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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_E1AQlneS_cWCRrq5Y3jwFiXuG4ui0Ii9_08ZKYtz09YbS_WJfTwlPc123MLJOdhhH_uC-OdHKggpLPBVwb53aVYVMVEBbupRct10rGikUu_egMhVBeY6Em2KRvNLN6ezMyc4cWaC9i_MxVYMpSkLayYAHulZRfai4ia-sc2bpX_C5ECLJElMpv0na-g_yK-IXmaFsCEPMC-nlvTYLcWtTKq-C_bS-OPNjqo12ju_R6nRN9k0cYz4yyM6zZdi5keXtqS5peHUOYvI2bMIJJ7uSOObqEq4hxrYxJwfmYDhpC28kK_jNsQME_sjEe4kgWMDPvxMKozXYX_KQ2tif7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5YLT1OnCzmQegSpRJdLe2NYSf2b7VYr0YnVlIvecBfvdvxC3UmIGIjDa8fqoblJrvmFIMcbYIcfdVpiLrcVR7GrFBx2Z-2p_zspbU_IBI9ynntM-D3CSOihCDNP_tJRx-sx47KUCjKkWMnpGXdnbJDEnESH1ySPRmadxRwY36cnCDTpXkgtyAbMEYNi4MjioFPjQOh3qEBt2WIEWBX3rjDhdmWcR0pYWlGcdAJQiAsGyLGaz-q7RHtaQbtWMOd6xn8HAoyPzpaKQpC0rAs0rghE-8EtqdVNfy8ieRGwF1yaftfNyBQfxXZJzAwrP_DYnOwLCzd5vHlfwNjBRyGHl9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jut8cQceE433CeJXf-9_g1_bIv0qU6giDxbpJgJVvXJbKl7UTJPo-DfH5AxDhgKeG_G32gnB-Oziab_FB9LLyGLQMIVS77wMRSQBI1wvzoX3BwIcePIUNbjDYY-UlaEM3ZhFPMfLav9CpFHj0jAeCM5I2xPghcSwhUmha0tou9OuhRGZxtVGlJjPxOhkyHKTe-2-SJqZp_WK1Oknw83qfab6U8WDLQ62SgFrrbOMRB6RNfQGFzLlplSfHIN6yM1kGCZld7aey4a9kMhapREtb2FIiWBrOX_y-Xv5KEvhkQLMzLb3EULX4PA3K__lFA16otma-1v99gtygWBggTGeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6bpaBhOneVqI4HAkwRI-n4FmRNhSz5954foGCsGClRm5ldPNG_Y0VVx8NxSvl8jqIkKjtV0aNQ9gmyWeIg_Zg8I2Xsk-sVGj5eVUv7yBGfiT3ouwFd6PDrDice1397dgubbvOTPktnVliKyLVkzhhlXzGWrJCqtCpmhf33P_3RVm5az2yGYtRipgD-AXFI491fnACJKYMAGe35SLKdoWXgjIzHNICWy63w580RNeasTSnDd218RWxRBLTzg4XL-wgTESVKJkctWumhAzDFoEeAtQDMJyjnxy0vbB-kKBFW7TAoQ64Wxgan22HGAZ9I5uXQOR47486KiG_lhVBZBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=mP40uMmyEQHrGCE_z58Oaw523Mup-TP-rP7bjuRz5MS7ddqHJKuf9hj8qRN_-kLE2-Ft5QI8GGFlGnfm_YVsvpWOLfK_tpHlXLr4zFMr_AF6sFxBle7M1h4tLOnnrMGXV2jhv4uCnJnEfvb642GB-8t7XUeEo2IggLiMvHFHRtG7vlaKmBwFLdzb2DwH9r0_YJ240ooXGaJaoquBANCs1qyv5LxLNPq9dK21j0Wxc2esbRazQgbjSVppki7-W_DFywdTmYzvxN-Xc5qMJTAy7bueGp4uYzSzOCAKgARev3QA8_2mR1TfC2pn9dWMFIf23RzyXAGqYN3_jDj_6qDDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=mP40uMmyEQHrGCE_z58Oaw523Mup-TP-rP7bjuRz5MS7ddqHJKuf9hj8qRN_-kLE2-Ft5QI8GGFlGnfm_YVsvpWOLfK_tpHlXLr4zFMr_AF6sFxBle7M1h4tLOnnrMGXV2jhv4uCnJnEfvb642GB-8t7XUeEo2IggLiMvHFHRtG7vlaKmBwFLdzb2DwH9r0_YJ240ooXGaJaoquBANCs1qyv5LxLNPq9dK21j0Wxc2esbRazQgbjSVppki7-W_DFywdTmYzvxN-Xc5qMJTAy7bueGp4uYzSzOCAKgARev3QA8_2mR1TfC2pn9dWMFIf23RzyXAGqYN3_jDj_6qDDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=oor6ZKRc4jZ3WSVFCgYhE1-j5grl4CGFG6Tgm0L3lI4V88jVFLzdYyu35bg5YFWP1_I1AraHKpbTM6Ftm223OZKxfFUlfjoq1nWYjQKsg-NKQCkgwQ5Or3jMjMKcyvvSpUns6v4E6-Hxztjrm-13iBdm3MVJe0cFyU7NjfB00P_XhunhzDVsSY4ZRr2mYCXjskB6UTCNzIQixwbSCxtGmKheJmDoWw7-3lUy868CWe_JxtEKIRcE7IPsrw4fMCxv48YWh-_6fXJ8IwgE-P3JsK5qucoGRqK3o4SDZ_m2NiDOH6W0Hz9ZLgNGURkUMHAg1a_GpOj6XRoimNuop-L2hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=oor6ZKRc4jZ3WSVFCgYhE1-j5grl4CGFG6Tgm0L3lI4V88jVFLzdYyu35bg5YFWP1_I1AraHKpbTM6Ftm223OZKxfFUlfjoq1nWYjQKsg-NKQCkgwQ5Or3jMjMKcyvvSpUns6v4E6-Hxztjrm-13iBdm3MVJe0cFyU7NjfB00P_XhunhzDVsSY4ZRr2mYCXjskB6UTCNzIQixwbSCxtGmKheJmDoWw7-3lUy868CWe_JxtEKIRcE7IPsrw4fMCxv48YWh-_6fXJ8IwgE-P3JsK5qucoGRqK3o4SDZ_m2NiDOH6W0Hz9ZLgNGURkUMHAg1a_GpOj6XRoimNuop-L2hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSfhQ3TvPadU1wv8Mz-3l2QxgtYtENS00j0nv1cy1mZJ1-uX3aMmRj9TAdQr6sDFeQCWmNQa8_DO01thSkS94_6TG0cX1GcsTFNsZdVUEZiWN6c8Z29GXmqiTQz4EEZKSSXFuJuivpk4Cjpgk0_M-e2A3PAzlhLWIWLUuxbbVWgGt1wbXwCCn5DITrLYzUf9NDsfjryqjQ5NV9UXVYFJt7w-cZcJxyXbm-PViaO92WZFaOfqDDNg2ZNeqwGXAukZW7oLaHCu5PZHe6N5Ihwf7b92GSLIo7bJ--X8dMoLVBP_XoOjMeEe5hKdz3liwYRN2kvdbeOP6TUrVQqqSn92YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7MOCXZCd_JgXyViqeWZUMaEbgw5KiBup0Pnd09-H9Yv6CQmZAyCSDHHxNjJuPmeSDnZavqzOMUthgEueqtwtKibYDg9c0fk-hvuN5tSL_WVOhfEMr49sX1JUycaHq4lHB4VZgDCQZbuiuCav69uSWrlpw5jqxas9940kdsqjf6miOGbBdv0hQy5iUp2JH-HYMYYWhjuLZyiOk8qTfWxr4RQrJwN4ve4rQ8YyP2W_ytTnDGfEo_qy4qe1cIKXDdoOkrMExLIOHuNiz7M3sHc-T8TgaPbLXavfdTdz1rmkBGeHcpZqadihBXYXLIez88ZNHKpLD9x4j_wdSvsrpmSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Ajfb-OtcHpZIDaf63Q9jgfRhIpAr2-p4q9b_mxx61LTP6vRpeyet1flowQrrAjq8fUG2hVvAL4cMMz6SIlA3ihl7cnxjzbpxOMEg8hamKBu_fVqUuAG1pjwOSxnEzWPZODOGnuqezaOpYOasuUNsV11TWtnH6P76gjgNJ9DqoPRUIhedJxvxy_frL--4--3vXu6TmC-mPh-vFfi7Ftu2gNUyjs3bwnhuB9kKUzvxYvTQWaKvYh_OzbGQalk-fjZ4thqePyKguW3l2jSwY-0vdTJcPwRrUlwZomv7jv-iz9kdCojthnfTbL9jL5z6P-ESf9DFM1smUzyXEDs7-ySbhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Ajfb-OtcHpZIDaf63Q9jgfRhIpAr2-p4q9b_mxx61LTP6vRpeyet1flowQrrAjq8fUG2hVvAL4cMMz6SIlA3ihl7cnxjzbpxOMEg8hamKBu_fVqUuAG1pjwOSxnEzWPZODOGnuqezaOpYOasuUNsV11TWtnH6P76gjgNJ9DqoPRUIhedJxvxy_frL--4--3vXu6TmC-mPh-vFfi7Ftu2gNUyjs3bwnhuB9kKUzvxYvTQWaKvYh_OzbGQalk-fjZ4thqePyKguW3l2jSwY-0vdTJcPwRrUlwZomv7jv-iz9kdCojthnfTbL9jL5z6P-ESf9DFM1smUzyXEDs7-ySbhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=KclURl6AQr9lcUogeYv5HWjBi5z-an7Fw98nOS_HB5GJSqsaHG8FMZK225WhHV_EFjStzsV9Mn0ypo_kdxOK7EPP3oPEZBpkRBpyJZ2Qzu88vGfkLP82WC2A4vDql1oNhSnl7OWuSWJMOSUuV8oVqM0HyYgWznMJKOPxeIO-XTU41FsIM2OA_Q8Oa3A3S-IMC_WziToV9K6I3o9AtBWEG8xgO_puWMBAqH8gMCIGYdM6gvYxP84_Z4XSlhdQPMPYU5mtFRvin-FmZsDET58wysF0KH4nZesZEIBE_x9CRgH7k2HZH6GRunKNlPeQFEYDRdPN8S3z7-s2eOWspPgIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=KclURl6AQr9lcUogeYv5HWjBi5z-an7Fw98nOS_HB5GJSqsaHG8FMZK225WhHV_EFjStzsV9Mn0ypo_kdxOK7EPP3oPEZBpkRBpyJZ2Qzu88vGfkLP82WC2A4vDql1oNhSnl7OWuSWJMOSUuV8oVqM0HyYgWznMJKOPxeIO-XTU41FsIM2OA_Q8Oa3A3S-IMC_WziToV9K6I3o9AtBWEG8xgO_puWMBAqH8gMCIGYdM6gvYxP84_Z4XSlhdQPMPYU5mtFRvin-FmZsDET58wysF0KH4nZesZEIBE_x9CRgH7k2HZH6GRunKNlPeQFEYDRdPN8S3z7-s2eOWspPgIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4-I9aH6OrEIo4h_DRa2Y9lLTvPmBg3NMpWmzXOiuGZnLujcNTvKaExKm97pSuGMqSoLpatoAWfDyfCrXvJcOwO1vn4h8JjVDNDzVaSt9k0slesFvJhG1WK59RNR3QKhIETETz41pXAbGtFvUzJkeHJDndlLMYw-uXg5M2rZ_411ioPFaS93GLvlVgORkO_o7tzBEtqG5rhem0JmOfZobh49AT9spr1Mr_J7tI9rOFQJQQv6Z868AMtseB6jGaj5NJbRZ_-gOxFyAaa_TJw7zS2e8oNl29m-BOKLnzKEjP05of1S3npYxeNSvJL4A4pjtRox16OMqvF5Uwb8HhEEhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laEWJyI6m2eu4MIQkM_ZSIRFyrnxQKrLrp7mEDWGJqgyQ5mOpXTfmf23Aq6Zw-IaEa14HqtwOL7nN4rzfGGc87kRkEWTnKFHLgbSS3ERRtI8vt9P72rR813DiVPRjp8N1yxqO6-579FNgGk2F_hDzB0CtWpVMSRKc-IMItq_r61x8-jdYAptnXAV03j8pd-gMLCwNbTqDKXeg4zEUMAfpag4NhflsHD858qP7F2v7Ua_BZJlqbRYAhXBWlGLE4ld_SvKsXeNDI66ayrxzCiTa5HODzPd8531k_sn7QaPSispwPuy-jSlKMwtEBDZXizkpw2tU6AOzde9dOzWBNJT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPztCgLCKdfohJfuhMNHrJ8PLcpWED0YxYdfebAMVSGUJjSoMLqZR7JwLxOFM_JPXbeK_lmGR6H3KHh0CyvE3GjGWorxGQ-oFwBYMmLh6yro9m3szasa2LABE48o9xkNmz8l9xP-EkjUieSw_9hXIAti9agQ3ZngZcPqUyTYRwFCWTWFtHkknoz0Mrr--ppj-vqI-4TNQ4MCd_JGbcfUs4nQriKKLsuRWka0ZVTxBMAvvmHsN_dksqaQrdelN0cW1BL_BgMDpmw6gxzddbTgcfiGKoLTRbBm7ka6-vN0SNmwbwjRrktXVFeMmSMV8Yll9PzqaAx4eag4qZNW55YHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrNPtHIN21tarBVL_vkGPR_3F7CtijfccT-5GAA1THF9FSYKTOlMefQETM0IY1XUl_-72cxtBWC6qCsTWLl7kTW2nygv5HU7YKJn9cex8zhOG8kP2UYTzka85Ql-K_0LCs8IgCMqlzkpToCNt5x-fYevOxRCxz2p0JOn-p7S88_RDFoc6E6QESCP434DprNNoAzzIu955LfGdMjnfG_kqikh5x1tEpa_3lPYF2Znxddw_oVS3nUqW5mSBa0R4up70AJcEpe457sgYTjqYcAUetPci5FFhpksUzJzgyB4Md4UavHs0JvNFMoje5Ai4Xpf2shNJ4ET-BkEXYenLBBNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaOB-X27250AuuyCgloFQx6Zz1zIVJb1c1Q8zeszTV90NhnsZeu8EeqKn5ldhufCWtELtOyzr9HVQ_W_8RZp9yErt1jhhBI3DQ-fa4t4Ip8FUVqWmVabyGgVHX-9KrnhSfsQipmnTg85uD4ogy5Oow5fsBNdhXb8tQkPv9Y7kidwvqzctj4QYWM7VweSQG4rYVxf-TQQe4BaB-2E22GynHo1m6f9eKACr9QrCZ_tsm6uX9ZcF3kFnKYiSLil_wHoEWd3zBsG0ICEcgBp7ZQuRm1OwfEtTk_HgA5tCWLnofv50DoJciwzRpOpuTNvOJTRyKo48jMXZ-Vj8Mw1Xopmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoieGEG6DhdYEExtTWWHuwOFVob1a1S9Mdfxp_DO53E408OjmZiEO5UrobJGRoPYz0-wsz9Pe6Kl3cXgmGl5DM9Cyvk5CtxdtINEUeqnOUJCeWAIYowor-c70AjAsX6nHkMlscn5k5ZPiXtslURd0cMkLOKv5HIU1wLZttArAzNQxkcJj4EmDU-9O2ezoyfWF_n6tDd3BxIn-B2LmIZNnFkhzEGT0K5V4GmBYLl25ZqEZdYDFrOSAi-X8FC2HQutOR_rC281GNCGDZDtDh_FnSNYmKVGqhmBbUjJONvOTrSgiNJWAr0bBDuHG1TAqzPmpApiykZvNX_oyUzHUoYnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LajTSrDz_ksIfqNvzegqFfSV5bOdCEWVXhxvyjikbFMvNhzByJw-WYVef-x7dJIl61LmUYgNplPeRePitcUW61lTOrsbfyV_SvtzeGTSuKEuQcjYpGFXX4Mu6MK-__PYvXA_hDn8mnBGeY1dRaiIFbUbgj6WiIUgp7NM6TIdPN3ABKdV8MMoHGqXUmA15pCK9ef843ChBxRJDsLQF20yWwuMoGc6Xy-KLg58UZG4ScR0P2j_843m0NTkhE-AUn6WmHQzS2ut1humsypAAl9XQfNTGgCQ7rHq1pGpejSzAlkNQ65bHWukvFez1hZCoSjYAYjSAHibw-uNkHPSlxRVLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkEWpHxrqg4gD3B_EAwyieexkTMJjP0TNPomP1IVshjUkml-CmsoaPdqEP0-sORBWnxulUEHTn8SgXAM28ZefRkY4loXo6P2G7Hp7oM6uu2B4Pd9HiDFURaq_IJ-m17bCaNozFB8OB35tnIQNWaKljcCZOT0hXGmKZdcnJMKv4q0ypP0jh2hEG1E4Yv3Rr8sTQGMKxICwH-x83rLRb75nERn89SOcYAUcaTPQ_U9uDydpu646rxk5T9NilR1o5B3xZQSylX5_zmvqtWxKvpJugLuS6mrgLtafWzzXLd_aj1pameNTj7V3IOr7a51_VP48-zsYGfj7d1VILUIgZHkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0fE4KP3XUkBzQmgmtXmsFV8RpBq92fJ1dHRF9usRLCButhHfWaU4cw5GYxF3s8yKg4qIJSc165uLFrVWgVC0EFIWZLvKytjBdh-YE7MEUwd2TBKYMwIDcukeAoJBnI8B6QfdceS-x6C0GGzx8ld-S7CDVqYfx3J8o0ob8_cccmXSpLQq27ymG2y0dFlWkgwM8SI0g-CHo9M5sbX0MbSQHOPlUrC8IEZjEUxPys-H23bypnTIqehD28QTQLMxfhpw7TAvhhQMgJkpkuh1c6u-lXMuMHHCQKQ29_Q7oD5e_A7zs6Je-05f1xd0y62L3lzj1TqaMIW3OvgwVZ6QOeR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=KecuW9FcbIVn6Nd8vI7wxhthTpB5IJnRmYbcRZgZSf1cFW-_3JC7fYbwUKQg3jVwtABbWxxU5PmiXg1VPn0fJg2fnXACvB8LXRQzqCevxUfnlwb7GkqF66oQqw52xL_FMwXKwrw59Napv3Jwgcw9eU3P8UmDoLpCAZHpiIXrlZ_3hsVummdXo8tt00ieDpe_kcwsn1l1b6N13C1n_Q4UzKi0yuy-9UMNGk_hV0sEuzZIOHdExT86gqgNPlpzz8yMwi8NNArfthxqFZax1YEpPTLaujbgUCMDPKwaiMQ8HJ4uyu3lurAKxh_PCGm4NS13Rmp4zphtE_vFS_VTymX2gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=KecuW9FcbIVn6Nd8vI7wxhthTpB5IJnRmYbcRZgZSf1cFW-_3JC7fYbwUKQg3jVwtABbWxxU5PmiXg1VPn0fJg2fnXACvB8LXRQzqCevxUfnlwb7GkqF66oQqw52xL_FMwXKwrw59Napv3Jwgcw9eU3P8UmDoLpCAZHpiIXrlZ_3hsVummdXo8tt00ieDpe_kcwsn1l1b6N13C1n_Q4UzKi0yuy-9UMNGk_hV0sEuzZIOHdExT86gqgNPlpzz8yMwi8NNArfthxqFZax1YEpPTLaujbgUCMDPKwaiMQ8HJ4uyu3lurAKxh_PCGm4NS13Rmp4zphtE_vFS_VTymX2gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=fZS0RJpX7P_smVCdv6sy-YZO5ctjhCep5bpHd_QobzltPzDmtfZDHdc-3I1ysM-qlHMzKIl1vRO5yzzKJMnH7I_PsRlYnOgGmPHLZFTpNY2ym6smhnPDKlDGbe8vOBlIitASafqnoSClgIXJw4WxGWWDaBxeI0gmUNKqTQj6V5CGN1WGbKevYi29n-8Ik4nDzE2tUyJudm7TmokTGwtWgBovg5nAB-zUturStmMU3R1edKBpsFqK9VntbIFr1M0vNk_QJ6cGQXHXGBkT5vcUC5lpMrJjd4lw50WWxI6YE5fX3CT0JhJ9k4Up4jhFh1OLGoQYXd0gy2DJxmuKbs2hJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=fZS0RJpX7P_smVCdv6sy-YZO5ctjhCep5bpHd_QobzltPzDmtfZDHdc-3I1ysM-qlHMzKIl1vRO5yzzKJMnH7I_PsRlYnOgGmPHLZFTpNY2ym6smhnPDKlDGbe8vOBlIitASafqnoSClgIXJw4WxGWWDaBxeI0gmUNKqTQj6V5CGN1WGbKevYi29n-8Ik4nDzE2tUyJudm7TmokTGwtWgBovg5nAB-zUturStmMU3R1edKBpsFqK9VntbIFr1M0vNk_QJ6cGQXHXGBkT5vcUC5lpMrJjd4lw50WWxI6YE5fX3CT0JhJ9k4Up4jhFh1OLGoQYXd0gy2DJxmuKbs2hJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=to6B2g4p-2TquATPDmLoY5uBYpr4S93Mk8X5u7p1J2uMZ9HsMSpTJBYkThr1N1hPQae3Vy5KHvlxrGF6LiVqgBN1yxHwJ8kyyC0gpW3JpraG7tk4a4SVAHZ3VIZ7TPfZSWt9nqibeWRdbZnO-J-FtDUkuKGRZPbk6Msr9E-OXGszN4b9SNB31MuCbO-SXllSrSxMeRtlQLZw-wtcW1i9UtQYMHlpmxug5aqTPVB0wLfXPnMAG_6DdZSy_QIWcTN0uhPO8mhKvPEv8CO-qB2Q-re2uDHU6S7byn0y2wk41LUctN7htN6vQArYCveKxJr3D1B3cGZNiAiWegIuv67dGV3TEZTmE1bpCZ1DaUqX8XCNx8SaDhks6j5VkD-_6pVt2BQzfGFB08O3CbFc9BPBNlW75fbniublug8c_8grvqmci0lMOk1-JZE-Epd5pFwmC_iRx-mVPdqfU-8AD43dcxYJapIvyGlaBemRkMZ-NK8LyLjb3lCAgwaoWwBWIoUnsASytLZgfjLON6LPBKH8lJzJUYnnyt9JcQttkDwIcsI8NBqjP36M3FJO1nH7zY8S3QVPF5uHNs_bcJqNwUtHbrOKuLCQjLxzxp_CYsIRdDXpMRoqPHqYccqMie2zFMy6CJ1LSTp9dfa98Dr-ERZ--dmjSTu--B3jB1Kp1IMoWN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=to6B2g4p-2TquATPDmLoY5uBYpr4S93Mk8X5u7p1J2uMZ9HsMSpTJBYkThr1N1hPQae3Vy5KHvlxrGF6LiVqgBN1yxHwJ8kyyC0gpW3JpraG7tk4a4SVAHZ3VIZ7TPfZSWt9nqibeWRdbZnO-J-FtDUkuKGRZPbk6Msr9E-OXGszN4b9SNB31MuCbO-SXllSrSxMeRtlQLZw-wtcW1i9UtQYMHlpmxug5aqTPVB0wLfXPnMAG_6DdZSy_QIWcTN0uhPO8mhKvPEv8CO-qB2Q-re2uDHU6S7byn0y2wk41LUctN7htN6vQArYCveKxJr3D1B3cGZNiAiWegIuv67dGV3TEZTmE1bpCZ1DaUqX8XCNx8SaDhks6j5VkD-_6pVt2BQzfGFB08O3CbFc9BPBNlW75fbniublug8c_8grvqmci0lMOk1-JZE-Epd5pFwmC_iRx-mVPdqfU-8AD43dcxYJapIvyGlaBemRkMZ-NK8LyLjb3lCAgwaoWwBWIoUnsASytLZgfjLON6LPBKH8lJzJUYnnyt9JcQttkDwIcsI8NBqjP36M3FJO1nH7zY8S3QVPF5uHNs_bcJqNwUtHbrOKuLCQjLxzxp_CYsIRdDXpMRoqPHqYccqMie2zFMy6CJ1LSTp9dfa98Dr-ERZ--dmjSTu--B3jB1Kp1IMoWN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5G_vRRpfLA_qW2xkEroSuY4VcS02L3cpI_ApwJQtMc2L4qfH_seGakqyEfObyrO2o7CDYX9QNDkWQKzoAnXSTUrFsnwMUG0su8Uyl0twsLDxK7x9HBfde3bu3hBYpTYIO2YPv0GTal7gRIQ192x29RnnGzVsH2kkmJKDtjLxz1diXIm5DbfvrxdNCFKqJ3KLit5mK4clhQdYtVvA5Bi9CEuWMW2oPYIlh21OjdEn-g3EuMCrp5iqDt39SwpDZmaHlvcFmxRkKwu9n8xSqtyGwga-uJQvcQbRSdAeoAqMUcsRz3wFymeEsiNbatH9dCuUVfwnHQGQ71nz06q9ywmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=tJ4eeF_qOz8CVk97lSAu5Sg6I7zoXr8wocHVchjwqieoK7jseDyFfnTLo3AvN_91H1qmKRhWi0sshr2EObbvDWqOrxibxws9zRuHOIkCr9IRhk0A78mfNX82k_bkQgy-dMwQsBXkm7A3pT7c8rXAv4ybzKbxqqLHElfONrWQ5uz9XSBC0d63y8mbLp4qnb6avMEdFEE8XoR_x_6xOgd-3NQNOlN5AIXITDNOnCG8cJ9KCCUHHlDCBaFOS7WJpmD50Q-KZsk5xdTb_uzfu5Dxut8omiWUsV9h7DTxeSxkGdUxIp3lW_wVN3eiJ4h6UJHDcZyhPYEpirp2BP0OBGN2Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=tJ4eeF_qOz8CVk97lSAu5Sg6I7zoXr8wocHVchjwqieoK7jseDyFfnTLo3AvN_91H1qmKRhWi0sshr2EObbvDWqOrxibxws9zRuHOIkCr9IRhk0A78mfNX82k_bkQgy-dMwQsBXkm7A3pT7c8rXAv4ybzKbxqqLHElfONrWQ5uz9XSBC0d63y8mbLp4qnb6avMEdFEE8XoR_x_6xOgd-3NQNOlN5AIXITDNOnCG8cJ9KCCUHHlDCBaFOS7WJpmD50Q-KZsk5xdTb_uzfu5Dxut8omiWUsV9h7DTxeSxkGdUxIp3lW_wVN3eiJ4h6UJHDcZyhPYEpirp2BP0OBGN2Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN0QwjmEvhaN7Veu096yuq6-TekH8TD5hxlU4ktouh7srbtxjan1BaPNbKK2ind1gnaqIpXV9Wf23cDF7Nf6nvohj3v9a3Pi-VTAnF8t8di2xMRg-V6h15EZ00RFAveCaUMl18HLdu5bTj1Tx0ddOOUdyJd50s-gBTq4lUd2nGgDDFXayNgkTYETiueepfNwVf9afgYb8acMAN1PK1fpnmv9lpLKyC0k7ls6bxUzx36U9mWeijsanvWV_ibh8uCSJzECXEbdUSkNv9CO8CG8NoYvclxm4UB_Bg8IEgJhjvU6gL_PpbLRA9v-8CrrJG1M6X4Giu2iPCPvAbMQ35luNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMgJHd28rANGQ4WFPx2nfD1WKO79Zj9i2aMgcnIDNKeh2pBm3kq_5Ojf7VYmnJSXsuYQEKP4oqflty-zVZXk0NfQRSvlm_ptvMIt0BdMmGAhYPi5E7NvMTYcXwIq1I9gwJBqnBTvlLuyBd6RLcuuhpkNypJRUaUA-EmxtnOMiFBjdZwMDV3II9wb2jL9QYjAEBEkwW-x0DHbLHQ8FOw5i1QuH1pZVYXKaSVqPVL9WtmeKNzo714MCzmZ2tjyMstMo1Kj6g-3Tz83oxvCb9A2JOrHgT8c5VFh23wJzGwDi4m6xgKaU5katWMcN88wmDIn2K7_0_zOSaBt-Frll3x0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuiFaTceQxlQcMppvKisedeVS-YuOcXqEKqY_EfrlJ_bxWEXMkpnkjKk3g8WrJ-83Kv4PBd70YyfP5Q8MLZqfa-UYI9rxdww1gyOQM-lcoUBcoRYx3fgtH1y8oLjoafTgIwSsP7-lUS5HAyekHaQYuD1WaWrBp2M_BMx6vX5McWEjLKAROUzYiIQVXgARa6X-TyT9hvPp5IFuHfdq9jcv_KBKaViWYM-VCDKP_LTND-HTqisQr4uhd3gIJwhlaP-LX6wjc35G8b-Bkrk-P_vjejGZYlbrH5Ppm5E_Hdwxyhb93bmGsDKVgXauU5IiC-mG_wk0QaoBqDkMOmAAOLCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIAGS3k_fCiWbzJ8OK3IKtChu54zPt4NQCs1F0D1p-G_BvQWD369HsJ4T8fZzyXj831HsiJC6FYpAtwHLYzx8ngcClNqjGQ-BR3YRpzhmz5PHN6CRdqqhDQNgWy3rKzgZynprOQY1tord_eyKI1gHKrmAM-aHhHb50Z_RgDCgUvulcKiFCNjQLN8A4KmUZP8Ly_BAk1-h53C6CT_2xBoAxqUOrZM1TtoehWwpvgBoyqrUwiQ79Cpyk-BxrszC_tv_wriKShC_-mxkwc7-qEyevqEYH-078sl-Ls8oly00NFb9NySyPOn-o9lcJiaep_ycmNSBDL9k8z14TSlNc_MkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgK_CmhZv25aSPsvmU8G4-dDQp2HK8-IriZ1UtgmDtRpajISET_7UmLjeLhYOK28Z42ViFzPzrlpR6EhhRBljo16rEz-AgOaSlFjgq37bX7h-1PJA-3i2hoscNRLOLGqtq_W6sswZ-42WSC9CJsrp62SY7gWlRGmqOG-Yv3S0uE6tOFc1Z5SU1n1CtLlaaIClbGx_xAIs6iPa7z_e_tdQ6-6i5cTsNNWIRURn7IfoVUeoqghKz9dLmTUgSo19gfVqODEi0LgJ7WDZI9czzHdZhXQegRRVj87eDqLFVHt24KEdlS4qQc4bNo1PoOvCORX_SSF-GEx8m3RUM3_NNcrcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK4hiF4ghOkpNSWi0XRT1HGXKfhxPcz15tyxD1Efz6rY4Lrm1TApqrgW8ZDdMz9g1jy4VuKyEAtem6bSLPDVrnduxMkDz4Pn2Skwsut7BSNbsLe4s4Ed_2Pzd3HDJswj4PSDgdK-R0YFmzEDEXNT5TKQM4tLCwnNVureCUg1Y3jGdQbR-_m8GYOKKDebvcGVIP4Cq5K9bw8nG3O4Cy_8fFSyTdAFJb7qnQLMHgYp6rUAcUjQZ1uQUObhTueFrvjkUUiP944f3LO4fX5xk9xUAShhec9pq_G4hUD1JRTFEQKDaFcVNhgMRedJFrIanzwSkYJRO6I0RG5H8Fmf-5UDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuNQdfvrm52BjKPnkIN6jMfTBwYi0TPLgooVK-4ZgfWEGxLh-HDkN78E0jWO0fLL5X3QD_y8-OZP6JogGrrVp79fUq_rTLyaqyDZZ2z1dH5q9Kb5WaoObxYJ52ChOHddodMUFZ7DKW7opN3QkEoBySRJRVUacZ5zffpwB1GCs18qG_Y_9EoH-HFD8wZqO6aSIScFSK0gHbslia2quP37NN7aFk-CsXf0noPj56MYPFx7ihemcxudiwp7dlbpHbXkOkAkf0HGtMhTXdMukmz6Gn32Bzv1bw5zlnQmYtaIzrRZHqJ8oqVSHgCy6XmV3Y_nw5fhXP039e4Wmu9gYQdvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-xav07vge0ENGFhWZHQopAw-SOjCbpG0ntYyrI2dq6wvL4pzJr-BFFJ5xNXtW61iCUt1s05x2s6IdiJpbzHK2q6EPt9csSs8l5PRab1whRPCH3H1kjxnwdb4qpCKELNyeFM0D7rKCXX-A7hFYQEspwQ5AwPT_RwqV8OUR_6ZuyVZgLza-KlqJwp0ag1u8yEys16-i3E3RPJHSrNvGyN4dLa4nuOg5j8uXyuh57Nepnhdf8eQ2pRBbDFZEb5QEmjgFn6Y1zZxxIOnPVMahA8tg1vtaTa11S3rnR3-IqLkteHriIWEIPVAMVEWx7u2ynj_5DZTvI-4-C980dGBXImOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7jsLTKlxIspEFrhUC7CdNQMfMF7OmKYQM3DykEdbYHaV1F_NwxtNjdOoIMUsppkZYI32cnvgBsPO-SV4Qhoe4L3AHGzCocLxkebCfJYmtnFsOL-j3-jM4cNeARafgQCsacwD2g9WbQDkuvSr2Nh8hQNQJgR1rnGPifIagtM6NBSdo7HXhdnYH8hn-TQ7SibRzDok8bIuxGogAqTRRKyT9eHXvGsSALyOqA9hz6UbqU5ItwHZHS8dKBhOd615a8lLubwC7PiuTdbVxEZC3RimEB--fF1l6TNY0dOXbVcPNiVv4OePqEs6iNpjtOo34b7lZZaACrTAYP7NHjRonVvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWs5vv_Wpc-i2yrUXjwNycQop8CPGIjbr1wMkjZzRV9zSex0FJaF8GWxc9KNXf4JwkiKUnxVFP5WxI6v6AgGZB-C_W3Ej8wgCdViSEG7sGPs2ebVbl-qn_0tsUt_LYGcQQXPEPvXAyHUwonkTFLB07P9o5bRKeA7Pe8mewI1R6A1p4AHTfiZ4Y6K09rLn0xMjNIhnFQLzQt8C_qHVCaBl7VNcqZxf8hqAe-0YLqPB7L2KQ-0odwah4EAAvN96p0plA9ZtKUs_-K2RHsOgdzrant6iF8I6zfCnZHp2uhg-oUKYOmGzTi3KqhzQBt5q3Hv7T8-1B-PN56UQffp7U1-bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwNfhWS-mHYCV57nYM_OfXDpTc0rjfTgWLDTLYGoCLcVAUrYOzeB2mWjOKm77F31wmBrcPQNZCxKdCsuKz_Lo4sftflqDWleP7bammHrLCGtUkdx2ADbRCPbpj9KyLLo18lVIKrBn7mMg8cipWouT-zs7Or5G24nS0CHlq0YCvRUp3XTLACeskAadrsM-Q9dB0AVT5TDycVYDwGSrbXwaRAsdccKYf7EiZrRT36GcQpNN4tNjg8M45h1THNrE9RjYmJkfUyKvrSJ8GkWzzj3NdLNqYR3s7TZPB1V_vD0xMg517qSbKSEXJ4VFY39S89wlk6Br4RnBEMKxwLEcxh3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsG6_WxcHyvzqoFvxwrJtHazuqVJ_ljjja5qKtoBViUw_hMhw0YcLuKa89-Sc6F2l4N_0ujTgqiDIAeov2a15JLhS4mMjW7nR1kwI4d3CyY5b_Q3uuOK85ntbQx03IO1xKABEGokf3jdZS2b-J38RhezpuR-EYFLPLBnt3zWKX62eRVBmLAsB9eX7Sbz7H5c8ybZLFM2gaWdmpckWWarf74aM4FrDFGbHMfhFg7PtIHH9DwhrwR6pB1I1tYL4tpSME9PbZStJA5rF6LjyBumu60TB4T3r07V0Vod8PemKlcMImTC0e0pCGeU8nIINOgL9krmblj8dtUCAFiEkIUejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFSvQITPC99SIxigg2F5fLB88M6PN9I1NQKHQ3Uv4a9aiIrBdiXUBcpVOZbcO6f6BqNy8Qijao4JUfqeDO7Lr-rE0R4FersRrvSGKHqIaIUv1GwsR2tTAmnrfsmZ_AzmNpfEm5bhMkU-fBVzki0VEw5UV43b3-MPQ3WlmkAsctwSNYHRTSHXg6MHJ49S1Urvpu9IC6IW8EblESyWGX-C3C0KuheMRcVZ4jmmCPAJovrH_sI4CJikzlHOJPEbS8XWHN8B5dK-0k8F7fD9fIPEVTkxylcj-NDGpJC_NfWmjohVmEnbI4z8OPyXqQ0uEzDHy73Dafu7PbbCIToxv5tgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gx8TjAMmJPaDhSmAokObu6T-HhOFxI3e1NQIqisqoZZgWB-jHBkx6oqbdYFvMkxOoypTitDYYrreH1LQRfaucIGUilIMQXxDvFKK8ttfvgapi6U_fcZfXfNMbmfKUa4wdQwHhv1k4zjIGkymxtZkEC1nd7PMBqQlVLXugErRh69vDtKRxTWhbkOORw69JRwPCXsblZgrtBb20kQGWaLwDWEBVoEnYggAt5blYbcYStNnlpLB3yWvM-QzANuPFr1QnXLVFTJmooA9MM76nMrWRcrw1PY3LYu-e9jQ-VSy_dTJlzZzHELeG1FrgSAx9qLelz9boVG17fibLAUXXy7YNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj5gE6SWwdk9fjHIliWcWSZiIRUK_w-s-Ttp2g4SZJvnuxpta36XLTndqzcKfz-l8hOE96Dar-U0Z908c5oaMmmcncCzKFacOSCmYwm9Z8z22969Ubia1ypWB7Pdnr_emcs-HPybIpzXDEJWTVKEHxqJL5uDmyBZzOBuEVZI9HImciEH9N0yLh2PnmUiOcHiQcqdNPQ35VfIs9cxcb4_vneWxej7kF9_aGJu7c_gbDNzP39vZPeC5XtKDwJ1ljRZ_X6n7O8KyJmRhubl6sinHn4Huu9RNPwvHWvL4lrDEYnBceoXfb8z-ktmQKEBxsoUkl8tIStj4kP0o1qznnvemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPu58QvAbUClYnhRAavkNGXhwQVH-t3d9Y7gHvdTvEhn9nNNJ4-RaKBf37rWXgek_Gn0yRRt7ECfsCs9OB8eevulk4gz6UUXgWYmxZ6iPCibIxr3UHakwc-jlFtJn7lkMvfuQ4R80koq3BvkPR0e-3kFqfei4E4wjLir5UVPpGqwaX03wRoSLt6OQ2twvffaMe8JXIP_om9vIP5wacALjdYFOQoB003iCQMZnoehxvT3pSs8XnGDul_KhFu4tHIYqHYAltRlC85oiF4YjGuwy5H08KxhjJk3U4MykkJYV5s6qvq3v8s_tvPGO9r39IRJDQfMEk2wKh9gsBmwFaDPUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCJD6BYnjsh_L7od3wRx-PZ8GWr1awRQPWZJIM5bshC733P7S5wEXNcdgVecBcX_1WanxNV6aYo7wRNp5uaSG-Lfk7Sxy17Ud9DnivokQvI-AntIUEt1NNlSGoHX_-LitsN-MxXIXwYbdEhVnx9mFf-ryJQ4GeyqDBG13rVPEM5EHKx5Cwak4T_MJkLCglhDqulU2C4g88DFyE5wxIMZFcLOGDaf7VDM_toobJeiAOcHcjm3VeWLvmKmrONNMVXC467SnS88MpB2cVTqd8q6s2sG0jLVwPGME7mUox7Ocr1VX5etFKyk1Lmvp9x86miiHhqSYKEzXtRvH7XVsIPBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=lU8uvFdj4OZI2KLNOjPZjJ1xsdriXsfCcfGxLMIFMKArUHVGqFL9DM_clvk5MrwrsJb-6bcXyGb-W4A7BT74A42BUC5hQvCCcUJYvefx73HNyqFb7xUUoPqmemzTi7SF72v33MSDcrkTwYOepFq7agfi_Vt2OZSaRIQYz7VSEQfdgMbJcGLi8YCce4DZrB0Tedm7oHUR5rnhSBMYZ8NL7zJ3gmrZKsVVkHhhdkpM5r2YwmiEEdHEHOct3mHRUBm7MKOnyCYe7iEr2O5hN98b3B4sqApqaqwh-eSlcZj6CUwFxmJs6E2zc0nXQ0tPEsVHvYyYykbHVSnFxqsxZiN0_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=lU8uvFdj4OZI2KLNOjPZjJ1xsdriXsfCcfGxLMIFMKArUHVGqFL9DM_clvk5MrwrsJb-6bcXyGb-W4A7BT74A42BUC5hQvCCcUJYvefx73HNyqFb7xUUoPqmemzTi7SF72v33MSDcrkTwYOepFq7agfi_Vt2OZSaRIQYz7VSEQfdgMbJcGLi8YCce4DZrB0Tedm7oHUR5rnhSBMYZ8NL7zJ3gmrZKsVVkHhhdkpM5r2YwmiEEdHEHOct3mHRUBm7MKOnyCYe7iEr2O5hN98b3B4sqApqaqwh-eSlcZj6CUwFxmJs6E2zc0nXQ0tPEsVHvYyYykbHVSnFxqsxZiN0_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjEX6TdRoKL1KAh7W9fgOIaEPop-ouN4Y0lkvtxkkpcXhIjUG3o8MR1EiCBz739pIBo6KJzx_eMDGnCvaTfRAkgDU0ATLH24CG89TqUY3IDx7kCsZ8-beTj6m7KkWZoqu0V5D4MLYginJBXFy0wtoObFdNr2ridTR_AHzCi752kpgR_lBaYsH6nIthh20o3qgZCH0J3OtMpfsvcGF1f0wAk3IhQlCwcykR5-HY3PHhF-YrD57Y02p_wLjskyLwWIpM8mqleVbcnYssoBxCUIY5mfsNANqkg2okVvNd9ER5J5brrusBOxn3esu49TDqLj9rUUrjc_NB1cgnBso1122w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b06dN9hrqW92J1YqKj8g4mVsiwnZP2RxrFrkIHSvcUyRcTgdkMQImwTEw_w9hSp4CAidX67MDDC1Mc8p8g9U0fVuvui1E1QpCzkBIWApKfbgjg5Zi97yIZU_EDqsSn7BFGdsYPmz3tfR1sRk4euQ5Sp2fwa_o6Huhe3N_4dAANF356hqCT2co7eTi56Uo9pcpXgrKKoW4KGEXTQEc-RBBEfIu_W_RIqW8FlMFjU7XGDXX8ogTr_wmXfp9TjRYSKVb-cpYyjJLK6oTuTEGjZCtDHlYK1DlHTAhE-hz1hTwGhGHNhkj2YUiNUEHACuMUcAKsbPg7rMMtSFkGZlOVRG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfOdd5GgKUgbTqo3uEAIhxLjRaj5Jhn6eOMzAxwpSM_2cD0A7HjLEHCKGgcneToBqYOJKYJczqC_DrWTezjvQ7gJTaVySBW5GbVfgQgXCU3fqag0y9MKiC3y2cUd_pT6dvdubqlvyNI_9OXZhmWKImrO7oAYGXl4te_yRkFc-pXqtnCn0wTfqGykghC0sm_GgK6_1Y6zUm-KzCwKYQsdSlz4CjiXQfkzsWzwbDblZE1S8NX2XjBbM62k6-p_wWe9qoGfe-a8Ue8LiPqqLqGwz32T_DDppZ_dtWp5JRI36QbIWgDDO6Q93EhMLmSEgD02CyrkrVQ60KXhDenN3ZiBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=PO2m0512QytUCgP8hentAdUNGSDMUHcl7vwYtztSyqs1-CLAdnTd4MSROLeQekdrUh_rEVYBJh7UDy3Gm7q7bZp8TQRJ-K_zw5ElCwntMBJsxmfIoFIwyaa-S72gj-Prlsd_4s-YIuaV2GeKsx6lVuls3V9TxgOMDtIv3wY7qxtWu-r5JOE-JIIdSl3iKhtZJ6XAGAyfowVa4e7VhiH7Uqg6IqfuXSK6hQG5NsiPrCZkHWCliFnzceT4_ZGzzgQwH-1MRlMe_R1SMMqZ8PdM4nPe1kwgLyw2tezGMnhVqgBUs3-DkqDm4rdL9UsDksb2csLOrgCcY9hmN7i-F8JE8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=PO2m0512QytUCgP8hentAdUNGSDMUHcl7vwYtztSyqs1-CLAdnTd4MSROLeQekdrUh_rEVYBJh7UDy3Gm7q7bZp8TQRJ-K_zw5ElCwntMBJsxmfIoFIwyaa-S72gj-Prlsd_4s-YIuaV2GeKsx6lVuls3V9TxgOMDtIv3wY7qxtWu-r5JOE-JIIdSl3iKhtZJ6XAGAyfowVa4e7VhiH7Uqg6IqfuXSK6hQG5NsiPrCZkHWCliFnzceT4_ZGzzgQwH-1MRlMe_R1SMMqZ8PdM4nPe1kwgLyw2tezGMnhVqgBUs3-DkqDm4rdL9UsDksb2csLOrgCcY9hmN7i-F8JE8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdhQkpevVyQWwW6wgvSeKBl4bq1KUo9ujsQZ8fum7ZohsoGHqukEbwU6f_CoY0L9qOVsKQXea5gtF-06uXoxfiOH33uPBrUCcBk97A6ZGuJjzqUCQ5D3DEzu1LoY0pHetD-R3dCbU3FcQs1Pl96m-QMGa0wdQYfLxJ5i1XFh4H5TPEK-80a6VZJlKs1vIoW9XRd1tz6mro4ili-t3l9X50X1wmgz1viZEepcWgYBHls2NJ2T0RT80w5rgNBgdGOA5E3hOJ_3oXZVXp1_S9JgBSPAWEwumHemIkFsBtMM13MwLlsmkxdWsbpWAPGEg4YxuKRGksVTJgvXXSfnfsLhww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=GRtNFz7Jr-mbfnN44hdjJ3HIlvQ4G3R0fspT3JjwnRzJVT4TGzDfC9v217QH00IAxymtogQZH-KD0pFNO4vZZYDu4grwaLA-ifcHkzKjJahOkMHKW-2XEipbKVBRcgNmOL8XJ5MwXgRl0bsoqJ0Ul1jMePZtUJ9n97xfROZS83Q_mDyX0sZG0HmIvdF30kPCpBCKtFPkNgIGS1HtZFkOlVLO_S5w6kDR4Yx4R2KxgPZ5r6rgPu324adw94RoOy_kaCbnBt1c9f8ZXZWyZ29Sks-MrqkBbJtQCrCchQAnMUMWhjp6WjvUOCxmt8D3OnQxomXqVo0U6Dvoov7Bow4Ecg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=GRtNFz7Jr-mbfnN44hdjJ3HIlvQ4G3R0fspT3JjwnRzJVT4TGzDfC9v217QH00IAxymtogQZH-KD0pFNO4vZZYDu4grwaLA-ifcHkzKjJahOkMHKW-2XEipbKVBRcgNmOL8XJ5MwXgRl0bsoqJ0Ul1jMePZtUJ9n97xfROZS83Q_mDyX0sZG0HmIvdF30kPCpBCKtFPkNgIGS1HtZFkOlVLO_S5w6kDR4Yx4R2KxgPZ5r6rgPu324adw94RoOy_kaCbnBt1c9f8ZXZWyZ29Sks-MrqkBbJtQCrCchQAnMUMWhjp6WjvUOCxmt8D3OnQxomXqVo0U6Dvoov7Bow4Ecg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqcnIdTvhYEjvilyjIGOLTnmTAb7g4_kCoobJYNzbvL_OhAtW1RMVxf3oK_tw4zWmbk9Z994uu8r0utHQ_IykoZjTwNxi4ZJ8RvAuc0qxVddfEfkEmrPUoJXbExV9ySFmePbC-KPgoWYkzm8t61IxJcafptUqeFGGw6yGhoFR7fPtMm06aEt4uZbBLsdxvdAI2CN7mB_EyTLGQ3pqDIQul_LFjZZPhwm5Kuqw3s-cVEXxdJ_7F2aRX8fqr7eg157F8ENFiZVdbWfy282B74HuJjL7yhUlkIA1Xd40uzDoJl9puKIVt0MezDEzOD8Kq5lEJrCVVNES0mVa7jeH3nd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Deau80rP0nTukq8JG_ACKsuHuRJCrt2Y0IX91goIuXftLGb8cy9mE-l3ikZ33T-BBNQbxieUV9ikQup1GQAUGZ-dqehjXs2hF2Dp-YW4ilEJGOdqBA9u9veKSOJSsogTAJAS8tkGuxcE6Kj2ovmYV-k6dGKS9upiAsjqd309VeBYoyPhhYYjB2XYt7YHh0SPNQVEiTEzjklCpaRuOivLr3LSng2-jAfugw8Ja9A252td0Eb5EjUqZ_T6e5c02W5yLRRWzCV8Kzfei1dundGQl4DrOugn9qAMUnOkt9emvumkg5fBGjgACMOtnmOvUnX0ci6t6U9hCrE_lNIo5zFtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=GHWz2c_tG4iem5GRHUtOKqo2HHy5n7gfKxo6Wa6QZ7rkYvmNYUY23vXwGWNLlFmkDLoTSgbbpyhBnRClOYGfY7NxMRY50mrvPSUrRCdxBPYWd79ZGtRcvnNLNrTKaEXEBnMNWZy5lqQk0dWDmTP6lCJT-VD86mbLbBAVLreset4Nwt3ggUA60aM2t6d8q1lZmFOWRU1EiSYLgrvGrgc2dFEWIKNHyn0snO4YEFdkPtdv6qEKnfnA76z83Tl-lfzSpwaXFUEJHQHSNce3CCGdMzcQwWWwmB-NB99rawL-TZDy3sQPzEw-279poR5Ae7LYyA9bpEdf2uwR-hS1J7zBmW6mx3Hvx5P5KQ2gFIrWGbZCN6w84-pfTpuopjMubIyL-EcVsh5jNUc-oQI3xGYd4302pDgQZGJoeGHF8E24tAuUjRJhENtt8oRSeFKll2j2pXgQr51J0LZY72tTOa5VSdlSMLu0eXkXu4eW6LCfNtXEgCMiQ5cErsMpTRCJbZQalSklPArrY43i1sPCdhu7KH3Y5o61aEx7BiiiZDi6_bLULr1dwXzGmRN6hJrkvChz9btQTOBRxP7u7as9J7CjIFCQpGIMNyR4I5zCVp20QAJ1aXyAnkQBe5PHCHLi9ZO4MaNXQvZeVlYNfo_CxhwzljqMrAhpDDQw5kik5a2IkWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=GHWz2c_tG4iem5GRHUtOKqo2HHy5n7gfKxo6Wa6QZ7rkYvmNYUY23vXwGWNLlFmkDLoTSgbbpyhBnRClOYGfY7NxMRY50mrvPSUrRCdxBPYWd79ZGtRcvnNLNrTKaEXEBnMNWZy5lqQk0dWDmTP6lCJT-VD86mbLbBAVLreset4Nwt3ggUA60aM2t6d8q1lZmFOWRU1EiSYLgrvGrgc2dFEWIKNHyn0snO4YEFdkPtdv6qEKnfnA76z83Tl-lfzSpwaXFUEJHQHSNce3CCGdMzcQwWWwmB-NB99rawL-TZDy3sQPzEw-279poR5Ae7LYyA9bpEdf2uwR-hS1J7zBmW6mx3Hvx5P5KQ2gFIrWGbZCN6w84-pfTpuopjMubIyL-EcVsh5jNUc-oQI3xGYd4302pDgQZGJoeGHF8E24tAuUjRJhENtt8oRSeFKll2j2pXgQr51J0LZY72tTOa5VSdlSMLu0eXkXu4eW6LCfNtXEgCMiQ5cErsMpTRCJbZQalSklPArrY43i1sPCdhu7KH3Y5o61aEx7BiiiZDi6_bLULr1dwXzGmRN6hJrkvChz9btQTOBRxP7u7as9J7CjIFCQpGIMNyR4I5zCVp20QAJ1aXyAnkQBe5PHCHLi9ZO4MaNXQvZeVlYNfo_CxhwzljqMrAhpDDQw5kik5a2IkWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=R5oW518SNUn-T59nreWBWUg00Q1Op3lwyEHzQRNp5XXLK78f_XjPC-t1GTnDMQISh-R1kknc-Hq0rdqLk3U_Fm2uykzyAAZ6p4le6WD1Hp1iQgyJnqrjuYihFLTnezZoPh9G5glThMgXBB3WHkSJSXy2mkUrDDAmbvxPqqYHPPhD3Ju-otRyhvtfV_eyMKRQ7t6KdjAqErgLD0BboQSahz4cmA-QjjPkL26BRQ8fbT28_NrSwA6U7jqkyIucsfdYGgEoiG_vITXIzTfxIzuVOXB-1BCKCKEJAHpxvRuv5X6DaFPobZ8fRzSqjyZxBRQCZXpYd4xjne7wNqRHdV4OWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=R5oW518SNUn-T59nreWBWUg00Q1Op3lwyEHzQRNp5XXLK78f_XjPC-t1GTnDMQISh-R1kknc-Hq0rdqLk3U_Fm2uykzyAAZ6p4le6WD1Hp1iQgyJnqrjuYihFLTnezZoPh9G5glThMgXBB3WHkSJSXy2mkUrDDAmbvxPqqYHPPhD3Ju-otRyhvtfV_eyMKRQ7t6KdjAqErgLD0BboQSahz4cmA-QjjPkL26BRQ8fbT28_NrSwA6U7jqkyIucsfdYGgEoiG_vITXIzTfxIzuVOXB-1BCKCKEJAHpxvRuv5X6DaFPobZ8fRzSqjyZxBRQCZXpYd4xjne7wNqRHdV4OWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfHAutue4FG719ObZKcWV-6pbMNZqvFDLtRQACFc44exCi9An_5FeV1McpVknnK3ooVpDXJA69uOWuxT4LER0KTC7Na3awCwdYfcWPz7wpPAWmPvEZaxN9eblCWXJLmKwuXjXpa-8dlBKpikrnCTqyZ2x0ewR24jt5R2Lf2RL1Mp_cRhOMWtkdD1_6JtW4HrqIpx4TGfF_t8J5JtTCqky8dG6qUucgBWeGdZws08ZX7MyXT6jIG5urx-pcZ_viLPTky41T8zYpRDZGMXgHJNbR9-tT3SKya5BLF5W9ZDnyOx9VC1N42alZ4-kIA7vuvEmT9n_vauzhvpS-eW36Ys9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=nXKgdZlOWNGlC53aiVNgY365rBIpUpf8dsAzEKoMZToqW91lzAlviSxfm-kEWyxAUYyIOiBjBsVjSAl6Oj6wTslKwC01wAHvpTdsCahSD63kSuZeooTIHU_ymRlSEs1vvl9A4A3AA0ZWWG7ZNNsy2tfymKv-5HYCBVOxRnnaO8wcPBqp22CNH5-r16Wa1dlU76QlSxn-uoQC30CmL-Tydx-kNrYtY_dzYa968UCxg7R2eN3v1FT9ma1gObIYqrxiJr8MVTe1Kt8X8DkWQ3Kbf1V5NEV4pKqcndrqcoA2DJGqsgXBmfaOWkgS3GakhOPiMYeelES093aupgkusCvKiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=nXKgdZlOWNGlC53aiVNgY365rBIpUpf8dsAzEKoMZToqW91lzAlviSxfm-kEWyxAUYyIOiBjBsVjSAl6Oj6wTslKwC01wAHvpTdsCahSD63kSuZeooTIHU_ymRlSEs1vvl9A4A3AA0ZWWG7ZNNsy2tfymKv-5HYCBVOxRnnaO8wcPBqp22CNH5-r16Wa1dlU76QlSxn-uoQC30CmL-Tydx-kNrYtY_dzYa968UCxg7R2eN3v1FT9ma1gObIYqrxiJr8MVTe1Kt8X8DkWQ3Kbf1V5NEV4pKqcndrqcoA2DJGqsgXBmfaOWkgS3GakhOPiMYeelES093aupgkusCvKiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8kSzUvx4h-mYi2tLmNoN5VhlG657V74hSagKEHCL4UVwXNhqaxXJwW1MTQMqfzjYiVzlZ1HntuZbtwJqu9Gy5YPxzJ-ORbTGJc9T0AxGELz-yEfv3oOrFbNN80PIzKRa-tj4nivULks1Z-o9GbT9G2NaVJLTxCPfkGlz6Z4dyLsghmmTqMG5G3geixYJ7qdK0LwV8cUHv5TauH87mlKoctCgX6GaOLnn77-ALTN7gzjxeC75HCojKowHhtLizGb-I0Iso0Wx_XnqFPQIq5ovd3wmYumpypQYe5qxk889QQNIlOSdz3XJKLFbvgkN-oD2OA2zHN9p01HtNNCg0JikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZiF6s1_1emgXqjqJMdPgfWW2AcTZ8E9Z_X1b0nkLzBgM8l4UwCmR86Y5LjLQv6hFK5TdJ356Wm5ETeZaUkmfcfPF7BQFzUnQEjcop_xOH61D1QEtVPlIwyqQFoqjPWbcPYtmzfebR84bCtbWuO5c3qaItQlabaXp9OegWwl3WJOD8WWYlAXiZ9W1wRdLH0gAQU9aeLYaVl2uy6OzJY5LRJEEbGcnFQBibwT5helWdQ_cwRl4S1eZ1wRvEm1zm89BIooZ2M5uXiO-9G303rgGlVFvxBP8vLGBDgRHN_jrCAEkcn3j8VHAmRxye-rL8zdYgn8NCUblBVlbokzHSlJ0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbmdUrFVrc4XGH7-eyRHZhFz2oexeHWosrLEVtibxAQs23Nkf80-4kka9qBKEEN_OUeRuAsabZSuE2ZZOnv5NQ3TofxwVqdaVq2vF2NghqWOZpZCJacx07_5MnNYmxuXzZ4BuducR6yn5DnqUsTsXDEmMcfVqz8yy_WanYOCxSyDe_-lpv8BrQHOzkr9XqTyqNzPNusFsOIqkkOrvG8ewo5uHROELyNVr6U0XTSK7ZWMMQc2kTyfjsR6wo2MTNdzqrYe4ynjwllmmbsMgXxQ1JCAGOiPZnKSTdxPJ7OCJRiHVypB9gnPBg4jF9rgZ0be4-aIg-pyOrr4WfQtACwMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg1_Sfe4amgXEN4MBAAVFWQAEwOxZWgSPeEh2veNp1ConG_hQquoxFIQ0AdW1d8p6Ukm5iyNwUP1R_104sAEVB_8Sr6O7jHvQ9dV3ytWj__6zzPwp2uMft429Fih-tp9WHGN2xWwbpBsizFQqSXrRdag1-GaL2Lu38pmT77k_XwFAy-O1lK1Wo6IX54sUd6DE_kAwNamX6QEh1TOX25XWsgZpsRc8hXs2ZhAxkkC6Vt1gwme4kMCgo8qN0cY6Kh6pLP3UZmPGeMj_TpQuoXAVOY9XnyeUFmZpcNb1W1R9Y4P4OMx5eDu-mLCnFnet4hUoSwuZLTkan04WKjD6cX1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BboXW3CSW2EUJI8wnuA5zdzq1-gq2SqRgeyx-C_-1qrwJofIWsuixcK9V6z5EKyka-3s9Lq3EJBUwiTMJk6GTnFnrhdujlfXpEVBW_ILxCWTXx20oELFmCsVdFABIDBNMDJ6HF4ey5vLFcVVw5Ofukl5Zo26xP3CMGJo7EgIsamdQbZ0cSKimcVVSndpjx_6lOYh1vvH-JiCh883gbAfm4TLNNx-pKOKiw6SwIrr0fwhAyvyKs_sdLLBYOe32j0eb9XzDbJFn6ju6nhU5Gwfkvo73D6m5UH6K0EvW5XArly6MUnxVqR0lq6Ue9GkmWy2LD36hYBGvKIqEpRN4Kd9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=eh8FezKltgTAADUlwHHlBVfLGUKPKMUXsfEsPLJmvEg4MYkhXC78sToS14qo8qan55vcDyojFWMDnR9EQe_eCumVvfDXtVXVMII4KkI7ELZXnIierk5jUz017c9zE2rEO-cmiTtJrazRMonRAEwXhvMA07pS0V4iq8X3zQB1wxJxw_O79ostBboCM9gFfuvx8Aenym8nR2Kx21s5JhD51xzqYBdTvV9FhQhB0HzWWw5nM54SzELKUGbc5Cq4PdBRH4EOYPNSHtVSIhXY9UnGHG8n8vmxoKq1o4siETuLA6V8Vb5BRR5mdAwAnT2qCQjN2nalZhAKQ3D51sPG6vMfgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=eh8FezKltgTAADUlwHHlBVfLGUKPKMUXsfEsPLJmvEg4MYkhXC78sToS14qo8qan55vcDyojFWMDnR9EQe_eCumVvfDXtVXVMII4KkI7ELZXnIierk5jUz017c9zE2rEO-cmiTtJrazRMonRAEwXhvMA07pS0V4iq8X3zQB1wxJxw_O79ostBboCM9gFfuvx8Aenym8nR2Kx21s5JhD51xzqYBdTvV9FhQhB0HzWWw5nM54SzELKUGbc5Cq4PdBRH4EOYPNSHtVSIhXY9UnGHG8n8vmxoKq1o4siETuLA6V8Vb5BRR5mdAwAnT2qCQjN2nalZhAKQ3D51sPG6vMfgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3hwFCs9HG9XmPaPa2IRJ9VjQZ4e4ULeVBL2LlSpyUDb05pU14jP9qbVDy_Up9R79i3YZcHfDEh8xqMSWRjtbBcLdU2bfsnysjH5opvv5Ea0-pxUqEK326j_wtNM05amCIlFiQTwduQQjKZ-7t3xczewT6ykSO_12Y5RhYQszIrwVZi0Tnp_qdEOsk5BJXOHpT3CRZQR3A16ylHh7Y1uh8LJoQcunDUZqsspP3C7CF159N32LX6zD9dM1ce8iprk98YP7ushE-tlapwPL8iRD58ZvMMJQi5ucYVvKkLsDqLJQyYAhXu9KWoIBtoKJ3B1kXjr5ZbIyIDvH_zjxUR1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4qLXTepr1bbkxkgf9u3CN71BZoZ87j1wyE_8va2_dBoPDUECWcdFbWMjgUb3xorrtdX__xZyBS8b6dwRrKMS-bvEvN-0FUiQcqcNBsB8j1y_Bk0pDFQuBPeIvoZNU0nSALJIjYx-zGOcnRqx2XLC6aJ37n8pJ3krdXmEN_FBXewWLe-ZBHNR-HRlvaMf2bJcn1qE6lUgKBfOpkvL0vKduAbUm-nNLbLLYtgENbI77mYkgnqQYkMRx-cihc1TsvK-sK6ElC7_ebcXOUlM3Cno2-NzMXZ0-CRa0AFJ_5LW4BNJouvttuTWj9Z81_UykwZTNui07iZ9-Xmr0MlzFJwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=fu0qtm6PgAuxLo5ikZiTH74Y_qOP9lSlz6SBBUuo4SkbWDooqQae68fOQgZrgfNPST3XRNvSA8lso9tgISFC9pt5VOIF_ENkTeUCmSII6ZToSCcLYtzmBaULqBwF2hvRzXEQ5c3E6kFerXzcaYtfny5K21hMOvB7fOWC8ITnnY0PKqHcq_GC7438gMBwKrXa4Q17esKipJoaSXqnbrf8FOyLQvb6aCE4HGUkWosWyAI6ePypxc3t9xx1qJlYUgKFM7XbVJfjPhgZLKX9jZvtSoGl1LvEOTtG3vnzDFkpU5xMnHYSorBF0EV6aTLrVuKNmTDIm4EgiEV9zoZmMlnipxQXrTHDLLzH4NgfpI02lS8xYPg72AP2jl_1fOVEZ7t6O1d2OSLZFytMTr6ya1z1IzlWfwduwsA0wP-rDANkTg550-FndFbZNV5Sbke2pe39T1vqI-cdPlNpSdCB7oxJQ8ZEBp2r8S59n583sJ0FWgUPDT_Agj4WWJBNjgI67JQP1P2BPyQFjW-363MnRd3-WGtCALDw9rgHRu6O9GFJdsBuzbYzpTsBRVlPN99frBQ4uGAYGwcVU8ujalkwohN9FNHJWSBwW-e8KzI6i100XwwJ7CG72ozg7FGcpdpYGxAd0MIDRv9JEmznLGQ4u82NDey6aX2EaRACJ6LeMj6L6H4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=fu0qtm6PgAuxLo5ikZiTH74Y_qOP9lSlz6SBBUuo4SkbWDooqQae68fOQgZrgfNPST3XRNvSA8lso9tgISFC9pt5VOIF_ENkTeUCmSII6ZToSCcLYtzmBaULqBwF2hvRzXEQ5c3E6kFerXzcaYtfny5K21hMOvB7fOWC8ITnnY0PKqHcq_GC7438gMBwKrXa4Q17esKipJoaSXqnbrf8FOyLQvb6aCE4HGUkWosWyAI6ePypxc3t9xx1qJlYUgKFM7XbVJfjPhgZLKX9jZvtSoGl1LvEOTtG3vnzDFkpU5xMnHYSorBF0EV6aTLrVuKNmTDIm4EgiEV9zoZmMlnipxQXrTHDLLzH4NgfpI02lS8xYPg72AP2jl_1fOVEZ7t6O1d2OSLZFytMTr6ya1z1IzlWfwduwsA0wP-rDANkTg550-FndFbZNV5Sbke2pe39T1vqI-cdPlNpSdCB7oxJQ8ZEBp2r8S59n583sJ0FWgUPDT_Agj4WWJBNjgI67JQP1P2BPyQFjW-363MnRd3-WGtCALDw9rgHRu6O9GFJdsBuzbYzpTsBRVlPN99frBQ4uGAYGwcVU8ujalkwohN9FNHJWSBwW-e8KzI6i100XwwJ7CG72ozg7FGcpdpYGxAd0MIDRv9JEmznLGQ4u82NDey6aX2EaRACJ6LeMj6L6H4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=XQYdpGuemA58suFoA940_YY2cUT8dlvwEzjI6hDksuQ6MiwOw6a0N73FMO93W6Lji_3Yjt0MHim9IJuTl1PRGC5Hy6rtubdiWXsNiTS0sBEv8nhADVVorFN9_OIcMF4cGncrccbddETbp5DWEiMqFX1lc2u9irxO0ZcoK47s9wCPK-oJnkWIRgYTHqlwEVloG7FOIkI96X6HGR7mfXaOgLXtd3hbhQ4EtwzmdLD2cmz3X_eqicBDr-LscinmtNb5iPbRdJFxzJPp-NYQjJ_XJKHALTZ4fBzfF6_-rfORO314kqONwRMhvyKShoCUWoM2n5LIBm6waSZJb33zVDOHIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=XQYdpGuemA58suFoA940_YY2cUT8dlvwEzjI6hDksuQ6MiwOw6a0N73FMO93W6Lji_3Yjt0MHim9IJuTl1PRGC5Hy6rtubdiWXsNiTS0sBEv8nhADVVorFN9_OIcMF4cGncrccbddETbp5DWEiMqFX1lc2u9irxO0ZcoK47s9wCPK-oJnkWIRgYTHqlwEVloG7FOIkI96X6HGR7mfXaOgLXtd3hbhQ4EtwzmdLD2cmz3X_eqicBDr-LscinmtNb5iPbRdJFxzJPp-NYQjJ_XJKHALTZ4fBzfF6_-rfORO314kqONwRMhvyKShoCUWoM2n5LIBm6waSZJb33zVDOHIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrV7BRpJtcVUIuDk-MJR2YYcaJKES9MeVwFzEwDPiStM7CO1AylCQ7lXTiyjf46AIiqj9KwwfjUDZOHRs5dly7IM67uAIH8zsR3KKJWUg9XuVYclgz2HUd--SswtT4lzI4MGtZyscmnNgZ3wyRF-5CI9MY80z1QSNUS2czNk1FNA6St1orbY2e22ToADE9LP20oXk3ydvwAobMqEHTHRh5B6PyEs4fw6WqLGT0DiCd-Rf75-GvrUhlGoC0y2Qb7xvikVYc47SHYKmsxO_qBhbmWqkjflX7mtPZnV4vd1vfm9pw36C_tWYT73nUXedHSivXJ8yDW_gPW4HlsZAQa-7kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrV7BRpJtcVUIuDk-MJR2YYcaJKES9MeVwFzEwDPiStM7CO1AylCQ7lXTiyjf46AIiqj9KwwfjUDZOHRs5dly7IM67uAIH8zsR3KKJWUg9XuVYclgz2HUd--SswtT4lzI4MGtZyscmnNgZ3wyRF-5CI9MY80z1QSNUS2czNk1FNA6St1orbY2e22ToADE9LP20oXk3ydvwAobMqEHTHRh5B6PyEs4fw6WqLGT0DiCd-Rf75-GvrUhlGoC0y2Qb7xvikVYc47SHYKmsxO_qBhbmWqkjflX7mtPZnV4vd1vfm9pw36C_tWYT73nUXedHSivXJ8yDW_gPW4HlsZAQa-7kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rynykSW-vqIo2RwZtdgSa6ZzuvxHPzE2g1q4gcFVXypmsvHuxuljHuXupZXnmU-fX0-yy_GA6ofGS4votstFTY_7pq2xq4H46uDE23KArHEQ5prA76HXy91m7MGj5fPhcCKPlVnki8XAsaRm14kYDG7YR41WHLB9KwIA_jD4Vm76eJTAMJdU59-OzbQWi1haDV39P--AUXEseMGlHoS6P118To-1IAmOKS2SZB6_EUvHzpnQy1MDu_ysO6yBA3u8hGrFSHFSboAlNhhwnjl6lxxa2_k0fOGHANT8cx_M5ptFizv1oaPLaE9PE5-ctugbBjnjO2XaGdxSgraL0Eco-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwG5D0Vn-Y3SSEjAZm0Pe6cXOeRGd-wCeYsFKqzHdqNkGhcyDowOkulJ1VOdXJikVpZmSpfzMaRjrtgN3L8FQYuOwQD6cpyhd6dSIXmkaQGLR_aQd2zpGLl1AAJtSaD70X4EgPxi0A6MoPOX4A4IiRHBzoBGcNvZykSfap1fGkE6g2C8DauyGgh3NuvY5-N3qHiKtPjEnaHxc6Tx3GhCoi6ty03n13VQZ-eqpGU695-kTFggtEM5QnK-GNxpPINJWHJ1KbAGsbp_vkYwKurX-LydZrroAkyhK2--0VaVHLZeUvboFacawdY3xlRKMm_nHp7spfe1XzaAcOkuWdrN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUBiYku7zwafezkFec7YolrajCugSmu8jdoIyGLbb5CwTwiABBP61WXn2AdfOfpaaRWIPcHNGZrJ7n3_tSMYiU2B3wmKhajcnquMxs4OueXvvb8n3Dbr1Y026XX0Fw-0TtN_p52v_6wIS9VSzbKJ-2tEwQfysMaYOfQ8XiipIhzRRlR2bzKOeoGWZhLIVOAzq7IiZwwZpcod7ttKCY2Fw4PUt4070r3MlroYjKNwzoF9qtkJ-br-J1uGHdcHPogkT2hXIcKdiU7_5vO2u16pGa_IWAmU_-ulG83hrVxoj5d6uz1zRD9PeTump2SWCZUFzEgJ61d_8ixD-fguo250kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=qFHIERa6ghDetjoDLEMRwQJ22bFJPDSNxx9_G7whfeUIGoYfslwLlNSfFAgJMOjc7jfJ-mZNXBwakDQeRDksU0tH_7U-do_uGKFeD_9G4d5uCkLSu_8XJQzWdtKoNeJcv-iqOpaG88dvc9gu1hOhR9SC9VjLgw7044j5FaDJOY5szzFBDtNsX5u2KyigfKvONgyhdjNI0Iwg2B9qAo6IidtUDr715mOy15d7tOkTWRvaGkE_I6t_LFoH0pzCoJOkLpfK6XeDiu8CekZxPhw56oXpF9VEQ1AyeFjZXt0uKraCONE7ZDcO7PaVdZ50p_YC0zgZ9AY7PiqYOcPbW0tCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=qFHIERa6ghDetjoDLEMRwQJ22bFJPDSNxx9_G7whfeUIGoYfslwLlNSfFAgJMOjc7jfJ-mZNXBwakDQeRDksU0tH_7U-do_uGKFeD_9G4d5uCkLSu_8XJQzWdtKoNeJcv-iqOpaG88dvc9gu1hOhR9SC9VjLgw7044j5FaDJOY5szzFBDtNsX5u2KyigfKvONgyhdjNI0Iwg2B9qAo6IidtUDr715mOy15d7tOkTWRvaGkE_I6t_LFoH0pzCoJOkLpfK6XeDiu8CekZxPhw56oXpF9VEQ1AyeFjZXt0uKraCONE7ZDcO7PaVdZ50p_YC0zgZ9AY7PiqYOcPbW0tCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
