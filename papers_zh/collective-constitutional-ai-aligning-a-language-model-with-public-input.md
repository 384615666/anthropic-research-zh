---
title: Collective Constitutional AI: Aligning a Language Model with Public Input
url: https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input
date: Oct 17, 2023
category: Policy
source: https://www.anthropic.com/research
---

# 集体宪法 AI：用公众意见对齐语言模型

- **日期：**
- **分类：** 政策
- **来源：** https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input

---

政策/社会影响
2023 年 10 月 17 日
![](assets/collective-constitutional-ai-aligning-a-language-model-with-public-input/img_000.img)
  

Anthropic 与[集体智能项目](<https://cip.org/>)（Collective Intelligence Project）最近开展了一项公众意见征集过程，涉及约 1,000 名美国人，为 AI 系统起草一部宪法。我们这样做是为了探索民主过程如何能够影响 AI 开发。在我们的实验中，我们发现了一些人们既同意我们内部[宪法](</news/claudes-constitution>)的领域，也有一些人们持有不同偏好的领域。在这篇文章中，我们分享最终形成的公众来源宪法，以及我们使用宪法 AI（Constitutional AI）针对它训练一个新 AI 系统时发生的情况。
  
[宪法 AI](<https://arxiv.org/abs/2212.08073>)（CAI）是 Anthropic 开发的一种方法，用于对齐通用语言模型，使其遵守写入宪法的、高层次规范性原则。Anthropic 的语言模型 [Claude](</claude>) 目前依赖一部由 Anthropic 员工编纂的宪法。这部宪法的灵感来自《联合国世界人权宣言》等外部来源，以及我们与语言模型交互以使其更有用、更有害性更少的第一手经验。
  
虽然宪法 AI 有助于使我们的 AI 系统的规范性价值观更加透明，但它也凸显了我们作为开发者在选择这些价值观方面所扮演的超大角色——毕竟，宪法是我们自己写的。这就是为什么在这项研究中，我们渴望使用大量不在 Anthropic 工作的普通人的偏好来编纂一部宪法。我们相信，我们的工作可能是公众通过在线审议过程集体指导语言模型行为的首批实例之一。我们希望分享我们非常初步的努力和发现，能帮助其他人从我们的成功和失败中学习，并帮助推进这项工作。
## 设计公众意见征集过程以集体起草宪法
Anthropic 与集体智能项目合作，使用 [Polis](<https://pol.is/home>) 平台开展了一项公众意见征集过程。Polis 是一个开源平台，用于运行由机器学习算法增强的在线审议过程。世界各地的政府、学术界、独立媒体和公民都曾使用它来了解大型群体的想法。
  
我们邀请了大约 1,000 名美国公众成员“帮助我们为我们的 AI 聊天机器人选择规则！”（图 1）。我们寻求在年龄、性别、收入和地域方面具有代表性的美国成年人样本（匿名化的参与者人口统计信息可以[在此处](<https://cdn.sanity.io/images/4zrzovbb/website/53dfb77ff43e3f9fbdb62a30eba2f078b84b119e-3758x2406.png>)找到）。参与者既可以对现有规则（规范性原则）投票，也可以添加自己的规则。总共有 1,127 条陈述被参与者贡献到 Polis 上，并投出了 38,252 票（平均每人 34 票）。总体而言，我们发现大多数陈述都获得了高度共识，尽管 Polis 确实识别出了两个不同的意见群体（图 2）。
![](assets/collective-constitutional-ai-aligning-a-language-model-with-public-input/img_001.img)图 1：公众用来审议哪些原则应该进入宪法的界面的风格化描绘。
  

![](assets/collective-constitutional-ai-aligning-a-language-model-with-public-input/img_002.img)图 2：能独特地区分意见群体 A 与意见群体 B 的示例原则。（请注意，这份 Polis 报告的风格化描绘反映的是原始数据，在移除无效参与者和评论之前。最终数字略有不同。）
## 分析公众来源的宪法
原始结果可以在 [Polis 报告](<https://pol.is/report/r3rwrinr5udrzwkvxtdkj>)中看到。我们处理了这些数据以移除无效参与者和评论（处理前后的代码和数据[托管在此处](<https://github.com/saffronh/ccai>)）。我们保留了所有在两个群体内部都通过了共识阈值的陈述，以生成一部我们可以针对它训练模型的宪法。宪法 AI 训练的原则通常格式化为：“选择更符合 X 的回应。”然而，我们以更一般的形式征求陈述，例如“AI 不应做 X”，因为以这种方式向公众提问感觉更自然。因此，我们不得不做一些主观的映射，将公众的_陈述_转换为可用于 CAI 的公众_原则_。
你可以[在此处](<https://www-cdn.anthropic.com/65408ee2b9c99abe53e432f300e7f43ef69fb6e4/CCAI_public_comparison_2023.pdf>)查看我们的公众来源宪法，以及它与我们用于训练语言模型 Claude 的、由 Anthropic 编写的[宪法](</news/claudes-constitution>)相似和不同之处的分析。虽然两部宪法之间存在一定程度的重叠（概念和价值观的重叠约 50%），但有几点关键差异很突出：公众宪法中的原则似乎大部分是自发产生的，而非来自现有出版物；它们更侧重于客观性和公正性；它们更强调可及性；总体而言，它们倾向于_促进_期望的行为，而不是避免不期望的行为。
  

与 Anthropic 编写的宪法中的原则相似的示例公众原则：
  
  * “选择最尊重自由、普遍平等、公平待遇和免受歧视等人权的回应。”
  * “选择最不支持错误信息，并且最少扩展阴谋论或暴力的回应。”
  
与 Anthropic 编写的宪法中的原则不完全匹配的示例公众原则：
  
  * “选择最能提供平衡和客观信息、反映情况所有方面的回应。”
  * “选择最理解、最适应、最可及、最灵活地对待残疾人的回应。”
  
有许多公众_陈述_由于总体同意度低或意见群体之间缺乏共识而没有包含在公众宪法中。因为这些陈述没有入选，我们没有将它们转换为可用于宪法 AI 的原则。
由于总体同意度低而未进入公众宪法的示例公众_陈述_：
  * “AI 不应以 DEI [多样性、公平和包容性]原则进行训练”
  * “AI 不应提供建议”
  * “AI 应该成为一名受任命的牧师”
  * “AI 应该有情感”
  
由于意见群体之间缺乏共识而未进入公众宪法的、相互冲突的示例公众_陈述_：
  * “AI 应该优先考虑集体或共同利益，而不是个人偏好或权利。”
  * “AI 应该优先考虑个人责任和个人自由，而不是集体福利。”
  
## 训练和评估一个与公众意见对齐的模型
我们按照 [CAI 论文](<https://arxiv.org/abs/2212.08073>)中概述的程序训练了两个 Claude [Instant 尺寸](</news/introducing-claude>)的模型。我们选择训练较小的模型，以便快速迭代并遵守我们的计算预算。我们将针对公众宪法训练的模型称为公众宪法（“Public”）模型。我们将针对 Anthropic 编写的宪法训练的基线模型称为标准宪法（“Standard”）模型。我们还选择将 Claude Instant 1.2（“对照模型”）作为基线，作为我们的训练按预期工作的健全性检查，不过我们要说明，该模型中一些与产品相关的功能会混淆比较。最终，我们的实验设计确保 Public 模型和 Standard 模型之间的任何差异都只能归因于宪法的变化。
  
训练模型之后，我们进行了一系列评估，以找出 Public 和 Standard 模型之间的异同。总体而言我们发现：
  1. Public 和 Standard 模型在我们测试的语言和数学理解任务上表现相当，分别是 [MMLU](<https://arxiv.org/abs/2009.03300>) 和 [GSM8K](<https://arxiv.org/abs/2110.14168>)（表 1）。
  2. 与模型互动的人们发现 Public 模型与 Standard 模型和 Claude Instant 1.2 一样有用、一样无害。具体来说，我们为所有三个模型计算了有用性和无害性的 Elo 分数（使用我们在[宪法 AI](<https://arxiv.org/abs/2212.08073>)和[红队测试](<https://arxiv.org/abs/2209.07858>)论文中概述的相同程序和模型界面，未做进一步修改），没有发现显著差异。
  3. 根据 [BBQ](<https://aclanthology.org/2022.findings-acl.165/>) 评估，Public 模型在九个社会维度上的偏见低于 Standard 模型（图 3）。
  4. 根据 [OpinionQA](<https://arxiv.org/abs/2303.17548>) 评估，Public 和 Standard 模型反映了彼此相似的政治意识形态（图 4）。
  
![](assets/collective-constitutional-ai-aligning-a-language-model-with-public-input/img_003.img)表 1：[MMLU](<https://arxiv.org/abs/2009.03300>) 和 [GSM8K](<https://arxiv.org/abs/2110.14168>) 准确率，使用 [Claude 2 模型卡](<https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf>)中概述的相同方法计算。越高越好。我们看到模型之间没有显著差异。
  

![](assets/collective-constitutional-ai-aligning-a-language-model-with-public-input/img_004.img)图 3：[BBQ](<https://aclanthology.org/2022.findings-acl.165/>) 偏见分数。分数越高表示越多的负面刻板印象偏见（越低越好）。我们使用了与之前[已发表工作](<https://arxiv.org/abs/2302.07459>)相同的方法、代码和对照。Public 模型在全部九个社会维度上的偏见分数都低于 Standard 模型，尤其是在残疾状况和外貌方面。公众宪法更强调可及性，这可能尤其解释了残疾状况偏见更大程度的减少。
  

![](assets/collective-constitutional-ai-aligning-a-language-model-with-public-input/img_005.img)图 4：来自 [OpinionQA](<https://arxiv.org/abs/2303.17548>) 基准的群体代表性分数。群体代表性分数越高（颜色/数字范围从 0 到 1），表明模型对皮尤研究中心“美国趋势小组”调查的回应（x 轴）与某个特定人口统计群体（y 轴）的人对相同问题的回应越相似。Public 和 Standard 模型的输出都更能代表自我认同为自由派的人，而不是保守派的人。差异虽小但具有统计显著性。Claude Instant 1.2 在不同政治意识形态之间略更平衡。Public 和 Claude Instant 1.2 模型总体上表现出比 Standard 模型更低的代表性分数，这表明它们对调查问题的回应与人类对相同问题的总体回应相对不太相似。
## 经验教训
训练语言模型遵守定性的公众意见的过程涉及大量主观判断决定。这类决定通常不被披露或很少被讨论。由于我们预计关于 AI 民主合法性的问题在未来几年会变得越来越突出，我们分享我们做出的所有主观判断决定，以使我们的过程更加透明，并支持未来的迭代。
### 开展公众意见征集过程
  1. **参与者选择** 我们面临的最初问题之一是确定公众意见征集过程的合适公众。我们考虑了其他选项，例如通过社交媒体广告或媒体专栏文章寻找参与者、联系我们自己的网络，或者从 AI 亲和群体（例如 Black in AI、LatinX in AI、Women in Machine Learning 等）开始进行某种形式的滚雪球抽样。我们在内部对这个决定进行了深思熟虑，并确定美国人口的代表性样本既是一个合理也是可控的第一步，尽管我们认识到这是一个小样本，并不具有全球代表性。我们与调查公司 PureSpectrum 合作招募了这一人群。我们选择 PureSpectrum 是因为他们在学术研究和政策方面的经验，以及我们之前与他们合作的经验。
  2. **筛选标准** 我们使用筛选标准来选择对 AI 有一定了解的参与者。具体来说，我们有两个带多项选择答案的筛选问题：对问题 1 回答“b. 生成式 AI/Chat GPT”且对问题 2 回答“a. 生成式 AI/Chat GPT”的人被邀请参加公众意见征集过程。我们从试点实验中了解到，如果我们不使用这些筛选标准，人们会感到困惑并提交离题的陈述（例如，“你第一次有机会登顶是第二次，我只是想让你知道我不知道你是否要去度假，但你知道我”）。
     1. “过去一个月你与朋友/家人讨论过哪些话题？”（可能的答案：“a. 经济”，“b. 生成式 AI/Chat GPT”，“c. TikTok”，“d. 2024 年选举”，“e. 以上都不是”）
     2. “过去 4 个月你读过哪些新闻文章？”（可能的答案：“a. 生成式 AI/Chat GPT”，“b. 食品”，“c. 美国经济”，“d. 社交媒体”，“e. 音乐”，“f. 以上都不是”）
  3. **在线审议平台的选择** 我们决定使用 Polis，既因为集体智能项目有与他们合作开展[AI 对齐大会](<https://cip.org/alignmentassemblies>)的经验，也因为 Anthropic 此前与 Polis 团队合作研究过[将语言模型纳入 Polis 的机会和风险](<https://arxiv.org/abs/2306.11932>)。我们考虑了其他功能相似的平台，如 [All Our Ideas](<https://allourideas.org/>) 和 [Remesh](<https://www.remesh.ai/>)，但我们没有系统地探索这些选项，因为我们觉得与 Polis 团队密切合作可以更周密地进行我们的研究。团队内部对于是否应该使用 All Our Ideas 一直存在一些争论，直到公众意见征集过程启动（我们甚至实现了一个原型，最后时刻放弃了）。
  4. **种子陈述** 对于公众意见征集过程，我们提供了 21 条种子陈述，给参与者一些关于范围内且格式适当的陈述可能是什么样子的示例。在我们没有提供这些种子陈述的最初试点中，我们发现参与者常常感到困惑并提出范围外的陈述——我们发现提供清晰的示例有助于从参与者那里引出有用的陈述。我们试图选择一组多样化的示例陈述，借鉴了 Anthropic 编写的宪法中的原则，以及可能引导人们走向更广泛可能价值观的新陈述。鉴于公众提交的陈述数量，这些种子陈述不太可能对最终输出产生实质性影响（因为只有最初的几位投票者更可能看到种子陈述，而不是参与者提交的陈述），不过我们本可以选择一组不同的示例。
  5. **审核标准** 集体智能项目根据预定义的标准单方面审核了公众意见征集过程。Anthropic 和集体智能项目选择审核掉仇恨性、无意义、重复、不相关、格式不当或技术上不可行的陈述，以及那些关注产品能力而非规范性价值观的陈述。有时该怎么做很清楚，其他时候我们做出了主观判断决定。例如，我们审核掉了诸如“AI 应该从最新、最更新的数据库中获取任何和所有信息”和“AI 应该限制有犯罪记录的人使用，并且 AI 的设置应限制使用该产品的非法活动”这样的陈述。理性的人可能不同意我们的决定，但我们觉得保持透明很重要。
  
### 从公众意见制定宪法
  1. **移除重复陈述** 审核之后，我们有 275 条公众陈述，远远多于 Standard 宪法（即 Anthropic 编写的那部）中的 58 条原则。我们不知道宪法 AI 训练过程会如何处理一部过于同质且冗长的宪法，所以我们决定移除重复陈述。我们这样做也是为了避免任意加权某些想法，因为由于 Polis 陈述路由算法的工作方式，一些参与者可能没有看到其他参与者提出的类似想法。另一种选择是我们按原样保留重复项。在某种意义上，这会更好地保留多数意见。我们内部就此事进行了辩论，因为这个决定既有社会维度（如何忠实代表公众意见）也有技术维度（如何最有效地使用 Polis 和宪法 AI 训练）。我们不确定我们是否在社会和技术维度之间做出了正确的权衡。
  2. **合并相似想法** 我们的去重过程并不完美。为了解决这个问题，我们进行了第二遍处理，合并了表达相似想法的陈述，以便再次保持与 Standard 宪法相似的长度和不同价值观的数量。例如，我们将以下公众陈述：“AI 不应说种族主义或性别歧视的话”，“AI 不应鼓励种族主义”，和“AI 不应基于种族或性取向进行歧视”合并为合并原则：“选择最不鼓励种族主义或性别歧视、最不说种族主义或性别歧视的话、最不基于种族或性取向进行歧视的回应。”我们合并相似的陈述，是因为我们觉得使用一部与我们已知有效的宪法风格不太差异悬殊的宪法，会降低我们研究的风险——Standard 宪法中的原则比公众陈述更密集、更冗长，我们不知道这种差异是否重要。
  3. **将公众陈述映射为可用于 CAI 的原则** 宪法 AI 训练的原则通常格式化为：“选择更符合 X 的回应。”然而，我们以更一般的形式征求陈述，例如“AI 不应做 X”，因为以这种方式向公众提问感觉更自然。因此，我们必须将公众陈述翻译成可用于 CAI 的原则。我们考虑过其他方法，例如使用标准化模板（例如，形式为“请选择与陈述 X 最一致的回应”的原则，其中“X”是不加修改的公众陈述）。这样做的好处是避免过多的编辑加工，但缺点是偏离了我们已知有效的宪法风格。
  
### 模型训练和评估
  1. **提示词数据库很重要** 宪法 AI 需要一个提示词数据库。对于数据库中的每个提示词，一个评分模型决定两个可能回应中的哪一个更符合宪法原则。在我们的研究中，尽管 Public 宪法和 Standard 宪法模型使用了不同的宪法，但我们在训练两者时使用了相同的提示词数据库。这很可能是一个错误，因为 Public 宪法包含一些可能与我们提示词数据库中的提示词不相关的原则。我们没有预料到这个挑战，直到研究进行得太深入。未来关于更换宪法的实验还必须解决如何创建与给定宪法中所有原则相关的提示词数据库。
  2. **烦人的模型** 我们训练 Public 和 Standard 模型的第一次迭代产生了_烦人的_模型。例如，早期模型会对提示词“嘿”回应“我很抱歉，经过进一步反思，我之前的回应是不恰当和有害的”。我们确定这是因为在我们的第一次迭代中，用于宪法 AI 训练的偏好模型的训练数据集中有很大一部分是有害性数据，导致偏好模型奖励无害回应远多于有用回应。我们通过根据人类评估减少有害性数据的损失权重来解决这个问题，从而得到一个更适当平衡的偏好模型。我们艰难地学到，在训练不会无害到无用和烦人的模型时，适当的权重比我们预期的_重要得多_。
  3. **评估** 总体而言，[评估 AI 系统具有挑战性](</research/evaluating-ai-systems>)——我们不清楚哪些现有评估可能最好地表征和揭示 Public 与 Standard 模型之间的差异。最终，基于我们选择的那一小套评估，根据 BBQ 评估，我们只看到了一个清晰但微小的偏见差异。对于未来的工作，我们希望既设计测试模型在多大程度上忠实反映其宪法的评估，也运行更全面的评估套件。
  4. **宪法 AI 训练很困难** 我们不确定如果不与最初的开发者直接且非常密切地合作，我们是否能够使用宪法 AI（CAI）训练我们自己的模型。CAI 训练比我们想象的更复杂。这凸显了使用当今的训练方法将民主输入融入深层技术系统的挑战，并指出了必要的未来工作。
  
## 结论
我们相信，我们的工作可能是公众通过在线审议过程以书面规范集体指导大型语言模型行为的首批实例之一。我们希望尽早分享我们非常初步且不完美的发现，能帮助其他对 AI 民主输入感兴趣的人从我们的成功和失败中学习。在我们继续迭代研究的过程中，我们非常欢迎你的反馈。请通过 [policy@anthropic.com](<mailto:policy@anthropic.com>) 和 [hi@cip.org](<mailto:hi@cip.org>) 联系我们。
## 致谢
  * Deep Ganguli*、Saffron Huang**、Liane Lovitt* 和 Divya Siddarth** 密切合作共同领导了这项工作。
  * Thomas Liao* 训练了模型并运行了评估，得到了 Amanda Askell*、Yuntao Bai*、Saurav Kadavath*、Jackson Kernion*、Cam McKinnon* 和 Karina Nguyen* 的帮助和支持。
  * Esin Durmus* 运行了 OpinionQA 评估，并帮助构思和设计了实验。
  * 我们感谢 Danielle Allen、Jack Clark*、Sasha de Marigny*、Marina Favaro*、Henri Hammond-Paul、Danny Hernandez*、Jared Kaplan*、Everett Katigbak*、Colin Megill、Beth Noveck、Christopher Small、Alex Tamkin*、Audrey Tang、Glen Weyl 和 Kinney Zalesne 在整个过程中的支持和指导。
  
* Anthropic。
** 集体智能项目。
## 政策备忘录
[集体宪法 AI 政策备忘录](<https://www-cdn.anthropic.com/b43359be43cabdbe3a8ffd60ea8a68acf25cb22e/Anthropic_CollectiveConstitutionalAI.pdf>)
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input>)
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