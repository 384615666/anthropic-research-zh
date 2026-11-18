---
title: Measuring Faithfulness in Chain-of-Thought Reasoning
url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
date: Jul 18, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# 衡量思维链推理中的忠实性

- **日期：** 
- **分类：** Alignment（对齐）
- **来源：** https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning

---

Alignment（对齐）研究
2023年7月18日
[下载论文](<https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf>)
## 摘要
大语言模型（LLM）在回答问题之前产生逐步的"思维链（Chain-of-Thought，CoT）"推理时表现更好，但目前尚不清楚所陈述的推理是否是模型实际推理（即其回答问题的过程）的忠实解释。我们通过检查当我们干预思维链时（例如添加错误或改写它）模型预测如何变化，来研究思维链推理可能不忠实的假设。模型在预测答案时对思维链的依赖程度在不同任务间表现出很大差异，有时严重依赖思维链，有时主要忽略它。思维链的性能提升似乎不仅来自思维链增加的测试时计算量，也不仅来自通过思维链特定措辞编码的信息。随着模型变得更大、更有能力，它们在我们研究的大多数任务上产生更不忠实的推理。总的来说，我们的结果表明，如果仔细选择模型大小和任务等条件，思维链可以是忠实的。
  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning>)
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