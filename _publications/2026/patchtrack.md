---
title: "PatchTrack: A Comprehensive Analysis of ChatGPT's Influence on Pull Request Outcomes"
date: 2026-06-01 00:00:00 +0000
selected: true
pub: "Empirical Software Engineering (EMSE)"
pub_post: ", 31(5), 136"
pub_date: "2026"
type: journal
venue_short: "EMSE 2026"
topics: [ai4se]
abstract: >-
  The rapid adoption of large language models (LLMs) like ChatGPT has introduced new dynamics in
  software development, particularly within pull request workflows. While prior research has examined
  the quality of AI-generated code, less is known about how developers evaluate, adapt, and integrate
  these suggestions in real-world collaboration. We analyze 338 pull requests from 255 GitHub
  repositories containing self-admitted ChatGPT usage, comprising 645 AI-generated snippets and 3,486
  developer-authored patches. To support this analysis at scale, we use PatchTrack, an automated
  classifier that identifies whether AI-generated patches were applied, partially reused, or not
  integrated. Our findings reveal that full adoption of ChatGPT-generated code is uncommon: the median
  integration rate is 25%. Qualitative analysis of 89 pull requests with integrated patches reveals
  recurring patterns of structural integration, selective extraction, and iterative refinement,
  indicating that developers typically treat AI output as a starting point rather than a final
  implementation. Even when code is not directly adopted, ChatGPT influences workflows through
  conceptual guidance, documentation, and debugging strategies. Integration decisions reflect
  contextual fit, integration effort, maintainer trust, and established pull request review norms
  rather than serving as direct indicators of code correctness. Overall, this study provides empirical
  insight into AI-mediated decision-making in collaborative software development, showing that the
  influence of generative AI extends beyond patch generation to how developers reason about, adapt,
  and negotiate code during review within pull request workflows. These findings inform the design of
  AI-assisted tools and support more transparent and effective use of LLMs in practice.
authors:
  - Daniel Ogenrwot
  - John Businge
links:
  Paper: https://link.springer.com/article/10.1007/s10664-026-10869-5
  Preprint: https://arxiv.org/abs/2505.07700
  Code: https://github.com/unlv-evol/PatchTrack
cover: /assets/images/covers/patchtrack-overview.png
---
