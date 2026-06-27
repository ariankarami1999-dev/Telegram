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
<img src="https://cdn4.telesco.pe/file/HWYsdFxfi_56_sc7WbMUCbGMdc9hAyiS0Zc6Rh8SlhvEwDLi57s6ysXxi-lIvJNqnib3zik4WTo6RskMaRyCWgiSEmGBmM8jferbvsTs9fXktAEu1x7du2YwfHuhrIuYGapIfpO6MCNnLD3aLDxlUKvHbDx9DZm8xMkTuP8y1XPFVFAd_6HIUFIqy8AqZ36KxawuTQBXrioDhF_epjWdC6Op9GLqLBLIcwoaWKNKACRM3q4nL0MbT6224KIMnvlySIcyMi5n0qvloER-tA6zy6sZoY3i240AxblDcSJkLqLQ7vchC_p3-urQkaG7EJbjIJml8C1QRXSH99ML1yUTIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 21:36:08</div>
<hr>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Xc_LHU5kX9qvM-SpQAh2EshjvsMFi7QnIMN1kD9qUR1-jI2-HiOGVpXYO7yxB2RAv7jtczrQ3j-Zr_L_qLJRIFaYWrHBADel4q4X6tGE65a-CT62TF4OkYON0CUmiseLoOdlxaMJ8zTvEvrEFLEqdBZPRZTpk1PxBz4w2L5KmBwNpuJj3GNyVfRZoF_WNoZK0rt03DYOMeZFDRdQDZmGV9HnAh1NK2Nv-4X6c3dCeA-ccM867HTqa7vuK_M3oOWLcfnCaCrVLROCOdKynTBH8xPnuWxBGfCxfKLTx1XRYYRt_Suc9U0Ufncstv4hnR5Y5lYmGPqcc9exnbHDazUydQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Xc_LHU5kX9qvM-SpQAh2EshjvsMFi7QnIMN1kD9qUR1-jI2-HiOGVpXYO7yxB2RAv7jtczrQ3j-Zr_L_qLJRIFaYWrHBADel4q4X6tGE65a-CT62TF4OkYON0CUmiseLoOdlxaMJ8zTvEvrEFLEqdBZPRZTpk1PxBz4w2L5KmBwNpuJj3GNyVfRZoF_WNoZK0rt03DYOMeZFDRdQDZmGV9HnAh1NK2Nv-4X6c3dCeA-ccM867HTqa7vuK_M3oOWLcfnCaCrVLROCOdKynTBH8xPnuWxBGfCxfKLTx1XRYYRt_Suc9U0Ufncstv4hnR5Y5lYmGPqcc9exnbHDazUydQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=dTJK6tB7y1wgm6VJNlqLA3Ahf6ZZJbxSoY9GoizoEfiNT1Jug1T_hM3lvLoD1cQ-NaIHGP0p2tzWeOBarXxUeGLQFXN6iuvVq5wDcsfNraW8Ie3dUwf24SUsnC6z-tsxPBSXrqS0BqLf2VmjLWPBbyIQQEN6pZZ8Iib6t68UmCQdtgXS5Fv7X4POEL7JB9-Kl2FpYVD87E0HCS-I0iUGKMww08UhjYsmCGy_p8x4zUrs9Z_bJ-6B9z1X070sYiDAoEbZlCHtYFJ6udAKwOxrhIf0oikuCv3ivzuBc8X_8jUrfAsevbhsblqLjML9t2VYZ3ht3kIClF9dQ_Acjfb2Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=dTJK6tB7y1wgm6VJNlqLA3Ahf6ZZJbxSoY9GoizoEfiNT1Jug1T_hM3lvLoD1cQ-NaIHGP0p2tzWeOBarXxUeGLQFXN6iuvVq5wDcsfNraW8Ie3dUwf24SUsnC6z-tsxPBSXrqS0BqLf2VmjLWPBbyIQQEN6pZZ8Iib6t68UmCQdtgXS5Fv7X4POEL7JB9-Kl2FpYVD87E0HCS-I0iUGKMww08UhjYsmCGy_p8x4zUrs9Z_bJ-6B9z1X070sYiDAoEbZlCHtYFJ6udAKwOxrhIf0oikuCv3ivzuBc8X_8jUrfAsevbhsblqLjML9t2VYZ3ht3kIClF9dQ_Acjfb2Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ialgFhCO0J1ZtPdQAHYBKSWHdoSo9Y_1o00Gb6rLgLndnxo6YmBqWdM7edJXkjw_Jqpi4RLXT9tgR79wlSmstbS9VbeL2HzPUyU9s3_-5oB1gmr9UjGw44SsTlNnFdgoYrqEdyniXNauv9I4ewKVfFQN8AHZAZAHhwh-C8cAVLHsIM0BkiEYwN5IdrNeddfMu_tIklZH2nAkoPaSx94mSykTpIXZb29Sxrmdyigsrhqp8e6qfqCqR-GSQqHZYZJNtyF3x_3TJVAlCkdyQD8EInLZ8a5FbVGSwcrzikEXs95Efd2pJr4exc90-DetnjT1Citqnt46xpF6Io3zL_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWRPilpdYp4TkEx7losxXvM_PtTClcQOmWJk-zIdDOBfLjFXbFBtujRZm456BMNSO9vXiqvlM0t_17gsFfToVJCTUvMdwdbO3TMtG2SXvSGZDB0KxtOTSTlmDqRL_aD6RZUABMavd9O6uSfSK-dbaPcSJG-1TCm4ir8CPOaaAFKuRpUZ-elfV5ZYfGhcTxxMXgvVXg4c7YZnFk38fvbYvR5ZoPjqPgT9Mlh-eUxwYrPp7IZmKrT7SYIBA1Mqs05HKwVnNMpgOF8yyW-xPFtu2f_L-TD-IH8BBbN2GcTvcrernGe5gnvVpFaeMX9moNRzz_TD-bQgBIR_MmQrNAEHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEwIbrOCZ7ZjwAJTBgzGPmOQfEQfE7tko6GMubk8q4M1wnuznKgx2Ye4GQ9-moA_ILqiOBTnv_ztVXDRppuO-OJJroskl2HPzWE0yxFUZiz2xydCJqZlPiDKAITlM8SeBdSA_qpPqutchNNdoAW2kigsrfFtnlprUSAxKGj5wbNy2ce_kUQTbzGX50ON6rkvAW1ziOJwLOy-MrcsfBtPTrh-elzk5OeOTcsnLIwsKqU7xY5JJxR_Nkj6ebdCIUinijIPJYfJItjH7DTgr5psrHiiXZ3y6Kmfs9JipyRL7ZytmRPAqwqLpack-WwagAyEnCPkREMljq_6J5Gm0CC5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP6EcUUYKdIuG6uv_wDins9AJYHsyY-GYxxbFs_VZLn8TCRh8bFKHBpvqLBWvLWdYSTcgpH46ngeL2sEC-6iTjq0ONjJ3nERaKzW-_DdoXuOgUIXBTuYyjpPowpOXvsi-CRlUfXmqn43WPJPusVJyh8tiU5zO4VL6pxcBGAX-OJeKAP3sNstp8nhZdno8BXBsRKacgXBxoQKJdJqKAOE62lGsh2_yEAqWwlSgZ2o0zRKi2tCM0ErS9U0m1v2s9bCECqusOmKsUUqtG4DCyHlY6fSBa7-kIXraX6_IgiU2MVY2dRKOo2VFAwVAz9SdqVzHbIVz6GJ1ehtaUp3ImgJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yoxtfii8wIqr6Mt5hpI-HK63nYZWB0TuBnKiBE2d-c5lx_pP7tFgSY_WY-ipSif2MxgfYGoKF4rv1sSmL-w0ayY3PJO9PduUz3P_vy_FJ6nF0lU1bO_LPcxhVaoriFYkYO6JxYPkzaLa22HgPcosLXcSpJDEYS1Qo9kuJ-TygKA5ByHKTXyvk1caNVxSux-nazU75iUNPMAzYOxAUhifpo0P1iFwfHLjgJFArp5WTqFkq0E8gV6-JkP5fI5tdznj6ej-WQxSlLMG858sxV8XwqfEQbO_IR5sVMusI3Vp7msgySqXQdVVhNCPYH4Fj9676x2XpHHc09buWUATO6bbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=sRHijjOUWuK9mSOgpCA0-uRtaBoOzKpveCy4zincI-fAXuZuRhUawzg8DjtDdF7xX1uif_7DILm3T_01qppsvyfvfvlOKK3T9aNCKgCDtViWFodfKVeSnsDvSfNrSw1_R9FqUAji4rGrLz0JEzvUtsBVgWlsismSNF3ovYhZp3a7okgcfy6FgvnX-0WPbz9C1M5yBiiEI2tGLZQ1oMjuqXlWTB3aoHbhqOb3gCJEQdZcnsnKATP8H2PXlTKW3ykfEP6NJJBYXzCY2v0fNNloXKHs9ZwBREi70QfK13nPu9y28c0P1NLAYd-lnvwJ0aVBNJP-BtmJetmZjhmg0p5fkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=sRHijjOUWuK9mSOgpCA0-uRtaBoOzKpveCy4zincI-fAXuZuRhUawzg8DjtDdF7xX1uif_7DILm3T_01qppsvyfvfvlOKK3T9aNCKgCDtViWFodfKVeSnsDvSfNrSw1_R9FqUAji4rGrLz0JEzvUtsBVgWlsismSNF3ovYhZp3a7okgcfy6FgvnX-0WPbz9C1M5yBiiEI2tGLZQ1oMjuqXlWTB3aoHbhqOb3gCJEQdZcnsnKATP8H2PXlTKW3ykfEP6NJJBYXzCY2v0fNNloXKHs9ZwBREi70QfK13nPu9y28c0P1NLAYd-lnvwJ0aVBNJP-BtmJetmZjhmg0p5fkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=jA7555vCSne6najJJtqTcnZROAst9zWMasDTpv8Hs5h0B7aBep1zZAJF5bL4XUoBEL73-zoF7-nJDxjyCqqL6YSwBqiuVBknOX78IFR4Q2XX_Dh_jeztCAbw8FMag_2ocd3zt0SiPq3w-kQWwKEw8Yp_So-BZVEu3pbiblD4zBhY9ozzpu9vabkdwNrpYm9vHHzqASpH1zWB7s2eYK7Cc7QnLR_tpqzYeHIdIGAqq1zMowKj98g4jmGevR1F-OLmQym8s6aCJtIbACgMl_mJ-ooQBUABqZyjP56xcqFAG1ucJy3sVtDQ8E-KYmD9y5dZXL0V-l4l9ytdMuTr4t7GlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=jA7555vCSne6najJJtqTcnZROAst9zWMasDTpv8Hs5h0B7aBep1zZAJF5bL4XUoBEL73-zoF7-nJDxjyCqqL6YSwBqiuVBknOX78IFR4Q2XX_Dh_jeztCAbw8FMag_2ocd3zt0SiPq3w-kQWwKEw8Yp_So-BZVEu3pbiblD4zBhY9ozzpu9vabkdwNrpYm9vHHzqASpH1zWB7s2eYK7Cc7QnLR_tpqzYeHIdIGAqq1zMowKj98g4jmGevR1F-OLmQym8s6aCJtIbACgMl_mJ-ooQBUABqZyjP56xcqFAG1ucJy3sVtDQ8E-KYmD9y5dZXL0V-l4l9ytdMuTr4t7GlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBT0it7_jbWW-fFAp_fryTqBVOuLjKOCsVRFRXFpEziL2yv-EOfaPG6qfjoFDfLUYEkwBv_GDp4R3rESlZnoTxLo6tK7gjOmgqLGSQPXKxRuKpK59crOO5Iq0v68AL8kjAxGf3phQ_xMpH5EO2UwFGQ8QXWE1fLyEL9XbOCDcRVhZOno5TKAE_hn4iISteO83PxS-C-hssIq2HCbxZL8lMTINZ118fczb_8ILi3njjaSPh9PDnfsmtbBwBe6K68Y8eYTtcv1uG1zXETp6KbMPL_DpT_wrPf43WZlUunPIFDLe8HCHTDKhRivJkvPGHigrnfGGcKrfUV4uIb2aOhDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5jJixW8Qpp06pipNqujkS4BjaejcUcSGtBt8Vu0uzMlB5ofoewzN-_woGd2TUXK5tb6nSlNVWUsewaM67syqnT5dEwjp9bY_NLM2mTQQAmSLMHyS9qawDOoJu3881mhIJHVPPNJB2CIsncocaugZ9PDGgebC9jJxAKK0_bZhR_0pSH1UALCThwiGqGyza5DpKF-hB4Hxy4LGDHsvPBsRvXTKl_0iyXkpa332uvJzXOojBBlchbP36KCmCKWrHTJnp30nSS679y6FDf-FS6zs7mOICjpCtjtLvCM4HLJ7vUWAdzKQknbPgcSwn1NEvseUy4ryfDMtNgQCeHpUVhn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=o0Ljbrbu12aLYaoE0087nfw_cTXIZ8ABV9jmQ8LQUiYi79I8oTMd5Rz9Eq1ifHLPiUWXUuUYNG0TSmUH90zgDpmeCjrsHYbrWJgoEfv7uMt-yuCbXl5KM0Rs3zvUjtm-Wmzl7iJQK1UG86AkGQFBBbbyLJDiUTlChDGukKspXqqUOiwHPhOCxnluRGChlPW9K_4zlswAc6b89zHD966vjkQK2FWE3Hwz7jpKLgoFkCT82hj_2Bi7QaPWuJef4ZiNn99GPH-fvk8EwO6OWmvY-Yld7vQS6g-LTSOzOSBFm6W4Z_klymUGR3MhC5L-fP4-71OcdaNzF_dkNWEchnSY1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=o0Ljbrbu12aLYaoE0087nfw_cTXIZ8ABV9jmQ8LQUiYi79I8oTMd5Rz9Eq1ifHLPiUWXUuUYNG0TSmUH90zgDpmeCjrsHYbrWJgoEfv7uMt-yuCbXl5KM0Rs3zvUjtm-Wmzl7iJQK1UG86AkGQFBBbbyLJDiUTlChDGukKspXqqUOiwHPhOCxnluRGChlPW9K_4zlswAc6b89zHD966vjkQK2FWE3Hwz7jpKLgoFkCT82hj_2Bi7QaPWuJef4ZiNn99GPH-fvk8EwO6OWmvY-Yld7vQS6g-LTSOzOSBFm6W4Z_klymUGR3MhC5L-fP4-71OcdaNzF_dkNWEchnSY1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ezSoXdd7YLLk0NhcuqxJo6Y6iIYbT4R_gZ4oUitjXCLrNgtwsDGbITPo6l1wnSet4ZTgDMz9-W4t_VoKSLzOmDUjthkrCC0Na385wsyxnRY-Z25r2UWwKARhvIum1vc40mCe_1Or8eD_TSNmYC02mNXUJm4GvbLhv-tQV2rYGRHGaL81LdC3aiOXDAxn7BDdkpQd6Pg-tAmAjAcAlMr2E8Q9kMHhyITaj6EAjY-UmJYfWj5BYPLGO4WxwZpoY544aOsnc0tLRH-8zp2vFY5F4NSokIHgYF1y6WYqmsZHW0rCRwzJwIKfFMYZjvPp1TEwX-gzJzlMrId074b6RhvuSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ezSoXdd7YLLk0NhcuqxJo6Y6iIYbT4R_gZ4oUitjXCLrNgtwsDGbITPo6l1wnSet4ZTgDMz9-W4t_VoKSLzOmDUjthkrCC0Na385wsyxnRY-Z25r2UWwKARhvIum1vc40mCe_1Or8eD_TSNmYC02mNXUJm4GvbLhv-tQV2rYGRHGaL81LdC3aiOXDAxn7BDdkpQd6Pg-tAmAjAcAlMr2E8Q9kMHhyITaj6EAjY-UmJYfWj5BYPLGO4WxwZpoY544aOsnc0tLRH-8zp2vFY5F4NSokIHgYF1y6WYqmsZHW0rCRwzJwIKfFMYZjvPp1TEwX-gzJzlMrId074b6RhvuSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3GdT-95tGddin_VNSxZ_3SL-eDFZOQGtCuXhmnpKeB2WY8XImsVsD0XGF7J0aDIdihY2bS57EaNRKNSWtAte-W4HPbtcJPlkTUK5TkE7me0xsSJb_JeQq41GRg0KrXy-FJSY6fOh6lggCILfSWuoAzHmP4AJUgEay-oSRj57JP0aeHzUTbNPUc4z-cV0wwYctLU6-MlVre6hmyNFL5L2wAPMXb2y2S4BI3njr_9tO2BrjttoMAyfbAeksUcMUK6oh6INyyG8NlbQXnupfKWAnfclSa7ctjBtdPicHt-XtDpSu5qP4I1MKhyWhcM6YR1DxrKUxVSrPdEEdexyXy2mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tltr7ABqptHAh8p9h9fwG2Xq0m60FrpajtzKccQ-m-XQDpK9IBH5L_6VnCd-R2i5zEnxsGj9Viv7IW8qG3n2lA76Fz4LXS0A1TtY-t8vwbVtRJT5OAVfEEv-McdxY2UCIwDFL6PajmT4Cx6sbgllodPXCvkGB72_uJLLGc9vsMFTrI7mAnb2Se7vGf6H2Wt5tcRBhsIZEJvKWmX8u-6GxWMfTmFTMf1BNTzv3SsEJ9ahTIsDf6jdcmHTpsUreRldhbW9nOGpwjkfIyarBGC66vU3B5dNcNU73FqtqYV2OJhNAKbH9EXBGJ18vF0EUWv3umw4SR9gg8aQTFLG_4lzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRE26x28VnZZrUHPetcNS6aX8KBJ9T0o0ZamrxsU_BW0Yhl0Xa6ZS3xGufRpbQ7n988w9VwCWtbgtrgDsGAY2KMVK3OHTijYQg77jcuW22vhElGkxRLW4Ogn5QGLypjd9S_Q1RlWZC1BKC9J6CcOCEjPTPplUvRTlQQXaUeV79-1hPUmx3ChrZMOq5hb3ctunkGkPIS1dm8TMavVMiVHlu1IlJHsuWg7o9HwmkBNIi-S9hHECVXKVRPdRzRF5CRbFpVMHyT3s8Y3Y9zu8j-3qkJTeg5u1qJFToQ4TTzQY9IKwaBHAJrKhArlZgfPMexOlStt1mQOpmT8Y-5HCmEOmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=mhFAp4puv6HhE5DW2ZzyTNbYE9zcZltXpJ91HxkS-PTcWrZ15qQXcMYifS0x3-JYaoiozO81utUixrEbjNIdD5pZmdpgN0SZW1NxQ_9EWe_ukMsw_lONlPlP5kwY9W2JG7-2E2pupuNxYmvhz8_EWLttEXgg47eFo-1u2Vai7hgFTEJE3KYO7QV2XTzDsDtyvArgwHgk2RWSfXY4uJBBTJkmuVEz285n1-KZWSwD4A1W5b9z5wIGdYw344b_6ajE9S_o4ko5Qv_jtN9K6nTZRmxXwGMwBF_ZVfWNruazIciaDmoQOUf_DPwuQ8ODTmUv-g7FvlQv1vrYznPIp8VN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=mhFAp4puv6HhE5DW2ZzyTNbYE9zcZltXpJ91HxkS-PTcWrZ15qQXcMYifS0x3-JYaoiozO81utUixrEbjNIdD5pZmdpgN0SZW1NxQ_9EWe_ukMsw_lONlPlP5kwY9W2JG7-2E2pupuNxYmvhz8_EWLttEXgg47eFo-1u2Vai7hgFTEJE3KYO7QV2XTzDsDtyvArgwHgk2RWSfXY4uJBBTJkmuVEz285n1-KZWSwD4A1W5b9z5wIGdYw344b_6ajE9S_o4ko5Qv_jtN9K6nTZRmxXwGMwBF_ZVfWNruazIciaDmoQOUf_DPwuQ8ODTmUv-g7FvlQv1vrYznPIp8VN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSVBMaZ1LWeB2khlR-zSSQI3aewi59M0Ae6P0vIAzg87XYkr0v_ChP-9US9rQ_6YBqNRmC-AauXD1C6ZHjLrIgOcA1W-aAFKm_ueIWZMupmFM2Mk8qHBUpnlQ9KSwm_A0kqfcs448F44oR6prAXX18I9t9EG0p2gUVJglLXNoE4jbH8Y0M27ZxzQlO_vyZ4p1vM10zk-_VUQV_xY6612q7VjBi0ngpZQuYl9FPXZhKZg9JP6Q7fHLishIOnr5iiSHchIuoJYbHSvaLYpSWP1iEEhX9SKqKwIGUT_vRMgUdnhbtaf0JHbw3tzop6Y1a7_mm7Br6P4_seT-6ABGuRTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M708bAOoCrS7bSjDkfXPGXPGapQPjAi0HrAxouaMTBNGV1n0tI0M5S941jUEZFYPx7kffmEBLHyHBLcHXHmTR6Vv_7S7ubpFDSM-Q3D3bq_96ynyJ8xPXcnmARWcRRIvVDZ5ojZYNOeyDg-CnTRkEMpt-fj5joDUdMJ_PdZxMXY8XtBqSx6ctETt1bI0V0r1vy8R7DYsLep1NiZmojRsWznKo3W1jYS7gpbpaLji8UFmu8Id6S7kExpaQ384NI6yQuiPi52BT9a6CX6yH4_GaVI52Y9s80SKJu0_UMZZeMNDQMjb8z4f8pac7dqcS0TUEaSfz3sOl3lqWjrcfoXDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letjAHzYF4MfxX1l06yiCq58mkfrzn4S6DLWYM3RxBMQFs1KYJ5tqNdkiPR0j1RTr65fnUFqEEgW1SbiDcS8QwwEkyLmUfPKqBn2fOQA8jkfDcpCOJ5il9tZvlSVcky9-2rr0zbFay6Iqt9i-WYXo7NCdh3Ss97AwdF7xt4QeaAwiMPhNd-TVE5kYzBK-yAz-4UCKMogTmfiu4IzflzP-aBO1_rx9R5mdsLFXdwXYcEx1PetAVsWzQf58TrD2DHnh_pOBgTEhYBVO2CKO33fD10B3HrUL4r-tfRRx9qD3pISjeEBetHS2Je9HI0RLIsqFihvmMYEosHmLZkFMCcHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQRFY5N1RzHQ5YaiWQJFlvLxEQUS00_YiSrS97BvH70p3LyJHPhPQAbU5V58sV1yZFoh5wlGG-0cuO0IqM0CiVKTpFNG_SCMiSPTYQ4xWbKdy0B3-n2KLPTyUOuU5RdGK78cvuMwdSjliu3tLvLMvG51EzOYzu08_eKmMeuwGSm5c2qXruSgaZrMzWClZXMsHrDW7Zb9ViBnErY6AgOG2fxyjScwo4B5BWFootuLEA-NhEA6b5oqKuUuDRSnukjDF5Vv3ZaIvHd28bmjMVORopjbzEA39-xNVw6c1yYMHgLhaQgRWGHaC_282c4hngLWk5rcrZDJOtHIZMW7vIl0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Cu9WPCzXrnwl0OcDMZQmOt29IEXeo73D4Ci6BNFrCCskgO4lf_SywLISzMiMjFtS0Yo0vEeaY9ZKi_WlmfukwaEMOxDG07ytxYWxXCjspJ5kdoBmK1s8LxztwtpG7eTOAdtnOJvUSvMm0dpFafalUv2ygF9K3lJea-OD9fdeovP417M1RvdDQOMke7t6KVGX4xmrOFVOA0AusO9NwRozaGVVs2jP3UOeg9d9rnNqOFzylvIOztg4Y1Jy70u7etrPh1CP8f69swSdiBppcLMkFZ1AbWJCm1NO14NQiGlccWmPy3KFJzWcaZEiw6yDLJeCVWEf1ABLKeeMtXEx5nQxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Cu9WPCzXrnwl0OcDMZQmOt29IEXeo73D4Ci6BNFrCCskgO4lf_SywLISzMiMjFtS0Yo0vEeaY9ZKi_WlmfukwaEMOxDG07ytxYWxXCjspJ5kdoBmK1s8LxztwtpG7eTOAdtnOJvUSvMm0dpFafalUv2ygF9K3lJea-OD9fdeovP417M1RvdDQOMke7t6KVGX4xmrOFVOA0AusO9NwRozaGVVs2jP3UOeg9d9rnNqOFzylvIOztg4Y1Jy70u7etrPh1CP8f69swSdiBppcLMkFZ1AbWJCm1NO14NQiGlccWmPy3KFJzWcaZEiw6yDLJeCVWEf1ABLKeeMtXEx5nQxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-_-WfTBHQwpSdt4bWljOiMmWAmL_fPyo1k8ZhiitmKsqEWZ46lhfFhSdchbKmNbD3DkvNCI7BgEkXj4Qx0lcAw_DL8_K86sQd6HQw47z70Ekoz846Tp1_iYXMrZ3Cc8D_6pZ6uASKmYUrUbd5hXz0dfNAJ76WKkVylfh4SN6KyiZGslPNyqGYnfCUAUT-J1511pdYNQMj5_RhdAX7OXy4NivSTDGZrnT7qN_Dzo-ST9xkAnEja5C_iJoxj1sqTgEXRJivnPHv1-bFlwlxWCvJ59j5s8et-ZzCJ03HaW69-47leaKmeqTB4POghpy_HJXG3Rbcmn412IxDlUZEmImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2GlPawc4bUXJukGjPc9hiielMZQN2Hi8fH0ORS44pLadjprfaQ0SBALoa0_Lsq2i_ZK9ANSxmlKz-3hRVgRm1qm5ChtjUPtunM4W1dOWZH97IHFFVGytlQiBtKIxwT09AK5fsQVxKFIEDOLKJ9OB8ZdE0MEM9fqnNpmamMKnWEKpRu6isKntIZUbQ3_Yvm1JZc-YvkHoLWXF9YPAnV6nfUzxILeompID02tapHmMD90uYnEWFltnSAJvxKNGs-g-_6eqv6W6zs_eGEJpIn6BH8rNcNv9J6Hs4_NcN97Zhr9HUUat5fp5aDup3YHdzR2m4lQLHRA-P5Kb76dKUoSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJUioGNn24RJQjwzUkaS8pvzzSYfMtz6CtP5D6r7FnUW_-d4E_C6apjAr6ljO98bvDeiODDy1_4ACcDkZiAE3Augrm5T6nNkNdYIGLsH9CcwRJcc18PrVP5aawir7qSN2MHaBFC_Qjq1TxBxlxW3S00p0tNsjGgtiRWOdAVcP7fWoazRlJFRONQ4EALbM0rzjGF7E4fYo4f1I0GIQ9RhwL6ecP93h5-Hir6mBjU8jeaaRNV9XZ670XboURAXhTemPq1bGxVeUP919Lj0Cz2abUP8-yEu9hAU2ZK5vVt25LWemqh95ylRrUcHBJ8hfLW-bw1AnhyiqdDycf5M0B8nxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=UD9g0Z6Af1wYQUwCu5kx4F_K1_aLARsxQit1V4kwqaI9AGzo3HExhCoUaYkTwghsWAr6X564fTNFKUUhUwGf6edE07nmaZqKkAlQpLkGlEbeMh5lpSUZs28gHzj31QDCweEL3b6lPSSCKX84OKubigjzGiGAtRQGShF6hKojNddV0EMPYlysozNF41VZwp0YcOE2xPDaH07-r90rDwD2ZsTV48aqAMktHI6exM3UHg5fVifbzBxUuTgPx_k5XGDN5itFHyCLAKHgwxuaUSBJBRadOhoUN2Rtl5Vdfn1A7Fx-B5BpqMZSVJb4X-dAnBOe-Pvd3MHG6sSe4hvi3z2Peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=UD9g0Z6Af1wYQUwCu5kx4F_K1_aLARsxQit1V4kwqaI9AGzo3HExhCoUaYkTwghsWAr6X564fTNFKUUhUwGf6edE07nmaZqKkAlQpLkGlEbeMh5lpSUZs28gHzj31QDCweEL3b6lPSSCKX84OKubigjzGiGAtRQGShF6hKojNddV0EMPYlysozNF41VZwp0YcOE2xPDaH07-r90rDwD2ZsTV48aqAMktHI6exM3UHg5fVifbzBxUuTgPx_k5XGDN5itFHyCLAKHgwxuaUSBJBRadOhoUN2Rtl5Vdfn1A7Fx-B5BpqMZSVJb4X-dAnBOe-Pvd3MHG6sSe4hvi3z2Peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=vfYJWu4eQYCAbRU8GWHiM54SYbfa59v5OcXRp5ExF6BaNyuBfDupoDJRYrfcEd1_fqhJsUFYI3IXN34q1f324g5-hxoa00QHgy7EQ_vR9y72IPRUQ8CT37V_oVN9I8lvxgkUZvChJz1xv_dXb1J70RSawKoDtcJkGKzwBAVd-H4Ve9SOepU2Yde4FDv-mXOfPc6aGHKD6me1sB5GvBukBVgRdh5q47OgdSS7IKk_82TrjLfYxIzAXA9tguGG5ZfQg_ibPC79PmTnybetYCs9Ow-da4ZmkQx2EWXlQsoR4J7OGaV3GGYT3xb0uQ7w6K0Qij0ZSzipGrsklNSUtTNVIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=vfYJWu4eQYCAbRU8GWHiM54SYbfa59v5OcXRp5ExF6BaNyuBfDupoDJRYrfcEd1_fqhJsUFYI3IXN34q1f324g5-hxoa00QHgy7EQ_vR9y72IPRUQ8CT37V_oVN9I8lvxgkUZvChJz1xv_dXb1J70RSawKoDtcJkGKzwBAVd-H4Ve9SOepU2Yde4FDv-mXOfPc6aGHKD6me1sB5GvBukBVgRdh5q47OgdSS7IKk_82TrjLfYxIzAXA9tguGG5ZfQg_ibPC79PmTnybetYCs9Ow-da4ZmkQx2EWXlQsoR4J7OGaV3GGYT3xb0uQ7w6K0Qij0ZSzipGrsklNSUtTNVIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=GBj-sh9STIyWucXpcifQSfC2thz27fftJOXRlK-FlqwMUstGJwVbjanhvtAMpxsOlfc5SWrJAtVI9SAUJTjsWwJCtc43_Y9ctPIHZ0a6Sq_ZtQN2uLvNb80f3Wr9eulku1tDdOuRvxXd-bp8ADE1X-DgGwTXH_1fvzeva3rQ-PkyOB23jDOrOxV0HYu53XiqrkMUPdCrNGp6a41iGYM6pcMeP7Twn96dFnKTJoY4UT79mFCj-oAHVqfk_eAOBmVOnLZzrbgMlAZMPydID5ExfMY8_v95zK0y584EcT2bngXm2F5XX0COnk-bkkOGJm_xEsJzMNldB4PFlTERuI9UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=GBj-sh9STIyWucXpcifQSfC2thz27fftJOXRlK-FlqwMUstGJwVbjanhvtAMpxsOlfc5SWrJAtVI9SAUJTjsWwJCtc43_Y9ctPIHZ0a6Sq_ZtQN2uLvNb80f3Wr9eulku1tDdOuRvxXd-bp8ADE1X-DgGwTXH_1fvzeva3rQ-PkyOB23jDOrOxV0HYu53XiqrkMUPdCrNGp6a41iGYM6pcMeP7Twn96dFnKTJoY4UT79mFCj-oAHVqfk_eAOBmVOnLZzrbgMlAZMPydID5ExfMY8_v95zK0y584EcT2bngXm2F5XX0COnk-bkkOGJm_xEsJzMNldB4PFlTERuI9UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyINHFlZlAE2GBtbs01hY8HOahDJdpdqp_zFDHgqIC0zOl3zbLRbcf_mmueIMPwA85bYnq_5r7SlxQFGk5PpplRfSQG6sQg-jtNDhMKnM9U00UYI8y5v9thEgzh_WECU48ZAz4iNZ-ylfFwb5rSa2XjPCrFoB905k4f8G8c7r3yiwya5X5G7D3Y30ytNV0Zz6ZQ6yLpk9WVlWCg4t5J6F4p4ea-_D79S-zdFH4m4_vzQmgRUMRRekUSUH2vrUs5DtZspO-7AovlQcPQRCIRG8x23kPdIhs13bcMLGdvFpIPERoU8vlZ_KG_dQmLoG-ItvlZc7RfC8W1rDCWIs9MA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSgVa89_kYQiwfWR1jbe5Oj0wUY1UsQvc6CxbrkbZTWVlY67cEHP1KrldCagQcdxtLFzCs32r2nsMYuK3cmX8Wz8MBgLf2B_37fnNDFFFBbTyLpZ1f5CgDXUkjLP9-Q4EsZWo9dHW7P7DV-zFCVMFfB0pomXeijgh8OI9_UxVdjejZxXtHZQ98zhCvhZTp6JCyXSv6GBAwiAJU2tEIzurQxjOa8mWZqFwqKRV9kGtT-SRdGGQ_HXK5EjWIu0ctzSTcAikN7169NgHxfLZQkW0HTTJIm3xchCjj22JJfORpzS6fhRjWYRsDuUoZF84l4hKDe2dGTMp1gSiw6ntTmizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQFpuk5TWlS97M61LJQj6vyTbGLyuJrhciLu9fNbZx5F78AXQB3V9re2xkVGTGHNbvZlD5PXWymJXXODpw7U8Y6ThIWvap5cphoLg01GZwMggQKsOYAqUw1PDaywxLoztJaC7MOBnUNQVKVTk-RNiwVS5h35wu74g1j6cuXKgoU_38r3luV480Tk1ef4jyClFp-AKTBwIE5A9G257839OWst37kZJRtx6v9ENibyZEGNfwuYdzDGVBICHhgN0lk1bSf8dyCiweImG3Yzy5WW6QrRCrH6FNtPU2e4A9LQHy8sP0CAfZ0CQtJtF15GvsYT30qhkfeMvIHnoW-AfP73QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkh5y1IF3x0weyjXyCFZ_MI9otWyvOOT0D4WTa9O28cazxhUw_iHSs1WBgTKoIXDnK1X8zlVkLjRRwYbnFmMYwhZYhv1RPLFUGHYzYr0TWP7NbjkQr0goTPc-P7lnVlFDzFOUmmWbNK5Qe87kxBQ0UZ8xOEtgrCXU6t2bQ7PlG2FOr9zL5PEhr3gOel4fki_EPCDnYFbirUA6Hyy0uuRMmi9PWOCHwEoUDGlYo5HnzdMRC3qAsEiUWGjlKv44YcaVX2gNsVKRP4s7JOdpZwEVE2BSp2sXW0AzKFqTdEszSjisRZuBAxO_W5flfEyokePZE8RAymgBaL1cQFAkSy3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6GXH0pklDNC7htGUxtZymHeKA4g9OhpeT0dLasWCebFlFAejmYE7S5zO-NSxlDdKlKndbjh_BcTq4IRzKCAiySL0mXHgGs6-QN0Gz79TqEAX72kkwGSdsvBnoRXZH9gKv8TPVcWuQL7rGXn3SoZHiCurRtAWm632aKPnP7pmJW7h2H3Ut_qvooZ4EBuSPF2wXe0Zy4NQcLKGO4_MeaJQ9bR9ZiL0wLcYlFx-Y6Rzul_7nFHJwxrBPqeN_MY47kvu2YBj3JPB1_NxLBZCwXhiftoMBcUglye3bgnPUc7FgPevfjUa9GvC0p-DTB7nhxH1mbBHjLLRxCab5Y8lOAAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8ytQ87N8iaOKp44KvxfEfOAT38x0L8w4dzrsOvzZ2zPO8UJ8FK-61V11LYSSa1fPO3V4o4bS-7srgKChC5IpsNc-G2bRZNco3r1FhVifsic_Mm2aF9_Ga6Hei6uDFKGdM-i5wu8l7xqTSsrhO5E93PQVKNfVCY2ZV7smsAL7gwIABo0bcn-RZaYWedUt_vNTclxqM4DFlBwnUkJR2PWPQn9mB4n1PCpZPS5PxYYgbtq7p59zKxo8Ff2G7lWfz5fqMboiI0Omb1AXqTSW4Qhi2Qi1sO6in9-cZmVLv8sSbQCiaRI24COWMaD649O7oj__qJ4CXZWhq_3houfGLULgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-7jNmP8HYhJxedOJVxeWFTt3cKq1uSkHCGEzDcIwUIi2j0x_jUeIxQNkoN-RMXc8ZNc615wp_DQ4pjFXKXJDubU0iHDo1VFmTdfdlZZdDDdi9vwed3M_3Kt0nXPdaW59frbFPThEW_JFE3GBN7dZ1wMZdy02WqiT_HtEiifblx8JVcwa2xz005p8ZZbEp9DFmnyuL5-AIEDYCNb0dhT1Mf7efAfNQ_ouBIcyE5Kah0dWMZmdGkJY3i9k06-vhRWFS3a1PbbprLLDzubOqf8RgkrQbNxvunfEs2WTpcVKfFe6Q7y-jVlf7US7NnQUfZPI4yPj4_3IVIVv7lFhXYMqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdlKloDO0qUItUSbkaE4ummaoJ0qpokyfpe1ZDCmuCYM2P7sPrLrjBfFcm3No6j8L6Yep90GDixHBPcC6R7LhTwG1tYNp24HrFxfAXwH1cY6eKKFG7pgTC3IO7wjzynHDpekVxxAaOirzhp7ZcBTcuvQGhs7tK3CWh-8GxzJLQR8Cf0S4z8AJiSeiyCYC7rTwD95h3puHDRe7if8HE3Y0V9xZ-PGYy7zWFqyXCnKRZJSkij0ZQ7mCsy-AcX3ofbbWW-u_ftsWTgPz7AMEGgOcSWvvtuMDbC14suKBcjGewRbyvliubKNUaOm8EckfIiq8yMMKt_Uj4chx6FjdJzTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwANccQlYfBJd_LscGsgetyWouRXYx9fGuXAeGnLEoIccJ8M3RmDVu3XOOMUtyLXt5rrqdsQpE96xAHbitfnNhJ7oKapFVx4uK2myvShNtaLVTMH1XfBlMXpGfXtmE8tY8aa-aV24N0CgoZ8_fCZEO3wkYIwZkDPojtGyXsKUhQvsC0hFZcUTVq3VPdtnjQwsSzJp9PvWHMTVll2ILHWCMVxCsaazD9qjbZL4Ktb3E1elpsSO0ETlvLhW156YTXzu5K8CmtjY20aIRU2OlceASJTLW_1knfHt42StwTtlyVWRzKJJZKyHfYI__vVmTLopkeUdcPrJpqtFk1ffuRcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyQoJSsFpwogBwAqXejoiWOp4iDZfyMjbCnI6HETvL2K0P4IuCcT9nf2QpALAZGAka7jwKA8FZJkbhdHtFLG8h_-h5Mlox52XmZ5Tu8Ho-PPw_oh3K80VyK-Fv0MFp1nnDHBDNqFizq9uJV8WEtAi-1alO1F4j3wap7pUAyWJOp74vwc4W-8JT9i-POpZrNTYZ-1pXg8nQAuoz2GqKnr-nalXiwWWpvaxRRHRUnmc2n-Pel3vKe5kKn1veFEXouGXI5K3ameT7bxMTIXGdW1jYnCkjewZLUnfolWysHk78VjsPfyvR77I-y7lKUolH3b93Y-p9LfQL_We6ncTbSMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js_g8k8nTrI7s_ddY5YEU2suaUPKNWRImGnFcXFrE0xhCWytU_UtRWhirrhNJSPnQX2JSMLpHhYSdGoAHJDjKs4Z5hmFpuqzbIejvPlcuC-UyFQKc4oh1Zqg7AEAO5n2cDvBMaXNlh7P8NKoLPYPUcm6sXA-G8qv-LjjTgfpUR0l7cPK5qBW1rzwPNiCIJmiNyeq9OtjHd-TsahZaEGvZWuK99ACOWw7pjTJx_6LkUgAXNsrZYmulSb5dxfz4vQqCVw6qiodYIwMcziPZ43d8zJHfw2BI_A82AnRhQlabwPhzfcIvye_muSD_vcr3Wet_ef_264rngRCCz8cQm9twQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWTpSnqpb4c0r0_BURLQq1ZixICwsGc_rHibEE6wac9SjUA7hnsYCcUKrWA0u54Bs04MCOxczs6zFWGKkOmNS6kwS4lUWNbwGR54rt51kYEIgKerCxcgsBeU09HQt50keCL-BXmnPmMXwRyV325oc2dyq2eH1o4tOGIcBrwGf_51PWKtYGikaDZ_84_lxboZWnW1nTd-0V5x6iuOX_IBkHdUS_nFayxGcysB4fXIrhtBY2doX_7Aa1j2QLsAxfP_V3Z46je_P7WVFCA-M1F4bNrlTadAfVzSNX7vFv_z0N_W_i-Rr26KTo9REKZ0JOhmpNya-D7-wQFnY8kenOLzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMy8hgvFpNaHux2Peah6JKdX808VdpAPQ-cQScPJjxqhT58LGUx9d_z0qKChkvSjxVN9ao5clfKKJpjJCZt0JICEGnPPkG2u2hGurUiZB74tcZUWpuzjLyBUKd9ZXyljT0vc0UYSC1MgSKHxwiwZJ9Cnx4BzgpmUhTE1BQM7dMWMzP635-m_bB9hKfoHMFiB6PQkMG5XiltaeNb2JzIRvcC2vE7FxY2pl0sNB3gfgfaG5npzHttxXLRguO6ArQWYgKsI5mL7GdpTq4O7vlHzxXXltOh1nqf7B6YMAL8QJP9kSF-ml12mBglzaO7CUwtkZTj8F1oEigv3lONhMKHETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBQo-bSSZQ_TUa_Asci6Y9rT9vDBTis2batT_GdxWTT0ZiA4V2uRZ6UyqcLS-frsmULj0X4o7tMR8QGjESw_JYXt_H2HdQtxSMBBwLQd4XSr8PueRqs31WgtKWUnHL3iHeLUw-7Ei-PDTpYGFYrVfm5oVRsC5acUYQZpy86PpHaUTToRxELQ8gBCjJSLfVu8FoZEd24Sac50mtUqF99Jm-ekwcGPccE7-cv-mZb-FJzLtHxgA3lpHG1NWXJx90ZS5QzMjtfIsfcp-3wsJHhQbOQio0L_Q9qpHVV5m8rFgi1jdfKaRCpZBlbc0utXTjP44uQO5guZR9PIwz23AkI2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAyVgjmm4W_xCVnHAClibeAMv-Vz0LJlsgGPKAfddz_t2pgo5QQnjploe-aeeggI5rj_X1whp8Ejn-_GtltA0HYmNMFBxU7ChhStvEBbqvfRF__eNmbJJbZNSk8e9MJREDZnDAXDsGfyyEZTRBLcEAw1QNhcRcPtVdEjRUxonmbydwk6pI-yoKxW6GcX6OxL78P9v5DXXdm3MvBj127KCBTNln1ahsJaimmcSNRBv6hlTAWy3DrRfj9nr5yRIxPAbmK053VTruFVZvAx7ItF8C_4tpVcxLywtBz5qrreDEcqMhaHMYzXZ7y3cuPT3j4Y9tuj_HPwyeETcAcsr31C8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=MgfHfDu-soWE9fpRHozznbqDG2ulG1vyjfamfhRZvKH4wcewy9prgU0FK0OhFBzAARpPXo71UzYTM-OqaIVOpNjoOex5wj6yNSxz5xAYtxJmUkDt3MUY02y56au8pzECY1iU8n8cy9lwVs0VdNgltyMjpFuKdsZufgnhPcGtn1RbqbpICVfOIO3ZP93Ex8QthLniPdlNwsWjusmLmSmsYbXwEs4U4KNtZrm4-p_ueJv0pP4-TdMNB_iaSQMp9Ub_dkstIy8cpIlJPEAWRZBRup6TxDju2GoypNGN1QDzpzaX57VzcmEkmiiCMnJoa9oBLpzxqguxK-x8CmixcnZi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=MgfHfDu-soWE9fpRHozznbqDG2ulG1vyjfamfhRZvKH4wcewy9prgU0FK0OhFBzAARpPXo71UzYTM-OqaIVOpNjoOex5wj6yNSxz5xAYtxJmUkDt3MUY02y56au8pzECY1iU8n8cy9lwVs0VdNgltyMjpFuKdsZufgnhPcGtn1RbqbpICVfOIO3ZP93Ex8QthLniPdlNwsWjusmLmSmsYbXwEs4U4KNtZrm4-p_ueJv0pP4-TdMNB_iaSQMp9Ub_dkstIy8cpIlJPEAWRZBRup6TxDju2GoypNGN1QDzpzaX57VzcmEkmiiCMnJoa9oBLpzxqguxK-x8CmixcnZi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5KT8wStlSf2m1nnZFCSQ4qz9MU-zZVTsgancIxcVW7YSWBFjFjcdsi80eq4CSO5ckkiGQH9txfNLwdfLTI_Hfh9lDV1iLvgP3SnVRrEYz9XyKCXL_0rBI7RqumNR-OGbWIUaEwtYUcUbLJQRzB7cuHS1R4ulfOdFfKXw4rfGkwaIZJ1r7fliTaJOu9fMECK8XwhfCeLiKKYKb3LssS8lWzi6dbHzr_G3jIgDoSG2r5aVmiBTwcxkRnaMb_E-kHXLvv-8RV9bk0HyCMM4fBjtki_9sHqukOGSlFQvZSMqC_LTSqRVJQnoqL86A9AXJivumRGb_l2OYuTNutRMAlpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=aR1pUsjdtUTTflDYGnLHCCHezGLa3B8mcB4VIlLVYksRvoU-86SdxHX8nYJEfKm75qGUXjjbdBKrwbU6MqjL0nJbbnktfe-3vdl4uwSvrjwygDFe-u5vgw-Tnb6Le3mEkDIn5jAr9nnWelH3D28bkk6z9pHVVMVsJ9rlmhJRv7FpLixpLrZoQuDkFdLMuJUXV4-uUauxxhik_zue2U7BdIinovccghOkFRUcNsLHil-FjdwVAh_4O3pFNBLGQ-zOfashHxASd0qh0b5hA2ERcXdyP5t73lo2NEsZsGXDav9c2tzRIq-YkrGA6lBp6h2N3TE0KiktoyN5W8da_5Ahpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=aR1pUsjdtUTTflDYGnLHCCHezGLa3B8mcB4VIlLVYksRvoU-86SdxHX8nYJEfKm75qGUXjjbdBKrwbU6MqjL0nJbbnktfe-3vdl4uwSvrjwygDFe-u5vgw-Tnb6Le3mEkDIn5jAr9nnWelH3D28bkk6z9pHVVMVsJ9rlmhJRv7FpLixpLrZoQuDkFdLMuJUXV4-uUauxxhik_zue2U7BdIinovccghOkFRUcNsLHil-FjdwVAh_4O3pFNBLGQ-zOfashHxASd0qh0b5hA2ERcXdyP5t73lo2NEsZsGXDav9c2tzRIq-YkrGA6lBp6h2N3TE0KiktoyN5W8da_5Ahpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=OcdNc48Tbgrgub6mApO6n2Ecqlme-meQCVahaUxbbWZiMwuux9I_FHuvJa_RinxtiFNnMuYWDykbcRqEvEst10z-XPPG0qVz8ROlD0VdcVmQU1tP0qjA5niE6px2LXUNEmAHWMlqGlEMso7hfW_lLDbAvuKghnG76yS_zfxWMUmBE6C24CJAFKkvvv8Tk-QUh1hhgBSa7nrEsKpzFzAUCWdD5ryiEis_PS6YtX1ov4hZYYFVHUyc61YpcNvPJOKuSNcLJ-rVjarrkce3Xzg9ScXCbnDHxw-wYO6yrKOrLK-DsYwot1uaMZqUMtxdJ-RZx7fRBhgWU4CwpVDn-gwDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=OcdNc48Tbgrgub6mApO6n2Ecqlme-meQCVahaUxbbWZiMwuux9I_FHuvJa_RinxtiFNnMuYWDykbcRqEvEst10z-XPPG0qVz8ROlD0VdcVmQU1tP0qjA5niE6px2LXUNEmAHWMlqGlEMso7hfW_lLDbAvuKghnG76yS_zfxWMUmBE6C24CJAFKkvvv8Tk-QUh1hhgBSa7nrEsKpzFzAUCWdD5ryiEis_PS6YtX1ov4hZYYFVHUyc61YpcNvPJOKuSNcLJ-rVjarrkce3Xzg9ScXCbnDHxw-wYO6yrKOrLK-DsYwot1uaMZqUMtxdJ-RZx7fRBhgWU4CwpVDn-gwDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE8x9TtaIJrMvDlGjXqmGxs5muN3wsICFls2dnV0HfK-FCuEeh0EtjKiHYRdi6LdQ8Pn0ac5rYeyUYxDAzRuC1q374VzWPGI3KQ9IuAv282qQfo0dheiPYKv3rCibkBEZ_bD3o6JlgWmRg1Cb05_HptsjL6_fWuGKx0fHjz7COxLLBTiG6QcrA6vbpmxKdw3Kfnhbnle3EmCQp2jQeBOfWM8gaM5nNEmoSlh_34bJ0ElJfzazdvxNG6mHpIFGd-S5dkt7X_BH0Y4QySHDjwYBY7sYI6Yzaj7tNVnmFFk4WabtIpjVh2fZN9f3WVkw-hS5ZQxMGowVpPdQlQB-0qelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=XmCvHO9_TER9cSKTzCtEkkFdwGA7VZgFRqpTQR7HnRQqfyE4rEQ_4a0N46oUmxKM5fD6KmithMmGdot-8r_wpCw8JAVGfZiTPaEROJdlTUZ9icgD-yzmPjikWLWlgaBwiyhOSMkq1aRI-CPE_37RhIFo0osAeRDAdAk4jERsGwRUKU3fpifpsoynyjhPcH7Vue21fLAOMqKpe4FjS9XNYIZKffieW6IOrR_dBOTaP_3ahF5fydrQLbrXBiiBMcGVaxhR61gdyPFDg9jt9S6HM6aQdVEozfn412lk5q1w4M-sH-X2WIcaw5iPB5U_zcldLwvBvdqLtNhx7zH3UE_EJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=XmCvHO9_TER9cSKTzCtEkkFdwGA7VZgFRqpTQR7HnRQqfyE4rEQ_4a0N46oUmxKM5fD6KmithMmGdot-8r_wpCw8JAVGfZiTPaEROJdlTUZ9icgD-yzmPjikWLWlgaBwiyhOSMkq1aRI-CPE_37RhIFo0osAeRDAdAk4jERsGwRUKU3fpifpsoynyjhPcH7Vue21fLAOMqKpe4FjS9XNYIZKffieW6IOrR_dBOTaP_3ahF5fydrQLbrXBiiBMcGVaxhR61gdyPFDg9jt9S6HM6aQdVEozfn412lk5q1w4M-sH-X2WIcaw5iPB5U_zcldLwvBvdqLtNhx7zH3UE_EJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcjWo8hHWNF8CNZ5a0HE3Ct0TwKG9_2crowc3MPRUShVEG_LtV0gSVVq4K5NOavNPU29RYxDsE01lKXz41YPbejuJkv8Js9VD97eNSnNB7rJ_L5b2wdpBaIY15C4pt2NlvI0MqoyQYzG6NqREm0QAZsDR2kuEuJ86vPXNtyB2TvY-watkezO5iSOeS8bboZ95LlEVsOF7PvQqa9_z00Bh9_geSc9J8UfklQyY4MbegONpp5YzVQUaKxVoKDl94C4fxlzk71zEWN_7JrnML4Pn2ZZQi8F3PAOcfW-2qIQx-FxaeMHY8NfrjSy2zBNOMsBDp7Ca2Fd0ynaaur4hdREPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugjjZTFy5v9wZPDxrcFQW-PcOqboxjhrlYq_vRAQgENf36yqjxCvaQnlRKtTXUbBngA6TZEI-BCksb5-JlkTuV7Ju0Pk9J04MvMOne-LE_uTEXMySWxnHXXcdvdEgguB0EOJPR4O9-YIqz_y71xneKMiHFNi-wcKyPm3kpfCIN8kwJgr4IKqq_wVaGowcmcOy4QV4g2Wpikjsr5u9Ek5WmYjJ_99C6yyNHZzkdOuDmFQbt7lNyLEuHVaPo3ffg8ol56b2i_3mjUHNlSi8zZDKMNhpYVAmhN_AcNw4npsHdMcnyvGcJ0IV-bmVWJYilwXotN5OVqaH_4MHAShE1ecmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M95bPCCQfROe5n5eJGhhmljfu7yUu_CXWqMzk6UpjkyypqlVt7XF3puTDRGaVHSLBzQIS1qSiTJVllfQxq-LEKc0hTUKRLAdck9bkayE1Vne3lcpjTqm8rNt4we-uc_Gf_evzNDx4c4_7-6-CXc7sdODZseiF7RuHQGfku_ZvFKmerenlMNcd5EiMZ4r7aglYvBCctfLP3QkkN9wZaZCOWFc500PSAwuxjL2q9p2AlEFbCzsO113fKoG9apZoCPCIFyqY5ycrP4kTI8juQTK2NC8RfzFUBEgeAI8bdg_LTbuPF73djaTqjao2KKxIB1oN9ASF81U64jB04Q_BFKXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZkNX-kaLZPuUxRU0PvohU7sxxMaYNkbM2P6dfSk7VsLJh4ZkM97mYmqsKuYdDuko5_MG1voejQrDONhd2FgNHHbae34hR_dmiVk6eab4r7MxKvtSWeLKDynTM54INfGaP7W9JYtBXcTbmGA-5DbkrsYcvBjepU2C9l1dLTv7wUPvIFlK2W3acRVwt_VyutjQCTL3D0rUVSdCjFvjjEdmRHsvGAbUv_O5RpZnP76CnqK7qVOJRQUH6XvXRj8_m1xlEAWq2CwuWexloZTZ5sNwhZD8277k19V4_qOwFcRT89iLsXzv8CONJka4sNSDhmXG7ydmyXvDt9bO45DvM-2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=fCb-9hkK7J48fNc-Gat_jBEUAjXQ6kUcYoVuWZe_0DQK7zvGzkcT3q8tfBzE9ncYAjYURyBDOgNDfOTTbfFiu8a2cBTQ1pgR_nKvvp5vvnas-aNh1rhh302TJBVyELr4VGOw8owmKAvxBNuORrvl8qiKNuZlV3hnEsW7NfMEpXttwQ5XUevebNKgGHGbvYnbW8sEJseljM2nm7cBPoiovtR6_eLMMo6L8bczdb-pz1C2XkhOsZ45pZtxFo8TBwXELUlGS7CfOzrvgqg74h8BE09GN-FBGR4UjTPJRITRig_bLG4XlDq-ex1BR-yXvIsLZZRgJBp4gDoBs-2mJgoLDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=fCb-9hkK7J48fNc-Gat_jBEUAjXQ6kUcYoVuWZe_0DQK7zvGzkcT3q8tfBzE9ncYAjYURyBDOgNDfOTTbfFiu8a2cBTQ1pgR_nKvvp5vvnas-aNh1rhh302TJBVyELr4VGOw8owmKAvxBNuORrvl8qiKNuZlV3hnEsW7NfMEpXttwQ5XUevebNKgGHGbvYnbW8sEJseljM2nm7cBPoiovtR6_eLMMo6L8bczdb-pz1C2XkhOsZ45pZtxFo8TBwXELUlGS7CfOzrvgqg74h8BE09GN-FBGR4UjTPJRITRig_bLG4XlDq-ex1BR-yXvIsLZZRgJBp4gDoBs-2mJgoLDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=N3ie4YPWoZ94au26kmFPhQ7sVz-btzhPbxWJlwsL-uZUK81xhz5IY0pFFWzqQxJrdpYWrsRbQmLuLwV6sHe9dkAB9b8fmZ8aFZEdlnRoZ_75qOZEAkAgbM0VjAPO1jhgRdkLIcih2Ew1_7VR8LhzDOx_fl3NIkPjASeQY-Yqy1fbRHHMkQGZZCLArE5BSBq7IFBhWciDX15LFLbCK8OnBQHBapDvFvX75mBggPfBFDjPXmWdwGyWY2xlsyw12JdLDUYyLJKDrQZ6UWovUEx4jvd9X97oH3UK5BAYtiCMa2Roxi7qZS8E6GYGX-kSiidLa0sPAShlLeuqsk-3K9awMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=N3ie4YPWoZ94au26kmFPhQ7sVz-btzhPbxWJlwsL-uZUK81xhz5IY0pFFWzqQxJrdpYWrsRbQmLuLwV6sHe9dkAB9b8fmZ8aFZEdlnRoZ_75qOZEAkAgbM0VjAPO1jhgRdkLIcih2Ew1_7VR8LhzDOx_fl3NIkPjASeQY-Yqy1fbRHHMkQGZZCLArE5BSBq7IFBhWciDX15LFLbCK8OnBQHBapDvFvX75mBggPfBFDjPXmWdwGyWY2xlsyw12JdLDUYyLJKDrQZ6UWovUEx4jvd9X97oH3UK5BAYtiCMa2Roxi7qZS8E6GYGX-kSiidLa0sPAShlLeuqsk-3K9awMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=uvOODqHptAFX3th_ePzPo0QuW6gQOEJXigv_v8eTZpFOXLLBJAIHnY9LmWrRy8F7Uh1QOdDGIGCMSbmVdJIq0GRTCzcCEU1jVtbv0SE_IABwTo-1JLujExvmrqsLtTk9SRtOOvbc2VCbIErGDeg1SWm2fAwAWyVSUd_gT0po2ijqRR-zRu0WTJjVd3NBjk94P3Lj1Bjk1R1qz7z0C-dyFivUlSQGA9ooG48YC2-_wpEX0UovBAHt7na1XNCkiTldPlPdY-uG4QOXhGSOBQh5pc2HvkAVP8PQwcMkmyJ0di-cmsin2hKZMdQH-Dec2TQ5vyejEqmQqUSTMQlS7ZPErw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=uvOODqHptAFX3th_ePzPo0QuW6gQOEJXigv_v8eTZpFOXLLBJAIHnY9LmWrRy8F7Uh1QOdDGIGCMSbmVdJIq0GRTCzcCEU1jVtbv0SE_IABwTo-1JLujExvmrqsLtTk9SRtOOvbc2VCbIErGDeg1SWm2fAwAWyVSUd_gT0po2ijqRR-zRu0WTJjVd3NBjk94P3Lj1Bjk1R1qz7z0C-dyFivUlSQGA9ooG48YC2-_wpEX0UovBAHt7na1XNCkiTldPlPdY-uG4QOXhGSOBQh5pc2HvkAVP8PQwcMkmyJ0di-cmsin2hKZMdQH-Dec2TQ5vyejEqmQqUSTMQlS7ZPErw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=c3IX5-dy-e4vSK6x4Igev7DgvL8ESqxiPnmkX8T5ou8d1w6AE31aUZK2hREGKyO2ZRSejkcxXJkq1KqRPuThAjZiuuL5vllZGT7qV6301BAT9YTUkkArm3PESPCLbFQ6lx32XYVK9Lu2L0F_a64MNq0OD-NOD3HGuBRjbfulzAD_B_UP9MMm-zRxMyW8XqCFC9heG3ZzbEsw9lPEvmTqs785HzlvEjk1lzXU1eYhEZzVQwnx5FunU3RsZws5JxQKR7ckFDyAjABmK6HVbKfkui30-iQ6NXgJWfabjxhpkI8hTOeoIg4bTupgXL1Nk0QRj-cp_y1ceee2PaL-YKedA0IpDtWqX8p9TYO3nDZsWl6xaPj9ksghWBnPzxHpnIjizN6f2RQUktxVZ0iJXDG2FlyA7sCd64Z1-Z4N0WBhUXgzoqFln2hB0wQ5au9JiJMmlg5sgwtlGmmyqA06Q1oFYENVvt4VguFjxTCmNbnu_64wnnuwatkclyrq7M-ZgXXQH7UBY5SSc23S5k4SttsTlrxm1qBp2Zvr_ASBEnKYNAkLIVaJDLr4FFip8q87iriFOEbgNcxlNUR0cTLnIrjhtYF8hsEomzPFXgFn0jar_ieCgTe3wfeyE2mEMv8HcxC3vZF2P_rw50WMYB-GyZ0l6H8Tf_JJqV8_ylyuQz65dhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=c3IX5-dy-e4vSK6x4Igev7DgvL8ESqxiPnmkX8T5ou8d1w6AE31aUZK2hREGKyO2ZRSejkcxXJkq1KqRPuThAjZiuuL5vllZGT7qV6301BAT9YTUkkArm3PESPCLbFQ6lx32XYVK9Lu2L0F_a64MNq0OD-NOD3HGuBRjbfulzAD_B_UP9MMm-zRxMyW8XqCFC9heG3ZzbEsw9lPEvmTqs785HzlvEjk1lzXU1eYhEZzVQwnx5FunU3RsZws5JxQKR7ckFDyAjABmK6HVbKfkui30-iQ6NXgJWfabjxhpkI8hTOeoIg4bTupgXL1Nk0QRj-cp_y1ceee2PaL-YKedA0IpDtWqX8p9TYO3nDZsWl6xaPj9ksghWBnPzxHpnIjizN6f2RQUktxVZ0iJXDG2FlyA7sCd64Z1-Z4N0WBhUXgzoqFln2hB0wQ5au9JiJMmlg5sgwtlGmmyqA06Q1oFYENVvt4VguFjxTCmNbnu_64wnnuwatkclyrq7M-ZgXXQH7UBY5SSc23S5k4SttsTlrxm1qBp2Zvr_ASBEnKYNAkLIVaJDLr4FFip8q87iriFOEbgNcxlNUR0cTLnIrjhtYF8hsEomzPFXgFn0jar_ieCgTe3wfeyE2mEMv8HcxC3vZF2P_rw50WMYB-GyZ0l6H8Tf_JJqV8_ylyuQz65dhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=aQwekU7iYDCNYQYGxihyVncjREUczsBGt2-6RQvwWmBjjSfNt1NOK2Vf9Tg41jVH1whqmQorvJBCucdd7EspWrivn-S0p0JODx0z_98yIj_exwmTX01gjhoc3CZbLkDCPj2bTZ2dLhKs7UqPSz4f_-S3pHjJb5rPUkwjDw9wc15X2YtJu2d8_Saina_0_pkkI-M4_C4SqIe2Qs_R_V8m3ZU7j5ktk8vEfkcrJZIIQnNa3azIgQ2N-tV3eVVzcWC2CjavortjWrNu74ieFfb_uFKtTwv1klNoPpMaGJ-tb25XyB8xMuCS5M3INjDRzfKn-v3NtiYvQI_Ec7yZIgkjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=aQwekU7iYDCNYQYGxihyVncjREUczsBGt2-6RQvwWmBjjSfNt1NOK2Vf9Tg41jVH1whqmQorvJBCucdd7EspWrivn-S0p0JODx0z_98yIj_exwmTX01gjhoc3CZbLkDCPj2bTZ2dLhKs7UqPSz4f_-S3pHjJb5rPUkwjDw9wc15X2YtJu2d8_Saina_0_pkkI-M4_C4SqIe2Qs_R_V8m3ZU7j5ktk8vEfkcrJZIIQnNa3azIgQ2N-tV3eVVzcWC2CjavortjWrNu74ieFfb_uFKtTwv1klNoPpMaGJ-tb25XyB8xMuCS5M3INjDRzfKn-v3NtiYvQI_Ec7yZIgkjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=U5lQFB4ji8TFxHKFxW67u_xwf16tl1Biflu_NNgdJk7TLh5nkRu9cxPVWOaV_qEPRzg5WxH8wYGB12wZQEb-tT7hEP0uytrJ85SIl1vHPO1u7ksWYTkOhkQWLs7Q1LA1Q_C8BsRJ4puC8CRRKh0zGGLgOX5FPIGu7NGTcUHheIXGXYb8nug8hPG7Ou7z43SXTNcXfz5h52YKr0m38RIgo_-gEmKujpSvSgeL6zReF8E4Qk3s6i0kigL67wh0fFZEOofE-tKFSKg5kdlJ1cf2RUVxOFgP8G4Fdg5FQjl7cWtFXu3w_6zmdUfDn0-lx9ISj6429reslLwuc3OnYSa6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=U5lQFB4ji8TFxHKFxW67u_xwf16tl1Biflu_NNgdJk7TLh5nkRu9cxPVWOaV_qEPRzg5WxH8wYGB12wZQEb-tT7hEP0uytrJ85SIl1vHPO1u7ksWYTkOhkQWLs7Q1LA1Q_C8BsRJ4puC8CRRKh0zGGLgOX5FPIGu7NGTcUHheIXGXYb8nug8hPG7Ou7z43SXTNcXfz5h52YKr0m38RIgo_-gEmKujpSvSgeL6zReF8E4Qk3s6i0kigL67wh0fFZEOofE-tKFSKg5kdlJ1cf2RUVxOFgP8G4Fdg5FQjl7cWtFXu3w_6zmdUfDn0-lx9ISj6429reslLwuc3OnYSa6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld_O3S6ae5BAGaJzEhMkdFIplEJ1Ksripj50FoKeTZQoMrm741kULjvRYPDke-NHFAENz0hDo58QK39kDt898w0KPk118iQc_L8HiTOHyyphTqYrthnsQ0YpHaCV_Tr7ADArbLGjvr6fIgdDo8rYRPSk3LUA2gvjuU68qrPBH_5Me3KwaqUVnzOXZy21IQn2g7NgEVgijm45Ge23OGxcOFeidDCzQ7lfUIsiWf_npDGUOdYQzd7PJa6x6fwAL0VuxiEqvmvHAjBR2kjuQRhpW9fwoGRyqsCh2QvB28tay4IiVRC-0mJ-kPaDPeUOL3lgxLHSc1NgCpqQ2VLUbB5-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Ks8CxVd7M6Ci41iTLFreM2MIZqU3W_MLclaNw23Gu0KoJhDzQ9z-gB_qEWPcjhHzK6b469MvPcm4Fu3hx1RG3tA2iFRdCKQTUs9xlbH0REDmh8M92DOZNOC-AfUdn0uIPEou9l5-mvMSMDxz_nGpZg97LqWVIC3S3_ri_VVEKSjumSh3XzaE9fmDLvai7wKzaYqdyWuEndu5Br8JWripxQO-2t4sxuo4yuj60_itYIxancpScbiv2w17EKmWtW_qkNwqA4YsiUme5FDTCHHRtmdqubcMZhOTxum7u7eq5rDxC7R7Y8oJxCjg-4_zCZq59vp569tU4-gNluShbU7eOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Ks8CxVd7M6Ci41iTLFreM2MIZqU3W_MLclaNw23Gu0KoJhDzQ9z-gB_qEWPcjhHzK6b469MvPcm4Fu3hx1RG3tA2iFRdCKQTUs9xlbH0REDmh8M92DOZNOC-AfUdn0uIPEou9l5-mvMSMDxz_nGpZg97LqWVIC3S3_ri_VVEKSjumSh3XzaE9fmDLvai7wKzaYqdyWuEndu5Br8JWripxQO-2t4sxuo4yuj60_itYIxancpScbiv2w17EKmWtW_qkNwqA4YsiUme5FDTCHHRtmdqubcMZhOTxum7u7eq5rDxC7R7Y8oJxCjg-4_zCZq59vp569tU4-gNluShbU7eOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oda-XqrSW1tKl5q11v1yWNomkyEAq-X_LrPO946gFBovVyVv8RHv3ivDBFyGtYe1TgYmy7DqCgaxcMEZiHuiDyHhq4A2AOwjGYOQAfe2kaNNzY912SDYipAf6Oecbr9l9fTclIus719Rkvr9IrVDTNkuOLgn-Zociz_nc-L1-1sHdq3suxzJbLIc1RGR4t4m6v8Xg_otRMcialX_QsYb4zfiL1ax1Vr6qbMV0ASAABpvqZofdcbhPYM4ts2K94WQ-7a8up0rPNg37N8MLty5BMWsstoskCy8Y0uGlYQ1RSAKIDtdDI0XmfDNKdFC6gFVqLD9kmEvS6JTtaokJR71xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMjyaaM7ErXgPqpWWgVskdBvYUMqf1FjF9LW-297CedudwYv_0r-IqI0Bj9dUhooPbx7viaZD5gjX1w-FtbJaOLzJxfhfcR23qxBn-moZIeZxSB_Ak1d6YQT2D4haWeNT0RXwMI994hreoEsbMX1X-rXM6ZLUxJGpyL1sngCoA9BYj5zongsv0hojV3wpHACCj0r5E94e6jB78Uym1hRhh8Nl1fDUqd1t1o81TIhK1YrJ1dY7OVBR3ApfVJGuEFr2kc69-SdlSD2UWY9p5OZz64H6x-u-xkW8sGH5NHxNCQulHnxEQPeTtHUC9F1xLBBcXBIoOAtKoNr5zoEb0NNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Md8n5VuuAEkwuAUPjOypOuIXq0rShL6WeksWAoMR8HruHwrbieQ0Aq9KnIfeyAXyH73lWYelnTWk1zyekSLnMQoSfOxLyDV8sZi18J9egKhpBZSrd1gwP2lUREagfxKy7vEs_6bPUvxAPlVRdxJf3j4_K9VjHaYlSabKJJ7WqJpDpnj_G6-N12xWgKrT5SEFgnZoVcdD3sDsAe8AJ7xLWL-i89sSkTEcNGT3P1wG2dPx1yJwN5SLm-ei5gGy5Fq1dcKRanmaHGYvqQZxBPO8nPMfSIQ6WqIHuMYUhqZ37QsttafNqbSgFY0PDvRuYQtf6rI-9hlQcxYK19eIB3aOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Md8n5VuuAEkwuAUPjOypOuIXq0rShL6WeksWAoMR8HruHwrbieQ0Aq9KnIfeyAXyH73lWYelnTWk1zyekSLnMQoSfOxLyDV8sZi18J9egKhpBZSrd1gwP2lUREagfxKy7vEs_6bPUvxAPlVRdxJf3j4_K9VjHaYlSabKJJ7WqJpDpnj_G6-N12xWgKrT5SEFgnZoVcdD3sDsAe8AJ7xLWL-i89sSkTEcNGT3P1wG2dPx1yJwN5SLm-ei5gGy5Fq1dcKRanmaHGYvqQZxBPO8nPMfSIQ6WqIHuMYUhqZ37QsttafNqbSgFY0PDvRuYQtf6rI-9hlQcxYK19eIB3aOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=fABFzod5E-IKqYaR0sSx6xtPNhss8kNPl2bPEiDG89Vb6l0UnqtMXnM4ykRobnU3fzfIzhhj5kEhTZwrbeY9W77eL6yzbhTrTNwkmabni7hbC_xh9OZR3Z7vWCKiqkJLQ1HywyYSYKwi0C4zXXgnr_FtbJ4Mf2z8J7LzA3JqaleJC4oQqcRPUS_2Sng5SfJ76wjTSwC5tGUuFvpyyDdxHNdIZmSITtDJzLkOzPqk7Dmu1XTulWtpssgAXsn601gQPvDez8NtFxpa7o333VG57MNnEwhEGVwcAxAglw0hCuDnDJOYUzl82dNLw2c0P-irTd5PA8bZWztBwBpXxOYbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=fABFzod5E-IKqYaR0sSx6xtPNhss8kNPl2bPEiDG89Vb6l0UnqtMXnM4ykRobnU3fzfIzhhj5kEhTZwrbeY9W77eL6yzbhTrTNwkmabni7hbC_xh9OZR3Z7vWCKiqkJLQ1HywyYSYKwi0C4zXXgnr_FtbJ4Mf2z8J7LzA3JqaleJC4oQqcRPUS_2Sng5SfJ76wjTSwC5tGUuFvpyyDdxHNdIZmSITtDJzLkOzPqk7Dmu1XTulWtpssgAXsn601gQPvDez8NtFxpa7o333VG57MNnEwhEGVwcAxAglw0hCuDnDJOYUzl82dNLw2c0P-irTd5PA8bZWztBwBpXxOYbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=qcfCTgyW0mSh1JDalNXfPRC3BKdBEN_1DQnI0q64_SW0fbAC9qWf2NOvPD4YHcydnWEecwzwPPCTtkFFPr0dx96szQeSJ6Gq14yExFBMWwUnMTnjtghkM98_I-c89OPPnzQLbwye4i3FlaYO5DiHXoyPhPUWylUrnzSLFIKm0LbnpV8XkuXkpq0WNXQflU1G20SBwy0sj9bdpT2PEA-c0fpMhwV2_JgJT3tJWrQ9-SZviGgVPa6hpgdMDAb0NoDwDeGXtpsMcCF7LMPC_bvWDZYBYVLX0Ye5Ef3SCFcNjKg0h9FLBBu7sYPWJ0vNv_CT8VLUzWQaS7ZlH8Rtkc221g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=qcfCTgyW0mSh1JDalNXfPRC3BKdBEN_1DQnI0q64_SW0fbAC9qWf2NOvPD4YHcydnWEecwzwPPCTtkFFPr0dx96szQeSJ6Gq14yExFBMWwUnMTnjtghkM98_I-c89OPPnzQLbwye4i3FlaYO5DiHXoyPhPUWylUrnzSLFIKm0LbnpV8XkuXkpq0WNXQflU1G20SBwy0sj9bdpT2PEA-c0fpMhwV2_JgJT3tJWrQ9-SZviGgVPa6hpgdMDAb0NoDwDeGXtpsMcCF7LMPC_bvWDZYBYVLX0Ye5Ef3SCFcNjKg0h9FLBBu7sYPWJ0vNv_CT8VLUzWQaS7ZlH8Rtkc221g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa8Ym8VaiZkPnPLaFKIfv6NWnsdlaPu8k5JORWUrHFudu19zDscvD3SS4VKLlmVHkcyO4VuUmPXA4CBFF0Wzui7yBic0Cjy5cnZ1kVSwEkynVnnIBE__uxfqKj_-oRm5DHojN1zNZ38syWIhth7ZeNdLKtlNxjUZYEIW7FT5T9kmeaOf3a8oXAqMvY86nEAGAfTinx3PV0MQfUDtgUWrg2H7IQo3SwrJszU0E5vC_s9Jw451vhhVT6GG1imqzygEy-qeOFwHDIbks4J_xveOGGi8cBtO6a1g9oU9W_JY5pKwp7M43ayM7UwyaJa3YCQZAx3at75GwLI0XtvzvnKJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=kmUyFUpFGnBQGVz4PxZWqmakxBcTawzf5haSY1x2qMxPTHwEh4tQvgUFAYkf5NuIxumHzBd-XHZfC6nHvqFwtlVdTVfjIUFwQSphIVP3E0MpVrRSUedtgF4rqgSf4nsuEo98B9irrXfHhrzxGbZCSbErhrB1T2zrrtz50kLl7fQN03RjInTSiN1cwoCvAx9MFuzPrqKhq56NvfovYI-zHuLa2zWcTUGluZEQip9ryVZBn7J9izWW_cBKCq95GbC1FVEdl_cQ2fdA1LMJer5XkbFNTYuYFbJAREaIx7nx1vemHGxjDzZy4HOQZSSWojVbr06oTP_TSx0oDvU5Pq0ETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=kmUyFUpFGnBQGVz4PxZWqmakxBcTawzf5haSY1x2qMxPTHwEh4tQvgUFAYkf5NuIxumHzBd-XHZfC6nHvqFwtlVdTVfjIUFwQSphIVP3E0MpVrRSUedtgF4rqgSf4nsuEo98B9irrXfHhrzxGbZCSbErhrB1T2zrrtz50kLl7fQN03RjInTSiN1cwoCvAx9MFuzPrqKhq56NvfovYI-zHuLa2zWcTUGluZEQip9ryVZBn7J9izWW_cBKCq95GbC1FVEdl_cQ2fdA1LMJer5XkbFNTYuYFbJAREaIx7nx1vemHGxjDzZy4HOQZSSWojVbr06oTP_TSx0oDvU5Pq0ETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=FzrvimufszNrJaTzVjf27-WonBo3lrNTsSAO2B_M2zsvKQRhoKRhEKdp-i16iEPcyxjvcGQOL8Y32-hJug623mC1UdUh0fdJiPmB0bSzOcGieNA6tYTyzRj8VO5C5Irc-cKVYhRElbptGx5EZl6JuXDaUELX6YYXdXHniiBtMYLo5fe91y_MxcdbQt6QIwMFraAEa2v9P8h4faz7osKHCNncRC_OlGZzxWcI7H55lX5eqo7cU3AsPt3G6lZI0K6exKrFvngoGZC4p7VPxKVaVcnNQ0hODq-BqDO1XfyW6xv-ftWMmOR_02iEZ2jKEmMl2dItzXWxc4Y-qY0E8iu1UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=FzrvimufszNrJaTzVjf27-WonBo3lrNTsSAO2B_M2zsvKQRhoKRhEKdp-i16iEPcyxjvcGQOL8Y32-hJug623mC1UdUh0fdJiPmB0bSzOcGieNA6tYTyzRj8VO5C5Irc-cKVYhRElbptGx5EZl6JuXDaUELX6YYXdXHniiBtMYLo5fe91y_MxcdbQt6QIwMFraAEa2v9P8h4faz7osKHCNncRC_OlGZzxWcI7H55lX5eqo7cU3AsPt3G6lZI0K6exKrFvngoGZC4p7VPxKVaVcnNQ0hODq-BqDO1XfyW6xv-ftWMmOR_02iEZ2jKEmMl2dItzXWxc4Y-qY0E8iu1UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=p5riFKZrqwHZ73SLwpycL7WmpTZZUoJGIJDMncXH2JN_3RIHDG9piuToyESkWSB4DJ6GOzRMZhBOyoHbgpW4jZsSlmrBnZ0L_xwWT4D34TbF8VFh0FLqsjPhu8kKnYquHZ-6Bx8muT0LXne9BLxDQepxaa7iEuT9EelqtpKv5-7qzGu3eDuu7j7CVFjbUZ26IuwnABZ72UMQRuiYIkiCANp28EyMq4Tq_6rhpf5d765nVtP-SgrsdXz4AQQ3Odlq8Pe7qvYRmPjZAofBWqCdnz89ul_ZU2uyfVi7aF3vfE4TQeZKLBf3TUSE5K2Ov5HJmFUr_KGV8HLBUW70KL-IBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=p5riFKZrqwHZ73SLwpycL7WmpTZZUoJGIJDMncXH2JN_3RIHDG9piuToyESkWSB4DJ6GOzRMZhBOyoHbgpW4jZsSlmrBnZ0L_xwWT4D34TbF8VFh0FLqsjPhu8kKnYquHZ-6Bx8muT0LXne9BLxDQepxaa7iEuT9EelqtpKv5-7qzGu3eDuu7j7CVFjbUZ26IuwnABZ72UMQRuiYIkiCANp28EyMq4Tq_6rhpf5d765nVtP-SgrsdXz4AQQ3Odlq8Pe7qvYRmPjZAofBWqCdnz89ul_ZU2uyfVi7aF3vfE4TQeZKLBf3TUSE5K2Ov5HJmFUr_KGV8HLBUW70KL-IBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr1DECzZ7reM8n-xXlySDwjp8-XSMhyNfngx9s9pIKEosO1IoxHTsHY9mYcDehWarFJL4OQyGJtmdQr5nCNKa7dGD49-vmQrb-cq5awZ9F-2Cv2MDyNgrN6GnCHIUuk_0_MjhTbQ_y9bRilEPti8E91AZssO6j-dUZ_8jBBFBUBXPPqvqr84UE0ByqxrWzjU1Sz5E-6vFYYTs3a-AlcwcWNHw1TikJMHeOqLFqanl2pF13rBEOhZ3Ri5nx9yD65GUvJ3EiXiVAmtfkFN1--fksaWEHwFuExPoox2DDm6HU5FP9b2jBIe6Hhk8wtWAKYvKMQIQi02HnEBZCxEsSCgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=WqpFei6xqdwFJKihZMTT5xaXX9BeFUL4dXAPbcfXVcXh-ijGgRHxZRZMYQhaU_hj4h0KdTMKx9ZZqZ19-HB2yaI8bzTcC4F1LRsJhjuPs_C1FILKGnhdUIr34msPjY5nOA2Kz2xOlyHraE0CkxnbD1Wj0R03YsoeWFTrLbRYZs6nX-YHZmqqyTfX1HDgYmh9UMeORcT0WVVz1z34LzMARpngeRT9nVJ37GEXc499hqz5HLG5f9T4PgV2o7c-DzqlHCFi4XlUr5kzNkWqOXaUdcWv0s2Wa5wvXNXCWEOu71aOmvi2OxGAKhJ5yCDuq84NFFSrp-XSvlmzTiY1eu9v0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=WqpFei6xqdwFJKihZMTT5xaXX9BeFUL4dXAPbcfXVcXh-ijGgRHxZRZMYQhaU_hj4h0KdTMKx9ZZqZ19-HB2yaI8bzTcC4F1LRsJhjuPs_C1FILKGnhdUIr34msPjY5nOA2Kz2xOlyHraE0CkxnbD1Wj0R03YsoeWFTrLbRYZs6nX-YHZmqqyTfX1HDgYmh9UMeORcT0WVVz1z34LzMARpngeRT9nVJ37GEXc499hqz5HLG5f9T4PgV2o7c-DzqlHCFi4XlUr5kzNkWqOXaUdcWv0s2Wa5wvXNXCWEOu71aOmvi2OxGAKhJ5yCDuq84NFFSrp-XSvlmzTiY1eu9v0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAgx59jIvVqpVuKlOb4BpcG_Q17g8X1mkbzFNW6_FDf4oyYT0xn1UqjYBHg1bt00r4AxsmwNYLicFRXSusdmVFrav77KeppGP5uK3yHO-JFLmY44rhziDqZe3RM7yPMHoNJBgkS-68jmvHdUhxqjK2A2MxPR_KnLjPmROlNuHdFLs6U7p2rfgb6I9idZghke40ZpwOK6EvfLZpvHYY-Qu57IFHfL6mRYH8ZOChw3-u90CqRWemD67q1J7r0SuF0_DM9FoqaAraM1A6IoSiWQk_ShzdsHAWCTUX3KECuInpfEYO784nLsrmRUVACSS8qSYfGYiLByFCWSbceIViAq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=R9mhy5cdBmwdEelncYU9SDZSQitrpWW0QNEX7SD_zc-BCm9jmMrCcPFff4EPxKw8lI0IDBkd3r8Vv-OfTNw3-0Ne3o1kmUi5FYDZYZElEJt0w0kKqcQr0GwQqtsNeks9rhPYVE8zOPGhCDOWObu3RB0vKlTb0Nxpm282AITcClgsJSdHHcuxekrpSdcEBClgXy6s3kBgYuOTzt6JXBY9m2POaHLkyY1sH4Wl5nM3le2SHqD8cNrRK7_zzZagXYmzUGDxSxVuTjNJhUuuqRTN5Kt-518y5NupBSmE8obYC6MbxBCOwvN7JRiN7SA9YsvmZjfKBEXYTF9Wgqm0LvMaow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=R9mhy5cdBmwdEelncYU9SDZSQitrpWW0QNEX7SD_zc-BCm9jmMrCcPFff4EPxKw8lI0IDBkd3r8Vv-OfTNw3-0Ne3o1kmUi5FYDZYZElEJt0w0kKqcQr0GwQqtsNeks9rhPYVE8zOPGhCDOWObu3RB0vKlTb0Nxpm282AITcClgsJSdHHcuxekrpSdcEBClgXy6s3kBgYuOTzt6JXBY9m2POaHLkyY1sH4Wl5nM3le2SHqD8cNrRK7_zzZagXYmzUGDxSxVuTjNJhUuuqRTN5Kt-518y5NupBSmE8obYC6MbxBCOwvN7JRiN7SA9YsvmZjfKBEXYTF9Wgqm0LvMaow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji5c4HvvvQFdDwQ-kilaaXS88g3aA-LWZsbmbTAzpmo2jjNbpcaADCMf9fitk4VKttMmkxz17ogi_c8HbW-OFPdMWf088lrs3lmG3lGPPlwmLAQVQZCl-fi-TbbBTuHu-68bs3FqcXbn6l5nbofEorlbN60DbqNEqoW77ObliTveYFEcAWJPiooeOtDvFnPw0XXNrM1ccL7-jkVSGR3kdrZit26Gve8y5hLxmIShieuxaZIkmRsfsqvmhx_WxBUrHPJP8RHh9Lgh04AEejllqMxhmkbAcrnpzgl6EEe2JSJvOpdF1qgdaFAlLHVZ4pTMM7iFnBs30ka2Tkd69VaIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=fCGAnfUy_aD9s91M_1u4Cjwj5dPb8A1j_Le5R61ThNCchR5Qu6tmse7MLZhILcX8bXFE6AqTr9Ub5Lut367t-phPOqDONYPxL2Owcc6lTd7AcJJNTIkU64TStU6bMycldc-CHNH3tIWV7gqqj2xWoOB8SErowjrHpO1wlfKN8bhLLNjzsIXYFrkFpMRB-I2VlDmMhr3J4jyq8mV1foZTB8RlMkjkOuBs-2VzZ6LbC8w-3SnckPQkRKMBs_Ey4SluthrOH5m1-ztQx1X6Mo8giKCA4jn3Cd9j4bpIVmVOfK38axIh-KM0DUhXpIQJqQ8kjcAeh7DCbhWvC6nI1kKtsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=fCGAnfUy_aD9s91M_1u4Cjwj5dPb8A1j_Le5R61ThNCchR5Qu6tmse7MLZhILcX8bXFE6AqTr9Ub5Lut367t-phPOqDONYPxL2Owcc6lTd7AcJJNTIkU64TStU6bMycldc-CHNH3tIWV7gqqj2xWoOB8SErowjrHpO1wlfKN8bhLLNjzsIXYFrkFpMRB-I2VlDmMhr3J4jyq8mV1foZTB8RlMkjkOuBs-2VzZ6LbC8w-3SnckPQkRKMBs_Ey4SluthrOH5m1-ztQx1X6Mo8giKCA4jn3Cd9j4bpIVmVOfK38axIh-KM0DUhXpIQJqQ8kjcAeh7DCbhWvC6nI1kKtsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
