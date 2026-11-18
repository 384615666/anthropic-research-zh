# 前沿 AI 实验室论文源清单

> 核查日期：2026-09-18　|　实测方式：python3 urllib 直连实测（本机网络，含系统代理），HTTP 状态码为实测值

> 目的：为 Anthropic 论文库（145 篇）补充其他前沿机构的论文来源。

## 状态说明

| 标记 | 含义 |
|---|---|
| 可直抓 | 实测 HTTP 200，可直接抓取 |
| 需绕过反爬 | 实测 403/429，有反爬策略；浏览器或带正常 UA+Referer 可访问，抓取需降速或换通道 |
| 需境外网络 | 本机代理隧道 502，需具备境外网络可达性才能抓取；地址本身有效 |
| 已停止服务 | 站点已下线，仅存归档数据 |

## 优先级说明

- **P0**：论文密度高、与 Anthropic 主题互补、抓取可行 → 建议优先接入
- **P1**：有价值，但需要绕反爬或走代理，或方向偏窄
- **P2**：补充参考，更新频率或相关度较低

## 总览

| 分类 | 数量 | 代表机构 |
|---|---|---|
| 一线实验室 | 11 | Apple、Google DeepMind、Google Research、Meta AI (FAIR) … |
| 模型公司 | 21 | Anthropic、ByteDance Seed、Alibaba Qwen、Cohere / Cohere Labs … |
| 独立研究机构 | 5 | 上海人工智能实验室、Allen Institute for AI (AI2)、EleutherAI、LAION … |
| 安全 · 评估 · 对齐 | 12 | Apollo Research、Epoch AI、METR、Redwood Research … |
| 聚合与发现渠道 | 9 | Hugging Face、arXiv、Semantic Scholar、OpenReview … |
| 学术机构 | 4 | Berkeley BAIR、Stanford HAI、MIT CSAIL、MIT-IBM Watson AI Lab … |

## 一线实验室

*Google/Meta/微软/苹果等大厂研究院*

### Apple　`P0`　`可直抓`

- **论文入口**：<https://machinelearning.apple.com/research>
- **订阅**：<https://machinelearning.apple.com/rss.xml>　✅ 实测可解析出条目
- **实测状态码**：`200`
- **主题**：端侧模型、效率、多模态、隐私
- **说明**：RSS 实测可解析、返回 10 条且带 pubDate（最新 2026-09-17），格式规范，是最容易接入自动化流水线的源。列表页为 JS 渲染，抓取建议直连 RSS。

### Google DeepMind　`P0`　`可直抓`

- **论文入口**：<https://deepmind.google/research/publications/>
- **并列入口**：<https://deepmind.google/research/>　<https://deepmind.google/discover/blog/>
- **站点地图**：<https://deepmind.google/sitemap.xml>
- **实测状态码**：`200`
- **主题**：基础模型、科学AI、可解释性、安全对齐、强化学习
- **说明**：实测 200，结构化的论文库，含摘要与合作机构；sitemap 实测 200。blog.xml 实测 404，与 Anthropic 一样没有官方 RSS，批量抓取需依赖 sitemap 或列表页分页。Gemini 技术报告多走 /discover/blog/。

### Google Research　`P0`　`需境外网络`

- **论文入口**：<https://research.google/pubs>
- **并列入口**：<https://research.google/blog/>
- **主题**：机器学习基础、NLP、感知、推荐系统、负责任AI
- **说明**：论文库规模约 1.14 万篇，支持按年份/团队/研究领域筛选，是最接近 Anthropic research 索引的镜像源。无公开 RSS，需走 sitemap。

### Meta AI (FAIR)　`P0`　`需境外网络`

- **论文入口**：<https://ai.meta.com/results/?content_types[0]=publication>
- **并列入口**：<https://ai.meta.com/research/publications/>　<https://ai.meta.com/blog/>　<https://research.fb.com/publications/>
- **主题**：大模型、计算机视觉、多语言、负责任AI、机器人
- **说明**：Publications 检索页按 Responsible AI / NLP / CV / Speech 等分类，每篇带作者与日期。旧站 research.fb.com 仍在线但内容停留在 2022 年。

