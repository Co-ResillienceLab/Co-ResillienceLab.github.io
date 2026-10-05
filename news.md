---
layout: default
title: News
---
<div class="post-list">
{% for post in site.posts %}
  <article class="post-card">
    {% if post.image %}
      <a href="{{ post.url | relative_url }}"><img src="{{ post.image | relative_url }}" alt="{{ post.title }}"></a>
    {% endif %}
    <div>
      <p class="role">
        {{ post.date | date: "%-d %B %Y" }}{% if post.author %} · {{ post.author }}{% endif %}
      </p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{% if post.summary %}{{ post.summary }}{% else %}{{ post.excerpt | strip_html | truncatewords: 40 }}{% endif %}</p>
      <a href="{{ post.url | relative_url }}">Read more →</a>
    </div>
  </article>
{% endfor %}
</div>
