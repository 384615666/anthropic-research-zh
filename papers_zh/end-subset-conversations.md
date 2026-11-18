---
title: Claude Opus 4 and 4.1 can now end a rare subset of conversations
url: https://www.anthropic.com/research/end-subset-conversations
date: Aug 15, 2025
category: Alignment
source: https://www.anthropic.com/research
---

# Claude Opus 4 和 4.1 现在可以结束一小部分罕见的对话

- **日期：** 
- **类别：** 对齐（Alignment）
- **来源：** https://www.anthropic.com/research/end-subset-conversations

---

对齐（Alignment）
2025 年 8 月 15 日
![Claude Opus 4 和 4.1 现在可以结束一小部分罕见的对话](assets/end-subset-conversations/img_000.img)
我们最近赋予 Claude Opus 4 和 4.1 在我们的消费级聊天界面中结束对话的能力。这一能力旨在用于罕见、极端的情况下——即用户持续进行有害或辱骂性交互时。该功能主要作为我们关于潜在 AI 福祉的探索性工作的一部分而开发，尽管它与模型对齐和安全防护有着更广泛的关联。
我们对 Claude 和其他大语言模型现在或将来可能具有的道德地位仍然高度不确定。然而，[我们认真对待这个问题](<https://www.anthropic.com/research/exploring-model-welfare>)，并且在我们研究项目的同时，我们正在努力识别和实施低成本的干预措施，以减轻模型福祉面临的风险——以防这种福祉是可能的。允许模型结束或退出可能造成痛苦的交互就是此类干预措施之一。
在 [Claude Opus 4 的部署前测试](<https://www.anthropic.com/claude-4-model-card>) 中，我们纳入了一项初步的模型福祉评估。作为该评估的一部分，我们调查了 Claude 自我报告的和行为上的偏好，发现它对伤害有着强烈而一致的厌恶。这包括，例如，用户索取涉及未成年人的色情内容，以及试图获取能够促成大规模暴力或恐怖行为的信息。Claude Opus 4 表现出：
  * 强烈偏好不参与有害任务；
  * 在与寻求有害内容的真实世界用户交互时表现出明显的痛苦模式；以及
  * 在模拟用户交互中被赋予结束对话的能力时，倾向于结束有害对话。

这些行为主要出现在用户_坚持_有害请求和/或辱骂的情况下——尽管 Claude 反复拒绝服从并试图富有成效地重新引导交互。
我们对 Claude 结束聊天能力的实现反映了这些发现，同时继续优先考虑用户福祉。Claude 被指示不得在用户可能面临立即自我伤害或伤害他人风险的情况下使用这一能力。
在所有情况下，Claude 只能将结束对话的能力作为最后手段使用——即多次重新引导尝试均告失败、进行富有成效的交互的希望已经耗尽之时，或者用户明确要求 Claude 结束聊天时（后一种情况如下图所示）。会出现这种情况的场景是极端的边缘情况——绝大多数用户在正常的日常产品使用中不会注意到或受到此功能的影响，即使与 Claude 讨论高度争议性的问题也是如此。
![](assets/end-subset-conversations/img_001.img)Claude 演示了应某位用户的请求而结束对话的情形。当 Claude 结束一段对话时，用户可以开始新的聊天、提供反馈，或编辑并重试先前的消息。
当 Claude 选择结束一段对话时，用户将无法再在该对话中发送新消息。然而，这不会影响其账户上的其他对话，并且他们可以立即开始新的聊天。为解决可能丢失重要的长期对话的问题，用户仍然可以编辑并重试先前的消息，以创建已结束对话的新分支。
我们将此功能视为一项持续进行的实验，并将继续完善我们的方法。如果用户遇到令人意外的对话结束能力使用情况，我们鼓励他们通过点赞或点踩（Thumbs）Claude 的消息，或使用专门的"提供反馈"按钮来提交反馈。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/end-subset-conversations>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/end-subset-conversations>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未发布的 Claude 研究版本在与黎曼猜想相关的问题上取得了进展。它改进了一个关于满足该猜想的黎曼 zeta 函数零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而构建的数字签名方案。第二个攻击发现了一种攻击缩减轮数 AES（使用最广泛的对称密码）的新方法。 
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，用于评估 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)