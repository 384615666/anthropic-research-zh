---
title: Evaluating and Mitigating Discrimination in Language Model Decisions
url: https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions
date: Dec 7, 2023
category: Societal Impacts
source: https://www.anthropic.com/research
---

# 评估与缓解语言模型决策中的歧视

- **日期：** 
- **类别：** 社会影响
- **来源：** https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions

---

社会影响
2023 年 12 月 7 日
[阅读论文](<http://arxiv.org/abs/2312.03689>)
## 摘要
随着语言模型（LM）的进步，人们越来越有兴趣将其应用于高风险的社-会决策，如确定融资或住房资格。然而，它们在此类情境中的歧视潜力引发了伦理关切，促使我们需要更好的方法来评估这些风险。我们提出了一种方法，用于在广泛用例中主动评估 LM 的潜在歧视影响，包括它们尚未部署的假设用例。具体来说，我们使用一个 LM 来生成决策者可能输入到 LM 中的各种潜在提示词，覆盖社会中 70 个多样化的决策场景，并系统性地变化每个提示词中的人口统计信息。应用这种方法揭示了在不施加任何干预的情况下，Claude 2.0 模型在选定设置中的正向和负向歧视模式。虽然我们不认可或允许使用语言模型为我们所研究的高风险用例做出自动化决策，但我们展示了通过仔细的提示词工程显著减少正向和负向歧视的技术，为可能适合的用例中的更安全部署提供了途径。我们的工作使开发者和政策制定者能够在语言模型能力和应用不断扩展时预测、衡量和解决歧视问题。我们在此发布我们的数据集和提示词：[此处](<https://huggingface.co/datasets/Anthropic/discrim-eval>)。
## 政策备忘录
[评估与缓解语言模型决策中的歧视政策备忘录](<https://www-cdn.anthropic.com/f0dfb70b9b309d7c52845f73da8d964140669ff7/Anthropic_DiscriminationEval.pdf>)
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions>)
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