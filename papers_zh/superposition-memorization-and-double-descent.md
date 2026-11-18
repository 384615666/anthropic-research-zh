---
title: Superposition, Memorization, and Double Descent
url: https://www.anthropic.com/research/superposition-memorization-and-double-descent
date: Jan 5, 2023
category: Interpretability
source: https://www.anthropic.com/research
---

# 叠加、记忆与双下降

- **日期：** 
- **分类：** 可解释性（Interpretability）
- **来源：** https://www.anthropic.com/research/superposition-memorization-and-double-descent

---

可解释性研究
2023年1月5日
[阅读论文](<https://transformer-circuits.pub/2023/toy-double-descent/index.html>)
## 摘要
在[最近的一篇论文](<https://transformer-circuits.pub/2022/toy_model/index.html>)中，我们发现，在玩具任务上训练的简单神经网络经常表现出一种叫做叠加（superposition）的现象，即它们表示的特征数量超过它们的神经元数量。我们的研究仅限于无限数据、欠拟合（underfitting）的范畴。但有理由相信，如果我们想在机制可解释性（mechanistic interpretability）方面取得成功，理解过拟合（overfitting）可能很重要，而叠加可能是这个故事的核心部分。
  
为什么机制可解释性要关心过拟合？尽管过拟合是机器学习的核心问题，但我们对深度学习模型过拟合或记忆示例时到底发生了什么几乎没有机制上的理解。此外，之前的工作暗示，过拟合与学习可解释特征之间可能存在重要的联系。
  
所以理解过拟合很重要，但它为什么与叠加相关呢？考虑一个逐字记忆文本的语言模型的情况。它怎么做到这一点？一个天真的想法是，它可能用神经元创建一个查找表，把序列映射到任意的续写。对于它想记忆的每一个 token 序列，它可以专门用一个神经元来检测该序列，然后在它触发时实现任意的行为。这种方法的问题在于它极其低效——但它似乎是叠加的完美候选，因为每个案例都是互斥的，不会相互干扰。
  
在这篇笔记中，我们对在有限数据集上训练上一篇论文中相同的玩具模型进行了非常初步的探究。尽管极其简单，但事实证明，这个玩具模型是研究过拟合的一个惊人丰富的案例。特别是，我们发现了以下几点：
  * 过拟合对应于在叠加中存储数据点，而不是特征。
  * 根据数据集大小，我们的模型落入两个不同的范畴：过拟合范畴（以在叠加中存储数据点为特征）和泛化范畴（以在叠加中存储特征为特征）。
  * 我们观察到模型在这两个范畴之间过渡时的双下降（double descent）现象。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/superposition-memorization-and-double-descent>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/superposition-memorization-and-double-descent>)
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