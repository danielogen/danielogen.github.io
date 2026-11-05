---
title: "Refactoring-Aware Patch Integration Across Structurally Divergent Java Forks"
date: 2025-10-01 00:00:00 +0000
selected: true
pub: "2025 IEEE International Conference on Source Code Analysis & Manipulation (SCAM)"
pub_date: "2025"
type: conference
venue_short: "SCAM 2025"
topics: [patch]
award: Distinguished Artifact Award
abstract: >-
  While most forks on platforms like GitHub are short-lived and used for social collaboration, a
  smaller but impactful subset evolve into long-lived forks, referred to here as variants, that
  maintain independent development trajectories. Integrating bug-fix patches across such divergent
  variants poses challenges due to structural drift, including refactorings that rename, relocate, or
  reorganize code elements and obscure semantic correspondence. This paper presents an empirical study
  of patch integration failures in 14 divergent pair of variants and introduces RePatch, a
  refactoring-aware integration system for Java repositories. RePatch extends the RefMerge framework,
  originally designed for symmetric merges, by supporting asymmetric patch transfer. RePatch inverts
  refactorings in both the source and target to realign the patch context, applies the patch, and
  replays the transformations to preserve the intent of the variant. In our evaluation of 478 bug-fix
  pull requests, Git cherry-pick fails in 64.4% of cases due to structural misalignments, while
  RePatch successfully integrates 52.8% of the previously failing patches. These results highlight the
  limitations of syntax-based tools and the need for semantic reasoning in variant-aware patch
  propagation.
authors:
  - Daniel Ogenrwot
  - John Businge
links:
  Paper: https://ieeexplore.ieee.org/document/11190222
  Code: https://github.com/unlv-evol/RePatch
cover: /assets/images/covers/repatch-divergence.png
---
