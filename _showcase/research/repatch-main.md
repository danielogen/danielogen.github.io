---
show: true
width: 8
date: 2026-06-03 00:00:01 +0000
group: Research Highlights
---

<div class="p-4">
    <div class="d-flex align-items-start justify-content-between flex-wrap mb-2">
        <div>
            <span class="badge badge-pill badge-danger mr-1">SCAM 2025</span>
            <span class="badge badge-pill badge-warning">
                <i class="fas fa-trophy mr-1"></i>Distinguished Artifact Award
            </span>
        </div>
        <small class="text-muted mt-1">Oct 2025</small>
    </div>

    <h5 class="mt-2 mb-1">Refactoring-Aware Patch Integration Across Structurally Divergent Java Forks</h5>
    <p class="small text-muted mb-3">Daniel Ogenrwot &middot; John Businge</p>

    <p class="mb-3">
        When two software variants diverge through independent refactoring, replaying patches from one fork to another
        fails silently — renamed methods, moved classes, and restructured call hierarchies cause integration to break
        even when the underlying logic is sound.
    </p>
    <p class="mb-3">
        <strong>RePatch</strong> addresses this by making patch integration <em>refactoring-aware</em>: it detects
        structural drift between forks and resolves mismatches before applying patches. On a benchmark of previously
        failing cross-fork patches, RePatch recovered <strong>52.8%</strong> of integrations that naive replay could
        not handle.
    </p>

    <h6 class="mb-1 mt-3">Fig. 1 — Patch Integration from Source to Target Variant</h6>
    <p class="small text-muted mb-2">
        Source and target variants share a common codebase up to the <em>fork date</em>, then synchronize
        until the <em>divergent date</em>, after which they evolve independently. Structural drift causes
        cherry-pick to fail; RePatch inverts refactorings on both sides before replaying the patch.
    </p>
    <img
        data-src="{{ '/assets/images/covers/repatch-divergence.png' | relative_url }}"
        src="{{ '/assets/css/images/loading.gif' | relative_url }}"
        class="lazy w-100 rounded mb-3"
        alt="Fig. 1: Illustration of patch integration from source to target variant"
        style="background: #f8f9fa;">

    <div class="d-flex flex-wrap" style="gap: 0.5rem;">
        <a href="https://ieeexplore.ieee.org/document/11190222" target="_blank" class="btn btn-sm btn-outline-danger">
            <i class="fas fa-file-pdf mr-1"></i>Paper
        </a>
        <a href="https://github.com/unlv-evol/RePatch" target="_blank" class="btn btn-sm btn-outline-dark">
            <i class="fab fa-github mr-1"></i>Code
        </a>
    </div>
</div>
