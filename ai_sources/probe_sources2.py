#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二批：补测遗漏入口 + 国内 AI 实验室 + 会议/开放评审平台"""
import json, re, ssl
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from urllib.error import HTTPError

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

TARGETS = [
    # 大厂补充
    ("openai-index",      "https://openai.com/research/index/"),
    ("openai-rss",        "https://openai.com/news/rss.xml"),
    ("deepmind-research", "https://deepmind.google/research/"),
    ("google-pubs2",      "https://research.google/pubs"),
    ("meta-pub-search",   "https://ai.meta.com/results/?content_types[0]=publication"),
    ("meta-research",     "https://ai.meta.com/research/"),
    ("msr-feed",          "https://www.microsoft.com/en-us/research/feed/"),
    ("apple-rss",         "https://machinelearning.apple.com/rss.xml"),
    ("nvidia-labs",       "https://research.nvidia.com/labs/"),
    ("amazon-science",    "https://www.amazon.science/"),
    ("mit-ibm-watson",    "https://mitibmwatsonailab.mit.edu/research/publications/"),
    ("anthropic-eng",     "https://www.anthropic.com/engineering"),
    ("anthropic-news",    "https://www.anthropic.com/news"),
    # 模型公司补充
    ("mistral-rss",       "https://mistral.ai/news/rss"),
    ("hf-trending",       "https://huggingface.co/papers/trending"),
    ("hf-papers",         "https://huggingface.co/papers"),
    ("cohere-blog",       "https://cohere.com/blog"),
    ("stability-research","https://stability.ai/research"),
    ("xai",               "https://x.ai/"),
    ("salesforce-ai",     "https://www.salesforce.com/artificial-intelligence/"),
    ("databricks-blog",   "https://www.databricks.com/blog"),
    ("figure-news",       "https://www.figure.ai/news"),
    # 独立研究机构
    ("allenai-home",      "https://allenai.org/"),
    ("eleuther-home",     "https://www.eleuther.ai/"),
    ("eleuther-blog",     "https://blog.eleuther.ai/"),
    ("laion",             "https://laion.ai/blog/"),
    ("mlcommons",         "https://mlcommons.org/"),
    # 安全 / 评估 / 对齐
    ("aisi-uk",           "https://www.aisi.gov.uk/"),
    ("nist-aisi",         "https://www.nist.gov/aisi"),
    ("alignment-forum",   "https://www.alignmentforum.org/"),
    ("lesswrong",         "https://www.lesswrong.com/"),
    ("arc",               "https://alignment.org/"),
    ("timaeus",           "https://timaeus.co/"),
    ("control-ai",        "https://controlai.org/"),
    ("far-ai",            "https://far.ai/"),
    # 开放评审 / 会议
    ("openreview",        "https://openreview.net/"),
    ("neurips",           "https://neurips.cc/"),
    ("icml",              "https://icml.cc/"),
    ("iclr",              "https://iclr.cc/"),
    ("arxiv-cs-se",       "https://arxiv.org/list/cs.SE/recent"),
    # 国内
    ("shlab",             "https://www.shlab.org.cn/"),
    ("internvl",          "https://internvl.github.io/"),
    ("opencompass",       "https://opencompass.org.cn/"),
    ("modelscope",        "https://www.modelscope.cn/"),
    ("stepfun",           "https://www.stepfun.com/"),
    ("damo",              "https://www.damo-academy.com/"),
    ("kuaishou-kling",    "https://app.klingai.com/"),
    ("sensetime",         "https://www.sensetime.com/cn/business-detail?categoryId=59592"),
    ("baai-hub",          "https://hub.baai.ac.cn/"),
    ("minimaxi",          "https://www.minimaxi.com/"),
    ("thudm",             "https://github.com/THUDM"),
    ("moonshot-github",   "https://github.com/MoonshotAI"),
    ("deepseek-github",   "https://github.com/deepseek-ai"),
    ("qwen-github",       "https://github.com/QwenLM"),
    ("idm",               "https://www.idm-vc.com/"),
    ("ieit",              "https://www.ieisystem.com/"),
]


def fetch(url, timeout=18):
    req = Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    })
    with urlopen(req, timeout=timeout, context=CTX) as r:
        raw = r.read(300000)
        enc = "utf-8"
        m = re.search(rb'charset=["\']?([\w\-]+)', raw[:3000], re.I)
        if m:
            enc = m.group(1).decode("ascii", "ignore")
        return r.status, r.geturl(), raw.decode(enc, "ignore")


def probe(item):
    key, url = item
    rec = {"key": key, "url": url}
    try:
        status, final, html = fetch(url)
        m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        title = re.sub(r"\s+", " ", m.group(1)).strip()[:80] if m else ""
        rec.update(ok=(200 <= status < 400), status=status, final=final,
                   title=title, is_rss=("<rss" in html[:2000].lower()
                                        or "<feed" in html[:2000].lower()))
    except HTTPError as e:
        rec.update(ok=False, status=e.code, error=f"HTTP {e.code}")
    except Exception as e:
        rec.update(ok=False, status=0, error=f"{type(e).__name__}: {e}"[:110])
    return rec


if __name__ == "__main__":
    res = []
    with ThreadPoolExecutor(max_workers=14) as ex:
        futs = [ex.submit(probe, t) for t in TARGETS]
        for f in as_completed(futs):
            res.append(f.result())
    order = {t[0]: i for i, t in enumerate(TARGETS)}
    res.sort(key=lambda r: order.get(r["key"], 999))
    print(f"{'KEY':<20}{'ST':<6}{'TITLE / ERROR'}")
    print("-" * 110)
    for r in res:
        print(f"{r['key']:<20}{str(r.get('status')):<6}"
              f"{r.get('title','') or r.get('error','')}")
    with open("probe_result2.json", "w", encoding="utf-8") as fp:
        json.dump(res, fp, ensure_ascii=False, indent=2)
    print("\nsaved: probe_result2.json")
