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
<img src="https://cdn4.telesco.pe/file/Ml7TZqxbaiyyDsI-0ITTrK0lpT59cTsxjXnDQHGIjjpeEZ1cYn78JwS_B2gN7Virv6MT1fnrXY2duJxqYAqXYpXCSS2ZTJAr8VIyXcXkZzh4E9kSHEXApyMAqi6xnPB_CvbIBM3VPcAacmKlCVVgyb2XRSCx856OtAeUJZ9VJvJ9ZoUplQUUMU42_bGVlcHyt-HEC71SUox-xU6HBWtUBjkKptXr0BXs24YpNmxAXHKJ-chUNGTQMwZh0kNxwh4I-Z0JEkvcMx9O77u0l5tV9SZszdLkv6plL66TqWXsVzgdyq_JjOYWVvEZTEOWCgeUWOKk5svrnunin8fUSyP3zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-451895">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d7d5c206.mp4?token=CWnbOLcY-e7Uz7ykilYGWpHOpxUgBDOsv8iizMw1NUs7KYYtK1EhcXMVVQ7uKdrvqIgRhBmxWT1FQ04JcSbzoxJaSKhzx8IdYa4CsM0oGOa4OXu5-u4VcUcVgH1RzKAL9rWh7dOA_SV41TV7q4_0grsmbV5OXFkwOFayRyEEu5IZxpfZQ99A2QftetHzbXv2qhNKUyPaBvpbm4fur7Ymm8uo66MnrhtU66TUT6NCOmpdZzxVTce2v20ZUvKJ3lhPn6G45jC4oSUkaiwJnZ2611WqE8bUwqU68ixlnSrqRAt-PKRYv8dZEvqkKHwktsCcmEk3Rck9PCdS3MQ3VsONrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d7d5c206.mp4?token=CWnbOLcY-e7Uz7ykilYGWpHOpxUgBDOsv8iizMw1NUs7KYYtK1EhcXMVVQ7uKdrvqIgRhBmxWT1FQ04JcSbzoxJaSKhzx8IdYa4CsM0oGOa4OXu5-u4VcUcVgH1RzKAL9rWh7dOA_SV41TV7q4_0grsmbV5OXFkwOFayRyEEu5IZxpfZQ99A2QftetHzbXv2qhNKUyPaBvpbm4fur7Ymm8uo66MnrhtU66TUT6NCOmpdZzxVTce2v20ZUvKJ3lhPn6G45jC4oSUkaiwJnZ2611WqE8bUwqU68ixlnSrqRAt-PKRYv8dZEvqkKHwktsCcmEk3Rck9PCdS3MQ3VsONrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: دیتاسنتر عظیم دشمن در امارات در جنگ تحمیلی سوم نابود شد
🔹
این دیتاسنتر در طول ۲۰ سال با کمک و سرمایه‌گذاری اروپایی‌ها، رژیم صهیونی و آمریکا در امارات برای کنترل منطقه ایجاد شده بود.
🔹
همه سرمایه‌گذاری‌های آمریکا در طول ۵ دهه در منطقه با نابودی…</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/farsna/451895" target="_blank">📅 15:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451894">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
عربستان از فعال شدن هشدارهای زودهنگام در شهر الدمام خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/451894" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386a38abce.mp4?token=eT4TaNzdbu9_6OgoPmxMbRsdzaOrYjLftQivAnx0LM8AAuNsXJa4a0bsc7JwDMuLdvobScuO4ig7hq1DHeG4sw5WZcini0Sy0RNt5B1jUwzIgNG89SMnUhXFPe7ZznTnSXeaJ38_ayzN48FJVVHKXnAMZ1_0DOxCHYQA7u2QVZ9xiDOgfSTYqlAY6ABWTY7HCrIZnv4_cYvZCa4Yo4eejoVWCYlnxEtqQBf-747nS47SbVplePHeCYP6BNHjY2EcSj1TDKIPi4xLGxnUr2p3KhibSgp1Eew82IeWpYorRSWQoN3PneZHIf8ZKDrbngAu0oIJjKxOlc1AanGIIxCIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386a38abce.mp4?token=eT4TaNzdbu9_6OgoPmxMbRsdzaOrYjLftQivAnx0LM8AAuNsXJa4a0bsc7JwDMuLdvobScuO4ig7hq1DHeG4sw5WZcini0Sy0RNt5B1jUwzIgNG89SMnUhXFPe7ZznTnSXeaJ38_ayzN48FJVVHKXnAMZ1_0DOxCHYQA7u2QVZ9xiDOgfSTYqlAY6ABWTY7HCrIZnv4_cYvZCa4Yo4eejoVWCYlnxEtqQBf-747nS47SbVplePHeCYP6BNHjY2EcSj1TDKIPi4xLGxnUr2p3KhibSgp1Eew82IeWpYorRSWQoN3PneZHIf8ZKDrbngAu0oIJjKxOlc1AanGIIxCIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: آمریکایی‌ها هر سلاحی برای جنگ جهانی سوم کنار گذاشته بودند علیه ایران بکار گرفتند
🔹
سخنگوی ارشد نیروهای مسلح: دشمن در جنگ تحمیلی دوم فکر می‌کرد ظرف یک هفته نظامی جمهوری اسلامی را سرنگون و هفته بعد هم ایران را تجزیه می‌کند.
🔹
باتوجه به دو عملیات…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/451893" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a82f3c1b.mp4?token=aLbD7-mgV9NnytDsrr_13c7A2dXALuYjlkMEM98kqIu_inyATgiOJ7VLLH0pAzYpAI5ExBJRdIEmUjHzCKI1vZV_Dc8k6tK-fpFjXUxqFeESnbPYjKcd43qQWi4ng96f_sKeSDMGl1uk7ryw2V2MdrnGsysajeHdP9__N5wvR3qIS1usOj2eOeylB2YnYqnx1auXkKERxPuC1ge1dSPLWbfb8rHBU3QLEhmgH_YDsREzZ1tpHwWmzqvLKaSsepd__OBL9RVud6nwPf82lQtL-H124wtrnspkTUR-5b_dGSh9_R0_3ixnWNgZb7Knn-FmzxjBYoMTPFN_Bd59n_vq8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a82f3c1b.mp4?token=aLbD7-mgV9NnytDsrr_13c7A2dXALuYjlkMEM98kqIu_inyATgiOJ7VLLH0pAzYpAI5ExBJRdIEmUjHzCKI1vZV_Dc8k6tK-fpFjXUxqFeESnbPYjKcd43qQWi4ng96f_sKeSDMGl1uk7ryw2V2MdrnGsysajeHdP9__N5wvR3qIS1usOj2eOeylB2YnYqnx1auXkKERxPuC1ge1dSPLWbfb8rHBU3QLEhmgH_YDsREzZ1tpHwWmzqvLKaSsepd__OBL9RVud6nwPf82lQtL-H124wtrnspkTUR-5b_dGSh9_R0_3ixnWNgZb7Knn-FmzxjBYoMTPFN_Bd59n_vq8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: آمریکایی‌ها هر سلاحی برای جنگ جهانی سوم کنار گذاشته بودند علیه ایران بکار گرفتند
🔹
سخنگوی ارشد نیروهای مسلح: دشمن در جنگ تحمیلی دوم فکر می‌کرد ظرف یک هفته نظامی جمهوری اسلامی را سرنگون و هفته بعد هم ایران را تجزیه می‌کند.
🔹
باتوجه به دو عملیات وعده صادق ۱ و ۲ و رزمایش‌های اقتدار آسیب‌شناسی کردیم و بانک اهداف تعیین شده و برنامه‌ریزی داشتیم.
🔹
دشمن در هفدهم و هجدهم دی‌ماه می‌خواست کودتا را با جنگ سخت ترکیب کند اما ملت ایران نقشه دشمن را ناکام گذاشت.
🔹
در جنگ تحمیلی سوم رهبر شهید برای جبران خلاء خودشان و فرماندهان کاملا برنامه ریزی کرده بودند.
🔹
هر سلاحی که در دنیا آزمایش شده بود اما به‌کارگیری نشده بود در جنگ با ایران استفاده شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/451892" target="_blank">📅 15:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451891">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
عربستان از فعال شدن هشدارهای زودهنگام در شهر الدمام خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/451891" target="_blank">📅 15:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451890">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/451890" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd44dfad6f.mp4?token=W8s0eqdGTYNeHeApgBH6GOzM62EFPkKI0RDW7JG8cHV0vaPtQ-Agj5ZkHoCFXev7pxaIGSxf8rfLbFA-q2NrB66wDmjsCsw2n2z0p24z0xRDlnRfMzifUdR5sl0gl32-Nwb8bDxpnscK9x8n4cYQnuzMMvyrzNra7jXKQdSneuP8n0DYYPa7jq95H6Is6pRGg1hjU67pVOUhHRFhzTgaLNj5ijLz8GaXdAYIQCq9XpzaXigsLLgZM1ENnJA5Veoj4ZOsNRHO3eJ-Cw--n4bYVocuNbUfEr8wGH7JtcJ7PiKWrNArtys993FHBtTdkrxcwYw5CLZA70Yvea1Mfow2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd44dfad6f.mp4?token=W8s0eqdGTYNeHeApgBH6GOzM62EFPkKI0RDW7JG8cHV0vaPtQ-Agj5ZkHoCFXev7pxaIGSxf8rfLbFA-q2NrB66wDmjsCsw2n2z0p24z0xRDlnRfMzifUdR5sl0gl32-Nwb8bDxpnscK9x8n4cYQnuzMMvyrzNra7jXKQdSneuP8n0DYYPa7jq95H6Is6pRGg1hjU67pVOUhHRFhzTgaLNj5ijLz8GaXdAYIQCq9XpzaXigsLLgZM1ENnJA5Veoj4ZOsNRHO3eJ-Cw--n4bYVocuNbUfEr8wGH7JtcJ7PiKWrNArtys993FHBtTdkrxcwYw5CLZA70Yvea1Mfow2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: ما خرمشهرها در پیش داریم، اولین خرمشهری که باید آزاد کنیم ذهنمان است
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/451889" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8785a722d0.mp4?token=vWOt4wzcMJWT2KZmZRhKwuFEb21ZVDW9IAxcf6ZdOlDEyPc01hTKwRovmiDaMPZbFXi8ssJ5s7SOK-tKVTurEBA7y-wWrkXkx0cjLHGlC8TlFiYZkWK6_3CQIw204wFzmX_nBqO3MBFAzxHA6Y8HIR3fPyJRnphUb5t5IL6XQIWt5vgg1ZB5F6le9fiF7G67KQ_0q12dOVDtFYKCXakijZVnPMAcxpWmGX-EgEgTyUvm3b0SfdLpSzaSIdvNCydVbkgVSJZ1vghUSFgLL_Nde7y6dkiWA-TmNNEvUn3Si-roxrYtgSqZ9fTjyQhPoyfQ5GgfA34EWO1CyOwWs9dOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8785a722d0.mp4?token=vWOt4wzcMJWT2KZmZRhKwuFEb21ZVDW9IAxcf6ZdOlDEyPc01hTKwRovmiDaMPZbFXi8ssJ5s7SOK-tKVTurEBA7y-wWrkXkx0cjLHGlC8TlFiYZkWK6_3CQIw204wFzmX_nBqO3MBFAzxHA6Y8HIR3fPyJRnphUb5t5IL6XQIWt5vgg1ZB5F6le9fiF7G67KQ_0q12dOVDtFYKCXakijZVnPMAcxpWmGX-EgEgTyUvm3b0SfdLpSzaSIdvNCydVbkgVSJZ1vghUSFgLL_Nde7y6dkiWA-TmNNEvUn3Si-roxrYtgSqZ9fTjyQhPoyfQ5GgfA34EWO1CyOwWs9dOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ چطور هر روز پیروز می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/451888" target="_blank">📅 15:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
عربستان از فعال شدن هشدارهای زودهنگام در شهر الدمام خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/451887" target="_blank">📅 15:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ec99538e.mp4?token=BcUOWEu3fDlChkVBh6617eN-3llGuU5Glskh62Swj60SciR9A6C9IqNTt4fPeHv_dGGUGtwHWiGOeDoRgKNaOyA1Pa1lMYFEGi56rUtD1M5ZIjisrmn4veh6N0uPKsUI9oiWMiaTQeNvrFDayolT4xlq4BlspbdwvpS6g9Y0cQdvxRmQgCwTLtAOCHk5i9anAzhqiBtSDjwNVFQgZeDh5i1f64KFXu32E44OaVaU84erg0hesVuPCFdct8SWRb12-ScCJGoPDos_qlrzhL99zHkLN0YPn8g5zSmZ1yl25l5kSk6LNMvMmUczsIqK_FVxXd7ySPawgEcZwXFebfBA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ec99538e.mp4?token=BcUOWEu3fDlChkVBh6617eN-3llGuU5Glskh62Swj60SciR9A6C9IqNTt4fPeHv_dGGUGtwHWiGOeDoRgKNaOyA1Pa1lMYFEGi56rUtD1M5ZIjisrmn4veh6N0uPKsUI9oiWMiaTQeNvrFDayolT4xlq4BlspbdwvpS6g9Y0cQdvxRmQgCwTLtAOCHk5i9anAzhqiBtSDjwNVFQgZeDh5i1f64KFXu32E44OaVaU84erg0hesVuPCFdct8SWRb12-ScCJGoPDos_qlrzhL99zHkLN0YPn8g5zSmZ1yl25l5kSk6LNMvMmUczsIqK_FVxXd7ySPawgEcZwXFebfBA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به مرکز توزیع شرکت تجارت الکترونیک وایلدبریز کراسنودار روسیه
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/451883" target="_blank">📅 15:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/451882" target="_blank">📅 15:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eccd805d5c.mp4?token=Cxt38npDg3bG7NDn5hV0Vd9TtAXW4633OY8TZ4qBF3i5AxnfmdaSOyy_4ia9eqGepvc5dTyyGb6II4qtVPdMQJnbCzzmd478pBpIsZFWXtHfd8tUu1PIbdTKxsw-WIBnIKr4rD6SORz63PupWT8hanma1ebc0N56-ZHV-FlW-1CAgTd5fMT1_Ea8J5jCXMeRI6FFQjph3-SwxiQ8tWq-jcQKJO3yDzsAQrdsbJnw0ENoZyWh5aWD00MSqikADkXfvdMIJByfgW1mhcTElHInPXkOBgkx4GGoe3Sdr-0hhiFu_XTOcTDzYM5fWjHncNTpXHm0czXQoHkY237LE7ze8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eccd805d5c.mp4?token=Cxt38npDg3bG7NDn5hV0Vd9TtAXW4633OY8TZ4qBF3i5AxnfmdaSOyy_4ia9eqGepvc5dTyyGb6II4qtVPdMQJnbCzzmd478pBpIsZFWXtHfd8tUu1PIbdTKxsw-WIBnIKr4rD6SORz63PupWT8hanma1ebc0N56-ZHV-FlW-1CAgTd5fMT1_Ea8J5jCXMeRI6FFQjph3-SwxiQ8tWq-jcQKJO3yDzsAQrdsbJnw0ENoZyWh5aWD00MSqikADkXfvdMIJByfgW1mhcTElHInPXkOBgkx4GGoe3Sdr-0hhiFu_XTOcTDzYM5fWjHncNTpXHm0czXQoHkY237LE7ze8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدافعان جزیرۀ بوموسی آمادۀ مقابله با گزافه‌گویی‌های ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/451881" target="_blank">📅 15:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b20c00b5.mp4?token=sQ2SXz44pexFOjmoxBbwOUd7sM6a5D_zm1HycueFcrKAjpqDwVnQJICSZ44sTVbALjCsOilJJs7VufYbwmFutYpA6csbaHEULKSZho7ce6Bp0qoBqXbUujiO1mLOg3X4QBu8IWWDIowvn0vdJB-kh8p3wFEi_FFmF3hale_JtP6g5bAOUBQZ37AaOzpA2wnkzxMSAX-Mu93H2dyf_DNsO66OCdLst4u0xkv68mBSiTP8WJuCn4zuiA9K-wdvNm9s4X45Nh0Sf-d-tcOpC2LVgnWNvSo--VtW8DVMKMdtI5dLUfYXZmvU_HVBWd8wZE8_7QGhYB-0wCADsuOmFEfr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b20c00b5.mp4?token=sQ2SXz44pexFOjmoxBbwOUd7sM6a5D_zm1HycueFcrKAjpqDwVnQJICSZ44sTVbALjCsOilJJs7VufYbwmFutYpA6csbaHEULKSZho7ce6Bp0qoBqXbUujiO1mLOg3X4QBu8IWWDIowvn0vdJB-kh8p3wFEi_FFmF3hale_JtP6g5bAOUBQZ37AaOzpA2wnkzxMSAX-Mu93H2dyf_DNsO66OCdLst4u0xkv68mBSiTP8WJuCn4zuiA9K-wdvNm9s4X45Nh0Sf-d-tcOpC2LVgnWNvSo--VtW8DVMKMdtI5dLUfYXZmvU_HVBWd8wZE8_7QGhYB-0wCADsuOmFEfr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایگاه‌های آمریکا در منطقه زیر رگبار حملات پهپادی ارتش
🔹
روابط‌عمومی ارتش: در دور جدید حملات پهپادی عملیات صاعقه، از بامداد امروز «ساختمان‌های اسکان و رفاهی» و «انبار تجهیزات» ارتش تروریستی آمریکا در پایگاه الازرق اردن را هدف حملات پهپادی قرار داد.
🔹
همچنین…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/451880" target="_blank">📅 15:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: ملت عظیم الشأن و به پاخاسته ایران اسلامی؛ حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های…</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/451879" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbQpOGjdNuvzLNZ-OzF1DYD58ScX3_CQ8ar5BOSD3lokI4ihVUUA-4UHJUAmp4-3YQRO4NGca6PmXT0COzFTkyPEyNe38Vrsv0pft8fWos2sqBzWrtWPV8gJrCL3ZyWsO3BWrZG-Ir2JkFRxPGbExzPzUQZ9aqdfGRgo8jcQsdqEoIZQ6hO7ixRCWMV1oSpwacb3tuMyvIwESjUUDriix-mFW0ArkZmFcBCmt_SRa7nuUt_x4VP8jmkEOWJj10wMDtDNum_qLC7i4bIhYXp0watpkmsYgSnvcMyxTkE8McXdJopWTsn-CLX3IklDUoMd7kzmKXUXVL_Vo9m80b5AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: هیچ فعالیت هسته‌ای در کوه کلنگ وجود ندارد
🔹
سخنگوی وزارت امور خارجه امروز با بیان اینکه فعالیت‌های هسته‌ای ایران بر اساس تعهدات پادمانی به آژانس اعلام شده، گفت: تمرکز بیمارگونه آمریکا بر کوه کلنگ که هیچ فعالیت هسته‌ای در آن وجود ندارد، چیزی جز بهانه‌جویی برای تخریب و ویرانگری نیست.
🔹
بقائی پرسید: راستی، مدیرکل آژانس بین‌المللی انرژی اتمی و نامزد دبیرکلی سازمان ملل کجاست؟!
🔹
سخنگوی دستگاه دیپلماسی تصریح کرد: ایرانیان با تمام توان در برابر کینه‌توزی آمريکا و هرگونه تعرض به حاکمیت و امنیت ملی کشورشان می‌ایستند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/451876" target="_blank">📅 14:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=bY_3Vz8prRrvtYRtHYlmqO1is-LosOpQi1sMA3atwvPNC9A5OFDv09TPZpH8vlD45uCC81fuJ7nP4DXHRJt1r5Ec6kUTKv8jr0ylW9qznrrjKKxqDx4avOC5lSzL-v6aJPWschkq3xaZZV3I5ylz3rQjY9zy8uT5RBMXuxbBnUzlz_lyNwkMkllznh6kkDwE8Mv4UZKLZ_qZexBtKq6POSnuKo9qfqZ2L7NZVFZc4s4a9NaEA1040Z1HwyW_5PY32E1rq5gX3a7NS0mZnUvrerpEy5qLxX7O503-GostviJfKWItJ8pi_gyIPTDW6aZFRt1-XO-MUQBCYQhE7uBujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=bY_3Vz8prRrvtYRtHYlmqO1is-LosOpQi1sMA3atwvPNC9A5OFDv09TPZpH8vlD45uCC81fuJ7nP4DXHRJt1r5Ec6kUTKv8jr0ylW9qznrrjKKxqDx4avOC5lSzL-v6aJPWschkq3xaZZV3I5ylz3rQjY9zy8uT5RBMXuxbBnUzlz_lyNwkMkllznh6kkDwE8Mv4UZKLZ_qZexBtKq6POSnuKo9qfqZ2L7NZVFZc4s4a9NaEA1040Z1HwyW_5PY32E1rq5gX3a7NS0mZnUvrerpEy5qLxX7O503-GostviJfKWItJ8pi_gyIPTDW6aZFRt1-XO-MUQBCYQhE7uBujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: ملت عظیم الشأن و به پاخاسته ایران اسلامی؛ حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های گذشته به بهانه تلافی انفجار کشتی‌های متخلف انجام می‌شد.
🔹
شب گذشته هم که با وجود وسوسه خدمه کشتی‌ها، هیچ شناوری جرات آزمون عبور از مسیر غیرقانونی جنوب تنگه را نکرد، و طبعاً انفجاری هم رخ نداد، ارتش کودک‌کش آمریکا خوی تجاوزگری را کنار نگذاشت و حمله هوایی و موشکی به تعدادی از مراکز نظامی و غیرنظامی ما را تکرار کرد و اینک در حال دریافت پاسخ‌های کوبنده است.
🔹
با توکل به خدای متعال، رزمندگان شجاع هوافضای سپاه در پاسخ به تجاوزات دشمن در موج ۲۵ عملیات نصر ۲ با رمز مبارک یا حسن ابن علی (ع) و تقدیم به شهدای مدرسه شجره طیبه میناب، پایگاه‌های آمریکایی در اردن را یک بار دیگر در هم کوبیدند.
🔹
در اولین مرحله پاسخ در حمله موشکی و پهپادی به پایگاه‌های ملک فیصل و پرنس حسن یک سوله آماده سازی اف ۱۵ هدف قرار گرفت و همچنین در حمله به یک سوله آماده‌سازی پهپادها، هشت پهپاد MQ 9 نو و آکبند در بسته‌های خود قبل از آماده‌سازی به طور کامل منهدم گردید و به دو فروند از آنها که در محوطه بودند خسارت سنگین وارد آمد.
🔹
در حمله بعدی به سوله نگهداری بالگردها خسارت اساسی به دو فروند بالگرد سنگین آمریکایی وارد آمد.
🔹
در حمله به یک مرکز اسکان نیروهای متجاوز، تعدادی از آنها کشته و زخمی شدند.
🔹
عملیات تنبیه متجاوز ادامه دارد، چرا که اگر متجاوز تنبیه نشود و هزینه سنگینی بابت عهد شکنی و زیر پا گذاشتن توافقات نپردازد، تصور خواهد کرد که هر وقت اراده کند می‌تواند جنگ را از سر گیرد و هر وقت تحت فشار قرار گیرد به آن خاتمه دهد و چرخه جنگ، مذاکره و باز هم جنگ را تکرار کند و سایه جنگ را دائماً روی سر ما نگه دارد.
🔹
تنها راه احیای بازدارندگی و برقراری امنیت پایدار، اجرای فرمان قرآن است که می‌فرماید "و قاتلوهم حتی لا تکونوا فتنه".
🔹
برای دور کردن دائمی سایه جنگ از کشور جز ایستادگی و تحمیل هزینه سنگین به متجاوز راهی نیست اگر این پاسخ‌ها اکتفا نکند و تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451875" target="_blank">📅 14:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ee3caa25d.mp4?token=uf9dTfg1c0oen6LdMr6YGcje-e4hwRq6ykFbyN7hoQOZLWrWEQ4tRJIPMeRclmmBCCq2jYu-Eq7qHuef7AXLJSENP6h1yXLtJnJA6_9wEnFkKzn9Arbg114PhFfKtZbC3J_PfhvpYWg87Z6v1jD54HkJ6S5jdqmdm3aCwScF3LDL0QUNCufixGVk4M1fMX5wVTZx09ZlkgJKoNxoIFXEvWnfsPVUQ7zXDyK37dhqLSTzVBJEsXWUKhPhP8lZ9qZ1B1Q--po8aZgr_RCiUXVt9Ek46qAt3N6YAgM3hiXDOy4ruagKAa5GaL6onZhUGA1cs7qU5LUyNr4t9YK5fwnIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ee3caa25d.mp4?token=uf9dTfg1c0oen6LdMr6YGcje-e4hwRq6ykFbyN7hoQOZLWrWEQ4tRJIPMeRclmmBCCq2jYu-Eq7qHuef7AXLJSENP6h1yXLtJnJA6_9wEnFkKzn9Arbg114PhFfKtZbC3J_PfhvpYWg87Z6v1jD54HkJ6S5jdqmdm3aCwScF3LDL0QUNCufixGVk4M1fMX5wVTZx09ZlkgJKoNxoIFXEvWnfsPVUQ7zXDyK37dhqLSTzVBJEsXWUKhPhP8lZ9qZ1B1Q--po8aZgr_RCiUXVt9Ek46qAt3N6YAgM3hiXDOy4ruagKAa5GaL6onZhUGA1cs7qU5LUyNr4t9YK5fwnIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین اردوی دانش‌آموزان مدرسهٔ شجرهٔ طیبه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/451874" target="_blank">📅 14:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45b08c6ac.mp4?token=igNUBW3QRle_MkZNRg3lKxZxPw1SgJuaYMBMcanCx36wyowoBGi9Wg6ivlj3nLbHC_5hXOkf0csqN1bQqtPRvVV_Mp_w_synrIb6cYzjc-avq54Ok6L-EspLZ29lLRQxUCcmiTqqKbtW1-KgA3DC6lQBv6W14v8Ywi7S4TFAo_68TjBUTrP_oOipCG9EBCGRLvkc-UlbvUS2AJWUhnPPMJAfZsbCcr-Ub5jvErm11MMgYZ6TVN6YsaOxeQyiI3wYeal2egRrbIT7Gwm1nY2tjA5vowb4qdyVmgnLUqrfVH_pPE8C6_o6l3rlF_UNDw36rbzQgOc74MEXgoXsgJa8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45b08c6ac.mp4?token=igNUBW3QRle_MkZNRg3lKxZxPw1SgJuaYMBMcanCx36wyowoBGi9Wg6ivlj3nLbHC_5hXOkf0csqN1bQqtPRvVV_Mp_w_synrIb6cYzjc-avq54Ok6L-EspLZ29lLRQxUCcmiTqqKbtW1-KgA3DC6lQBv6W14v8Ywi7S4TFAo_68TjBUTrP_oOipCG9EBCGRLvkc-UlbvUS2AJWUhnPPMJAfZsbCcr-Ub5jvErm11MMgYZ6TVN6YsaOxeQyiI3wYeal2egRrbIT7Gwm1nY2tjA5vowb4qdyVmgnLUqrfVH_pPE8C6_o6l3rlF_UNDw36rbzQgOc74MEXgoXsgJa8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر شهدای مدرسۀ شجره طیبه میناب  @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/451873" target="_blank">📅 14:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451870">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_GL8uKGlEV8OFZBAEtv5xI04WxmbujGjEOzcKXJog4Zu5UvNQqAUrHUOnv31rJOkgq9AvLUf6YjwNuS7nU_mtDmYVtDmkwnTJUyUCF1N64azxYyvzt-BPD43LHIq0WdT1AKsJ6gGnavQI4YnRv1ldXfhI_9g6bpEkQKWP3WGEFq4G20tPBmh5gJEUWzfDMFgk4667jjr2vBGvsJwzd2aMwgmvE2bAufPPLlq4OjPnERdCPQ_Ra8Ndv-74Hm2NyzMnMibNI219a2DR_BJ1raEW7zdsPVDFgUidJLhKQClhw8JMDTJdFJYu1pqEPQMxL2UEqYwL_CCR7d-D30KnNh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ace_diABzCTZ9RqfDfIeTjXzwTCABJE4QopFFsHkWRBHC8PhrRQLP36OHdsIGGKufA_VShao_8HHwEh1d_UjW-mw7kXUAqt-KwYci-ddT8fFyvBBqkjEpVc4J63NKRd9W9-zUv4W57FYbix7527DBaX5BeAEip7YGc1eAbcmT9J8ctpnHxR55hbeM2BGO0_VQ95dV8KIdalWCumL_6FH-L_b7Rcj4bF686ZLsFfSIfi3RZ9RoC_Urj9WMQFK-boZeAUOJfyUFu0KvBMMAPPAFzcaljLs2BSeXCkV1lG5LXmDdmo3oMv1A2ZNK4yjNhtFnouq2wmsxycam3vtO2_aGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C58mZIr6TQ57Gpa4J8dOtTmFevmoSPf_tBfKF7PO7Wf6cZ-54KhSHuzYM7tWndAFm8xiyii5n6-h_BNjwdyeyq0eHXMPG_iShN2LOjnXDvJrPD07lC9PoVng3bFUG9z8fJ15X_ZxUfYtlUWxYDk7A0dUKqJ5oBerWadcIwO0eaduPb-qSEFw1F5-L5fyZpeNCHgxflyLb4RBx2NXq7PQna5dbMPsgp5Dqba_L17vGfDObwsW5qEwzppGB9PcTzWPOItxz8W2DfF4qNeVBkQ5lREOSi9fP7ozoPMVD7421CndjB3sFVVqsY2N19d5avn9L22ab4zcrGX4xmOUJt4EkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصویب
۷ تصمیم عملیاتی برای تأمین برق صنایع
🔹
در نشست فعالان اقتصادی و صنعتگران، ۷ تصمیم مهم با دستور رئیس‌جمهور و در راستای حمایت از تولید، صیانت از اشتغال و افزایش پایداری تأمین انرژی صنایع و اصناف به تصویب رسید.
🔹
برخورد قاطع، قانونی و بدون اغماض با واحدهای صنعتی متخلف در حوزه مصرف برق و ابطال پروانه فعالیت واحدهای متخلف از سوی وزارت صنعت، معدن و تجارت.
🔹
ایجاد سازوکارهای لازم برای فعالیت واحدهای صنعتی در روزهای جمعه با هماهنگی شورای‌عالی کار، به‌منظور جبران بخشی از محدودیت‌های تولید.
🔹
کاهش برنامه محدودیت تأمین برق شهرک‌های صنعتی از دو روز در هفته به یک روز.
🔹
الزام مجتمع‌های پتروشیمی به تأمین برق مورد نیاز خود از طریق خرید برق سبز از بورس انرژی، به‌منظور آزادسازی ظرفیت شبکه برای تأمین برق صنایع.
🔹
الزام مگامال‌ها و مراکز بزرگ تجاری به کاهش مصرف انرژی از طریق کاهش ساعات فعالیت، به‌ویژه در دو ماه پایانی فصل گرم سال.
🔹
اجرای برنامه فراگیر اطلاع‌رسانی و فرهنگ‌سازی از سوی دستگاه‌های مسئول و رسانه‌ها برای دعوت مردم به مدیریت مصرف انرژی با هدف حمایت از تولید، حفظ اشتغال و پایداری اقتصاد کشور.
🔹
اختصاص ظرفیت‌های جدید ایجادشده در شبکه برق کشور به طرح‌های توسعه‌ای و واحدهای صنعتی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/451870" target="_blank">📅 14:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451869">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSUG9zlE_ZNMnG0dO4rLZxxSz7YtHUHp4VYQBXgYAY929EhDtTIaG5HYFnKDzAbemhFCy8sJe8ShHC-x957WZ9n5n8DLH1JGcCqHwfTph7A51sSlnqvZ4v1vfWFXhHaQvmtBn4m7Vrb7UutgNm17Ftjl78dn1ezbpO6PEnwDCgSny_cXbxNCj-54kgQWzOqb1CO_s9AByhNxMNi-zrT7PFs0NtOgM3_x7S7Zq0JfbHdwCxLFSN9qO5i0RPXbhrSY_KToC5eDs-o-wDJ8IN3FvrRljfIooXbXSrA_brmeec2JtPvs-tvlUSKnAPPGpbPlFzTk4-MVMKYC_1W3gfi2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیفا آب پاکی را روی دست استقلال ریخت
🔹
‼️
فیفا در پاسخ به استعلام باشگاه استقلال اعلام کرده است که در صورت باز نشدن پنجره نقل‌وانتقالاتی، این تیم حتی اجازه ثبت و جذب سه بازیکن آزاد پس از پایان نقل‌وانتقالات تابستانی را هم نخواهد داشت.
🔵
این پاسخ در حالی ارائه شده که  تاجرنیا، پیش‌تر اعلام کرده بود آبی‌پوشان حتی در صورت تداوم محرومیت از نقل‌وانتقالات نیز می‌توانند پس از پایان پنجره تابستانی سه بازیکن آزاد به خدمت بگیرند.
🔵
طبق قوانین نقل‌وانتقالات فیفا (RSTP)، باشگاهی که با محرومیت از ثبت بازیکن مواجه است، تا زمان رفع این محدودیت امکان ثبت هیچ بازیکن جدیدی از جمله بازیکن آزاد، را ندارد.
🔵
بر همین اساس طبق پیگیری‌های فارس، مدیران استقلال درباره این موضوع از فیفا استعلام گرفته‌اند و این نهاد نیز در پاسخ اعلام کرده که تا زمان رفع محرومیت، امکان جذب و ثبت بازیکن جدید برای این باشگاه وجود نخواهد داشت.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/451869" target="_blank">📅 14:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IED01n8GAfZag9Q5Lx9KF8EsIBtFgiHWQSR_kdpc_vdPCscsIo0uJMNL3jrHaWty5Q8syHAJYuoV8Nx_hV5NTJas4JotV32zYvD5W4AoJHeqm2nhXNe-GP9CEdFme7iTksGgKJmdnm82aljOlkRdwfGnyizJx8_nLwZrlRKLK6JHQFET5FLSH4ezlNVBOKFo1la2VbAhDpBHVb-UyyUKyQG33jI1dmI3V_pcTcD2a7myTjsphVn1BCAiWFvTScAzod5fI1zEO_V19eBmRL08xYPBKg0CKo6xuOGzCsAFyVabsLOqKPoEGaOXdKU_SeRF9znYbAaUmyPHXYm01yXt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xx1e1rMFe08xfnYfvrwmoeq2ByvOGKcwYIviKvFojOiC7hSvorUEA43nWxjEOtt3Nk2_ffAX5Na-hupsOBzWImVncGBjFHRxQKU4lYjrpDWH19kamlhoGsdMZVzxICc19nksVM3MZvzEt8-9jw7I71L-MsI1JI4o7HqoYvNfeA_1r515cCx1VHJdgiMk5aGcJFH0BxvyzBNSjn_iHaqE15932aGNUrFe3uvv5q2fcL79fuIYeneRulKVfqKihilAx_M1wlCMRZETkjCrZdpqtwP1ZxcbU7mQBif9NKuHND3bqCH0MZBydxSEukmIiIC-BEeN_leBWYsejgG_57u16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUKCGSX-IxfrmBnXQDlxEgg9ZS9Rm6QxccG-5YiIYkBX6cKZGBJhHOXsCoWlu0Y9vZIYSSqR-UbUlobL5JCBBs6e978B7IigweGc1DLkbYILbcpdXnObpXkfSv6Jy2HEteCHAtDeGEQ-HMsDxB6bG1UlIRaAWraN6XKS8FHJMxw7PnyIbNxi2kAHFaZCupPm3CRgOadIhevn60ROeZgnRDg_6BmHlMVFhhlMwdain-lpfJoUlkGLjEUhCJlln5MjbDKEIMP8YZzR3VrJMEeHgSqKL49esVTRhKXVjbOywUNYdvzL-8-8Mwhbdc2PBMRQLg3SNXO1sElB67bIPUap_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLwIXa5EVBi9a3AJAtc4xrPvpoIRzsi_ZLMT-arPf4ZUtgBMA_wP1glutCRR7g5d3kjWr4YtZ-Jm1sMz_CPnaaL7dMGXasr4ffjHuFcmRrFc4EgrWQa62ZGVXhC1FasOeajTujBrPei7xNPmSzF2I1o6i6dTO2kvF1hbnixk6v-dumYjJiss3pSpyQD0NUe3vWGb0244Bc6kso2ybvF883KjeAvT7YNVP36iOWMD-UvG0DJaeKB7hWCxb1GEKcJVWjNmtgapu3H3CXS2mftdGnBOM7IsBjCLTC-qwXbUJ9BErDq3aS5yHxFfY2vHT4YSOryKaAz45vP7NjvHC-1UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J73-9VW714PNkEPXEjYpXqI7RTkb1_k-nbE66bYNRK2rWm3GWEYJ2OqSKppsNoO4y3kjOutIw6Wz078VlT7buDlrWVNMbOrnvShaET5aXhxKveuBplc3x9gniH7fJPK9vpPq03a3XuidPbk1MS85vadvsmlUrC24kX0OjzfAroepfp5_ZCcLS8xoCQF9mTWRlo2MEYrE0XZj1Qdn2kgSizgkUEUVLq5edT7xqwpE9qXNuTOCGdzMqTdDryb_nKEu7ZQbSXoSWkiFvLtDUSOfE9k5Aj48y-1LEAk8pkzqzBvAHrYUuLbKtUwiNRX1NGfw9qONj9_XHfcnhTbs4FGRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp_FJtVU3DnqyxITKNLhmcy2AKpjWmcn_OHVjrxySZIdulX9TCWNDI3x5SvvTBuj4cvAiTAiOYwp9BYmD8zYyFDm60oE5H4tx7oa0rqaC-BQzK-1vBFXgxF7IJDCUm46Ohu3dQXKoJ7cew3YK-jDbQkfWYPeVasGDCRnua-DbDGCOPvyHl_YYrkKe942tIi9lIEG8qn6uXAc1q_vuQLFUGZ1ebZUk06mQ2J8aa-ZVSj87CSGQzXA-MwL3QXSCgqYcuMJBl25YyHzWOnE6bQYWDKXTHfxS4elYwqAQRUYXNmfzE4C7rajOS9ZYl0u48Zrcy4yraEyVeU90eQ0Jxs8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7IyF2ctx2wZPpVKmnwzpfPvwP3QsdOPhhoxEpq7pvRgQphX-LJf2l_6Ospi5uQGQn4gMPP_pL0JBptNaDX8g6MbW0LXgKiQ1zzC5komBAAmbzA7tHPdGCMfOfpu_6ncE3EJgmqMUccHvIgIsOIQCqCNUkqf-TtrCIr6z5IWiSKXWCEZH8nBqh4vx9aEaab21CWPj91hqe451evGqYly6-QTPADGPkHWDwmrbAvYhwpok86ayxzwt3e0fSEJE1sdHdsKU5HhKxtst_66_tANpE0fIDl2QkbOhUcOl8N5JTvB2WzSTAzWguyjM0HOGVgph_mrCQie6T0RASZI1mXpig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایش از خیمه‌گاه کربلا تا آسمان میناب در قزوین
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/451862" target="_blank">📅 14:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451860">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6918e70.mp4?token=fyxddGVSyeISu4i8VIgACbXljLl3wR3a6F6_eT7lwCfu7oHzvUNDLEQh38W9itZbmiPH0bSrEvUBaq2l0LAMFO22sLOYnZhufUORBZn3KVdUskZKyFyfgKpeN5Z43hw0d_pjqaVDBroETffOfRSKI16RlucNG-dRRBiWBoKPsVc0rvSXKZJ4pjtbmIYi2rsnnPPO8_G7kLoW9QUwLgLee2LxfQ2-ioBN6lRvdOj-UmLoojEwoyhfTqMacX31XjU2FHMp4e783gRxG5Hbt6PDqgy4-gr_HYiH5EkWvmOaLrFO7itZMeYkEN6vOeZqMiUBWoQuCzNdrZzkkDY6MkStuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6918e70.mp4?token=fyxddGVSyeISu4i8VIgACbXljLl3wR3a6F6_eT7lwCfu7oHzvUNDLEQh38W9itZbmiPH0bSrEvUBaq2l0LAMFO22sLOYnZhufUORBZn3KVdUskZKyFyfgKpeN5Z43hw0d_pjqaVDBroETffOfRSKI16RlucNG-dRRBiWBoKPsVc0rvSXKZJ4pjtbmIYi2rsnnPPO8_G7kLoW9QUwLgLee2LxfQ2-ioBN6lRvdOj-UmLoojEwoyhfTqMacX31XjU2FHMp4e783gRxG5Hbt6PDqgy4-gr_HYiH5EkWvmOaLrFO7itZMeYkEN6vOeZqMiUBWoQuCzNdrZzkkDY6MkStuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دسته‌های عزاداری امام حسن مجتبی(ع) در حرم حضرت معصومه(س) به‌راه افتاد
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/451860" target="_blank">📅 13:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451859">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OPL1BfA4ba0qz8fUB_APe21rtdO4-af4zmRzAwHHop2-ahFjP0ldkafalKIf76Ei96uSxUhzQNhsd2zrhBZBjzDy5SU1_xV0m3OfCo6R-VriBenmPMcM6FBXEHSyEnFrmV8qTH9kdThrwxZUq2nmpR5POkILGPMHjWajizVNKfMzNnP77ptQ9KAM9c0tAxhmLvOYHw2G8lXR-4MXImW2MPdKO9QQWJ1Vx4THDeTjwFHDkqSqdLPrQpGLuM963P-RSPLbOepqGbYR0NMvnMQ5LhgXfpREEYt4v2K9DrGVbvVbM53ADnT9GoOGdiV8se-dzMG7RpwJ3ttgrXb6JL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار ابن‌الرضا: نبرد اخیر به سکوی جهش فناوری‌‌های دفاعی تبدیل شد
🔹
سرپرست وزارت دفاع: در جنگ اخیر دشمن با برترین فناوری‌های جهان آمد؛ نوآوری ایرانی معادلات صحنهٔ نبرد را تغییر داد.
🔹
هرچه دشمن بر پیچیدگی فناوری‌های خود افزود، توان بومی ایران نیز متناسب با آن ارتقا یافت و میدان نبرد به سکوی جهش فناوری‌های دفاعی کشور تبدیل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451859" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تکذیب فعالیت پدافند و انفجار بامداد امروز در پاکدشت
🔹
سپاه استان تهران: گزارش‌های منتشرشده در فضای مجازی دربارهٔ فعالیت سامانه‌های پدافندی و وقوع اصابت در پاکدشت، در بامداد امروز صحت ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451858" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دقایقی پیش صدای ۳ انفجار از حوالی سیریک شنیده شد
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451857" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP0AZoMp9FAiKtqnlVp98xQaD72_xjD0TiJFOxCQqmROC4TG9E5SSgC4d2_YOv_2mvcjaPzIm4EFkC3zsFHNiLmlHL1rTPHyo5hThHXbMKdwku-BefPvGxoAVbdF1ZoqfXLusDEb-gMXJA_e5mT9ugvZitPxWrI1J59qxpFycH8JoYZsrZcv2T7g_iovHjs5N0ZZgl6LSM-hcTuNh52tveFCpKfEGbyA3y8RmoFNHPusr0vgsUEVaf9csBxubJHasffDxfKmUOFnDwhgkh08xLYG1jv8wVKcNin7iBMNR7_1S815684Ubp6lOZcihJYkue99ZuAqW41H_5BkpeA7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ کشتی سعودی مجبور به بازگشت از باب‌المندب شدند
🔹
خبرگزاری سبأ یمن به‌نقل از منبعی مسئول در وزارت دفاع این کشور نوشت: در ۲۴ ساعت گذشته، ۶ کشتی پس از هشدار نیروهای مسلح یمن و اعمال ممنوعیت کشتیرانی علیه «دشمن سعودی» از مسیر خود بازگشتند. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451856" target="_blank">📅 12:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451849">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohw1i6lSiHWhFiI-SoBmkIG6A1jrtblBip5MGwdV8eMRiMVrUedZ6gkUpAbk16tnHok2y637FvhKcZX-gCzcHrOWz7F4wVPGyy3WH9rlyTTWu84UnM6aDkf9KChrB6t4jtl0lwa_ZP087CpUR6N7CABk9Hm6PB_OB6xBdXBv9HqjSX5YiFe9WSYGhOjIKZNakv-ym55fm1HCr9IQIIW77e-ngx_VM41IV0DiRjjnfLtzw66RlqRVUv_8QgHAvY8KhG0aK-jvQI9bgW76EYaWPBFyPX91ohwsEZ8p1k8Ce5ooFYLJGRrgfwHV3HMmdNDrzeomi-TiCXRDW1gqR-WjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW-kFAVJR_HbJBwbNGF8ZMnqVWtMizl9ckvTzWF1SdrLai1ff4issHpPZjE1OIvLI4j49sB-3hl1YGkdtWYPEI-iXBdMdk68LhvcTzKEUKyLtOhoRA0qynA0c47hCUHFoj5YPixAzgdbIMgd76l71m7X0gFlqRqk25T-sv2NXxoHRpKMroL8eY-HhjHiyzDTsMbntmHhi4IcmtKPykMj1s8UTIYjfU5gFInPXZUfbu_BHn6zbiQlX8TUoYkmqVJoW40Ft6HiTjFBiMjhb9KtdoTPmBihdyAF9TBWEPFiena5d2v5CT3YUCDiBkgzxGT1bhMe6ZeN4VfXath4N7-6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN2ZUiEJT3-VxKN5ekGZgOGV3JrixSE7eQjYMSns09y9we0TprRjyWyWBnPpEZ2MdRDlgac2ryAdFjbndbvpsl5YmxtuuP_VVgjPk5vC3mcFmU78rrFpNVeCMeTIB1aq3LMz5MtzZgDSWy_s9R2iviW_LSrMJdxq73EEmsNW1ZhmIoYLSuqa2yLueIhlg_6g91bgOmW8rpEbWfo6GMjv6pDmS3ISDHOp3qmLf4T6ljwArm6BkBppLjC8O-j3ntLWPAAOzVx4AjaPtOOaLp8HzGcQlyH1e9qcF0Fe263wm4rvoF5c0QUOh3OimtA_gZqTFw7RW5H5zR2jsGKWrm9g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZZiqkWnPnAyPubY53Z1QLyIT6KNs1HYgM5gCJHiKFuEXHIvyaB32DC7DeJm0Y6cJ-b9bqOPLAj0RMc4_OfmNwxMcJtHujISnj97jAL3EZF6Nh83hWQeAajtdASpvIZzps8SPMeE8yYGzBgTHk6vQXYXOaF9HpksA9kmGJP__ALWvX9vCgPiz-d3ilYeJB-aznMYteWA_T6v46T297tlclmJn7SRySpaKkp7upeA9r2WLhok-eJA6gXblPUeFuJBiFojujLuRL-eMwAUIeARYzFiD-NmArzLoFtXd266z4eMYNZoPhplIgyKKbso1re4b57ekVjw-ladzOgLaf5pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrjdgmL2VCVrAPkY7v6GjzY1Ls0Ia_s11nxg6ZB7DhgIL3_6-YjeflKTr_Anst1APEVb3o9NayVPbfkN_pACkrKu8dHjY8Zmbew5kXKJh4L_n--AXx0GCAvx_RZvSXguPMKoDnrMo8m7xpLjJf2jJSqIlxVweC6Zwxt_Ml9A10czCEzCHOXUGyGPpuECiMM73TJR-18lEppz4lVL2-55OXtSKOwRkLEA9fswFnbaLYA9YTH-Peh90KWO2CO7Gb3diIwHnINB_0jVzcLpTi9otUEuOwgAWqWZkRbKpjDHjVJwXpq1nTNVRaLxC_5MXQGd0-wzRoFERvbdKOKn6t-Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnlO7180ZFwWIDvelJhl8wKkXv15XFTf6nIwvaR7ngBWd78z84LTiJ6XcGBp-a4FnNDvUdWXYJ0GbTImCDizmyc7J-ZbcD1t3zdC5gUFtBsCogIukvQgOs77XLkOFMA8DrfLsbG4WAfo12lV1n5KJG2raXSKglfQXQ_6sMl1wh2IjUc3-P73gBcByVqxYP_x13mWXxzDwJ70S4pL5BYpR4cbEFWkaDeResKomueUvt_TlR8vczdsT8LZICwv8B0p42JhicTxkFa_2LmHkPO2E3s7iSJI1eH0VM36gqfHClOaDkhkUAnIc8XCBOvF2Ep3mNoKKhXIK2fuMsqUiCjWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_icb74_GsiLmaWQ3_m7YgbkzksND6yrX0hxb_5QkxF8So-EyoGclJ3HYYI_JiB7i38lNhrRaN2Tk4H6NbPTnHP1sVH_NDRT4UkPGlr9nDK38-4kd39EqQj9Z3qQg3ColL7ouL3Msdg4SwdS7xACF365lqQ38xA2hQkElPV7VuijjG8W3bkMx-YTXuFq47T1Ib7olA_J8uCc5ZHbc_babjmcv_ZeHEPNbvROZWUstqv7nhLoy0cBFeJv2kQEFlIjXPHwUHvYjREH_CtSlEpyNG8oh0c6kN68wgt_PpqF8bbgcnDgE6BR8lkdQvjwwBz_7FunjNW1z3wtfsJdOOO_TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده کل ارتش: به اندازۀ سر سوزن به دشمن اعتماد نداریم
🔹
ما می‌دانستیم دشمن به تفاهم‌نامه پای‌بند نخواهد بود و مرتکب حماقت خواهد شد؛ بنابراین لحظه‌ای را از دست ندادیم و در جهت ارتقای توان رزم خود گام برداشتیم.
🔹
اگر دشمن پای کثیفش را به خاک ایران بگذارد،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451849" target="_blank">📅 12:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451848">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYDQun4j8_FQA7S12GBEzY1QqghE1JZyW2_lOunyz5OQLqkgt2tyT2vg70SM1Tudbm0yC2OAmci8fDisI8nQSUH-cb3yUQ_KY8pbfQ6qTJ1xR00gHsr6R0knT89ffuB8yfyPKRlJfQPfIoMsRNhH0Mgb6mh-hZ8j5BeeXZOVZcerhhErGkU-wwTQVOx9vvxXXw9SDn58SZlcC4NTlJnLhlpx5sWhxZ_wSdG4N56pVhWYWC_4oh1N_l1nYKAYymrk8rijApZZuJZdnupJw9eB66agTjmKfysCSaoyZUpS1bMzDPUaBPSTwxrBlnHXzYmW9dgTrSZATI3DzXldBsvy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۴ هزار واحدی به ۴ میلیون و ۸۸۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451848" target="_blank">📅 12:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451846">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXLut2YCVS1x3Fb3SQ7j1uKusD-lre9Xv9F9UGUhCnh44UmpNtF7P8RvprwW-SwRE9_jAIpMVA8oHgFtru0nBbkpYyA9_wRrPiKyL-MvlPRj0lxd_tQRt1mkvnYXnATSSmH_aWF_t9_AbvPYfYYb5TYnv_jK-wJjnojT8-9I6_b6-6oou7qomI6MO9_2ymuJsSrmj75AcSGIJIHFrGAw2m3ZPcWy3NFg1MHTl6xIO_EakGdIMNFOdt02x0geJwz5PSQMwfEM6cAe-8PrkZgg1_5HwUh2oW_C9EjYA7xMkm9A9BcrLJLs-x1Glbonw26SaztdrCFev9UgcuoHfabOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
فرمانده کل ارتش: ارادۀ خدا پیروزی مردم ایران است
🔹
ما با ارتش‌های سران کفر جنگیدیم، آمریکا جای فرعون نشسته و تصور می‌کرد که هیچ ارتشی در جهان، حریفش نیست ولی ما ایستاده‌ایم، تنگه هرمز را کنترل می‌کنیم.
🔹
ما به آمریکایی‌ها شلیک می‌کنیم، آن‌ها باید بدانند…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451846" target="_blank">📅 12:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">سرنگونی یک فروند پهپاد متخاصم در آسمان تهران
🔹
پیگیری‌های خبرنگار دفاعی خبرگزاری فارس حاکی از این است که شب گذشته یک فروند پهپاد متخاصم توسط شبکه یکپارچه پدافند هوایی خاتم‌الانبیا در آسمان تهران رهگیری و سرنگون شده است.
🔹
این اقدام در شرایطی صورت گرفت که بامداد امروز، مردم تهران از شنیده‌شدن صدای فعالیت پدافند هوایی در برخی نقاط پایتخت خبر داده بودند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451837" target="_blank">📅 12:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1fa10be9.mp4?token=BvLE_WpjtJW030wMxUMTwHSUoHJmBYrashif736YHGInQDHbQ308S1bRff8sW62WLmDzJn8KW8Igdnswjt1NYvxeug12okZDxLFDs9c8ou8WTA8qzq1CLYtw3tyAPaGmCsKzjq5MFWHhGT2_5nD0Ixpk48BplIDkXKMnNbLhnR4E5a4upbxVjJCsoq1wlEinqz2mtoW4njNvGWqPIsImJP4aCDvMglseUmSWVqnVmNko9Na3NJTqClJczHHAA8xHfBAbBLUPASDD6g8VfgakVc05A6jvY-ZRoWYe_3-IV7uKm2vP8gw16wmU3F2kYFWHhuLm0gwp-IkYDVuCSzWdzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1fa10be9.mp4?token=BvLE_WpjtJW030wMxUMTwHSUoHJmBYrashif736YHGInQDHbQ308S1bRff8sW62WLmDzJn8KW8Igdnswjt1NYvxeug12okZDxLFDs9c8ou8WTA8qzq1CLYtw3tyAPaGmCsKzjq5MFWHhGT2_5nD0Ixpk48BplIDkXKMnNbLhnR4E5a4upbxVjJCsoq1wlEinqz2mtoW4njNvGWqPIsImJP4aCDvMglseUmSWVqnVmNko9Na3NJTqClJczHHAA8xHfBAbBLUPASDD6g8VfgakVc05A6jvY-ZRoWYe_3-IV7uKm2vP8gw16wmU3F2kYFWHhuLm0gwp-IkYDVuCSzWdzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451836" target="_blank">📅 12:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/505093e0ab.mp4?token=hPWQIKWkcrHy4kE_dDWhceTqucl4oyqWENYMaFy9gT11_DI0T_7rjT9wv0YZMRmLnNh4n1B9rG8oQ9NB29EWfWO4L7AHQODhfpvn3ijRVEeFYzJuP-QX5MGT42qi3OkdppeO-H2V8jV02kzrN71UUYITJqavy7se4JzHFwCNUkodqg7PO-mryx2ui3ut6cEZK0QnD_ku7W-jcwSS_HzrMLiMuN9nh0f6MrXzqPsQPsG1QTxlqcfuSgAZkIUm5IvIzOak7x7gKzPHjphXjeOneT1XGRBAgCOJjvbY7Ad-jJp3DpAgX21_AptiE0EliHBPLiOjHB-pWArirlvx7JBF3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/505093e0ab.mp4?token=hPWQIKWkcrHy4kE_dDWhceTqucl4oyqWENYMaFy9gT11_DI0T_7rjT9wv0YZMRmLnNh4n1B9rG8oQ9NB29EWfWO4L7AHQODhfpvn3ijRVEeFYzJuP-QX5MGT42qi3OkdppeO-H2V8jV02kzrN71UUYITJqavy7se4JzHFwCNUkodqg7PO-mryx2ui3ut6cEZK0QnD_ku7W-jcwSS_HzrMLiMuN9nh0f6MrXzqPsQPsG1QTxlqcfuSgAZkIUm5IvIzOak7x7gKzPHjphXjeOneT1XGRBAgCOJjvbY7Ad-jJp3DpAgX21_AptiE0EliHBPLiOjHB-pWArirlvx7JBF3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکم اعدام عنصر فعال یک گروهک تروریستی در کودتای دی‌ ۱۴۰۴ اجرا شد
🔹
با گزارش مأموران سازمان اطلاعات فراجای البرز مبنی‌بر اینکه شخصی به‌نام «مهدی خانکی» ضمن عضویت در یکی از گروهک‌های تروریستی ضد انقلاب، اقدام به نگهداری اسلحه و مهمات جنگی کرده است با صدور دستور…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451835" target="_blank">📅 12:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=rGXC9hB972cxs_xrptbRoAqgoqC5N77q1YZmFspZtiBI2PtoMH8EY4lfWwJtYo-_4RculoZdXIDwbTKphfdOvc3VHQqmiPuvkycS7J86Dbgn-CYZGmA8_sor-043otdDHKdSdAObro8L5xBjaVwgXZmxpwj7H8lgmSHh_VlVlGMLfPw_z_57wzomBRIWUQ0lbScqkR-kSn5k5DgEglvf-QCGaEBxpDM4wMvO5IOZr3CHNiQTDx47iSAMq1QCg7hPAscsfNizfxVS2G4lFbqicKrI1CDvJWvC3wzul6Pi_WNSJvoPk6_4Ccjw486X7m1S7QpCbh2HzwXGnvGwk6y4Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=rGXC9hB972cxs_xrptbRoAqgoqC5N77q1YZmFspZtiBI2PtoMH8EY4lfWwJtYo-_4RculoZdXIDwbTKphfdOvc3VHQqmiPuvkycS7J86Dbgn-CYZGmA8_sor-043otdDHKdSdAObro8L5xBjaVwgXZmxpwj7H8lgmSHh_VlVlGMLfPw_z_57wzomBRIWUQ0lbScqkR-kSn5k5DgEglvf-QCGaEBxpDM4wMvO5IOZr3CHNiQTDx47iSAMq1QCg7hPAscsfNizfxVS2G4lFbqicKrI1CDvJWvC3wzul6Pi_WNSJvoPk6_4Ccjw486X7m1S7QpCbh2HzwXGnvGwk6y4Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451834" target="_blank">📅 12:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451832">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvpy1nNn0gsUVNKjiJnr6QCefVN0ZPR0mQmHDmzAAnfPjyE6dzTw9NKVKXkVcwC49Mtc9hnEzXfY7eeXY-FTjH_LHzJppnxqrLboLtbioWqfbQxgs1uBrIiBUY1p7wFDcfIqovjcmEbnVUMMXKaxoh4oLWToBvJJ7vONJSnBX2VQCoCc0Tc7vbzLGemylH_ySSJio4EDdeX3Qsm_YN5bk5xVTIPZhQ6tGC0ibTIcYFB8vpeY36CVq9RO6fmmYavaK-oEcS-D0o4A6mfzZW9KZEKe2lsLdl1g-uWWfm44H07zfOibefphLcHay-N3xp76G_jDgAHnVcyMZ41dBCAsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/getwCgfLX3BheQLksCfP6aJTr85AOjfBZvFLDGD_zZEsqc8y7iKEjVCUHUkf9l56u5kUaKNNNcXC17FXUf61plRnGQAdVplrHYp9CGN07DswLnGB42VIkSdY1UARMHwdq5HoJUp3JchzvDMZrgmR4Zqkz6ByFx34eGm9UeQ8FFjxyB2FajyRjMXf3_P-Ne62U-0gzLAicYONjsoSQ5Gr1mSP8i_3eyLUbu3-CQ8wTvfUqGZ4pKsNSF5xfsnK6IaYHnE-6GHjeXwGVIyoj5Fsa9eCEuQlGwhbmMWT6wNLDuJR_R5VVFBRqBBqLEmAKhJuz2gzLKMokKuTw8nSkTpwJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ پاکسازی راداری منطقه در ادامۀ شب سیاه سامانه‌ها و رادارهای آمریکایی
🔹
سپاه: فرزندان غیور ایران مقتدر ضربات کوبنده‌ای را به دشمن مستاصل وارد ساختند و با ادامۀ شب سیاه برای رادارها و سامانه‌های پدافندی آمریکا در منطقه، یک رادار هشدار اولیه، یک سامانۀ رادار…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451832" target="_blank">📅 12:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv3PLTtc_c4LMghQ2-h7_2hPoZh-bhVAR8t8jeIhIO00lwVtAQdQ_GehpX9eF4a8Q9Y8uCfPLdJNzdvvSIl4Ru1EH7O5miABnlQzddnJp61J7PHIuKN1QwVjWXf6gXoGw7Xplsw9Isyov3uyAqJvAzZV_meULPgCBYkyXhQzt3lEgyfdEBjkMmvoksy6Y1255-_tH-hJNXP2QcoRaoUgIPmS-4gSX4Y4BOS3UFIDSki-J9nuugT4bEyAyFYwH_U_pQRJFZFdcfOS5OnxJz75ETdOBf8l8RW8sl1_6yQjEkuPmZFxfRhH7lTvt681zLuvOUBjTJUXU6YyMtoghHHtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر دیگری از بلندشدن ستون‌های دود در منطقۀ مرزی بین اردن و فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451831" target="_blank">📅 11:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451829">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQO9n3Tfg_Rj-HsS7Vkq5gBeSq834q8RlgLdINsrozUy1Q5XrzHgCiIMDj-GUIcetaDL5_-mGh898x56VdLe_-uTgNN6CK7mcqLGfD4BkwdJiqxBAufwtqHJJjFEQIi6k6FVTHFCKzogJuhZcIRH0R9jQtLMdPNFf5BIxtGBUgJbkEG1zhxh9xhxht_Y1nYD5MiA6M3ihtIoFthW7EyIoMCqFsUd7PJKlsCa-8eLjp4L8LWQzW0H-StkbieUuFNknVreX0ZrXUp8PK8NMXp7o_7mqwCMPRBGaWDNnGqKFeE40eVbag8NnIOyciWf9eCV-8ZTKoOjtJB7pXYgU8dyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h11S-fZO6KLdcjBRyCc6saDPlXdVbfQqG-gpQ7PtgCqhzZn9GAgXCW6BIo0FYyGEyYyydSY6xhPmq3lKbvoMj3dlODLicMke3mhtUouJE-cSoi0SU7qkrFbnnKKx0wGq0X5iXsJet7LV64YNDfUkkrSc1K99tiYJTplk6Bu8c0FAaIu20bU9tty-H-V47TtLgj2oF9KVHtyutnFkJmOuRFm_me-lW4_Sy6Scj5QgQwbtalQ9nANT3YKFDyByFZnKI0WDTvQV98g_5XI87pytMyHq9Gn9xznhSP0n8dkyxEd6OblqOxQI8bOFHrH4v_F5BTJ9Xwj16HlS78lWkjaVGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شبکۀ ۱۲ رژیم صهیونیستی: در پی شلیک موشک از ایران به‌سمت اردن، صدای چند انفجار در ایلات شنیده شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451829" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451828">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ac646b74.mp4?token=i1Z2HzXg5T-Y9BXpIWcEPPBsBoYeQyuOEzCM_MMdCefiGBCgq2YQgWEvdglcR_f9guLkP0BJTKSB8_4P6L-8l7YpBzjwNPHxy3zWJX04XsdfBNVg18fE9TJYccITvNfYnYqBiWonMYLE1qZHKbysHAa9dttp-xXGgUaqA_CTcOIKJr0glE-nWFviNmIJTf0W3wwgIsrQimQ11DLjpAOKG2d9CWAn8vaBcanWGsJsRrK_aJSFjBMYStodlPI-rnDC5xhxPGm4-kK65ICPTNzmry4KlDerDz74FI2lBBr0_Vmdr5_xyVtHcJ3ktOFvxookEQBbbpmCxRPmf0MsUAf8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ac646b74.mp4?token=i1Z2HzXg5T-Y9BXpIWcEPPBsBoYeQyuOEzCM_MMdCefiGBCgq2YQgWEvdglcR_f9guLkP0BJTKSB8_4P6L-8l7YpBzjwNPHxy3zWJX04XsdfBNVg18fE9TJYccITvNfYnYqBiWonMYLE1qZHKbysHAa9dttp-xXGgUaqA_CTcOIKJr0glE-nWFviNmIJTf0W3wwgIsrQimQ11DLjpAOKG2d9CWAn8vaBcanWGsJsRrK_aJSFjBMYStodlPI-rnDC5xhxPGm4-kK65ICPTNzmry4KlDerDz74FI2lBBr0_Vmdr5_xyVtHcJ3ktOFvxookEQBbbpmCxRPmf0MsUAf8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: دستورالعمل ما برای تجمعات همان فرمان رهبری است
🔹
فرمان و رهنمودهای رهبر انقلاب، دقیق‌ترین و منسجم‌ترین دستورالعمل برای مدیریت شرایط کشور است.
🔹
هیچ دستورالعملی برای پایان یافتن تجمعات شبانه مردم صادر نشده و این برنامه‌ها در چارچوب شرایط کشور ادامه دارد.
🔹
حالا اگر کسی پنبه در گوشش می‌گذارد که نشنود و بگوید منظور رهبری این بود و آن بود، کاری نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451828" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451827">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6e664d9d.mp4?token=phG0FvP955eHT0Yq2qhCPkfg59isoHmh2GdahMbSTHh1lzbTII2Zqyxf64fOgf4XSTp_uizhBT9P6eE__kO8Cwdx-ShuVINVZuuk89RyxMI4OtADg5vJ_TcX3QsVbvwXBaFbQtqXBT4036FxcJGWqJd45HTxCkvBbrKpYPA3Fnt8sKpND7hQJ9eC4SYh9a5qpYznbbtCA60xlwsLeTqLGUsus3tAUZ44Tz2Fuf8r0S5k-aakuAijJaO3i_6_uHMilhz88dgTqSP9EGppU3DBHP5j6Tg18Vu33gzfbJNAXRmOj_OrjvOZ_pciKgcLQ1kkgrT-tpLDKeDKtGpj0EoTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6e664d9d.mp4?token=phG0FvP955eHT0Yq2qhCPkfg59isoHmh2GdahMbSTHh1lzbTII2Zqyxf64fOgf4XSTp_uizhBT9P6eE__kO8Cwdx-ShuVINVZuuk89RyxMI4OtADg5vJ_TcX3QsVbvwXBaFbQtqXBT4036FxcJGWqJd45HTxCkvBbrKpYPA3Fnt8sKpND7hQJ9eC4SYh9a5qpYznbbtCA60xlwsLeTqLGUsus3tAUZ44Tz2Fuf8r0S5k-aakuAijJaO3i_6_uHMilhz88dgTqSP9EGppU3DBHP5j6Tg18Vu33gzfbJNAXRmOj_OrjvOZ_pciKgcLQ1kkgrT-tpLDKeDKtGpj0EoTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: دستمان آن‌قدر پر است که دشمن را سرجایش خواهیم نشاند
🔹
ما برای بدترین سناریوها خودمان را آماده کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451827" target="_blank">📅 11:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451826">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24826791a5.mp4?token=mjQZV5e__Akus2KoA04_C82wXYR_k8P0BgazlGvLfgEuiViYGipmRElItf8QsKS9VDuUBUw6-3fPvqA8t_OhoSvkifzOVA3fIs3urGGkjIHWUnzhVVgIUwaI7oq0449SRMiNI9xcL99mVMBYYxqe1qssfRfTPDRni7MhcZPigzO2NId51_E6ZfSLtxCGoiVgxc_pbv7dka-6HAf_H5G5XcR5ee4pHG3vzqq_QHu-g54CoguY_KmsOrgwKS3RHZJfsqxx29majP6HDzUmiLK2lJwcisy-U-QWwOQa6XMUMKd1HrCspQPrCXrysRVDjEkk6wHpr5jCIaMqC7OJcr0rDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24826791a5.mp4?token=mjQZV5e__Akus2KoA04_C82wXYR_k8P0BgazlGvLfgEuiViYGipmRElItf8QsKS9VDuUBUw6-3fPvqA8t_OhoSvkifzOVA3fIs3urGGkjIHWUnzhVVgIUwaI7oq0449SRMiNI9xcL99mVMBYYxqe1qssfRfTPDRni7MhcZPigzO2NId51_E6ZfSLtxCGoiVgxc_pbv7dka-6HAf_H5G5XcR5ee4pHG3vzqq_QHu-g54CoguY_KmsOrgwKS3RHZJfsqxx29majP6HDzUmiLK2lJwcisy-U-QWwOQa6XMUMKd1HrCspQPrCXrysRVDjEkk6wHpr5jCIaMqC7OJcr0rDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر شهدای مدرسۀ شجره طیبه میناب  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451826" target="_blank">📅 11:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451825">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
شبکۀ ۱۲ رژیم صهیونیستی: در پی شلیک موشک از ایران به‌سمت اردن، صدای چند انفجار در ایلات شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451825" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce52e2213.mp4?token=WiCEle5X80Qob-bi5ZjqRdDegpjTQAPiIFutex3iD533H9-aLD7J2Xqe9t6TgO6LxIL0xLAcQmJDCGmLJw3n5nQfRu3ghOSXKoGjB7iKyPuAOEndazZR8bcfmV96qyNeL3HTAe-Ub7R7P_3Oex_cOlz16rF-lL1Rim06W2ZdC5U1lAYArIRa1y4alneotzVMpzwTHhtfhqTvuM1MnuSaG6VFZR-2D5RcgZDVLXvQg1nkvR1Kg11Kbn57V_-yhgL2m6PRz7KRDsWgjPSLeJ2d_JykTgd3gBEWkbdYjLUZ9rtxA20NT77690vE2Jq3bLHHQRG1eof-hS-_xCj3Y7b9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce52e2213.mp4?token=WiCEle5X80Qob-bi5ZjqRdDegpjTQAPiIFutex3iD533H9-aLD7J2Xqe9t6TgO6LxIL0xLAcQmJDCGmLJw3n5nQfRu3ghOSXKoGjB7iKyPuAOEndazZR8bcfmV96qyNeL3HTAe-Ub7R7P_3Oex_cOlz16rF-lL1Rim06W2ZdC5U1lAYArIRa1y4alneotzVMpzwTHhtfhqTvuM1MnuSaG6VFZR-2D5RcgZDVLXvQg1nkvR1Kg11Kbn57V_-yhgL2m6PRz7KRDsWgjPSLeJ2d_JykTgd3gBEWkbdYjLUZ9rtxA20NT77690vE2Jq3bLHHQRG1eof-hS-_xCj3Y7b9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده کل ارتش: ارادۀ خدا پیروزی مردم ایران است
🔹
ما با ارتش‌های سران کفر جنگیدیم، آمریکا جای فرعون نشسته و تصور می‌کرد که هیچ ارتشی در جهان، حریفش نیست ولی ما ایستاده‌ایم، تنگه هرمز را کنترل می‌کنیم.
🔹
ما به آمریکایی‌ها شلیک می‌کنیم، آن‌ها باید بدانند که جمهوری اسلامی ایران یک قدرت معتبر است و به عزت ملت ایران اذعان کنند.
🔹
خیلی‌ها منتظر به ذلت کشیده شدن ملت ایران بودند اما به برکت خون امام شهید و همه شهدا،  اراده خداوند متعال، عزت و پیروزی مردم ایران بوده و هست.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451824" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e40b4184.mp4?token=M-LluhqRUtperX5o_nOn-ciZELaqLnr6E11VaO8FsaajcvBdm2Uia2ux3-BnylbkAUK-3weDexffQ51ND8MOub2ghl1f5lSjLdP_Q996gogpzJgrqSgBjAL1WFBsb4oZZ-h_5k8kUFKRK4SK7efftG2uh9DVMm-aCme0C1hcdyG5tjqe5rQib4oroNq4vD_wpjdW0Dx5UoRwfrfthIjtRgFpMQbMfkvHNHTV15C4RIYAdIVlb7sdIwtuJ6VFOiLM6u0KRg-UBvnAX5j6l6aeB18EPPfchUiRRp75PAm0gXExLWr-uB_MWJmWiaeU7kL0VMI0hV1retZbcuEXrlS1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e40b4184.mp4?token=M-LluhqRUtperX5o_nOn-ciZELaqLnr6E11VaO8FsaajcvBdm2Uia2ux3-BnylbkAUK-3weDexffQ51ND8MOub2ghl1f5lSjLdP_Q996gogpzJgrqSgBjAL1WFBsb4oZZ-h_5k8kUFKRK4SK7efftG2uh9DVMm-aCme0C1hcdyG5tjqe5rQib4oroNq4vD_wpjdW0Dx5UoRwfrfthIjtRgFpMQbMfkvHNHTV15C4RIYAdIVlb7sdIwtuJ6VFOiLM6u0KRg-UBvnAX5j6l6aeB18EPPfchUiRRp75PAm0gXExLWr-uB_MWJmWiaeU7kL0VMI0hV1retZbcuEXrlS1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض به جنگ با ایران در قلب سنای آمریکا
🔹
معترضان آمریکایی در جلسۀ استماع کمیته تخصیص بودجۀ سنای آمریکا با پلاکارد «نه به جنگ با ایران» و سردادن شعارهایی علیه حملات آمریکا، خواستار پایان فوری جنگ شدند و آن را «غیرقانونی» و «منفورترین جنگ تاریخ آمریکا» توصیف کردند.
🔹
یکی از معترضان با اشاره به مشکلات اقتصادی و معیشتی در آمریکا گفت: «مردم اینجا خانه ندارند، انسولین را به‌صورت سهمیه‌بندی دریافت می‌کنند. ما مخالف این جنگ غیرقانونی هستیم. ما به مراقبت‌های بهداشتی نیاز داریم، نه جنگ. من شاهد هستم که مردم آمریکا دارند می‌میرند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451823" target="_blank">📅 11:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZJkfy_wDTc9P9Uj1ARDwD7mITi1KIWABDUasQMIRR2VU4iRcqk4H4OgdMY_VlpbH8s8PVzXUiOAzIH1EoixMHpy2bhk4AoX-Uos9uZauQF7g6zvjNsZ7QHqAQ_tQOH-sJ8daZMDST2jvqWA5wLwQrv-lb_uln4vDleKP6nOdFTXBiPUpZkXyl4nzKMsDnnOg4mLHubU6f1TNHyQgehPEX773jyv04CzjaBZJNO4pimdW7fgsPJC_9iUMWvOiDfD6-tXScEgr7YIS--yWk5Qcq0zdvdN5OYEzkKqBtnNNJaL8MVTbDqYog5x0_fWF1Kn9-U-TTEb4vsuy15QRTCABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفهٔ ۲۵ درصدی آمریکا علیه کالاهای وارداتی برزیل
🔹
وزیر خارجهٔ آمریکا اعلام کرد که به‌دستور ترامپ، تعرفهٔ‌ ۲۵ درصدی علیه اکثر کالاهای وارداتی برزیل اعمال می‌شود.
🔹
دیپلمات ارشد آمریکایی در توجیه این جنگ تعرفه‌ای مدعی شد که دولت برزیل در مذاکرات با آمریکا،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451822" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR-ePPK0G6xcKTKpQtr9SyK6SnDgNJ6JpyWEXCqwziCNsQ3E5lIubdR3SFxtMt7mib_oVJjQ4vDAhuIlcNib9wtNwbQ1OvvGRJZphTirEtpUiad1_fEgcpuEFrcWIlZIhduk8UI7Lmg5VK_3LOFFt9oTlu4wkKBegX6iHJHpTH3hOyxqyu7u8Gm6o1MwZxF9XCxwOC0GMac8ORLoxEUUCUy1I31y15U3wPYpu09HzFtO-TGk-VLZBPICBshXHOf9ZUA96OmeaUuTNm7DJJDKkB9sQKkJ1fdd4jeeh3HUiIGdJnItvUuYOPkhJSLLs7aa9YBAqkO-1-x9pDcmCXPzMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جراحت» بیش از ۵۰۰ نظامی آمریکا در جنگ با ایران
🔹
خبرگزاری آسوشیتدپرس به نقل از یک مقام آمریکایی گزارش داد که بیش از ۵۰۰ نظامی این کشور در جنگ با ایران زخمی شده‌اند.
🔹
طبق گزارش این رسانه، این رقم بیشتر از آمار رسمی پنتاگون درباره تلفات جنگ است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451821" target="_blank">📅 10:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام تسلیت رهبر انقلاب به مناسبت درگذشت مادر شهیدان مظفر
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای رهبر معظم انقلاب اسلامی در پیامی درگذشت مادر گران‌قدر و پرهیزکار شهیدان مظفر را تسلیت گفتند.
متن پیام رهبر انقلاب اسلامی:
بسم‌الله الرحمن الرحیم
🔹
جناب آقای حسین مظفر! سلام علیکم؛
درگذشت والدۀ مکرمه و مادر فداکار و صبور شهیدان سرافراز حسن، علی و رضا مظفر (رضوان‌الله‌تعالی‌علیهم) را به جنابعالی و سایر بازماندگان محترم و خانواده‌های معظم شهدا و ایثارگران تسلیت می‌گویم.
🔹
این بانوی گران‌قدر و پرهیزکار با پرورش فرزندانی مؤمن و متعهد به دفاع از حریم انقلاب اسلامی به مقام رفیع قرب الهی نائل آمده است. امید است روح مطهر ایشان درکنار ارواح طیبه فرزندان شهیدش، قرین رحمت و رضوان الهی گردد.
سیدمجتبی حسینی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451820" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حضور با لباس یامال و پرچم اسپانیا در مراسم عزاداری محرم شهر
🔹
بعد از قهرمانی اسپانیا در برنامه «محرم‌شهر» میدان آزادی پرچم این کشور به پاس حمایت از فلسطین برافراشته و چرخانده شد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451819" target="_blank">📅 10:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451818">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
🥇
لحظه تماس با نفر اول  جام دی (دی کاپ)
🎬
این ویدئو ساعاتی پس از پایان فینال جام جهانی ضبط شده است
🥈
🥉
🏅
🎖
گفتنی است ویدئوی تماس با سایر برندگان  هم به زودی منتشر خواهد شد.
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451818" target="_blank">📅 10:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451817">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451817" target="_blank">📅 10:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b84671ec9.mp4?token=VrBh0NAF9Q4LsQ4LUE-7D21NKhlzdejaqnk197bPe1r9pdoIzGyhDKjrLY0BqqyWkcMm-C3e0v2QlPdfYCP4B8m6jfCPD3Ki2jBRXvvjzPnS-UdSJUQ41m5hkcMqHrGgybZqqj034pMi0iWVLfCI9s6YFyev4YYw3eXh_8r3Pe77cVfdN9j_XscEp_Ui8iXCTPQeX5FWM9PK5iagPVIUEigOvHpungL4yhUb0_rBGXX98Z65djG9kwf63ffQvbjUGfNcx2zYIIim0gPJ95LqowqVO8hJCNpzqwFn86dV2otM7CrP4crBd3BR4rOpykwTNcJrGCh4B7gZBWo7nUj_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b84671ec9.mp4?token=VrBh0NAF9Q4LsQ4LUE-7D21NKhlzdejaqnk197bPe1r9pdoIzGyhDKjrLY0BqqyWkcMm-C3e0v2QlPdfYCP4B8m6jfCPD3Ki2jBRXvvjzPnS-UdSJUQ41m5hkcMqHrGgybZqqj034pMi0iWVLfCI9s6YFyev4YYw3eXh_8r3Pe77cVfdN9j_XscEp_Ui8iXCTPQeX5FWM9PK5iagPVIUEigOvHpungL4yhUb0_rBGXX98Z65djG9kwf63ffQvbjUGfNcx2zYIIim0gPJ95LqowqVO8hJCNpzqwFn86dV2otM7CrP4crBd3BR4rOpykwTNcJrGCh4B7gZBWo7nUj_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: تا به امروز یک میلیون و ۳۰۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451816" target="_blank">📅 10:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451812">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1795ed65.mp4?token=s2QlXLQ7aH5ViWUH4taUbapfR9_tYrIKPddupO29BkK23N_flP5_CwWVQml1WXUoaPHSsDcPwT5djQS1l_gpOcZd7TEO-0p6wMwq0_kbMWl0AGTx3bEnVFn68FASAcbsWiMAZJWYXpOUddkeTfbFyavf1CxgWu7Y5w4fszSShYurIGJpgku0fs6-adceQ8hPDn1MpgDrBZ5YU4D8rQzKtA8SlP4wNFkSVTCv4UA-nPwQNZgbQjIKAUme-2JrA_QgODII6cwg2cR9IKJQqExMqe3TkeHxunarwr_gca913JkzlLPKtrxPTAAGrlTuI09XeKLN5EZsWU8k3YYpqsBTqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1795ed65.mp4?token=s2QlXLQ7aH5ViWUH4taUbapfR9_tYrIKPddupO29BkK23N_flP5_CwWVQml1WXUoaPHSsDcPwT5djQS1l_gpOcZd7TEO-0p6wMwq0_kbMWl0AGTx3bEnVFn68FASAcbsWiMAZJWYXpOUddkeTfbFyavf1CxgWu7Y5w4fszSShYurIGJpgku0fs6-adceQ8hPDn1MpgDrBZ5YU4D8rQzKtA8SlP4wNFkSVTCv4UA-nPwQNZgbQjIKAUme-2JrA_QgODII6cwg2cR9IKJQqExMqe3TkeHxunarwr_gca913JkzlLPKtrxPTAAGrlTuI09XeKLN5EZsWU8k3YYpqsBTqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای جزئیات جنایت میناب توسط اسکای‌نیوز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451812" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451811">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG8jP76LyBOdiVd3p6VVTwjmXZlHR1LpjirqVXwplBzJ_Fx5YZYXStXxyIHjNeIhHIynwnq-JOW5cZ8ncNebS1XdFIt25SylOhBj_jnlf8C7qyowTbRbEQT6FcBdU-gTSTdlVV82WwATLxBPgjBHr6ljyJ4FKkHqQPz-Mj_0UEX95aaV9zMS4nBiNhTDPg6bP2CJ5EiVrgz-3UF1nbBSF4E-5CYx0bsUnZkmLGkcWS-QJbwHPiRYbiBHiV0Pqn_t2pSh-QTrTJSI9Rvyr1SvubkQfaoRZUbSHotSiDOUBztyl_yGefgMzX9GoEvn3gKzMlRSFnaTj8JMZhOGmCEujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمانی کاهش نفت و بنزین آمریکا با انسداد تنگهٔ هرمز
🔹
داده‌های مؤسسهٔ نفت آمریکا(API) نشان می‌دهد که ذخایر نفت خام، بنزین و فرآورده‌های تقطیری ایالات متحده در هفتهٔ منتهی به ۳ جولای (۱۲ تیرماه) با کاهش مواجه شده است.
🔹
براساس این گزارش، ذخایر نفت خام آمریکا حدود ۳۹۹ هزار بشکه، ذخایر بنزین به میزان ۲.۹۳ میلیون بشکه و ذخایر فرآورده‌های تقطیری(گازوئیل و نفت کوره) نیز حدود ۱.۸ میلیون بشکه نسبت به هفتهٔ قبل کاهش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451811" target="_blank">📅 10:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451810">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9OjfZxOZqJS_qT4glA0Lvgn5Szr-OpJTzEQ3uITMXX1MmMwq55nfeKXrejErfx_A3wc63bue00qE40dzwcpeKYfe8wcO6WtDXJ9IZ-URDm6a2dqavgf_TGBo9c8a67niQd8KHgxGeaKR-lRPOqQfTrJWdj39VcE2B2ZI0yV_L7pW_DCkRL05nCfvx9XK5cMjYYFhFInYzIRLpRbXMhcnRBo3jyQBL_JPQd-x4pcm4b8I87ZhoK82H5EJha4pevtAhC5zYkwro45JOr3w1Lk9lP2beJgQOmEWMlSm4kmkHjbiK0tDhO0nD1fSHKb69bdNPCqK6V3qbFAgc1oWxhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند تعلیق پرواز به اسرائیل را تا مهر تمدید کرد
🔹
شرکت هواپیمایی هند بار دیگر آغاز مجدد پروازهای مستقیم خود میان تل‌آویو و دهلی نو را به تعویق انداخت و تاریخ جدید آن را تا اول اکتبر ۲۰۲۶ (۱۰ مهر ۱۴۰۵) اعلام کرد.
🔹
این شرکت دلیل اصلی این تأخیر را «ادامهٔ نااطمینانی‌های امنیتی» در منطقه عنوان کرده است.
🔸
ایر ایندیا پیش از آغاز جنگ غزه در اکتبر ۲۰۲۳ (مهر ۱۴۰۲)، هفته‌ای ۷ پرواز رفت‌وبرگشت بین ۲ پایتخت انجام می‌داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451810" target="_blank">📅 09:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451809">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77fdddf31d.mp4?token=DUgHWmY_J2FBxONPtFMzq12ezsuY8fF4zY-Ya_igjaIeFJQPgkGjBv776Mk5HRX07ewpK-j1KeQOra1UbC0gav9mm7VD8R9-OiddfwxS8oLlVZdYtWPzPT-WuCFXQrQjkM0E2ieRhZ99gHFQna3uxbpnkrkqrtMwjj3OVZKs3am_hlE5qVAcnVO-ZipLNsHCCZnynhbm1io4sJOoTA88S5qdp6AjJMabhigXAG9Nsbw6KsTtX4E1brpn1THo79RQZOp8MO8rPelYrvvxI64aX9a6XD4O7Tu4vYcZxTnF0MCDGbLYePz_NiXs2ZdV2n0IT5bpbjvYLN_JVKm0WzieNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77fdddf31d.mp4?token=DUgHWmY_J2FBxONPtFMzq12ezsuY8fF4zY-Ya_igjaIeFJQPgkGjBv776Mk5HRX07ewpK-j1KeQOra1UbC0gav9mm7VD8R9-OiddfwxS8oLlVZdYtWPzPT-WuCFXQrQjkM0E2ieRhZ99gHFQna3uxbpnkrkqrtMwjj3OVZKs3am_hlE5qVAcnVO-ZipLNsHCCZnynhbm1io4sJOoTA88S5qdp6AjJMabhigXAG9Nsbw6KsTtX4E1brpn1THo79RQZOp8MO8rPelYrvvxI64aX9a6XD4O7Tu4vYcZxTnF0MCDGbLYePz_NiXs2ZdV2n0IT5bpbjvYLN_JVKm0WzieNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه و مراکز مهم آمریکا در کویت هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در پاسخ به تکرار تعدی دشمن خبیث به مناطقی از کشورمان، ارتش جمهوری اسلامی ایران در مرحله بیست‌ویکم عملیات صاعقه، ساعاتی پیش، انبارهای مهمات و  تجهیزات لجستیکی مرکز فرماندهی نیروهای…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451809" target="_blank">📅 09:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حکم اعدام عنصر فعال یک گروهک تروریستی در کودتای دی‌ ۱۴۰۴ اجرا شد
🔹
با گزارش مأموران سازمان اطلاعات فراجای البرز مبنی‌بر اینکه شخصی به‌نام «مهدی خانکی» ضمن عضویت در یکی از گروهک‌های تروریستی ضد انقلاب، اقدام به نگهداری اسلحه و مهمات جنگی کرده است با صدور دستور قضایی، ۲۱ بهمن در کرج بازداشت می‌شود.
🔹
در زمان مراجعه ماموران به منزل وی در کرج و در بازرسی به‌ عمل‌آمده، ۵ سلاح کمری، ۹۰ فشنگ، ۹ خشاب، ریموت‌های انفجاری، ۱۱ نارنجک دست‌ساز، ۱۲ منور دست‌ساز، ۳۰ لوله منفجره دست‌ساز دوش پرتاب، بمب‌ها و سه‌راهی‌های انفجاری با قدرت تخریب زیاد و مقادیر قابل توجهی از مواد اولیه ساخت بمب و مواد منفجره کشف و ضبط می‌شود.
🔹
متهم در تحقیقات و بازجویی عنوان می‌کند از سال ۱۴۰۲ عضو یکی از گروهک‌های تروریستی شده و فعالیت علیه کشور را در راستای اهداف گروهک ‌آغاز کرده است.
🔹
در تحقیقات، مشخص شد وی چند روز قبل از شروع کودتای دی سال گذشته، سلاح‌های گرم و مهمات را از مکانی که با ارسال مشخصات و فیلم آن از سوی رابط به وی اعلام شده بود تحویل و تجهیزات ارتباطی را هم از مکان دیگری در ماهدشت کرج به همین روش دریافت کرده است.
🔹
نامبرده به اتهام اقدام عملیاتی به نفع رژیم صهیونیستی و آمریکا و گروه‌های متخاصم و ساخت دوش‌پرتاب آماده ‌به‌کار، ۱۰ پرتابه انفجاری و ۲  ریموت و سه‌راهی‌های انفجاری و نگهداری ۵ کلت کمری به‌همراه ۹۰ فشنگ به استناد «قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی» به اعدام و مصادره کلیه اموال محکوم شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451808" target="_blank">📅 09:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار کنترل‌شده در لردگان چهارمحال‌وبختیاری
🔹
سپاه چهارمحال‌بختیاری: احتمال شنیدن صدای انفجار کنترل‌شده تا ساعت ۱۵ امروز در محدودهٔ ریگ لردگان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451807" target="_blank">📅 09:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن به بوشهر
🔹
فرماندار بوشهر: دو نقطه از شهر بوشهر مورد تهاجم دشمن آمریکایی قرار گرفت.
🔹
این حملات تاکنون شهید و مجروح به دنبال نداشته است.
🔹
در جریان این حملات پدافند هوایی بوشهر برای مقابله با هواگردهای متخاصم فعال شده است.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451806" target="_blank">📅 09:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0705c2a9.mp4?token=bgzIwmDhvG1IpKqLQYIhdzeFUPRatG0aUAItL6RJIc_XodfhOCvJL9BX5_-mmAz0EFf80WIJ9lcTdvHVtz1jWL9HZj_9j8Gw146HXTsfGhtjm8ZlvqXvrm0snev_ofWo-ekXPIPsUTDeGgzti42HGytIwIv7MZeyEecHlMDm0_TKYAL7xsivPRB_MCFbqbhPHpuvJc0SODJwUH4DGPoDJ_dsi4T00fkMoDXqyc6oYfcC4Li-H7sFJFBYfC-nOkNsv3LaFfW2uUCmWYipQR5ES-nolxYK8H6JJz9RSMPOFMSv40Yp8tJsQ_wfHwntUV_PaQO2Y7Z4xGcRkI9luzmdKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0705c2a9.mp4?token=bgzIwmDhvG1IpKqLQYIhdzeFUPRatG0aUAItL6RJIc_XodfhOCvJL9BX5_-mmAz0EFf80WIJ9lcTdvHVtz1jWL9HZj_9j8Gw146HXTsfGhtjm8ZlvqXvrm0snev_ofWo-ekXPIPsUTDeGgzti42HGytIwIv7MZeyEecHlMDm0_TKYAL7xsivPRB_MCFbqbhPHpuvJc0SODJwUH4DGPoDJ_dsi4T00fkMoDXqyc6oYfcC4Li-H7sFJFBYfC-nOkNsv3LaFfW2uUCmWYipQR5ES-nolxYK8H6JJz9RSMPOFMSv40Yp8tJsQ_wfHwntUV_PaQO2Y7Z4xGcRkI9luzmdKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر هوایی از تشییع پیکرهای فرشتگان میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451805" target="_blank">📅 09:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0127444c42.mp4?token=i-4pblXWEAYUdYtaPFhtp4z265hHdk44t0eW-T2DYf3JwOwmpyKC30lnQx34xsax4zLUlp0wE5-u8_qlAfS19KLS-Yvy0qucI1zmrpyy9v-Sk2DkMzgeQM2Keb5HPH3C3qzENEJ_XFoMC4FY2pf4khQYI3vwrbhXdqgwq3VWSWx7fTF4iCOULv_51MB0T7gXYK1yGSJ_HdeqNKL8PX0nYtQdsKHWz5utrrR4Eu8gQZux5z8r4RLZw6H_V4Ne58p_ScLdywVY6XeyM92KKrWlGc9Fr9pAWScdnoo8ZmrH2g40R5v_KuqRdABYWIigQ-Vy96wvCkhRxtOVyts5KzzsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0127444c42.mp4?token=i-4pblXWEAYUdYtaPFhtp4z265hHdk44t0eW-T2DYf3JwOwmpyKC30lnQx34xsax4zLUlp0wE5-u8_qlAfS19KLS-Yvy0qucI1zmrpyy9v-Sk2DkMzgeQM2Keb5HPH3C3qzENEJ_XFoMC4FY2pf4khQYI3vwrbhXdqgwq3VWSWx7fTF4iCOULv_51MB0T7gXYK1yGSJ_HdeqNKL8PX0nYtQdsKHWz5utrrR4Eu8gQZux5z8r4RLZw6H_V4Ne58p_ScLdywVY6XeyM92KKrWlGc9Fr9pAWScdnoo8ZmrH2g40R5v_KuqRdABYWIigQ-Vy96wvCkhRxtOVyts5KzzsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داغ میناب دوباره تازه شد
🔹
در کاوش دوبارۀ آوارهای دبستان شجرۀ طیبۀ میناب، ۶۲ پارۀ تن متعلق به ۳۲ شهید که پیش از این به خاک سپرده شده بودند شناسایی و تا دقایقی دیگر تشییع خواهند شد.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451804" target="_blank">📅 09:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451803">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d8875669.mp4?token=mdQj0EAjlCqT_x8PlqugwkzaRTpeplSWC_0B45aVGRVmRWmeufM-yTp5unu7u-fDrZkt6MHsHBQU4U_uLYvT8-xNdkDLhXh7xcS7p_eDURLmF2leNcAlv0y7XY6hb3g1WIkkOY5Y0nkQhtfpw7XgSglQNI5VohsjJqnsNA2pFLHubffRawIIakUBMdoJQe_l1CkyrQRSt6Qw5S_lAD1zbvOs-ObFUK80rpqb6hWN9VDpKVEKZFtqJQLiMWq8zwm5R7vzkNhAeeqsZ4lDcYNmSrXHQ6LbgIhePw59EAYiQ_4IAU0wa-Qh5IXDTpfuePxoHWwHr4za18G9y8YHwhCC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d8875669.mp4?token=mdQj0EAjlCqT_x8PlqugwkzaRTpeplSWC_0B45aVGRVmRWmeufM-yTp5unu7u-fDrZkt6MHsHBQU4U_uLYvT8-xNdkDLhXh7xcS7p_eDURLmF2leNcAlv0y7XY6hb3g1WIkkOY5Y0nkQhtfpw7XgSglQNI5VohsjJqnsNA2pFLHubffRawIIakUBMdoJQe_l1CkyrQRSt6Qw5S_lAD1zbvOs-ObFUK80rpqb6hWN9VDpKVEKZFtqJQLiMWq8zwm5R7vzkNhAeeqsZ4lDcYNmSrXHQ6LbgIhePw59EAYiQ_4IAU0wa-Qh5IXDTpfuePxoHWwHr4za18G9y8YHwhCC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داغ میناب دوباره تازه شد
🔹
در کاوش دوبارۀ آوارهای دبستان شجرۀ طیبۀ میناب، ۶۲ پارۀ تن متعلق به ۳۲ شهید که پیش از این به خاک سپرده شده بودند شناسایی و تا دقایقی دیگر تشییع خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451803" target="_blank">📅 08:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46a0d7e8f.mp4?token=RWO55SfaymKbSsvcRu3QqhCf3mt5UafS7G53OrbFAOVFgdlt_nW-5dNiRdmVgdF6wnqCEo2yeuA8EtWYaJbPnQcsm1nCfgYW0ij8D1XhhOc4CuJSfvksFyp5eoZMx3BHSdaY2WD8N-YNFKs5ZI0W4tMsBqSP2XY2CMP0_9Q-SORK4u3EG8fvowIKwuyvXtlD-9XcXVEkWPQnZ5U7fAtjNNqRdYlWMP3zTfI2RIubxE1ag-7CtWC572BiUItZKkSHSU94ieEjoN_QEa750n6BV4pCrVjOHEW4apV0D87J1awMByhhZnLOWHIS1xWxNMP0jtzwxyjl-EeRhR9O48nenA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46a0d7e8f.mp4?token=RWO55SfaymKbSsvcRu3QqhCf3mt5UafS7G53OrbFAOVFgdlt_nW-5dNiRdmVgdF6wnqCEo2yeuA8EtWYaJbPnQcsm1nCfgYW0ij8D1XhhOc4CuJSfvksFyp5eoZMx3BHSdaY2WD8N-YNFKs5ZI0W4tMsBqSP2XY2CMP0_9Q-SORK4u3EG8fvowIKwuyvXtlD-9XcXVEkWPQnZ5U7fAtjNNqRdYlWMP3zTfI2RIubxE1ag-7CtWC572BiUItZKkSHSU94ieEjoN_QEa750n6BV4pCrVjOHEW4apV0D87J1awMByhhZnLOWHIS1xWxNMP0jtzwxyjl-EeRhR9O48nenA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چابهار و کنارک با توجه به شرایط جنگی همچنان ۶۰ درصد از شیلات ایران را تامین می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451802" target="_blank">📅 08:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbV3vPd17tnxDJ4zHuRo1TqwmefjmjrZKjM3U6EnpLPvGdg81xzzKAwiuDb08AH7mImeggvxewDJoy1g5LkZJIbC6NY8JPopawX9kHWdVltuoDIfhczCchuwyZG69qOeUHayInftScQkegOkxPKj9UlLV6PvMBNq_gVRkZxPyRRYdShclZg84EsgrjkJTLJGB9i6OIY4HWOqSMbSg8r6oQ_tf0IPvL-1wvUyH9wHotrBw4cky7ViPxVwBNX4kyN3tz6bABQ9-huHlg7CBYWJpyH6OX7CoOr4I6boFfzieE6UmEhukv_wm17gU5xr4z1cUcSrXVMD6A5OaHThe975Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0EL5r9fsNNPPtNWQcKmo45JqEd5nbUU7GAWv_jSaOy5DzbtHirRErfd9F4YRBWIlkKkYjW3loCy8xa70MZzvcFzPLO9N76Jtk6gmAeh1fiHWTfPR_IGF40PNNnBAq6YmGp0cM6fGFCN0k5eGv5WWA0DOoWUUyEOkCQwQt16t7-hbmBP3JNdE2EZ8u7rvNuv3F-9QPs2ciw3h1fNMAnmligIAKmkf0RqAIpoyC_YBnQGNxrD5Cm1DC659xaCv0CVNU-ZH_xm4S201PQsaW0JGtAZMKAotOdTEJ81CXkU9ihOaZGRVy7nZWR5q_j8T-Rntp6DIjgHvcPLo3qPRHXGPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آماده‌سازی قطعات تازه تفحص‌شدۀ پیکر شهدای مدرسۀ میناب برای تشییع
🔹
این قطعات با تست DNA تشخیص و تفکیک شده‌اند.
◾️
مراسم تشییع و تدفین اعضای پیکر مطهر این شهدا، ساعت ۷:۳۰ امروز در میناب برگزار می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/451800" target="_blank">📅 07:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8azdGQxMFPmYDhcJaeiMqdeIxt1keC-z2TlbKlXzc7xit6fQvVoMHDGIAAi44nP3ryKJY8z9mNlffhtvZZm7rkyRvXIt3gyKYw83qoIh1yNhMzwTSmp139_6SiIS8d4UZAOaA6mdNwDqVE9eFIM3sDCPoXRlWdi7zZt9K4KXRnHgXS-NboFDd4TTrMs1A5DaoXLrmI2iJjKGUR6EDslOVC53IG0cK751dVoLBZRu7LMNS19UbH1wJZ8RYdG192fhHKbycU8hqrchUuj0-XpNc2M139eIY9VuV3sVA1HaDNtbZER4BGhIsDeze5-qs8d4TaYKs4bq73HHKi55Qn_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7j4TtsYA-l7lknaCLL6dztC2STojnG8HgCSvNcf8fW2GMivF4v-yNrqYoRJ0JzNsJMveXUC1f2MhxE14JGvd_Er3Y0XG1TmfAXm-6oVASsm3alhZ3NEMN5TK6gQpRhWRjgAo_oc8_DlbV1NqZmBXjuStztk3JQGi8wQN5MjadqkoONgMDeXH2e6erf8YpCGnPq8btlCGrBDVhwodypgi4CChMhFLm_L3xwWgOT5vNhJqkFALODH4_abVZXOrm5dCi6o8Io-6H6YI4oqVDg-Kku-WEHYjWE-o3aWnBPk6wQaQj-Bv8f1ph3VYh86LlJ1LzFkEaDIufN7HkPgx1demg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVmutTOzBS_cELMy741adOn_MVpYTKpgZ_mwRRCTsO4nYV8kHC5T6hBdD5KKzG1cCeDWWf_PD218s596na79Gbij-vlByDu3-vnBe63WEHAvLuUNhGn_wwKoYeIvfr-Ie6KuSzfDDUorPK9Q2Q1265XkGkKJsmdvX6qfs1vLOew9YM-ml6xaUMFTFBtpTNmO5AQQhRPtzUfrCJoUv2TYniYdRJZxkX1vCRkBU4eYiXI8eM1OBONzEhXM7KtNKDVJLgWMK14iRnilIHE7k9ZK0QmOtS3-13_4UAh_MmzvxcwJ6S_QSYklWkquZCnMZoUXASd7rMM5ztZE3Y7k34WaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNqgYiSmQEeMKRTlu3HRU2tEdPaXw8_IU0b4Yw8FKXnCSFNvkZ_0Rd8NaGMh-hf3IaJ8N3aLiqJpLt7fryqkxPd6U4yWVeZhm_n_snAgqCbuhFOy5aINwd8IfoP-od3vpHH57Y8UgpWw7xgEQzQ68nExG4khC61glxW7oFZ-EKWNGiZYKS0-iAbbYwSvTyMy9NW-mIkSOXX_wJG1N5H0ivpiyNpA99GDUuZLsHYJF0SEJrcKwSu1QvMYxR8V99BVyVaud4Ur4MlbDaVBIlsfa5Rd5MVQzxhweHQn0XhZ7mLLo606F_Oh3Do7bSVwHDJvYT7xtXR74N6j7uUxeQ3T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTLwstDzxsbe5Woj8jGV1p8d2ebggd9eHuyicoLmM5nX2r3puv9xs8_M2IzLcGm8tZKHiw5KfeJ5_08c_oU2C22cnMkDOo239UVHCixzyXMJwT6BE5TQ4w2J4vnqVhdoxK-B7usipGhD2hCzEsKbfJ-2pI53VTzUS1it5VyvgfP3muUh4c-zo4ezrcx-JCnS-IBRW4kWuqJS3ocVhHiJsQkcq33XcWIuOGbRterFLds_IcpuyYCmEBUe6GmA2WuK3yb7jZy2pfcJQO4dktBS6PnKqdwyOwuDDRKq42mKdsTbvXalpM3cVpQY1mctStbnfXNRcbHd42Je9sSKavjyWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزهای داغ تهران
عکس:
عرفان باقری
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/451795" target="_blank">📅 07:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrrQEwgULRXU66kCjzt0ZlMjtDrqfpRhcU1lfiberCaLaQd_F09HKx408dg9InwmFo98pZlS9Cs66aFbp8KWpRb7eaH-JHewrhIPA33SUkxaY-Kadt4d9g5qn9NSRljhJIDZmdZaBRIZQNA-xr1p4Fsbb5MSdWbCsLklBIxu46Upw6pS8WOqyMSxVwQ6S4YJ5TxMwOy2qLCKsJU7PYv8rH1HnpKmwp4Pn2KEcGmo2apbx3tQmdtBgws5SDjdncjnMQCLdUd5Ap6XtJ38WUpW4QJcJD5sa1TjkGoAGueVs3_VlJTe9vcQxZ5ERS6V7DLW8guSKxdMReFzTOnlZu-NCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روبیو: ایران برای مذاکرات جدی نیست
🔹
باوجود اینکه واشنگتن طرفی بود که به الزامات خود ذیل تفاهم‌نامه با ایران عمل نکرد، اما وزیر خارجۀ آمریکا ایران را به نقض تعهدات متهم می‌کند.
🔹
روبیو در ادعای خود گفت: می‌خواهم یک بار دیگر تکرار کنم که آمریکا همیشه به دیپلماسی متعهد است. ما به حل و فصل اختلافات از طریق مذاکره باور داریم و این در موضوع ایران نیز صادق است.
🔹
متاسفانه، تاکنون، علی‌رغم تماس‌های مستقیم و غیرمستقیم، اگرچه به توافق رسیده‌ایم، اما آنها به تعهدات خود عمل نکردند.
🔹
اگر آنها جدی نیستند، ما هر کاری که لازم باشد برای محافظت از آن، منافع خود و همچنین منافع متحدانمان انجام خواهیم داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451794" target="_blank">📅 06:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01fd54a95c.mp4?token=KsfUomW2fOzBORbyRMdHNtBLs-5bnl6JUWXwsMJJGPI_eO9wGveLE13Ga52ZtsobTc2pURbU7OWL0Jl6CZQBMcmxQniD0Wi9SChjRDBTgrluIRiu_e5Vu4H1o-RaNYNVRxjVSKvVl7mD1Cyils2vLbrWQTjqVLo7uI69RwdEH9K9As-g-7a9V6YdlyjAp96SJNE-ZKgN5pd4wtq2WKNjaEptHFlVhpFTOSEj8ahrG4hHFol4B7LZ9W1ZpFTnjZTDRaZvMgQR-tT0ENTuz3egg8RBdG3YEN4fDkj_X5opMyg85WAro9PXMnwgqe57_XsUv5vQdeC33z0Q3ALVY6F_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01fd54a95c.mp4?token=KsfUomW2fOzBORbyRMdHNtBLs-5bnl6JUWXwsMJJGPI_eO9wGveLE13Ga52ZtsobTc2pURbU7OWL0Jl6CZQBMcmxQniD0Wi9SChjRDBTgrluIRiu_e5Vu4H1o-RaNYNVRxjVSKvVl7mD1Cyils2vLbrWQTjqVLo7uI69RwdEH9K9As-g-7a9V6YdlyjAp96SJNE-ZKgN5pd4wtq2WKNjaEptHFlVhpFTOSEj8ahrG4hHFol4B7LZ9W1ZpFTnjZTDRaZvMgQR-tT0ENTuz3egg8RBdG3YEN4fDkj_X5opMyg85WAro9PXMnwgqe57_XsUv5vQdeC33z0Q3ALVY6F_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه و مراکز مهم آمریکا در کویت هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در پاسخ به تکرار تعدی دشمن خبیث به مناطقی از کشورمان، ارتش جمهوری اسلامی ایران در مرحله بیست‌ویکم عملیات صاعقه، ساعاتی پیش، انبارهای مهمات و  تجهیزات لجستیکی مرکز فرماندهی نیروهای زمینی ارتش جنایتکار آمریکا در پادگان الدوحه در غرب کویت را هدف پرحجم پهپادهای انهدامی خود قرار داد.
🔸
الدوحه، از مهمترین و اصلی‌ترین پایگاه‌های نظامی آمریکا در غرب کویت و یک مرکز پشتیبانی برای نظامیان آمریکایی حاضر در غرب آسیاست که حجم زیادی از تجهیزات و سربازان نیروی زمینی آمریکا به همراه نیروهای دریایی و هوایی در آن مستقر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/451793" target="_blank">📅 06:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
حملۀ بامدادی دشمن آمریکایی به بانه
🔹
فرماندار بانه: دشمن آمریکایی بامداد امروز چهارشنبه یک نقطه در شهرستان بانه را مورد هدف حملات هوایی خود قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/451792" target="_blank">📅 06:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721598e238.mp4?token=e7Kwi3GRbEx3VvMi72dk0LARR5GGj6ygQ7AtVoGwG-YcxsRY5JAvsXRMDA6kWNxxs2EuA7QMNgg1lUkqkn4qhZhKNBvGtgRF_wUmnOYfiNZboUq_bQ_p2PrdNRxjpfTD1L5V8to6XIkOVDpyxJo7hMm3WRi9Gqt1jF0TOPpiReIGuLFn5Mt4sICpkEozaG3m2sy3XrE88wlWtCsqex-mXo3-Ahwegxyi-6iavwfUq6FhYJSCv_tNYY0wwgoi3V6PfsVwbhag1fzKTyQfZ7E5ysViFcCjH6jaA476EydhAoQtcN_ubOVX7FSW1zNqeRqEOTiYUVAyq9S4V9Rlm8CmW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721598e238.mp4?token=e7Kwi3GRbEx3VvMi72dk0LARR5GGj6ygQ7AtVoGwG-YcxsRY5JAvsXRMDA6kWNxxs2EuA7QMNgg1lUkqkn4qhZhKNBvGtgRF_wUmnOYfiNZboUq_bQ_p2PrdNRxjpfTD1L5V8to6XIkOVDpyxJo7hMm3WRi9Gqt1jF0TOPpiReIGuLFn5Mt4sICpkEozaG3m2sy3XrE88wlWtCsqex-mXo3-Ahwegxyi-6iavwfUq6FhYJSCv_tNYY0wwgoi3V6PfsVwbhag1fzKTyQfZ7E5ysViFcCjH6jaA476EydhAoQtcN_ubOVX7FSW1zNqeRqEOTiYUVAyq9S4V9Rlm8CmW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/451791" target="_blank">📅 05:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT7bwtdo_riwGy-yQmDgOo0m7MaATnj-hSyZ0wi79mfpvy2ntZsDimFkM_n4X8S53Lo_rKGWPLIbI92riM7e5l_tgIZrkjLps-MspvarMZ-nkB7h9qs-J2L6Y319yeyuvgnwyxjgPumz4aj0p-swgesCbSXNPpVEZKP2_X0ERGoygnuH4L7oARHlRuFt5w4ydTZJNTxgVV66jzVZTIg6FXQ0CDyOVYpZhpeZURZIZcoSHKq5HWxcG3Cre1AfiNsjBOMJa5xHD9ScL2IML_8BFm1V6DhQqhpAE-B5tejxbqWVkiFj4_gpU13BahUXQU7xK14tBm9ndVvVFYmAKJaApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت ترامپ با قرارداد همکاری هسته‌ای با سعودی
🔹
مقام‌های آمریکایی از موافقت ترامپ با توافق همکاری هسته‌ای ۳۰ ساله با عربستان سعودی خبر دادند.
🔹
بر اساس این توافقنامه، شرکت‌های آمریکایی می‌توانند تأسیسات غنی‌سازی اورانیوم را در عربستان سعودی بسازند، در صورتی که مطالعۀ مشترک آمریکا و عربستان به این نتیجه برسد که چنین پروژه‌ای موجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/451790" target="_blank">📅 05:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
حملۀ آمریکا به نقاطی در کبودرآهنگ
🔹
معاون‌استاندار همدان: در ادامۀ اقدامات تجاوزکارانه، دشمن آمریکایی ساعتی قبل نقاطی در شهرستان کبودرآهنگ مورد حمله هوایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/451789" target="_blank">📅 04:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن به بوشهر
🔹
فرماندار بوشهر: دو نقطه از شهر بوشهر مورد تهاجم دشمن آمریکایی قرار گرفت.
🔹
این حملات تاکنون شهید و مجروح به دنبال نداشته است.
🔹
در جریان این حملات پدافند هوایی بوشهر برای مقابله با هواگردهای متخاصم فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/451788" target="_blank">📅 04:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farsna/451787" target="_blank">📅 03:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به بهبهان و امیدیه
🔹
معاون استاندار خوزستان: نقاطی در اطراف شهر بهبهان و امیدیه توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farsna/451786" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIiEMut_G6_Movwk8iVqUiUUryjXmgOjYpXGvAo96rPRbTHjYgzYD1JMG-DSxTFH2fT0B1u2OkZdOYNh-P7Soh_-MfbzZ14MeBOZ08bBdHgaGNcPehWsKb-_ykzi9S6B48bRadfp-X1LmrP6eSJsZnaKcU4iotvq4wOpqptQPtIwQMJHArOa-SmiPGnxUHttnmDorUxLXNWzoUAzzYYoc1_Sjh3AQDEV3ksz39quQ8waPTb3ZPhx7IENqh4qicMZnaI_gOkYU1ok8aOo47JmC7J68zP9GinJcQbTTU9jQ514UiEj7JKZjxLXj6pBGmILmRYZOo-OkCage3Pb4XGnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/451785" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شمال شرق تهران خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/451784" target="_blank">📅 03:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در چابهار
🔹
خبرنگار صداوسیما: دقایقی پیش صدای ۴ انفجار، و برای لحظاتی صدای پرواز جنگندۀ‌ دشمن در چابهار شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/451783" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجارهایی در سیریک
🔹
دقایقی پیش صدای چند انفجار در حوالی سیریک در شرق هرمزگان شنیده شده است‌.
🔹
مردم سیریک حدود ساعت ۲:۳۰ دقیقه هم از سمت دریا صدای انفجارهایی شنیده بودند.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/451782" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/451781" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در ماهشهر
🔹
دقایقی پیش مردم ماهشهر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/451780" target="_blank">📅 02:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار گاز در یک واحد مسکونی در نارمک بدون خسارت جانی
🔹
جلال ملکی، سخنگوی سازمان آتش‌نشانی و خدمات ایمنی شهرداری تهران: ساعت ۲:۰۴ بامداد امروز حادثۀ انفجار در یک واحد مسکونی واقع در محدودۀ میدان ۹۵ نارمک به سامانۀ ۱۲۵ اعلام شد که بلافاصله دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند و آتش‌نشانان در کمتر از چهار دقیقه به محل رسیدند.
🔹
محل حادثه یک منزل قدیمی دو طبقه بود که سقف حیاط آن با ورق‌های ایرانیت پوشانده شده بود. رگولاتور گاز در فضای زیر این سقف قرار داشت و به دلیل تجمع گاز در این بخش، انفجاری بدون حریق رخ داد؛ حادثه‌ای که در اصطلاح آتش‌نشانی از آن به عنوان «کپ» یاد می‌شود.
🔹
بر اثر این انفجار، شیشه‌های همان منزل و ورق‌های ایرانیت و شیروانی دچار شکستگی شدند، اما خوشبختانه این حادثه بدون هیچ‌گونه تخریب بوده و خسارت جانی یا مصدومی در پی نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/451779" target="_blank">📅 02:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c8267b6.mp4?token=e_RhUKQsHs41PfR_RY7gK5ZnvlYxtAgNCdH28cfElCaSrncEQkQAG4myWrbFxuMxNdgSiEQluQBpC7TyThkuLLEQU-g3kr-HnTlFFUiTt6Lm-JlG9IQtDGUuw7d1QOxXFG1eHUgwlbR8Eo1KpWhoQLT5GgZSAVMv0nYQ1nKHnSbwze3S7CNzE46TuJB5xHTi3FODuP5W-vtw4C9DVApb-bREaHVe5p9SIINxff8G1SFiACv_hbtcmRsE8IeEtHuwJSi14jZk8HXgfbg8dRAoVej2A_Y2OXrADy_bQxpnAXNrNcewQMQtFNlBo0XMmrU7RrQHWe8sRKZvdHLALEBTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c8267b6.mp4?token=e_RhUKQsHs41PfR_RY7gK5ZnvlYxtAgNCdH28cfElCaSrncEQkQAG4myWrbFxuMxNdgSiEQluQBpC7TyThkuLLEQU-g3kr-HnTlFFUiTt6Lm-JlG9IQtDGUuw7d1QOxXFG1eHUgwlbR8Eo1KpWhoQLT5GgZSAVMv0nYQ1nKHnSbwze3S7CNzE46TuJB5xHTi3FODuP5W-vtw4C9DVApb-bREaHVe5p9SIINxff8G1SFiACv_hbtcmRsE8IeEtHuwJSi14jZk8HXgfbg8dRAoVej2A_Y2OXrADy_bQxpnAXNrNcewQMQtFNlBo0XMmrU7RrQHWe8sRKZvdHLALEBTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان حمایت: در ۹۰۰ هزار بازرسی انجام شده طی امسال، ۷۰ هزار میلیارد تومان گران‌فروشی و ۷۰ هزار میلیارد تومان قاچاق و احتکار کشف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/451778" target="_blank">📅 02:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9171ddf436.mp4?token=AyWPUZffwiuZrIAJUp1NR4eCQG7SlFb649vXeMvA6ZyGSd5IN_PG2aEKorwCkQD4LU0vdyg7hSg8ZiYvV5NAcaRRluA6Tmp-KV8b-xaFjPEFUt2o6g-a2Xr8rApjZG6tCqFizdIOHqdqodGmsWYdwVbUoEo2-88rGgEqLJnIW1Z2TWgtJ9aPDIn_tlZqRMVwo5cxAKDCTWC2xD0mWvrxJhCR_Uhfqd8gfKq3IOlKYClZ07Zz2LbU3vxP8eYhmG9Ckxyu3KaxGEVCtZCZrj7ISVqJNjgN2yKxN_VH9hXrl06g-za-dIjaCgFDDnqEfbc3Tlv1VeOHyhR_PydTikppqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9171ddf436.mp4?token=AyWPUZffwiuZrIAJUp1NR4eCQG7SlFb649vXeMvA6ZyGSd5IN_PG2aEKorwCkQD4LU0vdyg7hSg8ZiYvV5NAcaRRluA6Tmp-KV8b-xaFjPEFUt2o6g-a2Xr8rApjZG6tCqFizdIOHqdqodGmsWYdwVbUoEo2-88rGgEqLJnIW1Z2TWgtJ9aPDIn_tlZqRMVwo5cxAKDCTWC2xD0mWvrxJhCR_Uhfqd8gfKq3IOlKYClZ07Zz2LbU3vxP8eYhmG9Ckxyu3KaxGEVCtZCZrj7ISVqJNjgN2yKxN_VH9hXrl06g-za-dIjaCgFDDnqEfbc3Tlv1VeOHyhR_PydTikppqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ قطعی برق گسترده در منطقۀ کردستان عراق
🔹
منابع عراقی از قطع برق بخش‌هایی از استان‌های سلیمانیه، اربیل و دهوک خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/451777" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0a0cb6e0.mp4?token=b3ZEn3fc-Es1OZVBqZmG2g2waf3NoaubbqkIcyBbGB1nPpKv4_dOM4VBB_wWqEdU-7jhhV7k2oxXkPuH52HBPPKQ90Z6GnDpVFcxx2g9tGS13nDBlz9oSMb8ML9b_Mcy9uutKY80ov5a5lkTS8r6rq98AzDyXUpewZIYFBIH961_S7MXWN-WVzGpR9C32xDPEuWlNXp7vvl02F22t3T8JyTPlL-5O5-TvzYjJe9WdCeEhPGvSbJDsToOkFvFCX_tifXBH5JKB2KiKfFRTSSlVlxXV2Cw-5ceY74ZPCFW1fnzSz_BRUy4U6f-mx0ZP6DUhhSDLrQsGok3NfpDtIwNiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0a0cb6e0.mp4?token=b3ZEn3fc-Es1OZVBqZmG2g2waf3NoaubbqkIcyBbGB1nPpKv4_dOM4VBB_wWqEdU-7jhhV7k2oxXkPuH52HBPPKQ90Z6GnDpVFcxx2g9tGS13nDBlz9oSMb8ML9b_Mcy9uutKY80ov5a5lkTS8r6rq98AzDyXUpewZIYFBIH961_S7MXWN-WVzGpR9C32xDPEuWlNXp7vvl02F22t3T8JyTPlL-5O5-TvzYjJe9WdCeEhPGvSbJDsToOkFvFCX_tifXBH5JKB2KiKfFRTSSlVlxXV2Cw-5ceY74ZPCFW1fnzSz_BRUy4U6f-mx0ZP6DUhhSDLrQsGok3NfpDtIwNiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع صحبت‌های هگزث توسط مترضان ضد جنگ
🔹
در میانه جلسه استماع سنای آمریکا، معترضان ضد جنگ با قطع کردن ادعاهای هگزث، فریاد زدند: «بمباران کودکان در ایران و فلسطین را متوقف کنید!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/451776" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad125befb.mp4?token=I2eZ9FCAch1imqIYEvANPdaV8OzN0c_jpIhN10JPNZ9xX2y5XcHoy2BbEHxm6J6qMtBptEMf756yWDxHH4l5bbL4iVfQlK9wUqBorDIkrYf4mHhmfVEBVS7equYSamvuOjwnh2bHeZxthGeUtjxJ6DDOD6ODqDPnY9u8-SdHja3cPEyjJi0yxSVDKzdi93goNjK0axOWFr1ll65U57xhGsSRPzvDpRd3loGFoyBT5tECZmFof1lWtdIixTrj3vFjbQ1S1jDTgcGl2M-eznqMt0-xxKvUdv1V_LzxCq3duVFmcW-FAbBAIxg18PMGBsUXHnGa7vQul2Qts-gmRPDbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad125befb.mp4?token=I2eZ9FCAch1imqIYEvANPdaV8OzN0c_jpIhN10JPNZ9xX2y5XcHoy2BbEHxm6J6qMtBptEMf756yWDxHH4l5bbL4iVfQlK9wUqBorDIkrYf4mHhmfVEBVS7equYSamvuOjwnh2bHeZxthGeUtjxJ6DDOD6ODqDPnY9u8-SdHja3cPEyjJi0yxSVDKzdi93goNjK0axOWFr1ll65U57xhGsSRPzvDpRd3loGFoyBT5tECZmFof1lWtdIixTrj3vFjbQ1S1jDTgcGl2M-eznqMt0-xxKvUdv1V_LzxCq3duVFmcW-FAbBAIxg18PMGBsUXHnGa7vQul2Qts-gmRPDbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/451775" target="_blank">📅 01:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLytiPTqOe7LH-NQhS7c38_N2QbKuojCINRlMZ5Hf6-TMmg9GVftWp0u-YPdfPXGr93pph1OLTiLt5DYghyzRpqakZJWKTaKtFX4_kU4ncxn4yxbgcq47aDgC2wiMMuiCKjriV61pI8TTN9C0JORc-AAxIJGJncRSALHisKXQNxWK5B-LVbPHvGEmyxF6AJZiuVxsvb58mNJXWV2IJdeKY-rA-GwVT0KHnN7o7_bf7gVBV7Zpbs31xr6GRHiLznn0-ReyRskFGUk0cAe4UiW8YOTrmRfNwvm3ZtSWtmih1HOhXPNdCi3eN0-BS0OEXwh0WF_-CvKOBfum7lxyeTQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودای رئیس‌جمهور لبنان برای پایان دشمنی با اسرائیل
🔹
جوزف عون در دیدار با ترامپ در کاخ سفید تأکید کرد که هدف نهایی، پایان دادن همیشگی دشمنی بین لبنان و اسرائیل است.
🔹
عون، همتای آمریکایی خود را به ادامۀ حمایت از ارتش لبنان در آغاز اجرای توافق اولیه با اسرائیل ترغیب کرد.
🔹
وی در این خصوص گفت: ما باید از نیروهای مسلح لبنان حمایت کنیم. بدون نیروهای مسلح لبنان، همه چیز از بین خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/451774" target="_blank">📅 01:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odpPtarsLtV5vvzXYuNZTlQwm-tembeh2155S6JWEIPoE-_b00ASL6YrN5vUFAf_7DtR-K_ETxM4B8hzPUuWckOOLBnoEpIljobQqHGbeqWw7py2Twh6jn5ItsbJ3ZK6UitTVl-IIV6bhfXiG5bJ7pV9dpag7sB9fSSNOStFrgekZT-3pb-1OgApKBBUOOUAoLp4BGojbSxcwgppPMxb5FKwD6uPtZhPvaQD2u6bEvzbXh60VwEkEu83ZW7PNkq81N5ih4WJEXOmodGFgF7s27M6jYjdqCtNUleQOzWEPggaMJHpukHRdY3A9iIkoO50LpuG-6CIgZZHGinBVjpYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2SCladuotH3TIXIPr9HWyC1Q5Ug_hDzdjmej_ycLXopci3ihcrudoMbb3EolPTJkGrt8UHy92UXpzG-g9YBkou9ba7_ytc1gfI1D8vbe5RaRwO_vJJQLAmoMdiVQGt3GWc1AcOLJJLsah5yLfIAoA5xxyz9lGBgMTq76U6JZUgGaLN5Akp57j1vL19fPCU54hRYHpybBeC8zLL5PS4m8Dc-FSZzaHXoOB7yAoe3X0YlArHK3hYpvjvV-1F566enWnJuKjiipAqB10dUt_uHhN-VPFz5ASDq06ValdhIrdIxFEWSSDYO0XgCs_tXIvurszFgyTAYXSHV3L-HKDS7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5WM6PECjQjd7AKKzqmsrfoM-Fl_UXmpt1hjmKh7tvq6yzkx8XpPoDF7KoGmwbHzVRhEohj2NW2U9GplIL6kaAVzcmSzkjx-xHYlamgfPDnBDSQMBHHS8hLXtfEUw4MEQvtK6ekHC2Vo-OVuZLEWPpLHU8mDNYtk2tetRaJk0qb35hFv-cfRSkJomC3skZk5bRtPvEcRIRPmpw4o6FmdJWiYyFer5pEOQKlzrDtfWpLuOtb6ui0X6Uc8Bs6dhzf36Gq3p8a_A7d85TeoR6UuWeAu-1fywl1xBZ3QU_sZwdly7mPnS_62zb4OK29uMNXzu_utnmltDENdfmjoT1aS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNXUDU4EJHHF9-TrSkh1kKz6-HtVJXbDwkdZ3EiHuE7pFXvFVmupl9TfkzOBpNJMWFHLuPY2y7Y4wizTDBqIem15vGYJ155WdEmVtut5fuazcMKCNuza6nK1H0F1I6R5WAFna_May6DA51fAMiBFMS_sdad49_VUpKTtJ5bV85djEvCh4GraqqLz6unK6tHPeq8DxgjYDTTvlOmrJJAOl-sIy7qkgTx1-4cCLOQvTQGqe4L0RuNgLGHR9WUdDbzZjQqHRCLLzCnQF_goFyIDrvFKtYijkcrE0fAu37OHQecNFsTXNEB8W1a72JgJIKH-A8KrVLPpc8Mj6cQD6-nZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StZrB8U9cEc77YseyUoYc6JlY_3F_4-Ot5DYCh1Ia8rrhKoInu05ywYH7o0ua17UV0IiS2iq57iWKBElvQTcl02NR43I7jogPLYY8HuonzEQmd9wHb0gL-jX8wxgjgFx2sQZqFVTHAjLDeEuFuUqt8u-asYgVzw0jrqHiKLbw5wgNmVwLBgOhaXRFqFc7WPg59_l9G9IC9ITEx5_f0xJ_RRnNy-WLNTuFzer39yPPNXEua9iCDgnlacT-yd3Py0KfAMhJTMafdsKSpOVp-LOCbJGLqQHwVNsaMbRBOAR5oYK-KuM81imu-ULIXwsOKI7sBYq2iCm1xksN1NiNOqE9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۳۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451769" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMHW9-HM-wo2Ti6N0z3nU45GkN9kKIgenDuC0u1Nyzn_YGHy8GLOmEIa_GPteYhpILjQdY_ZsFmJXCr5WKkiR3q5wdNpBWgEYJm1n6VrJZ_nInuRIpQanWPW7MXTdwLsbBfxjPzKe4y7XcnC7pAqvSh-3Ifjz01160yhJf_Vlznb6OhniaAJlKDa23Txv2g9__ncjMX7nS0gnf2F7BokG3ZHTuPo0_tnxBmLG-DMP7sXQWkjAZxJMP8PTL4pJj4AbTDIu9IeqL3kaHdJHnh4bWb0uIlggj2gVXGWFZud5BkVEe7HuMNuH-iFm6vEeoYJCebkzXRAw-gSdhG9X056fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9IJIg9ldf2GdlWff_GLwPHVirAvSHgKzrNuv836UPcKhuBeIWLvApOUfYTgDnCO5RgJQG_q0fbm1rbbrnsDU8VyPedBweYjMqHHdvtV2x4mRnXEzeVLq_XvT_ILFXz5Fsz48Hmh1jDT8gFdbkQNc5Io64-Zy4Bzqwp-5IY2i5ORm5E9TZkcFq6hEVYW7SEgXeiXRksKYGb_67FFqtb9pPWMV8cZpjFuNDYmV0RiW-Ym9JkuIfQumZgZbgyd_fJyvsL3xXFud2MTcbGnNeqKTZ4nxNY39Xji_4vqCE6DHdQutAvn2TSSuK3sHznM-fli4OWGFfMQPKBntE61h0uS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmDQfNC2ICdHHHTPEbeZ5Lf5MHAKgGadcMCGtJULBRrtFEY_NQBHROjU6QbILSreoF7dJEldUe9ScCLH8r852O2X0zi1pOj6IdiXEm_rmwUpa0AGIU9c4pvPUugHiAXWKz-LorZI1Xizzh6XofcZfz7QUhdREeoUNFXAmryRnSgtMDdUxIg144PMuCb-dHQS2Ck6fjJ4P0R7G7kQduULM1KONMZtIPiI7o6ysGF33p-60utrd-CfCqP45nERiupgfcIANSy9ETSW8Too-1tLyGmDcIl23mCe80DvIh1hipO7Qt-UH13n3IYCHG0OtWsCihKVMpZZIw1K-FII7hnHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGaikiqePBmsxfhSzZ_QZPf4D4szwuY8TdMtLDBT6uqGGS2t80kVqoly10-PTHbrNFXvKWz9CopBdEnBua2L19VHa05_yg5xOjNj1ikG7OCBBSVQ60I-AJR35jyVc6CtDeN-4sWFqemfaZMje4s1YlW37GJ8ezVVp5io3mhiuYfWAHKxGAOWK7aq1karbcxPws9iHbhdQz6DI9_-2ZQeJ_5WDuiS62EX_1yZCIEk7A3Mh6WcJirLq3B0VlwIWdi5V9kIj1fHl3VJEKxiLW0vQHHLumEI1_np740l4EdXnulXmv3BEDQ-YCO7sQTUP5UGdLFhzVBmXTXSGJMxkAsQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbXwUfFegpHLzZdWoWRvsM7-DuMLoVpnXlUSoc6wcBY6UceHwIFtyikV4F9b3tndTHSdDQKtdBFxsGcoJXw-UIexHiJGlzRIyQU9B4wBiMmaGEMDI1zevScj2FO80W41oUu7ZtmJhvYCpvDBC0ocQfQBKUQ9kiBu10yTMXwhVgKAYQnvMnugtdOC6zRnCPrD48-3kispTT6LgaoYTo0fskvU4T6ErJEgh0dTOlm3_T61kAnPLqlZ5Jkv2JeNRlQD9y9V_DHEasypmG6BJM6Az8mU2ecbo2maWbHOgDAYJRHiYW9B-KKEArzz_W5XOKVh24k18QgtE7cF_hjRF_34CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKqIwe5Co57VcaXUTtyMMjcSJUPNqhUEyM2Su6WRAQZ9r_Jyo396ecbCqjyiHoZVqA5UYFTyPR8c1Uy_WD2l1Xq0y7V4Q0PsUaB8qKHmD-LNurZesAaJATRUo8Wx-B9UUW3AZu5WIWwYcXdr3r2ipQE5bRy63GeOJT-7y1GS6AV9wZeuMmy7hqatBfchAbY0tBHa4zG_YFM089TLYJTzWrUNat5_dJH0VOMMmoVknPMFtsoNxeCnD01Ld1mqHT7HBYZKdLjvBa_gDkjojshDry04BIEYlptOKQqTgeFFmbBFU6_-NwnSmVroOBYaqhQzklUgQGayiEhUpaOfDyNa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEs2lDb9wKu5Sa-SW2tdtawNS-6ux2B4AQEsF3CdWPe46kW5QFy5bt2b8qUSde-R-nGqrszjwLnTEM_lWEjnWARJh05Qlgzvqcg5peU7m5waNI-hwgZh0hP8lEqSwU4sU2PXtFBqWGBR_8p0Z1swxqXKO0WApDrGeuij6apG_JITtMCEjnLqkIelajtMWr9t_IQft3AjlUFVxf3TI7EopXC2tfkdPdLZWbfLWMSMKF6PGnCHRabH1tcma4usFyySP_LOP_7H_H9UrzHm69jUDfgIdRHA2_gLgGAZ80er2ZoMIQm3blsv9YKdSe0Fh4pVtRmjG4TI48Y1iCgizXMPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LagNz-Tggq2ZXmHIQ0-tAf9Dols7U77j_itVeAqfBtywXb97bQHLcligWnzVtJWoOGL_oobjjKg5cx8ghvbf_rtcFXkxo5kmLupfrLJT374gdrlofoxtkqSQljga0z332kZvxgo61ILx7w9PEOGdR3Bpfo-nZHoEKRxynpFII3egylpu2WoSUKkqrGJI_BRflcKa1CK9neQEwJBUkectU3GaRcx03qbWfzSUi2OTrAC4rNQwK9feYoQnS1xnoKI-6YdWuwA-26vn8xrSZgs-bVcruDMFrGZjgyOKuiFqwdgLEIeWfIOn1W5XCi6vG3Z5xQ59JSdONe5EE7EWjTCwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeudu0e1CzfEoIf0j-k1nTSaqlw91RgxsEDCNT0WaykqxrTJw9T3W8tbRmnWBhtK54hp72d2XTQiQjUSaIZyC6wDLjn8jD7TU3kCTrk_i8Qc-zShuTz82svyOHdKdcThF0hEGXEnARM0OW7ieF3uRdWtnFBNJk_Bl0iOjkfFVdPV7qipXHa1UMJXiQl90r9tJw5hkqntQeNQo2v8EeEZtMgiLairg5L9I6F645Ju9REJqY_adIBVq7vq_AZxVmW_cDLVu7hP4wEYCiXXs4ud38gkQDdGpcnaEPqqpWjPdlAIE1LbgIXeh8esGNu1qu3yDLi1a6hifqhxzOCkaJc3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATL_a7N7SbXgMy4kAtGA1pQu-vhXiW0PwFkTZ5nVRrkiG817J5ct3xJEo8tnBCIO0EgSya5w7KsqUzM2y3DQCM88ZOtiRZJYa94bsF-XtBmwNNLgEA7zXwCZRgJ3YajMVWt0kbTuF42NHWBNCZ7LM3oaA_5QtyL6S1zAN9MQhnzwzfjb0oTll_KZkgE4J72l_gmR3Ny_NmKOU6LJPdg9uSm52_6YGLPJexT8ktoG_i-auawQpTSfGtnxAu_NJy0o_5ETPcJb2CRCSAos_LdRFzLwfB7UMBXcbSeZZGXDI3dzYPfqQ1BPOz2j_4S6nsUyzFgl67nyiNRZbKUDjIVVUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451759" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451758">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451758" target="_blank">📅 01:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451757" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
منابع عراقی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451756" target="_blank">📅 01:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451755">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmAxh8dL-Jkqv04RmiYCORn0are9X2x-ANFkARhkE2T5R0uIJ5ac5EptN25ZyLMwvbNY-zEmH1NbP1hpId9SzHjNaFAELmD0BjiEeN22988-0z3DVundMP7UYHdbGwLjVv5Mg5icj7VaScwfq7V3E3xL7Q2Mq_LvXIlgydJaziGdgoJ4_dqeXwiPxnbUzKo-GJWIkZQIjX93cPvD9losaddyh8RnN5SXZpZX-4o1KkWd3gEeQxF7CZcoezzLq3mApCo5x-K__q9hp5zVgT56X2Vc2VbCmpFKACQKXpapDphLlF2Yfn9WIp0-FriYYLkzfERMeUyGAAVH3qksWQnzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم دیجیتال سنتکام در بحرین کور شد
🔹
نیروی مسلح ایران در واکنش به تجاوز آمریکا، زیرساخت مرکزی داده آمازون در بحرین که یکی از گره‌های کلیدی تبادل اطلاعات ارتش آمریکا است را هدف قرار دادند.
🔹
منطقه ابری آمازون در بحرین که با شناسه انحصاری me-south-1 شناخته می‌شود، نخستین پایگاه متمرکز پردازش داده شرکت آمازون در خاورمیانه است که در سال ۲۰۱۹ راه‌اندازی شد.
🔹
تاسیسات آمازون در بحرین هرگز یک پروژه صرفاً تجاری نبود؛ بلکه در عمل به شریان اصلی و مغز متفکر پردازش اطلاعاتی واشنگتن و متحدانش در خلیج فارس تبدیل شده بود.
🔹
مهندسان آمریکایی این زیرساخت را بر پایه سه «منطقه دسترس‌پذیری» مجزا و ایزوله در نقاط مختلف بحرین مهندسی کرده بودند.
🔹
آمازون یکی از چهار پیمانکار اصلی وزارت جنگ آمریکا در قرارداد «قابلیت ابری نبرد مشترک»(JWCC) به ارزش ۹ میلیارد دلار است. این قرارداد به پنتاگون اجازه می‌دهد پردازش ابری، تحلیل داده و ابزارهای هوش مصنوعی را در لبه‌های عملیاتی و پایگاه‌های منطقه‌ای مستقر کند.
🔹
جزئیات را از
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451755" target="_blank">📅 00:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdy2fClS_inf1VKxS80kq4jPFWzbYItBzUmqjcWReT6PmR84ngx2zPRjyGRUEg3FAn8gOV1q5_aNQGpM1xHt-YlqsP5RDDF9O9elm7ofi0nePidDHeL40LqinKdyOa1NmpdUUONk3PmTdOaCgtetiXmHJ3aAdDOdeR6gVMjwqSI9FHCo3xWPmWjSD24XAg9o4MC_Vt8ReASu6vxmb-yF3NMKruac8zxJ__SuO0044usybl-WWfyhBYtWOtNsembpPd7TQo6uJGBAzLoPKH9a-aU5Hs6VsONYZzMC3Y6dbwzfsqq0zhsCitCsFNc_4HmQMFk2r7k-1VFYNrB6u014Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e6c3b61f.mp4?token=GtoGdGd53CbOTXhLG_J-HRSyuHSHbuB28tMXYZ3JVKQz0Q0S9VD7ivSgfgq-oIyii0CaoaC_wlWxPoWTGRNHO986llhGkOyQ_ACmQHvZgrMA8Wq3qTb1Lq83Lg2JfOZAgipM5Hfpz_ei-iMrPP02KbLz1UfrW-uIqQwJ68M8ZExrqxvLmHB9EP0b7Wiq19IeuofI66Qxx8JLRCKSzQ7riI0iGDnKlGpljx7qnBBfH-R2K2xNGs95J5fgUf4T-fMdAqNTpwbTMpn_npQxsnwBsbkbfrS65djbJWWMfHzW0nS1S4s6Y-l3VP5TKK8h1H4MxDLV7GvxI1LAhSLjlU9r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e6c3b61f.mp4?token=GtoGdGd53CbOTXhLG_J-HRSyuHSHbuB28tMXYZ3JVKQz0Q0S9VD7ivSgfgq-oIyii0CaoaC_wlWxPoWTGRNHO986llhGkOyQ_ACmQHvZgrMA8Wq3qTb1Lq83Lg2JfOZAgipM5Hfpz_ei-iMrPP02KbLz1UfrW-uIqQwJ68M8ZExrqxvLmHB9EP0b7Wiq19IeuofI66Qxx8JLRCKSzQ7riI0iGDnKlGpljx7qnBBfH-R2K2xNGs95J5fgUf4T-fMdAqNTpwbTMpn_npQxsnwBsbkbfrS65djbJWWMfHzW0nS1S4s6Y-l3VP5TKK8h1H4MxDLV7GvxI1LAhSLjlU9r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451752" target="_blank">📅 00:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
ترامپ تهدیدهایش را دوباره تکرار کرد
🔹
رئیس‌جمهور آمریکا: ما ۱۰۰ درصد به سایت هسته‌ای جدید ایران حمله خواهیم کرد.
🔹
آن‌ها دارند تلاش می‌کنند یک سایت دیگر را بازسازی کنند. ما به همان سایت ضربه خواهیم زد.
🔹
هر سایتی که حتی فکر برنامه‌های هسته‌ای در آن به سرشان…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451751" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c48ca5530.mp4?token=P0esqZm26lgoQtXUBLhndWyXitDh1IBa2tDZSxtxG0lcp_ilRH-qVaaI-wtlCoSj70nJwCFpcAs9GGCTHXZS9QCAM4r6NFv-o1ZAF-58_hy_xRcY-hjrOBcFi3xxhn-0329K29S0bnpkOms4k_Lgp23GnSnC88fY6D8SdRdCY4LIB7YqzH_FC2Wov7grI153RF6wkUEu47N6PXKv9_gkJpdLV5iQceukkxlrGdHEyuomv0MGwuixdHlK-3wsdsK8tpagPktbVqTd__Qf1QsU3a6snuEqlgPYOpH48TcX4ZfPGTQMZ_Pjfenp-L9Wn3-SuCTCdrfF925HQKqvAGCZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c48ca5530.mp4?token=P0esqZm26lgoQtXUBLhndWyXitDh1IBa2tDZSxtxG0lcp_ilRH-qVaaI-wtlCoSj70nJwCFpcAs9GGCTHXZS9QCAM4r6NFv-o1ZAF-58_hy_xRcY-hjrOBcFi3xxhn-0329K29S0bnpkOms4k_Lgp23GnSnC88fY6D8SdRdCY4LIB7YqzH_FC2Wov7grI153RF6wkUEu47N6PXKv9_gkJpdLV5iQceukkxlrGdHEyuomv0MGwuixdHlK-3wsdsK8tpagPktbVqTd__Qf1QsU3a6snuEqlgPYOpH48TcX4ZfPGTQMZ_Pjfenp-L9Wn3-SuCTCdrfF925HQKqvAGCZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر جنگ آمریکا: جنگ با ایران تاکنون ۳۷.۵ میلیارد دلار برای ما هزینه داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451750" target="_blank">📅 00:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=oJgf2Ybfr8-3T6CqrFzxmdOrDuDe4EwJD3fQf8EffUUcnVFAgoCZbBWaGHSBaQcaWgMSAFbDH5lL7Vl8gqH7XkV7j1t1d_Arp9L-j4Qrud-qhM_8VgsC_tWo57TT-1qhkUNkeTfVwetlCNDsNzKNtaxJyXsk5yAvNJ47D_ZtmI2pAs8XLq6axbxVnpubpa2ZBxiQu4PG72YnzuoY3HGmSziRPEfqJqVUpJ2N-EzAJ9jyUMXRzMPeO81cF2RdKwEzK95buean50wjoTdFLKWjVXxC-7hIFmiepGL3HLhjYaJO8zxEPEwsZItYks67h4-EKOU0kbulboKpRh7EoIz0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=oJgf2Ybfr8-3T6CqrFzxmdOrDuDe4EwJD3fQf8EffUUcnVFAgoCZbBWaGHSBaQcaWgMSAFbDH5lL7Vl8gqH7XkV7j1t1d_Arp9L-j4Qrud-qhM_8VgsC_tWo57TT-1qhkUNkeTfVwetlCNDsNzKNtaxJyXsk5yAvNJ47D_ZtmI2pAs8XLq6axbxVnpubpa2ZBxiQu4PG72YnzuoY3HGmSziRPEfqJqVUpJ2N-EzAJ9jyUMXRzMPeO81cF2RdKwEzK95buean50wjoTdFLKWjVXxC-7hIFmiepGL3HLhjYaJO8zxEPEwsZItYks67h4-EKOU0kbulboKpRh7EoIz0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی وزیر جنگ ترامپ را به چالش کشید
🔸
پتی موری: شما ۳ ماه پیش گفتید برنامهٔ موشکی ایرانی‌ها به معنای واقعی کلمه نابود شده، پرتابگرها، تأسیسات تولیدی و ذخایر موجود منهدم و تضعیف شده و تقریباً کاملاً بی‌اثر شده‌اند. آقای وزیر، ایران طی یک هفته گذشته…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451749" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=FVserwFM_INzC0_LLUCiXIdTIUtdoHY-oe4xLBqhsUw-GaHhdulLE_wRjk0mT9DTSaO-2HdXw6qekNmjwLN_kEJ1rQvT5W5j9gnp_U2Ag7hsop4dZaMKhJQIhGoipHlEEJUUiIpbi2i23mSWLnLhO-BPp6QE5W-XPi4cSvCUOGShdcgxPDbJQphVlX8EBGNwW8vKOHCvZ2XpJ0W10NnMhEFFVCSzzgs43nbctzCBdqTevPbdPKuZwUreLqV_kSyQe3RRKlT4Ch_zv2neEpXPkofELsZBjMklf_TWdIoWdEc1RO9Ak4K0uCB2K5EBt_J3kG0XCCFBIx9E8PDP1_SIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=FVserwFM_INzC0_LLUCiXIdTIUtdoHY-oe4xLBqhsUw-GaHhdulLE_wRjk0mT9DTSaO-2HdXw6qekNmjwLN_kEJ1rQvT5W5j9gnp_U2Ag7hsop4dZaMKhJQIhGoipHlEEJUUiIpbi2i23mSWLnLhO-BPp6QE5W-XPi4cSvCUOGShdcgxPDbJQphVlX8EBGNwW8vKOHCvZ2XpJ0W10NnMhEFFVCSzzgs43nbctzCBdqTevPbdPKuZwUreLqV_kSyQe3RRKlT4Ch_zv2neEpXPkofELsZBjMklf_TWdIoWdEc1RO9Ak4K0uCB2K5EBt_J3kG0XCCFBIx9E8PDP1_SIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: آیا توانایی نابودکردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بخش زیادی از توانمندی‌های ارتش آمریکا طبقه‌بندی‌شده و محرمانه است.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451748" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVNDI8d-NvaD70Zex7YA-9XBL9Qo0TzrLjj5-Df6RLlDhNSu7y4lTs8DOi1iNFKpH-YQEryfkBPdV3240MlHODeIREUnaBd6IYAHSIuRGa799_708-j77XCHAPfGPmNMzuEaBmo_s2lVKSZ-pZTgA8alyJVuQ9fmsWYk_Z9ewfwEnwPSwtRkoxg--ogZLYOaSSEO-yp_aHeSDD4t3HgfKEB1X7VRsDJPh4hDYN7zJ6LvEXT9n9uv1vtclxYu0XzP5TVz_H8jggZKHrlphvrdSX7czt0WoGpJ-aj1nb4JI3jl2LMLUy6Fn4GZs1T9IvpDOEnU0HbK2JFCnPnuzeL3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش جدید ترامپ برای توجیه تلفات آمریکا در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال، تلفات آمریکا و مدت زمان جنگ علیه ایران را با جنگ‌های قبلی این کشور مقایسه کرد.
🔹
وی در این باره نوشت:
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
جنگ ونزوئلا: ۱ روز، ۰ کشته.
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته
🔸
ترامپ در حالی این آمار را مطرح کرده که در روزهای اول تجاوز نظامی مدعی بود که جنگ با ایران در عرض چند هفته پایان می‌یابد، اما اکنون بیش از چهار ماه از درگیری‌ها گذشته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451747" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5683a4e5b1.mp4?token=A_fPw-JrK8xkFyhPtT5cIvoPjcCKXeO6WW-dSHRuVuQOMfMJBiXuDUqeq4vkGjzm0aewLy0_B9hAJUrU3B93LaSTB6jf-knzJwZ0WfdudBTdqFftuIEeeYRA3f7EPdPOUWJjaJ-y-sbGuUtTorRLaQUX425x0T0SbaPNQakDV5HqNnNTQVTn1QwdPwuJjh7Dw6b-L_Wqc1n9WQeNK0iLfakiVPZD8Or1_tux9ZVTOLtPy6ESniQWG0WAKI8S7Nv9ZDNRz-Ehw5BDKlpRAxt7PTINr-96TEiusd55MyI44YlUVA5WOd_D5NM7qXMC3UIjUPURy8H_FNoP5hWmM6GT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5683a4e5b1.mp4?token=A_fPw-JrK8xkFyhPtT5cIvoPjcCKXeO6WW-dSHRuVuQOMfMJBiXuDUqeq4vkGjzm0aewLy0_B9hAJUrU3B93LaSTB6jf-knzJwZ0WfdudBTdqFftuIEeeYRA3f7EPdPOUWJjaJ-y-sbGuUtTorRLaQUX425x0T0SbaPNQakDV5HqNnNTQVTn1QwdPwuJjh7Dw6b-L_Wqc1n9WQeNK0iLfakiVPZD8Or1_tux9ZVTOLtPy6ESniQWG0WAKI8S7Nv9ZDNRz-Ehw5BDKlpRAxt7PTINr-96TEiusd55MyI44YlUVA5WOd_D5NM7qXMC3UIjUPURy8H_FNoP5hWmM6GT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدجنگ در جریان جلسهٔ استماع سنا، سخنان وزیر جنگ آمریکا را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451746" target="_blank">📅 23:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451744">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ab2fe524.mp4?token=bPAtt8cz3TelyALYwX1yEgMLrkZxbvLsuJGZhCThGS2pZz41M50KXZcF48v_x3TplcpElf5YqqkK4pF8Vg49PmjJkwD5aCw7BzcJ4MIC5wFokPKoTa2U54ihS5e6k1SzeWYf72TBlDZv_uZrpyx32SA-cq0TJEBbjdtFLd-Fhw7OqqbxyFSgSTcajW_ehJ-P-mLv1KDf062YiJI3-JBTT5Eh7qz-Eur6-nZfl4jR4f3MBF-1QmUSKiZJ1sJYJGQpnBYrJ7jfOu4MGNjpuJOF_MeMGu_eQR_Df0NRkuMXh6H3QK0r1etpMLetWVMlvWZ0q0l0oZuSXkwRKQtp9x6_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ab2fe524.mp4?token=bPAtt8cz3TelyALYwX1yEgMLrkZxbvLsuJGZhCThGS2pZz41M50KXZcF48v_x3TplcpElf5YqqkK4pF8Vg49PmjJkwD5aCw7BzcJ4MIC5wFokPKoTa2U54ihS5e6k1SzeWYf72TBlDZv_uZrpyx32SA-cq0TJEBbjdtFLd-Fhw7OqqbxyFSgSTcajW_ehJ-P-mLv1KDf062YiJI3-JBTT5Eh7qz-Eur6-nZfl4jR4f3MBF-1QmUSKiZJ1sJYJGQpnBYrJ7jfOu4MGNjpuJOF_MeMGu_eQR_Df0NRkuMXh6H3QK0r1etpMLetWVMlvWZ0q0l0oZuSXkwRKQtp9x6_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدجنگ در جریان جلسهٔ استماع سنا، سخنان وزیر جنگ آمریکا را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید
.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451744" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451743">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF-A1awx63txHLN5S06GOKkxOIH541rtYUwyuldIvXKI_vj6YX7WXmP5IYnDPNrPxtT_w5nDLG4nSARSw0aWQQDD73eNGir-lEzUztpfk3CTTGjd52a-ea42BuJ73iETcV3-HKUqRrg7J1xpbaRe3OUNvO_SSiXs2-HOtPBH6WP1EkI-gOrDmQ-XOfqokvQNHMqHW02G4Tl675trpw88zi6HY_lGoJi7ajmdJ_CczMbeqNmUkb53kVgyu3YlE6YsNvAMhJOXSDAgTGP0Ne-x___wZ85M3aUfvd9c4BUMKMUZPnJvKfV4iIh0NTWyZdlujmZ3kS1_tmHV7TRPplfXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: محاسبات غلط، دشمن را به بیراهه برد
🔹
اسماعیل کوثری : مبنای اطلاعاتی دشمنان غلط بود، آن‌ها تصور می‌کردند که می‌توانند در عرض چند روز کار نظام را تمام کنند اما همین اطلاعات نادرست باعث شده است که آن‌ها اکنون در گردابی گرفتار شوند که حقیقتاً راه برون‌رفتی برای آن نمی‌یابند.
🔹
اکنون کارشناسان نظامی و سیاسی آمریکا به‌طور مستمر و علنی اذعان می‌کنند که ترامپ، با آغاز این جنگ مرتکب بزرگ‌ترین اشتباه خود شده است. بی‌تردید اطلاعات غلط، چه در حوزه نظامی و چه در سایر موضوعات، همگان را به بیراهه می‌کشاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451743" target="_blank">📅 23:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451742">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6f3ba24d.mp4?token=s-Bd39YYNctyjFc6uIlbpV9s2FwjSv59RgvGqfdOslk-BPtuEqM4vjaNJE_yujdb9ao3yPC24MrvSRt8Z7EaBuwTPSlNWeRP-Jp5-4VjNl6czIpHJBqkvHE6KTgpZq01usq7Ubt-hAGC74g4M4AYWuTd3mFVsSnbqxC-S-GNg-7TEzz2PraJ4nse_6Wc05AJG-q_PWV1MAPdmXbASqB1pRi1ww_FIKKls28Um_BFmvu_CHsJuHnTHEnDLuX1gEFQFRdQeTcHVcuAuM-OEdSypmOENOMQAZptWsCXjcvmXcTqrNSKJxrQOdH6rq3Kj7ZQizQls1vSOKlQigUxIL-SkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6f3ba24d.mp4?token=s-Bd39YYNctyjFc6uIlbpV9s2FwjSv59RgvGqfdOslk-BPtuEqM4vjaNJE_yujdb9ao3yPC24MrvSRt8Z7EaBuwTPSlNWeRP-Jp5-4VjNl6czIpHJBqkvHE6KTgpZq01usq7Ubt-hAGC74g4M4AYWuTd3mFVsSnbqxC-S-GNg-7TEzz2PraJ4nse_6Wc05AJG-q_PWV1MAPdmXbASqB1pRi1ww_FIKKls28Um_BFmvu_CHsJuHnTHEnDLuX1gEFQFRdQeTcHVcuAuM-OEdSypmOENOMQAZptWsCXjcvmXcTqrNSKJxrQOdH6rq3Kj7ZQizQls1vSOKlQigUxIL-SkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع پرشور بروجردی‌ها در حماسهٔ ۱۴۳ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451742" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451741">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323a6a4a89.mp4?token=IgZiSa9l6hSMMtp9oUIcu6UWbVyprcgWcJPbWsER_2ZttaXCjIWTNAtBlBRSRDT4xbf6dd6ow49KYNK3RORdG4EikeAAxXT_G4FPHdv2gJsgL3FqjKdn0MK5T1cU5m7YDrheOLM6Ie1kR3h05QUQfKaJR2ngzmRnnX5TeBUAXjnUGjehiPJLBqte55yogbxj4Os_J-bCVQWuviH3jF0PVR6Msjzye_WON5Jt-nW8wshXeXHxmwFZEhLiLh4ufhOgDVrkoYeT2sU5oBr0MwU23BFsllxI5XD6-GHOVOKXr4AYpOE_Oej7SNUo54tfN2-SSNNYhd417joDZPRzDXObQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323a6a4a89.mp4?token=IgZiSa9l6hSMMtp9oUIcu6UWbVyprcgWcJPbWsER_2ZttaXCjIWTNAtBlBRSRDT4xbf6dd6ow49KYNK3RORdG4EikeAAxXT_G4FPHdv2gJsgL3FqjKdn0MK5T1cU5m7YDrheOLM6Ie1kR3h05QUQfKaJR2ngzmRnnX5TeBUAXjnUGjehiPJLBqte55yogbxj4Os_J-bCVQWuviH3jF0PVR6Msjzye_WON5Jt-nW8wshXeXHxmwFZEhLiLh4ufhOgDVrkoYeT2sU5oBr0MwU23BFsllxI5XD6-GHOVOKXr4AYpOE_Oej7SNUo54tfN2-SSNNYhd417joDZPRzDXObQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات بانوی ۴۰ ساله از عمق ۱۵ متری چاه فاضلاب در کاشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451741" target="_blank">📅 23:31 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
