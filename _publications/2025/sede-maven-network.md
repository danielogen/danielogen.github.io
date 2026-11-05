---
title: "Structural and Connectivity Patterns in the Maven Central Software Dependency Network"
date: 2025-08-01 00:00:00 +0000
selected: false
pub: "34th International Conference on Software Engineering and Data Engineering (SEDE)"
pub_date: "2025"
type: conference
venue_short: "SEDE 2025"
topics: [ecosystems]
abstract: >-
  Understanding the structural characteristics and connectivity patterns of large-scale software
  ecosystems is critical for enhancing software reuse, improving ecosystem resilience, and mitigating
  security risks. In this paper, we investigate the Maven Central ecosystem, one of the largest
  repositories of Java libraries, by applying network science techniques to its dependency graph.
  Leveraging the Goblin framework, we extracted a sample consisting of the top 5,000 highly connected
  artifacts based on their degree centrality and then performed breadth-first search (BFS) expansion
  from each selected artifact as a seed node, traversing the graph outward to capture all libraries
  and releases reachable those seed nodes. This sampling strategy captured the immediate structural
  context surrounding these libraries resulted in a curated graph comprising of 1.3 million nodes and
  20.9 million edges. We conducted a comprehensive analysis of this graph, computing degree
  distributions, betweenness centrality, PageRank centrality, and connected components graph-theoretic
  metrics. Our results reveal that Maven Central exhibits a highly interconnected, scale-free, and
  small-world topology, characterized by a small number of infrastructural hubs that support the
  majority of projects. Further analysis using PageRank and betweenness centrality shows that these
  hubs predominantly consist of core ecosystem infrastructure, including testing frameworks and
  general-purpose utility libraries. While these hubs facilitate efficient software reuse and
  integration, they also pose systemic risks; failures or vulnerabilities affecting these critical
  nodes can have widespread and cascading impacts throughout the ecosystem.
authors:
  - Daniel Ogenrwot
  - John Businge
  - Shaikh Arifuzzaman
links:
  Paper: https://link.springer.com/chapter/10.1007/978-3-032-08649-5_9
---
