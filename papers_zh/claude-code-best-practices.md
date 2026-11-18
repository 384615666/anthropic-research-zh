---
title: Claude Code:Best practices for agentic coding
url: https://www.anthropic.com/research/claude-code-best-practices
date: Apr 18, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# Claude Code：智能体编程最佳实践

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/claude-code-best-practices

---

工程（Engineering）
2025 年 4 月 18 日
已发布
    2025 年 4 月 18 日
团队
    [工程](</engineering>)
主题
    
  * [Claude Code](</search?topic=claude-code>)
  * [编程](</search?topic=coding>)
  * [智能体](</search?topic=agents>)
  * [上下文工程](</search?topic=context-engineering>)
  * [工具使用](</search?topic=tool-use>)

[](</features/making-of-claude-code>)[](</research/building-c-compiler>)[](</research/code-execution-with-mcp>)[](</research/equipping-agents-for-the-real-world-with-agent-skills>)
相关文章
  * 特性
2026 年 2 月 23 日
[Claude Code的诞生](</features/making-of-claude-code>)

[阅读更多](</search?topic=claude-code>)
  * 2026 年 1 月 26 日
### Claude Code最佳实践已迁移至文档
本博客文章已不再维护。有关最新的Claude Code最佳实践，请参阅官方文档（https://code.claude.com/docs/en/best-practices），它会随着Claude Code的演进持续更新。

