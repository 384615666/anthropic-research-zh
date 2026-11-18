---
title: Long-running Claude for scientific computing
url: https://www.anthropic.com/research/long-running-Claude
date: Mar 23, 2026
category: Science
source: https://www.anthropic.com/research
---

# 用于科学计算的长时间运行 Claude

- **日期：**
- **分类：** 科学
- **来源：** https://www.anthropic.com/research/long-running-Claude

---

科学
2026 年 3 月 23 日
![用于科学计算的长时间运行 Claude](assets/long-running-Claude/img_000.svg)
_在这篇文章中，Discovery 团队的研究员 Siddharth Mishra-Sharma 解释了如何将多日的智能体编码工作流程——测试预言机（test oracle）、持久记忆和编排模式——应用到科学计算任务中，即使不在自己的专业领域内。_
### **前提**
目前大多数使用 AI 智能体的科学家都处于对话式循环中，紧绷地管理着过程的每一步。随着过去一年左右模型在[长时程任务上显著变得更好](<https://metr.org/time-horizons/>)，一种新的工作方式出现了：与其介入每一个细节，我们可以指定高层目标，让一队智能体自主工作。这使得原本可能需要我们几天、几周甚至几个月的项目，能在仅仅几小时内完成。某些类型的科学任务非常适合这种模式，例如重新实现数值求解器、将用旧 Fortran 方言编写的遗留科学软件转换为现代语言，以及对照参考实现调试大型代码库。这些任务的特点是工作范围明确、成功标准清晰，人类监督可以是偶尔的而不是持续的。
Anthropic 的 [C 编译器项目](<https://www.anthropic.com/engineering/building-c-compiler>)展示了这一模式的一个版本，Claude 在大约 2,000 个会话中工作，构建了一个能够编译 Linux 内核的 C 编译器。这篇文章描述了如何使用 Claude Code 为科学计算任务设置类似的模式，以典型的学术实验室为背景。作为一个具体例子，我将逐步介绍使用 Claude Opus 4.6 [实现宇宙学玻尔兹曼求解器的可微分版本](<https://github.com/smsharma/clax>)。这是一种数值代码，用于预测大爆炸余晖——宇宙微波背景（Cosmic Microwave Background，CMB）——的统计性质。它通过演化早期宇宙中光子、重子、中微子和暗物质的耦合方程来实现这一点。
像 [CLASS](<http://class-code.net/>) 和 [CAMB](<https://camb.info/>) 这样的玻尔兹曼求解器是宇宙学中科学基础设施的核心部分，使我们能够利用 _Planck_ 和 _Simons Observatory_ 等巡天的数据来约束宇宙学模型。一个可微分的版本——能够将梯度传播通过整个求解器——使得基于梯度的推理方法成为可能，极大地加速参数估计。用 JAX 编写是一个自然的选择，因为它几乎免费地给了我们自动微分和对加速器（例如 GPU）的兼容性。
  
值得注意的是，这个任务不在我的核心科学领域内——我对这些工具和科学有高层面的熟悉度，但没有在合理时间内自己完成它的专业知识。_确实_拥有这方面专业知识的团队已经在 JAX 中构建了[可微分的](<https://arxiv.org/abs/2311.03291>)[求解器](<https://arxiv.org/abs/2602.15104>)，具有 CLASS 中功能的一个子集。这些努力通常代表数月到数年的研究人员时间。这里的重点是看一个智能体能否在非领域专家的最小引导下走得更远。
这类任务在结构上不同于 C 编译器项目，后者可以分派给大量并行智能体。另一方面，玻尔兹曼求解器是一个深度耦合的流水线——在模拟早期宇宙重组时，一个小的数值错误或糟糕的近似可以微妙地偏移下游的一切。因此它需要一套不同的智能体技能。调试需要因果地追踪整个链条并借鉴领域知识，这可能更适合一个按顺序工作的智能体，在需要时生成子智能体，并使用参考实现来对差异进行二分定位。
我们将使用运行 SLURM 作业调度器的 HPC 集群作为我们的计算环境，但核心思想——进度文件、测试预言机、带有清晰规则的智能体提示词——无论你在哪里运行 Claude Code 都适用。
### **起草计划并在本地迭代**
在这种转向管理自主研究智能体团队的方式中，你应该花大部分时间（与 Claude 协商）精心制作一套清晰阐明项目交付物和相关背景的指令。这些指令应该放在根目录的 CLAUDE.md 文件中。Claude 会特别对待这个文件，将其保持在上下文中，并参照它来制定总体计划。至关重要的是，Claude 可以在工作时编辑这些指令，在解决问题时为未来的工作更新它们。
[这里](<https://github.com/smsharma/clax/blob/6a6b2330cf25edded1bb31ec57a0091aa794a5d3/CLAUDE.md>)是宇宙学玻尔兹曼求解器项目早期的一个 CLAUDE.md，显示了在最初尝试编写求解器后编码化的总体计划和设计决策。为了得出这个，我指定了项目的高层目标——与参考 CLASS 实现实现完全的功能对等，同时完全可微分，并在主要科学交付物上对 CLASS 有 0.1% 的精度目标——并与 Claude 迭代，直到计划看起来令人满意。鉴于 0.1% 是两个经典玻尔兹曼代码 CLASS 和 CAMB 之间的典型一致水平，这似乎是一个很好的科学目标。
### **跨会话的记忆**
进度文件（我们按惯例在这里称为 CHANGELOG.md）是智能体的便携式长期记忆，起到某种实验室笔记的作用。在 CLAUDE.md 中，Claude 被指示在这个文件中跟踪进度。
一个好的进度文件可能跟踪当前状态、已完成的任务、失败的方法及其失败原因、关键检查点处的精度表，以及已知的局限。失败的方法很重要——没有它们，后续会话会重新尝试同样的死胡同。一个条目可能看起来像：“尝试对扰动 ODE 使用 Tsit5，系统太刚性。切换到 Kvaerno5。”[这里](<https://github.com/smsharma/clax/blob/main/CHANGELOG.md>)是运行示例的变更日志，展示了这些元素。
### **测试预言机**
虽然通过智能体进行更开放的科学发展肯定即将到来，但今天长时间运行的自主科学工作关键地依赖于智能体有一种知道它是否在取得进展的方式。对于科学代码，这可能是一个参考实现、一个清晰可量化的目标，或一个现有的测试套件。指示智能体在工作时扩展测试套件并运行测试，以防止回归，也可能有帮助。在我的示例任务中，Claude 被指示使用 [CLASS C 源码](<https://github.com/lesgourg/class_public>)作为参考实现来构建并持续运行单元测试。
### **Git 作为协调工具**
Git 可以是一种以不干预的方式监控和协调智能体进展的好方法。智能体应该在每个有意义的工作单元后提交并推送。这给了你可恢复的历史（如果出了差错），使进展在本地可见，并防止工作丢失——例如，如果你的计算分配在会话中途用完的话。
实际上，这可以是在 CLAUDE.md 中的一组指令，例如“在每个有意义的工作单元后提交并推送。每次提交前运行 `pytest tests/ -x -q`。永远不要提交破坏现有通过测试的代码。”
为了引导智能体，你总是可以 SSH 到集群并手动重新提示和/或更新它的指令。更符合人体工程学的做法通常只是让本地实例的 Claude Code SSH 进去并为你运行命令；这也将适用于下面描述的一切。
### **执行循环**
如上所述，通常有用的是先在本地迭代计划，直到你有一个看起来合理并编码在 CLAUDE.md 中的计划。从那里，在计算节点上终端复用器（如 tmux）内启动一个 Claude Code 会话，告诉智能体在哪里找到你的代码库，然后让它自己工作。因为会话在 tmux 内运行，你可以分离、合上笔记本电脑，并偶尔检查进展（就玻尔兹曼求解器而言，我会在手机上查看 GitHub，例如在排队买咖啡时）。
在 HPC 集群上，你可能会通过 SLURM 调度器请求一个节点，一个在 tmux 会话中启动 Claude Code 的示例作业脚本可能看起来像下面这样：
    
    #!/bin/bash
    #SBATCH --job-name=claude-agent
    #SBATCH --partition=GPU-shared
    #SBATCH --gres=gpu:h100-32:1
    #SBATCH --time=48:00:00
    #SBATCH --output=agent_%j.log
    cd $PROJECT/my-solver
    source .venv/bin/activate
    export TERM=xterm-256color
    tmux new-session -d -s claude "claude; exec bash"
    tmux wait-for claude
  
作业启动后，你附加到 tmux 会话，给 Claude Code 指示（例如，“阅读 CHANGELOG.md 并接手下一个任务”），当你满意它在正轨上时分离。你可以随时重新附加以检查、引导或启动新任务，使用类似这样的命令：
    
    srun --jobid=JOBID --overlap --pty tmux attach -t claude
  
**Ralph 循环：** 随着模型能力的增强，它们需要更少的定制编排，如提示词工程、RAG 或上下文填充。然而，在某个时间点，提供一定程度的脚手架作为能力提升可能是有用的。例如，当前模型可能遭受_智能体懒惰_（agentic laziness）——当被要求完成一个复杂的多部分任务时，它们有时会找到一个借口在完成整个任务之前停下来（“时间不早了，我们明天再继续吧？”）。
为了规避这一点，一个有用的编排模式是 [_Ralph 循环_](<https://ghuntley.com/loop/>)，它本质上是一个_for_循环，当智能体声称完成时把它踢回上下文中，并问它是否_真的_做完了。这对长时间运行的任务可能很有用，因为智能体会承认任务没有达到规格，并继续工作直到达标。其他类似的模式包括 [GSD](<https://github.com/gsd-build/get-shit-done>)（以及[领域特定](<https://arxiv.org/abs/2603.20179>)的[变体](<https://github.com/psi-oss/get-physics-done>)），以及 Claude Code 原生的 /loop 命令。
Ralph 可以通过 /plugin 安装。在 Claude Code 中一个典型的调用提示词可能看起来像：
    
    /ralph-loop:ralph-loop “Please keep working on the task until the success criterion of 0.1% accuracy across the entire parameter range is achieved.” --max-iterations 20 --completion-promise “DONE”
这里，Claude 将迭代最多 20 次，直到它用一句“DONE”咒语保证任务完成。
### **结果**
Claude 在几天内从零开始[这个项目](<https://github.com/smsharma/clax>)，在它的各种输出上与参考 CLASS 实现达到了亚百分比级的一致。我请 Claude 在项目过程中重建代码一些主要输出——各种 CMB 角功率谱——的精度，并标注开发过程中的里程碑。它生成了下面的图，展示了通往亚百分比精度的路径。
![](assets/long-running-Claude/img_001.img)智能体在代码库上工作时通往亚百分比精度的路径。
  

智能体的开发轨迹有些笨拙。例如，它的测试覆盖存在明显的空白——有一段时间它只在单个（基准）参数点上测试代码，大幅缩小了它的抓虫覆盖面。它也会犯初级错误，例如在规范约定上绊倒，或者花几个小时追逐一个宇宙学家会立刻发现的 bug，但它持续朝着亚百分比精度这个既定目标取得进展。
这个项目的一个副产品是，通过观看 git 提交历史，我学到了关于玻尔兹曼求解器及其所建模物理的惊人数量的知识。这个项目不是来自我的核心科学领域，但跟随 Claude 的渐进式进展并查证我不认识的东西，被证明是一种有效吸收科学知识的方式。[提交日志](<https://github.com/smsharma/clax/commits/main/>)读起来像一个快速、超级字面化的博士后写的实验室笔记。
虽然最终的求解器不是生产级的（例如，它并非在每个区间都达到与参考 CLASS 实现可接受的精度一致），但它证明了智能体驱动的开发可以将数月甚至数年的研究人员工作压缩到几天。
这种压缩改变了什么算作空闲时间。AI 研究中的普遍体验是隔夜启动一个实验（例如一次训练运行），然后早上看到结果的满足感。不运行实验带有机会成本。如今，不运行智能体感觉也有成本。如果你有算力和具有明确定义成功标准的项目，那么每个_没有_智能体为你工作的夜晚，都是被搁置的潜在进展。
### **致谢**
我们感谢 Eric Kauderer-Abrams 的同行评审，以及 Xander Balwit、Ethan Dyer 和 Rebecca Hiscott 提供的有益反馈。
#### 
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/long-running-Claude>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/long-running-Claude>)
## 相关内容
### 了解更多关于 Claude 数学能力的信息
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界：满足该猜想的黎曼 zeta 函数零点的比例，从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而设计的数字签名方案。第二次攻击确定了一种攻击减轮 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)
## 订阅 Anthropic Science
获取 AI 辅助发现、实用工作流程和跨科学领域实地笔记的专题内容。