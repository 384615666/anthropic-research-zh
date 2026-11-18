# -*- coding: utf-8 -*-
"""
Rebuild papers_html/*.html — full Chinese pages.
Each page: 中文标题 → 完整中文摘要 → 术语注解 → 中文全文 → 英文原文（可折叠）
Uses summaries_all.json for Chinese summary block, papers_zh/*.md for full translation,
papers/*.md for English original.
"""

import markdown
import os
import re
import json
import html as H

BASE = os.path.dirname(os.path.abspath(__file__))
PAPERS = BASE + "/papers"
PAPERS_ZH = BASE + "/papers_zh"
OUT = BASE + "/papers_html"
os.makedirs(OUT, exist_ok=True)

data = json.load(open(BASE + "/summaries_all.json", encoding="utf-8"))
meta = {p["slug"]: p for p in data["papers"]}

CSS = """
body { font-family:-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; background:#faf9f6; color:#1f1f1f; line-height:1.85; margin:0; padding:0; }
.wrap { max-width: 800px; margin: 0 auto; padding: 36px 26px 90px; }
h1 { font-size: 27px; line-height:1.35; border-bottom: 2px solid #e8e4dc; padding-bottom: 14px; margin-bottom: 6px; }
.meta { color:#8a8575; font-size:13px; margin-bottom: 22px; }
.meta a { color:#c15f3c; text-decoration:none; }
.zh-block { background:#fff; border:1.5px solid #c15f3c; border-radius:14px; padding:20px 22px; margin:18px 0 24px; }
.zh-block h2 { color:#b5522f; font-size:18px; margin:0 0 10px; border:none; padding:0; }
.zh-summary { font-size:14.5px; color:#333; line-height:1.85; }
.zh-terms { margin-top:14px; }
.zh-terms h3 { font-size:14px; color:#7a4a30; margin:0 0 8px; }
.term { display:inline-block; background:#f6efe9; color:#7a4a30; border-radius:8px; padding:4px 10px; margin:3px 4px 3px 0; font-size:12.5px; }
.zh-full { background:#fff; border:1.5px solid #378ADD; border-radius:14px; padding:20px 24px; margin-bottom:28px; }
.zh-full > h2:first-child { color:#185FA5; font-size:18px; margin:0 0 12px; border:none; padding:0; }
.zh-full h1 { font-size:24px; border:none; }
.zh-full h2 { font-size:19px; color:#185FA5; margin-top:30px; border-left:4px solid #378ADD; padding-left:10px; }
.zh-full h3 { font-size:16px; color:#0C447C; margin-top:24px; }
.zh-full blockquote { background:#f3f7fb; border-left:4px solid #378ADD; color:#3a4a5a; }
.zh-en-toggle { margin:16px 0 4px; }
.zh-en-toggle summary { cursor:pointer; color:#888; font-size:13.5px; user-select:none; }
.zh-en-toggle summary:hover { color:#185FA5; }
h2 { font-size: 20px; color:#b5522f; margin-top: 40px; border-left: 4px solid #c15f3c; padding-left: 12px; }
h3 { font-size: 16px; margin-top: 26px; }
blockquote { background:#f3efe7; border-left: 4px solid #c15f3c; margin:14px 0; padding:10px 16px; border-radius:0 8px 8px 0; color:#5a4a3a; }
code { background:#f0ece4; padding:2px 6px; border-radius:4px; font-size:0.9em; }
pre { background:#f6f3ec; padding:14px; border-radius:8px; overflow-x:auto; }
pre code { background:none; padding:0; }
table { border-collapse:collapse; width:100%; margin:16px 0; background:#fff; border-radius:10px; overflow:hidden; }
th,td { border:1px solid #e8e4dc; padding:9px 13px; text-align:left; font-size:14px; }
th { background:#f6f2ea; }
img { max-width:100%; border-radius:8px; margin:10px 0; }
hr { border:none; border-top:1px solid #e8e4dc; margin:28px 0; }
.back { display:inline-block; margin-bottom:18px; color:#c15f3c; text-decoration:none; font-size:14px; }
.back:hover { text-decoration:underline; }
"""


def esc(s):
    return H.escape(s or "")


def clean_md_body(raw):
    """Strip frontmatter + leading duplicated title block, return body md."""
    body = raw
    if body.startswith("---"):
        parts = body.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
    body = re.sub(r"^#\s+.*\n", "", body, count=1)
    body = re.sub(r"\n(InterpretabilityResearch|AlignmentResearch|ResearchResearch|PolicyResearch)\n", "\n", body)
    body = re.sub(r"^-\s*\*\*日期：\*\*\s*$\n", "", body, flags=re.M)
    body = re.sub(r"^-\s*\*\*分类：\*\*\s*$\n", "", body, flags=re.M)
    body = re.sub(r"^-\s*\*\*类别：\*\*\s*$\n", "", body, flags=re.M)
    body = re.sub(r"^-\s*\*\*来源：\*\*\s*$\n", "", body, flags=re.M)
    body = re.sub(r"^-\s*\*\*Date:\*\*\s*$\n", "", body, flags=re.M)
    body = re.sub(r"^-\s*\*\*Category:\*\*\s*$\n", "", body, flags=re.M)
    body = re.sub(r"^-\s*\*\*Source:\*\*\s*$\n", "", body, flags=re.M)
    # 去除翻译文件里重复的标题行（# 中文标题 后紧跟的日期行等）
    body = re.sub(r"^---\s*$", "", body, flags=re.M)
    return body.strip()


