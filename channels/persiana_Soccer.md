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
<img src="https://cdn4.telesco.pe/file/iWqKpB7m6HaYvoUmd9Z4IhqLKmsoNTnvELS6hLArbZiaRZfT737DKmiBh2FaLlpXisDPkLBfSJQ_9iZLOgx1vF-bAOnD-UEDKU8lVe3jUugp3laC6qg3yepVJSG9iW-9M2d6wZLdGC6cLb4l7AymtOxMpQI4eYfGvV1UidbJm4JF0Fg-_E-FYr8Iqsl2CYx7_pgN49xRbgEKxBcVTTU9XnQe0HZE1uIplHQjKwW6-62Ou_SfRg6rwI-NdBW-V21AUzOYpEAHxWEJF6ccU6DpQKTG_7Zz3ylRVy_Q78QWMQHLMpcPju85ZqnZ2kkpGo3JLRHCA0KUk8iycD5GQKlfSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILd3YLSDm71dN_rWvCpOgXOViohS0V6D9uaB10cdt7SCe5GCaF6oID4fKEoq_Kgacey7H1ERxbutEDcIfrY8XaP1rShxggujHvqsDk_XMzaU2CrzFEBNuRlVkf5nohssT4brHll5sgAU7Jo2gmAgCfemgvOOyKxEUA9UiVLWk2BwLYDp-j44G9cuxFtYcOdecGGtB4qJbUTmLIPWDnYjI5xBuEq8oT_NKp4REf8L4hOcetpsfnP-o5J8rQPAsq_95FUnyulST-Au-kD9Y_w9KkBD92a4myOhz5RoMkI-P_6tAXCcCq8ohW8SfdseBsnCYrFhjAqUUtK3_-hLBRRXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=SF_SRwN7UboFJK6jm93MIOcLhoDcl37D_nEjHqvUKNedaUPS00zJbOB5sKUVgqKgnUODepi7MztG4we-cvzHZXOljtkgHNoVEletqYebDmratdwwxbHqibzhSX2ucmGcfDbQvPfVFf6YSuZeQTi-3W5Ki3vfCMZ5K5sxOxCVCAqacKPNK0I-qDRjEq3KEhRxUy7NXd8XR_HkPyp0P8pmeRyru-Ww6HBCP_nikSgUOjTCRrh6ahlbphMClP1OtSv4zEH1IByZVLR3yflRFy6mCOjFAx_ENrdiTs-0eS6ZrynK_tgjVTUDD14NO93AO2i-QyMqqwIqMcQBSk3PyVD3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=SF_SRwN7UboFJK6jm93MIOcLhoDcl37D_nEjHqvUKNedaUPS00zJbOB5sKUVgqKgnUODepi7MztG4we-cvzHZXOljtkgHNoVEletqYebDmratdwwxbHqibzhSX2ucmGcfDbQvPfVFf6YSuZeQTi-3W5Ki3vfCMZ5K5sxOxCVCAqacKPNK0I-qDRjEq3KEhRxUy7NXd8XR_HkPyp0P8pmeRyru-Ww6HBCP_nikSgUOjTCRrh6ahlbphMClP1OtSv4zEH1IByZVLR3yflRFy6mCOjFAx_ENrdiTs-0eS6ZrynK_tgjVTUDD14NO93AO2i-QyMqqwIqMcQBSk3PyVD3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM9jXUAB0jYc80_6R7VOZZMlSkGa1KSZXIXJSnDd5iNADzHWWnApP0v3sEUZuWgQmpc7B5aMtzM7WlcHMCFtsJw4rWFtA9qHWtf9eYTgcZ8khna0GEw8MLAUy3dmBBWGPJvOoTlJRMZAF-C45y_C_gDN9s5pOpbKto4KVv-AIr3V4D7yE_Xk6zF9Nylu8PJV7twKYJq9WjZSZe6K3CzavscwRcCy5D3m-4287nB0gZo5qo_Gt2HHAthlyJFJOZ2VI4vU4xUnMBtl0EJEKN06pP4wGVCI2l_KegpN-_f3p6S5Gy8RlYd-UCMPQtSrXLO0pFvReNnPORxvrLe4xmTH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=KJrQxAHs7Hm3dkJBSmVCFB-BwMJOgU7HV_vnpJ2dQ27Hb278r3bx--0Ae4gNHroPiShl7RaLdWnV3anQKj7XUlN_2lBV9XKWBFYCq6y7YwrTcEt7M_lWUxwO0cdRebhTqga_LSRV8AxfrpiEGbSWHKCWLlryXxxCslMiU_04hZVUHCmDRIA00-d4mS92J8LNUsVjWDj3OPZP6kB1PEC1OPYZkDhjeJr5Pvxe8HhC5tpRif_SIkdb0-K4Oey7vqTYpCiH-k3KvPWHoRu-DxuMUjuZl-fj-bc7-8pkcaMqgV3pAk7Y_QbVY2EnhIeGVkpOi-ePlZjd_dUp6ObXELpsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=KJrQxAHs7Hm3dkJBSmVCFB-BwMJOgU7HV_vnpJ2dQ27Hb278r3bx--0Ae4gNHroPiShl7RaLdWnV3anQKj7XUlN_2lBV9XKWBFYCq6y7YwrTcEt7M_lWUxwO0cdRebhTqga_LSRV8AxfrpiEGbSWHKCWLlryXxxCslMiU_04hZVUHCmDRIA00-d4mS92J8LNUsVjWDj3OPZP6kB1PEC1OPYZkDhjeJr5Pvxe8HhC5tpRif_SIkdb0-K4Oey7vqTYpCiH-k3KvPWHoRu-DxuMUjuZl-fj-bc7-8pkcaMqgV3pAk7Y_QbVY2EnhIeGVkpOi-ePlZjd_dUp6ObXELpsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCkZVDVRozApnxw76FtMANxMg0f8MOYPDF1vEyRwEYU-vPuy2lj2v3cPCA9jwIt-hiL-Bdr-z9XJZP0oCIRFP2xsXVgCx_I92ImdF_Wbl6LSP2hCAu0Xy8rA8BxsDbrCJCCX3VFJUyfPWu_fx9FBufctoCvnv5KdS90_hPkwzBPocVzInSboF25eqjUwEH3Hw8qNb2xWSNswsfQPmz5xHzMiu8XQ7DwG-cO1zK40iMroCmvx00rR_u4ioq8T-bmE7NmUQ4-QD0ATtS9BghKv6xbjp9LCb6jdHsQZBjdPkjnc311iV_TViWV79I5iAG2uzgpxe-5TaLpqmusHhBxHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJIbKkPASs9oiNRJintKZA8xAvnoCZPCq3ri25JvbXl0RJVIT_BeIXEstv7ikiyywYAL6Y9M8H6OVsuOqCeNcJcruLMmjM4Ihqa3c7LGtgpnxg1P40z4QAKOPBe9vV9iMm4lkBjcBqaitBrEOnF_rG2lYfwhgsm8ghEM842VlhifFeUCxxwoi_t1hHkR0mBh95DnwcFq0rVEOVqfYn1y5ivxOcmvAquD5YgVU6x5rBLd6PAR41qKgl-SQ9UggCmxUC1FBefElZK-AhjS2ivXtu-37sozwfiamdqVT1BbnYBA-83w1K1_2CXuVcLPkPFmUIHxb1aamA-XF3FEq2M0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YEMn2UxOV9iLOlfFcQvJnXbYLVALq0Pv9eWoALvBhvSgHWtCOhF83TKjpLW9ZA9WQcn77GCvsT7XoFwDTSQZ8hhnVJvdXEZFEyyeO028v21DppLWqVT_Qn0dk83kh5_uERDUMPWmdTThykFd_HgLkPqn8mfkVxjPNh4ZaJx-dWRuNS0AbLyK9uQin8NnIlSfXsEy23C92i0Ew2gJKpIO8qRezs5LimskM2QX9qb5t3oRG0m1jbPUms83PpmKJdqSslk9aRtVuHxGsE-zaOm1WfqlF8e5_mL2OPS9VOP9lgnSjwHvEO5q1XGhTEEpkq33ZxPk1DeIZkGaR4-t9WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT1C5NRituRP1PkES2LugngbA58IhsAQYy0coNLkyLFgLoQ8GPvk29XMeKKDiyu41Ab_dB2NUZ9Zk3hzJwowEUznNH0JH6Q5aiEpag6RXrY4jNiylV5VrXN7WGAalwfUbUIA-sKYckJERbK_JQ4_DKCxrjdX3b7iGfz3s0cVNRKXFCT5bXAwn4a7-sqjEzCfI2nSokPwEVKqnH1pi7HLqaTahXOI0gtduzoBHfrq-aBqexEXNESE0dMMq2CXYhuIbQ5YYt-HBPDssWLEoNc_LbhoJXKJ3umzjSLE8cPeKX4dDjjECGJ-_B8m_SMC2HZH-ZyzBBhPIN0kaNy2O4Xrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=SQ0ud1HREJssr4tY7QX2ZTklkzPjQq5j-XSGoPUxLcWRMph7Qz3HRGyE-cUARig-zKjfUnkahtSg-HsDAWRQBM7g_wHT-eF_tYgKPbgY-0s0DXaJ50POaYNOInck3SOLVSu4MDMRH2pmbFvxvwoZEdTRoTcYZUtEwcKDJdPsxvo7ueV2UjDNlgV0TN2o2PxCUpIyJMJwrchrEFMIH8GIyXWv6OKeA14yDo_KBa5gCkXkVYXNqiakaxL70-GO25bTXPvycplu44wYr8dwHZLC_c-cQ11rBFtuAs6VMQfKenQ22aT7C4YTjvfEx9F__ALa17gSv3egbRzTOVJgcSd7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=SQ0ud1HREJssr4tY7QX2ZTklkzPjQq5j-XSGoPUxLcWRMph7Qz3HRGyE-cUARig-zKjfUnkahtSg-HsDAWRQBM7g_wHT-eF_tYgKPbgY-0s0DXaJ50POaYNOInck3SOLVSu4MDMRH2pmbFvxvwoZEdTRoTcYZUtEwcKDJdPsxvo7ueV2UjDNlgV0TN2o2PxCUpIyJMJwrchrEFMIH8GIyXWv6OKeA14yDo_KBa5gCkXkVYXNqiakaxL70-GO25bTXPvycplu44wYr8dwHZLC_c-cQ11rBFtuAs6VMQfKenQ22aT7C4YTjvfEx9F__ALa17gSv3egbRzTOVJgcSd7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg70vCUiqqDzJQQ1yxT9zpMovM9smRml_pcOz1EsUvcT45XLktlzURHRl-EpikuFYCIQjMak7ovsCZScdWkCQgtcoilHEJAkWPVWu9rj6QINeM_7Wrsb_B9vamqsYStrkmWb6jsz_QCBSsLvE7jhetNB4s-Ml3gUmAVYPGNGGqMd8W2EDcMhuFIbFNVRcb3jSung1M55uFCIhZ07YOhhiTyH_cx3sttDTnUb7eOkMFHGWPBFYoi7jBYwMG5Iv1FHgOlRKDm4kGtXwz2Hln-doSRuZORnYWiyp7BKS2Wg38HDlU7URxAyxjnJMWJEf9sq2npQZtl-XwAGplycp7nFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuD4C286E2w1VrJ3myv2n-5Dxw_fNBw3DXEgogaMaXS-7GU1iMjcDKJX1VWGOsiTGPsk02162Lzng1K4dfFMJVrG1hqzaBUL9VOqtAzA2yyyJ1IMRSKl95Ps2tY9hzytX2-QG1Gj8OdP06qSybLybwkW0qJjDW1OqDTR83_hXx1AUXrezO8ajVC0V0b1yU9uJzZthnpJ1Ko7lD1CbhPzBuOQpCja5ylZVYUYySeyXrLXXjsGjmiSQpg2F4KtNZ5WobyT3G56_imt5UGIw-a39zlC6FyOr5Bm4rCc_H2VicR9JtbBjzmDUNJAmKLTkndMJhEfJXS8EXMSPDFOjobeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22672">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxn1dzp3ZuXl9wBefXL4XTn6sr2QjmOI23G1lyGRdIHGedT-CiPaitblhSKmV_lW5uVXWDRS6Q-wMlaoIv_mO0_DKokCCgI2piezxVaTG4PX54zhUHcXSZGO8l1los1ZLTxSTHVoF540jRSnAJuKv1i7UmmrTEz3rE4MwPne0X6BrnKiIeAS6WQv6jXCeLVtimFyyZuJV5ZuXlWf7IuOERUwTFvp6pTZStTKqWeFFxvYdPRer_Uc3ckx01cMC-nKr932eXLhW2iSfBXY475z8M6ymgwSeGK7hyA9jr6rLOpZTnM-r78_7KFUk-aS7gAZ2Si5ajXfCUjcU3Uipfx5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
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
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22672" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSaayPErbbxIX_SEGg_BuZmmokKpa7RiNhohHluQzjgsbquQ3dYwM1hllSQTBfNkQcSggPI4Sx8IB6vRstvKBZrF_TcCd-iYhM-t_vzbwXfpbtKh_D7zIjsZVcLYwy2LTaGlzlNmf67LNqqVkLqwYbBdpI4zG-pM5El6wozCNTJH4ztdbZu-K4bbEPtw01zf41Qxuy_UhVIfFawfPfHSTUK750E_bxys3E7eIGh-ZHntwwzDkNWWYi4mvlInpFDGAcAbZ-43niRx1x45YkV1rIBNoFrEOMSp5GGYF4hTXD1cT9gBGaBSAKnbXV5-Kvtb9DhuWnJVzSRi9F_XRPRT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oat-ZeSdjXWOIVhiiOUFQ-_oO79UU4QWqKdzG2fVk36AoFlcIcMwrhLB46Gqq8tS5vO3FWFR0pNjnLCxWc7UMurYcjoX4D9j_NziHZ9mHhzWOaGMF0ccSVc3bXuu4IuCsB86WDyQwYtd_YjreZAVxtNo4K9vtxEM12YO_J6asQvICtOsrD-rCcbchrDNilI0TZ8w3qFpgGCrpazkAFNZ7gp5asLmDQvzdmBNcSOsUQacMBpLTdKL6H65H-FqUeH-zGrZjh5bKLfSgLmc8lCrJ8HLnb3ydm2pnSQ4kltsSo3m0qlH0vB9VjMUH62VrpMRIjrLOzY9m4eATqKPiBn6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXQmvB8rRGTa70FiWUhARawdIOYdfQdD2TFBkeDtQrnCqGFClDxw7Nxw3aP-D1045efENBYVcj2nDHNWM-cOqQLX6Yu7bjulIHo637TGdQ0JDF7-Tk5OFkxLjEYFhThO0a9i5zIQyXXZK08yAjBEuG7iGJ0r_dLblep0WwezxDooA-YnGQ878L3GFPQhEBWjd0hklxrnE-QDJdoJN_GxmTfgrls7IZQyYmmXIDY2Dn4AweIqjzukIeZZZagn1j7li9ktovPVIuDBCr-GMgeHRoVsQJDh4wbW4WzUwTFCx-lhK6XkfywfgI31_6bI2OrUpx-fVT0I5FxS2AqFSF5Wqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbM46susScVz9xwfdHfStpPR1pP9MMbUWc7ExfqP1doE5auc6JsLtZxAH6PbO9Mg_SvR_jzL5R5n9jhSvYVYJjrAMGvc_rs3kAMd4bYLBJ7fGgknnQUiypf1WcZA8Ycuzx3O5KLQtfiSmD1Y5ccdmVO4F913vaJWlWk6XH3yEIDgEKXaqqhcG2JSq4XBwuPxWXEBizdpDF8A_RENuPb0XQ8HgmCjzLKWGBYGmnrcLstAQPsPRxyA3TxObaqct7Eyh346NROMP66zHrBeKH41rxJKo9_bU0_fBt1NTXFVMAeOJGmRCIBAmpSm7W-ceaLItWReOOyNqRhRvsHcOLz5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avG1S1TCyKQ1qwhwtMntvd8riVbZPOGh3D7gOXdN69hICvYevv0ShmGTHS8r3RgcHW64fl2IZmW9eiTVX9yrMpSOOPLmozBa6U6kAIvI6zuJSm8w6i6F6BRwNetacUOcULejX8s9_Xd3Mobb0MPaUusastScIMohEKCJ-BhXxAXGg9U4ms7l0KrdmRKH9irU1sV2A3ziprQWsmX0y_lW2lRTXonIwbwjuDXe9msmKbv5LMDgtvQMzCbGRUfrV-9yMUHzWNqlhxKqRCNNWKHLgehGVML_iXXe4k8FjzEG7AcTDjiH25arnFzaHTaQGuRQkqSkkljjXbC44GU7X-etMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqxOSyQe5-HgezMYo9hXtEa6Ip3-UI1YFyqOewnHL3Q3oJrElqWlxxIIJ3mPAJf4KsAWWAtrdhfbMtdN8sUwM9VxRRUwpAhgWm6h1cMrGfM6OqE61F-bmfms2vZg2jQYvjXG47b5Lo5J30Dyo1ojZhcONZNc78VWnnILge24KEhvPTr3eERp23pqSYqzRDSkhVmyQZTfFJqmuP3eIdKnQrkUywcOhubaSZga3NvfBkN4QYHXtUqIt0ujQtxYtwmQE4tORNkncmx5GKww1zCWg6JY2xKtfosY2wkgUyLns5R7FCzsOfw_SjRu-3r8XD_kfAJnr9BAMr4mgC933b41XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzd1ZgESS86X9P6xtO9lUHWZyGSjhWM4Nz9esB1bAZ3lXLotrvJOhAQbBJVTaT9A2FGa2E2zebwhdscY6kFMLvvkA9HvXPglpI4fHBXJOoTOy_YtS-XU2UTVS8W_2wJwT7jk-25eNtEq0xLAt_MsgubuMMEgqIIAGgtrPU0gqa88WDIPViNKnjQsAFBUhPcyBWc5ioEs4P8k-hd0NNpEcoaFWzWzxWUNgtk2qS9V2B474inpADyis-V_x6DwBKxoph-m1dbi89BH61v3NwNGPfLTz4-hAUjLVzR6gClkLU0x-Iis8zdukgxMmDqf-SeY_wn7yYb_K9tpPVmvlvrRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-HBQH4QB2Ts9dMQplU7E3JEORB0ROxMfXMgpRch0TZ1QVRF98v9ur6kbwyJROc5CVajyPsiDA7vg-k7fDwRXg0cOe23oinkUawGXGFOSfklASc8tGRTwkatxKBFPAHSGXakvk2VDl5Ra-gtJ5Xlne3cjkpt2mYm60sZAwwhTzC7WIZ-u-eWkbrdAmykgq4uU2cgmzmJhVnzLLUhns70nZbByGOYvsydHnitDeVA2X31PmZV30umI-rvRD5ivgrUZu26CDo-9eN0D_fMEvj3p83NdPc3QKujgMrhRreE-alYWyhw_g3pbZyyou5P_d2wUI-aWW9y2nPKxRz9PTANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGWgad0Xb4p1-AsDO8ZqmQndrh6viT1J1mf7yBu20ISnBPHp8zKdyBy051O2HLTPfDLbePxivEx1bbyGY0mVTU8riresTNhzbRCVO7FMfitsA7hqsgQlt_UUZEA53pBcgIL18s6hwh71OzxcJ3d2noDHkwJKIsCUF4uFD47Y_xORxSsjsRLGnnGTbR3gmtBCRFVBuD4mkHFTvWfrbc0o-CtF4SCKAujFM7VTW_RYqrlB0GvG06EajJputO4WEw5ywT0OXFfCeeq9_0kfiqviLMJBTZcOQO4MDLmJLP2mPUZYYJcCzJSbGRT1Kthr0HW-mgt7vMIhf023ZIhqF6AZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX1NjWctARD-rovJhsUNtJtZutAdTW4803lXoEUb3HSjOC1cRMSydj6546dGP36KcgAj3816fkKLUFyL7UjojNO4N-8Vt8g6Tbp5l0nYqyzolKiB6unsGkJKTu6qUd7GAJ1xF3FpT1T12-zTH2uPNW_WilHT_pJzRmfWSWcFiEglB8iw6unqIwuZJbhMyyJXGlKr-sFOmqrCEmpr6JLVOXF3piW1yMU0OMjoPfiVSQl-m8GKdGHSKEQBHEH4lJsHxlvpaNkunyiBwNXH_qYwX4FM2oPQaMSModNQeD2mmOPbO_w2452g-XyLJKXuNRDxlt2jX4aKqtcXxFa-DNHh-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbDJ7YN6HhRBPNpcHulocX6d8PXa9DTSzxcj-I0cpumNJ-JRhIZJaxFQcg1TtOvr353XOHt7dMtUT4D9IhJOjRRoKjxdaQS-wqq8ahoavcBBftnMy7_1Dlf4HuunXh6M5jGs4OIvAlW4qSmWsoM3SbkvSh1TmZM-GZFH3igfqeaitPrAQYEn7oWVnnEWnZsiPKsiNfFXxByJR92uF5e-8ghW_J_Ch_t1K75oQQSMuzbAM6617J8qqRd2KiRd1mQ6PljgWPJenWLpIINDyF7P56OeKXZ2THvHljlOGNgsRgLEJr_YqaVNH-un43UEMdwvWtN7hE0jJx3HxGdLTUHg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=bNDLbTVM0YPvD5zv195CMrof5FUNxKTfyu_QUWww_zAbQYbd8YJnZCHh9ShZ0tkcxxs7Ts38zdDG0H2Vingpx6fhBBNS8BdWaOsu3rAPw6UNiXgLG6qzkvYr8quP-pO5FV-yzxtcrpOlt4FA7nMzfFQbqFpevCwUT8uOaEzA1yKxUxNl6sgg4eoWpBazx-Ay97jNZYn2wUt1weCeyQI2TgojuDAhtFZbYG8HnH0jsVi-Ze5V6m34irQWOmItAED1gw_U6sLNsYhisDMhXbrJCy16P3wPzOHNu0ZcoRYAKQQUYkH-uScv4o0jgR6yDyRLORVn_elqgkCJP1XirUYRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=bNDLbTVM0YPvD5zv195CMrof5FUNxKTfyu_QUWww_zAbQYbd8YJnZCHh9ShZ0tkcxxs7Ts38zdDG0H2Vingpx6fhBBNS8BdWaOsu3rAPw6UNiXgLG6qzkvYr8quP-pO5FV-yzxtcrpOlt4FA7nMzfFQbqFpevCwUT8uOaEzA1yKxUxNl6sgg4eoWpBazx-Ay97jNZYn2wUt1weCeyQI2TgojuDAhtFZbYG8HnH0jsVi-Ze5V6m34irQWOmItAED1gw_U6sLNsYhisDMhXbrJCy16P3wPzOHNu0ZcoRYAKQQUYkH-uScv4o0jgR6yDyRLORVn_elqgkCJP1XirUYRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU_dDPGcQUueSdHbtQWdNem9nD_C2SHFha58nuipyFhRgzOQyPU0OQJqsBFvnOJJzlw22VAOqqSiKC0_7g13Wydf2w5EmtMdpN2vmDorkVqH4bRUXOb-mKOQzySo1dW3HQ803TjDU1xVDeO7w6a4IqNMVrcakE8oQf5jwcJg1mysUA9gROoOXQDcbpPaoyWQwU27H9q96KhwaWFFwqeq_B1OGp0YEkfLc3AqcgMdqUcDnn-9LxlyySyJ28671nBS17P5nLaBxht--O_3LjBKLN4Rck7pRZPCzX-30CnsSzioTVZf33nyX0ddUnaGObrYNPtjXQq76yCfti3i9uWdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1v5OZnQS4kd0T9q9bFj56j61LWjSCpZ1dEl69NzYtMc2Czc83yt8D0Qt7k2-PuRSpR92JivXwWTmWRrdUUVz4WlnsIKhJ49jn6jl0fZn-3Zvzysm_S_xQLXwLI9cPk0BD_vs4spNxHm3c7YfD5FMD6hKpSFedOtg9uTKIU3aBBZze9Yb8qsoCfoBKYTIpH-8FnZX_o9CYadaqRJjW_IC1vkXeaUJOUWlcxlSt59F4NmtoM622DeMO4m3Ut-I9UPAn9eGxKUMGzL_SpXbCORzzG7coABeaIlmbZWkwVqsA0O4qGHjkmJW3sD1OZsfxa1AfwDonwPcCwV1WpjHFwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=GfY-NoK73nLsDFBR-_vpAN15zX6VW5kNojEItqkpJBtvTjY0tsBHQkrlRDKa3WLWTYIgFnS4ujwU8LPFvVsKBeQsG8vQ5jl9XcIekLu1kfSQmL_PSEvzOTFRT_tFQlHQ0ITg8U0gLZ_EILnRSrjCg1QqtnYlHEL7C3waSrUyeq8nSp8xhrQ-Mhmpy7LJuNEIgiA-HQI3q91Ex4QTibJ2bthyu--TY54X8nXT5yYnwrqKwbK_G7e7eBxfMsmtHiC8ZcKwo0WOogYxJD2k4ngq-9N33kwbxvwAIEWpNtPlwTqjXvVxk7PAYeuLNSngZm2jduwra54MWU0BbT1JSi2FZqjy8ALTVgFNWDeK0OO4nac_HywrEZ__5eT4JYZTVNPXaAnjyHJqG-EuJwI6LpW_ardE4nujaWeonFW_XND9F0NfvX9E-7Tr26roNM7AK6BohN352D225XFdn9fzCsl2Hyz5-w6QrhZUFBPKCa9xEvVw5y1c3NqUXKnFjCi27S9a3viyC4EXRO4tJfMeuX9ksSUncRNq8ubEtKeqgWkcHvm4R27n_Reo4DFJmss_iXjADB-Ufu2jqp89-ZadkcNhFD7PfT6WpyYsBaGbhDc19BpGtImJeaDJCxscMvnyc21_LGSYQ6QuyKSjvDW4fgym8fOxcxmoEKJdpXDX4e9O980" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=GfY-NoK73nLsDFBR-_vpAN15zX6VW5kNojEItqkpJBtvTjY0tsBHQkrlRDKa3WLWTYIgFnS4ujwU8LPFvVsKBeQsG8vQ5jl9XcIekLu1kfSQmL_PSEvzOTFRT_tFQlHQ0ITg8U0gLZ_EILnRSrjCg1QqtnYlHEL7C3waSrUyeq8nSp8xhrQ-Mhmpy7LJuNEIgiA-HQI3q91Ex4QTibJ2bthyu--TY54X8nXT5yYnwrqKwbK_G7e7eBxfMsmtHiC8ZcKwo0WOogYxJD2k4ngq-9N33kwbxvwAIEWpNtPlwTqjXvVxk7PAYeuLNSngZm2jduwra54MWU0BbT1JSi2FZqjy8ALTVgFNWDeK0OO4nac_HywrEZ__5eT4JYZTVNPXaAnjyHJqG-EuJwI6LpW_ardE4nujaWeonFW_XND9F0NfvX9E-7Tr26roNM7AK6BohN352D225XFdn9fzCsl2Hyz5-w6QrhZUFBPKCa9xEvVw5y1c3NqUXKnFjCi27S9a3viyC4EXRO4tJfMeuX9ksSUncRNq8ubEtKeqgWkcHvm4R27n_Reo4DFJmss_iXjADB-Ufu2jqp89-ZadkcNhFD7PfT6WpyYsBaGbhDc19BpGtImJeaDJCxscMvnyc21_LGSYQ6QuyKSjvDW4fgym8fOxcxmoEKJdpXDX4e9O980" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq_fRMdu25rW_DnO_kMF9a_nFTxHv6HqXnybki7gl07gfmbRHGnnb8Zytv9WPvfolWtquQByOg_i8amAez4Fs3y2Wfnc3AY_y9xOr-LoFEMDXDC0oaJC9dzpTrTUo51MGDXwEDEojTqCFVDRDcs3FX1RIbTiil0zesfxT6YAHGP7nTFOz3iWu872o3Vgl6HBzJpZ9EQgKpt4pqGk7sWLlPn-RdLxounOjU-IMnEFI-TNrSplgUF1SQenXqOLXY3SIeCsoPIbcdJiTLnoiTmD50fWkI0FfJBYD22sQGZvtwB-izmHkIUQLZpjUu2rqIGzGyqVb_wvA2mXi2yy7dfzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs1EnwjQRiPUhlGOBA_7KFfxDRJz_j5PZvwJzY39qgXhV83swW2DdtdL4tZlfntwFOt1uPGC2vqRCmVaBQEatPrzIzs0Lx2Oarx8rzcXbdtKzvr40u9rEdIwb0WYelelvRPkI8YrGm8u2i9j5RLWP7TbrfarWr1idji2QoQPAeJNdcqCCDEUGvT2UWcJj0faizQ8k_gmzz-56OWEr6t5DwtgA16jppvs48hbkIe4qkdfsmMK7Z45MGXUVFQSaRXbyUPqArd-2fNaMXRD-E2-jB7N8_loYH7aIwAP6LFDmPiJwRQS4An4IR7-0qjZ81IV-TFIMhLrJshbjwiHepp4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22651" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAn8vhCyXwnFuIuXaU3zcI2XlqBQQ4F01-koPHWciDC4WqjwzMFl_Kuu45DDMy7jsfppB2qS5ETJxZ4aAMsVeinb-cAHOrqXoQ2LVkOuCeZQOXni5SMtEDNHHxyNrW1EPAJlu-ypdLQO7fY0jRo8AGmnmTZ1QC5EO6PjiKcnefsc56KxQdlyFgtWwA4rgpgtB0Y9VIBMdeLtaQ0maGZjvRwsLfv6GycEdCXBFKepDg2-JqS_Wxt5Xtko-k7GtBu-3xYpab1QCmGeGKDKhlKwFs-0o7xzYWn6B3R5iSom0BeVH0avekZlogatBZf9MaY_8fP8-_0b45N-T6rKbYNq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaOHNvDT-Y-0KJhjWsgphlRduDHKEYxFqfEuz8dW4OmRGknGovcTmreZ6qwTwo9k3MJheS1TFNpUOGRTftYG1_IzCFvB9VKgjWBZgEaTOx0U2_fqZFHlNutEox7oeVudCcz-UC_Ay_c4J2fYROLZFKQvU5qSO7RnX6pliPrwWy4o63SIwqMW1F7J5_x3JN9OJxqe4n9LavKPZs8fBZC5Urv9Z3tD7VpU0CJhn9wDIKUJcYzLQyWoDFSGW5io3_wPdIZgIvnftXVRyZvidu0KIOqgPSCGnf3dBhyYRqJmwk2hhONp2CniW3Q9LirreKYzb2LzKSO903EB8PgP4_ADoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv-W_xr7beGP3DKGWcH55l3k67riB7kuCPH7E9sLF62pUWoXAJqSy_4n4gXTSsZt8xuonirddlVQWBsvmHOmc_8logkfnC-cihuNWoyHOj0hfg-3zAeoDdqZNYF4t-x9jD5h4xBvEUKK6mlVnDwtGo1SXr5DkYbTN6X7NXo3xL_WWv0VACIL9P7aclJ0XxVYIzhNIAj7HOBdLyef2XJpLD5KpkczbHq7r3ymKyy25j1N-ZMZ0-Ime20Ma9YROAR0trcNumuQdcGrGYr3TJFbpQQNefP0GWj1dqqaWC25Q545bOvGvp7vb3w2xQ0Di77iEWmwVRVIZ5pk57v9HgRhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6Yd24U5AtNm6TlRnH94QcELxZoOQV_QU-XHUW0LWDk_zA6GharphGYBh8wT4lowysyT19M2oL9ey1kOTqh6lMF0yYz-frCcRPpOBvUk3eSdtsCns9et2IXr-3jesS2KaokRPeBV11LKJ4iWafO5oQ-FICT6U64ngmieV5O-8KjyvKvCeCJObabTrjbFhDd7j4RZFLI-ebZHI56eX2sct-Rx5vlkqnE-IEcqT-zFhsYt4Oyfnv4LFM8EkenkUxtLjDCU2Bhme_E8a6xVkduVZcoW4iCZW8hJfNL8UsxwwvhKV2SYG36qvHv066n9Nk_yaONYClaL-KL71vaL_jwthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzinCT8NRko_Z6FY5TpJwJXNU-Gy5pcwqrcDKFohTK3ASdOJmxBD8WZezGhCS3SDtZYRUcr0pbSSYswYV1X1_yoEDcrZNaZEBzg2K72hwHMuv791s6dxlIuk6jKgUrfIzONF8zfwhMbL0eD8O2pusatqCEB-cSb_GcasWv6BYv73E2r-8qn94eGL8z6wnIjL46RsKHRfrSRSo3XoHXPCXlU8TMXXRqPc7LxClV3pjzvpURo5303rU6tPzpit-Qa6_CxRZNylQr9el5JBlbs8RRi08Rw-K-jCLbNlh1uaupRFhOXS7Ru3wrO8l-AQPXKRnwJ_02h6xaqCSqeikcOJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2fMSPi1P08woO1Enu5q7UVXmljTJifOAc7sVPKfzUOOoyXwKM01AdiRKLImT7UBVtSpCCOssudwDdP6EUIjWqi8O3HHxFTMUu-A4coXOWR3Zn98BTfZBXMZbhYyfgRhMZmRXAsoqghTd00T7nCavBmu2H_sQXcPSjaZyUaIE5D-XZlCXrI2KQTuxHjxDZkdX3i2Kmo6LFhg6eDWV9yaT1bprlFEbXKbU5IZaPts0zeYDZxvbjspQGLq9fjGesfd_JPk4zSenncH1BDXWLWEUp5Ml-XZICG-zFsiR_HxYMcTH8T0G98o4jc7z63c-Ruobr81oaut2vfKXlmUsyjBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPVmY8Gv_Co7GCNwCirycuYaMYMHyAtWEK_s1yUxfrhktsn6AiW6k37t-2ihKDgkoRl8JAJtuTAtRd-AdKRPKDgjr60cw-gdm7pkIAcjlWjtbgswWHU8IMSjscm8B9R-B_1zMC-i5Im7zQ5Wuc6qENccd4TDuPKTFQ8KMsCJknOPsIGrrE__N3SMBctk5O8NuYG5Aw9Jyiu0QYRfbVwNjyZArW8cP6jaTqkaN0DYE1IVrKV2FDObff34MBIoJC3lx0UXVU_WxqpfPmY-pSI3stZYDcVyOpokk9-jxhKSCvUZdPlfENE9NNAiRTHb-I4pM1SRvbUw7dI8gOdsNNRjRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=cQVJEOjXsfqYVjA4T8le1mCJyODbOcXin6IgIhIofHAPNn6vq89qcSSK8CArivX_xkcRqpsfZ0oSZZdBV3cg1YUnpmv5rdhddsZjol5UEbTjee59LBubWUsWEyp4imOcY1CKuZLJkdY7R-ORHXuk8vXY2w_7B6u4c5DksviCO3LylKb0rJuwhH4h2aOO6Pr5wmu5gkhg3DgFHczd-Uu7QnSCAE1dMSuCcUA89H_10NPjVWaEdyvCXxNdfWxQwKO3w5go3_TpG1qSy9cEvwomIMgjU5FtrgZQkcVr4fpdySQ-nwEF0mWvqjBl0GpMTLTlQQ3nwEuigx1jT3TLRzcn_TGK0dDHkMmHtDIiBQSWS8bVB63Wfn1NbKA17WfZqwjQEATQd7VTm5xH3AGOF0lLjXLD7odkOyQ1y8ZOGB_fPdfKDPsztoCZfAazP9GXZ5UufQR7LgddkLl5v74wWG1VPjRSGIj-gC_ye_ZpTddqhvMYnqbxG5SlT5K5zt8Nxq5hz_IcEAoOhBRTD0hIZolQQvHSHOLs-Ddz2DZFJliNWmxlWL0DXXPeZnT0Tec87eyVHg3zAgM9DWOYLw7qHR2HqOP4sucq4PnhK0rbTusiHoJTaHrwrz9gx8LNRXJieBwrvZXIMrOznhPNTaufGFN066rPnInVVTMRrO7dC6Q3nv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=cQVJEOjXsfqYVjA4T8le1mCJyODbOcXin6IgIhIofHAPNn6vq89qcSSK8CArivX_xkcRqpsfZ0oSZZdBV3cg1YUnpmv5rdhddsZjol5UEbTjee59LBubWUsWEyp4imOcY1CKuZLJkdY7R-ORHXuk8vXY2w_7B6u4c5DksviCO3LylKb0rJuwhH4h2aOO6Pr5wmu5gkhg3DgFHczd-Uu7QnSCAE1dMSuCcUA89H_10NPjVWaEdyvCXxNdfWxQwKO3w5go3_TpG1qSy9cEvwomIMgjU5FtrgZQkcVr4fpdySQ-nwEF0mWvqjBl0GpMTLTlQQ3nwEuigx1jT3TLRzcn_TGK0dDHkMmHtDIiBQSWS8bVB63Wfn1NbKA17WfZqwjQEATQd7VTm5xH3AGOF0lLjXLD7odkOyQ1y8ZOGB_fPdfKDPsztoCZfAazP9GXZ5UufQR7LgddkLl5v74wWG1VPjRSGIj-gC_ye_ZpTddqhvMYnqbxG5SlT5K5zt8Nxq5hz_IcEAoOhBRTD0hIZolQQvHSHOLs-Ddz2DZFJliNWmxlWL0DXXPeZnT0Tec87eyVHg3zAgM9DWOYLw7qHR2HqOP4sucq4PnhK0rbTusiHoJTaHrwrz9gx8LNRXJieBwrvZXIMrOznhPNTaufGFN066rPnInVVTMRrO7dC6Q3nv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4kaAOHAh33JfID7nfgieMzOXvtvTgsnBjahhjTEfZwobd_5XvHeop7K9j50wX28ee5HaWANa4SgYcPopzDtazQBbNxcqTbcZr3UZrHpWb4_599j4YwTFet9lfpni-X9p1FsYx5gLlmrvYE7xBdHy2ou-K8pPLhrILWEodgevSh5T4n6OInsCzwxvyuEC66VgbY1G-8TbpLPBm9bk_wiy3iHwRiwiDc4T2FQZxoZSzyNvwMmqoPPco9YEpmFgupKZkNC7km4rFhKxIlI9WIL8ekwBDY1u_oOUi9KN_KefdXtzFUzwjFh-ZGRdUd1uQ1iM8rKce3NRgw8_oRqm4DC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=oTPZN47c_4XKvyeqw5xDesHdbaC8nxQdRINEpX1nMfk4Z4XrqPcCl6aufyaY4LoGVFTI-PLP0KhtBtUcmgcQcKohtffT_TALGpUBH39_oAZk36JeWD-OhWognF_2BOejXt_pitND4yBT4Q3AkNKBvUNqif2k-nL5Nq2SAGVYmzf7gKTZmw2E9uaD10Qll3N3aiwlNlWZHMoxTZGaCdyZs-ve6Ams06ijXNLYGVe7f5eRcwe8RXqoOIzFC59Pywpz3yWdWuziKu34SzgND2UekepB6L6Th6KYdsNN-hT3i_95-VXiFAMQcv6jkXe5uKr-VurQQEUyPG9cwXt5plMkkJCiq-NqTgf7HoLkQv_RE8JyO5svpJ4KXqEhiegUcpIjriwGMZLd80NGswwglb_YxSZAfP_BuMyehh6H1g2dDtbU2u97OyTiqT3V8BZiMinPXxk0RYbBdSd8TuOf4kzYOLQBjupkLYiAnWPN0kGjPFQ_jNnzbHuXURJdvynQgTMLCvQ_Gf5Xwvw7nS8OE90Y7la25xzC7NYVTmR6kFEQFntLKgn4atI8Y1dHYjJ_VQDJyHKtuwv5ZKDr6rlwEHwKCLMi7N_KHMKeiNXpTOUEvdH8A2VbQPYykhC3Pgq1uIVlY3MNx5a9NJcLaymxwcglX5CopbAnLC-Lv7J-3lReGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=oTPZN47c_4XKvyeqw5xDesHdbaC8nxQdRINEpX1nMfk4Z4XrqPcCl6aufyaY4LoGVFTI-PLP0KhtBtUcmgcQcKohtffT_TALGpUBH39_oAZk36JeWD-OhWognF_2BOejXt_pitND4yBT4Q3AkNKBvUNqif2k-nL5Nq2SAGVYmzf7gKTZmw2E9uaD10Qll3N3aiwlNlWZHMoxTZGaCdyZs-ve6Ams06ijXNLYGVe7f5eRcwe8RXqoOIzFC59Pywpz3yWdWuziKu34SzgND2UekepB6L6Th6KYdsNN-hT3i_95-VXiFAMQcv6jkXe5uKr-VurQQEUyPG9cwXt5plMkkJCiq-NqTgf7HoLkQv_RE8JyO5svpJ4KXqEhiegUcpIjriwGMZLd80NGswwglb_YxSZAfP_BuMyehh6H1g2dDtbU2u97OyTiqT3V8BZiMinPXxk0RYbBdSd8TuOf4kzYOLQBjupkLYiAnWPN0kGjPFQ_jNnzbHuXURJdvynQgTMLCvQ_Gf5Xwvw7nS8OE90Y7la25xzC7NYVTmR6kFEQFntLKgn4atI8Y1dHYjJ_VQDJyHKtuwv5ZKDr6rlwEHwKCLMi7N_KHMKeiNXpTOUEvdH8A2VbQPYykhC3Pgq1uIVlY3MNx5a9NJcLaymxwcglX5CopbAnLC-Lv7J-3lReGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjRlGaFF0grara8a0zK27euFwf8CHX1vEltcT3Xq9w0c8Vv-Cn_cRsWcyRgiSUsnCgAjQ4te-rQVnqVenZ0j7CGDm_5vvfBwtj2iWZERkOkgmFZoHO2U1qZNz39cK1r_2b_wmFSsEEeHWkfOmao5yNuZkSzpHlvAN4ZSjqwQGxOUGHaDtclUjl57Idu0uhG8bWi1-kYxFQ9nDRdJaL447iAvhg1FJMoq0kzWXag0f8F7NFn0h2GgtYriCuKlf6xDPP_6yITSSFIQszzsteN2HkqJH-jpMbD9P6xnHuhVX1g33BMI2y32ZTBJB7e-TNIjFenfMupYpJR3nyphD3bH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqEGBs_S45iSKugu_QTnkwNp-Lt_nwU10E2GI-7xEaNR-F326kS0BTBBfk5lfYRDRnLOgr_dg1GXPNn05xM5gi3Qv48vnKSMpq6FPXXYCWm2jlvOyZD_6Vtcl5HxdVuqZQ1qJe1PATbhADIVzcgPeDHssca1QkiQdxycslPf0sszyfM1AGkkSK8Kpf6jwxJzSZuTonvjZt-dDJBPNUAylguf4uOMvx-gJ84i2wNNDB0RWx2_x73AwTAC4bCL7d-paEygKeGGpFtq0L6EoWcpfzsltTGEHFWV6i4lx-8P4_bCZYs1A5q3OBrfAOJMz8z5Y34DYA8BxZVRecaFRxDCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=eNwF83iOiFHIn36lTYQG0DIzRHcyBKTmQHpdbNbm057lvr9cgE-cGik9pk4AxZTbpd5htD7t6Y97VTCyFgBKN8vwXgRK2ZXYNgKzO2LrtM8_lyy6Z5H1Kt0uwb80UpaC8M9a-tFMZK-hD3qO1--pzm4HjSU-RZ9v7Pf8tHTmD67GV9ervFpW5a17lVmWzaY_vFDf1r9fmLIk77uI12hfWERZzGZN4ndQIMH01Gd06Qh1GSwRD1Utob0uWrp1con2cOBFFauml77rxf2WvLnbdd1kMGGkqRKa13SSUsrpPk6JZ7Et7TQP-ZX38-Bj8FpO_E2ikzKYEJt4pSBNBYDi1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=eNwF83iOiFHIn36lTYQG0DIzRHcyBKTmQHpdbNbm057lvr9cgE-cGik9pk4AxZTbpd5htD7t6Y97VTCyFgBKN8vwXgRK2ZXYNgKzO2LrtM8_lyy6Z5H1Kt0uwb80UpaC8M9a-tFMZK-hD3qO1--pzm4HjSU-RZ9v7Pf8tHTmD67GV9ervFpW5a17lVmWzaY_vFDf1r9fmLIk77uI12hfWERZzGZN4ndQIMH01Gd06Qh1GSwRD1Utob0uWrp1con2cOBFFauml77rxf2WvLnbdd1kMGGkqRKa13SSUsrpPk6JZ7Et7TQP-ZX38-Bj8FpO_E2ikzKYEJt4pSBNBYDi1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0GqpyIKZp9bzFMEYF4BpEXDgIpoNn7AAEMYSkFNko3az02DKUGBredLE4sbQh97Fdy5HfBzUwN1BTAjEGpGDk_D8aZwGZQmjKGMOUVsWlVunUoeXfeqDM_khzJRM34lyaEz1Oodk87wCv4udO876uxj38Dp_S1IrpGgKuYyH5D_vIajzTijpTC1sdrIexNfdTrsVyqK3Xy7KRqAf9-rjy0jKxVzxV8j-DM9jVGob-r6D96V6tPOmvWOPWMPWNW-2kPACQFnsTGXNXCic2P6MFTjAMU5Q7dU-yE3J2JOnTA3uMhmHDLUHJA63jD7aH_8p69ERXPqcrUQEqLAZ3Lblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIUNHMiPzsxKV42Ck7Ty3EljJsyFXDUy_wgNXZ137SRE2z1yZ6gnSI4vuB5t-5Rdp9oaG87WfWC4oU1P9MKm9orbj6LvBB7qPI4e8Q4SgzC1x6nVkrNCIqH_gV_nOw7bIx7kn9V_IOA2qv_MvfHjBPDggyn8H12NNOfJLgj35EzJXUCHKcY2UgaLh2ycM9qETm-7Dx3mLdcRS27GNmgOGj4MupD_DgegAksIvSd28-D0FmBxoeWQkD5S5BXqNRDlGxqoPijwdWdZfOmywGvXyIzTuYL49L0tevMicVXKZU5vqbiRgIEJAKVLykVx6R6pTfukfxPhj5AC_xUYCz6_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=VsRo7S41cpXBZsHLX9ZmwGhiUDFqVPetzWaqKFGgWwhynGzkW5Ajf7E8YPAFw0b03r-JrdTBpgLJwmHSNZJqcc8npZOwrdMLfKanQYcbsEl-Tvm0KZD3N5QXXELqLFLmH81r4WPJwwms9lJ18l1tnNRzLXN95_MlfZIelcnm75DH7sX9u1c-8VDebKbVOQMtvsXx97junXD2ijjw58BBIZSJa_iyx-9whteB1jirb_vyqE78Nu9r3ZfooxGPMNeLe1mXoYfSou6w-Rgevd30P_1iMKxIazzjSl44mDAMZZvHqtzxDd6DmxJYb_-E4-qjBMMwHxn4TZZPOjyMZL9YGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=VsRo7S41cpXBZsHLX9ZmwGhiUDFqVPetzWaqKFGgWwhynGzkW5Ajf7E8YPAFw0b03r-JrdTBpgLJwmHSNZJqcc8npZOwrdMLfKanQYcbsEl-Tvm0KZD3N5QXXELqLFLmH81r4WPJwwms9lJ18l1tnNRzLXN95_MlfZIelcnm75DH7sX9u1c-8VDebKbVOQMtvsXx97junXD2ijjw58BBIZSJa_iyx-9whteB1jirb_vyqE78Nu9r3ZfooxGPMNeLe1mXoYfSou6w-Rgevd30P_1iMKxIazzjSl44mDAMZZvHqtzxDd6DmxJYb_-E4-qjBMMwHxn4TZZPOjyMZL9YGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFMtYgIy6kbwZF6cQXSJsVOh2SfqRcJcAo38XVGr2Z3t9G3VFDD7pYGogup9-9ZsH7fn71_vUhjZf3aaN4hZCZWEbpkAyMM3ETdI2nWQsUXBb1e5x8j9zoNiNZij47CqZEObTlXCsjo1oyHjH3J0N2s7uYt4uKxptcbWsb9TXrql3zQH3A1MQifnyEpUEbFm1lCOU5A6mOiup8A4m76dp0b5sXXZzjKb6MaQRaNqWZIzffiTarOED1X58fCBQbsFXuVZf-dV2WA62DEf_azgUGwA5VxdL1AvSTlwCTo3Qqu_zVzkgWWqUD_4hY-fe8CcalPz2a_0QsElMeaN_AVdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfHG6neFve1naVXCqeHG0kkzLZ-yysYjgek2s_VozNt2rLj0XnX6CPjsrgyGYMPXkpeRo3MvTGgBC6I1f69GvCX-H-zy7Ot6_MuB2F-3l4kRIsvIdKmnN0rBxrMOjCig9HrHMrTpFwAWcxNy6nGghJx9p9eeK2QGlVuIxzkOcVCYtFb0UrAZmPCDMLbOETUld7yY53sNuLtqVv-Ty4TPLk8Y0ZEwI-nRG9ckOs-0OnlXN3w5u4Ee7hxmQyTTVymxkspBfX3FjlLHm4P09XH5Rr9TBXateEasHixFAwNyVuvbVkUh2BB0FTPkZT9OZ12-IrVGo-y5SBSS-ZSZA_GtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=JbJMvkuekNKxSckWIVnnGrTawwmAfjS0iOPXs2CdHosIarclCEVTi2jlnD7-w0YJen1qepm9__MTFsy_cJDjiFx8bpEglLRtKc3fyPCoYdpRM61_s6I1wIu4KH8Bo-dHQtnN2CG8wSWZFlJiHBjlDSYvH363aIKWpl4tIW4zbPCfhjLp39S8FR4FzY4MvyPq3-d_Nd6duuS8T9Zo0VeW8uFiZAT_on1OF28J-pKlkKG292SeB5RBLdPtjmLpSlt-JlGqLoeSV33W2xFHfPzzhtjm8FJgXklXAz7tW4rlvjMt3JuKDtY0JwxjkRUeoTRfylI7JwKzQg7oIDO3oc7esA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=JbJMvkuekNKxSckWIVnnGrTawwmAfjS0iOPXs2CdHosIarclCEVTi2jlnD7-w0YJen1qepm9__MTFsy_cJDjiFx8bpEglLRtKc3fyPCoYdpRM61_s6I1wIu4KH8Bo-dHQtnN2CG8wSWZFlJiHBjlDSYvH363aIKWpl4tIW4zbPCfhjLp39S8FR4FzY4MvyPq3-d_Nd6duuS8T9Zo0VeW8uFiZAT_on1OF28J-pKlkKG292SeB5RBLdPtjmLpSlt-JlGqLoeSV33W2xFHfPzzhtjm8FJgXklXAz7tW4rlvjMt3JuKDtY0JwxjkRUeoTRfylI7JwKzQg7oIDO3oc7esA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=hNPzEoaZ1yFUZctUNkMc1P5KDMGPbFytKW_s_2Yz6qBlnd3c7xbLq3pfrbKKqEFNqefxtcPkt7ngNP9ARgFy7oDZAbl5eaWd7OEH6c-xbzNWD0ENW64WTvXVVqH4lEPKp2Cdb4O9waDt0OpFhpcnneUIuO3maqTYgmsF35ZBWyK2hMMAJbF16NFL3Duj6DB9PethvTz-zNBIGl-2RRogmE_ExN9pzRrYQ8c5I_DMgv6TqJdFucrNmYMRIf1dX1AfSjZvomWCIydV8nxANOsFwqINXGou3BuAoqb6HIE32k3pwiyewsZB2Pt-AxnHaJ73Sjlbbz_J-UMhOjbWqDAlmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=hNPzEoaZ1yFUZctUNkMc1P5KDMGPbFytKW_s_2Yz6qBlnd3c7xbLq3pfrbKKqEFNqefxtcPkt7ngNP9ARgFy7oDZAbl5eaWd7OEH6c-xbzNWD0ENW64WTvXVVqH4lEPKp2Cdb4O9waDt0OpFhpcnneUIuO3maqTYgmsF35ZBWyK2hMMAJbF16NFL3Duj6DB9PethvTz-zNBIGl-2RRogmE_ExN9pzRrYQ8c5I_DMgv6TqJdFucrNmYMRIf1dX1AfSjZvomWCIydV8nxANOsFwqINXGou3BuAoqb6HIE32k3pwiyewsZB2Pt-AxnHaJ73Sjlbbz_J-UMhOjbWqDAlmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNgvLrATOO1uCxb5L8KxGySGQgPJZdpPK3gdfcXt-kA01YSKOsI2u1jbOLi-pt9UAJqglGXoye4iqFz0oMqHzmYJXh4fjQjdQuDcRNlRb6Yt-XTQcYVUDNKYFklP74EQdcmQsNVaYHXwAt1K2MEQTCEqMJlyaJ1Bfg5cJrBxuLDcVmlQZLspnws_JWlVNO-3LWHZaM3Q0jHnj53iebZQhb82-rnFRbj6yWfGtsNPqcSaO4Ml8VPmeX17SItVPAITje-vyUJHEhLhUg-wEJ8cfF_EG9F4IaewOZiKem-dF1XUwXnuj6sTPlEMO-706Xm3SUDqsJBuuXZHu3ZVX4MFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-ZSg3OPtce-GDRNHj8gb0uH5_6CFqgO0Uyrwso070S1mfzwGEWP7jCRfTzm8OiYTIVjpq6ydROvlj5MEMijwaAiaaDNY8uilBHQLsitmE8Y1g13GGOetH6K39PIobL9DJVDKUjMHbegDFJ8M-dFqe-k8TdHsNXkCzFSVhAVHMAZwhdbYzJDhQvwwBJtzyj9IOKccGvp6gwFhDmchhFqJJI1NIssj1b3nDpfHQCfBbJk__91PM-C32zLP_Z7-aM80lVFGhSzY3Cap_QlVRXs2uXvYgKJ8M0D1mzCD_Lj7wr-Z2xmkHg7ar7Nw1wnA2Az87qvI05gFbRoSwKE3vdVAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=aaMBGQ_fQcqe9qSxCrDgQQv0ZEDG3xDZcymVFb8kEIcb8-JjZBzR4dQO7bWZI3Sd0Wt5Uae2NhYeocQv9Evic3jQfxka7Q5OqgXOTfkzdPB23uJLiYYK4GXBh_HG54PesvPjBrfuDGlDnrf33JEfCO3riVwcCT0sPT4Wz78P53F2kmmwIVDdHmv_uhQmM10-rGP8BiX3j6sxRwNnWNsRLgFa4YyxCRvThfxpn_4Y7O-TQ4YW8yjMJ4buQV7R9b9xYbHYG-nz2A-gv5lcM77T5Iy3XxmZ6DX1B9frrnAvzFNJYTjmcd1Sk_cfNxDhT6uYdc-0ndeS9L8Xo_zvF7aonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=aaMBGQ_fQcqe9qSxCrDgQQv0ZEDG3xDZcymVFb8kEIcb8-JjZBzR4dQO7bWZI3Sd0Wt5Uae2NhYeocQv9Evic3jQfxka7Q5OqgXOTfkzdPB23uJLiYYK4GXBh_HG54PesvPjBrfuDGlDnrf33JEfCO3riVwcCT0sPT4Wz78P53F2kmmwIVDdHmv_uhQmM10-rGP8BiX3j6sxRwNnWNsRLgFa4YyxCRvThfxpn_4Y7O-TQ4YW8yjMJ4buQV7R9b9xYbHYG-nz2A-gv5lcM77T5Iy3XxmZ6DX1B9frrnAvzFNJYTjmcd1Sk_cfNxDhT6uYdc-0ndeS9L8Xo_zvF7aonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=E5xoRHltloyXZ8LvSOQwdJn2SRlAY4Xbq8O_dKl25IbijpyKd1QCokQ0XPiUlxvkjzuSSKBiW1qaHqG9iaO0KxfkZGKY6uoQx6nWDAYA6Cyzdiw6QtLmsiWbOnC7KlJOe9W6fsgvmFCuLfzcjrTu3WEy6HMLIV_o8-nYoI3aJlP4Tgz9uZ57Y2_UG_74gfMr-STeHFEVqOFCuJBxR5Hn5fjnnLAg861cmu4VPhQTkJxPbAB2kSEQh_oKirRGaph3O6Hrnv-Ijz5tmvzCkrkkw_W5KWLuY0ozz3xKJzuZXP1bZ_fjCNVLZDf9YB2OB97mrsq0w1J1g4T2tiMLlzbdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=E5xoRHltloyXZ8LvSOQwdJn2SRlAY4Xbq8O_dKl25IbijpyKd1QCokQ0XPiUlxvkjzuSSKBiW1qaHqG9iaO0KxfkZGKY6uoQx6nWDAYA6Cyzdiw6QtLmsiWbOnC7KlJOe9W6fsgvmFCuLfzcjrTu3WEy6HMLIV_o8-nYoI3aJlP4Tgz9uZ57Y2_UG_74gfMr-STeHFEVqOFCuJBxR5Hn5fjnnLAg861cmu4VPhQTkJxPbAB2kSEQh_oKirRGaph3O6Hrnv-Ijz5tmvzCkrkkw_W5KWLuY0ozz3xKJzuZXP1bZ_fjCNVLZDf9YB2OB97mrsq0w1J1g4T2tiMLlzbdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPRBxI2B2YZlgr-u34mBk84Vi5k5l8VqmxrdhuW76TvUeFs7q-NIfB5-bhxqLfpImF6PlGkzfQbiKO3-271r79XoFQgef3SSoUhHN3UUkYbAznjBVC6y1r0FX1-a2bKIIV5dltAKfaBgJx9mbhqqCi8N09spBRYJC4AfBh70Its8sT3ETalEcOY_u8ZuIGCqNgJKIAp10FjI3uA51Rke0TEqLHacuCXljUhRKo2tOCmNZIz5qWRqOXJIykXVby4VD6EcpgDtnvWJ9kerMz1VVcxsZ9zMP_XA5D1mKvZZiNbge-S2KhNOn67RnB4GNtFntmY4ZfM4aOugtFOGSeFxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sobo2kHzWgyVbg6uoXwxh-zOA0tsePqfsIQXkEqO5SKL8M_YtbOX7SBlCILkUES3ezEsUiaNkt2V9q7XEViYJoCfJrLk6f5uB8nkI8QJHrtYbpPk5nYDpdfXw-VUZd1L2D3jUZN8praNQRI9HaTlmSp9zi3drV8AbkW9CGFr4Np2fQf86GdTtIrP9_AFAx_d0wYZ1oeEhpZqTSA8pUcXBc9OvuMh0jEcmmwlFjFX_xmPVFUUgZqKxg-K-hrApxMTbomiRUZxZFwueHGRJSMXzL4CaC49vYUUTgyR5-NVja1Jeg3qmrL_zLUtPqfWesR91gy1KWiXXixr4biQYiCzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6-N1PlMj8rkiMnhz-uVSM4uk9Gf9jN2-2z7TJlKrVfx6OuK2tz5UkOwq8AqbhIKoKN31GpnhEdizvTjfHl_EBgfG0nWv4BhvWfqLj4xgsKQK2Gv4DQqtKxM7ZKK8IDNgRMncJpz95Fu_YELf2T6YO6wUluP_cbPUscTFeXCKBcOrWISpjnPVQg2w7jEfNmEZrI2PPFzDqXAKs4O7r97il6mEtf9879XPtRbBJ0yB3P5GSjvicxPFpfAvLf4snCMttOfPdN59B2gjTSJWFgIRm_ARBrYT9dsf7h47NHQvkMLjgpIFPhqwpJZlrjGRRV_w0JOqAwRuf2tGS4Y1h0aMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_vOK_BpakOjN5NWyiezXOHMRHykLuAJJhoAeGx0xhxIyP445VZ0rVMG7ZBkH5kNZ-WWosr0Z7gDUR2tfOhOQDM3RHCrXhU1rXs6QeTju7_NgJn4KgmbM7saV3sCoJe6e4k2RwncPLQbftN8fkZKRy3Zh_wi8GM-snM0WRUmwg2ekNXMBKlXXrckgh3ORcFHw8hyHVwxxsVvDIQ2rZ5pXJDjNKdaerJNI2K9gtU9T8RSwSbWrw904GBJvHEnHOZ1uMjSMlv8lCWOI2Qfh5Jh2Fqa9XU4HD99NHw7ZGEfgy6Heve-riVvITlG7vVPmMmyGLRPqUMPz5AabHNss90Rrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDeGsVY6cjpo3hCot9AH_6hDyjIwmx8VI8up2coABkIcEFjXbb7HdhmXv3ZVBU8hndwbaGyC73WwBVwHzyEMtOHrPQPwnbJ8AiCdecS6Ri2C5AKaCU9v7uxrJ8rX7acpMritF-RbHLQMiU4EOfh0-xchVX2Q504OoSX5C4Nww-W60bkHVqb5ze9jNVwAKwCsJm0emVHoGyJiOippk6N7Sq1J9tyt27KbKJP1mTqrhHe69RQBtzKGxlk1kaUwYf-zQPd0OHsZFdBKCS-gp0EgWSqtjNYbqzxcjeZb1h_H7OQxKouPilDSXc_U--xaRkSBzG986C43v6SLcW9zO2Xq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=NI0qUJnXZYtdJwb6EAFdyjx7cboht669CR493hgF8ylcXUqo0_rDNevWtZCiMZMV_NbE6dnG7ds8E7fmzLMLm0X3gAmopq7AP4p8o4ovbh5ewUiXdN9qAeZpn6XCTfCFBQX_eZ2Yo_9y2xbaTS5sMDrj_63qL0Jtk8i75cV9h6OTcxi-NY1nPyz7h_UrUZWjU4YMzHUj02md_Z0Q9dF4hx46iShRkG5JJZzmCHPUZNS1QhvK0IDhxW71IFRfnzNaQpXI1dbIJuiMPpOgRLoMZIUZ6eUjEqITgFiycBymLjBN_bA9LrTlBNngbYUxRi4KfnDRrfVV71uYK-JU9uTouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=NI0qUJnXZYtdJwb6EAFdyjx7cboht669CR493hgF8ylcXUqo0_rDNevWtZCiMZMV_NbE6dnG7ds8E7fmzLMLm0X3gAmopq7AP4p8o4ovbh5ewUiXdN9qAeZpn6XCTfCFBQX_eZ2Yo_9y2xbaTS5sMDrj_63qL0Jtk8i75cV9h6OTcxi-NY1nPyz7h_UrUZWjU4YMzHUj02md_Z0Q9dF4hx46iShRkG5JJZzmCHPUZNS1QhvK0IDhxW71IFRfnzNaQpXI1dbIJuiMPpOgRLoMZIUZ6eUjEqITgFiycBymLjBN_bA9LrTlBNngbYUxRi4KfnDRrfVV71uYK-JU9uTouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB4gSJtaQzNCrRf9PWaHBKlqtQCi6Dv8CLyyRCWh-q4fvXDbEwJeuH5loZlqqcLvHk532hGCAku9JdmOQ7R8LN-yaPg1x2pLUXng-omD2GGcrpZ1d43wpBED88WkbBLxjN4VdKwcuqPDKhBxjfKppXhlufVYvX016ut-LwrOl9Hf-QTP3IxHYSb5VrIGj5r0hQ0EC7l2ImVEIUapKc0l75dFWqWcjwvpMbX7v4p57ZiEjYlYPXk5KbQbQbzCqPz5Tf8VYtRWB4z6DLoDJByAz6WCjAdNf3KFfdtoXeQ20x5Y79NXIlp7V6WeXUAGXYRR-Pmfx22q48vBW57AkRpqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=tb10iIUe7Ux-AoiKIrzf9EnHX1x8TQmdWXxu4Dl_9SQdQXTd22nDi-IkCiJpNDntuIBCSfbs3x_nXYMtfpCTE5yf3pVlRyaWsiUPVY3hZnojYxtladk3h9hH7OMbx1EqOT8XMfXWRmB7-wpwK0cj-TMfjaM54v7CGUaUcqHrlMG69SuaGeAtS5KR-i2LYSX7Qzh-k3YcE_sUsIYMJVODt4lR72GP1kSjDvRZGfzUVP_BH9I2NkPiDr-3nZvS8T4AIxaDngBnG1R3359QJa4Mb9pCgCQ9zoycSD1LipGXDznHaAD0dUh77-_tx6Doay_i7ZBoR5-fCYGhbO1DxOkEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=tb10iIUe7Ux-AoiKIrzf9EnHX1x8TQmdWXxu4Dl_9SQdQXTd22nDi-IkCiJpNDntuIBCSfbs3x_nXYMtfpCTE5yf3pVlRyaWsiUPVY3hZnojYxtladk3h9hH7OMbx1EqOT8XMfXWRmB7-wpwK0cj-TMfjaM54v7CGUaUcqHrlMG69SuaGeAtS5KR-i2LYSX7Qzh-k3YcE_sUsIYMJVODt4lR72GP1kSjDvRZGfzUVP_BH9I2NkPiDr-3nZvS8T4AIxaDngBnG1R3359QJa4Mb9pCgCQ9zoycSD1LipGXDznHaAD0dUh77-_tx6Doay_i7ZBoR5-fCYGhbO1DxOkEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO62tRD56RtJ5aTeDud1YtY_Gtov272UTSvArcFql8OsySCdrHYqRB_aq3taZjcypMW6K8Vg7_tu6b1fD4m-ek_P0nPpesOa6sXkxr85Eyx-vCz9p_iQhkNtxhgcMVcRFbMHAVT1kovgp_oBTvE68XZ2FpZrdfoNX4fLpSyc6gDDWAeSQO-CBsExJz9FgMi0HCVqfRFwVaMRukzeICnRzm9TBZjwWrRub2bav5ZpRPVkrgKP3sLG_5POh-CgVOHIDBX6G00dfW5a29rAsbIJvc3VeMKHOlVixv1MNq_MoAnUQq7ag5ZbWrYX6wdU0oYEhw6grVQR6synKjxOaP_vtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=lRVBosVCta0nb46dd4kHEhuXMC45mY1MBchZAFCLjG1m2XCdzbZdOXrQxuq_QXJDhRhVWMW_CtJuJ_L3jAwjFEunFtbySePwQehdVZ9QsZzJOgaPJegpuNtJmgKUieN2fNJ7bp_yHVCmxpeUHxdYDKoa1SOMRIOrYEPWcW3w6OyE8VeRM-GsrUXso9WCrhP1ub53vuxwnnOiytKV5bgSukkwg9K_jbxQOO2VU0AmpuNKmrrOQzMy9qeJkQhFoFbCa2kKb858F3CB6lLzmnh4CQhXULEkZQriV4ojz2N7gRXm3dSrYTFYkNde6QzQ9w2-48s4EDIyK3VH0pMRAhwnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=lRVBosVCta0nb46dd4kHEhuXMC45mY1MBchZAFCLjG1m2XCdzbZdOXrQxuq_QXJDhRhVWMW_CtJuJ_L3jAwjFEunFtbySePwQehdVZ9QsZzJOgaPJegpuNtJmgKUieN2fNJ7bp_yHVCmxpeUHxdYDKoa1SOMRIOrYEPWcW3w6OyE8VeRM-GsrUXso9WCrhP1ub53vuxwnnOiytKV5bgSukkwg9K_jbxQOO2VU0AmpuNKmrrOQzMy9qeJkQhFoFbCa2kKb858F3CB6lLzmnh4CQhXULEkZQriV4ojz2N7gRXm3dSrYTFYkNde6QzQ9w2-48s4EDIyK3VH0pMRAhwnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLd7mfvAP4P0FGcaDNqQE6U1cFyd_iu_bCN4-HPTWZ7DB_3XIv7SDyhFZzAMpqjGKR62MDDcI__4SQSLRs8xEpcU8n8fISlD_i3IeJ9Y35ie-mhpS_x9iXfouCZpryJ9EzAPW2Wbdx3K_zCDAks768xYxgW1lOxa1pGS2BRwd2xEgV3LmWJ1iR7SixF74r_99Tx0cKb9DwOKMuALMaB81nCAwtSgJs0k-4pZ44TZWX_94mTd8uEnjhy7hIelAagbJYu4Oe14teac0gXTNe-vli0sjr1kyYlkPqByU_S5cyccEltCeMhfanBfS9FHl8Nps6-6hpnPQDA6Vw0kbUqkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkBQ1kCbDDjI44qtIU37bB-fjRDqwLxsaUbgNxT6AZdfDVbvKu0Hk6phvKO61mPWGJUT6vrSqC0_T0bsKTRymXRD9m3w0cruV37mZAifwCVpw1h0poDT4L_-jt0pkaiDzxfR0S8fzw_ddc0zKbmRNfAW2ks6mKniWcpxMOgQ0_34rewEoYAtgn_sRCdaLEXNJDv44bNaa6MYEsGnB0ow4glmxClVDK35nIruZZEVCXhtsN6R0HyFRR0xjXGKRrR6bP0EODjKAOFsA22Zvk9cOn_Mm3o0_HWa-sRPLn1TTcq8fmturjwIdLEPL2oq5d2QmBiBqRc8W091ZcipkbGvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHhSG3zqBxI3xlPmWChY8JpbhgXFoZA4e-gBQfU_Sx9d7GpsM50cll_yd9pcGE3CwJTaMFK-9Uenn-HHckBDs7hb6HvIChW50MDuvFYQ99xKpm5xB6kOAy1mbjCFxkyaob75l33QnYSjwHcUUkSGVFODy3_Vd3G2n7bMn2buFV0R6bIuiKEbg_yX17rMAfapS97dctRGMjrZpBhXcjPyKB4Fn-1VHCoQ636SiWuegUFwySlpLYx3YmmxzDqkhXREU8HEvT7qFUg6aKtMWRXuPH8NjBRxnAewK3lIolC6svVGDN4CQIXLfxzRo7ii4FkkpuzPJCywscTCWHOvmgc2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxdzZvwbHxp38_sOXp0QE6DBhUjM92GLN2GXnPtlLm262P0fg1RwyemdyT207_prl-kSeszyqch0YEMa6a3x-4ALdVagRG1TtguddxFn7MezJsMXB_Z2vgsWLn7NkixBRbE3Qwx4cJ4oocZZQ-SAm1WTKH6di2y1P4xnvDe01-qer7dS5lsP4rgoub7axUlNIZAPaDRO68ci0gV5by1c0kZvZT6XB0TWaIDKUIHXQa9M0i4nZHHdLeHxmHZLldEoIt9uefciQtbxHA2eLyFmPrEijYbIg8XofLPPx3LqJKzOVGz1w1E1EOKhpAlIUpzs4AWS_NnKEQnP0PfIP0pLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHg0WK47oeGdo4QgOCwE4HbjpGrmQAhIQAcw7jhuAgYENMVmBE75GfQyUwYgplqtgqI6GbaY97AQ08qG_vQ2d7ohEjrK2IafgfP-kWQKkfsGcNH4OVVVcwizdH8d2Hly4oOmXS_37zFrL0kwEIoq6WFWx3a4qHzYa_tN5BoCDCQ61c_yfmfw1gjVHOmfAk7cHZ7QTL9G920FlBaIHWxIRnrE8j2ze_MnVsJ8QJaItAFT4vb2DCgZ8rSC_eSWGNlasRaesiXyVJZB2uo11-JvH0ivoWs_VNClkVQ01NXIn_oJlOV6ulx79Dj6HUBqRIyv4zVZBXi906nTnNhAPNNgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s76DHVy5WfFw3YFoYJd68b7VPaK5ZPQAgavrwtUdql8kRacODn3RQa_30T47KWzg1cK8jsT88t4zTqHibAV8OsQBDfqe_iWqos5yc98Oj2gyT9n_KomeZIgivjA4KtC6RcwWKl66qS-Yx3wUKE_f-wq387Gjov5_3HutTTr_QzoR4t0aX8KcgS-PRnKug2hIOJCpUH1Aq03EZAnnFqtAV34TXezT1Dp1It8hA4nCRdJ7FagpwINXNeMEKGmWNZP901-Bhm-NtW0k1kkI6qjjBLfF9wh3xWGYHGzYyLrAL2DmpdZETDOBR7bI4H42paopILS7b6BNuu7azoBu3ULPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVQOlhrAz4ElJZ4jGXnStXpq1kh02WLstKjJGEZWhUvHcNlfS7WQOAIuJRBlnscF-oGT-2VnC2yRnCxZKyFsD01rEryXNwCkE-JZZLejfI23SVWo-E6VAMoMiOFrdnJpHdYnvtzyA6Rao8Eb87O0g3TVOtIa79Qy2TzJV6QSz-WKSsr-pHxVyvXL4OwT7eiaV-kail2WrmM6EmmG8EpMmVza_WNE_KEdkzwMyvDNfFG6aVN_kVTWLq8xuTa7TRy-PMZm7fZ1pEufcZnZ1L2s0cwCqOMZH--i_2AnUaQyQu5VWzFBm7iTdGMuYoPcTlTM61p9drdZnO2MI-448oLgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evM_3qXETtXZRT7XHzDz9WlJkp6M85EYrPeXa7eNXBD37UnXYt-E6g2A8bSsi4I-BPMSmEM_8fRg1gxNOsiauHYPSYaBHg8IxAt12uwwJ4VZYXJLrBBZhv4db84ULMm5QgaQ5ojXBG5DfCL4rjynCwR7TnpvDtpejMqgrdX4FIpCenzpeMyKXRPpge3ky0PoJQkl1-NLeP_r0eVwE45yfFBpefVoAxtDFcAKHmy1VyboLxvjqFyMbXHFrB-Pgkkf8IH5WD9-y6UYmvKRUWlbKjVFL9QJm707QYi9KOAvRfm6Gea3hEqFnNXkIZKA_HSjr5Heuc2Aalexq8PIgaEsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=dl3REvc-bUXQ3Zjt4DXd7oS2GPPebCPNCZlJ6C3O-TMWn-OSFHSNvye0_8snmthhcFfgE3Zd3Dsb71NJde1gwLFl42sqqA6KkS_mPIml0EXaJKitMaI83TpTyHjkos7ClydrqP6x9wZFJ7d36UgSB04s0p9G6MKF3gZyYh13GEo-o-2sFje5U_xTDkfMfD-AY6HlYnSZF_bJeaIIjSk1UWmnbFBZ8hp9cuOeF-Z2PUJ3sMZSQowgMCS9EkQ5U1AXjXlB4bjV9eEziFz9hQAVslsYaCw75av-ZG7-3mXcfX-bBZUV34Y-mZJ9ZM3z9naPVEygf7Gpk_kMIHmK4ZqGBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=dl3REvc-bUXQ3Zjt4DXd7oS2GPPebCPNCZlJ6C3O-TMWn-OSFHSNvye0_8snmthhcFfgE3Zd3Dsb71NJde1gwLFl42sqqA6KkS_mPIml0EXaJKitMaI83TpTyHjkos7ClydrqP6x9wZFJ7d36UgSB04s0p9G6MKF3gZyYh13GEo-o-2sFje5U_xTDkfMfD-AY6HlYnSZF_bJeaIIjSk1UWmnbFBZ8hp9cuOeF-Z2PUJ3sMZSQowgMCS9EkQ5U1AXjXlB4bjV9eEziFz9hQAVslsYaCw75av-ZG7-3mXcfX-bBZUV34Y-mZJ9ZM3z9naPVEygf7Gpk_kMIHmK4ZqGBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=VARyc-UqGfXTRyUSCAYcwnYEWB21lWyWx6HuEtmakgutmOikoaDJk7-pKxHkFRyTRdFL5et70BUpPtP2G8gmT5aYj7zKHEe1qyxixGnLlgGkU5PUkPAXpympSUaG2TlYoeIOwQxpn0ytOFd6S70RLwTCr2s5MCqyZXkIB9bfHooITJIgmDgx71vRamkS_I0khNKhr8PNKJNkMUTJAmVoKaihkL8xgGEgTo5dOGXqrmLSn04_gXzi2GMSFCwtcO40iTxKnjN2wkNBcsykKCnhY7_2xMjc4juUjvGAcmfl5OEea51nh4igLm-m0xlkh4lxMgdkOHG1YUpp3h2xRNI-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=VARyc-UqGfXTRyUSCAYcwnYEWB21lWyWx6HuEtmakgutmOikoaDJk7-pKxHkFRyTRdFL5et70BUpPtP2G8gmT5aYj7zKHEe1qyxixGnLlgGkU5PUkPAXpympSUaG2TlYoeIOwQxpn0ytOFd6S70RLwTCr2s5MCqyZXkIB9bfHooITJIgmDgx71vRamkS_I0khNKhr8PNKJNkMUTJAmVoKaihkL8xgGEgTo5dOGXqrmLSn04_gXzi2GMSFCwtcO40iTxKnjN2wkNBcsykKCnhY7_2xMjc4juUjvGAcmfl5OEea51nh4igLm-m0xlkh4lxMgdkOHG1YUpp3h2xRNI-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXHW5i5rryQOfvTumzDSw3CoDH9aM9CS1G791Rl5VpvYKErwT_tyl1KUWtRhWOewSy7B1nnbxrgrsmnlvBdrZN9k5c6WEEB5HKSthYBB1U5u8Rd2ZydP0XQBo8_QcnWX5iihjQTHYqHUAGPqo6VTQGVxtquHlSGQAUILz7as9JTckCF84nj5dPhgasMQBwJak5m_wlgSRKa7C6mO3FTf5DlWr3-6Si-47__eyWwAKgDTSxaPqLgIipaSC-idAgtFPSmB7v2_V208Bw_vCq-ovpDujDaXw0XU02oPQXJX1RS254rXEZvgOYLMn-3DOzuzf8c8neQNBTfuJJxocSN-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=ni03THKRlITPxzwTYryF16wYaNTGawHgS9KpS4EJzgrkUJQc9oxgPNQyq52ilxtAfxufzUpGfOzMJIPGRUCVIluA_55vJ2VhkY9tFgL9i1mLNZJlLn_WNuDCj4RadFOTeUs3A8819i16evb1-JtQAvJfx4-Uk6swOyzHIMCRVQa2Ovy2WGbKLrTlomWCWY_ciLpSjHqjZ0uW87-9XeogSHM0cpmYQ_ALNIcEi-F5m2HFacd-mcUEk6xtLKlJAzRQ9bf3NouxZHcXSNFz2BTvRMeMZ_T6Pb5U6rnKoLbKj55A78QxKAbZSb5lrdcKt6s9i8DHBZV9tT128flUOP7ZbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=ni03THKRlITPxzwTYryF16wYaNTGawHgS9KpS4EJzgrkUJQc9oxgPNQyq52ilxtAfxufzUpGfOzMJIPGRUCVIluA_55vJ2VhkY9tFgL9i1mLNZJlLn_WNuDCj4RadFOTeUs3A8819i16evb1-JtQAvJfx4-Uk6swOyzHIMCRVQa2Ovy2WGbKLrTlomWCWY_ciLpSjHqjZ0uW87-9XeogSHM0cpmYQ_ALNIcEi-F5m2HFacd-mcUEk6xtLKlJAzRQ9bf3NouxZHcXSNFz2BTvRMeMZ_T6Pb5U6rnKoLbKj55A78QxKAbZSb5lrdcKt6s9i8DHBZV9tT128flUOP7ZbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF0ZQkuV5tiLlqED9DuhCCe2eQxFxb6AMQbotDFHJR-GeEyVd7aYGzYDHJisehEp3PcwyhRdvpOXoxGA-Hw33b4eh9cDxvISfYkCixZjEq8S2H4n1Weap6TLsy43ojm4H3At6vOj9ZJaVo3YrpWGfrXSEDgkSjJOCdj-8kedKlLTano31LkGOsGeXUY1Bhx1Z6b9fzjHcLch_Ac0afoW_gdTyxP9GEKyBFgSK4XM_L1gV36t8XY21AbBI4eILNaJEEqrli8xoDFyqLBMh9GGx4HbsFhVAtdOlmFwR6WPSSMhq6VXF7qex3ENLPdG1KUeDyKQUhTgqj-w_6sjt8K8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veQF3tjyh9h1V231XqBqszxoapQSGr2yVEXIz8tQC7hKFX5bKxL7h556BGCdkTIua4epcXTk3Bp-4mOKaIgnOyt-y4_EuhKC8hNmqYsmQvx5NtUGPJF4SFad-3-FPZwf9vh2tZZe40hTDacIBB0V-jxt2iRAFCjcSyUow5KoQ0U1z4YC-PDg_r91NIJ9Jh2QbM-r5C1KFmOghvGlV5YAMXUOQgBqXoVJxATBQV-pldqWH70YSycimTWx5dzYrQjIw-mKyyUxL8DTE3nb1v-YAlUdQTTfS1Qdp7UNIAYS-9QsQSNDrhLJEKhFaySj_2axz1IimKasUe2F2HeYthPqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=prUDkgf4R1vvI7sKZ5kNjgwqD8g8HW8v3W5s_gpc_nDjqQ6qvVJPMEYwSsXeQcwsiMbJXNz9Rqd-HNZykubJnm4eM8sl2zTUDDW0F_ruNLF38-ferz6YQJyjrmg-UrlvfAWsRQQLaq3XI0x10qdmhmJzTvVyFOm--XGqNxv1FiZ0krBis5ZprFwk1ztLuw1uffpFjjG1caqOgZBbffrtVoFiQuPMmCqPDn-Kf_Ve8C8DPBvLqDPMLYE8jsP3GcMaEeGNVl8tCyIPJGvUvOE27srgyJKDcLyBcrHtqypViIhqkztymfKrVM_3ZdbcPdPYtjbLWxO0i670RIB-2KAwrxLs1ZGduptAEgSZS1PJ7Ol-XuJid8gLutsA0DWTonzLK0vU3VP7JAb6tmYKmfc0YW8XY5H2zbrqrYMARkTB_sKNOJOaIjzw_lEL3X38EJhvIpGEJ0QKmK-NYqJFhmYsi1MbuoMFO2G8np1XeOKGUh8qOJ3zsEkKDMkiBSSnkRdlhYHZAfWKNpZht5ZqMIagxO0ueExb_lPdFQe33vmAMwTqcLiotxsQOYPk-2h7wdHQcmhnEDbnMuVsll0fLw-KASi5Z2z-ly0U0vG7hEiKGTiknFmjsUns2TcfYGGmEvxENYh46VICILv3MJ5XBmPJsgrbeaVAQendSONM257Ykpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=prUDkgf4R1vvI7sKZ5kNjgwqD8g8HW8v3W5s_gpc_nDjqQ6qvVJPMEYwSsXeQcwsiMbJXNz9Rqd-HNZykubJnm4eM8sl2zTUDDW0F_ruNLF38-ferz6YQJyjrmg-UrlvfAWsRQQLaq3XI0x10qdmhmJzTvVyFOm--XGqNxv1FiZ0krBis5ZprFwk1ztLuw1uffpFjjG1caqOgZBbffrtVoFiQuPMmCqPDn-Kf_Ve8C8DPBvLqDPMLYE8jsP3GcMaEeGNVl8tCyIPJGvUvOE27srgyJKDcLyBcrHtqypViIhqkztymfKrVM_3ZdbcPdPYtjbLWxO0i670RIB-2KAwrxLs1ZGduptAEgSZS1PJ7Ol-XuJid8gLutsA0DWTonzLK0vU3VP7JAb6tmYKmfc0YW8XY5H2zbrqrYMARkTB_sKNOJOaIjzw_lEL3X38EJhvIpGEJ0QKmK-NYqJFhmYsi1MbuoMFO2G8np1XeOKGUh8qOJ3zsEkKDMkiBSSnkRdlhYHZAfWKNpZht5ZqMIagxO0ueExb_lPdFQe33vmAMwTqcLiotxsQOYPk-2h7wdHQcmhnEDbnMuVsll0fLw-KASi5Z2z-ly0U0vG7hEiKGTiknFmjsUns2TcfYGGmEvxENYh46VICILv3MJ5XBmPJsgrbeaVAQendSONM257Ykpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPBOBusssXyc5mei2_xbDUNNTWJTJ2pjfa68zqXrPngHPXAqe03HowmA065NJ2ehM0r1cmtYSPYg_mncsdQBKmIBXh-bcTowl5J58GDWAvqcPtz3TkfPnT5lJl5Uym8Hy-x8kmEgCcZGj8ofhNt0Im_HMdx_Hx0O0QzztGe3HylY164nvxw99_ohKLQxFqacCenIPsSaNun_cOjuoqvme31ncRnBIOVi_3H6atn63tuHDasGnqEJavVe929BpyDo26bkLhJgCnpeabFrWh0e-BrAQkgvy6YzuXNhxbXrqURTm9muuTShpdGoyVc4skt0TdF3DJqz9CIeQYK1DtOAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clWCg5kgwZiX9AeexUrctnEG-ES1iJsc8c3H99r5FZ-LUfD-oKlSgpBaJEqOnyL8P9GgSc_rTpAV9lojU9_1h8EX2LGipQ8opYmCO5LRbstl_PsqRY2W5Nep6da5OqitUC59cwqtaoAYOLYeB5vBK51_Dq2oxPJqWWPw4XWR0t5McGz6N1jmwu_F1l-SldvDoba3oziSG8KahIkaWjeDmrox4_5dqmcCpEaFh-S0qIzOWYfETlBMgxClXUIoR1DcWwrMFj91wQUUb3AyJ5VZm5YNUVIj5bC7QhLnNkYdsjFLJsiRvkMmRXti5q0OsMks6FgeflxLZ-lj__zNhSqI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enX3mKYzNsSTasRWQML7QvLeih7cOywQW003zfE1RU9psgzuOUAmuulAYCvclbNcnP_AqZ-eIDXUjbxzn2Vcdw6MuzlXREbTjCLJMLF-IMRMm4ZE9WEOCDzegwbAesQdxTkSss7KFviHH0Vn_1S-rCeG4ehpMU0DSrlxg-M3KPycS1oOFovu1DBNMnBCF6SkI4IRmNMmTTcpR3ulC_VJdgeEjgpGr3Hi9Lk_oN8RfCcbpuJaBD2C5t2vAXDyhnVrjjVC46GuTu3bYnpaVTvDVWP1XYNHwtdB6ys0kU3NEgnhgIAU7815bbeMzaNO4yQ8wbKgbbvvhyKlfagoXxyNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukHelOWMOXZ18tpNmGmf1osEL3_IQqyhuph9G3HhPSvjIrT6s1V6W0GM23FqPf3UjJ4c9rAs3c-c8HcpAaN8YvjoiZhxsPf2e9jdtwj6ptU8jrTyr0XWTDFgwU8-t7HrbzmwCqOgXtmXs5GBTEhaVSHIOHaVb_TxBPyijx6deGwp9zgSYKsBLFZJRFsSJXB-qvABdwgIVyu1NuQKgNVNj-ENzy-Hf1Hcb2Joh9SHyxCnUAnsMQYUOTnC_lmQGGvhRnbFYfIXTSUco85qvpY-7HL6Z4ihlL7gkGDH5eG4NznlU6bECss2SaPb67tfA15fwaO81Z_AEY4SlFiLuKpEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGrdKKdH2iy4cG4AGoCtFmwY90KKabxs6qOLQ2eGtRO_ZyEfZVc2Ntt_bq9UNtEYFMwmh72reITysLGzaEg4kptIp3puf2G-m9JE6jTZ110I1zk7rJDVfC6ukW7nrZ8mS1HLIFaCGaUCpSNH7R5r3kZhfIibNt2_FCDM46biNJNH2vFye1Z2Jq58nn5-o_u8FbuFotrIR8Icp1gxcU4V7dECGird9HublEPKkeyk1n-fTdBmfxXebt7qRVAW4WMUudEGvs5XsptBdlj_N23j6GFiwJ5lTVrgS9iEwMy-4_yi3Px-PPcsdulD5Wu5s2Tvp3_YLpll-psgM8NaEur42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=FNr64dXVtS5ZrWvzWmwY2LJ1OcWMFvEF2XDrpr8nWiFSgdlNZbZPIhynPHmRTO2B8ezTa1uOERtwWBimPtXSO0IEoRrDuoKv5NnCFA5VVwvyGrJIqT33WWvR2--oDDs9sd5bgNwNEUoGfs_MdgLKxkwvQ9LkDAm5kZZuq4g98UyrJ_4ZtReQpy726Sxcz0BFo9kNCGme8tldbVAZgaR99i4CzvkGzr00OQZ1d5AiWYvyQ_tM1RRUpGIr7i3Fn75DI5ZNOhRdKiYTF1paBYnu2xlTTjWLvjUS4vKuCcSepzJWEfQzk8nhloZqMQcLh96ipvN66GMKiVEmCXSelf9Mcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=FNr64dXVtS5ZrWvzWmwY2LJ1OcWMFvEF2XDrpr8nWiFSgdlNZbZPIhynPHmRTO2B8ezTa1uOERtwWBimPtXSO0IEoRrDuoKv5NnCFA5VVwvyGrJIqT33WWvR2--oDDs9sd5bgNwNEUoGfs_MdgLKxkwvQ9LkDAm5kZZuq4g98UyrJ_4ZtReQpy726Sxcz0BFo9kNCGme8tldbVAZgaR99i4CzvkGzr00OQZ1d5AiWYvyQ_tM1RRUpGIr7i3Fn75DI5ZNOhRdKiYTF1paBYnu2xlTTjWLvjUS4vKuCcSepzJWEfQzk8nhloZqMQcLh96ipvN66GMKiVEmCXSelf9Mcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkv1PKAhIGyAWctmXDjpzSnh8UidxD3QdAljsnuwtVQL7b6NEvn2Me8uFuMTlH6k0SclEBqyp_MOUONKn5WnfM-y7LYdDMT7lTjIcmmdpAeq-bgrRQoGS6tk5uZJ9TMLb4nwYyi0kRSsr0jVUhcP8o3vN87eoh-yPKALXVZZ40s7l8S9ITUN5YmcM1puLbAbR8MzmUeMhGMYs4ckHQDdGEMdPS8EtjtB3AHKC0jOcHUK0EEvAUC13FslFzIQo01bPQIEiaNgrb6z0iA5vbUntqpj5ekGMd6LIMizCUmnSSXQdiEar1shNKJx6Ka36WUvCA9fbZhpi6Llza8r4g0-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=VLWo2LZMI3EppHprEuIpqiM2hXxqlkTGn0OvvUwaMHNxOgTFJjcYrKGjceuzmVtCruSo-M26nJT960ScJKg7pNJWhdp5GUk8J8D4aRARt9dFVMh_IbhiRQcn4GIm6Uaxiy42F2hJiYuZ3lcR9RITLA8Ee_APxHZzCv3r2J6_zL-dGd8jdVYempVc-EpDlxPPxE9FjXZWWo4eeUYR7CWpiJj6XqWCZPpShVcryJ6dM93OeXFqgNl0ihr9k2Nx_ZDqeXwnyxN3Tiv_q5v3Y7E70QiGHpsbOVZ7A7Z_CNaXFlJvS7KEjyd5JP7iHVXpTW9TRwcKQrDMKouLHN6Iv0Jg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=VLWo2LZMI3EppHprEuIpqiM2hXxqlkTGn0OvvUwaMHNxOgTFJjcYrKGjceuzmVtCruSo-M26nJT960ScJKg7pNJWhdp5GUk8J8D4aRARt9dFVMh_IbhiRQcn4GIm6Uaxiy42F2hJiYuZ3lcR9RITLA8Ee_APxHZzCv3r2J6_zL-dGd8jdVYempVc-EpDlxPPxE9FjXZWWo4eeUYR7CWpiJj6XqWCZPpShVcryJ6dM93OeXFqgNl0ihr9k2Nx_ZDqeXwnyxN3Tiv_q5v3Y7E70QiGHpsbOVZ7A7Z_CNaXFlJvS7KEjyd5JP7iHVXpTW9TRwcKQrDMKouLHN6Iv0Jg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnvdOkkvDV3UgcxReRstoHpznzzFPaYwwv9vSzubLwqzdCV7qO93zCWAqoOO9x31jPC3gSDnK19rb_ZqQAewHBK3n8xv-VEQi2vco0GKSef8qpNp4X8DJFHLu_B-5M18n6dsxGrrR8KfEKeFEy_92YRc7ZXH-I65CkHx4TnDQX3qL6zMVGcu46yvWgtJ33eB55PJoD8ewnxV_dMxDdDNguK2QwIj9ES64_56X0kh3wkk-L8fkFQQYfUkj8F1L6XVZnI_VlaXujETQwMhZY3kiRRugm3veAPZQg-Wegc2uR31aZj-zLfjyXJ0VGO0a91LhRC3nTh0TMHCRFJ8WXAkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4P4_En8Mg02cQfKAHxzXKJ4cKl7gvJr39a5ep-nbORAKd6RpzUEl5nUjOpsPPHCmKdTzqmfJtlITpTHJxyIplykYw5dlZfqHQIT-pTi5Inb85p4npPiKYQZAFE_n-9dxNry10yFvwWZzaPnuP3qYx4PW4UpHk084BRHQte7agZgpqJckZiolYmw5h7RCmqAURw5BJNvjtepTrrt2cAp1URUe-8SdwuwDdut6Xt2lNsOfbhX1eJaPeemAZqoJGGVCO5cs_p0LVbwNI1JmX2cC2EqdcKL7fYYG2T0dQWBNrAmcPZAHoad8e-C8cZY39S9sARNsVHi-7PNchWv-hez0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_pHFa0goHSb2rC_0sG2TkSD5dxj0Re_1e59mh2HytrVho7HPBgxrljc1c16TTq1mqHP2N_E261l6xH2z4wyJ-SZjzCQa-dSS112HX6BDluI8rxafGEe2A3UcD-SAjfQGB64TJLoeodlkoPJt_gkY8zGegXBDAz21ndG3xZiFJZ_KdRZC-QAz1gxtCK4swK7jeGMKdPJTiQ7xYarIeP2WpuYkgx8jXlOvcqoxy5E38asI9fIcSXp2TM2gAIsnnVSg2WRBkooFaUS8TfMqJVK6jFfHbFEwwemiMMGFgStX2tXM3vZOyiBoXlb158QdNkM2GgE-zCj8qbbLtwrefsM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3kj4F3rblJDOk_F5TW8zElLknYI2uQfyLx1jyjrV-DJHwT_Px23bQEepybYf57Bw66-LzpSP9siX-Q1PatTfB2zhUIgChAO6FUOXA44QscHY-u-qCGCgKheiADUjkTu2loTlSz10Rb5jbrXb3X7VWCAAUOQKPDPzzS5iXsdOWufDmMdYvj8ClkAqSl8PgDqlB9xgwY8GXCFI2QE6lWDzZAGgqRnNXPiRY7rjTqm0mj3mLAM96bzwgRBjqhYShePMcU6x1vAqgPZV2_cBold7Tp_LmeMahkKtCAhBo5-DAl76nuxgvfKx1xcKYJ9y2kB2gW0zDITedU_NBz7VApQAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvnRDdtW4YcPevxWcsmEThnpInVCB5pr-Ol7AbHXEI5jJxOkpf8TV80E7cdAF_MYLqce8kieOzSRN1CE8l9hPN3qtbPec6a_Dyr_NrhQpv-_TmzLD0bbIFFsjBEkR9xxF1FZjjZNfTELCCW0EYFsZFQuT2xJkAlyFCggst_WMlz1Wnos2yt_Drm7mCn8ShYT8dcdkdDJCiDfVHRhruMruph-Q8rlLQhnN8JimMClQmxZfhZyJAmHZFWdM0Xrc7LKxz29YcxhHsYV41RioZ-Jh3HZbMlHkCoOvT48Y_gSX6KO36jlTQ2xDgBsfRSkfgJ7-uyuWhpwll2ahhjgO5P0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=uM2gQZWksdL5pmgz7kkIucBAswglhIRIp2tH8fBbzF1GFHTzUAWPYuPBXVO5_-NCjpKoBcLLJr51yVJswPSCfvlG0EmNlLkxU68C9IDtiSRSbVsj-uilkEhcPGi_ZnoDbrTbvB2VUqlDjCxCZWBMAO7VHswcQHYsE1CY9HiPNLznRRfAej3SvT7sziSgGCjjtuusVGy__FFwxZA48_xoJpoMVXr-U-Z3q5sXI-965hRD4qg1jtXNhZdKIsESrFegQV6k4ie8898ca_xvPYeNt2silMENRyCmRY35XaB8JqTCOGXfJCPem1Tbi-Jz_QAyY1-hKCY2HOM-t4rslJIdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=uM2gQZWksdL5pmgz7kkIucBAswglhIRIp2tH8fBbzF1GFHTzUAWPYuPBXVO5_-NCjpKoBcLLJr51yVJswPSCfvlG0EmNlLkxU68C9IDtiSRSbVsj-uilkEhcPGi_ZnoDbrTbvB2VUqlDjCxCZWBMAO7VHswcQHYsE1CY9HiPNLznRRfAej3SvT7sziSgGCjjtuusVGy__FFwxZA48_xoJpoMVXr-U-Z3q5sXI-965hRD4qg1jtXNhZdKIsESrFegQV6k4ie8898ca_xvPYeNt2silMENRyCmRY35XaB8JqTCOGXfJCPem1Tbi-Jz_QAyY1-hKCY2HOM-t4rslJIdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC6lWw8Eo7G98oDxhagP8tf0v1l5OebmRNJ47IToIPiNNZMG47X_jjaGQFicqvuWFrnisDp2ldmPXo6EAYMgDqI-rrS6Cxu15Sd6UN4leP5MM2LJVEgxyTtqqqaJTsHV1wIfuc2bauH7F3xDNlcheYA3mhjhHluph0cdqexfPmjZHKifN1TtQLnYkd5WcFlrnbMvFALLEBUnFFJ21_jQ7wLjTLa-girf1uvbgQ_g-OyBb1GRMd_idf1e1ubL7cObHy-tVz6HGNSV67BFzjO3f6x48YWtP0g24ifpZUTdssSySTHFSfP_QG8z3AHbQXTNEGdpE6cgOempzYo4mgskWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj81NKfenYlLOwDEM9YmBU0idyP6yUekVdPTDqHNlTJ3y5MQ4DP3wy6pYDh-eKTVxekbOnCqylyVD3O4gsiq7_CI-AbBnaMsg0aFJ645WZB2ZMotFD80y9HfLA0NdU556cWBqHwBe8V4TACvnZczqkkg70FRmrc9DctkmpXdf53mySd1NaxLrikGor0mpJtgbPmmbhylXBW8pGwaY1N8WvRaa7ng_tIsTRtzJm27lvqIGIpaiUaY7JCqAA335cKgxLE_gJBM6em5YabsUwEmBUo9QQOhLHSjysfqkbEe-tqnvV2GIHWCBNcYcCLYscI3WlGs935Le9hubGRVFvn5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT4xllOFyLoaR6HwvzI_L5d8SwpNkHUSR8_uKsQgUz0In12vdr-FMjLScR9XD2gmaY1bquhGrjBP6B6jDL2XjfYT_zmvHMMWnJMBKGPLyf1UBLdUR1n4Vztx9nSYlENepNOtylcaNiQAJYpmxdmRMqqhyCncSkx8a-tXuvRB5XWPD_rvtyL-Sr1x-qIL7DDvH5U8JpZRsdA3WwZM_-nBTtMWpDO_rAomPRlu1LkecirDFdcSrHQmsj8XBMWpcGYE6mnLLbMTbvwsf_VMKrvspTHb0MBsqNXTWqwmtGDxgG1oHmTZ1FfBEkDsYKnlXerxiCg4LRVJ7rB1g19z9Mp9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=pm2mKRLFTzycADU2j7xUxDTaIAZbavqfAV_cgxQqCVeK7IujsY7BfLPbTiFxA-NjW0wOQIlRUAagZqccKSFKdRXRNXVROXMyo2PJCAmG8MlKcTzSdXpNLuFu_M5idR_24nqUukiWVVfFK-GAlsKGhRWhpyrL_yDOJIvqe7sZ16IPVd0IooBHOk2W4C4_ie_jzYgQ1HjoF-D05XxxAZPsF8912O9SU8PCCfUNMRvp-vS1yq-jBM1glRaQS74t86VdmVUr8HQAgj3PH1MXvYWMPo3hBc0IzWMfBUbbD7P88_xtQvRzodXGbKRSgrld3DGufTy9xjTNfSoIZjaqGsxrWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=pm2mKRLFTzycADU2j7xUxDTaIAZbavqfAV_cgxQqCVeK7IujsY7BfLPbTiFxA-NjW0wOQIlRUAagZqccKSFKdRXRNXVROXMyo2PJCAmG8MlKcTzSdXpNLuFu_M5idR_24nqUukiWVVfFK-GAlsKGhRWhpyrL_yDOJIvqe7sZ16IPVd0IooBHOk2W4C4_ie_jzYgQ1HjoF-D05XxxAZPsF8912O9SU8PCCfUNMRvp-vS1yq-jBM1glRaQS74t86VdmVUr8HQAgj3PH1MXvYWMPo3hBc0IzWMfBUbbD7P88_xtQvRzodXGbKRSgrld3DGufTy9xjTNfSoIZjaqGsxrWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ycyqm6BMVfvYqjEEQobpvgMb5k790lnKQluXoXIhv-3ZF-SBhXqboFcePsBWtF1yjhmEaqeCTPYwOVIaUcTv01v1Eggf-sEpnviG0JPAX0irFgYo9tzhamX_lXY0v6xe4jgwrF2UDtguv6czqHC4fbCtBKIufQ_wz0iTejVchVMlSDnOSpiQI0ibDg5Fp7eM86bLqyQWe9jZ4wLkRvPuLX0YcdmHmAco2mUD22Z1BjBJl9FcSUpNUOxLCPC_VnH1tsHSa1tNHK5eTMEVelSfjMNTHdtleISnGiWGqZgRsay2TXpib5pO_oysP4ERs5uUrqq1i9XrT8n1gg_9dcwtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReY89-3LatQGuNYB5ECf1TJV3mvQslEcYOBVmf4E01CdgT7u_pejcx-zA_MApgLSRqop-UZJbNEJShQovWqMAwrnXDTaSY_Xg9v_O2_7_H_ik6QDpUzrahIc-Dr8A5d-W3xonZE_IiHf3kh1AGCIL2FH32K5NFOqybhTpAIijsepY1rwrK5yxyACE9W-2t9iZxaeJAQKT5OXLo2RnuFUy68akOtcLKDll-slC9NktTKc6lYpFckupxCziaBa0aKr8bFrWo1g3ZtCN8o5k0_lpbIqHKcelWgq4Drcplm5F5l2iFQUJP3xlBomklo1HOQK14eUUxxQIpwS6D-kpnOG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmbbOscL1w0zdOpAPGRCmZdGi7sXDFcp4H2-ayGtI1IIB_F_KCZw6ORifWyyf8qyL2SrYsbdTqXZGnMsoVcGRlcna7KD8ZIf8flB0Ww2cWeT_OGSDDGbNTArL3oJ2y-eoWyh8R_I8remSVGRl6lrSJBrsFc5Fk_3YX2xVaOFc5dEf0V-inClIl2MN8KxWYlXaKWUscsEELd2e3VNeS9QQFmENqbp_N0O_lpWDk0bNosASkybCBk_8RgiKoQlJF2g51tju0MZJjleVkrEO4YFqJxtDEi94sfOAQlM2QqpWNwMl879aeDU4uknL3m3GOVKBJJWfE4xX7MSrjDl7G7-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otKCC5NcMDDbSGB6q6U4yOCEm3zHGcDlAkSZvkYqmqydVCpMWHU3NQrtiTOT2EYSjskLCDsaZ4k-QfOVgIYY4fhFBsAQLpcZkBYDkyK-EqYACFz3W9OFrngvgOugBVjOm-Q7i_w9qBr0KhUj15FJhuZP044lQSGxuEkej69e83gQo9cdU_N87hQqyZq_G7tVGiFgFuLmuMwHiSBCpFfMlGciP0aIArcA6BO6-HLiOlLfHIZ617WNPp-VG4rPNpHV2a9MxiWElX3u0Wy0Dt4NvAN_iDFbUO-CuiqFB22Jg7hm1Mv1faWH07Z1GmIOdwa6yNKFX2oyb-i5yfre0iF2KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYsStT69joJEnw4z4mlEhYaAp_zJNCK71kBj4-gREE-tq5DghEziYt_p-ITY6g6HgQ7aR1Dw8-sEmokJzVNQZUoXwy8IFVKxJd9gWvvBDxrOz-euw_GMCQ5N8mCZq7PY4pz7ddLiM9NQ_Rh5xUWmikVq3ufjZ7b6Od6-2XUjgCPqed-8uSAKufvBdYQss167ZJk2f86HqFXaRY7b77-_ZUJVrlIxx9prj0nQhtbXie0IjwVpdc9NdXFXM06p1YBFHP0ndrZaGn6VKr7P1bcHdWoJDUO92j7oeWgCRun9q3mu2GdOEUsMdNTMBOIltWByfN5AKgObH2o4XWbSjKKvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