### Microsoft Research　`P0`　`可直抓`

- **论文入口**：<https://www.microsoft.com/en-us/research/publications/>
- **并列入口**：<https://www.microsoft.com/en-us/research/blog/>
- **订阅**：<https://www.microsoft.com/en-us/research/feed/>　✅ 实测可解析出条目
- **实测状态码**：`200`
- **主题**：AI 基础、人机交互、系统、医疗AI
- **说明**：论文索引与博客分离；feed 实测可解析且返回 10 条（最新 2026-08-31），也是少见的官方可直接订阅源。

### OpenAI　`P0`　`需绕过反爬`

- **论文入口**：<https://openai.com/research/index/>
- **并列入口**：<https://openai.com/research/>　<https://openai.com/signals/>
- **订阅**：<https://openai.com/news/rss.xml>　✅ 实测可解析出条目
- **实测状态码**：`403`
- **主题**：模型能力、安全、对齐、经济研究
- **说明**：研究正文实际位于 /index/<slug>/ 路径；/research/ 只是概览页，/research/index/ 才是完整索引。重要：网页端 403 反爬，但 news/rss.xml 实测直连 200 且含 1208 条历史条目，是可回溯全量的最佳入口，无需绕反爬。但信噪比低——实测 1208 条中安全/对齐/治理仅 74 条（6%）、经济研究 36 条（2%）、研究论文 32 条（2%），其余 87% 是模型发布与公司动态，入库前必须按关键词过滤。经济研究独立在 /signals/。

### Amazon Science　`P1`　`可直抓`

- **论文入口**：<https://www.amazon.science/>
- **并列入口**：<https://www.amazon.science/blog>
- **实测状态码**：`200`
- **主题**：NLP、搜索推荐、语音、AWS AI
- **说明**：博客实测 200，按研究领域分区，含 Amazon Nova 等自研模型的技术解读。

### NVIDIA Research　`P1`　`需绕过反爬`

- **论文入口**：<https://research.nvidia.com/>
- **并列入口**：<https://research.nvidia.com/labs/>
- **实测状态码**：`403`
- **主题**：硬件加速、图形学、生成模型、机器人
- **说明**：首页实测 200，/labs/ 返回 403。实验室分站（如 Toronto AI Lab）论文密度更高。

### Adobe Research　`P2`　`可直抓`

- **论文入口**：<https://research.adobe.com/>
- **实测状态码**：`200`
- **主题**：生成式视觉、视频编辑、多模态
- **说明**：文生图/视频方向论文密度高，可作为视觉生成方向的补充。

### IBM Research　`P2`　`可直抓`

- **论文入口**：<https://research.ibm.com/>
- **实测状态码**：`200`
- **主题**：企业AI、量子、半导体、可信AI
- **说明**：granite 系列模型与 AAAI/NeurIPS 论文入口。

### 百度研究院　`仅供参考`　`可直抓`

- **论文入口**：<https://research.baidu.com/>
- **实测状态码**：`200`
- **主题**：大模型、自动驾驶、生物计算
- **说明**：页面实测返回 200，但内容显示「网站维护中」，实际已长期停更，不建议作为活跃源。

## 模型公司

*OpenAI/Anthropic/Mistral/国产大模型等*

### Anthropic　`P0`　`可直抓`

- **论文入口**：<https://www.anthropic.com/news>
- **实测状态码**：`200`
- **主题**：模型发布、政策、安全公告
- **说明**：与 research 页互补，模型卡与系统卡（system card）主要发在这里，是论文正文的重要补充。

### ByteDance Seed　`P0`　`可直抓`

- **论文入口**：<https://seed.bytedance.com/en/>
- **实测状态码**：`200`
- **主题**：基础模型、多模态、语音、Agent
- **说明**：站内直接挂 arXiv 链接，实测页面含 arxiv.org 外链，论文聚合度高。

