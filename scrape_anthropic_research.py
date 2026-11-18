# -*- coding: utf-8 -*-
"""
Scrape all Anthropic research papers from anthropic.com/research.
- Reads the URL list from sitemap.xml (already saved) or a local list file.
- For each paper page, extracts the <article> content and converts to Markdown.
- Saves markdown files under papers/<slug>.md
- Saves metadata to index.json
- Downloads inline images to papers/assets/<slug>/
"""

import os
import re
import json
import time
import sys
import html as html_lib
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
import html2text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(BASE_DIR, "papers")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
INDEX_JSON = os.path.join(BASE_DIR, "index.json")
URLS_TXT = os.path.join(BASE_DIR, "research_urls.txt")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)

# html2text config
H2T = html2text.HTML2Text()
H2T.ignore_links = False
H2T.body_width = 0  # no wrapping
H2T.ignore_images = False
H2T.ignore_emphasis = False
H2T.protect_links = True
H2T.unicode_snob = True
H2T.single_line_break = True


def get_slugs():
    """Extract article slugs from sitemap.xml."""
    sitemap = os.path.join(BASE_DIR, "sitemap.xml")
    xml = open(sitemap, encoding="utf-8").read()
    urls = re.findall(r"<loc>(https://www\.anthropic\.com/research/[^<]+)</loc>", xml)
    slugs = []
    for u in urls:
        # /research/team/<name> 是团队介绍页，不是论文，需按路径排除
        # （旧逻辑用 slug != "team" 判断，会漏掉 alignment/economics 等团队页）
        if "/research/team/" in u:
            continue
        slug = u.rstrip("/").split("/")[-1]
        if slug:
            slugs.append((slug, u))
    # dedupe, keep order
    seen = set()
    out = []
    for s, u in slugs:
        if s not in seen:
            seen.add(s)
            out.append((s, u))
    return out


def fetch_page(url, retries=3):
    for i in range(retries):
        try:
            r = SESSION.get(url, timeout=60)
            r.raise_for_status()
            return r.text
        except Exception as e:
            print(f"  fetch error ({i+1}/{retries}): {e}", flush=True)
            time.sleep(3 * (i + 1))
    return None


def extract_article(html_text):
    """Extract <article> element, return (title, date, category, article_html)."""
    soup = BeautifulSoup(html_text, "lxml")
    article = soup.find("article")
    if not article:
        return None
    # title: h1 in article, fallback to og:title
    h1 = article.find("h1")
    title = h1.get_text(strip=True) if h1 else None
    if not title:
        og = soup.find("meta", property="og:title")
        title = og.get("content", "").strip() if og else ""
    # date: try meta published_time first
    date = ""
    meta_pub = soup.find("meta", property="article:published_time") or \
               soup.find("meta", property="og:published_time")
    if meta_pub and meta_pub.get("content"):
        date = meta_pub["content"][:10]
    if not date:
        time_tag = soup.find("time")
        date = time_tag.get_text(strip=True) if time_tag else ""
    if not date:
        # fallback: first standalone date-like line in article text
        txt = article.get_text()
        m = re.search(r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4})", txt)
        if m:
            date = m.group(1)
    # category: 官网改版后放在 <article><header> 的 <dt>Team</dt><dd><a>…</a></dd>
    # 旧逻辑（找 meta/header div 里的第一个 span）会抓到「Copy」按钮或空值/日期，
    # 导致整批论文 category 失真，故改为按 dt 标签精确读取。
    category = ""
    for dt in article.find_all("dt"):
        if dt.get_text(strip=True).lower() == "team":
            dd = dt.find_next_sibling("dd") or (dt.parent.find("dd") if dt.parent else None)
            if dd:
                a = dd.find("a")
                category = (a.get_text(strip=True) if a else dd.get_text(" ", strip=True))
            break
    if not category:
        meta = article.find("div", class_=re.compile(r"meta|header"))
        if meta:
            sp = meta.find("span")
            if sp:
                category = sp.get_text(strip=True)
    return title, date, category, article


def clean_html_for_md(article):
    """Remove nav-like elements from article before markdown conversion."""
    for sel in ["nav", "footer", "button", "form", ".pagination", "script", "style"]:
        for el in article.select(sel):
            el.decompose()
    return article


