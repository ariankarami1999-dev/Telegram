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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 17:53:23</div>
<hr>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ialgFhCO0J1ZtPdQAHYBKSWHdoSo9Y_1o00Gb6rLgLndnxo6YmBqWdM7edJXkjw_Jqpi4RLXT9tgR79wlSmstbS9VbeL2HzPUyU9s3_-5oB1gmr9UjGw44SsTlNnFdgoYrqEdyniXNauv9I4ewKVfFQN8AHZAZAHhwh-C8cAVLHsIM0BkiEYwN5IdrNeddfMu_tIklZH2nAkoPaSx94mSykTpIXZb29Sxrmdyigsrhqp8e6qfqCqR-GSQqHZYZJNtyF3x_3TJVAlCkdyQD8EInLZ8a5FbVGSwcrzikEXs95Efd2pJr4exc90-DetnjT1Citqnt46xpF6Io3zL_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuepA5yjmztdzmFOoF3_dVlgn96Gi3VtJ7T1DZFqXqNt-89jtLQUZOmbj52G7LLwJrkLhWn_POTFHG41MmIFho2p97-GJ6QUqFPrDVHnj6cAMjbqUC_FWYiwMbKpHqxnLQnjI_S-DJZVBddHLYnPvr2h26b2yExxyCZv1CA6UimpKdctlWtBmHZ6iYAsyArGOUjaLjEEkyTNsTW33t7pGYp0a5YVpnHFpHENkeEHbvv-q2HZcUGAlIo4wTTna6kVY5GQFwdC1bM5xbt03KAOFdN_HBigVgwKBs9B5gW8iSyc0wUWvaVMRAE-5RcZkPWN-w6prWOs_nUNvtJq5CfNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEEby9RpWb9e9hfRPwQ_Y8sLTZNcfX3penP1RwX7b7zTVmcE009f7c9opc82aRbdGh3hMV_tfTUzyQB-aufItTDWIyhfJXjLvlceOpQPYkvqgmWrq0NKvb3CFB-O2F9aUAEb2UklQDqNsHH8tB_Po0-a7tCxrLJaAiPXgDw5ie5qnJ9qX_a1L5im8u9HmbR4-TIy-NIdte0-IokBv_HZR0xFmW8g_rHETjjc5QgsE4hHkgvIzB8gX1MTqPjSlTqtuob2KyE71o3UZiy-ZKH35AuPtUgzcMEx_wtRd5IaKBCZjBPJfjPZnBXAAwgT6bKzNm178jfSk6fptFBnC2ePoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1jh0CX0ofoIdUnxvDoYs9IX0gzO3yoLoE8a8kBXySUKNn8_yjxHR2NiQtsw3GgKx_EtQQsJNpcMchTNZ4Km_jcxTctu0b6fs57l3Tc0BJYC4lkCgDAR-tdPGzifvA6ddaPEplL6KYA9irYTZithSlJuNTTChFrAePtue30uJx5eBpK215TrzVnBqL0wRuR9_Ekb9PdahhU0d538wYT7vgPSck3GbweMFS5gTHIwh6FM2rE75iw-EXAwXylemdBHRMR2-XDlQhTap6_x12uw8UNfssmSmnU6TUZBqKkdTqPQ6tvctIoV8yUo3U0vGjq5MTDhkrF2IihblteQpuZiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em-wE3jBYn1iiIttvLdQtTxbWHV8e9eny4dWWvPRvL30Xof4-IrGCBw3kzCpkHikX26DGCXvhtt4zOZqL9_w159teAMbb2lAa-mmwN8Ogb3Q4swdx7UiyqZV7rMZDz4dwG1GZ27NgL-LSFB8pcMuiv5RQsCXSJGYW2GXLU1y_Eicm78XeP9r6iEq9jNxs8GMlOUTtqWJ118TH-OcUhfNImjtxRNdtPEoBfM-OAX2gaRFDRVYy5jmSyFnK_Nq_mruq-NcsyAkfhNVUDG0YkoF4Rmpj040nkiMhYSux4hfSvVRInskzpIQDvbNXcCAo7m-jEZ3gliiBB-Cg9-jn5Z6Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL0FqVSA1HCSu1RylqX0Dh3SnM3mHe8pSori-1it913Ku9B0VTO03OGOhB50_-VTtmV9cLsjaiMdpvdfMteokcDGG60d8RkC_jaRsGn_AqlyIPYsMxG7Smg55Gb7rFJHQnxYA_xeREObUGOD3feGJ4iNlIdVLueZk26lEA96Gc-Lih2XNOJ371j0D1D0UKpt09RQNqo46eF0-vAKyTjP0-m0OaMxfAxC2Y403AmdrdkWHqFqFzLztGLuIYOTRqCLY1CMHnRnS1GTB038KaBo_MCF5UlyrKLW3bNY_o2qdX2eGIH7xtBh_EpKMKGf435P3Uvgyze4GJMzGjcR7PMVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=K4F4-4YnfdQPEZ8IhfINsyx02nGinU9JFvS0PU5hICK7c3QlWHjHmrgh4NRZTiDsglv2cjQerCVsUmcqUPPjvtQ5W492dR0nZE7G0wV02EgMLEf2GiP6c-WGcvzDAEV6WgMmwAOG51WHaQvawQjNXN1488mIbAYckDQ6dI6ORkzPPhG0fDF32w2kkOvWOmyWLP57yAQ0lrWEovfo9dl0e5lNNRfgGA_m47XDkVShGFc5OB6LRViTDeZtuEEUINN-o7ug1xwqpin8yZx-mKaowVyM0InA2Stpt5YIH2cIRJQ683jOxrqQCHGe-UcGPuJJ0FQgj_yk0YZNRvivfv5nvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=K4F4-4YnfdQPEZ8IhfINsyx02nGinU9JFvS0PU5hICK7c3QlWHjHmrgh4NRZTiDsglv2cjQerCVsUmcqUPPjvtQ5W492dR0nZE7G0wV02EgMLEf2GiP6c-WGcvzDAEV6WgMmwAOG51WHaQvawQjNXN1488mIbAYckDQ6dI6ORkzPPhG0fDF32w2kkOvWOmyWLP57yAQ0lrWEovfo9dl0e5lNNRfgGA_m47XDkVShGFc5OB6LRViTDeZtuEEUINN-o7ug1xwqpin8yZx-mKaowVyM0InA2Stpt5YIH2cIRJQ683jOxrqQCHGe-UcGPuJJ0FQgj_yk0YZNRvivfv5nvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_yAA2-4SMSrgYOAKuH1WqUEn0MocDX1EQcCCkrWwUZdOUtmOEE5aP0Wzj7qcd2-1PVeMxr7An1MbeQ-ekuvwBVH_n1hON75xMeNXXf4JkhLMrqbNcqyD3PQWxLp2tXmtxCFtT7P8b0oo5qjoF9abzOYnTri47ldxF3NSbo4pjeFNNcbAFuH_rZgUokExKgAjsCOU11S5I-0AgxT6-WfGsZT-OvGLKCncT0mxLS8TaB0EHeRGWx3jYh8fQSTcCLh5IAEkQHPCCWyvwVwd2EGT9vzYxhQ3Mfqh3rsGTkTMKyiiaHiD6xHxkWI-9-Wv4N_NqHHGXZEAz5tQt86Kib-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4sSMadJqvHii4URxoVPiibcGImMY20TLhPdYGJpo6gmzts5PwOgiF473kiW1f79Ku9lXmNNzvDHFF6vVkgDuLwtvA4cZdxpxReN4mOkg7Y2I7cCAcJ-VA-5IrJqwuYvjOgLEEzyIkO53FHM2bhyB8ln-vdOo1GeU_-VHC9IO0esIkuLOunCt58JsSEJLMKLz1ZuHRewxIlcc97Jz2HGJ7e3QQ3c5U9hjoo0CLobVHCRi01EkS1640sbZ5Z9MdZu3C-oB3d-0J7gvnhoSWoqJNPzrcqc6s5DHH7ulBjAEJ_vvn1xO2iMdf3zxzFS7jXNR3iAd8FSAOncanIG8ajOnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwpPWS0p2I7FqIF6faVz2JpdV_IsITI6p0mg5Im81PkEqzB49YhqDZQsUnORRPh0OGId84wOv_iReFcanEZUHIDLs4RiDF2wE8wBXowj0QLL9_cSOCIiOz8NfoI0Jcx-erODRYPdVtfvgbtWk8ygSS_Fh4mxZr1wPPrDVzCDQgzSsDWS-k0nC9l2WbR-SzBVHs0ZYR30ZsDG4m-4VN4AAXFdG0KprW6-7w_KF3jaScvvd95XmKDuyL9yXxg5ZkuJ8Ch4YCNtr_jiaC0HW0tJJ79kygw9LK5nTXMcrXuqVy1TizS27UZjFuEkzVblsAWIymvyW1CX9-3LTXEzoSqLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfBVYiIVxffIQ-i2slg7ChPPbIFLCrqSTBEAgOozvT8emDtkPPi19SK2YFac_SUxcFhnp90vWOGasZG9Wn3wFeqYynlMWPd3ovqpK9UqRgNfWsazbm6zow6X96J2Q3IqwvDZPE8uj2UHDVZGdHgYMPcliSlP0m7pwbVF3_wtWjJEmc8Zo4S2o7CqSpXiyeU3aDYvBtwBkAo6ljEhd2RR8GCa0XV1vdFIOSkuE5678iPgv06M7FwsktfD7SH2CEcEwNwBKTBDzRam2djOlrPj_CpJw3M_ScJlkatOjrU0vLHKWT2fw3PBPuGxltaLeQUqxeIYJBI-HABSPE-bvkYeeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ_M36E4KIZ7h7fY59MDpzmr5-_zsf2uFje_hu99dV9seE8SpAbLWZTsBhU4r5MzBy5ed89pVohb674j5iGBcoPRu9Kx3UxLNBGNP_WmhADUAjOwIf1TEhz88NlmT9cgGsamdiVTGWBhCmgYP8SpMdf0DdLqYOCt3znY6mGL-AjyGPkiwbZa7sA_-OsOKItjfHd13QrrSQrpQpw2cm-7PqjpLAOGjRRhvqol11HE2x_OsCUdiQV-8XHjkvLfjV3jM6qxYrC9IRkRx1EQq7CskvmOlFRwJ7Y3cTb9axquNsP716quGySZ5SGRs-mRrnNxC7e2VNHNXiVq0JuEscBAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Zhaez7pWcpzgkQXCLeG1pMeoff6hM7Zka7dnLC_4xDlGesth5HX8DacA3CJt65RcMQSsu6sNVr1hItdRW9mQInbYLlG2efI7CjJxSRXLLEVyA0SD6B2yhDDFqs5P3mBc0Jm3OGjd87gpJiRDFFdTRtYstWtGb0mWSYyeQ8h21RPpMuBKmml7kMdfiEtEYRDIrRw8hBe62ZuyV13BrDIKsjIOq52xPM0BYs8VhmcZmwxobh2mPQyb6C9Y-QLupBWAxwyLAVTk8V6cB5jZM9h2pWmODekIpNjqjYy0n_h_dWnqu0t0JqGlPSoyl6IDHyNQ3aF7z1vXxmh9en06sB6qRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Zhaez7pWcpzgkQXCLeG1pMeoff6hM7Zka7dnLC_4xDlGesth5HX8DacA3CJt65RcMQSsu6sNVr1hItdRW9mQInbYLlG2efI7CjJxSRXLLEVyA0SD6B2yhDDFqs5P3mBc0Jm3OGjd87gpJiRDFFdTRtYstWtGb0mWSYyeQ8h21RPpMuBKmml7kMdfiEtEYRDIrRw8hBe62ZuyV13BrDIKsjIOq52xPM0BYs8VhmcZmwxobh2mPQyb6C9Y-QLupBWAxwyLAVTk8V6cB5jZM9h2pWmODekIpNjqjYy0n_h_dWnqu0t0JqGlPSoyl6IDHyNQ3aF7z1vXxmh9en06sB6qRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7ZcaYbtEr-qC6hpPVyHiyiKhmH99GUuUYTkkdXECCxTnDHNUQSGbun9N5r120WJSeKG1Jayqw6JmYm1-byWKwvpgFuJC-3yjyj9jFf_YKH22HfhedN2Nmd1tX8rUtlGFYrkklzTZz2qe13SzCLJnJPXV_WzuqwXeILIL8f-AaEG2vHWdVkUFdW_upRQ1E8GQOSqouTLzYX2UKf5t2ynqnM6MNKhVJX5mND63VG9Tpfm2kznTRC7iNWzEqt3naHM0puvd6RjSpZEgYDXibE0mr3SZK_9ApFEsYvbIOHApprHOU51bEFnDjOI2V2fjfGPTlELCToE4VzOZcJlWTQR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErsEAkRNa_BQbhffu32lmUlJcNiMrziMMmhe9LllsBW0t2Y9vbNpAQJB0zwb_y1Xxtaguu0zuKTpcVDMUyZ_V0OJiW0R9x6DZWi8CAKGIEkAfhno5D6gtbWV_s40_vxQ9b87-8kQLpmz0HWlASyRdHm_N27wQTiH9wQjKOmFE_tX6DD0xyS4YYWj0BE8epu1TV6KEPtyfKqrI04QQnHtpI3oz04gq_q65gaMO9fkX0fUrc50mfZLUNasUfnUOJWwEOxc_Ejq7LmOO5ZsWeZ7_yTnVJWJYMannmz6ULasaQEeAETqoRjSAQzTSoJxu7VS5ax5TgR1W8XH4m97wV8SYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3Gf4vqU1D6Gx7cQn993DggUbK9Me1PKZuNOcGWNT7Pe5rNTGKfA53NtWsEgsj1_I8MASwILLs2m4bY8vB5t_cIZ3HZzE4hwNOf2PGzVuY-nBvWSFX0UArOw5BBduzBD25cvpwrI5_DnBs8JkzSIqiIhhaoHjTHAzeVlb4kyDPXk7VUZ0uy3PKBXZ0uDJNnQ-Gp9FnbyeGYBq270PoEoAUzNc2ZKZxVfmIH4DLEsDJEGFyw0gO0rGlJZPFRiCVnT0lQVg79UD5eoAL3wB-be77hKcDSQxjMffe4DhRczk1JJyP-pghDTipmA3bGYq-9_6oaNn-Mzq5nT3L7FV6vuIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Lh5QNc9TKJa9LlZhhTWN19eY0eKBXFaod94XNUlBAPDetx9l8RvzCkztjkjfPl9sPwlpn8JdJiKOm0U2821zxV3ubUSFx6u8u7CEssqSn_Ukj_TCJ4Rz4KSNf3VpiaQN1i-zgBZfWAXcwTKImKpp6TmofpqJUphxMlzWU4MhuYRlPEK4jBHLc2DzW1B-BhoRgFv2Y7Pbolog4TLsvpplb1veKAtquQTqddnVP-geQiTYB1uFWKoOa0BYeeXUeGE0zBhsAOH0fLBEl4zc4Y_mvrrWjvmI3c5U6lowrU4TDKD31yfovbXqM503eUpiT0zSGIj-XlAuefe-8qFQ1y-5Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Lh5QNc9TKJa9LlZhhTWN19eY0eKBXFaod94XNUlBAPDetx9l8RvzCkztjkjfPl9sPwlpn8JdJiKOm0U2821zxV3ubUSFx6u8u7CEssqSn_Ukj_TCJ4Rz4KSNf3VpiaQN1i-zgBZfWAXcwTKImKpp6TmofpqJUphxMlzWU4MhuYRlPEK4jBHLc2DzW1B-BhoRgFv2Y7Pbolog4TLsvpplb1veKAtquQTqddnVP-geQiTYB1uFWKoOa0BYeeXUeGE0zBhsAOH0fLBEl4zc4Y_mvrrWjvmI3c5U6lowrU4TDKD31yfovbXqM503eUpiT0zSGIj-XlAuefe-8qFQ1y-5Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=r4nVfBIL_bICVMp6ASeKoKn9Lz2k6rAe1kw4_fPEQ9x6l4nNxJzf6ZCbGOZXRGuhUKyNhJScWO6xjO-P9rwwHNLuZF_3ox7HBCuMeuWtDwGIlg7h1ergGi2JQx_tRMgl20F9HX-E-HzxCMx78j9eh2uhnqh9IGDfv3MbM4jhZsGDdD6H29ETdOMIU3lCL5DnPdplTr3QhV6y_HHHL_4jOwoeK4toOaGzmx8ta59f369l5DFgeFzd7MlMOY1ha3guljKHRKuID5kK6mI7MRvzvyeheYBDCY3lGEcA78DokcOXse5S0p7DyO8l7JFRnXNBJtcK7U-v0WBjgQxSUdAJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=r4nVfBIL_bICVMp6ASeKoKn9Lz2k6rAe1kw4_fPEQ9x6l4nNxJzf6ZCbGOZXRGuhUKyNhJScWO6xjO-P9rwwHNLuZF_3ox7HBCuMeuWtDwGIlg7h1ergGi2JQx_tRMgl20F9HX-E-HzxCMx78j9eh2uhnqh9IGDfv3MbM4jhZsGDdD6H29ETdOMIU3lCL5DnPdplTr3QhV6y_HHHL_4jOwoeK4toOaGzmx8ta59f369l5DFgeFzd7MlMOY1ha3guljKHRKuID5kK6mI7MRvzvyeheYBDCY3lGEcA78DokcOXse5S0p7DyO8l7JFRnXNBJtcK7U-v0WBjgQxSUdAJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=cPBcgCuRpBN_HM2TbX4-dXd0bSZNE_8IMu40UwCp4H-fMM3H9byT0vef1yPh_IHZcgq_nYuVzGfcTHKE67HLwikVN6oF5nHY0KlC6tehs9LqsQCCud2yWoZIuplfJZiE6jTzWOlMNEhqeLzwHhorx71LS8MY5Ryc8jL1LIvbYSFOSRhKqo3GHYxN1BUZoBVShCJrPhAanjDWiSCIdh9CnhRrU4y72aigakQIKQ6ckGa7lWOpnA7dib9RdgWttJoAwXOvHtRu-83r0gF2JvXNjtB3JjFbebbG_qxREJclGzowTsAw_kFm5iT3MKLqnbu3iWmLFjmWPHvfYExtVNhEIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=cPBcgCuRpBN_HM2TbX4-dXd0bSZNE_8IMu40UwCp4H-fMM3H9byT0vef1yPh_IHZcgq_nYuVzGfcTHKE67HLwikVN6oF5nHY0KlC6tehs9LqsQCCud2yWoZIuplfJZiE6jTzWOlMNEhqeLzwHhorx71LS8MY5Ryc8jL1LIvbYSFOSRhKqo3GHYxN1BUZoBVShCJrPhAanjDWiSCIdh9CnhRrU4y72aigakQIKQ6ckGa7lWOpnA7dib9RdgWttJoAwXOvHtRu-83r0gF2JvXNjtB3JjFbebbG_qxREJclGzowTsAw_kFm5iT3MKLqnbu3iWmLFjmWPHvfYExtVNhEIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAr9SBVPPKCfl0jagNcsppSKNpx9pCxyHwNUqPOo35QdD1W5ujrNRx1S9gYeuj04n_RhetE-W9xUeEzS6M0UeGO5OQdA75NHfMsh5V5DfB433XE_Dvc6btTN0daWXRjmWIN0j-Td2iTo8gTPZIbO-WclExITQHVALvOxtuAoQu24aaqoiAJai3aCug91krMNVHYYFAxr1z262jNAXTeoqEdTdceic8iZ6jF0ITEZUaS8jr9SApOE0HZW8KCEuxvIhglOiKKSMh-08kda8CDkRaH6ZPfu0Jd-J6nEwtlpdv2Er4lCLkMWA8i4xszxbUHFrdvAmmYx2WA7PMcSjas7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9MzoGmRuaLNab-fR-OF7GtqxDdSvP90vTUFvgfFUJhilD2fxc7MilP3QQaM79f2qjlpDN1UwvHL07h18-eQb7ThUc0AeTEdClEMVNjPHXtMp5-KdwDOKXejNeucob_vt-7lFDdPHuY452LE8kBRdv4Yu9fl0w7mCIyUkqsakjPWZqkNln5xld1d25tsVw9Q8hDQiGUjMdfaMJzON6ZpIfmBZI5o58KYpOEHHLZRrmmZnfEClbARFgHE2fG5P4Yrt7V7uq9WfKyHC2FJWhfS7YPVHo-NY39skGID5ksBzPdG5UtS71kQiUxqU8rqRBHrnH56cdnSOsrG-zi6lWl9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGr3VVDAhn1FOIEVfC3bmycVEHGkB8KgbMe3UnUsnztAxqUxSGR2XW5NG7Ns8VGXRDCbgUT1J4quh4VIVWYdM1UXv0HyxdgVKVEkoNybiYZkdCTd2IlYuR2dizX7Ptvo5eRaGdCh4FlODZ6Qjud3LTxm4_ABA4mLmbD0W_pLcKBawhdhTU_bfI73gx0uEbZOs7-ntkEefGSFhNz1QxV9wsOI8uAzRI9p63jd64klGdpBkscVX5qoeoTG-plvohAG9Fli2GUO90ppKENInQFY3bBh4GIbQ5VDW9lDlVZ5nF6NVDcBsjOgchUgaGZeWnjmXJNVcwLPt6NVjF96a_JESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHvmPGTNcRJdSIB6CZFk5l4Fd4jVqzS4JoJaa4-Jx8GjfSwyX78mSH_goBNhvz_akwwVxTOf2cUHOXvgB7NyL0VjhjqByD8JJr_nSASy4_V-6BbxnDuksxDqV5Kl962I8vTlhuAEs12EMJYY2HRQ4mKNdaODCvQD3fwdmx0Oz7MpNyzgnr3hyDCwbGaMKEj-K9Uyc-VPRVLc9s6OAzuALsXQ9My1cfcHt8iszmTejYrI9jRMdaZQwNCn-l-3dcpMRaeE5D63m_MYm4YNEteSAsZC_9uX12kkm3PIydOxRHxtwOJHkJdy0Nb4HAt1YYilZzqUhrdXfsmxDMTTLGYbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-6woNyoN-U3PSmnXReYNEdfM8otl29sUWaw8LzDRQbvMekp4eNx6qNkaMkTV_V3uc-JlyB30FWDSShF4L0ssCmVPXhtlakMZNthSlaysTV4k9g5LyKTSYRhd8WbVlMFkVkjeh3eGGpR-YQXXDWbVrxr9iswQWRPNUo8lYzCZ0SXMtFFHBMFo5lB_X7OO3PcCyvK_Emjzd88ugElh-Xgxvo9MfNQ7u55Rg0UzeiJoHi05Yjz9q4s7Ss_e8KtvTwX2dnCgm0BN_Hmnsm_phClPVqq3l4_kBA2eUfnz-TAkVgedHOh2TN93Z1uxIDJH-tMd84bUXMsHULFlzmJRMArdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkiaDNfPrt5LBVsmkBNzRqbj8g0vhmEr18rv6WyXyR0RQhwNr-tw4pE4cLtvNmvHC_AnVfGoBfKxnJRRqkoualANhqlz1Qtzd6axE3NX2l8XhJEdOT7nhuslBrs4s-SSnIQWg6CmBhFhIim1V38gRsmYbI5Ec8FJ6xjxr3NVyYhlgLXgazo7jWFU0diiQudk2r2ADQ5lqkbCRMjEYMEmOI3eXWnufDVsxD_CBIOelvjtHuW-Skt7NtcisDCe03sLYQWqM4olkNUoMU_pF7O2JHulMYK81D6IjK0WNhnltGGr1JLo4EdOq-aPh0zEwQ_UlNAzYE0eA3J_47iPrK8lhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVX9wAhMKF9T1QCR2pMJandrKjBvrJjqgaaFNqTEYscCZE9Wn2bKI8zID3XSVa5V6mvlwzY4AgremniugIgImMSkS-97MmAalNZO_meZXnzDOuYc6Y8_1GUP6cYjmbWZlUfHUlFtLEgEVeyj2ats1jXQ0O0-n467h9WbTBB6s2ZY-HIukQ0CZLnLbMWmuViRWfuBMd_Wn4AaGA9wlx2QUtFytPNfFoGbsCU4eSjS3zv3nsQLygnMaMcKdYTsAM9fvADTI-XPOFFfBj4zfI2_2uOdyXA7wZQ0YF5O7eWIhX1nXUGM_mRp-MjCR_pAfX8wU6tCbdZl9r8hM8RnlDrGSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcEmFDdQf-YfAelJhBkZAFa9Q_dZwdzxINlZvzxQOoxO1iXZ4BpnkFzv1ksbJmARSzQSfgYub8I0yavcUtj9DSUA8bJJcarcwP1c2xw-whRV1eWRcvqfH7yE-AemUpRTgbQXFEyNLE4ZeDLWkuG26aNy9h90I1OVe4qcdt4fEirU660uiXAYED2CtFYy846Fq5LG46iHZLpFhIl8Sb-dxaIw5rS86uBQQoSahgMy59U_vMQ1ZpeikaGalAlEjgRiynei3IeuhMe7cESDkTcoDnQgMo8ucbvYKRiVMoWuTf20ZoZe_-VcsRcywJ6gynbC3BLgyZoXfMMTY7M2nZn3hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN3CjY6nxFeIs8KXewlDkwKSS3LHioxF3BkKOfsjj5O0JOSeTSMLxJl6TX6A2ocfsa5YKvnleQuu7SxhhdrMgEU1nDnN0P3kvV69phTWuufsEI-rMSCPVHi6RAwGKIjc2OfyLAApODdNZMjfWurE7K2_jB2hqW36nX9_hpX6WqV6u49IEzrkeEQ8Eg9j0LmdQKQBNR2EUErilPokSwgpfVkfJs3aag3HAqmqhjXcjn4KoEYXY2jKAMGuMfGxRXoDdd4rN6a_V22VRgEsw21GE-USH1mn_4-qNKty-oFONV8mqRZ0Y16Xkzh55i0VCeAzeY2gkFWZStF5Nw4a_Y_m_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo5fgtO1ZE7brX_UotAPmLMgLOXtSwaZA0VSKQHDHKs5KJGPo4LMkPKfkg4h1eOUR9JboY-L8kmXo3_32JCW5JnWQBUL1XhWcMOsSl7bL2w8qhB-0rOYOcspXj74ceSTFjjrjsRhnx6te0QI_qY_PZw6xj8YGUwo-BLADA5dAOhW9za5W9HrfcYVADFDIBY7_34XOBfNSG01o-BANB34l59Wle1JdPGoWVgogzshrCPEr7a5KV5sO0SB2F1UY4iyzWqxlexE5eCLpm00b-A_v_4o1bEYslUhyAX14S5IF4MxSCscnxOzEXc_G4SbDHTPU3E7U6hf5orQY0F_C-mMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d73dKBx3wO_GWNP7Ic1bjzpbXaryDKoC5-sJLgbXT4FuE8NH24r2OwxkdJYXEUnVqMwHcbBoeVQ91mfQKxiSTSlWY2M0b-SuXkbYGUlfmfOpEyAif6oAoHV71NvksM7AfF4KbmzeyTzFmT7rKcmeNsKZL18Kxl18KXiDnRdeby40EnP6eKmyhgQPZfqpis37rY_UQXcjtzU7mnsH9lDXClhpgZsfQ-dAWHJXbiv_v_OrBF2w521lmyfQ7HM5MjUUAzIeAEu1N0_zmXD0Bc00FRNKvbgBnZrytpN-nAnHwEwIIRjVrnSNmiSNKGP46qEUfvzinxH2--lHq8v_s-N2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ1BiV8oMGsJkTJLegu3R3lbP2VEXmOO1u1bHmRAtztaw6MfFUtLnwhrUNi08CsEQMkF2dkcrJjbxEcYP6U8LcyxQfBhj1kpo1zJ77FUeYmVhex8vaQllaL4-km9mO7oIgUhr-0iZYLnpGWKCVjBM5fpio1ZgwkJR22exBlKrgdHT78e3cJ9ayfNKA9OHfqFoxUblDPTharIUKk7p9_IIovFxqesxeHAYbUHcF5px4yiBxSB0raU1jwTfXVzQKxflznLAHX3loP7M6Z__WTEdNI8vq2iR1-hXaFA_QPNWovz8QWjUZj_-foK2R8VVu5oBx5XTcBh4ckuVMHBAn8oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8qFoBU2lCdMWxZedI6gLkYKRW3Nab00FvK4JXk8Us5HqgJWliRhzhgT8tgfPiPiqzhoVRTWKeNWAEA_ik6HVMSKxijbuU0n59yrZ2LsypyqSVmcmqkhwf45KNxJ2ccdrFJ0CGJ1UINNbNerpBmBNCSrz06j8TK518ZxcDo6f3LG7iV84l0K7RV7gMhq3IkMm0UjOxd0qs5JgdQIyMHztoSm6gpKDENyYLbLCQrJ-3C38Ah-2_ywZaWaMkkTzSVZUczXqEtSn3PY8qAclUBfAXbw7dyU14MdWoUB16uDo0VESCIPpJERhQYbv1cfF_90c-zNuI7skzWNxPeZUgjJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCzYSE4my1AYtS5PjaKCG-opqj5nhwvBoZhB8rPN9Wr8llWwjYtJU2j4JGZeWU8kM8h7-JCK7wfMArv-aWHFNumRs6kzOUIXYAbZm_CafGB-mrlQ5O4t6xTOHGTBjGb4atdgmeg49NUIXRIXjWb-sgGwS7IHgmdlVPokPIKj1FVAchEVafYolm-V-BVltfaozj4jXHqhl2r_2Ykanqpts3PxkiBVgOG6ErsvZ52QAZntnW3IRY_UJ4tuoZDTaxlzbc6rzRlfycy0fCENx-5HhUnP1I7ssZwscTLDhFyrIHN-0TYgdHXuZtfk0H0CH74CtNgXdsifJkFMDXFgEFNSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzfbbjQrjxV7NpbaHW5bGxrJEvbJyD2MH53FTO1XwnsfjNtUbs6vOraWTCX3i0LZIsuzYEHZH9F2FhQjs2rX0r7yF3Vp5dXV2azQv64E5JpNzBfgyQOxCpOJxr1gkhF8g0-T5Y4cgO5HgvBawpnox9jGGKET5haNf06VPw21mYygnRMd0rN83KrYxpcK7ELFQb3mf2TXhk4EFMQ7kjvyBd1Qyjf5DQnbPHJvXdaozwW-X47grkh8dhBeDpUt_f2xa4tminmUiwiLLdEVL2cJyPT0EZGHBF9Ule-QZmc8abL9i5x6OdZOLEczp7X_paGW_RckI11zYnN5sqYLN_6tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=e2_oFb7YA122weRMJ47lMvfktvtgp6zbZQjrEWm_bFx43_cY_wm1zyGaUOVDoFk5V7P37k2N-ZVR0HLyBbf-Lc6yButEZ1ty1mWIbQUr2cOQO8ajCqCX6zhOndNMP5oSdSRo3ml8PPlkMnOnxytdDZgC7_6wV855duRLR7nvItEN8Lv7PXt2OmPLWS1Dwa9-U8jv6KDFSxQ23wMitLSG8zH9F3Sj-86NALjzax32TrDEe_LkiDDyJq0ZfTOQJB9mDUsML1eeCedxiHHcxLjT4qLPB3nhVBXOzPMCl4VZv5OMhg75-I_jZDe9t-y1GxBTjkZzZTBKMafsjw49KCA5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=e2_oFb7YA122weRMJ47lMvfktvtgp6zbZQjrEWm_bFx43_cY_wm1zyGaUOVDoFk5V7P37k2N-ZVR0HLyBbf-Lc6yButEZ1ty1mWIbQUr2cOQO8ajCqCX6zhOndNMP5oSdSRo3ml8PPlkMnOnxytdDZgC7_6wV855duRLR7nvItEN8Lv7PXt2OmPLWS1Dwa9-U8jv6KDFSxQ23wMitLSG8zH9F3Sj-86NALjzax32TrDEe_LkiDDyJq0ZfTOQJB9mDUsML1eeCedxiHHcxLjT4qLPB3nhVBXOzPMCl4VZv5OMhg75-I_jZDe9t-y1GxBTjkZzZTBKMafsjw49KCA5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLj6eKXRGRO2jbunEfSFfInMLt_-6kTHphV-8Y9HxMGZojr0ZOyhBnupz8xzxfx0e6-wdjxpwAaytKPyh3gPhe9OAGET-ieDRt7YdpLupC0QaKAj6xH7oZ6Xtk1ik0NKl69WxIndArHtEXLrNiTkH-GP-xuQYw5fQZxGmzCamhIAClHs4JKW7Mb1Og_H3zseZoQdmyQENvqhNiGRZ8VrXmjPP11EK7bn--WhwqVj-vfH-aGAamSHzVTuYHZ6sgFuRaTXQA359VFP6PeVAMdys1VWFKIS0aCN2whYdERhndIrXx7pbQjsuEyC63Rchhl8HqHLEzMornuOrU62oxZYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=NqVP4VD3Cp_gDedf4GyueK_NiwhUHZcKDrCIGpJIYMi9nUGB1txh2JU2SZZacR8GNr19w0ffpTTog6YIgLH8VEijKYjLl9MCp2vDIXDFFF0R2ZlZ4lmjcLF5wIUZCNQU0FY5qRaI3fcCJnZ0tStNUWaMc4V5dTclV5SvQAs8RiJGY8rqV4tRzWGALBTPn5GgeKoaUjIJW5Mx9yPIviOglkbV0tnonL8Mibe9g53W9ANljOBTxUlLSWwU7PjL3H6vDFJKboU4BTKzSKFNF0pG7hV3mz8to7oDB8H_50rAJSrWF2lRhM7_PuXqSY6PoJUR5p6Tn2zb55tNCOlEbD6WAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=NqVP4VD3Cp_gDedf4GyueK_NiwhUHZcKDrCIGpJIYMi9nUGB1txh2JU2SZZacR8GNr19w0ffpTTog6YIgLH8VEijKYjLl9MCp2vDIXDFFF0R2ZlZ4lmjcLF5wIUZCNQU0FY5qRaI3fcCJnZ0tStNUWaMc4V5dTclV5SvQAs8RiJGY8rqV4tRzWGALBTPn5GgeKoaUjIJW5Mx9yPIviOglkbV0tnonL8Mibe9g53W9ANljOBTxUlLSWwU7PjL3H6vDFJKboU4BTKzSKFNF0pG7hV3mz8to7oDB8H_50rAJSrWF2lRhM7_PuXqSY6PoJUR5p6Tn2zb55tNCOlEbD6WAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=qC4F99Uv5gPTbP5-ukrqUT44wFgxcXRyc0ccjnmKh-48YG1qLj78YXH-iVPJRHT-xu9Kq_FICSWj1jf2ezeNIp1IvKKZlZJQ4-Ylm36NzRCl10RDe6Sn5NXTlfMwnLQyrmcR4bZPxGLpbZFq5X2n0lSF1AyLJ4MSXH95CAbwPZUS9q4LWC7Lm2A-wNUPWv-TFIb_yKk3f8glcUPEjoHrNFGnt8p9OVDKKlVMXhxnVCLY3qtZQSKvpyctJkqMHnvcxNURSQO7Nv-hwUi1Wf65bB2MgXbwjp895KSJROIQHaxnDi4IBK0nZrzuocH4pQj2P28VXKd_S9wk1xp7fiGz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=qC4F99Uv5gPTbP5-ukrqUT44wFgxcXRyc0ccjnmKh-48YG1qLj78YXH-iVPJRHT-xu9Kq_FICSWj1jf2ezeNIp1IvKKZlZJQ4-Ylm36NzRCl10RDe6Sn5NXTlfMwnLQyrmcR4bZPxGLpbZFq5X2n0lSF1AyLJ4MSXH95CAbwPZUS9q4LWC7Lm2A-wNUPWv-TFIb_yKk3f8glcUPEjoHrNFGnt8p9OVDKKlVMXhxnVCLY3qtZQSKvpyctJkqMHnvcxNURSQO7Nv-hwUi1Wf65bB2MgXbwjp895KSJROIQHaxnDi4IBK0nZrzuocH4pQj2P28VXKd_S9wk1xp7fiGz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4xKoklNwazrPfwxSBc7ZA-MVkAdTpwdyY3y7ZT7LH27dSZ6ScK-lH-fEznNz4NlLiItpQXKWb2U8zBuN5BiE5fpgh1IuB0pd8Vfd-i3NAuw8PwyvQxAF9PgFmOUBFHYF_3elbtyPVlusXm-vNvv0ZcXTtetBCSth1UPHubMdCTG4Z9y3VdvDyNStMA0ZlkRL6uLkpbHayFZeOkQI-mEoMTNAVzBTvqOW6lMcj8GlsASN1SGohShoVoOXxZw21AQA1oxflIlps1-vQY9OkFnIezRBL8iccZllSX_mAOSArBr0C7h0JbtezzrlYOoOpDevH8gRgtuhfpEUbaTTKSqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=M_5OIVxxcCqUtsEP_0MX07fPx1H5hT6tBssRWbnua9MwrLbWrUM2YPQMim56SqiqlA_ssKO-2YUkIBUiYtKTStEu6qvXGHToUHFBPsNUVI0ZyGL01tS4bZ443nbDP76ltMiXzPDo7QLqIqNyHdyTMvCgICmI_F09-TMit8p5nhaWmrRtHYUjiCLPqCSQwuVFT9mnC_AnA5HTRNBOhqM-i_WevLwqxyStylXUFyGHMKM3_UdrHnTzcqKjigl9zjHQrP-6VhJ7-tIQV0rsh1rQN8Yjn4EckmWk6IiYmksw0dlDPsY6TXX5aZtAsXrXf7oggGk7OyFZQ7Eyh7HCHaOIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=M_5OIVxxcCqUtsEP_0MX07fPx1H5hT6tBssRWbnua9MwrLbWrUM2YPQMim56SqiqlA_ssKO-2YUkIBUiYtKTStEu6qvXGHToUHFBPsNUVI0ZyGL01tS4bZ443nbDP76ltMiXzPDo7QLqIqNyHdyTMvCgICmI_F09-TMit8p5nhaWmrRtHYUjiCLPqCSQwuVFT9mnC_AnA5HTRNBOhqM-i_WevLwqxyStylXUFyGHMKM3_UdrHnTzcqKjigl9zjHQrP-6VhJ7-tIQV0rsh1rQN8Yjn4EckmWk6IiYmksw0dlDPsY6TXX5aZtAsXrXf7oggGk7OyFZQ7Eyh7HCHaOIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTkQPU16kWdyReqWkAoP5yiaYN6uVgCjMDmyXcv3hVJeqRBLTQ02Km8LbV5G7jbtcC9irD_MSffUFDtsZEBLaOFCSBEImUIacayQvDjGclWNHfg4Uh9T9lzqtjP1DwkSxibQpsZmSHky1lQXvp9C7ADhCPV_cemVMLEeAKvdJTY6x41I8J6qVgTURa8KAeUQlzEWCA21vubP8RNNnWPjen_yEj2NpbUdPi3dKxKzcX0RYPEIM7TnQmhVNYt84lSkVVah2mI8MfQ60YSt6kSfoRA1VdrQv4TNZpab15bWVuqNyjVWQtMCR1dHtVU3MwfY6f98bbgaahfqd-MfTu-ong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX_3a9VkHS4gzek6XBNylwwKbz-rkSLngAxrc_JXhjI3naH5-hj0u-EhBL4p4bG4KjqmaDQlOqqZeEloXD26AtMfhdldaYbMI4RZm5m-5K_feQaA8WF2uJBK-Al1BpaTWGeHa8YiPVekIM865eeYRh5vlLvKUvb13ts7Ukcqg9dYhfkpf1fGrc7yglZb_R5BOKr4wEnC6M7R7R4xFpKsbhwXYgIEDOACD4H05kFjJulUu_wTYkDT-FuxjnGWtV1wX8VurNuvTt80qZZzjODFh8S2QHFZMDUtu-i5HzSoeNaAfLeRlkFn2dVFlYARXU3PbjINIfvwNO1VXQWiQpqO5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0Rx0SP4mZiEuFiIcBQxWfYmJJA0SxoDq0H_BgM5aPO7z4qjVvHNAqx9I_m8Dln7Qjc5PQJrimlZUSPZQzFO_457fHb8-AV_PlbQH0jkQF4EATOqP6ZIB06Bpal3CHtmhHKl_X-Ee-KW7CS5_4TAm6FFRCw8PRIKvFBZl-us5HXlbXYgpEs3ePE2oIm7FzlmJ8WhkrMc8mLQv6lrVVz2uzhdK-wndcxV--Nu_iDuWA9C5WbRoP3a3NHCxZXuUKHpS7wXeinLGrfSLl4cLCSHadLNlc4PGtYEJyva4N3kCI2PYUCmm6_oFfJcyJRVYHvASJQWItl55s19s7q0opdJIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skmil1i2flutLLDk_eYFIFmHQK3SYC_LSQGboh8JAyyg0mnsnQsGApRmnvFDXPPY8vaynCxQzYm7qI099FHRpeUn7q9JKwgQwLaIv-qkV_YTOFRxad8m_A44kdoSqFmI002jONBP53Dc4jH_0VF9WgXbsY99kmn47paeCtjLUHSVfWd-zoF2SOQ4_UKez5HaNOnggitcIGTJE8ZkJICRs7RF7GUhxIEkZLkNQ1vYs4I7v59yyLrgq9JIuS9weem5Xt3s0DBzyxWePKMpfQk-StESB4MKjQrG90e4kblDFfoIj4eX-coV8HOJofO6lgSKYnlYLWmtew_fLUJpvl81Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=giF9pp-2PHPzAtKs53LTXH6CXQtZaM6O5r7DyEt2veJtSRiV5hOjb_zcWv85-KQWloQv6BjhY70ct9SOoRbhIEc1b1e2CNAqWAfy8tvh2_aDNvxqnauzLm2IfSZKuWJNFBSn7MBwQvqEZeCw43oX2RYsUEKQN-FGINF__E8BX9eiLgLd2ZJ7kY_PYng0sMDLDR-ZHMQ8wFEr-Q1udq7K8pgIZVI9Yv8Z49F5THIeNRUgbC9FX1i18ikjuniVhSTIveN_h9IyAddTzjRaxKryP-LkDD4vDO63Nx-5Ac5Q730XnWJ5IBfrbXE3G1hyr2fZEScv8x-jVL21wS1eZlGr3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=giF9pp-2PHPzAtKs53LTXH6CXQtZaM6O5r7DyEt2veJtSRiV5hOjb_zcWv85-KQWloQv6BjhY70ct9SOoRbhIEc1b1e2CNAqWAfy8tvh2_aDNvxqnauzLm2IfSZKuWJNFBSn7MBwQvqEZeCw43oX2RYsUEKQN-FGINF__E8BX9eiLgLd2ZJ7kY_PYng0sMDLDR-ZHMQ8wFEr-Q1udq7K8pgIZVI9Yv8Z49F5THIeNRUgbC9FX1i18ikjuniVhSTIveN_h9IyAddTzjRaxKryP-LkDD4vDO63Nx-5Ac5Q730XnWJ5IBfrbXE3G1hyr2fZEScv8x-jVL21wS1eZlGr3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=jNN_mXdECgSQPa4Pr5dOT2TV9EFhKaTdueIPNWjWjfY4aJ6bMlpmoHB-PBAFyx8IT0ldgfJZ9In9QBU8TPHlD6wiqIPAX9h99-aSgl2AnNM7DorJJwUp0aUY8u5S2jt2yUhnQ1ashalUMY9JtwSq4h_WwDRz2WhY6jjxnDgx63WNmX9dGgRyKXjMesi5x6WuRRbN-QmSsGCNR6aC_MbEHsX4188RpulPSZABdLpURbURQaMnNyItJB0zPob2wZS-OYZJQw1htkVJG886B7QDfAx8OkXGjUg92j5HlJHsUUxiJckr8FpWGqIubyh8LWCLsEV1_F4PIPyY-VxwLZtPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=jNN_mXdECgSQPa4Pr5dOT2TV9EFhKaTdueIPNWjWjfY4aJ6bMlpmoHB-PBAFyx8IT0ldgfJZ9In9QBU8TPHlD6wiqIPAX9h99-aSgl2AnNM7DorJJwUp0aUY8u5S2jt2yUhnQ1ashalUMY9JtwSq4h_WwDRz2WhY6jjxnDgx63WNmX9dGgRyKXjMesi5x6WuRRbN-QmSsGCNR6aC_MbEHsX4188RpulPSZABdLpURbURQaMnNyItJB0zPob2wZS-OYZJQw1htkVJG886B7QDfAx8OkXGjUg92j5HlJHsUUxiJckr8FpWGqIubyh8LWCLsEV1_F4PIPyY-VxwLZtPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=WJp35j240WFBGFqem4EuMQZaxeeKuwGe4yRcd_7n0JDqtFVVgwYHAoMPK0Z2r_MpyZMNy_XFGkZb74HF0P2Kplaf4n14PPJOe_PwI-AcOemPNQ6vnaVuCQ8YnXgzWrtYhz5vnoh3J7qK9AQEyQklAOV2mBlzDKohTl9X2uFYkSYW-OAVwYMzNIvIp3mkdQ9RCTp5LSTwndmCqyGhRWMsBjaZtLJdxWVpnTy_T01RVY5DOYk_nIYCkpFrF3ORAGGbhdeopTeA4aP21BwLPYqxgR3Tnbd3scDNZemmkxFhUJ7kApijJYHACyYg4M5Ujv17me7qAmiiJffn7SK2jAWosw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=WJp35j240WFBGFqem4EuMQZaxeeKuwGe4yRcd_7n0JDqtFVVgwYHAoMPK0Z2r_MpyZMNy_XFGkZb74HF0P2Kplaf4n14PPJOe_PwI-AcOemPNQ6vnaVuCQ8YnXgzWrtYhz5vnoh3J7qK9AQEyQklAOV2mBlzDKohTl9X2uFYkSYW-OAVwYMzNIvIp3mkdQ9RCTp5LSTwndmCqyGhRWMsBjaZtLJdxWVpnTy_T01RVY5DOYk_nIYCkpFrF3ORAGGbhdeopTeA4aP21BwLPYqxgR3Tnbd3scDNZemmkxFhUJ7kApijJYHACyYg4M5Ujv17me7qAmiiJffn7SK2jAWosw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=o3BwKovQ3qbckvuqSY5Nq3SlDsHm-6bay_YkXqI-py5c4ocVwDQpM3BPVRB3QNnajJdfOXUOzr7DkKCkOObgG_UqZ5MMMbzKfi31aldOR4f5eR97HMc0SqtoZa7ZFXlpPWY42dsKfaozCSn1ifJ8AJ_0Z6B5PBMwWTaJPDFJ2MOz7c587On5w0k8dvxJyKoMGRNPiOEJ_leHKwEOjm0dcdm14M6zTTHqXq6Sheo2xI4xsRt_4Uuc2l7RuVOHUxLFSBtl-Jlk5KVETNhHrOYFnNqJ5qSVRE2oiCF7B_3bcPA1xSuaxWf9Z8x6KDQEBifa3xXUC43zk0eJeo_AhnF59ovidtuz_n9HGraXKZhFauPwvu5_R4HuwVtvl0fXCYKuoMHTNegGKTLSRFyp8F6JcU42F652W7ZZQ0d32HNdND0KIHX2drXnMb2yIB6BJbDMvl0fEQ8oDz-yXvasi8CwwMvjfl06_9riubfyZ4ANF1tiVHoDp-UZ1gXv-zmWqdlRjkGlVQU4UWKCAKaHlBu99daua26CmxrNnuOLAKhsgM24nHxefZak7oxEImiyLDSia3g1lmoSq8UvGmjrBPRcD01rhOn3WAiMNdO4WF4KCHZZGG0_ggOwI7qro34FhAknTaYvCmkVzt3gxsIDPctUkV2N9RNCirITP34V4_sUTAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=o3BwKovQ3qbckvuqSY5Nq3SlDsHm-6bay_YkXqI-py5c4ocVwDQpM3BPVRB3QNnajJdfOXUOzr7DkKCkOObgG_UqZ5MMMbzKfi31aldOR4f5eR97HMc0SqtoZa7ZFXlpPWY42dsKfaozCSn1ifJ8AJ_0Z6B5PBMwWTaJPDFJ2MOz7c587On5w0k8dvxJyKoMGRNPiOEJ_leHKwEOjm0dcdm14M6zTTHqXq6Sheo2xI4xsRt_4Uuc2l7RuVOHUxLFSBtl-Jlk5KVETNhHrOYFnNqJ5qSVRE2oiCF7B_3bcPA1xSuaxWf9Z8x6KDQEBifa3xXUC43zk0eJeo_AhnF59ovidtuz_n9HGraXKZhFauPwvu5_R4HuwVtvl0fXCYKuoMHTNegGKTLSRFyp8F6JcU42F652W7ZZQ0d32HNdND0KIHX2drXnMb2yIB6BJbDMvl0fEQ8oDz-yXvasi8CwwMvjfl06_9riubfyZ4ANF1tiVHoDp-UZ1gXv-zmWqdlRjkGlVQU4UWKCAKaHlBu99daua26CmxrNnuOLAKhsgM24nHxefZak7oxEImiyLDSia3g1lmoSq8UvGmjrBPRcD01rhOn3WAiMNdO4WF4KCHZZGG0_ggOwI7qro34FhAknTaYvCmkVzt3gxsIDPctUkV2N9RNCirITP34V4_sUTAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=K7ar4BuCyrRp_fsFdGU_-V4NrD4xltVOVqPqyN-11QcyKXQS9jToEfw3u68rHNyrh-CVsFSwz5pvuc54SN7MTjJ-JakBTFT0rYDYQqkRG95Zm6pn0Fc68H5I_g0fQKZfCp1zW3IpMqiBlVm-5wM0a355bUUCIIqSPqb8Spk-7e3Svp9aQ4n_PWSlK2cGYG_lZFvPQeVwLpccLiEt21bEb2xcoSPeaWvEbqrFzePkfTTGc_ODbeF_8V8-ri6b7mAWSGXTtN7DAibVTizHL0bHjGW8wJz2iit8m1orPWVhY6h8vDpxOrDMkGQQy-pfRxTuZc6r5WfN04Jnv_gq15TbgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=K7ar4BuCyrRp_fsFdGU_-V4NrD4xltVOVqPqyN-11QcyKXQS9jToEfw3u68rHNyrh-CVsFSwz5pvuc54SN7MTjJ-JakBTFT0rYDYQqkRG95Zm6pn0Fc68H5I_g0fQKZfCp1zW3IpMqiBlVm-5wM0a355bUUCIIqSPqb8Spk-7e3Svp9aQ4n_PWSlK2cGYG_lZFvPQeVwLpccLiEt21bEb2xcoSPeaWvEbqrFzePkfTTGc_ODbeF_8V8-ri6b7mAWSGXTtN7DAibVTizHL0bHjGW8wJz2iit8m1orPWVhY6h8vDpxOrDMkGQQy-pfRxTuZc6r5WfN04Jnv_gq15TbgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=YeUsUVO0_3mnzOl_Jt9oRpCvlfHVrRJ9GHnVM2xhrDy_rK7zu8A4PB7tw9jEuEOz7yJpETdL0SfvsoIwlQASGtz9PGdqDnw9aA3vOPGtK_leWH4CJYuQAO9NqTceH41As7OzRMBxY1pFoUwo4eEChOY4yg_8ZSzN7NATJ1Ow2j1UXhh0I-JQowTMo-6BNMmyc2f1KDG63x8CTFVKGvs08xH_DLpmpPJPEPhkIL9sRrpYh6iO2-u9UUlwApKJYQa5bP8F82us0ga6DS-AMwg2deUGwcxSMFxMgw3egGFiWGrnb5KTh0POSKNiDRw__OUuHoPIDQvl6L9ah6DFILD2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=YeUsUVO0_3mnzOl_Jt9oRpCvlfHVrRJ9GHnVM2xhrDy_rK7zu8A4PB7tw9jEuEOz7yJpETdL0SfvsoIwlQASGtz9PGdqDnw9aA3vOPGtK_leWH4CJYuQAO9NqTceH41As7OzRMBxY1pFoUwo4eEChOY4yg_8ZSzN7NATJ1Ow2j1UXhh0I-JQowTMo-6BNMmyc2f1KDG63x8CTFVKGvs08xH_DLpmpPJPEPhkIL9sRrpYh6iO2-u9UUlwApKJYQa5bP8F82us0ga6DS-AMwg2deUGwcxSMFxMgw3egGFiWGrnb5KTh0POSKNiDRw__OUuHoPIDQvl6L9ah6DFILD2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJLisXnRRrJ11ZrmHz8BS9nTwLvEliCzbEgJRsHwMg_nK84DkKCCwG7TPH-s0rUTqh6FNvCOXm1qbbOcwAhA8TPgYI1pEOc0V7Ob7udR_zgrt4a6S3aoUkr6dMu-DQ6_GPxO3Ne1fjFXojHz8I3ViPFjgpF8doedVccr5EUhe7ERGnkF7QD0t_EfpbSH4EikkTgA6jVsMbPnyKTt9UJykJR_b3oi6wr2avbcc1M2TKXFBdshkquUi3ubLbZv1MjM3l5qjWzu3CuVjh_V7F60-wqDFHt3tiE2ThVIrpUm_mycJcu8Nmhd_d9dK9giUGHN8nx__lAjk6IlSlZauTIhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=tx-1ai51Ih7vItOm0CGxY3AkATKX75hLpYdKVYyN62kiOI5PKsubrXXkTsVVOZGDzx9puDRydvBPRgz4nCqTB-YeAy-WWvQwZ7DVOHKLajsXnLHKozDRTcyPti4uwwye5WjhqktRusDwxECgCJkId7x_iGlSrAkhRqvQZUbhDYTSbJys1zptLDiASlPzvUWeD5nA3UTwKaldoJhxDRuCLtPKm-wplXVDF_aTCabev3kjff3l5A0D2A4yQM9zKCqpANIRy6XX2PeVjwPMGX9pJ4jyp-irjHSpsuD-UzabQ5HMPb4wC9N_pgcR_WpX5F43zlYdXVMDTuKKoJd-ZQd2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=tx-1ai51Ih7vItOm0CGxY3AkATKX75hLpYdKVYyN62kiOI5PKsubrXXkTsVVOZGDzx9puDRydvBPRgz4nCqTB-YeAy-WWvQwZ7DVOHKLajsXnLHKozDRTcyPti4uwwye5WjhqktRusDwxECgCJkId7x_iGlSrAkhRqvQZUbhDYTSbJys1zptLDiASlPzvUWeD5nA3UTwKaldoJhxDRuCLtPKm-wplXVDF_aTCabev3kjff3l5A0D2A4yQM9zKCqpANIRy6XX2PeVjwPMGX9pJ4jyp-irjHSpsuD-UzabQ5HMPb4wC9N_pgcR_WpX5F43zlYdXVMDTuKKoJd-ZQd2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iunyvr2_xkkqEdTZS1Jk7XzZ6-UekK4L3ET_wFB_uD3BgN0ZqrxMoPjSLx4MtXQ85xkp-8C4nrqFR6Pb4BMX1r48Ncj4QZWuObURKjs1taamyzTLpUGyoW1BWqEp9d7aLOnec4BDzrIUaCASL74LjPXCoPUD-Oipk-4hGnRa6f3UuQ85N4LJah7yggQWNXuRusIsrjQwEEgPzROLqpdCQavA2TOZ_FuTgAvabL5YFM6H_wQUqlS42zuoscfjYQxxdUTn6nCDYgjHGtYU7eQ15P8drWoFHduZrvNP99P-uvL0Hh60ZGe2acu-v5EezLDw5D4KOFOa3M4A4S9NVXs8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvzno4UC7ZnivkG-h8XoVV33nvO67BjFn5Pu2A6vSoU1r9MEIdDUYnHeXmVTbLRVJZhgx4zVhDfrO9PdJ4KIwXUe_1hEYfZP-1ym4ystjz5s4AIDu6LQJ6XoaWjLhvk-4JHAQzBFbPHgkRiMTE8avEoTnPASLfJP9MqJKceatvYWkw4x56fOvmJr3GuHBQaQZ8D8CLyrYNJpzFnC4Nc5OyePr-LJAjowAE2RLYEqXggKtfVxCzYKLMETY4Gzjfu4aelmFEmpgJsgCVwNYINklZAIH50kLdCThjz7wTr82j76WdtbN0AiA-Ht3BkrYScBT9tDEZWcgLJEHQwp2xZtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=i_I-TsESFyJNdXqrLF-1Bo_6QeeIrZyDkV1_hHTjZgo2Jkf_P1zMkXl6w0NU5puhtaHwM2cPWYF399Vq5N6GxHNPevw6S2Qk2n8f3XSo_ERnYaqqkBTeiILI_wOldczOcQs9B1nlm1nR1Tbc3w79YUPXCglGMqKYcBZ-aMaCQINzqZHGXF9DOBecFOtGiPVj-1WNv598cin3RGtCnGkzHR3RySOxcrdNJOEWpPxbho98fClC7lfXVppdrf7mhzI3_aWdSMzulV3QguDfX5QSy67TZkSTMPPgfoLgViLsy1AXEz9RD5BXyLu7e3kgPPpJzGKHWijt3TiWrNknPUfang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=i_I-TsESFyJNdXqrLF-1Bo_6QeeIrZyDkV1_hHTjZgo2Jkf_P1zMkXl6w0NU5puhtaHwM2cPWYF399Vq5N6GxHNPevw6S2Qk2n8f3XSo_ERnYaqqkBTeiILI_wOldczOcQs9B1nlm1nR1Tbc3w79YUPXCglGMqKYcBZ-aMaCQINzqZHGXF9DOBecFOtGiPVj-1WNv598cin3RGtCnGkzHR3RySOxcrdNJOEWpPxbho98fClC7lfXVppdrf7mhzI3_aWdSMzulV3QguDfX5QSy67TZkSTMPPgfoLgViLsy1AXEz9RD5BXyLu7e3kgPPpJzGKHWijt3TiWrNknPUfang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=OJEr8rqXcsr_l8nv-eEOzoyj18Wo5ZdvULtPY-kz_ifPFBExfpLsUhZUXIkiPBl8XKt3qMeqSXvP7NlBtvGB2TsPaNDyLlOZyxCdVoTWs_uuhMx7UUnFWnBx6vFxs6yYIm8LJy8BPuO5fdhiy-GR_sIpxkDKcVREZMmSuAMzpm-GGYGXhGaii0EEhBCe4N8u1V8Pa63GEJNboeNNwZqWDERWGCMxUmk9NN9MINo4BgN3K56TLjK_t5OOBrCX3BbwOJ5B4yiX_JzrGjjrqpHhkDKt5BBq4eBJ3JE1y58M01LAOCvc-osaj902iw3OztBtlwjQvjuWJ2dJxDe1WC4NhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=OJEr8rqXcsr_l8nv-eEOzoyj18Wo5ZdvULtPY-kz_ifPFBExfpLsUhZUXIkiPBl8XKt3qMeqSXvP7NlBtvGB2TsPaNDyLlOZyxCdVoTWs_uuhMx7UUnFWnBx6vFxs6yYIm8LJy8BPuO5fdhiy-GR_sIpxkDKcVREZMmSuAMzpm-GGYGXhGaii0EEhBCe4N8u1V8Pa63GEJNboeNNwZqWDERWGCMxUmk9NN9MINo4BgN3K56TLjK_t5OOBrCX3BbwOJ5B4yiX_JzrGjjrqpHhkDKt5BBq4eBJ3JE1y58M01LAOCvc-osaj902iw3OztBtlwjQvjuWJ2dJxDe1WC4NhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Cgj7Ony9BqFEza-QQO2fpVY1cG3GEhia9QOxSU7oamPxctLcnPF0mgKp7h9MtOJ4KwoSQr2Pjrm3nNh5_eAppiWjHnV39pUEheKv6_UFJAYQg2m3ly96YMe9k6xK7uI2uNW7nqg1lZNWPs4eePrjPjjZlyPn7KJ1YWr8q5fv5fzNfYZmjWWrPLOIRlHj1xMoTl2y2eCqNmmMDPUIIsjtVrBCWXQisEYc814uYC7GiXGYtkmdg5u_Tky2LT6TQk7MWur8Vm0qDQR78VF2kHJtohpx6ahzsNBhtL8n9kq8Piy_19WOFyfnnOOeY8MUmAy1Ntju4t1vRRfZsFTiR03IYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Cgj7Ony9BqFEza-QQO2fpVY1cG3GEhia9QOxSU7oamPxctLcnPF0mgKp7h9MtOJ4KwoSQr2Pjrm3nNh5_eAppiWjHnV39pUEheKv6_UFJAYQg2m3ly96YMe9k6xK7uI2uNW7nqg1lZNWPs4eePrjPjjZlyPn7KJ1YWr8q5fv5fzNfYZmjWWrPLOIRlHj1xMoTl2y2eCqNmmMDPUIIsjtVrBCWXQisEYc814uYC7GiXGYtkmdg5u_Tky2LT6TQk7MWur8Vm0qDQR78VF2kHJtohpx6ahzsNBhtL8n9kq8Piy_19WOFyfnnOOeY8MUmAy1Ntju4t1vRRfZsFTiR03IYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L13rXINcy4vkAreNwjQLQBaqvBnE_9O0DkQUYQgSa3dF1xBqcO3-7ml37P_SXx8P47R6XfDO-_dKjrK5ZlBcj-GTLa-MQNr0AuhSla9Wc_tl2nLqL2pZaASwwHcU2xU2K1qsQ48RqFIT7t_yjcjgfNRPlSm9yhX9ejxSC-WaRI0Y--7YrMwSVUbWibi1EQ2nA9vrzN78mSoSgtbXOj7d6-78A7bjCT0DOT54fFE8MOw9XX8-JPCmnXVCCJl_0t-KbJ5RQGD0_Xx00b0nn9_8Jo9eeAI638zwNYdL5X4M3jqoz5jH6MnBjhKX-_u6LOHMZ9gHF4o369qPF-yZwhcrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=W4fglQ-ppkAK9tg4ptCKgdxHUSN6PkUolqDU8inx4mEUMk5xLJpztE6Qrmpl5OO73RIPWGq_ocKH4M-7OQ-gq1uK-ZGWri7BdBZ_JF__UQt8HNqPRKsDeCaOsKsFTUMGwG35YmNQfrI2RRs5iKB-8R50uAoe1bjbYNg3lyw6Na_vIfzzlmvrl5hJQxbZ4r5j3RZlUPsXP_JDq-ynuEdlz_pqE0M89g7yrdGE7SIx-6mGXnWdAPQtN10hl3SEdDPf9DrH1swux1KAJcf3gG4sCc11olvej9UqbhZ9MaD4etq4dYioWm_E740Ni-IhVkezJ3cjhRMtjuo1OwR9P_AP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=W4fglQ-ppkAK9tg4ptCKgdxHUSN6PkUolqDU8inx4mEUMk5xLJpztE6Qrmpl5OO73RIPWGq_ocKH4M-7OQ-gq1uK-ZGWri7BdBZ_JF__UQt8HNqPRKsDeCaOsKsFTUMGwG35YmNQfrI2RRs5iKB-8R50uAoe1bjbYNg3lyw6Na_vIfzzlmvrl5hJQxbZ4r5j3RZlUPsXP_JDq-ynuEdlz_pqE0M89g7yrdGE7SIx-6mGXnWdAPQtN10hl3SEdDPf9DrH1swux1KAJcf3gG4sCc11olvej9UqbhZ9MaD4etq4dYioWm_E740Ni-IhVkezJ3cjhRMtjuo1OwR9P_AP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=gm75WJvCDG9zsYmpkoMt4XYfx2apGo0Z77W2-dCTtKJ-S6qPXwo6B4KUFjGmk7mDgvk0yIMPnWtlnvWrB_prlgpBGeOTnYp7Sdh82JVBmmj7zkVUquqxykSJhR4znS6swaqNJAdhX8lV_UPQJneSs-LL_YymOLAKki3bBiQUJfcb9Dt--TcbLmk1auhBnrwDkj38EAYm-QVnekcJ_vlXBRmfd433O03r5NYO5tV0K0B509HFTxK7CRYgIpORHSppPGJcPe_huPJ2_17OlC4VWRcKHDqh0VeRRt6y2ZCNwBNRl13KL0l-2F64aSk5tXij9StamuD9c8-7NbnfxlblKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=gm75WJvCDG9zsYmpkoMt4XYfx2apGo0Z77W2-dCTtKJ-S6qPXwo6B4KUFjGmk7mDgvk0yIMPnWtlnvWrB_prlgpBGeOTnYp7Sdh82JVBmmj7zkVUquqxykSJhR4znS6swaqNJAdhX8lV_UPQJneSs-LL_YymOLAKki3bBiQUJfcb9Dt--TcbLmk1auhBnrwDkj38EAYm-QVnekcJ_vlXBRmfd433O03r5NYO5tV0K0B509HFTxK7CRYgIpORHSppPGJcPe_huPJ2_17OlC4VWRcKHDqh0VeRRt6y2ZCNwBNRl13KL0l-2F64aSk5tXij9StamuD9c8-7NbnfxlblKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ciktxyJIljsNAyyYWuF7-YftXbVE3AV-Qnl5-2AEse7k8IMk79oPUGj0R6FihQteRt5IcWh0ncmL2xVPIF5OOu11RYy34dXUMdLBjyBTPeoEX569fIAN7YVJHKfhYGuU8VRJPAtTROYP2D2JLixzSRlOZ7nS1gcJ5WZIi33U4xWEfuDCmOZoG6tu29iIqCtFKetvdCpNt5JBNaVFwmWG5FyxQxUw0OoQpRT0CXngcbeqaiBS8K9HHEJYVZTRpdRfo-1zni21juf7sdFCGMm_W_IA99nfsSbIm2MLOmslGzqF5KaQdFpamFFRe9aXS04JYIJ3L22Sv8V-rZyAqJphhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ciktxyJIljsNAyyYWuF7-YftXbVE3AV-Qnl5-2AEse7k8IMk79oPUGj0R6FihQteRt5IcWh0ncmL2xVPIF5OOu11RYy34dXUMdLBjyBTPeoEX569fIAN7YVJHKfhYGuU8VRJPAtTROYP2D2JLixzSRlOZ7nS1gcJ5WZIi33U4xWEfuDCmOZoG6tu29iIqCtFKetvdCpNt5JBNaVFwmWG5FyxQxUw0OoQpRT0CXngcbeqaiBS8K9HHEJYVZTRpdRfo-1zni21juf7sdFCGMm_W_IA99nfsSbIm2MLOmslGzqF5KaQdFpamFFRe9aXS04JYIJ3L22Sv8V-rZyAqJphhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJNKRB0QoyS5LL2Euj77zXGLJ5MH-zhkT6esdBBEdf5HcEk_XyAKi4YHs6_1P7vczeT0LPsLfWteMgHSg2U6DdqCg5VKEXW6vvSY3r6h20YStZXR_hl6U-ihxdlEm8QjAsHF7x_WuhAkngA6jUrqMFoef-GjTBd0bOla6pkXM2Wt9h4vV-DfTVKTMVkhZv4J19VgeF_Wly8eG6A-CpYTLTr3EFS2HLOzE4FkuyMytsldSacQWKihnDfyUrGex5fSmmW15XnPGyHBOIgqxgL8TlHbDhO7cRh8sP6lH_8scnPV4BjF_dJi-KqzUjRrTZ2g0rvXJZHkBTWC13rkOekskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=IS22WJwTdCXW-KjlTTesb-B7TVp_9LXXCZjtlbXPF2J1aC52fIdV7OT9Xx5szo_Hymt1NoesTcfXg6IxGXdh6NMBvKCJdmKvfOw-W4YTM53ixecHJg2FDXfE0JG5_oK2PmtuQbIn20q9sKv1NdIh61NizqsDxUbobmHA__eiXE70jxv1qJt6rtkJQX1hMxqFrM_jEDn9bw0JR397nptZKPdOVrCn_VsbPp6NKY6S_KP6cOFShWjNuWCwdhzjrELVnA3lxnMvwV-XV8zHu0BvsrYuIaI-GSEdmeLV_KGTjotHW4ljFZydrgYQchCxMmv-5jWYeHcEpibZUa9sYkXjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=IS22WJwTdCXW-KjlTTesb-B7TVp_9LXXCZjtlbXPF2J1aC52fIdV7OT9Xx5szo_Hymt1NoesTcfXg6IxGXdh6NMBvKCJdmKvfOw-W4YTM53ixecHJg2FDXfE0JG5_oK2PmtuQbIn20q9sKv1NdIh61NizqsDxUbobmHA__eiXE70jxv1qJt6rtkJQX1hMxqFrM_jEDn9bw0JR397nptZKPdOVrCn_VsbPp6NKY6S_KP6cOFShWjNuWCwdhzjrELVnA3lxnMvwV-XV8zHu0BvsrYuIaI-GSEdmeLV_KGTjotHW4ljFZydrgYQchCxMmv-5jWYeHcEpibZUa9sYkXjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrPZ4pvlPR3oeEmtbgpKb_foM4bBZ9mAl55P8FrfSQb9grkK7IFc6FxPI9RAFpyEsfMroVNHhege2qjVGUjqwxzU2ohySSSsZMjNH8QzCAU17Pz1k3iv9Q0xnkbuY1JDWwi4uHq4GRSfXRA2BxIAdgCVEMiNbAdt0AGUZ-IyP6Cl8_WfaSOnGGnzUeZZ23r4GiKTIxZyY8yjj_CerpGIt5Z6BV7fPLVoZfYmokYD8YxjEH7N1NUN6lnPZjTOtGGnedPP-AYlWq-TM7r4-PJ1_rME6sR7HyeAAxL4XjlLfsQpf900wt9tMPv4kBCBUrMedUlj7N-zHvctJAJ5LQHaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=L2S9iddemD2a63tAtsgcfWt-NugpV7a4hbFJ6XCHrDSYFSPAe8v2zmRkKIWZWDuu_-mbhcTUP3SPU9Wkto87nfRYXreAloQiJuZK9N5rZdKFnSfz5JBSuxDTwJSe-2veEAftlmqH0TrfFAqW5_RBFgYADpPXz_8g4tc4O7RezWx901ZvI0wfgAiSiahiP1tw6KsLMGmexjnMyeIKejaQWA0cb5qfvgxkWAmUF3LmvD8XhDMI6yUxiH9GA5KzYkNplmcSKRHRMbfeX86MjQyxCrgZImwBV0yEXGiuoI1i29NGPn1JMIQ02dZok4cyhWjqTwjN_fYa5y-zgq2NcxxC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=L2S9iddemD2a63tAtsgcfWt-NugpV7a4hbFJ6XCHrDSYFSPAe8v2zmRkKIWZWDuu_-mbhcTUP3SPU9Wkto87nfRYXreAloQiJuZK9N5rZdKFnSfz5JBSuxDTwJSe-2veEAftlmqH0TrfFAqW5_RBFgYADpPXz_8g4tc4O7RezWx901ZvI0wfgAiSiahiP1tw6KsLMGmexjnMyeIKejaQWA0cb5qfvgxkWAmUF3LmvD8XhDMI6yUxiH9GA5KzYkNplmcSKRHRMbfeX86MjQyxCrgZImwBV0yEXGiuoI1i29NGPn1JMIQ02dZok4cyhWjqTwjN_fYa5y-zgq2NcxxC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMT1DrJXz83Wd-P_GeNoSUR_STA2RQ6wzcMdIqX5u9isS2PiQTqKNX7ohxcQ8d6f015XoBDihiuyjbYL8ZQjkQKhvk2OJka8aYTOLcu4QNWASDQ6Sr7i0iMyj_soWw0Y997tCoq3jH93pAaZVnGYkWH1pwgyLF3IWq3HlUrd-R0nJcYJmUKwff9D8mCYeOIBgSkWuntMGPLrodiL68iKgzdh-2QjcKwDxvPCBtBW_hkF6ICcQnea_KXkNjU5_hmKPF-cWWaI6ufqSwEJOXU7bN0fT0hsd97B55_EL1HB-Lx2nGq4bzseJvVYwb9A3E9ZEI1-uT5W7h0K2LELFW0_DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=YCKZF5iuWiv_atscEXk2HsfI7FRIQ2-6pp8h375mGaB3maOO70oDe9rlWDhctT0ep-zBhTrXfhbVzS2qOk3TdkSfMaxo19dTXogkpCI4YTLQPKs-zgK6puIN8O3hkgadpultitR3JhwaPcHLJWiQ3OILXWRsYfpTE85szQa1HZO3wqSSE9L6ugdIiIdazCKepljLjEoYcUQojzdNrX0gYULlH4Ltpt2dpeYaXhQdMbQUXhDj7PLC08NCZV9_a3aQrXiwMC6P7h6YV8Z0F8mVtREV_-P6AO-xlaoOZ8_0dR1w-_2-AEIM1Pp9yZ15SnknrT_Yos1_GiYW6E0o6VLTLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=YCKZF5iuWiv_atscEXk2HsfI7FRIQ2-6pp8h375mGaB3maOO70oDe9rlWDhctT0ep-zBhTrXfhbVzS2qOk3TdkSfMaxo19dTXogkpCI4YTLQPKs-zgK6puIN8O3hkgadpultitR3JhwaPcHLJWiQ3OILXWRsYfpTE85szQa1HZO3wqSSE9L6ugdIiIdazCKepljLjEoYcUQojzdNrX0gYULlH4Ltpt2dpeYaXhQdMbQUXhDj7PLC08NCZV9_a3aQrXiwMC6P7h6YV8Z0F8mVtREV_-P6AO-xlaoOZ8_0dR1w-_2-AEIM1Pp9yZ15SnknrT_Yos1_GiYW6E0o6VLTLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfUSTwzNH8Q8MvZwkdBOibk_I2_zPIvZp4EU1ZAX1dHdr149mY2kAFyn4nfYHB_4_E1Ash0w9ArlOOzB6cyqmLzGTh0tIoeaBHBo6x-1Up4VSSdNckEYPKiYG6XjJniHPicM5MDzVV2T3VwdaQtbkdL6UAKEhEJR0ahsTzVbLTICwGWuffhev8ITsDHriWURRt3znbuM2QPc5RGen8SBZoBS0DhQn1IY6HjdYs8vbQknq5hxzHJmBmUvIz5cB-_5ETkoHZhJFt5K9DDHdGjD0J0Sp6eaicw__9xphoLcoNYEvspfQ8KVr7sZ8TaETwyflVpsT2nhRS33HeB_ukQghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST_3I1tloAO6yw4MwvxsMvtIyowSbm5FW2rnxe9W_bw5TtnKn8Sxp7o_RZI6Y7hUL28WvOmbHB3xT86GovYA6ynf1EifcUREtgpq2KYntpCJjsMYN0_rVyceUmtdGwgFKr6fzQPSoIbv8cqzcOamQ6UrWa5iOVjgcB5yKjttmctbPfYg0woX6AyssxSV8yzC6kUBE887wHpSwNdtAHM0wRsQYed6l6ZikL9mJzORcTIcIdttf0gO5byIcAaMB1by_YfOGZ8JIgrgUoxPQ2AA2E5GCXd6EjJ_mNW8Xa7jrmQxu0aYSes0hL2iCZvWrx0s2pk9OhAQdLJ07DrHk34ZkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=o4ble3BBrbRLG1k2_ke4jX0O7naHMXiq0OeGFBCMExeMQlVES7hquFCPFJWkn7yUP1Z-vSBzM81oYWg95NWhXUw2BcWy3JemZCGNNf9ia0s8qNUWx5SVq9mnZIjHtJn8vIDqojeTTfXOoIPN_4gSFGoIqhQTKSoy3nz2vRG_6INxZBfZYQqZycJ60-7V0x8v6tth-Ey2885Jzyl_Mcarctd0BX0rDkwGQAzHFwOHuSFKnwJVhgkkgD1NQ69-3WVdmKUxAUDPhfshNZgKRTQ6kL3sRF1HpQsdJukiTpsF87MaKgmZ5Ob8UpwgFVEOw3kM0CKf5m7ly1abXO3Mw9iGEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=o4ble3BBrbRLG1k2_ke4jX0O7naHMXiq0OeGFBCMExeMQlVES7hquFCPFJWkn7yUP1Z-vSBzM81oYWg95NWhXUw2BcWy3JemZCGNNf9ia0s8qNUWx5SVq9mnZIjHtJn8vIDqojeTTfXOoIPN_4gSFGoIqhQTKSoy3nz2vRG_6INxZBfZYQqZycJ60-7V0x8v6tth-Ey2885Jzyl_Mcarctd0BX0rDkwGQAzHFwOHuSFKnwJVhgkkgD1NQ69-3WVdmKUxAUDPhfshNZgKRTQ6kL3sRF1HpQsdJukiTpsF87MaKgmZ5Ob8UpwgFVEOw3kM0CKf5m7ly1abXO3Mw9iGEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