### Alibaba Qwen　`P1`　`可直抓`

- **论文入口**：<https://qwenlm.github.io/blog/>
- **并列入口**：<https://github.com/QwenLM>
- **实测状态码**：`200`
- **主题**：基础模型、多模态、代码模型、开源生态
- **说明**：抓取有坑：2026 年已迁移至 qwen.ai，新站是单页应用（/blog、/research、sitemap.xml 全部返回同一个 HTML 壳，链接数为 0，需 JS 渲染或调后端 API）；旧站 qwenlm.github.io/blog 现仅剩一条「We have a new blog at qwen.ai」的跳转提示。建议改走 GitHub 仓库 Release + arXiv 作者检索。内容本身价值高（Qwen3Guard 安全、Qwen-Image 多模态等）。

### Anthropic　`P1`　`可直抓`

- **论文入口**：<https://www.anthropic.com/engineering>
- **实测状态码**：`200`
- **主题**：Agent 工程、上下文工程、工具设计
- **说明**：工程博客，非严格论文，但对落地实践价值高（如 building-effective-agents 系列）。

### Cohere / Cohere Labs　`P1`　`可直抓`

- **论文入口**：<https://cohere.com/research>
- **并列入口**：<https://cohere.com/blog>
- **实测状态码**：`200`
- **主题**：多语言、检索增强、开源模型、评估
- **说明**：Cohere Labs（原 Cohere For AI）论文多走 arXiv，官网页提供索引。

### DeepSeek　`P1`　`可直抓`

- **论文入口**：<https://github.com/deepseek-ai>
- **并列入口**：<https://api-docs.deepseek.com/news/>
- **实测状态码**：`200`
- **主题**：MoE、推理模型、MLA、开源权重
- **说明**：没有独立论文站。技术报告通过 GitHub 仓库 Release + arXiv 双通道发布，api-docs 的 news 只记 API 变更。

### MiniMax　`P1`　`可直抓`

- **论文入口**：<https://www.minimax.io/news>
- **实测状态码**：`200`
- **主题**：长上下文、语音合成、视频生成、Agent
- **说明**：技术报告以新闻页形式发布，附带 arXiv 链接。

### Mistral AI　`P1`　`需境外网络`

- **论文入口**：<https://mistral.ai/news>
- **订阅**：<https://mistral.ai/news/rss>
- **主题**：开源模型、MoE、OCR、编程模型、物理AI
- **说明**：RSS 有效且字段完整（含发布时间）。模型发布与技术解读混排，research 类文章需按关键词过滤（physics-ai-research、magistral 等）。

### Moonshot AI (Kimi)　`P1`　`可直抓`

- **论文入口**：<https://github.com/MoonshotAI>
- **实测状态码**：`200`
- **主题**：长上下文、MoE、Agent、开源模型
- **说明**：Kimi K2 等技术报告经 GitHub + arXiv 发布，官网 blog 更新不稳定。

### Physical Intelligence (π)　`P1`　`可直抓`

- **论文入口**：<https://www.physicalintelligence.company/blog>
- **实测状态码**：`200`
- **主题**：机器人基础模型、VLA、具身智能
- **说明**：π0 系列机器人基础模型，博客即论文解读，质量高。

### Sakana AI　`P1`　`可直抓`

- **论文入口**：<https://sakana.ai/>
- **实测状态码**：`200`
- **主题**：进化算法、模型合并、AI 科学家、持续学习
- **说明**：日本实验室，论文+博客一体，风格接近 Anthropic 的长文解读，可读性好。

### Stability AI　`P1`　`可直抓`

- **论文入口**：<https://stability.ai/research>
- **并列入口**：<https://stability.ai/news>
- **实测状态码**：`200`
- **主题**：扩散模型、图像生成、音频生成、3D 生成
- **说明**：有独立 research 栏目，实测 200，生成式视觉方向的稳定来源。

### 智谱 AI / Z.ai　`P1`　`可直抓`

