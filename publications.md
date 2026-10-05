---
layout: default
title: Publications
---
{% assign by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% for y in by_year %}
<h2>{{ y.name | default: "Undated" }}</h2>
<ul class="pub-list">
  {% for p in y.items %}
  <li>
    <span class="pub-title">{{ p.title }}</span><br>
    {% if p.authors.size > 0 %}{{ p.authors | join: ", " }}<br>{% endif %}
    {% if p.journal != "" %}<em>{{ p.journal }}</em>{% endif %}
    {% if p.doi %} · <a href="https://doi.org/{{ p.doi }}">DOI</a>{% endif %}
  </li>
  {% endfor %}
</ul>
{% endfor %}
