---
title: Towards Monosemanticity: Decomposing Language Models With Dictionary Learning
url: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning
date: Oct 5, 2023
category: Interpretability
source: https://www.anthropic.com/research
---

# 迈向单义性：用字典学习分解语言模型

- **日期：** 
- **类别：** 可解释性（Interpretability）
- **来源：** https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning

---

可解释性研究（InterpretabilityResearch）
2023 年 10 月 5 日
[阅读论文](<https://transformer-circuits.pub/2023/monosemantic-features/index.html>)
## 摘要
在我们最新的论文[《迈向单义性：用字典学习分解语言模型》](<https://transformer-circuits.pub/2023/monosemantic-features>)（_Towards Monosemanticity: Decomposing Language Models With Dictionary Learning_）中，我们概述了证据，表明存在比单个神经元更好的分析单元，并且我们已经构建了能在小型 Transformer 模型中找到这些单元的机制。这些被称为特征的单元对应于神经元激活的模式（线性组合）。这为将复杂的神经网络分解成我们可以理解的部分提供了一条路径，并建立在神经科学、机器学习和统计学中先前解释高维系统的努力之上。在 Transformer 语言模型中，我们将一个具有 512 个神经元的层分解为 4000 多个特征，它们分别代表 DNA 序列、法律语言、HTTP 请求、希伯来语文本、营养声明等等。在孤立地查看单个神经元的激活时，这些模型属性中的大多数是不可见的。
  


[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning>)
## 相关内容
### 深入了解 Claude 的数学能力
一个未发布的 Claude 研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例这一长期存在的下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二次攻击发现了一种攻击缩减轮数 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新测试，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)