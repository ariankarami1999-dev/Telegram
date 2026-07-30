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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 15:21:00</div>
<hr>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSfhQ3TvPadU1wv8Mz-3l2QxgtYtENS00j0nv1cy1mZJ1-uX3aMmRj9TAdQr6sDFeQCWmNQa8_DO01thSkS94_6TG0cX1GcsTFNsZdVUEZiWN6c8Z29GXmqiTQz4EEZKSSXFuJuivpk4Cjpgk0_M-e2A3PAzlhLWIWLUuxbbVWgGt1wbXwCCn5DITrLYzUf9NDsfjryqjQ5NV9UXVYFJt7w-cZcJxyXbm-PViaO92WZFaOfqDDNg2ZNeqwGXAukZW7oLaHCu5PZHe6N5Ihwf7b92GSLIo7bJ--X8dMoLVBP_XoOjMeEe5hKdz3liwYRN2kvdbeOP6TUrVQqqSn92YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDP4jmDkdLZZJZPP5SqH7mU5ME3J2Djq4TYL9bT8ZVuZvlq8FEdBJReARMDrwauS90xfIEWW8vuNpHHH0d0A-xA_3X_OxfUsLYhKjTt_g3LM-uO9_wP52iNk1zTrZ4-s6JccgOa2RlQXGdvvpqkXWss3SSSJQVHeQUD3kbdxqf44oIBzNoUFt2lpY82ePKXvnpwihQ0s1FC5X069S7QRWXIwOXAWNC6Y11y9u4lp6nItEWdNRfzq5WITctimlAbxnrhhZyQBX_bKdnQpJf1EpGjFDME23l4IalLCDBP_tWgZlvXp89aQLCsxj03h-io6K6QB0I_MOH0n0AltgErp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=MbrlmJASkcIt8Z42MNuLmRPY1inToumTIeUtcuu9iiEk-7BA-aVaKCsh4CsEgwIvDYVXANoU9LX9_bcMQ78IFeWXyynvPAlLeEUK6-Ky-53ZF2v4zYIsxgKxMTplVDf8lUvFRxmBCANdHefXYbvPO82_471vFaSPvS60ARFKslpHa7gg1-ezpSisuTQq4NN6rKCa1WT_wA0ooRgPd10EIbRznsSAdvk8RiZ563nyljyEzzOwgM4QPVILyi4OU1-wagJNpZbwT1wzzoyeC4X8OSwoFKLoPMkt9II9SMqhTIbwOfBPe8LBobomUQXJzeejiizJOmGWTO4BC4bkVEGWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=MbrlmJASkcIt8Z42MNuLmRPY1inToumTIeUtcuu9iiEk-7BA-aVaKCsh4CsEgwIvDYVXANoU9LX9_bcMQ78IFeWXyynvPAlLeEUK6-Ky-53ZF2v4zYIsxgKxMTplVDf8lUvFRxmBCANdHefXYbvPO82_471vFaSPvS60ARFKslpHa7gg1-ezpSisuTQq4NN6rKCa1WT_wA0ooRgPd10EIbRznsSAdvk8RiZ563nyljyEzzOwgM4QPVILyi4OU1-wagJNpZbwT1wzzoyeC4X8OSwoFKLoPMkt9II9SMqhTIbwOfBPe8LBobomUQXJzeejiizJOmGWTO4BC4bkVEGWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8bSaQ9ILleBm8huN4fEKzIeoIL734wNEi_JqJIXbrd7SRNWglL6uLhdPXCMR3OiJKlJoGsIHYwVcdKykIrQljayk_gjy09P_Tj_SkqazBtD-Jm2o52Q6lxTsKJJOmikAAvRMcAx6rqHB8DcO5BY7v5wI8Dey241S-mWsFX2jQgELIv0pyci2mkRyGh08qlycGofCkZWus8iJrsoSkGALDGz5SpFpkvvZ8-7v52Qn5kE8dIpkoQYqCLvFOCqLpxiQPUiqw85Kss9_gv8AgSoUYJG3q_w6iO3e1hEyk2mz01zw_AMIxTWEDonwPCnQ9l2uxxHcPfIunAkZXrckrDB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krBGoYPJIqe_DM1U739fE5ovR4UwtDwg2wqHtBkcuVaiQ0R5Dba7RyzKWMAyVSpJWBZ9soo-vFGZBM6BVnOr79O4EEdCuB8eMQMFQCKAoJbwb90QBM5LqZH7xTqUzBEvLf1XXPZxPy9aIm63ulSxnci7-mj6TtycwAmVZQpI8x7at1QvYH7gDspz7-H297AUvhZtNGiijbcKESLI6U1JS4uojMVi0F2MHDXM6B4zeKqApz_bzYIp4sJEt4DK2G4yiKE92_Gdj38xuHxrb_DQbKuqHeQEoIKy5Ro5073Z5IrnRgPtVPanf6mGH2bZbhFfEz5B6McDpqtG8KJ1o7FxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP6lO-y2hirmHzcnjGLHoSKBLiV9MB-KarTypc-7iwvOiEEBdr7OBsQ0gKKRM9keBMLZ-YK4J7wdd1_nSevgxzbnF-BfDb8lpcJ-nR2G4IwwHkERuWsJsi5R1o6yRYiN1Ox6lw9aWYjJypKSZJ4zDAZseYzm2P0p4Mv73mEKIChqm3Jnhj-C036MNToRZIkELUZw6z7K20dvPe83ttS7oB55KlWLyty-FmhqSx2s3-qwuo5ZvjS_y__1fUkPxSYDEgq0agFEL6PoEF_9WGzX2Js4BTU4u_uPeFTt_8NKQ2KwqlC9hG4sb4SeCI1umcA7Hh6qN-YEApLvDSkMKHp1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzNBEuvuKFhvosmDZEZD_qHgdiES36oYGgbV82oIecEeS9rGiVpEnZ58AgmTh0hkIoPJmT8MoG45iHIbOkrQOKBPPytH9JaK8lxl6MeLThaq5fjFuDMPS-Ji9sedJP6L8kMJqctmUWORMOWwbatT-q5JCIL3l57lV0lzg6YrVSWAf6ywU_gTBApcXyiw2xJRY38gfhcb-iFdNJCQs_qkphRlLpgMrSon449xoL0WKlV4TWUho_ncX9rRuBl_21xvdWqGHyFxqKW1vBcQbv56LiTLIh_jDplKS7SxUshMfeO1pidEzy5cydQePF1spWz-bSTBZEjhdjkGMmzvFLzDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBENYvy1whp4V74uNVeGf6UPZEkcwo8e6AAqGWz8v7KAbgdFoxlJ8cedDuDTQZAiDnllpnzs_P4qr843ERL5ZhYeYrmIdv8Jim-UWHQlDKQEQru1dRVD5kDsupB6SHbE9lSrRloi5-7w38V1bIQSqv7axLAjYauJNawfkj7JtvvGtgwtxxVXPlUArn3OOv5UZkYTIvsPMn9b3bP1nw7FnCpDc4z-8hyKIXdw8ufmFXh0ChdyLQE99rWNM_bvHTOlxHi3BNaL8tVmoLekPI6fcQ9jTsZ01JbBKKghNW7apWvdDTf350kUmK7ArfrdePwfkOKHjmSmrUHdBw8kw65aJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqs4qSIFRBtMRucuBUvrWeStXwpibJWyodqMmweTp_hrr-yKEJUq9dsqoluh7Okt2wKdp3IA_ZlrzMMqQUBt-ORdjk-gU6HTdTW1nqN0eT16iypLAAh3wrg5a2O1j9iD1txLrlC08KHekwUMqbVLAjurjzqYzOYnBIbTglGxPd3qJ63FxUGtMftkEMyU1P-RpOPPglFo7mSh0uwiVHT3ob39zWm7bFJ54Qs2zxboks9Q9EkeAsCJzeDdegBcUR0kJULeNFjinWpXgQ0rvupr3C2qPKmc7n4wBQh2f_DBj46CebTB6NAp0jdXihIHnDV1UXdImV3jQD6rsKss8cv1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNQwTEW3EjULHs83DeMqYG-Zht6c4jtdT6yLm97dn6JfeGL2-XLhu8lh-EYIz6dxLnPCJInTf8JFyHsw6FXCTa-Zmo3D4Flss_CQxQTO3SZ3X-9PtDBKKR4-3EnlGlPDy5hXsmWQ_92jNu934avLmu_IPKT3DZSXToPU3gH1y0sZww1FGYUPLFoETNaFu0lSNEJEInPDuMzzdVCbxeuL9FTLzihokGPhvWhFjMateq_R16LhdKkix4lu1WegyD9Ks9Hv1n10n2LtdVWaIRHqqSHWOTgUqZIktG1oq6G5bhSzaLRkfFIMJEoyubN-m2ry_DmArPZcpyMnf13Tk8gQJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT2G2T6MLPMRuMjA32pkagiL89kT-j_aLuhtp3vI38gsyCbTnGjAfZlhX50nfUMHriuxVgEJ2l9abVElIk1wzcVMZWxmtze5hGLufhXz350i0yj62TBrGH9jaTV3xyVprW5CT_s_0peTE7mCbem9BhZw7pfFFNVNCl9TaCyxXbxkvfTJUB9uPvRUiBWSHbQ1zVVzx-fmI43MOxBiOKelH2L-ZT7ZroCRD9E-s9EaZNlY9YKvnF16gxLvsHp4MQ_6SRhk6GBo5U_AtfALQD9cvC137-1bLUG2PVXbPGnXzI-3rbo40-x7z9wwVNs05ilj3oHbzcZocm2k9lI4LFVwRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjdxZlHn7ka8Cq3KIp6GCn-4KZNHOSteP4WLoKfjFS_tkW3HI9lCaSkWLCFtSEqjoGunEGPpIebHDerLNFLunFfdgm3Ut2bGBJw8N4kpmjb-Fj2ZBwLr8jJQvJwiAe5mzcL01JrJ5bgiQ-y4SRDV4VX6RcAoNU80Z7RcaO5T8U40BQ4rwjd8nKxqfDrTZyQ_PUxTaQT78Dm8eZP8GuQ65rdEAHXl_EoBgXLnAod-ba4PSF8ObADcL6bJXhzNBkf1nXcgiXyNNmP1XqfQPbNq3JP55BiUJ8q5P7YVSAEh5A5oMVEiwGxFOKtImfATHqq1A7KNH64yeKoBO4_jPK0PVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=NLka_7D7WLLfvd6oPukh9uHcnaxVUCBTXJyK3O8ofYeo48iNugHQ93fA-xGnLG2zvytSRaBgFIGyG_9uGeMv5cjbK31xWP264ckZD3m6-TPGqtgh5n89rT8V9VBccx73jNOTz0wAREgWyDGqwLNeBNzuLxQjJxqo7yQ2hcjWnYfDGnMm4qFJ5NZdADlNSv0xd2gdCJur2qZC2Wv1hvwnlZGV8WB46XNMItThwty329XnrK_GVR-qLoqVrWVcFaGzAGgxghYFRI_BVCEiQc2AKifMdgZVswAd2WbpZc7N9kk58M_MP8kTO9AMzGT_pn3ykxu6fddl-O90-tNb0PFwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=NLka_7D7WLLfvd6oPukh9uHcnaxVUCBTXJyK3O8ofYeo48iNugHQ93fA-xGnLG2zvytSRaBgFIGyG_9uGeMv5cjbK31xWP264ckZD3m6-TPGqtgh5n89rT8V9VBccx73jNOTz0wAREgWyDGqwLNeBNzuLxQjJxqo7yQ2hcjWnYfDGnMm4qFJ5NZdADlNSv0xd2gdCJur2qZC2Wv1hvwnlZGV8WB46XNMItThwty329XnrK_GVR-qLoqVrWVcFaGzAGgxghYFRI_BVCEiQc2AKifMdgZVswAd2WbpZc7N9kk58M_MP8kTO9AMzGT_pn3ykxu6fddl-O90-tNb0PFwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=Pr28gxVCEjKLg_DsFU9XGMQXWmRHit1Dxl-gXt7_WBr6thfI1ZPTKzrFUDuVfO_kBLFzJrjfRpKqvRx3c-2KpJOV_95R9iT-4RgaqApsJzhEniQyDWwuo-Otg6G4ddEOvNFxYlzav57QK2IRMFg6grtc2TrwcpDx6GHVuDJcLuIvrWPpPktOWYTWpRn1S5iNXT62Ae9b8d4q5s3ADQxUXlxlpOat7L06sd03zjQg9E-Cdb7L6Ui6mCVn6WyyNuwBP7RUbMjfoLI382zPguAnFXdGdjY4psV6hIQ01uG1X5XH36xclX_Cb6B4N_yC3qEog4Nsm_m7D8WY1VQ-f8OSOCSZIHX4HIalGDg_lDX8ND2HWUVyF9ivh0qdBMhEgVcXwgZVDRYOYshCXDiWpw1eulRgBwNKDneNv0PjXSuElQTzFklcyMz6UPp-Pb8d_4uFF25nkBybiQEZNWYiJm09DWoCTRJgS1RCulO9yUU-qGfsqyxEALz0vEoNSgr18xO7Sv71tgRY8nv9VTAOcDqglIz_NUhhzhIhTnqBhXnlLrhuzNm6_5BlUgdGV61xc2nSFXSZZAFR0jWtUeSuH2dMY4uNLvfilNPQdDdMrwgXJdygysk9jVjdkErfa05rfbjglS18bcNDbk1SelB_OURzKJNyD_y_NtlxJZRM31Wgjmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=Pr28gxVCEjKLg_DsFU9XGMQXWmRHit1Dxl-gXt7_WBr6thfI1ZPTKzrFUDuVfO_kBLFzJrjfRpKqvRx3c-2KpJOV_95R9iT-4RgaqApsJzhEniQyDWwuo-Otg6G4ddEOvNFxYlzav57QK2IRMFg6grtc2TrwcpDx6GHVuDJcLuIvrWPpPktOWYTWpRn1S5iNXT62Ae9b8d4q5s3ADQxUXlxlpOat7L06sd03zjQg9E-Cdb7L6Ui6mCVn6WyyNuwBP7RUbMjfoLI382zPguAnFXdGdjY4psV6hIQ01uG1X5XH36xclX_Cb6B4N_yC3qEog4Nsm_m7D8WY1VQ-f8OSOCSZIHX4HIalGDg_lDX8ND2HWUVyF9ivh0qdBMhEgVcXwgZVDRYOYshCXDiWpw1eulRgBwNKDneNv0PjXSuElQTzFklcyMz6UPp-Pb8d_4uFF25nkBybiQEZNWYiJm09DWoCTRJgS1RCulO9yUU-qGfsqyxEALz0vEoNSgr18xO7Sv71tgRY8nv9VTAOcDqglIz_NUhhzhIhTnqBhXnlLrhuzNm6_5BlUgdGV61xc2nSFXSZZAFR0jWtUeSuH2dMY4uNLvfilNPQdDdMrwgXJdygysk9jVjdkErfa05rfbjglS18bcNDbk1SelB_OURzKJNyD_y_NtlxJZRM31Wgjmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0w6YRs6M_Y1qSt-04f4H4yGDuM8gEzTD9GWMykTHIUweL-g-EYFekGOZkEtYYmeOFl2O4-tkgMkO7LnhydcS1gQ_Vs-2MqWfIdZjD8pWGxPF2ZnjMbddD6otxClrIC3ky9YBuAih_DDgBBp4wLWHBIPMNbGDmEuwpAKjt3Eza-lBX-K6y-GjLw3qc6car2kb7tWe_1cdV0bZw8L63RccE776IgwhA7QP2QIxwNbH8ws9v181vNhKy64oFmrtvyuHKDaO9uwo9uIrwWkzueCwDM4j5IGyyB2JWejUrGvsbhaC1ck2ebCfZ95xddxgpgOoxrNAFG3yBs_uuWBTB3CZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=I9wNbqZ0hhwPg_NfhXAjARJ983Tv8w_1RPTUbhZtZyJrJOv9k3tds94IwGrwPJSSA49zmx9TVy2DZE0gSL0DMN3kSfvB8CBNVECkc3_4G_MRQwHIfDi0_JwGnU8U6T7pft1wUY-P7XKj5OJM1N07IzlATT1ujA5pySbcLJJ_-MWlFdJUUnvGa6eGjISwmQOv8e2nAuoa6LKE4F1q0XzeaUIbBUFUN2bN2UnDlclIlE4MUt-sr2WHcHUQwrvJUBRQWrA0O6zBVqixNXSnSRdEuyWfZm4jIxEajjzKMGlczwmuQJhYlDuAWdkWRjGb7lPjeLOzH4ZR2-l1fKkAkN7Tgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=I9wNbqZ0hhwPg_NfhXAjARJ983Tv8w_1RPTUbhZtZyJrJOv9k3tds94IwGrwPJSSA49zmx9TVy2DZE0gSL0DMN3kSfvB8CBNVECkc3_4G_MRQwHIfDi0_JwGnU8U6T7pft1wUY-P7XKj5OJM1N07IzlATT1ujA5pySbcLJJ_-MWlFdJUUnvGa6eGjISwmQOv8e2nAuoa6LKE4F1q0XzeaUIbBUFUN2bN2UnDlclIlE4MUt-sr2WHcHUQwrvJUBRQWrA0O6zBVqixNXSnSRdEuyWfZm4jIxEajjzKMGlczwmuQJhYlDuAWdkWRjGb7lPjeLOzH4ZR2-l1fKkAkN7Tgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzVI_I--Nao7pr64-4AniTjlcgApYseXHvU1B70qpuulT0ezladEG2RyEONwzHcCnPOe03Zyloh0wMYMLJc2Eg6fEwjLkbMIHW0nqZTGV7Vqy8BZ4CEHP9jyKvFYUdzNmuLKjnShqw4t_sPYsn-K0BKILTr5_nUEHVh-0DKeAfBzdjP8fgU5Ifxk3WxfF9ma-zQbw-ftnRfE2o7AnWxZJnnXjhmg6w52kplYuzhZkke1HVEZtFizTfOLhq00rBOwXmb5P4Aq_59coDD5uVnVBnXfN3OAbsl0sJ6K1NFNvd042YvQQmEC8oJAPdznLq_E3G29Fkn5wTyISaocgrIXPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9OLgBJO1V-tjIhF1MGz35FsWxkOXhy87z4c3TU17Ucdni6x2A2sztS7J58VX46VUGSK2WDjunPp-reX9DxzwF274J1kzg9thXpWFq3IGL-CQBlFCbtABwJ9VvIfolSgd8sjqpDBtfh-FAJXke5XiOH9U758dsqigtC99qnErFqs-D7DJ7bNTuQr-aSzbOO7Ga9Cao78uWslSeE-sQAKXo9k_siaP6TNnJHFTfSviKhvAqVSET-OYYfykBjN3pTJxdXkXkn13LdF65rrP9ztzB7Ipr8_jWI0WfKMZXpgYCUYXTqj9-mk7kBcG3EA9d7rJxOkz9x1DAPOfYFv8SFWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TR7Lb0cFw6MFgOb6IbOe5hSEIEKbS-NsGf9Dd6TIVlbkepJUwh-CiPZvutoSBwR6iOI90DqI9Oh3HjVbVTqJq--E2iX-VUt2Ddk5nktue7H_clqtAUbnekPNxEZW_uxrRappjOBtowNx-Ml5yLCm77FWqClJcOTcMyLduYEDAbqr4308zSe3xOFeFDV4vEehDtoelSW0P-uOgfhpVgw_JCXQxQNuL1PNmqhvymVMMlyhAIlbV3cYYI0Ofy20acKDz_w2wWAuUPvf-RIxdHahP4SGY2kUaiS1aEFMoOl3a8qWmWWKroOGVmMiJvmarbRSTRu61XBpM5tWqmJLJdiaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STZt9RD2zpxbc-OamTmqhekF94i8OxMFov5360PgohhcaxhYKseEPUXSACgI98xVV-ru9wUadD_veyl6162Bw13HWthq-MvEO46r_4CY4NidoqvMQjj50Oeg5_kUNn9-upwuLwXVDoYPFi9N7S_6chK5Ug9vYMDi_mihBOgkiTjc5_N7CO64Na1aHTMVmCwE1Tl3lY95PWNVGY4f9BgUjTby7ehJPDpGPMY-2zS95ESzD2Gg89NqgEWGXvU35RVho2SbG-RyVT64CZIj0XfvH_Wl290qQmVj3f8KTQaC2dnTBsmIPnIhL5HnTo11FiHRg0I6S-tiyG7MvQy3DEsLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0ieiiBEWi0C3KuYqCWw84PMfvO7eBmxAe_6bqHlVnoLGOXq5eKHmL3jaF2-N0q4f999KKrhRsxfMo_E7F-cyVuCUa_ih4tT1VzTxNdCZyAR65DyuytVvxppzSbquZjiUiuYvNf33Qlb2f8E3vprq-zdR-LeJQOKfA2AGeCEHPpt2JqAqQq9Ikbk6xVozYPlVEjd51-aChYXn9mX98cltZkg7gJ8jK4ZnZUTOnvihUGakAg--5fEtZW-M3VHA-3ePSV-9ot4K2WisNmkWLRLpxKDJj-QGGVXGZ9zuGP8KYUKU1i8Y-HSWtfAr6dn3vZtI0RNqxN5vpSmZOkWjs9oZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyPHTTdQ90Uo6SRoTTvHyz9ufUefDxYnAnYsnnub4G7Qa1Q9e9QcNgRKL8XU4EWZBqyntJcK0A31mftbg1qMMiWqnyHqRryJt_kPaumomTl4KLIaF4ly5NWxymZtm2fWHWdQXpbcP9bNept6kuMYdW1I0rgRAYjqbWvqtOA8w5CeIHFIYGa8dOm6C8gue4Fsx2z1xyBIA9xqoRMsWZNY97gIkJPxmvzD8sbJp2hqGzjUCjnNPNFxyvyjExPsUqAWPBHqyePpcvLL-Jw54qdKMCP6vDQsrbFi6RJIfaOR0EL-xpOu792SOXaQ74nWPlz8RnpMzR3UoWlyavQUdyj0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPZeKHgsWEeRqhELYDJ3AZDNRU6Rnh33XeacBxPBJQdiaTaQYVOFvvN29xK3NIFfLgQX616u-w-8ru_H5YWOl_Wflzv85I9I87a8vN97N6zuCbV37KycnMkixLfZEMwWKZxMLvqFLQF_iKwPRe2kieamWoZzaxpJsQUViOBWnzn3hTRUXRwD9Y-5IVM_iEeWrJaZKQZhtN5FYz1abFdeQz-MfCtPkMt37Yzs5x3hEUFKAMSQyLhaYYVcnnGWMyuTOCl6MO2DaqNSJLzxZr_IPfQMsXcE_Cx8CyWtHbXVs73uzcu5EnFtw1qRMPXUiO_gQUh_FYN3bwbbYg_49SiThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mz-OPwpYudU8PZ4IiMWncKVw6xUas_pC_6Jd3N4bdah-mxf5tSbFty2Yi5EFt-VHf1LciuKeEEXIp2gBt9CmZ5gGzlTYgHWOkBRBDCPFLxCnbmGhEZKB4lxlqBj4W-Ev3VeEx6O7gjmwUGyBhxE1QiOFg1tifnvRnOboAESsWdT6ALOcY8i9rN0jbtboSp2fUMUFdbESn2IPcXQoJ2wqfkY3UDRj6XNjx_IFbbXpAxYpHgwbwA94Q9q0z5LmjPQ3Ja2tPVstGa30mSuDssd-Jzoext5SNwakBoROmHdru8Yg02-wrrBzt6I7K4YH_28q01K90oSRs4Zb0DKNYQWjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vH_Ohsxvyn_rXPfSzwsf9GV4HIZmuWvu5cFadl_GctStotPu1fyQKMumDERA9D2HwzozxWfsoGKCLGavD3b_HGzr0dY0kM-tCk-VfNFE3kjngcGiQyjzq8vPx5lvWmm9FYVqdg-1CO5hKotW1agmV2CH4GRnvzZ1kkizbg3xcPTFIOeN_55pIEwFqXq8ICbVeCLcVL359-71qYoqGxVtWcqc-JN_WcJsMwJQP8VmTax2k92yUpZyQpsDYjxPqxYGtyYCZN5jrFA8fsxZm_rlz-dqR2w1TVZMe3vsQ7R8XT0cfW7aiqHzt7VzubVUEZnJ4evNMdtzZYjrW4xv-fG0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opziwOZXJeJXV4J8WWS68qjRcynbYWxzj2MbnU_c7HRnWcoNwUFEe0RGOmJJa4S0b-sUvLg4gAC21Z853iEwy_7t7m2eGP91ZCACIuUqdoMVz4oOseMyh5QdVnXOxm2d3sOrinOBEObZRSp-gvJB4N_O7EcCwkuRbicuAY0L23S6qVQ6MlqXYoETPpQkr4Kj1fcq9c_V3w9o_cLX1m7IWmEnKKoqb5-zInBx7AFJwP4DKyJDHyyuW1WN1m58VaSp4Lvtchb_EbDiUltDAaruWT85jfAvigQW-6rXKtTC_1HW01ztH_EtCCkvkZjNJ8DI5iHdXvMgItnPsLlvGVvHzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzkbikhDeFMDcnSP8QEprXxjd4t5-aUVjoja6N-2MFMdfHV7CY4j6jNg9xBlpWvSvIm89sf5vRR0XlibMo8hmR1lPmRh0lRrJQ0lonKL2WQHtGkD-bFhbIhpPB4gQDgDwmiwv7db3C2rolcHh_1kVY1GSlkkJSFWy7JW5wa_qNP9ZwHn_Tu2fk96pqIhoS0w_QN4F3Z4baqY_wBoC70EJqK7wDsSwsOlVm2TuUMKV28-D2GY1MUyYcAYuOZXJElOZC8r9U4oHA2NCwSP5fCiZx-V7V6dZziZuQFy70LdgYINUYnZ6_Ay117_eeL70diuHa8xmgKeyHJkG7RHqk3s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI9GMDb8NPtaEZhgz7dzo62Xic71qJNi7PcoqPtfaFOy5OJua7LSwB899eKzuGKFUlMlRjj4FkdwcIahO3fK1cdMAsaFu4E6Ph9VJ27tsphZzM4imVMrLmkm_EtgYbsX9dz05jkiomGbTap-0gHfgr2zvpNwB_dI-EsUaHReqnJIinu_YGzpJgybFs6Q2CBlVSnogB4eWgbfp9Gww8J94z0dFj5AZ-ODfSGl176GbL-zxKMkOfoSHx7ZcqHMi5TspYIFNTw26oKWeBCY-hKsDxlLYBDl7XsocFb7yH2QfCq6wgUxNEV9s5xrNRskyQ6fO9OI2tMpIC-_rJhhbkMKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx3J__HqnOSklmyYyaVA67Nvl-gMska38RaJ5YvoTs1Iwg1I4Ujk0YK40IbkG8AE16h-Iy4bCz1VZUnO0NP9_bUIYG8U1nYvoaY4Uhjrc3sSbY4-6kQALTz6FZ7W5N_DBTwP_biDwoQaGCMmL53sTkyC9OIPEmIv8_1h6SM-Z150HmTOvWB6PWHZ-CglPfyQCwWLA1HkvV3Vd1yPblewxsPzKaFahWZ2x74MDm53Rjs9XW_E-riiHwmf7qfpk1MCPc-F2Mx8ZdN0oXrak-iag4KS0av-ScLrICvyaLgOGRrVblFxcvYUSF9qJf7Yej_oxKflaGpX0W7dK-tpGhwU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRicRcpqLAZckedT_5t2W3SmOWpGlIOtDo6J5PFB5jV9_MqpZnbLXO2CRyrSn42fqGgQk20HIDJt1aojO5fKZaDTp1PR46WuDnaNOQvlsymRhER5o51jz6c8lCdfeuTqqT2zB3hmoR-9jqyVQxgsCe6hg_2J0K4Z0zid7TLlTiz5JxNflyc190N0nAZUm733igaB1H3vZhQY3g-R7E1WHbEl2VObToMsJ8aP0HKG-qYqE9K8lopC0BjJUFxHD-GPtBqoK1-92rRymuwIzDJBhDjRmTcXveM4P3SmiYsziqZEgf3qtTEY06WZRedgwRcTIYdU-70c9ZmV8SkgbHg-NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozX8jax6HwsG6RjVa5xHjXUzb79PqW91V3d1M8kH25MSQjf55REd5FDYsANNoQGjwjyozxLJZPyP5Pu43aELXThHF8RYLVBs0LcVosYeOp-19DwNJWtOLEcKolUhLHw441dN9cRBH55iq3Ahpn1NQevszZH4H1LilfWBOePAlMyDo15JEbitrL_Ot0JM8xevXwto8W1xHMVBasiyH40C1DEXF_rfAoJBGxRxpC44V3olGrSUbnJ9oNKunlCUDYMHaEt7JepgyJFrDlyN6Zm0HGi-fB8MazOx-oarBNC3Y-dU-nqWbpcb5_xpGeEeFJq3i8PGYLIIld--Air9iBx28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hR73d7MsxmXnYHhHcpz-RPSVO-qy8xOkfyp8XYGMAXdMxIjrS2TiLxQQjVR0X7M-DR5T2hHqlKVy2xY3xAwGFpl4n48KvHB488rjRv9cEUe97SZcuanTmM08ZEwQaoZV2PuUDX7JYRae6x_pE2BqlL_gtBU7Z9MieQicHzXW9hFZpqgCMejTCVHSAIbiDAv-rb-MGhhXoSnROPv2zT3oqr6I_q_9ijQzpcj_hZvMmTbi3NgZvjMAE4wYkkHT9Lr0AlXnPleFoXBNLQWCYRX7rg7XU_PkEqcbbYZXvmgaNgv2fapuQoDm5XWdGR8uN_rHlNGNL2VJ9Yv13kprW650lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxSArzPI9qTZl0wN9J3Dxb04yznii4SavncZYhAoh3JIY2rI0HPaa1okRQ-7GKdoR59B2EZng78u13kRvya9_uqfhlF5gyZruK67wWrFVCzGYD9rQTLGpbDEoYg_NwhvlmD0yU5Fp9F8_1SeUfbqNPtxA0NCH1YKCWoFiW030tA-t2__9zjfos2d2rlxT7zXdpYjT0lXZ-qUFBP7CGtKCQev89uTNC7PKCPig6iHWLUgwrZMqoTonT-5w6byEpcDcHMOg-cRPQuWWHTLHgQ_-4MUqvFzHcjSDay8b0E4d6OYpSiSl-yIqP6DcBQ4q8ntDcTb9xJAlxducYwTYlREbg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=THw6KkCJv008qWrtnQiC3bj_AtDNAy__TiM1Qk2na4TDNHnIuXrI-CmCnALrLleP4RDyffrMjCOWssWkROB2DrgixZ4MP7vzt6956ag3l9Z_iFDcaDAbewJ9zGFM9TPDJP9Ku0GssJdQ3vp2nSE_z4gbjxVVvJfA93t9250m01jZ_6eG1JDxlJUyCJoPjOUkXENaB6TkL15hHW2HRiZYHV7aUM0WiStqncVIBsG0FHrNXW__EMTwYbztX3wkX8Z4iK61YO-J-hAUCWW-6oSgI4bRyBzWypZYhCtWiMQtM90Ts7IqyKGvQwkB9b0csY9CZ3oVuncbsqjHRvGn1CtwJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=THw6KkCJv008qWrtnQiC3bj_AtDNAy__TiM1Qk2na4TDNHnIuXrI-CmCnALrLleP4RDyffrMjCOWssWkROB2DrgixZ4MP7vzt6956ag3l9Z_iFDcaDAbewJ9zGFM9TPDJP9Ku0GssJdQ3vp2nSE_z4gbjxVVvJfA93t9250m01jZ_6eG1JDxlJUyCJoPjOUkXENaB6TkL15hHW2HRiZYHV7aUM0WiStqncVIBsG0FHrNXW__EMTwYbztX3wkX8Z4iK61YO-J-hAUCWW-6oSgI4bRyBzWypZYhCtWiMQtM90Ts7IqyKGvQwkB9b0csY9CZ3oVuncbsqjHRvGn1CtwJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-BxSyCL_pZClT_RasN6kkHjXNtOc_G2bhIqTkZ7UC4TTOeY6ZRb0nuUlfy40UNaNBxtAu7VMAAqrGItyAbgaP1I2on0KiFyq7kytvycUe0uAxQrpmO-Rnq8ZcsnfR9W1USezB24gZfbWNRgEmIgmBifNyolY8ycyUv65TA4eTxoRKIAmiyYGFw9NbyftlJA3vaTvn4_-ui-GS-Mya3VJvyDlqXrqBLcXQykzkCiZcRA_SAiiOYBIbw7YvzORPzY48-utUbn9ol9N72JTSfH-Ap4CnR8ZjRxfVzVzROFeCBvft8b1xxdVcVMj3ipvTk36xo7QbOL75dFwpHEOYDtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3f5xGz_sRz3GPmyBRTgSpCe_P8IKCEU_cfGP3QQi2RB6selJcYTOdxt3g16NCEjO6bGnMGJal4Dt9Ud1OBQtoupuof5C05P3LY_fUuJ8UDziGVnOCHa7_6TOgVVYMzfrXGfi_P9IsjoBTeNNOwODJslildV9xY0ipmG3jLDHVsgGsiw6kBhX5TyPl89WKySaU28a10ws1nhispBYGhl6OmSnUakx03Q2hkm57bEIDIKkCiqHLFNqFlvQgRatKvDepD3zgPhXeUGtH9pZDy_UoiFAKGtm7ZhassU6RU5X2JkY9BwRCHYDnRuoLaEjMub4uFAd-9_BjMS-39ny7FyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlFTsyLbZ_huG-ilruK3wivRS_XrV6b6krOrsFXaqrsFVdrBt6HBA348IoD34ygXGNgpGSXJ2OsYYCd1QeWb0xOUh00WLfc9ZJO69a45CZ5bbnXxzt4SUrGzNKyk29Znn1iLVvIpDFa_kDNjREmYmvtH68r32wUWPbQYaENzeEL4gWApeQI6E4msNNm3Q4ixSBjd8mR2os4SOgWGVGHpNdzdu6kMSK_0w6CVeQOu51xmt9SiKGn-KolRP4zcwAXxKuCdMwIGLss0WasVEihGWS7K0MuCMlCWT7K2qQrsbY2DG3w39VqRL39htY5-y3sCufyDkZrTzD7jeWW8DAQ0RA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=QsGYHJS3ifxoFwWUBbI4XDQBhKx8koFd8bHGSu8adkmolz2uFVYiyl9auF6s4KmS7Qhyxl6LlawxSmQH74GKybGZ7eh5CHViy1YQFqCcV2eOQeQIPWXzdjq5nAr2mJ1tnL-wWIbD5EiZXJ38hW8lnHPkfbA0IrV27Axc4tJ6TGpwOzjc7ot_My-EeTPuhDGxZ8NhAZzSD-vZ69LNJngCJCA3WV_mgCnmsqGnejbRgnF13_Jxe_ArJdCnh-gevGpLBnrwdjElRZ9HxhejpkSWYHOHORA4X360Efc5Z-_-48Ah3aUhJDOnr4bFbxbqCF1WRxUehP312QgPMY_a9eZwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=QsGYHJS3ifxoFwWUBbI4XDQBhKx8koFd8bHGSu8adkmolz2uFVYiyl9auF6s4KmS7Qhyxl6LlawxSmQH74GKybGZ7eh5CHViy1YQFqCcV2eOQeQIPWXzdjq5nAr2mJ1tnL-wWIbD5EiZXJ38hW8lnHPkfbA0IrV27Axc4tJ6TGpwOzjc7ot_My-EeTPuhDGxZ8NhAZzSD-vZ69LNJngCJCA3WV_mgCnmsqGnejbRgnF13_Jxe_ArJdCnh-gevGpLBnrwdjElRZ9HxhejpkSWYHOHORA4X360Efc5Z-_-48Ah3aUhJDOnr4bFbxbqCF1WRxUehP312QgPMY_a9eZwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJsKScbo3eI-5JMaW2R3aD_VYOzlK-uvsGQ89hHUApjK5HOgxjhWL11HA-6TBQoScnQw1c51PtPZ0cnFxIXp5MQt0GWjMhxKkfirTpLhQ5klqVg2njohdFtIFiQP3J8kzuBnv20kuTmlKw7sSAjSkrJ5hGvKDSs2EoV_70UR3HhYEfiJC87Z6MgJY0f4X8bUWGLbOPB3BDkzNuor_uPlNOYiZdzZKsX2clWnleCpvAVI-qaLlwtDTLSEbRA5OvnkjxzfEltCivDRo_oRD9-RI2jPCCVnryTDIOWtaKuNyyMGETen_z9Q2-50hsi1_M7Ktn9OQXN-OaHvew0pizqj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=LiTKzTYWk0AT_qXZT57euqsoYOQdq0Vdj08ORSFgf4SmBDGfAHb7aIxsoNicw6ZVjYVqWk9nuuntGO5XBk5d2Bb3u7P3PWp7Mzkzsd3t0Uen9rMj58Sg4wygX4GOE1Ro90gVMFadwok1K3Fb1IuN4V8vlmMEXBQGBLvnnmx9xk9w_r0thFtT4U8gjMomAYD9fc6qAu_uNd11fxwCQWSJkByuI7EdYjUkWsVEKmwKMlCy6fAsvAkQGqEj1M1Fs5nBb-HrMAtbuPqsqyXQ5oNqd70PQMzbrwFr9rEUj_pb3ut41rAjmB0f-GlaO5x_JBj8J38lAa0eYntNapPXHv6QLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=LiTKzTYWk0AT_qXZT57euqsoYOQdq0Vdj08ORSFgf4SmBDGfAHb7aIxsoNicw6ZVjYVqWk9nuuntGO5XBk5d2Bb3u7P3PWp7Mzkzsd3t0Uen9rMj58Sg4wygX4GOE1Ro90gVMFadwok1K3Fb1IuN4V8vlmMEXBQGBLvnnmx9xk9w_r0thFtT4U8gjMomAYD9fc6qAu_uNd11fxwCQWSJkByuI7EdYjUkWsVEKmwKMlCy6fAsvAkQGqEj1M1Fs5nBb-HrMAtbuPqsqyXQ5oNqd70PQMzbrwFr9rEUj_pb3ut41rAjmB0f-GlaO5x_JBj8J38lAa0eYntNapPXHv6QLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gwh70bXwhf9kyMtjUlu3u2P2zMGJGx0bX6EKaRRqKX4G_MSTF0wgvmj_Lh9ZNk3aBBfp_ZMKF5VI6kIdbXb3R7Yz5UQKDoVBnV5KaDqKQsSmHPuPn3Z-BiwJ-cBDok_q76WSlofVObpaPvJ3HPo_UJkUo6_jlUB6gKPsV6FveKSXd9vZcQjeux3vcfskLFnRHQiBtaK04H3QGrUto3lftiK6hkDa3Rh1lvvVSFSQLqZhY66RTSF8rAYR0h0RZPguTi0JuTjWoNWkc_IeBttyjLwHUndd9zT_ANBDAiLJ_iSgqLN8uMBOiwFT36vtehN2V-RmrRvjU-wfX8SHJ1Q7Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDyiChdI9T05beECtEs0hqMiXig7atBaeP7Lv6mHaFfe3LxOnpeG1EbIW_yynFNYtDp43GtYL9yqVeUmv9-li_oT8bPh6zodMnBBqvK5teyJM7gzDepCP5ZM5FejlNpr_AauiGSCkGXFujjv_Az0yMQ7YYob3o_WpwgpNxY7AG2dKoYQUmBWz88B4HmmW5X-g_2iBZw0j9l5ClqMGOyWKM7WYmj8rNVEloDA6r1TUlJYxmdOKtt0llT14QfHjKg5YH3Bki50H8Hfdb56kWlzAa24mOEtLe58E3tbusU2VfrTpPnhDdyEvON4Tc-5v22FD4DnsngoUpBXYrZdqd1lXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=LKu7fhhTbqjGxNKNvsiAk-k8Z7NfUSIx-xvGTAsPHGOupAmv7DhaKzE59VsLjkqmIAJJBAXMHjkocMMf_7OazpmziCR353vf2ODXm7oUDu3DP_mX3g-OhmawOJybjgNRy4xP9nl9kzolt7ppOo_EVet8lMzo0vMLkYiVEzW0TS0MBam5xUeuzkvErZBl4Mn4c-6BqrIsNzWRXgVVEkak1rrQB6ytIqXDOVZ19-8YWmTN23B5n60Uurd9WZTe6_3qJb_SWK63P7GIArS-H8iLdsrUggm59fxwEIEFsqubCaobFOpaUBLlfcLt4bryvln8gqalXih7IO7OpkJYM4bD-HOIaHrUj-PhqPzzDGki4Okmiunc_J3csYyhwfPcPQFQm9NF8zWbNazTAG8Inqv0aU2WuOAQhOuEfYYaZwWbCy-RuX5HbrC7mdcbf7Kt6sAHIEz0xFl8SWCIKS8WwqwZc1mWo9xrhCdecEmHJn1wwblZEJaMKC3IfGdgdVYcjqnIBC_-IOr_5z0klcsCZnuZ7rDXAMJesFVAEGWpvy6HXJC-dclu8UrBFBNURA73u3KDWTsAmTw1PfG9YkOfN-GWR4GuM2baNiFQ3hkRFY2nyZpjrqZFaFN1JAYXJHlNNfAl1InuhEQ3ke_wb4wm1J7GBeXcUflPzNuhIQXAyHhg42Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=LKu7fhhTbqjGxNKNvsiAk-k8Z7NfUSIx-xvGTAsPHGOupAmv7DhaKzE59VsLjkqmIAJJBAXMHjkocMMf_7OazpmziCR353vf2ODXm7oUDu3DP_mX3g-OhmawOJybjgNRy4xP9nl9kzolt7ppOo_EVet8lMzo0vMLkYiVEzW0TS0MBam5xUeuzkvErZBl4Mn4c-6BqrIsNzWRXgVVEkak1rrQB6ytIqXDOVZ19-8YWmTN23B5n60Uurd9WZTe6_3qJb_SWK63P7GIArS-H8iLdsrUggm59fxwEIEFsqubCaobFOpaUBLlfcLt4bryvln8gqalXih7IO7OpkJYM4bD-HOIaHrUj-PhqPzzDGki4Okmiunc_J3csYyhwfPcPQFQm9NF8zWbNazTAG8Inqv0aU2WuOAQhOuEfYYaZwWbCy-RuX5HbrC7mdcbf7Kt6sAHIEz0xFl8SWCIKS8WwqwZc1mWo9xrhCdecEmHJn1wwblZEJaMKC3IfGdgdVYcjqnIBC_-IOr_5z0klcsCZnuZ7rDXAMJesFVAEGWpvy6HXJC-dclu8UrBFBNURA73u3KDWTsAmTw1PfG9YkOfN-GWR4GuM2baNiFQ3hkRFY2nyZpjrqZFaFN1JAYXJHlNNfAl1InuhEQ3ke_wb4wm1J7GBeXcUflPzNuhIQXAyHhg42Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=CACDF-Zd7U4Kv_JWGZoaKXxeVVxZB-uG8U9kTJcgIBx8ilsv4lGrY7k6d73iAb_vJkcLWIQoU9HlsKURHjlaNSW_J8YOmAubqM86MPD7kqlP6LlIBXEvx44kl1_sZ6JNJ_fXb5KZlQ3DEF9JtEZBXXg4PghyGvzvxeALb8xFwKtCLnJHklebTjh1phg12-eGtFfJn-8PVGPkmup0RVqkobnrcjwDFT8X7gUnE8FAFIJO8qPVh78JRENf2AiK8smm9-SvutycDqKZ4s6DFpw3ugBBn6btmw2p3scqGwaUa1Jimo3S9SvhW0-67zEgZgq8nJc_XInIcOSHZztMiP90wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=CACDF-Zd7U4Kv_JWGZoaKXxeVVxZB-uG8U9kTJcgIBx8ilsv4lGrY7k6d73iAb_vJkcLWIQoU9HlsKURHjlaNSW_J8YOmAubqM86MPD7kqlP6LlIBXEvx44kl1_sZ6JNJ_fXb5KZlQ3DEF9JtEZBXXg4PghyGvzvxeALb8xFwKtCLnJHklebTjh1phg12-eGtFfJn-8PVGPkmup0RVqkobnrcjwDFT8X7gUnE8FAFIJO8qPVh78JRENf2AiK8smm9-SvutycDqKZ4s6DFpw3ugBBn6btmw2p3scqGwaUa1Jimo3S9SvhW0-67zEgZgq8nJc_XInIcOSHZztMiP90wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceruQytfh5wZMdLrEMhjxt3aitlBAO-NIAurm7QygdUEtV5XL1XUYmlz8q0cRd_u5hJTrEbHRpMcoJAmwXzggwEHBEd58_D1C7Jq_GW1youB-RDtDnDBmL5zFUDpAj8WOwxmmSfoYZeraMC6uNUXiOx2EZ58TU42TacqM1ReQaFozimBeEbRwEq2fMLJo9_YEBjYsIx8y0DedeWw7nHdVQgAMXqSEd6OAnuiiN2qYK3yn9j6PicDWqWSRMY0z8y6QxIFHRlU_ZPD5WoSB20PGDwADN2n4eXxZD1vVBepKSZrrnMWNtTuYCyg1tSK88xEUry-0Ece2D1x089f0kozxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=i3T2Wav_LDUOq3EAETZP027VRvf_ionDUTBuFctP95iBZfiSsfqM4CGinE_xkn2lTwIU7Z9rFj-PMP-uBnkI-oQ-NxNhErvFq9t8w1cimtIrnexL0vmIO8pe_sRKOWkz95xTRLmAqNkZRI5l6Qc-qSVkTuTqtzp6Hvh6CLj8c3AKa3BUs20jmzCvpbfh7BWeo-IUZXpCpt-83AmyufetslC3tLLuvijYF_h4-hnSLALh3zCa0DM90XQVDtv_6_gom2WBMK8C7ofDlH80apRiR1t2lSD4Ej8S-qnN2I5fRu-V28pjFGzLmIhIqxpMcohBNlxbJ6scZxSQfZL_xTxO2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=i3T2Wav_LDUOq3EAETZP027VRvf_ionDUTBuFctP95iBZfiSsfqM4CGinE_xkn2lTwIU7Z9rFj-PMP-uBnkI-oQ-NxNhErvFq9t8w1cimtIrnexL0vmIO8pe_sRKOWkz95xTRLmAqNkZRI5l6Qc-qSVkTuTqtzp6Hvh6CLj8c3AKa3BUs20jmzCvpbfh7BWeo-IUZXpCpt-83AmyufetslC3tLLuvijYF_h4-hnSLALh3zCa0DM90XQVDtv_6_gom2WBMK8C7ofDlH80apRiR1t2lSD4Ej8S-qnN2I5fRu-V28pjFGzLmIhIqxpMcohBNlxbJ6scZxSQfZL_xTxO2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlugZNwdfoWIH7W7pKb-Bo3h7gQ7Dz9qx126H-k768L5woS7ffJx5cIOQE_Rore9vY1_wmNUnDOqsP9-d9oQDg_bN5lYEkn-hWRfJ7ejlrslbi9tyn3H8ltbU4AXxrYAULHrMH-n77wj9f4P23FKKrE4kUiVLFAkMlqnCRBosuE6hBKnyJZQGmBWdiEpK5JB13-8Dpw2OgKyg1onSO0VwmbEr7eHHg6plBdqUdx-cjAynIX60hJXH9qQ6H3QLOCXUw9VEPf3JeYetfNNkzVeBZu4KnrtniU6I_HUgevTDfZvCU-MMjGH7EwUAXdJd5Hl1njHQp7ZLrAc9-KJHl-Ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHgelaAYqEDgGFhr8N_jFgEA9zjPC_xu1s3GIjiA4BRNHyreGUkwOon3o2JGEzicVT-MqBd0n1p6CtBL6GcMPy-qGsASKnQ_gOogyKrKdRtbq8yO_jNEOXLEdZlVuhpJfpyb6Ri0Vb3FTPB3dXisOdlUTTNdS1b8vDEpYX2q2Wh21uR7bitYStFiFwae1WpL0uoKceQCz8EEkn0XYSyZsM9C7bpAUgOAhOovV3kOsUyHLPIuDFSWGLPI6u5ZW2oivK8aPEPL-53HA4CY_NYjIB62-B5-IJIIqCHEDxd0CBiJq-s34NwoWUQ0G0u9VmjXm5bG4ZiW-D8_EsbbXHCusA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROYuiz7d-bvbKKWWs1iTzYHjiXYa8fV4qvFzcao4ljEb95Ds9SDoBm2gIs_c8qZdkXRSPvfHhylzwZCNywxjygqSZv66GRfSGlCmq8QReXfyC7As2qiN3gIWl9NGHJVdTnvMdjl_RuqDFrFmVAGxkR8hZ_xpv2rbW1A3HfWiUlgbnnXM6J87BXhWEFL3GewQhvp9O9M7bHhx3m8HUNJ-lmNhydvuOfkpmzenkirBCW3kDgUrI5ig1sh84GywWfBOw7eIWr7eCEcPp0geRFVuTBXUvoB9VUTVn3d6nohAW8P6M8TMnxB2NfIVSLrMzUo6iVjFT6EzpLtNld7T3ZNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTcvBAJZCI3ktSfhX0iqY-3EJFupsOEN5rYTb34Yqdq1yE0WB7l8c13dR6Z-VaQJ2oiEfpv6bUCoMsLRBo9Q-Ef7DN8pkpSVXGnU56S5aE8deqKdnNxmh2pecmjvEl8ryKFTFIMMEmrmdEaVQALZySmrbieGJVaDOqossn5fSexxHBWeo47mdeOlW99yi2U-qSvyrG53EVCdKI2o0fwZQkynAKU64XZ7L2WrPFhpPghxyHpGM-RYceb0a-BrffDQ2MU4CCtacwkVNtWEl72TsM6eCWSCatB7FOG65oZZ0jPq_2n3Xu52u6qpF2Qfws5KIHyMBjSxj2mfySQzDdRuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWthXCNEfaV89AtBbNeYuOOru6e2NGJ3gZKWc2S47YRX42tl3RpOhKQZ7rFgub4xJpGPNu2qY5Po_PCzjC7M2iWAMuVNqH_daZ1vThgCVuGZ_SkTVoB44WspQ9MCn-nX0FrJFW91590HI_McDHVXdOxndfL4fpY_LUpvtAGUJE3BZGzukapPVLMCaD0OFXD5BlSRQ8B3QzgiYPML_FD6Fqw_Brp6D5foQzP55977P2le98woIUG3MO8lBCIpsUeAeVQvcOiyfExwMWVI9f7btnuf2ejAvMZMnv7ihNExRb9iBb5y5axVyHoEHSJdIuCdcTO-W82_vW2MhrYg_9_3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=DqtQnQKZ6dqDREWdJIpWicF0PV1pFqgjqLSgoCOgwxm1kDJvJ61i99JmtN08esMddm9zprcnlqcoZrosU27cfoljd9MEtt7o3BySzmOckdgNtm9xQdQgGu6mp8g3Z3EbZXG2QoWr0Wg1mCfxbkv-o7-_t3HDTf9Fyi11pH8Ih-vNR9q6PO6mmiVuCseh72OHJuICSSMK8Q38MeIa4oFjFF72Ih9l3t1bJbsaTo4bxy7MF1RIorztPnpMdWwbSFQICphkEAkvxg5hSBjDMB6k69GvHUr8F-AUj4yI3qsEVl3lv2bix8oB9gpxwtt1Scve9OmRMojiOLi2IyQC2u6G9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=DqtQnQKZ6dqDREWdJIpWicF0PV1pFqgjqLSgoCOgwxm1kDJvJ61i99JmtN08esMddm9zprcnlqcoZrosU27cfoljd9MEtt7o3BySzmOckdgNtm9xQdQgGu6mp8g3Z3EbZXG2QoWr0Wg1mCfxbkv-o7-_t3HDTf9Fyi11pH8Ih-vNR9q6PO6mmiVuCseh72OHJuICSSMK8Q38MeIa4oFjFF72Ih9l3t1bJbsaTo4bxy7MF1RIorztPnpMdWwbSFQICphkEAkvxg5hSBjDMB6k69GvHUr8F-AUj4yI3qsEVl3lv2bix8oB9gpxwtt1Scve9OmRMojiOLi2IyQC2u6G9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhS-DMB_rj7aPGkTLHuQFbM4kKK63SUFyj-vKJMLZwWmxOnR5yX79VzQTsI5acZgr5UI4eknyOX3Rba2cBWmXRq7VoYal9790DvZgl6D7TC4mAkJvONCXRY-STmkVUv5fOG_9UEGX_55L1xnFDJuUTrR5ZukN4mAATYt_NLp1CNecSCTllbxBE9gnMt-0LCfsgt6QHfedX96kzIk8IZ4n53_RHQCWIUOa5GyjYsG2g5c3pOelcqgAZbnaa5oOG1NCT6XJPbH2Q3gJNdxwUewS1f7zN46CE9ftyHfRIClspsQ3sPc_-sy9xqAW6_HMucs83g8EKjrvVyLobUk_SpxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs3tKi2pChfFmlx21B14Kth4ICBdbmSx90FFhZqA5pzE85N-yZoqt-Wl2oft2ygY_9Q3Oglg-vyVfvrc4p0cyZwXY4Qucw4qElFBnja-FuCcSFP7SeE5558u0WsvfyIjthF-JBVWB4HHIDcInkrc6nOxOWkYx4BBxU8F-SsXwaaACVmKDvd1c3LLR3MVzedgkpi8cZ3TtJ5YdxAkapQs6o8wHo1Q-X40szFxA9j7LwqUOPBZgKQsHySKVSnMQ5EOcqQu5g2RZFo8ptDba102rnaoWbdLfMIDSVgIkxfoLzWUA28jgHFRRqtu0MK6o5ZfbMIHqc28xAeTyPeiapuqUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=JDYIwt-E22aXasaPPxVM0p7-yWgKBteJZL95OnwVBJrNssHJ7Gc-i8MIue-HXvlqnlhJMurBJvIEsR1py4H4szRME2dgv9Ua_8m_mv0Smgc7hBMoF8RDJrv9DUH6IqM81JSsBKYOwrMQc85EKYdBaTvtvehVuskKSajSSYbWUbvoGjLK73ySVt43KvLshXM5VSXQY0q2e9Z4Mp95k4Mly6nZ_XhKBP-FdcwBMD4EW3YZ9--0Bkl0fFQW9OVWo0xO4ul9NsMa3QOgl3XxP2n9BVioQfPkkh6r1N7KeKHzBWp_f_XahhV4sBlciGpoILEobePkCRHQ2BqK_X31uhl9BHxXEjVHoSF_0SWy_nX9AwkB964wUfLztirTcYYodKFa4luYvx0pqdEo6iwu8QCJzQgp_FbNIE536EXAFhRKrIi3fz0NTnla7P-KMuEPKnreOnAf-rQ6LhuLhlgETufaNtDLh5zNthRFx_uq_-NHI6UrpzZMRW_yAwdFUnzfEgxLXdV-y62q2udmCbhqa62v3obUhC4RJrTw2vTfqhw_3I1UC7XZqYcsEugwPdSW5DnlcaYYrp1OWRhkEgNKAGQgiWQYxKtCRkc7qzZ4h4QokPX7yQNSHhkJaFmHSMjtPn7R4q1VCFQ_CEua1B24R1TJrZdVj1jSHypkTXRnsY15Ec4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=JDYIwt-E22aXasaPPxVM0p7-yWgKBteJZL95OnwVBJrNssHJ7Gc-i8MIue-HXvlqnlhJMurBJvIEsR1py4H4szRME2dgv9Ua_8m_mv0Smgc7hBMoF8RDJrv9DUH6IqM81JSsBKYOwrMQc85EKYdBaTvtvehVuskKSajSSYbWUbvoGjLK73ySVt43KvLshXM5VSXQY0q2e9Z4Mp95k4Mly6nZ_XhKBP-FdcwBMD4EW3YZ9--0Bkl0fFQW9OVWo0xO4ul9NsMa3QOgl3XxP2n9BVioQfPkkh6r1N7KeKHzBWp_f_XahhV4sBlciGpoILEobePkCRHQ2BqK_X31uhl9BHxXEjVHoSF_0SWy_nX9AwkB964wUfLztirTcYYodKFa4luYvx0pqdEo6iwu8QCJzQgp_FbNIE536EXAFhRKrIi3fz0NTnla7P-KMuEPKnreOnAf-rQ6LhuLhlgETufaNtDLh5zNthRFx_uq_-NHI6UrpzZMRW_yAwdFUnzfEgxLXdV-y62q2udmCbhqa62v3obUhC4RJrTw2vTfqhw_3I1UC7XZqYcsEugwPdSW5DnlcaYYrp1OWRhkEgNKAGQgiWQYxKtCRkc7qzZ4h4QokPX7yQNSHhkJaFmHSMjtPn7R4q1VCFQ_CEua1B24R1TJrZdVj1jSHypkTXRnsY15Ec4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=CEN5yjaSFrHXaEqKBLsBs9262h02JayOqMZE06Ei_JYpp6h2YZ6ZiqmiJ0jk7yBZgsMinJvMFqJdSxxpo7gA2sJBcg6QMOFj8zS_30PkvqABMp3t8zmtfeLUIeI6Nc2quZwgx9s82d-yl8csJi1G5KILHYO_3upOYKJ0dGcVmOig6P9R5FfhWIQ80OsuvSPHKbChdBQhp_gqYUq_aNMHuYb2Hu78_wuw2S1vBe2JGbU21_WRngYibGeLET59wdNynqCMwf1A4Hx8gs8NWsUwUcb0_2C9pX94rMWyQzmA5Q0glDitjl5rH3atOYFrnQJM2x1Aql-rgHpqsE1ESLNvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=CEN5yjaSFrHXaEqKBLsBs9262h02JayOqMZE06Ei_JYpp6h2YZ6ZiqmiJ0jk7yBZgsMinJvMFqJdSxxpo7gA2sJBcg6QMOFj8zS_30PkvqABMp3t8zmtfeLUIeI6Nc2quZwgx9s82d-yl8csJi1G5KILHYO_3upOYKJ0dGcVmOig6P9R5FfhWIQ80OsuvSPHKbChdBQhp_gqYUq_aNMHuYb2Hu78_wuw2S1vBe2JGbU21_WRngYibGeLET59wdNynqCMwf1A4Hx8gs8NWsUwUcb0_2C9pX94rMWyQzmA5Q0glDitjl5rH3atOYFrnQJM2x1Aql-rgHpqsE1ESLNvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCklKbQxukTsYGahYX-zbHA8OxGEuTtTfxlFY4OWGSR-UEzx1DO-oYcnL11vhUWTP2RbyStdwUeHWCeESg_dDq9ZcaqGT8Vnr1xVkzVY29uHhTetCrCB95AY82wdWxk0nC9Ma4NuLAZGZRQ9yI8cm9fxrG7RD8rIzeAQWXmt9EBLDlf5wfQHOWn90y_mB6cPCN7nfnvMStWN_zalNc9NlDCs8GJuUA-bCwQqWzEEW4Cb3CxVj1Z1Cj_WbCf-6K36PyLh_kFcoeC2S7muzXm8zfGql-Kja2vHKyyEVt7c1S3gUAxPuT4dUyYgAZAYzJ7ucZx_sYQ0fm_AUso-ZQgfqk1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCklKbQxukTsYGahYX-zbHA8OxGEuTtTfxlFY4OWGSR-UEzx1DO-oYcnL11vhUWTP2RbyStdwUeHWCeESg_dDq9ZcaqGT8Vnr1xVkzVY29uHhTetCrCB95AY82wdWxk0nC9Ma4NuLAZGZRQ9yI8cm9fxrG7RD8rIzeAQWXmt9EBLDlf5wfQHOWn90y_mB6cPCN7nfnvMStWN_zalNc9NlDCs8GJuUA-bCwQqWzEEW4Cb3CxVj1Z1Cj_WbCf-6K36PyLh_kFcoeC2S7muzXm8zfGql-Kja2vHKyyEVt7c1S3gUAxPuT4dUyYgAZAYzJ7ucZx_sYQ0fm_AUso-ZQgfqk1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcZ92PnnhgV6I9afnEYctzOtdHThlOP78lCMAYAHXkDs5XOPUTxh-KHgoDBjeH8Ou-nj2BrpLaophk_1oE-HGd3qgZzRoncQEQ7-viHGEcVD51xhRlkCQlLJS4vRqX4w58QdjuTs490-vb9ejagB0ND8ZCmRiUe4sQ2Ytb7WI4n0CPJpqv545bed-y1pRW-h37UUiaEm7eJ3hgg44rlaFbDeznhrmJgRFc-kMEz01C-pnevfGarvqMbD7GVAjd_C1KevPjRW8DHOV0SQdruhNe9DTd8bKhLXwqPqyEqqdZq-CqfC3zRhbgDyzJ8hH-yqCXqu7e4K4MKeiYbDY3gF7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF3gJxbLX6aB9I02KDp9tfRMgjPCfZLcuZUr6MJIUzhk2m9g7LeULGbGtmdY15iXvb5oVGV682rA3Kw48YLaxcoD9ac4mZL1q5js6rvIIiB3XObKPaeT7tDiPdsgi2udS3qrK3BTZUNjJPMXCe1urcBE_HnyM2Bx8Wk5FIRm6dW_3Z4NP3eSpwdLxh27M2L6QvCztXiOrSyjv4lsGC-1cWnsIMo0_EzP-rXGIL6aihtGjnWzey_7ms-sTsfm5X35qt76cHucIW3RkldXQfx_bN9cX-OAyiqH1yW-jl_M2JCLP7MyD2Ex7K0gE4FjtxU_I9vXsmRANyEcWUQ9eu_FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9ur21rrPuJAlBDQQH4CBm2sKwUVCoouZKnPrH87RjRfIIfYnSODAi9tp8J4lt21kofv5b8vK7jNLA0EBLBA6Y3pdg7TJnnHC9cSx7iDe-i8pkOuJSGm2CUI2rz_Aq_LkBf8fB5RzXtZZYhR_hfHU4prwG_NZTRCw6yU6aQtuZsMY3T4WBktUaNH44KU2-7wa548eMwV3G13fj73cgtQimJmLRqc9kQrqn3Wp6yoS0xOV6Z0toqsTuDyImCXPwmkREDLK98cZFVjqZC4O9LxM8EaLglkChMTXE6z6FPjZIfbMb8p9Mnfb_N9v3yyxkyKGtAiR-H3-0SJ1xKVtglHlw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=mMwKyEiBKwxUsf65gMs1peKaDLul7QhsWLKh2yv_BzYBWmLCvm9fpQJr8n1gK1GNrIts4niGBrOIdLLGfu2jnsCujTYNxg2nVCxuUV6O1NkqqjV66T1uQY8X0lwaathDKB2V9qdhlFPb2Sa2dSSgIb9g9X36uJlgk79TN5-DGTLer2zw5L4bKTKKjthX0nRKLQ-JXZZghoczwgmJ7novTtGJWxrqgkptWpUTdtje3EJzaqHU-tVbaWXSypgHpLnJsLxDYK_cVGMMjeMcVgMbsjjvn0BVJdsti3ZErFmFVI7C7l4ahezlslsE3Twsh4C1Dk7SwL4g7rL_YoY3QAehcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=mMwKyEiBKwxUsf65gMs1peKaDLul7QhsWLKh2yv_BzYBWmLCvm9fpQJr8n1gK1GNrIts4niGBrOIdLLGfu2jnsCujTYNxg2nVCxuUV6O1NkqqjV66T1uQY8X0lwaathDKB2V9qdhlFPb2Sa2dSSgIb9g9X36uJlgk79TN5-DGTLer2zw5L4bKTKKjthX0nRKLQ-JXZZghoczwgmJ7novTtGJWxrqgkptWpUTdtje3EJzaqHU-tVbaWXSypgHpLnJsLxDYK_cVGMMjeMcVgMbsjjvn0BVJdsti3ZErFmFVI7C7l4ahezlslsE3Twsh4C1Dk7SwL4g7rL_YoY3QAehcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
