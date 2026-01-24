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

<!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. Suspendisse condimentum, libero vel tempus mattis, risus risus vulputate libero, elementum fermentum mi neque vel nisl. Maecenas facilisis maximus dignissim. Curabitur mattis vulputate dui, tincidunt varius libero luctus eu. Mauris mauris nulla, scelerisque eget massa id, tincidunt congue felis. Sed convallis tempor ipsum rhoncus viverra. Pellentesque nulla orci, accumsan volutpat fringilla vitae, maximus sit amet tortor. Aliquam ultricies odio ut volutpat scelerisque. Donec nisl nisl, porttitor vitae pharetra quis, fringilla sed mi. Fusce pretium dolor ut aliquam consequat. Cras volutpat, tellus accumsan mattis molestie, nisl lacus tempus massa, nec malesuada tortor leo vel quam. Aliquam vel ex consectetur, vehicula leo nec, efficitur eros. Donec convallis non urna quis feugiat.

My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=iL2j_yAAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->

I focus on **post-training of agents and multimodal base models**.

I received my M.S. from **Nanjing University** (advised by <a href="https://cs.nju.edu.cn/lutong/">Prof. Tong Lu</a>) and previously worked at **Tencent Youtu Lab**, collaborating with <a href="https://scholar.google.com/citations?user=3lMuodUAAAAJ&hl=en">Dr. Xiaobin Hu</a> and <a href="https://tyshiwo.github.io/">Prof. Ying Tai</a>.

<span class='anchor' id='-news'></span>

# 🔥 News
- *2025*: &nbsp;🏆 **Championship in <a href="https://curebench.ai/">CURE-Bench @ NeurIPS 2025</a>** (1st out of 322 teams, both tracks)
- *2025*: &nbsp;**Multimodal benchmarks released**: Human-MME (human-centric evaluation), Med-CMR (clinical reasoning)
- *2025*: &nbsp;**Three papers accepted to CVPR 2025**, including <a href="https://github.com/jixiaozhong/Sonic">Sonic</a> (3k+ stars), GroundingFace, and HunyuanPortrait
- *2024*: &nbsp;**Four papers accepted to ECCV / IJCAI / ACM MM**: DiffuMatting, UniM-OV3D, DICE-Talk
- *2022*: &nbsp;**Two papers accepted to CVPR / ECCV**: ColorFormer (image colorization), SGPN （blind face restoration）
- *2021*: &nbsp;**Publications in NeurIPS / AAAI / ECCV**: S2K, FCA, AE TextSpotter
- *2020*: &nbsp;🏆 **Won NTIRE 2020 Real-World SR Challenge @ CVPR** (1st place, both tracks)

<span class='anchor' id='-publications'></span>

# 📝 Publications

## Selected Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/cureflow.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CureFlow: An AI Engine for Complex Medication Decision-Making](https://curebench.ai/assets/MedXIAOHe-B0jbUIgI.pdf)

**Xiaozhong Ji**, Jinghao Lin, Yuhang Wu, Zihan Wang, Boyuan Jiang, Chao Gao