* * *
我们最近[发布了Claude Code](<https://www.anthropic.com/news/claude-3-7-sonnet>)，一款用于智能体编程的命令行工具。作为研究项目开发而来，Claude Code为Anthropic的工程师和研究人员提供了一种更原生的方式，把Claude融入他们的编码工作流。
Claude Code刻意设计得底层而无预设立场，提供接近原始的模型访问能力，不强制特定工作流。这一设计理念造就了一个灵活、可定制、可脚本化且安全的强力工具。虽然功能强大，但这种灵活性对初次接触智能体编程工具的工程师而言存在学习曲线——至少在他们摸索出自己的最佳实践之前是如此。
本文概述了一些被证明行之有效的通用模式，既适用于Anthropic内部团队，也适用于在各种代码库、语言和环境中使用Claude Code的外部工程师。这份清单里的每一条都不是一成不变或放之四海皆准的；请把这些建议当作起点。我们鼓励你亲自实验，找到最适合自己的做法！
_想要更详细的信息？我们详尽的文档在[claude.ai/code](<https://claude.ai/code>)_ _涵盖了本文提到的所有功能，并提供了更多示例、实现细节与进阶技巧。_
## 1\. 定制你的配置
Claude Code是一款会自动把上下文拉取进提示词的智能体编程助手。这种上下文收集会消耗时间与token，但你可以通过调整环境来优化它。
### a. 创建 `CLAUDE.md` 文件
`CLAUDE.md` 是一个特殊文件，Claude在开始对话时会自动把它拉取进上下文。这使它成为记录以下内容的理想场所：
  * 常用的bash命令
  * 核心文件与工具函数
  * 代码风格指南
  * 测试说明
  * 仓库使用规范（例如分支命名、合并还是变基等）
  * 开发环境配置（例如pyenv的使用、哪些编译器可用）
  * 项目特有的任何异常行为或警告
  * 其他你希望Claude记住的信息

`CLAUDE.md` 文件没有必需的格式。我们建议保持简洁、便于人阅读。例如：
    
    # Bash命令
    - npm run build：构建项目
    - npm run typecheck：运行类型检查器
    
    # 代码风格
    - 使用ES模块（import/export）语法，不要用CommonJS（require）
    - 尽可能对导入使用解构（例如import { foo } from 'bar'）
    
    # 工作流
    - 完成一系列代码改动后，务必做类型检查
    - 为性能考虑，优先运行单个测试，而非整个测试套件
你可以把 `CLAUDE.md` 文件放在多个位置：
  * **仓库根目录**，或你运行 `claude` 的任意位置（最常见的用法）。把它命名为 `CLAUDE.md` 并签入git，这样你就能跨会话、与团队共享（推荐做法）；或者命名为 `CLAUDE.local.md` 并加入 `.gitignore`
  * **运行 `claude` 所在目录的任意父目录**。这对单体仓库（monorepo）最有用：你可能从 `root/foo` 运行 `claude`，同时在 `root/CLAUDE.md` 和 `root/foo/CLAUDE.md` 都放有 `CLAUDE.md` 文件，这两份都会被自动拉取进上下文
  * **运行 `claude` 所在目录的任意子目录**。这与上面相反，此时Claude会在你处理子目录中的文件时按需拉取其中的 `CLAUDE.md` 文件
  * **你的主目录**（`~/.claude/CLAUDE.md`），它会对所有 _claude_ 会话生效

当你运行 `/init` 命令时，Claude会自动为你生成一个 `CLAUDE.md`。
### b. 调优 `CLAUDE.md` 文件
你的 `CLAUDE.md` 文件会成为Claude提示词的一部分，因此应像对待任何高频使用的提示词一样反复打磨。一个常见错误是堆砌大量内容，却不迭代验证其效果。花些时间做实验，弄清什么样的内容能让模型最好地遵循指令。
你可以手动往 `CLAUDE.md` 里添加内容，也可以按 `#` 键给Claude一条指令，它会自动把该指令收纳进相关的 `CLAUDE.md`。许多工程师在编码时频繁使用 `#` 来记录命令、文件和风格指南，然后把 `CLAUDE.md` 的改动一并提交，让团队成员也能受益。
在Anthropic，我们偶尔会用[提示词优化器](<https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver>)来处理 `CLAUDE.md` 文件，并且经常调整指令（例如加上「IMPORTANT」或「YOU MUST」以示强调）来提升遵循度。
![Claude Code工具允许列表](assets/claude-code-best-practices/img_000.webp)
### c. 管理Claude的允许工具列表
默认情况下，对任何可能修改你系统的操作——文件写入、许多bash命令、MCP工具等——Claude Code都会请求许可。我们刻意采用这种保守设计，把安全放在首位。你可以定制允许列表，放行自己确认为安全的额外工具，或允许那些容易撤销的潜在风险工具（例如文件编辑、`git commit`）。
管理允许工具有四种方式：
  * 在会话中被提示时**选择「始终允许」**。
  * 启动Claude Code后**使用 __`/permissions` __ 命令**，在允许列表中添加或移除工具。例如，你可以添加 `Edit` 来始终允许文件编辑，添加 `Bash(git commit:*)` 来允许git提交，或添加 `mcp__puppeteer__puppeteer_navigate` 来允许通过Puppeteer MCP服务器进行导航。
  * **手动编辑**你的 `.claude/settings.json` 或 `~/.claude.json`（我们建议把前者签入源码控制，以便与团队共享）_._
  * **使用` --allowedTools` CLI标志**设置仅针对当前会话的权限。

### d. 如果使用GitHub，请安装gh CLI
Claude懂得如何使用 `gh` CLI与GitHub交互，用来创建议题、发起拉取请求、阅读评论等。即便没有安装 `gh`，Claude仍可使用GitHub API或MCP服务器（如果你装了的话）。
## 2\. 给Claude更多工具
Claude可以访问你的shell环境，你可以像为自己准备那样，为它积累一套趁手的脚本和函数。它还能通过MCP和REST API调用更复杂的工具。
### a. 配合bash工具使用Claude
Claude Code继承你的bash环境，因而能访问你的所有工具。虽然Claude认识unix工具、`gh` 这类常用程序，但若不加说明，它不会知道你自定义的bash工具：
  1. 告诉Claude工具的名称并附上用法示例
  2. 让Claude运行 __`--help` __ 查看工具文档
  3. 把常用工具记录进 `CLAUDE.md`

### b. 配合MCP使用Claude
Claude Code同时充当MCP服务器和客户端。作为客户端，它能连接任意数量的MCP服务器，通过三种方式访问其工具：
  * **在项目配置中**（在该目录下运行Claude Code时可用）
  * **在全局配置中**(在所有项目中都可用)
  * **在签入仓库的`.mcp.json` 文件中**（对在你的代码库上工作的任何人都可用）。例如，你可以把Puppeteer和Sentry服务器加进 `.mcp.json`，这样在仓库上工作的每位工程师都能开箱即用。

使用MCP时，带上 `--mcp-debug` 标志启动Claude也有助于排查配置问题。
### c. 使用自定义斜杠命令
对于重复的工作流——调试循环、日志分析等——把提示词模板存成Markdown文件，放在 `.claude/commands` 文件夹里。当你输入 `/` 时，它们就会出现在斜杠命令菜单中。你可以把这些命令签入git，供团队其他成员使用。
自定义斜杠命令可以包含特殊关键字 `$ARGUMENTS`，用来在调用命令时传入参数。
例如，下面是一个可用来自动拉取并修复Github议题的斜杠命令：
    
    请分析并修复这个GitHub议题：$ARGUMENTS。
    
    遵循以下步骤：
    
    1. 使用 `gh issue view` 获取议题详情
    2. 理解议题中描述的问题
    3. 在代码库中搜索相关文件
    4. 实现修复该问题所需的改动
    5. 编写并运行测试以验证修复
    6. 确保代码通过lint和类型检查
    7. 撰写描述清晰的提交信息
    8. 推送并创建PR
    
    记得用GitHub CLI（`gh`）处理所有与GitHub相关的任务。
把上面的内容放进 `.claude/commands/fix-github-issue.md`，它就会成为Claude Code中的 `/project:fix-github-issue` 命令。之后你就可以例如用 `/project:fix-github-issue 1234` 让Claude修复第1234号议题。类似地，你也可以把个人命令添加到 __`~/.claude/commands` 文件夹，让它们在你所有会话中都可用。
## 3\. 尝试常见工作流
Claude Code不强加特定工作流，让你能按自己的方式灵活使用。在这种灵活性所留下的空间里，我们的用户社区中已经涌现出若干高效使用Claude Code的成功模式：
### a. 探索、规划、编码、提交
这个万能工作流适用于许多问题：
  1. **让Claude阅读相关文件、图片或URL**，既可以给出笼统的指引（「读一下处理日志的那个文件」），也可以给出具体文件名（「读logging.py」），但要明确告诉它暂时不要写任何代码。
     1. 这是工作流中应当考虑大量使用子智能体的环节，尤其针对复杂问题。让Claude用子智能体去核实细节或排查它可能有的特定疑问——尤其是在对话或任务的早期——往往能在几乎不损失效率的前提下保留上下文空间。
  2. **让Claude为如何解决某个具体问题制定计划**。我们建议用「think」这个词来触发扩展思考模式，它给Claude额外的计算时间，更充分地评估各种备选方案。这些特定短语直接对应系统中递增的思考预算：「think」<「think hard」<「think harder」<「ultrathink」。每一级都为Claude分配逐级增多的思考预算。
     1. 如果这一步的结果看起来合理，你可以让Claude用它的计划创建一份文档或一个GitHub议题，这样当实现（第3步）不如你意时，就能回到这个节点重来。
  3. **让Claude用代码实现它的方案**。这里也适合要求它在实现各部分方案时，明确核验方案自身的合理性。
  4. **让Claude提交结果并创建拉取请求**。相关的话，这也是让Claude更新所有README或变更日志、说明它刚做了什么的好时机。

第1—2步至关重要——缺了它们，Claude往往直接跳到写解决方案的代码。有时那确实正是你想要的，但对那些需要先深入思考的问题，先让Claude调研和规划能显著提升表现。
### b. 写测试、提交；写代码、迭代、提交
对于容易用单元测试、集成测试或端到端测试验证的改动，这是Anthropic内部偏爱的工作流。有了智能体编程，测试驱动开发（TDD）变得更为强大：
  1. **让Claude根据预期的输入/输出对编写测试**。明确说明你正在做测试驱动开发，这样即便代码库中尚不存在相应功能，它也会避免创建模拟实现。
  2. **让Claude运行测试并确认它们失败**。明确告诉它在这个阶段不要写任何实现代码，通常很有帮助。
  3. 当你对测试满意后，**让Claude提交这些测试**。
  4. **让Claude编写能通过这些测试的代码**，指示它不要修改测试。让Claude持续进行，直到所有测试通过。Claude写代码、跑测试、调整代码、再跑测试，通常要迭代几轮。
     1. 在这个阶段，让它用独立的子智能体核验实现没有对测试过拟合，会很有帮助。
  5. 当你对改动满意后，**让Claude提交代码**。

当Claude有一个清晰的目标可供反复迭代时——一张视觉稿、一个测试用例或别的某种输出——它表现最好。通过提供测试这类预期输出，Claude能做出改动、评估结果，并逐步改进直至成功。
### c. 写代码、截图结果、迭代
与测试工作流类似，你也可以给Claude提供视觉目标：
  1. **给Claude一个截取浏览器截图的办法**（例如用[Puppeteer MCP服务器](<https://github.com/modelcontextprotocol/servers/tree/c19925b8f0f2815ad72b08d2368f0007c86eb8e6/src/puppeteer>)、[iOS模拟器MCP服务器](<https://github.com/joshuayoes/ios-simulator-mcp>)，或手动把截图复制/粘贴给Claude）。
  2. 通过复制/粘贴或拖放图片，或给Claude图片文件路径，**给它一张视觉稿**。
  3. **让Claude用代码实现设计**，对结果截图，并迭代直到结果与视觉稿一致。
  4. 满意后**让Claude提交**。

和人类一样，Claude的输出往往会在迭代中显著提升。第一版可能已经不错，但经过2—3轮迭代后通常会好得多。给Claude能看见自身输出的工具，才能获得最佳效果。
![安全YOLO模式](assets/claude-code-best-practices/img_001.webp)
### d. 安全YOLO模式
你可以不盯着Claude，用 `claude --dangerously-skip-permissions` 跳过所有权限检查，让它不受打扰地一路干到完成。这对修复lint错误、生成样板代码这类工作流很有效。
让Claude运行任意命令是有风险的，可能导致数据丢失、系统损坏，甚至数据外泄（例如通过提示词注入攻击）。为把这些风险降到最低，请在没有网络访问的容器里使用 `--dangerously-skip-permissions`。你可以参照这个[参考实现](<https://github.com/anthropics/claude-code/tree/main/.devcontainer>)，它使用Docker Dev Containers。
### e. 代码库问答
在熟悉新代码库时，用Claude Code来学习和探索。你可以像结对编程时问项目里另一位工程师那样，向Claude提同类问题。Claude能以智能体方式检索代码库，回答诸如以下的一般性问题：
  * 日志是怎么工作的？
  * 我该怎么新建一个API端点？
  * `foo.rs` 第134行的 `async move { ... }` 是做什么的？
  * `CustomerOnboardingFlowImpl` 处理了哪些边界情况？
  * 为什么第333行我们调用 `foo()` 而不是 `bar()`？
  * `baz.py` 第334行用Java怎么写？

在Anthropic，以这种方式使用Claude Code已成为我们核心的入职工作流，显著缩短了上手时间，也减轻了其他工程师的负担。不需要什么特殊提示词！只要提问，Claude就会去探索代码寻找答案。
![用Claude与git交互](assets/claude-code-best-practices/img_002.png)
### f. 用Claude与git交互
Claude能高效处理许多git操作。Anthropic的许多工程师把90%以上的 _git_ 交互交给Claude：
  * **检索 _git_ 历史**来回答「v1.2.3里都改了什么？」「这个特定功能归谁负责？」「这个API为什么这样设计？」之类问题。明确提示Claude去翻git历史来回答这类查询会很有帮助。
  * **撰写提交信息**。**** Claude会自动查看你的改动和近期历史，综合所有相关上下文来组织一条信息。
  * **处理复杂的git操作**，如还原文件、解决变基冲突、比较与嫁接补丁。

### g. 用Claude与GitHub交互
Claude Code能打理许多GitHub交互：
  * **创建拉取请求**：Claude理解「pr」这个简写，会基于diff和周边上下文生成合适的提交信息。
  * **对简单的代码评审意见做一次性处理**：只要让它修掉你PR上的评论（可选地给出更具体的指令），完成后推回PR分支即可。
  * **修复失败的构建**或linter警告。
  * 让Claude遍历开放的GitHub议题，**对未关闭议题做归类与分诊**。

这既免去了记忆 `gh` 命令行语法的麻烦，又把例行任务自动化了。
### h. 用Claude处理Jupyter笔记本
Anthropic的研究人员和数据科学家用Claude Code读写Jupyter笔记本。Claude能解读包括图片在内的输出，提供一种快速探索数据、与数据交互的方式。没有必需的提示词或工作流，但我们推荐的做法是在VS Code里把Claude Code和 `.ipynb` 文件并排打开。
在把Jupyter笔记本展示给同事之前，你也可以让Claude清理它或做些美观上的改进。明确告诉它把笔记本或其中的数据可视化做得「美观」，往往有助于提醒它：优化的目标是人类观看体验。
## 4\. 优化你的工作流
以下建议适用于所有工作流：
### a. 指令要具体
指令越具体，Claude Code的成功率就越高，首次尝试时尤其明显。一开始就把方向交代清楚，能减少后续纠偏的需要。
例如：
差
好
给foo.py加测试
给foo.py写一个新的测试用例，覆盖用户已登出的边界情况。不要用模拟
为什么ExecutionFactory的api这么怪？
翻一遍ExecutionFactory的git历史，总结它的api是怎么演变来的
加个日历组件
看看首页上现有组件是怎么实现的，理解其中的模式，特别是代码与接口是如何分离的。HotDogWidget.php是个不错的入手例子。然后照着这个模式实现一个新的日历组件，让用户能选择月份、向前/向后翻页挑选年份。从零构建，除了代码库其余部分已在用的库之外不要引入别的库。
Claude能推断意图，但它不会读心。具体才能更贴合预期。
![给Claude图片](assets/claude-code-best-practices/img_003.webp)
### b. 给Claude图片
Claude擅长通过多种方式处理图片和示意图：
  * **粘贴截图**(专业技巧：在macOS上按 _cmd+ctrl+shift+4_ 把截图存到剪贴板，再用 _ctrl+v_ 粘贴。注意这不是Mac上通常用来粘贴的cmd+v，且在远程环境下不管用。)
  * **拖放**图片，直接放进提示词输入框
  * 提供图片的**文件路径**

这在处理作为UI开发参考的设计稿，以及用于分析和调试的视觉图表时尤其有用。即便你不打算把视觉素材加进上下文，明确告诉Claude结果在视觉上是否美观有多重要，也仍然有帮助。
![提及你希望Claude查看或处理的文件](assets/claude-code-best-practices/img_004.png)
### c. 提及你希望Claude查看或处理的文件
用tab补全在仓库任意位置快速引用文件或文件夹，帮Claude找到或更新正确的资源。
![给Claude URL](assets/claude-code-best-practices/img_005.webp)
### d. 给Claude URL
把具体的URL连同提示词一起粘贴给Claude，让它抓取并阅读。为避免对相同域名（例如docs.foo.com）反复弹出权限提示，请用 __`/permissions` 把域名加进允许列表。
### e. 及早且频繁地纠偏
虽然自动接受模式（用shift+tab切换）能让Claude自主工作，但做一名积极的协作者、引导Claude的思路，通常能拿到更好的结果。最佳结果来自一开始就把任务向Claude讲透，但你也可以随时纠偏。
这四个工具有助于纠偏：
  * 在编码前**让Claude制定计划**。明确告诉它，在你确认计划没问题之前不要写代码。
  * **按Escape打断**Claude的任何阶段（思考、工具调用、文件编辑），这样能保留上下文，方便你重新定向或补充指令。
  * **连按两次Escape跳回历史**，编辑之前的一条提示词，换一个方向探索。你可以反复修改提示词、重试，直到拿到想要的结果。
  * **让Claude撤销改动**，常常与第2项配合，用来换一种做法。

尽管Claude Code偶尔能一次就把问题解得完美，但用上这些纠偏工具，通常能更快地得到更好的方案。
### f. 用 `/clear` 保持上下文聚焦
在长会话中，Claude的上下文窗口可能被无关的对话、文件内容和命令塞满。这会降低表现，有时还会让Claude分心。在任务之间频繁使用 `/clear` 命令来重置上下文窗口。
### g. 对复杂工作流使用清单和草稿本
对于步骤繁多或要求穷尽解决的大任务——比如代码迁移、修复大量lint错误、运行复杂构建脚本——让Claude用一个Markdown文件（甚至一个GitHub议题！）当清单和工作草稿本，能提升表现：
例如，要修复大量lint问题，你可以这样做：
  1. **让Claude运行lint命令**，把所有产生的错误（连同文件名和行号）写进一份Markdown清单
  2. **指示Claude逐条处理每个问题**，修复并验证后再勾掉，然后移向下一条

### h. 把数据传给Claude
向Claude提供数据有几种方式：
  * 直接**复制粘贴**进提示词（最常见的做法）
  * **通过管道传给Claude Code**（例如 `cat foo.txt | claude`），对日志、CSV和大数据尤其有用
  * **让Claude拉取数据**，通过bash命令、MCP工具或自定义斜杠命令
  * **让Claude读取文件**或抓取URL（对图片同样有效）

大多数会话会组合使用这几种方式。例如，你可以先用管道传入一个日志文件，然后让Claude用某个工具拉取更多上下文来调试这些日志。
## 5\. 用无头模式自动化你的基础设施
Claude Code为CI、预提交钩子、构建脚本和自动化这类非交互场景提供了[无头模式](<https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview#automate-ci-and-infra-workflows>)。用带提示词的 `-p` 标志启用无头模式，用 `--output-format stream-json` 输出流式JSON。
注意，无头模式不会在会话之间保持。你必须在每个会话里分别触发它。
### a. 用Claude做议题分诊
无头模式可以驱动由GitHub事件触发的自动化，比如仓库里新建议题时。例如，公开的[Claude Code仓库](<https://github.com/anthropics/claude-code/blob/main/.github/actions/claude-issue-triage-action/action.yml>)就用Claude在新议题进来时检查它们并打上合适的标签。
### b. 用Claude当linter
Claude Code能提供传统lint工具检测不到的[主观代码评审](<https://github.com/anthropics/claude-code-action/blob/main/action.yml>)，识别错别字、过时注释、误导性的函数或变量名等问题。
## 6\. 用多Claude工作流更上一层楼
除了单独使用，一些最强大的用法还涉及并行运行多个Claude实例：
### a. 让一个Claude写代码，用另一个Claude验证
一个简单却有效的做法是让一个Claude写代码，另一个审查或测试它。和多人协作类似，有时把上下文分开是有益的：
  1. 用Claude写代码
  2. 运行 `/clear`，或在另一个终端启动第二个Claude
  3. 让第二个Claude审查第一个Claude的工作
  4. 再启动一个Claude（或再 `/clear` 一次）来同时阅读代码和评审反馈
  5. 让这个Claude根据反馈修改代码

用测试也能做类似的事：让一个Claude写测试，再让另一个Claude写代码让测试通过。你甚至可以让多个Claude实例互相通信——给它们各自独立的工作草稿本，并指明哪个用来写、哪个用来读。
这种分工往往比让单个Claude包办一切得到更好的结果。
### b. 使用仓库的多个检出副本
与其等Claude一步步做完，Anthropic许多工程师的做法是：
  1. 在不同文件夹里**创建3—4个git检出副本**
  2. 在不同的终端标签页里**分别打开每个文件夹**
  3. **在每个文件夹里启动Claude**，各自分配不同任务
  4. **轮流查看**进度，批准/拒绝权限请求

### c. 使用git worktree
对多个相互独立的任务，这个方法尤为出彩，是多个检出副本的轻量替代方案。git worktree允许你把同一仓库的多个分支检出到不同目录。每个worktree有自己独立的工作目录和隔离的文件，同时共享同一份Git历史和reflog。
使用git worktree能让你在项目的不同部分同时运行多个Claude会话，各自专注于自己独立的任务。例如，你可以让一个Claude重构认证系统，同时让另一个构建完全无关的数据可视化组件。由于任务不重叠，每个Claude都能全速工作，无需等待对方的改动，也不用处理合并冲突：
  1. **创建worktree**：`git worktree add ../project-feature-a feature-a`
  2. **在每个worktree里启动Claude**：`cd ../project-feature-a && claude`
  3. 按需**创建更多worktree**（在新的终端标签页里重复第1—2步）

一些小建议：
  * 使用一致的命名约定
  * 每个worktree保持一个终端标签页
  * 如果你在Mac上用iTerm2，可以[设置通知](<https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview#notification-setup>)，在Claude需要关注时提醒你
  * 为不同worktree使用独立的IDE窗口
  * 收尾时清理：`git worktree remove ../project-feature-a`

### d. 用自定义框架搭配无头模式
`claude -p`（无头模式）把Claude Code以编程方式集成进更大的工作流，同时利用它内置的工具和系统提示词。使用无头模式有两种主要模式：
1\. **扇出**用于处理大规模迁移或分析（例如分析数百份日志的情感倾向，或分析数千个CSV）：
  1. 让Claude写一个脚本来生成任务清单。例如，生成一份需要从框架A迁移到框架B的2千个文件清单。
  2. 遍历任务，对每个任务以编程方式调用Claude，给它一个任务和一组可用工具。例如：`claude -p “migrate foo.py from React to Vue. When you are done, you MUST return the string OK if you succeeded, or FAIL if the task failed.” --allowedTools Edit Bash(git commit:*)`
  3. 把脚本跑几遍，打磨提示词，直到拿到想要的结果。

2\. **流水线**把Claude集成进现有的数据/处理流水线：
  1. 调用 `claude -p “<your prompt>” --json | your_command`，其中 `your_command` 是处理流水线的下一步
  2. 就这样！JSON输出（可选）有助于提供结构，便于自动化处理。

对这两类用例，用 `--verbose` 标志调试Claude调用会很有帮助。我们一般建议在生产环境关掉详细模式，让输出更干净。
你有哪些使用Claude Code的技巧和最佳实践？@AnthropicAI告诉我们，好让我们看到你在构建什么！
## 作者与致谢
### 致谢
作者Boris Cherny。这项工作汲取了更广泛的Claude Code用户社区的最佳实践，他们富有创意的方法与工作流持续给我们带来启发。特别感谢Daisy Hollman、Ashwin Bhat、Cat Wu、Sid Bidasaria、Cal Rueb、N.T.A.、Barry Zhang、Drew Hodun，以及许多其他Anthropic工程师，他们在Claude Code上的宝贵洞见与实践经验帮助塑造了这些建议。
