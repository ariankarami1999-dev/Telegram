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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 148K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 13:21:19</div>
<hr>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT066vbXZVvUEEXkVWveOlNR1CjcIztnenLL73Jx_5aqK9L1rwJNA1QcvH6n-l5hugcFT1gwlAwM1I3pb_6RxXJaKr1IVErss292kWz2MBzw74qPDH3k2M7srEgKixJxCsiKQGbVkp65zkJQJUChV6Ri62ULHgC3oRoFJxPro0v2XCGp8ljK0hSCVRk04HUVmM_xiVPLaELvWEO7AD1wO5MQ6K50ER3wEuuUL6I9DzygDTR8AK6ZPhgQ0vQN__E51A7jn8pqF6BC11cZGpAeRhSBDKUbgAtq0hmtLHUEr9bM9TKGo449D0cQuXa0oYuWa8xxHoMQWLP2nB7eCi055Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSh0BmAI8gCgZd5aEPST_cvNOcTmi6Za82EDj4YQqcn1easmc7RPhbnzmSFe_ZeRnCOpBhQm27OPP7JXKFckTHBOsAk5i_jj31LvWhBVcnm_DiN52fFbDlXcn0f0GLgRYcMeiYpq9JeVHdiNMyzv4rjbTz2FDXo_afAIQ3o6aEDJN5QdnddwnJMJExQlSag8udZsA3avOYFM7m9fdl0dyPpZB5yQwpRTE8MHWzOzpu3KNj-acpX3jfidwTs7yXyemTEeWbOc_cc7XwBKVh7MiVUqthZ_Mfnltzpb2sSKpxNQPkrViDlcee9alSlq_uOPT5JtIARiMa2lMPDnmB9_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVtzW55e80MJU6g597T2KK9tlunHTwblk63T5apfv7ZqDWetPxQi-P7z_xqSyrpTkKS1hx1VJOKuCY1mA8rbKVLohC05b2Yvo6kIVpxIfoLwIYd8nIz4bu0pTabrzx435_zc3aN3DlX9VLVEENn1qJKFT89zHZQx8GYtwUkEfySEXuzKGatxvFY6D0Z8mqEBbgTfb3_cONWBnVI3NKi7sY5C-IOSo2bNL-qQ0ZwGMITtWwVBKCQyGWjgxnhnyFz8pXrIK7v4ZlD1IEC_aimAQeT6ds6McV6hFi17p03Z-1NBVXiiBgPxNcTiB9VKxQSzuof3CerRDVgPYV-td1G7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=IsPa7mK0UmoKsJgKHL33hffz3I18yhs2sF2Vhdi86qHca8w_o55L60TTTid32WGqNhA4-E267LfhHTNstS8d57xpFAhRKEgrcHltdvt3GqoEU2nb7TwhPRGPsIjPOBV3RjFVuVGVfAMAB4bFJ9lVAVhxT9BMAuRBdKL2b2_r78IDfBQ8Q44L6ImIAzZJ8rbKmSNWlRuqbyMKJ80-2PlvUM0DBlmjUtm4zieLRBQt6S0is_4rKs6zBrXCN_65pWOJiD1iWH8GQSO26CsE3Bx3TnUrz2kTvCGDdO9HMVRSk39ev83-hJi0JK1HtwKt_xbU-5jNey-AJHqbjq99yfFZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=IsPa7mK0UmoKsJgKHL33hffz3I18yhs2sF2Vhdi86qHca8w_o55L60TTTid32WGqNhA4-E267LfhHTNstS8d57xpFAhRKEgrcHltdvt3GqoEU2nb7TwhPRGPsIjPOBV3RjFVuVGVfAMAB4bFJ9lVAVhxT9BMAuRBdKL2b2_r78IDfBQ8Q44L6ImIAzZJ8rbKmSNWlRuqbyMKJ80-2PlvUM0DBlmjUtm4zieLRBQt6S0is_4rKs6zBrXCN_65pWOJiD1iWH8GQSO26CsE3Bx3TnUrz2kTvCGDdO9HMVRSk39ev83-hJi0JK1HtwKt_xbU-5jNey-AJHqbjq99yfFZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5wU6govHqEx4R9-z9yC3h5QCa1pyQ8Dxx5klceZqBTOoN7RwN9WicRbaccZySYqlRH8vt7ttF0u0a7DdWbVcS2sPbKJv3FXnpdURuprtJGWSiGmK3L0CiSd27PaDx3Wb8EeMC89neZPQfdpZG_OKh8cQMrd00rZPcf_VrkJkF4OH6FaDusyzZzkGlTwpOYAV-o8WWrjIUdwvbLm2ItML5SftAIT1Ruzp28ObeVWA1M9mzyBFr3SLqa49Fy9zG3XwzRHuUltd3abLgEYGCe4e29Vr2UCtcPlgRPM3504JRO7b0V_iX2RGHiXdCvzHqAdqmdcrXXG-55qWGrwiinWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=DWGQqvPRY8l4HAY1xmKFQXdxpBKrwnWdX03zvjY8IbxIQaAZHsUP94Ei6xMVRT2PF7gtOdWs_u8keJnMqOSMxwu01cg7roOQEBde4dVJYw-vRtnw_FWGJdZzg26XFlyNVfQgT_VAIv9GE7CwFfnJgY378ia5vPvK8w1is3tgoGq9wvN7LpAXKMxC4k6A6XTWvdRCouaeD4f-c0zNPFGJeKSs4Ox-2ateUmT1tFNNqdBkQIh2mdHyZoj-lfv-dlpQeCyhpTsHm864zWHvUUfM7p8lGapUGWL2gcjJ3dkyiGBjYly65EFxix1A0u6qJY7zZqdoHy3S7kcntB39rtcsWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=DWGQqvPRY8l4HAY1xmKFQXdxpBKrwnWdX03zvjY8IbxIQaAZHsUP94Ei6xMVRT2PF7gtOdWs_u8keJnMqOSMxwu01cg7roOQEBde4dVJYw-vRtnw_FWGJdZzg26XFlyNVfQgT_VAIv9GE7CwFfnJgY378ia5vPvK8w1is3tgoGq9wvN7LpAXKMxC4k6A6XTWvdRCouaeD4f-c0zNPFGJeKSs4Ox-2ateUmT1tFNNqdBkQIh2mdHyZoj-lfv-dlpQeCyhpTsHm864zWHvUUfM7p8lGapUGWL2gcjJ3dkyiGBjYly65EFxix1A0u6qJY7zZqdoHy3S7kcntB39rtcsWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=R5UYwch4VIC1YoaGXjWulgJSCRQz-ZG2QzE30W9VZzHyOGwIZAwNmA3OasBwzT9QP1aH41mWiMJ3ZheLlHIpN7qfK6bambDq3E2wKplMuaBv9sTVpGk4GTIiRAIQRUER8_EOatxKMofha6ADtxZGkkmJU2yUz4FW43K7rrcO2qvN9gAzJLs9ON6g6_rZktovwtmfEBDOxcs4l377-mnmQAeF8BEVliGpuQvm4zRpHkeTvjSHjdl-_3LunyUIZg1vRYnzYQgyEiCRpdYc8XQ0KXBlC6SioFE2iqQaXcTb8rZVc1TJ4r7R16FIScgGsvjL2_CckT2NSMK7icGiu7VTtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=R5UYwch4VIC1YoaGXjWulgJSCRQz-ZG2QzE30W9VZzHyOGwIZAwNmA3OasBwzT9QP1aH41mWiMJ3ZheLlHIpN7qfK6bambDq3E2wKplMuaBv9sTVpGk4GTIiRAIQRUER8_EOatxKMofha6ADtxZGkkmJU2yUz4FW43K7rrcO2qvN9gAzJLs9ON6g6_rZktovwtmfEBDOxcs4l377-mnmQAeF8BEVliGpuQvm4zRpHkeTvjSHjdl-_3LunyUIZg1vRYnzYQgyEiCRpdYc8XQ0KXBlC6SioFE2iqQaXcTb8rZVc1TJ4r7R16FIScgGsvjL2_CckT2NSMK7icGiu7VTtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=RWSXWdpbCQ17VWkIB399kRz-Xkpo53o48VkK8NQ2TgOwPULTGy6C9xoWJSLFaaUMvbNk6R6t5gf3zS-Vr-FqELosOIoeTskoRsWw4Mpsh47_mcMJYLG6mLanJVfWL2IQ0-brZTVW4k3aN5pKS91iYB3IRdgeEFGT6kFQfec4GaJspZTsTe9XbCBUCM-iUL67SXgA_iQgIb5Btj1g6vymyrmz5pJhGLj1bItgJW0U8pA9JsO44ZShq3K8ANTrDN-oFIPFBJjxSA9Dx2pBLXQE3NLDbEuAfA5FB31SHjK26MhQs_-cmogDdYB1KYy0s4tmwDXlToawAJ144LMcSCOmLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=RWSXWdpbCQ17VWkIB399kRz-Xkpo53o48VkK8NQ2TgOwPULTGy6C9xoWJSLFaaUMvbNk6R6t5gf3zS-Vr-FqELosOIoeTskoRsWw4Mpsh47_mcMJYLG6mLanJVfWL2IQ0-brZTVW4k3aN5pKS91iYB3IRdgeEFGT6kFQfec4GaJspZTsTe9XbCBUCM-iUL67SXgA_iQgIb5Btj1g6vymyrmz5pJhGLj1bItgJW0U8pA9JsO44ZShq3K8ANTrDN-oFIPFBJjxSA9Dx2pBLXQE3NLDbEuAfA5FB31SHjK26MhQs_-cmogDdYB1KYy0s4tmwDXlToawAJ144LMcSCOmLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=Ue9q2k_WzomrO-eD1r5O22NEf1LMUGv1hOobaLMj7g8pJN51nfjAel_Vsp4R-BCkuNKiPJze3FvTDa_cKUHjI6fdSM8pqL6Vo5pEiZxOnM1qPtvf6nq-7_tkIw2oAEG4EnCEZdxN-X1vsYZV5oi_DiHSutMaVFPGhDLBYeChyx3kpNkGEwgaaXMAcr24-uEX5ngZGi6TpAPO2jFINBlyiqq4Qa6qCdektWmw9f_RWq704d1S5tw4JNyC-r5NwOqtL9o3_MBiIp9sqgXLHcebm_3buaxJvTa4AAxbT12rf5DX0p1k2NCdfydXYoP4mTv5ernLCa9busHrJVDVlsNtcF_5nW7_835qhtRV3WByZp2eSciX2NW9R3IPU-4w21w47qKYmI9W53xdiZj9b4yE7oj3O6OjYYHF5bHjsdiVfON1z6Y_etRNX6PibSb2eGiGdv6HuFaPjZ8_CitJwL7ieGgQNjtVs8C9D9zxVhy7Y8enKOyuoN6mRu9xwUumCY02zzL8eaPGaLuLkWWRj25Q7JlaX_ZS2JNVyu5QYBY_BXfmJXW4A4sqsYF9OHbrxcBjk-rbgZTQ4IJX_yeqHo49qOulRXCVGs4PkpEU9hEADNdhiVabCj7ce_O35iDOZU6m3naTt6_UKR3zbR5YG9P3dervmq73MIdy3o-OADRP2W4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=Ue9q2k_WzomrO-eD1r5O22NEf1LMUGv1hOobaLMj7g8pJN51nfjAel_Vsp4R-BCkuNKiPJze3FvTDa_cKUHjI6fdSM8pqL6Vo5pEiZxOnM1qPtvf6nq-7_tkIw2oAEG4EnCEZdxN-X1vsYZV5oi_DiHSutMaVFPGhDLBYeChyx3kpNkGEwgaaXMAcr24-uEX5ngZGi6TpAPO2jFINBlyiqq4Qa6qCdektWmw9f_RWq704d1S5tw4JNyC-r5NwOqtL9o3_MBiIp9sqgXLHcebm_3buaxJvTa4AAxbT12rf5DX0p1k2NCdfydXYoP4mTv5ernLCa9busHrJVDVlsNtcF_5nW7_835qhtRV3WByZp2eSciX2NW9R3IPU-4w21w47qKYmI9W53xdiZj9b4yE7oj3O6OjYYHF5bHjsdiVfON1z6Y_etRNX6PibSb2eGiGdv6HuFaPjZ8_CitJwL7ieGgQNjtVs8C9D9zxVhy7Y8enKOyuoN6mRu9xwUumCY02zzL8eaPGaLuLkWWRj25Q7JlaX_ZS2JNVyu5QYBY_BXfmJXW4A4sqsYF9OHbrxcBjk-rbgZTQ4IJX_yeqHo49qOulRXCVGs4PkpEU9hEADNdhiVabCj7ce_O35iDOZU6m3naTt6_UKR3zbR5YG9P3dervmq73MIdy3o-OADRP2W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCNmMo2NAFs11gxNjSuZqPGyTJaTQGWO_Zap180JPzO6NxJXFTKJtlT0seyvuxeRB5VHleo8pL109xEwwOu21Ql401qoRYPPhOyj_Xu7QT18S0-72kYcqFWt9PAyXz26wNq5aooRtrzJpTxbiMxZcUwDrgHawnieusAYjxIc2n_Gqf7ilmtTQNV85RSQMrYOOAN3hTfU_fxNc9L8QptwQT4tsdYlkXWKBOhYNNI3GyLpKKmJL6DOyRWDOI74561moVKvCN7JIpzBFomF8VY7KhSDGGWVjNe6uTbT_mrImZ8PwfC-PIneS9OLHaONo8Yd_umih9fTv4uT_ZiPZoezEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=paf-KsEEsOfGK0NTuXTgy2bnEQ2wHWfct0bFXam05nBXBNDDI3Jnd3ZYQuL0jSWziWms2lTYlQKHUgtxf0pxBi_MfmwZ4eWvBLnmt4whJEFnF0BexHdApJWFYDAtU2pq1sGM1KubvGbbqCY06vGBsspWRB7-IQy1fSTMwYPCuaR92x30VVjD7u_VrCAFIJHln5JPTY0e3_52V89yuAwVfH6Xa88c6VsIiQXV_S-xZqJS08oXMzfgbEbN0Nq_VzaL0vyR3gBUU_YGVwOPGcN5d4wE-G5M990aLQIF1o1xg-1OLrb-xrNcICsC2kGM1R_wJO0v7fZmoa-J4u1i5hw5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=paf-KsEEsOfGK0NTuXTgy2bnEQ2wHWfct0bFXam05nBXBNDDI3Jnd3ZYQuL0jSWziWms2lTYlQKHUgtxf0pxBi_MfmwZ4eWvBLnmt4whJEFnF0BexHdApJWFYDAtU2pq1sGM1KubvGbbqCY06vGBsspWRB7-IQy1fSTMwYPCuaR92x30VVjD7u_VrCAFIJHln5JPTY0e3_52V89yuAwVfH6Xa88c6VsIiQXV_S-xZqJS08oXMzfgbEbN0Nq_VzaL0vyR3gBUU_YGVwOPGcN5d4wE-G5M990aLQIF1o1xg-1OLrb-xrNcICsC2kGM1R_wJO0v7fZmoa-J4u1i5hw5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByKFsJ6Q-fA7hXFjU7Pl1pYC76xlG-Gx6DrkMt0Jbh-agmNetaK29RUqZ74I1nt0IDgNPRpcVnR5o__3kq5YS2TBjevLyexPDTqQhDxjargNIwZEqlbg2zRxdCf4EWaC5OMoYDoIBhxyJed2SC9cTZmETJCmJVtFy8ofRN9Oo9aCglsEgNkdGhA7NCjQzh8X17cebgv-lsJzYHkferD1NVt8u6MIta2h9c7WUxVTaIfPeoJFsnODd7MbL708Hd-TCEzFGOQ4aIHvHdHgZtV2sSS8gml57SrtWXFza4bszGlt2DdlGj9oKAEKEXoW-L1JS0g1z2A9BCokKqYyYBxcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX2wkNnsNTY_AYHFV-s0LnJo6VUmsv94s0i_YZ0UY8pV2_yoSts6uorHHh6GA9yIryhOCdOhVP4h032io6MwB0FdvqgxgdimwTPrZJ2szTLy-QHr-e0_-OMk_L0bCc_j377gokwkhkWezX8mBFsXtgQvODpVQilNu_7pLlg9E9RrZQBYrOTgUYUXXChtXjkWbyc-o6mLQejMSFq2O2nrm3yWtOIuuUJPvMWTtscYDMLjBIMxxP5-7hz7M4_3VEP1mCjxllov5AblNmgm9U1jmcp7hhhewAgRCCvXo9cdl6onG-Bt7hdpN6WqvOuE0e6Ms5vnQmLRpmMvYpLCcSK6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJKxgxibXg70LARwbarUj0dDgiAs7rwg-F9J2h5bkV4-lXItYYiQdnR__VdCvcP1Y0jtOz4dZfIsOQgVdFCqmJ09V5yuKc2AzdF8DrSTvtHDIZzG7YwKczNrMwTxRrqWNDy6EWlb7sYe3MXnvbaHDQC2oiUBXDlkG5FQLstAaNo__4oG4t4Sly4dS761OXzYDTrbDe6zveJiZcRBnfsjwz1fy53f8vWsrbCFgIlVTyJBMAhKwR0iFJnvgUdKaG64E1KqMgqvDBHhNdBIUfGI0Bs_SLGeptouY3M7i4XMPhOdP4bHl3LBD3julC8pS2GLHmXCwuFUo8UOvyj-jeKQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBvPdB1WKReOtidITfRMYxY0rRSbhXauVLKTrmTjKlY3sLSjqHzeeF3Hnjg1t7W5wEqXAsDyDpezPDkmnIow4StuJLBhd1hBFdf5rkfy7CwRsephZnEGkduNWGXx4UDtnMd1vGHQhqJIzfKxcYjnM9Nb0ewoMl6G4IsgVO2Qo0uO6oGtGIs6e79y_F9OaicnNMLpF6w4ESRoOF3geSVi-_R05y3DX_UX8Cn2ufFGNLE7pJEArnKzsfRKM7lhXpsD8tIj-IJsOHR3NIAe2AxuSFE4GY_PAhASNhUme_Dzcz4lvBe3gwo6GjNXMI5Mb3npGOFtbayGSfGRX2LTFUFBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHCO1Yw4pf2TfM_c93Of5akgJu3KJfxMW7Au7mBnZiyD775DszbCl6Dj8HOfeB_D8_c2N3QlKgwxScW_O0lbvF-zA86UfZPHUdWJc9eETXOteC7_RDEdv1BtSsecvBLMoVWMgzsG9EQNdxdd4x1kiil9rNrDvD4au2biOWkQ1M-KDDcRBfYoal0CWoXRhgfugLySPDu3gSB7N3C0WzF6nVfwLzHQiaoEZnFd2HjMhiUB8VUdoVAEJGs6LlZzSfHbu0VVEACI9kHqxOB8LQwwYx9mzkVhAMXZlOftyx_4pVpl7gdLcpWh6FJiROfsWJs6pB2xAe-yv5cJDrzoeN3DCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_JjH320_nGjKAwLVV5b3dNKn5m8Cnn2gugCPjVReXqjf_aYsJ_BBiFWB5fepGa9TlMv5cegzNC-bsoMNQDWRHgSsj5j8Ovgq16jgHmloYM0oD82LhwLnBT9KWLBww9AUeRBlUvQWknp0SXr8Onp0bEfcTXhMnuOdNGctpWEwc5rVyfp_bFNOWa8n2ryx77aTqck6P9GCqTp_CYyLH3MeCGxjeKnUUI4_5cAYWhIURNc4oTvNgZTV-YLmSGJGFEcW-VJOVCFK_X4mI4bOuFgqUqwUCfB9UFTRoL-IJAEJzdNi-g2yqThdFY6vC4npx70ME_tyDnoGFmWk7pJsoWXmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=Ps4tU-gy9A4yPA7QPqH_YByd8fOzJ07LI0v9WU_XhZVNcrC-IcyVIgEPPve1vWMO7GUa24yRDcbLg87xZzheo3RgJBmLoepDsFYpx403DuvdTioGd7j2ediAik6WTUKstFqRhXaM8RxQYgBQA3HbQAR0x4S7JUpDSQa0ON6tWqtsaFmNs_0Z7cVOZnbI36whhK_gKJ_Tv2zS6mcOTle58PQn-EiNYXNvKc8htRHXR0xFCXnw07CF4I2qVdFg_Kzv_X8UaOX3aVZ4PQTnxJj9qwMsU7N21D--QvzJLHh5RPFCLmfQLjX174OaPdnzVa7EBiBQdMpE0z1T_FP8QdnzwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=Ps4tU-gy9A4yPA7QPqH_YByd8fOzJ07LI0v9WU_XhZVNcrC-IcyVIgEPPve1vWMO7GUa24yRDcbLg87xZzheo3RgJBmLoepDsFYpx403DuvdTioGd7j2ediAik6WTUKstFqRhXaM8RxQYgBQA3HbQAR0x4S7JUpDSQa0ON6tWqtsaFmNs_0Z7cVOZnbI36whhK_gKJ_Tv2zS6mcOTle58PQn-EiNYXNvKc8htRHXR0xFCXnw07CF4I2qVdFg_Kzv_X8UaOX3aVZ4PQTnxJj9qwMsU7N21D--QvzJLHh5RPFCLmfQLjX174OaPdnzVa7EBiBQdMpE0z1T_FP8QdnzwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=RZcWQxRmm30lzvHLgig93AY_pkpOwFUgcciwQWCbKbcFJTDeo-jwj_3sggMorGZ_45zvFI2056cXqU30SyojQxgvdoIzPFhoJat_kPMV9YHkLn7Sd3Jkyod3GdbhXfd-cJZCEpuejwhRgqS9qvoypDAUylqk0FxVp6W8KoI1DJ2J2MZ4f7MfXfgUBUmtW9iIk8CnMbriHgxt9bAsOFB8lCYFNbN9HzhjBNaQAnNXk4K2nNa3mAm0ToYH3uaUHReY_j3qCBV4TsMwMfnISwBJsAL_xWr19Ap-7aMiSA-dYyCCjqv0yKUig49huGOr9qw10txe7_YLE-oFK54AQ5YwZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=RZcWQxRmm30lzvHLgig93AY_pkpOwFUgcciwQWCbKbcFJTDeo-jwj_3sggMorGZ_45zvFI2056cXqU30SyojQxgvdoIzPFhoJat_kPMV9YHkLn7Sd3Jkyod3GdbhXfd-cJZCEpuejwhRgqS9qvoypDAUylqk0FxVp6W8KoI1DJ2J2MZ4f7MfXfgUBUmtW9iIk8CnMbriHgxt9bAsOFB8lCYFNbN9HzhjBNaQAnNXk4K2nNa3mAm0ToYH3uaUHReY_j3qCBV4TsMwMfnISwBJsAL_xWr19Ap-7aMiSA-dYyCCjqv0yKUig49huGOr9qw10txe7_YLE-oFK54AQ5YwZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=KlyNJpWaKKy_izh3LSDgidS6kyohBOqulRGvkwjAdbOowv8HSEWdGjOd-wrH0KzAkn0t-745TJsGXlt6igWJphKAoQin3YW0Ps5y7w6GuyT-n3xo-d9nmJeKe1LBwMNWB2etzwn6j0JGKwa1-_qUJeSPPOuDAPQwAvNM0iE2jAL3F4szDHtX84Rxys6hKWGHGyeOOU5eRStLy8FlWFbmxzhHQjci9oqLfDMgTPj8bwETk4G-dygPv1gMkc8pV7spLvRd9Sz-meIKRUNtYgEdLua2FCmt408lnGtPy1-_Zc8k8j7c607etHzHh2Xj-i6zOGnHY5GZVkCo1ro2cRckJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=KlyNJpWaKKy_izh3LSDgidS6kyohBOqulRGvkwjAdbOowv8HSEWdGjOd-wrH0KzAkn0t-745TJsGXlt6igWJphKAoQin3YW0Ps5y7w6GuyT-n3xo-d9nmJeKe1LBwMNWB2etzwn6j0JGKwa1-_qUJeSPPOuDAPQwAvNM0iE2jAL3F4szDHtX84Rxys6hKWGHGyeOOU5eRStLy8FlWFbmxzhHQjci9oqLfDMgTPj8bwETk4G-dygPv1gMkc8pV7spLvRd9Sz-meIKRUNtYgEdLua2FCmt408lnGtPy1-_Zc8k8j7c607etHzHh2Xj-i6zOGnHY5GZVkCo1ro2cRckJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=GqUzn15217g5iK3cUu_NEDYp_xUCrQi_96FAGNpy_OXioIGWmr6-uIoL7Cdee6Gp6nEMz2_cHRLoxNyBd4ETD3bGcXWSxmtjD3uhy6X2tvrRd_S3A804wF5roYvJyNxWk9TTkGMDzy43EqURXoZOyUcrWl3NqroIhVdhb1M-jy2a_xvTeoGaHjDyL3AMISm4IryReSeT-YSOBM04SHGgsoluQNRvgHnHBsJwtE3M1aCpnSCI0zWaPudPBGefq0WngWCWd8SIHZcYQMOk8GOlYcvs2uK8c0_o7fqRzdFcteNjTdQSqInFjLMqGfArFkcIq4iwohgzaMcoYhRmzRgxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=GqUzn15217g5iK3cUu_NEDYp_xUCrQi_96FAGNpy_OXioIGWmr6-uIoL7Cdee6Gp6nEMz2_cHRLoxNyBd4ETD3bGcXWSxmtjD3uhy6X2tvrRd_S3A804wF5roYvJyNxWk9TTkGMDzy43EqURXoZOyUcrWl3NqroIhVdhb1M-jy2a_xvTeoGaHjDyL3AMISm4IryReSeT-YSOBM04SHGgsoluQNRvgHnHBsJwtE3M1aCpnSCI0zWaPudPBGefq0WngWCWd8SIHZcYQMOk8GOlYcvs2uK8c0_o7fqRzdFcteNjTdQSqInFjLMqGfArFkcIq4iwohgzaMcoYhRmzRgxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=mjDMbZYZdK4r9J4c8-GjlH3TijcFTTa4TcQdTTRZZ6-rk9N1GgxVNXpqqWK5BP6-OGMdXJ7_e5FtCrDRKvwCr9t-UnpgC7Wjow-Dw24imnmSne1DDKS8_NS0d0JzXvpal_CNbhipyeRytqNGPlG4JOzaF_CchJPowW1f1b1KwI7-JqwKqCnAWyT5Eg-yUEWjjACs9_xVye5l3oi8vUo_00onixoxNOojo_kjhPLz8HVsrlO4q7jvlRa9qWaTVsshd5WzIQdUp5ko4182S1-GnyBFEPV0IHbhGWwOmmbr6UyER8zIj1kE0rYNVDMktV6glAb5t0KQwt3jGf8Gg0wvlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=mjDMbZYZdK4r9J4c8-GjlH3TijcFTTa4TcQdTTRZZ6-rk9N1GgxVNXpqqWK5BP6-OGMdXJ7_e5FtCrDRKvwCr9t-UnpgC7Wjow-Dw24imnmSne1DDKS8_NS0d0JzXvpal_CNbhipyeRytqNGPlG4JOzaF_CchJPowW1f1b1KwI7-JqwKqCnAWyT5Eg-yUEWjjACs9_xVye5l3oi8vUo_00onixoxNOojo_kjhPLz8HVsrlO4q7jvlRa9qWaTVsshd5WzIQdUp5ko4182S1-GnyBFEPV0IHbhGWwOmmbr6UyER8zIj1kE0rYNVDMktV6glAb5t0KQwt3jGf8Gg0wvlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=h9PxuaDjW2mrZGf1rLc4znpRQbpEGDMMiIpmz0yxvI7S4aEnHKyNciRX6AgmT4uFCOJEDFtKuFOaiIpq8cr4DjbOHzhDhrGy-4Rast7xoWxuAF3ICPspDPhut-GfyzngcRvO1nIZ0rsLOnIw_nIarRyCH4qEz3_bkAaBr90UpZ2xg_qd5CDpHdAXYwPUgErbhdEOypKlgf5KpzuQG0xqDx95HxOWT4VK9EQV1foF-2abjItdB3IoGOHlpGo1na7ASBHn0x1APQrHxYQnESgWTYsqO0vof3TR8JGuDIarnMCbF1vICOCTSFuwX4_zMX-9igdsr_CRsYT923A4eIJyUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=h9PxuaDjW2mrZGf1rLc4znpRQbpEGDMMiIpmz0yxvI7S4aEnHKyNciRX6AgmT4uFCOJEDFtKuFOaiIpq8cr4DjbOHzhDhrGy-4Rast7xoWxuAF3ICPspDPhut-GfyzngcRvO1nIZ0rsLOnIw_nIarRyCH4qEz3_bkAaBr90UpZ2xg_qd5CDpHdAXYwPUgErbhdEOypKlgf5KpzuQG0xqDx95HxOWT4VK9EQV1foF-2abjItdB3IoGOHlpGo1na7ASBHn0x1APQrHxYQnESgWTYsqO0vof3TR8JGuDIarnMCbF1vICOCTSFuwX4_zMX-9igdsr_CRsYT923A4eIJyUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyLQV1jxwKZ7Im7fEY6FDbn_CtX2eV_dF_nCtNe8U9rBei6KSVdI_-TafBtEQK1X5j2JKSh21q9bNAG6Kdn4hQW6JSHj15NmTFpPX6MOHLPLHPlINTk-Ce2jGUfSvPi0vhS4JODcQjUYK1smR1DnqrUSUC4zEZfwfI4mtAMFYmqFKoeZnrjfS9PpC89igY3AdaOr069N5F6mKiOiHX18-cALu0P4xxAR13Cbknl1V7WCiPY4JiCu90xIhAxaKqVz3-ZhK7HWwSrv58w5x9p3f5LXw83L6cwHu4rGf8GQE1HvcOnksiChO2drOtSh3ZOrf43qi69gQKB-N68SJ0Higg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4yDeJgxBCC97CibQzERQcN3xtEkIPX_tWdw49L3yK9Mozl18OYu3_HnP3id1iSqmSZ5Oeuid6k8htsXVcNvwSh-Bz7NjbYaS_VrFQjIgzT3gp7e5KRz8Dm0MGloQ73sm1IImKALAzsnmeJig7427N5e3YEiltXYx5Dj2IeAqE6-cKBJ5EgkPIfmdLBrby58lTLAHYadOqu0N1kYmKZrLPSvqxb9YkOJampAPYR3kPJ03dPnJgypUq6H_CyISjrOZEMk5SBUwzL7dX9Pc1vYkBfp-nV4ji3gTw5d7gNbLbW7q3jRyZWDBvBkHHxYrUApp7-pDylEZhc_GwqkBdBJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pin5TSfaSgmfF09b9TM35yQDDCfv9RwoUlFKQFm_HeZuRhfhJzKp-ietL88lSB90fuojlgW1zqzdAJ66-jWSczVCtStcjS1LzKty1srcd54v-otIHpMi13vhvtslgVtHusfLUpzAL274u98OKOJdNF7CPtOfuLyllZcHFu1Y1Y_cN_Qcoy_EMWern-HhA1v3QpdZ8XF6DAsMKqfyyHQLoLuH007K8SzCLzbp2c5IyCTN_uvaBusna2hHx1_-t5j7ayhfsC7ZqwwJVARjYxciY_7j7L7H19rNDhHSTBQjZ5zWr3bxX2iVkXHfs8yg6SNGl9mGehgiXI1m-0vLA0j4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=r7MYpnNCdckMtC1u9XG2_Up_WY-qyYPWjtUMgkKgYe89H3QCl834qoexs3deYzfMrQFhKkRz0xa_3QMqh4DliWG1Abp-pDYOTqZMUMaXthL0aaFWXCzDGJqtLxqcehK2eVzOYnMN-JqnFQZoJsmptnnAf5g-C8jrFnHM5e6589yAeGnM4GpwhT_09GqeDd5tERFe0OwmV61fObUp8w3_H-pAitg61YGPjRxX39xl8SYC0nKegPGpMc7rbUOM8ccZJplOxlowFaypkPzK9aqHekdG6siuLCcTaTq-lr6fQEgN17TWEMS9JAEzI7DakyHUomqrtjfxO5_O8vXXRj-82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=r7MYpnNCdckMtC1u9XG2_Up_WY-qyYPWjtUMgkKgYe89H3QCl834qoexs3deYzfMrQFhKkRz0xa_3QMqh4DliWG1Abp-pDYOTqZMUMaXthL0aaFWXCzDGJqtLxqcehK2eVzOYnMN-JqnFQZoJsmptnnAf5g-C8jrFnHM5e6589yAeGnM4GpwhT_09GqeDd5tERFe0OwmV61fObUp8w3_H-pAitg61YGPjRxX39xl8SYC0nKegPGpMc7rbUOM8ccZJplOxlowFaypkPzK9aqHekdG6siuLCcTaTq-lr6fQEgN17TWEMS9JAEzI7DakyHUomqrtjfxO5_O8vXXRj-82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKeaBpvTT7iT0Wr8QJD_kJD3DMRuoFC9CH6ZnttEGlxQlGuBCgx7-4qSv7VlheGbrT9fAxkgmrCmlmoPTIzVeF8yKY5ZAKCELEYU1Ewn6urs_C8kPw8Qbhhm_mFtEaaQuTLnCS-9pxJniVLWdySBP4Gn1YC1HZYlAUFoK9KepuDOsXCfuOac4uZJaLvyU-bRqZuoWENB37aBl4IhnEWXIe9i2HQagqxu0FAkJnUyy1lm7O1a9lMR6bAAgNjo9eMRfovTFl8HYCHwtaDfX7iWGPjAjJCZ9c-GkZbkBwT_fJm4jSy0IA0kweRcsfNZyZNqd4h-lmZ5u-7EKwLpEbTvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8Y1JNKJP7gE2lnMQ3_ZeJdXmaDEYQxXEh2plc1gdspC8s-O-LOFFbM91jprfe1utEgywfZKombDZ_ADxeSIHMfqFQbqbXYuX0GRZgQRxvk4Vjf5S0epB3E2kMQGA9Y_aql1mmKag3JRt2G4NTQcdhl1nGv6LdmyjkxUOguNtTMq0wmDwrjnZmhhsteC0Di9hoofD3xzqzO-zMKG3lrnHGLY2uTtpahbKj1g5fDpi5qDQoimcgcCXrj_O_hoCYN1VFzn1DRcdVE3Rb06KACiZ0NOF4jd-hyEVRzPC7CtOpbbjS0WMjkGMmgEx_CmltF_jWn9RHIQkp_A17CdE6mEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=RznlhWzCcBHxBo354A_UjTlpD1g3tzJREZrIdgrDRNhpIDBAqs_dJHcni3hZHcXOEupQRkm-_2S76wud-28Kqh-iN5SQnzUUXgplzHY6zmUgdpHdInT9qssZOX9hXPC7zlXjA6I2-r-wmn-OIZn9Ed5YXniYiZvIOe1v64WwnhGKx04wjAAq1Xi4DT9VZrZr2InRY3VY6gCp8E0aOJsT__HFpgLHhVVVyW7c15jXPdkuCcQHIA5VmF0r5BF7bSRsIXbruFQNy6UHm08LLpcsGDs83O4dG3kSIJaEAuh2JQA0ix_w_wri0Ajvnc0iY1DWXVFyJfqz7kSsOMYPjhXOcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=RznlhWzCcBHxBo354A_UjTlpD1g3tzJREZrIdgrDRNhpIDBAqs_dJHcni3hZHcXOEupQRkm-_2S76wud-28Kqh-iN5SQnzUUXgplzHY6zmUgdpHdInT9qssZOX9hXPC7zlXjA6I2-r-wmn-OIZn9Ed5YXniYiZvIOe1v64WwnhGKx04wjAAq1Xi4DT9VZrZr2InRY3VY6gCp8E0aOJsT__HFpgLHhVVVyW7c15jXPdkuCcQHIA5VmF0r5BF7bSRsIXbruFQNy6UHm08LLpcsGDs83O4dG3kSIJaEAuh2JQA0ix_w_wri0Ajvnc0iY1DWXVFyJfqz7kSsOMYPjhXOcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU7puNv9Pqz3us00saOXY6fo3dOt8e-ndJPl_h5ucRtvO-4_Gyc8j0bpHwdhh9viQ-oWw77C0Waf2HZV1_8DcE5mAgbKsX--SNk7DJnCnXFGD1qOUu3O_0i43352221EdQrsuQHTCN7PuFLRuTE9IQV2akGShMaJwrXhd1beNMmHn0znIBfaxXFi8XgIdqighcaw2z9iZev6VlfsZYWjYd9WiyXQ7CmxKOkMYDwlHm612a1CO23rXZeaFQkFCLkNDT3TjG8suklPVKvYKB3Fd5LYEGntL_ytya_wtpxNXsY9epphw91arn3Bqh0Ap_Egsn7HP-ZJSjcEJoXMwj2UqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvMkSF4GhOJ-JxsKq-1tV0uawGUyX5Tddr6mHG8ACKg2_SAUQig0Hv8YtbtbbDuT-NiK15z9tXC6lb6pRvfoOYZe8b1Hmh7hi2tLdcK3VaMJtsFU1wpyMa89lpl2Lc2Z4bJrYMpA25Z0uo8r2g-2hr-X_cmT3L1PIOT7xKULWMmToIydUyX4ibJWru89P6UHSxwT0nZpO_7HMcbISL2G5mTqNabj2CgO5-bCYL6EtT13AD1II7eUBK-dnkZI1FIz_OHWqmgVTAYjnnqlmfqz1e2I4bGhXK1r8af8SrjuXMzBUqT0rGEBOUI8O0Kuc-kBaRngjjHwYlM3_lCOe84vNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjIlJIsMvORa-DneUfn6G43BGRKXsPSjva0DI65CDdfJXbSKx8EV08wtma5rZfObJP1u1BMM4XDg_oSbpypSe01begTb3c1X3TFFC6BarQ-XLj7KwUHW2U5QTM3qX9rNXNaPC94uPwsnkdTmFo9bmAaXhwXlffsaX1wsa5rGfRhzOPcdYE0PU-UfTL1HXvt3Cl_0ukboQc6d7puHHGqwHkGBHW-xx3fuTR8DV591bsA74ALRF-6cEO-7mcLPWCfKZLTaa-4vvmyoJByLFsohBYDcEvNK8P3GnSys0s4CiHlnL_l-hMBzxcocQx-lC5gD1Ap1cUVcmgzb6rqa6UlKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWb3jj_b7dReYy-XcrE-Qa_OtGI4OEdO2Dw86nSF5N3ZuWfowcjmu881i-_FQ07QwlxacNtP--oZOEQVMiknaOJD4UHLSuJkGIsHzZ1em8C3je-axJsxyuu1HD4271rW18oSb1r8KByVTl6lD4ohZyU3H6NFR-SEa4p4pSmgnCzSkX0sZyJbqTt8q7sgsrJ-61HEpFfEj2_eBc_gC6oaPOwJS8-C6JGy1PKmfA_qRDnVG6xdyW5R07PSjWLpYOiM034j1aDTo2dt-o7IIvNM7aJtBUVlerFyyB6Ox8OJsZuC0DuQScSfL2V5C7XCea8gOIu0lMSYRc98w10bz3ZRag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=UWCQbJHuuhneNND_JZW_KiFSYJTLq4lgEJXmJU-ELGgN3D7zb71uKE8nVDEB6gGhy7a6HyYhwMLRqbL2g5RWJRP5jkeSAYxMBn_zmO7hwGM6nqazgNXJBzq5737JYYDOuEow9T3W2s0s8tcJnWG7NNRFq01tc7y3fzCBLvKrbFiJL9y3tfKGROaaj91uH546lUDJPYEudGpZQ2JX72cVGfxXJTcOWfh9JNWjvb0vLwdC8gnHwYaBz_msphKRxoM8oDNRVRKSAVV8A15bJGoYjsBhEDvPfCPwdFQOaoGBBHtwcWdiEKhyjgbMe2ADWy3C_QisLjMPjSKWaUnSu6JxXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=UWCQbJHuuhneNND_JZW_KiFSYJTLq4lgEJXmJU-ELGgN3D7zb71uKE8nVDEB6gGhy7a6HyYhwMLRqbL2g5RWJRP5jkeSAYxMBn_zmO7hwGM6nqazgNXJBzq5737JYYDOuEow9T3W2s0s8tcJnWG7NNRFq01tc7y3fzCBLvKrbFiJL9y3tfKGROaaj91uH546lUDJPYEudGpZQ2JX72cVGfxXJTcOWfh9JNWjvb0vLwdC8gnHwYaBz_msphKRxoM8oDNRVRKSAVV8A15bJGoYjsBhEDvPfCPwdFQOaoGBBHtwcWdiEKhyjgbMe2ADWy3C_QisLjMPjSKWaUnSu6JxXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=B1YlouXsXCewbd4gJbSgvJ0_THWn7Ec7e2EJ-aEyI5rRhBlPI68Y43az-nc4yyNUu1pcDD7vyHSBGG8Tet2Ld-eS1USmULcHUBRT5BtGHEH9daq9drmESauNyRRWdWlEz3ANXtS5dkMnyZs1rKzYH4tMo2gW5I_URhHwn4x2iILt9MyTy4Op4s4x3R4ZtO019b7xpxhd3VpaMAWVSufv2CKx9rlewQkK1FhwN5tqj9FuQXRmYahDD09whk1lYJY54UnkC1IrpP_NGjoOhCwlUJsJAG7qZv5x6OBRG7NfpqOUPzhd8ilETX4PMnQUT3jpnXCgCHNRnGSHzMN3VMTR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=B1YlouXsXCewbd4gJbSgvJ0_THWn7Ec7e2EJ-aEyI5rRhBlPI68Y43az-nc4yyNUu1pcDD7vyHSBGG8Tet2Ld-eS1USmULcHUBRT5BtGHEH9daq9drmESauNyRRWdWlEz3ANXtS5dkMnyZs1rKzYH4tMo2gW5I_URhHwn4x2iILt9MyTy4Op4s4x3R4ZtO019b7xpxhd3VpaMAWVSufv2CKx9rlewQkK1FhwN5tqj9FuQXRmYahDD09whk1lYJY54UnkC1IrpP_NGjoOhCwlUJsJAG7qZv5x6OBRG7NfpqOUPzhd8ilETX4PMnQUT3jpnXCgCHNRnGSHzMN3VMTR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4f2UA86HL3zPnInQWwZ4z12Qha3PvYcVsCaw_ZDReJ-tsBnkzdSvaTUsYXJU4JIBxRJDECgpUgi49pCfIDarVmGuQLkam82uAgmpE_DBbCkeDz5NmRvD8NsBtKi8_zYOMNHC2yvLXgXGdWaAMtGfqLQjF5n17SXaceCBFyb1LsfS7TRrLbmFCIoLRoRwJaMhj9FXElm42eVr2qhXJobjc_tdIBXA30h6si4TdPLeNA0jl0_0eLH5OghNrI6XdLDI1lEwy89AK49__cEl8KOFqYDKWj-lgyet_kEYgHD0YgZ2U1LtkyJ2qi-b8X_mUo0VSDUvNIMmXbd6QwjeZt5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=MmAkbbv1lKKr1LqUJC_8MpWJV1y8BzFWClkZhlO3CoPKBzZ4EirwT93yCXPh7IvC3qtAtgVEqupcpL00nz5gQtkPVXyAHE-HJaqR8t2_D88NcUQ8-kGXriDOtHRFICXLN025QImbe_X4NLD59OaGPR2MZ6OaPtDfi0fLXTGBTohaelEReLn7mfXEOePIkDUCRTIegvuYmqH__5Y2BxUdY3VxbqUO3xEPhsKOIdbzIml2Jjk4Yagpzlb8927B_pZK2PW9IQFarmwVvpvHTDmzBnZUTesrL2b-ue_eirw-fjN6hgCaefcJYwfyitoloNdKWtoZMlykMIeSEEoqenqzSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=MmAkbbv1lKKr1LqUJC_8MpWJV1y8BzFWClkZhlO3CoPKBzZ4EirwT93yCXPh7IvC3qtAtgVEqupcpL00nz5gQtkPVXyAHE-HJaqR8t2_D88NcUQ8-kGXriDOtHRFICXLN025QImbe_X4NLD59OaGPR2MZ6OaPtDfi0fLXTGBTohaelEReLn7mfXEOePIkDUCRTIegvuYmqH__5Y2BxUdY3VxbqUO3xEPhsKOIdbzIml2Jjk4Yagpzlb8927B_pZK2PW9IQFarmwVvpvHTDmzBnZUTesrL2b-ue_eirw-fjN6hgCaefcJYwfyitoloNdKWtoZMlykMIeSEEoqenqzSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=B6S91dfGts6J1uNoabCfksFxcTSx1oZnUYTeyuZSWVvUSjijNbDpRmVII9s-gNHQHVYUur96TBIMe_6CNe6RfP95MDI0Gi0GxLqbOFKLIhq9udwELdtmyjCAwUsCqQzC76MFf5Ae7tCBPd2vIqw22Wx_Hrx3UTs8uQSqv1cSfVpc_sY-VOwJicFiIn8UZFhcdpjvDoN7iawnGOPdlGDVeW7oSMjru6VNjtCpxVd8RoCIhzsj7JCppK0fqfR5OhOwQ_XxlVcEc0LQpFVSkkS0Y_pKonC1K89upPbhfNTZPESBM0wX7fWIs2kX1lVuUZMb_SryeeVkAJpwjVkNLj7djbVudDZIav_lg5y6amXqOS-jHFT6Ss7ivnHrE23-7pCMgijGXI5tD5fdKu5m_IjhFhLHPgxV4IxRDKijGTJ7lk5PycdO4FTnwBdBAkjiRhCUW2co_PaZt2M8gbdiXB9xmVb4rgqtneg8M4kWXtwikTjW0yWFEZDar7TvLp01RUCKmj_mtUuTjiZpuiZtqkLtT0efzFzXLN4LjP9mUwbpOrhYlUiAs59IVKLPENDZkbNK3mHQ55Oi9OhRdp492sL6kIdSW-Uy6mFFUhFtZd6Z6Sr4I_iJdjncRz_5jjQj1h1Z-WRjpSo3H4fTCNc7GgIJywhnxApYvTlYsJExsWEw2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=B6S91dfGts6J1uNoabCfksFxcTSx1oZnUYTeyuZSWVvUSjijNbDpRmVII9s-gNHQHVYUur96TBIMe_6CNe6RfP95MDI0Gi0GxLqbOFKLIhq9udwELdtmyjCAwUsCqQzC76MFf5Ae7tCBPd2vIqw22Wx_Hrx3UTs8uQSqv1cSfVpc_sY-VOwJicFiIn8UZFhcdpjvDoN7iawnGOPdlGDVeW7oSMjru6VNjtCpxVd8RoCIhzsj7JCppK0fqfR5OhOwQ_XxlVcEc0LQpFVSkkS0Y_pKonC1K89upPbhfNTZPESBM0wX7fWIs2kX1lVuUZMb_SryeeVkAJpwjVkNLj7djbVudDZIav_lg5y6amXqOS-jHFT6Ss7ivnHrE23-7pCMgijGXI5tD5fdKu5m_IjhFhLHPgxV4IxRDKijGTJ7lk5PycdO4FTnwBdBAkjiRhCUW2co_PaZt2M8gbdiXB9xmVb4rgqtneg8M4kWXtwikTjW0yWFEZDar7TvLp01RUCKmj_mtUuTjiZpuiZtqkLtT0efzFzXLN4LjP9mUwbpOrhYlUiAs59IVKLPENDZkbNK3mHQ55Oi9OhRdp492sL6kIdSW-Uy6mFFUhFtZd6Z6Sr4I_iJdjncRz_5jjQj1h1Z-WRjpSo3H4fTCNc7GgIJywhnxApYvTlYsJExsWEw2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJl_Gw65t5BEi9TTCQQXHsSaPvuKVlovF_QUsceMg3r3XDgAUzGA99t0kd-TGm8vRK1NLbASjKjyTBG-28pcZI8dhtF_29DBzHSrzN9ZuKobAn-N_scjfHHgXxm4zsV2oOglLxdxMrMrYDREmokURlYMTEfpm0-ZDoti1ZoZfPRtD7MDk09o7-VuOsjfgUs4-gKqOdBAvKKMgJMJY6AmXtnQXlvtu5jnDIREA18AeoiY10rzcJ-ECeU16JwEDrdieWtcHoYu4OuCwAY7eYMC0EW5SVMwBh_CXfIOiw_9DkG_9hiX5I57Ix2XpC2r7cHWG-U9jEyuGMpLBslstOz2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNMbwMdkp-RxANcnFjmD9mN2oiDf4SJxeCq3ZRWxYkimd5N809rHQJZrWhs_An-GGCXbNccgspKhmFe-lhvFcg738EqqzTxjKAf-TzgTVcVWILwufp_LY_ijif-C5HnDlUZywJbfg8T0na0voQrdeQBg245oyEa82eUx3xNw8L2vXxkPBsawiZVNjnMSq1TC8qJxA0VMb3ZYBgt3-fEypvrCtmyPOjT7jQyRVGisMef5ywJqWe6uxTZOrglUiKjDFZyT1_pehKv3heC2jcU6NTNTvO-Sw9FSJWKBHn6x2XdkE5TdDkQEkp3wzXMuDRbpZ2X0kH5FpVJ19lA2pgZm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sM3ZJgkUVkpp2wXerCWja1yMNOlREoBikG9NC1zkvXS70atqxnnNFpJEi9B-gs-Dt6diVJwvHqSy4_PjQiLWzQcvc20Ku5ZRmzyg_S3yxCD_t3FnBeM1dZBl2HPIhzqR1iRSqZm6MTWlO2BgVpZm5UoeI2CoWU7NgA71h4IYWZoyGqqL52G69aHO-BGi_xVWcIW7zqta_IwHwcgLEh5l1_FBVxRdkkkyKUfetOFwEngMaqhBEOkWdz2CoT9cVJWJ210HmDUjrKAOxtm8RY2Tkq80nxdEH9JrjAceuLGGCULEfAvTFAMMAAYrjmoUi_ImYQsfsMcDmwFnLpPKjxf43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uf0QreX_rg-83E6RRS4uGVM-QF8o8dgh6dWyFww6t9jeR6gjRAI4yAPaP85ArPPKzfPIhZJhNGgWNhleEMrZUW2ryhnTg93hUcN6Rnd6qLBFfB3HuXOD6TOMgH0utYTgRFWgqwHQEdlcmlYir4B2GsG-vaTRrCZuZyg7mDbM-8vXpI34sHpxuATjLuuZPTGsnVb_QavjbEbDX2EtIU0JpISY-X4Mvp61Swf-muEMKKwRptXaFYaeavXVFrCeNe25SXxzdntA18_Q8BqC6JG5QwSnSHoixlZjtKEaICOcsvPSldk5PSXWAqbqr_bVAtQn-HnguWSSd5ZPOyGwsySnJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=EYzp-KWOYqNCWwPVEN9KTRzIrTFbea41-j5tgaDdK-HIe305wGyKAfh_fd16P2JlDwHARslCvQfD5LLv1rPGaaSh0014ypVFd9RLTzhWxqbkbpU13lAbxpYDQPlcL1_Ugl2m9eYoUIHvdnF4u5VZnzY3_fh9Gu_-vDG73-HvKV7oFDxt_mgCN4ry3piL_rtXPJHk3I5RZ89r0TkcRHklURFU070Hhi_0rEIXctoDS1kJ-vjTRNpvlrbKDd49MsdBy_PUCIDFK5o5rYRWg2-0KOb0NB1kfkgbPgATo8RKQx0NIk_FkHX4foFsm8f46fcRzDS036ugzGh87NR49i8-Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=EYzp-KWOYqNCWwPVEN9KTRzIrTFbea41-j5tgaDdK-HIe305wGyKAfh_fd16P2JlDwHARslCvQfD5LLv1rPGaaSh0014ypVFd9RLTzhWxqbkbpU13lAbxpYDQPlcL1_Ugl2m9eYoUIHvdnF4u5VZnzY3_fh9Gu_-vDG73-HvKV7oFDxt_mgCN4ry3piL_rtXPJHk3I5RZ89r0TkcRHklURFU070Hhi_0rEIXctoDS1kJ-vjTRNpvlrbKDd49MsdBy_PUCIDFK5o5rYRWg2-0KOb0NB1kfkgbPgATo8RKQx0NIk_FkHX4foFsm8f46fcRzDS036ugzGh87NR49i8-Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYBhDmLBpY9w3n1HrxBGK1Wrg5nGIqPQ4zY8GZbHiXjt8lM4fSZJv6-Cj-sBZpGqjkoVKpW-KY-qTX4LK4k-vFbCaW_1cyp4QJoS330trb09l_rwIaqUYTm5_U8PFMMNLNXdk6t53H3ShndF-gsJRVj5Ks4tpT-GDEEjnhHLcbc-ZuETP7jHClVyi_5C0kjTBSW-IpimSE0VsI-KBoUBN46NmPMXLvSt-qbDuah1B88CsdZXVoIovjhuKlBfo8wEkCUMmmuwc-yUZzRRRMDaKZ0frhcPxQzKG8-NYvXSNOVBf-nG_UEtsUVAWLEHJmdmRQBHgCKAB3H6S4RF6jLTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn88lCiPFucil6vxiOcakMmAZ_x3VK65Sww0UAv0oxB06GQkBMuwJa_YrVmB8WZkHLm3C4_Ech_8Nzj0GOVhP9DDSHkvoxYqlFIOquPMX9ozuMncn6XdPZrWp4bqkcs08F7QIv7MrEoU37OHBn_l-IRP7-waAWvIvJM_zIHR1VJthz6h10hdFjLP3lD5RDMWfaVI2qc9LpNImhUuV_fgwT49poS0fuF9rOBlcMInvJTEoSVmdCou9lRRsgX0fJGJ9tsB6MIJbuxPMbP9GQDIxQtKFnQ1Jb-Dx5PqnUdyDJs9ZYWgtZzrtw8TZShGy3R_WU34qfPp-QKadhaw0WFyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=R_RV9WhVMkr8Ev6xPVDEDQf5R6I3Af2UC8z0jeZj9DYXExt36EzLMspClRkVlNsOqkcxxd0v7uj5RJi8bPu6wkg7bsLHTpIwtvf8oE4JxOA6vDvT3fcc1yLa5ZvGn5IVkfU48pDPhKkIe6GzI674sxpVsjwhmnaEiU73fEIGuNYgmyHw8XEtlOqfNGzXV00gDdNeEB9hU8erBy5JCwthvmMkYe6GdL7znwsd8a0wDp7xsB70CwSu_WMNm4Bd8YE6TuXn2gHS7C0tRFQiQjgnFVRD0dk2RgCbPdpx_IrTensbVU6mIsL6Htkm9xXVpufQmO8VzEgUwISa-15U7wZ-zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=R_RV9WhVMkr8Ev6xPVDEDQf5R6I3Af2UC8z0jeZj9DYXExt36EzLMspClRkVlNsOqkcxxd0v7uj5RJi8bPu6wkg7bsLHTpIwtvf8oE4JxOA6vDvT3fcc1yLa5ZvGn5IVkfU48pDPhKkIe6GzI674sxpVsjwhmnaEiU73fEIGuNYgmyHw8XEtlOqfNGzXV00gDdNeEB9hU8erBy5JCwthvmMkYe6GdL7znwsd8a0wDp7xsB70CwSu_WMNm4Bd8YE6TuXn2gHS7C0tRFQiQjgnFVRD0dk2RgCbPdpx_IrTensbVU6mIsL6Htkm9xXVpufQmO8VzEgUwISa-15U7wZ-zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=FWhiTWc4x0RQztKfRMhhtR8nB77taMljOJPEryITUvG02BwK6v8A-XG3LAqax8mgGB0G2owxhxkNESaOaPQVSlc8tCxXPQbpmUUAIW-1_BhBw3gK6pykcmHbtJhy1wpu93_5-QMFT2MLWmFfaFjJcV9ZKu-oUt4Cvlzsw7Foyw2M6lTbLBhErlq1kMmnRNjUOD0s02D41BJNYAhc8ZCwZUC_tNyCDD1uiQ6vEKHL_BZc-jEJFmY1noEqzhN8AQMkXUyrRxDsYM_DS9uKPX2KZI8L88cq4mCtuDQkIsVT5udI7I4saT3PabWM-Ew7qSLExVzdP8lfJ6iT-GDjd2ydnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=FWhiTWc4x0RQztKfRMhhtR8nB77taMljOJPEryITUvG02BwK6v8A-XG3LAqax8mgGB0G2owxhxkNESaOaPQVSlc8tCxXPQbpmUUAIW-1_BhBw3gK6pykcmHbtJhy1wpu93_5-QMFT2MLWmFfaFjJcV9ZKu-oUt4Cvlzsw7Foyw2M6lTbLBhErlq1kMmnRNjUOD0s02D41BJNYAhc8ZCwZUC_tNyCDD1uiQ6vEKHL_BZc-jEJFmY1noEqzhN8AQMkXUyrRxDsYM_DS9uKPX2KZI8L88cq4mCtuDQkIsVT5udI7I4saT3PabWM-Ew7qSLExVzdP8lfJ6iT-GDjd2ydnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=b0QpCTpR6xWf3E1Xo4Pj-Sni-hv3J97zMyGSBtw8OiUZ7vx3cAchLJJv2TwXmh1oF_KIKMi5eWdj-EtayjRbXtjkr4q5tacCmFVwOefXzVmzprYGgYQlNyDDh1NsRTUrVb5CEUIjQ5WdRqu9ILiM1raAyu-Assm9Kpo0BuD1Mj-sp-QbUkNQdIQ2R-CbhT-Jns2hkLeaLqnBmAUWu24ysYTts-DKkGu15aFnRT3lTmjCKaAoOTwuD1bK0BQI0JoNXHGRVwhVhzk1s9V784teH1YBcJwWKGGIzaMs0F2UFUmgYJZxYfDpdQjPW1B61S47bFexbTQDb3osoaVqlrLk7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=b0QpCTpR6xWf3E1Xo4Pj-Sni-hv3J97zMyGSBtw8OiUZ7vx3cAchLJJv2TwXmh1oF_KIKMi5eWdj-EtayjRbXtjkr4q5tacCmFVwOefXzVmzprYGgYQlNyDDh1NsRTUrVb5CEUIjQ5WdRqu9ILiM1raAyu-Assm9Kpo0BuD1Mj-sp-QbUkNQdIQ2R-CbhT-Jns2hkLeaLqnBmAUWu24ysYTts-DKkGu15aFnRT3lTmjCKaAoOTwuD1bK0BQI0JoNXHGRVwhVhzk1s9V784teH1YBcJwWKGGIzaMs0F2UFUmgYJZxYfDpdQjPW1B61S47bFexbTQDb3osoaVqlrLk7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=SIVZKwQ5fzAVDK5BIID-fuFMvP-9D0UMuqeo7kWlecG2qrcSBeT2HftJFxnOjuiXaBg6eow-Y9_lEYWcdzwF-iYcihAGerHRZLcDegXUNsCncyM_DKHgG4mLqOwFBmhBy2RoIfqcY367HX9XZIZxQv_m97XuNhlG1vXbetHDGZFi45jpWsK9QErGx0u73rWIoxVy7sdFy3CmdK60FqVNP1t_EFtTJdxLvu5x-LZlqe1DiqH5AX3FV8ow4hCSoSIykPjykjlRImW-E8_lm_4DGuBkxxdxTSXDQucktXDbV0nSXz_2PjzFx6R7AssxGqwEL-NF8BEwK8sYtq5WhZ2lNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=SIVZKwQ5fzAVDK5BIID-fuFMvP-9D0UMuqeo7kWlecG2qrcSBeT2HftJFxnOjuiXaBg6eow-Y9_lEYWcdzwF-iYcihAGerHRZLcDegXUNsCncyM_DKHgG4mLqOwFBmhBy2RoIfqcY367HX9XZIZxQv_m97XuNhlG1vXbetHDGZFi45jpWsK9QErGx0u73rWIoxVy7sdFy3CmdK60FqVNP1t_EFtTJdxLvu5x-LZlqe1DiqH5AX3FV8ow4hCSoSIykPjykjlRImW-E8_lm_4DGuBkxxdxTSXDQucktXDbV0nSXz_2PjzFx6R7AssxGqwEL-NF8BEwK8sYtq5WhZ2lNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=NonobEhXwaP_JhC2jgqlW649LZN-xPg6_dnr3PgXMJCuQ3OLixIMxxBMM49Z8Kcy418xv4QVLRne4Eu-dZJi7ZvmlJedw0xG2a4mKG_oSfVkZpQA5Ow0FJ9noG0ReWYrSUDd0KrftsWQcZ_N0rBfjp_1XhltzKgnuAdQsS1SXAiV8tL3i5Lx8bEZC1SHb_vckh3V9W4h9QhkKo-s9Ir_QIftuATFZ3-Thk1je0C6xZkWHdr7JyZyi8MHRPLvgih7m49Ghw5L00F9duzs4eqdfwuK0fJxN11P_80gqOsjvNLyQW0zNjexc9nsjvxZcrtoDwdgvgnCe72_SQuYQ77_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=NonobEhXwaP_JhC2jgqlW649LZN-xPg6_dnr3PgXMJCuQ3OLixIMxxBMM49Z8Kcy418xv4QVLRne4Eu-dZJi7ZvmlJedw0xG2a4mKG_oSfVkZpQA5Ow0FJ9noG0ReWYrSUDd0KrftsWQcZ_N0rBfjp_1XhltzKgnuAdQsS1SXAiV8tL3i5Lx8bEZC1SHb_vckh3V9W4h9QhkKo-s9Ir_QIftuATFZ3-Thk1je0C6xZkWHdr7JyZyi8MHRPLvgih7m49Ghw5L00F9duzs4eqdfwuK0fJxN11P_80gqOsjvNLyQW0zNjexc9nsjvxZcrtoDwdgvgnCe72_SQuYQ77_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=OzrzjzqPw2HW7NVYQTIdeevmgdA77lsze12PO2mQaoXAza_LqDah6cijy4bOfhilm0inMMSEuK--7zOkGf8N_zVdpkeAqGgn887JWaZrzoU6h4HYb9YOm-rez9NOiEeJSh_aGaHvRnNLomypan-j_Pw13J-OkPf85_HMQTeC16b7zaGLM0NbaHIVkuHVrElqK-8Xhspx3c9qoOkqNAOoyNDs3z6pmZYHWUoc0VmYUinjk0xSDZVNiT8xfKy25eqoETW1kkJTE39wF3X3icqW52EKEqjNqGcefEXeGn0P7sriyQPgwLJDvxfJpUIpUcVB0c5t83MiV5xtrfIBf71xeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=OzrzjzqPw2HW7NVYQTIdeevmgdA77lsze12PO2mQaoXAza_LqDah6cijy4bOfhilm0inMMSEuK--7zOkGf8N_zVdpkeAqGgn887JWaZrzoU6h4HYb9YOm-rez9NOiEeJSh_aGaHvRnNLomypan-j_Pw13J-OkPf85_HMQTeC16b7zaGLM0NbaHIVkuHVrElqK-8Xhspx3c9qoOkqNAOoyNDs3z6pmZYHWUoc0VmYUinjk0xSDZVNiT8xfKy25eqoETW1kkJTE39wF3X3icqW52EKEqjNqGcefEXeGn0P7sriyQPgwLJDvxfJpUIpUcVB0c5t83MiV5xtrfIBf71xeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGq8ymeaMhf9lldeuwoPCpSg802C2oHF66L4-TkALksKZZDgRFQCYq2r83iyiOXjH0kXmtNWL-pklfpu9P7NnFpmLyAnNCF-OrQ3_5al1PyEcsLWVNIlUc6IXQHrfbDW3cZCBiT3LnZMaBVFwKqcVXuVmY6BZ_gqWsRQML3RuMo5f_zy-1vX0Hz5yoi-sDrzRTqBnD_wEszmB3mCyA7VasnYOf5EcWx1npi_3UOYz4L9ov28Y4VQiiD7VvRFERFjHo7Cgdw26SMWyXdhJLJ7xQzFU6cxxfN0yX8DxH_T7rWV4AfysARS6BGZ_4CDEqNyWkRAtA_x_P0YkZNX0A29bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubhqm6r9t_4sqKMxTWELOMelXLBtCuhByPPV4LBaTiN0aBmEI3D3rqeay9roPwTWebft-3tzJfr4xlIgDMR_XY_CK7MMMM_2zSd_0sWZNDZrTjFfOInOo-kwVailmN8xR2GMZjCupNr1Tvy7aVwgb_bksOOkx5hIwPBbUBYbltvQA2Wpx4C81dhB9uvhppHT_y8uDFJkbjH0m6AIdcc3dIkIVBUKQVHSkwWW3lBYVznT9jJJPvKrQWydoMuHSnPSYo4_e8OkGDNAOe06ddRfj-_Uz6-2tFEmAswRLRhV1VjA1pkCNnYHy9w8dfHWUdv0sITIwycfunWGGcfOMZfbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdkmhS9q0OHbn9ogkDwKloWFHDwn3LY3nzli9UFo-_Wzm_eHCldKxCw6a45rzrMjdjl8jxNyZDX0uDCZEhiTs315yv54p28i_Kyccec_1vVz0kIe8L-OduyyDEQx_8DRsHN6Z7mE0qE-Bki0SW5DBpbmoL-4lJqUfisgdI545NvWF1yGmQg1KwDAAqgEjhxsVdhAyfS8m6ous7lS_3rCtT5VH4RIGBI-saFVmX7dd3xeDgPzpHhAoKADqD2j0WsiwFVbrWXl_gzlkNi4kx8O511qd_thzASS5kOPqutjl73cUOsXkzI3vvNWZ6xKY1IUUzy8ZBW0_-R8HVa7zH-Fug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=BfjRStVv9u4ya59cwGgWVTCCfT4Kv14S42KAxXKab_d2iEFMdS1Hbdfk3NI5vtw4qEgmHkSKIgF2hKq3HCfM3ugoK6sRIm4Rrl8T2P6VdU9K-2HlVkVGgT6SWNMyxVe_MGq75ldMLfgSOKy9-ScgTQLFUlfMWCzYDPQBnrEsoqH_K0BYjchmKoQrQBEZYSz0SNxCqdVqyRNZL47KIRCZZbAecyv8FQDivWJrbBYK1ekQWdNWj7pbCbhYHFuO3_CNHoxGUOva1qPruqcV9DZ2sO47U3b64s_hwYgJqmONJKgysxWECM629AKQHwYaY-fbjCk7-ajjDb3j-Y9c_qXZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=BfjRStVv9u4ya59cwGgWVTCCfT4Kv14S42KAxXKab_d2iEFMdS1Hbdfk3NI5vtw4qEgmHkSKIgF2hKq3HCfM3ugoK6sRIm4Rrl8T2P6VdU9K-2HlVkVGgT6SWNMyxVe_MGq75ldMLfgSOKy9-ScgTQLFUlfMWCzYDPQBnrEsoqH_K0BYjchmKoQrQBEZYSz0SNxCqdVqyRNZL47KIRCZZbAecyv8FQDivWJrbBYK1ekQWdNWj7pbCbhYHFuO3_CNHoxGUOva1qPruqcV9DZ2sO47U3b64s_hwYgJqmONJKgysxWECM629AKQHwYaY-fbjCk7-ajjDb3j-Y9c_qXZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=aWKchDG848VkEeKGZdPxHSNZbL-EeDHygyGTAb64aDeZN4kgd5DzpfTMQR3ITOqyInRoqFsDO4W7VPf2DFMBAUoylnYd4GzXTIcO-FIINFzCikyyGxhlDLM87K3b0VjZF-b2Zc72JtJdjZLiPptebiEtae9VMxJ0xCIucZT8N6gFMSm_nMQvEba5gQB3otJHfH5EEOFOYo8w4oOPV4Fyfwkao-A3A_BXHVuT-DCTMSWfa9Su74X5pd38l2g1z8S8VF7BZhxx96ebkk9JRbChPjElMsIxEz1ICTMei6sLyMfrssjEYxA-O6_XQgIdPbWNiXeaQa5oD4xSGpmamqx2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=aWKchDG848VkEeKGZdPxHSNZbL-EeDHygyGTAb64aDeZN4kgd5DzpfTMQR3ITOqyInRoqFsDO4W7VPf2DFMBAUoylnYd4GzXTIcO-FIINFzCikyyGxhlDLM87K3b0VjZF-b2Zc72JtJdjZLiPptebiEtae9VMxJ0xCIucZT8N6gFMSm_nMQvEba5gQB3otJHfH5EEOFOYo8w4oOPV4Fyfwkao-A3A_BXHVuT-DCTMSWfa9Su74X5pd38l2g1z8S8VF7BZhxx96ebkk9JRbChPjElMsIxEz1ICTMei6sLyMfrssjEYxA-O6_XQgIdPbWNiXeaQa5oD4xSGpmamqx2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=td7-SCOHBVtn6bvyDyhNQLQPSFGKYi6hJWVolU7vzc-pIxFCsHBcWiOvzrDf9OFTAKkSNjIiwnop03feBRbxrScSADsAEMjjn8X4M8KjZer8z2TOVnjnAbR0-JQPVT8v7yUQ02V-BVYydit8WsJnfMLvZixQZT-SfmDNTEYPO90hN7Vb2oPPgcwQHNRYN6A6Friyhvd2GVMLw53h0HAREBV8xWMVi5hzffsTimWMDAMd-YohnJV8MWO3-DidMJ7hDMmUsVrgx5VtnchmsWHSp_g9viyKq2-_O8FJdX5Ny5d3prB1RNwzqCsF8VXslahgM7yg0TjYctVPCPaS9XGm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=td7-SCOHBVtn6bvyDyhNQLQPSFGKYi6hJWVolU7vzc-pIxFCsHBcWiOvzrDf9OFTAKkSNjIiwnop03feBRbxrScSADsAEMjjn8X4M8KjZer8z2TOVnjnAbR0-JQPVT8v7yUQ02V-BVYydit8WsJnfMLvZixQZT-SfmDNTEYPO90hN7Vb2oPPgcwQHNRYN6A6Friyhvd2GVMLw53h0HAREBV8xWMVi5hzffsTimWMDAMd-YohnJV8MWO3-DidMJ7hDMmUsVrgx5VtnchmsWHSp_g9viyKq2-_O8FJdX5Ny5d3prB1RNwzqCsF8VXslahgM7yg0TjYctVPCPaS9XGm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9rTweIX3x2rpke-eLvkFZUbvi7ovk8NfCLhJNOQh6_uQEP8_P2Kp9aiqJkEgepkQk6mV421POfRrMYlwz85nMex67GQ1VMY0pszS8_6S5EiIk-uMg7kTm_AnthSWDyHU33oxSscK05Bqe3xXu8pfCYE6SbbP0DbgWpjOfvPWio5NkH6Blcs682Ck0eY1of9L5LAQKUvVzJYyf1bprRTWx6-uZsj6pHQIQSbgpiT2d1MNu89WweaWe67A9RyZkV-Mji7fTCZjJxZ1bCDe6dWLJ57gZ0jgrV8-Aa1Q4FgFQcPmpXcczA0qK9fJ25V0pv9_naFDJCiDusqYr3Mh9tVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=XDVWxQvzUjquQGFI5bvscf6s49NqP2Y12YR6kelRirQR9X5VQVT5GD0CEcWr_DwXjzSHrxNfKEoTrV_8J4GwYRADHvqM7ujOJFeT1IePesQoVYxPojro9OO7oX5aHy8-5WDYvdlg5p3rCzym-sPOQKgJ1OEOCsEKUgpnXgUcbwqsox44xpA8_2sfmzInhZrJkkgEdHQhbP_TwHMos0SFWr7RLY2Ylv3RpwBP11RN95ZlZbwoCuUnX5iXWXwG_ZxlZ1I4Z_PYDmmi-7kAHc-oYkng5SMNBTwqrkfZxH4Lg5q93XQH2JfGc2LnXzKK6RnEeY3LZ5Bkhx66tFsQRzLGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=XDVWxQvzUjquQGFI5bvscf6s49NqP2Y12YR6kelRirQR9X5VQVT5GD0CEcWr_DwXjzSHrxNfKEoTrV_8J4GwYRADHvqM7ujOJFeT1IePesQoVYxPojro9OO7oX5aHy8-5WDYvdlg5p3rCzym-sPOQKgJ1OEOCsEKUgpnXgUcbwqsox44xpA8_2sfmzInhZrJkkgEdHQhbP_TwHMos0SFWr7RLY2Ylv3RpwBP11RN95ZlZbwoCuUnX5iXWXwG_ZxlZ1I4Z_PYDmmi-7kAHc-oYkng5SMNBTwqrkfZxH4Lg5q93XQH2JfGc2LnXzKK6RnEeY3LZ5Bkhx66tFsQRzLGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=U3WeExb9iallDh0KGvq_QbchtwoXdCvQ7NGyTuQUaQFGRN84eLTL8Iw-VZAF7R4ZdkU2No7uKwjanAPNysV97JInVkhoZAMxu9KG235_z2HaNSoKsLAIKc5oeEmgVTdTx5IZpQar3FU7TER-fOZqzCSgfnBKmx1Pb58lw3TeVAXVAJP1K2IiVOGA38egFNcVamdU6oaEhDZ_cMtdjEQd-HpmroSMFnn6jPEa0bcnhs8BQH8u-R37ocv3inlxRk7wge4t3B5mihRoz93EifoChSc4SsD1Xmk3URY9qLtLnN8QZ_XDZcp2DZsK2df0TlzSOt0Qpkca7X0J4q78TEL6Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=U3WeExb9iallDh0KGvq_QbchtwoXdCvQ7NGyTuQUaQFGRN84eLTL8Iw-VZAF7R4ZdkU2No7uKwjanAPNysV97JInVkhoZAMxu9KG235_z2HaNSoKsLAIKc5oeEmgVTdTx5IZpQar3FU7TER-fOZqzCSgfnBKmx1Pb58lw3TeVAXVAJP1K2IiVOGA38egFNcVamdU6oaEhDZ_cMtdjEQd-HpmroSMFnn6jPEa0bcnhs8BQH8u-R37ocv3inlxRk7wge4t3B5mihRoz93EifoChSc4SsD1Xmk3URY9qLtLnN8QZ_XDZcp2DZsK2df0TlzSOt0Qpkca7X0J4q78TEL6Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkJLUDHkiLWebGwJzPswbMxmBnnktaAO-EpLDNNOLu642vERj-ijxcZCXcgWtXN5NUS5BdnKPRyrpCRcN3ssXKmoJ79n7VPL2GrCp7dIohPEU9VnKtLZMlo83xpUmAqMYVbkbyGYzRVu12VlWtRqYH7Q1YJaAmPFeV9smFfRjHXVH3-1A-7RjRz754urm2Nq1GF5BfMbvt_mCD2lyro21ZMDGlPrsQ3knj8I_gI63UyJnCLlKiD2nazxNxn37RWc3gRyXO9h9jkd_XS-uqUVnGi1Bq7048RsC-MYytgx3ZNX_hMQTq3BkT4xseYYqIL5ZuxB8z_hqi29Tjpt12H7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=CHWi2wycA8VynVpEUcjSCnL2Dy9uJjp61IGzZAW7w3cFuzGFMeyTH0WU_0yWbSwlNO8fEl2BlSkz4syGRYf5kM9raRF9jLifMhcYfzaxXFJobQTOwTA-0L1qkTxXDudSNaKUQ-hKOiwAY-VLIKA0QH1dcDExlscryVVEBOgXo4_TDufbqaCa8ixmLPBvah657Pvh4EbDDqLr-RhcbIIHKNzAMMZtOKmzYFxdykDdg5dX4jCSvEA9bZ21gFz8o8X0OenIDeCtx1VyqC9Bt8UL6dHadLM2xqF8-_2asljPiXM6SrzPEnhsKfrYObtjGu-KQnnuLTcBsSGaCHa5EzfTJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=CHWi2wycA8VynVpEUcjSCnL2Dy9uJjp61IGzZAW7w3cFuzGFMeyTH0WU_0yWbSwlNO8fEl2BlSkz4syGRYf5kM9raRF9jLifMhcYfzaxXFJobQTOwTA-0L1qkTxXDudSNaKUQ-hKOiwAY-VLIKA0QH1dcDExlscryVVEBOgXo4_TDufbqaCa8ixmLPBvah657Pvh4EbDDqLr-RhcbIIHKNzAMMZtOKmzYFxdykDdg5dX4jCSvEA9bZ21gFz8o8X0OenIDeCtx1VyqC9Bt8UL6dHadLM2xqF8-_2asljPiXM6SrzPEnhsKfrYObtjGu-KQnnuLTcBsSGaCHa5EzfTJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=f7EQ7jLGKVJvQ4yy1oQks5V2hcKq6Jo4rqVzhrL9unY1U3wYDeyWHjSiUxkbe8hpDXilkD3cMlD2P9_gRMVx4UaD7ZIGN_bBmxlxFxaxsSR-pVwJjt_DvYemm3uy_-5vZNewtQjjmJ5nzVq_8Xw5fiULwms37diu6Trd0rXo6EJv6r_GhkA-9ZlQ7u4LhTMayyB7DZREqRiloYYhWJvm8_grhYgYBekjuoEepHQEyT7sE-wygjYUf-UfXsqrkkkOQYRReN0Gh8swxQzz97fh3YX1Z3PhClC5sV16xzYaf3D5GD_S4R3lDZKBPq6qQt7Xo2ERKCanxMTrApsTZbYOZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=f7EQ7jLGKVJvQ4yy1oQks5V2hcKq6Jo4rqVzhrL9unY1U3wYDeyWHjSiUxkbe8hpDXilkD3cMlD2P9_gRMVx4UaD7ZIGN_bBmxlxFxaxsSR-pVwJjt_DvYemm3uy_-5vZNewtQjjmJ5nzVq_8Xw5fiULwms37diu6Trd0rXo6EJv6r_GhkA-9ZlQ7u4LhTMayyB7DZREqRiloYYhWJvm8_grhYgYBekjuoEepHQEyT7sE-wygjYUf-UfXsqrkkkOQYRReN0Gh8swxQzz97fh3YX1Z3PhClC5sV16xzYaf3D5GD_S4R3lDZKBPq6qQt7Xo2ERKCanxMTrApsTZbYOZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=hnDI2K_ofV-eP6oDsZTiyqfkb1_uy7UAlDjhgN9rQvIJ705FPwfJmoW38uqUB2dxoarWOmZSPLpHV5qWsHjEOLqHUYciWxuUqT6bLYxwDKX-uZyX8AU-PqBeSXcpqwJgBxXJNZ6wDWnL6j_o4-vvcvd88WYNUC-mnK-q_4j2gBDzWnAHNRVfpXt5MqqvUwy5_tkaTunHmJoPC1_xeUg0zBCPRx7i1WtlyUIsZQwgqr7AsVj-mnhcv04LBhNzF0LcP1VVSMICxYw_IN2xOwmRnxEJfQBTXF-2skRne-oNmcy47rUnD0UTQ-NFQOaf087-_qvLso5VbCh8LXi0a8Rt-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=hnDI2K_ofV-eP6oDsZTiyqfkb1_uy7UAlDjhgN9rQvIJ705FPwfJmoW38uqUB2dxoarWOmZSPLpHV5qWsHjEOLqHUYciWxuUqT6bLYxwDKX-uZyX8AU-PqBeSXcpqwJgBxXJNZ6wDWnL6j_o4-vvcvd88WYNUC-mnK-q_4j2gBDzWnAHNRVfpXt5MqqvUwy5_tkaTunHmJoPC1_xeUg0zBCPRx7i1WtlyUIsZQwgqr7AsVj-mnhcv04LBhNzF0LcP1VVSMICxYw_IN2xOwmRnxEJfQBTXF-2skRne-oNmcy47rUnD0UTQ-NFQOaf087-_qvLso5VbCh8LXi0a8Rt-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
