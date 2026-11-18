---
title: Enabling independent research on how people use Claude
url: https://www.anthropic.com/research/enabling-independent-research
date: Aug 26, 2026
category: Societal Impacts
source: https://www.anthropic.com/research
---

# 支持对Claude使用方式的独立研究

- **日期：** 
- **类别：** 社会影响（Societal Impacts）
- **来源：** https://www.anthropic.com/research/enabling-independent-research

---

社会影响（Societal Impacts）
2026 年 8 月 26 日
![支持关于人们如何使用 Claude 的独立研究](assets/enabling-independent-research/img_000.svg)
_今年早些时候，我们开展了一项试点，让外部研究者访问关于 Claude 使用的聚合真实数据。三个研究组为我们的隐私保护分析工具 Anthropic Insights 各自设计了研究；我们代表他们运行了数据收集，而他们进行了独立的分析。在这篇文章中，我们分享这些研究的高层结果，以及我们在运行该试点中的收获。我们还提供了一个[意向表达表单](<https://docs.google.com/forms/d/e/1FAIpQLScujFA2mJXnLhrvE7wazD7drfHlfRmfnrjhMZRpeIFW_b6I7Q/viewform?usp=sharing&ouid=108982467493638405621>)，供未来可能希望与我们合作的研究者使用。_
确保向变革性 AI 的过渡顺利，需要理解其对人与社会的影响。目前，关于与 AI 真实世界交互的数据集中在少数几家实验室手中。我们认为，如果能向研究者、政策制定者和公众更广泛地开放更多数据，将是件好事。
实验室之外的研究者有两条路可走。他们可以借助实验室发布的分析，这些分析反映了真实使用情况，但往往回答的是实验室自己的问题，而非研究者自己的问题。或者他们可以使用公开数据集，可以随意研究，但这些数据集偏向更随意的使用，可能无法反映大多数人实际如何使用 AI。两者都不足以支撑关于 AI 实际如何被使用的独立研究。
今年春天，我们试点了一项计划，三家外部研究机构通过 [Anthropic Insights](<https://www.anthropic.com/research/clio>)（原名「Clio」）设计并运行了各自基于 Claude 使用数据的研究。Anthropic Insights 是我们自己的团队用来分析数百万条 Claude 对话使用模式的隐私保护工具。我们希望未来能扩大该计划的规模，因此还对所有共享给第三方研究者的数据进行了额外的隐私审计，以验证我们的隐私保护措施有效（见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/8a665c85eec3a63b4d86287b9255657016f50e29.pdf>)）。
我们相信，这是外部研究者首次基于 AI 公司自身的使用数据开展公开独立的研究。下文我们将讨论外部团队发现了什么、我们在运行试点中学到了什么，以及我们在决定如何更广泛地扩展该计划时正在权衡什么。我们还公开发布了[各项目的聚合数据](<https://huggingface.co/datasets/Anthropic/enabling-independent-research>)。
## 研究者学到了什么
我们与三个研究组合作：斯坦福大学的[社会与语言技术（SALT）实验室](<https://cs.stanford.edu/~diyiy/group.html>)、牛津大学的[人类信息处理实验室](<https://humaninformationprocessing.com/>)，以及 [METR](<https://metr.org/>)——一家评估前沿 AI 模型的非营利组织。每个小组都提出了自己的研究问题，并使用 Anthropic Insights 对 2026 年 4 月至 5 月约 25 万条 Claude.ai 或 Claude Code 对话进行了隐私保护分析。
我们希望外部合作者拥有尽可能大的独立性，因此我们的合同审查权仅限于用户隐私、可能帮助人们违反我们使用政策的信息、Anthropic 的机密信息以及研究的准确性。除此之外，Anthropic 对研究结论的内容没有发言权，研究者可以自由发布其结果，即便这些结果对 Anthropic 不利。以下是一些早期结果。我们对于这些方向感到兴奋，也对数据公开后其他人将发现什么感到兴奋。
**社会与语言技术实验室**研究了人类如何与 AI 协作。他们考察了人们将何种类型的工作交给 AI、人类在完成该工作时保留了哪些角色，以及人机协作在何处断裂。他们发现：
  * **人们交给 AI 的高风险工作比预期更多。** 先前的研究表明，人们大多把低责任任务委托给 AI，而把后果性任务（即影响他人或难以撤销的工作）留给自己。但 SALT 实验室发现，超过一半的 Claude 对话中，人们将后果性任务委托给了 AI。当人们寻求专业指导时——尤其是法律或财务问题——最有可能将后果性工作交给 Claude。
  * **人们在与 Claude 协作时通常负责指导和监督工作。** 在接近四分之三的对话中，人们设定方向，而 Claude 提供协助，并且人们通常会调整其输出，而非逐字照搬使用。但即便在就自己想要的输出指导 Claude 时，人们对 Claude 生成内容的了解和从中学习的程度也各不相同。
  * **人们在与 AI 协作时常会遇到摩擦。** 然而，这种摩擦往往是有成效的。人们投入时间和精力去观察 Claude 如何尝试任务、识别请求在何处不清晰或被误解，并对自己的方向进行迭代，从而带来更好的结果——它推动人们厘清意图、精炼输出或持续投入问题。

在此[阅读他们的完整报告](<https://www.alphaxiv.org/abs/2608.human-ai-collaboration-at-scalev1>)。
**人类信息处理实验室**正在研究人们使用 Claude 时的感受，以及这与 Claude 的行为有何关联。他们的早期结果表明：
  * **人们使用 AI 时的感受与 AI 的行为相关联。** 研究者发现，人类与 AI 的行为模式在对话中同时出现：Claude 表现出温暖时，人们也更积极；Claude 拒绝或不同意时，人们会反驳；Claude 表现得古怪时，人们更加投入思考；而 Claude 只是提供帮助时，人们似乎感到满意。
  * **人们使用 AI 的体验与在网络其他地方的体验非常相似。** 研究者发现，Claude 对话中专注、沮丧和愉悦等状态之间的模式，与一项关于日常互联网浏览的独立研究中的模式高度相似，表明人们参与 AI 活动与其他数字活动的方式存在相似性。

他们仍在完成报告。一旦公开，我们将在此添加链接。
**METR** 正在估算编程智能体带来的真实世界生产率提升，以及这些生产率提升如何随模型代际变化。他们对 Claude Code 对话的分析仍在进行中，但早期结果表明：
  * **能力更强的模型可能为用户节省更多时间。** METR 将 Claude 对「没有 AI 时任务需要多长时间」的猜测，与「使用不同 Claude 模型时实际花费的时间」进行了比较。他们的初步发现表明，较新的模型比较旧的模型带来了显著的加速。METR 计划随着分析的深入分享更多内容。
  * **AI 能较好地估计所花费的时间。** 由于该分析依赖 Claude 判断任务需要多长时间，METR 将这些判断与先前一项开发者研究中已知的完成时间进行了比较。Claude 的估计与开发者的实际耗时相关。
  * **下一步：衡量 AI 加速了研究多少。** METR 继续研究他们的研究如何能揭示 AI 在多大程度上加速了研究者的工作，随着 [AI 承担越来越多自身的开发工作](<https://www.anthropic.com/institute/recursive-self-improvement>)，这一点可能变得愈发重要。

他们仍在完成报告。一旦公开，我们将在此添加链接。
## 我们的团队学到了什么
在 AI 领域，共享使用数据基本前所未有，因此这个试点既是一项运行此类计划的实验，也是一种以隐私保护方式促成第三方研究的途径。保护用户隐私和研究者的独立性都至关重要，我们也做到了两者兼顾。Anthropic Insights 正是为此而设计——研究者从未访问原始对话，只看到经过与我们内部工作相同法律和隐私审查后的聚合输出。然而，所有这些都使试点比起 AI 实验室正常的研究速度更慢，且运行起来耗费资源。这两个因素都对有效扩展该计划构成了挑战。有关我们如何运行该试点的更多细节，请参阅[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/8a665c85eec3a63b4d86287b9255657016f50e29.pdf>)。下文我们将讨论所学到的以及我们如何应对出现的挑战。
**从不同视角研究同一问题很有价值。** 我们部分合作伙伴的研究问题与内部正在推进的工作有所重叠。例如，METR 的提案与我们关于「[智能体式编程与专业知识的持续回报](<https://www.anthropic.com/research/claude-code-expertise>)」的经济学研究相似。我们发现这种重叠很有价值：它让外部研究者有机会考察相似的数据并得出自己的结论。他们的研究是否与我们的结论一致，我们将随着其研究的持续予以关注。我们还把 METR 与我们的经济团队联系起来，发现这种联系改善了两个研究团队的工作。
**内部有效的方法需要针对外部合作伙伴进行调整。** 使用 Anthropic Insights 时，研究者会写出一个类似「此人在寻求何种类型的指导？」的问题，Claude 会为研究中的每一条对话回答该问题。答案随后被聚合成若干类别；研究者只能看到最终的类别以及落在每个类别下的对话百分比。由于我们依赖 Claude 的判断，该工具对问题的措辞很敏感；措辞不当可能将对话归入错误描述它们的类别。由于没有人能阅读底层对话，这些错误很难被发现。
在内部，我们通过数周内对问题多次迭代来管理这一点。外部合作伙伴无法这样做，因为在共享每个数据集前进行反复隐私审查会使研究难以为继。相反，我们让他们在 WildChat 上测试问题——WildChat 是一个人类与 AI 对话的公开数据集，他们可以在其中将答案与底层对话本身进行核对。但 WildChat 偏向随意和创造性使用，与 Claude 流量不同，因此一些在 WildChat 上表现良好的问题，一旦应用于实际的 Claude 对话，就会产生误导性的类别。我们通过提供关于如何解读 Anthropic Insights 输出的指导来解决这一问题（见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/8a665c85eec3a63b4d86287b9255657016f50e29.pdf>)）。展望未来，我们正在探索外部研究者如何能提前更有效地制定他们的问题和类别。
**在保持对滥用行为的透明度同时不助长滥用。** 合作伙伴在 Anthropic Insights 输出中的某些类别暴露了违反我们可接受使用政策或服务条款的行为——例如有一类人寻求关于被禁止活动的指导。我们认为公众应当了解我们平台被滥用的情况，因此我们分享了其中大部分违规情况。例外情况是那些描述用户_如何_绕过我们防护措施的类别，而非_什么_他们试图做的类别。在每项研究中，受影响的类别和对话都不到 5%，并且在每种情况下，我们都告诉研究者我们更改或删除了哪些聚类以及原因。作为一项标准做法，当 Anthropic Insights 暴露此类违规时，我们会将聚合数据共享给我们的防护团队审查。这也是我们未来与外部研究者合作的一项重要流程。
## 展望未来
理解 AI 对社会的影响，单靠 AI 公司无法完成，任务过于庞大。真正的监督需要外部研究者就真实世界的使用数据提出自己的问题，并独立发布他们的发现。
这个试点是一项实验：外部研究者能否在不损害用户隐私的前提下，在我们的平台上开展独立研究？这项工作比我们预期的更具挑战性，我们也吸取了许多教训，但迄今为止答案似乎是肯定的。我们的合作伙伴开展了我们自己不会想到去设计的研究，而且每一项都告诉我们关于 AI 真实世界影响的新东西。这是一个有希望的第一步，但还有更多工作要做。
下一步，我们要确定能否扩展该计划——既包括在上述约束下我们能支持何种类型的研究，也包括我们一次能运行多少项研究。我们从缓起步，以确保隐私、安全和研究质量。我们想评估兴趣，并了解研究者希望研究什么。如果你是一名研究者，且对 Anthropic Insights 的访问能让你开展今天无法开展的工作，请填写[此表单](<https://docs.google.com/forms/d/1PyyC-GU4Jra2WoXWcJjuFXZhM-lRxeBNnlh1tJv_2Jg/edit>)。
## 附录
完整附录可[在此获取](<https://www-cdn.anthropic.com/files/4zrzovbb/website/8a665c85eec3a63b4d86287b9255657016f50e29.pdf>)。它描述了我们如何运行该计划，包括我们如何选择三个合作伙伴、我们撰写的研究入门材料（用于解释该计划的目标以及 Anthropic Insights 能做什么），以及每个项目如何从提案走向研究设计再到分析。它还包括我们合作协议书的细节，其中明确说明我们的合作伙伴可以自由发布发现，即便这些发现对 Anthropic 不利。此外，我们涵盖了由伦敦帝国理工学院进行的第三方隐私审计，以及我们对所有发布数据所持有的隐私威胁模型。我们还包括了关于解读我们从合作伙伴的 Anthropic Insights 研究发布的数据的指导。
## 贡献与致谢
Kunal Handa 领导了该项目，与合作伙伴协作制定研究提案，起草研究指导和合同，运行合作伙伴的 Anthropic Insights 研究，帮助构建支持合作伙伴研究的技术基础设施，参与 Anthropic Insights 输出的内部审查，并撰写了博客文章。Miranda Zhang 协调了合作与沟通，并参与了工作的各个方面。Gabriel Nicholas 协调了第三方隐私审计、Anthropic Insights 输出的内部审查，并参与了工作的各个方面。Miles McCain 撰写了关于解读 Anthropic Insights 输出的指导，开发了支持合作伙伴研究的技术基础设施，参与了 Anthropic Insights 输出的内部审查，并对博客文章和隐私威胁模型提供了反馈。Ryan Heller 为支持合作伙伴研究的技术基础设施做出了贡献。Saffron Huang 参与了 Anthropic Insights 输出的内部审查，并提供了关键反馈与讨论。Thomas Millar 和 Suzanne Wang 为支持合作伙伴研究的技术基础设施以及 Anthropic Insights 输出的内部审查做出了贡献。Shan Carter、Mo Julapalli、Matt Kearney、Sarah Pollack 和 Judy Shen 参与了 Anthropic Insights 输出的内部审查。Matthew Jagielski 为隐私威胁模型做出了贡献。Shaoyi Zhang 为支持合作伙伴研究的技术基础设施做出了贡献。Heather Whitney、Ankur Rathi、Aisling Keenan 和 David Saunders 在整个项目中提供了法律与隐私指导。Jake Eaton 和 Sylvie Carr 对博客文章的框架构建与撰写做出了贡献。Jack Clark 和 Michael Stern 在整个过程中提供了宝贵的指导、支持与讨论。Deep Ganguli 在项目各阶段提供了详细指导、组织支持与反馈。
此外，我们感谢 Miriam Chaum、Ishita Dasgupta、Esin Durmus、Adam Farina、Zoe Hitzig、Jerry Hong、Devin Kuokka、Hendson Lin、Maxim Massenkoff、Peter McCrory、Maryam Quasto、Nitarshan Rajkumar、Amie Rotherham、Divya Siddarth、Taylor Sorensen、Jerome Swannack、Alex Tamkin、Molly Villagra、Scott White 和 Charles Yang 提出的有益想法、讨论、反馈与支持。
对于他们在本计划中的合作，我们感谢斯坦福社会与语言技术实验室的 Vishakh Padmakumar、Yijia Shao、Jennifer Wang、Diyi Yang 和 Dora Zhao，牛津人类信息处理实验室的 Tsvetomira Dumbalska、Hannah Rose Kirk 和 Christopher Summerfield，以及 METR 的 Joel Becker（现任职于 Anthropic）、Daniel Paleka 和 Parker Whitfill。
对于进行第三方隐私审计，我们感谢 Zexi Yao、Bozhidar Stevanoski、Peter Romov、Euodia Dodd、Xiaoxue Yang 和 Nataša Krčo。
## 引用

    @online{handa2026enablingindependentresearch,
    author = {Kunal Handa and Miranda Zhang and Gabriel Nicholas and Miles McCain and Ryan Heller and Saffron Huang and Thomas Millar and Suzanne Wang and Shan Carter and Mo Julapalli and Matt Kearney and Sarah Pollack and Judy Shen and Matthew Jagielski and Shaoyi Zhang and Heather Whitney and Ankur Rathi and Aisling Keenan and David Saunders and Jake Eaton and Sylvie Carr and Jack Clark and Michael Stern and Deep Ganguli},
    title = {Enabling independent research on how people use Claude},
    date = {2026-08-26},
    year = {2026},
    url = {www.anthropic.com/research/enabling-independent-research},
    }

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/enabling-independent-research>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/enabling-independent-research>)
## 相关内容
### Claude 如何提升生物分子建模
Claude 让科学家用于预测和设计生物分子的开源模型变得更快、更省内存。Claude 在不到四周内优化了 30 多个此类模型，平均提速约 4 倍。它还创建了一种低内存模式，可在单个 NVIDIA GPU 节点上准确预测大于 10,000 个 token（氨基酸、核苷酸以及来自小分子和离子的原子）的生物分子系统。
[阅读更多](</research/claude-uplifts-biomolecular-modeling>)
### 衡量 AI 模型在战术情报瞄准与常规武器能力方面的表现
Anthropic 的前沿红队开发了新评估，用以衡量 AI 在战术情报瞄准和常规武器开发方面的能力。
[阅读更多](</research/intelligence-targeting-conventional-weapons-capabilities>)
### 近期网络安全事件的对齐评估
我们呈现了对四起事件的对齐评估，在这些事件中 Claude 模型未经授权访问了真实的第三方系统。
[阅读更多](</research/alignment-assessment-cybersecurity-incidents>)
