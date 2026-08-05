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
<img src="https://cdn4.telesco.pe/file/IDlIcgVzMC4pt-LUkL68bFxexMQ55XE5dU7OKE9PK8O5hOlBj3zUxsmfyp7hUjR_IvosrcnS3bgIo0bJgHepZqZON23PGvpHckxqKM2XqndUBST1OZuvrSNplbttYq_A2a9h4wge3yb5GS5YQr9608ZqGT34Petkh2D9MooMv5kvqg52t-wCvP1M7-RKVoFJ_LZ9LGYEQEV6Shse8m1_CeQsVuCyjbbgyHx6Yu-hgTBdXtx0Ah_FSf9cW_7Ca9QwljBjUNJpbZK4t49-PfF_PaVn6jirZs8W5Ik9xQ7oIMp2bhk8NGsaI2CqwjH0O-tHlFszLgocRnZDdpMuR7pIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 626K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 11:06:15</div>
<hr>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyWNoL-SDPM3IVNXaSstWde_17KRfM3YYNXL4Yzuh9OJtcu6hS2ELmVOhjt2qaInaDJQrlmxdAvJNuOHYKPV_mW1Tu1y9t6rJTK4PMYbmX00GC4QXN1hensvS793_85099gfQ6P0KgsuyxsCaXdS_XIlYOdcyjNfYEMLQt8JwTpsdeNTfVnYMfbQGWLs2k38bv0iAuNBpiUs6zFoPWQFZSPluydpGzirwuHEf8YIYbMEgMJs8VbLxqrML7PwwfsbI1MvIArPoNh716O9h4C39UBK0t3ZLU0AwS_JV-w1fxweYvqt0pGsfaq175Z3nCLomYlYEC3mUxXApEk9q-umkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=rHRlrZ3wfA4zSVGRkLhkY0u20Gj-9rgP93_6Cxvyq5fQKHovBqpTp7rmFTOygIFKr7wFZUqC9s8TVuU1LGKOW2V24UA-f2pK0KJhjUtPNMsTEHwY6M11Lw2GdIVrG3FE-xMX0H2zJpsj_c0gu0fW9FV5hBoZ5KS5bq6Maxdo3l75bHPL-GpwKHalrJI9h9VHMLbv3K2vkUtMs9454EPw9BJ1dJZGHibqeM04mIseCCQRvp38ZRmKzI3IEBRxIg5shHuZo70Q5g2hlJB1f4g2y-aLfN0SvN965HMF306pjEXfaFn7mceptbDfHDDxOrymkbfXuGkaphw7G6dYKAE58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=rHRlrZ3wfA4zSVGRkLhkY0u20Gj-9rgP93_6Cxvyq5fQKHovBqpTp7rmFTOygIFKr7wFZUqC9s8TVuU1LGKOW2V24UA-f2pK0KJhjUtPNMsTEHwY6M11Lw2GdIVrG3FE-xMX0H2zJpsj_c0gu0fW9FV5hBoZ5KS5bq6Maxdo3l75bHPL-GpwKHalrJI9h9VHMLbv3K2vkUtMs9454EPw9BJ1dJZGHibqeM04mIseCCQRvp38ZRmKzI3IEBRxIg5shHuZo70Q5g2hlJB1f4g2y-aLfN0SvN965HMF306pjEXfaFn7mceptbDfHDDxOrymkbfXuGkaphw7G6dYKAE58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn-IJyYqSHieUiomEMsYNbXYs9H3t2tjrcLZzg3CQ_ewKyDgcHkore_hxLR1HN2z23ikNyxufgeQmtSDij5uUoBRyD9knS49VBnnShQrNDLPDp0pzK-qLObVNkSObEC1-1OAaqpZGRBJKc5f14SB_T12Kz1OS3evwpDVAmhB1zBzcUSi8-bk2b1ahdhCitoKqTRcPhO58-uU2zgSNiEmM2_-DZxm08rzMgwjBI_o6HWmKAp_18OfKbLD9UHtZCVtvQeSQYU2iDYl42THyf2w1iJjE-r2MGDKp4xaRnBaqS8z2PGsZ2ynYjuYR0HIyC5ZLO2mQFjGaH1z_1gB2LkyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDykLp6j8KiAm8fnV2XoUKxRWi-llUV4_lvPMyFrwjPxYJcIOgYTTDVG_G9bkQ3nAGaZmp7FX2otNbsBujm0MMd8rxZLA3mczACM6kPqUyP3B5dsYHelcGquGZ63deR9afFenMXs2PnFN3IejsePtezuVtdRYDSs-gGo9YaargsfAaX71ZjnmeehcFj8G4hpX2rrZncvv-i7f5h_pihUvZZz0lhypdta67SELA7q3-G8rridwYdEPa_YdilBhTK3ByfnvLLBE5tKr_PGZedou88oeEICkwvJWCIn77A03M8EAb6LfglW4O7vQqtOtEP1dThas77PYBX0EGQkBU8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ky3MnN16YfvEYwMV67zXITc0tkBtoGTHMDWvMLr5DQ-RbIjbHwo9n1p_UkVmXk6If4ojOA7GeuHMgrsajjtj5r7HszA0stC4lhDA5r1m7_Wlzqv1XeuaX4XLwe0wxyWpbwGH-SatELoo_UQTqZ5lLDusVzvgvQCoGlfOiCExRdtm7kCz6Mtsq2bj8KXfGYY9iVRzt7R93qkp8hX03jTSdGPL8IkQY0lfmOO7TGnznDPPkif7hHu50kIISxU-GxUCO3_YxRZM9sg9EKEN8GRm_0vkIQhQoeS8UIRRtUzO0_VUtVojcng095rJFXjTY9UV4w3jRvr1fcILm94m7g0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVrL2ZVHZdjWtce5zjjZEFDHo7RBwsTKHmuSghvyMmXA3-3bQIprdSPMqE49o6pdjBBc3E2o8CgU39zgft9EDxUzYLRjLD5FhQnTfTxd0LheDxTXpoarYSgLfk1Lck9ZVpkZDBOP5tp56pgnMM1yH1l5TWVNxIzJDLRiUuysTzf-HZQYsJmrZT9ilH-f2yVG1BS2QVztH8UxEYSV5g0qw68yVGmT8oyBMZMrARj7BUAne-aLgpvCH6aFb1Hyny8K9N5h9-KpCmhqmjuBioJ4WUGduz7gqncA_hiQgiS7m9PS6CN1rzG_GEevAucyqvzVINv8NrhsbsWJLiEO14gRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHb91UhO4uAYUrEC3XHp-156xTpKIPsITwEzJvAFP6VpGDrF8lv6veEASWVchPoYbvKvxpPDZZmhHoLznFlIDwyVBMWYbQl1qEtbvi1Z-NvM0_jFOiqBui9hKA9e5Ba9Ce0u900vA1ArwumthEoWsDwDeQxHzJFpC0vSytJJNtkU-79PtdUIdHJipcjTMGE3E00Vge3xuGqLzr1OCYqDqdLMWwuWqcBdQ4Rz4oDw1I_3Z9DQ9VdjMRDH4ToevUNAxif4uJnlPq3Z6c44ZTlVUF9x1JQGs-FD0rG8v5q0yrO9MI-1Dmpk9ZfqBDElg1cR4eqAvtKUUhUKXLOleOsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfiPNVkQ6cn_Nqu90YM9A6cNW_cCqfSipXNFgquHphgb5BfnvKWtU0obNBLIvvG2xc5L4X-5K2fGfg7DdJ29YtNFNbCHX-f1R3kUrbHj3CFPPwMEx0Xc1C7_5aNGLC71kIMzkvAhz01o4ixSvBsMmRywNHFIMnt2yp4dcAiortv-sj9UYZQD0LUfn_o8uIfGsT-p14ajsMXvhdbFR7SIy2vu_26B94eu5Lp7VDgIG7XipGMWtqwf8XNvDLB_WNhei7eyDd47ayPTAgchvjxVaTJtvfF-GcNc606GgLkMr8SmpFIaIWaituRC2irpw9AXHNQ6VkSOxUDGUTxlM584CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roXqTXiM32UW6_i4clNY1rEwASB0BRtbpzHQEr98PL5krpYGIMJyiJygVStDoftcss7U92Xi1wJJ_yQgAk7_d6KKfppsoZTEckImt-Hz2pQYO47-lD6G1HpCmsDMSXRFnu2e-EIXkR6wLXHH6fB92xyxYMM34JO7amsYRUzkg1uA9JvLMyOZtGcPwF8FH3wiM0j_r6wpgqDwj8bWtU5t3nNkQpFVLoIoBs31mFaCgrduT6vXVSJzScmoTEWXX_mfBmMyCRdDGUXNg0RUBKxl90moIYPomPsluAznme2ljKMB60GQ_lehT3Ue-24csr8iTsC8TO6wsqc4yBvBhpwo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/27125" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1X_JJEipGV5I_k4zJT99ZBtsMCsDUjgfgvkBC_TVhvekglmbehdrCK2FNbj6mD0tZyr-CyUbH3B9r4ccDIhjTcwyW7deFH6ptsIeEA56SP6rBnQvpEPkslvhBpEvb440yM8DoAxBYymXc07SownFjQrDFtckZFMyJlWXmKWA61vrDkfCYnb0LwFyYhi867Yy4g5fNYoepEjaFGA4U6CcIg_vw22SSJJ53PBJz8XDyV7GduvIlgZ7BAXRDrrPHTgmkJX6xyd7_v3H5i8TZSollYAVwenEty48fFDtXyWVFXLIphTP3eWqzoC9HruV6Pwa4KAYfsn5N0aCAIgXBNOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjvSYGksE8eLNsCszDCJdUSLXrsw1r8knbFNYHHNRRc9KgRVsDw2aSRjRNQsaEwmWqyt52hl5Jm-VDyZf7mlVEYbJf9g95VpiWx8saIme1T-fq8BKHiXvBkjvSVlDuk38SSyqbuqJWd6SYxwENbEg0ibEqwkEJxfF4Z02JXEgydhDNuyumNT8kolG4Wz6IjnM8OIrxhWDF3Fn_qS9gzuhK_pg10-jMrJ8vw7GBNsoixGZQHttulWn_qHfZSiUB5NgtfoCdE1K1756nKaa8ZQMVJXqVF_nLDlhIzo2lBV48K4RpC15hYe7kAqI9rhntikadauvFPONS6B3wfx_179Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Px2pTfHuSEjQ3yW49ToX5BpYq1i7SArOJfRSQ7GcLM9IEZy5pO0ckAe3nBcOZjuqSP5uqKSdyi6jCPnQRHohHTsDJso8yvqVBrT8hTq6pHVWfMyBG_vD3Z7UyIcNlCNGbLK4aBbq2URZUTEFmgcrvCCRWJxmsYJ0PXWRw6zlXUJ-1de05axC2sBSaZLkVhXYm7P3UbjUz11AMluokcywrCdErIUhIYO_hwo92G7G6XnduPqBJubYio76jDuQCVGxgGI1m_tScK99oUeF2gBcNpzemRIBzSb5LKma1cx88MBqnSi3BB2AuyxKA-1jTXAfCNBZ5LhfSCYf04CUeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c01adXPElgswivrea1atQ8Jgvpu7GfRC_3GZ8HmdY4N0TnruDSfvQflb3zYhtJFOudhpXqTAENP2iqNq6fUnXDOKGRw9z3T6wmjdslhrj57WTqslVN3tzHTdBoC5Ie27noTSWtT5zys5M1uTQa7XTLEqnEbzoML8TZ6ngUqAq7oL4PhIEOWa5_kl9IdMSyCVdkp5bQTD1E0bRdiEVkP71VlgfrmUPp7uUi9Km7NIZtniZMxjajgtmhkOUEpSQ-qzze23i6iFUkbLuRLOHzyeoJk1lwdDofAVhJJ0w_cR5OqWeOaqGs6IrmbmUAFSsk2Bcko76MJxRhYzMkGbZ0Hv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu57dAGB7x7AARZXE_ePRBDSbGS_PYFJhs1_P8YrBRhvC-FrZ24cWYLQjGa93MFIrluHHAS32D72Pfc8dLkDEWAgG_Ujk_pSmvBamT4yHo7o_MrYovGFpTyRb1lw6CxtaYklfJkkr9nLNrgwk-Kzlx1erjgT9BPb8w4PWbguQq88SaD_iCaqsHztHSLQRr3-6Ye_ffyv949HHS_0tp1q4iwqwwwzEv9Zmu_9EUv_zLUTkNOLfx_uJRpelwKDnA87rfSNNagFKhGa-ihtqEapI_b8baNSDU2CgRqVE6CPAlnIg4WZOOya6u--Hj54CpEc6-Rkq5vP5lSiUqUwGfNzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBk-DGzMHI1C3v6qzozIqC6zcMlfw-_VcQ4vfTSr4NR-4h91M8Od_zdBmYQ2jjwZvLm2EVdTDy22siyZAPck2xtNR_ZWAm1VlFizwQBTIiM6P7Wt3C6lafJDxLfvT5hWp77WqoXmFGJKCrSrDbOo19NP3zEJ9PdkFV8EK3pVTtM5aEh3e2LUu61gdkKdM9eP6SpUCIvCdXgi_y2_5IR6Lk4myjE9iVIWoBwaWFs9gYkeWj9RvHyMw1zapOq83nl2Tx25kSoPraaAmCHWAV4uxGJdsduCWh-ZK2zlHV8m0hLexYp4EpKuomGgb2i4lkaxFKcnEPRTuL_vIUTxsE9DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAbD3C145jxhbnWFCJmbqcOQ_tdXfrF1UK4aN48q6DCP-Ot1HWpT4glmz000nrVRaNU-q-b4311BCy-NWHNfKAkuzzhE3D_rrjlXzGkRuyPNWOm7uweoYzCHh3pAg9-j3qGhJyNG4P0H0rk0H1boaphGnnVSeiSis2C7egV2ma_pjgGQeOT8b928FyCJ2WvWqcmAudbQZVs1mr4JjlEm8LgjAS9T_NfoRjbX7GJW6HSAMQuFPtowEGeaV-qCu2MtrXz_QrSA2BZ2rDLRZzmfoqDuHZ_UlF6WFWMyS27t3LhAWY2-Aoi7RCyiLazsJQzEQ4WhCfSTn_Yr5x5XgpFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfkCS9H68mU_PJJtPR1dOj_zvtBqLmWrHEBgmfGKBzOrx8zItRR1UIjCV41Cdo9kd9W5ZpdUS6OFTBHGUEzQCkXovolfusvDX29tFSviGG38CfqP6z-kIABjDh-bT5pHioP94zmJswh9i371SyM_0tyg5EOWiWIyYgB5KVUPCz7onqdJnxgIRvAbkMIUWCl71pxKr_OaOFEIW5ko0J8tcPCCq37A0sWbgYWVfk09JyIOl-HJ0abi40KoA0xaFRNBPkmnc1gFaAOXa0Z7gR1Bda1f1-V1zImoo0gqqs894k3JXsOxrpPsbb_LqBmEZg3CuD5nb7SCtSmYBnzKzQXRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWGgN0qtBBCTMP_re3UDCOz8IgBCMni7cgENy8NjJmaZRx2YzWfvdGL2ElgugbNdXJ7TBFE9RwtxWk4VLKaXK42-SejSVIYcPs0Y2NRH1rm799-KACoJfQoAqe9TG_6bcWBeB_Xm-MExwJh0WNv2VowYgZNdwxEyAsRm2H-OBwZkdaUkoZ5MZMHK8bWcxDTa7OBxsZ1uMhgXJv4WpeW_1CgGNLM3C4ze4P2iShQlNEHpJVfKTr8CpKD3yNwkTJ_bx7Q749Yf4Uhj4Y0mq-pyyacQ5_Jy4mlpolISTnQmhwWwQtHkDY1FUF7iHw-UWn5-dZzNPwbv9N7fj4eF0EXXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q42LjlUXyZKsYxEcyOkQ4OAsqVN1BZXGncGQNwkfjawuPGyr8C3hE_2zQQ3O5V0gI3MaND3-dPr2ir2Ag_X9v_GA9g9kabdr3qktNI44Q_O19vYezQIq9wi57U_aZSRlcD8V2gYsxpjJystLiUt575-ASyMbHnbAg43-QZSPT1nHJ4B7ywMPzdqQyzj41MWN1s3psmuwOMHoF1Bk3GQtBoEXKorHYUnJyG81cEYu3SPREVDYYiEcKTG2q6tSZPaUv9FQQHbdKKxnP1TDao92Yi_2fSVBKjmctvmWziAJ3-zNzXdBnfpng-wg8bczxYHLp7kk9CRUI6EpqBT8xIguQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfAbLigdGpwzS_SYmd_1vgERTjy0PmcML2IPdP_qvpouPooVLwk16OtQ29vLshI7Ci-ubf5gRc0g-kxeDvG4JVIGBsCz_F3mBd630hgHDNT3u_ymPD7iGfIrLFnFiikU6Nh67mm2AqVOEuPH8UHdI-fyIluAcGBOym0KmvZ26_U-JFXe0IojGMIsnaGpk8_M4g-SOHxXPzog78uhSA8KzrenlMS-wvf0NwAaknVo6pbiiN5nzKD3VDGtuYhV05LNVyz24K9ar9PagXygk7FyNAZCMz65gMgv0s6yNwEZess_unswvs6VSqmsv23aKnji96rHmlCmGss-X2slisS73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMQyx7PA-jBPQvZFi3GpzPsRZUeE2yT817Y65ilecfajIxOcqqEhZJxS7iiZfm5xshl-3HXG9boPpHW9Nl1ytXCgrZZ-_qW1pEozmfZff8nbLa9kvVuKdqmSFVqaS_J2f5MYLakmrM7l1Rar-w_JWX_xTCTg7j-u7P0jcaCmjJ2thf_Yn2R7HbA6Rk6Pmfi5BUHPHrvGXcKj-JrzVu4S1qGZs5b6GgtSZvI20O6niV0-Qj5WOawq8e3iKkJnArAB11rxuzHWvuEF4u72HSoY6m5LOztnhi49zKfZ_SB2vIMhmyi0sKTzNB09TQn1ig9nkLC5cDI97aZbbWRLmbpOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3TS7ZhautjT2ckPJwIiaQU2fsKPAfhod6KrA4CKqgNwVkwuiCi39UBREVRgKMxJ5fHPOsGypjqvtjLOdhYODbppXu2KQUR9T-oNVSl-OlcalTKoh7lMOueDVa0nVV45IPYlTI6hkUNr2Wg4ww7IhLhXyiGR386JDtjG83CbyzTiavImulp4gPno2vn_6YTk7YvyKqa7UkerG4jEsjNinX0r9XiEF0HC5p9Eh1BmXqRLXnoZZ_oVlgY5N8NHuPs_gZasAVY6vwnSRckL_2G8697oIIlrk1Nr58VOVcN9IqZwqnu-KI355ObxgwvzzuP3Cs2kJL-pdigVjktOYgc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWWYupexukNNBV-_I7mZoohWSz0Vl7sUyAQ190tOTdnuaLgNAF-uNpGkKsT6n_24lWbWdVTKBnVEePd7YkQHtszi6ysyPQTa_ce7KkILcxzeHAKgJczeSJX8B0P4oLys4oc772Tk7n-2KN5DNZBZcj5ax25f-37_5ExI0Qct8mYLDoEC3nBukSeHw0YrxEiUUa871cyvYjgrUTQ0fjRDjW1J_VmC9s59saWFJr_y60VAfp4isUBjh5LTacKcJkJLwW0DWd0WfBsghjD7rlx8DRAl2lqCyYLtzLlA-Igo37L8iRRbfVjsJhG6DEj-gO3wT_jwmg6w5kmWNItL6kopcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtnEIbR83MrbJpjsDoxH6kHY5mweSj7Hv3dPEi0V85QKnYS-6ZQExnRZD3kQAYaUEfsoLihvka9UFpSLUNNQrIquhVtI7isS4kU8xK4SpZIx5db0iur16bgSB5UOKNO340dmyjZwChgkVieTeF1vDJGnqygGWL1T3Hol1N-MMkjbWK0gkEMJTrX1YocReize_-62EcAvfDfWmp5i5D4d31eFyIQXQy8fgtO8C3mIxpHa6nBeXtyoratOxNjhSRA5hJWzF1yO0n1iP6RgiDbyJla552XjG3UVk8hq5u-nyl3wOETM4tkes7lJjgs2Jqd0rN1Un6RwCZDdxOueq2Mclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qViPoyhAKcyGDIGj8HrUC-WKhfRq6ZFY4OJ5voLu29LRw_kv8_k6bG4ucQoLC4q6pKFReMvqwek0KWXeNPF9STGF-1rtOpQ7ET7IgEm8MTnJwj2aPqvp-0DA-PRJwkS_2cFt90Utq7BvE1aEm_5vN-e6FgwRPmI-1UXZqmvc0o7MZiVM2EnNNLA44iVR1qo2VceoHbe2XRy8NXE-P0y0lsusAR_hmqpu5Rn5u0zndELr6ScbLF6OfhQ5SHA7aLRVtzI7Bhv8AZ93n8_yzCPbp0HQkmpWoszV6msQRr9RJy9bo8YMN7APvngZ1A7YZRJAkGhSLoaIs_VgujQWqaW43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub71iKPswRgLY_pqQAnpWF1mflkhQfAMMTwaxcRGo2Ng5c5OUfApefUoJ8Kj5ymojBSskX9ufMRSGhTNRs4zM2XGCCoaIxiuS26aC1BgDYt7d4SSMLHcNMT72J_sye3JPROBZ9_8gU_5MpPoiL-5gHu5foc_WDiE56gaBw_6xNDpHZobpluluHvCLHtMFuYIKG_Kg1zdMXMNTfWarTxP-h9dH8bjl-ePOVU3zv6Hzrml_nunFTbTLcjNBs1ZQwnT_aXUVzyAhGSpDh0gn9TcVkDw_SKlPZoiRada1EkVwLKkDdXaiSTpOeKNktQgr7XA3VJplk79uvllVWnKCI2AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntd67xHqISAR5W5dG0dF_bUYZBjbSpxtrsw6x2qduNwK2hgzj0Tqv4M7euBEHTRXQaV-rG6a99RjIHAQylbiani7fIGSqHgXI8ppN_EoaX4xmIrq_fluY9Sz-MH7B7_IewnkUP2FHIkB7URKePcMkkTiY54yvSOu8ZaKNlAID5kR0Vcsf_YPfWL-_-p85N46yjDW5NpdqMqCu-HFZyVc7t7w8XflhItvEe_XKUgobp6P5HewTvtZ7PyHZBR_OGk25ZmX7UjcUO7xXWa8qTY9Go4HoMMofecTWpGuzoPcReVwNiGCXzaFAL875fHALPY4KNCvoFiRMR2sgZ00Qgkmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTDN_x3QE3uP_JvF5TFkLLB_EDGieavdvxyAiiUNzkwZRYWXRHGjRpPOXXt_qLs8_IQ3zgky-brhVtANdzf-b8L7pPcB1oZGHxto3-QpDTlmIw5pSHrP69e7mVasqT1zi_ohujOJKubVXNvvNxvEgLgsYnb_MIzA8HEwxMZ-_prg4Ma2xxJR2Yhhn8-MEvXaISn1ljunE8Plg7RHv1rsLkzg6fK7ylENKqcLIyXx_HPAVzEq9pQcamPPv0suS1Qiwy53mjCkZbO_eNxPdxBOL6TMXcEH5v_W9rSYtfAt6trkCcNwI0Vtn8J4Ulyum160n7RhzKHS2JkpauHF5iwMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3q5es5ZJXPzY9caEIVD3wd1NdShJci-46wmrakSzImGF2hLeVYNM7CuohQdGg8ZRr013ukL6yDFJvkFgrQOVoLRz6wp-ba5lGo5xpbIjJ6FeukO7GOCLw5sQcCYwiyxby2SY-y8biayJMUypirmSbzWUdFGoFhPvxbCvz80fsKa2icAh9wgQSDz5yARiefEXL_p2OEq2o6dHP6x3Ebrx5CxMCLO4nev4HIxI4q_ypw5OpGPpkPJJdqT9S3TAO0mnzC79yWxn7N--17Y_rZYc12V2wQSjhXMat_Fzn5iPYxQM7OlJw_OkJXfEVYFk5ecEuoeeHXwzl2U9-nwetPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/retUssdp_gfhy1ihfY55xqHPDRHRLzKuragYTz6un0tFHl38XQYOQq30ZqpDPzrqw19b79sv67Q9VgUn92AopM_3qfoRAzJDgMgGzeRUxtfk7bqhUPwVLHWmPMOqyZxmQFnGBNVHV27DdjbOCZwVyJ9F4FJUTyvL9rth2xNl2tk_cZ_mXxyP85fCPHPPlcvds4zX796obyFqZPaeosf8U5DPJGw-62eKV5thTGHRLb-XRmdD8RSGluQE3inAbi4BJ_oNHqIM-l2rEslYLyQfU5xHJ3a76GfaoAGLjKApcX4CuB8mOzqjujyJoU05wovyWRaFqkz_3MJ5h1ZKkbzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d39tCvmdr27z7WLjfXiQOkJGi8rrSlvAu-JmpU_in267MKkDSvnH9stfeOJN3g0ekJJrA5FSBzoOnZuP88U8Z5VG70IkUIvA-MCVxa0R7PTW630ta57ldh1g1mJRS7NkCyamAQP5VddPerTDPq375TVhZA94-cbYso1DqGQMRm2NVV8V8XPoLM5K-oJWWE8YpM4uT4eu_DGSgzNQdt72QIDVDIXr32nmTSGx-YudUDAWvhTakMko9tRnCx5enbmwcsBOXwpxJc8kIMME_AGckdsgKq5OVJJcs3scUiMjQyuZte4Nkecr69vWV68WrYvzMTlTwjYjB0hH3shCqzEnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTRdXCs3BXfRJb1LPdWxP0KEliF41D-w_dOG95CjOIIymS-NgEpoOesPNa7PgN5PZaZgQ92pPv_VVRb5X_BXI7BK-KjPVQQsoFkkBFCHh-MJmS1GxUcdcQ6vPmr0-i5BvwAbCg1Aivn9sFVOJ83sf_nj2nLrQ6vrFI0v1IxD_oRqzKeSOC9Qr9c84PB4V5HF99wiPlJxYcG7QI3ewYJcUM7rRpHztU1CJN4HjAVyk46-xflrmxDVDFUxuHiFHEGY7bKYjsBiWZC5tnQ-LnIZ39jcEg4-0azeBZw3rMreWWA0uk1iVu3qpiMsfXXOJddrZwsBdgm_fK6yaXuLRVvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJvdcyCSPugtiPgFv6dr4N-G3hcs7QcHiyeoYlY5edVAcfvCI41c-G5jDLnaemM7fMJVHZ5iBBYl3iZV643wZ0i2O-4Epa3Vmb1d6HB69S5_l99O0810ZuyvSU2MXuI3DSC97dDFLL8oKxZp8mGgu9BED8iO-y3ZznuDau8sSypIdTdq-fRAclbzf1WNV55uueEwiJZmLnllJwPAXtGdO2enwwo0CYfm1ER6p3iF-pnrI26UGN_8JfeaTM0E94KrSPSjVQLR92eLPiVr2tnNKQ0YW2jYv1TnCbTEN-m8b9FgjXcHKV0wcDA-nwsH7SLrAPNc-oi6XAL3VAAwZYvA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgc-Z9q_aOBXjeeBHJzmOKKhsLkP0WEB1VeDH7C_pWmOXZQwfjm-r9BPAcq6so5MrW7Aycbu_9pGvcNs82CfNFacUEIm2f9pQkopzTYydY_h7vFev9gyRdhyPtk070JCgdhX1z57vwvuMVluTE3tRno_mpKlkQX8ctn6PUYH2tja1zxgDj3ahbQy3EUsQ2ZYkoIR5nxCY3V85DyggXzJXAGIPofxTEzIgskfSUAsJwYjvyAMIolR4-GwmSV8LuYsM2WQwNePsPgxu_4LZPaDTtpwXOyvswB1GUthSKVmjbCMtchUDh7lkSh8Y05VaWmPBwoEdm5sOHZM98DuVFRBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=CFDuM2UXOcYu5vY7F6WcWcXF8UQ-Dcps_sdlO-7zjVxeMSmgm7xEGx2CgBfkbxhB3Pakak3i579Qrqv2OVvetQa8Wz84ebssRV9Gk3KC-7UAeMxrn8eBfTYcpySvfzTMVj0IytY5CUtTB3K35jea1uTTPEFnIFpCJscSm7tW3oBz0No-ArgX891fcPcSJ8RY2U3zHRwez6JgZ7N8dBAozVolkI9dHLe0-S-eNkFv7anqXEDTdWQ4rZwkUTAEBjd-u3n_TxSV7HXu8AA7j2yLBc01WINWuVMt6FrmMAAhBdBE85RHJmitt08ONAhruyNF-zsHBtpAwiA-f8R65wLUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=CFDuM2UXOcYu5vY7F6WcWcXF8UQ-Dcps_sdlO-7zjVxeMSmgm7xEGx2CgBfkbxhB3Pakak3i579Qrqv2OVvetQa8Wz84ebssRV9Gk3KC-7UAeMxrn8eBfTYcpySvfzTMVj0IytY5CUtTB3K35jea1uTTPEFnIFpCJscSm7tW3oBz0No-ArgX891fcPcSJ8RY2U3zHRwez6JgZ7N8dBAozVolkI9dHLe0-S-eNkFv7anqXEDTdWQ4rZwkUTAEBjd-u3n_TxSV7HXu8AA7j2yLBc01WINWuVMt6FrmMAAhBdBE85RHJmitt08ONAhruyNF-zsHBtpAwiA-f8R65wLUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=Q1PTtbptHidlox-km9x-xL_4YUlRnlzCyu99Ma65GE4Ol0I9GpMhQnuC3rhuK1qn8K1iUTMNOO3xQ_2pd9J7rXD5BB5-Qj75eQcz9F0Bc9x6MtceQ3NqIOH1uPCfs3GfccgARFF97g_mR5L-lsET6HHVTYpB2LtFnOmMvVOEGZ2JasVmi_VMh2EARMokf50H9Oc1W1cx_oHxfQ2CNvgyD7f3jFS-gal7YRw4_KPl0htO0t_aCYT2zDuPnroxBKlu0oLpZZA7Ic6byiEthb1p74nvswLmXww8yXeEP_2yTP0TD1umJceCvlrv5UjFFDXT_xaAai9NFGVwgEDU4aQjzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=Q1PTtbptHidlox-km9x-xL_4YUlRnlzCyu99Ma65GE4Ol0I9GpMhQnuC3rhuK1qn8K1iUTMNOO3xQ_2pd9J7rXD5BB5-Qj75eQcz9F0Bc9x6MtceQ3NqIOH1uPCfs3GfccgARFF97g_mR5L-lsET6HHVTYpB2LtFnOmMvVOEGZ2JasVmi_VMh2EARMokf50H9Oc1W1cx_oHxfQ2CNvgyD7f3jFS-gal7YRw4_KPl0htO0t_aCYT2zDuPnroxBKlu0oLpZZA7Ic6byiEthb1p74nvswLmXww8yXeEP_2yTP0TD1umJceCvlrv5UjFFDXT_xaAai9NFGVwgEDU4aQjzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5g98mx4PuWLNTj0kDL2rcSCqItdxbvibUC6AABKmaxZW07pDp7R9BaxeM-eLgqb3RcYJSwTSQ7HyecgV0imtC2u-kP9eqzyGRSxPsnMfqnYuI1YCkgkSFglcehQdAfRv_ZtsX4nAyjYLDAgcxxAHJNzODYvn2Kx20slG2WpBR30F7azXna23_yIWYuSKqEPwa4mieWDywW0JL63MeAAB9W9vvLMLdo8B9_WToHXNTjbO_QoOr2TOLEBViLM5F95vmy_jrwYfQGiDCzYwFTHdxPDIYHAVBShKXKQ-sphqanrlxP9oWcCkxB27ml6QFd66glkgiJXjV9hbFiZuJi4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr81vYVr8HBHWsrlSqjuxBx4SthQwRaSWUHDdKIBAg2BsXJUUI3k5Rm7SdX1m_naxUbA1lVRCN8V7dsdQQv1PtphqrauiSzxz3bGDKTQ-KOLbvY958Xz80YPmLYY2TT1EhetzsjMRn2abRTjNmClTxdckJzo7bC-GHE2_9O-XJl3mVReWI9pyaRhrTaLGfGdHGxfiu1U6ABYxJjiG98Qb4kfj7Lwazl-RIdtB4-gjs_JiWxoTOC1plJXpwv6gnJBLpjoB4YsXiGcTTw01f0JRHirneQVwktR4f8haYYs1fx6VSNPAKyR-72HEs7tZMF0X-r2ncaKIjXLv42pEcrZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbzGeDU4xbkKyGGd0LWYCzUHcWWXPYHNDompvLLM0SHtqEZoErDu9f_qauaymOxBHH33M_lYD7s6iaxVkryNk0l8TEFxxOPkqeshnGd54hoPaczNK6KVarRe_tWqsZnZKJvPbr3R4lOnJigqQaNXiJP7YDwiGrdqHvpwv6FD7AUVB7TfYAovjOAciajprbrgi7BfH2En11Pi_gj1N4qTtkjBXU0xaDptO735JsK9I-joZ3lJJ1UmrB7Tp1YFlowdkZTCY_lbxZLfaaKuVHbcJAA70mC1kxtONIGU4KKY0xOR8k9xNxwtJkARsFDGoZAAx8hzMHv1pbRXxNhOF6J1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO-poCxE1IiU1Czf0nYAqzGwH7zDheHmvshcIc0jYu_XC4tpj2zC7GkrFwXxlVJcGSgANsGqZLF25-z1k_Mds7E7iurK1ucMn34_q8yqlFLzLvliymqCcYfuhUEfWbFmd4JwgL-1z9ZVYjbjuUXPsuDDP52-steKXrSyyUI-frO2_x3IoLwwdzSakLssLHZBei4q5ab-jPS-7PJ5R0PHirTxFzn1YUCgTSZyoftznRR_45nN_CpMbeK4ZpNxjmyT5x3Nj5sYdWXEGSeC5MwoLkIXla5qhoc-yDwc8KK2IXm7_e5OD2E89hZ5Ilhe12PZZ3AqT507O0Br9Ioc39Iyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=gJyEAc_iEePhDFbhpFyPMBCqucZ5WIoB-O-MrP76dOWNiGtTtKknFyKj5vwsh05OjFoBKw8PSsNDzbSgTgTBxe2TCDgArKZps0RR6Xnm603XMz8mzpbvzhUOEcnsY_wphOcI9HaJYr5iwFSSmWbfPK3FmFABugcjDOD4q6gKgqHElgqKB-txbKX6aFLD-di-1ufQiaFo8gWC7X6Z70nhWoKs-059RRWXnVdnVWy56vkObzu3ZfDMZahSv96cIgoel61uAbRLoHHUGdyCejiOgpDdwhWZIINomF6UahrtyjvBGeto3BO8rnD9RHa5BRFDjog-a7GpIougAa2ioJ1O4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=gJyEAc_iEePhDFbhpFyPMBCqucZ5WIoB-O-MrP76dOWNiGtTtKknFyKj5vwsh05OjFoBKw8PSsNDzbSgTgTBxe2TCDgArKZps0RR6Xnm603XMz8mzpbvzhUOEcnsY_wphOcI9HaJYr5iwFSSmWbfPK3FmFABugcjDOD4q6gKgqHElgqKB-txbKX6aFLD-di-1ufQiaFo8gWC7X6Z70nhWoKs-059RRWXnVdnVWy56vkObzu3ZfDMZahSv96cIgoel61uAbRLoHHUGdyCejiOgpDdwhWZIINomF6UahrtyjvBGeto3BO8rnD9RHa5BRFDjog-a7GpIougAa2ioJ1O4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_kkaP-3PuWZ2GVaeUFEeiJotVtHctc8qM2RFITdMrOeCyLNagma-9nDjZY5H2bSKIF-rTN7gWdQrsvizCAH5f3Fp7-DYydWHLXP8ZJTH5bq_vCsBdqViGSKE7wpav8q_MjmNF_IZKr8ppFJNfHWpC0QRciF7YJjEkpXSLtRQdjYx2JJ8wVrM0yI5vBj50YMSoY16sdtqWeNn3pI77iEqSApyA7RNdNG5ZdxiBLBUDSCEkls-G1C57AhKOGkNraaI2Zfd_8FGPg_gzhCFQ6nSGX02skavjTGmqoCrBRbUPrzwX9r5z2Mugm81mXoY3Y6vCfrglP8P1-Fi773eanVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgcRNOBmIODJ3d843dl8A5AfzeKz23mJTJP5tmAjKnfs4PFOijeBlLIuc-FCapguFpYDIXpA3jtYta41uE9KP0YTsWxi17aaRsoEnMoAV1_qNdTKySpo0w8HePI6VND2F4Mih_xavJ5b_w0VHxhjaUOG2Z6dHxNEkNvBzELWFeU4AtQFzS_WcvChaSwGCSbzFWesCYCsNxT2vgDwWb4jmdUBQ3rAg0YPCMmLzNc8X0nAHuWCzKxNu5D2vsfz3dfjBo6Di1bPcbh7JdPT5uj8u5pPT0efrGf-odpQl655YMYZl4c1viqsj3DaqK9pXIosWHe5p5R2vXVWnsbw_7ekfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vig97366SK_V8HpWXnfZellvoGbSWp8Pd5Vu9fvPKowMK6SLIovU206Xg6MWN_hArn1E2QPcD_f_OOrlvhj9z6nKUcJGW57tRH9JdOZsuLecaOBj7U-zJyi28gjRk0-QXLkRaUB-y8TVadQ6HXDqNuvs4oq5szkFEvtby5lo37pkoejCzoM1SQabJYjFWD71QaZEmkMUPraw1OusepI-Liqt-guwEFzv1zydah3ISdgUphglzdSsnht7W0Id93eqp8eq6bS6O-jC4fg2uFjYJN7dQjuxegT6DQm0Cr76uI6LDIVTFFQ9WZDBel5H25WmgkTyFHFHvAUOM7I2WyMwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm1GacFStH5dufUFeajLH-ZKa-XxHJvJY3ZVQItOjkPZAXhuiGou3uFQjh_4qmJh8DlpnMpMTX-5oEXaZOEqMLfxUB2L77BjbsCqBSJ3QVCUiRJlWBB5FZl_i6pwasuC26f9htzRoKydZiabPmFcM1UO-uN1o5WEbOwh_oQyogOBuNAEuwhqCTZ4qUmRZeQ79SfrhMyvV73owR6Cm1nvmEo8rVYatPFF0ia_Ebg9O5iTjgwDsk56zsE0apZIyLeV7C7xATkqHEvEH0uf1o_gDTOzOAGkP2Sybs6RbfYgmfY2POTIB_Fjny3mCqTpl6-2KHKEG0Kt0vkP7yi8RQXqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogsx6xDHJLG0166cacwCaFv7TVHwhx8wYiSKUqtZjyu-9hRPguA2uRcuthvMAHvAWTYz3ZljQkDN99r6mjWf7ZjZ8PzkguuY5NigggIQpEZxPs84kFAs9fdxv_ac1oABj2rtx9YANKGFSSxW3eh4ifeJLXNLTmDZOucnVtHO1NHTLMQdgjl1rFYB_eXjoBfgmCL3qtfSzHrUPWY8Kal2RwsNgdz1qLz2QwxY7GrD_EHLugsngtfN88dKHXhJPy6w4cZHrWO7bLo_rTDSO6-Z8AxQnmrG4kCQZuKBdd8bLBSGVXRWXfHRM4qeKKetdIaWTCjZxLwXSAr6mQcA01TFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgYDlwz4_I4NVoC2ShI7W6K8UXkHksVu7cGf5MduPwEVD-riClx-gu_KBJKr7QEB-4eF3Gd1odp7_U_KED2DpFB7qHg1mquSnKpRfEW6yCeZkrzH9aG_2xYHknkqVoaEIerGzhrNvFvCbQ9SC40yVUWD6DgxHpNVWbnMQ9Ymwwtf8_nWp1G9tYqChvQQX2GmU0wS2nFbS3eGJcdV7Cs2T_JMU17lYdVzaMxKmXfZIrppnkhsN9KP_pxOY5BAc0Rv7TKOnVtisZ3owyn1kTzF7NMwvVBPXEMJETfaiI_0wKQFNE-04AsTMtxt3030S9YR4Ez8FVMsDybZk39RnvNf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQF5lTbUE-DE_NO1ZRVMfGGodhYo8VrAyeWVUkOU0VXKKrnjA5oX8CWKk1x9MBb5-y0hV54SNwxIEzSWv9s8TXZsAMC2nocenkrw8dCiPXRmRo6NPYGbg1n3h0C6NweDfKffR9SfnNuFPG5eE0aAYTnwVq29C-LcneEXRdOwNHMK3WClLTuM0l2TDEiJZhe5t2kWMKdzUbuICivsY-_J9CO-XByrUOzqGsYHBtpcP0oj_hRYJ1OIpCtdK7_wOoJa7hfI2icKSYeEKTFNp8dhGM1aM4iD-s7Dq9jI56N8aLIT5NJ1E7ULYSQ2JEvlnxDWx1JGYEDfSumg99sa6mFaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glR7N4WPkdApg2yrhn9qATbaCddwdrTYkyPtlP-7vGComiE9AGICcUTY50LdW7LYQQv5VXtcrGOchDbHmHTXfKfIBsFEcAXksSAqHpUVrfBW-SNX-UErcHp_XOpcm64UBbl2kJ1bCeyUAOriury-P-frjAsA9848UK16bGtfg7gfA1VeMEMAwBFDRA_5cCGSZrgRYf3RM6fVfQR39Tx0pI88sI0_74EP9HKqqYDNmoG7Ueq6ZoLzrEOLYPNrrq3SDRePnmuEXb3v_MhlrdN8FrF01ZQTH-gdwHM81826Plqi9_1581SOYkFHsXdUBBmc1teFJOGsex6gLqPAFGqr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGLTzGJzWmM5IeSQYd004_XFSJDBne0YR0S6zz9COUUw86mGrZQegsn_BWqfI5xqst21RRG4z-jpNmk3Tuj2z8QN-5YQezvlFBc1_rPNjVPcalkbdCMS8XBPGwE3h2_zTHicU3WDp4vRGMRmIrh5D6KFXAglAyln7AEPX25OolOpF4lyduwUT5L1Y2fpVVU36K5chEIERAl_c9NDZF-NM2KvvI55X09DKwZuUlmJ-XTCIZmc5QdxuMyskKy3eCka0vERjGFnXYsIRAzWeAxQ_u2LHa0AlvdlBtcK92o4rJaQMOKx78oDG2BWGL_P6ogPluzI-VPu9Ix5Af3ZL59Sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFgaRnDYoOhSLd8CkLU9KEi6hNEvn0GJM5A2OctJDgtw5sVYsweOzpLpFCFs380E5C2HYZgnpp9AfERxqjJxyXySi7KUg_PselXksR-ERReag1tTKFuqSA_Tc2n-UBqfao2sCxjqOkT6MtL_W0yI2vEpkZds4Jc5E9KjotxG8QDiMon6tM2kJEmF5lKy46Px0satNK6C2Vizm1eaYNJSHMTD9Wg8XODHCQfDMiYvvfT3X83KOtEXlb61NAX9e2l40YsG-gMs1nqsbyRSPCFssLml144EeWSFg0GFtTNDw6Vp6BjnrHaS_Razlzh6w3fyey2bbcx7uEzV2YWwTAHMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNEkKWgYtkLVDRDdWecrg2vsmgtC2GsHjXVN3R8Ol5xVOzhPYyOlb7oBn3MB4tSTKIwo5njrsxBh266yQSx-ZF-VT17xMEwam8qdkZIHiQLyLKYmAZ_umoSGkUfgEZjqgGEAHC6dA_mQB_7BJlEtZ4Q90qX3a_p5j30GHw8Qs7t7HPFpnEG9FCoxcl1BI4p0orzyh3BdPHiHO1zxTQ8qKXrcGst82J1tZlnkzaQ-DYfmaXBtkJ_743t74-ySrsJJ51tkVwXcJasuRPpVteQd4TCR95xU97VBiCtT17BjGxlFDLpQUQmubmYRdFwECAoT_SpYzRwivSyVsPk5KN3BDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcSCbgwyb203u3qpkSW3ATbKmOHOHii3xsqqYSrVgjO2Nq1oaeGqpizJGHrqTfbMzfu-JkD9t5v7oevSsS3ML8lRvZU917OfFoCzfVLM0IanlPb65ww-9myIFLADjUMbNJF3Cpcsj2i0QHBVzeL0wQkzWyRJdE8UCSU5i3OV8NBcCizVVGUIdU3xK0cznbAKOlKlrE3eub8gUJ3ObfQsIDNzaKQ9nT9qtrR5wVpee6kUQl3JNplxwv2SvZbJhhK19pwiyJMajAYfZSn1siOqPfD_Cs--r4VD50E0ypbyfPI2FTn-4MD_uMtqoxWbWlvDPg0R8wyCV6VmTWBZForLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=ICVeshF2t0BXadmZ4_1AZWCGteWcBbzJTGSXH10vuYimlk8uHft_eayV54xVlAK_M5aXXUd3WMRvpKWxWRV2tbD-rwKMAp1ssUZXXoyGCEfstVZjX-DohJqdyFaCKa0WWDa-BUxFmYfgIVdMQd31BGs6Zwllbsv6F-3IwKz3EJ57D0d5E_5wFXNobJZeblrlAgswafjk32WJwZy9ZD6yVKsPhbN6TGtzUkTlS-0d0wb7bNCIh8dlMhzYjYKyMliffcR1Sq6m7BYId2gdXZSrW8uETQia9Rn--8MWeXaJR9QWx04-mrfVKaslXKUrJdIxPJd3IL1IjYRbSLjDczLCMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=ICVeshF2t0BXadmZ4_1AZWCGteWcBbzJTGSXH10vuYimlk8uHft_eayV54xVlAK_M5aXXUd3WMRvpKWxWRV2tbD-rwKMAp1ssUZXXoyGCEfstVZjX-DohJqdyFaCKa0WWDa-BUxFmYfgIVdMQd31BGs6Zwllbsv6F-3IwKz3EJ57D0d5E_5wFXNobJZeblrlAgswafjk32WJwZy9ZD6yVKsPhbN6TGtzUkTlS-0d0wb7bNCIh8dlMhzYjYKyMliffcR1Sq6m7BYId2gdXZSrW8uETQia9Rn--8MWeXaJR9QWx04-mrfVKaslXKUrJdIxPJd3IL1IjYRbSLjDczLCMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJj5SeHdNR_A-q3WeMXp8kHP_lbXMnycYKPhKgUyahsWCnBNg86B5B6u-czPkOTozfb5vsTCCJFTlxws7QuQ-qiLmI46TleXG_g8HTZoI5dYIfBzIwoU9HNKjbsxlCTlpAarEfg-yK3Ttl9VFBVKGKMetUdKD_qxd_fdTQW8QLYqouwbkA__HuV5_KLReJW5sVz9ADlQQimvX7Oq8zqS3fGaUFMIqPCEP1F_H8jc6UoIxmO47F9R_4_14l3VNwCTSr3BALmBs1jbtdeFIau2TgfkYrNc9L5RLG_VZro4BqzCCCmC8XLpRRadlSusmA0v6vAiRGa1-v7MBl-puZpTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm1HzQYcm1hIDNBiw-T3DWxhIdbCgPRGzEQDmsZu25baaMdc4nltYciwYMqrKIGTHsBWBhvBdnwxxKnel1vIICkebEQPfca9n85h4Gha_fyAs0niWhU1KlOUbfPMFm47j5n3vfujXaE0nvN6EJEsdDZb_HFaxHUkpLkOCHUptUBzvmJkMKtOwfz3gbHX39Qh0TUb98YVUEXDun0h6b8MTR86iWPd1Mo_ZgOu4eADLVRupSkDZ6UEf1hHoRJrwEabNX_UndwUTNmWy8jWXnfHAWiz4Y5EWVy9siXVMsj-EOwOn8fdIoLuq6Xqr0C_IrX26okCUuXbR2Jlq6B_FTxFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcOj27tXIoxTP9iDdwRPnLrmHFH_HIC2US1QWqxni2S0c7kKYlBdaRRvSPfeAbxi8xiqP14QGwM_WK_yyOPn7hZSsl3mwfqLLeG-anGNKKocjozMh-Tnu2vnOxmrMMeeeMSLlJ32FjS5Q72aKYpOqpHikkoYCYuKGZZh7sSEjOqhjVOuWV9z3WhDP1ff-bf8ALogNLxsuRTG9ntUJcCoHk7q3py_BtE_qMPrxm64yK-cjfFU3Ea0EA_m677WOVvt6RWQi4iStOgdNZaRaRUewEVEA3zFgvGOfgIBqrwQzKCdj7pVImVEzTUya1GIOHpWzfxXEgrvms7LPJvaL_Ea7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgC3XPWHanICQqEXz1dFohLkODGAlg5Jc7I12PTF2CxtfFnSlHfspL9zvfPkEY5kTDrM1hMR72gXpsU_E7F3HZhF0w5jp-vDtJ3nF-VLpZ9fsSlGk7PRm7OTtd87t9_vBPr_oD3aTWuRE03tXO8_TJCphG5y2wxAskN1k4aDcD6AlQKLXp-ybBzjvGHv417Kj7zgXw8oVp8Vy7xI20OSZUOI9v6gA_unbnN1UarQsBDFvevlW_RCHndxr5MzYLm4HhAKE_k9S1wezfEBHOZOByiVO0NTxeF2fgUQ5WsgoRCViI3tHhI8jjT1ZpqkKf1fQTYxoQg20b2leup_AiJxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=jJMblcnFrJf7cfZCYzy7e8Rva3H3DTeXbsGpAuTiWHhHS6xNtn0ZijlbEYht1moD2j9VqlaCzJuctG7WE8qtrWI-1KgmoAuCAn8Eap9QFtoRvGUPxmd7zrfpZrF73gvj2I2IA_xeXilPna3OxoMnitdWZMEUaqq8b_Mf9-AMqbqeil74PP7My_vfmGpSGG3k6obrF5E_ZlWheiPPjEPOp2vQ0s2a3hcearP3fXajQ1k8_vbHKli88r7aS7JfmwiQyfpqLiCRbB8U3NH9tcDaWsJFehnfJNDtdjgmu5cJdwG_LGYYGH63KmnUc6Savw4KpZ6yHof5sYT8JGGF7Pbi-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=jJMblcnFrJf7cfZCYzy7e8Rva3H3DTeXbsGpAuTiWHhHS6xNtn0ZijlbEYht1moD2j9VqlaCzJuctG7WE8qtrWI-1KgmoAuCAn8Eap9QFtoRvGUPxmd7zrfpZrF73gvj2I2IA_xeXilPna3OxoMnitdWZMEUaqq8b_Mf9-AMqbqeil74PP7My_vfmGpSGG3k6obrF5E_ZlWheiPPjEPOp2vQ0s2a3hcearP3fXajQ1k8_vbHKli88r7aS7JfmwiQyfpqLiCRbB8U3NH9tcDaWsJFehnfJNDtdjgmu5cJdwG_LGYYGH63KmnUc6Savw4KpZ6yHof5sYT8JGGF7Pbi-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTXqL2Ockk9OC3J_UA5xGn5-qfHmJMFX-ZCIb0LBtATv-7eeHusR-TzOLwnEcCr2NwwolrVD6ShaiHGYe9Y_q6UVX-h2cF3snvw1-byxvR2BnbZwJ3ObMpl0zBNXOB7YE2CzZ4tICxcDSs-LFg6DN3Q89VCkkMLa6OrIBVM4XkyrNxUY632voBTQ2-ABlm4r1nFkDn6V9Hgkf6lhzgPpud5Og7UxcGe82vmxJNfb2fNqGyOsoWMPfTHlyIqAr7xIhao5W7UT0eW0H1Jj5LAPErpyeQvHnGExPQxmlQg3nPGw9xwpUJazqLK04R2MS7Epl6EEd3aJpC2GscVeHwVO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LznaxQlG1r66F2Ry7hLOMA2MXgM4OAcHhkz2v3VAX0BlB6n4tLMcHLKld-x5BHUly5NFufeQhzDjY78FZF5jnqoBPcokZwShrOgJgB0pZG8aESq_XdrN3OXFT8PB5SOLBQROgxTbkM36ETPKx0TxmpBjW79gvouu1si7Yr3ULq9sT_2Km_yrp7UI0T_ns18qzo4AjaoRRvi2dbKKqSAhcD9s1sBtnYiQthbcTGStTdG6f934xPdRNm7geDt1lz3WlAdRtuJhDHQHIMYJMx1hS3KrAWPfZMjW_5KxtLUcKRCpq_byhe4qtOdg0RZoLGl3mwAWCAPTaWYU0cFJvALKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4Mn1y9qUF7iQBQN_dzkP6-SdF9ixXehFQfV31jU65cbCPKWhCBC2ogv0_Kf36XijBx4JfZjzSV8mE6atfusFrcZ2mbYHIFP5V0DqEBpCBMoSN3EKRltn8GHGdpSCgRvz_mcuAdRx_sEqI3StLiR9e8HNWYpV9etvBcgJ6wJpKNUQAvdJtl4a4sCBqKASstEthrGMRhlML39PFmJ7h2ng8eolRJegm1l7MyDN7JLpPuNmMGzMUiLn1btktYPS_4mziqBE8Um3mhdoZgnUsQCS6aO-_j437KlTPR05Swn7tGo2BOPpSYiiH1N7UjaOuK6nOmRcq3hsnOdF2tqurMFKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVOqxjz10gKtdDCV0lyiU1pjPEZ5jnr3oaSA9v767VEVrYOkPttttiSqzoV0aa-ywkRa9OZccy4oHpyuYHaGvZuPYhohbsAuRGQWshQiG6nIbfVWJJfEkSg9ttyMPS73bmOMXCqXDXgaeaHV78fhEFJgUIgDlHSu4M8529wWoJcJrjBrsrKijd8CybfIFjZIf6UMwc_jw-ih8CQX1xrfuA63_vlXrEznPk542brp2eavl6gHh_65SE96wnBun7qm2RcjPBnf_XF8N_D6uqPylWRknNSMADj2NAwD8K-bDNtLun43YngUSzv0CIAL1_Xjz2EsibGYS2Rh7LEGFc83fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRjYTaqHe-jq6ksSreNq8cd-A1tBHaSfdD0sN65ls6VZ4IZQuLLgHfmkVWX1StidO5leYAywhf045zzaQb2AS_l2o6mPpQyMjgacpk9wy-eCnib-CIVC-Sp4SfTbNuqqgq3EZQAOb7CVaYvq_AO6ilTQrT315SP4yji7FVG_g6mQXoqn4mkLr6Mn8TwVvXBSxglPkKomvGfHrjy-ODEqOfaaFBh0HTUYpyKjF7MJeAdKzKhnXvUTvUzXzLAxcJFdkq_ebRZzu967K7ah4__NAUA0CkjDk58PWIUXCwpNgiZe2kt8NK2vyaft_nDSbhiKB9aNOUwjyCNcEQXiPpyaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJVIf7upCxCI3NRO-56wgu1vToaDcOclxSlTo35wLUY_bUqWsr53l1_dVXQiZtgR_wG36I4r9cheskkTGjZt2Nb72jrkvRPKeUIY-TKlqOTMMnPQlMbX-rCmn1xgH4GpRIhIBDOUE1MtcKnatqzu8qIgiBWmytfBEupXuJwub_DHubcMOXwRbhOAPcG8LcYA8N8VJ6Y5KnlraZoDZ1ou5IO0LcQBeya4QsdTARWvzaCIcFC-Y_k-lnzTntm23AOD6wWo9lOhby_37Mbc2VO-DrAQwUIwmYC04G6QwdIEMPOmlbmudr8BJZFOR1OKYjUJlX5W_jCSd7zXaU0W4JNgsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0Xpy9XFoPZ0msZ2dYLuquGsQovwRNq2MpSlXgyHMhL5ZgjGAAbngJwoYlNwugFRv3kOSTWmfsFnMxu0VRsN7WD8DWnFiJe-L39DGU8SKj_-ogeEJvS8PkP--GJQVdQ4O9Hs7nZsAZEt2pSpJNOCmirmlS9GWVUy2dQw8VDA7MI9bXmBnNoXvwS4kH9gwpxgxJX1LmqwhfBD3T2geoW_iJLIsJle76iCrWRE-FgFN_QC2egsX9nLZfzqVYuF5zIFVqRGcKU2_Yh3tbCn3EZs1z3Yq6n2hUhqKhbyfHcnxYpiLzpILPQLGZC1-fOvOmP5rywi3ooTu847sQBLCO34OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=mJvxcqbRrPMN6DTv5xvrsXpAluQ-lSxkO_xK1TOrvVQ0iZ7I4bvWcmEvQOVZQnH9DdyfrPEDKOF4dn47YtgQC5ATbddEgQH1ZkxFRr9xd38RAbrRcltvSF8bJVQaTkoks_YFxNWFA95r5AgN9dDUhp5HkwC80C2FNIxConYnBac_MbACkXG7KnDzl78anQK1BqKnVclO3JiR-nwVuF6PVf6wSKRrpp3TWnoDI-6MsO9Zf8FUq5LaCtP1z83M08RXNHIYUEFpe-BStDT7L1r5kqn9PL83k44sjRnNXft6Ic408hK9j9nmgY7yPWit2cAwpjDmF5DUvK2KSb-AHXb9oIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=mJvxcqbRrPMN6DTv5xvrsXpAluQ-lSxkO_xK1TOrvVQ0iZ7I4bvWcmEvQOVZQnH9DdyfrPEDKOF4dn47YtgQC5ATbddEgQH1ZkxFRr9xd38RAbrRcltvSF8bJVQaTkoks_YFxNWFA95r5AgN9dDUhp5HkwC80C2FNIxConYnBac_MbACkXG7KnDzl78anQK1BqKnVclO3JiR-nwVuF6PVf6wSKRrpp3TWnoDI-6MsO9Zf8FUq5LaCtP1z83M08RXNHIYUEFpe-BStDT7L1r5kqn9PL83k44sjRnNXft6Ic408hK9j9nmgY7yPWit2cAwpjDmF5DUvK2KSb-AHXb9oIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW5A6ngk67aDD2-zxBCARc1CH0cRHKCzOvnXlBTIFLrkyGGQJJXggEdDKeevSENrxZhulROlM9pxsgjlicQYod20uZQj7it5PlYudS-YY3ZSzd6x0k2DsfQRQ0GX_NUWWTrW-4ru-ThZX8RrSUlxjEr_XXlUSwZSW_LzCNKV8TQNy1nH3Mmu5GewQ4C84u1fkXYgfHE1Kh0vIBgskVydhQV9rE8eUBrQ4ZITmI2QMXSnJnBt5MRgb_KlSkzKKYEN6QeqC7k-aFGyvPz1uy5JMspKY0OaFhs5S7Ddxz7BEc6_TyaZb-MxYz3-EN3KRGgOxB-02qLlW9coQDDcHy5VNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJGKzv25zM6zmuyaONHHSsmB-4H2QkvIZBHYa7UXoSvxEUxsDdo97neUSWA4vLKit_Qw5nPm5ylpgEhO2YfhTLj4y0s5aN4GVNcjMSa8ZR2XzAeQ2evBzT3ekv1esvBpLN8iwTBX-_y4HB6DFtS5lwx4lsU3s2ZYBf26WzDY7nmTwMq-t2nHNjbH5ohkxKz-95gRx7qOB2rUyLVBMfkWk6EJVZcBRsn_Mc1D170IdFxP9sp-Bz9YVnHQLDvUAT2eEg_hY6PP6mp94xGPEK-WslV7tzwP6TjZ0s8DKlRqn4xSOJFBXLEKAYadVRY5zev2uH21OcQ1fsxZfI_teiqwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pedBOSDoiiRlbFsUWvKWvq_5Z3hWoZbGm5Y3ZErIZr1tp9fVMQ4gmdDF0mMOt3qC8Fg-moWMbQyMiO2w3McCfaVyWGZmM17KOtQrYDjLlyxrPFJdP0XEj2_cBqE80back0CwlsnI0JuB4fijfTL1IlFM8_PyqFYcLCE6Sv8I4NKpShfZRq2VVohL6nTFHn6CC91f07UkCLSw5Zw-zKTI264Qd9vUKM-p90YQQnfzPcPk9HC1rnPy8v13gwKFsWCBmz6KS63nDvodMz_4Oot7ag004FS6Gsev7JSZ7hRqz0JQig631GBZK2y-CS1eDc2390HMomdHkCDShNBOouJ5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQXRCF4Pz_l5gNQ6ZjPCLLTwh-KFqUvVjnMEVDj1tc3FVBU4qMkQHbrORqc9JDtX_9dqtlhMqoMb3uFw7hALOcSL2E7fVzEO_GvErnoRJQ4oPa86giwNKBPjGfkDRAf7vVVOMwEEXHnCpHP3fSvnJ9my1-BtOQ_-1BLspstUh8cXZ2tQXqrD0qTMfWc0DNZCTs3ISTIwTkYYwVmcu-YdiwajWQEHA6pvEtOa0gBpy7hHZUJzPZkFTFrd2swI1tTuEZRNgHGOhuLJbqqvrWGKUCCV8CWexrQLlx6XVeGv6LbXm-tHIM9ifGeh6DgXzqDz0TJZMQ0tpMwOpfc_zekTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3E_kOoYQeRCe2qUxjpyhtIHnv5hJN9vOANlpkvptCT7zWNIldn7xSAlRekSEbjlHl06OgFNYXXGjj3baN1mUVK3v7pCoSHgLrx59ehlDF0oLAqWMj3wKC0XMvD7bDxb0EZjv28-SpbPfaPbe_o8QFyR_U0eGYM8_NnzJqcbXIrWPIhq9FyVdkmVXjYTEA3mCtn3zziqVtQDCVd_ejiUyNWo6I95jmVNR6qD2ctpK3EpbYdTHMs7cFF6rFsenndKYgPgh1IJHpEfNS7JSUeRalQIZ0oD4r-f8K2P1cz0MP5xGGlXwnmtz7QWe31P_uMIQ4RTsk915HDCvtow14msmW3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3E_kOoYQeRCe2qUxjpyhtIHnv5hJN9vOANlpkvptCT7zWNIldn7xSAlRekSEbjlHl06OgFNYXXGjj3baN1mUVK3v7pCoSHgLrx59ehlDF0oLAqWMj3wKC0XMvD7bDxb0EZjv28-SpbPfaPbe_o8QFyR_U0eGYM8_NnzJqcbXIrWPIhq9FyVdkmVXjYTEA3mCtn3zziqVtQDCVd_ejiUyNWo6I95jmVNR6qD2ctpK3EpbYdTHMs7cFF6rFsenndKYgPgh1IJHpEfNS7JSUeRalQIZ0oD4r-f8K2P1cz0MP5xGGlXwnmtz7QWe31P_uMIQ4RTsk915HDCvtow14msmW3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb8oDaiOak3a43WW7lFqR9gFJ2SmT7RkORVc-ZzVDvITd4UY_t9nD7ECApZ39asLKhmM9UZGq7wtjr0pH1y9eZdgtdaPyLq2oySk7KxrsDzpZLw-hkp_a4WCXucy6r7pSfMv_G00RgmX0k6EVHMuZjyA2KCPdapbva-EQDcddAbbNEcO7XU3aWZ215jdMclyup4hqQP77LGNRi-Gw-zgoxl1VoR5SG76tTzp3AVccPlRmrJXZ66jBQFmW6wHRl_znt-kz-lc2STu8x1SgEDwzZMqd-akh3_zT0cICNFJLeviGD59wUGL4dvRNscxrUvtqNCewtopbQxyYrxzVXFjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzSPxS8x7ODFlG6avhWiqODKxMRxS_XmBQEAv-Z_fTftmqwX1YX48o3udKO96OGJNW0ahGG9cYwxSXWNBwWRe7X_TeioWotnQGHbFY_yI5AbeEogCfR2Ap30_Ow1lJktqdwcKG3GLne6DDvY3NFNXXwvPFltz4PcXfDCGUt6DbgOsmGBGjuApvA8sGJd2uZZmN93VWxXMzKimj5BQYErZblVklB2d2uAF7FLo8IhFgXnOeONpem9VkHiWZUSX_0W3ZbpHxMvlhfuJUNY_ZgkvO3cycL375QTgY63CKsMAhhIk6Dq86vCGtQiTll2ZlzIPJjq7gLJjpD9GRH5ICaGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhsckVXBj6Txx9-KAxmksdD31ZFZi3hbZ05QVMznrcapej7EGBDtgRIBj4PZlVJiVOP-zmzKTAVmM1OZcVKPvo075DCx1WpCcwRTDxVOEjiCX0--aUsb_X1Dryj_x2fu57PkXXjJk30dLtheoAGH_xTI34vxK9o6zA4qSmT0gbhxLW7pUrf3ONw_gIw4gpZodaCrE7aMaOWKFRdCFt1Ku0Q27oAM2icFn9C8Aa7DG8QKJynfUeEAjckDdLTEFU1gIBQIdMCfaHxKG3t5iOrKWR0-kjh7N31_eZbg3KBQtIoBaz4wjpXPNGoAiCdEfl4m2bbGwKIbTOt_WDjonJk_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=R2TukuB_owpqhcj0b7RM5PJr73phP_q66ZNLA1kRqJ8o7WeR36Lu9pCp7NceDOErTjpXKwmA2Dth8K2JuwqRqcbLuTW5WvDESM8WdrA6TiS3DwXnN5BzqinHw6rNubO029-kZMVdkBJVBjwxZETutDgYqMPvq_NI1xondbalPXqUYXa1n9SJZM_D_-Am8Gth7Nwxppt4HyAj5XhZwZ9nHxXc59b4Ow7vUqk0tbeI6yTNFNgNKeCzPAwhPtKmEqjrwSdiBsUkK3OpCqti3sno8EeN2MVDWv64R2e3HJLKYuwYyvdDNyIXGb5LkmntXBseusRToGQBt6sssKjLE4WZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=R2TukuB_owpqhcj0b7RM5PJr73phP_q66ZNLA1kRqJ8o7WeR36Lu9pCp7NceDOErTjpXKwmA2Dth8K2JuwqRqcbLuTW5WvDESM8WdrA6TiS3DwXnN5BzqinHw6rNubO029-kZMVdkBJVBjwxZETutDgYqMPvq_NI1xondbalPXqUYXa1n9SJZM_D_-Am8Gth7Nwxppt4HyAj5XhZwZ9nHxXc59b4Ow7vUqk0tbeI6yTNFNgNKeCzPAwhPtKmEqjrwSdiBsUkK3OpCqti3sno8EeN2MVDWv64R2e3HJLKYuwYyvdDNyIXGb5LkmntXBseusRToGQBt6sssKjLE4WZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPKziee4-UCz1aW_hPa30ej0jxxycRIaZIInL4U5_cEUKOjfcu0xSnkqitABDvl1n7G9EPpqIp_6t2iSNnTtamm2AGIvrzauOYt2yu1CtnCKIDgSgYYgCeK87Nz7jc4eLncCSD2ea8Y7Lx8wht_mwWa1mr1Qcpm7saXQy1LsBLBXRhPJO5dcG_B9trKbnlf_WoTrDPbA3HYdr41_q5PXc4fN474EdJ9AhkNn7Dh9wX3BIsuowG7b982xzyz_OEoUAmHVMbWTFLPeAdAvTIRwVjfrfP3WieEfEswrcNpfvAdYC9b_cooeASX_4K_8Bkne3vuo7gXxTruqHVAgbEtobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCxzaRQ7Ot7g-eUYlOqKdJzA-0AiyyCrNcq2LU9qxCgIYsz4IDGOIkwy6nK0tTUc6nMpJK7pePLEg9ip4Vn0xqHByn9dZxv3Kab9wJjitSacBtMUo8--skrWPVACjgIe5OawhJcmC5EJ4MNcDuuctiLszw5_24DbOOW9ETHaDyNVQB0WruPNwiyy2g6xLIAv2KknRBFRisNqZgY4P4WUFi8RMVn8NsQh8SqmISyyQWRSNdwOGz7CQ0k2jOP12Ujd74Kh5YrDN56uJ48yIloJ6W5Egm3Y1M8X6i4stXHCAiqkaQof3ibZDTnwYDkdSmjwnCdf_KBIc_vcLUZnesNNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBBcSDuT-VurVS_kj9JGxQyQCnoKzwajQ0csFtxFRuohZVEDjhtZMnci3A5FYv2q1VoggG07tGz2y9mKDclTAaJ2CQI8Gist5PgYuNXKzQA37LxBisy53zDhbe636bkP4eYU9ug3qSuDQWLWe60-4nGez8fVU1JnSfsaqygxsEHTSSkhUILp1iwAlt6YUV6jkoc0kdrxBKMJnvWx2L8lq88ETOGrzHEXgEpF7NNh4osmKqrMaxl0gEIHbfbOYdtEPdrYG8LAPOsFrONe6NLuxBhif2ZwaclBIj9v702bImUXSpMSIhMwl1OwbY50uBX1iobV9v5X4l_m359rsJXsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0qtcWykqKCHA1-78_BcwOraVxPuqKtgTxnJPuIPNO3S3QaPReVN-7Rt3NuwGvj5wZKLi2SiR_DhUHbSC9X1qU-Vr1obY5uFdnLol9u4i-95L4EV1zsaNjhy8_kyEw8rmNy-mibMdlXY97uOvzLWmExcFlZkXLATFsvpI7Dhom1p-GacqtJd856G_NcdZkTayzmDVt6K0xXiJoSGiRKP7PmooR9CnrdDkaKKO3-DFt3cSkIisk86jAYHjqeM6uW8CkvEYlFfQE8jms-N166jwPAqVuusYyh6S2HK8FJnoa3bPMaucgCcYQeIbtIM5Z18aUE_sloSmmPHzvM-fNesXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3FZ5GjvCpq6G4uOp3-2MpzVlmhaGwFLMoADvrf5lOT35HYL4xqPSGJ3rAJY67nxesh9HCJt4AW3GARWMkS8zcDxbKfXFmeJ_ReQSOAVd5feQQWUJCrnbQPV9A-iUd7QFZBtGQtibYsKQQMHZFKrMsxgEnH0fmsV3KUVIezAqKY6eI2AsFshoIBPlx2YbKYoI-8MM0Tb4W5zwanlZS4Q4EAARu-yym-DVfRnqMmRzgAJxEkXq7WT8AwlRgsC7Kvz-yeBVG6CmkHvG11pX_U4crfVaGC1G7ON8UZuWL44T056jENiCp8kUF6WtNwVpoj2gmuEtHOC_uPRakn8qn8CaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRVNbqS_MS0cPt1WbbvT31MsdGcjb0Qu1zYCRNxv2Oa56xydDzpmVoWeBKEtJ_S3mVoaUvJErdWZWqZO5rbco3hWe2KlEAKEu3yPg1LYVwnsI8rq9w4q-kSv0pdf-mgGlzCpywohEGZZ9iYq4oddvdwPR9u5ryq4v8UxwZFGLcU6USHmtkx_9L1bpF8FMKy-mMOv2jkeIlR-jdIC5iuq52LuxO_CcyA6yWQH7aN-_U7JPe6nLqQ-CsHjzrFkqJ-7bY6ujudiAnji43hEqxVFseH1PDo357-6xHbv_q49If2_IO9sSj3NzURSq5Hcygowj7uvMxG6gd1yhL-ooGOJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSSTx6Fo1Y9GGmhd7FO20JdUgSNNhgaYlvdp-Fnxh4_Gf0MOVmA396RZGMrQhV2sQVfy0z-gaQZGIh0K6KZx6jDIF9ehluSXKIq-53puFjnfZM8MROl6Vi07zwkeEELptf9Xj6GW2NoVlXhoM-tMjZoHccOu3YY5fZdR0AtdJGZ_UN6ViNEo_eIXNf4l8_iriItkwzV0XjSYkADrOvV9H5QoAHFuJMCPy0ZTO1Uw1DrtfupVV_OmxEVy65o76d-29f_0oRN3uED9T4hPtpl-P1fUPaFU8CxvIkTWAkxyJbJadDkIa9LcBGR5LGGyJGKikljGQ_awh6p22EmxrfNNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ1Wrhse_6N7yPp_r0mO8wKeC0qTmbki3rH40Hfhm3ssxZFxxrhUxYI-gkblxe-WejiqJRPof0ufL_rgBF46w8Cth3U0LdTeg-QxFqSbVhdaDSU5CiGoHtVs851RSQkCTHnuW2pSsGuh5acQaZtw5NEoQ6mqJBSMltcpHbJWAraIwNwlc3C8QSAOcP_InUdck-Ejlunj4LMzXX4AItt52l3FlHP0BfHbjzyjQcBZg-nfIZcYxFU3G3huiZFtKaCoYZsUKu_EKKep2P4oYWK7CNeCZyU3UQZ015VpKeZJUzhKLyKE8mHTtT7cBFyyQdrbcmHTB3ht1L9wYN2YV_nbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=lSPbwXdl5Pa7qVZH1COwgKgO-AZcTl61cYaT8nGwO_muAQwlSmGNfCKa081y-A_kBO0sfZL70QdZXahh_QYUuaOu_HhQH2UyFdpzkAr0VcAOIQTZAcl3ibp9HIZchZRO_zE98MU0TiHfzVHmQJWo-vaEo7PrJKaVitgbPBLBz_KE7S3EBMQqSLdBG5dXcv1wUNQVaKgFDFU_NcHmbcXh77czp7gxhT5ocvsHEg4-NlxQuBNzOGmtLz4CIse4o_nrszJWezgvt1CGseApazPB_deQ4PAO-ZEX5dD9eLznO2EaIkyyMFbWex3BnmYbQNT11r1K6ujUYSCpAtO3Nytvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=lSPbwXdl5Pa7qVZH1COwgKgO-AZcTl61cYaT8nGwO_muAQwlSmGNfCKa081y-A_kBO0sfZL70QdZXahh_QYUuaOu_HhQH2UyFdpzkAr0VcAOIQTZAcl3ibp9HIZchZRO_zE98MU0TiHfzVHmQJWo-vaEo7PrJKaVitgbPBLBz_KE7S3EBMQqSLdBG5dXcv1wUNQVaKgFDFU_NcHmbcXh77czp7gxhT5ocvsHEg4-NlxQuBNzOGmtLz4CIse4o_nrszJWezgvt1CGseApazPB_deQ4PAO-ZEX5dD9eLznO2EaIkyyMFbWex3BnmYbQNT11r1K6ujUYSCpAtO3Nytvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=ARjQMKO8slMKqWmbUyx089fQhXcBaDVEERY6TiGmiQgtbLILf8NYUK2jlPYMGNGG_ZQmaN181MqcIN2RFp8mgRIeq7pgRVKtoXt-aHQIRyyFcxHqY74yOizaXP7PXpSQ4ZDvgfcpowEHCYyX6gM-YtAwCJdI2QYq7VtFyNPOZsSRdcFKM9yDUmAH03bk41S1nEBouwrQeT1CftHTZwvlyBzBlq4cUpxoam_NE0HU6kF5jAHQtMeoJZHoKaDjoB7G5PgRbtT62XmjpSs8lYo809IYLvLCL4l6UW_u-JR3vNbd6u148Xl_rpQsqUzum3PI0Ur-ne4EgbdjL8sHuwNjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=ARjQMKO8slMKqWmbUyx089fQhXcBaDVEERY6TiGmiQgtbLILf8NYUK2jlPYMGNGG_ZQmaN181MqcIN2RFp8mgRIeq7pgRVKtoXt-aHQIRyyFcxHqY74yOizaXP7PXpSQ4ZDvgfcpowEHCYyX6gM-YtAwCJdI2QYq7VtFyNPOZsSRdcFKM9yDUmAH03bk41S1nEBouwrQeT1CftHTZwvlyBzBlq4cUpxoam_NE0HU6kF5jAHQtMeoJZHoKaDjoB7G5PgRbtT62XmjpSs8lYo809IYLvLCL4l6UW_u-JR3vNbd6u148Xl_rpQsqUzum3PI0Ur-ne4EgbdjL8sHuwNjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHL2eix3BU62b-qawk1uOV1GjxLoEO110cSqREjC-bKu2thQQSt3p2W8d3jEPcL0GfXrljR0z0Um4JS14dAoyudrUxR6dRUxZf9pQx6rtS7k4Qo-w6a-NQEuUj0EFnXDlFvr0ATVZ6mMIKptj9qoE4T_rBE5E4XhfJeVZVy8PyWiefQc8PIthhCNpD1uCQDCo0FoyYHCR7pbICIVQcqnsYD0MkcMk8r6SaUnb_R-AQoILSRceB60M_i4cFTUOSCZTArgoUfGXS5VSi-1tD9FMjgQvBvTzVQkWPcMhioeXuCazZS5NnOW5sn9wxqrgnvlGguIsOVxC6jMeD2MfO49iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=bj9cRg8tK1ovqVr4VHYTmoAQfbKufAaFRxBJSJYXbSW5IF281FKfWnVgqCu5fT2VfL-qU9MP9m-NlG2c4Y3OEim5mVld76s_asVKI7BF6tGV-M76G97Y93t4ZSQC9UiGvh9rDhQV4JI25UPDK2j04qDRlq8dTevnFrd1KnS7zhdTcXR6DtnGB-4Z6UYVe-DLAGPVua1u0XC-2m7KJ0TmX89H5bGA8rQlL9A8bHD1ldTRX21ZvZRmvJmgfbGsigWT_80lIXb4fidebdFkZ-zOPBoDxH1RUDZknsAQH11i7QL10IqiTpPWaXqK90PR6V9pEpl7J2wLQTxi91N8pCItGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=bj9cRg8tK1ovqVr4VHYTmoAQfbKufAaFRxBJSJYXbSW5IF281FKfWnVgqCu5fT2VfL-qU9MP9m-NlG2c4Y3OEim5mVld76s_asVKI7BF6tGV-M76G97Y93t4ZSQC9UiGvh9rDhQV4JI25UPDK2j04qDRlq8dTevnFrd1KnS7zhdTcXR6DtnGB-4Z6UYVe-DLAGPVua1u0XC-2m7KJ0TmX89H5bGA8rQlL9A8bHD1ldTRX21ZvZRmvJmgfbGsigWT_80lIXb4fidebdFkZ-zOPBoDxH1RUDZknsAQH11i7QL10IqiTpPWaXqK90PR6V9pEpl7J2wLQTxi91N8pCItGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghzc5ZqCDWQFpuUxYKgVWlNefS-hiSd5H0lOLk8Gkfs9_KyYU7--94L57B5k7eKFNKjJZXlP9qa1SeN9RL1U-kWPsFCJIzfL3MMDtsfuosbg9gtX3M73oVIsj_l331-DWKkQjrfJG-_QqTNhserUnJP8BsapPLXA3AylAQvJsWnEt2rNFDlVb-QjfyBTWX5tc38fqM2Zr7B2D_yy7m1J2rGt5IFF6vlcNdwOtib1SyCw0s6G4kSVcm2rZTHBiQHuV7O4Ixsm3Nrsp1D_zDD0QHLZ5Zi2DFE3oXhf-e7zr7RQYAMFUTLluYUN6ZQ3Wd7srBi-TGZw4FQwA3RuEyaHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCd-V7V5Kpe74NEwCrPq0_3S6PDCmpa_sgZ26X489ubuLfMOWfXGhwHrHmVXKk4FiB5Pn_ueY66P69BFs3vaoTJcZt9G_LtyvZZFy0GX2tbvqRxShg6JW2AX01hHHyFzSLXPB8l3DmtZOz_34omigtY0a60oGJUkwdThmuFjyG0l1o7DTIGz3Z1B2IlQIJpuJyKOK42qipy_7-j-TBKdHiGEXJu8ghfqfVIK1-_2soj9fY5phpj_MOXCN1OcTI0RHsHB8M3g9T1BiJwurN5xv3bySuvmTkmAyKRD6iVVtfHL-mIsJRXYbB14RTP9g1OtYoAk5Gd1qkmvfQpeRfsQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdS5OnRqA1nNoGJbUhhiknBq6oXoYLPh8TDnbvJk-8ldkth-AKxCflYaJLXl377mdOf4Y2wGM3dyQQM81LBNxicX_CUgvte-R0aU18O9GE4yGoFfF_cKXhX7UzQ1si-sr6WzXltWbZf3K6auhkVykuXDMVZGVukK51pML0k9viMKSFDmRHsAFeELNy88IZhCmdHM8278rKplZZqBM9qecSQ4F_nHOdsx091QqsKnAMDNjf-RBEuDmm17RH9Ctvt-fdTsPn25tTZb37o2GWmv75I2NAjmU5XtQw3RIKT1FANVMLLlk7n2JXct5IJE5HH9EEsoLR95E2sAq7udHTEGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
