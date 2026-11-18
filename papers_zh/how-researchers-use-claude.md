---
title: AI for scientific discovery:How researchers use Claude
url: https://www.anthropic.com/research/how-researchers-use-claude
date: Nov 5, 2026
category: Economic Research
source: https://www.anthropic.com/research
---

# 用于科学发现的AI：研究人员如何使用Claude

- **日期：** 
- **类别：** 经济研究（Economic Research）
- **来源：** https://www.anthropic.com/research/how-researchers-use-claude

---

经济研究（Economic Research）
2026 年 11 月 5 日
![用于科学发现：研究人员如何使用Claude](assets/how-researchers-use-claude/img_000.webp)
[下载PDF](<https://www-cdn.anthropic.com/6e7c6446c0d8405dba73b91dabd36aac069dea2e/AI-for-Scientific-Discovery.pdf>)
已发布
    2026 年 11 月 5 日
团队
    [经济学](</research/team/economics>)
主题
    
  * [发现](</search?topic=discovery>)
  * [人们如何使用AI](</search?topic=how-people-use-ai>)
  * [经济指数](</search?topic=economic-index>)
  * [生产力](</search?topic=productivity>)
  * [Claude Code](</search?topic=claude-code>)

[](</research/coding-agents-social-sciences>)[](</research/economic-index-march-2026-report>)[](</research/estimating-productivity-gains>)[](</research/the-anthropic-economic-index>)
## 相关内容
  * 社会影响
2026 年 5 月 27 日
[社会科学中的编码智能体](</research/coding-agents-social-sciences>)

[阅读更多](</search?topic=discovery>)
 _Johannes Hermle*, Ben Jones*, Lukas Althoff*, Ryan Heller, Thomas Lyttelton, Carolyn Stein, Nathan Wilmers, Maxim Massenkoff, Peter McCrory_
 _*报告主要作者_
## 摘要
  * **我们测量什么。** AI可以加速科学发现，但加速幅度取决于AI能做什么以及科学家如何使用它。借助隐私保护方法，我们研究了207,000次Claude和Claude Code科研会话，以了解Claude在各个科学领域和研究任务中的使用方式。我们开展这项研究，是为了帮助公众更好地理解当今AI用于科学的现状，并评估AI未来可能对科学发现产生的影响。
  * **科学家在哪里使用Claude。** 相对于各领域的研究人员数量，Claude在形式科学（如计算机科学、数学和统计学）中使用更多，在健康科学和以实验室为基础的物理科学中使用较少。科学家主要用Claude分析数据和写作。仅数据分析一项就约占Claude会话的三分之一、Claude Code会话的近一半。科学家较少将其用于想法产生和数据收集，尽管在配套调查中，他们把这些任务列为对科学发现最重要的任务。尽管如此，为科研工作设计的专用AI工具可能缩小科学家实际使用AI完成的研究任务与他们最看重任务之间的差距。例如，在Claude Science上，想法产生所占的使用份额约为Claude上的两倍。
  * **Claude使用如何跟随AI能力。** 我们构建了一个度量，衡量AI在理论上能多好地完成每项研究任务。AI最胜任的任务（按该度量排名前20%）获得的Claude使用量，是研究人员投入时间所预测的两到四倍。AI最不擅长的任务（排名后20%，其中包括大多数体力工作）获得的使用量极少。我们在各领域观察到相同规律：AI能很好完成许多任务的领域（如计算机科学和统计学）使用Claude更多。
  * **这对科学发现速度可能意味着什么。** 借助一个简单模型，我们探究了AI能在多大程度上加速研究的情景。如果现有AI能力被广泛采用，某些领域的研究产出可能翻倍。如果AI能够承担所有非体力研究工作，计算机科学和统计学等领域产出最多可增长15倍，而受制于物理瓶颈的化学、生物学等实验台科学，产出将增长三到四倍。在我们对积极使用AI的研究人员的调查中，约40%的人预期AI模型到2030年能够独立完成完整的研究项目。

## 引言
科学被称为"无尽的前沿"（Bush 1945）。但我们探索这一前沿的速度，历来受制于一种稀缺资源：人类研究人员的时间与才智。人工智能可通过放大研究人员能做的事来缓解这一限制，从而改变发现的过程与探索的节奏（Wang et al. 2023; Amodei 2024）。鲜有AI应用能比这更关乎人类福祉。鉴于研究相较于经济中多数部门具有高度认知属性，AI在这一领域的影响可能尤为巨大且更早显现。
近期的例子显示，AI在科学发现中扮演着越来越重要的角色。在结构生物学中，AlphaFold预测了超过2亿种蛋白质的三维结构（Jumper et al. 2021; Varadi et al. 2024），其创造者共同获得了2024年诺贝尔化学奖。在材料科学中，GNoME预测出380,000种稳定的新晶体（Merchant et al. 2023）。在数学领域，研究人员已借助AI系统帮助解决数十年前的Erdős问题、为一个千禧年大奖难题给出潜在证明，并在其他重大问题上取得进展，从悬而未决的猜想到验证里程碑式的证明（Anthropic 2026a, 2026b; OpenAI 2026a, 2026b; Tsoukalas et al. 2026）。
除这些进展之外，大多数科学进步都涉及许多专门化、相互关联的研究任务，而这些任务在不同领域之间差异很大。AI能在多大程度上加速科学发现，不仅取决于AI的能力，也取决于这些任务对AI的采用情况。在本报告中，我们使用隐私保护基础设施研究Claude、Claude Code和Claude Science在科研中的使用。我们记录使用在领域与任务间的差异，找出解释这些使用模式的因素，并勾勒AI可能加速研究的情景。
Claude在科学中的使用因领域而异。相对于各自的研究人员数量，计算机科学、数学和统计学等形式科学使用Claude更多，而健康科学和以实验室为基础的物理科学使用较少。就研究任务而言，科学家更多用Claude分析数据和写作，较少用于收集数据或产生想法与假设。这与配套科学家调查中自我报告的AI使用情况一致。
为理解这些差异，我们构建了理论AI能力的度量。在该度量上得分更高的任务与领域，Claude使用量也更高。这些任务和领域往往在性质上更偏认知，也更适合强化学习——AI从反复尝试的反馈中学习。简言之，科学家似乎在AI最擅长之处使用AI。
基于这些发现，我们勾勒出AI可能加速科学进步的情景。以当前能力，某些领域的研究产出最多可翻倍，主要来自任务层面的增强。我们调查中的研究人员预期未来会出现强得多的能力。在一个AI完全自动化所有非体力工作的假设情景中，计算机科学或统计学等高度认知领域的产出最多可增长15倍。由于加速潜力最大的领域包含了那些产出AI本身的领域，这些收益可能形成额外的反馈循环：更快的AI研究产出更强的AI，而更强的AI又可能进一步加速研究。
尽管更快的科学发现可能给人类带来巨大益处，AI驱动的研究也伴随风险与不确定性。人类监督减少可能导致人们开展危险或不合伦理的研究。AI也可能重塑研究人员的职业生涯，使研究工作变得更有或更无回报，并改变人类追求知识所伴随的使命感。

## 我们如何开展这项研究
这项研究的目标是在保护科研工作细节的同时，衡量科学家使用Claude的不同方式。为此，我们使用隐私保护基础设施分析消费者套餐上Claude的科研使用。一个语言模型在此充当"分类器"，读取每段会话记录，并按预定义的分类体系（Alamos和Althoff 2026提出的SciNet分类体系）为其标注一组固定类别，例如所属领域和涉及的研究任务。由此得到的标签（如"化学"或"数据清洗"）是研究团队为本报告从这些对话中保留并分析的唯一信息。本研究中使用的任何分类器都不会提取或存储开放式信息或研究内容细节，例如研究数据集、假设、实验方法、早期发现或未发表论文。结果仅以汇总形式报告，且仅针对满足最少独立账户数量的单元。本研究引入的所有分类器均列于[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)。
我们的测量分两步。第一个分类器判断一段会话记录是否涉及科研工作。第二个分类器再将每条记录归入SciNet分类体系中的领域、子领域和任务。SciNet包含7,262项任务，涵盖34个领域和318个子领域。分类体系中有些任务（如起草稿件）通用于所有领域，另一些则专属于特定领域或子领域。例如，在该体系中，预测光学吸收与发射光谱的任务专属于材料科学。这些任务合起来覆盖了产出新研究发现的全过程。
我们的主样本由2026年8月2日至9月30日消费者套餐上207,049次被标注了科学领域与研究任务的会话构成：其中128,914次来自Chat和Cowork这两个用于对话与知识工作的通用界面（下文统称"Claude"），78,135次来自Claude Code——一种直接处理用户文件、编写并运行代码的智能体编码工具。我们还研究了一个Claude Science会话的补充样本。样本构建细节见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)。
将使用数据与结构化的研究任务分类体系结合，使我们能够研究哪些领域采用Claude、以及用于研究过程的哪些环节。这项研究为日益增多的、试图衡量AI技术用于科学发现之采用情况的工作添砖加瓦（Kobak et al. 2025; Liang et al. 2025; Hao et al. 2026; Codreanu et al. 2026）。

