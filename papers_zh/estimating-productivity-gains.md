---
title: Estimating AI productivity gains from Claude conversations
url: https://www.anthropic.com/research/estimating-productivity-gains
date: Nov 25, 2025
category: Economic Research
source: https://www.anthropic.com/research
---

# 从 Claude 对话估算 AI 生产力增益

- **日期：**
- **分类：** 经济研究
- **来源：** https://www.anthropic.com/research/estimating-productivity-gains

---

经济研究
2025 年 11 月 25 日
[阅读 PDF 版](<https://www-cdn.anthropic.com/e5645986a7ce8fbcc48fa6d2fc67753c87642c30.pdf>)
![从 Claude 对话估算 AI 生产力增益](assets/estimating-productivity-gains/img_000.img)
## 概述
_与 Claude 的真实对话能告诉我们关于 AI 对劳动生产率影响的什么信息？利用我们保护隐私的[分析方法](<https://www.anthropic.com/research/clio>)，我们从 [Claude.ai](<http://claude.ai/redirect/website.v1.885f58b9-7bdd-416a-89ac-4517a9d2f952>) 中抽样了十万个真实对话，估算这些对话中的任务在有和没有 AI 帮助的情况下各需要多长时间完成，并研究其对更广泛经济的生产力影响。根据 Claude 的估算，这些任务在没有 AI 帮助的情况下平均大约需要 90 分钟完成，而 Claude 将单个任务的速度提高了约 80%。_
_将这些估算外推表明，**当前一代**的 AI 模型可能在未来十年内使美国劳动生产率增长每年提高 1.8%_——_大约是近年增速的两倍。但这并不是对未来的预测，因为我们没有考虑采用率，也没有考虑更强大的 AI 系统会带来的更大生产力效应。_
_我们的分析存在局限。最值得注意的是，我们无法计入人类在 Claude 对话之外花费在任务上的额外时间，包括验证 Claude 工作的质量或准确性。但随着 AI 模型在时间估算方面变得更好，我们认为本研究报告中的方法可能越来越有助于理解 AI 如何塑造真实的工作。_
_以下是我们的结果更详细的摘要：_
  * **在十万个真实世界对话中，Claude 估计 AI 将任务完成时间减少了 80%。** 我们使用 Claude 来评估匿名化的 Claude.ai 记录，以估算 AI 的生产力影响。根据 Claude 的估算，人们通常将 AI 用于复杂的任务，这些任务平均需要人们 1.4 小时才能完成。通过将任务与 O*NET 职业和 BLS 工资数据匹配，我们估计这些任务原本需要 55 美元的人力成本。
  * **任务的预计规模、成本和节省时间因职业而异。** 根据 Claude 的估算，人们将 Claude 用于原本需要近两小时的法律和管理任务，但用于只需要 30 分钟的食品准备任务。我们发现医疗保健辅助任务可以快 90% 完成，而硬件问题的节省时间为 56%。然而，这没有计入人类可能在 [Claude.ai](<http://claude.ai/redirect/website.v1.885f58b9-7bdd-416a-89ac-4517a9d2f952>) 对话_之外_花在这些任务上的时间，因此我们认为这些估算至少在一定程度上可能高估了当前的生产力效应。
  * **将这些结果外推到经济层面，当前一代的 AI 模型可能在未来十年内使美国年度劳动生产率增长提高 1.8%。这将使美国自 2019 年以来每年的增长翻一番，** **并使我们的估算处于[近期估算](<https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/miracle-or-myth-assessing-the-macroeconomic-productivity-gains-from-artificial-intelligence_fde2a597/b524a072-en.pdf>)的上端。** 在给定 Claude 对任务层面效率增益估算的前提下，我们使用标准方法计算出美国劳动生产率未来十年隐含的年增长率提高 1.8%。然而，这一估算没有考虑 AI 模型未来的改进（或对现有技术更复杂的使用），而这些可能会显著放大 AI 的经济影响。
  * **随着 AI 加速某些任务，其他任务可能成为瓶颈**：我们看到某些任务获得了巨大的加速，而另一些任务（即使在同一职业群体内）的加速则小得多。在 AI 作用不大的地方，这些任务可能成为瓶颈，从而对增长构成制约。
**这为我们提供了一个新的视角来理解 AI 的经济影响如何随时间演变，我们将作为 [经济指数](<https://www.anthropic.com/economic-index>)（Economic Index）的一部分持续追踪：** 基于真实世界的 Claude 对话来计算这些估算，给了我们一个理解 AI 生产力的新视角。这补充了其他方法，例如窄领域中的实验室研究，或提供更粗略洞见的政府统计。我们将追踪这些估算随时间的变化，以便在能力和采用不断推进的过程中，获得对这些问题的动态认识。
![](assets/estimating-productivity-gains/img_001.img)我们方法的概览和一些主要结果。关于我们如何验证 Claude 的估算、我们所做的假设以及分析的局限，请参见下文。
## 引言
作为 [Anthropic 经济指数](<https://www.anthropic.com/economic-index>)的一部分，我们记录了人们如何在不同任务、行业和地点使用 Claude。我们捕捉到了使用的**广度**——人们如何将 Claude 用于法律、科学和编程任务——但没有捕捉到**深度**。人们使用 Claude 处理的任务有多重要，Claude 为他们节省了多少时间？
当前版本的经济指数无法捕捉这种**任务内异质性**——例如，它无法区分需要五分钟的报告写作任务和需要五天的报告写作任务，也无法区分需要一个下午的财务建模任务和需要几周的财务建模任务。这使得评估 AI 的经济效应变得困难：一位软件开发人员可能一天内用 Claude 写十个拉取请求（pull request），但如果其中九个是次要的文档更新，而一个是关键的基础设施变更，那么仅仅计算用 Claude 完成的任务数量就偏离了重点。
不仅如此，随着模型能力的提升，我们想了解它们是否在从事更高价值的工作。要理解 AI 如何重塑工作和生产力，我们不仅需要知道 Claude 处理了_哪些_任务，还需要知道这些任务和节省的时间有多_大_。
一些团队已经开始进行随机对照试验，以衡量窄领域中的生产力增益，包括[软件](<https://arxiv.org/abs/2302.06590>)[工程](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566>)[任务](<https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>)、[写作](<https://www.science.org/doi/10.1126/science.adh2586>)和[客户服务](<https://www.nber.org/papers/w31161>)。METR 关于[衡量 AI 完成长任务能力](<https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/>)的工作已经证明，AI 系统能够独立应对扩展的多步骤挑战。但这些评估考虑的是一组狭窄的问题，而非广泛的现实世界使用。要评估 AI 对经济的_总体_影响，我们需要一种能够分析数百或数千个现实世界 AI 应用的方法。
本报告向这一目标迈出了第一步。它使用 Claude 来估算人类完成 Claude 处理的任务需要多少时间，并将其与 Claude 和人类一起完成所花的时间进行比较，从而计算出 AI 节省了多少时间。虽然 AI 模型缺乏关于用户专业知识、工作流程和约束的背景信息，但我们发现，对于一个软件工程任务数据集，模型估算的时间相对于人类估算的完成时间和实际计时结果，都显示出有前景的准确性。
在下文中，我们介绍估算任务层面时间节省的方法论，对照真实数据验证我们的方法，然后使用这些估算来评估哪些任务和职业从 AI 中获得了最大的生产力增益。接着，我们探讨我们的任务层面估算对 AI 开始在整个经济中被采用时总体生产力的意义。
## 估算任务时长和节省的时间
利用我们的[隐私保护分析系统](<https://www.anthropic.com/research/clio>)，我们分析了来自 Claude.ai（Free、Pro 和 Max 层级）的 100,000 份对话记录，以衡量 Claude 处理的任务的时长和节省的时间。我们为每个任务生成了两个核心估算：
  * **没有 AI 的时间估算**：人类专业人士在没有 AI 帮助的情况下完成任务所需的工时
  * **有 AI 的时间估算**：在 AI 帮助下完成任务所花的时间
我们使用 Claude 为每个对话生成这些估算。遵循我们的[经济指数方法论](<https://www.anthropic.com/news/the-anthropic-economic-index>)，我们随后通过对每个任务的时间估算取中位数，将这些单独的聊天对话聚合成 [O*NET](<https://www.onetcenter.org/database.html>) 分类体系中的任务。这使我们能够探索这些时间估算如何随经济中的任务和职业而变化。分类提示词见附录。
分析真实世界的记录使我们能够计入_任务内变异_。例如，即使_设计制造设备_任务的总体份额保持不变，记录层面的信息也能让我们看到人们是否在用 AI 处理更复杂、时间跨度更长的项目（或获得更大的时间节省）。我们的[经济指数](<https://www.anthropic.com/economic-index>)将追踪这些估算随时间的变化，并共享汇总数据集，供研究人员用来做出自己的预测和结论。
### 验证
估算任务时长对人类来说[是出了名的困难](<https://web.mit.edu/curhan/www/docs/Articles/biases/67_J_Personality_and_Social_Psychology_366,_1994.pdf>)。AI 模型的任务更加困难，因为它们缺乏关于任务更广泛背景的关键信息（尽管随着[记忆](<https://www.anthropic.com/news/memory>)和[外部集成](<https://www.anthropic.com/news/claude-and-slack>)等功能变得更加全面，我们预计这种背景会随着时间增加）。为了评估 Claude 的估算是否具有参考价值，我们进行了两项验证分析。
**自一致性测试：** 首先，我们评估 Claude 在不同对话样本或提示词变体之间是否产生稳定的任务时长估算。
我们创建了多种提示词变体——例如，询问“具有适当技能的员工”与“熟练的专业人士”——以评估估算对提示词措辞方式的敏感程度。我们用每个变体分析了 1,800 个对话（用户已同意与我们分享这些对话），并计算了各提示词变体之间的相关性。结果显示强烈的一致性，各变体之间的对数尺度相关性为 _r_ =0.89–0.93。
![](assets/estimating-productivity-gains/img_002.img)**Claude 估算的人类完成时间在各提示词变体之间显示出高相关性。** 提示词 1 要求 Claude 估算一位“具有适当技能的员工”完成任务所需的时间，提示词 2 询问一位“在相关领域胜任”的“人类工作者”。两个提示词显示 0.89 的对数尺度相关性，表明高度一致。分析基于 [Claude.ai](<http://claude.ai/redirect/website.v1.885f58b9-7bdd-416a-89ac-4517a9d2f952>) 中用户同意为研究目的与我们分享的记录。
**外部基准测试：** 如果模型的预测与现实不符，自一致性就意义不大。为了检验这一点，我们用一个来自开源仓库 JIRA 工单、包含数千个真实世界[软件开发任务](<https://zenodo.org/records/7022735>)的数据集测试了 Claude 的时间估算能力，该数据集既有开发者的估算，也有实际记录的完成时间。
这对 Claude 来说是一项极具挑战性的任务，因为 Claude 只收到 JIRA 工单的标题和描述，而人类开发者拥有代码库和工单的完整背景，并且知道类似任务需要多长时间才能完成。在该基准的 1000 个任务子集上：
  * 人类开发者自身与实际时间的 Spearman 相关性达到 ρ=0.50，对数值的 Pearson 相关性达到 r_log=0.67，表明中等强度的相关性（两个值都是越高越好）。
  * Claude Sonnet 4.5 达到 ρ=0.44 和 r_log=0.46
  * 在提示词中给出十个任务及其真实时长示例的 Claude Sonnet 4.5 显示 ρ=0.39 更差，但 r_log 提高到 0.48
这一分析表明，Claude 的估算提供了_方向性_信息，仅略逊于软件开发人员自己的估算。然而，我们观察到 Claude 的估算比人类更压缩——对较短的任务预测相对较长的时间，反之亦然——并且总体上更容易高估。这表明任务之间的实际时长差异可能比我们报告的更大，而且实际任务时长可能略短。总体而言，这些发现表明，至少在这个领域，模型预测与现实世界结果具有有意义的相关性，使其可用于比较一个任务与另一个任务，或追踪随时间的变化。我们还观察到 Claude Sonnet 4.5 的相关性高于 Claude Sonnet 4，表明这些估算可能随着模型能力的提升而继续改善。
![](assets/estimating-productivity-gains/img_003.img)软件工程任务实际花费时间与开发者和 Claude 估算的相关性。左图：与开发者初始时间估算的相关性（对照最终的时间记录结果）。开发者熟悉完整代码库，理解请求背后的全部背景，也知道类似任务花费了多长时间。中图：仅给定 JIRA 工单的标题和描述时，与 Claude Sonnet 4.5 估算的相关性。右图：在提示词中给出 10 个示例用于校准后，与 Claude Sonnet 4.5 估算的相关性。总体而言，Claude 的估算与开发者的方向性相关性相似：Spearman _ρ_ =0.44，而开发者是 _ρ_ =0.50，尽管 Claude 显著高估短任务、低估长任务。坐标轴为对数（以 10 为底）刻度。误差条为每箱的 95% 置信区间。
## 结果
我们首先使用上述方法估算任务层面的节省，然后将这些聚合成经济范围效应的估算。
### 任务层面的节省
![](assets/estimating-productivity-gains/img_004.img)Claude 估算的任务时间、职业的平均时薪、隐含的任务成本，以及九个不同任务的时间节省。**任务时间**是通过让 Claude 预测一位专业人士在没有 AI 帮助的情况下执行任务所需的时间来估算的。**时薪**来自 2024 年 5 月的职业就业与工资统计（Occupational Employment and Wage Statistics，OEWS）数据。**任务成本**由任务时间乘以时薪计算得出。**时间节省**通过估算人类完成任务所花时间并计算 _1 - 有AI时间 / 无AI时间_ 得出。
#### 示例任务展示了不同程度的时间节省
查看职业内的单个任务，可以为我们提供关于 AI 可能在哪些方面以及如何节省时间的具体例子。在最极端的案例中，我们看到用户用仅 11 分钟完成了 Claude 认为需要 4.5 小时的课程开发任务。根据教师的平均时薪，这类任务的隐含劳动力成本为 115 美元。
人们还用 AI 节省了 87% 编写发票、备忘录和其他文档（至少是 Claude 被要求处理的那类文档）所需的时间。最后，AI 在财务分析师任务（如解读财务数据，此类任务原本需要 31 美元工资成本）上节省了 80% 的时间。
#### 任务时长在不同职业之间差异巨大
人类时间估算显示，Claude 处理的任务根据职业不同，时长差异很大。在下图中，我们展示了使用 Claude 的任务子集中每个职业类别的平均值¹。使用 Claude 的平均管理任务（例如选择投资）估计需要人类 2.0 小时完成，其次是法律（1.8 小时）、教育（1.7）和艺术/媒体任务（1.6）。在光谱的另一端，食品准备任务（例如规划菜单项目或为其定价）、安装/维护和运输任务平均只需 0.3-0.5 小时，表明这些是更受限的任务，或等待时间较少的任务。鉴于 Claude 的时间估算往往低估长任务、高估短任务，这些差异在实践中可能甚至更大。
![](assets/estimating-productivity-gains/img_005.img)根据 Claude 对 SOC 主要组的时间估算得出的各种数据。人类时间估算在不同职业之间差异显著——人们将 Claude 用于管理类和法律类任务，这些任务在没有辅助的情况下估计需要人类约 2 小时，而医疗保健支持和食品准备任务平均约半小时。职业类别的平均时薪来自 OEWS 2024 数据。平均任务成本通过将每个职业的时薪乘以其任务时间中位数，并按各任务在样本中的出现率加权计算平均值得出。时间节省通过 _1 - 有AI时间 / 无AI时间_ 计算。
成本估算放大了 AI 影响的这种差异：时间估算最长的任务往往也是劳动力成本最高的任务。我们通过将每个任务的中位时间乘以 OEWS 2024 年 5 月数据中相关职业的平均工资来计算这些成本估算。平均管理任务对专业人士来说将花费 133 美元，法律任务为 119 美元，与食品准备和服务相关的任务为 8 美元。商业和金融任务平均为 69 美元，而计算机和数学任务平均为 82 美元。
在我们观察的所有任务中，我们估计 Claude 处理的工作在每次对话中，聘请专家完成这些工作所需的专业劳动力成本中位数为 54 美元。当然，对于许多任务，当前模型的实际表现可能不如人类专家，尽管最近的研究表明[差距正在缩小](<https://openai.com/index/gdpval/>)。
在主要职业群体中，我们观察到样本中任务/职业的平均时薪与 Claude 被要求处理任务的人类等效时长之间存在正相关。例如，管理和法律职业类别在平均时薪方面排在分类的顶端——这与 Claude 在复杂知识工作上的优势相一致。
![](assets/estimating-productivity-gains/img_006.img)职业类别的平均时薪与样本中 Claude 估算的平均任务时长之间的相关性。在我们的样本中，高工资职业类别（如管理和法律）的任务使用更复杂（_r_ =0.8）。
#### 时间节省在不同职业之间高度不均
我们的人类时间和成本估算捕捉了人们用 AI 处理任务的_规模_。但节省的_时间_——Claude 对用 AI 工作能快多少的估算——反映了使用 AI 处理这些任务可能带来的生产力增益。
中位数对话经历了约 84% 的估算时间节省，尽管我们看到任务和类别之间存在相当大的差异。例如，检查诊断影像的任务只显示 20% 的时间节省，这可能是因为这已经是一项专家在没有 AI 帮助的情况下可以快速完成的任务。相比之下，从报告中汇编信息的任务约有 95% 的时间节省，这可能是因为 AI 系统阅读、提取和引用信息的速度远快于人类。总体而言，按任务划分的节省时间分布集中在 50-95% 范围内，在 80-90% 之间达到峰值。
这些巨大的时间节省与 Claude 阅读和写作速度远超人类的能力一致。然而，我们的方法没有考虑人们为将 Claude 的输出精炼到最终状态而需要做的额外工作，也没有考虑他们是否会在多个会话中继续迭代工作成果——这两者都会导致更小的时间节省。过去的随机对照试验通常发现较小的时间节省，包括不同应用中的[56%](<https://arxiv.org/abs/2302.06590>)、[40%](<https://www.science.org/doi/10.1126/science.adh2586>)、[26%](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566>)、[14%](<https://www.nber.org/papers/w31161>)甚至[负值](<https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>)——这可能是由于这些效应，也可能是因为这些研究考察的是较早几代的模型。
![](assets/estimating-productivity-gains/img_007.img)样本中 O*NET 任务时间节省的密度图。我们看到 Claude 估算的时间节省在我们的样本中是不均匀的，大多数落在 50% 到 95% 之间。总体中位数节省为 81%。时间节省通过 _1 - 有AI时间 / 无AI时间_ 计算。我们的估算没有考虑在聊天窗口之外精炼 Claude 输出所花的时间。
### 从任务层面的效率增益到经济范围的生产力效应
上述估算捕捉了任务层面的 AI 驱动的生产力增益。为了理解宏观层面的影响，本节对这些增益如何在整个经济中聚合进行建模，假设它们按照 Claude 的估算实现。
#### 方法论
为了估算经济范围的生产力效应，我们使用 Hulten 定理（Hulten's theorem），这是一种标准方法，使我们能够将任务层面的效率增益聚合到更广泛的美国经济²。与 [Acemoglu (2024)](<https://economics.mit.edu/sites/default/files/2024-04/The%20Simple%20Macroeconomics%20of%20AI.pdf>) 的“基线”方法一样，我们将隐含的劳动生产率增长建模为任务层面生产力增益的加权平均——这一建模选择隐含地假设，与 AI 采用相关的全要素生产率（TFP）提高将导致资本投资增加。在这个框架中，隐含的 TFP 增长等于劳动生产率增益乘以劳动收入份额³。
**任务构成**：对于每个职业，我们从 O*NET 获得工作任务列表。然后我们使用 Claude 来估算工人的时间花在每项任务上的比例。例如，Claude 估计程序员将 23% 的时间用于编写和维护代码，15% 用于分析和重写程序，以及较小的比例用于测试、文档和会议。
**任务层面的生产力改进**：在上一节中，我们提供了可用于计算每个任务在 AI 帮助下完成速度快多少的估算。我们取无 AI 时间与_有_ AI 时间之间的对数差，以生成生产力改进值，并保守地将样本中未观察到的任务赋为零改进。
**经济范围估算**：我们用两个因素对每个任务的隐含生产力增益按经济重要性加权：(i) Claude 估算的职业花在该任务上的时间比例（如上所述），以及 (ii) 该职业在美国总工资账单中的份额（该职业类别的就业人数乘以平均工资，再除以所有职业的总工资账单）。对于总工资账单，我们使用 2024 年 5 月的 OEWS 数据。这种方法隐含地假设 Claude 产生的时间估算代表了每个任务所有实例的可靠平均值，并且 Claude 或类似的 AI 系统将在整个美国经济中被采用。
![](assets/estimating-productivity-gains/img_008.img)**美国经济范围劳动生产率影响：十大职业。** 总体而言，Claude 的估算意味着，假设当前 AI 系统被普遍采用来处理我们观察到的所有任务，美国劳动生产率将实现 1.8% 的年化增长（虚线），主要由软件、管理、营销和客户服务任务驱动。这对应于隐含的 1.08% 年化 TFP 增长。平均 _ln(时间估算比率)_ 表示每个职业所有任务的时间加权生产力增益，其中 _时间估算比率 = 有AI时间 / 无AI时间_。劳动力统计来自 OEWS 2024 数据。
### 发现
假设 AI 需要 10 年才能在美国经济中实现普遍采用——并使用当前模型——我们计算出 Claude 的估算意味着美国劳动生产率每年增长 1.8%。这将使当前长期增长率几乎翻倍，后者自 1947 年以来平均每年 2.1%，自 2019 年以来为 1.8%。假设劳动占全要素生产率的份额为 0.64，这意味全要素生产率每年总体增长 1.1%⁵。鉴于自 21 世纪初以来 TFP 增长往往低于 1%，这些估算表明，即使广泛部署当前的 AI 系统也可能使增长翻倍：达到 1990 年代末以及 1960 年代和 1970 年代的速率⁵。
任务层面效率增益所隐含的总体劳动生产率增长估算，处于近期关于 AI 对生产力潜在影响的估算范围内，尽管它位于上端（Filippucci, Gal, and Schief, 2024）。
重要的是，这一推演假设 AI 能力（以及人类使用 AI 的有效性）在未来 10 年内与我们抽样时保持不变。然而，这似乎不太可能成立：我们认为 AI 将在未来几年[继续快速改进](<https://www.anthropic.com/news/core-views-on-ai-safety>)。
因此，这一估算应被视为一项基于_当前使用模式_探索可能发生什么的推演，而不是对实际最可能发生的生产力影响的预测。正如我们在其他工作中写到的，我们仍然对 AI 造成重大劳动力市场干扰的可能性保持高度警觉，这种干扰可能伴随着 AI 带来的更大生产力增长。随着模型的进步，这可以代表 AI 生产力效应的一个近似下限，尽管我们的估算没有考虑采用的不均衡性，这可能会在短期内降低现实世界的生产力增益。
![](assets/estimating-productivity-gains/img_009.img)非农商业部门的劳动生产率增长。图表显示了劳动生产率同比百分比变化的五年移动平均值。我们看到从 1960 年代的近 3% 总体下降到过去几年的约 1.5%。
反映[某些任务和职业在我们的数据中出现的频率远高于其他任务和职业](<https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf>)这一事实，我们在职业对劳动生产率的贡献中也观察到类似现象。软件开发人员对可归因于 AI 的总体劳动生产率增益的贡献最大（19%）。总经理和运营经理（约 6%）、市场研究分析师和营销专家（5%）、客户服务代表（4%）和中学教师（3%）组成了前五名。
相比之下，餐饮、医疗服务、建筑和零售对总体生产力效应的贡献要小得多。这主要是因为它们的任务很少出现在我们的数据中——很大程度上是因为这些职业在我们的样本中相关的任务很少。
### AI 可能如何改变工人分配时间的方式？
如果工人能够用 AI 加速其职业任务中的一部分，那么 AI 加速较小的任务可能会在这些职业的工作中占据更大、因而更重要的份额。例如，AI 可能帮助房屋检查员准备报告，但如果检查员仍然需要花同样多的时间亲自前往房产进行现场检查，这可能使检查成为整个工作中更大的部分。
下图以几个职业为例说明了这一点。对于软件开发人员，AI 加速了软件开发、测试、文档编写和数据处理的过程。但我们目前没有看到 AI 在协调系统安装或监督其他技术人员或工程师工作方面的有意义使用。对于教师，我们看到 AI 协助课程和活动规划，但不协助赞助课外俱乐部或维持课堂纪律。
从增长的角度来看，这些观察与 [Aghion, Jones, and Jones](<https://www.nber.org/papers/w23928>) 最近的一个观察很好地吻合：“增长可能不是受我们擅长什么的限制，而是受那些必不可少却又难以改进之事的限制。”
![](assets/estimating-productivity-gains/img_010.img)四个不同的职业以及显示出巨大潜在时间节省的“加速”任务，以及未出现在我们样本中的潜在“瓶颈”任务。例如，软件工程师在开发和调试软件方面看到巨大的估算时间节省，但在监督程序员方面则没有。每周时间比例由 Claude 估算（见前一节）。
## 局限
我们的方法存在几个我们认为值得就该主题进一步研究的局限：
  * **Claude 的预测并不完美，而且我们缺乏对 Claude 时间估算的现实世界验证**：AI 系统是不完美的预测器，无法看到用户结束与模型互动之后发生的活动。虽然我们预计这些估算会随着模型能力而改进，但使用模型估算引入了显著的噪声来源。虽然我们的估算表明模型在估算任务时间方面正在接近人类表现，而人类自身也远非完美，但我们缺乏现实世界数据来验证 Claude 提供的估算。
  * **任务分类体系局限**：真实工作比 O*NET 任务列表更复杂，我们为每个任务估算的时间分配只是近似值。工作的许多重要方面——隐性知识、人际关系、不确定性下的判断——不会出现在这些正式的任务描述中，而且任务_之间_的联系可能对生产力的影响与单独这些任务的时间节省一样大，甚至更大。虽然我们对单个任务显示了巨大的预计时间节省，但一项[最近的随机对照试验](<https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>)研究端到端软件功能时并未看到 AI 带来的时间节省。
  * **结构性假设**：在我们上面的计算中，我们比较了专业人士在没有 AI 的情况下完成给定任务所需的时间与有 AI 时所需的时间。但这可能_低估_生产力增益——因为雇佣员工和传达背景需要额外资源（这是我们没有计入的）——也可能高估，如果 AI 的工作质量比人类差的话。
  * **组织重构**：从历史上看，单个企业最大的生产力增益来自于[重组业务运营](<https://www.jstor.org/stable/2006600>)以采用新技术。我们的模型可以帮助预测这种重构的_效应_，但无法预测公司可能决定如何重构，或这个过程可能有多快。
  * **创新的作用**：技术创新是经济增长的[引擎](<https://www.jstor.org/stable/1926047>)。我们的模型没有捕捉 AI 系统如何加速甚至自动化科学过程，也没有捕捉这对生产力、增长和工作结构的影响。
  * **数据有限**：我们的数据集仅来自 [Claude.ai](<http://claude.ai/redirect/website.v1.885f58b9-7bdd-416a-89ac-4517a9d2f952>) 对话。这个样本不能代表 AI 用途的完整谱系，而且可能存在某种选择效应，即人们使用 Claude 的任务实例是他们认为 Claude 最有用的那些。此外，由于样本量有限，我们可能遗漏了一些不太常见的 AI 任务。
我们在这里开发的测量基础设施能够在大规模上持续追踪 AI 对节省时间的影响。随着模型的改进和更好的方法解决这些局限，我们可以重新估算这些节省的时间，并确定这些能力改进如何转化为更广泛的经济影响。我们期待在未来数月和数年中追踪这些变化。
## 结论
Claude 处理的任务复杂度差异巨大——从只需要几分钟的简单食品准备问题，到需要数小时的复杂法律和管理任务。但这些工作的总体效应是什么？
根据 Claude 对每个任务的时间估算（并假设未来 10 年普遍采用），我们发现使用_当前_模型意味着美国劳动生产率每年可能增长 1.8%——这是近期劳动生产率增长速度的两倍。基于当前的 AI 使用情况，这些增益将集中在技术、教育和专业服务领域，而零售、餐饮和运输行业的影响微乎其微。随着模型能力、产品和采用继续发展，我们将作为[经济指数](<https://www.anthropic.com/economic-index>)的一部分持续追踪这些变化。
这些生产力增益来自让现有任务更快完成。但从历史上看，变革性的生产力改进——无论是来自电气化、计算还是互联网——都不是来自加速旧任务，而是来自从根本上重组生产。在这样的未来中，AI 不仅使功能实现更快，公司还会重组会议和代码审查，以更快地验证和交付这些功能，无论是否使用 AI 或通过其他方式。
我们的框架可以用来帮助估算这种重构的效应，但无法预测会发生哪些变化，或变化有多快。未来工作的一个重要方向是理解这个问题——更好地理解企业何时以及如何围绕新兴的 AI 能力重组自己。答案将决定 AI 何时从提供显著但有限的生产力提升，跃升为代表那种历史上定义了技术革命的结构性转型。
### BibTeX
如果你想引用这篇文章，可以使用以下 BibTeX 键：
    
    @online{tamkinmccrory2025productivity,
    author = {Alex Tamkin and Peter McCrory},
    title = {Estimating AI productivity gains from Claude conversations},
    date = {2025-11-05},
    year = {2025},
    url = {https://www.anthropic.com/research/estimating-productivity-gains},
    }
## 附录
### 将 Claude 的估算与其他估算进行比较
![](assets/estimating-productivity-gains/img_011.img)AI 在未来 10 年期限内预计带来的年度劳动生产率增长提升。图转载自 Filippucci, Gal, and Schief, 2024。虚线为 1.8%，来自 Claude 的估算。
### 我们用于时间估算的提示词
**人类时间估算提示词**
    
    Human: Consider the following conversation:
    
    <conversation>
    {{TRANSCRIPT}}
    </conversation>
    
    Estimate how many hours a competent professional would need to complete the tasks done by the Assistant.
    Assume they have:
    - The necessary domain knowledge and skills
    - All relevant context and background information
    - Access to required tools and resources
    
    Before providing your final answer, use <thinking> tags to break down your reasoning process:
    <thinking>
    2-5 sentences of reasoning estimating how many hours would be needed to complete the tasks.
    </thinking>
    
    Provide your output in the following format:
    <answer>A number representing hours (can use decimals like 0.5 for shorter tasks)</answer>
    
    Assistant: <thinking>
**互动时间估算提示词**
    
    Human: Consider the following conversation:
    
    <conversation>
    {{TRANSCRIPT}}
    </conversation>
    
    Estimate how many minutes the user spent completing the tasks in the prompt with the model.
    Consider:
    - Number and complexity of human messages
    - Time reading Claude's responses
    - Time thinking and formulating questions
    - Time reviewing outputs and iterating
    - Realistic typing/reading speeds
    - Time implementing suggestions or running code outside of the converesation (only if directly relevant to the tasks)
    
    Before providing your final answer, use <thinking> tags to break down your reasoning process:
    <thinking>
    2-5 sentences of reasoning about how many minutes the user spent.
    </thinking>
    
    Provide your output in the following format:
    <answer>A number representing minutes</answer>
    
    Assistant: <thinking>
**软件开发时间估算提示词**
    
    Human: You are estimating software development tasks for open-source projects. Provide ONLY a number in hours (e.g., 0.3, 1.6, 15). Do not explain.
    Task: {task}
    Description: {description}:
    Estimate (hours):
    Assistant:
**任务时间估算提示词**
    
    You are estimating how much time workers in the occupation "{occupation_title}" spend on each of their job tasks.
    
    Below is the complete list of tasks for this occupation. For each task, estimate how many hours per week a typical worker spends on it.
    
    Important: Don't worry about making the hours sum to exactly 40 or any specific total - we'll normalize the results afterward. Just give your best estimate for each task independently based on what seems realistic.
    
    Tasks:
    {tasks}
    
    Return ONLY a JSON object mapping each task_id to your estimated hours per week, with no additional text, explanations, or commentary. Format:
    {{
      "task_id_1": hours,
      "task_id_2": hours,
      ...
    }}"""
#### 脚注
1. Claude 容易产生时间和成本两方面的离群估算；例如，它将某些编程任务归类为需要人类数年才能完成或价值数百万美元。虽然这是可能的，但为了产生更保守的估算，我们取每个任务中位数值的平均值，并按每个任务中的对话数量加权。
2. Hulten 定理指出，在没有扭曲的竞争均衡中，微观层面生产力增益对全要素生产率的贡献，在一阶近似上与生产要素的 Domar 权重成正比。一个要素的 Domar 权重是其总产出价值与 GDP 之比。在 Acemoglu (2024) 提出的基于任务的模型中，劳动密集型任务的 Domar 权重等于该任务在工资账单中的份额乘以劳动收入份额。关于 Hulten 定理的最新处理与推广，参见 Baqaee and Farhi (2019)。用公式表示，Hulten 定理指出 TFP 的对数变化等于微观生产率对数变化的 Domar 加权和。在我们的案例中，对数变化取为 ln(无 AI 完成时间) 减去 ln(有 AI 完成时间)。
3. TFP 的增长比劳动生产率的增长更根本。劳动生产率是每名工人的产出比率，即使在 TFP 不变的情况下，也可能因劳动以外其他生产要素的增加而提高。
4. [Acemoglu 2024](<https://www.nber.org/papers/w32487>) 计算出 AI 暴露行业的劳动份额为 0.57；鉴于两者非常接近，为简便起见，我们使用整个经济的份额 0.6。
5. 关于全要素生产率的历史数据，请参见旧金山联邦储备银行的估算：<https://www.frbsf.org/research-and-insights/data-and-indicators/total-factor-productivity-tfp/>。2015 年至 2024 年 TFP 的平均增长率为 0.7%。二十年前，1995 年至 2004 年的 TFP 平均增长率为 1.6%。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/estimating-productivity-gains>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/estimating-productivity-gains>)
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