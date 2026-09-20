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
<img src="https://cdn4.telesco.pe/file/Dg0WRgoEdKlhP7PkANmk30b2tUpDP2uTWXcP_2g0PQTAYNGRLZ7wxRcxfFbDvfL1GQKUek1aiZLQ5k0KGbIZEt6qHlKI7LMcIQBpHpQQc33iAykfZdNp_RbMrFsK8bDl7zaxL00WKL1Zn0DWsZKxfIjvq3uddGLuQu34st6Ht89nbr8_HRYSR5cexZ0ysWLKSXxR8XjqF62fPMobkncO3UbPIjStevrr2E3c6DJrarmNqfVPMC8dcQjjvWMK_3td4_rNaadVH5_rzqctO5bIz8PAoBqU9JvcSDfDoDk7VqjqIwvXIAxZpF60KdXmKKOCtk2bGMXo3qxiDWne47L4Wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=UR34cLh5fPhQzzifOsqwpXF8OVGuFIXaH2Q5fg18a6sfVDdPFYcrZnyLfq0FYQtOhatA6UN2I3K7z0UPexCKmd4svkwdYFIxCKljl5hfovPPQDGr9gbSIMEuj0fwS-GHaYkUyXvZ0dcUu05brnPRQEuJDXQrQhdmnYkyf7vvg9lL6-1fbSTG5v90xce2DqGQlMuPRCdkQPSGVWRE2nkp2EuwvOafrXK6VsGEBIIf3DVfAsfu2aotaih2MYoVyeHzYI3QeRyBEhlbgh73bYC7U4gdmGEDXIq7kuUOPSr0PthA-wVitkNlvmSi_o_aLP-Dn8PzdWI6deYCVvmFBCWZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=UR34cLh5fPhQzzifOsqwpXF8OVGuFIXaH2Q5fg18a6sfVDdPFYcrZnyLfq0FYQtOhatA6UN2I3K7z0UPexCKmd4svkwdYFIxCKljl5hfovPPQDGr9gbSIMEuj0fwS-GHaYkUyXvZ0dcUu05brnPRQEuJDXQrQhdmnYkyf7vvg9lL6-1fbSTG5v90xce2DqGQlMuPRCdkQPSGVWRE2nkp2EuwvOafrXK6VsGEBIIf3DVfAsfu2aotaih2MYoVyeHzYI3QeRyBEhlbgh73bYC7U4gdmGEDXIq7kuUOPSr0PthA-wVitkNlvmSi_o_aLP-Dn8PzdWI6deYCVvmFBCWZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=q9EAhju6S9tgzvOZzpGBkpd47n7RkmfqzDFw2VG4TNDibteHpO6EqVveITLsfGpyYsxMBdAn2VzgR5IIBSzjlhWOB_L0WtRjfjJetK-znPbR6p9uiM1haKDmrkqNK6Xq5zXRjEfup2gwA-iPDsCZmEAwyNcgxmkHq0Q__iOYxBNq1DS_jOkbLe8s403ix5vURaxWEROVpi6MHdPgYY2KlppmUND0bPRpWslCDQhYVcEBTyHxdt1JtBikJdG7XIyaYpP-ProMRlUEsLt0W516ABtjiZbbI5LXH7KJtM-Ir8K21Tu6h-EIw05Wkj3fmbRfNucuotgR8FxKBw454OgF2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=q9EAhju6S9tgzvOZzpGBkpd47n7RkmfqzDFw2VG4TNDibteHpO6EqVveITLsfGpyYsxMBdAn2VzgR5IIBSzjlhWOB_L0WtRjfjJetK-znPbR6p9uiM1haKDmrkqNK6Xq5zXRjEfup2gwA-iPDsCZmEAwyNcgxmkHq0Q__iOYxBNq1DS_jOkbLe8s403ix5vURaxWEROVpi6MHdPgYY2KlppmUND0bPRpWslCDQhYVcEBTyHxdt1JtBikJdG7XIyaYpP-ProMRlUEsLt0W516ABtjiZbbI5LXH7KJtM-Ir8K21Tu6h-EIw05Wkj3fmbRfNucuotgR8FxKBw454OgF2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=HlZJhOgV2p3_azktj0Kg4RrMOSqPLaKOox8QrMzAPOq6BwZfkx3l1jFHAbGG2OHP7SIfBUJl4kHU2QEp75JFkbcG6nrTPITTSYW9l1KEoVXx_Qs_LUkurnYPhbMO352tKz4KQKGeJYWbz2Ms9T2Xoe2d8sZb6uj_daHs601lwE4LvTl4Su-TxKBZD_jQdVAJuwDVI_s6vK9aCi535JqWiDqnECuTithoQ6zd7KDYmNs26Mtr7G81Duocv8Yx6DQT26EnXoPCwTPJY2KDl1CUUCeOrN_aCJkKi7J_mR-QL5sv1OdmdQfkVcS_L17IUMRUhrHXvYwB6vvhabARQOj6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=HlZJhOgV2p3_azktj0Kg4RrMOSqPLaKOox8QrMzAPOq6BwZfkx3l1jFHAbGG2OHP7SIfBUJl4kHU2QEp75JFkbcG6nrTPITTSYW9l1KEoVXx_Qs_LUkurnYPhbMO352tKz4KQKGeJYWbz2Ms9T2Xoe2d8sZb6uj_daHs601lwE4LvTl4Su-TxKBZD_jQdVAJuwDVI_s6vK9aCi535JqWiDqnECuTithoQ6zd7KDYmNs26Mtr7G81Duocv8Yx6DQT26EnXoPCwTPJY2KDl1CUUCeOrN_aCJkKi7J_mR-QL5sv1OdmdQfkVcS_L17IUMRUhrHXvYwB6vvhabARQOj6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=pEhlVpXSbVTg1JkVsyY3CVPLdwsuBiCLgFBt_aJIYyof397eaAkLdwZpSo30MWC6zBek83luRREwINUSAMfipOxbQe23CVRZYk2m8JNWZk70f-OhtdwbBQvTVfyvRnLnv0yUZDd3Et-sLmVg7DqzbU3qeU7vDmm-Oafljb44SdXJR1TVVlMCXfPQ70ENH0450KvbbgOhdORaI4II0MvhrVzxfCCyMEmCbs-D5qfGfz9Y_MU-xCLhDSWC0j69gnY6PxHqaHX9oMd0ZeyaXX-KoV_ICjTyEcQKCSSdiVCBoXZvaDgRGtzHpdo0n_VAA-_9hZkFBMmC37_cU6qC1ho7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=pEhlVpXSbVTg1JkVsyY3CVPLdwsuBiCLgFBt_aJIYyof397eaAkLdwZpSo30MWC6zBek83luRREwINUSAMfipOxbQe23CVRZYk2m8JNWZk70f-OhtdwbBQvTVfyvRnLnv0yUZDd3Et-sLmVg7DqzbU3qeU7vDmm-Oafljb44SdXJR1TVVlMCXfPQ70ENH0450KvbbgOhdORaI4II0MvhrVzxfCCyMEmCbs-D5qfGfz9Y_MU-xCLhDSWC0j69gnY6PxHqaHX9oMd0ZeyaXX-KoV_ICjTyEcQKCSSdiVCBoXZvaDgRGtzHpdo0n_VAA-_9hZkFBMmC37_cU6qC1ho7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfzL9uNCLslYMrKQUVoTcQLFlqfpMPCAYjzoDEluYpkKjBvm-dHqvjtBg4jJxF1oE1HebEuvFN57cc8oac4ebvsi90iN5-Zjjz4bOHcAzsDxJo9-EwbjLRVc7hP-ZBWD8ubUUqA6AUN_xUejoVSfbz3VGqOXIJ5Nn5Q-F506LL8GCpFM65cYz5dmT6EyE2EYL8-BrxvroSgp6sQDJZNUF-RtSIAcQtVHOBh5uEadRGMk6ZvlQlKvCHsVPd5glG_vvAlMY5v-62KwDPsuUTK-sW9eJMRw3bpy5qFY9o0d46e1iDPHsYBkn2os3zp3hEbHBh7POV_DO4m1aig-yEHR82po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfzL9uNCLslYMrKQUVoTcQLFlqfpMPCAYjzoDEluYpkKjBvm-dHqvjtBg4jJxF1oE1HebEuvFN57cc8oac4ebvsi90iN5-Zjjz4bOHcAzsDxJo9-EwbjLRVc7hP-ZBWD8ubUUqA6AUN_xUejoVSfbz3VGqOXIJ5Nn5Q-F506LL8GCpFM65cYz5dmT6EyE2EYL8-BrxvroSgp6sQDJZNUF-RtSIAcQtVHOBh5uEadRGMk6ZvlQlKvCHsVPd5glG_vvAlMY5v-62KwDPsuUTK-sW9eJMRw3bpy5qFY9o0d46e1iDPHsYBkn2os3zp3hEbHBh7POV_DO4m1aig-yEHR82po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=hkNHPXOlk3LPQQ59kG_mDXqmPcCNDV8CupP7VY8iYotVvilmUvbTSwCWd6e0kR-cFgMV-8VXAjCIToSJlHbzV6mgKOrcVdyTwTDbsLI44Vf6S97wuNz5pxaLeLOQ8rs1XWGelTUI8UE8RAVo3TnnbRqCXrZ4oRvL0_SuV_RrDlRXRaiUBUngxifBf7MVl2nyxVTNYpevgbQlFnzMYCs8QLHeVH6AdphNfIOV7Xo_r3aueRJcixfpWTFijTFqNq0X_hUW1FRsT5v5qvykLX6i3BJzHHkKFi4oOO6iFI4ybHmtt09O_6_KhiKTZm3Ez_y0DmOp-QglzYMBOFyDMyZ6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=hkNHPXOlk3LPQQ59kG_mDXqmPcCNDV8CupP7VY8iYotVvilmUvbTSwCWd6e0kR-cFgMV-8VXAjCIToSJlHbzV6mgKOrcVdyTwTDbsLI44Vf6S97wuNz5pxaLeLOQ8rs1XWGelTUI8UE8RAVo3TnnbRqCXrZ4oRvL0_SuV_RrDlRXRaiUBUngxifBf7MVl2nyxVTNYpevgbQlFnzMYCs8QLHeVH6AdphNfIOV7Xo_r3aueRJcixfpWTFijTFqNq0X_hUW1FRsT5v5qvykLX6i3BJzHHkKFi4oOO6iFI4ybHmtt09O_6_KhiKTZm3Ez_y0DmOp-QglzYMBOFyDMyZ6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pizIQmObhU7nYxqWlufZnyBZoA1TISjCXsMbbMEo-sUOYzJMiFB_K5zy1ydaIEcbHmu55WBNTWBbxOQmOxz1CkPhIYY1QAiDyYvydYEGAQKKcZ6XnXjLxi74Gl6F1iR3SJ0l5jEAq_hOJQSbcsElJ0MVk4Y-ePRiwSY-N7NRfBARqjbrMIDx_bQSkFWul8P8q4NoJxMpnbUbYY093_q5lUF9h7TbBgXteROVMbgQ0td0Wkvu9u8mjvuL55_U1JM3aUAx9f9dNsJLY5mC-gMDAEuuMr9TBIMl7dBMhlN68iN9t-qxTgHs_5CnWlqEjnRA7joBUt7IkK9Sh8BAoVWcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Cujnbmne1Qs_bq-J3uv-gkBM4QGnLNiYygnaCH5_AJNhE1MGfjDbypatFLqEF4kPN5bHWOJvzlNbYhXtv0k3fQWESbWi-wSU3tNWnW3DXUjiCz0VHQUh-juUvK1OP-33PkXte37f9Nv9KImnadoYHXfj1kc_FqrmjFbfgbuJ2ALEK1kYMtcOWmErRrJKxzhIvE3LFoGY841HfZLIRh_PvDNaX4w2iYGu_3tm4mUnZHMDIHqczVQ0_XH86FhDcWUsOz9pqeCLOvMk4h8w-IETNLPxUuotsQXOBh2l3R_gtiNgGPCOBKRWAtZg9aB1DDDZMeKvYXkTiOGQtmv8II5W3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Cujnbmne1Qs_bq-J3uv-gkBM4QGnLNiYygnaCH5_AJNhE1MGfjDbypatFLqEF4kPN5bHWOJvzlNbYhXtv0k3fQWESbWi-wSU3tNWnW3DXUjiCz0VHQUh-juUvK1OP-33PkXte37f9Nv9KImnadoYHXfj1kc_FqrmjFbfgbuJ2ALEK1kYMtcOWmErRrJKxzhIvE3LFoGY841HfZLIRh_PvDNaX4w2iYGu_3tm4mUnZHMDIHqczVQ0_XH86FhDcWUsOz9pqeCLOvMk4h8w-IETNLPxUuotsQXOBh2l3R_gtiNgGPCOBKRWAtZg9aB1DDDZMeKvYXkTiOGQtmv8II5W3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=BgCPM-1O4cn46pN8V_Ap8QlQut-MgpJQM_qWSEYyRo73A3kiJNCu1QBvpj1kyy6w6lv-wPhYXvgI-mA43Nj4VGG5OmBpNb7WjL33D4csT2HCLozMQZzhbykgaur4_klxFGLmWGneRkXVuO5XS7f1QgU0DFIXjfDBJ7H4PJHL6OMI5IvElMU_IvfZciKXWfIuk0bND0ow3fpYW7TgrjYbQEGV7vXj66JR7dZhgpJPHxId8rG9-_17IUNUxnpQ-X3O4t3D15XJEomH2LRBDU9k8VXoRlfiv7silti9ll9Hh8LFae8v9c3JGuf3Tt8EH3pbogCrVmuaC2tTwMVzVq2r4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=BgCPM-1O4cn46pN8V_Ap8QlQut-MgpJQM_qWSEYyRo73A3kiJNCu1QBvpj1kyy6w6lv-wPhYXvgI-mA43Nj4VGG5OmBpNb7WjL33D4csT2HCLozMQZzhbykgaur4_klxFGLmWGneRkXVuO5XS7f1QgU0DFIXjfDBJ7H4PJHL6OMI5IvElMU_IvfZciKXWfIuk0bND0ow3fpYW7TgrjYbQEGV7vXj66JR7dZhgpJPHxId8rG9-_17IUNUxnpQ-X3O4t3D15XJEomH2LRBDU9k8VXoRlfiv7silti9ll9Hh8LFae8v9c3JGuf3Tt8EH3pbogCrVmuaC2tTwMVzVq2r4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=X6Z38fa8agehO0QIrzojxQVNSw49Cw2fg4i3wC1jZXm4HyJqzPWOl7FZ4whYYjPxHVhtUvg17eZD3c4IQiXsKflkpsPrezyPyLoTt1xzjM5X0BYGyxR7oyvzKH-Hrv8FHiOvsJGC4cz-khbAhIXQmAHNuIqXdKdqDngSXNBbJlX9u4WOOWtyV__7-miMQDroh8qUkJiTuaRUhrd7r8KrlR2cJQ5t6Nyn9vQuYUrwjlLaa9H7ALw-Hba5fVY-oSoADbSnWXmsUfXm-AQiBKO_p5Eq-irpaqBF30A0bJ_x3alHjv6_heiVmazvPHZSAa-SGeZnUxftAhyoZ0r7tKN1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=X6Z38fa8agehO0QIrzojxQVNSw49Cw2fg4i3wC1jZXm4HyJqzPWOl7FZ4whYYjPxHVhtUvg17eZD3c4IQiXsKflkpsPrezyPyLoTt1xzjM5X0BYGyxR7oyvzKH-Hrv8FHiOvsJGC4cz-khbAhIXQmAHNuIqXdKdqDngSXNBbJlX9u4WOOWtyV__7-miMQDroh8qUkJiTuaRUhrd7r8KrlR2cJQ5t6Nyn9vQuYUrwjlLaa9H7ALw-Hba5fVY-oSoADbSnWXmsUfXm-AQiBKO_p5Eq-irpaqBF30A0bJ_x3alHjv6_heiVmazvPHZSAa-SGeZnUxftAhyoZ0r7tKN1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=j5I6Jk6ageTpaN180cHWMNoNRtGbhrKutgvjmCTcimrWtaMAAy4JPx5I2YCiEXQQt_bn1Xkc6ps8KIcwV94tdQRlPu-8Ygx1zcY6KHQmZhBlAIaN1FKYijcKI7fgQp7rFfx-35JeswSP2OSm2_KW4c8OyZCIOzSioxM8vu08j8AYkFT9b_xhGeBZTgTPESihpJTq-CE6l1KJesYxL6rIi-J6OVEWLdjppGgBUEEwl0vSIMnaiqMKyd7ZMdzIB1GtbS-EZK2InunHzgtWeTQT_nJHxiGQrIobtcbl33AeN3GDEb0-WOxRU_JrpD0DiRcgGfjEWE_-27sQqbc8LXLEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=j5I6Jk6ageTpaN180cHWMNoNRtGbhrKutgvjmCTcimrWtaMAAy4JPx5I2YCiEXQQt_bn1Xkc6ps8KIcwV94tdQRlPu-8Ygx1zcY6KHQmZhBlAIaN1FKYijcKI7fgQp7rFfx-35JeswSP2OSm2_KW4c8OyZCIOzSioxM8vu08j8AYkFT9b_xhGeBZTgTPESihpJTq-CE6l1KJesYxL6rIi-J6OVEWLdjppGgBUEEwl0vSIMnaiqMKyd7ZMdzIB1GtbS-EZK2InunHzgtWeTQT_nJHxiGQrIobtcbl33AeN3GDEb0-WOxRU_JrpD0DiRcgGfjEWE_-27sQqbc8LXLEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=k1UZwAOPtuRiJ1VrHnZbM6ADR0Ly280YcJMPIrDH0QLGnf4ADVXTLDl1ZpgQ9vsat1JiC7t8sMH8PnOwLpZyFbzJ8B2BdPHCWazTW1b6y2g92l3rOQ33tjLWgf0oT4N2MijPmX5NWQwxMktc4GYSul9t3NVf_VSugdNXTF_2MlGEYzBTyomLyoNnPubeYGxXc8c6sPuL8Rdu3ZrJIQMkXzate2C2yxJZa4ul4upTHxzOV6UsYS7a1v0IYeeDV7Xz_6489Wyfye1WLrfjnyj4sTP7R7bBSEfKARm3ZTDFy-LpZM0nJAck9WEyi7c6vCnYr36OIZu49OoXiXGhY2hkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=k1UZwAOPtuRiJ1VrHnZbM6ADR0Ly280YcJMPIrDH0QLGnf4ADVXTLDl1ZpgQ9vsat1JiC7t8sMH8PnOwLpZyFbzJ8B2BdPHCWazTW1b6y2g92l3rOQ33tjLWgf0oT4N2MijPmX5NWQwxMktc4GYSul9t3NVf_VSugdNXTF_2MlGEYzBTyomLyoNnPubeYGxXc8c6sPuL8Rdu3ZrJIQMkXzate2C2yxJZa4ul4upTHxzOV6UsYS7a1v0IYeeDV7Xz_6489Wyfye1WLrfjnyj4sTP7R7bBSEfKARm3ZTDFy-LpZM0nJAck9WEyi7c6vCnYr36OIZu49OoXiXGhY2hkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btyb_i51yzMI91wGGzc7CbxpCX8Zk5it3OmY2HKC4NlKx6SAgSWEKecJV97mkZiFIj7SmvW8a8dCPUJvLDKPZtbbcw-McPCoDMXnYtOsYY3Ea7MFBtKT8Jh4sCc-0E58x0K-7fEqrNTOiRtfNWLgV1kAm2XK6TuQeWw1oANbFbFpOpx1TLtz0t_An0NkbAL4Uu4dWSyHrpXscdCotwsVwJeLoHONwFZVrWGt3b_YHtJRYcUZSZZY4j0brBri3gWJhSpM9EzHlKpdU_H1xhV2MimqimBCXTFgBupHJpfNfZgCFlx9lClmA1JPSOhk0qXgaQ8Rjm4neabNUTlhqhG22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkgZ9RWaonZx2dGy_ks25dQ-S41q2j3q2vjuvB7P3YbtanupyvPRKUD8PYch7SOVtrkoASn5mEMa3a6pyycQqOxbpoRbmQf7Gwr47cmFXKC3zkEmynfJTwySlSYLE9yHdZuB9-5BcYRWmOFrduVgwLuC9FT4qfRUShTaRwaPag5SC2rAhpOevdvBSFOmc7AxSdAkux55hc9PgYxu9V7O1oIj7zP4QqNPtxa3YYvBVOUHFu4HGyQAr-WnIyXPs92kQsaldzwxb8_eM6qXH6yhWWD6h0Fok1D9Q6R1S0WgQLWPW60O06bIhlxyO8bdAA84BVJrnaANbUUH-llwHxcUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uRxC05GfOwnxHUR5bcqEYl5m9k2APTweOub0XJdDb3zP24iW48tzf3AJinCYdMXKp_MFd_eHtQby-ZvhK-w150Zkqmsy9C34Ippcv88epjflvh_geL68RNwtgJgo8KmAeGpDz5T6DtU5VbTJp894uW6ONyuE-Cop4LkfXg97-r04ZnJxE3X8ah4s26K57EePne8GaLf0DYC3BPb_p0Qm3qJWahUcZlsDfbZNJzHZk1gEX1CFADVNlopdtxXVnsTYizOBR-9dfWwmYe1B_ZBFdEAnk6FvxRhk8kPvTpejUaIOAmDBcP3w4rKbG3_aOTTj8k4GpppJ-4s2RMHu7-dyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Lqb8z38SkhdXEk6Oy2v7vINpJb4GUmO5t2hSmLIlXaXSW4vQiuhpczJhTVXkyKrH_N8IB-5voSr9TzlQhw5ziMmX-lYxTWqkR2lF6EKKVrmo7iOf-J7PLZbEhBIq_QpHslrtrYccgNxAkyBX5oHY_mS44yd9VrDvbcUwv8Dnu4AE9iqkXdA4rRP8M2uKcFwV3ozDOYswKRjC9AKgw6GyYvU7AIwyszI-XFQowCXgNW1Bb0zBwY1igXUvYCYJcVLwwMruJXoXVJajDXel-3r6OA2Pzhf9V4ZAEfretMaSex1iR5BnxQtoo0syNyj9gHGUXXBPTs4hfR7iteyFMKn_rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Lqb8z38SkhdXEk6Oy2v7vINpJb4GUmO5t2hSmLIlXaXSW4vQiuhpczJhTVXkyKrH_N8IB-5voSr9TzlQhw5ziMmX-lYxTWqkR2lF6EKKVrmo7iOf-J7PLZbEhBIq_QpHslrtrYccgNxAkyBX5oHY_mS44yd9VrDvbcUwv8Dnu4AE9iqkXdA4rRP8M2uKcFwV3ozDOYswKRjC9AKgw6GyYvU7AIwyszI-XFQowCXgNW1Bb0zBwY1igXUvYCYJcVLwwMruJXoXVJajDXel-3r6OA2Pzhf9V4ZAEfretMaSex1iR5BnxQtoo0syNyj9gHGUXXBPTs4hfR7iteyFMKn_rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7zAwpgw9kSYdA2ya8azjYfaPZTF_583E7dLI5dxnPYq1AR82Zi1oI7OWQDvYOcpq6A-FjFRNf5HYCE5jjHfFyi5C_vdHWscWmNeV0_oxg6T6pqiS7FbRH-IIVt_6zpseSdJHPPX3hPvoA5sm73fyr6JjJDSNRhbDWUOIl1oY1z_YekzgkBJsdmi0iMeTTS3i59XnVaQRdgKqlJKIvd1MBAV4jMhm5Wya8HgWTA2EMe-y-GItSig77RXdQCUENHp3N1mrDjLH1TpEwMxvYg6B_kOF-3CHq0loLNr_p8lF0GtzecJ0LKxGd66eXE69ctgqZUpAopkeQGUATqiNL5A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=ZDHSjNN6tckvK-pD4vjbt1UVOn587G9vEKkEOYY22kMfYp2eSTh1fDOr11nf4UmPx5GfQPWIMhO3jZQtQC4awUshrza8NDtOM2cqkwFNBZkEe9V8O6h54HKajoVndAuu7Or0tvCdpqdWO_jiFQhmIeKy5hjTMiB5_aJTEXlkUBzyhlrBBGQX0ve_BRu3bFsH53TvIO7jcFH1N9zUdmkixJyS2uhsUf7RJO23IW2P6Hoeqc09p5KRv18xI9uwp6gL7v4pKirr_l64BrnrgoUQ8byDlTa9RiVmq9cr8LHA3Th11zeHg7sMMOS9Iat8duuK1OUmhaqVcwq_AolCTYxrkWpIkCdVbcYmZfjAoUDOQsCixcOBvu7TomMeOeEUhmHYfi9CLWSXBc4m_WlTaHGxBZOse4pSAOjfiCBY7e0wdxSaBNXrwpr4afU53gZOeIMfRXd2LP1lMb870nLFUGuQBPO13oi2kAz4lnwDKMB9AVjopE7_UPZ_vdTADTjevGc3VlawWclaV_eE47CnQSw-aVhwXNm4Zi-Ww136mWMq1jJGb3XwTtUZAleJ-d6fYbc-bxsF0YKqapwozm6SzjqrWtQob4DyKEbfodxFiKcLHnXE2iXFSJh4kOe6l4xCHXAw6ZnV-VUJQQylx-Dcvo_Rwl5e4oxr6BrxKXEaQeOhqjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=ZDHSjNN6tckvK-pD4vjbt1UVOn587G9vEKkEOYY22kMfYp2eSTh1fDOr11nf4UmPx5GfQPWIMhO3jZQtQC4awUshrza8NDtOM2cqkwFNBZkEe9V8O6h54HKajoVndAuu7Or0tvCdpqdWO_jiFQhmIeKy5hjTMiB5_aJTEXlkUBzyhlrBBGQX0ve_BRu3bFsH53TvIO7jcFH1N9zUdmkixJyS2uhsUf7RJO23IW2P6Hoeqc09p5KRv18xI9uwp6gL7v4pKirr_l64BrnrgoUQ8byDlTa9RiVmq9cr8LHA3Th11zeHg7sMMOS9Iat8duuK1OUmhaqVcwq_AolCTYxrkWpIkCdVbcYmZfjAoUDOQsCixcOBvu7TomMeOeEUhmHYfi9CLWSXBc4m_WlTaHGxBZOse4pSAOjfiCBY7e0wdxSaBNXrwpr4afU53gZOeIMfRXd2LP1lMb870nLFUGuQBPO13oi2kAz4lnwDKMB9AVjopE7_UPZ_vdTADTjevGc3VlawWclaV_eE47CnQSw-aVhwXNm4Zi-Ww136mWMq1jJGb3XwTtUZAleJ-d6fYbc-bxsF0YKqapwozm6SzjqrWtQob4DyKEbfodxFiKcLHnXE2iXFSJh4kOe6l4xCHXAw6ZnV-VUJQQylx-Dcvo_Rwl5e4oxr6BrxKXEaQeOhqjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkQNzfFvMwqde7wgijebXV8K0YQRPktke61pbKm8UW8E8Rvo5nB3do89vfoOouaJqhxYNeK-PNwHbhDFgjr9WIrcj96TMbZuV79rL2sFxfgLL4ox97FfsrGepOu8YjytkRNrBtSh_NI4l8eN5EnpW_rpCRy0UismxFa3RfBdeT05bvACZydyBfsdOIhg3eGowVhrK8dXXn2ceSFxVGYEbRM48hLHZeExx5iDxRmX0tM3TI-N0rng3Ehk2u9cxuJDbbzV9tj1j_3cN69vuXl32D34h2w9eq_nzaJEvRzuMTpkTCjaSq-rcvft_6BKAZm0bm-AilGWDU6FLGQMtNw1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwxYkNYC01RcMSxldV2zYj065EoWc3tj6yd1AJJfOQb6Uk0WX7CN6vLTQPTcxHyuSoMD-UVixoYW_lwVP-PjhnlW5u-dr5psjoqmxkOKGEJ-CjG1PFGSAMNa77TftzSBsfAlwemOcrSmuoDDUu3L3UIjKAhnEJ-6OvwH2WtmPr1NploxULX8RkSMtMOp6QsxpZXYEHUDcyc1BvL5dOsAOLE6nK_jWqmYdGquRG-y0cHbZDw-FiOAMfvgsocacztYUETcMtXnO5Fma3ms4N0oFAoxoLhU3y3h8bIaUx1r1RGGHOgqxMb7m8nMyn0XGKCLb8Rs2b46G8BslyGJPpIVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=pqhpcC_LTztpb_esvXSEOMm7WQ1xXMf_ajFARtZPOHPR1zHfJtKws3mKSqOSF8c1fMtklgaIBk7F4h-BCFFKDEF62nn7Q4yCeumODs8ergPyg3sxdA6lLPqTZtay7m1REWZk-Q4CYWF83K09xQQlP855jLreUrit71UBTH4HDpu9IXlbn0uGKo09eEktwwvC_IBrPX4iCY8sSP0EOLK5ydEeQPHQpO135YPTTCbzbV6ZBF9hZqunQ5rbNq472SMguHq7gYaU79LplZkxM_JZ-JqiJYmftP27RfIt6mnyQfdUiGbm98pWsYHm4KbEwP5lWl1CnDN6uMn_UHVULVQPHIfdqXijhOjfYXiheMJ_IX1_YB2161Ageijk6102oIIvmybmkLnvqotjoQiK47yNfXhe9SuE4R19BQI1Xh7oSbStw2w-KIQtM_icCbSwxfRoVbv6-FTTFWJP97oVauDDGMYhW15m2Lyx7TRKIcYFSHZ4EkK3IPokpqEgLui1l5P8KLp2WF5whQrbySe2zzrZmSdh8WmQE_ZKpfrdUE823jJnW-oV-g6zW05ffHo-WWe6bg3Iqa-E-_EzdSKBsU_rWcQZAtWuHMLI6fJ3sDX7Xb94VjCAGh2sRe1F13vj5NEXzgNuDk5m7I-WHIkjg8PJK7uPdCqj5AhdbwuM4EFp2CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=pqhpcC_LTztpb_esvXSEOMm7WQ1xXMf_ajFARtZPOHPR1zHfJtKws3mKSqOSF8c1fMtklgaIBk7F4h-BCFFKDEF62nn7Q4yCeumODs8ergPyg3sxdA6lLPqTZtay7m1REWZk-Q4CYWF83K09xQQlP855jLreUrit71UBTH4HDpu9IXlbn0uGKo09eEktwwvC_IBrPX4iCY8sSP0EOLK5ydEeQPHQpO135YPTTCbzbV6ZBF9hZqunQ5rbNq472SMguHq7gYaU79LplZkxM_JZ-JqiJYmftP27RfIt6mnyQfdUiGbm98pWsYHm4KbEwP5lWl1CnDN6uMn_UHVULVQPHIfdqXijhOjfYXiheMJ_IX1_YB2161Ageijk6102oIIvmybmkLnvqotjoQiK47yNfXhe9SuE4R19BQI1Xh7oSbStw2w-KIQtM_icCbSwxfRoVbv6-FTTFWJP97oVauDDGMYhW15m2Lyx7TRKIcYFSHZ4EkK3IPokpqEgLui1l5P8KLp2WF5whQrbySe2zzrZmSdh8WmQE_ZKpfrdUE823jJnW-oV-g6zW05ffHo-WWe6bg3Iqa-E-_EzdSKBsU_rWcQZAtWuHMLI6fJ3sDX7Xb94VjCAGh2sRe1F13vj5NEXzgNuDk5m7I-WHIkjg8PJK7uPdCqj5AhdbwuM4EFp2CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ritkojX6Rm8zfHmJ_bSG8VDis8tSW7S1RMdgNaRyFlsYSHEHuMD8mUhL6jsFGeRvyEo9Yoclc7RBn7Ph7mEhpEzvYlcf4YzPEGEfhd_HSRHcOS1HN-p02Q-CKgeC87iQpDkatLrcwkp7cCKcupjh64Kf6J8ap9n7NYxdTu2yIy6WNaCFsNK3Efvj0upsr4CXEGtTLFE4GXCFJy1p1oIDyRUpdErLf_UKHDXzWIb_Zx6hUNTrPrAGoROLcUjRsAvxfU2-ScWV6XylZ8A-FoU3gS_JKTUlQMUWDYjurnD068_gaWXCwpcif-TVR5augkr-3WckRJScBxtUv8IgR3HMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzONjUlKW5dUrqwBhZQ8USEH4E6NgWzSS_r7MnuRuiZMVbk9C8L6ffQMMMPXRjUifj7jHIXFTK6K0BGI-Dm8dWMBzc0ZIsAmvFApLkKdKvQaMSx1IUqcrGaMP31LmJ4Orb4LQtvivWjQoVKQY8rZAVCVpVZ-tK0NBM3xsRswmI0OUjAuTNFoFvceAKSrFw17FeXS48mZ10FJfEIgEoWp98VVUBUtGh_LMIZQUIIfD7kvMad8G37QdQBxlEbwXiRnQL3xQ_Hmu_9GXNM_Ub_5RBp5phhJnSRV33GW-yFlG2STeIRYLUHsPCVnNabSrkHvNEY-2ANT0LshCwNJo2VhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmANSvseZgXSPmWiRw_jxIQgRIC8Ik3SXBdIta2yfqqqhqi-VcvhMgjZfRhvx8eW4qzfbkEgjG2o83rdLvutLRtTJm9Sh6iUWY67M4VwYsyEmYd8ER9topIw5lGPK_2vb_dEB5j7_Pbw1IULyfKoE8y-9HZG0GAEry3owslAGkxsswqSyTUA8ZwiWxb1_aGBdzYzGqJ21ucGwwlOzrjq2EhUD6dI9VhcuP2eOMMi6jkbf0421eXwmQJ2Z0Q-teWmgANiksOchDqR2SRBDDGdkf8vHM4fY0abk-G28rsUiR977kiqwiQLYAZC8OI9LRJlOj4-Cd8sT-2Lb82Wvg2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=oOcNcLVduYBqv1n038tVvMvM9l8koIpz-4TqO9r_oC7sEs1UdNapKqoC7Sm_0krCHdWo-9Bc5P0iZTmwlZ16zaf7_v9-ltuDF0uuli6TU5jcpqR7q5FCxC_kJKirfhcUnxFjWSv6GNxMw2xHdGV5OsrhsWJCpBgcLduJmmOPgvhmomjZgXyFqF0XXpbwHE0kztf2t5JMA0m3jCCCK8IEcPT60xMhlM8qN6UvbucTXc1oJgLkg3zEaUA2lID80KNNmcpt8RLAkAn38TZTPX1FGy-YXxUEnZMtic_-28__bQrE1mjhBxOsHebjpZehBYCfwbWDvgw4Zp-s545i6Lwdpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=oOcNcLVduYBqv1n038tVvMvM9l8koIpz-4TqO9r_oC7sEs1UdNapKqoC7Sm_0krCHdWo-9Bc5P0iZTmwlZ16zaf7_v9-ltuDF0uuli6TU5jcpqR7q5FCxC_kJKirfhcUnxFjWSv6GNxMw2xHdGV5OsrhsWJCpBgcLduJmmOPgvhmomjZgXyFqF0XXpbwHE0kztf2t5JMA0m3jCCCK8IEcPT60xMhlM8qN6UvbucTXc1oJgLkg3zEaUA2lID80KNNmcpt8RLAkAn38TZTPX1FGy-YXxUEnZMtic_-28__bQrE1mjhBxOsHebjpZehBYCfwbWDvgw4Zp-s545i6Lwdpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=beJ0ukUELKF9xM96HSbh6az1F0azkl1OM0lzneh89RT05op2yPidEZfGR5YELrCyGxqx-4aLvASVikKsFZx7PVX-4rPZ-O8pgOapVMVj5cx5OBvS162glxiulTt_3_TZgaPJabQ2FXKK7-y_2BI4Y5t7s76bHe54v7G7RztNPOMKEZL1StrJ1D_9x6IAlqai6uwHmiTlTuxue2HKhQqH_CF8gmi3BgZn13wQREXvsSI23NgF0VQqHbgOmTtzwnWbly-L4hKNzM1wR0aD9_vRPTNDKLimIv2FZXXFMKrYxxbEIeLYjBVYyc5gXWbfC2qtZeFRY7ODcVwYavcNee4EGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=beJ0ukUELKF9xM96HSbh6az1F0azkl1OM0lzneh89RT05op2yPidEZfGR5YELrCyGxqx-4aLvASVikKsFZx7PVX-4rPZ-O8pgOapVMVj5cx5OBvS162glxiulTt_3_TZgaPJabQ2FXKK7-y_2BI4Y5t7s76bHe54v7G7RztNPOMKEZL1StrJ1D_9x6IAlqai6uwHmiTlTuxue2HKhQqH_CF8gmi3BgZn13wQREXvsSI23NgF0VQqHbgOmTtzwnWbly-L4hKNzM1wR0aD9_vRPTNDKLimIv2FZXXFMKrYxxbEIeLYjBVYyc5gXWbfC2qtZeFRY7ODcVwYavcNee4EGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=ec1FUYDnk0_AKcV26Af73mvY2GToWqqqjpXsW3fYWYT2MzveeGv438SOor4AwiBdw6hMpidGRDQK0SrxnJY4oeoeFWwahPX6LIj8nJke66xhcWxgDL_WDg8_Uy8Ae4ZzeSVwrbmf4MqFRUFh367jAbDi1n9mq0Rq0pme58tOrY-TwcJjfXl1GbUlEo_IjhngWoMnTeKgk1sT8a2WXKHOjPT1Cz8GY_Shl3MrRj1tcUoNhbWbANwx_9f_oX0O_lVa2YvFluiVlcsXIOpWLg-Y-tzZmRjKxAAuCdWKLJ54lPnJen1jIWqu3YuhJVxtwg-YG_LRT9q5p228j16nOGyH2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=ec1FUYDnk0_AKcV26Af73mvY2GToWqqqjpXsW3fYWYT2MzveeGv438SOor4AwiBdw6hMpidGRDQK0SrxnJY4oeoeFWwahPX6LIj8nJke66xhcWxgDL_WDg8_Uy8Ae4ZzeSVwrbmf4MqFRUFh367jAbDi1n9mq0Rq0pme58tOrY-TwcJjfXl1GbUlEo_IjhngWoMnTeKgk1sT8a2WXKHOjPT1Cz8GY_Shl3MrRj1tcUoNhbWbANwx_9f_oX0O_lVa2YvFluiVlcsXIOpWLg-Y-tzZmRjKxAAuCdWKLJ54lPnJen1jIWqu3YuhJVxtwg-YG_LRT9q5p228j16nOGyH2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9GQhYWoPG7opZe6Nvqs975y73sJ_dx_tWPo1HbisXhEHrwE5N6b72V-X9_O4VIXNUescwkDaWlnWGTgTmBepCsiY1cre6gVb7nPa7t9na5eXqp8Gt0-Ha8v04xiOdbKCRfQhb4njb2BkFVjXYQr0SIXeIGIuhRAGB6k1pmJZb-zzvtfBNPvFV7zS00_ZLtSUXlpB3bnig-0LdZwZz5LVq19DVIcM4HHI7wINd6RDCQ-DYQRWnvk6Gc4nPUKBwvOjjsTs-jhNxHae86zj_Dl6ZO7k0jV55l6RC1XlbMHcAS_q382_8xVs9TtRuphuPnGymITOLB6Af5OpyRypoT_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=OfE8wbOJTMerljbxhBsZu0q0MpeteIkmyJ9NrQiInIOSHH8jA0fFRt7gRkhOQBI2GLcf7zcTc2rhhXUh448M8S2HxMGidOVPdJnBPKltFEfVzt_ss56k5YrlCjoR27SAihO3MHXhcbONZILB4c30pJpcNJuRFE0KIRdip5KTXarqes5VsGmYd_7YwN9C5_eAcWmMRZ-_YEo6Zrs1XPB0IiayW3D7v-hk-9iQwzPu46-i8Q1Cv1ijWm_qpZncOIzrP6UYHSvo5FbMLx-rYO3_f7_tfGDrnaTMXAUyH9fN2TDWxjQM-CfaWjoby3YmeyBSAK8tueElA014czzrCpLBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=OfE8wbOJTMerljbxhBsZu0q0MpeteIkmyJ9NrQiInIOSHH8jA0fFRt7gRkhOQBI2GLcf7zcTc2rhhXUh448M8S2HxMGidOVPdJnBPKltFEfVzt_ss56k5YrlCjoR27SAihO3MHXhcbONZILB4c30pJpcNJuRFE0KIRdip5KTXarqes5VsGmYd_7YwN9C5_eAcWmMRZ-_YEo6Zrs1XPB0IiayW3D7v-hk-9iQwzPu46-i8Q1Cv1ijWm_qpZncOIzrP6UYHSvo5FbMLx-rYO3_f7_tfGDrnaTMXAUyH9fN2TDWxjQM-CfaWjoby3YmeyBSAK8tueElA014czzrCpLBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Wex88sT9wMdUAqdBZiVC3lZUYImn0_-0f5Bv3-GPf0AY208mu60XRxBDgqYxNMK8OZJ3fXmtE5peoPCFaPqiI3sJpDszThJMUlLM7Dlg6sDEy7X5uAlGGCuKVBOzUxYLlp-x9IyJrpwka5zKDVEOGGaynl7EC5HvSLenBzXmmy6y47BYLhN--F5ZONvJADbe8qNcMqm9kwdrhFzX3Vao-jaLj1zXS5pHVrA_SpGWk-wesTDLc233vRPLjWCHXqzH6OeVyjd7LxsT5TME327DSU6pi6jVsSDzHDDBvqkpYE6zYIm6478stWMbrOBOS5bulVEANDMRhQaFf16USYVqGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Wex88sT9wMdUAqdBZiVC3lZUYImn0_-0f5Bv3-GPf0AY208mu60XRxBDgqYxNMK8OZJ3fXmtE5peoPCFaPqiI3sJpDszThJMUlLM7Dlg6sDEy7X5uAlGGCuKVBOzUxYLlp-x9IyJrpwka5zKDVEOGGaynl7EC5HvSLenBzXmmy6y47BYLhN--F5ZONvJADbe8qNcMqm9kwdrhFzX3Vao-jaLj1zXS5pHVrA_SpGWk-wesTDLc233vRPLjWCHXqzH6OeVyjd7LxsT5TME327DSU6pi6jVsSDzHDDBvqkpYE6zYIm6478stWMbrOBOS5bulVEANDMRhQaFf16USYVqGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzOdNu2lj-6rXeMcFoA9VZp1V_KIFO0BkHv4rqc7ltHWFWLKYZngtbQrXTnG4YyXGGg2Hy9y2LFyOe6uN8kqQM0ZiooEy51BzCsIOsSUon0U549rfxi1vPLDR4Q-vKnbA7gMRUUAG91bChGmt3loF02EcSysdyWYWJQPDhh1RCxHArb4PJ_JbbCHBot9T8B99-IeFbxFAelvMlLYFaOFyt0rAd9-cIvFvICMaSBPns_oCdI0MoxtEVWIkEWbCvtklGkHR9cXFQJD-2u_RY3Gbb2Vwv3irEbVs1zycs3l-CwfTqj9yCxWng3HsIJ-E1Zf6yFTXaW2B5b83tb_UlWpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=le1TCrsP2ZvLP6DyaCjQchYABN-ARjOnyt8NStE7mDd5rMs-A4eWbamlKDfK3EnMDeXgfgo0R3pHRUe-YbZrK450DFprlkySeA6dwThVhKnG_AGjp8mhwH61mDZ4dfTU16Q36VMTegmivbSSYNEBDD9vQM-So8oLV_gTk7r1AJj5LnTJRr19I6DFNr7h_FsmTsLRvW1zSulfnD6kVFAj1D-RQUREMYmr5sMOu_lXuzyqEWORN0d3yyMuyCdG49iVvTwInk-nm9_3JfNc5MtdQnEVrBcEce6oQ0ZW6t9ZaT-0lXR4XXoKsfj0uaT7V1k3utRK16BCFMEKYhLpOSKkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=le1TCrsP2ZvLP6DyaCjQchYABN-ARjOnyt8NStE7mDd5rMs-A4eWbamlKDfK3EnMDeXgfgo0R3pHRUe-YbZrK450DFprlkySeA6dwThVhKnG_AGjp8mhwH61mDZ4dfTU16Q36VMTegmivbSSYNEBDD9vQM-So8oLV_gTk7r1AJj5LnTJRr19I6DFNr7h_FsmTsLRvW1zSulfnD6kVFAj1D-RQUREMYmr5sMOu_lXuzyqEWORN0d3yyMuyCdG49iVvTwInk-nm9_3JfNc5MtdQnEVrBcEce6oQ0ZW6t9ZaT-0lXR4XXoKsfj0uaT7V1k3utRK16BCFMEKYhLpOSKkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aVWWDCNN-vZ2ukjYShV2xUT4Jv7YT3nHxIwQ0d3iygc01Obx6IltFrhqWGC_46WtfDlM6aSLiq5K3M0-31KkS2gRcSKou15qk5cepybmn9fLN6DPSO9qq2NICzLOZJygT_nFRG5XA3MpeiyUN-wefOcDam6QB3Ko8kdE8LDKZPtRGrHA1t45jiUMA_lnSZSxPIah00gPmPthfVro6uoBu1ITbvWSj6R51rtkbryOPsZzIvPzTZhzcQBl4JVK1lhfIFUcgxhbIUA-ZK32DmSBXQedVIlWp_dXfo3mrFr5svxsx8MpWS8_LHFEun50S3BpELTiinu-cDrEL0QvHNCehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZsiIvjX3d6_t1AHZkbCd064-_Uiogf0kLFFXOg4Kase5Gr_71iO8dlmMeXupc3fNsCVvqRUOJT8tEjbgd_6faIazTApbKo9ROKNhiIgHh5CHoygJTBv4Tr660HSTOvA4pwC3J9C5PrFpBhjT1Xz6ybBRTtPbPpSzvmBdYNYeW0Y39oAtyWa5YBItHKQTfp4JDyAlbcrkXhxz37p4m4mkdDNDmuC7k0P3glmO-aH0hMWYHwanLh2YU-SgPa5CNQ_fcZ-U2oAHCvenfTIIMEdOq4nZ2RLXMQsid63HhCN2ffPdMJ_vIXaJBG1xKHQbyj2XesJGYIMaMGp9xfiNfSmmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pt9Xws_zCsd2xDM2z6IpUKuPstakXWG6mlrnrspwks446fCE39k5_ILUXbDHZ4r3XmvU_lcLsQvC4LLpftS0L9hnJ0Tffse81gSVWGBWiMF7S9aWz1lic_naGEYHxp8GTm0Mc4fdKHsg9JVOD2AjB1Qp8yrrRV8hs_7YLZB8GAwIHJMOUBo0SD5qOBG0wmHnknSae-GnW_ykuEuADQnflp4WE42felsPnrt8hzgXNuAL2TpTN_0pc-J9oqccTfgdczUN51WxdJXzQO-Oumqwv242buCzGXafg4KEIXOaW7Ntf-SPL_lv6KYlDFMSYCaCd4AebZk4EqPYZSeNsU7_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YtEPBmtb0edi7molDxe8t8Y_1vYQL150bGZebV_psEkCPui_q0Ez1LcFkMWr14tZ94cGZGvaAh1DIXQLibNeZ-uUNT2xslfOuoI1nRJEdcHr6uDcD7xkiDaRmL2NFqM5t4FRKNoWe45iRvGkuK9V60TvFXovg2y2Rcv3WChpRsnOgbivy0QtOwY3pqWPp-LKLTCIY5cs9FggNvC7o8HiV1Tf7DuR2ABC4Z7Bp6_W-nrkJCxXZg78d92r47Ii8ay740bWaHKj_2L4iV9fUhcAtCHCEmiYDwp_Xz0KYBGYYlvl9_26T1KhCcgl5Y9RkwtiLZWzW_DwdyOoHrHvJ6mTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t559uhyYee_NASDPFLWZcnnBuro2WRBMD45Z5ti9LJzI24b4XOlJ3IxynyD-j-SrL_pIAgI2kMvJsH5Ie1vfZdePszfcYfVsGbJjC2uFEWClL76aUrrL90D4wv8oB2lClSht4ChBqWfJUed1N9s9t8Ip1LpsK1ghVfHbAsGi91Bk_20Wta8FtuPCIfTi_Zp34R9SzX4tlJXzl_4pN4g4eNcfXUuWBaWmV640pwtQfkM06NHWfLRpLNlkFKmwgfDlsyU9MSP2gVcB8CC5iDIv_7Z7pq_vyeRaGj8rU8U_tEEEnR63bbFZDKS9bhkj5O8q_Q3f1yAWwvvteqVdAdAwLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxADOnJdflz8C4rDBN5TvrFVm6kqMY9g8e4i2eSTE5NNsqpLBCHXxMXt_iZuuKeY2I9ABX_NZ3dIgEfaH7L0q97MND6lLWUg9rRhOpGHVvC0uMhJocJf91upEHp_sDIP0csgN8zIcX1HDHjCxF9qbm5PVzZmWMBGUqsl8otHBdCleLoLPnNwotJwYOoe0ElwZU9tF47B1CohSvW4I6oLoUudkoyhZ7TXOHJsyl4mkeMlrPBjf9z7dJon38JINBzwPNptlew1AZ9l6ugZbAEoumTQlt8lZFPcAmkwJPYTRqjBAcLpZWSmpeA_6EIXplDQa1PuE90tkfe-2hsrvYi94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNB6oUtAXJli_EAb_6q2wdsiK6gFVwQQOxZaINbGVu_pDLWVStB6z0phifzrS3zrARsC5ywmyKxQmZMlIfKlB4xVICUnJuNr-c7wjBUOuVpiPoYOJVnLy1JbDzOI8bacIlPzh2TM5MDvKq2G9zuw4EJT9Py1BXJHxhX2x0HrSKRwRofeEzfSnr8qrfVP4BNrfMpVqYO4XS0KCWuWWdwIkrDH6h-Ng6NVZxePVUUqUJNM5Fw9vqhTsuyi5NN4wB_0PjnpBebZqMB-MyI-iNtqJ9UWZ1fHqxi63vAkBshfSMzEo0OSpqzbndroW6X_vxn2iVhlFzmmagZxoQvZ43wMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwBEfTXeL2YmJcHSOfa845BNM4lUGmis8_xWyXSRKewyeMtUM9WZXBUXpCTXc4SWqEprh3amtEUtX8cGydViYzkxmSVM7LiA49EkmhrA6qWS0iz-6kRg4GrQAaQx2rTQvEkW5uojvNxJZd1BLfe4Gx2vKTBD1gQ589hTUE354zfqttZTwSkS5v2yCXaFalP1SBmR7RmrJCdEEJ0gP2qYARzdxy2arBxQnnR6PAzOp36iGjwtP-Yjoc5N5DUveb58Nu207Dn7B1sIUIwRleSIe8FrmRx3pEQNLFn66PobIg4ffOKiEA6R2ro0trkMi5-wc2iRcLXwBXUwmvf01txpJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=eBs5KFkHiyQJljb9_XL_bMV4pNGVnheJqgz6hDWIFUKQYx42d4nbI4yjUbI6vWI5J5hlmP7Gag7ZDYQ8fl8MRXgVtU7poLIkNwL4wRjIJ0Uj5-gu1zvgrRghXyDeNnuzdn1LIs0Zz4AP7uJticsDxKX-EiD78csRV9vejJz-nTVvU2s9vc6i8nPiNzYheWMT8h2hgj__IzdwLPRrRCmakKf31bHmVsf38IFoYw9oOKwptFSN9FmidBKjKBLrSY34602U1isL6C1RlomlaxTTjc2qrOTMxWDz3uE2H-Ux5XnVcHOXFyxOcr92a6VJ-2c2FID6HAJW7i4tQ1bfoDIwCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=eBs5KFkHiyQJljb9_XL_bMV4pNGVnheJqgz6hDWIFUKQYx42d4nbI4yjUbI6vWI5J5hlmP7Gag7ZDYQ8fl8MRXgVtU7poLIkNwL4wRjIJ0Uj5-gu1zvgrRghXyDeNnuzdn1LIs0Zz4AP7uJticsDxKX-EiD78csRV9vejJz-nTVvU2s9vc6i8nPiNzYheWMT8h2hgj__IzdwLPRrRCmakKf31bHmVsf38IFoYw9oOKwptFSN9FmidBKjKBLrSY34602U1isL6C1RlomlaxTTjc2qrOTMxWDz3uE2H-Ux5XnVcHOXFyxOcr92a6VJ-2c2FID6HAJW7i4tQ1bfoDIwCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=pyZELajTA1bEVrPejRHr-wzFcCwhDjZ1dWqRkRAQA6wPZGpZb9rEqFEqUxHApD36bFkBvhcjjLZ9bqYZqXF2NCTcGMcUMitzQdjDYrrjyQEYM3EJQj4-IkXm965gHyY-Qk7iC5qP38_wxndnAwMJEKENROtFCRmpxb1279Kp0zxP7GNE_LGoBce2nzNYbJJWF6XBJbxGe9mhMUAX2hA4VW8cE0-grviQIDvK2HJ7SQq_jrX-1_a4zSdL_UhwNCh3yXmxFM8AIyREgfpXyxYvh5r2i0cRWZFRjUTHLirgdzZ6bDDWYUreN5Tqlq12K01NLc4irK3SdkkMbnCoytoXAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=pyZELajTA1bEVrPejRHr-wzFcCwhDjZ1dWqRkRAQA6wPZGpZb9rEqFEqUxHApD36bFkBvhcjjLZ9bqYZqXF2NCTcGMcUMitzQdjDYrrjyQEYM3EJQj4-IkXm965gHyY-Qk7iC5qP38_wxndnAwMJEKENROtFCRmpxb1279Kp0zxP7GNE_LGoBce2nzNYbJJWF6XBJbxGe9mhMUAX2hA4VW8cE0-grviQIDvK2HJ7SQq_jrX-1_a4zSdL_UhwNCh3yXmxFM8AIyREgfpXyxYvh5r2i0cRWZFRjUTHLirgdzZ6bDDWYUreN5Tqlq12K01NLc4irK3SdkkMbnCoytoXAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=CWtxUkaTYgU36JgX882XStSLIiApradTFcqZFzqOaRVa87r1Dxknq8jvZfC1263MSLhoymAMXYNYgCVzK8WubqLkHuiLFUgudAISaAY0bvIG-BtlP7kXdTt4U3kEi01h0mvBHu9iZS9fHShwvhLWDz14nVTOdg6Pa9RDixNDNc_C6JPReEi6jE0E3Pwphw7PO8IZ-O1F_aSpRQFxYnuneMWIuKykFwzxbz_hxWGZafvC61tfuMDLSfHo2flWpczwFzV6Xx5GncbJcDV8H1KvvS1eZ3IafoA_OL43G3iEAQ7zdupGhRnQ8xDmJiCzSEp_9CPctiblSqBCc0DTBwKwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=CWtxUkaTYgU36JgX882XStSLIiApradTFcqZFzqOaRVa87r1Dxknq8jvZfC1263MSLhoymAMXYNYgCVzK8WubqLkHuiLFUgudAISaAY0bvIG-BtlP7kXdTt4U3kEi01h0mvBHu9iZS9fHShwvhLWDz14nVTOdg6Pa9RDixNDNc_C6JPReEi6jE0E3Pwphw7PO8IZ-O1F_aSpRQFxYnuneMWIuKykFwzxbz_hxWGZafvC61tfuMDLSfHo2flWpczwFzV6Xx5GncbJcDV8H1KvvS1eZ3IafoA_OL43G3iEAQ7zdupGhRnQ8xDmJiCzSEp_9CPctiblSqBCc0DTBwKwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=AZ1YEF_6SppiASsEzU_SrqjazRbVsPhhGvFo5TA7xsxZASmYMqouTPEduk5n3tn4Avsw4XJp1defe4tFWQLg4GUzT1PzUSaZcj4rur-qX21pPxmv5vk1LmGYeXsJrMQUJ55511G8e3uKuaQo6tmjiDZRIrXD_RqrI-VQI_4dQkmFT3THLvHFUZumSgW2U1R_N_QLAojZKgas26drRkFk5faeDX3p9Aqbjnra4ZhsGUuityYytyuL3neAQ-Jz3TfL9ZL406hLD1ukdyQvGPcxpkIgB6HEY3hqIVuATuRpS6R0GuQfName57Ht8PIg0tYmkWJELU_j2WKVI0YQassEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=AZ1YEF_6SppiASsEzU_SrqjazRbVsPhhGvFo5TA7xsxZASmYMqouTPEduk5n3tn4Avsw4XJp1defe4tFWQLg4GUzT1PzUSaZcj4rur-qX21pPxmv5vk1LmGYeXsJrMQUJ55511G8e3uKuaQo6tmjiDZRIrXD_RqrI-VQI_4dQkmFT3THLvHFUZumSgW2U1R_N_QLAojZKgas26drRkFk5faeDX3p9Aqbjnra4ZhsGUuityYytyuL3neAQ-Jz3TfL9ZL406hLD1ukdyQvGPcxpkIgB6HEY3hqIVuATuRpS6R0GuQfName57Ht8PIg0tYmkWJELU_j2WKVI0YQassEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfz5siuWbzQDfu6QxofqNKq_z3fbBtJVDJ3eGxjmkh8-Wr2jlEkJs2DgnhTiYXTsi_TUm09TlmlJ9b3kqMxTL2EalYrSb2YMVcWAMjRGXMLEIDTnHJ2gWAfknYc3OzrSqrTa4hMqgSZYvjY6ik7dH9hDiKuMOzn8FMJ8acujLua5c3wpehkF4L-5lG3FuimY49Aaue54XVKqtKtMSVt1zPBgsRiSFT75C3yDee_LyPdKu-j01xNgzAqXa9UYm5vLKxonzuE9D6q595zvlUFtatMb_bmAosGWyjeF2fm9FD-vpQRQOk0IucgQlc43y37Euf0OMGw1a9aeBNY62ZM09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=JaPLCXvMnqBJuUq8zNhQhfWC8FfdQCdDLF3UEjgoEjCswUtevGhnwYwM9k3Q0xM6iyqui3j95UtkG-I3NczqW8RlkEPMHRSSC86oLErcE94qD2FqJPK5zZAfI1tvW2RtyiW3HuZhIAgNBGOpSVGeN_C6-g5Eyuo-pNfiJ-ThfZWEgLzoANAtKDTUXdILwZM8e2QyuQTgOVg-C0nHitzRfF4x2sUXD-CDQQju7UqEIYGHp8pE0ze_C8yrKsoF7AKLgV5eeRjQ8cXC7kvgi_n5ebdQ6mcyyOxYZCB5hN26qXpX1l7uBKL-OVWfCzLRTMEpYZ9jq832BCYfzfBTpdJokI9jaeFv_CcHvCUaIy_tFdR_K1Dk-FQoi9ZV2iL5kNCdjRkYPZ-ubNomQeb02q8C0zwymtaDuusrggrMTmEDc4No-E4CK8Gd4EcJyH18MtB7OBfyyIUJy9_GzeMK_OJ1yioPdmPcAhlLHNn_CZ1TAEsirc-BaCW0ucNERxHINcpK1hhj5SGcTp4Ob-Nc-0sauvIKwr1AVJqKG5ffyC6b-4vgFnP5ihq7aRBTLNuXtC1q2Xk_w5Vd1Myl2fJaj3Ivv9-x2Mjcc0BMoLR6yzK0g8AUqiiTn6e662zxbnm3iFV4PD_gTQtgYGZzYwPNF67yA1azoBH5zTVnYIFtDpExJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=JaPLCXvMnqBJuUq8zNhQhfWC8FfdQCdDLF3UEjgoEjCswUtevGhnwYwM9k3Q0xM6iyqui3j95UtkG-I3NczqW8RlkEPMHRSSC86oLErcE94qD2FqJPK5zZAfI1tvW2RtyiW3HuZhIAgNBGOpSVGeN_C6-g5Eyuo-pNfiJ-ThfZWEgLzoANAtKDTUXdILwZM8e2QyuQTgOVg-C0nHitzRfF4x2sUXD-CDQQju7UqEIYGHp8pE0ze_C8yrKsoF7AKLgV5eeRjQ8cXC7kvgi_n5ebdQ6mcyyOxYZCB5hN26qXpX1l7uBKL-OVWfCzLRTMEpYZ9jq832BCYfzfBTpdJokI9jaeFv_CcHvCUaIy_tFdR_K1Dk-FQoi9ZV2iL5kNCdjRkYPZ-ubNomQeb02q8C0zwymtaDuusrggrMTmEDc4No-E4CK8Gd4EcJyH18MtB7OBfyyIUJy9_GzeMK_OJ1yioPdmPcAhlLHNn_CZ1TAEsirc-BaCW0ucNERxHINcpK1hhj5SGcTp4Ob-Nc-0sauvIKwr1AVJqKG5ffyC6b-4vgFnP5ihq7aRBTLNuXtC1q2Xk_w5Vd1Myl2fJaj3Ivv9-x2Mjcc0BMoLR6yzK0g8AUqiiTn6e662zxbnm3iFV4PD_gTQtgYGZzYwPNF67yA1azoBH5zTVnYIFtDpExJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=gTPtVcrPxFgklFQ6CMMiK4B7NcmLXNuyZ_0pM7LR1tBL5sd5lU7msmzW3q_wMBG0gaKbn-gehB2yfZE_BSSWpyq3TFEZ4WsRWrfrvjv9-ORTRiLCtbgQhZmiJoKovDdwfGNBlVGustGKkEWBrtBgDzAwFSPnQOTAizoz9Yh8zhHLQSDd2zhT8w1wmW__Mnmwhvz7unqsp4RtasnOQIuTWfniMRbHY8JMVT83wtfDoLmgTLfPGnktgmVzHsgYdKQ1q2zVWnljGIljCzAF7wMzcb4aijRMtFP3NKUCa4T8cs9-MEDiMFvoOOuT8T4wW-2geOhFybGIMz6HGcrgZY0jRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=gTPtVcrPxFgklFQ6CMMiK4B7NcmLXNuyZ_0pM7LR1tBL5sd5lU7msmzW3q_wMBG0gaKbn-gehB2yfZE_BSSWpyq3TFEZ4WsRWrfrvjv9-ORTRiLCtbgQhZmiJoKovDdwfGNBlVGustGKkEWBrtBgDzAwFSPnQOTAizoz9Yh8zhHLQSDd2zhT8w1wmW__Mnmwhvz7unqsp4RtasnOQIuTWfniMRbHY8JMVT83wtfDoLmgTLfPGnktgmVzHsgYdKQ1q2zVWnljGIljCzAF7wMzcb4aijRMtFP3NKUCa4T8cs9-MEDiMFvoOOuT8T4wW-2geOhFybGIMz6HGcrgZY0jRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=phswrtf-1ToOhtm0FeGZhx5g6x5V098YDfQekkqSu7gvI8VjRSHynLgWRBkpO9rCmdgwngE9J-gKoZ_Zv3x1pXcdINc_Y8Ztivtn_xzlhYuIWBivdXiv6or6jekbgI3Osrg8D-shxvAXH9Emoi4Kfd703K-VSRwvUSz71NsL3TiL-eOPBx0VoLmpD0zJle1jH_PUDBaX5E5v7uiMDEprGicCkG55CECCk0wswlxvckyFnvjMyvgjV5zrFgftOUkbnWi_UqajROvIONh27x4Z4kPgwwcbfm409iIEDeKWp63J7C6gpkPjtnQ11lhGReXoJpq5pBCVC1h7X4NKFbhEvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=phswrtf-1ToOhtm0FeGZhx5g6x5V098YDfQekkqSu7gvI8VjRSHynLgWRBkpO9rCmdgwngE9J-gKoZ_Zv3x1pXcdINc_Y8Ztivtn_xzlhYuIWBivdXiv6or6jekbgI3Osrg8D-shxvAXH9Emoi4Kfd703K-VSRwvUSz71NsL3TiL-eOPBx0VoLmpD0zJle1jH_PUDBaX5E5v7uiMDEprGicCkG55CECCk0wswlxvckyFnvjMyvgjV5zrFgftOUkbnWi_UqajROvIONh27x4Z4kPgwwcbfm409iIEDeKWp63J7C6gpkPjtnQ11lhGReXoJpq5pBCVC1h7X4NKFbhEvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=K7ytOZRWCo6rioTmhXPAhrauprxZltKCPqW9IGE-SPSzUCrBihVc_bUrWjd7HGW-pWrWmEZaqriVTvMeDADcn6FF0TOBGYJ1miCdPzIbmGe9mgThqRb9kQHEVLMqlF_p1-kqV8gVAu7R_vS51JchEsDhvs2ULEbw5btM3YWC8c-ZOUB2ZejAXFvNiJSPdTEdl0Ok7exFox1m4pRU6FEaqoOX1pgq4MviYHT6hmHDGXkiYn7_7VSRPxA0poLSYZCKUDaSWrDxtmKwViP6lAS8D8Cml-vtShKCVvlxngQb_5f9nXd71qEH8_81Rb_nrPLXZ6xuM4FEsJPFccRFFPc2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=K7ytOZRWCo6rioTmhXPAhrauprxZltKCPqW9IGE-SPSzUCrBihVc_bUrWjd7HGW-pWrWmEZaqriVTvMeDADcn6FF0TOBGYJ1miCdPzIbmGe9mgThqRb9kQHEVLMqlF_p1-kqV8gVAu7R_vS51JchEsDhvs2ULEbw5btM3YWC8c-ZOUB2ZejAXFvNiJSPdTEdl0Ok7exFox1m4pRU6FEaqoOX1pgq4MviYHT6hmHDGXkiYn7_7VSRPxA0poLSYZCKUDaSWrDxtmKwViP6lAS8D8Cml-vtShKCVvlxngQb_5f9nXd71qEH8_81Rb_nrPLXZ6xuM4FEsJPFccRFFPc2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=VQcjyMoFqPjj2W2eLaQuzjddSHzqzUI2Usq-2TwcuNF7Gw-jccBn81DzFlVg6zHmeFdC5hKMLxlGUL7-kOjynwXZzx93XE8AyVf5eA8eQxbk3gG-xvP2cofy_t7Yz8DIj-vZ78n4l2nipZAyzrB1gVdtxH0BTwH_bPUoWKT5ieeDalgXzwwrZiIyfceYA8k5VSXK-GAtdZEkPQWq4zWySy0XeCyqwSVJYVIgq_2dCCG1nBQWISR1eHFCopUNqmu5oyurb3QbKQCR7WThKn5qY-KvuPJxITO_QbFx2MOAqQoHDjfEtUdamtVnHRtZErXZkq1JlPE7YLVY_cW1lRzPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=VQcjyMoFqPjj2W2eLaQuzjddSHzqzUI2Usq-2TwcuNF7Gw-jccBn81DzFlVg6zHmeFdC5hKMLxlGUL7-kOjynwXZzx93XE8AyVf5eA8eQxbk3gG-xvP2cofy_t7Yz8DIj-vZ78n4l2nipZAyzrB1gVdtxH0BTwH_bPUoWKT5ieeDalgXzwwrZiIyfceYA8k5VSXK-GAtdZEkPQWq4zWySy0XeCyqwSVJYVIgq_2dCCG1nBQWISR1eHFCopUNqmu5oyurb3QbKQCR7WThKn5qY-KvuPJxITO_QbFx2MOAqQoHDjfEtUdamtVnHRtZErXZkq1JlPE7YLVY_cW1lRzPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=Cr4N7tnEYp6wd0A_gWgDukJNtNyruYCURW2Z82-1qlUTN_pEKWt88_KqGOmEpJ0Drg3LiDI6IdRY9bn_e-Y2dQqPuwUOB-uLWnFcv_pyge0jfqtHsg1YzWAi8kFzn26JRVv87_N-WOZ-vg8JS6Gns4zM9zqPvYwvUlT40AuVDmtwsI0wuW_-8wtw_GYo_eUYRfy4OuCG5v04BeqIPABxBJ-VLuT2xSRllldYmtDiVeqTmXi6fnCMgJXbkSeDMyYYiq640fH3pJM3_uMtf2uR7VxTZ9MLO_PTvOuRsJPEdyeRbg9roLWU-wXVb6ptXypAbhlfP3qn_GxgWucMiAmt7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=Cr4N7tnEYp6wd0A_gWgDukJNtNyruYCURW2Z82-1qlUTN_pEKWt88_KqGOmEpJ0Drg3LiDI6IdRY9bn_e-Y2dQqPuwUOB-uLWnFcv_pyge0jfqtHsg1YzWAi8kFzn26JRVv87_N-WOZ-vg8JS6Gns4zM9zqPvYwvUlT40AuVDmtwsI0wuW_-8wtw_GYo_eUYRfy4OuCG5v04BeqIPABxBJ-VLuT2xSRllldYmtDiVeqTmXi6fnCMgJXbkSeDMyYYiq640fH3pJM3_uMtf2uR7VxTZ9MLO_PTvOuRsJPEdyeRbg9roLWU-wXVb6ptXypAbhlfP3qn_GxgWucMiAmt7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=ACiuZsFgPOnXvsHf9RSupNIZIfEt7Z6K2VIKzAN8F0wsIjikmUcbVYWdO_0l8hxOETu9Z8yu1hZEq6L5ILHM4ZdUOnYwF5KJfz3aGy8pfK2HYD3fs19-DAEaOuV9ThHlKEtP41-c8HO_NbWpdNqY6iFw_0YdDEPwqqqXw008ejCFoE5qqTgRNNti4I1lDaaM0ulEkL6IxSFUjFQJ6bw4WpAurmpbyLTUlrbxaeT4vNNOgOx_V-63cemG5hHWxDDDOCeOtCeTbmoi4DYI3DRstp8chxcb3a2reqlpLOsj4fbEcE5Wxg_aB0AyUAm2lU-RBMJoDzIKC6GQELZMqrvLvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=ACiuZsFgPOnXvsHf9RSupNIZIfEt7Z6K2VIKzAN8F0wsIjikmUcbVYWdO_0l8hxOETu9Z8yu1hZEq6L5ILHM4ZdUOnYwF5KJfz3aGy8pfK2HYD3fs19-DAEaOuV9ThHlKEtP41-c8HO_NbWpdNqY6iFw_0YdDEPwqqqXw008ejCFoE5qqTgRNNti4I1lDaaM0ulEkL6IxSFUjFQJ6bw4WpAurmpbyLTUlrbxaeT4vNNOgOx_V-63cemG5hHWxDDDOCeOtCeTbmoi4DYI3DRstp8chxcb3a2reqlpLOsj4fbEcE5Wxg_aB0AyUAm2lU-RBMJoDzIKC6GQELZMqrvLvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=WwJjSQwl1Ni3YP0_877xrSl1TSLbjP6W4trHdyEgcJHos3_Q51qjvgcijKnWYM3PTHZkG0Pd2BDHH7hlPOYd2XV-_GSLLSVtPYsAwmFicLAKdaPkhjzVbXIawl4mxGOT2Pn5-23hY99RZzbmr2_NvkwEtKLVmYAe_PDtFYldHUL8BN1viKVIDodldJ9rYAOV-0UzIIygP0T4ggRKcWPUS5MN4E3x64-12xXF9P54iet5IH8Q-D9H1dzGWpL3iJowYpnaeVN7IOEiePhtmkdxMDfjnKd8L3_p3fGX5aEWqgcEUFPdweu7zD_zIe3RbGeSofla-ElzCmnejXzeNVqbHpv5kjGqiCRvwN3Urhi1AFZYwNJkOKnXWBlwVzHetJUHo3ID6o5eLnel8g5E2H60OtQiO8r73HD2nnKnV0E8QB938-hXjz-Q-jDOnmldA2WWZGI0YQ2yL8gbtxZ4b-JwhBT2iNzwd6Z9Q1wENVhAulzkJ0PqEU-lK3CFTGkT88Sx9hi2_rCqxwxoqENA0WK4-Q9598MNbdW2JT1ZAoauSKVa1w1agg1aw3m1NVWJJj0bn_ztR7SziWtoXD2qt9ZYM922WOpKXlMewl-TsvetzrRFSBkWx0D98Xj6-DUVlEB73ff-snWS4kckPwaXylCE1AAObVlTlwCwohGcd9qa13E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=WwJjSQwl1Ni3YP0_877xrSl1TSLbjP6W4trHdyEgcJHos3_Q51qjvgcijKnWYM3PTHZkG0Pd2BDHH7hlPOYd2XV-_GSLLSVtPYsAwmFicLAKdaPkhjzVbXIawl4mxGOT2Pn5-23hY99RZzbmr2_NvkwEtKLVmYAe_PDtFYldHUL8BN1viKVIDodldJ9rYAOV-0UzIIygP0T4ggRKcWPUS5MN4E3x64-12xXF9P54iet5IH8Q-D9H1dzGWpL3iJowYpnaeVN7IOEiePhtmkdxMDfjnKd8L3_p3fGX5aEWqgcEUFPdweu7zD_zIe3RbGeSofla-ElzCmnejXzeNVqbHpv5kjGqiCRvwN3Urhi1AFZYwNJkOKnXWBlwVzHetJUHo3ID6o5eLnel8g5E2H60OtQiO8r73HD2nnKnV0E8QB938-hXjz-Q-jDOnmldA2WWZGI0YQ2yL8gbtxZ4b-JwhBT2iNzwd6Z9Q1wENVhAulzkJ0PqEU-lK3CFTGkT88Sx9hi2_rCqxwxoqENA0WK4-Q9598MNbdW2JT1ZAoauSKVa1w1agg1aw3m1NVWJJj0bn_ztR7SziWtoXD2qt9ZYM922WOpKXlMewl-TsvetzrRFSBkWx0D98Xj6-DUVlEB73ff-snWS4kckPwaXylCE1AAObVlTlwCwohGcd9qa13E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIV3AZ8kvml6FhxK7wldk2Va0iU3rZz6EPWPOJ1Xd00GFa6KKKDx3mqavVXUsZaiuU1SGv7rBSmKfgWTaqhMKwKw56X26d7RCk26pwJPHkO7C8Iae00tf_fa9Smdhq3YlQFRCNYLux2AV140iNJ7n3AG8GxNDzxS6vRB-syjpIWxOhyhdK0Dmr7Wth0IK422QSfqygCu8cVnqc8O1rKCDTL6eGtzs8VTodsz3dkhgMNhxbTnTcxrIvBV3GubwhuQa5gSqFGo4QvqFafmjqwhd-Wd5JO1BMii_6vZ-vknqBMKgiQ2Y5D6KyYJv6jKvLqVrlJWFM6ZSZ1_iq93SvonuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvVPhcZ4hLL0Vazzm9FHWUa4QSHSy_6UP6N017KYbg7QOpnML-0e2qVhWyiQWbLOtxpIZ15mnizocid2zRADUgqBPVmUkaa1RU9Fv5y_Ux1r-YOAEzJoDBU0O5Cpm6cWuZ-gVsxZJjkY-Sx_5LRL4j7_oaxM8TRi_hVWdXK3lamqsEWdLTlFAmadbTRKuoMNREtD7PPcVQxPYDQ-Ef8DzAAlGz6-2sHGklIJ4uv-MZpg-ghMcJBJ5ghTxCeR8FWxN_hmcCualnpfMFBjl1Vfx9obBA4r29PvZa62ZeExBKCWS5Gq99iFBZvDPZQYnFT7Bj39laZSgSRSXMpzWJTg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azvi6Wa-4gslhsHxIdknXaGU0tmS6uee4GzHifwYEV5TW0fxbPKh91cAcooXgbLLSD8kxfr4NCN5HwfkQWZO_1Ylh_alIl2-eExqTDeJCsU53hVTeIiMjI3L5umqVWji0W0oaAf4WRTeJGIEPP0s6EYrgFn3bTB05oXK_MAYAL_3Jm-J-m79HfJF4gM8-fSuNunt22gk_23OTdeOCxJF8J627HsDz1aR5XwVmEZ-C1EkdQl4UI_37Q6pPOTlvyNCUwj6wlPqzYq9ysf8XY4YJ5vQQBHuPbqJxs-SZXTnJW9suY2j6hdf1H1i20i-4wjvCX_aHvFkezBUn_j3m9Sjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diUdSG8rUcrfP_h9UPbJdtGnVa1gSE9SbD5Cd6ibxkRNWzGx1vRcvPG4zOw7agR-emPEN1yBT6eQvPEsZVv9o07MoDS72uwC4Rvh52cHeUTpQoF63Y4wf5_Ck7o3twPJjGsKgqv_mxDyXURvfECKCx9KRXnBmxjOs2sjd1WCY6Ra29n7Z7FPF4srYcq1ZNllSnKgX5KhfJeCKeYz9NBEpav26F6e_Wq2YufWbTgG96z9kS5gKOEoD-HBM9_9Ucga3ew0PoeVIxlKc4UwJJD7TM6rupp2XpGVIaHDudR1GSrGQgb8kxj3SPaX4NP0b8za8iEDNa96IhpsIOxovQWldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4RU4agRLSsQ_rqeMmAkX8yeUmToFRzUXrfRFMZsQ79bbCcamsqca6L_aRjSqGrxMGpT0PGB4GLEHtYgErvb6G39p2Ue3j8EZpzSxR0U-2f3Hy2BaRc9te95fPktcjX8POckR2BBWNRC9ULZlBstQ0HbhKoYjMPLY9Z-53_eKYRdytCSziIx5XhsmdohhyXU2ZnZJR178RUXShae1fCpJbslfQaYroAsX3fI8w5M33P7foxRoxKGTc0F_pGmVcpaviQpFA2F-1VchgBEDhGQF_COqdNcrgAgyzhLG65hi5-Yp__HvjqX_Vhik5Yz92suK83CLb-mzVLtfYfbK0V9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeTEvigttIe86i-wUuDEYRFKz9SWctf15w_Mt8itM9p7TllcY9dNDUKKxU3ivsOiBQueo1zaScI6fcNPMJK1WX4_nJwzL_xh678SOYdnZWy0gAqdbNTuGBr7sZgW9dW1hZL0ihuAnk63YbGKbJyemWGxyD39YfT4YzNBJfN60uCL6KVqc7zJcjne9HoQe8BECj3pu28Ljz63kyDVG14ZGhykW5qQA4IPjrFfJPmvgINjdMozLtijZa8BRH2TnNhZ5j3ENEBxXZdm5Rv1EDSveCSeFjYKe_GS19l9gkFo7HvDfGRKp3I__If-7Gci1f_vC7ORl2MM6cy3F-THYZAg0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=f1jW4VJhTy9VLjvCYXB_5-POjMXcbJNhikyfL5Wifrys9Q1LcZUo4cvWUrB4J3TOj_CaecMbVJ3g9ryWH4jBqodHncxq-5G1JqgPhgHHiQLbaN621JXWDya-5KT2yWU-_DXFmIXd83dGm082NAkAIz-fpNMzjCPccdX3X6PtsaZwYv0KBnkOCyMcpffC87gtRiJ1cC46IZSSO0wGFHCssYJVhrfVMZvC8bA49oIdxVtsiEO6z7xwb1sAlYz19sX_geA8yooSY88FORYlwEAD4sqpJ7zYP1B3oTMPC35sGfC87uRSV4oqjIEy5pCQkPge1yXq_1sly7lKRR3Knk5AUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=f1jW4VJhTy9VLjvCYXB_5-POjMXcbJNhikyfL5Wifrys9Q1LcZUo4cvWUrB4J3TOj_CaecMbVJ3g9ryWH4jBqodHncxq-5G1JqgPhgHHiQLbaN621JXWDya-5KT2yWU-_DXFmIXd83dGm082NAkAIz-fpNMzjCPccdX3X6PtsaZwYv0KBnkOCyMcpffC87gtRiJ1cC46IZSSO0wGFHCssYJVhrfVMZvC8bA49oIdxVtsiEO6z7xwb1sAlYz19sX_geA8yooSY88FORYlwEAD4sqpJ7zYP1B3oTMPC35sGfC87uRSV4oqjIEy5pCQkPge1yXq_1sly7lKRR3Knk5AUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=hL6S7-b7Uc1DQY4yXDqYimTCgGKSxb99EbwCwW3nylAam6ciSXiGLMXQEcPO8dLURVuXcCvMACBXbVt7LB3u31fz3mYFaLiTDsD4RoqGDy-2nuAEvwFdimA9rtP-lK8FSCYf8cWU7driQjsUsyxeGDobPu_o6ipdXByHhtZxql2OkzBuhRItJfcvbAfq_NMEBMrs1UZ_4RrOa1BInsdl5uzRfRQ8JFr41CvReFoZ37Pm3SpNf531JrERY_zBEAsS6YH7fEi85jWp1dc-bmwSFt_7w49XHO_dvTR8YJyb_bn93aZmWMpphbyeGvfzl7qvzdOPkt4yLe7pR5hc7jCXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=hL6S7-b7Uc1DQY4yXDqYimTCgGKSxb99EbwCwW3nylAam6ciSXiGLMXQEcPO8dLURVuXcCvMACBXbVt7LB3u31fz3mYFaLiTDsD4RoqGDy-2nuAEvwFdimA9rtP-lK8FSCYf8cWU7driQjsUsyxeGDobPu_o6ipdXByHhtZxql2OkzBuhRItJfcvbAfq_NMEBMrs1UZ_4RrOa1BInsdl5uzRfRQ8JFr41CvReFoZ37Pm3SpNf531JrERY_zBEAsS6YH7fEi85jWp1dc-bmwSFt_7w49XHO_dvTR8YJyb_bn93aZmWMpphbyeGvfzl7qvzdOPkt4yLe7pR5hc7jCXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5XUTzVMshKZrY09a4el_FB8rnkbpXhuid1cyw6SOxGmvuZq5TuTKkCTFq8EEcAGhmmVfCUpGlFAiTBdddra2nSKIGGNwgqEQW12m1LJzI-G1Rug4MtFVOhOCajfmBeIW_HBKNp2n9wwJDkJB8DrODiqFPvs_YDgrVMjoW0BxPHr14a12I9CN8T-Q6xveLQf1VVWcnP4mnuZu8QVVt14KIvbBd91-6BK-lFDN7RduzqI2Q1ROX8RKnHc_W1cGkjQuNWrVby79KcGoKf-ZkXLAv4kAThV0_S2s6HJYQaL52T6FMoYNaAYM4UqecGOJFOH4lDaoDJwThBpSIMYgEAG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBpNkcSJhCI8V4pGTyRAaYzRsVb-tlWR1DG0-G3SgHon7x-WCtLVkONWh6l9-0F8XPUG0GUvOHUsHKm-zvpnMPZbzgDNDlket256Pc9GI8th3ESasnfZ-UWCXmFJiSqpRGCKAMn-Yp3BirzJ_Hn8BjfPoENPlAoS20H7zA43NkouZNCz8TwihRw91ZOSu2TyAk8VV6fvcU5mRM07ppWC4vxP9Kjx0h1-N5S9z0wYhZMOcX4dWae5ZndNSHJ_2OqV-rJ7usGprreVn4E_i0wp01-eFrOQkcl3GK2xGjbXHlUvUAwtknlzNkEQtFbYDzsdhbGObUKfgW0a5hNHCYdCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-qVKzFuyM7BmW4dhi5HnIdsTrGZqYxP5DfRgfoUznhMGVQNk2Ql7EhAZ1Hkf7LdqrF_AVaBtr51elbbkxDTHWPtXZzvX9pxxNaqfZDnmQA0NPVgJCo2mTN7gxJmSA6rRk3pBifzU0zqw5oTRs_y7DheNIdJikIhoNJ3xO7v0pLilmtoS2b4fXZ8krToIW2ooZT0RDTqLhd87iziqpmqBFDTRZpcqnHc8UWDxM9MIXjPcFynkykZTYdW0xZH6GBb8IqfOFA-CCu91iBhekLyajY9L9XnVoCdl3XJkRjzWJGxyRaO84e2I6V-bWVSr_dsOXG7jOh1I-LZjoDTk94PAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=aeTOsFNV5agmrtxbPM4Y8hUGWu0dxZb-brd5KWdfPm0rCPf-VMw6IHM5jaCd84RJT4huFpd1JCiTXSBn7rBw8ZGhuftEMpQvbnvnZG3mPPDEulIE1T2cjZ7cTs3gwCagg2I2n5GXzfUaTUKj0d6k5bw-AYx-1-RVZyC4qxCi6rsR462K7YkSPzN6gOaRSC_VjnyDgffEO_cMqchSE9v-rM92DInU2rmY6f7saw4uJqDCzoqHCDtrhjCb3fTByrl2excdNJSnlsU-NK6OE83o_bxX5Tv05c4pgu2mW3cG4VO8tqVjfp7LMX9wu_nf5WW_Df52HcYMNM-7tHajdnptXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=aeTOsFNV5agmrtxbPM4Y8hUGWu0dxZb-brd5KWdfPm0rCPf-VMw6IHM5jaCd84RJT4huFpd1JCiTXSBn7rBw8ZGhuftEMpQvbnvnZG3mPPDEulIE1T2cjZ7cTs3gwCagg2I2n5GXzfUaTUKj0d6k5bw-AYx-1-RVZyC4qxCi6rsR462K7YkSPzN6gOaRSC_VjnyDgffEO_cMqchSE9v-rM92DInU2rmY6f7saw4uJqDCzoqHCDtrhjCb3fTByrl2excdNJSnlsU-NK6OE83o_bxX5Tv05c4pgu2mW3cG4VO8tqVjfp7LMX9wu_nf5WW_Df52HcYMNM-7tHajdnptXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=CBHRkImSm0SSOcx-5eJpfmllket3fv4InKwbc4kx8SKJV6rXq_i_Jq6mxrLGd6kXaVuosdkDgXv-qe9MaF3ORGHUJ8Wjb9Yi7LdNHXq7bM4WFTGMTHxId01Dg53TY6EhEdo8rqr7G3XTZgMiUFPjMt0tEUPzK4S4vHwDlH02ARH37XYNrLGElihmJJXiusH2ze8M8H2tcAhq9gRWHq9xyU1vaTY0tsg_lx_3Ha4NLnpBPzw_v1aklbR9_4UQSz1i3JiBkN99uY8QlJiWdTJ4m6kh8_LenxEPeRFxCBEMI6PWHfG1TPdORedHm-HcANZuQBEoHX3Yp_fSeBSpgRUENA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=CBHRkImSm0SSOcx-5eJpfmllket3fv4InKwbc4kx8SKJV6rXq_i_Jq6mxrLGd6kXaVuosdkDgXv-qe9MaF3ORGHUJ8Wjb9Yi7LdNHXq7bM4WFTGMTHxId01Dg53TY6EhEdo8rqr7G3XTZgMiUFPjMt0tEUPzK4S4vHwDlH02ARH37XYNrLGElihmJJXiusH2ze8M8H2tcAhq9gRWHq9xyU1vaTY0tsg_lx_3Ha4NLnpBPzw_v1aklbR9_4UQSz1i3JiBkN99uY8QlJiWdTJ4m6kh8_LenxEPeRFxCBEMI6PWHfG1TPdORedHm-HcANZuQBEoHX3Yp_fSeBSpgRUENA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=kWc-b-Qg63RONtznXu3dHE59ny4ByGN1N9U95wzywgnYlppS7rRjFT0e2jesy9f0YtIfXAzBAIpfcpaIftfF5HTNlP61R8LoBlxrNgh1Eb7hEa6tk7USg0qxJuKTT7wR0xYD313-w5vKNnk7fyeOdV9MWr4ziwUbQ-_QweYN8MM3dXEorPdkO7RdW5AU7Sgo0s0YXAdCJotGrAPfD6iY-uzIyuS6l7DvTthbOSv1tGcsq5WxhZLS9NHHhP5JE37QWBSc_HWGv4snmd9_PlJ0NVfEyJ7CIv20YV_bmLLIvdQ2N4JuQEZ3mX4GP5uPqnLGYj8WwAC-3f1w_WJBkCV8iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=kWc-b-Qg63RONtznXu3dHE59ny4ByGN1N9U95wzywgnYlppS7rRjFT0e2jesy9f0YtIfXAzBAIpfcpaIftfF5HTNlP61R8LoBlxrNgh1Eb7hEa6tk7USg0qxJuKTT7wR0xYD313-w5vKNnk7fyeOdV9MWr4ziwUbQ-_QweYN8MM3dXEorPdkO7RdW5AU7Sgo0s0YXAdCJotGrAPfD6iY-uzIyuS6l7DvTthbOSv1tGcsq5WxhZLS9NHHhP5JE37QWBSc_HWGv4snmd9_PlJ0NVfEyJ7CIv20YV_bmLLIvdQ2N4JuQEZ3mX4GP5uPqnLGYj8WwAC-3f1w_WJBkCV8iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDOLmuHVkVn31XwHtp2lM037ob0xhfpO9JrvTP8cHEaFUqG1tFrLkP-uFiK2yFkpgjZr9-CZDxxhf05iZIhObI9Cu9guxafcAg_aDacz-6BnPWjR0-p4Gm3qzlfhQk5EZ6FxvUp8eACh2pSxqyGuhEC_Z3MsUEXBp_3kQaDc68POjZucGjlYpaEzdiL04Fkh3Ya0zfvDv35VJdR9lMrHy6oe5N-iIOzDuaubGvKf2sNQiBhymGyuuxKuCnK7saHx6pLHA0v6N4q7o8jtrg_2qCvdr5KOEMXsHx5wKJuxCI4Sju58HDL_mkoEAuXTd5xFAumYiXUXgj6PrLmtMSh76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eubu2Y69s8kI5_lz2dLy5W3pb2jBJvTMYFZl5KKgr5P10-wblEq0eH-9swiFo83qoL9-a9dmrkO0i04R7M5Coich1gH3zDlEWPAuuMEQwVoqvU3zrWv25Eu3xkDK7EQxF4pV0qCjpuqLQvucl5VQ18SUjvUAkQFpEmYf0LyMnEAsvkX7wqVKFIECgw_U87EvlCwbBawfZP69IaLPQGNpNglCXTIF3lSm2q9utEPdUOCfkn8ak60z27YwqppXzybkDTeAu_gx-D-ESMbXGEDgkgo_Q_jgGCyyP5bDgeB-RMnZSn-UfN3pbnq0foEbAXVFNcNh47d-OOUAt1k_7PbkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=u9FL60okZYj_PENVzX6c2irih9tHtI82FWfQuTOQd5taPjlnJp7eFFVmnh_BZ3tStFkDeMVOm1SSOtdKL7ceiji9MBEF155t6UkGL8GnTZN09Jh2KvfuoniypPR_yfe4S5A1oFnJxDq5V9mtZw4vhO4OytGyi4KPWFVN3fo-6FkAoMeRicP6LW73h2tleAuPNtMgN0cHo_tsT1COobixuATI9AWyYrnfJqpZJL6063AIoo4be6_P7Z9P8rsj2J0rvu-d0nxLkKhaNWqayaLlW6TMjrTHiX3a88XxM2ooQr5Pf4zp8XEwOaC9oKoDfyZMJzNHaYZKx4jzMgTh2y7Z6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=u9FL60okZYj_PENVzX6c2irih9tHtI82FWfQuTOQd5taPjlnJp7eFFVmnh_BZ3tStFkDeMVOm1SSOtdKL7ceiji9MBEF155t6UkGL8GnTZN09Jh2KvfuoniypPR_yfe4S5A1oFnJxDq5V9mtZw4vhO4OytGyi4KPWFVN3fo-6FkAoMeRicP6LW73h2tleAuPNtMgN0cHo_tsT1COobixuATI9AWyYrnfJqpZJL6063AIoo4be6_P7Z9P8rsj2J0rvu-d0nxLkKhaNWqayaLlW6TMjrTHiX3a88XxM2ooQr5Pf4zp8XEwOaC9oKoDfyZMJzNHaYZKx4jzMgTh2y7Z6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHR7PWiXRJl7TrOAwkOwlyGF1pxIAXwN9Hf6uTTAypJZ9SxEOOp8PSo1awOc-DoYq0_M3LSXGZ6DQU4vA9osItBAQoldkZWCWVNXD5TS6K4Yr3_FFeDZmZP9jzRy8X-BaNNZA4sfBIhPdk7BmS6Rj8T4w_w7gSatlEWTRmCzrhMhpAVK9j8Zet9Ge_mkyaSOqCf6cIC6bUBu-NKqJoZdM77GGl6-YpeO7xSqM6jLl5OCDZ7NdNna7q8_cYFB9ePMiEtSr2uTTFDWGjqYRzKTLOdbYCqwcuvUa2Yh6CwzrSuTFUVrD3Av_1h3gogCCNHbK2ZcjqeyrJGOWEUMz_XVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=bBfpMNlkIwa3zSXgKuTlrwKyZX80yc7oqXwKVRG1GMn0I2ybJ6M7NwPelXFaUmOUeuXJuWv4bxSBj-gVKrpXtHoVyYhc38f_Oyo3OsIvCSJaZMspZJwU8vqrp3N-kiWDmxC1bxSFviU7tukuwlCsnboC4APw5R_SaJPCkCo5YL6T8XduQgyqf72rkhJuHfs4Y7pt3aMbz1JN33kgEgpOkM6oODb4pcsTk5IFEFw55benKDzZtB8ZGULfoBovrhcwUNRDLk46Zh9Xzcv7aD-nrSGQFvcSo98zWwOA-BZDy6pjHEtWQxfdGAVqzNTBquR_L5dZ9vILMNz7WIsmK51IAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=bBfpMNlkIwa3zSXgKuTlrwKyZX80yc7oqXwKVRG1GMn0I2ybJ6M7NwPelXFaUmOUeuXJuWv4bxSBj-gVKrpXtHoVyYhc38f_Oyo3OsIvCSJaZMspZJwU8vqrp3N-kiWDmxC1bxSFviU7tukuwlCsnboC4APw5R_SaJPCkCo5YL6T8XduQgyqf72rkhJuHfs4Y7pt3aMbz1JN33kgEgpOkM6oODb4pcsTk5IFEFw55benKDzZtB8ZGULfoBovrhcwUNRDLk46Zh9Xzcv7aD-nrSGQFvcSo98zWwOA-BZDy6pjHEtWQxfdGAVqzNTBquR_L5dZ9vILMNz7WIsmK51IAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buPi1CJ4xVtM6t2QDB1Tm6f2mOjuYvMfANGizdLTiUcwtQvdsdG504lznHtF9KXBmTNZVdiL9OVKo0byvjI7LXueHGn7fgdg2FrJWPIEFnKPLDRHODW8FypvvsehUUz3cf2QsnFtUzF3u1jV_u7vTp66YYONWTMPn0-86CMo2tjsNrzlNP3wvV9deeJEE13zfnzyNTIx8QPNfVTueRqs4CvROvYpU_anJ9ypcMjsibndgJsoYt6afCy_CqFswZl3okhQXzlwZBnVCo0nCoB6w9HOxqWdVlEhfhjDUKVONM6TqWw_uRnjlVWbK-bgmMtXBHc-8xnctcGsrOQugRSvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=doEsy42mn2OVh7zmvcNbcc3i5Nr4gmsw7AoFP2H0e_xTqJsJDkMTbS55n7jiX9w3O58nqEp3S0Ugbh6xk6HAZc2VeVAPeNvuTlSN01eiGkUIRL0jL-Y7LTaFsaJsmx5TyhSbKwzVGGr-cR2p7Vv2pflf2h83sq4aqH0DoxZKOppyJg5CLf6OSaI7U8f2ejPWmsTQc6d6BSrpSwymOJ5gRhoDa-poDfdvNE4iQ_WFQhPegI2OaYa5boeHwHYgPnQpsaMKUpeS2lMPGg9pz10H1ecx3kHVkk-8Q5ZaBZuvo-s6NU2vofbBDzu7zGyYwzXp_HuAe90Eo6MBi9r490LhrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=doEsy42mn2OVh7zmvcNbcc3i5Nr4gmsw7AoFP2H0e_xTqJsJDkMTbS55n7jiX9w3O58nqEp3S0Ugbh6xk6HAZc2VeVAPeNvuTlSN01eiGkUIRL0jL-Y7LTaFsaJsmx5TyhSbKwzVGGr-cR2p7Vv2pflf2h83sq4aqH0DoxZKOppyJg5CLf6OSaI7U8f2ejPWmsTQc6d6BSrpSwymOJ5gRhoDa-poDfdvNE4iQ_WFQhPegI2OaYa5boeHwHYgPnQpsaMKUpeS2lMPGg9pz10H1ecx3kHVkk-8Q5ZaBZuvo-s6NU2vofbBDzu7zGyYwzXp_HuAe90Eo6MBi9r490LhrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=bMmtTbsEqUOSt42JfOL1Z94L6l-zedfPgJTd7-tYCC5GMR8HQFG17-jwS8nbMCfw4AnMduWGAqm-4W6iz4qHTeZ0v_CbtnvM4Xxuk4ytsOtZRJ2dx_irhD7iOEEUEcF0XHzH47tZcMBxt6zza2zs_CsnfkSpDD1pfpmVO5X6pkNdjSwPft39JQtfH6FetWYqX44YHlrD0pDEXGQkkuZ_QkN7p7rtv0pECBaUG3QI7dZD1VSGCmFgJ6A2Y89Tda7YhzLS0aw_rsSRNvrYnNzJhfGvTtxM5LxuY9AGxDTAu2MO2kxxjNbYvFo0LMnaX_EyqZEasZ36U1OInVCqGPU5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=bMmtTbsEqUOSt42JfOL1Z94L6l-zedfPgJTd7-tYCC5GMR8HQFG17-jwS8nbMCfw4AnMduWGAqm-4W6iz4qHTeZ0v_CbtnvM4Xxuk4ytsOtZRJ2dx_irhD7iOEEUEcF0XHzH47tZcMBxt6zza2zs_CsnfkSpDD1pfpmVO5X6pkNdjSwPft39JQtfH6FetWYqX44YHlrD0pDEXGQkkuZ_QkN7p7rtv0pECBaUG3QI7dZD1VSGCmFgJ6A2Y89Tda7YhzLS0aw_rsSRNvrYnNzJhfGvTtxM5LxuY9AGxDTAu2MO2kxxjNbYvFo0LMnaX_EyqZEasZ36U1OInVCqGPU5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=vUMQH7R-8QmmAep5iV5CV0DZkMIPtRN9kK9Cb2of_dKMfrXg4Yyrl5F4SBOWLz9cV0zJl4hSsXzLL45O-DrMCWipI5bK--rrC4JNfoEJjUfeyFwlWf-YX0L5AWoPCX_1M7jqrmVmiMLa4ANAUJZr4-VkczN9Dk0svbZg4XXZKi8nL7gFHWFNnvZB4IW65Ct0Q5BHaXIejjD_pR4iQWRe6X5971DWS3pnBHknm66sQRhvQ_6MKVy8zqaG0PSxEB1ABgmogR-eUcRURuR2IrbMOx6ACvn6ja9bpXBPpjVSfIoFW0ZTJg1HjVb87AqwGxTzMmAMcLrF9gnHYD80Ev6mcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=vUMQH7R-8QmmAep5iV5CV0DZkMIPtRN9kK9Cb2of_dKMfrXg4Yyrl5F4SBOWLz9cV0zJl4hSsXzLL45O-DrMCWipI5bK--rrC4JNfoEJjUfeyFwlWf-YX0L5AWoPCX_1M7jqrmVmiMLa4ANAUJZr4-VkczN9Dk0svbZg4XXZKi8nL7gFHWFNnvZB4IW65Ct0Q5BHaXIejjD_pR4iQWRe6X5971DWS3pnBHknm66sQRhvQ_6MKVy8zqaG0PSxEB1ABgmogR-eUcRURuR2IrbMOx6ACvn6ja9bpXBPpjVSfIoFW0ZTJg1HjVb87AqwGxTzMmAMcLrF9gnHYD80Ev6mcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=j4rVWmoXrvsKNV0P3oRtfbY-NONBMZ_fXY6MIjUBUrq4O6_F2NIdx9Na6wpgTp-xX0q4jjJ9PN4L-Nj3tmTMyobcF8pbgHLVf57iW05uDSVQ8-4Wu_m0s5GOPReBEYEYF9tTbR944_StJEM1D2nFDrn4UEhdJtS5bKZVxP0IudZyYRZ15r8PEZHKECoCC2XouDZXVVvM8WJgqySU3tFvdCNexRu_KgD1zttuD7_YJ_SEHfYYQm3A66lEV__oUt6W4-2mYGPEwmmzh8eVZbnmjkxoKYdhBeRgV85OVsUxghn7W2ZuwgwEDtSNz3cBv_M0P0gxrLYFmo6GXhEAyD7f9ZMeEdbrO1o3q_BIJQaqKVmALYbUy7rbpAqo4tNEt2Wp86eaeRshF7-fNdu_Z7u3U1U7TZsSYyaHxQUGyH4dv0yXfjB3B3WgBkpT7cbJxO9na57NTAmJnQ81cNRFXMzhwObsHw8rEoV916Kylv2IDpSb0dLIGozAnqYLHSQNIr6UEp0t4QJP27TYyStDrexGbBDyhKcNUcIpGqwQJ4cs2hZJs6oxxSkS2yTkOJba1rOnZ8I3oIFcImjjboE_XzGxrnZLcsXt_rq2NU5u8tPXEu0yz0Dn6pfOn5ialX5I4gAkYf2KHBlHdwMaTBO7ipq61Rc7_idoTVYQsahn5OB7hgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=j4rVWmoXrvsKNV0P3oRtfbY-NONBMZ_fXY6MIjUBUrq4O6_F2NIdx9Na6wpgTp-xX0q4jjJ9PN4L-Nj3tmTMyobcF8pbgHLVf57iW05uDSVQ8-4Wu_m0s5GOPReBEYEYF9tTbR944_StJEM1D2nFDrn4UEhdJtS5bKZVxP0IudZyYRZ15r8PEZHKECoCC2XouDZXVVvM8WJgqySU3tFvdCNexRu_KgD1zttuD7_YJ_SEHfYYQm3A66lEV__oUt6W4-2mYGPEwmmzh8eVZbnmjkxoKYdhBeRgV85OVsUxghn7W2ZuwgwEDtSNz3cBv_M0P0gxrLYFmo6GXhEAyD7f9ZMeEdbrO1o3q_BIJQaqKVmALYbUy7rbpAqo4tNEt2Wp86eaeRshF7-fNdu_Z7u3U1U7TZsSYyaHxQUGyH4dv0yXfjB3B3WgBkpT7cbJxO9na57NTAmJnQ81cNRFXMzhwObsHw8rEoV916Kylv2IDpSb0dLIGozAnqYLHSQNIr6UEp0t4QJP27TYyStDrexGbBDyhKcNUcIpGqwQJ4cs2hZJs6oxxSkS2yTkOJba1rOnZ8I3oIFcImjjboE_XzGxrnZLcsXt_rq2NU5u8tPXEu0yz0Dn6pfOn5ialX5I4gAkYf2KHBlHdwMaTBO7ipq61Rc7_idoTVYQsahn5OB7hgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=OWan_aKKX9Wt_n-Te7fEajWXqk_vuVLu4x1Hs1-rp8XDOspaKhZ7E_YovDYvC2mw62cDFMHOrZQwtJCuhIVqYjexVosGIHHwWUTDKifnMFjDFNB5q4E4cGVQRvyA3IJmIvXmDzl3EXRcDhqBQqEn61eoFV2ChVhGJ-Bo3au3PC4Xej7Sd-FMjgNNv5-cOY4ck785qOZjivV_0wHXxewQGoFCbD9br2Csd_9C3h4_8qf9S58G3jvAWR9tBcDfCY_E2O7dzRJqhK9HP4aIhvneqTGSKh9pL3F2K5uWiPETezfz5x3G4KP8CFDhnQ5LbPuMZDregjY5QN937b9nTr58YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=OWan_aKKX9Wt_n-Te7fEajWXqk_vuVLu4x1Hs1-rp8XDOspaKhZ7E_YovDYvC2mw62cDFMHOrZQwtJCuhIVqYjexVosGIHHwWUTDKifnMFjDFNB5q4E4cGVQRvyA3IJmIvXmDzl3EXRcDhqBQqEn61eoFV2ChVhGJ-Bo3au3PC4Xej7Sd-FMjgNNv5-cOY4ck785qOZjivV_0wHXxewQGoFCbD9br2Csd_9C3h4_8qf9S58G3jvAWR9tBcDfCY_E2O7dzRJqhK9HP4aIhvneqTGSKh9pL3F2K5uWiPETezfz5x3G4KP8CFDhnQ5LbPuMZDregjY5QN937b9nTr58YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=l--d_sWveyHDj_KizZn6vreAmjk42HSOANLGaoMzxO3vaOh4I1Z65O6iysESiNUmr5JfvkQlnL556OeHpIJggU54z9i9SrIPbtNihqCCjclsdNh6uHSc8OezCe5Z0cSK6h3i7D7UFgGBNF7hXNkuHHFcBD4kRw3TKSgvArMHpKYl0_KoUHHpY4ll81Em5xHq1ZX6YIN94gXAwXTPp2tu1jyDoZ5wYybIF2Seeqy_yyknlGtcBxAfBxzYaEW8j28KLRGjXWy3iADYLCWZUe77ViAGS9YZ81X3iwhQBirW4licbbKSHKBGvqtG_V0vrg6bkKHtuLZlgtJ85tCdp7uNYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=l--d_sWveyHDj_KizZn6vreAmjk42HSOANLGaoMzxO3vaOh4I1Z65O6iysESiNUmr5JfvkQlnL556OeHpIJggU54z9i9SrIPbtNihqCCjclsdNh6uHSc8OezCe5Z0cSK6h3i7D7UFgGBNF7hXNkuHHFcBD4kRw3TKSgvArMHpKYl0_KoUHHpY4ll81Em5xHq1ZX6YIN94gXAwXTPp2tu1jyDoZ5wYybIF2Seeqy_yyknlGtcBxAfBxzYaEW8j28KLRGjXWy3iADYLCWZUe77ViAGS9YZ81X3iwhQBirW4licbbKSHKBGvqtG_V0vrg6bkKHtuLZlgtJ85tCdp7uNYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=MrXXI1r10l1fhD_SIEimpN0p_jRtQuhzvr2NjIoygC9JNu8DOnHljGtWCP7XgP5-QQGJu1kbAxVAqj5-1Qhxmr5Fbu4uaAgHYYQT-rDqesczgPby69ud_dbBhL-zeuVTAghkAldx2kU06ABeTOdD_cmZe3D06E07M7MiG711yjlE1y6ZyaWQ7W-U29x1_BSG-_9c7p3SpjJE-mkWgtm3nDrrBBExBPvmn_DfO-ijWRjP-qVJB2NaIUzrzfGLmrkXYynQFNH2Ab5rMghTEITY_fClY_VxOOmtWiX1kLGNjeT5Du1HiSlku0Pw8AtV287lvlHpeMJErVXl7Ph2JlM-0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=MrXXI1r10l1fhD_SIEimpN0p_jRtQuhzvr2NjIoygC9JNu8DOnHljGtWCP7XgP5-QQGJu1kbAxVAqj5-1Qhxmr5Fbu4uaAgHYYQT-rDqesczgPby69ud_dbBhL-zeuVTAghkAldx2kU06ABeTOdD_cmZe3D06E07M7MiG711yjlE1y6ZyaWQ7W-U29x1_BSG-_9c7p3SpjJE-mkWgtm3nDrrBBExBPvmn_DfO-ijWRjP-qVJB2NaIUzrzfGLmrkXYynQFNH2Ab5rMghTEITY_fClY_VxOOmtWiX1kLGNjeT5Du1HiSlku0Pw8AtV287lvlHpeMJErVXl7Ph2JlM-0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=jgv20c-394_SArnLRuKxC_7xmHw3CYiwSELNo5Yvz2ewVKVrpPwi0cMuDYrK7UPUH4as19_zWq33acdVHvZpX9CgBpjEkUZLoQa9GvXCH4Oidbkyrd9PbgCA4_9Zy3o4H6thBvPcmf6r5hXYtHa6H7HDc4WIhHzWS9RyTLST1jCRrFpUIrV-r41RzIXcT7XYF-evSrYPvF1WB7a-PhyFgDiEzma65jYve5gHOLlRfIzO5qHiCoc1NkGuwP9DTd5odakBNulAzzPZIyXqdJ5pczThcS3yM_cdPFkrmeIFj3OgqLb5Qec82nS_hB-xUCRXjPOxgdFDCWQcss0HMEHdJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=jgv20c-394_SArnLRuKxC_7xmHw3CYiwSELNo5Yvz2ewVKVrpPwi0cMuDYrK7UPUH4as19_zWq33acdVHvZpX9CgBpjEkUZLoQa9GvXCH4Oidbkyrd9PbgCA4_9Zy3o4H6thBvPcmf6r5hXYtHa6H7HDc4WIhHzWS9RyTLST1jCRrFpUIrV-r41RzIXcT7XYF-evSrYPvF1WB7a-PhyFgDiEzma65jYve5gHOLlRfIzO5qHiCoc1NkGuwP9DTd5odakBNulAzzPZIyXqdJ5pczThcS3yM_cdPFkrmeIFj3OgqLb5Qec82nS_hB-xUCRXjPOxgdFDCWQcss0HMEHdJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=TAqQGn25p_K0lSRhHcYl97kT_DBSSA3i4LCA2gALG3tm-hrKDpupAOZ-WD7VEy5gcuT7pRgupYUT12fm-ryTpm4sBU0Djh_d57alFjhgDgMaPx9ilaQ0EEAMkQabNDLnX1-hg3jUeSg_pZl5_dC1FL5ZFGxrwMXMG47RJg3SlvoEE4tCjx6x9-t_ua5FIXcVW_lQvhct_RPEg1R5-foAPwmKP-kF6bLF2afXRl7bX-pP-BUPFQaF6YCB9wmitodKrypilE5bQwFx6viuf2SlavNTnbnA6xh-Hl0JjX5cVPSkpSQjQeePESXEfKsaikKDg51BUPhphJeBa-bb9hDCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=TAqQGn25p_K0lSRhHcYl97kT_DBSSA3i4LCA2gALG3tm-hrKDpupAOZ-WD7VEy5gcuT7pRgupYUT12fm-ryTpm4sBU0Djh_d57alFjhgDgMaPx9ilaQ0EEAMkQabNDLnX1-hg3jUeSg_pZl5_dC1FL5ZFGxrwMXMG47RJg3SlvoEE4tCjx6x9-t_ua5FIXcVW_lQvhct_RPEg1R5-foAPwmKP-kF6bLF2afXRl7bX-pP-BUPFQaF6YCB9wmitodKrypilE5bQwFx6viuf2SlavNTnbnA6xh-Hl0JjX5cVPSkpSQjQeePESXEfKsaikKDg51BUPhphJeBa-bb9hDCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=I-0lCIbN0SN321xVfetxDXdZKavBHIDqxAnG1yuFsk2H-q_ezdEUokLz4-CoHKEPa9lFbZqDts6YLBNT_uhdEtIun4smXfxEUBpwYYZpbm687Po2EDNHGf4SDAEnh2RY4TWMl6ry6WGJiKSBxz_gJ9kn1nEVRO2Yn7uf8kFHYNdlsCWfNy1GnAF_aXtVPgGGogbnTOuPWG-vpiYTFxmYmDhttmyOHw1lUgtKGozzydUZ-6d19zTbuWNPZhLMra_RL8Jwze9vbI_s_xGcU5fruKE6YYoxrnz6dEDQ5iwbNLJy_o3hmQS9bbGfBZirxsnv50fMD6bO2bCgTV--HNht_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=I-0lCIbN0SN321xVfetxDXdZKavBHIDqxAnG1yuFsk2H-q_ezdEUokLz4-CoHKEPa9lFbZqDts6YLBNT_uhdEtIun4smXfxEUBpwYYZpbm687Po2EDNHGf4SDAEnh2RY4TWMl6ry6WGJiKSBxz_gJ9kn1nEVRO2Yn7uf8kFHYNdlsCWfNy1GnAF_aXtVPgGGogbnTOuPWG-vpiYTFxmYmDhttmyOHw1lUgtKGozzydUZ-6d19zTbuWNPZhLMra_RL8Jwze9vbI_s_xGcU5fruKE6YYoxrnz6dEDQ5iwbNLJy_o3hmQS9bbGfBZirxsnv50fMD6bO2bCgTV--HNht_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=iZ3j08sJVzAqAQvnvmi1DgQpEL8sU3DSygw17iHBdqdED4LFyqFiQeb35KkbAIdC0T5MKDWpD2BEcF4_FVOibbYdyn4CsrqHlIEvpuBHSSYzJWueIeCaZEmhi0Haem7qiazceR-8e3yA6NeGCKh6QHghKnznZjdsl5UbMEMW6H45GEpwxi5R9uRpZlIjYLWupGETBaPgRdkavXsjcvNSMmH7lV1VS6q_1-KlP589EWe6CVHibMxoDOOs99uEzeAcic_22LR9W7dUynY1QTxaqiRvYCqlZ4xeoYEqj0G-GGSICsHeNKp4n2fw5PofCyJ7g4QvSi-hj-xM8OevOQzzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=iZ3j08sJVzAqAQvnvmi1DgQpEL8sU3DSygw17iHBdqdED4LFyqFiQeb35KkbAIdC0T5MKDWpD2BEcF4_FVOibbYdyn4CsrqHlIEvpuBHSSYzJWueIeCaZEmhi0Haem7qiazceR-8e3yA6NeGCKh6QHghKnznZjdsl5UbMEMW6H45GEpwxi5R9uRpZlIjYLWupGETBaPgRdkavXsjcvNSMmH7lV1VS6q_1-KlP589EWe6CVHibMxoDOOs99uEzeAcic_22LR9W7dUynY1QTxaqiRvYCqlZ4xeoYEqj0G-GGSICsHeNKp4n2fw5PofCyJ7g4QvSi-hj-xM8OevOQzzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv4tCTpb6uUaJ5PInB1UcKL5J8bRdLM2fHNTBwxaTtmfssBbsAdToxP2IGHR5wa0olG8rJfu7LkwD8wGqQH0aJh0lHTvC0_HLU_O8Wl-V4up1Et3aOLUrvTYCj5bG7AD2iLiYMiRcfBX3OMA6YzRySEm-LAUuGDSGe23oFDkR3-3pyYQ46UUXEVp3EHoqZKkDtH7za07cSEPaPuOmE-6VlFXVPT1dkl-d5ulNOqJHqc-j29QexDtd3KTzBLS6ZpFirtRSFabSQR7d-wQHzHf6yaAzdXlKSI1afNWDGD2vdTXYGsZ5O3_Mb09N4eSHGSoUuyDgTsaCsTtIxUkdVEAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=UgcUXOHg56gTyUrn2yaA_Pvbplzk6pHDWczAv8INoX8YJ13HW634V7HefPcjoiIm_Xhgy0_Mme6mbszzkazjE1eR_HTiQEpQ9DCuthZlw_N30SSE2gvNjgtxjLEf2bemZ3-C2fY9A0Ba6BhOwc4Z-KPPuPw0fBe22q7oHmRVZw46Fxar1ICME53DheDm_Z1mK5rudPrvgljpf6Gjv5OgI98g6h-F1uPJ0-sTVxK880ExFVhrNJWhyY_1B0JZ4pHb1VJTRSjbXwYH9KrAH6hZ-1_YCuFCVqTcz7GinkR-OWVUfCt23sK26vWiNBr3wfoTo3bwxK2XODRRQU6uHvhpcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=UgcUXOHg56gTyUrn2yaA_Pvbplzk6pHDWczAv8INoX8YJ13HW634V7HefPcjoiIm_Xhgy0_Mme6mbszzkazjE1eR_HTiQEpQ9DCuthZlw_N30SSE2gvNjgtxjLEf2bemZ3-C2fY9A0Ba6BhOwc4Z-KPPuPw0fBe22q7oHmRVZw46Fxar1ICME53DheDm_Z1mK5rudPrvgljpf6Gjv5OgI98g6h-F1uPJ0-sTVxK880ExFVhrNJWhyY_1B0JZ4pHb1VJTRSjbXwYH9KrAH6hZ-1_YCuFCVqTcz7GinkR-OWVUfCt23sK26vWiNBr3wfoTo3bwxK2XODRRQU6uHvhpcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=gbHyBW1hYDfrS7OyXge0HLy0jL6AOKYkHrAsxRV7Kq8tr0XiSeqYVujSzCWG0lXiFUmYLI8r5D2XASdYRfzba-dgUpdX3zrdsJEzK-8hrgTw2Ox1S1wI0PYq-luNxFTrBH2PiLaPR_sIefrXwx2P5Kcy3PGHn5UkoJXBK-C5s4uHImoWwOlgcfl9QJz-SmLvzGW24uQ7LuUAXipO_zCM7JUYx_yZqznG7_ISMd6P_Rzncjb-T61ipP562Epc9K-BZZs7ji5viQKV1a58HSwqDzpRJO3fB7WcIHX6ANtD3UDWuy9k6E8vjwEjQI9Ad2YdDvBRA_R2QdWQxP3jWppjjUwjqsebvwcjQRr1UgSbUFXdiNsdxman6FtBANq_AxLVSyJ1_c6Zed-Gfm_47K8Dq7Bxxn0upj-NxA7fi-EueD5rcSAcd6muCxbh4BEksoUALiFHp0jXAR768fvUOsjA4Zw-isx-gmuEkdZMM8CKqnRI0R0wRs0tuZqdpXhLq-lEbK2dIKs3GFo9GgKML7-0W0BWiUwY6of1Z2jU3ZFVu_InWeKvwFgi9ihSlYlZagCPdq1NxQ22MrgyW1vF3CMjmBNxBoA1qUzH2FtseoQUBE199fPVDmmjScuw7J_VFt_VffKMFSarXqBPQTCc7c3IS9XSZQNykzP0rFQMbLBl_IY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=gbHyBW1hYDfrS7OyXge0HLy0jL6AOKYkHrAsxRV7Kq8tr0XiSeqYVujSzCWG0lXiFUmYLI8r5D2XASdYRfzba-dgUpdX3zrdsJEzK-8hrgTw2Ox1S1wI0PYq-luNxFTrBH2PiLaPR_sIefrXwx2P5Kcy3PGHn5UkoJXBK-C5s4uHImoWwOlgcfl9QJz-SmLvzGW24uQ7LuUAXipO_zCM7JUYx_yZqznG7_ISMd6P_Rzncjb-T61ipP562Epc9K-BZZs7ji5viQKV1a58HSwqDzpRJO3fB7WcIHX6ANtD3UDWuy9k6E8vjwEjQI9Ad2YdDvBRA_R2QdWQxP3jWppjjUwjqsebvwcjQRr1UgSbUFXdiNsdxman6FtBANq_AxLVSyJ1_c6Zed-Gfm_47K8Dq7Bxxn0upj-NxA7fi-EueD5rcSAcd6muCxbh4BEksoUALiFHp0jXAR768fvUOsjA4Zw-isx-gmuEkdZMM8CKqnRI0R0wRs0tuZqdpXhLq-lEbK2dIKs3GFo9GgKML7-0W0BWiUwY6of1Z2jU3ZFVu_InWeKvwFgi9ihSlYlZagCPdq1NxQ22MrgyW1vF3CMjmBNxBoA1qUzH2FtseoQUBE199fPVDmmjScuw7J_VFt_VffKMFSarXqBPQTCc7c3IS9XSZQNykzP0rFQMbLBl_IY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL9sSSGSTyMMzfoOiKNiQlqXOxqMj1hckL9nBCI-OZrdex1sD6kf0yU7eXN6TDIkU5LC5FJXNpNmrD1L4Qds6DMUw7PB7GAtgrtx2yYLfyX41FQVLyXqrtg6j8cWVseHFYdIMuWNsmwrUjJ5QJ5-cNG1ldMW698APpVkTIgITD7wDfPXj0DcjpVS-whZxAlwzi-zwxFAXjmtYPdh4yhSVFViold5NCCZRdX0MIXXg9T4MUYW3OCdZjyqaLSPnL_T2dxesMiSb-8ELXvMLA7t50IcVmMNN_e_2RJXmdkvRuHVaC60nRBdkqOc4McZnC8ediQs84klq-PQkqVPU7OUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=fgRlxNrnI8Xpmb61k-oxvIuA74EKJ00fvcnT0TBwYhbASCA84kWyyf3l7fZOiM370T2tfgDMYDiVeELy_jdzn5Od6kQAxUhUI6u9iikhc2qz1TTFipvoUOcoe9D9mfTkn7s3RBD27owViyCX7Z_Xdcq7mUeOom-PwIW95wIttt-zJCrHiEylKvM5TnCZAQehvIoFvFpcIcXANKx7Bh5nXUCRncMJwxoUJzxqEJ1L6a4lHhSznOqdbeqilmD2K8LeVGNDEhefCF_ygnKQW8iU0d9P_M3Yy8kvPzDyouTxqEUz2Ypuh2Kcxsc18-vMWV573K35jH1io5U37IIVpI1hOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=fgRlxNrnI8Xpmb61k-oxvIuA74EKJ00fvcnT0TBwYhbASCA84kWyyf3l7fZOiM370T2tfgDMYDiVeELy_jdzn5Od6kQAxUhUI6u9iikhc2qz1TTFipvoUOcoe9D9mfTkn7s3RBD27owViyCX7Z_Xdcq7mUeOom-PwIW95wIttt-zJCrHiEylKvM5TnCZAQehvIoFvFpcIcXANKx7Bh5nXUCRncMJwxoUJzxqEJ1L6a4lHhSznOqdbeqilmD2K8LeVGNDEhefCF_ygnKQW8iU0d9P_M3Yy8kvPzDyouTxqEUz2Ypuh2Kcxsc18-vMWV573K35jH1io5U37IIVpI1hOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=lHmI_Dc3XUBMq71vBW7_HKev6jognu49UmCe3GKLqhuxCAKqWGqcqE_GJIStYzw9N4w27h7UlVe71m5hH5_lQYUCp4EJ7t4M4Z4UcKQleGtnyEnuFL6eUGTFgDFO-H4ncnMXIvJMDqGG03WYmzxN-7OXCv-TCFY6rLKBY5--FbAERCfEfxEPysJWiYt5vBYMU1sxZaXlG72kEq9DjCBQqt8RuJrP0ZvvhPx53PW2Lb4SivCnhprtlZBQqXmgl8DZ0VkvyqaiAqSbZy9HPcUzcSQdeuDDav-Oy-0hHbVLQrEzPN8yxlNAqT9eLT5bW0HAsE4m8hvC_FCd59kDNt-xyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=lHmI_Dc3XUBMq71vBW7_HKev6jognu49UmCe3GKLqhuxCAKqWGqcqE_GJIStYzw9N4w27h7UlVe71m5hH5_lQYUCp4EJ7t4M4Z4UcKQleGtnyEnuFL6eUGTFgDFO-H4ncnMXIvJMDqGG03WYmzxN-7OXCv-TCFY6rLKBY5--FbAERCfEfxEPysJWiYt5vBYMU1sxZaXlG72kEq9DjCBQqt8RuJrP0ZvvhPx53PW2Lb4SivCnhprtlZBQqXmgl8DZ0VkvyqaiAqSbZy9HPcUzcSQdeuDDav-Oy-0hHbVLQrEzPN8yxlNAqT9eLT5bW0HAsE4m8hvC_FCd59kDNt-xyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=IjFyeHDYCjelNBid3IO4njmAvVcD1h5jE6vGwNmDkRflTaX-i8RhDVuA0r52nGUScX7sOBZ-Y0xzPkY19Od-2cywtlMyKxo0DQZiJnjvEOAGFmSmT-rknB4NsJf8tXJmD5QFa04VVT9X5j5w48F5t8Y8kV1lD_sH-T6ZizIsNpY-CvIau4o68Rcmld6s4YMpBFjRotcp1iClUM0VDz4JPfN2F3H3Pp-4DePPcIffgbnmyda0yUA7BHyu1UE-3w6CJsYDACadrzqCMYtl1CNdwzOiBYCwn6IibV4NoVg5GEnSyAn-pOuZDPZtjw2qC0XWtntQC-OH7cYw4Cq8IJfuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=IjFyeHDYCjelNBid3IO4njmAvVcD1h5jE6vGwNmDkRflTaX-i8RhDVuA0r52nGUScX7sOBZ-Y0xzPkY19Od-2cywtlMyKxo0DQZiJnjvEOAGFmSmT-rknB4NsJf8tXJmD5QFa04VVT9X5j5w48F5t8Y8kV1lD_sH-T6ZizIsNpY-CvIau4o68Rcmld6s4YMpBFjRotcp1iClUM0VDz4JPfN2F3H3Pp-4DePPcIffgbnmyda0yUA7BHyu1UE-3w6CJsYDACadrzqCMYtl1CNdwzOiBYCwn6IibV4NoVg5GEnSyAn-pOuZDPZtjw2qC0XWtntQC-OH7cYw4Cq8IJfuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