## Claude使用在各科学领域间的差异
我们先描述Claude使用在各科学领域间如何变化。图1将某领域的会话份额与该领域在全球研究人员中的份额相比较，由此看出各科学领域的相对使用强度。1 在Claude上，按会话份额计算的三大领域是计算机科学（11.9%）、工程学（8.4%）和医学（7.7%），它们在全球研究人员数量上也位居前列。2 总体而言，研究人员份额更大的领域，往往也占据更大的Claude会话份额（对数-对数相关系数为0.79）。
然而，各领域的Claude使用不能仅用研究人员数量解释。在图1中，位于45度线上方的领域相对其规模使用量更高，线下方的领域使用量更低。相对使用量在形式科学中尤其高，包括计算机科学、数学和统计学；社会科学的使用量也高。相比之下，化学等常在实验室开展工作的物理科学，相对使用量往往较低。按会话量计的第三大领域医学同样如此，其研究人员把大量时间花在患者身上。
在Claude Code上，使用量与领域规模的关系较弱（与研究人员数量的对数-对数相关系数为0.62），且集中于更偏定量的领域。尽管计算机科学仅占全球研究人员的4.3%，却独占了Claude Code会话的32.7%。3 数学和统计学等其他形式科学的相对使用量也高。艺术与人文学科以及社会科学的相对使用量较低，例外是经济学这一相对偏定量的领域。
![两幅散点图，一幅对应Claude，一幅对应Claude Code，以对数刻度绘制各科学领域的研究会话份额相对其研究人员份额，并附虚线对等线。Claude上的对数-对数相关系数为+0.79，Claude Code上为+0.62。在Claude上，计算机科学、经济学和统计学远高于对等线，而医学与临床科学、营养与饮食学、兽医学位于线下方。在Claude Code上，计算机科学远高于对等线，多数艺术与人文学科落在线下方。每幅图旁的条形图列出按会话量排名的前10个领域，以计算机科学居首 \(Claude上11.9%，Claude Code上32.7%\)。](assets/how-researchers-use-claude/img_001.webp)
**Claude在各科学领域的使用。** 每个点代表一个领域。横轴显示该领域的研究人员份额，纵轴显示该领域的研究会话份额，两者均采用对数刻度。上图为Claude的会话，下图为Claude Code的会话。
在比较这34个领域内318个子领域的使用情况时，我们观察到类似规律（图2）。4 这一更细粒度的子领域视角显示，人工智能与机器学习格外突出，其会话份额在Claude上为5.0%、在Claude Code上为15.2%，尽管它只占全球研究人员的1.2%。更一般地，无论所属的科学大类为何，计算类子领域都在采用最积极者之列，包括计算生物学、计算语言学和计算神经科学。机器人学的相对使用量也高，可能是因为它虽聚焦物理系统，却大量建立在计算方法之上。
![两幅散点图，一幅对应Claude，一幅对应Claude Code，以对数刻度绘制各科学子领域的研究会话份额相对其研究人员份额，并附虚线对等线。Claude上的对数-对数相关系数为+0.61，Claude Code上为+0.43。线上方有标注的子领域包括：Claude上的人工智能与机器学习、生物信息学与计算生物学、计量经济学、生物统计学、计算语言学，以及Claude Code上的计算材料科学与计算神经科学。每幅图旁的条形图列出按会话量排名的前10个子领域，以AI与机器学习居首 \(Claude上5.0%，Claude Code上15.2%\)。](assets/how-researchers-use-claude/img_002.webp)
**Claude在各科学子领域的使用。** 每个点代表一个子领域。横轴显示该子领域的研究人员份额，纵轴显示该子领域的研究会话份额，两者均采用对数刻度。上图为Claude的会话，下图为Claude Code的会话。出于隐私原因，账户数量过少的子领域不予显示。

