---
title: Project Fetch: Phase two
url: https://www.anthropic.com/research/project-fetch-phase-two
date: Jun 18, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# Project Fetch：第二阶段

- **日期：** 
- **分类：** 前沿红队（Frontier Red Team）
- **来源：** https://www.anthropic.com/research/project-fetch-phase-two

---

前沿红队
2026年6月18日
![Project Fetch: Phase two](assets/project-fetch-phase-two/img_000.svg)
 _Michael Ilie、C. Daniel Freeman 和 Kevin K. Troy_
2025 年 8 月，我们进行了一项[实验](<https://www.anthropic.com/research/project-fetch-robot-dog>)，看看 Claude 能在多大程度上帮助 Anthropic 员工——他们不是机器人专家——用一台现成的四足机器人（以下简称机器狗）完成复杂（且有趣）的任务。我们称之为 Project Fetch。我们发现，使用我们当时最先进的模型（Claude Opus 4.1）帮助一个团队显著超越了另一个团队，后者只能依靠互联网和自己的聪明才智。有 Claude 加持的团队做得更多、更快。
在我们把同事拖到仓库做实验之前，我们仔细检查了 Opus 4.1 是否能完全独立完成这些任务。毫无疑问，它不能。就像我们没有 Claude 的团队一样，它卡在了弄清楚如何连接到机器人的初步任务上。
但 AI 模型进展很快——甚至比去年 8 月差点撞上我们人类团队的那只失控的机器狗还快。
我们认为该重新审视 Project Fetch 了，看看我们的新模型能否超越上一代。它们不仅做到了，而且**Claude Opus 4.7——在无人辅助的情况下运作——在不到一年前我们参与者完成的所有任务上，比最快的人类团队快了约 20 倍**。
这并不意味着 LLM 现在已经解决了机器人技术。远非如此。最新的 Claude 模型在用机器人精确移动沙滩球——Project Fetch 的"取回"部分——方面仍然很挣扎。而且这些实验中的任何任务都不涉及机器人控制更具挑战性的底层元素，如开发特定的驱动策略。然而，我们再次看到一种模式：首先，模型对人类有帮助。然后，人类对模型有帮助。最后，模型在很大程度上能够自己做事情。我们在[网络安全](<https://red.anthropic.com/2026/mythos-preview/>)中看到了这一点，现在同样的动态开始在 AI 与物理世界的交汇处成形。
## 我们做了什么？
最初的 Project Fetch 让 Anthropic 员工团队（随机分配到有或没有 Claude 的组）完成以下步骤：使用制造商提供的控制器操作机器狗，连接到机器狗的摄像头和激光雷达（lidar）传感器，编写并运行一个手动控制机器狗的程序，开发一种监控机器狗在空间中路径的方法，编写一个检测沙滩球的程序，最后把所有东西整合起来自主取回球。
对于这次自主更新，我们不能让 Claude 使用物理控制器，我们也没有评估研究员使用 Claude 编程的控制器取回球所花的时间（尽管我们确认了它按预期工作）。在其余的任务子集上，我们用 Claude Code 中的自适应思考并把努力程度设置为最大，运行了三次 Opus 4.7 试验。我们测量了每个目标的耗时，并定性评估了模型的成功程度。
我们研究员的角色仅限于把运行着 Claude Code 的笔记本电脑接入机器狗、输入初始提示、批准命令，以及批准模型进入下一个任务。
## Claude 在哪里表现出色？
非常简单：在 8 月至少被一个人类团队完成的每个任务上，Opus 4.7 完成同一任务的速度至少快十倍。1 如果你考虑两个人类团队都完成的四个任务，Opus 4.7 平均比无 Claude 团队快 37 倍以上，比有 Claude 团队快 18 倍以上。
![Bar chart labeled "Total time comparison: 4 tasks completed by all teams." The chart shows that Team Claude-less completed tasks in 361 minutes; Team Claude completed tasks in 181 minutes, and Claude Opus 4.7 alone completed tasks in 9 minutes 35 seconds. Opus 4.7 was 37.7 times faster than Team Claude-less and 18.9 times faster than Team Claude.](assets/project-fetch-phase-two/img_001.img)
该表把原始团队（有 Claude 团队和无 Claude 团队）的速度与 Opus 4.7 在我们作为第二阶段一部分测试的所有任务上进行了比较。
![Table comparing Claude Opus 4.7 to Team Claude-less and Team Claude performance on tasks related to programmatic control and autonomous operation. Tasks include "Connect to robodog's video camera," "Connect to robodog's lidar sensor," and "Detect beach ball." Opus 4.7 was faster than Team Claude-less and Team Claude on all tasks. Team Claude-less did not complete all 5 tasks in the table; Team Claude completed them in 264 minutes; and Opus 4.7, averaged over 3 trials, completed them in 12 minutes 7 seconds.](assets/project-fetch-phase-two/img_002.img)
人类在多种与机器狗传感器交互的方法之间挣扎取舍，而 Opus 4.7 能够快速识别最佳路径。它编写的大部分代码首次尝试就有效（原始实验中，有 Claude 团队和无 Claude 团队都不是这样）。事实上，当我们查看它生成的代码量时，可以看到 Opus 4.7 效率的证据：它比两个人类团队都更成功或同样成功，同时生成的代码比有 Claude 团队少了近十倍。
![Bar chart showing total code volume for Team Claude, Team Claude-less, and Opus 4.7 alone. Team Claude wrote 10,309 lines of code; Team Claude-less wrote 1,136 lines of code; Opus 4.7 alone wrote 1,045 lines of code.](assets/project-fetch-phase-two/img_003.img)
Opus 4.7 并不完美。例如，它默认使用了一个过时的目标检测算法。但即便如此，它也能绕过这个问题，得出一个有效的解决方案。
我们观察到，模型完成的步骤在完成时间上的任务内方差（绝对值）很小。（尽管前面提到的次优算法选择很可能是某次沙滩球检测试验花费的时间明显长于其他几次的原因。）总体而言，对于这个实验中在其能力包络内的任务，Claude 现在已经相当可靠。（关于 Claude 仍然做不到什么的分析，见下一节。）
![Scatter plot showing Opus 4.7's reliability on task performance. Opus 4.7 performed each task three times; the scatter plot shows that the performance time was relatively consistent across runs. ](assets/project-fetch-phase-two/img_004.img)
值得强调（正如我们在上一篇文章中所做的那样），这种进步并不是为改进我们模型机器人能力而做出的协同努力的结果。这些改进，就像 LLM 发展史上的许多其他改进一样，来自更普遍的规模扩展。
## Claude 在哪里挣扎？
当使用双手并经过一些练习后，我们的人类能够操纵机器狗，轻轻把沙滩球推回机器人出发的基地（一小块假草）。这需要能够快速感知球是否偏离了路线、该误差与先前命令的关系、球现在在哪里，以及如何调整未来的输入以更精确地移动球。这是一种人们擅长的闭环（至少在犯一些错误并从中学习之后）。
在我们的第二阶段实验中，Claude 难以捕捉这种微妙之处。像到达需要编写自主取回沙滩球程序阶段的人类一样，Claude 能够把机器人移到球后面，并把它定位来把球敲回起点。但这样做的努力控制得很差，而且（再次像我们的人类参与者一样）没有成功。
我们的一位比第一阶段志愿者更有机器人经验的研究员成功完成了编程自主取回的任务。有了更多的时间和额外的脚手架，我们认为当前几代 Claude 很可能也能做到同样的事情。不过，我们接下来要观察的是，模型能否以它们在 Project Fetch 其他元素上展示的速度和可靠性完成这最后一个任务。
## 这意味着什么？
在写第一阶段时，我们强调了 LLM 如何为需要用到机器人的非专家人类提供提升。现在这比以往任何时候都更真实。模型现在自己完成以前是人类和模型之间的结对编程（pair-programming）工作，速度快得多，这意味着人们可以更快地过渡到控制和操作机器人。而且对于某些任务，一个在环的人类控制机器人可能仍然胜过把手（虚拟地）放在方向键上的 AI 模型。
有趣且不同的是，我们现在似乎更接近这样一个世界：模型将能够相对轻松地使用现成的物理工具——至少在有限用途上是如此。这类似于 AI 模型在向更智能体的编码过渡时使用现有的软件编辑工具（如字符串替换）。我们很可能正在进入_物理_智能体 AI 的早期时代。
需要更多研究来理解模型把这些物理工具变得更加定制化的能力，无论是通过编写针对特定任务的控制策略，还是通过设计机器人系统。而且这个更广义的、具有物理能力和适应性的语言模型愿景可能存在重大障碍。但正如我们所见，模型能力上看似巨大的距离可以快速跨越。模型构建自己的软件工具在不久前可能显得古怪，但它正在发生。排除硬件领域的相同轨迹将是不明智的。
_6 月 18 日更新：_ 更正了 Project Fetch 第一阶段的日期。
#### 脚注
  1. 我们报告 Claude Opus 4.7 的结果，因为在我们运行这个实验时，它是最先进的非 Mythos 类模型。Claude Mythos Preview 的初步试验表明，由于我们设置实验和提供服务模型的方式，它无法与其他模型进行同类比较。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/project-fetch-phase-two>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/project-fetch-phase-two>)
## 相关内容
### 了解更多关于 Claude 的数学能力
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足该猜想的黎曼 zeta 函数零点比例的下界——将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而设计的数字签名方案。第二个攻击确定了一种攻击减轮 AES（最广泛使用的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新评估，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)
## 订阅前沿红队通讯
获取我们最新的红队研究和发现更新。