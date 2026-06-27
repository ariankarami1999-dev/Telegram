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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1jh0CX0ofoIdUnxvDoYs9IX0gzO3yoLoE8a8kBXySUKNn8_yjxHR2NiQtsw3GgKx_EtQQsJNpcMchTNZ4Km_jcxTctu0b6fs57l3Tc0BJYC4lkCgDAR-tdPGzifvA6ddaPEplL6KYA9irYTZithSlJuNTTChFrAePtue30uJx5eBpK215TrzVnBqL0wRuR9_Ekb9PdahhU0d538wYT7vgPSck3GbweMFS5gTHIwh6FM2rE75iw-EXAwXylemdBHRMR2-XDlQhTap6_x12uw8UNfssmSmnU6TUZBqKkdTqPQ6tvctIoV8yUo3U0vGjq5MTDhkrF2IihblteQpuZiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ovD8p25V6YxAN3-7_24x_8zIhJHSBQ9kH05T0FUxSFsavndsdaV5b9ObVJunAbRbzl1O4hgdy2hkksY1owjgK2_44uQaO5Z4WhKiAVsalqeF7ld713Ji-dlxH6WpqgsRITfPPYH_d-fNIoH54pqbwSDPNYkAcLBwjri_pReYOU8EgQ73kXT1IXxnSIcLD_kSJ21DhwQkFE4n3gTFyKiaeZ6Ef6MXOnmvIEWQTxoLsj_MMaxzbx52WoC1ieaMSoqkJXGKq65S511eT9gkeC02NZb5ZDEhB37736VKQdgMrMaI7y0-qqr7UUgYO1Lt0m3CpJozLQkOKF4GEA3tf6RFyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ovD8p25V6YxAN3-7_24x_8zIhJHSBQ9kH05T0FUxSFsavndsdaV5b9ObVJunAbRbzl1O4hgdy2hkksY1owjgK2_44uQaO5Z4WhKiAVsalqeF7ld713Ji-dlxH6WpqgsRITfPPYH_d-fNIoH54pqbwSDPNYkAcLBwjri_pReYOU8EgQ73kXT1IXxnSIcLD_kSJ21DhwQkFE4n3gTFyKiaeZ6Ef6MXOnmvIEWQTxoLsj_MMaxzbx52WoC1ieaMSoqkJXGKq65S511eT9gkeC02NZb5ZDEhB37736VKQdgMrMaI7y0-qqr7UUgYO1Lt0m3CpJozLQkOKF4GEA3tf6RFyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=abM3axnAUyZhP0y_7HcnwZIbGMRk_YTLoxUuVDgix41hHIeTaRAJdeEk-vdigOrVZengB6ASUVO-_88EMmHllkDe5oOBbl25gfKZiMfHhS9xp9IKNJ-kaYMOt4Kzims42OIR7yAVLby3Qmfo3lLZi816z5hB6gR63x6ytcDDBrOWhYM4Q952uAsqDSTJcjgwOqRHmw_wLRXXiXkG4KTnM5JWgeAJQ5OUvQ0C_hY_e5HP7pLLD4m2mJYb8z6ebYlG5liWQW1dLUmiXcGUegzz2IDe8Sdkwqo33QjpJy313LarYOsgXqAywG6HKvcbMjSLhqdlKF7zqnUcduV30msvhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=abM3axnAUyZhP0y_7HcnwZIbGMRk_YTLoxUuVDgix41hHIeTaRAJdeEk-vdigOrVZengB6ASUVO-_88EMmHllkDe5oOBbl25gfKZiMfHhS9xp9IKNJ-kaYMOt4Kzims42OIR7yAVLby3Qmfo3lLZi816z5hB6gR63x6ytcDDBrOWhYM4Q952uAsqDSTJcjgwOqRHmw_wLRXXiXkG4KTnM5JWgeAJQ5OUvQ0C_hY_e5HP7pLLD4m2mJYb8z6ebYlG5liWQW1dLUmiXcGUegzz2IDe8Sdkwqo33QjpJy313LarYOsgXqAywG6HKvcbMjSLhqdlKF7zqnUcduV30msvhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlphiIxbA0gaoR-R9C17LUgEy8m5a9TCgjWIUTxx0at4cqC6kxqGX7NsNLk_gds8bBil-80yzLiNvbhsxMIzHGcMGkqr_sxEFZs7nNTHkXgLBLMOWgsV4KfDgWb2tQn4XW8l1aCu9o5SUdioLggx-vRl0ghlvNzgS0LWPTstm7MQK0y_hM90YK4E7lvb-UP4BjCs9HknG8LVAATyqKw9-le0dDGhKi3DI6PAzVByxIZd7gJdyDAbYJlWE1pOJXyuIgT_mS78lzqFtnDPkVpsr3DKmjmkk5-udMUzhDQIJ72BzoZKUrSZucCJpdV13GJznIE89_HGrfYRh0xhlebZtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR2caAWNtzIDa8QTmovQx-JUb2KBGJYE6G4J8JZz3JcCjLT7FJFJgxo7Oqw__U7QMMdUzddzxjAtDFff_j4iTHpFev0v_QR2KO-PwHU35YLCxYY-Yb6tkwqP3P_YI4erpJpVftTOEJS8oSj9sMpC4sHnmgUBgjAG-rHyY4yxdNe3aJVVs7yTlFW0qOZUkWV85_cZqEtMpXEKY8ruP-N4hwI3dYYju15e38dMlSpbr_23lhpJuTOfy50OSFTveoiPCRWQtDxum42Xm96me18P9ZywD0rWa5BKd0HqKXCBk_qwoH6kPZHiMvFk8LvFEYqcDiyrOO80KWThKksx9PHMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=RPSHztpLP9lxPryTEbLLKvVa2JUMM8oO-SFYq9QsnzkzJ8zNfpmyk_7lzqbvf67iYNVknE0gxT1ikLvyaY_D2qfDRwionQDkTwXlMCY9DcCDIycUhX0-QwpHov24mQG87Xtl_gDlCotmmATM7HYwkbqlOCFApQ10Vk7bAtnYN-Uzhnlmgj2NayC6za8mEhXQ0GpV3UBHixKf4fpAjy2rWTVU_9K4e3jl3EpPCRTmEOKOyaebzOOQodPXGcd3JuTFtMybl6i6576aoahZXOuHl3Gp04GTuT8A-dVSFkogJl-ZzOdbSxvLaMQPaDtOKeb7tpA7dsSCJErGz096b13fTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=RPSHztpLP9lxPryTEbLLKvVa2JUMM8oO-SFYq9QsnzkzJ8zNfpmyk_7lzqbvf67iYNVknE0gxT1ikLvyaY_D2qfDRwionQDkTwXlMCY9DcCDIycUhX0-QwpHov24mQG87Xtl_gDlCotmmATM7HYwkbqlOCFApQ10Vk7bAtnYN-Uzhnlmgj2NayC6za8mEhXQ0GpV3UBHixKf4fpAjy2rWTVU_9K4e3jl3EpPCRTmEOKOyaebzOOQodPXGcd3JuTFtMybl6i6576aoahZXOuHl3Gp04GTuT8A-dVSFkogJl-ZzOdbSxvLaMQPaDtOKeb7tpA7dsSCJErGz096b13fTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=USJ7SX7NSw_5tp8RtQLK7oQR5Lbeb7g5pqwLL508rtydGFLNg1mbQlrY4hYCVFJn4ZyJM6Ue3E9JTG4Fkqna3v7aD9rCE35jHOBMxHVSmiCufH4XPsFsbw6xi82J0fzgx8r4NRHlM8a5iacMMlb7qp9Ya-fwyd2TWWln82W-4q8bUeWEyKfkii_Ka3YSGiiW1WihQniVJtqw5Bhwlmte24pwoXtPUlDfqBm2KHex2qR3KC2u-_p0JkedKi5JOgO7LBtD3P7Aoa_SmCEatYvXaH-umSOp_lZPOYnQgqs8FhR8O8otdgflo0yUaJIH8NOL9OoEIU2DzTilpRvX3z-AIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=USJ7SX7NSw_5tp8RtQLK7oQR5Lbeb7g5pqwLL508rtydGFLNg1mbQlrY4hYCVFJn4ZyJM6Ue3E9JTG4Fkqna3v7aD9rCE35jHOBMxHVSmiCufH4XPsFsbw6xi82J0fzgx8r4NRHlM8a5iacMMlb7qp9Ya-fwyd2TWWln82W-4q8bUeWEyKfkii_Ka3YSGiiW1WihQniVJtqw5Bhwlmte24pwoXtPUlDfqBm2KHex2qR3KC2u-_p0JkedKi5JOgO7LBtD3P7Aoa_SmCEatYvXaH-umSOp_lZPOYnQgqs8FhR8O8otdgflo0yUaJIH8NOL9OoEIU2DzTilpRvX3z-AIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiVqouHDart2mnEBgF1xeymY-K36EIL7tNopV73xsVxvyuq9UMSV0olG9m0rNl0tLwu6yfSZDiKg89YnK6ZxKb1gEubr8cBpLDwcUfWs5MtNNXZKdprkf0osPyHC7ZmGNU0DNWsmCH4oKB4QHhYWptzFVLwy91Q7JopJYhUsyq0TXU67p_xum8bSgtawUWiqdmyDYQqn4VnFBEcRrj9rDje60Gd_FyDl3gvNYYTJczK2Z7uxReS6078K-8jIZVowTuc-p1GClMYmClDeWFHsm4ugxe1x1dDAeMLFz50jdcHZzkISffVtHLZ950imjC56SRInv5h04EKbUCvJXXdYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGguO2kVsbiXwydcQPwE20LdcV2wKrZbSnpjiriXiglI61Itid4ugZhINymN3YUjGehNjHS8-29SpuQ6doBivc2c0HWERuyTtIE6_uMp40AXKUjtbjGVYxowRSsAm4QnIhwnecyCv19mnec5h6yPDCX-xPern8MIvZWv_bPcC85egPY156NfgkWzZaW0hz4XnJ7tdpjGHtW-kiN1vG0h7iNKrCCSZp_K9yZhJHiM6lISGhRr6TWyjA8unIjvOEfWvFyoOEfHFwSd643LVmMzw4ShTZhLWt9uB3FOtycWDhecgIrM8Yt35B9oqyjcnyng10BTjZDgLB7UOLVD5z4dWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsiSpz1cfa5wwjO5Gv7E74X1VC38tJ0dB7HOpjpDu4_V5pLahfDQnXz5pVohvHtiEPpQAGLzxjJOd92K3nTPu7MkQojILk8asnqxKBrJXizC5jzw16_Jrb4dbBOJIvitp9tkRH77entAQ1AuCFrMSKzc4ucIyQa4akj06icQvEGZfr6A5pbUUQtlu9xL3bm9ytjzVVBeZOPRGMQR8WG5hRhSEVuW2ktK6aZTDxuGK2XyJcymmfHgrjBpXqQlj96fGjE7G96Zf5vDP-vW7Yd9IPVWRPaIrN1BEDeCLMPf8t0fBqaUsHAXPHcuWffcTWS5Andw2PaoxXqVjDdcj7Zvhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=Dlm6DAqR6bFuk47pSKIFeZEx9hCIQKgYgkiyTAEAkyxUgj_aFwcjcot-INclOAMcNTlJ_7X706TUBsgBtZmpKla9mVkaeGn-VTbmRSno2hi-cP3iMKDUl9sj-t9K_7r3gJTDRsOc29Q8q13NEuU0kcuLpmJKqSZG8d0uXhC89YaKagsu6jdXy6inCWI1zCmH9bNkQhONtS_n2tYEZCF6uuDF5btXc9t4koxXrk6-urPMacDQB58fE_hEihgceuvwnQvcNT3mPIIicx9f5ox9QxzSMZIQghI_c_suydRDWBDLLgOl1XqSIfYxRrVh3t5d5of_PoeMEoA6ZlkG-ln1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=Dlm6DAqR6bFuk47pSKIFeZEx9hCIQKgYgkiyTAEAkyxUgj_aFwcjcot-INclOAMcNTlJ_7X706TUBsgBtZmpKla9mVkaeGn-VTbmRSno2hi-cP3iMKDUl9sj-t9K_7r3gJTDRsOc29Q8q13NEuU0kcuLpmJKqSZG8d0uXhC89YaKagsu6jdXy6inCWI1zCmH9bNkQhONtS_n2tYEZCF6uuDF5btXc9t4koxXrk6-urPMacDQB58fE_hEihgceuvwnQvcNT3mPIIicx9f5ox9QxzSMZIQghI_c_suydRDWBDLLgOl1XqSIfYxRrVh3t5d5of_PoeMEoA6ZlkG-ln1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SURwxFU-gMuA-kXIXCq3s2Xvgs8IkZVZvAmSg4YBFwKh9cQpxvtarBQpt_nv89ho-oLEY5CLRqEslqaUT38bgfen6Bd-IRWajV7HANv7mjilg-XQmKGr0jeh8gucsN7eac0xEiOXq2bG4ncGKVBpKZYh7v28CCVdH9jFT76imRyAsEXr2Mi4oWbhojVtToY8YvKQj7yqnacrik9a1BKM4iF7o6EU-MYTDqEaydFWkoOzQZ9uAKGkMKU-pe0H6kA3OpVcAtO_heD2creG8QNB_pTEAax9ZkKTTfO7Jey-6fXEHyX2-tug568hv4LGZZKmTbCOfHp6z2D4kOeexp79DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnrY9HyR1OuHVz5XwoPW9D0Pkmm0Eu3frSdNKZjpRn7UwoWpx8LmTftXoA1xl9IM4FpBKcW_UQ-NlevxhyZyA-Sm1JiENDWzszFsDP8fzrxgcxAbKL0Y9zoMv5E0UdsUr9BWHGqnai6KwMk1j5g-x21omOj5vuYUswpPfAJoZ3rcMj_wVcMvNgs3J3DOFeqj75_O6V7ha8qVsJrrHEIIYk-vQmoqbQay5vHTvj6E80jHRfE6aD0XtIjLe4MPreeSM5DxvcZHlpEn_OBQNRJyqtt9OFMzldQ7KWLJrj2Bb4URFENFR6ttAws1qJBwJELlfFrjsKloTbfOyf34IrYVYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4hBS8WVY8gqvzeqxdABQEIcQbkfx1oWCA5SLl9Au6FVsHBlRtq59gdgEUcJaVsG1VOMPvfs0PFHGGBIzEJu0nkJPPdM6ZQK4KIxAAsAbMuROyGuuBIFkazzuvSaKyOAlRAWcOupAME0EtXdp_79hyJwpm6y5fKWY8Q56ZHK6xzozR7mY-7md4SmKA1bOqmbcjCB0w3M5b-vNZ1S1HN1--5FX62uOxHN-A79N166zyemnMg6V6MfS7myEgcrt7069sc5nfy3uyxagGN6hStr9llFDBKXtAM8Fttr98uuaHDR88BGWAnasFbzFpxLevq8TeCguJ5_C9sw0-uFcTOthQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ifex5jZtb1sTvIWK0jKp3UlOTFaS0x79axReAouFxC-WPsAEjCBvEwO8DBDrRAe2zhApGnvg7EzKccAaCjQetRJiimi_NQQHKHVwpILt_BMYRT2b-SXMj35B93ZmtBD0s06JWpYKvGo1lZ4roYFFpoyraz8XS3TxsRjiaC_qyEGaFTFk9qMW-PXE7ppCR7JFfbpnk5GiNq0oN6YNNQg2TbIFWJQLcwZ3Q--ESUPMHvAqgw9Eu82F_-3I0z9Req3Rz2JxnncdjpS4_9lNF2emi2ifZgRkfvmAYKmGHfjMoVHlqmfU6mHC1XWQDnUKajbhv3O1loPh4g5cQuDMGvQYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ifex5jZtb1sTvIWK0jKp3UlOTFaS0x79axReAouFxC-WPsAEjCBvEwO8DBDrRAe2zhApGnvg7EzKccAaCjQetRJiimi_NQQHKHVwpILt_BMYRT2b-SXMj35B93ZmtBD0s06JWpYKvGo1lZ4roYFFpoyraz8XS3TxsRjiaC_qyEGaFTFk9qMW-PXE7ppCR7JFfbpnk5GiNq0oN6YNNQg2TbIFWJQLcwZ3Q--ESUPMHvAqgw9Eu82F_-3I0z9Req3Rz2JxnncdjpS4_9lNF2emi2ifZgRkfvmAYKmGHfjMoVHlqmfU6mHC1XWQDnUKajbhv3O1loPh4g5cQuDMGvQYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6pRdWU91oYwZbXBBIPNzALjKpwEw6xqdJW6YkZag7AEdk8V4wmUvvv-tyyGQdjpqLja3UFxbCvOoy0uT0ctLr5g9FNDvLr4koy7w40qlw0ID_1ARDnJqRi3Rvvj26qd_2HdPFmYa7SKaSc7PfZ6xe8UCYLX4irzlcaIa-28cEXVETvIKaeQIT0eDBybCJ53g2--YQOHnYIZe3jLu_0B_YJLxVLQ0X-M-PUIB4R-3Uc4eRbDIm9reOiB5bAaNAjKSbltIW7Msr7oDQNdgTkIduy1Q4pLAx2To2RDEH4vfNXfSWWbY1nqQ9Fj2FqHpz_5NpuBA_A5e7VVBJyz0UVXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbJNRIciaDOorQy1T1_7e0ydVNe9cRn_UQ3zF2sHtI6dKDKiLDkoscqVPjzgEuO-tFtJZvBHLzQgtBDmNsFoCMfWS1hwcVrLPhRpS2aRagl9mjswpR9TonAeFTaqHqaN7z4vIhPMWw9nH7IwSBk3gApNpx4e1GnEdZBWyxFgZ_SFUozmJo6Q8Nu23bkujqdzuE3lnMS1oka0a4jS3-JR1tktV_JI1Tn8-Pb9n6wZ2gTG-GmHRqkXz6L3B4yBbRL2IfdJQUmq-3ce3Ub3F4tANf7hu_dH1C8venYKd4-K64MnBcDrm9aRYhcCprBtbbpXkyl4wO8nUjBJdzYr09gTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIGDxizdBHfSapmfSVBmdLwLg04lgappGewjoUMiTXZmAVaNKc8_qtSFJUNngVa5L-3LTop-swsVgMcboyer4QbQvrnf5eAJI8LWn0Y6_Y0OhvY3cqmtFd7NOOHyvT6bmx-Xi5kDBiFSlotXMUCYRZHtjBd-Q2oNvFpFrMVp-fYKC6_a1iVt3dTPBglZv8wGBCBIRE1RFMR-yWZXC4XqT-bBGrJJkqEY1sb16T8XXlvs3r0gwQAFqPfInN3fe57VrnCU3wTIOjyZDK60EE2ksaPaLAY3Anc8E-WtIJJJwmJF4BxugmrLKntYVSX7uYTHIaX-AY1Oolh0k2zA7tQY5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Dg1qhBS6LJakaNzWkMUFFIfsmKpuaWjpL0u92NMTJXorMn02Bz23UCFm_fKx2vqwLQGKRzvTH3M07CJC0W8cupa3ZgHSDHLL0EuUa3ixnPzKl6_gujsCZoPX6W9LvUJw_pw-imkuA4TtElzxFUTGfDxdITOTeAyJzAgBpVHiB-OvmK24AyhMEfav3_CLLR-SkKm6ZYMi8NRhPiOsG9H1sJkIUOmJw75u9ulyWNuXAmxLvFQwuA-Qm0rlHQ7y1VbulnpCaIbXL-4t6O5GeyOJT6YSIbZ0s1N0vX5kLEpul6bMRvb4JBIprDS4iWMQKJAZIvt6mG7ynsx92gOevX4mhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Dg1qhBS6LJakaNzWkMUFFIfsmKpuaWjpL0u92NMTJXorMn02Bz23UCFm_fKx2vqwLQGKRzvTH3M07CJC0W8cupa3ZgHSDHLL0EuUa3ixnPzKl6_gujsCZoPX6W9LvUJw_pw-imkuA4TtElzxFUTGfDxdITOTeAyJzAgBpVHiB-OvmK24AyhMEfav3_CLLR-SkKm6ZYMi8NRhPiOsG9H1sJkIUOmJw75u9ulyWNuXAmxLvFQwuA-Qm0rlHQ7y1VbulnpCaIbXL-4t6O5GeyOJT6YSIbZ0s1N0vX5kLEpul6bMRvb4JBIprDS4iWMQKJAZIvt6mG7ynsx92gOevX4mhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=T5mQpGNP9YlvIrF39zldeNyl25tJ8rY-9Zdyu9HYC6vuQo1n_-_OKl3IepB_T70-PyOulKcuB1fUxhPQunkgC1J9vO68oSdJAh0zIG9K3kl2UbhAApuhwxRI8krgmw5aFIi3NW1RkUOTlpBHcCwtAD78O8zS5MfzrlNWdb6kBxKOvv8L1lr0cGQMTXB-FNMDPVxcEXJeG5JFMgdNTpdhri2xJzLt7ZrtrMSHKVNu1p4SWeT-vYycnWgpdPWzqObQpa8FXLTMIeYb0jUQ4xH6WGVp-6Tunbsi4rGEEs48LyVC1ns7qWEhjLcCeAqQ-W3eZd1e14YpF6ypcC4uazoJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=T5mQpGNP9YlvIrF39zldeNyl25tJ8rY-9Zdyu9HYC6vuQo1n_-_OKl3IepB_T70-PyOulKcuB1fUxhPQunkgC1J9vO68oSdJAh0zIG9K3kl2UbhAApuhwxRI8krgmw5aFIi3NW1RkUOTlpBHcCwtAD78O8zS5MfzrlNWdb6kBxKOvv8L1lr0cGQMTXB-FNMDPVxcEXJeG5JFMgdNTpdhri2xJzLt7ZrtrMSHKVNu1p4SWeT-vYycnWgpdPWzqObQpa8FXLTMIeYb0jUQ4xH6WGVp-6Tunbsi4rGEEs48LyVC1ns7qWEhjLcCeAqQ-W3eZd1e14YpF6ypcC4uazoJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=qz9H0E1-YDl5lLaJmpLrG7tMiBwBC2R-dQVDAqM11NixYapBac7H-0OYiIVw2IF-2HkB2rVl4Itg049Y4ZIACV0EDis7MqoS1BKlhkpVKYDOTy_et2rTGoOFIQAtkbEWqgL-7y3UDEo5ZJ-3-CvttC-C3EeJzTRZkq_D4_h_fDDju0BV0i4LsFZhHlClNLj19_8eu9rr_FAQIVlU1Y7h-uQm_xnTJ7_wX-3UPryN2ZfAvLuIJ_Fz4bJQsf0Rai4TEmk82pyzFyF5HDEKlsgKTkL7KNwQzcwFG3Ow_9dwLndn1xwQtqSTjoVlz0pby5ROCvAbfcDqAsz7VBnNM83pAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=qz9H0E1-YDl5lLaJmpLrG7tMiBwBC2R-dQVDAqM11NixYapBac7H-0OYiIVw2IF-2HkB2rVl4Itg049Y4ZIACV0EDis7MqoS1BKlhkpVKYDOTy_et2rTGoOFIQAtkbEWqgL-7y3UDEo5ZJ-3-CvttC-C3EeJzTRZkq_D4_h_fDDju0BV0i4LsFZhHlClNLj19_8eu9rr_FAQIVlU1Y7h-uQm_xnTJ7_wX-3UPryN2ZfAvLuIJ_Fz4bJQsf0Rai4TEmk82pyzFyF5HDEKlsgKTkL7KNwQzcwFG3Ow_9dwLndn1xwQtqSTjoVlz0pby5ROCvAbfcDqAsz7VBnNM83pAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGBVV3toirqA6JXnfnrXBa-I7dH5kspxGWxjBR0ftvYIWAZpJnMB2SunzUijJvDq9ExlBJSepNbrSd6f5iYU5Z3YK1ydyqIQ3rZbhLcAetwgbhjkilOrVnVLe95ItkNtDYd5od2Vv0WaNcFgSx_45BeHeWz8BNgN4IpBZvc7gLjakuQ3e2heeEsnHXOY-VU4blOJkZqmvXhkUram54c3OeXjcpbo2882E8iaWMW67c1mENWRKCpXfp1_aSJmq4sYxh0h-te3uVdRRliU1IYAKvY8GaCTLjYevH2uhr5qQRnOpx4Pqen0fkE6oWw_wrnw5DiKenPAiYvzjvZeIRJLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrQ4Qpi3T5l74ovyelm4BFb_OhdzHn8oyFu21AvvOWq10atj-HPXsXdPYU1b_u4CAR_-G85Ae9J6JAKphdcIikO6d_l2BQU7sCcXgvaX0A71oLKoWXMf6cdmO5fwLhsIIKCbQIrE3uVwQj3r2o-bJLlF5-Wbs6nJXVd0r87VO7jg59XVanpDHLaF0-m8GxADLnrr9P9UTZOQJP0pV9SdPqlPg_4sPsB0IDyuhzwXwVx2AbAbPX9rlGMzDpe0-t7SHLnxh2T9DHt3VuRuEl18pU8EyoYIoTnohuOdXlcjqcH44BTvnefgqO9iwT_5VItt8PsV_6IEchSV5dGtc_n07g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pt5gLcCrNtDZZncd82zBvz1F-BT-Fm9UkkonWLLJWpOJbQuXbAVplIhBuoRp4Sq__TerBra7ds05VonJBLvEu9bzBEAf1uP7vfFutyxD6wW3v-uOMIEFAkiunOBNuqFBgSrhkBogERHByKiFHD7Al3LyUh0BFppOWmBu5m78FOxdohs8LOYsz8Kt0YpMk95jVxOwryAHHXa3jeKXK_RbxPTtbQiomwd2quAX5gBl8ksy9BqYft3NuFxAKs01hVLuyyUrI7TnTTy1q5OtdPXy4IV5MUI7Xi5sNrjPMhJbMPT4GgAhMf2D8ImvD6e4A_xrSaOHata-me-zr0LgYeR0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nckLfyDqzJwWgnNdgRZ8_jIWz_vINGhuJp-NL_0qVgCjhdC45THMbC0W6FYt2Wd75PGBptvZZLiliWg_AnesUCake4LdnHHI47yS_ocKP0usSWX109n-06rl0TKVKWGPLjFpdwuKhpqJHGiKOmu47KZknmO6UINEfggfj2kND8UOuM0U0T0KmDpTLF7H-oAFl9AfbxFA3tV1DPIs2swuiYCAfkFGcRQ1m5JGzDmQDN7opUcixP-RHGZelZAqBLFARx7-0Bc3sUTtlE6rYJp_5j8QU9l1F3sAVKiMvrGIcOgtroYsPFwb43gGbcbGOwZo-nId2IbE5Y_UHt8keqoXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGJR4J_BJjlcUf__5qK_nGUQtZLgJ6U2M9MWssBAClymmXCwqzNF3NjRb0gdRpdlEsXkhDk6aFd6o7M26lU7sQ4qCav0lPCEPrF5Oo0WUSgAtryTEZXDa8YA_Uk6SCtGRGd0maWbaJRYg_b2fZ5kbTszDuSs36BVLg3FXrrhorkTG9AYSGVh7IaT8q3_Oc-NUmDp6xWjHxmo6W2h112w85pjv5XV-gRlSYQU1NXJxj_pdnJ_rI6P3W2ftVN8FqnYkaZ4TDyu_ZaBSq3aSG9y2KkC4nNczn_Tt0oaKvWooHEjOTsoVf_efNnOMcijl_QH4wdTK69hUueOoIUiy3wsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qctzDhMeG8WlHtuF9MH1wGZ2OoM08Bc7c0J4yWDMjH_28hYLe2TMIj9j9z6al3WwyEyNqGgKZIq_9LI-ufaGhz3GKll54njTMl3BdMGyb-gYcj7GEUZbrCcmKOFYvZ82JtdOwBT1MqiQqqGJNmofkANwqsX9B6p4BRDMepSAuqzoxCqx8JUNI40GObGNzjtJ6b5s2ozmOW2u1ce_iLA_aS7IckOBlWzc7pTw3kBCudZrV6gz9_4i_c9x--PpJ4-J11oKfIxctfrYNl1CtAk2BuMtm6MBHBkzP6Aaj0QL4KoEQgHq2RBbNJz83L2HET6_1lTYhLx6Uy0EKPWTBqswPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2JZPP-m0pfXMwWKW7c9BS-BSipm4cbKAYiaum2G_2ZWz_Cqbr_3NIWZGwrWGMzwvvQJcSVceQ4D81H2CazQg_fQ_vTtm7_vyV_mKgpvHXjIHcT-Vo53kEGlgcZKsUdrjAudZobYds1xFJP6PBLXDYcZ11uN-BlHayIiFntdGwIO7HqzD74sI_kNfHUGqRbxQ4gApGAQs4yxux8azYLlsT9e5hg3niupnOXMsvkSvAB5S3ScsjAAUXqYN36QBms_or3hRmlVfnZ25JvotCPLVkjM8Kj3a-Q38gQP8AGKYBvp4Vo-gnL-tIDsbbTznOk_9deKakDDqsnAs07sNk4iTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsADrLxTqFASNl8Y3K7l-utA3lMhuO46LIU1cx77eoLMgn4Zkws299xCO17VCSb42vVM8TOYZQdD1Vfw7LOUszp6kMeHiIKfZYf-7QDA0thQHYhxDqBE7BtwneLhJ4GYZP-E3VsifwyPz27aEr7MCF74BRkI3sUGeC-Q_j7gwYTEW4NID0c-Weir3cd383D4h5m25-krK1qqK1oZIoHgsJ6fMrYz0rTdj860D9ayON-rmo6DB8rwSEgN2ApCME16d2bbsCVf5QY-6ec5NQu9RY_WdHHn6Ip29I1mcGLWxVCbCuIJvjAwwYhiNRhl--aMPWChqAnxPRzNxpW8j7_xVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulXolibkjh0cLtkmi7nGBeuwM2jPV4dpVOrMW09Wj1H3nqswKpUQ5bPSdY31SQsS6MvxVv1hzB_Geh1tPcv4TwgWyiD-VSL609A1GwmLusyfs0CHg7rEQyJ0nP26sVNGogt-6r9FRH5_2neiInizS8-Sn_-N1Zlym7kmIRA164tL9DESM3QgZIloaz5_7s1TSQPpM-a5OLfd7-Y4Sf_43RqAarLmMO6ReG-txefvC1ugAU5x9vx2tCiHGjbVZiYds44N-isKzUSs48zA-Jiw3TINzPTOMGIWJ97CHr7AFeX3DSl7WLEmiETBN0Q5-LjmyZu1bj9WQLTLB2a7oamiSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukKiEuhHFcU_4Uksx55-Kq0539MuMFG9yIF9Onu0wXBEtqimRGgFobMZuM3gLWL8X_WJ2oiAWacNW33edABsmQhSOpt6fOEbf0kX0yZzXbBQBEwtC8nWHMSe2-PZsHrYM9-3OR-lByZqNnm2NjYCNxCff7gYgwvLHaMjbDgjDflqNfAYL4DMd7F_hrTVe-aZUl0FFJjQfRpNigEMmsx-_scviHdate0TFJ29IZtn8iwlvoJDM1xS8JNYaniapHgC3qPKsBf79StwsSBhSWwFd9k0E-dPVZ6D02cJeO9v2LFqtwIBV-p-swF4yPQS34DUcY4SCI2hyH34r6eOVJ3k-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJRsg8NXwCC4Q-dlkQ5kT1LVRzT5rMH11TehnHIzUL2j9XHsOeC0MWlqqGlB_6nQr7MRPd-8RE7CCmSBbn90vPaSudWTairTpTXFkYdbFW27Xtw61ssCkDdQfXNETQfTny-xsYbqy-z8cV6qKEfKFGYYDWsm2VfMYmNwMfcOdFTVlg6RkSpdb-Kj4kZyRTpt19WHyTaIoOx990RMRerdJn084t05eD9pG6LeMd0Z5OjpFgAjK3XCuMDVuef6fv5ypZ-OyL-i6AH0hgOfkP-cvY_7m0AXCkw37gDostEZFunwhcDmoxN7zFHuQwueMgwvkLGxmR182LvO9yN6VFTRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqTk-jsHHwm-Y82KVMlMiUAM4nDmncYfpuZXEad_3gnPEwgHnE0w4XkLc4XX2jLYU03NbqCupWLL2_GBC21AXk2Y9kABiX2DJW50hJeUDzR5dIy4JB48Qgc989Ap4T-Lp9X4upZ_mmrZzrQiIDOwsvVIpmeikWmLsEV2tGioUS8l3TkoFcffyAMvboVPU27R76cRwtwePxwL4PP9X4rZR10OGfyxGwOA_r1lWeGadW_ezAKNamgB7-hzBqeh-aAe6Cn4lk8CAP1RiZ1bHrQDD75oY1nrXqleEAtdeb1EvcvRgd1Df6LuT4XtrkbWWWCI-eD1CgLOrGJyJgK1z4sBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW0UQqQ_dpzyUmYX3dqZGnbNgDRQ6p-L7juFYMRiK13FfGm7q7PyScKN9D2Hv0sx8e_8ZH68r44KAUGMmidu-M7xWYRTg5uMXxzAIcAOaToVPDyhouwFSp21KjTc_qDUG3C8C8bVA_lhEG0lRvap2lPqRPEibAII2FjGAJr8h86-JC7TQLtj_OYjeEnlBnHflT4jGfWTeNUjNdAOTLpkVf8mn_oLD4A4iHKc5HWccVrVEg90n0zh13utn66wg7VL4O15eZmCdWTVltu8OYwAAH0zqKfW8a0OfIH_1Z6sb1IRRxGl8bbQ5ECEzBUilaTbQhuFM5UGPAtROVOlmOCHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMONZZBGaEBwD4v4CLb5ZfbTyaLx6Ikt9jbjgykCuZ6_a1Lqa9GWjBrlXDk_kBeBSYFUdUiYANVqj-d4zSD27S3tu8C_JLiMI03zQVtUz8cHHIWRTfp1teb5vdZruZPkmWWREk9MFOjkuaS2KXX0KsPM3RzCst0Fjy0YarkF6Je2TpgTNPfjs3u2yylM6p53QBwIi0ldLJ-aspEymUTmsUAuA2L7Dw6_jDyF5VgoDCKEm399gSZQGK5AGZKRC-CIFKSV1ryeFAKgP62cWkqbqxBRmr-G6qIUDkNuQJP8u8hPXPavgMBbcRKY5xZ86pgDmAqIQtrUfQwy8uoZAoj8bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzivhljrpbplS33YxzrkcrdlumxsJL21u0asLPI6xEEY1seMnBXPsv2GUXauVF-RK_qwG-UOwDgxv9Al2G4hzNjZTjoAAc68VflFULVaSenjxm5BmhumJC4fWmCN4DuyQidY9yrAklZ-lesta7xTJKv1N5cVv2x7oGzwmu1MvaIVvranL-jKMQgwMC1fnGnZ9JL3IlTU5sxQwtq_BAj4-lmkGf4GE8nJysi19FZnvRl0DpTwb9CqLz8788iWmtuesr7qAl092vkEMoENEV1kFEsmTHnvOOkxD5KF45ndB3ae3YpGpVaT_lj0d1dIgW_HT1OxHjM4kg8R8ncSa3lP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ClLMPaOallcIm_RGWMCuQNJeyh19LcjD4c64Fe4kxK3HpxGMmW_GJJ2ZWZ-FCaAtlmcJiZN-1B7m-T8vHdLBckivjnePU6tNQMJKJTUUBm4cejv4HGXriSOzEt2p1imtg1aItuaQ4MUlRTqO0diesZwWRJ2_cZ-Sn3x5lKcP5m93Kjt7R4GAOQhZNYnu48_UXGe1BBUnMpd-0olq47g-AUKhUDH3QgkN-YFwz1D3n55Xf2ElBJarE5XaBca6X0qG09ziI-WDlpj2oJBIFcqbSE9wM_-GAGZRCWpXgSUSBMwOwtyEmFpPW1uUdUm2GJpf_FRuhBJLl9ZiZv7W3a840g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ClLMPaOallcIm_RGWMCuQNJeyh19LcjD4c64Fe4kxK3HpxGMmW_GJJ2ZWZ-FCaAtlmcJiZN-1B7m-T8vHdLBckivjnePU6tNQMJKJTUUBm4cejv4HGXriSOzEt2p1imtg1aItuaQ4MUlRTqO0diesZwWRJ2_cZ-Sn3x5lKcP5m93Kjt7R4GAOQhZNYnu48_UXGe1BBUnMpd-0olq47g-AUKhUDH3QgkN-YFwz1D3n55Xf2ElBJarE5XaBca6X0qG09ziI-WDlpj2oJBIFcqbSE9wM_-GAGZRCWpXgSUSBMwOwtyEmFpPW1uUdUm2GJpf_FRuhBJLl9ZiZv7W3a840g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzacY2gndDZ1GRE4hriGtwdz5Zj2Ro-rXerU98vbgNhbSb5EVyE0KVijfgdnUxiTy1Fu8DkUKph-IAXlE05EETXRxt4T_ICWR_wocOWm-igZQbwNwo0PZ_OEwIVD3W5erO_Fz9emCfC55KFy_JPODokHPZUe3RzQbcs23Col4T8LkCKJqLsNss_XXtiD5pR1TKAXbEA8cTm4b4uW48l5kB8bd3OuZi1PlBtLRPpTJGJrKGf2APlkjyNYU6egH5zc8Ca7-kSyOwjdqvvtXJDnC_nUpG-yS3E5KEn98HWIaQqNWWzRx4rGZURuud9FhFUdQSnP0vkGjoFFYMH8K_j2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=H9E7kzojkquSkbOXeLq0mupwOzAsYbYl_eHmrnoZ8UVoXFaY3u-l2v6643a6es99QiRrHh-8PoOJud4_NnDgVEaAZ8BMTDYecChqXyfjdaCD8f8RLNJEdkiG_xmehVUIk17ufi4Q5lntjH0Jn9rJkj1hKgTT8h_CCQWmy_NSuUh1b1hbKQ0KyxAlj4XNi_d_LQg7JlHsOmnQTviqLt0P3OUlI_ldxqiATvv0MYBbc0SlrL1ePIFEvgedb4jtXNpO78bh5jFik47mE_qv54GFyAEod7n7Bhan5zgVzhFpg3jlahOIahUA35-6tCPDEmXOYBEqGLZuSCytYWlOvmE_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=H9E7kzojkquSkbOXeLq0mupwOzAsYbYl_eHmrnoZ8UVoXFaY3u-l2v6643a6es99QiRrHh-8PoOJud4_NnDgVEaAZ8BMTDYecChqXyfjdaCD8f8RLNJEdkiG_xmehVUIk17ufi4Q5lntjH0Jn9rJkj1hKgTT8h_CCQWmy_NSuUh1b1hbKQ0KyxAlj4XNi_d_LQg7JlHsOmnQTviqLt0P3OUlI_ldxqiATvv0MYBbc0SlrL1ePIFEvgedb4jtXNpO78bh5jFik47mE_qv54GFyAEod7n7Bhan5zgVzhFpg3jlahOIahUA35-6tCPDEmXOYBEqGLZuSCytYWlOvmE_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=LwquyD2cqHzFXaUljetprTVu2_RN9Fx6Lo3aGEX3KqyMczKC5CwkUYeDxg9Sz7e00ReFXblIcEegHzJOnHbKevRuQpuQWOqMmZF8n7GwDm5bDq-SGRKRComVtszAZxgfl5SIm0OW9wyYMU3MtDReSjdNuowHmDEJBRvV05GjSvHdEpO34l5VGIe1rtjM3AnJKP8pinS0_solxxig22n5O61A0MAO28cXIFS9KrShBK0c3by1cfPb4gt8xkdqaxl1YUHJfTmVeYicZ8_Jx2Qz8lAmi7g1mj5-Qpe75QHeCUyeN0qiOaLjZktfGxfdlcAj81qLcQvGJeZjzWipIjX-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=LwquyD2cqHzFXaUljetprTVu2_RN9Fx6Lo3aGEX3KqyMczKC5CwkUYeDxg9Sz7e00ReFXblIcEegHzJOnHbKevRuQpuQWOqMmZF8n7GwDm5bDq-SGRKRComVtszAZxgfl5SIm0OW9wyYMU3MtDReSjdNuowHmDEJBRvV05GjSvHdEpO34l5VGIe1rtjM3AnJKP8pinS0_solxxig22n5O61A0MAO28cXIFS9KrShBK0c3by1cfPb4gt8xkdqaxl1YUHJfTmVeYicZ8_Jx2Qz8lAmi7g1mj5-Qpe75QHeCUyeN0qiOaLjZktfGxfdlcAj81qLcQvGJeZjzWipIjX-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZj189JtduA_ynXSMx3bMaMA23aXjAyUbxejsGfABX1ovVv1YCzHtqFCRdY7n2InjkPMkMpxpDIWbDR_QlHCn_h8xMY0Jgtw8Jup5CpzFcGBQ3RzCUONIWSu8orZpMMLjCsmGMP4W8RwS_-DKf8rRuoU3kYLaHgpGEBcZeWodEwpJWuMMqRcd_MUMAi_MOEDVjO0X0h-HGdJt7p9J2CLl7m5E9EPNSnjYT2owKXSEaGV1b9NLZizMDC1UKJurcCv8TFjmA6rO5tUeHrCPSFvK7kjQXy6MGdpo4s9R-UF6eIq-3vPmCrOGdWCrSNJ8jlNplWdCaze4HK9EJN4hKPs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=RIqpsB3LvuIfIw-aena3Mt_-82fJs39t7O0sdbTcLfjiFL9x0RPJxfVBS4r-rHvsdu9C0Abb9WdBIhM_M4xKTcSUAOUbUYXgdk_5PHucJSuQGVxWCGnZCMwnEYz8E0rEuohRQAiF-jJRXX-dRmzXPbNohjYZxQJ5kEawJlfmwP79qSPkQ-Gwl5IhxDZ7vP-Thh9agu2hGfxlA7de2LLWPAeSO3SlMVBDKMjXsgI7dTjrHX1igMC6JNvIitmM_cW_2Ex9EAclqRdHkSjrNqn4gG6vSLcUf1JWHaTwNDhaCGT3ZuHN4-lraMNntWH-YeI24QRNZCHxrlXoIAt7ljkejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=RIqpsB3LvuIfIw-aena3Mt_-82fJs39t7O0sdbTcLfjiFL9x0RPJxfVBS4r-rHvsdu9C0Abb9WdBIhM_M4xKTcSUAOUbUYXgdk_5PHucJSuQGVxWCGnZCMwnEYz8E0rEuohRQAiF-jJRXX-dRmzXPbNohjYZxQJ5kEawJlfmwP79qSPkQ-Gwl5IhxDZ7vP-Thh9agu2hGfxlA7de2LLWPAeSO3SlMVBDKMjXsgI7dTjrHX1igMC6JNvIitmM_cW_2Ex9EAclqRdHkSjrNqn4gG6vSLcUf1JWHaTwNDhaCGT3ZuHN4-lraMNntWH-YeI24QRNZCHxrlXoIAt7ljkejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQX7_eLm3xRGcwxh6BT1Y2fnOpaNnnECFfIuOmT6SUUBnonq-e1NDh5E2VLv1NC3oHdf7qQMKM9Yt32YZG5dfWMbGAL0NP6XjtnJViHPFWLjbm0g7XzokMQ3sBWRhVutMPYTD2f9WC1WFxR7grhtfGgxG4ehaiK-GcShb5BZ0n2R6LDcFl7svQP3bRKfFE36RVc_e-M3CRRaPULkIKwRI3e0fGiy8sS4P3bGLUTIvDZ8ajoQO_J0u4Y4Ewm01XDSfF0LYm2VHLaQoYGHa16QnOLlpay3v1AHalcamKhJQZ5GQAgZZSVT5exJBujLeyJGh5ZclHXUJkQD4hMTf3Q6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDEMKbHLqdbjEL1xkYV7isd4hyamxluaAX7e9UMN9Hzb8hNRsZqWqKElAuGRZThEodabUX6GY-YL2Ih70e0sw_5WF3p-zSKbwVu7acOkQmuuNaVEr2YLuqDxblhR35CIGzHejr3E76cs1_BAhMNCuyMpNwP_WwBIOkLu4cne-KC03B0WzjXBo47YAlY1R5P3DnYe6DxhwlvmcRBE_vvOoXGGEcqex90oVTiD6kOtFQQtifERdmpWqyMSty-d23IUfvqoNOnTsHU9u2nkF7EELqbqYRHozCdUlR5GxpdOId879N7Wea0pU6FfSve0-lhC9Va90qPiiRCoiTDQNgysuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8cSYiT8mu6cmLbEpbf--OMhcDMLut1PbFwTsczV3YolPcVZdAM37EdAJXl7b-HJTgqG5cusafok1816uL4-G2Mhv5lSAqRKI9ZEw_z3sw8RNE-AEovq9QOxg9ZpwPIN3b7Zcvu9xSuo9A-hYZf5BK7Vza8YbkHB82B8yNDeWuHaC_kGCY5v9WXR7pZ_blt3hvAC5orRjF1-5qE_TKXtS6uv-CDiETHH1BJBoLqUd1Or3JcgzFMktyUnxIRcstjh0mG_Dwijp006_00b4u6za2NJLF3an40DZxPghGs_s25wA-s-wvzgZjsPrC0Nug0Lcdqyz1qABTYmGPW_ykWPBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF3egV-remBvcmfgcB6yjO305C_myKjkCxzx_TsgkIeRSoc2vPzUn6i7uHnmXTer_z415waWIYvIyKGbOfhc-l_ILUgjbVRzE7yuQzl4bmqkmaQUacOHVEIbrd0jxFtkDQiHu-6odVjazJ40FCQdhxtr5r-FRk7GGXi_bpkOqWtd2SXtnRVwmKflhewHC19lGXXD8m1MGvelyoVEph57dxzzU-BZDBya_oeToYSDNqBSarX4fQk-rnmQ_5_rZ7G-cHFeA7Y-_anWxcDkbGbeoYfWwpv3B695pVx0UYv_kzClsZVMgdbJrq8y_8UG1hSdTmXe5ZS-ZbmE1vToJh05dg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=VCPtnvNv0WHOtXOBPxP9y1HHa3g7RzXrfnhnrHpZhXxeUmK_W-cNdq_eJ6A7e0V9N55Qc0-IywsvKSKPAaz5l3wHH_9M-R80vezwT_ZHFJkU-5PBNhEF4EhUzAS1bzED9FcBW9yETpAFJKO0H8t9Y3ebapPndg_XAQI1LT1ql0ZcKcspm24m2H6GWqEWFo7_tQvjtQBRIDc1N23SqD1rXxPsCiWlwohIH9_qtny_UpdOMSnZ851T-Lz7nPJ7PvBuRwcDlHlTa9tnRoYutG6XR8dJz8qHVY1-d311wnJiWIwzhtQHh-zYEdNxiY1l6b_5J4SMi5xMoG26c9FBKSBrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=VCPtnvNv0WHOtXOBPxP9y1HHa3g7RzXrfnhnrHpZhXxeUmK_W-cNdq_eJ6A7e0V9N55Qc0-IywsvKSKPAaz5l3wHH_9M-R80vezwT_ZHFJkU-5PBNhEF4EhUzAS1bzED9FcBW9yETpAFJKO0H8t9Y3ebapPndg_XAQI1LT1ql0ZcKcspm24m2H6GWqEWFo7_tQvjtQBRIDc1N23SqD1rXxPsCiWlwohIH9_qtny_UpdOMSnZ851T-Lz7nPJ7PvBuRwcDlHlTa9tnRoYutG6XR8dJz8qHVY1-d311wnJiWIwzhtQHh-zYEdNxiY1l6b_5J4SMi5xMoG26c9FBKSBrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=OTp5XNw4u5aska8G_y_feCScPxJS3p12bNM5_WXr2O6R2vaNjYJArVBA6alKSik5cqzaZYmvbweINbv8rzSrCd9NoIIp2cbSrW0Uuuk5X1pkfB-FFZ5-KbI5aqb6nv8UNr3Tn2X4j9UpLA8GzEKy3ECHLwQahsM1I5UePeFdVOi5VJ84QioK51eM4_gqhPYmhwgwDDbljALphF0-VZIhX1UBMRHXxY4xFe_JEL1-RPz1Fj7VkLTzx0xI7Wq-RC_WOSIkkQEOs4nbh4kETPz8lbqtICAxlLUciJy-iLRh2KYQ5m1XdDjbChiqT60fpI4niLyAVveff0BDqDfGGMo7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=OTp5XNw4u5aska8G_y_feCScPxJS3p12bNM5_WXr2O6R2vaNjYJArVBA6alKSik5cqzaZYmvbweINbv8rzSrCd9NoIIp2cbSrW0Uuuk5X1pkfB-FFZ5-KbI5aqb6nv8UNr3Tn2X4j9UpLA8GzEKy3ECHLwQahsM1I5UePeFdVOi5VJ84QioK51eM4_gqhPYmhwgwDDbljALphF0-VZIhX1UBMRHXxY4xFe_JEL1-RPz1Fj7VkLTzx0xI7Wq-RC_WOSIkkQEOs4nbh4kETPz8lbqtICAxlLUciJy-iLRh2KYQ5m1XdDjbChiqT60fpI4niLyAVveff0BDqDfGGMo7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Ez2zuCC7-TOIPRMlafXa9ellhy5jCoQI3fuT1ocl7VoFac3ReoEWTfoCtpOcC0XEGd7QzJg-abROSoCSwbfVMaFLaHiHtMBKF2INPjiATE8kOGF86YDwXdXhXq544DnzsTfcS7vRM2sEgVuCnnJxXL0DEzAGRk3m7-Dk9cYZQwaTSC7Gn5JheCiUXAV9_IZTmVsRFnUVTgAaW9xlUAPu3HtnQ8b7-Xv02ybifVTqqSt2gcgiMNKEyCShAmAuvZZ8lC5Bm99_-ZPR2TUpinocnpT1s2u_WjVnxj3k2ZAllrFmFvZH9vD-q4HOCPlD6pbcHz17jYHFylrlnhMumxYLZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Ez2zuCC7-TOIPRMlafXa9ellhy5jCoQI3fuT1ocl7VoFac3ReoEWTfoCtpOcC0XEGd7QzJg-abROSoCSwbfVMaFLaHiHtMBKF2INPjiATE8kOGF86YDwXdXhXq544DnzsTfcS7vRM2sEgVuCnnJxXL0DEzAGRk3m7-Dk9cYZQwaTSC7Gn5JheCiUXAV9_IZTmVsRFnUVTgAaW9xlUAPu3HtnQ8b7-Xv02ybifVTqqSt2gcgiMNKEyCShAmAuvZZ8lC5Bm99_-ZPR2TUpinocnpT1s2u_WjVnxj3k2ZAllrFmFvZH9vD-q4HOCPlD6pbcHz17jYHFylrlnhMumxYLZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=MNS5FOYJiisHKAaoEFTmkpPcLK_4xWQyQ1snJ0x4ElWP-C9WQCOR_6esDrEnfZTFn1optGuRnFLtdR1U88_t8qMh1CG-r4B_kqUd1VRUUcG5WFYPDMK3SR8xF6vWf0Eena3FqmWXtk7OEXUHXuzWG8xZduB6koJMaaqZ5DWf8LpCJFc6QKEASSwYn_V3n7_2Hfau0XCURWvPDx7ezNJ1ATTaixr-0bMYsRinIXa3B6d9ZP-EVOjJp-jrbMdH14uCuUPB49L4KBv_hWBWqHLQ8C6HU8PQ5T0euIlBsNMXOUW3_4jb7-o5HgJjjNrJQ51q0h1Q5oM86p8EpZZDakEL-HtkMUU3gzSZ-XSJ6FowgeWb38xyOqxvQkAzdWJMiZo00DLGeuATTDJlp8BPpyTS7j3rcDlFpWsqgF2qgXYxLkOHJVFpopxB7OuZvd8RECHtGoIIRdJPri50-lWe3wjVNyeoiL4G35gxuapFbJf_2zeuyNWWDLqMXzF3wMJY_9BaXKvu-JwMZa3hOIvsBrJOaMbFuweSJcAAzDjqAx5_CdbUQrq7e2x47DK3hMP7MBaEBpBca9GvB4O-w2PzJ74z8ilzZr6MO-pyRQo1kp-1ZEepuMaCWgUFc19pQcrsBvXMHG8J1N8p0jmtpg2QUjwqFH0j88_bUHvkpV5PbL0w8bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=MNS5FOYJiisHKAaoEFTmkpPcLK_4xWQyQ1snJ0x4ElWP-C9WQCOR_6esDrEnfZTFn1optGuRnFLtdR1U88_t8qMh1CG-r4B_kqUd1VRUUcG5WFYPDMK3SR8xF6vWf0Eena3FqmWXtk7OEXUHXuzWG8xZduB6koJMaaqZ5DWf8LpCJFc6QKEASSwYn_V3n7_2Hfau0XCURWvPDx7ezNJ1ATTaixr-0bMYsRinIXa3B6d9ZP-EVOjJp-jrbMdH14uCuUPB49L4KBv_hWBWqHLQ8C6HU8PQ5T0euIlBsNMXOUW3_4jb7-o5HgJjjNrJQ51q0h1Q5oM86p8EpZZDakEL-HtkMUU3gzSZ-XSJ6FowgeWb38xyOqxvQkAzdWJMiZo00DLGeuATTDJlp8BPpyTS7j3rcDlFpWsqgF2qgXYxLkOHJVFpopxB7OuZvd8RECHtGoIIRdJPri50-lWe3wjVNyeoiL4G35gxuapFbJf_2zeuyNWWDLqMXzF3wMJY_9BaXKvu-JwMZa3hOIvsBrJOaMbFuweSJcAAzDjqAx5_CdbUQrq7e2x47DK3hMP7MBaEBpBca9GvB4O-w2PzJ74z8ilzZr6MO-pyRQo1kp-1ZEepuMaCWgUFc19pQcrsBvXMHG8J1N8p0jmtpg2QUjwqFH0j88_bUHvkpV5PbL0w8bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=psfR-AyGZkSqdTWAJdMZ21b5HyY_3lILNjw_vTAEqTustvFCdsI_dNgLUMi6NzNbL0G-1ocwuzql3La51EFXduyfTh82Z7ZL3jvbX3bL8e3ePKMw81DR49H0mpiUW4JHS7x0OnNejJsp1GqIParaauITi6oUI2lTdNwmKmCa9GtORCObOkYohdwLkytMP4NLYjSysg9RdhjpMIpq_6bAHgUiq_V_M0QwHh_6KvCTD9LT3QeQ_1zmBnaCl6xs8euujSkvqqBqcQnjgr6aX7ix8ejHYq5x2VqqNLS9WYub3wBkI02cX4h-Kp6OeQpJm0xLE6CPXStMk90Bvb5H0YdOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=psfR-AyGZkSqdTWAJdMZ21b5HyY_3lILNjw_vTAEqTustvFCdsI_dNgLUMi6NzNbL0G-1ocwuzql3La51EFXduyfTh82Z7ZL3jvbX3bL8e3ePKMw81DR49H0mpiUW4JHS7x0OnNejJsp1GqIParaauITi6oUI2lTdNwmKmCa9GtORCObOkYohdwLkytMP4NLYjSysg9RdhjpMIpq_6bAHgUiq_V_M0QwHh_6KvCTD9LT3QeQ_1zmBnaCl6xs8euujSkvqqBqcQnjgr6aX7ix8ejHYq5x2VqqNLS9WYub3wBkI02cX4h-Kp6OeQpJm0xLE6CPXStMk90Bvb5H0YdOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ezCe-NC0XHEWRFW8ADBuwKu7srUCw6WBEOYqzGPfb6B7UkqEJ9cG1JKeMeK92FPw3xEm5-B2-nzbNGzcHkKYbv9xEJEAe5rLPgjmkr-Bgh4376qoHQuSF8aoAx0VoPgD8TBQqB651OJtV9-ouPEAaoNxIvbGjZoobmKPtjarQGSXrmxDyI3S3KRmu6QhotUXH6QrOr6meXIohO7-xW5Ml-ftmqyyKStghhWOBP4-TXNhAfEZ2yS9adtevklb1pfdbxixduyjunwiJgg-qiUpbh9Z-DgzFLFHnFu7ZVrdrtmDhUXoo30zM9rNCMILra8v8occSJxhLUIiesAxpSF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ezCe-NC0XHEWRFW8ADBuwKu7srUCw6WBEOYqzGPfb6B7UkqEJ9cG1JKeMeK92FPw3xEm5-B2-nzbNGzcHkKYbv9xEJEAe5rLPgjmkr-Bgh4376qoHQuSF8aoAx0VoPgD8TBQqB651OJtV9-ouPEAaoNxIvbGjZoobmKPtjarQGSXrmxDyI3S3KRmu6QhotUXH6QrOr6meXIohO7-xW5Ml-ftmqyyKStghhWOBP4-TXNhAfEZ2yS9adtevklb1pfdbxixduyjunwiJgg-qiUpbh9Z-DgzFLFHnFu7ZVrdrtmDhUXoo30zM9rNCMILra8v8occSJxhLUIiesAxpSF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfNeBHffSIqVTDdugh2bwM3KE0ewy2f6tS4jiCPqjpCildlPbU32C_U8xE6R0cJ0cEdd93qLxKGsf0AIGakbXbeut2OYUmZTxRZ4knXP9RjJ9BXv-Yf_GUhnzd1nXzzGzjGyIZx-1SANgiKtPd-Hvpnmj3xYv5j8aQxw9zN99KZf7nxDjJdGzw1yfjaK8nBfXOjuIB-xFJ9h_kPfBgnO4IeljWgcW9oVn5LGxmhnN75OdOxMhqcBaAnnsQ5b0ZyPv0RzzWRuIxbyZT-fJMlLhzmmufs0rPsNIEh9fixkA_WmqFazLlsxtJddIw71igwHzw5fOifWd2xLjMrDYyFt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=LgNE4r6XGH0EZPIBtgDmA6yKCe0tINxNlZ-niEduC0b93m_hn0NtAchF8mtNiCiwqjhtjFXH0kwWXNFwN-wgjG2-UEDPB4y2CYgLiY4KqPFMTuexOorT7GCeH8umRC5e7zwgSVU3dfHqDh5N30It_KDWIc1eC-iEs3YejjxkG6nSNt8kCHoAi_kLdxJsePSGOknB5cqMbP2IH428QrBGqmqsixQbqaejAl5Yb4k7WcortSuU6K7e1Ql5xxphuGmZboJe9-bfssTjejRHeaAZatedgA3KW8xs2Qt9ayCJYs-UNFk0Nw3zrdPhDPhjnx1x466Xbv2s3ngAfyZ613wT1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=LgNE4r6XGH0EZPIBtgDmA6yKCe0tINxNlZ-niEduC0b93m_hn0NtAchF8mtNiCiwqjhtjFXH0kwWXNFwN-wgjG2-UEDPB4y2CYgLiY4KqPFMTuexOorT7GCeH8umRC5e7zwgSVU3dfHqDh5N30It_KDWIc1eC-iEs3YejjxkG6nSNt8kCHoAi_kLdxJsePSGOknB5cqMbP2IH428QrBGqmqsixQbqaejAl5Yb4k7WcortSuU6K7e1Ql5xxphuGmZboJe9-bfssTjejRHeaAZatedgA3KW8xs2Qt9ayCJYs-UNFk0Nw3zrdPhDPhjnx1x466Xbv2s3ngAfyZ613wT1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmx_gACgDfCsm1ZIEdF1L4sBkDSTy_kREq9gGdh86vcCRgZm-3fWhFXXqpFWTiIsMKmuh9yulOZ7QoxJw9KSGUUUiowX_isvU0gGGWLtc-MwHAKjY5w0ooueC9x6BUN3hXMwE4qYQKMdCkEzTSgW4CLp73uETrmE4uGmVDb-p3VWc5UuGDyNvnPfIvZ9zpnwASgEF3fFZbXDinflXi8FLzgsi8_7Yh_Orc7zy7WEjjiZjnZElDaqcf0PsTxDDopvm5c6uxxqa5i6i_ai7HAbD-CZBCv40QHP5x7NUUxkEpHFQn4F3xv10b1qQr5D4kqfs_4hDwATtPYz1Naea5z-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuRulSzmitiw5-M5N_yhKVfHSGM22O0UoU4bfsE_Lrf-0RfPKO8PD3o46MndK-rhXeqBzKc9h66ixR0fznwVkLjoKDV3EV4rUV89w9O7cH3K61hKXc9yVr8DLLmfhizVpAyfTE0PC0vTwWCP-wtRy_VGEg4igZv5kAPlNykAyUfuK8h8omn4zy8uNYtaPHGQ8OwNaAc6arunh5SHBB_nBCweL_MVpptmwxCkbzO39F0BJCHgyvvljGGMNwrM05KVfNnz5gZXStqSxUrEiP3chM-VssQAT2ZLx2zVJxOOKsKRPstItVNlmufkn7_9yvCmk_6g7zid_68WtG4oxoIonA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=A5EiDN0VPMM5CMz9yzOo_Y4ber4iLD2Xbr303KH6LS6RRmnXic5ITpxrL9pTcE-nz4ABzH9X4iAaEqDOlbulBD6KJ-5NF_HaOiehuX5Z0f-gIC8yqC70vfbAqWD6sns6i85HNd3PRGdF1SR-Pz3G8m8sMUP2ie8PgysTDSarH745tQM6OIyD7JojOPOhVX8Bo830V1zH85JAE4U0u2lhClCu8VbR30uREzvWraNcC77FOj9yvYEqoAN1JDL2q9aSVp44YrHoAcU1bhvImzmrvOM4_V7umxABTtBdmVb7fnEKNvuj8eq-tMblViSE92JTHucTeZM9sB9t9UW2HyzQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=A5EiDN0VPMM5CMz9yzOo_Y4ber4iLD2Xbr303KH6LS6RRmnXic5ITpxrL9pTcE-nz4ABzH9X4iAaEqDOlbulBD6KJ-5NF_HaOiehuX5Z0f-gIC8yqC70vfbAqWD6sns6i85HNd3PRGdF1SR-Pz3G8m8sMUP2ie8PgysTDSarH745tQM6OIyD7JojOPOhVX8Bo830V1zH85JAE4U0u2lhClCu8VbR30uREzvWraNcC77FOj9yvYEqoAN1JDL2q9aSVp44YrHoAcU1bhvImzmrvOM4_V7umxABTtBdmVb7fnEKNvuj8eq-tMblViSE92JTHucTeZM9sB9t9UW2HyzQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=MpVOzw1vRu8enEBW4NlyCDaXWCIwuc0kOZOMuQ23076JZ7p5_z_X2wNTMWKU7E9jzICPNObOoWIT4UVixvjdp_PlnL7HoY-1xN4VOx44n1NSfvf3muKeUrnAK8jcrtmKmPru-ien-F-WLpPBErodIpKDLPPQC0yC-hfjPjZ_fufUEMALEHsB4_sMHZAHrwBK8tCduJNQ8-p-pQa0huq_O5IjNAOGFpuF7LBNJje2HJlSStNiNiD0TmcQUTAvWYAsnu1GvL7BKa0CSyEHVcQcJfxkhfWvPLVqCMRdUv0xLt7NjKCfNsx4jaAUCBaQn-cdJzhPdArwklDaKU7_4wB0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=MpVOzw1vRu8enEBW4NlyCDaXWCIwuc0kOZOMuQ23076JZ7p5_z_X2wNTMWKU7E9jzICPNObOoWIT4UVixvjdp_PlnL7HoY-1xN4VOx44n1NSfvf3muKeUrnAK8jcrtmKmPru-ien-F-WLpPBErodIpKDLPPQC0yC-hfjPjZ_fufUEMALEHsB4_sMHZAHrwBK8tCduJNQ8-p-pQa0huq_O5IjNAOGFpuF7LBNJje2HJlSStNiNiD0TmcQUTAvWYAsnu1GvL7BKa0CSyEHVcQcJfxkhfWvPLVqCMRdUv0xLt7NjKCfNsx4jaAUCBaQn-cdJzhPdArwklDaKU7_4wB0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=va3mUQuo3T05umVvhd7wOAGmHIkZGjCkKy2J4C0Y1MiYcGLJAdrEAFW6V-7HUEVfDRNmdHjLyC56EE7lgA4nNaqHQgJfRzN1fm98Yufwj7DS3RcjC_o7meAmCYbT-P6Sbip9XGCwQAMzOr6NxRyf9yKMvqJYggnXhroGzFgljqLpGyr-vzXA5NwnZ_2VpDYGvW0O04kULFjOOaDhYqShY2zvCQfqRoorLL31C0UfLylAhvRaVI-SOmkXjBEXXAKsVJ_SHaE4LBM8vu9h-VQeYQX4GOtmsW0h-sVyWD8NhkX6H4FHCSRQfsBJ-zaLALg9JUYODjWFNsMdFzeDGd-1dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=va3mUQuo3T05umVvhd7wOAGmHIkZGjCkKy2J4C0Y1MiYcGLJAdrEAFW6V-7HUEVfDRNmdHjLyC56EE7lgA4nNaqHQgJfRzN1fm98Yufwj7DS3RcjC_o7meAmCYbT-P6Sbip9XGCwQAMzOr6NxRyf9yKMvqJYggnXhroGzFgljqLpGyr-vzXA5NwnZ_2VpDYGvW0O04kULFjOOaDhYqShY2zvCQfqRoorLL31C0UfLylAhvRaVI-SOmkXjBEXXAKsVJ_SHaE4LBM8vu9h-VQeYQX4GOtmsW0h-sVyWD8NhkX6H4FHCSRQfsBJ-zaLALg9JUYODjWFNsMdFzeDGd-1dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlkvBHaxFIqtH66Fy7LZ5kvs6YNNKe8ZZSBRHdBbupxAo3FhcCRmnbJoUl0yWRL8VgR7RbsNuRnH42rVPty7XoH04QTbcOcEomrFv3kAEt_xfOqa0hTMyMh5qB7yUj6i2mLERV7lc_HknzlqEQ8-Jg8cHCtuUpxUCafOz6_JRszQyv71_HEFtX3QQyjYkHkRB-Rmejq_MWg0mdF5zPCiGvzVv5fGM9uGouDUPGOmtdRSMrAi3GvaEb5zQv2Y6nvfWThKuG96ljNqshtTZbU_ZQn7cA_5HjVvVA3AoZvTJ4hcPi8yBuVO-NEfkoEeYc3aCUgtB6-q-zHG7WL80miU8w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=T67CIwglR2Knk-rdJukfG2YnaLiP-oMKWwE8fTrR9o2_bpjXbPyefM9uWwNj1v1O0BKMrzHhz22A4_3AIoIt9OypCaxFqyfaeXpTD2XRSxhBiEIl0zfdPT8C3PehvtXQFtM2XF6I8HB7_bPpltVEg6F8FNbc9zn1rcR9mdbHp8OE4f1dc03-uZJFlYNvSUkHOF0g4LiaITSMPWXqNU1tVnyftYHT5EZ7uSdIJQdqd6OsmsWyZKewahPEaVtzXGfyQpx0BW_sJK35N7Cs9D8HvED_COGGqMaeAi8Rc7nfyiNyeTFE3AH11e8ga0kWXmzkcDus5sg9xPNZdRa1_9py8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=T67CIwglR2Knk-rdJukfG2YnaLiP-oMKWwE8fTrR9o2_bpjXbPyefM9uWwNj1v1O0BKMrzHhz22A4_3AIoIt9OypCaxFqyfaeXpTD2XRSxhBiEIl0zfdPT8C3PehvtXQFtM2XF6I8HB7_bPpltVEg6F8FNbc9zn1rcR9mdbHp8OE4f1dc03-uZJFlYNvSUkHOF0g4LiaITSMPWXqNU1tVnyftYHT5EZ7uSdIJQdqd6OsmsWyZKewahPEaVtzXGfyQpx0BW_sJK35N7Cs9D8HvED_COGGqMaeAi8Rc7nfyiNyeTFE3AH11e8ga0kWXmzkcDus5sg9xPNZdRa1_9py8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=tjDT_pxUSd_gKY9UXyTJWSup2rF9ZPMGMgCkRXVFM5gqB-Y990CHrbht5P2Cs_NUrQgjItpITS78_SFc_esAWEomfctWMYDJIRixChX20Ej0OoljluB_7PbNXyppeL5UkcR6FIEodqhniW-eVHPMCClmVFfx4s8i5fyu0CchtHSjKa6ohqZyDwubBD6xANRSKV8qaMlZSrmHr-GM18ZT48kK7D8E76Ebf4b5J5keWwYphiywNreb5L6-3SZEgHI9maYilUAld9YCd3V0pp9kq0dd59hmDRNlZMJBEUu4-Aj8hBEX2_-W32Ldh2x78-FLxgR5iCl4qqO9j8FeGlMCPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=tjDT_pxUSd_gKY9UXyTJWSup2rF9ZPMGMgCkRXVFM5gqB-Y990CHrbht5P2Cs_NUrQgjItpITS78_SFc_esAWEomfctWMYDJIRixChX20Ej0OoljluB_7PbNXyppeL5UkcR6FIEodqhniW-eVHPMCClmVFfx4s8i5fyu0CchtHSjKa6ohqZyDwubBD6xANRSKV8qaMlZSrmHr-GM18ZT48kK7D8E76Ebf4b5J5keWwYphiywNreb5L6-3SZEgHI9maYilUAld9YCd3V0pp9kq0dd59hmDRNlZMJBEUu4-Aj8hBEX2_-W32Ldh2x78-FLxgR5iCl4qqO9j8FeGlMCPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=IF7YnIbKONLKGcUj3B0crWUjtyhujvL9D7YAYf7nLci4CMannqkfSAjJT-Dy1XtJBtqvqM0K473eXazZsuj-3OHDIbPGsyc2PudvmC377c1gZ0-IEjs_dRWQYmItSb05xqwOntzdLHIcofxpFru00fh5GnEAzrsnRm4VMjAJy-g3JF2PNyahWxL_ZaDe5xiQUzxsvWBZPW3T8ZULwXc3da_ketaTmE3Xdjx59PKdRapHoLHZVy9MGpYX5XU5XoIg5qr9Jf-COM0PQWClKC8Y-O-os2u3TV3_ntKGmeZxdnp-wcXxFxCP7z5JRqGGWF6PLNceeY8eONhm5TiXmdIeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=IF7YnIbKONLKGcUj3B0crWUjtyhujvL9D7YAYf7nLci4CMannqkfSAjJT-Dy1XtJBtqvqM0K473eXazZsuj-3OHDIbPGsyc2PudvmC377c1gZ0-IEjs_dRWQYmItSb05xqwOntzdLHIcofxpFru00fh5GnEAzrsnRm4VMjAJy-g3JF2PNyahWxL_ZaDe5xiQUzxsvWBZPW3T8ZULwXc3da_ketaTmE3Xdjx59PKdRapHoLHZVy9MGpYX5XU5XoIg5qr9Jf-COM0PQWClKC8Y-O-os2u3TV3_ntKGmeZxdnp-wcXxFxCP7z5JRqGGWF6PLNceeY8eONhm5TiXmdIeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP5O48m7-UHHJ3tfuRItAUlaFEXh21G51XKTxYqy1VM8o2vgKsBG5gq-izU3ynxyG6MgUuvq7PTSKyYnQNAkFW7P4VLXxLOHV7tLoX7OBZsXpoA-mjzfJ_A5ucpFzT-oSBaOszoVgiWxO2KjzF4Lqa0MT9guuyAC2P5Pe4yvOQTJN_r5u58CjYQZdI-p_0fqBXlpYtM4NAYq1y4_dQg__mNlaxHrX9feHtvl1UqUTM1M9h8JAN0L81qE3DoIgQzPX4iB1XnlVQ5k9GQW2gn8VNesfAPsj5DU1_1rJGIJlOT9I58W-TZPDBRGVgAZ6PsNNU_SFPnxjThhh_e3NzD_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=fv8DBpRnvx5MKHFTQ7G5Ekhxdcl-1bSM2YOvpixgD3B43bvokLKnbsVE9v99nU0_qoLBA6UtkZ3XA9XQxK4fiSMZbMy8iwHjZPHf6dTnzyLvUpTBOMuvk1CByAPEqa7GIaZI5U9BCw_gNBIo0aua-jnTvTAFSs466zGr6wrlcDW7ooo7Nmg1ryE1Ra-Vo7jZAtVg4VA4LNuBAG5tqaFMag4A4lb1Y-Jx7MYZ-qkEe5MCdGwBA3HJJhZgCv6Yowvt10ON7skM-HdNoSHSR1BhZE_p7fW_5bwAUxrm0u5vDjTe-e3CGtRDe_LYD_fuQGNBURnX40b9CRgG3rWRisUZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=fv8DBpRnvx5MKHFTQ7G5Ekhxdcl-1bSM2YOvpixgD3B43bvokLKnbsVE9v99nU0_qoLBA6UtkZ3XA9XQxK4fiSMZbMy8iwHjZPHf6dTnzyLvUpTBOMuvk1CByAPEqa7GIaZI5U9BCw_gNBIo0aua-jnTvTAFSs466zGr6wrlcDW7ooo7Nmg1ryE1Ra-Vo7jZAtVg4VA4LNuBAG5tqaFMag4A4lb1Y-Jx7MYZ-qkEe5MCdGwBA3HJJhZgCv6Yowvt10ON7skM-HdNoSHSR1BhZE_p7fW_5bwAUxrm0u5vDjTe-e3CGtRDe_LYD_fuQGNBURnX40b9CRgG3rWRisUZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbSIBaR4GPe4Xp5bNfujjUQ2L38cGNevllLdioZOpD_b0h9mk5iRoCw1g9mD3wIHuts8zL77S_Cp6K3zPXvwLxL84XrUF019IN_vl4T9TP7yBN5frJnCIw6KmXXkCE1FNWFJ4OUHtvqGHl2kQlUJAcXHDAx7-sdJsPBUfBa67nOqTZl0W0M0Lj01RC4NJyPGnqyoCw7ingDu7ojzl6W6kFrgdH9yLG0jyL1tZ1tZKUJEdW9nd7FA7L6y3YPiLFWF1GwYnhpPi555iklEzMo1eb4VEScQ2Mz1bwonn4WxS7xW8mNUrpIbKHyA9iozgosybdUBq4kyHstqWXqPKivc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ujmjfGCg8l7w_gSqmQg8WmAaPHNGw1SLCjE6C-ShUhr8YguiNqsZWRcHoEdG2JZdVCUKYXWM2Pkii8PYNhVYSHlS5zbcvlUzsNOl_LWOlJzq27VEYQxtCYEvkJHagQfEtO57yHS6EqZN_SzzR3kEcRZJRnZt1R6QxM-BmUIhQlN9COOAcXFqRzGU5GuH0r8qizcjpFyvBXpgpHpKB4vE7AycEnwmRGG42f1FtFctuISUXRL68wm-KdmKkg0MgBsMW8Mb2qJC6yDUaAIR0j2wrJ_rCZIyMp4I7zGOEih7l0GXunOPBNQRDEggwnQGl-QV2GbH0T-ztHzwIj-t1poO6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ujmjfGCg8l7w_gSqmQg8WmAaPHNGw1SLCjE6C-ShUhr8YguiNqsZWRcHoEdG2JZdVCUKYXWM2Pkii8PYNhVYSHlS5zbcvlUzsNOl_LWOlJzq27VEYQxtCYEvkJHagQfEtO57yHS6EqZN_SzzR3kEcRZJRnZt1R6QxM-BmUIhQlN9COOAcXFqRzGU5GuH0r8qizcjpFyvBXpgpHpKB4vE7AycEnwmRGG42f1FtFctuISUXRL68wm-KdmKkg0MgBsMW8Mb2qJC6yDUaAIR0j2wrJ_rCZIyMp4I7zGOEih7l0GXunOPBNQRDEggwnQGl-QV2GbH0T-ztHzwIj-t1poO6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kACOwnhRdlcs3lpDeroJZ0rjhJqNvEx5RC-mybQPRt8uIqz5zY0SLPMyHid-HGoM809MG-uU6GGfurvPmg0msc25nzDW6UfmfA8qs74XFLF5eiUOMIUzwGWEB2I9E_m2s8WOpZS4TVFEX--N37HSvJofGcnPAGTqvrdxU3WNVPpBxTqDa8XnqdHB2yJ6B1yo1c2D00quQIJxdd2eb_2Y5jXuWYDL7I12wC4BMnR7EB6JTEqL-3yFBOZikhCSAntSLzkYkUCHEIQFqlm7z1-kmNuUs4CigBEyIPV3pyzw8Y2cPmSS0rAmVmu_p3dgKwhJptHxmHeGGf3K_CVvSmV6Nw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=tR2KzxtQbffbnGeUno1tKHysymT0eP2aXtGxHuq4ctVZXnV9CuYt81pNo3ymBCqAEDG7Njtsc0b2TvfATJCDq7Ola1NJxZGw9lz7gq8wHwElCc4S6jddkUg73712ClHLPmtqZfpYlA7SQuezUxfMbUuvb_mrTNMeGzYwjDAeRNwZW6a5nLalvSzh4yiYVKMABufaF1Jph1QmvSwgJkrCBdf-1FSRK_SEBluNddMQ_vZcowI3jDlzRKz7bvC8M0EjnP6_qFokpdyi_x8gXA1yS1fY56LrDm602_WONp85e6Oa4ddsVw3NxGa-xyeDKS5QMX_TB7nfn62MHppNnrfVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=tR2KzxtQbffbnGeUno1tKHysymT0eP2aXtGxHuq4ctVZXnV9CuYt81pNo3ymBCqAEDG7Njtsc0b2TvfATJCDq7Ola1NJxZGw9lz7gq8wHwElCc4S6jddkUg73712ClHLPmtqZfpYlA7SQuezUxfMbUuvb_mrTNMeGzYwjDAeRNwZW6a5nLalvSzh4yiYVKMABufaF1Jph1QmvSwgJkrCBdf-1FSRK_SEBluNddMQ_vZcowI3jDlzRKz7bvC8M0EjnP6_qFokpdyi_x8gXA1yS1fY56LrDm602_WONp85e6Oa4ddsVw3NxGa-xyeDKS5QMX_TB7nfn62MHppNnrfVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnbP67AFV5FeEQ9PMKohSISAWHmZiqaI34O-64yTLSzdCe_IPs76d4G68fRyZln2MBUPlqlgtrN7CNTePvbrV2RB2KDbxZFzoN3eK8JWFMjJPQk5ErChw8J53SzdGIAEMHNrMDz6330c4JzBfBvb6bZNyzUnRQ9CDwxG0llOZP_JSmOgL47FsND9p7UxG38S7r7McFpFNiQUmMtnsTpzWtATO-rQ-tQ8xeMDMzFlWxqELD04Q7mcw_AnyTisQDt1Vlo-H9F3su9E-7jScPL3C8_JwimxoOdSYzuMben5b3_WZUQf6_pCQqJEhnTbHDjsVSIxqPw1iCQczfE_2ZcPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOSRqLnCHuAdH9OrW2pshv4mdDWx3ggej3mkeVDhRc5dKkpnOgzvrMJ7MMXtZDRih2KDer0Fndb9sFRIFeqM1Cn61PpUtbmpz-CdAC_RlJ1z5_nxnOz3RCEbYGEiSlCctk8fLJS38b_JCxOXOJMuJlot5snJpP4qLCux_w51gBltHWOly3CuhoGa9hcPF_8YeOVjSe8K3KtqcyS2aI0QsOM5l5m6OxzzdiAeODV3GOYvCF38MB3JcXUnw9ZLYbaKB8HZKAePQr9zbR7Bbfy2am_BeCVQAOlPiY21PBrWgu901odxdjLjaepv4Gnt1hMTPSCnYDOBKVTzQWfHLy2bbw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=CHfeH4Y1SND8DcL3hxwpmI7Mb-pHWGhOW2A0bkoayXpuSDm27SOISZBkLYW7wvqw623-aGY7WxMOagX9DEcdXd-A216UDB1RMwipMDuH1NhKmvY6z4paMq4zRiTil_mD8kyo1WD5yce1J5mTunXyUnWxiJJL3GjzufYT62SjWQ-yhxgd4kbj5CfuFLuvNIH11w5iIFrueyGnpkt-5M5Ynw7FmXHyonUnQPHV18gHudsRlwLdyU69ckVKht53AXD_vXM68ZLtt80K75YsgHe6xi0cATzTISTlAVDBAXI_bWzCe9mVoRDi6gPMT2IfXVieDJs11v5DB9UPtsdA7IBO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=CHfeH4Y1SND8DcL3hxwpmI7Mb-pHWGhOW2A0bkoayXpuSDm27SOISZBkLYW7wvqw623-aGY7WxMOagX9DEcdXd-A216UDB1RMwipMDuH1NhKmvY6z4paMq4zRiTil_mD8kyo1WD5yce1J5mTunXyUnWxiJJL3GjzufYT62SjWQ-yhxgd4kbj5CfuFLuvNIH11w5iIFrueyGnpkt-5M5Ynw7FmXHyonUnQPHV18gHudsRlwLdyU69ckVKht53AXD_vXM68ZLtt80K75YsgHe6xi0cATzTISTlAVDBAXI_bWzCe9mVoRDi6gPMT2IfXVieDJs11v5DB9UPtsdA7IBO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3779mGrlwqAGXy_OLsAwyGEKzgLHaVcsuMCEv-S23D-5uPkgTPAtIAEOaasChS2Ia1k7iNdm26xk52Aepk7rj_0mQm7ucWovILzFCfou_TzomWBwSQ7nrSVRljwitIXzdQMT8Iq_P-IPOfhJY5mSyCm7xg8uBeusgBKbNHGl26v391GB1RGR3uxlxKFNuJUmqMcc0OFj27HBQzc1VF5hQJugP63kw03fJo583Zyzws4je8MmPS2sCqn3TznMXxYApfI3BcVi-8H0OW8fDIziesgE0WbC0-vr7xN7DNXsQi0bN2LyoIDBvTq8pyYSvFkUmd-XtVa5sa-MfzLf0z0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHTovIkfv68AVmJZarfpc99-LwG63KLIuRdc4Nd0QAL1rxqL7mTKtFEYl2kZG3fWT1k4WqcQdCu5nVzLxeb8hNRdU5F40nzkl6rRdixUuA-txa4-QxkYxuWN9cFt_7GqHYU3N3qkqqAtBtUnRsRhV07AsxBCv1ies4sT5mIqDBoxJ8ajFavSVd1oYkb91Y5idMHo54CsLn5Lm1QKiDpWmk1y73TA0tEPlwTkt27h_nANJ9iMlzyju69g4zFdn-PuDz6LBH5nm4Vwt65McEZVx3jRzsj1EZtwmXz570Y-C15TBiLl6ASyMNZxiwjhp0Ujmje55DCkIPnqn_Z9mb5Zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
