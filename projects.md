---
layout: default
title: Projects
---
{% assign active = site.projects | where_exp: "p", "p.status != 'Completed'" | sort: "title" %}
{% assign past = site.projects | where: "status", "Completed" | sort: "title" %}

{% if active.size > 0 %}
<section class="people-group">
  <h2>Current Projects</h2>
  <div class="project-grid">
    {% for p in active %}
    <a class="card project-card" href="{{ p.url | relative_url }}">
      {% if p.image %}<img src="{{ p.image | relative_url }}" alt="{{ p.title }}">{% endif %}
      <h3>{{ p.title }}</h3>
      <p>{{ p.summary }}</p>
    </a>
    {% endfor %}
  </div>
</section>
{% endif %}

{% if past.size > 0 %}
<section class="people-group">
  <h2>Completed Projects</h2>
  <div class="project-grid">
    {% for p in past %}
    <a class="card project-card" href="{{ p.url | relative_url }}">
      {% if p.image %}<img src="{{ p.image | relative_url }}" alt="{{ p.title }}">{% endif %}
      <h3>{{ p.title }}</h3>
      <p>{{ p.summary }}</p>
    </a>
    {% endfor %}
  </div>
</section>
{% endif %}
