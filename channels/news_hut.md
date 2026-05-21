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
<img src="https://cdn4.telesco.pe/file/kKReu-6fyG43823cOSG1LFmMQu1WqE6uhWVdCuL8pdBt5hMQr_CAABJFaYak_OMt1gOw5yyTaevRWbDz9oun0YV8Xt7RPqU5mx16ijjN_gwBYW9sB8VZPePANvBZEUuqUQEKuSxd5ya8ilMbxxXvunjarm5jelwEZo1trjdg5s0GsD-j4S57hYKVrTGrkZD9azz4NiTkwiv4VHkaJUn3Lg79WkGfASoujw06dwbquidT-PUNS0GrVHASUtY8vLC_IXockYAw3NxoG88UAnznz2RecnvhDjtRY2YHKOz3l5RxNGhyPBZGYgKz9MNVCfrBSkc_Nd_0kX40OvfxB06Nnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 141K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 10:14:44</div>
<hr>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYUEd9QEJ1q1FCuEWNy1x2C-h-CFqCTvn2UyVe8pQk9DQuSsBhKBqL1--2O5skRcAtHDJOE8J69MZ_qqxdTiaWfWuPVY5YlRdUtQKDmxnJj8sVPftsgo3VNUHfN1auVRTVfB7wbOnuPYq22P6wOUXW4h2CfBWfuMtnVfjMogb4kP8Fe5XLzAHfVwj4YT_ZJEEdVZ3O95xl1hIc-wZ2Vj2vxvHVJD01isLRrMJFk2vs49YFnleMr8v8VSM_dMSQPQQ22toeXpS8llnfLFMsPcbIOuSbLJM_lQIWDk7wkdhN_sAlLyC2TB__033cfrtRABpYMu283gXo80tcFFzCqopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcxGPt1jEVhsispUmsHyyqBmYDfH8k0Gqrg3jN5CBVcUSpjAf3k62ue0BxaXdI73TN2gfu5JPkE3a1ih7BbiwXh3IKEyrYjS1Fh9_0D9Pbmrdjz78l4dgYiDmHDLJIz6gWnyzz8wHBPG99ki-626rCxnt1XW9oAPl5S7TKDhg4zkLwQDynu1XYOmfDJMYEcdu6n_po-FXYDQrQDLBhRGmF98lt7tRjuE4fjcN-EdWuspXZHVhZu7uc_f0uHKae0h9KXjPGBWXPwCgwhlm_1VZtXzcXtO7HvWBXPuh9NsehqYDjEeZCP4fPccsQTmz28jbx7xie1ctDkcNAtMdYVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZPxGJolenhBv6yG5U-NkEW1tz-mxW46TthFGR7Uyvo4zx50vKmTitj2Hjhypxip3GgzkIFQvYUP9wZardj0_M5vfnome7cE9P9LY81RYsDkYoR-MFg3d-H-5m29WgZqTpqt0c9bkOcU8pDXXX4ClxCMF-53Atd8zt1m4Ci-XesxLo4j6e-kosbdRBJ3SbBefncEjmosPipnxm-Okq6iPi3IP-QtDAbgPsquIwAYDSdPZH8fIi1uNK8J9wZTI1KhdO_lXN931G0_Bj5EWJIDcgJk9wdiws35tNnhz3tMrtJKRPqAb0SPbETiNpGBEdAm4kgEBxAqY0wi6FYFZoeRdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84fs079zHmHkk077wHgQqTxoztbl8NpjRuqlMCbXcdK5PGYThW3mDtGLLGBjmH5OcZGy217ZqvsKUN4BuuDw8T6kKu5n1UothFaWXAt6lyNJ3eek6NhH0SpP1tOTm5G1pSYdIoxDGpta9Iwuzh1kgYOGlMSsOYFzfhMYuWAl-MagiZSRr1eu6-Sovnak1cceSPe1xyCK4LofZ9gXtOXHZ6vSkL5zVnYygvRnyP7JPbgCzx02pk0B3e3De5L7xZkWZ_LC7vg5qWK7F1rUySTFwYObXmRLNClI2TJpozuJEkv4guMvLA5KQXHNUrfA_M9thHn0j3XaVPRXvSNvehiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xppes16jBr6icjVEyfw_RVuywgbv9JAynjxL4z_DDKmTexdGrFDLJ71mMZFPGy4LMtnZYppTEvrCBhSoATslT-ADoHBDX1QPfO8kWdVn6JR3EiCNVDeKT4Y6-K_36_NTAg2filUeQctNQeJ-hCP1_2iOQSIuWQOugDVbMiGXYPoZK7SbT5_SibaBx2Gq6DEuE8F82FvZz8yVTRel-aX_-xd9CY90_f3baw2fJSYK2XMjSYPxenZOqZv4O6oHttWfUplvfg7Z7cHpO5juiq-2s8g4tf94LDCOfWNiEIXSQ0da-DnT5Wquu0ACPntE1ZMkg0a-S1CJuQ-Gua-xk2_S2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=mqEkkMbFOSglUgy255C635OESdE7XyevqKazRpNMpRV8t2Vd5e17E2qcZKCsuhAukCzRl3StQWXD9_B-dzwkrFwoXAXxCBT9VXXJarVbOVAd8gFfcSzhiSzE7rHbJ-x79Qwr3NHb22cFBf6wsWp0p4VgE096fIeFHgDWKEbMk6RluG4sNjuArqD2TpwThCBml3JN49MwoxKaf-VmfmCtu4-2BZvKEeSKnQjiEygYAbb0CWQkQkW0_6sIm-PVfF2Gy0NaKdF4YCruBvScAJvSxry2wOIIoszzlIkCuRCy9IQkdc1e4nhHYWLWl9GwmfPcR0VVPOgD6t3LBIfqzoJTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=mqEkkMbFOSglUgy255C635OESdE7XyevqKazRpNMpRV8t2Vd5e17E2qcZKCsuhAukCzRl3StQWXD9_B-dzwkrFwoXAXxCBT9VXXJarVbOVAd8gFfcSzhiSzE7rHbJ-x79Qwr3NHb22cFBf6wsWp0p4VgE096fIeFHgDWKEbMk6RluG4sNjuArqD2TpwThCBml3JN49MwoxKaf-VmfmCtu4-2BZvKEeSKnQjiEygYAbb0CWQkQkW0_6sIm-PVfF2Gy0NaKdF4YCruBvScAJvSxry2wOIIoszzlIkCuRCy9IQkdc1e4nhHYWLWl9GwmfPcR0VVPOgD6t3LBIfqzoJTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=Cy_BukeKtj-GllQ0xorFAm-yvEdLgGTqLygak72hMJ1lDW7Ltvxm6RG49pPZYRJvcvIFLrXwaLrfBrXQEDiFSzTjRKuM0s4cytN95z_RgzN3wWC_ZnhLjwsnlaESMnOQAv77e_qRJ0_Up1Ueo_B5t3zQcsovWOGA58kk1Sk_7JNkcGM7WFz5S1l2g7pecWPgtsafDRoFczrPMmZ8Y5lR6Jzr1m1tkYboTGHcFErh8IapS0TNPeSlFWpz4Ph1EZqx8meTZZ5GDmZqYBSQIYNwDBGJAGWbyGo3UtLCP0Ki4vmdVz5GOGytFEIg3_9i0wmdZs8nF4jqRZFmJofE_0CQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=Cy_BukeKtj-GllQ0xorFAm-yvEdLgGTqLygak72hMJ1lDW7Ltvxm6RG49pPZYRJvcvIFLrXwaLrfBrXQEDiFSzTjRKuM0s4cytN95z_RgzN3wWC_ZnhLjwsnlaESMnOQAv77e_qRJ0_Up1Ueo_B5t3zQcsovWOGA58kk1Sk_7JNkcGM7WFz5S1l2g7pecWPgtsafDRoFczrPMmZ8Y5lR6Jzr1m1tkYboTGHcFErh8IapS0TNPeSlFWpz4Ph1EZqx8meTZZ5GDmZqYBSQIYNwDBGJAGWbyGo3UtLCP0Ki4vmdVz5GOGytFEIg3_9i0wmdZs8nF4jqRZFmJofE_0CQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVH2G9KROt32B1Rpu5CPQb60EqaI9RViv6BxMTHtl7YTupNZPPQEnfL4YICB9klIrqEEzVodOiWGBMGvDiknzYPif1Y4zWjSZAOTzh_b4yA-Ioxucf0YyFb12qxBFT5v5GJ1irgV-4MeiYOaIZ9GNMpkvZX_5vxBafTa9svLwZcjQAULk4WHP1HH29h5-XSCNgxFPoxgGI1Xl65heODjCcvASSKp0eEGCJfaZ48_wGef_tVKOq_w2Xg821xmXU_8s3dVMhPg7WAk5z1ugQJ_I88JOe9cY0mdF-3UnxLA7hiVSR64H2NXwDtsg5wpIaJaYlGR3nSTRnIfXq9DsOtz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4qfr4NxQJTwQf8_a4RL7POdjOGpwubK0hBT-8aDGpNBVnFPqgmFyfWmOTRM8pSHtBtZYT5y2RcAzLMBv4UXOtWNPxQu6td48QXenZV8q6Ln0TTAz1GijhCcOGz7AW791TV8HVOo_6dE93hdEUjHhME4_ITxdSht7Dm6o8tbS4VTt8ZA-PQpeX7_RZKAMVUCKkrY8I7P4A55d2oL8HxXa9Kmq79XCyPNewlrFAitXoz6Kmsz4Uc1ZqE5DNfSB_QI1bpXoBS4qmYlZnyY0Etc4TiEDzlyEehUzEvGsaVEJn0Oyat_puwIAI6RS2ZPyPmAjvongaXZNcFFLCFsd9bVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttlNASEL9OlSYz98dPa6IX_XYXz7PseyZz6Yezl3K-AJK4jUOdRxRffTD-Y9P8mfcxL6jfL8Htgb_vZKRRipUOsxQrHfGDcDJKFUGnZFKzjPvJTFlwEZxwHpSacTFEwEmOUPoWLXWTQzOHtxG0jFb6WSxn3aGWuy3DfHpE7olCjpEefdicz2_TmWLvQsq0Sir9qTM4dYWrr1DoFOAAivKXpJs7qBo2Qm2Q8awtOkk_V2h0xbzVRzcXpKLyeEh3x5uSe1-Ws-WEMofGG1Qckv69Z2kZna5UJZLtd4tlBUvQtJTFgAtxClirGj-4gL9miF1DLq26WAao_Cy95jJCmDpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvGLM0T9bHNPyciUOHoZxnLxV6NM5vPESG31gll-brRuUfT85WbJ0JLmj3x3_NIWH64xk-o5GmU7VlrMX5W37qCAMozsxx5a2PyfSQKJ4BfxndUxyaWiyHJunLfIqVS0zT6oO9zpUZd-JYjZsf--J1-JO_HO069OeEt3I4YZUwXvXNs4RuReho6aBXtTX7RaGnETRQO4f7tbaXfw3WGVMy6iNA30PdvVq3YZ2uwH5igxHo0nLYaGCxM52rDXq-fVAYrEYOnM55xA1c5Ctf5SAVDSivjgP5U9PMKp89x78HCI-O3DcX1agiuDjv9L3aqpKiP9E54pvBEbr2_x_TAQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYDtU1AsNPswJUrbOZHCbQi5WenDK9rTuuBY4T7P7f81KuvPwbUdkWyxAb5R1EShEn4n1NAckFsdccG6hnD3VByBOxCdLnsmm-PsY0o8eYCNUGCUOxjOQAiyXdhtSZIlXto2iG1OrAYdyPgr4QHCZyH-EkRfHVyXy1KRozJ1VMUyMBF-w42vg1gC8kDEqTWIdYPlE25LNdFtw3eUMFXkqgl9C_YnynqUBJ5lmF1L7nqiLCG1W8Dt1v6-4L3DStOiSxtEeap-J3hbIiXwpIqDL8cVlYYY7OWUzO6Uw9fmu6KtCFsLbdjK96f8fQA65ZrKTcPRUlT5WO-Ez5iCiv4muQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rvZyhCjkF2OhXgNo6UHCJY9nT2gd5g18b_T60vcEDMw8gdvrX-gGljUCREf4qEgqYYBsjum6NDHWCTsEG5WZsBgeNSAs9NNRba76u8G-7N6JuI0mCZYmFnHnu8NljMvrn-CK9TuC_VSi2tuQ-fmOWtqYxhZvaxL4PvdbMkNsDbJTo8vrPEi6IyGUqa0kdO_6TiK38Xi_c3XAVNYUF-xuyK-15x8nqnsMCgWgKt8-nn6Pr9DikeSXpf4sEe_2agM24cS2J9Dn9v1Njcuhin3PdAcf5itmw30z75q6IbbqiInxlZGYKkGZDq3FgH--SY0tiNAphS5H-DCONoCWVNd2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PVemp8tK9H-s_lmU5Q9Cy_rmaMxNJQ4HuYNxF6_9hZZ4gWHb8StZnmGULSDvtZK4_F_qgBIA_8tORV9TBvfw7KjsGlhz2AcDS2B0ZE_3oY1BwtkchY2Ne9HP9JFjUQYn68x1SqcMbihU-VOAXdAYc6U4eFT2ghcA5XDi2kxCvLBUpx9k170USJTz13ecm-F9L2kkuPLl8SRLI9C8Mheu4FRoL_3st_B7-pCi0fAKJ4z6za1LIq8_PEfMxMybpSeD2O60MbYiRKPhG16s79U9cAKimwMUZy1-s8h-ZVj6oJXVcac8BI6vPzFmCcP4U4RnjhvDT5wi8nJBPGco-ofrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TKptSfuuaMqYXNTScZYW20VipeHXr18ZqJWHe0Si6R7JtJXVCQSE-7-Xe4REMcmcV7giGTVk-fwl6WFUtRISDjuBJxNYa-ve8UDMpA1ZCijuRPmnnxTAP9mw6W_gP4s7hjv6rjisxNGPs6gioaPzbmtpKXWQmbVrpIkr_iMsBgWdYwJ0FeCIJ9xPsh7PnLLJimDaDtu-LIu6PKQpktPNkOg_JypHtbznzLbxpZP3_gdTT5ukXKe3vsr-EcrKWooeRYssTMxLaBjILTBgXbYKInn8X8HZ-MMDn-TpqHUYL6wrtFHbKpDkO1GiIdUlRNPpsOZf31jotPoHEcPtTeaQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X2H-ZvV1CxjyAxFH3sBu2B__gsKhNhCbuf4Lw5e2vvTJa0gn66zsWW6vrH-GSuqdvZje8yMb1V0wqPD5xwZS-hXBWfwYcmCH3HdaEDOsLRTLCYxWgUCIVxkh-1S3pdsHbbtZgH1byWwUDKSGVnZSeoS2u8q6Q0B0iud2L-_Thtnd6Quviux7d3dGc6avsZCL_Rgw1fAfYVMkqmiSXaDP76eV68aUHbvi0_wlTtdm9ptEQI1gvyNm4ubQWmhqpnz9sXNCBadx8ccv_pR5lXWAs3hohEOklbc9tMg39Ccdtn6YeRvJqGHW1MJVlk_Aij8AjkC2HSyvJaVeWXY5_R5q_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QhEbTt8GeZzbPIe60oDGa_bebURvQ_krRW4fIsAFdIFaeVUF7ADlOS3LIWLuARZd0YgxOzqkKofNZARCmYUm7EL1KZWbOcAL_AfWUq6ltxvksHnwxKhOdoKUMDFSHWDhHkGlEniX7iKVrErVrn7uPq55pKXHnzSd2OmsGreYDAGa6tyyvWkui1_014BVhMm9ZjJO4sEjLdru0M8R_wkcz2qRDRHpFVBCr83LBN1T2s_cMQO8TuICgeR9rIClxvQO0jdggBujmKKpwIzbblplUd1x7fGcpwEDKIPBtpmdBAjdOfV3fymbHqRfqEYirE_eTr4sktriwApaF3IA1L7EgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XAYuzS5XVxrL9psN-j_vedvajbCxXAKR1jYcmnguKHdcYex3xFy79LdW01DnGiaavx9l_1UyYcNpqYLRQM0ha9p1IPf1FRsqlLGX1n9A6YnMW3bKGonvGmoMPmNzeKVQmYVnWtfN3Qs5UbJY208W1cM079DXp5ZIsqAZP-jfpHk2LArAcYP5iJeRkLfJcs_VR6phsDIqGdTEOrXN50sLAjS-UeEFOd1eI3t2RCYnnIRk6zgC35ng7uxTpVcYJXshi-d1Z-LpmDiuQoQgfG8OESXP8wXdgKj4lmwT3F2IoLyW3YtkFBlWj46sZUOooPkKuAK-7LUJN4pkazCQW_oJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Laz3UCx6JYyYQRP7grjamSn3fCbBk49Sqa4ta9eabLcruJgEPG8wcN5x1sj8fexJ8MPNfhvzFBLg5vRsAq2AlKd8JfO4EVpFCOENGTtWIMOoVrk34edNVX27VnZW3pmHXiZO-1Y5fb7ylWwWHg4vJSm-POBmM42gagU0CMl33Lo4FZa7C2zCek4FlE4rtaTMSa61SZ9fXwi4-NTDicWTJ2tEcmyugQUnm1yRBC7sYeBf0U4IbmrcZk2Gteb1V4qvqGyYKhKZ2elxlzzbimT9v5vYCQH1moVTfkD745oBlX1jRoeqT4EDSd1Mar8_CGfOWa_87WbKQTtMcAKaFR0lqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIXfLeeEk-F9Mfy9JCg5oPNjhUV6ORhg9Agpvv63cTmQBmQpBvnyyr8UqXid6rEUJN1rFL8VjbaCLg3BQxN_BEZz73svfcxKucDeY47zg2GlozOZ02URDELfV-LWvpF8_jrxc8tBP4KMe62PePwE-k6vQB551Rkl4goxm9DEXaFMpZMyS9UxeKbrdTT3Kp0aUD1VDEkwAJXFqzGKADH7QCQEJ6DzZRauiXBh15o0DF7lMk7-kJ-dfF-BgZBlwEYKYzZ1FWyFNs-_tUhTBK_T2nJjIUScjaFAlEyQyHAh5IOxQaSzxeN_RMOHLXS-b3HaLXBKxh_BhDPx-UlqEAZM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EIS80VYWwT4WU4l0FgJmwY6MT5NhNKZAugZjy1cqG1UepI84ukwkkIx3aFeBbrnZX2d6P0_eonNOoR23vm72YCKxrp5fQlA-wZ6eUjKk8sbcPYXUUY9O4TjqMOvFT9nLWkHWE6J-nH7c7b3NQxGCHrAFmgFcYVp-b1MTAsAbHVAvoF9St-r5jBOhBEm_ZkQob_TU9Vo1gF_KCqioHbzt5A5aJAKyQPNTTJzQ1JjWkBswFV_TaBUGWNOKbrLauEYB9WsRS0lxgGhXM0ARWPzgs19_ZYAvOHsUq0rQeQNVi0gvk8qie3FABO8Wq1ESvm9kF922AdxjI4PgF3N85O8crA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClVZFPj4a_P2_14k8yFX1x-4aVwHiWnyg_MP0g64RxdIjj6MtHqbkojVnJoP55_vBmBRsfhu065KBVCAFXboRX9SrgQqa8GEgbA8v_bjvOHMb0DVufKTQSYzOzDqJfvU1Vyz43UIxUmoE0MwsZkjRTPVniWzq98xZWuIvLeIrANhv25SOWwIBbYHxpIKZBvs7XA5faaDocPRn5YuDKavPLBR8i6-2m1RHx_uSPQYuqhK4Es5g4uSwKrUTsXK79WkiJBtBFA6G6SPm6flPYI-JMkI9sxSMHrNw2Lt2sQKiHjlEsTslZo6md0-ET44prCaXmh2NySFV_IFx6S79ajYQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=AesqHsd8bbmcRUHpc0dd_B9bdMrAjByRVwNGAeXtmzZY38hrYElI0H0ECTACQO9OEEShtBfMs549JXbcFd6EV8kXlGAc2ZgnOa9pNCAIpC4FQh_t0lhaI4jBpZF5GY-HnQNO-bzYHvJxifo7epvTgf3axyNDZ9cz64YH4oAJob8b6jSOY27rQYw9WGiWkOgF84fRuXAFpf1Awg3ZhwdQ-sTpQqY3L4VZ3odFrOh5N43VKfoskcuw-3fuDjrXHItMRUz3E203K7g2o3Ihpj-7nv4yNrRq7tLQP4lB9JztMJ_fAhb-Z-ugn8OpEn57AjiZm8xsQaWT_f31GHRRmQsz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=AesqHsd8bbmcRUHpc0dd_B9bdMrAjByRVwNGAeXtmzZY38hrYElI0H0ECTACQO9OEEShtBfMs549JXbcFd6EV8kXlGAc2ZgnOa9pNCAIpC4FQh_t0lhaI4jBpZF5GY-HnQNO-bzYHvJxifo7epvTgf3axyNDZ9cz64YH4oAJob8b6jSOY27rQYw9WGiWkOgF84fRuXAFpf1Awg3ZhwdQ-sTpQqY3L4VZ3odFrOh5N43VKfoskcuw-3fuDjrXHItMRUz3E203K7g2o3Ihpj-7nv4yNrRq7tLQP4lB9JztMJ_fAhb-Z-ugn8OpEn57AjiZm8xsQaWT_f31GHRRmQsz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=h_OARsanAKFcvW6q-4IcCDQxn6mpHgRDif1UlSy3jIFPczALxgXylzaldxd3MmCnsb8HN1PrwNHedOEYYbFbA5RFJNY3IO6z_mEyy9Oq7XRbFLU6C4GX0niBM_sFftK6RAZKQLsSTIPBRTKe49dOv1FXUx8FyZgrbU_s123zcHHKjExsUQJh8nRGGIT6AgzlUBTzmgJSsj5WVbR_j679ENvcvgLwEue2uZJsMRBR1VVI4eYoZcgnqEsi3ANBfN71Q3o7ZVysMM3KLjCzyOLSCgsq3Sm2-IcfcJtxyaLTZwmq364iGpDT8qr9eUTmGsdLO0kvNf1b3Odn6YQIOLiiIA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=h_OARsanAKFcvW6q-4IcCDQxn6mpHgRDif1UlSy3jIFPczALxgXylzaldxd3MmCnsb8HN1PrwNHedOEYYbFbA5RFJNY3IO6z_mEyy9Oq7XRbFLU6C4GX0niBM_sFftK6RAZKQLsSTIPBRTKe49dOv1FXUx8FyZgrbU_s123zcHHKjExsUQJh8nRGGIT6AgzlUBTzmgJSsj5WVbR_j679ENvcvgLwEue2uZJsMRBR1VVI4eYoZcgnqEsi3ANBfN71Q3o7ZVysMM3KLjCzyOLSCgsq3Sm2-IcfcJtxyaLTZwmq364iGpDT8qr9eUTmGsdLO0kvNf1b3Odn6YQIOLiiIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ENQAipeaA8rmInAVfAoFrRKnjXl-8axb1ULz9nAGHOqrFjNMbxe1cLtHGiPCW3ooIsL5rO8rizGYkPEo_5VQ-R07AIOFBHzeS6wJa_BJkjpH_6OYbOxR1I2zKL_nNTnd4kmc3ldPKXfwyn65sawQPt9kkkFlCzLlZyc_ELlgjwCKPmdEMn6LqrQGJRzXivA0DT4ZzspI0YQTYH6MjW-wMk2r8CHu-agvmsoD-J2-IitUHq_rLRaCJGvR5VBiZhxKjkyItbGzruaVNyP9lNDFQulrFrIsxBZFR_2mnuSnBpiaj8pQySvEelu2qHzvhRYqggwZDmaH5wO7Gxac_a7ubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxBjF5x7z09VwmTANelGyqbEa5ZfDlbS-wKXkrDv8phTzURk8l-5ZSqE6bBOteKBjlgicM3-cefSt6PFwdOa_fa13AffOoqeLNiuGXqQPYXOrSIq0U_zEaXALxcjY8h3un0w-NiAA_K6Ig3rSSAiO51XfWDrpTHegwdr33j9Nf3BoeCT77HTAV2Y5u-yO8n0WM6CwPlFmxIu9IoHQFsizsChKdlHF4aOpno7kE9hLWS9T29nZBqdC_uh3XxGhrMdfhqGwvtPLq88BFPOKAh8zZuDwXP8Eq8MKd4nJGNpB9LzLeLiO3LYSHmFgWTsm6enb8ya8PnFgNBfguopr-gVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH223a8OcZ6jMYMyR8vQQHbxFKF2cs_sQsfSh88248QJwbClV73RTK2wkL2CTptKxbYGXLPW0uKm6x84TH30tB3YluO7J_H1zv4yKA76pN0rALz146hOZQiDSXkr6pgvsJZsvR32HKyj_UZs3kf-KGxsQ8vKzNFDB57wGRIZTOpwVrGYaS5vRRff4RORyGu8xJYcRoj0XUDG6QWIyCcs5stT_zYHbFb-iEgedWXj95ZiR5LG6Effw6akrBDbwe6BbWDAq0pVS4to9dndgVbijiS8q-hm8xIMDk3gS2WFsl3-2xk0ghBOpIn1qXgOa0GZId6UjxPDSMD5kIiBwutiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e0CGmCZr0i8QRB4JU8C0xSDIgLNOc16lTeS8X18hZPYJoiL4UBamHAi6olkEksJR4B3ZBPILuOgzV2jjfT33BPTUdiDISjzUYgOQkTYMx6W3FKIrK1WLmnNdLiCVTtM4uZhbDaysNpiG3DbTHacCFOvG56qoeNJW_H94oVgtK6QCpEek8kV5-x8D_o9gziYhb4_8enZDMaEvvtW0HL9JVUrpHKrdtjNd3ck2v6hBGQEu5YHrXhfYKCFGbV5W5ENOtOR9kIDz-1H5onByekUIq6DkHtIf0nsMN3DjNIioPPmFl-NaFqNio-iIOOHnEeTh1MyzgCyD9ybJYRKDpptdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe0Jm2T4QeDs1J3cWODDCCML3a1sUZvLoO1yiQ34PE_n3M-mWtst7JDz7lU_0J8CNm1BLC_A1Vj1ShGof9_i8kVq7HNcP7yG1jfon8psLfaX-eltUgQ13XEZWdgxP_0uwhhJewY1vLU_HXQVj7G4V8wvqcTgdGQx17ol_zKONK1UM42Eg0xQMHPCr19A9dJ9O59tCT-UsWb6NOqL3swfIno2_uV-zx4IBycwFMvL-4wbLXKaWNcc4rN3di9CzwSOjZgA5rDuhhVGqFcB_CHUKwHiVY7GsD_GGmHHfgfZ-vTyeD9vLADX_wqymVhrxxrsDeIDY6j3geQDvMlKJSqpaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l10r56F-mewB-DefDyPei2DaompSe1P_MT1B18rSIo0fjs--LSJbDl6jZkZRqrMkR5Wwr6RzJpQNAC3jIPizTE_O9MMc1BpJSBbdpR-kZcm9wGKtd4Yvir-waCgGKPBSLisGBGr_ryUhIaJa-HyyeCUdvsWawt4oKhyvpe8cHrd-LMhfdv1xHqofd2FRUXixif1EZCA_yO62gmuZPkMn_yD5YpoOkTfr-Ntsg5Gb4HPX1pr14NSgeibNMn1LA8J1wjzKb-wUUk0Z4ycQ_LBSwuisvZvGQgohF7vrDtr550brUITF71DgZg0mHyE0wZR6wFKOwy5BsLJjjWCHmdFAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=SRDxbzv5lbiulWwHYasN8lyzfi6nGNV8mRFH7TrKj0MhYzIcQtu6uWKEBH6rMzw3FQOo7SRtRKI0L-jth058JzK3H0BRS7G4vFBlHzGLMpcFEO21pSmAZ8RadSyUn5VAy-SJEYW_iGdr085F87Tg13dMkp6SkqD5-6ibz6r4tTrDdUF2afXwx0r8uv0pKP61kiXGugvsw5bgwtOvlvejaWDq78Y-Tu3UTScIkWk9RxZvMvulMBbrjYb7Fkgmdb_eGse1EreIg0pXkruy1BK3bjExySWmKlK0yRXl0Co2p1PzoslIuSZz0yk_ZefLcl432RyVq47EYksfkDiiTwfVOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=SRDxbzv5lbiulWwHYasN8lyzfi6nGNV8mRFH7TrKj0MhYzIcQtu6uWKEBH6rMzw3FQOo7SRtRKI0L-jth058JzK3H0BRS7G4vFBlHzGLMpcFEO21pSmAZ8RadSyUn5VAy-SJEYW_iGdr085F87Tg13dMkp6SkqD5-6ibz6r4tTrDdUF2afXwx0r8uv0pKP61kiXGugvsw5bgwtOvlvejaWDq78Y-Tu3UTScIkWk9RxZvMvulMBbrjYb7Fkgmdb_eGse1EreIg0pXkruy1BK3bjExySWmKlK0yRXl0Co2p1PzoslIuSZz0yk_ZefLcl432RyVq47EYksfkDiiTwfVOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj3L7fc7IKV4Dr9eYyHyLcoZmfilVjXVTM5pPSMItRNFXnlSd4SLjSStJyNJOLQ0bId6kaMqanf2-nC-6vkelc6ss5cWJcWxhIwWvzC9AKgQfPrnnF5pp0uVmEJG9rAi9byNFpuIVRMjKViLQooGnqc1mVN--gVNpCfNnpHr3BcdJohW7BO_EOW5cyvzuj1HcAqUijV6bNuNzhPcmZhsLNRcGvoP-qBfeSAf1AVtg8mcWSOEyZmu03WfJHLWTWzwSLz9vhjdhRwWepwrNnZOxmL0JVo_YIFvpeZjh4r6y21sHYRYd-H-VnEbHHRNUvSF0qa0WK6mny7BOozs6TZYhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7GbIEHLtxBZTsZoFVqaipay2L-QQ2bBgjG2PRK_5z97gRLYI9CI9OTWdB9KOl3BSFEgDSvLrwrj33nApD5TSANG3QU7yYiLjI6CrBeJ3UPMECnuEsN5CdfdO62Y7BCJ6cRt7x-oBaVR20fQ7iQm_annSTm96fyeFCuqhrot7gtYHMelS8PaMRAY4w8FGiu8-nd7TfbbEa4pKBkdPQMXiSVlD0LKV-U9Lmsa-2jvgVJRGZw3r0FthB0o84O2HSrrEjVWZs5-l54J-dz3h8ensW_R4S782fmCoWoMLslA1ZwO3NznHMpSV8PQqQX54n6pSQ0PFCRye_-hPNYC-Q0H5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ek1eHFpx3bghq6WXU5P14d7PeJwC28t6jBln2u9QpchA2VG9r866YsmyaZLyNXBXAJoZWwTl8yCSrOzpphECNoxw9It_EfTtPBq3E6OcZ9b3HuYXDIU0UhLHsit9D3QjIpnOeOk9dkOKOA0r17RQ9wJ1CoOt6Ei1CAQG4kIi-UPA5dIPcpwd2NiTDCy9IAXFTdS4h8A8uJiOcYHND3qN51M7Hp470xFRvUiz6QdtHu66i5taE-5quQTlXYA4YzN9Twwyh8cBtKAo-zwTFQ6GeXcXgscJ0rlW5o6lwvwiGrlEWnV69SLbMVBjRr5ngCLolE-JjdXpow7V90ftX5aklw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM77h2c5kf1Xl3e0d28k-XCumExd_LFduNvzd2LCnwzBKwAX5BnaDI0OToxJY6_SAIz4_a9UUoTO_YzwvabUIcv8-hSJnk6op6VDwEGXe4nLOuikJrLtEKf8RZcgpRXWDG2-uJEKQ9lO1WUeqTnYvMIYvr0aUflbRMqfKDX78hJMosnApVtsRUaDwTMcKmGbjSEDKWjlUbH5UXf038rvJlnboQNPaZdPcemmu3H6ZGU7GP_qyo4PpiZKo8PxrKydgtVuEwGWGSmYG-6Dilstqj4XW7d_cMocUERM-RQKph6tudTzVDgfz5HAlwCdtyAVu3h_lxGiWotYZ0sNmNE-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c69zuMNWZBh_MkHuneIjrBbXaffmLkZGU_JSLMwkmG4EIC2GAnGj5gwrf_WAjXEdGT5hY7O48uDcv2z4yxSDJBub-9CzDa-CSff9ol49Jto0auBM1AgP1rx99nSTNbuGxkd811dSsfvmwd4sMNTb6gRstyOadkYNn0lP8tuOBZVViT3X7MsKENnfZhe5E_C7owEIwK8ZpJfEkawP4b6XoZeEC0E38h5yzWf3pkztq_qi4rJtkoDMgNoUaAlJSSfX7bs-CqxFOYdkHk05m7qEafa2tE-cRTW99W6czupKnJOIxHUb30oqFqwVZoTRJMt6xuLAN7ecwakdxYUMwvzYKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=j5YEbk23WMN2TQ4JMmumdwBBJ8GBthGlP5BK84ZA8bGHqUYCoY06qWQmnTpgddD5jlLHTgll94xqxsqOQDktfL1J8VCE9yXHAUVSs_cLhZKM6kvPdnwiSN6DwXXoHVfXywOIrzXegRdNGKz_1EWECmHCvuf_GzjdkVsRhPn2PaSo_4CzntLw7Vr9ALuD1TqRrTcyP0a2y5AcOMkxxqnYYKN4OIDKaXyLhfrmR1IjI45glKquEVRmj8HOwJ_Toj9pernZoXDcI6CqxdFMk71hy9ktq7RAGFWf4MI30Y3nfFO5rrvhHSIqRUapwhyQurMxyzfcQsIw4-8984iOvJePjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=j5YEbk23WMN2TQ4JMmumdwBBJ8GBthGlP5BK84ZA8bGHqUYCoY06qWQmnTpgddD5jlLHTgll94xqxsqOQDktfL1J8VCE9yXHAUVSs_cLhZKM6kvPdnwiSN6DwXXoHVfXywOIrzXegRdNGKz_1EWECmHCvuf_GzjdkVsRhPn2PaSo_4CzntLw7Vr9ALuD1TqRrTcyP0a2y5AcOMkxxqnYYKN4OIDKaXyLhfrmR1IjI45glKquEVRmj8HOwJ_Toj9pernZoXDcI6CqxdFMk71hy9ktq7RAGFWf4MI30Y3nfFO5rrvhHSIqRUapwhyQurMxyzfcQsIw4-8984iOvJePjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lfL395i6BC6rt5CeAxnN0EqePraLmPS-N5RohIXyvf-twkbm9h5gK5pFY3_okwIlBZgDFXUULdCFQSCxwHW9kLDL505REPJ9_gQEkE-dXWqDXhoZq_2ETUtIDFukLcL82ef50nqChfNCpCpwtPK3KHlgKP-hxMizr-BfllY-MMhY932Pw7cCoEMAVp1j6IvwBAFkBbgL45KsKh7asMzTE_YylZ-8H3VBSUvE0KpjmrOWd0l9_uQ9sDOsTt8BbBrZMy184mX84A06S2iqMNFi7GMMkseEwyu251Ug_VREpfROzhLtQflfFAhZbOV-xQ0iVc1wuWwNf-WGooOyH5afsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxrhSExfqtbvACCbv9M2mygeuUoisjg4J74wAJpHeKwyPuixFlq8D0aQGDpUP0yMBmLF3YTcTsqGkkRAza45fzzgADLrJAXcB5rxeN5rDqf1WIuEuu11uqeQO_MNzN9Nv1lbAPz_Qdu7w47-Zx3VHCgZ1ioKWgpAZHTZrrLjVY5X_t0D0ASAYtI-VIQqisxUK7CNma4JSdjWYAat958Yck9z56-aSegP9ztYgGJeuVM06Kgxj6r31ZJquq43k33ZNCBDQ03OERKi0GIK4a74X_e_CNOfqhN6F5GBWY49kvN3HPDBnJ5QEh9BptlHP5nfjSJ6_6YEEd8A0ZRqwCp13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=NPzVgVgiFeTpZHzRcl-RXjj2Ia3bXTn9vjU9uTe1orST5cv9jXII8mgxekIicPablpNJBpuWSEl3AvV1YrGrEpN6q6zQVjxkZbFEdWDuey7bMD8YAs-E1P0CylWd5ERCBXJ9fRqZxdcL81FobLsjJTBho3OUAdVjeWmx2ngC7E5vwBVALcfHuwfmWhVOhaE3N1KNZwY5mTlzlJ15hQOo15M9p5OT4NuoNCdgCI4QTPQDRtPd1fb4Z5h1kO2rbI1mMio7PBMY8AGKep7pCp2yqlH55C_i12fgk6SiGuLiX08_7mFG8Mrlhfl9vHgO6yw09km6qxJSieYHTPzUDD-fNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=NPzVgVgiFeTpZHzRcl-RXjj2Ia3bXTn9vjU9uTe1orST5cv9jXII8mgxekIicPablpNJBpuWSEl3AvV1YrGrEpN6q6zQVjxkZbFEdWDuey7bMD8YAs-E1P0CylWd5ERCBXJ9fRqZxdcL81FobLsjJTBho3OUAdVjeWmx2ngC7E5vwBVALcfHuwfmWhVOhaE3N1KNZwY5mTlzlJ15hQOo15M9p5OT4NuoNCdgCI4QTPQDRtPd1fb4Z5h1kO2rbI1mMio7PBMY8AGKep7pCp2yqlH55C_i12fgk6SiGuLiX08_7mFG8Mrlhfl9vHgO6yw09km6qxJSieYHTPzUDD-fNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZomS17vYfETkAPvdsP5OuqlB_8SCnjbcvHjTWxzh8IrRnC_KVUBaqF1Gr8mXU7ECiv7kfYIZvmJND0YtAcFopj-22MD6eNMHTcdrb8dm2GSp8DvVn-x5bUeti__Os0oedE4mbbrCupv-GHbyoX1s2k1r4YohTpY3TPG3SwJ4PVZrik20vymocWehnJsluRoWxxtwyDub4wYcLoeFaKu2XdJgN84vPGNggaWxsAnibvS4ggWGoNg2GHWBfAhGdjmkJanecur7W4Tm7KzYoui_el0SLrEqHyiQ5eETV5DZzqwJM7hZYtCRPHy0wtL00Z_7hY5soY6ZA8z6urhGolVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyPQK3CZMF_XMrsg0Q7cMFNX-wi0BGvvPhLPHIa93ePDZiP5krX3j2bmEimqxjSMrDLW7us5XObOYKmal9qvgthz7lO-aN_y5EeF8ypBFKlT79AqdbAQ9OYbSSmXsQGgtUhUzWFJRd38q-AKPzi7HHyk-DAl33zJF_NjjBONCvZpyKHNJd7Ir1e08foKj-BrCBVUKiOfxAyE5vHZh5dj2SDjCAS61L6UvFBd__4ZNxb8IHtenN2bR-Lz5qefE0uaO9l1GxmbzSwSae_s2SzXhxiZ-pdppIJxAqwRcpHJJkN0ZnEYXpesSvl4EK3PEP9xZEVqd9anVXx90HJzwYPIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0mP59lzwG5c-OITHmiqNgRA8zAp2nFJaOGqnEynUL5wIKo0UjPrLqenLk93CX1p7ibo7Jqd--0Wnj-l0JYJapkB0OclhdBM6VkYbJ2svQu-ZzhndPMDo6Y337CQNhLJeAzuk6oN7Jba56Rf_SaOWPGJC5lJyJb9IXFSSY-J1F5CrZP1lui0Qm5AH2Y8lz0uERRInKJ9_zryE03iOmUi2EFi_Fl5xnBvY6jMUurypVfd85UNRpSgKD3KRPCVkLcybd8CngOztvhd1-uBr3uwPJE16q2g1Jv6z13SH1xiPTKiqT4o_Sr6Wk2Y8AgfrEZHQzio7DF8YtXYSJw34Rk19Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=Z0hdCajocyY0DOIvdiCXo3EDaEN-t-uD0bNM0YFMB-0MEgn3hEnIECsy5nFQhf_y0iMEZaFKxjQERkag3o4cdwvHaOwGY7U49Erpt6-6SV6vLu2pCVhbcmBKOzd-eXUUHMk0rKiGMnhn5bBIV3YoRlVX4mG6OE8GI9LwG0-brB7r-Y6IV3qrnOJFQN9fAwY00r1cHe7-XjiubX6pwDJeVJAUH2OcGwro860laXIlpLEt_WaX5uEn1akG1xQ8nbgrY-TFfCVIQphHzRK-UglW-XmIUbmCmSFfuRGEfTisuf2dMJAus0A9a1qzzkMiyoVLs7lTsmzbF6DbccMz4YeKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=Z0hdCajocyY0DOIvdiCXo3EDaEN-t-uD0bNM0YFMB-0MEgn3hEnIECsy5nFQhf_y0iMEZaFKxjQERkag3o4cdwvHaOwGY7U49Erpt6-6SV6vLu2pCVhbcmBKOzd-eXUUHMk0rKiGMnhn5bBIV3YoRlVX4mG6OE8GI9LwG0-brB7r-Y6IV3qrnOJFQN9fAwY00r1cHe7-XjiubX6pwDJeVJAUH2OcGwro860laXIlpLEt_WaX5uEn1akG1xQ8nbgrY-TFfCVIQphHzRK-UglW-XmIUbmCmSFfuRGEfTisuf2dMJAus0A9a1qzzkMiyoVLs7lTsmzbF6DbccMz4YeKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VLdpW-uf5f-xRLGA2trTmep6R6K_TTJl0Iay7xvsm_9mJyOnGWJ-euCSZbwu7RzXTtY1LuZqjbQSHcxfHTM_tpm0dpWjRtnwbBv56Y3H40Rhkx0piEMfuzSR-_-3Yz66gL6WZBU2a4NSHTMsTz9JT-to8-9-8V0DPE1O5pBuhDnoe7dr2ItNnUh8T5iIVuDcRJ_3szB33qf511GnkdUMtoOSl6Zhk4J_iSAxnjhKNyokL7HcZQusiswnIT7vCA4wQqpb8vsd3KKuKHMw6XgdePvJ6OPnZZD5uzSqSl1sHqjt0UOeIjJOGAmg7FztiEZuPIp1Brclx_qT8nqCid2OBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BZrtpJ0PmWe6Q3pvrznAnCbAQ1BebVxJR-acD3mbWxdDLp79wB8YffuxYvQOTRiwIka9q9FEbLQYJxleuDqo3fOQZOAav27j5y9KQiLWZkIzJPSw1iqw-k3-nfIQVQtk4oOBr0h-fvr1Eb7xg-OhkSNXdR8fEH7Wq6VOZFUy0epmkoRUgsjUQK01KKI3VxbMTktjwUp8nRKXwkl0DizH9XJVoqK3QoeNzHSzXuOkhWV1LL4_etJVqUbweZ3GL0VlTe__M2sAxsV8jxCk6QHPSnCzB5tvkGpvB3YIzKYpC6Vumw0omBzHJLyFLIMXHONgsRjiq0WeMk4yow5Amoj92A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MblkigY8ureGkGDYwb0FIxbrWlmmJKnUySiZDCjpcs_amrRF85oaC7x1F4MOCIs8bVe6gRHNrZ7P3_8pxX7QRMAUHeGZljq5-MRoEqp5qmhneChWN_qIAWt-eZDUk2V-op_yh1Nchltt9n9wx-7i2QKhHZIb5WvBQrbXvdvwqUbDyv0U_es-AW2Y94UHuTPoT7hOarca02HiojGsQWJUOKsZgTBAjBDbfUNUeprNFQl1iNH4U8Wp4NI9wMmGWARcPI8l8S-bWs9-b3PLc7TJCAWDCkg_DWcNaDR3w1KamX5QQfR6B7TkMKDaeGIaJIg_pHv28N1vB-5XaQ3ht23ZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQLe-LXmsI2O2XCOc9sgaPuJjzR60V_lR0jM9cbE_sR7HRmmHcbRWcXPDyuDYAaHGA3lehV6IjmcTiyNImt8O0C_dmesXVvHCqFL7d2hyIFnaWddgqkpHjcCLu_De_2Tm7CuG7vLmG1-vC9tANKduZ0fSd1EGl_v7zbZ0d_u3gWDqsl-NrsBdX6dftzBQImCgdvA2HQaSBJYrKwaImNXXl_D6azNd3tgh31OwAAAl-phPX2Ogh4qByByb1y2rOkuvWO0n57RFUhFPkBEUdet7kZ4UE7EY07U5O1EgxRBGrcnAXWBMNeKPNWdEpcBaZNuhpWXyQnq-IXGL4Sk7p_3hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fenoI8HYT7MkkwQSN4PhntxciodwbQGH7ocNLXZlCmna_2kPD0pBfDKOWK3HT5Mrzd3_QKPE4bxGMM2P3E9q6vd7yMqqzmXhiKPxoo18UM39EOz1dJ0T9y8MVfSt2UPo1J73hbxdUck6F-vtBxKG5yVOIhpzuyns_YU3ulHDrUkQ5R9xI1zl8x1dpXyQIzX9fpKGFm3tFoMrXmmg9Rt9HXFLNaEDlcAq0cgOSVwEwjts-u76ZGHNGw3AKDKhxYaz15FhYTouS3-MVmWzqPpPs-mqOMt_xjoLGF5kuAwtXk96h9a61xJ63k1OOo0T5hsfdg8LNkWezT04NZs3TAltmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHohZ5BoTmcY_Uj8tIjX_JG1AR4shidSoq2ABQ7KO5YWpwyin5fHWrRxtulCOGFInyqrPQnJ9XB1XSmffmx2p62qzQo6d4mcXYwPa9qjeYb54irQZLlirakDB-ZbrLUla6aU4YuweXQ6ujdM7zXA9CCNdMYiMKqhMjWIhZetitliRRsjNGrJfJWNBbu8bddaCADu9siJ6BiG76DhqM-6ygS96DA7TqDpMwhJFHcyMPtifsjyu02nFr8yNsczZ-Glhb2mVHMTvZwzmyDovBXUNVYYfs3BfpCqOHQKtQJtuAoZLRyaq8_oTGOz01HL0Y3VP9iFLV4J0fXQ2UMLUpAKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=aDBEc5Ug_STXdvo5rkKZ0A7kwyBo71BH-q024zH6q-WFx72luWzTkRX7hNubsfiiAxe4svADQPSgVJQNua3UPqpO_c2KETc4k9QY9Q5vZrBNHlYJM0uCkwuNSOOD_HYbMfsI6sG_o2olVNYOBFDvTGtAgMN6wWGZx12iear1FJPySEdopcLr34UwXcYrEZqnH3ObC4x0qmHuKechERWAY_YTE-IYSDhgeDfJJSX1vdPEDBAKmB01tuSZVfOJk9ZA2hzzlZni6Zgkgml7peyyhW5bmfZyHKeDqTGDQ8C0aKqKNa3yKyf73t4lbaoyezM2Sg3Q9s5SQ76EHJwDi38-MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=aDBEc5Ug_STXdvo5rkKZ0A7kwyBo71BH-q024zH6q-WFx72luWzTkRX7hNubsfiiAxe4svADQPSgVJQNua3UPqpO_c2KETc4k9QY9Q5vZrBNHlYJM0uCkwuNSOOD_HYbMfsI6sG_o2olVNYOBFDvTGtAgMN6wWGZx12iear1FJPySEdopcLr34UwXcYrEZqnH3ObC4x0qmHuKechERWAY_YTE-IYSDhgeDfJJSX1vdPEDBAKmB01tuSZVfOJk9ZA2hzzlZni6Zgkgml7peyyhW5bmfZyHKeDqTGDQ8C0aKqKNa3yKyf73t4lbaoyezM2Sg3Q9s5SQ76EHJwDi38-MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0RUz0LG9qeVoRE9yCWUOdp9baSRa0U8J8wGqiZTYcZibDUSG7s95npxWEzMRWEizELwZ89_rOET8QOwNbpbLlGebaN3ZGbeciypna2nO61OcX8GlhcdJ55GvBmSkMGijM2BPM2ChYyGXPT4mTO6cTA53CdztzU4F5kM5qMuSo5FU48eHPARg_YRMzKjfoNV0VRZALMASWZ-AhnsozqqdjXM8jVlpKS1b-2YAzKkdAO41A6X-SVYZ8BwQf4ZiPq_iUQ-s3pRMwzJwm6dJ2HHCRrIb-dN02xB3G31feJZxn0asiVhE2EJUxF6p7IzOPNLyryaMel3aY3rxN6ZvNTbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMeCPaq-zBVy8elyjQnhCQlo_CRCULlAphBjZz6zbGxJYNU_yVihzYgybhcMCnfL4G8XWRgX0_lphgBJQdi3fnXralkgCRKtmL1d88Eu1MP4yXUCF3JJso0sdMoWdrZ_BWGkcoIMpBvbvhAP45N_HLOIQakGZjtqO_Md0jBeuyEd5I_hA-KUjtMJBXPzyL9a9XbdCtPTeT_FJF6Cbs9QkPV6VBed9Xsxal_b-Flo7iddD8h-HoLY-hKj0_LHZ9iaOa7HaPLXQkR3j9KlmKvMP013KFg3jAoLAYaDNOZT3rS0HQRwvW8yCDB4VpqIqGxYvWf7810ejDjKwfe7pgrNrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHHnvI-emd9Kje92LvmdtGLOr090jv906AdQTUJ2VSagL1Sh_hCHxmSDKEyWrrcAb9xqcoI3KHvmjMNVCIbPzuqOxuoW7I1L4aU5yHMvGhQIUe6PhqC2yXBKonh63sDmOtWdGxR2kLwE_mVnD6oQ5tAKmDu63q8CTmdPPz2VtuPRY_syODXCjt7bbUDPmxd1gEo56mMV931zGDlwEOxmb-4nWjERjSCOfS9uYBFAPaa8P--cdqmVdZESHukCmNrhzD20JpPjGQksTOVz_j1f3JteUHAwCG0MXJxZXjb7bDvs81rquecNjRasXezHzFOIh0nQf-xtT_UGuiyuXiXTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=ec1XGcJin7tVmyAwBRTRivizgrh6F9VDSNBrNP0n1ydH8jKhVgaWNKXK4Pt5SkkM5cfOTur6MExuzGpGBUGNqRqxljsvUIHRTiooaWbOd8nElQjLAQS_MZgDw0RD8e7Cxo_-4DNFESdBLGJBzvdRlhZqKG3Olb0Cx427Xww-TcqjovTglLOpOXWasRCoZtbSw9fBlYSxfNXschRfMzzgEHCtAq7JHHCY1ulS1ALuTM2qyRFPExU-qN82fh9x_pjOM1FgYfFNpZFMEwZJKirihd06ip-36Ub6X2IJr5ZsW3OVaVlHqQwl7DtCRiNUq_ojGiWpbtMmITbDGDpndxRwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=ec1XGcJin7tVmyAwBRTRivizgrh6F9VDSNBrNP0n1ydH8jKhVgaWNKXK4Pt5SkkM5cfOTur6MExuzGpGBUGNqRqxljsvUIHRTiooaWbOd8nElQjLAQS_MZgDw0RD8e7Cxo_-4DNFESdBLGJBzvdRlhZqKG3Olb0Cx427Xww-TcqjovTglLOpOXWasRCoZtbSw9fBlYSxfNXschRfMzzgEHCtAq7JHHCY1ulS1ALuTM2qyRFPExU-qN82fh9x_pjOM1FgYfFNpZFMEwZJKirihd06ip-36Ub6X2IJr5ZsW3OVaVlHqQwl7DtCRiNUq_ojGiWpbtMmITbDGDpndxRwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=SZQFgokFk8qlIv1-cyT3oVj5VMxEHt2pkgfysw-TIAAv632FcRkVoAYuqTO5w4JCQgGAtB2RFPRPNxD2tlT5-T5E-70MwIaSfZ1Vs7ie1eDzWVek_3PjwIYWCrQCNDUepSRxeb3QqGbDPNMADmFzWNllTZrk4ZwKcBUhO-xpNWDGtdmCWJjqh6SpsNvhkVU9wgh6QHXvgDDyLBiqAnjcZ1QqNGSs1Q5ZQtha311erKEKhp_wmWRcnf_j4nNINgaq3SZvA2gVbDUIaI6siWBV72VL5qY7oVWCS6JYQptzy2hhng0GzC-J6H0HE8wPGWwIY5gOjN1AS5Ble75_5SIYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=SZQFgokFk8qlIv1-cyT3oVj5VMxEHt2pkgfysw-TIAAv632FcRkVoAYuqTO5w4JCQgGAtB2RFPRPNxD2tlT5-T5E-70MwIaSfZ1Vs7ie1eDzWVek_3PjwIYWCrQCNDUepSRxeb3QqGbDPNMADmFzWNllTZrk4ZwKcBUhO-xpNWDGtdmCWJjqh6SpsNvhkVU9wgh6QHXvgDDyLBiqAnjcZ1QqNGSs1Q5ZQtha311erKEKhp_wmWRcnf_j4nNINgaq3SZvA2gVbDUIaI6siWBV72VL5qY7oVWCS6JYQptzy2hhng0GzC-J6H0HE8wPGWwIY5gOjN1AS5Ble75_5SIYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj0LvADG1Koq6SeRfXqjDhRu5TrJ6V3RM3Z090v3VGmN71_pxw-kQyrGc44NMssVwQIL8ThJilq8kk6how-CLfz7K9SV3HKWEnv9EHWnSLACNmwfuA9cFwcGbqlKKt42EPPeAerZJvcVNMPk9DBNc8_zmpCUxzn7NR6GZqXyu3723itU31m7ePIfYEKyvowFzinix5RweAMgerfISiT-7m3ZIZWdjZE9MbN7VUwHqqUPqfk1CdxvddJxTunjePLtgWoGFC_HSTZRqzoNEwrpK-NhzbJOeI0-Iw_YIYiZqz7lo8ZAOe_QvlzkMm7dkgYYyGrhpSnQzmF3H3EIFmuviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Z5YhlXwKMtceg02uogCU6kbKKXAK501T2BT_3LKC_0hZCrw7S0ebvBdiin6G90viVL2d44iI0UpNLi6XJ6QUJZxE6u9rREFKi6tIWMAXRhQttcEBygVX7o3C-w_j6i32oU4un8eU5ol1L9d6Y6SP1YH_bqs_f80nQ--Gxosbg35TmmxYPylodJTRx6153fnGPt_6ko3q-uZ3i177j2wsjErfaNpUV_7d9LCkBXi0LzwFrn4hxxtMqd4t7g0lEze_upwGpjcX869HPb5AkAdbhiNK5JH1iBcG_PeSxM0RnLMtU54uOp191R0e7pG6zMqf_eMq6BPX48zxXlFqkeD8cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2YlXYUTPeHGkMDB7fpKBw9pTiDJHx8IF_nuqhmXPq4myHISsNf5fk1eVB3OIKLjB4A2vxRZS8sx0Vh3a3A4uidiNHxAtpCMnLApkw3BetcGKL8DR1hCG9Hm8my7xwWDNiTPnc7VAElkXaiXZ6240N-XpYLZ8DZTWGKiFTRkOhyxu5Vx9BwTYL_ZeQF18uLhLjkFjjEMuYcLMTUA1oyzJmyAMpWZXD3c3Y8OeoIbQ_8q-5gzQEazZsaFiDLtp7ft6cbwNz3SSgaB6busTjyV_oiWqY8tSDc1gpn2Ojl444CX_8APh-9q9wNJ0D9CmL1Nkj2iQUyhHyurIgKCPVoXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYHKbCHvRv8TZPZ0FkGR805D3gCb2QU-AEgK-308GNdi87lJgfuTz4HfpxG_D_1TIkQwxBMg1xtuGX_XWOxeQtgkE2xqA31duvDLd__mAI63aHR19mosxyh7HrHUb3Pedh1Lym55zM7HpptwfMs1CARexDPXHfazvF0fYQFPVy66NVS_Ok8iZJs548WltOcl7iKs01k4A-os-7jo2qNWrFv4VKHpU7eCkSBQhU1te2JWaQC6x2fpbV4XDXyHuh5t3SRoOwFQADujtMvExKzpI2HH6tsAd8DmFcsSKG6muGpuLhwHnDm2zBx2PGU4qUMidWdMuHeYnBmcahpAPcHuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7dzAfMWwqN5W0EF1FIDwD6mQVjxMKoybSr-ibDZWLFj6B8mPDhjFQN0V9gncvkUfpPR1MFM5Kcs15DcyFAF4z5HTWC2LZ1GDPSp_WmKufg1GXsqQ2yw_N8LgHrTtvWmTw3y4WnyB8ninfrEPCzrcUACRDUnknGKxwvl1mItc59aWzorAB_ToVor8IegHaWGh1nJ-L5TXSqWVPndJ24jFN4OK-BogZ1g0nrxdL3nWZAaZ8io293mAPoXZ-6YQ5IJa2dQ_Eu29l1TjV-8PDdBiDTPDeMAT_4xvrelEHiRb2kLyjdQZS21n1C_i9EiTL1Q68yL-orp9IjsnRA3Uvi-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=fSHKoIqrpxuGRf6VOLRfqT3-Lf5lIbbYyTXewY9QB0ci5bOa9AABzUPIAKCVPYrOOJTCtalY4YgoSBWsvIOeVdhwOxk_PolB2KDHwv5K2MX_4W4U6mMjPI2biAl99RRdHtcBXYRV3wRprVJMw5LgxcpKEUNTd4KenWBU0WROr3ZB0D08RWVTv7CCw39a0qHe1EcteS33KM8hd0OMPegp8n4ny-LpIF_5Nd3iOXJw-EKoZIG36XwNdmsbgJ2ohmGypCVXD9m97FvhCt4W0fcaNyKu2OzZxoJ-Mp_KKRSkyT5YzU3ptYxKM0d9cqNso3QlyayFpnCzLiwCqhpFQSNQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=fSHKoIqrpxuGRf6VOLRfqT3-Lf5lIbbYyTXewY9QB0ci5bOa9AABzUPIAKCVPYrOOJTCtalY4YgoSBWsvIOeVdhwOxk_PolB2KDHwv5K2MX_4W4U6mMjPI2biAl99RRdHtcBXYRV3wRprVJMw5LgxcpKEUNTd4KenWBU0WROr3ZB0D08RWVTv7CCw39a0qHe1EcteS33KM8hd0OMPegp8n4ny-LpIF_5Nd3iOXJw-EKoZIG36XwNdmsbgJ2ohmGypCVXD9m97FvhCt4W0fcaNyKu2OzZxoJ-Mp_KKRSkyT5YzU3ptYxKM0d9cqNso3QlyayFpnCzLiwCqhpFQSNQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=dkR5rVsnEtqP1fO1X_-v1hy03uSi5KrHIXEsVR9_S-SsCnWYVOGYQ9B5_A9adMwJZ1MVC6Yo-6CKtkDQ_ildcAslxfdQiz1gOqaaupJu2hOZFuFv7HhBliH699_XbnCA2GC_DHEE_m5n-KJIeIuvjC7SNYEH4-XlKIQdi5nTBaY2YDsp_4rC1xxnnl5yLt9M9x-ru53Znx9KufBEr8nl_O0mTYwYgXMaHgss_mipglnKzgnDRPNbxguCrTM8v1aM7tM9W_dbwq0NOZf9kj1qjfrGVxpiAHHpK54dxcssvOegnCJuQ5-5y_IWXOVHeY5czjF5EwZuVWRaqj_yTLGvEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=dkR5rVsnEtqP1fO1X_-v1hy03uSi5KrHIXEsVR9_S-SsCnWYVOGYQ9B5_A9adMwJZ1MVC6Yo-6CKtkDQ_ildcAslxfdQiz1gOqaaupJu2hOZFuFv7HhBliH699_XbnCA2GC_DHEE_m5n-KJIeIuvjC7SNYEH4-XlKIQdi5nTBaY2YDsp_4rC1xxnnl5yLt9M9x-ru53Znx9KufBEr8nl_O0mTYwYgXMaHgss_mipglnKzgnDRPNbxguCrTM8v1aM7tM9W_dbwq0NOZf9kj1qjfrGVxpiAHHpK54dxcssvOegnCJuQ5-5y_IWXOVHeY5czjF5EwZuVWRaqj_yTLGvEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3vE_8pDfGwmEs_CKwba6T_zx5u0KESHignmat7TqCAs_IdD3tizWotB9zQNusBz_KmWq4ies1mnyV3cRZbF3VLyKyoJk_Lm9V390apq0dDogYaNFvTvG4gxlhc0R3VPlYa600nCn-L-UxaFxYf4ZFHYrjCcQsS70irW4eGFcDbXRN7OWiSLlayIiM_NPC8WPBFTvPgmXSsEOjHScWYb3HqpYN95kAdYDt8eKtTXQ_vQ8nu-vGaHcM0Jpmx2tr1ryEMseNUOpQZo3Y7ODYcU6mJ-IRugHxoA7pqB-nCtoR5LpB4YiJCWe3NBCmL2eCiBXPEID1d6KTueOvJGQTi7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZC-vxUb8d457l06P_bRoluB2747cN8tHCTPEV31V_g8Hv9-pY3hXHc7pqD6sisz3h6p2bwMIZqs7q37GbhJ5NDrZs4pzqhh3zGToUyn27ZapPO7Tes0BMWJaDB3Yq5BC5YbrCi_6s6rCO9OEZ0cPmRmVT7bgsObdF0L4r7Rec34g4x7_gyWWhUoBFWCDCIfZUWFoky3KLNmKiuK82OF-DRw0q4JsSfrf7JUvTKMHpB0-fQ1yF2mbjRtKahVOc5EQqqGYJEe9KNtCanuEihWBVAnbyKr73w9S97JIEWRIWr4Tt3MbcOKO8_NYIliULbNQmaQEo6E13ms16-Y-q56oHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izEid4BQyGNdxl54T6b-v3L-L7q_e_KyrW3gRa1_VPs2U4FIdASTIPS8CxTL-J5S0XppZJC2CaMEnk8u5qu_yvc9oqJfL8XgdD17Gasm3_ytvs7uMHi6CpmH4l3aAQrbZ-_yaYh9gR094Qh7V2ILYKdCjTHUlKmmGpwdTnR_Jq-lRKyohC5GJo3k-cfIfQY9BDrA3tbDZs5aHPCzXOZ5XK--LfM4KBJGtpCNxy6Wfa1q1GqIF16KMpLXPeRz9i-4wgwH-KtyUksJJDBlfgIESVqz8SnW_ubEgFJO60TJUais2ZGLqYK6gCGN5bxhyqAEBmAKnMlc13qVwddpgNZzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
