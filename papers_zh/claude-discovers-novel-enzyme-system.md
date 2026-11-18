---
title: Claude discovers a novel enzyme system with CRISPR-like repeats
url: https://www.anthropic.com/research/claude-discovers-novel-enzyme-system
date: Sep 23, 2026
category: Science
source: https://www.anthropic.com/research
---

# Claude 发现一种带有类 CRISPR 重复序列的新型酶系统

- **日期：** 
- **类别：** 科学（Science）
- **来源：** https://www.anthropic.com/research/claude-discovers-novel-enzyme-system

---

科学（Science）
2026 年 9 月 23 日
![视频缩略图](assets/claude-discovers-novel-enzyme-system/img_000.webp)
已发布
    2026 年 9 月 23 日
主题
    
  * [生命科学](</search?topic=life-sciences>)
  * [发现](</search?topic=discovery>)
  * [智能体](</search?topic=agents>)
  * [研究项目](</search?topic=research-programs>)

[](</research/teaching-ai-to-build-scientific-models>)[](</research/investigating-vault-particles-with-claude>)[](</research/claude-scorpion-toxin-binder-design>)[](</research/accelerating-scientific-research>)
相关文章
  * 科学
2026 年 11 月 6 日
[教 AI 构建科学模型](</research/teaching-ai-to-build-scientific-models>)

[阅读更多](</search?topic=life-sciences>)
_我们正在 Anthropic 组建一个新的生命科学研究小组与实验室。我们的重点是使用 Claude 开展基础生物学研究：探索 DNA 数据集以识别尚未表征的蛋白质家族，大规模生成假设，并通过实验室实验加以检验。本文介绍了这项工作背后的团队，并分享早期成果——在科学家仅给出高层次指导的情况下，Claude 发现了一个性质令人联想到 CRISPR 的新型酶系统。_

_许多彻底改变生物学与医学的发现，都始于某位科学家在自然界令人惊叹的分子机器多样性中注意到某种异常。限制性内切酶——即在特定短序列处切割 DNA 的蛋白质——最初发现于细菌的免疫系统，它们在那里摧毁入侵病毒的 DNA。研究人员意识到，可以利用这些酶在选定位置切割 DNA，并把一个生物体的基因拼接到另一个生物体中，由此催生了生物技术产业。Taq 聚合酶是一种在高温下复制 DNA 的酶，最初在黄石公园一处温泉里的细菌中被发现，后来成为 PCR 的基础——PCR 是现代诊断中广泛使用的 DNA 复制方法。CRISPR 最初只是某些细菌 DNA 中一段不同寻常的重复序列，如今则成为基于基因编辑的药物的基石。_

