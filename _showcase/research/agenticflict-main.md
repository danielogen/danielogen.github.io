---
show: true
width: 6
date: 2026-06-02 00:00:01 +0000
group: Research Highlights
---

<div class="p-4">
    <div class="d-flex align-items-start justify-content-between flex-wrap mb-2">
        <div>
            <span class="badge badge-pill badge-primary mr-1">AIware 2026</span>
            <span class="badge badge-pill badge-info mr-1">FSE 2026</span>
            <span class="badge badge-pill badge-secondary">Dataset Track</span>
        </div>
        <small class="text-muted mt-1">2026</small>
    </div>
    <h5 class="mt-2 mb-1">AgenticFlict: Merge Conflicts in AI Coding Agent Pull Requests</h5>
    <p class="small text-muted mb-2">Daniel Ogenrwot &middot; John Businge</p>
    <p class="small mb-3">
        AI coding agents (Copilot, Devin, Cursor, etc.) are increasingly submitting pull requests to
        real repositories. AgenticFlict mines <strong>142K+ agentic PRs</strong> from 59K+ repositories,
        identifying <strong>29K PRs with merge conflicts</strong> and extracting
        <strong>336K+ fine-grained conflict regions</strong>, revealing that conflicts are both frequent
        and often substantial in AI-generated contributions.
    </p>
    <img
        data-src="{{ '/assets/images/covers/agenticflict-overview.png' | relative_url }}"
        src="{{ '/assets/css/images/loading.gif' | relative_url }}"
        class="lazy w-100 rounded mb-3"
        alt="AgenticFlict dataset curation workflow"
        style="background: #f8f9fa;">
    <div class="d-flex flex-wrap" style="gap: 0.5rem;">
        <a href="https://arxiv.org/abs/2604.03551" target="_blank" class="btn btn-sm btn-outline-primary">
            <i class="fas fa-file-pdf mr-1"></i>Preprint
        </a>
        <a href="https://zenodo.org/records/19396917" target="_blank" class="btn btn-sm btn-outline-secondary">
            <i class="fas fa-download mr-1"></i>Dataset &amp; Code
        </a>
    </div>
</div>
