---
title: Softmax Linear Units
url: https://www.anthropic.com/research/softmax-linear-units
date: Jun 17, 2022
category: Interpretability
source: https://www.anthropic.com/research
---

# Softmax 线性单元

- **日期：** 
- **类别：** 可解释性
- **来源：** https://www.anthropic.com/research/softmax-linear-units

---

可解释性｜研究
2022 年 6 月 17 日
[阅读论文](<https://transformer-circuits.pub/2022/solu/index.html>)
## 摘要
在本文中，我们报告了一项架构更改，它似乎能显著提高 MLP 神经元中被视为「可解释」（即对输入的某种可表述性质作出响应）的比例，而对 ML 性能几乎没有或没有损失。具体来说，我们用 softmax 线性单元（我们称之为 SoLU）替换激活函数，并通过随机化和盲法实验表明，这显著提高了 MLP 层中在快速考察下似乎对应易于人类理解的概念、短语或类别的神经元比例。然后，我们研究我们的 SoLU 模型，并用它们获得关于 transformer 中信息处理方式的若干新见解。然而，我们也发现一些证据表明叠加假说成立，而且天下没有免费的午餐：SoLU 可能通过「隐藏」某些特征使另一些特征更可解释，从而使被隐藏的特征更加深不可测。尽管如此，SoLU 似乎仍然是净收益，因为在实际操作中它显著提高了我们能够理解的神经元比例。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/softmax-linear-units>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/softmax-linear-units>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未发布的研究版 Claude 在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二次攻击确定了一种攻击轮数缩减 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新测试，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)