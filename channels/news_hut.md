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
<img src="https://cdn4.telesco.pe/file/fqcG5RfpsVYHIqZrI3_9H4bDSdhiTiZg5mSHK-bHT9QE8ob1bFnFNFRMfguH-WLyBjMPtg5LVYKJcT7r2T0YIzq8iXz9V6CykhXiP0QkJhY9_STBEqrXr-nwA35b3sWLggBrHJE5WGRJLDUAgXsisZsHu7-cBvcP1Ns4ZfznKbAv08Vxj34xHNuUfVzq0Dj1q39lfLwSe_SsSMeZqVOIWaiWHtLQryQK-RxOqflpGFFXLj7yDiITIU4w8q0Pt5i18V6KgYGJaejFo5fruS9otrJIV36y-G0FDhc4vpb0hS74M483R1Ig_cguJGlC1M4KZbeND3eWJV3epF6X0Onn3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 126K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 23:03:50</div>
<hr>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LleA7F26tngJJsXT4NO8V0CQToxfh70C-i0oC3y7rrpSwip0BcuFCGLFBu5LlfyDnTRReLnRH7trLPYCSlW6nwqvd4JlfGwIVkg8J1vLdCdD_VexHWjIZXpJRLdJoZ3CfIiHebI1zXsi3hC5uIaPxkistUZrLKT7F1QL0D4mxqzo0rH5V17X21KhBsdDHNGys-_5fnoODCNlQHL_nPZ8OGqrIdvwD_ppEI3-UklbiHgfZY3TKTOnHcnyWIfzCqAuMDQMvYfXtG4exSm_O4lS_zLvLvVlI0S9YTpPn0QGoqv049HHZ5zYLT2d-Q8vp0RTQhXYLhQbY0Q8AfVmmTR4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=TcYoQtXBqJljs8W6exvvew_Dw_l473HtOXLFn9g1OFXiRWE5Cmk2A5-4pI9PlPUjSI4ySya3zlp6Td5e7MWtdH9qB5ucQ24O6_Vb73-KJpkjkg74DZySuA3mXdagsIsmTc7upEn8sYdOKkX4uCyqwgF3WTiIQrohpwLRh6EgOc59O1znxALPKkb3YK6T3rRIPrg-OmNlLYr-PYhTBLB-pXrLGDoKsTSaqLiFb6J1mG8HvPd6zFZkWLUCmAJ18Mg7bMTy86mv-TENKB9NIRjtw47yLYxE8RAC_omxqu7UsSEWho3UYgRKsb4OdiB7clppuN4C-TOUbnHFc1ayUMPjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=TcYoQtXBqJljs8W6exvvew_Dw_l473HtOXLFn9g1OFXiRWE5Cmk2A5-4pI9PlPUjSI4ySya3zlp6Td5e7MWtdH9qB5ucQ24O6_Vb73-KJpkjkg74DZySuA3mXdagsIsmTc7upEn8sYdOKkX4uCyqwgF3WTiIQrohpwLRh6EgOc59O1znxALPKkb3YK6T3rRIPrg-OmNlLYr-PYhTBLB-pXrLGDoKsTSaqLiFb6J1mG8HvPd6zFZkWLUCmAJ18Mg7bMTy86mv-TENKB9NIRjtw47yLYxE8RAC_omxqu7UsSEWho3UYgRKsb4OdiB7clppuN4C-TOUbnHFc1ayUMPjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiTMKJ-i1IN51NzH6U-yk4IOK-t658PnDdtXE8ADFeD3Sew-ibwCcEmGge8hV_1oR92o5SSoojmFPKc1Vlu7c7QbYXx-1X3MjIQIN4rtHN-gcW54N-4TkyaFkb9MDz_eLarnjwsAPOWuUrGpmFh5pBqgyU-4DD8ntH9T3pmGIV69j59a5MOF5CnGc2VmKJCNBjqwl0CkSTNdDxlhFKZvdhWoYMit2q9fs4xVFSAC0shKFZBvZijtZCMOJofbAfS9PTXTsSfOjutSo0JsVtOA7yy_NGSqJ4R406-avJmGvF0TiAD1Wf73eEReacndp1v_F5cdSTK44ueIMPOx64EXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et06YdsKblZNEbnI30xcjHRLCeHm-D7P3InAioByjMX-7Mpwe-WrsN_pHBFlKYx3nZRIxhiQtp4zvYzNfLRvV5Ztk9ECYygL19Y02xktiNotQj5-hVLl89GafYrvmRQkJUXZvbi87v5juynh-2nFngUDgQeOjQpyIpfPncYooQbLw4UiGHrU8-KO6uxHpOaFr8HbqONz8Ooy2OM9b_Ko14_PzdyUNjTIxibcU1ksj82wN8yE13z2F5v6Ktzs73-6RD7resQ-2TmbGM8Z2P_YHjV4dd329UCIOMAKzS8XQQ_5aHehFuaE2XOB-xlho6P6d-EIVipH110uwxIE-TSghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kff3DGmIM667V1c1190JiDNQ7YEZjWrETCjyA6Q_2m53ZfvJd69MeeXJWSauUXhS3y6BCiXs6h7Rwf6dIPuUL5e3Q2HMz_fgVTTntMZ56TRbcgtAHgoH2aXcHeDcaqQvWffK58x82zyfKulx5bFkzRHCBGMObV8L7zLA2cEM2PhObjQExwd2c6kYC0BFCtVpHan6A0UEJ1oLnVpFkT8orUL046lfjByi1JX38-AjwP2fb4BXJM61OQLIyaDV1E5dowFtzcznosADdli5vOCRVGCxJ-EM-lxfNWhBoaHNVtqHG-XdaGpYip_XYlCABdafggq-oE2Dx9O7v1tZ24VAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vct1DEK63YEq8hVqrmXGLoU0aqtIyoaVMogkFZNxnHbIXa-vojxxGRarV8sRheYViJkeKvuFuLZX6mjI-7gV5fFyc1AtbKnaqqnJKWrmBrRGUoO5CulBwmrs8me2QIGdJSf0I5X_Lv8J88aU9qhIO9ocVhwCv14Y7bkqbPfNXCFWuwjOEhOA_74gUlKheapY0fjqRMDrgC44l4sSt9hJ3PVqcGkntJpjNwGBbHEU5WhAuLGhphPbzy66kdfqu4cPRvf4g4p2Qg2KqXjNtyw8MS6-h6JJHbKIyUrmzAcL0vpH0u2VTlFp-lik9N9kZLhA3TFZtY2oFDkfGdTINY0rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCngHQYJ8Px8QVZzaC9dqLFTCY3mLChmHEfHpit-3YQPbsBYsWdJB09e2BeFQIHMh1Em-k2IDxj_4Sl1PIK8MSFz8x2XQDGxb8YL0z_QeFmTCfYeL0P1TvtPKie6P9qWUv6KBg46bm2fgz52Fa0yX_wyUBFa71hiF7HFWCkBDrLAuLEwVir-WfjHox9R480UXfMKhZAh71RkFsQ-LPMAEB5DUkpkF9FN7-mwhve-_azG8PuWNQtCb4ksMfOhbIfH7N2haOkX0LeIaleocPzFXC8uDCWqOXs0awpsmZc-xd2dSQrA3Fl7xbRcehrlLFHHHD_CpnDH7_1nWclz8FLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=K1to7Rf3KRw_7UdssVggaiStZin18xKTu_1-dRZUbxEhQaToAArbqjZxiSwl8lGEEHQEbh7K83E_BMrJkkkkA6AjG_LhOKTdWxr5dKzsFeVJRPPMvJe3yIx9PBCRvvu2lpIu6LxL_HTj5XLJTtdwfcYmjrsLNFeJQwtjEJ-mXxuWLaJV3jksuxa6HmlDUclN1eRUwAZkH8XeNga6v5T1HY2Rn8ug5HK38vZP8uXgcjzITTFZJKqPadR0etbQIYB5vCkwo0F0UlN19YhNWEMlpFo4oWjLJT1SU2_TaudtDZ5Wqg4bD0dVlHVjUYxPE1xDx3x_gbnVdV37FIMV9yNjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=K1to7Rf3KRw_7UdssVggaiStZin18xKTu_1-dRZUbxEhQaToAArbqjZxiSwl8lGEEHQEbh7K83E_BMrJkkkkA6AjG_LhOKTdWxr5dKzsFeVJRPPMvJe3yIx9PBCRvvu2lpIu6LxL_HTj5XLJTtdwfcYmjrsLNFeJQwtjEJ-mXxuWLaJV3jksuxa6HmlDUclN1eRUwAZkH8XeNga6v5T1HY2Rn8ug5HK38vZP8uXgcjzITTFZJKqPadR0etbQIYB5vCkwo0F0UlN19YhNWEMlpFo4oWjLJT1SU2_TaudtDZ5Wqg4bD0dVlHVjUYxPE1xDx3x_gbnVdV37FIMV9yNjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahjHkbDS7PpcszymJ3A_Y45CWJKXVCrGxuQTv1SzWg4qDOk1-Q_3lV4pkk7FLci3YUhKsvUdHMrHLkK_TT6CsBNvUNMWoxxCiiD2zwVT0MPenvgMqL_sFtENVwYBhs-AaZ7MvqLWcorW1EdsvihclyNUiCdMUBmP-bWBb96HPqE4Rz5Sv-Zkpqx4lFhQ5F05xVSRVMqRPSuBsIDiGvZhuCEzdqSbN7Sow_yKjNrbxaqCLCA7I9h1wksvSFvNhmbQOuOHtz-Ph09jDOz_lE9waBCcPl9G-mHXGS15JRlnbbED-77Co0yBosLPmulN-aaODQaerFkvXrx8stebNram4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=JCkxd3lQk67uVs8_fKWVWAJhTPSbeGiIGSiR0r7mksDJWQBBHKnzXrFNXaVpegcelAtke2Zl2vKJgv7R04Tzn65yE5ghAQ-phC5U71qxeRuOPUrJNW7-oZCzyJxpcMgjaFIeMuqa-CyHmmt4RyXrf5SOHqlQgLbi6Lo8huAm9leeIfSnDoek5o2Bm7gDXaizs2l9kCpdM61X7mcpxOiG1F0Zmmmlhuu84ylaWZU3PPTVENdlyicguC7a5N08yuHzCuzYGiqDUtNaOLphmld_2X1RDorXOSOHVtDqcepcI3SSVtzhBkFTjvx9hl4xCADJ9GW8c_9ipqVZJkwNkxALCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=JCkxd3lQk67uVs8_fKWVWAJhTPSbeGiIGSiR0r7mksDJWQBBHKnzXrFNXaVpegcelAtke2Zl2vKJgv7R04Tzn65yE5ghAQ-phC5U71qxeRuOPUrJNW7-oZCzyJxpcMgjaFIeMuqa-CyHmmt4RyXrf5SOHqlQgLbi6Lo8huAm9leeIfSnDoek5o2Bm7gDXaizs2l9kCpdM61X7mcpxOiG1F0Zmmmlhuu84ylaWZU3PPTVENdlyicguC7a5N08yuHzCuzYGiqDUtNaOLphmld_2X1RDorXOSOHVtDqcepcI3SSVtzhBkFTjvx9hl4xCADJ9GW8c_9ipqVZJkwNkxALCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=q9GBT5BiWp2VCYUqFSMRbsBbNF4eI-aJy_MujK8-rasVncVaSb5jN-JCOIiPmbg6DOHkUlIw2PKy4Gz21wyc-KQieC24f8Q5vUn1FIV_cthbGMIONjmlg6i7OEe9IiJtQ5Lqjs2xccu2u-l78XQwWJiR22Q2kq457PZG9zwqRQ-9Ss8mJJiI7sEoEZrPA-5hmLUyeQ5iLDdovw5mSrSWxi_T_e2FCDmz-1w_nd1FtpkxkOCxON5ockd7_VGroosw7deu-PVdy2KXOMjniSLZ1wBdc638Zjun3d2SMb8_6AZz2UbEPVYHBQ30iBDul5O8lGpPw_CiFa-Lk91B2ctVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=q9GBT5BiWp2VCYUqFSMRbsBbNF4eI-aJy_MujK8-rasVncVaSb5jN-JCOIiPmbg6DOHkUlIw2PKy4Gz21wyc-KQieC24f8Q5vUn1FIV_cthbGMIONjmlg6i7OEe9IiJtQ5Lqjs2xccu2u-l78XQwWJiR22Q2kq457PZG9zwqRQ-9Ss8mJJiI7sEoEZrPA-5hmLUyeQ5iLDdovw5mSrSWxi_T_e2FCDmz-1w_nd1FtpkxkOCxON5ockd7_VGroosw7deu-PVdy2KXOMjniSLZ1wBdc638Zjun3d2SMb8_6AZz2UbEPVYHBQ30iBDul5O8lGpPw_CiFa-Lk91B2ctVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDuFZoTpqjGwTTwMgsQDdA5h7EhYmmxmn3nSiJWZTWszCNp-LGzrU_frpxsrMQXzS9-0Pc3Dyf7YvomjxOb9IzCRims1dsvLUqn6vFneho_UJKVSEaeHViGDIJV3J0MIHs2PH912OmDiPlsCskX3Rio3OnzSRKTK1XunYDrjDn7zq3Vee-sEpDqWGlY0u5DBOEV6ndmsigtOdE-JlAqAsB2uo-sHz7f1OopEPAFTulvSgLa3OEpe-VYdrdLxTiGq5J5YeY5odMrFgNvz9rcXc-NlU9rtzWpC7NI1HSegQh7aFEroML_WLUimYxbKakx2KUV_LZyNXBds3kWh8yVMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=DVgqEK0Sn1reMqf5OcwNDH1ZvjFAqdmPd7H_VszQKSogiiPzx9Lo4Veo--nfo8PzOox-KVpq9nNjuWOiUSTyKVmxTvvSOTg-11k1TZVWczLjpU72HxYtkJyI0oyWE98OxD-_4o4ROz8i3UDNLcbDrf3facyRrF7y0R_Y5EtDhgdy5kyOzW3ttVlefQE5uZk7o9fsvQYUb27vd8uP4pw_h7U4UKtHQzWwjCLdAU6XbHETR7aOnPc16p59RydNG0BC7hD--n1BT9xkowUA1od5pi0FcTH27JRgX0K3jHqWXKi0LdT8IqLCSFRSuaaQT03HER7ReOyegH1bbgKhgzGpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFYFA6TX-GHFfrL0X_FL-HkG7dxfeX91pgevZNM-SAjVhOQ4-AtluzYphOVHXju8O4IpEAQaWF_m-dNxUEa-O_FKW0nG4pBc60YW9_7VVd8lfZMpwoGaIRX6wnCrk4vo_rz99c0oKqZafCxHDzZsU7vvNL1vLMfCsQBlYsM3gcMEX65nvEnIVAd4JPR2Qcq-pgRAzrq54LEaCXB9-KwtGdz02UaXWtWss3bM9JMoyKg8of-krDF2qeIrFa4tkG7vu0bcce3W1vHaCkbThIREdemoMm2c6udhVAkUDa5bQzhoQbNpOjHTmnH7b5QoTl5J5Hydi62ZGMt-x6Cpk_1_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=GVy_S4kkT2JDIDapK-fkxImNiY2Dp7O4qDVBFQ1dGJsacraHyHKwmH8HEdwUu6TC_qLautnzhGrpMsZwDt3qvRJxv45BI9dkytaIYWfSMnAGm_TGAp_BCyw2yIKRaa-3Yl00EyFaeDVMx5b96T5gg61-rViHOCU8-xbMYdNANWW5uhGoUfCy5S0Rc_gHxQue1VPhrsJQ_rqXsO2zZ_rrgh1h2y9frzR1yf_AZ-9urt5BTyjWa8qrZBtRcvY8BXEoQe8YSlh5oz8q9g0Ju66auCrfg3DLaEf6nIkJRytxfNsxpO6gEbFjjdEiEbNRg_oqvTty4ZAdUmW400u-dDLFpW7vX6O3d7kWNIwmNuss3-o0D48Y0RjtHWltfVL2YIwUm81dnOE7FreN6o15YUkZeN8Sf1gzgtnwes7RIAYQrs-rfFCNSXPkqufmDwUW6D0wJdV2v2rY_gyREHJB6yyA9J2BHb3y3f3XBgvaBs1-KrqxlHQogeA1mRFGRoRibMo2UasDX1Wl8hCP5M_M0v60tRasUJIoISOoOwchwv8uVS-WrPALcfpK8ZMwaH_eDbuoMTeoTTuIPpFBXzEVd4S_ZohjSqToMzBjBwFaUn72-ny53OMZ43mGZFsuP20GpcGwfqmqduOhaJIZyo3f0qtKKF5c12kdsL-Sov_n2Iuh7wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=GVy_S4kkT2JDIDapK-fkxImNiY2Dp7O4qDVBFQ1dGJsacraHyHKwmH8HEdwUu6TC_qLautnzhGrpMsZwDt3qvRJxv45BI9dkytaIYWfSMnAGm_TGAp_BCyw2yIKRaa-3Yl00EyFaeDVMx5b96T5gg61-rViHOCU8-xbMYdNANWW5uhGoUfCy5S0Rc_gHxQue1VPhrsJQ_rqXsO2zZ_rrgh1h2y9frzR1yf_AZ-9urt5BTyjWa8qrZBtRcvY8BXEoQe8YSlh5oz8q9g0Ju66auCrfg3DLaEf6nIkJRytxfNsxpO6gEbFjjdEiEbNRg_oqvTty4ZAdUmW400u-dDLFpW7vX6O3d7kWNIwmNuss3-o0D48Y0RjtHWltfVL2YIwUm81dnOE7FreN6o15YUkZeN8Sf1gzgtnwes7RIAYQrs-rfFCNSXPkqufmDwUW6D0wJdV2v2rY_gyREHJB6yyA9J2BHb3y3f3XBgvaBs1-KrqxlHQogeA1mRFGRoRibMo2UasDX1Wl8hCP5M_M0v60tRasUJIoISOoOwchwv8uVS-WrPALcfpK8ZMwaH_eDbuoMTeoTTuIPpFBXzEVd4S_ZohjSqToMzBjBwFaUn72-ny53OMZ43mGZFsuP20GpcGwfqmqduOhaJIZyo3f0qtKKF5c12kdsL-Sov_n2Iuh7wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTODHIDWDooa13NPildW3ir6oyHwogodSwsCAXuvreFurfc0EVCsuDIgcrTEBq5feNCnVHizVvmELMF4FS5Gm5WrbVdG_CBNdBVlIi1y7pqpc1Y__s-YrxdMBrkE4_izkTsH5tl2mPvT4dJPl8c95M6ihXhGxViySUbitPnQZMVCBLW26Z-ijKAbQIFaSq3hAYXn7IRXSLLaujBEBh0Q7z8iiBB6J7HyObEwKmWXKStY3tcY0BOk9ZjrL7gXXHIyTlqgv4id9itrwdTXuT8RU2-pTnevkCem3eIVt3zE_jxF0LPSUyP3WJdCXRoE0PDgI-HreaK-EEHV3TdzArcSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLYE6454VuX8BTyGaLpbVDPyDosiKCwnGVIvT6kF4jbuTjW0Rd1CYyTlfjaecypK103hgThBNCaAS57cy4HDjM-L0g5YQCNB4PJMPXtCUy7BvAI8wV_o5wNoQa2j7yIlAjs65ztFwMcUpPm9d3W2f0CEXGMQLwAgycaEjOitqo_-Qiwa7P4tXe2xrNoScLVOSQPYKFWJ86AqBQ_EDxtizAgusrrtznxSKzVgb8wqpI8d4NX0GW_72tm0koHlumjiOVJn4ScKDN0GlhmLBGnpNc-SmCGNVFG5XEQvpyrb4QS_5DaaMpH3ScMwmPYP53aXkpnOq93e8GfWtw0IdgbwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8jVQ_qdpKXR2a2LkCDH-fRiwZVFHwLItAox5gkQapVXYyLR8rAxEi_ieMJE-Q9LrKBNhon1BkengMOZ3dRzQeWyA4grJUZ_kKImzRIWxRLPhU6_KGjJAqkmAc1yyf9kVFKYcP2yltAkK4yrktEDxBTRnMGjqEWqTX0Scqe96n6gLVaH2ivy3gIfSXDa-IKMmiEm_jmM1EL0FGGimj-cL2I1Hy_A3mSgULZHxWlluvYpfZaOKK4gnFfddXjAgdbmFMBTjK__JhTibNYhgBKc3rDE8gP5qcJsw47a4wnr7N0bhyWOhneDZ-StuHJXxYStFkPzVJ9K21asyeI9TvMJwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=XK3s3fr9AuvTAjm172HSBvqfsHW_YqLKqKxytppZ9SB8ILo-j7WyFgoGajMFe9yacKANVjiAXtOHLHzHv7AonTHE7gDXCi8zrRDY6zNBGJJbkVV-D4qNsikzbO2fgkSeUi3fEur_Txaxhc8s4R3qvGf8vwkEGFqAfx6Ma9CcszPvCzX2m2RRJkjii_RzJsp2ZOAexu9TmAf7KvNK8WO1Z6HIBt2fEZrWTtMPcaef7c5wvGojjTWi4cXEuiRu2ouiY2mZlNWfw7lUvp-KddiMHR-0E6-v7Y_R1XmZD8S8VSjQIBH-eFPKH_FSVxgojPOLRPE-_aCD6VGTFbRSk5B1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=XK3s3fr9AuvTAjm172HSBvqfsHW_YqLKqKxytppZ9SB8ILo-j7WyFgoGajMFe9yacKANVjiAXtOHLHzHv7AonTHE7gDXCi8zrRDY6zNBGJJbkVV-D4qNsikzbO2fgkSeUi3fEur_Txaxhc8s4R3qvGf8vwkEGFqAfx6Ma9CcszPvCzX2m2RRJkjii_RzJsp2ZOAexu9TmAf7KvNK8WO1Z6HIBt2fEZrWTtMPcaef7c5wvGojjTWi4cXEuiRu2ouiY2mZlNWfw7lUvp-KddiMHR-0E6-v7Y_R1XmZD8S8VSjQIBH-eFPKH_FSVxgojPOLRPE-_aCD6VGTFbRSk5B1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=idl89F6yp6w-nwL47tHBPlg9XQJl8dLc-P4nDQE5uViFCzLLDblC953fsMktpasbE9MlyS3cR36o4vYoYGbtIz2rM5XVcDh8TDQmUqs8GlMohjz8Y6zSvsWiRjjtbstyS07KYyw4uDgbO-55BYJM2C4ION9SHmRao-HSGEqhbmaBvh53Pw_6CUG6eThivHyypPgT5G1b94DqrVEnZt20lSwVJBHsufXzbQ2W8lNT2C0sq-oUzaP57zwIkIGqCZIspygJMytxkpGEES35sRAHjzd-7I2sok9Vq1p5taQJq1k3FwYOirRkulKVxyWSjLdKVY0eT8z2Wcw-y0eJmgK7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PscLmmb2l7O0atTMjicCj3mZ1DmbQ_L5gQmSJfrvDkEncVVEmfzjTOafu1emeYFYWulZsuR6Vmk1eO075Ru36PU8-ma8grTYeioEqStsA4Rd5eZSCdTJjUMDGs5HydG0FjALbIIR0Yo9XCRVwXrPfvYfHIeas7Mmuua0BqSYEYEVa7K83OwXQWLIrgWOqLdYeAHFX9cahqTBTJcT7_6JVX9B8k8zlhmR4bftKH_hTKpVeRh9H4ZCYVLNTif4CNJLEe7JfVpdB12XZfZ0T4B_JbdlDPcTRwk5IKokTrCdhFMxFNMCUayIU838mxFdx3WR99kVJxIWCltB5dnB9hyKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=DrxGVFJtNomsmiVGcSSP1ffSyYIlnZbnLvKWqTNG8Hhda2NH6Gj6Eebwsq4rLvpKPr9a4JoAJGPFB6DvW1FXuwyDlYZJXHHPPqubzyDkY64e04Ea7qJ1TOEH-ysY3-hJWy2F30zBG8rBSU0brFnCP0mKdzOvG2UJfgPlRM_nNv0NWS-N0EnuQmKVloziml14tmvM6mzdb7RcHfMekgVdrBRRUZBX09npXW_rN9eAJwM1NaFCUWXWwXdiAo-4RSFp5WHO0bMLT0aRDireQ5hEEZbosBFuu4u7aIQWV_6VdVdOChrSwutc0CxMClPdDvGafNx1lqZdd_p2vtFnFG0T_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=K5VySA69XHVzE0oetpXSl5WptWObdHFebvcGxWXTGu1SOmuUNruSdUa8VXx-4gEFbi7mQfMvSOvtGTa4rWQe_voWhVpX8Jwg8RfaEZj3ad4N1QPfcNLeQ4wLg9BEzJ7leYTPL1q6S0MV6jQlRph3A1iJV7mX6MXNRpoGjs7s2X8p63fa4kLYpx2HMoc0SsL9EoZKQzOoZtP4f-xZOID-j3Qelerk4hBMdupcaemEdFj0Q4mzdB31rfX1EZThaHYt4g5GIPxy2KdK93JQAHx51rf3FRZ13HScWFovWB6XQh9wQNxxFvNCfsVJT3fX5z_SfaYQZZpOJyM-4OcNqdYNwZgtrB86YO7IfALWQKrxKT2ckbeaeK0nf1ejjZJ-AKTZYEYLL6cINrJyrkXOANFD5Lf8tOfmPvJFMwR5hxFmkeqZR4qdRZU1GGLLt-xkSuv5Q6W4Ra_70ZPDiNiTSmJnjcoaA0V7XgpJzU8cuZjh86Ptm5Q6lzJQwZap5PJqVZ85xFMYG8ofHgLMrsQOMfqtqHDGlhcblMn66QMe2o4lnRfLyfj3VVV0728DMe6pV6wkETMBQt-2E2yYFEu8pcJSX1qxQRjiW9pvxxTI1DktFFwaDImvJeSvc3NN5vCCUHMJxi4oySqWPL2Q6AvZhQd10s_5SOwAAsRnbFBBYHDtYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=K5VySA69XHVzE0oetpXSl5WptWObdHFebvcGxWXTGu1SOmuUNruSdUa8VXx-4gEFbi7mQfMvSOvtGTa4rWQe_voWhVpX8Jwg8RfaEZj3ad4N1QPfcNLeQ4wLg9BEzJ7leYTPL1q6S0MV6jQlRph3A1iJV7mX6MXNRpoGjs7s2X8p63fa4kLYpx2HMoc0SsL9EoZKQzOoZtP4f-xZOID-j3Qelerk4hBMdupcaemEdFj0Q4mzdB31rfX1EZThaHYt4g5GIPxy2KdK93JQAHx51rf3FRZ13HScWFovWB6XQh9wQNxxFvNCfsVJT3fX5z_SfaYQZZpOJyM-4OcNqdYNwZgtrB86YO7IfALWQKrxKT2ckbeaeK0nf1ejjZJ-AKTZYEYLL6cINrJyrkXOANFD5Lf8tOfmPvJFMwR5hxFmkeqZR4qdRZU1GGLLt-xkSuv5Q6W4Ra_70ZPDiNiTSmJnjcoaA0V7XgpJzU8cuZjh86Ptm5Q6lzJQwZap5PJqVZ85xFMYG8ofHgLMrsQOMfqtqHDGlhcblMn66QMe2o4lnRfLyfj3VVV0728DMe6pV6wkETMBQt-2E2yYFEu8pcJSX1qxQRjiW9pvxxTI1DktFFwaDImvJeSvc3NN5vCCUHMJxi4oySqWPL2Q6AvZhQd10s_5SOwAAsRnbFBBYHDtYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=DKht-ztE-UU4lnbeW0rhLVJw_LxdxgiNXD15APPy0w9Gv5uatPxA5sa8bUpnriXpG1wtYIUR_NAuN_92JX5VhSSfmMkX3eynY97K0u48_SDw2K8IPHRo_lPmFRcLTDNRHHuk7TXPidvnhIpH8H-uIbiV4EJOqrpQzhOF8u2kVR2MxN6SZY8z7kfQw7SXrMtqz6DxaK2q1QMwTExFbejdu53pXEyKiMHQZT0aJOTkSI0Fh5aNIK7kgStbOUzkKHCxgPsWV8qxETk7_7vQSnb4XO0OVOCz5kCkB8ko1z1X5PXkerjcLaIqTny99OcsDNtzC1i2PSVs_wl2jFV1Y5vtoUl62Wm1dOldWBU1NjyIUllr2x5OiofKzxXxRiHnBQg41w8zIGPmLpMxyLGwnuAA9nNQRQSgf9EZlt2b4PJvU0FlOivKhxxZNkqbxNVYZmud-CtIpSAsZD4hy0oeVzSi3fQCOMZhXzyj7XxI_CmiIXRUCEXciWCvZ622idbIaEG1pWz7zwSs7tPWOujRaNKz_iv80jwQn7MZEFtjdV4xQhvwlGGtKzzrL-1BdG0ojSaAMdFB7bs5x12ku29ztUiQhLA0loIrJfVGDm65c7d38E-CBg9a2T3X-KKBQJDrQgoftL9aWq284Q2qKqqN2qRxWYmDCUKzeZq-KmXs1bsXf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Cyq6CShY7HJ1GrxOKdUOePoT_bSlUqNtLxdbAuktx_5bhqlknjFpoD9Q10S3EqI2YJ5k6x6F4RsSlYtS3J5f9JVgJdb5YxOXBy-mOfPDSVwDYqlEmMSjzCRatiBUgnrtWqKiND5kHlKp2Se25NZgoUevrC3-DxJGfFjtBJM7EVZQKSwsDBYartbU1LQo7bpqoxIBEqTD2AXH_LKpwdz-PgJhganbF5v9UpCiSBz-tlnmV5i-TtkyXn4TP-llQnkdd2_AUK2EzVf4ERgLJgip1uU3t6gYVVjxMyxh_M90l1uE946zVStLxg_v0A1tSOrFSV5G4U2e0s2MoeLJVON-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Cyq6CShY7HJ1GrxOKdUOePoT_bSlUqNtLxdbAuktx_5bhqlknjFpoD9Q10S3EqI2YJ5k6x6F4RsSlYtS3J5f9JVgJdb5YxOXBy-mOfPDSVwDYqlEmMSjzCRatiBUgnrtWqKiND5kHlKp2Se25NZgoUevrC3-DxJGfFjtBJM7EVZQKSwsDBYartbU1LQo7bpqoxIBEqTD2AXH_LKpwdz-PgJhganbF5v9UpCiSBz-tlnmV5i-TtkyXn4TP-llQnkdd2_AUK2EzVf4ERgLJgip1uU3t6gYVVjxMyxh_M90l1uE946zVStLxg_v0A1tSOrFSV5G4U2e0s2MoeLJVON-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=YPnE_znPvUJwUUul3Sisl8CJ25lbeFH4crBZEhRtTzZJBY1R1cDtwLWszAsWV8ll6XNbKyxQC5FI5RMrPoPwM6v2cvEhNCYxwLiek4XZWBKQoedFCIloKCIRdTm92IYSFbQx-JInlP__3xfAitc3PDI2fs1UFZhRdXGeml_7Rq7xJ1cuvXilQCzl2LHr-riEMvFo3Y6xCB1HdJD5aVThkbpp1unHiztBM0oHp77uZL_WfBBIWWW4zLQkxyoOe6tUFI2lao4nILbDxsvWNBRCg9JY3eX9LIDcD0uR6vVlJqhJ6IDlsKP8xDVA1KKK6H0yzyMti1GUyDnjohSCNFNFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=YPnE_znPvUJwUUul3Sisl8CJ25lbeFH4crBZEhRtTzZJBY1R1cDtwLWszAsWV8ll6XNbKyxQC5FI5RMrPoPwM6v2cvEhNCYxwLiek4XZWBKQoedFCIloKCIRdTm92IYSFbQx-JInlP__3xfAitc3PDI2fs1UFZhRdXGeml_7Rq7xJ1cuvXilQCzl2LHr-riEMvFo3Y6xCB1HdJD5aVThkbpp1unHiztBM0oHp77uZL_WfBBIWWW4zLQkxyoOe6tUFI2lao4nILbDxsvWNBRCg9JY3eX9LIDcD0uR6vVlJqhJ6IDlsKP8xDVA1KKK6H0yzyMti1GUyDnjohSCNFNFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=qaoOR2O4Y0rFEVamaQqRD4FgMh-eFsSRXu6B67I-s-S_1M4s1YdVSDyPPn0s2TCih8wN9Av8W8EwKGmg950q6a6tJ2b2Eedv5kO1L9sJmmFU2hQt4tNpQFf2WNwbtlKyX0NSHSiQkQHxKqYH8K5x0c7jQYyUsxIzHgeHclTv_QLbs6m9AK9X2GOk8qsBtxQXR2vHrVAkFChovzViKUc6zMggJ3Ttf5vuwADty9wKNwIaRYYJffaRy1tiCiREl-Ful6ANy-XTr-2B6_gwgEl1iogVsNdZWyakMJN-Y6pHCwxb8-rErHAw8pwtcCQUFnN-6fP6LquRWO3DcE1BVGYV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=qaoOR2O4Y0rFEVamaQqRD4FgMh-eFsSRXu6B67I-s-S_1M4s1YdVSDyPPn0s2TCih8wN9Av8W8EwKGmg950q6a6tJ2b2Eedv5kO1L9sJmmFU2hQt4tNpQFf2WNwbtlKyX0NSHSiQkQHxKqYH8K5x0c7jQYyUsxIzHgeHclTv_QLbs6m9AK9X2GOk8qsBtxQXR2vHrVAkFChovzViKUc6zMggJ3Ttf5vuwADty9wKNwIaRYYJffaRy1tiCiREl-Ful6ANy-XTr-2B6_gwgEl1iogVsNdZWyakMJN-Y6pHCwxb8-rErHAw8pwtcCQUFnN-6fP6LquRWO3DcE1BVGYV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=qE4EnJW0FmddjPwuFek5anmK9Rrn3873071JwSsG5f39QFquAciWOPq4lJVauwFaj9NQaIbBvfMtt-6Pe8FAh9RCCefcbu9wu3xC2EJl1a7ETtUskp5CAlwn_HPOG48txYgdLrIukuFqFDaXulhFn_CtkxTvJ2U4aMhUa9AHR48Ewl7rQAoKRc6DlCaws3-_QeKB5ghzDOYo9Mqya4iOEr-PpWnA9X8gjrtnsqsjHp4uDe1V7qLLPcbUgWpU-lytJFLHP4nWktIWdfGx-4FIoh9CSpj8zOpTzmpa3LNkygojrtY2a-q1GyE8cOue1dxFXMKUn2RtcLXG1InIxrINOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=qE4EnJW0FmddjPwuFek5anmK9Rrn3873071JwSsG5f39QFquAciWOPq4lJVauwFaj9NQaIbBvfMtt-6Pe8FAh9RCCefcbu9wu3xC2EJl1a7ETtUskp5CAlwn_HPOG48txYgdLrIukuFqFDaXulhFn_CtkxTvJ2U4aMhUa9AHR48Ewl7rQAoKRc6DlCaws3-_QeKB5ghzDOYo9Mqya4iOEr-PpWnA9X8gjrtnsqsjHp4uDe1V7qLLPcbUgWpU-lytJFLHP4nWktIWdfGx-4FIoh9CSpj8zOpTzmpa3LNkygojrtY2a-q1GyE8cOue1dxFXMKUn2RtcLXG1InIxrINOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOy_R3Cnj8iqsebVTe7dHTqJDDRZsxzsTkB_6JBUsUJIf1_XiGi7WnyYcgd46jwPDwjjBo3Y6SntIBXTX5I-OJeSIG4zJ_AqiAdR7vr4sWpE9vadiFDxXbz17bEL4a4t4VQoq5_N_r0eiG0oHjrQ17ZKSg1LaXdONDRKuKYwlB1TSTsq9cpIXeSCJOnWGOYk3UhPXUzgZmu34FfB9yVJFAvAwQg3Vk6eGqEy-4KvOzGo2iGjYdbsDZvn1avkoGrOe7TsVtjPi67dpKHhWkOhLWA5LsAwxFzYE_4HUfcmfwYdZr9tpoQ-ToXUmw1Uadquuryb27CA-dsnpZTJCLSRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OggyxV9Bvzl4tMRCcbiWRfpE-xmG_oCALcteHIJJKwmQt-qyEAx3j2m21yVKitxVHbmzW8ZdNlWG3hhTc-oYRBJs8NPc7VGLOS2sW4uS-vXsmXa1gwoXQGQ03NcGrDv9iPo1-B8ec1607zVPmTeOnenI7JkMGCpZ9vEib6Ro3ndjvAJnMgJbP0BKJACPZ5I5nxRVIOUTIs5fmIRChYMmwFboW5dXD8nNm5HyGW560cia8XVcwz5S8uzLSXPvv7lUV-zXjSSK9FNehHJeL4Y6e6YPKUHYClZK7qno94tEMIMEEkC0xUYKx_yMepbeSjKjFSqAdui7eaSGMIUpvB3Snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=rCRKw8C515iE2nWbBmme81mow_hxGsZXHSs69RN591GZdQvP7YdDtiPnyu35n0xV4874m76pCmaC0mgBpO4G4lVGH8fXm4OAyH1f4wjqcYqxlgaAns7eAfPJmTg1dn67EzedPq46m5yXSmC26hxPeWuONxeBZ9ML8nrgP_bIiwyGYlqLc30m7eJuenzSGQi6VskuxjqQxji-UrZvbeO_n3zv7u-QwB0wyqqVji4QsAfoRD_bNv2hTVUBC_tz2IXwHEjfouNcKMvHVsEmbAak9CFTAXcAOpnk0Ku57AFUu5I0dIBxkZXFIMxYlVJRrl6pUX5hU8SYqO9VHK8XuRMGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=rCRKw8C515iE2nWbBmme81mow_hxGsZXHSs69RN591GZdQvP7YdDtiPnyu35n0xV4874m76pCmaC0mgBpO4G4lVGH8fXm4OAyH1f4wjqcYqxlgaAns7eAfPJmTg1dn67EzedPq46m5yXSmC26hxPeWuONxeBZ9ML8nrgP_bIiwyGYlqLc30m7eJuenzSGQi6VskuxjqQxji-UrZvbeO_n3zv7u-QwB0wyqqVji4QsAfoRD_bNv2hTVUBC_tz2IXwHEjfouNcKMvHVsEmbAak9CFTAXcAOpnk0Ku57AFUu5I0dIBxkZXFIMxYlVJRrl6pUX5hU8SYqO9VHK8XuRMGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=W0nzJEn56Qf7F7MnGDnJaXzMreVXcO2nxzwPc3Bvg7N2X9zg4bGP3-gGL4vjghW9p8yg5tgcdBREsodnYpZpFkdgi4fcSPGOLMcQS5YcE8EZUJrRyqz8m1JnGm81OXCkW-N0nlu6pwTHdNNmwHse3Eh5UknUqJMgszl3qoUCAyiZm6h8YBZxDgC9MNvJ-EYXqsKkON9GNkX2yu0RF1IVtw2249jCDmXV61--3Tmo2pJsmsI6liL0wOc_gM_U7NIsZqo0zXozl9CSHS77iIHM-IYZ1RaJCuuOattyLoCgzlg_PQ7vaeX8q_-svQOlw-QNOJ4pBMV7UPo7boYcXIz7lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=W0nzJEn56Qf7F7MnGDnJaXzMreVXcO2nxzwPc3Bvg7N2X9zg4bGP3-gGL4vjghW9p8yg5tgcdBREsodnYpZpFkdgi4fcSPGOLMcQS5YcE8EZUJrRyqz8m1JnGm81OXCkW-N0nlu6pwTHdNNmwHse3Eh5UknUqJMgszl3qoUCAyiZm6h8YBZxDgC9MNvJ-EYXqsKkON9GNkX2yu0RF1IVtw2249jCDmXV61--3Tmo2pJsmsI6liL0wOc_gM_U7NIsZqo0zXozl9CSHS77iIHM-IYZ1RaJCuuOattyLoCgzlg_PQ7vaeX8q_-svQOlw-QNOJ4pBMV7UPo7boYcXIz7lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=r8zkwh6Ek0b6JOTkUUlpajhqEi3jmGO1dW4xOMNuGp-nyARyM36SttOUkYc_EVpjyG9F95mmXRW7Rm_uqLegTGX_OHa0emshgPbmeZn8ohS9zvUBs7FkuPiZtiHwJa2XJW3w6JpJsvTRgwNYT72hxX_kXiH1FgpRHy-0gG4wE-Yv0Rbqf_A0yjpihdtphkJfG1MGUCAIOXg2D5zJWwcfTxUvJy-6fxZ8w4U7YA5rqJIHCySLn1dOLD__Loa3kl7RqtOq-d4QjpnGRfb0ZhZJRSLwM_lzZ3AiKNLlolw-jMiKOX72u1Y2UBEyXdFUYJ3RNwpUk8VbRoDV00Ul1KsbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=r8zkwh6Ek0b6JOTkUUlpajhqEi3jmGO1dW4xOMNuGp-nyARyM36SttOUkYc_EVpjyG9F95mmXRW7Rm_uqLegTGX_OHa0emshgPbmeZn8ohS9zvUBs7FkuPiZtiHwJa2XJW3w6JpJsvTRgwNYT72hxX_kXiH1FgpRHy-0gG4wE-Yv0Rbqf_A0yjpihdtphkJfG1MGUCAIOXg2D5zJWwcfTxUvJy-6fxZ8w4U7YA5rqJIHCySLn1dOLD__Loa3kl7RqtOq-d4QjpnGRfb0ZhZJRSLwM_lzZ3AiKNLlolw-jMiKOX72u1Y2UBEyXdFUYJ3RNwpUk8VbRoDV00Ul1KsbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0fevNIM3CaO0_32ANv3kcUoGwbC6lY-KI9tv9JIzUX9nRm-PKOKRnBQvkIZLb_I6M1v0NhLktiN-w5nr7GIbVepIhksNIELcR9PSWeXFV9xNzTXKH_Rc74cO3RsSwzuh2v9a2kQItmVOYuabBIrDgp22oeBSGn_LRHKuVchF8O_h4dLcaVZddrqHNxcAUXvg5GqY74PDdNK51hRC5tI5GRuSqHzNMjv9tJP6VGXkvU8sL1zlhOwNn1cBJAHUZAy0c-zeS8ZvZgY6EqmdrKJRkKfY6TuiCIuFibanUflFMZOL_zdAbjj8n_HQUcLIXJhInXSbHnnktYSiC7n7I-jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=I3_i3vzwqoieXB9Qpo6bN4lx0OZaBtgGgSCBnGRNQBjabSYkX8sHaBwG9X9eqA6DhYOLbZS-8m2fyZ0qfqZdwPWDC3MfhCGugYr0U0-L8XDMDXb0ynL1tDQz1srFjwdekBV9KRD5kc4ylwnkqqY6uv0dNS37bh00XXnCQsNzH0NRef7GNC_Dt2GaDjwH23Rg4MwBzH6HkPanf0oGN-8H5qjU1QA97NcXAUp5ShLyTQoCHXtkT-1bLgwHM1mu_ILBbBWc17dWJwFeQPh64q44BAbhwyvG1xp_PDG_vLlZic5nMMq4omKEO_pF0ycj6e54F_BaxWeg8GDl_VOeieOFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=I3_i3vzwqoieXB9Qpo6bN4lx0OZaBtgGgSCBnGRNQBjabSYkX8sHaBwG9X9eqA6DhYOLbZS-8m2fyZ0qfqZdwPWDC3MfhCGugYr0U0-L8XDMDXb0ynL1tDQz1srFjwdekBV9KRD5kc4ylwnkqqY6uv0dNS37bh00XXnCQsNzH0NRef7GNC_Dt2GaDjwH23Rg4MwBzH6HkPanf0oGN-8H5qjU1QA97NcXAUp5ShLyTQoCHXtkT-1bLgwHM1mu_ILBbBWc17dWJwFeQPh64q44BAbhwyvG1xp_PDG_vLlZic5nMMq4omKEO_pF0ycj6e54F_BaxWeg8GDl_VOeieOFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=khpqHyPsVauOjTq2w94nA1xcxQvf9KQkb7wpTy4cbH47NLLNa-ZX0uozVcnN445cDyS5QZeII38rxHXiSpqi1PEFAc9EN7hgWLmRpaa-co8r2LY4248QLTpba-LeX95alhEECdDY2RODGCCgcPe28nLkB5R9uwuwReJbBVlGbHeoWqCPZcHaspQfLLD--hgUqbRdOAGXa5HQd65YBILRvFSXe2Oo_imSECIjWUDdXypsGcRxpqtXLPJompRaWBZcXlrUhi46k8gwzAyS6MCbBVZvg1C2lIxjIzW-0JFBqE2B3O9npoa6alTs6oGzUN2xnanAfv09IpzZ69-DS7HHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=khpqHyPsVauOjTq2w94nA1xcxQvf9KQkb7wpTy4cbH47NLLNa-ZX0uozVcnN445cDyS5QZeII38rxHXiSpqi1PEFAc9EN7hgWLmRpaa-co8r2LY4248QLTpba-LeX95alhEECdDY2RODGCCgcPe28nLkB5R9uwuwReJbBVlGbHeoWqCPZcHaspQfLLD--hgUqbRdOAGXa5HQd65YBILRvFSXe2Oo_imSECIjWUDdXypsGcRxpqtXLPJompRaWBZcXlrUhi46k8gwzAyS6MCbBVZvg1C2lIxjIzW-0JFBqE2B3O9npoa6alTs6oGzUN2xnanAfv09IpzZ69-DS7HHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=cnT1cl6RPulY5k2xsm7N1gcl6kabdZvC8QoHIV6dt7qypv7gktsXnroe5Qx-0WyjsX0zXV2zlmddJ2xP1tb1ZgeO5XqKPva8DmbnA3rvEhkqe6SyaiqrqG7rjDbOwyy7T_FQJwiI7pXF9IhfKWGn8AF410kyLlGmdddt4w3dWkciA2Q8D60ELiGMrYNX_V_bseLm7PDvzmLKrqpGqr7eCCddkPShiSfIf-uUTrjl3G9JL2JDmuEOF1r0meEgZmTSijLkdL4RQtpfeAnTVR_i3oANai3qNM-76raJHad1xWg9qbJa9Env4j-0FB7qYmfEBHkNANBVBYprxjEXgdeeWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=cnT1cl6RPulY5k2xsm7N1gcl6kabdZvC8QoHIV6dt7qypv7gktsXnroe5Qx-0WyjsX0zXV2zlmddJ2xP1tb1ZgeO5XqKPva8DmbnA3rvEhkqe6SyaiqrqG7rjDbOwyy7T_FQJwiI7pXF9IhfKWGn8AF410kyLlGmdddt4w3dWkciA2Q8D60ELiGMrYNX_V_bseLm7PDvzmLKrqpGqr7eCCddkPShiSfIf-uUTrjl3G9JL2JDmuEOF1r0meEgZmTSijLkdL4RQtpfeAnTVR_i3oANai3qNM-76raJHad1xWg9qbJa9Env4j-0FB7qYmfEBHkNANBVBYprxjEXgdeeWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=anWIf3mhNwQyvAb3du7Oar283nsgBrxM76PLqzJJxjFSp9Lz6TEqmAyILJRW2xkz4wQzAqwnS46ic51kdoPhzTwQCM60cBzeU6CESrrHXEz_m8n69WikqsSCMDP1m9MH02eyhnR57Jc7g5tNjUUJX3ijlj40SlZ4pZyXaz_Sz4vi5xOGODfMCsdLv3etW7fdru8877hnyUiyRFII_vE1MOAQzvMpjVySlLsT9G2Vmu3f_gdYXJOfIWCyfpj71HeG-ZGS5oPKW1a9sPBoUeeYm4jOYivC2WeH9MCqdl5uJFDfrtHqkor8C_QxmYvu5MGCA5e_IEQMIAVrrYG0-ONQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=anWIf3mhNwQyvAb3du7Oar283nsgBrxM76PLqzJJxjFSp9Lz6TEqmAyILJRW2xkz4wQzAqwnS46ic51kdoPhzTwQCM60cBzeU6CESrrHXEz_m8n69WikqsSCMDP1m9MH02eyhnR57Jc7g5tNjUUJX3ijlj40SlZ4pZyXaz_Sz4vi5xOGODfMCsdLv3etW7fdru8877hnyUiyRFII_vE1MOAQzvMpjVySlLsT9G2Vmu3f_gdYXJOfIWCyfpj71HeG-ZGS5oPKW1a9sPBoUeeYm4jOYivC2WeH9MCqdl5uJFDfrtHqkor8C_QxmYvu5MGCA5e_IEQMIAVrrYG0-ONQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSoGhcjZt7AXW99wjSrvStG0zIypeMZYvK3fNVSrd8rgVbDBdBl41qh7L41ox_-TL4DQbHP7Qhp1asROkqj-5QyMyun55mjgRE5_OZ6xzsotV677TAMrqrnRrnrmIpgOibBnb9AIJeVw-N7DegTV0sjGoicflF_Fhfgsju104841rSbyBnajhnPldYM4b0xas_GbfvSg_dGdB-IU8TcU2PDVkZx1SIuUWdIGe7a7SVB8_Kw9k5cQk7plC6_fEcX7WY3V9HuLmImfweF_i4Y3GqploGpN4LH5Oyxl964OaP18Vj1fnrZpJxdR88uEQUCHg89SPDuf_U4VNxJWB2JSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=XBcYlL3YcIGrZNmdAGuLltwCD3jvwxw4JlMrS9DnP-eD_B9NZwLK7AKag6JUreQWmAKKJoLjmSBGXRaXNnLGzGY6Iyr8G9mSsLkVBC5KOVa2nta2p_SOxHIAicJQ3k0fR-fktBCa9xVgujq8DTIatk505MRr_N9ewhtpdIqzwG0RkiYNqY7jFYtD291I_KLGhedk6TV0B76zTm9SmUC6g9rRgS7ql7tYB4B4b7NQY-YVQDIJeoPlMt6X1iIct7qAOcsBhOReRlDCbG6h8ItxxQpieCAsTWyeFKTEpjtxH41D9Qb7ugH4JSb1Dl0Lz9DZX6nmiRpG7-fgzpVd5KC9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=XBcYlL3YcIGrZNmdAGuLltwCD3jvwxw4JlMrS9DnP-eD_B9NZwLK7AKag6JUreQWmAKKJoLjmSBGXRaXNnLGzGY6Iyr8G9mSsLkVBC5KOVa2nta2p_SOxHIAicJQ3k0fR-fktBCa9xVgujq8DTIatk505MRr_N9ewhtpdIqzwG0RkiYNqY7jFYtD291I_KLGhedk6TV0B76zTm9SmUC6g9rRgS7ql7tYB4B4b7NQY-YVQDIJeoPlMt6X1iIct7qAOcsBhOReRlDCbG6h8ItxxQpieCAsTWyeFKTEpjtxH41D9Qb7ugH4JSb1Dl0Lz9DZX6nmiRpG7-fgzpVd5KC9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=Ia2uotN7powndYtlnd7-Pj0-YWYpYIbRlb5ftkU-sPmtv3R_bgJuADAl130jgUG1XlOCURtH3bGiVm2tDCS0nBHI5OvosGhJ3PBsiKNpXIKszrj4CjdN-DcDl1DaIz1uE_gxcRi8DYGKAt8WNZCrzoMMxBhiB2F7otAZ2FoYQp8nv4IWp3jeQOCmDaNOu8b0SfQng7yLo6rlN2zXyJERA7NIbRt34Q7HnWYRdUvs7hNzFgroUPoyWmVG2tv01hi0FIssF3RVABrjOfa97EKMMIlpQhN59Gs7eut8uCuEhG-axpW4iSj50G6QfhjkDiCnqDYPHtnWQX41L2dL1cbeBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=Ia2uotN7powndYtlnd7-Pj0-YWYpYIbRlb5ftkU-sPmtv3R_bgJuADAl130jgUG1XlOCURtH3bGiVm2tDCS0nBHI5OvosGhJ3PBsiKNpXIKszrj4CjdN-DcDl1DaIz1uE_gxcRi8DYGKAt8WNZCrzoMMxBhiB2F7otAZ2FoYQp8nv4IWp3jeQOCmDaNOu8b0SfQng7yLo6rlN2zXyJERA7NIbRt34Q7HnWYRdUvs7hNzFgroUPoyWmVG2tv01hi0FIssF3RVABrjOfa97EKMMIlpQhN59Gs7eut8uCuEhG-axpW4iSj50G6QfhjkDiCnqDYPHtnWQX41L2dL1cbeBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=Z19htL6zcq-uYjQGUeRV_CvasTVu6Fg38H3-OUIX9va90Zw6V8KnrHQ2kmVssqdRCCf-TJJpGxGWCiVnyd8GfE44asck9UhtOkJeJCP-K_w6XOn_cEKbPRAinQSS7TbvPloZgeck8tLz5y8mCybdQ7S114kYslFtkDLkmQ_c3FC0pSpZvndaE7AK1udrv8uBJEtCNMuNvLWH6oOlcdYyK7loKiVs6u98qJfAnonkDJP2v5gwQ5PmOyXlkMgCNH30ARG8xPIIYfNI3gWmUOWCCKid50TsySqqE4k3TFyxduNASa0Oh6EfrVDDV1LZJeFikl1FiQB88qgdBm1xINFq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=Z19htL6zcq-uYjQGUeRV_CvasTVu6Fg38H3-OUIX9va90Zw6V8KnrHQ2kmVssqdRCCf-TJJpGxGWCiVnyd8GfE44asck9UhtOkJeJCP-K_w6XOn_cEKbPRAinQSS7TbvPloZgeck8tLz5y8mCybdQ7S114kYslFtkDLkmQ_c3FC0pSpZvndaE7AK1udrv8uBJEtCNMuNvLWH6oOlcdYyK7loKiVs6u98qJfAnonkDJP2v5gwQ5PmOyXlkMgCNH30ARG8xPIIYfNI3gWmUOWCCKid50TsySqqE4k3TFyxduNASa0Oh6EfrVDDV1LZJeFikl1FiQB88qgdBm1xINFq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=X4aOPNiSF_mNxbWYA5pWqGBypBNSsNe-xbEmq1g5UfZ0wd3l4sm2y-e5AY4KqCN3A3-ScYg9NgrxBOrDYzC94XNafZQR__PF85F-VxiWS8x8NvbpTqYuABAg33TpM2gysGZFTS1zO2QdwXMwLkwHodTPaHxUeV6tVml7JQuCqkt1Y-8jeJlbyQoEuOGd0OtmDNY017ikVSd9sntqmlV4mvXMvyVhAQJ36fIB4TAxJs3nwTaGWqzKzJU5lipBaomrK9Rnwc3pg_rlsIqaze2SWE3A6UqVEcDEkWeOwsWWSbjzUk8Z7Ve_k8ftJCJgfL5M64AofWqkMQjaOT1FvPYt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=X4aOPNiSF_mNxbWYA5pWqGBypBNSsNe-xbEmq1g5UfZ0wd3l4sm2y-e5AY4KqCN3A3-ScYg9NgrxBOrDYzC94XNafZQR__PF85F-VxiWS8x8NvbpTqYuABAg33TpM2gysGZFTS1zO2QdwXMwLkwHodTPaHxUeV6tVml7JQuCqkt1Y-8jeJlbyQoEuOGd0OtmDNY017ikVSd9sntqmlV4mvXMvyVhAQJ36fIB4TAxJs3nwTaGWqzKzJU5lipBaomrK9Rnwc3pg_rlsIqaze2SWE3A6UqVEcDEkWeOwsWWSbjzUk8Z7Ve_k8ftJCJgfL5M64AofWqkMQjaOT1FvPYt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ihCl9cYoV6m4T7P2ZeTs3r4xi1Og1lEGfXIUe1AJtchzBNx5yqgYY7LVVzSqIotdpevLN9ix13jP2fpslVWTt9jfUbHwmm3MNSzIfyG_0uahBxmW7P6sPvW3yUgrTTh_iOsM1k_LxeSttSpbpJn41dX5izkz8C34RvgRSNZvergZgJCvrWiU8R68w1LVOa-g3lC-RGMWmsWjCOSw1cNwjaPNPwOss6xFUVlAIOyxklYbIHnN2ze1_a1cyq6Chh9szh3nw2bWQGDuLwNpgygm1aga3EKjMqLQwFbuWw3kmMxtNJv7ljIL1ee0IPGUr0P3Pel1MbX79RCQVPUeVZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=dByYhy2sfFbvj-qBSX8Aej2WgO5GSLck7ssWjbYBsNHnNol3zZPXzSpAg3vtqGnS-WqyIh8wBSZ43KdaUrAYclSqwEVCdeBZO0yxcPPkLm3TdxYSsWOgdDANi3Gbi828JqxQjEaF2YJoQFtVFstlF4fhtnKmO2-VLPvgP824iqXOFpEjj-SMmocekt_15OpyPLbdTeQFMhcy7eLbDjGF9tmTjr-Crnmceg6CkHcXSxeN_8RuBg1EgI7UbZ9BfoRoNUVHYU_1XaPvTaeYo1hj-hF5tz9oOt8EHl4657cONfLeYfStDAno3H_JN9T_rhURNAz3DVCf806W4lH-udQxaGTwAD1dVHV9jWcO6COiSAtF9f0jDd4-K0Q-V2uCC9ydYXpCFlLgMxYCW1Iz846pLshB7M1U-kf9__sJidAsIbRGBCZTq_RPlJQRveB4vj_bmtFM_eJUqqaR9b8xdVB6shdZbaYt8uJGy6zxqsKDwsFuSBW00SKG6WfCwWjyC7L12xq8tdMfL7yX9XoRM_Jk7UxRpPMeyHrM-FDntq8Umlapr4sNu8N-N9ryKWMDjdTSBz-dK99mnMLwyt6hx9CIDYkPPqjxcROBv6xhR2oQ9BXbDXnmn-h_FtRSGCEdv83bBkZolZSP14CTTiTQoFwtikVLkZLcw8OChLf6zIRHKDs" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=dByYhy2sfFbvj-qBSX8Aej2WgO5GSLck7ssWjbYBsNHnNol3zZPXzSpAg3vtqGnS-WqyIh8wBSZ43KdaUrAYclSqwEVCdeBZO0yxcPPkLm3TdxYSsWOgdDANi3Gbi828JqxQjEaF2YJoQFtVFstlF4fhtnKmO2-VLPvgP824iqXOFpEjj-SMmocekt_15OpyPLbdTeQFMhcy7eLbDjGF9tmTjr-Crnmceg6CkHcXSxeN_8RuBg1EgI7UbZ9BfoRoNUVHYU_1XaPvTaeYo1hj-hF5tz9oOt8EHl4657cONfLeYfStDAno3H_JN9T_rhURNAz3DVCf806W4lH-udQxaGTwAD1dVHV9jWcO6COiSAtF9f0jDd4-K0Q-V2uCC9ydYXpCFlLgMxYCW1Iz846pLshB7M1U-kf9__sJidAsIbRGBCZTq_RPlJQRveB4vj_bmtFM_eJUqqaR9b8xdVB6shdZbaYt8uJGy6zxqsKDwsFuSBW00SKG6WfCwWjyC7L12xq8tdMfL7yX9XoRM_Jk7UxRpPMeyHrM-FDntq8Umlapr4sNu8N-N9ryKWMDjdTSBz-dK99mnMLwyt6hx9CIDYkPPqjxcROBv6xhR2oQ9BXbDXnmn-h_FtRSGCEdv83bBkZolZSP14CTTiTQoFwtikVLkZLcw8OChLf6zIRHKDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=QaFKO7-ynCdK7_UpCX6MRiBwlp1Plk6L5tGyTtOtX-r7Zm-y41ycrISz8iu3RtOkFZJ2PeS4BkAOyROOCepuxsNwwwZfZurnd_RAWW2AEsVeagjl9ljlQdEgLJP3Ck04lLVUPLvIlSJ4dbvfDcMokDieyGaHP4skVPznTAvRuemdBSUJc6TNrxvnEVnfPZc0g8qSHoFj_xllKb0jU8YYmYhIXnwKsl6kaZ1XspLuFTcJC-ZsCExZaqM3vv0RR4IwoSYuf8_gjhdusMY31B0PchMRXaYZCuXRY0f1tJMoK1Ryar4_6-3Em9053yKN60BQvA89HbxFnSXcJnITG3ONdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=QaFKO7-ynCdK7_UpCX6MRiBwlp1Plk6L5tGyTtOtX-r7Zm-y41ycrISz8iu3RtOkFZJ2PeS4BkAOyROOCepuxsNwwwZfZurnd_RAWW2AEsVeagjl9ljlQdEgLJP3Ck04lLVUPLvIlSJ4dbvfDcMokDieyGaHP4skVPznTAvRuemdBSUJc6TNrxvnEVnfPZc0g8qSHoFj_xllKb0jU8YYmYhIXnwKsl6kaZ1XspLuFTcJC-ZsCExZaqM3vv0RR4IwoSYuf8_gjhdusMY31B0PchMRXaYZCuXRY0f1tJMoK1Ryar4_6-3Em9053yKN60BQvA89HbxFnSXcJnITG3ONdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=RUiCZTrXaiByf8rxcNYwqWbkNEqDjf3jEzC3a05stWNcjkj5FkCJxkE_kQkCvVf3NgysrFJrRXOy4GYYgfV93kWovVwrnaJHYqnU1chEgYq-xOURU_Vb3sPBlChCgKsc-yNezgiTNmlGPXRU_BRQDqK_088PHJXE1tpBEdao4q2u_sn0KsG1H3BOHwsLM0IZAQX_xjXgsnAsEahgiluyY63g2WfCItlnmaJP8DJk8vCQ3DUt3dlEpDEJmUabOdSZmgzkFkpZfjM_NIHf5LWzio6f6aREvTq1O3Zfy58DO0k0Hj9CTeZLqYj5LmjVEQXzRb8VZIvv2j1jb_cZSYczxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=RUiCZTrXaiByf8rxcNYwqWbkNEqDjf3jEzC3a05stWNcjkj5FkCJxkE_kQkCvVf3NgysrFJrRXOy4GYYgfV93kWovVwrnaJHYqnU1chEgYq-xOURU_Vb3sPBlChCgKsc-yNezgiTNmlGPXRU_BRQDqK_088PHJXE1tpBEdao4q2u_sn0KsG1H3BOHwsLM0IZAQX_xjXgsnAsEahgiluyY63g2WfCItlnmaJP8DJk8vCQ3DUt3dlEpDEJmUabOdSZmgzkFkpZfjM_NIHf5LWzio6f6aREvTq1O3Zfy58DO0k0Hj9CTeZLqYj5LmjVEQXzRb8VZIvv2j1jb_cZSYczxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=UNbQ5jejM4R4G39okSFs11n7c0WH9KoAZJ_-MZbhz_3bh8_4RfwYd3cv_aqTXXZeAsU3CtwES3s4d5ZMyrgdXtuLUnbbBWMGvo_nU_egZ7bTd4sqwBqGzsLabFN_Swj8u4cFLO4eVdbVolMjjD_iSaqopcSQWZXXLUSK_FdQwWYH2y9V4qX3y7QmvIQLMqzfqwFUjdUka1iwI2McqG4J8pF-mrr4Oj3m0wBz3TJT-fdQdXtKRx0768aXNdvhFkbC794j1T7kxgsyxHFscNjE-RKGK8c12XhNArkj0Csmt72i3oRwE6CTxRh3H18y4jwnLMxVR2vUVDgG5i2KGO9Icg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=UNbQ5jejM4R4G39okSFs11n7c0WH9KoAZJ_-MZbhz_3bh8_4RfwYd3cv_aqTXXZeAsU3CtwES3s4d5ZMyrgdXtuLUnbbBWMGvo_nU_egZ7bTd4sqwBqGzsLabFN_Swj8u4cFLO4eVdbVolMjjD_iSaqopcSQWZXXLUSK_FdQwWYH2y9V4qX3y7QmvIQLMqzfqwFUjdUka1iwI2McqG4J8pF-mrr4Oj3m0wBz3TJT-fdQdXtKRx0768aXNdvhFkbC794j1T7kxgsyxHFscNjE-RKGK8c12XhNArkj0Csmt72i3oRwE6CTxRh3H18y4jwnLMxVR2vUVDgG5i2KGO9Icg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=JNIR5b97RFr7hUQZrc2LLxlU_mcykiUk35FKPlv6CB1yuDcQJ3eWAt8qRYDXKEcS4acTpK8nEQpo9E7YAxWkE76fK3DKTr1E3RF0-n1qbaYbGWx9Y2WlH5F6jxXmCIh5dbPje-4IdKYI48SIgHsJx0dfgH7yczAxMfIeMk86nGPWrPlXt4C2YfB0LvOnl7CB2y6DgIj0yzCCvvHxGauhGubeyhqiUOTS-YTWEft_bLRSULwp8bN1-zX4ez07yo2tBOXZPcYIlXMBGDKTpWRwiE8wZgyKf4ODtwDLJXz1U-L7_KOIMc8p3H7pqOMGLSvVq6KwfWyOG8fUcI6u1pEk3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=JNIR5b97RFr7hUQZrc2LLxlU_mcykiUk35FKPlv6CB1yuDcQJ3eWAt8qRYDXKEcS4acTpK8nEQpo9E7YAxWkE76fK3DKTr1E3RF0-n1qbaYbGWx9Y2WlH5F6jxXmCIh5dbPje-4IdKYI48SIgHsJx0dfgH7yczAxMfIeMk86nGPWrPlXt4C2YfB0LvOnl7CB2y6DgIj0yzCCvvHxGauhGubeyhqiUOTS-YTWEft_bLRSULwp8bN1-zX4ez07yo2tBOXZPcYIlXMBGDKTpWRwiE8wZgyKf4ODtwDLJXz1U-L7_KOIMc8p3H7pqOMGLSvVq6KwfWyOG8fUcI6u1pEk3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=mf7-Onm0FV5Tv-CM4stiwt8LGtCEKQUs88kVAE4ge7FLLY5eJHdYej0skr-MFkcRH_qXhbsQmUjYRh1z6Qof7TphZ3yfS3XDUsKooPvfsnnOPbJrkYEoBcMYBSUhgkVAjSKlRjjSxRZX1PpFl_Wb_JOO6Brs8N3fzuqyCudVXLAI2YaxqucZYLW0InQFMaQFtW8jZRFjYeJhKbbBCm-3fzgWkELN6ax1jRE9VXqB6f0I3Oysr2skmQUs5ELX5e3-2IkLBq70pkXDU5zKc6R_Ui50wHBSOcJFv0Gn-aZEiAhqPq5Aoo7mMRqEL5bVyyPVNATrL72VXFQZokI2Y-FN1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=mf7-Onm0FV5Tv-CM4stiwt8LGtCEKQUs88kVAE4ge7FLLY5eJHdYej0skr-MFkcRH_qXhbsQmUjYRh1z6Qof7TphZ3yfS3XDUsKooPvfsnnOPbJrkYEoBcMYBSUhgkVAjSKlRjjSxRZX1PpFl_Wb_JOO6Brs8N3fzuqyCudVXLAI2YaxqucZYLW0InQFMaQFtW8jZRFjYeJhKbbBCm-3fzgWkELN6ax1jRE9VXqB6f0I3Oysr2skmQUs5ELX5e3-2IkLBq70pkXDU5zKc6R_Ui50wHBSOcJFv0Gn-aZEiAhqPq5Aoo7mMRqEL5bVyyPVNATrL72VXFQZokI2Y-FN1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPtY5pb-0GEvPjicGlkkuF0BM5EXitAdF6TC9BT6yYoPp9rkoA2CEZ96dbhE1cghl1TMRKUSQAHyeg_E0NA38UGAIAF1VyzzyO5snNxdccVcHcFAQiXAcUbb887g3I56PFuic0mgyXdSSPWeG2kqXPFLLGB9LqDd_TxwoDE8nH6OTHIC8PC7VSEsPKIXpyQU8KV7lSE9uC8DY9eS-XwH08TR8PrYNiTtYy_OTjawqrHhMUn0XRpyMUBO9Poou2_R135gfY2GIIcS3aRK-u2XRRfidmuv7e4Vh4Z5ZC5vKFMjo_2WAF-lEzbkmSWdC5LViCLpmcsg9EqcUFkhTFQtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=AY1dpotIq4H-eyIxlmuZTgvu1AXVJcC-iBzX7VMXcsFTUug2_qjWLlVPbmVCLjqrWDKoSx5WY3jP8W8Zpv8ik8Ckize8EPhkTy6yu2nwJ2o99fwN4YIsEwNfqyyq-mGe2xkUqQ52QwDvvRRgq281nU5ml6Mgr0njC-Y7JpX1GSsnLvHYBLHhCfqCMBXwHdHl5GX7OEooj1cc32Gotu5FIJba_CLBzYPou9Eix4rvwt1D0MaySAxA4N9-sKW7ekeNLvPu2FCNmRAYSyVmfaplGggsYFNdcdzoXiprpqZGPsAzrtV6uzZE41I88TbWiZXv-ZUqC_Q9Vga7M--ye5Ke-0MHyk_7gGCYqRxFDGUz7NM_D_-aDo2Sw7VWrb6N8Om_DTlGuUOHHsTxNg6ktSkZDdmgq3zKoAdrWkJqu1GTPc2A7R2_Ney9NEEKTxF8h1pPkCSJFRyB1AWiFkR1kFu2tZ3spaRfXCvWqhgKRZcywTZTFpn_NaouFZfWSmjdn2B6k2QWWemE4LWhuihrcI3MVMbN9AI5g_2Nv_naDkLes75Z_yDbsGaISn2kS3Vcz-lhvbJW0wQPMyvvhLYlDzNMIXex_zjGvcxouCNUomd1Ais0A4HCbqViqgF9NabXmh1cAYBuIUTkM-3b70j6naGZlNZS-Hd-CSqeIPd7Z1yfKh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=AY1dpotIq4H-eyIxlmuZTgvu1AXVJcC-iBzX7VMXcsFTUug2_qjWLlVPbmVCLjqrWDKoSx5WY3jP8W8Zpv8ik8Ckize8EPhkTy6yu2nwJ2o99fwN4YIsEwNfqyyq-mGe2xkUqQ52QwDvvRRgq281nU5ml6Mgr0njC-Y7JpX1GSsnLvHYBLHhCfqCMBXwHdHl5GX7OEooj1cc32Gotu5FIJba_CLBzYPou9Eix4rvwt1D0MaySAxA4N9-sKW7ekeNLvPu2FCNmRAYSyVmfaplGggsYFNdcdzoXiprpqZGPsAzrtV6uzZE41I88TbWiZXv-ZUqC_Q9Vga7M--ye5Ke-0MHyk_7gGCYqRxFDGUz7NM_D_-aDo2Sw7VWrb6N8Om_DTlGuUOHHsTxNg6ktSkZDdmgq3zKoAdrWkJqu1GTPc2A7R2_Ney9NEEKTxF8h1pPkCSJFRyB1AWiFkR1kFu2tZ3spaRfXCvWqhgKRZcywTZTFpn_NaouFZfWSmjdn2B6k2QWWemE4LWhuihrcI3MVMbN9AI5g_2Nv_naDkLes75Z_yDbsGaISn2kS3Vcz-lhvbJW0wQPMyvvhLYlDzNMIXex_zjGvcxouCNUomd1Ais0A4HCbqViqgF9NabXmh1cAYBuIUTkM-3b70j6naGZlNZS-Hd-CSqeIPd7Z1yfKh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_QRQKQl09vYYt2rpU1m1VTSVBVWk8A67UBfbd4KIZ9xqEFaJd6N4bs2S5e8u_g-OBM4OVD7yZLQvDyRnzHkTRpJOKM2EI11Yq7qVUTuhsDtWHeMMc3sS7jVt9-9F_Ascud8TXAGetjztAUJbPOQ-H3EHmk7lrxHlJlhU2hmZTYgwM3si0MwrgKzaAtybI78YYV00ym3HJt0yA4spWCnNf-zXZvDhk36qfwgE2246DZUvKP4GBWqDxa0aSRecryeAzb0Pdkl8r1edLwR8tStdeEO-pi5y6ec6ukJwkMGhUKdlWm5jPtaW7Z-67bDGwvqpv_k79tsUzfQq4auXEE-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paLSW1DTYvbes1XAwLrSo0onOXIYxxo-L8KG3V1YLq485eI4zZR-62Tm9X3DdkHihYMRjzBPJuw4uKHmVGslDrKtzZQBc5yxSa1WD9hXneRiBPMRN94yND4Oy-AMvFU8Tce0cHNlECoGfliOjvmbGzzimr8IfGJD1Ij4ZlDrTSeIc1flaoW5zA28wULkoal-Qqb7gb_F-86ulwp-x6cS2rWnhWOyB7oIkkAPT0RtQZS-GpGgB_TV478JFRzCboSsr8LxnvVAE3QjEtsErP11-oi0fZTMPfQfIKlftnYy7DIM58AMZg2sQju7mj9ein2-G8ICxS1MBiuFyH_8GNnQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=A1y3Zhe1XIt-DSiWOfHkVNdk5f_Y2d5w-cGyOq650HfsN0uiotiy94eA5IHNrSwE5DrxGSp0PlnOLscfD_lwDmNtxk9o5Tr2rZR9jv0EqqkzU9vKdQGzpY1dACeCF9z3NWJLkb4PsA7wtYACXpYPwXj1zsLe-XK1O3iikLAGaIb1rSL9Ox3i0nGl4xdW6FfyvJxZX3RuWXaIRhcK3se0AmE1pF8NKYymdnrTU7Axm39_8vrREOQTo4xUofSf0w5XU8-nVBDf_7jFZ8NR_c9jyEKVGdETk32Uqqmw7Z30Yi4BijJIrRNFvCb8zDy3_YLw5OJydSTGOoQGAxk10y4lDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=A1y3Zhe1XIt-DSiWOfHkVNdk5f_Y2d5w-cGyOq650HfsN0uiotiy94eA5IHNrSwE5DrxGSp0PlnOLscfD_lwDmNtxk9o5Tr2rZR9jv0EqqkzU9vKdQGzpY1dACeCF9z3NWJLkb4PsA7wtYACXpYPwXj1zsLe-XK1O3iikLAGaIb1rSL9Ox3i0nGl4xdW6FfyvJxZX3RuWXaIRhcK3se0AmE1pF8NKYymdnrTU7Axm39_8vrREOQTo4xUofSf0w5XU8-nVBDf_7jFZ8NR_c9jyEKVGdETk32Uqqmw7Z30Yi4BijJIrRNFvCb8zDy3_YLw5OJydSTGOoQGAxk10y4lDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1p883qRaDhA8ylGFiklmgSDzpFFuxwuz4Wqg9MGEfqGdfcYEOIf3_mqXXsRqHAWH2yZuRzX5QEUqaW459bypiooLLMy3BCB3_SkKG9s40pIWFilM892E-z8HXPb39OVC6yei16NDdBy7jryXzL1Cwtz-ra7JoTgFQSA2xT9W56FcFQTvvjgX8n3AvAPkxhmf7NlsG3_bsXPa3Vb6qBo20eHZhxG7A422GlVdHP8vqaFDsxY3rxnupwGrckSk4TwTnMV8E1tjfNziWklnOXUXb1ZZcKPoAxjmxNFHchRo54E5pA_9qEZJKRFzKNXF9FKCOBZYKpuyYQ2hR44gCaGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=l_AEvVIDiW0E6LrBLHOEXg7DmV26LHAta9mV3hN4qlpTbQF2uD59aZqqu4EJq8ohGqGa69DYPX-qioF-9kzf3H1J04x8jLCsHiBOPc-_HNGQFUYZ0TnFbXbN54VZlum9s4gj7Ffcood1yYGAUpOwquI8NzMe-W5xxQd_Su9CzKs2K81acYa-pDM71yWsoFqUNftpDFU4Ogzg0NbVlnQX36I0sjul5yQna1FZ-71Ou6aq9yZJxV3xsJ4YpomiwmlWhUDXqNoSXultqNtB79FPo3hf70I8dk2KbuHJHchGvZ2wsDoUUDTpvMUPH2jNCHY-j5t1PT6knhGu2yhrXeC9Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=l_AEvVIDiW0E6LrBLHOEXg7DmV26LHAta9mV3hN4qlpTbQF2uD59aZqqu4EJq8ohGqGa69DYPX-qioF-9kzf3H1J04x8jLCsHiBOPc-_HNGQFUYZ0TnFbXbN54VZlum9s4gj7Ffcood1yYGAUpOwquI8NzMe-W5xxQd_Su9CzKs2K81acYa-pDM71yWsoFqUNftpDFU4Ogzg0NbVlnQX36I0sjul5yQna1FZ-71Ou6aq9yZJxV3xsJ4YpomiwmlWhUDXqNoSXultqNtB79FPo3hf70I8dk2KbuHJHchGvZ2wsDoUUDTpvMUPH2jNCHY-j5t1PT6knhGu2yhrXeC9Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=AVpRoRTxbO_Q7Lh1mLx2gwYsVnBwLre6rMJNP3RwAixNkWiiA4dcNKshebszzVHz6UCH4uh_RBiDrlzJIz6seAEQu38-ZrcEaxXAOkK2cCWnyvEUCEUdz5TLqjeZmPnmv3bLyBAEAiEBV9k7kCWM_jf0zB1C0pmblMyd4dAW7f9tXml-hCr7AWXZiGtmBYOT8SNMms9aSa7NRGR4pgsIpwCNGSrapOv_sws_UvxHpkutz3vBoDkiDxYrPqUVNzNHVyR5hEHy_rksaYbWRctv899DgxQ5njQamRH8YZuTkNcw_c5cntltq09v-8LzHi2Hcf5sb_eO_K3oT9U4HZA9EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=AVpRoRTxbO_Q7Lh1mLx2gwYsVnBwLre6rMJNP3RwAixNkWiiA4dcNKshebszzVHz6UCH4uh_RBiDrlzJIz6seAEQu38-ZrcEaxXAOkK2cCWnyvEUCEUdz5TLqjeZmPnmv3bLyBAEAiEBV9k7kCWM_jf0zB1C0pmblMyd4dAW7f9tXml-hCr7AWXZiGtmBYOT8SNMms9aSa7NRGR4pgsIpwCNGSrapOv_sws_UvxHpkutz3vBoDkiDxYrPqUVNzNHVyR5hEHy_rksaYbWRctv899DgxQ5njQamRH8YZuTkNcw_c5cntltq09v-8LzHi2Hcf5sb_eO_K3oT9U4HZA9EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=oEpsE5UdaGjfLH09h8wHcpHS46LceTM3km6_loORFrcxgSa4Irc2hWFapoYh-CpGA1UaRD2-BRaO4g78SYrjiWfT-COH_5xqhKD-tSzhwEm_4pNh5jA6PM8IWdjNt-pFez6BH1Hn3ZiW19LcgFvx9XdbaGvM1E1XVBA5AzVOiLpyYKCSyW1dc2oYVxt1i-6G5ChXAQQvi6oq0NbqQzsDhX6e0Etb4h8Q3v2mju61wqwKYNdmk8JYjcSDFhR6XXQUoQZUq1eAW9ZENtKK4PjQoVsjxgpevQzvsODSHZs_Q-lvl_xIrarJG1GSeEaxNsXS5CQrW5Pc3TKQCl9MDebi4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=oEpsE5UdaGjfLH09h8wHcpHS46LceTM3km6_loORFrcxgSa4Irc2hWFapoYh-CpGA1UaRD2-BRaO4g78SYrjiWfT-COH_5xqhKD-tSzhwEm_4pNh5jA6PM8IWdjNt-pFez6BH1Hn3ZiW19LcgFvx9XdbaGvM1E1XVBA5AzVOiLpyYKCSyW1dc2oYVxt1i-6G5ChXAQQvi6oq0NbqQzsDhX6e0Etb4h8Q3v2mju61wqwKYNdmk8JYjcSDFhR6XXQUoQZUq1eAW9ZENtKK4PjQoVsjxgpevQzvsODSHZs_Q-lvl_xIrarJG1GSeEaxNsXS5CQrW5Pc3TKQCl9MDebi4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=eZG4aFZhrfPPg2GZ8nf9AEU4JBiRcZWou9o9siEdXAVF08bx8Cfl1A9AHqgHxDHVay0sOJ2pVZhewMKySmhiuDDHxNc7seFWpsv1frJC4tlKJpBdLP_f-zwoaMsOwVEbjnnNqmTEHhGoyVMlx-v-DLX6NBR5BjVbC8WVPAencWDLIqSjfHmhTyuDzfL7raHUr-bchDFFRzgAZ87M-Osq_3c4zINNKDy_0lF7lPqG3PC8ZXKohUplOYRtQtt8oTUm2_584ILGqrND8PQlVhnRWafrbXBl06jQXl3mJnDqYLNLJm37Rs1al1h7Kygbkv0nYghG7Txf27DZWOm94_RsTLJ35537vTxX2cjr36jFhIk2teOcdgOoOfw_qOcTYrCGwlVP4s2U61EQ3KFWD_N-1nIFxk5sSIYY4Ufr6woxsHzHNdfIsZdz89QdljBsoKtpjfBqavkK8KSAQuNB7vYQMwxg0EM0PY8UmOmlLrcAijbZHEbkIt96kFniP1b3V5PH_jWHf9Zi4o74yYRB0IQuQKoWzBbty1pqm2PM30KHz4EBbpxldYv6myBhR-gj_KkTqGICecz3Yw9GasLkOYUYhDTD91PLFO5NfjuIlaTi5z_D-xjCO_J1uTS_m05UaV7HECJ9ISAqWFtiYxHjhGAGNnS8UMgAXeiyfkZ8VyLjqNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=eZG4aFZhrfPPg2GZ8nf9AEU4JBiRcZWou9o9siEdXAVF08bx8Cfl1A9AHqgHxDHVay0sOJ2pVZhewMKySmhiuDDHxNc7seFWpsv1frJC4tlKJpBdLP_f-zwoaMsOwVEbjnnNqmTEHhGoyVMlx-v-DLX6NBR5BjVbC8WVPAencWDLIqSjfHmhTyuDzfL7raHUr-bchDFFRzgAZ87M-Osq_3c4zINNKDy_0lF7lPqG3PC8ZXKohUplOYRtQtt8oTUm2_584ILGqrND8PQlVhnRWafrbXBl06jQXl3mJnDqYLNLJm37Rs1al1h7Kygbkv0nYghG7Txf27DZWOm94_RsTLJ35537vTxX2cjr36jFhIk2teOcdgOoOfw_qOcTYrCGwlVP4s2U61EQ3KFWD_N-1nIFxk5sSIYY4Ufr6woxsHzHNdfIsZdz89QdljBsoKtpjfBqavkK8KSAQuNB7vYQMwxg0EM0PY8UmOmlLrcAijbZHEbkIt96kFniP1b3V5PH_jWHf9Zi4o74yYRB0IQuQKoWzBbty1pqm2PM30KHz4EBbpxldYv6myBhR-gj_KkTqGICecz3Yw9GasLkOYUYhDTD91PLFO5NfjuIlaTi5z_D-xjCO_J1uTS_m05UaV7HECJ9ISAqWFtiYxHjhGAGNnS8UMgAXeiyfkZ8VyLjqNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=o0RRWXs5FbIpS6RRq9uQ429DR3LLC652n3ajbZrxA7m1Vs7miJSqeUz0Bwf2ww_VodEdlx-rulyD7aW4uRcxaJRZYCUOc4PjnLg9KWQtqSckHKpy8x7Y4lY5TMGGpmZJybbdfzsnTW1WpFTJcIGchJgKSOGd-_1aKEmeBFwQhw1l4KBMkHyhKhTWYji7oeNP5v_biOXRnljqZ3SOxUpboco_lUozuL1rAJoJGOpLrW4tJ_H9nX3aptosUeaHWRY9NMv8xpHGM8dX9nHz05-hYDV3vCpJ8Yxjy3jmeoSSHaSMayj_W2z9Hmzlpr9XZWq5xlAi0GHOKNTAj38KS49Q8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=o0RRWXs5FbIpS6RRq9uQ429DR3LLC652n3ajbZrxA7m1Vs7miJSqeUz0Bwf2ww_VodEdlx-rulyD7aW4uRcxaJRZYCUOc4PjnLg9KWQtqSckHKpy8x7Y4lY5TMGGpmZJybbdfzsnTW1WpFTJcIGchJgKSOGd-_1aKEmeBFwQhw1l4KBMkHyhKhTWYji7oeNP5v_biOXRnljqZ3SOxUpboco_lUozuL1rAJoJGOpLrW4tJ_H9nX3aptosUeaHWRY9NMv8xpHGM8dX9nHz05-hYDV3vCpJ8Yxjy3jmeoSSHaSMayj_W2z9Hmzlpr9XZWq5xlAi0GHOKNTAj38KS49Q8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFvfLoN57m-gbq1N9hBeBGFbs3uIHyFaN-hLDFzCYAsq7lS9xbdBKhkvkZlnzxfkjq8BFeTlBttC0u2hZbSk0pH0nYJBkbudmMfucbgjlMg8By3J0xbY50LaO8OsZuwRPfgCSBD7UfvjrY3kXTWgsV92HlFbL5NuvtM3OWMi2xCRYcguuiJ6SYQxRDPAhJeh4P9DS4JWgxBtV-XIqnbY90aoJGaq5XwGUDwnOWUXJEehKZ9_Rzx76r-ATaiiU1DKccy8piTu0JQyEEQIP1AJ70rJDNje-QhNOOJMlhcS5Mva5UbGQefHzak8OqVtAwAriDN3Ouch7q6Qk9sB_sg-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIH3XdAT8m0_l0D9sH__J26sE4qK8BZXqGEFgG2sJ9e0vH_lb_dh0C6QOqzmtB6x_WBIRFhDhVzMe_4uS6ctBfj4mgX4QFBeaVfFN3sj8UizldihlyC2f6CZa2lTwaXP2c0g025djQu9Gwc29ntyOnQPYfTePwy-Y9RQm-URbR2elB4UWyokoNmyfL4AgtrylFcrRtgWpUyiF1l3VDRKrAnkiwhGXJSRLVY8HliCrE4jsJk5sPU_jYLk_g-6fjkumk1_j1WJukTrXWJSbQNjp18-c4j5U2gsBbA3nPVHo4-TKBwWre-xsHP3MNqeukSlIbbIf5W0XcTs6tfmuup8Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=tUId2P_N3-9JXearhYlMtl7n4qlBun_BNrRf3-QPuKNAHsveHhyQ4bmabey39ISX5I2PT860wbuQbV_XcsbfMwfS1Y4YaM4bV2U5CQwZxGpnDprzKY2mBSclj5TXFlWw84AyznLICUMFLCzr8w0po2SEZRxPYtdJ44CBgmqGVnQw-hMpPaPD8nlefLyiufuppjAycMrThdY09DrbeZb927ePk8aZOpF_jjxUlaAmDXlJX21fyaAnNeYerBcCDs6kZD33cOmGHKsgqmSlUROnaBBjND04XzeUSBlcVFh259_MCiDMmCU2To1krge7tnA67e3EQz78kZZbfzFsETuaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=tUId2P_N3-9JXearhYlMtl7n4qlBun_BNrRf3-QPuKNAHsveHhyQ4bmabey39ISX5I2PT860wbuQbV_XcsbfMwfS1Y4YaM4bV2U5CQwZxGpnDprzKY2mBSclj5TXFlWw84AyznLICUMFLCzr8w0po2SEZRxPYtdJ44CBgmqGVnQw-hMpPaPD8nlefLyiufuppjAycMrThdY09DrbeZb927ePk8aZOpF_jjxUlaAmDXlJX21fyaAnNeYerBcCDs6kZD33cOmGHKsgqmSlUROnaBBjND04XzeUSBlcVFh259_MCiDMmCU2To1krge7tnA67e3EQz78kZZbfzFsETuaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=renh43z5QFABcS8BpNH02cr1ULNn3DeQJkjM0KnYyvBdns1wj5cwmzqq13bu3ccSd6D6KLJqoFAGHLW24ejU1m2vRXi3XMS7J7Ayv8QEx9MqUhhQ1pAoIiXRaxcHve_o5WUn7LpgyLqWeJMdhrlGeiY50bkB_MflM3CfxG30YJS00gv3xeFuxPXqxOfqe5BHVnVjXqNs6jf4P8ifB6cbz_5NAWCkubXUQP8tDaYMtoZBrpB4HAUSqWcguUQUpONcBwDIVGx_fsrcMIHbxA7zM5rBukx-2JK_kbWd1A6SeHBCNd2i50JudMiBwOqiJSFrN9SkbboAFvb71IzAtYlsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=renh43z5QFABcS8BpNH02cr1ULNn3DeQJkjM0KnYyvBdns1wj5cwmzqq13bu3ccSd6D6KLJqoFAGHLW24ejU1m2vRXi3XMS7J7Ayv8QEx9MqUhhQ1pAoIiXRaxcHve_o5WUn7LpgyLqWeJMdhrlGeiY50bkB_MflM3CfxG30YJS00gv3xeFuxPXqxOfqe5BHVnVjXqNs6jf4P8ifB6cbz_5NAWCkubXUQP8tDaYMtoZBrpB4HAUSqWcguUQUpONcBwDIVGx_fsrcMIHbxA7zM5rBukx-2JK_kbWd1A6SeHBCNd2i50JudMiBwOqiJSFrN9SkbboAFvb71IzAtYlsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFk6wPKCzn7zwSapIPUJjLXUXeq9cfiQBsjVkM_9BggMJ2NUsGwiqYIO2drMolLtDjGdkDVIDTepvbLYoVEiLb_wOd7V-_MnoyepcBHkevEb33c8F93WG08I_6HX7JYAEc57MyLWBgRC2S4YbkEHmTfzDxhkMPbHe5Ia8_GdhvxrvcKul4uC0xq2X0HnAvZpuTZHpHo7sC06KWg_lw1AY6Sy9ES9VUFQXZUNLo9uLa8Zg0ZJ5CdIo_LMaqRWptwl-Fn-szpM0e0zx8sG9fYxTGb9nWpkMvi9TAQpoUGBostZRQdcfhmQJNyjU7TCVeVBhaJdn02jEwJzrHIzcp1ASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
