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
<img src="https://cdn4.telesco.pe/file/USd_8-UIpPPpVpem14L9t5-iSahJGCZDavATvbt_4nilAPK9Ic8zknyqgXad9l3I2qfDWZyNjEAau8i_iBi2vG3-QXIH9ljNjs7P59YEnlgC287O264pJm2NcmWfZyiAs_7RPw5HWoJENHXlhEl55Cq_MnBDReQ2xMS3NmctOPSMJHzde5grz9S3KdoSlp5ztkhRccZgjN5ytpJhf2viHiplGLz7dVuFBQILs0Y55DsRFZHChVD4R9HIBLfsRw5i-Q5XgwkCmR91fkDXEVLlJYStkvHyABO1IPw46rQoKeQIAjQeIDjOfIfRozGzTojSO6JxlYbxmC5Q2o5ckYAUDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJhPQDmkJLTlJpw6ja_zEZrEJd56ME-NkYkGZBoa9R0wbPGVCLnazAHwy-K8LUil6pDDdPgSsH48JpuylotF6bmjDrJxOOpQD1CQgElvjQAR4nxJbv8OSpEGHrreXhIrM6H97Ig17Nt-xpB64rGmYj9HQ53cU-fGDKS1cpnVfswQmu5lvKiDeJEtssKN4elISDwO4ITtE_M6LSdiGRbsg0hgp-URwUNt_D_pU1XFqS8T7FA15b9lRv7yBs-KJWaAXDOS1lIEb7CULvjs6UddmpF6YmVx12lmmum2lUSKxjex_PHoRmLFWtCWyXUpz4KYp-wJ_l7vQ7PAkUsJoriPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jut8cQceE433CeJXf-9_g1_bIv0qU6giDxbpJgJVvXJbKl7UTJPo-DfH5AxDhgKeG_G32gnB-Oziab_FB9LLyGLQMIVS77wMRSQBI1wvzoX3BwIcePIUNbjDYY-UlaEM3ZhFPMfLav9CpFHj0jAeCM5I2xPghcSwhUmha0tou9OuhRGZxtVGlJjPxOhkyHKTe-2-SJqZp_WK1Oknw83qfab6U8WDLQ62SgFrrbOMRB6RNfQGFzLlplSfHIN6yM1kGCZld7aey4a9kMhapREtb2FIiWBrOX_y-Xv5KEvhkQLMzLb3EULX4PA3K__lFA16otma-1v99gtygWBggTGeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6bpaBhOneVqI4HAkwRI-n4FmRNhSz5954foGCsGClRm5ldPNG_Y0VVx8NxSvl8jqIkKjtV0aNQ9gmyWeIg_Zg8I2Xsk-sVGj5eVUv7yBGfiT3ouwFd6PDrDice1397dgubbvOTPktnVliKyLVkzhhlXzGWrJCqtCpmhf33P_3RVm5az2yGYtRipgD-AXFI491fnACJKYMAGe35SLKdoWXgjIzHNICWy63w580RNeasTSnDd218RWxRBLTzg4XL-wgTESVKJkctWumhAzDFoEeAtQDMJyjnxy0vbB-kKBFW7TAoQ64Wxgan22HGAZ9I5uXQOR47486KiG_lhVBZBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Utev5yPOd-ooKzNstrUIc-ybcjSVSKLbqLtxIVNTXGsCaTykpa6pjGrUJnzmI0HmrtPRVPFmtT-RH-9OKU2XXh5WhM8vF76AZj6IcPL1pswXHJVigtuDV-oGucR-3x5ua5V0HeYf9UOnmDYEOGtkyqLXHMTQqv5A5mmPE5g3aGaZ9na90F8Il3WXM_3o9rdyzQoWwyy4EAgxK1E8WYtpBZha_Qn9mt85M7bK9_9GUYjfYqj4g9YvYNQb0koTegOVZKap0IhVSVnzFVk3dhc5f8G8MiNEZ1prBkF5gGE1tfazxQ9VVYXmWVPbTmnAony5TXG8FtmcMRGtqgI8xA99iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Utev5yPOd-ooKzNstrUIc-ybcjSVSKLbqLtxIVNTXGsCaTykpa6pjGrUJnzmI0HmrtPRVPFmtT-RH-9OKU2XXh5WhM8vF76AZj6IcPL1pswXHJVigtuDV-oGucR-3x5ua5V0HeYf9UOnmDYEOGtkyqLXHMTQqv5A5mmPE5g3aGaZ9na90F8Il3WXM_3o9rdyzQoWwyy4EAgxK1E8WYtpBZha_Qn9mt85M7bK9_9GUYjfYqj4g9YvYNQb0koTegOVZKap0IhVSVnzFVk3dhc5f8G8MiNEZ1prBkF5gGE1tfazxQ9VVYXmWVPbTmnAony5TXG8FtmcMRGtqgI8xA99iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJrw3ChXN3NCI9-ptnOcieOxVzrDApaY8cG7XHGcX80bifNNc1oCbcpsNtBAYT8WSZJguD_If1bchEoAANRUiNdgTxjjtR2nu0WusDDWjaMRRyLdKW67MQZWoaZLYlBlpB6nAxGRNCK_7buokA5LxL3ZN4aGItZS6f4CMC8Gocno_cBnr04eyi8fU--e-49hMdCXGQPfPXkiO1cShOcoO7SKLRsNKo0EIqUxdhpUkb7M5l4uVjxB6h6nVlNEJEsPnxH7WhiQnXryCGshjY4sVqJ-CNadxLGowYOQB-Q6o9slsVHWI8PeDX0ALzltigpjvOuytS72-_aAvocI0vuKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=o7RDNwvFmdYZrRGjOpkQzbbnBivxeLOaVO-Gmk2wvZ3kXkgXMVuDtfeMy1Wou6h5I4xYsUBQ3AcEuOYvKh1SOsXT_N4O0ef17qClQQcm_rkFIcKRKKQo5Ti_Jzk9OUxwGtLiTqyOrmEE9jse07Vah4UhLphUZGr4GOGQ-29VhI_gZ0uiJMouRn97zpQesbjTQWyyGue9aH6cAKTd5G3kGlkulBMsbpf27Qi6xUriu5AXbZb787XvjXFiV2qWRAMF8Tpkpa1W80pSssye648iv1f_QWglV6wyxQAaPcPzN1SkKk9SEBDidDwoQd77zjy5zTsuVQVkMavdP2A9kv0kZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=o7RDNwvFmdYZrRGjOpkQzbbnBivxeLOaVO-Gmk2wvZ3kXkgXMVuDtfeMy1Wou6h5I4xYsUBQ3AcEuOYvKh1SOsXT_N4O0ef17qClQQcm_rkFIcKRKKQo5Ti_Jzk9OUxwGtLiTqyOrmEE9jse07Vah4UhLphUZGr4GOGQ-29VhI_gZ0uiJMouRn97zpQesbjTQWyyGue9aH6cAKTd5G3kGlkulBMsbpf27Qi6xUriu5AXbZb787XvjXFiV2qWRAMF8Tpkpa1W80pSssye648iv1f_QWglV6wyxQAaPcPzN1SkKk9SEBDidDwoQd77zjy5zTsuVQVkMavdP2A9kv0kZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=RTNDBWC0yKp9Xmlwm4b4vLd2NHUzqGn-1-QPWX50DM4lPqlWlzlZ26t-WIUCYhw9ryFwel9ZbM8dOxPRZDcQ_BMHPXsvvf5IgYg6vJWWRb5rI6s3yhLMzfxRz7UK901g1she6cvV77_d3qtKukQvoGzga7rkxd7Oec2DH72o1CmD7e87JjwIyqn-nDvrsBm3PpfTLfeXEbnmYVTa7lKFzA4zLk3Rz9qY55GWM2Id6COZfJFWi4v305mJRAiINZ2P1Wv3YS7l9IoTt6NED7Qwuw_i8hnKiAp3CMCIKYUoFGsCjj7y0jINnYf1QQv5VppQzVwo5cK_bMvbpkIDczMpzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=RTNDBWC0yKp9Xmlwm4b4vLd2NHUzqGn-1-QPWX50DM4lPqlWlzlZ26t-WIUCYhw9ryFwel9ZbM8dOxPRZDcQ_BMHPXsvvf5IgYg6vJWWRb5rI6s3yhLMzfxRz7UK901g1she6cvV77_d3qtKukQvoGzga7rkxd7Oec2DH72o1CmD7e87JjwIyqn-nDvrsBm3PpfTLfeXEbnmYVTa7lKFzA4zLk3Rz9qY55GWM2Id6COZfJFWi4v305mJRAiINZ2P1Wv3YS7l9IoTt6NED7Qwuw_i8hnKiAp3CMCIKYUoFGsCjj7y0jINnYf1QQv5VppQzVwo5cK_bMvbpkIDczMpzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuTDlbgGpbwRiuf-hUkz5KfhFJS77iagNFCpNB2U4huvH7cBG3IJdxqXy-f9yffakqUOffMOLpFL0UyDfS_8T7srYl-dpNwWHeBoZF--T2vzs0Mj9HfN4P22TKu6udj6zxeIcnhalZyPMdch1pi37Z5PR42qa4VEbo84deSdtMk4u_ykvxjNhFGv0M7K1yGPJvcpVfOG-D6vX--SPQzocEFueIX0YhsPCebxumoUWKRoMxBsfZCskgUCNXqB_gVqSPpntOaVvFPvVEvfaZCHBPUDqmTwguxBRWF01lsuS6veIxo7PbPfFY5TwXNHcyBFlovoFt-ZcTnk8ywuUp5H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFr5ONdNu97a-uoe99F78p-BssPmUgJ2ToTSQvGN9xAh7vprF1oItUgsj_Ld1S6HYoeqT3-pUTNn-hfI8W1UelWApj4Mr8uRn18Jr81pwDmWGnYO--srUtSrxzMLIoFZIsIjEB-X3EqEugbCHCPBkequciGUbyMYEMfWaQQlTAGybFahWpBqpF2igrVkdGdzNvx1CO5ZapMOvxPsAHyywTf8y_0t2p6lKN3o63gPgoVw9Vw3MEvMix7ZXcOLcA30J2nYkPXWaLhQemHP3PP_WboEsbBIu_K1nSkxC_V4xViua4X7ulCkTJCfVvFE_p3QKo7yCKEAL0pk5GcrvVE69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu6ifF0nfZkqs5z2xbQJ0PI5ROP1FQlvlB5QHOvbXcl9h6WG3FR0xS9yOEJtMCvnZo_DVw4Kip_ZAU3MCdwuheIJTVhqCy-qEWWiLQcCiyce8TATL_NE5PLL1WbXXNze83bUeq8SydxgGas80QZRykru7VqerlyEPlBC7NLGzbBjbCxgoV-1WXbe4zi6L1SFKHpjYdjkG5DVD8Rn1irTZaRtz9vG5MHn8OvsOP3wJ6N6haPOaZh4h_7UfV_NKSmIBz5E9cYglGWrL-tBf5nnmP1n1MQuRkpJVYtbmqIo9Uo2Bu6F-0djHl3VTyMeJwWgssciPx4yKmQDzeLNS-n1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP6lO-y2hirmHzcnjGLHoSKBLiV9MB-KarTypc-7iwvOiEEBdr7OBsQ0gKKRM9keBMLZ-YK4J7wdd1_nSevgxzbnF-BfDb8lpcJ-nR2G4IwwHkERuWsJsi5R1o6yRYiN1Ox6lw9aWYjJypKSZJ4zDAZseYzm2P0p4Mv73mEKIChqm3Jnhj-C036MNToRZIkELUZw6z7K20dvPe83ttS7oB55KlWLyty-FmhqSx2s3-qwuo5ZvjS_y__1fUkPxSYDEgq0agFEL6PoEF_9WGzX2Js4BTU4u_uPeFTt_8NKQ2KwqlC9hG4sb4SeCI1umcA7Hh6qN-YEApLvDSkMKHp1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBENYvy1whp4V74uNVeGf6UPZEkcwo8e6AAqGWz8v7KAbgdFoxlJ8cedDuDTQZAiDnllpnzs_P4qr843ERL5ZhYeYrmIdv8Jim-UWHQlDKQEQru1dRVD5kDsupB6SHbE9lSrRloi5-7w38V1bIQSqv7axLAjYauJNawfkj7JtvvGtgwtxxVXPlUArn3OOv5UZkYTIvsPMn9b3bP1nw7FnCpDc4z-8hyKIXdw8ufmFXh0ChdyLQE99rWNM_bvHTOlxHi3BNaL8tVmoLekPI6fcQ9jTsZ01JbBKKghNW7apWvdDTf350kUmK7ArfrdePwfkOKHjmSmrUHdBw8kw65aJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZf3T9JDly_ojLe_IUzZukA3H1zcy5t02q3ocsYi9Jr9pPWeIR6MNIPbWyFtwBravecGeN8pIM13bMlwaa17-CnrZgKSFAqGnPRDOtFuewL7-m4uBCHblu1ZnETNfaFYPtpD4VWhnHo7jIn6ObFXmFaXHaPE6pCWsOXEvE9Hddth-f4apY78sIRIzXVM763_drQlraJBBuMrjpfIBg6Ao6HyyE_kQke7WzP1TuiUAHMyhlAZKVGL4-Tu8db7lmoWMSWydMkvZE_T0q8_5U0qIKFrRJXirVEyfeqenKeJ94BGJko6pr_-VA4ZbUr5jjaMRSTsqGjH52DmEYtFl1WYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRsfb6W185klI27jQluMRKm-ngPa2iI9XCow-Jm5Ty5ANceCGTuoBPCbq5qcIQCk7DGOVwHPN4N61VcAsTpYGZRP6_ByjtwlZkPvBIEtHVzJRdq-oBpLXNrfjZLpF5pY40lU3g6-Zw-ExwWohGg_z2QQnXhmcMthaFqMrX6d3RfhM43e9ryTUfpm7q3Tm9-lSLCbOJG81vykWeSTjo2DVD4OPr3CdpXGPo4XD65QmI0rkIWL9mgSriFGKXvlFI5FjVultwvkO5BD5Fqs0r5yfhvtv38YxN9f8SWr9V3x4MeFQmLelctkiV-VrNXTnDC3E6VG-aClNo1Ye8sKJ4y3zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbJd1f0fb5Ru8XSoygsni5oF1kT3LVeKI4woe3kJyS3Bwi1ipwzGdiwoqnGl5iLlV75SRBt3UlsHLBMGHHmzwzkLE7z0YXzeW9OMcnuNdvO-ZeWigQC62lt6l29Jd3H_HTQEAgYo-l9qj_0pRlvqHR59m6w9idgCqoxDSrxJnMXPIdRrlmqLdfuqSeHKJhZwWedFRzPoP-42OTMos3xlq4BVZEbLYsWhpu4Bd_5SvoVgSEnbopk-NBl_r3OFj3TcDGX3-bjINTsZxNx4MT1lDTdApvxisM0nnbwNRnAs4HDY4REo7wkBj7FViS0cF4PTyuuB2KnaQO9Amm8s5XDALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wedq_aIOohFqd4eubgGHxoZhGIR-RnoubRgOADxg2bindcNCf87BfvPsDygj7foqRGPZsuLzr1GzgVOQ24QtMUsnclLQLxaqHYGdXCnBN-GH5zTogAwixpavBz2WBftBE5F499zaD52OIQl1nwIsHxF-7poSd8Bo2NjM7scJR4fHOCx43JBzwFjaXnDoVAa3a4vOSCypmYAqfL6dj3NPnqbBHHhomLPh3kuX7Nty-v3tI-Km3H-fbXGbBP2VnPQ2p4fZbfUv_NONempoe9LYzoxKj024kIpxCE_8O8KTUaCrvrnHVzipWSoywYDa931H_QFMtePII0CgAErKpYEp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=HQcTAQKVcHM1D5ahfi2iA3-sr6OiJ3X9V7oW_UMF5pZqGCvzl4Ju3VgVy7qfDoVs1Xm3q43DSNFnCTh-ycAXd8Bm-xun9ETWzp8nGqtvS1F2Me6SpCdKC-w_I7V0FT7xqCF1v4FZhM-Ypa05XKDdSeO6f0Tj8FJ4Swb_cumt9-_UGMar2k5d1Y9YZ38s93U58prNv9pIV0mLmTRqqC-_eo2IKE9_vPuBFGAXt9BRiDwCGe6fYiveFZZxUGqKbLsM-qtGD-W1gCEbaUEWgytt14vaQy0rWP25pwc8AsqoyW67dstBPoebSXrH32oxufiEtxjHmOWwi_oe32SapDA1dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=HQcTAQKVcHM1D5ahfi2iA3-sr6OiJ3X9V7oW_UMF5pZqGCvzl4Ju3VgVy7qfDoVs1Xm3q43DSNFnCTh-ycAXd8Bm-xun9ETWzp8nGqtvS1F2Me6SpCdKC-w_I7V0FT7xqCF1v4FZhM-Ypa05XKDdSeO6f0Tj8FJ4Swb_cumt9-_UGMar2k5d1Y9YZ38s93U58prNv9pIV0mLmTRqqC-_eo2IKE9_vPuBFGAXt9BRiDwCGe6fYiveFZZxUGqKbLsM-qtGD-W1gCEbaUEWgytt14vaQy0rWP25pwc8AsqoyW67dstBPoebSXrH32oxufiEtxjHmOWwi_oe32SapDA1dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=pFxeHE9MmEH-Kq_vJqTiQRtoxhkiRGFZ_RjqGc_P_pspiz3clgcoT0MDvC2tpHouaym-17H1oLYf_kRLLsvzWQNUMs-kRn3KaFw5H8Ni_vCCKL-f31JE7ZLEnGv3f6gjiF9xFWpq-6Fk9DREtNLeL5K8VBK5sArNFjit5gwTK3sLLOWiO0kmUcU8Mzd79YW5BKzj9PJ3AU59lemA-D8xyN8ymVbCHHyvUOlOkoivNHQF2RNR-oxHlrlNsvFm8IQdumhk-ljDeE4jE5ZCG3xrVfN-hE4pglxc254AYQztVST1D9o5ocHddK-ippIGs2G3nCsVT6tqxDzhyQDAT5gv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=pFxeHE9MmEH-Kq_vJqTiQRtoxhkiRGFZ_RjqGc_P_pspiz3clgcoT0MDvC2tpHouaym-17H1oLYf_kRLLsvzWQNUMs-kRn3KaFw5H8Ni_vCCKL-f31JE7ZLEnGv3f6gjiF9xFWpq-6Fk9DREtNLeL5K8VBK5sArNFjit5gwTK3sLLOWiO0kmUcU8Mzd79YW5BKzj9PJ3AU59lemA-D8xyN8ymVbCHHyvUOlOkoivNHQF2RNR-oxHlrlNsvFm8IQdumhk-ljDeE4jE5ZCG3xrVfN-hE4pglxc254AYQztVST1D9o5ocHddK-ippIGs2G3nCsVT6tqxDzhyQDAT5gv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=RhT_clu9rP8CW866m2YOhFAtoU-qBfRRYxPfChAKKTIcRaOYc1evydFtQZKmLdbIX1XTWKdr8fPjo_1Hzo5snVoq-PVkQXBfOXCuaRFi2Lolx-EmKfmmnkozcaLrLx14dsgdKYjFfQh-DPrIceePEtPm7PeYs3IoDDtG4T-__sr25J4WKsrx2DepTzltvFWhUbCVDAQCZkLJGHojnrVXrd1I9ZmMbGp7bnLpJ8wdnJEs2wmnhgLXPfVN7qQDHIfzxTigpcd2dfMwIn1v_EjEuV4sSih1Zv3wgUMgPiIsOpKDnxijQ55zRvSOsnqFcYeBpWJahwyfZ94MynfXZt9TRGT3MHRFmW0u7W5cIMvg0oiVEJPL70puM82gNSajwzaVHdoJd-ywAK85QR5a8kxhMkEaHvKCqa7cDiLRG1HtyM6-vp_nvBGVdyu2AGwP3voT3FH_tsk0-madWSPUR2mtdziHEWkhREzWNzpXgTBm9VN8q2kzkna6DG0vYquqAALFcI2mP-zsrmTb6j9FRayBy_BPLeWe7NqQcFP8yuk7ptbfq1PQpVAZ7GFOZM0q7WEmSvq_JZ3cmux3H8utdKixTlu_X76OAA8kJP64TvvjY9X1ri5nlvJNFITH2a_0N-Fn-bl2jwfHvdKXMvkuyj3zUDDQsU33FeVdKgCZ1BqACvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=RhT_clu9rP8CW866m2YOhFAtoU-qBfRRYxPfChAKKTIcRaOYc1evydFtQZKmLdbIX1XTWKdr8fPjo_1Hzo5snVoq-PVkQXBfOXCuaRFi2Lolx-EmKfmmnkozcaLrLx14dsgdKYjFfQh-DPrIceePEtPm7PeYs3IoDDtG4T-__sr25J4WKsrx2DepTzltvFWhUbCVDAQCZkLJGHojnrVXrd1I9ZmMbGp7bnLpJ8wdnJEs2wmnhgLXPfVN7qQDHIfzxTigpcd2dfMwIn1v_EjEuV4sSih1Zv3wgUMgPiIsOpKDnxijQ55zRvSOsnqFcYeBpWJahwyfZ94MynfXZt9TRGT3MHRFmW0u7W5cIMvg0oiVEJPL70puM82gNSajwzaVHdoJd-ywAK85QR5a8kxhMkEaHvKCqa7cDiLRG1HtyM6-vp_nvBGVdyu2AGwP3voT3FH_tsk0-madWSPUR2mtdziHEWkhREzWNzpXgTBm9VN8q2kzkna6DG0vYquqAALFcI2mP-zsrmTb6j9FRayBy_BPLeWe7NqQcFP8yuk7ptbfq1PQpVAZ7GFOZM0q7WEmSvq_JZ3cmux3H8utdKixTlu_X76OAA8kJP64TvvjY9X1ri5nlvJNFITH2a_0N-Fn-bl2jwfHvdKXMvkuyj3zUDDQsU33FeVdKgCZ1BqACvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFC0wrdWuRjXOri0ZMdG4viL8Bf2iksj8TeCeRqsdjgAIcDH767p469Ka7SPObcXjKCL0Jj2T2RJuGQJ8qBeBnr96cZ4LF4U82ieTbNS5v_BCG7kVVfGjhBfiTiQMKe0Sb18hyC-zxDviWU3WRDhFsXJ8RXUv_miZPcEmbpDsVZj-SkCDy5t68Gq1hBb5e9SrMB9KrqmTxaiOdBHSKYe6REAnJ-ICZm9U6pjtsgl0JnsFC7GZQ-IUNa3XC8o0J80606gJFq6-tw-557ZYFR6vcrmqwJYnMWcbb89kG_nf7rvetqAkNwKPuYx1qI_rZGMoNPaR9txw8jZ-ki6Er2gWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=A26oXobYWlIsMxeo-NXg0KEZuiDxK95CvY9Sk_S9uVLvDsLUpgDxCOm4dfCmGxs2FOKielZiRDU2TGz6F6oMKpSP-fqOJP4f63ijTw8hDV-6yIUGLkbfhjKyLZ1Q9DOpvtxLKOvZxnd9Gt4di9AnDD3O7WVVf44Exma5AGDZ-dC44d-rcl1Qi8egbRKYDiFusUPGzc5vJAAew7wTAZ87oMHLgdgE8TLrzy60lChJS1L0-eIGQWnn8zNS22SX5AlDRP0KsG6Uc7EBq2AXixNtTuoinqDsM62qb6Y4nmkerIYiHjJ5lK9pl5JV-W7rS5_I1iPZjjVivJCdvJXogSt-bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=A26oXobYWlIsMxeo-NXg0KEZuiDxK95CvY9Sk_S9uVLvDsLUpgDxCOm4dfCmGxs2FOKielZiRDU2TGz6F6oMKpSP-fqOJP4f63ijTw8hDV-6yIUGLkbfhjKyLZ1Q9DOpvtxLKOvZxnd9Gt4di9AnDD3O7WVVf44Exma5AGDZ-dC44d-rcl1Qi8egbRKYDiFusUPGzc5vJAAew7wTAZ87oMHLgdgE8TLrzy60lChJS1L0-eIGQWnn8zNS22SX5AlDRP0KsG6Uc7EBq2AXixNtTuoinqDsM62qb6Y4nmkerIYiHjJ5lK9pl5JV-W7rS5_I1iPZjjVivJCdvJXogSt-bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeOFjG5CtfpRXypoFlfxrNZ8VIkkXgTy8Hog_XlDzMwRH6VyWtPPx3PWOC0Bz01pG6R1L0uHLmGeZAsDxZIPQ7RXyCp62CgfPBdk2qtmml93Yg3pu33hnvT-7wdIk6WNWkJEkC0mhlR_0jGtAhZq2Z06TByHhNrq5yvtdiypQDujY9HBP8cYt00KYCnr0U_mqjm4uf0RX1wXW0LGHuLJOWBcke5HvnPgaLRXYhTv_rcdiqkcgttK0_Ei9-RxYME1fnTqrQC-m2m3SJI9D9rJVc-HJO8ULVC9XJMdQX0d6srUrUwyUzZuNUobHQh2N3Ok1abpDFcL1bJ0_-tpZignEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSHz8-Qv3Spy09a_remq4lk1Ql9zRfHmBGVdWzRZP1Qf4kqZgJES07t2Sq0nyP08yLXSktXL7Qp1rh22tlSJheyEEA1eVtg_U9UqxlHyyVZmwhzuJtiM3FlrouA_hGu6LMTB3oWXDje1L09m-tD4yPj5Ca4CGI-LVhV0zCFMIpb8HWpcHnsjaGTBlEZymO8W1hcGn26s4hUq20w-quNPmSC409W1SJDmUY85-QwCJBq4APshwyufcJkcuM026v_QtVdIFBRd3h5SzTzYtfaxu6fhAobmgVEQploIjx3Bl2hpRtp0nOVVE6gQ18O6BxZbG6oKdkgePlqAwLMmKBHDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhGja0nnbElluQ1Ja_WbbFtYSF7DxG7yoVKHZFxX5Ium4niNhaEVsVt92ExWjuvpRY4Kf7PGlaXBfj_k-Tf9m0jX05UQpO04Pm1kvk8d3lfW-YeDBHTiGTS4EAVovloCkLkZVr8ZmIqT96m7zFU2hl3wxgIglwSGOXttDlR03EdgxcsSNSdMJm4MNL51b5nhPPLYRJvpQx8T_64Q6OfWXFg7-Q6wPyvTHBfN_2uactSUp-thr-F_v82JB2VMZjV6YmM_GANQZ9LBh3bSyT6OEv5-VXi1sEpwClpmkIpGe-DFzSPo5siEy8FiQfZl7_TvYLnOqL8VFgR-hoiyxW1b8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyvroW0xnfXbDovLWJP9Me2jA8DQEsimHCy0Lufg8F3d9qZakUE8kCV4sB6X6IVhKX7-TVfaApXEUyWrChKyAaejEa9yykSM7Mfo1AfCsFMzCzD9gg3BMGsDl0vph4VX9FlGrRdZIB-MP1kH_82NuXdoAB40ogjsViI5dPvRq0ijaCwdzeAm1SP_L5nqP50vM--q21iw_keGZoLDx2-tKYCKw1QQvrmgdS7rDPNuffxbQlnx2VQsiPZOChatamJN20kDsuqAtQjebvysfxgSZ54fzYd_SIVzhd5GyDhnayAwxi8XxsD8P9HJfQe96dIKGD26GdJQLGmgj3V-FmpCjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uECznx2e8tWjFueVzBTPoyRfpGB_TR5xEvgGas6dNA_9gqD8K5C0Npq3BWGEfDJcE96kmdX3akAc1r19ICqJ6icXynh-e98kiUzcXJVp95eYinb-gyARlSQzW1oXciGjmomn1D6toq9Ty4ZqCIGYRWjB46UavDceLbYrKSyB7sdl6a3gH0TQZ75_hxvnqBGdXeop5OOtG-3RmTkiu5_H-lea2NU7u-m9TBW52I8HgbrKTbBnEQofDzzxDQJb84bssAWDC62vyVQNPmuppNGCdcB626zLIJzizz623ZoIKGizbJulIskUIcYXdbux-WJU3Z5Sdk_d3AKd6m5_0600wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edEwrc2j8RP0DJ5Yia03hlTKmArJ0HIQ4n2LpOHLhUCcKz6eI6iHY06d4pPJpESnpnZdexluZv9_RejlurJlP1JXl3GfKrU6Kez7OQ8aBvJ2nJnlaSoaeoF5UCLw4BZJb-0xH7m6vj_YEkxEbNVmIfKcz6Oqf_Gr2iVxPHfjLr5-vdM4ieQJimPw3yDlIGmgQrn3kFcocy9967GWZEReFokxAOWUVnWVodDsBmsEWKJT65UkTVQwL7DsPsikckGzsPWL15EEHFsD8k9Zg-F8BEyfbuoJAxrvSAbEFsmnCkvRnDLxgjEha_PyHRT7YasbRsb0IIMABqaHLrugR-KTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0MiNDPjZrH8uhbIChdcuspuZb8Djoevhz4lpuqPpfpQlbOkzSelCJ4Vgast8A513xIhawAU0jilXfjyLdyaIeIr6c31ombpH4kZVgIevAIQqL2oasCDEGRuJ52-pz4-4phNro74yjd5u8AlPoy-7_meaamLhOGc4eYcfnvVB7R-ye6tCbW0CmR8Fp7jFzoNH4jzv8hrJVVv54tHTt2txMGVsLbMDLSLEa10FnsLSW--JGYs7gIxtg6BtJbVzHmziTSxk8UnP5j6IY6Rl4s1Mmi2md0PTbuq_soMJuon6b8zU6zPrSWqxYSZZ38kxdCqweLvhMyPjbjgi0AFggwqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THGDg5W_WQk7Suh8oM6acKU-El2Oma0soEK8JRc3nC-6MqB-qfG6muofiJS9aCER5CnXa6wURsBXtT5yx5-UvjqGgCe5Kc54iRYSQVqYgBDwNsXUoRs1QHtEEGWtBeQiya7tZV4AdZiCOxaAXL_Nh3oj-AkmxD9M5R8gNsLxJ7oWCMIeQ2kL3s3lnJCm-WVKAcv2fIMaVVd7I7_Fo40xQMPFmZA7wn__b80a7AcuJuKAR85hQrL7UGHGAC5hjAGXJY8_jYdN0MGqYs2eWAUmcQJSFxedTyBG1nTsbkwseIWY2vdJfQGZBs8JYL8vJ-Vgx271hpwtdOKIGFlWCUru9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sK8oRycNKTE3IMPhySSmVWpjQAn7DBL3Z6MtK-4Wn34h4gfQI6eoD9V2B0GMox8kKHoHfN9MJOv9pa_Uh4StkYwsMT-KpNNaHw0HtpC1ZRMj7RnvAdOUk2DXjrg8hGnC44wJfVKolQfhgZYAv1Btj_IFBQwD9NMs2ZlCrWPJc-khZj1xZ3hQjq-oP_J6zOtDvPxmMqPQa3r-LwL7xis382CW72ft4jqPYEB8Y93m_EwgSzq6NgtRPM-jwbly_3mRouxZsowB7UO-BIY9_kjnEu0yIl_duA5ltQ5qQdszUZvRE-MyEHAWeDhdqJJKn8vKx4lL2-oheWKeCx37cTrQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYUsjKIY-nXAw3FsQCwU6WRtdDAw3t4kJayHT3pIvL0X_we9gk4z8A7fNqVL3mghfL2AuPX3l5CAcKJkghFSKIAjrapV9lVNhPvYT7vDAPQSdz1uy3RMpIjBk_vMq9TGGiaMA780Cf-AfkBqVOFSoQgZMbp_X79lDOYTzxuC1Wh3Dp3ADyuUmxkwGan0mU39nbVmcHS0HDN5sVnxSPc4_hkb-BnpzShWCoHQAGkC-JSVv_WAnINvZFpfKpaJckGajM1-qg_BBREjoueWuFST3AEeBpNAw_rp4JqW6JGikWiRtGAq1cIsGT7XS67XHetFEPFfN4TMRhGo4N13W5lOiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5U1L63pk8t1pq4hW-ptFOiDR6matN9H7obD2CNiDMAKtG5zfYYiKRaRG7ZGN-H37VcjucEgY2-KXifhOnCVq_gp8xw-k7gedQ3xnHUCiS-v3MHzCGCQ54EZmhoCvwTMtUxRSBNYsMIrujO_n4Mr0-l8qAAaL9Re74ODCslcvLCH6hp3it90kkKtWl8fOsMw4ipjwTQQ1BVSSuKkQ7-moCo-ycxazZbGguEd1xuNJLrkLAQX_DTIPy96K7Za3kDOFKrtnDc755yGMmpjmCbnqDbWWlPv1pGiWovStneHRe5H4dX4JH4NjAOkfwguB1DaUnawXiSXSYJtjacxC-8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odftG6oSTWrt7KjkCuIR7AOZBo-gsoLba5yMMWL41t2UBpHxH_2Nr9JfdEj3bMYpcycv_V2Cm1Aw7pchdWHEkZTptst0QQUfj6mngRv_DraPhYTLBcG3xjb3sDOcd7eS-yoh3gCjR0Hz45e9qouFay0hwaldbo32r0xZdPKptzb610GadMtAeiALL3luZFzbHLvWjSkLMPKtgwj_W-ZPt04vfyWmesXyMLrQg4t-M4bYjRl49_lpIoXL79Affg8nUmZ95tmwLB0bu1PhcsUj-hRusPiFwljdM-MBcRQTxhf_LCUo3hjPSb8OAlRm3QWqMby-Hk0-TaXi55i1TulLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsMwoaINX5dasWDzxDBFQuEw3rr19s1IeZakDBShV2z6pWHZmoYGgpvLomyFWCXi2P2BvRteodoJvgqX8CvdO4CaDjaaCmgV-2rHrMfjn6e7qbqnZwPYWmnTaogcF6D9p4L5MBRIs0oUleEV3kcNcRD1CfYiy8wRCqB87-1mJlBJ8GyMREQABvu9xD5_IJmb7fG36RIer8qyij-woT7O8CEWrJVfh9iSxoqmJOnIKdbAw9MT-sue46Nom3Px7_5U5ctT8Wz3tP74xi5iHygl7xvKUs2W_egHwU6ZT7KsgvdPsQqRW2OSkHadeKs9npVzwDUa_koEabrLWL0kFKO9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehy6MwZwMdAqrQ54tnCGKOew3b2AQeLbcbs1PXwEEl0xciC3izZ4Bbt1yrvv5RChpMkHe75H4vvAnZRGlWgN6IJducSwqhSgKqfzDVXloiI4zxduEPm89s-GlI446fbNFTafbmTT8TU3Uj5J8foum7fa_hLkqqARbCbnCcKoo851Ch567FB3WDTWD7Gfce7dA_iI44fiPAj3A0gOU8vjCwxQ7W-NRkvdgqFnTdkkcjTjiF5hBHMqLoSqslQanqnJZToe6dIixPfvBIXkRusRFZiVQnKXuTgkiwOVY3U21Ieb813v-KDVCXBFA4Dygv5Yxgz6lbAfRuh-5OjF_mKdkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKr93esvUI88tP8KE-rSXcDyFLniDxnbXohymKJtB5oGzWdLFXnkuU90a2BOGR5v-Y4WxPq35bfI4GNBjMZTnR5OrlK1O8O118657Wy1d5QK11BSgKNxck9IJW4_yfdf-LtwrxszvaKuKSTrCAsvsq-9eLKDuavJCJhCc2C1fohM_hZnfMQLakel_5CvWL67WmkN1pJ2iKEntIb5OX2hZ8xZsc1aXsT0iONT9btQiOBAJI_GqCaQ2w5RIZVOo58uPSqnOWeOjGyQoiuxp1DoonRf44ZcGqtximQ5Zar5Y5ifyioHryG8J6riG8g-Jw36XGSfe3AmM3nZMLQrv9Q3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUkXAuDHSV6JE1AkrIn4XiqNruIMPjEhz0r6ywv9EMpAhf6Iy7CmCvUQfRYMpmyQfrvS7NwdJQjCGtNYVaBVQihuSka6e_RLSP9lzb0xxB6cHTiTYnvpRahdxGEQ_A-vnemhcVxHUEc0j5wZ0ZbjVeDIabK1TO2FRhYrwdC0Dtj2P9Mbe6iDMdWKdfXA5DTQk3IEcl1rboywSsHg1WC2H9CVFi16-rPNt_Q9ZGq_12eVilR4ci090L9YZPbrSrcagUMvfIgPCkK2VE1CUVUFitG47g_T3zETVDJq7_0wzVBEmQR_rxWBrdE5Cr0Ee-TjOcSbS9PDqPCHEYi8Q5CRXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrGf78fDmF0Iy0U6dJoMbSPZa1thiIeyuAmvLJLy2ciKn1a8i-o4cnalLVkxYKic3JW84_xyNf0DJVYgds6LrsmzaLjhsXKW-osfnPDKSMmqImhknXkKlyQTpF9X32f45Zcva-cvlykeZ9Tc1svcsUA5FLHuPRelDLDnH2cEC2yHZi6k3Ox_5K44iASG1Zrln_AjMLMyxXpMQARMZTTM0W9oVxJiBZW0NFYAalLGAjN_5R-dyNrOQqB51SsvXHnrzQ64wJve1rfhe_8sbe7PSGxOyRH7bd96rK6dB2xOsFJXhzqtyu0OiwADAtjBmcVK4AZu0qhwJF4FYBxOk34twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=qPg8b-m0NyTfYRt3IrZPAr3vWNupQG8V3oKV5lwEzBSlw_ICuer9bTYA6vbkvKZH5xB4kjMAQ7vnVrNA9zbbo_n2rF9Y0BDSZVDO1q3L2PZzLLr5IYWd2xIcPcDhz2aMxb9wXAmCqijku-hU5Zrz5fDQMxApCBGhB2vlGoRCRxt1prp2rIQ_YhMMwDDQSnn0ymJ9clBmASKZLuHkuEBIvY_TaaKdO9DAWXUptT8PNNssKYXHS23YCGI7NJYnSTzN1dvHpsczVf-hyVkgj5jquivgAlriY1OnCT1se2dWXkYkWaXLii2Gl8W8lkyLoCvpRzl6wH8aUMNrLA_LKWFZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=qPg8b-m0NyTfYRt3IrZPAr3vWNupQG8V3oKV5lwEzBSlw_ICuer9bTYA6vbkvKZH5xB4kjMAQ7vnVrNA9zbbo_n2rF9Y0BDSZVDO1q3L2PZzLLr5IYWd2xIcPcDhz2aMxb9wXAmCqijku-hU5Zrz5fDQMxApCBGhB2vlGoRCRxt1prp2rIQ_YhMMwDDQSnn0ymJ9clBmASKZLuHkuEBIvY_TaaKdO9DAWXUptT8PNNssKYXHS23YCGI7NJYnSTzN1dvHpsczVf-hyVkgj5jquivgAlriY1OnCT1se2dWXkYkWaXLii2Gl8W8lkyLoCvpRzl6wH8aUMNrLA_LKWFZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxAPuSD8xZcy32iWGrXOfzbANk8GbrX3blvob-escmOxUNn6F4z2l7vj6zfg2c5W4CQ-LZXnvTRaiO_wmWvSlCDQqocGRnsfWa8zIfOSfzHWASdAgwNecT3SdkAWusZezGFKLWQVxgvCpCYtGNyHJFGJAmTYLwIs1yVqy1pb3ID-Sur6A2_ud7sIg4Ho-I8352LYEkp-rJunnwJxSXZPXuHR26dHa8fJnIKeoQkYbqCCl6ZhO41RRGZHpLoqKEkbjGqq34PZK12c0Cg1AeP7-begDP9sLemLfq2gF56pv0UGTOdlR00rW48JXB7-Pihu6EQXP5GlE7kDt2wD1PyDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czn0rJEBwsPWN-wx17bqdOjekVa0LamfzKh9U01gyl2drB2P8omyOTlHtY7z6VI_nCbkKubxIU2xA_0h6KTNcqVdEgLoV7kizsMNaUb9Ks_xNDLRhI5Cxv9CJAtZ24QLQJ0kG98BIbzv1AMH27U_72l5xYYD-RHTybWJcsJdWcamyrV62clPYz_nkkWwJza0QMd7BF8JP6HW9VkfAQbCj_uiHVvTK1gQsVSKIJIcltszg0n7NHOKHuruBpa53_d2guRCFw4HMp8XcNDD636GMPsMy8fpI7f86Yu81s09ig1cWJ3zOweulQrvJN_gReVqbElttMHM4b-Kzo69fqVPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsdlnKwwdR_V6a2jQWszAiU5W-LjOc177LOzL0_o0Ibjzkh0-xtvCBCZQAu6mRgG8tVR6U8CUuEnLvUwpPE3B2rrkdbVL-O1PWWueQJRMQcVTUNYhrpk7DX-HdKriUA5qL6S5637jivStsI2QE5rFZaGVkFf1CeqgJG69JN9OHaGGATQXHDQM3XS52S2pUaKXWinpe5yz_iiAB-3rC8661MZVCGp3Ppis6sBmaoEWg7AlEqFF4Sh0djRHaV3KrlV51BUWa_4fxH3KOvNt5Hk4cedOm3ukWZVz4PuOXCocaPugga5FDVLLbilvmf0hp0CWdMJ3gqyO34sGte--mBbrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=I4b6eqxlLXmxQDXsPyVdb8rnPFa_SR-U8Qar7drV4ojeuqhEZ8-QVIzeBd2aDmmInBXkONeTJ2d3No1NpMjTTHhqVJnglU-KRFIn_l6Tpr1xoOzbEvzz7TpnKhqd6l9J8pE_ZVGir6_nJF-RCj13ivpQnNVSK6LsSeVwzfYsaQpsBLc8soqnPKHlXmfjPJrIsefDzmxw56Jq-QhOP_2DdyevGUGUoYsFlPP15u5mtmEMnG7LfylHcjajyZpKJ5uXNuCgjVj6j3hdTTtSWMhcNuJAH4SuR0CSmsT9Ze-A1q8_g19IXMUClhGro9DLG5Of5K7I5hs-ExAvyMSuSDaviA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=I4b6eqxlLXmxQDXsPyVdb8rnPFa_SR-U8Qar7drV4ojeuqhEZ8-QVIzeBd2aDmmInBXkONeTJ2d3No1NpMjTTHhqVJnglU-KRFIn_l6Tpr1xoOzbEvzz7TpnKhqd6l9J8pE_ZVGir6_nJF-RCj13ivpQnNVSK6LsSeVwzfYsaQpsBLc8soqnPKHlXmfjPJrIsefDzmxw56Jq-QhOP_2DdyevGUGUoYsFlPP15u5mtmEMnG7LfylHcjajyZpKJ5uXNuCgjVj6j3hdTTtSWMhcNuJAH4SuR0CSmsT9Ze-A1q8_g19IXMUClhGro9DLG5Of5K7I5hs-ExAvyMSuSDaviA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOakbE2rxoRi2wFmb-C0oq-xyCcY6nmksQDHJNDj5IXpl87z3K-H7HOCL0NuY2SIg5087UEXxA4oODW3FIlntrXKxU5BdifKFTW8QAFZone4-_COGPZ2ZqSQO6U5GYhcE-UcVIKrrSTZVdL-E4kGAsIHgNRxt3nlpH_Sm_fDLCsy64dpW826vQuF7AUpMe1YR4GrqIevBWWrajRosN8ujmkymi13v0EO5WgfB-lF5bjWRVsWTZzajnzVz5iOwSnUZwV3f5QELcoP9S6qcus8SItw0qz1PD4PmMObNBvgLyUdTh-fd5HyQJQDKLnvJ4dLQmjbLo8xBpRaTxFX03wK1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=nJAnebsXkSMw3fiDv3g6g0H15HU3ptQDS1ZFrLZbWGDIoMDHFXDsysiNaDi4SqLDWNMQWVxLYaGw9QwbDX7NFl4EYEwVm6wj1fCe_mH5_l6e0NOpXYD7EzypDi1l3K_g71hLaV0okBH5iic0iQwzp-LnxDM9TdWYAeFpwlP65ENqeF0hOA8LZ-ENS4rS9ip6rekfHM5AN9zuOu3MSznquHzfNBPRytFsNoiJk2txWbtGreYVLtaaifhI0OfSG4QnrudXQW11d_1S6uS_Q82T-g8Qc0a2vb4HGOfQPk0E3Vp_ghvM4h7JH0MI3EitKijo-gZoQglIrD4_hagW0I5o1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=nJAnebsXkSMw3fiDv3g6g0H15HU3ptQDS1ZFrLZbWGDIoMDHFXDsysiNaDi4SqLDWNMQWVxLYaGw9QwbDX7NFl4EYEwVm6wj1fCe_mH5_l6e0NOpXYD7EzypDi1l3K_g71hLaV0okBH5iic0iQwzp-LnxDM9TdWYAeFpwlP65ENqeF0hOA8LZ-ENS4rS9ip6rekfHM5AN9zuOu3MSznquHzfNBPRytFsNoiJk2txWbtGreYVLtaaifhI0OfSG4QnrudXQW11d_1S6uS_Q82T-g8Qc0a2vb4HGOfQPk0E3Vp_ghvM4h7JH0MI3EitKijo-gZoQglIrD4_hagW0I5o1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hezCdibouJLIg2Bbhl6u8BIZ-LLihHoBeDNyrbZIJvDT_4wWMVppORpT2M8n1MP4Z7FPSo2kxLFq1miTYosSYTeI3p3tKkueraSj0qdcLmAz81J3NOSMBwtk883IzeYfcvFHlTxLqYdbI8jYJUEAmy-4MglKl2lKalOxSfdgOnfhneDmIdZYDDLad-RG4uhWdcbjiYfkcd_O73elyIeZiDPJ4aLsXmwLCwQuV6hrBl1GfuNQS9ZKCSJWEoDsIIQw9APJ4PgFR9BbjDytB8nP0Q7rX_6NCQSX_9cFcvAlo22LJRynH5oK6UhenvTX44FqboEMtofBGed1RrNTmnq-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPG0wAUcU9OrFUXLqfp_6nSGEAZVrPqPAH5GrEjVJVQylesIoEVXiEqzvhedaoVZT-Qvd7u3gE1l9-b3_68F6gNy7WTcKOGfPzwnfqQfAPcuVofdcZN7B_8aSrB7ZSKP5uTQCTNBhYglOMNJHF45qSHy86AahNW-DLO7zgsoJGLS6bO4tYte27Q4jD3u4VG8m4t-sWVqXFU4V-fkxk4GrT8UCdFL__qkaivJrD7hTqZLItXZyS9wC-7RxI4s2Fa-Vq6QOLf3qfEUI6oVeT4SzW4jct2rs3fj4TBCCPQrjiOztz69wAa0UZo6ee5OyLWjjGyCqqk8yLRsMYoAmoKw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=TOIusZqah5gjcRjPTrLn2R9z9E55Kx8TFzip1AwBBJmAOuX0wZMrLbfNfuV0YfMvE_yyY5HDHaZlJCuTcUtJ7eeeoQ3peDwxfvJuHoNSzTw6iMvEJCr-0W2G14mJQ6nwGIUMF1v84u-krcgZwHh6CGTbg3Ex8ys2fEo_2j95Sp1p5g0QEbCECKRs7Jw008S0gRSo0_jlx7QpCKWJFG5oonIDxo2dFb-D6K8SKjSpbN1uQU4IyhYzJ5LgmV12I_41_A34rHKmAdu3EUqpEs-DYJhzDN5xkYX9qFkVJ0UOTIoVYd45quw2R9SL1MJEUDE8zEkhJjD1LtuU2Zjx8zUFYzlf95ViglEBiKjpKkpj62FUBHqk4Ek6Yp-7ss72c1tveBKXAJbcLGczo5Z6co773K4ULP1N2mLOs4pRREV_J3r57snyQefIBP-EzekPdEFWyzPLJbp__3IDQSktEE1MPb0-SinmFkqGfO2-ubfyMvs6iVmdZqAfXzldD12VSAve_KU8GE6QupiFUCMje9zsLq3DfTQBebBoLzOCerix84VTCrWiiBn8Q46ZcRPQTcP8x_J7AcwPy3rtCc98QUEgvDoRxd6Up5YsAGrpR43r1kz50l-tXSEnxKY2vnJ1xdmSUZZ5BHluOAYKbl06hqpOr6NM2I90wNaEGvobfkEp83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=TOIusZqah5gjcRjPTrLn2R9z9E55Kx8TFzip1AwBBJmAOuX0wZMrLbfNfuV0YfMvE_yyY5HDHaZlJCuTcUtJ7eeeoQ3peDwxfvJuHoNSzTw6iMvEJCr-0W2G14mJQ6nwGIUMF1v84u-krcgZwHh6CGTbg3Ex8ys2fEo_2j95Sp1p5g0QEbCECKRs7Jw008S0gRSo0_jlx7QpCKWJFG5oonIDxo2dFb-D6K8SKjSpbN1uQU4IyhYzJ5LgmV12I_41_A34rHKmAdu3EUqpEs-DYJhzDN5xkYX9qFkVJ0UOTIoVYd45quw2R9SL1MJEUDE8zEkhJjD1LtuU2Zjx8zUFYzlf95ViglEBiKjpKkpj62FUBHqk4Ek6Yp-7ss72c1tveBKXAJbcLGczo5Z6co773K4ULP1N2mLOs4pRREV_J3r57snyQefIBP-EzekPdEFWyzPLJbp__3IDQSktEE1MPb0-SinmFkqGfO2-ubfyMvs6iVmdZqAfXzldD12VSAve_KU8GE6QupiFUCMje9zsLq3DfTQBebBoLzOCerix84VTCrWiiBn8Q46ZcRPQTcP8x_J7AcwPy3rtCc98QUEgvDoRxd6Up5YsAGrpR43r1kz50l-tXSEnxKY2vnJ1xdmSUZZ5BHluOAYKbl06hqpOr6NM2I90wNaEGvobfkEp83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=MBo6iXzGqsi2J5BM2EpGSRmgvt-wWGTK9NLuiGEEBaHbI4IDsF_Sad7yc-HvGytbmNgcc18QmokkIhPPLhh-qegZt_LdYEecByh0Tp8idUEY4R-cBJ9SjYX7YoEP3hYj0qgdji2-27gvl_JvC_c_0bLdOfzZYS50UTWYoIqNvhXfYmELUjO1jtUih3jImpI6TNUoWerRTYQEmrrD-9lxjpRwPbnOrXLb1dSrphzw1OI6JVXun4rDv2VGs9b9HPDF-F25PGKQSpUdgSWEGMVFrcEBvjJ4yCgQov9OVidS0lGW0lZbeiIyniKDk44KFBW9lN5jNWOGbtcLt7FRVKiy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=MBo6iXzGqsi2J5BM2EpGSRmgvt-wWGTK9NLuiGEEBaHbI4IDsF_Sad7yc-HvGytbmNgcc18QmokkIhPPLhh-qegZt_LdYEecByh0Tp8idUEY4R-cBJ9SjYX7YoEP3hYj0qgdji2-27gvl_JvC_c_0bLdOfzZYS50UTWYoIqNvhXfYmELUjO1jtUih3jImpI6TNUoWerRTYQEmrrD-9lxjpRwPbnOrXLb1dSrphzw1OI6JVXun4rDv2VGs9b9HPDF-F25PGKQSpUdgSWEGMVFrcEBvjJ4yCgQov9OVidS0lGW0lZbeiIyniKDk44KFBW9lN5jNWOGbtcLt7FRVKiy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQwXOm82OCnLJQbdhzE_3z2_aVpNaUH-h4I9JfumawN4Nlb0ze_2bbArIoPRsvKP4fz7KFONQV4rHSIsTokrJaH1wRa_XagNJjuKzeNWUigitgV4eKZqERzblioAWni4XLkQlov1x7QHsKVhaOfhsn0bf6l96_RwNdDDV_Hd43628z9xlEeVxMs7sjoGywT_qnuNX0fZNMC5lS-UWSDyBHowtEqNN_W0eKIXP2MtlQiUt-PtDE7W66rptKzng1jApVk6I-Gt2kRnC2YvcRoZyQjoP56-TOX7sih8Gz5FMrjshKb1qkNoVwbe-XiO9pDGEX4SiQpXZ2VQHsInNDxPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=I7r0b1hodt39XDrtf85koOLYwvO2iENRoYV8uqtjwglP6s_JMGx-5iPVBRUrof6bf9GUOYZlrsWj90SLiehDovsbjuLzL09JGksgADrzgbZ0PAyRz-ppMMzYx21XF_rvQuuXuYWHWPGwTB5gnAAVLxyBonPq21KcZWDD0roJn8vjmwm7NcwOBFu47lVrYmGNScxyRhF8eOjc2DQ3Fg8qzbAD6kNWFldMGG0KxhoLs-yoRuufyWjRIKgdOVmBbTIuOyqVYDRk6yZQdkuA9OxUoOMlaEzwaYLZy0MP8qTddwdg9OsUbmuxHhr2TA70FRAJeE0jTF2J9f4HHp-T5NPVbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=I7r0b1hodt39XDrtf85koOLYwvO2iENRoYV8uqtjwglP6s_JMGx-5iPVBRUrof6bf9GUOYZlrsWj90SLiehDovsbjuLzL09JGksgADrzgbZ0PAyRz-ppMMzYx21XF_rvQuuXuYWHWPGwTB5gnAAVLxyBonPq21KcZWDD0roJn8vjmwm7NcwOBFu47lVrYmGNScxyRhF8eOjc2DQ3Fg8qzbAD6kNWFldMGG0KxhoLs-yoRuufyWjRIKgdOVmBbTIuOyqVYDRk6yZQdkuA9OxUoOMlaEzwaYLZy0MP8qTddwdg9OsUbmuxHhr2TA70FRAJeE0jTF2J9f4HHp-T5NPVbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxv7AJxpZUXwSRkG5IdD3BcRCHy-5Yt40kALCqpLqiP7iplqNELB6eYRHN_ZUYaqFbSEUq4c_wKtDyH0ONKvKdHKukKqctLIbYYOstt-x09BcZbYO1sRQzrl2mJkvJlLRcU3HlkRDkaHGmWIDOlxn3wWtt6YyPJK2levgw2Uf8c8DHKW6goa0MIvf3JMnvMFgwnj_TuaQLLFNbLKFaSzlUDip6eTlMTeNwW8GhecM5YUZ84IFf-kE8qH4TNwl5lsumCNDsU2QlroO349UQv3n96DqwuQbNePd64igRmA5XychccNin-DltSBRsLVDzx7L-kTpAb4xy0zPXoec797Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGTyJuCrGANvFl9RXfTBax0aBF0xmd3YiOlsRY7maqjLj6TOhtdgITsegQbORCNPRLRfjNOggavyfxQJ7NDk2ZCXQXNsM6ieVfj2IrLg2Vyqf4spzFUuZYYHYropC7mSv-xCHfKAouukEB9Ub75Sz7ifJk1aUSM4UCT7TDpvee2640ErW-6FjmrXKAd4Kzx9w7cmVKYb_8B27I2SQ78Qc-TvK7KDHPj4RzoXwoj32WQllxPOu6n7xAp-3IcBPiJkb061XMVHLUByv6yLsb9dsRKco9wUMSe8tkeoe_scqF1QwkNKIVbuolJ3YLKnod28BBEIv3VJDbmQZBltg2Rwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o754exu1STZOcH1EMWHnkkUNxtIhhZvUD5X0kbddEGrr_qxfEF9lvcVBvelI28IGhn7fOqehXnsRv9VHP6lzteiIx6NcEqIvbGeaEekCi4zyyqFyWx5Z-z68A2XW40hHSEghpbejb_Qv8elEYWa2oWvQN9R90VUsrs6Po5xBt0VLztbhZ4-EYXIgbFJS-Pg0XDAhCEiXbDvsa8LR4851dMUmD4ya1YqpnSE0Nwq8aoTy6m9CTcq1u_k82N1OVdaT3dt1Dgni39J7Z0SZCBS65aQjofOLVkUNkzWAtu5h-ewr4mLWlHZ2RtmBOdZK4GDM-GFgWMv7-VnZS5FWC0Dblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBb8fQ7QvQztQ9qPmpJVhRNX49YOvRgeCkO8yu6UybTRNuPGSl-Moq-RWeiW4FkBpTiWTTy6cwgBQIGNoEmye_4zLLVT1gPYKLJYS3izUxfgrmhSi5ePr171HYScaMbiFwZ8twqtV35iJI9JpzFTLSP5vwJWBYn-Csj0_oJbHG-z0K2gZax2gXihrqKPMw5ZFStqd6MM3X95M29IjRtSI2wI5kvLXPWhx-d156x209QWivjzvm39ZRzk06nj_CjVRLuxwsCG9oSyyRd7HbOV7nb6Xo-f8OGEgxBzDNejAoHtLBK2boQOTnzgnVgb7aD_pCzvTgc9bxhS3_c3VbA85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQQDFypbLIa4GFG5PjOIxSBz0GD9GWeLEY0dfWAKHgIaGY_KBTvTUBfAJqDc9QbUoyYPKguqa4fuiiM1Hoqtjb-R4De6h_sRZ-gib4OULtxnYrAJf4l1NlgZrTMNjoEPLfLOU-BpM7M-BZpWrKMyDHpC3FBucB46KtTA2Yi68_7E61k5PMDfWb11Y1LrCXd2U-olg9h3G8tbHs4fUm4988ZbaUBtwsvWmmWq04tFaeaRjcBCzRz20yQcB84JaJLEWzvb_WyTaZ8hk-wKKsIbVJy5ZpdvmLqBc0UlHWYr09BneZ0bQlvhgikEJn6j1-r2VjHwAhdtNJCJyYKSS2kSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Hze2P6Af8tlY287wtr0tgKYKEhBaqT1pZ7-9kxu-AiLNPzMOBhzE5BwdAsRzwEbpYaoZXbHjcj_WE9OHvMPUI4I94xjY6fLVQsyMbLQ0Cf8i4zrqvfu8qJamKzGCuUWpGtFKRWPv5oJMJX1dxs6J3QOA9JBmxmn1x-SMnkvBmzN4XZ7CjTdPppREEixw00YpayGJ5dTyzxbwrwg4hrr6I5uox27RMxj2hT_q1a-2PMLWdhmkHkjAhGLn9fdieJ4pvedfFCOjDOeuTNA0BaniEUHy1gXryK_zMOygSlgqxk7JljN8P0X-YvRO8XQmV1OL7OTjYyK2X67aDcAJ_xbUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Hze2P6Af8tlY287wtr0tgKYKEhBaqT1pZ7-9kxu-AiLNPzMOBhzE5BwdAsRzwEbpYaoZXbHjcj_WE9OHvMPUI4I94xjY6fLVQsyMbLQ0Cf8i4zrqvfu8qJamKzGCuUWpGtFKRWPv5oJMJX1dxs6J3QOA9JBmxmn1x-SMnkvBmzN4XZ7CjTdPppREEixw00YpayGJ5dTyzxbwrwg4hrr6I5uox27RMxj2hT_q1a-2PMLWdhmkHkjAhGLn9fdieJ4pvedfFCOjDOeuTNA0BaniEUHy1gXryK_zMOygSlgqxk7JljN8P0X-YvRO8XQmV1OL7OTjYyK2X67aDcAJ_xbUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXBqcJcBZ7em-BQWpT4wfDtectS9sx7C5m4zoraS9pEPsF5v__Hh6KENfDfHZgxRu_15MzxZ4Sr8HWffEqqFFeZ-BZInKbrALqJwc18SigyJq8uwN5FiCX2885S1i0QQfabTyh8WX01rhZSCa1qfF0rJ7-2xsS9zWKIG-2sM5zlD7aDAwP6Y9JKWgnSfD6f4UA406I7i9YjUXFl6nA_BIF63AKdjUfcD6Dn1L24Av5zaWSwvPXrMP-hwa69DIvhrRQnUCn__CLyHhcTUQHbkK37PnVt9fy3cspFe8htayZ-maGCy75sXxmQGMqv40esBMbAbpN1_KvniAo4zu2fGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es4LwDuoYn_-6_seG8hPoyEXtRyG0Krr6p5NzV0Li7A9DRCdyT5dqwmaQ2EWmmeVDy8O9FL2ytPt1Rno78Dmdox_jB2tbcGKwsU_efiMnTpMQJ7-akDtO0FCQzGUXBkpPiDuJtyu1ppy-KIDj6lAYnHAIw2-W7CCDcn65VjX7QFt4LNFdTveLP762FZdbtyv8S36xaE2LP6h2vtvelUJwjXA-Ja7kVM1N0Ql-dAqu8zCkRS_Gz3ZirnbpeCDq_vg5S2I3adDjaQV9oGmGXQt-0dTEuEM5-p7y1e4gMC_y0-HcljhDF1wBhkA-3atTiFoqnGzgoB3onZ4P9kRGXLmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Dl-dpLsN7so2HP9G9LBqDgaHlUVwb2YdRh325yExSsy3JRKTCjW-vuecFhGTH1Tv0dyve-WP4zLPK2uR7n4WIYKV9jOvbbGTT-HO87f7pdPlKb1Elquzoy1exRHda5jwx4jCdjbb2uzhhNkGlr-pERIjWR-ZIuggLnpmGnsDfYBjEyipo4H6IeT0hIsqPg5FbM75OAJC3hXjRWCLK4H3dLUM7TkQRm5j8vnCumM8OT4FhHlV9nCQ7ghngg_-3H6ykyK793GHv8gqAWjo6h4I5ZiKOCBxFZ_rrzXm2fvRvxuD5tQDdEVQBIsCLCoUCzeXewqwCzuB9VVstJFFQ8DbeZLFfhuc85Ei1D1TCCcknYsmql4y_sOoB4Cgeo4R4DcHpYza_SX6yfem6gefAYSC7kXOjY0iwNrDQx45aSq5C1bsLse84HBVLcSl6ueHqKlnLe0E4Ub2Bx6WE0A6cgI5620aAjen1k2GGmnGkhQ8jhc7X-pDAOhiphKSMdAUjYkeluITWIS1HPDMMV1dTq4ry8mPm6hkXn9hZI9iSMkhzMy0xfxGOCT12oplCQzfdqg4yQzXqDxQ48yd4WWAbAn2nNdzZ_aUEH2nfq4uSCiD7vKOY06mk4wvuJvze5JtIDgW6girPdUmfstTg-2p061Uq-cyosI8CH78Q_v3SWelASI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Dl-dpLsN7so2HP9G9LBqDgaHlUVwb2YdRh325yExSsy3JRKTCjW-vuecFhGTH1Tv0dyve-WP4zLPK2uR7n4WIYKV9jOvbbGTT-HO87f7pdPlKb1Elquzoy1exRHda5jwx4jCdjbb2uzhhNkGlr-pERIjWR-ZIuggLnpmGnsDfYBjEyipo4H6IeT0hIsqPg5FbM75OAJC3hXjRWCLK4H3dLUM7TkQRm5j8vnCumM8OT4FhHlV9nCQ7ghngg_-3H6ykyK793GHv8gqAWjo6h4I5ZiKOCBxFZ_rrzXm2fvRvxuD5tQDdEVQBIsCLCoUCzeXewqwCzuB9VVstJFFQ8DbeZLFfhuc85Ei1D1TCCcknYsmql4y_sOoB4Cgeo4R4DcHpYza_SX6yfem6gefAYSC7kXOjY0iwNrDQx45aSq5C1bsLse84HBVLcSl6ueHqKlnLe0E4Ub2Bx6WE0A6cgI5620aAjen1k2GGmnGkhQ8jhc7X-pDAOhiphKSMdAUjYkeluITWIS1HPDMMV1dTq4ry8mPm6hkXn9hZI9iSMkhzMy0xfxGOCT12oplCQzfdqg4yQzXqDxQ48yd4WWAbAn2nNdzZ_aUEH2nfq4uSCiD7vKOY06mk4wvuJvze5JtIDgW6girPdUmfstTg-2p061Uq-cyosI8CH78Q_v3SWelASI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=JoZ6pJoP_fQoNEOwEPVjIKcCCOW6EWKN8jEiZAIAwV-CjrR4rEQ7QbHlLeJZav8dCjJ-yDFDiNChAhBRZ5Hh5YBgbqKJvExsPw00oaXv3RGFAkNzmECI-v-D7X6y5xpk0nb_kJGZfUy-XNlbjbkVvWm-6uI-iRQHjaQUI8_v0qE-OUg29sp0dyEdr5yAxQFh5rgVUOPPpDbLl5FpFXz88IU5bbKUDTdt1A_93iloFc6cUwuxjkhmWZ8nvG4q_Ej_1l409YgNLnOwuvSKkXojClMxoGifnJz5wIg6N8h-AyMUsqKSryl6QJq33IOZSh6gYTo28ZI722UFttc2Dq_oAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=JoZ6pJoP_fQoNEOwEPVjIKcCCOW6EWKN8jEiZAIAwV-CjrR4rEQ7QbHlLeJZav8dCjJ-yDFDiNChAhBRZ5Hh5YBgbqKJvExsPw00oaXv3RGFAkNzmECI-v-D7X6y5xpk0nb_kJGZfUy-XNlbjbkVvWm-6uI-iRQHjaQUI8_v0qE-OUg29sp0dyEdr5yAxQFh5rgVUOPPpDbLl5FpFXz88IU5bbKUDTdt1A_93iloFc6cUwuxjkhmWZ8nvG4q_Ej_1l409YgNLnOwuvSKkXojClMxoGifnJz5wIg6N8h-AyMUsqKSryl6QJq33IOZSh6gYTo28ZI722UFttc2Dq_oAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIlg07JPrWXnuPv9SJJggkmosJvIDBgh86id5J9IylOV4y7e-oVaCH5Mkp_qedsJkapRiLzNBx6fW2d7Qib64zM33TcjMQ6UvISmG0V7xzdrTEHXdlQVHboKFRToD8bjDtNFQlnGLgSgAkKryi6A3BqpmAjrQ_Hmjm2WDm_QfHR4sQX6gE9vPQVl9Btq3cZkWxXT5-A_KfBXq__MxFSewKGYJM9MB7IFB2s2BxXIIgsxIG8bXp4TKhaeOICXsNpkgpc2e9aPUJHMIzc4XNdoTAxxSi6sSZjBs7TuQqa0H1fxk2s2f6utp_XQDK0ZdYn-skPBlyt895lV5Wg6ur5-XZDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIlg07JPrWXnuPv9SJJggkmosJvIDBgh86id5J9IylOV4y7e-oVaCH5Mkp_qedsJkapRiLzNBx6fW2d7Qib64zM33TcjMQ6UvISmG0V7xzdrTEHXdlQVHboKFRToD8bjDtNFQlnGLgSgAkKryi6A3BqpmAjrQ_Hmjm2WDm_QfHR4sQX6gE9vPQVl9Btq3cZkWxXT5-A_KfBXq__MxFSewKGYJM9MB7IFB2s2BxXIIgsxIG8bXp4TKhaeOICXsNpkgpc2e9aPUJHMIzc4XNdoTAxxSi6sSZjBs7TuQqa0H1fxk2s2f6utp_XQDK0ZdYn-skPBlyt895lV5Wg6ur5-XZDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPjtrXwLmJNBxwCz4fxW0aEugBk6Be-CSiI_EKa2ce7JsgQDkl6zHnhi7O8FNuDSPe4WDnvDckhOIFRO2_gpADbJPdddCP5k6OAADcnGsE0Kd7K5xd8wHlm8P-cl47ux1pxAEp8Qu_WRyyNetCRHNa5iYY2taW-LdzIrNidX6uUVp9AIJ3XxFKOjoI0ZVMjaZIWyK2ASb-utUwUMnvNYuaH0XlKevr_D2dCcQgId-iurqcqVs5lJ78v18pvCK0s13feCSla5pDGknzmrWFuW61LE5uqSFmXb9EOi8nVszBUnkdWTEITd-mRXF8O9gR86IzX1XdlHBQ2bmHo7urmTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9rpiRzx3yH6QBhLZ6fW4cyg844HL7OKQ78EWRnOxthZJ5bl3XG8VCPa6LAk6wayWsa98O9IBKYAJllYYEn9Jy9-Gk_pbchq-I-kqrjuQl4zn_6OaEYGrLMy7564nSLVvgdvBc2juHvp42io9T63hPTEDO7KLUTBN_hEdJQho5y0Zf7a1Y2JSqydgmj-2UfWrwGZXwvFueQ3HHEkqcoa7SMlKrJoBOh8gQnivDIDtw_FYo8Vw3IsHy_KOS7JAonPtxRYT5UHfEJvRKbnzo0yqyQ7Ysz09PyBvwUfNOW3A9gBd4Saoss-weCwen97_Kuj3NuOeNuC_rVJUwDdzNXN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1f4miUpWtilWi9m-KqTSJPph1VG29nXADwFknOVSELNeehy1-dfWAGbplRntlv5fKt8tiyXBLekd36qjP9oUvL_XqbcKSMJLIFA139728Whdsy6IZEnOd0ihWPVyEpQrNf2GicI4UQXTkoTS3N76KX3j_9vACQak_rkx2ixB0Za9dAbPxa3WiHh2Wfz-hlXBaDElxY1qW8BapxLD-2CtpcSzcCTNq_A6PNvaVfCTp4t37RI52i6DDez5R_O-YS4njK1OXzg_pme6FGCk5PM99ijxqSOHkhQVwWTUdym7q82E_8Zbyehb9Qk0YbLEUiaioy5ACO4YrRmLJy-FSQekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=Wbl424kEX_UQSPGdNeQpWIcxwzOWDJmVU63Oet8QzDFY-TjSQN8d4BF3dD-2w5xSLl1U4Z2uw72q_sBd8WM49adJcGU0dT_rbBvMvIWAKNx9uxQZ0hRhwIgMce-CxtqK_DlJQACfD_iMAsdLDWj0drtvzecpJ9ubq8zoFAqhIuR7ZDiUzO--fLdIwk1YWjFUli3jymOixXiyydsdAn01rmDm9B4cefL1HaT8qyhEtoJcYxigGE7-Ki0XH-VC_aWjIFwCKPZ-3CQuSiiPFx95-j8kAQodhDXN_nDT_y1rHcl92JiZfHj-xaO7WWl26kr4nNPBg6sIdynUh6OLEiXcrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=Wbl424kEX_UQSPGdNeQpWIcxwzOWDJmVU63Oet8QzDFY-TjSQN8d4BF3dD-2w5xSLl1U4Z2uw72q_sBd8WM49adJcGU0dT_rbBvMvIWAKNx9uxQZ0hRhwIgMce-CxtqK_DlJQACfD_iMAsdLDWj0drtvzecpJ9ubq8zoFAqhIuR7ZDiUzO--fLdIwk1YWjFUli3jymOixXiyydsdAn01rmDm9B4cefL1HaT8qyhEtoJcYxigGE7-Ki0XH-VC_aWjIFwCKPZ-3CQuSiiPFx95-j8kAQodhDXN_nDT_y1rHcl92JiZfHj-xaO7WWl26kr4nNPBg6sIdynUh6OLEiXcrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMip9JxfsSW6ROL7tY6eJX9nsKaioRHLbgH5T1wBNNXfVa0fqBD8SOIOwtjaQZlT3SDzd-LoKyT5aYEfrdKrJ8qVlg8BhA3icbw2unH4PaiaR5vG3VIodo288CewWHDR7TNYRT_Broba53wtDqhgl2ITxDoR_N1d5Ec2GqAZgk68tZgG2fwtDK0ciG8Vw8oehGXQYaq25c18wrLEPu1RgTCcJGYUUqL6xm3LraXUF5GdShFX1IKh57VrvUkJbs4szR-709pwLJWY5xD8-pWdtqxJdQTbZysdhYrtUommObCXWu8TwN9wZ5U2BLCO-JZ6FG16nA43lJ5IyFClyd79eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvbILHaflNekTgRlooJ4L1OIoN8Q_EYmGlADg-YK3bYLrkQZsTHEEtWzCxOlalfQe2mt4Hi77T6sz4b3okrpoySJrjXRPwPQaouEfJ5y4qoOD8PiPatsPAbfbQVbFje0q9rZ7GkQFaNTT1Q9Aj492qObBSTDBJXKB75GMaLvSK41IrFaRkCF5J8KJO81SWiKVgkjtJ8e3e_SPIua9nqXR9mUak93duxEW_1UFy4hR6OIcWjSdWljlxYzcdXhStV4a784wqM6Bg_QdBgEa00ozS84r-jSCVOuHRCVYPAGNU8P7PvUFbe4RaNKEObU7-KyJ3CnJi31CNH8qUJdASJ8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8Yc5cojl2nejthTy0V9KJbFMK86qBT2SGl-vvuS4_nnSVc24YPoL_xUIw73emMJOmneo4jTEjvfT-9knDyH_rLS148ERvErMtdigoaqUPbE2aahuM7RrTcSQy4QMDxO67wMBRj5V7lgAYz8eYK1OoqvSbThjr_-rM30JGxX2_wrVbav2iO2puQ6jEvuFzvmuXIOL4u5U_HQPuWvQefWYWxzsp6DE96fIH3RQbnbHfywoGFYEEH9J4D5gD73LVTTWltwKX6Obc05bV7WYR73SvfgUAXuhQKY5hcBTEODRlYUY0_roS2KEIYj9mX1XmEu8bsCUhg2-_xYItbxmP_7HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
