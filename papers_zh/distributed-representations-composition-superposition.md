---
title: Distributed Representations: Composition & Superposition
url: https://www.anthropic.com/research/distributed-representations-composition-superposition
date: May 4, 2023
category: Interpretability
source: https://www.anthropic.com/research
---

# 分布式表征：组合与叠加

- **日期：** 
- **分类：** 可解释性
- **来源：** https://www.anthropic.com/research/distributed-representations-composition-superposition

---

可解释性研究
2023 年 5 月 4 日
[阅读论文](<https://transformer-circuits.pub/2023/superposition-composition/index.html>)
## 摘要
分布式表征是神经科学和联结主义 AI 方法中的经典思想。我们经常被问到我们关于叠加的工作与它的关系。自从发表我们关于叠加的[原始论文](<https://transformer-circuits.pub/2022/toy_model/index.html>)以来，我们有更多时间反思这两个主题之间的关系，并与人们讨论，因此想扩展我们[早期在相关工作部分](<https://transformer-circuits.pub/2022/toy_model/index.html#related-codes>)的讨论，分享一些想法。（我们非常关注叠加和分布式表征的结构，因为将表征分解为独立组件[是摆脱维数灾难](<https://transformer-circuits.pub/2022/mech-interp-essay/index.html>)和理解神经网络所必需的。）
  
在我们看来，"分布式表征"可能被理解为包含两个不同的思想，我们将它们称为"组合"（composition）和"叠加"（superposition）。1 这两种不同的分布式表征概念在泛化以及可以从它们线性计算什么函数方面具有非常不同的性质。虽然一种表征可以同时使用两者，但存在一种使它们从根本上处于紧张关系的权衡！2  
  
为使这一点具体化，我们将考虑神经元可能表征不同颜色形状的几种潜在方式。这些可爱的例子借自 [Thorpe (1989)](<https://persee.fr/doc/intel_0769-4113_1989_num_8_2_873>)，他创建这些例子是为了展示神经科学中"局部编码"（local code）和"分布式编码"（distributed code）思想之间的各种可能性。Thorpe 提供了四种示例编码——"局部"、"半局部"、"半分布式"和"高度分布式"。传统上，这些可能被视为处于"局部"和"分布式"之间的谱系上。我们将再次考虑这些例子，并提出一种替代观点，即这些例子反而在叠加和组合这两个不同维度上变化。  
  
按照 Thorpe 的做法，本文档将聚焦于神经元具有二元激活的示例。这显著简化了可能性空间，但它仍然是一个足够丰富的空间，可以提出有趣的问题
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/distributed-representations-composition-superposition>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/distributed-representations-composition-superposition>)
## 相关内容
### 了解更多关于 Claude 的数学能力
一个未发布的研究版 Claude 在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足该猜想的黎曼 zeta 函数零点比例，从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而构建的数字签名方案。第二个攻击发现了一种攻击缩减轮数 AES（使用最广泛的分组密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### 项目 Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，考察 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)