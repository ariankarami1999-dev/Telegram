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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTlxXodelZAAUKeGl_CSolqihwb9i2RTgfHoj5F0PULg6_R1ps2Z55DfHD3yEQ6dQaqc0lEzOUmFLC_gejZzbBX7U4vITdlBcuWiLkhyA3AVQb7N_0PwToznCNI6AFDwsGHg53SHI8bekdkBXHoheGV_CU6H16uIPmJvJpvw8wjzwWwaqkBQgnGEKdHB9Rm-_KeYxmk1blfd14DROqikmnQOpwM1DRHXqAYR4NnowRwCsDkZZsMVS48SvsjAy7Xrued8ABhjjPFXm2lttdmCz1-gtqGqDa0QgeWVArkK_Z5ZQOkB7sT4ytXUjnHDdAxXtlqHqlZt5lzixl69-2pyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pjXkqxNRFubABhVcJ6Hbh6TAGi1WM61RVlc2HvTR57o-PDuSLeHk2MKZbMMycoZ5_v8dy4vJVnjN7I-Fv_nw17lHRD7Fn5I0C7W2iiA65Pzq8sAKwe230C8mbDsG_N_oc2L7pgXH4cj0M-Q4rtrxwdLEOEDq29vhAwu6l0dxEWwcQSzEsUl975tpUvobQczt9P1wci3X0EEqaIDjUb9auZtYP97_Ugja5iXH5kj-pA3KKFwHuBhipb3uG9xsnhuenxZSAYPyfA5qLMPihoNby3PpVwqJbnAOGlmWss8G2oDBi2mINdhA5AqKyRMRmN60rKmgBET-Se3pTRZBmSmHgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pjXkqxNRFubABhVcJ6Hbh6TAGi1WM61RVlc2HvTR57o-PDuSLeHk2MKZbMMycoZ5_v8dy4vJVnjN7I-Fv_nw17lHRD7Fn5I0C7W2iiA65Pzq8sAKwe230C8mbDsG_N_oc2L7pgXH4cj0M-Q4rtrxwdLEOEDq29vhAwu6l0dxEWwcQSzEsUl975tpUvobQczt9P1wci3X0EEqaIDjUb9auZtYP97_Ugja5iXH5kj-pA3KKFwHuBhipb3uG9xsnhuenxZSAYPyfA5qLMPihoNby3PpVwqJbnAOGlmWss8G2oDBi2mINdhA5AqKyRMRmN60rKmgBET-Se3pTRZBmSmHgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=siw36y4HumcqOjy1rP3CFbYN6pIxidPM1veZ3PNbIhhL9NjmMQtVa-gjp9YmljkP2D503oAdwb7BSvshJEQCT8yC4pJkHOVx0Nfi9qMq_J45UX8UzXlaHjvjykYJUmh2LDQEtIYWVSySYa3HnWrB4TOcvjo5t27fghlIsJkzbtW2p2uM1gbTFmO1AEJYE8HloSpogYiA7BjQ-Xdm5NFNE3EdLgVNl4HOHu3fmVKcApNBOYaJuwT1yfurmiv5oPI03hgIzLieGk9z4ituCt2DTCtsKTOtJmUzgFitZKdEu1C7hCkqIgUs7bjBZ33mdc1lX8FRhJe8bsGm5Uioj9pRDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=siw36y4HumcqOjy1rP3CFbYN6pIxidPM1veZ3PNbIhhL9NjmMQtVa-gjp9YmljkP2D503oAdwb7BSvshJEQCT8yC4pJkHOVx0Nfi9qMq_J45UX8UzXlaHjvjykYJUmh2LDQEtIYWVSySYa3HnWrB4TOcvjo5t27fghlIsJkzbtW2p2uM1gbTFmO1AEJYE8HloSpogYiA7BjQ-Xdm5NFNE3EdLgVNl4HOHu3fmVKcApNBOYaJuwT1yfurmiv5oPI03hgIzLieGk9z4ituCt2DTCtsKTOtJmUzgFitZKdEu1C7hCkqIgUs7bjBZ33mdc1lX8FRhJe8bsGm5Uioj9pRDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vENH149oob8m3r0iWQC6r7OJAKNwfCwWGtLzEzVpfkGscYRWp9voBqKviOAjxE7dahe_CraXVBTKbcZh2bTO_bQOTWvyV_fkMo1kHeKYKlr5I5Q6O8eEU7UsJL8dGRRuY2KLiu9iz6lbm1vS2pQeMH0XeyH2_yRnUJyfyGPA7TIpkrRXrDnuZy2hvCYwgjmmCSvGgtnntTO3g58AvXrDsCeMczwliXiWMkayRAsRaL9PgfCD-iOAdRwHleJ97mqNhU5niZMjIb46LVZjzy9hZXZbRKqw7E_yEG6DI3xQkxGk7RwPZvOFwCw5lce1sIIYKimrwsGwfKar7HcpOclfgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsWbbY0E4wZ__39fksHjM5PNWmGcmVOnWg8eHsG-kPx_BNbzVvYAIRv-FXxtNTAbZYX216ey8uaSXcHwl6ZS1ALploY-5w4oHaFIydEbw6tx9p7yX5ugfc6aiO_YSlLyni-ICNER0cgaxLE4hUVPqEr3rpSli4-LcginqZTYhm6WQNothYZifehwpBr6ATLJ0VR94VWILNPyUADaxzMdxPOig7Kco60ZDOwWuZdPfqIiCJ0xq-tMnnzUpbWyDnqHCLx_Hy3TLwH08j8euYR0u87nqxFEmKBUcI1eQxgNEGaCWZWWZ73whAGOf3r-rJB96vze2u5y4ZSsGy8v0x6t8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=sgignsBkiU82FZZVuA1mhKjRIiVVPbj9_72_IuIAavdupkqiu9BiQQ00PvpAXAD2-FBQqG1HSCi-N2hh7Gy1_HGO5yFygjSHdXTqUi2BJlmunreER9j9vbUOU4FTdPFRCrBYpR80ZrfLH4S4JL8O6Y62i0HVsgKjAcdPVy-V5ALvhP317gF8qdj-JyqzWnMbHmvw-GuE5lcYN3259WZCEcIlTX83hoP31dF0W-FId0FHb1bg49QONMg6_jhWckGcP9W_2d4eNv1Dh45vVr5m6_CT_-5cEK_ClsR3PVv2a1L7C58b44noZClwXSyCqnA-biAzvUVylkyXIx6KsAPQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=sgignsBkiU82FZZVuA1mhKjRIiVVPbj9_72_IuIAavdupkqiu9BiQQ00PvpAXAD2-FBQqG1HSCi-N2hh7Gy1_HGO5yFygjSHdXTqUi2BJlmunreER9j9vbUOU4FTdPFRCrBYpR80ZrfLH4S4JL8O6Y62i0HVsgKjAcdPVy-V5ALvhP317gF8qdj-JyqzWnMbHmvw-GuE5lcYN3259WZCEcIlTX83hoP31dF0W-FId0FHb1bg49QONMg6_jhWckGcP9W_2d4eNv1Dh45vVr5m6_CT_-5cEK_ClsR3PVv2a1L7C58b44noZClwXSyCqnA-biAzvUVylkyXIx6KsAPQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=LCCcaYWg0y4oYpVdHA6YdMuK2wLH78bMW7AqKFUMirQrYAIsIsu0t9nn6Mazc_XEEyv79VJA0rNZ2GD8t8u_jo1otYlMqi9OZRFR1JI_pKFJpw6W7vmvdDBkAMHCp5H_KjTMeAC00Q8Wa-vQDBRECQXmpi3XKTfK48Hr2USMMibWKuo64J7St93MdM8G279lzd9UAV7dX8FL-hPv_VKg-q6ASomq3m5_JeIGKg3gQXoA_h-aRTmCghWE8h9dGC_PIq4GpMxNSUzo8EwbgmJQNT_kCNcNMZhITnJ871avjQzZTF51FCukI7hIQ2cEc6RfhU-b07Kcg0pSQP6hbg9oPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=LCCcaYWg0y4oYpVdHA6YdMuK2wLH78bMW7AqKFUMirQrYAIsIsu0t9nn6Mazc_XEEyv79VJA0rNZ2GD8t8u_jo1otYlMqi9OZRFR1JI_pKFJpw6W7vmvdDBkAMHCp5H_KjTMeAC00Q8Wa-vQDBRECQXmpi3XKTfK48Hr2USMMibWKuo64J7St93MdM8G279lzd9UAV7dX8FL-hPv_VKg-q6ASomq3m5_JeIGKg3gQXoA_h-aRTmCghWE8h9dGC_PIq4GpMxNSUzo8EwbgmJQNT_kCNcNMZhITnJ871avjQzZTF51FCukI7hIQ2cEc6RfhU-b07Kcg0pSQP6hbg9oPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9_T4rph7s4FcYgCsbn3oSiHkeNbYM8R-MZRTsSZH4mSu-ExQ9NBcZB62Tnu2eWduWZlLVsdf5sbE0PlP2UUwxEIjuDZtyLAj_cFPi_e-iy1_uEtffcYtjAcgazYEkvzmVBPtjt4j3hpAZBvOLHcpMAcnEJ1ck35C0TLjMF5KhVVXT3owJhV16kFKNwBzLPtCgUB-T43fVEJs4wrSDhG8XncoAavdt7REsgpu_SH6kZhG0UyRyl_tR_I9YZLrgWSUyizb4VVPsGdGGqfDAv-paPPMupVfz_gnYH7rJyS7_L8LGcS956DJywcTu0izCUfZsYztvyEAVcas8cCRXsDBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlXLldbXFCmWCN2O-7GgnMEbn_wCT5MgrsoKATj6TmgC37-7LIUOi_2oBmbRZsfsx7uH3Xp-C3NTGfbbHosFeLCcus5LraH-5hZm3PDITzdNL44T5H5iBY8uiTE59V-8kSyMYUa1TqIAVw3Wvu4LOvcb5KK2FTzin3c6YFAlIMGbyVO14RDF8hvyqJ1EP1QGEQJcZPj9CBzon0_5sYFd4WrW3svc5QrmhBWRL_5T-bCISFh1XaPPuHiZdaDrRdqY_qNQKHphh8DOjLIRgQoxEAOLWW9UeSRs8U74Q1kYgCtLqiboxJTNTca4Kj5OYeY22crHecEp7qdKhs3HfdhwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRC0exJBir5zkqh58WAknUTJHApXNtHjbB1VGgKnYADKALxtvXp2XnNV2v3ipGJpl9eofO5Buynf0q9ZCJWzRdSiNCFlqt9sm_4LuorDnwJnz1l4XoadghOOrCVgo9TnCpW-ucPuzdN9qTfvrXIZUKPTYuXP1XZ9dpQ20DMQ9uF4IqagPoxHoTg4hHHVhi_Qw-U1xVgRtGveZVkgGXU0nuR3HQHnB5x4hRSd3svockdrQyQL5p80AQ1M9AfTuUCpaJe0jHeKZ_cbhuhpwVJuBXd96VVM3O1SB0HmSMkTOYeGrT71M_JVX-iJqcgpVI50HRnMK2SYU-QgPpgH1hFI-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=rwVORBEsr2anrp5hXjftCGQP667GL7PTWXceaE7k1RlmPINaEVfQ_mKU02YI0SVlIQQYE9tTIU8MtTLy_u6TUZb0GPi8eyQN07GJqfBTQ1fXfEAHxunfnEvjEeEr1iTIO4ejrREK1jZ3A2erY_6v04lylckSfCso6nD-Ied6GLEUxxKI_hRTp-p_9Q9IXWCF7koHVOMe4lBaqTX-c0277KUKLrHZ9YpdqY9XfJ31y-Aer-XVJ2TEQTGpJEhEE9H_6BQ2So2Jl4tqzzYXLvWz_lXloWbWGRQXCN1sRs0Sp3Iw0Q3qcHEGNm5lWst4S3TTsp34xH9qq_R0zEvPlk3QZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=rwVORBEsr2anrp5hXjftCGQP667GL7PTWXceaE7k1RlmPINaEVfQ_mKU02YI0SVlIQQYE9tTIU8MtTLy_u6TUZb0GPi8eyQN07GJqfBTQ1fXfEAHxunfnEvjEeEr1iTIO4ejrREK1jZ3A2erY_6v04lylckSfCso6nD-Ied6GLEUxxKI_hRTp-p_9Q9IXWCF7koHVOMe4lBaqTX-c0277KUKLrHZ9YpdqY9XfJ31y-Aer-XVJ2TEQTGpJEhEE9H_6BQ2So2Jl4tqzzYXLvWz_lXloWbWGRQXCN1sRs0Sp3Iw0Q3qcHEGNm5lWst4S3TTsp34xH9qq_R0zEvPlk3QZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWxDiGgSspkZfk0GbdAuuqp0lcmoAXRbgKcZYIV-U3wRUt94ZM7JaxMTRCZsuW6neMsb7vr7AVY6vL-NSuSGiGnqOK9AYMbavdDthpxQOjqfuRw0eqcTUF8Sb9E5d7b1bwnv80xDbUqJmvZEdo1nZ2LI7r87xRwHllcz3Lh0FR4O1nPG5cZZ6LlSeujkaKZzO4gzVTn2X7d6mAQMcbSOw1ERT_dlWcCwKNagyyDEiqlXBjbrIFRP95-lWxsm7BQhJpKfL5evqPwozaU2FFj6RbVpXHC4lyKraVg3kaCn8eWscH-0FrOUuFeNBfO0XJke3uIPriW1F1eS0E4Mda6ZpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMd4BGKU3sC4gsiGXQW2NISE7dR8BdM_9AKl5D_wB8gyugFufE_R-5q_JQj2vFG1QSrIviuq022-scq5HhLIwdZlxF7uiFb0YDwZnKtw6fT3UjHsuwLGvluCWTcZn57HKYZT76ldpDSmaMHZ5RDcY-OBsg7DeaWYMzCyFdkPzBw49SPkDPretY2-rKx0DGoeBbBJgrepR5MhwuwYlae_rcA1DQQpmTLFceFWjTftCxAeyPJIQuJdFXAfjeHsgQyWkOgWQuKVCCAxomsYa7TYAhFJQgAfd0razqQnzlSsPAODHOTF3A5UPi4LbutozXrd3Hs-j9yDI60E5hMj9mWCQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNNBAdjDnwRblmR7coRWpx8El0MNXNYEzS1LUiAsr2pqETty40vs7SInfczGWOHsTybkaQs15YsbjTm3m9l4QiZHu4x20u4Zfm5nkoCw6tDktHxs_cAkNjudkWMDBPfTEd2s7rgPnrDKzHq2l6Rsbmo6kpzyt2SqVGsnB9jUe3gpbm5sdFkOm0nsIOOSFP3xksHgE4G8M82kkDDAZHN2blyk8nJERUdrCGIIexwe4kfVdMTLLAJ-pM86Ic_2rY5BAXs8hNw5XbyfLf1Of5vjctObiKhtnL5dAGXMGamroJ7RhP5kUgXvDR-g7nJRrBRQrpZA6sdl6WqvePmOvtYtZA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=NO90-SWqZlkH4qEhQCfBakU1eCHEx2f040Maa2aS_LS5DymoD4Xva_FnwNVq1JqJDduk6-eZGV_9stal3GnScrNkgyU7mEXSgfOEDUS0xqOfEmu0ge5c3110frDGciEzqmAQFTTEzZzxYvTy8D7tTbgTc9Yf_ReqW_4oFpjINV8zk8nZTLNuJIi3nBEG-2g9aPwV73KfIssCpdTZJRjz1FF13uELygWDeB9A-BgCPnja3YBHJ8M-Qcjx9qkmIK-Xucr5itcqAEdT15wkjBkowauGjtCqczTqll5B2uPm_jiOPCWApw5WP9bIg3NZJ6AUWaLJ2M-8mQKti-TH8LxE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=NO90-SWqZlkH4qEhQCfBakU1eCHEx2f040Maa2aS_LS5DymoD4Xva_FnwNVq1JqJDduk6-eZGV_9stal3GnScrNkgyU7mEXSgfOEDUS0xqOfEmu0ge5c3110frDGciEzqmAQFTTEzZzxYvTy8D7tTbgTc9Yf_ReqW_4oFpjINV8zk8nZTLNuJIi3nBEG-2g9aPwV73KfIssCpdTZJRjz1FF13uELygWDeB9A-BgCPnja3YBHJ8M-Qcjx9qkmIK-Xucr5itcqAEdT15wkjBkowauGjtCqczTqll5B2uPm_jiOPCWApw5WP9bIg3NZJ6AUWaLJ2M-8mQKti-TH8LxE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3HKSA5UZMZqT43-znmT2DvdkgH8oLW48mCUAstovnX86K7ULhZzQU-N2SGOfX_GivnPd2Ni6d2VbVtNTgvSgYt78U8yXLy3P90oLZKg6MKmyqDbA4S5hnAdLeGR7aay5SgLJVSLXCbzBfXALE84wcDHWM_vkyuhfT2pErT382G9eS200f4yQaY8mCieO90gA93YwWZe20m8RHYgviz38T59rG7B54sAAev1OOm1bLMokh-MNVLRGv3oo-r471-qWvbpFpotcRL6wPqDUtkIT_PLeRNRIzhXPFdVlx9wYc2YIsBRXRBB57lOQi7IvMsR5dW7OK8Svyj49LQ9n-t4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjDPP1_QKlwoHl6o199_-zow07W5EJ9NRiLsRS2avqHRQ_bb2QH2ermD7O_34XAimVd9Q5cj89WNOW5xG8bsVN0ZPeHkageIFnLQBQJUqPP4X-mPMKC6RpSsGvZ8p2LvQ0fxynoowP0SH06_QswpBhln3WhYQqTvaLBkQpliN7x9KjXVZaiTnL7nuFVENmV1Mhgi8giWbO0MglD9tsj0P4kIqiHXXbI2i2hltWBjNXnrgAke5XCdG9oPmsHYl9gbXtU4uckJmKpbA2UlCSmTwBOgmPkjyeb4MInvsyaXsmXK2qqgKHwy3FzJf_0uybC4CcPwDIfu2B0ugjehXeA89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK6u23yVFEIt-B5Xjh9D9RzLL-1v0qpBIKdfjPjx18l_cgP-uSyqQ1e5-kW7PjgeRLGmkpWSc2COzKPx6y0KRmAJE31PBAr2hMMB1qLAbH-jcjbgy0qmMdJuJLSfHiktaODMNHtmnfH60mnOPU74NZl80UNuu-JqojfO-7QcAJ_YccJYP3re-z-Kwr_JZh6IusMPg2iZNpbbIOyjYMw0Gr_qZPMT3__Oy2iU_1NQuEgNXmX4YRoBhghnRX92SC6dLEZNVdR879iL0p-k5sf2orL8OFunYsyiFFD3JHoJyOnwbFxNDVxp4U6EXOGNl6-7eGHjm_JhjIfc2SvHUQ7Hsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=gTwmyPn7smFZ67DigaDikB_2IHtQM4GZ1JVJSIF36zS6lR3vvV0WY1rTrJfaUUcZtpLFtdQqb6Am7w_nq5CG0aYdzEW-MO7d_1AUkebH3ZDFQb_6zJQG7Rj68f-L_SKV2-fRvOUXzW4r115qgqF_K-le_qKf5OHSNnNYzna7Zux0bGwNfhpMAi-xAoxj0_tHnkNb13LUNynzyFs0_jR-PPj7-LsAF4wlCRAJcHRBdwX7FGW-hIrEuwsXI-wCPHp3fPSWIDHEoUjw1hrdq2j-NjHqQtW9ud_X3iyht3-jg0u181Y7cvsuXbjIPrauDQW6UZm_mUq3KdvGEg-fCJO7UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=gTwmyPn7smFZ67DigaDikB_2IHtQM4GZ1JVJSIF36zS6lR3vvV0WY1rTrJfaUUcZtpLFtdQqb6Am7w_nq5CG0aYdzEW-MO7d_1AUkebH3ZDFQb_6zJQG7Rj68f-L_SKV2-fRvOUXzW4r115qgqF_K-le_qKf5OHSNnNYzna7Zux0bGwNfhpMAi-xAoxj0_tHnkNb13LUNynzyFs0_jR-PPj7-LsAF4wlCRAJcHRBdwX7FGW-hIrEuwsXI-wCPHp3fPSWIDHEoUjw1hrdq2j-NjHqQtW9ud_X3iyht3-jg0u181Y7cvsuXbjIPrauDQW6UZm_mUq3KdvGEg-fCJO7UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=FkPRs6YihhStM2bVMnx02CGR4YfH_OHCOUBCLIb8Bb5TZOg_8QVe5SnDWivhFP51pWhJtxtG3S5H8uv7xmCXA6nRBNgozVcvSjJgcgs8D0XsVr1iVJZMNDcsAWLdHtm1rMcOJOp6a2weGnhS7CXQlFY_pxqImF4ed8ERXRXbSfxoqtt1Pxz0hViMB2XUV8oJKRVB_vhmBGG2SEbhRRsh0LEgdeO8Kz947GdBvHQO-sXQowR48vJnyMIVMXuuUpLjNxLuuK90Vn0EjDiFa0iQsPRS6A7ks2D0OqVaJdJvasyNIw_I_lgIOv6nQS7_gzpEcJbkP_OZdIcF6atDks--ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=FkPRs6YihhStM2bVMnx02CGR4YfH_OHCOUBCLIb8Bb5TZOg_8QVe5SnDWivhFP51pWhJtxtG3S5H8uv7xmCXA6nRBNgozVcvSjJgcgs8D0XsVr1iVJZMNDcsAWLdHtm1rMcOJOp6a2weGnhS7CXQlFY_pxqImF4ed8ERXRXbSfxoqtt1Pxz0hViMB2XUV8oJKRVB_vhmBGG2SEbhRRsh0LEgdeO8Kz947GdBvHQO-sXQowR48vJnyMIVMXuuUpLjNxLuuK90Vn0EjDiFa0iQsPRS6A7ks2D0OqVaJdJvasyNIw_I_lgIOv6nQS7_gzpEcJbkP_OZdIcF6atDks--ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=HLeLnQTrGDQ-d4IzMLf3X83pSaoxfh4uMKHrtn6cWDDNHZY77Rlr1cYEYSXmYQGWi2-19ZxXVqZSa1C61s3Bok4uTV4TJ6jriUxhB4C9veEN_0KWqsoNtgGEAikBzQsI0bX6025D89PZcuuspl09juBBDjD8Lr1robzmwXkH7ahyMToGVdL2_YxS1wq59zRrBKBI0kvAWbZuv9h0LTPkprTQ7SoAALu2GA5Dx9s_hycWLTl4w6b-ZDiS9cJxgepfu6nWHFJMsS1oeHGVyi1EsL6L7Q-LXHg9tWHZ_jVBYqbBUAA5TyjyzCIPyquYNHJ3m0jketPHMDA8jKz0qF5ejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=HLeLnQTrGDQ-d4IzMLf3X83pSaoxfh4uMKHrtn6cWDDNHZY77Rlr1cYEYSXmYQGWi2-19ZxXVqZSa1C61s3Bok4uTV4TJ6jriUxhB4C9veEN_0KWqsoNtgGEAikBzQsI0bX6025D89PZcuuspl09juBBDjD8Lr1robzmwXkH7ahyMToGVdL2_YxS1wq59zRrBKBI0kvAWbZuv9h0LTPkprTQ7SoAALu2GA5Dx9s_hycWLTl4w6b-ZDiS9cJxgepfu6nWHFJMsS1oeHGVyi1EsL6L7Q-LXHg9tWHZ_jVBYqbBUAA5TyjyzCIPyquYNHJ3m0jketPHMDA8jKz0qF5ejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfCGUIWzF4kJBc7QN4i8a6bvsnPldctjgy-jxR-2izqVPeBthroWiB8ZxHqpmc-qxW2dSpZqLqiueWY5I0OlM_8mzQvGr9_OP8avmWHKy1LAjCqlUdqfSDFbWgt6Wz6kE3rbHkRrIuuWA24FwN3aRUbiTZxzvioH3GEwZZQfJeMQOmeqDoCPM9Sj6aBbfwSlP2zChbcugeacq4YRjVUpHoINs-PF9RRHq9eKRd-ovnVN813aDcrlgiGxjwyDXt9C3JkRgAO6Yue7CG3KQYrM71OW-thrhUAFJfs9af6P_ujhZEMRQu-Ypbp3wQCh2qsJ9x9Zdaj6T_L38hQFv0FFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw5fq6Gx4rJ5B5NYsuqWGi_bqNJwGa7E7NRzcLKkhCF6NVrD9AAP-sREj9Pl7c_xS7LCeHxMSunamIz0J9IRf-8OqENRkDHBQjbmX6cbOzhdQel-l85X7pNK6y4Uo5lH8aVUxSS8yFLetcSO1hRBxPsy7mOhnw8CephPv105AriCQ6An-ZnT9u8J72j7QUxDPNYX4-WExUHgy6iUIGsgqMwk_axbBL2IMcNLE5prhAEYOsFdbi2OKklj_LTztEfXDd6ltkblNEmx8_TS9HjLaxRjFcD0y66yyeHvuJAIUNekFkIQW4KajVZFR7uAGL1--re9yDzGA2Yqj7e5tBrPCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKKKtYsMR7wilYfqJcEwcZnYR03I71VArbfLY0oqX-Q-SHB0jP5Orc2d4GospL9FRP8xgV9-jDjze0rpoNP5qdby5CL2CIJL4zXRWhSbMmGmFOwCklN2Y-TEEfjA9mCDbtfAADlbmkZirx9LGbY7NLuxKzzVuDMEgJ-i-yjk8bOjWPjtWDelrzU7JcTHnH7JyhY4Ze3luzJSI_H_DtS8llRY5-iaOHEgSu4Pfau8RxNaQwKU5fDQvDH1hiqiFAjje7spszMylFFDICeTqXuetblvo_9RKP37ruhq0R7kAhAPyWPyGQbyWBc1cLYm-8xyJqfQWlmYxN83cz87RcawHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GiyVXhNFliqEvKc6quxyByyC4RDKBbHFvBZPkDmCezPSnz5g0ndvmw68CaTKU_1Ub2QzvG6wJdg_xpY6rPtafdG_N0wTksAVZIUmk5XvFXZ4tS6MSz50UrESr536OutDs17InAyaENucaOKDcbI6_GFrxkS1qmNJv5H2qAWzmKYHBGTZdSHtUo5UeZBOzPOCWvInboyJ49rBZUNMy0L8AhFO_wtuTaSZRN0EaOGdA8VR2f10czTkdPx_yGq_zH9YgLDD4XQVnwCeb6_SZ6H8Ock-eMLTgVyL7Wc6NUlWtcZO_Ntn60zLrfgKyhBYpdzkjLTwX5D5RFGWArdTZVp_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUKVaLZzvMrtYkbrrIiW68mtZ2fNxHLLClALV0VGk4LBUGlg-yvHNdPPm6lPdhrSAsue0x9DForLhBVwoeQJNqFOGwJl2xwVM-7ljbr9ieAkC0ANhxyRIWoMSuSIiNKSj24ldHVcPGvZXeC174t9-HM46BPM-IOjsGY2wpwg--yEJtS99ytW7QRo_4FtfkR3MKlC5XkfUJ98mtarxf87Z21I0MlUwUh6wqJli2ls1xJbOmxwB-_lUxzAx_gV3Ir7lLMV8o0cTJBgvcxK7M4_JuJXyLI1Kb7kATEBDh44Obuku8q65vedHiY-WKsYNVuVhkzmHmcXa1in9IqFHYWQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPDA_0UeobwHx9WyvQMkrfL7sc5U0EMx6zSFbjKGu7mfKtVabScQo55mh1WqXcm-s3HLVj0ZpMe0exJG4w7zLXlUnekhvWEHNvKwxQcNjOxbbW9u1nDue5zaj-Y1OVSP070zJBvKhZjZsoX6lp9n1rZFt4EPYbG2QlQW8pTxfdBCYXexCqNdkArlBYkWYxUQxNOK824qP4iz8ZLEOeGUvYJx9eJSk92m2pzp9LBcrcTnvlDlpt5QCoqddAUnf8Pr18co-I9Ra7zixb2wN5_WgLL5nBA4DQNV78E4amTIqsh9sqvGq6chKHGPi1QlnWAe18f4lZHysGGh0LAQSyJI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5fFlFoRQqYFEwmGnleopoOud-wEZarXm8dpOsfsas4seVYWEW5Xg3bohPf-OBvjUHuDFSvzyGKn-kW_Zj6XEPSADiEnU0Tg1vW8VVfM-sunaFqLX8XDSrSjYPXBBgmvnJtVcfEKSpOYN5Gy2vUyq26N4yLfoAmyRR6psPH4-ztcb63mqUhPHtYYKfRImzJ0ieWWWthawXXUoclWHyMTMx1wMqFH1ZgpjQh_gzrM4QFnf-CVpriFdAakVCePU_bIE9Q_Oo1-kWgV_qlwzzht8AOlUtpb8Cq3fiDE-4bHvU4YuWf4he-Dp9WmXQsK_Bc58a8m9EkYir-tMCbsuCNkXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe2dZMiuvjA_kwwhdkGDMCZSW_o9w1QwVFfcHbZNYHcN34zEI-iFEOqFVVZs_XO1qY_PMLA_LkOu3MIpSHKF2gQ4RmVY338W9ftupV9vrodaNJbC8Nhv_Jrukn1CtJRDmJazFB1oWVOK4728pHZi0nxvotrs_K-2ZW3IWljtV5x9LsQi69NJF9NQK1dH2oR1nAHEdChHVpRq70MUcCJ8llLUqVn93zbzhskPP17B164KOABl5_6rLEfXLCX0aYQEE-hWwau7ntYOUUESCjGyBq_hsTzU0ePfJKsRwNvHoOrLFnqRHVBNkvwFlN3Ck4de3bNRTeDydQnzhpTopk46Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlhRGa6VDGKUccxjPCRHKLHK6sloigG7UN5BUV4Yy14kFtaflsA9kCBZvN4YPvVQCgc1a8CCc0P_OylWzztqlUlsdLs70QATT8FAED4tXqwglZGACxgx98fH9NCo1ZLnQwF2kBaazu_ezVZ_vbgGDpTStSsbWrpwsL6KlFQosP7hOfqfDJ9kk8VjeIsMz7gSVjh_32iwce4v9_Neb6DlRLWR98rMKhOPffUrcXOedLmA3KoDtPZsfXjCe1CyqDD3HvrfGh6ls0TedQK-DsB6X48snurk04Vivga2G8K5R7nfIkzMC7HBhODuFKQsDD2E8ZWicWOnEhcX_JcCGt-4eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJozAETk2FBRmC4s9AzRc006bi9VaJbJLWbmBQUYAbPWeC3U5Mqg-KkV7dmcGdF5H-RTY4ccFOkweRos5STdNTG8onQA6wI6-2sH0LKL-UzYAw6gsw1AuEp8OUCQyjOMXtk1yY6cA0_mwJ95dy4F4S7tIa_Zm-DeZRnFc8c7yEOj81IZFapOsQnIIM96uBWTFu7SuX_oONIge6XKqlcXShjTSrPxJPLucmRhS5b7O0U4HzYmetzKu3ilRABPkMwe377RMFF8b6RL_hoKjtHwD2IFAUfRxMlGmc87Ibq-NLb8HkR7OXzabiDXEAlfQP2tjZ0rceh-VYCY3MJTU_tJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxxkLrZDejDMrLIBlUaAnsWCa10ysawAMQnP9ARcsw2Muk0hfXerzySRBF-Gat24__fWro9M8jBItp3RvFQVOXmtpjqGXTX7HjFAUbCzN5ftZjY2PnFAEWsrNCBD9yN7UIPz4YLsze9MHL_f6TWL10Bks4Z9xdgl9HWL27lPUBGUIMg7Xv_Shy9WfIiLGB1VyfgQ3JtVbI9rjYhymkJ1l7Vi_IojzIbmviIzVJHOZR3jiVFiWxnZNZdpJYDlzZ6cXeXna3FTRSrcv_FndHCce3mmUrJ2j1M9v1XSJFalejZ0Ti9wHSmkr1SFnyEv0tZcDEzqJaRXi8bSA_HzpCrulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVZ-Eda4JyjDZUN_J8WRdPqhdnZQbgTYs8_BtBdqhbSJ1jNDaL3-vS7RP4kHlXNpoRTJogyd2IF4ZqnWGNSB0mqU1NZS8LGttz0NVLULcCL2RnabPjiqHTXft0BTcAYYaiJORQe9USZW0A2kCU82yHbct-U24o3BEaNh7p7viuoUOjeJNKblMVjZmBY1NRmEKEem_cu6qROPVH5R6kc1xVpTK5jQNUb9q0yX7_J_Drm9XR2cZW9N6d_a9Vg7_STPoRKhOfD-T1F2qq_bHKLORr3UlIFQnW5lrFsej_rJ-fMtK1qqUwid7wHYNQiFPvo9j1WoiZl1V7WvnN3jhDmVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIpA8bR61UtsLSK7Uf1sl6deyy2kvOf6toDK3Zn8Jr6QTslL9xFcuXLqOHHZ3YKx57Hhlli6YTSlCkcQIYbcupRlIUt_15GqB9BUoR_4P-z9DV_JP41Wyj1up5nHnLPyVioovyv0VVLHcMyEW-39iFPtUa-qeZdOjEtlFlo3XeMOBconYdcaQ3gCl5fZ5F3G_ThTRORNz66jPribPAyNxkfYMsbP8UHePxbyIlz3qmqooMIFjXpFEKkQZ7OJH5qSk3SD5aiIGD-s_j6eAyms-QSaU8tMJprPe4SXJUDPlSISuMwIe_JCLFmP5UTg6jD1hoz05Rl60sv0ZqsbqSLLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnj5qlFuphOMA1DBMWkFIRcsHwynCpp8ffbqsEVps8Ljhg6lrIkHvzZ6sPgyKGsPf9QdxyR3M0NVPbJMNHw6jiKQBz50R1AT6SOzhpA5PcKucQMzaf_H2G0MgqfJeQ3GXo1NN4ZJnz-gFwp7nJHqoadPR_g-3SGn5cpKgAnbSC890aS9Uyxzo6ujZKypCyF-p7djL-YgdrBHLMJovlAOZKJaB33VXyEzCXxbs2oxLlK8I0Hdo6yJCTnl_8F5agE_-5sBCYsNjjHBQ5ms93zvdZ2A7hCyv6YsVTBptQNXYLxVIY6QG8EPpBESfnvxpwyPFxxsujLKSrcrHe2uYeCPPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2tqMFJ0BcxTgc_kjdjWXdnyl1rDZz1ZsRynpSRfTL7VldocRAzCzeMUrPz0WEpTcxTm9gFueeA72qMAdUqlsKUADoIncpLqBXnHyLvAlo9yOextxV0yLPqanseaHExlYbmARCQnEMqZIztbW6U_fs9JW2lvMA1sFCWcs8eJF9xtCTwdiCajeUsOWN2uX4jjJ2aNMYgMYRukFoFnaZ-bTEa9h6xRicu6VetdAd5zpkUjyIxSqH6zn5JGn0vjrV201QpLvXaTiCKr3Ue2Q-kxWoiIo340CvjX49AWxwuq-0b1PouK81BX7HB1npaWpVHap7bTjXtodSlP4nM0_dc1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=D5NdUd2NWGt6Z2YZdNv-Ctr1faxFraxaL--sFLj7ResAD2Nh6gwnF0UbApcYoCoxgCUXWqLsD6k9xrcoY-C81LWzDLuB_rr5eNbB_h8J9sQGfkKWYmt32uFLLKew_LZGfWGyfxaa7345utqigrbn-Z0b9-AvlTm1v1FvaBaLkJg0BcT_Gv06yU__32oy16rmLKLLvuOIbh36uWziIH-lW3ct9-LOA35YCUk8u3zlyHrI1fN-kZENHGlmBoPEHgXCyMQbfYpib1pz4l5QoAutD2rTsMHB8GuI0aWmZidCBPotREX4P9qCqKBF2JiaEr63YUvmnG8Nd67jGXfBaqIQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=D5NdUd2NWGt6Z2YZdNv-Ctr1faxFraxaL--sFLj7ResAD2Nh6gwnF0UbApcYoCoxgCUXWqLsD6k9xrcoY-C81LWzDLuB_rr5eNbB_h8J9sQGfkKWYmt32uFLLKew_LZGfWGyfxaa7345utqigrbn-Z0b9-AvlTm1v1FvaBaLkJg0BcT_Gv06yU__32oy16rmLKLLvuOIbh36uWziIH-lW3ct9-LOA35YCUk8u3zlyHrI1fN-kZENHGlmBoPEHgXCyMQbfYpib1pz4l5QoAutD2rTsMHB8GuI0aWmZidCBPotREX4P9qCqKBF2JiaEr63YUvmnG8Nd67jGXfBaqIQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIUIDC9qI-bbWIS8Z9jYrs9jLmuW0A0NDydHWeJ4cYba7TMlh0QMceE8PkNSKq1pwlk57QWSt_Ob4jVF5FK-raKRxf2XlCWSamd4ZWTnNE9zK0ejpP2bvMQrn1LGzEk5VaPWlhtETR5iVAzTmQdkCZvuHFdLVBXQjS_7PIwq9ysMbMbjBtJ3L3pvTIRqOYaWrgMGm9hALCm5PQ6glYnf-1qImECiTGdx_AD2wKxXPivPBT9KIkKAdjjI8DvGCTieTTHSA9GWMwumYqQBsuyTLsFa0fQxPZsLjQG5znc58K7L_-RX29Igf51VZfbvaZRYfC2CtOA1h-ogGvJsUp0SZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=Q97CcTOWJpSjp772vemrnjnm4BALqhOVduidDeM4V9zsErEOW0x8cexn7EVSd7EZfWrMXfqMaPX8banr8tib1yHZY_UVETIjWxVBtZ4ht0fNSeYL7Z-sngXjiM_0yrodQveg0bKAf3oynwuGN4GXyNEIESCAyCN26jKr1iSG9atJFIbWuoN7R7ARAhcFbdtipcaFIP0ysaJw5TjXOxWqdrfPqELRscrAGw2WSfGY0gYy5MJAUPliYri2tAksfvlpSYIY7Uy1ixzeS8glWNOJrMtdTu7uXDN-L0KtV7-8Y-Ez-8aoqdIdLKxynF5bWx9cNL5rGPxzGukh2LU5YrxyYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=Q97CcTOWJpSjp772vemrnjnm4BALqhOVduidDeM4V9zsErEOW0x8cexn7EVSd7EZfWrMXfqMaPX8banr8tib1yHZY_UVETIjWxVBtZ4ht0fNSeYL7Z-sngXjiM_0yrodQveg0bKAf3oynwuGN4GXyNEIESCAyCN26jKr1iSG9atJFIbWuoN7R7ARAhcFbdtipcaFIP0ysaJw5TjXOxWqdrfPqELRscrAGw2WSfGY0gYy5MJAUPliYri2tAksfvlpSYIY7Uy1ixzeS8glWNOJrMtdTu7uXDN-L0KtV7-8Y-Ez-8aoqdIdLKxynF5bWx9cNL5rGPxzGukh2LU5YrxyYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=KSNnp8zX96Vnlj9Le_qpzmB4fxZrjrKPoqJ8PQL_4dOoIT7iMjY-uubteOGfV37bI38UfeBdGWGXJjqMbQbTcbIqVZ1cXZeDhmiZdQ6dSTb9KlveMd80B_TWc_Di314e5kNuuwCiVPLORA2Q1LhNybesaF5aE40JX9xrelwl3onC0thoYwko0x9p7YgQk0KQbgwbb-qySkU3ZONbr0HFmDMUDONuuoop6sUGkFHyuTlfqpUGQWYVZ6c2lUYl6Yp5DNDYkgfiDJHdUTYyz4BaofyQvc4346Gps5ZQwzMaOCAdxBjqdTAQdZQANZbjEAJbO-5xmh2rjks3CU0lrBv_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=KSNnp8zX96Vnlj9Le_qpzmB4fxZrjrKPoqJ8PQL_4dOoIT7iMjY-uubteOGfV37bI38UfeBdGWGXJjqMbQbTcbIqVZ1cXZeDhmiZdQ6dSTb9KlveMd80B_TWc_Di314e5kNuuwCiVPLORA2Q1LhNybesaF5aE40JX9xrelwl3onC0thoYwko0x9p7YgQk0KQbgwbb-qySkU3ZONbr0HFmDMUDONuuoop6sUGkFHyuTlfqpUGQWYVZ6c2lUYl6Yp5DNDYkgfiDJHdUTYyz4BaofyQvc4346Gps5ZQwzMaOCAdxBjqdTAQdZQANZbjEAJbO-5xmh2rjks3CU0lrBv_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nICbnC6sAxJAhvMnz-CmwQC6cvocZf9dKm2MbcaXR6XqqK6yxhXh5BAxnrOR1o9GF4RBtGUZAn646L8JGxf8OxL3TKkf7PuxCh_8zTK4p6QJPyTtIDQxyBYhV-D03HRNP2Tbp7pUtuMi9AKMHdZ5l34ykXxAfabAfZTIbIbe0h8ObIxY6UXnxGA2G5JyLw5f_GPDHbut_uTwI0ZLaoVmKdJAk3C116xe2xTGfpyejjaSa9gwmoQR0Sa9Zf6SArQ0TutFtDCxRFavD1ii_hhKOx_VOxR77S_QlTBKLYdCqFzd2KEUECraEO6U-GfTHvcot5rx_0SaQgqpFyJ2YB5PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=jFEPBnLrcFsXR43klYFzvmTVydf7alsuuDhvK4kuIfpeWg4bFITOpmhJ_IvNwojwS0f2UwR4WdfLydSmyCbk59NJflsQTwLRLUi81lwXw8ZD-KBkSZBFv4bmp8h3SffL4DUsAN5y60fZgI9JfHr_7xk3O8O8m_yad1DP0saAF2K6OKNbSK5HdPGVZbRhvVWg83mrRCDqS0fo-BmNn2Wz5hBZWeIhGgHQkqSZBt6rGqFT7FAl841PDf7ti-QoDP6EQiHTCwS7RC77w69uONsjijV06NtR6PtfGl7sROnM4UpGk2sRt4GbwIoaHkhgypCzxyVSivInm8ET4ACtM48zrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=jFEPBnLrcFsXR43klYFzvmTVydf7alsuuDhvK4kuIfpeWg4bFITOpmhJ_IvNwojwS0f2UwR4WdfLydSmyCbk59NJflsQTwLRLUi81lwXw8ZD-KBkSZBFv4bmp8h3SffL4DUsAN5y60fZgI9JfHr_7xk3O8O8m_yad1DP0saAF2K6OKNbSK5HdPGVZbRhvVWg83mrRCDqS0fo-BmNn2Wz5hBZWeIhGgHQkqSZBt6rGqFT7FAl841PDf7ti-QoDP6EQiHTCwS7RC77w69uONsjijV06NtR6PtfGl7sROnM4UpGk2sRt4GbwIoaHkhgypCzxyVSivInm8ET4ACtM48zrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQFXnlOYUgxgxvUMLpWsvCI3yGd08FJv6jg83WoQhHRtOJ-K32J7KEUs-QpXUnWep6Z6614Du3Ag0pdv_sFd2P3IjKp10yug4xKwMvLftsAEchDToGS3qKTV7HJo6gg-9e_oZLhpEQiWHvS3JhtA5Jzfg0Vu2oGioaNqDHKoBSvsY1qQplCe6vtrre_59ca99JvKivnEUkerfKQ0wBUX2fanfzINtT8j6xhQ9D9-bKoy_bjp0zCjw1adbEy-RazJ17AVn7w1LqynxwW48RPTy53EpKpC2U7ajH0shY-rfNOHOoc5_-s7nM1L2pqNJgYy_pBYKq1RUhV5AsrZJUhE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnnPobsmT44FIGnAYk1Un8UfzI6evDTL7RSGT-42JjIeihEWPJCx-ZZ3pB3BriIvZSqiIcPhg4yaG07GR8nShCIpadmgTJMA8XwuUC_1WmdlZnx2kXpfmco4wzGe2CqNRO9Nl6N4x1WRFeb6ZBRp8vyrv2c6WejBHzDftkl2SNWu42vEwKLcw6ptdZBl8zzliPcJb7_vsf7MF7Nx3WGLnEHcAfBIaopLvPPW12Lqld5p5HQVbECMgJG-0KwZMmZyoZLJonSaojFaJp5Wut-lPblkVVNRpmMTl1jAgzzr_Imeum6nibsW0uqyFlU8e5F8GegvspX2fOelP8_gd0Qx-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vb0RWXdQHlv98J8EPwh_7RM89r7pwQxFdye3quJLwj19CYf1nopllW17KnfHNjGSOTrpKr2pkWxVm3okrLlY4fvoaZrEmUU-6mUyB4O_-wFxd080j7O_8puFGLFet7W8u1scQt6yuJgO_GCnkfFGU1uOISJK5lAf0Yu1f2b7WyZ8VnC8CMZ-2pzNsa8nc38_CfnPtzmFOO98JW6uhypS4NJQY41atwPQ9KRp_5oJUARSUsf5MpRgUwmk6uLhGmgROZWxPSdatGNhv0X8dlZ8CC7Cf828LDkz-JyRvPHnTmzgNE5-V1stnMcvEqP9SrcF-w2dO7OozpiC0QbksbjAsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHYLPRs16biOdYTYF8FWaFnYhX-a0L5ppcVkNm-n4iCXn1EIj58sT_71PyIomdDVlGb9-u8dTlACVFewwq2RMRghsk4jwcx-2kdmM7D4piskX-lUMeblrCV0md0PESkD19ugOHjcJPdfHEpGz3RqZVKnMoZv-G9n_hBxkF-QvXTXOJFJ39z-BZMzFH6SU2zNf-Lkk9FYI7U5K-YSk6T3feSnqqCa35KtReiOtPtKluSTuk7fC0tMvWX_SOx9XyRyKTc0hQKf0w1dZr1L3V6yBQI_4hwIVBO1rLUJXGCV9T7MH73ONKYMGlLGkNOwtU8BSPwafwCdv_8y06pP7y_Qdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=P89WZEQP4g6m7iM-jHItqbXPOb3Z7JTYjhrBz1aXDFrQW-ZyMM5zUtkco1vQcxxBurysHo7pB-uWjpHP7uCcxDV7Zg_3fIqB_zHCL73IVnXrvzkl1KWfQM7lS2SnhYA6WoxDF03L7k2gwLSjAZT0ISN4utPPR2jOzUsGEEDCQqjhCMRWu_kyAjD16j-HY9cZDc4aCuZ1vVWgAWeg6wIKOUUcFtRc-JbnfGDJJnflChgj7hQFVCaEMU2gdIqVkm20kwt8UyY8ywzXEKUXdkQt1bPiSsASnFDs4cDxbK4oHg--gEh51mAu1mPPuwUpinwAAvcHgF62JIbteBveoBtLcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=P89WZEQP4g6m7iM-jHItqbXPOb3Z7JTYjhrBz1aXDFrQW-ZyMM5zUtkco1vQcxxBurysHo7pB-uWjpHP7uCcxDV7Zg_3fIqB_zHCL73IVnXrvzkl1KWfQM7lS2SnhYA6WoxDF03L7k2gwLSjAZT0ISN4utPPR2jOzUsGEEDCQqjhCMRWu_kyAjD16j-HY9cZDc4aCuZ1vVWgAWeg6wIKOUUcFtRc-JbnfGDJJnflChgj7hQFVCaEMU2gdIqVkm20kwt8UyY8ywzXEKUXdkQt1bPiSsASnFDs4cDxbK4oHg--gEh51mAu1mPPuwUpinwAAvcHgF62JIbteBveoBtLcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Xd9SHYFe_e21kI5eqtBoeoqR29l7yfA1R7amBHuSCS09xJQuRV93aWBjXYi2oEAjXkTyPkAlQYxXgN-0SmvsANdknIQ6vgMSq4TvXvG2YpyZDPam75pB7lDASIr2P5bpswkbSi4wTtjOJHnxOuo5o4lUFsSFk9vi8Cp7WQ-xe9x6NLHqVw93vpSYw5TSb8PpAskKWIWXmXQhdUTM6Xp6K5ike9QUpYgIRPv5jMW3D3oDHyXEo5FEaR-fivr3UIsC4CLm3K9S16zQe95FYwQKteW5c1fWSVNGbuJVbxU-pWm7zrTCrZ5uJtmfMfU8GFQLPTALerqy-whG4GP79nPO6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Xd9SHYFe_e21kI5eqtBoeoqR29l7yfA1R7amBHuSCS09xJQuRV93aWBjXYi2oEAjXkTyPkAlQYxXgN-0SmvsANdknIQ6vgMSq4TvXvG2YpyZDPam75pB7lDASIr2P5bpswkbSi4wTtjOJHnxOuo5o4lUFsSFk9vi8Cp7WQ-xe9x6NLHqVw93vpSYw5TSb8PpAskKWIWXmXQhdUTM6Xp6K5ike9QUpYgIRPv5jMW3D3oDHyXEo5FEaR-fivr3UIsC4CLm3K9S16zQe95FYwQKteW5c1fWSVNGbuJVbxU-pWm7zrTCrZ5uJtmfMfU8GFQLPTALerqy-whG4GP79nPO6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Ij9x7h3v1ArMuFzYNgrYvUzyh4xZiUzIQ4KXzUdQD5sDmwVvhC7zAVpd_5HYvBADR-FaVBv1BtQVHwiGA_Emg5EqyBkW_exqbmR99Fyrsv9t2Syz5WFr8I9rho7zEd_Que3p9ulJ0lu35lVr5Evk4ILUTADBBo2-qFeKU0Jo-1JJIpMi6XyTT2qkf_eElg3zVtPsGhp69dgz5Ijy9Xi-G7kUK6cMINMJ3bpX5ZXpJp0UkiCa0dem8bR8lXjhxUMM2v69FGiThJ8EF2PM-6qVNo6VSIRPbcblxRah0UsRegExeorLkejWmZA0wDYdRrfoBYA0QoEgbvWYaXb3goYyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Ij9x7h3v1ArMuFzYNgrYvUzyh4xZiUzIQ4KXzUdQD5sDmwVvhC7zAVpd_5HYvBADR-FaVBv1BtQVHwiGA_Emg5EqyBkW_exqbmR99Fyrsv9t2Syz5WFr8I9rho7zEd_Que3p9ulJ0lu35lVr5Evk4ILUTADBBo2-qFeKU0Jo-1JJIpMi6XyTT2qkf_eElg3zVtPsGhp69dgz5Ijy9Xi-G7kUK6cMINMJ3bpX5ZXpJp0UkiCa0dem8bR8lXjhxUMM2v69FGiThJ8EF2PM-6qVNo6VSIRPbcblxRah0UsRegExeorLkejWmZA0wDYdRrfoBYA0QoEgbvWYaXb3goYyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=igJGXLONtk2RK4WfsMVksEDYGezFeYK_iizEhaXKoBeBwF1mvhzsxeXTVxy5BIt6KY2KAZJXe_5io7RdoqfW-V4XWewZeBYp_Lf7VFBCJxh0K3osDqVsh0tqthHs6bfzcnX-ZdH9VbBhikGXLtTrlb4UjFnCJmfe3lQUVvasqmZDF74YUmmXdS3DXw6y9D6111mxh6u-APmQfCGrio89OJKMlksdXtSZYbU71sQ4JqC-5hIVHIhFeG37H6-h8Z_EdAeBK43CXttEedWv6eqaPBBcLUMRpREuylDH0gincacoNGHLpD8v-vzOzXNWtlKw81jt3PbzP_FK20AfUCc9aEaYhXNf33xxVtJu008AS64lO14F9YV18Cv3y5h2jQQPXRmGF2dKB1kkTnYmT3L1_WujWqzYfjmBpZePlX1kNRiFkq5aChrsVn2PQNCXvXvBQm7Oznm1KHk_SYbqDUeI1rqc2lSZ04pBxCYSyaz9kAhX6p6_7RTomnDrrabt1SK-IkMKGQXdAPu7gIV2p5jaPV1jaBh2UC-Z3k7iLpo3_FrsEMXQFeqFTKWGrnhwkH6ifg6CiCCDccywF9bV_US45Yn4G3PTJkqSZzc9hbJBGyeIqsjJquyGC2tGr6eZ3fDrMZtUVlp6i9USI6fp7kG1fWh3Lniw9jidciN0NvuTc94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=igJGXLONtk2RK4WfsMVksEDYGezFeYK_iizEhaXKoBeBwF1mvhzsxeXTVxy5BIt6KY2KAZJXe_5io7RdoqfW-V4XWewZeBYp_Lf7VFBCJxh0K3osDqVsh0tqthHs6bfzcnX-ZdH9VbBhikGXLtTrlb4UjFnCJmfe3lQUVvasqmZDF74YUmmXdS3DXw6y9D6111mxh6u-APmQfCGrio89OJKMlksdXtSZYbU71sQ4JqC-5hIVHIhFeG37H6-h8Z_EdAeBK43CXttEedWv6eqaPBBcLUMRpREuylDH0gincacoNGHLpD8v-vzOzXNWtlKw81jt3PbzP_FK20AfUCc9aEaYhXNf33xxVtJu008AS64lO14F9YV18Cv3y5h2jQQPXRmGF2dKB1kkTnYmT3L1_WujWqzYfjmBpZePlX1kNRiFkq5aChrsVn2PQNCXvXvBQm7Oznm1KHk_SYbqDUeI1rqc2lSZ04pBxCYSyaz9kAhX6p6_7RTomnDrrabt1SK-IkMKGQXdAPu7gIV2p5jaPV1jaBh2UC-Z3k7iLpo3_FrsEMXQFeqFTKWGrnhwkH6ifg6CiCCDccywF9bV_US45Yn4G3PTJkqSZzc9hbJBGyeIqsjJquyGC2tGr6eZ3fDrMZtUVlp6i9USI6fp7kG1fWh3Lniw9jidciN0NvuTc94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=XcNGuNCZqasCqxz4R_8wx8UHgMnEKVZzaNevK63UBF8P1NxkqhWhoRUxJeHFdMldf2RWotZ8ayMfC3-rHCU92wkuyJ7xru7Vy7ehDrk6yzEs7DUUl4Rf7uXwlnVvYgig56e9Mxeq4NwJgyq2tNhu0HFa-D48ubgZYQqVNaYmmlNl3l9iKyJ3e6T_kvtBYI3Oj6TK1BfDQt7jbG1r56xpIRZUKSkEQdsbM0G-tjh2pJtyvC_XGB2o2drbFyhOehJQZCBnP4B2AwQC6KPr59cQZlPt6aWkb4FyAoRglvSg8RUAO5mTEkTFSSihlokieJw0JndNKMPVYaugWInWiqmwMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=XcNGuNCZqasCqxz4R_8wx8UHgMnEKVZzaNevK63UBF8P1NxkqhWhoRUxJeHFdMldf2RWotZ8ayMfC3-rHCU92wkuyJ7xru7Vy7ehDrk6yzEs7DUUl4Rf7uXwlnVvYgig56e9Mxeq4NwJgyq2tNhu0HFa-D48ubgZYQqVNaYmmlNl3l9iKyJ3e6T_kvtBYI3Oj6TK1BfDQt7jbG1r56xpIRZUKSkEQdsbM0G-tjh2pJtyvC_XGB2o2drbFyhOehJQZCBnP4B2AwQC6KPr59cQZlPt6aWkb4FyAoRglvSg8RUAO5mTEkTFSSihlokieJw0JndNKMPVYaugWInWiqmwMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=pkBTT2jIT1s0cnEJxd6LdTt201bhdX7y6Lc-9j7ffRooCtyEGU8vlcaZqWeHiFmjjX6H3JfDshoVmJhs8etMKhFG-ON3QpHZUwvdAALDwKnbAQ2_bxZ2OJoyAh9cmr73qeant-AY6OXu_jTgncqPcl0tlenNuO2OEkoSRkFURFC_T4On2-mCE5DI-lpZsFGPCGyUuv_gAQJXj3GrN-xwmfntNDLeQAliJGMSulQMWS-MG0S-Q3jsRKM-ZpQnFP1XTj879XTm6H2dKiQu0yHcA4e_3g15_9WP_rDIOgPmcrrQp2f7twtu5DnfYwPRJ7DcH6AiAsB-3jRLkf1ujtIAOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=pkBTT2jIT1s0cnEJxd6LdTt201bhdX7y6Lc-9j7ffRooCtyEGU8vlcaZqWeHiFmjjX6H3JfDshoVmJhs8etMKhFG-ON3QpHZUwvdAALDwKnbAQ2_bxZ2OJoyAh9cmr73qeant-AY6OXu_jTgncqPcl0tlenNuO2OEkoSRkFURFC_T4On2-mCE5DI-lpZsFGPCGyUuv_gAQJXj3GrN-xwmfntNDLeQAliJGMSulQMWS-MG0S-Q3jsRKM-ZpQnFP1XTj879XTm6H2dKiQu0yHcA4e_3g15_9WP_rDIOgPmcrrQp2f7twtu5DnfYwPRJ7DcH6AiAsB-3jRLkf1ujtIAOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EraR0My2JH_XX0ZKc894DGEMDZHAtSYb0KEAXwPrA_OXjrOajmqiLPWaplQEtQGCdIuQ4C2GP9zalwmAdRAwJVOII5TfmWoFFKnz-NuyYzDNd8cj_lQmy1nnk1kiQUFg-CnqialGfDvdmCpjaqZTZcdma8_YMfRxMkBiMWOQ9w05jkAAxtoEnuZX5hc7uy49hLzRcLCD0ORMoXLEwslNfN5Cfe4z_hRYtp-rf05DEuZn8UNmWCZbGvI9Qum95_NJhZ2F-h2TZ_dTNE_61usneWGLss5weLjESYRJ8Dc2-UpIrD40mqW_OdOBFRAj0Vpu1y1MB8540g0TzFSmpzwHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=f3BFd56p0XsXYrwLJHFSfVwxwM1nrj-utyeqsH9467EXPI4-OFwLg07xCt5iwv_OXs2PpaLIfQMiG0TJpLcdYmPA1DloxBo0O_pJ6cTw3ZN2NAcpRqvreE7EblMeMud9CfnikDUjH5nZg8UCNK_iXcKUljbvTVeGckt2NCciYwMpgnqaNCRko8tKfC9yNCSvmxn9pq55An07msuPehLMtfx3dGP0FyNuB0L490zHu6h1CA8nbasQ6fxgThydScbj9Br03Hbq1FHFXURHxGfIrP8oMppD1rmVvf6SFeo6oGJZMvxxq7ZZ-J9pJQ633VKiIebCkq8wpUz6kPVKx1pZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=f3BFd56p0XsXYrwLJHFSfVwxwM1nrj-utyeqsH9467EXPI4-OFwLg07xCt5iwv_OXs2PpaLIfQMiG0TJpLcdYmPA1DloxBo0O_pJ6cTw3ZN2NAcpRqvreE7EblMeMud9CfnikDUjH5nZg8UCNK_iXcKUljbvTVeGckt2NCciYwMpgnqaNCRko8tKfC9yNCSvmxn9pq55An07msuPehLMtfx3dGP0FyNuB0L490zHu6h1CA8nbasQ6fxgThydScbj9Br03Hbq1FHFXURHxGfIrP8oMppD1rmVvf6SFeo6oGJZMvxxq7ZZ-J9pJQ633VKiIebCkq8wpUz6kPVKx1pZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAszOcLLZDhXfi9q9idUycGxMt2Q2jNiFkGNuiy-3B17xlEzjvZfXmZ4vr95r3bsqzlRWqWxzF2GHtUNFHdMeq1Z1DzsRCxeQcPjb7B1S67OP87_DsoYFx2_luAuOlfuqY5qGNkBqiHtY5s98_Or0_6UDpoXlYIOKntMwHeHsekkBU0oE3GBmix_NM-VLpdZLQCz3M0b62Yy7VeWOQOAOkQm3JJB_Z5nDh7xbwR1SAgECd9O-n8_Bj8ds6xflPutqBj2pERKHBYfkJPhPrXb_0Av5QlsoP82MwMbs07o9gf-R70jmY-BRpeuRHlSv3NTaqZUB7QJDrlDzpkOFI7XWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYYl2HD9hucBfQzOW1_sBmQMmOvO1Kd1wKsyNJu0xRTmzzz1cKLMIbJ3Y2Ly4tK-RsMUMA7TLnLF4dApaOCMRhNtTFiD6szKaFhOhef9PhegSgl31Du1LePFLaIDY0oDPXFZGq3I618EFA_uLMqY1gaveeOAay_4ZF_AEPYhOZk9bgtRAxdIGXFqkEAWEd4tXujYuj67W4P0GW-DUgHhEzeNkxsj7vcGg1MCA9LZEeL-r_tguc9jruEyNXfTYxe_SrzQI81wef1q4WSAi-ZB_jtuU05g-KjAUzcL3fe6V4TrVpYvX1gk99ER6qOv1Zuk5f0eKLq2dBf6LIWVEssXjQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=AGQAP5LWGPI8UclWAUMu55slcwyF5H7DwEuzlKZtoJfJlAeU1a05uwfCuMd7HeMCMTK06obcjQoBOL6xt5KXKLxBzcI2caoPK5BWF1VaHOgnERvaAJn7xygeIdkJY0AEdymyUlUUR0GtRBUuSCOufWFlicLzkEYBh3eERmvikD2yboNogXIY0NwFTPq_eA9JTyz1GhVqSuVvtZgxekkHQrprPNbxuBrCafhCl7ZEqrxQY54w8pOCQFwSpdR7lECiPO8J1AhrG46gqy3KA-_G5EXnHv1yVcsrjFXlw67U2N-_ikY9JxLo-0T8bL7WX41XF-elPDRwknUcgXe39WqYGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=AGQAP5LWGPI8UclWAUMu55slcwyF5H7DwEuzlKZtoJfJlAeU1a05uwfCuMd7HeMCMTK06obcjQoBOL6xt5KXKLxBzcI2caoPK5BWF1VaHOgnERvaAJn7xygeIdkJY0AEdymyUlUUR0GtRBUuSCOufWFlicLzkEYBh3eERmvikD2yboNogXIY0NwFTPq_eA9JTyz1GhVqSuVvtZgxekkHQrprPNbxuBrCafhCl7ZEqrxQY54w8pOCQFwSpdR7lECiPO8J1AhrG46gqy3KA-_G5EXnHv1yVcsrjFXlw67U2N-_ikY9JxLo-0T8bL7WX41XF-elPDRwknUcgXe39WqYGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=aSwJpGBtmI1wEKpI0VPMPpDe8XuTG9I33574ArB6LSLsqVF7JyTi8JktTXTRJTzDJ6eEhC_ioIWFXUyOHVKg7kpgD49RtdpeFBx6vEKLCLLCzCiafrY24uLEAS5C7rlboE9-kRxhiMQbP4cHF7Ec-hEtritn4rzGek_Y5BzJ7nfhSY6PI3PMaSEvkbML-GGi4WzGEobxsaYwds4U_sXeYAExOeq2ixc7JP93zz0puUOVlF4kRxB3GonWXFWuEEQ57s3kddXF43DexbyeQxfqkJ8aqWYuCtseW-wqkpLPTnIV0KUs7FKa2lSzkDe8LMpd_b6aY2GpPY_tW7DOqUI1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=aSwJpGBtmI1wEKpI0VPMPpDe8XuTG9I33574ArB6LSLsqVF7JyTi8JktTXTRJTzDJ6eEhC_ioIWFXUyOHVKg7kpgD49RtdpeFBx6vEKLCLLCzCiafrY24uLEAS5C7rlboE9-kRxhiMQbP4cHF7Ec-hEtritn4rzGek_Y5BzJ7nfhSY6PI3PMaSEvkbML-GGi4WzGEobxsaYwds4U_sXeYAExOeq2ixc7JP93zz0puUOVlF4kRxB3GonWXFWuEEQ57s3kddXF43DexbyeQxfqkJ8aqWYuCtseW-wqkpLPTnIV0KUs7FKa2lSzkDe8LMpd_b6aY2GpPY_tW7DOqUI1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=q_MVlNRQLa8YgeNNcO3wgdZ3GHPsae_OAz5C9jFrt_FrhiXR2IrDslvwJiHbOwfY2I9QCAIsZXHKHSAEsxZWf4j5jOub2JX4I48gvQ7v_26_5gI2KqoePo6IEcOryqCriuLjgde0Unv72j94HDYh7xVnHsh8SrB_JqOsQt4B0ORDHTHcGH2D7lIEcaxoTmZhE3d3NbkF9e0lG24uGeExalskqmtyuE9VaArSRSD6AglR9-3GvSt01ogEj7mWDfcXddh9LbVg-IMns0SYoasmhkfGGmoAu3RP6dQiFfRlEAiAbFzmZZMqcSMhJCnDlzq9jpP7TfL5edzlYGsvEiydYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=q_MVlNRQLa8YgeNNcO3wgdZ3GHPsae_OAz5C9jFrt_FrhiXR2IrDslvwJiHbOwfY2I9QCAIsZXHKHSAEsxZWf4j5jOub2JX4I48gvQ7v_26_5gI2KqoePo6IEcOryqCriuLjgde0Unv72j94HDYh7xVnHsh8SrB_JqOsQt4B0ORDHTHcGH2D7lIEcaxoTmZhE3d3NbkF9e0lG24uGeExalskqmtyuE9VaArSRSD6AglR9-3GvSt01ogEj7mWDfcXddh9LbVg-IMns0SYoasmhkfGGmoAu3RP6dQiFfRlEAiAbFzmZZMqcSMhJCnDlzq9jpP7TfL5edzlYGsvEiydYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkm__pTjlr7QQdOfFdipqkfxgMocAIUV8HgLUAOjhMTKBLbkPnhVgkxbLCdePkq5BccbmaXkSHdgt4WIDhYtK9vdwDwhD1weiHauBUZ3LQLeQy3b7yBcOAk6hxhYIJ13bDa3gNFbx5dZ-q2lis8BhYNZX0gT1QBax5kXA27NPuzpQmq0BRl5SZ-1tRQNVjw23qW-AM2H3cGf6mDFrCPeQwZyiQvxtL8d9D24FoonE_GmY6ymgoJjZfpfw3tVE2gS4gDy9o1rbelS8y6IC3zfGw-NIrxHfV1Tot-5Tl-i77Dlt0QRLtIOAsu18WyBH01zoJE88ChAE_4XOS5FHd7tPQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=LmC8OIcwOLabrT941_O3YOxHxhRi38UKrjsySOtZJzw1IEaUvvHTau7qze8bIyJP6S5z23cZBa6AlwUlm85yrGhTryUzFWjFXzk2XVDQi3TstQfnfbWQcGl4Ufa1XsLXwD3vmkdSdpDCCGPlfBQ3y_2wQWJoynx0nqQEeh7XqBSNpRki2mDnYxdUwc_eTfKgMT9733p7OGsZPpDJvfzlkoZGwePM9_eu-io2KVCSQ7RoX7JduogL31oRCF4Z5sgaVYCPzQbobSg9OaMOTVdaUbZ_HHmIirMGQtNTbj4kcQYdaV4bP_3-WBHcOLATg1YviZzUHWv6Pu1BlrcrGXFexw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=LmC8OIcwOLabrT941_O3YOxHxhRi38UKrjsySOtZJzw1IEaUvvHTau7qze8bIyJP6S5z23cZBa6AlwUlm85yrGhTryUzFWjFXzk2XVDQi3TstQfnfbWQcGl4Ufa1XsLXwD3vmkdSdpDCCGPlfBQ3y_2wQWJoynx0nqQEeh7XqBSNpRki2mDnYxdUwc_eTfKgMT9733p7OGsZPpDJvfzlkoZGwePM9_eu-io2KVCSQ7RoX7JduogL31oRCF4Z5sgaVYCPzQbobSg9OaMOTVdaUbZ_HHmIirMGQtNTbj4kcQYdaV4bP_3-WBHcOLATg1YviZzUHWv6Pu1BlrcrGXFexw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=hZA62bn8s189tlvztky5S5ehbuaozliiHfCZ1k8tyHICZklKdhx7Xydj4yQhaYwuUrIF7dkFxpPDvyFHl3ex4NB0o3wBXUX1jP754eoiUZnuJeYNnMvprjjimd8gFUwHPEev_NGWg3ORKTqGdHLG_Ovm1WRr8VNx2JBtFAw7QHEhEJDhUKTThzmATO8_Pd7EvAEPa6T0x4rJb5DwqsGp223q38sGQO1Y3WmhVTT_Bt3i0JJWA17VLpHBzATxbXtQ8eL5wQP2JxUq7KNE5t4rJgTfUDCj26qPMoL9ZpjQgvhwrX6GL2oGJdDIvxLDHy3xsoiJg5Gmt4KPSc5IQoJdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=hZA62bn8s189tlvztky5S5ehbuaozliiHfCZ1k8tyHICZklKdhx7Xydj4yQhaYwuUrIF7dkFxpPDvyFHl3ex4NB0o3wBXUX1jP754eoiUZnuJeYNnMvprjjimd8gFUwHPEev_NGWg3ORKTqGdHLG_Ovm1WRr8VNx2JBtFAw7QHEhEJDhUKTThzmATO8_Pd7EvAEPa6T0x4rJb5DwqsGp223q38sGQO1Y3WmhVTT_Bt3i0JJWA17VLpHBzATxbXtQ8eL5wQP2JxUq7KNE5t4rJgTfUDCj26qPMoL9ZpjQgvhwrX6GL2oGJdDIvxLDHy3xsoiJg5Gmt4KPSc5IQoJdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=PrhS78e2WyAGWbwWwIaDsAOjUv05lCUtSoxjy0q5PmVCZhHYpY0PQEzIieVzgZAliHn2GPJQoEutJ6yLiNrWBXdTwpyUKNuxk2wATL3DIEav_cXzZZrE55xpWjcZ4A9Gd1KwbZOorbD1d5WamrDYZ6_XQDkOHVydO1Z68JnCr_IQhHLGEJeK-3XRDb1b5i3e_QwlPwJF9Ms2QS8cQHrWOOSv7k5GKxCzCiaLe-898uZWk8_pu6eLXOQZIHEAeKViPydjINLB6s3lxqsGX0Qf2GCkR7p40yOfsJMqOYchJa01S_dd-tFLMaBJfGdQKDdBWiY675O3T2wj4hjOd6rwUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=PrhS78e2WyAGWbwWwIaDsAOjUv05lCUtSoxjy0q5PmVCZhHYpY0PQEzIieVzgZAliHn2GPJQoEutJ6yLiNrWBXdTwpyUKNuxk2wATL3DIEav_cXzZZrE55xpWjcZ4A9Gd1KwbZOorbD1d5WamrDYZ6_XQDkOHVydO1Z68JnCr_IQhHLGEJeK-3XRDb1b5i3e_QwlPwJF9Ms2QS8cQHrWOOSv7k5GKxCzCiaLe-898uZWk8_pu6eLXOQZIHEAeKViPydjINLB6s3lxqsGX0Qf2GCkR7p40yOfsJMqOYchJa01S_dd-tFLMaBJfGdQKDdBWiY675O3T2wj4hjOd6rwUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulNJJOKFFu-vaVXk5z401PcWK1C1OdJVhRurgUKJeoT2UFH80bF2FrGGVU2EG9eTHdyzUnp406lNaZ5MzZKV7Waok_K6hQFwqVl2aPIhLsUzx7UCRfSnKs8lPddDs_nNrvNqaDzH1085q49pmd8F2ypAERdZzkvPGVucmmd7Xfs5yrPwcacUOYgy68KRpcpjoNzHVYRD3J_WjIriiBg0nkce3Ltvo3mM74l06lZgML2askFeLpSs5X99liRfqc4GnIG3nWKNPShQLkNqNqVQVpPhsH_LqIxWyMfeCl6Gg81OrtD9Dxmm1udpxTgGb3_EzLBja3vLZeIqQFuJdB1d9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ZfFF864YHeA83j9llHHi7BITrNMlAPC3LK9HEI4FEEcoA5zQSBS25HobPPDsdwAPdu6GHbD6WUp9-XZWjojX_I4qWexBysLlT9a_CSThNwflSgd90Tber3a-84dGxpIzUJIY8I3wEKI2D_g6pZjCW6pNPkuAzq6odYjLKB-w_JFj1pN-o55j15UEtKw1_GtFxZpl0VGLm-YoplmJ4nV144cr6ectYgGwExMP2zRzSbpXc1kQ0DCju0D5jesFdOaqb0uueVn2f-jgbSuePDUYsoM28JNdhViolV5F3oaSLhu12RkVtnA6tcFrcVO7oRutX2B8AkUlU6e-KeKsSAlK2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ZfFF864YHeA83j9llHHi7BITrNMlAPC3LK9HEI4FEEcoA5zQSBS25HobPPDsdwAPdu6GHbD6WUp9-XZWjojX_I4qWexBysLlT9a_CSThNwflSgd90Tber3a-84dGxpIzUJIY8I3wEKI2D_g6pZjCW6pNPkuAzq6odYjLKB-w_JFj1pN-o55j15UEtKw1_GtFxZpl0VGLm-YoplmJ4nV144cr6ectYgGwExMP2zRzSbpXc1kQ0DCju0D5jesFdOaqb0uueVn2f-jgbSuePDUYsoM28JNdhViolV5F3oaSLhu12RkVtnA6tcFrcVO7oRutX2B8AkUlU6e-KeKsSAlK2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfFImfL4yHyUTFhDZB-5NHrDNxN7kFAaY1OGXA4SloLyAXx0Zl3csl8gxfou-YkQ88ZyTUf5ak4TZcpGqfiKoglXd-k5xHfxeVKHWefpv8RrepET5y5YFX-kb7xddeUAP2GtnDDED4bMGj3PWyN6S2YVHGO8U1GDq83Rara4BHARWtDYEpH4xPZIpFTUa5jb0SX9d3DtGQ6MZd4qgwixzBu2eaoyipVDxsvuJm704HlhTJw2vhV20kDqFuOAjcRg-zZU5P5TWgFogiCWBwF4vU5mpsUMgWa6BBrPw9hKkqSg7H402pkN8GtB5x8BGAljJxU1eI8mCxQ-olgCkikURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=NSGRJJK6_3OwTSn8qRSNATkA_uXXWeb6s8luVnwbd1sr9QWeNVrzHHSC7z89DNV8JJN16zN3nceJFiXQE1ysctcmcAfoseuBK49c0ALz58IsU_7uI6JUEvObHt6daNKT0UhHL1QqwUh4ILcI13IVc66xePSrrVfqahOxg2bhNalB1sY7mDYAF1uHkLX2DirGKgnmRLsBxU-A3emw-tXDWAMa-yF3CXrKDBc_V0N3KsKTMbbX7mbBTO_dVYGBcSgbZ8McITINFNDeGoSgVqCiBjAsKT6tf03xqjyNlKH_g2UeTy_adRebJVpvW91kmY_cAj8I1R73xIPgP5gh2cFFaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=NSGRJJK6_3OwTSn8qRSNATkA_uXXWeb6s8luVnwbd1sr9QWeNVrzHHSC7z89DNV8JJN16zN3nceJFiXQE1ysctcmcAfoseuBK49c0ALz58IsU_7uI6JUEvObHt6daNKT0UhHL1QqwUh4ILcI13IVc66xePSrrVfqahOxg2bhNalB1sY7mDYAF1uHkLX2DirGKgnmRLsBxU-A3emw-tXDWAMa-yF3CXrKDBc_V0N3KsKTMbbX7mbBTO_dVYGBcSgbZ8McITINFNDeGoSgVqCiBjAsKT6tf03xqjyNlKH_g2UeTy_adRebJVpvW91kmY_cAj8I1R73xIPgP5gh2cFFaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY9By98VwFnGHHdPp9sRa54BC2tpdwrbEhnSM-M6x-fNr5jhMSVB2fDTUOkVLi2HmzlHa8MGDn-YWgqC_7a9uveSt0D8YBMOOZV9a46pq3xBpRCdoxJf4cICNQMdNxigcF-T4ii4rYM_avCoBB85c2bcG2NZLkruZTcw1mf2TfDeox8FMprJCUQI1Snb3FM46fJO1Qw71PfLCCnkcy4K50KJVZBV-ttrjpz7_FJ1t9s3xHAD8N-wXBXUJTPYpde98VXbDNbegE40QEy9D8Q5aTg4KfS8lWLDROKoAvYSqXu8Do4d-LtGSClaFOoMDm15_YzXoxSXTfoPV_JUXoYjWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=hagAVn8h-XjwEaImAOK7-RUNiKrLpMdGxmaZtk4tGLs6A9h3r8gcu6W3wjBl2W-AqlHYbshQRnykRdEb4zTU90q1B528rg8NgpA6SbaUoTBBvyUx7QhPae_Mo_uVWogPNv1ifFRt6Y436W7gTvHgP8VB9Ty2X8QzCjnTXr06Hhf-jugURejVE2bhIQdTK28JOvFnQkwi0-1I_JIX0vVeSx6vdC9uq_8rTyYMj0VTG_0em3nvnKqWC8bmLKfvp6HlJ1P5Nbcy-PASuqRBuRCePNEguP0xrlabhvVeC0c-05GxDRWbSC3y4sdLCqyZdHbu8RjZHtqP-97EGD5gSosekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=hagAVn8h-XjwEaImAOK7-RUNiKrLpMdGxmaZtk4tGLs6A9h3r8gcu6W3wjBl2W-AqlHYbshQRnykRdEb4zTU90q1B528rg8NgpA6SbaUoTBBvyUx7QhPae_Mo_uVWogPNv1ifFRt6Y436W7gTvHgP8VB9Ty2X8QzCjnTXr06Hhf-jugURejVE2bhIQdTK28JOvFnQkwi0-1I_JIX0vVeSx6vdC9uq_8rTyYMj0VTG_0em3nvnKqWC8bmLKfvp6HlJ1P5Nbcy-PASuqRBuRCePNEguP0xrlabhvVeC0c-05GxDRWbSC3y4sdLCqyZdHbu8RjZHtqP-97EGD5gSosekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dKJdH47csfCIwCNIyY7F5LE2Ralp5n3FKd9I2QXxaYaVk23XfUIDSQ783gSttWUopEC82mza7kn2348Cr2dzZ0982aapaQ3P5oOkF2MLTv5YF97kS8D04EJnpw5noq1l5ha2y5GJ28SVuOtmWn9sS__2LpEGCNDFTqmWQoYbIVApixSd7fpL-1gur_blKr109KNRWswsA00Q1IevEfbB5cn354wTeWg2QEXSx6-5qXTy8ar-g-IjKnvako6AXO9-nVOWXqhZeZSZa-Bc-jNS7ye1pOvzOM-Gbj000-3qHX8F7m5Og-wJ4C9z79a2YWnhP617NzpWHe72noAL23VMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjqSwDM-qrG9kQcMp1kotnrsefrZLA6ApLqiNq-wQrAktu-feRXtN7l14PO2EM_5lPvNv4lUKInMDGyWLjn6WJ2_VVNKKo3L7tEo8z_nC_SXTXDgNgYxmmpodtQfbZ647ZlNWcqjXYJrFGICRbGWrMQD9d4oPAXg2G3hmdLrjAKRzjdDFh_82o35Kv3RCS0PhQd2N_HF5LzhnbmsMJX_JIASGLYQG0UzIll9whdjLdLbwKbAtnfSxsejij8bb0r35iMBF89rd7jhNpbahJwRU5ODVXfXh1B1uPmI9sNJnpjTQvc70XlxI1QMVJAIH2ErIK9xF1OirTUZeTNzlZVEBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=nfNEgffbWanS0Cb-ls7hRzoAcFoT3Lh49vFxnV_Me-_L1VNkWmy4jh6tvaIBzK4s0MG034AJlkhfJHtWuOS5YQJZVgdzDMqKDHxvtFLbjAYznELlCUIsoDd9GC8aJhS1dwbd8Rby6PvEiqYtVF-K1QNWFLr6nt1FS-X-rVgqK2Xs-oYOl8YCFf8J_R1rNrymXUzSjsBhphY1vesDw3KhZj1jcJpsNn_mAMaK-NGfFGiRfhxJja18-M56KCACIWcQ1Q0UFesDSufEI04P7umL4fIhpNJCJ53sh38rpp5aArqzbl_8zQASBJZWwSyf1Uw7Dgc3TDsNTPijc5zcSFRB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=nfNEgffbWanS0Cb-ls7hRzoAcFoT3Lh49vFxnV_Me-_L1VNkWmy4jh6tvaIBzK4s0MG034AJlkhfJHtWuOS5YQJZVgdzDMqKDHxvtFLbjAYznELlCUIsoDd9GC8aJhS1dwbd8Rby6PvEiqYtVF-K1QNWFLr6nt1FS-X-rVgqK2Xs-oYOl8YCFf8J_R1rNrymXUzSjsBhphY1vesDw3KhZj1jcJpsNn_mAMaK-NGfFGiRfhxJja18-M56KCACIWcQ1Q0UFesDSufEI04P7umL4fIhpNJCJ53sh38rpp5aArqzbl_8zQASBJZWwSyf1Uw7Dgc3TDsNTPijc5zcSFRB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGoQw704ssbSrpe2tG54uSPdg2d-JcqtllwmaqdxwsMF25NH9SsdABaTfrGnjPvlehIEplMmtD5gtba4ccPU97jELKQ3R5WNXNFo7M_laUFJOIblxdgkDOzVY0BrdxDzGvAckF8p5ssie9z8uLGqPcV6DfGCUaW6Mdxh09Yy_VjJdwsnDwq5MKPF_U_9v4EjDkLAvvkUE0ZPKHYFl82eDvZ_c9d4zhB9qSzTR4hHQj1UyE8kRa6NyRfJkfjEPHBWcuc2WTzQ0QlhmjryK-F8UYfo0d13lFQrGSr8U0t-GE15GGgjdmIf24ZEMB857Nu5Xfzwo2kzNdfHQRB72dKpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcz1nURuBwrC8KvtLPQ3utPx6GokV7kXRuT_lpsT11f4AJfjqArEgm357FDsF68hO8Bx_WButZLOYtU3jVbiyFwB5xnn5DgUCtVyA_hlHc7_vfvgzHsZmRs7gS6yRzHJOF_BDj3foeKN6V8xVz_6awb0PKdxiKJ7eihJEuRoaGKdV394c7-UA0B-yQJ5EjnB1XC9ynwo1yM41TjePARWiJ1MsIAhcTNRxEiBGodsE8W4AYZSWJil-Sfdsaa8PmL7oi6Wvuw8kzzlvqQIyLybEV6ddig3slk0cyQ6UQv56g19brw5kTdOqaEz5Qjpwwp8y8ywsaNvSTXM3pp6hivHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
