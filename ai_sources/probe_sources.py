#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量探测 AI 实验室论文源的可达性 / 最终落地页 / 页面标题 / 是否提供 RSS·sitemap。
输出 probe_result.json + 控制台表格。"""
import json, re, ssl, sys, gzip, io
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

TARGETS = [
    # ---- 一线大厂 / 头部实验室 ----
    ("anthropic",        "https://www.anthropic.com/research",                   "厂商研究页"),
    ("openai-research",  "https://openai.com/research/",                         "厂商研究页"),
    ("openai-news",      "https://openai.com/news/",                             "厂商资讯页"),
    ("deepmind-pubs",    "https://deepmind.google/research/publications/",       "厂商论文库"),
    ("deepmind-blog",    "https://deepmind.google/discover/blog/",               "厂商研究博客"),
    ("google-pubs",      "https://research.google/pubs/",                        "厂商论文库"),
    ("googleblog",       "https://research.google/blog/",                        "厂商研究博客"),
    ("meta-ai-pubs",     "https://ai.meta.com/research/publications/",           "厂商论文库"),
    ("meta-ai-blog",     "https://ai.meta.com/blog/",                            "厂商研究博客"),
    ("msr-pubs",         "https://www.microsoft.com/en-us/research/publications/", "厂商论文库"),
    ("msr-blog",         "https://www.microsoft.com/en-us/research/blog/",       "厂商研究博客"),
    ("nvidia-research",  "https://research.nvidia.com/",                         "厂商论文库"),
    ("ibm-research",     "https://research.ibm.com/",                            "厂商研究页"),
    ("apple-ml",         "https://machinelearning.apple.com/research",           "厂商论文库"),
    ("amazon-science",   "https://www.amazon.science/blog",                      "厂商研究博客"),
    ("adobe-research",   "https://research.adobe.com/",                          "厂商研究页"),
    ("salesforce-research", "https://www.salesforce.com/research/",              "厂商研究页"),
    ("baidu-research",   "https://research.baidu.com/",                          "厂商研究页"),
    # ---- 新一代模型公司 ----
    ("mistral-news",     "https://mistral.ai/news",                              "模型公司资讯"),
    ("xai-news",         "https://x.ai/news",                                    "模型公司资讯"),
    ("cohere-research",  "https://cohere.com/research",                          "模型公司研究"),
    ("deepseek-docs-news","https://api-docs.deepseek.com/news/",                 "模型公司资讯"),
    ("qwen-blog",        "https://qwenlm.github.io/blog/",                       "模型公司研究博客"),
    ("seed-bytedance",   "https://seed.bytedance.com/en/",                       "模型公司研究"),
    ("minimax-news",     "https://www.minimax.io/news",                          "模型公司资讯"),
    ("moonshot",         "https://www.moonshot.cn/",                             "模型公司官网"),
    ("zhipu",            "https://www.zhipuai.cn/",                              "模型公司官网"),
    ("01ai",             "https://www.01.ai/",                                   "模型公司官网"),
    ("hunyuan",          "https://hunyuan.tencent.com/",                         "模型公司官网"),
    # ---- 开源 / 独立研究机构 ----
    ("allenai-papers",   "https://allenai.org/papers",                           "独立研究机构"),
    ("eleutherai-pubs",  "https://www.eleuther.ai/publications",                 "独立研究机构"),
    ("stability-news",   "https://stability.ai/news",                            "模型公司资讯"),
    ("sakana",           "https://sakana.ai/",                                   "模型公司研究"),
    ("reka",             "https://www.reka.ai/news",                             "模型公司资讯"),
    ("together-blog",    "https://www.together.ai/blog",                         "模型公司博客"),
    ("physicalintelligence", "https://www.physicalintelligence.company/blog",    "机器人公司博客"),
    # ---- 聚合渠道 ----
    ("hf-papers",        "https://huggingface.co/papers",                        "聚合渠道"),
    ("arxiv-cs-ai",      "https://arxiv.org/list/cs.AI/recent",                  "预印本"),
    ("arxiv-cs-cl",      "https://arxiv.org/list/cs.CL/recent",                  "预印本"),
    ("arxiv-cs-lg",      "https://arxiv.org/list/cs.LG/recent",                  "预印本"),
    ("paperswithcode",   "https://paperswithcode.com/",                          "聚合渠道"),
    ("semanticscholar",  "https://www.semanticscholar.org/",                     "聚合渠道"),
    ("alphaxiv",         "https://www.alphaxiv.org/",                            "聚合渠道"),
    # ---- 安全 / 评估 / 对齐机构 ----
    ("metr-blog",        "https://metr.org/blog",                                "评估机构"),
    ("epoch-publications","https://epoch.ai/publications",                       "评估机构"),
    ("apollo",           "https://www.apolloresearch.ai/",                       "安全机构"),
    ("redwood",          "https://www.redwoodresearch.org/research",             "安全机构"),
    ("transluce",        "https://transluce.org/",                               "可解释性公司"),
    ("goodfire",         "https://www.goodfire.ai/",                             "可解释性公司"),
    # ---- 学术机构 ----
    ("bair",             "https://bair.berkeley.edu/blog/",                      "学术机构"),
    ("stanford-hai",     "https://hai.stanford.edu/research",                    "学术机构"),
    ("mit-csail",        "https://www.csail.mit.edu/research",                   "学术机构"),
]


def fetch(url, timeout=20):
    req = Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
        "Accept-Encoding": "gzip",
    })
    with urlopen(req, timeout=timeout, context=CTX) as r:
        raw = r.read(400000)
        if r.headers.get("Content-Encoding") == "gzip":
            try:
                raw = gzip.decompress(raw)
            except Exception:
                pass
        enc = "utf-8"
        m = re.search(rb'charset=["\']?([\w\-]+)', raw[:3000], re.I)
        if m:
            enc = m.group(1).decode("ascii", "ignore")
        html = raw.decode(enc, "ignore")
        return r.status, r.geturl(), html


def title_of(html):
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not m:
        return ""
    t = re.sub(r"\s+", " ", m.group(1)).strip()
    return t[:110]


def probe(item):
    key, url, kind = item
    rec = {"key": key, "url": url, "kind": kind}
    try:
        status, final, html = fetch(url)
        rec.update(ok=(200 <= status < 400), status=status, final=final,
                   title=title_of(html), bytes=len(html))
        low = html.lower()
        rec["has_rss"] = ("rss" in low or "atom" in low or "feed" in low)
        rec["has_sitemap_ref"] = "sitemap" in low
        rec["has_arxiv_link"] = "arxiv.org" in low
        rec["has_pdf_link"] = ".pdf" in low
        # 估算页面上的链接数量，判断是否真的是列表页
        rec["link_count"] = len(re.findall(r"<a\s", low))
    except HTTPError as e:
        rec.update(ok=False, status=e.code, error=f"HTTP {e.code}",
                   final=getattr(e, "url", url))
    except Exception as e:
        rec.update(ok=False, status=0, error=f"{type(e).__name__}: {e}"[:150])
    return rec


def check_extra(base, paths):
    """探测常见订阅入口"""
    out = {}
    for p in paths:
        u = urljoin(base, p)
        try:
            req = Request(u, headers={"User-Agent": UA})
            with urlopen(req, timeout=12, context=CTX) as r:
                body = r.read(2000)
                out[p] = r.status
        except HTTPError as e:
            out[p] = e.code
        except Exception:
            out[p] = 0
    return out


if __name__ == "__main__":
    results = []
    with ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(probe, t): t for t in TARGETS}
        for f in as_completed(futs):
            results.append(f.result())

    order = {t[0]: i for i, t in enumerate(TARGETS)}
    results.sort(key=lambda r: order.get(r["key"], 999))

    print(f"{'KEY':<24}{'ST':<6}{'RSS':<5}{'ARX':<5}{'TITLE'}")
    print("-" * 130)
    for r in results:
        st = r.get("status", "ERR")
        print(f"{r['key']:<24}{str(st):<6}{'Y' if r.get('has_rss') else '-':<5}"
              f"{'Y' if r.get('has_arxiv_link') else '-':<5}"
              f"{r.get('title','')[:70] or r.get('error','')}")

    with open("probe_result.json", "w", encoding="utf-8") as fp:
        json.dump(results, fp, ensure_ascii=False, indent=2)

    print("\n===== 订阅入口探测 =====")
    extras = {
        "https://openai.com/": ["news/rss.xml", "index/rss.xml", "sitemap.xml"],
        "https://deepmind.google/": ["blog.xml", "sitemap.xml"],
        "https://research.google/": ["blog/rss/", "sitemap.xml"],
        "https://ai.meta.com/": ["rss/", "sitemap.xml"],
        "https://www.microsoft.com/en-us/research/": ["feed/", "sitemap.xml"],
        "https://mistral.ai/": ["rss.xml", "sitemap.xml"],
        "https://huggingface.co/": ["papers/rss", "papers/rss.xml"],
        "https://arxiv.org/": ["rss/cs.AI", "rss/cs.CL"],
        "https://www.anthropic.com/": ["rss.xml", "sitemap.xml"],
        "https://machinelearning.apple.com/": ["research.rss", "rss.xml"],
        "https://allenai.org/": ["rss.xml", "blog/rss.xml"],
        "https://bair.berkeley.edu/": ["blog/index.xml"],
    }
    sub = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(check_extra, b, ps): b for b, ps in extras.items()}
        for f in as_completed(futs):
            sub[futs[f]] = f.result()
    for b, res in sub.items():
        print(b)
        for p, code in res.items():
            print(f"    {p:<20} -> {code}")
    with open("probe_feeds.json", "w", encoding="utf-8") as fp:
        json.dump(sub, fp, ensure_ascii=False, indent=2)
    print("\nsaved: probe_result.json / probe_feeds.json")
