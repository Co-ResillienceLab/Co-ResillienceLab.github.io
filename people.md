---
layout: default
title: People
---
{% assign sections = "Members,Affiliate Members,Researchers,Students" | split: "," %}

{% for section in sections %}
{% assign group = site.people | where: "category", section | sort: "surname" %}
{% if group.size > 0 %}
<section class="people-group">
  <h2>{{ section }}</h2>
  <div class="people-grid">
    {% for p in group %}
    <a class="card" href="{{ p.url | relative_url }}">
      {% if p.photo %}<img src="{{ p.photo | relative_url }}" alt="{{ p.title }}">{% endif %}
      <h3>{{ p.title }}</h3>
      <p>{{ p.role }}</p>
    </a>
    {% endfor %}
  </div>
</section>
{% endif %}
{% endfor %}
