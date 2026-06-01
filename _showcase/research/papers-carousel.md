---
show: false
width: 12
date: 2025-10-01 00:00:00 +0000
group: Research Highlights
---

<div id="papers-carousel" class="carousel slide" data-ride="carousel" data-interval="false">

    <!-- Indicators -->
    <ol class="carousel-indicators" style="bottom: -28px;">
        <li data-target="#papers-carousel" data-slide-to="0" class="active" style="background-color: #CF0A2C;"></li>
        <li data-target="#papers-carousel" data-slide-to="1" style="background-color: #CF0A2C;"></li>
    </ol>

    <div class="carousel-inner">

        <!-- Slide 1: AgenticFlict -->
        <div class="carousel-item active">
            <div class="p-4">
                <div class="d-flex align-items-start justify-content-between flex-wrap mb-2">
                    <div>
                        <span class="badge badge-pill badge-primary mr-1">AIware 2026</span>
                        <span class="badge badge-pill badge-info mr-1">FSE 2026</span>
                        <span class="badge badge-pill badge-secondary">Dataset Track</span>
                    </div>
                    <small class="text-muted mt-1">2026</small>
                </div>
                <h5 class="mt-2 mb-1">AgenticFlict: A Large-Scale Dataset of Merge Conflicts in AI Coding Agent Pull Requests on GitHub</h5>
                <p class="small text-muted mb-3">Daniel Ogenrwot &middot; John Businge</p>
                <div class="row align-items-start">
                    <div class="col-md-5 mb-3">
                        <p class="small mb-3">
                            AI coding agents (Copilot, Devin, Cursor, etc.) are increasingly submitting pull requests to real repositories.
                            AgenticFlict mines <strong>142K+ agentic PRs</strong> from 59K+ repositories, identifying
                            <strong>29K PRs with merge conflicts</strong> and extracting <strong>336K+ fine-grained conflict regions</strong>
                            — revealing that merge conflicts are both frequent and often substantial in AI-generated contributions.
                        </p>
                        <div class="d-flex flex-wrap" style="gap: 0.5rem;">
                            <a href="https://arxiv.org/abs/2604.03551" target="_blank" class="btn btn-sm btn-outline-primary">
                                <i class="fas fa-file-pdf mr-1"></i>Preprint
                            </a>
                            <a href="https://zenodo.org/records/19396917" target="_blank" class="btn btn-sm btn-outline-secondary">
                                <i class="fas fa-download mr-1"></i>Dataset & Code
                            </a>
                        </div>
                    </div>
                    <div class="col-md-7">
                        <img
                            data-src="{{ '/assets/images/covers/agenticflict-overview.png' | relative_url }}"
                            src="{{ '/assets/images/css/loading.gif' | relative_url }}"
                            class="lazy rounded d-block mx-auto"
                            alt="AgenticFlict dataset curation workflow"
                            style="max-height: 320px; width: auto; background: #f8f9fa;">
                        <p class="small text-muted text-center mt-1 mb-0">Fig. 1 — Dataset curation workflow</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 2: PatchTrack -->
        <div class="carousel-item">
            <div class="p-4">
                <div class="d-flex align-items-start justify-content-between flex-wrap mb-2">
                    <div>
                        <span class="badge badge-pill badge-success mr-1">EMSE Journal</span>
                        <span class="badge badge-pill badge-secondary">arXiv 2505.07700</span>
                    </div>
                    <small class="text-muted mt-1">2025</small>
                </div>
                <h5 class="mt-2 mb-1">PatchTrack: A Comprehensive Analysis of ChatGPT's Influence on Pull Request Outcomes</h5>
                <p class="small text-muted mb-3">Daniel Ogenrwot &middot; John Businge</p>
                <div class="row align-items-start">
                    <div class="col-md-5 mb-3">
                        <p class="small mb-3">
                            Studying <strong>338 pull requests</strong> from 255 GitHub repositories with self-admitted ChatGPT usage,
                            PatchTrack finds that full adoption of AI-generated code is infrequent —
                            median integration rate of <strong>25%</strong>. Developers use structural integration,
                            selective extraction, and iterative refinement rather than direct acceptance,
                            showing AI's influence extends beyond patch generation to the entire code review process.
                        </p>
                        <div class="d-flex flex-wrap" style="gap: 0.5rem;">
                            <a href="https://link.springer.com/epdf/10.1007/s10664-026-10869-5?sharing_token=mD5opNwR77D4ukrUIIYD__e4RwlQNchNByi7wbcMAY7xh1s4CXXz38H72KxsIoYCtfkP67vK30Jh-x17Yoy23dky9NHrVQmUKPQNp8AgN_JbqNPTJu2d82UYgsMc8UDm4ie8ksro1fVQDnxpA33ru3yRyaoIhaLmj-JQ04-WPow%3D" target="_blank" class="btn btn-sm btn-outline-success">
                                <i class="fas fa-file-pdf mr-1"></i>Paper (EMSE)
                            </a>
                            <a href="https://arxiv.org/abs/2505.07700" target="_blank" class="btn btn-sm btn-outline-secondary">
                                <i class="fas fa-external-link-alt mr-1"></i>Preprint
                            </a>
                        </div>
                    </div>
                    <div class="col-md-7">
                        <img
                            data-src="{{ '/assets/images/covers/patchtrack-overview.png' | relative_url }}"
                            src="{{ '/assets/images/css/loading.gif' | relative_url }}"
                            class="lazy w-100 rounded"
                            alt="PatchTrack study method overview"
                            style="background: #f8f9fa;">
                        <p class="small text-muted text-center mt-1 mb-0">Fig. 2 — Overview of the study method</p>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- Controls -->
    <a class="carousel-control-prev" href="#papers-carousel" role="button" data-slide="prev" style="width: 36px;">
        <span class="carousel-control-prev-icon" style="filter: invert(1) sepia(1) saturate(5) hue-rotate(300deg);"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#papers-carousel" role="button" data-slide="next" style="width: 36px;">
        <span class="carousel-control-next-icon" style="filter: invert(1) sepia(1) saturate(5) hue-rotate(300deg);"></span>
        <span class="sr-only">Next</span>
    </a>

</div>
<div style="height: 36px;"></div>
