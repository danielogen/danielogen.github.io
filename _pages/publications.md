---
layout: page
permalink: /publications/
title: Publications
description: For a complete list of my publications, please visit my profiles on <a href='https://scholar.google.com/citations?user=ZpCrmOQAAAAJ&hl=en'><b class='badge badge-primary'>Google Scholar</b></a> or <a href='https://orcid.org/0000-0002-0133-8164'><b class='badge badge-primary'>ORCID</b></a>. Feel free to reach out if you’re interested in collaboration or learning more about my work!.
years: [2026, 2025, 2024, 2022, 2021, 2020]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
