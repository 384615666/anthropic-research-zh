---
title: Language Models (Mostly) Know What They Know
url: https://www.anthropic.com/research/language-models-mostly-know-what-they-know
date: Jul 11, 2022
category: Alignment
source: https://www.anthropic.com/research
---

# 语言模型（大致）知道它们知道什么

- **日期：** 
- **分类：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/language-models-mostly-know-what-they-know

---

对齐研究（AlignmentResearch）
2022 年 7 月 11 日
[阅读论文](<https://arxiv.org/abs/2207.05221>)
## 摘要
我们研究语言模型（Language Models）能否评估自身主张的有效性，并预测自己能够正确回答哪些问题。我们首先证明，当以正确的格式提供问题时，较大的模型在多样化的多项选择题和判断题上具有良好的校准性（well-calibrated）。因此，我们可以通过先让模型提出答案、再评估其答案正确的概率「P(True)」的方式，来处理开放式采样任务上的自我评估。我们发现 P(True) 在一系列多样化任务上表现令人鼓舞，且具有良好的校准性和扩展性。当我们允许模型在预测某一特定答案的有效性之前，先考虑自己的多个样本时，自我评估的性能会进一步提升。接下来，我们研究能否训练模型预测「P(IK)」——即「我知道」某个问题答案的概率，而无需参考任何特定提出的答案。模型在预测 P(IK) 方面表现良好，并能在不同任务之间部分泛化，不过在新任务上 P(IK) 的校准仍存在困难。当上下文中存在相关的源材料，或存在数学应用题解题提示时，预测的 P(IK) 概率也会相应提高。我们希望这些观察能为训练更诚实的模型奠定基础，并有助于研究当模型在模仿人类写作以外的目标上训练时，诚实性如何泛化。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/language-models-mostly-know-what-they-know>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/language-models-mostly-know-what-they-know>)
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