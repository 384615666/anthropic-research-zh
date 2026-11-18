---
title: Privileged Bases in the Transformer Residual Stream
url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
date: Mar 16, 2023
category: Interpretability
source: https://www.anthropic.com/research
---

# Privileged Bases in the Transformer Residual Stream

- **Date:** 
- **Category:** Interpretability
- **Source:** https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream

---

InterpretabilityResearch
# Privileged Bases in the Transformer Residual Stream
Mar 16, 2023
[Read Paper](<https://transformer-circuits.pub/2023/privileged-basis/index.html>)
## Abstract
Our mathematical theories of the Transformer architecture suggest that individual coordinates in the residual stream should have no special significance (that is, the basis directions should be in some sense "arbitrary" and no more likely to encode information than random directions). Recent work has shown that this observation is false in practice. We investigate this phenomenon and provisionally conclude that the per-dimension normalizers in the Adam optimizer are to blame for the effect.  
  
We explore two other obvious sources of basis dependency in a Transformer: Layer normalization, and finite-precision floating-point calculations. We confidently rule these out as being the source of the observed basis-alignment.
[](<https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream>)[](<https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream>)
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
