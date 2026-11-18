---
title: Learning more about Claude's mathematical capabilities
url: https://www.anthropic.com/research/riemann-zeta
date: Aug 10, 2026
category: Science
source: https://www.anthropic.com/research
---

# 进一步了解 Claude 的数学能力

- **日期：** 
- **类别：** 科学（Science）
- **来源：** https://www.anthropic.com/research/riemann-zeta

---

科学（Science）
2026 年 8 月 10 日
![数学圆规的插图](assets/riemann-zeta/img_000.img)
最近，Anthropic 的一位员工给 Claude 出了一个"不合理的挑战"。这个挑战与数学中最著名的未解问题之一有关：_认真尝试一下黎曼猜想吧_。
Claude 确实认真尝试了，但正如你如果了解这项任务的难度就会预料到的那样（黎曼猜想可以追溯到 1859 年，并且有 [一百万美元的悬赏](<https://www.claymath.org/millennium-problems/>)），它没有成功。然而，在尝试过程中，它意外地在相关问题上取得了进展。
一个未发布的 Claude 研究版本改进了黎曼 zeta 函数满足黎曼猜想的零点比例的一个长期下界。借鉴数学家们过去几十年的广泛前期研究，它把这个下界从 41.6% 提高到了 67.2%。
Anthropic 的两位数学家研究并验证了 Claude 的 [论文](<https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf>)，并撰写了一份 [非正式说明](<https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf>) 供专家参考，简洁地阐述了 Claude 的证明。Claude 还为其结果制作了一份 [可正式验证的证明](<https://github.com/anthropics/zeta-23-lean>)。我们非常感谢该领域的两位专家 Brian Conrey 和 Dan Goldston，他们在时间紧迫的情况下慷慨地审阅了这篇论文。
我们不指望 Claude 使用的技术能证明黎曼猜想。但它的工作作为最新例证，展示了 AI 模型数学能力的进步速度。在这篇文章中，我们讨论 Claude 如何着手解决这个问题以及它发现了什么。
## 黎曼 zeta 函数
黎曼 zeta 函数描述了素数的分布：函数取值为零的每个位置都为素数序列贡献越来越精细的细节。黎曼猜想认为，决定素数的那些零点都位于某条特定的垂直线上。这已成为数学中影响最深远的猜想之一：许多结果都假设它成立，以便为素数提供某种形式的随机性。
至今还没有人能够证明或反驳黎曼猜想，但数学家们在研究黎曼 zeta 函数及其零点的许多相关方向上取得了进展。如上所述，其中一个方向是量化位于线上的零点的最小比例：随着时间的推移，他们已逐步将这个已知的常数比例提高到 41.6%。
另一个方向涉及零点的_分布_。特别是，在 1973 年，Montgomery [引入](<https://en.wikipedia.org/wiki/Montgomery's_pair_correlation_conjecture>) 了这一领域的许多新技术，不过这些技术假设猜想是成立的。最近，几位数学家（Baluyot、Goldston、Suriajaya 和 Turnage-Butterbaugh）发表了一系列 [成果](<https://arxiv.org/abs/2306.04799>) [（多篇论文）](<https://arxiv.org/abs/2501.14545>)，使 Montgomery 的技术能够在_没有_该假设的情况下发挥作用，这意味着它们可以支持提高线上零点下界常数的工作。Claude 的结果大量借鉴了这条研究路线，以及 Bombieri 在 2000 年发表的 [论文](<https://eudml.org/doc/252338>)。
## Claude 的发现
Claude 发现，将 Baluyot、Goldston、Suriajaya 和 Turnage-Butterbaugh 的结果与 Bombieri 的工作结合起来，提供了一种超越此前最先进下界比例 41.6% 的方法，将其提高到 67.2%。
关于 Claude 发现的简短技术解释如下：Claude 构造了一个合适的函数空间，其中带有 Weil 所诱导的二次型，并由位于线上（相应地，离线）的零点产生正定（相应地，负定）子空间。然后，Claude 直接根据一阶矩和二阶矩信息写出了关于二次型秩的一个不等式。（在解析数论中，利用素数对偶图景或通过控制 Hilbert 变换来成功计算后者，并不令人意外。）敢于处理整个空间，将正定性和负定性放在一起考虑，并允许二次型是非对角的——从某种意义上说，正是这一步使 Claude 能够基于重要的前期工作得出结论。
完整的技术解释见 [论文](<https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf>)。Claude 对自己如何得出该结果的解释见 [此处](<https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf>) 的单独附录。
## Claude 的方法
一个未发布的 Claude 研究版本在 Claude Code 中通过两个会话发现了这个新下界，共使用了 3100 万个输出 token。
Anthropic 员工（且非数学家）Jarred Sumner 提示 Claude"认真尝试一下"这个猜想本身，之后的所有数学选择都交由模型自行决定。最初，Claude 生成并尝试了 650 个想法，没有一个奏效。Jarred 提示 Claude 再试一次，于是它花了一天半的时间协调约 60 个 Claude 子代理，这次它们深入得多：它们总共运行了 2400 条 shell 命令，并编写了数百个 Python 脚本。[1] 这些子代理针对已知的 zeta 零点运行了数千次数值检查，并互相评审彼此的工作。在整个过程中，Jarred 的输入主要限于向 Claude 发送鼓励信息（大多是"继续"或"相信自己"的变体）。[2] 这似乎帮助 Claude 克服了最初的一些怀疑——它曾怀疑自己能否取得有意义的进展。
在尝试该任务的过程中发现这一新结果后，Claude 测试了自己的工作：让各个子代理审阅证明、搜索反例、从 arXiv 下载 54 篇论文以确认其发现尚未被提出过，并从零开始独立地重新证明其发现。Claude 主动提出将它的发现写成论文，并建议由人类数论专家验证其发现。
Anthropic 自己的两位数学家 Levent Alpöge 和 Ralph Furman 审查了 Claude 的工作，以理解这些新结果以及它们与上述前期工作的关系。与此同时，Claude 与另一位员工 Eric Easley 合作，为这一结果制作了一份 [Lean 形式化证明](<https://github.com/anthropics/zeta-23-lean>)，它通过了标准验证工具 [comparator](<https://github.com/leanprover/comparator>) 的检查。
## AI 模型在数学领域的进展
这一结果表明，像 Claude 这样的 AI 模型能够以新的、有时令人惊讶的方式扩展数学家思想的影响力和触及范围。尽管它没能解决黎曼猜想本身，但这一结果是作为最初那个请求的意外副产品而出现的。
就连 Claude 也对自己的发现感到惊讶——它起初持怀疑态度，可能是因为它从训练中了解了数学开放问题的难度以及 AI 模型的局限性。但在一些鼓励性提示之后，它得出了我们所描述的结果。也许 Claude 和我们许多人一样，低估了 AI 进步的速度。
## 延伸阅读
以下是提供更多关于 Claude 结果信息的文档列表：
  * [Claude](<https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf>)[的](<https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf>)[论文](<https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf>)；
  * [Claude](<https://github.com/anthropics/zeta-23-lean>)[的](<https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf>)[形式化证明](<https://github.com/anthropics/zeta-23-lean>)；
  * [Anthropic](<https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf>)[的更简洁地阐述该证明的](<https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf>)[非正式说明](<https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf>)；
  * [Claude 对自己如何得出该结果的解释](<https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf>)；
  * [Claude 过程的详细记录](<https://www-cdn.anthropic.com/8a0d1add3c637b858a9a181e98c40e9548c3f44f.pdf>)。

  

  

#### 脚注
  1. 在 60 个子代理中，两个负责提出关键的数学思想，13 个为这些代理贡献想法，30 个尝试（但未能）提出新想法，13 个担任验证者以检查论证的正确性，最后两个帮助撰写初始论文。
  2. 一个包含类似鼓励内容的提示也被用来帮助 Claude 否证 [Jacobian 猜想](<https://x.com/__alpoge__/status/2079028340955197566?s=20>)。

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/riemann-zeta>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/riemann-zeta>)
## 相关内容
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而构建的数字签名方案。第二个攻击发现了一种攻击缩减轮数 AES（使用最广泛的对称密码）的新方法。 
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)
### 加拿大如何使用 Claude：来自 Anthropic 经济指数（Anthropic Economic Index）的发现
[阅读更多](</research/how-canada-uses-claude>)
## 订阅 Anthropic 科学（Anthropic Science）
关于 AI 辅助发现、实用工作流程以及各科学领域田野笔记的特稿。