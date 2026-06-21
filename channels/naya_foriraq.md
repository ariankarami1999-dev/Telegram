<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/mS2imGDr675hJ8BXp3mRkUQ_ZEafQTKKiL8CoLokq8OPRpG1z5D_8or4yLr28va6PjJQyCHTwbTOxtUux3JH9PGq_baAWflqybossL7_40CsPQd3FBJATjqe86Ks2Aa2RlNejQ-w8YWtH3pmjIkIsZrejsg3GPT8_-wKQnPXRFqlJuNbQUTsosnaiPLjXeRKUPKfgfzjSyBNLq34OiiOJcEraAyzw0Bpkq8STWb9b5-HLK8Ye9jwhmHnZi8sUEa0N9XCkqxXehLLBUCrLiwPYF-jXmCvQVcvYg9L0px62fiail2YCysZO_lyTDbTPU4zxWq4ixhge4sgigRgkSDM8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 20:29:25</div>
<hr>

<div class="tg-post" id="msg-79515">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: الفريق الإيراني المفاوض يترك محل المفاوضات.</div>
<div class="tg-footer">👁️ 393 · <a href="https://t.me/naya_foriraq/79515" target="_blank">📅 20:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb5dd698d.mp4?token=ryJKL49CVXGJ-yhynMKH_X2m5UZwOK-cpxwAAwDYk1euyY6grsNjpl7hcZE9ismn5dF6p1CNrI73VZv97VE1O-K-WV4EbNSFYqlzs0wuzVKQE-Xz67cetAy83njmy2TibNE5VrI18rvPzwu5KwGXaOHDo2Ahu9V4hOP646Ns6fimK3qnQ11e-YyNuFQNAFQv9GfZc9VQo039L7gZTfYX-8amhrmZIiwuzOKyDuZKaiF5kpK9bKW9cIsjXdciZX86TqcFqwN6QReKMnyNcb1cYSrKBzMmh5sGGXDnhLO79GUA770Cb4khiJvyJhOSY1UOZ7MHx8OdWozmInjvrDIZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb5dd698d.mp4?token=ryJKL49CVXGJ-yhynMKH_X2m5UZwOK-cpxwAAwDYk1euyY6grsNjpl7hcZE9ismn5dF6p1CNrI73VZv97VE1O-K-WV4EbNSFYqlzs0wuzVKQE-Xz67cetAy83njmy2TibNE5VrI18rvPzwu5KwGXaOHDo2Ahu9V4hOP646Ns6fimK3qnQ11e-YyNuFQNAFQv9GfZc9VQo039L7gZTfYX-8amhrmZIiwuzOKyDuZKaiF5kpK9bKW9cIsjXdciZX86TqcFqwN6QReKMnyNcb1cYSrKBzMmh5sGGXDnhLO79GUA770Cb4khiJvyJhOSY1UOZ7MHx8OdWozmInjvrDIZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
الجيش اللبناني يسحب آلية إسرائيلية تم إستهدفها وتدميرها على يد أبناء نصرالله في بلدة دبين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/naya_foriraq/79514" target="_blank">📅 20:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79513">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvAYcIeMO3cm7UUv9PlcxiEoQm0WpLaJxyHLCH-vHLu_lBkY6uFs5P2KzouJKkbRqRCk8epIwVWriqJ9hUPn0gIV2BlgDd6dOwcDvLhyWvEQ3xom0I8Sy83omktEtxMm0ELZb3Q5Gy7gi6luRzdmau1iN8w3ZDFGnwRmsBy79lLYvdQAidWLwGKQGrLbTU8G2_Epsri1zPg15INOrSYHeWQ7cr0vWB4WK0n4LN3vm3FsqOgCncDDKKmg23tw-OneX-YeAc1ou2W75lUMlpw6ScZ-5p3673tijQQXzChTaRuX3gRXeqL1x9nYOCBMp1OBAx9C5X2uRddogYdk5nxvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/naya_foriraq/79513" target="_blank">📅 20:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79512">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: الفريق الإيراني المفاوض يترك محل المفاوضات.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/79512" target="_blank">📅 20:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79511">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: تهديد ترامب يوقف المحادثات في سويسرا، ويُلقي بظلال من الشك على استمرارها.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/naya_foriraq/79511" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">طوفان ٧-٨ ادامه دارد
طوفان ٧-٨ مستمرّ
Storm 7-8 is ongoing
#كابوسكم_رمضان</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/naya_foriraq/79510" target="_blank">📅 19:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0d5c6577.mp4?token=pzij6QFlnGWsBhgyHIDEck0BEJAHSlC_vxeX1oRdXDcPTxOf9HGEeI7lnrcZ7OrmbTL-B5NIEAjTl1i3AsHQ9D0Ci_TMpPCBoeu-JZk0J5UzYjaGxwuv4ifSg-k71zr8hD1dz56Su5gfdeRJgHJvVyAOgtLJhGow1NqOMCGdTc_oUlDr3OyR4SX72WQTVFCjjTRBiJISbE58pDRSdk74z4FbNM2qXOMcd4_Z45codSIW-QMTY83QPXafKQ64zjc8VuegyLmbUveK4ql4dOvayE0oDJ3rBnYdb6smbvGH8IU_fDYBFKMMATsYl7pPRLMZMBV5Q41b791Bbq-8AGgx-SpAK-dVG4fqt69VeRBx7T9lPCnVwa3xEzf_orF1w2QhonivNHX7DHgaxTF6qOrQyoa-iRV6HUHXYayTbaRkNIzYLa1ISb7uhXxSIRE7pRGAPIt3coBSGWor0IDZijZVam-hxoj_qa5nGYYeZnsSbWP9vrbbVNAtCfm2JFXJGEo-mYNqltZDrOgvIJ_VnKa4T6b2zhA8HNIUFiIAB8x2fmkz5whZnz_dM1tU_mxrxKrPWLbKfEy0yIlTv2KxzDjtMJ9qYXWzFe3X_HN0h8ISFx8XEWx1yrh1WkxZHa_k8BWmSSSuzssV_6nh9VOUyH6NyCTILJu08UkEII5MB_7iUjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0d5c6577.mp4?token=pzij6QFlnGWsBhgyHIDEck0BEJAHSlC_vxeX1oRdXDcPTxOf9HGEeI7lnrcZ7OrmbTL-B5NIEAjTl1i3AsHQ9D0Ci_TMpPCBoeu-JZk0J5UzYjaGxwuv4ifSg-k71zr8hD1dz56Su5gfdeRJgHJvVyAOgtLJhGow1NqOMCGdTc_oUlDr3OyR4SX72WQTVFCjjTRBiJISbE58pDRSdk74z4FbNM2qXOMcd4_Z45codSIW-QMTY83QPXafKQ64zjc8VuegyLmbUveK4ql4dOvayE0oDJ3rBnYdb6smbvGH8IU_fDYBFKMMATsYl7pPRLMZMBV5Q41b791Bbq-8AGgx-SpAK-dVG4fqt69VeRBx7T9lPCnVwa3xEzf_orF1w2QhonivNHX7DHgaxTF6qOrQyoa-iRV6HUHXYayTbaRkNIzYLa1ISb7uhXxSIRE7pRGAPIt3coBSGWor0IDZijZVam-hxoj_qa5nGYYeZnsSbWP9vrbbVNAtCfm2JFXJGEo-mYNqltZDrOgvIJ_VnKa4T6b2zhA8HNIUFiIAB8x2fmkz5whZnz_dM1tU_mxrxKrPWLbKfEy0yIlTv2KxzDjtMJ9qYXWzFe3X_HN0h8ISFx8XEWx1yrh1WkxZHa_k8BWmSSSuzssV_6nh9VOUyH6NyCTILJu08UkEII5MB_7iUjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/naya_foriraq/79509" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
قاليباف: ألا يفكرون في أنفسهم أنه لو كان لتهديداتهم أي تأثير، لما وصلوا إلى هذه الحالة من اليأس التي هم عليها اليوم؟ نحن لا نعير أي أهمية للتهديدات الأمريكية. ‏عليهم أن يتوخوا الحذر في تصريحاتهم، فقواتنا المسلحة مستعدة للرد بطريقة مختلفة. مهما قالوا، فنحن…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/naya_foriraq/79508" target="_blank">📅 19:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNr4SdOdqhF5HsN9zg6qtLHvnDX4MBQC5oQV11WNoZsLb2BLR6JDGvozEf1SLBcUWfrhwoJriWDZhwPwzq6d5Xovd6Me7DeEC_ipa6NORPP9WqUGaYByehmLgYhxaE9a2nxZSW4vha6gzppgLhJ5fG1dAj2DJO1Z-8Ymx3hr7RVWDCC8jAST_JOG76B26t0bzCx-AtUmoQ-TFAqJztvBxl2YlBLRsZzs4VVOpBH_eoQo6P6xJgUzqYobvSNyIq-b0vcG4KW3qb--QMOEWnNV-qlMMBccTnutkCciU4dptYr1akzdO3U7_XM9tks3sP9EosSf-RI3ZHByW58UMhMTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: الوفد الإيراني يحتج على تهديدات ترامب؛ إيران تدرس خيارات الرد المناسبة.  أعرب الفريق الإيراني المفاوض عن احتجاجه للجانب الأمريكي، وهو يدرس حاليًا خيارات الرد المناسبة على التهديدات اللفظية الأخيرة التي أطلقها دونالد ترامب. وفقًا للمادة…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/naya_foriraq/79507" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: لا يزال من غير الواضح ما إذا كانت المحادثات الرباعية ستستمر أم ستتوقف.</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/79506" target="_blank">📅 19:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79505">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله أكبر
🇮🇷
🌟
مصدر إيراني مطلع: إذا لم تنسحب إسرائيل من لبنان، فسيتم إيقاف جميع المفاوضات. وستدخل إيران مرحلة رد فعل عنيف مع استمرار الاحتلال الإسرائيلي وجرائمه.</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/naya_foriraq/79505" target="_blank">📅 19:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79504">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
🌟
التلفزيون الإيراني: بدأت المحادثات الثنائية بين الوفدين الإيراني والقطري عقب المحادثات الرباعية.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/79504" target="_blank">📅 19:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79503">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: خلافًا لما ورد في بعض وسائل الإعلام الأجنبية، لم تُعقد أي مفاوضات حول الملف النووي خلال الدقائق الثمانين الأولى من المحادثات. ركزت المحادثات على تنفيذ المادة 13 من اتفاق إسلام آباد، مع إيلاء الأولوية لقضية لبنان.</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/79503" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79502">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
حققنا إنجازات عظيمة ولن نتخلى عنها. سنبقى في منطقة الأمن في جنوب لبنان طالما دعت الحاجة. وبالنسبة لإيران، مهما كانت التطورات السياسية، لن أسمح لإيران بالتسلح بأسلحة نووية.</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/79502" target="_blank">📅 18:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79501">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/79501" target="_blank">📅 18:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79500">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
السيناتور الجمهوري غراهام:
لقد أمضيت أربع ساعات ونصف مع الرئيس ترامب يوم الجمعة. إليكم ما أعتقد أنه سيحدث بعد ذلك. إذا فشل هذا الاتفاق، فإن الرئيس ترامب سيسيطر على مضيق هرمز بالقوة.
ستتحكم الولايات المتحدة في مضيق هرمز. وسنفرض رسومًا على جميع الذين يمرون من خلاله لدفع تكاليف العملية.
وسنقوم بتوسيع اتفاقات أبراهام في السنة التقويمية 2026. سنجعل المملكة العربية السعودية تنضم إلى اتفاقات أبراهام.
وإذا اعترضت إيران على سيطرة الولايات المتحدة على مضيق هرمز، فسنقضي عليهم.
إلى الإيرانيين، إذا كنتم تستمعون: عندما تستخدمون حزب الله لمهاجمة إسرائيل، ستكون السياسة الجديدة هي أننا سنهاجم إيران.</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/79500" target="_blank">📅 18:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🌟
مبعوث الولايات المتحدة في الأمم المتحدة:
إن إسرائيل والإمارات العربية المتحدة "عملتا معًا عسكريًا" لـ "الدفاع عن بعضهما البعض" ضد إيران.</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/79499" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79498">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله:
لقد بات واضحًا ومؤكدًا أن جولات التفاوض المباشر التي سيق إليها وفد السلطة اللبنانية إلى واشنطن، ليهز برأسه ويبصم على ما تسطره الإدارة الأميركية من إملاءات تصادر سيادة لبنان، وتنقل موقعه السياسي إلى ضفة المتصالحين مع الاحتلال الصهيوني وكيانه اللقيط.
ليس مأمولًا على الإطلاق أي خير ينجم عن هذه المفاوضات التصالحية، لأن منطلقها خاطئ ومريب وهدفها إذعان واستسلام.
إننا في حزب الله ندين مجددًا نهج التفاوض المباشر مع العدو الصهيوني وجولاته وما ينجم عنها. وندين وظيفتها التعطيلية التي تشكل عثرة في مواجهة مشروع العدو وجهود الميدان المقاوم والتضحيات الكبيرة لشعبنا العظيم، والتي يمكن للسلطة تثميرها والضغط بأوراق القوة هذه، لتحقيق انسحاب كامل وغير مشروط من أرضنا اللبنانية.
إننا نعتبر أن مواصلة الحضور في جلسات التفاوض المباشر هو تنفيذ لأمر اليوم الذي تُصدره الإدارة الأميركية للسلطة اللبنانية، التي تُلبّي متفردة بقرارها وبمعزل، مخالفة للميثاق والدستور والقوانين، وتستجيب لما تعمل له أميركا وإسرائيل في زيادة المخاطر على لبنان واستقراره واستقلاله وسيادته.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/79498" target="_blank">📅 18:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79497">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmVEsNOtmxlBXvv0BARLXZwXz4fvdCxvGNQFR-AT-bxLficnVmH3UhFZ17h8qLBra19317sdoLp7JPZGOJbjyiWWVZgUlEzX-SWItj40qGctAm2jIeJUNP7YmW397B53i3m6qu_qsHm7mrVglXi1ql6wT9aA3yCR-cfuXRYOggn_S_lBU19c9Kpvlm7yxU2dfVhTvnvIfbXQ9CessqN9e19HqQulEnDWTkmLMBTCXv9w7AJc_Ok7OBO-Sp_385cE7CAv8mJSnKwtTGEo0Osp0lyS9BK3sMlml2QHMeLNAw5dgDuqM7L4cFD9yeKnHQiQMlqu29aovrG1k4kbuevpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
حزب الله ينشر:
لن ننسحب من المناطق الأمنية العازلة في لبنان - يسرائيل كاتس</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/79497" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">منظمة UKMTO: حادث على بعد 50 ميلاً بحرياً جنوب شرق مدينة الشحر في اليمن.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/79496" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/79495" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRO4UfjIfucl7vfknGTo_WadG15cs5-LHzJk2cUJ29-SMufxiw5Q1xiR2IecCndaxcrI597QQcnnL-Opf1F9CgBZOaFd4WypPvJfRGSdunB5SxI9TnDAymAGSUq2XpK0vFoP9vDlmJ6GJjIe8DbNiaC_T8-1jaA0LzarDRO4qWvRktaz0VLYg58ILG60I5mqRgodCCpIws0VfpqI2-PMNuMrCveCkjMVyMpBItEyRxx7uWwle1Mm6WVbSpTPqzcRFBQPXGHFju1HfQAtBL13uLqIE5GJlYj6xPMaOl7bHrPMH1Cpu610D8iuAaEIRl9gY6zJcGrFxAW3hZ2cmm_uJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/79494" target="_blank">📅 17:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI-zUPNm4xFq3dAqds0VDYNOaEAIHmWMwVbFaGHr132egM4Mqak20c1iFb36qnp94jP-W32u0nr1SxQBQ5REB4ojrN8syImCBCFouFcIeBdc96eKOnCf3dIiWTrA8-JlvoCBTQUBdeROEfUcgQKUygOHECzW0RGjqEmnGpHESEEJNdQRks46G5ZqKNYWeTuGvwxdFuX0HVC1h-8rNijSdodhk1Xld_oEl3fRgFFcUgqGgd4cevbM--VKjNm8Dbt1AbLt8xFTOMurVFWfiVOFUS91qLWxj7wVTuIdxPzOHkt4RYJ0s3vfW2cc_OR2LFEtS6VUgkfJ6WEc34fSZXdl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
🇺🇸
ترامب:
سيستقيل كير ستارمر من منصب رئيس وزراء المملكة المتحدة. لقد فشل فشلاً ذريعاً في موضوعين مهمين للغاية - الهجرة والطاقة (فتح نفط بحر الشمال!). أتمنى له التوفيق!</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/79493" target="_blank">📅 17:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصدر مقرب من الفريق المفاوض الإيراني: مضيق هرمز لن يفتح دون كبح جماح إسرائيل في لبنان.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/79492" target="_blank">📅 17:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انباء اولية عن تحطم طائرة اسرائيلية في الولايات المتحدة ومقتل طاقمها</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/79491" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
‏
ترامب:
على بزشكيان الالتزام بقواعد اللعبة وإلا سنستولي على إيران.</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/79490" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انباء اولية عن تحطم طائرة اسرائيلية في الولايات المتحدة ومقتل طاقمها</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/79489" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZhGE8ts5VDxzp7BiaZD86KP_j0aSgepsksxlho9RDVsXllgBCgZClLTk-i-efbAA_1qkEkrhOb5H_Up2VHFotzl8-ufPLFsT4fzDvA8c0M407qWkURUsgCYhSMLoh3CQUwUPgL6hNKRbK8eE-LjU1nIYwLuYylc-WEvxPuCzExLwKwSXi2IFY4qzK1iYtxAcpyMsN07Nhg16H8TVrZEJ6EJ1BIhRvlP-8PMsaZyCPcNqRmq5JxBLUoQ8CP2pCiYLMcLx1iBDWdL2lxZm9H8ACblDahHLKUbSf8-Ep-47pggQHhgU7Ok7UkTVEVcs78RycxwonQVty4Kx6hjYd9EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
يجب على إيران أن توقف على الفور وكلائها المدفوع لهم بسخاء في لبنان عن إثارة المشاكل. إذا لم يفعلوا ذلك، فسوف نضرب إيران بقوة شديدة مرة أخرى، تمامًا كما فعلنا الأسبوع الماضي، ولكن بشكل أقوى!!!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79488" target="_blank">📅 17:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79487">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79487" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgdG1-wdCOBUoMhC6QqFSISP-FwN-t41mGNAX_OrwKcZCaB6J_GW5JaOMcmfihpa5PZ57zcPrUeC9TY5SWJ4__ULSYpWGI1WRjEfQwY5snM52q_PD-9valGjxkfiGQreFt3fPJZ9NAj9dmiAq0V6rUXZ3uKrxoiqbgLHm12TYsni5MxwvNzgw8HUOG0u6QS-GK6GnUqmfPz4In2wdDRgBgciAJcM26TcaCSlBXQ-cWOgLFdHgvVwrmr7ycVUA8z0YmkbbS7C2wThb96fW8wG8OJacnxw1VoUg65T1N6RL_UxgPZ02KOqCysLa7ndEnA0OAn0yqTlEIaQS7MI7L_MpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب عن الانهيار الامني الذي تشهده المدن الامريكية بالتزامن مع تنظيم كأس العالم:
هناك الكثير من عمليات القتل تحدث في شيكاغو. 22 شخصًا أصيبوا بالرصاص، و4 قتلى على الأقل. لماذا لا يتصل بي الحاكم بريتزكر لطلب المساعدة؟ يمكنني أن أجعل شيكاغو مدينة آمنة في شهر واحد، وفي عام واحد، ستكون واحدة من أكثر المدن أمانًا!!! لقد تحولت واشنطن العاصمة من واحدة من أسوأ المدن إلى واحدة من أكثر المدن أمانًا في الولايات المتحدة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79486" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79485">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏ترامب يهدد: المفاوضون الإيرانيون لن يعودوا إلى بلادهم إذا أغلقت إيران مضيق هرمز.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79485" target="_blank">📅 16:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🇺🇸
الوفد الإيراني يرفض التقاط صورة مشتركة مع الوفد الأميركي.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79484" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#ترفيهي  ترامب: أمريكا قد تصبح الملاك الحارس لمضيق هرمز وتأخذ 20% من النفط</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79483" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
ترامب: إذا أغلق الإيرانيون مضيق هرمز فسيتم القضاء على بلدهم.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79482" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
ترامب:
إذا أغلق الإيرانيون مضيق هرمز فسيتم القضاء على بلدهم.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79481" target="_blank">📅 16:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فانس:  إن ما يمثله اليوم حقًا هو بداية مفاوضات فنية لن تحل كل خلاف، ولكنها ستسمح لنا بالجلوس معًا كفرق، ولأول مرة في التاريخ، لمعرفة ما يهم الأطراف المعنية أكثر، ولتسوية تلك القضايا، وحل تلك المشكلات، والوصول إلى غد أفضل.  ‏إن سبب وجود القيادة السياسية للدول…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79480" target="_blank">📅 16:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فانس: ترامب ملتزم بتحقيق وقف كامل لإطلاق النار في المنطقة</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/naya_foriraq/79479" target="_blank">📅 16:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فانس: هذه الهدنات دائمًا ما تكون معقدة بعض الشيء.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/79478" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فانس: حثنا ترامب على "طي صفحة الماضي" لإعادة تشكيل العلاقات مع إيران</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/79477" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فانس: هدفنا هو إعادة تشكيل الشرق الأوسط من خلال الدبلوماسية المشتركة</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/79476" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فانس: تم إحراز تقدم كبير في الساعات الأخيرة</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/79475" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/79474" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCFt2XLFVQR6gg6h2FQsEwFc340nibuF8paYuU1ndj3VjZdG_bIbPcBfkiClI0IK0fPw4HdHYtHRIK4_KnSwsTCB6ofmvmKFLwnvH-k7Izs9T6R3GJp8FuqVejFCzx3YkUnMLGV02l1fvH6zwzc97Y09imt3DjPNPmqWC0RwAFaAh_QuV3T2uLByTsSTB5TcXbuSchTUFEY2Y7b4qc63qLbIcXqvTWFSH7oVox3uhj1rcoXtMTyS--9-pzYx2kDEkB32GPAWlopkHJYpLQ-fgmkHJ1R-Xfd73dRWx0ARfadFiA9lecHVf1gi1w7KaBRMS6z7ph5cSDvbdYZqnXkF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/79473" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/79472" target="_blank">📅 16:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-06-2026 آلية هندسية تابعة لجيش العدو الإسرائيلي في أطراف بلدة أرنون جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/79471" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/79470" target="_blank">📅 16:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQpzmUtV_mCiPvwXfPKrNwz5sIk8KRGZ34WYJvhDa5igczdGGTUlz3RhEKDFBnSLXt-DB4qGa804IwvB-FDlqdFLMlZklthJXbgmb7UtpQGjzy_hrQ07nz9efTHvvBs0Xw0Z0Xi_8Jg2dmZ8sdQvssCyzdAdAs78djy1P-eUxoMY4hBDVW7OxLx926RT08XG65ZGj5DSFWtgm9V2UNJgmKc-ZrlQMiCQ6CN_crUiE1y8LfGlsF6BsWFPe2624fyBDLisa9eJsYboeaEnnln6FajrPSuhA4vHaWpEjVheEKBM7_zcR8-BPwLEUuN34T0DMa-TIJK28mrZZY3P7yxmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿ وَلَا تَحْسَبَنَّ الَّذِينَ قُتِلُوا فِي سَبِيلِ اللَّهِ أَمْوَاتًا بَلْ أَحْيَاءٌ عِندَ رَبِّهِمْ يُرْزَقُونَ ﴾
تدعوكم المقاومة الإسلامية في العراق كتائب سيد الشهداء لحضور مناسبة الذكرى السنوية الأولى لاستشهاد القائد الشجاع السيد حيدر الموسوي واستذكار سيرته العطرة ومواقفه المباركة.
حضوركم وفاءٌ لذكراه الطيبة، ورحمةٌ تُهدى إلى روحه الطاهرة.
📅
يوم الاثنين 22/6/2026
🕐
الساعة الخامسة مساءً
📍
بغداد - البنوك - شارع الكنيسة</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/79469" target="_blank">📅 16:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiT8ewQNS14nIts3HcpszNKoUYWLoLlawfnQ_2Iq5d01NYYPdAocPheOoy6yJwnwYo8zecDAhADYvHAhlLRSAjEqOAbvUJHfTwp9DYzhQZOVyR4KDZxXNXrvNfO7jpWFTjvaWDF1EQlI6Q3o8CfbMSOTqdRPrjOWhrZSdPVh7J9HYBVakCPJt5QN6Ah56z8XIGFP9wbJcjkkk3ylBwIOW4hDInTWv-Bjy3-CHtBqvmJN2fVkrlqXTXK7I49par7Xn-drL53rYySQ3AMa29ghs_JZCOehYvO0LG5NJYXqZFWvEVCVVC-6O3VMop0v2sHA1D32z1yve2H8bVCsGoDRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ايران الشيعية
استخدمت مضيق هرمز من أجل شيعة لبنان
برأيك لم لا تستخدم تركيا و(الخليفة اردوغان)
مضيق البسفور من أجل غزة!!</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/79468" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOy7d2Fs0JwfLra41C8mst4CIzPmep_3VjHxlong7WydQAml8d-Z-tQ2LTummghxvAiPhXhI2BT6EjAMMREsL3gEgXQwhKJ4dV-pUER7mxNKmptEQPufTjQkc7ZzSLXdWLWy6BYo0dRWyu_hhBXhAfb7ydarz3BGBuseF6XWbTEypSA0KgA43ovYPyiW9qOlErWChvZUf2y9ocaVDtgp_smabBvsuib1H7uz-Ey702vQJsE6lLCkXE37pjDFDtufz6jOKgJYrPFWx6nVoIhvYxpj74H51HvzkByrhYcdq2JSNrP2c0bjtW7Wn_vB2cMMad1QiUk72jsFYHWNTI5EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اعمدة الدخان تتصاعد بالقرب من سجن بادوش في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79467" target="_blank">📅 15:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79466">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
‏
وزير خارجية باكستان:
أميركا طلبت نقل مخزون إيران النووي وتوصلنا لحل "خفض التخصيب".</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79466" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
مجلس محافظة الأنبار يعفي (رهيب حميد هايس) من إدارة مؤسسة الشهداء في المحافظة اثر خلافات سياسية داخلية داخل المحافظة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79465" target="_blank">📅 15:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3460aaf297.mp4?token=H3UJ8j0zZqbjtnEC9HuuOAs_9L98hbbB0-bOd720DqA_VBUO6IFBZ1O6VqS8-tV1c1yBV_U3ObyaYpbrFwDozwqgrq2hHrmvgLg3gqV-Bupxz12siZASfCko0Qiq1CSdWW-aEdmmYglkZZERbBbaIgwlg7hBfGR4T2SFXwHbamNnWNdF9ndX8Myws4H72c8YGEt9GDvo7bO3k3gtFlgak6ce9gJyi7EcnsAKXcwf__11lXLb5tS5gEvvVd1oxFE0C1xOY2MfMVrD1BkHj5KehUJ5V9nTCWI8CqcIEkEEG1J_AQZaM9to3PZ4imBByx9mLi2CRdiGZTK4hmB88APzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3460aaf297.mp4?token=H3UJ8j0zZqbjtnEC9HuuOAs_9L98hbbB0-bOd720DqA_VBUO6IFBZ1O6VqS8-tV1c1yBV_U3ObyaYpbrFwDozwqgrq2hHrmvgLg3gqV-Bupxz12siZASfCko0Qiq1CSdWW-aEdmmYglkZZERbBbaIgwlg7hBfGR4T2SFXwHbamNnWNdF9ndX8Myws4H72c8YGEt9GDvo7bO3k3gtFlgak6ce9gJyi7EcnsAKXcwf__11lXLb5tS5gEvvVd1oxFE0C1xOY2MfMVrD1BkHj5KehUJ5V9nTCWI8CqcIEkEEG1J_AQZaM9to3PZ4imBByx9mLi2CRdiGZTK4hmB88APzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دهوك ضمن اقليم كردستان العراق قرب احدى المستشفيات اثر مشاجرة عنيفة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79464" target="_blank">📅 15:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
محافظة بابل تقرر تقليص ساعات الدوام الرسمي إلى الساعة الواحدة ظهراً في دوائر المحافظة إعتباراً من يوم الأثنين الموافق 2026/6/22 ولغاية نهاية الدوام الرسمي ليوم الأربعاء الموافق 2026/6/24 لغرض فسح المجال امام المعزين والمواكب الحسينية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79463" target="_blank">📅 15:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10626f3f5b.mp4?token=bLfy2zwVzyoErAOX4QF0mK-5FE1i5cEZ7rfBuhFEdAKbeOei-SDTLypAfrneQF_L6CcM0qKdusr8Ynabojs-meTdzxyk-GlAFb3dQskXLZeKirpLe7I2puUEPz8Zqm-JppKAOvU_BDRzJRW5Gd8pFjC_7YVDx0H-qGFNizvnX3OLAwFYIhIm2kgTzv0MvB9Eq1wsKJO29Fhzh-OThEYfYl3R7zF1PpFC6V6lGJu71KFvZF_YFv1pB132r9XylO5qojQncLo4aMuTpnI4LALRunLm-e36kQMoX0M-PoAamNJcQbfpk205UWpiF5cEuvBvW3ukEpo8QkQltYQw8r7fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10626f3f5b.mp4?token=bLfy2zwVzyoErAOX4QF0mK-5FE1i5cEZ7rfBuhFEdAKbeOei-SDTLypAfrneQF_L6CcM0qKdusr8Ynabojs-meTdzxyk-GlAFb3dQskXLZeKirpLe7I2puUEPz8Zqm-JppKAOvU_BDRzJRW5Gd8pFjC_7YVDx0H-qGFNizvnX3OLAwFYIhIm2kgTzv0MvB9Eq1wsKJO29Fhzh-OThEYfYl3R7zF1PpFC6V6lGJu71KFvZF_YFv1pB132r9XylO5qojQncLo4aMuTpnI4LALRunLm-e36kQMoX0M-PoAamNJcQbfpk205UWpiF5cEuvBvW3ukEpo8QkQltYQw8r7fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قاليباف ينشر مع بدأ المفاوضات</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79462" target="_blank">📅 14:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcfQNDZqDt4HmBt1OIaNgUh-uz7OQIMGi9iEvhEQ0WdEo-EgNp-zkth92YxlAXfzYyrppe5sq1_hZlTKOesNUeMQKTNyHdm6-qFHr9VIhAW0VxpWiic1XK1ROi-b_hcTsP_yXMRsKlqfkgTJrKaveMjRr7Vl_faAKeLUUk_lc9yK57p1LM51qm-QC94dH5xNZ8pUR4TcpY0SMNau7Twy59tv6YHUu3PDt_lxv_cIHKlhGpRpMTrw0tf_LuPTE6uYRU-qGa67JWlsyhnDiAoJjcVdBPAD8demKAQDEV-YJ1jpNnsaz9KYtVSbwmxNxm9fGr_RF1KwtePOGFfEdMfeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضيحة تهز إقليم كردستان العراق..
ضبط رجل الدين السلفي البارز وأستاذ جامعة السليمانية (عبد اللطيف أحمد) متلبسا بإقامة علاقات جنسية مع طالبات قام باستدراجهن.
أكثر من 10 طالبات أخريات ضحايا له تقدمن بدعاوى قضائية ضده بعد إحالته إلى القضاء للتحقيق في القضية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79461" target="_blank">📅 14:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🫡
خلية الاعلام الامني العراقية:
في تمام الساعة 02:00 والساعة 02:20 من هذا اليوم، تم تنفيذ ضربتين جويتين ناجحتين على مضافةٍ لعصابات داعش الإرهابية في مناطق مترامية في عمق صحراء محافظة الأنبار. ​وقد خرجت قوةٌ مشتركة من أبطال الفرقة الخامسة والصنوف الساندة بإمرة قائد الفرقة لتفتيش المكان المستهدف. وسنوافيكم بالتفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79460" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
مجلس محافظة ذي قار يعلن تعطيل الدوام الرسمي يوم الثلاثاء تزامناً مع ذكرى استشهاد الإمام أبي الفضل العباس (عليه السلام).</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79459" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79458">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
وكالة مهر:
اجتماع سويسرا سيناقش 5 بنود من الاتفاقية من بينها بند وقف إطلاق النار الشامل في لبنان وبند الأموال المجمدة لإيران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79458" target="_blank">📅 14:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
في السابق، كانوا يقولون إنه يجب التفاوض بشأن صواريخ إيران أيضاً؛ لكنهم الآن يقولون إنه كما تمتلك الدول الأخرى صواريخ، يجب أن تمتلك إيران أيضاً صواريخ باليستية. القاعدة تغيرت</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79457" target="_blank">📅 13:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
- تحذر مصادر في الجيش الإسرائيلي من وجود عدد من الحالات الأخيرة التي ركز فيها حزب الله على استهداف كبار قادة الجيش الإسرائيلي الميدانيين في جنوب لبنان، وهو ما يثير مخاوف جدية ويتطلب تغييرًا في أنماط العمليات.
- يُقدّر الجيش الإسرائيلي أن حزب الله قد أعاد إنشاء نظام مراقبة وجمع معلومات استخباراتية مقابل الخط الأصفر في جنوب لبنان، وأنه يشن عمليات ليلية لتحديد مواقع القيادة العليا في الميدان وشن هجمات.
- يقول مسؤولون عسكريون أنه لا يمكن تجاهل حقيقة إصابة قائد سابق للواء 401 بجروح خطيرة جراء هجوم جوي بطائرة مسيرة، وإصابة نائب قائد الفرقة 36 بعبوة ناسفة، ومقتل قائد الكتيبة 52 في هجوم جوي بطائرة مسيرة، ويجب الأخذ في الاعتبار أن حزب الله يستخدم التكنولوجيا، لا سيما ليلاً، لرصد النشاط اللاسلكي والإشارات الدالة على وجود قيادة عليا في الميدان. وأضاف المسؤولون أن هذه الجهود تتطلب مستوى عالٍ من المهارة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79456" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
المتحدث باسم الحكومة العراقية: استكمال الكابنية الوزارية سيكون في النصف الأول من تموز المقبل أي قبل زيارة واشنطن.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79455" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌟
المتحدث باسم الحكومة العراقية:
استكمال الكابنية الوزارية سيكون في النصف الأول من تموز المقبل أي قبل زيارة واشنطن.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79454" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZh3fznDi33Fi9vlWmwFPjCodsYTxFtnDpVwRz_J1SYgI2D_yksTmGFUWA5QeE55r2KkpVWENjCbO0svav-UoB20cx8Rj7Bc_vqT1vz75Ra4YQV08W_Qkv9qRCBTwSWfhc-41i6LbHIS7YRGTWxL6r5DCedKDF3ZMbcV33sWZDY3hnH53A4Aoa7QOp5tfxJv1A-KH2LGwHF-VBhHNweI1cI1RSBIk8YJl22xaCjbvtE1aBkeS_CG_MFJbYFO1NPd43BOhxysxBzlCpu0yPyyW1Ua_rcEaOYsLNc4rC2MQ5hgQFRbBSqH0rAMTwMR4xNh6OLRo4URiXBAJc82mbBjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
رسالة نائب قائد كتيبة 52 في جيش العدو بعد الكارثة التي حلت بهم على يد حزب الله:
كانت الأيام القليلة الماضية من أصعب الأيام التي مرت بها الكتيبة. فقدنا قائد كتيبتنا وجنودًا أعزاء سقطوا في المعركة. الألم عظيم، والفراغ هائل، وقلوبنا مع عائلاتهم المفجوعة.
رغم الألم، أنجزنا أهم مهمة ممكنة - إعادة رفاقنا إلى ديارهم. بعد جهد كبير وفي ظل ظروف صعبة، تمكنا من إنقاذ القتلى من ساحة المعركة ونقلهم لدفنهم في إسرائيل
اليوم سنرافقهم في رحلتهم الأخيرة. سنقف شامخين، ونحني رؤوسنا إجلالاً لذكراهم، ونضمن أن يظل إرثهم وروحهم ومثالهم نبراساً لنا.
هذه لحظة حداد، ولكنها أيضاً لحظة وحدة. الكتيبة قوية، والمهمة مستمرة، وسنواصل القتال بكل قوتنا، بمسؤولية ومهنية وشجاعة - حتى يتم إيقافنا، وللمدة التي تتطلبها كل مهمة!
أيها العائلات العزيزة،
في هذه الأيام، أنتم أيضاً تحملون عبء المعركة على عاتقكم. إلى جانب المقاتلين والقادة على الخطوط الأمامية، تواجهون القلق وعدم اليقين والتوتر المستمر. نيابةً عن قادة الكتائب والجنود، أود أن أقول لكم شكراً. شكراً لكم على صمودكم وإيمانكم ودعمكم وقوتكم التي تمنحونها لأحبائكم كل يوم. أنتم جزء لا يتجزأ من
من عائلة الصغار وقدرتنا على إنجاز مهامنا حتى في أصعب اللحظات.
"سنعود من مهمتنا مرفوعي الرأس، بعد معارك دامية."</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79453" target="_blank">📅 13:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
‏
الرئيس الإيراني مسعود بزشكيان:
لن نتخلى عن حق تخصيب اليورانيوم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79452" target="_blank">📅 13:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCZDP9cvt-PxZOKWruB5r6CbvsarqMxzYaatTEWaWceAilI1k5uaLHoWzqPZ21CUGG2hDO5wEOWBjs6JlvT4VaUEmpq22rWYvldcq4eCX1R0aeTRJJVie_WxLr5s_6Gw01xv4ZWRf_R0bFv6WN4bOK56-ks8Ppvkroifc0fBa8MwtyxIBzoD6xJKeXh_Dfjpawvkh_sB2iNADobYwiQijyl63g2ak4s-1B6AHdIePIepZqaE07_QtxqKyXBUp9Fa-5XmfUoG5pzqBeZSnqBEq95vC0nVErq4bYQi6Z-5wDYzLZ9JXSpmvA6LXNTKRCL75Wv2FWfPgjDZ3PccJYTm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🌟
مطار بن غورين يشهد إخلاء طائرات التزود بالوقود وتوزيعها على قواعد سلاح الجو في الكيان المحتل حيث تبقى طائرة واحدة في  الساحة الغربية لمطار بن غوريون</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79451" target="_blank">📅 12:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
هارتس العبرية: نتنياهو أمام معضلة، إما البقاء في جنوب لبنان والمخاطرة بجنوده وبالعلاقة مع ترامب، أو الانسحاب وتلقي هزيمة في مشروع حياته.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79450" target="_blank">📅 12:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNeoX7vjSlUboH0k1EEzHnxTHti2F3TSlXvnWuy3bkiX8U3KONZnufiLX4gf0wyHd2CYc3nHxvFxKXvkJo0lboJ7SC6-1xf7grXJ3yIdhxnoEIl6H72NI_Mu8HsmmlzcyEoMtil-tWV4OdHKmxja3VfkFv_X8Hn0Qdgzdjd-7g-2zR6aBJfpQnwvzs_fq_LPeBtoidHujIf2YNofPs5m1p8ikHxYLTGa4ztMHW2P8_ikP9HKF7VmZUfseB2_dq1a5evZDmat65Hl1lWQPUf_yWJXttckgZxberc-Q9snlNw6sIGQ-BqtYF6FvsXwtwXhrD1_q2YrlQ2vAEHE9XBmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يراد منه دثر إسم قوات
الحشد الشعبي العراقية
تدريجيا من الذاكرة العراقية
الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79449" target="_blank">📅 12:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79448" target="_blank">📅 11:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقتل اسرائيلين اثنين بظروف غامضة في لوس أنجلوس</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79447" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79446" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f73573e0.mp4?token=XtkGceT6u0d-uFywNuDiA5CG8TviS4eNiCZ09rtNGWZtiXSzeIjMPel7pfd4UmgckZhjn-JDem_viF7ymcRsIE3G_IXqEZNx24DoXUPNZDIYCgLgBoPMyxQhkcfu4ojZxcZ4kB0_4B36sFOUwO1-KiCcAoYCm3jE8C_NstxePxQuTS-DgpnST1mu28uYpOc1qzymqSm8F1xUOPQxG8wSFEouwsb6bBpFpoxyO4IYv-VavzBhPBvvFBD6AvDkVMrgj5iCtmdNytT4Nrlz--T5uZ-wnByipjhQ__UY5SI4bF5oZ-pbcAqbnY1alnMomjOZzyCPPBCkxN0jNtoHFQKGyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f73573e0.mp4?token=XtkGceT6u0d-uFywNuDiA5CG8TviS4eNiCZ09rtNGWZtiXSzeIjMPel7pfd4UmgckZhjn-JDem_viF7ymcRsIE3G_IXqEZNx24DoXUPNZDIYCgLgBoPMyxQhkcfu4ojZxcZ4kB0_4B36sFOUwO1-KiCcAoYCm3jE8C_NstxePxQuTS-DgpnST1mu28uYpOc1qzymqSm8F1xUOPQxG8wSFEouwsb6bBpFpoxyO4IYv-VavzBhPBvvFBD6AvDkVMrgj5iCtmdNytT4Nrlz--T5uZ-wnByipjhQ__UY5SI4bF5oZ-pbcAqbnY1alnMomjOZzyCPPBCkxN0jNtoHFQKGyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بث مباشر لتوقف حركة السفن التجارية في مضيق هرمز بعد إعلان إيران لوقف المضيق يوم أمس.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79445" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d381d8e4f.mp4?token=ZfQFhMFae7Sm3yQAiIAyPfDZc2L5lrjXAOp2EcT3FZKca-KLErYYm9JC-cGxrNsg_glXRnpD7EOQPYWEvkpmoTe6u2NOhF0yA5bIcsRQqPR9YQhj0tHPqCfgOyK0md8rRs7hShbGs8j7KR9OUHhu5CoKL14_ZP0hVZbJmDTFOzI9rEi3FGAmvEGnCZIrtPS9_xfLz6nROUDgXzBY_1QdT2INk5JHQGjDl4Y6Zi4qtgZMFMQN0A9LcgxirSnGhN8WE4TcFMUUK1B5JxNzar2nVttk_I5MyYRCej3DlWH-31Y7y7J4-Q_-OB2iGTcsNVWccfZNg2dhjavjlZvjEPztYiE3QRDuz0NzID75gan176eLaKD2af9tbIyMIKM4wQjV8H5wDnwFcw3hC-YYFNuaQZHVQeGJlOF1pnwvlg3TbNWHHur4IE2zj-UgwAb0zD-lhLvov3MMZgSEXIjZMVeEmwwWLU9SNQ7kirZxDJ-m6Xfdn8aThYHukSNi-C4ifklPg_rS6oH_eBwC6WSwSo8duS9wWowfkcQMKv4dEhFb0cuiqTBbB39UV6DgJ48LRe44XHAr7JbNGi7a28vzfdv-HRVGSuMwhcYYRxOjeus4dmDRyp2hX9t8VZtfkIHDF7X8uiVWWdN_OiQhaGQ9efy5NYCE1oYgGbwUHCOiR4w1C30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d381d8e4f.mp4?token=ZfQFhMFae7Sm3yQAiIAyPfDZc2L5lrjXAOp2EcT3FZKca-KLErYYm9JC-cGxrNsg_glXRnpD7EOQPYWEvkpmoTe6u2NOhF0yA5bIcsRQqPR9YQhj0tHPqCfgOyK0md8rRs7hShbGs8j7KR9OUHhu5CoKL14_ZP0hVZbJmDTFOzI9rEi3FGAmvEGnCZIrtPS9_xfLz6nROUDgXzBY_1QdT2INk5JHQGjDl4Y6Zi4qtgZMFMQN0A9LcgxirSnGhN8WE4TcFMUUK1B5JxNzar2nVttk_I5MyYRCej3DlWH-31Y7y7J4-Q_-OB2iGTcsNVWccfZNg2dhjavjlZvjEPztYiE3QRDuz0NzID75gan176eLaKD2af9tbIyMIKM4wQjV8H5wDnwFcw3hC-YYFNuaQZHVQeGJlOF1pnwvlg3TbNWHHur4IE2zj-UgwAb0zD-lhLvov3MMZgSEXIjZMVeEmwwWLU9SNQ7kirZxDJ-m6Xfdn8aThYHukSNi-C4ifklPg_rS6oH_eBwC6WSwSo8duS9wWowfkcQMKv4dEhFb0cuiqTBbB39UV6DgJ48LRe44XHAr7JbNGi7a28vzfdv-HRVGSuMwhcYYRxOjeus4dmDRyp2hX9t8VZtfkIHDF7X8uiVWWdN_OiQhaGQ9efy5NYCE1oYgGbwUHCOiR4w1C30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79444" target="_blank">📅 10:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
مصادر:
الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79443" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🍅
الأردن: محاولة تسلل إلى المنطقة العسكرية الشمالية الحدودية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79441" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79440">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbff44506.mp4?token=L2oiussQTp6dtTc4M3H5PL2cMpXR-SG50c3VVoNGpSbJ3ePgV1lX5RJanUj-ua0J9UfPgNAUxLd-rUGzNvEGyeacMpERBYLmgloCFU-4QS94Uy40l4smEWQ1Uk3n-wWo2-oJwEvVCZaOQBl7Yp5hEswxlpQV04-OwkUsJvjrOiZVPCtPe7ajyCEwP1TU0S10C4G_Kii0UtFjrErn9FpH1GrSw0QzoWkY9Sy3ht-29TNwY4-va6WupdnW3qa1obl4Zt_Zy4SbpArX7cdvfN0bF9fS8AUg-p5uU3XQBEyj6gYWX9K_tRI9-brAkmFTlFiKTesppdlFesIM-FgtU4M19Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbff44506.mp4?token=L2oiussQTp6dtTc4M3H5PL2cMpXR-SG50c3VVoNGpSbJ3ePgV1lX5RJanUj-ua0J9UfPgNAUxLd-rUGzNvEGyeacMpERBYLmgloCFU-4QS94Uy40l4smEWQ1Uk3n-wWo2-oJwEvVCZaOQBl7Yp5hEswxlpQV04-OwkUsJvjrOiZVPCtPe7ajyCEwP1TU0S10C4G_Kii0UtFjrErn9FpH1GrSw0QzoWkY9Sy3ht-29TNwY4-va6WupdnW3qa1obl4Zt_Zy4SbpArX7cdvfN0bF9fS8AUg-p5uU3XQBEyj6gYWX9K_tRI9-brAkmFTlFiKTesppdlFesIM-FgtU4M19Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قائد الجيش الباكستاني عاصم منير ورئيس الوزراء شهباز شريف يصلون إلى سويسرا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79440" target="_blank">📅 09:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/79439" target="_blank">📅 01:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
وزير داخلية إقليم كوردستان العراق:
أربيل وبغداد اتفقتا على توفير ضمانات أمنية لحقول النفط بهدف استئناف الإنتاج والتصدير، استجابةً لمطالب الشركات بعد الهجمات التي استهدفت الحقول مؤخراً.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/79438" target="_blank">📅 00:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMX6789EgcvgspE1f-FJ9JR1rnZedJnzvcbWvbHOJhm0PhhvJUTZ8GrcnLrKeAjpGEy8zD6QIrBzun_DKWEIzbLddRDu5yGmR6l-gc34HvcogBnXNh1FsCdZB5MPHIMGM85OwMkrhWwe7Cg5HRmTTzq2WZLDBqmLcFjCa18nO7cd0-13J1rg53GDX2hpvE9EjC1TiMPOCCuvxDxGA850_Qvx5fATlBknNDOe-aAZZYazO62046jPi-f3t3OryjKuo9LQgB0ukJ3Um4OLKrZ9RuVlPGcVMPDbNJ1UEbsl3yzLWbenPBphC7aE8jBTfB7Ky5l1RoXqYhWPowOZrFXx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/79437" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79436">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y13_jXSfcMXA3EusaKL8GjlAdh7XOa_41BF60PxbVlSdsCIptwjC5xAC38SYacsU7hG1LCLbZvfUaRgJJI2hpSucBve170A2-GncH4MPirfgFTBQoWqRl2sgXUvId8eEPrIXP4vV_KyUXsFjzkeG2tGIOF6Y4BAAxdqpdw8bE4lsUE4vR0pJX-zqEI-Z3awYBhFEt122b_I5PeKhx65MqV6oJIY4Nkh_CEdXTvX8c9OrmzwTWurZia6irCzhAqmj9pAfi5hBYrCAB-wn-gwDveLMrwTloWnLbKchf3zBb-lI-FRSPGSKHbO4xennOnrwmxc8HIl83XTVrliVnuy1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/79436" target="_blank">📅 00:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79435">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=NukIPZZ0QJKrc-4MC423MZTy2h97eeE9FaQOFRp5dvmdzllh6eWMzPjXiob8OA4Z0uDrhubEB3ekr3aXoVomhPgQCqeHOEBjvxez0XhUkfl7HP6qd-LDzeljLWZZ8QMhKIBp42K4HaH-65rIZYyPXUwGMrfTXuKlEK-TwkQhhz96XDqPpwct7knLrGBcWi_veLVJxw-P1TW1LGyp0NY8blVeco5sxNV3lIq1-Mc9r8qnDA4CekVebacFiZh51bd-zubVADv9eDdhKsEcIIC_XQYAXH_wBTMDBtWjZ2nE5-2_aaVwTA49MCXO4ufx82HeODYaiMD6VrBSwTVEudUx_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=NukIPZZ0QJKrc-4MC423MZTy2h97eeE9FaQOFRp5dvmdzllh6eWMzPjXiob8OA4Z0uDrhubEB3ekr3aXoVomhPgQCqeHOEBjvxez0XhUkfl7HP6qd-LDzeljLWZZ8QMhKIBp42K4HaH-65rIZYyPXUwGMrfTXuKlEK-TwkQhhz96XDqPpwct7knLrGBcWi_veLVJxw-P1TW1LGyp0NY8blVeco5sxNV3lIq1-Mc9r8qnDA4CekVebacFiZh51bd-zubVADv9eDdhKsEcIIC_XQYAXH_wBTMDBtWjZ2nE5-2_aaVwTA49MCXO4ufx82HeODYaiMD6VrBSwTVEudUx_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79435" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=l2C4vdahkc3jJnWFnYI6bgwY70YYM3sePwTF9ehMzOOWYu0yZaaV60qm5AvOpiUBUmQ0LYjZ0Pkws6TJ8_V2h9u1QUOX0g6xEtir0SppNXl8pZSxncL-UVMoYur8LRYx-Lwe-0kyHEyhNMAQpK1Z1sBDSCJO1HBGobMd84CjewaOAIxnxDdkEatHso2CDI7zCOaoyBa3Px4g6iLZ-_Vc3W2IFXZZ3sznnRsFp_11LoGiTKL8kVualWv8tpDEOlW9l0zwsdpi924kBiORxyjykARoqPs4QODvWUUQXA_T4tAUc7ap7pik6PwuwCP1H1XtPO0AnhClDrXDwXbRQzJJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=l2C4vdahkc3jJnWFnYI6bgwY70YYM3sePwTF9ehMzOOWYu0yZaaV60qm5AvOpiUBUmQ0LYjZ0Pkws6TJ8_V2h9u1QUOX0g6xEtir0SppNXl8pZSxncL-UVMoYur8LRYx-Lwe-0kyHEyhNMAQpK1Z1sBDSCJO1HBGobMd84CjewaOAIxnxDdkEatHso2CDI7zCOaoyBa3Px4g6iLZ-_Vc3W2IFXZZ3sznnRsFp_11LoGiTKL8kVualWv8tpDEOlW9l0zwsdpi924kBiORxyjykARoqPs4QODvWUUQXA_T4tAUc7ap7pik6PwuwCP1H1XtPO0AnhClDrXDwXbRQzJJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فانس يغادر واشنطن متوجهاً إلى سويسرا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79434" target="_blank">📅 00:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79433">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
مجلس الوزراء يقرر تعطيل الدوام الرسمي في  الوزارات والمؤسسات الحكومية كافة، يوم الخميس الموافق 25 حزيران الجاري، تزامنًا مع إحياء العاشر من محرم الحرام، ذكرى استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79433" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79432">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
تعطيل دوام الرسمي ليومي الاربعاء والخميس في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79432" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79431" target="_blank">📅 23:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duPrOGpr0-wL6OR4PV8YbJoiIgS4656qa404Bafw0Ps-GKKQ-fHljQ8ti_XVIdgDkKy3wRdttRuhFUTgZ3bf949OeWM1VNVvp3fXS6whiO5javNo8y4GEYR7plme-QF5ncQame5yfnyee-ddgDsoSKoxr02rmaPazgqoZpf0zI5gcs9LsL2AfCVJUDe5nYJCTKhY4HS_1KSI2xqbqMmk0bOALk-GlJnVtQYO5AUhp6iys91ivKyoMLO8uuqaWMvkzL9u8w42_NQw49m2scgxPKUJuzSJqGHnZmICjX_QcVbMbI1htqMhgcGcg4NZDMy3K7lrf1tKWKl_TP4D1GVNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الصحافة الإيرانية من اجل لبنان اغلقنا هرمز .</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79430" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeMNwC-ZcO9Thn_dKXjRYDhmDoEtchoRk-Do40bhPD0y6SONg8qMijVM-L8kUgjbFQVGvG7kqBoUY0LoS1V1oKdiUDcoFYK16BJ2-Ge5DjtVy0beM_9pFbCa4CyxOuNJ684AyfMu8Qte5dE6mhGaRlBRS3ohMfEtodUrecdwQYAxZXLcDJ_lHeIdpH9kbS31AUI6LpK5hyzZ6gfQxeAFd23TdZQGhcCqrD4SGwRqXJkkZzVP1kpuq1BKB7-WdgtN2tQvXvuPvya2NaRVxH8_qIZgW_Rp-I-HBDUA8rQNc7WFDzGmafd8j73jEc2g0r-NZnTi4MDm-ClS46h8g0Hzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب
: يجب أن تفرض الولايات المتحدة رسوم المرور على مضيق هرمز ولصالحها.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79429" target="_blank">📅 22:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsUf1mhl5QolxYB_Z7j2g_kSjXbsnlTiTtDnkRbaZ4IMmqJV9TjHi_OOftqB10El4OukmroJbDsLpsc51EJZsz8GXM3ySHzoaaVYr5XoEaK8IHl-A7kEc90Ebp5rZnxMq01iFscZezOTd5OtzuVo8YP2BkdKSzeB5nVhdNfo4CC_zWa0niU-0nkGHS3Zm-uncUZA-ymLv8O-rRLNFPW9dhTk8MURT6XfspPKsduV9lSQJN5wUHXpOrNhDz8a7fGZGPJa6rY8NO8pnxufYNkFBeXOsI_FRHNK28tEQXLMZNxOUj1Ee3jYN4KNu8AJMnkwSU9diNf7_IpjAihkd2HYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e54NjEa5-lsZ9HxsDg33pJSd0CIQJXthBDmmzMKiuJEoFZNY_P8qFpGONdYOBxd-jKrr3lKYifmSUViuVVC1jjEK8TwiJWSvL_6jdRMJyqH6MlOXiSHs_vYlvKqx5sWlmZP7VYgAiTZ_lD0oohmONoMp5UNpQnX6H_Hua3fj14veDN3zLMxCRsvnl-w8t3-yPFvbNSa81mgbWFnScGvnlPOMblGleK_ys3EMYWYc7ds6pMkqTu83jABOmlUO-RCn4KXp0TO20H48_dtULViiflhube-ArdlYhzOq2816gTfYAuTviR7smvJQBr-Kyv9BA9d6i4CYlvssX7kUbP_jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZVfYACADigP2MebITN_sfVDuIn-VIk37oSRQTZKhDdpCYvUTbrRL6dYkQ-3QGbzRE3J-ZbCiIKbjZT4wq0mkhhZWaK6mcqdeBCRsBPkkUHG4uefBYZv9U2ZmWHtkXh5Awv8U2RTyiZHfJwZJ28TgHb3t8V_gY7CuH1CDeskaQcctFv4NOl6s5REHnkCGzH8vNKOtp0ovGe7KgOMKeiD_LLiCA3vCahtMbvhF_fl3GnE8AJ0jpAXLQ1-bqp9NvCXxZcJHS3muLau7pHqxIjCy0sf_LcJQpWLAzg8oR_MCyUbxkDoKtwrFHyYVPa23QYT0Rwe89-afc7ny8jwuwEtlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/79426" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79425" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79424" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
حزب الله:
لَن نَخشاكُم ولَن ننكَسِر... قطعًا إنّا غدًا ننتصِر.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79423" target="_blank">📅 21:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79422" target="_blank">📅 21:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79421" target="_blank">📅 21:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J49j2sVvuX7AlUBCDtXlENbpzEKdXYCmqo7T2ezyh7kDmLB6iXgy4xpr4emrGhdE6Y-tAV2tIua6LDuMMVUBmLMY2V4terkqEbb_T6BvxXBjJunOXJNgJ1Uke6kp6heQXn8rLOGrNnKCSlpm9dKbuc_a1fISFcUQi4679Ij5EHqyuMNVvsnztCaSZFh30rx0_6ZkHCuRcGtHknHCcmur_Yns40QNzmQYsp7QohPvCifMfbr_Bskl_SoGV6_tU8Ed6z0tT20wdrU83YPLarkjSTN64GkvrIDdZsYJYryNShlaFtBTk5fpDYT_RbMIhAlTYCY_zLBIBWb_LkocfDbt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله..
جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79420" target="_blank">📅 21:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة كربلاء المقدسة تعلن تعطيل الدوام الرسمي يوم الخميس المقبل الموافق التاسع من محرم الحرام.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79419" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=CSQBuzcH3_Q3NhvRmiwM2sb_BAtU_lY0ZeUgrL6_FcKOyOfz4Q-1VWzrPUWsO480JeuB0ldBTPHJPk4xZCtm7bnzUVehIoi9AZGEYxOoS-M2EKUyLhY0KOHYOOVvftgvwfhJk4Lyx-hCc891QGUdvVSCYrGc5wccNvrzCh4kB3d4Wenx2uzxtKUoWSGme1r0fnHoh0De5ge85Kimdt2XUPW_byzM5wqr9Fkhv-tKt3mLPoEFCYZvR1T3uVM6Pujsjm7GbyGvBuSjqH3J--q_OP_bHmcWiJ3UAsiGWUlB4FIhUeYbOv51npv8f1CyXIqf5iUBx9ngFBBeEY1UmAz27FZcya16SEVs0i0KQ1HD8lu61kMlC-Z9xw50wgv3ovyIQZoJS6bUGH7OZBd68MQ2As6MXhYUTFsSNn4S9EBJ5yyHDlK0u_VHMmAWdUtfSYTyS8ElklR-aB4gKJpbUexqxUr4yTbd6MF0h2QbKm_6auzSqjHhUkJ8UXS-l-adEnJ0gpgmU35N2fYMxSYfNpDCuVj9lNHwcoZkicgUTjHIUxjpvbyv2mp-NP9GdXcparVVGA8epgDmu5reYnequnP9airMU-crJqtSF2WcUWN5_v7nlOWl3D-3sPBcxa6hHHdpOonV3fz0WTKx6JGo0beGYKnY70v1DLr8izFaf4s1VKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=CSQBuzcH3_Q3NhvRmiwM2sb_BAtU_lY0ZeUgrL6_FcKOyOfz4Q-1VWzrPUWsO480JeuB0ldBTPHJPk4xZCtm7bnzUVehIoi9AZGEYxOoS-M2EKUyLhY0KOHYOOVvftgvwfhJk4Lyx-hCc891QGUdvVSCYrGc5wccNvrzCh4kB3d4Wenx2uzxtKUoWSGme1r0fnHoh0De5ge85Kimdt2XUPW_byzM5wqr9Fkhv-tKt3mLPoEFCYZvR1T3uVM6Pujsjm7GbyGvBuSjqH3J--q_OP_bHmcWiJ3UAsiGWUlB4FIhUeYbOv51npv8f1CyXIqf5iUBx9ngFBBeEY1UmAz27FZcya16SEVs0i0KQ1HD8lu61kMlC-Z9xw50wgv3ovyIQZoJS6bUGH7OZBd68MQ2As6MXhYUTFsSNn4S9EBJ5yyHDlK0u_VHMmAWdUtfSYTyS8ElklR-aB4gKJpbUexqxUr4yTbd6MF0h2QbKm_6auzSqjHhUkJ8UXS-l-adEnJ0gpgmU35N2fYMxSYfNpDCuVj9lNHwcoZkicgUTjHIUxjpvbyv2mp-NP9GdXcparVVGA8epgDmu5reYnequnP9airMU-crJqtSF2WcUWN5_v7nlOWl3D-3sPBcxa6hHHdpOonV3fz0WTKx6JGo0beGYKnY70v1DLr8izFaf4s1VKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
جرافة (D9) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة
#أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79418" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79417">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭐️
بلومبرغ:
‏قال الرئيس دونالد ترامب إن احتمال انهيار الاقتصاد العالمي كان سبباً رئيسياً لتوقيعه اتفاق سلام مؤقت مع إيران. ويكشف هذا الاعتراف عن نقطة ضعف رئيسية للولايات المتحدة قبيل الجولة المقبلة من المحادثات مع طهران.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79417" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=Eev7UMbPaZsCKlyCUVvbgXQbdPLAjz-4NwO6IJTOX2uNhTeXYutfz0gxrUey0C-0fZE287VDViQas5mPHHG0UNRy6tUdnHXgMGN89lphvHJkrgenveq-k7n10gOPp2LoC57QMnfn8lxUMh-8FDzW6s-RppHrNBrCH6dGoMsNn02BCGnp1wwQ8no9Gb4oBmYdtdpj068LrFmzhmMVSPFtyx_aV_UXPSSUvpjW1PgjGjiC1pkLUC713DY_X-tJRLylSKT9qfftLmhnIIc33_k5R24UAUKlk4i8QVbDTvG8eHZJ36Fuh4k0GsfPkDxiNhw6XerU9IgbO53pVMyVy7gLIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=Eev7UMbPaZsCKlyCUVvbgXQbdPLAjz-4NwO6IJTOX2uNhTeXYutfz0gxrUey0C-0fZE287VDViQas5mPHHG0UNRy6tUdnHXgMGN89lphvHJkrgenveq-k7n10gOPp2LoC57QMnfn8lxUMh-8FDzW6s-RppHrNBrCH6dGoMsNn02BCGnp1wwQ8no9Gb4oBmYdtdpj068LrFmzhmMVSPFtyx_aV_UXPSSUvpjW1PgjGjiC1pkLUC713DY_X-tJRLylSKT9qfftLmhnIIc33_k5R24UAUKlk4i8QVbDTvG8eHZJ36Fuh4k0GsfPkDxiNhw6XerU9IgbO53pVMyVy7gLIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هيهات منا الذلة..
أبناء البحرين يخرجون بمسيرات حسينية تحدياً لعصابات آل خليفة المتصهينة ويرفعون فيها الشعارات الكربلائية بذكرى أيام إستشهاد الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79416" target="_blank">📅 20:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWVGBHoRomlKrVxUAjlk6IOo8BBgqfWEGFUI2c6Q0hY6_wXF9A49OmFvfC5TgoVdvbYN3m7lf7WTS3CZ5zVOc6DMMKaJ2nYqLpnzfve_26qiXbCzGa8r5DpoT1ySdqxge1tff33Ql_YjAZyrR_Ago3MDUhWSyMDpkBCxsQk5BXzU-dsZ9iM2XxgGj6PrQ1XOFkkHpPoiqKW6hL_C3BnOlCYGvMp_-wV3K5o7xt0u8QSu8wHaBSZTetehTpMWNqWXU5dYStm072M97lcAZg7j4Iw_wUEeJClEJ9M4yOpLZZ4ZnUq1IjZTgP6N0QrsaqMdCxd3XdwyQSgbwE3Xx143xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الجيش الأمريكي: تبقى القوات الأمريكية حاضرة ويقظة لضمان الالتزام التام بجميع بنود الاتفاق مع إيران، وتطبيقها بكامل قوتها ونفاذها.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79414" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEhcZJubfAGqqo2g7l4eWpGUenzciz5ENQXgf8cNvJXvpZBZYPnYeC7lqoPilo1fPczJ1Ef1MW6IYEo4Y5Bp9QxQmPwGR1b_NixOBSu6sjP7QWG5PY8gBh_e1zWujKrrv7uK51WiXjuIEW0EIj7RriFWWCbI-HRZgHkgl6XWD1XQS99JC5QsxU_VhuLlWpDVsX_kg86YmC7TLCabR7SEr9EMbUceEczSqvjzD1SXF9Os-dvXqBXHvXJkoCxKc6-nCxwer6TVHUGndLuMn-E9bUKBju5N_BNBUPFWBgVMcyf-_zoJeCRnrUn2kta21ENb0r4hzDNRufbeETr5K2maQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79413" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGSUws9pjqRpDRzeW0dvi4-hbkVNtBPPZ19TwihiwLNi1KKgfXmu1oQx9uDwe91OxVAQZbbi3ur5drzPfPFbMJEN-E7ZWbgsmhoSEK0u09Gc-YYjBgj2T9SNMc7-lRfkY64_MZMZ4nPSBqF_1qzsKkJAgjz36UbbKOgYwuprhXuRcG36q0cacAwE622Q7tZmeW0E_kj5uOHVZflDVljFKZYblB4yMsI-4FaXaY1ElgwUCQzhFjXEz3bL3715Uyjwuc2caAOR8cIZ6MFyBzfqlRpEU3ZPsIRo8iDWqvwUZq1ekEOYb5PujqsETWDkqPhwas-62S3u2iTlL0GS6mEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:  مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!  ‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79412" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
