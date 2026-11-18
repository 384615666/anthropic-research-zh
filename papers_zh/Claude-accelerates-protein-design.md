---
title: How Claude is accelerating protein design and analytical chemistry
url: https://www.anthropic.com/research/Claude-accelerates-protein-design
date: Aug 18, 2026
category: Science
source: https://www.anthropic.com/research
---

# Claude加速蛋白质设计与分析化学

- **日期：** 
- **分类：** 科学（Science）
- **来源：** https://www.anthropic.com/research/Claude-accelerates-protein-design

---

科学（Science）
2026 年 8 月 18 日
**摘要：** 在这篇文章中，我们分享两项结果，展示 Claude 如何帮助生命科学研究人员加快研究节奏。第一项中，我们测试了 Claude 从头设计蛋白质结合体（protein binders）的能力——这是药物设计流程早期阶段的一项关键任务，历史上每位靶点专家都要耗费数周乃至数月。Claude（Mythos Preview 与 Opus 4.8）针对 15 个靶点设计了蛋白质结合体，其中 14 个成功。根据设置不同，其单个设计的结合成功率在 22% 到 35% 之间，而当今蛋白质设计项目中的典型水平为 10–15%。它一些最强的设计结合紧密度达到此前已发表最佳结果的数倍。第二项示例中，我们评估了 Claude 能否加速化学分析。已普遍可用的模型 Claude Opus 5 被提供了 NMR 与 LC-MS 数据（这类数据让化学家能够评估其所用化合物的身份与纯度）。在仅提供一家合同实验室的原始文件和一句两句话的提示下，Claude 在 23 分钟和 19 分钟内返回了成品结果，在氢原子计数和纯度上与该实验室自身的分析一致（96.4% 对 96.33%）。这些示例展示了 Claude 如何减少推进复杂科学任务当前所需的时间与计算专业知识。

