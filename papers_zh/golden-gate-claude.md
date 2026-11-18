---
title: Golden Gate Claude
url: https://www.anthropic.com/research/golden-gate-claude
date: May 23, 2024
category: Interpretability
source: https://www.anthropic.com/research
---

# 金门大桥 Claude

- **日期：** 
- **类别：** 可解释性（Interpretability）
- **来源：** https://www.anthropic.com/research/golden-gate-claude

---

可解释性（Interpretability）
2024 年 5 月 23 日
![金门大桥 Claude](assets/golden-gate-claude/img_000.webp)
发布于
    2024 年 5 月 23 日
团队
    [可解释性](</research/team/interpretability>)
主题
    
  * [可解释性](</search?topic=interpretability>)
  * [Claude Sonnet](</search?topic=claude-sonnet>)
  * [Claude 应用](</search?topic=claude-apps>)
  * [对齐](</search?topic=alignment>)

[](</research/emotion-concepts-function>)[](</research/mapping-mind-language-model>)[](</research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning>)[](</research/a-mathematical-framework-for-transformer-circuits>)
相关文章
  * 可解释性
2026 年 4 月 2 日
[大语言模型中的情绪概念及其功能](</research/emotion-concepts-function>)

[阅读更多](</search?topic=interpretability>)
 _更新：Golden Gate Claude 曾作为研究演示上线 24 小时，现已下线。若想进一步了解我们在可解释性以及 Claude 内部特征激活方面的研究，请见[这篇文章](<https://www.anthropic.com/news/mapping-mind-language-model>)或我们的[完整研究论文](<https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html>)。_  

周二，我们[发布了一篇重要的新研究论文](<https://www.anthropic.com/research/mapping-mind-language-model>)，探讨如何解读大语言模型；在文中，我们开始描绘我们的 AI 模型 Claude 3 Sonnet 的内部运作。在 Claude 的「心智」里，我们发现了数以百万计的概念，当模型读到相关文字或看到相关图像时，它们便会激活，我们称之为「特征」。
其中之一便是金门大桥的概念。我们发现，Claude 神经网络里有一组特定的神经元组合，每当它遇到这座旧金山最著名地标的字样（或图片）时就会激活。
我们不仅能识别这些特征，还能调高或调低其激活强度，并观察 Claude 行为上相应的变化。
而正如我们[在研究论文中所解释的](<https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#:~:text=For%20instance%2C%20we%20see%20that%20clamping%20the%20Golden%20Gate%20Bridge%20feature%2034M/31164353%20to%2010%C3%97%20its%20maximum%20activation%20value%20induces%20thematically%2Drelated%20model%20behavior>)，当我们调高「金门大桥」特征的强度，Claude 的回答便开始围绕金门大桥打转。它对大多数提问的回复都会提到金门大桥，哪怕并不直接相干。
若你问这个「Golden Gate Claude」怎么花掉 10 美元，它会建议拿这 10 美元驾车驶过金门大桥、支付过桥费。若让它写个爱情故事，它会讲一辆汽车在大雾天迫不及待驶向心爱之桥的故事。若问它想象自己长什么样，它多半会告诉你，它想象自己长得像金门大桥。
我们将在短时间内开放这个模型供所有人互动体验。你可以在[claude.ai](<https://claude.ai>)上与「Golden Gate Claude」对话（点一下右侧的金门标志即可）。请记住，这只是一个研究演示，这个特定模型可能会表现出一些出人意料、甚至令人不适的行为。
我们的目标是让人们看到可解释性工作能产生怎样的影响。我们能够在 Claude 内部找到并改动这些特征，这让我们更有信心：我们正开始理解大语言模型究竟如何运作。这并不是口头让模型做点角色扮演，也不是新增一段「系统提示词」、在每条输入后面附上额外文字、叫 Claude 假装自己是一座桥。它也不是传统的「微调」——用额外训练数据造出一个新的黑箱，去微调旧黑箱的行为。这是对模型内部激活中某些最基本层面所作的一次精准、外科手术式的改动。
[正如我们在论文中所描述的](<https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html>)，我们可以用同样的技术改变_与安全相关_特征的强度——例如与危险计算机代码、犯罪活动或欺骗相关的那些。随着研究深入，我们相信这项工作能有助于让 AI 模型更安全。
