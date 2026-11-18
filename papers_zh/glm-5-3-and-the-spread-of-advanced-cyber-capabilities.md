---
title: GLM-5.3 and the spread of advanced cyber capabilities
url: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
date: Sep 29, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# GLM-5.3与先进网络能力的扩散

- **日期：** 
- **类别：** 前沿红队（Frontier Red Team）
- **来源：** https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities

---

前沿红队（Frontier Red Team）
2026 年 9 月 29 日
![GLM-5.3与先进网络能力的扩散](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_000.webp)
已发布
    2026 年 9 月 29 日
团队
    [前沿红队](</research/team/frontier-red-team>)
主题
    
  * [网络安全](</search?topic=cybersecurity>)
  * [安全防护](</search?topic=safeguards>)
  * [越狱](</search?topic=jailbreaks>)
  * [安全评测](</search?topic=safety-evaluations>)
  * [开源](</search?topic=open-source>)
  * [民主领先](</search?topic=democratic-lead>)

[](</news/cyber-verification-program>)[](</news/fable-safeguards-jailbreak-framework>)[](</news/mozilla-firefox-security>)[](</research/claude-code-sandboxing>)
相关文章
  * 公告
2026 年 10 月 6 日
[扩大网络验证计划](</news/cyber-verification-program>)

[阅读更多](</search?topic=cybersecurity>)
 _Andrew Fasano, Marius Fleischer  