- **论文入口**：<https://www.zhipuai.cn/>
- **并列入口**：<https://github.com/THUDM>　<https://github.com/zai-org>
- **实测状态码**：`200`
- **主题**：GLM 系列、长上下文、Agent、开源模型
- **说明**：GLM 技术报告以 GitHub 组织仓库 + arXiv 为主。

### 腾讯混元　`P1`　`可直抓`

- **论文入口**：<https://hunyuan.tencent.com/>
- **实测状态码**：`200`
- **主题**：多模态、视频生成、3D 生成、开源模型
- **说明**：混元系列技术报告经官网 + arXiv 发布，开源模型走 GitHub。

### Figure AI　`P2`　`可直抓`

- **论文入口**：<https://www.figure.ai/news>
- **实测状态码**：`200`
- **主题**：人形机器人、端到端控制
- **说明**：以产品进展为主，论文少。

### Reka AI　`P2`　`可直抓`

- **论文入口**：<https://www.reka.ai/news>
- **实测状态码**：`200`
- **主题**：多模态、视频理解、Agent
- **说明**：更新频率中等。

### Together AI　`P2`　`可直抓`

- **论文入口**：<https://www.together.ai/blog>
- **实测状态码**：`200`
- **主题**：推理加速、训练系统、开源模型
- **说明**：偏工程与系统方向。

### xAI　`P2`　`需境外网络`

- **论文入口**：<https://x.ai/news>
- **主题**：Grok、推理模型、集群工程
- **说明**：更新频率低，以产品发布为主。深度内容主要靠 arXiv 上的 Grok 技术报告。

### 阶跃星辰 StepFun　`P2`　`可直抓`

- **论文入口**：<https://www.stepfun.com/>
- **实测状态码**：`200`
- **主题**：多模态、推理模型、语音
- **说明**：Step 系列模型技术报告主要在 arXiv，官网提供索引。

### 零一万物 01.AI　`P2`　`可直抓`

- **论文入口**：<https://www.01.ai/>
- **实测状态码**：`200`
- **主题**：开源模型、多模态
- **说明**：Yi 系列模型，更新频率已明显下降。

### Anthropic　`已收录`　`可直抓`

- **论文入口**：<https://www.anthropic.com/research>
- **站点地图**：<https://www.anthropic.com/sitemap.xml>
- **实测状态码**：`200`
- **主题**：对齐与安全、可解释性、经济社会影响、能力评测
- **说明**：本项目已抓取 145 篇。sitemap 实测 200，是当前最稳定的批量入口；rss.xml 实测返回 404（官方无 RSS），对比其他厂商属于少数没有订阅通道的站点。

## 独立研究机构

*AI2/EleutherAI/上海AI Lab 等*

### 上海人工智能实验室　`P0`　`可直抓`

- **论文入口**：<https://www.shlab.org.cn/>
- **并列入口**：<https://internvl.github.io/>　<https://opencompass.org.cn/>　<https://github.com/OpenGVLab>
- **实测状态码**：`200`
- **主题**：多模态、评测基准、基础模型、科学AI
- **说明**：InternVL 视觉模型、OpenCompass 评测体系、InternLM 基础模型三条线，实测全部可访问，是国内可抓取性最好的机构之一。

### Allen Institute for AI (AI2)　`P1`　`需绕过反爬`

- **论文入口**：<https://allenai.org/papers>
- **并列入口**：<https://allenai.org/blog>
- **实测状态码**：`403`
- **主题**：开源模型、NLP、多模态、科学AI
- **说明**：OLMo 系列开源模型与开放数据集的主要发布方。403 为反爬，浏览器可正常访问。

### EleutherAI　`P1`　`可直抓`