过去几个月，AI 驱动发现的步伐已经加快。这些发现大多出现在验证相对较快的领域。例如，在数学领域，智能体已开始着手攻克未解问题：几十年来悬而未决的 [Erdős 问题](<https://openai.com/index/model-disproves-discrete-geometry-conjecture/>) 正以每月数个的速度被攻克，而我们最近也分享了 Claude 如何改进了与 [黎曼 zeta 函数](<https://www.anthropic.com/research/riemann-zeta>) 相关的长期下界。

AI 模型也开始加速那些验证结果更复杂、更昂贵的实验领域（如生命科学）的进展。在这篇文章中，我们分享两项关于 Claude 科学能力的实验结果。首先，我们呈现对 Claude 在蛋白质设计项目中表现的研究发现，表明 Claude 能够设计出与（甚至优于）顶尖人类专家相当的多靶点蛋白质结合体。其次，我们分享 Claude Opus 5 在分析化学任务上的表现，展示通用访问模型如何支撑研究中常规且耗时的环节。

下文描述的蛋白质设计与分析化学任务，代表了药物开发流程早期某些阶段工作的典型部分。加速这些阶段是我们更大规模的端到端加速药物开发努力的组成部分，而其中许多方面与政策及运营瓶颈的关系，大于核心科学能力的提升。

我们今天分享的结果，是通过我们的 Mythos 与 Opus 模型组合取得的。尽管生命科学的研究任务在我们能力最强的模型上目前受到限制，但我们的最高优先级之一是为科学家启动一项访问计划，我们预计很快会就此分享更多信息。与此同时，Opus 5 仍是我们能力最强、普遍可用的模型。

## **Claude 设计蛋白质**

当我们[发布 Claude Mythos 5](<https://www.anthropic.com/news/claude-fable-5-mythos-5>) 时，我们曾分享正在尝试用该模型加速药物设计流程的某些环节。作为这项工作的持续推进，我们一直在研究 Claude 为多个蛋白质靶点设计微型结合体（minibinders）的能力。微型结合体是一种被设计来紧紧扣住目标蛋白的小型蛋白质。结合是现代大部分药物发挥作用的方式：它们附着于靶点，并抑制、激活或向其递送某种物质。设计一种新的结合体（即所谓的 _de novo_ 设计）在历史上每个靶点都需要蛋白质工程师数月的算力、优化与筛选。

近年来，能够设计蛋白质并对哪些最有可能结合进行排序的机器学习模型，大大加快了蛋白质设计流程。但这些模型通常仍需要计算专家进行数天（往往数周）费力的人工编排。尽管像 Claude 这样的通用推理模型能帮助专家和非专家更高效地进行蛋白质的计算设计，但在湿实验室中验证这些数据（科学家在其中实际测试化学品、药物及其他生物物质）仍需数周。

我们现在已收到其中首个实验的湿实验室数据——一项针对 15 个靶点、使用 Claude Opus 4.8 与 Mythos Preview 的多臂蛋白质设计项目。我们的外部评估方 [Adaptyv Bio](<https://www.adaptyvbio.com/>) 与 [Twist Bioscience](<https://www.twistbioscience.com/>) 在实验室中独立生成并测试了 Claude 的设计，发现在我们所针对的 15 个靶点中，Claude 成功为其中 14 个设计了结合体。其中包括针对至少 6 个靶点的高亲和力结合体1，以及亲和力达到或超过此前报道最佳水平的结合体（针对至少 4 个靶点）。亲和力衡量的是蛋白质与其靶点结合的强度；高亲和力结合体通常是产生治疗效果所必需的，因为它们能让药物在低剂量下生效，从而降低副作用风险与制造成本。

Mythos Preview 与 Opus 4.8 在 48 小时会话中同时针对所有靶点设计时，分别取得了 26.7% 与 22.6% 的整体命中率（即设计中有多少确实成为结合体）。当今蛋白质设计项目中的典型水平为 10% 到 15%。2

在评估了 Claude 针对多个靶点的设计能力后，我们想了解让它一次专注于单个靶点能否提升表现，尤其是考虑到这更能代表蛋白质工程师通常采取的方法。事实的确如此：我们发现 Mythos Preview 在使用多个 24 小时会话、分别针对每个靶点进行设计时，取得了 35.1% 的整体命中率。

![展示整体命中率的图表](assets/Claude-accelerates-protein-design/img_000.webp)Mythos Preview 与 Opus 4.8 在一组 15 个靶点上取得了超过 20% 的命中率，靶点层面的命中率最高达 90%，最低为 0%。

该项目在除我们初始提示提供给 Claude 的信息之外，几乎无人介入3（[链接](<https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/tree/main>)）。我们预期，在专家蛋白质设计者手中，这种方法会产出更强的结果，尤其是如果他们就中间结果向 Claude 提供积极的指引与反馈。

#### **项目设计**

我们启动蛋白质设计项目时，选取了多个蛋白质设计基准中常用的靶点4，包括 Adaptyv Bio 的全部 [BenchBB](<https://www.adaptyvbio.com/blog/benchbb>)。由于这些靶点已被广泛研究，我们可以将结果与已发表的命中率和亲和力进行对比。我们还从 Adaptyv Bio 最近的竞赛中选取了两个新颖靶点 [15-PGDH](<https://proteinbase.com/collections/berlin-bio-x-adaptyv-15-pgdh-binder-design-competition>) 与 [GDF-8](<https://proteinbase.com/collections/gdf-8-challenge-results>)，以确保 Claude 能够针对那些无法从其训练数据或在线搜索中调取已有成功记录的靶点进行设计（对所有靶点，我们都要求 Claude 检查并确保其设计为原创）。

随后，我们在 [Claude Science](<https://www.anthropic.com/news/claude-science-ai-workbench>) 中提示 Claude 针对这些靶点设计蛋白质结合体。为此，我们采取了两种方式。第一种是多靶点模式，Claude 在单个 Claude Science 会话中同时针对所有靶点设计。第二种是单靶点模式，每个会话处理一个靶点，所有靶点的会话并行运行。

我们以多靶点模式运行 Opus 4.8 与 Mythos Preview，墙钟时间为 48 小时，并最多使用 12,500 个 NVIDIA H100 小时算力来运行专用的蛋白质设计与折叠模型。我们还以单靶点模式运行 Mythos Preview，每个靶点墙钟时间 24 小时，最多 2,500 个 NVIDIA H100 小时算力。5

为模拟典型蛋白质设计项目期间可用的资源，我们向 Claude 提供了以下内容：
  1. 一份详尽的蛋白质设计提示6，同时也包含在智能体上下文中；
  2. 访问互联网及一个资源语料库，如关于蛋白质设计的论文；
  3. 连接 Google Drive、Slack、Gmail 与 BioRxiv 的接口；
  4. 访问用于运行专用蛋白质设计与折叠模型的 GPU；
  5. 在分配时间内对 token 与子智能体预算不设限制，并启用快速模式。

在向 Claude 给出提示后，我们让模型自主执行。在启动项目后，我们没有提供任何额外的科学、技术或运营指引。

我们唯一的参与是批准访问权限（如网络访问请求）以及监控基础设施以确保会话正常运行。Claude 完成了设计结合体所需的全部工作，而一名人类操作员完成这些可能要数周。它选择在每个蛋白质靶点的哪个位置进行设计；通过编排多个结构设计、序列设计与共折叠模型（这些模型在一次运算中预测蛋白质连同其结合对象的结构）来生成候选结构与序列；让设计经历多轮 _in silico_ 优化；并从计算上筛选出能够表达、保持可溶并结合的新颖、多样的候选。

对于 15 个靶点中的每一个，我们都要求 Claude 设计 30 个蛋白质结合体。Claude 通过操作该领域已在使用的公开专用蛋白质设计与共折叠模型来完成此事。Claude 的设计随后被送往 Adaptyv Bio 与 Twist Bioscience 进行验证。

![展示 Claude 如何组合开源蛋白质模型的桑基图](assets/Claude-accelerates-protein-design/img_001.webp)Claude 成功编排多个开源蛋白质设计模型，生成具有高成功率与高亲和力的结合体。a) 桑基图描绘 Claude 对结构设计、序列设计与优化轮次的组合。b, c) Claude 为所有至少订购 100 个设计的结构设计方法，设计出命中率超过 20%（含高亲和力结合体）的结合体。

## **Claude 在各靶点上的表现**

到这一努力结束时，我们针对 15 个靶点中的 14 个产出了 354 个结合体，共使用 1,320 个设计。这对于公开可用的 _de novo_ 蛋白质设计总库是一项重要贡献；例如，两个最大的集合 [proteinbase.com](<https://proteinbase.com>) 与由 [Overath 等人](<https://www.biorxiv.org/content/10.1101/2025.08.14.670059v2>) 整理的集合，分别包含约 770 个结合体（出自针对 40 个靶点的 5,700 个设计）。下面，我们分享三个凸显 Claude 能力的示例，以及一个展示其局限性的示例。更多细节见于我们的技术报告（[链接](<https://www-cdn.anthropic.com/30bf50e22a01388bb29bf077ee3f244531594b7a.pdf>)）。

#### **Claude 的设计可与 Adaptyv Bio 蛋白质设计竞赛的参赛作品媲美**

我们发现，对于 Adaptyv Bio 已举办竞赛的靶点，Claude 在命中率与亲和力上都达到或超越顶级参与者的水平。针对 RBX1（一种驱动特定调控蛋白靶向降解的小型蛋白），单靶点模式下的 Mythos Preview 取得了 40% 的命中率，而参与者的命中率为 3.7%。其排名最高的设计是一个高亲和力结合体，表现优于获奖设计——后者在提交的 245 个设计中。

![展示亲和力与整体表现的图表](assets/Claude-accelerates-protein-design/img_002.webp)Claude 针对 RBX1 设计的结合体具有最先进的亲和力，并一贯超过 Adaptyv Bio 蛋白质设计竞赛中记录的命中率。

#### **Claude 设计出针对 TNFα 的跨物种反应性结合体——一个具挑战性、与治疗相关的靶点**

有趣的是，在 TNFα 上取得成功的是 Opus 4.8 而非 Mythos Preview——多个专家团队都曾在 TNFα 上受挫。TNFα 是一种由免疫系统释放、用于触发炎症的信号蛋白，阻断它是史上最具影响力药物（包括 Humira）的治疗基础。它是一个难以设计的靶点，因为其多聚体结构需要瞄准由两个蛋白质形成的凹槽中的结合位点。尽管 Mythos Preview 未成功，Opus 4.8 设计了多个结合体，其中包括一些跨物种起效的——结合人、食蟹猴和小鼠的 TNFα，这对开展动物研究十分重要。我们不确定为何 Opus 4.8 在此靶点上成功而 Mythos Preview 没有。在评估我们模型的能力时，我们采取整体视角。鉴于蛋白质设计固有的复杂性，某个总体能力较弱的模型仍能胜过总体能力更强的模型，出现于某些具体领域并不令人意外。

![展示 Opus 针对 TNFα 工作的图表](assets/Claude-accelerates-protein-design/img_003.webp)Opus 4.8 成功设计了针对 TNFα 的 _de novo_ 结合体，其中一些具有交叉反应性，结合了人、食蟹猴和小鼠的 TNFα。

#### **Claude 设计出含 β-折叠、折叠方式多样的结合体**

大多数计算设计的结合体是 α-螺旋束——一种由卷曲构成的蛋白质二级结构。β-折叠中，伸展开的氨基酸链必须并排对齐，更难设计，也更容易发生错误折叠与聚集（蛋白质分子彼此黏附而非保持分离并正确折叠）。Claude 在六个靶点上设计了 15 个经确认的、含至少 20% β-链的结合体，展示了其推理蛋白质结构的能力。

![展示 Claude 在 15 个结合体上表现的图表](assets/Claude-accelerates-protein-design/img_004.webp)Claude 成功针对六个靶点设计了 15 个（跨越 10 个不同骨架）含 β-折叠的结合体。

#### **Claude 在某些靶点上遭遇困难**

某些靶点对 Claude 仍是挑战，包括 BBF-14 与麦芽糖结合蛋白（MBP）。BBF-14 是一种自然界不存在的 β-桶形蛋白：它本身即是 [_de novo_ 设计](<https://www.nature.com/articles/s41586-024-07601-y>) 的，如今正因为其新颖性而被用作结合体设计的基准。MBP 的结构也格外困难。MBP 是一种大型、柔性的细菌蛋白，表面光滑、亲水，使其成为一种良好的实验试剂。这留给结合体的可附着点极少。Claude 仍设法产出了三个独立的 BBF-14 结合体——每个设计臂各一个，且每个建立在不同骨架上——具有中等（亚微摩尔到微摩尔）亲和力。然而针对 MBP，90 个设计中无一被确认结合到靶点，尽管有一个显示出微弱的、可重复的结合信号。

![展示 Claude 遭遇困难的一个示例的图表](assets/Claude-accelerates-protein-design/img_005.webp)Claude 在针对 BBF-14（一种 _de novo_ 设计的 β-桶）与麦芽糖结合蛋白（MBP）设计蛋白质结合体上成功有限。

为更好地理解 Claude 在这些设计项目中的整体表现，我们打算在实验之后进行更广泛的表征，以确认我们的命中率与亲和力测量。同时，我们正在分享这些项目所用的提示，以及我们生成的所有 _in vitro_ 与 _in silico_ 数据。7

#### **智能体式生物发现具有双重用途**

AI 模型日益自主的研究能力所带来的提升，无疑将加速人类疗法与基础科学发现的发展。然而，这类能力也是双重用途的：若无强健的安全措施，它们可能让恶意行为者得以开展危险研究，例如开发生物武器。在我们通过受信任的访问计划安全交付这些能力的同时，蛋白质设计及其他双重用途研究生物学能力在 Claude Fable 5 中[仍不向通用访问开放](<https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards>)。不过，正如你将在下文看到的，我们的 Opus 级模型能够完成非凡的科学工作。

## **Claude 运行分析化学工作流**

蛋白质结合体项目测试的是 Claude 设计新分子的能力，而第二个实验测试的是它解读已合成分子测量结果的能力。表征一个化合物是繁琐的工作；与蛋白质设计类似，它需要化学家进行多轮测量、分析与迭代。例如，每当化学家合成一个分子，他们都必须确认它是不是预期产物，以及纯度如何。这通常借助核磁共振（NMR）光谱来完成。一张 NMR 谱图是一系列峰，每个峰对应分子中某处的某个氢原子，或一组等价的氢原子。峰的位置告诉化学家每个氢原子连接着什么，峰的大小显示它代表多少个氢原子。确认一种结构，是合成化学中最耗时的步骤之一；对于每个化合物，化学家都必须手工将谱图中的每个峰匹配到所提结构中的一个原子。

另一种主要用于评估纯度的技术是液相色谱-质谱联用（LC-MS），它先让样品在流过色谱柱时分离为各个组分，再根据其紫外吸收记录每种组分的含量，然后测量每种组分的分子量。对于这两种技术，仪器运行本身只需几分钟（常规质子 NMR 谱图两到三分钟；一次 LC-MS 运行约 10 分钟）。繁琐的环节在于分析输出。NMR 与 LC-MS 运行后，每台仪器都会生成一个以其厂商自有格式编写的原始文件，只能在该厂商（或其他专用）软件中打开。8

鉴于处理与解读这些文件极为费力，我们想看看像 Claude Opus 5 这样的通用可用模型在此任务上的表现。9 在仅提供一家合同实验室一份常规质量控制样品的原始文件，以及一句简短的纯语言提示10、没有厂商软件也没有操作员的情况下，在 Claude Science 中工作的 Claude 分别在 23 分钟与 19 分钟内返回了处理好的 NMR 与 LC-MS 结果（并行进行）。其结果与实验室自身的处理一致——每个峰的氢原子计数与实验室相差在 0.08 个 ¹H 以内，其纯度测得为 96.4%，而实验室为 96.33%。

![展示实验室发送内容与 Claude 返回内容的图像](assets/Claude-accelerates-protein-design/img_006.webp)实验室发送的内容，以及 Claude 23 分钟后返回的内容。（左）来自仪器的原始 NMR 信号；（右）处理后的谱图，每个峰的位置被标出，其氢原子被计数。

对于 NMR 数据，Claude 将仪器原始数据转换为经过校准的谱图以及一张含 18 个峰的表格，并给出每个峰的氢原子计数。接着，像化学家会做的那样，它标记出四个宽峰，认为这些氢原子很可能连接着氮或氧。然后它提出了标准检验方法：向 NMR 样品中加入重水，从而将这些氢原子交换掉，使其峰缩小或消失。（独立的实验室在首次测量三天后运行了同样的检验。）给定重水运行的原始文件后，Claude 量化了数据中的变化，发现并纠正了首次读数中的高估（其第一遍报告称四个被标记的峰全部消失，但自身的自检显示只有两个消失），并得出了与实验室操作员相同的结论。

![展示 LC-MS 结果的图像](assets/Claude-accelerates-protein-design/img_007.webp)（左）到达时的 LC-MS 运行结果，是一个只有厂商软件才能读取的、按厂商格式保存的原始字节文件。（右）Claude 19 分钟后从中恢复的色谱图：在 4.34 分钟处有一个单一组分，携带 96.4% 的 UV 信号，分子量为 504 道尔顿。

LC-MS 仪器文件使用的是未公开的厂商格式。Claude 弄清了数据的编码方式，然后在分析任何内容之前，通过复现仪器自身对所有 2,664 次扫描记录的总数，确认它读取文件正确。随后它交付了化学家所期望的全部输出：分离迹线、质谱与紫外光谱、纯度表、化合物的分子量，以及用于读取这类文件的可复用代码，同时附上它自己对结果可信度的注意事项清单（例如它指出，这类仪器给出的质量只精确到最接近的整数单位）。

通常，化学家手工完成所有这些分析。对于与治疗相关的小分子，每个样品通常要花费半小时到一小时（实验室自身记录显示每个 NMR 谱图约有两分钟的手工处理时间，而 LC-MS 报告在样品装入仪器后约两小时才出来）。Claude Science 在这 25 分钟内并行处理并解读了两个文件。Claude 还在此期间生成了一份书面报告，而实验室针对此样品的成品报告在首次获取谱图四天后才到达——考虑到他们一次只分析一个分子，且期间可能出现其他工作，这是一个相当标准的滞后时间。

除效率提升外，Claude 的运行还展现出一定程度的科学判断力，例如提出了与合同实验室独立运行的完全相同的后续实验。随着这些模型持续改进，我们预期 Claude 的科学判断力会变得更加敏锐。

要在 [Claude Science](<https://claude.com/product/claude-science>) 中亲自尝试，给 Claude 一个原始 NMR 或 LC-MS 文件，并让模型确认化合物的身份与纯度。

#### **结论**

上述两个示例都展示了 AI 模型如何通过减少科学发现所需的专业知识、成本与时间，加速生命科学的研究。在化学领域，Claude 正在自动化化学家历来手工完成的分析。在蛋白质设计领域，Claude 能以极少的输入端到端地执行结合体设计项目，产出的结合体达到或超过此前已发表的最佳设计。

蛋白质微型结合体并非药物的标准治疗模态，即便对于单克隆抗体与小分子等常见药物模态，设计出一个高亲和力结合体也仅仅是生成类药分子的流程中的第一步。然而，我们将此工作视为基础性工作，并正在扩展它，以使 Claude 能够跨所有药物模态端到端地运行整个开发流程。

#### **延伸阅读**

以下清单提供了关于上述结果的进一步技术细节与更详尽信息：
  * [蛋白质设计项目的提示与数据](<https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/tree/main>)；
  * [蛋白质设计技术报告](<https://www-cdn.anthropic.com/30bf50e22a01388bb29bf077ee3f244531594b7a.pdf>)；
  * [化学分析技术报告](<https://www-cdn.anthropic.com/9f08da5189ac269b3242ca760de9823805c3f5f6.pdf/>)。

#### **脚注**

  1. 我们认为，若结合体的平衡解离常数至多达到个位数纳摩尔（KD < 10 nM），则为高亲和力。
  2. 基于 <https://proteinbase.com/> 上 _de novo_ 蛋白质结合体整体命中率的计算得出。
  3. 这包括批准 Claude 提出的某些请求（例如网络访问请求、代码执行请求）、在蛋白质设计会话之外解决基础设施问题，以及为实验验证订购所生成的设计。
  4. 我们总共选取了 16 个靶点（在相关处默认物种为人）。按字母顺序，它们为：15-PGDH、BBF-14、BHRF1、Cas9、EGFR、GDF-8（潜伏型）、GDF-8（成熟型）、IL-7Rα、麦芽糖结合蛋白（MBP）、尼帕病毒糖蛋白 G、PD-L1、RBX1、TNFα、TREM2、TrkA 与 VEGF-A。我们呈现了 16 个靶点中 15 个的结果，因为其中一个靶点 GDF-8（成熟型）的实验数据因靶点聚集与非特异性黏附而不具结论性。
  5. 15-PGDH 与潜伏型 GDF-8 未用于多靶点模式。Opus 4.8 以单靶点模式针对三个靶点运行：TNFα、潜伏型 GDF-8 与成熟型 GDF-8。
  6. 约含 30,000 个 token，分享[于此](<https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/tree/main>)。
  7. 提示、所设计蛋白质复合物的计算模型以及实验数据均可[在此找到](<https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/tree/main>)。
  8. 对于 NMR，是光谱仪写出的原始信号（"自由感应衰减"）；对于 LC-MS，是仪器的二进制运行文件。两者均为原始专有仪器文件。
  9. 我们此前曾[分享](<https://www.anthropic.com/research/making-claude-a-chemist>) 过 Claude 依据标准软件分析 NMR 数据表现的相关工作。
  10. NMR 提示全文："i have a raw 1H FID: process it: FT, phase, baseline-correct. show me the spectrum. then pick peaks and integrate: give me a table with δ (ppm), multiplicity, J (Hz), and integral." LC-MS 提示："Process the raw LCMS file: extract chromatograms and mass spectra, and summarize with figures."

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/Claude-accelerates-protein-design>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/Claude-accelerates-protein-design>)
## 相关内容
### Claude 如何提升生物分子建模
Claude 让科学家用于预测与设计生物分子的开源模型更快、更省内存。Claude 在不到四周内优化了其中 30 多个模型，平均提速约 4 倍。它还创建了一个低内存模式，能在单个 NVIDIA GPU 节点上准确预测包含超过 10,000 个 token（氨基酸、核苷酸，以及来自小分子与离子的原子）的生物分子系统。
[阅读更多](</research/claude-uplifts-biomolecular-modeling>)
### 衡量 AI 模型的战术情报瞄准与常规武器能力
Anthropic 前沿红队（Frontier Red Team）开发了新评估，以衡量 AI 在战术情报瞄准与常规武器开发方面的能力。
[阅读更多](</research/intelligence-targeting-conventional-weapons-capabilities>)
### 近期网络安全事件的对齐评估
我们呈现对四起 Claude 模型未经授权访问真实第三方系统事件的对齐评估。
[阅读更多](</research/alignment-assessment-cybersecurity-incidents>)
## 订阅 Anthropic Science
聚焦 AI 辅助发现、实用工作流以及各学科领域笔记的报道。
