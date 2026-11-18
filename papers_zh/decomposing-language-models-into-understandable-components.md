---
title: Decomposing Language Models Into Understandable Components
url: https://www.anthropic.com/research/decomposing-language-models-into-understandable-components
date: Oct 5, 2023
category: Interpretability
source: https://www.anthropic.com/research
---

# 将语言模型分解为可理解的组成部分

- **日期：** 
- **分类：** 可解释性（Interpretability）
- **来源：** https://www.anthropic.com/research/decomposing-language-models-into-understandable-components

---

可解释性研究（InterpretabilityResearch）
2023 年 10 月 5 日
![](assets/decomposing-language-models-into-understandable-components/img_000.img)
神经网络是在数据上训练的，而不是被编程来遵循规则。在训练的每一步中，数百万或数十亿个参数都会被更新，以使模型更好地完成任务；到训练结束时，模型已能够展现出令人眼花缭乱的各种行为。我们完全理解训练后网络的数学原理——神经网络中的每个神经元都执行简单的算术运算——但我们不理解为什么这些数学运算会带来我们所看到的行为。这使得我们难以诊断失败模式、难以知道如何修复它们，也难以证明一个模型是真正安全的。

神经科学家在理解人类行为的生物学基础时也面临类似的问题。人脑中放电的神经元必须以某种方式实现人的思想、情感和决策。几十年的神经科学研究揭示了大脑运作的许多机制，并促成了针对癫痫等疾病的靶向治疗，但仍有许多奥秘尚未解开。幸运的是，对于我们这些试图理解人工神经网络的人来说，实验要容易做得多。我们可以同时记录网络中每个神经元的激活状态，通过抑制或刺激它们进行干预，并测试网络对任何可能输入的反应。

不幸的是，事实证明单个神经元与网络行为之间并不存在一致的关系。例如，小型语言模型中的[单个神经元](<https://transformer-circuits.pub/2023/monosemantic-features/vis/a-neurons.html#feature-83>)在许多不相关的语境中都会被激活，包括：学术引用、英语对话、HTTP 请求和韩语文本。在一个经典的视觉模型中，[单个神经元](<https://distill.pub/2017/feature-visualization/#diversity>)会对猫的脸和汽车的前脸都作出反应。一个神经元的激活在不同语境中可能意味着不同的事物。
![](assets/decomposing-language-models-into-understandable-components/img_001.img)
在我们最新的论文《[迈向单义性：用字典学习分解语言模型](<https://transformer-circuits.pub/2023/monosemantic-features/index.html>)》中，我们概述了这样的证据：存在比单个神经元更好的分析单元，并且我们已经构建了能够在小规模 Transformer 模型中找到这些单元的机制。这些单元被称为特征（features），对应着神经元激活的模式（线性组合）。这为将复杂的神经网络分解成我们可以理解的部分提供了一条路径，并建立在神经科学、机器学习和统计学中解读高维系统的既往努力之上。

在 Transformer 语言模型中，我们将一个包含 512 个神经元的层分解为 4000 多个特征，这些特征分别表征诸如 DNA 序列、法律语言、HTTP 请求、希伯来语文本、营养学表述等等更多内容。这些模型属性中的大多数在单独观察单个神经元的激活时是不可见的。

![](assets/decomposing-language-models-into-understandable-components/img_002.img)
为了验证我们找到的特征在可解释性上显著优于模型的神经元，我们请了一位盲测的人类评估员对它们的可解释性打分。特征（红色）的得分远高于神经元（青色）。

![](assets/decomposing-language-models-into-understandable-components/img_003.img)
我们还采用了「自动可解释性」（autointerpretability）方法，即使用一个大语言模型为小模型的特征生成简短描述，然后根据另一个模型基于该描述预测特征激活的能力来打分。同样，特征的得分高于神经元，这提供了额外的证据，表明特征的激活及其对模型行为的下游影响具有一致的解释。

特征还提供了一种有针对性的模型引导方式。如下所示，人为激活某个特征会使模型行为以可预测的方式发生改变。
![](assets/decomposing-language-models-into-understandable-components/img_004.img)
最后，我们拉远视角，从整体上审视特征集。我们发现，学习到的特征在不同模型之间很大程度上是通用的，因此通过研究一个模型中的特征所得的经验教训可能推广到其他模型。我们还实验了调整学习特征的数量。我们发现这提供了一个「旋钮」，用于[调节观察模型的粒度](<https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting>)：将模型分解为一小组特征可提供更易理解的粗略视图，而将其分解为一大组特征则能提供揭示微妙模型属性的更精细视图。

这项工作源于 Anthropic 对机制可解释性（Mechanistic Interpretability）的投入——这是我们在 AI 安全方面最长期的研究押注之一。迄今为止，单个神经元不可解释这一事实对语言模型的机制理解构成了严重障碍。将神经元组分解为可解释的特征，有望跨越这一障碍。我们希望这最终能让我们从内部监控和引导模型行为，提升企业和全社会采用 AI 所必需的安全性与可靠性。

我们的下一个挑战是将这种方法从小型模型（我们已在其中验证了成功）扩展到前沿模型——后者的规模大出许多倍，且复杂程度大幅提高。我们第一次感到，解释大语言模型的下一个主要障碍是工程问题而非科学问题。

要了解更多相关信息，请阅读我们的论文《[迈向单义性：用字典学习分解语言模型](<https://transformer-circuits.pub/2023/monosemantic-features/index.html>)》。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/decomposing-language-models-into-understandable-components>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/decomposing-language-models-into-understandable-components>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未公开发布的研究版 Claude 在与黎曼猜想（Riemann hypothesis）相关的问题上取得了进展。它改进了满足该猜想的黎曼 zeta 函数零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[了解更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二个攻击则发现了一种攻击轮数缩减版 AES（使用最广泛的对称密码）的新方法。
[了解更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作开发了一系列评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新的基准测试：Drone-Bench。
[了解更多](</research/project-pilot>)