# -*- coding: utf-8 -*-
"""译文质量预扫描：对照 papers/<slug>.md 检查 papers_zh/<slug>.md。

检查项（对应本项目历史审校中真实出现过的缺陷）：
  1. 译文存在且非空
  2. frontmatter 的 title/url/date/category 与原文一致（title 允许保留英文）
  3. Markdown 链接数量一致，且全部为半角括号闭合
  4. 图片引用数量与路径一致
  5. 段落数（非空行数）与原文接近
  6. 重复字：的的/为为/被被动/作为为/了了/是是/在在/和和/与与
  7. 疑似未翻译的整段英文
  8. 结尾完整性（最后一段不应以半个词结束）

用法：python validate_translations.py [slug ...]
      不带参数则检查 _new_papers_meta.json 里的全部新增篇目。
"""
import os
import re
import sys
import json

BASE = os.path.dirname(os.path.abspath(__file__))
PAPERS = os.path.join(BASE, "papers")
PAPERS_ZH = os.path.join(BASE, "papers_zh")
META = os.path.join(BASE, "_new_papers_meta.json")

DUP_WORDS = ["的的", "为为", "被被动", "作为为", "了了", "是是", "在在", "和和", "与与", "并并且"]
# 中文里合法出现的组合，检测前先剔除，避免误报
#   为目的的 —— 「以……为目的的使用方式」
#   为了了解 —— 「为了了解……」
#   旨在在   —— 「旨在在三个领域……」
DUP_WHITELIST = ["为目的的", "为了了解", "旨在在", "以……为目的的",
                 "实实在在", "确确实实在在", "现在在", "存在在",
                 "除了了解", "为了了结", "除了了"]


def count_dup(txt, word):
    """统计重复字次数，先剔除合法组合。"""
    s = txt
    for w in DUP_WHITELIST:
        s = s.replace(w, "")
    return s.count(word)


def frontmatter(txt):
    fm = {}
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
    return fm


def body(txt):
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        return parts[2] if len(parts) >= 3 else txt
    return txt


def nonempty_lines(txt):
    return [ln for ln in txt.splitlines() if ln.strip()]


