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
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 23:20:31</div>
<hr>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnJoDBqq329PIGb4Afybo7MsPSivmktuG4l4eFtSRCTE8Q_Z9ZbvnQYUDu4AsgkPLCMJzGEZGj85ihCa8zN_IyCEaqmT0NAigLIko1O3wAaFZ138nO31LVr07-TguZaItVw9oioEVtK0RjafdXt021BJ40b-orsFlpyhw0HQN20E9jCNhG0OR9Y1LJOSn6gZmoAjwr1lGCGGEZF8804etaz1i8YjFvbjPZckZwIS5S9hnkPKzdnfnIqHbWhw-ag8u-4ofozs79Bd5n_yEoVMHY27_GWsEA3y8bVGpqz6VXteCdKD2C7-RC9THkauZSjx8bBTEqS1xYsSiELkEzyTPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnJoDBqq329PIGb4Afybo7MsPSivmktuG4l4eFtSRCTE8Q_Z9ZbvnQYUDu4AsgkPLCMJzGEZGj85ihCa8zN_IyCEaqmT0NAigLIko1O3wAaFZ138nO31LVr07-TguZaItVw9oioEVtK0RjafdXt021BJ40b-orsFlpyhw0HQN20E9jCNhG0OR9Y1LJOSn6gZmoAjwr1lGCGGEZF8804etaz1i8YjFvbjPZckZwIS5S9hnkPKzdnfnIqHbWhw-ag8u-4ofozs79Bd5n_yEoVMHY27_GWsEA3y8bVGpqz6VXteCdKD2C7-RC9THkauZSjx8bBTEqS1xYsSiELkEzyTPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ialgFhCO0J1ZtPdQAHYBKSWHdoSo9Y_1o00Gb6rLgLndnxo6YmBqWdM7edJXkjw_Jqpi4RLXT9tgR79wlSmstbS9VbeL2HzPUyU9s3_-5oB1gmr9UjGw44SsTlNnFdgoYrqEdyniXNauv9I4ewKVfFQN8AHZAZAHhwh-C8cAVLHsIM0BkiEYwN5IdrNeddfMu_tIklZH2nAkoPaSx94mSykTpIXZb29Sxrmdyigsrhqp8e6qfqCqR-GSQqHZYZJNtyF3x_3TJVAlCkdyQD8EInLZ8a5FbVGSwcrzikEXs95Efd2pJr4exc90-DetnjT1Citqnt46xpF6Io3zL_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWmwlNt4IhEOrppCJl24isvSOzsHX0_BoEswH3rS-aT1nwUI--J4kUsQNEONwjyFEotGZbhfwut8AdqA5ILbRxLOffMlyGgyQhFasXsMxGtGPQkZHyW5_TcEML2qY-DB9S4iuX2IYzQDuBOZcUEvGfvqG4HF34GSTPFSzKd1u9gvhNLAJyvfs3vq3UNNC9ddxzDlyofeiLp68qMkNHTtGjWApWRqvSbUErLdskDkNGIX3cF20SzcZdVnB3ugRT2bdI90lXQ2scJMbFjQt-Wq9oUoKGr4T7t3Ai0W4WxIaOLYpY9fkO91kzJTwyQTs-YVAACvUj3AEgUZIM877lbm8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT8zue9NElwuwhbZojsy8eRUbMl27CLw_RjiIkbShKNn8vrKqpiTZgsL4KHESymcU6beuSKWFsHi6jEPCWktQ96hHcZxkKZL3xjQZKgI-RaXIV-y8oBgOwaDBcIbejsxJYNtu_-I4Zn3ett_JH5cfigw7vcdSTtneD-XaLXaUJhZHJG41RWH4lVga_NkQfwV50Dm8z01GlNuIptR8eJjhHoXFLME4OnWX5BrU-1etoLD7PDPWUmMASoVDscQtLk01_sOwsrRO6D6i_apMOU9u7QcUeWs8lOZ4y27kAFs3KR_jAJrGpUrl-usoV9bYsUR4YonflwZxv_SD8rJVU0N3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilLOk-WsBA2LKM-bZXiHxZn0x7KnML6MLJJ9VdRuLy4RRi0UBIWrYMmo97KWIhX5FIdl6eP6SyrMaSC3_gWDVD9bPM9JwoH7TRFAyBUGRPBU7NC7MhlkYSENG1YqK-gt_5HLQPnnz7TmqPur0qWlV5SrMRmHrzPDjk0y3urvvYvEaxOwqWS-Sy3_jKTofxzvPlwcp_l643Wujmh6PHnZN5qVnHxSdOR2RepD4GdWYTgSbcwjd3SBdMSrO3uN5U89uR2Fsx06FDv-QaHe78qUUKETCFEYw0Joek43l6rm991ZkHi_PbJ1oJ5_7xdCijV87VrmHGmGQqZ5bhikcTwGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yoxtfii8wIqr6Mt5hpI-HK63nYZWB0TuBnKiBE2d-c5lx_pP7tFgSY_WY-ipSif2MxgfYGoKF4rv1sSmL-w0ayY3PJO9PduUz3P_vy_FJ6nF0lU1bO_LPcxhVaoriFYkYO6JxYPkzaLa22HgPcosLXcSpJDEYS1Qo9kuJ-TygKA5ByHKTXyvk1caNVxSux-nazU75iUNPMAzYOxAUhifpo0P1iFwfHLjgJFArp5WTqFkq0E8gV6-JkP5fI5tdznj6ej-WQxSlLMG858sxV8XwqfEQbO_IR5sVMusI3Vp7msgySqXQdVVhNCPYH4Fj9676x2XpHHc09buWUATO6bbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U6WsH1HnTmQwS6_APfKUPeTsqEplrXLDLkd6f3jT4RufLb4LwLQBsSfVt7bNrAMJ4o70gMPlxQMpy4glizt8kyQtpWcoPevnUquVUQvQylvkLkQ44PGUUAsziwgocmP0MmuFiD9QjaVE1fRibze0IKk_kzI1FO6s8Hz-QQ614ass7yNMwDFlEGTu0DLQMdsGtSGKA8O6j8Ryi5ISjetO5erN1g1YBCgRLX3cPjpu8Mw90nGoH0KFPD_49cpPC09wSSldRWOjsH9kf3iy7FvO9cWMXP3iyLc2pIYitYFO_H4qzJ_iIfguDgetYFCaf-oofUbKmhZfNOk3nOTR7Pz-SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U6WsH1HnTmQwS6_APfKUPeTsqEplrXLDLkd6f3jT4RufLb4LwLQBsSfVt7bNrAMJ4o70gMPlxQMpy4glizt8kyQtpWcoPevnUquVUQvQylvkLkQ44PGUUAsziwgocmP0MmuFiD9QjaVE1fRibze0IKk_kzI1FO6s8Hz-QQ614ass7yNMwDFlEGTu0DLQMdsGtSGKA8O6j8Ryi5ISjetO5erN1g1YBCgRLX3cPjpu8Mw90nGoH0KFPD_49cpPC09wSSldRWOjsH9kf3iy7FvO9cWMXP3iyLc2pIYitYFO_H4qzJ_iIfguDgetYFCaf-oofUbKmhZfNOk3nOTR7Pz-SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=NLyOIEx3vVsc-fJzEXbJoLIhvV20Q-h-zQf8enX9f6-iM2cYJ2E9ik4UsPSJHsppCroX29Dc6zp4EtOPtx3RJJ-cZVSSFVDD2-88WzQJScpz3tctsN7p1SJnGNrK7u3b3Q7MWtD2O9K4S1xmCjkxAKSRyaiQtKRfNoovGw8CWQac5_50rPgjV6YY3bLRuHyV5zWp-CFYyUia-Vqth5Z5Lrojeja6OUIPjucR6QM4hpomMlkDv9hUF_oxNiZIEKZKarlSsvLW8DFo6ftksYgiMajD79Qam6aN4U1dzcqVhXXo1woaPEVnEmV4VqPi8XtIhS0Sm_VHcVZ9s1Baw05EFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=NLyOIEx3vVsc-fJzEXbJoLIhvV20Q-h-zQf8enX9f6-iM2cYJ2E9ik4UsPSJHsppCroX29Dc6zp4EtOPtx3RJJ-cZVSSFVDD2-88WzQJScpz3tctsN7p1SJnGNrK7u3b3Q7MWtD2O9K4S1xmCjkxAKSRyaiQtKRfNoovGw8CWQac5_50rPgjV6YY3bLRuHyV5zWp-CFYyUia-Vqth5Z5Lrojeja6OUIPjucR6QM4hpomMlkDv9hUF_oxNiZIEKZKarlSsvLW8DFo6ftksYgiMajD79Qam6aN4U1dzcqVhXXo1woaPEVnEmV4VqPi8XtIhS0Sm_VHcVZ9s1Baw05EFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpnlFpNlPNN1etMb7K6RKJNPIOk8ffSJHzIzrfH7VJX5pHVl6zFdnE-6FETUMYiHnPbsnWHvMUFtJQosDLYFNXZV7K-yW7gWlQJDyAPcjDzrvgbynr5puTJeEOswdOx95HIyAG-gQt5NnYMVpsR0_4mh7ErhtLykuuKwXx3TAkYwEMjD5Ibqqj3gNl6xu_XEwZRAxR1ejuNDqs0Zv-5JdWQfiOJnwIMZ1vdIZZveShWQvPYLD3o3Xxr-ek0lyTeIPu8V8k6RPnuovkUSitD1lsJ-FX3J3YiISwNMrxPIPyAKJ4WzFtsQhUYVILi4oMgZKN79EDlObDxxnVStjM9Lfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjv8QD2Zg4xDprjKDG7P_spXwR_lehNsDb3gNKqMZ9JuACOO9UhGjR5K1AfaSZbccUTZ0lYawq95c2HCptTHaCIdyzrgB3t7HgaA5E39Ch4GrebLmwKDUxMDqSXKdwUrizBk4Eunqsz2HW0oPdIbtQkMPtld6hCDwfoHAIDWzZEvaPhfCf2ivO_vO4aT5tPhEZkQ2te21fH2i1dWZbz6-VPQQK8ZaIoSPQ5LrlkQvf6vXbG1YDJDeoicBCsR2yf0i3_pR45XfmpW3iC-A36iQoDlVlhfj02kC28zjpuq9QZSPFDRznHeCgeSk8i4Gw7zf5xZmG7_5tdlBRe9g1GVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=vf6S62ZHyNCo0eTAobc-sJ13Y6gRyIERUqiRxs2YEjEvHT7CwTNflABdtCNE8PZ3AJnX3aRtjVkrKjQo_LGFDaBEQjUCI-EzYIfccbCXJL90qTzATHEn3xkZ0WFkDk6nwb_2JqOofzL4jHiDzvgXginwsXkcS3jqvjiEbcoLnoOeF9Agcs6mb-WFiSsTB4xSVIl2PX-grZ3UxUY9FAwj4k736hN-63AbcoLLtRBl75c44lTASKx7kE2oax8q8CGk2jg3M5L7ou1WuNdkho2D-LlKJ5FbcJVi8qS3gssnMHXK_N8esS9Ah9H6rDyJnUDJOAB5HkQkcLx2lj4FDJ9pMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=vf6S62ZHyNCo0eTAobc-sJ13Y6gRyIERUqiRxs2YEjEvHT7CwTNflABdtCNE8PZ3AJnX3aRtjVkrKjQo_LGFDaBEQjUCI-EzYIfccbCXJL90qTzATHEn3xkZ0WFkDk6nwb_2JqOofzL4jHiDzvgXginwsXkcS3jqvjiEbcoLnoOeF9Agcs6mb-WFiSsTB4xSVIl2PX-grZ3UxUY9FAwj4k736hN-63AbcoLLtRBl75c44lTASKx7kE2oax8q8CGk2jg3M5L7ou1WuNdkho2D-LlKJ5FbcJVi8qS3gssnMHXK_N8esS9Ah9H6rDyJnUDJOAB5HkQkcLx2lj4FDJ9pMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=B8MA6ZbUwCH841Na74n20xaT6_LIAA13_TkhgaxGIjeUIzwodfsNq40cP76EpJhLkCyMsVJkdFgGhK2v_ZbGm2xguc2LAKwkPPeRcMZFoWP1DU_lRn6XRxjonTNnwJXHlF3_ryDQJK607gScOFyP_pPkxBWUXfYlQKv0ty9Q_3ImVUxepmMDbD4UdWHr-Cu_dqvUB-f1trJmaspHQWVz8ogu9mxnwCwYW4BcIjxQnztpkKcG5_LW-Uo3tae-fcJwJgUSOgmo-mabF6DPvAU1Xdn3qwru_5NBp_pRSQbejqFBjrk0x0_pqZn8KmTwM1h6yjn01PhcBdeyfOKQ76P4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=B8MA6ZbUwCH841Na74n20xaT6_LIAA13_TkhgaxGIjeUIzwodfsNq40cP76EpJhLkCyMsVJkdFgGhK2v_ZbGm2xguc2LAKwkPPeRcMZFoWP1DU_lRn6XRxjonTNnwJXHlF3_ryDQJK607gScOFyP_pPkxBWUXfYlQKv0ty9Q_3ImVUxepmMDbD4UdWHr-Cu_dqvUB-f1trJmaspHQWVz8ogu9mxnwCwYW4BcIjxQnztpkKcG5_LW-Uo3tae-fcJwJgUSOgmo-mabF6DPvAU1Xdn3qwru_5NBp_pRSQbejqFBjrk0x0_pqZn8KmTwM1h6yjn01PhcBdeyfOKQ76P4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft1LXU7na8sVoiZWWbySpl0-wLJI0pr2xAp9uadi0YIgq5lq6MjJLk2vboDWIUcLj9YDE6JWATWnBkRE8ygYd-5-peSIOaw1limzj6A1SV8GkTzHpvvAO0m3ulakSsUfCFRtyw707HwjSxptUtYtEM25fpULTYfaNZMw-DjmytvlHGtIeWwpJICEkftRAkn-lhi19M8nzVO6W-0UkwlDcN2rq8iD0SjunnkpFxrBHMLoDidiDFoVFqUPC3KyYgX756Y6gYTrkPEFdLdjD4yxccGzcxTSiIJExvKq2AJuxa5lCrt5WJtHJJIVqffsltOg1ifZgUpGXA7KQkiNewx16w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuZ1HMPSUd_UcEGW6z8IGVuIb1xPrOLV7FsSjBCIEvqWDAxupXJ9xKkjh_Yl4rJYNs3mu47UqWsF4UwJ-nwQU9AGsM1d3rG_V8GKXtFZ_jhn-3hVmbGskXCPocIqK3renwTI-fxVAwyRCqh1xEcAvGpibjCQHgHPyjYOQYOGAvCXKOjPhjWIEuwB1QgDHs9dBdcndGgPy9cj62tdngH9huRlIAI7VOKmv9EBTSGrxYT61o9hRKMkfDR4OgNKhbrh9izpzo0UYYZQ2AFvC6DVyQUzJGZPHZjTDD7P9Clzw_qzB3mdvG1msx4BhyylRzJ1LvinW6avNnprFkcSYOeheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nP2VJiBfqvCUBCTdqW3EviBTGvXgcC5smsl-jMb13cBXiCLp7d_MG057qGH8IFZ_BG5ve67zlz6FE4JUPLXGzs8xOyWAnT0uZiAig3oxp3Z06cp7DrYXp3uIC8xkns6RLpe5pG_e2YaeuVCo2Xed_ukDDEM85h2hAxA3by_Dyeht9kruy_T1JzvBTC1SMxKX59kwSMVmCbhoueRnKmok62GvhzDizpnU1uDA-RieQ6dFsTKVDAbnXUVZqCRnkEa8UqvfpHI2mOA-s_z7G27UrkYkn3iWf5GrJfahC9YIR1l6zKz83jq_gxpsAzq8FO4G6SU-dpGcfIbi6E6T_JOXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=qIFJgQJaURJQ7GUZaNLhmZigJULzYCYBsjVy0dJGEvOu3r1aKzJ_0oNFqtCE1J1J43e9DQXKtaGooOPO-B35CTqQrS-ulZo_Kxey1PCOWwok29525Qjv_dwFxr_wg8QFJ8ArriInKKHfVCyhZ1N7a88HON7tlGI2-bV0lr4xZsXL6kp_u-CVreN33RJmSZsozP45L2uJhIzCfmUxxo5eFignoWKhL1M-zVszpfYfkV3yfrN9wTt1agBv6tJaKPjB15hv2JLBCeczpC3l79rfTegZwOq_t6N1cYre3IrF5xCdYGRbIeBoipoZkywvBfZF9Zh9begPbikMmP1ahEPXeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=qIFJgQJaURJQ7GUZaNLhmZigJULzYCYBsjVy0dJGEvOu3r1aKzJ_0oNFqtCE1J1J43e9DQXKtaGooOPO-B35CTqQrS-ulZo_Kxey1PCOWwok29525Qjv_dwFxr_wg8QFJ8ArriInKKHfVCyhZ1N7a88HON7tlGI2-bV0lr4xZsXL6kp_u-CVreN33RJmSZsozP45L2uJhIzCfmUxxo5eFignoWKhL1M-zVszpfYfkV3yfrN9wTt1agBv6tJaKPjB15hv2JLBCeczpC3l79rfTegZwOq_t6N1cYre3IrF5xCdYGRbIeBoipoZkywvBfZF9Zh9begPbikMmP1ahEPXeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCv83nXVVVO3mRCXAGzV-KL7KJO7zJMNbDniugFjZ1Jl9f-RU9cXhM3aUl9sP1y-JqjJpCcnF8BLEQsUqqAQn_E3Vw7-Chp7F_x9WXBCae69DdNuaezfRX9uHcApetWuRE90mgyq_b4WbuIFFqwIpvkeUEvbt5uUWpMuRXBaO5_L3UgYqL0rDQb9CzSX09DypU7eP7e1jkgPKokTkCthdWFG8F8QNhlPL_2u5a_ZRo0viFK4DTwwWMeVF4wX96CUpEpVw2rJuoxpcxPNQ7j9DLCYUbEV8iYmKljjp8On3ECaC1-HEBZCqaWKGBol5Zx91P7ZkrKcy_DdN7cIxjoi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M708bAOoCrS7bSjDkfXPGXPGapQPjAi0HrAxouaMTBNGV1n0tI0M5S941jUEZFYPx7kffmEBLHyHBLcHXHmTR6Vv_7S7ubpFDSM-Q3D3bq_96ynyJ8xPXcnmARWcRRIvVDZ5ojZYNOeyDg-CnTRkEMpt-fj5joDUdMJ_PdZxMXY8XtBqSx6ctETt1bI0V0r1vy8R7DYsLep1NiZmojRsWznKo3W1jYS7gpbpaLji8UFmu8Id6S7kExpaQ384NI6yQuiPi52BT9a6CX6yH4_GaVI52Y9s80SKJu0_UMZZeMNDQMjb8z4f8pac7dqcS0TUEaSfz3sOl3lqWjrcfoXDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVcz32y1u4Bsj7FfC-geAvevTr17SMzLWY7gVnH9-C2AQFxkkIEEDVG8KB9Nav0CKguZ9mVpU-MpcwcVPZsQuAAsud7UnwGrs1vWeEqTXk9gMxo8e9KtmOO8QiLLJyZ5x--99ysuX9lBZa-Q4bZDxfNMI-vDCJF4pSUJ0cjkNmwfaOppYScz86WWGarwG-ITdjZ_tMQk3Z48PhleuoytFs4ytGbyLIQi4OlVgSf9aX1JmvVYqYC6xgdM2UqJBYXNqklXu-hwxedShy499ExGRB0baeYN8OuDc6Y-oP4fKGu8h5_HgKDGCjl1Jrx472dWfYTEqL5qGSKE-aJ5-EtSwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMIJawfqS4t-rVjg6YfZGXUP6vEN-ZbDg7JfTxWJiF0y_GqwXnYLW_GIFlH2hIp1T8ZJiS75Lqlo-TIJ0oohO1thKr7VA4wTHHZkH9ynNpSnbQuJ7xmDjmqhceSCnev8-6hJ2puf9hYuQ9jGsNeheRyOZyh7Ove3c3GtJhV7fy2mW42pJ3LUB6Iuxfwf5P3pqFaPJndbD0vzUyIWJ7YE4jZ3CWvmq1Hya0t6DYtBYNfDfBAiOYiPXusnNzBwlWzUkzRXLN7-mv4FQuDoXyHa4-sIEVyva1wMSfhv_QTb_vo73YFbj-QQU87jbAWMSsB00Xc45FTgVfLnD08wn5lp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=vN1aq_XjXyK24npMfuGUPWbRomGgRC2VL1_djV2ixHOyD2Opi-aQsa3r7JZ8uVCtQWZYyColTegqd1__cERte4fJotT93pZf5SGD2J4eVPkSvlm3XM5CswCJLSHDu51ZRjuH2Qn3SXtuUEYPD2xBU7OO5B8lDX3N9xLys0t5JBrDcEn5GzxzIoIC9HhXo39pnp__uzIzdE5pccB2ahUGxl-MSjLTSUzYGLBGbtdW0kZqCP-AH-daVo22N8dzlspbvyc0LyLQFhb4pwwfil9CfzIz3RMRTrHLgjMYP_vF1BRtqtNd5xY4LYHRW6m5jXIW2mjhTgGuWqNKTo9AS8ybZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=vN1aq_XjXyK24npMfuGUPWbRomGgRC2VL1_djV2ixHOyD2Opi-aQsa3r7JZ8uVCtQWZYyColTegqd1__cERte4fJotT93pZf5SGD2J4eVPkSvlm3XM5CswCJLSHDu51ZRjuH2Qn3SXtuUEYPD2xBU7OO5B8lDX3N9xLys0t5JBrDcEn5GzxzIoIC9HhXo39pnp__uzIzdE5pccB2ahUGxl-MSjLTSUzYGLBGbtdW0kZqCP-AH-daVo22N8dzlspbvyc0LyLQFhb4pwwfil9CfzIz3RMRTrHLgjMYP_vF1BRtqtNd5xY4LYHRW6m5jXIW2mjhTgGuWqNKTo9AS8ybZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyR2rHoHCkRTIAaqj_g5lele2lW3xjIvxg4DdXZ25aGPNMDOvmZdX_8iH_xqiuIQzk9Izy7vNF0aEX_Vs_6Bq4a0C6-YKBLivGYNuzGGW-p9nWRHBctswTcqwd1KRwfmHUhkjtrvo4YO450NswtsOGqRmVtHv8pmHN073OFwqR1fk52tynqg9fGqcOpvFNJHyb3iOKExxu97zZnEFseH13ajX3QIBv9J_mWpmpTEeiOkDnEJkYkJx_9tGI6LKtQRkMTz8OWbcCKWtb-bZhKElwHnKxsyIikk0ibitmagyuR2b7i9MKvh_cf6XHot27tvLZjMB7np7HKfXTUMJ0v-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmG0AkSE_XSwTwlozK_rRH1NxIzOgzdRxDW8XtHOrjFWGXdmI61eYm3w_vukqwxnurk8AMDoLJkMqxwqKb7_9GAynudtcK2Wc8IPmvFm9yHNIRBFHD_HJC-HDNiZbPFtu1bRrIM04xDZL7gKgtwKukT5qR2ChWFo8tvW3dxtg1gI1IRoMexag-YgVts1D2X_47MoDWxReNCcTMu7vYuVXvL8A411VHEI52OqGpHw3V1MCKRl14D7b3kybdJoWZeJzX7a5IH33Ni9uMTWcV3mOstuud2-Ug22HbpUgQHPHj2YQWjR7QMijn_VYZPDA_EFZ8l1c7TMOWE4h8Xy8L1pOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYiMFgd-_J99N_3BXXbLROJ7PflN9M1hNXD1POt-2mIdvTh20RpvzUIz1hBbymnrtV11uWYtZwr4OhSaEMa_611MmaECUZyh86R4Zm_HMznoz5sSi3UoOkGLej_6WlAEDSUHzM48dhxQBo_Af9W_l_dq1GGpmzTt00TsjaLPuJsxBT3J6igJqMFti3PCG3F4m51G54auloaEk1bkBijunl4ScpoIlUNWJ5LKY4rHSBxFxcDwW_ZGwt86eSyXGZmbfx9RPrdXbMip5ARfikL94tZlAj4wa_T6vqysUrHk-uESnmgYffhaHZ9rcVd2Q5kDQAHvCJBNFyb9B4ooI9VUyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=L6k5KzOmD8iH0BBIG2UFuSxuR-5zGGO3AUUM1GwyttnhSagsiohSraNu7pZ3g4n_huXXtxHcR2gySh7oYUWt5lKAtn-WUZ44b_5BmUnv1iwhqvu8PclIFEa6_s8JUTY8-LMI5NJjy0iLmmrDYKvxt1sKWeBDswOGtYT2MhJsgqt_C2GdG2HpuxS46McJH3pwseMfyZgn22vot1HR_tSy8PTTDl25adntnfWnIWYx8twQ1HKjSRiO7PcPrfIhxjdH70v7pv9t3HeJCsqGcwlV95-GtDo28bYgsQ0O26GrvN6yGcDgkDh1FyAQuaq8PAmlr5LDmAuZjALPcTQp3xHfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=L6k5KzOmD8iH0BBIG2UFuSxuR-5zGGO3AUUM1GwyttnhSagsiohSraNu7pZ3g4n_huXXtxHcR2gySh7oYUWt5lKAtn-WUZ44b_5BmUnv1iwhqvu8PclIFEa6_s8JUTY8-LMI5NJjy0iLmmrDYKvxt1sKWeBDswOGtYT2MhJsgqt_C2GdG2HpuxS46McJH3pwseMfyZgn22vot1HR_tSy8PTTDl25adntnfWnIWYx8twQ1HKjSRiO7PcPrfIhxjdH70v7pv9t3HeJCsqGcwlV95-GtDo28bYgsQ0O26GrvN6yGcDgkDh1FyAQuaq8PAmlr5LDmAuZjALPcTQp3xHfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Q5RrOB2jjAWe-li0W9pTPAshoHXbawLsnSuQNG5pjhqRq4y85bpQFICSy3NYFVg2E-07dtMQpzp10tb-WRMr4qR4glomSofmQXOVTovcjD-DHwF1VbLXYDLGrC_XZa5_HXe3yWvNsrR6sASmRG9ioE888sljVpkJ2zjww01i4M84oBjCg1iB78JgofEsbZ129gARvmDcOLTso7bqKtuJi5cK-u44Cp9dvSQmg9Cd8SKVFMupwrK7fPLvIh7DRrhQ_sfI8pJZoYYkNANslYiw2FC95OiE9L931cRRLLQVRNMwMRY6B4uoYeowVUuxC2LP93LTkYpg82TyFNw-E3NeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Q5RrOB2jjAWe-li0W9pTPAshoHXbawLsnSuQNG5pjhqRq4y85bpQFICSy3NYFVg2E-07dtMQpzp10tb-WRMr4qR4glomSofmQXOVTovcjD-DHwF1VbLXYDLGrC_XZa5_HXe3yWvNsrR6sASmRG9ioE888sljVpkJ2zjww01i4M84oBjCg1iB78JgofEsbZ129gARvmDcOLTso7bqKtuJi5cK-u44Cp9dvSQmg9Cd8SKVFMupwrK7fPLvIh7DRrhQ_sfI8pJZoYYkNANslYiw2FC95OiE9L931cRRLLQVRNMwMRY6B4uoYeowVUuxC2LP93LTkYpg82TyFNw-E3NeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EmRRxmrg4_A41BEu8GZCwP08YFBBA1HvVMwNN_Y2e2mYefS6M0mo4nDoH6o7BNBOjWRwwwR0xqAsfDdkl6Y5yvBpfahp0FJjLEWQ42o4n9cVZbvBM3uDiZ02RnaIQ9tyFOqZVZ2uzYrF0NT8xfa42JUV1te4hRBQEjLv18d7rPWl9W4-ZPLkvWI5swfwr53zr_MxDw27rxVjFsckZT-A89YMdN9gcPRm6dTa7wj2A26lCi89so0HZ2imW4r90DMtoP3gYp_Q1qv7YWZj7Zse6XSsqHvRIFIavsEHic9fZCB43CKwzQV-awe5WTK-wWhPq2kNhqBoYY9RPMkFJuERfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EmRRxmrg4_A41BEu8GZCwP08YFBBA1HvVMwNN_Y2e2mYefS6M0mo4nDoH6o7BNBOjWRwwwR0xqAsfDdkl6Y5yvBpfahp0FJjLEWQ42o4n9cVZbvBM3uDiZ02RnaIQ9tyFOqZVZ2uzYrF0NT8xfa42JUV1te4hRBQEjLv18d7rPWl9W4-ZPLkvWI5swfwr53zr_MxDw27rxVjFsckZT-A89YMdN9gcPRm6dTa7wj2A26lCi89so0HZ2imW4r90DMtoP3gYp_Q1qv7YWZj7Zse6XSsqHvRIFIavsEHic9fZCB43CKwzQV-awe5WTK-wWhPq2kNhqBoYY9RPMkFJuERfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otjL-PWaPNbr8SdYe5Mb0xEBEa0-sZqYKn21FwSfKzskmlC0tarvqb2yHiXwOqQpFHCiwE0HFNVjz4_VNdC5HqfpUvRyxWZ4R3s5oeyTUDbuh0KEWbddv6rgS1qQzG0neYUzTt8LVdUukojaLS7I4vtTx5kD8dHeDgVrgiULCR8X_3TniKnQTLjIZxYQYo4ZO7JewRaBZ-tZ1oZRWq91mZ10Bew4Z4l8Ssyo0mOIoxg5yob_xUtPXTPiIj_zbpqA3xQGcGmwXvB0Z-MBf-3Ddq3krcVyeZQXecabGv4O9y6TtbGwnFZoGKrBfmpYeAkwc-jF9zBEUnIz10kqAswItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIsktCXOmNrW1cR5E4fZAcIVKRCOHUFAoFuuSQeCJM0OG3cp7_kQcgo9bbBTyGCFrzpRQVIgG5d0n01OGJx8fuEYTAjVgrEisiM_npVvJzuB-2gVFUIaAz4he97-qVu6WPddhWcR4iIM5LFUsbUSpTzw6gCrU432oXadgfYnNnahi9jzbHpcASdbS9wblffdXewQbNgdDxwpLaxOnYNQTECFMMGEc1PSe0HFuLGb_ENBhtIY9SOapt7oV0vd7WJYPQIS4rOAvJLLguCI7CaLyTlQwFEl1ynLqj_JQcgaeiF_HgPI3SP4W6_i8916Ow3ikwIq25Cis7vYGeU2Op1qwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cALgS4vWv7mRpfRrcy7gHg5flVQ6604-7J7Tbo-zP4MvVQcF0O4JaowFTdTG3KUGf-9nj62skQPdQDIULWGftC3vyBknmbMfrFv_MI2_wOGmj3da5o4ZX8WoDatfnrbAD6zuVXQfZjjlAFE1p_eZY6koath2D1kpgM8BWyF4CqVJweuMWgSK-ZgxEvZTX8CXXh3OmDUwmpAYnGywQRO8e3DHQmggRXM_PDuwsfIZhTJAEVHFCgd6SsqbHoYG---f59-xaRXBbgBjsCkPlfAvn5FKyVKD7YZoH3M0IqNbhMLTNLH5rtKNJy5WJoBWTcfW4WVTgj-HZFapGSf49Xa_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urXueEaUc344attL6J0zSWNTCpRogjOnZRT14_1ilKBGh4yMrE8AYclYx2tjNjHmTGjqwHf-K_Ob50gUQQ7QCF8a3TQJHHeURH4eMGwchDvJDSqugmP8wbkxrMLGPuEUaDOFQ-toa_-jrCHDJsEHdAXmL0ljP-_e8Mnf2tuvx6IYV1wNw4I2oUpo7df5A-oTHrzlLVmLHJyvcJAZD0IrdDo1VMZK6bq7Jjqz9oC3CkhBYexann3cYpQtCWvl7ZIgIrCiDgvJbTDwAkblKAAA2j4tebkB3a8fYUQtrbQGKzQ60rBBWGLqUDYhr31if_yqmToxKeLMeLISZZ9MoOpqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdwvTRpZEjb2yMnJ9aAi_LlcXm_hVQgYuv_QZt_9KlMNpgQGoSIHUlB0-Eyw_4wtTLJw1X7frqjECIEBwZ1KCeYMeYPX68JLCrT7MF0nEzzGp7G6o27M_hZlXFZ7_eFZGWQtN-UW9a4d9yOFq56gXrl9VY-NsTYVQzZS6EQbX70tzhp9MZOYVOU1JSJIaacyizm-cn_15HNTnvJVvnu6yA1ar9nB5LebAOSCDFXKYbpqTUnvCwtyCZEJXKczH987JLd-d7bPb5V2QA8t7JRLYjnsXg1G77t_jftAUhyhafFAaq5JlNvWTkDMOKCFjqrymTPm7mqRe88NLZ_Qn2StLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKxE0Z_BX6zBiTQC3wl2n7aAf_G7cw6JFmxg9qgGlN-52SdvEC_-Ya_s49QAtVEL1W8aGDJ2Iq-_LOIXNoZzR6_tdnRLEcnmf4vhnlDaQ9DI3gRwLwLb3dU0eb9HacBBgqs07lm00CyiW8jV_X72B88mThrBI8lg4cFqJu-PmO_tWAsXf3xvjNNGG66wLv7fBWFYQEWFEB5kXoCQPctwLburrpYvJyFEhyPpFT7u5cHPJ2FQA0DHX3sfdaVga5iFJE8DiWO5l5IraeU_c66Xv_DqpzQZzxarbrSZsFjyUgapMi0pQBuUc4bFhm4KyB8i6qy6pE7t_nBO3lHvuYnSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8gMQ6opnRWhNXCPz6kHiQLZomFXvEeSt-aIBwNu7AKkfaBXKOO9HVcoNcs1oJYhO0r0phEHnr3X_7nCoWfzrir2e35ITEvwkDl8BzriBSCF59d0ndRd45duYe-Ny5HV3jbQNIXzXe9nVH4Mhbwq_9O_eNfRD3T3ysY_KxWd6LBYspKjNYCLK2KOvGAvdeuSOHROm0Lx2A2S7XZnt4IltGUHl3BB1Nj3XmPNNok-eEJDjBpF1O7NXaWFo3K0j04FD77f6-kUgptWij5AV3FqcQayUaVYYRW5uy7Ep0AIumAN7P0SEiXELG0f7laW59Z9AngTPAWh6Q4SEdRwX2E0Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dabye2HcleJvi80AjEnsRFJtNIbLHLZpDPJUcc36inMxa_paaUjnqHdNteQQ0p6ewYKXlxeI0pj5l3m5yFVHN_AXM5ps6qy6g6yLI6lcKvtp6sSL1RJFjU31kOzHprQ3xWLVz_-i4mmPVVMUvl80DXbOhA9hAeKBSdXdRhDlDEuzmVpzXXMO1MSAg80w-24QQaofyoDtSrgtkk2PjfVamuWzdQUD3vYZAPmrL8yKRyTVlEeEKRWu3-xV-Lx4CV7oe7y0QOwUiAb51JFZzRj27tom1wjnuPXNPXy051tTW9iRcA0iTkuyehSXCNr7i-yMov2rXv8dIB1jOJJ7Y4IcTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQnJETyPChLQxc562gN3CqDfcIOTxnhRkV_wqHZIfdYx1v5ypcsIL0NLjjzHdeVmI1__kOZj6k4LlAYoXNem7k0B3dkn21Dd7EFZKv8vBxCneu3gTeyCA_zV_0A_kho4AzODBEN8cWE4FLlMhDp_IaPwO9A4wRcFG02PTCEkCzad7W9KEsAmhMNhL1TmhF6uLk0SxHxWMJb7w_wi7N-zooagWFrBpFWGCNhlhPX5Bg3YrfNjfXGN7qsupHd7knMKtKJRWuLbnxYPM5umGihlXFIE2_lFS-gf657BP4PU5nfyl0QZ3m5ZQVe8HQsXI917mVqECZFbJeF9vLZHZfFb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvMDt_saoWsAVba9uNlp7aUmfAXgee0vT8jya5ShhKI1znxwJGpE-tmno9hGLk6ysYh_0j144_MQW9wbaJPui7F-EFvIrPbnBfqsA1ehGamZ7J2msXbozfu4GFjwkNVYGff_dU5fKKy0_Po3RjJBd8wSozN8HK7Ny3YiAomNUldo_dNMtsAxtLFVM690zyzGOJFNQc3_qYlJFP_ZdypLlMYJnyVnjYvvt9PJs0V8LKvJPW4zGGvLK8N-Lv0GLcTavD-RnoGtXJdoBmMMuuTSdXVo9onGZjRuPlGxyrO9Y3_uT7INtOgHTI4y0ZEunjbXDXCy6Sks1AjtC7dEYC1idQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPgZt01-OZM5_Vmmfc_8hSipnM2fsuZAfLnOE46n0GInr-I40zAL_sbf3GyXV4wN6_vD0LuM57DXeG87ne3ZEbotgPwAnDx0l5AG1tEtzXo6UY7gXkYb--0m-dKk87cyabbJHj4RayAF937giFOcKTMV_Bucp6GifKLpkjvE77pKoOhfVfJwZlg_JC4a1JJV0qE0zjdC_YRS14fyUifvHcLXDAzhimqrozuvbKZFhlQnS_tnj9LVwri_qcYZeGyxTdvDK0EXCyTWJVvH6Bxpo6_fD9Xr0dZWNFQYFyuKZRs3lwsyh6y4SeUj5qo7ZZyM89arJmW0ytV-l6Zt825CiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srIORWIVcS6gAvIHlSW5hAC2xmFy1Sr3P_YIRnUK0PWpQEokaO4-31o9fN7a8oXQuqItCF5vYE8XTHOJsfZbC0knxyVjvYbGhpoa3LzqoVebBTsFAQQQoeL6HVCmwMAj0Rful4NSXwHcC9RD5Vh92QYlTpcFY6gmcs3nv7NI03q1Zev4Lk1PHOfIBwsZTlJCulY8C0bfXS0RMquJMaipyI1-J-q3icBlJe2o3d9TBaD2SJ8hXb4m5t52ANgMBwEqk7AehuKoizDVUR6Lu7g8IURgoPNt0kw6q_KLFk7GvGaZtKAZeDCUIsuUmYn-ABzP7caWiBrjBv0tv4OGfEMoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcQu8B0ovle301QSkXu8XuB3AwZ5RRoh7uTHGneGdqvDMT18nSVOk-vNpQRBReXYWah0raoFj60n15rEs2pv8GsKfN7DDvAVwGCam7jv1QLWpbO2TbZZIPx0yiVU3ZOeqpUY8gLahuiG5IXUH40wNU6mJDlewgbUfI4x7sJWSoGq0LCR4y5d7WR9lsA9K8yslzPMyHUJLIcy22JuegGYKOJp_Wc4aEs0CEg81Xkna4aSv6qsxJJA_nGSDnlTvxSWKvr74FCsOI_nOQCpEc1sqsWhlPHpmmDnfjlcKU2CLochdfKlSRY0qSA1UaQpWJtYTQfvxpAwhnY8We0LYV3-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAXzfhSR794GFroGuPXxsmmb2OHrTg6Of2pRQVEf6Nb_C5KAbkEyhUUNoHrJxte3AVe804p_iqHss-TEiF30O3k1_j70DPMOk9yvL7uJwKmslFU8s92VWbQAqHyc15HJ8qdpFCetRl7-ltS1KGyWdIrodpmK4Z5o-xj37kFdSL83gNi4IMMiDbz8eUTSyUY0hBAUSIFJy-f1icb_4POChiVbutjX9ABnohk5WWp0dyG_awhneQjG_ZpwD5ov_oUo3f63cWPF4Naznve8MSBnc45kQmvSNyGIFj6JHX-hawfNWhR6sa-ZPqcrnjVVkoQUlNbjevHRsa-pwClPn2NNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf3bFn8dT5RzfPRBRiBB-FTY2wLl4UCxiYZJKPOF0Q1dvgIjNBIn5G3fzpNDAsrNn5rMMThEQJWYycR6O6rozt424AR7xJEGC2rxSj-62mFBrI6DQjPmuo8aSBU6NK3k6Wqqi8qqbss2vzC9TOJTz6DVfVyLj-FuudVvXa19ks_ODdVcCl7xcjOGleJk_XQJkDkyikUOXL7TnKksVr_9RExJM-ifnZFjRKalhEz7NLjxwPCqIW6XO9oP7qc2L7kFt3614ZYdPIGYpebTiuO6THyMvsfN86_bViqys9_EEgCjfewt2Lc_9_OauKpgAoROmEOpAF-w5ENEvvGLXGIfHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=hbFFxgy1Fz9NhWe9Od2LtB8Cq6ydP8JAeqykfFF2roIimLFqEnpqZegJJdt_FC5eJxC_jZ6W_74-lFL6gDoHauuh9vSmgEBCCfRLUydApncWtzoyquzH78UNvtlujrJ5vFRnfrcmwa_-qexIkVGyDHeqOcERfPTa7-Gxpefl8kOp2aEFCemRBvpMGMV3LyXdj3EUKmsJ4tQ2HM9Pbtat5mD377gs6Dw4lMTsoAdvrH6HY3eytjvp9nc7UI0BrUgXDkH5gf-Mc_fUTyMX2QG1h3n1qyvDTcR9x0AhfEwhPGXDnIaCaV5aIlemvZ3lMq__OsVl9Vo6Hs253pIHstl77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=hbFFxgy1Fz9NhWe9Od2LtB8Cq6ydP8JAeqykfFF2roIimLFqEnpqZegJJdt_FC5eJxC_jZ6W_74-lFL6gDoHauuh9vSmgEBCCfRLUydApncWtzoyquzH78UNvtlujrJ5vFRnfrcmwa_-qexIkVGyDHeqOcERfPTa7-Gxpefl8kOp2aEFCemRBvpMGMV3LyXdj3EUKmsJ4tQ2HM9Pbtat5mD377gs6Dw4lMTsoAdvrH6HY3eytjvp9nc7UI0BrUgXDkH5gf-Mc_fUTyMX2QG1h3n1qyvDTcR9x0AhfEwhPGXDnIaCaV5aIlemvZ3lMq__OsVl9Vo6Hs253pIHstl77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPw-Om00DVOiSG_iSwSBUNtE2-1eNp29p098Hy3xTqb7QWZRYulzYXgg0f0JCSxcaYfy71UX3JUu9h0WBTEpk2zEUdPnwKgjNH9v77hYhRAbiss9EbyGP6ZAIQ671mfgtkLdz-VWe1-YZT8qCLFBx8Olm337ZczQRQYlkBA7mpJCQBov3-fuN0pYOZm1qcQ4Be-vFGBjQt8YBPHcW8d-S072u2Hs1YuDxBNKQsimFBkErPYlkJqlGbGdc_0c0T4TldPiKp1Jgv6yOJLc2b4ZTJ8xfsQTPZcUdSq26l7pDKfWlBxUe1TUOb3dCd9KU47BbuV7h9350sdTXr3E5CvYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=QY8WQNlBtorM2Su_ISemW2UGDkH_PYzWRnusDIjKTiYT1mr-e5bwSThPJIqY9RBvb7tR-GizYSW56WBsd0lRxTbLj_c-jYmvKf0QcA6JhXXweykACpsqm0ppBcwRkgwzfBTRwSlyZy43nry-dX5UfJr-Wd88kH7aES8G3Ef4Wgs4fY5zygZQi0lt7hsjkhOIf2nIqfeRenlW7-Ip8Okhnunqa5eN8gU-Zl_Q3Z_VOC2Jw1AKu0kGwco6YZJoWAeEnUH1LllF_d6ErU3onTP6j3pKcAMnQqdD46ThXGe8zvXapNKazJsKzjl31RUN5QaOov9xhrcFutl8iD8xBuaNFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=QY8WQNlBtorM2Su_ISemW2UGDkH_PYzWRnusDIjKTiYT1mr-e5bwSThPJIqY9RBvb7tR-GizYSW56WBsd0lRxTbLj_c-jYmvKf0QcA6JhXXweykACpsqm0ppBcwRkgwzfBTRwSlyZy43nry-dX5UfJr-Wd88kH7aES8G3Ef4Wgs4fY5zygZQi0lt7hsjkhOIf2nIqfeRenlW7-Ip8Okhnunqa5eN8gU-Zl_Q3Z_VOC2Jw1AKu0kGwco6YZJoWAeEnUH1LllF_d6ErU3onTP6j3pKcAMnQqdD46ThXGe8zvXapNKazJsKzjl31RUN5QaOov9xhrcFutl8iD8xBuaNFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=quGivnqWicDLCYvV_DkLzZywXL1Oqwf8_nd5W3miX10PPjQx0BwQXsTCKLRki8zY_WQjAUpvCEGFDQ6eb2zPgGLpN_jl2T9ieGAkpjwvAio4zdhXce2s7EM3miOCqVCvIP8VpowqrnVyQs2fZo54r4KYkcXayp5ld2CJw07KRaYYoCftc_1zywpDSx7A8Fcdr45AXxUQI0KtBGEAn_mWXNWaO6y6PVLHiq8ae1SNhTu4XJpG4JFBBCNhceKimEUaChWty7zeZ6gYp3EfCEJT3fxsQgOMpi79QkEd7WxZUSQ9h1FV2-5Y_wXV1Zj3_IqI31n5IO6hfacwQvv10xfYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=quGivnqWicDLCYvV_DkLzZywXL1Oqwf8_nd5W3miX10PPjQx0BwQXsTCKLRki8zY_WQjAUpvCEGFDQ6eb2zPgGLpN_jl2T9ieGAkpjwvAio4zdhXce2s7EM3miOCqVCvIP8VpowqrnVyQs2fZo54r4KYkcXayp5ld2CJw07KRaYYoCftc_1zywpDSx7A8Fcdr45AXxUQI0KtBGEAn_mWXNWaO6y6PVLHiq8ae1SNhTu4XJpG4JFBBCNhceKimEUaChWty7zeZ6gYp3EfCEJT3fxsQgOMpi79QkEd7WxZUSQ9h1FV2-5Y_wXV1Zj3_IqI31n5IO6hfacwQvv10xfYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/havsQd7fshx1MZO89iSX6xIodVZVVn4q17u7PxGDiFVnU7d7Tz6qNKWIcxhLG6AxE6jHxkxXVOsHRmhdlxFf_3k8EIfEqIelqd5_sxGKD5W0LNidYIwNdPvvd6iRsxjoRdpLMcFDYtxiVJth6e-Z1_DIyHdCadLNA2I4T50JzHVtAbaEuvAxFuuidzJ5QOv1goOHR_T6hG_qWo4gr7w1eKPMEMP9gPmcKhvMuHTcENxMXvbDu8m_j9l0whq9j_CYciMhfW6DRjPU15gMsarB7hK9Vza3zEAzLM-vZypicGE9bhJ1qkKUkm3d7CpWxxlIQod3lDjpY-uEdE8_YpXNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PQWEBB-0GeAgjxJzTV22fAvt5dgTp80bkTP_9OkOJAmTpFfNI7wOkfiNp_22h2wFsUHVVZFu3vGErqNSa5wfGavIIv7KYUoNXU9_64MxwSoXWjypuZ6AwBa5q1sSLfjSrQYINQfbQPUH3fz8He0z9dTXIA9woKsYMj5sRjNGwFY4SzXahzfxfVRmU10dZKzflr6yh-1SeMQhR-a3GsIAKBZW3jwVulRwa9uRAC7t6oujJPc8p3aoswuu0nAffISDdd4eI2C8OVh_cTvOdP813yRL2Da3OOdlET3sd1gkDeuaqg0yEBoFUOd0hpxmXpTpMblWBlsaU4JczpwGu_zMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PQWEBB-0GeAgjxJzTV22fAvt5dgTp80bkTP_9OkOJAmTpFfNI7wOkfiNp_22h2wFsUHVVZFu3vGErqNSa5wfGavIIv7KYUoNXU9_64MxwSoXWjypuZ6AwBa5q1sSLfjSrQYINQfbQPUH3fz8He0z9dTXIA9woKsYMj5sRjNGwFY4SzXahzfxfVRmU10dZKzflr6yh-1SeMQhR-a3GsIAKBZW3jwVulRwa9uRAC7t6oujJPc8p3aoswuu0nAffISDdd4eI2C8OVh_cTvOdP813yRL2Da3OOdlET3sd1gkDeuaqg0yEBoFUOd0hpxmXpTpMblWBlsaU4JczpwGu_zMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN8YVFp0QPqqejHFh_2jgXURnNvfZIdHxZ0CXqtxaivf4I-avpmzbKju4AN2lOq62VMaF8PjKvGZfvgLliryHSNPJX5IVj3WYTbRG8Ld-nKhi-EoYWjwLx50aWGkYL9WEwoBsF6094y2yre3R4dbtXFdxs_IxiOKOAVkonyblp8o5uyTSXu39xaEdIaSNnoABK4K5AoKcB2RaccOSWib-2GRq776FMjmnlPkZOVQaq72oyNoC_MKOsGtzNXTY0wVhM3waRlLrsnv1anmnGarAEc62asJjOYrtsiKU-K0DiQIC6mVVT4A7iF2DjqXjiLgix_vVyDYC08qeZr9PXlSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6-qDzKNY8Gq4744TOB56Ss_pTIY5nnLE58CBNd7Xg_IysEj3ReoW3I2n0sH2OWz2c7ag_KLHHQkQd3rBRAga9-CawH3KUGFLsU8sBW7VftQSAmfiy7be_EMUn_ytQj6JO5_EOSERugdnnn7qcFXcLM1G1JP1RfWsUveuK7ygzq__UDnEELay4eLtGnQ-D5Dfp_nvq59bftrysbdc_30vecN9wDY99X9vfajmiWzxJ7wSOksr0FDKT0ODVlBxt4OscCxz6Z-NrBqhP9Z4LQO4oDwJkGFWOG4byo1gEZbaIpIOXGvSU3GSmuvgNWCt4e4Mx676X345TedhXwSi-yU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8g_gL6S-TlYRQ-mLL5bctUya6_x5c5cA_vnMNhv3M0UhO89jCprOpeRA5ooUtsRbMJ-tQa1VB8HWRxmjy_mj_lu_muc8aNoVfrIg12yr9C8UeGg1gq0IcNNUkEPpAeV-wX6LPP7Q_134K7cslU8AJUgGyxCRCW9A4qh0W_zLSMbcUGcqgt4qlJYW7_4Ze27xZlPLwZfDXt1hYkpoyK8vGEX3iAk1_Mja267lh8LuYVEKhKAoHrdH5bTNzYdPCg_Cp-4gUa9Q-icvekK3Qj5TYdfSUFFK4ZLQXMymxiiFQ9ZMK5OtZcfuRRG_ANM0bbQuS9Rp8tpXOYHXBiqU_tWNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSUAPVQaigq4FuKOHw7fPHUMFndnXgVzXRAtOyc86CZE8ZSCpcOn0ddtHILz4k96Y5bmEJBv4chRisPAFjPu8Qb78-pq9h7mkhB7BZngSV9_4iO8CA3yjl_ZD0Z3CIVouemRBN3gqNwVvxHrm8Ez34f8yP-jHb_hkmetXy4_iAWRCEVk86J0lax-mPLixquCf8GtgWQn5JEvGzdAGvfxEkUC-_NevtdciECfiThP-fZzXp9M3g06AsLcqqtOkm_WUXkDXXpKxxML3HbKMSeezaxEN4QQdHzvSzVq2bQAmtBBuBHeB45BZmtKmJVzcS0S4sSBJXvjoZ5PnnxGlmKvNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=MFNiHtk0jLO5ad4YuHI6jtR6GWYsmQV_wEzbWVROvCry2ylFhknen0ug6w_GidQoZxJ2hMguNB1JMQM13hnt8Qo7UIv3u-XABf703MEAp-XFLh57LID5nu8oU9e3mOEVeMO0dMAFYq4u7xNX7MR18jxe7WXSq07pGLqq133bQudWcU_g3rOcLLSkUvNhXyoTFQgjNcWnd3gpeJrgfAS2IJnYCB0V999w4ouCefNQSXgQZ52JB_nTHuVjCW9jNRAkl7RkNEaHcn-RCudn8CB8dqyeZptt-ZsnsyqhqJ5b-vEiJtBYMR_x-ekYyhkgABpuuaJQeW-KDez9XpiCu9MiQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=MFNiHtk0jLO5ad4YuHI6jtR6GWYsmQV_wEzbWVROvCry2ylFhknen0ug6w_GidQoZxJ2hMguNB1JMQM13hnt8Qo7UIv3u-XABf703MEAp-XFLh57LID5nu8oU9e3mOEVeMO0dMAFYq4u7xNX7MR18jxe7WXSq07pGLqq133bQudWcU_g3rOcLLSkUvNhXyoTFQgjNcWnd3gpeJrgfAS2IJnYCB0V999w4ouCefNQSXgQZ52JB_nTHuVjCW9jNRAkl7RkNEaHcn-RCudn8CB8dqyeZptt-ZsnsyqhqJ5b-vEiJtBYMR_x-ekYyhkgABpuuaJQeW-KDez9XpiCu9MiQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=jbBDeifFTIiJpYI-aS5StWlhjHvSjBWjGqTN0O_qwRCAuWIYS4K17geF-bHSN-SVwQnsNZmd3FDp-V-VkJ0Y-NnEvmRS6TybqmCYDoGi3SDEO-ohB_51tLVROB82BdQWy5TvezdAj26nIV7U3PYQrWuTG3-IAH2I9wcuEnqmdTWmQR2g8gnH4iu34ASSP1POtaw83EgJFffOJkuCVn9_z1wtwfpYyCpUnz9co4_GZB8CT12CQXnBB-a_aWDKbIUkpdVPBl-tmKTMCXPGa5tVgejQfhhW5VJsDcOIjf32iZ1QyNK95EYS0y1NPcodkHHw31gEugyE_C8-ZLRBqgX08g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=jbBDeifFTIiJpYI-aS5StWlhjHvSjBWjGqTN0O_qwRCAuWIYS4K17geF-bHSN-SVwQnsNZmd3FDp-V-VkJ0Y-NnEvmRS6TybqmCYDoGi3SDEO-ohB_51tLVROB82BdQWy5TvezdAj26nIV7U3PYQrWuTG3-IAH2I9wcuEnqmdTWmQR2g8gnH4iu34ASSP1POtaw83EgJFffOJkuCVn9_z1wtwfpYyCpUnz9co4_GZB8CT12CQXnBB-a_aWDKbIUkpdVPBl-tmKTMCXPGa5tVgejQfhhW5VJsDcOIjf32iZ1QyNK95EYS0y1NPcodkHHw31gEugyE_C8-ZLRBqgX08g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Sp4RgvCeHPG-Kgbzn-aTsQ_zyl5YJ32viS9LaJmOnt5RQQVrHdEUGoOanMYj0vZ3mb2JcECy9DAqM0TiYxP-A_eNUkao6HNnegzA9l-3LNtxWrdAxHeRnOaEdurZgsjvosGGowp8PFT7567PNY-3i0ozwE098twNVPP9Ded_GBmCQx-e7mjER-ukLZKTRuLYCJu3cCvDI5k7hu9jARxjjnYhPeb0WtWvGcxTjkdFKe_c3wv5TtOtHVpm6ce6RVUnEiX-kSRgGgLChXu5UgF3fcTVjF4A2240vKnrzFoBVSGYYd6lzlXN0XQB5OMaYhR2svHPRlg20k8vEGixlKF1Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Sp4RgvCeHPG-Kgbzn-aTsQ_zyl5YJ32viS9LaJmOnt5RQQVrHdEUGoOanMYj0vZ3mb2JcECy9DAqM0TiYxP-A_eNUkao6HNnegzA9l-3LNtxWrdAxHeRnOaEdurZgsjvosGGowp8PFT7567PNY-3i0ozwE098twNVPP9Ded_GBmCQx-e7mjER-ukLZKTRuLYCJu3cCvDI5k7hu9jARxjjnYhPeb0WtWvGcxTjkdFKe_c3wv5TtOtHVpm6ce6RVUnEiX-kSRgGgLChXu5UgF3fcTVjF4A2240vKnrzFoBVSGYYd6lzlXN0XQB5OMaYhR2svHPRlg20k8vEGixlKF1Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=FA7y-jV2vYwwWy7ncAYGg9omFlbWd0SLDk3JHhayA_p1mJbKoU-xNwAvBu_E1Dg6V_p2iv6KOCbDmou6JnSjq88lvx-sY-TlMoi6e1OL_HaCkPAx646SiO41R5VBqBJAFC6Ou732Xgnycm8By-OOFHieuVuRUDotrEw2YXqSpf5_ONogI4mWgVlMXF4AB9WovVEZWuhXV1dikQNwtaEat2ALlYQ73bj08hY4yJiQteo5hdmGHIMZO1nIJKmsNbPEncfNjZ_dG9vwwLfNFu-cnyh8_tVe9DfUJxCDJd7u9jtwKNke4o2qh73fZydfrDTxMfnlTL_-cQhJi9uaPiVzN4Gj_-OyEsjUdj-eTE8pfHkXyEQE276Zd7CLPECK6KqekHzl0dZ64kERDR44zlHwHZJiMW_ztAiXZ1c62iB5555Lql7t-nRJ3QQfCcYfWqOGsmUmuMWwIN2Fup9OLqXRbObEa2fWpkTSTeqSBeLQ3JSEqSFavcbb_zhawatq8a3Wl5sGRzG7x_nJJgWIGvAw92FGgdd_GL3HSr3pbulCF4Yxn-FZOVM68gTCebQXQLeUcvTlz-jHa7oVxee8yoQAj_JYbeyiW9NjU5uAlq-MCCRz5266EXF9lauQEZPO8-vbaOoo8RQEC27vTIFURj3B9KuLrIBPPYDvaplhKV-z7rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=FA7y-jV2vYwwWy7ncAYGg9omFlbWd0SLDk3JHhayA_p1mJbKoU-xNwAvBu_E1Dg6V_p2iv6KOCbDmou6JnSjq88lvx-sY-TlMoi6e1OL_HaCkPAx646SiO41R5VBqBJAFC6Ou732Xgnycm8By-OOFHieuVuRUDotrEw2YXqSpf5_ONogI4mWgVlMXF4AB9WovVEZWuhXV1dikQNwtaEat2ALlYQ73bj08hY4yJiQteo5hdmGHIMZO1nIJKmsNbPEncfNjZ_dG9vwwLfNFu-cnyh8_tVe9DfUJxCDJd7u9jtwKNke4o2qh73fZydfrDTxMfnlTL_-cQhJi9uaPiVzN4Gj_-OyEsjUdj-eTE8pfHkXyEQE276Zd7CLPECK6KqekHzl0dZ64kERDR44zlHwHZJiMW_ztAiXZ1c62iB5555Lql7t-nRJ3QQfCcYfWqOGsmUmuMWwIN2Fup9OLqXRbObEa2fWpkTSTeqSBeLQ3JSEqSFavcbb_zhawatq8a3Wl5sGRzG7x_nJJgWIGvAw92FGgdd_GL3HSr3pbulCF4Yxn-FZOVM68gTCebQXQLeUcvTlz-jHa7oVxee8yoQAj_JYbeyiW9NjU5uAlq-MCCRz5266EXF9lauQEZPO8-vbaOoo8RQEC27vTIFURj3B9KuLrIBPPYDvaplhKV-z7rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BpbB2nUNm0WMW4LaAZNxJBpUi3lIEiwGZ2igRHeiHoLWhCt-eOHCx746aGF7PBhVzhnoDzIF4y5KsgPESWYRSsOhlvAX2EYLEh9_cTlXhLfTp8bXnxy7uYhhRSUZBun92PK46iRc-4sG9znfcEFej7OECjRj8p5TAo2NvbZCdd9QIidKnKth_DPINJ7Q06EUdP9CUIEcfdYN-RF4tHuvpY9I-b8CwWIb3_ppcwPWDMHEL8-ZWTZ11q61G7xDdmv6-rnKDxZGg95mHklxQ4YWJ-5L9g5jloqgHXxCPwhkCm3_65av5KUqVnfc-wQ50VYfSHzmpowbD2Z0InAuVQVaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BpbB2nUNm0WMW4LaAZNxJBpUi3lIEiwGZ2igRHeiHoLWhCt-eOHCx746aGF7PBhVzhnoDzIF4y5KsgPESWYRSsOhlvAX2EYLEh9_cTlXhLfTp8bXnxy7uYhhRSUZBun92PK46iRc-4sG9znfcEFej7OECjRj8p5TAo2NvbZCdd9QIidKnKth_DPINJ7Q06EUdP9CUIEcfdYN-RF4tHuvpY9I-b8CwWIb3_ppcwPWDMHEL8-ZWTZ11q61G7xDdmv6-rnKDxZGg95mHklxQ4YWJ-5L9g5jloqgHXxCPwhkCm3_65av5KUqVnfc-wQ50VYfSHzmpowbD2Z0InAuVQVaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=k7iTfPHeAs8Diam7lbFU_9QD8yLt_8FPDekL3MVXtIGpV3BCA_f5Rv21KzqC-UKLknH3HEI74yGzyNF59GB5ktv9za750PiL8jQDtGCUAzfqtWj0STiKU3w8yu46_-Fqyr9uczUg_TKc0A0FeBXjIkJJ2EDpjHBTlOKcTD3eaPwtyPjj1LLHN5lHNi2VSX3ULz0bMQFb9P0f2sw88JDKKtCs5jv2uxEIVisjBAQrFSMucWdXEaSkAaW0o-pvNlPWMqZD7Y-a95Wcm3QTULOiCssmd3fTEloai5M3C9tUudL5bywOrIjShpFyF0TurKKwVqhl3kNlOBe8IOnYMPM7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=k7iTfPHeAs8Diam7lbFU_9QD8yLt_8FPDekL3MVXtIGpV3BCA_f5Rv21KzqC-UKLknH3HEI74yGzyNF59GB5ktv9za750PiL8jQDtGCUAzfqtWj0STiKU3w8yu46_-Fqyr9uczUg_TKc0A0FeBXjIkJJ2EDpjHBTlOKcTD3eaPwtyPjj1LLHN5lHNi2VSX3ULz0bMQFb9P0f2sw88JDKKtCs5jv2uxEIVisjBAQrFSMucWdXEaSkAaW0o-pvNlPWMqZD7Y-a95Wcm3QTULOiCssmd3fTEloai5M3C9tUudL5bywOrIjShpFyF0TurKKwVqhl3kNlOBe8IOnYMPM7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dECVnGy3zdO6hjSPm2ZDfgV9Ahb70c-FdzTM69DVwzzzR4L5SM_8ox74iW1c-JHk_v09eg5_zBEfYlyWsbp_Z9iyp7chjGpycCt_crSUb38aCWa6wYsOwqlWialQt4lcUM8f6oSAfC9C4Gs8CuRvIjAua2N_LAYEkl1e1X6jyubZBannseYO7o5KxiX9IOWnp2r93JGKhEx1GQOjXbfuF1ma8sdYEHmruEUC-BOmAZh2j0wSwR3sca34uMh4iNM7VVcr7a_pAiVszh93krfXC9Ajqzp0skYEGbPUP9KHOkzvkTDj670wQCClVZImnnFSE9bniScZkctmpiUsdwxTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Zo-c7LHmzfQVndXDgIwvhsreoIbE5m7rsI2jZysdpT_amJHocI0tHMIlSraZbCUkkplhuO-YsaeQ2gz-uYmKkPkRTB-XRDkdnrv2jFps6NP_-AJxfnb9pH2XzacGnCCQMP_rPTVGE_plZsQZas3Mlq90sA6v30x8Ot1KraLgVHf7HO7NIyh-z1QTJMHIG1R-L3ln1ThfKO6WjmLal7ubFxr-MFmiSbeaTCv6qZFpPoU0NYlwkwSFoxU5zuTxS6dgRVe6oMB3hb_WX9dmdMikCKKppPnKz3lFcT3ykVYwrchdewcDdsJhNpjWd4-dc-T0jxDkBfJ-M7qBBGiBMxAXwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Zo-c7LHmzfQVndXDgIwvhsreoIbE5m7rsI2jZysdpT_amJHocI0tHMIlSraZbCUkkplhuO-YsaeQ2gz-uYmKkPkRTB-XRDkdnrv2jFps6NP_-AJxfnb9pH2XzacGnCCQMP_rPTVGE_plZsQZas3Mlq90sA6v30x8Ot1KraLgVHf7HO7NIyh-z1QTJMHIG1R-L3ln1ThfKO6WjmLal7ubFxr-MFmiSbeaTCv6qZFpPoU0NYlwkwSFoxU5zuTxS6dgRVe6oMB3hb_WX9dmdMikCKKppPnKz3lFcT3ykVYwrchdewcDdsJhNpjWd4-dc-T0jxDkBfJ-M7qBBGiBMxAXwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcotwBHXLQRouCgcAxH0Ru88uEmDJbA7b1E3_CwU_162kRnzGkfgOZMmRGlwpkat9f3kExEC8F_o72ujrq3xSryAV81VpwZYhrP82TOLq6hM9XVB0clwcdyWBMyi3gMUu1MsRxJNHMT_xypYWE2L1aIFtmSVBMLOSUVGB3JdZtVpjdM-YtT-GlFSiYce-w2c5iB0yIQUe9tl4qsbrWLAWQK9pZlFCaej7h0ArX_mFIhzsqNaueBQrdGeKHwXKmnaV8MoxLt2tl8fDhCB7-3r-RMWj-pDeQu_nXZWvqvut2YV8Qe1OVMig0Tz62E9CoHVqSxkVY816GsNQsm9MxI2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8Uh9ROkMOU0FxznucoP0Sz5zVav_dKaxMET7oMOZgCvyl8h0mwnwCJzbVbxLV7dFe_2GJKYtjNG-FSn17YMQCKobH-CkxExQchBgC1bwj_SxDX1D5_pDfylqo5Ani_lmd68UZrOmSW7xlt7IuxKDfwYUFMjIZn5h6rwuRY0NoPzkD5ZVJdNK5iXm0bA_uMTRUN0ggM2MGrqoSXB9ODC2Vs95Deo0B32mtKI38xkGmE0KuBgB0qA83ICR0CPdyNRLU6rB8RMNYvYR8ruXO_3wO8RfjVKTm8tZ_qv89bFlQ3BY2_mciY__FsSm8AVNUL8v_s2PPrygudbbPvjhrQhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=IkTVTQUmowbWUMVvK1jvfpXKR7YFlzV4p1resZDLmi1XpUmeoyKVAeq1SnNW2BASvWcRSn1-G5f_8Y-OGSc_xIQzixxCR9mRA7TIxwlwRwcUaOUcdlZM7kbKjFdpUYoqWuJ1ORZu1ORTdJi2OKCnRN5MHi6vd2K_-H9pM7PWn9eMC1nTX2crr4w_c_ua6Zo4dkpPPA84rQzLM8HeE4_JfHipM9srxes1pLQdmt4__el5RPpjRiMqYH538EorLNKRKEjn3xyGkijSJTXiP-9q4Rn1g2dqwaJKShy3z7PrUT44zjtCZ-JXsFNwQgvkA2ZAfnmA7FWrfEvkXfFznLTkFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=IkTVTQUmowbWUMVvK1jvfpXKR7YFlzV4p1resZDLmi1XpUmeoyKVAeq1SnNW2BASvWcRSn1-G5f_8Y-OGSc_xIQzixxCR9mRA7TIxwlwRwcUaOUcdlZM7kbKjFdpUYoqWuJ1ORZu1ORTdJi2OKCnRN5MHi6vd2K_-H9pM7PWn9eMC1nTX2crr4w_c_ua6Zo4dkpPPA84rQzLM8HeE4_JfHipM9srxes1pLQdmt4__el5RPpjRiMqYH538EorLNKRKEjn3xyGkijSJTXiP-9q4Rn1g2dqwaJKShy3z7PrUT44zjtCZ-JXsFNwQgvkA2ZAfnmA7FWrfEvkXfFznLTkFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=H9kwupqY_x9bBebDXJWU72fcR4Rwi7Ec0oAPYuEwUwS_9egQ-EdLjrJxOHYFlYgEUyZDN1UCgrmetFemVx4cfDhUkx80_ASpomKaUmSCuUN0gCEiFJcPOLbMbRj5rPiaGCgXXRyo-JjnREK_C2Ic_tIua_0IHCFqtQk0H3jzfBj7vj5KLURS1Qo55VV-nAZaJIwAgn_lOxfQRwZ0hQi5Y_aMxy52AYQ0EqnknVX2VqG32k9VShXj_sEhuribkGbp4uJs_byEcn19th3-FnTArFK2bfpInZcFrysEDaBHdWcEFUCaC4mNpw5HsGo7TTzKzLE9p2fhQFR2uAfVuquKKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=H9kwupqY_x9bBebDXJWU72fcR4Rwi7Ec0oAPYuEwUwS_9egQ-EdLjrJxOHYFlYgEUyZDN1UCgrmetFemVx4cfDhUkx80_ASpomKaUmSCuUN0gCEiFJcPOLbMbRj5rPiaGCgXXRyo-JjnREK_C2Ic_tIua_0IHCFqtQk0H3jzfBj7vj5KLURS1Qo55VV-nAZaJIwAgn_lOxfQRwZ0hQi5Y_aMxy52AYQ0EqnknVX2VqG32k9VShXj_sEhuribkGbp4uJs_byEcn19th3-FnTArFK2bfpInZcFrysEDaBHdWcEFUCaC4mNpw5HsGo7TTzKzLE9p2fhQFR2uAfVuquKKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=uB-UxtOCxvEt2KeXKUMDBTsId8dg4vk-wiXfvw8or-Vw7vLfJxHBkTybGY0Jk8FxYap931Daywns1mdi0mgv2JY81KRmVGO0-GIpYYrx_VGZV5gV5tT4TOU5axZXJCCGw2cWRtiDOlLy-Vz7pkRWnzuqkO3fMPAAgfe8ttWmlatDr4vJViKMCiiZTZnT6PSeG8FL7GMEMOebc6AkHfrZVPsqxfGAyLQZtxayNk6Gs-i6l5sLMa1QTi_Jm0zNOsMEDNI2vUWFb0HfQRoFgTiyxRKQx32U1GUpdCZCzhkzonUvYgznLS1pmxbWy-AN0hbq-30L8G9AJJKb7hRC93b8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=uB-UxtOCxvEt2KeXKUMDBTsId8dg4vk-wiXfvw8or-Vw7vLfJxHBkTybGY0Jk8FxYap931Daywns1mdi0mgv2JY81KRmVGO0-GIpYYrx_VGZV5gV5tT4TOU5axZXJCCGw2cWRtiDOlLy-Vz7pkRWnzuqkO3fMPAAgfe8ttWmlatDr4vJViKMCiiZTZnT6PSeG8FL7GMEMOebc6AkHfrZVPsqxfGAyLQZtxayNk6Gs-i6l5sLMa1QTi_Jm0zNOsMEDNI2vUWFb0HfQRoFgTiyxRKQx32U1GUpdCZCzhkzonUvYgznLS1pmxbWy-AN0hbq-30L8G9AJJKb7hRC93b8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVTOHhxE2IaO7NB905-dF39Ew81y9BebLiow2KbooiKMEYlB7ICZ8yBQxe8kJmW2bSw513VMuC8i2l_Dxz9oXmEthLKz3BlLLnjItTMVnjM4aH0OADsurPQ-sK625BwTU9MO759THbmkb8-mC2pPKYOzxUA3hgezO-oX49N_0X_-CNHyTAGDsBtePNEkkvuHpP6O1gPdB4AOBSYFx6k-lCEiCmM6v9VQ21tkWuI25d0CWrx3NdRxnCiYctaPZ7g4fwLHbKipkCAC-9dzJWz0TXBl3RWc5LdoSQY-RQrnAwWvu16KndTfuljQmPVe33S6-SbFje8n4JqMOOyZzbY8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=nTPd0QtifxkHdGxiO5y3rFsgcbMDEqJ1BlQvH66hqDpZTL0qDPmR7oX7r1ILflJv70NHr5j4HmT77_lpCsSiubfaOAKgxKSCtgQ0wt6j7qOqS_tIkjzdJIsorrDDTs7dEefMsSzvjbfqB6Z9xggkgaXskX-NgZI9-RBT5HJnzwbrwHpo7KbKYU0gUy7Ub_tHA6vcPpbU1SkUK1BBCBXBajm819DxtAucSgmxZTcQumPjiRQaF7wXF1AYgqGOXua4gJtufE8n46zk0yKEr-s1Pjar04bUVGFl5RrgawKdaxl5dOKe-vnRbPbxaY9xG_W--pg2NCap1YbuuYALVJF1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=nTPd0QtifxkHdGxiO5y3rFsgcbMDEqJ1BlQvH66hqDpZTL0qDPmR7oX7r1ILflJv70NHr5j4HmT77_lpCsSiubfaOAKgxKSCtgQ0wt6j7qOqS_tIkjzdJIsorrDDTs7dEefMsSzvjbfqB6Z9xggkgaXskX-NgZI9-RBT5HJnzwbrwHpo7KbKYU0gUy7Ub_tHA6vcPpbU1SkUK1BBCBXBajm819DxtAucSgmxZTcQumPjiRQaF7wXF1AYgqGOXua4gJtufE8n46zk0yKEr-s1Pjar04bUVGFl5RrgawKdaxl5dOKe-vnRbPbxaY9xG_W--pg2NCap1YbuuYALVJF1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=J1w-J4971hcaH_gDr4vqVFjCkkkRoiUE-bsruua27e3u2II3gRHyz2N-DWJIVPH2lUtEsNLco4CHHqbvlZxkhPUCCs6fB074ILXM9f7hwHRrx7HQl6EPXHSjZCfFlxrr0LrkS8D0tfAsN8uJfrSuBK912LaF32VbLsAeEMpLy3WRAZo4FWTv9aGuGkvA1XrRFhIowq2IbvDThsZ2ULwa8sB5Jzekfskix5mCNtNQbHUtiBNeXxqpVLBGPetC_WDQbLCglcOczLIuIHnDuqFSkcDTdtA9MVJyc9_FiG1ECUvanF5pUTdg36yCbNrEvFpzWT-CRYvtme1qa90MZg5dnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=J1w-J4971hcaH_gDr4vqVFjCkkkRoiUE-bsruua27e3u2II3gRHyz2N-DWJIVPH2lUtEsNLco4CHHqbvlZxkhPUCCs6fB074ILXM9f7hwHRrx7HQl6EPXHSjZCfFlxrr0LrkS8D0tfAsN8uJfrSuBK912LaF32VbLsAeEMpLy3WRAZo4FWTv9aGuGkvA1XrRFhIowq2IbvDThsZ2ULwa8sB5Jzekfskix5mCNtNQbHUtiBNeXxqpVLBGPetC_WDQbLCglcOczLIuIHnDuqFSkcDTdtA9MVJyc9_FiG1ECUvanF5pUTdg36yCbNrEvFpzWT-CRYvtme1qa90MZg5dnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=OSJ75CU-4UZEJVgAOcA6lP8ciSHJ0HGXgbuxhW9a2FfMM_onaSlciUYiSb0lgNxQQmc_b_oAk-Zqj1Yeg7gWiGaccc141t1BdJobXdsRLOptTEHiLXVWYYDnlNu17qIFzrBNdPzPEg9Jqy5LQtyN63f2YraVd1qrWbhAxJfz_eLM2i-5TSPmhq_HTHeJgymmsWMq_p76dXL_6nBWV6aDNzrGg3ooMMFBmzZBOOcjc4VnwV34o0b3fZzpsuxEwDBs0HM7IyC3x_Eb2fVrtR_uiKGiOzQcYVBJgZCc2f64EtYt8QQfoYPQ-alc7CGx5YpGN65b-vC3NXOA9tIyngh6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=OSJ75CU-4UZEJVgAOcA6lP8ciSHJ0HGXgbuxhW9a2FfMM_onaSlciUYiSb0lgNxQQmc_b_oAk-Zqj1Yeg7gWiGaccc141t1BdJobXdsRLOptTEHiLXVWYYDnlNu17qIFzrBNdPzPEg9Jqy5LQtyN63f2YraVd1qrWbhAxJfz_eLM2i-5TSPmhq_HTHeJgymmsWMq_p76dXL_6nBWV6aDNzrGg3ooMMFBmzZBOOcjc4VnwV34o0b3fZzpsuxEwDBs0HM7IyC3x_Eb2fVrtR_uiKGiOzQcYVBJgZCc2f64EtYt8QQfoYPQ-alc7CGx5YpGN65b-vC3NXOA9tIyngh6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFJtRWoozvu7-uTg6cqQvYiduD1EKJJPwpkjVksyCmcBLDcjeNa5HqZowlQ3y44AVp_dITbDLwUev8rWHP928R9iSvOYN4MlXuk9jGT9oIfmtAcdokKBZt19V_fLTbGQqrWYYDAeJr4oOHoO-wFVex5AxbJs0FL0iiKxrqDjUjGIIl-PQtyfdwFdv4FNxa-n3-fwLGVkLTf40iI5hQTZXblj2EbDO67gVbpOFgXnjpNPtztUkazFBoRbswRysdm1rdOEA2m2Zq1H2p38D6wWdWrTy0eVuvyKZUZWzpEl7W_g-Gb_BJ1_dJTMDpyt2VBwTNJAp3flCukYJxikH9pOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=Q2i4YWHCYgvy5C4P-U2HPgUub6JikqcZwtkKLxSdzPLowU70_ir9PJfgoy6WBZIerlTZORB7zlZiKYReegm9BR4LEV58fCrDzfVgjnD03VlKr0SQQN0sEybyoDjwmFdi_30DGU_WNIGzFWwV3zqgiD4uM2N8NBPwwaCnoIeN0gvEhLNbA1qW6jLVtzNIrB-4nYUgy3JnP37Wa4YuxchqtbkSknv7D1Cl3-e1NXDh0KbW5UNOjQtbLAQUHKz74f035l4lptZtM8ABM9-pspzAS-g1qhyeo20etGWJM3c_a4ZOKpZ9KzIXt8ftthfsfUsz35Th5qXPaJ9rcMw2dqXQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=Q2i4YWHCYgvy5C4P-U2HPgUub6JikqcZwtkKLxSdzPLowU70_ir9PJfgoy6WBZIerlTZORB7zlZiKYReegm9BR4LEV58fCrDzfVgjnD03VlKr0SQQN0sEybyoDjwmFdi_30DGU_WNIGzFWwV3zqgiD4uM2N8NBPwwaCnoIeN0gvEhLNbA1qW6jLVtzNIrB-4nYUgy3JnP37Wa4YuxchqtbkSknv7D1Cl3-e1NXDh0KbW5UNOjQtbLAQUHKz74f035l4lptZtM8ABM9-pspzAS-g1qhyeo20etGWJM3c_a4ZOKpZ9KzIXt8ftthfsfUsz35Th5qXPaJ9rcMw2dqXQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naKDRAPo4SBJ4SnzkD2EeKaYAdSRCX-ccavpkTifycLUZhKUpci-X1B4MvGKvr8GIlm7k13Vy0-cm9-A2hjtVa01Qbetfs-dTJjUhmgiuvZVAGy7kBVy2TjBUEikSfRywZ88Wac5dQKKl1Z7qN-Jt-y2pFXayTH9HOnP4Xu_4nPKDlBXnOCBE-HNvtN7Z5HhJDBG-L5A1eSAZhto0If8OyR2BsjGlHxPaXYXfvm66DWiw7_PF8JMsNWlOIyiY9G9CKLWtInhDclsRlU_QOzkQF4bMnOm-M4ocDYllQONQkxYAB-TE2DpiSugm949UDULbrqFi5HfRyUwu_AhmUiLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=fr6glssKPMDh7QBEp26OpjXFaDKVcuj3DhA0zLNZvHcDAfyY3tdBpokGOSd_RE1y-w_TUGoATnGCYZasHAdFP5GLG6yLJD2pfe8d5sM9U_bSZLlKOJ0GVu4Va3waKqI3P5BgW2FlZ0amnpZF8OmUmFTaB4UBGSKJTjk-SEdoWoAsOyF5uXAe1pPIvbnyHeMB6jJUqot1fDC-wxRaiNYQSQaPbmCTtFBAYzjNJb5Gg6XT1Xl1ycpk_n_Lq2v2MXpu9xefLS165pRMkoJgiMiTd11CqrGvrykU0e-pv-O_kyj1hHkSphSwMM_EP1Lun-6rAkAFMNMCmu6Mf53EIrJo8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=fr6glssKPMDh7QBEp26OpjXFaDKVcuj3DhA0zLNZvHcDAfyY3tdBpokGOSd_RE1y-w_TUGoATnGCYZasHAdFP5GLG6yLJD2pfe8d5sM9U_bSZLlKOJ0GVu4Va3waKqI3P5BgW2FlZ0amnpZF8OmUmFTaB4UBGSKJTjk-SEdoWoAsOyF5uXAe1pPIvbnyHeMB6jJUqot1fDC-wxRaiNYQSQaPbmCTtFBAYzjNJb5Gg6XT1Xl1ycpk_n_Lq2v2MXpu9xefLS165pRMkoJgiMiTd11CqrGvrykU0e-pv-O_kyj1hHkSphSwMM_EP1Lun-6rAkAFMNMCmu6Mf53EIrJo8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGAd7ZwWw3Pf0grmzEJwzUtV_1xofmOwoeFLGZJk8E9c-JSMGsaitnmRNa75XZkwgvPHoMlD3BBXsl6-esrqFfiRePO1aYe8BmXRkuwqimt-w7CZ2A3PwVimp0BaW99h1GPFRmr9Tsw4wb8MZB1Lfo2PCRqaSsmBw_AQMVrJMbbM0d21Ufl6dtDdjXOmVX4MWn5FxiU86wfO4DMOw7SFm6UWmzjlOmAWyDeDMurcI5Zzx11kutwtftSqUKQqnZdgaiXq2I722xkWrGo8IHy9D9EVMhUvlfHFvb9M4Lzt1rI3PAVvIFHQ2Nx2WJr93FsyNQ0Kksqdwj3iEZxNw8HcQQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
