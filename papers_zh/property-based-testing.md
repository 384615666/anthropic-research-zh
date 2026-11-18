---
title: Finding bugs across the Python ecosystem with Claude and property-based testing
url: https://www.anthropic.com/research/property-based-testing
date: Jan 14, 2026
category: Frontier Red Team
source: https://www.anthropic.com/research
---

# 用 Claude 和基于属性的测试在 Python 生态系统中发现 Bug

- **日期：** 
- **类别：** 前沿红队
- **来源：** https://www.anthropic.com/research/property-based-testing

---

前沿红队
2026 年 1 月 14 日
 _Muhammad Maaz ¹,²、Liam DeVoe³、Zac Hatfield-Dodds²、Nicholas Carlini²  
¹MATS、²Anthropic、³东北大学_
** _我们开发了一个能够高效识别大型软件项目中 Bug 的智能体。为此，我们的智能体推断代码应当成立的通用性质，然后通过应用基于属性的测试（property-based testing）——一种与模糊测试类似的技术——我们能够在 NumPy、SciPy 和 Pandas 等顶级 Python 包中发现 Bug。经过大量人工验证，我们正在向开发者报告这些 Bug，其中几个已经被修复。_**
更多信息，请阅读完整[论文](<https://arxiv.org/abs/2510.09907>)、查看 [GitHub 仓库](<https://github.com/mmaaz-git/agentic-pbt>)，或在我们[网站](<https://mmaaz-git.github.io/agentic-pbt-site/>)浏览我们发现的 Bug。
## 引言
确保程序没有 Bug 是软件工程中最具挑战性的方面之一。尽管开发者尽了最大努力，Bug 仍常常潜伏。最常见的代码测试方法是_基于示例的测试_：开发者写出一个特定的示例用例，然后验证实际输出与预期输出匹配。例如，开发者可能会验证对列表 [2, 10, 5, 4] 调用排序函数会返回输出 [2, 4, 5, 10]。然而，用这样的测试穷尽覆盖一个程序是很有挑战性的：Bug 常常残留在开发者没有测试的边界情况中。毕竟，如果开发者没想到要测试一个边界情况，那么开发者很可能在实现中也没有考虑该情况！
相比之下，_基于属性的测试_是一种软件测试范式，旨在测试代码的一个通用性质是否对所有（或大多数）输入都成立。开发者指定关于程序的一个性质或不变量——例如，JSON 反序列化是序列化的逆操作——以及该性质接受的输入类型描述（例如，任何可 JSON 序列化的对象）。然后，基于属性的测试框架使用类似模糊测试的技术生成有效输入作为测试用例，自动搜索该性质的反例。由于开发者指定的是通用输入域，而非单个测试用例，基于属性的测试让开发者不必思考每一个边界情况，并允许他们在更高的抽象层次上工作。
在我们于 2025 年 NeurIPS [_Deep Learning for Code_](<https://dl4c.github.io/>) 研讨会（[MATS](<https://www.matsprogram.org/>) 项目的成果）上展示的论文中，我们开发了一个为现有代码自主编写基于属性测试的 AI 智能体。我们指示智能体通过阅读类型注解、文档字符串、函数名和注释来发现性质。然后，智能体使用 Hypothesis 编写相应的基于属性的测试。
在这项工作中，我们专注于识别一般的 Bug，而不仅仅是安全漏洞。许多导致安全漏洞的逻辑 Bug 类别都适合基于属性的测试。例如，在最近一篇[博客文章](<https://red.anthropic.com/2025/smart-contracts/>)中，我们专注于识别_智能合约_中的 Bug；几乎所有那些漏洞都是逻辑 Bug 的结果。未来，我们设想可能可以应用我们在此描述的技术，在部署前主动识别 Bug。
我们使用我们的智能体，在 NumPy、SciPy 和 Pandas 等流行的开源 Python 仓库中发现了数百个潜在 Bug。为了负责任地披露这些 Bug，并确保我们不必要地加重维护者的负担，我们仔细审查了每个 Bug。
我们使用的审查流程比我们平时为自己代码审查实施的流程更费力，但我们强烈倾向于减少误报的数量。我们的流程如下：首先，我们只选择优先级最高的 Bug 进行审查。我们把潜在 Bug 交给三位专家人工审查（每个 Bug 平均约一小时审查）。然后，我们丢弃三位人工审查者中任何一位对其有效性不确定的 Bug。最后，我们（这篇博客的作者）手动审查了每个候选 Bug。只有当我们也对它的正确性有信心时，我们才手动向仓库维护者提交 issue。我们已经提交了几个这样的 Bug 报告，并正在提交更多。
我们已经公开了所有数据，包括尚未验证的 Bug，以及为了完整起见甚至包括我们判定为无效的 Bug，这样维护者可以在[这个网站](<https://mmaaz-git.github.io/agentic-pbt-site/>)查看它们。在未来几周内，我们打算提交许多剩余的 Bug（在额外验证之后），并将我们的项目扩展到更多 PyPI 项目。
    
    # 基于示例的测试
    def test_sort():
        assert my_sort([1,3,2]) == [1,2,3]
        assert my_sort([1,0,-5]) == [-5,0,1]
    
    # Hypothesis 中的基于属性的测试
    from hypothesis import given, strategies as st
    
    @given(st.lists(st.integers()))
    def test_sort(lst):
        result = my_sort(lst)
        for i in range(len(result)-1):
            assert result[i] <= result[i+1]
**图 1.** 测试代码的两种方式。基于示例的单元测试验证特定的手工指定输入。相比之下，基于属性的测试指定一个通用性质（例如，排序列表的定义），并依赖框架自动构造可能使该性质失败的输入。
## 我们的基于属性的测试智能体
我们的基于属性的测试智能体是作为自定义 Claude Code 命令构建的。智能体接受一个参数，指向一个特定目标，可以是单个 Python 文件（如 normalizers.py）、一个模块（如 numpy、scipy.signal）或一个函数（如 requests.get、json.loads）。然后智能体遵循以下过程来识别潜在 Bug：
  1. 阅读并理解目标：阅读代码、提取相关文档，并探索它与代码库其余部分的关系。
  2. 提出基于这些发现的性质。
  3. 用 Hypothesis 编写相应的基于属性的测试。
  4. 运行测试并反思：如果失败了，测试是真的发现了 Bug，还是测试本身需要调整？如果成功了，测试是否在测试任何有价值的东西，还是只是琐碎的？
  5. 如果智能体确信自己发现了真正的 Bug，它会写出一份格式化的 Bug 报告。

![](assets/property-based-testing/img_000.img)**图 2.** 智能体的工作流程。
为了帮助智能体进行长程多步推理，我们指示它使用待办事项列表来跟踪进度。
设计智能体时的一个优先事项是减少误报数量——根据我们的个人经验，有用的开发者工具会尽量减少呈现给开发者的错误报告数量。自我反思循环有助于减少误报数量，把任何性质建立在目标的明确用法和文档之上也是如此。例如，在一次智能体运行中，智能体写了一个首先通过的性质。然而，经过自我反思，智能体意识到它把整个测试包在了一个 try-catch 块中。移除它之后，测试失败了，智能体发现了一个 Bug。我们还观察到，与 Sonnet 4 相比，Opus 4.1 和 Sonnet 4.5 的自我反思有显著改进。
### 示例运行
为了演示智能体如何通过测试目标来工作，我们展示一段转述的转录本，其中 Claude 在 numpy.random.wald 的实现中发现了一个 Bug。智能体首先调查该函数、其签名、其文档字符串，甚至现有的测试：
请注意，修复并不正确；当我们修复这个 Bug 时，我们把错误来源追溯到一次数值不稳定的计算；见我们合并的修复[此处](<https://github.com/numpy/numpy/pull/29609>)。
## 在真实的 PyPI 包中搜索 Bug
为了在现实世界中测试我们智能体的能力，我们整理了一个包含 100 多个流行 Python 包的多样化集合。这些库跨越各种领域，从数值计算到解析再到数据库。我们对每个包调用智能体，并收集所有生成的 Bug 报告。
### 评估智能体
对于我们评估的第一阶段（论文中已涵盖），我们用 Claude Opus 4.1 对每个包运行智能体，并收集所有生成的 Bug 报告。为了评估这些 Bug 报告，我们确定了两个标准：首先，「这是一个有效的 Bug 吗？」；其次，「它既是一个有效的 Bug，又是我们会合理向库维护者报告的东西吗？」第二个标准比第一个更严格，因为例如一个 Bug 可能是有效的，但太小而不值得提交报告。
在 984 份 Bug 报告中，我们手动选择了 50 份进行审查。我们发现其中 56% 是有效 Bug，32% 是有效且我们也会报告的 Bug。
基于这次人工审查，我们开发了一个评分标准，给 Bug 按 15 分制排名，目的是把最可能有效且值得修复的 Bug 呈现给开发者。我们使用 Opus 4.1 按此评分标准对所有 Bug 报告评分。我们发现这个排名步骤相当有效：在得分最高的 Bug 报告中，86% 是有效的，81% 既有效又可报告。
在我们评估的第二阶段，我们用 Sonnet 4.5 在 10 个重要包的子集上运行智能体，对每个包多次运行。我们还开发了一个评估智能体，使用 Sonnet 4.5 阅读代码和 Bug 报告来检查 Bug 的正确性和严重程度，这比第一阶段的评分标准更精细。最后，我们付费请了 3 位专家人工审查者评估高严重程度的 Bug 的正确性。
要阅读我们的智能体发现的所有 Bug 报告，请见 <https://mmaaz-git.github.io/agentic-pbt-site/>。
### 维护者验证
评估任何在代码中发现 Bug 的工具的有效性都很困难。虽然我们尽最大努力验证 Bug 报告的正确性，但包维护者才是真值的最终仲裁者。为了验证我们的智能体发现的 Bug 是维护者认为有效且值得修复的，我们选择了五个特别有趣的 Bug，手动连同建议的补丁提交到它们各自的 GitHub。在未来几周内，我们打算在验证后继续报告更多 Bug。
### numpy
numpy.random.wald 有时返回负数，这是一个 Bug，因为 Wald 分布的样本应该只返回正数。这就是我们上面示例运行中演示的 Bug。Claude 知道这是 Wald 分布的一个性质，并写了一个直接的 PBT 来检查生成的所有样本是否为正。我们把错误追溯到代码中发生的一次灾难性相消，并在提交拉取请求时开发了一个数值上更稳定的公式。正如 NumPy 维护者在拉取请求中所示，我们的重新表述的相对误差比之前的算法低了近十个数量级。
_补丁已合并：<https://github.com/numpy/numpy/pull/29609>_
### aws-lambda-powertools 
slice_dictionary() 由于没有递增迭代器而重复返回第一个分块。我们的智能体通过识别「切片然后重构字典应该返回原始字典」这一性质抓住了它。
_补丁已合并：<https://github.com/aws-powertools/powertools-lambda-python/pull/7246>_
### cloudformation-cli-java-plugin
item_hash() 对所有列表产生相同的 hash(None) 值，因为使用了原地 .sort() 方法，它返回 None。智能体通过测试「不同输入的哈希应该不同」抓住了它。
_补丁已提交：<https://github.com/aws-cloudformation/cloudformation-cli/pull/1106>_
### tokenizers
EncodingVisualizer.calculate_label_colors() 缺少一个右括号，返回无效的 HSL CSS。我们的智能体通过测试「输出应匹配 HSL 颜色代码的正则表达式」识别了它。
补丁已合并：<https://github.com/huggingface/tokenizers/pull/1853>
### python-dateutil
easter() 在使用儒略历的某些年份返回非星期日的日期。维护者认定该行为因历法系统不同而属预期行为，并承认该语义很微妙。
_Issue 无效：<https://github.com/dateutil/dateutil/issues/1437>_
对 python-dateutil 的报告显示了智能体的一个重要局限：从语义微妙或复杂的代码中推导性质仍然困难。如果代码做出了隐含假设，只有库维护者才能决定要测试的正确性质是什么。
## 结论
随着语言模型的不断改进，我们认为智能体基于属性的测试可能成为人类编写测试的日益有价值的补充。基于属性的测试的高层语义保证使其成为开发过程中自然的搭配。我们发现 LLM 特别擅长从上下文（函数名、文档字符串、其他函数如何调用它等）识别出给定代码块_应该_成立的性质。这使得 LLM 能够有效地编写高质量的基于属性的测试。
展望未来，我们认为把 LLM 应用于测试和 Bug 发现是一个重要的研究方向。尤其是随着 LLM 在利用漏洞方面的能力提高，有必要保持领先于使用 LLM 进行利用的攻击者。
虽然我们在这项工作中没有专注于补丁的自动生成，但这是未来工作的一个明确方向。如果能够（几乎）完全指定一块代码的正确性性质，那么纠正 Bug 就会变得容易得多，我们相信在不久的将来，LLM 将能够有效地提出值得维护者考虑的高质量补丁。
#### 
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/property-based-testing>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/property-based-testing>)
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
## 订阅前沿红队新闻通讯
获取我们最新红队研究和发现的最新动态。