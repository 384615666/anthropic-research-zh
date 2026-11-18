---
title: Project Glasswing: An initial update
url: https://www.anthropic.com/research/glasswing-initial-update
date: May 22, 2026
category: Announcements
source: https://www.anthropic.com/research
---

# Project Glasswing：初步进展更新

- **日期：** 
- **分类：** 公告（Announcements）
- **来源：** https://www.anthropic.com/research/glasswing-initial-update

---

公告（Announcements）
2026 年 5 月 22 日
![Project Glasswing：初步进展更新](assets/glasswing-initial-update/img_000.img)
上个月，我们启动了 [Project Glasswing](<https://www.anthropic.com/glasswing>)，这是一项协作计划，旨在日益强大的 AI 模型被用来攻击世界上最关键软件之前，先保障这些软件的安全。
自那以来，我们和大约 50 家合作伙伴使用 Claude Mythos Preview 在全球最具系统重要性的软件中发现了超过一万个高危或严重级漏洞。软件安全方面的进展过去受限于我们能多快发现新漏洞。现在，它受限于我们能多快验证、披露和修补 AI 发现的大量漏洞。
在这篇文章中，我们将讨论在 Project Glasswing 启动的最初几周里，我们对这个网络安全关键挑战的了解。我们聚焦于 Mythos Preview 性能的早期公开证据、我们扫描数千个开源软件项目工作的初步结果，以及这些进展对当今网络防御者意味着什么。我们还将介绍 Project Glasswing 接下来会做什么，以及我们如何思考未来发布 Mythos 级模型。
## 我们的早期成果
### 我们讨论 Mythos Preview 发现的方式
软件行业长期以来的惯例是在发现新漏洞 90 天后披露（或者，如果在 90 天到期前创建了补丁，则在补丁可用后约 45 天披露）。这为最终用户留出时间在攻击者利用漏洞之前更新软件。我们自己的[协调漏洞披露政策](<https://www.anthropic.com/coordinated-vulnerability-disclosure>)采用了这种做法。
然而，这意味着已披露的漏洞是 AI 模型网络能力加速发展前沿的一个滞后指标：我们还不能在不使最终用户面临风险的情况下完全详细披露合作伙伴使用 Mythos Preview 的发现。作为替代，我们提供模型性能的示例性说明，以及我们迄今为止进展的汇总统计。一旦 Mythos Preview 发现的漏洞补丁被广泛部署，我们将提供关于我们所学到的内容的更多细节。
### 来自合作伙伴和外部测试者的证据
Project Glasswing 的初始合作伙伴构建并维护着对互联网和其他关键基础设施运转至关重要的软件。修复其代码中的缺陷可以降低许多依赖该软件的组织的风险，从而降低数十亿最终用户的风险。
一个月后，大多数合作伙伴都在其软件中各自发现了数百个严重或高危漏洞。合计起来，他们发现了超过一万个。几位合作伙伴告诉我们，他们的漏洞发现速度提高了十倍以上。例如，[Cloudflare](<https://blog.cloudflare.com/cyber-frontier-models/>) 在其关键路径系统上发现了 2,000 个漏洞（其中 400 个为高危或严重级），其误报率被 Cloudflare 团队认为优于人类测试人员。
这与外部测试者对 Mythos Preview 性能的体验以及最近对该模型的额外评估相符：
  * **英国 AI 安全研究院** [报告](<https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing>)称，Mythos Preview 是第一个端到端解决其两个网络靶场（多步骤网络攻击的模拟）的模型；
  * **Mozilla** 在测试 Mythos Preview 时[发现并修复了](<https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/>) [Firefox 150 中的 271 个漏洞](<https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/>)——比他们使用 Claude Opus 4.6 在 Firefox 148 中发现的漏洞多十倍以上；
  * **XBOW**（一家独立安全平台）[报告](<https://xbow.com/blog/mythos-offensive-security-xbow-evaluation>)称，Mythos Preview 在其 Web 漏洞利用基准测试上是「对所有现有模型的显著升级」，并在逐 token 基础上提供了「绝对前所未有的精确度」；
  * [**ExploitBench**](<http://exploitbench.ai>) 和 [**ExploitGym**](<https://arxiv.org/abs/2605.11086>)（两个最近发布的用于衡量模型漏洞利用开发能力的学术基准测试）显示 Mythos Preview 是最强表现者。我们在[前沿红队博客](<https://red.anthropic.com/2026/exploit-evals/>)上更详细地讨论了这些基准测试告诉我们的信息。

更广泛地说，我们现在看到已修补的软件正被更快地推出。最新的 Palo Alto Networks 版本包含的补丁数量是平时的[五倍多](<https://www.paloaltonetworks.com/blog/2026/05/defenders-guide-frontier-ai-impact-cybersecurity-may-2026-update/>)。微软[已表示](<https://www.microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday>)，他们将发布的新补丁数量将「在一段时间内继续呈增长趋势」。而 Oracle 发现和修复其产品和云中漏洞的速度[比以往快数倍](<https://blogs.oracle.com/security/accelerating-vulnerability-detection-and-response-at-oracle>)。
Mythos Preview 还被证明对其他类型的安全工作很有用。例如，在我们的一家 Glasswing 合作银行，Mythos Preview 在威胁行为者入侵了客户电子邮件账户并进行假冒电话后，帮助检测并阻止了一笔 150 万美元的欺诈性电汇。
## 开源软件
在过去几个月里，Anthropic 使用 Mythos Preview 扫描了 1,000 多个开源项目，这些项目共同支撑着互联网的大部分——以及我们自己基础设施的很大一部分。
到目前为止，Mythos Preview 在这些项目中发现了它估计的 6,202 个高危或严重级漏洞（在总共 23,019 个漏洞中，包括它估计为中危或低危的漏洞）。
其中 1,752 个高危或严重级漏洞现在已由六家独立安全研究公司之一（或在少数情况下由我们自己）仔细评估。其中，90.6%（1,587 个）被证明是有效的真阳性，62.4%（1,094 个）被确认为高危或严重级。这意味着，即使 Mythos Preview 不再发现更多漏洞，按照我们目前分诊后的真阳性率，它也有望在开源代码中浮现近 3,900 个高危或严重级漏洞——这还不包括它为 Project Glasswing 合作伙伴发现的漏洞。需要明确的是，我们打算在一段时间内继续扫描开源代码，因此我们预计这个数字还会上升。
Mythos Preview 检测到的一个开源漏洞示例位于 [wolfSSL](<https://www.wolfssl.com/>)——一个以安全性著称、被全球数十亿设备使用的开源密码学库中。Mythos Preview [构建了一个漏洞利用](<https://www.wolfssl.com/how-claude-mythos-preview-helped-harden-wolfssl/>)，可让攻击者伪造证书，从而（例如）允许他们为银行或电子邮件服务商托管虚假网站。该网站对最终用户来说看起来完全合法，尽管它由攻击者控制。我们将在未来几周内发布对这个现已修补的漏洞（编号为 [CVE-2026-5194](<https://nvd.nist.gov/vuln/detail/CVE-2026-5194>)）的完整技术分析。
正如我们上面所指出的，_修复_此类漏洞的瓶颈是人类分诊、报告以及设计和部署补丁的能力。使用 Mythos Preview 首先发现漏洞已变得容易得多。我们创建了一个[我们扫描过的开源漏洞仪表板](<https://red.anthropic.com/2026/cvd/>)，如下所示，它显示了我们披露流程的不同步骤，并将跟踪我们随时间推移的进展。这显示了所有严重级别的漏洞，而不仅仅是 Mythos Preview 最初评估为高危或严重级的子集。请注意每个阶段的急剧下降，这反映了验证和修复每个漏洞所需的人力。
![](assets/glasswing-initial-update/img_001.img)我们的开源漏洞仪表板，显示所有严重级别的漏洞（而不只是 Mythos Preview 估计为高危或严重级的漏洞）。
我们分诊漏洞的过程是密集的。首先，我们或与我们合作的外部安全公司之一复现 Mythos 发现的问题，并重新评估其严重性。一旦我们确认漏洞是真实的，我们就会检查是否已有修复措施，并向软件维护者撰写详细报告。我们在这方面非常谨慎：除了维护开源软件的常规挑战之外，维护者还一直面临大量低质量的 AI 生成漏洞报告。事实上，几位维护者告诉我们，他们目前严重受制于能力限制，有些人甚至要求我们放慢披露速度，因为他们需要更多时间来设计补丁。（平均而言，Mythos Preview 发现的高危或严重级漏洞需要两周时间才能修补。）
应维护者的要求，我们有时会在没有进一步评估的情况下直接披露漏洞。我们现在已经报告了 1,129 个此类未经审查的漏洞，其中 Mythos Preview 估计 175 个为高危或严重级。
我们估计，到目前为止，我们已经向维护者披露了 530 个高危或严重级漏洞。这是基于直接披露情况下 Claude 对严重性的评估，以及可获得的情况下维护者或我们安全合作伙伴的评估。另有 827 个已确认的漏洞（以同样的方式估计为高危或严重级），我们正力争尽快披露。
在我们报告的 530 个高危或严重级漏洞中，已有 75 个得到修补，其中 65 个已发布公开通告。补丁数量仍然相对较低，原因有三。首先，我们仍处于[协调漏洞披露政策]中规定的 90 天窗口的早期阶段：我们预计很快会有更多补丁落地。其次，我们可能低估了补丁数量，因为有些漏洞在修补时没有公开通告：在这些情况下，我们依赖使用 Claude 自行扫描补丁。第三，补丁数量少反映了一个真实的问题：即使以我们相对较慢的披露速度，Mythos Preview 也在给本已超负荷的安全生态系统增加负担。
发现漏洞相对容易与修复漏洞的困难形成了网络安全方面的重大挑战。成功应对这一挑战将使我们的软件比以往安全得多。下面我们讨论网络防御者可以适应的几种方式。
## 适应网络安全的新阶段
拥有与 Mythos Preview 类似网络安全技能的模型很快就会更广泛地可用。软件行业显然需要更大规模的行动来管理这些模型将产生的大量发现。
目前，漏洞的发现、补丁的创建以及最终用户广泛部署补丁之间往往存在很长的滞后。这为攻击者利用关键软件留下了很大的窗口。Mythos 级模型大幅缩短了发现和利用漏洞所需的时间和成本，放大了这些时间滞后带来的风险。归根结底，Mythos 级模型将使开发人员能够在漏洞部署之前发现它们，从而构建远比现在更安全的软件。但在这个过渡时期——漏洞正被快速发现而补丁缓慢——出现了新的风险。
软件开发者和用户现在就应该采取行动，减少对这些风险的暴露。下面的建议并不新鲜，许多研究人员（包括 Anthropic 的研究人员）目前正在研究更好、更持久的解决方案。与此同时，把基础工作做对很重要：
  * **软件开发人员**应该缩短补丁周期，尽快提供安全修复。明智地使用公开可用的 AI 模型可以在这方面提供帮助；我们正在构建工具并分享我们的研究来支持这一点（更多细节见下文）。开发人员还应该通过让安装更新尽可能简单来帮助用户保持软件更新；在可行的范围内，他们应该对仍在运行已知漏洞软件的用户更加坚持。
  * **网络防御者**应该缩短补丁测试和部署的时间线。像[美国国家标准与技术研究院](<https://www.nist.gov/cyberframework>)和英国[国家网络安全中心](<https://www.ncsc.gov.uk/collection/10-steps/risk-management>)等组织列出的关键控制措施现在比以往任何时候都更加重要，因为它们在不依赖任何单个补丁及时落地的情况下提高了安全性。这些措施包括强化网络的默认配置、强制执行多因素认证，以及为检测和响应保留全面的日志。

### 使用公开可用的 AI 模型进行网络防御的工具
许多通用模型已经能够发现大量软件漏洞，即使它们无法发现最复杂的漏洞或像 Claude Mythos Preview 那样有效地利用它们。Project Glasswing 已经促使许多其他组织使用这些通用模型对自己的代码库采取行动；我们正在努力让这变得容易得多。
首先，我们已经面向 Claude Enterprise 客户以公开测试版发布了 [Claude Security](<https://claude.com/product/claude-security>)。这是一个帮助团队扫描代码库漏洞并为其生成建议修复的工具。自发布以来的三周内，Claude Opus 4.7 已被用来修补 2,100 多个漏洞。（这比上面描述的开源修补更快，在很大程度上是因为企业修复的是自己的代码，而开源修复通常需要志愿者维护者通过协调披露来工作。）
我们还启动了[网络验证计划](<https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude>)，该计划允许将我们的模型用于合法网络安全目的（如漏洞研究、渗透测试和红队测试）的安全专业人员使用模型，而无需受到某些旨在防止网络滥用的防护措施的约束。
现在，我们正把我们和合作伙伴与 Mythos Preview 一起使用的工具提供给符合条件的客户的安团队，供其按需申请。我们的目标是让用户无需大量设置就能更容易地从高能力公共模型中获得最佳性能。此次发布包括：
  * 我们和合作伙伴构建并分享的[技能](<https://code.claude.com/docs/en/skills>)（针对重复工作的自定义指令）；
  * 一个帮助 Claude 映射代码库、启动扫描子智能体、分诊其发现并撰写报告的框架（harness）；
  * 一个威胁模型构建器，用于映射代码库以识别潜在的攻击目标，并据此对模型的工作进行优先级排序。

我们的 Project Glasswing 合作伙伴之一 Cisco 最近也开源了其 [Foundry Security Spec](<https://blogs.cisco.com/ai/announcing-foundry-security-spec>)，以帮助其他防御者构建类似于他们自己使用的评估系统。
## 支持生态系统
我们与开源安全基金会（Open Source Security Foundation）的 Alpha-Omega 项目建立了[合作伙伴关系](<https://openssf.org/press-release/2026/03/17/linux-foundation-announces-12-5-million-in-grant-funding-from-leading-organizations-to-advance-open-source-security/>)，这将支持该基金会协助维护者处理和分诊漏洞报告的工作。我们还继续发表关于前沿模型能力如何最好地支持网络防御者的研究。
我们还支持了 [ExploitBench](<http://exploitbench.ai>) 和 [ExploitGym](<https://rdi.berkeley.edu/blog/exploitgym/>) 的开发——这两个新基准测试使研究人员能够跟踪前沿 AI 模型的漏洞利用开发能力随时间的变化，正如我们在[此处](<https://red.anthropic.com/2026/exploit-evals/>)讨论的那样。我们通过[外部研究人员访问计划](<https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program>)支持其他高质量定量基准测试的开发。最后，[Claude for Open Source](<https://claude.com/contact-sales/claude-for-oss>) 支持维护者和贡献者，我们承诺今后对我们自己采用的任何开源软件包进行扫描。
## Project Glasswing 的下一步
AI 进步的速度意味着，像 Mythos Preview 一样强大的模型很快将被许多不同的 AI 公司开发出来。目前，没有哪家公司——包括 Anthropic——开发出了足够强大的防护措施来防止此类模型被滥用并可能造成严重伤害。这就是我们尚未向公众发布 Mythos 级模型的原因。但这也是我们启动 Project Glasswing 的原因：如果能力相当的模型在_没有_此类防护措施的情况下发布，那么世界上几乎任何人都将很快能够以极低的成本和难度利用有缺陷的软件。
Glasswing 帮助最具系统重要性的网络防御者获得不对称优势。然而，迫切需要尽可能多的组织加强其网络防御。我们希望我们的通用模型，以及我们为配套提供的新工具、资源和研究，能够支持这些组织改善其网络安全态势。
接下来，我们将与关键合作伙伴——包括美国及其盟国政府——合作，将 Project Glasswing 扩展到更多合作伙伴。在不久的将来，一旦我们开发出所需的强得多的防护措施，我们期待通过公开发布的方式提供 Mythos 级模型。
在这些风险的另一端，有一个令人鼓舞的世界在等待着我们：一个关键代码比今天加固得好得多的世界，一个黑客行为远不那么普遍的世界。障碍重重，但我们仍然相信 Project Glasswing 能够帮助我们到达那里。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/glasswing-initial-update>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/glasswing-initial-update>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未公开发布的研究版 Claude 在与黎曼猜想（Riemann hypothesis）相关的问题上取得了进展。它改进了满足该猜想的黎曼 zeta 函数零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[了解更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二个攻击则发现了一种攻击轮数缩减版 AES（使用最广泛的对称密码）的新方法。
[了解更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作开发了一系列评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新的基准测试：Drone-Bench。
[了解更多](</research/project-pilot>)