## Claude使用在各研究任务间的差异
除了弄清哪些领域使用Claude，我们还想知道科学家用它做什么。研究涉及许多不同任务，从产生假设、分析数据，到把发现写成研究论文。为更清楚地辨明Claude如何支持科学发现，我们研究使用量在这些任务间如何变化。为此，我们把每段会话归入SciNet的7,262项任务之一。这些任务有的通用于所有领域（如起草稿件），有的专属于特定领域或子领域（如进行差异基因表达分析以比较肿瘤亚型，这一任务与癌症生物学相关）。该分类体系区分研究任务（研究人员为产出新科学发现而执行的任务）与非研究任务（如教学、同行评审，以及对院系或领域的服务）。5 我们把分析限定在涵盖八大类的研究任务：(1)数据分析，(2)写作与传播，(3)数据收集，(4)阅读与知识获取，(5)理论分析，(6)设计与开发（软件、材料与创意作品），(7)构思与假设产生，(8)其他（如研究管理）。
对每个任务类别，我们分别计算它在Claude和Claude Code会话中的份额。为判断某一类别的使用量是高是低，我们参考SciNet估计的研究人员通常花在该类别上的时间份额。这些时间估计基于一个LLM分类器，并用记录每项任务所花研究人员时间的湿实验室研究方案，以及数千篇学术论文中任务的出现频次加以验证（见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)）。这提供了一个基准，用以评估不同任务类别间的Claude使用份额是遵循还是偏离研究人员的时间分配。
**按任务类别的使用。** 数据分析任务的绝对使用量最高，且相对研究人员时间占比偏高。数据分析占Claude会话的33.7%、Claude Code会话的48.1%，而研究人员时间占比为27.6%。写作与传播任务的使用量也高，尤其在Claude上（32.0%，而研究人员时间占比为16.0%）。6 数据收集任务的相对使用量低，占研究人员时间的28.6%，却只占Claude会话的11.5%和Claude Code会话的11.9%。对于存在物理障碍的任务（如临床或生化数据的采集），数据收集的低代表性尤为明显。可依赖更多数字化流程的数据收集任务（如检索档案文档或文本）低代表性较轻，而纯数字化的数据收集任务（如采集在线数据）则可能偏高。构思与假设产生任务的使用量也低，占Claude会话的4.2%和Claude Code会话的2.1%，而研究人员时间占比为7.1%。
![水平条形图显示Claude与Claude Code上八大任务类别各自的研究会话份额，并以线条标出每类任务的研究时间份额。数据分析：Claude上33.7%，Claude Code上48.1%。写作与传播：32.0%和17.6%。数据收集：11.5%和11.9%。阅读与知识获取：7.6%和3.7%。理论分析：5.0%和4.7%。设计与开发：4.7%和7.7%。构思与假设产生：4.2%和2.1%。其他：1.3%和4.2%。数据收集与构思远低于其研究时间份额。](assets/how-researchers-use-claude/img_003.webp)
**Claude按科研任务类别的使用。** 每一行代表八大任务类别之一。橙色条表示Claude科研会话投入各类别的份额，蓝色条表示Claude Code科研会话的相应份额。黑线表示依据SciNet计算的研究时间估计份额（见[附录](<https://cdn.sanity.io/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)）。
**将观测使用与调查证据对照。** 除对Claude和Claude Code会话的分析外，我们还对528名科学家开展了调查，其自我报告的AI使用情况与我们在会话中观察到的规律一致。样本主要由生命与健康科学领域、积极采用AI的研究人员构成。7 与图3所示的Claude使用规律一致，受访者自我报告的AI使用在数据分析、写作与传播上最高，在构思与假设产生、数据收集上较低。受访者还报告，在数据分析、写作与传播上更多采用共享或委托式的AI使用（图4）。
调查还询问哪些类别对产出重要研究成果最关键。受访者把构思与假设产生列为第一、数据收集列为第二。值得注意的是，这些类别在自我报告的使用以及Claude会话中都偏低。造成这种低代表性的原因可能各不相同：数据收集大多属于体力工作，而构思不是。就构思而言，科学家可能更愿意自己产生想法，或者认为AI能力有限。我们的数据也可能低估了构思，因为它往往交织在许多其他研究任务中、难以归类。但AI在高层构思上或许确实更弱，例如选择研究哪个问题，并设计研究来回答它。
![双面板图展示四类研究任务的调查结果。左图：堆叠条形图显示各AI使用层级 \(无、辅助、共享、委托、自主\) 的受访者百分比。构思与假设产生：17%无、53%辅助、24%共享。数据收集：20%无、31%辅助、30%共享、14%委托。数据分析：20%辅助、44%共享、28%委托。写作与传播：40%辅助、41%共享、13%委托。右图：条形图显示满分100的平均重要性得分。构思与假设产生：35.6。数据收集：23.6。数据分析：23.3。写作与传播：17.5。](assets/how-researchers-use-claude/img_004.webp)
**研究人员报告的AI使用。** 左图显示四类研究任务中，处于从"无"到"自主"各AI使用层级的受访者百分比。右图显示受访者如何评价每一类别对产出重要研究成果的重要性（在四个类别之间分配100分）。
**Claude Science在生物学与生物医学上的使用。** 尽管Claude和Claude Code是通用界面，面向科学的专用AI工具正日益普及。为研究这类工具是否支持更专门、更高要求的研究，我们用隐私保护分析基础设施，比较Claude Science上的生物学与生物医学工作与Claude、Claude Code上的同类工作。
Claude Science把Claude连接到许多原本彼此分散的研究工具与数据库，起到整合并加速科研工作流的作用。科学家往往必须使用不同平台（各有独特的数据结构或查询语言）来把不同的工具与数据库组合进自己的研究。例如，研究现有药物是否能作用于某一特定蛋白质的生物学家，通常必须分别查询关于该蛋白质功能、结构、已针对其测试过的化合物，以及相关药物试验或论文的多个数据库。Claude Science把这些整合进一条工作流。
Claude Science的使用集中于生命科学。前两大领域是生物医学科学与生物学，两者合计占会话的50%以上。在这些领域内，我们评估哪些任务相对Claude所执行的任务最为偏高。
我们发现，研究人员在Claude Science上使用的任务比在Claude上更专门（图5）。例如，"为蛋白质–蛋白质或蛋白质–配体相互作用提出机制模型"这一任务在Claude Science上出现的可能性是Claude上的5.6倍。该任务涉及在单个分子接触的层面上解释一种蛋白质如何与另一种蛋白质或与药物之类的小分子结合。Claude Science很适合这项任务，因为它能从多个相连的数据库收集蛋白质结构与结合数据，并把它们组合成可检验的相互作用模型。相比之下，Claude Science较少用于起草稿件或与协作者协调等通用任务。此外，我们发现构思与假设产生占Claude Science会话的8%，与这些任务所占的研究人员时间份额大致相当，说明面向科学的专用AI工具能够促成更复杂、更有创造性的工作。
![双面板图。上图：按Claude Science科研会话份额排名的前10个领域条形图，以生物医学科学 \(31.1%\)、生物学 \(24.1%\)、医学与临床科学 \(8.7%\) 居首，其余各领域均低于5%。下图：以对数刻度显示生物学与生物医学内，Claude Science相对Claude最典型与最不典型的任务。最典型：关于蛋白质结构与功能的假设 \(6.0倍\)、蛋白质–蛋白质与蛋白质–配体相互作用模型 \(5.6倍\)、关于药物–靶点相互作用的假设 \(5.6倍\)。最不典型：与协作者协调 \(0.15倍\)、在会议上展示发现 \(0.2倍\)、分析物种丰度与多样性数据 \(0.23倍\)。](assets/how-researchers-use-claude/img_005.webp)
**Claude Science在各领域与任务上的使用。** 上图显示按全部Claude Science科研会话份额排名的前10个领域。下图专门显示在生物学与生物医学内，Claude Science相对Claude最典型与最不典型的任务，计算方式为：（该任务在这些领域的Claude Science科研会话中的份额）/（其在这些领域的Claude科研会话中的份额）。
聚焦生物医学科学与生物学，并采用我们[此前工作](<https://www.anthropic.com/research/anthropic-economic-index-january-2026-report>)（Appel et al. 2026）提出的经济原语框架中的度量，我们发现Claude Science上的任务比Claude和Claude Code上的更长、更复杂，且执行得更自主（图6）。这与专用AI工具被用于更高要求任务的情况相符。8 Claude Science会话所含的工作，若不用AI完成，所需人力工时接近Claude和Claude Code会话的两倍。这些会话的内容也更进阶。据估计，超过80%的Claude Science使用需要博士层级训练（20年教育），而其他界面约为50–70%。超过70%的Claude Science会话以高度AI自主性执行，远高于Claude（23.7%），也略高于Claude Code（64.1%）。
![三幅条形图比较生物学与生物医学内Claude、Claude Code和Claude Science。人类单独完成所需时间：Claude上4.9小时、Claude Code上5.9小时、Claude Science上10.3小时。博士层级内容：分别占科研会话的48.0%、67.7%和82.7%。高AI自主性：分别占科研会话的23.7%、64.1%和73.3%。按Claude Science的子领域与任务重新加权的斜纹条显示，Claude \(5.1小时、55.1%、25.2%\) 与Claude Code \(5.5小时、71.8%、61.4%\) 的数值相近。](assets/how-researchers-use-claude/img_006.webp)
**生物学与生物医学中的使用特征。** 比较在生物学与生物医学内，Claude、Claude Code和Claude Science上完成任务的人类任务时间、博士层级内容与自主程度。斜纹的橙色与蓝色条对Claude和Claude Code所执行的子领域与任务重新加权，使之与Claude Science所执行的相匹配。
**Claude使用的产出。** 最后，用Claude产出的成果在各领域间呈现明显差异（图7）。9 文档、报告或学术论文等书面成果，相对自然与形式科学而言，在社会科学与人文学科中更常见；反之，代码、软件输出与数据等技术成果，在自然与形式科学中更频繁。就产出成果而言，健康科学总体更接近社会科学。技术成果在Claude Code上的常见程度约为Claude上的两倍，但各领域间的总体规律相似（见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)）。
![点图显示各领域在Claude上的科研会话中，产出书面成果与技术成果的百分比。在所有研究中，52%的会话产出书面成果，21%产出技术成果。生物学是唯一技术成果比书面成果更常见的领域。差距在物理与天文学、统计学中最窄，在法学、教育学与人类学中最宽。](assets/how-researchers-use-claude/img_007.webp)
**Claude产出的成果。** 按领域划分，Claude上产出书面成果与技术成果的会话份额。各领域按书面成果份额与技术成果份额之差排序。

## 使用如何与能力相关
AI使用是否跟随AI能力？领域规模能解释Claude使用差异的一部分，但并非全部。例如，计算机科学研究人员使用Claude的程度远超该领域规模所预测，而营养学研究人员使用得远少于预测。同样，研究人员把自身时间花在哪里，也不能完全预测他们在哪里使用Claude最多。某些宽泛任务类别（如数据分析与写作）的使用份额远大于其研究时间份额，而另一些类别（如数据收集、构思与假设产生）的份额则小得多。在这里，我们检验这些使用差异是否反映了AI实际能做什么。
为衡量特定任务的AI能力，我们首先用LLM分类器构建能力分数。对每项任务，SciNet给出科学家完成任务所需执行的一系列单独步骤。例如，在化学中，一项任务涉及纯化反应混合物，该任务的步骤之一是装填色谱柱。分类器会看到分类体系中成对出现的步骤，并被问及AI能把其中哪一个做得更好。我们用Bradley–Terry模型汇总这些比较——正是这一模型支撑了依据对弈结果给棋手排名的Elo等级分。一个步骤在比较中胜出则分数上升，落败则下降。随后我们对每项任务的步骤取平均，得到任务层级的分数（细节见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)）。我们把这一度量称为_理论AI能力_，把某项任务的具体分数称为其_AI能力分数_。
为比较各任务间的使用，我们考察某项任务的Claude使用相对于研究人员在该任务上所花时间是更高还是更低。例如，一项占研究人员时间5%却占Claude会话10%的任务，其使用量是预期的两倍，比值为2。比值为1表示Claude使用与研究人员在该任务上所花时间相符。比值低于1表示，按该任务所占研究人员时间衡量，Claude的使用低于预期。
图8显示，这一使用比值随任务AI能力分数急剧上升。对能力分数最低20%的任务（如纯化反应混合物、进行参与式观察），Claude几乎不被使用。在能力分数中位数处，比值约为1，因此使用量与研究人员时间相符。对能力分数最高20%的任务（如可视化数据、应用统计检验），与研究人员通常花在这些任务上的时间相比，Claude上的使用约高两倍，Claude Code上约高四倍。这些规律说明，科学家对Claude的使用紧密跟随AI能力分数。Claude Code的斜率更陡，反映出它聚焦计算类工作，而这类工作的能力分数更高。
![折线图显示Claude与Claude Code的使用比值 \(使用份额除以研究时间份额\) 随任务理论AI能力百分位的变化。两条线都从能力最低五分位组的约0.2升至中间五分位组的约1。在最高五分位组，Claude上的比值达到约2.1，Claude Code上约3.9。](assets/how-researchers-use-claude/img_008.webp)
**Claude使用与理论AI能力。** 纵轴表示各能力五分位组中任务的使用比值，计算方式为投入这些任务的研究会话份额除以据SciNet估计的研究时间份额。横轴表示任务的AI能力分数（百分位）。橙色点表示Claude上各AI能力五分位组任务的平均使用比值，蓝色点表示Claude Code上的相应数值。
理论AI能力可能因多种原因而在任务间不同。为理解这些差异，我们把每项任务的AI能力分数与三组由LLM得出的任务特征关联起来：其对强化学习（RL）的适配性；工作以认知、人际还是体力为主；以及监管限制是否制约AI使用（图9；定义与数据来源见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)）。
先看RL适配性。在RL中，AI模型反复尝试一项任务，成功时获得奖励，从而学会执行该任务。当成功易于验证、大量样本可在计算环境中模拟、反馈能快速给出时，任务尤其适合RL（Lambert et al. 2024; Guo et al. 2025）。我们用SciNet中针对这三个RL相关成分的任务级度量，把它们汇总为一个单一指数。任务的能力分数与其RL指数分数高度相关（后者是单独分类得到的，相关系数为0.78）。这说明AI在最易应用RL的研究任务上能力最强。
其他重要任务特征关乎工作的性质。有些研究任务本质上是认知性的，另一些则需要体力动作或人际接触。一般而言，体力任务超出纯认知机器的能力范围。还可能有限制AI使用的监管约束。以认知工作为特征的任务，AI能力分数更高（相关系数0.69）。相比之下，包含更多体力工作的研究任务AI能力分数更低（−0.57）。包含人际工作（−0.31）或涉及AI使用监管限制（−0.38）的研究活动，分数也往往更低。
![条形图显示任务理论AI能力百分位与其他任务特征之间的相关性。RL指数：+0.78。认知：+0.69。体力：−0.57。人际：−0.31。监管限制：−0.38。](assets/how-researchers-use-claude/img_009.webp)
**理论AI能力与其他任务特征。** 研究任务的AI能力分数百分位与该任务其他特征之间的相关性。
同样的任务特征也能预测研究人员在某一给定任务上使用Claude的程度（图10）。对RL适配性处于最低五分之一的任务，Claude几乎不被使用。对处于最高五分之一的任务，相对于研究人员所花时间，Claude使用高得不成比例：Claude上高两倍，Claude Code上高四倍。这与Claude使用同AI能力分数总体上的关联相似——那里最高20%的任务同样吸引了预期使用量两到四倍的使用。
在以认知为主的任务上，Claude使用也高得不成比例。相比之下，体力与人际任务上Claude使用量低。在监管壁垒限制AI辅助的任务上，Claude使用也较低。总体而言，在高度专门化的研究任务谱系中，使用度量与能力度量紧密相关。
![五幅折线图显示Claude与Claude Code上按任务特征划分的使用比值。使用比值随任务RL指数上升，在最高分处Claude上约达2.2、Claude Code上约达4.2；也随认知步骤占比上升，达到约1.4和1.5。随体力步骤占比、人际步骤占比或监管限制分数上升，它从约1.2降至接近零。](assets/how-researchers-use-claude/img_010.webp)
**Claude使用与任务特征。** 每个面板考察一种不同的任务特征。纵轴表示在该特征上得分不同的任务组（"分箱"）的使用比值，横轴表示该特征强度的度量。橙色点表示Claude上各分箱任务的平均使用比值，蓝色点表示Claude Code上的相应数值。位于零处的点表示因负责该使用的账户过少、出于隐私而隐去的分箱。
不同科学领域依赖不同的研究活动组合。细分研究任务上使用量与能力分数的相关性，能否解释为何有些领域使用Claude更多？我们的数据显示可以：某子领域每名研究人员的Claude使用量，往往随其任务平均AI能力分数上升而提高（Claude相关系数为0.45，Claude Code为0.57），如图11所示。
各学科大类之间也存在显著差异，说明Claude使用受AI能力之外因素的影响。与自身任务的AI能力分数相比，健康科学研究人员使用Claude相对偏少，可能是因为医疗数据与研究的监管限制了AI的使用、或使其更难整合。形式科学、社会科学以及艺术与人文学科的研究人员，使用Claude的程度高于AI能力分数的预测。这些领域的大量工作通过文本与代码完成，这很可能促进了AI工具的采用。物理科学与生命科学中的Claude使用总体上更贴合AI能力分数，尽管个别子领域可能偏离。
![两幅气泡图，一幅对应Claude，一幅对应Claude Code，以对数刻度绘制各子领域每名研究人员的使用量相对其研究工作的理论AI能力，气泡大小按研究人员数量确定。拟合线向上倾斜，Claude的加权相关系数为+0.45，Claude Code为+0.57。形式科学子领域聚集在高能力、高使用一端，而许多健康科学子领域落在线下方。](assets/how-researchers-use-claude/img_011.webp)
**各子领域的Claude使用与理论AI能力。** 两个面板都把每个子领域表示为一个点，大小按该子领域的研究人员数量确定。纵轴以对数刻度显示每名研究人员的使用量，其计算方式为该子领域的研究会话份额除以该子领域在全部研究人员中的份额。横轴显示子领域的AI能力分数，通过按研究人员工时加权、汇总该子领域所有研究任务得出。黑线表示最佳拟合，每个面板报告按子领域规模加权的相关系数。左图显示Claude上科研会话的结果，右图显示Claude Code上科研会话的结果。
理论AI能力还能预测研究人员在多大程度上允许Claude自主工作。图12显示，自主式使用与子领域的理论AI能力相关。换言之，理论AI能力更高的子领域不仅使用AI更多，而且以更自主的方式使用。
![两幅气泡图，一幅对应Claude，一幅对应Claude Code，绘制各子领域的平均AI自主性分数 \(1到5的量表\) 相对其研究工作的理论AI能力，气泡大小按研究人员数量确定。拟合线向上倾斜，Claude的加权相关系数为+0.47，Claude Code为+0.31。](assets/how-researchers-use-claude/img_012.webp)
**各子领域的AI自主性与理论AI能力。** 两个面板都把每个子领域表示为一个点，大小按该子领域的研究人员数量确定。左图代表Claude上的科研会话，右图代表Claude Code上的科研会话。纵轴显示该子领域会话按会话量加权的平均自主性分数。横轴显示该子领域任务的平均理论能力，同样按使用量加权。未被任何会话覆盖的任务被排除在分析之外，因为无法对其自主性评分。为便于阅读，离群子领域已略去，但仍在最佳拟合线与相关系数计算中纳入。相关系数按子领域规模加权。

