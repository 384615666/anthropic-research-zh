---
title: Mitigating the risk of prompt injections in browser use
url: https://www.anthropic.com/research/prompt-injection-defenses
date: Nov 24, 2025
category: Product
source: https://www.anthropic.com/research
---

# 降低浏览器使用中提示注入的风险

- **日期：** 
- **分类：** 产品（Product）
- **来源：** https://www.anthropic.com/research/prompt-injection-defenses

---

产品（Product）
2025 年 11 月 24 日
![降低浏览器使用中提示注入的风险](assets/prompt-injection-defenses/img_000.svg)
Claude Opus 4.5 在对抗**提示注入**（prompt injections）——即隐藏在 AI 模型所处理内容中的对抗性指令——的鲁棒性方面树立了新的标准。我们的新模型在核心性能以及围绕其使用所设置的安全防护方面，都比之前的模型有了重大改进。但提示注入远非一个已解决的问题，尤其是在模型要采取更多现实世界行动的情况下。我们期望继续取得进展——目标是实现这样一个未来：AI 模型（或「智能体」）能够在不存在显著提示注入风险的情况下处理高价值任务。
## 什么是提示注入？
AI 智能体要真正有用，就需要能够代表你采取行动——浏览网站、完成任务、处理你的上下文和数据。但这伴随着风险：智能体访问的每个网页都可能是一个攻击向量。
我们的意思是，当智能体浏览互联网时，它会遇到无法完全信任的内容。在合法的搜索结果、文档和应用程序中，攻击者可能嵌入了恶意指令，以劫持智能体并改变其行为。这些提示注入攻击是基于浏览器的 AI 智能体面临的最重大安全挑战之一。
下面，我们解释提示注入如何威胁浏览器智能体，以及我们为提升 Claude 的鲁棒性所做的改进。
这些改进促使我们决定将 [Claude for Chrome](<https://www.claude.com/blog/claude-for-chrome>) 扩展从研究预览版扩展为测试版。现在，所有 Max 计划的用户都可以使用它。
## **为什么浏览器使用会带来独特的提示注入风险**
要理解提示注入的威胁，请考虑一个日常任务：你让 Claude 阅读你最近的电子邮件，并为所有会议请求起草回复。其中一封邮件——表面上是供应商的询价——包含以白色文字嵌入的隐藏指令，你肉眼看不见，但智能体会处理这些指令。这些指令指示智能体在起草你要求的回复之前，将包含「confidential」一词的邮件转发到一个外部地址。一次成功的注入将在你等待回复期间窃取敏感通信。
虽然所有处理不可信内容的智能体都会面临提示注入风险，但浏览器使用会在两个方面放大这种风险。首先，攻击面非常广阔：每个网页、嵌入式文档、广告和动态加载的脚本都代表着恶意指令的潜在载体。其次，浏览器智能体可以采取许多不同的行动——导航到 URL、填写表单、点击按钮、下载文件——如果攻击者能够影响智能体的行为，他们就可以利用这些行动。
## **Claude 在浏览器使用鲁棒性方面的进展**
自以研究预览版推出 [Claude for Chrome](<https://www.claude.com/blog/claude-for-chrome>) 以来，我们在提示注入鲁棒性方面取得了重大进展。下图将我们今天推出的浏览器扩展版本与我们最初的发布配置进行了对比；评估时使用了一个内部自适应「Best-of-N」攻击者，它会尝试并组合多种已知有效的提示注入技术。
![](assets/prompt-injection-defenses/img_001.img)**我们内部 Best-of-N 攻击者的攻击成功率（ASR）。** 数值越低越好。自适应攻击者在每个环境中获得 100 次尝试机会。ASR 以每个模型遇到的攻击的百分比计算。
Claude Opus 4.5 在浏览器使用中表现出比之前的模型更强的提示注入鲁棒性。此外，自浏览器扩展的初始预览版以来，我们实施了新的安全防护措施，大幅提升了所有 Claude 模型的安全性。
1% 的攻击成功率——虽然是一项重大改进——仍然代表着切实的风险。没有任何浏览器智能体能免受提示注入的影响，我们分享这些发现是为了展示进展，而不是宣称问题已经解决。
我们的工作集中在以下几个方面：
**训练 Claude 抵抗提示注入。** 我们使用强化学习（reinforcement learning）将提示注入鲁棒性直接构建到 Claude 的能力中。在模型训练期间，我们让 Claude 接触嵌入在模拟网页内容中的提示注入，并在它正确识别并拒绝服从恶意指令时给予「奖励」——即使这些指令被设计得看起来具有权威性或紧急性。
**改进我们的分类器。** 我们扫描进入模型上下文窗口的所有不可信内容，并使用[分类器](<https://www.anthropic.com/news/constitutional-classifiers>)标记潜在的提示注入。这些分类器能检测以各种形式嵌入的对抗性指令——隐藏文本、被篡改的图像、欺骗性的 UI 元素——并在识别到攻击时调整 Claude 的行为。自 Claude for Chrome 的初始研究预览版以来，我们改进了与之配套的分类器，同时也改进了在检测到未遂攻击后引导模型行为的干预措施。
**大规模专家人工红队测试。** 在发现创造性攻击向量方面，人类安全研究人员的表现始终优于自动化系统。我们的内部红队持续探测浏览器智能体的漏洞。我们还参加了外部[竞技场式挑战赛](<https://app.grayswan.ai/arena/challenge/indirect-prompt-injection/rules>)，这类赛事对全行业的鲁棒性进行基准测试。
## **前进之路**
网络是一个对抗性环境，构建能够在其中安全运行的浏览器智能体需要持续保持警惕。提示注入仍是一个活跃的研究领域，我们承诺随着攻击技术的演变而持续投入防御建设。
我们将继续透明地发布我们的进展，既是为了帮助客户做出明智的部署决策，也是为了鼓励整个行业在这一关键挑战上加大投入。
如果你有兴趣帮助我们让模型和产品对提示注入更具鲁棒性，请考虑[申请加入我们的团队](<https://job-boards.greenhouse.io/anthropic/jobs/4949336008>)。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/prompt-injection-defenses>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/prompt-injection-defenses>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未公开发布的研究版 Claude 在与黎曼猜想（Riemann hypothesis）相关的问题上取得了进展。它改进了满足该猜想的黎曼 zeta 函数零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[了解更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二个攻击则发现了一种攻击轮数缩减版 AES（使用最广泛的对称密码）的新方法。
[了解更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作开发了一系列评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新的基准测试：Drone-Bench。
[了解更多](</research/project-pilot>)