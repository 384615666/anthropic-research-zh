---
title: Constitutional AI: Harmlessness from AI Feedback
url: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
date: Dec 15, 2022
category: Alignment
source: https://www.anthropic.com/research
---

# Constitutional AI: Harmlessness from AI Feedback

- **Date:** 
- **Category:** Alignment
- **Source:** https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

---

AlignmentResearch
# Constitutional AI: Harmlessness from AI Feedback
Dec 15, 2022
[Read Paper](<https://arxiv.org/abs/2212.08073>)
## Abstract
As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.
## Policy Memo
[Constitutional AI Policy Memo](<https://www-cdn.anthropic.com/7512771452629584566b6303311496c262da1006/Anthropic_ConstitutionalAI_v2.pdf>)
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback>)
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
