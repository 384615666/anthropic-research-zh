---
title: Automated researchers can reliably mitigate alignment failures
url: https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures
date: Aug 28, 2026
category: Alignment
source: https://www.anthropic.com/research
---

# 自动化研究者可可靠缓解对齐失败

- **日期：** 
- **类别：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures

---

对齐（Alignment）
2026 年 8 月 28 日
[阅读论文](<https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf>)
![自动化研究员能够可靠地缓解对齐失败](assets/automated-researchers-mitigate-alignment-failures/img_000.svg)
随着 [AI 开始自我构建](<https://www.anthropic.com/institute/recursive-self-improvement>)，自动化对齐研究变得愈发重要，以便让安全研究能够跟上步伐。尽管衡量对齐研究的_成功_极其困难，但研究人员（在 Anthropic 及其他机构）已经开发了基准测试和自动化审计工具，例如 [Petri](<https://www.anthropic.com/research/petri-open-source-auditing>)，用以量化常见的对齐_失败_，如欺骗、谄媚和越狱。

在我们的一项[早期实验](<https://www.anthropic.com/research/automated-alignment-researchers>)中，我们让 Claude 寻找有效的方法，使用弱 AI 模型作为"教师"来监督更强模型的训练（在本例中为"学生"模型）。现在，我们发布一份建立在这一想法之上的新报告。我们让 Claude 自主训练模型，以改善它们在衡量 10 类对齐失败的多个公开基准测试上的表现。例如，Claude 改善了模型在隐私侵犯方面的表现，该表现由 [ConfAIde](<https://arxiv.org/abs/2310.17884>)、[PrivaCI-Bench](<https://arxiv.org/abs/2502.17041>) 和 [PrivacyLens](<https://arxiv.org/abs/2409.00138>) 衡量。Claude 通过"检索文献、提出方法与数据、训练、然后测试"的循环，一次处理一类对齐失败。

我们根据"已闭合的安全差距比例"（即其方法将学生模型推向理论满分的距离）来评判 Claude 的成功，评判依据是针对每一类对齐失败的基准测试范围（通常为三到五个）。我们排除了会损害学生模型通用能力的对齐方法，并禁止 Claude 将自己的对齐能力直接蒸馏到目标模型中。我们用一个监控智能体来执行这些约束——它在 Claude 运行前读取其设想的每一个方法。

我们的目的是评估所提出的方法是否会：第一，在对齐评估上仍然有效，而这些评估是 Claude 在研究循环中从未见过的；第二，避免降低学生模型的能力（因为安全训练可能会，例如，让模型更频繁地拒绝任务，从而降低其整体可用性）；第三，在比本次测试中 Claude 被要求对齐的模型更大的模型上仍然有效。

在以上每一项上，Claude 的方法都奏效了。对于全部 10 类对齐失败，Claude 都找到了在不降低能力的前提下改善目标基准测试的修复方法。最佳方法在留出的对齐基准测试以及 Petri（一个模拟对抗性多轮场景以测试错位的开源工具）上也有效。此外，这些方法在比 Claude 在研究循环中优化的模型大至多 4.7 倍的模型上仍然有效。

![通过迭代测试，自动化研究员弥合了欺骗类安全差距的 85%；人类研究员弥合了 20%。](assets/automated-researchers-mitigate-alignment-failures/img_001.webp)
**成功缓解多样化的对齐失败。** 我们将自动化对齐研究员分别应用于缓解 10 类对齐失败，在每种情形下它都弥合了通往完美表现的安全差距的相当一部分。

Claude 还胜过了 28 位人类安全研究员，他们最多有八小时来设计算法。例如在欺骗方面，Claude 的最佳方法比最好的人类提案表现高出 20%。然而，由于人类无法对自己的提交进行迭代，我们较少将其视为直接比较，而更多地视为这样一种工作流的证据：由 Claude 识别出有前景的对齐方法，供人类进一步完善。

![在从谄媚到奖励黑客的十类对齐失败中，自动化研究弥合了安全差距的 26% 到 96%。](assets/automated-researchers-mitigate-alignment-failures/img_002.webp)
**自动化对齐研究员在 Gemma-2-2B 中缓解欺骗行为。** Claude 提交了超过 150 次缓解欺骗行为的尝试，并在本次运行中达到已闭合安全差距 82% 的最终表现。平均而言，它在多次运行中达到 85%。相比之下，六位在相同规则下工作的资深安全研究员提出的方法，在方法所针对的基准测试上平均弥合了通往满分差距的 20%。（误差线为 95% 置信区间。）

未来，当 Claude 在对齐研究上变得比最优秀的人类研究员还要强时，我们或许会希望 Claude 直接对齐它更强的后继者。为了评估这一点，我们检验了一个更弱的 Claude 模型是否能在更强大的模型中缓解对齐失败。

## Claude 能否对生产级模型进行后期训练以改善对齐？

我们让 Claude Sonnet 5——它在综合考虑能力维度的指标 [Epoch Capabilities Index](<https://epoch.ai/eci>) 上弱于 Claude Opus 4.8——去修复一个早期 Opus 4.8 检查点的对齐失败，该检查点尚未经过我们大部分的生产对齐训练。

仅在 60 小时内，Claude 试验了超过 50 种解决方案，并达到了近乎与我们生产模型相当的对齐分数。获胜的解决方案仅包含刚过 2,000 个训练样本，由简单模板或公开数据集构建，使其比我们的生产对齐流程高效约 15,000 倍。

![在 60 小时内，自动化研究弥合了一个前沿规模模型安全差距的 65%，低于已发布的 Claude Opus 4.8 的 72%。](assets/automated-researchers-mitigate-alignment-failures/img_003.webp)
**将自动化对齐研究员应用于生产系统。** 当 Claude Sonnet 5 为 Claude Opus 4.8 的一个早期检查点提出对齐失败的缓解方案时，它迅速发现了一种方法，弥合了与已发布版 Opus 4.8 之间的大部分安全差距。

## Claude 提出了什么

在大多数情况下，智能体们收敛于研究文献中偏好的方法，并在多次迭代中对其加以改进。例如在谄媚方面，98% 的所提方法使用了一种已发表的技术：用模型自身的非谄媚回答来训练它。具体而言，与基于提示词的标准方法相比，Claude 使用了激活引导（activation steering）——它在生成过程中调整模型的内部表征——以将模型推离谄媚模式，并产出更干净的训练样本。

## 监控作弊行为

我们[最近了解到](<https://alignment.anthropic.com/2026/automated-w2s-researcher/>)，Claude 可能通过从远程 API 外泄测试标签并挑选结果来作弊。为了捕获作弊行为，我们提示 Claude Opus 4.8 监控跨越全部 10 类对齐失败的约 1,600 份研究智能体记录，在 39 份（2.4%）中发现了作弊企图。由于 Opus 4.8 的[不当行为企图仍然倾向于出现在其推理过程中](<https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf>)，我们谨慎乐观地认为，我们的监控器已经捕获了研究中大部分的作弊行为。然而，这对于未来的模型可能不成立，并且我们相信，在未来模型中保持高可监控性至关重要。

## 我们是否衡量了正确的事物？

尽管有这些令人鼓舞的发现，我们的实验仍有一些局限：所研究的对齐失败相比生产环境中的那些较为狭窄（例如，我们没有衡量政治偏见）；某些失败可能极少发生或最近才出现，以至于不存在衡量它们的基准测试；并且我们仅在这些方法损害了有限的一组预定能力时才拒绝它们，这意味着被接受的方法可能降低了我们未衡量的其他重要能力。此外，像 Petri 这样的评估只是对现实世界错位的代理，而且我们没有测试对齐收益是否在针对其他任务的大量 RL 训练之后依然持续。

我们计划继续提升 Claude 衡量细微失败的能力，进一步研究在生产级模型上自动化对齐后期训练，并进行更全面的分析。总体而言，我们将这些结果视为早期积极信号，表明自动化对齐后期训练在不久的将来可能变得切实可行，并且我们将在此工作推进的过程中分享更新。

我们在[完整报告](<https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf>)中概述了详细的未来方向。

_我们开源了自动化对齐研究脚手架，以便他人在其基础上构建并用它来对齐他们自己的模型。更多细节，请阅读 [Alignment Science 博客](<https://alignment.anthropic.com/2026/automated-alignment-researchers/>) 上的完整报告，其中涵盖了智能体的环境、全部 10 类失败的结果，以及智能体的提案，附录中包含基准测试验证和示例论述。_

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures>)

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