def build_zh_block(p):
    terms_html = "".join(f'<span class="term">{esc(t)}</span>' for t in p.get("terms", []))
    return f"""
<div class="zh-block">
  <h2>📖 中文摘要</h2>
  <div class="zh-summary">{esc(p.get("summary_zh", ""))}</div>
  <div class="zh-terms">
    <h3>专业术语注解</h3>
    {terms_html}
  </div>
</div>"""


count = 0
zh_missing = []
for fn in sorted(os.listdir(PAPERS)):
    if not fn.endswith(".md"):
        continue
    slug = fn[:-3]
    raw = open(os.path.join(PAPERS, fn), encoding="utf-8").read()
    front = {}
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    front[k.strip()] = v.strip()
    title = front.get("title", slug)
    date = front.get("date", "")
    url = front.get("url", "")
    cat = front.get("category", "")
    p = meta.get(slug, {})
    zh_title = p.get("title_zh", "")

    # 中文全文
    zh_path = os.path.join(PAPERS_ZH, fn)
    zh_html = ""
    if os.path.exists(zh_path):
        zh_raw = open(zh_path, encoding="utf-8").read()
        zh_body = clean_md_body(zh_raw)
        # 去掉中文全文正文里的第一个 # 标题（页面顶部已有大标题，避免重复）
        zh_body = re.sub(r"^#\s+.+\n", "", zh_body, count=1)
        # 去掉紧跟标题的孤立日期行（如 '2022 年 9 月 14 日'）
        zh_body = re.sub(r"^\d{4} 年 \d{1,2} 月 \d{1,2} 日\n", "", zh_body, count=1)
        if zh_body:
            zh_html = markdown.markdown(zh_body, extensions=["tables", "fenced_code"])
    else:
        zh_missing.append(slug)

    # 英文原文
    en_body = clean_md_body(raw)
    en_html = markdown.markdown(en_body, extensions=["tables", "fenced_code"])

    zh_block = build_zh_block(p) if p.get("summary_zh") else ""
    zh_full = f"""<div class="zh-full">
<h2>📄 中文全文</h2>
{zh_html}
</div>""" if zh_html else '<div class="zh-full" style="border-color:#ccc"><h2 style="color:#999">📄 中文全文（暂无，请查看英文原文）</h2></div>'

    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<a class="back" href="../阅读路线.html">&larr; 返回阅读目录</a>
<h1>{esc(zh_title or title)}</h1>
<div class="meta">
{esc(title)} · {esc(date)} · {esc(cat)} · <a href="{esc(url)}" target="_blank">查看原文</a>
</div>
{zh_block}
{zh_full}
<details class="zh-en-toggle"><summary>▸ 英文原文（点击展开）</summary>
<div style="margin-top:14px">
{en_html}
</div>
</details>
</div>
</body>
</html>"""
    # 页面位于 papers_html/ 子目录，修正相对路径：图片、站内绝对链接
    doc = doc.replace('src="assets/', 'src="../assets/')
    # 若该图已做中文化（assets_zh/<slug>/<file> 存在），中文全文区优先引用中文版；
    # 英文原文折叠区必须保留原图，否则会出现「英文原文配中文图」的错位。
    def _prefer_zh(m):
        rel = m.group(1)
        if os.path.exists(os.path.join(BASE, "assets_zh", rel)):
            return 'src="../assets_zh/%s"' % rel
        # 中文化产物可能换了容器格式（如原图 webp、重绘后存 png），按同名不同扩展名兜底
        stem = os.path.splitext(rel)[0]
        for ext in (".png", ".webp", ".jpg", ".jpeg", ".gif", ".img"):
            alt = stem + ext
            if os.path.exists(os.path.join(BASE, "assets_zh", alt)):
                return 'src="../assets_zh/%s"' % alt
        return m.group(0)
    _cut = doc.find('<details')
    if _cut > 0:
        doc = re.sub(r'src="\.\./assets/([^"]+)"', _prefer_zh, doc[:_cut]) + doc[_cut:]
    else:
        doc = re.sub(r'src="\.\./assets/([^"]+)"', _prefer_zh, doc)
    for p in ("/research/", "/news/", "/claude"):
        doc = doc.replace('href="' + p, 'href="https://www.anthropic.com' + p)
    doc = doc.replace('href="anthropic.com/', 'href="https://www.anthropic.com/')

    open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8").write(doc)
    count += 1

print(f"rebuilt {count} pages (Chinese full text)")
print(f"中文全文缺失: {zh_missing if zh_missing else '无'}")
