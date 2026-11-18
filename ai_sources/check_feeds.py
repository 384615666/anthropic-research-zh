#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证「声称可直接订阅」的几个源能否真正解析出条目。
判断标准：能取到 item/entry 数量 + 最新条目标题 + 日期字段。
"""
import re, ssl, json, io
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

FEEDS = [
    ("OpenAI News",        "https://openai.com/news/rss.xml"),
    ("Microsoft Research", "https://www.microsoft.com/en-us/research/feed/"),
    ("Apple ML Research",  "https://machinelearning.apple.com/rss.xml"),
    ("arXiv cs.CL",        "https://arxiv.org/rss/cs.CL"),
    ("arXiv cs.AI",        "https://arxiv.org/rss/cs.AI"),
    ("Anthropic (对照)",   "https://www.anthropic.com/rss.xml"),
    ("DeepMind (对照)",    "https://deepmind.google/blog.xml"),
    ("BAIR Blog",          "https://bair.berkeley.edu/blog/feed.xml"),
    ("HF Papers (对照)",   "https://huggingface.co/papers/rss"),
]


def probe(item):
    name, url = item
    r = {"name": name, "url": url}
    try:
        req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        with urlopen(req, timeout=20, context=CTX) as resp:
            raw = resp.read(1200000)
            r["http"] = resp.status
            r["ctype"] = resp.headers.get("Content-Type", "")
            txt = raw.decode("utf-8", "ignore")
            r["format"] = ("json-feed" if txt.lstrip().startswith("{")
                           else "atom" if "<feed" in txt[:2000]
                           else "rss" if "<rss" in txt[:2000] or "<channel" in txt[:3000]
                           else "unknown")
            if r["format"] == "json-feed":
                d = json.loads(txt)
                items = d.get("items", [])
                r["count"] = len(items)
                if items:
                    r["latest"] = items[0].get("title", "")[:70]
                    r["date"] = items[0].get("date_published", "")[:19]
            else:
                entries = re.findall(r"<(?:item|entry)\b.*?</(?:item|entry)>", txt, re.S)
                r["count"] = len(entries)
                if entries:
                    m = re.search(r"<title[^>]*>(.*?)</title>", entries[0], re.S)
                    if m:
                        t = re.sub(r"<!\[CDATA\[|\]\]>", "", m.group(1))
                        r["latest"] = re.sub(r"\s+", " ", t).strip()[:70]
                    m2 = re.search(r"<(?:pubDate|published|updated)>([^<]+)<", entries[0])
                    if m2:
                        r["date"] = m2.group(1).strip()[:19]
    except Exception as e:
        r["http"] = 0
        r["error"] = f"{type(e).__name__}: {e}"[:90]
    return r


if __name__ == "__main__":
    out = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(probe, f) for f in FEEDS]
        for f in as_completed(futs):
            out.append(f.result())
    order = {f[0]: i for i, f in enumerate(FEEDS)}
    out.sort(key=lambda x: order[x["name"]])

    ok, bad = [], []
    for r in out:
        good = r.get("count", 0) > 0
        (ok if good else bad).append(r)
        print(f"[{'OK ' if good else 'FAIL'}] {r['name']:<20} http={r.get('http')} "
              f"fmt={r.get('format','-'):<10} 条目={r.get('count','-')}")
        if good:
            print(f"        最新：{r.get('latest','')}")
            print(f"        日期：{r.get('date','(无日期字段)')}")
        elif r.get("error"):
            print(f"        错误：{r['error']}")
        elif r.get("count") == 0:
            print(f"        正文前 120 字：{r.get('ctype','')} / 无法解析出条目")

    print(f"\n可解析：{len(ok)} / {len(out)}")
    with io.open("feed_check.json", "w", encoding="utf-8") as fp:
        json.dump(out, fp, ensure_ascii=False, indent=2)