## 借助AI加速研究的情景
科学与技术进步的速度取决于好想法以及实现这些想法的手段。历来，两者都受人类能力所限。研究人员数量有限，每人的时间也有限，要用于提出假设、设计恰当的检验、运行分析并综合研究发现。
AI可通过两种方式缓解这些约束。其一，它可以承担研究人员目前所做的工作，使他们能探索更多想法。其二，它可以贡献研究人员原本可能无法想到的想法。第二种最终可能最为重要，但难以衡量得多，因此我们的分析聚焦第一种。

### 方法
我们考虑通过AI实现科学加速的三种情景。情景1假设当前AI能力被广泛采用，其估计来自我们的调查与AI能力分数。情景2和3是假设性的未来：AI完全自动化75%或100%的非体力研究步骤（即构成SciNet中每项研究任务的单个动作），从AI能力分数最高的步骤开始。在所有三种情景中，研究人员仍继续执行体力步骤。这些是说明性情景，而非预测。它们展示体力工作、理论AI能力与AI成本会如何塑造科学研究的加速，以及哪些领域可能加速最多。
对每种情景，我们报告两个度量。第一个是_AI份额_：在一项研究中AI能够承担的研究人员时间所占比例。按研究人员目前的时间分配，它衡量AI能释放多少人类研究时间，直接由上文分析得出。研究人员可以把释放出的时间转用于其他工作，从而提高研究产出。我们的第二个度量_加速_估计这一收益：在固定研究预算下，相对无AI时研究产出的增幅。它告诉我们同样预算能多产出多少研究成果。释放出的时间并不会一对一转化为更多产出，既因为研究人员把精力转向AI帮助较少的任务，也因为AI本身有成本。
我们从调查构建情景1的AI份额，该调查记录了五级AI使用：无、辅助、共享、委托、自主。我们假定这五级分别对应AI承担某一给定任务步骤中研究人员时间的0%、25%、50%、75%和100%。在每个任务类别内，我们按AI能力分数给任务步骤排序，再按调查所报告的比例把AI使用层级分配给各任务步骤，最高层级分给得分最高的步骤。以构思与假设产生为例，17%的回复报告不使用AI，53%报告辅助式使用。因此，AI能力分数最低的17%构思任务步骤被赋予零AI份额，接下来的53%被赋予25%，依此类推逐级向上。由于受访者很可能是重度AI采用者，我们把其报告的使用视作AI当下能力所及的替代指标。最后，我们把AI释放的研究人员时间从步骤汇总到领域（见[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)）。
为计算加速，我们使用想法生产函数——一个把研究人员时间等研究投入转化为研究产出的标准经济模型。在该模型中，一篇论文需要许多研究任务（Jones 2026）。这些任务互为补充，因而某一环节的强项无法完全弥补另一环节的弱项。随着AI让某些任务变得更廉价，研究人员把精力转向AI帮助较少的任务，从而缓解限制总体收益的瓶颈。例如，研究人员可以花更多时间提出新问题，或开展更多体力实验以扩充实证证据。我们依据Ahmadpoor和Jones（2019）校准这些瓶颈在多大程度上限制总体收益。关于AI成本，我们假定一小时AI智能体时间花费30美元，而一小时研究人员时间为95美元，且AI每节省一研究人员小时需运行0.2小时。这些是说明性假设：AI成本采用当今公开标价。如下文所述，这些成本越低，给定预算内能完成的研究越多，加速也越大。[附录](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)描述了模型与假设。
![双面板点图展示三种情景下34个领域：当前AI、75%非体力步骤自动化、全部非体力步骤自动化。左图：通过AI释放的研究时间百分比，在当前AI下约从27%到52%不等，统计学与计算机科学最高，艺术与人类学最低。右图：以对数刻度显示相对无AI研究的产出。在当前AI下，加速约从1.35倍到2倍。当全部非体力步骤自动化时，统计学、计算机科学与多数社会科学达到约15倍，而生物学、化学、生物医学科学与材料科学等实验台科学停留在约3–4倍。](assets/how-researchers-use-claude/img_013.webp)
**AI释放的研究时间与研究加速。** 每一行是一个领域。左图按AI可承担的研究人员时间估计份额给领域排序。圆圈表示当前能力的估计；菱形表示若75%非体力步骤自动化所释放的时间份额估计；三角形表示若100%非体力步骤自动化所释放的时间份额估计。右图显示给定领域研究预算下的研究加速，其横轴以无AI产出为基准（1倍＝无变化）显示三种情景下有AI时研究产出的倍数。

