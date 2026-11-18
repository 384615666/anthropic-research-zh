# -*- coding: utf-8 -*-
"""抓取指定的新增论文（复用 scrape_anthropic_research 的解析与图片下载逻辑）。

只处理 SLUGS 列表，不会触碰库内已有篇目；元数据另存 _new_papers_meta.json，
不直接覆盖 index.json（避免原有元数据丢失）。
"""
import os
import sys
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
import scrape_anthropic_research as S

SLUGS = [
    "building-strong-safety-evaluations",
]


def work(item):
    i, slug = item
    url = "https://www.anthropic.com/research/" + slug
    try:
        return S.process_one((slug, url), i, len(SLUGS))
    except Exception as e:
        return {"slug": slug, "url": url, "status": "failed", "why": repr(e)}


def main():
    results = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(work, it) for it in enumerate(SLUGS, 1)]
        for f in as_completed(futs):
            results.append(f.result())

    order = {s: i for i, s in enumerate(SLUGS)}
    results.sort(key=lambda r: order.get(r["slug"], 99))

    with open(os.path.join(BASE, "_new_papers_meta.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n==== 抓取结果 ====")
    for r in results:
        st = r.get("status")
        print("  [%s] %-58s date=%s imgs=%s %s" % (
            st, r["slug"], r.get("date", ""), r.get("images", ""), r.get("why", "")))
    ok = [r for r in results if r.get("status") == "ok"]
    print("成功 %d / %d" % (len(ok), len(results)))


if __name__ == "__main__":
    main()
