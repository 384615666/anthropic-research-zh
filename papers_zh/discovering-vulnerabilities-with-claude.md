---
title: Discovering and exploiting vulnerabilities in critical, real-world software with Claude
url: https://www.anthropic.com/research/discovering-vulnerabilities-with-claude
date: Oct 27, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# 借助Claude发现并利用关键现实软件中的漏洞

- **日期：** 
- **类别：** 前沿红队（Frontier Red Team）
- **来源：** https://www.anthropic.com/research/discovering-vulnerabilities-with-claude

---

前沿红队（Frontier Red Team）
2026 年 10 月 27 日
已发布
    2026 年 10 月 27 日
团队
    [前沿红队](</research/team/frontier-red-team>)
主题
    
  * [网络安全](</search?topic=cybersecurity>)
  * [红队测试](</search?topic=red-teaming>)
  * [安全评估](</search?topic=safety-evaluations>)
  * [编程](</search?topic=coding>)

[](</news/cyber-verification-program>)[](</research/exploit>)[](</news/claude-code-security>)[](</research/strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team>)
相关文章
  * 公告
2026 年 10 月 6 日
[扩展网络验证计划](</news/cyber-verification-program>)

[查看更多](</search?topic=cybersecurity>)
过去几个月里，我们使用一个尚未发布的内部研究模型，在一些全球使用最广泛的软件（如浏览器和操作系统）中[发现关键漏洞](<https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source>)。在本文中，我们分享五条攻击链的细节，它们在几乎无需用户交互、甚至完全无需交互的情况下就实现了远程代码执行及其他关键影响。这些攻击链展示了该模型在开源与专有软件中构造复杂多步利用（exploits）的能力。这些产品中的任何漏洞都可能影响数十亿用户。它们也属于世界上对安全最关键的软件，因而成为检验模型漏洞研究与网络能力的风向标。
我们依据自身的[协调漏洞披露](<https://www.anthropic.com/coordinated-vulnerability-disclosure>)流程，把每个漏洞报告给受影响的厂商：该流程给开发者90天时间修补，再额外留出45天，此后我们才会讨论超出公开公告已有内容的细节。
## 1\. Chrome中的一键远程代码执行
在初步提示之后，Claude写出了完整的利用链，使攻击者能够以该用户身份在浏览器沙箱之外执行任意代码。我们的概念验证在macOS上、以默认配置的原装Chrome浏览器，在页面加载后数秒内启动「计算器」应用，且无需任何进一步的用户交互：
  * Claude在Chrome的JavaScript引擎V8中发现一个漏洞，恶意网页可借此破坏V8的堆内存。
  * Claude发现第二个漏洞，用于逃出V8的内存区域沙箱并攻破ASLR。这一步在内存中定位Chrome的代码，并利用面向返回编程（return-oriented programming，ROP）链完全控制渲染进程。
  * 被攻陷的渲染进程受Chrome进程沙箱的限制。Claude随后在CacheStorage中发现一个竞态条件（race condition）。被攻陷的渲染进程利用该竞态条件读取沙箱之外的内存，摸清特权浏览器进程的内存布局。
  * 最后，Claude在Chrome的联合登录功能FedCM中发现一个释放后使用（use-after-free）漏洞，使该利用得以在沙箱之外执行任意代码。

我们已把发现报告给Google：共分配了62个CVE，并[已在Chrome 156中修补](<https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_02018666648.html>)，全部被评为关键或高危级别。其中包括13个沙箱逃逸，以及21个本可用于攻陷渲染进程的漏洞。
## 2\. Safari中的一键利用链
在初步提示之后，Claude写出一条利用链，使任意网站的JavaScript都能完全绕过同源策略（same-origin policy，SOP）。该利用可访问用户的Safari历史记录、Cookie及其他敏感数据，并能向其他域名发送带认证信息的HTTP请求、读取其响应。举例来说，若用户已登录邮箱账户，攻击者便可读取其邮件；若已登录银行账户，攻击者可查看账户余额或尝试转账。
为此，Claude攻破了Safari内置的数层防护：
  * Claude在Safari的JavaScript引擎JavaScriptCore（用C++编写）中发现一个释放后使用（use-after-free，UAF）漏洞。某些TypedArray操作会通过失效指针写入已释放的内存，覆盖TypedArray的元数据。
  * WebKit的Gigacage通过把TypedArray数据隔离在单独的内存区域来缓解此类攻击。Claude发现该区域中的某些变量被用来索引其他区域，由此获得了Gigacage之外的任意读写原语（arbitrary read/write primitive）。
  * 所有网站JavaScript都运行在WebContent沙箱中，它阻止UAF之类的bug触及磁盘上的敏感浏览器数据。Claude在该沙箱的IPC机制中发现一个漏洞，使利用得以从磁盘读取Safari存储的历史记录、Cookie与会话数据库。
  * 最后，Claude利用该UAF覆盖内存中的一个变量、关闭SOP，使攻击者的页面能够读取来自任何其他源（origin）的数据。

这条链之所以有趣，是因为它是一次「纯数据」攻击，从不依赖任意代码执行。它转而利用对浏览器进程内存的完整读写权限，去修改一个安全标志、一个对象大小和一个URL。其中若干弱点本身并非漏洞，而是设计上的预期行为，只是组合在一起时才变得可被利用。
Apple在我们提交报告的当天即予确认，并迅速实施了修复。[该修复](<https://support.apple.com/en-us/127594>)现已向用户提供。
## 3\. Android锁屏绕过
在初步提示之后，Claude写出一个利用，使攻击者无需解锁即可从一部被盗的Android手机中提取照片及其他个人信息。这项工作结合了三种方法：对Android开源部分的源代码分析、对Google Play服务二进制文件的逆向工程与去混淆，以及在实体Google Pixel 9上的实测。由此在开源与专有组件中都发现了大量漏洞。Claude随后把其中三个串联成最终利用。
Android针对这类攻击设有数层防护。Claude逐一找到了绕过办法：
  * 锁定的Android手机在设计上不通过USB传输数据。Claude发现带有某项特定设置的USB主机可绕过这一限制。
  * 设备到设备的传输协议会拒绝来自未授权对端的数据命令。Claude找到跳过授权检查、直接启动配对流程的办法。
  * 配对由带认证的密钥协商保护，会要求用户核对一个六位数字码。Claude发现一处缺陷，可跳过该验证，表现得就像用户点了「允许」一样。
  * USB传输本不应承载文件内容，这一点由一项硬编码检查强制保证。Claude发现一个回退机制，会通过USB发送原始字节，且不受该检查覆盖。利用便借它请求文件内容。

该问题已由Google处理。
## 4\. Windows远程拒绝服务
在初步提示之后，Claude写出一个利用，本可使攻击者远程令任何使用Windows原生实现响应HTTP/3请求的Windows机器崩溃。此例的难点首先在于找出漏洞本身。在那次初步提示之后，我们把该漏洞直接报告给Microsoft，后者修复了它并分配了[CVE-2026-33096](<https://nvd.nist.gov/vuln/detail/cve-2026-33096>)。
Claude识别出的漏洞，是Windows内核QUIC实现中的一处内存安全越界读取（out-of-bounds read）。攻击者可通过网络远程触达这段有漏洞的代码路径，向一个正在监听的服务器发送少量数据包，即可令机器崩溃并重启。反复发送这些请求，就能持续使服务器崩溃，导致所有用户都无法访问该服务器。我们估计，互联网上此类监听服务器可能有数百万台。
Claude是通过二进制分析发现该漏洞的。我们向模型提供了一份Windows可执行文件副本，请Claude使用现有的逆向工程工具（如Ghidra）逆向分析软件的工作方式，编写一个带完整注释、可复现相关功能的C程序，把所复现程序的行为与二进制文件比对以确保正确，再研究代码寻找漏洞。当我们请Claude找出潜在风险更高的问题时，它便揪出了这个可远程利用的漏洞。
## 5\. Linux中的零点击远程代码执行
尽管本文聚焦第三方产品，我们在开源方面的工作仍在继续。借助Claude，我们在OpenBSD、FreeBSD与Linux上发现了本地权限提升漏洞，在流行的沙箱基础设施中发现了若干沙箱逃逸，并在重要Web应用中发现了大量漏洞。我们还在Linux内核网络协议栈中发现了可远程触发（零点击，zero-click）的任意代码执行漏洞，这些漏洞此后已在上游修补并公开披露。下文详述其中一例。
在初步提示之后，Claude写出一个利用，使远程攻击者向启用了多路径TCP（multipath TCP）监听的Linux服务器发送数据包，即可在无需任何凭据或用户交互的情况下以root身份执行任意命令。其底层漏洞是内核网络协议栈中一个由竞态条件诱发的UAF bug。完整利用分两个关键阶段：
  * 第一阶段，攻击者远程攻破KASLR。它利用该竞态使内核读取一个由攻击者控制的长度字段，从而多复制若干字节并回送给攻击者；只要某次这样的越界读取在回包中带出一个内核指针，攻击者便掌握了内核地址空间布局。
  * 第二阶段，攻击者劫持控制流。它利用同一个UAF bug溢出缓冲区，用一个已通过某项常规协议功能预先布置在内核内存中的载荷（payload）地址覆盖回调指针。当内核调用该回调时，载荷会串联一连串对现有内核函数的调用，最终以攻击者选定、以root身份运行的shell命令收尾。

该竞态条件有一个便利之处：竞态失败只会让握手失败，而不会令整个系统崩溃，因此有耐心的攻击者可以无限重试直至成功。在我们的概念验证中，泄漏一个内核指针需48分钟，再花5分钟即可执行到shell命令。该漏洞（[CVE-2026-98432](<https://nvd.nist.gov/vuln/detail/cve-2026-98432>)）已在上游修补，并回移植到所有仍在维护的稳定内核分支。
## 我们的经验
在用Claude开展这项安全工作的全过程中，我们总结出若干塑造了工作方法的洞见。我们认为其中两点尤为重要。
**测试时计算量的扩展与扫描器的多样性，会显著增加所能发现的漏洞数量。**我们搭建了一个平台，并行运行大量扫描智能体，按每个扫描器为整体贡献了多少新增漏洞来衡量其价值，并动态跟踪覆盖率，使扫描器覆盖整个代码库。
所用策略从纯覆盖率导向（这个函数里有没有漏洞？）到目标导向（这个应用是否暴露了任何可能危及客户数据的东西？），再到威胁模型导向（这个应用中是否有任何东西绕过了其文档化的威胁模型？）。我们还用Claude对每一条已确认的发现运行自动化变体分析（variant analysis）。所有发现都要经过标准化的验证与风险评级流程，因此我们可以自由试验新的扫描器，而不降低质量门槛。
**清理现有积压只解决问题的一半；另一半是降低新漏洞进入代码库的速率。**为此，我们建议在PR（pull request）阶段进行扫描。我们通过一个Claude Code插件把安全指引直接嵌入开发流程，该插件已[公开发布](<https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance>)。
## 这对防御者意味着什么
前沿模型已经能够发现多个漏洞并把它们组合成可用的利用。这类技能历来只属于少数对这些目标有专精的专家团队。如今，模型几乎无需人工介入便能做到，还能产出一个任何人都能运行和验证的可用利用来自证。
用强大的模型赋能防御者，是让他们在攻击者之前抢先修补系统的关键。最近，我们发布了扩展版的[Cyber Verification Program](<https://www.anthropic.com/news/cyber-verification-program>)，向符合条件的安全专业人员开放高级网络能力，并减少拦截分类器的阻断。其中包括使用我们能力最强的模型：Claude Opus 5.5、Claude Sonnet 5.5、Claude Mythos 5.1，以及后续推出的其他新模型。我们给防御者的建议始终不变：扫描自己的代码比以往任何时候都更重要。
## 作者与致谢
### 贡献者
Nicholas Carlini, David Dworken, Xinyang Ge, Ben Morris, Milad Nasr, Chris Rohlf, Luna Tong
