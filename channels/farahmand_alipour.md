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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 19:16:34</div>
<hr>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ialgFhCO0J1ZtPdQAHYBKSWHdoSo9Y_1o00Gb6rLgLndnxo6YmBqWdM7edJXkjw_Jqpi4RLXT9tgR79wlSmstbS9VbeL2HzPUyU9s3_-5oB1gmr9UjGw44SsTlNnFdgoYrqEdyniXNauv9I4ewKVfFQN8AHZAZAHhwh-C8cAVLHsIM0BkiEYwN5IdrNeddfMu_tIklZH2nAkoPaSx94mSykTpIXZb29Sxrmdyigsrhqp8e6qfqCqR-GSQqHZYZJNtyF3x_3TJVAlCkdyQD8EInLZ8a5FbVGSwcrzikEXs95Efd2pJr4exc90-DetnjT1Citqnt46xpF6Io3zL_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuI1aikzVRJwSEG4z4D02nXkvnDWw_JlGF0Y0UuU0grZ-C--ra51EnVI8ZNxv0p7MkQ-H5ZkG4zOnlG0r6bV8tLZBHuNpqY_As6lGBgdMwEr6h6GXpkUZJTaxsBVkz4sWam34HZFaaBN-0oAmXkhnM79nNZ5-0unkVplVKW2Rb7NeNARCnr5yXxgwqbyKh3JlBtlqLsNpSX-mkCZUILXoqPe7qnrnTe3LKi_-AR7sNfU5HbBo0OZGyTL8NEE4stYBeMmpYpgx_w23w9WWq44kl2pVmtPXzpbdk1yCTptHjgRO1QBpSLnyR3f6B5IwLF_A91qJtAcbalw-bhxlfBL1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuepA5yjmztdzmFOoF3_dVlgn96Gi3VtJ7T1DZFqXqNt-89jtLQUZOmbj52G7LLwJrkLhWn_POTFHG41MmIFho2p97-GJ6QUqFPrDVHnj6cAMjbqUC_FWYiwMbKpHqxnLQnjI_S-DJZVBddHLYnPvr2h26b2yExxyCZv1CA6UimpKdctlWtBmHZ6iYAsyArGOUjaLjEEkyTNsTW33t7pGYp0a5YVpnHFpHENkeEHbvv-q2HZcUGAlIo4wTTna6kVY5GQFwdC1bM5xbt03KAOFdN_HBigVgwKBs9B5gW8iSyc0wUWvaVMRAE-5RcZkPWN-w6prWOs_nUNvtJq5CfNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEEby9RpWb9e9hfRPwQ_Y8sLTZNcfX3penP1RwX7b7zTVmcE009f7c9opc82aRbdGh3hMV_tfTUzyQB-aufItTDWIyhfJXjLvlceOpQPYkvqgmWrq0NKvb3CFB-O2F9aUAEb2UklQDqNsHH8tB_Po0-a7tCxrLJaAiPXgDw5ie5qnJ9qX_a1L5im8u9HmbR4-TIy-NIdte0-IokBv_HZR0xFmW8g_rHETjjc5QgsE4hHkgvIzB8gX1MTqPjSlTqtuob2KyE71o3UZiy-ZKH35AuPtUgzcMEx_wtRd5IaKBCZjBPJfjPZnBXAAwgT6bKzNm178jfSk6fptFBnC2ePoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1jh0CX0ofoIdUnxvDoYs9IX0gzO3yoLoE8a8kBXySUKNn8_yjxHR2NiQtsw3GgKx_EtQQsJNpcMchTNZ4Km_jcxTctu0b6fs57l3Tc0BJYC4lkCgDAR-tdPGzifvA6ddaPEplL6KYA9irYTZithSlJuNTTChFrAePtue30uJx5eBpK215TrzVnBqL0wRuR9_Ekb9PdahhU0d538wYT7vgPSck3GbweMFS5gTHIwh6FM2rE75iw-EXAwXylemdBHRMR2-XDlQhTap6_x12uw8UNfssmSmnU6TUZBqKkdTqPQ6tvctIoV8yUo3U0vGjq5MTDhkrF2IihblteQpuZiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=mM5xXvWXy2E3u6DrJVl9qTACJ_n09T-fITlRJm9_2urd8btQSfiBnq7uJWfmJvsqmbP1X16dllukyKBpexLdUVo4pqk2HthipaAFN3ERxaQn47mD1JIw-xi3MGjNRDdi5OxFkEgzlFlqen2pJSzruD5pp-mqGxwJ2YabB3R47KI6sgDHEjyDnaDDnwqjJ34ooOcS7-yTxZaDRqjtg7wjlG78aUBLDoMriD26xRbne_cXPtRccoyiG9dkGcW6Ht5ei291L7cWnkkvSG8FPrGidPnworQhNPqjPuHUqmp4SG6MAUCk0pAPmzwSuoBDv_6NvQQLL-yfBMZa-k8SPt6O7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=mM5xXvWXy2E3u6DrJVl9qTACJ_n09T-fITlRJm9_2urd8btQSfiBnq7uJWfmJvsqmbP1X16dllukyKBpexLdUVo4pqk2HthipaAFN3ERxaQn47mD1JIw-xi3MGjNRDdi5OxFkEgzlFlqen2pJSzruD5pp-mqGxwJ2YabB3R47KI6sgDHEjyDnaDDnwqjJ34ooOcS7-yTxZaDRqjtg7wjlG78aUBLDoMriD26xRbne_cXPtRccoyiG9dkGcW6Ht5ei291L7cWnkkvSG8FPrGidPnworQhNPqjPuHUqmp4SG6MAUCk0pAPmzwSuoBDv_6NvQQLL-yfBMZa-k8SPt6O7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=EoTZIkgwXtBoCP69cZu_XIm-TkvHaa_pB7Rh3zcTUnW3e3V8YybZHgqZ4hV9gZykN9db1IBWIFEd29q8oLEkA4xtG-fuH8QyrlvU5Xuc-4Lt0pPiVRn4ZTDUuNfShNurroUHplgA1G2BBa9eU9xI0yYOVqnNnugI9p4RjIxqcPZLbJAu9BM4d8itBlIT1enIfvz72pS9GuklCX3KrI18ZDVr2gSYLcItGA423V3UqncHliNShXvBd6e3ikKum50pMTp_sk629SNWWUjhQtwalNo7ybJ4Y9oOFBbEPDP7_SeDH2Mg5kRKumgY9NGGJJeCIQRSPHCdYsNNzjGk2bT0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=EoTZIkgwXtBoCP69cZu_XIm-TkvHaa_pB7Rh3zcTUnW3e3V8YybZHgqZ4hV9gZykN9db1IBWIFEd29q8oLEkA4xtG-fuH8QyrlvU5Xuc-4Lt0pPiVRn4ZTDUuNfShNurroUHplgA1G2BBa9eU9xI0yYOVqnNnugI9p4RjIxqcPZLbJAu9BM4d8itBlIT1enIfvz72pS9GuklCX3KrI18ZDVr2gSYLcItGA423V3UqncHliNShXvBd6e3ikKum50pMTp_sk629SNWWUjhQtwalNo7ybJ4Y9oOFBbEPDP7_SeDH2Mg5kRKumgY9NGGJJeCIQRSPHCdYsNNzjGk2bT0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRQe5LrO4KY4jS8JNtoxHwd3XBTZrJlkeAbA0Zx1fBqj43_cfg6sUvyxGZtccmWMx2b3EFi25ttOCUV2W68dXjI-CERBbbVfiy2PQwrriDd4XH-Tpwmx3darnQ02jmmESfPqUHKIUYXjHHfFuo7ZmNxdkpthAGXfj3TQY3SgPXnFY9VFdQcg2-49rn8034hTLVzz5YMFkgsXpSXQE92TIWOdFAZxgX40ycSi8bygD4De5cQsvHX5fn6GXHZqN7_NzLSZdJS2ffjXvGbj8uttY901Wv4pKBAwQ_xxRrscJtM8d2VxAo1R7AU8p8zK26ZX8gG7ryU9cMz84Kukyb4s2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL0FqVSA1HCSu1RylqX0Dh3SnM3mHe8pSori-1it913Ku9B0VTO03OGOhB50_-VTtmV9cLsjaiMdpvdfMteokcDGG60d8RkC_jaRsGn_AqlyIPYsMxG7Smg55Gb7rFJHQnxYA_xeREObUGOD3feGJ4iNlIdVLueZk26lEA96Gc-Lih2XNOJ371j0D1D0UKpt09RQNqo46eF0-vAKyTjP0-m0OaMxfAxC2Y403AmdrdkWHqFqFzLztGLuIYOTRqCLY1CMHnRnS1GTB038KaBo_MCF5UlyrKLW3bNY_o2qdX2eGIH7xtBh_EpKMKGf435P3Uvgyze4GJMzGjcR7PMVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=t0VBP-ivzvcy2mjs7W9HlABfPqhXu8MmkH-fgl9Vc20JO0dWA85kEZr2xRszH5IT2UPnu6goM_c2jHCWISPdabocfIHA20mtdRN6f-i7N_6kfucdS1_VQG6Wbe_go6BJ4riHBJsIt-sF2GPnexfvNOrTqLo5gKbkHNC8JpNPPFhue75kn-A2pL51GyWQx52rNt1AYr1kr_Ggj5R4kocyHeBCmPP6jrtTbr0YpaW5OxfnUfxP9XCPfw3WcO1VdXCXylEzBe-V_DO1u_jZTXYSwmMDos-yqllYS66BFCze8ILSLJVpAYqW8EvfLYyvNFKGDPwpMP1VM6PcxbYQFvrqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=t0VBP-ivzvcy2mjs7W9HlABfPqhXu8MmkH-fgl9Vc20JO0dWA85kEZr2xRszH5IT2UPnu6goM_c2jHCWISPdabocfIHA20mtdRN6f-i7N_6kfucdS1_VQG6Wbe_go6BJ4riHBJsIt-sF2GPnexfvNOrTqLo5gKbkHNC8JpNPPFhue75kn-A2pL51GyWQx52rNt1AYr1kr_Ggj5R4kocyHeBCmPP6jrtTbr0YpaW5OxfnUfxP9XCPfw3WcO1VdXCXylEzBe-V_DO1u_jZTXYSwmMDos-yqllYS66BFCze8ILSLJVpAYqW8EvfLYyvNFKGDPwpMP1VM6PcxbYQFvrqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=fh-Lssni62a0Xc6POgqtJSmafhMGEfGiukx_ibOTR_T8uFVJp3orNb43xHL-MlXV5XJR2yEcTM4yDD7Qd2VUooovmG8uTJjR9DV2zmcEkzWR77cV1UsUHg3_tXy7OXvaxIjPb0WnzLp-iAi9veytFXGuCkbq6EHJjwkut0uxn_LXYlrogw6enkfFlC1QoPs4JSWt7OlMeWcqcflHIBkXm3dZLnEHMJhWTt4aVlfZf00Et7IwrRmjZeumWUviW1meF7VEJsOl0JfOn-D_vvo76tWpQhSmrFyxQ14VTMj0VaBJuyd-HGra1cH8MBhTUV5ToE5r683aFkK9QOcSno1SqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=fh-Lssni62a0Xc6POgqtJSmafhMGEfGiukx_ibOTR_T8uFVJp3orNb43xHL-MlXV5XJR2yEcTM4yDD7Qd2VUooovmG8uTJjR9DV2zmcEkzWR77cV1UsUHg3_tXy7OXvaxIjPb0WnzLp-iAi9veytFXGuCkbq6EHJjwkut0uxn_LXYlrogw6enkfFlC1QoPs4JSWt7OlMeWcqcflHIBkXm3dZLnEHMJhWTt4aVlfZf00Et7IwrRmjZeumWUviW1meF7VEJsOl0JfOn-D_vvo76tWpQhSmrFyxQ14VTMj0VaBJuyd-HGra1cH8MBhTUV5ToE5r683aFkK9QOcSno1SqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtnT4eNN4TpisbyRYRXk6JkUG-jdcT_AyKlVobcshc-LZONpYnx-RyTYLGd0hL7ZCpoaCtM4MuUnwXwzlfbBQdyHh7ooCd_TBI_6Sp8HcnyRoi6xZnNdycQ3QKRGGKSOAJTqa7gYbbSM826dOvEb-UDNKJCfAj9fygm7tfr36Y55oIk8j4VBckgkK94yfHVuKLfL1e7f8y0WopGei3lwBnwmxZC4Oq3W9ufSRCn0VxDBDmfoDXvDOPLXSnDQDd8efUDHSVrVtsCbeyhnluBQHLsZ9I5AahpUbMA191mhbJ1QT48ltdSP30pmpcKketM1ueoaZNfy7l5EMWXl-NDnlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_yAA2-4SMSrgYOAKuH1WqUEn0MocDX1EQcCCkrWwUZdOUtmOEE5aP0Wzj7qcd2-1PVeMxr7An1MbeQ-ekuvwBVH_n1hON75xMeNXXf4JkhLMrqbNcqyD3PQWxLp2tXmtxCFtT7P8b0oo5qjoF9abzOYnTri47ldxF3NSbo4pjeFNNcbAFuH_rZgUokExKgAjsCOU11S5I-0AgxT6-WfGsZT-OvGLKCncT0mxLS8TaB0EHeRGWx3jYh8fQSTcCLh5IAEkQHPCCWyvwVwd2EGT9vzYxhQ3Mfqh3rsGTkTMKyiiaHiD6xHxkWI-9-Wv4N_NqHHGXZEAz5tQt86Kib-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4sSMadJqvHii4URxoVPiibcGImMY20TLhPdYGJpo6gmzts5PwOgiF473kiW1f79Ku9lXmNNzvDHFF6vVkgDuLwtvA4cZdxpxReN4mOkg7Y2I7cCAcJ-VA-5IrJqwuYvjOgLEEzyIkO53FHM2bhyB8ln-vdOo1GeU_-VHC9IO0esIkuLOunCt58JsSEJLMKLz1ZuHRewxIlcc97Jz2HGJ7e3QQ3c5U9hjoo0CLobVHCRi01EkS1640sbZ5Z9MdZu3C-oB3d-0J7gvnhoSWoqJNPzrcqc6s5DHH7ulBjAEJ_vvn1xO2iMdf3zxzFS7jXNR3iAd8FSAOncanIG8ajOnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GIedbVxsZHGX6W4XtiNCKH-dtnE0ppM1fYWpNMu3URWhl2huPjLwjkyVrpV8a1juIIgkCGkOuikWl6knuWJvqS0yGGBaOucQQUTdoyOg-xrsh_Q1X6Dk7GK2TobCLFsJxOy1FxNwZSwVVQkMG2sWUxAq0ASRMi0zSNNs9YYjmqW-5bKYixtly3l1IEgr8-APvsU4k6iPV6z6X4NpgSjRIyIEYXIMGaCKBGOYXrJa_walNDjqDvFz1B1qZsZ9YM5VimIsYISgY6lyZFs_PUgnMPJiROBVG4PL4il3K9rFg137gM7rAz25iEtKQgCPz-3FYEBK8__54Cyl_k30CJhkYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GIedbVxsZHGX6W4XtiNCKH-dtnE0ppM1fYWpNMu3URWhl2huPjLwjkyVrpV8a1juIIgkCGkOuikWl6knuWJvqS0yGGBaOucQQUTdoyOg-xrsh_Q1X6Dk7GK2TobCLFsJxOy1FxNwZSwVVQkMG2sWUxAq0ASRMi0zSNNs9YYjmqW-5bKYixtly3l1IEgr8-APvsU4k6iPV6z6X4NpgSjRIyIEYXIMGaCKBGOYXrJa_walNDjqDvFz1B1qZsZ9YM5VimIsYISgY6lyZFs_PUgnMPJiROBVG4PL4il3K9rFg137gM7rAz25iEtKQgCPz-3FYEBK8__54Cyl_k30CJhkYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwpPWS0p2I7FqIF6faVz2JpdV_IsITI6p0mg5Im81PkEqzB49YhqDZQsUnORRPh0OGId84wOv_iReFcanEZUHIDLs4RiDF2wE8wBXowj0QLL9_cSOCIiOz8NfoI0Jcx-erODRYPdVtfvgbtWk8ygSS_Fh4mxZr1wPPrDVzCDQgzSsDWS-k0nC9l2WbR-SzBVHs0ZYR30ZsDG4m-4VN4AAXFdG0KprW6-7w_KF3jaScvvd95XmKDuyL9yXxg5ZkuJ8Ch4YCNtr_jiaC0HW0tJJ79kygw9LK5nTXMcrXuqVy1TizS27UZjFuEkzVblsAWIymvyW1CX9-3LTXEzoSqLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-awsZNNzlBbIEapcoz3hh4jOeo0VUv_QtAxBFsjeDctBqCbbiMz0cT3_iQZTid7IAiYah-d3nJX_6pLFpvotLV59NHtGQSeonX1arPIzXI79schLnvMIqt8JMPL6HbOQ4pGqtn9AQREEC7gQoPVn3kk6pfLHI9LdqG50B55ku817zvWqrbSeLfQbv6NhFUOAWtrlkj4nBHyWPARncmq12tSu6tqXvJOuA6oKXRmcpruuAHinchBDWOoYhQJTXRrhSFWrJyfQ_WdJsrzN1_UulrCqSfdJ-ztEmol6V7_oXmBU_3OeaU3jxZyjT9wpTjas5ZIcyasaym9z9bRoKksLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRjPjElIxrmaD6qOxnjrfUfxlZoh-MOlu8LbYmi1NItrPSJ2YGiWoN6o44Z2Yt6CMSMTbaReRgYX9qGbVBXt8oTxLxbo_UexzaappeCvU8j6HXojueZ3nOmQ9BVWm_s4aZcFsh-CJIGacNFsg8QNERRMoh2MmtIGRQeqzZUptA1HmosY_Gn8NxDORwdBXgMOjIi98ZLUiO0yy7PRKcx26ghb0vEMcJtNQbJYeIOKzG5dlMxmTb9aeNbIHof_hDoDQrfya5tPJ2BicgqdWNnmmi0YXcmq0TwX4RvJbarFl9f9XeRGPRSRwGTLG_b2yAM3IIOhbIvvNHHkPRmt7ynLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=MHBkMfQ3Uw_OjXZgZ3jT_4d2WG8gPoTPPdOuCyAfpOLqD9kZrPm4zdY3RXzKbn5j0hcTcJo2ukxu3Rd-QhlOe6Zf9IVt-T7aqzwYIIRNHjR7ZlgtQf80n2WcWl3sxWoa1JGxtLhf4kw02SgAmB0c7gTrRta7yItfaey7q222Uh_7epEVpOecqg2cCM0OqHc1kT8ctvVe0xNFvu7Ylz0WCXYRKGesqH4MxRLGluYATCyddWebUJkFVs5gY6qJ0enuDB28i4YHDoBLlvkGF-nT97hezi274U9n_L6pGbvwSLmCMuZhPcBpp3avDXRV6nmsRW20jwiZhMm7SadyIotJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=MHBkMfQ3Uw_OjXZgZ3jT_4d2WG8gPoTPPdOuCyAfpOLqD9kZrPm4zdY3RXzKbn5j0hcTcJo2ukxu3Rd-QhlOe6Zf9IVt-T7aqzwYIIRNHjR7ZlgtQf80n2WcWl3sxWoa1JGxtLhf4kw02SgAmB0c7gTrRta7yItfaey7q222Uh_7epEVpOecqg2cCM0OqHc1kT8ctvVe0xNFvu7Ylz0WCXYRKGesqH4MxRLGluYATCyddWebUJkFVs5gY6qJ0enuDB28i4YHDoBLlvkGF-nT97hezi274U9n_L6pGbvwSLmCMuZhPcBpp3avDXRV6nmsRW20jwiZhMm7SadyIotJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLiPpYWClldw8kuW7_FpwvVBbXzAKjYFfNWju0dP3_rQiVEiAcCsSVrhF5YZ06GvdcLmCGtvyFUnPh94emBLCdFw7snDB7HIdis2jxk2HINCeht1oJaWlDy2xdJtXrudjkpp7XxHfbtGjTD2hXirSprjF9tI8TPAOmYpvxAcZN42eosKaEHx3p0S0ilVU_LUg7jAZduU88SwFgHQLoFhN_pQCEokW8OtjzrafRS6V3AmSKFWAk0PsOlARrIs1TMkzGl-1zx1kwLZxSZllIgIuGzTvEWNqWRk6ufQBgSRRndJZ9-ZdUMSdxI_rN-aEysoaq29meg8nmfsB9OXxsi4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5v0zSm9G8OWOytq7mT7JpxCCnVCz4ndhtG8FgEBdCo_-WxeVWvOJk15IcC6heKmAomU0XcfTzcNV3tjRu5STR7oPcKxLa_T1k6efEdDaNHGxJNq_EOUVoEbkF8JOWbsV7ypN7Zw644dIoO6OWK8fj7_4sbj998sEZNfC9JnBQEwJAuS5MFSkZ1NohaIFC6VJ9LjYWNIRWGYTsh9l4rUr8mP4aMkge708HIHqfYG-jpIYOjn-4MGd-BGo0U_7zbXs7DEmFJMs1WPfeGaV6q_yqC6g1fKkz4NFNrzYyGI2sKz1Hkm9EDo-pyYnNttrrxWOXlOMekt4Krqozo7bR4pJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAoACt0YHGXpS3XndGqbOtVZPB9XGbjfLeicnsjrE9yMTyNTnRUdiHaMEtAlJwpb_OzPZoH4SOJOfXETcyEJpM9fzUvpgpgaSGEoRBQlEErvXPi_aD7HwTvwyR33W_JSNmk9Ti8lVpODLeEa_8-pVR-7Xxn09w8adNPRkp9wVuu-HBAncYCyawVW8O33Z87SYprmEI6UUpnltcalIVnnrDu85eoyiLhUf8EHHS7cBAv8iZxk-mw2mBRDREcTI7ErrHSJhcaC5EkmP08G9LnggYYlD0whL8Paq6g4ICv1w17De5LIRhnBgSr0NZS62pEQPesMF2H-ZF-YOP3jgsATyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Xwx2HFv-l1j7k7zljVdnPT_xdP-Y93PSLevATwHVF6P2Q4uTufPi6MLBcQARXixMoT_kRWk466ABYbiLjgURkpPPcKhyp7Fml5hXxnfbJ3Ogl91yopviAGOC8Qq8uRjuika0kHJceKLRkSw1B0c1cgXHzv8QcGGuSdv3mXGQUUDdJXhAwdjgjOlVrz_WJd8o5QpZDXmHh00rYM0eGr5FvGtMYvgzpmCJapFB7ePa16UmqRSnUsaZgrv7YgmId1t8kM4HrrntULC56XN4s_My7W7TS1wMfMasdZ3npG85W-_kbxECS4LElxDrGha9e04STXju6p8oi2Uo8Yg-xUOU7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Xwx2HFv-l1j7k7zljVdnPT_xdP-Y93PSLevATwHVF6P2Q4uTufPi6MLBcQARXixMoT_kRWk466ABYbiLjgURkpPPcKhyp7Fml5hXxnfbJ3Ogl91yopviAGOC8Qq8uRjuika0kHJceKLRkSw1B0c1cgXHzv8QcGGuSdv3mXGQUUDdJXhAwdjgjOlVrz_WJd8o5QpZDXmHh00rYM0eGr5FvGtMYvgzpmCJapFB7ePa16UmqRSnUsaZgrv7YgmId1t8kM4HrrntULC56XN4s_My7W7TS1wMfMasdZ3npG85W-_kbxECS4LElxDrGha9e04STXju6p8oi2Uo8Yg-xUOU7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=aoJVjon43iE-b0iSqIgcu04uFCiuW3E9hdKO8Ok65Msp4_fmlzNObXoLMfqgGklYMFAfozR-zgHimCAXZDm_6HPTiqrRP3uxj6SKwnLS8M_hevPUCij6ZYdbAC5abR8HtvPeYXwkCiykbhk6UlEOkpaVBwQBUjai9gnpQrsB2N4F0vMpO07_YBy9nkobYEGWRFgy4tmuJQtsxBZLBBRBYiK0suN2YwMnmY5MMbw7w6I4ei2XohOg-_uAuLzxzUc6zg80SKBSWL52qfcWkmyKd3pPS0gCjN3via-isOGO-aVL_m2Odigiw50okpu7Qg5sm2R0CR9MDi4lBzk-bcEPZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=aoJVjon43iE-b0iSqIgcu04uFCiuW3E9hdKO8Ok65Msp4_fmlzNObXoLMfqgGklYMFAfozR-zgHimCAXZDm_6HPTiqrRP3uxj6SKwnLS8M_hevPUCij6ZYdbAC5abR8HtvPeYXwkCiykbhk6UlEOkpaVBwQBUjai9gnpQrsB2N4F0vMpO07_YBy9nkobYEGWRFgy4tmuJQtsxBZLBBRBYiK0suN2YwMnmY5MMbw7w6I4ei2XohOg-_uAuLzxzUc6zg80SKBSWL52qfcWkmyKd3pPS0gCjN3via-isOGO-aVL_m2Odigiw50okpu7Qg5sm2R0CR9MDi4lBzk-bcEPZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU-71Ebm_XbpDEPoePmRlmV8eyWKh0lnDDRWiEIRRalpaGuTTryODLfZHbnGrxmJT2tM8AKaevVdtaQkg9HCkGsuf0lPodyt1Re6IrlkDGQMXI_G3a89jqJ6qdxDuYmEFIlbf6WneJffYte5gY7E25rV5jM62b5kX0bk5a3HJq8t-Bba5pTwgAk-YxH1xcNr5JRnl4t4CeBuzkHZ87fFQS6K66l4DXItg6nueoGyTCo4l5DoouzNESjvVZXHWJPh-m-_aTSPEI85nBzcH078d-KSvBeXv5ib6lBjTVVrvAAM6o-JUQmRJ0STZrT0a3DMRXMXQF2cm_ALnuK8kjxEcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVcXFJ1Tdji-wa3956mZHX7i1sELqPlf8ooAykkG-aRK1fnA-4lfJUUbNMARk5VVWcWY0hqZWDd_pVbRQvnNtP6hJNE5-yBCurMAdyof3dsNHqv6gDFnbkJRLRnTd2VVk0uxodpqSGMjZJ_07La4x4PMWhKStSADzLMvxXdkyFteJboTCqayDqu8tia_6ayG4kSDJQNkKinttNRxnAR8MIBDLmaw_NAtqydNM1o7ZhYC8t75xx1QdtCn1tDuRQXGZSQR1XtBMddQ3v_NwT1EnghPURv4LfyHmI5pmVBvHwqPNlsf8UTPUrvmp76iNtAqH0umOiPhqGv36xWpULp9gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-MqVNEnICWuWjsYeLbvT6kr5N9vC2t_dL7VOr4aXvL3YY9CuT9eMgWo0i55U_A0inbuPVkXeNYLI6sg_xWb9haw8neU-m8aNe2mPP6CjF7JtYKiAZ-jJ5L3A3TrFpOkBpYWVY5AJk5YEXrCWRiYqwqBUdtbSIFF0VVlGuRrb6RnY7IeW4QJNSoKDBmfJc7j6o3yc4SAcX45fHDrZHu5Wexn6Hl1-0no13MpVoFILTXkn14AzXZFJpz0N3kaNNfs_qhpxb48s5Z_1gn4MGMMoPM-QXNTrGfz1TPaIMWi94ZsXVHhjP7RKlrkEPZvHNtvf-HPXZKPpcCRUadvlVfo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV7O4x0kHZ-sb1Kl110vRNhZqupo3N94D8YxOU9LLwdhxklNyvVzvShY6mWCRlcJ0Jgi_ZrRYg9rVc42EpGQVXteZ_WFLl1eQ_3qRK0fSdvH4E5iZnbqTiuY5ln9vjQC1fCs1jMMn5JBxHMvxrumZurshlxgmg_qS9wGdgqs9kdkWtylhEpbQermWKLIbJngPiGsss-qd-Yokh5zPSGam7yhavmiNlKv6atXyA7Qz2jrZHzK4h49cLlynab3D35mOlLmj7dofRiMYk9-1QzVKFTPQSsy574nYD1-mufHuyYrrcK6jeY_ip5vtEm_jWYVDQO45N-VNh4-8z2jEaP08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZ5A1bkC4NDVVrntvCycdgCYsdqvKTsYPxVdfTD1-rEcjXTmixsvaXSw7diRsnomLe9I4a6QJRvRXyOF7YKpasI_PrkC99bGt_0wh2p0Z45aZMWhFro9GR750YhG36s9JtVE_dSkct-__DZ-gA2Buk1ZHeMtAGCLsLn1Odbmr6KTdmPGmx6oEB4aDjWRyvPP0iN6p_4qa3oeYNfaO67lnC2307FUCEdP9O6M_MK8A9ttMYwhBActkfGMHvvqV3GrFKO0lQRYITwodInu_FOgUnCIH_ynFpHdMaoCOzwwJSkW7T_LMhR2M7oKX1tByPJs_Ci1JiAnG75HBFzZsW9MXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntKfu5EjFcT2N34lrpA_e1HqqHtAEiD1umSKPVNCv_2egw8jjzDxsqcAhvUpIAn8kPLdV_BVVn9aCeQV6N-1QCw-Kl4rIqRFNgzPGwJGj_p3jwyIJBU_G1UUsjls78okst4pusi2oUqCfNPnr5DHXBtIQC1GwKONshXza4d-hRGedYqOZoZtBkT1iA762qysdz3O5pdWkQGVBELTt69_LxOobpVIm-ZnZykb96iaBhCGMUasFiwSR2ykSs7rL7kfGvLlN3WkQt4Z5jar63-xasvFugf0Xw5hGSz15up3JT-SfLBcDBkXMFOVTge08Svw_2e1i_SDWjNJp_ddsn-jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtZTCibS4qNLQlRRJ0cyM1RZON4aFjB84c-n7bgQXsYtMRnkYMUOENlBalbN4h_-KUQVvl-xAKBUcs2ky2KiluqkcTRQy-f4TPZpfZiJPyXIQtb9HSGJbuP6JwB9y-0QBT6sLSQ5JR8kDtRD1bd91q_JocTEpiJ5n41yaD4Z00mnYxMnDZQBoouA3T_iJc1qx7yWAhWA1lvz6B2ZiZYurSVr1k6BScB4FpYH7oeBBn8PmcLVqqDg2b2iQ16DgBKrykVWA6P_3cZ0h490FHNSxweBGJMz5WtOLapetR3NNtBligxSnc4Xj91ptz-DOe8YIi8Vt24PkINdSB4A7pcyfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uACX6JoDeGD3_2tgrUCXrPqxmGkL_FbsNfM7a2akt08ZzkvBIU-V-1Sv2DNv_iSccVFwhacxviTi3mhrb10mJs6A83EpN37R1DcIPCwaGve-Pd9ggBZu91UVo5oKK8qlTpCVasOwPsAzEZzhjSMbAbGeZb6tIRDRn2MER-QUK17TCRVXgJW8P8mFui2oNEzpZEkZ2qECoXIk4jXwecTvOgphK2PJUQQrcyDYmVZNrmCyYoPjxDe9PO-lyV8kBMCKiZb0NRL_V7uVSL5pxhAnBFNNmS35rN-VBOzGvkMpUEV6iY8vjTeMlzBoOYxClwMNisnfxC26siP8urdO2U7q0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUw3hju99I7tdEdMhqN30nPyT-y-qacsAkmWm1VJdR9yhpM9-exdP7TG3vxbWid7h0RqROeprfMb4mQMVl76l4-5tW8eHdInKYtrZjp0MtI1gsbRvRec3H2OLw5K7Htt_ffzwfOdgFtY06r4hHu7A8ZHRh8_4n9A2xMxuOhsqZuELif8F65lImTDpRYlnLBRAbDMPAK-tiIptJ1q9xfAPMAXtcUk0V85iacektDcmpd5Oh0RsnMODhPghbg32G4hWI0zMeer-_xFx0DCie9LjbCgcUZkMzlwk-LkNbPesNz86Pvg9VnoOZBih5nH0alJRo_h94fYMCoK8_L9XgH3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDLyHKd6VN8GOVtJv4DU4f5RuRGH1SlfSjuCeKZPbVKsahvxjn4Pr_lBTWFuS_HZKwiq51pNA7TKfNt2zr8Gs4OKu3Fs2m0cFBYlSxoHFj1RP2qw0x2HCdMNdvB5XrB0X9zD-Oy5m63lT31pYxzHtoKas37b1eRkh12I2WnKHy7g9AxziwUBr_G1FMqtoITS0_nnqTwNuKBB9hyf8pP2GeNHtw_hzeZ78aObrsEkutmSN3pR7mgTkzKRgVGLvUW76Fa8c-bAb4PAlq5PlB_3jRPFBecdWiiRaJyJlMOUZGtGORhKivLNONLLvWcbPhq6GkqgvdnJDAZ8E18JkOQUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az7ngpcYuwsv-AKBBPhMLdYMDHziWGxEEJBW4W9OjIKiTlhu5NbAN-9SFOkl0yYc9C04perxb7kcus9fkkuEa12huFG8IJuq_6YcvRE2IsPZb3mCQ2JVaMEEIpqGdLMX7yViEXklCZ24IhDbTpmbpDX8Oq3OjDpBv0MHlNgV9HlXAMagbsx9PItN0u7u9Gmp77N8UJDOj5xwXS6Qk2bTkaHaIjk_LFQAG5mVdg91cHye5HB0lfsbr7cH4YYnq3DUyAwHgHWX1iNwHRNLuSxG4s-xVhSY-sqxD40XnU40VOp817sskmuH4sMmGVCmi_WOmLhvy0AbMbC2xwJOdyBg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWkPb68Vv6NDRZNVZywwllymXyzENOamlLOAoMhcg_mkZ1g17F9HF7oKXUXu4rs9D5-Mjz-GBPcoP4BruroMQTF_nil6UFPXzYuDSCkrz-Hkfmv85Kdzo0RRMK2tgvN0uuKoEBfUQk7DxBlRPCaD16wI4jk7VMdaxR_ofyuFDC56_iHEZkLNCIGqXuY-KPImw8P7q9u7mdsZw5S2or8YZEOzGPUKAG2n1M62IZAVJgaNHqaAA7IDOuaBPvJvOX0DXxXEPHau6fGifhLJ0H39jvTLj8RKukwYhCumtiYztJU3_OeREWTwIhhiks3XniHti76hGbI2UrZ3CwCVjTwQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxCxQtD4qt4mw304aWu2LVzrCD3Udj1S80MZEwMTeSroP9q0QSKz9cxi5To_1OEIiH_fJaVlEAkUENmAuz_FZdaC03K5CPxc1vKs2g4EmoUAOjmF67t-rqrYZ9SUandAD1sD8sMvDgkUGSr4Aey9Ip-bbSpZwwSMCPJIDVmSJc6DuZxHXfLJaTZqfDXPJK5RmtFR4y83tlzOjzt7KzhXTjIHKo2256EggO5UGa-IQZ9uxzs_NoYq0AoqRW6gqz1Vrz1lI8Epp9qI8mkm_8HGrtEDMnIqefzTPFoE_q_lXKYP-uC-ZndoAu0tUSFoyjwzCqZD1LJ3fZmitt1a6UsWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE9bI3-LDGwBJUi2x9Y0odLUVWTgqg2M1KhrC1n4UpjEWwkd4zKscRy1cKAhXFT0UGMUw_a6qRGeUSckXwdFDjAYfFL6OU_dnSmew51mLmtw0imcc6L499YjzGeKDAKyqAnsPARk72gOw6QWh2WSwYm9Nvegk8XsgH3TgI3dZASneZmV2-fqKXvs78OjkQ9n3kJ3-d7OZhwle1zIHlzDRQceUQ5Buq0KIRn1BXHBzcLZWdZfqNZuHMOaLsyK20eDA-K8p0Ays4d2dTedhT4aIfva4xPai0NaFApra3gitvUb5R01o_DB5b7oRCW7rcIiYM4lk8ZH_kl_81WPHyQR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmVotSCdddU6H3CjRBFqFR6_0bAcm336Ut3rQ8Xui1IVPE-wHDw2eyUjW6sq8S-Ert4MxR3XnE818_hTcfVy5nf9GcYbcEBIfFD9bDv7ETyTt7xyj8iJN2kfitKC3Ok3XYCmr2OdfgjWBBCbbXH_KzYd_75ATsfzUC5i2FpZJIt_sSSRXeD7RuqQZWxrQGx234S6U-y_HSB9ySbRlahrplKb8ZNZUTNuJbJU7Ej-KjmW4RGWGaddggNx-D-R92HamgO_oBIKxteXLw1a-MRqiWh4EYMbIeTWzDy2n9amUgX7_mQjDd19myGBUTrm3r9Zpl23R9i9eC12LGF9cMPxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=kwb4UH-TC-3x5_gOmhxwJs-ROphgSSe7GRJQyYzdeUhg0jIdJmK2qNiKmxOToqyE9rJ7oFk9JwEsFFw8u0Tz2nbtoU4Ifh6Zv9cJ7bk4UmVLNt8NtPAcbD_Xk8YKfg67FbwwsQq-FiVKeazADre_pIzlSzA2SuG312av_yR_0QLvRLZLwtNxLc3JQfCwI_OBr0zu2asdhD1vWP94W2HUiFrt9jHd-DGSlZoWurprAL-x4S2fuQTyofRm9i7AlbQJaMbJkPUGNnICzG6zQHT7azv41GQdbPNAjm0d8dHeRE543fZL-KDEltkeyv7WcIPUn7AjGgfueQaU6jYJjb6YKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=kwb4UH-TC-3x5_gOmhxwJs-ROphgSSe7GRJQyYzdeUhg0jIdJmK2qNiKmxOToqyE9rJ7oFk9JwEsFFw8u0Tz2nbtoU4Ifh6Zv9cJ7bk4UmVLNt8NtPAcbD_Xk8YKfg67FbwwsQq-FiVKeazADre_pIzlSzA2SuG312av_yR_0QLvRLZLwtNxLc3JQfCwI_OBr0zu2asdhD1vWP94W2HUiFrt9jHd-DGSlZoWurprAL-x4S2fuQTyofRm9i7AlbQJaMbJkPUGNnICzG6zQHT7azv41GQdbPNAjm0d8dHeRE543fZL-KDEltkeyv7WcIPUn7AjGgfueQaU6jYJjb6YKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWzg0-kKsKPNG3Z6LhQOX5Tecop7aPg618aMFHUhz0KB2DviH1SeCUYEA6mQiFT1TYXe1WmVHavYuWrE4WZCH1J3agw6zOH3UHAzOParIVcmiDwM4n3iLZ10i9tRSlcRDFTqqpkRF4VeM4GSkd2GeKx69MkezMwJxi7zl87w85pWNaksQ8WBaBG46tcSNMhxHfH_usfRkWdUc__DAc1766O0UHNfAPmVQXPP4sIX2ml-OHyIzdDXfwm03Yo0u045JzU_GztccUEc-uq7yAaG5uGL-_eYrjnE5muBKTBPzEsSPUPEUqnRmQsz7CyUMPY7Jr4BRR3OjtMKV5aYbM-upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=K8HUt1uYi_wpgq5C-4InCtFtI7PyP41ljyEpdjHIgcNEEKIWm5n1yaRMax_MgLNMno_3w0NKDqzBzBp6eMSnGE04jESnGUKfTm6boI_cDsn_S5DGxQSCCFhxfIllNZy9aUxa9Bqga8SBQPV_CF2cpnYFJBRxCWqv3t42V64_NmJx97SZRwQ66mCvsyWHNJpqSDSivTi85YNSGBwDDftW5Ku7PWWKB7d3Wno-lnWm4MMh2SU1hbaQ6WHYWprt57uigFAe-1gmEwzD4rqrvR2c51o3MANtomQT-TYG9Rdib7Noyq7J0vCuB-R3zPvSOQGV1Rw1UQwqlsBBmzn5DsWoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=K8HUt1uYi_wpgq5C-4InCtFtI7PyP41ljyEpdjHIgcNEEKIWm5n1yaRMax_MgLNMno_3w0NKDqzBzBp6eMSnGE04jESnGUKfTm6boI_cDsn_S5DGxQSCCFhxfIllNZy9aUxa9Bqga8SBQPV_CF2cpnYFJBRxCWqv3t42V64_NmJx97SZRwQ66mCvsyWHNJpqSDSivTi85YNSGBwDDftW5Ku7PWWKB7d3Wno-lnWm4MMh2SU1hbaQ6WHYWprt57uigFAe-1gmEwzD4rqrvR2c51o3MANtomQT-TYG9Rdib7Noyq7J0vCuB-R3zPvSOQGV1Rw1UQwqlsBBmzn5DsWoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=YY_M0Bhc-Rthk0mMr4sEHFJd1Lt8DJmq2DXpHxGDLX-AoXsUOhKg7VyvgM8Te5E7TF1r1BjdIiTvEingY8PKSQ-BluD0W5TUsDgUbZvIAtgjVlJEWmzaAuiG45Vbxd7bzL2M7on3yk_UPJBhjvnSlWDnDyy0imgHUsYc109Uqdxnr8UitEwCdP2WJOponcTEvroEfJmf2O9Msp4hsC2l0uN7l7mKI96DIulB9XI-4mYjHwW6wmLs5_eZZEAYscIaf6nmxDM3CBzihjl4_fSDZmY7Z7C9uqF1XhnEVnEirOi8IkKIJo9cmoXd7YeToI-3jo-Wnxpa1gjQEszUsiZ_ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=YY_M0Bhc-Rthk0mMr4sEHFJd1Lt8DJmq2DXpHxGDLX-AoXsUOhKg7VyvgM8Te5E7TF1r1BjdIiTvEingY8PKSQ-BluD0W5TUsDgUbZvIAtgjVlJEWmzaAuiG45Vbxd7bzL2M7on3yk_UPJBhjvnSlWDnDyy0imgHUsYc109Uqdxnr8UitEwCdP2WJOponcTEvroEfJmf2O9Msp4hsC2l0uN7l7mKI96DIulB9XI-4mYjHwW6wmLs5_eZZEAYscIaf6nmxDM3CBzihjl4_fSDZmY7Z7C9uqF1XhnEVnEirOi8IkKIJo9cmoXd7YeToI-3jo-Wnxpa1gjQEszUsiZ_ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5PVozl_RlZkVuHCb6O56ZxbuG8jshPHUuZtJm_r6hf4U2HArghQ-JAwBz12r_fC-feS4Umx_U7FZTpL3gBoqkCLBJBNOkPl0aGvgSmvOadztROtqbO9jq_GIp6NA73rJuOs1xsLgV5se7LNypX10HyqjyhZ_cHKkfMZkOh1Odls1MKYFxE7EDDwMbcAXqZT46egto4L1dajyOvM9GhefZNH_Hxlohu9Ri2iN4zE2PYdbGsCOOQsNOGHcMKnrPcl3P_b8SkekspD4l-utalHSCkweJ2XwahXjQ1L7wcGh3jEpbr1zzpjEj-1BaBS3wJecjcx3PQni77C3s9MDDVLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=LHiF4mLf18jAAMZtKKSv0C7qg_Unfq3Mx4vIKz81N8ee42vWYC6BjIxpfG9OTnRyWHHUajzuG2sLy7OBMxXxGfJKgeRBttyJq6_jSIwUxOOnF1cZIfJP3cPBb4tDs0x2utewO3ZQ3QPe1nQ7fzoNPtxJ-T8CUog9i27I7p4Z3YqvjHMv2Pd4z5PTGLFfMCR1YGaLWADNcFvMT081ugkQSQP5DnAYo44fq4G1_gCwwMPn1zp6NyPpfJ1LUhctz_HgIvUatvDZHCpufva7F03WgVblo3qeTS1b7uK0kqjYBPH9lS3qGUkBZTMccLtvIIqVPTqhlp01XrUK8-EJpZZ9-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=LHiF4mLf18jAAMZtKKSv0C7qg_Unfq3Mx4vIKz81N8ee42vWYC6BjIxpfG9OTnRyWHHUajzuG2sLy7OBMxXxGfJKgeRBttyJq6_jSIwUxOOnF1cZIfJP3cPBb4tDs0x2utewO3ZQ3QPe1nQ7fzoNPtxJ-T8CUog9i27I7p4Z3YqvjHMv2Pd4z5PTGLFfMCR1YGaLWADNcFvMT081ugkQSQP5DnAYo44fq4G1_gCwwMPn1zp6NyPpfJ1LUhctz_HgIvUatvDZHCpufva7F03WgVblo3qeTS1b7uK0kqjYBPH9lS3qGUkBZTMccLtvIIqVPTqhlp01XrUK8-EJpZZ9-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ousq9V5LgrWhGcf703DvT5VQ2NdFAgZZv8gaNDezhNNWDV_jAbFlxPGitIzOZ5JF4p72lOytPMVbkAQOdyMeafxzM_95OrK3Pck_PxP-XwK5PUAKrqyuIokC1B7RtksMyg5WQWLZihWyJC9htXAC7dobMwZHctJbWAvqCI25g-0andZQLQ-rc2FPramXnZOlFjltQTig5OcIbj_blaGCw1-F8CKuHNBd8KhOY4a9TyBEPaa7r2fKlm_HPa5sAArawsqrMm56YL1MLpNZTTFsAaEYYBnNuHykSSe-vPZ_n4qcdh0cl69zxUq2wm1V6H6usT0597GsOxErzZUPp-wrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpxnQKslSy8YLQlKEFmtsPDgwqTzIIhHxrTkhRc4ddAe0ws9SkxALPnJaUgBIrXeKmQCLITIHjD-6lofxyinsesOd5bjWkV4cHk5K4iLBIMY_HA-pC-VYs89lV3h64AsczjBhVt6y-qsUPJbTn07xVy6FlUcf-xfGfPw9HsV18QjaPzDnoUbbKT-3G8ldwr3mDzr41OIssLykBbIXjS9C00dDkPAfeAOcpL2faj-NJ49Uc2KnhjrM17fppdeuoRb39p4mXH5qRPvZdSpHWrtVHKNQrg_DBVrDreg-26VenPQw5kMXcn5r06fV4sZLYHlLUMo0vAh3gv0TJimNgl6ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr8hN-iwDE1PkEBCW0U4cFrp5aBM_jh9eGyThx1zTrAH4eSisVkjqkRk15tLKo3xtqCAHhpkv-dg7aN84qkCRGvOrqnr3aL1nqWlj25al01JGOIwOUjSTnTCCJHScyaggO5yl1U9tZlCb0TKNbvxywiWLwE8_nqAVvLCngVH4CJeQq24LwYa0_T4_Q-G1sr4VrUWkK_PznbmKQrIKOkNAjPku1xAHNK7o6kYmsBXL-uFHcmEtep7d9QQlao4F8z45ibvVgE1-UlFKUUWjFzLp9LPAm7ViKEmMJh5y-xJFAutwkp8rCWlQNmWtxytR-p0jqVFJppDL71BkS47yLoUNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdIulshoVgaMKu_xZns9Ytw9819vXEbWnRdjgg2YvNdmJkR3fBJOAAZGIDZjjfpOheoyX1TGajPcG-WD1oUHbQQRX4Oh9MyUmESM20m7uM33SA-313qyOutAWf2qtM_EZEeG3dn8k32jXZv-JhNvu6d5bCR-CahXEC28kcO-YiFiEkmGTt3K8M5tmzmO2Ziq8y0w3yTH2G-y3BY91G9R-Vm78bBHui4E2pWT3_inAcfCQpXPDcIjt2YdZHMSnWYP8vp3cjOUDXyxPN0crJ1Mct6KhOnKyP0TKN2RzlcO-WnPNw9R-SbyxE3KW8lS_BFMZNkKXKs-x7W3tWclVfsoyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vzH-7xfa0oJr5d-hwyX6qDTKaDeM2ygYP7pZWdoNy4oB9IJ-DhqVfPKxWG6VoFnA1D0a5TVuqx39l-t8enIQ6lQmhQqPAqOwxqvJgmtYcdHq4Tb73PF3XfhWYZ0kcYWDLAXBfNtVhzLDUT0Lb2diTBoDT2xbdeanBW-5Bc2J07io_7B7Hsn2sCOYV5cT2uW1NjXI9rmgr2_oca1_onH6AQPxxltgPbXHFjDwX545eA2YZsD1qji26lubpSlz_zNmlkV1TZ24cvGNm3TrEUa1APXjQzwLvfTpPDFuea-BD9Bx_dLfRiYHyxkmayW_AiZtQLLLL9yJZNw09P368e8atA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vzH-7xfa0oJr5d-hwyX6qDTKaDeM2ygYP7pZWdoNy4oB9IJ-DhqVfPKxWG6VoFnA1D0a5TVuqx39l-t8enIQ6lQmhQqPAqOwxqvJgmtYcdHq4Tb73PF3XfhWYZ0kcYWDLAXBfNtVhzLDUT0Lb2diTBoDT2xbdeanBW-5Bc2J07io_7B7Hsn2sCOYV5cT2uW1NjXI9rmgr2_oca1_onH6AQPxxltgPbXHFjDwX545eA2YZsD1qji26lubpSlz_zNmlkV1TZ24cvGNm3TrEUa1APXjQzwLvfTpPDFuea-BD9Bx_dLfRiYHyxkmayW_AiZtQLLLL9yJZNw09P368e8atA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XQ9k3VGyNQHvd0FQrqB5u03nvdhbTvxbIWfPXOpkHXX4YYF_l-4rPZ7naTX-CNju1uTqOUR5-cDy-Yys-oSCFF_DYgyTKOhTgzxJHXCEJhC2wEvXAWGh8z-k0ArzEzG4jQPadt-fbIshvo095cmlxGAZKURxXHOT0cj-nQy5fCEkxU6xdnHhG2sazcH2VbOdg5Pi83gA4rYSnRqTNblmRiX9rvfHMjnytPcj5YFNfiMpkxH1MB2YxZDRQxzP1PCAIln70MA_a2OFcBiY39DOwsTtumMR3RZbIe0OZx1hFnGFjKMbChpppw6akDG_0KpdZDxOJ6G-xAxuMQo7eCQk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XQ9k3VGyNQHvd0FQrqB5u03nvdhbTvxbIWfPXOpkHXX4YYF_l-4rPZ7naTX-CNju1uTqOUR5-cDy-Yys-oSCFF_DYgyTKOhTgzxJHXCEJhC2wEvXAWGh8z-k0ArzEzG4jQPadt-fbIshvo095cmlxGAZKURxXHOT0cj-nQy5fCEkxU6xdnHhG2sazcH2VbOdg5Pi83gA4rYSnRqTNblmRiX9rvfHMjnytPcj5YFNfiMpkxH1MB2YxZDRQxzP1PCAIln70MA_a2OFcBiY39DOwsTtumMR3RZbIe0OZx1hFnGFjKMbChpppw6akDG_0KpdZDxOJ6G-xAxuMQo7eCQk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=qN_9J0NOFqHV1G958wFkU1ss_FWUPHpkNLFe22q49bsswyhxIufCa9j7sK3oEHI-2hkM120yGCsetQ9W5WPIelGNFGx3W5JAK22zQC2IcztNoSZ_S7bnWyUqt9wki0HENDap5bhqQcxDk7gasxHpKFL3sqfH4gXkxqPHrRvl30bXqr1sAX0IRbnajz4cceraw8y6AQHKRj03A3kPTt4LbM6hx5j5YT8S_VizePfOl_jeXXlyaAfabvLUHIh0YmVtbNSa4eP9-U41SkPJQDkBkZX9TnzacIFAfMu7GL52QJkhMuyghO-LF6eEqBBQ-oVYIdoQt1J8xC8k-hPWLqHZ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=qN_9J0NOFqHV1G958wFkU1ss_FWUPHpkNLFe22q49bsswyhxIufCa9j7sK3oEHI-2hkM120yGCsetQ9W5WPIelGNFGx3W5JAK22zQC2IcztNoSZ_S7bnWyUqt9wki0HENDap5bhqQcxDk7gasxHpKFL3sqfH4gXkxqPHrRvl30bXqr1sAX0IRbnajz4cceraw8y6AQHKRj03A3kPTt4LbM6hx5j5YT8S_VizePfOl_jeXXlyaAfabvLUHIh0YmVtbNSa4eP9-U41SkPJQDkBkZX9TnzacIFAfMu7GL52QJkhMuyghO-LF6eEqBBQ-oVYIdoQt1J8xC8k-hPWLqHZ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=P_9be-jm1XhhrHYpiXwkHWSXcltcnMy6JRqp8sExw6eMYeK61iQ3uxNFS2UVca36RqVlnlWkNBuFPhqGaH4wofIO0jJ1oGDoUeG7koQXNYMFxSkURuerDw77xY7Ka54efEQUUI5yEgcDIRA0_vkMm2-YU02oOTVMedLusiQ8epRKmSTsJ0U4aCAgcySWGPX3x8S12y5-w8t-AykSpI0Mo_1wQtev8BUsGX4wqOEFZROPNrYsAWFyymdupQL9j9P4AztJ5VZxT7C0Tr6pP9U0BBiB52YRPYVG1j2ZmT4jbHiwvEThjqnJjsR_BO9is1E28V1AWh727H0qH-u-mx7eLQEIL2-ni7Pt-OXyzpsS90J6jneigr-4fsc_4-aRFmoeudTSJkqbchVfpMiF-HbAMbDrzJorMazyt3xI7kJOUm08FbwnBisNcL_qKYLjo0oEcN87z2JyyuoY0ck_XvfiQc5xC0egYzHun0gpQVIffJ6E-Kd0wa7SGqjuX5cWki7BsZ6P4z04DjokjAERhRX3ShpGQ0IL7jSrRx6DbnlRt1sxS15DKfvR37V3iZmTp2kzWLIkdSC-RUSpwV8lyYPWNusFkP7872YLgT8i3m2WXAzWQ0yWgmhOvIqT-7wFB0JJGj1-e8Vfq18RYR1aJtJq-ipADWci8kMip128snlZuhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=P_9be-jm1XhhrHYpiXwkHWSXcltcnMy6JRqp8sExw6eMYeK61iQ3uxNFS2UVca36RqVlnlWkNBuFPhqGaH4wofIO0jJ1oGDoUeG7koQXNYMFxSkURuerDw77xY7Ka54efEQUUI5yEgcDIRA0_vkMm2-YU02oOTVMedLusiQ8epRKmSTsJ0U4aCAgcySWGPX3x8S12y5-w8t-AykSpI0Mo_1wQtev8BUsGX4wqOEFZROPNrYsAWFyymdupQL9j9P4AztJ5VZxT7C0Tr6pP9U0BBiB52YRPYVG1j2ZmT4jbHiwvEThjqnJjsR_BO9is1E28V1AWh727H0qH-u-mx7eLQEIL2-ni7Pt-OXyzpsS90J6jneigr-4fsc_4-aRFmoeudTSJkqbchVfpMiF-HbAMbDrzJorMazyt3xI7kJOUm08FbwnBisNcL_qKYLjo0oEcN87z2JyyuoY0ck_XvfiQc5xC0egYzHun0gpQVIffJ6E-Kd0wa7SGqjuX5cWki7BsZ6P4z04DjokjAERhRX3ShpGQ0IL7jSrRx6DbnlRt1sxS15DKfvR37V3iZmTp2kzWLIkdSC-RUSpwV8lyYPWNusFkP7872YLgT8i3m2WXAzWQ0yWgmhOvIqT-7wFB0JJGj1-e8Vfq18RYR1aJtJq-ipADWci8kMip128snlZuhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=mQPB358U1Wzb9ycSNqAM0X79OXS8CUR8Idih_i-KepLUWvPl6qTz31ryDkZ5YHAFeJLQaUjD0mwpEpvwlOQcZe0mX3-mdZ3UDFPi2ED8dlXM1OhfjNAFJ1otQARTfsVEGXlMvmFHBT-vUAXtomc95VnsDle1col8bRPszpfmPLoRRUsvLkcoBaYBEopXMSdKj1ofHxaEVvG0rhs4hZGI24vCbGby-zmcQjNwI0Hw5bYZdr9-gWZ5XPZOFO7gYEUMvPUVuJhBzy4xMoUjdKcwIaOAZChv6LHEjhsPY3gfa2r3mRcECKc-UEM9JA3QN6K7t3lYFBXYFl6T_izxdx4hEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=mQPB358U1Wzb9ycSNqAM0X79OXS8CUR8Idih_i-KepLUWvPl6qTz31ryDkZ5YHAFeJLQaUjD0mwpEpvwlOQcZe0mX3-mdZ3UDFPi2ED8dlXM1OhfjNAFJ1otQARTfsVEGXlMvmFHBT-vUAXtomc95VnsDle1col8bRPszpfmPLoRRUsvLkcoBaYBEopXMSdKj1ofHxaEVvG0rhs4hZGI24vCbGby-zmcQjNwI0Hw5bYZdr9-gWZ5XPZOFO7gYEUMvPUVuJhBzy4xMoUjdKcwIaOAZChv6LHEjhsPY3gfa2r3mRcECKc-UEM9JA3QN6K7t3lYFBXYFl6T_izxdx4hEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=PhkuyGVs03bdWMIxHgAwCe9O1KBGSVjdqEEuFBrQxFBfB_q8KfshS3Omvl8FhzL3mTgmu-I7PJAxj_eBMVu-rOAOCKSqN4R_Nsn1Pf0_VSilB4tySg072X1U3hHa4YRcORigIXUNwq8Xt4OmXryuW6zBrB29OOn7z_LLqY3oKVEatYmuaZ__noGoUjICQR1roiWpJUzYH1QY5NM3b3cWy1IinQysp4Lf6dq-sOROXOO7gc1O_kFH8tvRnXPK8jUFSrQhhS4YU_VnYCf8gjA5ObYk8CRli23QekUglqx7a0A566HbXALubJnkhmdCL8WJ69XSuV9L5PuLsVjrqroKYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=PhkuyGVs03bdWMIxHgAwCe9O1KBGSVjdqEEuFBrQxFBfB_q8KfshS3Omvl8FhzL3mTgmu-I7PJAxj_eBMVu-rOAOCKSqN4R_Nsn1Pf0_VSilB4tySg072X1U3hHa4YRcORigIXUNwq8Xt4OmXryuW6zBrB29OOn7z_LLqY3oKVEatYmuaZ__noGoUjICQR1roiWpJUzYH1QY5NM3b3cWy1IinQysp4Lf6dq-sOROXOO7gc1O_kFH8tvRnXPK8jUFSrQhhS4YU_VnYCf8gjA5ObYk8CRli23QekUglqx7a0A566HbXALubJnkhmdCL8WJ69XSuV9L5PuLsVjrqroKYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3QeRTD3Pg-W-cEDw7fcDEqYwtiZqa2CDpGsQdV-OjwHsM_MXF-YzzW-nGnIoGvYosPDy6wYUnTIl7LlFvlLcRZ_9dkGUyuKhrf0sHpj9EvgoUZKo-X1lksMN8NIlXJ6npV6VJ2_Z66mq3VGYBp1v5GZXGxWG9p6OCci1PFFm8-ra6ng44PSPY10YRRkcXHgH4L1lVQYYy2bk2OHKwOne0ZGs8LGTGqnZRSsdjrbnJi7k0nMGkdKdOxPs6nq3sAwn4r6FLK8VDlyUOJC9Mvt1QNWFn26cFQ-AjdDKePEVlyBVg3ulfRMEMZEofzwVS4hoaQSedVLIieZo1h-XaczDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=qTO-yQZZN4ciUQJzgdyvWdW1BH49b96VfdY0422RcM6VATBoGwoZCSS8SfcopDQ7uYz8VVpIa0dtW3v9xCfZa_o0BWTtPcBmVb8Uj3LRRkdPqmmQjUDGTrlB2IavybWTbQ5kPRf9zFmCYB4aj24sF3kYOz54EOebvAJK6cCOYBPTi5ZUGndrGNWCG4ZECJBYNVwN_7-nsirc1ZaS3uHds8PaIzKvbl52csHbXS8SBDHBMuvdkBkDYefGWxoQ6Chxr48_1Qj9Evx8Ts2jmSTOvq88eOuOdU-qXoqAeWPHH_Vv9jY_GhgV0xEnqwmyBY1x99wxrMOxoSYVMOm8EvnbnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=qTO-yQZZN4ciUQJzgdyvWdW1BH49b96VfdY0422RcM6VATBoGwoZCSS8SfcopDQ7uYz8VVpIa0dtW3v9xCfZa_o0BWTtPcBmVb8Uj3LRRkdPqmmQjUDGTrlB2IavybWTbQ5kPRf9zFmCYB4aj24sF3kYOz54EOebvAJK6cCOYBPTi5ZUGndrGNWCG4ZECJBYNVwN_7-nsirc1ZaS3uHds8PaIzKvbl52csHbXS8SBDHBMuvdkBkDYefGWxoQ6Chxr48_1Qj9Evx8Ts2jmSTOvq88eOuOdU-qXoqAeWPHH_Vv9jY_GhgV0xEnqwmyBY1x99wxrMOxoSYVMOm8EvnbnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDlLIR3tlkn9XZwDKdkJIjrrnamWudlKE7KRi3uwK14IuTFQrla3NZCePNXwq9p5CE9AS7SwUM5MHtunOSXdmEF4nW4GP0I-x2uAqNfwEbriHfOu5yb5HwGwalooAkc97atZJ0oNtjx73yDcJLuVi3sDNW30VELD7RbUPkHjLxS6PS4HsGcbB7hdgjMu829QbeD4qYD_Ie3aVRhFshsYrP9XfcQrsM450X8UxYLJsgaeeLWj5kzQp2cCFoxrdI9Z0QWaaHjIJ0ny5CQyNuMXTvhFe4eRjUP1D8Ovdg-hpDprneYdtjjVxmof69RKEVJQ35ptA3dEvz0wZiSVN5VVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEZXsuoa2n-oozvtbuomtI8byOX3YiqPl9bTAR2L9maW4C3dLAcNeZ9qhMcuvrfrpyzRcpYlNPw7HXtbn3LQ1LUP9-Va6oSeJqfKPDbo_TPiHPIoKm5FNCtc8ZaaV-zcb229ZfkYcGn8393hBMMgpLsqsKxeNArEP0I3jFFQZkq75UqGGNIUA6MyQi13tx1assLbHNpLDF914iqGWPWfDg7i4w1OJhnsdWNM0x5G025Rl3jCmXNMaQ0oKBEBLe1Lnij2oAOmwfRmAqeUMf3_0VlIx-l_W0oaW5--_X4dB7sTuInSDRBfK-xzuZ4DHAjLJ61ECdnCS-2HsITA0eoRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=nVo2QPqeuBKNyjN5MIdSKNEJXoVZx9QMOS-AIZ_oH1BE3k0K_AFmM2ibYu7CYTE3ne8Q2GEPdVRB2SuD9qrX-Wh5NE8Sde9cvXKkmke12h_H705_G7WX-Hgif5sSIr5MCIm8joEDaQ5kldszudTHAqmEO_v0VROyQrjLMfwReEWxstwJ5wm8yTAKOC7T1j2wIYA6M-Z8BXqXz1jXCUf5NbLxz36ksOP7Lt9yI7z1qr5nNnDhbLoBu0oK4sVKZLEV5s04TBl6jU7STDoPcImBuZR1pO1TduF3k1WG_EYXf4m_0Qht1C1Z7VXlnmx-_cUBEg0O0D5gA-0USzDBaL-aiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=nVo2QPqeuBKNyjN5MIdSKNEJXoVZx9QMOS-AIZ_oH1BE3k0K_AFmM2ibYu7CYTE3ne8Q2GEPdVRB2SuD9qrX-Wh5NE8Sde9cvXKkmke12h_H705_G7WX-Hgif5sSIr5MCIm8joEDaQ5kldszudTHAqmEO_v0VROyQrjLMfwReEWxstwJ5wm8yTAKOC7T1j2wIYA6M-Z8BXqXz1jXCUf5NbLxz36ksOP7Lt9yI7z1qr5nNnDhbLoBu0oK4sVKZLEV5s04TBl6jU7STDoPcImBuZR1pO1TduF3k1WG_EYXf4m_0Qht1C1Z7VXlnmx-_cUBEg0O0D5gA-0USzDBaL-aiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=UKnwDj01xIqmd23-mUtzCvrs4uqx1YKd5NSDY1bw-wpXm1k8ItCHqK6O7VplZwsJaURgjRmSL89NjgExg9wjKfuQI10UjbEkXTlLqU_ao1G0b0ypUvVuZKCrCyBCVWFxR63hTtts-u-6mmr45Tvf2pZSv10B3WzBQZ1lgRJ6iRzR-rjBifbwjruJ1UivAcUIphHuBCJt3xSbg8vJtAiIRa4jXXaOcwvBj5WCPiQORMPP8RTFBlN-u_-q_8O77ttxWZAkBHmPVbBwEchFHC8YYV0NR8dS-QepFFm6QwAcpGQjVSnFss25VuguLe0QtESK77cL0PovaPWmlPwQ5WYYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=UKnwDj01xIqmd23-mUtzCvrs4uqx1YKd5NSDY1bw-wpXm1k8ItCHqK6O7VplZwsJaURgjRmSL89NjgExg9wjKfuQI10UjbEkXTlLqU_ao1G0b0ypUvVuZKCrCyBCVWFxR63hTtts-u-6mmr45Tvf2pZSv10B3WzBQZ1lgRJ6iRzR-rjBifbwjruJ1UivAcUIphHuBCJt3xSbg8vJtAiIRa4jXXaOcwvBj5WCPiQORMPP8RTFBlN-u_-q_8O77ttxWZAkBHmPVbBwEchFHC8YYV0NR8dS-QepFFm6QwAcpGQjVSnFss25VuguLe0QtESK77cL0PovaPWmlPwQ5WYYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=IuvcDlILvGLrxEoUfuG2WC_MG3Rr4CdaBbInrZgtMEde-hSjLxOwg4e0slU_9d0F1WJCxkMrPLoaqNHQo1ETfGgPdMatgT4X_QY9MNDoIUvOCDrQPeQJKq4SnNWPQMIvWnjrUYATREYM0u6b0VJc_4FBil37jGd8sGnncCJ1J1QR2yhhjwZTTxou0qcufZU1EmFVlMdPkJjIdP8qPf6FgmcJS7RijUfzApmZv764Q4u5r9A7JHea5VV6UGfipFQzBGtvp1q5b5hp9TpOmhIQXETuT9_jVYnAIADTEHPyQIRdOFEgT5bPUIV2l0AygiNqPcyc3cAswYD8ZkT33bDpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=IuvcDlILvGLrxEoUfuG2WC_MG3Rr4CdaBbInrZgtMEde-hSjLxOwg4e0slU_9d0F1WJCxkMrPLoaqNHQo1ETfGgPdMatgT4X_QY9MNDoIUvOCDrQPeQJKq4SnNWPQMIvWnjrUYATREYM0u6b0VJc_4FBil37jGd8sGnncCJ1J1QR2yhhjwZTTxou0qcufZU1EmFVlMdPkJjIdP8qPf6FgmcJS7RijUfzApmZv764Q4u5r9A7JHea5VV6UGfipFQzBGtvp1q5b5hp9TpOmhIQXETuT9_jVYnAIADTEHPyQIRdOFEgT5bPUIV2l0AygiNqPcyc3cAswYD8ZkT33bDpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip1iCj0HgFrxHXaXPjXyexv29L2WUtWgpACEw2_N2SJvbnptbKedaTPpqZcYj3eWnMNgbWMROt7lukNotHFZvMxFuhbqowsljMaA2tsq4U08t6aeOsITKp09n7S-c_Rg9sffQGxnIZoRmc9B1JtsVzGuqPH8tYPpdU1np3x6JePslXL0cGKvZP5uLCCB5Dy6VrYFvAdW7pajk4qliVh2H86GOcmOx4XzZu9tHc8SOgTXDAIdcQBfVzMeUJKWnLb0JskTesLqmrejrXq0DUJV2oPII5zJFFJZbQXcNsCk0q5783tR8UFzdWCu7Y8BlJF_XD1FjAQxocwJsX_ZCvalkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=DXjGaifiyXnxg2unl7AGmGXoCYAu8AejXDkHYRvSkoGXIo2BTNeLDBeaUiSjZjsCK1cItPehFU4TmtlovhJXT7L8yGdOMBCiVwbUug-AKaDJbuGyN9t_nsBorcRtbDsjFqz2YEZAF5zGrWA3HXjfo83p_ubL5bCUso4moHBqGpON5LKOy8Ejbw0ZgVpUSXUowXKyAkszGzXTlIG23q0LmJ-lOsYA2gGywLwfe7MPzQD7Xr0mONDnxlI3_aM7VUGaOpDrOXTqUrESvpsYRokM-NzwdYgMC9UUdsyJG9BUsFiv9Pe9Mldv5mWBCWea4Xr9lv7OimvCVjzDV3igHuPKdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=DXjGaifiyXnxg2unl7AGmGXoCYAu8AejXDkHYRvSkoGXIo2BTNeLDBeaUiSjZjsCK1cItPehFU4TmtlovhJXT7L8yGdOMBCiVwbUug-AKaDJbuGyN9t_nsBorcRtbDsjFqz2YEZAF5zGrWA3HXjfo83p_ubL5bCUso4moHBqGpON5LKOy8Ejbw0ZgVpUSXUowXKyAkszGzXTlIG23q0LmJ-lOsYA2gGywLwfe7MPzQD7Xr0mONDnxlI3_aM7VUGaOpDrOXTqUrESvpsYRokM-NzwdYgMC9UUdsyJG9BUsFiv9Pe9Mldv5mWBCWea4Xr9lv7OimvCVjzDV3igHuPKdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=BWnkVxCn5EVn8VNpcIFGi47RWa7ZuTMEUoQGWdecD9zESarCn-fpaVrXq3agyNYI3fcyJ_snCogjTQHAzPmvl2Os2zPb-gw6xdWjDgBdtSmSEgnvrZxlqqkldDgg8vDsZ2jutguy-s934gr35usA0wntNZ0C33NHVg1nMj19tTSGfjVNaSxbxrGGpCy7SJiZdN2-f8P4UdNddG7TKZeD6IU9wshUq1CIVwcgateya5I8MYq_cqEsPrakLIDCe8veEqZq8XmftfgWeQF-idhBTTHnqF9VOiMtc4-HoLOWzk0UdsM_QZJJehxuy1hBvAxjRH7tyOeLQ-8c7iTCHmvwaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=BWnkVxCn5EVn8VNpcIFGi47RWa7ZuTMEUoQGWdecD9zESarCn-fpaVrXq3agyNYI3fcyJ_snCogjTQHAzPmvl2Os2zPb-gw6xdWjDgBdtSmSEgnvrZxlqqkldDgg8vDsZ2jutguy-s934gr35usA0wntNZ0C33NHVg1nMj19tTSGfjVNaSxbxrGGpCy7SJiZdN2-f8P4UdNddG7TKZeD6IU9wshUq1CIVwcgateya5I8MYq_cqEsPrakLIDCe8veEqZq8XmftfgWeQF-idhBTTHnqF9VOiMtc4-HoLOWzk0UdsM_QZJJehxuy1hBvAxjRH7tyOeLQ-8c7iTCHmvwaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=kPsyCDYXQSxSSYMtl8fW3fnKtstc7QjHdocyDkYDCH7XJkYWX7Fhf4n3xxgYM0oI9CjP90q5xksb6xcaKClMGM-f92udn2NehFYSF2YpGcg8J_bhFbajzzv1DHBp5NpYtUDTVMrCbAqelCuP85TSj0-FCgg10srydYptu3gw_n84vrZoP6kRmDggC-_TaHF0LUX1_gu-T18WFVJZ9b4LjaT_6HF7si7bXQvR5pisZT_DGqTihzjHr59HfoaLp4Y200RcLF2FDAxr8YVqshvILi20rqg7ft4-QneSEyQknRMCbujE_OQaozVesOOD16m_RCgsVNN0NctIRREaOBxP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=kPsyCDYXQSxSSYMtl8fW3fnKtstc7QjHdocyDkYDCH7XJkYWX7Fhf4n3xxgYM0oI9CjP90q5xksb6xcaKClMGM-f92udn2NehFYSF2YpGcg8J_bhFbajzzv1DHBp5NpYtUDTVMrCbAqelCuP85TSj0-FCgg10srydYptu3gw_n84vrZoP6kRmDggC-_TaHF0LUX1_gu-T18WFVJZ9b4LjaT_6HF7si7bXQvR5pisZT_DGqTihzjHr59HfoaLp4Y200RcLF2FDAxr8YVqshvILi20rqg7ft4-QneSEyQknRMCbujE_OQaozVesOOD16m_RCgsVNN0NctIRREaOBxP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww4sYWct0X-JwMGhkLcy-GGwmXDEuU3nQ6_tJ_3UUR3EMkJs-qLFqbbgRn2EWUtyoMBBKu0EW82iyk9ebbavQA-xsBvtnuEHZLnq368JyDf0xhncMH3MlGq7SQvM6B75GbUA6ksWXLDsxymjgr5uDq46NsdSoCeQBi3TuIUaDrFyJuKY6wgH_JX9ZtBn1LcltP7HwzD9n6ETPcSEsyOHQrWIQHie9jppOGm56i4Bl983N0E34taSmhqPBmWKM7YzVkPYHWJ132KL94v40fglfnCrQnbE_BkX5cNkLmHf65AIw4_haNKhIo7moT1zxc01-UtHEilxuJ3ivzDVNl8opQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=MH3chfkn5lvH6vbhfNqAJ8Am50WkQ9bqv4iLqWfWlUZ-EN-OVuHx5C8tvKWNaULFgBwiGcBfD6X1C_9i7voVgDTwIM1A5eANnDp4qIaF5ZctSxXdxXxLQOCP_FFL9AFbJXA8pbCp4Bv3_mhHvzQdOd-ZaOtrKDM3FIILXxZD32jfXhNOXslJl3dbd1MkWfZ9GDwI7kEegxZ5JGlkHXMqKFFHqdd9DS52rWlPw4DnqgcpMf-ra2vc_rMcfvtYA9v7LGSgVb-D1emfxnH-2PUu4lQCcJ8lD_2DokRjDuty8vBx83cs5JyfOuVfU6JwwFrbxdv3TMJLmKfAGdQU_aRI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=MH3chfkn5lvH6vbhfNqAJ8Am50WkQ9bqv4iLqWfWlUZ-EN-OVuHx5C8tvKWNaULFgBwiGcBfD6X1C_9i7voVgDTwIM1A5eANnDp4qIaF5ZctSxXdxXxLQOCP_FFL9AFbJXA8pbCp4Bv3_mhHvzQdOd-ZaOtrKDM3FIILXxZD32jfXhNOXslJl3dbd1MkWfZ9GDwI7kEegxZ5JGlkHXMqKFFHqdd9DS52rWlPw4DnqgcpMf-ra2vc_rMcfvtYA9v7LGSgVb-D1emfxnH-2PUu4lQCcJ8lD_2DokRjDuty8vBx83cs5JyfOuVfU6JwwFrbxdv3TMJLmKfAGdQU_aRI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXogmA32qwYhgYXPwzJV7PRLB542v9Kx_rNYKf58RGct6_5cAeklbrWb4SZ3kMz_DkyqqvKR0D9BxT7e5i8AtgqImEpeQRwYMIZ5efGkLSg4TXu8f6gawbAE7oBjRJqRAzN6YM8lI3GBA-z-FO24QLoUjUtIstatnp16M9JGE-5-ulYOUPgnnOvUxMB7dHCzTagSQ6dSZc40x8SP5hpEIfa5qEhS6s5kD1mi5kx-cHTPMUgah8dqtx68exemWue3JPtpWXsd5Uh_fqQB8YwCRKDC7zkiCTWk750dS5Oov7wbWfuKKjhk7-XSLjFptS7fIVxt9L3utDA3u4Xeg1o2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=hn6tar0n5CVI81_VJLPv1WNwEcAx3FGl7NYhRt6C8_RiCLySdS1o4TvRoK8CVtKrw_wBRaDrx4a2pZRPfjw8g7U2jJ8b08UT7WWVZHhzWzlMgyQ4GLgKNvkQiP7iPRWHjiOTHYmw1D56AZcFflUt4Yj_x6Km6khiFbdQ_fdZCcr2E0_2bXSjAWwE_iWymAmgN8t6NSNJTwUVsBjnHczkhOgqPzf9-_BLcDRshmd6qJDZ8ilkUxvfV4sH09EbnXBHCOJ08VAAgLKEPC8QRRhfn8Tq6_cKCnW7GJfUVIE2FpFBAP8kNgdGZlKDwMtX-Rjyh6-Tczz4PH5KJUqW4hndPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=hn6tar0n5CVI81_VJLPv1WNwEcAx3FGl7NYhRt6C8_RiCLySdS1o4TvRoK8CVtKrw_wBRaDrx4a2pZRPfjw8g7U2jJ8b08UT7WWVZHhzWzlMgyQ4GLgKNvkQiP7iPRWHjiOTHYmw1D56AZcFflUt4Yj_x6Km6khiFbdQ_fdZCcr2E0_2bXSjAWwE_iWymAmgN8t6NSNJTwUVsBjnHczkhOgqPzf9-_BLcDRshmd6qJDZ8ilkUxvfV4sH09EbnXBHCOJ08VAAgLKEPC8QRRhfn8Tq6_cKCnW7GJfUVIE2FpFBAP8kNgdGZlKDwMtX-Rjyh6-Tczz4PH5KJUqW4hndPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7Kp4B4Npyj5Iarb9OAnSCtV7h2bvTlXVRsKNurrQf6EU_dUb9aj57VdIWLi56elrpEyn6MJutWxby-OBReN-FRpw3CScvL6afyJRp3uqH7Gc1JDhKYsitxNvc9aRtVKtQWo4mAnZYIvUZfzkl03_ojaWnOhJnlcWwxymQWmolinjwTf7u6B28ktkrEgmFPxuafOFQ_t1JsyDg7J63GGAFIILKPO8Cay9UYIAZLmeyEMFq7kWhmsBUE-6dv8LzyIxx2CVOISuOjDv1u6Tp-LWFNaOzM9GZyJYY2m7-otPB_eefmr8lSyF3F8JeeSTEK6IDwcHCbFqYruF1SVQ6Lvsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=UiOEtY04SJ9jwPvE9VUzdPfrjlpMGlTXhrrIrhDqJJmqGsvhQD9JD8QJT4W6bgqYeNgO-W73AKrcDxsFWMqtxSv3EjgGVQOkwCoh7HONDdvLhiIlYZOHikJ7WR2Fv79E2hNmePpOSH3yYT7TXF4eNtt-1gv6GBUIp6KbFCXRQVGC_rpOh3Jjvf4iuyfdD6czHN_VUz08AIB8ixql0wYCN_KepCKoJW4e6e3KboP06yxED06q49Efdx3rsAqKyEfHjM7-_rflME1ts-Bo89bpHgdOF112Vg_jaOLYK4xPgxrTNcY05afsL05G6r7aoUctOuk3opfhWdOJ66tQ0Ao_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=UiOEtY04SJ9jwPvE9VUzdPfrjlpMGlTXhrrIrhDqJJmqGsvhQD9JD8QJT4W6bgqYeNgO-W73AKrcDxsFWMqtxSv3EjgGVQOkwCoh7HONDdvLhiIlYZOHikJ7WR2Fv79E2hNmePpOSH3yYT7TXF4eNtt-1gv6GBUIp6KbFCXRQVGC_rpOh3Jjvf4iuyfdD6czHN_VUz08AIB8ixql0wYCN_KepCKoJW4e6e3KboP06yxED06q49Efdx3rsAqKyEfHjM7-_rflME1ts-Bo89bpHgdOF112Vg_jaOLYK4xPgxrTNcY05afsL05G6r7aoUctOuk3opfhWdOJ66tQ0Ao_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M37_Ko8kSlfkRdO52yXWVz_jKGagb_D7EVfPLl3aRW9oP9DqOER3S79UjEROvFnxTmZDo-PFjdFUSyr35aJJZURePbTzCRRhrEUDeQfOVlpsegHRDFZeVPrI2tDqDn5Z3nVG4_SCVdOlbq9RccCt3APJXO5S7CXJpPhDDtD-S-jXQhiEamha_BzFrKcijATKhl44dzuIvODJ8SGphWsNVSbhpvCZ-QL-caWAp9ntWu5rZFHcveW-JrNvBwwUzqVZb0F4KavosYg_f_fNngxgxfSHJAgBnRRX77Ggcy6eX1eBpiW-usDxbi2xeRbMfiNiHeGS3bQtiwyUHYondvSccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQU73RAP8tUJ0O1uyPf_QjbtWpPqiydBUdp51vq-2RJ2Qkt0I7NpGQ3uB1UkGEmt5lm3tXhKYCnfqYez69S6uqNVlOaw_Tr-aZjJw6DB0oUdAakyzj_rzZZKCjSSE2CVnJQa8CRyg2qftpPiwVIvLTRd7trQwPT43zw3X0ov3olELTeAlUex74cMgpQYPA1h84eqrgSxBxC9seKMGsh23QUWyAKAeEmSzSBQAb45h_TrO54SdelaJ_Le9_OXGohhdJWfqQrLjPM1ahYpzLTNGKEEOtaNIiwMBS61onzjAXb3qtkN4x37wj2siCmoVIDQudLI1jjbPc0cK-Dm1p0uXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
