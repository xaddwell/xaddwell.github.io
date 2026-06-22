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

<div class="home-hero">
  <div class="home-hero__intro">
    <p class="home-hero__eyebrow">{{ profile.profile.headline }}</p>
    <h1>{{ profile.profile.name }}</h1>
    <div class="home-hero__bio">
      {% for paragraph in profile.profile.bio %}
      {{ paragraph | replace: "__WECHAT_IMAGE__", profile.site.wechat_image | markdownify }}
      {% endfor %}
    </div>
  </div>
</div>

<section class="profile-section">
  <h2>AI Risk Measurement and Mitigation</h2>
  {% for area in profile.research_areas %}
  <div class="topic-group">
    <h3>{{ area.title }}</h3>
    <ul class="topic-list">
      {% for item in area.items %}
      <li>
        <strong>{{ item.label }}:</strong>
        {% for link in item.links %}
          {% if link.url != "" %}
          <a href="{{ link.url }}">{{ link.text }}</a>
          {% else %}
          <span>{{ link.text }}</span>
          {% endif %}
          {% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</section>

<section class="profile-section">
  <h2>News</h2>
  <ul class="timeline-list">
    {% for item in profile.news %}
    <li>{{ item | replace: "__REPORT_PDF__", profile.site.report_pdf | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ul>
</section>

<section class="profile-section">
  <div class="section-heading">
    <h2>Selected Publications</h2>
    {{ profile.publications_note | markdownify }}
  </div>
  <ol class="publication-list">
    {% for item in profile.publications %}
    <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ol>
</section>

<section class="profile-section profile-section--compact">
  <h2>Honors and Awards</h2>
  <ul class="simple-list">
    {% for item in profile.honors %}
    <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ul>
</section>

<section class="profile-section profile-section--compact">
  <h2>Educations</h2>
  <ul class="simple-list">
    {% for item in profile.education %}
    <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ul>
</section>

<section class="profile-section profile-section--compact">
  <h2>Service</h2>
  <ul class="simple-list">
    {% for item in profile.service %}
    <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ul>
</section>

<section class="profile-section profile-section--compact">
  <h2>Internships</h2>
  <ul class="simple-list">
    {% for item in profile.internships %}
    <li>{{ item | markdownify | remove: "<p>" | remove: "</p>" }}</li>
    {% endfor %}
  </ul>
</section>
