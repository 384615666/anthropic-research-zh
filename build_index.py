# -*- coding: utf-8 -*-
"""
Generate a browsable HTML index of all downloaded Anthropic research papers.
Reads index.json and papers/*.md, outputs en.html with search & filter.

Note: 站点根目录的 index.html 是中文入口页（与 home.html 相同），
英文索引固定输出到 en.html，避免重建时覆盖首页。
"""
import os
import json
import re
import html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_JSON = os.path.join(BASE_DIR, "index.json")
PAPERS_DIR = os.path.join(BASE_DIR, "papers")
OUT_HTML = os.path.join(BASE_DIR, "en.html")


def get_excerpt(md_path, limit=200):
    try:
        txt = open(md_path, encoding="utf-8").read()
    except Exception:
        return ""
    # remove frontmatter
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            txt = parts[2]
    # remove header lines (title, date, category, source)
    lines = txt.splitlines()
    body = []
    started = False
    for ln in lines:
        if not started and ln.startswith("---"):
            started = True
            continue
        if started:
            body.append(ln)
    txt = "\n".join(body)
    txt = re.sub(r"[#*>`\-\[\]()!]", "", txt)
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt[:limit]


MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}


def date_key(datestr):
    """Convert 'Aug 10, 2026' or '2026-08-10' to a sortable tuple (year, month, day)."""
    d = (datestr or "").strip()
    m = re.match(r"^(\w{3})[a-z]*\s+(\d{1,2}),?\s+(\d{4})$", d)
    if m:
        return (int(m.group(3)), MONTHS.get(m.group(1), 0), int(m.group(2)))
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", d)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.match(r"^(\d{4})$", d)
    if m:
        return (int(m.group(1)), 0, 0)
    return (0, 0, 0)


def main():
    data = json.load(open(INDEX_JSON, encoding="utf-8"))
    papers = [p for p in data["papers"] if p.get("status") in ("ok", "cached")]
    papers.sort(key=lambda p: date_key(p.get("date", "")), reverse=True)

    categories = {}
    for p in papers:
        c = p.get("category") or "Uncategorized"
        categories.setdefault(c, 0)
        categories[c] += 1
    cat_str = ", ".join(f"{k} ({v})" for k, v in sorted(categories.items()))

    rows = []
    for p in papers:
        slug = p["slug"]
        md_path = os.path.join(PAPERS_DIR, slug + ".md")
        excerpt = get_excerpt(md_path)
        title = p.get("title") or slug.replace("-", " ").title()
        date = p.get("date", "")
        cat = p.get("category", "")
        rows.append(f"""
<tr>
  <td class="date">{html.escape(date)}</td>
  <td><span class="cat">{html.escape(cat)}</span></td>
  <td>
    <a class="ptitle" href="papers/{html.escape(slug)}.md" target="_blank">{html.escape(title)}</a>
    <div class="excerpt">{html.escape(excerpt)}…</div>
    <div class="links">
      <a href="papers/{html.escape(slug)}.md" target="_blank">本地 Markdown</a>
      <a href="{html.escape(p['url'])}" target="_blank">原文链接</a>
    </div>
  </td>
</tr>""")

    # top featured / hero section
    featured = papers[:4]
    hero_cards = []
    for p in featured:
        slug = p["slug"]
        title = p.get("title") or slug.replace("-", " ").title()
        excerpt = get_excerpt(os.path.join(PAPERS_DIR, slug + ".md"), 120)
        hero_cards.append(f"""
<div class="hero-card">
  <div class="hero-cat">{html.escape(p.get('category',''))}</div>
  <h3><a href="papers/{html.escape(slug)}.md">{html.escape(title)}</a></h3>
  <p>{html.escape(excerpt)}…</p>
  <div class="hero-date">{html.escape(p.get('date',''))}</div>
</div>""")

    total = len(papers)
    failed = data.get("failed", [])

    html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anthropic Research Papers — 本地镜像</title>
