---
layout: blog_post
title: "Introduction to Large Language Models for Software Engineering"
date: 2026-05-07
tags:
  - LLMs
  - Software Engineering
  - AI4SE
  - Empirical SE
---

Large Language Models (LLMs) have rapidly moved from research curiosity to everyday tooling in software development. Tools like GitHub Copilot, Cursor, and ChatGPT are already embedded in millions of developers' workflows — yet many practitioners and researchers are still grappling with a fundamental question: *what can these models actually do for software engineering, and where do they fall short?*

This post offers a grounded introduction to LLMs in the context of Software Engineering (SE): what they are, how they are applied, what the empirical evidence says, and what open problems remain.

# What is a Large Language Model?

A Large Language Model is a neural network trained on vast corpora of text — including source code from public repositories like GitHub — to predict the next token in a sequence. Through this deceptively simple objective, models such as GPT-4, Claude, Llama, and CodeLlama develop emergent capabilities: they can generate syntactically correct code, explain logic, translate between programming languages, and reason about software artifacts.

At their core, LLMs are **probabilistic text generators**. They do not "understand" code in the way a compiler does; they model statistical patterns over tokens. This distinction matters enormously when reasoning about their reliability in SE tasks.

## Key architectural ideas

Modern LLMs share a few common properties relevant to SE use:

- **Scale**: billions of parameters trained on trillions of tokens, including large fractions of public code (The Stack, CodeSearchNet, etc.)
- **In-context learning**: the ability to adapt behavior from examples provided in the prompt, without weight updates
- **Instruction tuning**: fine-tuning on (instruction, response) pairs to make models follow natural-language directives
- **Retrieval Augmented Generation (RAG)**: grounding model outputs in retrieved documents — especially useful for codebase-aware assistants

# LLMs Across the Software Engineering Lifecycle

LLMs are not a single tool for a single task. They cut across nearly every phase of the SE lifecycle.

## Code generation

The most visible application. Given a natural-language description — or a partial code context — LLMs generate code completions or full implementations.

```python
# Prompt: Write a function to check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

Empirical studies show that LLMs achieve high pass rates on competitive programming benchmarks (HumanEval, MBPP), but performance degrades sharply on real-world tasks requiring deep repository context, uncommon APIs, or security awareness.

## Automated program repair

Automated Program Repair (APR) aims to fix bugs without human intervention. LLMs have become dominant here, surpassing prior template-based and search-based approaches on benchmarks like Defects4J. The intuition is straightforward: a model trained on millions of commit diffs has seen many patterns of "broken code → fixed code."

My own work — [RePatch](https://ieeexplore.ieee.org/document/11190222) — explores a related challenge: **patch integration across structurally divergent forks**. When two software variants have drifted apart through independent refactoring, simply replaying a patch fails. We showed that refactoring-aware strategies can recover 52.8% of previously failing patches, a problem where LLMs alone struggle due to the structural mismatch.

## Code review and pull request analysis

LLMs are increasingly used to assist code review — summarising changes, flagging potential issues, and suggesting improvements. In [PatchTrack](https://dl.acm.org/doi/10.1145/3691620.3695338), we studied how ChatGPT-generated patches influence pull request outcomes across open-source projects. We found a median code adoption rate of just 25%, with developers frequently engaging in iterative refinement rather than direct acceptance — suggesting that LLM suggestions function more as a **starting point** than a final answer.

## Test generation

LLMs can generate unit tests from function signatures and docstrings. Tools like CodiumAI and EvoSuite-LLM combine evolutionary search with LLM-generated test seeds. The challenge is achieving meaningful coverage rather than trivially passing tests.

## Documentation and code summarisation

Generating docstrings, README files, and inline comments from code is a task LLMs handle well. Unlike generation (where correctness must be verified), summarisation is easier to evaluate qualitatively.

## Bug localisation

Given a bug report and a codebase, can an LLM identify the faulty file or function? Recent work (SWE-bench) shows that frontier models can resolve a fraction of real GitHub issues end-to-end — a significant milestone, though far from reliable for production use.

# What the Empirical Evidence Says

A growing body of empirical SE research examines LLMs rigorously rather than treating benchmark scores as ground truth. A few key findings worth noting:

**1. Benchmark saturation is not capability saturation.**  
Models that score >90% on HumanEval often fail on slightly reformulated problems. Benchmarks measure narrow proxies; real-world SE tasks require repository navigation, understanding of implicit constraints, and awareness of deployment context.

**2. Code adoption rates are lower than generated code quality suggests.**  
Our PatchTrack study and related work consistently find that developers accept AI-generated patches at rates well below what static analysis of correctness would predict. Trust, style consistency, and perceived ownership all factor into integration decisions.

**3. LLMs introduce new categories of bugs.**  
Generated code can be syntactically correct and pass tests while containing subtle logic errors, security vulnerabilities, or license-incompatible snippets. Studies of Copilot-generated code found CWE-class vulnerabilities in a non-trivial fraction of security-sensitive completions.

**4. Prompt sensitivity is a reliability concern.**  
Small changes in prompt phrasing can cause dramatically different — and sometimes opposite — outputs. This brittleness complicates reproducibility and deployment in automated pipelines.

# Agentic LLM Systems for SE

The frontier is moving beyond single-turn prompting toward **agentic systems**: LLMs equipped with tools (code execution, file read/write, search) that can autonomously plan and execute multi-step SE tasks.

SWE-agent, Devin, and similar systems attempt to resolve GitHub issues end-to-end — writing code, running tests, and iterating on failures. These systems expose a new set of empirical questions:

- How do we evaluate **partial progress** on complex tasks?
- What **safeguards** prevent agents from making irreversible changes to production systems?
- How do agents handle **ambiguous or underspecified** requirements?

These are active research questions in my current work.

# Open Problems

Despite rapid progress, several fundamental problems remain open:

| Problem | Why it's hard |
|---|---|
| Long-context reasoning | Most SE tasks require understanding hundreds of interdependent files |
| Correctness verification | LLMs cannot reliably verify their own outputs |
| Security-aware generation | Models trained on insecure code reproduce insecure patterns |
| Fork-aware patching | Structural divergence breaks naive patch replay |
| Evaluation methodology | Benchmarks don't reflect real developer tasks or acceptance criteria |

# Getting Started

If you want to explore LLMs for SE in your own research or practice, a few practical entry points:

1. **SWE-bench** — the most realistic benchmark for evaluating LLM agents on real GitHub issues
2. **The Stack** — a deduplicated dataset of permissively licensed code for training and analysis
3. **LangChain / LlamaIndex** — frameworks for building RAG-based code assistants
4. **RepoBench** — benchmarks for repository-level code completion

For empirical work, the MSR and ICSE communities have active tracks on AI-assisted SE — a good place to find rigorous evaluations beyond vendor benchmarks.

---

*This post reflects my perspective as a researcher working at the intersection of Empirical SE and AI for SE. I am always happy to discuss these topics — feel free to reach out via email.*
