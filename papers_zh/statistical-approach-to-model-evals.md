---
title: A statistical approach to model evaluations
url: https://www.anthropic.com/research/statistical-approach-to-model-evals
date: Nov 19, 2024
category: Evaluations
source: https://www.anthropic.com/research
---

# 模型评估的统计方法

- **日期：**
- **类别：** 评估（Evaluations）
- **来源：** https://www.anthropic.com/research/statistical-approach-to-model-evals

---

评估（Evaluations）
2024 年 11 月 19 日
[阅读论文](<https://arxiv.org/abs/2411.00640>)
假设一个 AI 模型在某个受关注的基准上优于另一个模型——例如，测试其通用知识，或解决计算机编码问题的能力。这种能力差异是真实的吗，还是某个模型只是在基准问题的选择上运气好？

鉴于公众对 AI 模型评估（非正式地称为「evals」）的兴趣之大，这个问题在 AI 研究界中出人意料地缺乏研究。本月，我们发表了一篇[新研究论文](<https://arxiv.org/abs/2411.00640>)，试图严格地回答这个问题。该论文借鉴统计理论和实验设计文献，向 AI 研究界提出了一些关于以科学信息方式报告评估结果的建议。在这篇文章中，我们简要介绍这些报告建议及其背后的逻辑。

## 建议 #1：使用中心极限定理
评估通常由数百或数千个不相关的问题组成。例如，[MMLU](<https://arxiv.org/abs/2009.03300v3>) 包含的问题五花八门：

  * 谁发现了第一种病毒？
  * 𝑓(𝑥)=4−5𝑥 的逆函数是什么？
  * 谁说过「法理学是法律的眼睛」？

为了计算总体评估分数，每个问题被单独评分，然后总体分数（通常）是这些问题分数的简单平均值。通常，研究者把注意力集中在这个观察到的平均值上。但在我们的论文中，我们认为真正感兴趣的对象不应该是_观察到的_平均值，而应该是所有可能问题上的_理论_平均值。因此，如果我们设想评估问题来自一个不可见的「问题宇宙」，我们就可以利用统计理论来了解该宇宙中的平均分数——也就是说，我们可以衡量潜在的_技能_，而不受「抽签运气」的影响。

![](assets/statistical-approach-to-model-evals/img_000.img)如果我们设想评估问题来自一个「问题宇宙」，那么评估分数将倾向于遵循正态分布，以所有可能问题的平均分数为中心。

这种表述为我们带来了分析上的稳健性：如果创建一个新评估，其问题与原始评估具有相同的难度分布，我们通常应该预期我们最初的结论仍然成立。

用技术术语来说：在中心极限定理（Central Limit Theorem）[相当温和的条件下](<https://en.wikipedia.org/wiki/Central_limit_theorem>)，从同一底层分布中抽取的几个随机样本的均值将倾向于遵循[正态分布](<https://en.wikipedia.org/wiki/Normal_distribution>)。该正态分布的标准差（或宽度）通常被称为[平均值的标准误差](<https://en.wikipedia.org/wiki/Standard_error>)（standard error of the mean，SEM）。在我们的论文中，我们鼓励研究者报告由中心极限定理推导出的 SEM，并附在每个计算出的评估分数旁边——我们还向研究者展示了如何使用 SEM 来量化两个模型之间理论均值的差异。通过从平均分数中加减 1.96 × SEM，可以从 SEM 计算出 95% 的[置信区间](<https://en.wikipedia.org/wiki/Confidence_interval>)。

## 建议 #2：聚类标准误差
许多评估违反了上述问题独立选择的假设，而是由紧密相关的问题组组成。例如，阅读理解评估中的几个问题可能询问同一段文本。遵循这种模式的流行评估包括 [DROP](<https://aclanthology.org/N19-1246/>)、[QuAC](<https://arxiv.org/abs/1808.07036>)、[RACE](<https://aclanthology.org/D17-1082/>) 和 [SQuAD](<https://arxiv.org/abs/1806.03822>)。

对于这些评估，每个问题从「问题宇宙」中的选择不再独立。因为包含关于同一段文本的几个问题所提供的信息，少于选择相同数量关于不同文本段落的问题，所以将中心极限定理天真地应用于非独立问题的情况，将导致我们低估标准误差——并可能误导分析者从数据中得出错误的结论。

幸运的是，[聚类标准误差](<https://en.wikipedia.org/wiki/Clustered_standard_errors>)问题已在社会科学中得到广泛研究。当问题的包含是非独立的时，我们建议在[随机化](<https://en.wikipedia.org/wiki/Randomization>)单位（例如文本段落）上对标准误差进行聚类，并且我们在论文中提供了适用的公式。

![](assets/statistical-approach-to-model-evals/img_001.img)如果问题以相关簇的形式出现——阅读理解评估中的常见模式——评估分数将比非聚类情况更分散。

在实践中，我们发现流行评估上的聚类标准误差可能是朴素标准误差的三倍以上。忽略问题聚类可能导致研究者无意中检测到实际上并不存在的模型能力差异。

## 建议 #3：减少问题内的方差
方差是衡量随机变量分散程度的指标。评估分数的方差是上述平均值的标准误差的平方；这个量取决于每个单独评估问题分数上的方差量。

我们论文的一个关键见解是将模型在特定问题上的分数分解为两个相加的项：

  * 平均分数（如果同一个问题被无限次询问，模型将达到的平均分数——即使模型每次可能产生不同的答案）；以及
  * 一个随机分量（已实现的问题分数与该问题的平均分数之间的差异）。

得益于[全方差定律](<https://en.wikipedia.org/wiki/Law_of_total_variance>)，减少随机分量的方差直接导致总体均值的标准误差更小，从而获得更高的统计精度。我们的论文根据模型在回答之前是否被要求逐步思考（一种称为 CoT 或思维链推理的提示技术），强调了减少随机分量方差的两种策略。

如果评估使用思维链推理，我们建议从同一模型多次重新采样答案，并使用问题级别的平均值作为输入中心极限定理的问题分数。我们注意到 [Inspect 框架](<https://github.com/UKGovernmentBEIS/inspect_ai/>)通过其 [_epochs 参数_](<https://inspect.ai-safety-institute.org.uk/scorers.html#sec-reducing-epochs>)正确地以这种方式计算标准误差。

![](assets/statistical-approach-to-model-evals/img_002.img)如果模型非确定性地产生答案，那么每个问题生成（并评分）多个答案将导致评估分数不那么分散。

如果评估不使用思维链推理（即其答案不是「路径依赖」的），我们注意到分数中的随机分量通常可以通过语言模型的下一词元概率完全消除。例如，如果一个选择题的正确答案是「B」，我们只需使用模型产生「B」这个词元的概率作为问题分数。我们不知道有任何开源评估框架实现了这种技术。

## 建议 #4：分析配对差异
评估分数本身没有任何意义；它们只有在彼此相关时才有意义（一个模型优于另一个模型，或与另一个模型打平，或优于一个人）。但是，两个模型之间的测量差异可能是由评估中问题的具体选择，以及模型答案的随机性造成的吗？我们可以使用[双样本 t 检验](<https://en.wikipedia.org/wiki/Student%27s_t-test>)，仅使用从两个评估分数计算出的平均值标准误差来确定。

然而，双样本检验忽略了评估数据内部的隐藏结构。由于问题列表在模型之间是共享的，进行[配对差异检验](<https://en.wikipedia.org/wiki/Paired_difference_test>)可以让我们消除问题难度的方差，专注于回答的方差。在我们的论文中，我们展示了配对差异检验的结果将如何与两个模型问题分数之间的[皮尔逊相关系数](<https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>)相关。当相关系数更高时，平均差的标准误差将更小。

在实践中，我们发现前沿模型在流行评估上的问题分数相关性相当大——在 −1 到 +1 的量表上介于 0.3 和 0.7 之间。换句话说，前沿模型总体上倾向于在同一批问题上对或错。因此，配对差异分析代表了一种非常适合 AI 模型评估的「免费」方差减少技术。因此，为了从数据中提取最清晰的信号，我们的论文建议在比较两个或多个模型时报告配对信息——平均差、标准误差、置信区间和相关性。

## 建议 #5：使用功效分析
统计显著性的另一面是统计功效，即统计检验在假设差异存在的情况下检测两个模型之间差异的能力。如果评估没有很多问题，与任何统计检验相关的置信区间往往会很宽。这意味着模型需要有较大的潜在能力差异才能产生统计显著的结果——而小的差异很可能不会被检测到。功效分析指的是观察次数、[统计功效](<https://en.wikipedia.org/wiki/Power_\(statistics\)>)、[假阳性率](<https://en.wikipedia.org/wiki/False_positive_rate>)和所关注的[效应量](<https://en.wikipedia.org/wiki/Effect_size>)之间的数学关系。

在我们的论文中，我们展示了如何将功效分析的概念应用于评估。具体来说，我们向研究者展示了如何提出一个假设（如_模型 A 比模型 B 高出 3 个百分点_）并计算评估应该包含多少问题，才能针对零假设（如_模型 A 和模型 B 打平_）检验这个假设。

我们相信功效分析将在许多情况下被证明对研究者有帮助。我们的功效公式将告知模型评估者从问题中重新采样答案的次数（见上面的建议 #3），以及随机子样本中在保留所需功效属性的同时可以包含的问题数量。研究者可能会使用功效公式得出结论：一个可用问题数量有限的评估不值得在特定的一对模型上运行。新评估的开发者可能希望使用该公式来帮助决定包含多少问题。

## 结论
统计学是在存在噪声的情况下进行测量的科学。评估带来了许多实际的[挑战](<https://www.anthropic.com/news/evaluating-ai-systems>)，而真正的[评估科学](<https://www.apolloresearch.ai/blog/we-need-a-science-of-evals>)仍然发展不足。统计学只能构成评估科学的一个方面——但它是关键的一个方面，因为一门实证科学的好坏取决于其测量工具。我们希望我们论文 [**为评估添加误差线：语言模型评估的统计方法**](<https://arxiv.org/abs/2411.00640>)中的建议，将帮助 AI 研究者比以往更精确、更清晰地计算、解读和交流评估数字——我们也鼓励 AI 社区的研究者探索实验设计中的其他技术，以便他们能更准确地理解他们想要测量的所有内容。


[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/statistical-approach-to-model-evals>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/statistical-approach-to-model-evals>)
## 相关内容
### 了解更多关于 Claude 数学能力的信息
Claude 的一个未发布的研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的一个长期未破的下界，将其从 41.6% 提高到 67.2%。
[了解更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二个攻击发现了一种攻击轮数缩减的 AES（使用最广泛的对称密码）的新方法。
[了解更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能操控无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估来测试 AI 模型使用飞行无人机的能力，最终形成了一个新的基准：Drone-Bench。
[了解更多](</research/project-pilot>)