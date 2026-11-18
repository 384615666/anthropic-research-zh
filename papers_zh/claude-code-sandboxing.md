---
title: Beyond permission prompts:making Claude Code more secure and autonomous
url: https://www.anthropic.com/research/claude-code-sandboxing
date: Oct 20, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# 超越权限提示：让 Claude Code 更安全、更自主

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/claude-code-sandboxing

---

工程（Engineering）
2025 年 10 月 20 日
![超越权限提示：让 Claude Code 更安全、更自主](assets/claude-code-sandboxing/img_000.webp)
已发布
    2025 年 10 月 20 日
团队
    [工程](</engineering>)
主题
    
  * [Claude Code](</search?topic=claude-code>)
  * [网络安全](</search?topic=cybersecurity>)
  * [智能体](</search?topic=agents>)
  * [安全保障](</search?topic=safeguards>)
  * [开源](</search?topic=open-source>)

[](</research/how-we-contain-claude>)[](</research/trustworthy-agents>)[](</research/zero-days>)[](</news/disrupting-AI-espionage>)
相关文章
  * 工程
2026 年 5 月 25 日
[我们如何在各产品中约束 Claude](</research/how-we-contain-claude>)

[阅读更多](</search?topic=claude-code>)
在 [Claude Code](<https://www.claude.com/product/claude-code>) 中，Claude 与你一同编写、测试和调试代码：浏览你的代码库、编辑多个文件、运行命令来验证自己的工作。让 Claude 拥有对代码库和文件如此大的访问权限，也可能带来风险，尤其是在发生提示词注入（prompt injection）时。
为解决这一问题，我们在 Claude Code 中引入了两项基于沙箱（sandboxing）的新功能，二者都旨在为开发者提供更安全的工作环境，同时让 Claude 能更自主地运行、减少权限提示。在我们的内部使用中，我们发现沙箱能在保证安全的前提下把权限提示减少 84%。通过划定 Claude 可自由工作的既定边界，它们同时提升了安全性与自主性。
## 保障 Claude Code 用户的安全
Claude Code 采用基于权限的模型：默认状态下它是只读的，也就是说，在做出修改或运行任何命令之前，它都会先请求许可。这一规则有一些例外：我们会自动放行 echo 或 cat 这类安全命令，但大多数操作仍需显式批准。
不断点击「批准」会拖慢开发节奏，还可能导致「审批疲劳」——用户可能不再仔细留意自己批准了什么，反而让开发变得更不安全。
为此，我们为 Claude Code 推出了沙箱机制。
## 沙箱：更安全、更自主的方案
沙箱会预先划定边界，让 Claude 在其中更自由地工作，而不必为每个操作逐一请求许可。启用沙箱后，权限提示会大幅减少，安全性也会提高。
我们的沙箱方案建立在操作系统级别的功能之上，用以实现两道边界：
  1. **文件系统隔离（filesystem isolation）**，它确保 Claude 只能访问或修改特定目录。这一点对于防止被提示词注入的 Claude 修改敏感系统文件尤为重要。
  2. **网络隔离（network isolation）**，它确保 Claude 只能连接到经过批准的服务器。这可以防止被提示词注入的 Claude 泄露敏感信息或下载恶意软件。

值得注意的是，有效的沙箱_必须同时_具备文件系统隔离与网络隔离。没有网络隔离，被攻陷的智能体可能把 SSH 密钥之类的敏感文件外传；没有文件系统隔离，被攻陷的智能体则能轻易逃出沙箱并获得网络访问。正是通过同时使用这两种技术，我们才能为 Claude Code 用户提供更安全、更快捷的智能体体验。
### Claude Code 中的两项新沙箱功能
#### 沙箱化 bash 工具：无需权限提示即可安全执行 bash
我们正在推出[一套新的沙箱运行时](<https://docs.claude.com/en/docs/claude-code/sandboxing>)，它以研究预览的形式提供 beta 版本，让你可以精确定义智能体能够访问哪些目录和网络主机，而无需承担启动和管理容器的开销。它可以用来对任意进程、智能体和 MCP 服务器进行沙箱隔离。它同样以[开源研究预览](<https://github.com/anthropic-experimental/sandbox-runtime>)的形式提供。
在 Claude Code 中，我们用这套运行时为 bash 工具加上沙箱，使 Claude 能在你设定的边界内运行命令。在安全的沙箱内部，Claude 可以更自主地运行，并在无需权限提示的情况下安全地执行命令。如果 Claude 试图访问沙箱_之外_的内容，你会立即收到通知，并可以自行决定是否允许。
我们把这套机制构建在操作系统级别的原语之上，例如 [Linux bubblewrap](<https://github.com/containers/bubblewrap>) 和 MacOS seatbelt，以便在操作系统层面强制执行这些限制。它们不仅覆盖 Claude Code 的直接交互，也覆盖由该命令派生出的任何脚本、程序或子进程。如上所述，这个沙箱同时强制执行以下两点：
  1. **文件系统隔离**，通过允许读写当前工作目录、但阻止修改目录之外的任何文件来实现。
  2. **网络隔离**，通过只允许借助连接到沙箱外代理服务器的 unix 域套接字访问互联网来实现。该代理服务器会强制执行对进程可连接域名的限制，并处理对新请求域名的用户确认。若你希望进一步提升安全性，我们也支持自定义该代理，对出站流量强制执行任意规则。

这两个组件都可配置：你可以轻松地选择允许或禁止特定的文件路径或域名。
![这张图说明了 Claude Code 中的沙箱机制如何工作。](assets/claude-code-sandboxing/img_001.webp)
Claude Code 的沙箱架构通过文件系统与网络控制来隔离代码执行，自动放行安全操作、拦截恶意操作，并仅在必要时请求许可。
沙箱确保即便提示词注入成功，也会被完全隔离，无法影响用户的整体安全。这样一来，被攻陷的 Claude Code 既无法窃取你的 SSH 密钥，也无法向攻击者的服务器回连。
要开始使用这项功能，在 Claude Code 中运行 /sandbox，并查看关于我们安全模型的[更多技术细节](<https://docs.claude.com/en/docs/claude-code/sandboxing>)。
为了让其他团队更容易构建更安全的智能体，我们已经将这项功能[开源](<https://github.com/anthropic-experimental/sandbox-runtime>)。我们认为，其他团队也应当考虑把这项技术用于自己的智能体，以提升其智能体的安全态势。
#### 网页版 Claude Code：在云端安全地运行 Claude Code
今天，我们还发布了[网页版 Claude Code](<https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web>)，让用户能够在云端隔离的沙箱中运行 Claude Code。网页版 Claude Code 会把每个 Claude Code 会话放在隔离沙箱中执行，使其以安全可靠的方式完整访问自己的服务器。我们在设计这个沙箱时，确保敏感凭据（例如 git 凭据或签名密钥）绝不会与 Claude Code 一同留在沙箱内部。这样一来，即便沙箱中运行的代码被攻陷，用户也不会受到进一步损害。
网页版 Claude Code 使用一个自定义代理服务，以透明方式处理所有 git 交互。在沙箱内部，git 客户端借助一个定制的、限定作用域的凭据向该服务完成认证。代理会核验这一凭据以及 git 交互的内容（例如确保它只向配置好的分支推送），随后在把请求发往 GitHub 之前附上正确的认证令牌。
![这张插图描绘了网页版 Claude Code 如何通过自定义代理处理所有 git 交互。](assets/claude-code-sandboxing/img_002.webp)
Claude Code 的 Git 集成会把命令路由经过一个安全代理，由它校验认证令牌、分支名称和仓库目标地址——在支持安全版本控制工作流的同时，阻止未经授权的推送。
## 开始使用
对于把 Claude 用于工程工作的开发者而言，我们新的沙箱化 bash 工具与网页版 Claude Code 在安全性和生产力两方面都带来了显著提升。
要开始使用这些工具：
  1. 在 Claude 中运行 `/sandbox`，并查看[我们的文档](<https://docs.claude.com/en/docs/claude-code/sandboxing>)了解如何配置这个沙箱。
  2. 前往 [claude.com/code](<http://claude.ai/code>) 试用网页版 Claude Code。

或者，如果你正在构建自己的智能体，可以看看我们[开源的沙箱代码](<https://github.com/anthropic-experimental/sandbox-runtime>)，并考虑把它集成到你的工作中。我们期待看到你构建出的成果。
要进一步了解网页版 Claude Code，请查看我们的[发布博客文章](<https://www.anthropic.com/news/claude-code-on-the-web>)。
## 作者与致谢
### 贡献者
Article written by David Dworken and Oliver Weller-Davies, with contributions from Meaghan Choi, Catherine Wu, Molly Vorwerck, Alex Isken, Kier Bradwell, and Kevin Garcia
### 致谢
Article written by David Dworken and Oliver Weller-Davies, with contributions from Meaghan Choi, Catherine Wu, Molly Vorwerck, Alex Isken, Kier Bradwell, and Kevin Garcia
