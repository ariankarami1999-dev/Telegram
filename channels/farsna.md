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
<img src="https://cdn4.telesco.pe/file/u41zx5H1e1syxXueR_Ee0hMXZz9GqG0-Gog22pIFIEgpNw5RcOgftO0lljIcyvMAcjmTUd5mjD1vtWA9W6jNgcASxm_9UFFoiugDlpWGZqTo7iv9prZdG0iFtiOvcEU8ZJUdwSd0Soipw3tpqx4VUaZuyzVNohozQ39USmy2w9g_rHmQygd5LqMjXb123Q7Kb--apRue9opI0jbY5_TNThFf1sl3kJ448idEPzaC8AfusLGfiPZsqLUm-nWjHAieJO337z-3VinIvP2yEFCieeILNjWLCVJ-s4VyQAVrc2QSiFg40JG6ZR1oAyg1_7LSXYQqsBX3f1QM_ayOogx6qQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
<hr>

<div class="tg-post" id="msg-459380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxgrK54jlUwDIX7JFx1sWSQ-dlEXGyvUb4FHgBOCrV0zfFRjqPMmqyOGie6vKuvHLd2n4TS_t-otWYBBHNl1qwqh67UA-UqKc_0vpeELWzf6tIuQ-Y5X3P0vocXmyZw14jqpiKg06eSCt-i8pSh4IuwE3xvHbtRBif7rOTBLayYJXMqww_kjbH_k7O9oZuJKlXcM491FuVxcI77Vnh_Ukj7ukmaZFqv9jqYab8I2elJv7JayNf7ZV4EnPg8swSMeFzz6r2DB9CYBQK5WjCawvJkU3u1blJ5MFCXN0BQUDrWjTyUBJluLaO8LYy7UPcZb9_QBVryTeegIZIj4GIgbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش هنگام عبور از تنگۀ هرمز هدف اصابت ۳ پرتابه قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 349 · <a href="https://t.me/farsna/459380" target="_blank">📅 09:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXCdeDvx8KY2QjX7NdTkORvvn8tz8C-TiMrI4O3E7Gt0bYqZiSO46dbgL6e93j76x-6JjNryBlZJitL1GLTbyRJq54HiTFgxhBXZu7Zyke7KzMtdb3_EGX75EahP3Ouk1KgbcGP3CWLsHOrPIDsQtl8XN24YokBktFR2bOLdcPCPb5YUYvzp_TgBjhDhiB6q8W6W7mTapCfTol8rcIC9q_kJmuT3TqA798N59qa-coY1T3lSVgOh2EO8NnwSttzoKQV1w9vI-BPUXXhhNrVaQGeIWtj-O7zskmEFdhHCHt5DSvT5JmDlwFA5JX2CF0FHOZNoXmK8hjTt_rrVsWARhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس بانک مرکزی: ارز داریم؛ به قدر کافی هم داریم
🔹
این ادعا که ایران وارد فروپاشی اقتصادی شده، به‌طور قاطع درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و کشور علاوه بر آن، از ذخایر داخلی نیز برخوردار است.
🔹
منابعی داریم که به دلایل…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/farsna/459379" target="_blank">📅 09:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس بانک مرکزی: احتمال وقوع ابرتورم را ضعیف می‌دانم
🔹
حجم تحریم‌ها و محاصره اقتصادی اعمال‌شده علیه ایران بسیار گسترده است اما تأمین ارز مورد نیاز کشور، نیازهای معیشتی مردم و نیازهای اولیه کارخانه‌ها و واحدهای تولیدی قابل نادیده‌گرفتن نبود.
🔹
با وجود اینکه…</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/459378" target="_blank">📅 09:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس بانک مرکزی: احتمال وقوع ابرتورم را ضعیف می‌دانم
🔹
حجم تحریم‌ها و محاصره اقتصادی اعمال‌شده علیه ایران بسیار گسترده است اما تأمین ارز مورد نیاز کشور، نیازهای معیشتی مردم و نیازهای اولیه کارخانه‌ها و واحدهای تولیدی قابل نادیده‌گرفتن نبود.
🔹
با وجود اینکه مردم از تورم رنج می‌برند و سنگینی آن را در زندگی خود احساس می‌کنند، هنوز وارد ابرتورم نشده‌ایم و احتمال وقوع آن را نیز ضعیف می‌دانم.
🔹
اقدامات پولی و احتیاطی بانک مرکزی باعث شد شتاب تورم کنترل شود.
🔹
در شرایط فعلی، مهم‌ترین وظیفه بانک مرکزی کنترل شتاب تورم و جلوگیری از ورود اقتصاد به مسیر ابرتورم است.
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/459377" target="_blank">📅 09:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">ایران و آمریکا در جنگ‌اند، در ورزشگاه نجنگید
🔹
«پرتاب سنگ، بطری، فحاشی، تهدید به قتل». این‌ها شرح یک دعوای خیابانی نیست، وضعیتی است که در هفتۀ چهارم لیگ برتر در دو ورزشگاه ایران رخ داد.
استقلال در این هفته میهمان فولاد خوزستان در اهواز بود. استقلال که سال‌ها اهواز را خانه دوم خود می‌دانست، حالا هر بار که این تیم به این شهر می‌رود با استقبال نه‌چندان گرم میزبان روبه‌رو می‌شود.
🔹
روز قبل از بازی یک هوادار خانم استقلال از تهدید لیدر فولاد مبنی بر جهنم کردن ورزشگاه برای آبی‌پوشان گفت و عنوان کرد که به همین خاطر به برای دیدن بازی به استادیوم نمی‌رود.
🔹
در درون ورزشگاه هم پرتاب اشیا و ترقه در طول ۹۰ دقیقه ادامه داشت و حتی برای دقایقی منجر به وقفه در بازی شد. در سوی دیگر برخی هواداران استقلال نیز در مواجهه با رامین رضاییان، اقدام به پرتاب سنگ و بطری کردند.
🔹
در یزد نوع دیگری از خشونت در جریان بود. خشونت لفظی. دو سال پیش در بازی چادرملوی اردکان و تراکتور، برخی هواداران حاضر در ورزشگاه علیه بیرانوند شعارهایی دادند.
🔹
در همان بازی شجاع خلیل‌زاده، کاپیتان تیم هم حرکتی منشوری کرد. اقدامی که بعدها با درد کشاله توجیه شد. در بازی این هفته نیز تقریباً همان اتفاقات تکرار شد. فحاشی مداوم به تیم میهمان. این‌ها تنها دو نمونه‌اند. در سایر ورزشگاه‌های ایران اوضاع دستکمی ندارد. خشونت‌ورزشی جدا از وضعیت کلی جامعه قابل‌تحلیل نیست.
🔹
بااین‌حال، همه چیز را نباید با جنگ، وضع اجتماعی و اقتصادی نامناسب توجیه کرد. نبود قانون مناسب و البته مجری قانون باعث شده تا هرازگاهی زشتی روی سکو بیشتر از نمایش درون میدان نمود پیدا کند.
🔹
در انگلیس و پس از فاجعه هیزلبورو در سال ۱۹۸۹ که منجر به مرگ ۹۷ تماشاگر فوتبال شد، به‌سرعت قوانینی تازه وضع شد. قانون الزام به نشستن روی صندلی از همان زمان باب شد.
🔹
پیش‌تر اغلب تماشاگران ایستاده بازی‌ها را دنبال می‌کردند، حالا جز در بخشی مشخص، کسی اجازه ایستادن طولانی را ندارد. بازرسی دقیق برای جلوگیری از ورود اشیای ممنوعه، نشستن روی صندلی شماره‌دار، نصب دوربین‌های امنیتی و از همه مهم‌تر اجرای درست و کامل این قوانین باعث شد که انگلیس حالا کمترین میزان درگیری را حین بازی داشته باشد.
🔹
وعده اقدامی شبیه این‌ها در فوتبال ایران هر سال داده می‌شود اما هنگام اجرا با بهانه‌های مختلف فراموش می‌شود. حتی آرای کمیته انضباطی نیز آن‌چنان‌که باید پیشگیرانه نیست و اغلب به جرائم مالی ختم می‌شود.
🔹
همین باعث می‌شود که مسئله کشاله شجاع برای هوادار چادرملو حل نشود.  به همین دلیل هوادار تصمیم می‌گیرد حالا که قانون کارش را انجام نداده، خودش حکم را از روی سکوها اجرا کند.
🖼
حمیدرضا صدر، ورزشی‌نویس فقید در تعریفش از فوتبال یک‌بار گفت: «فوتبال ورای نتیجه، ارتباطی است که آدم‌ها به بهانه پیروزی و شکست در کنار هم قرار می‌گیرند». حرف او اما این روزها در میان خشم و سنگ و فحاشی گم شده. این پیامی برای هواداران هم است که فوتبال را با میدان جنگ و حریف را با دشمن اشتباه نگیرند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/farsna/459376" target="_blank">📅 08:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9-Z2YvEKbwnTgLopcfk8sJgAfFkHAtM1mZ2Au9xPaW6Kmrs9FHRoMcZ6QMzxaxugLadmx7hG6uxGzQdzZqBFM1fIjEDmSiUZAJ6btnonbKsjV9DJu252NraUvqM4MzIbs0jOs95D2svpjgOK0fB037KUF1vWqPdo0ysJO7ykIBihiSXD4iOmvEiVPNaXZNuFLKFz2C0pEv6Ya3Hzv8XvH7SBStw4oXtIz6EAQaEF3bFyxeq0hKtVeOBk9l5OpWEVEHk1yXdWOt1AvAb7LoEy5MrPxgFYcZT9NsPlrjWbVMtAfv9lZeWhwcynie0FdJ7VbJD2MCAokTT-Lal4axRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: آمریکا و رژیم صهیونیستی در جنگ ۴۰ روزه ناگزیر به آتش‌بس و پایان جنگ شدند
🔹
تهاجماتی که در ۱۳ ژوئن ۲۰۲۵ و ۲۸ فوریه ۲۰۲۶ توسط آمریکا و رژیم صهیونیستی علیه ایران انجام شدند، تجاوزی آشکار علیه اصول بنیادین منشور ملل متحد و حقوق بین‌الملل، علیه اصل منع…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/459375" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z60n4YZGQWtarht0AnSyYZV3ZGoFfh6wY5ULlPW_BhoZmrF88QRokYfT3XbCqMv9fJagsebXdZKoiFMsKtxQqUfE6wNyRepMP8wp5ki-Y6K7ju0qcujNLpOJb1sjgVjgqMcCOklDoA1fGe2Dn06xze84tRDjWbiBJ4kTdhclU-zbHZ2OYf2IFk9zEKZlBpilmwqz7WVnsqu8wvMAFTzNNC2pGOkh2QWdlNrdEg4Vv9y8hsvwZXpFg559yKJMrQ0lLMSSlVNDyoFICzPCdO7-XFJ1UhTeJxl7vYg7OuW8ci-klq2VD2mPpTWetsNVOVZeiqt9TDb-WvOPdRETCp_aGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: امنیت منطقه در گرو مقابله با رویکردهای مبتنی بر زور است
🔹
رئیس‌جمهور در اجلاس سران سازمان همکاری‌ شانگهای: امنیت پایدار نه از طریق تقابل، بلکه از مسیر اعتماد متقابل، احترام به حاکمیت کشورها، عدم مداخله در امور داخلی و همکاری میان دولت‌ها حاصل می‌شود.…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/459374" target="_blank">📅 08:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRY4BtU29DwnbU4Rmvep-5HNDtOEH6_fFB_DFxe4b9w_9tcDxlmHY5abyJX4WVNZk8BKr_1eSDnIe5FbomnIkNDJK5ke6tor5OooRmmciqS3stu_q5OOE4BdKlivaY1Cobqx46AyTYiTnyaXUTWjgmfhA18aEN88ipTMUFgISN0WaN-CNeIc4UOx734AEIUbVhcOlQJ60OfgMmDMlh3s9CZmN1l1W1s-QPDP1JdEYszaum_6ulzuvBcZVkxAAP4JDismysNRfqLZL12XiHJyR8WWK4TFu0Pbe2Konsre-bMPNjU5p-_FKs604g3iuqj0LHR61ZKvwFoM7IgK4KBUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یادگاری سران کشورهای عضو سازمان همکاری شانگهای  @Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/459373" target="_blank">📅 08:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607c16eea6.mp4?token=C7b8vcaT68eCiOCIdIIeYIZ3HaXKwVLisg856ISRgrUAo26eWexau6vWZpKHsuUB-rQJx10pLvMNBx1pes36hcxXk-zOZINyGeiQsQfyMCdJDb5NhlNswD1U1kPyFF98EBJeBvwDeqHxLizgHRYL7lreLHCxWeHjTNv6Q5u2JM-UmIfcFr9ndglwoEIvK0uidfnC84wD4_hNhLuelQyH4Eri091FK4RVLuwR8oppOHsxLaxfsm6uNU2_kNDc982ka9_v4H8gnavoZG_aQvSP47O1ynCSoqkklQG5In9TDuOodTz1Xx-wu213ofaYPCuQMG41eyCjQbH6Mblu7hxgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607c16eea6.mp4?token=C7b8vcaT68eCiOCIdIIeYIZ3HaXKwVLisg856ISRgrUAo26eWexau6vWZpKHsuUB-rQJx10pLvMNBx1pes36hcxXk-zOZINyGeiQsQfyMCdJDb5NhlNswD1U1kPyFF98EBJeBvwDeqHxLizgHRYL7lreLHCxWeHjTNv6Q5u2JM-UmIfcFr9ndglwoEIvK0uidfnC84wD4_hNhLuelQyH4Eri091FK4RVLuwR8oppOHsxLaxfsm6uNU2_kNDc982ka9_v4H8gnavoZG_aQvSP47O1ynCSoqkklQG5In9TDuOodTz1Xx-wu213ofaYPCuQMG41eyCjQbH6Mblu7hxgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌ها در شمال کشور تا پایان هفته ادامه دارد
🔹
از روز جمعه مجددا دما در شمال کشور افزایش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/459372" target="_blank">📅 08:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش‌وپرورش: امکان ترمیم نمرهٔ امتحان نهایی در شهریور وجود ندارد
🔹
با وجود درخواست برخی از داوطلبان کنکور برای برگزاری امتحانات نهایی شهریور ۱۴۰۵ با هدف ترمیم نمره و ایجاد سابقهٔ تحصیلی، سخنگوی آموزش‌وپرورش می‌گوید: ترمیم نمره «خرداد به خرداد» انجام می‌شود و ایجاد فرصت مجدد خارج از زمان مقرر، نیازمند تصمیم و تغییر در ضوابط مربوط است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/459371" target="_blank">📅 08:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM-6rB12Xtcdmix4572os_D0oMpTkXi2d98equyFoyDV3z6-gxHsuSn4QeJSyA5gYKzWXxS67VmdCXbNuNh7DNF02JHtHAZHeLpuypTqyuPw6IbmkZHB5J2GW_vgY9LYnnVVodY8mRlQXAnNG7D3o4uORpqi28P2KU9V6CArafq79jo2GlVMu0CWRKOgiyMn0hOdZ07YZd_Pptr-jWgAejuQGHHCMTjxiNSCDFWBzxMR4-fV8F3SzqCzsE_bIK3rMomGe4i_vod8u64bNiYbhBjGe6Z7HZu0bLl7Kz7HJL1mbOxHP-DSnS15Hb7NTyofQmLZPdG2HKQRkSwcpuiMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان دقایقی پیش وارد محل برگزاری اجلاس سران شانگهای در بیشکک قرقیزستان شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/459370" target="_blank">📅 08:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYdvXE5O_yKgiyWkNg_56ck9dp5QJZX02KgZ6-3m1UCaj2UGxcGU5riHLUpIfgl-9714zlCm7y3E8D74PFVB1j2w5IFeHQJowISAz2RDp6diSePh8rOHN0F9_UMwvSbaG5dwkHxl0z9mfSMlpmH5RHby374rxr6k46og-ndcQGUpTmfFWdlVpYYW7pSny3g5pWcn4e6aeUvON5q8KRyEp6OSsv8sHu4ZpPKe5SmzzeL0OuS681Zh5CcAsrCpfc5DO7bHbn5-HCZzyT2d94x_3y1-fSK6Yneg70_1RfrSsmlOBvEBevBvT9lSOuOik4DtLwl3iOe3dS4qsHVJ4tLkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwqgWmQxRwspGKOSpODie2E3NU_tU_oMCo1noUt9O0elGKQUiwcEjCSTpNP1J-IqIMqEo1_Nr5DJljntE3hf7fSakVOdyd1KjrBsO6TPWgEh2mBNRmQNFeBDC-gAvq9w7__28Tu-99RGW4GmAq2xGdfg2IZpzT6IPxyxRFVOmYWywWhdIITntaA6hzoy5RzBI8kc6S6t9LLmMJzibO_f3eU8S1lrkRG65SakydvaWkxluB0wDJ-G6G1m-YGs-cRHOXBEmevRKTA8mSxY70i8qqM0wpqT6a_MfXKJlufF3Epul0jjdIRFzqVMPPpbuE1IBABvaW-OBnBfP1vCRw8j-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yr87cMCtR4bP1yOz75GK0xTwVcj7-sj3Xdxdmu7nO7b8K6c107duEmO8TVsZPAcCKyTiS437PfbhHUmyvKYH9oJZap3hso4dM6mbn0n7E-OHDJUd_yuBjglvLBKTVMOp9v8N--qwCsmwV60O0-jTdRU-URSZPEKeommbicmIawGimeQvC9rzB1dFOTlJjcR5kgbI2BBCnnvQi1VXX3eRSbjwM-NlMXLZ9NCUXJ770R3wj3OvUfioDKfzTiZKwxVQ5VLEFLc-Yv42YUdeh1r_IcsaJsMHsiJQ9Q_H86f6Crb46DaNGmPa4AHJX3C-Ys5jwb3aJ1T0wDjRKUB1E-Ep1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2J3Hvkj2YHAlJlwWt8KXdwDTwl77FZpo86dHMlKjpV_LlcKECTAj_d3yUeJHppur-7fmJEbJeKgQNjDSSosFg1y-CzZTygG_wANVuIVh1-lz8uBBiDp7OPF8f6SA6yAwfS9NM-4xkGQDOESImWJO7gZajhEMTpz179fTsbnXnMhKYZpHEI0c-5pH23Uhw4f5u876ANIEkmVEbnHqJCxu1Eb-Mfk6hu1Wwdsez4H2SePOgBxJHTkdJi9R10N44jNtPQn2BqDdWU6zA_9YDZiWyNf9_i8Z-PQOkYF11XKALxZlUsJB6bIQJCBd_s7RTVkBkRkfZ5Eubtr3G7R3aDbpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار وزرای امور خارجۀ ایران و چین در بیشکک @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/459366" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30559817.mp4?token=XtAOpXB8Nd59sHTKR1xKjH5WR2-8FOC72ZOCU-sG59fkJO8FQBMmfwisxbjVBX1_MyjajV_p0IjoQc6iUEMgxXE2Ybjsxze4g0i01vNzgsVxnepjjApfexQYPnfnLl-tUXBAcnhcp7nNg3tLeI2er-kxh7un1jOOoxWx6D1IgJ3LdpgCpMQwOTkTwe97iuGI_0F6xZ9X5V8VEgdbowznSZE3Q_nWQBs7Tt4VHAyrPP2vHTMTJ8u7DWUK_WWWjRNsSwpMEq6iKfCyH9Ya1pP8rBTgBgV7MjoNGxgG5hxlfEKUEVHPFFluIolSCGKXfRUI64xerXon0S7f1h4ogJUV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30559817.mp4?token=XtAOpXB8Nd59sHTKR1xKjH5WR2-8FOC72ZOCU-sG59fkJO8FQBMmfwisxbjVBX1_MyjajV_p0IjoQc6iUEMgxXE2Ybjsxze4g0i01vNzgsVxnepjjApfexQYPnfnLl-tUXBAcnhcp7nNg3tLeI2er-kxh7un1jOOoxWx6D1IgJ3LdpgCpMQwOTkTwe97iuGI_0F6xZ9X5V8VEgdbowznSZE3Q_nWQBs7Tt4VHAyrPP2vHTMTJ8u7DWUK_WWWjRNsSwpMEq6iKfCyH9Ya1pP8rBTgBgV7MjoNGxgG5hxlfEKUEVHPFFluIolSCGKXfRUI64xerXon0S7f1h4ogJUV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
عکس یادگاری روسای‌جمهور ایران و قرقیزستان در اجلاس سازمان همکاری‌های شانگهای @Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/459365" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c65-PAri1QbW-D8J8iLx3U3T80zwPtRRJXRbPHuDfXkL9uxxM5noT2rHlkAuQiayDyHJcYV2BSLC2Ra8QMGYuHJ4B52vTE8Mv3m8E7p8fzRGvysNDLqtL3jMc3WtRPVcH2Ly-Ar0iken2HYxzXNT1giQmD40lat14nVAq17dMPnwNg7p2iNJUElCp5jzMPcwTFutlrbA2RYrQVXeDXDE_xSAAFZJ4nN5Hd3EZvKasyC7B53tfIeX5MlaJK-lsRpZ6uppipRKTjeXvcNNT_UBEQoAXb4z90gJQJ5eV1tNPfOpgWHe4YHneba1m6eDZbhSYbduQhm-Fk0WdcY0wvAXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار وزرای امور خارجۀ ایران و پاکستان در بیشکک @Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/459364" target="_blank">📅 07:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcyjDeGB6Uy_7BQmkUUaPhtcXuTkf_PHZ5LV1Ffy0SC28Z0qZCkFnU6yfLRblrKaFSDajIwMilw5Ul-A-S-EOmHvz1ckmxVgeFW2DT9X4PbVJv1VjsosygIDCVzUeUKQ5z5-Dg5jpvB2iN9CClOszfGZVuTFlXrjydDKjDsNBrueWfL9VjQ7okrN6RLfJPT661R7mfiNkGlNDrbUFvkpgsoL8S8HnQ5EIRR8Bnsz4_wTZizQHbz_N1QmO4DF8R5o530iy_d7jkdpzKdGWvaQmDSJctrgdRNINRTvsG_3z5IEU8LW5TaLu0S8PXpU8AcJ53g0Dtjt3ctQg_QBzzW16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ جدید پرسپولیس برای «پرسپولیس ب» کلید خورد
🔹
یکی از گزینه‌های مدنظر مدیران پرسپولیس برای راه‌اندازی تیم «پرسپولیس ب»، خرید سهام فولاد ب بود؛ تیمی که به تازگی جواز حضور در لیگ دستۀ اول را به دست آورده است. اما مذاکرات در نهایت به نتیجه نرسید و مدیرعامل باشگاه فولاد، اعلام کرد که فولاد ب در فصل جدید لیگ یک حضور خواهد داشت.
🔹
پس از منتفی شدن این تیم، پرسپولیسی‌ها همچنان مذاکرات خود برای خرید یک سهمیه در لیگ دستۀ اول ادامه داده‌اند و درحال‌حاضر باشگاه‌های «بعثت کرمانشاه» و «فرد البرز» به‌عنوان دو گزینۀ جدی در این زمینه مطرح هستند.
🔹
البته هنوز توافق نهایی میان پرسپولیس و هیچ‌یک از این دو باشگاه حاصل نشده و مذاکرات ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/459363" target="_blank">📅 07:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgAgPGCeHHHBddzZDY-SPlNUiIjA_9rPBegIIubkr0_CviAlwtT2UIu1BKB2KOWeKEzLDGWzoayXtPS8GlBgGFEvKDPmEgoYFjPdQQ8o9hblMUosiQ2sIYu8ovKWlFE9t7QyJtVmuHToaZwSExKLmRkuYkrKF_LDv55S-iJtdPrlA6hZVhrUiw8WVbdljmknpLdq8QTE9io5EnchVOYVOYUd_LhRK_UoK4ooxPKfkFCBVsoYmpINTMRR2bHOEDc-1w_GNr7Ii0j63f197wRxQ6jiGWLqiYHGIAXS6UUb0mLzEn6-EB1Rbtgo-UCYaZNSwlOyzeiBs6opXYUaB0G9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار وزرای امور خارجۀ ایران و پاکستان در بیشکک
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/459362" target="_blank">📅 07:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvIeg6MCFGCj8FRx1PBcugYjh8hzXQmTHXg2eRzk28KNdTbBHk8RCJY30rKmCYrcgjT73ZGj-4V6Zua5Kmz1Izt6lSC_IL9HIj7i0iChsQ6ukHITCY3AQORNI-SzM2TSaQroNzaJ7QMFzQKyDZWug5vbjKcnXqX_XxDwpWpjyb5JDz16Fh9s4cqr4DtJlgfBM-l8coKDOG18KFNPiRHtmIc8czGtc0eGbCfipDuMFRxUHJDsKBys1-K91Pi_qieIUm6nNSrqtjvD-eCqD3Aa4ZB19y2RkcB5bgbaD738iUZFjj0zlluCIVSQa6sdBeOBvHyyAeIigC5IIUDMVWtSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان دقایقی پیش وارد محل برگزاری اجلاس سران شانگهای در بیشکک قرقیزستان شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/459361" target="_blank">📅 07:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e781b7ad2a.mp4?token=gd9FmL_IGCQHXvVRkLUvmz6_wDFOj5R1_9_NFCecCPN_ukm0h4lRhJtQuJxaN9R72xKQvRgBSDRV2cDkxVUjT4HE2MffHTEDVYM0nK6fi3v2Vk9h2Yxyh2Bjc28LXWtVMHRnnDbMOYpI6OcXvPvUANNcD-rAL_0RFh7yaOCdLYwWd51UuQ0w2WCSYDJDwZeLFtluqxEoJ64bk90MyhqTqjOtyQJdQ0tKHC1JJy1I16VN_F7k9oSCQpGtdrWzZVl6OxiO2f2t1cnPrIAMVHvvNGcquomtsUe03IL-VWnBQ8c1UEZRX_hM4dYUY4LtU4mKlm4NAh6ypOADJkJTQDM-zDJj-9MQydMGyJ-QjNMTT0EIC3uCUAnlIOSQuWpL-vI6bsmi74Q25nTvdHMR09eGRoAvXGuo8PpnGFn0qHNG89woEoIVdV8KGy26r8-5syHZS52ufCOcfTPihHWjK1xaei5ZN2CuMF1FPwUffbL_nB723pnojTxLrfTqSi4_XXxG7SJICuaAd86m_eTfeyxyMfdi6PpUMXsLf_WUEVI-mLZWUKGX3dEcKeY99VjnPje2FApt6-n7iLtzSO20m4ODeciQuE3yr-p1Ks7-kf1_ShvC3VDWUqZnwmgKbphFQGKr4hdCYsSfc4UqKu3yQ1GgVEOz4QoxEUF1NLCODnbIfSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e781b7ad2a.mp4?token=gd9FmL_IGCQHXvVRkLUvmz6_wDFOj5R1_9_NFCecCPN_ukm0h4lRhJtQuJxaN9R72xKQvRgBSDRV2cDkxVUjT4HE2MffHTEDVYM0nK6fi3v2Vk9h2Yxyh2Bjc28LXWtVMHRnnDbMOYpI6OcXvPvUANNcD-rAL_0RFh7yaOCdLYwWd51UuQ0w2WCSYDJDwZeLFtluqxEoJ64bk90MyhqTqjOtyQJdQ0tKHC1JJy1I16VN_F7k9oSCQpGtdrWzZVl6OxiO2f2t1cnPrIAMVHvvNGcquomtsUe03IL-VWnBQ8c1UEZRX_hM4dYUY4LtU4mKlm4NAh6ypOADJkJTQDM-zDJj-9MQydMGyJ-QjNMTT0EIC3uCUAnlIOSQuWpL-vI6bsmi74Q25nTvdHMR09eGRoAvXGuo8PpnGFn0qHNG89woEoIVdV8KGy26r8-5syHZS52ufCOcfTPihHWjK1xaei5ZN2CuMF1FPwUffbL_nB723pnojTxLrfTqSi4_XXxG7SJICuaAd86m_eTfeyxyMfdi6PpUMXsLf_WUEVI-mLZWUKGX3dEcKeY99VjnPje2FApt6-n7iLtzSO20m4ODeciQuE3yr-p1Ks7-kf1_ShvC3VDWUqZnwmgKbphFQGKr4hdCYsSfc4UqKu3yQ1GgVEOz4QoxEUF1NLCODnbIfSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی پس از اولین روز نشست شانگهای: تأکید کردیم که ملت ایران همچنان برای استیفای حقوق خود ایستادگی خواهد کرد
🔹
یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود؛ تفاهم‌نامه‌ای که به امضای روسای‌جمهور دو‌ کشور رسیده و آمریکا آن را نقض کرده…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/459360" target="_blank">📅 07:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459359">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هوای پایتخت «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۸، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/459359" target="_blank">📅 07:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459358">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc4c12292.mp4?token=l1NKTGV8jn0OZmd_DC2axl-N3jL9csemMZzn4kKZwZNqtXRUB9vpDF35LEqzvYi3K6fem4vZaWU1UvEXtyO0i_VOP2tLhFsVuKCKguKrnmpdAS86QLGASSOlhyWpwyEgVNXM4nQ1t3FNWIaR3IiZI8ljdkNd_FqvDyZOTtRLWOrMM7tb9OsoQb6L2gZKhg1e7B6zz7mIhTpSu2HQaiSshp8rAqZ19B4a0O7UlLfqH7n2FlO74_lHr6EuaVYg3HUgPROuN6IMAu5-1okkzVMMDpQq514x7IV4JbhiBTyLcl3u7GU3NAzXdQvnneL-l-Mhet5IKvFLY5mBf2JjIBsgMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc4c12292.mp4?token=l1NKTGV8jn0OZmd_DC2axl-N3jL9csemMZzn4kKZwZNqtXRUB9vpDF35LEqzvYi3K6fem4vZaWU1UvEXtyO0i_VOP2tLhFsVuKCKguKrnmpdAS86QLGASSOlhyWpwyEgVNXM4nQ1t3FNWIaR3IiZI8ljdkNd_FqvDyZOTtRLWOrMM7tb9OsoQb6L2gZKhg1e7B6zz7mIhTpSu2HQaiSshp8rAqZ19B4a0O7UlLfqH7n2FlO74_lHr6EuaVYg3HUgPROuN6IMAu5-1okkzVMMDpQq514x7IV4JbhiBTyLcl3u7GU3NAzXdQvnneL-l-Mhet5IKvFLY5mBf2JjIBsgMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبی(ص) هم جنگ دارد هم صلح دارد
🎙
امام خمینی(ره)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/459358" target="_blank">📅 05:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os-wov3bjRRkKbERmTechwbAD7kVkTXaW7-rpEUUacV4vyZnyHpn7wtf52VPGLNUd4GEusL7HcOBm7Olw0HLmfJ8kxI72M_oPj6HWr-ojCkkRBpQWthPCj9pUEVyNNSjxnSJ6YkgRlCZL5vmjoQTI5v4T3CEb4KaDbF5oyGn_aZiBu1DNtALDgr6xSXbb4q0Gu17_RcNcXDrPk6nUHRm4qbMOofgTjF_Fk2i5blql4gWkmZMiZXR-r3t6oHDrziCo04KZjmfjSWCVxdwk0HrCUsao7tE5F4wr1X64rECv79ue7dE6FIaQsqzVR1g6O1oR_hKkkbADr2UZADohKXGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اتحادیۀ اروپا با چشم‌پوشی از استقلال و ارزش‌های مورد ادعایش، نقش خود را در حد مجری اوامر آمریکا تقلیل داده است
🔹
سخنگوی وزارت خارجه در واکنش به بیانیۀ اتحادیۀ اروپایی در حمایت از جنگ اقتصادی آمریکا علیه ایران: نویسندۀ فرانسوی، دو لا بوئسی، در رساله‌ای…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/459357" target="_blank">📅 04:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459356">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN08W7mO4xTrjyo7zeZPCRmujNdFCEQZAqiEqk_CkQKmqv6UAW_Gz7oqKPgrV3aGU7YY3NXg1o7WJ8GdmLhY_9I0-WklKB2cmQIz-nFkCbWUl_KgGYMCw2Nvrg7aIQohlgi1XFi57sElvp6CHdpkmWiAcPeV5-LiPCUOsP37i5OtgMyxsQ1rnKnas8b_DV9ZjQ_gmmm_K3vzH9otCdqTlveT5f_f8AqxJW1M0gtaNlF6NENcyPNhta4Bibwf2TmDBlXm6J2IZdV0jsXIEKvlV7KneP0oidpth8Iz0ca3ai3MX1-YmB_1FuBa6cIPJfSEz8mTFB-St_4fwmRuHnZQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت دادگاه با خرج مالیات آمریکایی‌ها برای سالن رقص ترامپ
🔹
باوجود انتقادات گسترده از هزینه‌شدن پول مالیات‌دهندگان آمریکایی برای ساخت سالن رقص ۸ هزار و ۳۰۰ متر مربعی ترامپ در کاخ سفید، دیوان عالی آمریکا به نفع این ساخت‌وساز رأی داد.
🔸
این در حالی است که
نظرسنجی جدید مشترک خبرگزاری رویترز و مؤسسۀ ایپسوس
نشان می‌دهد که مردم آمریکا از جنگ ایران و هزینه‌های زندگی مستأصل و ناراضی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/459356" target="_blank">📅 04:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459355">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ماجرای تجمع مقابل پتروپالایشگاه لیشتر چه بود؟
🔹
تعدادی از جوانان جویای کار منطقۀ لیشتر و خیرآباد گچساران صبح روز دوشنبه با حضور در ورودی پتروپالایشگاه لیشتر نسبت به فرآیند جذب و استخدام نیرو در این شرکت اعتراض کردند و مانع ورود و خروج کارکنان شدند.
🔹
تجمع‌کنندگان اعلام کردند که این شرکت پس از جمع‌آوری رزومه‌ها، تنها گروهی از متقاضیان را به مصاحبه دعوت کرده‌اند. آنها با ناعادلانه خواندن سازوکار غربالگری اولیه، خواستار ابطال نتایج، شفاف‌سازی و دعوت از تمامی افراد متقاضی شدند.
🔹
با تداوم ممانعت از تردد کارکنان، درگیری‌هایی میان کارکنان و تجمع‌کنندگان شکل گرفت که با سنگ‌پرانی به سمت نیروهای پلیس که برای جلوگیری از برهم‌زدن نظم در محل حاضر شده بودند، بالا گرفت و با تلاش پلیس برای متفرق کردن آن‌ها پایان یافت.
🔸
معاون استاندار کهگیلویه‌وبویراحمد در این‌باره گفت: طبق دستورالعملی که به فرمانداران و شورای تأمین ابلاغ کرده‌ایم، کمیته‌ای متشکل از نمایندۀ اداره کار و نمایندۀ سرمایه‌گذار باید تشکیل شود تا افراد بر اساس ضوابط و تخصص و به‌دور از هرگونه تبعیض و اعمال نفوذ ارزیابی شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/459355" target="_blank">📅 04:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459354">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBvlRgZCvIKMWY6CmjfGUTEycSeEGM3gqEAiV3D9IB0OojYoaBxtd-GII8Gsly7bG0LLLLdYlQedHddynqY9fZN_ftvsdmjiXf2PLXn0_7xvyFtr3n8sXvzoJd9dtKJrN-aVw1hgyeJUTStdqjAtFHg4L5VD8o8oNEP2RQN8ufytUPC5OExDOcR5q0MQlc9ZBn6OU1XDvK-sAEdOD1kx5HZ9OCo6vsiW2vI-WZJeD0bwOHqBgEz2F-q1iZeQ8ZhRga3msuzTY8oWIufQufv8Hi-jhLkQNuhHSBAJaRe-pe-RcKzoV1b1h1mtnA1NFkt0fOLvKbYk1K_k4Yc2OeWxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار ۷۰ میلیاردی برای فنس‌کشی جادۀ مرگ یوزها
🔹
رئیس سازمان حفاظت محیط‌زیست: ۷۰ میلیارد تومان برای فنس‌کشی محور میامی-سبزوار اختصاص داده شده، اما این اعتبار برای تکمیل طرح کافی نیست و باید در فازهای بعدی نیز اعتبار لازم تأمین شود.
🔹
قرار بود در سال گذشته ۱۰ کیلومتر از این مسیر به‌طور کامل فنس‌کشی شود، اما بخشی از فنس‌ها نیز در اثر سیل از بین رفته است.
🔹
درحال‌حاضر، دو بخش ۱۰ کیلومتری در دو طرف جاده فنس‌کشی شده که سرجمع آن حدود ۱۸ کیلومتر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/459354" target="_blank">📅 03:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حملات هوایی نیروهای یمنی به دشمن سعودی
🔹
ارتش و نیروهای مسلح یمن بامداد سه‌شنبه پایگاه‌های مزدوران سعودی و اماراتی در جنوب غربی این کشور را هدف قرار دادند.
🔹
رسانۀ عربی صابرین‌نیوز گزارش داد که نیروهای مسلح یمن به اردوگاه‌های سعودی و اماراتی در بندر «المخاء» واقع در استان تعز حمله کرده‌اند.
🔹
همچنین پایگاه‌های دشمن سعودی و شبه‌نظامیان اماراتی در الخوخه واقع در استان الحدیده نیز هدف حملات هوایی قرار گرفته است.
🔸
بر اساس گزارش‌ها، این حملات یمن با استفاده از موشک‌های بالستیک و پهپادهای تهاجمی انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/459353" target="_blank">📅 02:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSm6oBYIZh5gJiV4mYcWmQKcWq9cuULZt2zyYg575dm1tbDEGKFqFRH0724wyyMWyKJJ5f5npZAKUhJUOk2aDS6hlKoJBORjhA7e6rchWk1VZpgG5PtnqcJfgaSQW2AFT5uQwm76CMNJ01LDs-ghSz7oEFlPLxXCds673fHrzAXMQxkKGwjg5hmT7Eey_SN1fGcnRlulE425a-vVzEUtYK2CVNQ93eWIo2qGotlIiQpK9D1r6WyrtXV1OE-6KMGAMiJngHrmX8IquuJKK7zxmvIu-m_aAsu2TLvL4NZ8iKddo0GgsxRbGFr_f4PRzc2Y07Cs0ItCF0xHeuC7Hue-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش هنگام عبور از تنگۀ هرمز هدف اصابت ۳ پرتابه قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459352" target="_blank">📅 02:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1966c1289f.mp4?token=TnwLSxKJX0NuJlKk7-d2M1G7Qv90jcfijKv9NUSdl2Xg7rLaRQz1c8L8g8Sg5m4dMF2AK_gRSkwC1pfzgTdQNbcEIR8t_scNf0rtOXXESns_MfTI7aRw2Jbv8K2rGXCFxuHeMGWOAj6_d3ovzpsPXpoVczh4_jYZDWGUEXx1ZVqg4IZ94dPkkW-HG2tQccCui1_1BFL4s4MX_a5tzKhY8ZPYIHqUBPh8kIVRYVkq4kLeaLJIE0VjOtHD3lDs-SYfCEmZ5JQRgi2A1LLQJ5omx_DGUWK1_KYWxkT7aYTwvlpUXFUkWbNJfW6mxyJHwpViVBHHoopwm08aHP2_0I5I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1966c1289f.mp4?token=TnwLSxKJX0NuJlKk7-d2M1G7Qv90jcfijKv9NUSdl2Xg7rLaRQz1c8L8g8Sg5m4dMF2AK_gRSkwC1pfzgTdQNbcEIR8t_scNf0rtOXXESns_MfTI7aRw2Jbv8K2rGXCFxuHeMGWOAj6_d3ovzpsPXpoVczh4_jYZDWGUEXx1ZVqg4IZ94dPkkW-HG2tQccCui1_1BFL4s4MX_a5tzKhY8ZPYIHqUBPh8kIVRYVkq4kLeaLJIE0VjOtHD3lDs-SYfCEmZ5JQRgi2A1LLQJ5omx_DGUWK1_KYWxkT7aYTwvlpUXFUkWbNJfW6mxyJHwpViVBHHoopwm08aHP2_0I5I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور شیرازی‌ها در شب ۱۸۴ تجمعات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/459351" target="_blank">📅 02:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1K3ZiJmKdcKWP1OKzxsSNyio1dPcuoHUyOzzRSff9xCqq-4gaxY_GuymyB5dr6iYDL7KTolcwgnx6hEc0MEjwQh1nxfRXsTIazKml96VXrKW0eVCm_RF3sQ_BhtOE2mfi9iwI-EuKwX5cGcrDWAM0yLRaPXYh9iWmuvxqhTTzLNEGelsuhSbHKcywtbTdTmMIkq6hPQj1ODDbZKBQmRB8B2lreAmSg0Msc2p2XGfhtiy6_nJ861NSeHY2Z-qCgH1DHl_I250Dr72y04uMmjOkZ8AV1w0ZdGLzHS0T_VgKQWkWv9T-zRCzyUnYNMJqUsZ4wDXxAGvKXBHk--HpqPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون برای جنگ‌هایش دستیار اختصاصی پیدا کرد
🔹
وزارت جنگ آمریکا رسماً نسخه‌های سفارشی‌سازی‌شدۀ چت‌جی‌پی‌تی و گراک را برای بیش از سه میلیون کارمند نظامی و غیرنظامی خود فعال کرده است؛ اقدامی که نشان‌دهندۀ عمق روزافزون همکاری میان بزرگ‌ترین شرکت‌های هوش مصنوعی جهان و ماشین جنگی پنتاگون است.
🔹
وزارت جنگ آمریکا در بیانیۀ رسمی خود، گراک را ابزاری توصیف کرده که به «سرباز» امکان می‌دهد مأموریت‌ها را «سریع‌تر و با دقت بیشتر» در طیف وسیعی از زمینه‌های عملیاتی اجرا کند؛ از تحلیل بازار برای متخصصان تدارکات گرفته تا مدیریت زنجیرۀ تأمین لجستیکی.
🔹
این نسخه از گراک نیز از طریق شبکۀ ماهواره‌ای «Starshield AI» متعلق به اسپیس‌ایکس، شرکت دیگر ایلان ماسک، عرضه می‌شود؛ همان زیرساختی که فناوری استارلینک را نیز پشتیبانی می‌کند و پیش‌تر در عملیات‌های جنگی مورد استفاده قرار گرفته است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459350" target="_blank">📅 02:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459349">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcYmfCugxGSkJ2QS9ndDrEwMHC_xEDQsI5TycahAOtcMW1ZMCKVk1l80SnSYTD4oALZ0pPKQLwVXgXoZMl9vRGrUshaKKL1G72NbLeAJZwkVE7BEqlPYZAra2Vhdf2z2FLVWMcJoTtrKqGpwgzb4Ukv9CSqNXg1DQbPtf3VFitQydvz5kPv5ZbxRMtSx-l7oD03GVG1Nj-oFdyVQBwVIAbmny5iI-q3o5LJ9MFcxEZslqjY-P4s8Xw6HW10YD1rJfgBBFnTk86ghy22eEZPNr5HnJgPC2mDuFBzbgFw_sRJeqWr85jMAxuxpYb-rbXlUQNTAsw2ZHN9zT5ubKhjC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر جنگ آمریکا استعفا داد
🔹
نشریۀ وال‌استریت ژورنال به نقل از مقام‌های آگاه، از استعفای «دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش، بعد از ماه‌ها اختلاف با رئیس پنتاگون خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459349" target="_blank">📅 01:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459348">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023803cd5e.mp4?token=d20lqbwfKATP3sncqtEBKPo_-3vmDmRwB6QUZV5x1256e2YtAEoPyllxHbVc_GzDg-u3cpWzbtC1Ljm0OuNNyin_PHhrHDdPMm2_r25JSSOL2yiQHHpH2lSG3REycWv41W_XoLITKzknvy41s4JyDaU_gj4sWUyj34bvs8vf-BKtqfv-2RATH_cW-IB7oNUV-3AE1sI---Af_69oQgBuFWufYMHtO9h3f6VQXGvMv-nFljKMJzRLLZRpV2mNYUrAdgzoW9jd4ivlbDolEvMaHIXjeB3mg2hpDKaMCpqhxaLfSc3xqL_9aIXPf3IjLpbLN4pNpzrd6ZiCwmu0wusPLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023803cd5e.mp4?token=d20lqbwfKATP3sncqtEBKPo_-3vmDmRwB6QUZV5x1256e2YtAEoPyllxHbVc_GzDg-u3cpWzbtC1Ljm0OuNNyin_PHhrHDdPMm2_r25JSSOL2yiQHHpH2lSG3REycWv41W_XoLITKzknvy41s4JyDaU_gj4sWUyj34bvs8vf-BKtqfv-2RATH_cW-IB7oNUV-3AE1sI---Af_69oQgBuFWufYMHtO9h3f6VQXGvMv-nFljKMJzRLLZRpV2mNYUrAdgzoW9jd4ivlbDolEvMaHIXjeB3mg2hpDKaMCpqhxaLfSc3xqL_9aIXPf3IjLpbLN4pNpzrd6ZiCwmu0wusPLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای جدید وزیر آمریکا هم دروغ از آب درآمد
🔹
ادعای جدید وزیر خزانه‌داری آمریکا دربارۀ صف‌های چند ساعته بنزین در ایران، با مشاهدات میدانی خبرنگار فارس از روال عادی سوخت‌گیری در پایتخت، به عنوان یک دروغ‌پردازی دیگر برملا شد.
🔸
وزیر خزانه‌داری آمریکا اخیراً مدعی شده است که صف‌های دریافت بنزین در ایران به ۳ تا ۴ ساعت رسیده و این وضعیت را نشانه‌ای از فشار اقتصادی تحریم‌ها بر ایران دانسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459348" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459347">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار مین حین عملیات اطفای آتش در منطقۀ حفاظت‌شدۀ بوزین و مرخیل
🔹
فرماندار پاوه: در جریان عملیات اطفای آتش در منطقۀ حفاظت‌شدۀ بوزین و مرخیل، یک مین در محدودۀ مرزی منطقه منفجر شد که بر اثر آن یکی از فعالان محیط‌زیست حاضر در عملیات مصدوم شد.
🔹
آتش‌سوزی در این منطقۀ حفاظت‌شده ظهر ۸ شهریورماه آغاز شد و عملیات اطفای آتش همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459347" target="_blank">📅 01:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459346">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e7ed18f1.mp4?token=ThhRscxj_h7nZPTWm6jNCgrr4gcJFknA6APe4rLL-5cj6Z_W00LWpqn3MQGmnh500C1EWL7bQuE6-QYFFHiFLfyfFqXTl0gnjUZJI5NG8SUnVF8ulV_onZLwJtshbq_LKzKSLmijPeDDF1GsmVJ6-ryreA-nX8S1wyV1FghTjSdFJUj6rcTvJk97SDP59z1JF3faDOe8VIlRYIrRSrkHnwCO02sEKZWPEzuk0WrHJvse1U9gf3dP5RjP0YEUS7aRldzfX4LefQdw0fVy1QpzQJV259jPA9VDrhh8JAnJ2PafamD5r9TEJojasPtmVP-9Clq6__wc7k3uSUaho8qdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e7ed18f1.mp4?token=ThhRscxj_h7nZPTWm6jNCgrr4gcJFknA6APe4rLL-5cj6Z_W00LWpqn3MQGmnh500C1EWL7bQuE6-QYFFHiFLfyfFqXTl0gnjUZJI5NG8SUnVF8ulV_onZLwJtshbq_LKzKSLmijPeDDF1GsmVJ6-ryreA-nX8S1wyV1FghTjSdFJUj6rcTvJk97SDP59z1JF3faDOe8VIlRYIrRSrkHnwCO02sEKZWPEzuk0WrHJvse1U9gf3dP5RjP0YEUS7aRldzfX4LefQdw0fVy1QpzQJV259jPA9VDrhh8JAnJ2PafamD5r9TEJojasPtmVP-9Clq6__wc7k3uSUaho8qdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار زنجانی‌ها به شب ۱۸۴ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459346" target="_blank">📅 01:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZcPC1-BAuJm-xJfAONO8omdV3hY4kYxWyOmgSjZyRDSEiW7DuNPw29Kip9huhnfKL8BF_sL4rvhINM_le4P_a0r7aLXKxs1hVV12O50MQaqpr882U4Crh2HM_u9n5kWQMF223MUarjTDiz__oxG_rIq2pwN9tHrxlP7oiH49JpFlBhnwJVyWoPRVcTBjqAzsAJtS0ruc-rU-ePtTFh4uD_2G8TzQBGjMsfsfcNc-aEuH2thnhOQkIbjQt-SlgBZ65xa8R_WV7Hffw1lsxY6RBRS99AEujwaayFxfGHGIeZKTCVoX6R93RGakznEnejPfumk8OJCGk8ryOSAB-vD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYw6-uyuCece2-uCJTbVMMovtgeGvP2UJHlFNEwgE5EeXupHlyannZb0aOqq3cw-nTnx-FChf-zv1B4MIalNShYZeQcM51OvGuO5Po5MhF2oejCJRrn89dn2MfVDEIZhpcOAzgqqIfvuVvmAB7ZiqzQfvecErgOJA5TZEb2_0_y0aUUOWE2TBRl7fOryArFQhY-YqNxf5E2W-gUqLQVgS-yiQTR2IaIr05tJQWTX2u_4Z02XtPH62k9B1g82GlhKsY0YWzIPO-uJih3_QuWkfQvr8dsC_uFKz-_N9IRJB5W_Kq4MO5Brc8dq2xn6mFYfmTgdHg9WHY5kqclhPGuBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmfMopEMB_Q7Gx1iIWfuVBfs7z_PZXjcacwxeXoqVEHKjRzEiXA2U14i0tLWwSyXILp1pmaHBwH1ByhFeCAI21kVqirzyOnZTDboWAGBz_5OsoYQbgEf0cgUYs4Z--tqi19nOXgbcmtpL3yVxvnU1x0WnwfWLd0I19UfKzOshuJVzr9aQ4vi69vX1tEpe4S-SJ6i9e8kMxyoDSkiB3tHs86iBwQrTDsPPbT7pfXJueW6Z2AZEMBsfuZ5pYWoXxV66zVWeHGELCDVXgd-qyasog7AnVPnIjNu2Zzz2NjGEy4m7VDEQyZrJKs2RYYNfnUvv4i6ivbsim0ryttwoTvF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIwjLXPMQUnE-TDjSbL9cVy00jfnxpWTjeEvaCl-HIO4OQgGoj9L44PUCtOV0wfrt5uBMSd8zHLH9w_Asq_GO3DQNEVJKW-wPUczZv-wxkwtk52HUdsaGOW6m-0KZHLLnDV9i8D5LRawyvXV9MP5E3LjCg_iwOX8uY5ymdFsZT8LD-muhHdJb_ghoFP7SYeM82n3krcaQpHKLli8JN3nCYuF6t7QjPGv_2C8P0RaF0Bcsao77zblL1S0A-LvTFbJ9kOyCP1oK0qn6pdK8AUA-UG_Iiv8h6AJBtaS9NYnvabLDS9iW70ecYM-Nw9usKk0A0OMEJCc4ce25HWs2P_Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti2PeqwP_G0wN6eH30ZzfY2KntUAIjMbTv55YEbh9LBr7oU8BElK_6YCWR0KNXNxhx1IGQ6ouWwif3xFOOJF7Gu2tqLHNUktUeB8nBJnYV2WnHyb_riTkZv0rU43HK_xWZPE4G4oEd7H-zxyLXEMaZBvj53A-Uisdq9OuIdOHR_0prnn8vszVRZAFHaMvixa2XaGzwXc5LTQjvhzex-tSIy1Vh5eASd_W4cDYu7FotxkBZkeSVQiOI8JCRK87bwzIfFxqYDt5tyvFnHL4CtQXF5RI4EqY6qVyyQMM2Qb22PFsddwWqBNwhnboXWi1c4pyzz7OlaG8aCCOtYJrYs7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHUPOXEqJm8L2__-rB3BcAftWWKz8mZM46J7PZDp-xUPhAhuVg5LArMoTZhCWbRvlE-A0jmMbyspIli7cvUuZA797FgKEBjg3HssQToIzgOhqje7JTDhiNPOc2fz2WGs0otMHgyv_OEQTQUqGDN6t3J2-mqdBWTz5HmABXoNEKwplwJOKwqx1mtUGrNlimZs4LNCyycFAKV94-qTrILOMZ-lxREOiZAnte73ALj9IkCJbLdfjCExz5YJLYq1UkHxDDaDXCJmgA-iUm1_6a3Y_Zf7Cq0owvW2TzAp4jUZjde1py9ZZ4SV-Qwa3LC043KdrmvH7brpZ42Hs478jMlirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7O-vtqhdkLPZbA3J6Qid_yEfOV2NBWMuJhAL3CXtDJmjMeRVMpjFwaxjOV7BRUF9L7NiYy5Hj9WSvZtxUDXy-tXQfeG6-S_c4bf6LUkANn8c91wXmyvPk07YOhJS6NqE1CTH9xV6f1BamrIHAp9BLn6dI5TtaZ7Xu_Nc4tzfWnfF3h5D127Of0wgtx4U8-JySo3sAk9OTIo1vlKgXFbK3Uh10fnWIzNcLbF5iNKjk1ZtFeivSyziivdIuQbJQAi5xMWp_KosKAA-asECtB_ktYo9AekZoHxA7uJxrskck2LDNAEAmro7aOlc4cu-EBTGc5lY1ee-B0RijnRzGtRDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۰ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459339" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APBFh9E7NYvmfiAl8pyy7Qqn_jCBqOZMVRz0nfmUhzRqVG5unRCnENBZbTHvRV-PPEnPj-qPtB5e1k_8YQ7k1iPL8Ng_s98aEvxuYo7uxRQA89D4f98MsC1MQOuJwc8ArdaAim36Hze8rWCHQFu-pRRMWNT5X_vIEiYprFyLa4VzF7PqB4qLiF0ilSjBDnDtXu7A7oHd8x_h0xcIP8rauTPkZVXXWZbzjIXk3uzlw5ov_xtmPWj_iHzBWflwr50d9HhhJLW4zbPi6ng4JTElEWefjnNA4pKhPhgl_8QP8l4krqmND7AZhVvKdjL2oP6WuCNWhn9U0Kkqjo4IXdhr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQEhiI0_Gq4TZbh_bTSiLVXybDZb9fmrUfNEh0_Kok0NfZRSMJh2_DYYmsVljkTCSDfsjKs6dikhea-ANew8Fp8AUBfx_GGhoxCN2mzvKFaOBEYPWXFrgWw81aNRto1HUmNyftqenGxqcrMx_rf09-XkLNklyia4YEevIX6Bq77_cNVSDQP6o7F_M39DNzfI9KunDkhY2pMxkkbqUDt8aIpUKJKqQWyDlbE_FRC6G3N3i43suBYWNRvYPvxMzxdD6_sTKzqkxG965f7iZlbeAT80BS0Aw4Zx84fwGJ5RB7B5dQ0vRv8bDnKnNKsqBf_clbudJuGj9aGlb9zyBMMORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tm97aywvaA55A4AWXpMFWg_K2DJGzYaSuUk7nk_EiCqLQRB-Z_lcaYDlvqeb__EQ_ic_V0Q7FVjYbjSid1cnrUGFa6j7g39r8XJO5Dlgc6O47N6flT3NYktk_6bh-80oM7fGNpjwXGg9ojEIm7FmXqWPgIzdqWlZp9J_Yfa-qJcMVafrGMrbI9SlVEt335Gcb_2TN-9kpKpEBOzLmrK3zOaus0p-xC-sZ8HPjmdjSpm3a6t-_UtTM1Mr-qoH4RzFUH4N0j0M4gK3YopBpT1wIjyGEQHKFkINv3u8_7W2L2h2gKgzotKLVM8N-Q0fbpeeX1kJOmsrlX1d3Qc7nnqd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhX7-9B-YaWF6A5hXoXeaCNEmP7ebG6pByiJF6rP5J7f4VyHa0PocHflx5kP9WsJWUWqeqfKiHHSwnr_zopvbtlMQSQkJdvSeY3CyqfTBAGezGx85KhiL7ryUqriVXOI4M9T9Ge_TiIVE7VpTP4sVKXzP0FUjjZOs_5HfwVHT6rTQvdQGWNNYinyOAfVOg7em79yz_ViZ4zw8RE5UjKyU-hx_pX5JY4OktmKa9LeOB69B64eggAtnoRAZo4OqzhiI0TxbODvhX54v72BM4fw_ReqgCZ8FGHAf5FJzra_eLAqp8y9FJvcXeXbKCj-6B8BVWI4-FualJSONCpo86-J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohSOKrvFPTNXPM0m6Min_EDbD0SR-ub0HDKIIrLmM3QlMnUPApTu6YjfXDwQx0VYLKPFuhSpVuPoU_lR1RWpd66kXxZWg7FRpgtu6O1GgsoJqUxLkpBsf6Zbg_HGT9j34iMLwx568HjGY94YsfbGTt1i_z4tbsv6r77XxO1iXUCjRvlACcTAQglxBDZ6oA9lr_X1KQK0rcp4iHfYtSubDz_Gcbi34yVEDo847FWTDyWfo8LLdEhhgRNo10TS05nYAtHR5DIv6IsJui20MRzYNJc83LmxuopJXQEvI0oV87v-MfofVxTClYjFUJCCv113yb1A-CvRfzw7ZWbh96iFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kroyIcuJHz4IscnZxKMpaojEY4Gxzst2QPIThiuGhAuEIsVJnXLA61nlozgdi2c20Fp2RGFq1wPN3jtGyhQdORloGqosbsLqal66FC8ZrQOfSxQJHUWbMuC8IS91rtp7yZgkgSy67wivrTZb3fyIqOf9U2U6H4KVH-jFY4j9oQOeb1MLHTBzf2uttnp9bbACB6QMdQthmO3OTw69mXuzNt8SohTrCbEn0up7Pi88ZtPE2iEBqFlVdVie7zL5lTefUWdqBH1W7wLDa4jnny6l7XKD8lW_AeMet7tYNHmjLTPAUi_Bk5rVa2nf4PwTZwmDHbpAXyJyTr3utX0q8WKFPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spDO82CTNL-Ra7NfeKc_BaJ-5tqbrUkcICLArkZOb6y0J-xqfRdXro2PwfbtI531ljRBsHlOgdep_JHyMB-srictmVOuMZ9hbxp8XhlNrwn4pquj2cBNW2JRmgbc-HhQixOCnXjiRfruU_YYam9Tu6nR7bqrue6DqRbNk2kZruMRYw08XZNIo3J6dzYkzEXWEVuFZXazWCOzTkXRW1vKuk9Uvxvw1c5RiVGcqbUqDOdrOFR_cwBXigtOECEui--X8s9z-yIi5QymzPEGvj48EuTwmS42onioAkS945dD-3R38kaghE8oDyfXIdol8Xi7Rv_3uQQUasRfUPuGWNvSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWkjrtRpWHmLSUqYkC16x0xG_qrNrVn8cIdsFOkwA-G9leaDih-9Bfd9OlirXHMudZk5VTfr-cK1KwCdbq4RrIZYcmu_0JeIR3tebVqqfeQvg7gRzZLmSm2bd4W46eML_7C1BY7ZJgzqKzo6IJn-RS1SiwP9UV9U5kOAllG_k4JhVigsUTzVv0FPLJlTekKYC15YzqgCO4r59HaXoGcmhCtrIuCBXLXoXFuUflkUxkKJAOjNW-Jw-JdEzrwGhqIxsd50FpW_fRQf2x9l2LApqKBpv7cRnuISv20M4Taj0Se8pv0PwGqEzpx5lC_NNRQqKroKwvzUqHHr-JpAl1-tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBmxr7LtBV6pNzzpgnjxYIDoxFJg5mEerVEwnHDRMovsI6DiLd5tj99vEvGmqdY5XvhOgGuBlVc6LCyAwfYiijH7ktMOenp1wWAL1pLUgP22G0imLIswGZ9DBkG59fazCco8eAoGqkzSPVDA5pFCMvMkftKxDC_FOiTcOHXfCc-uRYHTuTnKEc_wkC2RWmjWTLjXViGDGdK4c__p6ury2kuFKZSSV0x18Vi90ya0qT5g1Ou9P0Kt5XkXvJFYCfbqjl-Iu6sIcOrsAVwCm9-Dbn5ASlRT0Y2H_AZh48MFk0o04SypOTaDaCDAKVs2XrUjS8PI9v2JQFJPex6x-nbqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS1zU-NbAuwuqMw6tEiAtIEAwf5uHgrbiFOXd1D5bT1LyVj9UPW7At_9v5G2aEQ3TT4kzMUts06QJUIBBBAgACW9N6dzUaeT-KPobp9e3o19GWjsMqEPj8-UPxXfvotwEskd4izrs8b1bGNXRv9sWeOEyk67-kRtPF2cUOopr2CjhmaMrKFMgdRlZzBHmsjQ5CKML6PJoebTlBoRX7Wx_rWlemr7E9ZPLqz8LR_f2s0VkOuyD8Thny2xz7OXykC_-jTHLU7srjFLUYb8DyU-G-_1j4j3gW8PtKyQnVILLDLsL6eyO_oJe-S8WtI3QmAtoYOenjDRu4_QfWD-9GD2jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459329" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🖼
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در نزدیکی ساحل عمان خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459328" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVdDjwoJI3XqA0KNL_VHsEPXmjQQiZPtEQxt-u3xggn3h0qmVZ0WSWRGe3C6IAh2dwSdT6M5pL-WIuuISZRpW9dbYv_mzyiQZDH_DXWnRRWL_O_iYwg6xvQw6mQpMZD3S6Ti8IXHB7waBmqzXVRT1t9e5Ghwku7IssZTICrLSIKnaTVNxr09_vV9rNbLYQXDsQHUBcnjZI0ycSobyaMLbTk8MiVrjA55Fal3z5zoItBheJTypEVGH-YWXctH6g2ZD9iRvJYjo8G3gbWUfrjsprbib0qA0L5NfxIxz92GfRlC7wveRX5onkh1ZVGAhk4c5maz-eW6h7qC349wu-QFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات صهیونیست‌ها به جنوب لبنان
🔸
با وجود مذاکرات مستقیم و توافق دولت لبنان با رژیم صهیونیستی، طی ساعات گذشته حملات اشغالگران به روستاهای جنوب لبنان ادامه داشته است.
🔹
المیادین گزارش داد که رژیم صهیونیستی با گلوله‌های فسفری منطقۀ کفررمان، و اطراف ارتفاعات علی‌الطاهر را مورد حمله قرار داد.
🔹
همچنین اسرائیل یک ساختمانی مسکونی در شهرک زوطر شرقی واقع در جنوب لبنان را منفجر کرد.
🔹
جنگنده‌های رژیم صهیونیستی نیز شهرک عدشیت القسیر در شهرستان مرجعیون لبنان را بمباران و شهرک القنطره و المنصوری را مورد حملۀ هوایی قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459327" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUCc_b-hctlKO7tk7gBmzwRkVDV4js1fstO93TXd93xfJx7CZax6RYhFBV-X_Jg4kiiB-XI1Lk5Fyn-yuSczWqN5yA_u3eIFZqiCZDM_UKyCg7be_dBHMDl0sTrN-F7SkRQlunGTCr-Gusw8HWFucDZVrg1uXQPaVmp20FDGPqUZJUPdOxIXNP69EdLcjvb5nRjNa5a9x-D4MReurU53BsIOBllr-aEPvTJ0bxnXvVmszASjAb9R0_U-dbN9NBGGKkYffDRxYAIBamfQMDxHpWeeb7CZ9-6eI8OaI2bdBJaKTcJMaR4q7hjs0Q8v7ynD4nA3ctaCYZLhW0n_-CPq-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اتحادیۀ اروپا با چشم‌پوشی از استقلال و ارزش‌های مورد ادعایش، نقش خود را در حد مجری اوامر آمریکا تقلیل داده است
🔹
سخنگوی وزارت خارجه در واکنش به بیانیۀ اتحادیۀ اروپایی در حمایت از جنگ اقتصادی آمریکا علیه ایران: نویسندۀ فرانسوی، دو لا بوئسی، در رساله‌ای با عنوان «گفتار در باب بندگی اختیاری»، حقیقتی بنیادین دربارۀ زمینه‌سازان استبداد و سلطه بازنمایی می‌کند: سلطه فقط محصول زور نیست بلکه اغلب با تمکین کسانی که توانایی کنش مستقل دارند شکل می‌گیرد.
🔹
اروپا دیگر نمی‌تواند از «خودمختاری راهبردی» دم بزند، در حالی که عملاً خود را به مجری اوامر واشنگتن تقلیل داده است.
🔹
خودمختاری راهبردی با بیانیه‌های پرطمطراق به دست نمی‌آید بلکه با نشان‌دادن اراده و  تواناییِ‌تصمیم‌گیری مستقل و مسئولانه محقق می‌شود، حتی اگر این تصمیم‌ها با موضع یک قدرت بزرگ‌تر همسو نباشد.
🔹
اروپا باید انتخاب کند: بازیگری مستقل باشد، یا آن‌قدر به پژواک سیاست دیگری عادت کند که این پژواک را با استقلال اشتباه بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459326" target="_blank">📅 00:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d4640bd0.mp4?token=i8BDI_yeAYw-Y-7pbfVyv8rl5xPhCTV2QPjjRuwH97ClW5muRlUQLkRN5wa2fpm8udxUcLiDVj5UNir1t-PeXEVN4lAcIqdHRFfuRE9TT2o8MmdYXERpzrxl6woWDElQoIQyWaWcBmUEtKf4yQ22pV5ooLhvVbw9Omz9cYEa-BDn2Ch9j7ZNwDUISd4TbBSKFFZ5FdFNdvL-8vuPl972-VLYtecAkZQit7t8FE3qtp6CX0vAkfTO7tJcPqNdI2IKC_T4b_GY3yxgZnrYLEenW9xKzgUN_wDQZ-8NwCG_h2L0BZf0rXKu41cKbg2Byt0iJsoGXfJpJdmgxGx2D2A_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d4640bd0.mp4?token=i8BDI_yeAYw-Y-7pbfVyv8rl5xPhCTV2QPjjRuwH97ClW5muRlUQLkRN5wa2fpm8udxUcLiDVj5UNir1t-PeXEVN4lAcIqdHRFfuRE9TT2o8MmdYXERpzrxl6woWDElQoIQyWaWcBmUEtKf4yQ22pV5ooLhvVbw9Omz9cYEa-BDn2Ch9j7ZNwDUISd4TbBSKFFZ5FdFNdvL-8vuPl972-VLYtecAkZQit7t8FE3qtp6CX0vAkfTO7tJcPqNdI2IKC_T4b_GY3yxgZnrYLEenW9xKzgUN_wDQZ-8NwCG_h2L0BZf0rXKu41cKbg2Byt0iJsoGXfJpJdmgxGx2D2A_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: ما همه جان فدائیم شیعهٔ مرتضی‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459325" target="_blank">📅 23:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Of-QCVlBpWMBswosFYBBlThgNGggNZS0CT-dXw6NxhbpIZcHY9cykQR7CymRxrRxwferP5aW9I8LDVMmIaT0QMdycauaQ682R5OLfndKMfUTWIb5qJoD1pfvz7c80KMTrOMY4QdNMUYc5DXuuUCZcQdDK6KC1XtmLA7_dsujmO--XNad6oS2wQPDUsnMtLcPjHTtWXnamKGLGdnv88o9BwwrPQhmypeJqxILb4qq9xM8Z_NZGB9YLaFMFsjiLWWoT-Shh1uPPTsZwRlTix5h_DpqlANJcQ1GfU28uBLYbL8BGXKxZAC90ljayXVXeGgVBCJIWHimI3w5ML3FLBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در نزدیکی ساحل عمان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459324" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogXj3_iSCAbyf2nE-4pC9GaF5oVEzyrgWjL6sbG1jVTT_EwAOM2plN4zMpoqWEh77kEVYa0TldMjYw6muzr2Jq5S5IbU8KA-bcyvGKRZgAia1z77PSXtNP2GyAt6l_1mfizD_zZOA1xNsSMG4FD54LkqOpp35q1WFWFXr6KDDq9CWEcmMLsfGm9EfPWF189gWC2l68mqxvReCj5ebbL0_MV09l2z3VKjwBA36MKCbWdWTr3owm_I126ZBGGxKAy-mh6f_L6N5xcGJo305JBq0C3c3Y2gMSryIBgYjmpEKQQs5p6ez99sm7jg7m0T3fOwenGY6WKFwyoYG97xEcE4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ بنزینی ترامپ با ابهام ۱۰۰ میلیارد دلاری
🔹
بر اساس اعلام کاخ سفید، توافق نفتی ونزوئلا و آمریکا که با همکاری «نورث امریکن بلو انرژی پارتنرز» به عنوان اپراتور بخش خصوصی منعقد شده، شامل توسعه ۱۷ میدان نفتی با ظرفیت اثبات‌شده ۶۵ میلیارد بشکه است.
🔹
ترامپ در شبکه‌های اجتماعی خود نوشت که این توافق «بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی» به دست آمده است.
🔹
باوجود ادعاهای بزرگ ترامپ، تحلیلگران بلومبرگ و سایر رسانه‌های مالی نسبت به عملیاتی شدن این توافق ابراز تردید کرده‌اند.
🔹
وزیر انرژی آمریکا، کریس رایت، قرار است این هفته برای امضای بیش از دوازده توافق نفتی و گازی دیگر به کاراکاس سفر کند که شامل قراردادهای قبلی و تفاهم‌نامه‌هایی است که ممکن است در این سفر نهایی شوند.
🔹
با این حال، نگرانی‌ها درباره دوام سیاسی این توافق، واکنش‌های داخلی در ونزوئلا و ماهیت استعماری آن همچنان ادامه دارد.
🔹
پرسش کلیدی این است که ۱۰۰ میلیارد دلار سرمایه‌گذاری وعده‌داده‌شده از چه منبعی تأمین خواهد شد.
🔹
اپراتور خصوصی این طرح یعنی «نورث امریکن بلو انرژی پارتنرز» به تنهایی توان مالی چنین سرمایه‌گذاری عظیمی را ندارد و کاخ سفید نیز توضیح روشنی درباره منابع مالی آن ارائه نکرده است.
🔹
همچنین کارشناسان نسبت به کیفیت و قابلیت بهره‌برداری از این ذخایر تردید دارند و معتقدند حتی در خوش‌بینانه‌ترین حالت، افزایش تولید نفت ونزوئلا به سال‌ها زمان و سرمایه‌گذاری کلان نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459323" target="_blank">📅 23:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9915508bd1.mp4?token=IUVxq-PYsF1YiZBjaMZmMHTtzmCd6jK0jdyGxqQYmu_9wKd-7iLvfkVHrt3X8_kmZ3gEtF3C9NUySQRPtnLZGt_TIbAwrN8Q_YMB1sdIbtVkQE8IvIy9UAI-TC02IGaWJJbBS4GhbRqNOqsCkXiwTnxa1sEd0QrJj0CBMm22APcBpcTXKLz1L3VVcaY9tPWJzHp20FdGfhBuQj1ygeGmidlyBN4avCu_L5czKuOCTiB6C4d0Fm_YIQPe4beLnBSOm8-8Q4rpORHrPStx9NBY3In24IgfA16sYMQy_UvijVRmDk-WG5qYTqzyApfGqtAIhPBpMU6Ly6TQ628_gUdf07CEMl8O7mh1lbS4WRF3NqalWt03qqtm5j2OBEhoxkucxU-r8SK8TO-Z72RcMvDJg5iYG8S2LJMhFItqbblOhH40gcnBaq7Bj5nPlMkyBulV1uv5UHyRWzG1gBmeuiTO6IBM47nQh6Cy-nHDiRljTELhgy2GoCj75e64AB3ZX3chbnzHfLFaPjNfhODHYCxmXCwtVI6KeNOirSScmz68kAHMbBRMW5PPMg2OIsS5Pyg9u_L6qAyqSd5tYrNQk5hA2k8be5_yf5e9iAstFr3Mayc8n858Fb32mcLuaXml7JZLyARkr4nZJtr0q4yYksuqLfYRemulI5eY8anxhCKvC7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9915508bd1.mp4?token=IUVxq-PYsF1YiZBjaMZmMHTtzmCd6jK0jdyGxqQYmu_9wKd-7iLvfkVHrt3X8_kmZ3gEtF3C9NUySQRPtnLZGt_TIbAwrN8Q_YMB1sdIbtVkQE8IvIy9UAI-TC02IGaWJJbBS4GhbRqNOqsCkXiwTnxa1sEd0QrJj0CBMm22APcBpcTXKLz1L3VVcaY9tPWJzHp20FdGfhBuQj1ygeGmidlyBN4avCu_L5czKuOCTiB6C4d0Fm_YIQPe4beLnBSOm8-8Q4rpORHrPStx9NBY3In24IgfA16sYMQy_UvijVRmDk-WG5qYTqzyApfGqtAIhPBpMU6Ly6TQ628_gUdf07CEMl8O7mh1lbS4WRF3NqalWt03qqtm5j2OBEhoxkucxU-r8SK8TO-Z72RcMvDJg5iYG8S2LJMhFItqbblOhH40gcnBaq7Bj5nPlMkyBulV1uv5UHyRWzG1gBmeuiTO6IBM47nQh6Cy-nHDiRljTELhgy2GoCj75e64AB3ZX3chbnzHfLFaPjNfhODHYCxmXCwtVI6KeNOirSScmz68kAHMbBRMW5PPMg2OIsS5Pyg9u_L6qAyqSd5tYrNQk5hA2k8be5_yf5e9iAstFr3Mayc8n858Fb32mcLuaXml7JZLyARkr4nZJtr0q4yYksuqLfYRemulI5eY8anxhCKvC7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور مردم سنندج در ۱۸۴ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/459322" target="_blank">📅 23:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6de282f13.mp4?token=bOm0Hxv1Krgb-zbo1FRfk72VXx45zfhb39xPc6fZmFASA3aBAoIxAdRINb_vCUTGDDyirPu4T850pxJIAwWD_bC9ae0XUFpMChkw9vJ-gwNbmBN6ttxvUCdGcV59w-hyCZvB_eiBZs7WOW_xfwk66nXpUSckC98lNZ8eqqO3I8UAKqQ0JaWGvI-BDVra_p8s3XYfQSmWNjtanVO_7cx7uCZtJ5uHcwp_dgMT3K2nMi7STbRQakMPi8vy69xrKAYHxZkyhWfNXbq1lDC1ahSLdLfAlDOU1DCC0bXtSlG3Zt_T9TjqQFpAgVZJ4kBOz99Jq7morjKzok_J-2Qx6uzD_7uzD_DjOzmPkGODQKYZqsa-mEtMscXtIt03QCn60wYzl5oiIkFyTDYrQCjJvM9KAqqkwvVCyW-cCKKWqwOuwinD1_1Bm3EbNYS4b4F_kEcUmC2sWuDgKI3GwbokTMmajububQC3wdu3g9-zBjZL1gtZW0unLD6YQNok7vPUJUlWLbbFIEFOIPQ6DqIziK24GmjBf76TabF3aS1_ox2CWqxwP9PkttmB1WLA4YOfLYC9jvhDGTyyFzZ1nYQDfGx5_IoGypu1G8Qp-jBTaYCz-HtHE8Fih1iYKs3mGXNe9Fvl05kYn-r6gmtNhO4uhvuT6IjG5TIc2tbQ9yB6HSXzFGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6de282f13.mp4?token=bOm0Hxv1Krgb-zbo1FRfk72VXx45zfhb39xPc6fZmFASA3aBAoIxAdRINb_vCUTGDDyirPu4T850pxJIAwWD_bC9ae0XUFpMChkw9vJ-gwNbmBN6ttxvUCdGcV59w-hyCZvB_eiBZs7WOW_xfwk66nXpUSckC98lNZ8eqqO3I8UAKqQ0JaWGvI-BDVra_p8s3XYfQSmWNjtanVO_7cx7uCZtJ5uHcwp_dgMT3K2nMi7STbRQakMPi8vy69xrKAYHxZkyhWfNXbq1lDC1ahSLdLfAlDOU1DCC0bXtSlG3Zt_T9TjqQFpAgVZJ4kBOz99Jq7morjKzok_J-2Qx6uzD_7uzD_DjOzmPkGODQKYZqsa-mEtMscXtIt03QCn60wYzl5oiIkFyTDYrQCjJvM9KAqqkwvVCyW-cCKKWqwOuwinD1_1Bm3EbNYS4b4F_kEcUmC2sWuDgKI3GwbokTMmajububQC3wdu3g9-zBjZL1gtZW0unLD6YQNok7vPUJUlWLbbFIEFOIPQ6DqIziK24GmjBf76TabF3aS1_ox2CWqxwP9PkttmB1WLA4YOfLYC9jvhDGTyyFzZ1nYQDfGx5_IoGypu1G8Qp-jBTaYCz-HtHE8Fih1iYKs3mGXNe9Fvl05kYn-r6gmtNhO4uhvuT6IjG5TIc2tbQ9yB6HSXzFGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم مراغه در میدان همدلی و اتحاد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459321" target="_blank">📅 23:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6f58959f.mp4?token=I9NDDw9-RHRucPOCuuUC8vBHhkJBuJjZt65UDu6Y0idl9-EJFG47-jhS6aG_p0XXj16ocwHIF6WnZdWNi8havCU7QdUSbdTvTmKbInBk3lAT_SmhmepNLPUPNwv4BDb6uRZSr17s5xN7-WO5Ucb9GdeZ55BRiPL34LEZ9dR8NnKswmTKazFfIi-rjMGSNRIEWf3e8x81hx-qKz7yXdd9GbKSUJ9BNTC2OLuxPnS7SgMW8K8BgCHnYkQuRXp0l0wBXNcW_sbwZfmXYUqUF0MxXF5ACdPeUlvhjHsHxY9rVdpdVaPARTT5OhJ19-0VAu3YWswTF_kiYIQvWWOXJP1d3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6f58959f.mp4?token=I9NDDw9-RHRucPOCuuUC8vBHhkJBuJjZt65UDu6Y0idl9-EJFG47-jhS6aG_p0XXj16ocwHIF6WnZdWNi8havCU7QdUSbdTvTmKbInBk3lAT_SmhmepNLPUPNwv4BDb6uRZSr17s5xN7-WO5Ucb9GdeZ55BRiPL34LEZ9dR8NnKswmTKazFfIi-rjMGSNRIEWf3e8x81hx-qKz7yXdd9GbKSUJ9BNTC2OLuxPnS7SgMW8K8BgCHnYkQuRXp0l0wBXNcW_sbwZfmXYUqUF0MxXF5ACdPeUlvhjHsHxY9rVdpdVaPARTT5OhJ19-0VAu3YWswTF_kiYIQvWWOXJP1d3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: خداوند به ما لطف کرده که لباس «گرفتن انتقام خون‌های پاک به ناحق ریخته» بر تن ما باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459320" target="_blank">📅 22:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93e7c790a.mp4?token=g1CWR3g5Rv4TYtYYdd_Izc6oqCWAvzfnNPXQTS_zpYx8y6PIAVj2xGDlBUA6Jv72GDAyFHWwwzpUjZJErbovK0UFCb2SbAGA9G_7BZtyrlTnxJrTZ8c_VniHXHvqfpYhczwva9VOsSNhsdJJUUtAufmCCBkHSRGxz4uNilwUeF8i-kz4q83aUHebvUnTJfdSH1iRsMpcDb-r0KV0UUHPn-t3en-sHXk0p6v15VAGK-j4zbTv2rhPnYSNSFa3JoXq9beEmcF4RCoY7YdYcbdFTW_FMP8dNIs7RMXEAysk6UqMWdPPcFolRPmA0_TAYgGDFEVFCQ2xka0fSvPNaOiM7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93e7c790a.mp4?token=g1CWR3g5Rv4TYtYYdd_Izc6oqCWAvzfnNPXQTS_zpYx8y6PIAVj2xGDlBUA6Jv72GDAyFHWwwzpUjZJErbovK0UFCb2SbAGA9G_7BZtyrlTnxJrTZ8c_VniHXHvqfpYhczwva9VOsSNhsdJJUUtAufmCCBkHSRGxz4uNilwUeF8i-kz4q83aUHebvUnTJfdSH1iRsMpcDb-r0KV0UUHPn-t3en-sHXk0p6v15VAGK-j4zbTv2rhPnYSNSFa3JoXq9beEmcF4RCoY7YdYcbdFTW_FMP8dNIs7RMXEAysk6UqMWdPPcFolRPmA0_TAYgGDFEVFCQ2xka0fSvPNaOiM7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مادر مینابی از لحظهٔ اصابت موشک و نجات دخترش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459319" target="_blank">📅 22:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzppv3XGj9WGvCfVCXD9yrfuwOzbEjYpctHa9Aszm56n6u8VnKrJlViJb8YN8uChVhqI21nHXhCJzqd_HkZDBX72Idld11IY2pkt9t0cr1GJ3qhp4J5lrc4qjsxrzd-DEpmXOJ5jM-3rXE-NNtIXixufCUpjQIfYxgl22B-zoVsIzbDMejw7ZH4YsdENXnYEJHLAObiOgjraoBrUIserirOKmiBaoVyI5TpW9ojX4Z4XsB7krx4LrtknbFqdrqp8cm9C6dLosthJakMbDReFRUD6bUnQKik3ROJnYMAEa3mGl4KdgPsaYPS9NwKYUa8DQtNVqdIje0I1JX1vJ5n86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیشهٔ عمر ترامپ درحال شکستن
🔹
ذخایر نفت آمریکا باز هم کاهش یافت و به کمترین میزان در ۴۴ سال گذشته رسید.
🔸
پیش‌تر ترامپ، بایدن را به خاطر کاهش ذخایر راهبردی نفت، مرد نابود‌کنندهٔ آمریکا خطاب کرده بود.
🔹
هم‌اکنون ذخایر راهبردی نفت آمریکا به ۲۸۶ میلیون بشکه رسیده و کمتر از ۳۶ میلیون بشکه تا کف عملیاتی خود فاصله دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459318" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما اولیای روستاهای دالپری، جلیزی، پتک اعراب و نهرعنبر با نگرانی عمیق نسبت به وضعیت آموزشی دخترانمان، خواستار احداث دبیرستان دخترانه (مقطع متوسطه دوم) در روستای دالپری هستیم. دختران ما نیازمند محیطی امن، نزدیک و کم‌هزینه برای ادامه تحصیل هستند. با این هزینه‌های گزاف سرویس و کرایۀ رفت‌وآمد، تحصیل دختران ما با خطر جدی توقف و ترک تحصیل مواجه می‌شود.
🔹
خواهشاً موضوع حذف بنزین خودروهای قدیمی را پیگیری کنید. اینکه مشکل کسری بنزین را از ماشین‌های پایین می‌دانند انصاف نیست. ما یک پژو ۴۰۵ مدل ۸۲ داریم و از سهمیۀ ۶۰ لیتر نهایت ۳۰ لیتر مصرف می‌کنیم و امکان نوسازی نداریم. در حالی که مدل‌های بالاتر بیشتر مصرف می‌کنند. دولت باید سامانۀ پایش مصرف طراحی کند و مصرف مازاد را شناسایی کند، نه اینکه تر و خشک با هم بسوزد.
🔹
ما مربیان پیش‌دبستانی الشتر از آموزش‌وپرورش گله‌مندیم. نزدیک ۲ ماه است پیگیر لغو مزایده و حتی تمدید یک‌ساله هستیم، اما می‌گویند خودتان پیگیری کنید. ما مربیان با سابقه بالای ۱۰ سال باید با کسانی رقابت کنیم که هنوز مهر مجوزشان خشک نشده. این چه قانونی است؟ سال‌ها بدون بیمه و با سختی کار کرده‌ایم. لطفاً به گوش مسئولین شهر و استاندار لرستان برسانید.
🔹
از شما خواهشمندم پیگیر قطعی مکرر برق در اهواز باشید. طبق گفته وزیر نیرو، قرار بود تا پایان شهریور برق مناطق جنوب کشور قطع نشود، اما متأسفانه این روزها برق به‌طور مکرر و درست در اوج گرمای هوا قطع می‌شود؛ در حالی که دمای هوا بیش از ۵۰ درجه است.
🔹
معلمان حق‌التدریس کشور با وجود تخصص و توانمندی که در طول سالیان متمادی در عرصه خدمت ثابت کرده‌اند، همچنان در بلاتکلیفی مطلق به سر می‌برند. علی‌رغم وعده‌های متعدد مسئولان ارشد وزارت آموزش‌وپرورش موضوع تبدیل وضعیت به قرارداد معین همچنان در حد شعار باقی مانده است.
🔹
لطفاً قیمت‌گذاری عجیب خودروی MG360 را که در مرحله اجرای حکم توسط ۳ کارشناس رسمی انجام شده، رسانه‌ای کنید تا مسئولان مربوطه درباره این موضوع توضیح دهند. چگونه با مبلغ ۱۴۳۰ می‌توان خودروی MG360 صفر، اتوماتیک و توربو خرید؟ این موضوع مربوط به حدود ۲ هزار حواله‌دار است که خواستار شفاف‌سازی و رسیدگی به این قیمت‌گذاری هستند.
🔹
لطفاً مسئلۀ شهریه مدارس سمپاد را پیگیری کنید. بر اساس شنیده‌ها بعضی مدارس حدود ۵۰ میلیون تومان شهریه در نظر گرفته‌اند، در حالی که قرار بود دهک ۱ تا ۴ رایگان باشد.
🔹
ما اهالی روستای پیرخوشاب ۲ در شهرستان جازموریان خواستار رسیدگی فوری به وضعیت زمین کشاورزی روستا هستیم؛ زمینی که تنها منبع درآمد و پشتوانه زندگی بیش از ۱۰۰ خانواده محروم است. این زمین طی سال‌ها با هزینه و تلاش مردم آباد شده و اکنون بیش از ۱۰۰۰ اصله نخل بارور در آن وجود دارد. زمین که پیش‌تر در اختیار ادارۀ اتباع بوده، اخیراً به شرکت ماهان واگذار شده و این شرکت قصد دارد آن را از اختیار مردم خارج کند. این اقدام می‌تواند معیشت خانواده‌های کم‌درآمد، زنان سرپرست خانوار و جوانان بیکار را با تهدید جدی روبه‌رو کند.
🔹
من خودروی دوگانه‌سوز دارم و مثل خیلی از خودروهای دوگانه‌سوز موجود، تاریخ مصرف کپسول CNG آن گذشته است. حالا جرئت استفاده از خودرو را ندارم، اما می‌بینم کسانی که هنوز از همان کپسول‌های تاریخ‌گذشته استفاده می‌کنند؛ کپسول‌هایی که می‌توانند بسیار خطرناک باشند. قیمت کپسول به‌صورت نقدی ۲۳ میلیون تومان و به‌صورت اقساطی ۶ماهه ۲۷ میلیون تومان است و واقعاً توان مالی تعویض آن را نداریم. لطفاً اطلاع‌رسانی کنید؛ شاید دولت بتواند مانند گذشته طرحی برای تعویض رایگان یا با هزینه کمتر اجرا کند.
🔹
چرا در طرح نهضت ملی مسکن، بخش چهارفرزندی حذف شده است؟ از سال ۱۴۰۲ ثبت‌نام کرده‌ام و امسال برای پیگیری مراجعه کردم، اما گفتند طرح چهارفرزندی از دو ماه پیش حذف شده و فقط طرح سه‌فرزندی اجرا می‌شود. در طرح چهارفرزندی، هزینه آماده‌سازی زمین از متقاضی دریافت نمی‌شود. به شهر جدید بینالود، در ۶۰ کیلومتری مشهد، مراجعه کردم گفتند قانون تغییر کرده و فرزند چهارم اعمال نمی‌شود. لطفاً این موضوع را پیگیری کنید؛ چرا قانون برای افرادی که از سال ۱۴۰۲ ثبت‌نام کرده‌اند تغییر کرده است؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459317" target="_blank">📅 22:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9723c6bb36.mp4?token=fyQDVu_w1ClrjgsC_qLhomL7lC3gCl5j_2nkjmCZqgeilGPo_GyHElQebd9M73o-HFEuY9jrfEgYLgD3CnPOmQlB7rMJbPq-c52n6Q0Ym4MDEvxIGTYe1D6K6A5oSvK0dMNMObfwFDfs4YHpdNlgy-0XoYh-3bOHEej9cd6Ctj6EYMaxIWeaYFl_GSrWhuzgGBjfOi-JqjAwBvJI-yoY_e3Qfbtomk3RlnOs1ysiiSBUCHtnLwiQs0cxkqAl2puOnddInCz2XjsYv8EUt_-UIi0PzmDJKYpB1OOQA44GffpUu2TLuxKC4xO_j119WKOiCkYNZ_vnBY6UCJtiCYTF9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9723c6bb36.mp4?token=fyQDVu_w1ClrjgsC_qLhomL7lC3gCl5j_2nkjmCZqgeilGPo_GyHElQebd9M73o-HFEuY9jrfEgYLgD3CnPOmQlB7rMJbPq-c52n6Q0Ym4MDEvxIGTYe1D6K6A5oSvK0dMNMObfwFDfs4YHpdNlgy-0XoYh-3bOHEej9cd6Ctj6EYMaxIWeaYFl_GSrWhuzgGBjfOi-JqjAwBvJI-yoY_e3Qfbtomk3RlnOs1ysiiSBUCHtnLwiQs0cxkqAl2puOnddInCz2XjsYv8EUt_-UIi0PzmDJKYpB1OOQA44GffpUu2TLuxKC4xO_j119WKOiCkYNZ_vnBY6UCJtiCYTF9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: برنامه داریم ناوگان حومه‌ای تهران را گسترش دهیم  @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/459316" target="_blank">📅 22:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff7bc0562.mp4?token=RwdEBdrlAeL8SiAteWdWbvocZ154wcRt_qTOvPRqVvirqlx9j1a6So0tYXWobyFbpuGa2vKQ-GcG6yvbznNCEaFkjagR8uydV_sz5lYYIFqE0UqJpVMOzJaFqM7vZI1H1o0qXeJBtO9SgWq_FdTDxi6cg4KZ8d4ONTGKW4xNv0Fecrt-ybXjZqABqBOknwqqbsu2icWIrJ7kSJgD4xiWf4WG_6FoUcqpkow3CeXnNPYORj-SvGhkFboXM1eip1yTFXkr9xGC1lOd4SgAK09F1SjxoB4qMGmDotZlGwPLqgPAsYMP5Y_YKDMsz3bCtY-QgdytYiFo7OIZKvi8tMJhaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff7bc0562.mp4?token=RwdEBdrlAeL8SiAteWdWbvocZ154wcRt_qTOvPRqVvirqlx9j1a6So0tYXWobyFbpuGa2vKQ-GcG6yvbznNCEaFkjagR8uydV_sz5lYYIFqE0UqJpVMOzJaFqM7vZI1H1o0qXeJBtO9SgWq_FdTDxi6cg4KZ8d4ONTGKW4xNv0Fecrt-ybXjZqABqBOknwqqbsu2icWIrJ7kSJgD4xiWf4WG_6FoUcqpkow3CeXnNPYORj-SvGhkFboXM1eip1yTFXkr9xGC1lOd4SgAK09F1SjxoB4qMGmDotZlGwPLqgPAsYMP5Y_YKDMsz3bCtY-QgdytYiFo7OIZKvi8tMJhaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۸۴ شب چراغ خیابان‌ها خاموش نشده است
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459315" target="_blank">📅 22:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef54732e3a.mp4?token=X_SRxJKl4-EDdg7kL34QljnrZk8D_u1OliWAj4KgcynOn-WAFM1MAOfmgIdmKx-ZM0z6Q18q_yApR4LM9t_31g6W79z17KWRasaR4Eby3h9HGaa42SbWbyXT8399XugGR5dcCI68ny3WYrPRhWFvKahRom6119fWfYg-ZalWnMmAU_Lu3ke47ZPGvFK_cpTm3Tvp8VHJetamroObzTyzfTTOGfDQnqj8jeSP6N2C5Ohi7I0IabjuCGAqI6psdlbC5w1LU7bD6GkSjciJ7RVP1sviQjOHeW1kpNR1nfML0ggONUuVsbJot95KOgBcuZJmFzaDCF7ESc52owEIOnMwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef54732e3a.mp4?token=X_SRxJKl4-EDdg7kL34QljnrZk8D_u1OliWAj4KgcynOn-WAFM1MAOfmgIdmKx-ZM0z6Q18q_yApR4LM9t_31g6W79z17KWRasaR4Eby3h9HGaa42SbWbyXT8399XugGR5dcCI68ny3WYrPRhWFvKahRom6119fWfYg-ZalWnMmAU_Lu3ke47ZPGvFK_cpTm3Tvp8VHJetamroObzTyzfTTOGfDQnqj8jeSP6N2C5Ohi7I0IabjuCGAqI6psdlbC5w1LU7bD6GkSjciJ7RVP1sviQjOHeW1kpNR1nfML0ggONUuVsbJot95KOgBcuZJmFzaDCF7ESc52owEIOnMwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکهٔ سه از جزیرهٔ لارک
🔹
تنگهٔ هرمز همچنان بسته است؛ هر روز کشتی‌های مختلف هدف قرار می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459314" target="_blank">📅 22:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFjwtjp2R-KsOK0wAMcULej9I3cSnF1MVPStZh6xfWZtTwXZh7KFmO3VvNG4YN1FHRsWdQm7EutPjkzdSRH_DK-gqXRQwmQLoC-5ucnvkiWbxEGCL-2a3xHPvmjDoVvw-m6urXxjF20fG6LhP-ydcU8dxgMyJQmms9ptGqAUE0TAMg2zXm4eLtWy1D_lUTfPdXdS10C1c6NHHxqt7rO8b1XIgH2hYfzWsChPhtWt_31sMxjWhQn9L14cAo1rfj_AQO9zA3B5Z17I58HmXLUR1aPIX_LbLp8VGvZkpdmTorPUl7w608Rq-GJ0wBbZ9C2S-wt_gUXud-_LpNbXMrbabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا برای مهار پهپادهای چینی کم آورد
🔹
آمریکا تلاش می‌کند با محدودیت‌های تجاری و فناوری، حضور پهپادها و ربات‌های چینی را در بازار خود کاهش دهد، اما مسئله اصلی در این رقابت فقط دسترسی به بازار آمریکا نیست.
🔹
چین در پشت این محصولات، شبکه‌ای از کارخانه‌ها، تأمین‌کنندگان قطعات و ظرفیت تولید انبوه دارد که محدود کردن صادرات به آمریکا به‌تنهایی نمی‌تواند آن را متوقف کند.
🔹
بر اساس داده‌ها در نیمه نخست سال ۲۰۲۶ حدود ۲۲ هزار ربات انسان‌نما در جهان عرضه شده و ۵ تولیدکننده بزرگ این بازار همگی چینی بوده‌اند. مجموع سهم این پنج شرکت به حدود ۸۶ درصد از عرضه جهانی رسیده است.
🔹
چین از زنجیرهٔ تأمین صنعتی عمیق برخوردار است. بخش بزرگی از قطعات و تجهیزات مورد نیاز برای ساخت محصولات الکترونیکی، رباتیک و سامانه‌های خودکار را می‌توان در اکوسیستم صنعتی چین تأمین کرد.
🔹
همین نزدیکی میان تولیدکننده نهایی و تأمین‌کنندگان قطعات، روند تولید و توسعه محصول را ساده‌تر و سریع‌تر می‌کند.
🔹
این الگو را می‌توان در بازار پهپادها نیز دید. پهپاد برای چین فقط یک محصول فناوری نیست؛ مجموعه‌ای از موتور، باتری، دوربین، حسگر، تراشه، ارتباطات و نرم‌افزار است که باید در کنار یکدیگر و در مقیاس بالا تولید شوند.
🔹
بنابراین، چالش آمریکا فقط این نیست که چین پهپاد یا ربات خوبی می‌سازد. چالش بزرگ‌تر این است که چین توانسته است فناوری را به مقیاس تولید تبدیل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/459313" target="_blank">📅 22:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5Y-v1HAZmX2_nvU4xXT4o8tvzlmsrfvJZNejBCxdChD8wJEfw5XxndIB9Bzb4d0LkiwaH_S2jkYfajmdDEcIYZIVK2DSjAlIOH5V5brZuYV6n10KL7DcHX7PaaV58ixTD98EgP0ZZz_HWZPUCsIrTtcs3Ke73GqBuaXKrqJ49nY3sb_q3UgRTLycYIPj7B4YIflMKy82cK-NKK4zqjIjc2qU5jBWtOfhF5Uw_roEoxRebp_aSWAUgEYVNqK_DAzORhc9Ym_TK1Vcavi8MAuck7BeDNgwMYw5C0IHHGHeVw-_dzITJmcdQtItulXTQ9KRDleHYD_2zT5oMloJWI2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس: ارتش آمریکا در حمله به لامرد از سلاح مرگبار PrSM استفاده کرد
🔹
رسانۀ آمریکایی آسوشیتدپرس امروز در گزارشی تحقیقی نوشته اقدام آمریکا در حمله به «سالن ورزشی لامرد» با استفاده از موشک‌های «پریزم» انجام شده است.
🔹
آسوشیتدپرس این موشک را «سلاحی مرگبار» توصیف کرده و گفته ارتش ایالات‌متحده برای اولین‌بار در لامرد از آن استفاده کرده است.
🔹
این موشک می‌تواند تعداد زیادی ساچمه فلزی را در منطقه‌ای گسترده پراکنده کند.
🔹
نهاد آمریکایی «ایروارز» گفته ۳ موشکی که روز ۹ اسفند به شهر لامِرد اصابت کردند، غیرنظامیانی را تا فاصله ۵۰ متری محل انفجار کشتند.
🔹
به گفته این گروه، موشک‌ها بر فراز یک مجموعه ورزشی و ۲ منطقه مسکونی منفجر شدند.
🔸
مقام‌های ایرانی گفته‌اند در این جنایت آمریکایی، دست‌کم ۲۱ نفر در این حمله به شهادت رسیده‌اند که ۷ نفر از آنها کودک بوده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/459312" target="_blank">📅 22:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYxBgec5wLxPpSnSMjR6Ioo4WdwDGXSE3HEhKMxUfaZNUs0bR2xiHwPNM0iiqpKsKd7-hojudfQvYq3w_uGSoVoqpWLOlktl9xzJyMlm4ymu9l0Y2pteDjIIm5S6IC6hXF0y5zjXPju6-gl2S0v3wI1QduWPVupMGiAzOIZ0pNTLEokzz8ajEVXizbzNY1SA9cs1jMYwRvflPGiii0wlfU_kvC2aG8dogWdaXH0BxaYkzdN6YrZdouhBJnhq3n-zelFnBF0c9uxZYwZO2zdXaPpntcJvjxe2me4KOpU8OZIUqp7CU6dEgEkVsUqwO99ZFDGEvFdYe0ADMXGM1E3-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت گشایش‌های پیوسته؛ از اشتغال و تولید تا انرژی و زیرساخت
🔹
روزگار ما، روزگار دوگانه‌هاست؛ از یک سو موج‌های ناامیدی و از سوی دیگر، تلاش‌هایی که بی‌سروصدا در گوشه و کنار کشور ادامه دارد. در کنار همه چالش‌ها، طرح‌هایی در حوزه اشتغال، تولید، انرژی، زیرساخت،…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/459311" target="_blank">📅 21:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2zMP5cn0gcZPWssd2MnxXlp4lGpmLySAi1lqOnOJryoqGSdnXgdtzDmTWCQhpkid1Ivk1DqfZBpANt9m5f28I69JqB3eY52tfyt3_sjYDF_AOLilygyi2b5e1OZcTLeDMDFvVJFL81Ruqa5f96GVIZ9FPqYWOTJ0j3qZgRQDpY2UsBd5Wg8f204i_RKS8_q74BpoG-ofgZmk0rKrCzbvudwrA52KONfAGlc4Xw06oYryRlJiwJAAhaZTniFbLRpFSz1nih653K-y-RZxbyu6-pLR8ILWMuYAhq-7cLO8__Yo2TfDs9OQdub6EvIQqOft09GeupGrdWXWhyzcu36jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_Wwm5wBoS0RaHbvBeXfg8Kps4Uy4mdlUfafeRid26u4Cs5bNf8igAUWiLS5eZuZbQ9cdmWl9_merc7AIKps5C3_Nwi7p1I4VNVeyMq8lfqQ3SVUUY9qGbns4C2zYu2JoK8wnR5YeUV0BBJk_pzgt-1Stp2xXDdKvoC8ZVsXYKY0CkXAn6zG0Ou7BMCl-SYZLnfuTLD4X7gs0nOVIYRV_sW-Mj9oaio5iavv5sWx0Kl-dXp0spkd9UAy4NG5r3ZDadcVMgoXE1DJECJsQU2rKk9O41mcFZ-oQD8mjKmbSFyRNEM4n4pmv_9FUhL_jfqQ2ZkUPovgtzxOaskJ30r9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlk1walMQit0UoRhYV86aCiJeUnGbfi_R8j_qfJB76ANneLRtWsKH8eXVzKOTtVHV4aYlg8fsAQTTf-PBGoIioyjB-gxS_Zc3KewJmH_SeGixRsCHMDT--sp80wnaEkKz1RyzsByFZj_LfmgNaP0QWZBDjvOWZt9UvUCwzPHmQk3H3PKRB1g_NDHP0YfPx9tJQlj4FStlA1aCmNNObE8fPA78GT8YeBJmDQaC1kq-9bx27-hBaHDH7_Tnn-ldxCmSHPpL-9EAoJITGvEFHWjd4kIB_fbAyPPTlBH_6vuA1Z5LoCs-2ED1hg1ujSJlC2SUcUbJ7JgH95bgQ1OmIKYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wbuuz_vvnlMBx0EqORWr4aNpHxBX4Ph17cMl7A-9BNbmfDHjdp6rjF6Djm6OnwgzLF9QJXULwtuil6jZ59gln2CsA7St5gn6mKLxrlRATa8zPtu9qaWQ2OgheLBxSUHFaVumAoW-hzcHa3eKKOHEUir0nlMrNnXwevalmABzqROIetsn7qFkNKHvXvVtQ5effQ3dCW08HJdHrU1h37Es3dancU65SEFdIUSEyFF0HN3hIdLMuHg8wacr1gkpqrsjfzAQqwxVfjiU2fpidrJXG96pKm5lSLz0pRyNNs5l3wAwgpXiUNEDZQ2_C8SGIwUhZVEDTiNbnu84IXSNCeXJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bG6mnXPkgi6-SUwmJo6qd8yGZGGzYJgj1xVFVzIpoidNDPqnSs4R_Wx8hc_Hr21JyEiyNxNyz81C6bL1V1WQHiFKGvpkrYdJ2Xa6NkWZnVfu6KIRlTWsdRAtV1NshOyEDmIwFAamhH0I3WSiIvod3jq6Z4BHUcwuoWEcXXhE82TWicnbmbw9pfz0pG0lzzPFEmWBOpr7_EgWdlNZZkGtiNGeaCBPR1OvWrheZc2-dBQT6q9ULxFdSBHj2I04VULUlt-i3RCYyjdqoITMrZDzo5BQg6VpjYiCTXW42YngXRFE2Hixe99Vsp-BjFSrk31MOLtqYqPX5GgKlnITyEw6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdyniSXiJTRhW5dW4OpyxftwJN3Q_kVRADxBX-fF_For_1gkaWqp2Oi7CeBzEg18asYSN-jw5SpD6FYylmB5J0hWGC97u-YuVy3Wl-keC2sVHYk89dp_jdf1utWSvjyJ_NzzsAEa5-pUuOK02cEGgsTHI8c8acM_m_jzmVSR49jCoRsc-mvr1c0jS0IggqRzZaLbRr4TFsdcQsiNrtVaAtcXeQjyhr8B2Th8qbv-eA_1XMuOOjDjkznvmhm5TEj-Yte_tzebEuMqaN47sDblsMtnJTCPFLggQwRBQdtgwIF00IxJZvdOWmXaXL3jbrw8tnxFfbHdnzR0TYlB7OBBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjRCUx4WiFab4QvJhcD03xuP3C4g-pPlTXaUBWS-Me83t8jIemmdRhM-S6KA1zLODYlrvxcGczyuhX3bwOnhKnbfauxL_ES9blIyNuzSElxxvjjELhEnllLs_LRhiMEdAHlBdxOscQAgynNOS7xESwMe-l5ddxDq5Jjg4JeJvFxoivzzkCJctSK7UzC-H793IJechzO7RDQLxpvyPUHx8CVFMDJD-P8U7e9RZskJ3kk23u_1q1yh3iVLrn9CelkGrUSApVUv1l74CtXsG0hfouqyEMbaiT2aO8SfHKg5IWtNYBrK4FERkijXOh3RKtyEU77gMFz9Ift7LkPsypO2JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهارمین رویداد نمایش اسب در یزد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/459304" target="_blank">📅 21:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459303">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd22634b22.mp4?token=mfQ78SsNQksLge-0kh1cph-EG8VaPv1_LZUyMUugwgIHAmMWzCckA2qqDs0NIZlXVbGArcKYzA7X16XMA35fpOYemAIBOr1AFcjLI7AWfQ8Fux7XyPiq4WdHIuUePmgk_5wMY0vcBglOGXt-igqG2T00hCZbka3tpBnLQ0PTEmxOPRcHUPoG-Kfn0DOogUq1omb9eO5QS56Jol9qMe3xFwceWvpIQm3BxfQ4sx71FnxtxwY1qUMmRNe4Z2BG_NJnXDtndVAPHCyGJFBBnZuaejfWFIAR8i2IOcoAll043qBjKWtvZg5L3BHdOIPfPgyrxC5qYvMesO8JG9jylGiK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd22634b22.mp4?token=mfQ78SsNQksLge-0kh1cph-EG8VaPv1_LZUyMUugwgIHAmMWzCckA2qqDs0NIZlXVbGArcKYzA7X16XMA35fpOYemAIBOr1AFcjLI7AWfQ8Fux7XyPiq4WdHIuUePmgk_5wMY0vcBglOGXt-igqG2T00hCZbka3tpBnLQ0PTEmxOPRcHUPoG-Kfn0DOogUq1omb9eO5QS56Jol9qMe3xFwceWvpIQm3BxfQ4sx71FnxtxwY1qUMmRNe4Z2BG_NJnXDtndVAPHCyGJFBBnZuaejfWFIAR8i2IOcoAll043qBjKWtvZg5L3BHdOIPfPgyrxC5qYvMesO8JG9jylGiK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: چندین خلبان ما در طول جنگ برای جابه‌جایی دارو پرواز کردند و به آن‌ها حمله شد
🔹
دشمن در جنگ به ۱۰۰ هواپیما و ۲۵ فرودگاه غیرنظامی ما حمله کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/459303" target="_blank">📅 21:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459302">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9775e7da80.mp4?token=gyh_y8TN2tTXCykHTbTeTKeziaVYHUWXHOpwyyU_oZVCqd-Rh-dMLPvPCR4etZdsFqtSTnKXp4xUdvtVdiPGyKpYAkKRr8x4wx0g7IrZZ9cmpGolXlL71NXJyfu2DlEggamwwQ1zbt0RT9mtcopwTsVn64JW5bNTzdGZLuKdfTEymFs8f7ZUzIWkqJkxTC8GtonvG-heKw2ek2rUcRmVQRcCs0vdAT8JBmYKFnt3iTgQQlAEgViYEGAES_aArCJWoDQx2lhK1nt6CY7UhoxppUHvO370a3lpZkdnVLMhr2EFj8EQfqq0UKR49rPljlZ5we0LhDZbrypiZa0Ac2em8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9775e7da80.mp4?token=gyh_y8TN2tTXCykHTbTeTKeziaVYHUWXHOpwyyU_oZVCqd-Rh-dMLPvPCR4etZdsFqtSTnKXp4xUdvtVdiPGyKpYAkKRr8x4wx0g7IrZZ9cmpGolXlL71NXJyfu2DlEggamwwQ1zbt0RT9mtcopwTsVn64JW5bNTzdGZLuKdfTEymFs8f7ZUzIWkqJkxTC8GtonvG-heKw2ek2rUcRmVQRcCs0vdAT8JBmYKFnt3iTgQQlAEgViYEGAES_aArCJWoDQx2lhK1nt6CY7UhoxppUHvO370a3lpZkdnVLMhr2EFj8EQfqq0UKR49rPljlZ5we0LhDZbrypiZa0Ac2em8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: چندین خلبان ما در طول جنگ برای جابه‌جایی دارو پرواز کردند و به آن‌ها حمله شد
🔹
دشمن در جنگ به ۱۰۰ هواپیما و ۲۵ فرودگاه غیرنظامی ما حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/459302" target="_blank">📅 21:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlprkXlPyeqe3d9amJgUlpQvuk93M-hKY-tuBtEF-1j_gEwd-m2lXEmMu0EOSuCgHdG7vodIdUWX4EFU-xrAZYMw_3X0C2BJ6kfx9-kzCrhUhcZjUFD4NurrrjqTlZxqYTEpl5bnDNmnwPerbjOuS3wu7CLcbEai0_s2C9iYT8e3hgZArF2-MSm1h--ZCMQC3HrlnAo7oR6LRm8nqquc_tmXnFJ-nLtV7bWVtQkS1IL1CXu9xPUWeEOOw9LL4xEc1IT4Dr20ZKQmBOirDmrmuYEgSeddRufq5XW5JCNJKz6yG-eyp_QRDuq2L85B4O4kCUMGcfFLnjtYhC3IGj7avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروغ هرمزی ترامپ لو رفت
🔹
درحالی‌که شرکت کمک‌کننده به آمریکا برای تحریم محموله‌های نفتی ایران یعنی تنکرترکرز می‌گوید «تنها ایرانی‌ها قادر هستند انتقال کشتی به کشتی نفت در تنگهٔ هرمز انجام دهند» اما همین شرکت سه‌شنبه گذشته نوشته بود، حدود ۲۵ میلیون بشکه نفت و فرآورده‌های نفتی دارد از طریق عملیات کشتی به کشتی منتقل می‌شود که این نفت‌ها از تمام کشورهای منطقه است «به جز ایران».
🔹
نزدیک ۲ هفته است که آمریکایی‌ها ارقام بالایی برای نفت عبوری از تنگهٔ هرمز اعلام می‌کنند؛ حتی خبرنگار آکسیوس مدعی شد که در یک شب حدود ۱۶ میلیون بشکه نفت از این تنگه عبور کرده است اما جمعه گذشته موسسه اچ‌اف‌ار اعلام کرد که حتی سنتکام هم متوجه نیست که آمار نفتی‌ای که دارد اعلام می‌کند، «شامل نفت ایران هم می‌شود.»اما همین دیشب یک ابرنفتکش با ۲ مین دریایی در مسیر جنوبی تنگهٔ هرمز منفجر شده است.
🔹
حالا که خبر دستیابی قابلیت جدید نیروی دریایی سپاه در شناسایی انتقال کشتی به کشتی (STS) در هرمز در رسانه‌های غربی پیچیده است، وزارت خزانه‌داری آمریکا که می‌گفت ۹ میلیون بشکه نفت با کمک آمریکا از تنگه عبور می‌دهد، امروز فعالان کشتیرانی را تهدید کرد که اگر به ایران عوارض یا هزینه خدمات پرداخت کنید، جریمه می‌شوید.
🔹
درحالی‌که شورای آتلانتیک در گزارشی نوشته که پیامدهای اقتصادی استفاده ایران از تنگهٔ هرمز به عنوان اهرم فشار «ناچیز نیست»،  تحلیلگر سیاسی سکینه داتو هم می‌گوید که ادعاهای اخیر مقام‌های آمریکایی در مورد تردد روان کشتی‌ها در تنگهٔ هرمز «جنگ روانی با هدف دستکاری» بازار نفت است.
🔹
با این حال، نمایندهٔ مجلس ، محمدمهدی شهریاری معتقد است با بسته ماندن تنگه هرمز و تشدید تنش، هر چه قیمت نفت بالا برود به نفع دولت‌های اروپایی و آمریکاست زیرا درآمدهایشان از محل افزایش مالیات بیشتر می‌شود.اما تحلیلگر ارشد انرژی، گرگوری برو می‌گوید که دروغ‌های ترامپ بر سر باز شدن تنگه هرمز برای جهان نفت نخواهد شد.
🔹
موسسهٔ میدل ایست می‌گوید آمریکا مدت‌هاست ایران را با یک بازیگر عقلانی با آستانه تحمل درد پایین اشتباه گرفته؛ بازیگری که به تلفات میدان نبرد حساس و در برابر ناآرامی داخلی آسیب‌پذیر است و در نتیجه به میز مذاکره می‌آید اما «تک‌تک این فرضیات اشتباه‌اند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/459301" target="_blank">📅 21:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqOxMcj4eVwLm-YabLsJKW2jKxwRYC4xdhJAAK48NRQwiJSsMy0bePLSi0abl7i4l3sSq4BzTu-yZ8WO7dflxQQBi5cpvEAhgrE9qwW22PFtRPw09RHv7ee0MtJnNgFdJfstmFqM8JwiJMQOM4o0hr5gZZMP7Nv3sAbr-UiaCVx4OPAeJOK3QJIgDm8znMv4tJTW8tQwZoJWER_H7Turh6E10JPXe4j8dx5n225dwHr5xRVZwhK405-XPVbde8uS0M5RqKvl7Shnxvh0-WsgajWNB_d6qxsFd1j1t6lxifYtt1OkGYqHPnsglTOHCwCe-uuPAL7jSCVfDoAj1pNeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی از قائم‌مقام مدیرعامل تاپیکو ؛
✅
تأمین مالی اوره حمایتی؛ پیش‌شرط پایداری تولید و امنیت غذایی
🔶
اکبر میرزاپور، عضو موظف هیات‌مدیره و قائم‌مقام مدیرعامل هلدینگ سرمایه‌گذاری نفت و گاز و پتروشیمی تأمین (تاپیکو) در یادداشتی  با عنوان «تأمین مالی اوره حمایتی؛ پیش‌شرط پایداری تولید و امنیت غذایی» نوشت: تداوم مطالبات اوره حمایتی، تأمین مالی تولیدکنندگان و پایداری سیاست حمایت از کشاورزی را با چالش مواجه کرده است.</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/459300" target="_blank">📅 21:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVG71Vpb9lrPmKG5ZKdW_0-ARSr-HqtC7ygmPBOQWV-OvgdQ8aDlZs84s4YcdlFkwa9PZNC0gtICfcX2e1kDeWsoiCAukXA-27LeD93B0nZ6ai9Ci5aTR8RzAqY9zbqOvJpUkLqGGl55P6yxB_p_Lnz5yCwWcOPisyCtXNG9O7D3JvO3kgYxry87K6GP-_owdnsjNelQJa1r2jf1h2CKUxV_ek6FjESpWr8ctILb3SMnCl4YDfLDq7vnBCl4bNXSExigiaBrqFOoE_LaAEkz3rA-d69GuBR7xUDBiPJIJwp0FjZXc4Qq51TM6-HFr9dlrEZTk7Dvac07m_kWPLKsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
اجرای طرح ملی «هم‌گام» با مشارکت بانک رفاه کارگران آغاز شد
🔹️
با هدف استفاده از ظرفیت اوراق گام و برات الکترونیک برای تسویه دیون کارفرمایان به سازمان تامین اجتماعی، آیین رونمایی از طرح ملی «هم‌گام» با مشارکت بانک رفاه کارگران و با حضور وزیر تعاون، کار و رفاه اجتماعی و سرپرست این سازمان برگزار شد.
🔹️
در این مراسم که در محل سازمان تامین اجتماعی با حضور نمایندگان بانک مرکزی ج.ا.ا، وزارت بهداشت، درمان و آموزش پزشکی و مسئولان جامعه کارفرمایی کشور برگزار شد، تفاهم‌نامه همکاری بانک رفاه کارگران و این سازمان با موضوع بسترسازی اجرای این طرح به امضای دکتر فتحی‌بیرانوند، قائم‌مقام مدیرعامل بانک و دکتر محمدی، سرپرست سازمان رسید.
🔹️
قائم‌مقام مدیرعامل بانک رفاه کارگران طی سخنانی در این مراسم از آمادگی این بانک برای مشارکت فعال در اجرای طرح ملی هم‌گام خبر داد و گفت: تمهیدات لازم برای اجرای طرح در این بانک پیش‌بینی شده و فهرست بدهکاران احصاء و از طریق سازمان تامین اجتماعی در اختیار بانک قرار داده شده است.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/459299" target="_blank">📅 21:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/459298" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459297">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1121404fee.mp4?token=umHvvAvOgWCr6LoejDUIOFQbbydVCBCAo6ymYUCCtKaCZA5bOIIH3RZ41gz16fAHyCi-uw2FFRX0lG6ci1lV1sKQOkkKqNK_3ycEBGmQTbZ6pL6aI5F50VjoazfVwsWa6k8-3eyzqJD3z6Fau2IaoPxKRAcRS5_-GKCZr7CuUa-iRWQN2r-DP7IjmIDvBRljULaGeLMU3b2HmjTwVmThLdYGgme4lnqUtuOKIjzJWakaEaS5-l8JxcNaaqnXaZjQ9SNOSfbKKQBhcT7VrZOWJTsILlEbY-8BIElPVf7XvQ4_e4GG0BfpabhNd_690_E3NmulKzg19rNvXvHXnQOGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1121404fee.mp4?token=umHvvAvOgWCr6LoejDUIOFQbbydVCBCAo6ymYUCCtKaCZA5bOIIH3RZ41gz16fAHyCi-uw2FFRX0lG6ci1lV1sKQOkkKqNK_3ycEBGmQTbZ6pL6aI5F50VjoazfVwsWa6k8-3eyzqJD3z6Fau2IaoPxKRAcRS5_-GKCZr7CuUa-iRWQN2r-DP7IjmIDvBRljULaGeLMU3b2HmjTwVmThLdYGgme4lnqUtuOKIjzJWakaEaS5-l8JxcNaaqnXaZjQ9SNOSfbKKQBhcT7VrZOWJTsILlEbY-8BIElPVf7XvQ4_e4GG0BfpabhNd_690_E3NmulKzg19rNvXvHXnQOGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش آمریکایی‌ها به دروغ‌های ترامپ درباره ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/459297" target="_blank">📅 21:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459296">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4002c74c.mp4?token=OqIpnOqYMNK1WjXf2G-eRdb5clE5K7l9um7b41ZSHvY911V0WXIO2jCqY1l2INlHasBTqB2l_R9C8xFIGq5cJkVpZV0ii72xIMDDuM35j-Pw3SJe6hsFVvm7zR7jHbMDVD19A0mMwxVkztaObvNKGcdq-9yg5AVhyIgTjd_en_35m9YM0Jy75LYmZRTQ7gTEMWJ1kM6hEv7U3prwMaFVwRlf0urFpsFXwBf8zvAXMID8WBh3xA5E4Nb--D3iLVzGBecs2hvgJIsZItB9u3V9BMk8jAQnhFpA2nhDKiPn9F4wnCgkW4mYLfqfA0FLCpgoAtat3U6YcR0X6SOpX_kbIyQ7VMkVBzmy7HbzIklj2SalINGYwiiuMzOBBt8AEcvFftwRbIRJN7ifhqW9PXL76D5VYR6rA48lGkiR16zFWcd3Rl_AjUL0sbKeACXbdqYeqMBnc0TemFvLxepre2s8CkClOq2kG_T42BV7hTnPA9zSv4kUExuZV0tQp1NKLg-cN3JK5GGj6IjqWHh-Dk9_Op-jqEIbS1AHjv7x6UkThEsLhEdd59737ts9rUV32kLEFhtDZ6pmuhpfli-b1LIGfQYMw-MHP-xYmp-VN7oDdVd6gH6hFzi5N-NUg6LfMA2HnF6mNoeNzbMAw7eoyos0LmO8dnJknCPydxIGhXRYoq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4002c74c.mp4?token=OqIpnOqYMNK1WjXf2G-eRdb5clE5K7l9um7b41ZSHvY911V0WXIO2jCqY1l2INlHasBTqB2l_R9C8xFIGq5cJkVpZV0ii72xIMDDuM35j-Pw3SJe6hsFVvm7zR7jHbMDVD19A0mMwxVkztaObvNKGcdq-9yg5AVhyIgTjd_en_35m9YM0Jy75LYmZRTQ7gTEMWJ1kM6hEv7U3prwMaFVwRlf0urFpsFXwBf8zvAXMID8WBh3xA5E4Nb--D3iLVzGBecs2hvgJIsZItB9u3V9BMk8jAQnhFpA2nhDKiPn9F4wnCgkW4mYLfqfA0FLCpgoAtat3U6YcR0X6SOpX_kbIyQ7VMkVBzmy7HbzIklj2SalINGYwiiuMzOBBt8AEcvFftwRbIRJN7ifhqW9PXL76D5VYR6rA48lGkiR16zFWcd3Rl_AjUL0sbKeACXbdqYeqMBnc0TemFvLxepre2s8CkClOq2kG_T42BV7hTnPA9zSv4kUExuZV0tQp1NKLg-cN3JK5GGj6IjqWHh-Dk9_Op-jqEIbS1AHjv7x6UkThEsLhEdd59737ts9rUV32kLEFhtDZ6pmuhpfli-b1LIGfQYMw-MHP-xYmp-VN7oDdVd6gH6hFzi5N-NUg6LfMA2HnF6mNoeNzbMAw7eoyos0LmO8dnJknCPydxIGhXRYoq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان میزبان آغاز یک زندگی مشترک شد
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/459296" target="_blank">📅 21:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459295">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073f41dc0.mp4?token=csoHnerDDmyekKyc3megl9FTIvCa2dez9juVyh9oohKHbmfdsv516RXrqkXcI1JU4LfLKzOOrU-i7G_TSkI1xzpl5pYrCxHZ8cvRPCiiucNMWI92OEtVZjIRdxonXjJJmOBW-uvgIfse9Yx_VXytG-PV4MXcwuKYcj-dWLLnVB4o4DWhcgw4PGMpA5XVZCGjPW1kmfzL0o1w5qivRF1OJ-oqCn2oRr2HKu1DyXA6DiW9yIxC7YMMZyDen6Tpn3VCgHg4MdeBT-LFfdYGRIyuPEBSmdHnNpj0sSZXC89xKYgZ6RJAmouIxRD_GafqGiwt0v9_M79DEsgsCWbd9K_cEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073f41dc0.mp4?token=csoHnerDDmyekKyc3megl9FTIvCa2dez9juVyh9oohKHbmfdsv516RXrqkXcI1JU4LfLKzOOrU-i7G_TSkI1xzpl5pYrCxHZ8cvRPCiiucNMWI92OEtVZjIRdxonXjJJmOBW-uvgIfse9Yx_VXytG-PV4MXcwuKYcj-dWLLnVB4o4DWhcgw4PGMpA5XVZCGjPW1kmfzL0o1w5qivRF1OJ-oqCn2oRr2HKu1DyXA6DiW9yIxC7YMMZyDen6Tpn3VCgHg4MdeBT-LFfdYGRIyuPEBSmdHnNpj0sSZXC89xKYgZ6RJAmouIxRD_GafqGiwt0v9_M79DEsgsCWbd9K_cEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک توصیه، هزاران بازنشر
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/459295" target="_blank">📅 21:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459294">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28b896ff2.mp4?token=YAIzb59pv0mCqq_LRysJNMb_z-0T3BpTuN1uNqSwbJm-wb_3CSs1Q2elnLnK7kUwEng9AQPGhKSU2nvNwdmNRpXfmC8D2h2jeLiOSJ54AMvy9k1rNkc-BpalcwGtt27j6WzQPRgl3CnsBn3aO0oH83MbPcvUpYky97A9qtnxT2QXKsmeF98E_MJ9E73ajpoVdH-T8_QP7ykj4Cgmmx4UkjMXfMTC_h-z0H4wgwdFMbLf6E8KdZoMrLpNSDvBe3KXYUJ0tRnh_C0LnY4O9XwbdFSBBi4HClhog6A8Cy8hvzB2nN6ib89Bi94CkLVhGTCMJljM3Sd3Ik4NQigk_vLURqqhbOcIqr7KeO1LEm5f2UpEw4TQ5dTt-dPM8vsq3TJypMtoycNXqLo2dgYaQSIAJilLbWqFFkPefNXCxAdf64ClVmP5Cjfy2PgH1E8LahxKHRGGSYx7oL_kY3140-GXCesvXzB9rlYFDI_TAUAegRSZZ-dqJYTOONxmyjsrTMQ2mP4ynWozHusZ1vE3WX0esU0NrFQAt9f4zh59BrM9uHcPdPmb7ezBjvNNJzlmj_RpDwDSET2K_zDaiKtG7ttGKsx5wqrxEHwFlL01g0i-EGjYoRKWIXaDqwODB09VriYF3k1G9nqeN-lvLVRjAC2XPS-tjtUtij6m7sga_XKkc2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28b896ff2.mp4?token=YAIzb59pv0mCqq_LRysJNMb_z-0T3BpTuN1uNqSwbJm-wb_3CSs1Q2elnLnK7kUwEng9AQPGhKSU2nvNwdmNRpXfmC8D2h2jeLiOSJ54AMvy9k1rNkc-BpalcwGtt27j6WzQPRgl3CnsBn3aO0oH83MbPcvUpYky97A9qtnxT2QXKsmeF98E_MJ9E73ajpoVdH-T8_QP7ykj4Cgmmx4UkjMXfMTC_h-z0H4wgwdFMbLf6E8KdZoMrLpNSDvBe3KXYUJ0tRnh_C0LnY4O9XwbdFSBBi4HClhog6A8Cy8hvzB2nN6ib89Bi94CkLVhGTCMJljM3Sd3Ik4NQigk_vLURqqhbOcIqr7KeO1LEm5f2UpEw4TQ5dTt-dPM8vsq3TJypMtoycNXqLo2dgYaQSIAJilLbWqFFkPefNXCxAdf64ClVmP5Cjfy2PgH1E8LahxKHRGGSYx7oL_kY3140-GXCesvXzB9rlYFDI_TAUAegRSZZ-dqJYTOONxmyjsrTMQ2mP4ynWozHusZ1vE3WX0esU0NrFQAt9f4zh59BrM9uHcPdPmb7ezBjvNNJzlmj_RpDwDSET2K_zDaiKtG7ttGKsx5wqrxEHwFlL01g0i-EGjYoRKWIXaDqwODB09VriYF3k1G9nqeN-lvLVRjAC2XPS-tjtUtij6m7sga_XKkc2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در سفر پزشکیان به قرقیزستان چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/459294" target="_blank">📅 21:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459293">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ebde07faa.mp4?token=rzRiVes4lweP4LscWgHrh_TNK_3ifTdDOSOGqs7DSyuK5ZmxauikSb3MIiwKES8ekRKedW5is1vmOAsYcj8mZoxZZVLxki-1bjfxtH5AeelDG2Y7vissuF0Eqwk9N9kobe2VsE18WUDc0T2bt8zZGmoUSgy3iOxuDs3TJOccIlYpL6zmWUdS8U_Dd2HRtBx85qNgod2hvVmwuJ4gf8rVzbJooG_J8DSZZlTj8uk73fFYVcEbyWpEG8r5svZ8awgAQTT53uSw7sp9X4M0Lu78JDdnZzbVQ9jm0cPSU1RgzP6JuQ1owEHVGMzU8WlJTXpHmOI6SphKSrJgOpaveW6_dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ebde07faa.mp4?token=rzRiVes4lweP4LscWgHrh_TNK_3ifTdDOSOGqs7DSyuK5ZmxauikSb3MIiwKES8ekRKedW5is1vmOAsYcj8mZoxZZVLxki-1bjfxtH5AeelDG2Y7vissuF0Eqwk9N9kobe2VsE18WUDc0T2bt8zZGmoUSgy3iOxuDs3TJOccIlYpL6zmWUdS8U_Dd2HRtBx85qNgod2hvVmwuJ4gf8rVzbJooG_J8DSZZlTj8uk73fFYVcEbyWpEG8r5svZ8awgAQTT53uSw7sp9X4M0Lu78JDdnZzbVQ9jm0cPSU1RgzP6JuQ1owEHVGMzU8WlJTXpHmOI6SphKSrJgOpaveW6_dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پخش فرآورده‌های نفتی
:
۵۰ لیتر بنزین ۵ تومانی به سهمیهٔ سوخت خودروها در ۲ استان اضافه شد
🔹
با هدف مدیریت مصرف سوخت و جلوگیری از صف‌های طولانی در جایگاه‌های بنزین، کارت سوخت جایگاه در استان‌های کرمان و سیستان‌وبلوچستان حذف شد.
🔹
سهمیهٔ اضافه ۵۰ لیتری (۵ هزار تومانی) به کارت‌های سوخت شخصی در این ۲ استان تخصیص یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/459293" target="_blank">📅 21:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459292">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svbltforEnOZToH9DN7wiOj5uNgN6Z-PbH2PSqK2Lf_THeR0LZqJm7y8h-AgoAlOcFq0gNMfVlGuqmiP8OP1Jy9PrSLKzi7QBXpWR-_ZMup2w3EghqhtPlGoOrhqlYrXtm1q8Suk3N3achKB0odWnInPTVHj5Qv7z0vDwcJ1ZZ77plVNFWQ6C7NJXCef1dozAi9SZknk1TuSc4LQ5cLCQsKmDJLu0bts7La9j_7MP0RknWAmrtAJ6a9ut4xo6l1jqOjaNdJVVhb0Hr461EXAdw44-LMNVZT6bihppFhIYDQdFgQmk97bltUxL0puSbtDNGSXQRD75CoOPebJvLx0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح: تجاوز از هیچ مبدایی را تحمل نخواهیم کرد
🔹
ستادکل نیروهای مسلح و قرارگاه خاتم: باوجود تکذیب کشورهای منطقه، ارتش تروریستی آمریکا همچنان از سرزمین، آسمان و فضای آن کشورها علیه کشور ما حملاتی را انجام می دهد.
🔹
همانگونه که تاکنون در میدان عمل نشان دادیم هرگز هیچ‌گونه تجاوزی را تحمل نخواهیم کرد و پاسخی به مراتب سنگین تر خواهیم داد؛ نمونۀ آن را شب گذشته توسط رزمندگان دلاور سپاه و ارتش ثابت کردیم.
🔹
ارتش متجاوز آمریکا راهی جز خروج از منطقه ندارد و تسهیل‌گران تجاوز آمریکا به ایران اسلامی بدانند که نیروهای مسلح مقتدر ما مبدا هر تجاوزی را کوبنده مورد هدف قرار خواهند داد.
🔹
هشدار می دهیم شما بارها اراده قوی نیروهای مسلح و مردم سلحشور و مقاوم ما را آزموده‌اید، بار دیگر آن را تجربه نکنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/459292" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459291">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reUvUWIsd9Nfw1jDCe03RmgaSeXDdhM0EJNZSoMOo-F9v-XChpZmfVMSRkM7aEoj8MQrL2HjEK7cydP3nqyzbE51jhmRS63hOtQHK42vi8LF5mgPT7K42eKO87Qz8XI3tzwZDOfZ8Z-36UffmcOmTlpwaw393TobAykGD704dgsEPXiXgld9O5stB2pQgXzKK5IaX7x2I88f1bY0WRs8dwY_BtGkxnt3V3eYXpC8YUyOqpOPwE4J7FwV6vc3QpSUa7Pylddk3IUM1Bar6GtIndtfBGshvTb3wi86z0PNr0fe6B-3f_TEZ6Y7FqmppvYlTVf27R9zNNhAemm8OQ8r0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عفو و تخفیف مجازات بیش از ۲۵۰۰ محکوم با تأیید رهبر معظم انقلاب
🔹
همزمان با ایام میلاد باسعادت حضرت ختمی‌مرتبت محمد مصطفی(ص) و امام جعفر صادق(ع)، رئیس قوه قضاییه در نامه‌ای به رهبر انقلاب اسلامی خواستار عفو، تخفیف و تبدیل مجازات ۲۵۷۷ نفر از محکومان دادگاه‌های عمومی و انقلاب، سازمان قضایی نیروهای مسلح و سازمان تعزیرات حکومتی شده بود که حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای تصمیم‌گیری در این خصوص را بر عهده رئیس قوه قضاییه گذاشتند.
🔹
حجت‌الاسلام‌والمسلمین اژه‌ای نیز پس از بررسی‌های لازم، دستور اجرای عفو، تخفیف و تبدیل مجازات این محکومان را صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/459291" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459290">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCrRqlfE1GAoAv8jdX3yp8lb0bzs_4LhC0ueQIoBVq9FgSkOi6HhRWq_ddgUF9cBIP82MGvPlGdoAPs5DOZ_doC_CTd_Wlbg2PCudxoO3Vp-t5ymdMcxg_YqDQ5xF34udTVhD5R6dh3SZajE2cJMafgrvJM-u-UZuXker0m5Ow93lmkrZF1iSzD3IyiBPGHfyGRpTNcvug0Z6_0mzL_gRpiIaMlH3626PIXxNItdQ4nXp4mopIE_otCcDO2IQObxMPUI5qf-xc3OP-hMvpU-FnB0xIB-FkUH8Ssxm9pH7GzQUhYDxnAXPMAH_kUu5s98GyBh8nkR-ZPsM5JGhb0rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر ماهواره‌ای از انهدام آشیانه هواپیماهای جنگنده ارتش تروریستی آمریکا در پایگاه الازرق اردن
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/459290" target="_blank">📅 20:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459289">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088547a24a.mp4?token=WUq0emHC1xLKJAB0N_SR7xHK9lJXtBqtWg8Cot_FQPxunhU_XikZtwl1SHLCnMCepDqWjvv5b-k217xO5rPxRqr1ksSCMRF8CRA5aLicohwNosDzU6Rd5kiuej43JIxNPH5HgTKl4r6UP9MGGDx_CE5EUndIjFazNroj0Krv90rQymu3yrFntWRfhfzZQedZyVjS2G_zrUOqfFt_D1bYiALMEfeuxHf1LvtDT-n0FPal7Ii_j_p5zXBZIpuCJClNL-ZRIKFpiRgKw8WVkifbP_cwlA4g7AP_NfUfjpm_G0mIz5O8lokoNJp-LV7or91uRngC7NupLFxnOBnTsb7JvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088547a24a.mp4?token=WUq0emHC1xLKJAB0N_SR7xHK9lJXtBqtWg8Cot_FQPxunhU_XikZtwl1SHLCnMCepDqWjvv5b-k217xO5rPxRqr1ksSCMRF8CRA5aLicohwNosDzU6Rd5kiuej43JIxNPH5HgTKl4r6UP9MGGDx_CE5EUndIjFazNroj0Krv90rQymu3yrFntWRfhfzZQedZyVjS2G_zrUOqfFt_D1bYiALMEfeuxHf1LvtDT-n0FPal7Ii_j_p5zXBZIpuCJClNL-ZRIKFpiRgKw8WVkifbP_cwlA4g7AP_NfUfjpm_G0mIz5O8lokoNJp-LV7or91uRngC7NupLFxnOBnTsb7JvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی پس از اولین روز نشست شانگهای: تأکید کردیم که ملت ایران همچنان برای استیفای حقوق خود ایستادگی خواهد کرد
🔹
یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود؛ تفاهم‌نامه‌ای که به امضای روسای‌جمهور دو‌ کشور رسیده و آمریکا آن را نقض کرده است.
🔹
آمریکا باید به تعهدات خود بازگردد و به مفاد یادداشت تفاهم پایبند باشد؛ پس از آن می‌توانیم از این وضعیت خارج شویم چون همه کشورها دغدغه دارند که جنگ هرچه سریع‌تر خاتمه پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/459289" target="_blank">📅 20:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459286">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0fcbc506.mp4?token=tzHGtNgzZ-IyHNlN_Y9YgwnZxG3F7fYORDsY8zzYN1qUE-KV5sbMXi-o4GsyjH9rujeVpq1M3ol5lTe0HQzEGAo_iHD5_5HN_OPgZjX14UHMXPL1x-svAi_-oQde3SDnozOPxrbnguObH8Bw2FIDQFVNb-OyHJJeZw_wZCrnP7XT8lCsFgmgbYM6kEksWJy-H8MdB7wiqy3cWFwFFprjobHj_sP0z0rtsPmGx7ysUXRhS6W3XEmU3mkosWa8bMsuHmE8Iq61-ivGc9OeKZJbn0xKt4AND-CbYs7jzkArFt4tyHG2IuGUHxFEbnZa0CWS04XTxiDv1jlCGur_ttJohQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0fcbc506.mp4?token=tzHGtNgzZ-IyHNlN_Y9YgwnZxG3F7fYORDsY8zzYN1qUE-KV5sbMXi-o4GsyjH9rujeVpq1M3ol5lTe0HQzEGAo_iHD5_5HN_OPgZjX14UHMXPL1x-svAi_-oQde3SDnozOPxrbnguObH8Bw2FIDQFVNb-OyHJJeZw_wZCrnP7XT8lCsFgmgbYM6kEksWJy-H8MdB7wiqy3cWFwFFprjobHj_sP0z0rtsPmGx7ysUXRhS6W3XEmU3mkosWa8bMsuHmE8Iq61-ivGc9OeKZJbn0xKt4AND-CbYs7jzkArFt4tyHG2IuGUHxFEbnZa0CWS04XTxiDv1jlCGur_ttJohQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا لگد زد؛ نیروهای مسلح این‌گونه پاسخ دادند
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/459286" target="_blank">📅 20:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459285">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb97f9367b.mp4?token=QiiXjNVr1GtqnCS4hfjZUDAD8fD7MZkpjSOnuDNkHVOlzR-7AE5TG42XbtlhgS2KktxE4gBPqjPjTQguaph4dsp6qhxjCDL5dsPawpB14GJDfl5KARu_v_mbLP5DpnXbayzaZiFGY3LOPisHQp28T4V6-r_mASIybndqVfHZyNRzrSKrs6d8IAYe0Q7HtgOl5RU0K2QnRExasm3BfQ7z_Hth2D9Q4siYvO7FpF-qh0CdOJbG_cAef5I-NvBddm_4Q8NDbJQCtk7ypIT2ntq2a9_wZAIkCYu2V829Yiy_-Sw8maUbPn-oAFHbUMPne3FQ_TP5H1SOKJsvKblgseZt7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb97f9367b.mp4?token=QiiXjNVr1GtqnCS4hfjZUDAD8fD7MZkpjSOnuDNkHVOlzR-7AE5TG42XbtlhgS2KktxE4gBPqjPjTQguaph4dsp6qhxjCDL5dsPawpB14GJDfl5KARu_v_mbLP5DpnXbayzaZiFGY3LOPisHQp28T4V6-r_mASIybndqVfHZyNRzrSKrs6d8IAYe0Q7HtgOl5RU0K2QnRExasm3BfQ7z_Hth2D9Q4siYvO7FpF-qh0CdOJbG_cAef5I-NvBddm_4Q8NDbJQCtk7ypIT2ntq2a9_wZAIkCYu2V829Yiy_-Sw8maUbPn-oAFHbUMPne3FQ_TP5H1SOKJsvKblgseZt7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین تصاویر از شلیک پهپادها به سمت کشتی‌های متخلف در تنگۀ هرمز در روز جمعه
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/459285" target="_blank">📅 20:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmAkNy0R--0fCraOUOPP8BZ6I9FD_NdhrqXZRBgygRtYv3yCw-5z2ute0IFA8mxq0Q3LQ4FMPR_knCqlaZ5OCha4fHV1A8gNkPoTDROOeiva4V4tH9UucesXWiLeeabEVEULubofmfoo83en70WmEIWCoNA78pHygwcVnYlxllPutU4e9tq_N0JOjtB2itM8TCLnysJL7SUnbXxbsNZApDki22iuRUtvuqBjtrDjkepEdIdlWztzrmgIi7_pCIVpLTm8tIjORkDEDJNBnB5IWPmmN6KOSnPn1tZHlY5j1d2Cb4fp9sGLX6qZ8wZNyPRkX4fgFIS2rouFIYGfrfgCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2uxSx5HGbmU6BSlb3uXFeOqmEF4BCOZSXzLBF-m9vrrclKkkg5cn43gxNcMZGAtoGdAErIu7X_rgpNvy--DOfjDL36cuZ-REHNWQXFazeIsEmggXNj1zmXoV9_kFyYx3E_vpQ3eo6kLyig-JgxBuzrHmH-ZJhKHLa2C80T0Un49K6-Uf6WKhaWHEr5JDAErTPNmDbFcILXoBiZpnF-FMFe8--vJKbAlQlQ5DO1l7WUbEZhYMB84-dtxE-XSdWfxpXxJb-tZ2d3n0G0yNONQ3i6dQjgBwSLHot4QUJGdvn-HFYNKZ7n2x3M8Aa9e-UfbEXNieR8hvl-uvVm-zJcZEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رژۀ کاروان ایران در بازی‌های جهانی عشایری قرقیزستان در حضور پزشکیان   @Fasrna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/459283" target="_blank">📅 20:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار کنترل‌شده در محدودۀ کبودراهنگ همدان
🔹
فرمانداری شهرستان کبودرآهنگ: عملیات انفجار کنترل‌شده مهمات باقی‌مانده از جنگ رمضان فردا در محدودۀ پایگاه هوایی شهید محمد نوژه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/459282" target="_blank">📅 20:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0YXtgqmghnRnmDYcEfcz_ACYmXVH17wpR08JGxoVd_p1M2etmaEUTYNzB8I1gAaS78vqPY3CuFWd8T8zTOTPqB-WTFelEfE5ddTEVUo0MQsU5-89ZcAJ7p25uJ3bzBhSZqyredNYgNVnLSmSxArArLpphISZMQ9IXhgxoXcrHhA99twSHYFVkxXRCY5LoVR_enodXH69CBVJtKm-XMM7NmT1LTwzbnyuJ7rQ8b63dvDtFeYXH8CRRma13Vy2FCEP1EKXlrbhVt1tsjYdoF6V0ezm-xn5W06-nGl3RxMNbPM4236srI0rHdb6tQZm9X237InPST_suiPo8g1NSeqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش بلیت شهرآورد از امشب
🔹
ظرفیت برای حضور هواداران دو تیم در ورزشگاه، به‌صورت ۵۰ درصد برای هواداران استقلال و ۵۰ درصد برای هواداران پرسپولیس اختصاص‌یافته است.
🔹
فروش بلیت این دیدار از شامگاه امروز و صرفاً از طریق سامانه رسمی بلیت‌فروشی انجام خواهد شد.…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/459281" target="_blank">📅 20:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIPyDYN9q8IkrFki4ZX8hXgJw94qKspEjPJPPVB1JkYI9te-z8f7d8DT2NiearKwjL8Srwh6fD61RPyLdG6q0t-sD7M0VUQGqY-3XRf8xFT0NDdQaEQbOvwZ4U-jU9b6ocMmCdzqwM2YbPCJy7ZJBReB7olIukFs0gwPnbNlaZ4xFtPydJdPe6PmdBhUDtFvHyGdmSdR_2R0CHtw00PvsiiKxdrMdE7E63REmK7a_FwLnkmmkVU9S5rEJ6FhGeZo8sDggMqwSctvM0g7QeGp5AWl7Be4arNAAGNbRzurSvNr765IyRmxMrFNZcxesmzuEqKyRhiqwzyXB_nR251hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو آبراهام لینکلن در پاتایا پهلو می‌گیرد
🔹
ناو هواپیمابر یواس‌اس آبراهام لینکلن با ۵ هزار ملوان و تفنگدار دریایی که بیش از ۲۰۰ روز را در دریا سپری کرده‌اند، روز چهارشنبه در پاتایای تایلند پهلو می‌گیرد. مقامات محلی ضمن تشدید برخورد با روسپی‌گری، برای جلوگیری از آسیب‌های اجتماعی ناشی از ورود انبوه نظامیان، گشت‌های پلیس را افزایش داده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/459280" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyy3F5WoFJLnshST-U3ZBR-jEwPtyeXWx94G5sQCcicJysosmDY84ciZKBABA8fmNE3O1B4tYpMvCxcGGOiEph8ULYOoi3k39hmpQwdNdRIVu_JoIe3BGLAWiaQ5u3KCYKvxmJ4XVGTaUsgtvCvypIZVKh2HyB-ZDpc_fYg0ciQb55ijrxTpuWSqxAznX3LAUCtkaRE5TVjF-E9cQEsRCVjl6VQLH1TtOgQ5b1PFGLxTyH6_y9bQ05buUgRUNDeCkxJx9jR_K5vPBnv1t-SFLApiHBYQ8JdHdK_pIIXW0FWtlwqGfmy8SsgyNRagGjU_-OtUpn2yXMq8UDH949hNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم تجاوزات رژیم صهیونیستی در جنوب لبنان
🔹
رژیم صهیونیستی بلندی‌های علی‌الطاهر و نقاطی در حومۀ شهرهای کفر رمان، میفدون و زوطر شرقی در جنوب لبنان را هدف حملۀ هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/459279" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2pDIhgJED1LQ6X6ytXd4Xyi-8oCcz5BvhIYB7IdZwDOGxSiXgtuvGmGzaH2_YyqJ7BwFtuSyU1xT_Apa7csNNlgZWdFJJOrKWroOWGsp2rGMDBkVR7UdSdU4WrizWNLeJUl_mRHFqmg0WWGvqen16pCnDjtsB3YbrXcTI-VYV-Gq6sq0NG-tA5fAmDhvBwZibbP-cmGe8Wb0Wepw6ZPxDdLsa_auosgHJ4n5ihGOVxh5iwiGHpMs5Rd3ReyfFlhVpPVxBg6jrpprOXTmkv7-wbz6MslfSkSrwuZ47N6J4NOOn2UE6sQIgd-MzvFxQ2yZRne7qm0_PkuTo6jxDXfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی حالا باید پاسخگوی اروپا باشد
🔹
رویترز: کمیسیون اروپا چت‌جی‌پی‌تی، ردیت و روبلوکس را در ردهٔ «پلتفرم‌های بسیار بزرگ» قرار داد؛ تصمیمی که این سرویس‌ها را مشمول الزامات سخت‌گیرانه‌تر قانون خدمات دیجیتال اتحادیه اروپا می‌کند.
🔹
چت‌جی‌پی‌تی با این تصمیم، اولین چت‌بات هوش مصنوعی است که در این چارچوب در چنین سطحی قرار می‌گیرد.
🔹
چت‌جی‌پی‌تی در این چارچوب به‌عنوان یک «موتور جست‌وجوی بسیار بزرگ آنلاین» و ردیت و روبلوکس به‌عنوان «پلتفرم‌های آنلاین بسیار بزرگ» شناخته شده‌اند.
🔹
بر اساس قانون خدمات دیجیتال، پلتفرم‌های مشمول این رده باید خطرهای مرتبط با محتوای غیرقانونی، آسیب به کاربران، امنیت و حریم خصوصی کودکان و سوءاستفاده از سامانه‌های الگوریتمی را ارزیابی و برای کاهش آن‌ها اقدام کنند.
🔹
این تصمیم در حالی گرفته شده که اتحادیه اروپا پیش‌تر نیز نظارت گسترده‌ای بر شرکت‌های بزرگ فناوری مانند آمازون، اپل، گوگل، متا، مایکروسافت و تیک‌تاک اعمال کرده است.
🔹
اکنون چت‌جی‌پی‌تی نیز وارد همین حلقهٔ نظارتی شده و باید خود را با مجموعه‌ای از الزامات اضافی قانون خدمات دیجیتال تطبیق دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/459278" target="_blank">📅 20:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOVnOmQ5DuJe1CjhcdLZ_JZz44py3xA_JMsNTox75o7WFxOCcrZ6s5bw57_20SSXjTRTk47A85tu5i1rYzTGsP3XiRt7waMWPCS-rW3l7jaVjPCkYq6DfuqyoxTD5sbah7cth_HF7cp55F_1115WCgab4DSHjcQorkDyNPH2V65IjPO7ybn16Q83Sn8Bu9kCvtLPyj8qpUw_mU4mJoqoNGKVSq0AzuZBJa9KlpSGg0Nz3BAyc-KgvLv390xLR-FBKVOJ6ewgDoVXEHNebEv8Um99smLhRn5v6xZOZfoGIvJMWaCb_HAUAn008lBI2rC7lL6MWxNL-cF24mhDLQP9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردهٔ «آینده‌فروشی» قیمت خانه
🔹
برخلاف طلا و برخی دارایی‌های مالی که تغییر نرخ ارز را تقریباً لحظه‌ای در قیمت خود منعکس می‌کنند، مسکن بازاری کم‌نقدشونده با دورهٔ معاملاتی طولانی است. به همین دلیل جهش دلار الزاماً به معنای افزایش فوری قیمت معاملات مسکن نیست.
🔹
مهم‌ترین تفاوت بازار مسکن با ارز و طلا، سرعت کشف قیمت است. هزاران معامله روزانه در بازارهای مالی می‌تواند ظرف چند دقیقه قیمت جدیدی ایجاد کند، اما در بازار ملک ممکن است فاصلهٔ میان عرضهٔ یک واحد تا انجام معامله چند هفته یا حتی چند ماه باشد.
🔹
کارشناسان معتقدند افزایش دلار اثر آنی و فوری بر قیمت مسکن ندارد. به بیان دیگر، اگر دلار امروز جهش کند نمی‌توان انتظار داشت قیمت واقعی معاملات مسکن نیز فردا به همان نسبت افزایش پیدا کند.
🔹
اما شاید مهم‌ترین اثر جهش ارز حتی قبل از افزایش هزینه ساخت ظاهر شود. یعنی پدیده‌ای ایجاد می‌شود که می‌توان آن را «آینده‌فروشی» مسکن نامید؛ یعنی مالک افزایش احتمالی قیمت‌ها در آینده را از همین امروز وارد قیمت پیشنهادی ملک می‌کند.
🔹
این قیمت الزاماً قیمت واقعی بازار نیست. ممکن است هیچ خریداری حاضر به پرداخت آن نباشد. به همین دلیل در دوره‌های شوک ارزی می‌توان همزمان شاهد افزایش قیمت‌های پیشنهادی و کاهش تعداد معاملات بود؛ وضعیتی که فرآیند کشف قیمت واقعی مسکن را دشوار می‌کند.
🔸
کارشناسان معتقدند برای خروج از این وضعیت، باید با قیمت‌سازی غیرواقعی مقابله و شفافیت را به بازار مسکن بازگرداند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/459277" target="_blank">📅 20:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_TvdGINy8Xuodjkwgxg8zg8rICbIc3Ku8XFlYY65VEqV3QeZMKqGWFY_YnDZZyBaqBXCE2WwxXKn7HHkmCs9KHCGuMKjIkeUe7DcYCA7CdjWmQkqHEOVNNckZVpFJuP7_X2OOMoFwHKuX-3Lqsrc0tAQh2-bj2-mF84R9vBmZ32OhqzkUoutDqv0t5vFHie8MpU_N_J6k77X26PcxWj7JfmrWBct0asGzaX3f_aPZkImIhZMZYZsimX-5q1JPk4d1V4OvU3-KhxRHvmsq8qXubaB8bFSrzVlp4odhWMkST68e4PjmnpZqn3gfPV1jjptnZnwPE5nAC74D-rOPv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ جمعی از نمایندگان مجلس به سران قوا دربارۀ عملکرد همتی
🔹
نایب رئیس کمیسیون اصل ۹۰: جمعی از نمایندگان مجلس به سران قوا دربارۀ عملکرد همتی در بانک مرکزی و وضعیت بازار ارز نامه نوشتند.
🔹
در بخش‌هایی از این نامه آمده: «نوسانات شدید و تکرارشوندۀ بازار ارز را نمی‌توان صرفا به جنگ با آمریکا یا هیجانات بازار و سوداگری نسبت داد.
🔹
بانک مرکزی باید با شفافیت بیشتری دربارۀ وضعیت موجود و برنامه‌های خود برای مدیریت بازار توضیح دهد.
🔹
از مدیریت بانک مرکزی انتظار می‌رود موارد زیر را عملی کند:
🔹
وضعیت بازار ارز را شفاف کند.
🔹
برنامۀ مشخص برای مهار تورم ارائه کند.
🔹
درباره ناترازی بانک‌ها با مردم صادقانه صحبت کند.
🔹
از تصمیمات غیرقابل پیش‌بینی فاصله بگیرد.
🔹
گزارش عملکرد بانک مرکزی به‌صورت منظم منتشر شود.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/459276" target="_blank">📅 20:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
🔹
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/459275" target="_blank">📅 19:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a825933b.mp4?token=Vo9J5xqEuIHjBGmw-S85Y0Z78P9v8h80MEEPGClDrUrmryfZmsAPhLIBJKd-F_9CVM71LDwtf9LGit63VGDMxKMoxSOljM3_aoXiyEaM63R9dMqXRkcUc8J86vhi4po9avdW1F2M4YC0HYYxMeZIRSjDeGxpfIFVZamJ35TetXBMkbsbhaKqFx7MKSBvUhKLjIeiZfxTamKx_2vAYyt86Z0yzGgPbHZ6rr32HSiDk8raC-6-fg8CiiSJyfQX1SkEJBL4En2DE2aUQjlvHGf0ucZ9Zf2adOeKkjiLqe6XjvDeI5ZlAZUXGa_W3ty6kSlz94fTDzyDpTM08Hpf1Hv3kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a825933b.mp4?token=Vo9J5xqEuIHjBGmw-S85Y0Z78P9v8h80MEEPGClDrUrmryfZmsAPhLIBJKd-F_9CVM71LDwtf9LGit63VGDMxKMoxSOljM3_aoXiyEaM63R9dMqXRkcUc8J86vhi4po9avdW1F2M4YC0HYYxMeZIRSjDeGxpfIFVZamJ35TetXBMkbsbhaKqFx7MKSBvUhKLjIeiZfxTamKx_2vAYyt86Z0yzGgPbHZ6rr32HSiDk8raC-6-fg8CiiSJyfQX1SkEJBL4En2DE2aUQjlvHGf0ucZ9Zf2adOeKkjiLqe6XjvDeI5ZlAZUXGa_W3ty6kSlz94fTDzyDpTM08Hpf1Hv3kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ کاروان ایران در بازی‌های جهانی عشایری قرقیزستان در حضور پزشکیان
@Fasrna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/459274" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عامل شهادت ۲ مامور فراجا در سرباز دستگیر شد
🔹
فرمانده انتظامی سیستان‌وبلوچستان: درپی شهادت ۲ نفر از کارکنان انتظامی در شهرستان سرباز توسط اشرار مسلح در فروردین‌ماه دستگیری عوامل این جنایت در دستور کار پلیس قرار گرفت.
🔹
با وجود متواری بودن عوامل این حادثه یکی از آنان در شهرستان راسک شناسایی و دستگیر شد و تلاش برای دستگیری دیگر عوامل این جنایت ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459272" target="_blank">📅 19:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ab3b8a4.mp4?token=ZLIXao1iTfTaG6uqHj7nMHpF_XJQIxmNzl0ERTzduSQDcliufAIgi--0UOhDPoKOXljoC9jW-PfBi8umiGFmpldXA0j4-ATZYsacFOE30IyQOne8KUXjxG4WMa81MSI9KrU173hvLM0bFW51UbQELdgl0k3Eezp7J_GVvgasyXgnQGNvgUbF668i8Gzc-PPMK-TQyOk-jWWXOVCoVZxA07bav-IqUzaNLQ1FB-l4b3A15uucf7gk_tolfnQsaeeM3E1Tj7cpF828M_JKAkZUcKw18EOjKoQbaB0yybyeIjDZd884HBSMTZkIr9K5jmq4Pf_2oc5IAFWtEA_pghB98FvIpoxuqDsT-f33WCpTe-ba0NZAjFsz3HpvnFGYIjy1838YRln1fi1Y2-qSyxwTF40K0l3v2XG0O9b6IO2MtfeLOKEwqiaUmDwj-XxhHgzubgikfbCGm4zvTSJPpmpnChLhActyddVhpcmyQMoXEv9DM5IiSrdSpnW6tO4V6vcRzJxbV-jpRtr-5_kFhD5D9p0-jwaKJ67HDsvzqg2NXJMutffscC7Ww28W9P65XikoD_uP23iRkEY1Be_UUZb2ZB6dX7DOwus-Nvy_VhvpxRLylkGrOGAQYYS8NtWwqGE-89emC5FrO2FWeuJLDuPrIC6ouccsGaX0eB8Amzf11B4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ab3b8a4.mp4?token=ZLIXao1iTfTaG6uqHj7nMHpF_XJQIxmNzl0ERTzduSQDcliufAIgi--0UOhDPoKOXljoC9jW-PfBi8umiGFmpldXA0j4-ATZYsacFOE30IyQOne8KUXjxG4WMa81MSI9KrU173hvLM0bFW51UbQELdgl0k3Eezp7J_GVvgasyXgnQGNvgUbF668i8Gzc-PPMK-TQyOk-jWWXOVCoVZxA07bav-IqUzaNLQ1FB-l4b3A15uucf7gk_tolfnQsaeeM3E1Tj7cpF828M_JKAkZUcKw18EOjKoQbaB0yybyeIjDZd884HBSMTZkIr9K5jmq4Pf_2oc5IAFWtEA_pghB98FvIpoxuqDsT-f33WCpTe-ba0NZAjFsz3HpvnFGYIjy1838YRln1fi1Y2-qSyxwTF40K0l3v2XG0O9b6IO2MtfeLOKEwqiaUmDwj-XxhHgzubgikfbCGm4zvTSJPpmpnChLhActyddVhpcmyQMoXEv9DM5IiSrdSpnW6tO4V6vcRzJxbV-jpRtr-5_kFhD5D9p0-jwaKJ67HDsvzqg2NXJMutffscC7Ww28W9P65XikoD_uP23iRkEY1Be_UUZb2ZB6dX7DOwus-Nvy_VhvpxRLylkGrOGAQYYS8NtWwqGE-89emC5FrO2FWeuJLDuPrIC6ouccsGaX0eB8Amzf11B4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داستان دیدار حاج قاسم و ابراهیم حاتمی‌کیا چه بود؟  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459271" target="_blank">📅 19:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سرکردهٔ شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی دستگیر شد
🔹
مرکز اطلاع‌رسانی پلیس اعلام کرد «الف.ل»، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد. …</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459269" target="_blank">📅 19:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f6782742.mp4?token=nXca0vZDuK1viXJ-jYdNWqPo1EoTqQYsSsw9yqEBmdxm4igrpUUrY6_CBjCFY9Xj1Sage7HtR4kyl7mnMr3yJFA-eAaeEEvhDhArHL8EXNzcDkAVdpFF1vsv29CPv9CLeKYUJkRTOwvL-RQ28epgVZlHchjDT5qfdvnZgUW1kPImoQ4RTzGOYEvIVHII9Q3pQ2N4I5paiIHVojRWwKByGIOm2wyLkDV5E6Ym-pySAnXM9MrR0uYdUAKN3n_djdumoa96I3JLscNQ-K7EwRBh2KNJKv7tzIrgfXyQYQTtEP6CKcCsXf8FJ1Lqh0Oi_NKG13Z93iCvjOH-WCIUg5LrzFW5dsfGEQGRTTwR0ijnJoGUtPzbGBjUhTM7ueLEkNOWa0PWZt4liV3Ed7qH5muxkxp95ePnLV2gIon8TSqhkNZSeJ-i-faF7afkfT_cbcZl-PauSh61plUL41us6j9APwG6aFMm_r9zNrh_nCpQlf4blsbrbaH0x9-Dcqk8bweV5gPYop_sXTKh-1pEkqpxfgwEhU8dxi-i6Yow-YZq4NE-hN9L13BUDaSCx82ZUeOisnqvy57YSEUmalpJD-NCryo4bBaezjt4YJrPIqPz0dlH43HtoPueiq1CEJwso-MkNaB43vTxmOB5KN-50OuSfMvNqKPCtI5hAVpx_ZImz0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f6782742.mp4?token=nXca0vZDuK1viXJ-jYdNWqPo1EoTqQYsSsw9yqEBmdxm4igrpUUrY6_CBjCFY9Xj1Sage7HtR4kyl7mnMr3yJFA-eAaeEEvhDhArHL8EXNzcDkAVdpFF1vsv29CPv9CLeKYUJkRTOwvL-RQ28epgVZlHchjDT5qfdvnZgUW1kPImoQ4RTzGOYEvIVHII9Q3pQ2N4I5paiIHVojRWwKByGIOm2wyLkDV5E6Ym-pySAnXM9MrR0uYdUAKN3n_djdumoa96I3JLscNQ-K7EwRBh2KNJKv7tzIrgfXyQYQTtEP6CKcCsXf8FJ1Lqh0Oi_NKG13Z93iCvjOH-WCIUg5LrzFW5dsfGEQGRTTwR0ijnJoGUtPzbGBjUhTM7ueLEkNOWa0PWZt4liV3Ed7qH5muxkxp95ePnLV2gIon8TSqhkNZSeJ-i-faF7afkfT_cbcZl-PauSh61plUL41us6j9APwG6aFMm_r9zNrh_nCpQlf4blsbrbaH0x9-Dcqk8bweV5gPYop_sXTKh-1pEkqpxfgwEhU8dxi-i6Yow-YZq4NE-hN9L13BUDaSCx82ZUeOisnqvy57YSEUmalpJD-NCryo4bBaezjt4YJrPIqPz0dlH43HtoPueiq1CEJwso-MkNaB43vTxmOB5KN-50OuSfMvNqKPCtI5hAVpx_ZImz0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داستان دیدار حاج قاسم و ابراهیم حاتمی‌کیا چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459268" target="_blank">📅 19:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrtrSs88KUENtNsTPRVfDQH_Il6DSp3JMhgl-xgzoKU608CgTHwGTMbj4GQq-XG2JsIFb6tH7PvKx5eWctOWkJcaJ97ZRiYPPKAncjH7lIZDZn6_0PlR0qmIsQt2v81fJPvZF4zxazPmw97cmbCVafobHXHUqTiFxZeuoXtkFMUYttRxNiL4dIeZR5eplM7FaGfTCsSDji3czabqd3zxFVIWokPmkbJmomAeuNeozlXYKVnyzrllaoVcjmufChc_BMy-i2T9Bj123zH8hElVJx5-V2i4kJS3IngKc0VUaz9JJLWsKOIJq0-kch38ktx35yY4OJ3ldjEQc3EecMmxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_4slxGCtPNzUyS_sVSUtZKDTG8GfSEfyz0lHHNIZmCY8auWTSkTs6waXVJqDsikEMpdDKXP4TCmR1uYOUix39SGHTqWSj07Pk-T0GwuJZPfAo-MDw68jx98Et8rwJODSijLoR858F0y6IVnMP82ZFquhH_W2vkIS-ZJ6ykbMu-COiHBoIdJlPMFTFUCvU6BwQE9AfiTFjI8OOD2RFaKH2leHP02hwbM1b6FaI93HIXHVwCnq2nvMD9RWEN861ol-GRSWb1pj2o6YY1BBTrwtRmDWJHu0SyD-6AbUw8cgL9ISfW_YoRayKvhHhJF__2QAVXvFS6-erLMQBAPuyCrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2H4OlZqmfKP1s4xcVBWqiYQrOyU6a-UuNKiC8xdrBzIsJ2J65eXBbDlDVJmpshhHMAmUsdjBsFg0Yvhe3XzkcgFMuTZd1g_rMpv_dem-PYhsAWFCQRj6_1RBCtlAx8gna5HzyE6B3veKKBM8bbFD34alrBXmUAlEEQH6pU6ug1RpMBIQQ8OItrlq55PJh-8YhX52QhZQGXsVF_-P0VERYrFYW_sHqm-73xKpij5CqWmB45ulinWguHqy58fXvLVpCucB2aQhojG4AsJdtGgGn-TPc0_cSX9jr0DulD0_A2D1Ta47ctU6SLEBsNgSGBukRaj1ggRdOE2upiRXvKjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvKdbKOhFnux3R39ZHxKABTH7sy61QQhM3ZbLn9WLvE4yVhsi6aTLFDZLZxbwTP8Rb2qzh7AbTkztQzJXs5jagyZS5-5u25bKfBcjjf8qSFYQhYX3v8fPndz57XbFXywe8ntbPz3Crjkm4oqZp4OM1xtlVO7hxpHzQQnlApmupW4yl2fXLI6IOnLun3jROjwBGbE-aoPdqbWGUHIDIE1K4cGLT_KnLaQRSpIfQRZYFtIw8k7wDH4bZgFcqqHFCjUlynBX4nC8En-VV_fzaTSrRc-NEujNaluHzsixUb1nVEwXBw9E8uyZBLETzEAgGB9cNWT0iMe5rBj-rsaVxN6Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zlszm8JRQpREYm6GeQaODiH6NfmXHhUcGHsO_Ez3cnGkjtKoOQ_aR8g94VzqvOt04Ky2WeGKOJRyt8OELP-jcpV2D17u1xHazx2-2wtvtSamON4vdhGfuLFcNCXQHXEn0skZCKHs1w6fboTBgCwjEhjsY0BU8NVHmJONkrEiYvo2APyUo-r7tWvaNkgP_U1LEOaHCWoBBDe8FTJ5kWsAgEL0cDRbu2PU-eG47dJUWB0jHVGEhwScsqFilXBAGQPqX6iol0Fv4BD-2yXhMjFs4C9pRoTaUAZ-Zx3VpuQffpsgIgSiLnD-LVLz2nPW4cCXsbKTam0nLFZePBRHO9aoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER-kOcTM4DAVSlGBJIvcvG2pM-8lAxe_COnW5KgVFDI4UGbLfe-0UWGSLmzzQVl_1fxThikVzj7Fel5LdQrwg6BtdxK8_3qLp76sQDD3AEoecCNTXXXzHF6_ClIS5aHLxol97Bfe4AVEyOKa8KbO64MgN7VR8lGljojF-gUMQHcHPth0LKCDHM50oAZVMZMvwT-U1kgS3u6sbOmnttwtGBEq2ymctBcMvytsF5jzkORgzZHF--8jqVRK4WhENlYb3PtR2oNp-KKvKgfE0JBjcs7GNf78-ozEoVXXMkEu1qPm_bZ9n7KVhm5WMoDcCOr8nsUV75papxwfpFKPZJHYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/db1DqlJhD8hM-XAfWXOuEW4RzxJceA9AUI7ilTPIwCM6F5PtGnZuqVR3kER7isPoFfSK0yEFpKqHxgkKKgJfdWRoLUBiTMjuDYNNldWqqWDiErJNla0bsJNFtp-L-K9sFgXxme1o8WFZ4xskvGFywPHu4c3YOEP7iK5rI-QR2DXWXDgNSzc5KjsKtdhfTjfKRdRHodJOcHBpMTRpXbmEmXQ16R7Rv-8tiym1dgSkQL4XWR4WurHcG8v9an725huwYBZgP89FC5NXx-KR_p56bn8jLhF6fyOnnd8REDFXDZuYENpN4aIuwVT-0gh44SyFYq5UErszg0FhtAY0pqADkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید وزیر میراث از منطقۀ توریستی قلعه الموت
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459260" target="_blank">📅 19:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9967b11f9.mp4?token=N8oS3_vZtANvfbbE5gwGB23O5CBqeRJrGLgQtLq2xjQX1ZKklEwDvJ-q9lqEaFgv6GmLOQqG-Q9iVYEStuxrjMrEMhuW2lqDI3V8LPKefCKfg5jxOpr8ydLZyN-bua5BgOuLD3M2rM_8LJjqyVsaDAs_PlXWI449Oz7_rhhqiT_yu0sNbZouMqzzFGtd1CP_kOQSPAMYhuKP6zKt5GNXviaDbhDNpqqNchzSAKxRSs-ZOs_858Ya76lgvP_x0DPW8peuxt3rS1bxmsU_0_7-CoEdDRK4L_s7JAKuYOI2PJUhkAhkqpOm8LuL-NtsdI-ab3ELhPhnI3nn92I22t6yq5h8juLnjs8YfXVCW_o0qcc9UMBBScgZACpSvtYFFB4K6jHJYYpbk6E_cKn8-OBfQWAxAjOmqgSrtZ95RRVDTbrHwHFDLZrM367vWUhC5opevH0K2rDjVwil4ci3-kYL8u8YQ4lJnczqkvTVVjqLczJQi3nfmfYIteE3hF7jGr5mz-364XfYDZDAoOUd_4cZSyn4164B63bCxPNg9yImpFVUCw2XTNtvQcj9BkKHL-iGIhuvA5mV7rFsrmQM-so8mo8gpM9xLCaylIBpRk7gNIk0Y3vA-gThFiIpeHrqW0CVA_x1njSQAfGKcr023-HAhuQpAzS0qTjJcfdqn34FBwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9967b11f9.mp4?token=N8oS3_vZtANvfbbE5gwGB23O5CBqeRJrGLgQtLq2xjQX1ZKklEwDvJ-q9lqEaFgv6GmLOQqG-Q9iVYEStuxrjMrEMhuW2lqDI3V8LPKefCKfg5jxOpr8ydLZyN-bua5BgOuLD3M2rM_8LJjqyVsaDAs_PlXWI449Oz7_rhhqiT_yu0sNbZouMqzzFGtd1CP_kOQSPAMYhuKP6zKt5GNXviaDbhDNpqqNchzSAKxRSs-ZOs_858Ya76lgvP_x0DPW8peuxt3rS1bxmsU_0_7-CoEdDRK4L_s7JAKuYOI2PJUhkAhkqpOm8LuL-NtsdI-ab3ELhPhnI3nn92I22t6yq5h8juLnjs8YfXVCW_o0qcc9UMBBScgZACpSvtYFFB4K6jHJYYpbk6E_cKn8-OBfQWAxAjOmqgSrtZ95RRVDTbrHwHFDLZrM367vWUhC5opevH0K2rDjVwil4ci3-kYL8u8YQ4lJnczqkvTVVjqLczJQi3nfmfYIteE3hF7jGr5mz-364XfYDZDAoOUd_4cZSyn4164B63bCxPNg9yImpFVUCw2XTNtvQcj9BkKHL-iGIhuvA5mV7rFsrmQM-so8mo8gpM9xLCaylIBpRk7gNIk0Y3vA-gThFiIpeHrqW0CVA_x1njSQAfGKcr023-HAhuQpAzS0qTjJcfdqn34FBwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خارگ است؛ دژ مستحکمی که به هیچ متجاوزی رحم نخواهد کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/459259" target="_blank">📅 18:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459258">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvjF_eBYm3d8Gp_461eP8lJBzmU5p7aDQlhaJRB48g-xf_xDt4ZWZm5uMzOIHGjTi_dMMHXYxVpg7CDcfsRYMGkJCEDe1TYUJl8quIkZ6_jehdi9Z_heyAhorvmL9gUDicapIY-Mk3t1F_x_-eaLDBnq4DgkoV-uz910zIm75BzzItUuBSUJ7aUAuq94hrR881w2Ie57nNlqMlYpMSI4jPHuIxsRpx7VKGKluAGEFgP-0bNo0R-GJjHApVrDDivhN9lHEVT64Z5LArwCVkqWVkg-_y59tYIQG8UJ6BCgIo2hfPOYbigIK252EMPsISz_GR64Iy0iiaeblxtrS7JCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون سخت خودروسازان آغاز شد
🔹
رئیس سازمان ملی استاندارد فرزانه انصاری می‌گوید استانداردهای خودرو از ۸۵ به ۱۲۲ مورد افزایش یافته و این تغییرات قرار است به‌صورت مرحله‌ای پیاده‌سازی شود.
🔹
خودروسازان باید پلتفرم‌های خود را به سطحی برسانند که هم امکان تولید محصول با این ویژگی‌ها مهیا باشد و هم زیرساخت‌های آزمایشگاهی لازم برای آزمون و عیارسنجی آن‌ها در داخل کشور شکل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/459258" target="_blank">📅 18:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-l-ClePHCABtVScoZ0JYCXAOWD75NAFjSEM1giz9U68nwqmvELDDKpKD2pWgZhdJQLPWzDWL8CKx3unZDeA22qcOsQedGCUjdb0GlBZykYOTBqfpRA9mbk93SosuD5exjxMwVyo71JOgsoBPoRtwy7_oIDQphr_veWjJ7e7Ooa6VF5L0vhREgW00nifKe4-inthioCeowrVyhT2tXSZx1zNXPOr3hzzsKcoXlDdVd7PA5Y7kYrqk4CCBBV8yWR-hz_iaUqK5oZpT9SBxn9fbZFlRsIS-ZvfkNZWREtqt3xhUx0iDbqEZKzkLHLYkIg__l4HJgqoTqUNLNO87FtVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت: حقوق بهورزان ۱۰ برابر شده است
🔹
ظفرقندی، وزیر بهداشت: حقوق بهورزان طی ۲ سال گذشته افزایش ۱۰ برابری داشته است. باید توجه داشت که به دلیل پایین بودن پایه پرداختی بهورزان، حتی این افزایش نیز لزوماً به معنای یک رقم بسیار بزرگ نیست، اما به هر حال این افزایش در پرداختی آن‌ها اتفاق افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/459257" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcvOf3XCQaBylcvw_DOgn2h8Xb8oIkTugD4B_E3H1cKRTdI_PyRxoUIe0AItJJ1qMqSBtSx8i8FSmbiO-q3ra8LGp25P_FsVfpqy6WbnXB8nwMTStVp9R638mX_h08EDYJH2xH_l06y-7SgN2Z4ABeE-np0ZXC4SnOQDDOj09-RVxO7LoCdUEemZZewkKoG6Ai9DZ6JOH_ZkZuxsEkj72B3yqbeaqu6TvkPic01tmk8eBHHcjMx8HMjtcUfyHbp0ifG9OArcp749woZZMFXw8wbtHDQ_xTKeApT5SS-OnKuBwF86GrwjXVO9VM0MpDep2mqJrtDnNQ5gIV9yPFo1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا فاتح جام‌جهانی فوتبال شد
⚽️
اسپانیا ۱ - ۰ آرژانتین  @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/459256" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN3UnzkSe0YJ2LRLfEoe4nQTZJdLcugTDgtVW8CPQR_PQg3r32Bt4dxpa_ClRXxobp7B52ZfWnUMCG74OPrtW-8K-9ChjannQvJST1RHRrwPxL5y--ShgXw8MyE7Na91x7fvBTFs9irvvaVLbuZgSjZHtGJYhswxNZvyBLtD0vGn6DdXBZzQKj8Px04uz1GrBlxzcPnXb5X1pzKQEPC3RxueAay2Xc8kx8yITK2Q78vqHywL3Dhylzsoei99LmtPmmUiJ-sikVdVY14XXPV6dObrYnLKSrgbZixnyGU5TXAecb1Vejuh30-Az19nA_ltWe7588C7ZU6i9kZ_N-KOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در آیین امضای توافق‌نامه بازسازی پالایشگاه پنجم پارس جنوبی (فازهای ۹ و ۱۰) مطرح شد
🔴
مدیرعامل بانک شهر: حمایت از بازسازی پروژه های صنعت نفت و گاز را مصداق جهاد اقتصادی می دانیم
⬅️
توافق‌نامه طرح بازسازی پالایشگاه پنجم پارس جنوبی (فازهای 9 و 10) میدان مشترک پارس جنوبی میان شرکت نفت و گاز پارس و کنسرسیومی به رهبری بانک شهر با هدف تسریع در بازسازی و بازگرداندن ظرفیت‌های تولیدی این پالایشگاه به چرخه تولید به امضا رسید.
⬅️
به گزارش روابط عمومی بانک شهر، دکتر سیدمحمدمهدی احمدی، مدیرعامل بانک شهر، در این مراسم با تبریک سالروز ولادت حضرت محمد(ص) و امام جعفر صادق(ع)، با اشاره به نقش بانک شهر در این پروژه ملی اظهار کرد: برای این بانک فرصت مناسبی است که در همکاری با شرکت نفت و گاز پارس، در به سرانجام رسیدن یکی از پروژه‌های مهم ملی کشور نقش‌آفرینی می‌کند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/459255" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459254">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF7AFsyDsOckMW5gCmJ_vDSGbpiO0Cx_M7NsPCsFUhnci9sn6COrbv7pRduH3MvrHbW4qhXWNuCqZDbZRsWxQ7Me9Aw1sxIMzXHvb1T9QaVhFSsreGUn3iqbhOm3YXY3frKSvPvqN3RHaAYq-XrdtYIHwsRPY8TLpgGQaKPm2CCdtTFEVJ5_n-nw8__Un9521E9pWoCp0Jq9dcLq7XR_B3VDhFEgR2x1zSefaNzvth8E2IiFXHQiky0g8VI788wpeGDqkGUCUynUghI_HAfaUITZFKMHYyS9RYqm-9C_37ij0-BDc2VvoeYWDyKt2OCHHz2HpZ4R6ruKp9XDfT-5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشتوانه صندوق طلای رز ترنج چگونه شکل می‌گیرد؟
🟢
از ورود طلا به بورس کالا و تأیید اصالت آن تا نگهداری در خزانه و تشکیل پرتفوی صندوق، مراحل مشخصی طی می‌شود تا هر واحد صندوق طلای رز ترنج، از پشتوانه فیزیکی طلا برخوردار باشد.
🟢
این اینفوگراف را مشاهده کنید تا به‌صورت کامل با
نحوه تأسیس، امنیت و پشتوانه صندوق طلای رز ترنج
آشنا شوید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/459254" target="_blank">📅 18:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459253">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/459253" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459252">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDELSFvsNAWljVDwBEhak--ATZ-htWZL7frI2ri9EuOXJ8Soya8oJyei0vM9OGP_ANROqfoNzYrP8xCAT0gsq5mczirmM9lQJS9lP_vQC_yQd9m4UzPIC4lj_PMEUVOlz8lEz084dlS8gnsowZnfKosOLE3MT8pdTAGnL5-8XYM38LFD08e6Wi89Cl_oXVwoWuivetmMBHTmwaAFcwZ1MHDkGfg3uSvwdfSiz7E0hF4c3fhp52qjlk6v7yFRCDtmJVlOqePgRF7dohMLfZrWF6TBsruYpE6WI2OVZa_9UcjR7y7ncnWrz44VIePc21TZlHdgf79ACMFHyO9nS7BAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاس گل شانگهای به پزشکیان در اوج تهدیدهای ترامپ
🔹
روزی که ایران به سازمان همکاری شانگهای پیوست شی جین‌پینگ، رئیس‌جمهور چین، این عضویت را نشانهٔ سرزندگی خانوادهٔ سازمان همکاری شانگهای دانست و همان زمان گفت که چین آماده است فرصت‌های بازار و تجربه توسعه خود را با اعضای سازمان به اشتراک بگذارد.
🔹
در همان نشست ولادیمیر پوتین، رئیس‌جمهور روسیه نیز تأکید کرد که «اکنون وظیفه مشترک ما این است که به همکاران ایرانی کمک کنیم تا به‌طور مؤثر در فعالیت‌های چندجانبه سازمان همکاری شانگهای ادغام شوند.»
🔹
اهمیت حضور ایران در این سازمان در شرایط فعلی حالا بیش از گذشته است؛ چرا که هم‌زمان با حضور تهران در کنار چین، و روسیه، آمریکا بار دیگر از تشدید فشار اقتصادی علیه ایران سخن می‌گوید.
🔹
از سوی دیگر مسیری که چین برای همکاری اقتصادی در شانگهای دنبال می‌کند دقیقاً در نقطهٔ مقابل سیاست فشار اقتصادی آمریکا قرار دارد.
🔹
این رویکرد نشان می‌دهد شانگهای صرفاً یک همکاری سیاسی نیست و در حال ایجاد مسیرهای موازی برای تجارت، انرژی، سرمایه‌گذاری، حمل‌ونقل و مبادلات مالی میان اعضاست.مسیرهایی که می‌تواند وابستگی اقتصادهای عضو به سازوکارهای تحت نفوذ غرب را کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459252" target="_blank">📅 18:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459251">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سردار نقدی: بیش‌از ۹۰ درصد موشک‌های ما در دسترس هستند
🔹
مشاور فرمانده کل سپاه در گفت‌وگو با المیادین: بیش از ۹۰ درصد موشک‌ها هنوز در دسترس هستند و موشک‌هایی که دیگر در دسترس نیستند، موشک‌هایی هستند که ما پرتاب کرده‌ایم و موشک‌های دیگر جای آن‌ها را گرفته‌اند.…</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/459251" target="_blank">📅 18:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459250">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سردار نقدی: بیش‌از ۹۰ درصد موشک‌های ما در دسترس هستند
🔹
مشاور فرمانده کل سپاه در گفت‌وگو با المیادین: بیش از ۹۰ درصد موشک‌ها هنوز در دسترس هستند و موشک‌هایی که دیگر در دسترس نیستند، موشک‌هایی هستند که ما پرتاب کرده‌ایم و موشک‌های دیگر جای آن‌ها را گرفته‌اند.…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/459250" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459248">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfmxIzD-v2PHfUgrp5LfHEu-qz-xlib4DIp1X3aHd_sVs1H5D2WPgTOwt-xX8jiYoyD3CuRpXcHL-JZBRGrWKTwnnNLKWGeURA51atNGTxR9GnbQhVAWvPpWJJ3A4ozJyrsW46cybp0lKx9ymlBtplxOMnEDjz5vtICiJZAMUoYp7t20Ht4_cS3TMJLhOcRiC2fd34mjgNCQXuWlnpmjQi9bBPuxxeCfZIYUNxdGZFFz3n1jWL1AIjy8J8TJSM7ZdGhSLWttX3jXT1xH6EJKAsPzihB4CtB8FuT9bqnsKMp2aGGY3-1p5_DzMNAehADTnhEhsmX6Szh3zHlTzFpTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: بیش‌از ۹۰ درصد موشک‌های ما در دسترس هستند
🔹
مشاور فرمانده کل سپاه در گفت‌وگو با المیادین: بیش از ۹۰ درصد موشک‌ها هنوز در دسترس هستند و موشک‌هایی که دیگر در دسترس نیستند، موشک‌هایی هستند که ما پرتاب کرده‌ایم و موشک‌های دیگر جای آن‌ها را گرفته‌اند.
🔹
ما فقط یک نقطه ضعف داشتیم و آن این بود که برخی از کارخانه‌ها و سایت‌های تولیدی در مکان‌های شناخته شده و روی زمین قرار داشتند.
🔹
در ایران وحدت وجود دارد و رابطۀ سپاه و دولت در بهترین حالت قرار دارد و بسیار قوی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/459248" target="_blank">📅 18:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB-Sdmqeus-bamt0Hu5U1A1djmQ5_SuGH_ONVzuqEBjCxBglVeiZlt7sgoqDbBPL4oHyvtj5bEaMIOvSTxoljMFFLSD18RQBT7qY5RtEdfRYsBq-zB-8ShfMFReka-36NTrcGUm0MlZPGafkqw2iQlaBYGgRqNvg5_NTLobrenxhOMl3p_OCeT1CesdXKWg6u6YTjfQVJSXmXuUiTVwc7hZkhzemLNqNOFlrySNp4K7aEVMD2VZs-NzXVwJ5-vU37qt4NU6g2dySV0THW0azFtxkVAhoND37q-koCfq7vm9Z5AN0KxOTmuUvFBEYEB7NsV9hUiR3XGPyGigLi8NJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش پیشکسوتان پرسپولیس و استقلال به جنجال اخیر علی کریمی و رضا پهلوی
🔹
بهروز رهبری فرد: دعوای اپوزیسیون خارج نشین را که دیدم، فهمیدم همه چی مهمه جز خون بچه های ایران!
🔹
هاشم بیک زاده: خون بچه‌های ایران شده بازیچه دعواهای اپوزیسیون خارج نشین، واقعا شرم آوره، حیف از جوانهامون.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/459247" target="_blank">📅 18:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459246">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDHOj9VLBexUDJy51PcwwLIIdmN3OGuCMaMpeBU6MQPuBroNsOJK2vc2IrXICaV-BEFeI1RYjvOvnHjC2fE2YCy-bwAz1rK2k_qZ3co4r-p0Sc-KDm3NeBtNk4AdAiU6POg-viqKn9ew9JGhSL8eYSPReF-Ii56K-tfUeUrPQ02LkH4K_HibNjvB8_scTcr-5imSXRCPQ1Mq_qS955GJ9xzfnW9uxp0k3lQaJmH2qSwvfOMw_Ewk9q3mhpqkrzZ5xvE94BIXyVJL0gThC49eXZklD_3-oMVElftC3ME3bYnJ7VKHuIHFK9-WCr8AUQoyN8asBPngYWULm3tR93mVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
اسپرسو با احسان محمدحسنی
گفت‌و‌گو با احسان محمدحسنی، را هم‌اکنون در
سایت
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/459246" target="_blank">📅 18:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459245">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVCtVaeRGNg_tJ_4Ke435hxlHU0y3TAUDharOELlshexqXGMsqVNj3nfKqRATe1DDEKi5cofS7ym0j_0p8YsLhyHz-CXLGrR9CCNvhe_gu0MNW8gT80UUENEhf0FOfdjZvuIzGKrP2KSCAPJ00JgVZyc-pLe41GpvRh72Nr9Arc94v18nQLRfSfKys8JoQFoOwcC73exFVqI_h-CioNVqVAu9RuSrl5GjK0ZUIdqCeym1XqnZ8hALJ-7c-i8gfYkoWB4p4UZ_uSc_ludPgjWc70iMqMmEoS6NuVno8BLV_iGXanjRw5uNlwvM2CpwRXCwNG0H2TVSRJDABwCF9vDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان با رئیس‌جمهور تاجیکستان
🔹
پزشکیان و امامعلی رحمان در این دیدار، ضمن بررسی آخرین تحولات و روند همکاری‌های میان تهران و دوشنبه، بر ضرورت بهره‌گیری از ظرفیت‌های موجود برای توسعه و تعمیق مناسبات دو کشور در زمینه‌های مختلف تأکید کردند. @Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/459245" target="_blank">📅 18:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459244">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/459244" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
