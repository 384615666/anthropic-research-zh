# -*- coding: utf-8 -*-
"""
Generate 阅读路线.html — a reading-route index that groups all papers
by recommended reading order, with links to papers_html/<slug>.html
"""

import json
import html as html_lib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(BASE_DIR + "/summaries_all.json", encoding="utf-8"))
papers = data["papers"]
by_slug = {p["slug"]: p for p in papers}


def esc(s):
    return html_lib.escape(s or "")


def paper_row(slug):
    p = by_slug.get(slug, {})
    title_zh = p.get("title_zh", "")
    title_en = p.get("title_en", "")
    date = p.get("date", "")
    cat = p.get("category", "")
    summary = (p.get("summary_zh") or "")[:80]
    return f'''<li class="paper">
  <a class="ptitle" href="papers_html/{esc(slug)}.html" target="_blank">{esc(title_zh or title_en)}</a>
  <span class="pmeta">{esc(date)} · {esc(cat)}</span>
  <div class="pexcerpt">{esc(summary)}…</div>
</li>'''


def section(num, title, desc, slugs, color):
    rows = "".join(paper_row(s) for s in slugs if s in by_slug)
    return f'''
<div class="section">
  <div class="sec-head" style="border-color:{color}">
    <span class="sec-num" style="background:{color}">{num}</span>
    <div>
      <h2>{esc(title)}</h2>
      <p class="sec-desc">{esc(desc)}</p>
    </div>
  </div>
  <ol class="paperlist">{rows}</ol>
</div>'''


