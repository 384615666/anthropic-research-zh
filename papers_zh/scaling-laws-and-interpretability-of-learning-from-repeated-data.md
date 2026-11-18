---
title: 从重复数据中学习的缩放定律与可解释性
url: https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data
date: May 21, 2022
category: Interpretability
source: https://www.anthropic.com/research
---

# 从重复数据中学习的缩放定律与可解释性

- **日期：**
- **分类：** Interpretability
- **来源：** https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data

---

2022 年 5 月 21 日
[阅读论文](<https://arxiv.org/abs/2205.10487>)
## 摘要
最近的大型语言模型在庞大的数据集上训练，但往往也在重复数据上训练，要么是为了提升更高质量数据权重的有意为之，要么是因为数据去重并不完美、模型在句子、段落或文档层面暴露于重复数据的无意之举。一些工作报告了这种重复数据对性能的显著负面影响。在本文中，我们试图系统地研究重复数据，并从机制上理解其影响。为此，我们训练了一个模型家族，其中大部分数据是唯一的，但一小部分数据被重复多次。我们发现一个强烈的双重下降现象，即重复数据可能导致测试损失在训练中途上升。一个可预测的重复频率范围会导致性能出现惊人地严重退化。例如，一个 800M 参数的模型，通过将 0.1% 的数据重复 100 次，尽管其余 90% 的训练 token 保持唯一，其性能可以退化到 2 倍小的模型（400M 参数）的水平。我们怀疑在中间存在一个数据可以被记忆的范围，而这样做消耗了模型容量的一大部分，这可能是退化峰值所在之处。最后，我们将这些观察与最近的机制可解释性工作联系起来——试图逆向工程模型执行的详细计算——表明数据重复不成比例地损害了复制和与泛化相关的内部结构，如归纳头（induction heads），为从泛化到记忆的转变提供了一种可能的机制。综合来看，这些结果提供了一个假说，解释为什么在大型语言模型中重复相对较小比例的数据可能导致对性能的不成比例的巨大损害。
## 作者
Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom Henighan, Andy Jones, Nicholas Joseph, Ben Mann, Nova DasSarma, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Jackson Kernion, Kamal Ndousse, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Jared Kaplan  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data>)
## 相关内容
### 深入了解 Claude 的数学能力
一个未发布的 Claude 研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足猜想的黎曼 zeta 函数零点的比例，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一种攻击显著削弱了 HAWK，这是一种为未来量子计算机能够攻破现有标准的世界而构建的数字签名方案。第二种识别出了一种攻击降轮 AES（最广泛使用的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
与 Andon Labs 合作，我们开发了一系列新的评估，衡量 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)