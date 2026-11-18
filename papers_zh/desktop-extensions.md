---
title: Desktop Extensions:One-click MCP server installation for Claude Desktop
url: https://www.anthropic.com/research/desktop-extensions
date: Jun 26, 2025
category: Engineering
source: https://www.anthropic.com/research
---

# 桌面扩展：为Claude Desktop一键安装MCP服务器

- **日期：** 
- **类别：** 工程（Engineering）
- **来源：** https://www.anthropic.com/research/desktop-extensions

---

工程（Engineering）
2025年6月26日
发布于
    2025年6月26日
团队
    [工程](</engineering>)
主题
    
  * [模型上下文协议](</search?topic=model-context-protocol>)
  * [Claude应用](</search?topic=claude-apps>)
  * [开源](</search?topic=open-source>)
  * [工具使用](</search?topic=tool-use>)
  * [Claude for Enterprise](</search?topic=claude-for-enterprise>)

[](</news/claude-for-creative-work>)[](</news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation>)[](</news/model-context-protocol>)[](</news/mike-krieger-joins-anthropic>)
相关文章
  * 产品
2026年4月28日
[Claude for Creative Work](</news/claude-for-creative-work>)

[查看更多](</search?topic=model-context-protocol>)
  * 2025年9月11日
### 文件扩展名更新
Claude Desktop Extensions现已改用.mcpb（MCP Bundle）文件扩展名，取代.dxt。现有.dxt扩展仍可继续使用，但我们建议开发者今后为新扩展采用.mcpb。所有功能保持不变——这纯粹是一次命名约定更新。

* * *
去年我们发布模型上下文协议（Model Context Protocol，MCP）时，看到开发者构建出各种出色的本地服务器，让Claude得以访问从文件系统到数据库的一切。但我们反复听到同一个反馈：安装太复杂。用户需要开发者工具，得手动编辑配置文件，还常常卡在依赖问题上。
今天，我们推出Desktop Extensions——一种新的打包格式，让安装MCP服务器变得像点一下按钮一样简单。
## 解决MCP安装难题
本地MCP服务器为Claude Desktop用户解锁了强大的能力。它们可以与本地应用交互、访问私有数据、与开发工具集成——同时把数据留在用户的机器上。然而，当前的安装流程设置了重重障碍：
  * **需要开发者工具**：用户需安装Node.js、Python或其他运行时
  * **手动配置**：每个服务器都要编辑JSON配置文件
  * **依赖管理**：用户必须解决包冲突和版本不匹配
  * **缺乏发现机制**：找到有用的MCP服务器得去GitHub上搜索
  * **更新繁琐**：让服务器保持最新版本意味着手动重装

这些摩擦点意味着，MCP服务器尽管功能强大，对非技术用户而言仍基本遥不可及。
## 推出Desktop Extensions
Desktop Extensions（`.mcpb`文件）通过把整个MCP服务器（含全部依赖）打包成单个可安装包，解决了这些问题。对用户而言，变化如下：
**此前：**
    
    # 先安装Node.js
    npm install -g @example/mcp-server
    # 手动编辑~/.claude/claude_desktop_config.json
    # 重启Claude Desktop
    # 祈祷它能跑起来
**此后：**
  1. 下载一个`.mcpb`文件
  2. 双击用Claude Desktop打开
  3. 点击「安装」

就这么简单。无需终端、无需配置文件、无需处理依赖冲突。
## 架构概览
一个Desktop Extension就是一个zip压缩包，内含本地MCP服务器以及一份`manifest.json`，后者描述了Claude Desktop和其他支持桌面扩展的应用所需了解的全部信息。
    
    extension.mcpb（ZIP压缩包）
    ├── manifest.json         # 扩展元数据与配置
    ├── server/               # MCP服务器实现
    │   └── [服务器文件]    
    ├── dependencies/         # 全部所需包／库
    └── icon.png             # 可选：扩展图标
    
    # 示例：Node.js扩展
    extension.mcpb
    ├── manifest.json         # 必需：扩展元数据与配置
    ├── server/               # 服务器文件
    │   └── index.js          # 主入口
    ├── node_modules/         # 打包的依赖
    ├── package.json          # 可选：NPM包定义
    └── icon.png              # 可选：扩展图标
    
    # 示例：Python扩展
    extension.mcpb（ZIP文件）
    ├── manifest.json         # 必需：扩展元数据与配置
    ├── server/               # 服务器文件
    │   ├── main.py           # 主入口
    │   └── utils.py          # 附加模块
    ├── lib/                  # 打包的Python包
    ├── requirements.txt      # 可选：Python依赖清单
    └── icon.png              # 可选：扩展图标
    
