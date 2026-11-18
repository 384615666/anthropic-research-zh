---
title: A General Language Assistant as a Laboratory for Alignment
url: https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment
date: Dec 1, 2021
category: Alignment
source: https://www.anthropic.com/research
---

# 通用语言助手：对齐研究的实验室

- **日期：** 
- **分类：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment

---

对齐研究（AlignmentResearch）
2021 年 12 月 1 日
[阅读论文](<https://arxiv.org/abs/2112.00861>)
## 摘要
鉴于大语言模型（Large Language Models）的广泛能力，我们应当能够开发出一种与人类价值观对齐（aligned）的通用文本助手，即它应当是有用（helpful）、诚实（honest）且无害（harmless）的。作为这一方向的初步探索，我们研究了简单的基线技术和评估方法，例如提示（prompting）。我们发现，适度干预带来的收益会随着模型规模的增大而增加，能够推广到各种对齐评估中，并且不会损害大模型的性能。接下来，我们研究了与对齐相关的几种训练目标的扩展趋势，比较了模仿学习（imitation learning）、二元判别（binary discrimination）和排序偏好建模（ranked preference modeling）。我们发现，排序偏好建模的表现远优于模仿学习，并且往往随模型规模扩展得更好。相比之下，二元判别在性能和扩展性上都与模仿学习非常相似。最后，我们研究了一个「偏好模型预训练」（preference model pre-training）阶段，目标是在基于人类偏好进行微调时提高样本效率。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment>)
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