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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTlxXodelZAAUKeGl_CSolqihwb9i2RTgfHoj5F0PULg6_R1ps2Z55DfHD3yEQ6dQaqc0lEzOUmFLC_gejZzbBX7U4vITdlBcuWiLkhyA3AVQb7N_0PwToznCNI6AFDwsGHg53SHI8bekdkBXHoheGV_CU6H16uIPmJvJpvw8wjzwWwaqkBQgnGEKdHB9Rm-_KeYxmk1blfd14DROqikmnQOpwM1DRHXqAYR4NnowRwCsDkZZsMVS48SvsjAy7Xrued8ABhjjPFXm2lttdmCz1-gtqGqDa0QgeWVArkK_Z5ZQOkB7sT4ytXUjnHDdAxXtlqHqlZt5lzixl69-2pyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pBqwu1adqCy7Pckon69e_MQCvndFh-eZ7WZtdvckL5Fv0eN87EhIsV0q6614j2pahZkUN02omEYBlRa23eMhO8RjGV2-mWuRjoC_DDlymBo42MTJfy2MOdpPMtTmejICoaXTfr2c0WVS63dfj97iRtgmjob1-pAoU7NqPNNyYmS71aLvDHRo15HoGMXtfK8yzeiL7J-kGfMAPz9LvwNQqPJL2IQE0JLOEcFySJwTrQgZowmqL5Z57Hc6gyVmdzdb2JCUgyI0uzS1DSdsTzbvzcPzEdUJvTNZYCGxnf2-BMFL5pcDv8DQ-S6WDHKZMRIzGNcmtbAomch9n2fuJdnHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pBqwu1adqCy7Pckon69e_MQCvndFh-eZ7WZtdvckL5Fv0eN87EhIsV0q6614j2pahZkUN02omEYBlRa23eMhO8RjGV2-mWuRjoC_DDlymBo42MTJfy2MOdpPMtTmejICoaXTfr2c0WVS63dfj97iRtgmjob1-pAoU7NqPNNyYmS71aLvDHRo15HoGMXtfK8yzeiL7J-kGfMAPz9LvwNQqPJL2IQE0JLOEcFySJwTrQgZowmqL5Z57Hc6gyVmdzdb2JCUgyI0uzS1DSdsTzbvzcPzEdUJvTNZYCGxnf2-BMFL5pcDv8DQ-S6WDHKZMRIzGNcmtbAomch9n2fuJdnHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYRZhtEz-8sD1F7MOQR2V19u-NI8f3aDuGo8I2uLk3JrJkYC073IovJUzhtzLu1GsdLZ8aCqWnCyxgfTmT0DXuCtJslrKMJzw0_DFQl86GNCfwpqA9ddxfD1OnkvbD3xXUTv10YdmIhBH8-1iNo5fgabmddRISviAzMDvuGLqosvhC9y8RvNsbsIeZgra-Ql6Bzss_9Jmz0bHLy3qej3NrBZa0j4avcgWQrWhscITnMm7hCxwybICP9uE3WTXJRAbIdB37OTrc8vys_XJntqK6mkJxJocRP36hmLMIkmrYDxGiPtfaqU4vT9eTvY4M9OA0oaehk_dASQHHnVFszEGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYRZhtEz-8sD1F7MOQR2V19u-NI8f3aDuGo8I2uLk3JrJkYC073IovJUzhtzLu1GsdLZ8aCqWnCyxgfTmT0DXuCtJslrKMJzw0_DFQl86GNCfwpqA9ddxfD1OnkvbD3xXUTv10YdmIhBH8-1iNo5fgabmddRISviAzMDvuGLqosvhC9y8RvNsbsIeZgra-Ql6Bzss_9Jmz0bHLy3qej3NrBZa0j4avcgWQrWhscITnMm7hCxwybICP9uE3WTXJRAbIdB37OTrc8vys_XJntqK6mkJxJocRP36hmLMIkmrYDxGiPtfaqU4vT9eTvY4M9OA0oaehk_dASQHHnVFszEGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL1_9FeoM4DBDRV6AjojhNtTO3Ishj9yU406zHOQM229kcHiw0f7rdwgvxmUv1x6rGBtaX30gwauafdYqU_ku1JNHzVpuerRqyKmzsH1LOQ0IZIBVTLdu2Pdmmi9kJQSiCP4ZmNNL8DGvVIcCeuhTou6lUy9RdLCUHQcT8AT498I2NUZUzmXM7X0cZqf_uqtaIPsL6h259A1_vUf_0pEufdCyzCuYB_RzlNlBBAt8KS2szHSGo8rQeeFZgx2BUv8lBPoJAFcIyiwhcuKHSuC-6h67zS5IVG15-s9GaCQYeWg5u1moqH4Hsv0vK5dZ3Hz7x4Y3N3UM_7FmzQVU0Bomg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCYTIsExEHsuCIiFERV2VUn4EfEiBEVD86lWlORydKLKubRIaHj1wAI_I73_tL_BVYdXSFaXs50Imwyght0kl2rvtE-pnGiD6QOwGpVm7shoq8bZnjLVDsNjgywseIAgy4lXkcipt-h_-jN5mt-qGUa28G-sPwCgKBJZb9f7CVvEF9bGYPbtHlHjlcmQvH5zgZHloJGi_9e65ypXshwfOvWenH7xsEJSHr9zNdKfRUfV5TclEnbHzHVJ9wozlX-cn6RKykBkY7nLXV4X_aXv2i2vwBiXTwLN1hCcDrnvZ4BcclLiARMcpFo0i-0Pb3RqaZF3boCBPs8lnBl_M5V9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=WrKDlRfwaTE1G2i0VdTYlctNaYBAuqif3QsQmq1VhmRXGqGEJr7-J_ESaNLbpa7W18H21e9O5prFLcGs43truiA5sU4HShjtm65IOqoidjEfZPqvE36nQFKuRhZtksnmBCzXlcm3tcgPa7OXOMMQl4uc_v5UE_bzONP7uuyFP7gF01rdk8etO6N44bsuh0ksudQtt90HXz7nHYplb2cDJpzEcWpmY75hXUfzaTdrPttniUM0fGKEIz6rgOV3yBUHbKjJXnzVgWw2MDBruaGaMosb50UgNCiumy1HEZdox2Yw4CRm0FkdrTrDYB5iNhx0_RMxLwz1tDUOvy7RaJMRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=WrKDlRfwaTE1G2i0VdTYlctNaYBAuqif3QsQmq1VhmRXGqGEJr7-J_ESaNLbpa7W18H21e9O5prFLcGs43truiA5sU4HShjtm65IOqoidjEfZPqvE36nQFKuRhZtksnmBCzXlcm3tcgPa7OXOMMQl4uc_v5UE_bzONP7uuyFP7gF01rdk8etO6N44bsuh0ksudQtt90HXz7nHYplb2cDJpzEcWpmY75hXUfzaTdrPttniUM0fGKEIz6rgOV3yBUHbKjJXnzVgWw2MDBruaGaMosb50UgNCiumy1HEZdox2Yw4CRm0FkdrTrDYB5iNhx0_RMxLwz1tDUOvy7RaJMRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UiJ90sMLEy-XCQdbe0FD96mn82hbUTjI6wRtAQ2KAYHnKtlbWPiIQmOeBE56BzLl18K53qDUui6YXPe-BD-_AJeRXnOvde0xLUsIff5RmIgzaVlLTqCgBpv0F0i_VcgKqhZQ-j4qWEiWCkAmTr3D3fcOSPjsZrncRJAYcHD4MTUzmvY6_yKEaOavijbVRttGLYaY8Q1qdStGYUWrekofoDBjGqNdO0TFLBtReER6yg_iRy0cFnMLKSZO0Eu8_YYXPIIPh40FZo4aznHjfOjMBepo07qJJ71eJCA-JC_C4ih-1B7wHxmPrTyMfdJj7BtXifbylq1Njp0X2y3TKgOYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UiJ90sMLEy-XCQdbe0FD96mn82hbUTjI6wRtAQ2KAYHnKtlbWPiIQmOeBE56BzLl18K53qDUui6YXPe-BD-_AJeRXnOvde0xLUsIff5RmIgzaVlLTqCgBpv0F0i_VcgKqhZQ-j4qWEiWCkAmTr3D3fcOSPjsZrncRJAYcHD4MTUzmvY6_yKEaOavijbVRttGLYaY8Q1qdStGYUWrekofoDBjGqNdO0TFLBtReER6yg_iRy0cFnMLKSZO0Eu8_YYXPIIPh40FZo4aznHjfOjMBepo07qJJ71eJCA-JC_C4ih-1B7wHxmPrTyMfdJj7BtXifbylq1Njp0X2y3TKgOYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpv6g4Ak46Z1iYgtj42YEj63keEzLxc0dT1ABbwnr164Z1_rh902wa4VJgmIoEKUdO31YG4LKpo-m8kb1YklBk8o26-v0XU1_6QIslI-qXypRQwI5-1krv3cF92iyOiCXRx7Mds0_eNTvUNib_3QUJg7EVJ5D_aoPRyDGX3Nw0UYONmZ5hRJO72muKf472pE0m2g1VRat4-dtsyJNTJrvdz_hJFg3nJ2EPpH2ReX-a4DaHt90eIqjZwMe66SCu1kCerqGhq-2r53-aDnfvntOiYqMe0jGS4QYCRBnU_NL5fL1qlWCfRs_usMUzJzv54qrGS_97KZS8uK9DgO8QHcLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2NswGgd5lxDShXm_F01xt6tt_wpG9b3B2esiF7riYXC0YezRAwjKK3m0VP1EcZDk7FgUQu021yYV2_J3shHe0-kEtWm11fBDTKdlzGwJcgJrof2SUzNNEcazzzrTEwlUxNdqtrVQs7zYUypHHFl2DVJNIDVLdWNO39jaiEHhBydBndd6at4V_R4RjhUsKHrUMF1t2uKYUhUJaNWkeCfqO3nfihvVUQEGMcVHMvwj-9pm6TIwq2OymVyz-rGpS9CqdYPPlLdpZCO-LKSUZWKbh8PLsoQTLSWLKWvh-cSfoP9dEfagfmTEZbjl77c4xb5iln5BgcXBxXJRiJ1eDyp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf8mUJM6QxGdtYdv0zrlPfhEGMQ9SeHOZad_adJ2cqwceKrEhijYP9Du5gxNRHz-jNilSrErT_ins6FQ6p4CnXV_D9QZ9H5GwrirprUTsXXFz2ewCXQdWAJf-11uhpT_DtlooTZj4xiE4q8GifK1QTdL48KAyXlR2Al8k3MXJj9N8uXH3gxQuN8EQYC5lhMNoAuotUsgcgmKYsxV-lxCsv0iEwOFDUY3ZYwrec0fJNSg8Qnr2s36AvjfOc-GeXkpN8fd_OgGNnjOZMnkfnBYfjssHogpwxK7lnwn3pKgsvRfcIRoflGPM0e47BmSexDfiu_EtMiid3lqYfHnn5GYDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=qAIJl4LioND63Jyhtz_YHycA0flNSgHVWd35bGbLLaEUdKupR7_FORztpkH_UkBBXAlhLtmj-WjA-bLukD2o5pms1ZM5oGYRL9Lg4VrGgy_gMiWI5ZFD-a_CzAQ1LTVwm5gpxuiII7ZYg0X8cvppOchGmN_z6TLZabCeXiLehs29Qu9oFdpZmTQz8QBe6juajl8QYx5Ox66S-e6xl8WhPja-oqCJWGvlH9IrS8X6oLkWLVsAZLr4hXb-wFidZn34zOozfNYE1YOZtnKQyNzm03I3tHItQAQ0h-tY7mxqMcV6FEKt3aASpwJxAJB-U6UL3QNY4UoBU-FJZdexcOWrjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=qAIJl4LioND63Jyhtz_YHycA0flNSgHVWd35bGbLLaEUdKupR7_FORztpkH_UkBBXAlhLtmj-WjA-bLukD2o5pms1ZM5oGYRL9Lg4VrGgy_gMiWI5ZFD-a_CzAQ1LTVwm5gpxuiII7ZYg0X8cvppOchGmN_z6TLZabCeXiLehs29Qu9oFdpZmTQz8QBe6juajl8QYx5Ox66S-e6xl8WhPja-oqCJWGvlH9IrS8X6oLkWLVsAZLr4hXb-wFidZn34zOozfNYE1YOZtnKQyNzm03I3tHItQAQ0h-tY7mxqMcV6FEKt3aASpwJxAJB-U6UL3QNY4UoBU-FJZdexcOWrjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSNx8Pc1WVhuOaNU_anmJa5HLtexixxVpPwwdFAvm73MhWgWpbVZmxFXhQNlWu6Eloz7gm6YJIOZFMXKBeKaWIkg5y2tox6788wMa4o0xCCB96VtcV2i-FEW_rJe_f_sNT0-a2X5SoilOCFaCp1BTF_9JuNBatM4nFmNr2yc0gwgNvrXxJ2Dlee_vBBwoTAKwc-ryn69OZhAnryHwv7FOn5LIaWF_V1LPl0nrB22VxqcIGyQQHkTmwiuVcDK26RHJnW05uWIkb0rlHRy4ePtquVwEwQoE2yZCOgRxWzrADcSqJFdl5MtmXTi1pMLW34V3uqbPfFZiCLopsjxgdVDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNaoLG7kPbnqsvq6BBqAgsxw3av0GYqlAdmmu2nR174f3RTT3gn7UoeCT6ty-7v_ecHYVCX__nDDtXzVBNNaMgDLn9Z1QtJEDLl8HJuhibNAB9WFEawPwUkHo7KaEl_joJV7OtXt_jqNzOASz7eXqj4uQGxqodBqCByDZdxUOrCrew6Lg_EuqeYxveQde2_8uSnSYJFuT0ICDfs-RvZkzXP8iWLk8AGFvbPRZZaG-oAWYXT60MFcnAAzgKigk1Ks7ZUFBUmu8kREIkahFuSo4TQv-06OZuI8hxEQTctJrERYPibeAssySDX3uh3kUAClQLNsePY4qaK1ZU6jnaQ31g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ztzyo3lFAxGnJccBXGZCXp_3ChDLHoE1MiqIdfahk85wvaX592z8WMR4w17RVK0bJlsKzwgW6kBTsqtGKwx94-qjoIBpF6zJy5X-oLPdFb-bAIuYjHwhDKN2tKtQmQbjdfLf4jDzGzb-2DTrFI4LqQbuTa_0CPjvaAis9xa4sObtEHuBzcMEiWLgDLceORsrvz7s957P4-wxuri0qj39wfj-kqwqq_H2MZ11nNTkA7scnAxJYSCLwsbXI7GY6qPLXHUsFl7B0y0lvCr8AeV_SwsYMG2YwBWDqsLc2nel27pR3PagI77HZQOs4TGIP14xlD7vl9pRdiSYJYJuQSl6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=bq1183X25gwPNknjglDytIHVagfDFlzb4JCM-QMxZDeCTj6Ls8w0Bp7JPc5bCvpcz-pLbk0yYUkbQtSv_UXowWK3-000HYEXP2f-6O6Ffglur5iAX-_UGfJSkl8nVevcNPtwpURkOKZiFVvcrTL_Bme2iGcTqInifyhtD_0FTS7BLC10kpcNhTh4LLFa1FLzHAO80LXFve09hGvd2mi_vGFnXPlOJWkltF7k8OIDLLtzp-X7G6BHxyk0MkW9ioxi29LfXe9Kt2Z0MTxuV4QF8EfOelnIgq0RoUj1MJAmuMS9jw4R9wfoib_fESqPPexUGZ3dQqjI4eB3XUEnDfD8gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=bq1183X25gwPNknjglDytIHVagfDFlzb4JCM-QMxZDeCTj6Ls8w0Bp7JPc5bCvpcz-pLbk0yYUkbQtSv_UXowWK3-000HYEXP2f-6O6Ffglur5iAX-_UGfJSkl8nVevcNPtwpURkOKZiFVvcrTL_Bme2iGcTqInifyhtD_0FTS7BLC10kpcNhTh4LLFa1FLzHAO80LXFve09hGvd2mi_vGFnXPlOJWkltF7k8OIDLLtzp-X7G6BHxyk0MkW9ioxi29LfXe9Kt2Z0MTxuV4QF8EfOelnIgq0RoUj1MJAmuMS9jw4R9wfoib_fESqPPexUGZ3dQqjI4eB3XUEnDfD8gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL-h50Sie69E69F2gmb2JwedP2priYyOKwkGVh6f8uqKZVD04BfnBVd2lkw7UVIYf19VsEfk6F5ArLsN134kawqb_qBHUgz8w7lUakHfMAInHExDvwk6W8igNV3dUEMwqJJ21x2CHebteOQydIas3piISb-DMQJFWKfifLwJ5ndJOoS9zjZvPlgG3bcE-kB70cfAVhcnR3fqcmx8BMJkGcCYDwETH7Weq7A1omzLT5m6wuOvRKNRkGxOA_N3WbOIMCfyH8eb8yEl_lQah8xH6W88d7SekzNT6sK6Foc67dEy32yYpsK3aMiZ3rxIH1VP6R_pdgCGOJQGnw1pT-NVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJNcsGb9EugYQ0aj8fS3FjcMXxD2coriXht4IhZ3dbOhIxaRuOKsT5Uz-Z1ZIHLcsbcWr6NskcU9Avu_LP-j9xuRorHEasXxSGxUudvtlqMdSo7ugIKssuRwb5fGairFO2ed7mroyL8nK2vbnSv7VNAIlCGBqxC6PSQtbhpwl3TwHck1HLhWuginrHtvYqqLdjkVQWifk34bX1nPbKtoIsjtwa8JNk1BWf-4fj_OMOajorG5amGi1x4IW61PK0syYgu_rqTYidhEiLkN_aCQrOe0bTGHsKAcZDcU1fJE__ducjbB4-9JOKRr1gxhVO0rR9GwNj8-pLNHJXXq5_D1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkmWdIwyE8U6_TVtpzQzyhBvitPSgEqza3A4xAM-hyqLkBjYh8klIerb00gRHzmGQdSCp9PvxA_bnrWtXwf3rhLP9q550FoFG0ub7yz7vL1JvYMPb9fobujXls9bfgxjKEH-j_10t9djpCv1JSVp0OC3BRmP4-OA2B9uRoSpCLY_E1lHEB0TmvsiNcm59Q672LpWH9gPiSlpqe92ol8aNxHLnA2fYR7iu9chc2H5C0OEfHE3cYeduVVagTlG2kKCYD2Cq2cuE3uaIsLG6_1AB8Z_vKKJKgoiM0_qUZwNLCm9-WC8kDS9IZJaHvTPrFPsAjxUWqujpICHDku5_e8nMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Z_xbmp9a2FSkBb5rU-zeOv2FaV0bQRhqiAPngBHRO4aA_N4R_8AknRTzZUL3oF_cYK9aaVJXX3g-iOsactyyl9hmvG8sOOi_SJ7dk0fc8uhuMu93nHbPaogIhlfZ5BdQlP639qtcVc45d2Du4syReIQqaBRIpCHEOVb8PeBsft9SnyB_INYFakTB9j1jDcpIS9t4Qu1cEcRSkO8brAWE8bYE6R0pvN42_HR8iflhhX45KVo3ExdeC3g6P12UJC1U5xCPv9Go7z4MOb6ddZSciTFSyTxnnuuyoftbwRcE0U2oHzxqWTQPUZRZu0sWzgndErAS2yhN1znbnWfbA9gHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Z_xbmp9a2FSkBb5rU-zeOv2FaV0bQRhqiAPngBHRO4aA_N4R_8AknRTzZUL3oF_cYK9aaVJXX3g-iOsactyyl9hmvG8sOOi_SJ7dk0fc8uhuMu93nHbPaogIhlfZ5BdQlP639qtcVc45d2Du4syReIQqaBRIpCHEOVb8PeBsft9SnyB_INYFakTB9j1jDcpIS9t4Qu1cEcRSkO8brAWE8bYE6R0pvN42_HR8iflhhX45KVo3ExdeC3g6P12UJC1U5xCPv9Go7z4MOb6ddZSciTFSyTxnnuuyoftbwRcE0U2oHzxqWTQPUZRZu0sWzgndErAS2yhN1znbnWfbA9gHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SwcAgXqcD7KLuETmVZ5f2hx2Qtk9IBa4EtZrZa90MBaTqmCKuozg4lxwPoyIBD9Um8izNLIZTBl_oDIhd88YGz9is6EbUfoftXtlm8scwZdnj-6cgLkTH1Bs1kF-PAcQWUQCfX8h6ZFovhOmds56sOp4oMIIz5v8Wd_nF3i2HSMcjy697YN9LteYCDzeOFuDy89kXxR5E1P1gwIs7yG1zYvpoFiQl0c0EiBVTaC2RczESC0gtvyfEnqMUEnrJhLoEEX5nXL3GRqJIjo2ksFPjjB7TbPmkBL-GNGYOCoy4e10VyMSO9nVe1JHKPB3PlXqmEB7gvCf6qVH2LxRA_SMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SwcAgXqcD7KLuETmVZ5f2hx2Qtk9IBa4EtZrZa90MBaTqmCKuozg4lxwPoyIBD9Um8izNLIZTBl_oDIhd88YGz9is6EbUfoftXtlm8scwZdnj-6cgLkTH1Bs1kF-PAcQWUQCfX8h6ZFovhOmds56sOp4oMIIz5v8Wd_nF3i2HSMcjy697YN9LteYCDzeOFuDy89kXxR5E1P1gwIs7yG1zYvpoFiQl0c0EiBVTaC2RczESC0gtvyfEnqMUEnrJhLoEEX5nXL3GRqJIjo2ksFPjjB7TbPmkBL-GNGYOCoy4e10VyMSO9nVe1JHKPB3PlXqmEB7gvCf6qVH2LxRA_SMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=cPRs_Uzdvwd0BK2lEIeiPuC8GsUw6O9bAw31LohUVdsvdlWKyiSSKZhLO8T94vRDSyMlfpIlG2vGStcHeNNiOAdeMrOfvDd6Ql3MB_ZI_VFZWuHNEBC2MDEh9OyA4_2lZ-p_NdJEJXtsSjje0LLR-uw2iM25bSe8cQh76dC9yeQ0KMILvpamMy-M5l_wI-WJrCuHoJbUAi4SWYR6f7Dz5tA1lndXMy8zGoELB5TZrgodXsE6CZYP4pD4wE3z3MVfasvdEFfKbXTf7y6Bo42RetQs22zA3-t2LKYnOpxBkZqGsqvGB2Yl6orTBsYI6TexZ6zNDq4ZPRQBE9eNSYiAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=cPRs_Uzdvwd0BK2lEIeiPuC8GsUw6O9bAw31LohUVdsvdlWKyiSSKZhLO8T94vRDSyMlfpIlG2vGStcHeNNiOAdeMrOfvDd6Ql3MB_ZI_VFZWuHNEBC2MDEh9OyA4_2lZ-p_NdJEJXtsSjje0LLR-uw2iM25bSe8cQh76dC9yeQ0KMILvpamMy-M5l_wI-WJrCuHoJbUAi4SWYR6f7Dz5tA1lndXMy8zGoELB5TZrgodXsE6CZYP4pD4wE3z3MVfasvdEFfKbXTf7y6Bo42RetQs22zA3-t2LKYnOpxBkZqGsqvGB2Yl6orTBsYI6TexZ6zNDq4ZPRQBE9eNSYiAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV8IQqLUSvJDciryEMw1WjZwtDYvCp8UwqMusFdDeLtjGq5potCxtbhke2krJTkyBL5iE9Ts2DLc17UqZYJSZ1XFTNH9yavK4fAa2fnOrgkVlmkRdZu1az7JGV7sTeklD0Trwu3OUy8ivHVtlafUt4fZ2Ro4TIcnyxsm2ZWlXs5Mtlw0vJ0SqScuSQc6RhyF7y_75I8Z8woyLPKtm8lTKh9Mc5uRYRVpsCRhJiedrGV9ao5iUTiOGHvTjjuBVNDoUAcVyfLN-ZR1RiWBI6WENA2-RcnjEBP5Ws13q1uystAORcotW2FLCIU-NTSr7_iPh7912ruJOKFjAOytolbQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBPXs_GZ8CRSd2eAI4PiQ7iAQkzY4OdxOdvAs8UgFBLD0yjLdg9VSbTsp2XQbiK6WUEruKnkZ0Tyaf9oNkfgg6dKBTZgozNZIjC1enVNmb32KoT47yTfDdnmEJp6ZHsxQlHLMjA-TJSsaTJvM2E_yVOwFB6G7AcT2m_dt2JfSzWez_A4T_LNipg3iOA8bCHBEXYZgZ8xQ-KSqpKNBjzbY8uiQX3XspI0oyP7G85o3uIoz7SjE7kXD_P0Gy9Fnv_8UTHBc1aA4W4Gp2DC8BmFVyVXLafvk8-7CIUkftg0cW5-_p9V4-Oyj1PbWM8uF1uivCp4fCVeZbDGnqdXxZBXfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNT8gpDvFwzyzlEEojSOnDwyPgj-JmOM5iufqdd3QIUsW-1OXefoSfzLlkYwd4O5v5HilD__OSbn0V2_lRE76aFtsD2kCiWm_oqHoTTIARECbL4sl2suZ1nElR2W2vqid3ALVgwtH5v5dlK_LXOymkT-hjdZW0ZEiL3wKNiB-e0cACRJzyiLBw7_IQgd7BioEFLt5W1nxvJ2yirpJihFmL3ZNd-KpdKDsAMTAKFvDo-m8CFgOGIhoeTG81oqg0b990tWDdaHnoCoQT8DJlDhSrGKScrGCTm61InNzFCLN7aDg5pAi0_Q7zjauTaQ12Jw7IUcjMFceBTAjCWgHJ82kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBcLXz4ONbxbDts0Mwdc2VTPDv9KD9whnfl18rwpdXb7911hSEoo5Bx6AM78epArtcpzkdxBFQtWZp86oRycwlRJSqbSicTZjcVHFM5fp2Jmj_ljeA9oyuZgivDI6VLB8paKcyR9_R_mhQy7ZLCmV2b_NVqKf5-NBWiViahDuySovT1zzao1epw8Ny1nNUyLu5s-bzmBZM4ZwxvNuTgPxM0gxYOBEcy6QnHB5Jif4SwbwoSmEYNiWMOiIvXIaGs_GvpIAjB310zStfNjbcXn-FJtlw2kIP-me5i79nohY7JZKUr-H8a9U13JL1m23To6XysO1959egKGmPL3ZRpc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flJPrt-ZWVhAKW75Xxtu340H-18bca4RShCQzLSNbUGv9FFPE8vwpOJ8FiCwqNBapobB4GOAYrdEWjPSohIoI0asDyvXwaGSLr-NFqpEPssLiMib-MYBRzxg4OflZc2GWZ7OknhH9qlwlIb2-4LG4FQsZKhPOtlDdgwRkLrEQOjGpu8k1JcDSLac-jaTCULlauU65j7FbgIGg1KRM8tvIPMXx9ZmB7tKwxYhyDOBYrJTRckV74eCEI2qkNi0onKAEHcx2hZIVb5Ut0hIAsvu1mMEPWY7ojDqFh_cH2ZrU35toB9wWhD1b01_nn3uIiMNvsdqF3Wk3lgdHec-w2L-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viHaF_Wn28JtU8Ky4-8bpSsN99w0NkEuO9aa8E6hdrCoUqTJ21kBfVPLH-b6cOUkjxSnZtOtxWd6Ud9Hp2ExC7afyaOrjEBGZ_RUW9ry7z6-hnawG72E5rbi7RG44xuUDJY0-u9QSKfj7ulOvrD2iDIO2LdsTVAYvAj8MHN9JrdkHqexd3WDsHn5R28nKZrUs7I_kuJvX2Y4TD4i40Wi6GXTy-FIOi9YenWNtXnPi7HX26XAVSuBzMYbT2jYDLe7gulfRNmOlScyRPjDS1LoLoN-KewvxIKkxugUVmviUe2UInBKSh-ov6qsc1ZDaU93j3IRPD3j7dTRPIUmScovgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyDLzjHFD5EQnCoKrcX1aFyKc6y3E9s0fBoQ8gZaOMAQHn9pMiE-wdAajVrpNTvo6duAcCeCaf5GqIjyheJeId-iJQXgrV3hPaNAjKowzGioAX6HprZuyfCGxSOXQiojgGniyRoI-jWdUjt1dLI9AYSkqHVPMjgg-yquxjgGW0Q1zwhjJ8_s5LPIF9Qupfx-NNEHjbqYijxR9QwSSu8C7uBaSjf9VM6DPeeX81YnkEf_QRtsc8u-5v6rX7RieJRG5qbghqk-lHz9BK7F2CjQDcPSe_P11xUZdbABRIZAZmpHb7bnQFit50bnCei7sGGI2zVuSF7q3YOP6pUzhtzlUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZtCpeJKiLy6vcwFRlOsV--d1csp7O5-itWE49g8lQBmtkNAc1W_sn1fFJ8r67gNZoIVl6eZmTkpSa8V6_2Qe5s0r9t2H20RYFZUGxpluDkJQJdk0vletDmYnJK22d0RqJgFspCFCvYGrnV7cBL3krtwTsA2QIH7I103GUVugUHb36KZa13hxydR7oes5w8G94YoYTYfkzjv5Q2YvYRjLi6A1t571mOa-8vxoqmSG_0BGlK4etKp5pkEO7ZoEjNTchC5kBvoj5pLgL-W0y4BNCEOyf30SZaeqf6EnYgkAMWIV5ibrz-d0-7Cywwph7MzTrGGdU2779IWF3MZ3Jia3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBg0gj7Tl19PY8h3Al6U5XtYnxUFWGfjHCtTRJLjtRxS76WfHKYAC_SElSu4fZnxGhufqdRtnjYFsc3qQLOrvOT4koSCA2s-oxFXaxUdxOGZb42nIfYbFMyFaaAxE2BomPKIKabK9anQtev0SdZ-u7upRzdJ9psptQRV7DRoMKzxltPScMUI3hFMkO37PSNFMDpZZo7HjO2WHw6nHK4v5sNC0BsU_6_w22xyTe6BArmWfHAVYu4kVAfI1RpjNayxlW0FbjPgaKCU0XUOkO_IxpkdgDterAl5jaTtL4LhHEADro2lEgd1DlH5Dhx1W0qxEATNeBy6rdvkiqyjvFWmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzj-AVE2t2MUOk8VLQ0c5cfKqYKnHj5q8pwYOsTxyXHeOgGjM-CgnH4Ge6nohcvsTWVAQ13F13VkA4QZuQ1887Jpssk2of1FjUU4EIe2JgDb_BE5OoLbOQOsWUmrXtt3rjFUmqGLyEJP9KZoOw_RCBD2hsfAIjkz8LmAGO2kdehVszyWsUr5R6i0VsPyA0bVYJg6JpsxNEfjM8W9hFunha9gWUNrIRGfNh3xnFO4tMty2yNQuw3-ut_gquIynDqEmbdL9Bb-_QUuFZqr9KRMce-KR-mxyYficOhLZs0OsolqKxKytwl4qTfr2Pat9eceDtuCR4FS3qWS_IfQPuHIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqBqrlVYt51uKMbTcwb3PGbUrtmzsDcJeUEVtAhHde_xoX63uPJzKAtwz3qPbdu8Q7Pjb2L0a9aoAs0W5OAvZSRhKuvyNODl4tjycCiPopnJRCBiWlH01dL1IhL1oXHeRymzopGLyfsTmTNsA7zpUG9AFIg9jYZt_BRl_P4rw2BuzvcyUTojrhYTIpRynJZV1QP6fujuZWB3zqY8ypg2gHOXX01daE1dZpx88IqIMSnWmSzTSJ_FJUkEVl3pKmIQDNV6RS7IcGwHwUNpTq5mE0TG529zSd2mnPwbLdc1j6A40KbofUy-BpLFdX-vjMlU7KFN8lsssqPpsNTCPdzj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2BaoaqrDiBHSfiU18AAFIGmLwY4nhkjJEU8T9LUymNEXFo73jD5V3i-D79X4sANJiagSZHes4fuYW_K-4goNgafSwqMcvDsIH1PmhcPLpMcskU8OfLh6JX_lNzuiLv95jcs2jRNbNADEpbLWY9IQena3u124Q4AqWI-EKFdTNH_gWA7e7RMHXhNYGpIX64hY_31dK6QWqnAlHNdkWxP5WTeW0t_NYYtUUKNLYkOomycMmwmYPAY5eVC7uBQNEYd-qsGFAhPEVYEQDdVFGy9GZpYMLqdEnIanZwDfkSn2CZfMKhznxnJnth7jp3D41XFbpchBG2F5i9EHBWvtHn37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1L5DOfC0QZeTDHQgJ3c8bYfbGyk08Ng9DyLcmswGdP8UU87yLwEnHyykFN5L1wsI5vyCX1jiHNv1FqRbQXVyQH03nTQRuWxLbCZU1M5cr0xS-pBofUOtVyIPwXNH4Ojt756waFnPWFks-8xuFLDdeVNxRo8B_05gQzfTGEKwLHEtoCpadjE2CzRXDKVNDdp31Yz6U6MOWV3gfbSmN3nfjAHk923nZNNUa-UP40tNb-6W8GHfBlEjBpBp2VksRbEmqejAiholSJQRk95wMjFBthID0f-n6xXcrXV2XthcOb4lRKu5j5iPItzwyyqMQhN_7ka6H8DfeXQJ8dN_Vy9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGjofrWUYZMsKPQqbtdIAozGb__iGtobadhvwbS9OtQmJBe6iKDaQMrJlagGmKA7Alxf9LtehFum2uS5A5I-Ghqu9rj1rW0PCmIV9BUlZtjOtk0u3PwkLed2bvpZ4CJG3GViAbplgUQPWDnpsCB0k6ahsWjCsP9BAxKr8U3Y0HFPnepW4xXlsrWa5J9pcK2au3dThLa1xKFtUNeD7dhrC7IRVHw198mqHcZ_Lc4G5Qnar_Rt9wa6tRhfsu5FzrBbZlGMNNnKMQisNnVOqigFMIWpI6fbq8NQAi-3toTo-4WbDBv-ksozy-uFGHoRIcGyVvTXJM1MxRdzxYxAzJsTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzE8CCPBPa_EuTXlH3iebZHwUDUIXZqm7QsX37f4yMIcvyCbmjrXy5sLa-eMspIynjRnjE_OESXTxnLP3rBuP2c4HOBSsXtfsQmI3RS5KIRsjT0KamT8E3_L4NgHYL9gTrW3-Am8UyDbaf_3RkFMad-hAMZCHFT35_huBuYqDJgYIYaCY2VsV3deF9XXx8gmVIkQms8hozeiACpoec69AIH4npVIivLyV7pdOjgHfuN6YngY2HYh5S9xjXcW-MZXUfOouAdQk8Km6fXFbiozXFzn-eV1eUbERroJyJOUpANOqw-uA8w9Z0rq0YESuXPXam1TStUyi87LutdSLErFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SGNM0KbQtZOCHoENvzjhm73XnHh7nopkOv4pd_xvRMUy0NBz7-B8Ft7OHzw2PErzTxwV-Sr_cMaucXbzLRrPbe8DZqEsbyqqjLd0PevJMQuWHsRuModNotfNAt2p2xI3TgCzIoz4noRy9LJGg7aURKYEG5S_ccb834QeVeT717coWi4Rq5CJbn9vle7puSHF-SM40J-pcjGu08ZrFGrNY37Npcy799buGJ8H_jDO9Lrk78umVqqQGKLujLDGml1zBJ4ArSbQlzffi-i0tfdzNvhBSyKfpBkY0qheCa-VC3Dc06VSkrpFyH1kRcD0qsrjyX_atHkXK48UCv8x0rd2jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SGNM0KbQtZOCHoENvzjhm73XnHh7nopkOv4pd_xvRMUy0NBz7-B8Ft7OHzw2PErzTxwV-Sr_cMaucXbzLRrPbe8DZqEsbyqqjLd0PevJMQuWHsRuModNotfNAt2p2xI3TgCzIoz4noRy9LJGg7aURKYEG5S_ccb834QeVeT717coWi4Rq5CJbn9vle7puSHF-SM40J-pcjGu08ZrFGrNY37Npcy799buGJ8H_jDO9Lrk78umVqqQGKLujLDGml1zBJ4ArSbQlzffi-i0tfdzNvhBSyKfpBkY0qheCa-VC3Dc06VSkrpFyH1kRcD0qsrjyX_atHkXK48UCv8x0rd2jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMVTXkyiGs10t3SWoxDv5b_VUCovFUkkJSlMEPfbpO-ShrcENughif821vGKeSqcR4vT542-5H1-RqGyK86VRGqy9kA6g4stAr2UZDkZq6FqPt9KschWKXxVFAx7MvGwAiCmGPuaRt1bPSN9b7L1jdvRqe04-xgcStLLZqLSjWUf-hHAVT4llvg8f30zhRgCCPPmlLPlrZiGSKKM4I4hRgCCStMsx9thIopUlCs5lujKcE_KwzUDJxcjQNN1mM8FQWJ3Y7QnDDkC4NrZkrJVBhQvS3kCD1w5YXjYScp-vjcggGq-LyQONun1q4koSzAd5H-zhL4JNcUzK6_ba3pYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=Hqbak-K9CzdgIgSluWlXD6S1EokoNn5Q9UEZ3kps8oAuTJijuTeN_q8fkH2dtmwIa74N-a8hdUxJX-PCz1KgpEM1VGbgf7QOs6QuAwMC75iBnTgpyN0qoeQdTUzxOkxRX0hjpFMBDJczz63zruSlLNISCF6eonp8Fyekb6qon8NRCo9h06sGPnBUC1xtmlF8p8FTAh6j6fSuBDni164TPgCPa4OMVCzy3O5jqvnhaHzrCZlY3vBTllMa2KwH6f1OtIGSrIC7LhRWk2Pj2awM4RA7QZt5_RDbsrhndsMDRY2f_w6eCaAfn7-JheuHFCqNpHM7EX8deZraVlxm__HlmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=Hqbak-K9CzdgIgSluWlXD6S1EokoNn5Q9UEZ3kps8oAuTJijuTeN_q8fkH2dtmwIa74N-a8hdUxJX-PCz1KgpEM1VGbgf7QOs6QuAwMC75iBnTgpyN0qoeQdTUzxOkxRX0hjpFMBDJczz63zruSlLNISCF6eonp8Fyekb6qon8NRCo9h06sGPnBUC1xtmlF8p8FTAh6j6fSuBDni164TPgCPa4OMVCzy3O5jqvnhaHzrCZlY3vBTllMa2KwH6f1OtIGSrIC7LhRWk2Pj2awM4RA7QZt5_RDbsrhndsMDRY2f_w6eCaAfn7-JheuHFCqNpHM7EX8deZraVlxm__HlmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=AG4etvY31z1J-pjnDUWh9pfVBPBYJaChvLCpIiBJyfHWVDc7dMn3zBx4Oy2MB3K0h3hLDh251QpTNSonA80pxAarn98q3nTnJPO2nNj383KcQ6DsXMtKUkXNME2b4R5Rbhtn84RU6YkcbTB7RtRhnJvTMrHvtLo3qh1CbAjBJ-NoFP7l_gA3oDGeSjDJ8B_0D_JxVAKYb448yK9_TZa59HD5IlDD4G1fXl1-P8Id-dap0cMLgLlk9ysHvZ2nFicHcX8fIbNKi6SLf5GOIs979g2Xoqg2E497RURrnzcBnv_IXgnRrwqR25Fr146GYvBQEOYI5RHafKIh0eLxBUWdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=AG4etvY31z1J-pjnDUWh9pfVBPBYJaChvLCpIiBJyfHWVDc7dMn3zBx4Oy2MB3K0h3hLDh251QpTNSonA80pxAarn98q3nTnJPO2nNj383KcQ6DsXMtKUkXNME2b4R5Rbhtn84RU6YkcbTB7RtRhnJvTMrHvtLo3qh1CbAjBJ-NoFP7l_gA3oDGeSjDJ8B_0D_JxVAKYb448yK9_TZa59HD5IlDD4G1fXl1-P8Id-dap0cMLgLlk9ysHvZ2nFicHcX8fIbNKi6SLf5GOIs979g2Xoqg2E497RURrnzcBnv_IXgnRrwqR25Fr146GYvBQEOYI5RHafKIh0eLxBUWdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOmwbCgxFZ94i9BSVjrGCM1x7A6SO7AnwHfJpoRewGKzL_mCQj4VL3ln1POwDTB6sAR6wav2rIoFE4WT4vxA-H259mWbVpVUTMQ7lUsd1iCllTYhmA_z2i1RbWWq48exmx8SF1LoN_tiaLb3Qrunzp6eqNnTZw9K4mLmZvW3P46QBPrypgSVs3c4BQw1BOJouz8M5BA9qPIH1374Q-80nX7rDKu8SuGcdQ3Mq3CUFxBisQh_N3la-QoAjQq47VXbQnR-XTJEcd9V8DJI2EMZXvEnkRn6MDns-rkdIG1niuLFDPs5gN_Fh8RyjOCjmGfJ5WzfRQYfJZneeaNPiNiKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=n1TRHdIk9X8HhGG7eSRhXyFglKeItN4Btn1S1t7XNQfJeyGIeTrBLyVgBIAF1_R0MUpsr8MQa1mQB0w29_Xi3VPWWH1dl9MsUYtff1jMWIcDlMkrH5v8fwP_Q21fqHCegMGMnBLb8O_lrInPvq1wu4UdxXYzH8xfWR7fsnL5q6IbooYmLIJlC6n0swFoG7lyVtMfwa_vMBRDqkNNHmavFUwxYg2SXhgJWERRny1naTj0q7f4hpa7_GqAF1evyIT6Or62WSDugAX2Bo5TmLyQLkauhj8-U0bKrjlXiGtbyPCnKKKNujQjWwG-9Ih_oDsqsdNPJ_iIQsrdI8QffFmm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=n1TRHdIk9X8HhGG7eSRhXyFglKeItN4Btn1S1t7XNQfJeyGIeTrBLyVgBIAF1_R0MUpsr8MQa1mQB0w29_Xi3VPWWH1dl9MsUYtff1jMWIcDlMkrH5v8fwP_Q21fqHCegMGMnBLb8O_lrInPvq1wu4UdxXYzH8xfWR7fsnL5q6IbooYmLIJlC6n0swFoG7lyVtMfwa_vMBRDqkNNHmavFUwxYg2SXhgJWERRny1naTj0q7f4hpa7_GqAF1evyIT6Or62WSDugAX2Bo5TmLyQLkauhj8-U0bKrjlXiGtbyPCnKKKNujQjWwG-9Ih_oDsqsdNPJ_iIQsrdI8QffFmm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl9QJUjn2ssxI3AfADSslRzvQ7trgVvXnEFDdPEZtCYwO7HidKIf-W4muA4irrqClLGSXUkl_Zz0wCcWAFYWZCZdEPSA5-UMI5TDunWMTBXvxw_5jPzPVaSJJNDNjb6ygtWDVo20kbX_OjZfaKH4n13NIDq81Y9LhabWdtAejwdnzaohJcHjRSVh0NLbLL3KzonDZbevP9E_b_5ACD1MWsymAYLKX2wwW0EqCWsrggilD4PpNmtGpZ_pnfrHq2J7wJESkY8V6BjVMAX1uS8ZNEZ5fcBjhMe3v6HVkRjRXe8ScOrq-KTmkMFfGDyBz_RAOOleWwElqwt_jYhV1T1G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBknHb4wAJV_rg4IlnAIejCZaVUYy-WbCdpTVvNNGWhuzubgeDJxIs3Kt8s_lDGkSM1F9dccUZwLgQGf-LX1htqNnsJIvxayIq1s4uBxVwWgSnwwP2C-aLBS90y1UuGXs_4E1AH6rW-hiN8vCeKdFBCVYooz6Ppt-lF_Ykf7P97LMkKfA19k2O0cLO3VHQbn9A60a85VnozxpwAfsxvbgLt2E-OQ2mBZuM4w-KaBvDm72eeBfNl8fZXbuiosvWdYUjXslyA9Bu-V2VfJQMboTSrW0ZvLpnl5C51NLkB2dUBX-XyM7yasEqK78hy-KmpcgjxGo3bJ5LqQEmUeAQt6sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPwtEgU13NfTDjcZkOiBs2RGNvufq8KKDMrDgPSI0nF4CpGO6HOG9cKY9z5ub04HuDQBT-S31wCZcyIuxpGncluUGLqh-Sbeeqo__QWMofKMf0-1KZTHkivw76c7eunDJFZ74VZF3mlz9g5_3Gv72ipFOA6LfY695t1Ke3ugMHPkf5MVB7rs87030Bryn7kXyNSmNAwNzYSXYSsSbAz4kLR3Fv24d4gXmz8rJtIPYezaIqYTXkkygfcbtYVj2YNW4bmg6yfb6W8oyetOBgYeemtLm7LLcy4h51s_ILm-yUV4tCtP7hkQMXvxWl9dVNwarCqAe5V96GpFrCYvECNZ4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCpRA6TyvtnYnjIHPtxPDrr2NigPc0YGBv6hL7bd6HJQ48OLvBZ5i2W8_fnUCG8uRNU3plp1qETRaEHuj1LlNs6bcYI9fsVzrIbK19vxWGS8siCIrncXmncQQfREjEeKzFIgbUbPpW8P1sycx-a8ho_2_LvCdM_Zt-nKlntBuKbohA4NnDnKk94ziJxE8H1Yqd6eF3etbQbk6l5vJ13m6uXKReMOldU4u6urJIpiAY-EwfzkAoBgpO_yIwSpJl3WPWgnFa6JyYAqqWbQGQ_XI39z5YyNBoE2XRWq2NeeFYphrazBtp_qoxqQqWSMZxBSZVCNS0x8ldYk7LcT_YourA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vPdWTVG_Ip3ygwTJ2TblMphuwxmBTHYds3xA42nDWPB6mEDVyevyheWrK8BQ08bdslkXpI7X7MCOK_Jj2anK0qwCNikWe8tsppkEQKYeOn8C5NUkiUaDkOq4xoFT8RsKaWj2tmyNv_NwSH_KGypdcLGAniDrDkT8UZCxTw8uJWp988lcX4WujSKSuyr2tLA4HWgGefZnlgQZyUAcKDrXzNcKxes7aOIF-6WMQWvMFEhHqjw3aU1SXlu3sGDbC7sD4_7Mp_JH03H9X_9qBHmL4iueEbRvbvZEwv0scXR3O3kAZRkjfxTXJdpr6bCQnGN-BMr2DuBXfQ2Tn9ZXK2zLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vPdWTVG_Ip3ygwTJ2TblMphuwxmBTHYds3xA42nDWPB6mEDVyevyheWrK8BQ08bdslkXpI7X7MCOK_Jj2anK0qwCNikWe8tsppkEQKYeOn8C5NUkiUaDkOq4xoFT8RsKaWj2tmyNv_NwSH_KGypdcLGAniDrDkT8UZCxTw8uJWp988lcX4WujSKSuyr2tLA4HWgGefZnlgQZyUAcKDrXzNcKxes7aOIF-6WMQWvMFEhHqjw3aU1SXlu3sGDbC7sD4_7Mp_JH03H9X_9qBHmL4iueEbRvbvZEwv0scXR3O3kAZRkjfxTXJdpr6bCQnGN-BMr2DuBXfQ2Tn9ZXK2zLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=TJkPwiJfyv_qkyBRO9KHSYJVwsfj-nXLyVHeOspYXqv95t2BJG2DYzVyhG5EA5-EJ_OJmi-TFsXY3Vp_VqsncnGw3CB-7NmMlMpuvQeWMgiMrtNm2rx2dhwwNjitzrO2M_EIz_KNLJrYphFqgT5rFcd2qVerRPKHhVnaaO08Br_mJ4wTyHIMNtX3BI7lM1OWzjV7u4TTzvgfnBqZSGrF3QOtsW5CQelP3Oz5o-_HqxfxJioFg-wftsP9UTC9_LPoSrS04q1syWHTcC4LOYGaIyRORSu--K84J8cemSJMV8HFpfika4orwTXQdFZo9Ns246Fo7hxlpyWBmSO3suv8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=TJkPwiJfyv_qkyBRO9KHSYJVwsfj-nXLyVHeOspYXqv95t2BJG2DYzVyhG5EA5-EJ_OJmi-TFsXY3Vp_VqsncnGw3CB-7NmMlMpuvQeWMgiMrtNm2rx2dhwwNjitzrO2M_EIz_KNLJrYphFqgT5rFcd2qVerRPKHhVnaaO08Br_mJ4wTyHIMNtX3BI7lM1OWzjV7u4TTzvgfnBqZSGrF3QOtsW5CQelP3Oz5o-_HqxfxJioFg-wftsP9UTC9_LPoSrS04q1syWHTcC4LOYGaIyRORSu--K84J8cemSJMV8HFpfika4orwTXQdFZo9Ns246Fo7hxlpyWBmSO3suv8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=q-Gid6s4KOQaVpz-qcNT1Iu7-0mLdLjXoDDUY5QNdGNOnhgJsEoUC4vLhS4zkW03UueU6faNCfWV5WgN-5u98_DeFZc0lbNXQ5y-uKptpQh-lqWtk7raKKV8t82LSQ9-WtsUU8eC3_CVLcsIBaRPXznbbn9zKY6JQCI_UEGAIgH_msdOssOnL0QLKgn9_q01L5hXlr2S0SetlatsQ4OeXJbrQrgQk9P2qwLKO071ZJD4yuSCTnH2G1SGoKKaI5vQhcUKxm1rerZ0FpE7DwHNySRTJ4cmWjOh79T2946LmbUJx8h7zzFjUPLG5KWfTYFfYBozkCh7XXdCj8VUNFx2Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=q-Gid6s4KOQaVpz-qcNT1Iu7-0mLdLjXoDDUY5QNdGNOnhgJsEoUC4vLhS4zkW03UueU6faNCfWV5WgN-5u98_DeFZc0lbNXQ5y-uKptpQh-lqWtk7raKKV8t82LSQ9-WtsUU8eC3_CVLcsIBaRPXznbbn9zKY6JQCI_UEGAIgH_msdOssOnL0QLKgn9_q01L5hXlr2S0SetlatsQ4OeXJbrQrgQk9P2qwLKO071ZJD4yuSCTnH2G1SGoKKaI5vQhcUKxm1rerZ0FpE7DwHNySRTJ4cmWjOh79T2946LmbUJx8h7zzFjUPLG5KWfTYFfYBozkCh7XXdCj8VUNFx2Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qAo7uUkdPCQe9jHPyKiiLVnNjq6alWhgWSmqLcHRYUpbUy8phv3SDxaizrzpExgG5mZK8K56qIa_SSo0icIEihiYYJbRxkyCNalZC6_0AtwDR-O40FRJVa2wByEkOFBKXiEhNJd5hj58lLnPkuoytbPxf_hfat8SKLAzpZPAqSP0TMyg5T-ipPmYyZIUSPiCgV2q0llCsVnmxYSjv318Ub_Oz2rfc9Ti1YyYOjwkjGrGlEU-mWdbbYlAXhAWOfEF2IKmMiNjli4RmuYKQh-FsnOIJ5IYdDHuF1tAjaT_Pvwqs1DU7MsG72gmby2ymAZRm1h0VSt7KWpLUwgLr8nQcwpdFUDF3rK4v2_IF1P0TFH1Gw2cvWdZXglnl4hbpBmNamKybmCjbyYqjyIJKA6rteZf4tuNKvS_iIhKDdK-QmSmRSmartNEgRjhRy0aKKZhI_1WzSK49XAtFfmeb31pz_F8yfWNxQa4mzsSZGi8WZl-5WTlig8YudHwodVL5sb37s_bQUB2CIbtZyC4-fx6s9r587fY8VT-cERiNDqKbeWU1nihe0W5bNp3DSysGKtNIjZ2zSU5fF7l8MTfGZHrX68saZJhE_RHeXBlIZ_AjY-fZGq2c3tFZGq5-62FjPtdXyc-0JbOkwj--u1HKJD20xctYmQO5OrcpG4RXbRHjjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qAo7uUkdPCQe9jHPyKiiLVnNjq6alWhgWSmqLcHRYUpbUy8phv3SDxaizrzpExgG5mZK8K56qIa_SSo0icIEihiYYJbRxkyCNalZC6_0AtwDR-O40FRJVa2wByEkOFBKXiEhNJd5hj58lLnPkuoytbPxf_hfat8SKLAzpZPAqSP0TMyg5T-ipPmYyZIUSPiCgV2q0llCsVnmxYSjv318Ub_Oz2rfc9Ti1YyYOjwkjGrGlEU-mWdbbYlAXhAWOfEF2IKmMiNjli4RmuYKQh-FsnOIJ5IYdDHuF1tAjaT_Pvwqs1DU7MsG72gmby2ymAZRm1h0VSt7KWpLUwgLr8nQcwpdFUDF3rK4v2_IF1P0TFH1Gw2cvWdZXglnl4hbpBmNamKybmCjbyYqjyIJKA6rteZf4tuNKvS_iIhKDdK-QmSmRSmartNEgRjhRy0aKKZhI_1WzSK49XAtFfmeb31pz_F8yfWNxQa4mzsSZGi8WZl-5WTlig8YudHwodVL5sb37s_bQUB2CIbtZyC4-fx6s9r587fY8VT-cERiNDqKbeWU1nihe0W5bNp3DSysGKtNIjZ2zSU5fF7l8MTfGZHrX68saZJhE_RHeXBlIZ_AjY-fZGq2c3tFZGq5-62FjPtdXyc-0JbOkwj--u1HKJD20xctYmQO5OrcpG4RXbRHjjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=errHiHn1X2PS_JDm_niycWNT2ZAL9Qx4hpV9E1l1K6r3rFM-yO-arPsXJEqEUy4IhAhm7YDko5EGcYAYBS0zS16eEb8kauvllS7kdmtQ-nxBDvj-FM4SnFL1GONdy8qTyQJxiAYZCTWndHbo5UPpDSpjrO7CwBtmU543Rjo6UhbNQCr-DCoSlxOYcbbom7dj7LOTrNawk-tg6Fx562YoVQ0hLv2a5VzFQwBzM3-Ty8VNb2QPyC2vEzUU8HxHMN1RFMHYDkphALB0jSUKKLa3VqnMb4_CQ14L1RoT9rSjdx1adExpsu-FYmLCcoYiAvnQC3mXD4J3KXMtK4msREfiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=errHiHn1X2PS_JDm_niycWNT2ZAL9Qx4hpV9E1l1K6r3rFM-yO-arPsXJEqEUy4IhAhm7YDko5EGcYAYBS0zS16eEb8kauvllS7kdmtQ-nxBDvj-FM4SnFL1GONdy8qTyQJxiAYZCTWndHbo5UPpDSpjrO7CwBtmU543Rjo6UhbNQCr-DCoSlxOYcbbom7dj7LOTrNawk-tg6Fx562YoVQ0hLv2a5VzFQwBzM3-Ty8VNb2QPyC2vEzUU8HxHMN1RFMHYDkphALB0jSUKKLa3VqnMb4_CQ14L1RoT9rSjdx1adExpsu-FYmLCcoYiAvnQC3mXD4J3KXMtK4msREfiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ZMYQjqnKLuLDbYCOrEh9W5R2W5mzysrEpN3k0iaAzUd8Lo8g4mFnpx4pD8XkUS4NTIS4QuSYnQXcgQbUfdetGBaBltEvHGS9l1l3caSUqHxfsBmVlbv2Sr21lWKYy_vRRwb5thXgQz1yqw4_qTmSZ3cNoiNWtoArWXo-4KAN4jMQBz2i0cakzjgIUIj_7ow8jxwqR6EANk2_zZMg5uqaLV53E_evKxLP08z6HBThnnoGrTUniomR1pXFJ4rrs1lJBCCNk_mgyYU2rsJEuB_ZhiSAAKmSolM6E8kX8kodhjejyIgy5pmmegm4EhBg1HU8G_yl_QbTOlk52btgKr-FHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ZMYQjqnKLuLDbYCOrEh9W5R2W5mzysrEpN3k0iaAzUd8Lo8g4mFnpx4pD8XkUS4NTIS4QuSYnQXcgQbUfdetGBaBltEvHGS9l1l3caSUqHxfsBmVlbv2Sr21lWKYy_vRRwb5thXgQz1yqw4_qTmSZ3cNoiNWtoArWXo-4KAN4jMQBz2i0cakzjgIUIj_7ow8jxwqR6EANk2_zZMg5uqaLV53E_evKxLP08z6HBThnnoGrTUniomR1pXFJ4rrs1lJBCCNk_mgyYU2rsJEuB_ZhiSAAKmSolM6E8kX8kodhjejyIgy5pmmegm4EhBg1HU8G_yl_QbTOlk52btgKr-FHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB9inOZc-RWQNC9EuLiEP22npsDkg6XMgZyzgdZliM5GwIRXq-Kc_8aRtmFV_dL4YsddX6Dgp0SGqT2wDpf4kCD0VyDsRqrkhHmbjepTSb8FLaLgnuRTF704hr-NJP04TsZfWK5CE8HaHy3XFO9yX2klJhLBxnNzcKcBGysXfotzh--LkoUzADMImxsHkseE9DJgXWGpBaU9prVDO1vPZaXn7EfxhXyNFsmsn8YRl7t_FJC3GphuTT6UI9QGEtdAUw0Gxn0avfSPNR6b08tk5V7m6lHqcvegRh91ZMyennB4-8EhB5WEgdbJKvZtqZMYJ33LekBPiS_wKqLST2tJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=XKm7uBufQWvrGBVJxLxcPD3e2opusRRntXkavqGnPE3c273-jiPPjj-9_DBkeSlD9QVnoI8udCXN7nShK1aForcMsAvagCmfitJ_pch1d3XzvFsc6gkhXMHHqxXW3S52UYZ2Avg_xZ059dZ6v0q-wb1tfXb4mchw7ZX1YADMIYtjabjztZDnL7CrBb36gWPjYFi86ScUYlCszL-BHMrQCwiK4VRk02QrkQsMRYk1kU8NmpVhkMtQx8czcUJSXoYCnxfd6G1DAuvyxP0TE0KmOQyDAZfaIZI4f2s5UweHg2HVfwx0vlX71rKlzgGYuhkHo_SUKveIn6Ma9jt-FaDBoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=XKm7uBufQWvrGBVJxLxcPD3e2opusRRntXkavqGnPE3c273-jiPPjj-9_DBkeSlD9QVnoI8udCXN7nShK1aForcMsAvagCmfitJ_pch1d3XzvFsc6gkhXMHHqxXW3S52UYZ2Avg_xZ059dZ6v0q-wb1tfXb4mchw7ZX1YADMIYtjabjztZDnL7CrBb36gWPjYFi86ScUYlCszL-BHMrQCwiK4VRk02QrkQsMRYk1kU8NmpVhkMtQx8czcUJSXoYCnxfd6G1DAuvyxP0TE0KmOQyDAZfaIZI4f2s5UweHg2HVfwx0vlX71rKlzgGYuhkHo_SUKveIn6Ma9jt-FaDBoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmvwmDaLdDQJLn6-TeQcoKL8YAi46ia7vzHJwOdLvzOmOApAXiaRRS7jb2FpCwl-o4XENBIGjGhQMughsv1iNUsfWSZD4x7qqN4exFxPla8JwgcfKlgR6EQbYtygfvgMbDiHTj38EdMdablPprHKzfzlb5RgCeVEleSLYK4XBHjEL_7fE2aTLkeZTeDw0q0E3s-Ki0ai8EZVWkX4KLs-J1AX4jtCeNLNo2MkTdw5i3Iz7ha2Ikplia5ih3RmFUqF8fSlfLL1T7z08jytcAr39JwFzz34d3ryfuOFOb-CBzc_TqK2yViynnaOJhKJXlK5nkJ-__6PyRieYhct_iSBPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD255B_jVe6vQOwTcHc0lj7zcb475DRb1wcCqAVurWxBhvawQ0hQHs3UzB9HXXgD-Rl9sFkzjVVoq5tCjQMdM5yX_MMJgOWw7fh7Trs2EjO3YrNv5GJOlCYRS_2dfk5aazkhtGDYhckE6vsFd7_CXMQJ8ZQwbyk60JdlikwCTZ8LqAlc5CErg9jMlNP3fmQmQ6DUumd7hmN0BlpGonkP4hEnWTY2Lq5WpOFWTYne7RXA2rTHyi9Sr5aSIYDgmcMYQZXcUpKqaZHb20S0qvDP0TP4Tmair0fW1e89YPsyb6aWy8jFTzgNqQWXIyC4B6hYU3MihLlchQfcWdTo2CYlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=cmXvIkKaYwYwE3axhLbF0dom1QhAOFs75dib83sj77aVC0o2LJsJeROXPiW3jUiM7kZyEtiSTDfF349kEcgosJWqnR0MJ38ve6pj3zG0vtEk0t_l7rWowav57UMFNOed92Cc9wRXte9-ZOuTEQIkWhu09Ny_d-17czEYe1WYcKLZBU0QL0OIE8qBVuFZcm8FeZ-63zgcZMh5O-huDxX2Be_2xZxO3ZdSbz_BzqqW1HobnQ3MPV-tyPqZgnPuv3kCWAOG021e-6R6twh_aNywgx0FUFhkmzPR2GYdKXwQplacXbzopW1M1v8ysGHwhvGZMi6sPp4VOgwlzLG7kEqxEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=cmXvIkKaYwYwE3axhLbF0dom1QhAOFs75dib83sj77aVC0o2LJsJeROXPiW3jUiM7kZyEtiSTDfF349kEcgosJWqnR0MJ38ve6pj3zG0vtEk0t_l7rWowav57UMFNOed92Cc9wRXte9-ZOuTEQIkWhu09Ny_d-17czEYe1WYcKLZBU0QL0OIE8qBVuFZcm8FeZ-63zgcZMh5O-huDxX2Be_2xZxO3ZdSbz_BzqqW1HobnQ3MPV-tyPqZgnPuv3kCWAOG021e-6R6twh_aNywgx0FUFhkmzPR2GYdKXwQplacXbzopW1M1v8ysGHwhvGZMi6sPp4VOgwlzLG7kEqxEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=Ig9IrDNejvlaQP9xHt-67_VM6VXib6xkMFalwIsBybu9XxBkzjXR8obV9PdIuqrT_5Gj0kGBr2muWD1yZpMEm1vm3acbQkwRdtU2mc6JhZvM3nAOrVDS2ki9nHm-pDESzzAef1MozOvM4YKz9jQdMBmYPlElSrrGOa03C-n7xMtPG1lmYdgJHaJvVquc3-75Tv3uHHtzcyICAHX5ot1rZez1yXWAxw87qVuHlWDsN9X3lldaX8J_t6njAX5qabXfEsNfO-noJg853zSyY12ntmzml4rDK2aCoI5Vsy13AmGmTY4jpx7qCfrRqNEkkIiSMmrt6vJyr1P04J9tHaE8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=Ig9IrDNejvlaQP9xHt-67_VM6VXib6xkMFalwIsBybu9XxBkzjXR8obV9PdIuqrT_5Gj0kGBr2muWD1yZpMEm1vm3acbQkwRdtU2mc6JhZvM3nAOrVDS2ki9nHm-pDESzzAef1MozOvM4YKz9jQdMBmYPlElSrrGOa03C-n7xMtPG1lmYdgJHaJvVquc3-75Tv3uHHtzcyICAHX5ot1rZez1yXWAxw87qVuHlWDsN9X3lldaX8J_t6njAX5qabXfEsNfO-noJg853zSyY12ntmzml4rDK2aCoI5Vsy13AmGmTY4jpx7qCfrRqNEkkIiSMmrt6vJyr1P04J9tHaE8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ufo9dVrE2dlyQugQTdMaJ_q159SDcKNdHFMkDNBmP-IAaviqraw47Y9K4KNbcD9hZiUffTXYdPbQIZhqs67RzrmlcLuBJtthqKVTOod1wuwhpRY5n4IRCDidB79IFeohXaoD_5dXt8e-VATXG17lX_O4UoY5jvMxfMA8S1WMu2QAizq8GtollhUI2tMoDAB0uswKM1pZJ64KQSWAGH9JnbkTefhXNmy0MdEFEUm9Kmtq1VQM4-xk08xXfY3pax19jCTocxiwa6YfX96KxkI_hWJWTE54rqIxv1aQ7DRnLHNTa-iM7ylBdz0SY4PzNkxChdVIL4tnyQA97JfusCqjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=ufo9dVrE2dlyQugQTdMaJ_q159SDcKNdHFMkDNBmP-IAaviqraw47Y9K4KNbcD9hZiUffTXYdPbQIZhqs67RzrmlcLuBJtthqKVTOod1wuwhpRY5n4IRCDidB79IFeohXaoD_5dXt8e-VATXG17lX_O4UoY5jvMxfMA8S1WMu2QAizq8GtollhUI2tMoDAB0uswKM1pZJ64KQSWAGH9JnbkTefhXNmy0MdEFEUm9Kmtq1VQM4-xk08xXfY3pax19jCTocxiwa6YfX96KxkI_hWJWTE54rqIxv1aQ7DRnLHNTa-iM7ylBdz0SY4PzNkxChdVIL4tnyQA97JfusCqjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVO0d_ZQSfsvno383dymNgaPYEksb_fRXW2e13_QymKvLRZQGHaOXf1L6iZF3-LwxwuFm5BXXqTURKLZ5jtECzuamR3QyS5n6rDHJGRjPBOl9M9ZvZ1i6vjMMLqsJLIL4xR1y8W7DJYVT0QatjhKECd_EQZT4aYRNc8X9Z3MgWnuUJ6rruqaGWOhYetOIckbPTxr8TnXYfo7xZKN_NPx4eiqSgeuLxZpwvjbk6d6ouqRQOEVacv_sjTyH5vkEwkmZaOu4tlciFekh5vcqozC9WlULccHFaUhoTuxdsKw7ySqUIXiuxzJm5G8GEBekJghCEGEMUu5D55dzYMOVJ2wpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=UtPq1XTLbWBTL3FlYcZAGEI_KCVfkLDbbfEMl6vTwilJ1t7WJAl4wedD3umZ5kU8xQBHxnb2mFbL4lr5dojuBu_SeI9HRRpCo_idGOO2pvGNrcQxZltBorWgQ8in5okrscukbdlOw8o8RNgYXuq3JCGM8Lyu2LBPZtzl6_MmVqKHJK6jT4GndpISgoNEaV7xUt7nJV0mIH-dDB2h5zicf3tHuCexSilag13nFe32cY00uZGXY9F3W8jnAN-CrQJkuTWfX2xR20A0JkMtT8d04wNs5PQbYQtzDaRxTYRlcN465TZGE12qSXGmd1RjkmNPQJBIMFP6Lge25ApqLbUDnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=UtPq1XTLbWBTL3FlYcZAGEI_KCVfkLDbbfEMl6vTwilJ1t7WJAl4wedD3umZ5kU8xQBHxnb2mFbL4lr5dojuBu_SeI9HRRpCo_idGOO2pvGNrcQxZltBorWgQ8in5okrscukbdlOw8o8RNgYXuq3JCGM8Lyu2LBPZtzl6_MmVqKHJK6jT4GndpISgoNEaV7xUt7nJV0mIH-dDB2h5zicf3tHuCexSilag13nFe32cY00uZGXY9F3W8jnAN-CrQJkuTWfX2xR20A0JkMtT8d04wNs5PQbYQtzDaRxTYRlcN465TZGE12qSXGmd1RjkmNPQJBIMFP6Lge25ApqLbUDnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=rUr1fHoeUNGQoTHX0xbP4uKyMQQrEX3p_AuTUe5DetrK0t_XR46F1LG58JcGYBCXGPaOQykfa-QXAlrbLnwI3NZ3J_-3R4jDFN8IyrYiyab01HBbfui-Jjpk-zadOwPJBySyYSNHEK5mp-AbV_K7Szn-taVxVl1KsEUsoeSvL6ep8MnWiU_gww7J1O5K37lRcdCF1IOcbDpW3TLZPRP2IpqbjUHi8VxGOffOjQDCgoaoLXzSgmCdIfWVKEEWyBuufalpmT-kZA4AXSX3upHDnnIK-n7eKaAvc89DaS_MPQPKKGzGDxwpiFh7IUFXUDm3wRTnG0EnURliDtAjQjOZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=rUr1fHoeUNGQoTHX0xbP4uKyMQQrEX3p_AuTUe5DetrK0t_XR46F1LG58JcGYBCXGPaOQykfa-QXAlrbLnwI3NZ3J_-3R4jDFN8IyrYiyab01HBbfui-Jjpk-zadOwPJBySyYSNHEK5mp-AbV_K7Szn-taVxVl1KsEUsoeSvL6ep8MnWiU_gww7J1O5K37lRcdCF1IOcbDpW3TLZPRP2IpqbjUHi8VxGOffOjQDCgoaoLXzSgmCdIfWVKEEWyBuufalpmT-kZA4AXSX3upHDnnIK-n7eKaAvc89DaS_MPQPKKGzGDxwpiFh7IUFXUDm3wRTnG0EnURliDtAjQjOZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=MS0DlRrIpd38PHK5mgrBc09uviTNE96cA6qrDd4iwfwKGql48LREaUmIWoZEZEntfkimhSqTo9Qx6W_FW9fL6sMGEm4iqKVz3axeW61_bD2A_TTaLHqCwFwwkYGCdoo2wlChrx4jSwdokq2P-ZsMrYPseMeWrYlIddnKlUBk-otFiQNnR7z8rlUZoxGsoT801N9VSrrU-_9ivpEZfaqJwA1QyZdhJYPahYhs9MEWeqGaNs_EWRFm5QrsFyYy2CgkROMnvd8yC_pMVVp0j-MgidLZBSQUjU_uMrftnlORRDko_uy_cAvjp1GsLPgPaI9rzwtd5ZwAGWPkswebYPgDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=MS0DlRrIpd38PHK5mgrBc09uviTNE96cA6qrDd4iwfwKGql48LREaUmIWoZEZEntfkimhSqTo9Qx6W_FW9fL6sMGEm4iqKVz3axeW61_bD2A_TTaLHqCwFwwkYGCdoo2wlChrx4jSwdokq2P-ZsMrYPseMeWrYlIddnKlUBk-otFiQNnR7z8rlUZoxGsoT801N9VSrrU-_9ivpEZfaqJwA1QyZdhJYPahYhs9MEWeqGaNs_EWRFm5QrsFyYy2CgkROMnvd8yC_pMVVp0j-MgidLZBSQUjU_uMrftnlORRDko_uy_cAvjp1GsLPgPaI9rzwtd5ZwAGWPkswebYPgDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrr_eqec_LHvgfGBA8R2dPiJ--Ctl6Lzqf21UjGoVCTLI0uhxE11EYLDmlx_hdEAbXvtI5HBlpSwxK67-ZKEYzIcGamvEVjnNUB-a46edWMWds5WtGQ2MxO2U_Og_JZuXlykDbnfh6XTSOWRTf77acChHt3eNQlaqQk5bnqU2lJxZoX5GaO9pugVVJSkpLNQzV4gw1hGfpOI7r85xU1d9utRZpvjY99hzjb59KjHa5r-b3uAEO12bCR6-IIPFCfFC9ggiMHZFsm-A2XTtI3zZOS-ELx1ceJq0YU4OSB6-5skExyhWAx_esVq_irWPolYJDxZ9_tPLRASDoW0KPY8DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=hjTGbLAiDUG5OxFbc7oeVhI6X4grfw9-wvpcV6dv8MniPuewJPeYkgyNFdxyUqWvgzHRcMwpoMetf4Ug6aaXijfdNANR1znrXIsTJTDjpCQSvtAugH21X3qeW0KfPsUD5uPypAD7pCl7LFpzVwlXZaid8TsnXQ2svwK8DcDT1tiLSET0TTWkV_as5ZBMLYqLFZisC7zc-LJBiynk9tM7HnXDt8ZoBE3pPsd-Y06suLyq-a-iRzircnr-Qy16EWiBp4hLTCkrc8MkdLVMXBJSm4XIvLq2aNvH7R4uBvfPEqKV8nA43-cvhU1A0QWWbyKq9iniao4ypZI3MO1b0R0QyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=hjTGbLAiDUG5OxFbc7oeVhI6X4grfw9-wvpcV6dv8MniPuewJPeYkgyNFdxyUqWvgzHRcMwpoMetf4Ug6aaXijfdNANR1znrXIsTJTDjpCQSvtAugH21X3qeW0KfPsUD5uPypAD7pCl7LFpzVwlXZaid8TsnXQ2svwK8DcDT1tiLSET0TTWkV_as5ZBMLYqLFZisC7zc-LJBiynk9tM7HnXDt8ZoBE3pPsd-Y06suLyq-a-iRzircnr-Qy16EWiBp4hLTCkrc8MkdLVMXBJSm4XIvLq2aNvH7R4uBvfPEqKV8nA43-cvhU1A0QWWbyKq9iniao4ypZI3MO1b0R0QyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH_N_rQ7l80Pu6IoMbr0-M1Khu9K_3oSzVGy1r8do9ZTPdYm25QuDVs56eK9x7masrNGTrtbNGsVJ7RaSENLx0VBqDXBYdrVQMbrQGZ9-YmIZNr_Yv8K_vCqzs0CNh1HPwpeRKnTHJuhVZ5-4i4Zia1mD_2_sA-S3wS78Qy5Ew7DIw9n_sqrDOtAVEiZq-prBdJFBzmHHPVaHwYmY3BTxXg7yyJm2nmUWvRozOdAU2MAEFJSXfrGgpahPhN0JdnMR_wvr8D03-2xcD0JEVdmOR4W47Y35Tip4kri3vRHe0PS6ww9yWtD1JGjcRSHE24BVUoKM6oGmweCUH4jfZPwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=GTek8DP6eqbYWO0PIasZN54W_p8QUP2yC21wgh5YeUmM61HuLVxQmgizNxvxcpZ5AJqPBC-we02ijIZpxtbuOMdy0nBa9q1ZdXj2HHTN2-2lpaD4n-a4O_OB4g8pQ5AT0qSg7VCwCHJyYr8rwaHjuj59b6yMWYUeG0l_o8TB_Rr-3rTmHO2asg-2iaHbNN2ALHJPLdIeeQ-mbzdV5OwgubUEJxwCLXu3Zyz3WdAF8DPs_LtqK0Sf1lrq39YNRzslNsPaPT5j2Sm-G1M7Z01oLGfn-Eevxi12mf2xJn5i-EBhtPD5XQaqwG9p9mwee01GfVZdxhez8sB8hgRXtGXUug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=GTek8DP6eqbYWO0PIasZN54W_p8QUP2yC21wgh5YeUmM61HuLVxQmgizNxvxcpZ5AJqPBC-we02ijIZpxtbuOMdy0nBa9q1ZdXj2HHTN2-2lpaD4n-a4O_OB4g8pQ5AT0qSg7VCwCHJyYr8rwaHjuj59b6yMWYUeG0l_o8TB_Rr-3rTmHO2asg-2iaHbNN2ALHJPLdIeeQ-mbzdV5OwgubUEJxwCLXu3Zyz3WdAF8DPs_LtqK0Sf1lrq39YNRzslNsPaPT5j2Sm-G1M7Z01oLGfn-Eevxi12mf2xJn5i-EBhtPD5XQaqwG9p9mwee01GfVZdxhez8sB8hgRXtGXUug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAfcT1DspROCkxKzLkKlr8eZssBLyNB0VOC1fTkGwnUJmBrHk6avcOPl0q46CA0WFUVWRWm2mQFq21zdrN0OMofc9DAGLUTEMnIn49rhuQfWlvNztGjsx8SCkZ9foAX0v--HZtlNjG7nQHu3GAUvkIZDdGSGg5P2M_S91wuE9vZz-097DcEy3uO4QfWXChyXKZEJc0nT3iWKIF_nspD586K3tah5U3YHxqiYZT_vRbHIAAd_MHawiT93AmwbRc9fxeXuLpEvGsVRu_wmwRiGkTzzjYnfYBFLjwQCCYxhwbO_XyAoQeCQNkbfzjB_iRqePIfddU7thYd0-BEr_1qYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=apLavD4SDE-FdsCk04FQaL6ejlJvjbBDJ5TK-ZOwtGm1Euo3_Vtq7zSdfSUWv2oH2oPlmkJ8QtpvpNql0X1pvZuErl5GJ0ktHKOVv4x6RPb92QibEhuf1Qr7eRBSQzL8ztXgW0fYLo1bx-VVUE5OAVIkSmzQ8ZsX3WXuwGAIZWIzXGK_qbX33jXNDqD6V36lWEBSu77QiGVfFEmSQsOFudJiqzWuSdWXk10vBiV3w-LpOh6fljVjYNEVLtV1APTq0yp58FAcsGDAJ4TZMiH1WFzpuREw67rgHVC5LScIoRC4vErlgnAePI7pcy0nh4401u2nY3fxoZXUfHT0BkyALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=apLavD4SDE-FdsCk04FQaL6ejlJvjbBDJ5TK-ZOwtGm1Euo3_Vtq7zSdfSUWv2oH2oPlmkJ8QtpvpNql0X1pvZuErl5GJ0ktHKOVv4x6RPb92QibEhuf1Qr7eRBSQzL8ztXgW0fYLo1bx-VVUE5OAVIkSmzQ8ZsX3WXuwGAIZWIzXGK_qbX33jXNDqD6V36lWEBSu77QiGVfFEmSQsOFudJiqzWuSdWXk10vBiV3w-LpOh6fljVjYNEVLtV1APTq0yp58FAcsGDAJ4TZMiH1WFzpuREw67rgHVC5LScIoRC4vErlgnAePI7pcy0nh4401u2nY3fxoZXUfHT0BkyALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw19z0q-Itp3LVdLADmaHGkbJTB9fcRHxmJoBbP1ygPRIKk6iAQ_yHAWIxeojY1u7GyQBT3jtNI45ncqz_fL46iDmI4gD6R1RboaiIWrukRhm7DkV2DRqBtudAhPlbjew4sqnCR978oTsYAH5GLSohroJmgGiv7MYOSfWt2kLyu48dagveQX1L3uNVxsTaReeW6U-jtnhX_tk7tCKueuMgK6A_XDRlGmloWOpFf_GitKGx9AIqVS8wQaLt2fSWZ0FskfMCQ_2nWfUTOggFeadWAh2dNQBE9r9y_xa0-mgPdhWOGURKzh1p9V4i8o5ca_xYlhLQoxqx-8CsEJjUgYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGrD1IC4dpzsIwhL8jsfvSMwTL1mf0grMGgvGuIyMCVvcU7PV1iP5kQPYMiSTn5ZUkcDYBdcGF7wnBt6a33NaYTbWdVuNr0UeEQMLlHVvkMQimLdOpMuxj6PAfBFb_ZnPgk8hS4PnKDCs7VMPsr70YzoqpXn_jEi4QmFXV7fVxaVPBqMvd17Fv5WyyT_qLbzkvT1F00JrJJl4u6pSXlijtZ3pKIZQCJKl-ywfrz-rpFdwBlkugR2DdNnBh3ARprvP6tfvJrYG81zttBmjBfVWXDCVmk1dc0d86mS4yr1gMAzWN44I4ePRc81NXGfY-EIttyXat0NMlb9SQrsL459uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=bziyyNVp2FU0IHOygsi-fw8lQVES6U2DJ1cM-xiam-u7M9nOuW6w_To1O0U4KqU_3O9prSR2grgcfUg64F9MXZcBb-fhueIbzt3GzipxBMy9yuTttigBbQQj-x2SsOPbxP1uQ-bcHIytFUMBB8QQNI-I2-PVu6zoqGNN0YfXI_ryoYq4alHPEAWy1j8Xn6Y8BS8zVJskFuxg6M-Z1r_AhBBhfOwDqKIsTTjXiDe2UALOZynxpxRgit3agAM6esk3Yk8835THHmX7voXkoEW0RxbWYp1WSP7B_3hh3vIvRuUfbhmY9B8zyqw5teAfBYtX460mXXqA4bJqSSSnlc5y7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=bziyyNVp2FU0IHOygsi-fw8lQVES6U2DJ1cM-xiam-u7M9nOuW6w_To1O0U4KqU_3O9prSR2grgcfUg64F9MXZcBb-fhueIbzt3GzipxBMy9yuTttigBbQQj-x2SsOPbxP1uQ-bcHIytFUMBB8QQNI-I2-PVu6zoqGNN0YfXI_ryoYq4alHPEAWy1j8Xn6Y8BS8zVJskFuxg6M-Z1r_AhBBhfOwDqKIsTTjXiDe2UALOZynxpxRgit3agAM6esk3Yk8835THHmX7voXkoEW0RxbWYp1WSP7B_3hh3vIvRuUfbhmY9B8zyqw5teAfBYtX460mXXqA4bJqSSSnlc5y7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7SVHGRgS4brs_z-bb_-nYFsJAApUOq6dFKnlths9jlvsMFkGjD37g8A99DIc8VvlgXiWmBE5YXJPaIqOo2k91bl-PXvhlTtcxmikCeRHVPKSiAEAC2besYkAiyDBXiuFfOeZTlKr18n7nErQirT8kFEyNUr9MOO5vM9AgbdixFnVWRVGjnkSNYNkQ4i-Yz5kWGyiXKZi32IP_012YqoPHBfvxzUFBySlmjW9sJ6zNa_VyxPP_2AvhCvASF5q49L8_h0NZ7xUsN6Ro5WBOX5sSWxk-Mqc9BJBnf-zxSbFP5P-iQHYjEA7dC-egECPZhkNfTPBVEB4M4MY3hND-M6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfpLnurfCDi3NoVPbAroqSvBYvXfvR1g-AVaF6SA6dQPusPrFSQ-Fg9KpQbVM4Ve0iZVn922c-WDBeUexgA7ktUFLf_0NMpauIrF4Tu8Aw4vGsG0ZjT7yV3DEsR7ZGCpox4cvLmsxvJcTrYPcucEjCRRj4Xxe9KhoxhJLmMLmV-rXe7ephZGvBhurFjYKzHqR22974-BgEBdXislRIxEIqlpuSlB7BTGDn6BKK_0bzbIS1enslCrt9XiFQYzs5-ZZvVW2iawcJmKAl_W4Q7tpz1SnSto4EZd9c0YzX36bYOlvkHeN8PQhxnAqZzxn3V1KuxrIFeUDUkOaqCWK9RgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