- **论文入口**：<https://www.eleuther.ai/papers>
- **并列入口**：<https://www.eleuther.ai/papers-blog/>　<https://www.eleuther.ai/>
- **实测状态码**：`200`
- **主题**：开源模型、可解释性、对齐、评测
- **说明**：注意路径：旧地址 blog.eleuther.ai 实测仅剩跳转提示、无文章链接，真实列表已迁至 /papers 与 /papers-blog/。可解释性方向（sparse autoencoder、可组合干预等）与 Anthropic 主线高度重合，是不同方法论的外部对照。

### LAION　`P2`　`可直抓`

- **论文入口**：<https://laion.ai/blog/>
- **实测状态码**：`200`
- **主题**：开放数据集、多模态、可复现研究
- **说明**：以数据集与复现研究为主。

### 智源研究院 BAAI　`P2`　`可直抓`

- **论文入口**：<https://hub.baai.ac.cn/>
- **实测状态码**：`200`
- **主题**：基础模型、评测、开源生态
- **说明**：智源社区，含论文速递栏目，中文语境下的论文聚合价值高。

## 安全 · 评估 · 对齐

*与 Anthropic 主线最互补*

### Apollo Research　`P0`　`可直抓`

- **论文入口**：<https://www.apolloresearch.ai/>
- **实测状态码**：`200`
- **主题**：欺骗性对齐、阴谋行为评估、监督
- **说明**：受控评测（in-context scheming）方法论与 Anthropic 的 sleeper agents／alignment faking 一脉相承。

### Epoch AI　`P0`　`可直抓`

- **论文入口**：<https://epoch.ai/publications>
- **实测状态码**：`200`
- **主题**：算力趋势、数据墙、基准数据库、AI 经济
- **说明**：定量数据驱动，与 Anthropic Economic Index 系列形成数据互补。

### METR　`P0`　`可直抓`

- **论文入口**：<https://metr.org/blog>
- **实测状态码**：`200`
- **主题**：能力评估、自主性、风险评估、红队
- **说明**：实测列表页含 29 条，是本批外部源中体量最大、主题最对口的一个。与 Anthropic 的 sabotage-evaluations、measuring-agent-autonomy、forecasting-rare-behaviors 直接对话，且提供的是第三方评估视角（Anthropic 的评估类论文多为自评）。

### Redwood Research　`P0`　`可直抓`

- **论文入口**：<https://www.redwoodresearch.org/research>
- **实测状态码**：`200`
- **主题**：AI 控制、对齐、可解释性
- **说明**：AI Control 议程的提出方，与 Anthropic 的 sabotage/shade-arena 系列强相关。

### Alignment Research Center (ARC)　`P1`　`可直抓`

- **论文入口**：<https://alignment.org/>
- **实测状态码**：`200`
- **主题**：eliciting latent knowledge、威胁模型、理论对齐
- **说明**：输出以理论文章为主，更新频率低但单篇分量重。

### Timaeus　`P1`　`可直抓`

- **论文入口**：<https://timaeus.co/>
- **实测状态码**：`200`
- **主题**：可解释性、物理启发方法
- **说明**：可解释性专门机构，视角与 Anthropic 的 circuits 路线不同，可作对照阅读。

### UK AI Security Institute　`P1`　`可直抓`

- **论文入口**：<https://www.aisi.gov.uk/>
- **实测状态码**：`200`
- **主题**：前沿模型评测、安全治理、政策
- **说明**：国家级评测机构，发布独立的前沿模型测评报告。

### Alignment Forum　`P2`　`需绕过反爬`

- **论文入口**：<https://www.alignmentforum.org/>
- **实测状态码**：`429`
- **主题**：对齐讨论、技术笔记
- **说明**：429 为限流，属正常现象，需降速抓取。内容为非正式技术笔记，质量参差但前沿讨论集中。

### FAR.AI　`P2`　`可直抓`

- **论文入口**：<https://far.ai/>
- **实测状态码**：`200`
- **主题**：前沿对齐研究、评测、治理
- **说明**：含研究议程与出版物索引。

### Goodfire AI　`P2`　`可直抓`

- **论文入口**：<https://www.goodfire.ai/>
- **实测状态码**：`200`
- **主题**：可解释性、稀疏自编码器
- **说明**：SAE 方向的工程化落地，与 Anthropic 的 monosemanticity 研究直接相关。

