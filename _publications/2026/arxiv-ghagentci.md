---
title: "GHAgentCI: A Dataset of Coding-Agent Invocations in CI Workflow Histories"
date: 2026-11-11 00:00:00 +0000
selected: false
pub: "arXiv preprint arXiv:2611.15522"
pub_date: "2026"
type: preprint
venue_short: "arXiv 2026"
topics: [ai4se]
abstract: >-
  Coding agents are increasingly integrated into GitHub Actions to review pull requests, triage issues
  and modify code. Identifying these integrations is challenging because agentic workflows often resemble
  ordinary CI files, with evidence appearing in action references, shell commands and workflow conventions.
  We present GHAgentCI, a dataset of 15K+ workflow histories from 6K+ of 196K+ mined GitHub repositories,
  comprising 159K+ revisions and 205K+ agent-evidence records linked to workflow triggers and declared
  execution constraints. Our open-source extractor, cai-miner, detects agent-related evidence using an
  extensible catalogue. Manual validation of 576 stratified records confirmed 96.1% of dedicated-action
  matches and 98.8% of GitHub Agentic Workflow matches, with lower rates for other evidence kinds.
  Exploratory analyses reveal a shift toward command-line and GitHub Agentic Workflow integrations,
  differences in declared safeguards, and frequent removal of detected agentic workflows. GHAgentCI
  supports longitudinal studies of coding-agent integration into CI.
authors:
  - Daniel Ogenrwot
  - Jorge Gonzalo Delgado Cervantes
  - Woojoong Kim
  - John Businge
links:
  Preprint: https://arxiv.org/abs/2611.15522
  PDF: https://arxiv.org/pdf/2611.15522
---
