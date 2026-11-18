---
title: Studying Large Language Model Generalization with Influence Functions
url: https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions
date: Aug 8, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# 用影响函数研究大语言模型的泛化

- **日期：**
- **类别：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions

---

对齐研究（Alignment Research）
2023 年 8 月 8 日
[阅读论文](<https://arxiv.org/abs/2308.03296>)
## 摘要
当试图更好地洞察机器学习模型以理解并缓解相关风险时，一个潜在有价值的证据来源是：哪些训练示例对给定行为的贡献最大？影响函数（influence functions）旨在回答一个反事实问题：如果给定序列被添加到训练集中，模型的参数（以及因此它的输出）会如何变化？虽然影响函数已经为小模型产生了洞见，但由于计算逆黑塞向量积（inverse-Hessian-vector product，IHVP）的困难，它们很难扩展到大型语言模型（LLM）。我们使用特征值校正的克罗内克因子近似曲率（Eigenvalue-corrected Kronecker-Factored Approximate Curvature，EK-FAC）近似，将影响函数扩展到多达 520 亿参数的大语言模型。在我们的实验中，尽管 IHVP 计算速度快了几个数量级，EK-FAC 仍达到了与传统影响函数估计器相似的精度。我们研究了两种算法技术来降低计算候选训练序列梯度的成本：TF-IDF 过滤和查询批处理。我们使用影响函数来研究 LLM 的泛化模式，包括影响模式的稀疏性、随规模增加的抽象性、数学和编程能力、跨语言泛化以及角色扮演行为。尽管存在许多表面上复杂的泛化形式，我们还是发现了一个令人惊讶的局限性：当关键短语的顺序被颠倒时，影响会衰减到接近零。总的来说，影响函数给了我们一个强大的新工具来研究 LLM 的泛化特性。


[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions>)
## 相关内容
### 了解更多关于 Claude 数学能力的信息
Claude 的一个未发布的研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的一个长期未破的下界，将其从 41.6% 提高到 67.2%。
[了解更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二个攻击发现了一种攻击轮数缩减的 AES（使用最广泛的对称密码）的新方法。
[了解更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能操控无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估来测试 AI 模型使用飞行无人机的能力，最终形成了一个新的基准：Drone-Bench。
[了解更多](</research/project-pilot>)