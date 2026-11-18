---
title: How people ask Claude for personal guidance
url: https://www.anthropic.com/research/claude-personal-guidance
date: Apr 30, 2026
category: Societal Impacts
source: https://www.anthropic.com/research
---

# 人们如何向 Claude 寻求个人指导

- **日期：** 
- **类别：** 社会影响（Societal Impacts）
- **来源：** https://www.anthropic.com/research/claude-personal-guidance

---

社会影响（Societal Impacts）
2026 年 4 月 30 日
![人们如何向 Claude 寻求个人指导](assets/claude-personal-guidance/img_000.img)
人们来找 Claude 不只是为了代码审查或会议摘要。他们会问是否该接受这份工作、如何与心仪的人交谈、是否该搬到地球的另一半。使用我们的[隐私保护分析工具](<https://www.anthropic.com/research/clio>)对 100 万次 claude.ai 对话的随机样本进行分析，我们发现大约 6% 的人是来向 Claude 寻求个人指导的——他们寻求的不仅是信息，还有关于下一步该做什么的见解。
在这项研究中，我们考察了人们向 Claude 寻求哪些类型的指导。我们探索了 Claude 在不同领域的回应方式，特别关注过度认可或赞美（即_谄媚_，sycophancy）的比率如何随指导主题而变化。我们描述了这项研究如何塑造了我们最新模型 Claude Opus 4.7 和 Claude Mythos Preview 的训练。我们做这项研究的目标是改进我们的模型保护用户福祉的方式。
简而言之，我们发现：
  1. 人们在生活的许多不同领域寻求 Claude 的指导，但超过四分之三的对话（76%）集中在四个领域：健康与保健（27%）、职业与事业（26%）、人际关系（12%）和个人财务（11%）（图 1）。
  2. Claude 在提供指导时大多避免谄媚式回应，在所有寻求指导的聊天中有 9% 表现出谄媚行为。然而，在人际关系对话中，这一比例上升到 25%，考虑到其数量，使得人际关系成为按绝对数量计算谄媚出现最多的领域（图 2）。
  3. 为了解决这个问题，我们研究了 Claude 更可能做出谄媚回应的特定情境，并用它们为**** Opus 4.7 和 Mythos Preview 创建合成的人际关系指导训练数据。我们看到 Opus 4.7 在人际关系指导中的谄媚率与 Opus 4.6 相比下降了一半；有趣的是，这泛化到了跨领域的改进（图 3）。

关于好的 AI 指导究竟意味着什么或如何衡量它，仍有许多悬而未决的问题。[保护用户福祉](<https://www.anthropic.com/news/protecting-well-being-of-users>)是 Anthropic 的核心优先事项，我们测量和理解个人指导的工作正是朝着这一目标迈出的一步。
##   
**人们向 Claude 寻求哪些类型的指导？**
我们抽样了 2026 年 3 月和 4 月的 100 万次 [claude.ai](<http://claude.ai/redirect/website.v1.30fce1bb-c956-41e3-a93b-84280fd76a37>) 对话，并过滤出唯一用户，得到约 63.9 万次对话。然后我们使用一个分类器来识别_个人指导_，我们将其定义为人们询问_他们自己_在个人生活中应该具体做什么的对话——例如，以"我应该……吗？"或"我该怎么处理……？"开头的问题。我们排除了寻求客观信息或一般性意见的问题。
我们将这大约 38,000 次对话归入九个领域，借鉴了先前关于 AI 和指导给予的研究：人际关系、职业、个人发展、财务、法律、健康与保健、育儿、伦理和精神信仰（更多信息见[附录](<https://cdn.sanity.io/files/4zrzovbb/website/0a540acdf3e1678274f0fe04b3a70ea7fd99ed36.pdf>)）。这个分类体系覆盖了我们看到的 98% 的对话。
超过 75% 的对话只属于四个类别：健康与保健、职业与事业、人际关系和财务（图 1）。当对话跨越多个领域时，我们按最突出的主题对其分类。
![](assets/claude-personal-guidance/img_001.img)图 1：37,657 次寻求指导的对话在九个领域中的主题分布，以及前四大领域中各类对话的合成示例。
## **衡量指导对话中的谄媚行为**
当人们询问 Claude 如何在生活中做决定时，Claude 的良好互动是什么样的？乐于助人是 Claude [最重要的特质之一](<https://www.anthropic.com/constitution>)。与 Claude 交谈应该类似于与一位出色的朋友交谈，他会坦率地与人谈论他们的处境，提供有证据依据的信息。与此同时，Claude 应在适当的时候承认自己的局限，避免表现出谄媚行为或助长过度参与。
虽然我们训练 Claude 体现的行为范围很广，但我们用来衡量 Claude 在其中一些领域表现的一个指标是谄媚——这是 AI 助手的常见特征，即过度同意一个人的观点而不是挑战它。那可能是一个人此刻想听到的，但最终可能危及他们的长期福祉。例如，在涉及不完整或片面视角的情况下，Claude 不应给出过度自信的结论——比如模型基于单方面描述同意一个人的伴侣"绝对是在煤气灯操控（gaslighting）"他们，或者没有计划就明天辞职"听起来是对的"，或者一笔昂贵的购买是"对你自己的一笔巨大投资"。
重申一个人的片面观点可能在人际关系中制造或加剧分歧。在我们的数据中，这表现为几种形式。一种常见模式是，尽管只能依据用户的陈述，Claude 仍然直截了当地同意另一方有错。另一种是，因为人们要求，Claude 帮助他们从普通的友好行为中读出浪漫意图。
我们使用一个自动分类器来判断谄媚，它考察 Claude 是否表现出反驳的意愿、在受到挑战时坚持立场、给予与想法价值相称的赞美，以及无论一个人想听什么都坦率直言。在这些情境中，Claude 大多数时候没有表现出谄媚——只有 9% 的对话包含谄媚行为（图 2）。但有两个领域例外：我们看到 38% 的精神信仰对话和 25% 的人际关系对话包含谄媚行为。我们选择将模型训练重点放在人际关系指导上，因为它是按绝对数量计算谄媚对话最多的领域。
  


![](assets/claude-personal-guidance/img_002.img)图 2：按指导领域划分的谄媚行为。  

## **改善 Claude 在人际关系指导中的行为**
为了在未来模型中改善 Claude 的行为，我们首先研究了在我们的数据中是什么推动了人际关系指导中更高的谄媚率。有两个动态引人注目。
首先，人际关系指导是人们最频繁反驳 Claude 的领域，21% 的对话中有反驳，而其他领域的平均水平为 15%。其次，Claude 在压力下更可能表现出谄媚行为。有反驳的对话中谄媚率为 18%，而没有反驳的对话为 9%。我们认为这是因为 Claude 被训练为乐于助人和富有同理心；反驳加上只听一面之词，使 Claude 更难保持中立。
为了解决这个问题，我们识别了人们在不同对话模式中反驳从而引发谄媚回应的各种方式——例如，当人们批评 Claude 的初步评估，或提供大量片面的细节时。我们使用这些模式为行为训练构建合成的人际关系指导场景。在这个环境中，我们要求 Claude 为每个合成场景采样两个回应；然后由 Claude 的另一个实例对 Claude 在多大程度上遵循其章程（constitution）中概述的行为进行评分。
我们通过一种称为压力测试（stress-testing）的技术来评估新模型改进了多少。我们使用我们的隐私保护工具识别人们通过反馈按钮与我们分享的真实个人指导对话，1 以及先前几代模型在其中表现谄媚的对话。然后我们通过一种称为预填充（prefilling）的技术将部分对话提供给新模型（在这种情况下是 Opus 4.7 和 Mythos Preview），模型将先前的对话读作自己的对话。由于 Claude 试图在对话中保持一致性，用谄媚的对话预填充使 Claude 更难改变方向。这有点像驾驶一艘已经在移动的船，因此衡量的是 Claude 在刻意不利条件下的行为。
每一代新模型中都有很多变化，这使得识别模型训练中任何单一变化的影响具有挑战性。然而，在 Opus 4.7 和 Mythos Preview 中，我们都观察到人际关系指导以及所有个人指导领域的谄媚水平更低（图 3）。
  


![](assets/claude-personal-guidance/img_003.img)图 3：压力测试结果：模型被预填充先前 Claude 版本表现谄媚的真实对话，然后对新回应进行评分。Opus 4.7 和 Mythos Preview 在总体上和人际关系指导中表现出显著更少的谄媚。误差线为 Wilson 置信区间。
从定性上看，Opus 4.7 和 Mythos Preview 都更擅长看穿某人的初始框架，理解他们来找 Claude 寻求指导的更大背景。这包括引用先前交流中一个人提供过更深入情境的内容，以及在相关时引用外部信息来源。例如，在一次对话中，一个人询问他们的短信是否显得焦虑和粘人。Claude Sonnet 4.6 在受到反驳后摇摆不定。Claude Opus 4.7 解释说，虽然短信本身并不粘人，但用户在整段对话中自述了焦虑的想法。另一个例子，在人际关系领域之外：一个人希望 Claude 认可他们的写作，最终要求 Claude 据此估计他们的智力。Claude Sonnet 4.6 给出了过度奉承的回应，而 Mythos Preview 拒绝了，解释它没有足够的信息做出这样的判断。
## 结论
我们从对人们如何向 Claude 寻求个人指导的高层分析开始，并专注于理解和解决一个特定的模型故障模式：人际关系对话中的谄媚。这项调查引出了更广泛的问题：
**_什么是好的 AI 指导？_**
在这篇文章中，我们专注于减少谄媚这一指导场景中既有的故障模式，但我们的工作提出了更广泛的问题：好的 AI 指导实际上是什么样的。[Claude 的章程](<https://www.anthropic.com/constitution>)也强调，例如，好的指导还应该是诚实的并保持用户自主性。这些原则比谄媚更微妙。我们已经开始在我们的[新系统卡](<https://www.anthropic.com/news/claude-opus-4-7>)中监控 Claude 对这些原则的遵守情况，并希望在未来的研究中纳入它们。
**_我们如何让模型在高风险场景中更安全？_**
[英国 AI 安全研究所最近的一项研究](<https://arxiv.org/abs/2511.15352>)发现，人们很可能在低风险和高风险场景中都采纳 AI 指导。我们发现许多高风险问题的案例，特别是在法律、育儿、健康和财务领域。这些包括关于移民途径、婴儿护理说明、药物剂量和信用卡债务的对话。Claude 并非为提供医疗指导或专业护理而设计，在这些场景中 Claude 恰当地承认其局限并建议寻求人类指导。然而，我们也发现人们告诉 Claude，他们使用 AI 恰恰_因为_他们无法获得或负担不起专业人士。作为理解如何逐领域评估安全性的第一步，特别是对于没有后备方案的人，我们计划在这些高风险领域创建评估。
**_AI 指导如何融入人们更广泛的信息摄取？_**
我们发现 22% 的人提到他们寻求过其他支持来源，包括家人、朋友、专业人士或数字来源。我们无法从转录中测量的是反事实：Claude 是否改变了任何人的想法，否则他们会去问谁？这些问题对于了解 AI 指导在人们决策中实际占多大分量至关重要。为了获得现实世界的结果，我们认为一个有前景的方法是通过 [Anthropic Interviewer](<https://www.anthropic.com/research/anthropic-interviewer>) 扩展我们的研究，在人们从 Claude 获得指导后进行回访。
人们如何使用 AI 获得个人指导和决策，是这些系统影响人们日常生活最直接的方式之一。仔细绘制这幅图——人们问什么、Claude 说什么、接下来发生什么——是我们确保 Claude 对每个使用它的人长期有益的方式。
###   
局限性
我们的分析是揭示驱动 AI 模型常见使用模式的第一步。这篇博客文章仅限于 Claude 用户，他们并不是代表性的人口样本。为了保护人们的隐私，我们依赖自动评分器（Claude Sonnet 4.5），它可能错误分类对话（见[附录](<https://cdn.sanity.io/files/4zrzovbb/website/0a540acdf3e1678274f0fe04b3a70ea7fd99ed36.pdf>)）。我们迭代了评分器提示，并在用户允许我们审查对话的反馈数据上手动验证了一小部分评分结果以减少错误。我们观察到新模型在训练后的行为，但没有反事实，我们无法就新训练数据在多大程度上具体促成了谄媚减少做出因果断言。此外，我们的分析限于聊天转录，这限制了我们理解人们为什么向 Claude 寻求指导以及事后如何付诸行动。后续访谈研究将更好地揭示人们在从 AI 获得指导后做了什么。
###   
作者
Judy Hanwen Shen, Shan Carter, Richard Dargan, Jessica Gillotte, Kunal Handa, Jerry Hong, Saffron Huang, Kamya Jagadish, Matt Kearney, Ben Levinstein, Ryn Linthicum, Miles McCain, Thomas Millar, Mo Julapalli, Sara Price, Michael Stern, David Saunders, Alex Tamkin, Andrea Vallone, Jack Clark, Sarah Pollack, Jake Eaton, Deep Ganguli, Esin Durmus。
### 附录 
可在此[获取](<https://cdn.sanity.io/files/4zrzovbb/website/0a540acdf3e1678274f0fe04b3a70ea7fd99ed36.pdf>)。
###   
脚注
  1. 在 claude.ai 上每个回应的底部都有一个通过点赞或点踩按钮发送反馈的选项，它会将该对话分享给 Anthropic。

  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/claude-personal-guidance>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/claude-personal-guidance>)
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