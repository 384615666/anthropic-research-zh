---
title: Introducing advanced tool use on the Claude Developer Platform
url: https://www.anthropic.com/research/advanced-tool-use
date: Nov 24, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# 在Claude开发者平台上推出高级工具使用

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/advanced-tool-use

---

工程（Engineering）
2025 年 11 月 24 日
![在Claude开发者平台上推出高级工具使用](assets/advanced-tool-use/img_000.webp)
已发布
    2025 年 11 月 24 日
团队
    [工程](</engineering>)
主题
    
  * [工具使用](</search?topic=tool-use>)
  * [Claude开发者平台](</search?topic=claude-developer-platform>)
  * [上下文工程](</search?topic=context-engineering>)
  * [智能体](</search?topic=agents>)
  * [模型上下文协议](</search?topic=model-context-protocol>)

[](</news/anthropic-acquires-stainless>)[](</research/managed-agents>)[](</research/code-execution-with-mcp>)[](</research/effective-context-engineering-for-ai-agents>)
相关文章
  * 公告
2026 年 5 月 18 日
[Anthropic收购Stainless](</news/anthropic-acquires-stainless>)

[查看更多](</search?topic=tool-use>)
AI智能体的未来，是模型能无缝地横跨成百上千种工具工作：一个IDE助手，整合git操作、文件处理、包管理器、测试框架与部署流水线；一个运营协调者，同时接上Slack、GitHub、Google Drive、Jira、公司数据库，以及数十个MCP服务器。
要[构建高效的智能体](<https://www.anthropic.com/research/building-effective-agents>)，就得让它们能使用不受限的工具库，而不必一开始就把每个定义都塞进上下文。我们关于[用MCP做代码执行](<https://www.anthropic.com/engineering/code-execution-with-mcp>)的博客文章讨论过：在智能体读到请求之前，工具结果与定义有时就能耗掉50,000+个token。智能体应当按需发现并加载工具，只保留与当前任务相关的内容。
智能体还需要能从代码中调用工具。用自然语言调用工具时，每一次调用都要跑一遍完整推理，中间结果无论有用与否都堆积在上下文里。代码天然适合编排逻辑，例如循环、条件与数据转换。智能体需要能根据手头任务，在代码执行与推理之间灵活选择。
智能体还需要从示例中学习正确的工具用法，而不只是靠schema定义。JSON schema能界定结构上什么有效，却表达不了使用模式：何时该带上可选参数、哪些组合才合理、你的API遵循什么约定。
今天，我们发布三项功能，让这一切成为可能：
  * **工具搜索工具（Tool Search Tool），**让Claude借助搜索工具访问数千种工具，而不占用其上下文窗口
  * **编程式工具调用（Programmatic Tool Calling），**让Claude在代码执行环境中调用工具，降低对模型上下文窗口的影响
  * **工具使用示例（Tool Use Examples），**为演示如何高效使用某个工具提供一套通用标准

在内部测试中，我们发现这些功能帮我们做出了用传统工具使用模式根本无法实现的东西。例如，**[Claude for Excel](<https://www.claude.com/claude-for-excel>) **就用编程式工具调用来读取并修改有数千行的电子表格，而不会让模型的上下文窗口过载。
基于我们的经验，我们相信这些功能为用Claude能构建什么打开了新的可能性。
![视频缩略图](assets/advanced-tool-use/img_001.webp)
## 工具搜索工具
### 挑战
MCP工具定义提供了重要的上下文，但随着接入的服务器变多，这些token会累积起来。看一个五服务器的配置：
  * GitHub：35个工具（约26K个token）
  * Slack：11个工具（约21K个token）
  * Sentry：5个工具（约3K个token）
  * Grafana：5个工具（约3K个token）
  * Splunk：2个工具（约2K个token）

这就是58个工具，在对话还没开始时就耗掉约55K个token。再加上更多服务器，比如Jira（单它一个就用约17K个token），很快就逼近100K+的token开销。在Anthropic，我们见过工具定义在优化前耗掉134K个token。
但token成本并非唯一问题。最常见的失败是选错工具、参数不对，尤其当工具名称相近时，例如`notification-send-user`与`notification-send-channel`。
### 我们的方案
工具搜索工具不再一开始加载全部工具定义，而是按需发现工具。Claude只会看到当前任务真正需要的那些工具。
![工具搜索工具示意图](assets/advanced-tool-use/img_002.png)
与传统方式下的122,800个token相比，工具搜索工具保留了191,300个token的上下文。
传统方式：
  * 一开始就加载全部工具定义（50多个MCP工具约72K个token）
  * 对话历史与系统提示争夺剩余空间
  * 总上下文消耗：任何工作开始前约77K个token

使用工具搜索工具时：
  * 一开始只加载工具搜索工具（约500个token）
  * 按需发现所需工具（3-5个相关工具，约3K个token）
  * 总上下文消耗：约8.7K个token，保留95%的上下文窗口

这相当于token用量减少85%，同时仍能访问完整的工具库。内部测试显示，在大型工具库下，MCP评估的准确率有显著提升。启用工具搜索工具后，Opus 4从49%提升到74%，Opus 4.5从79.5%提升到88.1%。
### 工具搜索工具如何工作
工具搜索工具让Claude动态发现工具，而不是一开始加载全部定义。你把全部工具定义交给API，但用`defer_loading: true`标记工具，让它们可被按需发现。被延迟的工具起初不会载入Claude的上下文。Claude只会看到工具搜索工具本身，以及任何标了`defer_loading: false`的工具（你最关键、最常用的那些）。
当Claude需要某项具体能力时，它会搜索相关工具。工具搜索工具返回匹配工具的引用，这些引用随后在Claude的上下文中展开为完整定义。
例如，若Claude要与GitHub交互，它搜索「github」，于是只有`github.createPullRequest`与`github.listIssues`被加载——而来自Slack、Jira、Google Drive的另外50多个工具则不会被加载。
这样一来，Claude既能访问你的完整工具库，又只需为它真正用到的工具付出token成本。
**关于提示缓存：** 工具搜索工具不会破坏提示缓存，因为被延迟的工具完全不出现在初始提示里。它们只在Claude搜索之后才加入上下文，因此你的系统提示与核心工具定义仍可缓存。
**实现：**
    
    {
      "tools": [
        // Include a tool search tool (regex, BM25, or custom)
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    
        // Mark tools for on-demand discovery
        {
          "name": "github.createPullRequest",
          "description": "Create a pull request",
          "input_schema": {...},
          "defer_loading": true
        }
        // ... hundreds more deferred tools with defer_loading: true
      ]
    }
    
对于MCP服务器，你可以延迟加载整台服务器，同时让特定的高频工具保持加载：
    
    {
      "type": "mcp_toolset",
      "mcp_server_name": "google-drive",
      "default_config": {"defer_loading": true}, # defer loading the entire server
      "configs": {
        "search_files": {
    "defer_loading": false
        }  // Keep most used tool loaded
      }
    }
Claude开发者平台开箱即用地提供基于正则与基于BM25的搜索工具，但你也可以用嵌入或其他策略实现自定义搜索工具。
### 何时使用工具搜索工具
和任何架构决策一样，启用工具搜索工具也涉及取舍。该功能在工具调用前增加了一步搜索，因此只有当上下文节省与准确率提升盖过额外延迟时，它的投入产出比才最高。
**在以下情形使用：**
  * 工具定义消耗超过10K个token
  * 遇到工具选择准确率问题
  * 构建带多台服务器的MCP系统
  * 可用工具达10个以上

**在以下情形收益较低：**
  * 工具库很小（少于10个工具）
  * 每次会话都频繁用到全部工具
  * 工具定义很紧凑

## 编程式工具调用
### 挑战
随着工作流变复杂，传统工具调用会带来两个根本问题：
  * **中间结果造成的上下文污染**：当Claude分析一个10MB的日志文件以找出错误模式时，整个文件都会进入它的上下文窗口，哪怕Claude只需要一份错误频率的汇总。跨多张表抓取客户数据时，每条记录无论是否相关都会堆进上下文。这些中间结果吞掉大量token预算，甚至可能把重要信息完全挤出上下文窗口。
  * **推理开销与人工综合**：每一次工具调用都要跑一遍完整的模型推理。拿到结果后，Claude还得「用眼睛估量」数据、提取相关信息、推敲各部分如何拼合、再决定下一步做什么——全都经由自然语言处理。一个五步工具工作流，意味着五次推理，再加上Claude逐条解析结果、比较数值、综合结论。这既慢又容易出错。

### 我们的方案
编程式工具调用让Claude通过代码来编排工具，而不是靠一次次API往返。Claude不再逐个请求工具、把每个结果都送回自己的上下文，而是写代码调用多个工具、处理它们的输出，并掌控究竟哪些信息进入其上下文窗口。
Claude擅长写代码；让它用Python表达编排逻辑、而非通过自然语言调用工具，你能得到更可靠、更精确的控制流。循环、条件、数据转换与错误处理都显式写在代码里，而不是隐含在Claude的推理中。
#### 示例：预算合规检查
看一个常见的业务任务：「哪些团队成员超出了Q3的差旅预算？」
你有三个可用工具：
  * `get_team_members(department)` \- 返回带ID与职级的团队成员列表
  * `get_expenses(user_id, quarter)` \- 返回某用户的费用明细
  * `get_budget_by_level(level)` \- 返回某职级的预算上限

**传统方式**：
  * 抓取团队成员 → 20人
  * 为每个人抓取其Q3费用 → 20次工具调用，每次返回50-100条明细（机票、酒店、餐饮、收据）
  * 按职级抓取预算上限
  * 所有这些都进入Claude的上下文：2,000+条费用明细（50 KB+）
  * Claude手动汇总每个人的费用、查其预算、把费用与预算上限比较
  * 更多次与模型往返，上下文消耗显著

**使用编程式工具调用时**：
Claude不再让每个工具结果都返回给自己，而是写一段Python脚本来编排整个工作流。脚本运行在代码执行工具（一个沙箱环境）里，需要你那些工具的结果时便暂停。当你通过API返回工具结果时，它们由脚本处理，而不是被模型消费。脚本继续执行，Claude只看到最终输出。
![编程式工具调用流程](assets/advanced-tool-use/img_003.webp)
编程式工具调用让Claude通过代码而非一次次API往返来编排工具，从而支持并行执行工具。
针对预算合规任务，Claude写出的编排代码如下：
    
    team = await get_team_members("engineering")
    
    # Fetch budgets for each unique level
    levels = list(set(m["level"] for m in team))
    budget_results = await asyncio.gather(*[
        get_budget_by_level(level) for level in levels
    ])
    
    # Create a lookup dictionary: {"junior": budget1, "senior": budget2, ...}
    budgets = {level: budget for level, budget in zip(levels, budget_results)}
    
    # Fetch all expenses in parallel
    expenses = await asyncio.gather(*[
        get_expenses(m["id"], "Q3") for m in team
    ])
    
    # Find employees who exceeded their travel budget
    exceeded = []
    for member, exp in zip(team, expenses):
        budget = budgets[member["level"]]
        total = sum(e["amount"] for e in exp)
        if total > budget["travel_limit"]:
            exceeded.append({
                "name": member["name"],
                "spent": total,
                "limit": budget["travel_limit"]
            })
    
    print(json.dumps(exceeded))
Claude的上下文只收到最终结果：超支的两三个人。2,000+条明细、中间求和与预算查询都不影响Claude的上下文，把消耗从200KB原始费用数据压到仅1KB结果。
效率提升相当可观：
  * **节省token**：把中间结果挡在Claude的上下文之外，编程式工具调用大幅降低token消耗。在复杂研究任务上，平均用量从43,588降到27,297个token，降幅37%。
  * **降低延迟**：每一次API往返都需要模型推理（几百毫秒到几秒）。当Claude在单个代码块里编排20多次工具调用时，就省掉了19次以上的推理。API负责执行工具，不必每次都回到模型。
  * **提升准确率**：写出显式的编排逻辑后，Claude比不得不用自然语言同时兼顾多个工具结果时出错更少。内部知识检索从25.6%提升到28.5%；[GIA基准](<https://arxiv.org/abs/2311.12983>)从46.5%提升到51.2%。

生产环境的工作流涉及杂乱的数据、条件逻辑，以及需要伸缩的操作。编程式工具调用让Claude以编程方式处理这种复杂性，同时把注意力放在可付诸行动的结果上，而非原始数据处理。
### 编程式工具调用如何工作
#### 1\. 把工具标记为可从代码调用
把code_execution加入tools，并设置allowed_callers，让工具选择加入编程式执行：
    
    {
      "tools": [
        {
          "type": "code_execution_20250825",
          "name": "code_execution"
        },
        {
          "name": "get_team_members",
          "description": "Get all members of a department...",
          "input_schema": {...},
          "allowed_callers": ["code_execution_20250825"] # opt-in to programmatic tool calling
        },
        {
          "name": "get_expenses",
     	...
        },
        {
          "name": "get_budget_by_level",
    	...
        }
      ]
    }
API会把这些工具定义转换成Claude可调用的Python函数。
#### 2\. Claude编写编排代码
Claude不再逐个请求工具，而是生成Python代码：
    
    {
      "type": "server_tool_use",
      "id": "srvtoolu_abc",
      "name": "code_execution",
      "input": {
        "code": "team = get_team_members('engineering')\n..." # the code example above
      }
    }
#### 3\. 工具执行不触及Claude的上下文
当代码调用get_expenses()时，你会收到一个带caller字段的工具请求：
    
    {
      "type": "tool_use",
      "id": "toolu_xyz",
      "name": "get_expenses",
      "input": {"user_id": "emp_123", "quarter": "Q3"},
      "caller": {
        "type": "code_execution_20250825",
        "tool_id": "srvtoolu_abc"
      }
    }
你提供结果，它在代码执行环境中被处理，而非进入Claude的上下文。这个请求—响应循环会对代码里的每次工具调用重复一遍。
#### 4\. 只有最终输出进入上下文
代码运行结束后，只有代码的结果被返回给Claude：
    
    {
      "type": "code_execution_tool_result",
      "tool_use_id": "srvtoolu_abc",
      "content": {
        "stdout": "[{\"name\": \"Alice\", \"spent\": 12500, \"limit\": 10000}...]"
      }
    }
这就是Claude看到的全部，而不是沿途处理过的2000+条费用明细。
### 何时使用编程式工具调用
编程式工具调用给工作流增加了一步代码执行。当token节省、延迟改善与准确率提升都相当可观时，这份额外开销才划得来。
**在以下情形收益最高：**
  * 处理大型数据集，而你只需要聚合结果或汇总
  * 运行含三次及以上相互依赖的工具调用的多步工作流
  * 在Claude看到之前先对工具结果做过滤、排序或转换
  * 处理中间数据不应影响Claude推理的任务
  * 对许多条目并行执行操作（例如检查50个端点）

**在以下情形收益较低：**
  * 只做简单的单工具调用
  * 任务里Claude本就该看到并推敲全部中间结果
  * 响应很小的快速查询

## 工具使用示例
### 挑战
JSON Schema擅长定义结构——类型、必填字段、允许的枚举——却表达不了使用模式：何时该带上可选参数、哪些组合才合理、你的API遵循什么约定。
看一个工单API：
    
    {
      "name": "create_ticket",
      "input_schema": {
        "properties": {
          "title": {"type": "string"},
          "priority": {"enum": ["low", "medium", "high", "critical"]},
          "labels": {"type": "array", "items": {"type": "string"}},
          "reporter": {
            "type": "object",
            "properties": {
              "id": {"type": "string"},
              "name": {"type": "string"},
              "contact": {
                "type": "object",
                "properties": {
                  "email": {"type": "string"},
                  "phone": {"type": "string"}
                }
              }
            }
          },
          "due_date": {"type": "string"},
          "escalation": {
            "type": "object",
            "properties": {
              "level": {"type": "integer"},
              "notify_manager": {"type": "boolean"},
              "sla_hours": {"type": "integer"}
            }
          }
        },
        "required": ["title"]
      }
    }
schema界定了什么有效，却把几个关键问题悬在那里：
  * **格式歧义：** `due_date`该用「2024-11-06」、「Nov 6, 2024」，还是「2024-11-06T00:00:00Z」？
  * **ID约定：** `reporter.id`是UUID、「USR-12345」，还是就写「12345」？
  * **嵌套结构的用法：** Claude该在什么时候填`reporter.contact`？
  * **参数关联：** `escalation.level`与`escalation.sla_hours`同priority是什么关系？

这些歧义会导致格式错误的工具调用与前后不一致的参数用法。
### 我们的方案
工具使用示例让你直接在工具定义里给出示例调用。不必只靠schema，而是把具体的使用模式摆给Claude看：
    
    {
        "name": "create_ticket",
        "input_schema": { /* same schema as above */ },
        "input_examples": [
          {
            "title": "Login page returns 500 error",
            "priority": "critical",
            "labels": ["bug", "authentication", "production"],
            "reporter": {
              "id": "USR-12345",
              "name": "Jane Smith",
              "contact": {
                "email": "jane@acme.com",
                "phone": "+1-555-0123"
              }
            },
            "due_date": "2024-11-06",
            "escalation": {
              "level": 2,
              "notify_manager": true,
              "sla_hours": 4
            }
          },
          {
            "title": "Add dark mode support",
            "labels": ["feature-request", "ui"],
            "reporter": {
              "id": "USR-67890",
              "name": "Alex Chen"
            }
          },
          {
            "title": "Update API documentation"
          }
        ]
      }
从这三个示例里，Claude学到：
  * **格式约定**：日期用YYYY-MM-DD，用户ID遵循USR-XXXXX，标签用kebab-case
  * **嵌套结构模式**：如何构造带嵌套contact对象的reporter对象
  * **可选参数关联**：严重bug带完整联系信息加升级、配紧凑的SLA；功能请求有reporter但没有contact/升级；内部任务只有title

在我们自己的内部测试中，工具使用示例把复杂参数处理的准确率从72%提升到90%。
### 何时使用工具使用示例
工具使用示例会给工具定义增加token，因此只有当准确率提升盖过额外成本时，它们才最有价值。
**在以下情形收益最高：**
  * 嵌套结构复杂，合法的JSON并不等于用法正确
  * 工具带大量可选参数，且哪些该带上有讲究
  * API带有schema没捕捉到的领域专属约定
  * 工具彼此相似，需要靠示例说清该用哪个（例如`create_ticket`与`create_incident`）

**在以下情形收益较低：**
  * 用法一目了然的简单单参数工具
  * Claude本就理解的标准格式，如URL或邮箱
  * 更适合交给JSON Schema约束处理的校验问题

## 最佳实践
构建会在真实世界里采取行动的智能体，意味着要同时应对规模、复杂性与精确度。这三项功能协同解决工具使用工作流里不同的瓶颈。下面讲如何有效地把它们组合起来。
### 有策略地叠加功能
并非每个智能体完成某项任务都需要用上全部三项功能。从你最大的瓶颈入手：
  * 工具定义造成的上下文膨胀 → 工具搜索工具
  * 大量中间结果污染上下文 → 编程式工具调用
  * 参数错误与格式错误的调用 → 工具使用示例

这种有的放矢的做法，让你针对真正限制智能体表现的那个约束下手，而不是一上来就堆复杂度。
随后再按需叠加其他功能。它们是互补的：工具搜索工具确保找到对的工具，编程式工具调用确保高效执行，工具使用示例确保调用正确。
### 配置工具搜索工具以改善发现效果
工具搜索依据名称与描述做匹配，因此清晰、有说明性的定义能提升发现准确率。
    
    // Good
    {
        "name": "search_customer_orders",
        "description": "Search for customer orders by date range, status, or total amount. Returns order details including items, shipping, and payment info."
    }
    
    // Bad
    {
        "name": "query_db_orders",
        "description": "Execute order query"
    }
加上系统提示指引，让Claude知道有哪些能力可用：
    
    You have access to tools for Slack messaging, Google Drive file management, 
    Jira ticket tracking, and GitHub repository operations. Use the tool search 
    to find specific capabilities.
把你最常用的三到五个工具保持常驻加载，其余的延迟加载。这样既让常见操作能立即取用，又让其他一切按需发现，两者取得平衡。
### 配置编程式工具调用以确保正确执行
由于Claude要写代码解析工具输出，请把返回格式写清楚。这能帮Claude写出正确的解析逻辑：
    
    {
        "name": "get_orders",
        "description": "Retrieve orders for a customer.
    Returns:
        List of order objects, each containing:
        - id (str): Order identifier
        - total (float): Order total in USD
        - status (str): One of 'pending', 'shipped', 'delivered'
        - items (list): Array of {sku, quantity, price}
        - created_at (str): ISO 8601 timestamp"
    }
适合选择加入编程式编排的工具见下：
  * 可并行运行的工具（相互独立的操作）
  * 可安全重试的操作（幂等）

### 配置工具使用示例以提升参数准确率
精心构造示例，让行为更清晰：
  * 用真实数据（真实的城市名、合理的价格，而非「string」或「value」）
  * 用最简、部分、完整三种填写模式展现多样性
  * 保持精简：每个工具1-5个示例
  * 聚焦歧义（只在正确用法无法从schema一眼看出时才加示例）

## 开始使用
这些功能目前处于beta阶段。要启用它们，加上beta头并包含你需要的工具：
    
    client.beta.messages.create(
        betas=["advanced-tool-use-2025-11-20"],
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        tools=[
            {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
            {"type": "code_execution_20250825", "name": "code_execution"},
            # Your tools with defer_loading, allowed_callers, and input_examples
        ]
    )
详细的API文档与SDK示例，请参见我们的：
  * 工具搜索工具的[文档](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool>)与[代码示例集](<https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/tool_search_with_embeddings.ipynb>)
  * 编程式工具调用的[文档](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling>)与[代码示例集](<https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/programmatic_tool_calling_ptc.ipynb>)
  * 工具使用示例的[文档](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples>)

这些功能把工具使用从简单的函数调用推向智能编排。随着智能体接手横跨数十种工具与大型数据集的更复杂工作流，动态发现、高效执行与可靠调用成了基础能力。
我们很期待看到你构建出的东西。
## 作者与致谢
### 致谢
本文由Bin Wu撰写，Adam Jones、Artur Renault、Henry Tay、Jake Noble、Noah Picard、Sam Jiang以及Claude开发者平台团队亦有贡献。本工作建立在Chris Gorgolewski、Daniel Jiang、Jeremy Fox与Mike Lambert的基础研究之上。我们还从整个AI生态中汲取了灵感，包括[Joel Pobar的LLMVM](<https://github.com/9600dev/llmvm>)、[Cloudflare的Code Mode](<https://blog.cloudflare.com/code-mode/>)以及[把代码执行当作MCP](<https://www.anthropic.com/engineering/code-execution-with-mcp>)。特别感谢Andy Schumeister、Hamish Kerr、Keir Bradwell、Matt Bleifer与Molly Vorwerck的支持。
