---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% assign profile = site.data.profile %}

<div class="home-hero card" id="about">
  <div class="home-hero__intro">
    <h1>{{ profile.profile.name }}</h1>
    <div class="home-hero__bio">
      {% for paragraph in profile.profile.bio %}
      {{ paragraph | replace: "__WECHAT_IMAGE__", profile.site.wechat_image | markdownify }}
      {% endfor %}
    </div>
  </div>
</div>

<section class="profile-section card" id="research">
  <h2><i class="fas fa-flask"></i>AI Risk Measurement and Mitigation</h2>
  {% for area in profile.research_areas %}
  <div class="topic-group">
    <h3>{{ area.title }}</h3>
    <ul class="topic-list">
      {% for item in area.items %}
      <li>
        <strong>{{ item.label }}</strong>
        {% for link in item.links %}
          {% if link.url != "" %}
          <a class="chip" href="{{ link.url }}">{{ link.text }}</a>
          {% else %}
          <span class="chip chip--muted">{{ link.text }}</span>
          {% endif %}
        {% endfor %}
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</section>

<section class="profile-section card" id="news">
  <h2><i class="fas fa-newspaper"></i>News</h2>
  <ul class="timeline-list">
    {% for item in profile.news %}
    <li>{{ item | replace: "__REPORT_PDF__", profile.site.report_pdf | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ul>
</section>

<section class="profile-section card" id="publications">
  <div class="section-heading">
    <h2><i class="fas fa-book-open"></i>Selected Publications</h2>
    {{ profile.publications_note | markdownify }}
  </div>
  <ol class="publication-list">
    {% for item in profile.publications %}
    <li>{{ item | replace: "[CCF-A]", '<span class="ccf-badge ccf-a">CCF-A</span>' | replace: "[CCF-B]", '<span class="ccf-badge ccf-b">CCF-B</span>' | replace: "[CCF-C]", '<span class="ccf-badge ccf-c">CCF-C</span>' | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ol>
</section>

<div class="compact-grid">
  <section class="profile-section profile-section--compact card" id="honors">
    <h2><i class="fas fa-trophy"></i>Honors and Awards</h2>
    <ul class="simple-list">
      {% for item in profile.honors %}
      <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="profile-section profile-section--compact card" id="educations">
    <h2><i class="fas fa-graduation-cap"></i>Educations</h2>
    <ul class="simple-list">
      {% for item in profile.education %}
      <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="profile-section profile-section--compact card" id="service">
    <h2><i class="fas fa-users"></i>Service</h2>
    <ul class="simple-list">
      {% for item in profile.service %}
      <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="profile-section profile-section--compact card" id="internships">
    <h2><i class="fas fa-briefcase"></i>Internships</h2>
    <ul class="simple-list">
      {% for item in profile.internships %}
      <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
      {% endfor %}
    </ul>
  </section>
</div>