**NeurIPS 2025 CURE-Bench Challenge** | [**Poster**](https://curebench.ai/assets/MedXIAOHe-B0jbUIgI.pdf) | [**Leaderboard**](https://www.kaggle.com/competitions/cure-bench/leaderboard) | 🏆 Championship (MedXiaoHe team, 1st/322)
</div></div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='Sonic/static/teaser.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Sonic: Shifting focus to global audio perception in portrait animation](https://openaccess.thecvf.com/content/CVPR2025/papers/Ji_Sonic_Shifting_Focus_to_Global_Audio_Perception_in_Portrait_Animation_CVPR_2025_paper.pdf)

**Xiaozhong Ji**, Xiaobin Hu, Zhihong Xu, Junwei Zhu, Chuming Lin, Qingdong He, Jiangning Zhang, Donghao Luo, Yi Chen, Qin Lin, Qinglin Lu, Chengjie Wang

**CVPR 2025** | [**GitHub**](https://github.com/jixiaozhong/Sonic) ![](https://img.shields.io/github/stars/jixiaozhong/Sonic?style=social) | [**Paper**](https://openaccess.thecvf.com/content/CVPR2025/papers/Ji_Sonic_Shifting_Focus_to_Global_Audio_Perception_in_Portrait_Animation_CVPR_2025_paper.pdf) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-48-blue?logo=googlescholar" alt="Citations"></a>
</div></div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2020 Workshop</div><img src='images/realsr.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Real-World Super-Resolution via Kernel Estimation and Noise Injection](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ji_Real-World_Super-Resolution_via_Kernel_Estimation_and_Noise_Injection_CVPRW_2020_paper.pdf)

**Xiaozhong Ji**, Yun Cao, Ying Tai, Chengjie Wang, Jilin Li, Feiyue Huang

**CVPR 2020 Workshop** | [**GitHub**](https://github.com/jixiaozhong/RealSR) ![](https://img.shields.io/github/stars/jixiaozhong/RealSR?style=social) | [**Official Repo**](https://github.com/Tencent/Real-SR) | [**Paper**](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Ji_Real-World_Super-Resolution_via_Kernel_Estimation_and_Noise_Injection_CVPRW_2020_paper.pdf) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-435-blue?logo=googlescholar" alt="Citations"></a> | 🏆 NTIRE 2020 Challenge Winner
</div></div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/vrrf.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Align and Surpass Human Camouflaged Perception: Visual Refocus Reinforcement Fine-Tuning](https://arxiv.org/abs/2505.19611)

Ruolin Shen, **Xiaozhong Ji**, Kai WU, Jiangning Zhang, Yijun He, HaiHua Yang, Xiaobin Hu, Xiaoyu Sun

**arXiv 2025** | [**GitHub**](https://github.com/HUuxiaobin/VRRF) ![](https://img.shields.io/github/stars/HUuxiaobin/VRRF?style=social) | [**Paper**](https://arxiv.org/abs/2505.19611)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TechRxiv 2025</div><img src='images/good_teacher_better_student.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Good Teachers, Better Students: A Survey of Reward Models for LLM](https://d197for5662m48.cloudfront.net/documents/publicationstatus/298415/preprint_pdf/e523cab312a45c86a55700311bcdb4a8.pdf)

Linhao Wang, Zihan Wang, Jinghao Lin, ..., **Xiaozhong Ji**, Xiaobin Hu, et al.

**TechRxiv 2025** | [**Paper**](https://d197for5662m48.cloudfront.net/documents/publicationstatus/298415/preprint_pdf/e523cab312a45c86a55700311bcdb4a8.pdf)
</div></div>



<details>
<summary style="font-size: 1.2em; font-weight: 600; color: #495057; margin-top: 2em; margin-bottom: 1em; cursor: pointer;">
📚 Full Publication List (click to expand)
</summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/hunyuanportrait.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[HunyuanPortrait: Implicit Condition Control for Enhanced Portrait Animation](https://arxiv.org/abs/2503.18860)

Zunnan Xu, Zhentao Yu, Zixiang Zhou, Jun Zhou, Xiaoyu Jin, Fa-Ting Hong, **Xiaozhong Ji**, Junwei Zhu, Chengfei Cai, Shiyu Tang, Qin Lin, Xiu Li, Qinglin Lu

**CVPR 2025** | [**GitHub**](https://github.com/Tencent-Hunyuan/HunyuanPortrait) ![](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanPortrait?style=social) | [**Paper**](https://arxiv.org/abs/2503.18860)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/grounding_face.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GroundingFace: Fine-grained Face Understanding via Pixel Grounding Multimodal Large Language Model](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_GroundingFace_Fine-grained_Face_Understanding_via_Pixel_Grounding_Multimodal_Large_Language_CVPR_2025_paper.pdf)

Yue Han, Jiangning Zhang, Junwei Zhu, Runze Hou, **Xiaozhong Ji**, Chuming Lin, Xiaobin Hu, Zhucun Xue, Yong Liu

**CVPR 2025** | [**Paper**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_GroundingFace_Fine-grained_Face_Understanding_via_Pixel_Grounding_Multimodal_Large_Language_CVPR_2025_paper.pdf)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/medcmr.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Med-CMR: A Fine-Grained Benchmark Integrating Visual Evidence and Clinical Logic for Medical Complex Multimodal Reasoning](https://arxiv.org/abs/2512.00818)

Haozhen Gong, **Xiaozhong Ji**, Yuansen Liu, Wenbin Wu, Xiaoxiao Yan, Jingjing Liu, Kai Wu, Jiazhen Pan, Bailiang Jian, Jiangning Zhang, et al.

**arXiv 2025** | [**Paper**](https://arxiv.org/abs/2512.00818)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/human_mme.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Human-MME: A Holistic Evaluation Benchmark for Human-Centric Multimodal Large Language Models](https://arxiv.org/abs/2509.26165)

Yuansen Liu, Haiming Tang, Jinlong Peng, Jiangning Zhang, **Xiaozhong Ji**, Qingdong He, Wenbin Wu, Donghao Luo, Zhenye Gan, Junwei Zhu, et al.

**arXiv 2025** | [**Paper**](https://arxiv.org/abs/2509.26165)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TechRxiv 2025</div><img src='images/landscape_of_medical_agent.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[The Landscape of Medical Agents: A Survey](https://www.techrxiv.org/users/1005258/articles/1368207-the-landscape-of-medical-agents-a-survey)

Xiaobin Hu, Yunhang Qian, Jiaquan Yu, ..., **Xiaozhong Ji**, ..., Shuicheng Yan, et al.

**TechRxiv 2025** | [**Paper**](https://www.techrxiv.org/users/1005258/articles/1368207-the-landscape-of-medical-agents-a-survey)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/diffumatting.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DiffuMatting: Synthesizing Arbitrary Objects with Matting-level Annotation](https://arxiv.org/abs/2403.06168)

Xiaobin Hu, Xu Peng, Donghao Luo, **Xiaozhong Ji**, Jinlong Peng, Zhengkai Jiang, Jiangning Zhang, Taisong Jin, Chengjie Wang, Rongrong Ji

**ECCV 2024** | [**GitHub**](https://github.com/HUuxiaobin/DiffuMatting) ![](https://img.shields.io/github/stars/HUuxiaobin/DiffuMatting?style=social) | [**Paper**](https://arxiv.org/abs/2403.06168)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2024</div><img src='images/unimov3d.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UniM-OV3D: Uni-Modality Open-Vocabulary 3D Scene Understanding with Fine-Grained Feature Representation](https://arxiv.org/abs/2401.11395)

Qingdong He, Jinlong Peng, Zhengkai Jiang, Kai Wu, **Xiaozhong Ji**, Jiangning Zhang, Yabiao Wang, Chengjie Wang, Mingang Chen, Yunsheng Wu

**IJCAI 2024** | [**GitHub**](https://github.com/hithqd/UniM-OV3D) ![](https://img.shields.io/github/stars/hithqd/UniM-OV3D?style=social) | [**Paper**](https://arxiv.org/abs/2401.11395) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-17-blue?logo=googlescholar" alt="Citations"></a>
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2024</div><img src='images/mima_face.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MIMAFace: Face Animation via Motion-Identity Modulated Appearance Feature Learning](https://arxiv.org/abs/2409.15179)

Yue Han, Junwei Zhu, Yuxiang Feng, **Xiaozhong Ji**, Keke He, Xiangtai Li, Zhucun Xue, Yong Liu

**arXiv 2024** | [**Paper**](https://arxiv.org/abs/2409.15179)
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2024</div><img src='images/realtalk.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RealTalk: Real-time and Realistic Audio-driven Face Generation with 3D Facial Prior-guided Identity Alignment Network](https://arxiv.org/abs/2406.18284)

**Xiaozhong Ji**, Chuming Lin, Zhonggan Ding, Ying Tai, Junwei Zhu, Xiaobin Hu, Donghao Luo, Yanhao Ge, Chengjie Wang

**arXiv 2024** | [**Paper**](https://arxiv.org/abs/2406.18284) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-12-blue?logo=googlescholar" alt="Citations"></a>
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2022</div><img src='images/colorformer.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ColorFormer: Image Colorization via Color Memory Assisted Hybrid-Attention Transformer](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136760019.pdf)

**Xiaozhong Ji**, Boyuan Jiang, Donghao Luo, Guangpin Tao, Wenqing Chu, Zhifeng Xie, Chengjie Wang, Ying Tai

**ECCV 2022** | [**GitHub**](https://github.com/jixiaozhong/ColorFormer) ![](https://img.shields.io/github/stars/jixiaozhong/ColorFormer?style=social) | [**Official Repo**](https://github.com/TencentYoutuResearch/ImageColorization-ColorFormer) | [**Paper**](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136760019.pdf) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-84-blue?logo=googlescholar" alt="Citations"></a>
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2022</div><img src='images/blind_face.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Blind Face Restoration via Integrating Face Shape and Generative Priors](https://openaccess.thecvf.com/content/CVPR2022/html/Zhu_Blind_Face_Restoration_via_Integrating_Face_Shape_and_Generative_Priors_CVPR_2022_paper.html)

Feida Zhu, Junwei Zhu, Wenqing Chu, Xinyi Zhang, **Xiaozhong Ji**, Chengjie Wang, Ying Tai

**CVPR 2022** | [**Paper**](https://openaccess.thecvf.com/content/CVPR2022/html/Zhu_Blind_Face_Restoration_via_Integrating_Face_Shape_and_Generative_Priors_CVPR_2022_paper.html) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-12-blue?logo=googlescholar" alt="Citations"></a>
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2021</div><img src='images/spectrum2kernel.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Spectrum-to-Kernel Translation for Accurate Blind Image Super-Resolution](https://arxiv.org/abs/2110.12151)

Guangpin Tao, **Xiaozhong Ji**, Wenzhuo Wang, Shuo Chen, Chuming Lin, Yun Cao, Tong Lu, Donghao Luo, Ying Tai

**NeurIPS 2021** | [**Paper**](https://arxiv.org/abs/2110.12151) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-34-blue?logo=googlescholar" alt="Citations"></a>
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2021</div><img src='images/fca.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Frequency Consistent Adaptation for Real World Super Resolution](https://arxiv.org/abs/2012.10102)

**Xiaozhong Ji**, Guangpin Tao, Yun Cao, Ying Tai, Tong Lu, Chengjie Wang, Jilin Li, Feiyue Huang

**AAAI 2021** | [**Paper**](https://arxiv.org/abs/2012.10102) | <a href="https://scholar.google.com/citations?user=iL2j_yAAAAAJ"><img src="https://img.shields.io/badge/citations-12-blue?logo=googlescholar" alt="Citations"></a>
</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2020</div><img src='images/ae_textspotter.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AE TextSpotter: Learning Visual and Linguistic Representation for Ambiguous Text Spotting](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/3946_ECCV_2020_paper.php)

Wenhai Wang, Xuebo Liu, **Xiaozhong Ji**, Enze Xie, Ding Liang, ZhiBo Yang, Tong Lu, Chunhua Shen, Ping Luo

**ECCV 2020** | [**Paper**](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/3946_ECCV_2020_paper.php)
</div></div>

</details>

<span class='anchor' id='-competition-awards'></span>

# 🏆 Competition Awards

<div style="margin: 20px 0;">
<strong>🥇 Champion – CURE-Bench @ NeurIPS 2025</strong> (Nov 2025)<br>
1st place out of 322 teams · Won both tracks (internal reasoning and agentic reasoning)<br>
<a href="https://curebench.ai/">Competition Website</a> | <a href="https://neurips.cc/virtual/2025/competition/127720">NeurIPS Page</a>
</div>

<div style="margin: 20px 0;">
<strong>🥇 Champion – NTIRE 2020 Real-World Super-Resolution Challenge @ CVPR 2020</strong> (Jun 2020)<br>
1st place · Won both Track 1 (Image Processing Artifacts) and Track 2 (Smartphone Images)<br>
<a href="https://data.vision.ee.ethz.ch/cvl/ntire20/">Competition Website</a> | <a href="https://github.com/jixiaozhong/RealSR">Code (788 stars)</a>
</div> 
