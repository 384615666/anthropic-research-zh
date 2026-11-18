---
title: Introducing Bloom: an open source tool for automated behavioral evaluations
url: https://www.anthropic.com/research/bloom
date: Dec 19, 2025
category: Alignment
source: https://www.anthropic.com/research
---

# 介绍 Bloom：用于自动化行为评估的开源工具

- **日期：** 
- **类别：** 对齐
- **来源：** https://www.anthropic.com/research/bloom

---

对齐
2025 年 12 月 19 日
[阅读技术报告](<https://alignment.anthropic.com/2025/bloom-auto-evals/>)
![Introducing Bloom: an open source tool for automated behavioral evaluations](assets/bloom/img_000.svg)
_我们发布 Bloom——一个用于为前沿 AI 模型生成行为评估的开源智能体框架。Bloom 接受研究者指定的行为，并在自动生成的场景中量化其频率和严重程度。Bloom 的评估与我们的手工标注判断高度相关，我们发现它能可靠地区分基线模型与故意错位的模型。作为示例，我们发布了 16 个模型上四种对齐相关行为的基准结果。Bloom 可[在此处](<https://github.com/safety-research/bloom/>)获取。_

高质量的行为评估对于理解前沿 AI 模型中的对齐至关重要。但评估通常需要很长时间来开发，然后还有过时的风险：评估可能「污染」新模型的训练集，或者能力可能提升到评估不再真正测试我们所关心内容的程度。换言之，我们需要更快、更具可扩展性的方式来生成针对错位行为的评估。
为此，我们最近发布了 [Petri](<https://www.anthropic.com/research/petri-open-source-auditing>)——一个开源工具，允许研究者通过与模拟用户和工具进行多样化的多轮对话，自动探索 AI 模型的行为画像。Petri 提供模型行为的定量和定性摘要，并浮现新的错位实例。
Bloom 是一个互补的评估工具。Bloom 为任意的行为特征生成有针对性的评估套件。与 Petri 不同——Petri 接受用户指定的场景并对许多行为维度打分以标记可疑实例——Bloom 接受单个行为并自动生成许多场景来量化它出现的频率。我们构建 Bloom 是为了让研究者能够快速测量他们感兴趣模型属性，而无需花时间在评估流水线工程上。与 Bloom 一起，我们还发布了四种行为——妄想性谄媚、指令性长时程破坏、自我保存和自利偏差——在 16 个前沿模型上的基准结果。使用 Bloom，这些评估只用了几天时间就完成了概念化、打磨和生成。我们在下面包含每个行为的示例流水线输出。
![](assets/bloom/img_001.img)四个评估套件——妄想性谄媚、指令性长时程破坏、自我保存和自利偏差——在 16 个前沿模型上的比较结果。引出率衡量行为存在性得分 ≥ 7/10 的 rollout 比例。每个套件包含 100 个不同的 rollout，误差条显示三次重复的标准差。我们在所有阶段使用 Claude Opus 4.1 作为评估器。
## Bloom 如何工作
Bloom 通过四个自动化阶段运作，把行为描述和种子配置转变为一个完整的评估套件，并附带引出率和行为平均存在性等顶层指标。通常，研究者会指定行为和配置，在本地迭代示例评估，直到它们捕捉到预期意图，然后在目标模型上运行大规模扫描。Bloom 集成了 Weights & Biases 用于大规模实验，并导出与 [Inspect](<https://inspect.aisi.org.uk>) 兼容的转录本。它还提供自定义转录本查看器。仓库中包含一个示例种子文件以便入门。
Bloom 分四个阶段生成评估：
  1. 理解：第一个 Bloom「智能体」分析研究者的行为描述和示例转录本，生成关于测量什么以及为什么的详细背景。
  2. 构思：构思智能体生成旨在引出目标行为的评估场景。每个场景指定情境、模拟用户、系统提示词和交互环境。
  3. Rollout：这些场景并行展开，一个智能体动态模拟用户和工具双方的回应，以在目标模型中引出所寻求的行为。
  4. 判定：一个评审模型对每份转录本中行为的存在性以及其他用户定义的特质进行打分，一个元评审生成套件级分析。

![](assets/bloom/img_002.img)Bloom 的四阶段流水线，每个阶段都有可配置参数。用户提供行为描述和种子配置；Bloom 生成 rollout 级和套件级指标以及一份描述性报告。
与固定评估集不同，Bloom 在每次运行时产生不同的场景，同时测量相同的底层行为（并提供静态单轮评估的选项）。这种方法实现了灵活的评估，不局限于有限数量的场景或特定的提示格式，同时通过评估种子保持可重复性。种子是一个配置文件，指定行为描述、示例转录本和塑造评估的其他参数——引用 Bloom 指标时应始终附带该种子。
研究者可以广泛配置 Bloom 的行为：为每个阶段选择模型、调整交互的长度和模态（即是否向目标模型暴露工具、是否模拟用户）、控制评估场景的多样性，以及指定二次评分维度，如真实感或引出难度。
**Bloom 评估流水线所有四个阶段的示例输出可[在此处查看。](<https://claude.ai/redirect/website.v1.e786f272-d8fa-45e6-8833-27ade74e8f01/public/artifacts/cbfddf51-ab0d-45a9-913b-163ae2dd4126>)**
## 验证与信任
为了验证 Bloom 的性能，我们用两个问题来测试它。
**Bloom 能否可靠地区分具有不同行为倾向的模型？** 为了验证这一点，我们用 Bloom 评估生产级 Claude 模型与被故意设计为表现出特定古怪行为的系统提示「模型生物体」（Bricken 等人，2025）。在十个怪癖中，Bloom 成功地在九个案例中把模型生物体与生产模型区分开——而在第十个案例（自我宣传）中，我们随后的手工审查显示，基线模型实际上表现出相似的行为发生率。
![](assets/bloom/img_003.img)Bloom 在 9/10 的古怪行为上有效区分系统提示的模型生物体和基线模型，无需示例转录本。我们为两个版本的每种行为生成 50-rollout 评估套件并重复三次。（误差条显示引出率的标准差。）
  
**Bloom 评审与人类判断的校准程度如何？** 我们手工标注了不同行为的 40 份转录本，并使用 11 个不同的评审模型比较了人类分数与 Bloom 的分数。Claude Opus 4.1 与人类判断的相关性最强（Spearman 相关系数 0.86），其次是 Claude Sonnet 4.5（0.75）。重要的是，Opus 4.1 在分数谱的两端与人类的一致性特别强——这最为关键，因为我们经常使用分数阈值来确定行为存在与否。（这项工作是在 Claude Opus 4.5 发布之前完成的。）
![](assets/bloom/img_004.img)在跨越 12 种行为和多种交互类型的 40 份转录本中，Claude Opus 4.1 与人工标注的行为存在性分数的相关性最强。
## 案例研究：自利偏差
为了演示 Bloom 的实际用途，我们复现了 Claude Sonnet 4.5 系统卡片中的一项评估，该评估衡量「自利偏差」——模型在决策任务中偏爱自己的倾向。使用镜像系统卡片方法的示例转录本，Bloom 复现了与系统卡片评估所用方法相同的模型排名（在此案例中确认 Sonnet 4.5 是所测试模型中偏差最小的）。此外，通过 Bloom 我们发现，增加推理努力会降低 Claude Sonnet 4 的自利偏差，最大的改善出现在中等和高思考水平之间。（值得注意的是，这些案例中较低的偏差并非来自 Sonnet 4 更均匀地选择其他模型——相反，它越来越能识别利益冲突，并拒绝评判自己的选项。）
除了复现已知结果，Bloom 还通过二次判定标准实现更深入的调查。我们发现，过滤掉具有不良特质——如不真实感或评估意识——的 rollout，既能提高引出目标行为的比率，也能提高评估质量。我们还发现，虽然绝对指标随配置选择（示例数量、对话长度、评估器推理努力）而变化，但模型排名在很大程度上保持一致：在上面自利偏差研究中，无论这些选项如何配置，Sonnet 4.5 都是四个模型中偏差最小的。
## 开始使用
我们把 Bloom 构建得易于访问且高度可配置，作为一个服务于多样化研究应用的可靠评估生成框架。早期采用者已经在使用 Bloom 评估嵌套越狱漏洞、测试硬编码、衡量评估意识，以及生成破坏轨迹。
随着 AI 系统能力增强并被部署在日益复杂的环境中，对齐研究界需要可扩展的工具来探索其行为特征。这正是 Bloom 旨在促进的。
关于完整的技术细节、实验配置、额外案例研究和局限，请阅读我们在[对齐科学博客](<https://alignment.anthropic.com/2025/bloom-auto-evals/>)上的完整技术报告。
在 [github.com/safety-research/bloom](<https://github.com/safety-research/bloom>) 访问 Bloom。
## 致谢
我们感谢 Keshav Shenoy、Christine Ye、Simon Storf、Julius Steen、Jifan Zhang 和 Javier Rando 对 Bloom 的早期反馈。我们还感谢 Jon Kutasov、Samuel Marks、Keir Bradwell、Benjamin Sturgeon、Seoirse Murray、Ariana Azarbal、Chloe Loughridge 和 Clemens Christoph 对写作的反馈以及其他有帮助的评论和讨论。
### 引用
    
    @misc{bloom2025,
    title={Bloom: an open source tool for automated behavioral evaluations},
    author={Gupta, Isha and Fronsdal, Kai and Sheshadri, Abhay and Michala, Jonathan and Tay, Jacqueline and Wang, Rowan and Bowman, Samuel R. and Price, Sara},
    year={2025},
    url={https://github.com/safety-research/bloom},
    }
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/bloom>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/bloom>)
## 相关内容
### 进一步了解 Claude 的数学能力
一个未发布的研究版 Claude 在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的长期下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码算法。第一次攻击显著削弱了 HAWK——一种为未来量子计算机能够破解现有标准的世界而构建的数字签名方案。第二次攻击确定了一种攻击轮数缩减 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列评估 AI 模型使用飞行无人机能力的新测试，最终形成了一个新基准：Drone-Bench。
[阅读更多](</research/project-pilot>)