---
show: false
width: 12
date: 2025-10-01 00:00:58 +0000
group: Research Highlights
---

<div class="p-4">
    <h6 class="mb-1">Fig. 1 — Patch Integration from Source to Target Variant</h6>
    <p class="small text-muted mb-3">
        Source and target variants share a common codebase up to the <em>fork date</em>, then synchronize commits
        until the <em>divergent date</em>, after which they evolve independently. A bug-fix patch authored on the
        source variant must be cherry-picked to the target — but structural drift (refactoring) causes the
        cherry-pick to fail. RePatch resolves this by inverting refactorings on both sides before replaying the patch.
    </p>
    <img
        data-src="{{ '/assets/images/covers/repatch-divergence.png' | relative_url }}"
        src="{{ '/assets/images/css/loading.gif' | relative_url }}"
        class="lazy w-100 rounded"
        alt="Fig. 1: Illustration of patch integration from source to target variant"
        style="background: #f8f9fa;">
    <p class="small text-muted mt-2 mb-0 text-center">
        Source: Ogenrwot &amp; Businge, <em>Refactoring-Aware Patch Integration Across Structurally Divergent Java Forks</em>, IEEE SCAM 2025.
    </p>
</div>