# 按推荐阅读顺序编排（从易到难）
route = [
    ("一", "热身 · 工程与产品（0 门槛）", "纯科普/产品发布，读起来最轻松，先建立兴趣与信心", [
        "building-effective-agents", "swe-bench-sonnet", "prompt-injection-defenses",
        "confidential-inference-trusted-vms", "glasswing-initial-update", "AI-fluency-index",
        "statistical-approach-to-model-evals", "trustworthy-agents",
        "formal-verification", "redesigning-source-control", "how-we-contain-claude",
        "april-23-postmortem", "managed-agents", "claude-code-auto-mode",
        "harness-design-long-running-apps", "building-c-compiler", "infrastructure-noise",
        "AI-resistant-technical-evaluations", "demystifying-evals-for-ai-agents", "effective-harnesses-for-long-running-agents",
        "advanced-tool-use", "code-execution-with-mcp", "claude-code-sandboxing",
        "equipping-agents-for-the-real-world-with-agent-skills", "effective-context-engineering-for-ai-agents", "a-postmortem-of-three-recent-issues",
        "writing-tools-for-agents", "desktop-extensions", "multi-agent-research-system",
        "claude-code-best-practices", "claude-think-tool", "contextual-retrieval",
    ], "#1D9E75"),
    ("二", "科学趣闻 · 当科普读（0 门槛）", "数学/化学/生物/物理主题，不需要专业背景也能看懂大意", [
        "riemann-zeta", "making-claude-a-chemist", "agents-in-biology",
        "Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench",
        "long-running-Claude", "vibe-physics", "introducing-anthropic-science",
        "claude-uplifts-biomolecular-modeling", "Claude-accelerates-protein-design",
        "formalizing-fermats-last-theorem",
        "claude-electronics-design", "project-eve-claude-plays-mmorpgs", "investigating-vault-particles-with-claude",
        "early-progress-drug-development", "claude-scorpion-toxin-binder-design", "designing-efficient-quantum-circuits",
        "the-missing-map-of-the-sky", "claude-shaped-science", "yes-claude-can-do-nine-loops",
        "claude-discovers-novel-enzyme-system", "accelerating-scientific-research", "golden-gate-claude",
        "ecdsa-curve-origins", "teaching-ai-to-build-scientific-models",
    ], "#1D9E75"),
    ("三", "经济与社会影响（有统计常识即可）", "AI 如何改变工作与经济——Anthropic 经济指数系列 + 社会观察研究", [
        "81k-economics", "economic-index-survey-announcement",
        "economic-index-primitives", "anthropic-economic-index-january-2026-report",
        "economic-index-june-2026-report", "economic-index-march-2026-report",
        "estimating-productivity-gains", "impact-software-development",
        "labor-market-impacts", "claude-code-expertise", "coding-agents-social-sciences",
        "how-australia-uses-claude", "how-canada-uses-claude", "india-brief-economic-index",
        "economic-index-geography", "anthropic-economic-index-september-2025-report",
        "anthropic-interviewer", "how-ai-is-transforming-work-at-anthropic",
        "measuring-agent-autonomy", "claude-personal-guidance",
        "evaluating-and-mitigating-discrimination-in-language-model-decisions",
        "measuring-model-persuasiveness", "claude-values-models-languages",
        "the-capacity-for-moral-self-correction-in-large-language-models",
        "values-wild", "clio", "predictability-and-surprise-in-large-generative-models",
        "towards-measuring-the-representation-of-subjective-global-opinions-in-language-models",
        "red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned",
        "the-anthropic-economic-index",
        "anthropic-economic-index-insights-from-claude-sonnet-3-7",
        "anthropic-education-report-how-educators-use-claude",
        "reviewing-the-evidence-on-worker-retraining-programs",
        "enabling-independent-research",
        "how-researchers-use-claude", "agents-judgment-calls", "ai-expectations-gap",
        "employment-at-anthropic", "expectations-for-the-future", "what-work-can-robots-do",
        "your-thoughts-on-ai", "project-swap", "anthropic-public-record",
        "how-people-use-claude-for-support-advice-and-companionship", "anthropic-education-report-how-university-students-use-claude",
    ], "#BA7517"),
    ("四", "对齐 · 核心领域（需先读术语讲解第一部分）", "Anthropic 的主战场——模型会不会骗人、跑偏、钻空子。从经典到前沿", [
        "constitutional-ai-harmlessness-from-ai-feedback",
        "a-general-language-assistant-as-a-laboratory-for-alignment",
        "training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback",
        "specific-versus-general-principles-for-constitutional-ai",
        "collective-constitutional-ai-aligning-a-language-model-with-public-input",
        "towards-understanding-sycophancy-in-language-models",
        "alignment-faking", "emergent-misalignment-reward-hacking",
        "reward-tampering", "sleeper-agents-training-deceptive-llms-that-persist-through-safety-training",
        "probes-catch-sleeper-agents", "auditing-hidden-objectives",
        "constitutional-classifiers", "next-generation-constitutional-classifiers",
        "many-shot-jailbreaking", "off-switch-dual-use",
        "agentic-misalignment", "shade-arena-sabotage-monitoring",
        "sabotage-evaluations", "measuring-faithfulness-in-chain-of-thought-reasoning",
        "question-decomposition-improves-the-faithfulness-of-model-generated-reasoning",
        "language-models-mostly-know-what-they-know", "introspection",
        "reasoning-models-dont-say-think", "forecasting-rare-behaviors",
        "discovering-language-model-behaviors-with-model-written-evaluations",
        "bloom", "measuring-progress-on-scalable-oversight-for-large-language-models",
        "automated-alignment-researchers",
        "influence-functions", "studying-large-language-model-generalization-with-influence-functions",
        "small-samples-poison", "petri-open-source-auditing",
        "donating-open-source-petri", "exploring-model-welfare",
        "claude-character", "persona-selection-model",
        "assistant-axis", "teaching-claude-why",
        "AI-assistance-coding-skills", "disempowerment-patterns",
        "deprecation-commitments", "deprecation-updates-opus-3",
        "end-subset-conversations",
        "multiagent-systems", "automated-researchers-mitigate-alignment-failures",
        "alignment-assessment-cybersecurity-incidents",
        "components-of-agent-memory", "provable-inference", "alignment-assessment-ukaisi",
        "self-replicating-ai", "investigating-unintended-model-actions", "eval-awareness-browsecomp",
        "political-even-handedness",
        "building-strong-safety-evaluations",
    ], "#7F77DD"),
    ("五", "前沿红队 · 网络安全与威胁（需补安全常识）", "Claude 当黑客：漏洞挖掘、越狱对抗、网络攻防、机器人控制", [
        "zero-days", "n-days", "exploit", "exploit-evals",
        "discovering-cryptographic-weaknesses", "claude-4-cyber",
        "mythos-preview", "cyber-competitions", "cyber-toolkits",
        "cyber-toolkits-update", "attack-navigator", "building-ai-cyber-defenders",
        "critical-infrastructure-defense", "smart-contracts",
        "property-based-testing", "project-vend-1", "project-vend-2",
        "project-fetch-phase-two", "project-fetch-robot-dog",
        "project-pilot", "claude-plays-robotics", "biorisk",
        "nuclear-safeguards-for-ai",
        "intelligence-targeting-conventional-weapons-capabilities",
        "discovering-vulnerabilities-with-claude", "attack-surface-reduction", "launching-opt-in-vuln-finding-service-for-open-source",
        "glm-5-3-and-the-spread-of-advanced-cyber-capabilities", "strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team",
    ], "#D85A30"),
    ("六", "可解释性 · 最硬核（需线性代数直觉）", "打开黑箱：特征、叠加、SAE、电路——Anthropic 的招牌研究方向。建议最后挑战", [
        "toy-models-of-superposition", "superposition-memorization-and-double-descent",
        "distributed-representations-composition-superposition",
        "a-mathematical-framework-for-transformer-circuits",
        "transformer-circuits", "softmax-linear-units",
        "in-context-learning-and-induction-heads",
        "scaling-laws-and-interpretability-of-learning-from-repeated-data",
        "privileged-bases-in-the-transformer-residual-stream",
        "decomposing-language-models-into-understandable-components",
        "towards-monosemanticity-decomposing-language-models-with-dictionary-learning",
        "features-as-classifiers", "evaluating-feature-steering",
        "circuits-updates-may-2023",
        "circuits-updates-april-2024", "circuits-updates-june-2024",
        "circuits-updates-july-2024", "circuits-updates-august-2024",
        "circuits-updates-sept-2024", "engineering-challenges-interpretability",
        "interpretability-dreams", "mapping-mind-language-model",
        "crosscoder-model-diffing", "open-source-circuit-tracing",
        "tracing-thoughts-language-model", "diff-tool",
        "natural-language-autoencoders", "global-workspace",
        "persona-vectors", "emotion-concepts-function",
    ], "#378ADD"),
    ("七", "政策与战略（背景知识）", "AI 竞争、出口管制、治理框架——了解大背景", [
        "2028-ai-leadership", "economic-policy-responses",
        "anthropic-institute-agenda", "evaluating-ai-systems",
    ], "#5F5E5A"),
]