Desktop Extension中唯一必需的文件就是manifest.json。Claude Desktop包办了所有复杂环节：
  * **内置运行时**：我们随Claude Desktop一起提供Node.js，免除了外部依赖
  * **自动更新**：有新版本可用时，扩展会自动更新
  * **安全的密钥**：API密钥之类的敏感配置存放在操作系统钥匙串中

清单包含人类可读的信息（如名称、描述或作者）、功能声明（工具、提示词）、用户配置，以及运行时要求。大多数字段都是可选的，因此最小化版本相当简短；不过在实践中，我们预计三种受支持的扩展类型（Node.js、Python，以及传统的二进制文件／可执行程序）都会带上相应文件：
    
    {
      "mcpb_version": "0.1",                    // 本清单所遵循的MCPB规范版本
      "name": "my-extension",                   // 机器可读名称（用于CLI、API）
      "version": "1.0.0",                       // 扩展的语义化版本
      "description": "A simple MCP extension",  // 扩展功能的简要说明
      "author": {                               // 作者信息（必需）
        "name": "Extension Author"              // 作者姓名（必填字段）
      },
      "server": {                               // 服务器配置（必需）
        "type": "node",                         // 服务器类型："node"、"python"或"binary"
        "entry_point": "server/index.js",       // 主服务器文件的路径
        "mcp_config": {                         // MCP服务器配置
          "command": "node",                    // 运行服务器的命令
          "args": [                             // 传给该命令的参数
            "${__dirname}/server/index.js"      // ${__dirname}会被替换为扩展所在目录
          ]                              
        }
      }
    }
    
