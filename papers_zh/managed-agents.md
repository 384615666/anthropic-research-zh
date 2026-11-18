---
title: Scaling Managed Agents:Decoupling the brain from the hands
url: https://www.anthropic.com/research/managed-agents
date: Apr 8, 2026
category: Engineering
source: https://www.anthropic.com/research
---

# 扩展 Managed Agents：将大脑与双手解耦

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/managed-agents

---

工程（Engineering）
2026 年 4 月 8 日
已发布
    2026 年 4 月 8 日
团队
    [工程](</engineering>)
主题
    
  * [智能体](</search?topic=agents>)
  * [Claude 开发者平台](</search?topic=claude-developer-platform>)
  * [上下文工程](</search?topic=context-engineering>)
  * [工具使用](</search?topic=tool-use>)
  * [安全防护](</search?topic=safeguards>)

[](</news/anthropic-acquires-stainless>)[](</research/effective-harnesses-for-long-running-agents>)[](</research/advanced-tool-use>)[](</research/effective-context-engineering-for-ai-agents>)
相关文章
  * 公告
2026 年 5 月 18 日
[Anthropic 收购 Stainless](</news/anthropic-acquires-stainless>)

[查看更多](</search?topic=agents>)
 _按照我们的[文档](<https://platform.claude.com/docs/en/managed-agents/overview>)开始使用 Claude Managed Agents。_  
  
工程博客里一个持续出现的话题，是如何[构建高效的智能体](<https://www.anthropic.com/engineering/building-effective-agents>)并[设计脚手架](<https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>)来支撑[长时运行的任务](<https://www.anthropic.com/engineering/harness-design-long-running-apps>)。这些工作有一条共同主线：脚手架把关于 Claude 靠自己做不到什么的假设编码了进去。然而，这些假设需要经常受到质疑，因为随着模型进步，它们可能会[过时](<http://www.incompleteideas.net/IncIdeas/BitterLesson.html>)。
仅举一例，在此前的工作中[我们发现](<https://www.anthropic.com/engineering/harness-design-long-running-apps>)，Claude Sonnet 4.5 在察觉上下文上限临近时会过早收尾任务——这种行为有时被称为「上下文焦虑」（context anxiety）。我们通过在脚手架中加入上下文重置来解决它。但当我们把同一套脚手架用到 Claude Opus 4.5 上时，发现这种行为消失了。那些重置成了累赘。
我们预计脚手架会持续演进。因此我们构建了 Managed Agents：这是 Claude Platform 中的一项托管服务，通过一小组接口替你运行长时程智能体，而这组接口的设计意在比任何具体实现都活得更久——包括我们今天正在运行的这些。
构建 Managed Agents 意味着要解决计算领域的一个老问题：如何为「[尚未被构想出来的程序](<http://www.catb.org/esr/writings/taoup/html/ch03s01.html>)」设计一套系统。几十年前，操作系统通过把硬件虚拟化为抽象—— _进程（process）、文件（file）_ ——解决了这个问题，这些抽象足够通用，能容纳当时还不存在的程序。抽象比硬件活得更久。`read()` 命令并不关心自己访问的是 1970 年代的磁盘组还是现代的 SSD。上层的抽象保持稳定，下层的实现则可以自由变化。
Managed Agents 遵循同样的模式。我们把智能体的各个组成部分虚拟化了：会话（session，一份只追加、记录所发生一切的日志）、脚手架（harness，一个调用 Claude、并把 Claude 的工具调用路由到相应基础设施的循环）以及沙箱（sandbox，一个让 Claude 能运行代码、编辑文件的执行环境）。这样一来，每一部分的实现都可以被替换而不打扰其他部分。我们对这些接口的形态有明确主张，但对背后运行什么并不设限。
![](assets/managed-agents/img_000.webp)
## 别养一只「宠物」
我们最初把所有智能体组件都放进一个容器里，这意味着会话、智能体脚手架和沙箱共享同一个环境。这种做法有好处，比如文件编辑就是直接的系统调用，也不需要设计服务边界。
但把一切耦合进同一个容器后，我们撞上了一个老的基础设施问题：我们养了一只[_宠物_](<https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/>)。在「宠物对牲畜」（pets-vs-cattle）的类比中，宠物是有名字、需要精心照料、失去不起的个体，而牲畜则是可以互换的。在我们的情形里，服务器成了那只宠物：容器一旦故障，会话就丢了；容器一旦无响应，我们就得把它照料回健康状态。
照料容器，意味着要调试无响应的卡死会话。我们唯一的观察窗口是 WebSocket 事件流，但它无法告诉我们故障出在 _哪里_：脚手架里的 bug、事件流中的丢包、或者容器下线，表现出来的样子都一样。为了弄清哪里出了错，工程师不得不在容器里打开一个 shell；但由于那个容器往往还存着用户数据，这种做法实际上等于我们根本没有调试能力。
第二个问题在于，脚手架假定 Claude 处理的一切都和它待在同一个容器里。当客户要求把 Claude 接入他们的虚拟私有云时，他们要么得把自己的网络与我们的对等互联，要么得在自己的环境里运行我们的脚手架。一个被写死进脚手架的假设，在我们想把它接到不同基础设施上时成了麻烦。
## 把大脑与双手解耦
我们最终采用的方案，是把我们所说的「大脑」（Claude 及其脚手架）与「双手」（执行动作的沙箱和工具）以及「会话」（会话事件的日志）两者都解耦开来。每一部分都变成一个对其他部分几乎不作假设的接口，也都可以独立地故障或被替换。
**脚手架搬出容器。** 把大脑与双手解耦，意味着脚手架不再住在容器里。它调用容器的方式，和调用任何其他工具一样：`execute(name, input) → string`。容器于是成了牲畜。如果容器挂了，脚手架会把这次故障当作一次工具调用错误捕获下来，再传回给 Claude。如果 Claude 决定重试，就可以用一套标准配方重新初始化一个新容器：`provision({resources})`。我们再也不必把故障容器照料回健康状态。
**从脚手架故障中恢复。** 脚手架同样成了牲畜。由于会话日志位于脚手架之外，脚手架里没有任何东西需要在崩溃后存活。当某个脚手架失效时，可以用 `wake(sessionId)` 重启一个新的，再用 `getSession(id)` 取回事件日志，从最后一个事件继续。在智能体循环中，脚手架通过 `emitEvent(id, event)` 向会话写入，以保留一份持久的事件记录。
![](assets/managed-agents/img_001.png)
**安全边界。** 在耦合式设计中，Claude 生成的任何不受信任代码都与凭据运行在同一个容器里——因此一次提示注入只要说服 Claude 去读取自己的环境就够了。攻击者一旦拿到那些令牌，就能派生出全新的、不受限制的会话，并把工作委派给它们。收窄权限范围是一种显而易见的缓解手段，但这同样编码了一个关于「Claude 拿着受限令牌做不了什么」的假设——而 Claude 正变得越来越聪明。结构性的解决办法，是确保这些令牌永远无法从 Claude 生成代码所运行的沙箱中被触达。
我们用两种模式来保证这一点。认证信息可以随某个资源捆绑，也可以存放在沙箱之外的保险库里。对于 Git，我们在沙箱初始化时用每个仓库的访问令牌来克隆仓库，并把它接入本地的 git remote。Git 的 `push` 和 `pull` 能在沙箱内部工作，而智能体从头到尾都不必自己经手令牌。对于自定义工具，我们支持 MCP，并把 OAuth 令牌存放在安全的保险库中。Claude 通过一个专用代理调用 MCP 工具；该代理接收一个与会话关联的令牌，随后便可从保险库取出相应凭据，再向外部服务发起调用。脚手架自始至终都不会得知任何凭据。
## 会话不是 Claude 的上下文窗口
长时程任务往往超出 Claude 上下文窗口的长度，而应对这一问题的标准做法，都涉及「保留什么」这类不可逆的决定。我们在此前关于上下文工程的[工作](<https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>)中探讨过这些技术。例如，压缩让 Claude 能保存其上下文窗口的摘要，记忆工具则让 Claude 把上下文写入文件，从而实现跨会话的学习。这可以与上下文裁剪配合使用，选择性地移除旧的工具结果或思考块之类的 token。
但是，选择性地保留或丢弃上下文这种不可逆决定，可能导致失败。我们很难知道未来的轮次会需要哪些 token。如果消息被某次压缩步骤改写，脚手架会把压缩过的消息从 Claude 的上下文窗口中移除，而它们只有在被存储下来时才可恢复。此前的[研究](<https://arxiv.org/pdf/2512.24601>)探讨过解决之道：把上下文存储为一个活在上下文窗口 _之外_ 的对象。例如，上下文可以是 REPL 中的一个对象，让大语言模型通过编写代码来过滤或切片，以编程方式访问它。
![](assets/managed-agents/img_002.webp)
在 Managed Agents 中，会话提供了同样的好处，充当了一个位于 Claude 上下文窗口之外的上下文对象。不过，上下文并不是存放在沙箱或 REPL 里，而是持久地存进会话日志中。`getEvents(),` 这个接口让「大脑」能够通过选取事件流中按位置切分的片段来查询上下文。这个接口使用起来很灵活：大脑既可以从上次读到的地方接着往下读，也可以回退到某个特定时刻之前的几个事件、看清来龙去脉，还可以在某个特定动作之前重读上下文。
任何取回的事件，也可以在传入 Claude 的上下文窗口之前先在脚手架里做变换。这些变换可以是脚手架所编码的任何形式，包括为了获得较高提示缓存命中率而做的上下文组织，以及上下文工程。我们把「会话中可恢复的上下文存储」与「脚手架中任意的上下文管理」这两件事分开，是因为无法预测未来的模型会需要什么样的具体上下文工程。这些接口把上下文管理推给脚手架，只保证会话是持久的、并且可供查询。
## 多个大脑，多双手
**多个大脑。** 把大脑与双手解耦，解决了我们最早收到的客户抱怨之一。当团队想让 Claude 使用他们自己 VPC 里的资源时，唯一的办法是把他们的网络与我们的对等互联，因为装着脚手架的那个容器假定所有资源都近在咫尺。一旦脚手架不再待在容器里，这个假设就不复存在。同一改动还带来了性能回报。我们最初把大脑放进容器时，意味着有多少个大脑就得有多少个容器。对每个大脑而言，在容器准备好之前都无法进行推理；每个会话都要预先付清整套容器启动成本。每一个会话——哪怕根本不会碰沙箱——都得克隆仓库、启动进程、从我们的服务器拉取待处理事件。
这段空转时间体现在首 token 时延（time-to-first-token，TTFT）上，它衡量的是一个会话从接下任务到产出第一个响应 token 之间要等待多久。TTFT 正是用户感受最 _真切_ 的那部分延迟。
把大脑与双手解耦，意味着容器只在需要时，才由大脑通过一次工具调用 `(execute(name, input) → string)` 来准备。因此，一个当下并不需要容器的会话就不必为它等待。只要编排层从会话日志中拉取到待处理事件，推理就可以开始。采用这套架构后，我们的 p50 TTFT 下降了约 60%，p95 下降了 90% 以上。扩展到多个大脑，只不过意味着启动多个无状态脚手架，并只在需要时才把它们接上双手。
**多双手。** 我们还希望每个大脑都能接上多双手。在实践中，这意味着 Claude 必须对多个执行环境进行推理，并决定把工作发往哪里——这比在单个 shell 里操作是更难的认知任务。我们最初把大脑放在单个容器里，是因为早期的模型还做不到这一点。随着智能水平提升，单个容器反而成了限制：一旦那个容器故障，大脑正探入的每一只手的状态都会丢失。
把大脑与双手解耦后，每只手都成了一个工具：`execute(name, input) → string`——送进去一个名字和输入，返回来一个字符串。这个接口支持任何自定义工具、任何 MCP 服务器，以及我们自己的工具。脚手架并不知道沙箱究竟是一个容器、一部手机，还是一个 Pokémon 模拟器。而且由于没有任何一只手与某个大脑绑定，大脑之间可以互相转交双手。
![](assets/managed-agents/img_003.webp)
## 结论
我们面对的是一个老挑战：如何为「尚未被构想出来的程序」设计一套系统。操作系统之所以能延续数十年，靠的是把硬件虚拟化为足够通用的抽象，以容纳当时还不存在的程序。借助 Managed Agents，我们希望设计出一套能容纳未来脚手架、沙箱，或 Claude 周边其他组件的系统。
本着同样的精神，Managed Agents 是一套元脚手架（meta-harness），对未来 Claude 究竟需要哪 _一种具体_ 脚手架不持立场。它更像是一个带有通用接口的系统，能容纳许多不同的脚手架。例如，Claude Code 就是一套出色的脚手架，我们在各类任务中广泛使用。我们也已经证明，针对特定任务的智能体脚手架在狭窄领域里表现卓越。Managed Agents 能容纳上述任何一种，并随着时间推移与 Claude 的智能水平相匹配。
元脚手架的设计，意味着要对 Claude 周边的接口有明确主张：我们预期 Claude 需要具备操纵状态（会话）和执行计算（沙箱）的能力，也预期 Claude 需要能够扩展到多个大脑与多双手。我们设计这些接口，是为了让它们能在长时间跨度上可靠、安全地运行。但对于 Claude 究竟需要多少个大脑、多少双手、以及它们位于何处，我们不作任何假设。
## 作者与致谢
### 致谢
本文由 Lance Martin、Gabe Cemaj 和 Michael Cohen 撰写。感谢 N.T.A. 和 Jeremy Fox 就这些话题带来的有益讨论。特别感谢 Agents API 团队和 Jake Eaton 的贡献。
