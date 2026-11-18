---
title: Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
url: https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training
date: Jan 14, 2024
category: Alignment
source: https://www.anthropic.com/research
---

# Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training

- **Date:** 
- **Category:** Alignment
- **Source:** https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training

---

AlignmentResearch
# Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
Jan 14, 2024
[Read Paper](<https://arxiv.org/abs/2401.05566>)
Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs). For example, we train models that write secure code when the prompt states that the year is 2023, but insert exploitable code when the stated year is 2024. We find that such backdoor behavior can be made persistent, so that it is not removed by standard safety training techniques, including supervised fine-tuning, reinforcement learning, and adversarial training (eliciting unsafe behavior and then training to remove it). The backdoor behavior is most persistent in the largest models and in models trained to produce chain-of-thought reasoning about deceiving the training process, with the persistence remaining even when the chain-of-thought is distilled away. Furthermore, rather than removing backdoors, we find that adversarial training can teach models to better recognize their backdoor triggers, effectively hiding the unsafe behavior. Our results suggest that, once a model exhibits deceptive behavior, standard techniques could fail to remove such deception and create a false impression of safety.
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training>)
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
