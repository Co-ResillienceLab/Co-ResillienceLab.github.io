---
layout: default
title: Home
---
<div class="hero">
  <h2>Community-level resilience against digital harms and physical threats</h2>
</div>

CoRe Lab investigates community-level resilience against digital harms and physical threats. Rather than isolated interventions, we build collective knowledge and peer-support infrastructures to protect ecosystems, moving from individual security (e.g., one's own password) to distributed, community security, ensuring holistic protection.

The group also addresses the interconnected nature of protection, bridging physical (e.g., crowd safety, evacuations) and digital (e.g., community resilience, incident response) spheres, with both human and nonhuman actors.

## Our approach

Current approaches that treat vulnerable users as edge cases miss their systemic importance as both attractive attack vectors and potential points of failure in socio-technical systems. Our distinctive approach recognises that vulnerability in one segment weakens entire ecosystems. When vulnerable populations lack protection, whole communities are compromised.

We offer a holistic, ecosystems approach to building resilient communities, combining **technical innovation** (privacy-preserving systems, crowd management and computational simulation) with **social interventions** (literacy programmes, peer support and policy engagement).

## Research themes

<div class="theme-grid">
  <div class="theme">Mis/disinformation</div>
  <div class="theme">Cyber security</div>
  <div class="theme">Crowd simulation</div>
  <div class="theme">Policing</div>
  <div class="theme">Digital literacy</div>
  <div class="theme">Community resilience</div>
</div>

## Latest news
{% for post in site.posts limit:3 %}
- **{{ post.date | date: "%-d %B %Y" }}**: [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

[More news →]({{ '/news/' | relative_url }})

## Get in touch

CoRe Lab is based at {{ site.affiliation }}. For enquiries, contact our current research group lead, [{{ site.contact_name }}](mailto:{{ site.contact_email }}).
