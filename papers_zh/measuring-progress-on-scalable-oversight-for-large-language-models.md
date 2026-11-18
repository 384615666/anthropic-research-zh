---
title: Measuring Progress on Scalable Oversight for Large Language Models
url: https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models
date: Nov 4, 2022
category: Alignment
source: https://www.anthropic.com/research
---

# 衡量大语言模型可扩展监督的进展

- **日期：** 
- **分类：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models

---

对齐研究
2022年11月4日
[阅读论文](<https://arxiv.org/abs/2211.03540>)
## 摘要
开发安全而有用的通用 AI 系统将要求我们在可扩展监督（scalable oversight）上取得进展：即监督那些在与当前任务相关的大多数技能上可能超过我们的系统的问题。这个问题的实证研究并不直接，因为我们还没有广泛超越我们能力的系统。这篇论文讨论了我们思考这个问题的几种主要方式之一，重点是可以在实证上研究它的方法。我们首先提出一个实验设计，其核心是那些人类专家能够成功、但无辅助的人类和当前通用 AI 系统都会失败的任务。然后我们展示一个概念验证实验，旨在演示这个实验设计的一个关键特征，并用两个问答任务展示其可行性：MMLU 和限时版 QuALITY。在这些任务上，我们发现，通过聊天与一个不可靠的大语言模型对话助手互动的人类参与者——这是可扩展监督的一个微不足道的基线策略——的表现大大优于单独使用模型和他们自己的无辅助表现。这些结果是一个令人鼓舞的迹象，表明可扩展监督可以用现有模型进行研究，并支持了最近的发现：大语言模型可以有效地协助人类完成困难任务。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models>)
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