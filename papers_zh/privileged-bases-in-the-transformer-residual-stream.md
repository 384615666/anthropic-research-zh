---
title: Privileged Bases in the Transformer Residual Stream
url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
date: Mar 16, 2023
category: Interpretability
source: https://www.anthropic.com/research
---

# Transformer 残差流中的特权基（Privileged Bases）

- **日期：** 
- **分类：** Interpretability（可解释性）
- **来源：** https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream

---

Interpretability（可解释性）研究
2023年3月16日
[阅读论文](<https://transformer-circuits.pub/2023/privileged-basis/index.html>)
## 摘要
我们对 Transformer 架构的数学理论表明，残差流中的单个坐标不应具有特殊意义（也就是说，基方向在某种意义上应该是"任意的"，不比随机方向更可能编码信息）。最近的工作表明，这一观察在实践中是错误的。我们研究了这一现象，并初步得出结论：Adam 优化器中的逐维度归一化器（per-dimension normalizers）是造成这种效应的原因。
  
我们探讨了 Transformer 中基依赖性的另外两个明显来源：层归一化（Layer normalization）和有限精度浮点计算。我们确信地排除了它们作为观察到的基对齐的来源。
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream>)
## 相关内容
### 深入了解 Claude 的数学能力
Claude 的一个未发布研究版本在与黎曼猜想相关的问题上取得了进展。它改进了黎曼 zeta 函数满足该猜想的零点比例的一个长期存在的下界，将其从 41.6% 提高到 67.2%。
[阅读更多](</research/riemann-zeta>)
### 用 Claude 发现密码学弱点
密码学算法。第一次攻击显著削弱了 HAWK——一种为"量子计算机能够破解现有标准"的未来世界而构建的数字签名方案。第二次攻击确定了攻击轮数缩减版 AES（使用最广泛的对称密码）的新方法。
[阅读更多](</research/discovering-cryptographic-weaknesses>)
### Project Pilot：AI 能控制无人机吗？
我们与 Andon Labs 合作，开发了一系列新的评估，以评估 AI 模型使用飞行无人机的能力，最终形成一个新的基准：Drone-Bench。
[阅读更多](</research/project-pilot>)