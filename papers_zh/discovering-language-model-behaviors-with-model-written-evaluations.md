---
title: Discovering Language Model Behaviors with Model-Written Evaluations
url: https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
date: Dec 19, 2022
category: Alignment
source: https://www.anthropic.com/research
---

# 用模型撰写的评估发现语言模型行为

- **日期：** 
- **分类：** 对齐
- **来源：** https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations

---

对齐研究
2022 年 12 月 19 日
[阅读论文](<https://arxiv.org/abs/2212.09251>)
## 摘要
随着语言模型（LM）规模的扩大，它们发展出许多新的行为，有好有坏，这加剧了评估它们行为方式的需求。先前的工作使用众包（耗时且昂贵）或现有数据源（并非总是可用）来创建评估。在这里，我们用 LM 自动生成评估。我们探索了人类投入量不同的各种方法，从指示 LM 编写是/否问题，到通过多阶段基于 LM 的生成和过滤来制作复杂的 Winogender 模式。众包工作者将这些示例评为高度相关，并对 90-100% 的标签表示认同，有时甚至比相应的人工编写数据集更认同。我们生成了 154 个数据集，并发现了新的逆向缩放（inverse scaling）案例，即 LM 越大表现越差。更大的 LM 会重复对话用户偏好的回答（"谄媚"），并表达出追求资源获取和目标保持等令人担忧目标的更强烈欲望。我们还发现了从人类反馈强化学习（RLHF）中逆向缩放的首批示例之一，即更多的 RLHF 使 LM 变得更差。例如，RLHF 使 LM 表达更强烈的政治观点（关于持枪权和移民）以及更大的避免被关闭的欲望。总体而言，LM 撰写的评估质量很高，让我们能够快速发现许多新颖的 LM 行为。
  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations>)
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