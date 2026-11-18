---
title: Constitutional AI: Harmlessness from AI Feedback
url: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
date: Dec 15, 2022
category: Alignment
source: https://www.anthropic.com/research
---

# 宪法式 AI：来自 AI 反馈的无害性

- **日期：** 
- **类别：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

---

对齐研究（Alignment Research）
2022 年 12 月 15 日
[阅读论文](<https://arxiv.org/abs/2212.08073>)
## 摘要
随着 AI 系统能力越来越强，我们希望借助它们来监督其他 AI。我们尝试了一些方法，通过自我改进来训练一个无害的 AI 助手，全程不需要任何人工标注的有害输出。唯一的人类监督是一份规则或原则清单，因此我们将这种方法称为"宪法式 AI"（Constitutional AI）。该过程包括监督学习和强化学习两个阶段。在监督学习阶段，我们从初始模型中采样，然后生成自我批评和修订，再在修订后的回答上微调原始模型。在强化学习阶段，我们从微调后的模型中采样，使用一个模型来评估两个样本中哪个更好，然后基于这一 AI 偏好数据集训练偏好模型。随后，我们以该偏好模型作为奖励信号进行强化学习训练，即使用"来自 AI 反馈的强化学习"（RLAIF，RL from AI Feedback）。最终，我们能够训练出一个无害但非回避型的 AI 助手，它通过与有害查询互动并解释自己的反对理由来应对这些查询。监督学习和强化学习两种方法都可以利用思维链（chain-of-thought）式推理，来提高人类评判的性能以及 AI 决策过程的透明度。这些方法使我们能够更精确地控制 AI 行为，并且所需的人工标注大大减少。
## 政策备忘录
[宪法式 AI 政策备忘录](<https://www-cdn.anthropic.com/7512771452629584566b6303311496c262da1006/Anthropic_ConstitutionalAI_v2.pdf>)
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback>)
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