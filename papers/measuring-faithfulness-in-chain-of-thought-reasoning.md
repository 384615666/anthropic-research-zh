---
title: Measuring Faithfulness in Chain-of-Thought Reasoning
url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
date: Jul 18, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# Measuring Faithfulness in Chain-of-Thought Reasoning

- **Date:** 
- **Category:** Alignment
- **Source:** https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning

---

AlignmentResearch
# Measuring Faithfulness in Chain-of-Thought Reasoning
Jul 18, 2023
[Download Paper](<https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf>)
## Abstract
Large language models (LLMs) perform better when they produce step-by-step, “Chain-ofThought” (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model’s actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT’s performance boost does not seem to come from CoT’s added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.
  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning>)
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
