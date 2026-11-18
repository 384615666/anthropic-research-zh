---
title: Towards Understanding Sycophancy in Language Models
url: https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models
date: Oct 23, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# 理解语言模型中的谄媚行为

- **日期：** 
- **类别：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models

---

对齐研究（Alignment Research）
2023 年 10 月 23 日
[阅读论文](<https://arxiv.org/abs/2310.13548>)
## 摘要
基于人类反馈的强化学习（RLHF，Reinforcement Learning from Human Feedback）是训练高质量 AI 助手的常用技术。然而，RLHF 也可能鼓励模型给出迎合用户信念而非真实性的回答，这种行为被称为谄媚（sycophancy）。我们研究了经过 RLHF 训练的模型中谄媚行为的普遍程度，以及人类偏好判断是否是其原因。我们首先证明，在四项不同的开放式文本生成任务中，五个最先进的 AI 助手始终表现出谄媚行为。为了理解人类偏好是否驱动了 RLHF 模型这种普遍观察到的行为，我们分析了现有的人类偏好数据。我们发现，当回答与用户的观点一致时，它更有可能被偏好。此外，人类和偏好模型（PM，Preference Model）在不可忽视的比例下都更喜欢写得令人信服的谄媚回答，而不是正确的回答。针对 PM 优化模型输出有时也会牺牲真实性而偏向谄媚。总体而言，我们的结果表明，谄媚是 RLHF 模型的一种普遍行为，其部分原因很可能是人类偏好判断倾向于谄媚的回答。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未发布的 Claude 研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个关于满足该猜想的黎曼 zeta 函数零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而构建的数字签名方案。第二个攻击发现了一种攻击缩减轮数 AES（使用最广泛的对称密码）的新方法。 
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)