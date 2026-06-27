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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 00:21:54</div>
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
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugjd5jhK7RwlB1CYo_zEBJAnSyxr5MlV98fRkjSbkZqRFC58zbY36cxBoaGXslVnTG2X5irBJ_Go1CMqwJR50U4_SugaiqaiQbA5gxIg-j9jMj71mDlFa-qm98upE036JCEQL1pScAPuyeaoTsaSCOOORlLfN19e0lNwaawImb-HiD1cgqmS3fBsck7SMRz4kHjZMqOsSmroj3SoZskBSvre5NfCsmwIGrw5pwowMcFnIgRJBZqBqLYLAFja6plo6eFPCsBUPgspZxwM0ZyDreDGDxKfX8dyQotht90hKy2c3FG0GrOqd5yVi2_qKM1akbyqmJOb3T3n0V2LsvNeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsRAIFDKmhhy0ZedggxlxEY-DMwX0QuvVTcNxnx3Dth7pK7eJ5LwAg7T5unqTqtpLQ6hHyd5BnK4FCDPlZejdzn75pufolTkzKZ0IXCG8TXtJe80ovxDfr0IMF18wEFegQp-SuDQD9oD5H9zG_Nz4GrCxz-y-NtF_U69qU10RzX5idADglAN1l4kW1b464gBVhyuDr8u_wAiB8POxbkWi1EJsKEdc-caABHIYPK-8E1doR0gjQoGocdmHTklflIIif2vBoZY-8Aemw8RLbaoVFEaJd9_13s5Q6x3CizELVTFeF-eJ-GsxMnC-wre7qLdl05N57ZuAjweR_39zG9hzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouXUZs797t0DdgtY9fNVebDsS90zlFlpLtcbd-8K01z8_SFsWqxrxbGTtEluR40dqJzKfmCA12fptWwtMnMEsYFM92YC3jZAru3SRi4FWemfMnIbbdFY3nkfkRuXT6lNSR5UuGm2nhn67NthvAJ4ygn4tEccwu9Z82agXU9WDH1aFQmQwLlzBr5_E6q0KvpdCbV_VoRqw5owA1i5t8iJX8mZwWkoKJkfZkJhC0qiV8KVdv0W394a__ecRLbsHsfxTxO42QRTyC8pIB_atIUJbf0euwyp79AN_B9w9XTboh29fj0aL37126dJWoxtHqHvG1aRXjRNk8VpSnmvmpke5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOnD9RXfVzQOThVR_SWMFd44PlLdUzrtFD8Is_DHjOKW22_hWgEuVIzAWg7QlkEHEYhpBunhS_oKudgBZI5oTc8qPZAD-MbndhOVoxIAOeCO09imcrGRMmOeJnWd8GyVv_PIXLab8Yxl1DcmO5ySDqMO0PXYkBVolQhKPYnQwdfNSOx-nlC-X43UF8KY493dg-_epWaI8AjAsNNMpW0yeSgPfUvYTifgYucBTwenDRlFgNdVtsm_VcuiTyNAmQ07WVrYe_D1iI6tSfuvaps7Qd40h60v5EXpTL6ImmYxlctvg6fTgJHJXYu-r3Nz1WSiz8YGCT9MqL6v52_GPjXidQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwx1UTY7CJ3ACiV3Zxn8RUpkmlVUgcrROHyhKiYR80MmNyMGSrGu_T-kokKs5o5CV3SNh0qEHYgLSqjdiXFEce5Y6JOJgq8JeVElh7q_HHSHjHojFM_Drr4MIrdM0_m6_ZiBR8SVK9vVBLCIji-tlIOy3y-o3JvJc2Ie8Kek3t95XSG65CqcMc0Fsb-jCGaHGbEfj1OZmYtjS9lnpoLQpE8z3-R3BNU1fAhw73KKT_9EyGkHsjr9Sqm-3ltiOXkDSIWJIpmJoHkrTWsciYPbM-GcoxbHFaCo7i-Hjz3XPPR9at2Y7d0ZV3eDC1rk5DbQLWan0g11yA0WVl3ct6Besg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaC_zylbIUJe43dqgc8PPpV34JXd7qTqOFhDN9gaOAhL47qvior7oQrDT9AfO3zzDr48fw1p3JvSjjc87e1-3-SsVwWat0SZc5BKmMi_yaL6EjYn5ZrVyvjzLfnpbphCngXHnna_AYbWnYLqOCpw_tuphKs5h4zz-ax5Nrx_UumVGvf_ICaxxGvGL5gyJavyZSSj7L42GlofTIm06e_LCgcCSnwIbxRot7pLFsN7KaNgXkYJ7Ch_G2F_Z50jFam4yyChfvftZI3EpzDq6rBsn9_emmWqAt9rlAoOh6UeV6sgeIiUNN7i4Xrr2obDwKeOPzj9kyWc5OkcL4_biJoF8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=uxIsBJ0mUc-dkm4-LXWam1K_fU4eVITg6Gx_IDj3mV0HI0S-w8Ej1qxQpfFrCtOQfwI8Ib2tKUvDbKYPhBjZDttuyBZo8uZUvPdqsAS8FbdNsUYHQ3PZNEdWJeMobpfjohU5GzyYcffohU5hI0Jrb_FMmKgb9AQDE8ycArZ2SVu-Ke6wTyn3sJqO4voWZcZExNN_JOxh15JTc8tjtI-wuaOYy47mXf7QxRAunQZ1FC906Q1cPjfmzSB03ENGHNgmeniNZrSLuQSy_bQ6kfNMRm1rsImk8A7bWskwWsy2olKvjjNHxrADrC4__8Sgq03j1P29ltF5nJDU561MpL9asQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=uxIsBJ0mUc-dkm4-LXWam1K_fU4eVITg6Gx_IDj3mV0HI0S-w8Ej1qxQpfFrCtOQfwI8Ib2tKUvDbKYPhBjZDttuyBZo8uZUvPdqsAS8FbdNsUYHQ3PZNEdWJeMobpfjohU5GzyYcffohU5hI0Jrb_FMmKgb9AQDE8ycArZ2SVu-Ke6wTyn3sJqO4voWZcZExNN_JOxh15JTc8tjtI-wuaOYy47mXf7QxRAunQZ1FC906Q1cPjfmzSB03ENGHNgmeniNZrSLuQSy_bQ6kfNMRm1rsImk8A7bWskwWsy2olKvjjNHxrADrC4__8Sgq03j1P29ltF5nJDU561MpL9asQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=LIcizbfW_5O7ZGIsF3x4KBX8k-3R7Okd-g5J9F1Bhld3E5o4zLk35-FiAA6BUFz-_XuXcMDF13m-eOgDj7R56K_p2q5Vhlkf03LUPr6ouPuUiwTZEdqL2QvNOOdpY6C6jYNTZEhL2nedMdFtZ0Svkq1fPBJVwSAyy2MHUvT1tw_Mw7bgDE0jnvbB2suTOHXj4ppWFTL8FVALHdeMCXajLwpGDL0gTTlg7rpvTCOAacN-RuJ-sj07c26jLhgCCkylMZQGod8iMS-2J_6pV7im9Z-k2nJbNH7qOuqTpKbBzqaBQZfo8QxY9FPVtN1d9CTjwhzMKKULeRPdep-FOnxvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=LIcizbfW_5O7ZGIsF3x4KBX8k-3R7Okd-g5J9F1Bhld3E5o4zLk35-FiAA6BUFz-_XuXcMDF13m-eOgDj7R56K_p2q5Vhlkf03LUPr6ouPuUiwTZEdqL2QvNOOdpY6C6jYNTZEhL2nedMdFtZ0Svkq1fPBJVwSAyy2MHUvT1tw_Mw7bgDE0jnvbB2suTOHXj4ppWFTL8FVALHdeMCXajLwpGDL0gTTlg7rpvTCOAacN-RuJ-sj07c26jLhgCCkylMZQGod8iMS-2J_6pV7im9Z-k2nJbNH7qOuqTpKbBzqaBQZfo8QxY9FPVtN1d9CTjwhzMKKULeRPdep-FOnxvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9PtNdKfDdo6aBV4fQxLe2iufaAsilQz1aDp66IdPjY4rwBKeN1U7kq_U2OaNmnf3RKRwdde6TTmjutAdCv3gJIXSsbhocaMc74ExGE68yojPwZtSeA4jEeT_2jqucaXIz_Op2zmJsx0l1JEoVzJz6kqX13ItbuVk1Wv0xP0w9vuRP6HOymOrEzXoe0BB9Fk80H7n807NXqFKZW3sd_kW00B8uou7T5d8U0QyaWlMKYO-QAXty4JK4rddSn0wJBgVitaqYpsHGsbec0vj2fyYsbfD9X1LsK5OWTsQa2FozwQJ7EkY4-Xso6Ohr92MaGsm4gfh8sYrabEFj9LlbVDFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hipjNfTqsIfBeV94T98rryBSOX-mpupsL-wFvQ_-gMlslG1RZkKXMjXvPnWvkkXzYD97UNCClWz_Z0BxaV1NFrE1LDOv3N9uqfErSrqmcO2MkRcVHLna7AL-ZM_vI6HjgHYMk7yH47af-RvT_e6S0XHqhzQQrgXmxNZw5eClUQTciSJnoeRBAjKZEa88VAMLd4nzHIgdNE7alPnFXaPnsOitkOU8b9uSn5pLAvpGShvTv-aZ_WLU1dgRQiZbLyxV_Jy-NVyh7_IDkpl9fCWHS5MZKlnmyS5a7nghDY40FxZ5uDIB5Fgb7KN9YCKi-zVlos67E7-UCgxFpvTVlM-mCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=av44g2UNFMt4KlWtB2bXTxT9t62IohfpjycGi6PzfVE3KvLtC9WNw7cWHQvFlw5LzYcTa522aH5rS0W4_LMm1OdpM_VN9jlJhrKJUHetTi7HsM4yj7BzOXwpQua-3KEZVRtkSxHpHY1-GCGwa3F67Xq8MDHcK3IFTfdsHZ_pWNvnScJIg6I3YycxUnbQI54InfndIQ7kcmcgvWdAozO-IgkzmvzQArtYDmGG33QyDB0UgpxSsMKj1di7wp448ZxEBzjEe6C3100D0LJN1xUePomkKWkEQoIV-vqSnLWEe0_TKLzFgJ5zaj7RotptKM7l24vu5THa9niKnvG3AKK51A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=av44g2UNFMt4KlWtB2bXTxT9t62IohfpjycGi6PzfVE3KvLtC9WNw7cWHQvFlw5LzYcTa522aH5rS0W4_LMm1OdpM_VN9jlJhrKJUHetTi7HsM4yj7BzOXwpQua-3KEZVRtkSxHpHY1-GCGwa3F67Xq8MDHcK3IFTfdsHZ_pWNvnScJIg6I3YycxUnbQI54InfndIQ7kcmcgvWdAozO-IgkzmvzQArtYDmGG33QyDB0UgpxSsMKj1di7wp448ZxEBzjEe6C3100D0LJN1xUePomkKWkEQoIV-vqSnLWEe0_TKLzFgJ5zaj7RotptKM7l24vu5THa9niKnvG3AKK51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=VBevi8TPZOvEOIDUnYy_772axDqPg9OnPkhlp6osTb1mR4T5Rf-VdYmbdZms_wnnCo4r5jB1E5Xe5CwKvq7nTzMAterrPq5QtI5MVoWuAc5fr8DncwfHfqEneIO7Clc4SeRvHpucQYQTzrshMblfp_z6XwLd_jsZCS51PAXMcTeAaRf5JaytTsCM7kLkXPpfNTvQ_CsoSGo8yceE-CKV9sbswKFrt89K88_FBSdFS-hi0sSpmehIb20m4I7hYvjFxsn85TgH1tv_vkBLZzkQkwUlU1BOkVvFBqZ0ax5APUxvdp4bWFAq3UjJ2TbBn_o6NLqHcm_An92W-eWtRzhENw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=VBevi8TPZOvEOIDUnYy_772axDqPg9OnPkhlp6osTb1mR4T5Rf-VdYmbdZms_wnnCo4r5jB1E5Xe5CwKvq7nTzMAterrPq5QtI5MVoWuAc5fr8DncwfHfqEneIO7Clc4SeRvHpucQYQTzrshMblfp_z6XwLd_jsZCS51PAXMcTeAaRf5JaytTsCM7kLkXPpfNTvQ_CsoSGo8yceE-CKV9sbswKFrt89K88_FBSdFS-hi0sSpmehIb20m4I7hYvjFxsn85TgH1tv_vkBLZzkQkwUlU1BOkVvFBqZ0ax5APUxvdp4bWFAq3UjJ2TbBn_o6NLqHcm_An92W-eWtRzhENw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn-P52tTjNsDW3jMY8r7pmue0JJB3X7jgAguBiizq0JiSYXQS74kI5w2jHxCPy11w6jMVdaXKaSS8GhfEo191eBp4uJFX23GXZcFyWXnALgVBatN-zNIpmSxYK70OKc0xjvEpT1S84OwkP4tW6dRBrFCQDfNJEoUeN1a67XBc68j2v0PMhNLLRRx66lGrlKv_OauF-phZ4XRXPdRoLFBzuD2poiFlyxGgJwc-VSYya7gUU6StRXEb2nowaM4gr0NMFOl8N5BmrgvzFFKLrtuaZZ80DMpI3WnZIQlYUoOLe-AMAhHJza6I5YgmH1UmESMMH4tlMcXwsvVhWvmujqv8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzCgmSyBdVSmLLu4gbR5cjN6evQaDMHMdBJGDI2MhZNfvjgQNprL9xKp588t2Djbejmj-yvFma9dNB71bZVaH6NlqqnMyDvhqkZ5Koa0kcDu8nCiN_OpblbELFrUbzMiAOmi44XHp7ttXNxEkdH1P7KOwpMr4tUBBl4ZcB6_M9KNaAMxsLLhigI4rxfi7PKWaGsIcWqXMBTn9XlGWcI8OITpro-ZnMb_5SRFVQSex2H9anm0Dk6xcjIzATjVIdD3z0W6Rl03MmrERbeZ_nkkUkCrxRPP4L4zJ3kLdRmabjzrnYre7-0AtmZDX-QUWODftDr7-hO4-LVdjsCIxLJYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WX0h2lkHKS-76V6H0Sm4C18GPyFJRI0sEDup6Dp0XlzubHLeQ4MwTJ8q3I3VNoRfSTXIKoAnTe8O5GJPqKGmPCm2ZS_cHuY2wttCRVKe0k81Q3CUVqAwo_weoTsvgw6G_aAFSDP3sZm87SCv92OnTldkm5hrPHzkL4unWPcpbfbrLRnWHrhngkObN1rB5s_R570_rpNb-8DDwZ9d8O4txCB2z7KZiOzF9b-lh6AfyKJPXKpqHMc_9Vu7D32Eg4UyTN8H1ZSilUrxD3dZsETlfpvKhEVdIPi-J_bqeCHNuyE7X4YryCH0_m6GCRf02jUn7I2HBNqFsxNzLHWaJyDgEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=BCAYEX382Jbik8EEiQJ5LqTE8rbPYLTY0bN-iRB-5vR-KnpTS27z7EozdqXaz2M_JBHMfj9MYwmYBsnRLRee_yZKCSkvNy0Bxpu47bmhrU4vSV0QFW-9QzEyk673HpTv3BBb1mva5WIzpIJ_tsUiOZE0SdZpGI4kVEEasZCSuHXKAPMhVNrV8pxPPXv2oostjikOvYYrJkMctw0S8Xon0H3cu9z1WpmO-TkKhvMPyivkCKFqTJZJOkCJ5LF5_zqLBLa_kKD0lWDlCSRjHTpkOFm39A57sQm32bkjH_7wlUFosb7Q6nHSHXgAiE42DGnXwpEcPLuE-P8yu6xMoetspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=BCAYEX382Jbik8EEiQJ5LqTE8rbPYLTY0bN-iRB-5vR-KnpTS27z7EozdqXaz2M_JBHMfj9MYwmYBsnRLRee_yZKCSkvNy0Bxpu47bmhrU4vSV0QFW-9QzEyk673HpTv3BBb1mva5WIzpIJ_tsUiOZE0SdZpGI4kVEEasZCSuHXKAPMhVNrV8pxPPXv2oostjikOvYYrJkMctw0S8Xon0H3cu9z1WpmO-TkKhvMPyivkCKFqTJZJOkCJ5LF5_zqLBLa_kKD0lWDlCSRjHTpkOFm39A57sQm32bkjH_7wlUFosb7Q6nHSHXgAiE42DGnXwpEcPLuE-P8yu6xMoetspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRPui2_82yNYZ1_tHOAseWc0ds2o7NazLzhs8WWAEWifd8spOV8lAc7ptC1p2zs8zqK6NHFOtc9WPXcTIRs8ZOd8_zhdjxEZchomeB3fDllJN6O3tmmGTVM0NjwhRCYq7_V44q1JpEimZehoYTgY02GJdmVQq0GDKUopfXD61nA_OT03LgyWn3MSbQagkPo948ZoEBbeFPG3Ey6o5DblkXdIwIhd1FWrFuc5fcHoYdYTe0Gsy6d00v15GP2sYWD0A67jb3oiE91Cy4WL0RrrGVQa7l9VQJfrykoPVn5m_wA-Kfx1ucFp_D85B_ffjAfcDYNzjj0dm6_9l5xT4po__A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwzWl49YzjLNzku3UlJLbX6cErMLdJ5ZK5qkLMdvZasqE4f2LCAW75nGSwtTLqMXRT6gNfAgXQ4ItzEseWktddJ1f6roIzeW_Vf1JACftEeO3MTf47KBpZgqUxrwSMKVeor8O55rymE3UEsVusklw21T40c9xg51t1ecB_P6B2gqjm7LjXWccuyhmGARyL6d4qMwo5B4TSrRtoOtl17wnoubUIWkjn-iNK3l8-gYjjNmvulpcz8paY2b9T1nsCoAxD5Jh989rwXNculz7kEgaGU2kLVnhMscYX_DLR5Hck5CwuRKyncEHygnJJ6bUxhLJb77lXMl9uPVkKYp7qrS4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXBp3gMFsLk7UaYI9wklxLrSLr_Qg-8y-uE2_9oQX6uL8R-1Vw8Vc3S-vo0Uk30CzntxI9Cfku_OS9Nuwtfv84DUDp9uaYz3e_U575IoUFhq94Yh05kNZTgDtzMCBmRroSJPIwckT95N-1YLDd9bAJhLQ7UW7mHZGQXdm3QQMaaT0BdRLYoZtGQsSadp5FEAi1swRz1liKHsyQpNoUCZEjGR1GgqZzK8glMNaAdl0rYi7XjkxAPZ1HAyuQDs2dqlFVqiMqUrsqOqt9-JLtJ6r3FHiI9AEuT2ROlpVp3FZOFoNFUIDrkbIiCyUObWGCC0FwGbPB6NYHt9ouYoB99nKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Bqeqn9PhbFTY14tLxU6z5be9TsPzi-vNIkASZN53FSJK8MdnDZBa-cj-hu3ZpBThZvlywxJcTqKsVwitP434VyD0oAFFcBxbL3q7oFunAKml0Z_o8q5jXyDpHbBQiXOMg7PcRqUjr4WwTeVCsKJv5_7xy176D9CRXE1p8EdEOTXZXoepIWHriMZJkpZMjKha_pvHQxBKU2cZjPf8ixvA_1SdVFm-imoLxj9ehZIQ3ubeYBUvxsgar1e1W6KSFaTeAkc_VqM9LDG_O8zyk_VfS8vtthqUsSPaD7VSTi9ciQLZZn7_e3of5_V4qCu-90FaL5p-9N_aVaBdanSc6q9sXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Bqeqn9PhbFTY14tLxU6z5be9TsPzi-vNIkASZN53FSJK8MdnDZBa-cj-hu3ZpBThZvlywxJcTqKsVwitP434VyD0oAFFcBxbL3q7oFunAKml0Z_o8q5jXyDpHbBQiXOMg7PcRqUjr4WwTeVCsKJv5_7xy176D9CRXE1p8EdEOTXZXoepIWHriMZJkpZMjKha_pvHQxBKU2cZjPf8ixvA_1SdVFm-imoLxj9ehZIQ3ubeYBUvxsgar1e1W6KSFaTeAkc_VqM9LDG_O8zyk_VfS8vtthqUsSPaD7VSTi9ciQLZZn7_e3of5_V4qCu-90FaL5p-9N_aVaBdanSc6q9sXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4648mauTAwKSwnemJXKO4vCecBqe3yucNlQMVeZRCSqAZERTAzcQUqAt_LTnGKVfDJkQRUs7ovTerFVa8kPA7G7ai-XY0XQqjMixpqIRywF3pj20mBL609lAXPtQO0ZHnZSeIyYPCfG1JrAobbOHE12ddOO8n3CV9o8jlybzf5QGGhnSuFaJe9LQ5YgMDFhSWTg6j3mX-BPEEvnXEVJJNn3ktWA-mzSCaOXR1_4J_sfFv2MA5VxDEWFLsCrEnJ1Tc_HFkd2qSUiRvmbXEO80Nh4nUPmOJHPzPKRxOIUO7p7g4F9yXmj270FxC319HAj8_1RPHbJBV-kRm5yXxEQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTj45vcWIHPQlmCzOxSpCApS5au50AUnLBzlrnNlHbopBpE-jE_O9yTDbE58L9b6CuUk-MQnmRFrFrLuPbaBEmgUTzDGwegpRzfyqYlni363ZubMxOdwD92k7msp1hs6zolNIDeaYfa5pdQqqRUsNLIQl5s_xGNmvxg6chr32FFQjJIKGavLcHbHOvY9Q2DQ5strWcbslxAFyLmaObKUXFsC76DEF01LO497Zp_5KWZQpUqMfcN4h4fjL5o6af5ZuxGW1gyCQ9wiKUo6hZGsTaiewn523zS9eeQSxDiMcbMZbLkTlBs7jULn2V5uM5IjRS7Jez5vq2E959Bydzl8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfTHwtFVXqnzF84voHr0g-eY9Uwa38Q74DnBUxfzwpPoAFlamCAaFKdHqaatuHEh4Tza2cvSPnMHSazPJnsbXnXQCUtH5Af2wPcjiTQ0wbaojrCPYSZUVnYme_6NylZCU4SqZK9-kKvoYfociUcZoZqTKSy7d9d-iiexHnZnpz1SIDSwQjBv_RicDR7B4bQCAO9GeNId_1FzCURnmngtcZARNYKhZPnXs7jfG0UiB6p7yxiA_kkIf7xPpxhh_N7flo-UoE4lQ71qCKUpcxu54yV7aQIps7plKthtQxYC6kvsaafovWwX9fL6SS5rBDPktn6AZmm6WCmzhHOvE8MyIg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=HsFn9E4JceCWovgOfi9XLrk0PjAc8GmJIHhKYjqIXTCq5J467DJZNjESmfU54CIuDT1pkhWdnETvWZgxeIbzDy7Yg9E-jD3UsgsvX8dxqgzOiNnPUiJsCfduYr8TmUsGdoRf5XafrZOacIqLDVyN95lm_YvEJRFBJAHU64awnywl1Xsb5oUrox9zcLRSwlxWRbfqL86tpo1QFF5pYAzLlzxrP5VTNLfPtvUgmZPN0iKcnplWYvlQfgszjbZNk4tN9ZK90oULTIHlG607t7SYkIgQUkm8YkgReJTx4Qw5HyLSbpC1Cnx-HnPvgolhzsIBQQtr-HAsTzcIFqGscNqObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=HsFn9E4JceCWovgOfi9XLrk0PjAc8GmJIHhKYjqIXTCq5J467DJZNjESmfU54CIuDT1pkhWdnETvWZgxeIbzDy7Yg9E-jD3UsgsvX8dxqgzOiNnPUiJsCfduYr8TmUsGdoRf5XafrZOacIqLDVyN95lm_YvEJRFBJAHU64awnywl1Xsb5oUrox9zcLRSwlxWRbfqL86tpo1QFF5pYAzLlzxrP5VTNLfPtvUgmZPN0iKcnplWYvlQfgszjbZNk4tN9ZK90oULTIHlG607t7SYkIgQUkm8YkgReJTx4Qw5HyLSbpC1Cnx-HnPvgolhzsIBQQtr-HAsTzcIFqGscNqObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESif5Htrz0Mx-r9ROOT5939z53oyLq4OzUWk7GFvHnvBXHsY9Fe3TTrKnl49YjTJopQfMrEJA4Yjlq5NZsVB4L3j6G4uHU0JmgMOtWLGgNwU1CGre_HSivqMdRUsTXHF3cudJN-GuowbaW34LmUcKbBKRFX-YJTET5vMwG-vYIdcRJhbyJ2zwEKD7SGo_c4z44SYPC2G79pJOYWEjG30NLuAy_9W0-fSqn6py_EDc2xClu2L7wobaIoCqiHKHA1XmWqrtgEuzn-e_ZmD4yer7kR37gcfNSHesBp72erJaz4B_Ep5vHHqRpRQsQ1DNuVdjbMfz6QoALsX2eQiZN0QmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC3e1ItN8C1rclYxOxHaCnB5BpB6z7rvBMAUtbL4Gz-ylX4XMkfrumpJ8A2WFDFBecR_5Ztm-asNvq9t0pu4MowNxHlG_O2UawatU518QP9SgZOcKZ0Yky5PSNVw-KrMnM3yqkHCpfBPzb8zjxtHgn1pCOzio8idZG-RSLHF3tUMYBERAtXbveu8pXXpp9rc5v9eVlWLn322Jx16fLppGtn0NGWI0XeirxFVV7ZUPfau9v3zNq5EofanG3NfKencuyk4VHhzY6jYk72HFJDoTPSj0qAKydp0UeFFMy0zgyO4KcO4LjmSQJzyKK2GoJOCyUxbb8EBMUl4gw7fwFaRyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djSvNPRVKxrQHTOIB71jEr0ZqxQSit7WGf19NyX0K5AViR5Ro0fNUbN07kpIx1YG5SZt6IqMOMqtK_GiDyJk7732GlonxZCvojP918loLohtKSb9PLDnNYOLWLYKsspG-zWD4Ih9RFiIphVodH9DS4009oDuT0y0u0AE6WJhVTqwyRkvFc5juo92Kw7mYbC0z3whPgN2XP8it5G92hLQ447PtSiRQtvTjDBxc4nWyGkVXSAjSOH00J2I0T6Ujt_GKydkxoF1_IcQaCLvST9CqcWtgdOdn3qRgLFvOtYT1i6ewjrq0QMJYaCVKJDw9RxF-MWiI7bxVch4Km4PkhzlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoAeW09clqcbKw-YGlrt3CGMZe5EYpDN5U15swSD1PJWdBOr_iYhCWVZdBYYHw4tHPXnxCcJsARayrTHVdwtIk0NtxneClztwV_Nl8wXcVizBhvgNBm_P73hVv9Bn1aeGLTKfKpWBOWMCHSSLnvuMIe30E6EqOIzCq1suD2K2rPES-HVYJrecRT74InrvBVzTJnFw32cPOk9SqVW9NeXNGXXPiu6aYmSJWL_CI9aebGnT2XliHco5_Vb0mbu0iZAqhMzN25KiB_cA3YBytJldlt_Av3Ogb2GiwQm8rsGdQKkKoTREGGHuTf3Db2Pj4CUtprHLctcpE47HQG7oILDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpXmpomrCdW-77y0Y306viuezd71bH1VVGmAdSR_GlsdOVE7rVwVdTFDqPqMOkz8XnL87ZeAmSvqr6RU8QaWbPIX3qdQGjUlLyQJOX6sBC8u6VA6oup57SpNKGmiGLgYxUSEpW_tIeOHK3NNMLkzc9UfEcj27M5N7mSsHw-h0Arqjq3AWsNrPq0c9A5oy1erpgYDZf7m1LyIHDhFiFFrvdJFVptnP5bmchE2uaCQVqS33i7ANp_ydzgjrRhy9OMu2eRVWma89LipTprj2xcPbntYq7cMHJ1o0jf4lzvk89K8l11un-Lv9oEK0NLISgG3p9C9fXd_AiBryPl7kelrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNZB0ur9XG1WodP9u66eRr2UyCOFRoNCnezIkHNYjSc-0bbGQFDdvZYQjjJMXrta1iNcI9oMp-6i0Fl2wCvfEUCH50VMNrjI7wyNU0d-IPTb5iU7ic0UmHZwW_MzlDhj0Q_MKdvjiw7J2fyJQc-FanGQJQ2RY2ira8ih61wkCguNX5oM4g4bHfcSL01i5JtCwhxt6aMYBk76DXTrGorveDQUen7tkWl9Fm_dJErKvVg_W6sGiujrQBA_KsDH1TX0dkQv4-LVeVUrSWB2PvB__tluVcypknnox3VoD9-becHpQ56F0NxQ0OUYoJ2fYcbmFURrWiBEt48YJgSBioXn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB6QqbSmijuj4kXb6cDUJLrZ7nLn5hBEHaFqk9Yv3e9SpT1raGRtvPk6MOngpiz3v7mYZBvYeVHJBCeARjWonGP0lrP7FXP7ipWG9ihPx5rqjV_hjahfqiHbkixMHSCmgnoAiL-3NzuxsVjDzhJx4qwBrBMIOrK3HFAa2xP0Tkx2c-qaojJe3dMsRkbgJgVvl5EWRoDdh1sW1CQYfwDamjmDMxMYRGZlQEAHrJ0M34TsOsb8ZCC4-qqHC6hjOa0eSAEgApW3XcWVS_haXOMIXaJcgFxDmRk8pfccqSoZVDGZhKBmivKRQmnCsaCdkapTpk86VnzBPS6zSK_5Sj0q6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJRJ9mJzs1gVe6soGBPDptCNzdpns6I_m0v9r28dM-EN7g_dcfEuwTcqpM2_5W04DLE6T0DbhOKUxJZ5PpUX-3HjoVw_NcIj6xT7Fo3JdLZtuCN0vJFbl8dYtCsCQxenqkSV_Wp1wCweFcNRF85Jly4EqdN_qHAj5zMEu3-dsmzLLxYU_FQVfvfFOjlThaBzqwp0X9bBOsk2QI4B5qFPsY-ydrcvSq0f0B2p31jFRYYxiqHsLWHZhm4uncXWGCUaq42jK6Qwdk9kx6aH1UdfXs9E9olynQmSkDiwXD50fDxB0ioJKKOt-_k-2EwHM4vpa6cQkE-WTCaDhwDXupZCiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiNz_JDIOzVFLhF--DrPgge5LNy7HnbAoqufPTqj5hJ354QM0I1B2pu8i-aZx7LjD8APMAoXuALN6GlMgLygKTHuC6VW9WEh64XmSMdHvG56v7U1uXzwcFD_uhNBK1vfKj8lYFdSFSjxV2stQK151LC1p-BdtMbeIFGPESIx9xOdExjkijXCoeQcoWvLLdA7Jc_yYyO7OreBg9mVT2y8qxnfGm9viVH68BwPil92f-fVi4vuW3RTY9duu_GapiztaXR8hTLA7IdVIDWcBzOtO9bxMv1pVPeGkYPgBvAGcSvbTfAXnIxNgF9Cu_qulG63ZVWPE7SiX6SQWbZbo9hAFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9MqoulIJ6gKPQPQSXS-JS3BJ2t6NRxefNLURS_EoIjKf_G5HwC5W5DvISIjy3rZBnIm806C2mDXmAF8GO0RixoZcoSyAyb3EWhmOVLr7W3g8GXoosX02KralWQMG9BIOPZdul-NcnAn9EPQ1MGuFa4Y5dl2V1vWOaybyxe5YeEbPQcMu0_FgtxJ4mL-Sr_ocCekUqZFdnfzifdfgcOniyPQvJFNWGRnEZ2Uc_h6LwqrQtzTTyissyjg7BeLEq9K5AM8ofB3fcmQ-yrTiguSHYYNbw7NIvJ9oeB3U85KttZCv1WXBVa97w1ljpWf6Zh1uiRttEBSKrNXuVdR_RZndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFK6fBFkMnKDQXcW6PF0kPOgDzbC_6ePsX68Fu6tezYgZHb2NWvJvpAWkQRPZFtaNmK2ihVQAir46B-1pBUn2UyWgEQSnv-65Gf67tC-4Q-i3wSIrbNcAAr-SbKYlhEerNHTTf0hSCsdy_mwGVlBLD2i-ryg5i64rmc2AIsBTmADkvRUAVz7eguL87BAeIaNmTBn92zZ3Dw6ldRJ1Z9y5v-j_egodbinCniYqNRuhWm4wH92tvBrseIyotY-HlewBVwkM82hf-Tp20n_GMu2p4W3ZsRc4nlIBNcsahwLkISL9JUNWJ4JfPPu5Hsafjhe7xT1c4_k6x_HaISOjgi4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkUoT6VWFOLiO-YBMbXq896dFs_1t54TnXnPhSFjKDlFpoFTIIV1S_adMPw7ZFW0Ziu7we7hJzV7BqYiXvEs8iwN_0wZaWbc3ANIyeYAynA0LNkh-MEsL8_g7sTzI7pJ0h9NhoIaahtJHWDtYIR3Fcc5WWX_o0m9kbogLVDyD_hzWSqkv-SqstTUM17YiTe6SeesZEbpWi8lpgRo_GWuhnMgZY2C1NZSMTd4HR4gCiVjxUGe_-iSgTvR_jHAcuEHEspctp7_4oUbDat71uwggxHiTxtrT9Swq3Qhk2isgw4RLf4Z87vtW0HUdpEXahkDYjtCgfaQy4ic4J_83iCEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNKWHH0M5Dqkn3c6GpPgmocObp6PcL9hBd6lSbujhz37o69Gh9im6mpuloCqXA9gYeIpXi5V0D_e9f3n8hJfiqFUmkrzHkorvun-hqS7_AiI-Yu1br5LAdWCbm3hzIC6bXXMxlJT6lrTCB7pql7an2NKR8HEBmuZQPUQX5I00m8HGfvLCacF7xJlLvuS4AS0jRi2Doo7uox9QI-YGY_2QMu5BysI4QxXBPVhf4c6eSC0Ll6Eyd_8BlQOoA2x87f6mWA6qN8J4oi8sFzlzUDQJZ1oU7I53W9QWVsL_HvbdOMi6GZQ71VCm0_L3bO1vdRQQkBjqMKMSDHKDT5WTAB8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQc6NDE_E5n0ettNPfEeRYEdGA7SsDQNGpd6QhcW5_4n3TN1Cst1kgq8LYdYSQvgrTTtL6LiWuNpBz34eoSA-N68ORHQKN2x_sKgSRazdFgcSnNHikUTTFOrtr9tMYn38LvtL5Cyh3a83T3RsS0KZfZB__GjrKmfpkYflkm9fQMn7i4RtgIlPdAj66cfWKpublNB2C2ptlLrsoW0fd5GZzHLiw8U-eEzBnvxWVFQiJfaFHcSLcsylz8UMdZS3KlS7M9xRfaCHm8WhRJzTQGJ44sIDfs8TtG1IclW5_W1eKkte4g-vUUntvnoZaKXhpZ3gPj719ZNphwawgedl3sVuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR8G5uZrAVUjbdZPoy9F6z6aCknc_Lza0jKTAEu17LQAH7CiI5J41nrlTLFdr3MJIequwN7njhvgECRHxTwWrsJxi8Ra2jKPOq4cN3uoc3NqvPUPVMwc7AaguVxq8sQL8OIXrgp5gIG7GZDDpqycp3_QWL774I-GgkDNzQKi0sGEqFQl1AjsAa6FIbKNkPRAO1Fu2r0VCYbOEdBoFdvKgOREJkN4GS_0gFcNiQSGSpTKqP0sb-Fu3ptx2sXEQV_KwdDhjFCqDcw7zw5B13Twibv9pgy69WAjZqnxj4RJGRqwwvMHw3oAGCPh4igzfy8fWRDr37gTninUlk7xHULyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=CUYEAXm7AlfsD0tcF0mVDrrpE-ap8r5f96fqBMZH-AFFMqMxUu08_QQBpICVCXKB_0RhhoYNUFJzix_kTypzzKmAuBtL09dt4LV6UkIW13qHE8D7oy7n_TqFx-2DkCTHGV5gatoGTl_ZcRaewUjc3ozYc9d9AjAHv9oz_Ns_xlGv3-5_ZmbXl0GT1skK6li-nPDexx8k9y2Fe02qlDe9ewba9kSEm9RI694pRao7b4n6IfOJ9FJerO69N4EmeP4n9FGM0_8qDBzUfFC49oOBOU-eZb1gvdNxpgwkRwRg8flzHrc0Btb-rzDYIXFpkjc-4gGdtlsusCCeKRbXMWh7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=CUYEAXm7AlfsD0tcF0mVDrrpE-ap8r5f96fqBMZH-AFFMqMxUu08_QQBpICVCXKB_0RhhoYNUFJzix_kTypzzKmAuBtL09dt4LV6UkIW13qHE8D7oy7n_TqFx-2DkCTHGV5gatoGTl_ZcRaewUjc3ozYc9d9AjAHv9oz_Ns_xlGv3-5_ZmbXl0GT1skK6li-nPDexx8k9y2Fe02qlDe9ewba9kSEm9RI694pRao7b4n6IfOJ9FJerO69N4EmeP4n9FGM0_8qDBzUfFC49oOBOU-eZb1gvdNxpgwkRwRg8flzHrc0Btb-rzDYIXFpkjc-4gGdtlsusCCeKRbXMWh7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFmRuCqbu4A9971BCwWfGIDwwUUZrWwzB_uRfGkxvcsTINFUWzOzerj75A9_3BPuf0zncMd2EY9cgMD3YML62VDu-P0pvRuOy7bhrskP6ctldsPvEV2wQktzdq4EJqvZmDE7hBwVH7jP_oIrFoWHVnz8NX4jzSCyY4skchKQd-4FJTulRwydAKTPzx68nqagQUolQi2wB5alBCRvOpzcylhXu7N7Osy7tnrUwdunnBHzpgWueOz3e5uc8DpvbVVMxuFb47-qohNlcVxhWN26dgmjGZZ7KJ0IQfrubeTsFCwA33ZyHO2KJ_yF7ONNIhFvei7swY1JKn4kGO7-ToI-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=MyC4SjhcXzCmqtQqeqDzC5jfV-i5kS3y8SU1BNd790kAPyasCXNMOuDfxBNBK1Gke7bAbiWW6akPrCk-33eJ99mJoTmF_2AGUMTHUjkleCxj4tLjHF9Dsgc_eta1QL6RBm-Mai1vAh1ofozuhHDQW2L39tHkounX13iuB68SaUpUgRWcOD86DC9tfA5TTOEhKLScjyV_lSabFrrTYS87Kay9xP2-8WVx6JeizEuOqkkx6VjqOh3cDMMggbJlqeqqiS5K7DQTIf_2KKny89bO7zAuEyVXmQ15nRrtGBxBzn7AtIEgI-MfueM7PLcHsGHEafRXRIUxAubk5EWhE1O2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=MyC4SjhcXzCmqtQqeqDzC5jfV-i5kS3y8SU1BNd790kAPyasCXNMOuDfxBNBK1Gke7bAbiWW6akPrCk-33eJ99mJoTmF_2AGUMTHUjkleCxj4tLjHF9Dsgc_eta1QL6RBm-Mai1vAh1ofozuhHDQW2L39tHkounX13iuB68SaUpUgRWcOD86DC9tfA5TTOEhKLScjyV_lSabFrrTYS87Kay9xP2-8WVx6JeizEuOqkkx6VjqOh3cDMMggbJlqeqqiS5K7DQTIf_2KKny89bO7zAuEyVXmQ15nRrtGBxBzn7AtIEgI-MfueM7PLcHsGHEafRXRIUxAubk5EWhE1O2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Y6Ci_O346LOuczvuIiCqh95_dDhLm_pWbuCle0D6jUjPNmHLnZTq-0tUipvJskXMMWVZsaXMGQO7mQ7yxx7EQKaA57fq_JZ4gNrUn8UnzAxRIA8U_uckok0dkaFZi7zL-kdlGXanlj4ArxkLxnTSR7KxAexHnaD-qkaDtf9xPGQ9OxQ-2_HaoTwLgidSSGKpB9C0OM8_fIt54ok399wjR0kdcIXHRlCYjnhngtVIRk50voQqu7WIN6yw5_R0SLpdTffrM84YurQ7cBHmEQNf_0kYzG9dgA-lLnyczdc2lVZc_BRhq7u42I4Wybge9FsddKIozGh1rIxvW7xZ-tcsGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Y6Ci_O346LOuczvuIiCqh95_dDhLm_pWbuCle0D6jUjPNmHLnZTq-0tUipvJskXMMWVZsaXMGQO7mQ7yxx7EQKaA57fq_JZ4gNrUn8UnzAxRIA8U_uckok0dkaFZi7zL-kdlGXanlj4ArxkLxnTSR7KxAexHnaD-qkaDtf9xPGQ9OxQ-2_HaoTwLgidSSGKpB9C0OM8_fIt54ok399wjR0kdcIXHRlCYjnhngtVIRk50voQqu7WIN6yw5_R0SLpdTffrM84YurQ7cBHmEQNf_0kYzG9dgA-lLnyczdc2lVZc_BRhq7u42I4Wybge9FsddKIozGh1rIxvW7xZ-tcsGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxKVDvfWCWR_A6hgte9Nb4C4GyipXPaIIggl6PTDgj4zFP6waN9Ev2Y7jQ_dSZEJFlRcnfZw8KFal7nIRD22TdMS4-OYoA-8ZTqqlFhaVcSjbMNN4M9NG-C2_gW1HwsCEX7tWlf3U6CtCRlPAT2sbZ9onjLNlmVCXbluUUhJQ7ODD0D0MxhK9Pk_oGY7rfZ0gH2ZM1AUvthJT4TZNlXrTQ1GV8ZMPgW1QBpEtEtnfSDch2rd2DjhmGFbOXgRspk6UcL6KM6WeJf4L3ZkE79xSIlCJ_fu8cmhhqvFy8uPkIlNyv8-b996IbzNwOIDNsSb5ImaIkxhHVAc70HXm7z-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akr5OC_khd1BuEWv844m131b_LAw8XU8kq62U2eZLKWtf1ME2ZNwg5OP32XD6RoGhgMAm5BUy1oq6GlD_6raciug-YY37ZqEb_1Xr5SpYF_0CcTfMuaLmUWtEmww-I8qzFQsmAQyXaHSOyAr9PnC2a7FNK5I5OnHzbbf4j72LyEPKDa0b_h_Xtuago_qLK-jBr9kwJXdecnkDtMhk7qiqxPnLgr8J_EDys0y3eyZ4YYsDVvfnl6XmGNdcxJrOrTeHpLVUn7u6WCviWSrRjYs5kDFrl4wgL0gFFuePQE9pbWZ9MlDkL6WK7r_76zUF6vEnIwQrriRiR0vpFkOib0KXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nolm0rolHQEFTyhSpn0QiGrmr8Y2DRp2pBKGjF1XiU7iYa-zz5PwXB6Ni9mES80GEEj2Rdm9DKTrQZF0eG-nGsnjd09pxN8rYxPr3GWHeOHRkidUBNeI8CoEG8Y0qRn83ApHNhZcXhUmans_b_FbG-glDA0Eh180W2ipnLBSzONGA4evGn9o75kM5tLjiyoH5l_IC79-eCu8xPFeFCM7sDy9kDHaGhvOYH_3BLOQQ8lhRKJCi4Dqs7CoojPqFWtTP0lg-kVs4gWqNX3p_scNDYQAnjNxE7grmiMqs7X70XRJH8Ev0FVALBpHcZ7682tuNLFBm_mmxPB_7no7tNVnDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B35lcXwqIWH7JtkzUN_g8BWEFqn7tKJJ5nxuCZtBJ-wt5MFmFNOtZ61EwvISldvdIFjifq6HfoIeKdjXeDAyiLRuC3_NGS1E-okWFwxiDYjVlfUooEXvNtDzYKu3MGksndfZgDa0fzcBcOBkqFUtsp09lrQLpSLnLOEyadiywtX0_dNjvVzF_oM6fNQEVfjp00uj7aq1V4Jl04k-uQYck3db388yTf3J7oWMbRayZHGSpf2Wk1xPQ9XWg51ADyE_0ITI5COcGQ0_-uT1i7JbfvHaO0XACMkAc4sTikdTgibR4ou5-01eNn2vEAdQRMTi3vuGh_ECQCqYkMpwlqQxDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=cAYfGiGAPTyvMO_FMtQ5MVcP6PI_dOAuxszoFd6xni0KxaSHHA2HoZ50Hh6llVcyES841JiCQBWWcH3GMUObU-hlI-vr9tQcQyhpjaVdg9YNb7FDmMcPG3hbs__MGnV4dgW6Qd99lXTcv4WZgyqwtLa1OHrQqaCeGfaSxIgkJGHKwiy8vdxaU1Kv0X9D9WujMM80FZ_qm9TCYzCejIeR2Tl_eynQRtA2Q_Xd_AOJWMuPuy5W6Vojy_yFmeQnOEr_SAbGBOl7pxXYc0vADfyVCwfveHMAMY8-_qU6WrBzxJHQB5G-IpzdIoxcWz2YasYb5U9miga3K0QwmdETILnkeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=cAYfGiGAPTyvMO_FMtQ5MVcP6PI_dOAuxszoFd6xni0KxaSHHA2HoZ50Hh6llVcyES841JiCQBWWcH3GMUObU-hlI-vr9tQcQyhpjaVdg9YNb7FDmMcPG3hbs__MGnV4dgW6Qd99lXTcv4WZgyqwtLa1OHrQqaCeGfaSxIgkJGHKwiy8vdxaU1Kv0X9D9WujMM80FZ_qm9TCYzCejIeR2Tl_eynQRtA2Q_Xd_AOJWMuPuy5W6Vojy_yFmeQnOEr_SAbGBOl7pxXYc0vADfyVCwfveHMAMY8-_qU6WrBzxJHQB5G-IpzdIoxcWz2YasYb5U9miga3K0QwmdETILnkeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=CP_9RGk13zjl9G0VdDaKzllEgK1-qccAQU7eOjMMP_NQq6SIC5EN87ORrylJv789mGcI4O6Xo19Vgg5MwFxCMMiKdi2WawyZPFxNdg5TLirkxnldkjMR3zcNvwmu58xG8nLAdTeyEyoArJfIiWHpFyx9jNnZQk1WiB60Sizuy4P3aSZywFgdQLu-nGMeYIB124DU8Boe4CdmaVnxgHnqfqwZVMNmDDdjSA2M7wyNJqO4DuLxijoiOkoF364P_mLbs8ABYxljTji-egWak-cB4y96P6ifII6jqKy0dcmBiA4YnElpsKT5Qg8O62feGRzrUNQ96pJlJQmiOxdEAf-YtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=CP_9RGk13zjl9G0VdDaKzllEgK1-qccAQU7eOjMMP_NQq6SIC5EN87ORrylJv789mGcI4O6Xo19Vgg5MwFxCMMiKdi2WawyZPFxNdg5TLirkxnldkjMR3zcNvwmu58xG8nLAdTeyEyoArJfIiWHpFyx9jNnZQk1WiB60Sizuy4P3aSZywFgdQLu-nGMeYIB124DU8Boe4CdmaVnxgHnqfqwZVMNmDDdjSA2M7wyNJqO4DuLxijoiOkoF364P_mLbs8ABYxljTji-egWak-cB4y96P6ifII6jqKy0dcmBiA4YnElpsKT5Qg8O62feGRzrUNQ96pJlJQmiOxdEAf-YtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=snd8OdQVqdqt5YPX3XiA5IK2WIAH0lsyYIQMIGzzdUtX4P94nM1QvXmAFTCk2vcNcnzPtUBNmzxqYKxLnzlbMCm7PNwq8HTNt6_lfgge8JkqohtD578hAT7aptYJPEaJkJJNMojPLdVtaVG8tlHkX2XgOSxK2xOPTjn03Q1qWCWIDFnD9OD1pmAMlypZv5rkyjnxwkwnQwlyU7P2pkh8HQiUsgRTGIDkhyTu2wuTzu75u4kur4o_-S0yMmN3H1pLUoEKQxFDmmuvz2Qz4OWj5qnZqTaxyc1wE5oVClYHM3gL7SAX4QNvNo75qx6iLCgELOxJACMVnUtqwfsfP7HGhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=snd8OdQVqdqt5YPX3XiA5IK2WIAH0lsyYIQMIGzzdUtX4P94nM1QvXmAFTCk2vcNcnzPtUBNmzxqYKxLnzlbMCm7PNwq8HTNt6_lfgge8JkqohtD578hAT7aptYJPEaJkJJNMojPLdVtaVG8tlHkX2XgOSxK2xOPTjn03Q1qWCWIDFnD9OD1pmAMlypZv5rkyjnxwkwnQwlyU7P2pkh8HQiUsgRTGIDkhyTu2wuTzu75u4kur4o_-S0yMmN3H1pLUoEKQxFDmmuvz2Qz4OWj5qnZqTaxyc1wE5oVClYHM3gL7SAX4QNvNo75qx6iLCgELOxJACMVnUtqwfsfP7HGhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qDJUZ9O9_UVtAZxojrn4JDW8WP22E3Nn8WR4OiAfhn9ChrAHgRpJdXdcx_OdhDEywkD1Kcird4Y7DoW2J0LmCEB6eIruj28JkxknuqHspSkGLXc3QbouC06YdyVYvs6yqYhZJvyCNCfmpX72Kdwbnb_daUpqiBaXem-WGWDIFuzBmY63eeTgCYneMVkHyuUFoP5IwW2OqYTg5sWqZLUz5spwN3VtYNXvMGoffZ9ON7QZout1-GnTM0KdiYy1kC8_URlUfkIfSi4thUtU4CFJvAb3xSgLpWXsbBxJcY6bKSD99UjEFBXSiolR878ncaOM1IZsunE-KRDYia3k49y6uDilF7a07ioPza4FARlz4GNjG4787zJ6pxyREqSKlc8t_coL7oM_Ndwk-jsKmWt9qpyvPY6DFkFa_14aCNQm-fkBQgFbYA1mu6e9igDW4tYexZkrxEo0vpSlJL5Sdl7nISucJCFSv2L68Rnmty4VJIv5hUqnWbDp_BkbXE0ZpEy_J_djl_WzvmSEdE8RsGLh90fjuwde3R6-1UWvLNsbVD7a2YHuEa6d3x7y5dbhsq68lUxcNJDbhUJZz7AeQ7lhv1TKDaSJ5P5uq-oOd0BLzzWP7wZ--gabQ0Wsd43BH1gLlWX27cZDYIrMCk9BZFlcgwXRe54y7pRzq7TH3OhCFxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qDJUZ9O9_UVtAZxojrn4JDW8WP22E3Nn8WR4OiAfhn9ChrAHgRpJdXdcx_OdhDEywkD1Kcird4Y7DoW2J0LmCEB6eIruj28JkxknuqHspSkGLXc3QbouC06YdyVYvs6yqYhZJvyCNCfmpX72Kdwbnb_daUpqiBaXem-WGWDIFuzBmY63eeTgCYneMVkHyuUFoP5IwW2OqYTg5sWqZLUz5spwN3VtYNXvMGoffZ9ON7QZout1-GnTM0KdiYy1kC8_URlUfkIfSi4thUtU4CFJvAb3xSgLpWXsbBxJcY6bKSD99UjEFBXSiolR878ncaOM1IZsunE-KRDYia3k49y6uDilF7a07ioPza4FARlz4GNjG4787zJ6pxyREqSKlc8t_coL7oM_Ndwk-jsKmWt9qpyvPY6DFkFa_14aCNQm-fkBQgFbYA1mu6e9igDW4tYexZkrxEo0vpSlJL5Sdl7nISucJCFSv2L68Rnmty4VJIv5hUqnWbDp_BkbXE0ZpEy_J_djl_WzvmSEdE8RsGLh90fjuwde3R6-1UWvLNsbVD7a2YHuEa6d3x7y5dbhsq68lUxcNJDbhUJZz7AeQ7lhv1TKDaSJ5P5uq-oOd0BLzzWP7wZ--gabQ0Wsd43BH1gLlWX27cZDYIrMCk9BZFlcgwXRe54y7pRzq7TH3OhCFxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgnlkmCwEIm151lsw1SE7HUqo0AUI8S-OlB3vPo9w5i_C664geizBv3NesnxOz_unx7bafASdMk5rbeUiyaLfc-mvb7tYGfhNO7YVvkjru_Qu9WBnvLwV3Gz19fXM3x_XDNMCsaROonizmGpNgWI6PWdiS9RcU8I-_dvNUCts1RGMSErxMWR6INU7F9eWGVSEAMmh9G2RkiMftU2dnFzVHUIW_L4K15XO1TpEffSTg3jad6xj6VgpDY50yRB2KKebpgDycbQdGiwRGQ-MMxaGlGz14_XlkpNVxonZ9TG6WHGzRdZu5T4c12hfKNkv57kSItVcwh2Wo0rUh4IuA50Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=JKUHfsXDZvOQ57fOMjsCQdi9v4g-m1TIolQFIoAO5UHYyTnhQoQURWQtfmwDj2RMUKuerW3kuLo9fH-f31m7t8eL-_vT_IlhC2xpA6PPzUFDbW-swyg55oniIF_TUGtRDVoB_fNYBu_vGW4sYFIJXRTdSjGdFdTcsvWr1eLHJkhBvk34aLG4AXoPQ48V3kGG2CACGtkpunwv4F6pe2kXzEdF0TmlECPFBK8hw8TyjAD4d1YCjs79BDrQcUpeQi4n4o24Z-f0OOzwOULq8Mh_8iYmaYboSzYlWDE1nPXFqYpyZ0jdS3xPg07UFUBT03c4LiSJtTOsURPCPjenuydGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=JKUHfsXDZvOQ57fOMjsCQdi9v4g-m1TIolQFIoAO5UHYyTnhQoQURWQtfmwDj2RMUKuerW3kuLo9fH-f31m7t8eL-_vT_IlhC2xpA6PPzUFDbW-swyg55oniIF_TUGtRDVoB_fNYBu_vGW4sYFIJXRTdSjGdFdTcsvWr1eLHJkhBvk34aLG4AXoPQ48V3kGG2CACGtkpunwv4F6pe2kXzEdF0TmlECPFBK8hw8TyjAD4d1YCjs79BDrQcUpeQi4n4o24Z-f0OOzwOULq8Mh_8iYmaYboSzYlWDE1nPXFqYpyZ0jdS3xPg07UFUBT03c4LiSJtTOsURPCPjenuydGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZTch52LMfndskKxvxwOsICWyxxjmkNG33W1TDMkdhRqE4Dcqm26oXTSuwK1f3vtOnadusiUYeyEWUL8jG6_DOTJiEaanAA7BesdO5GgxmN-ejdr8OwZP16TzihZPrOr94RCE4Y6lI7jBlWfrimY5iLUPcvC8OnkyCYXAC05KxSr8zrl_mKUAikis59mAf9TcskbBTzlXzK4Z_fxry4YYN4fT2DQrrtzBvVPoI9mlL7uXVLJvmszZGS4lqmnCUzbgxU6aA2rtQdaAiuj8n1rIoF7xCqRQcNlwKvTqrdldnMxEJZUNP-aFM4GCOxuW4rwZZ7In1kyD0_pX5uD9mfzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1r2rzu_zk3q2S6MuB_j5UBb1KGgHOZkpsSnXMLLWhGtFvRne64cOR32wcrh5-ekcUFKe0YJgIUvfJch3Jx0a-gYGkbZmubx5t5ZOaEpTWzkSzC6lDd49nF2TO6HQN8euZNWrZERcumyca4eBeWWaEuTIQmYb2jmZgqxh6WlHDXcQ7SZYCis7vcpn5OoCsETBjenQLcYoFWjtDqWA6XiOW0E_bpEFCgTZz5mVkfkRntHZN76ZnGLxNrITiac39T-j7K_Bh4Hi3YGffXVaCpRaa_kQYzrutzSeTgCaYMU08AdiojUK-Hj4aKhxpoPk1_9BgCErn5xtUlUuI7q6To48g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=boA9f2dnKAHcVsmm3sVJUKDt6t3h3QrqxsYtvtrkjxFQSBb8-ZgsxyEbghe97CntOra2v5COCnu5kW8ZQLAXr5gD7S307c2uONHnZWGcqVPICndvL-aiNFvjB2yBVBllctoCSCyGHqqDKrTZIPnxu_7zLDoNX0q-m5pddlH6o5E2YnowclqzZrbJTcldwvzjlDM9ptGS8hVLrQ8-xkDeVfZubDs5xMkWxwFLTWgTW_twvaOImN-QFSqrvFT78AdiYG0qPlCp-tGMeRR1uNYhh6SincZYNCL3noYah-JtKeP-obwv9nQ8IfiZbS0bKO9LKZThcq8qFaFRdP-BRR5_6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=boA9f2dnKAHcVsmm3sVJUKDt6t3h3QrqxsYtvtrkjxFQSBb8-ZgsxyEbghe97CntOra2v5COCnu5kW8ZQLAXr5gD7S307c2uONHnZWGcqVPICndvL-aiNFvjB2yBVBllctoCSCyGHqqDKrTZIPnxu_7zLDoNX0q-m5pddlH6o5E2YnowclqzZrbJTcldwvzjlDM9ptGS8hVLrQ8-xkDeVfZubDs5xMkWxwFLTWgTW_twvaOImN-QFSqrvFT78AdiYG0qPlCp-tGMeRR1uNYhh6SincZYNCL3noYah-JtKeP-obwv9nQ8IfiZbS0bKO9LKZThcq8qFaFRdP-BRR5_6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=sOWeUGApryl5zaWlFH957mAb-_tCieIeGFtJ9ExPwY-ETlpqhc8zhbaflBayUOaFmhosH0xQblUbF4yrr4WCKy6kKYcL1CmX9QYoZqiQcs-_pL2equDswuYSXCvN_OeMYaQv5BXOrW_Oo9m6fZzX5JqvTCrpnIvX03LKoHUiAxYKGcAC3hI_m0UcSm-lJq1F5bt0XTBuKQlNCv5JvfJGhyVkXc56M7JkA1GBLI6Jm9WQvQ6WCCw9QQXHPmE6za_XODwMfK7YIAiBZtjsySoG4ZBlqnaSv5Bh7owWhxgLqfwNsxgJ-zOmuKia-tL8v2n7Q7x0TCdvSNnilrWIY3v0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=sOWeUGApryl5zaWlFH957mAb-_tCieIeGFtJ9ExPwY-ETlpqhc8zhbaflBayUOaFmhosH0xQblUbF4yrr4WCKy6kKYcL1CmX9QYoZqiQcs-_pL2equDswuYSXCvN_OeMYaQv5BXOrW_Oo9m6fZzX5JqvTCrpnIvX03LKoHUiAxYKGcAC3hI_m0UcSm-lJq1F5bt0XTBuKQlNCv5JvfJGhyVkXc56M7JkA1GBLI6Jm9WQvQ6WCCw9QQXHPmE6za_XODwMfK7YIAiBZtjsySoG4ZBlqnaSv5Bh7owWhxgLqfwNsxgJ-zOmuKia-tL8v2n7Q7x0TCdvSNnilrWIY3v0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjlYzSm8veHxVbH-R5SidAP7q-QhPjw28DnZ6Ns5NYXJ3SgVDBpgPnf6XIk9Ew9syweZLCYHaBkj336x7makOiV2zLUFhG3d54coFARuVwFHkpqQTk5D0XpahCSIljtR8YsTXx7c70NrFtwj2Sl-MixTh5NX8pSlRtMsOOy6C9GzHoaCMWuLV4bKzSTkE2myDkms9jFNdDZ_wwUE90tGdulLp2YD1Yv35TEUJOo0VOZo9wMopOby8XrqnEk1JCClwI7d6F3FjnI9S0Rpj6_7FkfYp_OSSDvep_jD4HzU80UCNmZ7jJNXk5U6ngkfKFhhLJwvGYBgCF7fQTOXnEoHGA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=Q5kFmMAXFuLjpjIdkGHY0_VHo89gLsyrv0szBgZRZKslo9dxOpvYlZ9YZZSZw9PJOv9DHr3gNKowrkP8BoTqeHiI5cylGdYuveWU8RqhFXFm7XLehBcup7M1D6SvfVuA7nDZkxhIiWAXDPPC7X9mqgmHQpcoUpv8XVk6XDzglUxMXtErZ2pCecqiUZghC0UXtSJ7vquiHHXsc8VoR8lj27zCpsRlH8BgsCqiC0mm-Qbz8B-ATUIkG1MrWTJusC-Hm7fKYU15RttfP4YUNXvdWcFLGOxjjSCeatPLJiZXVz0HWDtyqs1_gMLeiceIz5jNcDBv1tYt2Q_hUkGtD6Hjig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=Q5kFmMAXFuLjpjIdkGHY0_VHo89gLsyrv0szBgZRZKslo9dxOpvYlZ9YZZSZw9PJOv9DHr3gNKowrkP8BoTqeHiI5cylGdYuveWU8RqhFXFm7XLehBcup7M1D6SvfVuA7nDZkxhIiWAXDPPC7X9mqgmHQpcoUpv8XVk6XDzglUxMXtErZ2pCecqiUZghC0UXtSJ7vquiHHXsc8VoR8lj27zCpsRlH8BgsCqiC0mm-Qbz8B-ATUIkG1MrWTJusC-Hm7fKYU15RttfP4YUNXvdWcFLGOxjjSCeatPLJiZXVz0HWDtyqs1_gMLeiceIz5jNcDBv1tYt2Q_hUkGtD6Hjig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=lT8f6FNPl6vc3dhP8CeNM68BIGTPslKsXOkyWPgvkwB_5JQ3f2hZjFnkTKCGG2K7vLzV504FdBP_huh7w2ducC5vA9-GSXyI7rx373-eTGJX3Ppln3FDlUHbK3mPhzsEW_4QwNTdRUQX2sywIm5qR9KXEOrpW0Bu59z3x48LtsrVYRs9X9VBQzyDmt-3zRZ5ZATZ29UI7RqrLdYHmVL2VWXc84ErKz5tbZvPczPnjGosMfMgutnms65ApyXPHAINhIV9Q_mwyz8-thMsqx5EckLKBXW5Nf7pJkzk4kXNdFvWhrr2It9DwX_FjtmoVwrYCoSok7J6kJis-hWA3Z1AHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=lT8f6FNPl6vc3dhP8CeNM68BIGTPslKsXOkyWPgvkwB_5JQ3f2hZjFnkTKCGG2K7vLzV504FdBP_huh7w2ducC5vA9-GSXyI7rx373-eTGJX3Ppln3FDlUHbK3mPhzsEW_4QwNTdRUQX2sywIm5qR9KXEOrpW0Bu59z3x48LtsrVYRs9X9VBQzyDmt-3zRZ5ZATZ29UI7RqrLdYHmVL2VWXc84ErKz5tbZvPczPnjGosMfMgutnms65ApyXPHAINhIV9Q_mwyz8-thMsqx5EckLKBXW5Nf7pJkzk4kXNdFvWhrr2It9DwX_FjtmoVwrYCoSok7J6kJis-hWA3Z1AHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=iuG7OOzAolqh40emtMdtTu46b2eyAarSPBFWDf0iZiA9kJ1dyQv9P25Cy_WGWvgGADu0Hyt6dMKipy8-vGDBF0W3dmuR5aGMGj3aUmqK4No14ECdzPEShe_dzdIOialrM0iN8LGJwCFaGSC29WLeKSoBJyLVhvXlnvYHCBh8I2Titd6djDKG__3C1n_gYSmuqaDn6KHN8wexIuMRL3JKhEymQ4raDryIhJy-TryuO-kKh14Ps7F9VOPMPI-y_psOMV482PeUP5mvCOaYIIT4p0D9ClPr3bxk9L6-JBDLjddDCMmEkGnc51xbYyMj7pDAZMOhOOhN85_KMrPDWoSRWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=iuG7OOzAolqh40emtMdtTu46b2eyAarSPBFWDf0iZiA9kJ1dyQv9P25Cy_WGWvgGADu0Hyt6dMKipy8-vGDBF0W3dmuR5aGMGj3aUmqK4No14ECdzPEShe_dzdIOialrM0iN8LGJwCFaGSC29WLeKSoBJyLVhvXlnvYHCBh8I2Titd6djDKG__3C1n_gYSmuqaDn6KHN8wexIuMRL3JKhEymQ4raDryIhJy-TryuO-kKh14Ps7F9VOPMPI-y_psOMV482PeUP5mvCOaYIIT4p0D9ClPr3bxk9L6-JBDLjddDCMmEkGnc51xbYyMj7pDAZMOhOOhN85_KMrPDWoSRWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWeJVi6hgTMTqsfUmY40N_LuRUZc-nShbnr3gfippqFUZ1GQrZENrM4aHbUe3wsGHOjwL4XIt4L4pVrbXIN6k4GoDIb71QcJTuhUnVacJ9vEuw1iyUL9HAXaRcyO0Jntnbqs9gheMlqMfSb1qDiX-QMhX-VB7ogH1KkNGB4_x2b3HIbFpt32Fd4AVSCYN3jkVFPz7JkIibKT004OTp7TvEYauCasZUauEgHc-WFiJg4UPMk2dHR-B1YTFbmGyy1lyYtCLLiPXYGn9cPM4WO3fRLEa6umL5e-lAmX7XJ-E8FKuFGYQzB_5a57rxkK1r8zN6JH6VnnVhckJhoU6B30ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn8g_ZeL8Wbp0o4QYTDKSZ2riBCmzL59QV180JgD-3mqk7IWO8VZlZAGaGL0IC2K-PUwojyGmm-1RtHJi5H71caCkVjvJNRfAwhsxnB_XsV1nK4Ry28qylbPgDeg-KQAnB7OLjrbVGDVFlPOXdN0915K7xLsAueL9Y0F7DWM-PGdT3WPcui1J1yeGl6W98tvnf3WMt73zuqWP8NCHYbDfixZvYAQIuh1cEzZKHVRmVzS6QBjtLiCzSPorAXQxEr0Yl3DwlFMSwlsIYntRrTa1_YwP2RzOxhGZiqVbaIKCw_aU_9V9HWFpaauqegugv3GOq_8gDJdavLuI2BT6CcX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=J0bRAkB_ztWH_56PHa3YY2qCjM0hue1j-RRsEoLi5CDSGOqPxfS56Rb3F0YD4tvF0mA85kgC2_PL9dkamXg5V3lZrZ_RN-DCoFbh0BMVTGe5yoBcOY01_96hDJEGLbYasHHoUb-Gj9tdnW-Cgkas1iXsu9pVOIErU-Tru_y4DYlr1Ki7oNWvAV3dbUNPbCxI3f9kCKx7Jhskc6K2dTY7h9MpFsEyPpgLnLOrVtJ7oaNJkmTnGKCulVe6Vddw6qmpAGF6D19g1Fa-zHF7stMUexCrCnb-dcfM__Xta3LfxdWTUCtYkwkxZdjay_BrP1b4QN81bpdlipjMGwdI2W4lGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=J0bRAkB_ztWH_56PHa3YY2qCjM0hue1j-RRsEoLi5CDSGOqPxfS56Rb3F0YD4tvF0mA85kgC2_PL9dkamXg5V3lZrZ_RN-DCoFbh0BMVTGe5yoBcOY01_96hDJEGLbYasHHoUb-Gj9tdnW-Cgkas1iXsu9pVOIErU-Tru_y4DYlr1Ki7oNWvAV3dbUNPbCxI3f9kCKx7Jhskc6K2dTY7h9MpFsEyPpgLnLOrVtJ7oaNJkmTnGKCulVe6Vddw6qmpAGF6D19g1Fa-zHF7stMUexCrCnb-dcfM__Xta3LfxdWTUCtYkwkxZdjay_BrP1b4QN81bpdlipjMGwdI2W4lGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN2_fbyY_jaB9OCRg09jXR1JiB98emLj4Dz9fttCARtsAQ5vLouM6KmW7hp1Y9H9TtdtmINyyJe8Fe_P7vYMeq-CLvuK8tHud1UHemUb9qi7AcKo7SDDmI4wPCbXAKRVsC73YUENpAWFdcCrFQG5GtRraB369Nf0CafGCH7ZdhjuXTAlySZLZ9kzQOZYu9ZIfmwMRlRcuhrXCE2nicLs3bXC_UcoJ02ftaCMKQUoGTKrwHsKkPskOpkzQHVKZQRzYhVAr1ELeIlQ9upE6Ce7KJJIh1Rbu2mfLiGfLG9PvK2IIIzzpaNPD6XZeXsgj0U9rmoquARjVSSOA12qp3Hz3g.jpg" alt="photo" loading="lazy"/></div>
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
