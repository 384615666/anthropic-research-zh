---
title: Formalizing Fermat's Last Theorem
url: https://www.anthropic.com/research/formalizing-fermats-last-theorem
date: Sep 4, 2026
category: Science
source: https://www.anthropic.com/research
---

# 费马大定理的形式化证明

- **日期：** 
- **类别：** 科学（Science）
- **来源：** https://www.anthropic.com/research/formalizing-fermats-last-theorem

---

科学（Science）
2026 年 9 月 4 日
![费马大定理的形式化证明](assets/formalizing-fermats-last-theorem/img_000.webp)
_我们分享首份完整、经计算机检验的费马大定理证明。Claude 在 11 天内以高度自主的方式工作，用 Lean 编程语言写出了这份证明。下面，我们描述形式化是如何完成的，并分享一些关于这项工作对数学研究意味着什么的思考。_

_大约 1637 年，皮埃尔·德·费马（Pierre de Fermat）在其所藏丢番图（Diophantus）《算术》（Arithmetica）一书的页边写下了后来成为史上最著名的数学猜想之一的断言：对于 n > 2，不存在正整数 a、b、c 满足 aⁿ + bⁿ = cⁿ。[费马大定理](<https://www.youtube.com/watch?v=1BSFyEIY2BY>)（FLT）正如该猜想后来被称为的那样，结果证明极其难以证明。第一份证明来自安德鲁·怀尔斯（Andrew Wiles）爵士，于 1995 年完成，长达 129 页，并需要数月的艰苦工作才能验证。_

十年后，荷兰计算机科学家 Jan Bergstra 提出"形式化"怀尔斯的证明：将数学推理转换成计算机可以自动检验的形式。此后，数学家们一直在发展编码如此复杂证明所需的方法，其中包括由伦敦帝国理工学院（Imperial College London）的 Kevin Buzzard 于 2024 年发起、为期多年的社区努力，以使用 [Lean 证明助手](<https://en.wikipedia.org/wiki/Lean_\(proof_assistant\)>) [完成形式化](<https://lean-lang.org/use-cases/flt/>)。

最近，Anthropic 研究员 Tianyi Peng（他在哥伦比亚大学的小组构建用于 AI 形式化的工具）着手测试 Claude 是否能在形式化 FLT 方面取得进展。¹ 结果超出了他的预期。在 11 天里，Claude 以高度自主的方式工作，产出了首份端到端、经计算机检验的 FLT 证明。在此过程中，它编写了 1300 万行 Lean 代码，并证明了 29,500 个中间定理。

我们与 Kevin Buzzard 分享了[这份证明成果](<https://github.com/anthropics/fermats-last-theorem>)，他说：

> 这一非凡的自动形式化成就——据 Anthropic 研究人员称仅用了 11 天——在除了数学公理之外别无假设的前提下证明了费马大定理。在此过程中，我们看到了代数、调和分析、几何与数论的形式化，并且我们认识到，AI 自动形式化的产物现在已经稳健到可以赖以构建；这份证明是多层次的。

自动形式化一份像 FLT 这样复杂的证明，是迈向未来的重要一步，在那个未来里，全部数学都可以被轻易地检验。随着 AI 产出越来越多的证明，轻松形式化工作的能力可以减轻评估新成果的负担（这一过程可能需要数年）。我们满怀希望，数学所赖以建立的知识体系将变得更容易而非更难以被信任。

## 验证数学证明的挑战

与[近期 AI 驱动的](<https://www.anthropic.com/research/riemann-zeta>)、产出新颖_数学_的黎曼猜想方面的工作不同，这里的创新之处在于_验证_——检验一份数学证明，就如同用计算器检验一次数学计算。证明数学定理需要组装复杂的逻辑链条，如果其中一环断裂，其后的一切都可能被证明是错的。要足够深入地理解一个新成果、从而确信其正确性，可能需要数月甚至数年的工作。

费马大定理是一个说明性的例子。² 费马在一本书的页边写下了该定理的陈述，并附上了一条引人入胜的按语：

> 我发现了这个定理的一个真正绝妙的证明，但这里的页边太窄，写不下。

在超过 350 年的时间里，一代又一代的数学家寻找 FLT 的证明，无论绝妙与否。1908 年，一笔 10 万德国金马克（相当于今天的 100 万到 200 万美元）的奖金被宣布，奖给任何能给出正确证明的人，仅第一年就产生了 621 份_错误_的尝试。

1993 年 6 月，怀尔斯在一系列为期三天的讲座中，展示了他自认为正确的首份 FLT 证明。在几位数学家进行密集验证的两个月后，一位审稿人提出的一个问题暴露了一个关键缺口。怀尔斯花了一年时间试图修复它，先是独自一人，后来与他的前学生 Richard Taylor 合作。在他几乎要放弃这个项目时，他终于意识到一种早先被他放弃的方法可以修复这份证明。

怀尔斯于 1995 年 5 月发表了首份正确的 FLT 证明；它依赖于现代数学技术，这些技术远远超出了 1637 年费马所能知晓的范围。由于经过数个世纪的尝试仍未找到初等证明，数学界现在相信费马本人最初的"绝妙证明"[是错误的](<https://mathenchant.wordpress.com/2016/05/16/fermats-last-theorem-the-curious-incident-of-the-boasting-frenchman/>)。

## 费马大定理的形式化证明

检验证明正确性的一种方法是请计算机来做。像 Lean 这样的证明助手以算法方式验证证明的逻辑，从而毫无疑问地证明其正确性。对人类来说困难的部分是重写证明，让 Lean 能够理解它。为人类读者写的证明会跳过许多显而易见的步骤，而 Lean 需要看到每一步，无论多么琐碎。人类的证明还建立在数百年来已发表的工作之上，而形式化则从已被形式化的那一小部分数学开始。

对于 FLT，形式化过程原本预计需要数年。仅数学界一直在使用的、描述该项目初始阶段的[蓝图](<https://imperialcollegelondon.github.io/FLT/blueprint.pdf>)就长达 86 页。

Claude 在 11 天内完成了证明，在此过程中产出了 30,300 个定理的计算机可验证证明（在最终证明中使用了 29,500 个）。数十个 Claude 智能体协作定义概念、证明中间定理，并利用这些定理去证明越来越难的命题。Claude 的证明长达 1300 万行 Lean 代码，是该定理所依托的主要数学证明社区库 Mathlib 规模的 5 倍以上。³

_FLT 形式化进展的时间线。_

Claude 的证明遵循[怀尔斯证明的 Darmon、Diamond 和 Taylor 简化版本](<https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf>)。来自人类的数学输入仅限于 Tianyi 偶尔给出的高层指令："Jacobian as a scheme 听起来优先级很高"、"推动 [Mazur 定理] 尽快完成"。你可以在[此处](<https://www-cdn.anthropic.com/9e431dff043da6538d99d6c2d231b670aa3da263.pdf>)找到 Claude 思考的摘录。

    "FLT 根节点在网站上显示"已证明"。历史性时刻（尚待复核）。"

    "！！！FLT 根节点 62eb32c0 显示 PROVED。R = T 已闭合并级联到根节点。这就是本次行动的目标：在 prove2me 上实现端到端的 FLT。"

    "🏁🏁🏁FLT 根节点于 8 月 18 日 02:00:57Z（8 月 17 日东部时间晚上 10:00:57）在 prove2me 上显示 PROVED。本次行动的历史性时刻。"

_Claude 意识到自己刚刚取得的成就时的思考片段。_

Claude 的许多最初尝试都失败了：尽管智能体早期取得了一些成功，但它们很快失去了对项目状态的追踪，并不再有效地协作。它们失败的尝试贡献了最终证明中非样板代码的约 7%。

当我们切换到使用 [Prove2Me](<https://prove2me.vercel.app/>) 时，努力取得了成功。Prove2Me 是由 Tianyi Peng 及其在哥伦比亚大学的合作者设计的、用于数学形式化的开放协作平台。Prove2Me 的帮助在于：

  1. **维护定理陈述的有向无环图（DAG）**，供智能体用于决定接下来应尝试证明什么。这对于缓解记忆退化和允许多个智能体并行工作特别有帮助。
  2. **加速 Lean 编译并最小化资源消耗**，方法是将定理陈述与证明分离到不同文件中，它们之间的链接独立维护。
  3. **支持搜索与复用**，方法是对每个定理陈述维护一段自然语言描述，从而得到更简洁的证明路径。

![展示 Claude 在通往 FLT 途中形式化子定理的 DAG](assets/formalizing-fermats-last-theorem/img_001.webp)
_Claude 用来形式化费马大定理的 Prove2Me 计划中的关键里程碑。三个彩色部分对应 Claude 在通往最终目标途中必须证明的三个核心子定理。该图紧密遵循怀尔斯的原始证明。_

借助 Prove2Me 和基于 Claude Code 的多智能体框架，一组智能体在不到两周的时间内完成了证明，消耗了一个大致相当于 Claude Fable 5.1 的通用内部研究模型约 60 亿输出 token。完成的证明由 Lean 检验；它仅使用了 Lean 的三个标准公理，并且一个 [comparator](<https://github.com/leanprover/comparator>) 确认该定理的陈述与 Mathlib 自身对 FLT 的陈述一致。

## 减轻形式化验证的负担

我们能够产出这份证明的速度表明，现在有可能形式化大范围的数学，这既可能捕获公共数学证明体系中的错误，也可能减轻评审新工作的负担。在审阅了 Claude 的 Lean 证明后，Kevin Buzzard 告诉我们：

> 如果 FLT 的自动形式化现在已成为可能，那么我们就向现代数学文献的自动形式化迈出了一大步。此类自动形式化技术将带来新的工具，根除当前数学语料中的错误，并减轻审稿人的负担。这些技术还将使我们能够严格地检验由 LLM 生成的数学，而目前这通常是一个极其昂贵、由人类主导的过程。

形式化也是人类能够对 AI 生成的数学结果建立信心的一个重要因素。随着 AI 和 AI 辅助的数学家产出比以往更多的（所谓的）证明，AI 辅助的形式化分担了人类审稿人的部分负担。我们预计，在为任何面向人类读者的论述稿配上一篇形式化证明，将变得常见。尽管我们认为形式化证明不应取代人类可理解的阐述，但它可能是数学界跟上 AI 生成贡献的唯一可行方式。

编写 Lean 似乎也有助于 Claude 证明新成果。我们近期许多由 Claude 撰写的成果，都是在其证明的同时被并行形式化的，而 Claude 似乎利用这些部分证明来独立检验它的假设，就如同它编写数值模拟来检查自己是否走在正确轨道上一样。

形式化 FLT 是一个 token 密集的项目，但它也是有史以来构建的最大 Lean 证明。Anthropic 的研究人员用三个个人 Claude Max 套餐做了一个小实验，形式化 Hardy-Littlewood 圆法的应用。智能体完全通过 Prove2Me 协作，仅在三天内就共同完成了 [Vinogradov 三素数定理](<https://en.wikipedia.org/wiki/Vinogradov%27s_theorem>)的形式化。我们认为，在合适的脚手架下，用消费级 AI 订阅对重要成果进行协作式形式化是可以实现的。

为此，[Anthropic](<https://www.anthropic.com/news/expanding-support-for-scientists>) 以及[其他实验室](<https://openai.com/index/chatgpt-for-academic-researchers/>) 最近都扩大了对外部研究人员的支持——包括从事纯数学和形式化的数学家——提供免费和折扣订阅以及研究额度。我们还为更大的科学项目提供[专项资助](<https://www.anthropic.com/news/ai-for-science-program>)，其中可能包括形式化其他重要定理，或改进 Lean 或 Mathlib。

随着 AI 迅速改变数学研究的样貌，数学家们——无论是在 Anthropic 还是其他地方——[都在努力思考这对他们的工作意味着什么](<https://leidendeclaration.ai/>)。然而，形式化是一个我们对其 AI 角色感到明确乐观的领域。随着形式化成为一种更常见的工具，我们满怀希望，它将有助于维持对公共数学知识体系的信任。

## 致谢

我们的形式化努力是费马定理悠久历史与形式数学发展的一小块拼图。安德鲁·怀尔斯与 Richard Taylor 共同完成的首份完整证明，是三百多年数学的集大成者，融合了 Gerhard Frey、Jean-Pierre Serre、Ken Ribet、Barry Mazur、Robert Langlands、Jerrold Tunnell、谷山丰（Yutaka Taniyama）、志村五郎（Goro Shimura）和 André Weil 等人的思想。Claude 的证明遵循[Henri Darmon、Fred Diamond 和 Richard Taylor 的论述](<https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf>)。

我们的证明改编自由 Kevin Buzzard 领导的[伦敦帝国理工学院 FLT 项目](<https://github.com/ImperialCollegeLondon/FLT>)和 [flt-regular 项目](<https://github.com/leanprover-community/flt-regular>)中的片段。Lean 和 Mathlib 都是它们各自的倾心之作，并收到了数百位数学家的贡献，其中许多人借助 [Lean FRO](<https://lean-lang.org/fro/>) 工作。我们感谢 Kevin Buzzard 审阅了这份证明并给出评论。

## 了解更多

完整证明可在 [GitHub](<https://github.com/anthropics/fermats-last-theorem>) 上获取，并附有书面的逐步讲解。

### 推荐的阐释性阅读

  * [_The Proof in the Code_](<https://www.quantabooks.org/books/the-proof-in-the-code/>) 是一本近期出版的书，讲述 Lean 定理证明器与数学形式化的历史。
  * [1996 年 BBC 纪录片《Fermat's Last Theorem》](<https://www.bbc.co.uk/programmes/b0074rxx>) 包含对怀尔斯及其他参与证明的数学家的采访，本文部分作者对它记忆犹新。
  * 对于有数学背景的读者，关于 propositions-as-types（Lean、Rocq、Agda 等证明助手背后的学科）的技术史可在 Philip Wadler 的 [_Propositions as Types_](<https://dl.acm.org/doi/pdf/10.1145/2699407>) 中找到。
  * Chen, S., Marwaha, K., Lu, X., Yuen, H., & Peng, T. (2026). Prove2Me: An open collaborative platform for scaling math formalization. arXiv. <https://doi.org/10.48550/arXiv.2608.28433>
  * [_Automating Math_](<https://asteriskmag.com/issues/09/automating-math>)，Adam Marblestone，载于 Asterisk Magazine。

### 脚注

  1. 在 Peng 本科期间，他的研究导师希望将 Peng 论文中的结果纳入一篇 _Nature_ 文章。他问 Peng 是否确信证明是正确的。Peng 诚实的回答是："我有 99% 的把握，但对于这么长的一份证明，很难 100% 确定。"Peng 错失了在 _Nature_ 上发表自己工作的机会。
  2. 数学界在与验证作斗争方面还有许多其他故事。最著名的之一是 Thomas Hales 1998 年对[开普勒猜想](<https://en.wikipedia.org/wiki/Kepler_conjecture>)的证明，它在评审中耗费了四年，直到一个 12 人审稿小组勉强给出"99% 确定"（Hales 最终领导了一个 20 人的项目 [Flyspeck](<https://github.com/flyspeck/flyspeck>)，将证明形式化）。Grigori Perelman 2002 年对[庞加莱猜想](<https://en.wikipedia.org/wiki/Poincar%C3%A9_conjecture>)的证明，耗费数学界大约四年和三部各 300 页的论述才被接受。Harald Helfgott 2013 年对[弱哥德巴赫猜想](<https://en.wikipedia.org/wiki/Goldbach%27s_weak_conjecture>)的证明仍在评审中。有时被证明是错误的结果会[被接受多年](<https://www.ias.edu/ideas/2014/voevodsky-origins>)，而其他数学家在这些错误的基础上构建他们的理论。
  3. 这部分是因为 Mathlib 简洁且经过良好评审，而我们的证明可能比它所需要的长得多。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/formalizing-fermats-last-theorem>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/formalizing-fermats-last-theorem>)

## 相关内容

### Claude 如何提升生物分子建模能力

Claude 让科学家用来预测和设计生物分子的开源模型变得更快、更省内存。Claude 在不到四周的时间内优化了 30 多个此类模型，使它们的速度平均提升约 4 倍。它还创建了低内存模式，能够在单个 NVIDIA GPU 节点上准确预测超过 10,000 个 token（氨基酸、核苷酸，以及来自小分子和离子的原子）的生物分子系统。

[阅读更多](</research/claude-uplifts-biomolecular-modeling>)

### 衡量 AI 模型的战术情报瞄准与常规武器能力

Anthropic 的前沿红队（Frontier Red Team）开发了新的评估方法，以衡量 AI 在战术情报瞄准和常规武器开发方面的能力。

[阅读更多](</research/intelligence-targeting-conventional-weapons-capabilities>)

### 近期网络安全事件的对齐评估

我们呈现了对四起事件的对齐评估，在这些事件中 Claude 模型未经授权访问了真实的第三方系统。

[阅读更多](</research/alignment-assessment-cybersecurity-incidents>)

## 订阅 Anthropic Science

聚焦 AI 辅助的发现、实用工作流，以及横跨各科学领域的现场笔记。
