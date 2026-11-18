# -*- coding: utf-8 -*-
"""
Merge summary_groupN.json files, join with index.json metadata,
and generate a Chinese index HTML with per-paper summaries and term annotations.
"""

import os
import json
import re
import html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUMMARIES_DIR = os.path.join(BASE_DIR, "summaries")
INDEX_JSON = os.path.join(BASE_DIR, "index.json")
OUT_HTML = os.path.join(BASE_DIR, "index_zh.html")
MERGED_JSON = os.path.join(BASE_DIR, "summaries_all.json")


def load_summaries():
    """合并 summaries/summary_group*.json（不限定分组数量，按编号排序）。"""
    import glob as _glob
    paths = _glob.glob(os.path.join(SUMMARIES_DIR, "summary_group*.json"))

    def num(p):
        m = re.search(r"(\d+)", os.path.basename(p))
        return int(m.group(1)) if m else 0

    all_papers = []
    for p in sorted(paths, key=num):
        d = json.load(open(p, encoding="utf-8"))
        all_papers.extend(d["papers"])
    return all_papers


def main():
    summaries = load_summaries()
    print(f"Loaded {len(summaries)} summaries")

    meta = json.load(open(INDEX_JSON, encoding="utf-8"))
    meta_by_slug = {p["slug"]: p for p in meta["papers"]}

    # merge
    merged = []
    missing = []
    for s in summaries:
        slug = s["slug"]
        m = meta_by_slug.get(slug, {})
        rec = {
            "slug": slug,
            "title_en": m.get("title", ""),
            "title_zh": s.get("title_zh", ""),
            "date": s.get("date") or m.get("date", ""),
            "category": s.get("category_zh") or m.get("category", ""),
            "url": f"papers_html/{slug}.html",  # 中文索引应跳转到本地翻译阅读页
            "summary_zh": s.get("summary_zh", ""),
            "terms": s.get("terms", []),
        }
        if not rec["summary_zh"]:
            missing.append(slug)
        merged.append(rec)

    # any slugs in meta not covered by summaries?
    sum_slugs = {r["slug"] for r in merged}
    meta_slugs = {p["slug"] for p in meta["papers"]}
    uncovered = meta_slugs - sum_slugs
    print(f"Merged {len(merged)}, missing summaries: {len(missing)}, uncovered: {len(uncovered)}")

    json.dump({"papers": merged}, open(MERGED_JSON, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # sort by date desc
    MONTHS = {m: i + 1 for i, m in enumerate(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}

    def date_key(d):
        d = (d or "").strip()
        m = re.match(r"^(\w{3})[a-z]*\s+(\d{1,2}),?\s+(\d{4})$", d)
        if m:
            return (int(m.group(3)), MONTHS.get(m.group(1), 0), int(m.group(2)))
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", d)
        if m:
            return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return (0, 0, 0)

    merged.sort(key=lambda r: date_key(r["date"]), reverse=True)

    # stats
    total = len(merged)
    term_count = sum(len(r["terms"]) for r in merged)
    cats = {}
    for r in merged:
        c = r["category"] or "其他"
        cats[c] = cats.get(c, 0) + 1
    cat_str = ", ".join(f"{k} {v}篇" for k, v in sorted(cats.items(), key=lambda x: -x[1]))

    # build rows
    rows = []
    for r in merged:
        terms_html = "".join(
            f'<span class="term"><b>{html.escape(t.split("：")[0].split(":")[0])}</b>：{html.escape(t.split("：",1)[-1] if "：" in t else t)}</span>'
            for t in r["terms"][:6]
        ) if r["terms"] else '<span class="term" style="background:#f2f2f2;color:#999">无专业术语</span>'
        rows.append(f"""
<tr>
  <td class="date">{html.escape(r['date'])}</td>
  <td><span class="cat">{html.escape(r['category'])}</span></td>
  <td>
    <div class="titles">
      <a class="ptitle" href="{html.escape(r['url'])}">{html.escape(r['title_zh'] or r['title_en'])}</a>
      {f'<div class="t-en">{html.escape(r["title_en"])}</div>' if r['title_zh'] and r['title_zh'] != r['title_en'] else ''}
    </div>
    <div class="summary">{html.escape(r['summary_zh'])}</div>
    <div class="terms">{terms_html}</div>
  </td>
</tr>""")

    featured = merged[:4]
    hero = []
    for r in featured:
        hero.append(f"""
<div class="hero-card">
  <div class="hero-cat">{html.escape(r['category'])}</div>
  <h3><a href="{html.escape(r['url'])}">{html.escape(r['title_zh'] or r['title_en'])}</a></h3>
  <p>{html.escape(r['summary_zh'][:100])}…</p>
  <div class="hero-date">{html.escape(r['date'])}</div>
</div>""")

    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anthropic 研究论文中文导读（{total}篇摘要+术语注解）</title>
<style>
  :root {{
    --bg: #faf9f6; --card: #fff; --text: #1f1f1f; --muted: #6b6b6b;
    --accent: #c15f3c; --border: #e8e4dc;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
    background: var(--bg); color: var(--text); line-height: 1.65; }}
  .header {{ background: linear-gradient(135deg,#1a1a1a,#2d2d2d); color:#fff;
    padding:48px 24px 40px; text-align:center; }}
  .header h1 {{ font-size:30px; font-weight:700; }}
  .header h1 span {{ color:#cc7857; }}
  .header p {{ color:#bbb; margin-top:10px; font-size:15px; }}
  .stats {{ display:flex; justify-content:center; gap:20px; margin-top:20px; flex-wrap:wrap; }}
  .stat {{ background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.15);
    padding:10px 20px; border-radius:10px; font-size:13px; }}
  .stat b {{ display:block; font-size:20px; color:#fff; }}
  .container {{ max-width:1000px; margin:0 auto; padding:32px 20px 60px; }}
  .hero-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
    gap:16px; margin-bottom:30px; }}
  .hero-card {{ background:var(--card); border:1px solid var(--border); border-radius:12px;
    padding:18px; transition:transform .15s,box-shadow .15s; }}
  .hero-card:hover {{ transform:translateY(-3px); box-shadow:0 6px 18px rgba(0,0,0,.08); }}
  .hero-cat {{ display:inline-block; font-size:11px; color:var(--accent);
    border:1px solid var(--accent); border-radius:20px; padding:2px 10px; margin-bottom:10px; }}
  .hero-card h3 {{ font-size:14.5px; margin-bottom:8px; line-height:1.4; }}
  .hero-card h3 a {{ color:var(--text); text-decoration:none; }}
  .hero-card h3 a:hover {{ color:var(--accent); }}
  .hero-card p {{ font-size:12.5px; color:var(--muted); }}
  .hero-date {{ font-size:12px; color:var(--muted); margin-top:10px; }}
  .toolbar {{ display:flex; gap:12px; margin-bottom:18px; flex-wrap:wrap; }}
  .toolbar input {{ flex:1; min-width:220px; padding:10px 14px; border:1px solid var(--border);
    border-radius:8px; font-size:14px; background:var(--card); }}
  .toolbar select {{ padding:10px 14px; border:1px solid var(--border); border-radius:8px;
    font-size:14px; background:var(--card); }}
  table {{ width:100%; border-collapse:collapse; background:var(--card);
    border-radius:12px; overflow:hidden; }}
  th {{ text-align:left; font-size:12px; text-transform:uppercase; letter-spacing:.8px;
    color:var(--muted); border-bottom:1px solid var(--border); padding:12px 14px; }}
  td {{ padding:14px; border-bottom:1px solid var(--border); vertical-align:top; }}
  tr:last-child td {{ border-bottom:none; }}
  td.date {{ white-space:nowrap; color:var(--muted); font-size:13px; width:86px; }}
  .cat {{ display:inline-block; font-size:11px; background:#f3efe7; color:#7a5c4a;
    border-radius:20px; padding:3px 10px; white-space:nowrap; }}
  .ptitle {{ font-weight:600; color:var(--text); text-decoration:none; font-size:15px; }}
  .ptitle:hover {{ color:var(--accent); }}
  .t-en {{ font-size:12px; color:#999; font-style:italic; margin-top:1px; }}
  .summary {{ font-size:13px; color:#444; margin-top:6px; }}
  .terms {{ margin-top:8px; display:flex; flex-wrap:wrap; gap:6px; }}
  .term {{ font-size:11.5px; background:#f6efe9; color:#7a4a30; border-radius:6px;
    padding:3px 8px; max-width:100%; }}
  .footer {{ text-align:center; color:var(--muted); font-size:12px; padding:24px; }}
  tr.hidden {{ display:none; }}
  .empty {{ text-align:center; padding:40px; color:var(--muted); display:none; }}
  .nav-links a {{ color:#cc7857; text-decoration:none; margin:0 8px; font-size:13px; }}
  .nav-links a:hover {{ text-decoration:underline; }}
</style>
</head>
<body>
<div class="header">
  <h1>Anthropic <span>研究论文中文导读</span></h1>
  <p>{total} 篇论文 · 中文标题翻译 + 摘要总结 + 专业术语注解 · 更新于 2026-09-18</p>
  <div class="nav-links">
    <a href="index.html">🏠 返回首页</a>
    <a href="AI术语讲解.html">📖 AI 核心术语讲解（预训练等）</a>
    <a href="en.html">📄 英文原文索引</a>
  </div>
  <div class="stats">
    <div class="stat"><b>{total}</b>论文</div>
    <div class="stat"><b>{len(cats)}</b>分类</div>
    <div class="stat"><b>{term_count}+</b>术语注解</div>
  </div>
</div>
<div class="container">
  <div class="hero-grid">{"".join(hero)}</div>
  <div class="toolbar">
    <input id="search" type="text" placeholder="🔍 搜索中文标题、摘要、术语…" oninput="filterRows()">
    <select id="catFilter" onchange="filterRows()">
      <option value="">全部分类</option>
    </select>
  </div>
  <table>
    <thead><tr><th>日期</th><th>分类</th><th>摘要与术语</th></tr></thead>
    <tbody id="tbody">{"".join(rows)}</tbody>
  </table>
  <div class="empty" id="empty">没有匹配的结果</div>
</div>
<div class="footer">数据来源：https://www.anthropic.com/research · 摘要为 AI 生成，仅供学习参考</div>
<script>
  function initCats() {{
    const seen = new Set();
    document.querySelectorAll(".cat").forEach(el => {{
      const c = el.textContent.trim();
      if (c && !seen.has(c)) {{
        seen.add(c);
        const opt = document.createElement("option");
        opt.value = c; opt.textContent = c;
        document.getElementById("catFilter").appendChild(opt);
      }}
    }});
  }}
  function filterRows() {{
    const q = document.getElementById("search").value.toLowerCase();
    const c = document.getElementById("catFilter").value;
    let shown = 0;
    document.querySelectorAll("#tbody tr").forEach(tr => {{
      const text = tr.textContent.toLowerCase();
      const cat = tr.querySelector(".cat").textContent.trim();
      const ok = (c === "" || cat === c) && (q === "" || text.includes(q));
      tr.classList.toggle("hidden", !ok);
      if (ok) shown++;
    }});
    document.getElementById("empty").style.display = shown === 0 ? "block" : "none";
  }}
  initCats();
</script>
</body>
</html>"""

    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"index_zh.html generated: {total} papers, {term_count} terms, cats: {len(cats)}")


if __name__ == "__main__":
    main()
