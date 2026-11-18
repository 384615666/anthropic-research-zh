---
title: Confidential Inference via Trusted Virtual Machines
url: https://www.anthropic.com/research/confidential-inference-trusted-vms
date: Jun 18, 2025
category: Announcements
source: https://www.anthropic.com/research
---

# 通过可信虚拟机实现机密推理

- **日期：** 
- **分类：** 公告
- **来源：** https://www.anthropic.com/research/confidential-inference-trusted-vms

---

公告
2025 年 6 月 18 日
[阅读论文](<https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf>)
![Confidential Inference via Trusted Virtual Machines](assets/confidential-inference-trusted-vms/img_000.img)
每天，数百万用户[将](<https://trust.anthropic.com/>)敏感信息托付给 Claude——从专有代码到机密商业战略。在 Anthropic，我们正在研究和构建新技术，以确保用户的信任是值得的——事实上，是为了确保他们的信任得到密码学上的保证。
"密码学上的保证"是什么意思？在一份与 [Pattern Labs](<https://www.patternlabs.co/>) 合作发布的[新报告](<https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf>)中，我们描述了机密推理（Confidential Inference）的机制。机密推理是一组工具，我们可以用它来处理加密数据，并证明此类数据只能在能够证明自身可信的服务器内被读取。采用这些工具有两个主要原因：
  * 模型权重安全：我们可以将机密推理用作保护 Claude 等前沿模型免受越来越有能力的威胁行为者攻击的更广泛工作的一部分，例如 RAND 最近关于[保护 AI 模型权重](<https://www.rand.org/pubs/research_reports/RRA2849-1.html>)的报告中所描述的威胁；
  * 用户安全：我们可以用机密推理来证明敏感用户数据被保密。

我们分享这篇文章以及随附的[报告](<https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf>)，以解释什么是机密推理以及它可以为我们的用户带来哪些好处。我们还希望分享我们如何看待所涉及系统的安全性。这只是我们研究的草图，用以开启对话；我们在这项工作上仍处于早期阶段，现在预测它将如何演变为我们未来可能提供的具体设计或功能还为时过早。
以下各节提供了机密推理实现的一些技术细节。关键要点是，我们正在构建的系统旨在确保你的敏感数据除在需要处理的精确时刻外，始终处于加密状态——而且即使在那一刻，也仅限于高度受限、可验证的环境中。
## 推理服务
机密推理背后的指导原则是，敏感数据除在处理点外应始终保持加密。为强制执行这一点，我们使用既定的机密计算方法。这意味着我们构建一条证明我们软件安全性的信任链，然后利用该证明来强制执行关于究竟哪些软件可以使用加密密钥的规则。
对于用户数据，有两个需要我们操作敏感明文（即未加密或以任何方式未隐藏的文本）的点：
  * API 服务器。该服务器处理提示、将其转换为 token，并运行 Claude API 请求背后的大部分逻辑；
  * 推理服务器。该服务器在硬件加速器上运行 Claude 的"大脑"，从提示生成补全 token。

对于模型权重，只有推理服务器接收敏感数据。
本文将聚焦于推理服务器——API 服务器的安全性同样重要，但超出了我们试图描述的范围。由于并非所有加速器都完全支持机密计算，我们正在探索在小型、安全的"模型加载器与调用器"之上实现的推理服务器，它可以运行在可信环境中。这个加载器程序执行几个简单的工作：
  * 接受加密数据、解密并将其发送到加速器；
  * 调用对加速器的请求，并将加密结果返回给调用方。

只有"可信的"加载器能够访问解密数据。系统的其余部分是"不可信的"，但可以向加载器发送请求。
我们正在基于这一设计为我们的实现开发一个系统。对于该实现，我们推理服务器的大部分运行在"不可信"一侧——那里可能频繁变化，但变化不会影响整个系统的安全性。我们有一个小的可信加载器，运行在一个由虚拟机监控程序隔离的单独虚拟机上。加载器向推理服务器呈现为一个"虚拟加速器"，与模型架构细节无关。这个"虚拟加速器"只接受由我们安全的持续集成服务器签名的程序，这确保任何运行的代码都经过多位工程师的审查。
最终结果是确保，只要加载器被正确运行，_无论系统其余部分做什么_，我们的机密性要求都得到满足。因此，确立加载器被正确运行至关重要。
## 可信环境
该报告描述了加载器运行在一个具有特定功能集的机密计算环境中：
  1. 加密内存，由硬件与其他工作负载隔离；
  2. 禁用调试功能；
  3. 密码学证明正在运行正确的代码。

(1) 可以防御某些形式的物理攻击和恶意虚拟机监控程序，但将加密主机内存与加速器共享所需的功能目前尚未成熟。我们将继续努力弥合这一差距，但与此同时，我们将依赖我们的计算提供商在物理数据中心和虚拟机监控程序软件中维持安全性。
(2) 和 (3) 可以通过广泛支持的机密计算实践实现，使用可信平台模块（TPM）作为信任根。TPM 测量启动过程的每个阶段，并报告代表最终结果的哈希值。该哈希构成一个证明：加载器服务器按我们预期的方式被隔离、正在运行我们签名和审查过的代码，并被配置为禁用相关调试功能。密钥服务器可以检查这一证明，并且只在接收方证明自身安全时才释放解密密钥。
环境是否"可信"的决定最终取决于密钥服务器。我们还在探索其他各方验证可信代码并管理独立密钥服务器的机密计算模型。这可能使我们能够为每条数据提供更强的机密性保证。
## 未来方向
随着前沿模型能力的增强，我们可能会发现在安全加载器层有必要加入进一步的保障措施。这可能包括诸如在持有明文模型权重的服务器上增加一层[出口带宽限制](<https://www.anthropic.com/news/activating-asl3-protections>)，或要求安全分类器的签名才能运行推理等功能。我们希望展示这种机密推理模型能够激发讨论，探讨哪些额外功能值得探索，以确保 Anthropic 环境的持续安全和用户数据的机密性。
## 结论
这项研究将推进我们保护模型权重和用户数据的持续努力。使用这种模型保护用户请求，旨在确保客户数据只在具有增强硬件安全控制的上下文中被解密：
  * 请求在到达 Anthropic 服务器之前的某个点被加密；
  * 当请求到达 API 服务器时，它被解密、处理，并在被传递之前重新加密；
  * 推理服务器以加密形式处理请求，请求只有在发送到可信加载器时才被解密；
  * 补全在离开加载器之前被加密，并通过 API 服务器传递回调用方。

模型权重是一个更简单的故事：它们可以加密存储，在加载器处解密，并且永远不会从那里释放。
硬件设计者（那些[尚未这样做](<https://developer.nvidia.com/blog/confidential-computing-on-h100-gpus-for-secure-and-trustworthy-ai/>)的）应考虑将机密计算纳入其芯片。如果加速器上附有硬件信任根，这类系统的信任边界就可以显著缩小。
阅读[完整报告](<https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf>)。
### 与我们合作
如果关于机密推理的讨论激发了你想与我们合作研究这些问题的兴趣，请考虑申请我们[网站职位页面](<https://www.anthropic.com/jobs>)上"安全"和"AI 研究与工程"部分列出的空缺职位之一。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/confidential-inference-trusted-vms>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/confidential-inference-trusted-vms>)
## 相关内容
### 了解更多关于 Claude 的数学能力
一个未发布的研究版 Claude 在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足该猜想的黎曼 zeta 函数零点比例，从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而构建的数字签名方案。第二个攻击发现了一种攻击缩减轮数 AES（使用最广泛的分组密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### 项目 Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，考察 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)