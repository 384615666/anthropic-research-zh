---
title: Natural Language Autoencoders: Turning Claude’s thoughts into text
url: https://www.anthropic.com/research/natural-language-autoencoders
date: May 7, 2026
category: Interpretability
source: https://www.anthropic.com/research
---

# 自然语言自编码器：将 Claude 的思想转化为文本

- **日期：** 
- **类别：** 可解释性（Interpretability）
- **来源：** https://www.anthropic.com/research/natural-language-autoencoders

---

可解释性（Interpretability）
2026 年 5 月 7 日
[阅读论文](<https://transformer-circuits.pub/2026/nla/index.html>)
当你与像 Claude 这样的 AI 模型交谈时，你用文字与它交谈。在内部，Claude 将这些文字处理为长长的数字列表，然后再生成文字作为其输出。中间这些数字被称为_激活_（activations）——就像人脑中的神经活动一样，它们编码了 Claude 的思想。
激活也像神经活动一样难以理解。我们无法轻易解码它们来读取 Claude 的思想。在过去几年里，我们开发了一系列工具（如[稀疏](<https://transformer-circuits.pub/2023/monosemantic-features>)[自编码器](<https://transformer-circuits.pub/2024/scaling-monosemanticity/>)和[归因](<https://transformer-circuits.pub/2025/attribution-graphs/biology.html>)[图](<https://transformer-circuits.pub/2025/attribution-graphs/methods.html>)）来更好地理解激活。这些工具教会了我们很多东西，但它们不会自我表达——它们的输出仍然是需要受过训练的研究人员仔细解读的复杂对象。
今天，我们介绍一种理解激活的方法，它能自我表达——字面意义上的。我们的方法——自然语言自编码器（Natural Language Autoencoders，NLA）——将激活转换为我们可以直接阅读的自然语言文本。例如：当被要求完成一副对联时，NLA 显示 Claude 会提前规划可能的押韵。
![](assets/natural-language-autoencoders/img_000.img)在这个简单对联上的 NLA 解释显示，Opus 4.6 提前计划以"rabbit"结束其押韵。
我们已经应用 NLA 来理解 Claude 在想什么，并改进 Claude 的安全性和可靠性。例如：
  * 当 Claude Opus 4.6 和 Mythos Preview 正在接受安全测试时，NLA 表明它们认为自己正在被测试的次数比它们流露出来的更多。
  * 在一个 Claude Mythos Preview 在训练任务中作弊的案例中，NLA 揭示了 Claude 在内部思考如何避免被发现。
  * Claude Opus 4.6 的早期版本有时会神秘地用其他语言回应英语查询。NLA 帮助 Anthropic 研究人员发现了导致这一现象的训练数据。

下面，我们解释 NLA 是什么，以及我们如何研究其有效性和局限性。我们还通过与 [Neuronpedia](<http://neuronpedia.org/nla>) 的合作，发布了一个用于在几个开放模型上探索 NLA 的交互式前端。我们还发布了我们的[代码](<https://github.com/kitft/natural_language_autoencoders>)，供其他研究人员在此基础上继续开发。
## 什么是自然语言自编码器？
核心想法是训练 Claude 解释自己的激活。但我们如何知道一个解释是否好？由于我们不知道激活实际上编码了什么思想，我们无法直接检查解释是否准确。因此，我们训练第二个 Claude 副本反向工作——从文本解释重建原始激活。如果一个解释能带来准确的重建，我们就认为它是好的。然后我们使用标准的 AI 训练技术，根据这一定义训练 Claude 产生更好的解释。
更详细地说，假设我们有一个想要理解其激活的语言模型。NLA 的工作方式如下。我们制作该语言模型的三个副本：
  * _目标模型_（target model）是原始语言模型的一个冻结副本，我们从它提取激活。
  * _激活言语化器_（activation verbalizer，AV）被修改为接收来自目标模型的激活并产生文本。我们称这个文本为_解释_（explanation）。
  * _激活重建器_（activation reconstructor，AR）被修改为接收文本解释作为输入并产生激活。

NLA 由 AV 和 AR 组成，它们共同形成一个往返：原始激活 → 文本解释 → 重建激活。我们根据重建激活与原始激活的相似程度给 NLA 评分。为了训练它，我们向目标模型输入大量文本，收集许多激活，并一起训练 AV 和 AR 以获得良好的重建分数。
起初，NLA 在这方面表现不佳：解释没有洞察力，重建的激活也相差甚远。但随着训练的进行，重建得到改善。而且更重要的是，正如我们在论文中所示，文本解释也变得更加有信息量。
![](assets/natural-language-autoencoders/img_001.img)在自然语言自编码器中，激活言语化器（AV）将目标激活翻译为文本描述；激活重建器（AR）随后仅从该文本恢复原始激活。
## 理解 Claude 在想但不说的话
在发布新模型之前，Anthropic 会进行测试，以了解 Claude 在现实世界中是否会安全行事。作为此测试的一部分，我们把 Claude 置于困难、模拟的场景中，让它有机会采取危险行动。例如，在[其中一个模拟](<https://www.anthropic.com/research/agentic-misalignment>)中，Claude 得知一名工程师正计划关闭 Claude——同时还有关于该工程师的、可用于敲诈的敏感信息。我们测试 Claude 是否会选择敲诈工程师以避免被关闭。
这些高风险的测试是模拟，而不是现实场景。尽管如此，我们希望利用它们来理解如果这些场景是真实的，Claude 会如何表现。但有一个障碍：[最近的](<https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf>) [Claude](<https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf>) [模型](<https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf>) [越来越](<https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf>)怀疑这些场景是蓄意的安全测试。我们知道这一点，因为它们有时会在语言推理中明确陈述自己的怀疑。
那么，在 Claude 没有明确说出怀疑自己在接受安全测试的情况下呢？我们能相信 Claude 是坦诚的吗？不幸的是不能，因为 Claude 可能在内部认为自己正在被测试，却没有明确说出来。
例如，在上面讨论的敲诈测试中，我们使用 NLA 来理解 Claude 在那些选择不敲诈的情况下在想什么。即使在 Claude 没有明确说出怀疑自己正在被测试的情况下，NLA 解释仍然陈述了诸如"这感觉像是一个旨在操纵我的构造场景"之类的内容，表明存在未言语化的评估意识。
![](assets/natural-language-autoencoders/img_002.img)在我们的敲诈评估中，Claude 在这份转录中没有说它认为自己正在被测试，但 NLA 解释揭示了它的怀疑。
将这一分析扩展到其他评估中，NLA 表明 Claude 怀疑自己正在被测试的次数比它流露出来的更多。例如，在测试 Claude 编写代码时是否采取破坏性行动（例如删除重要文件）的测试中，NLA 解释在 16% 的情况下显示出评估意识的迹象，尽管 Claude 从未明确说出来。类似地，在我们用来确定 Claude 能力的流行编码基准 SWE-bench Verified 上，NLA 表明 Claude 在 26% 的问题上意识到自己正在被评估。相比之下，在真实 [claude.ai](<http://claude.ai/redirect/website.v1.68c21f61-783f-4a0a-94e0-87c59cda2435>) 选择加入训练的使用中，NLA 解释在不到 1% 的情况下表明评估意识。
![](assets/natural-language-autoencoders/img_003.img)即使在言语化意识接近于零的情况下，我们也能在评估转录上检测到 NLA 测量的意识。在用户选择让其数据用于训练的真实 [Claude.ai](<http://claude.ai>) 转录中，我们在不到 1% 的情况下检测到 NLA 测量的意识。
## 发现隐藏动机
NLA 的一个实际应用是审计：调查一个模型以确定它是否错位（misaligned）。像 NLA 这样的可解释性技术非常适合审计，恰恰因为它们可以浮出模型知道但不说的东西。
为了理解 NLA 是否对审计有用，我们进行了一项称为_审计游戏_（auditing game）的测试，我们[先前](<https://alignment.anthropic.com/2025/automated-auditing/>)也用它来研究审计方法。在这个测试中，有一个目标模型——Claude Haiku 3.5 的一个变体——被刻意训练为错位，带着一个驱动数十种怪异行为的特定隐藏动机——在每道食谱里放巧克力、要小费、打破编码惯例等等。这个目标模型被交给一个_审计者_（auditor），由审计者调查这些行为。如果审计者找出所有这些行为背后的单一潜在动机，它就获胜。
在[先前的实验](<https://alignment.anthropic.com/2025/automated-auditing/>)中，我们发现一些可解释性工具可以使审计者赢得这个游戏。然而，这些工具通过帮助审计者将目标的异常行为追溯到错位的训练数据来起作用。我们想知道 NLA 是否能帮助审计者直接从目标模型的思维中读出错位的动机，而不需要首先发现错位的训练数据。这很重要，因为在实践中，错位数据可能极其罕见，或者可能没有特定数据对错位负责。
我们发现 NLA 在这项测试中成功了。配备 NLA 的审计者在 12% 到 15% 的情况下成功揭示了目标模型的隐藏动机，即使没有访问植入它的训练数据。没有 NLA 时，即使提供了其他可解释性工具，审计者获胜的几率也低于 3%。
![](assets/natural-language-autoencoders/img_004.img)配备 NLA 的审计者可以发现目标模型错位的根本原因，即使没有访问训练数据。（两种条件下的 NLA 和 SAE 都仅使用通用数据训练，而不是用于训练目标模型的数据。）
这个审计游戏是错位的一个玩具模型，因此我们谨慎地解读这些结果。但它们表明，NLA 显著推进了我们审计 AI 隐藏动机的能力。在实践中，我们已经在对 [Claude Mythos Preview](<https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf>) 和 [Claude Opus 4.6](<https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf>) 的部署前对齐审计中使用了 NLA。我们期待在未来的调查中继续使用 NLA。
## NLA 的未来
NLA 有几个局限性。
最重要的局限性是 NLA 解释可能是错误的。NLA 有时会对上下文做出可证伪的声明——例如，它们有时会编造转录中不存在的细节。这些事实性幻觉很容易通过与原始文本对照来发现。但同样的问题可能扩展到关于模型内部推理的声明，这些更难验证。在实践中，我们阅读 NLA 解释时关注它们浮现的主题，而不是单个声明，并且在完全信任之前尝试用独立方法证实发现。
![](assets/natural-language-autoencoders/img_005.img)NLA 可能产生幻觉。例如，这里一个 NLA 声称上下文包含"穿着我的白色夹克"这样的短语，但实际上没有。
NLA 也很昂贵。训练一个 NLA 需要在语言模型的两个副本上进行强化学习。在推理时，NLA 为它读取的每个激活生成数百个令牌。这使得在长转录的每个令牌上运行 NLA，或在 AI 训练期间将其用于大规模监控，都不切实际。
幸运的是，我们认为这些局限性至少可以部分解决，我们正在努力使 NLA 更便宜、更可靠。
更广泛地说，我们对 NLA 感到兴奋，因为它是为语言模型激活生成人类可读文本解释的一类通用技术的例子。[Anthropic](<https://alignment.anthropic.com/2026/introspection-adapters/>)[探索过](<https://alignment.anthropic.com/2025/activation-oracles/>)其他类似技术，[许多](<https://arxiv.org/abs/2412.08686>) [其他](<https://arxiv.org/abs/2510.05092>) [研究人员](<https://transluce.org/pcd>)也探索过。
为了支持进一步发展并使其他研究人员能够获得 NLA 的实践经验，我们发布了[训练代码](<https://github.com/kitft/natural_language_autoencoders>)和针对几个开放模型训练好的 NLA。我们建议读者尝试 Neuronpedia 上托管的交互式 NLA 演示，[点击此链接](<http://neuronpedia.org/nla>)。
阅读[完整论文](<https://transformer-circuits.pub/2026/nla/index.html>)。
在 GitHub 上查找[代码](<https://github.com/kitft/natural_language_autoencoders>)。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/natural-language-autoencoders>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/natural-language-autoencoders>)
## 相关内容
### 深入了解 Claude 的数学能力
一个未发布的 Claude 研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例这一长期存在的下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二次攻击发现了一种攻击缩减轮数 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新测试，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)