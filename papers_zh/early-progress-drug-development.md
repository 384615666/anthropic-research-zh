---
title: Early progress on accelerating drug development with Claude
url: https://www.anthropic.com/research/early-progress-drug-development
date: Oct 27, 2026
category: Science
source: https://www.anthropic.com/research
---

# 利用Claude加速药物研发的早期进展

- **日期：** 
- **类别：** 科学（Science）
- **来源：** https://www.anthropic.com/research/early-progress-drug-development

---

科学（Science）
2026 年 10 月 27 日
![利用Claude加速药物研发的早期进展](assets/early-progress-drug-development/img_000.webp)
已发布
    2026 年 10 月 27 日
团队
    [科学](</science>)
主题
    
  * [生命科学](</search?topic=life-sciences>)
  * [合作伙伴](</search?topic=partnerships>)
  * [医疗健康](</search?topic=healthcare>)
  * [发现](</search?topic=discovery>)
  * [有益部署](</search?topic=beneficial-deployments>)

[](</news/rare-disease-research-grants>)[](</research/introducing-anthropic-science>)[](</news/anthropic-partners-with-allen-institute-and-howard-hughes-medical-institute>)[](</features/claude-on-mars>)
相关文章
  * 公告
2026 年 7 月 20 日
[申请Anthropic的AI for Science罕见病研究资助](</news/rare-disease-research-grants>)

