---
title: Claude’s values across models and languages
url: https://www.anthropic.com/research/claude-values-models-languages
date: Jul 13, 2026
category: Societal Impacts
source: https://www.anthropic.com/research
---

# Claude 在不同模型和语言中的价值观

- **日期：** 
- **分类：** 社会影响（Societal Impacts）
- **来源：** https://www.anthropic.com/research/claude-values-models-languages

---

社会影响
2026年7月13日
![Claude’s values across models and languages](assets/claude-values-models-languages/img_000.svg)
当有人向 Claude 提出一个没有普遍正确答案的问题——比如是否接受一份新工作，或如何处理与朋友的冲突——Claude 的回答方式不可避免地会反映某些价值观。1 我们希望 Claude 体现的价值观在 [Claude 的宪法](<https://www.anthropic.com/constitution>) 中得到了高层级的概述，但没有一份文件能够预见每天在 [Claude.ai](<http://claude.ai/redirect/website.v1.c4912eba-b7dd-40b1-a1ef-1a55aaf58274>) 上发生的数百万次对话中可能浮现的每一种价值观。相反，我们力求在 Claude 的回答中培养 ["良好的判断力和健全的价值观，并能因地制宜地加以运用。"](<https://www.anthropic.com/constitution>)
那么，我们究竟如何研究 Claude 所表达的价值观，以及它们在不同情境下如何变化？在 [之前的工作](<https://www.anthropic.com/research/values-wild>) 中，我们分析了 70 万段匿名的 Claude.ai 对话，在 Claude 的回答中识别出 3000 多种不同的价值观，以及 Claude 表达它们的频率。但如此庞大的价值观列表很难进行推理。在这项工作中，我们把这些成千上万种价值观压缩到少数几个轴（axis）上，使其变得易于研究，这些轴捕捉了 Claude 回答中的关键模式。每个轴都是两组价值观之间的数轴——例如，一端是与情感温暖（emotional warmth）相关的价值观，另一端是与严谨（rigor）相关的价值观——而 Claude 在这条线上所处的位置告诉我们它倾向于哪些价值观。
我们应用这种方法来衡量 Claude 所表达的价值观在两个方面如何变化。首先，我们比较了 Claude 所表达的价值观在不同模型之间的差异。每个 Claude 模型都体现了略有不同的性格训练方法，以及许多其他的微调决策。由于我们的价值观轴方法量化了模型之间的关键差异，它最终可能让我们把 Claude 所表达价值观的差异与不同的训练决策联系起来。
其次，我们想了解用户在使用各种语言与 Claude 交谈时的体验差异。我们 [之前的研究](<https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf>) 表明，Claude 在不同语言中的行为略有不同。2 我们应用价值观轴方法来理解 Claude 所表达的价值观在 [Claude.ai](<http://claude.ai/redirect/website.v1.c4912eba-b7dd-40b1-a1ef-1a55aaf58274>) 上最常用的 20 种语言之间如何变化。
  

![Four value profile cards in two pairs, one comparing the values expressed by Opus 4.6 and Opus 4.7 and the other comparing the values expressed by Claude in English and by Claude in Arabic. Each card has four arrows depicting the magnitude and direction of Claude's lean on each of the four axes \(Deference vs. Caution, Warmth vs. Rigor, Depth vs. Brevity, Candor vs. Execution\). Opus 4.7 leans most strongly toward Caution and Depth, and also toward Rigor and Candor. Opus 4.6 leans toward Deference, Rigor, Brevity, and Execution. Claude in English leans toward Caution, Rigor, Depth, and Candor. Claude in Arabic leans most strongly toward Warmth, and also toward Deference,  Brevity, and Execution.](assets/claude-values-models-languages/img_001.img)图 1：Claude 所表达的价值观在 Opus 4.6 与 Opus 4.7 之间、以及英语与阿拉伯语之间存在差异。Opus 4.6 倾向于表达与顺从、严谨、简洁和执行相关的价值观，而 Opus 4.7 倾向于表达与谨慎、严谨、深度和坦诚相关的价值观。在英语中，Claude 倾向于表达与谨慎、严谨、深度和坦诚相关的价值观，而在阿拉伯语中，它倾向于表达顺从、温暖、简洁和执行。
我们发现：
**四个关键轴捕捉了 Claude 价值观中 15% 的变异：3**
  * 顺从 vs. 谨慎（Deference vs. Caution）：Claude 是倾向于迎合他人的愿望，还是防范可能的风险和伤害。
  * 温暖 vs. 严谨（Warmth vs. Rigor）：Claude 是倾向于表达积极态度和对人的关怀，还是强调准确性和精确性。
  * 深度 vs. 简洁（Depth vs. Brevity）：Claude 是倾向于深入解释，还是只做被要求的事情。
  * 坦诚 vs. 执行（Candor vs. Execution）：Claude 是倾向于突出自身的不确定性，还是给出更圆润、更自信的回答。

**这些轴上的价值观画像与人们对模型性格的认知相符。** Sonnet 4.6 被认为是特别 [温暖](<https://www.anthropic.com/news/claude-sonnet-4-6>) 的，而 Opus 4.7 以 [严谨](<https://www.anthropic.com/news/claude-opus-4-7>) 著称。我们发现每个模型的价值观画像都映照了这些主观评价：Sonnet 4.6 倾向于对用户表达更多的顺从和情感温暖，而 Opus 4.7 倾向于表达对准确性和精确性的关注以及防范滥用。
**Claude 所表达的价值观在不同语言之间存在差异。** 当 Claude 用英语说话时，它强调的价值观不同于用葡萄牙语、印度尼西亚语或中文时。4 最大的变异出现在"温暖 vs. 严谨"轴上，Claude 在阿拉伯语和印地语中最倾向于表达与温暖相关的价值观，在英语和俄语中最倾向于表达与严谨相关的价值观。
借助这种方法，我们可以开始追问价值观为何会随模型和语言而改变，并更好地检验行为训练或文化背景等因素如何影响 Claude 所表达的价值观。
## **如何解读巨大的价值观空间？**
归根结底，我们的目标是有一种方法能够实证地理解 Claude 所表达的价值观，以及它们如何随情境变化。在这项工作中，我们特别关注价值观如何在模型和语言之间变化。但我们之前的工作 [《野外的价值观》（Values in the Wild）](<https://www.anthropic.com/research/values-wild>) 识别出 Claude 表达的 3000 多种价值观。逐一比较这数千种价值观既笨拙，又会掩盖更广泛的趋势。
为了让价值观比较更容易，我们构建了 _价值观轴_，根据哪些价值观往往在真实对话中同时出现，把数千种价值观缩减为少数几个底层维度。例如，被描述为"温暖"的 Claude 回答往往也被描述为"鼓励"和"积极"。同样的"温暖"回答较少被描述为"严谨"和"准确"。构建一个从温暖到严谨的轴让我们能够组织这些相关的价值观组——温暖相关价值观在一端，严谨相关价值观在另一端——并捕捉 Claude 在对话中与人互动的一个重要方面。如果 Claude 在一次对话中表达的温暖相关价值观多于严谨相关价值观，那么这次对话就落在这条轴的温暖一侧，反之亦然。这并不意味着两端的价值观组是互斥的——Claude 可以在同一次对话中既表达温暖又表达严谨。但在实践中，Claude 在轴的一侧表达的价值观越多，它在另一侧表达的价值观往往就越少。这些轴让我们能够比较 Claude 所表达的最显著的价值观组，而不必跟踪数千种个别价值观的变化。
为了构建价值观轴，我们从《野外的价值观》中识别出的 3,307 种价值观出发，手工聚类了含义相似的条目，得到一份包含 339 种高层价值观的更短列表。接下来，借助我们的 [隐私保护分析工具](<https://www.anthropic.com/research/clio>)，我们抽样了 309,815 段用户交给 Claude 主观任务的 [Claude.ai](<http://claude.ai/redirect/website.v1.c4912eba-b7dd-40b1-a1ef-1a55aaf58274>) 对话。5 我们的样本平均来自三个模型（Sonnet 4.6、Opus 4.6、Opus 4.7）和 Claude.ai 上最常用的 20 种语言，每个模型-语言组合约有 5,000 段对话。对每段对话，该工具使用 Claude 把 339 种高层价值观逐一标注为"存在"或"不存在"。6 我们以同样的过程识别用户表达的价值观，以及对话的任务和主题。然后我们应用降维（dimensionality reduction）——一种根据 Claude 倾向于一起表达的价值观，把标注的价值观压缩为轴的技术。方法细节、提示词、额外分析和局限性请参见 [附录](<https://cdn.sanity.io/files/4zrzovbb/website/02da7f28f74daa1be526d3ded451a4efc86bccdc.pdf>)。
这给我们留下了四个轴，它们捕捉了 Claude 所表达的价值观从一段对话到另一段对话变化的主要方式：
  * **顺从 vs. 谨慎**轴将 _迁就_ 和 _尊重偏好_ 等价值观与 _负责任的引导_ 和 _减少伤害_ 等价值观相对照。
  * **温暖 vs. 严谨**轴将 _积极框架和鼓励_ 等价值观与 _准确性_ 和 _透明_ 等价值观相对照。
  * **深度 vs. 简洁**轴将 _细致入微_ 和 _批判性思维_ 等价值观与 _简洁_ 和 _服从_ 等价值观相对照。
  * **坦诚 vs. 执行**轴将 _诚实_ 和 _透明_ 等价值观与 _结果导向_ 和 _优化_ 等价值观相对照。

为了确保我们测量的是 Claude 所表达的价值观——而不是用户询问内容的差异或询问方式的差异——我们控制了每段对话的任务、主题和用户表达的价值观。
  

![ Four dot plots, one per value axis. Each axis is a number line between two contrasting value groups, and every one of the values is positioned on the axis by how many times more it contributes to that axis than the average value contribution. Most values \(roughly 250 to 280 per axis\) contribute less than the average and sit in the center, while the strongest contributors are labeled at the ends. The axes and their labeled top values can be summarized as: Deference \(accommodation, adaptability, respect for preferences, engagement\) vs. Caution \(responsible communication, responsibility, responsible guidance, harm reduction\); Warmth \(positive framing, warmth, positivity, encouragement\) vs. Rigor \(rigor, accuracy, transparency, efficiency\); Depth \(nuance, depth and substance, user empowerment, critical thinking\) vs. Brevity \(brevity, respect for preferences, compliance, accommodation\); Candor \(intellectual honesty, honesty, intellectual humility, transparency\) vs. Execution \(results orientation, optimization, action orientation, order\). ](assets/claude-values-models-languages/img_002.img)图 2：代表 Claude 所表达价值观中最多变异的四个价值观轴。每个轴都是两组价值观之间的数轴。每种价值观在轴上的位置取决于它对轴的贡献是平均价值观贡献的多少倍，最强的贡献者被标注出来。大多数价值观的贡献低于平均水平，这意味着每个轴由一小撮关键价值观（图中标注）驱动。
## **不同的 Claude 模型会表达不同的价值观画像吗？**
在本节中，我们比较不同模型所表达的价值观。对每个模型，我们平均其所有对话在四个轴中每个轴上的位置，得到每个轴上的一个总体位置。结果是一幅高层图景，展示每个模型倾向于比其他人更多地表达哪些价值观组。相对于对话之间的变异，这些差异很小，但是有结构且可检测的。
  

![Three value profile cards comparing Sonnet 4.6, Opus 4.6, and Opus 4.7 across the four value axes \(Deference vs. Caution, Warmth vs. Rigor, Depth vs. Brevity, Candor vs. Execution\). Each card shows the model's average position in standard deviations from the mean across all conversations, and its distinctive behaviors. Sonnet 4.6 leans toward deference \(0.14σ\), warmth \(0.17σ\), and brevity \(0.14σ\), and its distinctive behaviors include affirming the user's ideas and work, mirroring the user's tone and formality, using humor and playfulness, offering comfort without judgment, and adding creative elements to what it produces. Opus 4.6 leans toward rigor \(0.10σ\), deference \(0.09σ\), and brevity \(0.08σ\), and its distinctive behaviors include getting straight to the point and staying within the scope of the user's request. Opus 4.7 leans toward caution \(0.24σ\), and depth \(0.23σ\), and its distinctive behaviors include pushing back on false assumptions, flagging risks unprompted, giving candid critiques of the user's work, explaining its reasoning, acknowledging its errors and limitations, and suggesting next steps for the user.](assets/claude-values-models-languages/img_003.img)图 3：每个模型在四个价值观轴上的平均位置（以与所有对话均值的标准差表示）及其独特行为。Sonnet 4.6 偏向温暖、顺从和简洁，而 Opus 4.7 更可能表达严谨、谨慎和深度。Opus 4.6 偏向严谨、顺从和简洁。
  

为了看看这些差异在实践中是什么样子，我们放大模型分歧最大的具体价值观。每次我们基于 Claude 的隐私保护工具在对话中标注一个价值观时，它还会写一段简短的描述，说明 Claude 如何表达该价值观。我们把反映相似行为的描述归组到价值观组内，并在图 3 中加以总结，从而更具体地展示模型之间的差异。
  * **顺从 vs. 谨慎。** Sonnet 4.6 相对于谨慎最倾向于表达顺从，常常肯定用户的想法和他们的工作。Opus 4.7 最倾向于表达谨慎，常常主动提醒用户风险。
  * **温暖 vs. 严谨。** Sonnet 4.6 最倾向于表达温暖，经常通过幽默、俏皮和不加评判地安慰用户。Opus 4.7 相对于温暖最倾向于表达严谨，更可能挑战用户的假设并坦诚地批评他们的工作。
  * **深度 vs. 简洁。** Opus 4.7 通过展示其结论背后的推理来偏向深度，而 Opus 4.6 和 Sonnet 4.6 偏向简洁。特别是 Opus 4.6 往往开门见山。
  * **坦诚 vs. 执行。** Opus 4.7 通过坦率说明自身局限性来偏向坦诚，而 Opus 4.6 偏向执行，更可能保持在用户请求的范围内。

这些发现与人们在 Anthropic 内部和网上的感知一致。[Claude.ai](<http://claude.ai/redirect/website.v1.c4912eba-b7dd-40b1-a1ef-1a55aaf58274>) 用户评论说，Opus 4.7 比其他模型更常对自己的回答留有余地。Anthropic 员工将 Opus 4.7 描述为表达相对更多的透明、诚实和谦逊，而 Opus 4.6 表达更多的简洁。我们也在其 [发布博客文章](<https://www.anthropic.com/news/claude-sonnet-4-6>) 中将 Sonnet 4.6 描述为温暖、诚实和亲社会的。我们的轴能够还原这些印象，这一事实表明，我们标注和比较 Claude 所表达价值观的方法正在追踪关于模型实际行为方式的真实情况。
在多次对话中，用户与不同的 Claude 模型互动时可能会遇到不同的价值观组合。例如，Opus 4.7 倾向于对用户的工作提供坦诚的批评或主动警告风险，而 Sonnet 4.6 倾向于鼓励和幽默。模型之间价值观的此类差异很可能是由性格训练决策（以及其他因素）塑造的，而我们的价值观轴方法突出了 Claude 所表达价值观的关键差异，我们最终也许能够把这些差异追溯到这些训练选择上。
##   
**Claude 所表达的价值观在不同语言之间是否有差异？**
我们预期 Claude 所表达的价值观会因对话语言而异，原因有几个。首先，Claude 的训练数据在不同语言间不同，这可能塑造它所表达的价值观。其次，我们在系统卡（system card）中分享的模型评估已经 [发现 Claude 在不同语言中知道什么、如何处理敏感请求方面存在差异](<https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf>)。7 衡量 Claude 所表达的价值观随语言变化的程度，是判断跨语言差异是反映了合理的变异、还是应该在训练中加以解决的第一个步骤。
我们用与上一节相同的方法计算 Claude 的价值观画像在 [Claude.ai](<http://claude.ai/redirect/website.v1.c4912eba-b7dd-40b1-a1ef-1a55aaf58274>) 上最常用的 20 种语言之间如何不同。下面，我们绘制 Claude 在 Claude 平台上常用语言中的价值观画像，从 Claude 所表达价值观分歧最大的语言开始。
![Alt text: Twenty value profile cards comparing Claude's value expression across the four value axes \(Deference vs. Caution, Warmth vs. Rigor, Depth vs. Brevity, Candor vs. Execution\) and distinctive behaviors, one card per language. Each card shows Claude's average position for that language in standard deviations from the average across all conversations, and its distinctive behaviors. Claude's value expression across the four value axes and distinctive behaviors are described in the figure caption and in the text below the figure.](assets/claude-values-models-languages/img_004.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
![Alt text: Twenty value profile cards comparing Claude's value expression across the four value axes \(Deference vs. Caution, Warmth vs. Rigor, Depth vs. Brevity, Candor vs. Execution\) and distinctive behaviors, one card per language. Each card shows Claude's average position for that language in standard deviations from the average across all conversations, and its distinctive behaviors. Claude's value expression across the four value axes and distinctive behaviors are described in the figure caption and in the text below the figure.](assets/claude-values-models-languages/img_005.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
![](assets/claude-values-models-languages/img_006.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
![](assets/claude-values-models-languages/img_007.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
![](assets/claude-values-models-languages/img_008.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
![](assets/claude-values-models-languages/img_009.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
![](assets/claude-values-models-languages/img_010.img)图 4：Claude 用每种语言交谈时在四个价值观轴上的平均位置（以与所有对话均值的标准差表示），以及 Claude 在每种语言中的独特行为。Claude 在印地语中最偏向温暖，在俄语中最偏向严谨。Claude 在印度尼西亚语中最偏向执行，在荷兰语中最偏向坦诚。Claude 在阿拉伯语中最偏向顺从和简洁，在英语中最偏向谨慎和深度。
Claude 的价值观表达在"温暖 vs. 严谨"和"坦诚 vs. 执行"轴上随语言变化最大，而在"顺从 vs. 谨慎"和"深度 vs. 简洁"轴上最稳定。
  * **顺从 vs. 谨慎。** Claude 在阿拉伯语中表达最多的顺从，在英语中表达最多的谨慎。
  * **温暖 vs. 严谨。** Claude 在印地语和阿拉伯语中表达最多的温暖，其特征是礼貌用语、幽默和俏皮，以及对一个人想法和工作的肯定。Claude 在英语和俄语中最倾向于表达严谨，其特征是挑战假设、纠正细节和要求证据。
  * **深度 vs. 简洁。** Claude 在英语中偏向深度，对细节加以精炼和纠正，而在阿拉伯语中偏向简洁。
  * **坦诚 vs. 执行。** Claude 在荷兰语中偏向坦诚，承认自己的错误，而在印度尼西亚语中偏向执行。

综合来看，这些结果表明 Claude 所表达的价值观会随着对话语言而有意义地变化。面对同一种请求，Claude 在某些语言中更倾向于温暖和顺从，在另一些语言中更倾向于严谨和谨慎。这有重要的影响，而我们只是刚开始探索。举一个例子：两个人就同一份商业计划征求意见，一个用印地语，一个用俄语，他们可能对其质量留下不同的印象，因为 Claude 在框定其评估的方式上表达了不同的价值观。
我们还不知道训练数据的哪些属性导致了这些差异。一种可能是我们的训练数据在语言间分布不均。有些语言的数据比其他语言多得多，而在数据丰富的语言中，训练 Claude 表达一致的价值观可能更有效。数据的构成也各不相同。例如，某些语言可能在专业写作中占比过高，而这类文本可能反映不同的价值观。数量与构成上的这些不平衡加在一起，可能导致 Claude 在不同语言中表达不同的价值观。
我们也还无法确定这种变异有多少是可取的。不同语言承载着不同的会话规范，Claude 可能是根据这些规范以不同的价值观作出回应。Claude 也可能在某些语言上比在其他语言上更贴合我们的预期行为，从而导致 Claude 服务某些语言社区的质量存在差距。
这种方法让我们能够开始厘清训练数据的哪些属性驱动了这些差异——以及这种变异是否可取。
## **展望**
我们证明了 Claude 所表达的价值观可以压缩到少数几个轴上，而且 Claude 在这些轴上的位置会随模型和语言而变化。这给了我们一种在模型评估和部署后监控期间跟踪这些变化的方法。但我们还不理解这些变化为什么会发生，或者它们对与 Claude 互动的人意味着什么。下面我们勾勒我们认为最有前景的未来方向。
**这些价值观差异从哪里来？**
知道 Claude 的价值观随模型和语言变化并不能告诉我们 _为什么_。有些变异可能是继承自不同语言在预训练和微调数据上的差异。我们的四个轴指出了在训练数据中应该更仔细检查哪些价值观差异。把这些差异追溯到具体的数据、训练阶段或情境因素，将告诉我们如果想以更细致的方式塑造 Claude 的行为，应该在哪里干预。
**这些差异对用户意味着什么？**
我们已经测量了 Claude 表达了哪些不同的价值观及其相关行为，但没有测量这些对用户产生什么影响。借助 [Anthropic Interviewer](<https://www.anthropic.com/research/anthropic-interviewer>) 之类的工具，我们可以询问用户的幸福感、对 Claude 的信任或 Claude 的决策质量，然后把这些影响与 Claude 所表达的价值观关联起来。这将让我们能够直接把价值观差异与用户结果联系起来，并让我们能够优先修复那些切实影响用户的价值观差异。
**Claude 的价值观应该如何随语言变化？**
[Claude 的宪法](<https://www.anthropic.com/constitution>) 描述了它应表达的核心价值观，如温暖、谨慎和诚实，但没有规定这些价值观 _应该_ 如何随语言变化。我们的结果表明，使用不同语言的用户已经在体验不同的 Claude，但我们不知道用这些语言与 Claude 互动的用户想要什么样的变异。确定 Claude 的价值观应如何随语言变化，意味着要理解并权衡说这些语言的人的观点。
**还有哪些其他因素驱动 Claude 所表达价值观的差异？**
语言和模型不太可能是 Claude 表达哪些价值观的唯一驱动因素。价值观还可能受年龄、职业或地理区域等人口统计信号的影响，无论这些信号来自用户所写内容的显性线索，还是来自与提问者是谁相关的主题、语气和风格的微妙差异。了解这些信号中哪些重要，以及由此产生的变异是否很好地服务了用户，是我们的方法所促成的一个下一步。
**我们能可靠地引导 Claude 所表达的价值观吗？**
有了测量模型价值观画像的方法，自然会引出一个问题：我们能多可靠地引导 Claude 所表达的价值观？一种测试方式可能是尝试通过性格训练调整或系统提示词更改来引导价值观，然后用我们的价值观轴方法验证模型的价值观表达是否按预期变化。
**价值观画像能成为我们评估和监控模型的一部分吗？**
价值观轴方法给了我们一种简单的方式来总结模型在开放式对话中的行为倾向，我们可以把它构建到评估流程中。在模型发布前和发布后运行价值观画像，可以标记 Claude 所表达价值观的意外变化。我们还可以识别价值观画像与问题行为（如不遵守 Claude 的宪法）之间的相关性，并利用所学来改进 Claude 的行为。
Claude 每天在数十种语言的数百万次对话中表达价值观，而直到现在，这些价值观还是我们在训练中可以塑造、但在部署中无法可靠观察的东西。现在我们有了测量它们的方法，可以看到 Claude 所表达的价值观以我们并未刻意选择的方式变化，我们也可以研究它们为何变化，以及这种变化是否服务了用户。理解这种变异并决定如何应对，是我们将继续开展的工作。
### **  
作者**
Matt Kearney、Miranda Zhang、Shan Carter、Judy Hanwen Shen、Kunal Handa、Jerry Hong、Saffron Huang、Miles McCain、Thomas Millar、Michael Stern、Mo Julapalli、Suzanne Wang、Devin Kuokka、Andrea Vallone、Shaoyi Zhang、Jim Baker、Kevin Troy、Matt Botvinick、Hanah Ho、Monika Tuchowska、Sarah Pollack、Jake Eaton、Deep Ganguli、Esin Durmus
**致谢**
感谢以下人士在工作的不同阶段提供反馈：Amanda Askell、Joe Carlsmith、Jack Clark、Ishita Dasgupta、Andrew Lampinen、Shayne Longpre、David Saunders、Taylor Sorensen、Heather Whitney。
### Bibtex
    
    @online{anthropic2026values,
      author = {Matt Kearney and Miranda Zhang and Shan Carter and Judy Hanwen Shen and Kunal Handa and Jerry Hong and Saffron Huang and Miles McCain and Thomas Millar and Michael Stern and Mo Julapalli and Suzanne Wang and Devin Kuokka and Andrea Vallone and Shaoyi Zhang and Jim Baker and Kevin Troy and Matt Botvinick and Hanah Ho and Monika Tuchowska and Sarah Pollack and Jake Eaton and Deep Ganguli and Esin Durmus},
      title = {Claude's Values Across Models and Languages},
      date = {2026-07-13},
      year = {2026},
      url = {https://anthropic.com/research/claude-values-models-languages},
    }
###   
附录
可在此处获取。[](<https://cdn.sanity.io/files/4zrzovbb/website/02da7f28f74daa1be526d3ded451a4efc86bccdc.pdf>)
#### 脚注
  1. 我们把价值观定义为规范性考量，如诚实或谨慎，它们在 Claude 的回答中被陈述或展示。当我们提到 Claude 所表达的价值观时，我们指的是 Claude 的行为和输出所反映的价值观。我们并不暗示 Claude 内在地持有价值观。
  2. 请参阅我们 [Claude Opus 4.7 系统卡](<https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf>) 第 56 页良性请求评估中按语言区分的不同拒绝率。
  3. 这四个轴在 _控制_ 了对话任务、主题和用户表达的价值观之后，解释了对话间价值观总方差的 15%。
  4. 本文中任何提到 Claude 而未注明模型名的结果，都基于我们研究的全部三个模型——Sonnet 4.6、Opus 4.6 和 Opus 4.7——的对话。
  5. 数据来自 2026 年 5 月为期两周的对话。
  6. 我们删除了出现在超过 80% 对话中的 18 种价值观（例如，乐于助人、清晰、遵循指令）。这些近乎普遍的价值观本来会主导分析，却不告诉我们任何关于价值观在对话间变异的信息。
  7. 请参阅我们 [Claude Opus 4.7 系统卡](<https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf>) 第 215 页的 GMMLU 评估结果，以及第 56 页良性请求评估中按语言区分的不同拒绝率。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/claude-values-models-languages>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/claude-values-models-languages>)
## 相关内容
### 了解更多关于 Claude 的数学能力
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足该猜想的黎曼 zeta 函数零点比例的下界——将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而设计的数字签名方案。第二个攻击确定了一种攻击减轮 AES（最广泛使用的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新评估，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)