def download_images(article, slug, html_text):
    """Download <img> srcs from the article to assets/<slug>/ and rewrite to relative paths."""
    soup = BeautifulSoup(str(article), "lxml")
    imgs = soup.find_all("img")
    if not imgs:
        return str(soup), []
    slug_asset_dir = os.path.join(ASSETS_DIR, slug)
    os.makedirs(slug_asset_dir, exist_ok=True)
    saved = []
    for i, img in enumerate(imgs):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        if src.startswith("data:"):
            continue
        if not src.startswith("http"):
            src = "https://www.anthropic.com" + src
        try:
            rr = SESSION.get(src, timeout=30)
            if rr.status_code != 200:
                continue
            ext = os.path.splitext(urlparse(src).path)[1].lower()
            ctype = rr.headers.get("Content-Type", "")
            if ext not in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"):
                if "png" in ctype:
                    ext = ".png"
                elif "jpeg" in ctype or "jpg" in ctype:
                    ext = ".jpg"
                elif "svg" in ctype:
                    ext = ".svg"
                elif "webp" in ctype:
                    ext = ".webp"
                else:
                    ext = ".img"
            fname = f"img_{i:03d}{ext}"
            fpath = os.path.join(slug_asset_dir, fname)
            with open(fpath, "wb") as f:
                f.write(rr.content)
            img["src"] = f"assets/{slug}/{fname}"
            saved.append(fpath)
        except Exception as e:
            print(f"  img error {src[:60]}: {e}", flush=True)
    return str(soup), saved


def process_one(entry, idx, total):
    slug, url = entry
    md_path = os.path.join(PAPERS_DIR, slug + ".md")
    if os.path.exists(md_path) and os.path.getsize(md_path) > 500:
        # skip only if the cached file already has a non-empty date in frontmatter
        cached = open(md_path, encoding="utf-8").read()
        if re.search(r"^date:\s*\S", cached, re.M):
            print(f"[{idx}/{total}] skip existing: {slug}", flush=True)
            return {"slug": slug, "url": url, "status": "cached"}
        print(f"[{idx}/{total}] re-fetch (missing date): {slug}", flush=True)
    print(f"[{idx}/{total}] fetching: {slug}", flush=True)
    page_html = fetch_page(url)
    if not page_html:
        print(f"  FAILED to fetch {slug}", flush=True)
        return {"slug": slug, "url": url, "status": "failed", "why": "fetch failed"}
    parsed = extract_article(page_html)
    if not parsed:
        print(f"  no article found for {slug}", flush=True)
        return {"slug": slug, "url": url, "status": "failed", "why": "no article"}
    title, date, category, article = parsed
    article = clean_html_for_md(article)

    # rewrite image URLs and download
    article_html_str, imgs = download_images(article, slug, page_html)

    # convert to markdown
    article_soup = BeautifulSoup(article_html_str, "lxml")
    md = H2T.handle(str(article_soup))
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    # build final markdown with frontmatter
    header = f"""---
title: {title}
url: {url}
date: {date}
category: {category}
source: https://www.anthropic.com/research
---

# {title}

- **Date:** {date}
- **Category:** {category}
- **Source:** {url}

---
"""
    full_md = header + "\n" + md + "\n"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"  OK: {title[:60]} ({len(md)} chars)", flush=True)
    return {
        "slug": slug, "url": url, "title": title, "date": date,
        "category": category, "status": "ok", "images": len(imgs),
    }


def main():
    os.makedirs(PAPERS_DIR, exist_ok=True)
    entries = get_slugs()
    print(f"Found {len(entries)} research articles", flush=True)

    results = []
    failed = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(process_one, e, i, len(entries)): e
                for i, e in enumerate(entries, 1)}
        for fut in as_completed(futs):
            r = fut.result()
            results.append(r)
            if r.get("status") == "failed":
                failed.append((r["slug"], r["url"], r.get("why", "")))

    with open(INDEX_JSON, "w", encoding="utf-8") as f:
        json.dump({"count": len(results), "failed": failed, "papers": results},
                  f, ensure_ascii=False, indent=2)

    print("\n==== DONE ====")
    print(f"Total entries: {len(entries)}")
    print(f"OK: {len([r for r in results if r.get('status')=='ok'])}")
    print(f"Cached: {len([r for r in results if r.get('status')=='cached'])}")
    print(f"Failed: {len(failed)}")
    for slug, url, why in failed:
        print(f"  - {slug}: {why}")


if __name__ == "__main__":
    main()
