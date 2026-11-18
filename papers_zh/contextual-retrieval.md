---
title: Introducing Contextual Retrieval
url: https://www.anthropic.com/research/contextual-retrieval
date: 2024-09-19
category: Engineering
source: https://www.anthropic.com/research
---

# 推出上下文检索

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/contextual-retrieval

---

工程（Engineering）
2024 年 9 月 19 日
![推出上下文检索](assets/contextual-retrieval/img_000.webp)
已发布
    2024 年 9 月 19 日
团队
    [工程](</engineering>)
主题
    
  * [上下文工程](</search?topic=context-engineering>)
  * [Claude 开发者平台](</search?topic=claude-developer-platform>)
  * [基准测试](</search?topic=benchmarks>)

[](</research/effective-harnesses-for-long-running-agents>)[](</news/skills>)[](</news/prompting-long-context>)[](</news/100k-context-windows>)
相关文章
  * 工程
2025 年 11 月 26 日
[面向长时运行智能体的高效脚手架](</research/effective-harnesses-for-long-running-agents>)

[阅读更多](</search?topic=context-engineering>)
要让 AI 模型在特定场景中有用，它往往需要访问背景知识。例如，客服聊天机器人需要了解它被用于的那项具体业务的知识，法律分析机器人则需要了解大量过往案例。
开发者通常用检索增强生成（Retrieval-Augmented Generation，RAG）来增强 AI 模型的知识。RAG 是一种从知识库中检索相关信息并把它附加到用户提示词上的方法，能显著增强模型的回答。问题在于，传统 RAG 方案在编码信息时会把上下文剥离掉，这常常导致系统无法从知识库中检索到相关信息。
在这篇文章里，我们概述一种能大幅改善 RAG 中检索步骤的方法。该方法名为「上下文检索（Contextual Retrieval）」，使用两种子技术：上下文嵌入（Contextual Embeddings）与上下文 BM25（Contextual BM25）。该方法能把检索失败的数量减少 49%，若再结合重排序（reranking），可减少 67%。这代表着检索准确性的显著提升，而检索准确性会直接转化为下游任务中更好的表现。
你可以借助[我们的 cookbook](<https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide>)，用 Claude 轻松部署属于你自己的上下文检索方案。
### 关于「直接用更长的提示词」的一点说明
有时候最简单的方案就是最好的。如果你的知识库小于 200,000 个 token（约 500 页材料），你完全可以把整个知识库放进给模型的提示词里，无需 RAG 或类似方法。
几周前，我们为 Claude 发布了[提示词缓存](<https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching>)，这让这种做法显著更快、更具成本效益。开发者现在可以在 API 调用之间缓存频繁使用的提示词，把延迟降低 2 倍以上、把成本降低最多 90%（可以阅读我们的[提示词缓存 cookbook](<https://platform.claude.com/cookbook/misc-prompt-caching>)了解其原理）。
不过，随着知识库增长，你会需要一个更具可扩展性的方案。这正是上下文检索的用武之地。
## RAG 入门：扩展到更大的知识库
对于装不进上下文窗口的更大知识库，RAG 是典型方案。RAG 通过以下步骤对知识库做预处理：
  1. 把知识库（文档「语料库」）切分为更小的文本块，通常不超过几百个 token；
  2. 用嵌入模型把这些文本块转换为编码语义的向量嵌入；
  3. 把这些嵌入存入向量数据库，以便按语义相似度检索。

运行时，当用户向模型输入查询，系统会用向量数据库基于与查询的语义相似度找出最相关的文本块。然后，最相关的文本块被加入发给生成模型的提示词中。
嵌入模型擅长捕捉语义关系，但可能漏掉关键的精确匹配。幸运的是，有一种更古老的技术能在这些情形中帮忙。BM25（Best Matching 25）是一种排序函数，使用词法匹配来找精确的词或短语匹配。对于包含唯一标识符或技术术语的查询，它尤其有效。
BM25 建立在 TF-IDF（词频-逆文档频率）概念之上。TF-IDF 衡量一个词对集合中文档的重要程度。BM25 通过考虑文档长度、并对词频施加饱和函数对此加以改进，这有助于防止常见词主导结果。
下面说明 BM25 如何在语义嵌入失效之处成功：假设用户在技术支持数据库里查询「错误代码 TS-999」。嵌入模型可能找到关于错误代码的泛泛内容，却可能漏掉精确的「TS-999」匹配。BM25 则寻找这个特定字符串，从而找出相关文档。
RAG 方案可以通过以下步骤结合嵌入与 BM25 技术，更准确地检索最适用的文本块：
  1. 把知识库（文档「语料库」）切分为更小的文本块，通常不超过几百个 token；
  2. 为这些文本块创建 TF-IDF 编码与语义嵌入；
  3. 用 BM25 基于精确匹配找出头部文本块；
  4. 用嵌入基于语义相似度找出头部文本块；
  5. 用排名融合（rank fusion）技术合并并去重 (3) 与 (4) 的结果；
  6. 把前 K 个文本块加入提示词以生成回答。

通过同时利用 BM25 与嵌入模型，传统 RAG 系统能提供更全面、更准确的结果，在精确词项匹配与更宽的语义理解之间取得平衡。
![使用嵌入与 Best Match 25（BM25）两者来检索信息的标准检索增强生成（RAG）系统。TF-IDF（词频-逆文档频率）衡量词的重要性，并构成 BM25 的基础。](assets/contextual-retrieval/img_001.webp)
一个使用嵌入与 Best Match 25（BM25）两者来检索信息的标准检索增强生成（RAG）系统。TF-IDF（词频-逆文档频率）衡量词的重要性，并构成 BM25 的基础。
这种做法让你能以成本效益高的方式扩展到庞大的知识库，远超单个提示词所能容纳的规模。但这些传统 RAG 系统有一个显著局限：它们常常破坏上下文。
### 传统 RAG 中的上下文难题
在传统 RAG 中，文档通常被切分为更小的文本块以便高效检索。虽然这种做法对许多应用有效，但当单个文本块缺乏足够上下文时，就会带来问题。
举例来说，假设你的知识库里嵌入了一批财务信息（比如美国 SEC 备案文件），而你收到这样一个问题：*「ACME 公司在 2023 年第二季度的营收增长是多少？」*
一个相关的文本块可能包含这样的文字：*「公司营收较上一季度增长了 3%。」* 然而，这个文本块本身既不指明它指的是哪家公司，也不指明相关时间段，这使得既难以检索到正确信息，也难以有效使用该信息。
## 引入上下文检索
上下文检索通过在嵌入每个文本块之前（「上下文嵌入」）、以及在建立 BM25 索引之前（「上下文 BM25」），为每个文本块前置针对该块的解释性上下文，从而解决这个问题。
回到我们 SEC 备案文件集合的例子。下面是一个文本块可能被如何转换的示例：
    
    original_chunk = "The company's revenue grew by 3% over the previous quarter."
    
    contextualized_chunk = "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."
值得注意的是，过去也有人提出过其他利用上下文改进检索的方法。其他方案包括：[为文本块添加通用文档摘要](<https://aclanthology.org/W02-0405.pdf>)（我们做过实验，收益非常有限）、[假设文档嵌入](<https://arxiv.org/abs/2212.10496>)，以及[基于摘要的索引](<https://www.llamaindex.ai/blog/a-new-document-summary-index-for-llm-powered-qa-systems-9a32ece2f9ec>)（我们评估过，表现较低）。这些方法与本篇提出的方法不同。
### 实现上下文检索
当然，手工标注知识库中成千上万乃至数百万个文本块，工作量太大。为实现上下文检索，我们转而求助于 Claude。我们写了一条提示词，指示模型提供简洁的、针对具体文本块的上下文，借助整篇文档的上下文来解释该文本块。我们使用以下 Claude 3 Haiku 提示词为每个文本块生成上下文：
    
    <document> 
    {{WHOLE_DOCUMENT}} 
    </document> 
    Here is the chunk we want to situate within the whole document 
    <chunk> 
    {{CHUNK_CONTENT}} 
    </chunk> 
    Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else. 
生成的上下文文本通常为 50-100 个 token，它在嵌入之前、以及建立 BM25 索引之前被前置到文本块上。
实际应用中，预处理流程如下所示：
![上下文检索是一种预处理技术，能提升检索准确性。](assets/contextual-retrieval/img_002.png)
_上下文检索是一种预处理技术，能提升检索准确性。_

如果你有兴趣使用上下文检索，可以从[我们的 cookbook](<https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide>) 开始。
### 使用提示词缓存降低上下文检索的成本
得益于我们前面提到的特殊提示词缓存功能，上下文检索在 Claude 上能以低成本独特地实现。有了提示词缓存，你无需为每个文本块都传入参考文档。你只需把文档载入缓存一次，然后引用先前缓存的内容。假设文本块为 800 个 token、文档为 8k 个 token、上下文指令为 50 个 token、每个文本块的上下文为 100 个 token，**生成上下文化文本块的一次性成本为每百万文档 token 1.02 美元**。
#### 方法
我们在多种知识领域（代码库、小说、ArXiv 论文、科学论文）、嵌入模型、检索策略与评估指标上做了实验。我们在[附录 II](<https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf>) 中收录了各领域所用问答的一些示例。
下图展示在最佳嵌入配置（Gemini Text 004）、检索前 20 个文本块的设置下，跨所有知识领域的平均表现。我们用 1 减去 recall@20 作为评估指标，它衡量相关文档中未能在前 20 个文本块内被检索到的百分比。完整结果见附录——在我们评估过的每一种「嵌入-来源」组合上，上下文化都带来了提升。
#### 表现提升
我们的实验显示：
  * **上下文嵌入把前 20 个文本块的检索失败率降低了 35%**（5.7% → 3.7%）。
  * **上下文嵌入与上下文 BM25 结合，把前 20 个文本块的检索失败率降低了 49%**（5.7% → 2.9%）。

![上下文嵌入与上下文 BM25 结合，把前 20 个文本块的检索失败率降低 49%。](assets/contextual-retrieval/img_003.webp)
_结合上下文嵌入与上下文 BM25，可将前 20 个文本块的检索失败率降低 49%。_
#### 实现注意事项
实现上下文检索时，有几点需要注意：
  1. **文本块边界：** 考虑如何把文档切分为文本块。文本块大小、边界与重叠的选择会影响检索表现¹。
  2. **嵌入模型：** 虽然上下文检索在我们测试过的所有嵌入模型上都提升了表现，但有些模型可能获益更多。我们发现 [Gemini](<https://ai.google.dev/gemini-api/docs/embeddings>) 与 [Voyage](<https://www.voyageai.com/>) 的嵌入尤其有效。
  3. **自定义上下文化提示词：** 我们提供的通用提示词效果不错，但用针对你具体领域或用例定制的提示词，可能取得更好的结果（例如，加入一份关键术语表，这些术语可能只在知识库的其他文档中才有定义）。
  4. **文本块数量：** 往上下文窗口里放更多文本块，会增加包含相关信息的几率。然而，更多信息也可能分散模型的注意力，所以这有个限度。我们试过投喂 5、10 与 20 个文本块，发现 20 个在这些选项中表现最好（对比见附录），但值得在你的用例上做实验。

**始终运行评估：** 把上下文化的文本块传给模型，并区分哪部分是上下文、哪部分是文本块本身，可能会改善回答生成。
## 用重排序进一步提升表现
在最后一步，我们可以把上下文检索与另一种技术结合，获得更多表现提升。在传统 RAG 中，AI 系统搜索其知识库，找出潜在相关的信息块。对于大型知识库，这种初步检索常常返回大量文本块——有时数百个——相关性与重要性各不相同。
重排序是一种常用的过滤技术，用来确保只有最相关的文本块被传给模型。重排序能带来更好的回答，并降低成本和延迟，因为模型处理的信息更少。关键步骤如下：
  1. 执行初步检索，得到潜在相关的头部文本块（我们用了前 150 个）；
  2. 把前 N 个文本块连同用户查询一起送进重排序模型；
  3. 用重排序模型基于每个文本块对提示词的相关性与重要性打分，然后选出前 K 个文本块（我们用了前 20 个）；
  4. 把前 K 个文本块作为上下文送进模型，生成最终结果。

![结合上下文检索与重排序，最大化检索准确性。](assets/contextual-retrieval/img_004.webp)
_结合上下文检索与重排序，最大化检索准确性。_
### 表现提升
市场上有若干重排序模型。我们用 [Cohere 重排序器](<https://cohere.com/rerank>) 做了测试。Voyage [也提供一个重排序器](<https://docs.voyageai.com/docs/reranker>)，不过我们没时间测试。实验显示，在各领域中，加入重排序步骤都能进一步优化检索。
具体来说，我们发现重排序后的上下文嵌入加上下文 BM25，把前 20 个文本块的检索失败率降低了 67%（5.7% → 1.9%）。
![重排序后的上下文嵌入与上下文 BM25 把前 20 个文本块的检索失败率降低 67%。](assets/contextual-retrieval/img_005.webp)
_重排序后的上下文嵌入与上下文 BM25，可将前 20 个文本块的检索失败率降低 67%。_
#### 成本与延迟考量
重排序的一个重要考量是对延迟与成本的影响，尤其是在对大量文本块做重排序时。由于重排序在运行时增加了一个额外步骤，即便重排序器并行地为所有文本块打分，它也难免增加少量延迟。为重排序更多文本块以求更好表现，与重排序更少文本块以求更低延迟和成本之间，存在固有的取舍。我们建议在你的具体用例上试验不同设置，找到合适的平衡。
## 结论
我们做了大量测试，比较上文所述各项技术的不同组合（嵌入模型、是否使用 BM25、是否使用上下文检索、是否使用重排序器、以及检索出的前 K 个结果总数），并覆盖多种不同的数据集类型。以下是我们发现的要点：
  1. 嵌入加 BM25 优于单用嵌入；
  2. 在我们测试过的模型中，Voyage 与 Gemini 的嵌入最好；
  3. 把前 20 个文本块传给模型，比只传前 10 个或前 5 个更有效；
  4. 为文本块添加上下文能大幅提升检索准确性；
  5. 重排序优于不重排序；
  6. **所有这些收益可以叠加**：为最大化表现提升，我们可以把上下文嵌入（来自 Voyage 或 Gemini）与上下文 BM25 结合，再加一个重排序步骤，并把 20 个文本块加入提示词。

我们鼓励所有使用知识库的开发者，用[我们的 cookbook](<https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide>) 试验这些方法，解锁新的表现水平。
## 附录 I
以下是按数据集、嵌入提供方、是否在嵌入之外使用 BM25、是否使用上下文检索、以及是否使用重排序拆分的结果，指标为 Retrievals @ 20。
Retrievals @ 10 与 @ 5 的拆分结果，以及每个数据集的示例问答，见[附录 II](<https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf>)。
![跨数据集与嵌入提供方的 1 减去 recall @ 20 结果。](assets/contextual-retrieval/img_006.webp)
_跨数据集与嵌入提供方的 1 减去 recall @ 20 的结果。_
## 作者与致谢
### 致谢
研究与撰写：Daniel Ford。感谢 Orowa Sikder、Gautam Mittal 与 Kenneth Lien 的批评性反馈，感谢 Samuel Flamini 实现 cookbook，感谢 Lauren Polansky 的项目协调，以及 Alex Albert、Susan Payne、Stuart Ritchie 与 Brad Abrams 对本篇博文的打磨。