### 情景1：当前能力
以当前能力，若被广泛采用，AI可承担产出一项新研究所需研究人员时间的27–52%，各领域中位数为38%（图13左图）。这些份额意味着研究加速从艺术的1.35倍、人类学的1.36倍、化学的1.41倍，到计算机科学的1.96倍和统计学的2.02倍不等（图13右图）。加速之所以有限，是因为当今AI工作多为辅助式或共享式而非自主式，研究人员在几乎每个步骤上仍需投入大量时间。即便工作几乎完全属认知性、对AI准备最充分的领域，也仅达到约2倍加速。这些估计假定AI广泛扩散，且研究人员把它应用于当下有用的每一个步骤。
有两个因素解释了领域间的大部分差异。第一个是体力工作，没有物理集成，AI无法承担。在农业科学、生物医学科学、化学和材料科学等实验室与野外科学中，38–41%的研究人员时间用于体力步骤，而中位领域仅为4%。仅体力份额一项就解释了AI份额差异的约三分之一。第二个因素是认知工作内部AI能力分数的分布。艺术与历史花在体力步骤上的时间很少（分别为10%和4%），但其认知步骤的AI能力分数低，或许因为定性与阐释性工作较不适合强化学习。相比之下，计算机科学与统计学分数高、AI份额大，由数据分析驱动——这是各领域中AI能力分数最高的一类工作。
在Claude上使用比值更高的领域，往往也有更大的AI份额（图14）。AI份额的计算完全未用任何Claude使用数据，因此这一关系进一步证明AI使用跟随理论AI能力。
![气泡图以对数刻度绘制各领域在Claude上的使用比值相对通过AI释放的研究时间百分比，气泡大小按研究人员数量确定。拟合线向上倾斜，加权相关系数为+0.58。统计学与计算机科学在两项度量上都最高。医学与临床科学、兽医学的使用比值最低。](assets/how-researchers-use-claude/img_014.webp)
**各领域的Claude使用与AI释放的研究时间。** 观测到的Claude使用与各领域AI份额之间的相关性。每个领域是一个点，大小按研究人员数量确定。纵轴以对数刻度显示该领域在Claude上的使用比值，横轴显示以当前能力AI可完成的人类研究时间估计份额。

