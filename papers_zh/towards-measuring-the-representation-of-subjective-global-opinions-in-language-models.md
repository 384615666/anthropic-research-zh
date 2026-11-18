---
title: Towards Measuring the Representation of Subjective Global Opinions in Language Models
url: https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models
date: Jun 29, 2023
category: Societal Impacts
source: https://www.anthropic.com/research
---

# 迈向测量语言模型中对主观全球观点的表征

- **日期：** 
- **分类：** 社会影响（Societal Impacts）
- **来源：** https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models

---

社会影响（Societal Impacts）
2023 年 6 月 29 日
[阅读论文](<https://arxiv.org/abs/2306.16388>)
## 摘要
大语言模型（Large Language Models，LLMs）可能无法公平地表征不同国家对社会议题的多样化全球观点。在本文中，我们开发了一个定量框架，用于评估模型生成的回答与哪些人群的观点更为相似。我们首先构建了一个数据集 GlobalOpinionQA，其中包含来自跨国调查的问题和答案，旨在捕捉不同国家在全球议题上的多样化观点。接下来，我们定义了一个指标，用以量化以国家为条件的 LLM 生成的调查回答与人类回答之间的相似度。借助这一框架，我们在一台通过宪法式 AI（Constitutional AI）训练为有用、诚实且无害的 LLM 上进行了三项实验。默认情况下，LLM 的回答往往与某些人群的观点更为相似，例如来自美国以及一些欧洲和南美国家的人群，这凸显了潜在的偏差。当我们提示模型考虑某一特定国家的视角时，回答会变得更接近被提示人群的观点，但可能反映出有害的文化刻板印象。当我们将 GlobalOpinionQA 的问题翻译成目标语言时，模型的回答并不一定会变得与使用这些语言的人群的观点最为相似。我们公开发布数据集，供他人使用和在此基础上继续研究。我们的数据位于[此 URL](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>)。我们还在此 URL 提供了交互式可视化：[此 URL](<https://llmglobalvalues.anthropic.com/>)。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models>)
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