### NIST CAISI (美国)　`P2`　`可直抓`

- **论文入口**：<https://www.nist.gov/aisi>
- **实测状态码**：`200`
- **主题**：标准与评测、AI 安全指南
- **说明**：偏标准与框架文件，非论文。

### Transluce　`P2`　`可直抓`

- **论文入口**：<https://transluce.org/>
- **实测状态码**：`200`
- **主题**：可解释性、模型审计
- **说明**：可解释性产品化公司，有公开研究报告。

## 聚合与发现渠道

*arXiv/HuggingFace/评审平台*

### Hugging Face　`P0`　`需境外网络`

- **论文入口**：<https://huggingface.co/papers>
- **并列入口**：<https://huggingface.co/papers/trending>
- **主题**：全领域、社区热度排序
- **说明**：Daily Papers + Trending Papers。Papers with Code 关停后，Trending Papers 由 HF 与 Meta 合作承接。热榜机制天然过滤噪声，适合做选题发现。

### arXiv　`P0`　`可直抓`

- **论文入口**：<https://arxiv.org/list/cs.AI/recent>
- **订阅**：<https://arxiv.org/rss/cs.AI>　✅ 实测可解析出条目
- **实测状态码**：`200`
- **主题**：全领域预印本
- **说明**：所有厂商的技术报告最终都会落到 arXiv。RSS 实测可解析，单次返回 304 条、带 pubDate，是可靠的自动增量入口。建议配合机构白名单（作者单位关键词）过滤。

### arXiv　`P0`　`可直抓`

- **论文入口**：<https://arxiv.org/list/cs.CL/recent>
- **订阅**：<https://arxiv.org/rss/cs.CL>　✅ 实测可解析出条目
- **实测状态码**：`200`
- **主题**：计算语言学 / NLP
- **说明**：语言模型方向论文量最大。RSS 实测可解析，单次返回 171 条、带 pubDate，日更。

### Semantic Scholar　`P1`　`可直抓`

- **论文入口**：<https://www.semanticscholar.org/>
- **实测状态码**：`200`
- **主题**：论文元数据、引用图谱
- **说明**：有公开 API，适合做引用关系与元数据补全（引文、作者、领域标签）。

### arXiv　`P1`　`可直抓`

- **论文入口**：<https://arxiv.org/list/cs.LG/recent>
- **订阅**：<https://arxiv.org/rss/cs.LG>
- **实测状态码**：`200`
- **主题**：机器学习
- **说明**：训练方法、架构创新集中地。

### OpenReview　`P2`　`可直抓`

- **论文入口**：<https://openreview.net/>
- **实测状态码**：`200`
- **主题**：会议投稿、评审意见
- **说明**：ICLR/NeurIPS 等会议的公开评审记录，能看到论文的争议点，价值高于单纯摘要。

### alphaXiv　`P2`　`可直抓`

- **论文入口**：<https://www.alphaxiv.org/>
- **实测状态码**：`200`
- **主题**：arXiv 论文讨论层
- **说明**：给 arXiv 论文附加社区注释与问答，适合筛选高价值论文。

### arXiv　`P2`　`可直抓`

- **论文入口**：<https://arxiv.org/list/cs.SE/recent>
- **实测状态码**：`200`
- **主题**：软件工程、代码智能
- **说明**：配合 SWE-bench 等代码 Agent 评测方向。

### Papers with Code（已关停）　`仅供参考`　`已停止服务`

- **论文入口**：<https://github.com/paperswithcode/paperswithcode-data>
- **主题**：论文-代码-榜单关联
- **说明**：Meta 于 2025-07-24 关停，域名现重定向至 Hugging Face Trending Papers。历史快照（约 57.6 万篇论文、30 万条论文-代码关联）以 JSON 形式存档在 GitHub，只可作历史检索，不再更新。

## 学术机构

