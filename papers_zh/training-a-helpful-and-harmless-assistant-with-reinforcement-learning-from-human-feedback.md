---
title: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
url: https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
date: Apr 12, 2022
category: Alignment
source: https://www.anthropic.com/research
---

# 使用来自人类反馈的强化学习训练一个乐于助人且无害的助手

- **日期：** 
- **分类：** Alignment（对齐）
- **来源：** https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback

---

Alignment（对齐）研究
2022年4月12日
[阅读论文](<https://arxiv.org/abs/2204.05862>)
## 摘要
我们应用偏好建模和来自人类反馈的强化学习（reinforcement learning from human feedback，RLHF）来微调语言模型，使其充当乐于助人且无害的助手。我们发现，这种对齐训练几乎提高了所有 NLP 评估中的表现，并且与 Python 编码和摘要等专业技能的训练完全兼容。我们探索了一种迭代在线训练模式，其中偏好模型和强化学习策略以每周为节奏用新的人类反馈数据更新，有效改进我们的数据集和模型。最后，我们研究了 RLHF 训练的鲁棒性，并确定了强化学习奖励与策略与其初始化之间的 KL 散度平方根之间大致线性的关系。除了我们的主要结果外，我们还对校准、相互竞争的目标和 OOD（分布外）检测的使用进行了外围分析，将我们的模型与人类作者进行了比较，并使用最近相关工作中的提示提供了我们模型的样本。
## 作者
Yuntao Bai、Andy Jones、Kamal Ndousse、Amanda Askell、Anna Chen、Nova DasSarma、Dawn Drain、Stanislav Fort、Deep Ganguli、Tom Henighan、Nicholas Joseph、Saurav Kadavath、Jackson Kernion、Tom Conerly、Sheer El-Showk、Nelson Elhage、Zac Hatfield-Dodds、Danny Hernandez、Tristan Hume、Scott Johnston、Shauna Kravec、Liane Lovitt、Neel Nanda、Catherine Olsson、Dario Amodei、Tom Brown、Jack Clark、Sam McCandlish、Chris Olah、Ben Mann、Jared Kaplan

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback>)
## 相关内容
### 深入了解 Claude 的数学能力
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的一个长期存在的下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为"量子计算机能够破解现有标准"的未来世界而构建的数字签名方案。第二次攻击确定了攻击轮数缩减版 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，以评估 AI 模型使用飞行无人机的能力，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)