---
permalink: /posts/
title: "Posts"
excerpt: "Paper pages and personal posts."
author_profile: true
---

{% assign paper_posts = site.posts | where_exp: "post", "post.tags contains 'paper'" %}
{% assign personal_posts = site.posts | where_exp: "post", "post.tags contains 'paper' == false" %}

<div class="home-hero card" id="posts-top">
  <div class="home-hero__intro">
    <h1>Posts</h1>
    <div class="home-hero__bio">
      <p>Paper pages and personal posts.</p>
    </div>
  </div>
</div>

{% if paper_posts.size > 0 %}
<section class="profile-section card" id="paper-pages">
  <h2><i class="fas fa-file-alt"></i>Paper Pages</h2>
  <ul class="post-list">
    {% for post in paper_posts %}
    <li class="post-item">
      <a class="post-title" href="{{ post.url }}">{{ post.title }}</a>
      <div class="post-meta">
        <span class="post-date"><i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%b %d, %Y" }}</span>
        {% for tag in post.tags %}{% unless tag == "paper" %}<span class="chip chip--muted">{{ tag }}</span>{% endunless %}{% endfor %}
      </div>
      <p class="post-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncatewords: 40 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}

{% if personal_posts.size > 0 %}
<section class="profile-section card" id="personal-posts">
  <h2><i class="fas fa-pen"></i>Personal Posts</h2>
  <ul class="post-list">
    {% for post in personal_posts %}
    <li class="post-item">
      <a class="post-title" href="{{ post.url }}">{{ post.title }}</a>
      <div class="post-meta">
        <span class="post-date"><i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%b %d, %Y" }}</span>
        {% for tag in post.tags %}<span class="chip chip--muted">{{ tag }}</span>{% endfor %}
      </div>
      <p class="post-excerpt">{{ post.excerpt | strip_html | strip_newlines | truncatewords: 40 }}</p>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}
