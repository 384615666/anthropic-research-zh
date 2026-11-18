#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""读取 sources.json，生成：
  1) AI论文源清单.md    —— 人读版清单
  2) 论文源导航.html    —— 可搜索/筛选/点击直达的导航页
用法：python build_sources_page.py
"""
import json, html, io, os
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "sources.json")

CAT_LABEL = {
    "frontier-lab":   ("一线实验室", "Google/Meta/微软/苹果等大厂研究院"),
    "model-company":  ("模型公司", "OpenAI/Anthropic/Mistral/国产大模型等"),
    "nonprofit":      ("独立研究机构", "AI2/EleutherAI/上海AI Lab 等"),
    "safety":         ("安全 · 评估 · 对齐", "与 Anthropic 主线最互补"),
    "aggregator":     ("聚合与发现渠道", "arXiv/HuggingFace/评审平台"),
    "academic":       ("学术机构", "Berkeley/MIT/Stanford 等"),
}

STATUS_LABEL = {
    "ok":      ("可直抓", "ok"),
    "blocked": ("需绕过反爬", "warn"),
    "proxy":   ("需境外网络", "proxy"),
    "dead":    ("已停止服务", "dead"),
}

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "已收录": 3, "仅供参考": 4}


def load():
    with io.open(SRC, encoding="utf-8") as f:
        return json.load(f)


def sort_key(s):
    return (PRIORITY_ORDER.get(s.get("priority", "P2"), 9), s["org"])


# ---------------- Markdown ----------------
def build_md(data):
    L = []
    L.append("# 前沿 AI 实验室论文源清单\n")
    L.append(f"> 核查日期：{data['generated_at']}　|　实测方式：{data['probe_method']}\n")
    L.append("> 目的：为 Anthropic 论文库（145 篇）补充其他前沿机构的论文来源。\n")

    L.append("## 状态说明\n")
    L.append("| 标记 | 含义 |")
    L.append("|---|---|")
    for k, (label, _) in STATUS_LABEL.items():
        desc = data["status_legend"][k]
        if label in desc:
            desc = {"ok": "实测 HTTP 200，可直接抓取",
                    "blocked": "实测 403/429，有反爬策略；浏览器或带正常 UA+Referer 可访问，抓取需降速或换通道",
                    "proxy": "本机代理隧道 502，需具备境外网络可达性才能抓取；地址本身有效",
                    "dead": "站点已下线，仅存归档数据"}[k]
        L.append(f"| {label} | {desc} |")
    L.append("")

    L.append("## 优先级说明\n")
    L.append("- **P0**：论文密度高、与 Anthropic 主题互补、抓取可行 → 建议优先接入")
    L.append("- **P1**：有价值，但需要绕反爬或走代理，或方向偏窄")
    L.append("- **P2**：补充参考，更新频率或相关度较低\n")

    by_cat = {}
    for s in data["sources"]:
        by_cat.setdefault(s["category"], []).append(s)
    for s in by_cat.values():
        s.sort(key=sort_key)

    L.append("## 总览\n")
    L.append("| 分类 | 数量 | 代表机构 |")
    L.append("|---|---|---|")
    for c, (label, desc) in CAT_LABEL.items():
        items = by_cat.get(c, [])
        if not items:
            continue
        seen, rep = set(), []
        for x in items:
            if x["org"] not in seen:
                seen.add(x["org"])
                rep.append(x["org"])
            if len(rep) == 4:
                break
        L.append(f"| {label} | {len(items)} | {'、'.join(rep)} … |")
    L.append("")

    for c, (label, desc) in CAT_LABEL.items():
        items = by_cat.get(c)
        if not items:
            continue
        L.append(f"## {label}\n")
        L.append(f"*{desc}*\n")
        for s in items:
            st = STATUS_LABEL[s["status"]][0]
            L.append(f"### {s['org']}　`{s.get('priority','P2')}`　`{st}`\n")
            L.append(f"- **论文入口**：<{s['list_url']}>")
            if s.get("alt_urls"):
                L.append(f"- **并列入口**：" + "　".join(f"<{u}>" for u in s["alt_urls"]))
            if s.get("rss"):
                mark = "　✅ 实测可解析出条目" if s.get("rss_verified") else ""
                L.append(f"- **订阅**：<{s['rss']}>{mark}")
            if s.get("sitemap"):
                L.append(f"- **站点地图**：<{s['sitemap']}>")
            if s.get("http_status"):
                L.append(f"- **实测状态码**：`{s['http_status']}`")
            if s.get("topics"):
                L.append(f"- **主题**：{'、'.join(s['topics'])}")
            L.append(f"- **说明**：{s['note']}")
            L.append("")

    L.append("## 落地建议\n")
    L.append("### 〇、推荐接入顺序（基于实测数据，非经验判断）\n")
    L.append("先看现有 157 篇的分布，判断缺口在哪：\n")
    L.append("| 分类 | 篇数 | | 分类 | 篇数 |")
    L.append("|---|---|---|---|---|")
    L.append("| Alignment | 43 | | Science | 10 |")
    L.append("| Interpretability | 31 | | Policy | 9 |")
    L.append("| Frontier Red Team | 22 | | Engineering | 2 |")
    L.append("| Societal Impacts | 19 | | Evaluations | 1 |")
    L.append("| Economic Research | 15 | | 其余 | 4 |")
    L.append("")
    L.append("**强项是对齐（43）、可解释性（31）、红队（22）——全是 Anthropic 自己的视角。真正的缺口是「第三方评估」和「竞对对照」。** 所以推荐按下面的顺序补，而不是按机构名气补。\n")
    L.append("#### 第一梯队：建议立刻接入\n")
    L.append("**1. METR — 29 篇，可直抓**")
    L.append("- 本批外部源中体量最大、主题最对口的一个。")
    L.append("- 它是第三方评估机构，与库内 22 篇前沿红队论文逐篇对话；而 Anthropic 的评估类论文多为自评，正好补上外部视角。")
    L.append("- 技术上门槛最低：列表页直连 200，无反爬、无代理需求。\n")
    L.append("**2. OpenAI 安全线 — 142 篇候选（需从 1208 条中过滤）**")
    L.append("- 唯一能提供竞对对照的源。GPT 系列系统卡、安全框架、模型误对齐报告框架，可与 Anthropic 的同名文档直接对读。")
    L.append("- **但必须过滤**：实测 1208 条里安全/对齐 74 条（6%）、经济研究 36 条（2%）、研究论文 32 条（2%），其余 87% 是产品发布与公司动态。不做过滤直接入库会把库的纯度拉垮。")
    L.append("- 抓取走 RSS（直连 200），不需要绕网页端的 403。\n")
    L.append("**3. arXiv 机构白名单 — 底网**")
    L.append("- 所有厂商的技术报告最终都会落到 arXiv，这是唯一不会漏的通道。")
    L.append("- 但不要全抓：cs.CL 日更 171 条、cs.AI 304 条。建议按作者单位关键词（OpenAI、Anthropic、Google DeepMind、Meta、Qwen、DeepSeek…）过滤后再入库。\n")
    L.append("#### 第二梯队：按兴趣选\n")
    L.append("**4. 可解释性外部视角 — Goodfire 12 + Timaeus 9 + EleutherAI**")
    L.append("- 库内 31 篇可解释性论文全部是 Anthropic 自己的 circuits 路线。这三家提供不同方法论：Goodfire 的 SAE 工程化、Timaeus 的物理启发方法、EleutherAI 的可组合干预。适合做「同一问题的不同解法」对照阅读。\n")
    L.append("**5. 定量与经济 — Epoch AI + Stanford HAI**")
    L.append("- 补 Economic Index 系列的第三方数据面。Epoch AI 的算力趋势与数据墙研究是定量支撑，Stanford HAI 的年度 AI Index 是同类议题的对照组。\n")
    L.append("#### 不建议接入\n")
    L.append("- **NVIDIA / Adobe / IBM / Amazon**：议题不对口（硬件、视觉编辑、企业 IT），翻译 ROI 低。")
    L.append("- **MIT / Stanford / Berkeley 等学术机构**：论文量巨大但质量参差，缺乏明确的筛选标准，会把库变成摘要堆。\n")
    L.append("### 一、可直接接入的订阅源（已实测能解析出条目）\n")
    L.append("| 源 | 订阅地址 | 实测结果 |")
    L.append("|---|---|---|")
    L.append("| OpenAI | `https://openai.com/news/rss.xml` | 返回 **1208 条**，日期完整，最新 2026-09-17 |")
    L.append("| arXiv cs.AI | `https://arxiv.org/rss/cs.AI` | 单次 **304 条**，日更 |")
    L.append("| arXiv cs.CL | `https://arxiv.org/rss/cs.CL` | 单次 **171 条**，日更 |")
    L.append("| Apple ML Research | `https://machinelearning.apple.com/rss.xml` | 10 条，含 pubDate，最新 2026-09-17 |")
    L.append("| Microsoft Research | `https://www.microsoft.com/en-us/research/feed/` | 10 条，最新 2026-08-31 |")
    L.append("| Berkeley BAIR | `https://bair.berkeley.edu/blog/feed.xml` | 10 条，最新 2026-07-29 |")
    L.append("")
    L.append("**其中最重要的一条发现**：OpenAI 网页端虽然返回 403 反爬，但 `news/rss.xml` 直连即可拿到 1208 条历史条目。这意味着 OpenAI 是整个清单里**最容易接、且能一次性回溯全量**的源，不需要做反爬绕过。\n")
    L.append("### 二、需要解析列表页的源（无 RSS）\n")
    L.append("Anthropic 自身的 `rss.xml` 与 DeepMind 的 `blog.xml` 实测均返回 **404**——两家都没有官方订阅通道，只能依赖 `sitemap.xml` 或列表页分页。Google Research pubs、Meta AI publications 同样无公开 RSS。这几个源的抓取成本明显高于上面的订阅源，建议复用在 Anthropic 上已经跑通的 sitemap 方案。\n")
    L.append("### 三、主题互补性最强的推荐组合\n")
    L.append("Anthropic 论文的强项是**对齐、可解释性、风险评估、AI 经济影响**。要形成完整议题，建议按组补：")
    L.append("- **对齐与评估**：METR + Apollo Research + Redwood Research（这三家的评测方法与 Anthropic 的 sabotage-evaluations、sleeper-agents 系列直接对话）")
    L.append("- **可解释性**：EleutherAI + Timaeus + Goodfire（与 Anthropic 的 circuits / monosemanticity 路线形成对照）")
    L.append("- **定量与算力**：Epoch AI（与 Anthropic Economic Index 形成数据互补）")
    L.append("- **中文语境补位**：上海人工智能实验室（InternVL / OpenCompass）、字节 Seed、阿里 Qwen——这三家的中文技术解读最稀缺，翻译价值最高")
    L.append("")
    L.append("### 四、执行成本提示\n")
    L.append("- **优先级 P0 但状态为「需境外网络」的源**（Google Research、Meta AI、Hugging Face、Mistral、xAI）：地址有效，但抓取需要具备境外网络可达性，建议评估后再排期。")
    L.append("- **状态为「需绕过反爬」的源**（OpenAI 网页端、NVIDIA labs、AI2、MLCommons）：403 是 UA/频率策略，降速 + 真实 UA 通常可解。")
    L.append("- **版权**：多数实验室采用 CC BY-NC 或自定义条款，公开发布翻译前需逐一核对许可。arXiv 预印本相对宽松，但也要保留原文出处与作者署名。")
    L.append("")
    L.append("## 已失效或需注意的源\n")
    L.append("- **Papers with Code**：2025-07-24 被 Meta 关停，域名已重定向到 Hugging Face Trending Papers，按任务组织的 SOTA 榜单能力无同类替代。")
    L.append("- **百度研究院**：页面维持「网站维护中」状态，长期停更。")
    L.append("- **Meta 旧站 research.fb.com**：仍在线，但内容停留在 2022 年前后，勿作为活跃源。")
    L.append("")

    out = os.path.join(HERE, "AI论文源清单.md")
    with io.open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    return out


# ---------------- HTML ----------------
def esc(t):
    return html.escape(t or "", quote=True)


def build_html(data):
    by_cat = {}
    for s in data["sources"]:
        by_cat.setdefault(s["category"], []).append(s)
    for v in by_cat.values():
        v.sort(key=sort_key)

    total = len(data["sources"])
    ok_n = sum(1 for s in data["sources"] if s["status"] == "ok")
    p0_n = sum(1 for s in data["sources"] if s.get("priority") == "P0")
    rss_n = sum(1 for s in data["sources"] if s.get("rss_verified"))

    cards = []
    for c, (label, desc) in CAT_LABEL.items():
        items = by_cat.get(c)
        if not items:
            continue
        inner = []
        for s in items:
            slabel, scls = STATUS_LABEL[s["status"]]
            pri = s.get("priority", "P2")
            links = [f'<a class="lnk main" href="{esc(s["list_url"])}" target="_blank" rel="noopener">{esc(s["list_url"].replace("https://", "").rstrip("/"))}</a>']
            for u in s.get("alt_urls", []):
                links.append(f'<a class="lnk" href="{esc(u)}" target="_blank" rel="noopener">{esc(u.replace("https://", ""))}</a>')
            if s.get("rss"):
                vbadge = '<span class="vbadge">解析通过</span>' if s.get("rss_verified") else ""
                links.append(f'<a class="lnk rss" href="{esc(s["rss"])}" target="_blank" rel="noopener">RSS {esc(s["rss"].replace("https://", ""))}</a>{vbadge}')
            if s.get("sitemap"):
                links.append(f'<a class="lnk" href="{esc(s["sitemap"])}" target="_blank" rel="noopener">sitemap</a>')
            topics = "".join(f'<span class="tag">{esc(t)}</span>' for t in s.get("topics", []))
            statuscode = f'<span class="code">{s["http_status"]}</span>' if s.get("http_status") else ""
            inner.append(f"""      <article class="card" data-status="{s['status']}" data-pri="{esc(pri)}" data-search="{esc((s['org'] + ' ' + ' '.join(s.get('topics', [])) + ' ' + s['note']).lower())}">
        <div class="card-head">
          <h3>{esc(s['org'])}</h3>
          <div class="badges"><span class="pri pri-{esc(pri)}">{esc(pri)}</span><span class="st {scls}">{esc(slabel)}</span>{statuscode}</div>
        </div>
        <div class="links">{''.join(links)}</div>
        <div class="tags">{topics}</div>
        <p class="note">{esc(s['note'])}</p>
      </article>""")
        cards.append(f"""  <section class="group" data-cat="{c}">
    <header class="group-head">
      <h2>{esc(label)}<span class="cnt">{len(items)}</span></h2>
      <p>{esc(desc)}</p>
    </header>
{chr(10).join(inner)}
  </section>""")

    cat_opts = "".join(
        f'<button class="fbtn" data-f="{c}">{esc(CAT_LABEL[c][0])}</button>'
        for c in CAT_LABEL if by_cat.get(c)
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>前沿 AI 实验室论文源导航</title>
<style>
  :root {{
    --bg:#f7f8fa; --panel:#ffffff; --line:#e5e7eb; --line2:#eef0f3;
    --ink:#14161a; --ink2:#4b5563; --ink3:#8a9099;
    --ok:#0f9d58; --okbg:#e8f6ee;
    --warn:#b7791f; --warnbg:#fdf6e3;
    --proxy:#b45309; --proxybg:#fdf0e3;
    --dead:#6b7280; --deadbg:#f1f2f4;
    --accent:#c0392b; --accentbg:#fdeeeb;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--bg); color:var(--ink);
    font-family:-apple-system,"Segoe UI","Microsoft YaHei","PingFang SC",sans-serif;
    font-size:14px; line-height:1.6; -webkit-font-smoothing:antialiased;
  }}
  .wrap {{ max-width:1180px; margin:0 auto; padding:34px 22px 70px; }}
  header.top {{ margin-bottom:22px; }}
  h1 {{ font-size:25px; margin:0 0 8px; letter-spacing:-.3px; }}
  .sub {{ color:var(--ink2); font-size:13.5px; margin:0; }}
  .stats {{ display:flex; gap:26px; margin:18px 0 22px; flex-wrap:wrap; }}
  .stat b {{ font-size:21px; font-weight:600; display:block; line-height:1.2; }}
  .stat span {{ color:var(--ink3); font-size:12px; }}
  .toolbar {{
    position:sticky; top:0; z-index:20; background:rgba(247,248,250,.93);
    backdrop-filter:blur(8px); padding:12px 0; border-bottom:1px solid var(--line);
    display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-bottom:24px;
  }}
  #q {{
    flex:1 1 240px; min-width:200px; padding:9px 13px; border:1px solid var(--line);
    border-radius:9px; font-size:13.5px; background:#fff; color:var(--ink); outline:none;
  }}
  #q:focus {{ border-color:#c9ccd1; box-shadow:0 0 0 3px rgba(0,0,0,.04); }}
  .fbtn {{
    padding:8px 13px; border:1px solid var(--line); background:#fff; color:var(--ink2);
    border-radius:8px; font-size:13px; cursor:pointer; transition:all .14s; font-family:inherit;
  }}
  .fbtn:hover {{ border-color:#c9ccd1; color:var(--ink); }}
  .fbtn.on {{ background:var(--ink); color:#fff; border-color:var(--ink); }}
  .group {{ margin-bottom:38px; }}
  .group-head h2 {{
    font-size:16.5px; margin:0 0 3px; display:flex; align-items:center; gap:9px;
  }}
  .cnt {{
    font-size:11.5px; font-weight:400; color:var(--ink3); background:#eceef1;
    border-radius:20px; padding:1px 9px;
  }}
  .group-head p {{ margin:0 0 15px; color:var(--ink3); font-size:12.5px; }}
  .card {{
    background:var(--panel); border:1px solid var(--line); border-radius:11px;
    padding:15px 17px; margin-bottom:10px; transition:box-shadow .16s,border-color .16s;
  }}
  .card:hover {{ border-color:#d8dade; box-shadow:0 3px 14px rgba(16,20,30,.055); }}
  .card-head {{ display:flex; justify-content:space-between; align-items:flex-start; gap:12px; flex-wrap:wrap; }}
  .card-head h3 {{ margin:0; font-size:15px; font-weight:600; letter-spacing:-.1px; }}
  .badges {{ display:flex; gap:6px; align-items:center; flex-shrink:0; }}
  .pri {{ font-size:11px; padding:2px 8px; border-radius:5px; font-weight:600; letter-spacing:.2px; }}
  .pri-P0 {{ background:var(--accentbg); color:var(--accent); }}
  .pri-P1 {{ background:#eef2fb; color:#3b5bdb; }}
  .pri-P2 {{ background:#f2f3f5; color:#6b7280; }}
  .pri-已收录 {{ background:#e8f6ee; color:var(--ok); }}
  .pri-仅供参考 {{ background:#f2f3f5; color:#9aa0a6; }}
  .st {{ font-size:11.5px; padding:2px 9px; border-radius:5px; white-space:nowrap; }}
  .st.ok {{ background:var(--okbg); color:var(--ok); }}
  .st.warn {{ background:var(--warnbg); color:var(--warn); }}
  .st.proxy {{ background:var(--proxybg); color:var(--proxy); }}
  .st.dead {{ background:var(--deadbg); color:var(--dead); }}
  .code {{ font-size:11px; font-family:ui-monospace,Consolas,monospace; color:var(--ink3); }}
  .links {{ margin:10px 0 9px; display:flex; flex-wrap:wrap; gap:6px 8px; }}
  .lnk {{
    font-size:12.5px; color:#3b5bdb; text-decoration:none;
    font-family:ui-monospace,Consolas,monospace; border-bottom:1px solid transparent;
    word-break:break-all;
  }}
  .lnk:hover {{ border-bottom-color:#3b5bdb; }}
  .lnk.main {{ font-weight:600; color:var(--accent); }}
  .lnk.main:hover {{ border-bottom-color:var(--accent); }}
  .lnk.rss {{ color:var(--ok); }}
  .lnk.rss:hover {{ border-bottom-color:var(--ok); }}
  .vbadge {{
    font-size:10.5px; color:var(--ok); background:var(--okbg); border-radius:4px;
    padding:1px 6px; vertical-align:1px; white-space:nowrap;
  }}
  .tags {{ display:flex; flex-wrap:wrap; gap:5px; margin-bottom:8px; }}
  .tag {{ font-size:11px; color:var(--ink2); background:#f3f4f6; border-radius:5px; padding:2px 7px; }}
  .note {{ margin:0; color:var(--ink2); font-size:13px; }}
  .hidden {{ display:none !important; }}
  .empty {{ color:var(--ink3); padding:40px 0; text-align:center; }}
  footer {{ margin-top:44px; padding-top:20px; border-top:1px solid var(--line); color:var(--ink3); font-size:12.5px; }}
  footer a {{ color:var(--ink2); }}
</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <h1>前沿 AI 实验室论文源导航</h1>
    <p class="sub">为 Anthropic 论文库补充的扩展源清单　·　核查日期 {data['generated_at']}　·　状态码为实测值</p>
    <div class="stats">
      <div class="stat"><b>{total}</b><span>收录源</span></div>
      <div class="stat"><b>{ok_n}</b><span>可直接抓取</span></div>
      <div class="stat"><b>{p0_n}</b><span>P0 优先接入</span></div>
      <div class="stat"><b>{rss_n}</b><span>RSS 已验证可解析</span></div>
      <div class="stat"><b>{len(by_cat)}</b><span>分类</span></div>
    </div>
  </header>

  <div class="toolbar">
    <input id="q" type="search" placeholder="搜索机构名 / 主题 / 说明，例如「可解释性」「arXiv」「RSS」">
    <button class="fbtn on" data-f="all">全部</button>
    {cat_opts}
    <button class="fbtn" data-f="__ok">仅可直抓</button>
    <button class="fbtn" data-f="__p0">仅 P0</button>
  </div>

{chr(10).join(cards)}
  <div class="empty hidden" id="empty">没有匹配的源</div>

  <footer>
    <p>状态说明：<b>可直抓</b> = 实测 200；<b>需绕过反爬</b> = 403/429，浏览器可访问；<b>需境外网络</b> = 本机代理隧道 502，地址有效但不具备直连条件；<b>已停止服务</b> = 站点下线。</p>
    <p>数据文件：<code>sources.json</code>　·　生成脚本：<code>build_sources_page.py</code>　·　探测脚本：<code>probe_sources.py</code> / <code>probe_sources2.py</code></p>
  </footer>
</div>

<script>
(function () {{
  var q = document.getElementById('q');
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.group'));
  var btns = Array.prototype.slice.call(document.querySelectorAll('.fbtn'));
  var empty = document.getElementById('empty');
  var filter = 'all';

  function apply() {{
    var kw = q.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (c) {{
      var okKw = !kw || c.dataset.search.indexOf(kw) > -1;
      var okF = true;
      if (filter === '__ok') okF = c.dataset.status === 'ok';
      else if (filter === '__p0') okF = c.dataset.pri === 'P0';
      else if (filter !== 'all') okF = c.closest('.group').dataset.cat === filter;
      var vis = okKw && okF;
      c.classList.toggle('hidden', !vis);
      if (vis) shown++;
    }});
    groups.forEach(function (g) {{
      var any = g.querySelector('.card:not(.hidden)');
      g.classList.toggle('hidden', !any);
    }});
    empty.classList.toggle('hidden', shown > 0);
  }}

  q.addEventListener('input', apply);
  btns.forEach(function (b) {{
    b.addEventListener('click', function () {{
      btns.forEach(function (x) {{ x.classList.remove('on'); }});
      b.classList.add('on');
      filter = b.dataset.f;
      apply();
    }});
  }});
}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    data = load()
    md = build_md(data)
    ht = os.path.join(HERE, "论文源导航.html")
    with io.open(ht, "w", encoding="utf-8") as f:
        f.write(build_html(data))
    print("OK")
    print("  " + md)
    print("  " + ht)
    print(f"  共 {len(data['sources'])} 个源")
