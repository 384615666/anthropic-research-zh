# -*- coding: utf-8 -*-
"""
检查 Anthropic 官网研究目录是否有新增论文。

做法：实时拉取 https://www.anthropic.com/sitemap.xml，抽出所有 /research/ 页面
（排除 /research/team/ 团队介绍页），与本地库存做双向差集。

本地库存以 index.json 为准，并与 research_urls.txt 取并集——历史上出现过
「论文已入库但 URL 清单没写回」的情况，只看 txt 会把已收录的篇目误报成新增。

用法：
    python check_new_papers.py            # 只列 URL
    python check_new_papers.py --meta     # 额外抓取标题与发布日期
    python check_new_papers.py --append   # 把新增 URL 追加进 research_urls.txt
    python check_new_papers.py --sync     # 把 index.json 中缺失的 URL 补写回清单

退出码：0 = 无新增，1 = 有新增。
"""
import os
import re
import sys
import json
import html as html_lib
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URLS_TXT = os.path.join(BASE_DIR, "research_urls.txt")
INDEX_JSON = os.path.join(BASE_DIR, "index.json")
SITEMAP_URL = "https://www.anthropic.com/sitemap.xml"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "en-US,en;q=0.9"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")


def load_local():
    urls = set()
    if os.path.exists(URLS_TXT):
        with open(URLS_TXT, encoding="utf-8") as f:
            urls |= {ln.strip().rstrip("/") for ln in f if ln.strip()}
    if os.path.exists(INDEX_JSON):
        with open(INDEX_JSON, encoding="utf-8") as f:
            data = json.load(f)
        urls |= {p["url"].rstrip("/") for p in data.get("papers", []) if p.get("url")}
    return urls


def sync_urls_from_index():
    """把 index.json 里已收录、但 URL 清单遗漏的条目补写回 research_urls.txt。"""
    with open(INDEX_JSON, encoding="utf-8") as f:
        idx_urls = {p["url"].rstrip("/") for p in json.load(f).get("papers", []) if p.get("url")}
    with open(URLS_TXT, encoding="utf-8") as f:
        txt_urls = {ln.strip().rstrip("/") for ln in f if ln.strip()}
    missing = sorted(idx_urls - txt_urls)
    if missing:
        with open(URLS_TXT, "a", encoding="utf-8", newline="\n") as f:
            # 原清单末尾可能没有换行，不先补一个会把两条 URL 粘成畸形行
            with open(URLS_TXT, "rb") as raw:
                raw.seek(-1, os.SEEK_END)
                if raw.read(1) != b"\n":
                    f.write("\n")
            for u in missing:
                f.write(u + "\n")
    print("已从 index.json 补写 %d 条 URL 到 research_urls.txt（清单现共 %d 条）"
          % (len(missing), len(txt_urls) + len(missing)))
    return missing


def fetch_meta(url):
    """返回 (url, title, date)。日期取自页面上唯一的 'Mon DD, YYYY' 样式文本。"""
    try:
        html = fetch(url)
    except Exception as e:
        return url, "(抓取失败: %s)" % e, ""
    m = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]*)"', html)
    if not m:
        m = re.search(r'<meta[^>]+content="([^"]*)"[^>]+property="og:title"', html)
    title = m.group(1).strip() if m else ""
    title = html_lib.unescape(title)
    dates = re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? \d{1,2}, \d{4}\b", html)
    return url, title, (dates[0] if dates else "")


def main():
    want_meta = "--meta" in sys.argv
    want_append = "--append" in sys.argv

    if "--sync" in sys.argv:
        sync_urls_from_index()

    try:
        xml = fetch(SITEMAP_URL)
    except Exception as e:
        print("无法获取 sitemap: %s" % e)
        return 2

    remote = set()
    for u in re.findall(r"<loc>(https://www\.anthropic\.com/research/[^<]+)</loc>", xml):
        u = u.rstrip("/")
        if "/research/team/" in u:
            continue
        remote.add(u)

    local = load_local()
    # 官网曾把 /research/long-running-Claude 改成全小写 /research/long-running-claude，
    # 属于同一篇文章的 URL 规范化。Windows 文件系统大小写不敏感，不做归一化会
    # 把它误报成「新增一篇 + 下架一篇」，进而产生同名文件互相覆盖。
    def norm(u):
        return u.rstrip("/").lower()

    remote_by_key = {norm(u): u for u in remote}
    local_keys = {norm(u) for u in local}
    added = [remote_by_key[k] for k in sorted(set(remote_by_key) - local_keys)]
    removed = sorted(u for u in local if norm(u) not in remote_by_key)

    print("官网 research 页面（已排除 team 页）: %d" % len(remote))
    print("本地库存（index.json + URL 清单）  : %d" % len(local))
    print()

    if not added:
        print("=== 无新增论文 ===")
    else:
        print("=== 新增 %d 篇 ===" % len(added))
        if want_meta:
            with ThreadPoolExecutor(max_workers=6) as ex:
                metas = list(ex.map(fetch_meta, added))
            metas.sort(key=lambda r: (r[2] or ""), reverse=False)
            for url, title, date in metas:
                print("  [%s] %s" % (date or "日期未知", url.rsplit("/", 1)[-1]))
                print("        %s" % title)
        else:
            for u in added:
                print("  + %s" % u)

    if removed:
        print()
        print("=== 本地有、官网已无 %d 条（可能下架或改名）===" % len(removed))
        for u in removed:
            print("  - %s" % u)

    if want_append and added:
        with open(URLS_TXT, "a", encoding="utf-8") as f:
            for u in added:
                f.write(u + "\n")
        print()
        print("已追加 %d 条到 research_urls.txt" % len(added))

    return 1 if added else 0


if __name__ == "__main__":
    sys.exit(main())
