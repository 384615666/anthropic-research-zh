# Anthropic 研究论文中文翻译站

Anthropic 官网研究论文（219 篇）的**中文全文翻译 + 配图中文化**站点，纯静态 HTML，无构建依赖。

## 在线访问（GitHub Pages）

| 入口 | 地址 |
|---|---|
| 首页（推荐） | https://384615666.github.io/anthropic-research-zh/ |
| 阅读路线 | https://384615666.github.io/anthropic-research-zh/阅读路线.html |
| 中文导读索引 | https://384615666.github.io/anthropic-research-zh/index_zh.html |
| 英文原版索引 | https://384615666.github.io/anthropic-research-zh/en.html |
| AI 术语讲解 | https://384615666.github.io/anthropic-research-zh/AI术语讲解.html |

推送到 `main` 分支后，GitHub Pages 会自动重新发布（通常 1–3 分钟），无需其它操作。

## 目录结构

```
.
├── index.html / home.html   # 首页（中文入口，两份内容相同，兼容旧链接）
├── en.html                  # 英文索引页（原 index.html）
├── index_zh.html            # 中文导读索引（摘要 + 术语，可搜索筛选）
├── 阅读路线.html             # ★ 推荐入口：按从易到难分 8 章的策展路线
├── AI术语讲解.html / .md     # AI 核心术语讲解
├── papers_html/             # 219 篇论文阅读页（中文优先 + 英文原文折叠）
├── papers_zh/               # 219 篇中文全文翻译（Markdown 源文件）
├── papers/                  # 219 篇英文原文（Markdown）
├── assets/                  # 英文原文配图（按论文分目录）
├── assets_zh/               # 中文化配图
├── ai_sources/              # 论文来源导航页与源清单
├── summaries/               # 各分组的摘要 / 术语 JSON
├── index.json               # 论文元数据（标题 / 日期 / 分类 / URL）
└── *.py                     # 抓取、翻译校验、页面重建脚本
```

`.nojekyll` 用于让 GitHub Pages 原样发布静态文件（跳过 Jekyll 处理）。
`_imgwork/`（配图处理中间产物）已在 `.gitignore` 中排除，不参与发布。

## 本地预览

```bat
python serve.py            :: 默认 8000 端口
python serve.py 9000       :: 指定端口
```

也可直接双击 `start.bat`。局域网内其它设备用 `http://<本机 IP>:8000/` 访问。

> 图片有 555 个以 `.img` 扩展名存储（内容是 webp/png/jpg），本地由 `serve.py` 按文件魔数嗅探并返回正确的 Content-Type。

## 论文库更新流程

| 步骤 | 脚本 | 作用 |
|---|---|---|
| 1 | `python check_new_papers.py --meta` | 对比官网 sitemap 与本地 `research_urls.txt`，列出新增篇目（有新增时退出码 1，可加 `--append` 回写清单） |
| 2 | `python scrape_new_papers.py` | 抓取新增篇目的英文原文与配图（先把 slug 填进脚本的 `SLUGS`） |
| 3 | `python merge_new_papers.py` | 把抓取结果合并进 `index.json`，按 slug 去重 |
| 4 | 翻译 | `papers/<slug>.md` → `papers_zh/<slug>.md`（规范见 `翻译质量检查提示词.md`） |
| 5 | `python validate_translations.py` | 译文质量预扫描：frontmatter、链接数、图片路径、重复字、未翻译段落、结尾截断 |
| 6 | `build_index_zh.py` → `rebuild_pages_zh.py` → `build_reading_route.py` → `build_index.py` | 依次重建 `summaries_all.json` + `index_zh.html`、`papers_html/`、`阅读路线.html`、`en.html`（顺序不能颠倒，最后一步把结果写入 `en.html`） |

抓取与重建脚本依赖：`requests`、`beautifulsoup4`、`html2text`、`lxml`、`markdown`。

摘要与术语写在 `summaries/summary_groupN.json`，`build_index_zh.py` 会自动合并全部 `summary_group*.json`。
新增论文后记得把 slug 补进 `build_reading_route.py` 的 `route` 章节，否则该篇会落到「其他（未归入主线）」区。

## 免责声明

本站为个人学习用途的中文翻译镜像。原文版权归 **Anthropic** 所有，与研究内容相关的权利以官方页面（https://www.anthropic.com/research）为准。中文译文由 AI 辅助翻译并经人工校对，仅供参考；关键结论请以英文原文为准。
