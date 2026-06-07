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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 172K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 12:03:12</div>
<hr>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKnxU1o3xGCGkeus0PDmo-Vm-nH9h0ktOfQnd1Wu7ujFzwI1BtMayhq98EAeE382smq_RaiHXnlcyWjfmlX5dBhMT9cN19xhtzglL6ktj5tWc766Zczz846iRA3Gk1KiSd8zHap8qi3rEi05LzMuXnCRQzU_7AFVP_13CQgSQcFDiQzLZpUbmVAEVqBkXBCOLvZe-lJeWDeZ1kBSwPViW30E6qh2zgztLko054Voxliv3fxInDZm6cs6D99i04NpFvelBsB4oyyIoCJwTnXRgLVXyghaqSouGHIMDwwsRIb9UgAq-vkG7gcj2XKz_sYozNT5NzXrouLPWbr47pkwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کوین دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری که در تیم ملی سوتی بده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okeDmGPSsnfqlz1TZJHa7O4wjFo_t4dttwoBH1LsumkFzCKGiffhsB76nIyI-FrV57MfqyHkKegCYw9QmQORBlt-b-GzixJbRC_5PtkHVwOTWVaFnEjJMbDBS55UDD6FEsEBQuSIVfYZOaWPqu2MXvmzErCNQ-NtR0bQ2pzBM1gOkEdC7D2h5prblUJ6lh_KOr3S6sHdDX4zLVsiAHnbp4ddDZE7Yd3gTEK800xrsnpCDIImcU91pPZu3LQtg3VrT7WCqu-zFdrF4VEd5ix5IDlxPagQUUK-fjAl8G6npUCfUTBCgUQqYXP0tU3Hh4ka7-Q6NKEM4p4fluZkmtaPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM4Xz-Yhsz4-X-MYe5JzaoOoy6D2L-9-Utnhl7qb7Vn1MBYflfNf8fUDuE4Xt9DI4jmFB91Yn4Yjlguqnchkk2ybVMNt39t4p8oV3gnr9ne1apvw0kZFePwDmk0aQLZIdAcorJmCtHtww8jUNlhjeJCzig3K6dQ_WV8P3f0RutBHNqqfuk8f48NPultnBT1oILtbFFjKJ2D2X98SxBmUNq5R82jedrBfBrW9jThbYlvNpLw9jvqDtsNGHUKqY3y6dfkrHO7CTeSArYfE7t6sWUPZb7XvRiYrdvNnt2iEt7xUejNB9GMn1o-gdpbb8cB9Btk9FQ15-CutxXg6FYjBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=hFq31mxM-BgQJnkonvEESD6sw0nclzNL_mZm-kRfsfx1lud0rECa9jj5AZopwpjAXxkNeamFJPN87tj_0iRbgcZbpgd4WsbdDnZTURq666njweXUBkFtiMtEIFbDodxXf3OWkn9LrZ5KS8_whZ5crnF6WnkJ4Y4QVZwMewnNgxJ7NgCGUdBXMxT1P9Fst0XLvi-BYU2WJihgKZ50hOxpSqXfWeLWm8lM9qCiB-N4rvaThWGZhVpW7cK-FQk1bLMDFnozvAE7aeTG_cAFw_mDvfCzDN7Z6L4e5PM_LANu7QrNmoId2h2LfMABl2s7Bm97MtwEBktSemKV2w4qUb4_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=hFq31mxM-BgQJnkonvEESD6sw0nclzNL_mZm-kRfsfx1lud0rECa9jj5AZopwpjAXxkNeamFJPN87tj_0iRbgcZbpgd4WsbdDnZTURq666njweXUBkFtiMtEIFbDodxXf3OWkn9LrZ5KS8_whZ5crnF6WnkJ4Y4QVZwMewnNgxJ7NgCGUdBXMxT1P9Fst0XLvi-BYU2WJihgKZ50hOxpSqXfWeLWm8lM9qCiB-N4rvaThWGZhVpW7cK-FQk1bLMDFnozvAE7aeTG_cAFw_mDvfCzDN7Z6L4e5PM_LANu7QrNmoId2h2LfMABl2s7Bm97MtwEBktSemKV2w4qUb4_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCQr5lQIG7pUefNUFLKc9DF19gJDTnsNQIy5dYYVjB92oPIs9QwUFoL5VjsIByr957khbqeCWJHlDdd0t2hFR8_jghTL90r3HOugdh0bQrd14q_d0hMSt4ANIzqyHEGP9SJgcecHUi3l4BbUxp7W_VjC00PygSZ06xnCZFBfcRRIEyg3erq09KE_DwX74hCTX33hYC6wQ5EHaK-1Eq9_RUa6hd6i2UMpBzU71HRCjIKLrpFuvsxeVxnbk_jEu7XchUipjJt2k5z2vp8E8qGBLWR9B5gag40gbPlFleF3UQXeSUjyxOH4Z3ufgIhgd9zWuel5nhcotgHt69z5EbMbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcIZKiInmeKjbz7gucWvpbmiH-8Jm1qXw_c5t7QROBxAg02RiFwLoR6yQL9qwYWtKPmXgs2AMDjYbjQzjvU-QgwWpyMtr03k6tptKbzXRMdFLI0gXi1vQMzsHunH8V5IvOecny5d-plp_J6YofntItmxTZdh9ynoIy6zCioFiZV8X-80M8RvMm5rCmtEYykH9Ucaqlz7s4AheKzZn6iS4LmlKDe4G-e2HVmDVcAZ2rGPfLJtnzmEwsMfZolF74anuO462lVFwDgoAVszKlmJ7lmf60o0YUE-9BpG6opaXrM4-QpqQEyHyoX65hOgs8XzDcK1F_tAYykYX4jDDamBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_cGA5EC6fNsiEC6Qt-xtpJczXqgLl8Lnx6RdJyKz4MnkXVWkSCaEXKM7EVEWs9jJ0osaSIxqXaTnlWSzmKlrON8p3NO6fIhgCgIjT_F4Qgs2ENSbz6hyFRmmMBgpivZZT8MPTuGkiGGgsOjXqLfIPYNwqeB-qaLI6Vs-jy2sEi35_z7YYhXnje-aJ1DRw7vkORdCuIzM3oRmsK7yWE2SaiAC-wvXzYRU_VOeVJNM7eM688R5AZo-Y72eYybcOqJcVSMygucWGIK3IVYQxKqlROcnsg7b4Siin6BYt96LfX3_aoMYPIqn-NAdAFeSrDVdkqbfD12T5qw2Q62z1qllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=gVWPXJSDehIUvFzo66Z1Ik3gjlSeHz6H6tpScPffSNJuyo-3yNi5Y7f4cQVLZ73VyEZWd6AXl1Gzfc6rCRAcAYGF2o25xZeYmFKW2RoLi5lZYpU040PZJOL6a5hajYKtf51R1yPSlZCpFSB0DtTqO-ojD5eiLHzg7VdRXo4DrtaaLNeM0ej_YcQjTfQYllcUkO4lSijhnWzT7JjaO8s2hPQFgpH8vP2qSvRMp_2iStLt0nD9eCfqa2_fgh6OxzDy2DwP39tQBKQFhD07RB9Acm3RoxFHgmT1AZfT56-kXGUq_u2Z0ebzpSPQzu8HGqh3pkge34UID06mQhIwuCoDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=gVWPXJSDehIUvFzo66Z1Ik3gjlSeHz6H6tpScPffSNJuyo-3yNi5Y7f4cQVLZ73VyEZWd6AXl1Gzfc6rCRAcAYGF2o25xZeYmFKW2RoLi5lZYpU040PZJOL6a5hajYKtf51R1yPSlZCpFSB0DtTqO-ojD5eiLHzg7VdRXo4DrtaaLNeM0ej_YcQjTfQYllcUkO4lSijhnWzT7JjaO8s2hPQFgpH8vP2qSvRMp_2iStLt0nD9eCfqa2_fgh6OxzDy2DwP39tQBKQFhD07RB9Acm3RoxFHgmT1AZfT56-kXGUq_u2Z0ebzpSPQzu8HGqh3pkge34UID06mQhIwuCoDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=EyT_SoeODX6M9dbgPDppUXaIuIMiPvEJAdDf8g60eJ2NHInNJ1oV9W-xJ3GBWNI9hE6NnIrQL7Pss2mItcrTWfhXd-dxUgC8uq4l6n7oA8LQLW47cfSztJkEySynMyD2EKw5-YmVqZKZjTMFr0We-AK6wH1syTlV3BGjvTuDfK-IkosjQImpl-5_QiVQ-1nIuJrmnF-aj0b-KIUphqB2QR91IHBAzm_jQuHn67g2ZB4rGEsNmJnvIvAg9l7h5q2-XnHIELyYqqQ1Iwjt0g-3H3ZoApJy8xDovXgf-pCjKfeCH9l9oKq06qHI70ArlOz-fneDCQjg9zvfqOUCM7M1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=EyT_SoeODX6M9dbgPDppUXaIuIMiPvEJAdDf8g60eJ2NHInNJ1oV9W-xJ3GBWNI9hE6NnIrQL7Pss2mItcrTWfhXd-dxUgC8uq4l6n7oA8LQLW47cfSztJkEySynMyD2EKw5-YmVqZKZjTMFr0We-AK6wH1syTlV3BGjvTuDfK-IkosjQImpl-5_QiVQ-1nIuJrmnF-aj0b-KIUphqB2QR91IHBAzm_jQuHn67g2ZB4rGEsNmJnvIvAg9l7h5q2-XnHIELyYqqQ1Iwjt0g-3H3ZoApJy8xDovXgf-pCjKfeCH9l9oKq06qHI70ArlOz-fneDCQjg9zvfqOUCM7M1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22908">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC4koS21ZBv-LAdE1aLVbWjQOm4y-6D1U8jz7W-9aHS55iGfSsEhuFOuyKZolARqbXuCVcBgLI5HhSg4eVRB7EO9TKjm2yvogMCwbvT6ml-hCr1iHkb7f2zoNCBzWdj4anzURSiRKcAtXN-7W4_xXVy_sODNWUVMFp4HTkS-YcK562VDlCHpzvOiBHOnL5A0AHKtKIcmQDoHGapUMXyja76JvVAlFKQIaz-rfvaox7-yABd7wgP8B9ds1WagbxxTCGeew0yUjws2uR182tVJLFDuLjMVqGSBG4vOqmA8rUkST00BddEG5UX0pNbI7VAiDOp3RApF1uCOz6RIq-MUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌از مسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e16:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22908" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=kiRhr7cs0u-e-IypNX1shV8rmJxEoiMVlu_-ufdXLUg6o-nPnEIK4zzEmcFyFU5IDZfr2pC8eH6Xsw_UuKiDKNcN_tT-wAvodlUSIyBQa3krmccOp575wO6RIdAt-1aQTZVm2nXbpPO9-ZPxKaFhT67V3J49wJcTAbKheOPlhtBC5k3MYRH_1d2zNOW4R2jGateKFZWp3rfALnpDrJRXXOEjYRjuP4bTwJzqD0hTAXjL3lllJmWFvC1yHJ591DuTJGyxWAIXigNTvl07jur3NsbJMP_uA3qTU48qdyzZcGh4IB52G5ZIWPQcFUjP-JK_ohm5BemB9woVWJ3wNeovEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=kiRhr7cs0u-e-IypNX1shV8rmJxEoiMVlu_-ufdXLUg6o-nPnEIK4zzEmcFyFU5IDZfr2pC8eH6Xsw_UuKiDKNcN_tT-wAvodlUSIyBQa3krmccOp575wO6RIdAt-1aQTZVm2nXbpPO9-ZPxKaFhT67V3J49wJcTAbKheOPlhtBC5k3MYRH_1d2zNOW4R2jGateKFZWp3rfALnpDrJRXXOEjYRjuP4bTwJzqD0hTAXjL3lllJmWFvC1yHJ591DuTJGyxWAIXigNTvl07jur3NsbJMP_uA3qTU48qdyzZcGh4IB52G5ZIWPQcFUjP-JK_ohm5BemB9woVWJ3wNeovEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtB1zB68hpxpTBnZKUp5x-vIzcV16x-5mY0ZkcapYPDOAqPC3rkj17NI9WhOKupnFt2we3wSseISKmfQIgnUQ89u2MMvY94wYOFwSjMj0zMWc5YuQQ11mRzhpH975mI473nyZz1NbYx2I3dbDicPNO963_-zlxGjp1WcDmmBtdu7iO1qDmRcVK35Gl1u5VbD563aHPS8IXcXaoKkoLEWEhQiwXbtc8QtwftbPpjF65kNcjENzfa4Kg4sbPV_GrVXs28-qy-uZw0MJlrKkrLE9k7oJraNQGZyLK1s6u_MTxikNKl--TVDwii5hZeaolf7aipYKoe5pOC7bJHJhFtjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTp3zPjiS3VyQvtgOBj5NLyIZZ7QRA2dgmk2lakvx2HQuS484AnF-p43pBc3tlNZyrlAmyYmpm1jDByRmtj9ImxJ_KMH3uby33g659ZwxxNvrw4d9Hdv5fKC2s7Nxgn-AtsYV-ThyiI1zOEgb5oukzpINyuEof_FKscekM_tMhSkSnM-OvAjE8PYX9dDBStTair7ObE2NhbDpL0rczi3mFMLHLobqP3Ff79ArB-DYr_YIqqtWVJRy37gTGrEM-9yKL-xv_DFU6oTYUd1usp3cfFrQolh1j1_fPgMmA0zuxjaXJX4FVVKC4VoDlio7dJkgtgCZUBAghkGnWFw0xTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhsJtp8HlHJ2ayvkDCnPaLqnzk_MHpLPjJNujYbIiRDJPcPpiAQ8yW_HCvDDRSNxgP9MsMXKpZPoygZqNM6KndasVVFSXT01jHY9yeFOGk8DexVZV-LvzGvwXOHv7BOxqkAMK4yYKQwNaXwoU9CYtEFjifjTVcx47zyjyJtqJd3_wGNvzoRTolxwsujrteXVXhz-g9GaAg9yWEJnkhQKfTzAJnVD8s8Jm0XUYxxvqD__hPpsKJK3lb3eJl3LVsg_N_5ALsGZGdr5gD6PR0kDBq1PGKDHtaW1Pj0yHS-fLjSZlWDyB7oelgnUD_-zbC7Hu_K6NmGf640PA84qnUfQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBfsvKoly6_bLn28_7FiU2WZCEzBKrRzr29k6HoMkNjQDUcrpsM_xG5kMFkCs55BrocHlF-BlGW5MQX4HmJn239q7nNWG82GGvrevsCpYeMz4leZgdZGepXnJhtGAbZUyvzqo9-Qg8B_5y1PuArYukdOEGK-vmzMTg3rHDH9PS09t1G7qpFyDm-KuFITNUJrIvwfnw8Ar8Nv3U3ybTk2RRitXWnWr2juG3M7PSDsdqRkdC975wiHItBEetgY3NaDcn9JyviKLHDpk6ULfpYOwY0qxSauzqVZB0rOiA6EzYK5S6Yr5ekH8caZuOUdLZk8F93_GvtENBZANtfjO9JYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7PQgrnq4H4LpvVi6UB4i3nHDdE3H0Fff2htHfgdngA8HpVi6C0zzMtwE35EM9nKLZA9q0RA6kF_FV4gatX4QMlDg4Rdgj6kCTEBnPKcGUI7_kkOleClRCWaZSGPCbrdGhCYbqMxHnyqGMAxf_mIZsxolRNP_n5cYmUs0hKXFpTZZ2V0en9FEazpJ1C7RI4WUrQC1NObH3sZoQdVxIbh408i5zPHLgIXzxo_-WYCBS7PQVyvEoihTW2r5YODe3tx5wrOAYl6edpotJqGHaUxuaiFyZigxwqdaKuI09tTRJTijxQqzOBa5urdFHDYAXmjizLX3NMoLC-gHdCMqWMmzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSAeiqmRDWubKHCtpghixLQIz_veQ4FEuccDxi4Y8rfgiCXcsJvrd07LrQkC1BdowBN4Ube28re3Rlc7ddRml4gCBb3Y1zomIH4e_0PrDk68A--yi3Fk5ABmb-VjlyxdZ_MTHhKun291k6uoKs-EMvKtA9aQVCh1EMxLXNXKfZHAqhqlsJU6HRw6x_5IvzD9GxYCDkpz1szYNO2enrbbczSI2mbFS8JbcpxY_0lDXbiwKomscqp_1A_2UFCyNzEf1Ey5atQGJ-hnPsG3Up772wFj3Cwdh81CirJQAwRqeXv33SncwnJ0Om_7G-dQ3h4e51PetYTrfa2m2Tnn06i5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDcjEtjTflPuTBoFKo6EBeWO7_TDG5NDKK8kglSccSpxIfoU6OsQXHrC5roEPlFK8kNmUOYvAulwQTO9mRdnO-R59_JG9DT_GZMPlyXEu_nXPG4skK-a9aZ3rgGqumnUaCpbgeos4P8-vbDbPu2RlAIRTy8qekdM0t-G3EaEh6QCkiOxJQWCCAQuDrQ05-ukdOi-_fydUymF7wk0dIgOc78SUlhdTHp8OlyXJnxdBQUcONUzBTgB429GwgIQuoOw1SVCmHFR2_W4URRZvlorkqu_HzW46qK8d_p0t7wda65ZKAgVh4VKDJnhWtHVM3dfjTXbxwnwqP85LT9OvKp6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBQ7IFImwswuiMZKWw6SQLoFj2a8hD2TqnCvVZ_VEdF6K3e-iGDwtJYEMevV8DWcJlSeb9bvaxhnFS-Vvps3gwUkvueUaCEIH_EcYtJvJtuW39F7aUiaT9FNjKp8-VM4BNPRv9Y4IAoYuXrU041rRnvQ_aQLQdeDyhoZnxFly6bZSEsesd6JZtogvQZBy1ZHpFW0-tWqlJFTiflr1yxDTikSyft7ivGZ1GCc7_51c2AS6O1I36I67t1-6FjO7NptpfYr6SENI0_YAWjocpVMZ97FGQIzDtnTfQbOFbv1QCqQGmI-EeWOkpkg8n3b5wo6NUbZmpAUK8KlDT1gQMQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=Ux6DEyXiSZg1nnorePiCtXeVSNPndQFuO3jQtMvY6v_GKtw2VbvvkKvC2fa2igqGgpN9qZZbyOxnfH32ozDIlM3jpi0omYuPpFJ7J4MUa9qHCMJFJtfK-DIYdxlOdMl2a-P4z7Y8ydXJIC-OF1ZtdbfFHMYt_zFmxY-YpmSRkSf2VqU9fW6ClL7boIYFdKsjXsc6kQaFTYYAkx-arEIMjDzUYBVh38_VMWAadWy5QDjOatmkijeVXpBXJyXsz0ZAbGfEzGMliLKn00D4AXMgZxMZzFm8AqyVyEtxJHcHz-THBf1MK_RcO80Flq7TCQjjmIKh04w8DaC7Ar3u6Ued6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=Ux6DEyXiSZg1nnorePiCtXeVSNPndQFuO3jQtMvY6v_GKtw2VbvvkKvC2fa2igqGgpN9qZZbyOxnfH32ozDIlM3jpi0omYuPpFJ7J4MUa9qHCMJFJtfK-DIYdxlOdMl2a-P4z7Y8ydXJIC-OF1ZtdbfFHMYt_zFmxY-YpmSRkSf2VqU9fW6ClL7boIYFdKsjXsc6kQaFTYYAkx-arEIMjDzUYBVh38_VMWAadWy5QDjOatmkijeVXpBXJyXsz0ZAbGfEzGMliLKn00D4AXMgZxMZzFm8AqyVyEtxJHcHz-THBf1MK_RcO80Flq7TCQjjmIKh04w8DaC7Ar3u6Ued6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZn8I9yTAuKXWI-l0YUXfAus01I95Wh84w49JhZnVBSEcct8WFnI2qQjlMtmpspoACCaaSgmW6xFHW0zZjiBwSjTy9nlzyThYEB8IEXvuuuBw0bCUGtjYPlQv_-Exo4-cFz2LcSttg2GmqNsk31kqZLd9hISI1kfnA3pP2dip0lQJu8PVk9khN6YoasLfZjHId9BcNFRC-6CkZlx4f93OZAjRvhdGq2YTz9zsFUWoan_TT77IyCyTibL9uhvTm17OekwaPIiWEXbhsQJdsk3LvyR9P8jhH0rBjVq7l0WZWqWm1dPVRi99Z3FIHMORDmvXGJD_5kFjwMU2XXmU_JLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnJd1XxBkjbgBWIDQn3PZRrwELIEvv-cRgmq5hGXqWJhjKn0xjYM4qqXJ16kjKZ8Feim5rISj9kDClowpXr8BWaO0danU_yR_tBOb-URd-5jLPX0Y93w6MnTANGwATn8sin03adfKJEDGtcjU-GsjTT8BU7Xk-jY24j86XMWDq3vZU4-y11zRHaAxpvCQ-GteH-0OMIGrgj9HUWrGwLtOIcBvS4b1IGPNi8-a78VFEAuGJziPj4oQBbTWQD14nmlPG6aCvwafGMlrOCtYt4miwAOQD4xBlTEaEAqWjiD-jBn3dSgTie7fHclgnXPL2m2d1Bg9ObQ-CQDU-rS-3uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=M3Ln5cidRHBbERdA9WFn5uWlHhivlpgZkFa5x_szcxSdZXnK6p2wB_xfxrkUuxAgeiyB3Wo9l19YlRaRcyJkymfUhd3jQVehuQmh2HIrg2PajOy44S_KVyuUTvpSxtD_K-zNGVMmcXrB7itmT1rkqX4JmczLACmlpstpSvKBe4eznWPYVB8j6KbgUYEjkomkiEU0SlT3Iw2EmcvgKw8OtFZrK5-xforA-rfRK8eFB4tjQzF0rfDuGci741pz4LF9WgvjI9MRWtte10Pt8El9485NdvVKH9VG_4IIXhIr9fytQV8bvF_cr3VPlMGil6vHf2NrOZiAAybq-xUaKZqIdZ9PJBmWO8kjlwI-79gdoK0UXQAHg60wclEVNsYCThBPo-yJdxAC2ccN1opji2VnDjx38tg4hCoVyyWhnDGUp9F2Q_XEc9ObUtfIs46Y9j-NpUHYdtb7zwASzksmVqk_-vh7K7wjhEIpTVJ5PNFXslbb_UXIaSBoMnqE4MHGmSRxBEhOVeyNeJZ_lYOZtc2nlOEeONcVnoda6i1cZWRStDCOTQBbCdiOadXFOerY89XXaabd5Q44oq_Z3yx3NY_bGXzBSR0xxFSgxv0Yt6MkN7DJLYxNLepd09wPSE9xi8VUlxuwL2TW04b1esKUsCmMB7sart0fiucnxbXF3xBpgfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=M3Ln5cidRHBbERdA9WFn5uWlHhivlpgZkFa5x_szcxSdZXnK6p2wB_xfxrkUuxAgeiyB3Wo9l19YlRaRcyJkymfUhd3jQVehuQmh2HIrg2PajOy44S_KVyuUTvpSxtD_K-zNGVMmcXrB7itmT1rkqX4JmczLACmlpstpSvKBe4eznWPYVB8j6KbgUYEjkomkiEU0SlT3Iw2EmcvgKw8OtFZrK5-xforA-rfRK8eFB4tjQzF0rfDuGci741pz4LF9WgvjI9MRWtte10Pt8El9485NdvVKH9VG_4IIXhIr9fytQV8bvF_cr3VPlMGil6vHf2NrOZiAAybq-xUaKZqIdZ9PJBmWO8kjlwI-79gdoK0UXQAHg60wclEVNsYCThBPo-yJdxAC2ccN1opji2VnDjx38tg4hCoVyyWhnDGUp9F2Q_XEc9ObUtfIs46Y9j-NpUHYdtb7zwASzksmVqk_-vh7K7wjhEIpTVJ5PNFXslbb_UXIaSBoMnqE4MHGmSRxBEhOVeyNeJZ_lYOZtc2nlOEeONcVnoda6i1cZWRStDCOTQBbCdiOadXFOerY89XXaabd5Q44oq_Z3yx3NY_bGXzBSR0xxFSgxv0Yt6MkN7DJLYxNLepd09wPSE9xi8VUlxuwL2TW04b1esKUsCmMB7sart0fiucnxbXF3xBpgfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWHnOLi99ZPVEt9JnxVZD9aSZf8NG8jwCB6p4lqix7uyXRq1IibzFmx21QZ76qBpZhxmJHNZGYSfGLVWMR1Q8PWneblZCvZHYKR0yup2n3Lo8NRkf5_xQeZStKi4Wn1i-Yjs5SMUELrJmmseXCk3eLFWgnJrRN4nSE16UEeHc68zL4kLnV7oU1CO6fQ1E_s0mFWLYoN6FAwv4pJTZWOVXwEj7aLN76p3DK8CkH3uXT7CaKCqPBxnScZ2sIxeLuqJ05U2x9yeViXqjVLc3fRC4W5h4O18lXG1m0V2F9O8RCNkaZICl_63bjPpUAIsYM5TMxrsLcWF6ISqr2ySC2b7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRA47l1wWbczRPUquI-zCnK1mQwugzW732wHJKDaXt0bmvQYMjCdL5HzcbjLXgc6rSap87JTSKD6d6XcaZV32TQfXSqGYzVdI-glSWLyzeF-a3PSPcYBZWAq_hPVK8WbtbFv1-3u92bS1_hy7KDB0fvtsr5Rq1mZYjxLZg0Bd7ssy5czbLrdCWhKAJX97kVL99K41FdWCAJi-xO07PdbugasY20EG6Un0MgYgFk7zJzJlztexZlfKL3RF7H7pL1rMjqjsupOyBO5Vr_S4NxXH47Gi0IUt9MKnD_ztSwvD71Z3B7uZol2u4PxzZpl3mNZtDb1sKsTwwtwxtn9yGvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpwVgp9s1ofl4lYsp2EkBJz_jUA6zif5n_iZj3jfgHnKx0QyQX1WD3iY-YGyW9mE1fv1-fL68VYdkIkuOMOSKhnFYqzTihR4MfNH46kjYxPCCBp34vogzvA-GG41G6EBKsOhoHcOM5IMOuahnCDCcBNdTcquBpxSQ4ca13b2ZDFmwAungKbKCMgGfNmGBygHiNGtSebi5pFU6G0oKbIdeHT8uIp4uVSOSw9yz8tB6vyNn9d38pqNzGWvKWUkJCL-u6kCju72oC1aomW-fXLeGOB-4I8_kcCIptYnMdXrzGqPYdMlsJvcd0-W84qFzm1IGT8dWDhDfR8MUiG-UEFRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDNB4M1cbdq65D57DNSKXkhubEMMR51D35MjrnSvpe3ouHgYqKDrr1YNSWHnxc603v1GtsClf4YlSgRIICJ0QZhz22OVAMOpVzha28Xu7PTa719jEf8wJCDyBJXTrMqltVlZnKFXgMWQqpzEJ9tUEY0bkWmBZRnGVhAGTQbHaF7EludJWocdbq-ght9207gC0NK7mUMWzvvf25AhfXNMej3gKvRQwbNqK65137a7n6RYn4RbNmVF5XFZK5Z2Tnbq7y7m5c9tLkHu-GYSoksnDLYtTCrewdPfNXgTbbp0mex6QsIRLOXA-Ikbp_1E7iYAY7WWgme_Cm1D3whcbd6bhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej23QF5MfeA6CJPNGUhPCrUNMsRhyAfOy-4IFbIQ9aetVkCPi_Ro_HG1l5Nqy1awhvZ1OyIP5HQvd4jUUHjNwOAWuT3KMc1vw8PKRRv_-dGGq-qByVDpTDrEIOuIqNpJellhfL1hKVbbDsCks7Ctms-fE_7w5ofKGvBOo0WkYBqEpYqxgbAa6jsMNuWgB-hBuuWwm6UHV2-InWTkN8dU3emtirOeahHJ1uIF1_ceHHCX9jJsUVVis1NbWN7WWQ5HdMop0DbVedXfS9FBULO8yltr_K-_-Td-f8Q1VK6RRNnrbiVgpBfy9fsqaY-tgczbMM2i5XDUvx8o_MBsPyaEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRARahkgY5wpPf7qKrNgEAE0CqxEHndl_j9I5OdkcH2sy9XHoEEN2qwdcsYoMtDN7D_TJiDGKC33gOLikfJnlVriuhevu0riUUJUsCb-YnbRaPNU0iut65Gme7kbed2PUE5HPzOwvaZjd9_GPf5Ixf9eSfAoazLmNUa2H78fAiau1tbl0sUAe6iJw6awnYrd_P-7qTmPyYWKumfbab4qDUp4IWoQedSRYv8Fw-nJL4S7ZNHghDsJXw5k5K9qn1R8SoCJStNLnU2NASUY9SjhGDFYx-KqPHeTChSJZlqdZodn_E3hmHmQ153Ax9wP_qa4wtOGGcyb8ydUIN9zqqwCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeFm4WApxBatFFsWjst2Rj_rhrw2sML-cYAuG2VJr_V6l2A1XRkxP85qymxgNx6NF8I5Uvf-1loeVifvOoYk2zDSrtfM_zfByq8xT-rnODNZ8hDtI1rGprfwPqFUu9XDpQNZZuvWKHqwjDXOfGYt37agBkSeePCSTTNuLDd3pl3B433JHTwJolntPACzmtkaJ2GiVQQBdAQ7NzuEqdOowp_K8PoJ0vfLakA7SKyPtnyjIYk0YkYdp55TabUGt0WF2Mb9k2KzVHXnMAvkXYLO-TCYhZErWWBoif5CIBW9yOqobla7JBbUshclt5kaEQHRmOAD2tmhrtKJSrws6PKsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxXLxpKjIr6JsZXuXxRXHE7xM3D2HR9BAZewxV-zPvfKelY0uPpXUZFwcZEB8-LxXhokslnae-XXtmDXCsIqcXcdl1Jutb2M5bDteTUQn0O33ELwJqK3dGP9Enr5J8bmFj7_j1nfnsDDdRp3KdUAc-KTouAij5K7rKYOa86uXuHqCIyji-bgn12_K4bt7GdMZBj47masx_Ypi7w_KLDj3goIOi7PN_4zhr7w-w9ggm88VRf03j8zbR-Xj5TYqhUw_s5y00gHQxd6M_SraJ1UsbRq7_yi6b9CDMwZpCZaH1NDm3s1cn-FPPriiRZZbidxv_-7IJmsEYEyZ3iIt8O2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOu3geg7z9AA-p2sbfvpD-5ciYWvvemdsa_iFsVPdefjgVKMO0fHBJ-JgAcE9ocDQhnSWM4AQxqdS3cniagglg2kW5u2U_VGiyH-Ntb7H3JBjDut9DsMl9eAVv-HupplUd0IvISO4A4UbAcwlZWbKUNIITmRhKF4hXmiL2zbFLwq55jdXcIMywf_Tap9NaQ9t63pt5_J--Fpm9-vTzZjyoXRj-jEDEr2FR6u1rS3va2GqG6urMbG9fXIjAiwBRsBtXLhltI8w0bposiaa6f5N8FJj2zueBWvSblTEuLN-o9ThlN41BtGZrGq8CaI-QEXA_sb_GOL1jvLn7HcjIxmHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMjTjbUzpVCnqlF4IfKjEttCk6vPF2PDCJoS7_ZiNj7XYZoSj0bJvB79RxBC8UiPUV3maDjrqLxkqWJRHLOeR0aEbS0F0s9QpcogyoqRRL9AQz7JK3gtgj1Ai5JrQVaMmrrVBaJBM3U46amWtfyxcR2BUo3OWS8B9GaHMlrlmpgE_bLwvHjn_LwDc_ED4eNhgRvhEFLtclybROrSWZoztyXEW0fhx_kvWYxhjyHKlpB0gWny9FSNIfS0nU1SMVFvLRAiHDnlamhQ6EX5bZbQJXaFvX8LFFpKWhhp_Nmc0S3-1Otel79d71aYYB-_8ehyg8MF8MSEbgG8Gn-NvaXyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVG-EMJSlX5ipmAZ2aUsIry-foZ9aihKXh1uKhmZtRSwRCSD-Lgphx69AZBx0iAAySZFoRTJBJansx3z4HQMLpSuDahDeUNs5HkKFk5jgn3vX2IZtjJzsB9ZrrutR6FG7iIgz57kHTMUUog45kmjilftLWOBgLg_Zr-GSyFlN1fgN7T5OFZWI-sPs9J-_qKZ6jIDvkWdjpG1nf81QBYwm_aX4UCuPGBEX1CKECPZIJ50iUpG7gKiiY0aP1noI9GcdAucF3s7sVFMVIv56pddu7s_g2YDAdShTMN5MTMOfxuNM3j7u85pMQuSzLS6GbM5lHf0Ya6ErhCyVQKeOy5Ukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUftcz-u2KtdY9eaE4WCicCNJxMBLPDjHyfJEWonHVqfyeD6xsjW_eBGtqgCN4-ZZLMTLL4FUbAE9lesxnZ9Ne36MAe5Tdi2IwSseAtKCaQzoM2k0ENsVaoueFAVmFCHfpPdsaC665oHZTFwsTACzwp5Wn-GAZIQ23u3DbilBBrOprkCgP0Y1mRPaGmHi85sJ9ramVvboRsS8-sV2Ey0XH1uBo8r1FURegf0YE4Pm6_ICCrlzFw11E7mvmk6FhyaBo-eJ8BV-NoDDwUFn_M3eu5uUkpqoVxq3bF7qoXy-iUpkNSWZ8h03nZvk7UQT3-Y9JIJBLR5zDVAPb2lQvP04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk3m3TnhFJMsjl9e3iq_xIZxax19w_pQyU5u_mOABRPLiHHF6bnao-ewF_NMlhOYYOjCZBCU_CKOMKwNdF25xdhX8c8Fu2vzbKERFiqszTFSqUbfAemnGVqu0bl0_CBzuRB8g6bOvWFauqdUTGFyA7oFrPdke1JjRm_DmEmXbj7UtFftNSXpyqRw8835-eLFGNq9nWd08gN61YtIk05dKReJSsf4w0Tr4dFbRNa9yWZwr2VV_V-7QLImBdi28GkCNJFK7ddHvybUOLIsxFoNbYYg6kCg4jCRVfHun3fvWtQJUUSGf8JDgZfUs-FtumXuHblHcDMuSyDxENYzRezu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnocLudYF9_-27RTkwGR00KqGKFndPsYfF5R_pyIMk3dR2T4Inhk209FEeLvFoHFF5YgPER4svRf6GRsJ4R6zdVa3BM_P04kwW60pyWgzQIdyOPSeypDxVH-6YNNwet7Fu0ULTB-ev0rhSXBkXkC2dD-fTBqtAtgTzuJF7Z9gvYNCu84lRde9IwHa1xevL0PdrA9IK9mmMFq_s0DTMJxQEnZ5cZrFnw5aQTuhArNLM-CsqEhPionHmqrmpY6MJPXn5ZJXrvkKEu80zRkm983x2GBNJp5I22tFXuaFvum6Fdo8Th9sdppG7Mztz-ihMZVr-I7BEmPI4J76gtXk9OeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKhkeMU-mIBO7moMBdnz4FPj-q1qqkEEDEFCeXqW08u_J4F-7Xnly37S5jwvvGuDZJd3TuU2znM9611WDDpfUsm6vMrqMJhSV-PcpgSoGUdRuQUUQ2W42GZRCimIS4eAisjmuAPT_QHs5l8LcsgWygLbOlYqKDy8Vg_FA4HysA4FHOpfYjrQ5OoEUl6lRFQGdrTi1GDdI3aXt9AIdp2Fr6lMILuZ-H-5ZZQSN3JrW3EhanINkgrym7345yuAX3keI4AzjCXXXh57SP2IIl6Mpp66fC2mMHbwiYshY2-VdO0mEieTN9oI7rzeQw9iPnyq1mgJX21kzwtLEUSKExy37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDm7KlIx7kZ5UpvEvFpoeRM_6kFVzK6d-LKdG3KrnCN5jTLWWh-a9Mm-lXy_u3ZFx60S_7SHzfukhPcb7XuuAPHCtPjsBvF8rd9oN2RJCPoPL1ZgqwNixsD97DGNgGtLTVwi6FHef3LfE3qm_JwQZFuR9TDAL8AYOe92zCjMxnwZNXzVGwW1bco1TCv9etf272_1_3KDF1gF6HOu9r0DtVSpxUsKROYTOvIgFlSdma1GWXpcweNSnL9D61VGJBtsHWsjTh4wRr12NcmB8HS26yQcoStSz0Vw9aY4qWP9X_dRNzdk9IHTIVQRZd4M2V2xlqWjed7mNtWru172iSZkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzu3HO5QE71X51sg_88tqV-xbQ83YPlc2mqldQdbr4IT0VY7zZtQoTXOwt66eNpNHxLEjUYH_aPicXnG1ILMHI4PailkZUTvOJ3xg_S6QqrZjWEeSZJmYcVG69JrvY1Fd3nbF6xaSPpWKAmu27nEqP0CZZ_U4tIWI6sjUWKM16ra4JEFEOz_oRPceZiHM1nYCWCtwfNU7oKOGkcZJlexzZgZnwt4pJ_zWJTj_nScZ6QTuFR17nezhvy4tZIGbkAWjOYhU7HoszpwVPGprAhXQoBYpy6dQNguH6Um-qxPV2C69evrVdayRbfKZIdLCFG0tKayTeS9-gOCrgL2ZsDvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=qzOurtlhV2owX7nRJeXSENqIppWfdZ67j2VIokLQO8T2r1gYU-yQrvz8K-REwRs8hsMPPtTUtqBMakNsrxg9E8jGcWa-o5w2-ky_zoPd1LFSXyJ2U-xw01EfO3QjGZf8LPCy-57NSo0FMdLsX3pGkyJWLTP_i1CscGoXZFi5HEuZ51xp7sqUUvdoFeJ8lTSdOuBzm6FWHANr3cAhXrKujeTjktcIl5PA6pnYPGhRYskMzJU2e8WQ7wyoqsk1UKfC4sdJgRUd2Z6Wi-C34EZTDy6He8jVO_4ke5v9AqZBEPpEjErAjHNN8PM0KoOW4XSKNz0qx0Dci_Sbs1E4CgfatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=qzOurtlhV2owX7nRJeXSENqIppWfdZ67j2VIokLQO8T2r1gYU-yQrvz8K-REwRs8hsMPPtTUtqBMakNsrxg9E8jGcWa-o5w2-ky_zoPd1LFSXyJ2U-xw01EfO3QjGZf8LPCy-57NSo0FMdLsX3pGkyJWLTP_i1CscGoXZFi5HEuZ51xp7sqUUvdoFeJ8lTSdOuBzm6FWHANr3cAhXrKujeTjktcIl5PA6pnYPGhRYskMzJU2e8WQ7wyoqsk1UKfC4sdJgRUd2Z6Wi-C34EZTDy6He8jVO_4ke5v9AqZBEPpEjErAjHNN8PM0KoOW4XSKNz0qx0Dci_Sbs1E4CgfatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=e3DA9AZXbfHiNHPVKYQszj5pJpao73u5oVIFnugXMTnp3cAvyjRO8dD2sCqJoNg9AipXxYwEv1kyCuGRrv-Idz38_GaEv5nn8KoAiZOt0HPgcCfeO2LoJNiK1d1V4rphBWk4yippCln_PrScsheAj65ULi133cpWtmF-Xuxf2i_y8ByG2Iq_0UXSq-wHsnil3V9t6u0ELBQksCHVwWNtVq_DIjaF8L72ctjxA-NYSK0mo2tSmaBcZdvwO854i4jtLR5Pzh3YAYNSV8BYcT-YTWGzUAAy2DV_7sycMhSjVZ-hoVfrsTQGNQLcMBG8OAZ2d69B2UxwZo7nMQobnjYNAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=e3DA9AZXbfHiNHPVKYQszj5pJpao73u5oVIFnugXMTnp3cAvyjRO8dD2sCqJoNg9AipXxYwEv1kyCuGRrv-Idz38_GaEv5nn8KoAiZOt0HPgcCfeO2LoJNiK1d1V4rphBWk4yippCln_PrScsheAj65ULi133cpWtmF-Xuxf2i_y8ByG2Iq_0UXSq-wHsnil3V9t6u0ELBQksCHVwWNtVq_DIjaF8L72ctjxA-NYSK0mo2tSmaBcZdvwO854i4jtLR5Pzh3YAYNSV8BYcT-YTWGzUAAy2DV_7sycMhSjVZ-hoVfrsTQGNQLcMBG8OAZ2d69B2UxwZo7nMQobnjYNAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daM5PmacRI7BBIjtq9Av6_y1HnGw1Lh1dippcI5cMCAL-tH7xs1qTlxNzaNXKeYGzFHAGipE9IdSlRDjdtLygmw_naExzsfCinE4ypSwxA8S8j3160KLTGUyyc5vWmc-FM5XY5wFJ79AqwG9X7ccrgz_XbI8vc3nQJp78LJ9BWV4PUzZ7yNHgdzaEFp5987yrA6vOUHlKktvdzp3vTwIDCh_J6d6a_SRPBfUsnEXerwWIKTalUgrMDgjZAMM9On0zsdVOY0o8vPittY7oMzAQesNz54rdZOPEpL3XTl9W7-YKkuE0GW3SEBon0y82kBJYNvXTchN4Npc2k8u0J6pGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=SLSRFkneieMjMWR7n6LGWEVMR6j9FNsZOhF1AYRmEN5OfDh8dHRBPG4rF0-sa3TmBOY-uYtooik8SOS_Dt6Ff7boOA28sZrDwmXScw0Ld_iVi7OqynkGvQVmhc6XzObxKrjdwVwPzrqpeTPivUxRMWUkEzp_QbCwT7N-fbPgObFbmUUEmksvY0YAS6RC-lizR3Aw--XX3pq5P4Gl4L-bddDW2q0Ns2OL0y6BO4sior_TzN4IgvXbBlek3GZ4x4AqnODAFvG-MCpDGh-lYM5lK_tw4XtdLCEJ8L800dtejZ_sYlgnboeEy_9C2sLtd_uwZT9lhjBya2cw5yN5DKdQxSORBEDV30LzEAws1jYYOdm0Bs4T08lL3-_bUbJHdUT9hihVi2zBWq_IBH4R0eGXNKgpM1wvd_M6cC-MwfLhQrWjFZCfsSNb-P-zUskDt9n902LUd6aG-YQcLEvznxFTCu8SNFl46Qfw7d4vp16hhv6laNOyRx8Kh00VanrND-xIxrDFpOwLlcnxD2DV1itu8657RFDAg08g8jk7lc_a2UmCicO7P0TU_0CSUpF4gSFSrxJFAXkQuCGdbOWrL-pFeYvcm356vOsIBj1BY7YNportMIGj9myXg_AVztaDz4OkoUIIPhlEccigbTqJsCGQMlDW-cNweczfRqzDPm5lwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=SLSRFkneieMjMWR7n6LGWEVMR6j9FNsZOhF1AYRmEN5OfDh8dHRBPG4rF0-sa3TmBOY-uYtooik8SOS_Dt6Ff7boOA28sZrDwmXScw0Ld_iVi7OqynkGvQVmhc6XzObxKrjdwVwPzrqpeTPivUxRMWUkEzp_QbCwT7N-fbPgObFbmUUEmksvY0YAS6RC-lizR3Aw--XX3pq5P4Gl4L-bddDW2q0Ns2OL0y6BO4sior_TzN4IgvXbBlek3GZ4x4AqnODAFvG-MCpDGh-lYM5lK_tw4XtdLCEJ8L800dtejZ_sYlgnboeEy_9C2sLtd_uwZT9lhjBya2cw5yN5DKdQxSORBEDV30LzEAws1jYYOdm0Bs4T08lL3-_bUbJHdUT9hihVi2zBWq_IBH4R0eGXNKgpM1wvd_M6cC-MwfLhQrWjFZCfsSNb-P-zUskDt9n902LUd6aG-YQcLEvznxFTCu8SNFl46Qfw7d4vp16hhv6laNOyRx8Kh00VanrND-xIxrDFpOwLlcnxD2DV1itu8657RFDAg08g8jk7lc_a2UmCicO7P0TU_0CSUpF4gSFSrxJFAXkQuCGdbOWrL-pFeYvcm356vOsIBj1BY7YNportMIGj9myXg_AVztaDz4OkoUIIPhlEccigbTqJsCGQMlDW-cNweczfRqzDPm5lwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oD5xhj0BW_Efy_ac9NlBcoNQUJNjRV2A8KjFjwONn4Zj5jm7Wl52TnrY1okr6G_oah-aCoeCUH3oTiVQ3KXGzn9SZIOcXaDbUnkrQdGtlcPG4fioTSMuWnseE8AuRELvc5xc86Ogat-i4NYDc-yVipVQWaSctlvon76y5L_bEHVouf-lkHYAJbQlgCjRlylwH6847Ht6KnMJzjNyD6wQzP1CfgGjzhMENbk_Om6CfiWjvJur7Wn2Q_VVaVslOWIH-2XWdpI9kn2tWeAgzoCXHFFPn3EJGtI40iErEIAJYNUZS93Lv8S1Uml1Q-NSVocMwAhmTz2sW4L48CBy5yuPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpYTNoprhjdyLP7CmRzMWHW1U0xolGlCgByP_SwCVTD6w-Rm0uvA9MC2yMvc5hhfz7kSKMi1AkUzZdI10HmKPrhAc_BYdtHwye7EDLJYhzwEYsI5mP_0KZPlaNp3tLHTIPyREvaIcqHmzbo6-ZtKUI4on372Dw_ZwpOEV5PwuWqafNYE1j_U12C3JWkiEMYPv_ZoXXhHKQ5Nhrs4uZSizOHoit9-6C_QJvCOzasDF0Bf_a8t_GN3OTN8y4X2LjprInpW3D6wemOC7GHyW8YotDpmZNEqt6SJt6Zq1YGSFB4FNFmFE230pqC-xDU7mYIS3cnsLQ4lVBN6ItJ45nO--w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtwqovUmlpSBRQpytZsHDmfYudZt-YnpXIs7vtsMn-GNokyDBw6BS4SiDwKyCHDbFi-CZwG233xYGeRrJXHjIGUnL8Oyh3xtLhSpYVoP5X9x0_XxiTUIU3sRKu3Wbkyn8oewN_64Or3vHShHkDfgvMo-5aeluxEBDQIPriXCH4FWqSkCI0ktNUS2IWUN4TyduOQa2VsXLTUFVpPVtTvNCHPDiGfd3OPaqaEB-acRU4RCNeHCa3aFtn5SlgffGjcXI54aCm_ZHPHwSaUfUPxvtS69L7PGcMWxwPPF98m2s4GswGP11Y-TR-SyzBFJYmw140rehAkhdWNAgjmGz7jGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzi5CQk15i2-AD3llaOIcYHaNoRL0zJAn_KQ1s_y4ArLrkApglDDOWvsRAMV2xGidgsC_qL2Dr6r0BUhaE95KNG0gbeYeDKIj2FzdwR_EnpGfMk2hW6Ul1qbgpFeF-L2U_lH28wlOS3_I4oXhhH9CxWEu8HbrhR3tXaXkO5pysTDVpbV9P_KqexYBEcW3vP1o4DPancmO_y2qHkQpOHuJaPL9woEtLMtmyT_8FcrlOQD7YuEb4WWxF6bs0oeOtJDpbpGXBNPxDxwLD3UI2seSpJs5iCCvVbPMHvtHD76fg349Mv52m1eS2E_U4AQ6mxBTXUkvg7loGiRgt10a1G4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L29UgiIBXgcw9jMUFcJTG9r3IMLex4Z8E5DSfne3zSnrwXN__lIr1Fpyec0B4TNTPsvvVcEt5mR5-FYoL0qNXjaz4R9mZWYUS9B6aVYIigGdZ2ZwMtyumQZ92rWc8CtOUoyeysC73-OxhXNu2Wix4zIkjhXxLRoSs971T4DdcFWc8Nlxvp_pYhrIpleJrQ-iDvC0t3adLu1gAKtgs8j9ZB_CpQFWqIpJHfoZK2z7VUqfdHarjcvTstWzAtU3ZblwSc8G95chaowKzikBarBdsdnHb_FCjyLmjYbgr-xomjWu53uA69CYkea4xduaqCbBNkKjn6NlS0tZ0GqCZtpbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d58nxTeJkc4Ond8LpTYrOPrsCCLl16Rrmra9aAxn_wOuBn3wo1czZHbfIdUYCCoeqIAIuBDhrmQG-Cg6nfnUqY_0p0n9-w-uiQ3ctpDlywONntxSTxQm7rIEiOQwH5sLWPDqGH9rET2agnJuXy-kCcPl2aad-HieEvOcmffFevd4AdEeZSa87UmOVvG0X2ZSxTwU6QVjhFdMspNa90lFi0ZlYFYUx_i-eBXEUM-IYcBoe5X8DLeNu4ZJMbq15YfPJNpwzPdpNwL1s39nCrrLAUSsaco8Ghi54SBziuIQfiWx1QItWsYstikMeO0Ha8BRsKoIrVQ2rVFUmCrYUQZiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_noicZm6tv4JqHvvH-umf-SRoFvO0XjHMr9LDCho6TltGcNqb5pHv8ghlnuqXjdUgrDmU6HVAqC8SlUoUKgHEgTksU4KPXnVsioDqJJoVRVY1ERXvu0VoT2U7zAwx4CCn9-XeQIImtMN4_uEzFkcNHw-xss2LbnbRb9UfoU9_ex4Z6aVQZCuPgnoQQVhWrfbyyxn_Mv4AoU9_05Il192V1PXW9nirlq8m0e5IYNK5rm8qhYymSvMxZKnGiuvRUenXMh10lXQvH90u67NvcRN4WGSPm_wjBvo3TnDBV_sQl9YuVJQYMtBO94R1wSWKtS4nLeHDEd6TbAXmX4_lXj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=uR-sEy64y0WHJ1_8ndwd03Ne1-OIpZPXdX1CeCxa2rdIKK4BhBi_04Kt1JVbBfaNcC1L7dBKfROa9dM7PcK5FuyCVltOfUIKgWh0q5hfesBQIBWzu9ULQ6_ZFocd2QQBfkhBaUhZg3ZVEKk5V_WTPgXvVp2rKZMaxS8Xq0onWdMdKNxM7Igz8RofH6l8yuaqY_V9chycrLhHqT8qRGrgE2ABlEJYecpLlk64cmrK2ygxZZsN7DRxzZijq93BpundDF-_GPjBqw3SbLYPMgqTInWU2Y9nDYNCwW7qPrYQEqUp-dHHQQzPUhJp1bMWsVoV25_aauRLBjeB8Qm57xBqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=uR-sEy64y0WHJ1_8ndwd03Ne1-OIpZPXdX1CeCxa2rdIKK4BhBi_04Kt1JVbBfaNcC1L7dBKfROa9dM7PcK5FuyCVltOfUIKgWh0q5hfesBQIBWzu9ULQ6_ZFocd2QQBfkhBaUhZg3ZVEKk5V_WTPgXvVp2rKZMaxS8Xq0onWdMdKNxM7Igz8RofH6l8yuaqY_V9chycrLhHqT8qRGrgE2ABlEJYecpLlk64cmrK2ygxZZsN7DRxzZijq93BpundDF-_GPjBqw3SbLYPMgqTInWU2Y9nDYNCwW7qPrYQEqUp-dHHQQzPUhJp1bMWsVoV25_aauRLBjeB8Qm57xBqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4Dy8hRmWNl7lAgdzFupaSSm2wjPomog0OJKBwk4Ffco54mYZQnDMCLhClI3Z8_GZOju-CtTn2ePpVtBJO26U9JCw-aYQs54mSEPUjaWMvQjhTlZZSgHI_9HvmEIMEu0FOEVtP9i-X4YuuNRB3rIcA1keseLjMnsMQRgHli7NtX5NRvC7fIKCWizcz2-5mTTU3owPFVxN1xcD4AfQqY6kqgq9DhvAP5Go_6BcLj_c8GOsR4Tm9h64MIg4QsrlY2zCfTaSIhiRIHFtZ1U2WyklzFxBXm2RCAjTo0JJSB1nzZA0EJWUBUS10iJa5ONQmuDELMOzcm79kVHf5_zgguuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to1zWWqF9jvDh25rz4f8i4ZuxZYVaVu39qCehnhOP5LEZ3GTYxYwyEH9UuKjLzYq6RZ46PkxXhb8b7o7TF7RvxhNPPy3SO5sjDTsDs4p2S2d0sGd1xW9HYC8h3Vgdu23rhRNxSG02QtGBwnYOEKNDVR-PvE98et16qOqjd3f4Ehz0CTiGd_cBNiKtR_w5BufzeWdaUgPIrSlx1N7J_nc4KfV21vTrKPguWwBVHnJuPueI0C1ucagiFA-5KfL1NK80vycp65apZJ8YH0VTdJWv7wvJy0ByN5kfLAsQPlPIIx8fHjDmaf3Tu5IuXKtd1UGna8bGxD_TJJgdw8AEk9r_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=DLpAlkscdjvwoaIM_VY11PLswwp2NdyC3nzxD0e3mxJSDSflXiEQBW_kawTLu7inorwV-Anzzl0J72q2--sfvgiLb3NjHs_MRZ1RKznT8_R-B9MhBl0Y15HvvqyJsWWHK66HDYEYAtp7E4ooGAZn4OE3W3yc_VzfPYAQfoDp4j56aeVEbyJ35jPDCJXA45dCoEv9v7-kb2CfIeZq1UAVACWM2qBwZRG8GQEwhXmvaBLmmvjNMuDFSdZZ4ER9YZp2NX2EskjNLzLrH43-9bd3fUyydpn-8qMa8BlnA-QqgqGnuvLko7cCvH1LO5AaNSbZNx8gPLpPImNMsjZVMjfuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=DLpAlkscdjvwoaIM_VY11PLswwp2NdyC3nzxD0e3mxJSDSflXiEQBW_kawTLu7inorwV-Anzzl0J72q2--sfvgiLb3NjHs_MRZ1RKznT8_R-B9MhBl0Y15HvvqyJsWWHK66HDYEYAtp7E4ooGAZn4OE3W3yc_VzfPYAQfoDp4j56aeVEbyJ35jPDCJXA45dCoEv9v7-kb2CfIeZq1UAVACWM2qBwZRG8GQEwhXmvaBLmmvjNMuDFSdZZ4ER9YZp2NX2EskjNLzLrH43-9bd3fUyydpn-8qMa8BlnA-QqgqGnuvLko7cCvH1LO5AaNSbZNx8gPLpPImNMsjZVMjfuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=UMTN-QaMzjM7uJwLsKXg5SMmljywQyOeT31wprX-ElUv_HwQeyu_2wGkbpBLt2FAzNEfdjY3eOivTy5p0r8NJeQv01pBRgSjC5eYjYqFl2W2IP_tUi-G29o5g77n0-vNGO7EJxv3KASXypt9REnUO0b-GgE0pewHolnbFi8HjQZUDKpF8SYS22vIQqzzUKBVA19SINpW_mKvTXd67LM6ioRgnBUFO8BLQBeMUkRuBHu-T_HPZ58YzeleiYQUSlThGxvDxk2XhDhsX8a9GCpG2AtvCjRVmc_NfChvn3pjFT87MpNjEz70ymadP3lIZxnBIwTItueT_cEjjWz6d2QWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=UMTN-QaMzjM7uJwLsKXg5SMmljywQyOeT31wprX-ElUv_HwQeyu_2wGkbpBLt2FAzNEfdjY3eOivTy5p0r8NJeQv01pBRgSjC5eYjYqFl2W2IP_tUi-G29o5g77n0-vNGO7EJxv3KASXypt9REnUO0b-GgE0pewHolnbFi8HjQZUDKpF8SYS22vIQqzzUKBVA19SINpW_mKvTXd67LM6ioRgnBUFO8BLQBeMUkRuBHu-T_HPZ58YzeleiYQUSlThGxvDxk2XhDhsX8a9GCpG2AtvCjRVmc_NfChvn3pjFT87MpNjEz70ymadP3lIZxnBIwTItueT_cEjjWz6d2QWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPC74zYKDa08FlE1zukKmmHnRhU5wHFaIuKsoneFr5QrQhN-iqqqprZ9Wwo7qCq4IZ3jGQVAS9KNLKTtQGUYF_zlKSxm-gvsF0bbNQoLQGEBPkCITW77xapj85Go1-Q8Jl0XWpSjTnYYNhPT5dzpQJcbYIdYcVyscm-DQDUiCLNBIf9Hk45TuH3tQo5JiJnfsjBlzlJF10CPI8xoMVLpZgkURzjtC_j_kJSca9dPDNtzAD4YxarZbRmxErggAy-YkNHBtXdspr0-i_gXzWD5Lk0-Ro36AIowjdZc5O2jeDlJYBqLVzjYiAyM6TRjUVCGJOrvFlOC8T08lKAnb6gYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=ESChfbfjWUj9XzpwOrw8qdJ4rD_l4SoJq2VdfYTOV1tqkL5QNVhwDf6_n4igjp8UQVLpn1Uu-3vT-wth0em7A6L8pPfsal2U_aRJiqRurYW5P867jkFPp6yVkkN7c1tcLn9aXlO3vd2GTLTjSYdzQ3WzmRdrrN-8V9Vu3Yt2a-y67xltD2BQL0i-HPK-EmRA0eSjymK7obk-k7LcZqv8IWjMqrCdo0MrCjYZr6aw75jTqxxTh6Uz_F2vaVGBODHbkgH3dIDWS0sLiR9hSm_NlYRt3R6XJR91GPCoGWbbReCGX0xceg7g6jyUwfvStslYKgF6GiHvqYSt1YU_SrP09Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=ESChfbfjWUj9XzpwOrw8qdJ4rD_l4SoJq2VdfYTOV1tqkL5QNVhwDf6_n4igjp8UQVLpn1Uu-3vT-wth0em7A6L8pPfsal2U_aRJiqRurYW5P867jkFPp6yVkkN7c1tcLn9aXlO3vd2GTLTjSYdzQ3WzmRdrrN-8V9Vu3Yt2a-y67xltD2BQL0i-HPK-EmRA0eSjymK7obk-k7LcZqv8IWjMqrCdo0MrCjYZr6aw75jTqxxTh6Uz_F2vaVGBODHbkgH3dIDWS0sLiR9hSm_NlYRt3R6XJR91GPCoGWbbReCGX0xceg7g6jyUwfvStslYKgF6GiHvqYSt1YU_SrP09Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=eVwBE8cmlfzvSbaxXZ5VEfABsS-8NwFg9rv5jHue_06cW3O7HwRrTewoIsboOLPgpPv8N8e7ME8PLtcJR2WJlFS6-9Lg3WwRoWrOP3HpYwABp8NyrvsrS6JCNhk042ZgBUGCX4aRlXsQ2HjjDRsp9tZ3zxASlrusXC46nXQaUun_GFBpJ3I4r_VOQ-xd4bih6YZ3RiFM6Yr6alUX89XqUk8opA4m3wsvhmGyUtOZJZ7cgffElVi-bjvUFXI-2fzeKo9S5E3SY5Y21a2OTTOW6iIFcPl45_qy2RmDpJxV9ki68XOzuZO_hiw9DtJftx7-eD93jnYzU7Q1sm4hGrGpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=eVwBE8cmlfzvSbaxXZ5VEfABsS-8NwFg9rv5jHue_06cW3O7HwRrTewoIsboOLPgpPv8N8e7ME8PLtcJR2WJlFS6-9Lg3WwRoWrOP3HpYwABp8NyrvsrS6JCNhk042ZgBUGCX4aRlXsQ2HjjDRsp9tZ3zxASlrusXC46nXQaUun_GFBpJ3I4r_VOQ-xd4bih6YZ3RiFM6Yr6alUX89XqUk8opA4m3wsvhmGyUtOZJZ7cgffElVi-bjvUFXI-2fzeKo9S5E3SY5Y21a2OTTOW6iIFcPl45_qy2RmDpJxV9ki68XOzuZO_hiw9DtJftx7-eD93jnYzU7Q1sm4hGrGpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=SIPZeTSpjD4rI1PSHaQeJOjm3oCDcz76kROJt4qjcpF6xaqTJ3zRrNf-pV34lVuYOZ-BFi7N9RI7I9MB6azjakyuveiRV5OdWCrFMIbbHodyW_l8dzLXzObCyXLsHgFUg8z0c2Kf5005nIM1aRaNep_AMu4alMY3c7TxNkiZ0-8Ulou2hFdsnesdPyjpoLzG19bWAWLydrlvz2bZKYaC-_yT8JkzhzJ6ViUh5_qiLgALyQ5WpHYwts68-zoUFeXjBkBKxyiNWPO_ORMi3vDVFWfF3wdw72sywTiVqjBu1J5rIVqfrO4h2l0ZQ1hiS7f15JqloXb0Cphk2vXiVAUlICaPurxczKyKNz1HSPwgKd41LSf7bI0OL3F8W4EK5110S49kBAtv_U81vD2XZxfpMkyuKiSn_rrvjIRrtD_XcUfISqdeBUDQGTzpqaQ1xCneEdnsx7iJbKk2TNGC1LHS04PiQTWNHDeC1c6tSCr7ZMhOnUi_KYSbdbIncg8-1J5IMQ_sgL3R5AeTtq9J8RyJVSZBiiRRQc0ARCufCBW0j4WaL8lml0OL_buxmpqYo5Tl6SWDHSeD1bY_XYguW7HgOQMC0gO5YSOlnooIqgHoAZR-XA-CXF9S2fdYpqHRpD6EmTEz-KQpmerhG92T5tq3z9DXnWNNisewOQ35E5vapQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=SIPZeTSpjD4rI1PSHaQeJOjm3oCDcz76kROJt4qjcpF6xaqTJ3zRrNf-pV34lVuYOZ-BFi7N9RI7I9MB6azjakyuveiRV5OdWCrFMIbbHodyW_l8dzLXzObCyXLsHgFUg8z0c2Kf5005nIM1aRaNep_AMu4alMY3c7TxNkiZ0-8Ulou2hFdsnesdPyjpoLzG19bWAWLydrlvz2bZKYaC-_yT8JkzhzJ6ViUh5_qiLgALyQ5WpHYwts68-zoUFeXjBkBKxyiNWPO_ORMi3vDVFWfF3wdw72sywTiVqjBu1J5rIVqfrO4h2l0ZQ1hiS7f15JqloXb0Cphk2vXiVAUlICaPurxczKyKNz1HSPwgKd41LSf7bI0OL3F8W4EK5110S49kBAtv_U81vD2XZxfpMkyuKiSn_rrvjIRrtD_XcUfISqdeBUDQGTzpqaQ1xCneEdnsx7iJbKk2TNGC1LHS04PiQTWNHDeC1c6tSCr7ZMhOnUi_KYSbdbIncg8-1J5IMQ_sgL3R5AeTtq9J8RyJVSZBiiRRQc0ARCufCBW0j4WaL8lml0OL_buxmpqYo5Tl6SWDHSeD1bY_XYguW7HgOQMC0gO5YSOlnooIqgHoAZR-XA-CXF9S2fdYpqHRpD6EmTEz-KQpmerhG92T5tq3z9DXnWNNisewOQ35E5vapQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhT8dwPLFTz3jtzFYaV5k9u2yniPRMe4bpbUWIGJk6FPn9wMchesLVisT9hSAlTy-RITCD5rwzn2DBxf3xnZf9rsarZi1wY0MNaGfSf2upvdTNJmmfLF0nKOeX9op1-COwfAdMLuZGD_m_wqL56euGwMwW5q0tUg4XRyZQs5TpFJnnxwX10KxX33kkveir-deYxZwzMfuhvKPtDEK5hH8AYnYa0TZfncZ3g2KjghbW02gNFCop07SqhUpxTPUNu7PSsypO4lUepNbG3AqfWugK3wacj-HL0rLf0jLUy7mnwdwHz9GJLJ6y67MP9TtlumzsVQ-hOKQJDdbAD2MYweVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhHUKZowwnpuI6WOFLQGZdhdRJLcWJepYRckDRUt7xaPNU6bcZNlhkQND_Q5PvA9UjQaNBI2Q51ixaGARCm_uMffOC70vJIEpdPRmpphLUFgcVT9mhq0CwCfVEEEkm-t1uIhnhkTCtli-a2xn06fO_Y5FNwzqAAsyA6tde_rwWGdhbpdq5OuBFOatAcP8GLzzGn9IttQRHMc2Jajl__6-D--dUUKwbLMSch8Tb2ZflQvCW563I48hFV7FLZiOKMP0aQgXoM7P-h-8hdsflL_ccvaa55qtGq7qsyPJH89JekW_kUWOeVWQuet5gyLycgOq6c_hofmHXAkpqJzuIG0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=K4Pld3fVRivGTUqBkPt8d6Pf0G4G6vRHto8CxUqY6BYhl1WJUYlmTuTCB3KMLLabaeHidnl5QYEH2yFe1MzMCVpbC8I58WcO3roNY1CAsMRIphurjqbmePD7hS7KyqhNJNuqv6kL_B7jpAgfncffJ8NfCoI5oTOolM2hoFCW894mK1nMl6OL9uZteflry5T6KExKLO8SiPqXAuXmbwNWSV218KtPLg7WboQLU1ZrTfeYE7MYhEVyAFSxiy98Bwve0J_Q8_e6_0KfcYbaT7i-BF-mncQoeinWt0U1pOSf23yYW2giLeqM-7Z0cD1BIAdObJcNNINaGSyi0eziLHwDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=K4Pld3fVRivGTUqBkPt8d6Pf0G4G6vRHto8CxUqY6BYhl1WJUYlmTuTCB3KMLLabaeHidnl5QYEH2yFe1MzMCVpbC8I58WcO3roNY1CAsMRIphurjqbmePD7hS7KyqhNJNuqv6kL_B7jpAgfncffJ8NfCoI5oTOolM2hoFCW894mK1nMl6OL9uZteflry5T6KExKLO8SiPqXAuXmbwNWSV218KtPLg7WboQLU1ZrTfeYE7MYhEVyAFSxiy98Bwve0J_Q8_e6_0KfcYbaT7i-BF-mncQoeinWt0U1pOSf23yYW2giLeqM-7Z0cD1BIAdObJcNNINaGSyi0eziLHwDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COCyu6S2G9vHyZdgrjbCB9Jlmq6x9KUdAYBb8-Lk6h5QTQLUk26YaUtb63k1ki-75cb-zrEWrD2Q85iWFs4ErfCASIUZ8-2xzmaHODQCJobOzLXHpq14TGZOmh51O6phveWTRmoICDrckGZQAHFv5piLlRjpvZHcFAODzP7GP-ApzAr56jEyoBQJsYMu7avHvyZhio_ZAUCPOTyizRLa_7lxyMrOCVNvLxzwxMHe0zIgtebFVJ1fTLgeA8Wug7R9er1P0YE-ix9idjbM6ddbtwahBcsj6NX-EfM55uuBH9ZnjdObql8A34rqw0GhXvSXlrYNQ30-vC1MS6s_v3Pmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eudEQf67g9ikWG1XhmuvZ-IOoqcDKKUFSrilxdKOTlx9kq8DeKfev3HcSDbKvcPGsfUpxRkkmlgCRc5S_TkpW6HcjENrd7ucgrlgb8xBILqhLnpReUEQHMbaMG6OAyF4dteGMCWmpr78ZjrtBLr7TFI4VICZ2DbtXktigUzAq4tzjUrgrAz7pUXBLa7KHmkeS9zPVUb3vOLnLe2bDzF6wHzWiiA9CJmexXbeRVnVa2MGUfiENqW1nJ3HmEn5i8qP9QQ-B-wNZiWc5CRvh1lYGJj6uDiK_YHXzvy_DwtCKCEQ1kuzPXIqa6beqHs2CcO04vj7jnHtu55wDvJsJhjXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReEhSA0abpmPtYDL3rnqtN8BRWm6aAbI02Ueut3s4O1FF7ygsZcuRCaREdXHnBvtxMbb9GQZudV7US2b8sLg_r1TUA6HgCH4w2wHQi-Npmpbq9dMR_-EUiZsL7cuKJkSM82Sy461BExpon9CvQuQAxlswRrNLi8INjJPbnML23b48J2KWn44eBmMMUKzkHM9u9j54EO3j-0XhLGyZl_mPjatDNeK0nLSuBgufuXjYW2oDySzAKTiRh2nNpsVqa7Q4Q3Os14MyCEUD6XgDU7Yl0tuyt3v8aUWQhX5AxoY74dRWWRV-jfY5zQSjGVNgjIj83V77m2E_zsreX304cU4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=FcBkemy1CCgELGzAdB2HlM49Nkp6coLASM9-ytDW3pMLjHmngz88ekUrxEGp_6_cUZgKDk0p5BCwNtYzaHXdyJit0TrOCXduaxAo8JXu7dEDLbGGk5gSdOOHG8eJyDjMUI9NEUgAjDs8j0_rvYlS4_SeROqpfkwVnNxeysIqSuOcPIkMDi6d7Vl8S9BRNhxN65CdtdVG-lGrqhBX1QqiTS-jJrmYLGGrpYlKXLgVFOQcOucn7XleiPK-Q2Q0h402VRk-51XrcPUBo2pRCVnvOHVbUHdQTuP7MGYmw18TtvLhR-rB3gpQPPunSwFFAu5jpAhNV6j1mffT9GslNewCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=FcBkemy1CCgELGzAdB2HlM49Nkp6coLASM9-ytDW3pMLjHmngz88ekUrxEGp_6_cUZgKDk0p5BCwNtYzaHXdyJit0TrOCXduaxAo8JXu7dEDLbGGk5gSdOOHG8eJyDjMUI9NEUgAjDs8j0_rvYlS4_SeROqpfkwVnNxeysIqSuOcPIkMDi6d7Vl8S9BRNhxN65CdtdVG-lGrqhBX1QqiTS-jJrmYLGGrpYlKXLgVFOQcOucn7XleiPK-Q2Q0h402VRk-51XrcPUBo2pRCVnvOHVbUHdQTuP7MGYmw18TtvLhR-rB3gpQPPunSwFFAu5jpAhNV6j1mffT9GslNewCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsKNC9vs_lnieLWyI31rVRd7VLwFjIyXtsGSfr8JirrftRy8mD3Y0yWgu6Q3fDiXBHDAEuJABCGlMR_Fw_IiJCL5IYt5sv3zqKdBsRDjO7qI_M1O9kBX4pHvqmS6u1qcS4fzd5jrRigdmXT5g0bxk6vlTR4_tXzwm2FSPp4ndJEr856-JB1DorgvCRqhS7xXujPs4QU3fgHWBzm7MJ-WCNoa_Z82CH8n7huLt8m9vFBAXTtImj2T0zohHAlm0rqaY5xu4U5mvFSKa0GC6sukYYX6FoEDz312Aan_fYGpd4ymplkWXho-929ujb6Vc6mm7cY8_nqnldLg8E4b4bLHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VorEt_8pFS9YOLw6Cw1VU0MpdDy9JPjqWEAKZfZAf3SdCyP1j7YF5XaJ438pu-F1GwqjjrjRRC7Cg0o57HFXjMeI82UakjqCCkylgW2fJGlUbIK2aTyqj32GocIgpgznrBchkXp0U_ewDBtpgJOy-uo2ijcfeLDcVlqsMe4srYzy0ZOTJAFmmiuk89FQqd0LhaQJqPLK2hPxFISA5hDrXppqDrRxT8TIYrBVhhRqQMQ7vwalGmiaUnOKTCNjtlTeYN_hcIlvmP9Vv5O9QSUW2wXq8sUmVlPx47vZ54Rw5eQvrMb9XFM0ILKMBNP-vx8TNjKEPVg9PqZFYdbukvF1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWDRKsM0KekIRdDnrXECsj5p3aAeo52-zSQuycmSnErvuFbbSoJw6Crn-_5UmyMC2yevDytpsbKdwdwyJ49dhsFYSw1YpWtq9WZ5QzzzKfvJhHNZrl6pc1oZTZ7yCOuAS78mTfs7-0L7HFVCwVw6fz3CIOJu4fUzmUZ6qPytvEVBt4PBhgr1JL68dwuDNlBRbbzYguPYlwK4AXiXtDf8PbNPJsbdt-DyiGUGACVAxCQevbbL09RvJAZT0CNdFxPHJPgJsRKqd6HzGQuoFjg0VuS4qIYQwsBrM72ln8U1UKZugp8NqSbq4QKk5uDOU3pErntnXuO_sfVFV6WERtbULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jELFg2QIVQJD-oU4s8akwwPK_nJw5wFojCP6-q4JTaaqYWrKN3YCt893PJAvYSJuWUJozBM-cgAlVJ8t46q-ce0Wtf6PK6RZPOOZkJ757jbgHzmBX-fHfHVlP6vIKm3BUJFip7bgD5Oi5wBt6EALkL7PRYpoG9D3_iD-E-SZvTntmPpf2wQMdcl38xAgaBNiOSV-leNBVI_8zaOha12g5sWezD0v7IueuyjEWYUgy71nJ6lVbP1djitazgCFeXLSQ2P4JVJOgkTE-Zb4yL1zBLv_GN9ax1IEowAhSR5xrPyEM675-wtKJs0HnpWuQ-MBRy6A2I7nAxkfzq_pZX8j7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maY-wb1jZAhu2QfWU7LscFqMJ72hU2gyfSlnIHXzH2KPFNoqTW0EP_oaMYiFZ_Fjbwxau3yxyGD8Rx3_R57tmn1XaGNX3mCzmFmYTrtMdP_qbtTOtENsx_KsAzudBSnA9oKSsqCyuJUhj96zD0qdG9a-9PdQFAH9fMAFLPcGyWWD6XI-Fesl5ufQJAlsIdL8CxPapM3fPzHzj_3rGBE35d5lAVgLvQePRz9H8wZobqAwaE1Pm7Biebt94BepzPUZKJjmevnJDuyvNsAjr27L0iuiexaJ5HY5qE47GTc8Nqdf0kzD5leykKrKymOWLG9tzC3ojBFSBXXcWksdSbHq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=EH7n1rCRk6trZAMhK3EwTpZTJt4_YG3XZ-sw-OiP-NpBDOtXJ0CB6AhyUoHq53wFwPQBJVOQSgv1J457v9G0Qyt7a9no2FlHZRibzopPr1MTn6LO_z56U_-hJYLK9bFVJDf4lzAMR-3eNOHvhNRwu-aLWAaW3prP3a4wPSFUpkzqT9SVjtNSzFdS-78qtPXtzrNbWl_KaxZoXwVZd-cK4rC7-3HnUkfPZKeoHBu4AxlParF0yGc4-CM6XhYllERTya9WJjniDrcF2rz6mqBxH4IYvL8FaiTfjGw356Br1O_orgzhuUHFn_-Bog0Z1tDNwIdhfik4xVR8e9heVQduxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=EH7n1rCRk6trZAMhK3EwTpZTJt4_YG3XZ-sw-OiP-NpBDOtXJ0CB6AhyUoHq53wFwPQBJVOQSgv1J457v9G0Qyt7a9no2FlHZRibzopPr1MTn6LO_z56U_-hJYLK9bFVJDf4lzAMR-3eNOHvhNRwu-aLWAaW3prP3a4wPSFUpkzqT9SVjtNSzFdS-78qtPXtzrNbWl_KaxZoXwVZd-cK4rC7-3HnUkfPZKeoHBu4AxlParF0yGc4-CM6XhYllERTya9WJjniDrcF2rz6mqBxH4IYvL8FaiTfjGw356Br1O_orgzhuUHFn_-Bog0Z1tDNwIdhfik4xVR8e9heVQduxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqwRXv4Gs2nfbP7TiTG4UpfxtSsNamgU1iai5jUlFUePS1koRQZxfSRYqFN-LaNkGbI5d6YuK8gfw_j6cx23IEuYQ8p04jhoDcTChIBXFfq4r4g7ArYyw3hzeI4nIhV5ZHMPO0cfratfZD7BV7rfOOFQAu8LplRUpx1VwEuSZbvh4JM6Y6dFR3Y9SGEgkvzQAcLPS8DlgiJB2KNGSx42Ky6qm6hkuu03Fa_44S-qCRJRZ03rxGq-62B2lxJ7L1hGvJrvzBcdhNo01sqdrJdV2moYlXiYouH589guRAIjJcZtSwrZBRmu_Pmuna3NgqufLQEDynK8vDZUnrt84E3QQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkYYiK36KGCBnRRIZ-rMH_KuKq4aXKVd0QF_LIgFrrw3Ngy8OIqPqNGAHCTJhdEyc_AgK4ogcnvENW8Jq8h82p4Nr4-HQYuxCwUFOshrGAuudKVNaslqViW8KRUmzUU9sgFLymOof0FqoYYxl-vgFAfXLsBWsXAZK2QDptEZxTvtIsqK-e8gI71QFlwvEIkSRIniwG7z1E-GQqVl0X3uc94tqJsivHejsca3zucACXQs-6AYL6s5Z_ozTq10gAwmDn_ziAVPegt5qfdbSS0rGQgmXcjlRZIIWjSjmyTw77OEEJE002KoTuCTXeIsNgH6mA4zkYTb4htRoZa_Zm4d2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=SC6OJlUYOGo1x_-iDlDcUpn1iPlkfy1g_7NJR3qt00p0PjMVN08Pvx5tv8f80gmW4e7f7_yHn7_p74Bz_vK_CT0LqHzo20QEDDo7OX7sbnfF-qBW4odaTeSDGVax8wy16iMnWq7IJEEakkcdZ_nxeCcu0PFbD9ez5Rd8HiwRNDztkp6cU2tARbYc1PmKm7u05E0UCyYyI2PrUqU1xzeJfyJRUNgASgfxcx3PnHveBxQdG8wuCYQinY57WdclXk8P3qUWMXyM9SoQUVJSsWuyRunQZBuSBafUDag0Nm21SHylxcRIKSf-hdeXLIWusFODOB3h4WTT8zNWE25diWd89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=SC6OJlUYOGo1x_-iDlDcUpn1iPlkfy1g_7NJR3qt00p0PjMVN08Pvx5tv8f80gmW4e7f7_yHn7_p74Bz_vK_CT0LqHzo20QEDDo7OX7sbnfF-qBW4odaTeSDGVax8wy16iMnWq7IJEEakkcdZ_nxeCcu0PFbD9ez5Rd8HiwRNDztkp6cU2tARbYc1PmKm7u05E0UCyYyI2PrUqU1xzeJfyJRUNgASgfxcx3PnHveBxQdG8wuCYQinY57WdclXk8P3qUWMXyM9SoQUVJSsWuyRunQZBuSBafUDag0Nm21SHylxcRIKSf-hdeXLIWusFODOB3h4WTT8zNWE25diWd89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD0gBaIhsm_rvlWq8j2OxZ6-tBVx2FKrgjVxEPDxspV3GnB7z7Z1rFvvUa4crZU0WOmEkKv0Y1XkAKCnzOaQnaKD90b2KC39MDHumaGeCAx6iSb9-XAnaWCUlQ34g5rGz6ubfrNDQjKvUsmyTMHqyhNqlCzV6GfKMscl5nYgnQZrIth1tJUnGGkuZgkZfWQMvqmgl8OJsDzWpIoic2zhlW8FzeqE-SW01JpYd9639lihPXolZdQAbQ38iSBbtMwZ9fZmMfwWznKstHtTZx4f8RU1MRrBew3UkLRxrk3mHZiQMVoPl4pB9q8nuTgqQ1UaQqPtZj_6wgTp6aPqlDkppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlZfGukbuEPRVha3gAwEnXEmDAeQJPwoIMhI0Dc_iXnzIjyeoQT7ImiPGdU7wHgSLIN-mfRtXEJfgdYD89WgeclkJtijSnbgeQV5ChAjIGGu0PHDGrWXbsqJBtuFas3SMujobn5sX9ZHuupunChsLgTnJpejGWADOQZ3s1nLP72rK8j8G5lXjqtlz9XH8RWljOWfuAWaimb2ZToKESKhmBaWW0KFXjaKFETEAgnpACAuuRymZBXfQvSzeiyQuoljwMm0G2kpETZNe9krYslIOlq4CxxYpVwJqOycWl8u9pW3aNqqkAerkeEncjF5E4clM0SLGAeNESm832-c6szgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzM01BFCLKxNS59cAxJ02T08T8omv9sJ3Gr9mL02aHOWxcbLiWz561Thkf9UVju_y4hwM-MkHC-NCOO_Nz0G201lcpn0sef-9RIA-nYIq9y_oGjhGX3V5zFmAgGV76bMp_Yw1A9ydjuKLaPIao5A8GPzTd4PUH4sitYFR6x4U09VYxg4URpm8VOURS9dutxzCymVjprev68SE0TJTX7EyvXR985qmnzcypRnKWubL31kvMxTgXHS-o-LCJvqszI7hst1R5zyE1tWwq88HLOJ9gNZTImtHMxdfm9SCqRqUS102yhAGkzOn-6chl3GrAQuflXanCFjwAyjFR0cLxq-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9-IG_w_Xv8mc26jycXI2pNpkwAACy54p2c_CAsV-FEhH2b0FpPy1sIuT_v5rG163i9CXStzKNyJsaVgz4mY9uAIFjR2unCWMv5fTVZShouNUWe-zooPvZqR6m3dn-YgEwPhlPFn0X8mppIWGoUPAx7U9P89tpE4osxEnMvONUSmFMnIirWAdV_otrkRclnBewuzVr_We3qM9nM0CtZiA6aV1fzlT5uTjWqCxXNnxYfOS3ufMHCK0bjtNGS_F2ekRoeQBM7rQ5uapx7kFXJEzE17UujgJAOi_GD5ypP-gZ3DQ05lP7zNQxOD4twiQ8Buyeoe99TU3ce0Tdd8-MSszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=KfiUD7p9NB5s8kHZ1I9t9Rk6zaTBzJXRzB9Hx2nZrRqnaJQfOWOmNdJJipWgXoD8yQsxkp54gxTgESMAzk1vzOUDI8ggtxTwIqbhqDoyqVpgSttfgo1vdJNkdSeKGfllacFvJTpPuGoDILrOR1UYIKuP9Z3-IMYbd3a4OIOSCrZ-Q7OfIy0Es9phyN_ZvpTzFW6634h6_vzlq0AjboxnXM7lT5J628tvb2cLYxoFPFlTwHL3i1Wr4pGy0uF3yCWF7YpEzF6JgN50sHJMrzEmSEHgbsYQnpAmJt_BuiJO-rb5IExyt_6Rjo40yvKl2jJT-8mPybeJVCZqtGV3z4QWeGNU8swmoUMJGu2gnXhppNcx1aJ-eZhDjXgUhgvkh89zO1iHWtN99zUE7Yo6g_Mu3A5a2VGbOL3cPE8LqxevRKvBU4uPMgXsU3_MlgV-pQgI11ClkqXrMPPbOW7D5nAYx0Uqze9CxRy0ZJUqWy6kgD-VhOydn8asJtnowaHVDNznytFnDv0hn_amlQi8XH-UQ9KHXa8HmIFWiDJ2pmLJ3XP_TC7kVRNf0JoKisXxtphKpqf6APlwtpyQHtVzg9Lv2R3Qzr-L0G-RmR67HZilNXRotsqTEujQJdvL4LIWOa8yT_q_VK_U7RPfpZOxEf51AkThknARBjbF_RfKk2czUZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=KfiUD7p9NB5s8kHZ1I9t9Rk6zaTBzJXRzB9Hx2nZrRqnaJQfOWOmNdJJipWgXoD8yQsxkp54gxTgESMAzk1vzOUDI8ggtxTwIqbhqDoyqVpgSttfgo1vdJNkdSeKGfllacFvJTpPuGoDILrOR1UYIKuP9Z3-IMYbd3a4OIOSCrZ-Q7OfIy0Es9phyN_ZvpTzFW6634h6_vzlq0AjboxnXM7lT5J628tvb2cLYxoFPFlTwHL3i1Wr4pGy0uF3yCWF7YpEzF6JgN50sHJMrzEmSEHgbsYQnpAmJt_BuiJO-rb5IExyt_6Rjo40yvKl2jJT-8mPybeJVCZqtGV3z4QWeGNU8swmoUMJGu2gnXhppNcx1aJ-eZhDjXgUhgvkh89zO1iHWtN99zUE7Yo6g_Mu3A5a2VGbOL3cPE8LqxevRKvBU4uPMgXsU3_MlgV-pQgI11ClkqXrMPPbOW7D5nAYx0Uqze9CxRy0ZJUqWy6kgD-VhOydn8asJtnowaHVDNznytFnDv0hn_amlQi8XH-UQ9KHXa8HmIFWiDJ2pmLJ3XP_TC7kVRNf0JoKisXxtphKpqf6APlwtpyQHtVzg9Lv2R3Qzr-L0G-RmR67HZilNXRotsqTEujQJdvL4LIWOa8yT_q_VK_U7RPfpZOxEf51AkThknARBjbF_RfKk2czUZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhE_7rdW2MVQszhPhZ2ImM5mhcQPXKQnZzFNlbAr1dNo6N2EYQ_QiG3GZrtXhpzD5b4Uapu2cu1ilr02CcUpj8wia9NQ1lst6CsjTww6hl2hEOXP3VwRf-bg4nzPSJP8qDhx_s6xOmLKZucxtvS0ivSrtNCgUvjMmse9CO4_Mm5QI1FibTPzCvPGs3k9DKw4jAMC7-xa_8b-C61H1E2tecKh0YqRVqZNawdE9zWQHgvMBywD0F-V8iIq2dUjn0KqlNmHR_ZfG0ifFkGaZ5lS7v7-ChcBKZmy21qHmA-JNnaSGEcE4L37d-TauCGmMUsYZGQRJohVWY8GSucfjaUsykGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhE_7rdW2MVQszhPhZ2ImM5mhcQPXKQnZzFNlbAr1dNo6N2EYQ_QiG3GZrtXhpzD5b4Uapu2cu1ilr02CcUpj8wia9NQ1lst6CsjTww6hl2hEOXP3VwRf-bg4nzPSJP8qDhx_s6xOmLKZucxtvS0ivSrtNCgUvjMmse9CO4_Mm5QI1FibTPzCvPGs3k9DKw4jAMC7-xa_8b-C61H1E2tecKh0YqRVqZNawdE9zWQHgvMBywD0F-V8iIq2dUjn0KqlNmHR_ZfG0ifFkGaZ5lS7v7-ChcBKZmy21qHmA-JNnaSGEcE4L37d-TauCGmMUsYZGQRJohVWY8GSucfjaUsykGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZBPe5Pfl2kh2FpyBY8CG91Ny0OmIL-hUxjReaXEHLxFZvPDh31BkV1rXe9Sy1Jy8UeeetFDpeaNd5pf3vIud3hgtr8dSKiqb1F93PTuip-tKHpz4Qv6sPmYicPHfx6sYpuTkkC_HWn7E_o9h0g3f0yWsVTOw1keluenr0b8H--wSYxPs5Oxdj2A3O3S3Et4bMn1A1mUjZHAKE2M3w1d5_kwQBWv3Zg4Q9cLwrCXyUeer8chzCm6G9zbbi0byjPY1wSaLH6TgZRndNSJmr6oDcP7P4kYCCdjpaxxntS2MckP75d3uaXiZQw6fgo2IE-F39YBPKUH-S59MPZyswpG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqQbNRcHXCuxggR_4WIlDGxmuZlq8iPbOQnFXRyQgFdbY72LdDdE1nNpukL5yb1aT7l7CPAV56KxBNQVpyg9x6R7ZfVdAmZsBqOoOCqdqTx5jgnFiOqq4d6PutWvc0FlIawn4B9E4n_iLdS5qeBip5lrC85FDfrEq46RzwQXC4JZV3IuwDan37-PgFH45jYwgUpTIRCPoNIK0gz-I8S2-rRexMxabXQiXmzM-4YIL-mHclZRPmL0qAfFHx3szob-As03yv33lif7-ewma6h0cH5X4NwV1gmgHPSPHzTIZVRrODAbnxOof-2QM_GDRrq-U4Gd4VDLFv0J4nRi45u5cSfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqQbNRcHXCuxggR_4WIlDGxmuZlq8iPbOQnFXRyQgFdbY72LdDdE1nNpukL5yb1aT7l7CPAV56KxBNQVpyg9x6R7ZfVdAmZsBqOoOCqdqTx5jgnFiOqq4d6PutWvc0FlIawn4B9E4n_iLdS5qeBip5lrC85FDfrEq46RzwQXC4JZV3IuwDan37-PgFH45jYwgUpTIRCPoNIK0gz-I8S2-rRexMxabXQiXmzM-4YIL-mHclZRPmL0qAfFHx3szob-As03yv33lif7-ewma6h0cH5X4NwV1gmgHPSPHzTIZVRrODAbnxOof-2QM_GDRrq-U4Gd4VDLFv0J4nRi45u5cSfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQY5KVqsLfgwxScj-ms_slwecfTXZiezxM1VzXa73d2KSBNFHQyESF6dn94tKWxGHs8pJm0gFmCl-3yuj9DQaEomIRJ2rgn2zFeyqasWRltkRoUq1Dac1CwwojrAczDh_naOvyPMU5SlPJ19G6osWbYjX1BN2DVGIUGMq8pWa_buYsmyS1_Ne_UlSWckkRg80MBoH795CrQYwTOhXRzjBTQIOecYqc0AaQPcVH0FzraQBn5LSQ1NPDoDXZZi4XwFnBHWig3woB8sD30ZH0li3EIVpRGmQX0hPjeM9bL9KWIDC5voi1y4A0xPApYxrLzSpq2sGk46UL-xDPitachHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=su-zwbuVQey_SmnHsHBxV08Bbh4aOWWCPX0ypEdXnWUaRbhP3oGtZBWBUpQK3GmyHENAx7mxH0v-dpWyK3vDUeyvC1i8dCKpNcwmQ3X8LSk-UW9emorU3ewn4Wruaju6yCq75kPtVf3z0bRjHm34XAhkAZ8feG5jzyQGBENCX0NSscluye8b2YeItKEF7FJofYS9Vuhy7cU1U6iD2pVOCo3JmWNFI68ulRWK2bnSGvoUL2MfsFC0VoI6MVpjD9ImeAzfmp_qX0HOEz7iv18gUSNxhJzrhsnJFz0AVFu3HcZ4PCRKWDbeJzuNTlI4u-leZWhe5Rm2BAWTHJscFWzT6TFjYLTP8N1QsaUThzt6ajWqx6w1zTTsEHidpHhr7Mbnk0Th8MrvmkD8onizkWVSTdhpdsfdcx9SDVKZ89zd0ZqsQddO2fy9JQJhhqZ6zODEMLLTGaDiAvk3ywIy04jqszl0WUS5LzWkFeGOI3zXarhcluRopNGs_nRATkYyzB0vYhfbFme3HnTN9VBbSaIuGnFqjTEt4UMx7fbNvxpGIIiBxCQFwSPFudoc_EmdxVOovL-Jj4S1dq7Wldy8ChjEi1tlxDIJED_LigVO4J4yhtBKwuuSzr3yAe82AhGzaHIva8hsVkFAz-RW1JnW150vsJ9CJKuQfmhogkmjyZFMpDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=su-zwbuVQey_SmnHsHBxV08Bbh4aOWWCPX0ypEdXnWUaRbhP3oGtZBWBUpQK3GmyHENAx7mxH0v-dpWyK3vDUeyvC1i8dCKpNcwmQ3X8LSk-UW9emorU3ewn4Wruaju6yCq75kPtVf3z0bRjHm34XAhkAZ8feG5jzyQGBENCX0NSscluye8b2YeItKEF7FJofYS9Vuhy7cU1U6iD2pVOCo3JmWNFI68ulRWK2bnSGvoUL2MfsFC0VoI6MVpjD9ImeAzfmp_qX0HOEz7iv18gUSNxhJzrhsnJFz0AVFu3HcZ4PCRKWDbeJzuNTlI4u-leZWhe5Rm2BAWTHJscFWzT6TFjYLTP8N1QsaUThzt6ajWqx6w1zTTsEHidpHhr7Mbnk0Th8MrvmkD8onizkWVSTdhpdsfdcx9SDVKZ89zd0ZqsQddO2fy9JQJhhqZ6zODEMLLTGaDiAvk3ywIy04jqszl0WUS5LzWkFeGOI3zXarhcluRopNGs_nRATkYyzB0vYhfbFme3HnTN9VBbSaIuGnFqjTEt4UMx7fbNvxpGIIiBxCQFwSPFudoc_EmdxVOovL-Jj4S1dq7Wldy8ChjEi1tlxDIJED_LigVO4J4yhtBKwuuSzr3yAe82AhGzaHIva8hsVkFAz-RW1JnW150vsJ9CJKuQfmhogkmjyZFMpDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMHg_7qj1vBixg5RfNAyLmRhC1iWv8iZhZwfik1NxQt9Rma8ppN9g-VmgeJI_2Vt6BCkYIrDJYyRrmhH43cK3wSjnAsmrmHoZ_aW2zgGoX9vuPvqTDRQnskHg9vRRGDFTSKKxZmSCgAzC_S4kGe_G7bce-o3QKwz8wPBE8kWFZx9JPaF0RFYywy5kWDALrMvvDBrgejEnQbQKjOryQrWjT2VsElS26TnaFJVJviJrdjnhqylJ1R-gMGx0dPdTDqEQcUhWYTb2bXJLPEFQio7lFyCqgBQG7YHed7OOnC_ZLTIH0X54pUTOOIQ8627BYdwlr-dZNAUHtlO0jWn1Lo-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmFsbg3H7jpT1BIE2fKoUePeC176wqLDOJZRk-6P84x1Y7sNRtr3Ud6ZoKrtaz5dzJV3vHZoRmGlvovj0gV8gks7atJaa-VzFdAUkw_oxbpWacIlt7qenbgOtY2-5LxB715WtUzgMvPQYnFdOFRk2AYaOKdrTCe-YKfhZ92aBrRQ-4c5BtqU-Oy0mtLNayr2uRF2uc7l81EWYo-aAXEQ_E2fdu_50T6VumISQ5TFwF2fZIQAKTXUbaUiYwZB_ybweKAZDvdXsSqbrL1KRGF5XQfRqZnlQ1WURyU2g2Lx73VtkpFsnZkibDkF7604rBYdQOTo5fjMLB0T7q8-nPxRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZsdMPYKwfrmbTqITqCuTxJNpJAj4IpMc64LQcL0AZ85KJYO8rsaBLfFIOiJ7ZfNKLPAND4LJK8QwkI1kDdVgkicIYTtlnvT2wH3Sf2JLPkm7YdxglxMNqAWicu84Mt2YlrlgUZCX9S9v2WbT9ixim5MZ2at19HPp1-JS13qiEO23XfNrHamWidqIosYiB94FbOHFbtMKktthVInasHbE4YRXxHHnLgg_k3By2XM_VWheNQmwb9l8QtFzEocurTjdv37nSiXjMntyGSX5ErBuYzXj80yBkwsr6zLFuR-F0qQyj0PSJst0VQVrHdhvPsspAcxL-imRdVl5uGGLb0rzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWV-ftC-q-98pV6foAd31cPmTXzwG8ZnehCWu0SpCzXH5gzkHI7gtXdkmdc80Wt_RLe2vAeRkVB_U5iSt1v6YrwDafG7JNeq9Alf0h8Ylb0ErXamLCLcHeFPcWd90kZBulxa0f5fcYnEK9Ma9BfMLpEEqZxs7XSK_V-cyFjr1wJwwX8JS8alZJ5U_Mqg_N7LNoy2MOVvqSmUZTHySKscbKhsWbPcwopj9U-4T0xaIR8r7QsQ9v34nKgRAcoMa7t8zPU1f8qPUvGNrPHkHjkvydXqJnRQsp-YhodcvvFh9430w5T5gYmwUOLBl2AKOmqn7uCek31N7oTEIuPz0OOZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJw88w7nPvOYL6pwZpmqsaVTTQKehzZewXq1_mjAkptPblWyiLb7-_40v8WIOwSfwaFI-F0v6Fy5gAURrqE9Mx-GVigMH5VRv42zUn6aNTiR7UrT96qHm064LSeP6cFWXH49H6wwWEIqfoX1VDwi6uZ1kKS6bq4x1ZiRwplP--1__0NXX5j-nVOvaGxHEOsV77ocqTDjBzaQYe3fZH6Jn_xUfiwoUg9ZFS3l0eba7zmtlV9RoTocgDLjZJjAPxPJ_FMthT1_wQq1piXZp2Dzd5qVx87AdTv8BTMXM8S9qAxNdjB_kw5nx0NwYYTFgulRyR06md9As8TUc7gzM6rNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
