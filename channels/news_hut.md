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
<img src="https://cdn4.telesco.pe/file/bmjhguE7-B_4R-d5d-6kt3pWt5PTtMBjN8HrV-jLPT0MbUeZ0BruyxftwrYCP6CSSm0A3GCbksOQKr0--_JBfOF-rVkCnwWYrNfXEfFf02rNJrW2DM3olh-YGlTN5u-8t9PFqg5D82n0cTlqIwLYfwIrz1qkd60q7Lppf4YoZKHVYM0dPbSz0-qct-nTrQCzHdERfv9ckxh0SAcXMphRBlUd0R8W5jBcO_aCsZMRGN9Mi49762ooA0yHfN2yHVMMp37rNO2JAhCpgHowbK7tOlvf3B60QrfiuaVU2XXPJ0wxgnnEHVUyax7-4IhNCTK1fzaMPpAO1chuyqRZRhV4_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 142K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 21:07:19</div>
<hr>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYUEd9QEJ1q1FCuEWNy1x2C-h-CFqCTvn2UyVe8pQk9DQuSsBhKBqL1--2O5skRcAtHDJOE8J69MZ_qqxdTiaWfWuPVY5YlRdUtQKDmxnJj8sVPftsgo3VNUHfN1auVRTVfB7wbOnuPYq22P6wOUXW4h2CfBWfuMtnVfjMogb4kP8Fe5XLzAHfVwj4YT_ZJEEdVZ3O95xl1hIc-wZ2Vj2vxvHVJD01isLRrMJFk2vs49YFnleMr8v8VSM_dMSQPQQ22toeXpS8llnfLFMsPcbIOuSbLJM_lQIWDk7wkdhN_sAlLyC2TB__033cfrtRABpYMu283gXo80tcFFzCqopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcxGPt1jEVhsispUmsHyyqBmYDfH8k0Gqrg3jN5CBVcUSpjAf3k62ue0BxaXdI73TN2gfu5JPkE3a1ih7BbiwXh3IKEyrYjS1Fh9_0D9Pbmrdjz78l4dgYiDmHDLJIz6gWnyzz8wHBPG99ki-626rCxnt1XW9oAPl5S7TKDhg4zkLwQDynu1XYOmfDJMYEcdu6n_po-FXYDQrQDLBhRGmF98lt7tRjuE4fjcN-EdWuspXZHVhZu7uc_f0uHKae0h9KXjPGBWXPwCgwhlm_1VZtXzcXtO7HvWBXPuh9NsehqYDjEeZCP4fPccsQTmz28jbx7xie1ctDkcNAtMdYVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZPxGJolenhBv6yG5U-NkEW1tz-mxW46TthFGR7Uyvo4zx50vKmTitj2Hjhypxip3GgzkIFQvYUP9wZardj0_M5vfnome7cE9P9LY81RYsDkYoR-MFg3d-H-5m29WgZqTpqt0c9bkOcU8pDXXX4ClxCMF-53Atd8zt1m4Ci-XesxLo4j6e-kosbdRBJ3SbBefncEjmosPipnxm-Okq6iPi3IP-QtDAbgPsquIwAYDSdPZH8fIi1uNK8J9wZTI1KhdO_lXN931G0_Bj5EWJIDcgJk9wdiws35tNnhz3tMrtJKRPqAb0SPbETiNpGBEdAm4kgEBxAqY0wi6FYFZoeRdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=H6gBRsLqKvzb8YY1d18CuxIlxsKrpMJ44fxA0029gMXa1sVTZggkqBK_jaiQwD12dc-9S8aCvbP0UwPgpcnIbagL4UDV62QZ_fyRbp04p49JV99-pyPGRnu1zriPB1Pm7Of9jNS8WfBk2C34bWIEYdszsPgwh35mPYZaoXozh_Odfyghq4sEczhO2-Jhj7l3xFoUrbLGzGVus1c4uwQi4jVP7zktix6NsAhCdR8RD774VOi3vupEV726nCSz_hsgZJsOXptg6lgpaSasXytX1nVn4ReuCJiJCEh8LFvqSP_nh7YjpE-Kxy6DeejUOikJP6aO8n9p20sH4wIdqHM5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=H6gBRsLqKvzb8YY1d18CuxIlxsKrpMJ44fxA0029gMXa1sVTZggkqBK_jaiQwD12dc-9S8aCvbP0UwPgpcnIbagL4UDV62QZ_fyRbp04p49JV99-pyPGRnu1zriPB1Pm7Of9jNS8WfBk2C34bWIEYdszsPgwh35mPYZaoXozh_Odfyghq4sEczhO2-Jhj7l3xFoUrbLGzGVus1c4uwQi4jVP7zktix6NsAhCdR8RD774VOi3vupEV726nCSz_hsgZJsOXptg6lgpaSasXytX1nVn4ReuCJiJCEh8LFvqSP_nh7YjpE-Kxy6DeejUOikJP6aO8n9p20sH4wIdqHM5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be2cNgahM1VVjqgLJDxeYIWb4gfitHlthLFKaOrP6FDMObnVbxqcV8kLOzi0KdvNE33otGeIpnbFiUu80q0tDmcX6benKx1EwXukg3Hsu6I6gaM8lmM-LvJ8mW08VuFl428o5gmyxAERGaVydRo32ZSp9U_O0JelvsPbTmTX_LMogyBpucvAApoMx6uvTKCPb31ijf_CZILTZD9B_LTE_MN-0ZkdPPD2xx_dskDMvzpwanalYt4tynjZuM8fo96XCZOgXKOVOFa4sHCsq8wS-u5hLWPz3jA6aJ9spGfF2n-qIiU2wayCva9Bb3PIoxSoZmyXoxODUqWUzhwM4kMKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FasRPezAv-9QaKcS-V3yEYU4cKlqbxET0r_5xDW0QITa7a4dXYGeKyp8F8wCFtdXBGw85Cu14frMmtNPlHvJBrH17-9LeYxsoAF8yL8ycpl6BPJ_1Ha_X3tYUb-6K-0f90ieetPFuWGqLquvoIXRf14S1VuZFXrSNMxGbItJYqsKxi8D7WW2XATJnMoj0zQTOpiIVbJK9wZd_QZEN36kiUNJK4V3VHCa-VWIFxfcT6D5GfEsSrrfR5xpO2HWyfIoymx-pQim7ZwYyReuvypUqCTwpGJ5jVMXOFIvidWDR51RwNwNxYcN2bdpLcl-t8CJsio0Cp9vos1D9c5Fkqcmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=pkj68I_AqkePWocGdDYv6utgNlbMM4AfSFD4i9c2T-cMPRcab4XJUVc0KHraQUZW6BJ0KFOg4UiCo7KLzwZTbTlPcQdH5pZ5X31RooCMAc298TtADHfa6UJxDgX43GcOvcg81SQtXIhii3olHRafGCnNMQjawnRKQokKUizFj_4mz3VY75FtQ5x4NWh0FNz4vwG29LcQSaMcrHEZj93kXpT6a9pcWjUO4Dwwla39FWElE2kD07ht9cejCi58SkMroIdDQsbLlYV6MZ-y6VIZjLnMmQ4pFcVOUKbffgw2bQjuC59YlKcfqis1Rf6sxV3z8F7beKM8a6ir9FS5XKnjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=pkj68I_AqkePWocGdDYv6utgNlbMM4AfSFD4i9c2T-cMPRcab4XJUVc0KHraQUZW6BJ0KFOg4UiCo7KLzwZTbTlPcQdH5pZ5X31RooCMAc298TtADHfa6UJxDgX43GcOvcg81SQtXIhii3olHRafGCnNMQjawnRKQokKUizFj_4mz3VY75FtQ5x4NWh0FNz4vwG29LcQSaMcrHEZj93kXpT6a9pcWjUO4Dwwla39FWElE2kD07ht9cejCi58SkMroIdDQsbLlYV6MZ-y6VIZjLnMmQ4pFcVOUKbffgw2bQjuC59YlKcfqis1Rf6sxV3z8F7beKM8a6ir9FS5XKnjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=sGpN4ynIbFZRkTtzEMBvcHC9zyoQZxREaSG2h7_hq9fV4yY1bKVu4BxJWMekab6wTYIrT4hFl33VO6u-4n-BlEC05Z6IWwzyaRtLMxkd-Kbcjkj-wjaiYeCiPZv-XnJKzizWQuQEXrYg1tttcbD7_nZCx3X3SQ93HoSV6XyqvRs0oEIRsX-0TzYO-vzfbFTQdgG0OzANO_XVXbIpLVpW5ztUSjZnYXHBLxHby2vaF-q5Sl9hGNmfxHIXdPjuFqjYNsE8-MnHLDfXHpgf_fmZXuh3sHXye1WCGxB7a9o_b7Al6V9W3o89bzOkoEqhDwcMBpOzi-OMJtAbTEQPkezOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=sGpN4ynIbFZRkTtzEMBvcHC9zyoQZxREaSG2h7_hq9fV4yY1bKVu4BxJWMekab6wTYIrT4hFl33VO6u-4n-BlEC05Z6IWwzyaRtLMxkd-Kbcjkj-wjaiYeCiPZv-XnJKzizWQuQEXrYg1tttcbD7_nZCx3X3SQ93HoSV6XyqvRs0oEIRsX-0TzYO-vzfbFTQdgG0OzANO_XVXbIpLVpW5ztUSjZnYXHBLxHby2vaF-q5Sl9hGNmfxHIXdPjuFqjYNsE8-MnHLDfXHpgf_fmZXuh3sHXye1WCGxB7a9o_b7Al6V9W3o89bzOkoEqhDwcMBpOzi-OMJtAbTEQPkezOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=QbCVFI9JRaS-Txhja1-RDhxy3iPHmWWGWRJoXSZnygaHmSp2zntkTNKiIoteyIwkNNEPxi2QRBmC0prG4gVB-MolqhtKjm78q0_vrOC9eroNTh7DIC1CPFuCjSeOSwQqDweGxWLJ96qiR0wO2AlcMBhjvdKcT5fsjDMpOuCrGh3XJhKmgo5k24r3NUoeoVllTCH1aRQrg-TXiSXaeZgGXON4bmBTQdrgogdurmz3r9v1j9kQxbFnhYuNAkDZ7AVko2G4gAfvWq9xVwzM2a-lxK-74vL_Rf2-zpBTDBvCJ5qgEgCbUMY5IuFlPozAuzXZ4n9AdSIHp2mooc8OOTofjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=QbCVFI9JRaS-Txhja1-RDhxy3iPHmWWGWRJoXSZnygaHmSp2zntkTNKiIoteyIwkNNEPxi2QRBmC0prG4gVB-MolqhtKjm78q0_vrOC9eroNTh7DIC1CPFuCjSeOSwQqDweGxWLJ96qiR0wO2AlcMBhjvdKcT5fsjDMpOuCrGh3XJhKmgo5k24r3NUoeoVllTCH1aRQrg-TXiSXaeZgGXON4bmBTQdrgogdurmz3r9v1j9kQxbFnhYuNAkDZ7AVko2G4gAfvWq9xVwzM2a-lxK-74vL_Rf2-zpBTDBvCJ5qgEgCbUMY5IuFlPozAuzXZ4n9AdSIHp2mooc8OOTofjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=kuTiYy0k__U8YO91Inq1rxPMGveKlyL0CzwTOfkVGhzZxzBn62MSPFlyhSRdpYyQrtquEDOLqF75XjyanqD_Fw3Bst449QLO4_3VWapvfZ6MgajeolkXa1mhijLUnSJVDKNT-G7uvF1kYEheqdZ5W8MyJ7QmTtyNjBLEOblnkAmnWws6pvJnRxOBt_OTpkpZBnAnxpVjRMbelsziycRSFPXzLvt3lPOJU8LKWUE_ePLk4eAtS4KNJttVHSX6nF39XjZu6H79KA2MlD_FdbTixlWK-yNiK1Qmj0a74YraIuDX6cxnTyRcQkQqQfpEuMY-5ecIOId6Asz6Y2PPL74vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=kuTiYy0k__U8YO91Inq1rxPMGveKlyL0CzwTOfkVGhzZxzBn62MSPFlyhSRdpYyQrtquEDOLqF75XjyanqD_Fw3Bst449QLO4_3VWapvfZ6MgajeolkXa1mhijLUnSJVDKNT-G7uvF1kYEheqdZ5W8MyJ7QmTtyNjBLEOblnkAmnWws6pvJnRxOBt_OTpkpZBnAnxpVjRMbelsziycRSFPXzLvt3lPOJU8LKWUE_ePLk4eAtS4KNJttVHSX6nF39XjZu6H79KA2MlD_FdbTixlWK-yNiK1Qmj0a74YraIuDX6cxnTyRcQkQqQfpEuMY-5ecIOId6Asz6Y2PPL74vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=Cy_BukeKtj-GllQ0xorFAm-yvEdLgGTqLygak72hMJ1lDW7Ltvxm6RG49pPZYRJvcvIFLrXwaLrfBrXQEDiFSzTjRKuM0s4cytN95z_RgzN3wWC_ZnhLjwsnlaESMnOQAv77e_qRJ0_Up1Ueo_B5t3zQcsovWOGA58kk1Sk_7JNkcGM7WFz5S1l2g7pecWPgtsafDRoFczrPMmZ8Y5lR6Jzr1m1tkYboTGHcFErh8IapS0TNPeSlFWpz4Ph1EZqx8meTZZ5GDmZqYBSQIYNwDBGJAGWbyGo3UtLCP0Ki4vmdVz5GOGytFEIg3_9i0wmdZs8nF4jqRZFmJofE_0CQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=Cy_BukeKtj-GllQ0xorFAm-yvEdLgGTqLygak72hMJ1lDW7Ltvxm6RG49pPZYRJvcvIFLrXwaLrfBrXQEDiFSzTjRKuM0s4cytN95z_RgzN3wWC_ZnhLjwsnlaESMnOQAv77e_qRJ0_Up1Ueo_B5t3zQcsovWOGA58kk1Sk_7JNkcGM7WFz5S1l2g7pecWPgtsafDRoFczrPMmZ8Y5lR6Jzr1m1tkYboTGHcFErh8IapS0TNPeSlFWpz4Ph1EZqx8meTZZ5GDmZqYBSQIYNwDBGJAGWbyGo3UtLCP0Ki4vmdVz5GOGytFEIg3_9i0wmdZs8nF4jqRZFmJofE_0CQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yhxn0Rm82LjinjwaccLgKQBQ8pAn6odr_NRmRWIeqQCXtXl49lDgfp4Pquq6M_SVfbVGmoh3zyfQfFmkjEYV4oryn1FthSs8SC4jTVwPksBBYj5Llz-jsd_Pu6_xbn4MRBnz837xKOKHg2s2qO-7PSqJLdp9xJetLfRRikTUXsrgQae3Oc7SwYBCnSSl0kED-2GgXoF5ALdUHSzvlI_nocSNnGYYs0lTIL-MCYmDtFuBad-fnZJDCSx_yJ3DJnbXE9c5z_vUmYEjPSj9hpMESsVSBlSE4t4krhkQzOkXxvSIIJhCmGKIbGh5dhoebu0_eHo9HDIMJpoLW0LlR5cKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIZa6wI7jGgErNlVWvzit_XeTM0GqFOfgWvGCKm8VLWLI6XhLWUIFzl0bNh9nDxAAFYOKGJwk4PlgWLml-pa-42738Kn_uKIip8wcma6xc2btOb70boY8bkuncpfpxJ_nA5cA6choQdG8atnByuwLCJxt4FlVzBU9U-xL1deR8Iuiy61i5hM3NQtVPZMmme3UX8Z_oKVCw8irhCfBBjJ0X6W6rqld_QQGUWfGq6g0b-V7j8mxbi1yGINMholVa3byF42WR6Fcjb1Xdf_vzRkzBV_dsKhlo6429R3wu_BnE5mG-LrysrOnNDBWJlxUA8WiK-Ra9y9EhIqdt3PwHO6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE9chNGkKvMGYRmIl-rKyxBPCTLQrjbZJBSPP0P8WGDhXmFb_EvZPt5vzL7tXysnSMtkjRkRmVApIJNIbH6_hhSaVBCDezgqz9DHdKxrhoxW7ptIxKkUM_RIxsv3l8xbG7amEynqBt46NraBp2QCQplnwyjida73K0VOZ9YO83PacH3KY4VJhnqN6UhLge7CHVRhuVBA4XZlJJj-U6WFZWL3K0qasRA0D9vKx5mEfJMa6PYXgsjfZEVgyF3Sdr6YxdisWiuOvf3rjO36HIQrpR4xMxCyqOWTzYCIAfW3rxuq86Zh49GS8AJ_xJzm2aqAz9uvAvBz4mXAaeEx6OdoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjaeQwY8z7OXJVB8SvQRIUs7bEQQv2pVzLx0K-oV71AohelnZHQwQj_ieGDP0_FAYUHPPYNVZmIDy1gZviPDEXcR5cVoqV-Ia969J6PnmEh_RAsvwFATvJu48lPaOelEuW6Q3_NQM9X2fEuXptL3M0GO_IF6zJg2sZ78Dq0Vrc7_T1cEcU3Nb0ZBPTHDzdNbHplbIULgFOaACNC4Zm5DQW8mQDDY3PJcOKhM0wR3nf5RjolrK3lSdKXObJTEoljBYIELfjjI58dRqvRZjhrDC-0HOVBZV-uKK5ek_VHTkKVGDwIwkYec4DGE-9qzcPjdDsmmhxZPiB161aOxdiE3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmWGtOP3rC3IW-NXlsfuOU-fkz0sCmWk3UWP3_sqk06QOSsjvrlNVjLxUvWnDLwNFOUvsos9An7FddYUax274-8GX68e_IStZkfu7fGQ-0Fo5VjadU193HG0OZ8ndR3lFveB5rtNKg6CfEXn1meJccwEVIwwJsoegwCRZ8KxxUgkNle7x0c3S6PKvainTJmCa89A-ic7aYfSoGhRssszaBvotWTW3f0tizjr7HBH3fVcudcE5U1QHNUtN5RSXia4kRIlcVXE76JfhyQ1gh_T-JaMJIt533RBVjPfEwnAQeV-apoP5SnWFbQ7r5RGTc2JscOfsqOefJRw8hXr66VvMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CZkGo_IYoNO3NZWAckn3wMS-aMXAmNQudVWW4m5yNvcwIabn_Cxc3mG3Thm5ef4CMcoE1Q0mTAETkZMShrXKFRc-JQSvl4ppf4sJsNV8oEfq87TCw_R0ZNkM4IytBCSGBUpyaVAsnc689pmAwHDMEya3k4wwVtageVscgTf_mya9QNF9eyR6YtXLrbeIQ2Z-nAOQ0ROeJwPIitwtBqRjGL0GnqnCk2jhDGFEfEkj6SeVDuEknVY2gSy1zOMRnbX4lxIyGPhLnSJ_x5GRn23n00FNsj63H-K2dNN6ldpClUyrdN4tausFFFHKGRvamspYzUY6PNw2S8ElpNbURDqvkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HaFUDiHsOJUlqt5vdj-kNuwM4mygxi6CwQTXFdCzP3rvpTljmWejs-q2ZmSUiThNqYzrYX3lKUtIKm7SsRUaJ_4YVmMTPksDogW93cy6CoJkYno0mIntHoq9p3wv6K9czmej9uxKbLWfxNejllfgoxYFZgC3NS44JggX3DhhQSMZj7LYd7GGcCkD71ucBT0TRYW55Tbmei0oT6jEc6ZXz_fm7DvcEk45gixafkOoxJdC35MNT8GDcZT6N4uUFezxcsZj3Ajt5TIs6Szp9D7q_naGK-_C_za8JmHpz4FA5AVj_MAC68WT-iCvTJiBmst71SLnuhAhIBBJDKRwYwvrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iFq_R7lm5Gzv3FeJV42ju-pYkraK1PHIGb2QCDLgBs7yHMNc4gcC66A5quFhWzwDIb3BaolPri4MC8KQgVLU-wFpkCK2SjcLwabb431W4hZ9m_pNh_hTtjogHkt-VRjQ0kGa1HQKQfWHr5YtZNfpE_eAZm0-_klArL8DvAMTflbFp7OKEmaFE7aI20dJRVrvUpjw3x_CTHI2snygilHZ-pUq_4wisORarVuQ6kMDNkAY5j5qhHvBvohHBGfZqI0I50W5DWSPTztfC1494CvVgCIAXXUQnjOqEt6HjRB3kifPL1eiJDSEdDV73ScG9n7TgUanX9GA3dloE6-5Lm-hIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PQX1RPFD8dAcmUMDsJzK6dmQLiA725eRJ0laIBUKUCaRwoGHcFZtzGav64afuVHL1oGzszAOoE2SrL93iphckJweCasydmSGhNAHy5gG2ni4dJeIUuWFpHWzTMPJ3XWhH9yeST1a4pDqXfp9yv3oRKuw4SsK-CEZGAdmEOJdocAHMzzmRus4bqoIU_IPBMPVFcoXZ1wpirivr5emioJNTOypc5al6fQ13u0C9XgJu3IXEZfdv3VnhcGiWOVat2mKlueFU6GKqTI5EVzfZZs4tAtVe0IVFlmYVCod6wZ5jCZkPf82-k5zbL44PxqDdz7sEFSaVQ4ApGkXUr6mzmA4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Acpvpw9xhMHak4aTP5C6iPNYxMRl73QbTfBPGqYXxa26wes4zjs8NgkWysbCag3pjuxUobaZVHOoy7jxrMdxDKwWTkQuycJxwauiC8gMMq_wamkjgr6cJPH9Z_TkWmdUejVVMWRNSjR38uOizKUeyMmFsjDQ9A0gG2o3nEY4HCBXP17HoJ4NrYpGUDCk0Xn6Lx3CLSKRJGHiM6ERFacNuu_pq0P6IIwg7HlLgURUxmVvvnt_eMKkuSIBc7KA_mSH-hia0mFJ_zUQ-I6Z0osiVO6IdpUC_J0Co2T02IB3G4kes2tksTcbDjuc8T6N_g8-1Cer4-wLpiZciAoNNadbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oBMTydNMlbwy5NA59iB8gmaADL6PREInjH1efY-KE9IN0RFl8p8fYUuFrSPVjzIgzzBlWu9ulBPYox7onqbY_oU_jb2OgCSH-4t4qMWqupWTped6UEmwqqj9tquS2x5k_q3sECgA-tFjbN0WLC9WFqzLlzha52q1vCC0Z5SylQksTcVuqtntqM0FeGQzxEdIiVx0BOWPG6knSS89lyZWUHWcSbUqFQVdxemIjVRZVhN2LEcJc96gG6zRxwqjs5XqgSgvBYzdudaw82dDwr5fcAce09Hp9ATV0HFcydHIxE9rzR4chmjMvwMzrQB_7OpyIsH7Bvm_FgSyzLSDNU6unQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DGSDTB_j14Z9ba53r9SampF2OtOe5WJYc10ytKZJgRe6RrS9NfXdL-UXnzBq5kPyW7l9ZxnLLNyRWE1qqVZasJ31OnojBaktZ05DBRsiiB4aG9D1PySfaShWGH0lqFi-dbYZRyi2qsiaDtynZV27EnnhGPhTSquixp-FI1OkHOIrvK8pHWTdCnukAw8X1IW_z2kz2U9qSSuszDmdGlrCJEhcUHOeZBs1vNmsWJc-7mJycCdQfyF9-tfTOqOg3z5aofa2yT-P5H9S2Vl28ERZE0BzeiCC2c9krdSest2ggjYtII4q_Uomy_8P4beoJWCPV7R5YKPXjMyl7V2EKL1V7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEGIM2qTyitjsZgsPezyjsLtw2XxcEsVyeV3BNTO4j-6ZHK6t8k-Xd1vz0OqrXtIO56-qsvbM76G5ZFapTHKZ5ngVqwiyJP6jHEmpI4zoEbJmNzHofLPe0CrNPa9kR4sbfjbyB_xKN55vo9fvmF4IO4Y63qU_jz3mA4wEC-R26SaFq4tv25R_RyUojjggRxUvIRQ-ux-Z-os4wrUUaFAGe0FRgM3i-bmqauajHG8bkwA7tZCxsxSbnqUbtP0N7_03SEN6Ng8VQxTR6xYZ5Zaes-P72GLrJbJxaDpWs-igyQ3jFiieEHhwuSIpQqL6EBDV_P5tegj4WMuR7gfNxbDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EACjM9vQWv4Qp8IBWFibz36m68w9BBNyB55c0mx60BO9p51W9c4DJGNhPWlJAja-qs5R2j8QZT0ZPbl6uZ4LkiUvU_ABsDBPr5TPzNmHChM4n4qbssvWQ5p4bIqttSqZi05FFZ3iOPnUC9K57TaQxNFxG2OnUBzIY6j-JnKWqzHcJaL1uWx2krgWOEKMFRYQkPsLbjh6_gQVIb8ewPAguu5ndXIdMavhgufKS0W3flPLLv-xKB7_aA48M9TIoUtE4X_jI29nlUfC9TImCb6Wigpm6QUA_Lx5e31UQOhTSNAOpj7spLhWnHV_B91cvdib0ydh8xNmJlTshalMgbs2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJNON6OlKnF97tI4tYJnZyycValntjEhlTl5hGTX1saNKdVblWmGqfe8pjk3pQoR0F8NW6PR4uAmhLuuBTj-a3_LulYpFGLJWgsi250P6UEb_L5rxw8qWC7ixRsHgn1-5egnqTk0LM35FWK6pVSOOrT3SOI4Hss7Hc7NPA66YlvEXJgT_4X7nzIeX4QjfM11oPStAoB-h0Od_gHBfP3JstQCMXnMovN9YZrlaB0ZhVQNWG1m9ch6juClNWdZZKc_zulAOD8pVQE5nSA-IEr906ndVN8eAqsqcdvN1jkW5Ich4WabJTvlxeGHhjq3a99koaZLsKkWDpqvIiJjMUqMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=jsk2ei1A7f7awtAhGMsPCn1LpHsyTq988BtbqEmP6-LwtUq5q_OEdtQZj9r09APcVsrtLa2ecENePv_0Oa2NNmL3cqAu574IuLEAuISuZpTjM8iaAssNp6ivTEjSHoRa-LpZ5Lo7RcY1MqeH-NlmZ7-BFzLj9jWrVc2CDbmqpFVGhcWSf3ajaopCzJmduI4gc1m8XnPLx7bQ-Bot81m4YBgHmVslOrhEJK3uV60QgAwhkwbr-7AJkMISIxWMVga6wFh6ar4G18dpL7L5Ltb0UJtG8ZdiVe5f6y116n7hNniYTl16NM0-uoV9Q5PAA1K205eAOUAqsQ5br8mTppjV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=jsk2ei1A7f7awtAhGMsPCn1LpHsyTq988BtbqEmP6-LwtUq5q_OEdtQZj9r09APcVsrtLa2ecENePv_0Oa2NNmL3cqAu574IuLEAuISuZpTjM8iaAssNp6ivTEjSHoRa-LpZ5Lo7RcY1MqeH-NlmZ7-BFzLj9jWrVc2CDbmqpFVGhcWSf3ajaopCzJmduI4gc1m8XnPLx7bQ-Bot81m4YBgHmVslOrhEJK3uV60QgAwhkwbr-7AJkMISIxWMVga6wFh6ar4G18dpL7L5Ltb0UJtG8ZdiVe5f6y116n7hNniYTl16NM0-uoV9Q5PAA1K205eAOUAqsQ5br8mTppjV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=F6ewIRV_SuCA39RjaZjU2uMuOEth924FPt63t8lIYqf9ARPXBxB4feK9T2aDmv0Twr1Q16mAIXB9T1ysnoucfX5Z1_4_S-KZN2wN2xmHA3ZsRvxD5v4k4D7AmRBKfs4Yl2JereAsg7tDkUJTSRhlhAU1nBlC0LKSqBu-aAhTcEkEl0JvBTBk4ltnDnbS9HBWHcYzRS2zR6nItW1-Ddip1gs4Jj6mcDVUNDsOFUKr8pr0q5i2rlslXOanr-tUoDNEE-1H_O-HtzXD3f3sWGk9XbdFPXzb8k5q5V4sZrEgUtqQNDyJzMVS0OAB_n03FX6PjleRTC09jscaym2J1K-Ipw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=F6ewIRV_SuCA39RjaZjU2uMuOEth924FPt63t8lIYqf9ARPXBxB4feK9T2aDmv0Twr1Q16mAIXB9T1ysnoucfX5Z1_4_S-KZN2wN2xmHA3ZsRvxD5v4k4D7AmRBKfs4Yl2JereAsg7tDkUJTSRhlhAU1nBlC0LKSqBu-aAhTcEkEl0JvBTBk4ltnDnbS9HBWHcYzRS2zR6nItW1-Ddip1gs4Jj6mcDVUNDsOFUKr8pr0q5i2rlslXOanr-tUoDNEE-1H_O-HtzXD3f3sWGk9XbdFPXzb8k5q5V4sZrEgUtqQNDyJzMVS0OAB_n03FX6PjleRTC09jscaym2J1K-Ipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GWXJ46Y091gUV7coP0EEz5tfp72MTG-Syc50pPHHojrSf5g3Lko62eKFnJNStbhv-2l72ubIe4Vxh0rJIX90LRozHM5FFnZPFOulMlqWP0VOs9s8L5-aN-Zq0VpHUDFgjTl7Z3c3gb9wOkRhfbsxCT4xUyeREmxxutEEmboW7X5oJNF6-EgP_qPeLfSqVp3RIn3L7zaAswnjelmCUiYyD54i2deFfTnby_zXScAEvtR_ARikwMzJWNvLTf5WNGBZx_QogaP-xpTh1E2_B3RMD9Q9BPsgIlxtMkGsTvCUalrfzyziqXrRpU3z3jhTtk6c_aDZoBNmRVGS4Auiz_Y2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtRR3k3tSYHr2K6O5oZ8r-HAKNdsFRIUQiXUwmiaqJQVftUn_FL2vN5nQBR5WA94ZTiKsV_Prk5b_xhONVpNzVwpVSMhPbO4tpZMsgbmWCRdcpb1IxUgDokkE55Xcp8nM504u5uk4O908FACmJIcmnzrFycxv1aD0ez1jDOTRDZnAeIqeu0akPBaiF_rYahq9TiqObYFjkd6XndrA0eVwBfRfefQ4Rx0jffKZE6lQYyVuJjy5sz-9waEUEseDDlJo9F7DdoRVVXNL7C7HXCGhFDd7zGSZRIZn66OZmTp5LyO7LsuE88aVBxlP63BHxUpuNSava4Ou1DghzLdWrlQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bps8L33wRLmtb0qNzzTdJwGLWBuMpEAQF5p6C-pxHyp9NGA0EAe9ElfkayO04eSNPMofDzP2vVCxsjEkJDltwnGGwf1QpwMqyWwxUdoX2X574UZp8-yHLqtp8Cnsn-a8t3h4U9Io6vTwl7PEPhYGJQkI4yBkKvghaJUioxfBH4I2SifLf2lwIBk7eURkSDJCXydpnawHWoYxQBZ3ghkDFJFRYYnlhAOSjhECjFO07aQtagBxXcOlwRt0oviZQ-nNWKflZmvVyx1-VvYgl02c7frfKxuvVLy_VRd-zZJ5ZBz-6DnI17ijnQPOz-Qw5R-9rXuGjYCXK90QJVQfmdPtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=JyoU3hKzD7ukxkNrAGYIOtqpWZpz9SnCBjIX7aWpKGjH9TvIdOVrFqKE1H79ATY4tvuXfFpjI0JnjnBRM10ZEFlcRNdqTl1Zzajm2AXesZxRvaOUuUt9uwfsJm8Z58XUHcTmuQDS2oN5XyL0IrNcuokHgOBWl0p3msPYx3OkwleSJH0gYNsf24XjBcGmy5cXzwX6c_OXmevHoqjPp7tSyj0j2qGtby6ZPSZoljaK-cXuM6gDT7CviOr5PQrwpFKRB5Seuy58gbe82DkSr9_YLU9xukZAIqnCemA2NdSwesA5fCCEmgNCgw9Hoo9LnKwVygG5oQPqYNkisT48DEd6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=JyoU3hKzD7ukxkNrAGYIOtqpWZpz9SnCBjIX7aWpKGjH9TvIdOVrFqKE1H79ATY4tvuXfFpjI0JnjnBRM10ZEFlcRNdqTl1Zzajm2AXesZxRvaOUuUt9uwfsJm8Z58XUHcTmuQDS2oN5XyL0IrNcuokHgOBWl0p3msPYx3OkwleSJH0gYNsf24XjBcGmy5cXzwX6c_OXmevHoqjPp7tSyj0j2qGtby6ZPSZoljaK-cXuM6gDT7CviOr5PQrwpFKRB5Seuy58gbe82DkSr9_YLU9xukZAIqnCemA2NdSwesA5fCCEmgNCgw9Hoo9LnKwVygG5oQPqYNkisT48DEd6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtiZ9Qllj1ObvP4wTjvuC_w9G_vt7kkkgzyCqjJ3ghWyGzLIrJRU3PwI94B1sH7Ffgrou-qbLxfLPjQQqRz9a-UBC0Oewo8gTmuMVhu-fX-uXNaKH3KARYMLiBhA1pgZWlBTjlT9oF2I87UYMVslNXDdJJl9BLVRVNWlHCASM1fXqHp9V8Nx0K109sZMLNA4N-g7lUIeifHraSpROA-dmQG6bH2LpUJodedBDCVwvpquev5j9WKzKi5ZuMwWXyZfSbkm0OzhH_HWZjo-TFQ_9tvqA9NulJGFN0aAfSMWrP0RRtS1jEnwzCpTNWmucs7CoDCbnZKC8oWNN-Ng95zqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMxHoJX6jStB77dhGpXGmo4GGN7aRwMkbQoIIC39Sw_XcWZjpRQ8yzlBU_NoyrNLUBg-xUTn2etEkScpXj1kps0uYYzdxmbB_1yK21LlVZbQo-kaRecoX1JzqZGlIyzDsOB5llLTBmbuxU672iQIRnqrYjH44uowrSc5JoxyoLKAhyV8vDPz2r4bfeR1gJG_5_uc7plGv4_dqicjfQGdZPag7FqJhswXmejTG3kL2-2nndM2UtKVaq2MqkPYazfS7oUU5ApyJQQFmkmhSncAh8UW1QCXMADfvdBUQ0wLwi8Y6qMvRBxZ1j-YBi4H_gIFEpFhB7Ovq1V3qBkp5fkYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHQhAVxLVqxxK1HmqzREIsDKnJRNZOXlxbF_zbyGGYG5McNi1XKm-TDcvYjBNBTbSFFy7rSlu4QMdb4voLTi2g9RcfiTINFFNDt62-bp7bj1uv5-OCoIT2hkRd8tmJg0RLIIDoFSkalmUXhA9iNxL18kmzfXSAuAnnT-caOienyHjp49eLuPEJ9TGuJqvMK5bkd0GnpEKgiFCTwFWfjawZxMgr4ai3Q2Guk-PcQAu5QqwoO7FiCG3JsX5NXHHlt9gInVy_CMWECRG1DzZUHrzcXeOpQZoLPsAgjcwz05KNXbu9AZvTDH26CuPuFbpHDYRymntdjw0I9hUlz_tfN1xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtquXnzqoNaY2gnZPDmqLCvwudAiVYUplNttwgC3AUldghUdAnrjRtugCdd8cNgooW47kdyLUwbqAlPPxeM0jv44sVgYcBbc5i-PQvu3579mb7V8mN0XlYcbS8J4uQMqE6cevuHd7VDlBUI0GUHhCqYVk6FC2ikR9ZT0rqsBsL0JFRExjI5GHVARxm5oKKaIp0LgWS-0hhhSYqkdAwObiOlTFGd1NsMKOSHZjatJleOV28UeGmeY-zhoSsch4qCe4-vt1-VYf3pAEPH1aSzGgidwfZa8uJMGG12qZ9GzrfA6lNi30jvfxZyoVSidFF2yj6cu8FNFupldeAWTrtJJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=bijLj0yeKWUthKIeaFtJAgjC1D4G6bgqokiqTBhLIkWo-6n6AVvF-0mXOhjwNjkk7xYyTBnctLSBXfiy7qZGRC0qXMfZVcIbl6vOfNHLPBp_nv02qzTXv4ax1-PAGbL76HA6z8U1xyIPhXBHYSHdONtMrzpwfqikgF0CJ7O658ewscihiYKGrkR9ilClTXCYkJn4VHEXdC8lEkMqNQwjZAo1FXZiA6saYnL8eypXQcBvAn9SxOB7UJ5ouDkMRE9ctUXEuQrwBmWans1tTlKtmqtB3KQdiPh43sWjusGWSBbnln9Sbpbliq2TS-GBRVtqyo8IN4NJTlZ8_I1-zH3f2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=bijLj0yeKWUthKIeaFtJAgjC1D4G6bgqokiqTBhLIkWo-6n6AVvF-0mXOhjwNjkk7xYyTBnctLSBXfiy7qZGRC0qXMfZVcIbl6vOfNHLPBp_nv02qzTXv4ax1-PAGbL76HA6z8U1xyIPhXBHYSHdONtMrzpwfqikgF0CJ7O658ewscihiYKGrkR9ilClTXCYkJn4VHEXdC8lEkMqNQwjZAo1FXZiA6saYnL8eypXQcBvAn9SxOB7UJ5ouDkMRE9ctUXEuQrwBmWans1tTlKtmqtB3KQdiPh43sWjusGWSBbnln9Sbpbliq2TS-GBRVtqyo8IN4NJTlZ8_I1-zH3f2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0U4ByaKmhYBIVcMcGP2bnNNnEdi_fscl85kwOmuLzF9cNfGsNXWt8fHatI5BMmmV_b66MfmyqTZQ6xS_iuGIDF60pQw2YtmdD_6NI3mdOSgPsq6tq4IiCm8SdoyicRd5mHOv1XfuFtNRhvkJyerBfqCmxzYrnqdYvORZWHVW48kLZuX6EqVYgPmDUBTthejy3U6URcHlU0AzFloJQYszdw0yx9d7WJvPARgLt9ZHGvYyD_SVcIJQPBUrDu6cgdapkba_0o95fHpuLLhnB_URhQof_19qsTCpMFCB2WbpMXL5EbM9hKtonasJGTABivSnUztpoTojxnwgpq9USgeAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKObByphyn57PyB5mDcL3wRJ-Jdq9RgO9uM-pugYLRvLVflud4A0eoHPANSjCKPCaanQuCW9StQkoIkxNxyBF64_xjnWgsBsrOl57sofZCBPa_Ta8BeHfCyAQScMR12Rtpfa-R0yDGBV6VxwtwTAbtSeiweLbvtIiHu4U1jvdty2EVvVK7AhPgpUlxlnyNHtnqvT8fbnpkeRKWm_Pu7_Sd_iiqJZVg2ayc00tWbBSPwnj3BZt4ekZ9nuRLtIZb3mGrYPx3wQIn7Pbk-NZYKHOZc3CAK0hMUL_2wYnQZe1u6MqNi3J2-wzkq-FVgFP9uajVojRZRR2SooZPt4bpyM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCsnUcYAm_oVh6wiQShZdFrPCFpFqmqtnR03dVpBoprCoDODuXsvdPszhH5sLSUGWgolZuqVjaOKizlS58q6pqF2yg6mqDVuPgw2O95VvZA8ZKDO7g9G-q21pEYPoreiEP4G-hZTTE1ecZFpzRhrIOYbJ7I1q_oBhIgxVATxPwAq5n2KHsSRVd0g_Pu2gB3N61sYw7YND9xzefWPoJX4LNQJWCHJmbHCedq3vG1MPS1wvj3uy3XJVnTTqyD9eFEqGS7fKF0kt1e0TwpmCyFENsHzfZUeQrMNzmbk509rMJg-deiwrR9VZ4tgg3KI5C8fW8nCvwAdOwqn7wOIffaLvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvHNzhC4PMKXjViJNboRsRsA5D8x7wAWChQZwqY__YnJudIg5TX6LKLWChFaImJFB2vkM-afkOEeqxkD-n3C5VGr5QxBwmaBV3GRvs0-My16n2nNy22x7yJ2ssA6utQ5YrXUIO1GE3vlI_79OSAth1SZWmafSyRGC0HNTVYcKgPUwpDhLgk_6dF0lVuwrL388s8piIi9VTevaXci6ctDEqJDXYEWwvtWOwW0NA2DMT1YLq9tS_qcDOoewfp3PDEe_tiJuPGbPC9_j6PSC6dvQxYO3OctZCoTXgUVsUND6GKu2UsO26S88I9sz8fB97dav-qH8dt24tfMuzURWF4jaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyRWerA4dBBezXWigJa71HmCiRyPLC3arnT792BysoN_tGr8S0U9mb87RUMQWldz1hlkb7SxdhyskdcCbXZjgMjcXuOZzHzg1m8npeb5lbIr985Hw167gspWG5mOdiSUbapIsk4TA_8gJ5Ydy-GJAIhg63WNSEfOe3L5hXygOL3eZGa8v8Sohlq904FZ88DmqNcD0gR8i5u7XQMG6UduvKneDtLUcDPeO1rJN9hIcWJR86obKTk5NWrTuAye2s8r3Wthe9ImJ6ie1Fur30YqhyLW10V0h3YX9yBebIqJso1v7e4F_fM4wSy-zWRzSAY5dSXitsko8fIbxUkliP9F1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=rBRuvoua5EnJRISQdvw1pEzDsrgQIUwx1rHjYNbqr-VS7pra3HkLPz_ZqcMrV49d60qlfosJOt3R-YGztQR8wkIqlj0PqNBim9DiKo2Bprj4NW4Bv5h4SH8sfT2I0iTdQnbroYwrhC3A_ftUzYgZR3GDUdAJvuBOC8F8zIEoKVZuVln7PnbqhTjbVtgiwKVOxl_YRnEG_V_DBbOX0gp-CUYv9qsE45hPzjs06J7ZOwl44f32RqtqI-Z0NLVsPbH6_xsd3LitY_d_5KYsqP25U5yD-swIQLJU44gIrg_XyZFY_al0fv3ikmlSWs2GWR0zdVQoOdL9Hf_uNMI6zMSJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=rBRuvoua5EnJRISQdvw1pEzDsrgQIUwx1rHjYNbqr-VS7pra3HkLPz_ZqcMrV49d60qlfosJOt3R-YGztQR8wkIqlj0PqNBim9DiKo2Bprj4NW4Bv5h4SH8sfT2I0iTdQnbroYwrhC3A_ftUzYgZR3GDUdAJvuBOC8F8zIEoKVZuVln7PnbqhTjbVtgiwKVOxl_YRnEG_V_DBbOX0gp-CUYv9qsE45hPzjs06J7ZOwl44f32RqtqI-Z0NLVsPbH6_xsd3LitY_d_5KYsqP25U5yD-swIQLJU44gIrg_XyZFY_al0fv3ikmlSWs2GWR0zdVQoOdL9Hf_uNMI6zMSJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cTsdrNKDr9ThjVQpzcXJ3_ULkg7hlGmPl0oQXi7zabYUByPIaVUJmVvOdAFdbghJLwKpEe8tIkVvqPRs_pNU2U7KEAnj-5w9RlWoNxBxSiMVHD8IeIUgLE7jS8zoGy56GJyZm4ENFMyAzBjECrsC-OjvxY5mq2MKnFlC0t2rZsqdzTDsqqXzZIQ6CHbhoj2dR5NHJ4QIDI75Pm35KprnO5-2UBxGSKgC5IPyS1t2IQMc_nJAW9pIQkjgIsZVWgrI_4OcCZ6UYzlnNhHutncyo8tksL1PVNhg8vvaTtURU2LtC3ZtTv8SW9pE3ygp4wjfzrRGx6fGb8w6vV4wVLsSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOmobuchavuH9W1PD7NvVPbZJvp7B0v2eWMu6jyMdf9MNtWlBg45l0Oubbp_hXcfHT2WliJ8h8U8TrYukJ3_ym9HFCmRRMmTaK7H0lhu6MBPkScvdis9j-oEuz1m2ceJqStIeYIbAST3nG4BWsUMtPdEKVilWjESerbRc3Nzwkm7gxRAVDnYyVTPangarsn2TXX-Yl8Xa_JgTRmPc5rlO0waGCC9hD9KmXk3uWrDDj-krdRkFpLyJ_nv3dKV39kgZ5ap_EbnAmya1TMgf0W4pZnSV0Q1t6gIr20ZFkeofCj03vMd-FIpxwyf32p6J4LBz07Q8_F5wwtCW_4pQbcgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=LitDdMZbvZBy-GtjL3gyb9DUC2snegb0nMhbV4P4uxDiWUzb9wVRkJ3NaYG9MOA41Y6ga9wVzDKxC9sU3McnqDREcJYHpFmZrgpAkpVK_onpQ8gd9teCseNhP6kCsb23P9SzFkNuKxRdRbA807u5hLB_lJrB84_eTi4tnUdyPT1N9hpxqbclRnxVujag9y4mhQTnhZgjGvz5DiZ2lHRuOltEmRdKyk19RqSJqRuHDvS41E5nE9zQy4QaKGAHI4ShaXefw8ehoQU503CMpqypGRmKxXSJ8WvhQuSrmiPJHm0E3BWKxalpJInhmyZ46V8SrH80QSGbMvQ_8v3ba4Emaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=LitDdMZbvZBy-GtjL3gyb9DUC2snegb0nMhbV4P4uxDiWUzb9wVRkJ3NaYG9MOA41Y6ga9wVzDKxC9sU3McnqDREcJYHpFmZrgpAkpVK_onpQ8gd9teCseNhP6kCsb23P9SzFkNuKxRdRbA807u5hLB_lJrB84_eTi4tnUdyPT1N9hpxqbclRnxVujag9y4mhQTnhZgjGvz5DiZ2lHRuOltEmRdKyk19RqSJqRuHDvS41E5nE9zQy4QaKGAHI4ShaXefw8ehoQU503CMpqypGRmKxXSJ8WvhQuSrmiPJHm0E3BWKxalpJInhmyZ46V8SrH80QSGbMvQ_8v3ba4Emaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiIiLn7NgWzMInhhrkCssCfuGsyYXd5d4c4aheUxuJFz6Ju7ShksEJWgzBtQ8uvEF0mXQzQATk0qRQOn5I7KCZakedzMxHq2zkmfqDOHhtvQECkUhYQq8_xzOLx9UFHJzK7H-z-D_tNnqQRX-hS9RH3dptA6WdFvTqmywkgo8kZ7dJxDx-3hWnM6kU1OyyaZ7RwrkYTdPsiWHaAGQUY1IDgnMUoy0uD5ebq8y7wwmIxTXvEt_SuotZ3D_aNzhqaB-eNVtFuwJCY3mX54W5x8E4ysuKwLN4YGXSMP5h7ZA3d4tD3KpSs9oXGfd7Wttvi5y3kRiXVGfUct3v9e4KSEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTuPGtb47iC7QJM7awj9QfIFNAurmTovL1XNJVKetqN0hCrsZ3Zz1kqQisDWZ6w7EuwKelT2_DMMoyqmEdqWmUs1RX0rRmkM1dcXki0WP3ChfEjeIX09TR0P9VpQrsRwfGtiQ1Fnqt_a3ucN-rMHo98FNXSl3KzUtIfGwNnteoT0AtyCclzony_UEdJACMf63AbcvvxNSU9UFbYuwSgCuKxu1RYyTv3pliu-L9KfCt2-eAaTSh6LEjWx7nYJcnwBv-1WeqUhfkNO4DoABuM6lkGA4nEBnn9SR_JINSZKPxN8sGQFvuW8n3HWGwqEv39Sk0u5kp_hgfMRth8aDAdEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyE_ifu7nRq7nrCv7fQQLWOlmAz26pGzm_p0jIKJFfU7BMBT6Erd3lKOT70JwAeQRrFLJW_FXLKcHjTw6MHaoQzhhmqqyTk4PMniC5wcGQ93VI2eeG78k0Js1ZV5hjQtsfWYSXviQ_AHDvYHKvm2ZNYIG6k7LX5kA5kTRWblE1I-x1pHLah1NFlptO1cWvANIVCkg5VMVm-41JObZ1L0jjk5vsTGqXoF33lrpVp17Jq7czlsVp05yxuITvdQtes436Kf1_bB4QVv2YuKpsyCboMOK3qaKHz2H43Hu4epWZI2Me4RZA-Hqww0aFOoAOKHYoN0BfPbnsQmv_B_aQgH-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=PMF05Zx931Hj27ZrZ9SCvd_dba_z8syc7bTuTCbHkGWCXRddgRy1sfVbOeCT5gxrduW5Po1xMZ6vCpOXkNVnbRFt0U3v40nO_Lrxc_4dsHWauZ9p78Mj_sKtRi2zdx8baWA5SiU_G1vKEvnSwWuu5rKIWyGWiSWgwxb9Kthy5LKPm8Fc1guectagDfWG2i2HJvYW3Aqp7RGIGX-AMBBiZ7CNbDL__QDGqpoSfhCNAfGNuUL4dh4lZxd8qcLeLzRNit4Vp-06HRss06mnpCU3RI3AIQpRDIVSIIF8ES1M6L51WKflTUgLb-QMIUtE6myc7qk4JGfdAEZ7VJDKP6FRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=PMF05Zx931Hj27ZrZ9SCvd_dba_z8syc7bTuTCbHkGWCXRddgRy1sfVbOeCT5gxrduW5Po1xMZ6vCpOXkNVnbRFt0U3v40nO_Lrxc_4dsHWauZ9p78Mj_sKtRi2zdx8baWA5SiU_G1vKEvnSwWuu5rKIWyGWiSWgwxb9Kthy5LKPm8Fc1guectagDfWG2i2HJvYW3Aqp7RGIGX-AMBBiZ7CNbDL__QDGqpoSfhCNAfGNuUL4dh4lZxd8qcLeLzRNit4Vp-06HRss06mnpCU3RI3AIQpRDIVSIIF8ES1M6L51WKflTUgLb-QMIUtE6myc7qk4JGfdAEZ7VJDKP6FRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/usyrqBf-JAbXxdFvzk49bGWEfy9bTVhJnHQQTUz3Tor1qQLiOkqxy7Qvw21gJQy2V0cFh9obUxU39WJRPy9095_E6r5A4CvbMo0-on3-qXUic9mBwpDXFMvIFuWuNlqYcD2cQnWWpUvBYchL43EymLvazBCeSKofMzqhTC0TuIDl1gId5nSUHvG0tppcW5-QekZSST25N3A_Iy4ROUkoT_vK-_MByz2PniBv7jiEFY_a55_U-Fv40Uh1HUoOOxFIggPXj6zm5QOPniDjxa38Ib90FzemG5hwW-dKHDSjN33SEsaC5AZJhbjfGyPk0x0tpFCsUmm2oJK9h_gTDgsSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qArl1cyqzXeaVBfevl_95dSGIpXhKdXVdnPrf-XyqGFruLBkowGcuLJ2k78D9WBet05eg1UlYslr8VuM1yC9MmdkDAcyQsGfE4Z43ngLDYwYUPCb7aNEUi9KhcMGHi4X9M9QnCeRyzoSh18miOU6ULk5BU8J1P3VoWPkEcilQYFxbrHlGiwblkMv3GRzwdhQzey9nRG5gbuKJPnypG6K3haJIkUikLQB_0AtgyU4q7gXxZU373a7T4at4l4QA6FnwlvAFMIwtysk_SJG3j5ZCqc30UpUOMBKSHBTtz1EpVKcQ-r-yfOPgtZeUZnBYkKuXu39ta4FJqtJcHNCabT6kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIjyZ2pjbRhuiB4E1SYpLXEj4Mf2wxihu4T9zXgzfYRoOC52MmhylAxm22HIe3pQiD9bA5M0XwGVrQHnHhFmTSqla1xbp6KHhyY-U_Ey4wfUvMzvsf_9jgxxKNvBC7yepgH0875cmmpMBnT--SkOdZQbe5tjhiQj_ZcdKHsH0Y5jN6McloOwZs6CgqAdnZAbSbw54QGCbwfNxdWFrciEq1JVOlcq71LLLNd4qLgrpdLPnPFOIgz7XHUs6aPtXt0v1AzAN4XBVS7JpEXD_Tx9bllQZfWz9OBSnBCqkc1B4vZ4R2Va6gU5ug_8a5tQDUMxmoHTwb24AzjA0BvratNByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBPRPKaM2_p7ktVKxP3JyIEJniWWkn12oxpeeDgBhD_uq-5UtWLP8gwjIWYiBS-zTMWiJEzrNnDA30z4a_gnbFhsaAKytRCZpBNKC3W8sfv6IJUmuqtc1o1YwYdbsVAQm9liM7pCQ_P-ge7tmStmaNRMeYP0OCCdKsPXp8PqfYcVqOhgccaGp6s0yZ9PYA0NmxXcyXyFDMIo8OB8IQGyqY-QCUE_KaR08Gsr9Dbfa0CYD0y3Z5QHPwpLjodYUMWDRJduWxJt58MHdK1uqH1NsITJB6WffzUyaKAt5V1ofYrzNbxlwVuEWrxqAfuo9lfYxizwTYcuCbL77q77ljMKaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XywJmWjB3fNK0Q6kmvZdg33OsFP7a9P4oZxd5LxUZw-lt6_mEdMfMp1Samg6qGNjtSYtP3WOHcWzv1HMamCyiVJbz4W6IcdoJdSnXxOgPr8SMpmlhrypU920HnMYjNjqWPF0565XNu6i4GfIUkUw9GdrnId6Mf8YhJrDWsm4j8lwtGIE37JCWqie3ByoGKRMphs5L0cfBuGQnxY1WKqzXGd4B4lh0_I3fFrq4Im9_EkbLHtXz-hz7xZA_lAWnZnGo7nEOPWA_qqeGXVFo4IfwbwZsB47v-pXkiErBQ0BDYfuFoZMvn4UPtwAdPruKbnLpwKLmhFoabmoXBIJZhrlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ANdRPiA4pyJI_ii3bDsTDgZHIgHWDyvB91iowD4RayX6W0peu28_jCMZwmyvWhT7eqMS5k8uEe1Fkxw0U1cpL5jQqvcsHps-8TMDPDhcjcXnJm_EGGL30_IZFqfH__cedIkLQ3WAQr7HtYaaEv5gqnhadR5vPqbfjzmztLHNY4O0y1eTPMkRB5FMxmIeqSk-aVsxIaIjJuImeaaOGohTXGba0vejwW0uvernUY8wFa4EGVsSiSWZsLQv7LnwNf8Aqc29rYzEFnoJQxzsZx-6SMp4Kn5K2qIwSHLvtW8KxKOmp1aykLPpeUDnmIv7prAGYVKRE23Z5slySGFu9IyN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=P82dcgSa0K34jLY1qBGadaxh4q58I5QghVEuKOWVxaTBY24oANxwL16nrIyn2WjYJSj6cU_L-3of1qCBfE8K8K_Y76Fj0jW4BfG4gRbuYVHGtMJpt1M6s3A61pvrTNG2JPOBPsxeZmhu_UwsyuZlpRDB11kQTzl2tQQwckhglIhKoE-4Dd3RGgn9ESUuF3ddSrczJdMDM_LAQyGw4RiRiOkW_FyT9HtLXkolrWqghdoDJQM1fUmhlqrYMQheEfLlJAye4g-X8IZmumu90E3WFzt_bXraYKUGgDZudzAe1JHHwusPno6S4Tz-h22fWsRXzp83NN-WHiBKEbGCYMbUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=P82dcgSa0K34jLY1qBGadaxh4q58I5QghVEuKOWVxaTBY24oANxwL16nrIyn2WjYJSj6cU_L-3of1qCBfE8K8K_Y76Fj0jW4BfG4gRbuYVHGtMJpt1M6s3A61pvrTNG2JPOBPsxeZmhu_UwsyuZlpRDB11kQTzl2tQQwckhglIhKoE-4Dd3RGgn9ESUuF3ddSrczJdMDM_LAQyGw4RiRiOkW_FyT9HtLXkolrWqghdoDJQM1fUmhlqrYMQheEfLlJAye4g-X8IZmumu90E3WFzt_bXraYKUGgDZudzAe1JHHwusPno6S4Tz-h22fWsRXzp83NN-WHiBKEbGCYMbUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJsgrBVW4eSY_e5aIOS8pD9HYM2RFrnojh_RNGfOkeNJRn1kbWpvTsmBVuAXWSwaHyMEhozGfqVqlUL9QH5cUd5zUn8HbReFX6V2ET86qRB2VjJClHyAjncRGpsFIRNJ_rxUzEGy5XlysZU9r-KzlVKFnIeToWCLzs6eLTdQWQpRiqPShNKTnFVK5P5fQmyK8JCjftPq1AzIzHXq6tl_7F3N7HSR9A2uwrg-Jl4SD81oa7iq5BQ1sbkvb0VX-jWES8Kcj2ZPE6bE7qL7Dww731cjL9g07klBw1AXFqAoOXNN2-03ISJDE3AgUBVFL_ozPuwNenrnDgBBlsTooTnZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJdesrUEvuSqhE6C17brIv1c5e5VwvQ1IrIcTlG0-JB72-gXodRk7EvFRR-FxDHKKIJIHFjDQl8-abq1ODhcVzhADzPKurCf_pZIGIm04DvJiM-sERIABK_du49GniqkKPEABOnRJC7KLb6tkfqTd5QneBrtdwd1nQI6igBQvxXf8FDrK3ojF1J5hvUH_eiU_eNHvkCxse4v_e49pUGCRHWpMfz8g0QfS6S9JRIwgRwLYnzF3YCTbQuXs-IqWRO0Lr2f7QXY6SAtLKj0wdqDfjAG_z9JTa6BzFZvnOc6WhbirgntHCtIyCy21hzlEAhtFxeeHL_ojpu1lV-5DwUXiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBJ92E43ijPRt9NqWre3XJ9lW4a0ARuE6RWu5FcG879Dd8z7R8wrwrXSM0dASJ7kPjO3pvNtTUz4xNO9TL_uSxI66VlaV4tgSKm0TK6tZ3RweXlOIqqdHLfRiMKdTrVRNJiVTBymDnFwCNCXgb3RYUJU0WbEt4suU9rRCvmac3wSmTeGop_lRfR_9H1x8Ok1E0ou5y0_ORhH_W_kvDJZXsXrzGRlHY4Ox2o5HBU2OEkaJUzH-6iUR8HEdZJc77zzDxmzBa4_7KJkcN_EJQo_CBG9tcYjMREXS81M7VvSPMgH_4qUul3i63PhPjzkcTS4AaFrtjiYSh-U6Kt4SBRRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=YjOncMmIfNvapJn3hX8kEmOP2yCHSQHwYq0GZ3cZXDX6B90EWYAAKJsEHuJxoiDwriAu8Fc20DYmbuXhTOtJWa3rsZViCZXKQmvSRErkMyHrZfio9JQChD60TaGXibn9_TjAA6jHvCHbkal6FpErBAdAZWdUEawb62BL-OfesUo3pNarRFNfX5r11uQbHyiNu8XkRI9k0-tZXg017jhxCZtIDuiumpfJ9GYmR8_Sr9dqg_uaqi35BHaK_Hf1s71u8_7y7xGT7V0svc7JDmaBvfHuAK1gtkzI0OJWBaTkenFsE7hRxsqFnZXDvI2cmW6633UOYTjBWKKdwP7ympVL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=YjOncMmIfNvapJn3hX8kEmOP2yCHSQHwYq0GZ3cZXDX6B90EWYAAKJsEHuJxoiDwriAu8Fc20DYmbuXhTOtJWa3rsZViCZXKQmvSRErkMyHrZfio9JQChD60TaGXibn9_TjAA6jHvCHbkal6FpErBAdAZWdUEawb62BL-OfesUo3pNarRFNfX5r11uQbHyiNu8XkRI9k0-tZXg017jhxCZtIDuiumpfJ9GYmR8_Sr9dqg_uaqi35BHaK_Hf1s71u8_7y7xGT7V0svc7JDmaBvfHuAK1gtkzI0OJWBaTkenFsE7hRxsqFnZXDvI2cmW6633UOYTjBWKKdwP7ympVL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=dBtPApn42QRtKlVB0cUU_M_Skq2Ch5EmTr-4FEtR479Z8B3158s6pm_hefa9OEqiEYaZAfnRTwaK7TNpLYg9h3f_NsW_Y9SK_johds2QBYLTCjgcSdAgmhvy99LX67fY3i2dJeSdTvnnUrZtN8V4rDlo5dpU4p7k01JY1YkkiBBT3mm2spW30IKq44PLBnxKQG7ynYcyffUrSXA-0nUYpIjvTBbopMLbKxMpr74Gdmk7rrvlQIPaftWdRHQFhfpLDrE3EghH9jvogG1ogXw88dRro9LtEtixUS93gTGfoR4hb5zBovVT1lH7ECzY8tQ37Alwd5AaTGvKK_bdRxj8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=dBtPApn42QRtKlVB0cUU_M_Skq2Ch5EmTr-4FEtR479Z8B3158s6pm_hefa9OEqiEYaZAfnRTwaK7TNpLYg9h3f_NsW_Y9SK_johds2QBYLTCjgcSdAgmhvy99LX67fY3i2dJeSdTvnnUrZtN8V4rDlo5dpU4p7k01JY1YkkiBBT3mm2spW30IKq44PLBnxKQG7ynYcyffUrSXA-0nUYpIjvTBbopMLbKxMpr74Gdmk7rrvlQIPaftWdRHQFhfpLDrE3EghH9jvogG1ogXw88dRro9LtEtixUS93gTGfoR4hb5zBovVT1lH7ECzY8tQ37Alwd5AaTGvKK_bdRxj8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqClKUWaa8LHgCvEt2kUjK7Faa_sJfjTGQBLzknbhvIQ2d2M-1XREGkRBP5uUSCHi_SxKsaVQDL0N6ByIPD5vxy9EgwO6D7nf7pvbfs3RuW5ixlzMatZZxxpyZf1tdoRH9f9qDp1AQnKTg9jn-lyPq2ylcZYEulvQKqmUZjnFUutjJ8jTCxUGb1U9_qlqcSx9rbzPCf_xmOAnci9-mqKtlLAAcAxMUcJyJYk5yvLgNb3SSfrPXmwX7t5A4XdWxLerCuzY7FpZpEuU_vymSj12uOsfQnUC5ySoW62uLtHdbW9DaMBaSA2zSB1oNRm08-PBdmYlWhcY6BNTxTuhs-dLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KxnjSrLTKkTTuOF31_GYWwUjSQ4-46SC6bXv4UCEw_ghbj_viMnS7MI85HrK7smGBmWMKgj-ea4J6QiHi3ew3PHKAaAmCriN3e-4ExHfcIzvDCW0Wn2tfZuAkEKWfrFNnYGApu4VPB7QwA0eyaNBGwzqXn-r_TBJw5YZLJ5OeaVHaqudN-1B8khFQNNi1yFJ7DVGRi7z6aNOhL5x8445y8CoQPlVoUhQx3Qvn8OxigHf0HOZRIcyZTNTZIMA00Hdzc-9VvoKpzy190mWeosc_BEn4ObG6wFFc4kcfUKrGA8KbaVg19i7tVQNq0ocDVVfqtXpFmrHaHPkb8DD8jwt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfbE6O6-0ZFqvl9FZQcX0VHioS0fmoNnCYz8L6W9gg1b4-LHzTKzn7YmGAXTIaEGWZBBZaWR3x6Aq4c6tBKQvnlAO48iDLpzVIhcbRds8LXnDsm_uWZDH2m_BD6M3A-T1msjw4U1ztbq5Jc2GzXOAW0fDtICIvnjz9GYyJynLle2I00CRBuMZoeKTfwXOizAJtD-AP9MwE3lJcj7V7N-AAYJwUACyX067UmntWLa2VlFU9fY2i6wJiR2470Jbco6TM42DO1lXy_Ue2GIOTCANNDSQod0_v_WV6fxT-rhnzlo92pK7E2CpbSYnjTnTH_AACUgwdUMkC2n3lh_HnxAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEN6JcKiLVFaLOSWH1upJO-CmTX5PciEL2mTmEc1V_RlQQTK9i_O6APkyDNzDI-bLX65AtQJT-BDO4jmxyj64CGvodE3sT6nNUGHn9WFVAqPbHJp7qLSUWWlXuAgu8HK5zX4iHzBZnW6CUf5hE1ULtO1oTD_eaG6MbUCwzJhj270ICTDeNsjOszmBHCV5DgKViHLeExVDq3Kha_KhQ6uueion_TgK4Devk-exh0gZQx8EfwTfU7czpPjbCKCmeLTFEGqZTGS3d-x3OKw1ZwqGBYt6tDDyiQaDhIIjfLUExr8DZZAT2c24lkEMl65mV2U0dgseS77bTM2jcOHcSUu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD1jBi9Mr8Jis7OnO4-nllo-OAI16N57iV-2b5mp1QO5lfdcQuYiXUcX9kbp78MHFL8IljVUxTTKkeK74tvw_qotP2NsVbMYSI4IJt7mgytZpCjrpPogs-0gE1QFc9lqHVQAbTicq9VSZDsTB1sHfHHRzvo7t-R1cOMEU9-n1LzomkIbrKmbO9POTuJzEuvErpMy_8YDQ3xr3wCeF6F0pynspyaF2N_OyKRna07OrFPXszKWrYMPCsUyYGOF9KrvkJ2gc9xAfrZiU5tA6wWRxavi3r00EFuFoYQBQDJSJzNuWfTCtC_z_pH3fxvcDEcwn2zoldQU1NIXouMPNUUOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=WQGxNNREcjVEGjpO5rbfrme3ayXx1Q1tItRB8w2x2MATCgiruaubvCrLG2IC_VRneMkk73IzW9Z4wYey0e2vArENab14BLEq7vD8QHIYVZkR-Aaiefb_XQw77N6LjZCm255PRjT875-GUePakyFmCnzCYKtu3uzqeWpQ8SwEg2J3NZxUtorO_gHaRQb7yGXoPjY6ncwhSwQOr7LmpmpdRDd_4f3j9zTX3hR2yF4W3Z2zXusozDY0BIuCKGUChZjlBMbCvPNRa1KUFoxc-ddi87Lf75MP9tGG9b1y6k7Do6LI4E8LwBtW5QhkFRQXt3ivYyHQezikJu72LWsz9AtL-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=WQGxNNREcjVEGjpO5rbfrme3ayXx1Q1tItRB8w2x2MATCgiruaubvCrLG2IC_VRneMkk73IzW9Z4wYey0e2vArENab14BLEq7vD8QHIYVZkR-Aaiefb_XQw77N6LjZCm255PRjT875-GUePakyFmCnzCYKtu3uzqeWpQ8SwEg2J3NZxUtorO_gHaRQb7yGXoPjY6ncwhSwQOr7LmpmpdRDd_4f3j9zTX3hR2yF4W3Z2zXusozDY0BIuCKGUChZjlBMbCvPNRa1KUFoxc-ddi87Lf75MP9tGG9b1y6k7Do6LI4E8LwBtW5QhkFRQXt3ivYyHQezikJu72LWsz9AtL-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=D1cCqKLrfqaNnk9aFFaBdsNDSCCzcH11MdCPFu8F6yhQm_xqu-g3khuHhQP-O-4TPNbJeZdUP0wwjfPTOMZcJsPkgnoGerH4XN917tzPomd79A3UA9IcZ_DswmFqhYYEx6m47_-UwO6rLj8Zs7qlBf7FJuMnpOB2RPPM10qTfRKRl47MF_JiJl1C2k48hBNtrp1he_9FonYVM7guvL2AmjqUxsrV1M6V4BLAfyC12zrFhhKX7DLyE_3GCY2NIsiooxJoQ-qweQEolKdc3XqNzOwlgOOTNn2h7duiyJNAEJrZXSZd5wc-_YS7lf18C4T5pQG2yEdZYQR2hNiGK0wBug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=D1cCqKLrfqaNnk9aFFaBdsNDSCCzcH11MdCPFu8F6yhQm_xqu-g3khuHhQP-O-4TPNbJeZdUP0wwjfPTOMZcJsPkgnoGerH4XN917tzPomd79A3UA9IcZ_DswmFqhYYEx6m47_-UwO6rLj8Zs7qlBf7FJuMnpOB2RPPM10qTfRKRl47MF_JiJl1C2k48hBNtrp1he_9FonYVM7guvL2AmjqUxsrV1M6V4BLAfyC12zrFhhKX7DLyE_3GCY2NIsiooxJoQ-qweQEolKdc3XqNzOwlgOOTNn2h7duiyJNAEJrZXSZd5wc-_YS7lf18C4T5pQG2yEdZYQR2hNiGK0wBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wAGImNO1OkP7l89ib_-DxGxuPG2PlUpgMBxIG0rhwQKBLyZd48F_NxiUSNsoVrS1ng9bUWj4ghTsc8O81RmBLpWE2-OyFA4SwvtkpPfct_YijgJ_e7wLX20UtGghPBg0oUvHu19vEnrKWxAojt2c2h9RVRgctmcPbo8Yd0NTVpperKeKRh_BOoV9yTZ-BIaBCyJ7_weZnsIO5fhEUyQ14FwCGKXdsZAj7wr-Zvm2WjIXCWLjhK5BXppy6aZ6YXO3LifiYkp7xsD9zaoj1DAfSDW22fAk7rZjNET6UhKMwntICDIW3VS44PYqXQiXIiY-wGIVfwrAloNzaPzhRr2yJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pgPvBdFPIGoK3jazxwGf-n7htiNiAQtgapjkh13RwEcZT_-iYRJkfJqjCZudMO0pug-8UQAkDLzeGBS-k3rUTOYdW0gVlTgXsxsOLfLo_MWSksO9DMIdqtzu_A4eM0G3r7N0kAwWlpuwGsa-rMuK7XkJnof1bwdHDHRKaTTrYLx5ZE_E1_ZhULmMhSHktUcx2Wfx_I2jKGohEfSm0K5SicWN2UKM-sm9odHr7ilGUb9glU8mueYtztxwTUhncK0tQ9QkzQHEZcXIdIAgrrTPIXi4QQZ_HV6cfjl1bQZKxW8Uv3qcFW-4ykKLbdCMyz868khAJPI-wF6KlJo8hZnBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvIrZdSsE2byPUAlNo4O58vxpGM10BrrpUGg0AxyaaQtqmcib_7hIHZteClX4H-MF-3vYSJpIpTy4pAhfxFKXpb9ktLFxfTuUFJgwwPXm1lm99Q48ANuV9eXt65EDw-DIeF7vu1fMHhxyv_QL32p85uhIR5aX5Ari1Q-pqBPIdrJckTBZ6bZtU0eSp8vB-gVrBV-gZScDwzYbZpVJJs-UcBx6P-baxZDK4oIntSovnPJng_nYjNwYHk5ZqAHylxXUv5UODMO24FQPSw8b9cjb0X3MWk-lXj1iHuC40kgHCqRlGoaGvdN1VkUVOaPLPo0TsMTm1taN_lN0YE21zEm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
