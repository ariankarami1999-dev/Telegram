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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROvvxIlLROM9zioYlPUcHHWkr9vOVUC9ibT6TuNRWN2dxvw_6I94oMttV9qVemy4cdo3QmTf964tf2uox8eeQC8iP0jZ1S32PQhPbYrGsZr8u-qbLOXh0xSDBrzCfWP7B5jHiGbHxnXoSGmv80AMtCs1fHSjYZlMtVPd-3Yyh3jTNPYPj-0nWTExWCyExssW-5lr5x-eQptiPVhTuOm5gIeb4KNlG36CywLrg7v29t8-yRRKpBAwGfXFGvfQJWGGPsKsDsMdiqBg4jBlrSy3ipoMBZLvcIENUjEWLTGZQTQry2K3v8fcrgZlhjeag-dX28YSZOJcGNM9ZgZ8UaDeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T412G89qDyjd9EahL8V4vFbp-Maox0s9yDJAjHsDvDMZFW9C4o3aAU7H34BTzO5Z7Qww7c-X4VFZ1yaV6JgOBrtMQxnqJtU3ovVs6EiAaNTVTLchX8cWXrR3KlZQcG8Ae-1huk5Y9Up11MtAav2Gom8YCN-Vs1zcUfSd7ZmN7uMEJaTooccfb9xOyU2r7wnwvrii3wIP0nizd0NNP8M6_jiqLhYuXiWysr48-0NAntN2ulKNv9GoFNmlij0H2d-elng949tP0VUlp_sl8CRw9WkZUt2GEeXbKZBtWlkoZ7wQexPPTF9pdhPRacrqHSYUjnanvSxUveq4DfsxDZJcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTlxXodelZAAUKeGl_CSolqihwb9i2RTgfHoj5F0PULg6_R1ps2Z55DfHD3yEQ6dQaqc0lEzOUmFLC_gejZzbBX7U4vITdlBcuWiLkhyA3AVQb7N_0PwToznCNI6AFDwsGHg53SHI8bekdkBXHoheGV_CU6H16uIPmJvJpvw8wjzwWwaqkBQgnGEKdHB9Rm-_KeYxmk1blfd14DROqikmnQOpwM1DRHXqAYR4NnowRwCsDkZZsMVS48SvsjAy7Xrued8ABhjjPFXm2lttdmCz1-gtqGqDa0QgeWVArkK_Z5ZQOkB7sT4ytXUjnHDdAxXtlqHqlZt5lzixl69-2pyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Q_kJ5h6UB1gO-XegAnsxDq5ywetozPrUpg7nX75WHb2iAVD5YYLEgPT9m_kL_BNNtIVJmWLeSgKFDMApRba8tXYQfpXjaPxzbQs6qhpODfxC8Tbb-zPp15vZqc4jVorwPPZD9eMhwM1uMoqB0C3YkiJKHq43YyCZ7UKJ4RYmD19Gb0DQffoi0lXNyB1Gy7D1fGUIICOrP-dEF8PvdtzMFsn60xX1SvalmSPvQXrEbZbBZsTF89DvRS1oWr_rmxH2zQhhr2edvBvqhykAhrG5gQcmih-xNPGhi9QK4KlKoWz13tknUNjU4_18Os_EGhDEorGqxllZvZ00a6evE5468g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Q_kJ5h6UB1gO-XegAnsxDq5ywetozPrUpg7nX75WHb2iAVD5YYLEgPT9m_kL_BNNtIVJmWLeSgKFDMApRba8tXYQfpXjaPxzbQs6qhpODfxC8Tbb-zPp15vZqc4jVorwPPZD9eMhwM1uMoqB0C3YkiJKHq43YyCZ7UKJ4RYmD19Gb0DQffoi0lXNyB1Gy7D1fGUIICOrP-dEF8PvdtzMFsn60xX1SvalmSPvQXrEbZbBZsTF89DvRS1oWr_rmxH2zQhhr2edvBvqhykAhrG5gQcmih-xNPGhi9QK4KlKoWz13tknUNjU4_18Os_EGhDEorGqxllZvZ00a6evE5468g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=RBWchU-UDj3CoYz2V4sng-lwA4vPGqHEnnHNWd8vmH3eVdiUBXG61-dg8xQ3-XwLCB4AnTayUw6SA-vrxky_il-FHIbWXg_ONap2g1zYjszZrO6Xq5CTzXI5AXr_qCKfdjz3JA-GFGMm4bpQVU3jyD-y_Xjre6dg_zeNY_uRWmTgmEa3_YT75oWP8LwWYDYFuKGnLqXWJm3lUn53MsUhRHyBfkhGWYuHoboGJlwi9qXsvWvZuU9tYV_MgKDRbShfLPY3tOx3jdhE5yNRzllY03fNRNnr0vWny3jKBCqdgmh8HiNXm279XDQmvQ6dZGi2R3ntTgdaTduA424aa1vmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=RBWchU-UDj3CoYz2V4sng-lwA4vPGqHEnnHNWd8vmH3eVdiUBXG61-dg8xQ3-XwLCB4AnTayUw6SA-vrxky_il-FHIbWXg_ONap2g1zYjszZrO6Xq5CTzXI5AXr_qCKfdjz3JA-GFGMm4bpQVU3jyD-y_Xjre6dg_zeNY_uRWmTgmEa3_YT75oWP8LwWYDYFuKGnLqXWJm3lUn53MsUhRHyBfkhGWYuHoboGJlwi9qXsvWvZuU9tYV_MgKDRbShfLPY3tOx3jdhE5yNRzllY03fNRNnr0vWny3jKBCqdgmh8HiNXm279XDQmvQ6dZGi2R3ntTgdaTduA424aa1vmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FziwDxH2v_cL-HYZuCLlI8LJRlaIt67QFOiNJEKIDbOnq_LFdR3Qmd64rKcp1qCF6ze0o_i61sRXWl0LCYHIrYQVA3yI-3VUoPqoYI-pdv3g0IziH_MllqXxYzEHPQ-eFheAwg9GHeXkq-B70-HUSxur-4JKfGAvYB6ueD_y-JmK5Z0z6qI74udzWlzHBRW2lxNj1HvQ8oy4_5V9605Z_o3r1qZ0T883ylZWfY_KeIxBo8_7NPcce8W4JgrJ-6atAzd7LpjTo87IwdTkaTm9R4GtAMVohtCovZwgMNK5LWwqZHhHxGSOv1XGH681ug0vpOlyGOstRvsYd0J_ZB8TQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQlPXfgc_kY-7VGob_lUmrd4Do6QCUaZXsEocA4vvt24SHjtLRyuhhFfaGvXdzihIAhKffAnhR9cVKF_3SXkli5hTTP1qqfs1E02WmBhG70GOzGHULZZ8uQwWrqQrwnQdX8PY0k1CpkupYCXHePok1pDXHUoQZBvggiciYHK0FvigfP1WIsFNsXfzb5PmkDLw4BoQikbJgWtU7eAFvRcM6887ENaDFjrv2VXUfIVryKAfjbm3LqWwjljZzA5yKGJVE0Lyr6ODqY-hj75NopSj3-a1GXuy2pasvg9fat_EZXcZtJ8DtjknGDUDZo1UH1pVCrX4xIa0yfbUUYTC5_r5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=AJF3smvHPMKVH-y_lBf6adLjuQs9p9724Hjk6BL2I8j2JTo_47GLJNAa7HhFmYC03Egc3aKbPjzBfvBnHuG5RpUl-J3WNlqFiDUtyemb5YI-e3TZ-QL61ddFDZ4QWTzo7JKCoHwtqsPoAvrek5iMOWN5JHsyu077v8nC15Q3aQmsNjVgISXuVeKk_-vir8DAVxvtYKJnanZWZumMqr3_Uq7RLZ9Pb-Tq10EUhsMlOKaUVhDkGQum7k4VuxXVbDm-0oh4g8SfWrH8ci9jbOuvxbELpI806ribkg7NJcuSf8Mvb2VP-lhodwx7JqgRcL_kyehZlqO5gk9kqykG2TmvtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=AJF3smvHPMKVH-y_lBf6adLjuQs9p9724Hjk6BL2I8j2JTo_47GLJNAa7HhFmYC03Egc3aKbPjzBfvBnHuG5RpUl-J3WNlqFiDUtyemb5YI-e3TZ-QL61ddFDZ4QWTzo7JKCoHwtqsPoAvrek5iMOWN5JHsyu077v8nC15Q3aQmsNjVgISXuVeKk_-vir8DAVxvtYKJnanZWZumMqr3_Uq7RLZ9Pb-Tq10EUhsMlOKaUVhDkGQum7k4VuxXVbDm-0oh4g8SfWrH8ci9jbOuvxbELpI806ribkg7NJcuSf8Mvb2VP-lhodwx7JqgRcL_kyehZlqO5gk9kqykG2TmvtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=EKitY2_KW4L6936O63NRRQPvn3MthNmivomoo4Vj6C0SQ3VeX3wl9YZfnwUegdX4ldYVW0qlGPt_2IObStJWdHR4RgDawpWS6FuaQOlFqbMgejXQofXEJmTzuiO75helobafB2qdDcFpZUrkh9WFfmD7rXHR5Ck9dIOj_SjEwGiqdD-67mtHA74jAM9KqhdGRzj1zusaW6gSpiTtTRk9GLAniMtUh0AatkB1XhKXKosbpFFWDFUAyPZc239Uj844UJtJuhy11Io4wHahmQ59rFHYGSYNTKbZJ4CrpQZb7dBViWiHnq3DkdvExOO5_Pjc0PsOoDQaEuGBPltxVKAhGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=EKitY2_KW4L6936O63NRRQPvn3MthNmivomoo4Vj6C0SQ3VeX3wl9YZfnwUegdX4ldYVW0qlGPt_2IObStJWdHR4RgDawpWS6FuaQOlFqbMgejXQofXEJmTzuiO75helobafB2qdDcFpZUrkh9WFfmD7rXHR5Ck9dIOj_SjEwGiqdD-67mtHA74jAM9KqhdGRzj1zusaW6gSpiTtTRk9GLAniMtUh0AatkB1XhKXKosbpFFWDFUAyPZc239Uj844UJtJuhy11Io4wHahmQ59rFHYGSYNTKbZJ4CrpQZb7dBViWiHnq3DkdvExOO5_Pjc0PsOoDQaEuGBPltxVKAhGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5BJO5aUazfGoXP5OiM8KK0I-0t20qG0iMvvPV5lkMU_EYmtjw_o-3rCv6i0utu-1v6pILTTL6vzb_0wr0gIxlfioFIi9rQ2MWHQ5FPIXfFU7TkWphVC_X4PnE_T_JYGVJyPw7o6p5hCaSRSf1vBhlHq22HlXvfoZlmdTqZv1mvHSC1Y7WcpHaulUR6gHqdts5xI_HRtzWpIafpat37FbwuaEGscypmIOeFaefJRwal7DNrqsfmMeMGc8kzIRp3gE-ViZZwtxmsPD1EOgDyvj5YniLLzI-oscDbaq5oagGaOnr2vqqRmwiBq97R0QFq8CeUQLUXyDGjKsWOhgtla5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpN_Ncy8tZzikPJOUMxGwHSXAcwaQ99KPOOawW6xthOfeQlYhHoHkYcqPMxB5I2L7T2dnKX0dY4y9J3_vjkjnMpw-3i9BshT54hScNgqWmPvLE57TIErtgAZkmo7F_ObE6zxNkkkCh-ztfREKnyeVJ1mt2j4SdzMf87DKRiRCcTIQeJ0HS-WbmFLEMW8MK59caozJR3tXSoPae-YkMSR9QSNlOrd4kpA1rzeNvO8DNNI9ViwXVoP5bR4wIctqd37SEk6SQcZPLcKTjh6RjrAhQ_cEs-xzcGYG5JCdOTFZzprEVNIB6NpgvxiHmyrweWswpb9x-LftV8DH57gHjRbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUWGXZBQ8IhakZrNXsrn3DOGo0sEhFVfk6O6ugKNmQlz5Xq_BEAWUGqDEm_2qsFUxwRDHhKeBvV6ZdIMRweHaSlLVp7YRhyiIlWUkjP2CTQOMp3oR-0XFcwlFlRGq-82XMntcJV44yIgY3_3_jdTQFj828U_wTNpjIsXfthm-Qp98WZhJ1huHFUFmQQCCQH2nbEcv9XrCGVarSvW6bDbAjwnHGMiKMLwbjWSG9scIP2kdiU3zSNbQ4tbsVHZbB1YQGq63EZBN-FNj5jrNtwFPzryw53gn1JywfeqBDjmoMRJ3dGyZpbHmOZS8zZlAnOjWIWN74sNLteGOop4TE9v2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=XZ8mrHSxvpPgDJdCq-fAa36bNvTsPRA1BffhCh70GdqRC2akqTAzEhExfvH6RU3tpcBuJmsKH9ZIocN3LwiCFXoyroJRTflKHnrywJTQzb6H7wfiVzTnMjnb_VzILpeNBzSOGR0hDAvuVz9rITY1iNiWUfi9GenjFONfN5SM3mk9JafWqI11QabiVFXQeyiT7zLPT1RMTe11bWp52P7SXjpddfu6tG7DI7Sh37BPIit7ReOZejTt5D-cVuIqRWOHl7DqLR5qvdwed9_Io36qtXblEMLFnLRtennoZGMYPqEWZNDYZp_zOqWN8PccgT0Dt7VYwQ1EvSDBboMnO_O0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=XZ8mrHSxvpPgDJdCq-fAa36bNvTsPRA1BffhCh70GdqRC2akqTAzEhExfvH6RU3tpcBuJmsKH9ZIocN3LwiCFXoyroJRTflKHnrywJTQzb6H7wfiVzTnMjnb_VzILpeNBzSOGR0hDAvuVz9rITY1iNiWUfi9GenjFONfN5SM3mk9JafWqI11QabiVFXQeyiT7zLPT1RMTe11bWp52P7SXjpddfu6tG7DI7Sh37BPIit7ReOZejTt5D-cVuIqRWOHl7DqLR5qvdwed9_Io36qtXblEMLFnLRtennoZGMYPqEWZNDYZp_zOqWN8PccgT0Dt7VYwQ1EvSDBboMnO_O0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIhKalBwPjOAZaUZOzYXWaqMxUgqnjwZAsDpNLe1xeU9ipWKQVr81k1aAo9zvhTdbwto2zobt_lTYJWhcQoWP2TVjP99kGOFLx6WaA2ZqZ8_EVkEp11gJfAGn78VwwjcBy_6R0oykut-fGPAedoP5DZxNPLI7-F0RLtCGN1vUCkHG4_bsFGt5vD75C8BhWCEh5Gz86zgNn4ervt4PDMAG4lxcrKXLmQ2ESFIV5NNLzguTt5tY52726tdTxhNsi4ec55bZjt14FqA2C3nm3aydhHHvPSZrRvM5VFf4Frgnq2nRfhDcsBAdKpu80o9eH_Z5SpIub1_yohA3z8j_Ggo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfnwCWdww_8d6AvtxGLJTiDPNRFr-T6-tVmeo-Gi340ofdYakGeh8bfJ8ieSnAZq5BH1Bck4OPgPSXGxLnlOxd7UG-TJf5asN7s0LLDDT29nd1sIuc7fEKLTn9ysXpx9EAu1M7nu6HiM7L3vnRYrESn64_h9e4TLlXfL0DufsLLzJ8M6MJHth3lJVaMVMtRtwUA3Tqbft8EXCRZEsaIT6OkyGoXG9gHLb0oaujrqjTN_AHcQ-TAXV5lWpm0ld-D3qGRVCyFDv8P8YxU0fCaox--N7uZXrjS5qN_z8Vwwjh9lz8QwlCbX9zlb4-d3-N_0fxlLCN7kR5txKXswcmzv_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nulIr7c7WJmiBop0BAaZqFInFSlyJyzbTVif7getKkDYjCgt9L3X7iTnYGxWhONwN3tIMAvSEulykBW4-PS627zDCsZi3HfGdHEVB8EklglI-Gh9sB1XAyHLENCsOLJimc8B63v3NVxFXaPiap9VuK4DD-f676tHLzoZyjUGbGxUr63WBT_fGRz9vfAgfHB0gG_mqymxlLoCCynEEoQszqLnhOfX0BfX4ETjZFJtsi-XxgsiZYMiCurIaASbRpFmNNnziAO0--JBZA0vc-chDjY3KC1jp-MiU2IV4WnmrSz4Oz-3T7qRjf-E2VPk3gn8pKiic0TYqfpl7P6SPlMKSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=J5LhltnIcAdQmeQikq-rLU5End9shBtbU38Wj-pu2wGQMOuy2M6ZbFj_Zk_ggPBIlXh4Jzc31LNYMhyoCf05TCrJPepku2QP8n1zwbJptQBq06FtX098U5iyBpEg3XO0C9cfhQLbNhYcZeHbxDSFZ_0tG-ueuF0kzqz-BkyiHP22biqTG4DsiXoGQ6fGWDEEdEbUi6uT0lVlaAnbaViv63kUi-7xG7YVSWvNjBrknReonotVCmHuTtgApyP737_abSS7D9vleer9wcnPg5HGSJ4iIguicDKPYCdOvOgXGPJbH0T3ROOsiCNLImInRod6wRj5uIqkEOMpPEto-VpMCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=J5LhltnIcAdQmeQikq-rLU5End9shBtbU38Wj-pu2wGQMOuy2M6ZbFj_Zk_ggPBIlXh4Jzc31LNYMhyoCf05TCrJPepku2QP8n1zwbJptQBq06FtX098U5iyBpEg3XO0C9cfhQLbNhYcZeHbxDSFZ_0tG-ueuF0kzqz-BkyiHP22biqTG4DsiXoGQ6fGWDEEdEbUi6uT0lVlaAnbaViv63kUi-7xG7YVSWvNjBrknReonotVCmHuTtgApyP737_abSS7D9vleer9wcnPg5HGSJ4iIguicDKPYCdOvOgXGPJbH0T3ROOsiCNLImInRod6wRj5uIqkEOMpPEto-VpMCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgMeJWt36DeZKLPCPJqh0xSJh9x_TzfD-ltj81pd-a7verJAatMI0H1KL6BO7QFLm99LNRiH0ADXeTUPMxXaVXEfggYsZVjDkdH90Aule-b0oW3B1w24p3Zd2UnNlYJ7SbL2_L-qlMvBaDqHDQrFqQGLuKCFnYaXjG6MIdhVWzhyTDcZp1TriH7m2ee00qXjPGw4yhXqHvB6WNWP6RO6r-IbVEWQL0Z3gJHHQyzOQulZMxECX5xDVdTPERGcx3ARb637wnNcSgJDVltsYOEN988tnNLw5CcAEHqWV5F_FjwLy0wI34DjHXlOHGfoZcjLkKc7hn-BxfA-doHvsiJb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRa5wlZ9EyAD2Y-cofxPbvXMoozeWTWGoUXV4MaqY1dLbn08iQQAe_cXEyb6S0l56QFe7789CLZDtjQeqVt0ETsP3qYiN4bHfEzK7gyrALbNl1n1EHVIRc8MoYm5WbH19r7wTVhqup8SsmjzJs8Zi6AwayrG73JeXjKMLU2Gsihs74A4vGTwLc0cqac4gxMF-wvmo2_An3V1bkW8NNdQgpk0s7fn0wue5WsX1_DX0Sw5LyVroboaLbgim4a_ZCbKf40A-b0nKDCbWPqQ7CgN9hQqQWG3LI4lirnzY_-ytJhoMo9c-r8RBRal8_18fFWk3ETzLZueVi1BEwCoZxzZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYe1z80dTxbGz4YQUSWIUjChhZPPmkd_WsnGMJ4Az5rYv2JTG0_fo5TrydlYkZM4a9v7T4jnHna10qg52gbE4AC5TKtKnARUBhI4eYglEsrFkwtKDVuKSutTLmYPj3HllfFSlwmshlt_YvPwAMWZg6AUoWEXp9ZXu9riysJbc5uO19SROzhDAPJV0gDV15mJ2AE5ypxW_XMVZwJZ8fR1nE7v10jk2NrVCpzutakO_Iln9GCaiXpFitTMFU2_PQpB4j_6oBzE4IacPQuo4mO2Hq_7B5yBXFRyQ2aAV4rJlKHk-87NoH7yFALQA-BC0HP2WQraGvtkG8TEXW3fJZYrxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=kH-IAEtWFrnM2_QSB-F9V7AbQVjtbWccB1QS4SKNf-PWsmMkvrWmIGBB29Z-aYWgXTYvhI68IXeh57qkHo-IYjfU57P5vwSLJNluUrVRsSWuSTF8EaZTagfL9aPXToHNJhf9JrdfE9888GboPUJqzFEPzZ3tCC94qWyrzOy1dqQhZ4quT4zva9etXuFhuWeDkxTCl3wogzlnLtsqo3aQO25mZW8uIsk2QsHL1MOklKvlBK54oLyWqeXtLSeUXbif8uImFgX9jYMvTSiAAzHkMDJ46Dtgv04xmQ2ey2YeLLhXpAsXc0tauVza87cLK7TPld5huE-n5AkON0dtK-iczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=kH-IAEtWFrnM2_QSB-F9V7AbQVjtbWccB1QS4SKNf-PWsmMkvrWmIGBB29Z-aYWgXTYvhI68IXeh57qkHo-IYjfU57P5vwSLJNluUrVRsSWuSTF8EaZTagfL9aPXToHNJhf9JrdfE9888GboPUJqzFEPzZ3tCC94qWyrzOy1dqQhZ4quT4zva9etXuFhuWeDkxTCl3wogzlnLtsqo3aQO25mZW8uIsk2QsHL1MOklKvlBK54oLyWqeXtLSeUXbif8uImFgX9jYMvTSiAAzHkMDJ46Dtgv04xmQ2ey2YeLLhXpAsXc0tauVza87cLK7TPld5huE-n5AkON0dtK-iczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=QXYw9cZQ05C8DnSiOO2bG69Y8ZnoxRrylV2gKuXBkLZpo3_eTGVQhL6A5QFEb4WRuFvRjwUaxYNmBBDQkk9LwOIalAXK9IoGj1mHzHRdAODSXn9xhd5RH6E9QKQiljFFpXPXZfobo5zvdStCbfVvM6fznQcCF7Hj4roQpSLDHZ2hXCoHz3rdm2x4iwN8fn6fGt4K2ft6axUZiwocWlZ73OroUpxOhQxytyyLQfaC7RcJz9_FEDQzPA5vZC1W4bgsWaNFTOZdsbHfcDhKrXcteOp8Zmzyh5U2asBqXPqWats1m9eB8KFRWMjfNSEFNrMnFFTAUCQMT587pEv7whAl8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=QXYw9cZQ05C8DnSiOO2bG69Y8ZnoxRrylV2gKuXBkLZpo3_eTGVQhL6A5QFEb4WRuFvRjwUaxYNmBBDQkk9LwOIalAXK9IoGj1mHzHRdAODSXn9xhd5RH6E9QKQiljFFpXPXZfobo5zvdStCbfVvM6fznQcCF7Hj4roQpSLDHZ2hXCoHz3rdm2x4iwN8fn6fGt4K2ft6axUZiwocWlZ73OroUpxOhQxytyyLQfaC7RcJz9_FEDQzPA5vZC1W4bgsWaNFTOZdsbHfcDhKrXcteOp8Zmzyh5U2asBqXPqWats1m9eB8KFRWMjfNSEFNrMnFFTAUCQMT587pEv7whAl8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=tl5PDNB7Gc9Gin_hE4ff3zHJObKXgmU7hZKMJqvmC5b0R1T2xPL7rNjjo0T5HtgCUXNSx_2y_bOIt-VQYUvmgnVLPGqRVeQTukfJ9neE6P70nO5weBwX3trpxxQbAAqYEZ3wFz4KPyx0mIag2Yy1Up4iEJ319IY_fzdpzqzU1U_kpaw1jFsKqylCC0utaL75e_zqzaois_A6T5OJiXhiJtcTPVwj2i9UfqjR3022NjdpiUZpUOG2dePxRtyvA_s_CQ9pFPrEDD9s1A73tYH9BpAYotckoViIdSrPCK1hjzitGHVtLDK4YWfF_blf71tUS8k290P1bhyv_HjFObME5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=tl5PDNB7Gc9Gin_hE4ff3zHJObKXgmU7hZKMJqvmC5b0R1T2xPL7rNjjo0T5HtgCUXNSx_2y_bOIt-VQYUvmgnVLPGqRVeQTukfJ9neE6P70nO5weBwX3trpxxQbAAqYEZ3wFz4KPyx0mIag2Yy1Up4iEJ319IY_fzdpzqzU1U_kpaw1jFsKqylCC0utaL75e_zqzaois_A6T5OJiXhiJtcTPVwj2i9UfqjR3022NjdpiUZpUOG2dePxRtyvA_s_CQ9pFPrEDD9s1A73tYH9BpAYotckoViIdSrPCK1hjzitGHVtLDK4YWfF_blf71tUS8k290P1bhyv_HjFObME5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdCZPBWpCZqHEcpGNlusoLiaW7vcP62lSb6wmjnPTnDbm0qfaA7weQXp7lOxBk2o1jKVccKP80mTTO_JBOAoi5q87Uz9a92weDGdV5EcRu7Wfn8GBbZD1tzu0PD1xzz4eIXnxz2gZeTUg3416q6ySqrTzHoqNa-6caY7p8X_3uN5EsZC0dz78z5VcuzhYnXLFj2stLzuAQTaUhQ33LTvm8suMsDYLbOq61bu-DfFfyGd6Mb61oLHszZqD_E0E0d0K2K2PsOnrZD5-Ily0zvoI4LxyeSUGofvwjz4SUkXrcr0CILWnvgaMyGKwYMTkpj_TGH4ysnqKEECwW4R7hLQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJt9UFP3Zp0Fj9Z90EKNWR2c_JHx6ujNbwb_KSKie--jejKgI4xKxGTJZBkiod7QSDglwIS5Dwj8wxe2Ra2whc3INOH_xG5p0CFyuRZdpFcpvtjUjDuP7Fpf5bna_vGQwJCXAXCkFaD09RCf6iB7oH62_UfOIfzfZYDl2bmaqclynaqj6JMH3jgKNiP8Ik2Pue7FrpJzxtqmacqn0DSAHrbicPGrdPCpZ6qBhmi7fK8HgteCc-o4DwIpDZhoaOLJMaPrebcSuhJBQOmRxtVEQTxjh9VqnKrnGcVbUNSgvTmLrDxGWFdGxX_9b90Be9nSqc6IK4k1jFORq9bS1H-ZOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUpautT6t1iQVFluOTXRfgFGT_NmnoDlbolupBRWs5aG3OJDyQLYFf0TwpsL0iTssQVi4uwcWQWKI3Atwzb3FByRScKblRUksjokIN8J5JjavD-6asuL0u60u7krq9STB4kCCwXPeT5eS82Zw7ykO6lZrgshY86-7Ts0F3jZwn1g5OyYkk9gWf6yqSSgU67AiiFUHhXlUc1uz3ec0dqnVLoYX4UFEJ3EGTpzxAn46QuQEcnxK4h19Nbnl4BBe_FYwVpbJQnxgeN1dIQPwfRyQkIiC6OWp5fxTurS7KKVd-SWA-ZMw8K0brQ-nnv26r1D6BV1zSvdhZrooXERvVdzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLhnmh7inVgT3y1p_711m1oElj8P-D8YwaDH6bM0URGflrVlmLrxcPQBaB4ZKlPY7E2CcO_GEa4L8ZRo0Giz--HpUWMKH90vHXHgGmOrvB4pDvMSxzV7movcp7J8LJv1KLdgPm_B-FHFLLhaeDQxzVIS5Jhb9OSjrHcvmPCartBz59z0YbN09gAGRdIv6Faiua_UaZp4-7i9vRcI0mqXZRWu_aYk6P_vZYoXlL5F6R-TWQQOdzxTgw5L1oNCLtL25pWER8ZMbWE_cNlYcmWz74bHmzXwVBqWzl13c99giu4Dvr82CKgmT9asmiwcqjeTEA2-zZ2awVxdhIWAopr_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrD49BcWwFxVSSMrp-sA9i4lVundUzn9PZhkeC3UisLjEzLiHffX5qbIEPkf-QXGi6KxeP0CtfaTAGKuQIuRuNUg8BeK6buyGQrIh-SChwM9ieQmcT20jm899r2QcYmlcSVJ-ZvXic_RsIMBxQ2lE9gktjiXye9xsH_J1OIvHBZX61iVdcAp3Hu6z16xFEaUJEJy5mSWKh6gvEQdFtCo8skzjzYs0pqVn9Rgv7lXA4yUjiFrhNzVvVNkzt_ge9ykDsZwekd5d76R-iCIvA37dqIE49vVV1dVBXn4eSYdByIPpUHJ1183yFooqeG5ec6WQ1OFBT6Mk1W9KXSg-yoklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tE77_6qE29oK9Tb3O8GjfHXLhyblyuAQ_sUHB8Crsv4Ml2oO9FntIgOtDIv9TZd53nB8YfNhaR1k43OjIxBl9vabe-Ko0lKdDkWBxTdfgh3D05FGC2N90-9OKJwI3D6sSblfdme1fh-pXGu_IZAZMhT5nfQm9_fluDdwgxtxQtYUFCX7jGxJMtj1pZjT4eztN4jjI29dP-avPfXE0E2ffy3j3hwTQDkLxbmvMvgQQ5sQfqWeo-NgA1ps3EWCHk0VlvSR7XHrfzFNwFFEAmmZTBEdW9CtB3BhA50sCzTsHDuqn52qoBMS4q7SavYjVbIEqDNaU3l8c62EKjxeH8nEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSXaFe0G75zdgsdEoQtDHZm6hRiacGp90qVsSnhnSKaOWKMd94VmJUuJ5htcNmU9WY2ErZgakOPQ3Dt-cTjce735DailZ06XVkyPXgXIKYroaGOxPP7WL6WImW7d7EyEexcIet3qEAxmSQjKUZ7SVm7FTGCcnk96whE3xwZmpa9qVggTJ0smGkKNPQR5x7h3fhNFLZS1ihWXtFmDy3PYCLuapOEeABT20jREn5orYmE3c4PjoZnZNAhPXTh-YhdATaXHAA6duva2meB0kyEPL0_t5iV9JSUyo_4_vn9-hIDvwyOcEgDtSawNkRYdpBA8Ou_Z2r_fpHaIkh5Aj4vrrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6BFUXmnsYPowIkemQrhUUXDSQAs8zcTN3vMhdXvgYo_UGrNVZdSPSzXrI8grRhsOYfnPinJWtYnxTwMbGzmV9PCbfHhWldTL2HOQMljfrCff0br4VTdayrLwCAtBQpGTCHIFz9lW3tBwEErmBnMcPIVo7HKfdJIMuRejJ-Tt3ws8WFsUyeBLfh1ciVWgbRGXYF_plOd5LA3SWGQkIIaD7pWtbbobugFbIjV5aeUmUNHD-Sj1-J2ejDwmgcdk4n2AvznlsQhyweiDt0ThAFp-IUgspudzp10N10vcq-VOGe31ymMhRA7ekAtAlblo4vYyqKVXGN_TT9hfYDL2gFtgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CijZavJgXbwKLrWYl6BfcNviAvKHjtMcV3qSx2QTz-GZqDJAVPNEOkpP0CZk0Pp46OjIHOLcstm76WKymD-P0QVOCn9xgncxDnv6GjDuctTRvkQ6Z0WK7qTrWGBJCdZVMwcWNfPFw_MFQTrGNDzlQe6jE8we9Gdvroj4Ae2MoncGibOeZwo-TMcmf23rxARF4iCRqHYGV9ZWJv1v8jL_v86w_IbG32dWeDCF4PeP7Id_q68-D83gsZLXKUCqepZEhxfxjUHV3Dh-9wvJjb1lY98gtQb3fQZ6OWm_zdsVS0BFTy5FgPg05qLWlrN15UyYpwXgS6qd5Duvsyn1dVR7_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbTIzL8525RkBgTsAjZA19K9pgJTiCQuJy_24MiUSEfNf1iJfskPQ_m9Q0ytlJg4Uc0t8C8i1nqQJOMIMCbZeGLMi3B8vSqjVNq9U_tNQecXYimv9Ragc4qn8NO4z-FxQ-1LMG8SP-uEsZSjLDpt9nYCe8WUPRUEnLIsojUBH9Q8V76eCoFUUkcX_HF2Npze72rGuNb4q1IHVWiAGP-ByP8wt0dQbQvVNTPCNU1OOfT2XE2RbgOt1Mmg6AhIPFdWWH0xhrSv07OjGipxCQQzvJhAb2jZA98vrLiqE3QJ9RtcJz-gMmZYy3jZVLXhOzmr6d7FLnoqRwcJ7pV2DbxIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZc1z0XmPhfyvj8d-2oMkeavvlQAXQuaHs34XqowNGMDBAd4mk3TaF-QaYMXWqWIkBXlA7qxuTyM7EQ6lOsSkvuJru19gXzy1TvOhXPAS4wG0D3QyK7URz9r93Ow91DDLYngRB0Nq1YiWmMoJDLwAOnpQvh6A17UF3slXfmdPmJAgzfurQ4SAknWI7HkFTZ4-QssYKdmsmxjKK36Mg-vIdMHCmKPXgkqdjJVMEFtjdkbtOnZIeE9eIqtyDQNu2iEWZSO-Xq2G5mIcCvpXWi6mbDBcxLoSXK6qPkiKpnGuqqqSTif0Ws1poqeNE0edXSwivXPEX-57OJYAD-wLO28yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_vQoosL_nV0berMC5CDg17VW2F4s1VFZd4I_F27-alH4bN5nIGrIzUyJ4CtrAYZseAJxIU4LDB00eKbaLCZMEiRdOmaXj_mwIdljVt3vKun3ga6L7xQ0O_ynfafv7EwQ4TucshuWGE5musI0hFCBDZTl-NhaS8KYv3MBDQyMK6BI7Tzby_vjCeZLG4LdEFe-zBTJKbRHr2UGfhgXFst_rWWeUrQuHVXZ-huQ6A47TXz1DrnLXolJCTAe4GIzfbF3Eqcyvvzl6u7m-5e_i8_OOMyWjKvgbXtD9-Ehx52640byOmtSgnTJvBcL-2qT2pk0zkjCXFO_HtxW9scTqqlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdnMdgaOVpwrQlyUC1Tsz2V7XwaA_8YU2wzRqqlqSHhLDPOf-XvLsNxECvZCRS7WLtxvwqN1dLLWALfMcQxiJ9w1Ze3x51jVvHZXFbOhaXHVdspJ-RNPw4LwtD893JV6d79clW0ClLL7gaA30wBl0GWqJY1HGJVTttlj5zujKgJ9qrXV3fSY9GvPOaP2bFV0qmKtBVRWynFfm5h8npUx7STqta4L8aq9Y2HNKeSFyYjRDfZQMI2eL9NUktJ9LeOhIcorgWKdE7khRp5M4aVDTD6y9UY1igWL-3pUfcm_L9iNyMvl7KkQrpqPdckierzz-IiR6cJyIgBr8LEhiwmoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eoy5OQAqxX42_rMb2sXI-IKYEBtJ6Shsue6TkvXuOHzP78Vy2q5_ig1MvyIainAid8LYSEEJOMBEbO6QdZmfRSRZhmMmpGQcqO3LeH4stqb9vN12cAuZfchw4c32D0jiPvDlSm7ITZu_Mr0eBkraRuRvhzt6xyfscfqqgNnOpcHIxcPf2eZsv8f5BC7cDvGYguWLjka3F5Mt6bRvaNwrXSyyh0yA6faq02DJ_Qcg6kdemXQ9OZ8lxK-0JQNXd7xIXQIN4NhbGqLF57F3bSUSzHmAQx4UPFA1XAaAU89ZFcuox9gCY2YhU-_ME3fVczdeU0jw5aWcbJYQabVYR7qKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGh5SLuK-bitJuOoNmB_FtoEiLfwIMxQeXCdIOSaq8OGCZgRKqBtCKfWylB3WgZOCZFemzbOWLtocT53RvoNESxthZDjLbAnXFDFbqrx_ZjmKwTqtxoAu3o9V0Is7xNTwDm_M2L_KdcvGRO_5BbLtuRV0l2_ZGe-4jKBMHSRSD9t85mhEARG-B36z40rnfosVdojH5_PTI1rS8A7WjgytXNOucAajBBHKDe0vkset2IxISNCQZ3oFzpzEzRd6OYYxlUBvjHNGPW5UY2aW1f6kiuCs98xfnDOyFUTIyIBZ6DHUMNN6_6J2Use5EQTEUoYhlsImJmSwKseWhs2Yw-xXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=kvO2M9Xl0pIl_gQJYlw3iMp-_FQNA5PFSTo-EZ0z_4JD7V0yPolQp9l87-YcD8cdGdbaMIfomcNimbDCeu5fwabs72We3GnpHq-N9PSWUJl2H-uCW0uxDITOYp35FEwrPeiUPqPYoO7-OZbcAtGPZEHYapA-VU10dmVDkzwfDZ8K-JuIVsqhdG2vZNFVntcCxM5yhq0KotqmMkTe2UGxBYBnHw8JeqtlWbQbO9-W_QXlDglejhfExZbplUXe1-YoFMJpN6wqzpCEJx06kj5EVXVtPCGlQu-s4kk_4tbZhwawiT0X7LsCpIzHE9Z-Mz06Avkt0YP6vACF6E_YNq-14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=kvO2M9Xl0pIl_gQJYlw3iMp-_FQNA5PFSTo-EZ0z_4JD7V0yPolQp9l87-YcD8cdGdbaMIfomcNimbDCeu5fwabs72We3GnpHq-N9PSWUJl2H-uCW0uxDITOYp35FEwrPeiUPqPYoO7-OZbcAtGPZEHYapA-VU10dmVDkzwfDZ8K-JuIVsqhdG2vZNFVntcCxM5yhq0KotqmMkTe2UGxBYBnHw8JeqtlWbQbO9-W_QXlDglejhfExZbplUXe1-YoFMJpN6wqzpCEJx06kj5EVXVtPCGlQu-s4kk_4tbZhwawiT0X7LsCpIzHE9Z-Mz06Avkt0YP6vACF6E_YNq-14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA-h9_zpgNi16TA8WUjUAGykK526PmuJ4gSQOumEqX5ybm2Yf3iPsDLHzn1L-zpV8df_TironPEtVtZ4Rlm14UJkP9J-DCepq-4pgQDblo0aZJIeq3-49Emvk885e4HjgdLe-9Xcgr6QD21yUuxZ4_X0M0gK7fuMUBIg2-g3BCO6MiVHzu5iqtMbIOFqgokwc9w3vDrVGzfrvmvU0rUR0HpAlHoxFcRVjmgs_qGpFOjUDyJQlwHd-b3HZQOPn2u-ehjl6e5anzcGq18DvofJOTWUSlufXZ36qdVcQnLTqYtobr-Djood14URz3g7W0l23Ioavk7fFSx3ey3ptdSUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=IfNYlJdlvO24V4L9zVX-5BbTvaQjaD9Xuj7HkWV9D4lSJFI83DEx3zTG-R00CxWRXesxHL16nQYx-oPmGhXeNo1kPYd2xu57HIR1fE24zxU3KLGid4c4Mn4mRgfgdIHrc4A244XOKPqkPnfr45dFYwXQDjPWb_izCKPLyN4r05k75qRZcFhc45a28PrYdiCfZJcASaOGFesXs_n6OovSeIEITtGVGg9Wcw20wNtfwP_Kw5xGcRrjfKpzvtWGQaoCh8DTuD8rObvkibd0a0P00V6Yl0aSslOB-JWbYjD299KDe5FUYbycLDne_1jAerozlCdKdVY9uaN0kMhGInUzlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=IfNYlJdlvO24V4L9zVX-5BbTvaQjaD9Xuj7HkWV9D4lSJFI83DEx3zTG-R00CxWRXesxHL16nQYx-oPmGhXeNo1kPYd2xu57HIR1fE24zxU3KLGid4c4Mn4mRgfgdIHrc4A244XOKPqkPnfr45dFYwXQDjPWb_izCKPLyN4r05k75qRZcFhc45a28PrYdiCfZJcASaOGFesXs_n6OovSeIEITtGVGg9Wcw20wNtfwP_Kw5xGcRrjfKpzvtWGQaoCh8DTuD8rObvkibd0a0P00V6Yl0aSslOB-JWbYjD299KDe5FUYbycLDne_1jAerozlCdKdVY9uaN0kMhGInUzlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=iZdRTK9j_hzCcB2qAHCg0Uq9gKu4Fap7eou9B3Eajf7QESEJBLq5mybR2ZogRZQpoePPU_T0LiuiOx4KMJ6awXV0sgt3dJ4WvISlzoma06sHjyXz47zo6wEg3NqKf4lrC85ZTuU2Btz3YATgTT7cW8WkFydJzzfcm_On09OymUzt7C4958_qXvnyZswb3LpIcylSRLwbQ8WGVzdSJQkakXg23e_pNOuAMPPLPXuuCCva_DxXNXaCjh5eP4r2sIEIFJ3cYtRcjU3cPB1MWZDKenhqyUkEhZi3WCFCA-eUYRFBXiDix2hIDGQgBPhJSXpQJbT1-ENOBFHxdwcFkHwoHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=iZdRTK9j_hzCcB2qAHCg0Uq9gKu4Fap7eou9B3Eajf7QESEJBLq5mybR2ZogRZQpoePPU_T0LiuiOx4KMJ6awXV0sgt3dJ4WvISlzoma06sHjyXz47zo6wEg3NqKf4lrC85ZTuU2Btz3YATgTT7cW8WkFydJzzfcm_On09OymUzt7C4958_qXvnyZswb3LpIcylSRLwbQ8WGVzdSJQkakXg23e_pNOuAMPPLPXuuCCva_DxXNXaCjh5eP4r2sIEIFJ3cYtRcjU3cPB1MWZDKenhqyUkEhZi3WCFCA-eUYRFBXiDix2hIDGQgBPhJSXpQJbT1-ENOBFHxdwcFkHwoHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvkgAq8oW9t1KJeSg1I9g0Ve5xBcdGwyHt04qoWZmUKZRuqCWWC4FisnRGNtIQXdND1uojjs-R04v7079JACx8kjKo-99hLH-hnKcgRhDM1GUfOvHY4-zmrYyAnLcdJwQFsG3QlBRibVbau0kp5Q0GcsRUM7g8XZ79TeeJvvp0zD8RBwpK_v23Lk78jAibDmx-n0xHUk-Fx3gV6MK066NHn0kKNKTkg1a4x87etzwUx1sObdYI9YRZkeypk0UetH8OGyAmk5lMXx7oOHAetttCcQVJZR4-ptW3hXCHO8nUQghjQQ83Yk6KJg_LM3z2Gi-f9bNWswylzRvkXYTSSLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PG2PDgaa4rGltnpVY-NtxbysVSrvZZoGZbDgS0-wyGHjCoZr4RteMDTl8DJsIxiIoqffBpVdzgW7OCyEj0eY3NM95nfJjb5NFeP99P3tMEZwH7wZjuEQhMHnPevnpWGtc8eAurKkmGJyB6GwNGTOa7cnCd_Y0uXz8n27T0LPDr3akx0FHvfe2OIdPI3RF0_O5AXPRda7_czJMjLoq16jc8bSTk18lK_HUiPchhId8-zyl7EBjfOOfG9VioQjkd_EO1cWgAnhb4svIxYU_mAdvB5O9_foDVOWPhlU2Y7rlRXykHcLwjykeAhgLsbw5OFGpG_FEEETnttMOFwNCAT1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PG2PDgaa4rGltnpVY-NtxbysVSrvZZoGZbDgS0-wyGHjCoZr4RteMDTl8DJsIxiIoqffBpVdzgW7OCyEj0eY3NM95nfJjb5NFeP99P3tMEZwH7wZjuEQhMHnPevnpWGtc8eAurKkmGJyB6GwNGTOa7cnCd_Y0uXz8n27T0LPDr3akx0FHvfe2OIdPI3RF0_O5AXPRda7_czJMjLoq16jc8bSTk18lK_HUiPchhId8-zyl7EBjfOOfG9VioQjkd_EO1cWgAnhb4svIxYU_mAdvB5O9_foDVOWPhlU2Y7rlRXykHcLwjykeAhgLsbw5OFGpG_FEEETnttMOFwNCAT1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4gbnUi9smmsaz-QwqWSsHBWFgbaUBjiwLO-Od8mxWTmZojg9KbB8D1V7k9C-CXXZoZmdF2iCxyOP85g2PRArmKXeD_PwOiVV7_g50O0hO1cW9aueOCEK106GnQQQ6g7m8ppw7zks_jxeTkps0B9JyFwZpRDicpWh278jrfhJsnsOKyVBiZh1rGhDEtzcsUWvB8lSWzGKwKtOUGoodk6MzL65uehQGzlxUmHh2AckRc35Lek7sfGiVyb4F_Ad8j35o5pn1RzDjz3HapuLUswW0GXaLm6y-3VgdFAENa7d11YaDk_Y7bHLXy0l9r_ilNzS51yx2JgMfrdZl6rbP6YtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoZXRzwjF9deTcnnzelEu6-yy0pDw8Qt7mB2gqVP16M0XQDMzNi42ZF1tgcrmeJAUxvBpf5Y9xr18rQG6OQKTcHS2oOiLeLoc_k24HSKCGnaQl7mYR3M11YmhzHEfmjLtChm5a1h6wmZ4gd_gLM5Iw-rdnW6mWo9yzHO6hnybS1Rk_yjAQGFjrxWSqSlhtudvkdY2ra8oUEg1iMg8KQDjjcORrciXtXhUszb8KpvUmGmBzJPmLbR238vkVd9LE5n1yAb_Ddi8ogiZPhOQyS226zvThasBjLnggQY6UMCwdN-5JRwgvpwi_jRVtoPSBS-moJJs3F38N7AYQqJF3ftSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2xzTLhbcPCFN3yHOknk5ndAxh-vTsSrUt7dnnrj-9nkbylNTLRnYRNi6LUvyrpwxHZXPCVflY_RMvHrLbn1Cpoh2YI2tQJX2skJeVr2-B8ZeTHxeTidSO7giyMbDDLavMaLUbYz-I0Hqq7IEHBgkNL_J8cseQ6CmPwJYatzWCdL1LPgAgiQG_6d6zhdOaN9RXa3gjGqlwnpaPvEwJxfqA79bzL7GHfIGIGeMT8XyXH73T2w60zHSobOerU1JB3mtMoq4VkHfa7qFX7Gk1-wCu4ymoGfQ5YJTxXvZd55hVtNixLYBd7IoVEy62Vl0buyxUmQ8qF0BHijmTAsiYZe0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpLx3oqKri6sDhI8wthS2JttAAGVIdBEWhp1aovf-Ai-jYgRzVdRJ7EeQMA4TYGTxnb1bBK6an7RM7P-4ilR1OGmh7mn8qNfM3JIPGi7R3CUJSdXgHBxmz1qoL-8KQEwdNpVQ4rB5AeAnxS1HDkxgJ73R2AJ2S_mjyro7zA_Iv_OdW7bfSgT3kBwrd2Sl9Y454WleDiOwcLnT7jCOPAg0Vi3h-NHZB_kCH3rKhwKn_19kETeksN4jVOqmxNF6zBME3fLw9v2YL67850egDB4NYIR9s1_HRSrfkZ_3ND4eh1KPFoHEWr0Wya6lqrgrceGD_ndArpyhWT2Z1nDC0zwSg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=O7LQitde8TN528KmiSeJ84Y6hnXh_cgaRGYfUMBtOtpUxUpGAhHRSmttu9eNAAGd-yohTIz_ZDQ1T1-yujYYmivcXGEg1b1cgNClwmMu1WscIGDKK72LEFjuqPEUWfWLW1JnJpqLy5F56yOvB5EEz5uE34hUfbda2cGk4zYyt_M6OUYm-YAx9frzZER-J8JHxOYflvzbmedwT_ST7zTEF6hnu3KknKM4Bv_x2FKadhq6gMd4OHCMokisQ_qGlkkIlETdpyeZguUxldLQ32JfxNixYvbQvH5hPubeq8R8C7zT-qpziuDrvYMCyDumRd6b8Kgzj7p4UMX8VSZLhxKNbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=O7LQitde8TN528KmiSeJ84Y6hnXh_cgaRGYfUMBtOtpUxUpGAhHRSmttu9eNAAGd-yohTIz_ZDQ1T1-yujYYmivcXGEg1b1cgNClwmMu1WscIGDKK72LEFjuqPEUWfWLW1JnJpqLy5F56yOvB5EEz5uE34hUfbda2cGk4zYyt_M6OUYm-YAx9frzZER-J8JHxOYflvzbmedwT_ST7zTEF6hnu3KknKM4Bv_x2FKadhq6gMd4OHCMokisQ_qGlkkIlETdpyeZguUxldLQ32JfxNixYvbQvH5hPubeq8R8C7zT-qpziuDrvYMCyDumRd6b8Kgzj7p4UMX8VSZLhxKNbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=mEZShNqAoAihK_xnj1CY7lcefhsD2r88_ZD1-BbQ7PeNLliNiWIpmL8qOb4C9vNurPSjV-Ue_QEXWRzg_O-mpVTtVR3ckb91FosqQ6tfw8LBDoatT8pAwuPHkmvSTVNVHb13CeHH1yg0yCSMfEVFunpvKTIIfAjRYx1Jt9X1kMELfdvKhnx5zHpygafVHkpUxaedvKbTPI7Mj1t-L_23AkchdntvbLJ0f2Y7_dMMVFkZqLKI-CaYeZn7oe0kWfAGbtd2oZx828HDYI37G68ZnyIQhtP87A9rXER8tnnH2TkJaYVC9eMUyJ1SDBvNHgjuVwvTHRJGm6hqLzKWyV1nyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=mEZShNqAoAihK_xnj1CY7lcefhsD2r88_ZD1-BbQ7PeNLliNiWIpmL8qOb4C9vNurPSjV-Ue_QEXWRzg_O-mpVTtVR3ckb91FosqQ6tfw8LBDoatT8pAwuPHkmvSTVNVHb13CeHH1yg0yCSMfEVFunpvKTIIfAjRYx1Jt9X1kMELfdvKhnx5zHpygafVHkpUxaedvKbTPI7Mj1t-L_23AkchdntvbLJ0f2Y7_dMMVFkZqLKI-CaYeZn7oe0kWfAGbtd2oZx828HDYI37G68ZnyIQhtP87A9rXER8tnnH2TkJaYVC9eMUyJ1SDBvNHgjuVwvTHRJGm6hqLzKWyV1nyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=ngzZuZQqi-l30dD6vP7psMMhJ-NOjhnm_obzK72v9uIGaqw3pNk73qBqN6ou8vmesl8nmg1O2mON4Qwa7sNpheDCytTkfcZ6ALtW-Ty023Qya0LD68dUoIgnWXavKRYj6m28MQgw9fweuen6PlZaAdOdtM0lwyKaN50dgvWJ98OGzFgsIMkzAJO0tEx0Znd3s80up57fq55XZhLY-JTKfjTO_eXhPjeIIwAKsGTTi_R1SBEueIRuJkLVTqNFr2CRsAtfVWz87KKmkMA_b-wAtPnTazX3Q5v6WM9HX3z3LzGEVFBChhSWQoJ-gk7M8FmBxrdlX41idEjQVhS0if0EDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=ngzZuZQqi-l30dD6vP7psMMhJ-NOjhnm_obzK72v9uIGaqw3pNk73qBqN6ou8vmesl8nmg1O2mON4Qwa7sNpheDCytTkfcZ6ALtW-Ty023Qya0LD68dUoIgnWXavKRYj6m28MQgw9fweuen6PlZaAdOdtM0lwyKaN50dgvWJ98OGzFgsIMkzAJO0tEx0Znd3s80up57fq55XZhLY-JTKfjTO_eXhPjeIIwAKsGTTi_R1SBEueIRuJkLVTqNFr2CRsAtfVWz87KKmkMA_b-wAtPnTazX3Q5v6WM9HX3z3LzGEVFBChhSWQoJ-gk7M8FmBxrdlX41idEjQVhS0if0EDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qwwbC5bbcKTwnBbzR3-60fhfIJdG70Kv6p2-1v6Eoj9c6-XCqzF1CpQOc1FrXE08i5adTWm4utvsQQz9rhWbr6pTbd58FlCFMRVpxGM2w3CyKwdrWtD_Up3MdqLxOr0I8gVSg9J5lNlUNl5Y7reKBt3qhOxsZV6NgBuMNgZqbxpg4he7S7B6_HNOuwEN43jCR-NuAX3QkEkGSKQ2pbVbop8UlgI2-KTZOmbeMofG5XQ7CZiKV3Qg26hKcdjkVRfMaEYTehOlFhhYdIB-EjcJOzUzbBxXt7NBxxvb959A3b6D2ChnUsgHm8EC-AcFKzcn1T554gna7Ge994c6LmcZUQNEPYXnLk2Hr6nBmQpvTVGZXqUMtwryBBWq6bF8IWCxC4BFVYYALQsc4t819aDn7FDJ72vvOH8NFhw5C1Nv-rrPA51rGvOFTiGYPFK41Wz5e_V58QTZ3htxIpt3ydgRNuzX1MoD_txqHY32k4n7JkDdSq7l9DtzLoXbi6GN5jjRGzFx6fAT_AnUzEIYWb5qiUiJ3nlUNdenrvD8U9GBU3Xc31M5t3-Mo2gIqoJg1FzC2zglibwWbpFdvJJbaWKg1UEdWnHBbWzr0PARoDl8doyZfGGX3cXupzjBQWr09G29PHl2uemD0zNG61GGmUUbqLydGigmLMwfxkzg-jG3q6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=qwwbC5bbcKTwnBbzR3-60fhfIJdG70Kv6p2-1v6Eoj9c6-XCqzF1CpQOc1FrXE08i5adTWm4utvsQQz9rhWbr6pTbd58FlCFMRVpxGM2w3CyKwdrWtD_Up3MdqLxOr0I8gVSg9J5lNlUNl5Y7reKBt3qhOxsZV6NgBuMNgZqbxpg4he7S7B6_HNOuwEN43jCR-NuAX3QkEkGSKQ2pbVbop8UlgI2-KTZOmbeMofG5XQ7CZiKV3Qg26hKcdjkVRfMaEYTehOlFhhYdIB-EjcJOzUzbBxXt7NBxxvb959A3b6D2ChnUsgHm8EC-AcFKzcn1T554gna7Ge994c6LmcZUQNEPYXnLk2Hr6nBmQpvTVGZXqUMtwryBBWq6bF8IWCxC4BFVYYALQsc4t819aDn7FDJ72vvOH8NFhw5C1Nv-rrPA51rGvOFTiGYPFK41Wz5e_V58QTZ3htxIpt3ydgRNuzX1MoD_txqHY32k4n7JkDdSq7l9DtzLoXbi6GN5jjRGzFx6fAT_AnUzEIYWb5qiUiJ3nlUNdenrvD8U9GBU3Xc31M5t3-Mo2gIqoJg1FzC2zglibwWbpFdvJJbaWKg1UEdWnHBbWzr0PARoDl8doyZfGGX3cXupzjBQWr09G29PHl2uemD0zNG61GGmUUbqLydGigmLMwfxkzg-jG3q6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=Dvx2r6oOnHIz8HeQ_Pf6mWQeaXpYy7xYz_nkPfcU3zexNM7DxqSlhWnyrzAHyvcdnTprkX743araMPG0gFNIF_WkJdqlDfWFU-oEyxFNjc3tDPPS8T5li2JuM_UEu3H-QyrkZwPK9KHMjjfvI9EqpLnfEST7KLXhE4-QsV1UpKG-x1tF-fsNtsvebKBE6i1ZQfl_Bd9hOriPzo8FE-iYuknax02D4xGRe0brVwU9I255OMS84jn5cVVGQfbn-X6akkTIkBh62Jk1RPGWDnXArHbaTNsEY8OmUxDWejnkTu3FTmoTbUYjcupcGDjcqRB5AgZ2YtzQuadGmHlRHcFkDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=Dvx2r6oOnHIz8HeQ_Pf6mWQeaXpYy7xYz_nkPfcU3zexNM7DxqSlhWnyrzAHyvcdnTprkX743araMPG0gFNIF_WkJdqlDfWFU-oEyxFNjc3tDPPS8T5li2JuM_UEu3H-QyrkZwPK9KHMjjfvI9EqpLnfEST7KLXhE4-QsV1UpKG-x1tF-fsNtsvebKBE6i1ZQfl_Bd9hOriPzo8FE-iYuknax02D4xGRe0brVwU9I255OMS84jn5cVVGQfbn-X6akkTIkBh62Jk1RPGWDnXArHbaTNsEY8OmUxDWejnkTu3FTmoTbUYjcupcGDjcqRB5AgZ2YtzQuadGmHlRHcFkDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=Epim8nRFaEfcvnorgYuCTil1rRbl2lvtM3iG8jsioYHI0ZOkTu-uADmmtjYXHo-tgSV4fEyyisDedMjOgnhSWmPFyvBNMafyI93WdQWoiqsZ2CUJndUlQ5_mA1I9z3VoyvFjR1rPavQEblWbDq86qUqIErI0ebTU3EV3CCtRiNI3SYbFX9d7ivRWYJ1PAYdsUB0IQO4PzmMzaxm5TGmMmIGPbFEOIEEYhb8AfRJa2ih63aiGzOGkpRA76P3is9QLFo8Bn3M-ixpm81TBnC5EgxE7J_xpqdk7MGMGOR9q9mGLd1UzuoQ_LUN-8ZsrRpMk9kcnyPvsglKTO80dh7ShqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=Epim8nRFaEfcvnorgYuCTil1rRbl2lvtM3iG8jsioYHI0ZOkTu-uADmmtjYXHo-tgSV4fEyyisDedMjOgnhSWmPFyvBNMafyI93WdQWoiqsZ2CUJndUlQ5_mA1I9z3VoyvFjR1rPavQEblWbDq86qUqIErI0ebTU3EV3CCtRiNI3SYbFX9d7ivRWYJ1PAYdsUB0IQO4PzmMzaxm5TGmMmIGPbFEOIEEYhb8AfRJa2ih63aiGzOGkpRA76P3is9QLFo8Bn3M-ixpm81TBnC5EgxE7J_xpqdk7MGMGOR9q9mGLd1UzuoQ_LUN-8ZsrRpMk9kcnyPvsglKTO80dh7ShqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO4GfT5o0qQIHYD-XXXHwUgkcKU0ZEdlIqd5r6Mf5TQgcKYARr1kl6LV-FbLk-J9lCR9Q06egb07TAMQaQzq_yAlMATeUUJbEx9niSUy9XH5rrkskCSztRaTmxVBFnkBc5eTyBrgTKqj5ZBibbKVQ1YJ94kj9bX_yhjlG7C9ZzVQRNZGMbOcD86bsNw2GzvSXgonFyGEKjE_mxoxUHYiAyh1Vp4iYombjjFsodzSDQrcX9afeDx7tLNqpmVA1XY3YCtsU_0kWk02f90mT-FdlYQ3NWerE0bsVmxsN-MuxIRWeSFMBuhANPP4KR6emTjLz4tvaRvp1gyvWQzzdDibYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=TXkm1ee82pCH1d8xBkxr967KqiRUxUSafGNVIt80Y33Vh1sPqEtaNdz7Mhlkc5lKU7lcDcpp-UlCoDz3ganTrC-OUXph5ppa1ApB_Kx3CJAVFMeQJ7zLj9AIVrUo_sPgCzhBnC3e3eAt5vNe2-7gLk_911gQCRSDn_48W6wVb64em4rlU8YFUMQO_AMN5NXF-JVBDp2km4tJxGK_lt_NQ3Z5s70aCBVvgL-XLljGARRSpLAZiFAvMYHhWwTWtviQLV58uq32u7qZJQiJQKmE8xZp7ngk4fKRwZKzRZC_0D-9XKkUA_1hJaH3RoihGKih4k25d55k-otxNoaxWulLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=TXkm1ee82pCH1d8xBkxr967KqiRUxUSafGNVIt80Y33Vh1sPqEtaNdz7Mhlkc5lKU7lcDcpp-UlCoDz3ganTrC-OUXph5ppa1ApB_Kx3CJAVFMeQJ7zLj9AIVrUo_sPgCzhBnC3e3eAt5vNe2-7gLk_911gQCRSDn_48W6wVb64em4rlU8YFUMQO_AMN5NXF-JVBDp2km4tJxGK_lt_NQ3Z5s70aCBVvgL-XLljGARRSpLAZiFAvMYHhWwTWtviQLV58uq32u7qZJQiJQKmE8xZp7ngk4fKRwZKzRZC_0D-9XKkUA_1hJaH3RoihGKih4k25d55k-otxNoaxWulLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPjIFIduqhlBb37ZyuCdEcruWzWlqqnq5MM64iZaq666vakuwEKFyWn1QlDUw0mvm6MlS0G_nebvfI1VdAQ59cO5pEAG0AfBeTvQ13fVxboxeT3RwWl6gcy-qo23VwkRTUxZHrnZEipY4CN5va4ch-lN7DQZBsiPsFAru6s9PbjpvXNMXXaU4jUYkBuxzzRENyOx5fjC-9s9xjbkpkRVLr9c0jddw4m7ceHdvJeDC28rzfq6kZka5YPqtHJkF0Ri_ovmp1eNX9njSSEkxervV8ZwiqClqTXyxSuZd-1YMNQg5a_jgKeTymFZsQIZowkd-6UQqxv8MDfBoayxAv_50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc5zEbrmJh2YEmJJQ-x1It8TKD-ULm50w6XJdb6uqW832Vz6iGle8OIYLBs0obsDnvNSRXr2XamvG0MHGnLezDsq0viHVpukVKSLAfGESX1SQlvOKIavhYSRtkB1Lmt6aXJMNo2R6Zr3jG2tgoWeydr89ECNK5Om1Jk-hQGfv9vu42VNLnuAoqCIDnyciv25oqjX6JjYIyYszam2lWkzEgPnYOjXhdJuN5gp63v-pRTnXek0CbAkfRoXDU5ulM0gzSP6rGJWFY5RKFq-CPiTYxcks30SkF9UXHWN0Yi9yY0l0BTIyxrSoKubO5_W0RkqeW33n1rxAvXDqti5FbxVZA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=KQAJ_ZZff1uKWBGfhe0Y-m9yUqi8U9B7JVPSDDAEJ9VbULUpX8M5UdZ02Kk0YWrPZkvkPFfSDXFBDJ-e-gvKtL0oNzumIPR_Pa8F5OWTE2VVitgy700SGn_J-h2guH03l-heQaDi8qbnc3WRLra9GieqEEu8ErIWD_57wGVSrg4ZHmrWqjK0HlagnHNhf3hVzqLIqieJ9VR8PWVcc_D-pIr9FCgFuLbGz16xuLsO-ler-oBBeOJceDYtJbGJYx-e6fmEz1m-MGokdYrYVJI_zYYSdLito3rRTPshSw0sAMVPklYpZeJ1PM-7uhzOxASB02OqNlJeMIkyRIkUHxChqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=KQAJ_ZZff1uKWBGfhe0Y-m9yUqi8U9B7JVPSDDAEJ9VbULUpX8M5UdZ02Kk0YWrPZkvkPFfSDXFBDJ-e-gvKtL0oNzumIPR_Pa8F5OWTE2VVitgy700SGn_J-h2guH03l-heQaDi8qbnc3WRLra9GieqEEu8ErIWD_57wGVSrg4ZHmrWqjK0HlagnHNhf3hVzqLIqieJ9VR8PWVcc_D-pIr9FCgFuLbGz16xuLsO-ler-oBBeOJceDYtJbGJYx-e6fmEz1m-MGokdYrYVJI_zYYSdLito3rRTPshSw0sAMVPklYpZeJ1PM-7uhzOxASB02OqNlJeMIkyRIkUHxChqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=gAHUc8YH15VEYxoRywoaWo-8YovWEzZdsL8BrCtTn7m5R-JvazXFByx2fvYFllbbz3wjZagQJA3sNH9gHEPSYhott_KlrYunrsb6iMDoxE48xZ3Ncmls2yqC4PWWSWA0WgdS3Yb8h6ZnEZZ0Taq1OvlduKhbN-vaHU6I4hilOP48UU7i9qbRsREPezkqhi7mZWk30QMsOXZ_NduM5PRuVYlO3j7-YbJnz1v5hOsQfCCa-EppYBiop8tijG1LLjsoJ9NUroWsniZSBfTtgCS2XiRtYh28eebSiNwL_BbPi9WqQOTMygycDeXpHBeTXXS4vcjiToHxJEloYo0QIGUMrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=gAHUc8YH15VEYxoRywoaWo-8YovWEzZdsL8BrCtTn7m5R-JvazXFByx2fvYFllbbz3wjZagQJA3sNH9gHEPSYhott_KlrYunrsb6iMDoxE48xZ3Ncmls2yqC4PWWSWA0WgdS3Yb8h6ZnEZZ0Taq1OvlduKhbN-vaHU6I4hilOP48UU7i9qbRsREPezkqhi7mZWk30QMsOXZ_NduM5PRuVYlO3j7-YbJnz1v5hOsQfCCa-EppYBiop8tijG1LLjsoJ9NUroWsniZSBfTtgCS2XiRtYh28eebSiNwL_BbPi9WqQOTMygycDeXpHBeTXXS4vcjiToHxJEloYo0QIGUMrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=X-aDAleJoz8Cyxjl9P_IrxKXI1jyNNWgQNdv27wjAltV1O8RwqWEs6YFjjw8JoX0AYt659qAKDMhmorpl01Qzu0oeC4D0wq3rHdxqBMMm_AkODm2T9NX3dr3MZ6V6QTfjHJD06qC-WMIuG0XDegcaP2gB-6XysUdjsNGiABN3BYZ7P4Nhiz9PBIG3p42Imgy9h_YSTcTKTbRT0yEyNFkS0xUjUNbGFeibxCgacNDWWyGk_d27iuapBFYygt1OtNfnPXoVn1FxAqGGUrFEW2Uv3kfuZazjzoxd2O9kA1YEcVjCnq6Setdx5uLogC1szTtxCCFFbsS-AyBl04WVKn3nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=X-aDAleJoz8Cyxjl9P_IrxKXI1jyNNWgQNdv27wjAltV1O8RwqWEs6YFjjw8JoX0AYt659qAKDMhmorpl01Qzu0oeC4D0wq3rHdxqBMMm_AkODm2T9NX3dr3MZ6V6QTfjHJD06qC-WMIuG0XDegcaP2gB-6XysUdjsNGiABN3BYZ7P4Nhiz9PBIG3p42Imgy9h_YSTcTKTbRT0yEyNFkS0xUjUNbGFeibxCgacNDWWyGk_d27iuapBFYygt1OtNfnPXoVn1FxAqGGUrFEW2Uv3kfuZazjzoxd2O9kA1YEcVjCnq6Setdx5uLogC1szTtxCCFFbsS-AyBl04WVKn3nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diov5-B-4SwTiFe-p_tKn8NFi1k2di9s5q0Qcx0bMt6BFkPbMM_Pf-hj8ompQrjWVbUsr7XQepyhAmtWFEH954G5TS7JV-RIikBKD_ORrnqxvLlFA1rppMzWd1zCi8I19Rq7SuHffgOY7I6sLX-KZTw6jw7jkvYbBTzqNG0wX8ypFxV1BZ6E-3PV6tWwiyGnXY48LDMwae3uZBEk2Sv_YBSZupk9-F4n-NRFGMDIcmNxSSp5pFjyGViqzLrmstvpidZ0wKz3t2McRloT6RxghtXcNlRedinTydXhGRlK3TTA_XPeoaHfEbto3X8DYVTvM7fVykD5k2la3eFb5WuyiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=plBHyT4ebqclMLAK-IkwzJyMK3rtOufoDp39mfnTM_uc0XExxO3arBkvMA25RPmVrVU52ef3GsFo-qIQKBKKRKSCOooEzmx6URFnIQWrvhSizZVg29PA-qgdO1aEv9Xx1aw-PA2OLBHxNdt7Lahlcapu-2nmSK9AZBYWi-VbRw-ep-lVMKrbfKJIF2xcx8BLnjxgysQCzho5A_8o2nRRDrWBJWL0JEf0CT2CeC4rvgJtjo5rii1w9isS0jTCQat75XaqdO2-d0tfOEZV4wGJMQTvImVD2R73muq1R4YpABOfM-FbQYe_nS7d_rdUoyvaaeXB_9R0AMWasaLhTmaQvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=plBHyT4ebqclMLAK-IkwzJyMK3rtOufoDp39mfnTM_uc0XExxO3arBkvMA25RPmVrVU52ef3GsFo-qIQKBKKRKSCOooEzmx6URFnIQWrvhSizZVg29PA-qgdO1aEv9Xx1aw-PA2OLBHxNdt7Lahlcapu-2nmSK9AZBYWi-VbRw-ep-lVMKrbfKJIF2xcx8BLnjxgysQCzho5A_8o2nRRDrWBJWL0JEf0CT2CeC4rvgJtjo5rii1w9isS0jTCQat75XaqdO2-d0tfOEZV4wGJMQTvImVD2R73muq1R4YpABOfM-FbQYe_nS7d_rdUoyvaaeXB_9R0AMWasaLhTmaQvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=p0-GYG1erFptHoSDSsphEuYUzmtObngz7fOeXRrYB7f4qpaiJX3zsP8zM1CAe8RWXSCyIaW7bh9gZPGBkuBZunyYOdWNtImt-ItRIZYZhgP-dCaOVGqK3egQx4TxAIynJS0pwyN_qSniN5FqBbY56tkpYUuKso9xsDLjVMvQWDIeIvDoLselT96ujUJhjC9blsFmqfCnChw7cvuURK7T7fULV8bq7qUi3DpOFfLKcL51hA1nvSj_1Fi7XuLZ1b084ngrvXvCdWBL-dy6bf0kjlTLge-Ytnqc1-59pOVkXYm3MK3CjcTejGfYiJSEeR1prBdQFWviilIDneQFLXJh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=p0-GYG1erFptHoSDSsphEuYUzmtObngz7fOeXRrYB7f4qpaiJX3zsP8zM1CAe8RWXSCyIaW7bh9gZPGBkuBZunyYOdWNtImt-ItRIZYZhgP-dCaOVGqK3egQx4TxAIynJS0pwyN_qSniN5FqBbY56tkpYUuKso9xsDLjVMvQWDIeIvDoLselT96ujUJhjC9blsFmqfCnChw7cvuURK7T7fULV8bq7qUi3DpOFfLKcL51hA1nvSj_1Fi7XuLZ1b084ngrvXvCdWBL-dy6bf0kjlTLge-Ytnqc1-59pOVkXYm3MK3CjcTejGfYiJSEeR1prBdQFWviilIDneQFLXJh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=qptG0SXMLdTY3oO_bl88sSGQewNTUkVD24b-SiJu4E5GRhy4cyj_a4D0wizXJZijCbSMAX6lS1tuWQKziYYjoIy98sEPrggzDd56w2TKRRpJcEhGIgkJrJQjbDCK3b0AljFyiUTP61FJ4lo-n-K0C5DiqQIlyYL9wmq8RMS4VcaqgfDa-KRxjyJcSm3AaPbvu5R2gUvP3uYytiSWsvKNfYKVhiUo5QTwq-PhTeAQPKXGAyO3jOZiVq20NR-F_obpsX57CL3iOUpchZ27Rz-nX1Tdrw8mvEI2cR5JpDBjDd-KfG1sZH8kJd0Dh8aOf-TPQVkOCiDsdbCnE6gusRpYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=qptG0SXMLdTY3oO_bl88sSGQewNTUkVD24b-SiJu4E5GRhy4cyj_a4D0wizXJZijCbSMAX6lS1tuWQKziYYjoIy98sEPrggzDd56w2TKRRpJcEhGIgkJrJQjbDCK3b0AljFyiUTP61FJ4lo-n-K0C5DiqQIlyYL9wmq8RMS4VcaqgfDa-KRxjyJcSm3AaPbvu5R2gUvP3uYytiSWsvKNfYKVhiUo5QTwq-PhTeAQPKXGAyO3jOZiVq20NR-F_obpsX57CL3iOUpchZ27Rz-nX1Tdrw8mvEI2cR5JpDBjDd-KfG1sZH8kJd0Dh8aOf-TPQVkOCiDsdbCnE6gusRpYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RajBLnzrR3RmgVhIIoOsT3mOVmvOKcv3RM0YmF3_VK087SQl-tTAr-F6xYDvEiDDKRMcYJ0ahgL1FgXhIpLH3cygJKLI1qYCNZfic1WSGaup-2cKiM5Xxg3q_538yWhOpNVqwrlBmsDt2uCYyHZDTDALLTjx3rR5p7isPdIMr4VCiXouMNmO5O50qVYKNIb5_EvmymkhA9zcZo-BhcYE1cVkyZWgdP-u4TkmhU-WwAcrQ2CcmAQ612gH96R-Q_P3tYTotGz93_ik_uMKwKm27Uy3ec9O302uHf_0R3GWpBt4n0jJm-Up22TrOGX8uHydIGADALalHiAkPAklKpvz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=WCgLCWMtSFpuf8NDKrvl-WA7rPs1ZWDfCxJ55FSTZSIsbIIc_6sXchXgXs1JAUBujvA9Vf8DVuTokz2HV_uV7cb4JjKnNnp0HMQO347OJ4czt9EG78FTxb9V8gh715HbQuPvWOvcMksAfEo7GD_555wtVSXJWsHQBXbeXukir_AxkRaswNTZapJ-MnJK4xw0gJZMXnR0f_J2ZfS6xMheCWy4c_BFCGJsZLrijvN_2Bp-z4k8Gx5ebZjWAcmIu79UQflwjRgOVJBFLc37kH2reHNtqDeaOOlJIJhtCXW4Hndm4fcFBOM1cKeAy5FYB4ZkDg3uUlACmMy-GkNz3K6E1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=WCgLCWMtSFpuf8NDKrvl-WA7rPs1ZWDfCxJ55FSTZSIsbIIc_6sXchXgXs1JAUBujvA9Vf8DVuTokz2HV_uV7cb4JjKnNnp0HMQO347OJ4czt9EG78FTxb9V8gh715HbQuPvWOvcMksAfEo7GD_555wtVSXJWsHQBXbeXukir_AxkRaswNTZapJ-MnJK4xw0gJZMXnR0f_J2ZfS6xMheCWy4c_BFCGJsZLrijvN_2Bp-z4k8Gx5ebZjWAcmIu79UQflwjRgOVJBFLc37kH2reHNtqDeaOOlJIJhtCXW4Hndm4fcFBOM1cKeAy5FYB4ZkDg3uUlACmMy-GkNz3K6E1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ISECYQxSwzsyBBk8daxBCvgz41uTKXANM5HRbUgReUOlzUeUxnzXHoagieQEA-K-xYEJDmxbrF6k2zKCmHb1w-oXJF9dMeVSSvExZFJ2j1YQ6DSTm8pZYlavponcC-f1fHQZR09DdEKdzLcME0g64wYPJlCErOoD0zaWZmACJJ6yn9cj3sbd4kD3yEpIKjHreSDtpoKapZpLej0gOXwjwE6gKBmRCg028AdWlA2IFok77f6qM4V2-hBJR4IHPI2J3BXV3MnQXrEpUZG3ug0c7oCc5xsKXLLlhyUT89NXuk_Xr1wm36TVx0_h9G9pHusNK6ZCdr1dy-lheRW5mD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=I8jHDxhad_Ip0HQojsFP7v829Ks-NNkgG7tErGHuM7FLGGxXdiXNdjz7Kx4ZRaevQTyISK8hoYp0V4SHpMT8VV-POuPLyCq6_vYciT67gSnECZtDyb523XBs1sWJmBvSjO7NFGrim9GfhnGQLEteqYHd5uQmtW55wr1oVIq_piMq5obiBPWDjFXXA5BQfCK9-gZuHQXV-QX8zd2mwSKhpZTvxOwr7cf5CV_9RI_GEL3eCXZ1Nm39wXgGXR_rTV6pKYvQ64wC2-5QCQ05UKJ6KaNSH-CShxq-3Lu3mvCXXxjG82CBp_bVxDQiuzX0ZfEk_TS3-lI2pfziCevOgVgYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=I8jHDxhad_Ip0HQojsFP7v829Ks-NNkgG7tErGHuM7FLGGxXdiXNdjz7Kx4ZRaevQTyISK8hoYp0V4SHpMT8VV-POuPLyCq6_vYciT67gSnECZtDyb523XBs1sWJmBvSjO7NFGrim9GfhnGQLEteqYHd5uQmtW55wr1oVIq_piMq5obiBPWDjFXXA5BQfCK9-gZuHQXV-QX8zd2mwSKhpZTvxOwr7cf5CV_9RI_GEL3eCXZ1Nm39wXgGXR_rTV6pKYvQ64wC2-5QCQ05UKJ6KaNSH-CShxq-3Lu3mvCXXxjG82CBp_bVxDQiuzX0ZfEk_TS3-lI2pfziCevOgVgYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tenvjn4U9vZB0fWxlWPkfL5HHpm19nsdm5Zb3H8fefwRuMmKmMwRX0YWEiIWQvJsYT9veb6T6wdFUNb47y_czVOS13f1sg4l4XWVTOdbsrI6tGAEUtKtbS1PQ9jkNiLDh2wx2hxfKc-HUiamLfxj6AWGyC0-pAXI-NPmt9zzDH5Bp5IgqkPWWRTz5y0snmsVwY8i7CkGwu8w0YkQNIcEvlTNhTPAPmzmQGyoAN3uo_kvt0puCymzUsV-PHXbqVUqWPp755hI876e9_WU3OawMJyUVjIH-n5g8szzD3rEOmJ0GmMHi8kOYq9YheAMvHZ_YGyr0D2zWu_PC-IoJxy2og.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=fsB-ospqA6IeNJy7eE9Wp0sbay8JF9Bry_-Ti8NQfUEKHSsC9EcR9WPPGM90o9q-zsPBL8q6yX1hLVehRGDu2bYskQZOz4EirnygqJ1ik_Hie0NSbMPfYU7Dk8quVYPlvbMSZjwlHv0ooQJP8sYF_xZ_FIsLjEYqsOC0Dj5HAiLkUTIHeD22KKBWeTQe_HKJSjpH0ybx7mq1oBQk-6wOGZ5Uta7BjxqTbZv0fZX0b-OdgsaXxKfg8gF6pm2W2tgMiCsD1xK1Xq3FFY54N1CBWhK798IhhfxW9Ob4PAc1_y1fRhsBCxnAf2rjwTYMfkX_sMDU1iB-vjZtpcbH4W6pvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=fsB-ospqA6IeNJy7eE9Wp0sbay8JF9Bry_-Ti8NQfUEKHSsC9EcR9WPPGM90o9q-zsPBL8q6yX1hLVehRGDu2bYskQZOz4EirnygqJ1ik_Hie0NSbMPfYU7Dk8quVYPlvbMSZjwlHv0ooQJP8sYF_xZ_FIsLjEYqsOC0Dj5HAiLkUTIHeD22KKBWeTQe_HKJSjpH0ybx7mq1oBQk-6wOGZ5Uta7BjxqTbZv0fZX0b-OdgsaXxKfg8gF6pm2W2tgMiCsD1xK1Xq3FFY54N1CBWhK798IhhfxW9Ob4PAc1_y1fRhsBCxnAf2rjwTYMfkX_sMDU1iB-vjZtpcbH4W6pvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyDc5kyhiriP645-Q2dcfLqUcNOiTG2h7MTp9x32qz6xPHYqp_jt-oJekjRV7eacJSV60Px3cPYFbtFs5WlsgKc559aB2gUCp_y2IbBMcGntGMVAOQiO0gH8XJjwQs8jKU-8joB94fCljVqer7GKLOvt_ZYmelktfKV8ObfgqpFzaUX09pYjABoxu2CyK3fjOik2lK3nI0qPIcs77811lhSYeU4A6McA14LM249dTqAEraozaGcNzppqzHl-1SiAFy_g5pTaBekVSXO5otpk8qxQIvYUj3j9tIjP-MAUO0gc3axJnenSoyOPeRturYekzNeJY3R6XeMCw17XflsclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhWv5uktfMen_3XXmNGS7kowF-C6qfGYxr2O3hxIoqiFgCEOF4hY4Hblds4osxjZmDhYi59rAxPjijkYz2RloaBe_VhvEDAfVo0K6GsIVSgfvjy6o1N2e9hTqa1KuVzboXpA6FIwazXXoZtfMYzPCJlsOUMY0vg3qD1UySnzyuWyxBwN6Bp69imfPZLF9Z27IJg7uYPd02MQgEHF8XfPVF6p6pwqJAC7POBmmqgCPdrOL5OP2hl1ZFZv7n9lSsGX6Jo5NB2KPHjgZg2yZ7CQ9IF9vV47wSIomJzGjQe8RsW_7jB_770o-swSLgA404nzwn-9C7Y7YZC00a9mTHPoDA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=pE6KEtLUmC1LGJ1VzuaEHjoUZ0WPTzhMryH155Hb9vvIK8DTBtj6rM4HZTQlCCWvEnAlVlwEvhSLkv5CIMkxRKbcaS2CDXhijfubzKonIJ64xk83pCU1vZ8a4eUdW-g5ojJAACihne_Df3SgdOV0KdPfOwHocR7V3_c2cZUyUZ67KcPVkaqLJXteo-KjujvzAljcyEhsyD2o1_qknknvU-_MdhVRtJXn3JLCsyo-opFVIGv0GneRMNhcq6L1OuP6DGZZbxbC2wy_MBRXxC40BGImezDazIuLoE328hb7Xv-KdgZazeLl37FpCit6NNs8gOn44NvKbGf6DdeKLDHWHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=pE6KEtLUmC1LGJ1VzuaEHjoUZ0WPTzhMryH155Hb9vvIK8DTBtj6rM4HZTQlCCWvEnAlVlwEvhSLkv5CIMkxRKbcaS2CDXhijfubzKonIJ64xk83pCU1vZ8a4eUdW-g5ojJAACihne_Df3SgdOV0KdPfOwHocR7V3_c2cZUyUZ67KcPVkaqLJXteo-KjujvzAljcyEhsyD2o1_qknknvU-_MdhVRtJXn3JLCsyo-opFVIGv0GneRMNhcq6L1OuP6DGZZbxbC2wy_MBRXxC40BGImezDazIuLoE328hb7Xv-KdgZazeLl37FpCit6NNs8gOn44NvKbGf6DdeKLDHWHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr_LYzh0abKU4JPcrpp-UwV3ciUA8pNwxTVq09PMsYE9KuY2GRhjn8VTt-S7RxjAz-GiXQ5yz-80OvZyY2J-qwDtlHnD6YxluLIMwWs9eJwbFSu52PoEGMr44E58gBl7tZg726YwldRjwhzOdRGc8IooOUQwYburh63gDIr4F_1etqeIZx7S6JpPVYd8gcLS8t5MK5_bNVSnJHhPUtmdFWlLq_gv0Vp6PWm1FinlwnsZkqhD8BVFD8Js9mjzLTWWOpjv0CpEb9gtO0CJQbQcEKKtBJHJg76Wv10cfeERHb2lLzDBhFufgexHw5ZIgGSiYX-lpG_bjRRNDxi6_qkccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAs0qE00PDBSe_J2-78PBvBp-VpUp68_OArsOjo1knY6NtOFaUvSHSq6Z5z3LFzWsAr-b_JrAz2bc0UlF8XdTHUZ5qny6sKiizu_qRm-p1HFsnfMr3epra4k3Y86zxytTkcQc5mdGMwK5pM07c62qA-Jv4hpmYWOsuZtBI1oNsjq_ZKZ-GLUslNZIs_7rdpjWe5W5ZU94wt2Oom6dctMkL1VXHfBUOYbR-V3uf9qN_ijJspgJGS5idFuOtWWyef5zo_saczSSvDzpMoZfKawL2qCnzS0ziqAiqfbHPJFLclKef5fxah_64LLbdHHpySNKmrLUEF6W-lmj6Dl-P4wXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwmcXGnc3h41oi3d4d3NccM_oo_xYURamuk8z17YnOjPSJiK9Wlu08qM6ecSUE2Med1BQi5E-D-C9KY-2GpK2hE5ehykGQDlvmo_Synx3vBQPIn7TQzf42AGDXft4BtAMwUoDuJ8JwPtqvYgqPEH_n8LhUBZfiPm0ZeYTPXkqRMw8ztBUIHZ7cQjBYDSQTVfqyambvIx0Gdxq-jHXAdGSCL4hj4KnRTzgmhMblANIqVQcyzUupcJh5bm4gBBUddpBuL6n7K4yyblrwIOxoi4PguSEW1cKK4gp_2q0uOjPmGUyjMjw5JN5wX3n5tUAcruTktaeRe6714Y_UJABNcMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