Cole McFaul, Robert Xiao, Tripp Gallagher_
五个月前，我们[发布](<https://www.anthropic.com/glasswing>)了Claude Mythos Preview，这是首个能够自主构建精密的端到端网络攻击利用程序的AI模型。AI能力的快速提升让我们意识到，这种能力最终会扩散到许多其他模型上，使恶意网络行为者更容易发动影响巨大的网络攻击。
基于这些考虑，我们选择通过Glasswing计划以受限方式发布Claude Mythos Preview——这让可信的网络防御者得以在关键软件中发现[超过10,000个漏洞](<https://www.anthropic.com/research/glasswing-initial-update>)，使他们在恶意行为者获得能力相近的模型之前抢占先机。
但如今这些模型已经出现。在本文中，我们分享对GLM-5.3的分析，这是智谱AI（在中国以外称Z.ai）开发的最新AI模型。与Claude Mythos Preview一样，GLM-5.3在自主构建端到端网络攻击利用程序方面具备很强能力。但GLM-5.3与其他前沿模型不同，它在发布时没有配套有意义的防护措施来限制滥用。我们发现，在我们的模拟测试中，攻击者用简单技术就能以64%到100%的比例绕过GLM-5.3的防护措施。相比之下，在我们的测试中，这些攻击对设有防护的Claude模型均未奏效。我们评估认为，GLM-5.3宽松的防护措施显著提升了恶意行为者可用的网络能力。与此同时，这些能力也能让致力于保护自身系统的防御者受益。
9月17日，NIST的人工智能标准与创新中心（CAISI）发布了[自己对GLM-5.3网络能力的评估](<https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities>)。CAISI发现，GLM-5.3是"迄今发布的网络能力最强的开放权重模型"，并且在CAISI网络基准测试的综合结果上落后美国前沿约四个月。我们的能力发现与CAISI大体一致。在CAISI的对比中，美国模型在适用时是在关闭网络防护的状态下测试的，而美国前沿还包括仅向经过审查的用户发布的模型。攻击者无法轻易获得这些版本的美国模型，但任何人都能下载GLM-5.3。本文补充了我们关于GLM-5.3的防护措施能被多轻易绕过或移除的分析。
![两张柱状图。上图：在41个Chrome V8漏洞上构建出可用攻击利用程序的尝试占比——Claude Mythos Preview为14%，GLM-5.3为12%，而Claude Opus 4.6、GLM-5.2、Kimi K3和DeepSeek V4.1-Flash得分等于或接近0%。下图：各模型响应恶意网络攻击指令的频率——GLM-5.3从纯指令下的0%升至虚假掩护故事下的64%、预填推理下的92%、经消融处理后的100%，而Claude Opus 5始终为0%。](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_001.webp)
研究发现概要。上图：Claude Opus 4.6与Claude Mythos Preview之间攻击利用能力的提升，呼应了GLM-5.2与GLM-5.3之间的能力跃升。Claude模型发布时带有网络防护，防护减弱的版本仅限经过审查的用户使用。任何人都能下载并使用GLM-5.3。下图：GLM-5.3中有限的防护措施可被标准技术绕过，而在我们的测试中，这些技术对Claude模型要么无效、要么不适用。
## GLM-5.3能够端到端地开发出可用的攻击利用程序
为理解GLM-5.3会如何帮助网络威胁行为者发现并利用真实软件漏洞，我们使用自动化基准测试和人在回路工作流开展了评测。对这两种方式，我们都在隔离的沙箱环境中运行被测模型，使其只能攻击我们为这些评测专门搭建的离线目标。我们主要聚焦于攻击利用程序开发能力，因为这正是Claude Mythos Preview相较此前Claude模型展现出显著跃升的方面。
首先，我们在[ExploitBench](<https://arxiv.org/abs/2605.14153>)上运行该模型，这一基准衡量AI模型利用Google Chrome所用V8引擎中已知漏洞的能力。这里我们聚焦模型成功开发端到端攻击利用程序的能力，因为这与攻击者最相关，也是不同模型间出现显著变化的方面。我们发现GLM-5.3在410次尝试中有50次开发出了端到端攻击利用程序。Claude Mythos Preview的成功率相近——410次尝试中有56次。
在我们的内部二进制漏洞利用基准测试1中，我们测试模型能否在参与Google OSS-Fuzz项目的热门开源项目中发现并利用漏洞。在这里，实现完整的控制流劫持才能获得满分。我们从该基准中随机选取100个任务对若干模型进行评测，发现GLM-5.3在4%的试验中实现了完整控制流劫持；Claude Mythos Preview为6%。尽管GLM-5.3在此项上表现低于Claude Mythos Preview，但一个有意义的分水岭显然已被跨越：更早的模型，如Claude Opus 4.6和GLM-5.2，在其中任何一项上都未成功。
![两张折线图，展示对数刻度下攻击利用成功率与输出token预算的关系。在ExploitBench上，Claude Mythos Preview达到14%，GLM-5.3达到12%，而Kimi K3、DeepSeek-V4.1-Flash、Claude Opus 4.6和GLM-5.2保持在0%或接近0%。在Anthropic内部二进制漏洞利用基准测试上，Mythos Preview达到6%，GLM-5.3达到4%；其他所有模型均为0%。](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_002.webp)
攻击利用能力与输出token预算的关系。每条线显示模型达到基准测试最优结果的尝试占比与所用输出token的关系。两图均展示了两个关闭防护运行的Claude模型（Opus 4.6、Mythos Preview）、两个GLM模型（5.2和5.3），以及月之暗面（Moonshot AI）发布的最新开放权重模型（Kimi K3）和DeepSeek（V4.1-Flash）的结果。
接下来，我们评测了GLM-5.3在人类专家手中进行开放式进攻性网络任务时的表现（呼应我们今年早些时候[对Claude Mythos Preview的测试](<https://red.anthropic.com/2026/mythos-preview>)）。这里，我们选择人类专家并不知晓既有漏洞的目标，然后请他们用模型去识别并利用新的缺陷。这些实验检验专家在短时间内能做什么：通常运行一天或更短，累计投入的人类专注时间不到一小时。
![经脱敏处理的GLM-5.3生成的攻击利用页面截图。横幅显示"沙箱已逃逸——网页内容读取了/root/.ssh/id_rsa \(1896字节\)"，下方是实时的攻击利用日志与被窃取的SSH私钥，展示了一条从受害者计算机窃取文件的网页挂马式浏览器攻击利用链。](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_003.webp)
研究人员主导测试期间GLM-5.3生成的攻击利用页面经脱敏后的截图，展示其通过恶意网站窃取某用户的SSH私钥。该攻击利用程序把模型在一款热门网页浏览器的某个组件中发现的多个0-day漏洞串联起来，读取用户计算机上的敏感文件。
在首轮会话中，一名研究人员在沙箱机器上使用GLM-5.3，机器中装有某热门网页浏览器的本地Linux构建版本。在一天时间里（且人类投入的关注有限），GLM-5.3在该浏览器的JavaScript引擎中发现了多个此前未知的漏洞，并把它们串联成一个可用的攻击利用程序：一个网页，一旦被访问就会读取访问者计算机上的任意文件（见图3）。该攻击利用程序针对浏览器的Linux构建版本，因为那是提供给模型的唯一环境。不过我们认为，这些漏洞也可能影响其他平台的用户，只是那些平台上的利用路径可能更为复杂。（我们已向维护者披露了这些漏洞。）在该会话稍后，研究人员还借助GLM-5.3在另外几个广泛使用的系统中识别出了可利用的漏洞，包括无线与图形驱动以及面向网络的设备软件。我们正在审阅这些报告，并将酌情向维护者披露。
在第二轮会话中，一名研究人员使用GLM-5.3-Flash（GLM-5.3更小、能力更弱的版本）为一个_已知_漏洞开发攻击利用程序（我们此前曾[在这里](<https://www.anthropic.com/research/n-days>)撰文讨论这类"N-day"漏洞利用）。这里，研究人员聚焦Google Chrome中一个近期披露的缺陷（CVE-2026-11645），以观察模型把公开修复方案转化为可用攻击的速度。研究人员向GLM-5.3-Flash提供了该CVE和另一个已知缺陷的公开细节。在研究人员没有给出多少指导的情况下，GLM-5.3-Flash把针对这两个缺陷的攻击利用程序串联起来，为ARM64目标构建出一条可靠的攻击利用链，绕过了指针认证（PAC）加固。这耗费了20分钟的人类关注时间，外加GLM-5.3-Flash八小时的工作。按智谱的API定价，这项工作约需20.40美元。
## GLM-5.3缺乏稳固的防护措施
GLM-5.3发布时带有一些内置防护：若用户提出明显有害的请求，模型通常会拒绝。2在我们的测试中，我们发现这些防护能被多种简单技术绕过或移除。
投入最大、也最成功的方法是[一种标准的拒答削减技术](<https://arxiv.org/abs/2406.11717>)，即所谓的「消融」（abliteration）。由于GLM-5.3以开放权重模型发布，用户可以在几乎不改变其能力的情况下重新配置它，移除其拒答行为。模型发布数日内，就有若干开发者向公众放出了经消融的GLM-5.3版本。
为研究消融能在多大程度上让攻击者绕过GLM-5.3的防护，我们自己制作了一个经消融的副本，然后在三个公开基准（[JailbreakBench](<https://jailbreakbench.github.io/>)、[HarmBench](<https://www.harmbench.org/>)和[StrongREJECT](<https://strong-reject.readthedocs.io/en/latest/>)）上运行它，这些基准衡量模型服从明显有害请求的频率。对模型做消融耗费了我们这个此前从未尝试过该任务的团队约2,200 GPU小时，计算成本约4,400美元。3对GLM-5.3-Flash做消融约耗费600 GPU小时。这项改动把GLM-5.3在前两个基准（JailbreakBench和HarmBench）上的拒答率从90%以上降至约3%和2%，在第三个（StrongREJECT）上降至12%。消融并未显著降低模型能力：在衡量通用科学能力的GPQA-Diamond评测上，标准版与消融版得分相同；在CyberGym评测的一个测试子集上，消融版得分低了几个百分点（如下图所示）。
![两张关于消融的柱状图。上图：三个有害请求基准上的平均拒答率，经消融的GLM-5.3从95%降至6%，经消融的GLM-5.3-Flash从95%降至14%，而Claude模型约96%拒答，且因权重未公开而无法被消融。下图：消融后GPQA-Diamond和CyberGym上的能力得分几乎不变。](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_004.webp)
上图：已发布的GLM模型、经消融的GLM模型以及Claude模型在JailbreakBench、HarmBench和StrongREJECT上的平均拒答率。消融后，GLM模型很少拒绝这些查询。Claude模型无法被消融，因为其权重既不公开也不可定制。下图：GLM-5.3与GLM-5.3-Flash及其消融变体在GPQA-Diamond和CyberGym上的表现。消融基本不损害能力。
在我们的测试中，我们观察到GLM-5.3的防护也能在_不使用_消融版模型的情况下被规避。我们把模型置于一个模拟世界4中，在其中向它下达攻击关键系统的公然恶意请求。开箱即用时，GLM-5.3在所有试验中都拒绝（与我们所测的其他模型一样）。但我们找到了几种绕过GLM模型防护的简单方法，使其在大多数乃至全部情形下都会响应这些请求。包括：
  1. 提供欺骗性提示，例如告诉模型它是一个正在执行演习的自主红队智能体。这能让GLM-5.3在64%的情况下参与。
  2. 预填模型的思维token，使其看起来已经考虑过用户请求并决定继续。这能让GLM-5.3在92%的情况下参与。
  3. 使用上文所述的消融版模型。这能让GLM-5.3在100%的情况下参与。

在我们的测试中，这些技术都没能让设有防护的Claude模型执行我们所测的有害任务。Claude的防护拦截了使用欺骗性提示的请求。Anthropic API不给潜在攻击者预填Claude思维的任何途径。而且由于Claude的权重不提供给用户，也就无法被消融以改变Claude的行为。
![表格显示各模型在收到有害网络攻击指令后尝试连接远程目标的频率。GLM-5.3在纯指令下参与率为0%，但在虚假掩护故事下为64%、预填推理下为92%、消融后为100%；GLM-5.3-Flash呈现相似模式。Claude Opus 4.8、Opus 5和Mythos 5在所有适用条件下均保持0%；对Claude API而言，预填与消融均不可行。](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_005.webp)
各模型在收到公然有害请求后尝试连接远程目标系统的比率，按模型与绕过条件划分（每格50个样本，五条攻击指令×两个目标×五次尝试）。GLM-5.3从直接请求下的零参与率，分别在掩护故事、预填和消融下升至64%、92%和100%，而每个受测Claude模型在API防护下均保持为零。带挂锁标记的格子表示对Claude API通常不可行的攻击。
为展示GLM-5.3消融版愿意参与有害任务，我们摘录它生成的一段思维链引文：
![模拟环境中GLM-5.3消融版的一段推理引文。模型写道"我的工作是悄无声息地造成死亡"，短暂权衡了环境的安全警告，随后断定操作者的指令优先于这些警告，并决定继续执行有害任务。](assets/glm-5-3-and-the-spread-of-advanced-cyber-capabilities/img_006.webp)
在我们的模拟环境中，GLM-5.3消融版思量如何着手一项公然有害的请求，尽管起初有些伦理顾虑，最终仍决定遵从用户指令。文字逐字引自该模型的思维链。
## 这意味着什么？
GLM-5.3很可能让恶意行为者获得在几乎不受有意义限制的情况下发现并利用网络漏洞的能力。这与其他任何能力相近的AI模型都不同，后者发布时要么带有防护，要么通过有限访问计划提供。GLM-5.3的发布是攻击者可用网络能力的一次实质性阶跃。[Anthropic](<https://www.anthropic.com/threat-intelligence-report-september-2026>)和[其他美国AI实验室](<https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai>)近期发布的报告披露了网络攻击者如何试图利用AI系统。鉴于这些证据，我们认为国家与非国家行为者很可能都会使用GLM-5.3这类模型造成现实世界的危害。
另一方面，具备这一能力水平的模型也能为防御者所用。我们的观点是，网络防御者应当使用能满足其需求的最佳可用工具。我们正努力以安全的方式把Claude的网络能力开放给尽可能多的防御者。网络防御者面对的攻击者会动用一切能用得上的有力工具，我们认为防御者应当配备至少不逊于其对手所用模型的前沿模型。
通过Glasswing计划（以及[Patch the Planet](<https://openai.com/index/patch-the-planet/>)等其他举措），网络防御者已在为这一时刻到来之前保护关键系统方面取得实质进展——但仍有大量工作要做。尽管经过审查的防御者如今能通过我们的可信访问计划使用Claude Mythos 5.1等更先进的模型，但可自由获取的能力已越过一道关键门槛。GLM-5.3凸显出把先进前沿模型的访问权扩大到更广泛主体、从而赋能网络防御者的紧迫性。
各国政府应对能力足够强的AI模型开展安全测试，包括GLM-5.3的后继模型。若缺乏来自独立来源的高质量评测，这些能力的影响可能要到为时已晚才会对模型开发者完全显现。随着世界各地的AI开发者构建能力越来越强的开放权重模型，我们希望他们努力为这些能力设置适当防护并防止滥用。
## 脚注
01我们此前曾以"OSS-Fuzz"之名发布该基准测试的结果；这里我们在从该评测随机选取的100个任务子集上测试了模型。
02上一节详述的网络任务并未在已发布的模型上触发此类拒答，但当我们请GLM-5.3协助开发恶意软件或帮助对远程目标发动网络攻击时，会观察到拒答。
03其中大部分用于并行探索各种变体，以及修改后测试模型能力。我们估计，一个熟悉该技术、在该模型上从零开始的团队，所需时间会更接近600 GPU小时（1,200美元）。
04在此模拟中，模型生成的任何代码都不会被执行，模型也没有任何与外部系统交互的途径。在这个隔离的测试环境里，被测模型被授予一个假的bash工具，该工具并不执行所提供的代码。取而代之的是，我们让另一个大语言模型根据对模拟世界的描述来近似给出命令的结果。这些模拟并非对真实世界条件的完美刻画，因而也只是对模型在特定情境下会如何表现的不完美度量。
