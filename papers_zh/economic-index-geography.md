---
title: Anthropic Economic Index: Tracking AI’s role in the US and global economy
url: https://www.anthropic.com/research/economic-index-geography
date: Sep 15, 2025
category: Economic Research
source: https://www.anthropic.com/research
---

# Anthropic 经济指数：追踪 AI 在美国和全球经济中的作用

- **日期：**
- **类别：** 经济研究（Economic Research）
- **来源：** https://www.anthropic.com/research/economic-index-geography

---

经济研究（Economic Research）
2025 年 9 月 15 日
[探索我们的数据](<http://anthropic.com/economic-index>)
![Anthropic 经济指数：追踪 AI 在美国和全球经济中的作用](assets/economic-index-geography/img_000.img)
夏威夷的旅行规划、马萨诸塞州的科学研究、印度的 Web 应用开发。乍一看，这三项活动几乎没有共同点。但事实证明，它们是 Claude 在各自地区_过度代表_程度最高的特定用途。

这并不意味着它们是最_受欢迎_的任务：软件工程在全球几乎所有州和国家中仍然遥遥领先。相反，这意味着马萨诸塞州的人比其他地方的人更倾向于请 Claude 帮忙做科学研究——或者，举个例子，巴西的 Claude 用户似乎对语言特别热衷：他们使用 Claude 进行翻译和语言学习的频率约为全球平均水平的六倍。

这些统计结果来自我们的第三期 [Anthropic 经济指数报告](<http://anthropic.com/research/anthropic-economic-index-september-2025-report>)。在这一最新期中，我们扩大了工作范围，记录正在开始重塑工作和经济的 AI 采用早期模式。我们衡量 Claude 在以下方面的不同使用方式……

  * **……在美国境内：** 我们提供了有史以来第一份关于 AI 使用在美国各州之间如何不同的详细评估。我们发现，各州的经济构成决定了哪些州人均使用 Claude 最多——而且令人惊讶的是，使用率最高的州_并非_编码占主导地位的州。
  * **……在不同国家之间：** 我们的新分析发现，各国对 Claude 的使用与收入密切相关，而且使用率较低国家的人们使用 Claude 进行工作自动化的频率_高于_使用率较高的国家。
  * **……随时间变化：** 我们将最新数据与 [2024 年 12 月至 2025 年 1 月](<https://www.anthropic.com/news/the-anthropic-economic-index>)和 [2025 年 2 月至 3 月](<https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7>)的数据进行了比较。我们发现，「指令式」自动化任务的比例从 27% 急剧上升到 39%，表明 AI 的责任（以及用户的信任）在快速增加。
  * **……以及按企业用户划分：** 我们现在纳入了 Anthropic 第一方 API 客户的匿名数据（除了 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 的用户之外），使我们能够首次分析企业的交互。我们发现，API 用户使用 Claude 自动化任务的可能性显著高于消费者，这表明重大的劳动力市场影响可能即将到来。

我们在下方总结了[这份报告](<http://anthropic.com/research/anthropic-economic-index-september-2025-report>)。此外，我们设计了一个[交互式网站](<http://anthropic.com/economic-index>)，你可以在其中自行探索我们的数据。有史以来第一次，你可以搜索 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 使用在每一个美国州和所有我们追踪的职业中的趋势和结果，看看 AI 在你居住的地方或与你从事类似工作的人那里是如何被使用的。最后，如果你想在我们的分析基础上继续构建，我们已经将数据集[公开发布](<https://huggingface.co/datasets/Anthropic/EconomicIndex>)，连同我们之前经济指数报告的数据一起。

## **地理分布**
我们扩展了 Anthropic 经济指数，纳入了地理数据。下面我们介绍关于 Claude 如何在各国和美国各州被使用的发现。

### 国家之间
美国使用 Claude 的程度远超其他任何国家。印度位居第二，其次是巴西、日本和韩国，各自的份额相近。

![按全球 Claude 使用份额排名的前 30 个国家：美国以 21.6% 领先。](assets/economic-index-geography/img_001.img)全球 Claude.ai 使用份额领先的国家。

然而，这些国家的人口规模差异巨大。为了考虑这一点，我们用每个国家在世界劳动人口中的份额来调整其在 Claude.ai 使用中的份额。这就得到了我们的 **Anthropic AI 使用指数**（Anthropic AI Usage Index，AUI）。AUI 大于 1 的国家，其使用 Claude 的频率高于仅根据其适龄劳动人口所预期的水平，反之亦然。

![在我们的 Anthropic AI 使用指数上得分最高的二十个国家：以色列、新加坡、澳大利亚、新西兰和韩国位列前五。](assets/economic-index-geography/img_002.img)在我们的 Anthropic AI 使用指数上得分最高的二十个国家。

从 AUI 数据中，我们可以看到一些较小的、技术先进的国家（如以色列和新加坡）在相对于其适龄劳动人口的 Claude 采用方面领先。这在很大程度上可能可以用收入来解释：我们发现人均 GDP 与 Anthropic AI 使用指数之间存在很强的相关性（人均 GDP 每高 1%，AUI 就高 0.7%）。这很合理：最常使用 Claude 的国家通常也拥有强劲的互联网连接，以及以知识工作而非制造业为导向的经济。但这确实提出了一个经济分化的问题：以往的通用技术，如电气化或内燃机，既带来了巨大的经济增长，也导致了世界各地生活水平的[大分流](<https://www.aeaweb.org/articles?id=10.1257/jep.11.3.3>)。如果 AI 的效应在较富裕国家被证明最大，这种通用技术可能具有类似的经济影响。

![图表显示各国人均 Claude 使用量与人均收入呈正相关。](assets/economic-index-geography/img_003.img)各国人均 Claude 使用量与人均收入呈正相关。（坐标轴为对数刻度。）

### 美国境内的模式
人均 GDP 与人均 Claude 使用量之间的联系在美国各州之间进行比较时也同样成立。事实上，在美国境内，使用量随收入的增长比国家之间更快：美国境内人均 GDP 每高 1%，人口调整后的 Claude 使用量就高 1.8%。话虽如此，在美国境内，收入对使用量的_解释力_实际上比国家之间更低，因为总体趋势内的方差要大得多。也就是说：除了收入之外，其他因素必须解释人口调整后使用量的更多变化。

还有什么可以解释这种采用差距呢？我们最好的猜测是各州经济构成的差异。美国 AUI 最高的是哥伦比亚特区（3.82），在那里，Claude 的使用频率最不成比例地高的用途是编辑文档和搜索信息，以及华盛顿特区知识工作相关的其他任务。类似地，与编码相关的任务在加利福尼亚州（AUI 总体排名第三的州）尤其常见，而与金融相关的任务在纽约（排名第四）尤其常见。[1] 即使在人口调整后 Claude 使用量较低的州，如夏威夷，使用情况也与经济结构密切相关：夏威夷人请求 Claude 协助旅游相关任务的频率是美国其他地区的两倍。我们的[交互式网站](<http://anthropic.com/economic-index>)包含大量其他此类统计数据。

![图表显示美国各州相对于其适龄劳动人口的 Claude 采用情况，犹他州和哥伦比亚特区领先。](assets/economic-index-geography/img_004.img)美国各州相对于其适龄劳动人口的 Claude 采用情况。

## **Claude 使用趋势**
自 2024 年 12 月以来，我们一直在追踪人们如何使用 Claude。我们使用一种保护隐私的[分类方法](<https://www.anthropic.com/research/clio>)，将匿名化对话记录归类到由 O*NET（一个对工作及相关任务进行分类的美国联邦政府数据库）定义的任务组中。[2] 通过这样做，我们可以分析人们交给 Claude 的任务自去年以来发生了怎样的变化，以及人们选择协作的方式——他们选择对 Claude 的工作施加多少监督和输入——发生了怎样的变化。

### 任务
自 2024 年 12 月以来，计算机和数学类的 Claude 使用在我们的类别中一直占主导地位，约占对话的 37-40%。

但很多事情都变了。在过去九个月里，我们看到「知识密集型」领域持续增长。例如，教育指导任务增长了 40% 以上（占所有对话的比例从 9% 上升到 13%），与物理和社会科学相关的任务份额增加了三分之一（从 6% 上升到 8%）。与此同时，传统商业任务的相对频率有所下降：管理相关任务从占所有对话的 5% 下降到 3%，与商业和金融运营相关的任务份额减半，从 6% 下降到 3%。（当然，按绝对值计算，每个类别的对话数量仍然大幅上升。）

![Claude 使用随时间的变化，显示科学和教育任务的使用增加，艺术、商业和建筑用途减少。](assets/economic-index-geography/img_005.img)Claude 使用随时间的变化，显示科学和教育任务的使用增加。

总体趋势很嘈杂，但一般来说，随着一个国家人均 GDP 的增加，Claude 的使用会_远离_计算机和数学职业组的任务，转向各种其他活动，如教育、艺术和设计；办公和行政支持；以及物理和社会科学。将下面第一个图中的趋势线与其余三个图进行比较：

![计算机和数学、教育指导、艺术、办公和行政任务的职业组份额与 Anthropic AI 使用指数的对比。](assets/economic-index-geography/img_006.img)随着我们从采用率较低的国家转向采用率较高的国家，Claude 的使用似乎转向了更多样化的任务组合，尽管总体模式是嘈杂的。

话虽如此，软件开发仍然是我们追踪的每个国家中最常见的用途。美国的情况看起来类似，尽管我们的样本量限制了我们更详细地探索任务组合如何随采用率变化的能力。

### 交互模式
正如我们[之前讨论过的](<https://www.anthropic.com/news/the-anthropic-economic-index>)，我们通常区分涉及_自动化_（automation，AI 以最少用户输入直接产出工作）和_增强_（augmentation，用户与 AI 协作完成事情）的任务。我们进一步将自动化细分为_指令式_（directive）和_反馈循环_（feedback loop）交互，其中指令式对话涉及最少的人类交互，而在反馈循环任务中，人类将现实世界的结果反馈给模型。我们还将增强细分为_学习_（learning，索取信息或解释）、_任务迭代_（task iteration，与 Claude 协作工作）和_验证_（validation，征求意见反馈）。

自 2024 年 12 月以来，我们发现指令式对话的份额急剧上升，从 27% 上升到 39%。其他交互模式（尤其是学习、任务迭代和反馈循环）的份额因此略有下降。这意味着自动化（49.1%）首次整体上比增强（47%）更常见。一个可能的解释是，AI 正在迅速赢得用户的信任，并越来越多地负责完成复杂的工作。

这可能是模型能力提升的结果。（2024 年 12 月，当我们首次为经济指数收集数据时，Claude 的最新版本是 Sonnet 3.6。）随着模型在预测用户需求和产出高质量工作方面变得更好，用户可能更愿意在第一次尝试时就信任模型的输出。

![图表显示从我们的第一期到第三期指数报告中，自动化超过增强。](assets/economic-index-geography/img_007.img)自动化似乎随时间在增加。

也许令人惊讶的是，在人均 Claude 使用量较高的国家，Claude 的用途倾向于增强，而使用量较低国家的人们则更倾向于自动化。在控制任务组合的情况下，人口调整后 Claude 使用量每增加 1%，与自动化减少约 3% 相关。类似地，人口调整后 Claude 使用量的增加与_远离_自动化（如下面的图表所示）而非趋向自动化相关。

我们还不太确定这是为什么。这可能是因为每个国家的早期采用者对让 Claude 自动化任务感觉更自在，也可能归结于其他文化和经济因素。

![图表显示人均 Claude 使用量较高的国家，自动化任务份额往往较低。](assets/economic-index-geography/img_008.img)人均 Claude 使用量较高的国家倾向于以更具协作性的方式使用 Claude。

## **企业**
使用与我们用于 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 对话相同的保护隐私[方法](<https://www.anthropic.com/research/clio>)，我们开始对 Anthropic 第一方 API 客户的一个子集的交互进行抽样，这是一项首创性的分析。[3] API 客户（通常是企业和开发者）使用 Claude 的方式与通过 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 访问的用户截然不同：他们按代币付费，而不是按月订阅，并且可以通过自己的程序发出请求。

这些客户对 Claude 的使用尤其集中在编码和行政任务上：我们样本中 44% 的 API 流量映射到计算机或数学任务，而 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 上此类任务占 36%。（碰巧的是，大约 5% 的 API 流量专门用于开发和评估 AI 系统。）与之对应的是，与教育职业相关的对话比例较小（API 中为 4%，而 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 上为 12%），艺术和娱乐相关对话也较少（5% 对 8%）。

我们还发现，我们的 API 客户使用 Claude 进行任务自动化的频率远高于 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 用户。我们 77% 的 API 对话显示出自动化模式，其中绝大多数是指令式的，而只有 12% 显示增强。在 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 上，这一比例几乎持平。这可能会产生重大的经济影响：在过去，任务自动化一直与大规模的经济转型以及重大的生产力提升相关联。

![图表显示 Claude.ai 上的增强型用途份额远高于 API，而自动化用途则相反。](assets/economic-index-geography/img_009.img)[Claude.ai](<http://claude.ai>) 与 API 上使用 Claude 的增强和自动化情况。

最后，由于 API 使用是按量付费的，我们还可以探索任务成本的差异（由它们消耗的代币数量差异引起）是否会影响企业选择「购买」哪些任务。在这里，我们发现价格和使用之间存在_正_相关：成本较高的任务类别往往使用更频繁，如下面的图表所示。这让我们认为，模型的基本能力和模型产生的经济价值对企业来说，比完成任务本身的成本更重要。

![图表显示职业类别的使用份额与平均 API 成本。](assets/economic-index-geography/img_010.img)每个任务的成本与该任务类别占总对话份额的关系图。

## **结论**
经济指数旨在提供对 AI 如何影响人们的工作和经济的早期实证评估。到目前为止我们发现了什么？

在我们本报告涵盖的每一项衡量指标中，AI 的采用都显得极不均衡。高收入国家的人们更可能使用 Claude，更可能寻求协作而非自动化，也更可能追求编码之外的各种用途。在美国境内，AI 的使用似乎受到当地经济中主导产业的强烈影响，从科技到旅游。而企业比消费者更愿意把自主权和能动性托付给 Claude。

除了不均衡这一事实之外，我们特别注意到的是，在过去九个月里，指令式自动化在 [Claude.ai](<http://claude.ai/redirect/website.v1.88c07d8f-6506-4ef1-a005-386dc2f923fd>) 的对话中变得更加普遍。人们使用 Claude 的性质显然仍在被定义中：我们仍在集体决定我们对 AI 工具有多大信心，以及我们应该赋予它们多少责任。不过到目前为止，看起来我们正变得越来越习惯于 AI，并愿意让它为我们工作。我们期待随着时间的推移重新审视这一分析，看看用户的选在 AI 模型改进后会在哪里——或者，实际上，_是否_会——稳定下来。

如果你想自己探索我们的数据，可以访问我们专门的 [Anthropic 经济指数网站](<http://anthropic.com/economic-index>)，其中包含我们国家、州和职业数据的交互式可视化。我们未来将用更多数据更新这个网站，这样你就可以继续以你感兴趣的方式追踪 AI 对工作和经济影响的演变。

我们的完整报告[可在此处获取](<http://anthropic.com/research/anthropic-economic-index-september-2025-report>)。我们希望它能帮助政策制定者、经济学家和其他人更有效地为 AI 带来的经济机遇和风险做好准备。

## **开放数据**
与我们过去的报告一样，我们为本次发布发布了一个全面的数据集，包括地理数据、任务层面使用模式、按任务划分的自动化/增强细分，以及 API 使用概览。数据可在 [Anthropic 经济指数网站](<http://anthropic.com/economic-index>)下载。

## **与我们合作**
如果你有兴趣在 Anthropic 工作，帮助构建支撑这项研究的系统，我们鼓励你申请我们的[研究工程师](<https://job-boards.greenhouse.io/anthropic/jobs/4816634008>)职位。

#### 脚注
1. 至于排名第二的犹他州：在进一步调查犹他州的活动时，我们发现其使用的相当大一部分似乎与协同滥用的指标有关——这也反映在犹他州的「指令式」自动化得分远高于平均水平上。不过，我们进行了稳健性检验，并相信这些活动并没有驱动结果。
2. 我们辅以一种「自下而上」的任务分类，即 Claude 根据其自身的分类法对对话进行分类，以弥补 O*NET 类别中的任何空白。我们保护隐私的分析方法的完整细节可[在此处](<https://www.anthropic.com/research/clio>)获取。
3. 本节的数据涵盖 2025 年 8 月的 100 万份记录，从一组第一方 API 客户中随机抽样，这些客户约占我们第一方 API 使用量的一半。我们继续根据我们的隐私和保留政策管理数据，我们的分析符合我们的条款、政策和合同约定。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/economic-index-geography>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/economic-index-geography>)
## 相关内容
### 了解更多关于 Claude 数学能力的信息
Claude 的一个未发布的研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的一个长期未破的下界，将其从 41.6% 提高到 67.2%。
[了解更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二个攻击发现了一种攻击轮数缩减的 AES（使用最广泛的对称密码）的新方法。
[了解更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能操控无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估来测试 AI 模型使用飞行无人机的能力，最终形成了一个新的基准：Drone-Bench。
[了解更多](</research/project-pilot>)