---
title: Anthropic Education Report:How university students use Claude
url: https://www.anthropic.com/research/anthropic-education-report-how-university-students-use-claude
date: Apr 8, 2025
category: Societal Impacts
source: https://www.anthropic.com/research
---

# Anthropic 教育报告：大学生如何使用 Claude

- **日期：** 
- **类别：** 社会影响（Societal Impacts）
- **来源：** https://www.anthropic.com/research/anthropic-education-report-how-university-students-use-claude

---

社会影响（Societal Impacts）
2025 年 4 月 8 日
![一盏灯照在文件上](assets/anthropic-education-report-how-university-students-use-claude/img_000.jpg)
发布于
    2025 年 4 月 8 日
团队
    [社会影响](</research/team/societal-impacts>)
主题
    
  * [教育](</search?topic=education>)
  * [人们如何使用AI](</search?topic=how-people-use-ai>)
  * [隐私](</search?topic=privacy>)
  * [Claude应用](</search?topic=claude-apps>)

[](</news/reflect-with-claude>)[](</research/AI-fluency-index>)[](</research/anthropic-education-report-how-educators-use-claude>)[](</news/advancing-claude-for-education>)
相关文章
  * 产品
2026 年 7 月 9 日
[介绍一种反思你如何使用Claude的方式](</news/reflect-with-claude>)

[阅读更多](</search?topic=education>)
AI系统不再只是专门的研究工具：它们已成为日常的学业伴侣。随着AI更深入地融入教育环境，我们需要思考关于学习、评估与技能培养的重要问题。迄今为止，大多数讨论依赖问卷调查和受控实验，而非学生如何在真实场景中自然地把AI融入学业的直接证据。
为填补这一空白，我们开展了首批针对高等教育中真实AI使用模式的大规模研究之一，分析了Claude.ai上100万段匿名学生对话。
我们这份教育报告的主要发现如下：
  * STEM（科学、技术、工程、数学）学生是Claude等AI工具的早期采用者，其中计算机科学学生的占比尤其突出（占学生对话的36.8%，而仅占美国学位的5.4%）。相比之下，商科、健康与人文学科学生的采用率相对于其入学人数偏低。
  * 我们识别出学生与AI互动的四种模式，每种模式在数据中出现的比例大致相当（各占对话的23–29%）：直接式问题解决（Direct Problem Solving）、直接式成果创作（Direct Output Creation）、协作式问题解决（Collaborative Problem Solving）与协作式成果创作（Collaborative Output Creation）。
  * 学生主要把AI系统用于创造（creating，利用信息学习新事物）与分析（analyzing，拆解已知内容并识别其间关系），例如创建编程项目或分析法律概念。这与[布鲁姆分类学（Bloom's Taxonomy）](<https://www.researchgate.net/publication/235465787_A_Taxonomy_for_Learning_Teaching_and_Assessing_A_Revision_of_Bloom's_Taxonomy_of_Educational_Objectives>)中的高阶认知功能相吻合。这引发了如何确保学生不把关键认知任务外包给AI系统的问题。

