---
title: Studying Large Language Model Generalization with Influence Functions
url: https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions
date: Aug 8, 2023
category: Alignment
source: https://www.anthropic.com/research
---

# Studying Large Language Model Generalization with Influence Functions

- **Date:** 
- **Category:** Alignment
- **Source:** https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions

---

AlignmentResearch
# Studying Large Language Model Generalization with Influence Functions
Aug 8, 2023
[Read Paper](<https://arxiv.org/abs/2308.03296>)
## Abstract
When trying to gain better visibility into a machine learning model in order to understand and mitigate the associated risks, a potentially valuable source of evidence is: which training examples most contribute to a given behavior? Influence functions aim to answer a counterfactual: how would the model's parameters (and hence its outputs) change if a given sequence were added to the training set? While influence functions have produced insights for small models, they are difficult to scale to large language models (LLMs) due to the difficulty of computing an inverse-Hessian-vector product (IHVP). We use the Eigenvalue-corrected Kronecker-Factored Approximate Curvature (EK-FAC) approximation to scale influence functions up to LLMs with up to 52 billion parameters. In our experiments, EK-FAC achieves similar accuracy to traditional influence function estimators despite the IHVP computation being orders of magnitude faster. We investigate two algorithmic techniques to reduce the cost of computing gradients of candidate training sequences: TF-IDF filtering and query batching. We use influence functions to investigate the generalization patterns of LLMs, including the sparsity of the influence patterns, increasing abstraction with scale, math and programming abilities, cross-lingual generalization, and role-playing behavior. Despite many apparently sophisticated forms of generalization, we identify a surprising limitation: influences decay to near-zero when the order of key phrases is flipped. Overall, influence functions give us a powerful new tool for studying the generalization properties of LLMs.
  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions>)
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