2026 年春天，我们组建了一个研究小组，想看看通用 AI 模型能否把这类发现系统化，并[加速这类发现](<https://darioamodei.com/essay/machines-of-loving-grace#1-biology-and-health>)。我们相信，这种加速将来自确立一种开展生物学研究的新方式：在这套流程的每一步，智能体都与人类协作。要建立这种新的工作方式，我们需要建起自己的实验室，并组建一支单一团队，承担从训练 Claude 掌握生物学到在实验室里开展实验的全部工作。
今天，我们分享首批研究项目之一的早期成果：Claude 自主发现了一个与一串 DNA 重复序列相关联的新型酶系统，这一模式令人联想到 CRISPR。尽管我们尚不清楚它的功能，但 Claude 发现的这个系统具备一组特征，此前只在少数几个其他系统中同时出现过，而那些系统全都是可编程的，能够执行切割、复制与粘贴 DNA 之类的操作。除了已经改变了科学与医学的 CRISPR 之外，另外几个此类系统如今也正作为前景可观的工具处于开发之中。
Claude 发现的这个系统建立在逆转录酶（RT）之上，这类酶能把 RNA 复制成 DNA。虽然这个来自巨型噬菌体（jumbo phage）的基础 RT 在以往研究中已被鉴定出来，但 Claude 似乎是第一个注意到该系统界定特征的研究者——与之相关联的一串非编码 DNA 序列，以及一个功能未知的额外辅助蛋白。
在审阅预印本之后，CRISPR 基因组编辑先驱之一、MIT 与 Broad Institute 教授 Feng Zhang 表示：
> _这是 AI 智能体能够为生物学发现作出贡献的一个令人振奋的范例。与逆转录酶相关联的 RNA 重复序列阵列的鉴定确实耐人寻味，值得深入研究。我希望这项工作能鼓励更多科学家去探索 AI 可以如何支持他们的研究。_
我们给 Claude 下达了一个提示，让它在庞大的 DNA 序列数据库中搜索值得关注的新 RT 实例。我们的参与仅限于最初的提示与实验室工作，而 Claude 智能体则梳理数据库、考察各个不同的 RT 家族，并运用自己的判断挑出有意思的候选对象。在大约 950 个智能体耗费 210 million 个 token、用 21 小时检索这些数据之后，其中一个智能体发现了非同寻常的东西：一段重复的 DNA 序列模式，出现在某个模样古怪的 RT 的基因旁边。经过我们实验室的进一步分析与检验，我们确认这一模式标志着一个此前未被表征的酶系统，它存在于噬菌体（感染细菌的病毒）中，我们称之为阵列相关逆转录酶（array-associated reverse transcriptases，ART）。
我们理解 ART 主要功能的各项工作仍在进行中。不过，我们认为尽早分享这类发现很重要，既能展示 Claude 的能力，也能让更广泛的社群了解我们正在做什么。我们已经发布了一份预印本，详见[此处](<https://www.biorxiv.org/content/10.64898/2026.10.05.755809v1>)。
## 关于我们的实验室
我们是一支由科学家组成的团队，职业生涯一直致力于探索不寻常的蛋白质，并专长于运用计算方法系统地解读 DNA、阐释其演化，挑出值得进一步表征的生物系统。在加入 Anthropic 之前，我们的研究帮助人们更好地理解 CRISPR 系统的[演化](<https://www.science.org/doi/10.1126/science.aei0498>)与[调控](<https://www.nature.com/articles/s41586-018-0557-5>)，发现面向下一代[细胞与基因疗法](<https://www.science.org/doi/10.1126/science.adz0276>)的新[酶](<https://www.nature.com/articles/s41586-024-07552-4>)，并构建[工具](<https://www.nature.com/articles/s41586-026-10176-5>)以加速识别 DNA 中的异常，例如人类致病变异。我们隶属于 Anthropic 的生命科学组织，与从事药物发现、以及训练 Claude 掌握生物学与化学的团队并肩工作。
我们的实验室位于湾区，看上去就是一间普通的分子生物学实验室。我们只从事涉及较低生物安全风险等级（BSL-1 与 BSL-2）的研究，不处理能够感染人类的病原体。所有实验室工作都由人类科学家完成。尽管我们曾通过 [Model Hardware Standard](<https://www.anthropic.com/news/model-hardware-standard-research-preview>) 之类的举措，尝试用 AI 加速实验室工作，但这种方式不太适合我们分子生物学研究里那些临时应变的工作流。
## 我们的工作方式
我们的许多工作流都让 Claude 在海量与功能未知蛋白质相关的 DNA 序列集合中检索。一种典型模式始于对某个给定蛋白质家族的普查。Claude 阅读相关文献，用公开数据复现已确立的结果，以检验自己的方法。随后，它搜索不属于任何已描述系统的家族成员或基因组邻居，并为每个候选对象撰写一份简短、可供人阅读的报告，提出一种功能，并说明支撑其论断的证据。在后续分析中，Claude 会批判性地评估这些证据——通常大多数候选对象会在这一阶段被淘汰。一次普查最终可能只留下一个值得检验的候选对象，也可能一个都没有。
当某个候选对象通过我们的审阅后，我们会在实验室里检验它：在标准实验室菌株中表达该蛋白质，并从生化与结构两方面对其进行表征，Claude 则协助解读数据。我们在 [Claude Science](<https://claude.com/product/claude-science>) 和 [Claude Code](<https://claude.com/product/claude-code>) 中开展工作，也就是任何科学家都能用到的同样工具，有时还会用我们自己编写的一套脚手架，来协调许多并行运行的 Claude 会话。
由于 Claude 生成假设的速度如此之快，假设本身也成了我们研究的对象。单轮研究就能产出数百到数千份候选报告，我们一直在追问：那些我们判定值得检验的提议，与我们搁置一旁的提议，究竟有何区别。我们学到的东西会重新写进给 Claude 的指令里，教会它模仿我们自己的科学品味。
## Claude 发现 ART
在过去几年里，研究者发现了更多逆转录酶（RT），其中大多数来自细菌，在那里它们作为免疫系统的一部分发挥作用。几乎所有 RT 家族都是通过基因组分析、也就是基因组挖掘（genome mining）找到的：这要求研究者在序列数据库中搜索尚无人表征的基因，留意其中不寻常的那些，并弄清它们的功能。
Claude 智能体收集了超过 200,000 个 RT，挑出 3,500 个新的候选系统，再将其缩小到 20 个最引人注目的候选对象，并逐一分析、产出可供人阅读的报告。对一位专家科学家而言，这类分析可能要花上数周乃至数月。
在研究过程中，Claude 注意到一个不寻常的 RT 家族，并决定更仔细地审视它。在梳理 RT 附近的原始 DNA 序列时，这个智能体惊呼：「[RT 旁边的 DNA] 太壮观了：我肉眼就能看到一个串联重复阵列……这是一个类 CRISPR 的……重复阵列？！」

![一张展示 Claude 识别 DNA 中模式的图示](assets/claude-discovers-novel-enzyme-system/img_001.img)
Claude 检测到一个此前无人注意到的重复模式时，正在读取的原始 DNA
 _  
_随后，它大体上像一位人类科学家面对潜在发现时那样继续推进。它数出重复单元的数量、测量它们之间的间距，把这一排布与已知的 RT 系统相比较，并在文献中检索是否曾有人报告过这一模式。经过透彻的分析，它确信自己发现了一个新的生物系统，并提交了一份报告供人类审阅。_
它发现的这个系统 ART 主要存在于噬菌体中，由三部分组成：RT、紧邻其旁的一个伙伴基因，以及一长串间距均匀的 DNA 重复序列。这种重复排布类似 CRISPR 阵列——后者储存着一组各不相同的 RNA 序列，正是它们让 CRISPR-Cas 系统成为可编程的生物技术工具。我们的首批实验表明，ART 阵列同样会表达为一组彼此不同的短 RNA，这暗示该系统里可能存在某种类似的机制。
进一步实验正在进行，以确定 ART 的工作机制；我们分享这些早期发现，是为了向社群表明，Claude 能够自主察觉异常，并推动分析、开启生物学发现。
更多细节可参见我们的技术报告，详见[此处](<https://www.biorxiv.org/content/10.64898/2026.10.05.755809v1>)。
### 与我们合作
我们希望这项工作能向更广泛的科学界展示由 AI 驱动假设生成的价值，也愿意与其他科学家合作，把这套方法推广到基因组学及其他领域的广泛问题上。如果你有研究问题的设想，我们很乐意听到你的声音。
