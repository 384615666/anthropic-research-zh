---
title: Code execution with MCP:Building more efficient agents
url: https://www.anthropic.com/research/code-execution-with-mcp
date: Nov 4, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# 用 MCP 执行代码：构建更高效的智能体

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/code-execution-with-mcp

---

工程（Engineering）
2025 年 11 月 4 日
![用 MCP 执行代码：构建更高效的智能体](assets/code-execution-with-mcp/img_000.webp)
已发布
    2025 年 11 月 4 日
团队
    [工程](</engineering>)
主题
    
  * [模型上下文协议](</search?topic=model-context-protocol>)
  * [上下文工程](</search?topic=context-engineering>)
  * [智能体](</search?topic=agents>)
  * [工具使用](</search?topic=tool-use>)
  * [编程](</search?topic=coding>)

[](</research/advanced-tool-use>)[](</research/effective-context-engineering-for-ai-agents>)[](</research/writing-tools-for-agents>)[](</research/claude-code-best-practices>)
相关文章
  * 工程
2025 年 11 月 24 日
[在 Claude 开发者平台上推出高级工具使用](</research/advanced-tool-use>)

[阅读更多](</search?topic=model-context-protocol>)
[模型上下文协议（Model Context Protocol，MCP）](<https://modelcontextprotocol.io/>) 是把 AI 智能体连接到外部系统的开放标准。传统上，把智能体接到工具和数据的每一种组合，都需要定制集成，由此产生碎片化和重复劳动，使真正互联的系统难以规模化。MCP 提供了通用协议——开发者在智能体里实现一次 MCP，就能解锁整个集成生态。
自 2024 年 11 月发布 MCP 以来，采用速度很快：社区已构建出数千个 [MCP 服务器](<https://github.com/modelcontextprotocol/servers>)，所有主流编程语言都有 [SDK](<https://modelcontextprotocol.io/docs/sdk>) 可用，业界也已把 MCP 当作连接智能体与工具、数据的事实标准。
如今开发者常常构建这样的智能体：跨数十个 MCP 服务器，能访问数百乃至数千种工具。但随着接入的工具越来越多，预先加载全部工具定义、并让中间结果穿过上下文窗口，会拖慢智能体、推高成本。
在这篇博客里，我们会探讨代码执行如何让智能体更高效地与 MCP 服务器交互——用更少的 token 处理更多的工具。
## 工具带来的过量 token 消耗拖累智能体效率
随着 MCP 使用规模扩大，有两种常见模式会推高智能体的成本和延迟：
  1. 工具定义塞满上下文窗口；
  2. 中间工具结果消耗额外 token。

### 1\. 工具定义塞满上下文窗口
大多数 MCP 客户端会把所有工具定义预先直接加载进上下文，用直接工具调用的语法暴露给模型。这些工具定义大概长这样：
    
    gdrive.getDocument
         Description: Retrieves a document from Google Drive
         Parameters:
                    documentId (required, string): The ID of the document to retrieve
                    fields (optional, string): Specific fields to return
         Returns: Document object with title, body content, metadata, permissions, etc.
    
    salesforce.updateRecord
        Description: Updates a record in Salesforce
        Parameters:
                   objectType (required, string): Type of Salesforce object (Lead, Contact,      Account, etc.)
                   recordId (required, string): The ID of the record to update
                   data (required, object): Fields to update with their new values
         Returns: Updated record object with confirmation
工具描述占用更多上下文窗口空间，拉长响应时间、抬高成本。当智能体接入数千种工具时，它们在读到请求之前就得先处理几十万 token。
### 2\. 中间工具结果消耗额外 token
大多数 MCP 客户端允许模型直接调用 MCP 工具。例如，你可能会让智能体：「把我的会议记录从 Google Drive 下载下来，附到 Salesforce 的潜在客户记录上。」
模型会发出这样的调用：
    
    TOOL CALL: gdrive.getDocument(documentId: "abc123")
            → returns "Discussed Q4 goals...\n[full transcript text]"
               (loaded into model context)
    
    TOOL CALL: salesforce.updateRecord(
    			objectType: "SalesMeeting",
    			recordId: "00Q5f000001abcXYZ",
      			data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
    		)
    		(model needs to write entire transcript into context again)
每个中间结果都必须穿过模型。在这个例子里，完整的通话记录文本流转了两遍。对一场 2 小时的销售会议来说，这可能意味着额外处理 50,000 个 token。更大的文档甚至可能超出上下文窗口上限，让整个流程中断。
面对大型文档或复杂数据结构，模型在工具调用之间搬运数据时更容易出错。
![MCP 客户端如何与 MCP 服务器及 LLM 协同工作的示意图。](assets/code-execution-with-mcp/img_001.png)
MCP 客户端把工具定义加载进模型的上下文窗口，并编排一个消息循环：每次工具调用及其结果都要在各操作之间穿过模型。
## 用 MCP 执行代码提升上下文效率
随着代码执行环境在智能体中越来越普遍，一种解决办法是把 MCP 服务器呈现为代码 API，而非直接的工具调用。智能体于是可以写代码与 MCP 服务器交互。这种做法同时应对了两个难题：智能体只加载自己需要的工具，并且在把结果交回模型之前，先在执行环境里处理数据。
实现办法有多种。一种是从已连接的 MCP 服务器生成一棵包含所有可用工具的文件树。下面是用 TypeScript 的实现：
    
    servers
    ├── google-drive
    │   ├── getDocument.ts
    │   ├── ... (other tools)
    │   └── index.ts
    ├── salesforce
    │   ├── updateRecord.ts
    │   ├── ... (other tools)
    │   └── index.ts
    └── ... (other servers)
然后每个工具对应一个文件，类似这样：
    
    // ./servers/google-drive/getDocument.ts
    import { callMCPTool } from "../../../client.js";
    
    interface GetDocumentInput {
      documentId: string;
    }
    
    interface GetDocumentResponse {
      content: string;
    }
    
    /* Read a document from Google Drive */
    export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
      return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
    }
    
上面那个 Google Drive 到 Salesforce 的例子，就变成了这样的代码：
    
    // Read transcript from Google Docs and add to Salesforce prospect
    import * as gdrive from './servers/google-drive';
    import * as salesforce from './servers/salesforce';
    
    const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
    await salesforce.updateRecord({
      objectType: 'SalesMeeting',
      recordId: '00Q5f000001abcXYZ',
      data: { Notes: transcript }
    });
    
智能体通过探索文件系统来发现工具：列出 `./servers/ ` 目录，找到可用的服务器（如 `google-drive` 和 `salesforce`），再读取它需要的具体工具文件（如 `getDocument.ts` 和 `updateRecord.ts`），以弄清每个工具的接口。这让智能体只加载当前任务所需的定义。token 用量因此从 150,000 个降到 2,000 个——时间和成本节省了 98.7%**。**
Cloudflare [发表了类似的发现](<https://blog.cloudflare.com/code-mode/>)，把「用 MCP 执行代码」称为「Code Mode」。核心洞见是一样的：LLM 擅长写代码，开发者应当利用这一长处，构建能更高效地与 MCP 服务器交互的智能体。
## 用 MCP 执行代码的好处
用 MCP 执行代码，让智能体通过按需加载工具、在数据到达模型前先做过滤、以及在单步内执行复杂逻辑，更高效地使用上下文。这种做法还带来安全和状态管理方面的好处。
### 渐进式披露
模型很擅长在文件系统中导航。把工具以代码形式放在文件系统上，模型就能按需读取工具定义，而不必一上来就全部读完。
另一种做法是给服务器加一个 `search_tools` 工具来查找相关定义。例如，在使用上文假想的 Salesforce 服务器时，智能体搜索「salesforce」，只加载当前任务需要的那些工具。在 `search_tools` 工具里加一个「详细程度」参数，让智能体选择所需的细节层级（比如只有名称、名称加描述，或带 schema 的完整定义），同样能帮助智能体节省上下文、高效地找到工具。
### 上下文高效的工具结果
处理大型数据集时，智能体可以在代码里先过滤、转换结果，再返回。设想读取一张 10,000 行的电子表格：
    
    // Without code execution - all rows flow through context
    TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
            → returns 10,000 rows in context to filter manually
    
    // With code execution - filter in the execution environment
    const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
    const pendingOrders = allRows.filter(row => 
      row["Status"] === 'pending'
    );
    console.log(`Found ${pendingOrders.length} pending orders`);
    console.log(pendingOrders.slice(0, 5)); // Only log first 5 for review
智能体看到的是五行，而不是 10,000 行。同样的模式也适用于聚合、跨多个数据源的连接，或抽取特定字段——全都不会把上下文窗口撑大。
#### 更强大、更省上下文的控制流
循环、条件判断和错误处理都可以用熟悉的代码模式完成，而不必把一次次工具调用串起来。例如，如果你需要 Slack 里的部署通知，智能体可以写：
    
    let found = false;
    while (!found) {
      const messages = await slack.getChannelHistory({ channel: 'C123456' });
      found = messages.some(m => m.text.includes('deployment complete'));
      if (!found) await new Promise(r => setTimeout(r, 5000));
    }
    console.log('Deployment notification received');
这种做法比在智能体循环里来回交替 MCP 工具调用和 sleep 命令更高效。
此外，能写出一棵真正会被执行的条件树，还能节省「首 token 时间」延迟：智能体不必等模型去判断一个 if 语句，而可以让代码执行环境代劳。
### 保护隐私的操作
当智能体用 MCP 执行代码时，中间结果默认留在执行环境里。这样一来，智能体只看到你显式记录或返回的内容，意味着你不愿与模型共享的数据可以流过工作流，却始终不进入模型的上下文。
对更敏感的工作负载，智能体脚手架可以自动把敏感数据标记化。例如，假设你要把电子表格里的客户联系方式导入 Salesforce，智能体会写：
    
    const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
    for (const row of sheet.rows) {
      await salesforce.updateRecord({
        objectType: 'Lead',
        recordId: row.salesforceId,
        data: { 
          Email: row.email,
          Phone: row.phone,
          Name: row.name
        }
      });
    }
    console.log(`Updated ${sheet.rows.length} leads`);
MCP 客户端会拦截数据，在它到达模型之前把 PII 标记化：
    
    // What the agent would see, if it logged the sheet.rows:
    [
      { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
      { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
      ...
    ]
之后，当数据在另一次 MCP 工具调用中被共享时，MCP 客户端会通过查表把它还原。真实的邮箱地址、电话号码和姓名从 Google Sheets 流向 Salesforce，却绝不经过模型。这能防止智能体意外记录或处理敏感数据。你也可以用它来定义确定性的安全规则，指定数据可以流向哪里、从哪里来。
### 状态持久化与技能
带文件系统访问的代码执行，让智能体能跨操作保持状态。智能体可以把中间结果写入文件，从而续接工作、跟踪进度：
    
    const leads = await salesforce.query({ 
      query: 'SELECT Id, Email FROM Lead LIMIT 1000' 
    });
    const csvData = leads.map(l => `${l.Id},${l.Email}`).join('\n');
    await fs.writeFile('./workspace/leads.csv', csvData);
    
    // Later execution picks up where it left off
    const saved = await fs.readFile('./workspace/leads.csv', 'utf-8');
智能体还能把自己的代码持久化为可复用的函数。一旦为某个任务写出了可用的代码，就可以把这份实现存下来供日后使用：
    
    // In ./skills/save-sheet-as-csv.ts
    import * as gdrive from './servers/google-drive';
    export async function saveSheetAsCsv(sheetId: string) {
      const data = await gdrive.getSheet({ sheetId });
      const csv = data.map(row => row.join(',')).join('\n');
      await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
      return `./workspace/sheet-${sheetId}.csv`;
    }
    
    // Later, in any agent execution:
    import { saveSheetAsCsv } from './skills/save-sheet-as-csv';
    const csvPath = await saveSheetAsCsv('abc123');
这与[技能（Skills）](<https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>)的概念紧密相关：技能是一些装着可复用指令、脚本和资源的文件夹，用来提升模型在专门任务上的表现。给这些保存下来的函数加一个 SKILL.md 文件，就形成了一个结构化技能，模型可以引用和使用。久而久之，这让你的智能体能积累一套高层能力的工具箱，逐步演化出它最高效工作所需的脚手架。
请注意，代码执行也带来自身的复杂性。运行智能体生成的代码，需要一个安全的执行环境，配有适当的[沙箱](<https://www.anthropic.com/engineering/claude-code-sandboxing>)、资源限制和监控。这些基础设施要求带来了直接工具调用所没有的运维开销和安全考量。应当把代码执行的好处——更低的 token 成本、更低的延迟、更好的工具组合——与这些实现成本放在一起权衡。
## 总结
MCP 为智能体连接众多工具和系统提供了基础协议。然而，一旦接入的服务器过多，工具定义和结果就会消耗过量 token，拉低智能体效率。
虽然这里许多问题看上去很新——上下文管理、工具组合、状态持久化——但软件工程里早有已知的解法。代码执行把这些成熟模式用到智能体上，让它们用熟悉的编程结构与 MCP 服务器更高效地交互。如果你实现了这种做法，我们鼓励你把发现分享给 [MCP 社区](<https://modelcontextprotocol.io/community/communication>)。
## 作者与致谢
### 致谢
本文由 Adam Jones 和 Conor Kelly 撰写。感谢 Jeremy Fox、Jerome Swannack、Stuart Ritchie、Molly Vorwerck、Matt Samuels 和 Maggie Vo 对本文草稿提供反馈。
