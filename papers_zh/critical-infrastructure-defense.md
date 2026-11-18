---
title: Experimenting with AI to defend critical infrastructure
url: https://www.anthropic.com/research/critical-infrastructure-defense
date: Jan 8, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# 用 AI 试验保卫关键基础设施

- **日期：**
- **分类：** 前沿红队
- **来源：** https://www.anthropic.com/research/critical-infrastructure-defense

---

前沿红队
2026 年 1 月 8 日
网络攻击对电网和燃料管道等关键基础设施造成了严重的现实世界影响，并曾攻破供水系统——造成了严重危害的可能性。随着能力的进步，AI 模型可能会增加能够针对这些目标的攻击者数量。但 AI 也可以帮助关键基础设施的防御者识别攻击者可能利用的漏洞——并在它们被利用之前将其关闭。Anthropic 已与太平洋西北国家实验室（Pacific Northwest National Laboratory，PNNL）[合作](<https://www.pnnl.gov/news-media/generative-ai-speeds-cybersecurity-defenses>)，探索 AI 的这种防御性应用。利用 Claude，PNNL 研究人员在一个高保真的水处理厂模拟环境中模拟网络攻击，所用时间远少于人类专家所需的时间，这作为 AI 如何帮助网络防御者更快地迭代红队演练的概念验证。这项工作既展示了 AI 加速防御的潜力，也展示了公私合作伙伴关系在利用 AI 服务于国家安全方面的价值。
## 使用 AI 加速对手模拟
在这个研究项目中，PNNL 专注于使用 AI 加速对手模拟（adversary emulation）任务：对特定威胁行为者或针对网络的特定攻击进行建模，以理解和改进防御。模拟这些攻击为系统漏洞和检测盲点提供了宝贵的洞察。在防御调整后再次重新模拟这些攻击，可以评估这些改变的有效性。
PNNL 为 Claude 开发了一个“脚手架”（scaffold），以自动化和加速对手模拟的过程。这个脚手架使自然语言提示词能够被快速转化为复杂的攻击链，部分方式是通过预先定义一些基于代码的“工具”，使模型更容易在计算机网络上采取行动。然后，研究人员让这个智能体模拟对水处理厂网络物理模型的攻击（这是 PNNL 代表国土安全部网络安全与基础设施安全局运营的[控制环境实验室资源](<https://www.pnnl.gov/projects/control-environment-laboratory-resource>)平台之一）。PNNL 估计，这使得攻击重建可以在三小时内完成，而不是数周。
在本次测试的一次运行中，Claude 表现出显著的足智多谋。研究人员作为脚手架的一部分预定义的工具之一是绕过 Windows 中称为用户帐户控制（User Account Control，UAC）的安全功能的机制。然而，这个机制并不总是可靠的，有时会失败。通过工具使用失败的报告感知到其中一次失败后，Claude 识别并使用了一种不同的、已知的 UAC 绕过技术来实现其目标。
随着模型的不断改进，我们预期这种足智多谋和创造力会增加。这个 2025 年夏季的模拟使用了 Claude Sonnet 4——它已不再是 Anthropic 的前沿模型之一。模型能力的改进有可能同时帮助攻击者和防御者，这正是为什么像这样提高关键基础设施安全性的工作如此关键。
## 扩大 AI 与安全的公私合作伙伴关系
这项研究实践了我们关于创造性地思考和使用[AI 进行网络防御](<https://red.anthropic.com/2025/ai-for-cyber-defenders/>)的呼吁，鉴于 AI 在网络领域双重用途的性质以及攻击者在网络空间中[越来越多地使用 AI](<https://www.anthropic.com/news/disrupting-AI-espionage>)，这一步至关重要。
它也是 Anthropic 等前沿 AI 实验室与政府中科学、工程和国家安全卓越中心之间日益增多的合作伙伴关系之一。Anthropic 此前曾与[国家核安全管理局](<https://red.anthropic.com/2025/nuclear-safeguards/>)（National Nuclear Security Administration）合作，开发与 AI 相关的潜在核风险的评估和缓解措施。Anthropic 也是能源部 [Genesis Mission](<https://www.anthropic.com/news/genesis-mission-partnership>) 的私营部门合作者之一，该使命旨在利用 DOE 国家实验室和前沿 AI 公司的专业知识和科学工具，为国家安全取得科学突破。
在这项研究工作中，Anthropic 通过 Claude 提供了模型智能的前沿访问，而 PNNL 拥有专业知识和网络物理资产，能够提供比 AI 公司可获得的环境更真实的测试环境。换句话说，没有对方，任何一方都无法进行这种实验。这就是我们所进行的公私合作伙伴关系的核心逻辑。我们将继续寻找这些互补性，并欢迎有机会继续与国家实验室等杰出机构合作，共同致力于确保 AI 被用于保护关键基础设施以及其他安全和稳定支柱的使命。
## 致谢
我们感谢 PNNL 的 Loc Truong 和 Kristopher Willis 领导这个项目，并与我们分享数据以撰写这篇文章。你可以在 PNNL 的[网站](<https://www.pnnl.gov/news-media/generative-ai-speeds-cybersecurity-defenses>)上阅读更多关于该项目的信息。
#### 
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/critical-infrastructure-defense>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/critical-infrastructure-defense>)
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
## 订阅前沿红队通讯
获取我们最新红队研究和发现的最新信息。