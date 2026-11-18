# -*- coding: utf-8 -*-
"""把 _new_papers_meta.json（scrape_new_papers.py 的产出）合并进 index.json。

index.json 结构：{"count": N, "failed": [], "papers": [{slug,url,title,date,category,status,images}]}
按 slug 去重；已存在的条目用新数据补齐缺失字段，不重复追加。
"""
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, "index.json")
NEW = os.path.join(BASE, "_new_papers_meta.json")


def main():
    idx = json.load(open(INDEX, encoding="utf-8"))
    papers = idx.get("papers", [])
    by_slug = {p["slug"]: p for p in papers}

    new = json.load(open(NEW, encoding="utf-8"))
    added, updated = 0, 0
    for r in new:
        if r.get("status") != "ok":
            print("  跳过（抓取未成功）:", r.get("slug"), r.get("why", ""))
            continue
        slug = r["slug"]
        if slug in by_slug:
            for k in ("title", "date", "category", "url", "images"):
                if r.get(k) and not by_slug[slug].get(k):
                    by_slug[slug][k] = r[k]
            updated += 1
        else:
            papers.append({
                "slug": slug,
                "url": r["url"],
                "title": r.get("title", ""),
                "date": r.get("date", ""),
                "category": r.get("category", ""),
                "status": "ok",
                "images": r.get("images", 0),
            })
            added += 1

    out = {"count": len(papers), "failed": idx.get("failed", []), "papers": papers}
    json.dump(out, open(INDEX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("index.json 已更新：新增 %d 条，补齐 %d 条，总计 %d 条" % (added, updated, len(papers)))


if __name__ == "__main__":
    main()
