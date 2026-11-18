---
title: Donating our open-source alignment tool
url: https://www.anthropic.com/research/donating-open-source-petri
date: May 7, 2026
category: Alignment
source: https://www.anthropic.com/research
---

# 捐赠我们的开源对齐工具

- **日期：** 
- **分类：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/donating-open-source-petri

---

对齐
2026年5月7日
![Donating our open-source alignment tool](assets/donating-open-source-petri/img_000.svg)
2025 年 10 月，我们推出了 [Petri](<https://www.anthropic.com/research/petri-open-source-auditing>)，一个可以应用于任何大语言模型的开源对齐测试工具箱。Petri 是作为我们 Anthropic Fellows 计划的一部分开发的，可以用来快速、轻松地测试 AI 模型的令人担忧的倾向，如欺骗、谄媚和与有害请求合作。它是我们为整个 AI 开发社区开发开放且有用的对齐工具的努力的一部分。
自 Claude Sonnet 4.5 以来，Petri 一直是我们每个 Claude 模型对齐评估的一部分。它比较新模型在一系列对齐相关场景中的行为，这些场景由一个单独的"审计者"（auditor）模型模拟。然后，一个进一步的"评判者"（judge）模型对产生的对话记录中的错位行为进行评分。
我们很高兴看到 Petri 被外部组织使用：例如，英国的 AI 安全研究所（AISI）把它作为评估模型破坏 AI 研究倾向的[主要部分](<https://arxiv.org/abs/2604.00788>)。
我们现在正在把 Petri 更新到第三个版本。以下是一些最大的变化：
  * _适应性。_ Petri 3.0 涉及重大的架构变化，允许用户把它适应更多用途，特别是把审计者模型和目标模型拆分为可以单独调整的独立组件；
  * _真实性。_ 尽管对齐研究人员试图让测试看起来真实，但模型通常可以从设置中的各种人为痕迹推断出它实际上是测试的一部分。如果模型知道自己在被评估，研究人员就无法再看到模型_总体上_的行为方式。Petri 的一个附加组件——我们称之为"Dish"——让设置变得真实得多，例如使用模型的真实系统提示词和真实部署中会使用的真实"脚手架"（包裹在模型周围、帮助它达成目标的软件）来运行测试；
  * _深度。_ 我们现在已经把 Petri 与我们另一个开源对齐工具 [Bloom](<https://www.anthropic.com/research/bloom>) 集成，后者可以对特定选定的行为进行更深入的评估（与 Petri 更广泛的方法相比）。

我们还给 Petri 找了一个新家。我们已把它的开发移交给 [Meridian Labs](<https://meridianlabs.ai/>)，一个 AI 评估非营利组织。这一举措——类似于我们当初把模型上下文协议（Model Context Protocol, MCP）[捐赠](<https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation>)给 Linux 基金会——将有助于确保 Petri 保持独立于任何 AI 实验室，使其结果被行业内外视为中立和可信。
作为 Meridian Labs 的一部分，Petri 加入了 [Inspect](<https://inspect.aisi.org.uk/>) 和 [Scout](<https://meridianlabs-ai.github.io/inspect_scout/>) 等其他工具，构建了一个对实验室、独立研究人员和政府都开放的技术栈，而在这个时代，可靠的 AI 模型行为测试比以往任何时候都重要。
你可以在 [Meridian Labs 博客](<https://meridianlabs.ai/blog/posts/introducing-petri-3/>) 上阅读更多关于 Petri 3.0 的内容。
安装和使用 Petri 的说明可以在 [Petri 网站](<https://meridianlabs-ai.github.io/inspect_petri/>) 上找到。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/donating-open-source-petri>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/donating-open-source-petri>)
## 相关内容
### 了解更多关于 Claude 的数学能力
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足该猜想的黎曼 zeta 函数零点比例的下界——将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而设计的数字签名方案。第二个攻击确定了一种攻击减轮 AES（最广泛使用的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新评估，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)