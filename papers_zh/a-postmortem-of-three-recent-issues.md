---
title: A postmortem of three recent issues
url: https://www.anthropic.com/research/a-postmortem-of-three-recent-issues
date: Sep 17, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# 三起近期问题的复盘

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/a-postmortem-of-three-recent-issues

---

工程（Engineering）
2025 年 9 月 17 日
![三起近期问题的复盘](assets/a-postmortem-of-three-recent-issues/img_000.webp)
已发布
    2025 年 9 月 17 日
团队
    [工程](</engineering>)
主题
    
  * [透明度](</search?topic=transparency>)
  * [Claude Sonnet](</search?topic=claude-sonnet>)
  * [Claude 开发者平台](</search?topic=claude-developer-platform>)
  * [算力与能源](</search?topic=compute-energy>)
  * [Claude Code](</search?topic=claude-code>)

[](</claude-sonnet-5-5>)[](</news/higher-limits-spacex>)[](</news/enabling-claude-code-to-work-more-autonomously>)[](</news/paul-smith-to-join-anthropic>)
相关文章
  * 公告
2026 年 9 月 28 日
[推出 Claude Sonnet 5.5](</claude-sonnet-5-5>)

[阅读更多](</search?topic=transparency>)
8 月到 9 月初之间，三个基础设施 bug 间歇性地降低了 Claude 的回复质量。我们现已解决这些问题，想说明一下发生了什么。
8 月初，陆续有用户报告 Claude 的回复变差。这些最初的报告很难与用户反馈中的正常波动区分开来。到 8 月下旬，报告的频率和持续性都在上升，促使我们启动调查，最终查出三个彼此独立的基础设施 bug。
把话说清楚：我们绝不会因为需求、时段或服务器负载而降低模型质量。用户报告的那些问题，完全由基础设施 bug 造成。
我们知道用户期待 Claude 的质量始终一致，也为「基础设施改动不影响模型输出」设了极高的标准。在最近这几起事件中，我们没达到这个标准。下面的复盘会说明哪里出了错、为什么发现和修复花的时间比我们希望的更长，以及我们正在做哪些改变来防止今后再发生类似事件。
我们通常不会公开基础设施到这种技术细节程度，但这几起问题的波及范围和复杂度，值得做一次更完整的说明。
## 我们如何大规模提供 Claude 服务
我们通过第一方 API、Amazon Bedrock 和 Google Cloud 的 Vertex AI，向数百万用户提供 Claude。我们把 Claude 部署在多种硬件平台上，即 AWS Trainium、NVIDIA GPU 和 Google TPU。这一做法提供了服务全球用户所需的容量和地域分布。
每种硬件平台特性不同，需要专门的优化。尽管有这些差异，我们对模型实现有严格的等价标准，目标是无论请求由哪个平台处理，用户都应得到相同质量的回复。这种复杂性意味着任何基础设施改动都必须在所有平台和配置上仔细验证。
## 事件时间线
![Claude API 事件示意时间线。黄色：发现问题，红色：降级加剧，绿色：修复上线。](assets/a-postmortem-of-three-recent-issues/img_001.webp)
**Claude API** 上的事件示意时间线。黄色：发现问题，红色：降级加剧，绿色：修复上线。
这些 bug 相互重叠，使诊断格外困难。第一个 bug 于 8 月 5 日引入，影响约 0.8% 发往 Sonnet 4 的请求。另外两个 bug 则源自 8 月 25 日和 26 日的部署。
虽然最初影响有限，但 8 月 29 日的一次负载均衡改动开始放大受影响的流量。这让更多用户遇到问题，而另一些用户仍看到正常表现，于是出现了令人困惑、彼此矛盾的报告。
## 三个相互重叠的问题
下面描述造成降级的三个 bug、发生时间，以及我们如何解决：
### 1\. 上下文窗口路由错误
8 月 5 日，部分 Sonnet 4 请求被错误路由到为即将推出的 [1M token](<https://docs.claude.com/en/docs/build-with-claude/context-windows#1m-token-context-window>) [上下文窗口](<https://docs.claude.com/en/docs/build-with-claude/context-windows>) 而配置的服务器上。这个 bug 最初影响 0.8% 的请求。8 月 29 日，一次例行负载均衡改动意外增加了被路由到 1M 上下文服务器的短上下文请求数量。在 8 月 31 日受影响最严重的那个小时里，16% 的 Sonnet 4 请求受到影响。
在此期间发起请求的 Claude Code 用户中，约 30% 至少有一条消息被路由到错误的服务器类型，导致回复质量下降。在 Amazon Bedrock 上，自 8 月 12 日起，被错误路由的流量峰值达到所有 Sonnet 4 请求的 0.18%。8 月 27 日至 9 月 16 日期间，Google Cloud 的 Vertex AI 上受错误路由影响的请求不到 0.0004%。
不过，有些用户受影响更严重，因为我们的路由是「粘性」的。这意味着一旦某个请求由错误的服务器处理，后续的追问很可能也由同一台错误服务器处理。
**解决方案：** 我们修复了路由逻辑，确保短上下文和长上下文请求被导向正确的服务器池。修复于 9 月 4 日部署；到 9 月 16 日已完成在第一方平台与 Google Cloud 的 Vertex AI 上的全量上线，到 9 月 18 日完成在 AWS Bedrock 上的上线。
### 2\. 输出损坏
8 月 25 日，我们向 Claude API 的 TPU 服务器部署了一项错误配置，导致 token 生成过程中出错。一项由运行时性能优化引发的问题，偶尔会给「在该上下文下本应极少出现」的 token 赋予高概率，例如在英文提示下产出泰文或中文字符，或在代码中产出明显的语法错误。举例来说，一小部分用英文提问的用户，可能在回复中间看到「สวัสดี」。
这种损坏影响了 8 月 25 日至 28 日发往 Opus 4.1 和 Opus 4 的请求，以及 8 月 25 日至 9 月 2 日发往 Sonnet 4 的请求。第三方平台未受此问题影响。
**解决方案：** 我们定位了问题，并于 9 月 2 日回滚了该改动。我们在部署流程中加入了针对异常字符输出的检测测试。
### 3\. 近似 top-k XLA:TPU 误编译
8 月 25 日，我们部署了代码，以改进 Claude 在文本生成时选择 token 的方式。这项改动无意中触发了 XLA:TPU1 编译器里一个潜伏的 bug，已确认它影响到发往 Claude Haiku 3.5 的请求。
我们也认为它可能影响了 Claude API 上一部分 Sonnet 4 和 Opus 3 的请求。第三方平台未受此问题影响。
**解决方案：** 我们先是发现该 bug 影响 Haiku 3.5，于 9 月 4 日回滚。后来注意到用户报告的 Opus 3 问题与该 bug 相符，于 9 月 12 日回滚。经过大量排查，我们未能在 Sonnet 4 上复现这个 bug，但出于格外谨慎，也决定一并回滚。
与此同时，我们（a）一直与 XLA:TPU 团队合作修复这个编译器 bug，（b）上线了改用更高精度精确 top-k 的修复。详情见下文的深入剖析。
## 深入看看 XLA 编译器 bug
为了说明这些问题的复杂性，下面讲讲 XLA 编译器 bug 是如何显现的，以及它为什么格外难诊断。
Claude 生成文本时，会为每个可能的下一个词计算概率，再从这个概率分布中随机抽样。我们用「top-p 采样」来避免荒谬的输出——只考虑累积概率达到某个阈值（通常是 0.99 或 0.999）的词。在 TPU 上，我们的模型跨多块芯片运行，概率计算发生在不同位置。要排序这些概率，就需要在芯片之间协调数据，这很复杂。2
2024 年 12 月，我们发现当 [温度（temperature）](<https://docs.claude.com/en/docs/about-claude/glossary#temperature>) 为零时，我们的 TPU 实现偶尔会丢掉概率最高的 token。我们部署了一个变通方案来修复这一情况。
![2024 年 12 月补丁的代码片段，用于绕开 temperature = 0 时意外丢 token 的 bug。](assets/a-postmortem-of-three-recent-issues/img_002.webp)
2024 年 12 月补丁的代码片段，用于绕开 temperature = 0 时意外丢弃最高概率 token 的 bug。
根因涉及混合精度运算。我们的模型用 [bf16](<https://github.com/tensorflow/tensorflow/blob/f41959ccb2d9d4c722fe8fc3351401d53bcf4900/tensorflow/core/framework/bfloat16.h>)（16 位浮点）计算下一个 token 的概率。然而向量处理器是 [fp32 原生](<https://dl.acm.org/doi/pdf/10.1145/3360307>)的，因此 TPU 编译器（XLA）可以通过把某些运算转成 fp32（32 位）来优化运行时。这一优化过程由 `xla_allow_excess_precision` 标志控制，其默认值为 true。
这造成了一处不一致：本应对「哪个 token 概率最高」达成一致的运算，却运行在不同的精度级别上。精度不一致意味着它们对最高概率 token 的判断不吻合，结果有时会让这个 token 从候选中彻底消失。
8 月 26 日，我们部署了重写后的采样代码，以修复精度问题，并改进对「刚好触及 top-p 阈值的边界概率」的处理。但在修复这些问题的过程中，我们暴露出一个更棘手的问题。
![代码片段：作为 8 月 11 日改动的一部分合并的最小复现程序，它找到了 2024 年 12 月所绕开的「bug」的根因；实际上那是 xla_allow_excess_precision 标志的预期行为。](assets/a-postmortem-of-three-recent-issues/img_003.png)
代码片段：作为 8 月 11 日改动的一部分合并的最小复现程序，它找到了 2024 年 12 月所绕开的「bug」的根因。实际上，那是 `xla_allow_excess_precision` 标志的预期行为。
我们的修复移除了 12 月的变通方案，因为我们以为已经解决了根因。这引出了 [近似 top-k](<https://docs.jax.dev/en/latest/_autosummary/jax.lax.approx_max_k.html>) 运算里一个更深层的 bug——近似 top-k 是一种快速找出最高概率 token 的性能优化。3 这种近似有时会返回完全错误的结果，但只在特定批量大小和模型配置下才会。12 月的变通方案此前无意中掩盖了这个问题。
![Slack 消息，展示与开发该算法的 XLA:TPU 工程师分享的底层近似 top-k bug 复现程序。这段代码在 CPU 上运行时返回正确结果。](assets/a-postmortem-of-three-recent-issues/img_004.webp)
与[开发该算法](<https://arxiv.org/pdf/2206.14286>)的 XLA:TPU 工程师分享的底层近似 top-k bug 复现程序。这段代码在 CPU 上运行时返回正确结果。
这个 bug 的行为令人沮丧地不稳定。它会随一些看似无关的因素而变化，比如它前后运行了哪些运算、是否启用了调试工具。同一条提示词，可能在一次请求里完全正常，在下一次却失败。
调查过程中，我们还发现精确 top-k 运算已不再有过去那种令人却步的性能代价。我们从近似 top-k 切换到精确 top-k，并把一些额外运算统一到 fp32 精度。4 模型质量没有商量余地，所以我们接受了这点效率损失。
## 为什么发现得这么难
我们的验证流程通常依赖基准测试，辅以安全评估和性能指标。工程团队会做抽查，并先向小规模的「金丝雀」分组部署。
这些问题暴露出我们本该更早发现的关键缺口。我们跑的评估根本没捕捉到用户报告的降级，部分原因是 Claude 往往能从孤立的错误中很好地恢复。我们自身的隐私实践也给调查带来困难：内部的隐私与安全管控限制了工程师何时、以何种方式访问用户与 Claude 的交互，尤其是那些没有作为反馈上报给我们的交互。这保护了用户隐私，却也让工程师无法查看识别或复现 bug 所需的问题交互。
每个 bug 在不同平台上、以不同比例呈现出不同症状。这造成了一堆令人困惑、指向不了任何单一原因的报告，看上去像是随机、时好时坏的降级。
更根本的是，我们过于依赖噪声很大的评估。虽然我们注意到网上报告在增多，却缺少清晰的办法把这些报告与近期的各项改动对应起来。8 月 29 日负面报告激增时，我们没有立刻把它与一次本属常规的负载均衡改动联系起来。
## 我们正在做的改变
在继续改进基础设施的同时，我们也在改进评估和防范上文这类 bug 的方式，覆盖所有提供 Claude 服务的平台。以下是我们正在做的改变：
  * **更灵敏的评估：** 为帮助找到任一问题的根因，我们开发了能更可靠地区分「正常实现」与「损坏实现」的评估。我们会持续改进这些评估，更紧密地盯住模型质量。
  * **在更多环节做质量评估：** 虽然我们已在系统上定期跑评估，但今后会在真实生产系统上持续运行，以便捕捉到上下文窗口负载均衡错误这类问题。
  * **更快的调试工具：** 我们会开发基础设施和工具，在不牺牲用户隐私的前提下更好地排查来自社区的反馈。此外，这里开发的一些定制工具也将用于缩短未来类似事件（如果发生）的修复时间。

评估和监控很重要。但这几起事件表明，当 Claude 的回复达不到一贯水准时，我们同样需要来自用户的持续信号。用户报告观察到的具体变化、遇到的异常行为实例，以及跨不同使用场景呈现出的规律，都帮助我们定位了问题。
用户继续直接把反馈发给我们，仍然格外有帮助。你可以在 Claude Code 里用 `/bug` 命令，或在 Claude 应用里点「踩」按钮来提交。开发者和研究人员常会创造出新颖有趣的模型质量评估方法，作为我们内部测试的补充。如果你愿意分享自己的方法，可以联系 [feedback@anthropic.com](<mailto:feedback@anthropic.com>)。
我们始终感谢社区做出的这些贡献。
## 作者与致谢
### 致谢
作者：Sam McAllister。感谢 Stuart Ritchie、Jonathan Gray、Kashyap Murali、Brennan Saeta、Oliver Rausch、Alex Palcuie 以及许多其他同事。
[1] XLA:TPU 是把 [XLA](<https://openxla.org/xla/architecture>) 高级优化语言（通常用 [JAX](<https://docs.jax.dev/en/latest>) 编写）翻译成 TPU 机器指令的优化编译器。
[2] 我们的模型太大，单块芯片装不下，被切分到数十块甚至更多芯片上，因此排序运算是一次分布式排序。TPU（和 GPU、Trainium 一样）与 CPU 的性能特性也不同，需要用向量化运算而非串行算法的不同实现技术。
[3] 我们此前一直使用这个近似运算，因为它带来可观的性能提升。其原理是容忍概率最低的那些 token 上可能出现的误差，这本不该影响质量——除非 bug 让它转而丢掉了概率最高的 token。
[4] 请注意，如今已修正的 top-k 实现可能让「刚好靠近 top-p 阈值的 token 是否被纳入」出现细微差异；在少数情况下，用户重新调一调 top-p 的取值会有好处。
