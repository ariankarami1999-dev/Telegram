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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 144K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP5TU5bKWfej-pn08orWdChtYArDrZWGNL0gYOZpVIoEmn4tGJdMtxaxBZeDJS9lix_d7DFwEu7zuNNiU4nW5R_29_gdPd0DFzzPNE42e7ZKFCiBU8FMJcABmEdhgrMi3lIJW7N2rkjAvMhflYaOfDRVbojb2MX0xK6DnGuaU_SpfEJME66uY2CDBR5uzGvu3t4VyNrZeTFA8Tmb5YfQfCVsslyLg0dwlyPY7qmLKKE85YI0NQI9M5yLeXbadCvvqbIE1LV1blkNta3d149u13tt54y7-n9qSfVARfhOYIhdkfaCBRrER06fVw_MvdpXXiT6Q0ZZG5DggMnQImg07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=r_uR8OybMicfgLtd88RBq4O-njs4yeGnRM6Mi0pntyDJpmJr5hQ8BYtmHgLL5L-3zym0VpkbVFp5fddLobkLDrc7dP6C9bKj8uoVjxhSLEq0Z4Ux1AXRvBTMifrD3Ley5ikS6iNCpWG4RxhVCut4AEHUoIf8fNuX5-P9kc1dqVbFrVqXBnmfVvSFRdw-Dydd8meI4ECu7j63w9ea-RI3rA8D5pBKlvEhDKhqNsPyUZXjB_12lrwVYl1Xz9u2oIlUfiOiW7SmR43eV9cr-SbEiTnYHHyejjr3aM4EZSR-PoyILjkp1tQzugoO67zz6wCSO9b5p0apfqeT9-ltMo73gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=r_uR8OybMicfgLtd88RBq4O-njs4yeGnRM6Mi0pntyDJpmJr5hQ8BYtmHgLL5L-3zym0VpkbVFp5fddLobkLDrc7dP6C9bKj8uoVjxhSLEq0Z4Ux1AXRvBTMifrD3Ley5ikS6iNCpWG4RxhVCut4AEHUoIf8fNuX5-P9kc1dqVbFrVqXBnmfVvSFRdw-Dydd8meI4ECu7j63w9ea-RI3rA8D5pBKlvEhDKhqNsPyUZXjB_12lrwVYl1Xz9u2oIlUfiOiW7SmR43eV9cr-SbEiTnYHHyejjr3aM4EZSR-PoyILjkp1tQzugoO67zz6wCSO9b5p0apfqeT9-ltMo73gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=uAcEDYXXlZNt6BJKD4Xz23QHXgLTKLy3ivWPgkJlT41sd_dP89qgQH7nc5oLbmF1UxryoyFO_2EkMvYe7IW4gEG4DEeHNlUywTmFRFWxzHf8JPPmPJIdPn442VFIgn-N31vBebY2GMsiPYdkdToV8BKjRuYah4YygsjZNwQu-p46cwzqDmU4KaD70BdeaquwtwRfLT-5WzZ3JhMD3Oo0g1CvgOtNurqFZpqkYErk-v9Fc25CrxecB9l7RU4Re4-XXeCc68roFNPPBSiuRAMQtF-pbj-uWhm-16SSUBEuxevAgwbliWReYZDd8KESRcBAg5GQdbaPhNkQngowaP-Q5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=uAcEDYXXlZNt6BJKD4Xz23QHXgLTKLy3ivWPgkJlT41sd_dP89qgQH7nc5oLbmF1UxryoyFO_2EkMvYe7IW4gEG4DEeHNlUywTmFRFWxzHf8JPPmPJIdPn442VFIgn-N31vBebY2GMsiPYdkdToV8BKjRuYah4YygsjZNwQu-p46cwzqDmU4KaD70BdeaquwtwRfLT-5WzZ3JhMD3Oo0g1CvgOtNurqFZpqkYErk-v9Fc25CrxecB9l7RU4Re4-XXeCc68roFNPPBSiuRAMQtF-pbj-uWhm-16SSUBEuxevAgwbliWReYZDd8KESRcBAg5GQdbaPhNkQngowaP-Q5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=q543NOSQMZcKlxNVkCkBNt0t_kJnAze2lA0Ot1Bhu_dKUgmjgAxsS6k7f0QISivE_IjMe68hqU7pqmiMw8UOUBIg2cPSb2UgMmRWDAIXZALVt-63jrGdHhaR6SOKE76mYruekF3VCmPUskZGHGzcYDjsR_kDGSQdrov1w73ZTLq4Ro_QfT8mcCGLJOYtd5GHsO3WiQcEjodp7cpqY0NSZYWJ30io7fcnbHYi4COYkAF1rX5f2s0O8NmijjmGWScC8jScgkf-lvLAYeVkPVrCOH0-c3qGT2gNojhyGbUCQ24MuVW9q7uf-eyIHn0eq7xTSFP4AQibGz_bFsvfh9gecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=q543NOSQMZcKlxNVkCkBNt0t_kJnAze2lA0Ot1Bhu_dKUgmjgAxsS6k7f0QISivE_IjMe68hqU7pqmiMw8UOUBIg2cPSb2UgMmRWDAIXZALVt-63jrGdHhaR6SOKE76mYruekF3VCmPUskZGHGzcYDjsR_kDGSQdrov1w73ZTLq4Ro_QfT8mcCGLJOYtd5GHsO3WiQcEjodp7cpqY0NSZYWJ30io7fcnbHYi4COYkAF1rX5f2s0O8NmijjmGWScC8jScgkf-lvLAYeVkPVrCOH0-c3qGT2gNojhyGbUCQ24MuVW9q7uf-eyIHn0eq7xTSFP4AQibGz_bFsvfh9gecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=LdDO2DIFqWXa87NJhgdKnqmeeFYmEtODOI-1syvaj9ftYXIH5ph2miVI2zAK6AMnrnrGtRcvgdcVtCEBM_tSo43FBKY0upcSWWdkt7QLlFq3-LLJRtbLU_O3lcmGsKHouSIqiNKzXNulEsYDeRiLgupWtkEom_0i4VbCwLcp20R48_kjZBLKLLa1NzkKa-kjH6EW9tkVnbhUz1h82BotyBzyHTNTdCTzElVv_40YnIOoyJ1VPaUjvspF77MyPNOQBdQ9OlwCrhnG8A8HH2x4AQj6PZxfedI2fIXDBXUaZs34HOwUpQLGWZpXJUM4MJWqxtpsBy1fE7I2LhlD604Jjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=LdDO2DIFqWXa87NJhgdKnqmeeFYmEtODOI-1syvaj9ftYXIH5ph2miVI2zAK6AMnrnrGtRcvgdcVtCEBM_tSo43FBKY0upcSWWdkt7QLlFq3-LLJRtbLU_O3lcmGsKHouSIqiNKzXNulEsYDeRiLgupWtkEom_0i4VbCwLcp20R48_kjZBLKLLa1NzkKa-kjH6EW9tkVnbhUz1h82BotyBzyHTNTdCTzElVv_40YnIOoyJ1VPaUjvspF77MyPNOQBdQ9OlwCrhnG8A8HH2x4AQj6PZxfedI2fIXDBXUaZs34HOwUpQLGWZpXJUM4MJWqxtpsBy1fE7I2LhlD604Jjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgrscdclrRlV6IL0KWCzuOdVdmQmASYB2tU62jfyQoTg443iVoX6lLSNWa0MCigrtdstwY_C4nB5uLxEPPshf36wpVUsbXjx1hDnqiyw070he2gW0G4swqgnMgPCXqkNdGCZjvoA9m7EFoZiZ5SLzPsyOUWbcx_RJUK6TyJZjZxchuPEIrtUw3QR_j6fAasxdgQvAzclNFyQpPZNLWzMcaMFQNkFHg9U91d-DpLr6WbnAJDPzuclsIrqybCOGF4ZLlMHJ1qdSk-2iyp15xIEZYEXIZjkwcx21nOenm810v7vRk0MbglFcclprqxZpGGoK2Oi1ExncR1LPE30TU4z8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgrscdclrRlV6IL0KWCzuOdVdmQmASYB2tU62jfyQoTg443iVoX6lLSNWa0MCigrtdstwY_C4nB5uLxEPPshf36wpVUsbXjx1hDnqiyw070he2gW0G4swqgnMgPCXqkNdGCZjvoA9m7EFoZiZ5SLzPsyOUWbcx_RJUK6TyJZjZxchuPEIrtUw3QR_j6fAasxdgQvAzclNFyQpPZNLWzMcaMFQNkFHg9U91d-DpLr6WbnAJDPzuclsIrqybCOGF4ZLlMHJ1qdSk-2iyp15xIEZYEXIZjkwcx21nOenm810v7vRk0MbglFcclprqxZpGGoK2Oi1ExncR1LPE30TU4z8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI1r9kyB-BGimgd3u_V8qbuZ6lgljMH1Hm2VNxDk6geMvqzm5mRqP5ysZTJkj7JTSwMSCFka2g_5CeC-CfLd8tvpgdUHjWQTmicfprl9Z-uN4Da05hI8dVizD0saVAQvtjKnXq3xIhxr9fog7a_gyxf7LY3oN8werZr7vgHOHIZetCjVIu8CN-4G8paotgYxf6AWBQugiiFkPhh-CXcaVJj220IuRD80FC60cxviaV5AA6bDnELvQCDqNAmeZ5KpZ0hDXWm0THaOlpbTq6awA_DgdGOPEaeVg1lNVzxECmP47h25Jr2qGwoEQ6bOmgDD2a9c_yP7ALi7zqE-olWGEOBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI1r9kyB-BGimgd3u_V8qbuZ6lgljMH1Hm2VNxDk6geMvqzm5mRqP5ysZTJkj7JTSwMSCFka2g_5CeC-CfLd8tvpgdUHjWQTmicfprl9Z-uN4Da05hI8dVizD0saVAQvtjKnXq3xIhxr9fog7a_gyxf7LY3oN8werZr7vgHOHIZetCjVIu8CN-4G8paotgYxf6AWBQugiiFkPhh-CXcaVJj220IuRD80FC60cxviaV5AA6bDnELvQCDqNAmeZ5KpZ0hDXWm0THaOlpbTq6awA_DgdGOPEaeVg1lNVzxECmP47h25Jr2qGwoEQ6bOmgDD2a9c_yP7ALi7zqE-olWGEOBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=kROOLPFGEUn_psGUqApgfe1w0lyOmwbjDALwEn7AZ4vQolgsyImwKYaWI08unHPoqtCz85qHANSU3gRv0ftDG-clShlkBttiKgG57p3DWP-Mk4GyLA0dze1TH0R7iZULN8cfdQ7jC-41Cr6yAyvnE1aIXDJSCv4ZLyYvvmyi3hPJkEtvyG6cARFeyqVrTqEORcnfhzue_ZymQf2rH6QmRq2iu5R6JOc_bWXh5mFT5D29NEIi55dUAEJY7OfMLWmSGTZtcsmGZSA4eLgmQUvddgiVpQRCtZ0n6H9vIIja0xnViP1HWqaXKO-eu8Vp3ZlhRRILGTAK_EJ7-WhttUm3b38hn1mVIZJ-FNE875lw49Fp1cwJpa17sB2bi8uZ1Eex1d81k-PNlhLwA3C_5ZRcZri1VIwMxCQVqdEWm1zDi8L6p5VrHdTGiHV1t6WsaKkHrUygQ4EvHxSMVCq3DEHMfHYJ0QGLPlF_8RWPPTxW-hWQPTUK6qfd_UZkkS7hyyl7C89PEyn7O4zbHjf-s8bkPgAE61Sn0HM8ja3IMPyj73vit3LIudfggmmeYbgPKqib7Bfer1RNwr4eGd12eJrZC2Sa9tonKs90i7Q7PUBrLwsEDJQV2Mh4kpTZyleBkDqIR4LCmW5a4otMy72Mms4sUKi7EVkn5WoPnXdOBj4lPBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=kROOLPFGEUn_psGUqApgfe1w0lyOmwbjDALwEn7AZ4vQolgsyImwKYaWI08unHPoqtCz85qHANSU3gRv0ftDG-clShlkBttiKgG57p3DWP-Mk4GyLA0dze1TH0R7iZULN8cfdQ7jC-41Cr6yAyvnE1aIXDJSCv4ZLyYvvmyi3hPJkEtvyG6cARFeyqVrTqEORcnfhzue_ZymQf2rH6QmRq2iu5R6JOc_bWXh5mFT5D29NEIi55dUAEJY7OfMLWmSGTZtcsmGZSA4eLgmQUvddgiVpQRCtZ0n6H9vIIja0xnViP1HWqaXKO-eu8Vp3ZlhRRILGTAK_EJ7-WhttUm3b38hn1mVIZJ-FNE875lw49Fp1cwJpa17sB2bi8uZ1Eex1d81k-PNlhLwA3C_5ZRcZri1VIwMxCQVqdEWm1zDi8L6p5VrHdTGiHV1t6WsaKkHrUygQ4EvHxSMVCq3DEHMfHYJ0QGLPlF_8RWPPTxW-hWQPTUK6qfd_UZkkS7hyyl7C89PEyn7O4zbHjf-s8bkPgAE61Sn0HM8ja3IMPyj73vit3LIudfggmmeYbgPKqib7Bfer1RNwr4eGd12eJrZC2Sa9tonKs90i7Q7PUBrLwsEDJQV2Mh4kpTZyleBkDqIR4LCmW5a4otMy72Mms4sUKi7EVkn5WoPnXdOBj4lPBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2LJ8gRU7eN-HBxowpaRj5oNuEN_mpJrj6S33x88WoXFTCm8pWb5Ziqi39bvbUQDyv5IvtgE4nqVIyN3bw6rKreiOPDo_ErcO_PZLsOVKnWPLl0HWQ1fB28KY93uuwg4F4h34vWgP5fGfaNXM0I17IwPPP7xIsxbsKoOf8CKJr4Ptu9QHJWljZnaAFMj7G-4FqpNiwhuFnvJGzoVleU-B_8p_fmNfu2h1j0lu5vq6RoX9uWtdCACYrcF1ZsUChSAv0AOJV98zb7m47MpIaVVfIU1H7XTXeqy2zIddmO0oWlDozBRcSG4wet5ELvxHZujdqRjNocobNNgMjqNbnEQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI1b1wQl3UKNjlFIIGai6wefuKMBc5o1ZIXmWHuUU3AwyD8jvHG2_ZYOzYzWFiLgf2c5rqc3hj2VifvBD9M5t26Fej0mk9fO_ojUOIAzF4oEr-1yVdiLtg-dbMhQCptMAXhMuEBasDw08Z7UwAUwdImEPeYX5duRsYbGJ756WSgC1CkTED4v3DG_YATxP0uHI9m8MN_o3d4JX-i0u4V8RxYEIoKy3zPYyYQyPjd6LelkRh4oMwuzgxe9v-LhtCA8PKUP9dL7NYV8GLgGft0VLpLKCMbyQSzkX0cALo7Yn-li1ODyKVLv6kVziVqF553ackyx92JVx4foMSkvdXJO8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=Uj1kKajg_P966IDzwOhTjB_e0cV0gbz9NvclMDpXmM5zIUmYv2IfQMPXnCveMhq6M5CFVntSkUmUQfvi4qeJt5geaFv_kTTPgFIyIKzAeyQJsS_7woBLUZzTAifhxLFEgvEmJnSaw4M1Sgq5CNFiTRDujI7bK9wRbij0pYWOiQ6UIpROieWcG8SGaZKx4yT6S4QcGjLDbmW2G5nwmV9KK9izIsVwIGm0qcuHSea_xP8h7mNMnMx0TFvwM0vKWVruZODaAOzuq7rNt5vA7vbu-voXP_5V9DQ3iMq9zjtjb-IslPnAjNy5p4Zs0VT7MoZgmGqDMYsGcnTi_3-KIKjnLoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=Uj1kKajg_P966IDzwOhTjB_e0cV0gbz9NvclMDpXmM5zIUmYv2IfQMPXnCveMhq6M5CFVntSkUmUQfvi4qeJt5geaFv_kTTPgFIyIKzAeyQJsS_7woBLUZzTAifhxLFEgvEmJnSaw4M1Sgq5CNFiTRDujI7bK9wRbij0pYWOiQ6UIpROieWcG8SGaZKx4yT6S4QcGjLDbmW2G5nwmV9KK9izIsVwIGm0qcuHSea_xP8h7mNMnMx0TFvwM0vKWVruZODaAOzuq7rNt5vA7vbu-voXP_5V9DQ3iMq9zjtjb-IslPnAjNy5p4Zs0VT7MoZgmGqDMYsGcnTi_3-KIKjnLoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSKXfixdPdfbk5i_O0GyVU-5T7VCFSQsA6DvBBqiNGD39IecTWLgYg5ZERMMgGJdBVWTgoX87REh1SQXFOm346cVPDkbhGGW9p-8fI3AZHeCXy54ytRrSHIpkkABCM_Npn2wNAG1vqPXUY6EuRHNrtSg2fmASiPcsIZIm4zhNAFazd7P2MuoIa7iQFN75nRNxrWv5s5IBCSr5eN4NuZxFGCGThPDY1CkpJPh-kZ0QW1TukC600s0cxAE2FsIw4OTjkfi_l03TtDZQeZMCYONs-Z3TjEEPv4wFPg8t7aLFhcg1n4-bRT6egr3C24PKnKpkCfxYUyebS0dbdoMFjkvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwq1AWS12VTaiz_uaHQUU-Nk8zNEps31Kl-OP6E5suYJlflBGquvMmzwvJ4-JhZFKsnVi9IiwgbXatG7P6HRf7N8K1hd8MJM6jybae2yRmvANjAGcUJkggWUtUaoCZ-OIZGu0dLzyyb7ztcyl6TYyix6XjugkbCH9OP8qKgcPU-e3RSld1U0QP9j1SVuaMBHhq_RBKEkfCmLtLkb_44CYTgejEfQUZ11aix0r2UJrJI6ulZTQXAp1uQ9T7zp2KFjPJ77QtcICmwkDvOXO2QsX55R1EK2_v6cwtF6RfcL2vo9kJQLRuJNWjNvk1q5bmvDXfU6Z5xp5uH_kOA4hCyGfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=SLQNdL7sRwV1q-J8LEqa-r7oVstb-jTh3cET0SuDU_cbveB0MC3rrmjfEd6QtdWQbscOuHeNpbwSam-LxN06YyrqONTd14AbLYOXdu4xkjpOwTwhRBJdFztV4H87yiJ-dqp6SWKlMktSKCybh16ii9A8Pp1BErbsUbNa3rOpJdANHng13r1B4GeNhhZr-7ACc5ut4tOp4FNvA7t1HyX3deZEaKtK8ziROTqJZhzbUPa7sPG6UtX16kRBRYtvFcac8fLJ7k36WB5IQUN3aUIoH7gUZRuyi3jgVDJX_8Gq0xNRE-aFn00Onm4LLcpMWwo-Ny_8WqdL4ic4pstXFHEwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=SLQNdL7sRwV1q-J8LEqa-r7oVstb-jTh3cET0SuDU_cbveB0MC3rrmjfEd6QtdWQbscOuHeNpbwSam-LxN06YyrqONTd14AbLYOXdu4xkjpOwTwhRBJdFztV4H87yiJ-dqp6SWKlMktSKCybh16ii9A8Pp1BErbsUbNa3rOpJdANHng13r1B4GeNhhZr-7ACc5ut4tOp4FNvA7t1HyX3deZEaKtK8ziROTqJZhzbUPa7sPG6UtX16kRBRYtvFcac8fLJ7k36WB5IQUN3aUIoH7gUZRuyi3jgVDJX_8Gq0xNRE-aFn00Onm4LLcpMWwo-Ny_8WqdL4ic4pstXFHEwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g67oPA0tcC3Jg6OsmNxY6mM3h7lPi5vAvYSJVDRknfpIV015JTD2g0pv2ekJz60x0GB6WzxPdgOJkeUsrCKCyxjz8wX38mKp6MqiVzJoCbwJz_jPlj9ac-zqr0dvtnpk3wcxbdEyJW6CbTOO81y6dO3SVfewZdsdcjb2V3N3lTmq45dCLU6_g5p-3l3HzmoAfV9T9wOBYTAiVBTb8kALsmYp6Cd-KMuS4PpHCAqc3p522XwIXQELmGyUP0A30XGWax6bJTBoYOuK3pDw5KxjkhvSnvaAb5-Ekm-vlaZW2LHvYPDfy7p8VkU9AHElWgLO5_k4_4PTBGfSh23GB9sZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=HKC9WnQ1JHLw3r7OD7Y6-7mTES8KBqUT-xrGFFyGHlf6ba16JZMx0lbgGaqQe1pS4qedqOLhL-oBBDLBNhtX1Du2CzetU_fnNOFWfdrDn38KP0Dw_EUXG81Y4a_TQWLNTrMkfPzuoESaOOOz4xvX31VooW2muZ19RAsOrRs2u4mT9_7DLEJnmSGuI5M6mfQj7l-WI_NTNsdgzMAxBIQVPR6ubzQI46pdDU_twhWl0Llgd-ncSNb_UqVvRnXyue23NgAxRZyOOIAbtKRO9FYeBFI8aUc8CgQTRgS9lz8-yFHDvcgBfdzRT7QqEqsOZYk2T2RNd14l2i-EH6UhtseHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=HKC9WnQ1JHLw3r7OD7Y6-7mTES8KBqUT-xrGFFyGHlf6ba16JZMx0lbgGaqQe1pS4qedqOLhL-oBBDLBNhtX1Du2CzetU_fnNOFWfdrDn38KP0Dw_EUXG81Y4a_TQWLNTrMkfPzuoESaOOOz4xvX31VooW2muZ19RAsOrRs2u4mT9_7DLEJnmSGuI5M6mfQj7l-WI_NTNsdgzMAxBIQVPR6ubzQI46pdDU_twhWl0Llgd-ncSNb_UqVvRnXyue23NgAxRZyOOIAbtKRO9FYeBFI8aUc8CgQTRgS9lz8-yFHDvcgBfdzRT7QqEqsOZYk2T2RNd14l2i-EH6UhtseHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDsOUi49uqkvvdItTp168P5_y3a3S0H7as3w9wvU6myyzo0AC6kykK3sqNFM_dZ4R9OdvVVXyiwQpwaGaC7B8Fd72mkssKtRe9tXM2cmwGmde8KZXnYHkTAwVdgyOUc9e08UK_zY8FuhIVE_6YXsJNDbeKQlfKptp0CkCb7RZj9sxymg-aZkttmMukwBO2cYy1i-Thilm5_XsqJd9QCGYP3zEQ04nsKukgDOBdy24qi1kn-LoroxEItPT6MbmNuWRigX8tce_Db2uE7bfnjlY7gMU57iFCBhw0COJVsFGRamPK5G43qkIPE0JwPBxCHlPihm92B5rzdKmnIXhDCBBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=T1D6Gfm9iF57sN4lmEryRod8NZiRSg9luxWIGoBe1OJy_chSGp6QN1zE5joxX_mdVTUJLdsYTLMivJDIo4K6hZwNe01gphMZS0VV4SE5vLJ3FTYU5Pg_HtmeIYYZ-lNeMaX3izeSp0qEcq7d30pgwm2srCyhgoL_mDJdOFxRT_rClHeJKCyhNIg8Ww2vwtZRfcnhwnENjCxX9GuLR2GPkgI6M8uTGi1coZ2dKu45dppB_kLmCACSOHM6hhZsIq3j4W1AjQqRVMMeafMTHfueJ_gYjpLD_Rk8oYJtgXx8R1vgpxFnukbgE1Up-7kO9aI63BT_9FyAdq_EOK8de6ocBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=T1D6Gfm9iF57sN4lmEryRod8NZiRSg9luxWIGoBe1OJy_chSGp6QN1zE5joxX_mdVTUJLdsYTLMivJDIo4K6hZwNe01gphMZS0VV4SE5vLJ3FTYU5Pg_HtmeIYYZ-lNeMaX3izeSp0qEcq7d30pgwm2srCyhgoL_mDJdOFxRT_rClHeJKCyhNIg8Ww2vwtZRfcnhwnENjCxX9GuLR2GPkgI6M8uTGi1coZ2dKu45dppB_kLmCACSOHM6hhZsIq3j4W1AjQqRVMMeafMTHfueJ_gYjpLD_Rk8oYJtgXx8R1vgpxFnukbgE1Up-7kO9aI63BT_9FyAdq_EOK8de6ocBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=TbNjGlNtDW_ttSr-JLmamYeOir-vxxg7mss0Irbz2ZEbuG9ZLlsb4yB3K9N6zr8ys4b6Bp_NqhjrOGWnbdqO_y9cw2xi9Dqe-Bpn3LpLpEeMJ8J_byO5ihupuwlOYedvOE3yOogbnLqpLGtLb0Co2vkVNy6lVJeYaUqMbROo1DGMPFd7PqQUINSd-tUX-nKPC-xLbgvj7SuWgQ9yJ7WpVPJxI63VcUKtlyzXm5ar1KrR6CC59cq4XwDB5khgPoqB9_O1J_Pl769sut_RBp_NBcTp9TUM8shIVqgYwz2i0zEqRi07vG1mbL4U5QTF4AH1DbxTKjaPZv8YiZanZafaig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=TbNjGlNtDW_ttSr-JLmamYeOir-vxxg7mss0Irbz2ZEbuG9ZLlsb4yB3K9N6zr8ys4b6Bp_NqhjrOGWnbdqO_y9cw2xi9Dqe-Bpn3LpLpEeMJ8J_byO5ihupuwlOYedvOE3yOogbnLqpLGtLb0Co2vkVNy6lVJeYaUqMbROo1DGMPFd7PqQUINSd-tUX-nKPC-xLbgvj7SuWgQ9yJ7WpVPJxI63VcUKtlyzXm5ar1KrR6CC59cq4XwDB5khgPoqB9_O1J_Pl769sut_RBp_NBcTp9TUM8shIVqgYwz2i0zEqRi07vG1mbL4U5QTF4AH1DbxTKjaPZv8YiZanZafaig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDW0c1Swnn9rjevXqrTyhDP7BcXsuYGmuxdxKq2xniXL1A8NKRUJyoTReNs6JAmJXazGLfhEmsOLPhipLMRyeWP7Bb9yTOd9Qat3CWIYw6FK8mvqjn4L3T513WoH2Bmjm8e6-XHt7FLAlApJsBE79Z4wMaO5LHlOASJtCul36wr6lTt9B4wLeqAaAl69bRWwkiYs1HHFzD6nQ-9uHQY6MdVVtL9xJeI-Eyz4wNJ3O1IY9KnXM6XsrkpujqwVyV97WVNfLvaRkSI6Hyk2fo2A2PNiEzzDTGuXaZFaiwwsJe_8WdtW7T2w3FhcBsntFxfCxb-W9ye6YvvOUcMpLpzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPZYThiN_ebumfLUEl9DN428z35Y6SCkeUaJz5DQuSF4un4ezYIN86s60wbyN6WDAcVZprNhJ-PvsPzOAU6ChZNQh-hhU27BjCL_Ja2sknUGVgp5pStRKEwLc9NO2uKwfuFMJcNq0zSm0F9E8a4RNjn5ArpDyo72wzbnrlnzZ8y3PGLbkPrVtyo_3UIxTjFuV-jPQYwd9epHIpzc3Tvv2qF1KSyyKQLPai_6cgRNQrXIMoHPN4IusOvTDNWpPok9FOh1rXqc-9y6lbHx-GsOySgdEiRe92TQRqodDfr2FfLjHgrJlTZ3t8ry5MEeLdbTWwhwg1_ndzfTleIfSiexng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5zpWSLKtGJTveGouQ5YAJtz4dHOqQbO5ydxZDsWbd-D4h-P1uJaD-6-bv7WQHCeN6TlVT9LDIuNfXi2CgG5s2BpYdRYpKlwMX3PipXcg0N8sJ2UxK_0-BurOBpIgb1XVMlHBXn6iUWr3UV0vr2JsdbpgiPc2H3lu_nzO1oQcVc4vdzEsP_zOd9qv64HVP_f5ONtO8orbEw8sOKi8xn-lyXkDOL5KNoGGv2XCU7_Sa_olFPYDu-Q63kiO7rE_m1ihfBjC2ovADIA2rQgNZQdBOMufO107t_bdoGEQPggHKAdSlZUGOu0dAlI2zLSCXUWadC6LVUlZmgDVvyCKuW4Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=eHPGVTZfPuiEt1pUC2-sIEG7z0JdvIeU1Rre9of2JqtHjQz-S51Aw3pkVVckvhnJ84Po_TSzDP3yVxoehvMCvZBfsby5iNRkQxwPlusW6D3f9i75yCqUNj0eFnUE-gNZJlgClzzxq9XsMcKChcjDalOz7FydCdNMd_6ycUqzCovc1l1z7-UsJdMOOIfWVkjILUFQA7_NbgyXBkEvADk8nGQ59l6kW8VTXIK6tVV1v-gJKRwubVurt8k7Spm3kHyDlOmez66wty7zj_mNwKomWu1-sJkIJkHY0HCA4wItdqvWpQWRL4WaoNxPkmDWwHTtPMw8vUSoc3CqMLr28EjtFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=eHPGVTZfPuiEt1pUC2-sIEG7z0JdvIeU1Rre9of2JqtHjQz-S51Aw3pkVVckvhnJ84Po_TSzDP3yVxoehvMCvZBfsby5iNRkQxwPlusW6D3f9i75yCqUNj0eFnUE-gNZJlgClzzxq9XsMcKChcjDalOz7FydCdNMd_6ycUqzCovc1l1z7-UsJdMOOIfWVkjILUFQA7_NbgyXBkEvADk8nGQ59l6kW8VTXIK6tVV1v-gJKRwubVurt8k7Spm3kHyDlOmez66wty7zj_mNwKomWu1-sJkIJkHY0HCA4wItdqvWpQWRL4WaoNxPkmDWwHTtPMw8vUSoc3CqMLr28EjtFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=CutEgTS7LIH4s-_dLk__e57bm23AO4FMmwD7VwcMr5-Re9W6Hj3eYgvKM2JMZ-BDGl1PkagIF4vCNMbCKMGoqiXUsBMk4CHqzPWIXSfNnnWS_ljGYmnX8pl8FcaMLDwBWB6N9JdG5pMIAwehkY7F6We-xQgzyO8CGSV-O8kd2kMN6Ip-epxcNbvIce8CSja_qQ1JozQ2IWiwBS6LIWKw9XPeC2Esf5wceJRKrqzMC6hFzT5v8NdTz-IgKtg2Dof9Bs_pzAQkaIHLOouuAnz4lxTbNiarJ9byyAZv4K-lnZVsXmDH-5m6NHB6Gn3MtmEBz-d3I-q3feb373DjfDmzrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=CutEgTS7LIH4s-_dLk__e57bm23AO4FMmwD7VwcMr5-Re9W6Hj3eYgvKM2JMZ-BDGl1PkagIF4vCNMbCKMGoqiXUsBMk4CHqzPWIXSfNnnWS_ljGYmnX8pl8FcaMLDwBWB6N9JdG5pMIAwehkY7F6We-xQgzyO8CGSV-O8kd2kMN6Ip-epxcNbvIce8CSja_qQ1JozQ2IWiwBS6LIWKw9XPeC2Esf5wceJRKrqzMC6hFzT5v8NdTz-IgKtg2Dof9Bs_pzAQkaIHLOouuAnz4lxTbNiarJ9byyAZv4K-lnZVsXmDH-5m6NHB6Gn3MtmEBz-d3I-q3feb373DjfDmzrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=eZiCB05IiOLQKaaqF8s4JbfH81a00lcjMWS-v67Tf6zMh9dkmvnNQRzXwPSnzVwWrp0qPv-Tf1hRyf7izseHJOzZAlIIm-nUUDO80iRm0-yGgL0fqjbbX2x-00AEOVb2ulzfLGIVsTrBsPans_iXvYxvnc8S9P8rBoWdSeeH_kMZfmFFfzi3tq9VwPvYJybG4PXXvvb3NvIqJ7pcEHYiQO0Rx_9whP7fzLeipYtqZQTiOVBet3WhLcVhSeelDJguacK1x3PzTQhEehvRR1xgODNOgxOhPZK7dliU_KjtDehA2CLAbKJZZdWhAT86Rs6-IbXg1VeX56VJEQ61X_-LlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=eZiCB05IiOLQKaaqF8s4JbfH81a00lcjMWS-v67Tf6zMh9dkmvnNQRzXwPSnzVwWrp0qPv-Tf1hRyf7izseHJOzZAlIIm-nUUDO80iRm0-yGgL0fqjbbX2x-00AEOVb2ulzfLGIVsTrBsPans_iXvYxvnc8S9P8rBoWdSeeH_kMZfmFFfzi3tq9VwPvYJybG4PXXvvb3NvIqJ7pcEHYiQO0Rx_9whP7fzLeipYtqZQTiOVBet3WhLcVhSeelDJguacK1x3PzTQhEehvRR1xgODNOgxOhPZK7dliU_KjtDehA2CLAbKJZZdWhAT86Rs6-IbXg1VeX56VJEQ61X_-LlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-rXNOyd5WUeFqNPsirfNFbEOxAuZ4Ojga7lSvfalccTw11BDC2JvvZp4HHZvJEuEnaYQ8Pr9F0vSQuf3Q4fc3xeiIKTJElf6wC87Ymsd4-birL_iU1p1taLo74yz3WW-ijsr5oTzhPAjNZopGfPx0VIrsVky7K1ziLVh3yb4MzvclwGDQQ9DXMQ3-tcViuMN6Qi4w3ZCVma8nr0bQ4lBo45gQfiO5rUBWyP2E1J7EjU1-VLNb023GJqTCDuAC0RaMEZ9DN8G3q5DUag7ABKfVQe-R5tUa_gx7Pw6cIgbq-DuUOtR_m0ysRnm90zasl1Nm5aPbCqXb6zTTpJWTldZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjNs2-JiwQZ78Ihmgj-IVgnkUVf5Qpd3rVXd60yvnMypuoS9kRVk6mlRERwC1CjHnGrcQ9TkZg7HCHBvaqOMzf7djFTnpnZG6G-ciOSMxAkgEDc8hibSYmz4QBI5TFk1CjZAomgZHTw5iXCr_RKfAPF93DXvUJXQR_qp_BKntQneWrdPoFioFmuqkrfD9s-BnPgZO6NQT_VUvJB3kVZcniM5-rzY9Hud3q58rczh0WNdNicjmE3zSW6PF6P9s1vtwpV3J-pKw846JiwV2TmD1fEqO6T_YcBZFkeS3Art6K7j1gwuzt19loDyAtkU4RIcLXYmzb3L-EkF6Olimwy_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVjAlWD6Q5iuzIfCXB2Av3y9z330oDvKctCqYQWMYBg5lPLxpnIBA5el4KMPw3PwnSnWmqTIiGo1B0Pfhx01yfOk3yxFqP-yfvPLU-S1XjfziR6jh1i1uitxFeVvwSvj6nx5UzjIqaTxpLzOSlZ96BzGMtJxv1FcxWTghQ140Dv0HpuH50xeTLYqkd7y5FggZUE0sCyTMwdld3-OXR7qXAQvPb9jRkO5n5oY-L8QVYE2hbNuqArEymszofns5FiVhOfxTjchOfpEYg_WWIEI3w_Ps8yZ7Q17b0RmZEv3MjiZy2eFjXzPa2knuZlOlBf9HJAcZDbNsPJs_QmFigXguQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=TaXGRJyCM2mg9iFEODItjnTBBSX_P2iZxjUwDfuCWmqlj_lFl0tHe75T1DWFyKg3uetE0KVgxtf15NEALAQQpIPFgSC6PLrljcSJPPHLgvHpCk8b1oaVvvheITLaz7ZZD2oa_gsKGo_GBb9GExhNlxMwcdAhBOucMSfCl7F6_mnSl1Ie4wOscP6fQ2Ewf9FJ6KhFbEs0X2dnzVTlVBOYfs-LNzBl25A83ZOlyc1Xdyss9KFRPyWN9HRQaM5LKFSyQJo55U9Sr3IhnQv-ZDc1HcfkgpCsHFFHWK-CKsUz0PcvPdcHoAQRruZEO7vAtC6BSA-JkGXG3-hwXoXJhdHPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=TaXGRJyCM2mg9iFEODItjnTBBSX_P2iZxjUwDfuCWmqlj_lFl0tHe75T1DWFyKg3uetE0KVgxtf15NEALAQQpIPFgSC6PLrljcSJPPHLgvHpCk8b1oaVvvheITLaz7ZZD2oa_gsKGo_GBb9GExhNlxMwcdAhBOucMSfCl7F6_mnSl1Ie4wOscP6fQ2Ewf9FJ6KhFbEs0X2dnzVTlVBOYfs-LNzBl25A83ZOlyc1Xdyss9KFRPyWN9HRQaM5LKFSyQJo55U9Sr3IhnQv-ZDc1HcfkgpCsHFFHWK-CKsUz0PcvPdcHoAQRruZEO7vAtC6BSA-JkGXG3-hwXoXJhdHPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUIrEEfmuMPXeR2tEB8ak8csFJZU1eX7G0DDG0sLwDkNxysIGsUPWzN8SSZJewL_iToqjHjMtG4gHLUkdv28h3_zY1lDO6d8eJjadUvVqHiqPf7w7v1wdsnq9neN9TQuT8lYvmPn7tsF7oTPvDaLWHNs-iWlowUenq0L8I7miXx0AchYlTfl2Rgs1V3DQid_k8zvRwWdbIo-XLT4nTcUrlP8DKFuLg01u6SGuQzrkPWzHUWe3Wdb4joJVeopQuYec_QZXqlI27cchqt37BEEolPdeFEM2Qw9B29lCddoK9KZInKJ-h394fbMz2X8HQ2awiOivQAynJvEtnEAokYtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=gLtUHziEsihvf1euoCMfM_KgMb7FpDPn4zFegJ80JA3Ib1lrYTp3QeeLE4CnhBnoY6glOaiciYU54GkCdSGScQN5iu0fQNi_S7sfjAGlqgLeoeLPR2LCaZVNFQcGIIlUSP0ssgYoUeOMTn3vHVm9KTNwWeZtLc2hWnJUpp9HzBOoBTPHaTrha1sjmAHPrMfUEhP7SZB4qXSZhbbSjuh-HRvTB_E-3cCzSognG610ziitOvK2O3T-zxXtW51zMi0SHs9wUzu9SddM9Hinz5Wtfq-COe9tl4xKZleqrVS3iwtZYfbWR4551k-CRF3TK77WyNgfZ3HYnw-F-HHkeVUz8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=gLtUHziEsihvf1euoCMfM_KgMb7FpDPn4zFegJ80JA3Ib1lrYTp3QeeLE4CnhBnoY6glOaiciYU54GkCdSGScQN5iu0fQNi_S7sfjAGlqgLeoeLPR2LCaZVNFQcGIIlUSP0ssgYoUeOMTn3vHVm9KTNwWeZtLc2hWnJUpp9HzBOoBTPHaTrha1sjmAHPrMfUEhP7SZB4qXSZhbbSjuh-HRvTB_E-3cCzSognG610ziitOvK2O3T-zxXtW51zMi0SHs9wUzu9SddM9Hinz5Wtfq-COe9tl4xKZleqrVS3iwtZYfbWR4551k-CRF3TK77WyNgfZ3HYnw-F-HHkeVUz8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6y2MrAto26NN0br4LPyfnGLf8vNk6xHj9RuXTrciAKvHmheA956Tl_sLWnb17--8cj-WDFmLMBm3mROCKh2x3t5qaqXO8cdXkvxV51kb1gCE27hTdrKeh720DIR31duDVt27gbK-pF0OkXfznSmI26u5C3x_gvqrOTf2hEPC3k3FukToNmIjWHVqL4W1gqTLWNbYP0-z7eScxOTv1OD0-t6gEAyMyvDnXMQZuhITsmWAnZbwXZF7BRjbdeZjlOR8r8rb2-ymQx9Ms7rxk8zozobLG-_Mq2L6fYPDd7tdVZRfKPGk4aI_mhzjVGCQRNib9SsV-aBEkeue05u3Byhww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=cEwjzc1h-qfb7ofdKWvrOjrAK1yzM_ItZVkgbvjyX4J0Z-9kLj6RiKd05ScE3YpVoJgXNr-mXaNSpL9Ki6kUH_rxzwjCJuRKWPC74zFzOPIVdEt2HuW1FdD2f_q8S6E7rheScsWyoE6q_v2gjgHUFLeccca1P7Bseogkzq-bOkxY5s9gr3GiWplmopw6447NA61x-1MzJhPXlEUY5HVCIfkyoaQSaIGUc4Yklhaa6NBjrNb5nuvkLtWJrMrzsbklfDAVLqDkphCYItvtWXEitTkKu-tM9Q4eZxT0X0_EZw3YgvNIkc5-Ghsa8dpAKmo8ZE1MKYiWiCs08ARZfFiy0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=cEwjzc1h-qfb7ofdKWvrOjrAK1yzM_ItZVkgbvjyX4J0Z-9kLj6RiKd05ScE3YpVoJgXNr-mXaNSpL9Ki6kUH_rxzwjCJuRKWPC74zFzOPIVdEt2HuW1FdD2f_q8S6E7rheScsWyoE6q_v2gjgHUFLeccca1P7Bseogkzq-bOkxY5s9gr3GiWplmopw6447NA61x-1MzJhPXlEUY5HVCIfkyoaQSaIGUc4Yklhaa6NBjrNb5nuvkLtWJrMrzsbklfDAVLqDkphCYItvtWXEitTkKu-tM9Q4eZxT0X0_EZw3YgvNIkc5-Ghsa8dpAKmo8ZE1MKYiWiCs08ARZfFiy0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7b21bh6R4HgbyKleC5GUHs3q0_PTPTNA0qfCxhPGQuekKNTBbY1IGG6zJwcPP_nGmbiHggead5GRlXF5lNy3aBzPzGQDmXeBToi09L1Awjr734pnnfjdje2dRiUIEsJuo6odOyfAX03uy-LyK6IFcgVvri0XXpERI2f7fXd8WTeJ3D-QqghzAcpboSExsbSwIOj3c5vo8QP-Eg0MgbGrk7CXRXFAEoPKZMFEbMTn-CEfkN44jRjAt9wyEMEM7rNorrtSK1ukLkB9RaG6poCwoWjDAK4FiMmDzT7Ic__ZhGom6yxaoavM5bMsIs6_IfWnGV4VUQcmY6qryuD0ZOi1wys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7b21bh6R4HgbyKleC5GUHs3q0_PTPTNA0qfCxhPGQuekKNTBbY1IGG6zJwcPP_nGmbiHggead5GRlXF5lNy3aBzPzGQDmXeBToi09L1Awjr734pnnfjdje2dRiUIEsJuo6odOyfAX03uy-LyK6IFcgVvri0XXpERI2f7fXd8WTeJ3D-QqghzAcpboSExsbSwIOj3c5vo8QP-Eg0MgbGrk7CXRXFAEoPKZMFEbMTn-CEfkN44jRjAt9wyEMEM7rNorrtSK1ukLkB9RaG6poCwoWjDAK4FiMmDzT7Ic__ZhGom6yxaoavM5bMsIs6_IfWnGV4VUQcmY6qryuD0ZOi1wys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=Z-ucyzH8eC4z7714bqm8hvSEiLlFDMckl3rWRkm-GCgRwuMxXpyvBWOnRTgKjvM2SitZ9UkjCL2PPHolqqNJs0rZq3a3mgN9Rgl2LzdBDRuzqulpffD9gaOPnfc_dGvpSYAjTSeED9n7GuK_DsfnGv94kWgCEup2O-5ooz9bwfBuECaH2pSR5VcJhg18Bg2e2hE6MjBJGke3_U2UVoive4rs9_g-qJG6GlHi3UYZY3CWK-4cV3CjtSt6nwfU9mdUWaY6-uRd3jA70rjaNUortrvgGMyzPZtfTKJKsJeISJQ_F_85ei4_pve7ZEB4PGZoctvMt9sg6DHvFQ4i6b-JHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=Z-ucyzH8eC4z7714bqm8hvSEiLlFDMckl3rWRkm-GCgRwuMxXpyvBWOnRTgKjvM2SitZ9UkjCL2PPHolqqNJs0rZq3a3mgN9Rgl2LzdBDRuzqulpffD9gaOPnfc_dGvpSYAjTSeED9n7GuK_DsfnGv94kWgCEup2O-5ooz9bwfBuECaH2pSR5VcJhg18Bg2e2hE6MjBJGke3_U2UVoive4rs9_g-qJG6GlHi3UYZY3CWK-4cV3CjtSt6nwfU9mdUWaY6-uRd3jA70rjaNUortrvgGMyzPZtfTKJKsJeISJQ_F_85ei4_pve7ZEB4PGZoctvMt9sg6DHvFQ4i6b-JHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=QB6pg6PKhGMdQBBen5PVr8fc7vKvjjm6JKhlCnyOg5GVeodqfVgCeuEOSMnQJF-w6GJBs5zgiZEWWd1-JR_36kdd8EnxTDbIFzpD3baG3wMzhO6q2xYRzcddgmqJW1xH8bGKcSggQRtkUOLNO6JRGvWjSEI6EhLe9LeoKxSxgBHlCHQ6Fj2Rgx8KKnjyryZrq_SSbOFFRyQbJEzdfyzATHbDz6Xa0yWn-xgP9zxXtzRFLvlOhmXYOwYrP4-ZXCRC96Jo4C06W8VKGb-fYTstsYYrYhXlB4JaST4-OlFEbqvM_gIbuK4gcus6mZD36t52HWlqy1KwiDI_dCGj_FnUBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=QB6pg6PKhGMdQBBen5PVr8fc7vKvjjm6JKhlCnyOg5GVeodqfVgCeuEOSMnQJF-w6GJBs5zgiZEWWd1-JR_36kdd8EnxTDbIFzpD3baG3wMzhO6q2xYRzcddgmqJW1xH8bGKcSggQRtkUOLNO6JRGvWjSEI6EhLe9LeoKxSxgBHlCHQ6Fj2Rgx8KKnjyryZrq_SSbOFFRyQbJEzdfyzATHbDz6Xa0yWn-xgP9zxXtzRFLvlOhmXYOwYrP4-ZXCRC96Jo4C06W8VKGb-fYTstsYYrYhXlB4JaST4-OlFEbqvM_gIbuK4gcus6mZD36t52HWlqy1KwiDI_dCGj_FnUBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVR8th1LdDQrx3m8tDKfStCEDuQQFE8CZQafFDT7vwlQc6Q_5kKNzbSFJKSeLn1l3YUuqsGShLgdQJujaXWjrQ8IEXq-f0NJFa8MaW-iOzqg2F8wajovT7dihYEZB2bO18haQL_CwWrFjbuutLhIUwJqQZmMukp4d2XremRhF-RDhFnrSMKH8S_4NdyX90OpNIGxWF4P0AwcMwzU6T20dt6HxPpS_qlnevho2XHL0Fb28iPxa_TzYP_UPvWq4X72hJlrAWuYGvbQzU4tdNVJM7Ie-MWtqrqqG4ULmuvRzDV00aByXq3STJ6IYD2ZqyJBlz6dd3JA3hQKfDoswwjK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=R1W-4WYnJwSEQ3oVZc2ACRAvoN3bTnM8TxONjtgBsZBj71l8ZKXQKGl2kqvVC99qyJ2W9PbTnWJroy3lPdPBOy28fACdHNxMhHcsTgizkNfBYA2IwL0npjmbaJ9fP4khGDSrd2ayfNUWiDMQ6WRJoEYzoFq2IQwQuBtFlfVSWykYpmJBqBfoIp6gsm00xRicPl-hNNRCr4BJ7wmI4CDTj1fQAREJvB5CdBXm6eqZs06k1rWT5CbdhY9Zwm41e42K4UYvfvcDp9gYMd5jTeydXV945QyRBhDBDqscCtaVvOTNdWRZETvrNgS3mk69OGtjNfNGsTraD_jUgVcn9WhhNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=R1W-4WYnJwSEQ3oVZc2ACRAvoN3bTnM8TxONjtgBsZBj71l8ZKXQKGl2kqvVC99qyJ2W9PbTnWJroy3lPdPBOy28fACdHNxMhHcsTgizkNfBYA2IwL0npjmbaJ9fP4khGDSrd2ayfNUWiDMQ6WRJoEYzoFq2IQwQuBtFlfVSWykYpmJBqBfoIp6gsm00xRicPl-hNNRCr4BJ7wmI4CDTj1fQAREJvB5CdBXm6eqZs06k1rWT5CbdhY9Zwm41e42K4UYvfvcDp9gYMd5jTeydXV945QyRBhDBDqscCtaVvOTNdWRZETvrNgS3mk69OGtjNfNGsTraD_jUgVcn9WhhNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=urVps7jiQ6CPduVfaKZEUrwm_NZBTb8aRHNIy8rKx0DB0fnJiN-jSvdavtjFs8sESJnQ4vGdmCq7W1lApQpfhH4gTfc-E_JBOyoQto4qzQGZH-V7adpKtu48jgZJ5OOYVxWrP0ONDReQcqbukJ160a8GJRmU0gLV0_9AUyrmizFOzwvoqnu4ohSqAGDPm98NTQv1ThX2y6xPLKpmx8vw-5oQybDz1XYLFLkvebB382wfJQhYOvQwFhUmpAoGe1muKpbclRDEMgbcs_5RabjsYDj4a9UCRe-OMyyDfi8qYwCFL9RJeJWIjmcpq8HfGuRumzAxG6eslKp9fuHPdPyQ409C_mCTo29b33TD-YTVzRVtW-PM4OdtT4CFFg_gq2awn6Gzw1yDAzbXtbczKLLqC7Qte1J_B9KzbpDXTqCDGE7ApQq-kB5ygaqhMxSX4B9z1qJd9K06DDEQMI_dP3HhNbtIqUz4d9-CmsNVcRENSGNvKVXxy0jNarutfq6NCrNLliXswSnXLeUX65vUdzbch86oxd6fiLJg-k-g_9kyLplJR8-8TWSsjawPTpiIJz3g6jQB331B8UXmva3h_FIhbwk-M9WaVN5IhLo9x_6EeE4VfAk3ckXrkZc83fNLSlmBjYp0GroNXBefC2e82YXHLqT3kW0VWOHzs8yeZLGOjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=urVps7jiQ6CPduVfaKZEUrwm_NZBTb8aRHNIy8rKx0DB0fnJiN-jSvdavtjFs8sESJnQ4vGdmCq7W1lApQpfhH4gTfc-E_JBOyoQto4qzQGZH-V7adpKtu48jgZJ5OOYVxWrP0ONDReQcqbukJ160a8GJRmU0gLV0_9AUyrmizFOzwvoqnu4ohSqAGDPm98NTQv1ThX2y6xPLKpmx8vw-5oQybDz1XYLFLkvebB382wfJQhYOvQwFhUmpAoGe1muKpbclRDEMgbcs_5RabjsYDj4a9UCRe-OMyyDfi8qYwCFL9RJeJWIjmcpq8HfGuRumzAxG6eslKp9fuHPdPyQ409C_mCTo29b33TD-YTVzRVtW-PM4OdtT4CFFg_gq2awn6Gzw1yDAzbXtbczKLLqC7Qte1J_B9KzbpDXTqCDGE7ApQq-kB5ygaqhMxSX4B9z1qJd9K06DDEQMI_dP3HhNbtIqUz4d9-CmsNVcRENSGNvKVXxy0jNarutfq6NCrNLliXswSnXLeUX65vUdzbch86oxd6fiLJg-k-g_9kyLplJR8-8TWSsjawPTpiIJz3g6jQB331B8UXmva3h_FIhbwk-M9WaVN5IhLo9x_6EeE4VfAk3ckXrkZc83fNLSlmBjYp0GroNXBefC2e82YXHLqT3kW0VWOHzs8yeZLGOjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=chlU3GqPvz4xUnD2A728ekNnYlUU4Bl5dl_DqPNvIobFegqkzy9J-TnDbb8-H6oK5-9Bhy67_wpuDDjkDsArXLNYKjrPOHUl3M7a6D2FVYSSv6W2IaAZ929wpidF9gGAM_0-VE96lEN1VT0LIcMQmJkndfZuWhXDBtKF3drnSrU2F0VYxEblqUAIe9PM__gXiqvjos5fFfXpS3nilWjfheiLx4RM5mfEK1R1uGlcdbrUS3HW5QelOzX5iv1F1zfeGH-iSAnsf2ASDRwj86I9Zvp5YFaqmi6UNjUhRq0GUQtTO54-V41NVD0qqk7it3_PcxvX3JSFLt32q7J0vV9GYSlmJvQ8Jx8UX58e0J2Yjl0VbH9koe02rheHL4VJn-VK0bU7umVQvfoVbJTfLx-JhYVBc5fR3yjElbvB06BUQxPKF4mn6Y2gETC1eCJ6IUN8oYUuiM7YMYKDnU7aRDflR8Vkqa7WsDdRMhduSYu7Fjr9fB0okOFxiLaXcrkLEmZE1qCOUSS1-pgfi8OP8QfY-Y64EjHVfG8EbxMmniyMCWlr62j016ASp8meLxX2xyQ7Hdy3PziAq8WeOk5OfHhy4pOCuuM-x_rvT8jPEQrpL7vw7P_hjVNHptCxQoKplrS6ziVMiWw3u1KYKe9baRtNX-1TFu0UlnfYYj1aMS0vHnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=chlU3GqPvz4xUnD2A728ekNnYlUU4Bl5dl_DqPNvIobFegqkzy9J-TnDbb8-H6oK5-9Bhy67_wpuDDjkDsArXLNYKjrPOHUl3M7a6D2FVYSSv6W2IaAZ929wpidF9gGAM_0-VE96lEN1VT0LIcMQmJkndfZuWhXDBtKF3drnSrU2F0VYxEblqUAIe9PM__gXiqvjos5fFfXpS3nilWjfheiLx4RM5mfEK1R1uGlcdbrUS3HW5QelOzX5iv1F1zfeGH-iSAnsf2ASDRwj86I9Zvp5YFaqmi6UNjUhRq0GUQtTO54-V41NVD0qqk7it3_PcxvX3JSFLt32q7J0vV9GYSlmJvQ8Jx8UX58e0J2Yjl0VbH9koe02rheHL4VJn-VK0bU7umVQvfoVbJTfLx-JhYVBc5fR3yjElbvB06BUQxPKF4mn6Y2gETC1eCJ6IUN8oYUuiM7YMYKDnU7aRDflR8Vkqa7WsDdRMhduSYu7Fjr9fB0okOFxiLaXcrkLEmZE1qCOUSS1-pgfi8OP8QfY-Y64EjHVfG8EbxMmniyMCWlr62j016ASp8meLxX2xyQ7Hdy3PziAq8WeOk5OfHhy4pOCuuM-x_rvT8jPEQrpL7vw7P_hjVNHptCxQoKplrS6ziVMiWw3u1KYKe9baRtNX-1TFu0UlnfYYj1aMS0vHnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgi4KC5QqCWVbZT7pwiaF4_jJTywG94Eue8UwXRQ3-aX0MYLikIXembe9MJTBuMxTePzj3vYPE5xXitI27WSnO7MJNA7g3TS8OsTQU-cUInBrRhhPIsu414Qb1iu51x86NAr_KU0qcg_2P1fjDjO6j6WvRaM3onvULVq5NUfLG1QgyhnIZx2Dxc-5QkNlYP_oqdWKfXrYE1n8u8BmTgXa-1gQOX13aV9RU-hYOw473NTPsEAv3gi3BeV0-NGHWw3NWUSsgKuVUsZq2URA5HTXaPctfrKne5wmxCEmkNayKKVjvHABzXiHwTodyOwLkV3t6uiFgzYrKPfDGOGvNhH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgRpBnIL3LG7x-8hmSe93y1vCEk5Kw2oNYta8Uk1IotmNGjEBWFjC7DisDw8D_VA_vwUHCCiGVNjD4Dyy3Pzc80wnxWpnGFkdowtNPXvMhmFlEksTiNjhgfHDICBmR87vB9nnTuM2VNtmzbsE0daI3XkptRlK4CJTwy7R5E-rFB1Kh-Uxa7u8--5w0gYpYzWTv-nS-kfHWY47tJviBIiKJRqI57g7qBnvqRY997bycejYJslDKGI8qSb2uRNHyAm25OW329zhVHFRgaLA0v6Q8R15Kq1xIQWzcLnBb39VFCOLQByTpNruDhm-L13w7p6AQ-2WKcKeIuDCDRt0vwORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7cY5FQjqKfZj5GwZbkP_tgYdzoxz8bsoeY5F0UvQjGPAxJO39zA94ZQAi1S_QMiTTnTFuOQvtYcfb00t2X9d5f-dTbyWrVQiXsAqzID2P0Z1q16s9jAZ9XxHdOxn_XUAs6S-FAw89TN4ylCc8_eWlpdV12xq6tSW7tQsXyzMlpJ_neQ1A9um0ZrTVl1TbkSu1AaKOhP_GYiTyc8zoix90O8oUPMqav7QXZrI2ObIY-WJZRWb1giTaR7_mitYCsdnaBhc5PFaz765ok2qIBRp3qRE5Vw1EDXYf1M80NB3Uplpc1rgJDcwfykQ77q2J0noeGULa9muSEOubgLFRfFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=RCmC9u1qEcQZwS6QbI4EVQMWPBDGSDMEu0aeApKYBskFsJnaOck54rCIH666OddelIipqxvLy-6Yk7Z8FbLWaRqmv301zFdzD-oYWAlVF2HtdJTWqWdclZ82KVgDuuddA42a52jKVS8WxcGUb0ZOBi-AYOeI4tKky0L7P0ykOVxV35xzL_Mv6fq2Tb_dREzsKF2wmCvk1CTzjqnZra_3RFYobHngWWYH9c-j1DmZ7S8hGAqZhSuV2ItbWf2-bmp7HSZFT2PJiwNr0owGlCSj-Ikxygu68kgD1GDexAToHCaPqdtDm-lFki37p2otsfHwmB4wOowPxiEIZW3k994o4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=RCmC9u1qEcQZwS6QbI4EVQMWPBDGSDMEu0aeApKYBskFsJnaOck54rCIH666OddelIipqxvLy-6Yk7Z8FbLWaRqmv301zFdzD-oYWAlVF2HtdJTWqWdclZ82KVgDuuddA42a52jKVS8WxcGUb0ZOBi-AYOeI4tKky0L7P0ykOVxV35xzL_Mv6fq2Tb_dREzsKF2wmCvk1CTzjqnZra_3RFYobHngWWYH9c-j1DmZ7S8hGAqZhSuV2ItbWf2-bmp7HSZFT2PJiwNr0owGlCSj-Ikxygu68kgD1GDexAToHCaPqdtDm-lFki37p2otsfHwmB4wOowPxiEIZW3k994o4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=fbkIIqaWzJcKBFvCXy-C2SYSVcJMIKotZ_ysr7MVwTmo5lwyNcLrLrIYd2FyR4YrvI8dEzjbZe85feHA1STydlxdvo2psJ3nnYhKS1emj2UM_M-l0jvDYmjRl4dPamSb98xUaQdaZ1F0KMBiPzv-LQKJmWNEIMo544_ZSgjrqAzKQ6xyT0zYvYxesklp0zVzStfUkZzcoQRphv28hnZeewGF_4sHzVP9pSX2u-p6p-xC2b-R8EEVmVsrQOJ1GzcTn_T83mGzSU5bv7xVlBz4iSr5yWjGf_kmE6rsK0BLMri6mMm0vYD9cjhgAvfw4XPcz6g9LRXIsRQHnSm83q9w-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=fbkIIqaWzJcKBFvCXy-C2SYSVcJMIKotZ_ysr7MVwTmo5lwyNcLrLrIYd2FyR4YrvI8dEzjbZe85feHA1STydlxdvo2psJ3nnYhKS1emj2UM_M-l0jvDYmjRl4dPamSb98xUaQdaZ1F0KMBiPzv-LQKJmWNEIMo544_ZSgjrqAzKQ6xyT0zYvYxesklp0zVzStfUkZzcoQRphv28hnZeewGF_4sHzVP9pSX2u-p6p-xC2b-R8EEVmVsrQOJ1GzcTn_T83mGzSU5bv7xVlBz4iSr5yWjGf_kmE6rsK0BLMri6mMm0vYD9cjhgAvfw4XPcz6g9LRXIsRQHnSm83q9w-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGe4Uryobs4VAakAOHw7_0Yn3mcGcxOToTmwL764MjA0Czp2j7kuJGluHGYrhVvF18gd3VpReZ3irAtKgu0mHpOAvpKOhor2EVTHZpCYY0Kfne1mSa8bKa-R_mfU2H1W7xoLueyRklUcEX4jBj16pETAQUja6OTu_ujhN9ff6oNxNMJCrBmP4QANioDLO0V_cA3rZf_3rF_mT-EBhsmwq6HUgIj-kySXP3JblqphTCRZ-RdznuuAaM_qsLqC9X7rTz6O6WV7qmAEEqCKlBUaCLFINv3DFWpUzKWa8G6BdVRy2YiFAdp812intBIujJ3073NLaPKQRf8y2-D3KRBhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNl82lqGnX3CD9nC_e_9c3aPdbfKfgy1LvD7A0Pwfa5NPXX4tk6gHk-hGnZ3dOy_6NVec_nwL2K28QWp4jsZF6CH4IaEWjsB0ATm7DMdiPtx-KDUNRZ3CHcJCf7hSfSU797NFoJLcAn7AXCN8WfDnhd9S1qV9C-6hQQPogiJyIGt5nShTEJ2BjjUyNtQBtC9HThh2siYjhMPHeQPAG4mhbRtkAmXDzfkj673kFYes_sazapXa4iRe3BMovCzzHNe80M8iRGqkIIB6d_5h998Y2hvm06dqcOxt7HzZt3prcBJvvHsI6eTFR076TqQe49aeqXVzSeZCsAumUzqE5G8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwFe45ZxFGGZEhJeFsU_rX7JAfQ-GUyfnDqvA4GrRVk8gRHW4A4wGlh0nSW3k6C3tCkBL3bZS2O2dcVGvanP8hdGkZra2G3vR2kdYxb-iTkFHsxPREOjPVjzDkgbwVkPd9B0YFCe0K-yh06XkorWxLDcxNZXlnTUNwpCK1hhDnz4j5MkKmgENKHnYlbVnENQ3TZLyEft5AyxDJfKFltb0bMN4o-9rnH-PWQmk6FcRmJP5gi56FGUR8HLlyESkLtaqUWiOdPVcwUXFVneYw0SeMrVNmfAh2LNqjpwkprcBZ8jFzpqqcwm6zoLOj5KDRilTf6tACeCERZspL9pEDLfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=ivBZbeVw4oWQUYvG1ZFnysTjOwIJVSsqKcCKtB9WRdcPyII2mHiz8lPPEEILN6lKMu8QqnH4DQQFaB9JQw1bW_HIpHkWlAFWt4KpAlohyLxoU-EkjThrvfEuaz-Dxm8geH35Ix98h6jSVMOS2yRU71hFGhA59k7V2jhkY9DuC2yrZ-D4WUy3WFw02NN0HcvNGhM0xIQmANNt-vYDiN9ZDGRSs5Bi4AXIKp02Qenepjx2QKlNHEs7IJloW8B8r_5NlUKFcJQo_zs9lVcQKs24Qxlms0aLYlfTiA5OTuPmWx_1-tXPcNFKmGXXLXZdENIneVBEUO5os9RxD4Vk1IPkeLEMtRg9k31YMeTsux9P5l5BIYchLIQoK5_6q10O2bk8_6p4-HYNaC3w3Hu0CAKvCpaS52Q5uzn8pMl3ld0vEUYao-zzvihAeo0W6Hw5M5RsDPFuj3ScDpHsJTjkaHR3d2CWzWwX4cxJEfuWsZ2IlHPvg1vG9lWLdtmcXa0XJU4D065bo87e8GAisxl1O9earDpxnnxUwCR8sP_C2-fpZndj3Et5LXXSFRbhJJq-_DryiWn4bBGWvEpo-rVOgh6URoe9sQ_tciultr7fpscnCajN-bXpWjImaH0OJ5DFgwuXj_MeHELAD1NLZQTK__fffq_pII3pPXkLyrlPWh-mkzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=ivBZbeVw4oWQUYvG1ZFnysTjOwIJVSsqKcCKtB9WRdcPyII2mHiz8lPPEEILN6lKMu8QqnH4DQQFaB9JQw1bW_HIpHkWlAFWt4KpAlohyLxoU-EkjThrvfEuaz-Dxm8geH35Ix98h6jSVMOS2yRU71hFGhA59k7V2jhkY9DuC2yrZ-D4WUy3WFw02NN0HcvNGhM0xIQmANNt-vYDiN9ZDGRSs5Bi4AXIKp02Qenepjx2QKlNHEs7IJloW8B8r_5NlUKFcJQo_zs9lVcQKs24Qxlms0aLYlfTiA5OTuPmWx_1-tXPcNFKmGXXLXZdENIneVBEUO5os9RxD4Vk1IPkeLEMtRg9k31YMeTsux9P5l5BIYchLIQoK5_6q10O2bk8_6p4-HYNaC3w3Hu0CAKvCpaS52Q5uzn8pMl3ld0vEUYao-zzvihAeo0W6Hw5M5RsDPFuj3ScDpHsJTjkaHR3d2CWzWwX4cxJEfuWsZ2IlHPvg1vG9lWLdtmcXa0XJU4D065bo87e8GAisxl1O9earDpxnnxUwCR8sP_C2-fpZndj3Et5LXXSFRbhJJq-_DryiWn4bBGWvEpo-rVOgh6URoe9sQ_tciultr7fpscnCajN-bXpWjImaH0OJ5DFgwuXj_MeHELAD1NLZQTK__fffq_pII3pPXkLyrlPWh-mkzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPh4BeKiZxhhEb6nfXcCxuHk7N5IrSQhjai-g0aXntI3a3B6JgNuo_4fo0u4q6e6IxzbAyvfZDR9bmk4IuJxzxA8DoZHgHsFLRtQYEk4cSPvEe7QbZD7GPKLEBF5a9UKYjdzH8Ztp9dJrC0dgD4VVleNACQrYFzYFphiAz82-jl_Q7q7zcXXwtJX5W1xVhF9sNLdiURzEVB53yCluQSc187NtQMhKo5QtdIk25P9vTtlxdaHmQRp_TOgbFTJEOvNo85LPHhczs55Zfnpl5F78P4ssjGnXXmszDQgjb9lybExmyPqQOdUo4Tw3kKa5xXQGNSXowCXCAHOP8J4ryYkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=CHOTBDzDlZk3f7KcWTqOoh6EQDqb_TsmgpABHYkUYL2jsKIHAwfI8YA73q_RF_yWO7577Z7rcePk4IpASMUiOyk-AtZYVKOVwJUyqNz2Wk43hAXcUb6n2wVc5rQxwFS_tpyW5KmU6__hgGUUf_LOEL54GPjw0HSrlFXIIKTTkrhqJge6__W8Fmzrxy8DUDqWFpmXONMozOtOrnI_QTQJU6i6qkB1LwAEuchHDK2cs9tsUV4E6PeBaNcdj8CBdLJoaMiuN99xFwMU_CLTKbB-dpaZgayLjafmg0KZtmpzibXuPK3coWgrCxdsg8y50zijtY2O02SLg5R4JkDDR1tGZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=CHOTBDzDlZk3f7KcWTqOoh6EQDqb_TsmgpABHYkUYL2jsKIHAwfI8YA73q_RF_yWO7577Z7rcePk4IpASMUiOyk-AtZYVKOVwJUyqNz2Wk43hAXcUb6n2wVc5rQxwFS_tpyW5KmU6__hgGUUf_LOEL54GPjw0HSrlFXIIKTTkrhqJge6__W8Fmzrxy8DUDqWFpmXONMozOtOrnI_QTQJU6i6qkB1LwAEuchHDK2cs9tsUV4E6PeBaNcdj8CBdLJoaMiuN99xFwMU_CLTKbB-dpaZgayLjafmg0KZtmpzibXuPK3coWgrCxdsg8y50zijtY2O02SLg5R4JkDDR1tGZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv3kSSrC4aIn61dVvxERH1bXJpKyWxstHJs1UV_omccERmmzQmLaNyo6FtMbh_bXRxRFQBXP2nTloOKwMYf8OZYNl0Fw-lvXk-OUF3fvGpRrt4JD5vC1rIkChr3RXIlQBKbAwyWKjqBr5dBFJGIvy-8CwpS6sGqKFuVKWly5rhr7jfL9XoGBpVso15P69qc-P1CMq8WXBgCspfAU6WuHY1s6Wb8MpwcLkxQrCPx7xf8k8MPdYegll4U0PFKCfr1ArlNZaaFLEJqoa4gXhO2Lf128MDTfyygf91Qfw6kSmMXy2SC7PqC_b0LNP7vZbfRK4tUndLRCXP6NGNJX7GkcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HfSLoFIQYQMbD6ARr9mGy9ervAZ2Z--jbtAz2O4lSbpiVt5FWtTwLBM0DNmWsTrhI-cgTteL0F1LIxjVKOpEHTJ0ByBgBi47nsw6qA2Ouly8o1NHa7LgHUrDQBJfo3aG8lYLgNzbAhiAvjfEd93Y7vlp9u5xKJ2rGNODAhrXfJ7mY2B5URScUrefVYluU3Y5GOknwvWwLsQ0JKETbg-ywDTexfTmkLIAbxqMNuCA0nvUWMkZt_c6J_9c1s0Ag5razneWvSDVexUxGECLQ9y8Hp07e7LPex6h-o9ioDOTAoMRoLIupD-3D7r76uKdgm9kykY5ioI5M4KfNXmUKyJYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f9b7gmxMDzcqdXgKmw4erRAAqL96ghPemV9ntiRG0F6o_3QLuCEXAQl-OIQ7FdzeWe-mpMpbh_VSj3Q021tyhRegcL-3uVT2HMglIAWarRGoJmtpM950EBISkPRY-iYYWUTQYj0nka9x6Cu3pY4UuqGCQs4VUvjcOPyQfI_KEfXeACX-4nFi9kcAoVt_FXuJekBPbWk2qlrgAqdM1ix-gH09dEigLQu56VzzCB9CBOAuPiCnczwtwSzLIKF04kYIyomFyDS1tZ0jpG-O_8Ip5lNxIEn0unInH4HklrPaLrCbewKJK9NuTnVaXHKOwRRbpKElmlZrcGMdGqIj6XM4rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=pCPUPwoa3cs3esh8r3FUySI1VeQJ4kGDJDmzt_B_KD6xJC_uG_mLpTKSd-45T2dekntDhOJcnfBRI9vf02Z2s1PGEQa9bnbO2qFkq2Z6VqLZCjrSPR2bUVBlNBXBl3_aliB1Tnf1wJhbuIrdGB5ee73MRugkhhkJKmbelUJhlV-ezdrfJhINqeUqiB65Fme7UJUlvvENyWeqGCQZKPP2ibC-3gfLlOb5tc3aIXMFcnyzuZ92nwfY6HYVd4jtlL2QvWGvb1mVWOMH97lLKbp5UqflAJ_yKLvt1sNgDjJzgZIvdnIs_ji-CdNQhZx_XRher1DxIhJopHoZALTowmEYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=pCPUPwoa3cs3esh8r3FUySI1VeQJ4kGDJDmzt_B_KD6xJC_uG_mLpTKSd-45T2dekntDhOJcnfBRI9vf02Z2s1PGEQa9bnbO2qFkq2Z6VqLZCjrSPR2bUVBlNBXBl3_aliB1Tnf1wJhbuIrdGB5ee73MRugkhhkJKmbelUJhlV-ezdrfJhINqeUqiB65Fme7UJUlvvENyWeqGCQZKPP2ibC-3gfLlOb5tc3aIXMFcnyzuZ92nwfY6HYVd4jtlL2QvWGvb1mVWOMH97lLKbp5UqflAJ_yKLvt1sNgDjJzgZIvdnIs_ji-CdNQhZx_XRher1DxIhJopHoZALTowmEYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2oevg31Ad2mHP0a6N2Vhvm1tqOfTdVYHZUfVUfOtku_3Vb95R0XyOWlmTlm0RiK4BnAKIe3v9MUCe39nzmitWZbGA0EBNimFC4XTq58FXxslcmxnZ3AMh2FmVANyjwoCcDUy9XsVQG9zieONjAu3cltHrw2g94L5UwGeUsp99cCIG43lvZbhHKPxJPvnG4S89T9cuu6MSOKQ_UrWZGyvTSnrCencUxz7jPnFIrNodcBApBpZ9WwQiFcbYCkn9JJ9PBE5Dx4hzC1-LP1sPIWFNNdMMEAMqXe3CPLmF8NoAvtTFPA5VSeNI15lc4ftCNjYwCLbQpFqS84gHsFamEzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki1zec84_mCVOAEhArp1MuureYRx_FN45NcUb5XmRdcBAOhtivEWF8S8Ojcy3Uf_eh7uIqMXfGaM3FX8xgQ-8oHiiOtZIjigxgreIHy2yIlDByn9x89xwuSpgazBCZquVed6qhAIRQ_KDVBEg92z3zZWvk4l7tBKtmOUHQzxeCVjEO4SxthNXvBPmUCmps5c2AWIeniMbtYqpIWrioyQ7NxdycRc0Gj_FVMZu4H02S3DHVZzrxUcA1KxQz5HLVyAtWfe7JZYGHKm8hWd7q8Sb8LMMs-7nKhUH5hudxYil91ZJJ1l_kHFMaVx6FdDqCwFqGY3cUhYZeahj9H4iFeflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwlpgIef6Qs8aFyBic6mr2vCWecbupF756AO9YI4VlPrDqrBAH-0Cn3jODfLNpjRbp8-qiXY8F0ofeDmv1FXiOjNNm7EQokmh28ecKiC1xT-bAvH0QD2-BseKpj3RI8UVanfi3acLh5x6cjZh4eZLxqneY1W6wtwWmRTdZwl3DRf_AloWKfxTkrNmDlgJMCKyf6K6NG0XHLVrS7izgKjhgt0vKAwAqK7rvwn4Q8CC3dILlAQEz2yVYJ5RNsvSo9F7CQutMtf1IAOEIRp_UBiX5lraHwOY9bBFkN0xw52stUwhMgCez1Q_Mznl-TGDM7acANAcxqNvsIzu1va7vZZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BC3_FbFh2jJaj7uXVgNmk_nTEpKK1EE-Mw3qhM-U-ir9v0IHrO_qgQZcU6_vAdcUDXTnGpsGjKDCFbW3pGBZA_2HgWja9CJjkRlQ4Je2JIQkjznSAZMjJNotzih145t0JurCC7Nq0__IP24EKNUPlVgFsUO9CD-8joxgtYEwa1cvqnUrFlkvYMVZOHVBmpMtTkJselR9oaVSvx7gZ6b67R_UZMJRNznqJZ4vcWUkvn3BKtVg2ZsV0ldBOT7sEjaLJq--V9nRmn4uprF_n9nSUoC5FSIFtOWYSRkZ2w-j5FFStnTbB5dxkWqzuIkwDO843d9-jGXNcBMsMChnczaZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY_KBiadb3Vzs_lPVjstWRsP4G4s2TwAlFBI-hWc93NYV6dnT5xRF2zUNFu6Z2j4aBIf3EjybbolINTZ_veb9hzW43mW6zdW-7VSC6jeDYRZjNIp890Oi--kCrif9CXcxaJNrSIK-aUUt__JFWp3Ue5B5d23owWAcb7UZCTQuv7TKXwi-vJKAtK6HiVdAqArnPq7IGvh73qqWGplW5stQqyfXGFPsBeqy3R49clDjKVTLS4pXTIY0RHC_MGC5DgFS3vMAtScc3aZL4f4fgn45RypQmfs33XTgQuNkh_chh9bCuBZA8T-ibFhvJq_udUNcgSei6iK_gOOJ_s_-dHrUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd0PuMbPjtFbRJnOV9G-1zueMbb3Tl1zD3qPtYcptUncLGla_K1Vn22GCSb4slO51Om0bFiZDLwYG2wxiL81zHdLX8IZvl9LyI2s_D91KQTC4pfaZJ0skZezFvSAdWaQLJQHE_qcr9aPSheO_8vIteMVOLfkk1RjRc_2AVVw_Bim6GJIG5K2omSj28bEd20GLS99gUJdgJM6MXnhVNcEfQYXJtvNqc-IrFJgaUKSaXTXbbzzKRM25b3ISJnE4CSinEBKN9icuqLMtCBtSeiH0WPnUu86fcYZ9sNoegrpeWxp-xEqIXAn9suI_c2V-MLVE03KI4agBjNipKGurG0onQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOL4YSFaGQRH7aop8RRoPTuh4VAhBRAinldhua495LJLODFVjAw-TLsYVA2oK5xhsCqIwTjh-p8U-sC8xcvHt_BXZ4u7OrYmbMt1gYzxglBbKVFb0UUAiWyUokE3oBjIn8jiEz3ZrFZn0JXsKDiEqA2U4WSsuSMywHyYdBXUhetyXJTGDJcDS-DW62sUpYkIItA5P7CNkv83iMgQTBaxbSAubTaXKpHCWnwYNcSLErA_wsRLn2JveBhBDEwmmCFu_oPsOe38lYnVKiSawyibuMDqcY5sVU5nG8aT0qGkh1mkG6QhkMSFuXltzBsohhPpLiMqSjQe5GAr7oIfl27QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZaITQ9brqHOZpXoo0uWdmn9TePX6ordhjUEJtTd1InDt150MzVv4DznoUSohw9V9wHZbSC4gvYD-MoGvJhGx1Q3bqMm5rps257_ZWx66reDfP2j6qy7cjks7RNWP4uXzn_Ror-oDbEZbowwK-RswcQ4tvjtvAaH8TlYDeGiSPwM1R1g0F_EoU_PN-inWqLGbk8_EwIBiEqhUFS7rXNemBggzBP_QiEsZvExSUeegxuhxPMWEJYlNYAGo9kHuFzB2MatCytZhTaxWKePB67D08VY6tNSKNh0ilm-j5W4Z_raR2R6M2z_QeiJxuecKR4kwMt0v8FY2XNxA9_CThjKNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Il00LLwJT7r0TU4iH8DoiBtLIkieh8LUnnbj8VjNBOZcO0XI2_p0eEIclVNYXsW1ZFYbfWsXl2HmHuPaasQXpxPL2sXDkO8eKT96_lKzcCZaHr2EHVsNPR_C0A_iM4qS6HFQ5OQSIC75T94yI7nFnG2G3BPV-8YlghrzsbCTOUplkNw_amE6X-KzrQY1E5rMEEYaoa0Nn3QlEVDmkPah0JT7SGQht1PBtikR_ynnExtY011fBArQbNy0-bLLX9icd77HHOfF09AJ1vgjlyt1WGUY7lOE1arZfocKTf89N40xCFVtlFMXVz8P8B6bGX4DZ6PxjViiCjf-CBEPpLxUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKxt8oMMt7GDKxeAyNx1WlLnMwL-eanLKoKGdnkWXUpk6Meq7AJ444suRxLP7GPpNUqJybDLp21McbWn1qC-t5BAvoxn5Dc5NzcgRF6uTL_aPR8XVrzeP0GxMv8zosT5JkRmeFchEwKNyWpab0ZIhEf5fSDmoqwGfzqLbZVa-acNp9ItnAU70lC3WOE_LjWtHHr32R32X-Dn4uMGG1UHMciFrt5b599jcZbfX_FE9fsdzKg0hvtKQMg2zwJjW2c8VpvtXFErkye20K66pFFVQcczM8KTHnLBWrkrLpyIyTCrs9tN_rzeb5gEHRGJltNxIOkZyrc65hVaDtQfFsERRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQ106ffY0C9sSdVp3KpHM5iHGZy9_euyR4j1npPjiQo533xplvs8xXEJ2q8-DreNP5349J_WXZWJ9t10c5ZtCnH4x22Ijh5EzS4qAEWuUL1Gt2kmyudymH1F-Lb2SZvvp5D4yRJJPs5lmmqZvotZejgnXhAEcZnofC8swlRbydpPLWNZNqxWZWYPZVanIORKZH6WkuzoIboFPms3dCt7cWDDYL2nadfhEW3cUfWby7ImVZ3sxkVknHHNSHaxb2jvDt4-dfIqfJsyT55KipBrtK5Bk4O5dZPefRWCcpOMOxvxpyCH96HKpsEfxKyqJGBzUOuhttwRpb5Xyo5QJrzQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DacHk5l19iatESwZ4hJigt9Rx9f22zwF3rmZ1ByJWM4RoYZRTR88VVaCdqaPcmrEROL6jCQqCKLYrQNgfZBcKA8d9LEdWlVT5TsLe-pjyErao5d6ifwQeRYTwQcLvlKHhlIvA-3i-vu-O-Iirg5zHOTh1acLV4k-5z8Jb1yueSNz2fABIONhHJlVQ6QL8sAqIlpveNWurjpV_wrA3j8x3-MdcBTq4b4Yxq6uGnpluWzXaa0xd14kYphQ0GXy9hOXK1D5rP-aJiMOY4FbeEIjG3hh4zpWSwNjtgLM_CYUjDHNU0AvgAttEPhztKLG9azKPSSLFP8e_eMxxBLfSYITWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCOwdXHvw5fO8Cu8x3AfkcDFaBSvGQAvWczEHIiBAOPcnCs2qemqdbzSZEyCpcFXq0rUqbrfgwY0RkxJN4QGpAg4bzVp1B1oGj_5n6yywEJafEWYbkdsbepECBF33lsM7NTil4vaV88nK2PKAThKKwBh1T5eLthV9FaL_Dfp0b10IWKy-7B0fU4mdSo6fxY7eo9wnBxz_OaOPqgBxm5gEHRHwG3vEZab0xKYgEPTwgue16XDAod7_uwf5sMiT6yS2cU_Cm0r1dhCJYk8JAmijfr7EYQj8r22IYTNu5mOzsnNFZcjLrb8H2gNI4T03fazjNBvJxiuUGJw90iguFLamA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc5Go8sbsd4InY4VMZrYejTzSa9Gl4ISqsrBPXRq1i9gwqt8erYnmgmzJ6W3U5VDVJGQsERiBizWq0nJJNC2xUSZPyf9BXgEKG0X-ui7ZRKcqovuo-ustEWgEYhBBQObOlvDb33jNAv-Kyc-yj6VPAZ9ghixbXQB1YjJYBV8W064A0AF9i6c9LtgGot1k9aGmkQxAUEBnW-ffRY1tEXWS0G_raqjA6NhORm5zvYmhV6uSZHuK19Jj5HsLIOAPaa2ORZ0ka9NhqmR5xBBDZ963E8cw75U5qWh216nKAxsoQTwQ203g_SxsZhxjzZLSLXSyQcR9tyR36R0l2d51nTldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=Pii3496o9TykbRSXC4HTTXCSfwQatkGyBHmJIhWwAPOwGIYcPF6bjKEGVFtTbB2TvMPKJxZHqQKqmUxzpeMUKJSVf4BPA81Ry-vUqUaJk3xAGdsLeg5uIo67dZ_wHHXU2rKRhiSW1WxbHgfGDm93AFLBtMaRZrwUGliLIGV-qWyTI7Xr38O3cbbg6l2n9IFdl6FmyeEH7x45YG3wvqd64tG5YsqMyUXK93Mam7VbEKJDmo2WwFSyI_MQXsqysC4h2GngIkySvEeck080bkirBy5x1abEYYNZU1aeqkgo4onPfKS4sYSMEuLu5lPPHQW2hwE5psBBqyr_eqjo3_gDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=Pii3496o9TykbRSXC4HTTXCSfwQatkGyBHmJIhWwAPOwGIYcPF6bjKEGVFtTbB2TvMPKJxZHqQKqmUxzpeMUKJSVf4BPA81Ry-vUqUaJk3xAGdsLeg5uIo67dZ_wHHXU2rKRhiSW1WxbHgfGDm93AFLBtMaRZrwUGliLIGV-qWyTI7Xr38O3cbbg6l2n9IFdl6FmyeEH7x45YG3wvqd64tG5YsqMyUXK93Mam7VbEKJDmo2WwFSyI_MQXsqysC4h2GngIkySvEeck080bkirBy5x1abEYYNZU1aeqkgo4onPfKS4sYSMEuLu5lPPHQW2hwE5psBBqyr_eqjo3_gDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkmIarogshMu9NGQVGSW0RK2PbAXzpKVp-yUzzQYKmRt8doSrD6jWw_-l2a60TPsR68ob621bum8nRV4GJexJ6vlN-umqzMzE6GuR7gRghw_dbl2sMjuXiWwNZ3QWgCRRr4BCbg3WuWMgy5HIvkZmZQVz1YclvJP9W85ptBAZqWMroFVGN2ZEL8qUWFr1qKPAKH5rWBJXpSngD0g5cvlBDUu2v304Y-Ro4kr0t9LdRp1f5XaosiJ5RH_dpM5uroZ_wyq-EyGwosD3h1N7ndhNTMIystqCl3FdaCnkJXG3whgddApF-OooGKonqm2bP8FBdUrSPMyXlZW1Jm9uo-JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqGNB3-aH9wR8nMxLrycdpz36ryvkAog60MQ2rRCJ6zyMqWmuGrzv8yXpoqnauztcaafR3GYYt5n8Pz17Mu67uN2yBC26eaJrlKTpyor3g-QpnehanOIstaNBD78cbLEwOGSii13TtSrEHSHQfhEguyaUihwhcMEq0JKZAAoJyGr50_lVcEBMA0m4JOSRUfE7z9rGSxiU-jZIgC6qIWG8kW8xPfdnxA48KScfEIS-81_Hg5pkj8piL1gM9fI5wENWmS4l10h9lrTQ50Kh062dT1UvTb6CPSZhtBonEd-is93XQpL-MkpCvlR7vonigeoR3yTL-yTWx827cDyo8GAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS_W4W3nWFqs1cfGxv_AQa1kLzodlPi2yS1rcurLQn1KW5zrefA9VJtc8cXZq7fgk7Zny1b6214a9sV9dduIGo0w-AweFeIR1Fof9KbZu4ygv2UgG1_w5rN6_TaKY_xX5iG9GQWH54fuPewAVSHzwFtNSuSV5DbSOIPjmDXPQIRH_Eh9hzd1npTGdxhwwhAMCns5u-K7LSlOn-1C58t4F29x4T64HPsn8pIGO4Z-JDGSuvfYz_mK4WrObmxsknzi7li-6EyT4WNockLEmIeuTMbI9hBGKUQrrqaqIb6elDuL63ghW95ErRzvEuagzed8_NHJn79ri4cYRNkATK_Ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3fDatdK_U8pmdNy7RMc5TLea-lYr5fg9EjZGH-eeEJgI39X3g4rYlvD_2gMJFV9idPpV2sr67grMk9DDB0UOFBpr5Lv3A7MIZXsJ6RoxSCJ1FMR-WXiJl0KvYvwa9BtgihsRU4fKNcfHxW4QVMFjUrLbX7SllWR5n5mdVGTmX8zhhwAWM4Ay5Ftg_6EzfaEl1K6e2uYQ_pBe0zBk6z_tenNAk-EvcdpQbiQjrDCmOzyH860rzJuIp_V76ChwxLuUcKVXwy5c84sk29Zjd6cGpViYkO8zuBRyoXHeOFE15XYvdtcHLHmIALKZR1shF7_cSqel0e5ksxyhVgpj-w38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=psTDS4npVDtFYhgZAaZ2VjDkena4WFTSGPBMpr-Pmeb4p4gJrXz_2sT5pde9YqzLvuHQ-02DCZsShocbrx3XDvZsMteNkzXQ5SX6dGbcvMG_O73DkBsjdEgvc-S73Y9Tgf2HpHVLASQh6ugx42HD7GFfwv2nB-lpIUnScgD0mybrtoqxDXkCVerNJbj0lXQENbh0-eXcUqe_3jS0j2AKCV4RlD89q4gNICC9HVVqiPBryX4GdCBNEMWwrsMjAe6-lq0G8hnCjX-Pr4If86g57k81Gkk27mUqIa_IfW84KPTQff5qLRmkJn6D4xThjNi1xQJqoxNq6iaK2lyF0FxF6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=psTDS4npVDtFYhgZAaZ2VjDkena4WFTSGPBMpr-Pmeb4p4gJrXz_2sT5pde9YqzLvuHQ-02DCZsShocbrx3XDvZsMteNkzXQ5SX6dGbcvMG_O73DkBsjdEgvc-S73Y9Tgf2HpHVLASQh6ugx42HD7GFfwv2nB-lpIUnScgD0mybrtoqxDXkCVerNJbj0lXQENbh0-eXcUqe_3jS0j2AKCV4RlD89q4gNICC9HVVqiPBryX4GdCBNEMWwrsMjAe6-lq0G8hnCjX-Pr4If86g57k81Gkk27mUqIa_IfW84KPTQff5qLRmkJn6D4xThjNi1xQJqoxNq6iaK2lyF0FxF6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=E3fFCUNK8X5L76TDro-MXu1q-WrwxkgLsUbfAaAv93s4wJgv3LFeS5xr_wrqQRxYvPHSrAkbxXUqNR9bZI5T9Xt2NhPbJ9OXl2R0RE4bRvc0aUzQkOMBB66MukUPElsAu6DneS-1tCHiyRA-EGDZFxC0uPisUcl8WKYqz4Mso0f7CfnNktIoM3Lh1tl1OnwKIaPhuqGq8fz2ZVsOb1-zyd-hnXd_7JezLwyuxhsKGVcUAg8IbK5ag7WxSFWpvKX-PdZxDazkaFoslmYD4-pPyNEg2uNyKDka-PfNTN-j2yQqV3SacEdM8pYAvIJy4r_JBs0kkRKzJsG0LyYRFz2_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=E3fFCUNK8X5L76TDro-MXu1q-WrwxkgLsUbfAaAv93s4wJgv3LFeS5xr_wrqQRxYvPHSrAkbxXUqNR9bZI5T9Xt2NhPbJ9OXl2R0RE4bRvc0aUzQkOMBB66MukUPElsAu6DneS-1tCHiyRA-EGDZFxC0uPisUcl8WKYqz4Mso0f7CfnNktIoM3Lh1tl1OnwKIaPhuqGq8fz2ZVsOb1-zyd-hnXd_7JezLwyuxhsKGVcUAg8IbK5ag7WxSFWpvKX-PdZxDazkaFoslmYD4-pPyNEg2uNyKDka-PfNTN-j2yQqV3SacEdM8pYAvIJy4r_JBs0kkRKzJsG0LyYRFz2_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=Z825gr7h5YreS-3rsMf4D4-jeHnSwoygFZ3fFHavyXYznuVgRjXlNcZt_WqaRZF3IneHEFUKkSZyjcyVEbHaYdEe72A7R8mnLnd8pN7VVg6s5ZPyjH-KjHx9pokO-lKGwrlGpEFIKIDk3LoHpzTx1eNGS7J_2DSAhG59hFPC2Zc1KysbXpUR1d1tOPjl4eCt8DcEwqQ-tV5r3LSLEolLoDU976EoFNLsf6MEyqeEdlh6gZLd62C7sCVZ6KQHV5-lBs6B2THjRXvSVMeYUjKYBI4JMRW237x9dwtI00eRT6PuPCey7mrVJjE-zw3HCQRtnHfjW_OsNswCwyNeC0uAIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=Z825gr7h5YreS-3rsMf4D4-jeHnSwoygFZ3fFHavyXYznuVgRjXlNcZt_WqaRZF3IneHEFUKkSZyjcyVEbHaYdEe72A7R8mnLnd8pN7VVg6s5ZPyjH-KjHx9pokO-lKGwrlGpEFIKIDk3LoHpzTx1eNGS7J_2DSAhG59hFPC2Zc1KysbXpUR1d1tOPjl4eCt8DcEwqQ-tV5r3LSLEolLoDU976EoFNLsf6MEyqeEdlh6gZLd62C7sCVZ6KQHV5-lBs6B2THjRXvSVMeYUjKYBI4JMRW237x9dwtI00eRT6PuPCey7mrVJjE-zw3HCQRtnHfjW_OsNswCwyNeC0uAIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMnzg_A6e9-9cha0n6JRdwXiCGbJlh-urhkpaUKO-NX6MuO04mUy7krPTHOvGbELUGqElWAFULpz--EfdwZUCTwbfbppuYImWnr-iboeKKchaWpEgSHydpEdZLvNZGEJPVJyNdbbwpgFIi1NmR0T86WqtSXHU3R9XEn3B9NOBsVCZajRElW8FhxnwFEji10MwUMq0O6Rbg6wkYTm_cHSCRycLA_wsNgOwFGbaKY7iH8mGbw9m5hhOtu6WlFHnDxlLIhR-nNy6us6MC9C-5WJZpzob5FNXXM1RsqM31YL_qEymJkPW3NwiVKjuIU7cKyF2msW-Pjbd1ilpp03bgmz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=NcUYRi-lqsBQB2Tf7fd6s9XcnteGSTHIApRk7uz_reMhtgabsWXyCevLUVTo1ksF_hmz1zKjSpkPYgBKtquhk6t8Zk0S8eFN9wShEoXxFi9ROYHcQXZTStm2LVp-hFfkVCfRYlpkRVt-zNJ79y-XREudHJc1HlWwShEArxfJMdG58EzqY9-ASZAVpacMdcd4xWh1VVpmTJHU-xaT0vSdigiNuGJCLPOM1mx9ZlvhJPsjIJ7l2qzVtD2CC3ABw2aPY0H1ArK4IDQD43jYOt7CyK7vksR0li0BYKyaI5RJm7XaWaatREyJ2_hSi3HiV1yfqdydE-AlAMXR_xgbU9O2VofwdaNj1bOOJC3J2Eq-9UYH3nZUs4xb8CAr9bRUICq-jWR3ZNWCRao_3YBCAKTIucTFT_FwkkyIadGo9VfL2c3_SX9Q9WEuQr4wXQgkFELPcfhrzgOObXQgIb3w2N4VnBJYKAWrePVxVs7tK5JyM5hrBacpHK6aMtH8vbqVkJqaIFxrFmi67k-V08HG7-OuUgN3L01ID7LhjCSed8hB5GfElZNosC8E8EzP6Eto4bcdHgE1wnJUg-D5VW6RAxZuLn1bxIcfQ27bWwpT1KSFtqGSH0F6JtKobJFbYYoLSo__96rVMXn0UmOt4y07heMDJqf4fm9uQoOzAldBAHf7SAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=NcUYRi-lqsBQB2Tf7fd6s9XcnteGSTHIApRk7uz_reMhtgabsWXyCevLUVTo1ksF_hmz1zKjSpkPYgBKtquhk6t8Zk0S8eFN9wShEoXxFi9ROYHcQXZTStm2LVp-hFfkVCfRYlpkRVt-zNJ79y-XREudHJc1HlWwShEArxfJMdG58EzqY9-ASZAVpacMdcd4xWh1VVpmTJHU-xaT0vSdigiNuGJCLPOM1mx9ZlvhJPsjIJ7l2qzVtD2CC3ABw2aPY0H1ArK4IDQD43jYOt7CyK7vksR0li0BYKyaI5RJm7XaWaatREyJ2_hSi3HiV1yfqdydE-AlAMXR_xgbU9O2VofwdaNj1bOOJC3J2Eq-9UYH3nZUs4xb8CAr9bRUICq-jWR3ZNWCRao_3YBCAKTIucTFT_FwkkyIadGo9VfL2c3_SX9Q9WEuQr4wXQgkFELPcfhrzgOObXQgIb3w2N4VnBJYKAWrePVxVs7tK5JyM5hrBacpHK6aMtH8vbqVkJqaIFxrFmi67k-V08HG7-OuUgN3L01ID7LhjCSed8hB5GfElZNosC8E8EzP6Eto4bcdHgE1wnJUg-D5VW6RAxZuLn1bxIcfQ27bWwpT1KSFtqGSH0F6JtKobJFbYYoLSo__96rVMXn0UmOt4y07heMDJqf4fm9uQoOzAldBAHf7SAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=oH8Qby6QKRakr4xV22dh4k6pwd_i0UZqul0SKuf54e1rxW2OTebhJyDpBoxoql-MiNn3Ia5MXs-1_iEElNnQ8RLlx5AlH8gL0t1TTcsbaA4OwLnTuHQ72UcbQNwpIFDCr6kQ-Bj7SgQCUmkaond82P0z-4ICwBdcNl31w5YwRB4p43fBFL8Vw2SYUtHLIlaT_JBVtmvfT8igLx6U4IgfrszZsgKLajfdAvumnksuVBnjq2-YMf58SO-rZFAY93fiBxaMJAvv0IkinaRVpkasgy17lcjyDe5jN3gjBvkOrRW_rJcjFrhV4TfLRrqLBlYElo9olj6EZrY4bhFn_QFsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=oH8Qby6QKRakr4xV22dh4k6pwd_i0UZqul0SKuf54e1rxW2OTebhJyDpBoxoql-MiNn3Ia5MXs-1_iEElNnQ8RLlx5AlH8gL0t1TTcsbaA4OwLnTuHQ72UcbQNwpIFDCr6kQ-Bj7SgQCUmkaond82P0z-4ICwBdcNl31w5YwRB4p43fBFL8Vw2SYUtHLIlaT_JBVtmvfT8igLx6U4IgfrszZsgKLajfdAvumnksuVBnjq2-YMf58SO-rZFAY93fiBxaMJAvv0IkinaRVpkasgy17lcjyDe5jN3gjBvkOrRW_rJcjFrhV4TfLRrqLBlYElo9olj6EZrY4bhFn_QFsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsyzGNuRXPhmsJeMvDu8WpLVBpL93ZaojL8Oc4adck5uznMj-y_eazKUJV1YTTNwkI4BTX6tcFbS_5LDWcJsqoEU5u3AU9kSsjyhNDpE1FDN91LBuh2ZoUlzsCfOogr2BrRubYuMb38pPwX7wo8NqIE6OIWSBuNnivU0he-jqem2pEcfSYyJHbl_9FQwJhK4xAbwslopXY0HJc-YQw_Ug20N0I2xFa0WPIjxoxJKgtdhbYxXWBwiHCJ2EAj-6CezpBNVuqwEAt_VD2mAUmzgPg6NvhALib5Z4T0Agg0Zr4rWUqRBNLjsjGwGONMdbXZ89j_PvFW11NJA_dl9jTbzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDlED0EnuUhumNZ1vyz_PVpSIjTwe-S28HwYMkS8o9wlLL500AjjaAhl-wbBjF3werkcY_EY6CpvqgbMMtm3HI7QHQ0sF1vqKTCHQkP78fsKXCPgRaqUzOKvGyTftzt-HeT43RlH0qLaSt77xJXuX12UTKZKKwZTJN78f88XIq2hEdDyxdm_i_oayibLzdg3OxOh88MJJulj_hJcxYkEABx8UTcyB-k-FFOQHPQlzNGy00MAx-OtpzZaJjWlJ4cluPezc4pxxCsxqKVy7Aiin-NuRHJbDZnQvR-5CWGLT70srkHbSKeTr2vcGvCzFfVgGAv-o4-3u671JmQiY0d5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=KlWXYkNTdsO3BnowLRSxPlhQZWf0GfsR3dtSdrB7bATcQkp3txfJLqRH2_gGnvJYNbFV2KMmk8IoW7fNj_VnoweF6uKUXxl_KxW9ggk4OR_B0Fet1R5nMoSaR5DHwe0bpS_VI1VTz7aYYJ4ktpuZH-kIDwF27S4CWDOlK3tkekQ2fRvfWEUWIQ_KN4CLQccAa02j3U36umbFRYUYCl7jxmhdO5ujc-ZLSPkGwe6gOqUSOd5iuHN8lQkGbFpbokafWaAx_5r4Ti4z2jS20-w6-O6TtAV3rosLNCyJck6sMkhaLlh359Z_WL937fjJH0JdBVgIjnMBWd1bR76CjdZp5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=KlWXYkNTdsO3BnowLRSxPlhQZWf0GfsR3dtSdrB7bATcQkp3txfJLqRH2_gGnvJYNbFV2KMmk8IoW7fNj_VnoweF6uKUXxl_KxW9ggk4OR_B0Fet1R5nMoSaR5DHwe0bpS_VI1VTz7aYYJ4ktpuZH-kIDwF27S4CWDOlK3tkekQ2fRvfWEUWIQ_KN4CLQccAa02j3U36umbFRYUYCl7jxmhdO5ujc-ZLSPkGwe6gOqUSOd5iuHN8lQkGbFpbokafWaAx_5r4Ti4z2jS20-w6-O6TtAV3rosLNCyJck6sMkhaLlh359Z_WL937fjJH0JdBVgIjnMBWd1bR76CjdZp5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/INOWYXt7WsId60q4HBltJXpF-iRb2GnEI3yH-Oqn9-kc2dbYweH0yDfUO0Sci16_pkAvsSbkch1_B4msv107Hdu1JbTcYQjTiXqfWqhenloO8PE7NndDKebKHp7qRBz21NnDfE0OGBwO0QU-qVciF9UddzwhL8En5GtUUTSdt8aH7rQhhgsHImNAaPOSLKTFOKI2EUq8v4bosRQw1ivPTuU-oMXQMS3VyMp6MdcQqTEP79Kj4mLRKxCr3u5r7rawKdB8cGO9zn1D7vi7G62zEbzg3eDLIr7omD0LdaOClDB9qnRQxNx6A2cxs3qn7HCpa9_eyZs703Mkf6IZ3ZOAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hvf-8mfgI5iKmNHu-6fMbN6C9KnXAomCbWdHw3uKsRyqccQOTDON-fbuKJXUfUC1OPnhPBUph9sKTWREjauQV8ZEKGk6uXyWhsuMGoaO0z4lVEoBgSOiyBS2RsplEY9f_bcg1CVoAonGHBCvVJb4AHA2RNCNWQQHgQSROfM4fCNfYh_QLab9fhv0ruawvZcm8o_0vcdkE0ExaG4aUBwILrluoO1eKZ3_OjzXQzMU6as9R8p9qTGzULK2tgGDGvEflh6lsQ5s94YonKAHEwz5b4ZN6bBeVj5giDRxZhyYefpTFvpZmkKtGGHYe-pzNPPSL3qo8mE64KLrlTe96wne7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ICGqdtn0btaW7iNosErj88l7sru2wAy8TCcznNAGZXflrWBXaS2jAS3pttQXwgXMvPi3GK_SfYrf9xCTiblZQY8RpofWQ0eIilnEAXUCcJUbDufhCMnPeTTWrJVNkUnTBISqKQc7uR4k7g3yqtbni90q62GKMvPdXLDbEt0YnHxoAHBGh5-BIghaRtv2ISxqydXBqGnSVL3sw2IIIUximxvwvpgOirzAbvlgElrJ6ucGe162z9vpfWyeJ8kFPcpfvMWhgvIunH5eKCdjPSGHj_ox9VFizMhZRKkMf8M0iw4DkfAUyRdgzyPD-RkNXzdS11q3WniDDVHLzs-owkjA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ICGqdtn0btaW7iNosErj88l7sru2wAy8TCcznNAGZXflrWBXaS2jAS3pttQXwgXMvPi3GK_SfYrf9xCTiblZQY8RpofWQ0eIilnEAXUCcJUbDufhCMnPeTTWrJVNkUnTBISqKQc7uR4k7g3yqtbni90q62GKMvPdXLDbEt0YnHxoAHBGh5-BIghaRtv2ISxqydXBqGnSVL3sw2IIIUximxvwvpgOirzAbvlgElrJ6ucGe162z9vpfWyeJ8kFPcpfvMWhgvIunH5eKCdjPSGHj_ox9VFizMhZRKkMf8M0iw4DkfAUyRdgzyPD-RkNXzdS11q3WniDDVHLzs-owkjA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=cGQCtlr8B-pfVfDi0HoCDEC_rSRmNsMZvJLIDuRoRW7XrkpK-KoakRd7OVCn0iVeFyV-uP7gFIZmOpR4CFH0Q7KBe57M5LPt1HMO777ZEbDJl8f9GL9o9uEbUTxve3J1V1Dm9WlYpDKn5j2FBa0UXoNr5ikclrx3efI1KpMVW_5VdRsLkrdGkvCZ4j8XD349LMZTHsGmm2Xugg_PoQw_g2ZrxJN5pgGM3_6mKkPOMd6G6sx7S_iY_eDoXYVdb32QGXq4RxOw9GFy_fijxNxxATk5tyfbBUtDJg6kCpDMC5_u8WYVdxgmdtVMiMYp3bHEfj5ve6w9uMCEf0kKA3roLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=cGQCtlr8B-pfVfDi0HoCDEC_rSRmNsMZvJLIDuRoRW7XrkpK-KoakRd7OVCn0iVeFyV-uP7gFIZmOpR4CFH0Q7KBe57M5LPt1HMO777ZEbDJl8f9GL9o9uEbUTxve3J1V1Dm9WlYpDKn5j2FBa0UXoNr5ikclrx3efI1KpMVW_5VdRsLkrdGkvCZ4j8XD349LMZTHsGmm2Xugg_PoQw_g2ZrxJN5pgGM3_6mKkPOMd6G6sx7S_iY_eDoXYVdb32QGXq4RxOw9GFy_fijxNxxATk5tyfbBUtDJg6kCpDMC5_u8WYVdxgmdtVMiMYp3bHEfj5ve6w9uMCEf0kKA3roLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
