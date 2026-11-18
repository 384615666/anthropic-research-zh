---
title: Equipping agents for the real world with Agent Skills
url: https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills
date: Oct 16, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# 用 Agent Skills 为智能体装备应对真实世界的能力

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills

---

工程（Engineering）
2025 年 10 月 16 日
已发布
    2025 年 10 月 16 日
团队
    [工程](</engineering>)
主题
    
  * [Agent Skills](</search?topic=agent-skills>)
  * [智能体](</search?topic=agents>)
  * [上下文工程](</search?topic=context-engineering>)
  * [工具使用](</search?topic=tool-use>)
  * [Claude Code](</search?topic=claude-code>)

[](</research/building-c-compiler>)[](</research/effective-context-engineering-for-ai-agents>)[](</research/writing-tools-for-agents>)[](</research/claude-code-best-practices>)
相关文章
  * 工程
2026 年 2 月 5 日
[用一支并行 Claude 团队构建 C 编译器](</research/building-c-compiler>)

[阅读更多](</search?topic=agent-skills>)
  * 2025 年 12 月 18 日
### 更新
我们已将 Agent Skills 发布为一项开放标准，以实现跨平台的可移植性。
[阅读更多](<https://agentskills.io/>)

* * *
随着模型能力的提升，我们现在能够构建与完整计算环境交互的通用智能体。例如，[Claude Code](<https://claude.com/product/claude-code>) 就能借助本地代码执行与文件系统，完成跨领域的复杂任务。但随着这些智能体变得越来越强大，我们需要更具可组合性、可扩展且可移植的方式，为它们装备特定领域的专业知识。
这促使我们创建了 [**Agent Skills**](<https://www.anthropic.com/news/skills>)：由指令、脚本与资源组成的有序文件夹，智能体可以动态发现并加载它们，从而在特定任务上表现得更好。**** Skills 通过将你的专业知识打包成供 Claude 使用的可组合资源来扩展 Claude 的能力，把通用智能体转变为契合你需求的专用智能体。
为智能体构建一项技能，就像为新员工编写一份入职指南。如今，任何人都不必再为每个用例打造零散的、定制设计的智能体，而是可以通过捕捉并分享自己的流程性知识，用可组合的能力来定制自己的智能体。在本文中，我们将解释 Skills 是什么、展示它们如何工作，并分享构建你自己的技能的最佳实践。
![要激活技能，你只需编写一个 SKILL.md 文件，为你的智能体写入自定义指引。](assets/equipping-agents-for-the-real-world-with-agent-skills/img_000.webp)
一项技能就是一个包含 SKILL.md 文件的目录，其中含有组织有序的指令、脚本与资源文件夹，为智能体提供额外的能力。
## 技能的结构
为了看清 Skills 的实际运作，我们来看一个真实例子：支撑 [Claude 近期推出的文档编辑能力](<https://www.anthropic.com/news/create-files>) 的技能之一。Claude 已经相当擅长理解 PDF，但直接操作 PDF 的能力有限（例如填写表单）。这个 [PDF 技能](<https://github.com/anthropics/skills/tree/main/document-skills/pdf>) 让我们能够赋予 Claude 这些新能力。
最简单的情况下，一项技能就是一个包含 `SKILL.md file` 的目录。该文件必须以 YAML frontmatter 开头，其中包含一些必需的元数据：`name` 和 `description`。启动时，智能体会把每个已安装技能的 `name` 和 `description` 预加载到自己的系统提示词中。
这些元数据是_渐进式披露_（progressive disclosure）的**第一层**：它只提供恰到好处的信息，让 Claude 知道何时应使用哪项技能，而无需把全部内容加载进上下文。该文件的实际正文则是细节的**第二层**。如果 Claude 认为某项技能与当前任务相关，它会通过把完整的 `SKILL.md` 读入上下文来加载该技能。
![SKILL.md 文件的结构，包括相关元数据：name、description，以及与技能应执行的具体操作有关的上下文。](assets/equipping-agents-for-the-real-world-with-agent-skills/img_001.webp)
SKILL.md 文件必须以 YAML Frontmatter 开头，其中包含文件名与描述，这些内容会在启动时加载进其系统提示词。
随着技能变得越来越复杂，它们可能包含过多上下文，无法全部放进单个 `SKILL.md`；或者某些上下文只在特定场景下才相关。在这些情况下，技能可以在技能目录内打包额外的文件，并在 `SKILL.md` 中按名称引用它们。这些额外链接的文件构成细节的**第三层**（乃至更多层），Claude 可以只在需要时选择去浏览与发现它们。
在下面展示的 PDF 技能中，`SKILL.md` 引用了技能作者选择随核心 `SKILL.md` 一起打包的两个额外文件（`reference.md` 和 `forms.md`）。通过把填写表单的指引移到单独的文件（`forms.md`）里，技能作者得以让技能的核心保持精简，并确信 Claude 只会在填写表单时才去读取 `forms.md`。
![如何将额外内容打包进 SKILL.md 文件。](assets/equipping-agents-for-the-real-world-with-agent-skills/img_002.webp)
你可以通过额外文件把更多上下文纳入自己的技能，Claude 随后可依据系统提示词来触发这些上下文。
渐进式披露是让 Agent Skills 兼具灵活性与可扩展性的核心设计原则。就像一本组织良好的手册，先给出目录，再是具体章节，最后是详尽的附录，技能让 Claude 只在需要时才加载信息：
![此图展示了 Skills 中上下文的渐进式披露方式。](assets/equipping-agents-for-the-real-world-with-agent-skills/img_003.webp)
拥有文件系统与代码执行工具的智能体，在处理某项特定任务时，并不需要把一项技能的全部内容读入自己的上下文窗口。这意味着，能够打包进一项技能的上下文量实际上是没有上限的。
### Skills 与上下文窗口
下图展示了当用户消息触发某项技能时，上下文窗口会如何变化。
![此图展示了技能如何在上下文窗口中被触发。](assets/equipping-agents-for-the-real-world-with-agent-skills/img_004.jpg)
技能通过你的系统提示词在上下文窗口中被触发。
图中所示的操作顺序：
  1. 一开始，上下文窗口中包含核心系统提示词、每个已安装技能的元数据，以及用户的初始消息；
  2. Claude 通过调用 Bash 工具读取 `pdf/SKILL.md` 的内容来触发 PDF 技能；
  3. Claude 选择读取随该技能打包的 `forms.md` 文件；
  4. 最后，Claude 已从 PDF 技能加载了相关指引，于是继续执行用户的任务。

### Skills 与代码执行
技能还可以包含代码，供 Claude 自行判断、作为工具来执行。
大型语言模型擅长许多任务，但某些操作更适合用传统代码执行来完成。例如，通过生成 token 来给列表排序，远比直接运行一个排序算法昂贵得多。除了效率考量之外，许多应用还要求只有代码才能提供的确定性可靠性。
在我们的例子里，PDF 技能包含一段预先写好的 Python 脚本，用于读取 PDF 并提取所有表单字段。Claude 可以运行这段脚本，而无需把脚本或 PDF 加载进上下文。而且由于代码是确定性的，这一工作流既一致又可重复。
![此图展示了代码如何通过 Skills 执行。](assets/equipping-agents-for-the-real-world-with-agent-skills/img_005.webp)
技能还可以包含代码，让 Claude 依据任务的性质自行判断、作为工具来执行。
## 开发与评估技能
以下是一些着手编写与测试技能时的实用指南：
  * **从评估入手：** 让智能体在具有代表性的任务上运行，观察它们在哪里遇到困难、哪里需要额外上下文，以此找出能力上的具体缺口。然后逐步构建技能来弥补这些不足。
  * **为规模而设计结构：** 当 `SKILL.md` 文件变得臃肿时，把它的内容拆分成单独的文件并加以引用。如果某些上下文彼此互斥、或很少一起用到，让路径保持分离能减少 token 用量。最后，代码既可以作为可执行工具，也可以作为文档。应当明确 Claude 是直接运行脚本，还是把它们作为参考读入上下文。
  * **从 Claude 的视角思考：** 观察 Claude 在真实场景中如何使用你的技能，并据此迭代：留意意料之外的轨迹，或对某些上下文的过度依赖。要特别关注技能的 `name` 和 `description`，Claude 在决定是否为当前任务触发该技能时会用到它们。
  * **与 Claude 一起迭代：** 在你和 Claude 共同处理一项任务时，让 Claude 把成功的做法与常见的失误沉淀为技能中可复用的上下文与代码。如果它在使用技能完成任务时偏离了正轨，就让它自我反思问题出在哪里。这一过程会帮助你发现 Claude 真正需要哪些上下文，而不必一开始就试图把它们全部预判出来。

### 使用 Skills 时的安全考量
技能通过指令与代码为 Claude 提供新的能力。这虽然让它们很强大，但也意味着恶意技能可能在其被使用的环境中引入漏洞，或指使 Claude 外泄数据、采取意料之外的行动。
我们建议只从可信来源安装技能。若要从可信度较低的来源安装技能，请在使用前彻底审查。先阅读技能中打包的文件内容，弄清它会做什么，尤其留意代码依赖，以及图片或脚本之类的打包资源。同样，也要留意技能中指示 Claude 连接到可能不可信的外部网络来源的指令或代码。
## Skills 的未来
Agent Skills [目前已获得支持](<https://www.anthropic.com/news/skills>)，覆盖 [Claude.ai](<http://claude.ai>)、Claude Code、Claude Agent SDK 以及 Claude Developer Platform。
在接下来的几周里，我们会持续增加功能，覆盖创建、编辑、发现、分享与使用 Skills 的完整生命周期。我们尤其期待 Skills 能帮助组织与个人同 Claude 分享自己的上下文与工作流。我们还将探索 Skills 如何与 [模型上下文协议](<https://modelcontextprotocol.io/>)（MCP）服务器形成互补，教会智能体涉及外部工具与软件的更复杂工作流。
更长远地看，我们希望让智能体能够自行创建、编辑与评估 Skills，把它们自身的行为模式固化为可复用的能力。
Skills 是一个简单的概念，其格式也同样简单。这种简洁让组织、开发者与最终用户更容易构建定制化的智能体，并赋予它们新的能力。
我们很期待看到人们用 Skills 构建出什么。今天就从我们的 Skills [文档](<https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>)与[示例手册](<https://github.com/anthropics/claude-cookbooks/tree/main/skills>)开始吧。
## 作者与致谢
### 致谢
作者：Barry Zhang、Keith Lazuka 和 Mahesh Murag，他们都非常喜欢文件夹。特别感谢 Anthropic 内部许多其他倡导、支持并构建了 Skills 的同事。