## 识别教育场景中的AI使用
研究人们如何使用AI模型时，保护用户隐私至关重要。在本项目中，我们使用了Claude Insights and Observations，即“[Clio](<https://www.anthropic.com/research/clio>)”——我们的自动化分析工具，可揭示人们如何使用Claude。Clio通过把用户对话提炼为高层级的使用摘要（如“排查代码错误”或“解释经济学概念”），实现对AI使用模式的自下而上发现。Clio采用多层次的自动化流程，从对话中移除用户的私人信息。我们设计这一流程，是为了尽量减少从一层传递到下一层的信息。我们在这篇[早前的博客](<https://www.anthropic.com/research/clio>)中介绍了Clio隐私优先的设计。
我们使用Clio分析了约100万段匿名化1对话，这些对话来自与高等教育邮箱地址绑定的Claude.ai Free与Pro账户。2随后我们按学生与学术相关性筛选这些对话——例如对话是否涉及课程作业或学术研究——得到574,740段对话。3接着Clio对这些对话分组，得出汇总的教育相关洞见：不同学科如何分布、学生与AI的互动有何差异，以及学生把哪些类型的认知任务委托给AI系统。
## 学生用AI做什么？
我们发现，学生主要用Claude创建和改进各学科的教育内容（占对话的39.3%）。这通常包括设计练习题、修改论文或总结学术材料。学生也经常用Claude为学业作业提供技术解释或解答（33.5%）——借助AI调试和修复编程作业中的错误、实现编程算法与数据结构，以及解释或求解数学问题。其中一部分使用也可能属于作弊，我们将在下文讨论。另有规模较小但仍相当可观的一部分学生使用，用于分析与可视化数据（11.0%）、支持研究设计与工具开发（6.5%）、绘制技术图表（3.2%），以及在不同语言之间翻译或校对内容（2.4%）。
下面是各学科常见请求的更详细分解。
![排名前四学科领域的常见学生请求，基于Clio在每个学科内统计的15个最频繁请求。](assets/anthropic-education-report-how-university-students-use-claude/img_001.png)
排名前四学科领域的常见学生请求，基于Clio在每个学科内统计的15个最频繁请求。
## 各学科的AI使用情况
接下来，我们考察了哪些学科的Claude使用_不成比例_。做法是把Claude.ai的使用模式与美国授予的学士学位数量进行对比。4Claude使用最不成比例地偏高的学科是计算机科学：尽管仅占美国学士学位的5.4%，计算机科学却占Claude.ai上对话的38.6%（这可能反映出Claude在计算机编程方面的特长）。自然科学与数学在Claude.ai中的占比也高于其学生入学人数占比（分别为15.2%对9.2%）。
相反，商科相关的教育对话尽管占学士学位的18.6%，却只占对话的8.9%，显示出Claude使用不成比例地偏低。健康专业（5.5%对13.1%）与人文学科（6.4%对12.5%）相对于这些学科的学生入学人数，占比也偏低。
这些模式表明，STEM学生、尤其是计算机科学专业的学生，可能更早把Claude用于教育目的，而商科、健康与人文学科的学生把这些工具融入学业流程的速度可能更慢。这或许反映出计算机科学社群对Claude的认知度更高，也反映出AI系统相对于其他学科学生所从事的任务，更擅长STEM学生所执行的任务。
![把与某个美国国家教育统计中心（NCES）学科领域相关的Claude.ai学生对话百分比（灰色）与拥有对应专业的美国大学生百分比（橙色）进行比较。请注意，百分比之和不为100%，因为部分对话被归入NCES的“其他”类别，而我们已在分析中将其排除。](assets/anthropic-education-report-how-university-students-use-claude/img_002.webp)
把与某个美国国家教育统计中心（[NCES](<https://nces.ed.gov/programs/digest/d23/tables/dt23_318.20.asp?current=yes>)）学科领域相关的Claude.ai学生对话百分比（灰色）与拥有对应专业的美国大学生百分比（橙色）进行比较。请注意，百分比之和不为100%，因为部分对话被归入NCES的“其他”类别，而我们已在分析中将其排除。
## 学生如何与AI互动
与AI互动的方式有很多，它们对学习过程的影响各不相同。在分析学生如何与AI互动时，我们识别出四种截然不同的互动模式，并沿两条不同的轴线对其分类，如下图所示。
第一条轴线是“互动模式”。它可能包括：5（1）**直接式（Direct）**对话，用户希望尽快解决自己的问题；（2）**协作式（Collaborative）**对话，用户主动寻求与模型展开对话以达成目标。第二条轴线是互动的“期望成果”。它可能包括：（1）**问题解决（Problem Solving）**，用户寻求问题的解答或解释；（2）**成果创作（Output Creation）**，用户希望产出较长的成果，如演示文稿或论文。把两条轴线组合起来，就得到下文呈现的四种模式。
![我们针对学生与AI对话的分类体系，以及基于Clio所浮现话题的示例对话主题。](assets/anthropic-education-report-how-university-students-use-claude/img_003.webp)
我们针对学生与AI对话的分类体系，以及基于Clio所浮现话题的示例对话主题。
这四种互动风格出现的比例相近（各占对话的23%至29%），体现出学生对AI用途之广。传统网络搜索通常只支持直接给出答案，而AI系统能支持种类丰富得多的互动，并随之带来新的教育机遇。我们挑选的一些正面学习示例包括：
  * 解释并厘清哲学概念与理论
  * 创建全面的化学教育资源与学习材料
  * 为学业作业解释肌肉解剖学、生理学与功能概念

与此同时，AI系统也带来新的挑战。一个常见的问题是：“学生有多少程度在用AI作弊？”这很难回答，尤其因为我们并不知道Claude每段回应被使用时的具体教育情境。例如，一段直接式问题解决的对话，可能是在带回家完成的考试中作弊……也可能是一名学生在对照练习题核对自己的答案。一段直接式成果创作的对话，可能是从零开始写一篇论文……也可能是为额外的研究整理知识摘要。一段协作式对话是否构成作弊，还可能取决于具体的课程政策。
尽管如此，近一半（约47%）的学生与AI对话属于直接式——即以最少的互动寻求答案或内容。虽然其中许多服务于正当的学习目的（如提出概念性问题或生成学习指南），我们确实发现了一些令人担忧的直接式对话示例，包括：
  * 提供机器学习选择题的答案
  * 提供英语语言测试题目的直接答案
  * 改写营销与商业文本以规避抄袭检测

这些引发了关于学术诚信、批判性思维技能的培养，以及如何最好地评估学生学习的重要问题。即便是协作式对话，也可能产生可疑的学习效果。例如，__“带解释地求解概率与统计作业题”可能在AI与学生之间包含多轮对话，但仍把大量思考外包给AI。我们将继续研究这些互动，并努力更好地区分哪些有助于学习、培养批判性思维。
## 各学科特有的AI使用模式
不同学科的学生以不同方式使用AI：
  * **自然科学与数学**对话倾向于问题解决，例如“用逐步计算求解具体的概率题”和“用逐步讲解求解学业作业或考试题”。
  * **计算机科学**、**工程**与**自然科学与数学**更偏向协作式对话，而**人文学科、商科与健康**在协作式与直接式对话之间的分布更为均衡。
  * **教育学**对成果创作表现出最强的偏好，占对话的74.4%。不过，这种使用可能源于我们筛选方法的不完善。其中许多对话涉及“创建全面的教学材料与教育资源”和“创建详细的教案”，表明教师也在把Claude用于教育支持。总体而言，教育学占全部对话的3.8%。

这表明，把AI融入教育的做法若能因学科而异，可能会更有成效。我们的数据是帮助认识不同学科学生使用AI方式差异的第一步。
![各NCES学科中对话在互动风格上的分布。](assets/anthropic-education-report-how-university-students-use-claude/img_004.webp)
各NCES学科中对话在互动风格上的分布。  

## 学生委托给AI的认知任务
我们还探究了学生如何把认知职责委托给AI系统。我们采用了[布鲁姆分类学（Bloom's Taxonomy）](<https://www.researchgate.net/publication/235465787_A_Taxonomy_for_Learning_Teaching_and_Assessing_A_Revision_of_Bloom's_Taxonomy_of_Educational_Objectives>)，6这是教育领域用于把认知过程从简单到复杂加以分类的层级框架。尽管该框架最初针对的是学生的思维，我们对其加以调整，用于分析Claude在与学生对话时的回应。
我们看到AI呈现出的布鲁姆分类学领域呈倒置分布：
  * Claude主要在完成高阶认知功能，其中创造（Creating，39.8%）与分析（Analyzing，30.2%）是布鲁姆分类学中最常见的操作。
  * 低阶认知任务较少见：应用（Applying，10.9%）、理解（Understanding，10.0%）与记忆（Remembering，1.8%）。

这一分布也随互动风格而变化。正如预期，成果创作类任务（如生成学术文本摘要或论文反馈）涉及更多创造功能；问题解决类任务（如求解微积分题或讲解编程基础）涉及更多分析功能。
AI系统展现出这些技能，并不排除学生自己也运用这些技能——例如共同创作一个项目，或在另一情境下用AI生成的代码分析数据集——但这确实指向学生把认知能力外包给AI的潜在隐忧。有理由担心，AI系统可能成为学生的拐杖，抑制支撑高阶思维所需基础技能的培养。毕竟，一座倒置的金字塔是会倾倒的。
![Claude在与学生对话中展现的认知技能，基于布鲁姆分类学。技能描述来自佛罗里达大学教学技术培训中心。](assets/anthropic-education-report-how-university-students-use-claude/img_005.webp)
Claude在与学生对话中展现的认知技能，基于布鲁姆分类学。技能描述来自[佛罗里达大学教学技术培训中心](<https://citt.ufl.edu/resources/the-learning-process/designing-the-learning-experience/blooms-taxonomy/>)。
## 局限性
我们的研究立足于真实世界的数据。就研究结论的有效性及其在教育情境中的适用性而言，这带来诸多优势。但它也附带一些可能影响结论适用范围的局限：
  * 我们的数据集很可能捕捉到的是早期采用者，未必能代表更广泛的学生群体；
  * Claude的使用相对于教育领域整体AI使用有多大的代表性尚不清楚——许多学生使用Claude.ai之外的AI工具，这意味着我们只呈现了他们整体AI使用模式的部分图景；
  * 对话分类中很可能同时存在假阳性与假阴性。我们依赖的是与高等教育邮箱地址绑定的账户中的对话：其中一些被分类器判定为与学生相关的对话，实际上可能来自员工或教职人员。此外，另一些学生对话很可能来自与非大学邮箱地址绑定的账户；
  * 出于隐私考虑，我们只分析单个18天保留窗口内的Claude.ai使用情况。随着学业任务在一年中的起伏，学生的使用很可能有所不同；
  * 我们只研究学生把哪些任务委托给AI，而不研究他们最终如何在学业中使用AI输出，也不研究这些对话是否切实支持学习成果；
  * 把学生与AI的对话归入各学科，可能无法充分涵盖AI使用模式可能显著不同的跨学科工作；
  * 把布鲁姆分类学应用于AI（而非学生）的认知过程并不完善。像记忆这样的技能，在AI系统的情境中更难量化。

各机构关于教育中使用AI的政策差异很大，可能以我们在这份数据集中无法衡量的方式显著影响所观察到的模式。
## 结论与展望
我们的分析为学生在真实世界中于何处、以何种方式使用AI提供了一幅鸟瞰图。我们认识到，对AI影响教育的理解才刚刚起步。
在与学生和教育者的交流中，我们看到AI能以非凡的方式赋能学习。例如，AI已被用于支持[一名学生的核聚变反应堆项目](<https://www.businessinsider.com/student-builds-nuclear-fusion-prototype-using-ai-glowing-plasma-orb-2024-9>)，并促进[课堂上师生之间更好的沟通](<https://www.sciencedirect.com/science/article/abs/pii/S0360131524001970?via%3Dihub>)。
但我们并不幻想这些初步发现能全面回答教育领域正在发生的深刻变化。AI正以各种方式让教育者的工作更富挑战，而本研究并未充分涵盖这些。随着学生把高阶认知任务委托给AI系统，一些根本性问题随之浮现：我们如何确保学生仍培养起基础的认知与元认知技能？在AI普及的世界里，我们如何重新定义评估与反作弊政策？如果AI系统能近乎即时地生成润色好的文章，或迅速解出一个人需要数小时才能完成的复杂问题，那么有意义的学习会是什么样子？随着模型能力增长、AI更深地融入我们的生活，从作业设计到评估方法的一切是否都会发生根本性转变？
这些发现为教育者、管理者与政策制定者之间关于如何确保AI深化而非削弱学习的持续讨论提供了素材。进一步的研究将帮助我们更好地理解学生与教师双方如何使用AI、其与学习成果的关联，以及对教育未来的长期影响。
## Anthropic的教育方针
除这份教育报告外，我们还正[与大学合作](<https://www.anthropic.com/news/introducing-claude-for-education>)，以更好理解AI在教育中的角色。作为早期一步，我们正在试验一种“学习模式”（Learning Mode），它强调苏格拉底式方法与概念理解，而非直接给出答案。我们期待与大学合作开展未来的研究，并更直接地研究AI对学习的影响。
## 脚注
01 这些对话跨越Claude.ai上一个18天的时段，以便继续依照我们的[隐私与保留政策](<https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-personal-data>)管理数据。关于Clio如何保护隐私的更多信息，请参阅我们的[研究博客](<https://www.anthropic.com/research/clio>)。
02 具体而言，我们把分析限定在全球范围内与高等教育机构相关联的邮箱地址账户，例如.edu与.ac.uk域名的邮箱。我们认识到，并非所有教育邮箱地址都属于学生。为此，我们随后把相关对话筛选为那些可能涉及学生课业的对话。
03 Clio使用Claude以自动化方式筛选对话。在本研究中，Clio把对话筛选为“很可能是一名学生在寻求学业、课业、学习、学习新概念、学术研究等方面的帮助？”的对话。我们[此前关于Clio的论文](<https://arxiv.org/abs/2412.13678>)详述并验证了这一筛选机制。
04 经由[美国国家教育统计中心（NCES）](<https://nces.ed.gov/programs/digest/d23/tables/dt23_318.20.asp?current=yes>)。
05 在实验中，我们使用“事务式”（Transactional）与“对话式”（Dialogic）这两个术语来分类对话，因为我们发现它们最精准地捕捉了Clio所浮现的自下而上的互动模式。具体地说，我们用Clio把对话归为以下之一：事务式问题解决、事务式成果创作、对话式问题解决或对话式成果创作；每种互动模式都配有相应的描述提供给Clio。为便于理解，本报告用“直接式”与“协作式”代替“事务式”与“对话式”。
06 具体而言，我们采用[Anderson与Krathwohl（2001）的修订版](<https://books.google.com/books/about/A_Taxonomy_for_Learning_Teaching_and_Ass.html?id=JPkXAQAAMAAJ&source=kp_book_description>)布鲁姆分类学，以及他们的认知过程分类体系。
## 作者与致谢
### 贡献者
Kunal Handa*与Drew Bent*设计并执行了实验、绘制了图表并撰写了这篇博客文章。Alex Tamkin提出了最初的实验并提供了详细的指导与反馈。Miles McCain反复完善了所有实验所需的技术基础设施。Esin Durmus、Michael Stern、Mike Schiraldi、Saffron Huang、Stuart Ritchie、Steven Syverud与Kamya Jagadish提供了宝贵的反馈与讨论。Margaret Vo、Matt Bell与Deep Ganguli全程提供了细致的指导、组织支持与反馈。
### 致谢
此外，我们感谢Rose E. Wang、Laurence Holt、Michael Trucano、Ben Kornell、Patrick Methvin、Alexis Ross与Joseph Feller的有益讨论与评论。
### 引用格式
    
    @online{handa2025education,
    author = {Kunal Handa and Drew Bent and Alex Tamkin and Miles McCain and Esin Durmus and Michael Stern and Mike Schiraldi and Saffron Huang and Stuart Ritchie and Steven Syverud and Kamya Jagadish and Margaret Vo and Matt Bell and Deep Ganguli},
    title = {Anthropic Education Report: How University Students Use Claude},
    date = {2025-04-08},
    year = {2025},
    url = {https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude},
    }
