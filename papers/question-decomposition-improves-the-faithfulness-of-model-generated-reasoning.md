---
title: Question Decomposition Improves the Faithfulness of Model-Generated Reasoning
url: https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning
date: Jul 18, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# Question Decomposition Improves the Faithfulness of Model-Generated Reasoning

- **Date:** 
- **Category:** Alignment
- **Source:** https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning

---

AlignmentResearch
# Question Decomposition Improves the Faithfulness of Model-Generated Reasoning
Jul 18, 2023
[Download Paper](<https://www-cdn.anthropic.com/8154fb1d828cdc390dc1fa442d84034948679c47/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning.pdf>)
## Abstract
As large language models (LLMs) perform more difficult tasks, it becomes harder to verify the correctness and safety of their behavior. One approach to help with this issue is to prompt LLMs to externalize their reasoning, e.g., by having them generate step-by-step reasoning as they answer a question (Chain-of-Thought; CoT). The reasoning may enable us to check the process that models use to perform tasks. However, this approach relies on the stated reasoning faithfully reflecting the model’s actual reasoning, which is not always the case. To improve over the faithfulness of CoT reasoning, we have models generate reasoning by decomposing questions into subquestions. Decomposition-based methods achieve strong performance on question-answering tasks, sometimes approaching that of CoT while improving the faithfulness of the model’s stated reasoning on several recently-proposed metrics. By forcing the model to answer simpler subquestions in separate contexts, we greatly increase the faithfulness of model-generated reasoning over CoT, while still achieving some of the performance gains of CoT. Our results show it is possible to improve the faithfulness of model-generated reasoning; continued improvements may lead to reasoning that enables us to verify the correctness and safety of LLM behavior.
  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning>)
## Related content
### Learning more about Claude's mathematical capabilities
An unreleased research version of Claude has made strides on a problem related to the Riemann hypothesis. It improved a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the hypothesis, increasing it from 41.6% to 67.2%.
[Read more](</research/riemann-zeta>)
### Discovering cryptographic weaknesses with Claude
cryptographic algorithms. The first attack significantly weakens HAWK, a digital signature scheme that was built for a future world where quantum computers are able to break existing standards. The second identifies a new way to attack round-reduced AES, the most widely used symmetric cipher. 
[Read more](</research/discovering-cryptographic-weaknesses>)
### Project Pilot: Can AI control a drone?
Working with Andon Labs, we’ve developed a new series of evaluations that assess AI models’ ability to use a flying drone, culminating in a new benchmark: Drone-Bench.
[Read more](</research/project-pilot>)
