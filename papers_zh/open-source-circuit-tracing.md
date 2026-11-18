---
title: Open-sourcing circuit tracing tools
url: https://www.anthropic.com/research/open-source-circuit-tracing
date: May 29, 2025
category: Interpretability
source: https://www.anthropic.com/research
---

# 开源电路追踪工具

- **日期：** 
- **分类：** 可解释性
- **来源：** https://www.anthropic.com/research/open-source-circuit-tracing

---

可解释性
2025 年 5 月 29 日
![A hand-drawn image of three hands adjusting a neural network](assets/open-source-circuit-tracing/img_000.img)
在我们最近的可解释性研究中，我们引入了一种新方法来[追踪大语言模型的思维](<https://www.anthropic.com/research/tracing-thoughts-language-model>)。今天，我们将这种方法开源，以便任何人都可以在我们的研究基础上继续推进。
我们的方法是生成_归因图_（attribution graphs），它（部分地）揭示模型内部为决定某个特定输出所采取的步骤。我们发布的开源[库](<https://github.com/safety-research/circuit-tracer>)支持在流行的开放权重模型上生成归因图——而由 Neuronpedia 托管的一个前端让你可以交互式地探索这些图。
这个项目由我们 [Anthropic Fellows](<https://alignment.anthropic.com/2024/anthropic-fellows-program/>) 项目的参与者领导，与 [Decode Research](<https://www.decoderesearch.org/>) 合作完成。
![](assets/open-source-circuit-tracing/img_001.img)Neuronpedia 上交互式图谱探索器 UI 的概览。
要开始使用，你可以访问 [Neuronpedia 界面](<https://www.neuronpedia.org/gemma-2-2b/graph>)，为你选择的提示生成和查看你自己的归因图。对于更复杂的使用和研究，你可以查看[代码仓库](<https://github.com/safety-research/circuit-tracer>)。这次发布使研究者能够：
  1. **追踪电路**：在受支持的模型上，通过生成他们自己的归因图；
  2. **可视化、标注和分享**：在交互式前端中查看图谱；
  3. **检验假设**：通过修改特征值并观察模型输出如何变化。

我们已经使用这些工具研究了 Gemma-2-2b 和 Llama-3.2-1b 中多步推理和多语言表征等有趣行为——示例和分析见我们的演示[笔记本](<https://github.com/safety-research/circuit-tracer/blob/main/demos/circuit_tracing_tutorial.ipynb>)。我们还邀请社区帮助我们找到更多有趣的电路——作为启发，我们在演示笔记本和 Neuronpedia 上提供了我们尚未分析的额外归因图。
我们的 CEO Dario Amodei [最近撰文](<https://www.darioamodei.com/post/the-urgency-of-interpretability>)谈及可解释性研究的紧迫性：目前，我们对 AI 内部运作的理解远远落后于我们在 AI 能力方面取得的进展。通过开源这些工具，我们希望让更广泛的社区更容易研究语言模型内部发生的事情。我们期待看到这些工具在理解模型行为方面的应用——以及改进工具本身的扩展。
_开源电路查找库由 [Anthropic Fellows](<https://alignment.anthropic.com/2024/anthropic-fellows-program/>) Michael Hanna 和 Mateusz Piotrowski 开发，Emmanuel Ameisen 和 Jack Lindsey 提供指导。Neuronpedia 集成由 [Decode Research](<https://www.decoderesearch.org/>) 实现（Neuronpedia 负责人：Johnny Lin；科学负责人/总监：Curt Tigges）。我们的 Gemma 图谱基于 [GemmaScope](<https://ai.google.dev/gemma/docs/gemma_scope>) 项目训练的解码器（transcoder）。如有问题或反馈，请在 GitHub 上提交 issue。_
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/open-source-circuit-tracing>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/open-source-circuit-tracing>)
## 相关内容
### 了解更多关于 Claude 的数学能力
一个未发布的研究版 Claude 在与黎曼猜想相关的问题上取得了进展。它改进了一个长期存在的下界——满足该猜想的黎曼 zeta 函数零点比例，从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一个攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的时代而构建的数字签名方案。第二个攻击发现了一种攻击缩减轮数 AES（使用最广泛的分组密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### 项目 Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，考察 AI 模型使用飞行无人机的能力，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)