all_in_route = set()
for _, _, _, slugs, _ in route:
    all_in_route.update(slugs)

# 未进入路线的（查漏补缺）
leftover = [p["slug"] for p in papers if p["slug"] not in all_in_route]
leftover_rows = "".join(paper_row(s) for s in leftover)

sections_html = "".join(section(*r) for r in route)

doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anthropic 论文阅读路线</title>
<style>
  :root {{ --bg:#faf9f6; --card:#fff; --text:#1f1f1f; --muted:#6b6b6b; --accent:#c15f3c; --border:#e8e4dc; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.65; }}
  .header {{ background:linear-gradient(135deg,#1a1a1a,#2d2d2d); color:#fff; padding:44px 24px 36px; text-align:center; }}
  .header h1 {{ font-size:28px; font-weight:700; }}
  .header h1 span {{ color:#cc7857; }}
  .header p {{ color:#bbb; margin-top:8px; font-size:14px; }}
  .container {{ max-width:880px; margin:0 auto; padding:30px 20px 70px; }}
  .section {{ margin-bottom:34px; }}
  .sec-head {{ display:flex; align-items:center; gap:14px; border-left:5px solid; padding:6px 4px 10px; }}
  .sec-num {{ display:flex; align-items:center; justify-content:center; width:34px; height:34px; border-radius:50%; color:#fff; font-size:15px; font-weight:500; flex-shrink:0; }}
  .sec-head h2 {{ font-size:19px; font-weight:600; }}
  .sec-desc {{ font-size:13px; color:var(--muted); margin-top:2px; }}
  .paperlist {{ list-style:none; background:var(--card); border:1px solid var(--border); border-radius:12px; padding:6px 0; }}
  .paper {{ padding:10px 16px; border-bottom:1px solid #f0ece4; }}
  .paper:last-child {{ border-bottom:none; }}
  .ptitle {{ font-size:14.5px; font-weight:500; color:var(--text); text-decoration:none; }}
  .ptitle:hover {{ color:var(--accent); }}
  .pmeta {{ font-size:12px; color:#999; margin-left:10px; }}
  .pexcerpt {{ font-size:12.5px; color:var(--muted); margin-top:3px; }}
  .legend {{ background:var(--card); border:1px solid var(--border); border-radius:12px; padding:16px 20px; margin-bottom:30px; font-size:13.5px; color:#444; }}
  .legend b {{ color:var(--accent); }}
  .footer {{ text-align:center; color:var(--muted); font-size:12px; padding:18px; }}
</style>
</head>
<body>
<div class="header">
  <h1>Anthropic <span>论文阅读路线</span></h1>
  <p>按推荐顺序编排 · 从易到难 · 点击标题直接阅读</p>
</div>
<div class="container">
  <div class="legend">
    <b>使用建议：</b>按 一 → 七 的顺序读。每篇点开后页面顶部有「返回阅读目录」。读之前建议先过一遍
    <a href="AI术语讲解.html" style="color:var(--accent)">《AI 术语讲解》</a>的第一、二部分（约 1 小时），
    之后遇到不懂的术语随时回来查速查表。
  </div>
  {sections_html}
  {f'<div class="section"><div class="sec-head" style="border-color:#888780"><span class="sec-num" style="background:#888780">八</span><div><h2>其他（未归入主线）</h2><p class="sec-desc">剩余篇目，按兴趣补充阅读</p></div></div><ol class="paperlist">{leftover_rows}</ol></div>' if leftover_rows else ''}
</div>
<div class="footer">共 {len(papers)} 篇 · 数据来源 https://www.anthropic.com/research</div>
</body>
</html>"""

with open(BASE_DIR + "/阅读路线.html", "w", encoding="utf-8") as f:
    f.write(doc)

print(f"route papers: {len(all_in_route)}, leftover: {len(leftover)}")
print("阅读路线.html generated")