<style>
  :root {{
    --bg: #faf9f6;
    --card: #ffffff;
    --text: #1f1f1f;
    --muted: #6b6b6b;
    --accent: #c15f3c;
    --accent2: #cc7857;
    --border: #e8e4dc;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
  }}
  .header {{
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    color: #fff;
    padding: 48px 24px 40px;
    text-align: center;
  }}
  .header h1 {{ font-size: 32px; font-weight: 700; letter-spacing: -0.5px; }}
  .header h1 span {{ color: var(--accent2); }}
  .header p {{ color: #bbb; margin-top: 10px; font-size: 15px; }}
  .header .home {{
    display: inline-block; margin-bottom: 12px; color: #e6b4a0;
    text-decoration: none; font-size: 13px;
  }}
  .header .home:hover {{ text-decoration: underline; }}
  .stats {{
    display: flex; justify-content: center; gap: 24px; margin-top: 20px; flex-wrap: wrap;
  }}
  .stat {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 10px 22px; border-radius: 10px; font-size: 14px;
  }}
  .stat b {{ display: block; font-size: 22px; color: #fff; }}
  .container {{ max-width: 960px; margin: 0 auto; padding: 32px 20px 60px; }}
  .hero-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px; margin-bottom: 36px;
  }}
  .hero-card {{
    background: var(--card); border: 1px solid var(--border); border-radius: 12px;
    padding: 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }}
  .hero-card:hover {{ transform: translateY(-3px); box-shadow: 0 6px 18px rgba(0,0,0,0.08); }}
  .hero-cat {{
    display: inline-block; font-size: 11px; color: var(--accent);
    border: 1px solid var(--accent); border-radius: 20px; padding: 2px 10px;
    margin-bottom: 10px; letter-spacing: 0.5px;
  }}
  .hero-card h3 {{ font-size: 15px; margin-bottom: 8px; line-height: 1.4; }}
  .hero-card h3 a {{ color: var(--text); text-decoration: none; }}
  .hero-card h3 a:hover {{ color: var(--accent); }}
  .hero-card p {{ font-size: 13px; color: var(--muted); }}
  .hero-date {{ font-size: 12px; color: var(--muted); margin-top: 10px; }}
  .toolbar {{
    display: flex; gap: 12px; align-items: center; margin-bottom: 18px; flex-wrap: wrap;
  }}
  .toolbar input {{
    flex: 1; min-width: 200px; padding: 10px 14px; border: 1px solid var(--border);
    border-radius: 8px; font-size: 14px; background: var(--card);
  }}
  .toolbar select {{
    padding: 10px 14px; border: 1px solid var(--border); border-radius: 8px;
    font-size: 14px; background: var(--card); color: var(--text);
  }}
  table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 12px; overflow: hidden; }}
  th {{
    text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px;
    color: var(--muted); border-bottom: 1px solid var(--border); padding: 12px 14px;
  }}
  td {{ padding: 14px; border-bottom: 1px solid var(--border); vertical-align: top; }}
  tr:last-child td {{ border-bottom: none; }}
  td.date {{ white-space: nowrap; color: var(--muted); font-size: 13px; width: 90px; }}
  .cat {{
    display: inline-block; font-size: 11px; background: #f3efe7; color: #7a5c4a;
    border-radius: 20px; padding: 3px 10px; white-space: nowrap;
  }}
  .ptitle {{ font-weight: 600; color: var(--text); text-decoration: none; font-size: 15px; }}
  .ptitle:hover {{ color: var(--accent); }}
  .excerpt {{ font-size: 12.5px; color: var(--muted); margin-top: 4px; max-width: 560px; }}
  .links {{ margin-top: 6px; font-size: 12px; }}
  .links a {{ color: var(--accent); text-decoration: none; margin-right: 14px; }}
  .links a:hover {{ text-decoration: underline; }}
  .footer {{ text-align: center; color: var(--muted); font-size: 12px; padding: 24px; }}
  tr.hidden {{ display: none; }}
  .empty {{ text-align: center; padding: 40px; color: var(--muted); display: none; }}
</style>
</head>
<body>
<div class="header">
  <a class="home" href="index.html">&larr; 返回首页</a>
  <h1>Anthropic <span>Research Papers</span></h1>
  <p>Anthropic 官网研究论文本地镜像 — {total} 篇 · 更新于 2026-09-18</p>
  <div class="stats">
    <div class="stat"><b>{total}</b>论文总数</div>
    <div class="stat"><b>{len(categories)}</b>研究分类</div>
    <div class="stat"><b>{len(failed)}</b>失败</div>
  </div>
</div>
<div class="container">
  <div class="hero-grid">
    {"".join(hero_cards)}
  </div>
  <div class="toolbar">
    <input id="search" type="text" placeholder="🔍 搜索标题、摘要…" oninput="filterRows()">
    <select id="catFilter" onchange="filterRows()">
      <option value="">全部分类</option>
    </select>
  </div>
  <table>
    <thead><tr><th>日期</th><th>分类</th><th>标题</th></tr></thead>
    <tbody id="tbody">
      {"".join(rows)}
    </tbody>
  </table>
  <div class="empty" id="empty">没有匹配的结果</div>
</div>
<div class="footer">数据来源：https://www.anthropic.com/research · 仅供学习研究使用</div>
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
        f.write(html_doc)
    print(f"en.html generated: {total} papers, {len(categories)} categories")


if __name__ == "__main__":
    main()
