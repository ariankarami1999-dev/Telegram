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
<img src="https://cdn4.telesco.pe/file/lcuoRpvJo5mKTRofjHpg0O1ANyO9x1jwjt2QNNd7ZYAZgWnzcB9ESsMVcmBDp3djykeeNqW-aC4jV-8HSgya8lSGbEtSUa07PExQL1kRyNXKOVkHRyQvb7kWVEXeCT1sajFxAjC-mMkaN8sthlVypjI72GDvCBHwB-UpKRf6bP_eYOYBwk0grFpP1tOywwnTz3M16JU0bo5_y50hL7FKrxToU7e4PGw2HJrkdMOl-IUSj5nR74P2kQtSnl-TYGI2BBRiJ1xOZCgN1K5CMLAyWnRALmoZKDiXMIviYoC0eNMLKVqLnjHqXhW7en6qZzQBdNxL60dCAcgj0TOymAdceQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 418K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 21:20:10</div>
<hr>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">موج جدید حمله موشکی ۳ پا ، گزارش صدای انفجار در اربیل عراق و بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/19239" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efsHj6JeFBQPG4RvPsR77JmfIJo6jbnSyU-ji6pEmUdxuBaHU9m_D5SJX59cQ8eouxte9VmCk0L_IqthmmNJvueNxNpuxyOB4Ja5AOZ2OTaOBDzSA7hX3PJSnwyjMNFI8vd-OVmymvpp97-SXYY3f3yrDKj18g6TvR8PDsF-MW1OiOYZvQZiaDcuNr0e7J5nCcliu4gABwEfQmECa__FcplYnMWO0IbqOE6ibJLgH83iL6rXoVD8PjMEPzdC1DKyEpNRwdvFPH2SpOzIQGOwFoLDzQTu9DNc_Nb8nSgHF8suQ3W1ap1wpaRdi5TC4r_Zj3Zql1zWAyPkIM-llx6mLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6473d165.mp4?token=OUPM-dgnXIDzUvChcyw0PuskTqRCVXbzvwjawd1743Q0u9Gx-EveSYs_SUXxnxWzIiizna5YEds3rLuEUJVcANwkK4dm6SvxawDUiDPg943YgzBLgvuo_i4fVaCL_44T4AysCUKAolqLssUUSDHsF8GTVCprrYCrh0be2-aTDIm55p7MwEkrxUHk6e1aM_SxeEixs3sfTQWDes13XiwIjIw1tgxXLkjS5L7XlxOFVLukoXOBse1Mb5QqI2szzFhBYxpQDKnXxvAX59czjRpTL9zgQhRVTUua-HSyPmrSLXbme3f_tQEavSgEfcpRgXkwoUxkHUiRDXkZQvphrSXI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6473d165.mp4?token=OUPM-dgnXIDzUvChcyw0PuskTqRCVXbzvwjawd1743Q0u9Gx-EveSYs_SUXxnxWzIiizna5YEds3rLuEUJVcANwkK4dm6SvxawDUiDPg943YgzBLgvuo_i4fVaCL_44T4AysCUKAolqLssUUSDHsF8GTVCprrYCrh0be2-aTDIm55p7MwEkrxUHk6e1aM_SxeEixs3sfTQWDes13XiwIjIw1tgxXLkjS5L7XlxOFVLukoXOBse1Mb5QqI2szzFhBYxpQDKnXxvAX59czjRpTL9zgQhRVTUua-HSyPmrSLXbme3f_tQEavSgEfcpRgXkwoUxkHUiRDXkZQvphrSXI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر لحظه آتش سوزی داره بیشتر میشه آمبولانس و آتش نشانی به اون سمت میرن
@WarRoom</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/19236" target="_blank">📅 20:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/traycp9tAzTWUdzSA_JAkBuBMv3wvzznLl8cvn2muRwPx5ErQnWt7s-nCYvVv9zQ5yosAxx-XJZu0hbigwd5h9NVe1RbHXhdjGwkUMLvfeczG8KYc8hmq6_nc0hYhFCgQq425H1Gxkf4HLRzqjvSI3TYmE9lRVPp_q9_hutU6gszJn4pG8RjadkAFWV0g5g-PweWINdODs3K30Xa8AbmZQHNR7GC2c-6Fnp0VDUUZZsoGMZuRipARkPZm5wh-sEUgk2wJ5BJFHVParau3f9IgRgKmFqtXoyewCAsPJ9rMyc6TXaAkMQW-IDP2_5xyAZxABp9YG6JWperUxPG_8Crxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/212322f58b.mp4?token=ksuYsTBjXhy1pRGWA4jrLTERLbqzxS2Cb41ewbxtpk2uhGo9cdEQilVOaed8ZbGY-U33ULZuD0lk6wncfeAJvU-JfLoQZy8P2omjYKpJuA5pndYnShcZVpz1CPfRFLW-wMem0R2Ep1VfxIQg3GRRq2gjipVDjlByZeqzEUFAcGN81_xRvYRVSY79OufKDWzmxD9SA2goiysUA_7n-jSqZrvWAtfXsCAqHiwTsZK0-NN_brASrpklwsYaWOdwcSG2KgE9gQyRAwYgWe3O-N3fP1IoGLQ0RylN0caOdbjEEzIPf9Sea2bYzxVd3lTCXaScS5V6AAt1ymuKe4qYQMRVVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/212322f58b.mp4?token=ksuYsTBjXhy1pRGWA4jrLTERLbqzxS2Cb41ewbxtpk2uhGo9cdEQilVOaed8ZbGY-U33ULZuD0lk6wncfeAJvU-JfLoQZy8P2omjYKpJuA5pndYnShcZVpz1CPfRFLW-wMem0R2Ep1VfxIQg3GRRq2gjipVDjlByZeqzEUFAcGN81_xRvYRVSY79OufKDWzmxD9SA2goiysUA_7n-jSqZrvWAtfXsCAqHiwTsZK0-NN_brASrpklwsYaWOdwcSG2KgE9gQyRAwYgWe3O-N3fP1IoGLQ0RylN0caOdbjEEzIPf9Sea2bYzxVd3lTCXaScS5V6AAt1ymuKe4qYQMRVVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی کوه دراک شیراز ( دیشب حمله شده بود به این کوه)
@WarRoom</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/19234" target="_blank">📅 20:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هم اکنون تعدادی از بمب‌افکن‌های مخوف آمریکایی مدل B-1 از بریتانیا خارج شدند، همزمان با اظهارات ترامپ مبنی بر هدف قرار دادن کوه "کلنگ" در ایران. @WarRoom</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/19233" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هم اکنون تعدادی از بمب‌افکن‌های مخوف آمریکایی مدل B-1 از بریتانیا خارج شدند، همزمان با اظهارات ترامپ مبنی بر هدف قرار دادن کوه "کلنگ" در ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/19230" target="_blank">📅 20:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/19229" target="_blank">📅 19:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ : ما اصلاً کارمان با ایران تمام نشده است،ما در حال حاضر قصد ترک خاورمیانه را نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/19228" target="_blank">📅 19:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19227" target="_blank">📅 19:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سه فروند هلیکوپتر آمریکایی در خاک عراق توقف کردند و سپس به سمت اردن حرکت کردند. این عملیات که شامل فرود نیروها بود، حدود یک ساعت در نزدیکی مرز الولید به طول انجامید.
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/19226" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ارتش لبنان را در منطقه امن مشاهده کردیم که با عبور از موانع در منطقه زوتر شرقی، توافقات را نقض کرده‌اند و به آنها شلیک هوایی هشدار دادیم آنجا منطقه آزمایشی نیست !
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/19225" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا: اگر ایران به حملات علیه نیروهای ما ادامه دهد با قدرتی ده برابری به آن حمله خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/19224" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: محاصره دریایی اعمال شده علیه ایران ادامه می‌یابد. اشخاصی شرور بر ایران حکومت می‌کنند. اگر به ایران حمله نمی‌کردم و از توافق هسته‌ای خارج می‌شدم به سلاح هسته‌ای دست می‌یافت. ایران به 20 الی 25 سال زمان نیاز دارد تا آنچه ویران شده است را بازسازی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/19223" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ:بدون شک، ما تأسیسات هسته ای در "کوه کلنگ" را در ایران بمباران خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/19222" target="_blank">📅 19:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/19221" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6046e4dc14.mp4?token=VRhaEhfLznHvoADWrr7BrNo07TokLxlsEKpVel3SYTu6_eA-SnqrQLZOYX7y51_ekhrac2VVfoKcpoS0fpbY8s-ySxNc1ZLZe0sC20egfHbxYraCJ0NdJKe57ggxPxmkOm3MaMMhIjpRdB-rwC9_y_6fSm9MhOG6DQvkxOik3U33_kEX9E_C_-ko93YOTKmQOHH-BDkc0q7svWK90xWCqMeS5RtIkRwswkPXrCns9fb71zfWH5qMRBKFh-g6oII9zsiB7uAsoLAuJ3WmuNYNe3YHvJb6jha7cXNpmTT9M25Nys4gJXF14X2tnQi-ZNJqqKMCoW22T-WqOiTLUCef6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6046e4dc14.mp4?token=VRhaEhfLznHvoADWrr7BrNo07TokLxlsEKpVel3SYTu6_eA-SnqrQLZOYX7y51_ekhrac2VVfoKcpoS0fpbY8s-ySxNc1ZLZe0sC20egfHbxYraCJ0NdJKe57ggxPxmkOm3MaMMhIjpRdB-rwC9_y_6fSm9MhOG6DQvkxOik3U33_kEX9E_C_-ko93YOTKmQOHH-BDkc0q7svWK90xWCqMeS5RtIkRwswkPXrCns9fb71zfWH5qMRBKFh-g6oII9zsiB7uAsoLAuJ3WmuNYNe3YHvJb6jha7cXNpmTT9M25Nys4gJXF14X2tnQi-ZNJqqKMCoW22T-WqOiTLUCef6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏پرزیدنت ترامپ خطاب به جوزف عون درباره جنایات رژیم اشغالگر جمهوری اسلامی گفت: «آنها کودکان کوچک را طوری می‌کشند که انگار هیچ هستند، انگار آبنبات هستند. کاری که انجام می‌دهند دیوانه‌کننده است.»
‏او افزود: «آنها مردم را کاملاً تصادفی می‌کشند، بیش از ۵۲۰۰۰ نفر را کشته‌اند و هیچ‌کس درباره آن صحبت نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/19220" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ درباره ایران : «ما آن‌ها را در سطحی تضعیف می‌کنیم که هیچ‌کس فکرش را هم نمی‌کرد ممکن باشد. آن‌ها واقعاً به‌شدت در حال تضعیف شدن هستند.
البته آن‌ها توانستند یک مورد را از اردن عبور بدهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/19219" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:آنها به‌شدت می‌خواهند با ما دیدار کنند. تا زمانی که برای یک دیدار معنادار آماده نباشند، ما هیچ علاقه‌ای به دیدار نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/19218" target="_blank">📅 19:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرنگار: هیچ نشانه‌ای وجود ندارد که ایران آماده‌ی توقف جنگ باشد. پس برنامه چیست؟
ترامپ: شما از کجا می‌دانید؟ از کجا می‌دانید که هیچ نشانه‌ای وجود ندارد؟ چرا؟ چرا شما چیزی را می‌دانید که من نمی‌دانم؟
شما نمی‌دانید پشت صحنه چه گفت‌وگوهایی در جریان است. آنها به‌شدت می‌خواهند دیدار کنند تا تلاش کنند به این جنگ پایان دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/19217" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترامپ: «هیچ مسدودی در تنگه باب‌المندب وجود ندارد.»
@WarRoom
یاشار : پس اینم بستن
🤒</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/19216" target="_blank">📅 18:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری های رژیم: دلیل قطع برنامه فوتبال 360 عادل فردوسی پور دعوت کردن از علیرضا فغانی به برنامش بوده سر همین قوه قضائیه تصمیم به توقف برنامشون‌ گرفته  و نباید اینکارو میکرد چون فغانی ضد رژیمه و با ترامپ هم‌ دست داده.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19215" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال 14 اسرائیل: جمهوری اسلامی فردا برای مذاکره با میانجی‌ها و تلاش برای احیای توافق موقت با آمریکا، هیأتی رو به پاکستان اعزام میکنه.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19214" target="_blank">📅 18:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/674fc57c31.mp4?token=vjpH7XhyQGtcZPDplQjsw89dWPdqyiqILRuEH6pKS01TF_7JfJ7UiP5bhu2sRvKM7Fz8oJx6YAhBNMTgFzW6zQ16FqYE84kyU1N0M6kk7tPP-DqKZjvjmT7wkuxdstIkoU9lhHmYZgwhAOWtWg4ULQ2k-Q7XxmSMNlIWTq0IvHr2toQSwcZR5AsQYcewr_JAocU7Ol3HUopK7jEG59_4jegQb3alRfBqldRj2Bkgk63wFpTdDqjDEIwls9gC1fyiDeEDuXaqDhXZWuyGO_hWF6Lus8y12L_OdoJz_-m3n0zUJyIpAK_oVsfbyC3WIs2N-17KnQjy4ronYttPpmsI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/674fc57c31.mp4?token=vjpH7XhyQGtcZPDplQjsw89dWPdqyiqILRuEH6pKS01TF_7JfJ7UiP5bhu2sRvKM7Fz8oJx6YAhBNMTgFzW6zQ16FqYE84kyU1N0M6kk7tPP-DqKZjvjmT7wkuxdstIkoU9lhHmYZgwhAOWtWg4ULQ2k-Q7XxmSMNlIWTq0IvHr2toQSwcZR5AsQYcewr_JAocU7Ol3HUopK7jEG59_4jegQb3alRfBqldRj2Bkgk63wFpTdDqjDEIwls9gC1fyiDeEDuXaqDhXZWuyGO_hWF6Lus8y12L_OdoJz_-m3n0zUJyIpAK_oVsfbyC3WIs2N-17KnQjy4ronYttPpmsI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دارلین گراهام، خواهر سناتور فقید لیندسی گراهام، بطور رسمی اعلام کرد برای کسب کرسی دائمی سنای ایالت کارولینای جنوبی نامزد خواهد شد و قصد دارد جایگزین برادرش شود.
WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19213" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19212" target="_blank">📅 18:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19211" target="_blank">📅 17:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19210" target="_blank">📅 17:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19209" target="_blank">📅 17:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با موجی از موشک‌ها و پهپادهای تهاجمی رژیم اشغالگر جمهوری اسلامی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19208" target="_blank">📅 17:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19207" target="_blank">📅 17:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19206" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19205" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آلارم حمله موشکی/پهپادی به کویت به صدا در آمد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19204" target="_blank">📅 17:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBdcKNrjmk0QVqHs3VvsW2TQwrrlQC6ygRBMfnMgKCkEtsyiWeu0gc2gMPeZ4yvDKJKk_AaukyMsy4xC4Av6cQSoV_sCoQrafSC0gPaD_HUbMMhYzJ7cqNqeKZawU85yQi0slBIZW22KOIGeD1D9S3eq9vncObz8mSjTtZ3PUGVBMrMW0cwQOrjSI9AkoS_0Qtiho2Mu3vy06d0kJw3CA3FQjQuwFGx7MTe2W9RkV1KRLEi0OnHK2YVDVHK4NlqoL1HUQx5EawbjhP43j5lhAnr_Svtog7yOGKjg2uWACSujEw1b72TqkMMOgHHgYKZ9mSESvfxT5zHKI0q3iLmPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وزارت جنگ آمریکا تصویر مایکل سوینتون، سرباز ۲۶ ساله آمریکایی را منتشر کرد که دو روز پیش هنگام خنثی‌سازی یک پهپاد عمل‌نکرده متعلق به رژیم اشغالگر جمهوری اسلامی جان خود را از دست داد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19203" target="_blank">📅 17:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک حادثه امنیتی جدید در دریای سرخ نزدیک تنگه باب المندب رخ داد
تعداد کشتی‌هایی که مسیر خود را در دریای سرخ تغییر می‌دهند، به ۴ فروند افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19202" target="_blank">📅 16:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19201">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تشدید درگیری میان آمریکا و ایران می‌تواند باعث لغو ۳۰ پرواز مسافری اسرائیل در روز شود؛ حتی بدون آنکه ایران مستقیماً اسرائیل را هدف حمله قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19201" target="_blank">📅 16:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سی‌ان‌ان: هگست قرار است امروز بعدازظهر در برابر یکی از کمیته‌های مهم سنای این کشور حاضر شود  و درباره درخواست میلیاردها دلار برای جنگ با ایران پاسخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19200" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omm_m3cfTfZKh-mXam0UXvacJTG_lHLbj98xJvBlZa1tReBGZwA9rNXp-MHGVaRMl1HbKK0s5cyXRwlBa9K8Huk455lP8-z_z46FjkACE-F58FLX331vKXE1EVilvPchi72uRPaDnxOuxvZKEPsRS4SlsP9ds9c6bq-ppnm-N2W4HNGurGRHypAu_Jn8nM0OrxtVLq65L5DO14PEXirIlND4CJKLQQa9rB21USkTqtWN717gq_4s1bZy5adaTOn5wx4nxi8hdTqS-2FYq3ywt7PZ1rJWSupS4YOqbLB2PpB8rC6xpxiU49gUKvkLX65bWB7CeuhCVAF8lfg53-l3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکس معترض گریان ایرانی را بازنشر کرد،نوشته روی عکس : کشتار را متوقف کنید
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19199" target="_blank">📅 16:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19198">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL4a2cljHcwzDMWICOvbN50rrLj12AqR4xECfhTz8FJj9XwHBtftS5h5XDbMck4uEaL7AYniJgM04wLl1UrrURVXpiLHLdaso4kzt-oZ_FwmpN_Yt9Da1LmdHB7HuGTl8p5j7_oahw7iCww0etVE7yDOi7DkV-kys2ocdHujLC2xdK0VBMSBpIbh3TnlCNErD7Mh6qSqJUSzrKoxx7yp7jX-lpJMCadS_TZq-JzDQx4EKByLB32E5gr4kKf6DVSRtbjfjyG7ptAmHMyQ3EiUK8MDKCVCo2gSr2VaJysU4Mow47gLwNdEB0Eil8BUYWCDA8ChVRfz96Fa4uVJ8LAwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث:
آخرین مورد از بین ۵۲۰۰۰ نفر، به علاوه معترضین بی‌گناه... ای وحشی‌ها!!! دموکرات‌ها کی بیدار می‌شوند؟؟؟
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19198" target="_blank">📅 16:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19197">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال 14 اسرائیل: در حال حاضر، آمریکا نمیتونه پایگاه‌های خودش رو در منطقه در برابر حملات ایران محافظت کنه، به همین دلیل در حال تخلیه این پایگاه‌ها و انتقال هواپیماهای تانکردار و اسکادران‌های جنگنده‌های خود به اسرائیل است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19197" target="_blank">📅 15:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19196">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پزشکیان: روز به روز ارتباطم با مجتبی بیشتر میشه و مارو هدایت میکنه
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19196" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19195">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Liv1KzHvbAnt79AfDqvUjirTv_zX6AuCAx27JJklILYbij12REojBsTwZ2_pAUnY2unai1eN2jk8sh8kTZYLAtXI91m_GE87W_AOQp7NwJNCcPOEn46C1_12LFT94Otf87-ABk60lRep8GI1NXT86xVzRT0_L-LN4RXnpYABcHnwoKRHKpeAbWmYOC6ltxcu1rgk9QGcWW1JUMCaNFy04hvUEPKdnoWAm07LRL5LLeVTWvHlq_MDU8pgeeeBgW-qpCKAIqf7uiY_XO8XJa7P7ehObGXxkakVhQYz06WT-VC5jOq9qduIkqPGnqyPgm4CNmjVNEtG8ero_lY0Z1yQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای کاربران رسانه های خارجی هم بسیار سوال بوده که چرا اینقدر به صنایع شیراز، صاایران حمله میشود. آنها با این عکس گفتند که پیجر و تجهیزات ارتباطی میسازد.
@WarRoom
اگه همین پیجرم درست میساخت چرا نداد به حزب الله که اونجوری لت و پار نشن؟
😁</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19195" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19194">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏جروزالم پست: جمهوری اسلامی از طریق میانجی‌ها پیشنهاد آتش‌بس ۱۰ روزه را به آمریکا داده است اما
ترامپ با آن مخالفت کرده و گفته که جمهوری اسلامی باید بهای اقداماتش رو بپردازد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19194" target="_blank">📅 14:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19193">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">@WarRoom
انتقاد محترمانه</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19193" target="_blank">📅 14:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دولت قطر با ارسال نامه‌هایی به رئیس شورای امنیت و دبیرکل سازمان ملل، رژیم جمهوری اسلامی را مسئول حمله به یک نفتکش قطری در ۱۶ تیر و شلیک موشک به خاک قطر در ۲۱ و ۲۶ تیر دانست و خواستار پرداخت غرامت شد. در حمله ۲۱ تیر، سه نفر از جمله یک کودک بر اثر سقوط ترکش‌های رهگیری موشک‌ها زخمی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19192" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی لحظاتی پیش از حمله به مکانی در ارتفاعات کوه بالای خرم آباد لرستان خبر داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19191" target="_blank">📅 14:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : فیلمی با عنوان «بمب افکن شبح» که در حالت دید در شب به چند خودرو حمله می‌کند، وایرال شده. این یک بازی شبیه‌سازی جنگ است ، لطفا دقت بیشتر بفرمایید.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19190" target="_blank">📅 13:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3212047c5f.mp4?token=n5VKyHmpUJ41P9HhDtTdJ5Kq3vJo363RlIbskhEsepMBY16u9rVTUbSVQl9DWVK2CeyIA9guDyZGHxyWNtuSiP_ItxFSA4HAUxBJmJwbm-c6hWbmAQtZESpDF1_6C0fRCMF0iSMpqORcFABq6K2-RaytjEx5ZOy9Zrk-gAvm2NIREMhHfJydVX4Ok8xISHIP6u5tYM-9votpCRsbeXFpwC1Qrp_h0K2vSfxspsWGP98KLb9yUiQEa3oXzE5pAjlsdJwL_AfZuq8xLemQRXidpJWgoQ7sE8rLq4zJA-B4kp2aGsmXnmFIFl11hawZScOCqb6KPDQR9GNi78UiVKM560KxGLWWiSHY40bCAHnCScRQxssSg_XwOw5I2a9YiGTOiUW8Vu0AryXWDHIInqSCAEbFs_9hESaJDatsTnnjnv0A01JwJzq05l4kHoXeboPBXqmkjQJNjGclFH73nkcJeEItkLoCuWy0gRdy5n7kQ0E72AZHV5iTQW9zzW7eVo6pFGDC2VnBo3N1CyR_Ye-Y8Bt-iGEyEXT7YoL2GOIRpAQmUeYCUbLzHWljvl1opCWCPxI9VUoqb81WIeAKSNRvGu1SGN1WWM--gwwvhLz0bOfJDoMYEAQgmQ5iMXvlCcTFUdGWOOtEHRzb_xz5ibjx5G14Uf8TQqHpoy7ajRTHyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3212047c5f.mp4?token=n5VKyHmpUJ41P9HhDtTdJ5Kq3vJo363RlIbskhEsepMBY16u9rVTUbSVQl9DWVK2CeyIA9guDyZGHxyWNtuSiP_ItxFSA4HAUxBJmJwbm-c6hWbmAQtZESpDF1_6C0fRCMF0iSMpqORcFABq6K2-RaytjEx5ZOy9Zrk-gAvm2NIREMhHfJydVX4Ok8xISHIP6u5tYM-9votpCRsbeXFpwC1Qrp_h0K2vSfxspsWGP98KLb9yUiQEa3oXzE5pAjlsdJwL_AfZuq8xLemQRXidpJWgoQ7sE8rLq4zJA-B4kp2aGsmXnmFIFl11hawZScOCqb6KPDQR9GNi78UiVKM560KxGLWWiSHY40bCAHnCScRQxssSg_XwOw5I2a9YiGTOiUW8Vu0AryXWDHIInqSCAEbFs_9hESaJDatsTnnjnv0A01JwJzq05l4kHoXeboPBXqmkjQJNjGclFH73nkcJeEItkLoCuWy0gRdy5n7kQ0E72AZHV5iTQW9zzW7eVo6pFGDC2VnBo3N1CyR_Ye-Y8Bt-iGEyEXT7YoL2GOIRpAQmUeYCUbLzHWljvl1opCWCPxI9VUoqb81WIeAKSNRvGu1SGN1WWM--gwwvhLz0bOfJDoMYEAQgmQ5iMXvlCcTFUdGWOOtEHRzb_xz5ibjx5G14Uf8TQqHpoy7ajRTHyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای نشان می‌دهند حملات آمریکا بر ورودی تونل‌های زیرزمینی پایگاه دریایی گروه تروریستی سپاه پاسداران در نزدیکی کنارک متمرکز بوده است. به نظر می‌رسد این مجموعه برای نگهداری تجهیزات و زیرساخت‌های نظامی حفاظت‌شده نیروی دریایی این گروه تروریستی استفاده می‌شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19189" target="_blank">📅 13:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKmpJe_n7dQUOPfu1HXFm_VNh_6OaUgc55B4Oo--iV2eA01VIdRATYzRC1IJKOLNCzbeEVEO6Tjtavas-XkwhxeabG27LZxuaZTvoTCPAot_7H6-ZMhVtf33BkWfIV8w3XMzd7ApQDX5Yke90xuG_WajNsfjYdULMMfdw78WpN9Owlw8_5qjytvE9pqQ0UinEaTga6VcK9UAoNWRk55CrhL7qMlJayEQ7KVG0MRA8bV3LTFWXHJf1wPBiK8o0RDP6zedGFhT58kYRNy5uEK5oIzGGfndl2Vj5JTZPi1aZyVpkceuGR6pfbPaoCniSf0IXTrmmjJBqtaXUEM2bEfvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۵ فروند دیگر از هواپیماهای سوخت‌رسان نیروی هوایی آمریکا احتمالا با یک اسکادران جنگنده وارد منطقه شدند و در پایگاه سیگونلا ایتالیا به زمین نشستند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19188" target="_blank">📅 13:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏وای‌نت گزارش داد مقامات ارشد اسرائیلی مدعی‌اند تیم جی‌دی ونس مانع دیدار نتانیاهو و پرزیدنت ترامپ می‌شود تا از اتخاذ مواضع تندتر علیه رژیم اشغالگر جمهوری اسلامی جلوگیری کند. عالیجناب نتانیاهو قصد دارد سفر خود را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تنها در صورت قطعی شدن دیدار با پرزیدنت ترامپ راهی آمریکا خواهد شد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19187" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پرتاب موشک جدید از شیراز/لار @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19186" target="_blank">📅 13:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پرتاب موشک جدید از شیراز/لار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19185" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پرتاب موشک از زنجان @WarRoom
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19184" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa3-Zjzq3-kSq8E2Ju_Ao1ncHI56vhbKABE1WV2qLq79Ix3DXA8IDwOj3szLHO7W0RgVc8i8dBlBzKdvAIBJdQErJlHDoBDcxXWVqo2ycNCmI49LDyRRZajcALEyxGuESw6GdwwxD9hZ-yLKdA58SeLk-5p6_eDRSJvHpeKRxXdjpjtZDWCI_oV2eS7GuDkm8nUipHVS5VO9rt_mTM72qx0_fl3226v8JDyblJJFWjB_kDIc5UNj-csjWnV1TYCviuD1PhZrMsws1V2XvBXluzR5R4pSH78vZ8RFr-PAFiMX12cTG418NA4leI2AwKh31ALcNUf4unCwkjHMZY5avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از زنجان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19183" target="_blank">📅 12:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارشات رسانه های عبری :
امریکا برای برخی حملاتش در خاک ایران از بمب افکن b52 استفاده کرده و همچنان استفاده خواهد کرد .
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19182" target="_blank">📅 12:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a274348cae.mp4?token=Ea3Zi7xYMGEfc4C3aEJbJjfk1XINQ1J7QAsczcpF5NfyHdiY5lV3LfLgljDn8k5Mr6hx60jrrS0lsCmBse75ioxi3Ad93EPWIYGldkl9PST3i9NON-2cdWtjzFGhLDrrl_RWLDUAxUhJh5uocMO8hqdkiIH_B4yAtYgN6s3YmsW7GIZlkNew5BBHKtULMq7PjnaJhy2n2cfuEDiCqjH8XB1vb1IHuTFgXRW450CgM1_bF4vn1Eaf_C30FFT9VKu823A4schnyCA1n-3G11WS9-OTF7L5Aka4sY7FeLNIRNaSrd2nOOAuLmMf78UPU5dCwFbvg-WQGw2eOz9O0rOzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a274348cae.mp4?token=Ea3Zi7xYMGEfc4C3aEJbJjfk1XINQ1J7QAsczcpF5NfyHdiY5lV3LfLgljDn8k5Mr6hx60jrrS0lsCmBse75ioxi3Ad93EPWIYGldkl9PST3i9NON-2cdWtjzFGhLDrrl_RWLDUAxUhJh5uocMO8hqdkiIH_B4yAtYgN6s3YmsW7GIZlkNew5BBHKtULMq7PjnaJhy2n2cfuEDiCqjH8XB1vb1IHuTFgXRW450CgM1_bF4vn1Eaf_C30FFT9VKu823A4schnyCA1n-3G11WS9-OTF7L5Aka4sY7FeLNIRNaSrd2nOOAuLmMf78UPU5dCwFbvg-WQGw2eOz9O0rOzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : نزدیک رصد خانه لار ، لانچر زدن
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19181" target="_blank">📅 12:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19180" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19179" target="_blank">📅 11:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292e2cf49c.mp4?token=gYGU2TPKBDG9aGxiDzXLUAIRTIroKg0cECVU8iwAxw92XMA3ALfZhpnhTpBEARsHxUhVK0lLoPWCU1QLzyWsb5LtUUMbUNSpzf10Qi0rPUFWAYKHuKLBcOIIZAe7dUCYs4BFB5b3jbnV9Vnomg1CB15bgdbdHyz1_QA7n54Uh8uN_yvWdKwZdn4Ot_ZN6KYR9GrwZLYrSxEj6LdN4gUGfJgQWdby3Jj2JboeZ_GjgTVdtz3dOnkZURWy3gWF2zWTm8UEEk6yXNcsmYqllGIaeW8mVO8Nw8RURtwmQ1mlRmoahgU9PHBHFHbM4zQyaG5J8iwfHPzRwF4_csroNaPIjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292e2cf49c.mp4?token=gYGU2TPKBDG9aGxiDzXLUAIRTIroKg0cECVU8iwAxw92XMA3ALfZhpnhTpBEARsHxUhVK0lLoPWCU1QLzyWsb5LtUUMbUNSpzf10Qi0rPUFWAYKHuKLBcOIIZAe7dUCYs4BFB5b3jbnV9Vnomg1CB15bgdbdHyz1_QA7n54Uh8uN_yvWdKwZdn4Ot_ZN6KYR9GrwZLYrSxEj6LdN4gUGfJgQWdby3Jj2JboeZ_GjgTVdtz3dOnkZURWy3gWF2zWTm8UEEk6yXNcsmYqllGIaeW8mVO8Nw8RURtwmQ1mlRmoahgU9PHBHFHbM4zQyaG5J8iwfHPzRwF4_csroNaPIjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تراپی
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19178" target="_blank">📅 11:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتاق جنگ با یاشار : آبنبات چوبی جدید رژیم : نمونه اولیه «گواهینامه موتورسواری زنان» چاپ شد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19177" target="_blank">📅 11:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba43159120.mp4?token=MVZKIyyc0K9E6WQc9ID8NmAbFANz2RkwzFsl63QY9UN0u0igYbtndynTSDG_Z7E164kdrzpaRO35SyH6aeXqnXicKTDgxIbJPik9NJLN-Mf_tp-ZBghNQXP03JpRQvdhVnjHgym4hqRPWGnWrwPsBDotHQVn4ULgWcCCvpqTJdULJxip7FHYXEmavQy1MYT5y3ORWCpgH8PwJk_FkUXXTRzf27oJWa9jVLY5Z0uIyeimTVyKxbfuOsMxpn33F7pyX7kT0VNVWN3zUqcWYBO0EMAZf126-TZz29aTf1WVoAS6zvFnXQXp-7bFZs36Cld3zBboKjO0J8QkZCftcmTV7YCUpLqXqQMhr7ZfaXOKTD_fgW-YinT6uKIxTh821PzhCklnbdi-fFo711CkuDPrMCOvVnI8FDjeV1ABv-R1LamnnhxmlpNCKniv4lwy_fJ93Cnl0unV5wlULeimc8kfRmAOHf5tOzI-seLApMgem17IwkKCrtkFbH4tAsYq9LtAqisD1GmIHeDl3oQ2HpDqZLotTaIw62M5EQHDI4qhUiXZqJBTSzoqUJ0EH9GMwBS-BVrLNpNmcvvDDB13Rm6lIyM9DlkhDfYbQXEua4MVpDo7w4iM29W8z0PP-Qbtybrj-oXaJ6uOr69VguHiROYojE4ONx2VRrbh5CnnlOmWtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba43159120.mp4?token=MVZKIyyc0K9E6WQc9ID8NmAbFANz2RkwzFsl63QY9UN0u0igYbtndynTSDG_Z7E164kdrzpaRO35SyH6aeXqnXicKTDgxIbJPik9NJLN-Mf_tp-ZBghNQXP03JpRQvdhVnjHgym4hqRPWGnWrwPsBDotHQVn4ULgWcCCvpqTJdULJxip7FHYXEmavQy1MYT5y3ORWCpgH8PwJk_FkUXXTRzf27oJWa9jVLY5Z0uIyeimTVyKxbfuOsMxpn33F7pyX7kT0VNVWN3zUqcWYBO0EMAZf126-TZz29aTf1WVoAS6zvFnXQXp-7bFZs36Cld3zBboKjO0J8QkZCftcmTV7YCUpLqXqQMhr7ZfaXOKTD_fgW-YinT6uKIxTh821PzhCklnbdi-fFo711CkuDPrMCOvVnI8FDjeV1ABv-R1LamnnhxmlpNCKniv4lwy_fJ93Cnl0unV5wlULeimc8kfRmAOHf5tOzI-seLApMgem17IwkKCrtkFbH4tAsYq9LtAqisD1GmIHeDl3oQ2HpDqZLotTaIw62M5EQHDI4qhUiXZqJBTSzoqUJ0EH9GMwBS-BVrLNpNmcvvDDB13Rm6lIyM9DlkhDfYbQXEua4MVpDo7w4iM29W8z0PP-Qbtybrj-oXaJ6uOr69VguHiROYojE4ONx2VRrbh5CnnlOmWtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : من کلاً شخصاً با افرادی که زیر پرچم جمهوری اسلامی به هر نحو و شکل، مخصوصاً رسانه فوق امنیتی صدا و سیما، کار کرده‌اند، موضع شخصی دارم و آرمان من این است که اگر پروموتی برایشان بکنم، خون و حق کسانی که اینگونه کارها را نکردند و زجر های بسیار و مهاجرت اجباری در زندگی خود متحمل شدند، پایمال میشود. در نتیجه این امر، هیچگونه مانوری بر روی این افراد نمیدهم و از آنجایی که شما خودتان عاقل و بالغ هستید و همچنین عادل فردوسی‌پور عزیز طرفداران زیادی دارد، تشخیص صلاح این مسائل با خود شخص شماست.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19176" target="_blank">📅 11:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19175">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝑹𝑺</strong></div>
<div class="tg-text">در مورد اتفاقات پیرامون عادل فردوسی پور چیزی نمیزارید؟</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19175" target="_blank">📅 11:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسرائیل در پی اجرای بخشی از توافق با دولت لبنان بصورت آزمایشی از روستای زوطر غربی عقب‌نشینی کرد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19174" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه وابسته به سپاه اعلام کرد:
زیرساخت مرکزی داده شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز هدف قرار گرفته است. طبق این گزارش، حمله متوجه بخشی از زیرساخت ابری و دیتاسنترهای منطقه‌ای آمازون (AWS) بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19173" target="_blank">📅 11:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">BTC : 66,000$
TETHER : 189,500 T
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19172" target="_blank">📅 11:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه‌های آمریکایی به گزارش‌های اطلاعاتی آمریکا اشاره کردند: تنش بین تهران و واشنگتن یک درگیری طولانی‌مدت است و بعید است که ایران به دلیل اقدامات نظامی آمریکا، مواضع خود را در مذاکرات تعدیل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19171" target="_blank">📅 11:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک حادثه دریایی در کریدور عبور جنوبی تنگه هرمز  تحت کنترل امریکا رخ داد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19170" target="_blank">📅 10:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19169">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارتش جمهوری اسلامی: ما عملیات‌های خود را ادامه خواهیم داد تا آمریکا را از ادامه حملات خود به کشور منصرف کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19169" target="_blank">📅 10:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19168">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رحیم زاهدی، مشاور وزیر علوم : يكي ان روياهاي كودكيم رقم خورد!
مادر تماس گرفت كه در فروشكاه اتكاي ازگل هست وبه دليل عدم استفاده روسري بهش تذكر دادن وگفتن از ارائه خدمات معذوريم بلا فاصله تماس گرفتم معاون وزير دفاع و رئيس سازمان اتكا، جوري شستمش كه كفت اين هفته با مادر برم پيشش و عذرخواهي بکنن
كلا ما چنين ابلاغ يا دستوري در دولت نداريم وجز سياست هاي أقاي پرشكيان علي الخصوص در زمان فعلي نيست هر نهادي به دليل بي حجابي بهتون خدمات ارائه نميده بيخود ميكنه وبايد باهاش برخورد شه
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19168" target="_blank">📅 10:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19167">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هم اکنون
نیروگاه برق الزور کویت هدف حمله پهپادی قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19167" target="_blank">📅 10:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19166">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ادعای آکسیوس: قطر، مصر، پاکستان و سایر میانجی‌های منطقه‌ای، طرحی را برای
آتش‌بس ۱۰ روزه به آمریکا و ایران
ارائه کرده‌اند.
در طول آتش‌بس ۱۰ روزه، تهران و واشنگتن در مورد یک
ترتیب بلند مدت برای عبور و مرور از تنگه
، مذاکره خواهند کرد.
یکی از گزینه‌ها به ایران اجازه می‌دهد تا
«هزینه‌های خدمات معقول»
را برای امنیت دریایی، حفاظت از محیط زیست و سایر خدمات دریافت کند .
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19166" target="_blank">📅 10:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19165">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKv-eb3lYdNexl6vQpurZcPjR3_L8Jd_vxcOjxo-I4bTpsbT5QtBiaiEoAAwC4-0QMc0PoJXC2yP5hRBkARd7vsHeHp29jIY9PhG8vnBROCAeVQCtKFDzFzafEZob7JMmOABvmFcyFfOriKbLmsryCAFD527UlFJRzZ_zDRB39XV9BGnq-OrS8JZ5uc5eMNX5NddoyYc3mE1cnnDFDG0OD_ooPm1ph42vrzl5YINg7EAN4WH8KUKiv0lSaFOzxxv8lQAJofSSqqjySwwY2SWdyGPZSDMfsUVMLOkNhzjzf7d-SjsN4ELCB5PsWMiYFIhgIXazemlyOzSWxSI0uJhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دفاعی اسرائیل (ارتش) و شاباک، رئیس بخش عملیات تیپ "شهر غزه" را به هلاکت رساندند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19165" target="_blank">📅 09:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19164">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار در اصفهان مهمات عمل نکرده است و اعلام شده از قبل
⚠️
⚠️
⚠️
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19164" target="_blank">📅 09:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19163">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک مقام اسرائیلی:
لازم است عملیات نظامی در منطقه "کوه کلنگ" در ایران انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19163" target="_blank">📅 09:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19162">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کامران غضنفری، نماینده سابق مجلس که حسن روحانی رو به جاسوسی برایMI۶، ارتباط با سرویس‌های خارجی، داشتن تابعیت انگلیسی و فساد فی‌الارض متهم کرده بود به ۱۳.۵ سال حبس محکوم شد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19162" target="_blank">📅 09:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد؛ اما ترامپ و اسرائیل به دنبال یک جنگ تمام عیار علیه ایران هستند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19161" target="_blank">📅 09:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a46db237.mp4?token=NVm7A2P-0bJG_XUbitFSnk7iYVIMZvQSpxmAFWCzdXMAZaVQpZ4MDhZHprbznmLWsQLDQsjTIO5zcTcBIckUnSeqmffdm8NPg-_pAeMp5bQBWCbGtLzVcqDEmBTQ_G7mLCrAy6DQlL9Onr9yhwWu-bKwup-QPxvljMYWh55eMp-V5eGpo5VQyoj-0ilKgfworNg_UAoVP91prQWp70Nzym3QA11IfxTEym5bcfuveU6qWfuyArX-T9W2U6wysgoSaekgLluGupxeL4BOPDRSZLOobvTijRz4n62Rx0nYxHOpRDYqwA4rpCZsT5_R_4C-lQ4fuOlycnSyfJ1Y8C0DRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a46db237.mp4?token=NVm7A2P-0bJG_XUbitFSnk7iYVIMZvQSpxmAFWCzdXMAZaVQpZ4MDhZHprbznmLWsQLDQsjTIO5zcTcBIckUnSeqmffdm8NPg-_pAeMp5bQBWCbGtLzVcqDEmBTQ_G7mLCrAy6DQlL9Onr9yhwWu-bKwup-QPxvljMYWh55eMp-V5eGpo5VQyoj-0ilKgfworNg_UAoVP91prQWp70Nzym3QA11IfxTEym5bcfuveU6qWfuyArX-T9W2U6wysgoSaekgLluGupxeL4BOPDRSZLOobvTijRz4n62Rx0nYxHOpRDYqwA4rpCZsT5_R_4C-lQ4fuOlycnSyfJ1Y8C0DRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: با باقی ماندن کمی بیش از ۱۰۰ روز تا انتخابات میان‌دوره‌ای، زمان برای رئیس‌جمهور ترامپ رو به پایان است تا پیش از حضور رأی‌دهندگان در پای صندوق‌های رأی، از این جنگ خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19160" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شاهزاده رضا پهلوی در گفتگو با «دات ریپابلیک مدیا نیوز»، گفت:
«می‌خواهم کاملا صادقانه بگویم، سه گروه متمایز وجود دارند که ما نمی‌توانیم با آن‌ها کار کنیم: عناصر طرفدار رژیم، مجاهدین خلق و تجزیه‌طلبان».
وی خاطرنشان کرد:‌
بگذارید در این مورد خیلی واضح بگویم. در مورد هر یک از اظهارات تیم من، ما اکنون قطعا سازوکارهای بسیار سخت‌گیرانه‌تری وضع خواهیم کرد. به این معنا که افرادی که ارتباط نزدیکی با من دارند، باید بیش از گذشته مراقب آنچه می‌گویند باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19159" target="_blank">📅 08:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19158">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پرتاب موشک از شیراز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19158" target="_blank">📅 08:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19157">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وال‌‌استریت ژورنال: اسرائیل مدعی انتقال هزاران سانتریفیوژ ایران به «کوه کلنگ» شد
. این سایت در عمق حدود ۱۰۰ تا ۱۴۰ متری کوه ساخته شده و به گفته کارشناسان، هدف قرار دادن آن بسیار دشوار است. اسرائیل معتقد است این انتقال می‌تواند تلاشی برای بازسازی ظرفیت غنی‌سازی ایران و محافظت از تجهیزات هسته‌ای در برابر حملات آینده باشد. آژانس بین‌المللی انرژی اتمی تاکنون اجازه بازرسی از این محل را نداشته است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19157" target="_blank">📅 07:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19156">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19156" target="_blank">📅 07:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اکسیوس:به گفته منابع آمریکایی و اسرائیلی، رئیس جمهور ترامپ به یک نقطه سرنوشت‌ساز در جنگ با ایران نزدیک شده است و دو گزینه اصلی پیش رو قرار دارد:
1.  آتش‌بس 10 روزه برای بازگشایی تنگه هرمز.
2.  یک عملیات نظامی گسترده با اسرائیل برای وادار کردن ایران به تسلیم.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19155" target="_blank">📅 07:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c0991007.mp4?token=Pg6KMX73rR6kQ0QQc1taJqgUmLp7JlCxlR_TDhF3tY1I6r3chr3Ph5Z0JKzLq4XNeisjVmzoQ08KncVAvgelAwvHcvqtPgUKZCbzmQH_nlcjbadA26vwSb6H-IqBgdaXQc1q0OKvp3dAa44KDnACSHyhHrxZF7S5cg2z0F07wgJm4Nv83ThtDGmyRR7lxqGet8IeQ2SCcjbuCgG-0ie5RJXCWFPkq7_5OxspZ4xAciQa9U_jSpXLG0PP2I89BovdebHpKtrpyj-nf7fHqoXWEeKKtCBgpoIxKba5b9BDybAaTRvir2sG2LsnxxQzJYZRaMGQWa46j3x5g4PGmBexsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c0991007.mp4?token=Pg6KMX73rR6kQ0QQc1taJqgUmLp7JlCxlR_TDhF3tY1I6r3chr3Ph5Z0JKzLq4XNeisjVmzoQ08KncVAvgelAwvHcvqtPgUKZCbzmQH_nlcjbadA26vwSb6H-IqBgdaXQc1q0OKvp3dAa44KDnACSHyhHrxZF7S5cg2z0F07wgJm4Nv83ThtDGmyRR7lxqGet8IeQ2SCcjbuCgG-0ie5RJXCWFPkq7_5OxspZ4xAciQa9U_jSpXLG0PP2I89BovdebHpKtrpyj-nf7fHqoXWEeKKtCBgpoIxKba5b9BDybAaTRvir2sG2LsnxxQzJYZRaMGQWa46j3x5g4PGmBexsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : گوشه ای از تصاویر شب دهم حمله به ایران
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19154" target="_blank">📅 07:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سنتکام : پایان شب دهم
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد
دور دیگری از حملات علیه ایران
در
۲۰ ژوئیه، ساعت ۹:۰۰ شب به وقت شرق آمریکا (ET) (۰۴:۳۰ بامداد ۳۰ تیر به وقت تهران)
به پایان رسید.
نیروهای آمریکایی
مراکز فرماندهی نظامی، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد، و سامانه‌های پدافند هوایی ایران
را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری که از
تنگه هرمز
عبور می‌کنند، کاهش یابد.
عبور کشتی‌های تجاری از این
گذرگاه حیاتی بین‌المللی دریایی
همچنان ادامه دارد. از
اوایل ماه مه
تاکنون، نیروهای سنتکام به تسهیل عبور
حدود ۹۰۰ کشتی تجاری
و
۴۵۰ میلیون بشکه نفت خام
کمک کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19153" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نقاطی که در شب دهم مورد حمله ارتش آمریکا قرار گرفته‌اند:
💥
شیراز
💥
چابهار
💥
بندرعباس
💥
جزیره قشم
💥
سیریک
💥
بندر لنگه
💥
بوشهر
💥
کنارک
💥
کرمان
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19152" target="_blank">📅 06:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:مکالمه خیلی خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام داشتم. موضوعات زیادی را بررسی کردیم، از جمله رابطه ویژه‌ای که با بریتانیا داشتیم. به زودی برای موضوعات مورد علاقه مشترک ملاقات خواهیم کرد.
نخست‌وزیر وظیفه بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا. من آنجا خواهم بود تا کمک کنم! درباره نفت دریای شمال، تجارت، اتحاد نظامی و پاکسازی مین‌ها از تنگه هرمز و موضوعات دیگر صحبت کردیم. مکالمه جالب بود و خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت و انتظار خوب کردم!
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19151" target="_blank">📅 01:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">همین الان پایگاه هوایی بندر عباس رو سنگین زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19150" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">داداش الان سیریک طی ۱۰دقیقه ۵ انفجار قشنگ و محکم زد
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19149" target="_blank">📅 01:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE4KhJajnwro27uK7ggZW1h4_9VuPwaePPYf2angf8Tcv5OVyuRvnSj6MyeVgS3VKfAhHtGV9A16ROnDCRxIC1XeVAqrDBoUI-7pz97UtAHbhZGv6pTSmjH3Ve_-rM5YqaKq6mfpVQQHYRVB_nrU0zyMZszJFC96_KzS87drRR-Sh1gubi6ANKd_LTKNGR-u0Q2suWGRnQGXwi-Z1Ee0I50i1s91tUbZSDm9dqeB7cEg4Qm83XES7WUA7GYpznlVF4SrH7Nh9K0_l262wHhsrnLQZGK0JfvPFw_ON3fUXG7Z5pF7C2SJ2U6IIHMcQpCDg8usKhTO8OPsXLXEEKyyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان UKMTO گزارشی از حادثه‌ای در ۸ مایلی شمال شرقی لیما، عمان دریافت کرده است. مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ VHF گزارش می‌دهد که توسط یک پرتابه ناشناخته در تنگه هرمز مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19148" target="_blank">📅 01:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19147">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19147" target="_blank">📅 01:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19146">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش تایید نشده از حمله به نیروگاه بوشهر ، ممکنه مثل قبل‌ پدافندش رو زده باشن
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19146" target="_blank">📅 01:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19145">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش صداری ‌انفجار‌ جدید شیراز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19145" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19144">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">درود رئیس اتاق جنگ
خوشحال شدم رسیدن به جیرفت (کرمان)
بزنن هرچی مقر سپاه توی این استان هست با خاک یکی کنن. هرچی میکشیم زیر سر قاسم و لشکر ۴۱ ثارالله و این سپاهه. جیرفت و بافت معدن سپاهیاست. البته توی این استان کم نیستن. به امید اینکه اعلام کنی تک تکشون پودر شدن.</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19144" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19143">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اسرائیل اینش خوبه که قبلش میگه ! پل ها رو هم باید اعلام میکردن ! پل‌که در نمیرفت ! فرمون باید دست بی بی باشه  تا این راه بیفته پیر میشیم</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19143" target="_blank">📅 01:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19142">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خداروشکر حمله ها کاملا فقط پایگاه های نظامی هست و امروز تا الان مردم عادی آسیبی ندیدند
😍</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19142" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19141">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چابهار همینجور میزنند
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19141" target="_blank">📅 01:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19140">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a96706789.mp4?token=IYb2UoMxA6qq5_AHBrS9lV86UM85sdYup-PIFUhyvxGg6joFILYAenxOgCUZM-L9mrcbjqTYQyRESKrU8BMoc_C7VMI7hGhrfrKAy6qMEF6JoEBodt_-KZtXI_Co_6Ak3mPEOYenVIDq303RoUKqCsPJhJu0NQd3XR3iCkf2t3_CHdP2cUw5L1e3t6kVdEYZ-J5CYFyEs8c6AkQGyI7nHuX-TcxVQiHEW4mHZrjZupJQueh39zwfLWSsHVNMf-OSDgNFrRj2iwyQ_pMaPq27qlLPOqRzvkqR73CSkdkT4GldZE3fdn0CiCkcgwS1F8KgFxpSmKw9LKjXtgFgpZS4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a96706789.mp4?token=IYb2UoMxA6qq5_AHBrS9lV86UM85sdYup-PIFUhyvxGg6joFILYAenxOgCUZM-L9mrcbjqTYQyRESKrU8BMoc_C7VMI7hGhrfrKAy6qMEF6JoEBodt_-KZtXI_Co_6Ak3mPEOYenVIDq303RoUKqCsPJhJu0NQd3XR3iCkf2t3_CHdP2cUw5L1e3t6kVdEYZ-J5CYFyEs8c6AkQGyI7nHuX-TcxVQiHEW4mHZrjZupJQueh39zwfLWSsHVNMf-OSDgNFrRj2iwyQ_pMaPq27qlLPOqRzvkqR73CSkdkT4GldZE3fdn0CiCkcgwS1F8KgFxpSmKw9LKjXtgFgpZS4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوش این نیز بگذرد…
❤️‍🩹
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19140" target="_blank">📅 01:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19139">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">استاندار اصفهان: صدای انفجار در اصفهان تایید میشه ولی بخاطر حملات نبوده و دلیلش درحال بررسیه @WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19139" target="_blank">📅 01:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ffff35e3.mp4?token=t_ETt_wISLF3GmvSb8HKz5rkadfpg_0YIX3AFBAs1CELTf-K3sZCNzzl1jmm313asqTfGLeGmif6gp38KAHXK4BwYH9jhfCD6bSQgh0D615-Wjs9UHSYNMz8vZ086j01RmsCw5XPdFit0xhNg-2LlbGmmGhe7R1nLm9lSs86w9EPn96yL-OzWOqGYtnvH7fMPpx3wXIxJJNP6vtxAg-CmtIQ6mF7oyNSAKEt-2JEse1dC6bclrD3kA9DnPSZNCG2uV3RJmAOVdizdkO19lZ6vI_SV0QbOnFo3SB59VyugGYcGR4DLkMamjttfwA7dbQ-GnxVu-1uBY7Wa76hBRXHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ffff35e3.mp4?token=t_ETt_wISLF3GmvSb8HKz5rkadfpg_0YIX3AFBAs1CELTf-K3sZCNzzl1jmm313asqTfGLeGmif6gp38KAHXK4BwYH9jhfCD6bSQgh0D615-Wjs9UHSYNMz8vZ086j01RmsCw5XPdFit0xhNg-2LlbGmmGhe7R1nLm9lSs86w9EPn96yL-OzWOqGYtnvH7fMPpx3wXIxJJNP6vtxAg-CmtIQ6mF7oyNSAKEt-2JEse1dC6bclrD3kA9DnPSZNCG2uV3RJmAOVdizdkO19lZ6vI_SV0QbOnFo3SB59VyugGYcGR4DLkMamjttfwA7dbQ-GnxVu-1uBY7Wa76hBRXHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار پادگان امام علی
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19138" target="_blank">📅 01:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">استاندار اصفهان: صدای انفجار در اصفهان تایید میشه ولی بخاطر حملات نبوده و دلیلش درحال بررسیه
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19136" target="_blank">📅 01:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش انفجار شیراز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19135" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19134">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">تحلیلگر ارشد</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19134" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