清单规范中提供了大量[便利选项](<https://github.com/anthropics/dxt/blob/main/MANIFEST.md>)，旨在让本地MCP服务器的安装与配置更轻松。服务器配置对象的定义方式，既能容纳以模板字面量形式给出的用户自定义配置，也能容纳针对特定平台的覆盖项。扩展开发者可以详细定义自己想从用户那里收集哪类配置。
来看一个具体例子，看看清单如何辅助配置。在下面的清单中，开发者声明用户需要提供一个`api_key`。在用户填入该值之前，Claude不会启用这个扩展；它会自动把该值存入操作系统的密钥保险库，并在启动服务器时把`${user_config.api_key}`透明地替换成用户提供的值。类似地，`${__dirname}`会被替换为扩展解压后目录的完整路径。
    
    {
      "mcpb_version": "0.1",
      "name": "my-extension",
      "version": "1.0.0",
      "description": "A simple MCP extension",
      "author": {
        "name": "Extension Author"
      },
      "server": {
        "type": "node",
        "entry_point": "server/index.js",
        "mcp_config": {
          "command": "node",
          "args": ["${__dirname}/server/index.js"],
          "env": {
            "API_KEY": "${user_config.api_key}"
          }
        }
      },
      "user_config": {
        "api_key": {
          "type": "string",
          "title": "API Key",
          "description": "Your API key for authentication",
          "sensitive": true,
          "required": true
        }
      }
    }
一份包含大多数可选字段的完整`manifest.json`可能是这样：
    
    {
      "mcpb_version": "0.1",
      "name": "My MCP Extension",
      "display_name": "My Awesome MCP Extension",
      "version": "1.0.0",
      "description": "A brief description of what this extension does",
      "long_description": "A detailed description that can include multiple paragraphs explaining the extension's functionality, use cases, and features. It supports basic markdown.",
      "author": {
        "name": "Your Name",
        "email": "yourname@example.com",
        "url": "https://your-website.com"
      },
      "repository": {
        "type": "git",
        "url": "https://github.com/your-username/my-mcp-extension"
      },
      "homepage": "https://example.com/my-extension",
      "documentation": "https://docs.example.com/my-extension",
      "support": "https://github.com/your-username/my-extension/issues",
      "icon": "icon.png",
      "screenshots": [
        "assets/screenshots/screenshot1.png",
        "assets/screenshots/screenshot2.png"
      ],
      "server": {
        "type": "node",
        "entry_point": "server/index.js",
        "mcp_config": {
          "command": "node",
          "args": ["${__dirname}/server/index.js"],
          "env": {
            "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
          }
        }
      },
      "tools": [
        {
          "name": "search_files",
          "description": "Search for files in a directory"
        }
      ],
      "prompts": [
        {
          "name": "poetry",
          "description": "Have the LLM write poetry",
          "arguments": ["topic"],
          "text": "Write a creative poem about the following topic: ${arguments.topic}"
        }
      ],
      "tools_generated": true,
      "keywords": ["api", "automation", "productivity"],
      "license": "MIT",
      "compatibility": {
        "claude_desktop": ">=1.0.0",
        "platforms": ["darwin", "win32", "linux"],
        "runtimes": {
          "node": ">=16.0.0"
        }
      },
      "user_config": {
        "allowed_directories": {
          "type": "directory",
          "title": "Allowed Directories",
          "description": "Directories the server can access",
          "multiple": true,
          "required": true,
          "default": ["${HOME}/Desktop"]
        },
        "api_key": {
          "type": "string",
          "title": "API Key",
          "description": "Your API key for authentication",
          "sensitive": true,
          "required": false
        },
        "max_file_size": {
          "type": "number",
          "title": "Maximum File Size (MB)",
          "description": "Maximum file size to process",
          "default": 10,
          "min": 1,
          "max": 100
        }
      }
    }
要查看扩展示例和清单，请参阅[MCPB仓库中的示例](<https://github.com/anthropics/dxt/tree/main/examples>)。
`manifest.json`中所有必需与可选字段的完整规范，可在我们的[开源工具链](<https://github.com/anthropics/dxt/blob/main/MANIFEST.md>)中找到。
## 构建你的第一个扩展
下面走一遍把现有MCP服务器打包成Desktop Extension的流程。我们以一个简单的文件系统服务器为例。
### 第1步：创建清单
首先，为你的服务器初始化一份清单：
    
    npx @anthropic-ai/mcpb init
这个交互式工具会询问你服务器的相关信息，并生成一份完整的manifest.json。若想一步到位得到最基础的manifest.json，可以在命令后加上--yes参数。
### 第2步：处理用户配置
如果你的服务器需要用户输入（如API密钥或允许的目录），就在清单中声明：
    
    "user_config": {
      "allowed_directories": {
        "type": "directory",
        "title": "Allowed Directories",
        "description": "Directories the server can access",
        "multiple": true,
        "required": true,
        "default": ["${HOME}/Documents"]
      }
    }
Claude Desktop会：
  * 显示用户友好的配置界面
  * 在启用扩展前校验输入
  * 安全地存储敏感值
  * 按开发者的配置，以参数或环境变量的形式把配置传给你的服务器

在下面的示例中，我们把用户配置作为环境变量传入，但它也可以是一个参数。
    
    "server": {
       "type": "node",
       "entry_point": "server/index.js",
       "mcp_config": {
       "command": "node",
       "args": ["${__dirname}/server/index.js"],
       "env": {
          "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
       }
       }
    }
### 第3步：打包扩展
把一切打包进一个`.mcpb`文件：
    
    npx @anthropic-ai/mcpb pack
该命令会：
  1. 校验你的清单
  2. 生成`.mcpb`压缩包

### 第4步：本地测试
把`.mcpb`文件拖进Claude Desktop的设置窗口。你会看到：
  * 关于扩展的人类可读信息
  * 所需的权限与配置
  * 一个简单的「安装」按钮

## 高级特性
### 跨平台支持
扩展可以适配不同的操作系统：
    
    "server": {
      "type": "node",
      "entry_point": "server/index.js",
      "mcp_config": {
        "command": "node",
        "args": ["${__dirname}/server/index.js"],
        "platforms": {
          "win32": {
            "command": "node.exe",
            "env": {
              "TEMP_DIR": "${TEMP}"
            }
          },
          "darwin": {
            "env": {
              "TEMP_DIR": "${TMPDIR}"
            }
          }
        }
      }
    }
### 动态配置
用模板字面量表示运行时取值：
  * `${__dirname}`：扩展的安装目录
  * `${user_config.key}`：用户提供的配置
  * `${HOME}, ${TEMP}`：系统环境变量

### 功能声明
让用户事先了解扩展的能力：
    
    "tools": [
      {
        "name": "read_file",
        "description": "Read contents of a file"
      }
    ],
    "prompts": [
      {
        "name": "code_review",
        "description": "Review code for best practices",
        "arguments": ["file_path"]
      }
    ]
## 扩展目录
发布时，Claude Desktop内置了一个经过策划的扩展目录。用户可以浏览、搜索并一键安装——无需去GitHub翻找，也无需审查代码。
尽管我们预计Desktop Extension规范以及Claude在macOS和Windows上的实现都会随时间演进，但我们期待看到扩展以各种富有创意的方式被用来拓展Claude的能力。
要提交你的扩展：
  1. 确保它遵循提交表单中的指南
  2. 在Windows和macOS上都做测试
  3. [提交你的扩展](<https://docs.google.com/forms/d/14_Dmcig4z8NeRMB_e7TOyrKzuZ88-BLYdLvS6LPhiZU/edit>)
  4. 我们的团队会审核质量与安全性

## 构建开放生态
我们致力于MCP服务器周边的开放生态，并相信它能被众多应用和服务普遍采用，这已让整个社区受益。秉持这一承诺，我们正在开源Desktop Extension规范、工具链，以及Claude在macOS和Windows上用于实现自身Desktop Extensions支持的schema和关键函数。我们希望MCPB格式不仅能让本地MCP服务器对Claude更可移植，也能惠及其他AI桌面应用。
我们开源的内容包括：
  * 完整的MCPB规范
  * 打包与校验工具
  * 参考实现代码
  * TypeScript类型与schema

这意味着：
  * **对MCP服务器开发者**：打包一次，即可在任何支持MCPB的地方运行
  * **对应用开发者**：无需从零搭建就能加入扩展支持
  * **对用户**：在所有支持MCP的应用中获得一致体验

规范和工具链特意定为0.1版，因为我们期待与更广泛的社区一起演进和改动这一格式。期待听到你的声音。
## 安全与企业考量
我们清楚扩展会带来新的安全考量，对企业尤其如此。在Desktop Extensions的预览版中，我们内置了若干防护措施：
### 面向用户
  * 敏感数据留在操作系统钥匙串中
  * 自动更新
  * 可审计已安装的扩展

### 面向企业
  * 支持组策略（Windows）和MDM（macOS）
  * 可预装经过审批的扩展
  * 可将特定扩展或发布者列入黑名单
  * 可完全禁用扩展目录
  * 可部署私有扩展目录

关于如何在组织内管理扩展的更多信息，请参阅我们的[文档](<https://support.anthropic.com/en/articles/10949351-getting-started-with-model-context-protocol-mcp-on-claude-for-desktop>)。
## 开始使用
准备好构建自己的扩展了吗？可以这样开始：
**对MCP服务器开发者**：查阅我们的[开发者文档](<https://github.com/anthropics/dxt>)——或者直接在本地MCP服务器目录下运行以下命令立刻上手：
    
    npm install -g @anthropic-ai/mcpb
    mcpb init
    mcpb pack
**对Claude Desktop用户**：更新到最新版本，在设置中找到「扩展」板块
**对企业**：查阅我们的企业文档了解部署选项
## 用Claude Code构建
在Anthropic内部，我们发现Claude极擅长在极少干预下构建扩展。如果你也想用Claude Code，我们建议先简要说明你希望扩展做什么，再把下面这段上下文加进提示词：
    
```
    I want to build this as a Desktop Extension, abbreviated as "MCPB". Please follow these steps:
    
    1. **Read the specifications thoroughly:**
       - https://github.com/anthropics/mcpb/blob/main/README.md - MCPB architecture overview, capabilities, and integration patterns
       - https://github.com/anthropics/mcpb/blob/main/MANIFEST.md - Complete extension manifest structure and field definitions
       - https://github.com/anthropics/mcpb/tree/main/examples - Reference implementations including a "Hello World" example
    
    2. **Create a proper extension structure:**
       - Generate a valid manifest.json following the MANIFEST.md spec
       - Implement an MCP server using @modelcontextprotocol/sdk with proper tool definitions
       - Include proper error handling and timeout management
    
    3. **Follow best development practices:**
       - Implement proper MCP protocol communication via stdio transport
       - Structure tools with clear schemas, validation, and consistent JSON responses
       - Make use of the fact that this extension will be running locally
       - Add appropriate logging and debugging capabilities
       - Include proper documentation and setup instructions
    
    4. **Test considerations:**
       - Validate that all tool calls return properly structured responses
       - Verify manifest loads correctly and host integration works
    
    Generate complete, production-ready code that can be immediately tested. Focus on defensive programming, clear error messages, and following the exact
    MCPB specifications to ensure compatibility with the ecosystem.
```
## 结论
Desktop Extensions代表着用户与本地AI工具交互方式的根本转变。通过消除安装摩擦，我们让强大的MCP服务器对每个人都触手可及——而不只是开发者。
在内部，我们用桌面扩展来分享高度实验性的MCP服务器——有的好玩，有的实用。有个团队做了实验，想看看我们的模型在直接连上GameBoy时能走多远，类似于我们的[「Claude plays Pokémon」研究](<https://www.anthropic.com/news/visible-extended-thinking>)。我们用Desktop Extensions打包了一个扩展，它打开流行的[PyBoy](<https://github.com/Baekalfen/PyBoy>) GameBoy模拟器，并让Claude接管。我们相信，把模型的能力与用户本地机器上现成的工具、数据和应用连接起来，蕴藏着无数机会。
![一台桌面显示PyBoy MCP与Super Mario Land起始画面](assets/desktop-extensions/img_000.webp)
我们迫不及待想看到你做出什么。曾为我们带来数千个MCP服务器的那份创造力，如今只需一次点击就能触达数百万用户。准备好分享你的MCP服务器了吗？[提交你的扩展以供审核](<https://forms.gle/tyiAZvch1kDADKoP9>)。
![想了解更多？](assets/desktop-extensions/img_001.svg)
### 想了解更多？
[探索课程](<https://anthropic.skilljar.com/>)
