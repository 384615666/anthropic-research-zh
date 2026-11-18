#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为「推荐哪些源」提供数据支撑：
1) 统计 Anthropic 现有 157 篇的分类分布，找出覆盖缺口
2) 实测候选源能贡献多少条内容（条目数 + 研究类占比）
"""
import json, io, re, ssl, os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.error import HTTPError

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
HERE = os.path.dirname(os.path.abspath(__file__))


def get(url, timeout=25):
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read(2000000).decode("utf-8", "ignore")


# ---------- 1. Anthropic 覆盖分布 ----------
def anthropic_dist():
    p = os.path.join(HERE, "..", "anthropic_research", "index.json")
    d = json.load(io.open(p, encoding="utf-8"))
    c = Counter(x.get("category") or "(未分类)" for x in d["papers"])
    return d["papers"], c


# ---------- 2. 候选源内容量 ----------
def count_links(html, patterns):
    """按 URL 模式统计条目数（去重）"""
    hits = set()
    for href in re.findall(r'href="([^"#?]+)"', html):
        u = href.lower()
        for p in patterns:
            if p in u and u not in hits:
                hits.add(u)
    return len(hits)


def probe_source(item):
    name, url, patterns, note = item
    r = {"name": name, "url": url, "note": note}
    try:
        html = get(url)
        r["links"] = count_links(html, patterns)
        r["bytes"] = len(html)
        r["ok"] = True
        # 抓一些标题样本
        titles = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", html, re.S)
        clean = []
        for t in titles:
            t = re.sub(r"<[^>]+>", " ", t)
            t = re.sub(r"\s+", " ", t).strip()
            if 12 < len(t) < 130:
                clean.append(t)
        r["samples"] = clean[:5]
    except HTTPError as e:
        r.update(ok=False, err=f"HTTP {e.code}")
    except Exception as e:
        r.update(ok=False, err=f"{type(e).__name__}: {e}"[:80])
    return r


SOURCES = [
    ("METR", "https://metr.org/blog", ["/blog/"], "评估方法论"),
    ("Apollo Research", "https://www.apolloresearch.ai/", ["/research/", "/blog/"], "欺骗性对齐"),
    ("Redwood Research", "https://www.redwoodresearch.org/research", ["/research/"], "AI 控制"),
    ("Epoch AI", "https://epoch.ai/publications", ["/publications/", "/blog/"], "算力与趋势"),
    ("EleutherAI Blog", "https://blog.eleuther.ai/", ["/20", "/posts/"], "可解释性"),
    ("Qwen Blog", "https://qwenlm.github.io/blog/", ["/blog/"], "开源模型"),
    ("UK AISI", "https://www.aisi.gov.uk/", ["/research", "/publications", "/blog"], "国家级评测"),
    ("Timaeus", "https://timaeus.co/", ["/research", "/blog", "/posts"], "可解释性"),
    ("Transluce", "https://transluce.org/", ["/research", "/blog", "/updates"], "模型审计"),
    ("Goodfire", "https://www.goodfire.ai/", ["/research", "/blog", "/posts"], "SAE 工程化"),
    ("Sakana AI", "https://sakana.ai/", ["/blog/", "/research/"], "日本实验室"),
    ("Physical Intelligence", "https://www.physicalintelligence.company/blog", ["/blog/"], "机器人基础模型"),
]


def openai_rss_breakdown():
    """OpenAI RSS：总条目 + 按 URL 路径判定内容类型"""
    txt = get("https://openai.com/news/rss.xml")
    items = re.findall(r"<item\b.*?</item>", txt, re.S)
    cats = Counter()
    samples = {}
    for it in items:
        m = re.search(r"<link><!\[CDATA\[(.*?)\]\]></link>|<link>(.*?)</link>", it, re.S)
        link = (m.group(1) or m.group(2)).strip() if m else ""
        seg = link.rstrip("/").split("/")[-1] if link else ""
        # 用 URL 与标题关键词做粗分类
        mt = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
        title = re.sub(r"\s+", " ", mt.group(1)).strip() if mt else ""
        low = (link + " " + title).lower()
        if any(k in low for k in ["safety", "alignment", "preparedness", "red-team",
                                  "security", "governance", "misuse", "control"]):
            k = "安全/对齐/治理"
        elif any(k in low for k in ["economic", "signals", "research/research",
                                    "labor", "jobs", "productivity", "gdp"]):
            k = "经济研究"
        elif any(k in low for k in ["introducing", "gpt-", "o1", "o3", "sora",
                                    "dall", "whisper", "api", "chatgpt", "codex"]):
            k = "模型与产品发布"
        elif any(k in low for k in ["research", "paper", "study", "benchmark",
                                    "evaluation", "measuring"]):
            k = "研究论文"
        else:
            k = "公司/其他"
        cats[k] += 1
        samples.setdefault(k, []).append(title[:80])
    return len(items), cats, samples


if __name__ == "__main__":
    print("=" * 78)
    print("一、Anthropic 现有库覆盖分布（157 篇）")
    print("=" * 78)
    papers, dist = anthropic_dist()
    for k, v in dist.most_common():
        print(f"  {k:<28} {v:>4} 篇  {'█' * int(v / 2)}")
    print(f"  合计 {sum(dist.values())} 篇")

    print()
    print("=" * 78)
    print("二、候选源内容量实测")
    print("=" * 78)
    out = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(probe_source, s) for s in SOURCES]
        for f in as_completed(futs):
            out.append(f.result())
    order = {s[0]: i for i, s in enumerate(SOURCES)}
    out.sort(key=lambda r: order.get(r["name"], 99))
    for r in out:
        if r.get("ok"):
            print(f"  {r['name']:<24} 条目≈{r['links']:<5} ({r['url']})")
            for s in r.get("samples", [])[:3]:
                print(f"      · {s}")
        else:
            print(f"  {r['name']:<24} 失败：{r.get('err')}")

    print()
    print("=" * 78)
    print("三、OpenAI RSS 内容构成（1208 条全量）")
    print("=" * 78)
    try:
        total, cats, samples = openai_rss_breakdown()
        print(f"  总条目：{total}")
        for k, v in cats.most_common():
            print(f"  {k:<16} {v:>5} 条  ({v * 100 // total}%)")
        print()
        print("  各类标题样本：")
        for k in cats:
            if k in ("安全/对齐/治理", "经济研究", "研究论文"):
                print(f"  【{k}】")
                for s in samples.get(k, [])[:4]:
                    print(f"      · {s}")
    except Exception as e:
        print("  失败：", e)

    with io.open(os.path.join(HERE, "recommend_data.json"), "w", encoding="utf-8") as fp:
        json.dump({"anthropic_dist": dict(dist),
                   "sources": out}, fp, ensure_ascii=False, indent=2)
    print("\nsaved: recommend_data.json")
