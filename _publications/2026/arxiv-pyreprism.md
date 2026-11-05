---
title: "PyReprism: A Shared Lexical Foundation for Polyglot Code Analysis"
date: 2026-10-29 00:00:00 +0000
selected: false
pub: "arXiv preprint arXiv:2610.39224"
pub_date: "2026"
type: preprint
venue_short: "arXiv 2026"
topics: [ai4se]
abstract: >-
  Empirical studies of polyglot repositories apply the same analyses to every language of a corpus,
  such as separating code from comments, computing metrics, normalizing identifiers, and screening for
  duplicated code. Assembling them from specialized tools introduces differences in language coverage,
  measurement conventions, and workflows. We present PYREPRISM, an open-source Python library and
  command-line tool that separates language-specific lexical processing from reusable analyses: each
  language declares its lexical surface, which yields a lossless stream of typed tokens, and every
  analysis is implemented once on that stream. Across 187 built-in languages, language-specific
  declarations have a median length of 16 lines, and no language overrides a shared analysis. Against
  a reference parser, comment and string classification reach F1 scores of 0.994 and 0.958 on 1,412
  files in 12 languages that were never used to develop the tokenizer. In a study of a polyglot
  repository, one tool replaces three; with matched inputs and analysis operations, it takes 2.9s
  instead of 8.7s on one core. We also characterize where lexical analysis falls short, in complexity
  estimation and clone screening.
authors:
  - Daniel Ogenrwot
  - Jorge Gonzalo Delgado Cervantes
  - Richard Sserunjogi
  - John Businge
links:
  Preprint: https://arxiv.org/abs/2610.39224
  Code: https://github.com/unlv-evol/PyReprism
  Video: https://youtu.be/IXc-NP5t4GU
---
