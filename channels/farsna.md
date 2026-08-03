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
<img src="https://cdn4.telesco.pe/file/C7vkidNe9JAoRBpT8-7iaV8s8TPKvSpEVCT6mfTU-f-8OiR83gb1fh5t3wtgXqNKnwxxGGwBQQ9EbgdZFcg_t3uYD81Dk-jyFuMY2dMoMiIE_pMSz_vCEwhZ0NUqtYN17TAHG2asXb_rRfapLOoDnAn4LghyuIFfETlDThFLBE7ruNLQ81lAXBrytlbUc4QL1eo3qDu4rC6CrHYREWpl9Tu1H1jfeS9LR04qjcMY7mYSNr9PEqKxl8rtbe0h1SWC0XWaa6x_-P-ZBcZGaru3ojXg3FLrBdPmWyRnWzkzxloG3-YBkKnwL3HjlhzVAy1_DGCMFeHtQiFnfhDAL5f4sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 04:34:08</div>
<hr>

<div class="tg-post" id="msg-454139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c670bd2ac5.mp4?token=jch5kdP9zmJq9kEvLW8GI_nx03ZRUb2ZqA7bX18NU_WsR4aZD4ZGn9EZf-wBBItwlJiN_Uh0FehkZ26NLahgk5vyXaxlAR-09-dgLmhFp_4MdOCgbFtz10td-SWeUxfIgOZugSIGq2OFNIz81fjQw3Pe3ysRcnLLM1xrx_Sa4FUe15ZtBX5e-kVNKATaXH0J8T-X3dp8Nwx0L-R8fnPmvNcBYA6ZsfuSS-fxUhvg7j4lJxlqg0J1GuLSnJbwBXsO7hMNOUzwBOvOwFolXdAv9_JyELG_Eh0K1rNKrJE5fYQOV32sa8PJ7O_SJUOO9Rtf-M9iV_-4PZ2H3j4b_iSquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c670bd2ac5.mp4?token=jch5kdP9zmJq9kEvLW8GI_nx03ZRUb2ZqA7bX18NU_WsR4aZD4ZGn9EZf-wBBItwlJiN_Uh0FehkZ26NLahgk5vyXaxlAR-09-dgLmhFp_4MdOCgbFtz10td-SWeUxfIgOZugSIGq2OFNIz81fjQw3Pe3ysRcnLLM1xrx_Sa4FUe15ZtBX5e-kVNKATaXH0J8T-X3dp8Nwx0L-R8fnPmvNcBYA6ZsfuSS-fxUhvg7j4lJxlqg0J1GuLSnJbwBXsO7hMNOUzwBOvOwFolXdAv9_JyELG_Eh0K1rNKrJE5fYQOV32sa8PJ7O_SJUOO9Rtf-M9iV_-4PZ2H3j4b_iSquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
برافراشته‌شدن پرچم ایران در بین‌الحرمین   @Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/454139" target="_blank">📅 04:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">زمین لرزۀ ۵.۵ ریشتری در فلسطین و مصر
🔹
مرکز جغرافیایی بیت‌المقدس: زمین‌لرزه‌ای نسبتا شدید به بزرگی ۵.۵ ریشتر، جنوب فلسطین و مصر را لرزاند.
🔹
خبرگزاری رویترز نیز گزارش داد، ساکنان پایتخت مصر زمین‌لرزه‌ای به بزرگی ۵.۴ ریشتر را احساس کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/454138" target="_blank">📅 04:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCu-XKfWo7fg3zJa8ivRoZRbbHg8f1VEowfT1YN7dKyasAHIkLjCRluJ3isgeHdLWiuOHrjDnO0Atw-q1pW8d3mx7OIhNsjO3CW3L01rkyhOYCt0oBvzHi0o9M4HVzyjeIRkbJarLc4PmDQAeZjgEAQ4tHOP6D0EoZCXdRajBOrnmeJ2KMKO30gwa4vbFBzJw_azs2X0fhlhWm-sahpn18-viJl8do3hAU16PueqagKZzTdm4JA9qFHXho82_6FJJNmF1B_co7pbnKaAdB-TkV-XjxHf1MjSY4F9bJoj_a-K2FVx4nan2dv2WbFV7QkUXlljiSClCjtJwIK2zxFtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش بین وزارت جنگ و ارتش اسرائیل؛ ارتش از دستور کاتز سرپیچی کرد
🔹
درحالیکه وزیر جنگ اسرائیل از برکناری فرماندۀ فرماندهی مرکزی ارتش این رژیم خبر داد، ارتش اسرائیل از این فرمان سرپیچی و تاکید کرد، کاتز هیچ اختیاری در این زمینه ندارد.
🔹
روزنامۀ یدیعوت آحارونوت نوشت این اقدام یکی از شدیدترین رویارویی‌های علنی میان وزیر جنگ و فرماندهی ارتش اسرائیل در سال‌های اخیر است.
🔹
دفتر نخست وزیر رژیم صهیونیستی هنوز به این بحران واکنشی نشان نداده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/454137" target="_blank">📅 03:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کشف مخزن و انشعاب غیرمجاز انتقال نفت در استان بوشهر
🔹
فرماندۀ انتظامی استان بوشهر: انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی شد.
🔹
تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات توقیف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/454136" target="_blank">📅 03:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6sADxoa-KildI9FrFH7J3o5cUPHVdEJVBgrbMri7SUu5TCZ4bOays8mXrAYesjGU8b4DUNYmOTsZcYjW_s7VCxct8e0OUniQlgZaNACL1fJfYWO2VFslXqfIUzvxCfIJ6jKBErh4pEkcO2aH10E9HlfS5xRBZ81vBmoISnAlzS7UUzuXaLmM3SowbgEXIiLPKDZvEGweE-7fRLBjdczpW0a_voTcehumIOKBCkPuSGXLeEvdmiWj6ws9igYGCi2ICvAiTVHifxTClmt4rwTfi8wS-u00aQLHqj-Ognn5kecICDysr7EOzw5IjwcTv_yVSIuI6oYPElqFz_l-1AphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب فروشگاه‌های کالابرگ تا آخر تیر تسویه شد
🔹
در حالی که برخی مغازه‌داران طرف قرارداد با کالابرگ از عدم واریز وجوه خود گلایه داشتند، معاون وزیر رفاه اعلام کرد تسویه‌حساب با فروشگاه‌های طرف قرارداد کالابرگ تا آخر تیر ۱۴۰۵ انجام شده است.
🔹
همچنین وی از الزام فروشگاه‌های طرف قرارداد به اتصال سامانۀ صندوق فروشگاهی تا پایان شهریور خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/454135" target="_blank">📅 02:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glqGilF-2tHoUBGN95Fax3zSylNq0gnGKmF_KPirBXVAZSPG6qvrBKNmjbKFn7ljVFfKRGzi7OfaBIQoawOuHp-gbpTANACGjk_XwLTbxaLE2IdjktQw_olKVogNZbUAKzmuH8ubLDkkVYaE7LctHFbxNJEROK2zA2T6vJpdrxMN7HuPN-zsYm_r2R6pWKXbzVvRnEZUeBfbeigAyd2BORKgKuaDrn0nNeIwRZmPbtpX7b_h9i9gTWnHt57JDLQ6wTfgv8xNgSlMOwxDLa0SNnzj66q0bU9sRaXk0PDCmMOtnn9uzFgzskRnTNagZRXqKZDx4BTR1mBrU8YA4iGT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه تختی هم مثل آزادی شخم خورد
🔹
با اعلام مدیرکل ورزش‌وجوانان استان تهران، ورزشگاه تختی به‌دلیل کاشت چمن تا حدود یک سال آینده آمادۀ میزبانی از مسابقات فوتبال نخواهد بود.
🔸
سال ۱۴۰۴ چند بازی استقلال و پرسپولیس در این ورزشگاه انجام شد که اعتراض کادر فنی و بازیکنان تیم‌ها را به‌دنبال داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/454134" target="_blank">📅 02:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
وقوع حادثۀ دریایی در دریای عمان
🔹
رویترز به نقل از یک مقام دریایی انگلیس از وقوع یک انفجار در نزدیکی یک کشتی، در شمال‌شرقی خصب عمان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/454133" target="_blank">📅 01:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادعای ترامپ: از دوشنبه مذاکرات با ایران آغاز می‌شود
🔹
رئیس‌جمهور آمریکا پس از عقب‌نشینی از صدور دستور حمله به ایران در اظهاراتی مدعی شد: از سوی عربستان، امارات، قطر و حتی ایران از من خواسته شده که حملات را متوقف کنم!
🔹
وقتی متحدان درخواست می‌کنند که حمله متوقف شود، باید بگویی بسیار خب، ببینیم چه می‌شود. متحدان معتقدند که توافقی در راه است. دربارۀ تنگۀ هرمز توافقی وجود دارد و دربارۀ موضوع هسته‌ای نیز توافقی حاصل خواهد شد.
🔹
ما درحال مذاکره با آن‌ها هستیم. این مذاکرات از فردا بعدازظهر آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/454132" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NngK398En3_DsXUWoiOhJc_WGY_7nHexG7X7GkAHsunhxDA4VhkGh3m4nQmd7sPWNuE7qjSXVuueCZIWXl6_gB-1hoAekXyqZ5qPHFatdm-WlXIXe5VYD6Rq3lwW4Aif77Nm3JkH-2rpNyjdidiWO2x0DXkImx7kCkJRz5jQuUISKVQSLTsJzC_BMa_N4e8LW8tQD9XWRY1Cv5vKsHIqNVwGP_hQTkMlOz7nHK0z5xziFv8XlWctdJri4NY7DswtLBdy-LDTtx5Hap_-1wGi5S0Yvld1JlBBXY0t6FxMdp6aj2iuj-JIYnAGfEp8fD3LKe0kQqq5ZnaHXTbfYcbUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکۀ آمریکایی: مجروحان ارتش آمریکا در جنگ با ایران به ۶۵۳ نفر رسید؛ ۱۷۰ نظامی هم ضربۀ مغزی شدند
🔹
ای‌بی‌سی نیوز دربارۀ تلفات نظامیان آمریکایی در جنگ ایران گزارش داد  شمار مجروحان ارتش آمریکا به ۶۵۳ نفر رسیده که از این میان، حداقل ۶۴ نفر از افسران ارشد بوده‌اند.
🔹
این رسانه تاکید کرد اسناد و داده‌هایی در اختیار دارد که نشان می‌دهد در حملات ایران دست‌کم ۱۷۰ نظامی آمریکایی دچار آسیب‌های مغزی و ضربه به سر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/454131" target="_blank">📅 01:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnvvN-u4IXtag8Qzkz0G25AL6zHPb7gIoWbX_A-yrM43Xp7X87gJjgm7QY2FM7VIrL72msgen3U7bd7yX5iUJjCzwOrMkN-3OHc_MmpDQ5qYij7O8O7TnQ0qB9dLT5nIHOg-ATz1RXwPWLbaxIR3Xz1OF6AHfR8cN-U248ptWHY6fsrnjlEPx4-aiv5eGfu12SY2k1FpYqficRByER23KVBsxo1tS1uTTsuoeB9PzBflqOD8wH-tQ3-68ILgbVYX_X4aMfSf-E1Rati8RUqca-IOz351YAbqJcBb6Ej__vXMdevOqbqJuFRawPXv5vKqWQ_unHQFB-yvHqHsmEZn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP79Dsyb6vlBHiLmzRNO58JG6UHowB_zJIMn9RLG3Tlq4q1xRrFG3CGmhFqph34-rIT_9C-hIVtcNOLQ2IQvAlOsYyP3fI5qKrr5jiaIEx6AEbiVMguQTAToGUA1HkO6RT5nG_nrJURB3UOifIP2wA98TSLBWzJS135ukIvk9vbTskz6q8j0x6NxGMslZaztSEhWqJmsfTEF4SMzD8WIKz81cfldfHl43r_5b9PsL8rdhvD03v-fSJQItEgzkJL8BCQSIF7mguYnNwKCiSaSKPntVAKHqVAWBHjWapmoIbOtSM_6pLBh8WWIttLNWyOI1BdfghBbgbde0YDsEuSIAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQlB6Ja8yTjvfWCAONZpDaLWsIv6AU853_9de4028JZlFK-JXNKCY54vs4kPO3BLWhLnzlrm53I3GRk4IYqORmF_IDB5Ci-n48tPTCZu_gRbRdsT7IvuN7L1TE2kTmTkmGqzXl3PpWVwNFUx5eu6Z_ivD5pzynuCw0zigeL2gMxb-snSDCoNCJq6QxJ2qBcb-dTAY0ak3eBWup42BI9CaugvssuTzG57BFDuXvkJd3xoNtXmymaVPWn2E4-ZmTfWlBO7EjDdKKJblRutU3IYjsk-CQSU7vquMTPf-QkbLVDNQH0QurCAHW7INTXwBvM0FyHG_NqGJkstwC5iZfr-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qm3kygWBaGbpA_qnLNzdlbwR_gkQIfJ9nnfWSxF5238SdUTUefEH2685yNlCqbbegKzsMdj1DgAuMSNuA_BqomEApdbZMy2qWvZfqeB0vXzbAdYZ-QkRKTeJVQpH0mC-UozDawziQPtok98UMMQpKfVOpQZoupFW30Tp3QKalKOH12_4mpda9uCoK-ST-6aki9wTD_PtWTtCMmX241rhM4hkoJit1sLjDpyGnceVQwp46_ialzSc0KGEHBmrkMm0q3DOx6IFcFTGM00jla2ZBJGILmIsXivvmpEwd0_MsI2T2WydbZSgc62DtnFOv9K5E256lm2QHHJkdKg4zFoofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-Y7a_YNInfprbwuAd3qIpgqFfZlkSrUV1fP1C2-k-NS_-vJWoqyFkS5A7kL1IpgsLXHhrM9u_MWKCZTQK1Vv4n5O_b63MCGW6oEcWVBcSkgHWcjsvsjin5igJtNZB9Oy1mFPaY45BmpRAGRVxA37vApEa7nF2OVeX8WRO8e9-kLW6QCKpOOwSK1Fc38nEr3twmWsrrYRFJBI9i-8F2CD2EggovkyYk0i5WMmmVKzWq-ssUU7c9XGE9TKYMHGnucD_xzb2i5ODH7rujozhKT2082WhcDQYy5o-ehBo5StffX08jjWZMdJPb-vjd9Og4EDEHMtZc63XnWVN_iz6Wd9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۲ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/454126" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454116">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtkZk7mnSeYJLqfoYVd_Wggfh1vVGoTHVxADGWzpQ_ohWtf6zrYw874kCKRltMS4FvCq0PNzgMtXljReGmVkY8fOVqbzZzCU2JzY3Oyd09pZgJD0VVOmJrofRz9CXKxk8lvaY4jOKDRD-2Y4C3lEWzzsavB0tx3wEZocEPO2FkLvXbK8dXKtjDLaCbyAieh8rPkPj92eIW_Yorpr1fX0KuB9V2NSYKulslj2exUxTQPkztKB1y_GwO6R0d_zC0WvoWM9gx_MfCfVhJamnDfXWKEh_z_myM0nzIUTFbMWgaN719ip6g0Jp3CKWf3TqrJ7kRpiVkHxNjpvSUO2WW9eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEzOg6AkSrfq1z5xWOYiUj3jlQR13SLdOltF14SZhTwAgj5N0rPMNXJ_t9CTx99I1QIDfhzmgPfjanKcBe-90aD8WiwLm9xKRfhoXDW9UXeXcr3Tu625joE5a5AFpNeDXA06p8eRPp-LBufYVsTfJ_Rxnf-I9M-483FBnnPbyiXPZdflo8SeYTyc16K3Ooparpz414-xsjXnrA9Hf7_HV2qiMHh0-nK0kR_VmiZeVbHJhifMCTdQHKyHX0qn37Ob-IT4mQ_AKiqFR7LsWxkRV4KxxMyFYtJ0smixdHno2lCrrLzN21Pq2UcM7wjZ-u7KNMVhEz88pWfbNq5BMt8bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3wz1EInNDOlbWwtnGhrZHtTeKG3N0la7OH7F-xwSAJhuWbTR4_nu46UMqP4YowpFznhvAFoCpQ1fqthVsi9qhT1jt6PhORgv0Gc4Ayyd06dJ3sUsCyOGADdaCDDiYVA3fOJ7xzC0CN-6HfUKth7zaV0a6urYiyzVxSSkVlREtv-d2m07cRSZo6poUWRM6kzRXSBZPfRRXz9DYFCnIcIIqPE1SxgzuXzgwH2ciWM_YLLlJsxP-SQ-CiD0iAAP28Fjlbce-50ZgSHy3MXRQ6khrN67P495aT6TeZywNCHP0gvbspkH1YBE1UymIRPjS-D0LLaaX3z1zAFClp8i2qbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVYJycbYdJ-vIgw5S_1V5W7gJ-eEXtNYxOx7ypCL5_Ltb1njUUbedeh3z9ebJSfeliA31exPkQ0AbhY8G-MgOm9R2dKOpx-ggkhPldPxFQXnyDfUXcHza80JRhFbuX9mALz0OneUTRwnx2eABIpapEeJk0zZfoWPuFWN6VuL34sUU7ebJ4iMPQm2gz7cuppqJVgHfxh0qqBxymSXMZMk_MUXc5wcamMD4nooV01Os8w1QCmwq6bPnQdFx1zfcQdYUYJ4kEm1HECaLue_oRtY-NpuuF2PnRFBsUn7vV8TWwONN095hZ9JLalKhbeg0pltLMLX_6PzOqaDxd6NXy_Pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrUMcVx7blghHTAoXKj5I8Knn1U5qsohdt1nvjTw7iLR1npQeEao1ZkCHq2SAE5ZQQhdnAhq8bxgd5HXLAw8enLAQMszK7dz22UytDhOviFxnqO0Lm2kQhffuHsTotw2oQIxj3BsO_84Ta95TZkPOtKYI_XAustJuQ5MEJsKDdEoSSs6ejtZJvzOtCqin0ov0gWjLeiydGyJLq_rsg1GSRdUBij19FDXxGk8jZfsJAwy4KmWGfosvZOLGLWDecs5GilZNG9iR0nKGuJBOM-StQxliDN4MPckB1oY1Myzl3_Wbj0j8wZ1gxJwaZTk57zRKGYNChs22tMxl161orXjhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFap-TBYHznkfXxvn8cVryt-_cjlGf2Ajlb65kH8ejUU8pYB58abt52VVi11vO_DZCdInTB3yWuX7Dg2JXIFfMOH4fnoW6IbII7pw5hd2sCM-CtIYKZ83lkNzXbVRH-rE_TC5NAtGQYmUxT2Q62mtK0l1vxr2K_KB8NPl7yW6zMuux21jZdrm1Oy2pQX9w3_0ALGw2WyH4H0wFYDeTn0HNK05wKeWjKzeVsY9tMerBxVN1cXWudPQwOWPob9ORKaYhZyUFPqclj8DT5wGeTCehEFYF8ELqo4F91571UgtFp9LVXX5KVO7phKA9Y0uGPD7x8ULpObrmPunH5TxuMEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4O-_hkR7AI-dhf6_7Bp32X66FdY8n1t_4teLNM87gQLjdwX0qfMPDXdX6bm7A4UaAthToiLJ-eiiqKjPKqbyL3VOdAaZkKGNod36NPH11FJ3Pmj5u1mUo3mymUOYTSgGJosd69XZ4Ut3PBXUEUsVexAJXCZNnhsUISsRQ-gIkfJT2cxbEdDEptmXzZeubmkbdmsavi_WxzhvF1L6L09gPoNhE2AFtczG-CJT3KHLRSfFiCL2D76N77wQJ1rGstY2iWXk-vOOSRaVrtbeN-WgT6zWys6AE3MV4JIry8kXRLtUlBBg6BJf_ZFjdI1GS6RmmE4Lf-ogrT6T9DFGHqmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PW_YxpNMJafBB0TyfSi4wiDuorGcA-uc2vUcv5x7qDXaSd81EkyjU4SsH8knb-a-So7nEWwWiIiYW-2ckgSVZV_MALmH2xC3Aq9GooeyoWPlu2bt5Kkp3RRnHlt-q0TAuOf9uwKMtpQfi7ngAgvdfkq_9MmAbX75hsRhecpzYN9XwBhTx9XqOzVNT03fLnYsthUrueXb_7IrJThUbCkB9GnMMwpgKNewsMXpyTIzdVEwMJDJ4ULT5p4SlnpMf_Y1c56-KPR7zbVDT8nnKE5mLAa3HI5xlloaUid6WqBhoikNoGyiItj_p59VWb9HRdfsOpnzvFPEXWxWHejyfbEx4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BM4IaXGaRpV8z4efr4nijAMFs60ATrdoIFiM-2yhzVQwRIOcHjfpYuk49ECvh6XXPx5NkdvQB5kGzgJf0otZUwI0yvG7-pYMairrv1mWeg1Lv7D4BqS2visA_SFDd2nU6Tku6pckCA6567Pyu7535aLi7K3b7-B2fudmJF2Hq-IT97EhaW0MWDVWtarRcCHyXleZCsaLuCcQqJe6fCuiHPQrw6mk2VqnVTqFEmYhk6HEqLv4BrL14ZnHxCV9bXdEEO2Kt0RgJrDYMstVzm-QJ7-_B9xEEbKZDF2ttHyg3ieKWhMDWjBuOfhGvTxUFXszCN_1kBn0oo8d-ZBd_3GVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEdhrCIroLVcpH1o73WXD-dK9e_VE8PFflwhSfPjdBeQzCAMKXqYq5bNI-9H3bGcDmgJRVDO4wtxuXhlJrVA9cEmoU1ozWUotiUNq6lHH6RmbVUfSJeGmGtdKthznGeqTluwouYY0K8cPvimOHWRWvrku1axrCsm8ANFvXLvfJ9hi1Q9zfUYHGca32YfilWB8pWLK4Y2JfFo1ec1_DWD99LNxGsv1tmw2-BSJJBWwFWNe0xYJdViH_BvacdS-hDF52tJ0Z1fh_2WB3no5RioX9Yizfo-6hj9eQ-JDOj5vxpC8fogneQoqrEEEl_Kz1g4LckFN2s6N-Q5bW-ivPLWvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/454116" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454115">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMTvKMOavBwXUrqv-6dq_6Sq_rUwTKOlo0Oy5WXClIG2IOlMdcMi7H5dqhtW6vhNbF_P_Qc8xkzhJwYakh2E5KO93FzlZTTMSEa1EOAEI1aTSh4IPw1-Ve3xe0YF9uvubnAv_mR5oCTh7CbEXlLs8QPXw6cPcQBLsFVPvT-jL_1OZW8PfrGJ4QEuJlT-v8bd1bQXZD82Krqv-3ci_5WkVPi8zrZcRYCJswJTTmmkJ6Jxvazm1N77xMm7slGsgX0UImOgp2sO58scJXLFSBP6jqRKEXPKHtbuufXWdDaRhMDOZNOo_8sPb0TSzyFKgFCI4a03aL-unYbpXPakfEEg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، پست‌هایش را پیش‌فروش می‌کند!
🔹
اگر کسی بخواهد پست‌های رئیس‌جمهور آمریکا را «چند ثانیه زودتر» ببیند، باید ماهانه ۱۰۰ هزار دلار پیاده شود! چراکه گویا ترامپ رسماً جایگاه ریاست‌جمهوری را به یک اتاق سیگنال‌دهی و دستگاه اسکناس‌سازی تبدیل کرده است.
🔹
اشتراک ماهانه ۱۰۰ هزار دلاری برای دسترسی سریع‌تر به پست‌های رئیس‌جمهور آمریکا، در نگاه اول، تنها چند ثانیه یا چند دقیقه زودتر ادعاهای ترامپ را در اختیار مشتریان قرار می‌دهد؛ اما در دنیای معاملات الگوریتمی، همین فاصلۀ زمانی می‌تواند میلیون‌ها دلار سود یا زیان ایجاد کند.
🔹
دلیل آن نیز روشن است؛ تجربه نشان داده بسیاری از پست‌های ترامپ، به‌ویژه دربارۀ تعرفه‌ها، روابط خارجی، شرکت‌های بزرگ یا سیاست‌های اقتصادی، توان جابه‌جا کردن قیمت سهام، ارز و حتی بازار کالاها را دارند.
🔹
اگر تا دیروز سرمایه‌گذاران برای تحلیل سخنان ترامپ رقابت می‌کردند، امروز باید برای دسترسی سریع‌تر به همان سخنان نیز پول بپردازند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/454115" target="_blank">📅 00:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454114">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=NGKz5303vNMDrBMBXaAQgloSc0SsNZg9Cl6rqUa4pls-1bFOsT5GPoJRztbSaQ6LId98iwb8gmvX-4ch0SIYoxnygD_RD3M1U0SHATTeaqmUuODVyGFnV958d6zTaMANw4gnAyRfGB2WKmGlsCcfawUpvLVnurCFN4DfMbDmQgqXUGFSmvuo0tkAepER3CTwkGQdeVi1N_bVjZB_9jgtUAmTdVY6D41r4bOleHBkSvDDrvxFepxX2LTEjZTdr_VbgOBCJ6_6dqVl7gSmw8AyWwMNnc5nspTpu6oBTF7i7WPGN-C-XBfUY_yaReUhQb4HVfuaNOXfa0k0QNaHAWVbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=NGKz5303vNMDrBMBXaAQgloSc0SsNZg9Cl6rqUa4pls-1bFOsT5GPoJRztbSaQ6LId98iwb8gmvX-4ch0SIYoxnygD_RD3M1U0SHATTeaqmUuODVyGFnV958d6zTaMANw4gnAyRfGB2WKmGlsCcfawUpvLVnurCFN4DfMbDmQgqXUGFSmvuo0tkAepER3CTwkGQdeVi1N_bVjZB_9jgtUAmTdVY6D41r4bOleHBkSvDDrvxFepxX2LTEjZTdr_VbgOBCJ6_6dqVl7gSmw8AyWwMNnc5nspTpu6oBTF7i7WPGN-C-XBfUY_yaReUhQb4HVfuaNOXfa0k0QNaHAWVbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی عراقی‌ها با زائران در مرز مهران: اگر کوتاهی کردیم ببخشید
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/454114" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454113">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPiodd2uYErAUAzgBWn1deF2HolMY8TNpdgQPqeNZCWiseolhE305t5XDcGPD5T3An8W1iPW6jl4UB1-F2n17u-iAd867yIMP7CWrxPcJJpMvdFeil-Brf_e-m8K9JkJLRZSGGwfBWeqsmv9O8Cu1kvj-Ht7VwkbG156lua7MqXfIawQYDBti8hbJTgD1lyvGnJuKGKgI2FSofLI4INdfZt6MNRQSoinJfqvZrDfmIdoRn5xCvm3d_lRWJxv3olmB5biN2UWyF9I8O4ddWF5fDsmwj179p90Y7LjJ9bwkp-8coeJGTAIcxhrPhDO1RTu3xpPcUOm13j28LWBKBDh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین ژست اوپک برای افزایش تولید بدون تنگۀ هرمز
🔹
اوپک‌پلاس با افزایش تولید روزانه ۱۸۸ هزار بشکه‌ای تولید اعضایش موافقت کرد که آخرین مرحله از جبران کاهش تولید ۶ سالۀ این گروه است.
🔹
کشورهای عضو این گروه از زمان همه‌گیری کرونا و بعد از آن با شروع جنگ اوکراین برای کنترل بازار و جلوگیری از افت قیمت نفت، تولید خود را کاهش دادند؛ حالا دو سال است که می‌خواهند به‌تدریج این کاهش را جبران کنند.
🔹
درحالی در این توافق قرار است عربستان بیشترین افزایش تولید را داشته باشد که ۵ روز است پالایشگاه جیزان این کشور با ظرفیت ۴۰۰ هزار بشکه‌ به خاطر حملات یمن تعطیل شده است.
🔸
تحلیلگر نفتی بلومبرگ می‌گوید «تا تنگۀ هرمز باز نشود، بیشتر این افزایش‌ها فقط روی کاغذ است» زیرا عربستان، کویت و عراق نمی‌توانند تولید خود را افزایش دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/454113" target="_blank">📅 00:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مسمومیت ۱۴ شناگر یک استخر در تبریز
🔹
اورژانس آذربایجان‌شرقی: در پی احتمال استنشاق گاز کلر در یکی از استخرهای تبریز، ۱۴ نفر با علائم مشکلات و مسمومیت تنفسی مواجه شدند.
🔹
مصدومان پس از دریافت خدمات اولیۀ درمانی، به مراکز درمانی منتقل شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454112" target="_blank">📅 00:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454111">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bff5fe5a.mp4?token=Trb-eQj3xGi2Nqb4iD1CAhibvS0VyEBgobwJtOBDkE9ZlEX2iaCWPyoPZbWh3Hxlc4de4-MCUA7ApODYYDHqx876KqeOhG9y1N2fpv3s6_ZyiZi0eItYndjn1syMyDOSG5oBzdSJeRMQplom7NqxA39QnG8u9X8KjVA0yhhJJRmzeSN8Ks0iQQEzfgXbfcpQT8ord8LIZMCLlKrsdRQqk89wtxZJI5OUFzLrpUicw9yqNwwKual6y-G5fylJNKt2g23DeQGdjIv5T-4YHbiNMUocyhrymLoZ8dfFGTJI9_Hsx27pQ_jJLsVKqQ8UfL2lo5Px6G1d5R4UGg24rKhA3g7S9WZS3YQwxYtx_V3D2BeYFxogVYJ9iSFgPR5OXb2eggqDiTW2oaQltVpUxoDWaZA7fNryTXjCBTLVYnkXbZ5m3MsYvVXOsch74laoaAca2GcGx_OSFhYVXM47i30tAlzrmJt32nuQPeVkw5dyN859vmh0-SdGZA1HW3rYbFQBXjReKyMpdcN5YzVY5iInRH_XJVOggylYPwl4_qnslfHkGhlXg7Qwocp2EF1KdkzJ_mcdf0KsLan7zlp_HxnFB8YyEBJnQ-hWCqlNchiNS9YvFikuZh3kSn9Qmovp5TEWH2ybFPW-_Z3zN4ah8jXlwjzUXz4SpqoSI4SEwFg37pM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bff5fe5a.mp4?token=Trb-eQj3xGi2Nqb4iD1CAhibvS0VyEBgobwJtOBDkE9ZlEX2iaCWPyoPZbWh3Hxlc4de4-MCUA7ApODYYDHqx876KqeOhG9y1N2fpv3s6_ZyiZi0eItYndjn1syMyDOSG5oBzdSJeRMQplom7NqxA39QnG8u9X8KjVA0yhhJJRmzeSN8Ks0iQQEzfgXbfcpQT8ord8LIZMCLlKrsdRQqk89wtxZJI5OUFzLrpUicw9yqNwwKual6y-G5fylJNKt2g23DeQGdjIv5T-4YHbiNMUocyhrymLoZ8dfFGTJI9_Hsx27pQ_jJLsVKqQ8UfL2lo5Px6G1d5R4UGg24rKhA3g7S9WZS3YQwxYtx_V3D2BeYFxogVYJ9iSFgPR5OXb2eggqDiTW2oaQltVpUxoDWaZA7fNryTXjCBTLVYnkXbZ5m3MsYvVXOsch74laoaAca2GcGx_OSFhYVXM47i30tAlzrmJt32nuQPeVkw5dyN859vmh0-SdGZA1HW3rYbFQBXjReKyMpdcN5YzVY5iInRH_XJVOggylYPwl4_qnslfHkGhlXg7Qwocp2EF1KdkzJ_mcdf0KsLan7zlp_HxnFB8YyEBJnQ-hWCqlNchiNS9YvFikuZh3kSn9Qmovp5TEWH2ybFPW-_Z3zN4ah8jXlwjzUXz4SpqoSI4SEwFg37pM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش عراقی‌ها به دیدن یک تصویر خاص در مسیر «مشایه»
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454111" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454110">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2deda5123.mp4?token=MWrddv8rarTq5Odn8JXkGKgZK5uIDAYKRaEHOg2s7i4vDOk3PbmlZX-whRjA1wnKRRJpA2iuLIRBdsb7oTpFxDHd1YUxUhsDNVIU2CXy7PZdAqUpvwBzbD8AWqXIlqf9t6teZq4AOkIsQ0CkNFWx4Aln44FL1FY7Icq43W2lXa7moK_5kMT-3fBRbQPo1cycUxw7tT9UX5gBOcRgovcCqCtvB7V69xfnsZIAtAiHphR0iQDNfU3sNVYDxxQU6hCx9gMAk80Yfdao2VQ3WbhJFshABpnOqHJGbYa5nF9w25bK1ic2tAVPPHSaw42bxxlTIiP08awbBPwTYZ-kxUoh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2deda5123.mp4?token=MWrddv8rarTq5Odn8JXkGKgZK5uIDAYKRaEHOg2s7i4vDOk3PbmlZX-whRjA1wnKRRJpA2iuLIRBdsb7oTpFxDHd1YUxUhsDNVIU2CXy7PZdAqUpvwBzbD8AWqXIlqf9t6teZq4AOkIsQ0CkNFWx4Aln44FL1FY7Icq43W2lXa7moK_5kMT-3fBRbQPo1cycUxw7tT9UX5gBOcRgovcCqCtvB7V69xfnsZIAtAiHphR0iQDNfU3sNVYDxxQU6hCx9gMAk80Yfdao2VQ3WbhJFshABpnOqHJGbYa5nF9w25bK1ic2tAVPPHSaw42bxxlTIiP08awbBPwTYZ-kxUoh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلبان ایرانی در محرم‌شهر: کارشناسان جهان باور نمی‌کردند خلبان‌های ایرانی با جنگنده F5 عملیاتی در جهان انجام دهند که دنیا انگشت به دهن بماند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454110" target="_blank">📅 23:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454109">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKebKzgMAFHF3OMBltpHZBnnfjj0WK1j5_iRPntE7HxTkUPFMbMGrUl2xQBccp-LOfyfbh7ct4N5pKYJyK_-KtXmxzLvi4k17-fp2-bQnx-kozyBU-0IUg3ubC8TOx-IwXIBkWs_MvslwvUcQ_HgpZJKpsyHWfaurOevCwCNDtsAcue3PJVFzFHdaDe6sL0ByqOu7bujS10ar6scyj5j-gN-STP9hhyi4BMYrYl8uIhmPq_ngY8CyeNi7ftmyNb46Cu5QgqkGfI_g1Ao6GFYfQ_jEcVNM10hd1S1FmYrH-Nfkzlq4ILQIwM_K0UlZjtiNmKXdXXkm34z7RxNOVIexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تکبُّر ترامپ» و خودداری از پایان دادن به جنگی که باخته است
🔹
پنج سال از عقب‌نشینی پرهرج‌ومرج نیروهای آمریکایی از کابل می‌گذرد. حمله و اشغال افغانستان به رهبری ناتو که پس از حادثه ۱۱ سپتامبر آغاز شد، اکنون به طور گسترده یک شکست برای آمریکا تلقی می‌شود.
🔹
به گزارش گاردین، این جنگ جان بیش از ۲۴۰۰ نظامی آمریکایی و ۴۵۰ نظامی انگلیسی و ده‌ها، شاید هم صدها هزار غیرنظامی را گرفت، تعداد دقیق کشته‌ها نامشخص است.
🔹
با این حال، طالبان بلافاصله پس از خروج آمریکا به قدرت بازگشت و حکومت را به‌دست گرفت. در نتیجه افغانستان به نماد مداخله‌گری و دولت‌سازی نسنجیده غرب تبدیل شد. این جنگ، نمونه‌بارز جنگ «ابدى» بود، اصطلاحی که نخستین بار در طول جنگ ویتنام ابداع شد.
🔹
گاردین تأکید کرد که اگر این روایت عبرت‌آموز، ارزشش را حفظ کرده بود. به عنوان بازدارنده‌ای برای سیاستمداران و ژنرال‌هایی بود که وسوسه می‌شوند بدون دلیل موجه، اهداف مشخص و قابل‌دستیابی و استراتژی خروج، عجولانه وارد درگیری‌های بی‌پایان شوند.
🔸
شرح کامل این گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/454109" target="_blank">📅 23:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454108">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a169a1467.mp4?token=JL7NltOXZ48P7ikKttkbR0pOlBz1FEYM1L6u5pLhrJZkqFw7r6eGfOX1ignU_5ZKCxDAs4Vf_0ggGPt-Lveb5fmXp8tHdlUXXEn25fjiA-3yAFwKCR0N-xSvkMhilqwwVyYW447QsMYg8IVYp72SutYRHHA_FWLuZfiUN7EDVpw9vMwna2IcBJ3TWTNOsKI0UUgg8XFiieyBxuEAJL-Rqnb9o4b4SxkmMKcNPRqMx8FUSw5bg_CqpHsAuEKNQWz4iCZEJ851x8br7LrU_E4S7EeGcDLEn1gERmdvcRB2rmry0RKTGjbgRwsGfhCj7vB_p7RQ0i-0MEXG_V8mrObCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a169a1467.mp4?token=JL7NltOXZ48P7ikKttkbR0pOlBz1FEYM1L6u5pLhrJZkqFw7r6eGfOX1ignU_5ZKCxDAs4Vf_0ggGPt-Lveb5fmXp8tHdlUXXEn25fjiA-3yAFwKCR0N-xSvkMhilqwwVyYW447QsMYg8IVYp72SutYRHHA_FWLuZfiUN7EDVpw9vMwna2IcBJ3TWTNOsKI0UUgg8XFiieyBxuEAJL-Rqnb9o4b4SxkmMKcNPRqMx8FUSw5bg_CqpHsAuEKNQWz4iCZEJ851x8br7LrU_E4S7EeGcDLEn1gERmdvcRB2rmry0RKTGjbgRwsGfhCj7vB_p7RQ0i-0MEXG_V8mrObCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ ملت امام حسین(ع) به تهدیدات ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454108" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454107">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb6cc9232.mp4?token=mA5-WvTTMoPQWfrEyssbt1LlEfefDgiPHMr5lBILKQ9Tez-UbhfRZAT2t5b4j9vvgLX-HrJ9MWSQWUD8i54d5AuHsENubWpFFVju3JwIp8kaOP3VHr2EMK-cbM7pp7sxCDUULPAjFuczHklHM0Cno8BdKXMBSoNBhBk7jVT-dC2CTPqUMggkrhLtlYCOeCQEQVTRc9vONKxYabT_9szE6BzBzk1B8sXq-QZTLTTXE9oksqrsW8KhCDwdLwc2OxzggcTUj3sdUQ9f04z9dYabUYyvjDfNS310mI-AS_10u7U88BBvynfAClOgVGbyam8A3gpCRJGRvJMjDK-ntZhU3ydXPkO3Ef0MOuZBLtHrTBO7lT2hVJMgJVZbTv3H3aSfqRbjpmlicR5768-YXGuTxF066FSgSaHgI29DnqMUmNWtUNGa9zNU6wBLckDrhL86ehz7atWpc-f4i0IrfU-MmMGI10ImTy5OnrNE3jSvzQvyztsvUAcBRGyqfXhM2aQUvI3BfUDUb6pKTflyKgl3EpcCCkoBB4jK__ckUYkb2hBhwE45mxIL5P6elTcXSHSW5PwHaY1GPFRXx-VJf4JHdpxXezHe-LMVVOv0B-IQiTSZ0QiWU0GHtmG2eq2WgUJifSuDrG-CzD26yUlAMThWbNyjAvMnrb6V-MOcoqTRZTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb6cc9232.mp4?token=mA5-WvTTMoPQWfrEyssbt1LlEfefDgiPHMr5lBILKQ9Tez-UbhfRZAT2t5b4j9vvgLX-HrJ9MWSQWUD8i54d5AuHsENubWpFFVju3JwIp8kaOP3VHr2EMK-cbM7pp7sxCDUULPAjFuczHklHM0Cno8BdKXMBSoNBhBk7jVT-dC2CTPqUMggkrhLtlYCOeCQEQVTRc9vONKxYabT_9szE6BzBzk1B8sXq-QZTLTTXE9oksqrsW8KhCDwdLwc2OxzggcTUj3sdUQ9f04z9dYabUYyvjDfNS310mI-AS_10u7U88BBvynfAClOgVGbyam8A3gpCRJGRvJMjDK-ntZhU3ydXPkO3Ef0MOuZBLtHrTBO7lT2hVJMgJVZbTv3H3aSfqRbjpmlicR5768-YXGuTxF066FSgSaHgI29DnqMUmNWtUNGa9zNU6wBLckDrhL86ehz7atWpc-f4i0IrfU-MmMGI10ImTy5OnrNE3jSvzQvyztsvUAcBRGyqfXhM2aQUvI3BfUDUb6pKTflyKgl3EpcCCkoBB4jK__ckUYkb2hBhwE45mxIL5P6elTcXSHSW5PwHaY1GPFRXx-VJf4JHdpxXezHe-LMVVOv0B-IQiTSZ0QiWU0GHtmG2eq2WgUJifSuDrG-CzD26yUlAMThWbNyjAvMnrb6V-MOcoqTRZTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت مردم میهن‌دوست تاکستان امشب هم خیابان‌ها را پر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454107" target="_blank">📅 23:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454106">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575dbde72d.mp4?token=rpGo4XkwPpVIsmkWYylUQDY8rkzH7wGBFG-bpCVnGbJpy91CFpebUhkiY6gNJfkWhzGMjwZuz8_4HlSoF-3P2eOrUzD6nvPHf-muwZKGw31Yb7PrbiN0SXeTd-LxjmfJEcoxJryRBJBhIGgcZWCggKAlR4BKcrX5_zg5uImGG9W-b61wfFqQUz8izXYGTo6JriBbK2SIXBDDBJ5o1LFK3orkveCpxUEbA8WFhO1nx6gtVgDCGNJqMGcT_CLELAcOsqMxAOF1t2zYXHDjiLWi7pKLsaIa1YY_oOA6IcDN3w7BCx12ui195eMGN1A_BGH5W0YB0x-YTRv4W6NeGfN5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575dbde72d.mp4?token=rpGo4XkwPpVIsmkWYylUQDY8rkzH7wGBFG-bpCVnGbJpy91CFpebUhkiY6gNJfkWhzGMjwZuz8_4HlSoF-3P2eOrUzD6nvPHf-muwZKGw31Yb7PrbiN0SXeTd-LxjmfJEcoxJryRBJBhIGgcZWCggKAlR4BKcrX5_zg5uImGG9W-b61wfFqQUz8izXYGTo6JriBbK2SIXBDDBJ5o1LFK3orkveCpxUEbA8WFhO1nx6gtVgDCGNJqMGcT_CLELAcOsqMxAOF1t2zYXHDjiLWi7pKLsaIa1YY_oOA6IcDN3w7BCx12ui195eMGN1A_BGH5W0YB0x-YTRv4W6NeGfN5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم همدان در ایستگاه ۱۵۵ تجمعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454106" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454105">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کشتی روسیه توقیف شد
🔹
نیروی دریایی بریتانیا اعلام کرد ساعاتی پیش یک کشتی روسیه‌ای را در آب‌های نزدیک پانتلریا (جزیره‌ای میان تونس و سیسیل) توقیف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454105" target="_blank">📅 23:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454104">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57ade8a38.mp4?token=ggbniKEcETG5oh3VID0P33hOfky1bk0kf6uuAQyHw5uBJtmWplmT0sr6ESycw1xYP3edCSOQwO95fl3cP8KqwVTopvxGKHPJV5q7lgqcVvWgfoar5uJYy-iK1KYexwbQQrbPJevzMVXISaXw3Lyk-meyHPReu5MnKfFmmw-uWGmc5BgQshssb7nd2nH7xctIwv5cwdIEXeAfwwRG8wlGl_OoeQ0v225YwVvb8xk4TP3wGJSTCIh3ek_y47HVBDz0tN2vzhcAPvhn3skUx9hTVBDnZE67pAYhoi-dBTW_Rbc_32eiBz9fwGICsmMn6znKAWYnPZP2cTMhOWQ4yn-sejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57ade8a38.mp4?token=ggbniKEcETG5oh3VID0P33hOfky1bk0kf6uuAQyHw5uBJtmWplmT0sr6ESycw1xYP3edCSOQwO95fl3cP8KqwVTopvxGKHPJV5q7lgqcVvWgfoar5uJYy-iK1KYexwbQQrbPJevzMVXISaXw3Lyk-meyHPReu5MnKfFmmw-uWGmc5BgQshssb7nd2nH7xctIwv5cwdIEXeAfwwRG8wlGl_OoeQ0v225YwVvb8xk4TP3wGJSTCIh3ek_y47HVBDz0tN2vzhcAPvhn3skUx9hTVBDnZE67pAYhoi-dBTW_Rbc_32eiBz9fwGICsmMn6znKAWYnPZP2cTMhOWQ4yn-sejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌خوانی از زبان‌حال جامانده‌های اربعین در حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454104" target="_blank">📅 23:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ef4c7f5.mp4?token=CclnpDTBFUwEc3GyXnc1YjneYfKoB7tNFa0JLACYupuey6pb0T4zxHHByMUjjGPW7FnCQP92oF7S6keE5sQehDvJakHHb6HNxRNcryXzNpZLXJc-X0aSbKUoeOH28EaRfpIOaksZ1TJsymPC-lheBFqU4Tb6blvCxaX1MWzxMNMV50VbyEHeFPPcoBfNnZP1vy1e2Rlx4g6ZZ8GWrbwCLwA7dPTRLRMHDUAm81MVzpiDf_MsI66HXSiEA3IyjqsXmzxhcYP38-RX9a628wIIVbfP3KfPmxFmez5ZARlleUkIkgxQdax8VVlql_ng09oSUwj8to4SO5nrATAmMbbA4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ef4c7f5.mp4?token=CclnpDTBFUwEc3GyXnc1YjneYfKoB7tNFa0JLACYupuey6pb0T4zxHHByMUjjGPW7FnCQP92oF7S6keE5sQehDvJakHHb6HNxRNcryXzNpZLXJc-X0aSbKUoeOH28EaRfpIOaksZ1TJsymPC-lheBFqU4Tb6blvCxaX1MWzxMNMV50VbyEHeFPPcoBfNnZP1vy1e2Rlx4g6ZZ8GWrbwCLwA7dPTRLRMHDUAm81MVzpiDf_MsI66HXSiEA3IyjqsXmzxhcYP38-RX9a628wIIVbfP3KfPmxFmez5ZARlleUkIkgxQdax8VVlql_ng09oSUwj8to4SO5nrATAmMbbA4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعارهای مردم شهرکرد در شب ۱۵۵ تجمعات ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454103" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d0a061f9.mp4?token=PFrCslrjCxWRRg9DyoOA-3YcA_WFbVHAx9g8Lxt6E2N4F50XN7sYHpULysrIA3WOjubjqOXhQtfu72TIZN0hk0dod-H4Z61KzRwMf7W3dakLqQzY8qfr5q-M2J13nkVN5pwgQwGMwFzGryIvVYpSFXWaD6fKQpcjyqDxn-IyKFxrEMwajjIMCZUaKes7fRonpgWzXYEoeOVIiAe1fMhe9cz3KYh3IwI0gBJ6afnCwXrQYSFHXlm6Wopt_v8sYTWbKI_0ZGIB-JC4CtGJimvvvypVNwjpnda2eI8GC3pqgICcCrG5xCoqcM-m-yy5bWVeWJMF7detMijhvJD4i3SSwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d0a061f9.mp4?token=PFrCslrjCxWRRg9DyoOA-3YcA_WFbVHAx9g8Lxt6E2N4F50XN7sYHpULysrIA3WOjubjqOXhQtfu72TIZN0hk0dod-H4Z61KzRwMf7W3dakLqQzY8qfr5q-M2J13nkVN5pwgQwGMwFzGryIvVYpSFXWaD6fKQpcjyqDxn-IyKFxrEMwajjIMCZUaKes7fRonpgWzXYEoeOVIiAe1fMhe9cz3KYh3IwI0gBJ6afnCwXrQYSFHXlm6Wopt_v8sYTWbKI_0ZGIB-JC4CtGJimvvvypVNwjpnda2eI8GC3pqgICcCrG5xCoqcM-m-yy5bWVeWJMF7detMijhvJD4i3SSwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران تابستانی در بشاگرد استان هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454102" target="_blank">📅 22:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454101">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ورود ۱۱ تن کمک‌های بشردوستانه روسیه به کشور
🔹
فرماندار بندر آستارا:  محمولۀ ۱۱ تنی کمک‌های بشردوستانۀ روسیه  از مرز آستارا وارد کشور شد و به جمعیت هلال‌احمر تحویل داده شد.
🔹
اقلام تحویلی شامل داروهای ضروری، تجهیزات درمانی، بسته‌های امدادی و سایر ملزومات موردنیاز برای مدیریت بحران و ارائه خدمات امدادی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454101" target="_blank">📅 22:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f524f49466.mp4?token=YqXj8ivq2eUyV-grp9a-P-hmnkM_g6jJTFr7wvE-rd2kIixJ1jZoaJuwoPBEC9Qm67Ri60Bo1_ljL62YWnu_Y2bzXtFTatx1pNJbg9icsL6pmYdjH8InVL1gTj1Wl24MeU4k44UMDsH4NsuQ_-jfyFr43YZrRjTsTQ7IHW3Dgmy9uhw4Nk-ia7gk-GrbWR2O9icyZ5qp0OIv8RFmHGCIHSOYFIZI_3w9Yp4iqxOVM4IrZIlXlIeiwsfwU-sRaMukVRsSeFZN7LcD_-9N3qLI66WkFRw_iX0vKciTkiiblJe06cswHozGRrGWZBGILLlV6USv1CyxzapQhH62JeX6CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f524f49466.mp4?token=YqXj8ivq2eUyV-grp9a-P-hmnkM_g6jJTFr7wvE-rd2kIixJ1jZoaJuwoPBEC9Qm67Ri60Bo1_ljL62YWnu_Y2bzXtFTatx1pNJbg9icsL6pmYdjH8InVL1gTj1Wl24MeU4k44UMDsH4NsuQ_-jfyFr43YZrRjTsTQ7IHW3Dgmy9uhw4Nk-ia7gk-GrbWR2O9icyZ5qp0OIv8RFmHGCIHSOYFIZI_3w9Yp4iqxOVM4IrZIlXlIeiwsfwU-sRaMukVRsSeFZN7LcD_-9N3qLI66WkFRw_iX0vKciTkiiblJe06cswHozGRrGWZBGILLlV6USv1CyxzapQhH62JeX6CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی اربعینی مهدی رسولی در وداع با پیکر ۳ شهید حملۀ آمریکایی در بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454100" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poqeLA9daLVozk_VWNn5jIzfaH1uEcTqNoSEGOAN5DBceo15xGgUVKMLnnQRiaoVDeGO2XWwoTp0gMQXbgGmuJKx72ZC_WGVl2FeRCuro7b62-9qwjopgfsc32k_4UQ8sf2RT37Q4vpkNT-UkAhApX_j6dni-nPTJJt08OQAc-ENsWGXjdQF3zfO_rhrXP0PxKlwEmGn6E_M8nLZfRloFicJQdq0nhiSPur605jSSQZmU_2xWd1YqwinVzFoDfY0HHrxm_9KOd_pKa2yuhHo7w2PsHO_8Mhp9CFe3U6xuUSrS7fR9E_VWA67voZT5kGVs9Nzj1-sdnhjvn7okltiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: باید دشمن را وادار کنیم به تفاهم‎نامه پایبند بماند
🔹
تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود.
🔹
باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454099" target="_blank">📅 22:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad9674ca9.mp4?token=vcHf2Wu7tlxm9N9kJnE6O67ABdfEKqAL3SgzACDamWBtAjdQL-neloC0gSbRPcF2WVd5_AEB0ALYX9UOD7mwHbyU2XhJC7GChvML1RAB0V3SuVxxFUv5p0pRASxP9gZC0JVHbW7ZGRaxwzW43bvcpGlz3Gje9Y2uAs4NlgZfdflYYND62ap75jPIkqxz3H_cY_D8HWiktYxrh9u0xjUuPPgfbwvZ_-u5EjQpZNy_D3WH-xf3zHgN1RonuvW9vlJItgIOSvTkP-STnS1KGHbx7btAZjFT5-0XtnH9JmNa28gKKLmQQoiz5C_SG4Hy9tbBOihX1OcWlwia0jz4VUTIupKENDO5p8QQnXBIEJt_liQNKiK195m01Wb_qEgxMe7a1Ef1AQGVQuvdhF1LIbeYCkiWM6edZx5Z1SsVA2sGER2eT9Yi8TOsG5KSUzKUW8SSLIHgBx_B5FE7lzIRxEQMp2-zN_H1-nrDS4lPVr7X21hiweL_HdLdGIKFM9xWpudm8gBH2hHY8QYQQsYVTmXRMQjSNFlAFhzJajC7wRh0lk9znE0W7SQoes-7-Why3IBXL21xRWqwb6CuJ0If1sHhlLRlbeBziciPk4U2ERYrTA7b0y_H6gR-cGTxmd8NL25o7XnLcN0EVpQFvis1N_p_QEmOD1e1hE1Hxzitsx0I9sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad9674ca9.mp4?token=vcHf2Wu7tlxm9N9kJnE6O67ABdfEKqAL3SgzACDamWBtAjdQL-neloC0gSbRPcF2WVd5_AEB0ALYX9UOD7mwHbyU2XhJC7GChvML1RAB0V3SuVxxFUv5p0pRASxP9gZC0JVHbW7ZGRaxwzW43bvcpGlz3Gje9Y2uAs4NlgZfdflYYND62ap75jPIkqxz3H_cY_D8HWiktYxrh9u0xjUuPPgfbwvZ_-u5EjQpZNy_D3WH-xf3zHgN1RonuvW9vlJItgIOSvTkP-STnS1KGHbx7btAZjFT5-0XtnH9JmNa28gKKLmQQoiz5C_SG4Hy9tbBOihX1OcWlwia0jz4VUTIupKENDO5p8QQnXBIEJt_liQNKiK195m01Wb_qEgxMe7a1Ef1AQGVQuvdhF1LIbeYCkiWM6edZx5Z1SsVA2sGER2eT9Yi8TOsG5KSUzKUW8SSLIHgBx_B5FE7lzIRxEQMp2-zN_H1-nrDS4lPVr7X21hiweL_HdLdGIKFM9xWpudm8gBH2hHY8QYQQsYVTmXRMQjSNFlAFhzJajC7wRh0lk9znE0W7SQoes-7-Why3IBXL21xRWqwb6CuJ0If1sHhlLRlbeBziciPk4U2ERYrTA7b0y_H6gR-cGTxmd8NL25o7XnLcN0EVpQFvis1N_p_QEmOD1e1hE1Hxzitsx0I9sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت دسته‌های عزاداری در بین‌الحرمین، ۲ شب مانده به اربعین
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454098" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5decb8892.mp4?token=NbXXojehDfcTA95p-GIGcZ7mUBGOjQfV-ocsqycqVfuPBZTYo2C-Tlhus2aqPRdZVHaD6b1qktuZhBKebPM0l0PNBcdBnut-yvqyLFSajfWf67JTnRwUTuCX3j56Tp7myk1MOuNIsd3EQOUATuKM5aAl26Me4LwqocMPHRMci6QCAdudSjlrnd-33VO4wl4fGHARce5R_aBeWD5HMj2end1AtdghIgFFxQlgTGSmUwW3aKPCUMXuOX1okfFtbQdmKP2V6wJ1_AT3QcD3VTSnlubShfK5qFMMRInIEXueAKZQERMh0gCqxk46hzUbPxVki6Y0qfSK-Ai33CrO1MWKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5decb8892.mp4?token=NbXXojehDfcTA95p-GIGcZ7mUBGOjQfV-ocsqycqVfuPBZTYo2C-Tlhus2aqPRdZVHaD6b1qktuZhBKebPM0l0PNBcdBnut-yvqyLFSajfWf67JTnRwUTuCX3j56Tp7myk1MOuNIsd3EQOUATuKM5aAl26Me4LwqocMPHRMci6QCAdudSjlrnd-33VO4wl4fGHARce5R_aBeWD5HMj2end1AtdghIgFFxQlgTGSmUwW3aKPCUMXuOX1okfFtbQdmKP2V6wJ1_AT3QcD3VTSnlubShfK5qFMMRInIEXueAKZQERMh0gCqxk46hzUbPxVki6Y0qfSK-Ai33CrO1MWKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستاد مرکزی اربعین: به علت ازدحام از زائرین می‌خواهیم همراهی و حوصلۀ بیشتری با مسئولین و خادمین داشته باشند
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454097" target="_blank">📅 21:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd968655.mp4?token=uy6jRyD08eGshoP2bDUf2XsXjgvEQPf0i28bCG4tznSauHSJt7XAFDxk7EjDU9fVu2dH0P-kXpVf2CykZUWR_FlWpU0Z6pT-jBKqXfw4zz6RDw7w8sp_j_AfQEhkkynDrBWYr4FfX553BgQF3nRn9YPRFgdnhvweSGsiTG_LYDiq8-Yhl79WgtZzOM-wbtRJ_XRNT9JdXw55Fs3TCnxU_JAi1H6PwOd6TAT0VduwTF3G3ZlULAMvvkuhRO2TEmFSM5NE9LwJgE2tXzdl5y-TySwNea0K6U53gTgJLf4OMs-8dOSbh_2Ojrm_r2QHE7HXTlDoWCs8Irw8lXxnOeF5LBkOecdv7URrjveFEPAjodlSajJbzrTloPipcX3CADg6UaDab-zVoO1bU6_xM3d1T-oaGvfdG8wHMt91-5RPD1QEh_xV3fM7krTbHktPzqnLmhpxLohPI1QxD3G0tmYOFw--e3gEHnXPZsdNV48VXNmx7C4DMYc8-50fSImS19x7uuMGKniFOniUqBIRfzZkdF5I4dYPH0TA6gqg40iDKF4cUNNMndmu95ggAYXU_oh2SUDocK1bSeezN7Qhtb2ovGec0NYGEjJPMpz72oDH9ZidChCrprHhAXu5-Icm9qdsNcQO20JLK77R7i-M74NjBxAhbFd8f7H_9I2YtB_ICYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd968655.mp4?token=uy6jRyD08eGshoP2bDUf2XsXjgvEQPf0i28bCG4tznSauHSJt7XAFDxk7EjDU9fVu2dH0P-kXpVf2CykZUWR_FlWpU0Z6pT-jBKqXfw4zz6RDw7w8sp_j_AfQEhkkynDrBWYr4FfX553BgQF3nRn9YPRFgdnhvweSGsiTG_LYDiq8-Yhl79WgtZzOM-wbtRJ_XRNT9JdXw55Fs3TCnxU_JAi1H6PwOd6TAT0VduwTF3G3ZlULAMvvkuhRO2TEmFSM5NE9LwJgE2tXzdl5y-TySwNea0K6U53gTgJLf4OMs-8dOSbh_2Ojrm_r2QHE7HXTlDoWCs8Irw8lXxnOeF5LBkOecdv7URrjveFEPAjodlSajJbzrTloPipcX3CADg6UaDab-zVoO1bU6_xM3d1T-oaGvfdG8wHMt91-5RPD1QEh_xV3fM7krTbHktPzqnLmhpxLohPI1QxD3G0tmYOFw--e3gEHnXPZsdNV48VXNmx7C4DMYc8-50fSImS19x7uuMGKniFOniUqBIRfzZkdF5I4dYPH0TA6gqg40iDKF4cUNNMndmu95ggAYXU_oh2SUDocK1bSeezN7Qhtb2ovGec0NYGEjJPMpz72oDH9ZidChCrprHhAXu5-Icm9qdsNcQO20JLK77R7i-M74NjBxAhbFd8f7H_9I2YtB_ICYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر ۳ شهید حملۀ آمریکا به قشم در بندرعباس
🔸
در حملۀ بامداد ۸ مرداد دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454096" target="_blank">📅 21:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454089">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtUkQda3-xryFpEK9eQPulfT59zwVasX70XSXzPxVhHEyfSRSqJiIv9T-MOpM7Op2J1hQoE566mrw1oh7MJZYwQg4H8EhDu3rTrEoATPg1sfqtXvwgkRFqbCsV9iiQZUNYEdk1gs34EI1R14wVWZq8PmTPIXO5cp96YMRfUaEJ4LpMu5fVJ-0YHetSRw3LIrrtS0XQVRY5hSlUcSbUe1KDgfZJQKtpUh_rMjxSz6dxEfTlzWHBRXQmeOdR3oZncz3TNzDH9SLCr0ns57pPO-ADGNa7WnLYNjw9cRaYZXipCBdYXoPXL6H23D29bl_QXdC6haZt63xt7v14vIxlUXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSeMoLtmqlOGjWITP3IeRo3M5ofcb8ZBZbXZuKdr30vazvqC0lri-5ikEMKJIc-SQQGAuvmLy4xrVDbfODOqufUx7z9KfL0QOgcNo785mgY2_gFAfryME3H4I2V8Dq0g3pfn417mVNcvhfVhr5Jpv8sj1Ft0kZv47jl_RSTXpYisSi-SLxNw1jNqyh50SowWu2sTpgF-D2QLfbZhjd1t3rWVpwebqAqsZo8yGVuzh8JTkX-xkVMBaWApWfCdbU3GnNsFUhHkX0D7TMKM_gfLkr0fIHuceDPMC-PJcQGwDWQsDMX_oWlpXPAxlZ19gBLM7y0_mdE0LaLuTrrpJZBsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sg4qyWjHhNrUPcnDrbACxOFTQgZH281VJVk2Mj7fagsmYhye59LFZsXBZnR8Jp5ImBrWQea7C_ZQXUTHqFE_rj9C-g9ETNSGUaPtgBbX2lXphel4i8Nz9j9LDdWJWI8FxthoWjY4aPZG3ZCg-vFzSMIMo8lQo2Xswv9lS9P6SKiDE1PUMnji990pA93OwX6pz3Jd8S0N_1LXsRShsDMWSVG8K3GtFUg4efpMWOBbYL6AQMq1zoql8fYRjgsofNqkXo2ikcZ8V8QOK-cySWC9XPwA-b9avGvvW0HB0hD_i1ZEG_kCRP7_spTBprhNxuAnr3Kx0fnEjMhwEMDSf6bZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMozjlBUfoBU9G9ViYeYAvh57dZThndydd94qxK6waaoLxyNKc3joLezN0keaNWin8EWNwyDtKeyLPMAtJZyVW7rAGrQNvvdb9GUmjbNADno31IqDXDZiKf8kUM-0IoSGxVrTrsB6o4xSlsoxmxGiTjlYM6mv0xPmQ1XgEpIEdG6vLccc7Ny58YliZI6fkeQlB81I_1SoYlV6AGMHTudCX54uZJDXLSaxaNLTGUNOuO1oLJ7YYzaN2PwzBsVmLxSH4xjKkEZgCHQf1G8iFr-bTWwu_ak6UQdjPg86ER3N7M8JYMNNhIws-xxcDDYZshd6uQvYNxTPh1YmGjvHTX0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN9bzTxa3RUHoX56AyHAPmsetUIcVPtVZhinI-TYRIF62lsFUR5gLRBpDc2su8QiO73BAkcVdIflmCMgoZE2DhZZnJWvBkNzE-S5RpIgy_BOR47MaYw4o57qmZ3ajJTBXb_SPaeNb_zNlSw75K4xF5bj2-l49pYueeskEjZaJ0Qfz_OES6NZjgMKf-jntTdTT1xIWYQjht7fwpokXAVimz04PKDBEamKbOknXidhjYVLRuGlazu1Igw9EVJf6iEav_ZhyCu1yNQCHsbvERLeBNnoqcwqk7yRj__EeATP76jE4IRGyiSuZtj_fsGUkmaARph-e7EQpIRcSdoeBjvFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-VB99b4cirvJ8barY8nJ0G6IxYiylNjzlZhg5bCv9zkHdVAu__Zl5B2GKgbQAUUmsiKNG2Bs4NnsCSxzieLtwm-A8JgrStuQ4smnDa8bilW7_AwqQS2DgfuKyy4ZzVyC9kMF27BVX8imevB19ZguWXGQiO_zHDkWHnsNBmsSao-weVWZOupOaKhnh5J8574WotUAR4zGhcw7XQ36opR3KhDzGlBWk6ECUAM5lSIFpP6XZNiozhc51bnly1kfgrZ9OD_vaf1TJ7eoCbnV9MxPAia6klO3DlnQh0DYBzgVUu9QemEZspLrujmS0IKaasrsqEafJnZIz20BNPmRyLYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQIMOCHy2q7UdCkV8tMPggPWCyw2BpXtAHA88CFfDPCXz69vCjIStHSKaBqAet4UpIybboZh1-LUg80WEZPmYHuUY5jNmO6AFZPqHqgIIXVTJAZtgNn5xIoTfnB7bQg7v3q_3TSvcHMZACEL7MknTg6FAo6t0I7rizdJz9kqpbv4DrBTvLlEO9XFh3f9bYXMPumI5T98B4yNXQI4uIZ0HsCJlzOUOnODHeGbKKDVP7sG7Qpp8D41Nyua9jfg1RKC0jPzNQEnS1nbUWnxwPiFdI7jir6APpHEFGeJFMkfcQEd1tdJDt6WGIgZAo_opkcifjax6quqbQd5FHo8JU2uEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت به زائران در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454089" target="_blank">📅 21:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454088">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuR9Fn2W8c7pJ8d6wQu4mz_r9mr7MYn8fFG7kzBJ6ZzgY-jLt8IklM4Jayb2-uuPTeyA5DqblKixEiv01BxcI-FC4JjNTTDuMFQukHtSBxyYiIKUiYzz-U_2X6awwgZBb-TQ5oEQtGRbdo1WXCsqcnfqtqR4Rlc2BVbjbQSR-vLiOhVFZTXwPFX8L3OdSa8tuYXbCObMbLu90EjfLytDEt3DmYrMpYRHWlByhYd6sgZqa1pPLZcxkUu4uPFYI2ZQ1I0gq0Ca2s_25rPu6zn57xxPAKvFRPAuB8cQNNpnUFDUpvp7hsPRYdBxgmlNVPN-cdKojSA7zNsd_0w-veX5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
پشتیبانی مداوم و گره‌گشا از پروژه‌های شهری با «مسیر جدید تأمین کالا»/ شهرداری تهران چقدر مصالح از بورس کالا، خریده است؟/ افتتاح پیاپی پروژه‌ها، با وجود شرایط جنگی
محمدعلی‌نژاد معاون شهردار تهران:
🔺
برای نخستین بار، در دوره ششم مدیریت شهری، مصالح پروژه‌های شهری از بورس کالا خریداری شد و این شیوه تأمین مصالح، ادامه دارد.
🔺
شهرداری تهران تاکنون، ۳۱۵۰۰ میلیارد تومان انواع مصالح پرکاربرد پروژه‌های شهری را از بورس کالا خریداری و تأمین کرده است.
🔺
با وجود شرایط جنگی، در ۴ ماهه ابتدایی سال جاری، ۱۰ هزار میلیارد تومان انواع میلگرد، ورق، سیمان و قیر از بورس خریداری و برای پروژه‌های اولویت‌دار تأمین شد.
🔺
خرید از بورس، ضمن افزایش شفافیت و سرعت تأمین کالا، کشف قیمت منصفانه و کاهش ریسک معاملات را در پی دارد.
🔺
افتتاح پروژه‌های شهری، طی ماه‌های گذشته و در شرایط جنگی، افتخار مدیریت شهری است و به زودی، پروژه‌های متعدد و بزرگ مقیاس دیگری نیز به بهره‌برداری خواهد رسید.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454088" target="_blank">📅 21:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454087">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD_6N8cL5LAmhI-4RoKEoqJToBRJiRP3yFvxNlfv8tMIyw-WtGhRKCngYke4VqThyc0JpewE0FbSJQTyCW4dpmStB_SmD41n7xChjxsMG9jWyjHA4_ovgq4FD5VDb7Ru3c8dnMQC9zFIHUst3rM64v1Fv3OhYeZQ5wkXt59Hcuxsb1H70Co1TJkeLO3g36mFu50PY6SQHku9F8y9NiQO2289qxmCKgZFYR1Cl6q30RLfWmgu9n25iur0kJolTzvOZELc_LwJTZuDpmaykFWa3AGdvpDa9iGncYck8xSStNk42UK5dpc8FKPh1txFxWaBPc2UJntRmO7d1SxwCc7zmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
در چهار ماه نخست سال جاری
بانک کشاورزی ۱۰ هزار میلیارد ریال تسهیلات برای توسعه تولید بذر گواهی‌شده پرداخت کرد
🔻
بانک کشاورزی از ابتدای سال ۱۴۰۵ تا پایان تیرماه با هدف تقویت زنجیره تأمین نهاده‌های اساسی کشاورزی و ارتقای کیفیت تولید محصولات زراعی در مجموع ۱۰۴۱۲ میلیارد ریال تسهیلات در اختیار فعالان حوزه تولید بذر گواهی‌شده قرار داد؛ رقمی که نسبت به مدت مشابه سال گذشته ۲۴ درصد افزایش یافته است.
🔻
استفاده از این بذور به‌عنوان یک سرمایه ژنتیکی، تأثیری تعیین‌کننده در بهبود عملکرد مزارع دارد. مقاومت بالا در برابر تنش‌های محیطی (مانند کم‌آبی و سرما)، مقابله با آفات و بیماری‌ها، ارتقای کیفیت و ارزش غذایی محصول، سهولت در برداشت مکانیزه و افزایش بازارپسندی، از مهم‌ترین دستاوردهای استفاده از نهاده‌های استاندارد است که در نهایت منجر به بهبود معیشت کشاورزان و ارتقای بهره‌وری ملی می‌شود.
🔗
مشروح‌خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/454087" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454086">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/454086" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454085">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک شهید در حملۀ تروریستی به یکی از مقرهای ارتش در مریوان
🔹
تیپ ۳۲۸ مریوان: در ساعت ۳ بامداد امروز، عوامل گروهک تروریستی پژاک با استفاده از ۲ فروند ریزپرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای این تیپ در مرز حمله کردند.
🔹
در جریان این اقدام تروریستی، یک سرباز به نام ابوالفضل گودرزی به درجه رفیع شهادت نائل آمد و یک نیروی دیگر نیز مجروح شد که بلافاصله جهت مداوا به مراکز درمانی منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454085" target="_blank">📅 21:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454084">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4KqdFWVHqB5eIMq0DFQiKJDh5JV6flVOdIkFdwIQD8iBBx-kwUzfPgMSLlxdadFI3GcZG1NnL262d3-hvl6_vC3gCq9p7gVBYzFY8fsZUHz7KDxrroPhG10TCCbV0ZRATPoI-HOLZEBpBz9TMciXz8KumigMJyrJy5EUeJ0Cs150SXZap1q3EJ9tRHXaJxwADYH3Bf_6m-0_AWeMB5PPFfANssoea2N-2V2igvPlT52Fwp9X7VbZtsNZR1BfodUbkfD6SG2W2CNgbc6jttuCSM1zkTnCCUnR4ZAi1av56YkW-5780Qtl0WZMVjL7kSxXe2X_R8lnzVP2lEUyiuUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت‌ژورنال: کشورهای عربی از راهکار نداشتن ترامپ مقابل ایران ناامید شده‌اند
🔹
نشریۀ آمریکایی وال‌استریت‌ژورنال: «کشورهای حاشیه خلیج فارس در گفت‌وگوهای پشت صحنه از فقدان یک استراتژی شفاف ازسوی دولت ترامپ مقابل ایران ابراز ناامیدی کرده‌اند.
🔹
کشورهای عربی خواستار تضمین‌های مداوم ترامپ مبنی بر حمایت نظامی آمریکا در صورت طولانی‌شدن این درگیری‌های متقابل شده‌اند».
🔹
روزنامه وال‌استریت‌ژورنال چند روز پیش از این گزارش داده بود که جنگ با ایران موجب شده ایالات‌متحده کاهش حضور در کویت را مورد بررسی قرار دهد؛ این درحالی‌ست که مقام‌های کویتی اعلام کرده‌اند که همچنان نیازمند حمایت آمریکا هستند.
🔹
این نشریه همچینین نوشته مقام‌های کویت مانند دیگر کشورهای خلیج فارس از این‌ که ترامپ جنگی را بدون مشورت آن‌ها آغاز کرد که آن‌ها را در تیررس قرار داد، ناراحت و آشفته هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454084" target="_blank">📅 20:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454083">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HboBCXRErDSjKht6ofL93fr5VPcckY137hwzKAExzWHimrImvrXIa3FWD3SWLepIj8uarPxokeGNLH1bKxIywDzIj4T8Rzi04UuSijatk3u4J3gfoE8ADzoc2NVk1IG6gs1o0N2aXo7yHlVEFBqeSA7ph6eqeSbZRFzqBEZ0AWoQzS0NLbcIirnr0no0w-h8f8DX9gATNH8KtxGNSl2IBECcvUo633RP8ZtLqNB2ejFc8paXBLE0Wxc15T0Cay-lMMGZ3-vt0EhV-kSNq-q8LZYoOTf8FeA4-jPziJ9CwNmhx9HVkDhuJuw9XNPcRg9ZwT4qRe6NmE-WsnnYm1floQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برافراشته‌شدن پرچم ایران در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454083" target="_blank">📅 20:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454082">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هر کشوری با آمریکا در حمله به ایران همکاری یا همدستی کند با دفاع مشروع ایران مواجه خواهد شد
🔹
در اختیار قراردادن پایگاه یا امکانات نظامی و لجستیک در اختیار طرف متجاوز، آن کشور را در ردیف متجاوزان قرار خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454082" target="_blank">📅 20:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454081">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: همۀ دوستان و همسایگان باید بدانند که تبعات هرگونه حملۀ آمریکا به زیرساخت‌های ایران، دامن همه را خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454081" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454080">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKgaRQbHR3tY2AEEtb9bZ5ij4WJu8AnjUD3nvgBMA7BAjpOKExJQn583_3AtUy6Vx4HX39Gua5Ay9kn7dfw2nWJWkNGvgPLR7dN1grrcRuaYaC0F8FBuAScfU4Qe2ISnJbD8FRVjZBBgEhkmRXnK0m7yd1QRu2X5NRN_hdNJhhLqS7waBI5q2HQtKsZkUkcWTWI1p5a2QAd8lJqQq5FPAEnfNlFUNEeCcAdnK_YA9tAc7lZOdY-3yJ2GLT4Hccfo1E0z0tPywrzJWLq-13yr0jysh1x7nkfmoTvejikNlVEzY3dPvpyE-vvTCaqSrJ5uVSG5i02oCA3f_eUqc9NSzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: مذاکرات میان ایران و عمان در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454080" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: مکالمات آقای عراقچی با مسئولان پاکستان و ترکیه هشدار و تهدید آمریکایی‌ها به پاسخ متقابل درصورت اقدام علیه ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454079" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی: برای پاسخ به هر ماجراجویی آمریکا آماده‌ایم
🔹
وزیر خارجه در تماس تلفنی با فرمانده ارتش پاکستان و وزیر خارجۀ ترکیه: نسبت به هرگونه اقدام ماجراجویانه از سوی ارتش آمریکا هشدار می‌دهیم.
🔹
جمهوری اسلامی ایران برای صیانت از حاکمیت ملی، تمامیت ارضی و امنیت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454078" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454076">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ایران به‌خاطر تهدیدها و فشارهای رسانه‌ای از مواضعش کوتاه نخواهد آمد. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454076" target="_blank">📅 20:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454075">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: وضعیت تنگۀ هرمز به‌هیچ‌عنوان به وضعیت پیش‌از جنگ باز نخواهد گشت. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454075" target="_blank">📅 20:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454074">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌‌
🔴
سخنگوی وزارت خارجه: گفت‌گوهای ایران و عمان دوجانبه است و به طرف دیگری مربوط نمی‌شود
🔹
موضوع گفت‌و‌گوی ایران و عمان برای رسیدن به سازوکاری که منافع ما را تامین کند چیز جدیدی نیست و از مدت‌هاست آغاز شده. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454074" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454073">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454073" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454072">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454072" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454071">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9tCGzlCdxeBDFHDWtV7UCEAxCzKN8aA-cah3r7sPGl21Y0b53QgV4welOeUGA6w2gVtaXGJ0CVlS8QxPi9u2HinoSOfJWWHFKCn8hviFnFxxco2D1KD3eOkSg-FZjQS6s7xYvNVm4WtFKiJaRK3AED9vV13cOs9Rtl9StLWoptrQ_JN7FjHAl9fbagA1p9IMgR6gEbVa142U-txv6vlb5C9iWrSLAXr-BG9uQa0trnIJNxOl5lYcwVolRNk9g6gFicrG0eXNtbGfalk8qvtDONG5KDn4bLcXdwD6fv_frpopF_doZRe6ZG33xPZdV5ENFvcHSyLHhmQGIT5w4qZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
موج بازگشت زائران حسینی از کربلای معلی در مرز مهران   @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454071" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454070">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAxjmDXxXTp_okIKIl5jJkq7wLgEMy6TcmDVzQQ1X8lTo9FZNzgljjmxEgKFDj6opfyeEf5yIxK4K6HCqXarGItD2K1_p8k1otUtMoVl9hXhveP-d4Cwq2vhLdYmArCHphsT5jQvYycXMtNzLOE7LQf5s5dbKI1Kv0EtQppMfpqM6jSREbZWOh1-tGzCERYnFo5DmnH5Nw76cnEpC-nrWbk-3AE2jHubF8MmxxiF2AkOfJpHg7zu5B9vHWIOeBramSQ-VrAtvTcLy6dCnL3Vthy47e6RaY0PfHTCURGa9Z9vPlkr9s6Qhy6EaNQ8icaInK3I89aQs3zFUVUyHYzkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قدردانی رهبر معظم انقلاب به خادمان اربعین در مرز شلمچه عراق ابلاغ شد
🔹
نماینده ولی‌فقیه در خوزستان با حضور در مرز شلمچه عراق و دیدار با موکب‌داران و مسئولان عراقی پیام قدردانی و تشکر رهبر معظم انقلاب اسلامی از مردم، خادمان و موکب‌داران عراق به‌پاس میزبانی کریمانه و خدمت خالصانه به زائران اربعین حسینی را ابلاغ و لوح تقدیر به آنان اهدا کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454070" target="_blank">📅 19:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454069">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7858fce.mp4?token=KmYqOXE9URRiVI-ZNt_VVSQI0hdsMchyepvOXZvHnCjaNw2Hw7SHGjh3bzGhzITEmf2E0crHhrfTZ_-1M7JDzTReD9VhGH_i4kEsaPdUYNmJBKp0Dk_-tZYaQETr__m3O3xsHU1wQUrIBLMOUqIfDfeKkiSuNHBVkVVyiQZ-YyoZ-GcOcsfIQsceh0H5eOmptk3zNhmYStW1kHI2tFRUnM8GSWIJel_GG1YzC7T8N1R3FzukszfRdBVZTFVyLB7OyyQE6wp4YSM6XIf83uw5R6PyD3lQ9w4RyGB9J-3y4df-SjbmE5Cdx_xxcKjPmg5XZRVIa3qdbz21ay6jt1su4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7858fce.mp4?token=KmYqOXE9URRiVI-ZNt_VVSQI0hdsMchyepvOXZvHnCjaNw2Hw7SHGjh3bzGhzITEmf2E0crHhrfTZ_-1M7JDzTReD9VhGH_i4kEsaPdUYNmJBKp0Dk_-tZYaQETr__m3O3xsHU1wQUrIBLMOUqIfDfeKkiSuNHBVkVVyiQZ-YyoZ-GcOcsfIQsceh0H5eOmptk3zNhmYStW1kHI2tFRUnM8GSWIJel_GG1YzC7T8N1R3FzukszfRdBVZTFVyLB7OyyQE6wp4YSM6XIf83uw5R6PyD3lQ9w4RyGB9J-3y4df-SjbmE5Cdx_xxcKjPmg5XZRVIa3qdbz21ay6jt1su4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مرگبار در پاکستان
🔹
رسانه‌ها از وقوع انفجاری در شهر کَبَل در شمال‌غرب پاکستان خبر می‌دهند. در این حادثه دست‌کم ۷ نفر کشته و ۱۵ نفر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454069" target="_blank">📅 19:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454068">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJb1mwi8RR8UQ296fnqinQgbS9Wm-4_DbGEQ3kKyg9qBho8J2SpHCRIZ7RxqNeSAranjXZhPSrcPFX8ras3RB_xwr8arPSVOV5o4yY80Jhss1_AsixxRC0uR57ugesXr9El1_OOsHSbh71UxYvWXtrgXY0oxl-FWTf_lXi6D7xnfS57eU5ukBuducf506zOpgmb7aKDea3Jj6cJZyjQkMwLcSR4P-J0B54sKO4rlJVd2d3Do0w_-ZLDcEoKHIDV-Tg3FVETNkWyPciJczJYSt-NSmvWkS6fYb7AGw3w5PjByzF8Fmpup96nQ2Nl7rBD76UY8Ln6QtlMeQ2Rh_0ylAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیموچی در اصفهان ماندنی شد
🔹
✔️
مهدی لیموچی، وینگر سپاهان قرارداد خود را با این باشگاه یک فصل دیگر تمدید کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454068" target="_blank">📅 19:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454067">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecda317b69.mp4?token=cMrVP9uv274ZILIRDLHbK7Q_zz9jdjvoBm6yDKss8GBMo8JzlgnGHaitER5vR79PhD_sTaQcaDDUGKWdFWQq4eU3KjfMmNh3E7IqlnVd5GMsepYZN9sglMAGK5gXRbxcUYxm8YRF5wco5YEmrhdcE7moBqFf8bX3Zpy9M2kZqyrOq-DsA-oeYEzyY06p-fShTK24F-WR1GZOmbXO_TECaVKvImeObs4wMFzdEY_zNx9diHxc5fudHCN31BjaSEBiMPEznq-N10U4iGG5QfTEpVUjVHTB65oDuKPiMndTJYcpzIemYUOoxv7SFGaf7B7yFXk40qgZ9CL5hBtMWUPfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecda317b69.mp4?token=cMrVP9uv274ZILIRDLHbK7Q_zz9jdjvoBm6yDKss8GBMo8JzlgnGHaitER5vR79PhD_sTaQcaDDUGKWdFWQq4eU3KjfMmNh3E7IqlnVd5GMsepYZN9sglMAGK5gXRbxcUYxm8YRF5wco5YEmrhdcE7moBqFf8bX3Zpy9M2kZqyrOq-DsA-oeYEzyY06p-fShTK24F-WR1GZOmbXO_TECaVKvImeObs4wMFzdEY_zNx9diHxc5fudHCN31BjaSEBiMPEznq-N10U4iGG5QfTEpVUjVHTB65oDuKPiMndTJYcpzIemYUOoxv7SFGaf7B7yFXk40qgZ9CL5hBtMWUPfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ هجوم مهاجران به اسپانیا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454067" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d965dc091c.mp4?token=MfPITI3dZPFnxO-tVmISSOGzLJILCrxlkdi8rcd5xEfhsSBzsaC1CryrowkIjPhy7o7cj4pL1IhNjMxTY6gEDIgVk7CvuPeG-HbDKa2m7MeeLqWFxc_Vg1PlL7-2PEHV4jy3T5SxV5FyM09yrA0igK0yETZHx2Q7vw78QgpmtBr9zRJVnmaLmg6iI3buAjT_caJNp766s-6TamRfhit-LCkWSnbFrL2u4udAsAwRHhzuum5Q0V0nnKbHR-BMGFJHFphQAslI_DfqyjIFEX_ndenddvF4bkybmVBmt60tkqXAe3NrlbFLOitLPaUAIC7YLJb699BrVSBXALwmOsmrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d965dc091c.mp4?token=MfPITI3dZPFnxO-tVmISSOGzLJILCrxlkdi8rcd5xEfhsSBzsaC1CryrowkIjPhy7o7cj4pL1IhNjMxTY6gEDIgVk7CvuPeG-HbDKa2m7MeeLqWFxc_Vg1PlL7-2PEHV4jy3T5SxV5FyM09yrA0igK0yETZHx2Q7vw78QgpmtBr9zRJVnmaLmg6iI3buAjT_caJNp766s-6TamRfhit-LCkWSnbFrL2u4udAsAwRHhzuum5Q0V0nnKbHR-BMGFJHFphQAslI_DfqyjIFEX_ndenddvF4bkybmVBmt60tkqXAe3NrlbFLOitLPaUAIC7YLJb699BrVSBXALwmOsmrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با وجود افزایش حجم سفر زائران اربعین، فوتی‌های تصادفات نسبت به مدت مشابه سال گذشته ۴۰ درصد کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454066" target="_blank">📅 18:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQI-K3JJ_L7kMP-aFsfiTK940RVP0FPDFpXgYc8DAvZFhnje2_dEmIcvJKHSh0Pf6pGTs2JB_FnIoRl2dfZ6-C2POtQGyvII23kXh9gyKEDt2d79SMOmyVlMA5NIGfaLVuU-EgeKVbPFqCw84VNmxP8asMMU8suws4eGFb7T4VxqTpzkCoHs_WPgmOUqZzeEv-FYdF3FuitGHkS_tRCVEjohDpA4jfQfNhDY8IXzPuWvUzm0qFONBkj6Lren7oTZ9f7qzGciDF0Yuqh0_Plw5m3App8se9Pxt1Sy_VVS47FYxim_VyuAybKYTscWIyM3ofNicwhQ3QfQKcLZjCvI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdtwimWZbLXSdwPLfYSmp0GQMjaXnDVBAzAOrEw0_qKjcEer2alMzxcykb832bXXGzym48Qo2ilJLse4Rox9X3Kb03kon8gbIJ6i6Z2MfP6CwjLAG8HCxJGsghA_MZ_o2TeCSxAM6l-_kILUk2JU4Z6THogLsc7d3SUOap74tAa0OyhfpM3OpScqEP9lFeKNUCaR0mfZV2n5Wd9SqUlcCjmKjf-SAmfdHKI-vRFTev66MejcYVwgzAT4nB43Der1SxhxpVdEj60fphzIyWy54utUSZtrrltu7O9YlZ2TfThlwCoGikh4u-Wjd_ltZ-vc2e32d7EdlsV7Q98yzneBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Th2_GW-rnasOq9Vk3ypG5-gwdf1MAYrXU3t4ktKYRdYhxw6W5PbwxVKn-Qq1ES6P44pg-bEt0XoARCZi_JES5Fo_2SHE5K_fdYrHoXzCfbw-p7POjQ9yOHygj_0VJ1AEGmq_7yZIkEmv6nSPp5p0F_DQHNYSefahMNybIlDQdieQfNBm_so7ttublObGs73M02iLwVAUJ2eDLOunpfXM23t5Gy4XEmC5Fj9KMwgQwBFpxaVLHFPzOyUjL_4cugXnxm0_hiGbyRDzx0zAFCaKiVue7cVXM_zxK3gA4bzC-CcxO2eUIh8Y7bT3a-3vOzbsbdnVOn_ZU0xMOGqrarQbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-mnZGY_Z1f-Dgc0jlGDqDGT8dkzYCE_jcegKkcDFzQkhS1kZzjKsQd3CuXZ554cy9IisRdILcEHA-omMjyDYFJbC-Z-KsSPNH57pF6KQa8_U_pTk7oropy6SdNvDY86KdFjh9ekV71jjygCVkdd66LZ93f3D9xC2CldW_xfLO7dOijsrK-CLlMFbaLOrXtM1iPKX1FEfimUJ7Q3Ub5Yp4qPuslu-F3lgNCOOpvV_eKc3Pad7qrY83-94trRZi7dmCzgbTkso1Y1lAMOVDpBHs1Mi_bdCj51kcPxRBbkx3RyqaN6wAYqQQw-qZ9wCT1hF_TVGcVazZIgTTau1deb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWJfo1eC4zaPRqczhR5zD4t_QDspmyP6YTqU1m1FAomC86qgoF65GLrXfknZTQPZQ2OBB2W35MSEUoIvCvYHrXR5QHDRrDEzWD6BDVNcQ6G_irGz73taKsuzrA043J_owvgrOBMEkv2sSHrNkhu42ebL0Tpd93DXy_yai-eiGAvIc6t5x4xod5tKFR9xwajhLYXtVqNb7k-v89DGMIeXabd0er0dQoMhDpAL7nVTg8zSUzu5RmtA8Lh8EqgZnU2JO5XsSvZj5nUs3chv8zc19Bb0FsbxWHHW8PGtLtyijq3DeXuc5wx8cI-ukEvaWlJtmMQQ2yLe5AlMY1SWGMHPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uz64cEFW_k7sSD4M34f9pQUgM64uu1-UEqKO2wAbXxNDtQ5Ela5ZwAhTQVvxbflhIKbFVZuALqKXeNegFQ3rX-2aGhb4MyADc3-3sMRDphVw1OlvQ9Njg1P-3rKMd0dwVlK5-CuIM1ddfDVWozkXJJV7PaNqfHacZvcistfz7tCI8al7zKRef8C-QEVwSwxVKp_FdilO4V0elkJnpu064QnQVebfDceNm44W0bYjHQAQQiYrkehc-iGbZrU7alRKX6Hkp6-i0hfsxX26CPCOZOyGMzfu_d5wltyiK8MXK2QQYl9l3Q71xfDsvm3E8xo_G79S8mBsyBfThCRyYv6TRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTjYtzZB_xsda4Umv066wbnYM1Q03RHnsuz1AvaBMCwJb9RgdpMhyL_U5YkkjNDuMAmSUxZho1vE8AYc7XfTegoDFB3Vfesnff6NWQ5MEDbW2V2Y8w4GddM4MPdMEuSCuy5K2SooKq41Avacn5JOUiM6eSgaLBXrGmFcJT-WWP_X9RW7sLdXXaZtOTM2hUpU6dwCm88yfI_Ew-9rlr-DWT_X_jU__-Tb25OpdQRD4K1fWNJjebGXl52a_WslPODVYO3KmxA4MyrqGt1NTZ9l3Vfs5z_lpTdkGql9X54Yhisn-xRh8xARKidGDOponGsaeeWXO6kWUDVnGdiv-EAR-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طریق سدة الهندیة
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454059" target="_blank">📅 18:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWLY9W3DT_RMi73VN83w17NEM_jV9dv4QTJcMVuDpx9NVZQhH16q57Q_xfta9nZtAVndvCGqSmhhemZAcb9SUlkCkIC2t95LDLEr_W3caZmGljkjFBqCRjsv2evEX6wcPf6hzDhETQth-b9R36EibXdoWeLAibsojMd8HrlZA1l6KlIImxlu1BqTzAYUv_IOXCPFhVL_IZB9DUaLRvuLec8O3jy8-9hKsf6KdpQen1M2PCPUPXSu7z4LyOO0nkWpAS4eOCMwMH0hIhO5jqGVYluGcSo2HvfRvGnchDUcjqYZ7hvDriwaTcXvGcZFUpjrmqPEq0tLd2nI3Mf6UfqYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج قرعه‌کشی ایران‌خودرو اعلام شد
🔹
نتایج چهاردهمین دورۀ قرعه‌کشی فروش محصولات ایران‌خودرو روی سامانۀ
esale.ikco.ir
منتشر شد.
چند نفر متقاضی خرید خودرو بودند؟
🔹
ثبت‌نام‌کنندگان: ۸۶۱ هزار و ۲۸۵ نفر
🔹
ظرفیت فروش خودرو: ۵۳ هزار و ۹۰۰ دستگاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454058" target="_blank">📅 18:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e92d2385.mp4?token=bZSLh-Pq9ir_Gc1_u_5SIXqs_cAkLBLaENuZ2LrLfay6mTvYCd-K4y_mJXyXaXLM3Pi1iMQPESHoqcIiWczOxyS5lSEV0oDfqwen0dlBd020yaW-86giUUa2kmCjZPYQufgdlXEmBAeBdgPLKhBiwqqsLbuUpaB8_Q1G_7ozJuBfmTQHTsVQDXvHdOUFHu6IYsNda10EGqEBfnjE7gAilK7jLhNjBiF-S4PLahdHGBTLI_-YFjrC-aVikWbVGOY49bt8ocKGZmR9H2Qr505zVvVN6lRmeSY2eOhQAv0QrA6NrUAKGsMBLxsdKwuFQKeSMJIvyIDj-bvhXlgiRCGPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e92d2385.mp4?token=bZSLh-Pq9ir_Gc1_u_5SIXqs_cAkLBLaENuZ2LrLfay6mTvYCd-K4y_mJXyXaXLM3Pi1iMQPESHoqcIiWczOxyS5lSEV0oDfqwen0dlBd020yaW-86giUUa2kmCjZPYQufgdlXEmBAeBdgPLKhBiwqqsLbuUpaB8_Q1G_7ozJuBfmTQHTsVQDXvHdOUFHu6IYsNda10EGqEBfnjE7gAilK7jLhNjBiF-S4PLahdHGBTLI_-YFjrC-aVikWbVGOY49bt8ocKGZmR9H2Qr505zVvVN6lRmeSY2eOhQAv0QrA6NrUAKGsMBLxsdKwuFQKeSMJIvyIDj-bvhXlgiRCGPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جبیر گرفتار به آغوش حیات‌وحش بوروئیه بازگشت
🔹
یک جبیر نابالغ که در یک استخر کشاورزی گرفتار شده بود، با همکاری مردم و حضور تیم‌ محیط‌زیست به آغوش طبیعت بازگشت.
🔸
جبیر از آهوهای بومی ایران و شبه‌قاره هند است و عمده‌ترین تفاوتش با آهو شاخ‌های نازک و بلند آن است؛ جبیرها به‌شدت انسان‌گریز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454057" target="_blank">📅 17:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf9616077.mp4?token=surljXo2APg9yMRXtnECLxRYugaYwLaO_PUza5kSBHUMy9BFRK35HwQH46QdTotX14YthgWRAoG-Au1ah_f72aHjrj-0b8PbxCKpWrgUyz9HBmmpn2HuOB47dUGEfim5dboOT5IL5E8vLbOB0VR5d56xoKUcol9uT7Ksn8gTG_MYIAv7PhdX44e6XgAioeskCiM-mXvCOaFfWamPqgZyp4QcdG27fuMgpykrBF-gG-_Eb9j-OgNJoMX4PJnay8ScmenzHoJiYPOosVmcEPKrvXumjW0WsunguCifuQI7c01ZCO50HrK0COZDB5Ltk4Viwx2MWBoxbP-b1_UxGRcK4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf9616077.mp4?token=surljXo2APg9yMRXtnECLxRYugaYwLaO_PUza5kSBHUMy9BFRK35HwQH46QdTotX14YthgWRAoG-Au1ah_f72aHjrj-0b8PbxCKpWrgUyz9HBmmpn2HuOB47dUGEfim5dboOT5IL5E8vLbOB0VR5d56xoKUcol9uT7Ksn8gTG_MYIAv7PhdX44e6XgAioeskCiM-mXvCOaFfWamPqgZyp4QcdG27fuMgpykrBF-gG-_Eb9j-OgNJoMX4PJnay8ScmenzHoJiYPOosVmcEPKrvXumjW0WsunguCifuQI7c01ZCO50HrK0COZDB5Ltk4Viwx2MWBoxbP-b1_UxGRcK4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳.۲ میلیون زائر از مرزهای کشور خارج شدند
🔹
براساس اعلام رئیس ستاد مرکزی اربعین، تردد زائران از مرزهای کشور همچنان ادامه دارد و تاکنون بیش از نیمی از زائران، سفر خود را به پایان رسانده‌اند.  آخرین آمار تردد زائران اربعین:
🔸
خروج از کشور: ۳ میلیون و ۲۰۰ هزار…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454056" target="_blank">📅 17:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454055">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yun261Z1HIe8cAM74EhurmmlSFmWShhtE20IoSCm-nJHRWyoi2VaQg-MFbNeDEv67mKhfSsxrH5xXX5GSHnk7TN9DmKtOJHH5SERkP9NGobm7nzX65NttKFknNp3tOwa85jxaotuQunr2_-_a-N48Z6CSwrKX4vRZ6cGVK5gLrqkXjhFVololFVuZ3ZZ0WX_KtzaaqzyARHkHCPuNHs5K8kqDktm7kYPoVBiEk-gFsmz5hdBldwUGrzHIzEJ-1I1jO9Z2iB3vQXqd_g_301uC0hj9eailqM33UBcnrDryubXUsIcaa_ROcmin4EMLeW4zQLIrKd8ZwxJTsWPHyDWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدایی مرتضی از پرسپولیس
🔹
با اعلام باشگاه پرسپولیس، مرتضی پورعلی‌گنجی از جمع سرخپوشان جدا شد. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454055" target="_blank">📅 17:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454054">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NngOr-Meb0Lw7UHN94N2Y1XUH2Q_X1YvkArz8HEZ3YsYnEpNvgnsz5_wTQhBgG1Vo8g7i8K0isWITyEziqZGxIIzFARVMl3DihN9tb8MPH39hVoL7iOGukM6P1mKbYM2mQLmlWPFuKaqv9KF4ya0tEVUNJzBfeedA8jH1VZkzIcf5Eoufh7-JLoJioejEK4EKiNGZPnA0q2LFfeMEpPxzj8rMmxpkqQKhvFWPLqzn1Z50csPhyezTDvYFEJM7WO7lQCPN_T9Mp9TqlGQk4LPBazrgebMM7Efy8Eip18s2dxQvyiEfWz7h-HfVoO7V5pXfKMBRSECJA7NU0NTKMoA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نمایشنامۀ زنده‌یاد اکبر عبدی به پردۀ آخر رسید  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454054" target="_blank">📅 17:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597894cdae.mp4?token=WMUCxpJYVQfFARnCJsL4P4jKKvTVkFdVwLE-qXyAKsOyE_ndm1aMO6JUDjX4_X4K3mRSWxRxxrS8bbcRcbVG3MxVhOVuWmN3SKEBuq56rvrj2y2rK9bnf8LM4j0cOeFlIo01Fq23WSd3y9OQ6OIMlWhrt6pGPs3tlaup6vd2_1j18xQdzaYV659MiLcpsirz4IGGKU9IzNfw7zKK7BdxM3Thw-5mAsX_qpCPKyJgUuah1j9GSQ_zDUz_0ey88XJcNr6X5-SYG3WbMNKui5GRdbFmMykEq7QJTuuf7rwNZzfXAQ4pvEw17kB0y7rElOtvvIiY9K6kvBu-D3ayP_L2RTa9nWHpUqm7JI-Su1qtfRCQ3OiVtekyD0wSCxUbWqm08BrBMp_i1yPP-10ueblSkA0kBzXEY3AyB-G196pbjFyWUgEM9hCcD-K5_lnNHJPZHCg1DNCr-m_KUf9xOtPO3HU4sFmOd6anffuTBii0Y9D22C8P1xxXDVfnBSxHbXsXdAcykuYmELLrrKQeVMqrZ-tGublMElcq40BFqflfz8TjrlsIQIfTm2w6LcI9JJVDQruhQujxvpRy3GXp1EFbuD5_autBHvxrl5b3fp61AJ6I9efXNU2EbJVV19NWOPHgyG1t_WTr-5HQvnqUly-feK_pJsMOJL6-lWUS-_xt0HU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597894cdae.mp4?token=WMUCxpJYVQfFARnCJsL4P4jKKvTVkFdVwLE-qXyAKsOyE_ndm1aMO6JUDjX4_X4K3mRSWxRxxrS8bbcRcbVG3MxVhOVuWmN3SKEBuq56rvrj2y2rK9bnf8LM4j0cOeFlIo01Fq23WSd3y9OQ6OIMlWhrt6pGPs3tlaup6vd2_1j18xQdzaYV659MiLcpsirz4IGGKU9IzNfw7zKK7BdxM3Thw-5mAsX_qpCPKyJgUuah1j9GSQ_zDUz_0ey88XJcNr6X5-SYG3WbMNKui5GRdbFmMykEq7QJTuuf7rwNZzfXAQ4pvEw17kB0y7rElOtvvIiY9K6kvBu-D3ayP_L2RTa9nWHpUqm7JI-Su1qtfRCQ3OiVtekyD0wSCxUbWqm08BrBMp_i1yPP-10ueblSkA0kBzXEY3AyB-G196pbjFyWUgEM9hCcD-K5_lnNHJPZHCg1DNCr-m_KUf9xOtPO3HU4sFmOd6anffuTBii0Y9D22C8P1xxXDVfnBSxHbXsXdAcykuYmELLrrKQeVMqrZ-tGublMElcq40BFqflfz8TjrlsIQIfTm2w6LcI9JJVDQruhQujxvpRy3GXp1EFbuD5_autBHvxrl5b3fp61AJ6I9efXNU2EbJVV19NWOPHgyG1t_WTr-5HQvnqUly-feK_pJsMOJL6-lWUS-_xt0HU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454053" target="_blank">📅 17:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادارات استان بوشهر چهارشنبه تعطیل شد
🔹
استانداری بوشهر: با هدف مدیریت بهینۀ مصرف انرژی و برای تسهیل در تردد زائرین اربعین، ادارات استان در روز چهارشنبه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454052" target="_blank">📅 17:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtFFDmw6kwTjkooxm7HXhC62qR0KVB7n8FbnkAMp8qav1fKpCou0uCP3-hn8FiV_QSfE52eBSm4WeOyyloFTG4wjgMZMGtPdhXwbEXcLQAawFb3S-xwGIrWUl_FtxffKFUEgqw1KJcbvtDdumJ4MIKFj4UFUTmfDraU_fcmPVgTCIuwiRwLM3GKrRQNfpZl57ahkFo_LKcfCJeuYNv34iXRhnRA9BRbB81yIa5AdQWBJX4tC7r2TqA7Z9yy6Dg4NERomPJr6URu4q3FJn6NqUU7yKt_eY42uT75fkxuldL1PdYlmRbjNmAX8nKX8fj09qJh6vmRUrw25jpXGW3aMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هیوا» پنهانی از طبیعت زنده‌گیری و به مرکز تکثیر در اسارت منتقل شد
🔹
منابع خبری به فارس اعلام کرده‌اند که به‌تازگی معلوم شده یوزپلنگ نر جوانی به نام «هیوا» اواخر سال گذشته از طبیعت زنده‌گیری و در اوج فصل تولیدمثل یوزها، به سایت تکثیر در اسارت منتقل شده و به…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454051" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454050">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOu-5NnIMpzDDthzTVPjPF8Ni4mK4HbxVicYieVYejgg-eQz5qvO_QB1jf-x6FprUbEHHGUt30bb58IKQXf6bDPyIPz-lNc4pj52opKKgkB2n1-tNFnB_tIvniialNofNCY69_90yEP1nr4fKMpJeuMlTKsOkPnoJxFC9ClIR-moB5xHQnMy5JHPI5citmZtKdSCPo5lXHPkVMcEmn_HU7B2rVTgy83QyN6dCY8HBZF6cVnFQYZkX2gLYu-clVPpeMqpzy7Uvk0Dj2YA0AcBzpFLt-PeI5UZjL5-zqNdvlSeoYjFuSp8dwlgJkX9hnghR-JDVqg3JLgD_RZpapR8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: برخی بازیکنان پرسپولیس باید فردا خودشان قرارداد را فسخ کنند
🔹
کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی‌ها مشکل داشتند؟ نیمی از این تیم مدعی است باید در تیم ملی باشد ولی مدل بازی آن‌ها چه بود؟
🔹
بازیکنی که دنبال کسب‌وکار…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454050" target="_blank">📅 17:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfYi5N8oo0GopqJQ8ZDrydOq-_vQho_fB97PMQb5uUqk93arAR5PeelMB0QARR6YPfqb6905p_uib3McdhZmwh86wCpdGdlPeSLkKzOgavyNgpwpECw2IV3mxOTz1K_U-dioUJ-ZqbflTb7fCWi2A8EqC5kk02--Ma1n8lk9TzcaVs3B72m3403wosneg47lnrYouVMldgtKPW90MGm15444OKLLY2ouo2t5ftJE-39-DfknrLMrr5ALrY7Ca34LDwEgV6ti_O07TRcEhXLPLvijPBYIAN9J42qanC0JqPNVTorvrcmAeuWTN_jvrCApWQxOSLcQJ7-FtIx2T9BYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: توطئه خلع سلاح حماس با شکست راهبردی مواجه می شود
🔹
سپاه پاسداران انقلاب اسلامی در بیانیه گرامیداشت دومین سالگرد شهادت اسماعیل هنیه: توطئه خلع سلاح حماس راه به جایی نخواهد برد و از هم اکنون شکست خورده است. ما به جهانیان نوید می‌دهیم که سرافرازی مقاومت ضدصهیونیستی خلل ناپذیر و به فضل الهی پیروزی نهایی فلسطین در برابر اشغالگران، نزدیک‌تر از آن چیزی است که دشمنان تصور می‌کنند.
🔹
ترور شهید اسماعیل هنیه در تهران- در حالی که  مهمان رسمی مراسم تحلیف رئیس جمهور اسلامی ایران بود- جنایتی عظیم و نقض فاحش اصول و هنجارهای حقوق بین‌الملل، حاکمیت ملی و تمامیت سرزمینی جمهوری ایران اسلامی بود.
🔹
با گذشت دو سال از جنایت رژیم صهیونیستی در ترور شیخ اسماعیل هنیه، و تداوم نسل کشی و افزایش جنایت های قرون وسطایی صهیونیست‌ها در غزه و گسترش جنگ و جنایت به جنوب لبنان و سپس آغاز جنگ های تحمیلی دوم و سوم با همراهی رئیس جمهور پلید و اهریمن صفت آمریکا و ارتش تروریستی این کشور علیه جمهوری اسلامی ایران  امروز بیش از هر زمانی ماهیت تروریستی و جنایتکارانه این رژیم بر همگان آشکار شده است.
🔹
استمرار حمایت‌ همه‌جانبه تسلیحاتی و سیاسی آمریکا و برخی دیگر از کشورهای غربی و نیز همنوایی و همدستی دولت‌های مرتجع منطقه‌ای از این رژیم، آنها را تبدیل به  شرکای جنایات ارتکابی نموده و مسئولیت بین‌المللی آنها به‌خاطر نسل‌کشی و جنایات جنگی رژیم صهیونیستی را یادآوری و مورد تاکید قرار می دهد.
🔹
راه شهید هنیه، راه عزت، کرامت و آزادگی است و این راه تا تحقق کامل آرمان‌های فلسطین و نابودی غاصبان قدس شریف، تداوم خواهد یافت. ما به جهانیان نوید می‌دهیم که سرافرازی مقاومت ضدصهیونیستی خلل ناپذیر و به فضل الهی پیروزی نهایی فلسطین در برابر اشغالگران، نزدیک‌تر از آن چیزی است که دشمنان تصور می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454049" target="_blank">📅 17:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmxoWhrHaY9ryg4Awwbb1tk-2h-jmsIKx7XMRM1c00znsJf_tTQPB4lZxUYTakqOhX7yboOzmqHwBkuHyjlAefMNahAw6ShNYtf_lF52svjdTtIXnEi5AThinvI0jivBhQd3JUk335bSNLkMkrEDetB8-tU1ao9UnhwJNIVnqU21J-H474MuwBnY8WqqS8TFFi_ksrlBfr0INNYUaeWH6Q_7mPVK0JNDY6Gi20qh8W-BSeH3j6RbO4vc4vw3xPi4qh6vBb_Iox8BVFd0A9h7qfnXEfpOkAlNFGl8CEKy4vBZMp1bYGAx69O3l5obliT_FOXnnrlmOZaUGHOu6owbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی علی کریمی از عموی جدید سلطنت‌طلبان
🔹
علی کریمی فوتبالیستی که روزگاری شهرتی میان مردم ایران داشت اما با قرار گرفتن در جرگۀ ضدانقلاب و سپس اعلام حمایت از سلطنت طلبان نشان داد که در حوزه سیاسی به چه میزان دچار انحراف فکری و سقوط شخصیتی شده است.
🔹
او که به انتشار پست‌های هیستریک، عصبی و نفرت‌پراکن شهرت دارد، این‌بار در یکی از پست‌های خود از «یزید» به‌عنوان «عموی» خود یاد کرده است.
🔹
سلطنت‌طلبان پیش‌تر از افرادی مانند لیندسی گراهام، ترامپ و نتانیاهو به‌عنوان «عمو» یاد می‌کردند؛ اما حالا کارشان به جایی رسیده که با یزید هم احساس خویشاوندی نزدیک می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/454048" target="_blank">📅 16:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سردار آزمون و محسن یگانه در فهرست توقیف اموال
🔹
دادستان گلستان: اموال ثبتی ۱۶ نفر از مزدوران همکار دشمن تروریست آمریکایی-صهیونی با کمک دستگاه‌های اطلاعاتی، امنیتی، اداره کل ثبت اسناد و املاک استان، راهور، بورس و شورای هماهنگی بانک‌ها، همچنین سامانهٔ سهام قوه‌قضاییه…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/454047" target="_blank">📅 16:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU4JBIV6PubY0mPbgZTS1K6RKTTEg0i9A6T9qdUDEM-gtS_tVL2PEwCAcsnXAQNpcxNxIOrsAZ1RTUx11slKyKyzeDE0F9FxcbMhw7MyjWh_ZpjRyxB9-7jg4elApBLqBZcZC399HOerWAJyg9AaXGWuKkXa2WH43mafopFoncLG-NH1aj_B-fl__1NOVc52FG8hQF2UezKf6Eu37B8b7mnB12TY1hi-QZCPo2031UCz2U1JFvg5g1dJoZcEjCUDrDB8TQKdyvHycPX8-Z4Cy10Lnp8TklRPMNipts01V90XHYykFcdUTXrzDlWk03fLQSaYrBXWlDbrEnR6tm1QUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: زائران برای کاهش ازدحام بازگشت، مرزهای باشماق و تمرچین را برای تردد انتخاب کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454046" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454039">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7eOwlEtyClPD7T7Akir0bjblwebx59WMJBfkji9f5-V1cJqtoxpzzazQLJD7eA6TPZZSxFW9tSXjqV1JeFBZGqXTrdVCukaYWdPYAdtpNbzRR2qwkAoT378OajyRa9FMycRlh_m9tw_dFrHboCBW_i_LcTxHdNB0WitG86SDVzFzs0Ln9PD14-mMTskf_eyUT8zRvhpPv9DOMhHDYCgTdstR8l5zzcvFrNMhWdzKdOSUKUnYjcc8KGj_zKz0h8gw7NBTLaaiGwU5XT8y-bsYlGjnp8zvj5zoRvFCo8OsPVV4Coym_0cfdQ1Eq_MKbNgik70UTA4F1AXa_AKa_Kb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_FPRs6CJoIQDL2fh3PuDG2s-2MDP3A8CV43GTD5QRl_14c1kHVmb7gMjoVHhMf6sTkYLFkulm0kww5yMbPAeWM_D58h2T-YMOot2ZV_6v9njdXr9tX8yZyOR7a8s7FW6P883YhUU5DtLVQWq3h2M_nbSJZaFUUplI0ECviq3BVIMMKPIAC9gHYjENN_0nNyOGvIJ7TmAw12kNpyXemPkGCMTGoKJ1lhPeKPDJEIt1Ut5KjxBzfo_Icm82A5L1CkIczsumf9HQbBron2bS5hvBLC-kiguQJQ8Re4GW_gm1wbf3E-JqR5AqXDhNg1Cz-_N_MT6eN8iIItkVmvpaXATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fz87EGJkWiXLPs4m9YwltMKuxUE6IolL6XlqaTQM8vl5od8juJZ1o4oIexeykemX_cBtXtFHRxy0oST9dR9h09n22oIgwKocSBPWrflL3ASPefXL05P10u3ratL0MrxCajEPXUExGTq54EPF2gL7aOnh6hYKrl64wGA0o54vOu5xciHmrJQ0-cS5ay_nCictdXF3E0iTpd6c-M8B9VTeqzyhZGW-H6N9OqZK0empDkNne67hLRT-rYbFvZetVwssiGzPTytmSYtd3_7qCNqJxYM1_Tc9agc42oCleGtjn_wJUN0iXmis4K5CLOy4nZWxC0sR8Gmg2u83YVvq80lnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELhjga4Gn1jSZ9ZNc1tQ97USK4vpGRC3pIsuYH_Oww9o8w0GwOQQSHJFfbSXpbbP_HkyIYTUkrfBxfiNOzP5OPexRWPgN-ehaaAXQXACkE8wUGP1ob5h23E7vG_WTj4YiIi1W03qhDEWAIbwdf3v3wrt2jEyoL0mCDTS5qXjjpL9O8jOQSJLqMCmPxNSD-_Q307cXQ-vkzDMiCK_p6ca96_C9xqZ_Yp0Pl-uJADvxeYH-F3KpFve9B3ybqfmzW4w9M-eYj_-CxvYV6tp7i2zBVvbpGOrLumkws7_6JhszJBm5RXoP8W07R69M3TM3JswtLTKXr5AqhbpcTkm3nfXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiZgbvMNMR8OEUbR-CEBPPLXTpOJsxvY-kTT_vn6gQfoyKg0JpQ4BvFOicE8sFBv1Cxa5yiHKiP0WduRS3Io1fMSzeAuFyxEHc-8N0SXiB3OwzYagYh8M83KkANSgL7xEAEWepmFqg_kYmFcV-DLxaiDx3kY7ACdk-_tlSADCMz54UZX5xLJ4hDGxlun_SPJ_Al4OHZh8abNE0k-N7sxvh0-ZtvfLvaT3nvQcCtbhvMtrNo4Bsb_hChYtwnPUO9O-RgZix9DZy6AXKHXqzs5-IEGd4YzCCa_6hqhIbnrkF955oBcxJYjnuSUv51YfDSsvreFoP71ABpfnCFArrY82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOBba_Yf_kz9vVVgwpeTXAHr0ClCZ08Uq30wVi-hqrlqYRRGZqtAuU4MDn2baazTo6xTKUIPLIuUUsKEWbQLxRNR_I_mo31ErEhITUeZ88_xhPPGj1CvrhSLm04SfYD3FHf7td5HNpeG5E6a9xHWJ7cxplY1IemKBYLWdksqUuzjBFfGnzU6v4FMqsZfiiOrEH0D4J13eoeU4_HPIu02ccIgGpMcD80MytDq2pgVRqjFhaNbkDG_pIgnFMQIbfJ739uhyrKOHxrsTlYWLAEbjO6orcU8GHgF7v0hPIKB1EfFNPDZ9EkyeJqxB1aBrOu-kOFqU4rvpE1TFbfg0vP1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-2UC73fUAAhvHcfXsGgUdDgCBBR1aDx5EPQhrHq_mUqm3Jy6OC4NlDJ8nMgeqGXjJJeNT-fXYgmmrFtosy4gqV6T3dZvNMUwyuonEFEAU0XPZOzo3h-HCIddpkMJxw6aGBmajxGjL0EsysrVO4K33vtkJGlX9aABN1VfY2bp6l6gcEdbCxf3IqzuFqMLI4RyXPgolL2BTrITxT-F7jBVGY6w-wy3nwJ9UE5sVgbwpDL9mbnBbhtDwpR7sF7dMHrza5T1h34i259Ej8TBDP-YwAtNK4Ipx6QFdPe4D4BIJGhuR2kPCfP5QnJk1ZiCpp3kk7YsgFXTnRj-aMdqgNSuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری زائران اربعین در بین‌الحرمین
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454039" target="_blank">📅 16:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454038">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEVQrU-tr9vUVM-3Ksx-__3GS9co8pe0fdUvdLsYgqRc-lgf6gZLPN2lzsWGDNpzMqZPlPI3yQmJth5gIA5RR-XxaAkX2m_5Z8Ff6QSJGVoawvblMMNMNe9p0v6HYV_BxV505NoQnPRSbjkCjgjFFEjxSqyHahneh6W41BbMlS6ZgpuPr5DaG30XGU5oJ8ymlwr78brOdrQuk0Mk_9GQOr7GCrcIR_hh5VaPGcl5n-EGnqvWXy-vJ22iB9c6W1pqFqtMjBcjnkxRYjbOqZEwxqixK67qiZeBmssQYV1WkPEzqhbYSIHpF1y8WMiWDaeD3hdsiHdKYRk6sa56IGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح اینفانتینو و ترامپ به گِل نشست
🔹
بعد از مخالفت شدید یوفا، کونکاکاف و AFC با طرح فروش جام جهانی به بخش خصوصی، رئیس فیفا از توقف این طرح پیشنهادی خبر داد.
🔹
طرح جدید رئیس فیفا می‌خواست حقوق تجاری مسابقات مهم فیفا مثل جام جهانی را به ارزش ٢٠ میلیارد دلار…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454038" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454037">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbdb87e83.mp4?token=jnNb3cmNePlK3w-h1-Q6j9BqNrY4tmW_07Nd4ImhMQy0KKX7me8SMIeiXF5YqcYfu5ef8ewLM9C6hSB3IhbQAMUygeMbtSwZE9tmnVlZ6NBFlH8wKcwvjJm2kU3UaeBS-XGSmHcSRyGJ_RgdhI2aYvKsevqHv3_i49LMgSpBk5nDH3TxUZUesM1g2c2xTC-6kLmQCItDQjL8UsEBQp854ibocgxToPpbyOlEZ28TluKmQ575KhJ-rctUd_Sns0-ykF4zeTjXegFCT0Ne-2R6tXhXJ0WLxrJ-Dk8indjtern7g_YgxmD4YTd_SRDV-zKY3WrfQDleYcmZJWgVbE7vRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbdb87e83.mp4?token=jnNb3cmNePlK3w-h1-Q6j9BqNrY4tmW_07Nd4ImhMQy0KKX7me8SMIeiXF5YqcYfu5ef8ewLM9C6hSB3IhbQAMUygeMbtSwZE9tmnVlZ6NBFlH8wKcwvjJm2kU3UaeBS-XGSmHcSRyGJ_RgdhI2aYvKsevqHv3_i49LMgSpBk5nDH3TxUZUesM1g2c2xTC-6kLmQCItDQjL8UsEBQp854ibocgxToPpbyOlEZ28TluKmQ575KhJ-rctUd_Sns0-ykF4zeTjXegFCT0Ne-2R6tXhXJ0WLxrJ-Dk8indjtern7g_YgxmD4YTd_SRDV-zKY3WrfQDleYcmZJWgVbE7vRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح کاپوتاژ اتوبوس‌ها در مرز خسروی این‌گونه اجرا می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454037" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گرما اداره‌های خوزستان را دورکار کرد
🔹
در پی تداوم گرمای شدید استانداری خوزستان ساعت کاری ادارات استان را در روز دوشنبه کاهش داد و فعالیت ادارات در روز چهارشنبه را به‌صورت دورکاری اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454036" target="_blank">📅 15:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454035">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv68tC0uNh4ZplBOZf5lWzR7gVOzMSFN8WdlBOSmQY3KvrVYbUOZWeBCgZmLNFgw73k030sYknRfmV1zP398jcnMiqTsln_l8MCBPLAWWm_XF31N16xcILITXeNFcgf4FukoWu5HMWVMlv5uy7WhKo2LuVfa4kQBLSEfwjJS0J995VexOZVaxfLHn5Fd_-gE7xDnVeQrS7JdGI0FNTWIM1HMSW6HFapVex0SEbLceEatsx1iRr-Cl5SAwBp4trHvFxuD2BG8yfWbCepJrEoXdEn6xyn8SyMqAKOwY7Nyl-0WF6xxrMWG8sPWsZ6rxRmkAO9_u8eyqaGUvuBJCi1Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹️
مروری بر عقب‌نشینی‌های ترامپ از ابتدای امسال
@Fars_plus</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454035" target="_blank">📅 15:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNuJqXF0o4yAZJHvmHNlClEeOqMaDC3-UWf0QgOq43D89imJovEuU-GpGl7Dm5n7wh2J0haP_ghNgWmaxJXIHEDSXgsnnoR8yBJ2O5t0yXuFuaL7pVeddHicH4mONNepyOGxmBVQvsmnyOXYxqt0GxBN-xigEoNOs--6KRrMFWizQVjPncz91esyJqSKOgxz9SOpWTToTX-tXMr790a_yEX-q_h62wgeyOkcDNdVyq5bSlPNVPCIecc7FLlyYzevzq0CqPD9aRPXZtEJ9Lmk4DedbmzRHgCYfUC5u-Fb0mLWQoQUMdJrm8xM6kLrnO2TZCaRxoB2gki7lBDy5TP8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی اسکورت‌شدۀ آمریکا زمین‌گیر شد
🔹
منچ‌اوسینت، اکانت رهیابی‌های ماهواره‌ای، می‌گوید یک کشتی حامل گاز قطر در مسیر جنوبی تنگۀ هرمز لنگر انداخته و متوقف شده است.
🔹
بامداد دیروز شنبه دو نفتکش در مسیر جنوبی تنگه هرمز در آب‌های عمان، یکی در ۱۱ مایلی دریایی شمال‌شرق لیما و دیگری در ۲۱ مایلی شمال‌شرق خساب هدف قرار گرفتند.
🔹
یک منبع آگاه امروز به فارس گفت، «تنگه هرمز همچنان بسته است» و شناورهایی که از مسیرهای ناامن عبور کنند، «حتما دچار حادثه خواهند شد.»
🔹
منچ‌اوسینت می‌گوید که این کشتی در جمعه شب ۳۱ جولای تحت اسکورت آمریکا بوده و هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454034" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=MZ71_0J1SYAbExvVZ3Spn2womARG3FxniSyqcL2bn8WRW5yBy7rDXWuwghJNsvUyE76y6rau4j56LLVgxdb-6Iv35OH2d5mlSL2uYUcTLOvp47qmUaMENGC6VGMAUMwu9m1CfSEBTT7WPM5lJxZJJUOSO_XX_jFhFUQ0fwMlETwHiBW5NaDcPRWHe5MKLOZHBm5EWckOXOir_eCq5rqefBUD_QCaTQY2PJt1stmd95frXPN-0V6g5j6BGXUUsQkVPPr4RX-CXKOBOz78ebxKYH6FSLt_TCP7FgUWG2sZGqGAP4RM1aL3xncdPT5-t4GEkmueWNUc8jDNDC6SVgJymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=MZ71_0J1SYAbExvVZ3Spn2womARG3FxniSyqcL2bn8WRW5yBy7rDXWuwghJNsvUyE76y6rau4j56LLVgxdb-6Iv35OH2d5mlSL2uYUcTLOvp47qmUaMENGC6VGMAUMwu9m1CfSEBTT7WPM5lJxZJJUOSO_XX_jFhFUQ0fwMlETwHiBW5NaDcPRWHe5MKLOZHBm5EWckOXOir_eCq5rqefBUD_QCaTQY2PJt1stmd95frXPN-0V6g5j6BGXUUsQkVPPr4RX-CXKOBOz78ebxKYH6FSLt_TCP7FgUWG2sZGqGAP4RM1aL3xncdPT5-t4GEkmueWNUc8jDNDC6SVgJymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راویان پرچم سرخ» روایت اربعین را به شبکه سه می‌آورد
🔹
مستند «راویان پرچم سرخ» با محوریت سفر کاروان اهالی هنر و رسانه به پیاده‌روی اربعین، امروز روی آنتن شبکه سه سیما می‌رود.
🔹
این مستند امروز ساعت ۱۶:۳۰ پخش خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454033" target="_blank">📅 15:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454032">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c250a3573.mp4?token=UTWbtlqD4BBhMbWCVWAZJdUAi80HYYELQnDvfNbhOYwl7eFaWVI2yNy_8KLpwxx06uLEp9XBiywdYtD4zHTIDjrMyaZG0q9H8EcKcxRJePOW-glFzEwrmy3S78yvpWQ8GF8KcIkznBbrgmnGOYyVm_PFTi5EdwpVXdHn6fZLPSpLC3i1y8p-Nt196PUr6nKLORBx5LCkP-CzEQ53KNmNBebuURDvw06JQUwWGGq2F3kskySktEKVYUwsOEtFZe4iOGVcEt-uAhJGcBay9JB78L_SNORQ_fCETnm7NhIbVBIwOUS9RKnIs29T7dHVhx4qK9ce1QDhNfO8C8BuNBWk0FPWE7-LC378KXLFNbd_WVTI0SXCqI1nMfkv_4cUpGoB8HsQ0WiHKfiNtFGUOqlNt4ffdYzyFoMbTYZ4vGHlK6ttYnc5YG1Na6dD12j8tOoHep7NhqcJzdZ2_vcg_krNiz5mSdedYcwSCT_erPnfL_0mgTM2a_Kug7FTVMSWhw863PgtvHnCPgvk687AAWxnEcfaE__hw-fogfl0ua6NxxtJLNR6i2yICuWn53dUyRLBvr5BMg0i07o_d_3eeMiD5k6ILxnKSh7WwiWZQxSOAfD9lOxzPBnOApvxXTb639IZA2SZ2hwIkJkVB9nSd0_MZmPJK_V0s_A2RseYBz2YqK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c250a3573.mp4?token=UTWbtlqD4BBhMbWCVWAZJdUAi80HYYELQnDvfNbhOYwl7eFaWVI2yNy_8KLpwxx06uLEp9XBiywdYtD4zHTIDjrMyaZG0q9H8EcKcxRJePOW-glFzEwrmy3S78yvpWQ8GF8KcIkznBbrgmnGOYyVm_PFTi5EdwpVXdHn6fZLPSpLC3i1y8p-Nt196PUr6nKLORBx5LCkP-CzEQ53KNmNBebuURDvw06JQUwWGGq2F3kskySktEKVYUwsOEtFZe4iOGVcEt-uAhJGcBay9JB78L_SNORQ_fCETnm7NhIbVBIwOUS9RKnIs29T7dHVhx4qK9ce1QDhNfO8C8BuNBWk0FPWE7-LC378KXLFNbd_WVTI0SXCqI1nMfkv_4cUpGoB8HsQ0WiHKfiNtFGUOqlNt4ffdYzyFoMbTYZ4vGHlK6ttYnc5YG1Na6dD12j8tOoHep7NhqcJzdZ2_vcg_krNiz5mSdedYcwSCT_erPnfL_0mgTM2a_Kug7FTVMSWhw863PgtvHnCPgvk687AAWxnEcfaE__hw-fogfl0ua6NxxtJLNR6i2yICuWn53dUyRLBvr5BMg0i07o_d_3eeMiD5k6ILxnKSh7WwiWZQxSOAfD9lOxzPBnOApvxXTb639IZA2SZ2hwIkJkVB9nSd0_MZmPJK_V0s_A2RseYBz2YqK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در مورد قاچاق برق چه می‌گویند و برق‌آشام‌ها چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454032" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454031">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roIOSzudX2nQrxQdPHSOlaw9dHUkKdNpodvsYLcGO2KKCvONqrLBJXfZJNXTt9JLTtZnZUw5yEKoWbVUIH8-PUFahw3uaaM4rOgt0DdV0yXBnc4z6y_khBrx6oJGH0Fnpy_9Dr8lWtmTVlNWB4qjOi7lus5y5HM_61GJCEMtIsgXRrN-waV_EY_VZ-wpMzxC8wuuu7uvTgbHmb2LbZ9n2JS_5on-CzSSXhBsfoKbcWJ2YkNWO3EwzCbIvmPK-Zp9LpUSBKmeF6v0FFJ75KbZBcpDOJqwPkfQELuXPExT_FlNywujIx3A7_jZNWe6WNI_SBvD6xmMJme0PmgX0NCgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه خرید سنگین،با اقساط سبک!
✨
فرش دلخواهت رو با
اقساط تا 2 سال
بخر!
❌
بدون ضامن
⚠️
بدون بهره
با ارسال رایگان به سراسر کشور
🚚
🛑
فرصت محدود
🛑
4شعبه فعال:
📍
شيراز،خیابان عفيف آباد
📍
شيراز، پل كشن
📍
شيراز، ابتدای دوكوهك
📍
بوشهر،باغ زهرا
براى ديدن مدلها و اطلاع از جزئيات بيشتر همچنین مشاوره رایگان، يه سربه سایتمون بزن
👇🏼
https://jryn.me/bWa2AE</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454031" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454030">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454030" target="_blank">📅 15:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن آژیرهای خطر در اردن خبر دادند
📝
منابع اردنی مدعی شدند که صداها مربوط یک «هشدار آزمایشی» بوده که به موبایل اردنی‌ها ارسال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454025" target="_blank">📅 15:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bbac32d6.mp4?token=n57-l4h7bltVQmoP2bgvTq13CEEHPdbysvL2IH94VxoVX5DcnK3pNT2YSrvYw19iTxuqEzi89R7rNdU8ZwIXhX-mJY2iF8HvbeBWnV4elEDqwwUz77bSex6BpHQu5e6oWJReHISHBHdUjn33zyF8ZqzHddXIgJ58FGmt_66L2xcKoVWnwm0Feo_CvANZ9NIjJNNfYnqeYQ5snEMItt2JTFRaQK33TSTZZw1m3lZZmRTRhXKKOXydOrEr4OmXwJH4MGBpkhteBvhalpM9vZLZjiiES6JS8NnveFx0M7Xp4s9eD05qQP0AkFe5fNYUD6r4Klpoq5fn9z8sRTyeyiyyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bbac32d6.mp4?token=n57-l4h7bltVQmoP2bgvTq13CEEHPdbysvL2IH94VxoVX5DcnK3pNT2YSrvYw19iTxuqEzi89R7rNdU8ZwIXhX-mJY2iF8HvbeBWnV4elEDqwwUz77bSex6BpHQu5e6oWJReHISHBHdUjn33zyF8ZqzHddXIgJ58FGmt_66L2xcKoVWnwm0Feo_CvANZ9NIjJNNfYnqeYQ5snEMItt2JTFRaQK33TSTZZw1m3lZZmRTRhXKKOXydOrEr4OmXwJH4MGBpkhteBvhalpM9vZLZjiiES6JS8NnveFx0M7Xp4s9eD05qQP0AkFe5fNYUD6r4Klpoq5fn9z8sRTyeyiyyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر اتفاقی بیفتد خودم را به اینجا می‌رسانم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454023" target="_blank">📅 15:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
۵ نظامی ارتش لبنان در حملهٔ رژیم صهیونیستی مجروح شدند
🔹
فرماندهی ارتش لبنان از مجروحیت ۵ نظامی در شهرک کفرا در بنت‌جبیل بر اثر حملهٔ خصمانهٔ ارتش اسرائیل خبر داد. این حمله زمانی رخ داد که یک خودروی ارتش لبنان در حال همراهی اهالی شهرک بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454022" target="_blank">📅 15:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bbd64b9.mp4?token=HQEGuLL1rlklZGFDs48E4XYh15qUSqx5UNYw5f2bfIkT-meS0Y76812KlMa-skPMKDmYBO_i5rkf8j1rEeOapAZPdNmpHlDZv-AEENq4oNKROzTvAbWbuFhO1LSGBqSdhSunNrZ6AgB-CeH62HWjNLNLmyni30FMApYrkmimPtwA3ye1TXKLCqhIlnppCvPPv9DkJgjxOyaQ4Lx-o2VYEg899dQ0uGpnof29hTIhHYB5QwjJiZ67q6i-RxAQ6VcZBLiitY_c1bocnu-CWyLQtXqmXVEWpAZ09SeVwhrhJ0Nqux17cGtDIpar0kGR8Jy7TDapxz15O-aEAgr9Fv7fXBkpRlFVXA1KZ844UwB7P6b9lbJ61A04tB_yJnwm_wW3ENB61Cadd53gwGYJQyN2Rva3bZzvAy1FJk6_biIfeziCIO80oYOggKSFBlCiL7eGRRXzsyrgCo2ICO6W1NwzuC75vuoAki2nSsH0xbGsq8BWsYMfYMzba7D9UP5Q0RM2ONrzomrGQi4YDPKUXimVtbGuAsq72AZIkYfy9p1guHkVxCeWF8n9xBtTN3cuBGySCcohC_cg4pnIUSwpvoKzhG6PhRHsr18dDtJxpX-cfAILUNGqh2Y0_BblYSaeLViUCh346f8_v5Z_FyWP9hhpMq6G9w8vvRx6ZTJ5HjpA294" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bbd64b9.mp4?token=HQEGuLL1rlklZGFDs48E4XYh15qUSqx5UNYw5f2bfIkT-meS0Y76812KlMa-skPMKDmYBO_i5rkf8j1rEeOapAZPdNmpHlDZv-AEENq4oNKROzTvAbWbuFhO1LSGBqSdhSunNrZ6AgB-CeH62HWjNLNLmyni30FMApYrkmimPtwA3ye1TXKLCqhIlnppCvPPv9DkJgjxOyaQ4Lx-o2VYEg899dQ0uGpnof29hTIhHYB5QwjJiZ67q6i-RxAQ6VcZBLiitY_c1bocnu-CWyLQtXqmXVEWpAZ09SeVwhrhJ0Nqux17cGtDIpar0kGR8Jy7TDapxz15O-aEAgr9Fv7fXBkpRlFVXA1KZ844UwB7P6b9lbJ61A04tB_yJnwm_wW3ENB61Cadd53gwGYJQyN2Rva3bZzvAy1FJk6_biIfeziCIO80oYOggKSFBlCiL7eGRRXzsyrgCo2ICO6W1NwzuC75vuoAki2nSsH0xbGsq8BWsYMfYMzba7D9UP5Q0RM2ONrzomrGQi4YDPKUXimVtbGuAsq72AZIkYfy9p1guHkVxCeWF8n9xBtTN3cuBGySCcohC_cg4pnIUSwpvoKzhG6PhRHsr18dDtJxpX-cfAILUNGqh2Y0_BblYSaeLViUCh346f8_v5Z_FyWP9hhpMq6G9w8vvRx6ZTJ5HjpA294" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: قانون سقف بودجه موفق نبود، فیرپلی مالی جایگزین می‌شود
🎙
رئیس فدراسیون فوتبال:
رسانه‌ها باید بدانند که بحث فیرپلی مالی امسال که توسط سازمان لیگ فوتبال ابلاغ شده، به لیگ برتر منتقل خواهد شد و انشالله امروز یا فردا به لیگ یک نیز ابلاغ خواهد شد. واقعیت این است که فیرپلی مالی در واقع جایگزین ثبت بودجه‌ای است که قبلاً ابلاغ شده بود و نتایج موفقیت‌آمیزی را به همراه نداشت.
@Sportfars</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454021" target="_blank">📅 14:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4366d95c13.mp4?token=DZEccSG2qPhxNDd5cPFcMpQ6li0AK0x1L_Hu4Nop0NKAfWvdslQsdFTNmG4-8t7DwhMd7zUV4k6GiZFx4ONKYFB0kxqmM475yr0tVrqPzJXfbERepT-LO_QPJTMqGaUTmvSiVI1Xx87k3x1wEHJeOt0l4tjnuenTNK9ug4dHp3sJynNqLF21Jp3vxMitEmQCVaIxhNxiv306JOI4Y0YP7rwvEDhP5edMPDbveDRAs0GGT76db4PzsTiPq5MF1uj3LOwmTKYGinabAi2q-gAWKezyb_jLoMxSjOlsbembxzieqO5D5zeiHG9ePMxdDnCPx9RWZjKSeWMymu8vnCsMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4366d95c13.mp4?token=DZEccSG2qPhxNDd5cPFcMpQ6li0AK0x1L_Hu4Nop0NKAfWvdslQsdFTNmG4-8t7DwhMd7zUV4k6GiZFx4ONKYFB0kxqmM475yr0tVrqPzJXfbERepT-LO_QPJTMqGaUTmvSiVI1Xx87k3x1wEHJeOt0l4tjnuenTNK9ug4dHp3sJynNqLF21Jp3vxMitEmQCVaIxhNxiv306JOI4Y0YP7rwvEDhP5edMPDbveDRAs0GGT76db4PzsTiPq5MF1uj3LOwmTKYGinabAi2q-gAWKezyb_jLoMxSjOlsbembxzieqO5D5zeiHG9ePMxdDnCPx9RWZjKSeWMymu8vnCsMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت عاشقان امام حسین(ع) از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454020" target="_blank">📅 14:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d985612758.mp4?token=gOhzthbIxrcfBlyITplsunqhi3BdyNURyZvs12edd-n0RXxrbYcdrGT77KtMxvg1nkNOrb-ztenpiBK6fByHTDF9QyTVv9ewRUTJRc4O0P0DD0dytS6FAZyvoJOs3r-4vFN6KWEuZHuehxY69cjdDm4ln_QwB9vdHGp4oZSx1NYeEQOOFgpsedDceYqzLhVfNTHc5TuzETf2sE_2PWVzbjsXwldSmrvLSAkaywYLBPgktN5p-tN3w2uXyPWsXEP6c1bVytXltkr1qytnE0UOJDDJ-nz9GknIzsY1swnDEyAGKKT7taHOj0Jn8N1YuDcAvER2in_mAftwGVp6k_RWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d985612758.mp4?token=gOhzthbIxrcfBlyITplsunqhi3BdyNURyZvs12edd-n0RXxrbYcdrGT77KtMxvg1nkNOrb-ztenpiBK6fByHTDF9QyTVv9ewRUTJRc4O0P0DD0dytS6FAZyvoJOs3r-4vFN6KWEuZHuehxY69cjdDm4ln_QwB9vdHGp4oZSx1NYeEQOOFgpsedDceYqzLhVfNTHc5TuzETf2sE_2PWVzbjsXwldSmrvLSAkaywYLBPgktN5p-tN3w2uXyPWsXEP6c1bVytXltkr1qytnE0UOJDDJ-nz9GknIzsY1swnDEyAGKKT7taHOj0Jn8N1YuDcAvER2in_mAftwGVp6k_RWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی کشتی در اندونزی با ۵ کشته و ۴۱ مفقود
🔹
در پی آتش‌سوزی یک کشتی مسافربری در آب‌های اندونزی، دست‌کم ۵ نفر جان باختند و ۴۱ نفر مفقود شدند.
🔹
طبق اعلام سازمان ملی جست‌وجو و نجات اندونزی، علت آتش‌سوزی هنوز مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454019" target="_blank">📅 14:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZMNx6lPKDaFhcd2_5yCA9PbKPQ2jA69yc1GBU1ycVg2h0Gn5QN1L-PWXU2fj3vKpAbEEMjzm1BEeVT0zfQXY30kzd9y0ZBEf9O1GXiq_4YQ2-tjkDZPeMoDsRX5rgwo5-8QHP4rgVSCI04rxNoNyWeq3lamLE-qnO7Yy96lcHnAkYWOYc5zFayXympvvL6XHd_Gt23lA3kXImgxkj2EQ8hHoW9fW_RHAjGr07mo6pKqqD3AhjGdM5ficj87juC423C2Mh1oFcx3UkNV759AVFVp4zoEoZv96pikNMGGLhoq_9M6_0RQ_llBopa9fPBUxYsVnB7tZ1JKBmd4hAwRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: زائران برای کاهش ازدحام بازگشت، مرزهای باشماق و تمرچین را برای تردد انتخاب کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454018" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454014">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcIJ8E_LXqIM8G7sgy-bjhEYFM6h7zVFVejLM6wy-x-Zv8zMlNKVJ6ueuPQRfPhGj0PuiXDB2laouVmSKSNaComPdoARcovU27HJlc4hLkkqLUPmjk62WiC7Aic06EU_8Lwdlq4yQb3kHqz052Ki7vWTBPALvvcAGLIWp6nWUPCFAZiK0NU_o5eH5T7a1UZp5N4wS81TVV1hy64WNnnon6RyUWWvsTZmOwXyjbL4S_1wUzaoH2eiFVavt9LdAIq082hbcfWl254PbwnNwwZ-MWq7NTb5PWbc1riHYlKLw4IK_9Xz3h-y1IJeZUxM6t1v7vDIklKBgP9c1o1hxUeD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دلیل نوسانات و تغییرات در اخلاق و اظهارات رئیس‌جمهور آمریکا، رسانه‌های شهرک‌نشینان صهیونیست او را به سخره گرفتند و تصویری را منتشر کردند که «پیش‌بینی وضعیت روحی ترامپ در روزهای آینده» را نشان می‌دهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/454014" target="_blank">📅 14:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454013">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=i48ZCd-EcsWv0_ny_jp2RMIorXtxg8V4gI010HoHUvgeyC4Xyci3sNt7-CsiGzkrQL5IqF9hlPHtG2JttDvrfMgMmgFvkOrw-pkmedFi9hXXYHmcWrPtsvY6xj42_TZNC3ssasiyxwUX0ADe5IrrrZb6JFX2B1KgW1dcILzLMUSIKUf_8TTTWfjqDSC_r8Uj35vL0Q7Bco9zF4HWkEkpwK97y15G0yPO9DkcQy5rAo2wKflvPdbyvWbv1S3LI3mooCDDQNx4ZXxw91e5I57xYoI2n3YQ-rNO7fRBNQJoCocFmoaGqB5DNjIiVU8_DmuN4zRNmHPVY7HCr1vboJuw7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=i48ZCd-EcsWv0_ny_jp2RMIorXtxg8V4gI010HoHUvgeyC4Xyci3sNt7-CsiGzkrQL5IqF9hlPHtG2JttDvrfMgMmgFvkOrw-pkmedFi9hXXYHmcWrPtsvY6xj42_TZNC3ssasiyxwUX0ADe5IrrrZb6JFX2B1KgW1dcILzLMUSIKUf_8TTTWfjqDSC_r8Uj35vL0Q7Bco9zF4HWkEkpwK97y15G0yPO9DkcQy5rAo2wKflvPdbyvWbv1S3LI3mooCDDQNx4ZXxw91e5I57xYoI2n3YQ-rNO7fRBNQJoCocFmoaGqB5DNjIiVU8_DmuN4zRNmHPVY7HCr1vboJuw7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع آگاه: طرح بازگشایی تنگۀ هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
🔹
همچنین یک منبع آگاه نظامی تأکید کرد: تا زمان ادامۀ اقدامات خصمانه آمریکا،…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/454013" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454012">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoNWYDGDolwm7cTCsi36IKevyLwL3sqnXvpjiOh10g06VGnheSSC5DxOqzbf8M-JH281_LL3e1nzl9W1cabZOUCKZ-NaO-5iJNcJ0V3TXimdHVELyonc4UwG34oRhyW10DpZGPi8vvdTUol2qviPYQzne0uW3ztO1R09kH-lNjqlgarHcGLbblbE37oY0svAg976jKLKy9e0f9FXZZjVn-TLihNLZ-Y6T5HL3yVIs2USjmcLPtefPT4YQvMYvLSoFX9xhckaQFUDmXY5IDjB24ZIDWS38wy0IcmVeLq24OolG7k9wYeDsiw9aE6ddFZdjzxMzlI2jWyaMSFf9xmheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ هم حریف لابی واردات از امارات نشد
🔹
شایان نادری، معاون وزیر سابق جهاد کشاورزی می‌گوید که «لابی واردکننده کالاهای اساسی از امارات» آن‌چنان قوی است که حتی بعد از جنگ هم مسئولان را می‌ترسانند که فقط از ۲ بندر امارات می‌توان کالا وارد کرد.
🔹
واردات کالا از بنادر امارات در جنگ متوقف شد با این حال ۴۰ روز پیش، قنادزاده، معاون سازمان توسعه تجارت، گفت که تجارت با امارات با شیب ملایمی درحال انجام است اما «امیدواریم به شرایط عادی قبل از جنگ بازگردد.»
🔹
واردات کالاهای اساسی در ایران انحصارا در اختیار چند شرکت بزرگ است که در بسیاری از مواقع کالا را نه از شرکت‌های بزرگ تولیدکننده بلکه از امارات می‌خرند. تسویهٔ پول نیز از طریق تراستی‌ها و از مسیر غیررسمی انجام می‌شود.
🔹
فعالان حوزهٔ تجارت می‌گویند «کارمزد انتقال پول از مسیر تراستی‌ها در برخی معاملات ۱۰ تا ۱۵ درصد ارزش معامله است.» یعنی تسویه یک محموله ۱۰۰ میلیون دلاری حدود ۲ تا ۳ هزار میلیارد تومان برای تراستی سود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454012" target="_blank">📅 13:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700d519c63.mp4?token=QEoCqaSkpIfIgW9EoTUgZwvExxwMONDNxV-VbSbvcGJF6qnPzggu1rbKjPTJqEJLOmb8aoNzcmXNn8mTIXuzrlJOHo6nvxAMTP15QPYMz9nkoorHmMoEyv0-rD52vNm9wSdf7HRar3csz0bl82mfKWZOViliEhOqG24ZfX4wC0E-9Nw9TfurorKNOzP5J4BgRKLfxMBbpxq-X8CMNaLw9o3B285chMDCnVdvmtqKN_m8yf--NBffbTK-0oAqcAP0m-w6cew9qQMVxz6wDHNIlqrfdxdISijxgVgzXpAPwvGDbK7ly1cD4l-8zt26Mk-dYhHkBe0XK8de1hIML2-htVQPqSewDVUnF7Qjod1EX3H43DftSt7yQ3OjMlH0EKmgr6gw5z6RBIz_o16phdL-gTXfp8410WiIuRggUXINUCk6DUM4WbH_iWcfpxHVLr9mgN4N72zCUZ_NUtwLX6lPZ0FH22xNNUG3ZTDGoioi8J9sjZAJNmX4STDZWmEcTVo1QPPt13qxY1xU6s1_p5PiMttxN0Pp4phzygjLf-t29PjkHTuWzTAhVOuy1oaeVKnyHTswx6EBf9wHKqEv5IRiDiDQBcPlLbp4G-NRd1l3nqhQE9m_k08KPQmfYWbpD8EvJKyRBJ9KlJzi0V--AMslzcsEO07Nv00KOYIe3d6HOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700d519c63.mp4?token=QEoCqaSkpIfIgW9EoTUgZwvExxwMONDNxV-VbSbvcGJF6qnPzggu1rbKjPTJqEJLOmb8aoNzcmXNn8mTIXuzrlJOHo6nvxAMTP15QPYMz9nkoorHmMoEyv0-rD52vNm9wSdf7HRar3csz0bl82mfKWZOViliEhOqG24ZfX4wC0E-9Nw9TfurorKNOzP5J4BgRKLfxMBbpxq-X8CMNaLw9o3B285chMDCnVdvmtqKN_m8yf--NBffbTK-0oAqcAP0m-w6cew9qQMVxz6wDHNIlqrfdxdISijxgVgzXpAPwvGDbK7ly1cD4l-8zt26Mk-dYhHkBe0XK8de1hIML2-htVQPqSewDVUnF7Qjod1EX3H43DftSt7yQ3OjMlH0EKmgr6gw5z6RBIz_o16phdL-gTXfp8410WiIuRggUXINUCk6DUM4WbH_iWcfpxHVLr9mgN4N72zCUZ_NUtwLX6lPZ0FH22xNNUG3ZTDGoioi8J9sjZAJNmX4STDZWmEcTVo1QPPt13qxY1xU6s1_p5PiMttxN0Pp4phzygjLf-t29PjkHTuWzTAhVOuy1oaeVKnyHTswx6EBf9wHKqEv5IRiDiDQBcPlLbp4G-NRd1l3nqhQE9m_k08KPQmfYWbpD8EvJKyRBJ9KlJzi0V--AMslzcsEO07Nv00KOYIe3d6HOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
به نظر شما، شهرداری تهران امسال به شهروندان مسئولیت‌پذیری که عوارضشون رو به موقع پرداخت کنند، چه جایزه‌ نفیسی تقدیم می‌کنه؟
✅
روش مستقیم پرداخت عوارض خودرو و ملک (شامل نوسازی، مشاغل و پسماند): سوپر اپلیکیشن شهرزاد
✅
دور جدید قرعه‌کشی بزرگ شهرداری به زودی برگزار می‌شود ...</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454011" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454010">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNuonlJLOPvkRD5Kr5gG7PpeoUip6qUpfF_Cj5Qo3c6WS11ihbtML80hOWAj4hOLUtSBtixWV_mdePpNeSg6Ww2ZLdOi_QnnfG4w87TJ2_a8I4NdFyxmdl8CIvXpyq5n9uFMzJza6XkxBESiE19Eud8DCiZ9u4Auyp1YIrPeCCvpgGOW34iZKKvDy7aELSOIof94lbMLkjDHh_jcQSCwxFZdnT-TG2RFbsbc8GBl5MtfEKimMe9_z-_vcoDVWMcBjRkBfAXm3bV7BAFVe_FjVwk1113aSSeUdzITbWfNpkAyeKjQIdTB8fTTDFf8gozQsGmB_D1Db1bnW0tHJ7YAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ساخت داخل ۹ همتی تجهیزات و قطعات کارخانه‌های مس در سال ۱۴۰۴
🔰
صرفه‌جویی ۱۲۵ میلیون یورویی مس ایران با بومی‌سازی در پروژه‌های توسعه‌ای
🔻
شرکت ملی صنایع مس ایران با اجرای برنامه‌های بومی‌سازی تجهیزات و قطعات موردنیاز پروژه‌های توسعه‌ای و بخش بهره‌برداری، در سال ۱۴۰۴ از خروج حدود ۴۹ میلیون یورو ارز جلوگیری کرده و مجموع صرفه‌جویی ارزی حاصل از قراردادهای بومی‌سازی این شرکت به ۱۲۵ میلیون یورو رسیده است. همچنین جلوگیری از خروج حدود ۷۶ میلیون یورو ارز در پروژه‌های توسعه‌ای سال ۱۴۰۵ در دستور کار قرار دارد.
🔹
در سال ۱۴۰۴ تعداد ۷هزار و ۵۵۷ آیتم از قطعات یدکی موردنیاز کارخانه‌های شرکت ملی صنایع مس ایران در داخل کشور تولید شده که ارزش آن حدود ۹۰هزار میلیارد ریال بوده است. این بخش در مقایسه با سال گذشته، از نظر تعداد قطعات ۱۷درصد و از نظر ارزش قراردادهای ساخت داخل ۵۶درصد رشد داشته است.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sg
@mespress_ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454010" target="_blank">📅 13:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454009">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454009" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454008">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">با
بانک‌های متخلف در حوزهٔ وام ازدواج برخورد می‌شود
🔹
معاون امور جوانان وزارت ورزش و جوانان: با وجود اینکه سالانه بین ۴۵۰ تا ۵۰۰ هزار وام ازدواج پرداخت می‌شود، اما همچنان ۵۵۶ هزار نفر در صف انتظار هستند. متأسفانه بانک «سرمایه» با فقط ۲۵۰ متقاضی ثبت‌نام‌شده، هیچ پرداختی در این زمینه نداشته است.
🔹
تعاملات نزدیکی با سازمان بازرسی کل کشور برقرار شده و پیگیری‌های حقوقی برای احقاق حقوق متقاضیان در جریان است. بانک‌های متخلف جهت برخورد قانونی به بانک مرکزی و مراجع قضایی معرفی شده‌اند و این روند تا رسیدن به نقطه مطلوب ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454008" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40be920e6.mp4?token=UYHQG8QabAj3BhSukSnDIlCzvHKuaVOU6v4AyytYkInnQzHmYcrR-8vD6TRDG9Inb2YufyWdgxDaY6dIuU7fAzJuouMQci9mFPDetTiWPWTmjOQyx3oRtsfp4kWsJ-MzRR7k0Km3epePooL1fSiV2t1DVH4GQGcn8SZLzcr-xr8TX_YCChSRnGseZJ91f_3CaRm2cP0I9qzC2R782dh7hdj0ADo3-c_76IFSd8uJX_-EE8mJKxuuIwDcOVDkC0U_AdIt98bZjnGpCHoSXvWN8lx33KiNxl0f3pBwhrQ9wQopljjgCwGnppxvcd1VO9t_F_4pKJgP1MAmCQx9hQXZgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40be920e6.mp4?token=UYHQG8QabAj3BhSukSnDIlCzvHKuaVOU6v4AyytYkInnQzHmYcrR-8vD6TRDG9Inb2YufyWdgxDaY6dIuU7fAzJuouMQci9mFPDetTiWPWTmjOQyx3oRtsfp4kWsJ-MzRR7k0Km3epePooL1fSiV2t1DVH4GQGcn8SZLzcr-xr8TX_YCChSRnGseZJ91f_3CaRm2cP0I9qzC2R782dh7hdj0ADo3-c_76IFSd8uJX_-EE8mJKxuuIwDcOVDkC0U_AdIt98bZjnGpCHoSXvWN8lx33KiNxl0f3pBwhrQ9wQopljjgCwGnppxvcd1VO9t_F_4pKJgP1MAmCQx9hQXZgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاموشیِ تنها نیروگاه اتمی مجارستان به‌دلیل کمبود آب!
🔹
نخست‌وزیر مجارستان با اعلام تعطیلی نیروگاه هسته‌ای این کشور «به‌دلیل کاهش شدید سطح آب رودخانهٔ دانوب»، از محدودیت برق و احتمال جریمهٔ مصرف‌کنندگان خبر داد.
🔹
نیروگاه پاکس در ۱۲۰ کیلومتری جنوب پایتخت مجارستان، از آب رودخانهٔ دانوب برای خنک‌کردن رآکتورهای خود استفاده می‌کند. این نیروگاه بیش از ۴۰ درصد برق مجارستان را تأمین می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454007" target="_blank">📅 13:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
منابع آگاه: طرح بازگشایی تنگۀ هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
🔹
همچنین یک منبع آگاه نظامی تأکید کرد: تا زمان ادامۀ اقدامات خصمانه آمریکا، تنگۀ هرمز همچنان مسدود است و عبور شناورها فقط از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه امکان‌پذیر خواهد بود.
🔸
ساعاتی قبل برخی رسانه‌های وابسته به دشمن با انتشار اخباری مدعی شده بودند ایران با طرحی برای بازگشایی تنگۀ هرمز موافقت کرده؛ طرحی که براساس آن، ورود کشتی‌ها به خلیج فارس از طریق آب‌های سرزمینی ایران و خروج آن‌ها از طریق آب‌های سرزمینی عمان انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/454006" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWt9aXes-YjFFkrNfEe3TtLJ7uAGt57H79G1ki6UxU0slSvCEW38XdZWz1q-CzUB3no-4RZBmrcFKOCV1GpOJ3_GXKcGsqFBLZ-M4-0Kx37rkUPUWgRZ_NtY0ufQ8AKgpqz52tUWHx_FSFDpMyWSOwZeqEiQoPjO9htkRqICxXzRgzPzsK4LdtclACCqpwdFq544qYcYuMhqlrp5CF4tExpJ8ZQAHUFzuGuKosxudSMBHCHKdf21wzvT9gcO2rqxxw3ePwV6MCyVqWDGU6j__3mrNs1FMk3iImDN9OKn2eUK_lAHS0bcwWbI2cj-5-mxR85XOgJoj7MzBtDJORRhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ۹۹ هزار واحدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۹ هزار واحدی به ۵ میلیون و ۱۵۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454005" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLknFKPto43MxFj6FZI2FYNEgDyK0ZX8wGb9yhtF6n8hhlmuYUYT7GQDx4Wim3iPRtdp2z3ht4VDVK-uBz6UxA5p5YSSPM9oFQB5OiCYhwBzMuvEqrtOCYCXlvRD5lsycNMBMi2japzc4upw7mEVkjS34Fv31vqBvnJOFLmKUt-NaA0Ud2XybMbPecfhf8PwTAqa-vm5rPNpE65D7QD_wF9cEwWXYcFBHdZku26bK8ML3TztwcpP9PaFgtL2FQsZrz5jCcaabwMGCtSuBJpDS-w60rd1OtpQvTcBtbGyGrkRm0UYjuHZ09NwRrMYXS3sG168lad3qpafcLrGM3MbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار رئیس قوه‌قضائیه با آیت‌الله جوادی‌آملی
🔹
اژه‌ای دیروز در سفر به دماوند، با آیت‌الله جوادی‌آملی دیدار و گفت‌وگو کرد و در این دیدار گزارشی از اقدامات، برنامه‌ها و فعالیت‌های قوه‌قضائیه و آخرین وضعیت برخی موضوعات مرتبط با این دستگاه ارائه کرد.
🔹
آیت‌الله جوادی‌آملی در این دیدار با اشاره به جایگاه سوگند و دلایل در فقه اسلامی گفت: علم غیب، مبنای صدور احکام قضایی نیست و معصومان(ع) هم در مقام قضاوت، براساس دلایل، شواهد و سوگند حکم صادر می‌کردند. اگر فردی با شهادت نادرست یا اطلاعات خلاف واقع حقی را تصاحب کند، مسئولیت این اقدام بر عهدهٔ خود او خواهد بود.
🔹
آیت‌الله جوادی‌آملی همچنین حضور گستردهٔ مردم در عرصه‌های مختلف را جلوه‌ای از نصرت الهی دانست و با استناد به آیات قرآن کریم بر نقش ایمان و حضور مردم در حفظ و تداوم نظام اسلامی تأکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454004" target="_blank">📅 12:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a76ec0973.mp4?token=bPR4b5MvBsNv2-isDFJS50K7jmx2YjsU3NN1H851lhdWK-Cwv0fXIGDcLn9BTAAfwyxMFv-s9Buk58R0OuLAECkSH-dadQig0hR6Nexv3HAqWRty9xYHSA8xbt-00KrrtTKsO0US0RLMmVLEhZHSJOfgZxea7HnOnbvE0x3356gaI_DgeCz7WFwUcp36hnfhj2ztPCRIIlBloSrwG1U7gg6TH8xagqxndaKwYh9m9ZH5syEfEY0hqwOjsw8nhR_-6oGHa-WE0HuQFfL0AtOEsVajdFJuJ48CzgyrTTWpdsSz-upcsTRWfp0jsBIn3LrgzXhGk3ELujz39XExC4kF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a76ec0973.mp4?token=bPR4b5MvBsNv2-isDFJS50K7jmx2YjsU3NN1H851lhdWK-Cwv0fXIGDcLn9BTAAfwyxMFv-s9Buk58R0OuLAECkSH-dadQig0hR6Nexv3HAqWRty9xYHSA8xbt-00KrrtTKsO0US0RLMmVLEhZHSJOfgZxea7HnOnbvE0x3356gaI_DgeCz7WFwUcp36hnfhj2ztPCRIIlBloSrwG1U7gg6TH8xagqxndaKwYh9m9ZH5syEfEY0hqwOjsw8nhR_-6oGHa-WE0HuQFfL0AtOEsVajdFJuJ48CzgyrTTWpdsSz-upcsTRWfp0jsBIn3LrgzXhGk3ELujz39XExC4kF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشق، خستگی را از رکاب‌هایش گرفت
🔹
پیرمردی که مسیر ۲ هزار کیلومتری از خراسان تا کربلا را با دوچرخه طی می‌کند، می‌گوید: «ترس در زیارت معنایی ندارد و خستگی در مسیر عشق به حسین (ع) رنگ می‌بازد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454003" target="_blank">📅 12:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_krRhbniHSDMTrAuYvLNklWAbq2SvluFTe46SxJo4U8BicogyewVnPvfygTgRGToJN39lR31VpiMBNoX2zWKV-tfiHpnoEReR6JlkyKIOLC7ifQVzR_pctk8fa5HR7kb0342yYYQhlk7qZTEW9EJpd648E_GU99qyun4oQ0izuoV6zkfnBKOusEZCKOyEdDSBMTW0sk5P5HrJGaD5VFceQJzXp0DtU0Xi74YXU3UCNVniZ--6J09C03XulTHll2jfNVdcjYCvwc-9uyC0KBmHNgWpWRCq4DlWSrfFpv_DiIeaO_iokp__hXQJNBqzdgqnXcr-b9GGzZVEGotpfSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سی‌ان‌ان از عوامل عقب‌نشینی ترامپ
🔹
بعد از عقب‌نشینی ترامپ از تهدید دوباره‌اش به تشدید حملات نظامی علیه ایران، سی‌ان‌ان در تحلیلی به قلم برد لندون، خبرنگار ارشد امور نظامی این شبکه، گزارش داد تحلیلگران فشارهای اقتصادی ناشی از جنگ بر متحدان واشنگتن در منطقه را یکی از دلایل تمایل این کشورها به توقف جنگ آمریکا علیه ایران عنوان کرده‌اند.
🔹
طبق این گزارش، در همین حال، ارتش آمریکا با پرسش‌های جدی درباره توانایی خود برای دفاع از نیروهایش روبه‌روست؛ زیرا ذخایر موشک‌های رهگیر سامانه‌های پاتریوت و تاد به‌طور فزاینده‌ای رو به کاهش است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/454002" target="_blank">📅 11:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454001">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYSC4nSUZh3AiP_da1nVAe3aHCEFuEeAukI3mpAtXC5K_jo1zG8ltr-2MGuKzrMc8C0NyTqHchVEhLjBJVjmXaOd9ADqBizRNP9tnTNmDcUkBWUAweamRTORxliYpvD-FbS7HXwUlk37aNAT9njF-ux11yrAtPOKS7oZmKwh0zRHityhQpWh7WmdO6cJ3nEoURi5pctdiGIXeVA7kjJfaQWSIWxfHUbH6yIBwFKNvEEpivCvGizncsr9g3UNEHwKkftReiB_XNBClGWtgZUY-SONoSHjh72bDJx5xgKecHixS94lMVm5_LoZ3iBeQDS9SFpr3VitVzFWjBQO9zi1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سرپرست وزارت دفاع: نه غافل‌گیر می‌شویم نه منفعل
🔹
تهدید را مبنای افزایش آمادگی، تقویت بازدارندگی و ارتقای قدرت خود قرار می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454001" target="_blank">📅 11:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454000">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان یزد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c7996d5a.mp4?token=HwdXVsQr0EqrpfBkzEP_YxIQWHGL7VBfVzDwqrWXWL09RPwBlhBFPzOYxb-WDa4whQj3z-BL10TpTpnw3kpyD42qnMBkMzrm-qrwXXv4kTz7qLJb89XOVvqnzzTiKyNynGBjF88TmjwYwZV0IEVGnQYBkxpkeKir-w87fdUGEcjDFchFe-VWL67LRyes_JWGFUGHMhd98Twacn1oc3gKMmT2cpYifkiYpKBJ77BhZ6fBncTvx1LvRiH049za8gAQcbeJJCyIPrVR1tcSIqReLb0x8fzvQWbM-wqdlbQywDCXqXS6xx6Gw5gdJ2GwMTbEk16MFoIR0cDtCyHTVCJGbntD7Zn6XdpfoZ0Eed3ayA5N3a1ssyHsE7whpksdoJttP1oF_6XibR8R9mYkk6gZG3WgAt0grqk7UDgsNMcBEUVSh_JVyoiBzr3sL5YjUY2yI9EAggyoO30OD68RznAbSsowvvwzHcEVmpZtIC5XUqQOpxa-bgVFwz1pa6wniNxeUrnFIJtpufJBIbDMDLjHlAokKyuJzLnxlUJgkc1BItxWmNHtdRMPw_Fs1Wt6WjlCr9EBfDjTJMvmL6MU87WkeriMtwIRAreHM49-WJXjGVuJ_R83OxsSZtNDvfd0oOtblSMGf25hG5alDSg9bUTzZthGzTepKXbjC2gJnAmKe60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c7996d5a.mp4?token=HwdXVsQr0EqrpfBkzEP_YxIQWHGL7VBfVzDwqrWXWL09RPwBlhBFPzOYxb-WDa4whQj3z-BL10TpTpnw3kpyD42qnMBkMzrm-qrwXXv4kTz7qLJb89XOVvqnzzTiKyNynGBjF88TmjwYwZV0IEVGnQYBkxpkeKir-w87fdUGEcjDFchFe-VWL67LRyes_JWGFUGHMhd98Twacn1oc3gKMmT2cpYifkiYpKBJ77BhZ6fBncTvx1LvRiH049za8gAQcbeJJCyIPrVR1tcSIqReLb0x8fzvQWbM-wqdlbQywDCXqXS6xx6Gw5gdJ2GwMTbEk16MFoIR0cDtCyHTVCJGbntD7Zn6XdpfoZ0Eed3ayA5N3a1ssyHsE7whpksdoJttP1oF_6XibR8R9mYkk6gZG3WgAt0grqk7UDgsNMcBEUVSh_JVyoiBzr3sL5YjUY2yI9EAggyoO30OD68RznAbSsowvvwzHcEVmpZtIC5XUqQOpxa-bgVFwz1pa6wniNxeUrnFIJtpufJBIbDMDLjHlAokKyuJzLnxlUJgkc1BItxWmNHtdRMPw_Fs1Wt6WjlCr9EBfDjTJMvmL6MU87WkeriMtwIRAreHM49-WJXjGVuJ_R83OxsSZtNDvfd0oOtblSMGf25hG5alDSg9bUTzZthGzTepKXbjC2gJnAmKe60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضرب‌الاجل دادستان یزد به ۲۰۸ فعال اقتصادی برای ایفای تعهدات ارزی
@YazdFars
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454000" target="_blank">📅 11:14 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
