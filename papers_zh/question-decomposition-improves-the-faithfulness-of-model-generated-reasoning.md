---
title: Question Decomposition Improves the Faithfulness of Model-Generated Reasoning
url: https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning
date: Jul 18, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# 问题分解提高模型生成推理的忠实性

- **日期：** 
- **类别：** 对齐
- **来源：** https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning

---

对齐｜研究
2023 年 7 月 18 日
[下载论文](<https://www-cdn.anthropic.com/8154fb1d828cdc390dc1fa442d84034948679c47/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning.pdf>)
## 摘要
随着大语言模型（LLM）执行越来越困难的任务，验证其行为的正确性和安全性变得越来越难。有助于解决这一问题的一种方法是提示 LLM 外化其推理，例如让它们在回答问题（思维链；CoT）时生成逐步推理。这种推理可能使我们能够检查模型用于执行任务的过程。然而，这种方法依赖于所述推理忠实反映模型的实际推理，而这并非总是如此。为了提高 CoT 推理的忠实性，我们让模型通过把问题分解为子问题来生成推理。基于分解的方法在问答任务上取得了强劲的表现，有时接近 CoT 的水平，同时在几个最近提出的指标上提高了模型所述推理的忠实性。通过强制模型在单独的上下文中回答更简单的子问题，我们大大提高了模型生成推理相对于 CoT 的忠实性，同时仍然获得 CoT 的一些性能增益。我们的结果表明，提高模型生成推理的忠实性是可能的；持续的改进可能带来使我们能够验证 LLM 行为正确性和安全性的推理。
  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未发布的研究版 Claude 在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二次攻击确定了一种攻击轮数缩减 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新测试，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)