[查看更多](</search?topic=life-sciences>)
 _Anthropic的[生命科学团队](<https://www.anthropic.com/science>)正致力于加速攻克疾病。过去几个月里，我们的科学家与六家研发新药的组织开展了深度研究合作：[BigHat Biosciences](<https://www.bighatbio.com/>)、[Bristol Myers Squibb](<https://www.bms.com/>)、[Divergence Labs](<https://divergencelabs.com/>)、[Enveda](<https://enveda.com/>)、[Generate Biomedicines](<https://generatebiomedicines.com/>)以及[The Column Group](<https://www.thecolumngroup.com/>)。我们也已启动自己的药物发现工作。在此过程中，我们对Claude如何支持药物研发、以及还需如何进一步改进Claude才能实现AI在医学中的潜力，有了大量认识。我们计划从这里开始大幅扩展这项工作_。
加速药物研发的机会很多，甚至超出了人们最常讨论的AI应用，例如为新分子[提出初始设计](<https://www.anthropic.com/research/Claude-accelerates-protein-design>)。开发一款药物涉及多种多样的任务：开展早期研究以确定药物靶点及与之结合的正确药物类型，设计具备合适性质的分子，优化分子使其能够可靠地大规模生产，起草开展临床试验所需的监管申报文件，设计并实施这些试验，以及诸多其他工作。
我们实现AI医疗效益的战略，是让AI越来越多地参与到所有这些任务中。并不存在单一待解决的问题；瓶颈分布在药物研发流程的各个环节。识别并突破这些瓶颈的最佳方式，是深入参与真实的药物项目，覆盖众多不同的疾病领域和研发阶段。
因此，过去几个月里，我们与六家组织合作开展了这项工作。我们也启动了自己的药物发现工作，包括针对罕见儿童型肌营养不良症的项目，其中Claude承担了大部分科学与运营工作。
这项工作从三个方面服务于我们的目标。首先，它让我们能更好地理解模型在更广泛药物研发任务中的优势与局限（基于迄今所学，我们已为模型确定了若干具体改进的优先次序）。其次，这些项目可以作为更广泛生命科学界的案例研究。若要让Claude显著提高新疗法的产出速度，我们需要与更多生物技术公司合作，并把Claude更深入地融入他们的研发流程。第三，如果这些项目继续保持良好势头，它们本身也应产生直接影响。我们乐观地认为，其中一些可能为其所针对的疾病带来有效的新药，包括食物过敏、罕见儿童疾病以及若干种癌症。 
在这篇文章中，我们介绍与合作伙伴取得的进展，并附上更详细描述我们思路、方法与早期成果的技术报告。随后，我们简要概述下一步的工作方向。 
## 案例研究
**Generate Biomedicines：治疗模式工程。**Generate Biomedicines一直致力于提升一种名为CAR T细胞疗法的癌症治疗手段的实用性。该疗法历来用于治疗血细胞癌症；Generate希望对其进行重新设计，使其也能治疗实体瘤癌症。为此，他们计划缩短该疗法遗传指令中的一部分，从而为适用于其他癌症类型的额外指令腾出空间。六名Generate科学家使用Claude Code为这一部分提出新设计。其中一项设计比标准版本短约70%，在实验室测试中效果更佳：它使免疫细胞产生的受体（免疫细胞用来识别癌细胞的蛋白质）数量约为原来的10倍，更高效地杀死肿瘤细胞，且免疫细胞保持活性的时间更长。阅读更多，并参见[Generate的技术报告](<https://generatebiomedicines.com/publications/refactored-intracellular-domains-enhance-car-expression-and-function/>)。
**Divergence Labs：苗头化合物生成。**Divergence Labs正在研究一种治疗食物过敏的新方法。食物过敏由一种名为IgE的分子引发的反应触发，其中一部分IgE附着在我们的免疫细胞上，另一部分则游离在血液中。Divergence Labs正在开发的药物会把IgE从免疫细胞上完全剥离，而不像标准药物那样仅中和血液中循环的IgE。这有望提供有效得多的疗法，但需要精确的设计，具备两条"臂"：一条紧密结合IgE，另一条帮助把IgE从免疫细胞上撬开。Claude把Divergence Labs的目标转化为详细的设计方案，随后基本自主地在一个月左右生成了约35,000个抗体设计，供筛选和测试。在这些早期测试中，Divergence为两条"臂"都找到了"苗头"：三个能结合IgE的设计，以及20个能使其脱落的设计。这20个中有三个使IgE脱落的效果似乎超过标准药物。其下一步是构建一种把两条"臂"结合起来的药物。阅读更多，并参见[Divergence的技术报告](<https://divergencelabs.com/publications/ige-preprint.pdf>)。
**BigHat Biosciences：先导化合物优化。**BigHat Biosciences把AI与自动化实验室结合起来改进潜在药物（即"先导化合物"），这些药物必须紧密绑定靶标、在生产和储存过程中保持稳定，并避免聚集结块（以及其他标准）。BigHat的科学家与一名Anthropic研究员借助Claude改进两个先导化合物的这三项性质，二者都是可能成为未来药物组成部分的抗体片段：一个设计用于靶向癌细胞，另一个设计用于延长药物在体内的留存时间。Claude接入BigHat的实验室数据系统Reccy后，为每个分子提出改动建议，BigHat的实验室在约10周内制备并测试了约1,010个变体。中途，团队怀疑标准的热稳定性和聚集指标具有误导性。Claude与研究员重新分析了原始数据，随后提出不同的指标以及验证它们的实验方案调整。BigHat的科学家完善并实施了该方案，主要预测得到验证。与原始版本相比，最优版本结合紧密程度提高10倍以上，靶向癌细胞的先导化合物保持溶解的温度提高了18°C，而用于长效药物的先导化合物聚集速度慢了100倍以上。阅读更多，并参见[BigHat的技术报告](<https://www.bighatbio.com/bighat-anthropic-collaboration-report-10-27-2026>)。
**Enveda：生产与申报。**要开展临床试验，公司需要留存记录以证明新药的每一批次都按严格质量标准生产，并向监管机构提交申请，此外还有其他要求。在Enveda，生产化学师最多把75%的时间花在文书工作上。为减轻负担，Enveda搭建了一套系统，把其全部生产文档接入Claude，再让Claude标出任何可能的问题。在对1,061页文档的测试中，Claude找出了人工审核者发现的全部11个问题——还标出了他们遗漏的7个。在此过程中，该方法把人工审核时间减少了89%，从超过25小时降至不足3小时。另外，Claude起草了两份重要监管文件的初稿。其中一份耗时四小时，而人工撰写约需三个月。对另一份，Enveda的标准人工审核流程只发现一处小错误。阅读更多，并参见[Enveda的技术报告](<https://enveda.com/CMC-Document-Processor/>)。
**The Column Group（TCG）：公司创建。**由于药物发现可能缓慢、昂贵且容易失败，生物技术公司的投资者往往偏爱更安全、此前已验证的思路，而非风险更高的新思路，即便后者能帮助更多患者。我们一直与TCG合作，看Claude能否通过缩短药物发现的时间与成本来改变这一局面，使投资者有信心支持更有雄心的想法。具体而言，TCG正在创办一家新公司Pleiades，它将用Claude运行比小团队通常所能承担的更多、也更复杂的药物项目。这可能成为一种范例，展示Claude如何降低运营一家生物技术公司所需的科学以及运营与行政开销。如果奏效，这一模式可在全行业复制，把投资引向医学中更棘手的问题。Pleiades目前正在为Claude开发新的工具与工作流；其首个Claude技能帮助Claude评估药物靶点是否值得跟进，已在45个靶点—疾病配对上完成评估。阅读更多。
更近期，我们还开始与[Bristol Myers Squibb](<https://www.bms.com/>)（BMS）合作，寻找并解决临床试验规划中的瓶颈。BMS正用Claude评估一款处于临床试验早期阶段药物的方案，并估计这些试验成功的可能性。我们计划共同在2027年扩展这项工作，以了解其在提高早期研发成功率方面的潜力。
> _"我们在临床试验阶段使用Claude分析专有数据、制定临床研究方案，并权衡研究成功的几率。仅凭一条提示，Claude就生成了扎实初步分析，为我们评估不同开发方案提供了依据，而这项工作原本需要数天才能完成。所有这一切都是在确保高度敏感数据安全的前提下完成的。我们期待把这项工作扩展到整个研发管线，以支持组合层面的决策。"_
 _**Michael Pourdehnad, MD**，早期临床开发、血液学、肿瘤学与细胞治疗高级副总裁兼负责人。_
除与这些合作伙伴的工作外，我们已开始自行开展一些研究项目。我们收购了Mithril Medicine，这是一家由一人运营、一直在为两种罕见型肌营养不良症开发疗法的公司。其创始人Cody Tranbarger用Claude统筹与11家外部实验室的合同、物流和实验，并把Mithril运营的许多其他事务交给Claude处理。结果，Mithril在不到18个月里，把一种肌营养不良症的可能疗法从构想推进到在小鼠中取得可喜结果。如今Cody在Anthropic继续这项研究，并计划启动若干新项目。如果他的候选药物持续表现良好，我们预计最早在2028年底就有一款药物可准备启动人体临床试验。阅读更多，并参见[我们的技术报告](<https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf>)。
## 拓展我们在生命科学领域的工作
所有这些研究仍处于早期阶段。尤其是，迄今大多属于_临床前—_也就是说，大体上尚未进入药物在人体中测试的阶段。随着这些药物项目推进，以及我们与更多药物研发项目已进入临床阶段的组织合作，我们计划继续把Claude的作用扩展到临床试验中。
这项研究只是我们加速药物发现努力的一部分。最终，我们希望把模型分享给尽可能多的药物研发研究者。为此，我们推出了面向研究者的AI工作台[Claude Science](<https://www.anthropic.com/news/claude-science-ai-workbench>)，并提供[面向生命科学家的Claude额度](<https://www.anthropic.com/news/ai-for-science-program>)。我们还设立了[生命科学验证计划](<https://www.anthropic.com/news/life-sciences-verification-program>)，让可信组织能在更宽松的安全防护版本下使用我们最强大的模型——这些防护对防止滥用必不可少，却也可能妨碍合法的生物学研究。我们近期还在生命科学领域发起了[客座研究员公开征集](<https://www.anthropic.com/news/open-call-guest-investigators-life-sciences>)；我们正寻求那些希望用Claude探究药物发现及其他领域关键问题的研究团队提交方案。
随着生命科学研究的扩展，我们期待与更多组织合作。如果您所在机构专注药物发现并有意与我们合作，可通过下方与我们联系。
### 与我们联系
如果您所在机构专注药物研发并希望取得联系，请填写以下表单。