def check(slug):
    en_p = os.path.join(PAPERS, slug + ".md")
    zh_p = os.path.join(PAPERS_ZH, slug + ".md")
    problems = []
    if not os.path.exists(en_p):
        return ["原文不存在: " + slug], {}
    if not os.path.exists(zh_p):
        return ["译文不存在（未翻译）"], {}
    ent = open(en_p, encoding="utf-8").read()
    zht = open(zh_p, encoding="utf-8").read()

    en_fm, zh_fm = frontmatter(ent), frontmatter(zht)
    for k in ("title", "url", "date", "category"):
        if en_fm.get(k) != zh_fm.get(k):
            problems.append("frontmatter.%s 不一致: 原文=%r 译文=%r" % (k, en_fm.get(k), zh_fm.get(k)))

    en_body, zh_body = body(ent), body(zht)

    en_links = re.findall(r"\]\(<[^>]+>\)", en_body)
    zh_links = re.findall(r"\]\(<[^>]+>\)", zh_body)
    if len(en_links) != len(zh_links):
        problems.append("链接数不一致: 原文 %d 条 / 译文 %d 条" % (len(en_links), len(zh_links)))

    # 全角括号坏链：出现 （< 或 全角右括号紧跟 >
    bad = re.findall(r"[（(]\s*<https?://[^)]*[）]", zh_body)
    if bad:
        problems.append("发现全角括号坏链 %d 处: %s" % (len(bad), bad[:2]))

    en_imgs = re.findall(r"!\[[^\]]*\]\((assets/[^)]+)\)", en_body)
    zh_imgs = re.findall(r"!\[[^\]]*\]\((assets/[^)]+)\)", zh_body)
    if en_imgs != zh_imgs:
        problems.append("图片引用不一致: 原文 %d / 译文 %d" % (len(en_imgs), len(zh_imgs)))

    en_lines, zh_lines = nonempty_lines(en_body), nonempty_lines(zh_body)
    ratio = len(zh_lines) / max(1, len(en_lines))
    if not (0.6 <= ratio <= 1.5):
        problems.append("非空行数比例异常: 原文 %d 行 / 译文 %d 行 (%.2f)" % (len(en_lines), len(zh_lines), ratio))

    for w in DUP_WORDS:
        n = count_dup(zht, w)
        if n:
            problems.append("重复字 %r 出现 %d 次" % (w, n))

    # 疑似未翻译：连续 3 行以上且每行 >60 字符、几乎无汉字
    # 先剥掉 Markdown 链接里的长 URL；跳过代码块（参考文献/BibTeX 按规范保留英文）
    # 与以斜体标记的署名行（作者名单本就是英文）
    run = 0
    worst = 0
    in_code = False
    in_refs = False
    for ln in zh_lines:
        if re.match(r"^\s{0,3}#{1,4}\s", ln):
            head = ln.strip()
            in_refs = bool(re.search(
                r"(参考文献|References|Data sources|数据来源|Footnotes|脚注|"
                r"Authors|Acknowledgements|Contributors|Citation|Bibliography)", head, re.I))
            run = 0
            continue
        if ln.strip().startswith("```"):
            in_code = not in_code
            run = 0
            continue
        if in_code or in_refs:
            continue
        # 缩进代码块（JSON / 系统提示词 / 命令行）按规范保留英文
        if ln.startswith("    ") and not re.search(r"[\u4e00-\u9fff]", ln):
            run = 0
            continue
        if ln.strip().startswith("_") and not re.search(r"[\u4e00-\u9fff]", ln):
            run = 0
            continue
        plain = re.sub(r"\]\(<[^>]+>\)", "]", ln)
        plain = re.sub(r"https?://\S+", "", plain)
        han = len(re.findall(r"[\u4e00-\u9fff]", plain))
        if len(plain) > 60 and han / max(1, len(plain)) < 0.1:
            run += 1
            worst = max(worst, run)
        else:
            run = 0
    if worst >= 3:
        problems.append("疑似 %d 行连续未翻译的英文段落" % worst)

    tail = re.sub(r"\s+", " ", zht.strip())[-60:]
    stats = {
        "en_lines": len(en_lines), "zh_lines": len(zh_lines),
        "en_links": len(en_links), "zh_links": len(zh_links),
        "zh_chars": len(zht), "tail": tail,
    }
    # 原文常以 BibTeX 的 }、英文作者署名、代码块等「合理保留英文」的内容收尾。
    # 这些是合法结尾，不应为了过校验而在译文里凭空补一句中文（违反忠实度）。
    stripped = zht.strip()
    tail_line = stripped.splitlines()[-1].strip() if stripped else ""
    legit_tail = (
        re.search(r"[。！？；：\.\)》】\]}\"'`]\s*$", stripped)
        or tail_line.startswith("```")
        or tail_line.startswith("_")
        or bool(re.match(r"^[A-Za-z0-9 .,()\-&]+$", tail_line))
    )
    if not legit_tail:
        problems.append("结尾字符可疑（可能被截断）: ...%s" % tail)
    return problems, stats


def main():
    if len(sys.argv) > 1:
        slugs = sys.argv[1:]
    else:
        slugs = [r["slug"] for r in json.load(open(META, encoding="utf-8"))]

    total_bad = 0
    print("%-58s %7s %7s %5s %5s %8s  %s" % ("slug", "en行", "zh行", "en链", "zh链", "zh字数", "问题"))
    print("-" * 120)
    for s in slugs:
        problems, st = check(s)
        flag = "OK" if not problems else "问题 %d 项" % len(problems)
        if problems:
            total_bad += 1
        print("%-58s %7s %7s %5s %5s %8s  %s" % (
            s[:58], st.get("en_lines", "-"), st.get("zh_lines", "-"),
            st.get("en_links", "-"), st.get("zh_links", "-"),
            st.get("zh_chars", "-"), flag))
        for p in problems:
            print("        - " + p)
    print()
    print("有问题的篇目: %d / %d" % (total_bad, len(slugs)))


if __name__ == "__main__":
    main()
