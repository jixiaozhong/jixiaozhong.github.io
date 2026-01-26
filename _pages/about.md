---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>


I focus on **post-training of agents and multimodal base models**.

I received my M.S. from **Nanjing University** (advised by <a href="https://cs.nju.edu.cn/lutong/">Prof. Tong Lu</a>) and previously worked at **Tencent Youtu Lab**, collaborating with <a href="https://scholar.google.com/citations?user=3lMuodUAAAAJ&hl=en">Dr. Xiaobin Hu</a> and <a href="https://tyshiwo.github.io/">Prof. Ying Tai</a>.

<span class='anchor' id='-news'></span>

# 🔥 News
- *2026*: &nbsp;**Two benchmark papers accepted to ICLR 2026**: MedLesionVQA, Human-MME
- *2025*: &nbsp;🏆 **Championship in <a href="https://curebench.ai/">CURE-Bench @ NeurIPS 2025</a>** (1st out of 322 teams, both tracks)
- *2025*: &nbsp;**Four papers accepted to CVPR / ACM MM 2025**, including <a href="https://github.com/jixiaozhong/Sonic">Sonic</a> (3k+ stars), GroundingFace, HunyuanPortrait, and DICE-Talk
- *2024*: &nbsp;**Three papers accepted to ECCV / IJCAI**: DiffuMatting, UniM-OV3D
- *2022*: &nbsp;**Two papers accepted to CVPR / ECCV**: ColorFormer (image colorization), SGPN （blind face restoration）
- *2021*: &nbsp;**Publications in NeurIPS / AAAI / ECCV**: S2K, FCA, AE TextSpotter
- *2020*: &nbsp;🏆 **Won NTIRE 2020 Real-World SR Challenge @ CVPR** (1st place, both tracks)

<span class='anchor' id='-publications'></span>

# 📝 Publications

## Selected Publications

{% include publications/cureflow.html %}

{% include publications/good-teachers-better-students.html %}

{% include publications/vrrf.html %}

{% include publications/sonic.html %}

{% include publications/hunyuanportrait.html %}

{% include publications/groundingface.html %}

{% include publications/diffumatting.html %}

{% include publications/realsr.html %}


<details>
<summary style="font-size: 1.2em; font-weight: 600; color: #495057; margin-top: 2em; margin-bottom: 1em; cursor: pointer;">
📚 Full Publication List (click to expand)
</summary>

{% include publications/medical-agents-survey.html %}

{% include publications/human-mme.html %}

{% include publications/med-cmr.html %}

{% include publications/unim-ov3d.html %}

{% include publications/dice-talk.html %}

{% include publications/mimaface.html %}

{% include publications/realtalk.html %}

{% include publications/colorformer.html %}

{% include publications/blind-face-restoration.html %}

{% include publications/spectrum2kernel.html %}

{% include publications/fca.html %}

{% include publications/ae-textspotter.html %}

</details>

<span class='anchor' id='-competition-awards'></span>

# 🏆 Awards & Honors

<div style="margin: 20px 0;">
<strong>🥇 Champion – CURE-Bench @ NeurIPS 2025</strong> (Nov 2025)<br>
1st place out of 322 teams · Won both tracks (internal reasoning and agentic reasoning)<br>
<a href="https://curebench.ai/">Competition Website</a> | <a href="https://neurips.cc/virtual/2025/competition/127720">NeurIPS Page</a>
</div>

<div style="margin: 20px 0;">
<strong>🎓 Outstanding Master's Thesis Award – Nanjing University</strong> (2021)<br>
Thesis: "Key Techniques for Super-Resolution of Blurred Data in Real-World Scenarios"<br>
Computer Science Department
</div>

<div style="margin: 20px 0;">
<strong>🥇 Champion – NTIRE 2020 Real-World Super-Resolution Challenge @ CVPR 2020</strong> (Jun 2020)<br>
1st place · Won both Track 1 (Image Processing Artifacts) and Track 2 (Smartphone Images)<br>
<a href="https://data.vision.ee.ethz.ch/cvl/ntire20/">Competition Website</a> | <a href="https://github.com/jixiaozhong/RealSR">Code (788 stars)</a>
</div> 
