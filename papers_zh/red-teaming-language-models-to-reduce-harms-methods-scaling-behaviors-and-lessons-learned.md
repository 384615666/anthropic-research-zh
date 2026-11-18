---
title: Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned
url: https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned
date: Aug 22, 2022
category: Societal Impacts
source: https://www.anthropic.com/research
---

# 对语言模型进行红队测试以减少危害：方法、扩展行为与经验教训

- **日期：**
- **分类：** 社会影响
- **来源：** https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned

---

社会影响
2022 年 8 月 22 日
[阅读论文](<https://arxiv.org/abs/2209.07858>)
## 摘要
我们描述了对语言模型进行红队测试（red teaming）的早期努力，目的是同时发现、测量并尝试减少它们可能有害的输出。我们做出了三项主要贡献。第一，我们研究了红队测试在 3 种模型规模（2.7B、13B 和 52B 参数）和 4 种模型类型上的扩展行为：普通语言模型（LM）；被提示为有用、诚实和无害的 LM；带拒绝采样的 LM；以及使用基于人类反馈的强化学习（RLHF）训练为有用和无害的模型。我们发现，RLHF 模型随着规模的扩大越来越难以红队测试，而其他模型类型则呈现随规模平缓的趋势。第二，我们发布了包含 38,961 次红队攻击的数据集，供他人分析和学习。我们提供了自己对数据的分析，发现了各种各样的有害输出，从攻击性语言到更隐蔽的有害的非暴力不道德输出。第三，我们详尽描述了我们在红队测试方面的指令、流程、统计方法和不确定性。我们希望这种透明度能够加速我们作为社区共同工作的能力，以便为如何对语言模型进行红队测试制定共同的规范、实践和技术标准。
## 政策备忘录
[红队测试政策备忘录](<https://www-cdn.anthropic.com/82564d4ec2451b2eed2e0796b7c658fc989f0c1a/Anthropic_RedTeaming.pdf>)
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned>)
## 相关内容
### 了解更多关于 Claude 数学能力的信息
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界：满足该猜想的黎曼 zeta 函数零点的比例，从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而设计的数字签名方案。第二次攻击确定了一种攻击减轮 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)