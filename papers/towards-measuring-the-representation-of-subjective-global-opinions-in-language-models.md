---
title: Towards Measuring the Representation of Subjective Global Opinions in Language Models
url: https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models
date: Jun 29, 2023
category: Societal Impacts
source: https://www.anthropic.com/research
---

# Towards Measuring the Representation of Subjective Global Opinions in Language Models

- **Date:** 
- **Category:** Societal Impacts
- **Source:** https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models

---

Societal Impacts
# Towards Measuring the Representation of Subjective Global Opinions in Language Models
Jun 29, 2023
[Read Paper](<https://arxiv.org/abs/2306.16388>)
## Abstract
Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries. Next, we define a metric that quantifies the similarity between LLM-generated survey responses and human responses, conditioned on country. With our framework, we run three experiments on an LLM trained to be helpful, honest, and harmless with Constitutional AI. By default, LLM responses tend to be more similar to the opinions of certain populations, such as those from the USA, and some European and South American countries, highlighting the potential for biases. When we prompt the model to consider a particular country's perspective, responses shift to be more similar to the opinions of the prompted populations, but can reflect harmful cultural stereotypes. When we translate GlobalOpinionQA questions to a target language, the model's responses do not necessarily become the most similar to the opinions of speakers of those languages. We release our dataset for others to use and build on. Our data is at [this URL](<https://huggingface.co/datasets/Anthropic/llm_global_opinions>). We also provide an interactive visualization at [this URL](<https://llmglobalvalues.anthropic.com/>).
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models>)
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
