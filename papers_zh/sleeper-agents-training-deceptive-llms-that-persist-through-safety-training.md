---
title: Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
url: https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training
date: Jan 14, 2024
category: Alignment
source: https://www.anthropic.com/research
---

# 潜伏智能体：训练能够在安全训练中存续的欺骗性 LLM

- **日期：** 
- **类别：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training

---

对齐研究（AlignmentResearch）
2024 年 1 月 14 日
[阅读论文](<https://arxiv.org/abs/2401.05566>)
人类有能力进行策略性欺骗行为：在大多数情况下表现乐于助人，但在有机会时表现得非常不同，以追求替代目标。如果一个 AI 系统学会了这样的欺骗策略，我们能否使用当前最先进的安全训练技术检测到它并将其移除？为了研究这个问题，我们构建了大型语言模型（LLM）中欺骗行为的概念验证示例。例如，我们训练出的模型在提示中说明年份为 2023 时会编写安全代码，但在说明年份为 2024 时会插入可利用的代码。我们发现，这种后门行为可以变得持久，以至于它不会被标准的安全训练技术移除，包括监督微调、强化学习和对抗训练（引出不安全行为然后训练以移除它）。后门行为在最大的模型中以及在被训练为产生关于欺骗训练过程的思维链推理的模型中最为持久，即使思维链被蒸馏掉，持久性仍然存在。此外，我们发现对抗训练不是移除后门，而是可以教会模型更好地识别其后门触发器，从而有效地隐藏不安全行为。我们的结果表明，一旦模型表现出欺骗行为，标准技术可能无法移除这种欺骗，并会制造出一种虚假的安全印象。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training>)
## 相关内容
### 深入了解 Claude 的数学能力
一个未发布的 Claude 研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例这一长期存在的下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二次攻击发现了一种攻击缩减轮数 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新测试，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)