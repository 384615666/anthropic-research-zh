# -*- coding: utf-8 -*-
"""
Post-process downloaded papers:
1. Remove team pages (slug like alignment/economic-research/... from /research/team/)
2. Fill empty dates by extracting from body text
3. Rebuild index.json
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(BASE_DIR, "papers")
INDEX_JSON = os.path.join(BASE_DIR, "index.json")

TEAM_SLUGS = {
    "alignment", "economic-research", "frontier-red-team",
    "interpretability", "societal-impacts", "team",
}

DATE_PATTERNS = [
    r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4})",
    r"(\d{1,2} \w+ \d{4})",
    r"(\d{4}-\d{2}-\d{2})",
]


def extract_date_from_body(text):
    # look in first 3000 chars of body (after frontmatter/header)
    head = text[:4000]
    for pat in DATE_PATTERNS:
        m = re.search(pat, head)
        if m:
            return m.group(1)
    return ""


def main():
    index = json.load(open(INDEX_JSON, encoding="utf-8"))
    papers = index["papers"]
    kept = []
    removed = []
    for p in papers:
        slug = p["slug"]
        if slug in TEAM_SLUGS:
            removed.append(slug)
            md = os.path.join(PAPERS_DIR, slug + ".md")
            if os.path.exists(md):
                os.remove(md)
            continue
        md_path = os.path.join(PAPERS_DIR, slug + ".md")
        if os.path.exists(md_path):
            content = open(md_path, encoding="utf-8").read()
            # fill date from body if missing
            if not p.get("date"):
                d = extract_date_from_body(content)
                if d:
                    p["date"] = d
                    # also rewrite frontmatter date line
                    content2 = re.sub(r"^date:\s*$", f"date: {d}", content, count=1, flags=re.M)
                    content2 = re.sub(r"^\*\*Date:\*\*\s*$", f"**Date:** {d}", content2, count=1, flags=re.M)
                    if content2 != content:
                        open(md_path, "w", encoding="utf-8").write(content2)
            # title: prefer the H1 from frontmatter title if empty
            if not p.get("title"):
                m = re.search(r"^title:\s*(.+)$", content, re.M)
                if m:
                    p["title"] = m.group(1).strip()
        kept.append(p)

    kept.sort(key=lambda p: p.get("date", ""), reverse=True)
    new_index = {"count": len(kept), "failed": index.get("failed", []), "papers": kept}
    json.dump(new_index, open(INDEX_JSON, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"Kept: {len(kept)}, Removed team pages: {len(removed)} -> {removed}")
    empty_dates = [p["slug"] for p in kept if not p.get("date")]
    print(f"Papers still without date: {len(empty_dates)}")
    for s in empty_dates[:30]:
        print("  ", s)


if __name__ == "__main__":
    main()