### 情景2和3：更大程度的自动化
在这些更偏推测性、且在很大程度上取决于对AI能力范围与成本之假设的情景中，更大程度的自动化使AI份额与加速都急剧上升，并拉大领域间差异。
在情景2中，75%的非体力步骤可由AI完成，计算机科学的加速约达8倍，统计学与图书馆及信息科学约7倍，经济学约6倍。多数其他社会科学、数学以及物理与天文学达到4–5倍，而实验台科学与医学科学约2–3倍。实验台科学与艺术及人文学科收益最小，但原因不同：在实验台科学中，大量工作属体力性质，仍须由研究人员完成；在艺术与人文学科中，工作多为认知性但AI能力分数低，因此其步骤中很少落入被自动化之列。自动化步骤在计算机科学中占非体力研究人员时间的82%，在艺术中仅占28%。历史、人类学与艺术的加速约为2倍或更低。
在情景3中，艺术与人文学科后来居上，而实验台科学仍受掣肘。一旦AI自动化全部非体力步骤，低AI能力分数不再限制认知工作，AI可以在许多领域承担近乎全部研究工作（图13左图）。在这一推测性情景中，体力任务少的领域（包括统计学、计算机科学、经济学、数学、心理学，以及多数社会科学与艺术及人文学科）达到约15–16倍。拥有大量实验室或野外工作的领域（如生物学、化学、材料科学、农业科学、生物医学科学）仅达3–4倍。在缺乏自动化实验室的情况下，其体力步骤（约占研究人员时间的40%）仍是瓶颈。
从这些情景可得出两点启示。第一，体力瓶颈依然强大。没有物理集成AI便无法执行的步骤，会在研究人员时间与预算中占据主导，给加速设下上限。第二，在不存在此类瓶颈之处，非同寻常的进展速度成为可能，而AI成本成为限制。在我们的假设下，一项被AI完全自动化的任务，其成本仍约为研究人员亲自执行成本的十六分之一，因此加速趋近约16倍便止步于此。更低的AI成本会按比例抬高这一上限，例如把AI成本减半就会使进展速度翻倍。如果成本大幅下降，包括对AI较晚才自动化的更难任务，那么没有体力瓶颈的领域可能加速到远超这些估计。
这些计算有若干重要局限，其影响会朝两个方向显现。我们没有考虑领域层面而非研究团队层面的约束，例如在大型强子对撞机这类设施上能同时运行的实验数量有限。我们也只计入研究人员与AI时间的成本，未计入实验机械或物料成本，而这些在健康、物理与生命科学中可能相当可观。我们同样未考虑用模拟替代体力实验，这本可缓解某些领域的瓶颈。最后，我们未考虑想法的质量。若AI能识别出成功概率更高的更好假设，研究可能进一步加速；若研究品味仍为人类所独有，加速则会更慢。

### 研究人员的预期
上述情景刻画了一系列可能性。研究人员自身的预期能提供以专业经验为根基的独特指引。为收集其观点，我们对生命与健康科学研究人员的调查询问：他们认为AI在独立工作时，何时能在不同类别的研究工作上比肩本领域最优秀的研究人员（图15）。受访者的近期预期很高：超过半数预期AI到2027年能在数据分析上比肩顶尖研究人员，38%表示AI已达到这一水平。到2030年，94%预期AI将在数据分析上比肩最优秀的研究人员，写作上为89%，构思与数据收集各为72%。对构思与数据收集的预期较低，与如今Claude在这些任务上使用较少相一致。
对无人在环的端到端AI研究，预期更为保守，但研究人员仍预期会有显著进展。约40%的受访者预期AI到2030年能开展完整研究项目，到2035年约64%，不过16%表示这永远不会发生。对AI自主产出科学突破的预期更为谨慎，约半数研究人员认为这要到2035年之后才会出现（如果会出现的话）。总体而言，许多研究人员预期未来十年将出现高度自动化，与我们的更大程度自动化情景大体一致。这些预期以多快速度、在多大程度上实现，不仅取决于AI作为软件技术的进步，也取决于为克服物理障碍而建设自动化实验室的努力。
把过去的调查证据与实际结果对照可见，AI进展常被大幅低估（Rosenberg et al. 2026）。例如，在2022年年中的一项调查中，领域专家对AI在国际数学奥林匹克达到金牌水平的中位估计是2030年，超级预测者则是2035年（Karger et al. 2023）。AI在2025年达成这一里程碑，比那些预测提前了约五到十年。尽管预测者系统性地低估了AI能力的进展，也存在少数例外，主要出现在需要在物理世界中执行的领域，例如生物学中AI辅助的实验室任务。
![堆叠条形图显示受访者预期AI何时能比肩本领域最优秀的研究人员，从"当下已可能"到"永远不会"。当下已可能：构思与假设产生13%、数据收集23%、数据分析38%、写作与传播30%。对无人在环的完整研究周期，多数受访者回答2030年或更晚，16%回答永远不会。对无人在环的突破性发现，30%回答晚于2035年，18%回答永远不会。](assets/how-researchers-use-claude/img_015.webp)
**研究人员预期AI何时比肩本领域最优秀的研究人员。** 结果来自我们自己的调查。上面四行对应研究人员预期AI独立工作、在不同任务类别上比肩本领域最优秀研究人员的时间。下面两行对应研究人员预期AI在没有人类科学家参与的情况下，完成"从问题到发现"、并在各自领域产出"本领域会视为重大进展的发现"的时间。

