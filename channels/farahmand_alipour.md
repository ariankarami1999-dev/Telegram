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
<img src="https://cdn4.telesco.pe/file/uUxJ9gGeZ6LX1HvvPAm-cTD4AeK0qKxyah096SCivWFYVswq2vylJd3BaXnSxD7GAEMn1hGbzsLnj8FriXrpdSOpGpIkMeB_cXchHZG3WXrLb7loe7dfy_dg5KLVmkGcyHI-vq65mBnuTeDkdupxdaL19x0PqA-EFiTHnfsYNwOIywaqCcb3EwUY67p97iBulgTQ8zTKuSgy3VKS3-EPn4vBfzyZ1ZPenPKn4EstVQ-Xwuh-oaZK4bQmPlJYHtFcq36x3Tkn1fw6kRePIM_mz7U2nasa9SIrOn99mmEVtKe7Ygtzy2vC5IQBz_6jhUXGcYfkAtBfTV-lTW732rpryQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 06:13:10</div>
<hr>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ew-Bm9JV0DKidx-3p5-RDHMbrTJNsI6VklarUEWrUNqMPT8T1UxIJZwksHnv5lU15MkzcBsmkrLTQYyFp_SkJCHJJmsOJuL8rt111uDj8Ekyk6HTcm_-uDEQ9GihmK7B5f2lSnXL03bzOSalAIaQM9hTNWGYz3L-lU-ub-9zURvA8OCPt_CdwVZ9pqcrCs4S7XLOwQBT3P2VZ6jPU4KvIulh0jP_p9GJsewBmvY1ozWcTwawdqYkdfHtuQX9qJdtx-DbrkszG2qTAdPgwZ_OidnfpbawMJOv2IfgUWw1bO5BuziUAFcQYieN0rf8ThlGqe7hVr9yRkv0pHoXEel2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvv0oNieOKpjDD__S1oAM2RVzTuTnqVUIA5s65IBoptVQW67DBJvE-LvZSPzcaDgfLTor8bTn8HnzG46jbxuwYDjW73OcSgno5soLgqYPMW1xwYtmfn-NUEnsMpgjIa27LCJGSOA2guHFl-vxZy_nN-S6MpIQ3m_L8Pn4FcJi5Z5HpyVTNwQjJnMzDr6wYGutaPpcGLntFhJedDiyAgjZ7RN10K-2L8BIJSTb29K1a-vfjTfZ_mKlwKQAFqWOS9E5uup5Mt05_j25GTQiajTTRwODucgPumxji87EupCR-5GsZ02xisFy0zb18_stGn_oG6-H7wKT-N5-UsvP6hGMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTlxXodelZAAUKeGl_CSolqihwb9i2RTgfHoj5F0PULg6_R1ps2Z55DfHD3yEQ6dQaqc0lEzOUmFLC_gejZzbBX7U4vITdlBcuWiLkhyA3AVQb7N_0PwToznCNI6AFDwsGHg53SHI8bekdkBXHoheGV_CU6H16uIPmJvJpvw8wjzwWwaqkBQgnGEKdHB9Rm-_KeYxmk1blfd14DROqikmnQOpwM1DRHXqAYR4NnowRwCsDkZZsMVS48SvsjAy7Xrued8ABhjjPFXm2lttdmCz1-gtqGqDa0QgeWVArkK_Z5ZQOkB7sT4ytXUjnHDdAxXtlqHqlZt5lzixl69-2pyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPSyxV_OvfdyUWB6PiNQ7dU0cc_GZ_1vs6XYjwnAGTtubZRgzgzt9o4ET0VcBA60r9UtTdchKeKdeaYA4a7hQqelwPIhQwDLyvwfi5ab6dhHfMg2phnY9BIVXDYan_EldA7jde6xO5SXINPubhs71-e3-7KtbD8ebv22bztKNELwEGZjY-ba2gmbF8qNGM0LfwuSLlBvgfNAW9HcOXNseG5296ywC-k1mgNQAbSuv4VGmAyTw2h7vQB4LLo6L3aOiO35CZFNyEAvx3v0pJzWFGytPOmM2mCWra3HITny29JeVf-4D1VpHyTpatRmPc_xgHMe2O-2ZfwsokItlEpjlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=fOs8DEB2hTyQdom8hVZkv8DOybrApCF-P-KqVMPmsbmGy4BZJBNg41AEPT7evzkSRhj-RnkxW689q5r0C9WZj2jChv8ARU5rppUybyOl02J6Ga5tawqeEwvVlGlqn9Fc8eg6dTs_iGEEgqSAVvpaUFODKMRwAGnS-f8k3-Ub7JB4soGfl2hIO_kVXDg7c1YtyEgAPNE1UFmntRzNECOVTYpGmd5XEjGdv5ApZ6bAtXYnc79u7zy3zFeIyLVdOCiUMgIMCjHUcZPiQ0o6Qo6OzKrdqkfGwCbQ_WMNM1v95AP_ZW63QVrpNbwpNrFKQxPBlm9AHteDOMMvdeTNDMho7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=fOs8DEB2hTyQdom8hVZkv8DOybrApCF-P-KqVMPmsbmGy4BZJBNg41AEPT7evzkSRhj-RnkxW689q5r0C9WZj2jChv8ARU5rppUybyOl02J6Ga5tawqeEwvVlGlqn9Fc8eg6dTs_iGEEgqSAVvpaUFODKMRwAGnS-f8k3-Ub7JB4soGfl2hIO_kVXDg7c1YtyEgAPNE1UFmntRzNECOVTYpGmd5XEjGdv5ApZ6bAtXYnc79u7zy3zFeIyLVdOCiUMgIMCjHUcZPiQ0o6Qo6OzKrdqkfGwCbQ_WMNM1v95AP_ZW63QVrpNbwpNrFKQxPBlm9AHteDOMMvdeTNDMho7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ow6l9ksUoGYZxnwQlVeafEhcH8479ExBpzIW7qUM2TIrMAybIWU3tUK6MnXctg1RksF3XHaZ8D7pkgpqvrKNCY8OqHepUU8zwNpAaABO6QkPCbfCLQV3yqv-W17RM9gN3NypC4rVeod5sn_e9qENYBrWWglah_VORY7RLQBHVwBf2uXKLbbb-Crgd4vfP6vbR7fPRS1aXwOV1GHZjMZl0XDlsrnAWyyexQqU3vyjYi8phBRJI54YM43XiWi0A0V_HwYz3CMBKlVULO1Z4RSERIWCRxkAJNEGiQiBvnA_yDY_drf9RSJ7WctWGdl3r1d4fRIaHpbgnJ2yDyC4Q4j0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ow6l9ksUoGYZxnwQlVeafEhcH8479ExBpzIW7qUM2TIrMAybIWU3tUK6MnXctg1RksF3XHaZ8D7pkgpqvrKNCY8OqHepUU8zwNpAaABO6QkPCbfCLQV3yqv-W17RM9gN3NypC4rVeod5sn_e9qENYBrWWglah_VORY7RLQBHVwBf2uXKLbbb-Crgd4vfP6vbR7fPRS1aXwOV1GHZjMZl0XDlsrnAWyyexQqU3vyjYi8phBRJI54YM43XiWi0A0V_HwYz3CMBKlVULO1Z4RSERIWCRxkAJNEGiQiBvnA_yDY_drf9RSJ7WctWGdl3r1d4fRIaHpbgnJ2yDyC4Q4j0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsoFj93vZMXdyaGkA8Qc3isiCZafG3nKpjYOd-5sN9f1YVQz8n4sSeK0SKnSiARy5B_gOuxjpdts7Ja6OVtDqXFKOL31EdSZMbEbuUqdOE1clbnaNiziNv8toEglBzn2YGfllQY_xxJK15HHMtAI18CMpzUeXbz05BA9CLloGbC_WmKKiGRy4he9rWif_GVdAwB-ioS23OorHrjcuFPRe_c_JSlrXtK2_7-Ty319ps6Vc3HfuRxSeHBDJBGZOieGQjkYD8iZtGg5zgMFEvD3BqI_bqcIKk_qm5g_4XrMLmtHWYFc0KhyMJOGyrtUfKIUdUYOrzrSEfv3oxERyAyANQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcfzcMK7mDXhsHd_UDZpyo3xlEGuPC1iHSuO9BpG33lW2WfCLnrj_Sbj5CnXLeNWhM2KNqzPcikhezqmK7CO52-TPOxIbUt-jbuqT5GXtPMKsfkvDl0RvQ7VC06xgDf3VIo75UWWAZyKhp8a6My_ubuon-3Re7P93DAeJSBLnQieAlZRZ3RqTh5h54zWSx8vBXI6P_T3aLVhhOwFygWKRfsSzLWEPR_HnUDjFLJR6ru3XDBJKYVukUvDhfuMXwYnTsVYVnZtHSIxwUDIiRQfI2mFQ8i9DDGetOTv6_AK6ivX5QzACvqbRvAamDI-Zx45qNnZvSnDzszRqAdKCs23sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7X_h5eKAkMBTLRJ49vnXYGN2Rwwe2NLCOkY0m_kJ1DXVCord4aMVBrS5ERcakL0j3TlUBxUV0Acw-t_lxYDkKj1wZeP1Kh6i19bfqojGnaqamk7bJRESYQZGkJt4u-coPBZ1Ru4J1zAqFr7jEIVX1Ovz_sUo3nc6oEE3gByruaaKxI0FDGe2ckr48NgLQg5pIC257BPcYlRsj8gNNeoDt2dwuodiGwpqxLY3OK-QFuKPKJ4yoSnKg6dfmy0c1i6MJj2x9Enup1NP-nCkpxBiDpNH4NVksGmshHU7iUM7jUpgCbUtXwBYq-cBjHhVwo72ZtCKzMYS49kRDUwgGIX2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=m80-KJJyVfVgbmV3uRF0zT-9u2VJMRHVClKgE9IjMD1PK6SR4b64lo4vfjqkdWTi_cMPFx7mElWHNwn7m6lUsupF1N_5G73ncmPKYcjmj-KrHH7n4a9qdpJL8GI8otZ_zccVcblmy08zhrtaODZsRiUrMjX3N24SKQLua43p3ga08Kcrkej2bO-IsSeBlWe8uLtwJYzCo71zsIvPKCLCl4n4N_WSXim_AvKJDNrf3VuHCcs_lrY6myGKxAtQL082qAHSes8Kq4lWE9wYB67Uhd7m-vr0uX3CsNohsFRK2MFU_Hi3YPdiYoQKUmIF_7R5E97L2dzCwDTx678Tf8gqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=m80-KJJyVfVgbmV3uRF0zT-9u2VJMRHVClKgE9IjMD1PK6SR4b64lo4vfjqkdWTi_cMPFx7mElWHNwn7m6lUsupF1N_5G73ncmPKYcjmj-KrHH7n4a9qdpJL8GI8otZ_zccVcblmy08zhrtaODZsRiUrMjX3N24SKQLua43p3ga08Kcrkej2bO-IsSeBlWe8uLtwJYzCo71zsIvPKCLCl4n4N_WSXim_AvKJDNrf3VuHCcs_lrY6myGKxAtQL082qAHSes8Kq4lWE9wYB67Uhd7m-vr0uX3CsNohsFRK2MFU_Hi3YPdiYoQKUmIF_7R5E97L2dzCwDTx678Tf8gqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxqm79ep8VTQpqdsr2yZP6Z5P9_CsUN3IXPA2EB2sALV_XK2UjVzDJnAYtv0M5kUkptjNwfS_lkb57pEhvfkEVpKEY_cWDtjgxYmUQTJUIgrfY9V_Km5fzFMDKOjEseUDE6DGkXY9PqC8RfQEjQOAX_mpFe8MSiwmW_d2LLsZWfzxog3VW9RiwSMG4imYikHlQTf8Uv16I975t6Q65p21mgsayKzPWDMZ7jZcun8ry7aymOTUwuRlYd2jTJuyYkfdMFXCXoO27a11BQRoQk0rKK2n20yYtbxXku7qeT0vz8vi8D5bjRyQjIRl6TatmwsmNyH6RtdXiOja07riBs5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk4Fgnbd0evljIk3sLuW0XOzesvmpoe-mdWgZlnYpAGDdkb3qZ8zmpWlSf-47RaN2NZzxlbJN0Gu97re5WNprBZsu60S8aQqwIH7x9ngG2wDbsWXdmDVaYSlbAWcqkj1vFsqNSQ_WGXkncnTKGhXCstsk1LNrhlBAOmZ3u6a-c5zFiHr6SiqXVpMx58bPfOuNhujivrulEXXC19p0zl0grHBmCQMynn3DliKs0fR0FqRqKM0niTS4uT8-0YqOp3-uCg00CIR2RdKpHH7ZNhfduhKVHnOJaReEKFyF-JkvLQibCoPfEAaF5lA4uG5zf_rMKJQjBXzOAvpWf4EjGlGGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI_4CsDsFkn4f2M4SRQSKTRqGX6wM4yySvPKyIKl1rOg1G-ah9i0YRjSR2JiE6DQ36vdjqpO0g110J7pSatvNiyZJyHM5PtSI552xrmYbpGqnE_J8WUVJ7QsOQ9xI0XnlAHdXgSqZ0vMq5lgODCIupX14WyQv6bso_tgCv55v8K0t0K8oYZ6Z3vSB5EsOdNSSIyR09dOeF3On5XaLUkVOe3Oz6WXvnXIwiQRatOmQvamGGb4SrJyxDTXJ-HYD-wqFi0vysjKfSfGumlsBmUzg04Ftia_mVnUZyoGrldlNCrsMK1ajvN21-RJtfK3k1NFH-aDqTkxlctgfU_ubDhfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=JnwMB6mprivxCy4YtTbMKECwmone_kBVDce0TSvnFSNXSEdqRRpB6pdK14WF85Rx-iwjjK9u6rau2p0Ky6angx9dML17Hn8H2JPuOrhJUEpcm-Dw1mPlztex-JWMM1mRn2b3WEF28vzsKRbUJJoRU87_63WLecR8FDJIcxRRYLhTbes09xZyPwLhGEnKWt27dz3bweXpYL5susFflmhZDylqVCB0xWXTtbSIaUAYM7QIS-Pplx321ogRa2IGeogSXuKI0aGvKrqfHo6XyGejmTgIzXQklSIWnYTZ5sl73tvFaRXnxAYYxpdRsExhgk1lDzj9dGfU3JpGxWdU1IXJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=JnwMB6mprivxCy4YtTbMKECwmone_kBVDce0TSvnFSNXSEdqRRpB6pdK14WF85Rx-iwjjK9u6rau2p0Ky6angx9dML17Hn8H2JPuOrhJUEpcm-Dw1mPlztex-JWMM1mRn2b3WEF28vzsKRbUJJoRU87_63WLecR8FDJIcxRRYLhTbes09xZyPwLhGEnKWt27dz3bweXpYL5susFflmhZDylqVCB0xWXTtbSIaUAYM7QIS-Pplx321ogRa2IGeogSXuKI0aGvKrqfHo6XyGejmTgIzXQklSIWnYTZ5sl73tvFaRXnxAYYxpdRsExhgk1lDzj9dGfU3JpGxWdU1IXJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhkUuMtgeBbkXEgBphAMgD3D7uiPlKHCtcUUgT4g7M5BBvOqmWzfEEFC6PJ4eux15VA6Oc46oNF2USh7s63TGeKQW8sfbnBJAi5BG5yQ5JdE8ZsXqZlkajUU6m_0-jx_2OUysLHZ9l3YPzcI4oD2IJg7Hm6YE5NHlS-7-BbcVAmBK7aIWHO4yUjr-tN1BK0Hz1gb5whBzW4eMaQnd_sbmceGJQ9ZBk3OIYex51BiSpj8Mf_0lpoatB3E-BBk6VD03oHYa2RX_gulVZAQukyd1PxDO1BmcFUV8umNG3KbsQIwsghzri4PnS4TIDQXycZgTkxq4bxnXcxNB2UzQn7jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl9AiwnfKca5n9E0KUSK87Ao1Ro_6quKhOwq2K5UVkNnF9VnU4IRi7pBXJqcMivIijQ7EWFjz5CXivp74H44WKrENnheh41gjwq7cQJzVe9XDye9TJYHCHfHN1rmDNtyuBbpGlQwT-Y3fIhqqGlUk0_NqRzEe27kS1uWYz7HucQn5cvuoRbgH_Xp6xLupMZncPdqUQrIAhWDCmRC2Sp7ZjKChTZkT0MlyRONme3Pz5gpHxMYvGMFIeXT8pRidwnghsMUfZXQqDjFFKTCWAXCaQXrxb3Bao7qNBTS4yi3M8Nbg9OEI0s-R9THvlbJUrrg9FaBJS5G3RyDuLNK_s-xLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsoLQEBoNSD3VuOrsgLA3ZJx-7Gg2L9CJjSCaei8ySOTqbbprfaEjf7iqcy-UKrOvI5CZKiY0-JpAB2UGQZFaik9w6jCYBR0d9Q3B_Z5xNdLOETpBsHSpZobQaxxO8XxLeZbXi1FjlK7IMnoenaVSJyGmeXMrqNngfjzpwEgE_cpFFRITh2ws11C3M-s21tBSWTFWcSVvQWIE02JC3hxrw0I_Xv7MspE8k7Pwebu_qRNOsWzyMP-KRLIjcPGD_tNHQvm0dcLAXVDQc-j0CNrFn-5t5AZNPXwCSUqvyLOxAvuZjR-lyZ5IltLgFfjXjX5KW0iwtiF7k9yvOqB4cEaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=G9-QgkJNmZrI4wZ4qZfSo_YNumLkkFaHoQC4YSenkbZl5EJIJnsxPMi7QTHr1NuEGoBCULfJee3D8IXVnEyLNcvlOwCZSaG-BtrbnlZ9F7-RqWIzcRZSERvAaM69b-s1SCF3iiekyJKlAG-elq6r0rf8ecZkZxFnuNCvDR2WtoQE19O1DcGkheF0Bs9Yb0oOEqMXs1lhoxOP335Z3IE-A8c1tcAl6lsZIquU0aTkHukL4ZZgjirHRJwlWA8zP3fD3JzZ2y1oEP9mYAKk4hYiV-63Zw_gdVhuPFhKMnesYgeshDka0Uv22_FQO-3GYCEr9faE3QXT3uUWuZauzlUl1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=G9-QgkJNmZrI4wZ4qZfSo_YNumLkkFaHoQC4YSenkbZl5EJIJnsxPMi7QTHr1NuEGoBCULfJee3D8IXVnEyLNcvlOwCZSaG-BtrbnlZ9F7-RqWIzcRZSERvAaM69b-s1SCF3iiekyJKlAG-elq6r0rf8ecZkZxFnuNCvDR2WtoQE19O1DcGkheF0Bs9Yb0oOEqMXs1lhoxOP335Z3IE-A8c1tcAl6lsZIquU0aTkHukL4ZZgjirHRJwlWA8zP3fD3JzZ2y1oEP9mYAKk4hYiV-63Zw_gdVhuPFhKMnesYgeshDka0Uv22_FQO-3GYCEr9faE3QXT3uUWuZauzlUl1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=o31ieUp3tOxyPMneCBnpyyH9GgkfXgfNEYlWw2QopqtGXzBI_FIF12-n72xbd1bmnoomJCszjp4-CKURjsgp8N3qiX3rKopUUO9SFEmB1k-o1RrKCYKAU0SqCD8xPP9KJN_MDa2l4Nw8dm5ClX2AMSGjICuFubSiRI-aj0Fm6ETVGfTq1IX8sAqwmprQBzR7epzVuYgCj9Qe4rR6JcUk_Aa3_Qpr5_miGGIj11-aMSGjcjESE1SdWONusVh4zK7IpTvx_jY_RfnWcJQ-WJti1DbDhsefIvMdh-BnNVNff8OBGee5W3_bMvZXIj60tQQI1AfSkgy3IHlS9uFTGaO57w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=o31ieUp3tOxyPMneCBnpyyH9GgkfXgfNEYlWw2QopqtGXzBI_FIF12-n72xbd1bmnoomJCszjp4-CKURjsgp8N3qiX3rKopUUO9SFEmB1k-o1RrKCYKAU0SqCD8xPP9KJN_MDa2l4Nw8dm5ClX2AMSGjICuFubSiRI-aj0Fm6ETVGfTq1IX8sAqwmprQBzR7epzVuYgCj9Qe4rR6JcUk_Aa3_Qpr5_miGGIj11-aMSGjcjESE1SdWONusVh4zK7IpTvx_jY_RfnWcJQ-WJti1DbDhsefIvMdh-BnNVNff8OBGee5W3_bMvZXIj60tQQI1AfSkgy3IHlS9uFTGaO57w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=RU5ItMF-LXhIXIIlJUSSkfvYDLyep7cDFJ5bcrvWrvsoIZKUtHZQwB6hrMDpBmn_YqrMflf3i9iAYx6_Uy0sMW4-RjQql3aLK9TQEVGQ_SQoyLDt03TAndwpxA_C-P2x0KpvaPwBC_2vCQU8AWOCRhZPT-h1If8AJo53_WTAfPKZje6seERUlsALqHYKvaKuemx2YZ94nY65urCTXDa3Po0NTfsGegvjo1a63y3blUr4-tbYcQiqMPo9IM3t_QYvF173ZqALf6pK1GZIL3HveFDpglqIxlCPd4lJDDMPCn3ZHdtfOoQnDymGVabakHl4kh9C6rFJ-za1Z-sMi-0vMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=RU5ItMF-LXhIXIIlJUSSkfvYDLyep7cDFJ5bcrvWrvsoIZKUtHZQwB6hrMDpBmn_YqrMflf3i9iAYx6_Uy0sMW4-RjQql3aLK9TQEVGQ_SQoyLDt03TAndwpxA_C-P2x0KpvaPwBC_2vCQU8AWOCRhZPT-h1If8AJo53_WTAfPKZje6seERUlsALqHYKvaKuemx2YZ94nY65urCTXDa3Po0NTfsGegvjo1a63y3blUr4-tbYcQiqMPo9IM3t_QYvF173ZqALf6pK1GZIL3HveFDpglqIxlCPd4lJDDMPCn3ZHdtfOoQnDymGVabakHl4kh9C6rFJ-za1Z-sMi-0vMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex-FgarGJDZU8q34ysG8ieF82OkYEfylBHKDsw-7Y_8KBcuivTRAkCo_wDf_kETirvuIj3wlp1zBB2JmmUGgAPAiC0BTsZxOzd_LHxUy3kAWlyHNkOSiPzKMnxpw_592-t_X6G3Ry-yrS3LCNSaXynbex7888ot7DB_Kn8peUmiyi1ciPvkEKrBkVlLSAwytmxeFu0ZtLe91mbLqC0PNoXmbQ9zVB2MnJwIC_gJlm21S8oNLFc_8PdJiPKQTCEyBw92CYoX-JktOMr6KSwXAmf2WrtkMPgF_aUyKp9f3KWkHWzCI6ol99c739RNh73x7i6OZIW_aGMrn1f3zjBga8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReFK0ao1SlsaWwhlM1TO_kVPt7W2dw5Z9hRfz10VuNU3moLxGyeO0eLhvpJD_3P85TgoKr0Ya0Y51sjm-2iRhe_L8DFfVmO0byGymycn1PUPLOQRF6ag-CrqA3jl8mf_j_TB18OvB-pGWHNbBb1sJHOsKjXuoEys85qpzjBmRDM7RPpKLnJZqXw6BFDDmSiXCef5pNGlbRSqC_ZHGRe-OS_k5luA3d_cotgpIj0kc6P8xx07PCoTKvthHRHriwgFEYgCrKnatpKxs8oIskxsMW6HestbToyHsVc5mYyHWzmKB6yvOvakMQB1U5KsFo4LvPI9Ck1ZbmDErN3SyN5u1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4aDCBDHVmnNltDu0lVxraxdFtoZyII5LbF8BcV7dRzXVAdP5vsfqeDMjOpJkvSYa2315JYCrQoE1YSqOKGGPDr0ghWA1al8nMjNB3SHirOfEGjInXD9EdXjLW5rqDwrn47Pw8RfOsTG55BJUk1LQUsANXYS3mwZKFboL7kJU7IMBFjQmQuzrRg-piZHL2isZxZ60z0kwmdqjyHIyFkHoRSyZUqKgLPFSsPM8HbnFweL_aDhfasXt4YVUhlZQhP3nCCTK2JnW304L6c0bYmaEimssDlxKKtI1gNAJDR0yZVjVIw2kaWxgmDmipzUiAplEhcmXxtYjrRPnBXqp0hSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk_mQqEXgnIcbgowdVHZ_KYorA3eNuX15EuwHfiXeqOskRaaAh5-tv70LOFf6WKPXnyfzPPVRCZjWNNq9yVyPWrApC-nqHYamHKVKhL8AHgwtIf4SRgA3s-9sBgL2UEAkqy8zCST2TMTMrKv0RU4tfyNRxq_ehgav_82QHmHSMcxGEUlWpJ-UPi18LAbc7WQMsCho1-pVVM-AalAQx-66fTDcvUr0wEcLZTF_RT0yZDbHfDgtA4dAdw6RcAvPv5B0clm5ziiUiMEU_vLiVi05DOohkTdo66rHTmoif0TsFVLNMbGAkS1XPXFLJ0GhCXxIMkjhmqP5693A6ZAerErQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHsSXiFL-qNdYGepAd32ZAMP2K4ncEOySTXtLUlnHyZq_hXk8JwA4haMicGnj4zYGtI8uY06XdAQ8wuIgyNEp-EDEMR54h4NIN0-jBgTxMZ21qbL0O_8HWEv7Gnt3Vpo4Ucgz4DiY_sVPPKiL4NpPejrZHBJHry4SZTtrRsdYZDRb-DyjXxdh9uwsRoBL-_ggu4gc9EYYJG9mfHcytRgSEZ1Y2RyRJrecHa5isoe8Wync24H_krp2C455xr7jbzDRYJDuymUWipVUbm3MwUb5xMNW7ck3HxpgvmWVaD_HGZ94JM6E14cn7DFXmVbv9dPVqxhVbPdf6fASWX7Y1c9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V58HWCQv0XypslBjyuIXC8SB9H6hySVSgy9D4jQrKBPmS6IIdAsxxT-QEAZKmsEhCt-2-JJIW5ANnN0n6Ko4mv0xHszS0Yu7OkStH1Kzp8JCDS7Cy6CtA9Wil8nZ9Nr7GPa5VeWyz-FsfJOQDwDFCoJeaaCkLEeqhA_q8JCX-Ving3fqIMTGSeryOe16CIbnLpA7KQiwSpilHhvZrzLlpxN6fnFaVYlRooW3fWpzMCdRoVJXq_dBykRYlCbJqfb_KWiqtBr15SpFdOnHbvC79En7bS09WlZE9tRK5ckrDJFvo6-SJKkv6YFxnLJcDfDmRco9HLYWbD03aEQExmLblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7sx_NeerdtQpZItC8wR0o5S4YJNZCaltWu8rrh-XjGM8Q7aI2gYpBGIERkNtT1ZtL_7o1ZTxirNxJ2XHNI31ZTheiFOOzYED2ulxwX9F94jswuF7mGHCXv8ITWtThwcWAMLVmeGgdg3fMdRg-5ByPtj7cVMfVsymwUmiZsPQv_QlXAR1MAGX1YvVXtHuh1V5NRSUHU1iSG3SuZifPqXFawe_raeg-IkQsTZdsgvBxVRqu_5TBfycRHI9HimuayUB-vsxYjK4G0r90ZBdBA1LbbhaVJ7cP2rIFZzwHdwKjcxibjI6osp6xJKUjGvQS_2IpvbvUueVle6G9WfKIUhww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqwEhwJqCYPjBYj6DS7Fn9jNUvdHzIDv8lCEGBUNqN7aCc9pjwOH9Dcz1DoMmpgXSZl0Nn_fEaBKqQSrOLf2har7FnJiyW1wNQF1DLWbVsr6uTTC_UMTEFvKSLHUKl5YUtnxqfzOpcMzFBYYeG4DMPuWSHlvOdpu0R3daZeW23g17ONAP1uQ1shaMWpeyksptr9iTDn8kclsoi7NS3FxhyoVMh-K6tEjkGH-ewk5xixUcLET8wNsM7fox4XvAP7ig_se876FZE1DBnAYsTz3DZHtsaT5QnoNAp9Nq0qWN0o_InJUIXmMChhq63BzHdASqG45_hJXWXBJG6N3LRxgOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6iF9RoZ0NctQZT3zU9EuSRC2QX7z0JUprc6ij6qCuG0r4gzVckgcnsuArrJP5FSYVY3oAud28uPI95R-MrW5NzlWECgoIEuIf1CxSMZBUYKGU2w1w7uQA2l8_mjtTk-EvbT1DyzIOcNTYNwrxGBsfi7tCAOkzqYddaL1vBkdKtcURNuxkFyVm8Krh3TeiF8cGrqqFDQ8Qc2TTAFrgYUeYTQhZcp4VAtphZM1onDYqvyx1m_ZOPOgenQaqob_c5YR-DPl33SnUyAL15T5CvghOPpwMrAwTtpXsT66YzRxZwO3mAaA4QydoRUBu-eiRiJzHCXInyQQvjEyt3YFVTTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBHtDqAcsS7W9g0V4i_a5Y81hDXcX1F-P_IGnon8lEnjKPykxFX-PJXhyvwFITZoK1SyayEYL6TdoFPib1j4ORdnB5BN2kYdJqZLf5Phjqwq57Ahia4HWj1RzjzJanF3uSSxhSwUNL-Rcovo5L4Wq2wq0qihWa8ONLg439FHGHQkIFDoKs26gCPg2YhBbrHB15hlcGqxvOchuiimWIjk3piTPlbrZoOdMf3gT-QJ6N_CLM5kbloYK65wazm2wg_OG5SFJcn-OE6Wgf3B6N0xs7MRBa2cTQAbPumeDWcKKYyAYBH_r6g6uxWA6ityZQb3zepHZ0z6INFUgpSmtxIFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjunpEkWbBGPjR0joq0x73_pkYROXSOtYLJHSQIw5QAXTVCXtYlorncZFQivBQC7_rKbbsjktzLacopy6Gjf6ZQW8DoFqvdeo-8AVe5ty7klorQDKkwZ_dGrzDgwS3s5n5IkhsdnjYZEx6xi1BmGfhNHTJWM6SxTVx5SdDAINPhSayGAenwgiPIk628nhV2ExEUn9bDW9Sv_-GdifvYsFs4DtxRnAeYKL_Zg-cFXRYT7Dxdx9AgFvIzaEcsqhBzSnVrGsqRkqDBFCcUlQ4eYini--gFPepMUki6pbhYfztkOUBNC3sUgZk7eg9qpb6z5pkTZkerO2NDF_hPwbXChdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBlgjQS7Fo_acy90uhXp4zTzJO7QofUNwoJ6Chrn03UJ6Uxe9Uvb39OUUTX-d5Xbj-soxWFnPsB1u0NdykTsGVQw-Eg9ZSnHUZJxXDh7BzE4bRoUOo3iQdZtts4EwbK9tgRDgTTuz2QYj0FHbKfrv4XLfME01QaXqTeD9XE3Jed-bPU8tQjmjQ5NXiJvp96JeLEJDLkXos5anRTmlP_P8_BKTcc3jFE4z2xXZ1EgRZUYAMh1GkZmOqKUEr5ea5EcnRH5uvAaAsTJr7HCF4UL0cMxp1L0AHxRZIGKuVjAP3uENQrfa4G4eEL2o_2cu6t6fHEhaaYN3RuDYoeHuJZa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBd5FQIymdKZ8sVvh8TFvKPSlkyNDvy9NnS8w0qdEKiKO1DLIL5VGpGm-SNrrC3fDtLge3VjLoD_khA-Nivf_Nr3D1YmA-MB42y8z5KHFtncqjfS9f9Sr4KdTDGWQnbJqr_Slsj5eJLWAbXjxaNJYMuiA_NBna6ANgh0NY6fbLdjyr329yeRLjanLc2uEhOOHzfjUnvBche1uXl087UtZaysbif7r4SlVteOKmXfYGIbQt1PiaLIbDiSXuEXg-xyLghxvBYbxmyyLJMg4iphDhJcdUQuwtjgULA_kfgMIQGCo9PVw9Wpk3L1u9DdKTMrNfjD-mOxTsWmg2zzzSKZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIfXFf0V5wwt9iQLwL7f6jKp0iUyjiQKgnYTCKtKN4yfOBs11lX5RqWSi5Id7jM5FOKyyNyD5YT6eE_Fft0W3VN0TNMNjOgD38lgoZzYtnhgXN8uTzf_YFHYzODaVC-hZOuju9_ETzfC9q8mm_j37nY4ga7d6LW0z38wrFlyqi_UxZcWw3W_Hme5DtnAZEdf4qgbpy7s2C7T-EQWwIWDPCQi8o_0YYOSGfa9ZHiy5kCXCfCfmQgG_enazeoMTRAGrA6muwX89HeOg8cY37DqguN-1qJU6aHsg9cNm3Zx4BLFoUJS63GoI_RC367My90bxvrH0meMoPszceKNejYccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aflf--X7KbadlqOs9ISvVwJf8obraCSx6eG6SdgQZIwE85Y0nGg5xsMScTGwNvlzkOpJuN80k0XlIEJ9Gd6ncQLmJ_9xo0iuteTMtn84VMlKiqoA4UwXmwQDFh8B7TjniDeYoRHq7zMjhhV67BzmLbkvya8zdmtUspDFJgg9jQCIBmGg-l8wyZJeQXfLH-_H-GUnxo2Bvq5hlFDxUXOZzMBj2UVgRFvyv0-64bj4DI5giZBeBD4rP1lM4rs9MdhdgVyZ8z0UEUg3qqqezxVfgQy7vOaAvex3uuMEsgpfEhMbbbr7YtblDSNjxLVVsS2Wevg6oa1lJcKmCZgIPwG7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=CeZgGdHFbi3wG_C4UL9BNZHB0Uppl_X2cyU1cmcRoFG0b5UpgTIiUDXlT4UwuMjb0a45_0Ert_nwPBGAv4QEmOArft0EJTb7xMpqeCWf8z95vCXeffgSS8WhD7GH5rQ8c1rtz_p6cVBlFfufNgLoeVTltFsO8jikn4gzMtpBLS5W51u5VO4v_gCgfrAtJyGtKnyCoZLTA_DY7QerjFuj3mqUzLqQqEQ-C82rA0r1qLA2ZbmdA8KvXxk6uwQe-xBce-V3OkfoNeWsRwybBkdezwQGb8lRS9OcL78PDBmWanhAcnVW-2qGvGwYvxuvyAzRAdukL3rd2pcjLWL4dvYz2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=CeZgGdHFbi3wG_C4UL9BNZHB0Uppl_X2cyU1cmcRoFG0b5UpgTIiUDXlT4UwuMjb0a45_0Ert_nwPBGAv4QEmOArft0EJTb7xMpqeCWf8z95vCXeffgSS8WhD7GH5rQ8c1rtz_p6cVBlFfufNgLoeVTltFsO8jikn4gzMtpBLS5W51u5VO4v_gCgfrAtJyGtKnyCoZLTA_DY7QerjFuj3mqUzLqQqEQ-C82rA0r1qLA2ZbmdA8KvXxk6uwQe-xBce-V3OkfoNeWsRwybBkdezwQGb8lRS9OcL78PDBmWanhAcnVW-2qGvGwYvxuvyAzRAdukL3rd2pcjLWL4dvYz2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ2lwx6QDOac_B_PS-5YFPdqMHpluvdt7kQ6PFOke7A1V_Gmnd85ST19a2jU4sO3qB30DAoM_ZyWT3SlFxBLu3S-1hj7Fy_IqYrc2wMiZ0kD1tfzvW4wWMHCL-vIrET08cgGN6OCQIVLt6vrakxON4bHxBDrQn7MRmgIOtqawulrG938j5z2kTDLgrTgPOwjzHBNQnowhgcnzqhonCbbeYcJ7_-s8F973hm0JVZo50d7pULjhjRHjHPAhe-exaNtikJx1-aUcn0j3heoCmx5AaGbQnJ-KhUdhGdpoypQHgFKPgxYmJWpd5Higvf5fQFN27UvlhsZwjOHgJgLYf2dZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=j6p9ZzNVCfHNf-xq68A_2DsF1IUJwWGjn8TLLCkRfjNMAgVQ3dwQeGWMHo_8Mov_07ZL4faxQcY4KDmRtzAnoUska-JlBS3sjCGL0BvXnQSVgvnCctBLgbao-XwsQqOkP9SISSMebyND9Vawc2YMaClZxjCBthLB3v8Cr9TD0sDSf8rifNahde6Wj8kYRH-nJxnEEiplVU_cVH7fnEp3pBU3YNyvzg0gwZgRn3wR7opaHXYY4qaimF9WCfOrsdmk2Ke-0T6ltfgSi2HNLwUsq5Dcn7hcoIyz9iDrm-Girx-yViHGMYCdswQn8MkMQO8LtEocE18NYSLzB7jFH0P7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=j6p9ZzNVCfHNf-xq68A_2DsF1IUJwWGjn8TLLCkRfjNMAgVQ3dwQeGWMHo_8Mov_07ZL4faxQcY4KDmRtzAnoUska-JlBS3sjCGL0BvXnQSVgvnCctBLgbao-XwsQqOkP9SISSMebyND9Vawc2YMaClZxjCBthLB3v8Cr9TD0sDSf8rifNahde6Wj8kYRH-nJxnEEiplVU_cVH7fnEp3pBU3YNyvzg0gwZgRn3wR7opaHXYY4qaimF9WCfOrsdmk2Ke-0T6ltfgSi2HNLwUsq5Dcn7hcoIyz9iDrm-Girx-yViHGMYCdswQn8MkMQO8LtEocE18NYSLzB7jFH0P7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=MxgAQQoiIzDY7P6Hkkfsc5L1HNaUuLz6xsdKJIhEPIPMZz5i78VSkYj9d4enw44SSJcLsXsi2Lqdu6vd_O0y5ji2TZgwuHhwCa1LmFrnpYnBFQQVtTz1XYxvG6q6GjOf9cNSlF7f1kbCLMfrnHCpm1lJVPP3Nh5DsGZlhz6dCUN_UIkXqFH4Gc96Es45NGD8c_hy8CNVMetOtABLN7MtzRNGOA2uEDjdMs-T3UuLAribyujyxgL4ltd0Lqc_fBcYrBmM60Fldi0Sbo9UFAP6mO5X_zgFBXSkQOFqeSLxuqdcmeXAULgp25kzJ9ToNEPKASjX0fDFoaw2WDB71evzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=MxgAQQoiIzDY7P6Hkkfsc5L1HNaUuLz6xsdKJIhEPIPMZz5i78VSkYj9d4enw44SSJcLsXsi2Lqdu6vd_O0y5ji2TZgwuHhwCa1LmFrnpYnBFQQVtTz1XYxvG6q6GjOf9cNSlF7f1kbCLMfrnHCpm1lJVPP3Nh5DsGZlhz6dCUN_UIkXqFH4Gc96Es45NGD8c_hy8CNVMetOtABLN7MtzRNGOA2uEDjdMs-T3UuLAribyujyxgL4ltd0Lqc_fBcYrBmM60Fldi0Sbo9UFAP6mO5X_zgFBXSkQOFqeSLxuqdcmeXAULgp25kzJ9ToNEPKASjX0fDFoaw2WDB71evzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4LSeE6TK2PeXSHSmWQOFlB2vZr8q_dCJ_FbGdog0esJ3ILjqePSx17yyU2jN5rOh7KTd3CP7a-6RycQbvkBGW7GQFhnPyCvRu32sOKm0fUV3-72qTn16wsnh29x0OGGGq5pAc85xMd_ak6d98OosY3gkjzsI-iCvqMC3cbArT-PvgGdCO-TqJxy1vA17HccypAAh3_OnYzeM_5xxfFK1NalRATKy4OyZq04RaND9xWg1Y0pZq3xyy6X9L0WJSMVXQYg8CwWHr_jhEHhLS9Z8cwsx6todfRukB7V7ttfqEkIE5Wage7ii3sOmS1QuoKK-ALBdkqgzcpZOTYknsmkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PK5Pttu34Y4G4-tx8yDiMTUEjGMBI_cr1LKaXgipq5DlhnUjIhIxC5w-BzU9IUQCOq_dkLofL6cTEZddtJfKNMCGvn2jd-T7b7cxaSas6b8Td-Hd0qeA2S6xjfDliO4RCZi9m0AehY1XOKyFAGu8tqgnkMkDMBLLv6vejOkxTD9knFeXOjcpBYVIyvpGHUfJlUahyi9Jy_36wBWNXCedSQwL49__0wJhBlJ1pZs1OVHrMtWKjrytphI0lFWndSleRsxBNP7n0HeWmAqS19I4dHLRZkDUodjkWina4QC2DdgtM6kiA8EyjBLHe4X7BE57MWQcQ1fPu29Ovn7u7nbuPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PK5Pttu34Y4G4-tx8yDiMTUEjGMBI_cr1LKaXgipq5DlhnUjIhIxC5w-BzU9IUQCOq_dkLofL6cTEZddtJfKNMCGvn2jd-T7b7cxaSas6b8Td-Hd0qeA2S6xjfDliO4RCZi9m0AehY1XOKyFAGu8tqgnkMkDMBLLv6vejOkxTD9knFeXOjcpBYVIyvpGHUfJlUahyi9Jy_36wBWNXCedSQwL49__0wJhBlJ1pZs1OVHrMtWKjrytphI0lFWndSleRsxBNP7n0HeWmAqS19I4dHLRZkDUodjkWina4QC2DdgtM6kiA8EyjBLHe4X7BE57MWQcQ1fPu29Ovn7u7nbuPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLEjdreQPlAfolJoBLy5TdvhOnrTToacb_9xHoHRe2oH7K1OEoBEAt0ogogFcvSGF4yUsW8M-cKVaUT9rc-qtkt0NUXLoPSmMIbSb_e8q87eKQFtVYEUzNRCCj6mVGlOtlAn5AKcaCTNb7hbDiA3t5z4mSoUgl8MQRpfMww48Nzc178Ts8cMbYv8W2p-dX43jgqbrhBr8tLF-GaHwv3OQuWm9cSsq9UnKcGQBEljZpNYueDfcawAJAcbuE1LpodNkJC-k-ljt9MWb9uoddIfvbw5rfrWF-BTOBIUWRLx6pWII3B64MUne8lgK0A_R6L0urwI1xfmb5fPxIbFVFijhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwSggJY_Rw1u4UDOEPk8ZchmSFbf4kpPfYD6K7HlYEpSSSTqxDkzDK9f8It472hMFCkgKzl-okPBI--YbJUmeRj-VkDLQ04fc_w9755ur79e5Z_OhmyYl4HY6MpkcvQLTYruuJLUwEIQqGSqwUQYbJvTQuhxq0bqGaJMVU_PtjTjKVW5lQMPU_dylBFB4hj36WABVQU-KcfPVs6_LahXZzciT8j2FA-_rXg3foLHNVvi-iHocRFprGGzbpGaQT6tTfEknvHTdqUI3ovVpQ-4EmVPzTnty85Eev6JpHv-2j0wrelBHDcd8hJ7ieO9ECEmkRwHPexvo_ssp26QH2HcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdLd94iQchTQMxfA1kQMoQy1r7h__zpuKZ-W0CLdswTTdOz5RHc-VObfz2GFU9Bv6mPCP0BjDvlc0P-VMLFxV2mBDiS14VEBaKDtkmJ9R1kWFWS6NjctVOOSlrTkNxEoJWogbRGK6zzFRrJ5F-PgOC4m0py9ehTkchxwUCXo4L_4LI4oUgfEw48bHt10jEV6DHiannqbWjRVyQL-vGVMqUzNngzzBnWQr03BwumKjlFqoUQ3iVorXscS4IxhVmANzTV00aqM6VtsoRdTqaBxQUuqypf038X28hO7QmSKrrE8kcQ9Mt1dsg3v884sjuFUwvOsNmuQ5SVKm4w7ZyaR8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPQmoHLfwbJR0w_haHezY_O8M0GHBW7sqmRx-C-dCzVGqWUAdTAciwVFG4A17ZEzYUHXfiCfZEAjdt7l7MntlQXsPcOz2wfa-Ekpol-Cjjdds3WTlnrslsF3wElOyGjok5z3oaD8HBkRrXPA1IaxHyUu-FeQ2EweT6UoXUqkZG_K9ZSfHkX4f0Iqb97OqOLOENg_irZ4McJFdxHcOxE3k-wJ72EiA4NUMExGzaVrgwOrXV9JVoJl1OJs1-gQ9oyETiaqSi9E1-PEMFcgfLgX5cizWO0KgVn4OISZbCbagVziCvZVqnUDHSNgnj5QtpQRyo4uR3UDf-5TnmHvy5UTyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=JpJpGGKnDvEFB5U-4DJeBTeP3h1KsnE4BIIGhHhJXj8wmjU6N8ss7tvEWZf5gPGPE-ivWFAC2jOL0gAgpmfBruEkcQ_WL87w5Yjz_pQkesQYK7f2y8ohl5peW-_vnAvt4n9phbRRg_7lV4GzLeGhgGzJgFc4Yl-naI5Z7gZOohOdIAPJD9P1x-lAFcHnSRNoUDMt4YNbrbLeyMb5f2-jCzstg1dEeTGmUrSgDr7lkVtWgk8AfLGSB3wB_r-y85RL4JhY7QA9eMsT5SR0DUJcXB_L4P4C8oFZI8lZ9rLjedNbcER7X1G6NedJdOvcSko-dcIg839qNdfsWUlWdDowew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=JpJpGGKnDvEFB5U-4DJeBTeP3h1KsnE4BIIGhHhJXj8wmjU6N8ss7tvEWZf5gPGPE-ivWFAC2jOL0gAgpmfBruEkcQ_WL87w5Yjz_pQkesQYK7f2y8ohl5peW-_vnAvt4n9phbRRg_7lV4GzLeGhgGzJgFc4Yl-naI5Z7gZOohOdIAPJD9P1x-lAFcHnSRNoUDMt4YNbrbLeyMb5f2-jCzstg1dEeTGmUrSgDr7lkVtWgk8AfLGSB3wB_r-y85RL4JhY7QA9eMsT5SR0DUJcXB_L4P4C8oFZI8lZ9rLjedNbcER7X1G6NedJdOvcSko-dcIg839qNdfsWUlWdDowew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=JOJEm4SKfTPRASHizYbe6QQETSGaiddP0zB1ScLq_tuDhMmvpl5CzmVUkGrTtUTaRtvgDrkUR7QvKYSaaGqsoyEuy8tk3Azptmx6DLZg_sSSx05Qhea9AfQEwYkTr1VMKAEhGD1a2Y12IYgAHBpgnoGW4k8d5cfHLg6vbc2BaYLyjQCRcLRB4XGcvb4eAXk7Cl2jop2CMejRxW8uF85mxyWxsM6PSO-IVcn2iNyJQ_984nebm9XyNMV7EjRAzWBpCQ2FcK815jcHXBQrp7RFXR7OVkiKmF5sRx3NXAA9jYseaJqDrg9M-NBDk7pVMWd79UUJjhbM896wyQLd6PkMFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=JOJEm4SKfTPRASHizYbe6QQETSGaiddP0zB1ScLq_tuDhMmvpl5CzmVUkGrTtUTaRtvgDrkUR7QvKYSaaGqsoyEuy8tk3Azptmx6DLZg_sSSx05Qhea9AfQEwYkTr1VMKAEhGD1a2Y12IYgAHBpgnoGW4k8d5cfHLg6vbc2BaYLyjQCRcLRB4XGcvb4eAXk7Cl2jop2CMejRxW8uF85mxyWxsM6PSO-IVcn2iNyJQ_984nebm9XyNMV7EjRAzWBpCQ2FcK815jcHXBQrp7RFXR7OVkiKmF5sRx3NXAA9jYseaJqDrg9M-NBDk7pVMWd79UUJjhbM896wyQLd6PkMFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=swetDWh_GVI5rKWZ4B0nLxptV-uh9NNOs79jbq1HDbLnRWlm2nChkIOVzCpjPj1c4TWda345QB0I5PVXvGtum-AVKv1XwbfXDlbg4cfzKu3LQP9GrVkcTow81qr8_VE3yfLB8hssf6mjs4AfZbnt63IMvzG3ES23ulr4Z-X2yNxpY7jywEwrfXDcJtWHYDIjDMxcMi7GVkAO76cBKYwKOUNIXelqqIiy-2bfPAcostdKjJLQdFbEb5mrJxt7-dGeJKykOeZDq97yy227A0NfxELicAkzkjFWJOxP4ohIou76OAGAwsxma9wKy-VPCrBpahdNg936IPELfKJKP0ciMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=swetDWh_GVI5rKWZ4B0nLxptV-uh9NNOs79jbq1HDbLnRWlm2nChkIOVzCpjPj1c4TWda345QB0I5PVXvGtum-AVKv1XwbfXDlbg4cfzKu3LQP9GrVkcTow81qr8_VE3yfLB8hssf6mjs4AfZbnt63IMvzG3ES23ulr4Z-X2yNxpY7jywEwrfXDcJtWHYDIjDMxcMi7GVkAO76cBKYwKOUNIXelqqIiy-2bfPAcostdKjJLQdFbEb5mrJxt7-dGeJKykOeZDq97yy227A0NfxELicAkzkjFWJOxP4ohIou76OAGAwsxma9wKy-VPCrBpahdNg936IPELfKJKP0ciMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=eGvs4vMIbSebn2asc4243TRlQciD4UOZynxTFa9u0LqrhocNv6T4d9ULKAFqbDhL9mpYjL36lN5_qN-oRZvpwks1q6Jquyd1kT2OgM7s41sSfEFUu66BwuMiV1wHWdXpvDiFBPsfwhIO9GsxydlIQe6xSvWFsOc-Bj_07yhA7_f02cUlo4d0Xf0vzsYCmUNG_v5is4JFufb4uAYZli4ASGAEzfkodSLdgm88CiXGTNHTAknfnhsW2ZUrftmLcc1HZ_nl8rUWt2sO8bNi6aS7iCfcNaKZjZmRSJPBy_I0oA0eh8d5frVFmliEkg0aK-AyfRsoUqG-pQs9n6bsZsSlaY95Pn8VNyD-nSUGaD6_5KxI7G7y8DoQvy8Rq6P28DdWXNC1F0wFPyeftcL--8Ds6qdDuzYjnhYpsl5Pz5PBmshE9qiwMP1bnuqROvvr_ZJI-8FxF5VxAXf4NWAbXMKgUMLiHaZFGSjKyywnMO1C47jYiY_GTJ4g05SeHHzSBE8utFAzMew4c6UZUQPoPtu9m9vVGA8xjSADQ2Dt9YL8Qgoz5qJ0K1kOfe9k8cAbJV91jRRIdpTPl7UtAbhHCpyeBv5cDXIhi5vpYiQrtDb05hDkLTwZIrosT6D4a9_bDTsgW71LDcqleJMc_BnHagc0ksiBZP4lwhYxgCUsQJ87Tos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=eGvs4vMIbSebn2asc4243TRlQciD4UOZynxTFa9u0LqrhocNv6T4d9ULKAFqbDhL9mpYjL36lN5_qN-oRZvpwks1q6Jquyd1kT2OgM7s41sSfEFUu66BwuMiV1wHWdXpvDiFBPsfwhIO9GsxydlIQe6xSvWFsOc-Bj_07yhA7_f02cUlo4d0Xf0vzsYCmUNG_v5is4JFufb4uAYZli4ASGAEzfkodSLdgm88CiXGTNHTAknfnhsW2ZUrftmLcc1HZ_nl8rUWt2sO8bNi6aS7iCfcNaKZjZmRSJPBy_I0oA0eh8d5frVFmliEkg0aK-AyfRsoUqG-pQs9n6bsZsSlaY95Pn8VNyD-nSUGaD6_5KxI7G7y8DoQvy8Rq6P28DdWXNC1F0wFPyeftcL--8Ds6qdDuzYjnhYpsl5Pz5PBmshE9qiwMP1bnuqROvvr_ZJI-8FxF5VxAXf4NWAbXMKgUMLiHaZFGSjKyywnMO1C47jYiY_GTJ4g05SeHHzSBE8utFAzMew4c6UZUQPoPtu9m9vVGA8xjSADQ2Dt9YL8Qgoz5qJ0K1kOfe9k8cAbJV91jRRIdpTPl7UtAbhHCpyeBv5cDXIhi5vpYiQrtDb05hDkLTwZIrosT6D4a9_bDTsgW71LDcqleJMc_BnHagc0ksiBZP4lwhYxgCUsQJ87Tos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BdvVSuWzm-rcqTDk17Ieuick5BZ9qxnzFNm2CBUEISdiKUecEl3ioGsxfqLWH8hP20OLOaXvCWVGfWxeZBjwin5cT502QqboBnitV5sCHtJILwhid78gv5P3qrYeRrnSotektgJbKgWyC9i_3oJ1Psb14Tg2YajD7RPnU9h_P2F_EkFRESbgLR2tgWwL2y9ap1o0Ke6F4iYaDEK1SQbfNh8KOQ2LE2G3CmKZOxfFX2-Kn3M4A55zm63W2V5uWgzWhOp7nw3r0FZedMMZURVv7Rsrf0rb7CwqHvclmf8M4zWDIzLHyW3dg8Ew9D6MoUb9Aji8TR8TQSa-Gbk9YIibWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BdvVSuWzm-rcqTDk17Ieuick5BZ9qxnzFNm2CBUEISdiKUecEl3ioGsxfqLWH8hP20OLOaXvCWVGfWxeZBjwin5cT502QqboBnitV5sCHtJILwhid78gv5P3qrYeRrnSotektgJbKgWyC9i_3oJ1Psb14Tg2YajD7RPnU9h_P2F_EkFRESbgLR2tgWwL2y9ap1o0Ke6F4iYaDEK1SQbfNh8KOQ2LE2G3CmKZOxfFX2-Kn3M4A55zm63W2V5uWgzWhOp7nw3r0FZedMMZURVv7Rsrf0rb7CwqHvclmf8M4zWDIzLHyW3dg8Ew9D6MoUb9Aji8TR8TQSa-Gbk9YIibWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=YQqLWX1Cp5UNZNX8dDpn1x02X9RxEMJbKPu_0-0dMORKXExakB2tQxnouZI3kd4G5uNkjgPS6VkvtpjvEnai1Ivy07hPmchu3R567QDr5kuOPE3MlnQfmTnHop8IeCW_qVqv6bbu0oGUlrx-zMMQRTZ4UyVZl8gJ9IS62qhc2qORmT8ovYCnjwcAFQHCsoJ_ILFdU0Nvmp0FAz-gSocLDFYG35SZkaz1bVwcic9uOmDBOoA7I23if475zNJkwN-7DarleWsptLL8vSSOh9a56FeroygwbH59g9hDwLT_tasbiT5mew1o2X0tVWhl4EkcJ6zb0ZftEOoiclv3uIKUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=YQqLWX1Cp5UNZNX8dDpn1x02X9RxEMJbKPu_0-0dMORKXExakB2tQxnouZI3kd4G5uNkjgPS6VkvtpjvEnai1Ivy07hPmchu3R567QDr5kuOPE3MlnQfmTnHop8IeCW_qVqv6bbu0oGUlrx-zMMQRTZ4UyVZl8gJ9IS62qhc2qORmT8ovYCnjwcAFQHCsoJ_ILFdU0Nvmp0FAz-gSocLDFYG35SZkaz1bVwcic9uOmDBOoA7I23if475zNJkwN-7DarleWsptLL8vSSOh9a56FeroygwbH59g9hDwLT_tasbiT5mew1o2X0tVWhl4EkcJ6zb0ZftEOoiclv3uIKUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQUGMViK0k_XsDu7aENFYd6ZrKQ2aydbWWVureEzi-8rOIFfEnntNSv3DHV9LFIRJHYojOD_pJCK7MHH3n0UdK9JMfHgynmvfz1nELgeo9kcCBLZ5gPHaEJK7lpCqYwZ2QFjmHZ6klsLH_cQ47wuF3XCCB-fF7p8FbXFEVMsSD_hZwl1VWn6FIHtLKBRXII1u_aa8-vuvohiFvSXYl_bP915BZ7d3an68JUMBYnxkU1BiLALTwaEOR8kZ-S7sjFwi4nAA5oE3GFioX4md5mvfz5h5D0qqOrNXOQNfJ_2UBIsohglGAmccJ-l6obbT7mUEHRHRK_SR15SJW-l-aBDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=nGeqxEaFdNNIu8ihDXmSY4E-IWXj0yTNTDXeDFiqKiGFeI1ianZ4ynjdCajvmT0OnVUzsNe9-DpjF1kWLxcqVD0x13gt3kGYon9l0_csngFLFdnaHQnA3Y_tNGldMQ0d-VOfJsr8JFV5clZSV5NIoqx_RCzqYStRjwdCGWICjuX2P5iPCx4g7ZGXWHqniDii0BtnONAg62zWYHeAA7szyr5OZ7-WZm5DK_HVd9yW-Nnc047NrWzeUpOe5mL9JZbQpMxnFKLHuAR6SLbWpNe9c2rxZbzWUSks5Buhw5Rc9FMTMVrjGXJoJAASaNqp_IOy_CWzzshjEXDHRTiYUdFI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=nGeqxEaFdNNIu8ihDXmSY4E-IWXj0yTNTDXeDFiqKiGFeI1ianZ4ynjdCajvmT0OnVUzsNe9-DpjF1kWLxcqVD0x13gt3kGYon9l0_csngFLFdnaHQnA3Y_tNGldMQ0d-VOfJsr8JFV5clZSV5NIoqx_RCzqYStRjwdCGWICjuX2P5iPCx4g7ZGXWHqniDii0BtnONAg62zWYHeAA7szyr5OZ7-WZm5DK_HVd9yW-Nnc047NrWzeUpOe5mL9JZbQpMxnFKLHuAR6SLbWpNe9c2rxZbzWUSks5Buhw5Rc9FMTMVrjGXJoJAASaNqp_IOy_CWzzshjEXDHRTiYUdFI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeeOjlNibiHKdVCKUmBRTyGj9ij-WoG7I6fW6TMOuRaw_0XqYrjNHYTQxCQ-ZXdAoAZS-JcmNZU_YpV3u0TrHSh5bu1ynbzn_JN46NxMmwjyOsgk9yUpwyS53MQAcMzSy3mHpxUVNRtrAblEjWQTtJaf9hMvGaZ3vjeRtzSNrXriInU9Ic1ETyiZsR7Nkk8UFXynHb2ZiUOHJ48ITEnDA85h5x7JXW9LlUEeK24flzHkBt-EcTOs5gxcbuS-UY8Sa9OeAwpvAwhu81hxBKjRrVUQuudWIWiE2b8QeqzEc9Mpkt4iNg3cowykc9WgmS4Ik-i3UcNAUCc7lM40PEHgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8yR3mPae-Z_3UU4KWmvdpCDvdLNVsbH11moPyIrVeHRJ1s4P67S0OtQKa4WvrN9IVuWI0OtY0_3iXvQrr_hUOq9tncUJ3mWmUn9XzaKnQVN317MLgHDzuOvlx6ii3_nfXucvUEejYpOMrey3TrwKjEaUjMUo7g5kxaZV7wuFnXHjy5lvC-Y_H3D0hjfV9Sf8HOCvS3mNsyI2UQgg6dPpkagVSTJOfu0ooe1U2U2YMSrl9Od8HyZWD6cEIKUYOXXUGiND7ExmPaU0gjhu-6_hDHdJWYnIFii7QZzLkvhQUXx5opmaJ2iiRiJ1HExyMzEl9YBE6iTVHHk9jtZpoXO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=VgN58XGGVPAURA0ke6RNtmDwvzFrAdR6YXIFt50oBRS8kesmxmxxxY1qedvZWXkxCW5PITns9Ltu2DrRbX10cexh1LXRwnY-jnxSBWr9BM_3lFEFrhH-b56fLthrcnA81Et0s6hDjzFPGf9e0vocI_v2ZVwmCF_4HWZ-P7YXEjw5sJeCHPoPcwuXIROVDqGTWsatjmSS9LUNDvtzVnbX5w-KC1aGLEJh8j7JtNnpGINsTdxLA7Mdkz80PBHcz7_Xp65LgI8fFDQbgB7Fx_9JyZclnkqyJrxPrKLjhHArP5iAkKFSG3hoPic9M9Dej1Wluf6oOu44N48hgqhQDRDTqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=VgN58XGGVPAURA0ke6RNtmDwvzFrAdR6YXIFt50oBRS8kesmxmxxxY1qedvZWXkxCW5PITns9Ltu2DrRbX10cexh1LXRwnY-jnxSBWr9BM_3lFEFrhH-b56fLthrcnA81Et0s6hDjzFPGf9e0vocI_v2ZVwmCF_4HWZ-P7YXEjw5sJeCHPoPcwuXIROVDqGTWsatjmSS9LUNDvtzVnbX5w-KC1aGLEJh8j7JtNnpGINsTdxLA7Mdkz80PBHcz7_Xp65LgI8fFDQbgB7Fx_9JyZclnkqyJrxPrKLjhHArP5iAkKFSG3hoPic9M9Dej1Wluf6oOu44N48hgqhQDRDTqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=XGArF5yDkg6NL4kFX9rxGUAIHgU0xW6jpUmS53kZau3BjUhJdDEWYmxpyeQkKn9hz9XTpqTIWPq9Xmfo6DmvbEQtheBI1TfxFOMeHt0swdgDH_JdwLFe_hXRxfCtCFnfg91SIZebyW1IFHb64ATZmZoaTAzcmUy2hqQanL9d7BuX0qdmTiRDWFvD6qBBMTDCCNNVBum5ltsXAb7ze3ozMQl0uvy_QbTKxCUPBIojSN4chCwy8cSkKdX94JnRrBpdvswo8CJzVvcEo35QDxwPASjUbIB3hO-hh3annw3OP6cPuYxR6EfQGWSUxsPxA6UeXrzG7UlCTN8SYDYP4fX6Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=XGArF5yDkg6NL4kFX9rxGUAIHgU0xW6jpUmS53kZau3BjUhJdDEWYmxpyeQkKn9hz9XTpqTIWPq9Xmfo6DmvbEQtheBI1TfxFOMeHt0swdgDH_JdwLFe_hXRxfCtCFnfg91SIZebyW1IFHb64ATZmZoaTAzcmUy2hqQanL9d7BuX0qdmTiRDWFvD6qBBMTDCCNNVBum5ltsXAb7ze3ozMQl0uvy_QbTKxCUPBIojSN4chCwy8cSkKdX94JnRrBpdvswo8CJzVvcEo35QDxwPASjUbIB3hO-hh3annw3OP6cPuYxR6EfQGWSUxsPxA6UeXrzG7UlCTN8SYDYP4fX6Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=jQy_t4YnyfvIM3bsFc_jyz67_kn44Q00T6ZoyoePHo2CxcYt2x5WMIGumMt1Pzhrg1p-m8fAJ9mogP8pX0kQJXhJL5luJGQBBiHFTXBrIr2H3OEQ6YFvEq5zu1hX1Nv_bzeZvjZlp2LGxNV70yRylR84SLfV1PSKMw0UImzK35A0x_i1X2Nx1oEmtO0JGE-j2vPEq5HLkK2Xbs4k6DrqsIvxV7dCxZin-9Pw9Ku1xCREojhyTmJh-c3wrDDSgG5cC4XXYY7jdfFFFHl_Uy1L2xLwtnRFbDnXzsTlkLehUuDPDI2_HTE3sWh-ZrgZViLWJsNQLAGVLuLJZr2A7cedpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=jQy_t4YnyfvIM3bsFc_jyz67_kn44Q00T6ZoyoePHo2CxcYt2x5WMIGumMt1Pzhrg1p-m8fAJ9mogP8pX0kQJXhJL5luJGQBBiHFTXBrIr2H3OEQ6YFvEq5zu1hX1Nv_bzeZvjZlp2LGxNV70yRylR84SLfV1PSKMw0UImzK35A0x_i1X2Nx1oEmtO0JGE-j2vPEq5HLkK2Xbs4k6DrqsIvxV7dCxZin-9Pw9Ku1xCREojhyTmJh-c3wrDDSgG5cC4XXYY7jdfFFFHl_Uy1L2xLwtnRFbDnXzsTlkLehUuDPDI2_HTE3sWh-ZrgZViLWJsNQLAGVLuLJZr2A7cedpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtYKNhkYe6x8cQJSg4SrRpMeD5wrTTuR2ZBQ035E81tRigVVv3aiBwEEAAeuvtkInrbbTtMuY4mseycfBc_atk_nt-XXGUYXMpkX_S-XE8YQykx4o3VCrFPqC4uggO3QlC8GU1Xydt1xAN-gK2aV1qzLPpb-oLM57_CLL-sBu-iEcPY9to8KWkHW2cKZRoiQme0EwL30_XP1L6nsXNpANHb0sRf2_HxtrV5y8MhrfflOX7tVlR1LO5ei2AEi_WtA1NRRcJgkdEfzFMt6Php4QR8ojOHYUVsJMNtItv0OqucGBayE9iIe9AQVFQuPrf5FabKofghDlFlK4WBUbGwpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=qP6-vM-T1WbA3GVCcJnfnI4Mm4-SoT801mHTRqlngVteXM7FbuZxIMqGOEQkQwVVyTg88M_-EEoYmkvsqTlHQ3mPJTeT70RK8EK95k5Au2B4pwytK9uzpPp7jhcpviAgFKxHzJGbVwPUchGj_w8zPN84L2DQMPVIm0Wcv7o5JwVAPrrMiDtvOIYqsPi3Kql2AoKEO2vvFV-HBRW9P5oJ5LlT4ZMlygtO4Nr9F4DQZRPk3FOiRtu1z48EewH-ipgSNG18AxpYL60FGVnsJHdM7-alv8KdNdBrvTm7rz2heUCoNOOqWarPEQfa_jm4rRfyr__y5SK3ED8t_chLao2CVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=qP6-vM-T1WbA3GVCcJnfnI4Mm4-SoT801mHTRqlngVteXM7FbuZxIMqGOEQkQwVVyTg88M_-EEoYmkvsqTlHQ3mPJTeT70RK8EK95k5Au2B4pwytK9uzpPp7jhcpviAgFKxHzJGbVwPUchGj_w8zPN84L2DQMPVIm0Wcv7o5JwVAPrrMiDtvOIYqsPi3Kql2AoKEO2vvFV-HBRW9P5oJ5LlT4ZMlygtO4Nr9F4DQZRPk3FOiRtu1z48EewH-ipgSNG18AxpYL60FGVnsJHdM7-alv8KdNdBrvTm7rz2heUCoNOOqWarPEQfa_jm4rRfyr__y5SK3ED8t_chLao2CVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=TBFbS4Gvv-cbo8T-5U2OeLeC6l_IYtynjMsfBhd7WUhD-oVhp71m8I69JUAfdIL2qhF7Q3V3ai9j7fyu7OblhFf1faYwkT7ZG3AVatAnXT-87Uu_I7yGbazhO-gJB_dtLzCRDx4ov06F_yCe0WHh515ndxEybGv5gJGMte-Q2TOgDTnCzcXSW4FKfN1fkiXHhX-2Qgs9xit-qZhkvqxPlOvHk3Dw4d_bK52FMtUFA5LJ73icILzt-GXlLNsNb1o8lu-F-AjgV7fFD0-ZS9OfREOe3dogUiSHlCktJ9CT-XNkLdGTyZVpdJ6ObTKvbaXa6Fmj65euoA10q3ZKgMQf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=TBFbS4Gvv-cbo8T-5U2OeLeC6l_IYtynjMsfBhd7WUhD-oVhp71m8I69JUAfdIL2qhF7Q3V3ai9j7fyu7OblhFf1faYwkT7ZG3AVatAnXT-87Uu_I7yGbazhO-gJB_dtLzCRDx4ov06F_yCe0WHh515ndxEybGv5gJGMte-Q2TOgDTnCzcXSW4FKfN1fkiXHhX-2Qgs9xit-qZhkvqxPlOvHk3Dw4d_bK52FMtUFA5LJ73icILzt-GXlLNsNb1o8lu-F-AjgV7fFD0-ZS9OfREOe3dogUiSHlCktJ9CT-XNkLdGTyZVpdJ6ObTKvbaXa6Fmj65euoA10q3ZKgMQf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=W5JOHwnxSC5QF32qr6KzOKaDIJ3uAzSs4Ieh2vFtM_T81cMRsWfb-ytHxSnermpkM0WW7XjpB44GUw9H_T7TLiKizTyJVOI-UBWXSpbjOFPMjfjJZ1YAZD1v3hjRKGA6LCwGzR3Q0vVAuW_gF4RAjnXmYNOTdyj7TG9NDMmKXIMcP-VWJD_rdKHZeVrac0z1BMh4mnV1YIBmcsHvemm987lvFaIhiT44IqifFDQwvtMTPKXuqui_NFmtCC-WneayA1vU7n-wDM4yMGAn07Ws2ELOFuAKb-0sl9MRdmT-kgOkXmyTg1lalD8CuFocf9Q6k1ANEYREpTTuwy4c2xsq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=W5JOHwnxSC5QF32qr6KzOKaDIJ3uAzSs4Ieh2vFtM_T81cMRsWfb-ytHxSnermpkM0WW7XjpB44GUw9H_T7TLiKizTyJVOI-UBWXSpbjOFPMjfjJZ1YAZD1v3hjRKGA6LCwGzR3Q0vVAuW_gF4RAjnXmYNOTdyj7TG9NDMmKXIMcP-VWJD_rdKHZeVrac0z1BMh4mnV1YIBmcsHvemm987lvFaIhiT44IqifFDQwvtMTPKXuqui_NFmtCC-WneayA1vU7n-wDM4yMGAn07Ws2ELOFuAKb-0sl9MRdmT-kgOkXmyTg1lalD8CuFocf9Q6k1ANEYREpTTuwy4c2xsq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR9Llnp5vLern1mUzxS6v4xxpT91MYKcZty6XqFZPf3XKWQUT7nKBMcm9s_-_Gw_KbpwCejbkbHeb0CZd-9leRdZnt2pFKZox9g8pzI88WL9UuNsLVwchY8Fp276eYf5W3SPgHYzj5uN8qgtSmYBXPYEZjPGVsB2OiKlUe4YIZ6U_g7Zs3-CG9qfXGXt7ASPWi_cds_p793Bkwqr8UJF69HNWEJVmdsLaNYBzNnTgVpKzDHEpOHViBYi_yJWsGaylG-dLeunV_KC_6UOnJTzpGu8RdfIYQuM1N5Nv7eI72wUIoDd_KHBEOGLET1j6XHcL9XU04eyRVLrZyFwxbX9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=e15iyOFuE3U-4aUWo7oo0gdGhBj-J52UStxaz0qop2ZQavtVS2Wa84KvA5eiowru_gOOJ_mfW8T66ihsRDKUmh1R66OriRqtMNDYTfYp8Lm1fhQr55qRTax4cQyJgYKHyuQhMXCylAx5YISbuaVlhSAYpW0rLbSlj37K04rXjcbaS-_iJHnG5c3nqkSMgFR-BfFdks--TLDqdXqdnlyMDSqO7atrYhPeSkNneaUX4DS3pbDd6NecEweXgWm0kKM9-_pM2uC-FiBOTPkvnghLVHl16IW43KG2IEFaIxbfRs__1Xb9ikcnSbE1Zk6Y0s8eKjGIy9FtTNxi93jf9-VIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=e15iyOFuE3U-4aUWo7oo0gdGhBj-J52UStxaz0qop2ZQavtVS2Wa84KvA5eiowru_gOOJ_mfW8T66ihsRDKUmh1R66OriRqtMNDYTfYp8Lm1fhQr55qRTax4cQyJgYKHyuQhMXCylAx5YISbuaVlhSAYpW0rLbSlj37K04rXjcbaS-_iJHnG5c3nqkSMgFR-BfFdks--TLDqdXqdnlyMDSqO7atrYhPeSkNneaUX4DS3pbDd6NecEweXgWm0kKM9-_pM2uC-FiBOTPkvnghLVHl16IW43KG2IEFaIxbfRs__1Xb9ikcnSbE1Zk6Y0s8eKjGIy9FtTNxi93jf9-VIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-dLmhxCIedWHfzwbzcfMQqETCK1cnVND4NdYrWjVlMoJGQ0ld67MYfrkhirZaKODuKXAmhgGEJypKQq8bVe39uOwT-7jdtmy3npifaCa5tLN532T1z0sqdJdCCFVAVN1jGqHK9yvkkPOU59zhcCVoQETVSuIQFoo47icaM42ABa8wVZ5kGBxsn3eaEqB9rxEjOz3ZEUlyx8EedH0ZW7z3ZKbWBh3qPPAJ7qrzZkYg8H_oKj5JYPPwNNFPlfDbfeJKz7V-izkXTQ1a3gxuI5i41XjovWRVDv_CBLi2EUYOyFYF1hplr9SGC3SDhk_SED3t1y8DoXC9kVyYmu9ZpQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=oRLSCQ6U2qog6Is4LIIZ0vAe3AzwyUl0KMlB4WbJZxL_N_xaqnR0FwCIDPLSfB2ESXxT-YqzEqdha4Mkw-NurpkDcsw6I9op_BgQsaeBl7mv0s1U6U7nUJVxp4CxMaDmGQj0eMrBIPmhC0NuuwToLWqPOcDbmTLZHJnOCvR4s8HDa9alIdg6y9TtOzGvTMEwtwfdeqACnTOyT7X7ff7wn-snSO_Yod5QaAvS9gQrb14NDc64LaSH4Pp4u_H_qgJjB-KYKbm29pFT6d2OxrAbw1eZd3NpOBdbG8QepGxOfTt4cjRmCAs145g6x-2m72KMNUEg7GfZwBljxJO3YEsM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=oRLSCQ6U2qog6Is4LIIZ0vAe3AzwyUl0KMlB4WbJZxL_N_xaqnR0FwCIDPLSfB2ESXxT-YqzEqdha4Mkw-NurpkDcsw6I9op_BgQsaeBl7mv0s1U6U7nUJVxp4CxMaDmGQj0eMrBIPmhC0NuuwToLWqPOcDbmTLZHJnOCvR4s8HDa9alIdg6y9TtOzGvTMEwtwfdeqACnTOyT7X7ff7wn-snSO_Yod5QaAvS9gQrb14NDc64LaSH4Pp4u_H_qgJjB-KYKbm29pFT6d2OxrAbw1eZd3NpOBdbG8QepGxOfTt4cjRmCAs145g6x-2m72KMNUEg7GfZwBljxJO3YEsM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJgLvu1paTQvorkHcBJ1IM_oCsPO40NpRoEA7Qe448WueDtw4Y-iQIf0Ar5oVyRoVAZlEe8xGxyOckfRZtmDOqxaS-5gt6rWq8CaC05101QjmNrQJArsY7QyJTnfO6UJngR50_z0DtUFxe5ruRWmhv6xfJt8Rv8FiJdUglKPRuMr-nGx3sbKYe57ReYS3Cl_XlBH8Mv44_il_aIyKIhZSb7Q6zEzzpYFyNqJ_8c8D-n6pBYfqu4f702qOHO431FM5UC7UxD2myvC1HmzeDy8iX10wfvskgny3vjkpzIczsSgVhr0149p_HLBdWrEmDj0lN3RTPrZRxyKlXdqG5MUgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=rfQp4h8iRVrxq0WfO4gjdfIpEBw4rUWzuwCxEN6JvO9Kek4VjOmILgFXtgsYBuT26dulXOJBretYLyagTyaAMbl5uPdsfqG_6jBpdhDXGO0RhZd5on_21fx7XK08rE6oGx-IvkcYmjh6VZG-JObZPz10l3h0v23s9tSfdl5nJsOQc2eqe69LiNTETK42vg3xlmLz0QrvjYaVeUMrrJ_t_CRyVjJJWfW1hp0g2TgV3MiyKt9wnyA1b0BC72yDAbxP0wMs5e8D1wUovwlZOhlY2ToHGRL6GxswIwNj07dmUbFlTmTgK0ldRgY7PSpXSxJODab2xyd85NB0N_6vngli8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=rfQp4h8iRVrxq0WfO4gjdfIpEBw4rUWzuwCxEN6JvO9Kek4VjOmILgFXtgsYBuT26dulXOJBretYLyagTyaAMbl5uPdsfqG_6jBpdhDXGO0RhZd5on_21fx7XK08rE6oGx-IvkcYmjh6VZG-JObZPz10l3h0v23s9tSfdl5nJsOQc2eqe69LiNTETK42vg3xlmLz0QrvjYaVeUMrrJ_t_CRyVjJJWfW1hp0g2TgV3MiyKt9wnyA1b0BC72yDAbxP0wMs5e8D1wUovwlZOhlY2ToHGRL6GxswIwNj07dmUbFlTmTgK0ldRgY7PSpXSxJODab2xyd85NB0N_6vngli8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMkVPNXowy21Tgw6eKvrGXETOY88cA_VtY1v4c04yaRmy1ymZwkn2FokQ5OOZp6aGTUUDh-At2jLWoD4A6g6cAcHJliFNrIFINFD8ADY13ycmDbx8o2TeuWjAFkJKkzaUEGsNYHyWe8Pg2ewrQGJGoPLcUKLdXd1hRmpERdrkk8aRJtEJ_rEHd5Ni_Env87zqoSz8OCW4Q47zuiFTe6lq2fUhCleaoslgkev0q9Ee2F6WHumy-jI5lmpRtyeDpEgZuA6nNM3mOoKBMpGP3awvlBNqDLupluP2KvY5kua0UhbFrPy9BqSe0836vASZQg8fthQwjGAvMy01adZmB_peQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSCfvQGVIJeMs6kRFjxfHvzxcvEDtB0YVUZq5kdVRqMjuYxgdRtaLqcR-vcXJBAV9CzE2r8J5-rxz31BvamyAC2FeX8TUh7EauBsurThhcnB-nw0SgXiYbXSRAW__qYHqlPiCh3Rfr-aJW-GP3FQnbxSwQeIKGynG9mtS1JMhlx-tWMV-zNUd896wBHuGZLmvtpG3qouVjdJQWbPpjpWK_-PmM6NpwUopvn2KbX3U37NsCchurRzARjSBPQOKwGXxPVRCYgBUqTFPRm_t7dDvDswjgt3QDXtrRsNrG6hfBz45VJltcGx3piVktgpKcsufcCIe3DObTLNszJc_lzH6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=re8nDPX89YnzesQL8b7Kvvk60MIryk4FOoYgF7iTGIfYRG84XNY2yXwDi22v_ePfZ-Jkx8iHc2FWNsJXaDrKlg9GBnBoTT6uTdYBU2Rg42JVxZTcXyqZ0N_Sel5at2-dlaWMBn5_6zDj020z78n-jy_yxlwEYVNUhpoGmy_ECTt88i_iDao-xSICSI6XKJwZqkZjz22jmbxyMMKklK7j7Xh_DtkpWaK7ShlUPjSJrLDPL6VQ1-8uHQSbEzBxyN-BYDA_tWPB60DiXLHE_7LuQCXse9sYHHy4XuA3zhvEldIPky9dPllJN4iZ9jkKtXq5zil0SjCN55zVLTZKpAp6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=re8nDPX89YnzesQL8b7Kvvk60MIryk4FOoYgF7iTGIfYRG84XNY2yXwDi22v_ePfZ-Jkx8iHc2FWNsJXaDrKlg9GBnBoTT6uTdYBU2Rg42JVxZTcXyqZ0N_Sel5at2-dlaWMBn5_6zDj020z78n-jy_yxlwEYVNUhpoGmy_ECTt88i_iDao-xSICSI6XKJwZqkZjz22jmbxyMMKklK7j7Xh_DtkpWaK7ShlUPjSJrLDPL6VQ1-8uHQSbEzBxyN-BYDA_tWPB60DiXLHE_7LuQCXse9sYHHy4XuA3zhvEldIPky9dPllJN4iZ9jkKtXq5zil0SjCN55zVLTZKpAp6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozDgoDKlLKXcsUg-auOAbndoc6VusjntKlVS3NjZXzsfOrNXgMcaLC2K9foERuAFJM_Zdtw_52WfTXs2nBP1xv9moflBo3z10tIr8yuHvPnMSgwuaGI2tyJtsp5hP1gfIhjVC8c5lPn4HOT3QurRZos54hUmlsVwfOLOOqVMZ1CoyEj20FrfZXdv0fhBy_Lq750bGKpJoxg_kSS3Yuw3f145zkj6y8yrp6aoGGNS1rWqTnoRr8vherk4r-JJOGevHKTJjM0QI56iwprFRmSXIQvytPWU3yqW9OZW-I-yDqERD7jjfbSFVFHH6G5fMP7K2OXvq0qT1lymYOrRDfVq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKQ87bPdiEqYid6Ol-pSl9xDyy8VuHlSji1GNDw6l_C8eETIK3B4S-YEXF3oWhwJp0g2l6kU45sSkdcDc9N2cWZXlqKYq9q-2BRAb1OD8_Fyflzv_1Us5SOtfCD7_bDD20v-ClC3U1YKt6o2J6Jm4-leX0sKYYZH1M0mBvYqEGT-jFdFK3wvVLZ5ChfCZH4y1Dx5G4iPNbU6k_6QWcebx0F1WKZKfbWBHJlZ0ZehFBH2zSgpSQ7k7J_ojSr0DCLkflRMgb_-RmOufcHv-TYIvoIAdy4nXdiyoZOs-A3MMHiPCt5yyvomyZN5rgAIexCtDeKUnwWgbwgdSipnYRalTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6PG0Wgp6CSS0IUfDHxdLTcfBhkKk7RxXCojygGxha7o506T_KCp92yIXivpk1KjrhmWXDL8hdDBC3ObovgPGUTyS1EZU6uDV7niPG2BneICrkqwxZSeagnoMafMju3wDB78wPEJT7vsLivJYZMV5fXFdGVKeAuQsdtWBNr_hTNKl-CGnGFSTxi-dukRZ8-OkNHMCBBBpwAIu1Eh5YsC1AJWCkyTH32J63y7W9W0TVBQZJO4APGlXC2PD4t0CXWbhNPH7VlTxKXWZu4ufhKdSCRrqLpDuIjPJaG6hqf2jyIhtNzvxZz5-DUcIHH7NjoE7_7Sqr0PWELvcKj__znSVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