*Berkeley/MIT/Stanford 等*

### Berkeley BAIR　`P1`　`可直抓`

- **论文入口**：<https://bair.berkeley.edu/blog/>
- **订阅**：<https://bair.berkeley.edu/blog/feed.xml>　✅ 实测可解析出条目
- **实测状态码**：`200`
- **主题**：机器人、强化学习、视觉
- **说明**：实测 200，且 blog/feed.xml 可解析出 10 条（最新 2026-07-29）。博客由论文作者亲自撰写，是理解研究动机的最佳渠道，可读性接近 Anthropic 的长文。

### Stanford HAI　`P1`　`可直抓`

- **论文入口**：<https://hai.stanford.edu/research>
- **实测状态码**：`200`
- **主题**：AI 政策、经济影响、社会影响
- **说明**：年度 AI Index 报告发布方，与 Anthropic Economic Index 属同一议题域。

### MIT CSAIL　`P2`　`可直抓`

- **论文入口**：<https://www.csail.mit.edu/research>
- **实测状态码**：`200`
- **主题**：AI 理论、系统、机器人、计算生物学
- **说明**：偏学术，论文密度高。

### MIT-IBM Watson AI Lab　`P2`　`需绕过反爬`

- **论文入口**：<https://mitibmwatsonailab.mit.edu/research/publications/>
- **实测状态码**：`403`
- **主题**：AI 基础、可信AI、计算生物学
- **说明**：产学合作实验室，有独立的出版物索引。

## 落地建议

### 〇、推荐接入顺序（基于实测数据，非经验判断）

先看现有 157 篇的分布，判断缺口在哪：

| 分类 | 篇数 | | 分类 | 篇数 |
|---|---|---|---|---|
| Alignment | 43 | | Science | 10 |
| Interpretability | 31 | | Policy | 9 |
| Frontier Red Team | 22 | | Engineering | 2 |
| Societal Impacts | 19 | | Evaluations | 1 |
| Economic Research | 15 | | 其余 | 4 |

**强项是对齐（43）、可解释性（31）、红队（22）——全是 Anthropic 自己的视角。真正的缺口是「第三方评估」和「竞对对照」。** 所以推荐按下面的顺序补，而不是按机构名气补。

#### 第一梯队：建议立刻接入

**1. METR — 29 篇，可直抓**
- 本批外部源中体量最大、主题最对口的一个。
- 它是第三方评估机构，与库内 22 篇前沿红队论文逐篇对话；而 Anthropic 的评估类论文多为自评，正好补上外部视角。
- 技术上门槛最低：列表页直连 200，无反爬、无代理需求。

**2. OpenAI 安全线 — 142 篇候选（需从 1208 条中过滤）**
- 唯一能提供竞对对照的源。GPT 系列系统卡、安全框架、模型误对齐报告框架，可与 Anthropic 的同名文档直接对读。
- **但必须过滤**：实测 1208 条里安全/对齐 74 条（6%）、经济研究 36 条（2%）、研究论文 32 条（2%），其余 87% 是产品发布与公司动态。不做过滤直接入库会把库的纯度拉垮。
- 抓取走 RSS（直连 200），不需要绕网页端的 403。

**3. arXiv 机构白名单 — 底网**
- 所有厂商的技术报告最终都会落到 arXiv，这是唯一不会漏的通道。
- 但不要全抓：cs.CL 日更 171 条、cs.AI 304 条。建议按作者单位关键词（OpenAI、Anthropic、Google DeepMind、Meta、Qwen、DeepSeek…）过滤后再入库。

#### 第二梯队：按兴趣选

**4. 可解释性外部视角 — Goodfire 12 + Timaeus 9 + EleutherAI**
- 库内 31 篇可解释性论文全部是 Anthropic 自己的 circuits 路线。这三家提供不同方法论：Goodfire 的 SAE 工程化、Timaeus 的物理启发方法、EleutherAI 的可组合干预。适合做「同一问题的不同解法」对照阅读。