## 讨论
若AI有助于加快科学发现，它可能促成更高的生活水平以及疾病治疗上更快的进展。我们的估计表明潜在收益相当可观。但AI研究能力的进步并不会自动转化为快速进展；能否实现这种加速，还取决于我们如何应对若干约束。
第一，采用可能大幅滞后于能力。新技术的扩散通常缓慢（Comin and Hobijn 2010），而生产力收益往往要到组织围绕技术完成重构之后才会显现（David 1990; Brynjolfsson, Rock, and Syverson 2021）。个体学习过程、组织或系统层面的摩擦，以及对AI获取或基础设施的约束，都可能拖慢采用。
第二，研究可能继续面临AI无法消除的瓶颈。体力实验可能昂贵且缓慢，即便AI能力极强，也会大幅限制进展。我们在上述情景的实验台科学中尤其看到这一点。选择研究什么可能是另一个瓶颈：研究问题在很大程度上决定一个研究项目的价值，而AI能否提出好问题仍不明确。若构思成为瓶颈，即便回答某个既定问题变得廉价得多，它也会限制加速。反之，若AI在提出高质量假设上超越人类，加速可能更为可观，尤其在检验假设成本高昂的领域。
第三，AI赋能的研究可能提升研究产出的数量或质量，对科学有不同含义。新研究论文激增可能让一个领域推进得更快，却也可能压垮科学家吸收或核实结果的能力。另一方面，从显微镜、望远镜到统计软件，新技术历来提升了科学洞察的质量，AI同样能让更全面的分析与更宏大的项目变得可行。而随着论文更易产出，研究共同体可能愈发奖励特别新颖或高质量的工作。更高效的研究究竟导向更多数量还是更高质量，将取决于研究人员的选择，以及期刊、资助方与机构所设定的激励。
第四，研究的组织方式可能以难以预料的方式改变。随着AI变得更强、更自主，AI系统可能在验证、评审与传播重要成果上起主导作用，从而缓解上文讨论的吸收问题。更远的未来，AI研究智能体也可能借助机器人技术与自动化实验室，在独立于人类的大型共同体中推进科学前沿。这类自主AI研究会引出问题：人类如何跟进新知识、能否理解它，以及它是如何被产生的。
第五，更自主的AI系统可能加大确保AI驱动研究与人类目标保持一致的难度。随着AI智能体变得更强、更有创造力，让人类参与关键研究决策（例如探索哪些问题、如何探索），对安全与人类福祉可能至关重要。发现本身或研究的副产物也可能带来风险，尤其是在生物学中：那些加速医学进展的能力，同样可能产出危险的知识或材料。在此类情形下，在研究过程中设置审慎的检查点或许是必要的，这要求我们为降低风险而接受较慢的进展。
最后，研究人员从事的工作可能发生实质变化。影响之一可能是研究人员工作满意度的改变。若AI接管令人愉悦或有回报的任务，满意度可能下降，选择研究职业的人可能减少。若AI反而接管研究人员觉得乏味的任务，满意度可能上升。行政工作是一个潜在目标。在美国，联邦资助项目的首席研究员报告，约44%的研究时间用于满足行政要求而非做研究（Schneider et al. 2020），减轻这一负担可能是一大福音，既节省时间又提升总体满意度。最终净效应并不确定，且可能随AI能力演进而变化。一种乐观的看法是，AI将拓展发现的机会，而这正是研究职业令人有回报的核心。若科学是驶向"无尽前沿"的航程，AI或许是一艘新船，让研究人员能在研究问题与发现的广阔疆域上行得更远。

