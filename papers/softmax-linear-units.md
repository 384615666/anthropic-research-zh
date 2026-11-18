---
title: Softmax Linear Units
url: https://www.anthropic.com/research/softmax-linear-units
date: Jun 17, 2022
category: Interpretability
source: https://www.anthropic.com/research
---

# Softmax Linear Units

- **Date:** 
- **Category:** Interpretability
- **Source:** https://www.anthropic.com/research/softmax-linear-units

---

InterpretabilityResearch
# Softmax Linear Units
Jun 17, 2022
[Read Paper](<https://transformer-circuits.pub/2022/solu/index.html>)
## Abstract
In this paper, we report an architectural change which appears to substantially increase the fraction of MLP neurons which appear to be "interpretable" (i.e. respond to an articulable property of the input), at little to no cost to ML performance. Specifically, we replace the activation function with a softmax linear unit (which we term SoLU) and show that this significantly increases the fraction of neurons in the MLP layers which seem to correspond to readily human-understandable concepts, phrases, or categories on quick investigation, as measured by randomized and blinded experiments. We then study our SoLU models and use them to gain several new insights about how information is processed in transformers. However, we also discover some evidence that the superposition hypothesis is true and there is no free lunch: SoLU may be making some features more interpretable by “hiding” others and thus making them even more deeply uninterpretable. Despite this, SoLU still seems like a net win, as in practical terms it substantially increases the fraction of neurons we are able to understand.  

[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/softmax-linear-units>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/softmax-linear-units>)
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