**5. 定量与经济 — Epoch AI + Stanford HAI**
- 补 Economic Index 系列的第三方数据面。Epoch AI 的算力趋势与数据墙研究是定量支撑，Stanford HAI 的年度 AI Index 是同类议题的对照组。

#### 不建议接入

- **NVIDIA / Adobe / IBM / Amazon**：议题不对口（硬件、视觉编辑、企业 IT），翻译 ROI 低。
- **MIT / Stanford / Berkeley 等学术机构**：论文量巨大但质量参差，缺乏明确的筛选标准，会把库变成摘要堆。

### 一、可直接接入的订阅源（已实测能解析出条目）

| 源 | 订阅地址 | 实测结果 |
|---|---|---|
| OpenAI | `https://openai.com/news/rss.xml` | 返回 **1208 条**，日期完整，最新 2026-09-17 |
| arXiv cs.AI | `https://arxiv.org/rss/cs.AI` | 单次 **304 条**，日更 |
| arXiv cs.CL | `https://arxiv.org/rss/cs.CL` | 单次 **171 条**，日更 |
| Apple ML Research | `https://machinelearning.apple.com/rss.xml` | 10 条，含 pubDate，最新 2026-09-17 |
| Microsoft Research | `https://www.microsoft.com/en-us/research/feed/` | 10 条，最新 2026-08-31 |
| Berkeley BAIR | `https://bair.berkeley.edu/blog/feed.xml` | 10 条，最新 2026-07-29 |

**其中最重要的一条发现**：OpenAI 网页端虽然返回 403 反爬，但 `news/rss.xml` 直连即可拿到 1208 条历史条目。这意味着 OpenAI 是整个清单里**最容易接、且能一次性回溯全量**的源，不需要做反爬绕过。

### 二、需要解析列表页的源（无 RSS）

Anthropic 自身的 `rss.xml` 与 DeepMind 的 `blog.xml` 实测均返回 **404**——两家都没有官方订阅通道，只能依赖 `sitemap.xml` 或列表页分页。Google Research pubs、Meta AI publications 同样无公开 RSS。这几个源的抓取成本明显高于上面的订阅源，建议复用在 Anthropic 上已经跑通的 sitemap 方案。

### 三、主题互补性最强的推荐组合

Anthropic 论文的强项是**对齐、可解释性、风险评估、AI 经济影响**。要形成完整议题，建议按组补：
- **对齐与评估**：METR + Apollo Research + Redwood Research（这三家的评测方法与 Anthropic 的 sabotage-evaluations、sleeper-agents 系列直接对话）
- **可解释性**：EleutherAI + Timaeus + Goodfire（与 Anthropic 的 circuits / monosemanticity 路线形成对照）
- **定量与算力**：Epoch AI（与 Anthropic Economic Index 形成数据互补）
- **中文语境补位**：上海人工智能实验室（InternVL / OpenCompass）、字节 Seed、阿里 Qwen——这三家的中文技术解读最稀缺，翻译价值最高

### 四、执行成本提示

- **优先级 P0 但状态为「需境外网络」的源**（Google Research、Meta AI、Hugging Face、Mistral、xAI）：地址有效，但抓取需要具备境外网络可达性，建议评估后再排期。
- **状态为「需绕过反爬」的源**（OpenAI 网页端、NVIDIA labs、AI2、MLCommons）：403 是 UA/频率策略，降速 + 真实 UA 通常可解。
- **版权**：多数实验室采用 CC BY-NC 或自定义条款，公开发布翻译前需逐一核对许可。arXiv 预印本相对宽松，但也要保留原文出处与作者署名。

## 已失效或需注意的源

- **Papers with Code**：2025-07-24 被 Meta 关停，域名已重定向到 Hugging Face Trending Papers，按任务组织的 SOTA 榜单能力无同类替代。
- **百度研究院**：页面维持「网站维护中」状态，长期停更。
- **Meta 旧站 research.fb.com**：仍在线，但内容停留在 2022 年前后，勿作为活跃源。
