# -*- coding: utf-8 -*-
"""把 papers_zh/<slug>.md 的一级标题与 summaries_all.json 的 title_zh 对齐。

背景：阅读页的大标题取自标题库的 title_zh（见 rebuild_pages_zh.py 的 zh_title），
译文文件里的 `# 一级标题` 在页面上并不显示。两者措辞不一致时，会让维护者困惑，
因此统一以 title_zh 为准（它同时出现在中文导读页与阅读路线上）。

用法：
    python sync_zh_titles.py                 # 只处理 _new_papers_meta.json 中的新增篇目
    python sync_zh_titles.py <slug> [<slug>] # 处理指定篇目
    python sync_zh_titles.py --all           # 处理 papers_zh/ 下全部篇目
"""
import os
import re
import sys
import json

BASE = os.path.dirname(os.path.abspath(__file__))
PAPERS_ZH = os.path.join(BASE, "papers_zh")
SUMMARIES = os.path.join(BASE, "summaries_all.json")
META = os.path.join(BASE, "_new_papers_meta.json")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--all" in sys.argv:
        slugs = [f[:-3] for f in os.listdir(PAPERS_ZH) if f.endswith(".md")]
    elif args:
        slugs = args
    else:
        slugs = [r["slug"] for r in json.load(open(META, encoding="utf-8"))]

    titles = {p["slug"]: (p.get("title_zh") or "").strip()
              for p in json.load(open(SUMMARIES, encoding="utf-8"))["papers"]}

    changed = []
    missing = []
    for s in slugs:
        fp = os.path.join(PAPERS_ZH, s + ".md")
        if not os.path.exists(fp):
            missing.append(s)
            continue
        want = titles.get(s, "")
        if not want:
            missing.append(s + "（标题库无 title_zh）")
            continue
        txt = open(fp, encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", txt, re.M)
        if not m:
            missing.append(s + "（译文无一级标题）")
            continue
        old = m.group(1).strip()
        if old == want:
            continue
        txt = txt[:m.start(1)] + want + txt[m.end(1):]
        open(fp, "w", encoding="utf-8").write(txt)
        changed.append((s, old, want))

    print("检查 %d 篇，改动 %d 篇" % (len(slugs), len(changed)))
    for s, old, new in changed:
        print("  ~ %s" % s)
        print("      原: %s" % old)
        print("      新: %s" % new)
    if missing:
        print("跳过 %d 篇：%s" % (len(missing), "; ".join(missing)))


if __name__ == "__main__":
    main()