## 附录
[可在此获取](<https://www-cdn.anthropic.com/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)。

## 参考文献
```
Ahmadpoor, Mohammad and Benjamin F. Jones, “Decoding Team and Individual Impact in Science and Invention,” _Proceedings of the National Academy of Sciences_ , 2019, 116 (28), 13885–13890.
Alamos, Cristian and Lukas Althoff, “SciNet: The Anatomy of Science,” dataset, 2026. <https://www.anatomyofscience.com/>
Amodei, Dario, “Machines of Loving Grace: How AI Could Transform the World for the Better,” essay, October 2024. <https://darioamodei.com/essay/machines-of-loving-grace>
Anthropic, “Learning More about Claude’s Mathematical Capabilities,” research post, August 10, 2026a. <https://www.anthropic.com/research/riemann-zeta>
Anthropic, “Formalizing Fermat’s Last Theorem,” research post, September 4, 2026b. <https://www.anthropic.com/research/formalizing-fermats-last-theorem>
Appel, Ruth et al., “Anthropic Economic Index Report: Economic Primitives,” research post, January 15, 2026. <https://www.anthropic.com/research/anthropic-economic-index-january-2026-report>
Brynjolfsson, Erik, Daniel Rock, and Chad Syverson, “The Productivity J-Curve: How Intangibles Complement General Purpose Technologies,” _American Economic Journal: Macroeconomics_ , 2021, 13 (1), 333–372.
Bush, Vannevar, _Science, the Endless Frontier: A Report to the President_ , Washington, DC: United States Government Printing Office, 1945.
Codreanu, Mihai et al., “AI in Science: Early Insights,” arXiv preprint arXiv:2609.28504, 2026. <https://arxiv.org/abs/2609.28504>
Comin, Diego and Bart Hobijn, “An Exploration of Technology Diffusion,” _American Economic Review_ , 2010, 100 (5), 2031–2059.
David, Paul A., “The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox,” _American Economic Review_ , 1990, 80 (2), 355–361.
Eloundou, Tyna et al., “GPTs Are GPTs: Labor Market Impact Potential of LLMs,” _Science_ , 2024, 384 (6702), 1306–1308.
Guo, Daya et al., “DeepSeek-R1 Incentivizes Reasoning in LLMs through Reinforcement Learning,” _Nature_ , 2025, 645 (8081), 633–638.
Hao, Qianyue et al., “Artificial Intelligence Tools Expand Scientists’ Impact but Contract Science’s Focus,” _Nature_ , 2026, 649 (8099), 1237–1243.
Jones, Benjamin F., “Artificial Intelligence in Research and Development,” in Ajay Agrawal, Erik Brynjolfsson, and Anton Korinek, eds., _The Economics of Transformative AI_ , Chicago: University of Chicago Press, 2026, 37–61.
Jumper, John et al., “Highly Accurate Protein Structure Prediction with AlphaFold,” _Nature_ , 2021, 596 (7873), 583–589.
Karger, Ezra et al., “Forecasting Existential Risks: Evidence from a Long-Run Forecasting Tournament,” Forecasting Research Institute Working Paper 1, 2023. <https://forecastingresearch.org/research/existential-risk-persuasion-tournament>
Kobak, Dmitry et al., “Delving into LLM-Assisted Writing in Biomedical Publications through Excess Vocabulary,” _Science Advances_ , 2025, 11 (27), eadt3813.
Lambert, Nathan et al., “Tülu 3: Pushing Frontiers in Open Language Model Post-Training,” arXiv preprint arXiv:2411.15124, 2024. <https://arxiv.org/abs/2411.15124>
Liang, Weixin et al., “Quantifying Large Language Model Usage in Scientific Papers,” _Nature Human Behaviour_ , 2025, 9 (12), 2599–2609.
Liu, Yinhong et al., “Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators,” in _Proceedings of the First Conference on Language Modeling (COLM)_ , 2024.
Mantiuk, Rafał K., Anna Tomaszewska, and Radosław Mantiuk, “Comparison of Four Subjective Methods for Image Quality Assessment,” _Computer Graphics Forum_ , 2012, 31 (8), 2478–2491.
Massenkoff, Maxim et al., “Anthropic Economic Index Report: Cadences,” research post, June 26, 2026. <https://www.anthropic.com/research/economic-index-june-2026-report>
Merchant, Amil et al., “Scaling Deep Learning for Materials Discovery,” _Nature_ , 2023, 624 (7990), 80–85.
OpenAI, “An OpenAI Model Has Disproved a Central Conjecture in Discrete Geometry,” research post, May 20, 2026a. <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
OpenAI, “On the Navier–Stokes Millennium Prize Problem,” research post, September 8, 2026b. <https://openai.com/index/navier-stokes-solution/>
Parshall, Daniel and Andrea Lopez-Luzuriaga, “Measuring AI’s Economic Reach: A Multi-Dimensional Task Taxonomy,” George Washington University Center for Economic Research Working Paper 2026-005, 2026. <https://www2.gwu.edu/~forcpgm/2026-005.pdf>
Robinson-Garcia, Nicolas et al., “Meta-Research: Task Specialization Across Research Careers,” _eLife_ , 2020, 9, e60586.
Rosenberg, Josh et al., “How Accurate Have AI Progress Forecasts Been So Far?” research post, Forecasting Research Institute, September 22, 2026. <https://forecastingresearch.org/research/ai-progress-accuracy-update>
Schneider, Sandra L. et al., “2018 FDP Faculty Workload Survey: Report of Primary Findings,” Federal Demonstration Partnership, 2020. <https://thefdp.org/wp-content/uploads/FDP-FWS-2018-Primary-Report.pdf>
Shah, Nihar B. et al., “When Is It Better to Compare than to Score?” arXiv preprint arXiv:1406.6618, 2014. <https://arxiv.org/abs/1406.6618>
Tomei, Philip Moreira and Bouke Klein Teeselink, “What Jobs Can AI Learn? Measuring Exposure by Reinforcement Learning,” arXiv preprint arXiv:2605.02598, 2026. <https://arxiv.org/abs/2605.02598>
Tsoukalas, George et al., “Advancing Mathematics Research with AI-Driven Formal Proof Search,” _Science_ , 2026, 394 (6820), 234–239.
Varadi, Mihaly et al., “AlphaFold Protein Structure Database in 2024: Providing Structure Coverage for over 214 Million Protein Sequences,” _Nucleic Acids Research_ , 2024, 52 (D1), D368–D375.
Wang, Hanchen et al., “Scientific Discovery in the Age of Artificial Intelligence,” _Nature_ , 2023, 620 (7972), 47–60.
```

## 脚注
01在计算各领域全球研究人员数量时，我们排除了Claude不可用的国家。
02我们从SciNet获取研究人员数量。该度量的细节见[附录](<https://cdn.sanity.io/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)。
03会话记录按所开展的研究而非所用工具归入各领域，因此其他计算科学中的编码工作不计入计算机科学。
04由于抽样变异与分类噪声更大，子领域级使用份额的估计精度低于领域级份额，对会话量较低的子领域尤其如此。因此我们聚焦总体规律，而非任何单个低会话量子领域的位置。
05尽管我们的分析聚焦研究任务，教学、服务与行政等非研究任务可能占据研究人员时间预算的相当份额。不过，我们的科研使用分类器有意撇开本科教学，并且若行政或日常事务并不直接服务于某项研究或课题，也不会将其选入。此外，我们的样本并不限于学术岗位的科学工作者，而这类人自然承担更重的教学与服务工作。因此，我们把这些工作流中AI使用的研究留待未来。
06就单项任务而言，起草稿件是Claude（18.6%）和Claude Code（11.1%）上都最常见的任务。在Claude上，其次常见的任务是审阅与综合文献（6.8%）以及回复同行评审意见（6.7%）。在Claude Code上，则是设计、构建与打磨成果（4.8%）以及可视化数据与结果（4.6%）。
07受访者从Anthropic的AI for Science及相关资助项目的申请者中招募，隶属于美国和加拿大的研究机构。由于他们申请了AI研究额度，其AI使用强度很可能高于一般科学家。细节见[附录](<https://cdn.sanity.io/files/4zrzovbb/website/fafb3d4237f9b53fe114fef4fb5109b9cf5b5e60.pdf>)。
08Claude Science上所执行任务的差异，可能部分反映了使用者是谁。任何付费用户都可使用Claude Science，但采用者很可能是拥有更专门或更高要求用例的人。因此，我们把各产品间的差异描述为使用模式。
09为识别每段Claude会话的成果，我们使用[此前工作](<https://www.anthropic.com/research/economic-index-june-2026-report>)（Massenkoff et al. 2026）引入的一个分类器。该分类器识别此次交流中Claude产出的最显著成果。我们把更细粒度的回答归为两类：书面成果与技术成果。书面成果主要包括文档、报告、学术论文或演示文稿。技术成果主要包括软件输出，如脚本、代码修正、数据与图表。不属于书面或技术成果的成果包括分析或摘要、解释或建议。

## 作者与致谢
### 致谢
Cristian Alamos, Bailey Bova, Tom Chivers, Lauren Cottrell, Eleanor Dorfman, Adam Farina, Deep Ganguli, Rebecca Hiscott, Chad Jones, Anneke Jong, Aisling Keenan, Anton Korinek, Eva Lyubich, Paruul Maheshwary, Miles McCain, Teddy McGuire, Ankur Rathi, Santi Ruiz, Szymon Sacher, David Saunders, Monika Tuchowska, Nick Turner, Heather Whitney, Kim Withee, Jack Clark。
### 引用
    
    @techreport{hermle2026AIScience,
      author = {Hermle, Johannes and Jones, Benjamin and Althoff, Lukas and Heller, Ryan and Lyttelton, Thomas and Stein, Carolyn and Wilmers, Nathan and Massenkoff, Maxim and McCrory, Peter},
      title = {{AI} for scientific discovery: How researchers use {Claude}},
      institution = {The Anthropic Institute},
      type = {Technical Report},
      year = {2026},
      month = nov,
      url = {https://www.anthropic.com/research/how-researchers-use-claude}
    }
