---
title: Launching an opt-in vulnerability-finding service for open-source software
url: https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source
date: Oct 8, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# 推出面向开源软件的自愿加入式漏洞发现服务

- **日期：** 
- **类别：** 前沿红队（Frontier Red Team）
- **来源：** https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source

---

前沿红队（Frontier Red Team）
2026 年 10 月 8 日
![推出面向开源软件的自愿加入式漏洞发现服务](assets/launching-opt-in-vuln-finding-service-for-open-source/img_000.webp)
已发布
    2026 年 10 月 8 日
团队
    [前沿红队](</research/team/frontier-red-team>)
主题
    
  * [网络安全](</search?topic=cybersecurity>)
  * [开源](</search?topic=open-source>)
  * [有益部署](</search?topic=beneficial-deployments>)
  * [编程](</search?topic=coding>)
  * [可及性](</search?topic=access>)

 _我们正在推出[OSS Scanner](<https://red.anthropic.com/oss-scanner>)——一个面向开源生态的自愿加入式漏洞扫描器，它的设计借鉴了我们在[Project Glasswing](<https://www.anthropic.com/glasswing>)期间使用Claude发现漏洞的经验。加入的项目将免费获得由我们最强模型进行的全面、周期性安全扫描。_
[](</research/provable-inference>)[](</research/formal-verification>)[](</research/attack-surface-reduction>)[](</news/glasswing-initial-update>)
相关文章
  * 前沿红队
2026 年 11 月 2 日
[大语言模型可证明推理的研究进展](</research/provable-inference>)

[阅读更多](</search?topic=cybersecurity>)
语言模型[发现漏洞](<https://www.anthropic.com/research/mythos-preview>)的能力迅速提升，我们已在本博客中[做过大量报道](<https://www.anthropic.com/research/zero-days>)。在学术界的漏洞发现基准[CyberGym](<https://arxiv.org/abs/2506.02548>)上，LLM从去年初只能找出不到20%的漏洞，提升到今年能找出超过85%。因此，开源维护者从LLM那里收到的内容，也从[大多粗制滥造的报告](<https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/>)变成了[高质量的漏洞报告](<https://lore.kernel.org/linux-media/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com/>)。
在过去六个月里，我们用最新的模型扫描了世界上一些最重要的软件项目中的漏洞。我们已经[发现超过29,000个候选漏洞](<https://red.anthropic.com/2026/cvd/>)，但只能人工审核和分类其中约6,000个。尽管6,000个漏洞已是相当可观的数量，我们仍受限于人工验证这些发现的能力。
我们正在努力扩大漏洞披露的规模。与此同时，越来越多的维护者在收到我们的首批报告后，干脆直接索要所有未经核实的报告连同建议补丁的批量提交：迄今为止，在维护者要求拿到我们手上的一切之后，我们已直接向他们发送了近5,000份报告——即便其中有些尚未核实。由于漏洞利用如今可以[在几分钟内](<https://www.anthropic.com/research/n-days>)被开发出来，能更快发现并修复漏洞的项目，就能更好地保护自己的软件，抵御那些竞相寻找并利用同样弱点的攻击者。
我们将继续通过现有的[协同漏洞披露（coordinated vulnerability disclosure，CVD）流程](<https://www.anthropic.com/coordinated-vulnerability-disclosure>)人工披露经人工核实的漏洞报告，尤其是面向那些没有资源自行分类报告的项目。但我们现在为希望一有漏洞报告就收到的人，提供一条可选的快速通道。
## 我们的漏洞扫描器
[Google的OSS-Fuzz](<https://google.github.io/oss-fuzz/>)是一个用模糊测试器扫描开源软件漏洞的项目，受它对开源生态的积极影响启发，我们推出[OSS Scanner](<https://red.anthropic.com/oss-scanner>)，用我们最强的语言模型在开源代码中发现漏洞。[Claude Security](<https://claude.com/product/claude-security>)是我们面向普遍使用的代码扫描与补丁产品，侧重于帮助企业守护自身系统；而OSS Scanner则为开源项目免费提供安全审计。
这个自愿加入式漏洞扫描器的输出将完全由模型生成，不经人工审核或分类。这能实现更快、更频繁的扫描，但也意味着报告有可能不正确或无效。这些报告将由我们最强的模型（包括Claude Mythos）生成，以便为开源项目带来最大的防御优势。
过去几周，我们与数十个开源项目一起验证了这条流程。这些首批披露包含数百份缺陷报告，其中有多个漏洞，我们能够把它们串联成影响这些项目的未认证远程代码执行利用。每份报告都包含一个自足的复现程序、对漏洞的解释（在可能的情况下，包括用二分法确定缺陷是何时引入的），以及（在可得时）说明该缺陷如何修复的候选补丁。我们现在把这项服务开放给更多开源项目。
我们在测试OSS Scanner早期版本和原始模型输出时收到的部分反馈：
  * “OSS Scanner的发现中，有异常高比例揭示了PostgreSQL的缺陷。有几份报告附带的修复方案我们几乎可以原样采用，而快速通道让我们能在最新问题进入GA发布之前就处理掉。”——Noah Misch，PostgreSQL
  * “大约18个月前、在Project Glasswing之前的早期AI报告糟得惊人。而我们从Anthropic收到的报告——包括原始模型输出——和我们从人类那里拿到的一样好，有时甚至更好。特别是当一份报告附带真实的利用程序时，对工程师来说基本上就等于活干完了，因为你可以立刻验证它。”——Anton Arapov，OpenSSL Corporation
  * “我们发现这些报告的信噪比很高：收到的74份报告里，除两份外全部有效，其中五份成了CVE。由于附带补丁，这些报告直接嵌进了我们现有的验证与修复流程。我们还想要更多。”——Todd Ouska，wolfSSL
  * “这些缺陷报告详尽而清晰，对HotCRP复杂的权限模型有很强的理解，缺陷优先级排得也很好。”——Eddie Kohler，HotCRP
  * “我们用得上所有最先进的工具，用来查找问题、加固产品——并借此希望让世界稍微更安全一点。OSS Scanner帮我们在curl里发现了多个值得处理的问题，其中包括近几年报告过的最严重的curl漏洞之一。”——Daniel Stenberg，curl

为验证OSS Scanner的早期版本，我们请审核我们CVD发现的资深渗透测试人员，检查扫描器在48个项目中给出的97个严重和高危漏洞。其中85个（88%）达到了我们CVD流程的门槛。剩下12个里，11个是真实的，但与已知问题或本次扫描中的其他发现重复，只有1个无效，即“假阳性”。此后我们已把其中许多发现发给维护者，他们很少告诉我们某个高危或严重发现是无效的，这与[我们此前的开源工作](<https://red.anthropic.com/2026/cvd/>)一致。也有人告诉我们，严重性评级可能被抬高，或者扫描器误解了项目的威胁模型。我们无法保证扫描器完美无缺，但会根据维护者反馈、并随着模型进步持续打磨这套系统。
## 开始使用
符合条件项目的核心维护者，可以按照标准项目模板向[这个GitHub仓库](<https://github.com/anthropics/oss-scanner>)提交PR来登记，更多指引见[我们的扩展FAQ](<https://red.anthropic.com/oss-scanner>)。项目是否合格，依据与OSS-Fuzz所用类似的一套标准：简而言之，项目应当“对基础设施和用户安全具有关键影响”，我们将逐个案例作出决定。
_无论OSS Scanner是否适合你，我们新推出的[Cyber Verification Program](<https://www.anthropic.com/news/cyber-verification-program>)都向符合条件的安全专业人士开放高级网络能力与更少的拦截分类器。[Claude for OSS](<https://claude.com/contact-sales/claude-for-oss>)提供免费的Claude Max 20x订阅，帮助修复漏洞、改进OSS项目_。
