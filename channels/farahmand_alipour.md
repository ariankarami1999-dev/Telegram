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
<img src="https://cdn4.telesco.pe/file/kfOjvhHLDaislv7POjW0-aIlSI3ljixn89DTRgB9LNAJPgoGT0vUl2VevMVyx0AeRBMZf1ppeTN69vp9dpzcvuYobOXG6GJMUcGgp6OTva0wp9ojQTBdrLPnP85dHfwSGpMGPQb-RAMZaMdrq98m-OPq6AUbXe6KIbzJEDVpmSNT848vDWD0pmbjBGd2LUgN4eLhHUXohkFW-UjxJjF559cjM6wUMxXjBAk_ODFsX8sHl4_Kk4aM0CXVI47HrSQvXtsTdIJnmoompFWdhQq5A5ZlPM52zwWXW5pxZ7YWQ6U9HqcfV4Xu3fH9-Ql6GNIx2UU0O5AJNbFEdMrQneMFAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRSN09u_Ej5XVX3CKul8QeIlXERflG7x6xPGrALRQwzdRTiT0Nb-uwg9FI-xKl8Dz2bY0wHnstXfIu64gdrxwKqHr3tagyduv72FarkYSTFbAovjjrZ8lpRG38O1id9NMLPIhcho25KcCxHeHpYyTcQE4i7C7nMMrpoGnQlfa_1GDhjrF4zL0BTxpB6ws0cR06-1t-Z5RYcBu6wivDhkD7DMxb2rlMs1Q90zDUKjZGRJumFxg8TE0DfpEcAvKPc3Whni5NLXxjN5k4xBrgbeFMZkuZbysKM95aLHHrxTh15aycmEQRJK4EfxNPrryk-Htp70lsztEfgF-zM1G28bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LyNBbNr0OwF3CxqDF-iBhX0QRWaJuFyAXwT-YFqP3HngzPd4fwWza5TiPFjYrokzjakziA6zYrO1mq_0leBhl3PXZQmKgS2Cq_2jDQ34biAKNUDNDloHAL5V4ahXZcf9MgebzZxLYQ1PJEEBWmM3TWOqZR48GQHRncsMV3aocTan6BOXZWXirlR7wiaKTUgzoih-qjormBTY8bNFHTZQKMwW0mj6eR4lrvb7GNli1CSR78S3MW2F9gM-PUicIL-wgn0Pt3Vc_o0w4BbsxmV7q0J7pCahROEetEsPZcE2n2vZGl7pAFmSQEXEhZ9ggxik2WZoG0yOBQaIy82OV0eDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LyNBbNr0OwF3CxqDF-iBhX0QRWaJuFyAXwT-YFqP3HngzPd4fwWza5TiPFjYrokzjakziA6zYrO1mq_0leBhl3PXZQmKgS2Cq_2jDQ34biAKNUDNDloHAL5V4ahXZcf9MgebzZxLYQ1PJEEBWmM3TWOqZR48GQHRncsMV3aocTan6BOXZWXirlR7wiaKTUgzoih-qjormBTY8bNFHTZQKMwW0mj6eR4lrvb7GNli1CSR78S3MW2F9gM-PUicIL-wgn0Pt3Vc_o0w4BbsxmV7q0J7pCahROEetEsPZcE2n2vZGl7pAFmSQEXEhZ9ggxik2WZoG0yOBQaIy82OV0eDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGcTFHTDm5rs0PQm4WiNL5cWFg-0IUOmz5FUZ4-lTaBjlH21xlcjdOF3D2y6-r59f-9SMA7Iz9p1elb6UnSp6VZriqDOXAyThTHfFwIH6J_BrR9IPDec0A-FKkAIn6d8rw_Wp15PdOmnnHx_UbFPwBAuYq-ByIgr4Du6XW7aA-vbUCo_J1Y39bxM0XwZclqNI04kW75GSex1P1x3ct-GmUztW0xkOTS4EU0NnkF3jUTYu26MCXXehD_6M4eBEfbzaV1xi_JmuKPqj4Fx1ofDPCMFVi-mrgY-p3JbIwmsYVaBuNiznX4wTGxgDmnb1lhdWuNKcD0f0Nrm66q5Kw0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0hQcdAe-Er8Ch6T8Pi5fXDj0ReIZnLfzzJV3CmfdUD7C5cGwBClZf_ZWW6A0LwbIdlJEpqzcGY11WwwjM1ZJ9LhU8d8FTYLhaAb6nD3cuGThwU-wcpaHOSIDFIbWOSs0fP05Yj56rhBK6STrZKwOl0O5S45MxwmILdnLmxOEbETBtiE1nOlly2Xhi2JEs3M-7FT__DiKKxSgzPnewND2GXia22YYTQ0tJI5yvdy7eXMY4wb4FpMd6DmJsJTrJN5QXm50wT4VwTAuNz6aKw-cWT8bNs_Hm_N9w7H3-REguS4KtIvZstiGqLl93RUnqTP7fmq6j8BVLtlY_cZqW76Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX6mKjU6CBm9VoY03IWK6d_4syPbXAuJTKMW9yGfkl9zyqpnDitZutV-bzRrzLWyQdtaBaa4gCoVt8G7vByiCMvmDOXF4mEeV2_eAbr9jykANHV_8RFqyAP5IOICzxbrNUeuXTte_f4zRhChjB5jrPV92Ji1PVL5MkIygek-K42Rvs3CNZ_1yxUp3bPEeTgg5eTYqukrvYz98rHz-6LC6tajwx3HDo06XVaxMjg8WHu5twnzBTCG-ChtTdDg6aMuf-pu6gHaWkdLc541MxmRmtkoSY1GJs7-P5VMfQPCJF7PJ__B7DeqK5znMUyLz1Viut4W1JfrKi1Xo_lv-YpF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=GpLh_bem3gyYjRwcXynTq4Q5Bu2cV8Bbkr5QV8ou6x_XzuHx7yVNPmgAHZWbXdkkyutddKr7_1EpKm0QFyShO8P13JRWtLjgxG2eDJ-XO8aYMNEbY8ATEzsedaTvqe04DhS6bTFH9dHxLFr_YjJVzwqcLwUsBSKdaWey2Z0NFed6NqwMkbxZumoflsNcg3kJrvw2MUVfklgLUs7HELWWTOoZ01Y3zrFwRkViaIc6Ib545wl0B_4fTtZa7QRLqrL-cwNIAKjb0OvME3Joqsge4jBGa38cw5Y747CXXhaP3PmBSFZXHuXNxStmRABrF2JRgkinSU-chRLXFV0aDNL_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=GpLh_bem3gyYjRwcXynTq4Q5Bu2cV8Bbkr5QV8ou6x_XzuHx7yVNPmgAHZWbXdkkyutddKr7_1EpKm0QFyShO8P13JRWtLjgxG2eDJ-XO8aYMNEbY8ATEzsedaTvqe04DhS6bTFH9dHxLFr_YjJVzwqcLwUsBSKdaWey2Z0NFed6NqwMkbxZumoflsNcg3kJrvw2MUVfklgLUs7HELWWTOoZ01Y3zrFwRkViaIc6Ib545wl0B_4fTtZa7QRLqrL-cwNIAKjb0OvME3Joqsge4jBGa38cw5Y747CXXhaP3PmBSFZXHuXNxStmRABrF2JRgkinSU-chRLXFV0aDNL_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHx64jqVOQsibxvmxecEi9EBgNJbrBJc0iOFpUN1JTlqUrm9JAt2_l8JOLz-MbB5eSm_2s8JwdhETbilzNE8LY5OzDsbPqnKvgr7pbSHJBuHAdMeBt0u2pMLLLKfAlUPQJrVm6OlqlWq6y5QZunHRotrfTBiKbS5LZeWeLf2-j3GH6P0Dy_YhfVdbzQ1EWYWX8ovVXpuoODnN_y_DMOxDA7qXqnZYQ2K62QGK6VTOO1l-xTNVrAIYuH4uyUXcFLrtFZVtc3c5KJyxV8hzXQJciH1uZPtjtpIR_3UXEm60S3sklLvXHLvyoZl0gbvmAmiJhEHqSBZ1AhYZVv3C5--5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3jN8P7ojwLI2eBDqv8UzKlllX3-oCprTVbBbJkXfnSkEeei1IM2vqSas03RopPj5TnqUI6B0ZIlS9L4vsr-oEN79JElqnMsRoHgmzfghV2l0eU8AWdxF0gXGSUuYVV4D9wTL9eMFIWsrw-UxaGXAgxBwKf8oNNnErVV5_Gp39590tJa6v1Y8LJMbaz7hM33un_kYbEH_vkPbVwU_6Tp0k9CMx1E0LdRprUv9ozVR9cC_OmhghjdJWH4iDZRLwaqi_6W1O1j5v0Qs4Qc2K0D0Bz8V9sGMyFkyvz0G1iR_rFAx8ZpPLJIzXaU06lQIkCeWuNxbAICAtRB_r0umwA81tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3jN8P7ojwLI2eBDqv8UzKlllX3-oCprTVbBbJkXfnSkEeei1IM2vqSas03RopPj5TnqUI6B0ZIlS9L4vsr-oEN79JElqnMsRoHgmzfghV2l0eU8AWdxF0gXGSUuYVV4D9wTL9eMFIWsrw-UxaGXAgxBwKf8oNNnErVV5_Gp39590tJa6v1Y8LJMbaz7hM33un_kYbEH_vkPbVwU_6Tp0k9CMx1E0LdRprUv9ozVR9cC_OmhghjdJWH4iDZRLwaqi_6W1O1j5v0Qs4Qc2K0D0Bz8V9sGMyFkyvz0G1iR_rFAx8ZpPLJIzXaU06lQIkCeWuNxbAICAtRB_r0umwA81tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=gc4YuAVbCTfNavhScp79mS4mfBmWAcPFIM4K7Ckh1XB9JEnNLq2Oil88JB3usYE8wOJxq4SydoH5yNTvGpOUQojCi7lvZGLbTXIyI94RHbhWhXn08ppVHQpIvPOlaKSrG3hjYFVrtOF1-aMgLCrPLL8GvqLkhAVvWZQl6sfj82icoqtfmOQLM6_HfTwxqP9C-yK2iD4CJ4EVxo6CS-JeU_J6NuSlDaJPIzTRHY74F_Dr40SDZAbcpDcQWJTHXDdjgHkWTqJ5_1peeK5uev2d6TJw5jrbZbuoadtMbDEdvh9F-d_OEmRDXOSt8y_F2d15ZPjdUjVMM-sC7NwwMIh5jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=gc4YuAVbCTfNavhScp79mS4mfBmWAcPFIM4K7Ckh1XB9JEnNLq2Oil88JB3usYE8wOJxq4SydoH5yNTvGpOUQojCi7lvZGLbTXIyI94RHbhWhXn08ppVHQpIvPOlaKSrG3hjYFVrtOF1-aMgLCrPLL8GvqLkhAVvWZQl6sfj82icoqtfmOQLM6_HfTwxqP9C-yK2iD4CJ4EVxo6CS-JeU_J6NuSlDaJPIzTRHY74F_Dr40SDZAbcpDcQWJTHXDdjgHkWTqJ5_1peeK5uev2d6TJw5jrbZbuoadtMbDEdvh9F-d_OEmRDXOSt8y_F2d15ZPjdUjVMM-sC7NwwMIh5jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=a86rBwPpEWlgA-y1dDZEf3JlDq0vqhFWb1HnvavuLyXl7GdZR1URBwk039PSZ3mZsP_uZU_J2MOUdHduNDPjzfk3xWU_4xHeChz1D-TijEZsWKORVoqZRhfxZJos9xFF1mrj51JEKCz8Ls8-qW8FmMpl8hTcjXNd_YcdtJUK8wGI5FM1S-x58NRmzvUnrnXKIjW6xZC7LinjmNzN3OElhyaeJr1WXgNjaOyIkefLeg4k7pORwwrjUtFBo9yFRy8u1R_Bbz6yNC_Sq_7uHOgq2W05DJZQ6QzNnNhdfsRItgdcSpmpEqJmKdgLsVrEty7M91KPNq0B2pTdQPmzw3NInoac8YIVXCnpW9CMKqZWNt8MjiLosGGbu9vWq-W0RuR8LVuqQVmxmC5qFzmqauE67_HRyFjZ2beAu6F-JMdiZMP_6I-_R7ooC9uFh0rQx-i6FiYn_MVPe2Xc_tCIu5g66v4tsybxpNuxgXAxnM60DTqdW0kHfKTcl4vZ0hP-INQYv-qA-t-nstOh7EV268WPqWdlLq7Y8rw8xfUEZVtS8LpiC1zu4vNuNQSCvsYs4cVRef8j1KJC6gBch2wMFUkNPeCaR31d6FbgcjTvvDvSH515dyBPn-2r0bi0PMQcqZcJJeO-nunpBIDBEoYzPtdsSqZ4NINmlwN5zMRKha3UhZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=a86rBwPpEWlgA-y1dDZEf3JlDq0vqhFWb1HnvavuLyXl7GdZR1URBwk039PSZ3mZsP_uZU_J2MOUdHduNDPjzfk3xWU_4xHeChz1D-TijEZsWKORVoqZRhfxZJos9xFF1mrj51JEKCz8Ls8-qW8FmMpl8hTcjXNd_YcdtJUK8wGI5FM1S-x58NRmzvUnrnXKIjW6xZC7LinjmNzN3OElhyaeJr1WXgNjaOyIkefLeg4k7pORwwrjUtFBo9yFRy8u1R_Bbz6yNC_Sq_7uHOgq2W05DJZQ6QzNnNhdfsRItgdcSpmpEqJmKdgLsVrEty7M91KPNq0B2pTdQPmzw3NInoac8YIVXCnpW9CMKqZWNt8MjiLosGGbu9vWq-W0RuR8LVuqQVmxmC5qFzmqauE67_HRyFjZ2beAu6F-JMdiZMP_6I-_R7ooC9uFh0rQx-i6FiYn_MVPe2Xc_tCIu5g66v4tsybxpNuxgXAxnM60DTqdW0kHfKTcl4vZ0hP-INQYv-qA-t-nstOh7EV268WPqWdlLq7Y8rw8xfUEZVtS8LpiC1zu4vNuNQSCvsYs4cVRef8j1KJC6gBch2wMFUkNPeCaR31d6FbgcjTvvDvSH515dyBPn-2r0bi0PMQcqZcJJeO-nunpBIDBEoYzPtdsSqZ4NINmlwN5zMRKha3UhZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SkbtflSpXcwYtKCIKyh4aAHlCJrQttaGaPWzVKr78S6gjero7aZ4rKy-EjjIDAV9D4Qdd5ep4LEmxmQjxQGjxR2rr4r2S5oQBU-8uTgeO9HMAsFbtPqxJNu_KD2dPthXVJkGMA4F2iIRgA0D1gcEydzDZrhTgbba4jEV2N07Q0h72gXSbLq5iORgrtXgCiGTTqf2HcKoI2d7XFX7RNppurZbYk6igJaUyK1LOiYxcXFyKiyghSUHDzB9Pp8ei3HRJgP3SzGuR_PLGOMgatiNPcrF7ftlAxlr-2-A9ccbFUFdjxuqNCwRBzv5M4HMcKXo4DgXvtbfRz_C6ahcO2U6Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SkbtflSpXcwYtKCIKyh4aAHlCJrQttaGaPWzVKr78S6gjero7aZ4rKy-EjjIDAV9D4Qdd5ep4LEmxmQjxQGjxR2rr4r2S5oQBU-8uTgeO9HMAsFbtPqxJNu_KD2dPthXVJkGMA4F2iIRgA0D1gcEydzDZrhTgbba4jEV2N07Q0h72gXSbLq5iORgrtXgCiGTTqf2HcKoI2d7XFX7RNppurZbYk6igJaUyK1LOiYxcXFyKiyghSUHDzB9Pp8ei3HRJgP3SzGuR_PLGOMgatiNPcrF7ftlAxlr-2-A9ccbFUFdjxuqNCwRBzv5M4HMcKXo4DgXvtbfRz_C6ahcO2U6Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnOkKG4KBZ01e-18LYRzIZD5W21iLzodyQ9iNGCVxCy-_sYzatc-1t488Nj7n6WPsQByZuLDgdTpYwUZYvNlze3xjwVL0fQxBJWZfeqHPg9J-1jsvs80zPmaLdqSewjRCawMTjzwithO0CAiy28ullZ5IauCGOGRjVDTU_NJt2E0rcaGMPlcWWMtXzSXpf6zgG7bqCvkfPmcfB3nPnB7WExDfVsaTo2OCiHpI2iT1g7iWpmY7aA4PvHj4MInzlKX_ZnS8vcI5RBxJt-OgO8yBHd2J1Iz3lVr2EywqnV-qMzcDggjXjZazPn76D8bNce-zQ0wW871TleyLsQdUUq3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=CQ7arFTXMXg_7qDwwtxe_eAcFVCy2RbdVUhAuroNjX7uL0xxatTinRANJYP5ogYa9vnyVX-Bo44EUcPEYhsUSTX1F2S6h8b-f4FL3YWFOewxNPs01gNxRk0FGWk9jmrzvJ62hgnOMvip0lCW8tjNSkts3ilzLLWoOfuaA2sPHFDlfD715IOcT2pu4O0rAGz2K_LBggWFwJKWmU-aiGoAesWj2QDbXqXZTAkBkgTM15sq7I_B33rDQYHtxNNVcZSMZUlvMHDGbnsERQp42YnMCW3jIMTWFZlTqbIbruKWXst6uUvhJMWTkbOTOMN9Gq89EcLEUFhWvE6lP0u_5PgJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=CQ7arFTXMXg_7qDwwtxe_eAcFVCy2RbdVUhAuroNjX7uL0xxatTinRANJYP5ogYa9vnyVX-Bo44EUcPEYhsUSTX1F2S6h8b-f4FL3YWFOewxNPs01gNxRk0FGWk9jmrzvJ62hgnOMvip0lCW8tjNSkts3ilzLLWoOfuaA2sPHFDlfD715IOcT2pu4O0rAGz2K_LBggWFwJKWmU-aiGoAesWj2QDbXqXZTAkBkgTM15sq7I_B33rDQYHtxNNVcZSMZUlvMHDGbnsERQp42YnMCW3jIMTWFZlTqbIbruKWXst6uUvhJMWTkbOTOMN9Gq89EcLEUFhWvE6lP0u_5PgJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=HQKibe93vIT486RHmTAoL6Kr-YJZwGNVlQ6tcQbFazXm4k6zCLMDpvu60NW9d-O_8lxLeK1OSODJU59E_F3pz-erY0G9bha8xOxaRkpgWFS0z05qRta6LB-hLqwjbX-0CweFaoOoOtkYkLeXpG03x-WVutcapzJF6rO4L1X_L79vhCe4XSnbK_yKDwM_bwr8I-jijfu9Um22nQ2zAkCvul-4Op5ZL0MgiV-PX7nNY8n8OQj1mIBnAqFd5qekf6MlEIZAG5clbMHAPfSjLjEev54ujh6qJZXl8HJKdhupOn6y8BK6sKstugqofMOA58ioajny0OeixuRemneYhvAoXbhvrSyxghc4ZBnSa5Ca55Yt4CtKuIfjQx-JJ3AO0OTQd-K6NHWKXGh_0sZ1hiIC2WkhW44yZFo7jerjKKmSGQGc1Jxee09X_Czq6YLiM2qEC-6Q0Nnicu7_1SwcxGrPvOBZ2wYbqEDTNf2e_WApYydSg-I-pXutF-NbJmuQlMBq3RfV49aYfWX-c-7inas1Qg_ByBpljANuV8eWWDAE9fjcZAxz4w6E00S7ba3KkVQh1ygupDzg494etRrny96KRpvDlfmMzIpnJkYeJYitOd3QwJCh_KZjY2byf95lKLplXwh1m3kkShi6L6wMkASk6ap4W8ja6OAbjhYJJhwB5yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=HQKibe93vIT486RHmTAoL6Kr-YJZwGNVlQ6tcQbFazXm4k6zCLMDpvu60NW9d-O_8lxLeK1OSODJU59E_F3pz-erY0G9bha8xOxaRkpgWFS0z05qRta6LB-hLqwjbX-0CweFaoOoOtkYkLeXpG03x-WVutcapzJF6rO4L1X_L79vhCe4XSnbK_yKDwM_bwr8I-jijfu9Um22nQ2zAkCvul-4Op5ZL0MgiV-PX7nNY8n8OQj1mIBnAqFd5qekf6MlEIZAG5clbMHAPfSjLjEev54ujh6qJZXl8HJKdhupOn6y8BK6sKstugqofMOA58ioajny0OeixuRemneYhvAoXbhvrSyxghc4ZBnSa5Ca55Yt4CtKuIfjQx-JJ3AO0OTQd-K6NHWKXGh_0sZ1hiIC2WkhW44yZFo7jerjKKmSGQGc1Jxee09X_Czq6YLiM2qEC-6Q0Nnicu7_1SwcxGrPvOBZ2wYbqEDTNf2e_WApYydSg-I-pXutF-NbJmuQlMBq3RfV49aYfWX-c-7inas1Qg_ByBpljANuV8eWWDAE9fjcZAxz4w6E00S7ba3KkVQh1ygupDzg494etRrny96KRpvDlfmMzIpnJkYeJYitOd3QwJCh_KZjY2byf95lKLplXwh1m3kkShi6L6wMkASk6ap4W8ja6OAbjhYJJhwB5yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b__bqLa4Za7xoc3f8QC_JIfDblXVMDUTBHShfOjHQp71iFYI8WOvJfyzyzLhufFmcmC34ByW8c0PtTYBCVqtrMoT3QI_cPrOEK3XqmAT9XDMcyDMLWsnc63dM8JbBM3BUsHltKCdom62Q92WaQdyJMzsTMeQ4jnGoew5ERSI5qedjpOndDxo8E-10zxXFlUDVgbqGqNGJBNAQOI0M3SrS6JGmGR_IGWjHJXMinqn6GpH7wbZ32h67tb8rJmH3D-fyFi0YfSh4ycl4dBVFJQu5gSqaRIA_hSTx47WFYDND0IRAYnINyy-T3YNlGQGV3ph9aRliu1fskZMlv98My6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=mkywcgX4XPylN5-xquXNbrcBudhHtb17N36x0AenN50-2QIRR4RkxSkYs299cj0E9FIz5TLGfhKOBl_65jO8rfNVJnNIWCnzQEMopvZiogRqFa8UxLZwS9tPIqSEBFhMiNET-DPS_hcO4e07lgu_Hkei0QPlV9oziIPQ_PXKsNJd9wtoifeuhzwl-PridHObmbhVZfoWrZ1skrdeFwZRfKHwBwu2tTsijQMP00vbDrS9qjFwalUiZ52x7f-NgwV5fm9eqnpxfyRmb4s-vhKbr5c5SlHkk4fpGePxgT0rM6iWyaKIyKiizWFc8MwBAQtRZyNYRGwzENvTUtB2P_GQvSUV3cY9Ffnq_VM_H3oj9mVgofmwG_ty-DBQjkFxwz2F6DsigWzL8Pe-Kv4ZvWxEQjNX_FMYgDAi8P6CVaRpgD8TM6HHaGduyOuj-jXdHPx4qFI1i__LKAAjlLTBczY_2JfW0450i_ntfmFhN06mi8ULr4fiY_YVPYFDIR3nnWecsBqX0vKgNEp_i7tL1IGtoSxuvU9iDMOD3cz6DmgKJUVryMuV-ENC4nR35t9KrIqui4a2GPvMi6tFlfWK00L-vkqqbyUYuwsZDQ9YsVjjN5OAqEYIWJBsGPX7OT_a4tfuef3XetJJ2Q_qqqCCTISRODv5atTzcdAo8LH9PSSQkCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=mkywcgX4XPylN5-xquXNbrcBudhHtb17N36x0AenN50-2QIRR4RkxSkYs299cj0E9FIz5TLGfhKOBl_65jO8rfNVJnNIWCnzQEMopvZiogRqFa8UxLZwS9tPIqSEBFhMiNET-DPS_hcO4e07lgu_Hkei0QPlV9oziIPQ_PXKsNJd9wtoifeuhzwl-PridHObmbhVZfoWrZ1skrdeFwZRfKHwBwu2tTsijQMP00vbDrS9qjFwalUiZ52x7f-NgwV5fm9eqnpxfyRmb4s-vhKbr5c5SlHkk4fpGePxgT0rM6iWyaKIyKiizWFc8MwBAQtRZyNYRGwzENvTUtB2P_GQvSUV3cY9Ffnq_VM_H3oj9mVgofmwG_ty-DBQjkFxwz2F6DsigWzL8Pe-Kv4ZvWxEQjNX_FMYgDAi8P6CVaRpgD8TM6HHaGduyOuj-jXdHPx4qFI1i__LKAAjlLTBczY_2JfW0450i_ntfmFhN06mi8ULr4fiY_YVPYFDIR3nnWecsBqX0vKgNEp_i7tL1IGtoSxuvU9iDMOD3cz6DmgKJUVryMuV-ENC4nR35t9KrIqui4a2GPvMi6tFlfWK00L-vkqqbyUYuwsZDQ9YsVjjN5OAqEYIWJBsGPX7OT_a4tfuef3XetJJ2Q_qqqCCTISRODv5atTzcdAo8LH9PSSQkCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=LnZID_hzZvbFPeGGz8rtx7t19vH8Ab96xOTdi9vEhitEzVJYwvoWwyrLddsWGV-9Q3LL1R4Xw-KeUJ811Rpin08kyuRF-W1iLiiFCVqm8WK1_jTpKadGmo7EujQdXLRtuLvjO6XxPVIyb9HDY5MEl0HKo2xiVuwuJY4vDc7qMqGxbfczFlNMA24QSCKSvUMn2ZlpP08bxVqMeSi_B_vYc2tAO_YRHQca_QKdkL97v4_mYLI8AEZHGXE3IyhA8IhdJ95XFQaDxgIbaeUPsbxl4gO5LcKbeAX80xhVcWXi-mAX7_hRgRIKQ9l4Wktd2VLgzh6Xp-6x633ZgqIb9rK0NpyfPnZBZs2F4U4Tkn6dPwYvMIRLkbgdqJJlkNlGwv1sgUIdSxR1sjWAf39qG042pm8OF8k175T1v_wtTNZ3B7Lf446BEpYas7FIkSapym42qRd0Ipncwh9rauQ5xxREi0WOf3yIBVndC6yXP6zku8Jc4SGWPaqT5cX8Ij4IHkjXlFqXgjW84fq-FISZa0X3VLzCred1V5YK-tRR05v0VaxCqnSPTsWG3EVwuxJvs0OclE_8eFVxeWFgixYZRNR-FDxiBs6bwkyinLM8i2kLcYZH76KM1jhLhw9tdBD5Yq0fOj-TX4oK9CgujY77IQbzMV_WLCeFe6YmEdwyFwmYtv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=LnZID_hzZvbFPeGGz8rtx7t19vH8Ab96xOTdi9vEhitEzVJYwvoWwyrLddsWGV-9Q3LL1R4Xw-KeUJ811Rpin08kyuRF-W1iLiiFCVqm8WK1_jTpKadGmo7EujQdXLRtuLvjO6XxPVIyb9HDY5MEl0HKo2xiVuwuJY4vDc7qMqGxbfczFlNMA24QSCKSvUMn2ZlpP08bxVqMeSi_B_vYc2tAO_YRHQca_QKdkL97v4_mYLI8AEZHGXE3IyhA8IhdJ95XFQaDxgIbaeUPsbxl4gO5LcKbeAX80xhVcWXi-mAX7_hRgRIKQ9l4Wktd2VLgzh6Xp-6x633ZgqIb9rK0NpyfPnZBZs2F4U4Tkn6dPwYvMIRLkbgdqJJlkNlGwv1sgUIdSxR1sjWAf39qG042pm8OF8k175T1v_wtTNZ3B7Lf446BEpYas7FIkSapym42qRd0Ipncwh9rauQ5xxREi0WOf3yIBVndC6yXP6zku8Jc4SGWPaqT5cX8Ij4IHkjXlFqXgjW84fq-FISZa0X3VLzCred1V5YK-tRR05v0VaxCqnSPTsWG3EVwuxJvs0OclE_8eFVxeWFgixYZRNR-FDxiBs6bwkyinLM8i2kLcYZH76KM1jhLhw9tdBD5Yq0fOj-TX4oK9CgujY77IQbzMV_WLCeFe6YmEdwyFwmYtv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=SY4lNf6xEqFc7G2Un_UcheGNTBZSTCN_xioN76-4g-cgKucuIVIZpyTP7eMHiH0O_IhQ69q7hqKpZ9CMDef0lNxYbFnanA5Dvsa4yOT20X4dSOOZElwnBuRDj2z9KkEYgy5G2Vay7iTHgHf1LAgsKcDfHtpimuT1lO7R9NybHs-BCL5t0tHWb1ijvVVGWz0F_9J-nbEkWvTV5-d1CSoodQDiplkhYj9b2FqqP6CNo_OuJevLfj94zhrG4pyTZsY4V9eLlAqdQFr71lKaMJeMFgMoCmcXJhAmk4xC29usRTSdoARHmS5Ke8-lDZYHmR10ZHDYHrVyhBtUGTtKsZKGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=SY4lNf6xEqFc7G2Un_UcheGNTBZSTCN_xioN76-4g-cgKucuIVIZpyTP7eMHiH0O_IhQ69q7hqKpZ9CMDef0lNxYbFnanA5Dvsa4yOT20X4dSOOZElwnBuRDj2z9KkEYgy5G2Vay7iTHgHf1LAgsKcDfHtpimuT1lO7R9NybHs-BCL5t0tHWb1ijvVVGWz0F_9J-nbEkWvTV5-d1CSoodQDiplkhYj9b2FqqP6CNo_OuJevLfj94zhrG4pyTZsY4V9eLlAqdQFr71lKaMJeMFgMoCmcXJhAmk4xC29usRTSdoARHmS5Ke8-lDZYHmR10ZHDYHrVyhBtUGTtKsZKGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=oYpNXcqjldAKg49fQBouJG4g-8Q-Pm677gtx-_X5nQY0TjxWPKOF_ifRZBczpHSSizpmY-bUMOHsEgJsQKo6n9YDpeK-QGol46GpBN1VCeIvjBC2nLk5-fm77zNzZnz795yJuQH9EEQtj8kRyZBUHwQS_5E80-rmuFB4vMWgwO7Tdn6Iu3WnyH4G55q0RtlwFREQSQxmITdTLLgP7TRrmos1nR6lvLVkgDy_6TvlgtLkzHY0OxKuR9gZsDHHQqwIGblDjRKQ3jjZwpPJFoUl6Y86NSr_Qld06Wpoft1zt6y9_bcjzMX_xXEZxRcjs73Dd1KmNo43c1x9RyCdKjVCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=oYpNXcqjldAKg49fQBouJG4g-8Q-Pm677gtx-_X5nQY0TjxWPKOF_ifRZBczpHSSizpmY-bUMOHsEgJsQKo6n9YDpeK-QGol46GpBN1VCeIvjBC2nLk5-fm77zNzZnz795yJuQH9EEQtj8kRyZBUHwQS_5E80-rmuFB4vMWgwO7Tdn6Iu3WnyH4G55q0RtlwFREQSQxmITdTLLgP7TRrmos1nR6lvLVkgDy_6TvlgtLkzHY0OxKuR9gZsDHHQqwIGblDjRKQ3jjZwpPJFoUl6Y86NSr_Qld06Wpoft1zt6y9_bcjzMX_xXEZxRcjs73Dd1KmNo43c1x9RyCdKjVCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Gi13Vt1gVzBz6lnMX3br6LveqSDxALWFB_zMndUynRZprBNH1mbi79JC417JSENUJFIauwXmgIrpAHEw3w6sZuXBFcFuhsgP9F5Z6tixoeqZfVj8FtmAAhPFf5klQKvZHclJ6CH_bfRBXGqG-SmtvQ9OpAKEYotA43dfRelxoN4tJgUH2m7y_4OEywlwb_gsZSMNuhgQtchie3GcdxoeGC7SeG31wCM289iikfcA7jUFKV-U9FTid0C6mZQq7XRh2jXoVHhyr6rajyQlK8eekR-IyEBFCO1oyEvXKqVc61IWXKwQb6Q4AIiGYTmY7xxJMPlX2jsoj9MnMQh3b4nvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Gi13Vt1gVzBz6lnMX3br6LveqSDxALWFB_zMndUynRZprBNH1mbi79JC417JSENUJFIauwXmgIrpAHEw3w6sZuXBFcFuhsgP9F5Z6tixoeqZfVj8FtmAAhPFf5klQKvZHclJ6CH_bfRBXGqG-SmtvQ9OpAKEYotA43dfRelxoN4tJgUH2m7y_4OEywlwb_gsZSMNuhgQtchie3GcdxoeGC7SeG31wCM289iikfcA7jUFKV-U9FTid0C6mZQq7XRh2jXoVHhyr6rajyQlK8eekR-IyEBFCO1oyEvXKqVc61IWXKwQb6Q4AIiGYTmY7xxJMPlX2jsoj9MnMQh3b4nvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=OL9_UqcnsmRfYIy8dRHAXiVRlUDpsGce1eaAogkGBSSefpqYBE5vRErTi9ujiXUdK0FqsefpcZMRs_c2UAV-QcN3tPcJByHMteMIt2UicsqbdPMEeEuPH3JDMzrkONmHKVsT1eBlSJ2Q7T15Q-IzR1jUTjSRJ2KcYCe8aY2m3lNbhp4IgGAohSarSkjj6qRev6ZXU3VzDLZwwDPK3-Kutk-kuLR_ezO4WggEvnlhbH3jytN5z07RSOONpB2hJObnltKaRgZVsgA1bQHSRM-0bK9XJmh9eC74lzNIitftKsYGtPmbKofAbNMYdKMYzloFB-rx8oQjOHGX10HGRQX82A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=OL9_UqcnsmRfYIy8dRHAXiVRlUDpsGce1eaAogkGBSSefpqYBE5vRErTi9ujiXUdK0FqsefpcZMRs_c2UAV-QcN3tPcJByHMteMIt2UicsqbdPMEeEuPH3JDMzrkONmHKVsT1eBlSJ2Q7T15Q-IzR1jUTjSRJ2KcYCe8aY2m3lNbhp4IgGAohSarSkjj6qRev6ZXU3VzDLZwwDPK3-Kutk-kuLR_ezO4WggEvnlhbH3jytN5z07RSOONpB2hJObnltKaRgZVsgA1bQHSRM-0bK9XJmh9eC74lzNIitftKsYGtPmbKofAbNMYdKMYzloFB-rx8oQjOHGX10HGRQX82A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=pb_jQDbV1TcoJ4cOsX9EDnB8ia3-qbgRQC8aqeHNSuLWb5OcVV_y8iwZ_-GvCyRsOXjIq7VtZmdrrtjZFnFmBb5WzjOMn65Gz6wEepuDDvAvlTROmRd1pgrxL-RPTW4n3tF65i9Q8o3WNI-tiZr1Tn08zAB1-p1dWyfOxe8tserTqDl-hJWjK0NwnysdGWbV5N7s3XpcjxR7vSA88WPuaDduFD2T-AbBmpVQYUoQGK_w48ejon54fThFSQwzmmPRBwdYQzJyrqJREEikKXNPelHPR7K-oqtYGyEGsg8fg_YETj9jA99rz0QNk5zGwV4jFQ16-I2X0XWUbeKbaY2iEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=pb_jQDbV1TcoJ4cOsX9EDnB8ia3-qbgRQC8aqeHNSuLWb5OcVV_y8iwZ_-GvCyRsOXjIq7VtZmdrrtjZFnFmBb5WzjOMn65Gz6wEepuDDvAvlTROmRd1pgrxL-RPTW4n3tF65i9Q8o3WNI-tiZr1Tn08zAB1-p1dWyfOxe8tserTqDl-hJWjK0NwnysdGWbV5N7s3XpcjxR7vSA88WPuaDduFD2T-AbBmpVQYUoQGK_w48ejon54fThFSQwzmmPRBwdYQzJyrqJREEikKXNPelHPR7K-oqtYGyEGsg8fg_YETj9jA99rz0QNk5zGwV4jFQ16-I2X0XWUbeKbaY2iEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gGe-MSjzGCM49YNYTzZCDQSdC0BTT9hAzUwB6XQ6iQSFDFEAx54tpqvFJVIH9QJy02GtvxaYZRJMXpCrtZbwE7g4Yyhn8KaYOje9X--eCaM0LOuhUbTjEDQBpdd_3TxFL5pmMILCJVs-nqji4o2G6P2Z1kmMWyk32DUnbC3Vh9RREexFAa8o8FpPc3nCYr7vRfs-XKlq4K7bM-i1Iuygq2wnPnL--ylCgxfEK5En3fbx3UnkadYHnYa8K4lc81ilX2tizI63-ThvTdIkPmO8ZJx5sMGzo7tMY5aGdtOD6NKqQvbgLn4NlNwmMref2_2uJNym83upDNATYH005dqebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gGe-MSjzGCM49YNYTzZCDQSdC0BTT9hAzUwB6XQ6iQSFDFEAx54tpqvFJVIH9QJy02GtvxaYZRJMXpCrtZbwE7g4Yyhn8KaYOje9X--eCaM0LOuhUbTjEDQBpdd_3TxFL5pmMILCJVs-nqji4o2G6P2Z1kmMWyk32DUnbC3Vh9RREexFAa8o8FpPc3nCYr7vRfs-XKlq4K7bM-i1Iuygq2wnPnL--ylCgxfEK5En3fbx3UnkadYHnYa8K4lc81ilX2tizI63-ThvTdIkPmO8ZJx5sMGzo7tMY5aGdtOD6NKqQvbgLn4NlNwmMref2_2uJNym83upDNATYH005dqebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=T8siXtIPcUC3cGGm8uEGaMOktyKkyYL7s_jwiNhaAYjRLygyzhYvsnVqc4R4M3ygq02OkJCH5jwiWCV5ntfC7K2Lb3TP3ATlK2leK_eifI7IZDpJDyrNINOJ_ryXfhVDs3eWnDNptXQjSpIvtT-CY8Ij9f9Phshu3A9-lxaN0SWGJhIGV7LAhdfuY8CuWFLUE8dRb99r7FfjmoIYTU6txhPVQSCWqAkyG3lAOF23tHshTaDXfZVux-gytC7OWWmluoegaN9u7iLs6De8UNCUs3bqQjtho-fcRkpJcRHpHSKA_OB0YWElC4Y3hSxXRQDcPOYN4awRUZOdiaIXd45wTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=T8siXtIPcUC3cGGm8uEGaMOktyKkyYL7s_jwiNhaAYjRLygyzhYvsnVqc4R4M3ygq02OkJCH5jwiWCV5ntfC7K2Lb3TP3ATlK2leK_eifI7IZDpJDyrNINOJ_ryXfhVDs3eWnDNptXQjSpIvtT-CY8Ij9f9Phshu3A9-lxaN0SWGJhIGV7LAhdfuY8CuWFLUE8dRb99r7FfjmoIYTU6txhPVQSCWqAkyG3lAOF23tHshTaDXfZVux-gytC7OWWmluoegaN9u7iLs6De8UNCUs3bqQjtho-fcRkpJcRHpHSKA_OB0YWElC4Y3hSxXRQDcPOYN4awRUZOdiaIXd45wTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogJVeGtjqPjPbPe54MXxCEyY0hN8v1In_fdH1NCWadPj0tA4bz0z5In4ewfCuR4YD7_pn9OpzS4Y42gG15DwysnxU6pYeOx2zmvl6cIThNsZTDk_tO0pCaBQdu_f7mh7l6F_XMO2bTE_yBcFL8BDNWrQE9m6Qwmr6i5qBheUBNDU4bO7DbVvmHkULdbD9khC3nGsXjV2SvjPA-Wl2Vyg5byhkr8v91BhhTo-NGs8SR_S4gcdClTJ6Pp9TBoYSoCAy0WzYxH7FpE3S1B1yR5akTzNFvv-ImYfNpq5bEvCbCeUZKzSZ4RpDv2LzRh0TH-UBJO_S8mI4LjGZ_yTsm-yyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=X6srFSCPF2cm7swLuAKetvQmfo16OmR3-W3TvfcHhv9s4Gnybl4QzszgmVxlpdVDuElB87olvLvn3LsegUdik5GI88eTUDn90BC_9yE2tiAceG7f0vjVBqUBE3BfMYo6HRrfLuBmi8kwvdEl819lOBQsNVchCqvKCsN7RGZITY-zZSqjL-Qg6l18kyie81Rnmu_6G9Xv__2IhH8SsKrMBG7eDDs9aT9_VfMNU7k0ftvcsQhheUBSao9HEb37IH_yMoRtMWesMzGfh56EfE7wQzSRP9CDHSDIHriW6tKvChgiZtfGIISXN_D2YCiuzAqC3w6HLhnABzBmOotD3Q0quQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=X6srFSCPF2cm7swLuAKetvQmfo16OmR3-W3TvfcHhv9s4Gnybl4QzszgmVxlpdVDuElB87olvLvn3LsegUdik5GI88eTUDn90BC_9yE2tiAceG7f0vjVBqUBE3BfMYo6HRrfLuBmi8kwvdEl819lOBQsNVchCqvKCsN7RGZITY-zZSqjL-Qg6l18kyie81Rnmu_6G9Xv__2IhH8SsKrMBG7eDDs9aT9_VfMNU7k0ftvcsQhheUBSao9HEb37IH_yMoRtMWesMzGfh56EfE7wQzSRP9CDHSDIHriW6tKvChgiZtfGIISXN_D2YCiuzAqC3w6HLhnABzBmOotD3Q0quQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=L712Mt9Kku1y86PUmFBcZ0j2egfsO1FR-7TaGqtTm-0xjRR83HLIZ37Zj3B0aDRlhHmYgTg03a9KkArLcbgWIKFZ0CRBHU5rESfAew3Lkno_wvahjOoC5GJ_8i_sVd6RLDq6OO_M_atnPl66SayiefJzNUgL5xT5gJQDjPFFM3RfGSD321tKvWZDsSCawEUxkBcpbntnprvMnF0jerXauzqjfvD7jLpU7WFSJ4jWyRrF7_xrPr1HfACtxb8rwqXVSD1b4O-Uo0ix9W9NigLXuE6j0wvQQweWyjN9yj3UEU3n3KOnceRido0ylRD4VBvMddLfOksQjNMqpPRffS7YQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=L712Mt9Kku1y86PUmFBcZ0j2egfsO1FR-7TaGqtTm-0xjRR83HLIZ37Zj3B0aDRlhHmYgTg03a9KkArLcbgWIKFZ0CRBHU5rESfAew3Lkno_wvahjOoC5GJ_8i_sVd6RLDq6OO_M_atnPl66SayiefJzNUgL5xT5gJQDjPFFM3RfGSD321tKvWZDsSCawEUxkBcpbntnprvMnF0jerXauzqjfvD7jLpU7WFSJ4jWyRrF7_xrPr1HfACtxb8rwqXVSD1b4O-Uo0ix9W9NigLXuE6j0wvQQweWyjN9yj3UEU3n3KOnceRido0ylRD4VBvMddLfOksQjNMqpPRffS7YQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=quPzRe7bPH-r9UiNTIkHsgtPWGzo4MCCy0uo6GfXBeR7VgYDDMSrxiRR_K2MnVj48L20V8pi72tL1Ryh56lPf64BP9DAdf26m_wqXPbx_agmxNnsdOVtFoBsNJPKAJNtC9E5dsaJeVkJbcCBsB2fhSMall8S_fAjuFUksDbfkjTAm9Sg8CV_7i4vt-6E9e0MoMlEWaqUI-FFBuVzQZ7labNyCxzhLQ9gaFSvS6CFp8pCHUA7tU3fGZoG-iKegoTj9ElhLD8rxVqFUmJ0NJyB3GRWI-2mXgEc7QDY9gDnDri1XfelhkfwVx-AKqamnaZ89O0LlywPjx7kPhXXvJ1Sqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=quPzRe7bPH-r9UiNTIkHsgtPWGzo4MCCy0uo6GfXBeR7VgYDDMSrxiRR_K2MnVj48L20V8pi72tL1Ryh56lPf64BP9DAdf26m_wqXPbx_agmxNnsdOVtFoBsNJPKAJNtC9E5dsaJeVkJbcCBsB2fhSMall8S_fAjuFUksDbfkjTAm9Sg8CV_7i4vt-6E9e0MoMlEWaqUI-FFBuVzQZ7labNyCxzhLQ9gaFSvS6CFp8pCHUA7tU3fGZoG-iKegoTj9ElhLD8rxVqFUmJ0NJyB3GRWI-2mXgEc7QDY9gDnDri1XfelhkfwVx-AKqamnaZ89O0LlywPjx7kPhXXvJ1Sqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=RgBcWubpsyg9_7hMLozm3PfX-lzArsHjsrTGMQO0m30GYN1u0sgDeGqPJBAP5l4n-GJI_AFr7qAOq1ptmOxDHiX1Z0b7Ac7CUlNvmSALR4uRoUN-XAG8Pu_OcTNGBgr9G7X5i12RHGwhOid3VNGxpyKT4dYzd0tPy3Uhcl-O8COrJw8Z3slyAZ9sHmIPscPDo5MY5CpiLVNZ31DjgEL7u69lzgFzvree0C8mLwQyXRwRIpyieO9em-CmRjbF0FY0vvTEq5Lfv_ie_3dGAIHb-SCvt-Q23hKv1_a6PdwG96cnHr-ojMpkQdJF5M4AbL4zRa0D2mEKesElLFNgwGy6ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=RgBcWubpsyg9_7hMLozm3PfX-lzArsHjsrTGMQO0m30GYN1u0sgDeGqPJBAP5l4n-GJI_AFr7qAOq1ptmOxDHiX1Z0b7Ac7CUlNvmSALR4uRoUN-XAG8Pu_OcTNGBgr9G7X5i12RHGwhOid3VNGxpyKT4dYzd0tPy3Uhcl-O8COrJw8Z3slyAZ9sHmIPscPDo5MY5CpiLVNZ31DjgEL7u69lzgFzvree0C8mLwQyXRwRIpyieO9em-CmRjbF0FY0vvTEq5Lfv_ie_3dGAIHb-SCvt-Q23hKv1_a6PdwG96cnHr-ojMpkQdJF5M4AbL4zRa0D2mEKesElLFNgwGy6ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stA7QdewU0htZ7BF1lvuQ6g7vYAI13ZHktVTKgT1QCDSOr34klX6xMvCSek8hZScJro2iD72dziFYCiFQTuKZlEFzQ7qtXBMs3oDqGYlk_jQgGEkrqNNQZ_-OfTURU312_SEkatB14H0i1ZF0Woa8HcE__tlOnNjfrysdhck5DwM68HPIiEFEWJ_n25_O0sIBWdiLC9lsuHy-GkM2DFdPWkIFKq3oIaCW7uiHY3LmO0eV-1SHxPiJ2hqh-izj8EPeNZvLbpC_zcRJnU9i3f5yTeZJdA1A7JZogsjBx_fnICVMJ3pb5D1mVKLjgrYDsMYJB-ahn8Evfa-ieTw8BDfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ejd1w-7A-V_C55ssK_pQ3gGN_Y5l91fyRMAf4z5BjXEIrQYXRONP4_LH1ImgA-eFNjscR6ZTE4U8SrkYa8mzWvqNBTcwldHDMs_jESiq0HQwuy7NyObZp3L5kpvi-QcJVdLL6ZdMEOBG6t8Y9tTJYFSkgENA-bl7dC_HMOIKpTDwtRINP2yfkEktzVcaGqQjEueJWSLyVIT8wzRO7rKqHExSHwOOSbyBMYnyjd3rHRadNS4oNt4FVWIFqALor0HfuiVgaaOs8VD7jYY_7w1ZhNrQa03pA5Lm6acKUtc4gHfweq6OxlUO3-iQa_oxSXrmpEZDR_TGU3eYVicevJCJyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ejd1w-7A-V_C55ssK_pQ3gGN_Y5l91fyRMAf4z5BjXEIrQYXRONP4_LH1ImgA-eFNjscR6ZTE4U8SrkYa8mzWvqNBTcwldHDMs_jESiq0HQwuy7NyObZp3L5kpvi-QcJVdLL6ZdMEOBG6t8Y9tTJYFSkgENA-bl7dC_HMOIKpTDwtRINP2yfkEktzVcaGqQjEueJWSLyVIT8wzRO7rKqHExSHwOOSbyBMYnyjd3rHRadNS4oNt4FVWIFqALor0HfuiVgaaOs8VD7jYY_7w1ZhNrQa03pA5Lm6acKUtc4gHfweq6OxlUO3-iQa_oxSXrmpEZDR_TGU3eYVicevJCJyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=KgvFKqag1LFZj3hiJVL8srMct4aOcz_sOBBL0yd9eYbGMHtrIP7bE3XxJ1afuoUrp6cnXXtRMllncqdQhffnGpgNNenoY6PpHXoDXLg-x9wkrGk-SvEoL9kxMbLLU7UxlkmLG25W8y9rzLKJ645tMPmTFJqOjSvblUqewqHk7RWi8sB4tu5hJzcwf4OoWVd9incwtpFqSJaiKkvwATcUV2mIkpC4CAO_wkM-zBNo6_5y-J5MvA8Ea8M9L0ajRnx5VG6EU-A_B4ba3wK0MyJ6yrMMe3o2UUig7dGs2AFY0zrSR7DgA4Wifl-Ex9QcrO6EWRldxi9aJ_zTd3o8CW56Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=KgvFKqag1LFZj3hiJVL8srMct4aOcz_sOBBL0yd9eYbGMHtrIP7bE3XxJ1afuoUrp6cnXXtRMllncqdQhffnGpgNNenoY6PpHXoDXLg-x9wkrGk-SvEoL9kxMbLLU7UxlkmLG25W8y9rzLKJ645tMPmTFJqOjSvblUqewqHk7RWi8sB4tu5hJzcwf4OoWVd9incwtpFqSJaiKkvwATcUV2mIkpC4CAO_wkM-zBNo6_5y-J5MvA8Ea8M9L0ajRnx5VG6EU-A_B4ba3wK0MyJ6yrMMe3o2UUig7dGs2AFY0zrSR7DgA4Wifl-Ex9QcrO6EWRldxi9aJ_zTd3o8CW56Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODwEVJ69ZCG2CzGWLscxqY5u0dKOdm0mackq9xqQJcVqtp3SyHsXlrha8Qd0dpAVn5EZ6GuXlo2Pa5rGvX_O8Kw6d8f39wvPhErNllwjd02CgQG2_NqIj3RZnt_UMFy4c3Zy8DK2ZFQa69HjNbued1q9OuSwQ71Sg-zafuvIn3Zch5imbzmlvgjVZwD4epmB_DpPoASMvLkwKEBEpyP5l-BgLz8kYwfh8YfN68cefoELADNmTvy_qvSn9-T8MciIi0ORujwd15aiHvAsiY7ZPQSVIa1BkJTYLqFPSzY5Wv643CLgI7kjK69eRgVjI8Ji1hpzOKXgUYFCvNYzbefumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfB9D5CA9spEFk38Z2e1ExQH-FNOmDEZfWx4rlr07n3ulSWvzEIpy_XsUEgPQzg2XU7z-_3jIuf5UbZqgz8q1L6BEsmL1_V_OrS28yaCyvho3XBum-N9iEpvzoS_qqDyO7y9CHMJ-ypQZp1PjWQAck5KpQnMOgpYvylymYDKb3w8L38sWM1xQHi29ier4LYxmMdA3hzpfKDsLaCgTsNtD9JTr5NpGbLZcdnG7T_sYyXYCLTg_BdTp0rUBRojRU1k7jd4fC1sciNt-a25A1M9eJFHWNtUx2WduCvPlw2dGNQVEGQ42BPizR0Tm4iKCGDGobVSaQwrnIyykY8-HfERFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mxrdkI8-C9PHv0VbtuQw8vciVA070sRDspK0LCXSh5OuC8pwUYliAV15i1SmL5gyPuFFQ9o4n71a7Im3grbj39IM1tLFKPFPiPJEE5JDxjOVUKeZQExKUm4iNZ4ECiF5NXxJPaQ8M8_NuvjIEwjrpTaCA_huATPrVNo9_1Vj-0PgDfrGHpZDg2DN-HRgf7Bxxt7Iu4Qv113taZtoXXI8yCM9xl6s3ZUSVezgvxoL_CmFwiiFzRmf9mMXBZ0jDaAa2Hj6ROJPHiSaFRKgSEdNm7672fY8HMzmMK2NjBgatXRVH5XmtF3Fgs7XcWAmOvOkgG7DHQYFAp7_lFJXWKgFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mxrdkI8-C9PHv0VbtuQw8vciVA070sRDspK0LCXSh5OuC8pwUYliAV15i1SmL5gyPuFFQ9o4n71a7Im3grbj39IM1tLFKPFPiPJEE5JDxjOVUKeZQExKUm4iNZ4ECiF5NXxJPaQ8M8_NuvjIEwjrpTaCA_huATPrVNo9_1Vj-0PgDfrGHpZDg2DN-HRgf7Bxxt7Iu4Qv113taZtoXXI8yCM9xl6s3ZUSVezgvxoL_CmFwiiFzRmf9mMXBZ0jDaAa2Hj6ROJPHiSaFRKgSEdNm7672fY8HMzmMK2NjBgatXRVH5XmtF3Fgs7XcWAmOvOkgG7DHQYFAp7_lFJXWKgFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3cUob7V-SXwVfvoLa31llZPc8vuOyFpnJqDcj1xpJZiF0pOoQVh__3K5xwHQ1WlwwU4NE5qSbaxPa7h3ESXDPdurlqBJzoZAlXc74-SH-I_yO6CXiQs8brr0GfmQOIerDxnQT3ZwKOQmPIk1s3BLUC2U9uUnGGqDVcc1HkoYbGuBymxpHXaZyIWTq-rX6dom4nqZIKr_5Cy6Ki7fzYnV-gtSS05ZO8vKM76-Qlfa6tRBfcLkmZxUREv8MjTAnBR0x6GClYjmS0U1yCRDofxegDVwXj49CqDZWOIFZOI_Lj-i5fTKkO72zrpMp2UXXe1Oxi5UPigF1Pp3xeoCOAXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdPklCAQx3CWbmipk0tGObAC0EOmA0SnwWi2usX2cnyT65Igl40ZV6-2OCNm4z3RMW1s62dBb21JVy6B7c4lPqkWimiZjqPo7_cTH7mkjAaD56K3gPrISQzPTqoC-cRzTE8SzVHNaX2PuYYQMjOUCUMiLOJfGtv3DHR_laWBCaY62-vJauN8ppI8fqgcyaFhybhtLob3uBnK-fOSKfSRK7ZOpy0nX_gt5t3S6W928td95b3lbz7fB_Y8euBffeG3clRQRzwbIdlymN_qufZqkqHvg-WYrreALUzxFnbAf3g-WEQ7szyiU5xBJWiu0eOI5n8F6Gw8vpY8msKOq0jefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCrl1vYG4zoLCyZSPXkp6KaAjv5Kp5lOKtFw4gm135sFqtAAZpetnVpysqL82RqUYDtuGtT9eqB5gHr2cjwSCo5tbdFkD42BolKIH33WYqoSAsTExVoKkhxol3-y69GzEVso-EZdgPlLc-8-mVrgAiK0VjcKgblovBMBNRfmx4wRLS7oI2FoAPEiNquNjGiwd7DJPj5WTIF3x7Q4N9caTftmtcrlhqA-wDZNYMcudz_B0ootJFCM5LynQ7X2HbIPRobGcsuV24aT3GEqxvCTqWyqdflI3uhsCEsIwj1cJzAL-XuysxwHTivpQGC0m-kLrsqcFIIwoTuPSa5bM3Oi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=PWO0Z-4spZwGIrN-42xNDd2N5i2-HnscQp765vPZjMxfw7Bl12YLqW-yPAX2cfmwhkaN-f-LI5OLiXITBkqR4ADyPuueA-gLeEGGxjEqFxBDHG8uESFQ4tqvSucZQEh1x_hMm8ggpBejmjFq9G1aOM8lYuUjWPzrKurTkOvUsRTV_TpAuoxUcamlLyaQpEPlH34w7zQv-Il26tSEb1_TEAeynVw3XBPQ4rGcsraTmGM6wcnu7Q0bEHpM1RUFlIJ7MQ70ONV5Xy59zyv027FHWb2fsQyizJ_CYSJFR-UQ_tw0wGG_cUFYPssfn-ALeaRmQVWpG0rVjXrJYSRfLyiSZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=PWO0Z-4spZwGIrN-42xNDd2N5i2-HnscQp765vPZjMxfw7Bl12YLqW-yPAX2cfmwhkaN-f-LI5OLiXITBkqR4ADyPuueA-gLeEGGxjEqFxBDHG8uESFQ4tqvSucZQEh1x_hMm8ggpBejmjFq9G1aOM8lYuUjWPzrKurTkOvUsRTV_TpAuoxUcamlLyaQpEPlH34w7zQv-Il26tSEb1_TEAeynVw3XBPQ4rGcsraTmGM6wcnu7Q0bEHpM1RUFlIJ7MQ70ONV5Xy59zyv027FHWb2fsQyizJ_CYSJFR-UQ_tw0wGG_cUFYPssfn-ALeaRmQVWpG0rVjXrJYSRfLyiSZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=fE9T5ZAhudGjmTpWILy7OccizJ6DVqgEe27fwuUlhIac27cLWVpSXV3qA8KrAw4AkMmEmmDtw7XC4wPr4dfAnLY-Cl3LSm7S-XULdHpbpxm9H9MvaE5ZtQQmcF5S853JNZ6dXkYjR22c4YYEHhm9aNiB0YISoHyhVUlv5wWPVvf7KhGnSP4bqGP4sZDxOq9h6QmxWcICYtGbRTKGMNNafaf8gOEnfXIyphypIKyNCNtQFflS_bhgeSYVmP3089kBE7unze_RtkpG12N9MrNXyRpaMhacx9B5dZPjQ0aCPH5ZnVSDKbfhfH9lP1lAQIWJBWFoNWPOcLkMVgUYS3OxWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=fE9T5ZAhudGjmTpWILy7OccizJ6DVqgEe27fwuUlhIac27cLWVpSXV3qA8KrAw4AkMmEmmDtw7XC4wPr4dfAnLY-Cl3LSm7S-XULdHpbpxm9H9MvaE5ZtQQmcF5S853JNZ6dXkYjR22c4YYEHhm9aNiB0YISoHyhVUlv5wWPVvf7KhGnSP4bqGP4sZDxOq9h6QmxWcICYtGbRTKGMNNafaf8gOEnfXIyphypIKyNCNtQFflS_bhgeSYVmP3089kBE7unze_RtkpG12N9MrNXyRpaMhacx9B5dZPjQ0aCPH5ZnVSDKbfhfH9lP1lAQIWJBWFoNWPOcLkMVgUYS3OxWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=YibKNaqCiaxjMDivJfElRZJBOqSO8lxvffyPVOeT4AtAowb0yCWoaz0bNWcycv5cnSxmKBIkyo6gwmJAD1VnmquNqxA9ms9zmv12KyMagrMCQ-SdHL1hUpf90InPCRyj_LS2pplDxi9RKRFZllwo-pdmgBedVs7bBU7jPfHiCGreX_lG7QeOXJRiaGIPLt2BDaPQPGl7vHmvSIuqHpbuaCyTVAWdgO5bJO-ayH-jvYEqxe9oreE_t16wkrbo8VB89v2GrLgV95MBcqfvlGBkWRI3RVg7M6Xu8ahzk0UnWTtXzefaH-OPppPNcbvOta61e1DzgHIWvW4HQ5Kdqqxx3xSErLtiw-8kwk2tLvTPMD9zMtYafcLNrdye6EFRlniy77h0LhXF5RaGvV84r8WDmpdkdFSkHHh4At7xHH6j55RW7GOOAUdO-E2GBt15rVWPXoikdxWlUtYeaChbH7BtpIymjv5iUumZuRWvx8OagO9_JSz8x6vNQNX4zLh5BvS2Y45_sRBgbqXW9sxmbg_QtacOHdzElmWyW0sPYDEDXKsYfrMSOVXRAzHqenX52mg26vZud-OeTOEA4CGJek4wwGY6_d-7PAwVj6My3ipO_TAJc8kAwf4i3l5fByjPOaiG5f4i20BbxQxdb8yWwDPmF4yaVtuZcFttE7-0mGqe3Ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=YibKNaqCiaxjMDivJfElRZJBOqSO8lxvffyPVOeT4AtAowb0yCWoaz0bNWcycv5cnSxmKBIkyo6gwmJAD1VnmquNqxA9ms9zmv12KyMagrMCQ-SdHL1hUpf90InPCRyj_LS2pplDxi9RKRFZllwo-pdmgBedVs7bBU7jPfHiCGreX_lG7QeOXJRiaGIPLt2BDaPQPGl7vHmvSIuqHpbuaCyTVAWdgO5bJO-ayH-jvYEqxe9oreE_t16wkrbo8VB89v2GrLgV95MBcqfvlGBkWRI3RVg7M6Xu8ahzk0UnWTtXzefaH-OPppPNcbvOta61e1DzgHIWvW4HQ5Kdqqxx3xSErLtiw-8kwk2tLvTPMD9zMtYafcLNrdye6EFRlniy77h0LhXF5RaGvV84r8WDmpdkdFSkHHh4At7xHH6j55RW7GOOAUdO-E2GBt15rVWPXoikdxWlUtYeaChbH7BtpIymjv5iUumZuRWvx8OagO9_JSz8x6vNQNX4zLh5BvS2Y45_sRBgbqXW9sxmbg_QtacOHdzElmWyW0sPYDEDXKsYfrMSOVXRAzHqenX52mg26vZud-OeTOEA4CGJek4wwGY6_d-7PAwVj6My3ipO_TAJc8kAwf4i3l5fByjPOaiG5f4i20BbxQxdb8yWwDPmF4yaVtuZcFttE7-0mGqe3Ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=aps_LUitbCjhySPeJHIaeS3WjcP9DQ_eZgRkGWwvNM9HNQ_iKV9Ej3gnVE5A9mJ9B_b6jnHexg4OXJSycgsQPEKs9bs9Zb-CRFe9f7ULXISgw-9DoHP0SvXraW30E3xSRzZ7scRLHCFAj_SDpi7UlXbqNLDGWkWPMWXIUszVPYOwjzQ6i0J7bIMakxTpxUwoeKzjn3LyAijOFMxqn0uBMIfajEmHZrjYBl1naZuDen_XVOc9P91D9hRZduW0BxeNEKdTmPemkmYVc7REYaTzGr5mlBj4OKJsnAYONekwYes8unFdqhA0vqKie64K1mUM_Pp_x6txUNPXAbE2AAoRiQj17oy7T--hhG_mMGcfDv2wf6_Rg2Ehj38picHNStnoFUX5Wl5iQNXCpFXjYRtr71IWP_Z9vqPD2QlpQsoA3BwTaLMWj9TjBBjeJiELYJlRNaG57uJKWp4zxWszmBybNsUQyM9f-qSHEP8agG-qQPHLYwuguHQxsmCyue1xVppjLEVnVMMlopOiatZSnYf56UWAKnNLPSGTK4hZ4tMRxWAoptMSjoNaBb_zapWWCWhHZ6KSCe02bObmxNJe5EkjZmlArsuSEa169fGTaeVyiMlunIbpzafKSeAaXH7sztoOinbUEtsU-R5dBAk3auJCjL5ylnvbkLJA5g51kxcObLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=aps_LUitbCjhySPeJHIaeS3WjcP9DQ_eZgRkGWwvNM9HNQ_iKV9Ej3gnVE5A9mJ9B_b6jnHexg4OXJSycgsQPEKs9bs9Zb-CRFe9f7ULXISgw-9DoHP0SvXraW30E3xSRzZ7scRLHCFAj_SDpi7UlXbqNLDGWkWPMWXIUszVPYOwjzQ6i0J7bIMakxTpxUwoeKzjn3LyAijOFMxqn0uBMIfajEmHZrjYBl1naZuDen_XVOc9P91D9hRZduW0BxeNEKdTmPemkmYVc7REYaTzGr5mlBj4OKJsnAYONekwYes8unFdqhA0vqKie64K1mUM_Pp_x6txUNPXAbE2AAoRiQj17oy7T--hhG_mMGcfDv2wf6_Rg2Ehj38picHNStnoFUX5Wl5iQNXCpFXjYRtr71IWP_Z9vqPD2QlpQsoA3BwTaLMWj9TjBBjeJiELYJlRNaG57uJKWp4zxWszmBybNsUQyM9f-qSHEP8agG-qQPHLYwuguHQxsmCyue1xVppjLEVnVMMlopOiatZSnYf56UWAKnNLPSGTK4hZ4tMRxWAoptMSjoNaBb_zapWWCWhHZ6KSCe02bObmxNJe5EkjZmlArsuSEa169fGTaeVyiMlunIbpzafKSeAaXH7sztoOinbUEtsU-R5dBAk3auJCjL5ylnvbkLJA5g51kxcObLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dQXQbiibMrF1eAlDSXi_Ye73Ce9EPhFDzrzp-0_XotRql8kfg06mfh-6m483XvICcFG0TJSKjz1xxijAagFBkLAT9KFekrwCnzn9WRiX3fu0ruMvtSGOvfOPmhNMxgYnrP3aalHNiR7SozBBdovaA4Qwk3OpTuL8Kge37uzkMV2doTwsNWIa2PtokG828NjVE3zzxnOA1QFubYJfjNBbrmridRae6Lneuu0BnwGcme3ZUSTxMHlGOPGZYwt0i-T3TTJleMD9tomSTKvBBwrkD_UA9gElt2S1SLeGVyVDy-onKXuC89EyflePaWQs03dpUiH8Uyn0EJa_Hl14QGh4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dQXQbiibMrF1eAlDSXi_Ye73Ce9EPhFDzrzp-0_XotRql8kfg06mfh-6m483XvICcFG0TJSKjz1xxijAagFBkLAT9KFekrwCnzn9WRiX3fu0ruMvtSGOvfOPmhNMxgYnrP3aalHNiR7SozBBdovaA4Qwk3OpTuL8Kge37uzkMV2doTwsNWIa2PtokG828NjVE3zzxnOA1QFubYJfjNBbrmridRae6Lneuu0BnwGcme3ZUSTxMHlGOPGZYwt0i-T3TTJleMD9tomSTKvBBwrkD_UA9gElt2S1SLeGVyVDy-onKXuC89EyflePaWQs03dpUiH8Uyn0EJa_Hl14QGh4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUW0dSzajZq07JkZweShEAaN4DaijJ0EU8zt_aZ5FJez1PASpLBq5pj-JNT5sEa360Rprb1OksUOPXMTv9O-EidBEDl0amNLJcU2fu-TFDPSt7Mt_fp-jkwbqUsT1CEn4hPNfcYDX0PBobisSI2VhsrxcEp8eeBs6ZrYWovj3sNWF33ZOSfpAqy0PeKoZlyjw7XeO-Yoy5NBeiVHqUDQCpc6Kj1L3f1y3LB2XbnxLh8bZlkf5xHjxNPqYXtIV6Ylf-Ebn52MStDQqwftK4XcxVbUHSeCir8P8MU6t6am_rufgw66ddupgv6uAyIHnjYzG6YkGYX9JMgxtMuV47oj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bGZF7BJ_NSBi9OfCzc0zPb8GsrLGMUL1R-oG2a0iunPHW-Ytj40K5paWBrCI3pXPtqckh00OXT9ZlvVSC0XEBPMtGfPCH9JJ8EGKisu_0Eysk-Bea_RIJvv4Qn9FiZrecSbwfiXlUw0wRb5K2_-cFZF0a1C6w1Y5HWRoMkrpRBi6PjNXwBvbipKJE-ncC-Wmox6TUyuwoZRiXT_mGSuUKVvStppyOZD8E1Y2bsfsNF2Ade3yCn0G3B2i0s5B6EVmZMlrI7w-lfMYX06-AW61M0vsrmIkTSbJrABcCf5n0k1X5hceogDhfLo0qhBV4PZQ8JyXjONPne1RpHsK_Xa6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bGZF7BJ_NSBi9OfCzc0zPb8GsrLGMUL1R-oG2a0iunPHW-Ytj40K5paWBrCI3pXPtqckh00OXT9ZlvVSC0XEBPMtGfPCH9JJ8EGKisu_0Eysk-Bea_RIJvv4Qn9FiZrecSbwfiXlUw0wRb5K2_-cFZF0a1C6w1Y5HWRoMkrpRBi6PjNXwBvbipKJE-ncC-Wmox6TUyuwoZRiXT_mGSuUKVvStppyOZD8E1Y2bsfsNF2Ade3yCn0G3B2i0s5B6EVmZMlrI7w-lfMYX06-AW61M0vsrmIkTSbJrABcCf5n0k1X5hceogDhfLo0qhBV4PZQ8JyXjONPne1RpHsK_Xa6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oiy1FLOBDLnm4e-WH0DLtNE5QkWRLQ4NbMsJK5jHGnMFOzTnLAM-1iRcJbWZgvIBhyx4JFS0BJ_96P4K_0EBz8sSb7eGaKBDbK0JmguGXNZDXp9lCjmwujy4iia1gnWtrW_yKxRzHBYGS-VMua6GLY7HbVzvuIcVRZG-6cw50V_9H9tTMZhXKgIo-FdaUEU0UEpWvGzdhuR3GbR3_V_ZpRtKoKtHaobiA-IxH0MjmOuwhahVa9fcOEgzvRPQs0eU_hQGT2IHEi0zEmL04vdjK3NRriCRWTabQ0gcpetv2Zd34Jr_ENKQhPRgtwLYsX3T-zWhJND7ZKKitrmu3CtZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oiy1FLOBDLnm4e-WH0DLtNE5QkWRLQ4NbMsJK5jHGnMFOzTnLAM-1iRcJbWZgvIBhyx4JFS0BJ_96P4K_0EBz8sSb7eGaKBDbK0JmguGXNZDXp9lCjmwujy4iia1gnWtrW_yKxRzHBYGS-VMua6GLY7HbVzvuIcVRZG-6cw50V_9H9tTMZhXKgIo-FdaUEU0UEpWvGzdhuR3GbR3_V_ZpRtKoKtHaobiA-IxH0MjmOuwhahVa9fcOEgzvRPQs0eU_hQGT2IHEi0zEmL04vdjK3NRriCRWTabQ0gcpetv2Zd34Jr_ENKQhPRgtwLYsX3T-zWhJND7ZKKitrmu3CtZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPsOPAE1OUdTwUgTbXrcl_oNJso9CbvLL_fyYn1oFxVD8X05bvt2Ai_CsktdEoJ9d0UHMYxxr-njExB7C7zsdpiUOQ3fD5iLebMwqrbQRRxIr1M0dd_qEnhAJDV8YwdCJqQrFV1SSJiL8PzPWW3siXfSfeQVvjlNEY5o_bYGEoOOGncFjiKB74qjmevcYyfHvJgzltw8-auB1uAkjaTTC2IeO4v9EOWgL-YWYXTjhHLOz_twwxAP78AeedRt8MggI6uHdP3yXgPYZqyYEB4YgL0gG-oB8YkKnWoltRXKh2sMl4cHYO_CpX44Z_dnUbfQflt-8kfnhMHwt6t3v2_s1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F27nJfEnF1CCC-29m_YnDcxImJKMZ_AyWuK8WHCCevD2UsF-6gsYcxhmOfdfzBxHA5z8wAsOwzALuvQ3BInaL5NwjX7Rt3_ptwLbw-W2tTiTbHFjrCOLykRgh7H6rbtEAcqH7qaqhFpEdM-79-AcRItfpeOTuzCNa80afWvYuCs-AICYixNP0XIVOIGCo-7dPFkwEc_gjb5WWD4Ncv68BuRXGIjUt_XzlagChbGcAAHzQuqqogXHt4Gq-F3bx1QfNqyu6zxZczeR1fqh0MUMWL-uLTzbMEoVZdleNT302e075Q1CWQ4359UwZNkQx7cRq11TpTKl1XZ1FGMgvCmOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA3Tro7usi8uvSKRNvRKKHrnGny9vU2t00SdtL5FTqxEwbFy3WAOZy4dQmxfCf36d0eoOAPyeXBeU-9lg1CNu255Cy69Dv4RgfGabU6sKJ2GpHqZ-1wfbtjwb4rtt7CqsSZDtuvQ-q6x0dJfmr9uElr0O5ST6EYuGpLWJ_dOZbQZTMiezzdPmNunqoHTB7qEpUaWeIYvnucxW1O9-Qo6m-zHOO5wXaW6YV1K3KzLiKOX7XMYYKQcKQmVwiHUtCnlqysRBweer5gKDuqf8-iCrVbd7JtBB4jruqmRf2twFNWFTWn6dcao6tjEWa_6oahycWLdOdc4MGo51gclGg03UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWvxnbRpxrcyK22no-HPveNyd1zHZVT8tNDXv53j8V8aj2zAsdVuejTWXZdF-IxrwMtz2Y6gf3M4idSKmuCjPWJbjyG5Wlkuce1L9zRqqX6qMrAFWsHIt-A9C7l3qN6U1xXq6lqHEknM9xtxHcCxPQl3aPajEoio8afCJ5W_VP4JJ7yBQ88xcTr4qS9njQycaNE4724LdjseEYqncZGfSK5izRjRO8hFhje2Qx43h88VQXbBK7ssz26-jrKCe9f51aONi_sHifgHhNAvl2lRd1LyL_KMQpsoZtG66uipzV2VCoudvBUmyLxE9DE5HVbGyUVwQszf-DURKa7ogLf1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSJR58WIlYKceImT1KjH0PELeO3TCUvVDmYMc_oBEkMlLqqp7WSjJSuYEPaJhgf8Xkf8Nh5WJQisYQn1L75BTmRNkPmmEeqzxxSteYEjTDML_ZnntSi7eedLwbPpVz4qefLBI10cLT8iekcWbq6ubpyHaiiOBhHHw-tXkJ_RVhuAsK-CTa2xtlSzllEo3oGGEt6q0EuqQfzWrX3ksmdaYpc65j6ZUV2l1zt2qPuEWv5SnZ8CXaypbGroyFjy9a6jWf0WlLo9_FON004lrVFJSW8G1uR704eaeLB8I518R0AruEzVw6X1UHFt_NIWFyjh0Ec20lRtFmXivXX_YE7qlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWjhPKIoWzc9Pvaionz6ob04dJl7TjYx1Db1X0ii70NkMTEYfkRCkj315wu_paLzBolVJbZv60_brlLJpdgCIcQJ2MmmZx-kdeDPEf9mvfw0vAT7E8OEiltB3Rexf0zWLDFSJepodiC-6M8Dh6J5TlfgricQvh6XVmtnGzqcqR-uAueGnL0b2d7si8gXS4UBQ2EmllrLQUZWjm44XngYHHL8QH9TO9GfVm5a-It0CuWf0mhrBW51kjLUiY9S-qkr5Pb_R6iMU6sSYLhFxt5asWM9m6JMDUC5aqJvuH5VBpFfmPPKIDywBbKQJyFx98arkpWhHFHaPstOXMpRu0Qw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBs172VeVpCZ3FPqniYwPox3_l4ferJ9F3ECvGsy1qL89kobbKqj1Stj0q6k_xTUCLofLrNvFpUeFrT6d46Mi-MGxlH5oPCYA4abZfwtFljVQ_AneLJZ_WMOkZGF-aBeNx9fVb0LcqJgRG2ONFRyJ-fv6rR5PoQvYjvPsX9cU4YJIwkLjr5OHS-hLY888jdaxDyEZixvIHvIsQG5ET6-7OwhFva59fBoRpdO9pfvisbfGl31UH68RBTjIt3PXMakDTjNLPk-46c28E78AM0bc5pG08kRkMX-OH2SBiI6SOhBNHJFOBsl8BzzST-4cXZngiZ1lpKddMV2DnrA87GbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxCAyOZtNU7E9PfFUpqIzzmGPA3YRp1FTuWXlFGedkwotNtEaQUogXo4n7phYMa4a0RmB-iVMKBmZyLgUQP4oQeL8pMYGo-KvZNTEHieqf_B8n66LPxWMWk5Uz02o9TDDprJt1b0FbZWy79jkZoBkQMfa4dsXU3Zuyz2GzJ5UNEYdeDTMqWKahtMIF2M_SzYfIl0pm8D3U5FdUxtUvPhSIUR6oHAx4vxJJjyHGE3aJqBObhGzkTXH3-54kxzT-0vUYnqIIbzDg9VCCEGkiTe8rDFVXU1kUpTzF1AZpkhXIF7m-kUe1Jebg16Tfe9XAVe8M0po30vjW8ZoNME_bKGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGaOU83zHEONvXMtbSc9X0nS4Jply3vDLAziKJ_OA2d-IogthyyGZhqyrbifoO15FHpNyxDSk10GqSucymQNKTIdPFjjNPz85rl7bi5nRpur3vPFuSf_iQPxxEGq6qPXN9936YfcnO_yp_yJN8NRp38oBHiqLqyFnF_C1mcROBpKFG54BnNmXWtFwj7U4Cxj8MVrF11HmC0-Qj12olJLLQKqXmc2rIOPjo49QIilk6WCNm5ISx7EWuTD2nOaorulUWEtgNftbJdt2hPcSC94bR0s_gvxQouW9IJtGWzUplsVj6e3O2wkNZb5lpOfiZjnbYm9UVnXm5NTuYw4ZAIr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zl3lz1HPtwNtDbUXLHIaVt2yKJpaZQsTz-RLvlGUdwpoCSih8ONdmz8Z29QHLpGUv-fdYJ9Ec78l49Qtfs4L36IQUXOc_-aQ1LF4LY_n2fOY85VGGJl8khUgC0j_Neo4YkmvOZAKQUTqSc0DOaJwX4HeWo5QFIaU_LgcVN2pRixNQptmS9nCQCYONwe7o8mZAvha3XaQ1ufHVrxbpMNO8uVLSF_s3ofU6TO1o0QxQ_sbwT38KFMLlK51Tpe9Up5b5pzUqNhT9QAPCaRoSWpPMHiQymBQMsmnjxuHNQFtU-g3v858kv8dfaIrDqmmd1LN9uxBA1V6njegV3CZHltYhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dmGFI_a0hte9U1nyBQyVBEi2amrt0DgUmVUyd0SaAEs8dyPiZTY9RKSXnLg1aUwt-AXIvyObnA7dbW5uALqHPJVLtNxeHlZUU0X99GOcbgBwO_o9L8t6v4v7kHHR1IB-Z7jtNuEFdHYDuOeVlkWdZjsMgxwOWW0uS3-IZlveHFUm4MO242AXV5rUN_Yyc2zS1xgF7AZR4oYrVHt7fTrNeIamjQ3kiopTsRRV4jOVVHNvqD6a6xM6SWawJ_lt3oblhhYZutEvRp4FzqzMoRVl6iskjEoTHX_VmlabyJwV9afJhByAYbGFYJT5RzQ2gPVfXVi1grWNOImMNXtEQx224w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dmGFI_a0hte9U1nyBQyVBEi2amrt0DgUmVUyd0SaAEs8dyPiZTY9RKSXnLg1aUwt-AXIvyObnA7dbW5uALqHPJVLtNxeHlZUU0X99GOcbgBwO_o9L8t6v4v7kHHR1IB-Z7jtNuEFdHYDuOeVlkWdZjsMgxwOWW0uS3-IZlveHFUm4MO242AXV5rUN_Yyc2zS1xgF7AZR4oYrVHt7fTrNeIamjQ3kiopTsRRV4jOVVHNvqD6a6xM6SWawJ_lt3oblhhYZutEvRp4FzqzMoRVl6iskjEoTHX_VmlabyJwV9afJhByAYbGFYJT5RzQ2gPVfXVi1grWNOImMNXtEQx224w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqpKVWJ1f1e3FhIP8C9XNdQd8ZfPVjDxxdVUT72nN17Yao7OZkJknUe3wWj2Vmfqc7zdyElL3J0vaceZs7MKElZshcCOBsUrVDrNBlg5oGL1bKJ1Sl3G1LNfEMqV77wfTRqOerfxGuP_Sbs8cgT4wu8H4V9PrByizhJ1d2WLslqbRFsQAkUrZKjqhr0MMBaBEp-_G2vZBpPT1YPMzwpciDc9cnnJ8kWCz5B06l7SJ1A_J24puiWuoDjcWbVvpLNJrS8U0hTzGLfm9Ug2y1J71dlnj8-apX317mJ-t97IqTpIRjZhIYWs07PTHiYHIfA38jmZPDLuXcVFae3rbAsdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsbj28ibgnpbTCEJb0tIDefYX7o60hbdzo6BQSZAWLsmNcxc7bMEqQWmzJAOx9qBCu5pt3gOVJiOD1zAJXpkenX13WdIsZs-FZyTFupoP-EFnSlt8xcyFnwUV8WTGfNCa8wcG2lFwXDyaBVdY-6fvuPEeRdtA7Zf7BSV-20yamWUhU6boFb6p3nIfRupLgs0_JeqeLd7m_tPR4fUNhNMShVfXrM8FC_sfk65Mo6ZhePSdPNX5A0V_uQTXMHKYKy6JNoQVXZbKfFXOzFlLzZWmwqRN6rF96tuoYea2ZpHEScT5563VfH62kx5giFGX9HUPvTnWU-tGTbXB4653Lw3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=uzWnfU61DtV3-BJID_7zGQrv5VNKZS63zhfC9qMwp5P3P-zAOthN26TMahou2vzwqhgIbvpgud1jfdcrBeukVRZAQ1KzgZ9xWWiaxKu9LtnZwTtvIpjaYP2hKouXfNFuqgaltR17APMhg2zpABG7AWey_J1-9lQwRHd5TRTIH3RL9t_GIh78NeGpxXEE0T8m3YbcduVXsIEEHI5fycJRRDAHp3-15RifBf8f9lSaix7Mmw4zc53eytkccNSKQ7mSh4eUvoTi6jHG1FYpN4e57oDM7S1uCTY1Zabbw9lVYGvuczcQppo-rni8elEpHdv83xccVcoIndhYyz7oZyWLsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=uzWnfU61DtV3-BJID_7zGQrv5VNKZS63zhfC9qMwp5P3P-zAOthN26TMahou2vzwqhgIbvpgud1jfdcrBeukVRZAQ1KzgZ9xWWiaxKu9LtnZwTtvIpjaYP2hKouXfNFuqgaltR17APMhg2zpABG7AWey_J1-9lQwRHd5TRTIH3RL9t_GIh78NeGpxXEE0T8m3YbcduVXsIEEHI5fycJRRDAHp3-15RifBf8f9lSaix7Mmw4zc53eytkccNSKQ7mSh4eUvoTi6jHG1FYpN4e57oDM7S1uCTY1Zabbw9lVYGvuczcQppo-rni8elEpHdv83xccVcoIndhYyz7oZyWLsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=l5HdMFo4oMISo97Vwy3NybjAcdzqo7kD_XZld1iOeE6BYJEN0jBZFSReGueZ_QrDrYqGt7tf0vyYiC3e81HXJM6TlcrgP2McbdDeTTMbhV_qYmApEwdyWrdf3V4FgC4sL_tim_Y-BvEJrd0cdAH3ciQda-K-Yw1rkT8QEPUO77MiowmDuwU6t19v7-_94PiIXfsUOOs9b9Jb-accIAQtkiupNMRwxhNOIkz1XHGSZqwaU_SDmlWsAc9l5WRyye_FkKsfhnplv-9zvYYvaysz8w3MWnF_hTXVwZx8padqc0piHa0UwgAn4cJstsLSD7sYwcw6xl_SVeqx6M5OOBIUCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=l5HdMFo4oMISo97Vwy3NybjAcdzqo7kD_XZld1iOeE6BYJEN0jBZFSReGueZ_QrDrYqGt7tf0vyYiC3e81HXJM6TlcrgP2McbdDeTTMbhV_qYmApEwdyWrdf3V4FgC4sL_tim_Y-BvEJrd0cdAH3ciQda-K-Yw1rkT8QEPUO77MiowmDuwU6t19v7-_94PiIXfsUOOs9b9Jb-accIAQtkiupNMRwxhNOIkz1XHGSZqwaU_SDmlWsAc9l5WRyye_FkKsfhnplv-9zvYYvaysz8w3MWnF_hTXVwZx8padqc0piHa0UwgAn4cJstsLSD7sYwcw6xl_SVeqx6M5OOBIUCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVkyuAqkBR8kSO3QEX6EFOsDfziaRkkHKSDpFnKhyJQ1I1jbcNnQblhvBb3MD0SyjVC4aR-HBnZN5mlNQBlyEEyYepE80Ms0eeaq1jKa0QL6hgIVaIPSMod_xFvE9h0pd_RChz5lsoeM3ttWlcpvX-KWoe6bjUrd3Mq-9rKxdqQ2esASPxR0dZHJKvnIMFuy4y96_o9UYL3dp1hjCxUoTXlcDxM_4cvc2MbZIuKGfOs6ksPh0gdadKnHbpJ62kzsDa2UvOa6KfYawE21Ti_fFPPKXGuKd_pRmQVbFU9Bqxl_T5AwIMq3DOlA5V1u73skSQt96PUzJ7hSvQf0t22iPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSmJYcB0_2d_KMJ8p35-JOvhrFu2WorwoB4jGrRabdLUmeoHkpCka781-wARyWXqVi8kijJRFuyIGsJ8zeLVxPs-se_liRiBg3EhgHNeP-HS_vc9W8Fvs3VTkmeVXHVKEjRJDnye0BvNcZVcTwk-vIjw6w47R0ZsFjgwvJpS4x9CvSksES2042-_CTVRYBq7ws2RBkNd48NV-nzaVFa9p9-CfLjq0bCUr1ao7U7qwhMeMD8xo1IQiHA_hHXQkaL--G_DgkGVPBwb0KprRtgvy9bzbszPQAw0Nn9D-z6jNGQbvWSzQsdx87CIbfCAoPne-SL7ltR29aOJwfUcltrTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPu_KYUCafryBUtfxwHXVJI1qp9m6syjqgacIXHB0FKJK9RLALgWvA39lMC6s8i3TZZA7WN5z1Nn093EtYdcQ-LRrutdHROZtc3P7kzUp0a2svrbQ4-ef8rJb6na2nt5LvrN90x-HejQqfgDjEg6Mnmxb2RX1g6cARs_KQ37SVkclloMUdEiTTJ_Cl29aB0HZqKVvDHPY_wCq1h9RtCDuqTcbw7dKtCfsmR-sSY6AsWApsiWUT9pGgktlyLxHm4GGaKUKBrqfCIATD9Gv6itoW_yGwiqdGn4sf75Q3IAk6cEiTLZaB96nuO9sN9FkYsykiuIwwU1-nUpbMXXZfVE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IERmkk0Ttzq-ThUPOq5q0l8UBRfUNJTze8eUEux3MDpCHoMFznVFRdfJU2FOWepge5E9pdJy391iMq4XHG14TrhQ1WsoN0XH5AvAPA8AGX_JwvVnU4AVoh465MDZvlTOlq9Ih1aRoyz4Xxy0gMIno9tFCJxREMpvDn1HbVH1VQ7XofJhii0oqYgp75OJFaXnKQRLrqxtIT0lI4kBPGO1jcK_ePTDlvJffO_Ouyw8kxFRcki-6_fRrYrpQHs1nDh9NWESStqMDHQ0X62ad2kvrLYj3SuSxIyN1mtDHgC5e39tfr4Cbo982FL6zv5aGZVztQ_l9RNmLVfs02Lmv0JF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCpDBnco3aPGXuk6al1SU8Ds886fgFCf-hVsCpTJjcXz2Q6DkGpjGH0QNAtbx4Ybpodym9CptTs0BDzU0oLChiMNAnjqYh00OhzQf2EMfUvLaziZYAeMhpIntFUUwbWCAH1v3Xwzk9aqeYIIpWRIkRMrDA9rD-9SjPZK-0Ph64cGvTcPesXo2tYefqt3NIKffKS0746F8AVJnwMo3uPDr_wtt1AfS-vL-HqChAfdEHu7sk-PS1emDrDiAUaIUGfTxvAyXE135Vj1unkoqOrrLx1N2NptoIj1tDnIwoJPR9qiKKS86rPC1tcgMZEwZTqDt90jv7mEMvGc0a4ld1-Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8YwJV4AKMsNHPm-4eNIMta7BslA5IXvNI_8I0PMy-dtmsMVwwWlIwO9xsNeXGyyAX6NRpWvLhnjkdphPAivJ1jFMUOYyc9V001zPTGWNzoebCNYRR5vei6BIM7NznNtdsqo9G5y-9m-Rnm3D2mQc2R1FcdhjI82wOaR4JcL-s92LGCme55TzYJx3jMxP5Tl8rr1DOyJv6Ijw_8zIHaTHbtZ6n4ebXXckqmGGUFxw0rEVWYvDOxDia0TsvE0B7fVVrlTRf6513OKXGa5xIPAr5Z2L8zj5PO-u8DAPG443GnINKUtZAVwrUivrh-flgkMgO0bxJA4lOHvz1mJLu13DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHyYA9CGVRVV8_R-htW_LGnCQRfq3htFp3mr8OGPB5nPNk_1Fe0VCHWvvbIkCiE6slUED0jjFtmemjyf1M73cPF6ECOFIH__oMOXK3AHq4yxIn1MTRUB9iVwot-E2i9tqICRx3gYZREOLIWQo6iSMn8qpHar4rodJma2AtHj8IHhSzwvwSpWwUHzwVKIE9AVgc7ot9XKyKtQXxzF_V1CdOui6v6bAcQELhwMTQsP4rydsm8F-fL6S53kTQ9YBXchClrcYXyyosd7pED5TbrJjgOeSjmqHPIGwpBZlKOD0SLq4X4DFp92dcIaomC2rHZXzjEgTmLoHw7DqAh37I31NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go9mrGxFMo6MHnSO0GBR_GnZ6X_z2GMFOipKesRdlbOi6EAqAYIG-iq7NfHl7vtyXnvWI9btkjIxgMrJoHtIw6vK0c1JEl3xae5RDgyLXjJQmQcNdR8CPEKlKzPuFV4Pyu2XIVcB5-bm8151SKGso9samshhv1nmdrA1FtJkbGs04i01P2iAysb7BffwYpVNqyM1hpNiaH3IW8Pqp9jAqZSdLkQLxsIOOP785i5lUTXnRmiU0B0B1XAsRHhSfwX2N-c4TK-X09SFkeCPQYH0ObaoxJGxD4LWk1X29ovMFgXYk0fiAcC87J2kYY4eXHdLhmwXnQEf8xWQM10o-Ih_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nR1fMaI0PvuJ6PtZI0kFrM5gTqlyEkg0d1EdGVpbfnJ1e1yL5OI-W5bsLIUoS5GAFADx3zVK9bWDRPIVQ8C2lPDB-CofbAfRqsHlKWt8Ag1RtcgIF3HhdmJvd4Lo15NQrg54n2AL1N_kTr9tLDGxIWBqeNgHE6szjnYa5Ov214z4pUXQ_jHFgaybgM7VE918cWo_XlsFqztGgxAAbu84Jn8Hz6jBulLnNT_oqaQHrS6QsvvDXEayxum_XbthMP5t-VJBg3-Fr2bFMHvwR7xsDOBbwc2ZH_9-JmnjA3HSUkIvpq8lYOYb-nXMThHo2Y56IX-gVsZpsBil23i6c5Se4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nR1fMaI0PvuJ6PtZI0kFrM5gTqlyEkg0d1EdGVpbfnJ1e1yL5OI-W5bsLIUoS5GAFADx3zVK9bWDRPIVQ8C2lPDB-CofbAfRqsHlKWt8Ag1RtcgIF3HhdmJvd4Lo15NQrg54n2AL1N_kTr9tLDGxIWBqeNgHE6szjnYa5Ov214z4pUXQ_jHFgaybgM7VE918cWo_XlsFqztGgxAAbu84Jn8Hz6jBulLnNT_oqaQHrS6QsvvDXEayxum_XbthMP5t-VJBg3-Fr2bFMHvwR7xsDOBbwc2ZH_9-JmnjA3HSUkIvpq8lYOYb-nXMThHo2Y56IX-gVsZpsBil23i6c5Se4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpacghELZxG5rjGaSA8qy4XNlq8RRX9LeEWIGlqONKTlboy48xtQ3OHMUAd_lQwzjH7Vr4IN4PgDs6dfHiWClw4OAyPhZSC6IiL7kasvA2dj-QLSznb1YEBZiWUB4SP3FxRFegUBjjPbTuNrm0ke_8GKWMxuGNY1iEN78WfXWwsXXimwxfPNif0aNWjn6ooGuMxSTMs311Ya-hkxR9qT4qX7bNTr3zeusKkXha_eBhtv8XyRTJXgaT9XKLejfggcaLarcQpyRM1zvXTOSV56EwzbssyUk217OQgOSXUBgo_BgarARAfKKnZftQcC4ve9UR6tD8FUwgXW9QBWoFHexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=MNdJVscaedNBt3OrP1eFvRlJ0fmcHatI-IIYPPLbV1wkTLATfZ7nt8HyrBD4d2Wv0AUiilwcGYLMkGKovPQfhNr6vS6wzXEOENG78HI0bAQIykjZn_6jn_np4vI-vqPg0ON2eDgXWsoW50UCw09L-7NW9-6Hu2Edn7vmkywq8GiD0vthj2M-5gftyn39m0O_1Saw5ZshIo4150S0ImyXrY5our4EWMWg16M_3A1rykkQ8OR0UzfNRYAMIYETw60NBeW6Y3VL0y9WtjeaapH9_eLH9fSSVwZSSMCZSDgTjHJXFt1a9O5EebCriVEqUtGcIMeMMI549WKXvbb6oWS2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=MNdJVscaedNBt3OrP1eFvRlJ0fmcHatI-IIYPPLbV1wkTLATfZ7nt8HyrBD4d2Wv0AUiilwcGYLMkGKovPQfhNr6vS6wzXEOENG78HI0bAQIykjZn_6jn_np4vI-vqPg0ON2eDgXWsoW50UCw09L-7NW9-6Hu2Edn7vmkywq8GiD0vthj2M-5gftyn39m0O_1Saw5ZshIo4150S0ImyXrY5our4EWMWg16M_3A1rykkQ8OR0UzfNRYAMIYETw60NBeW6Y3VL0y9WtjeaapH9_eLH9fSSVwZSSMCZSDgTjHJXFt1a9O5EebCriVEqUtGcIMeMMI549WKXvbb6oWS2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=nrm1SV1MPJqzR83YN9PG3iy9gAxkZvAjOEEh2pLE5ZFZwqP728L6Z1eHjzwbocHhjalTdlfJrEN_ZyozhQNT6yThLUam4Yl4OsvJeLQiN9w5b3Uxkbly1nQ929nQi4HvFfDSgHRrfkTAiD2Iqh-_-djWCLh14Cw0XbH4Yzv0bGGFrdL-TZ1RvYRRsPc0_kIdNDpGq6VBHp057z6T05GuU6HZ1wV4_7P8P1SaXAJ_ZjdWajTi10htr3K2dMPM-wfWTOzt45TUxkHmJIg-1EUIlZN3ZMgWCRH6NqAe_GDiUgnIdQAXNpIPp0gvKu_qR0L3ElkryzLygKyHGfO7lFKRxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=nrm1SV1MPJqzR83YN9PG3iy9gAxkZvAjOEEh2pLE5ZFZwqP728L6Z1eHjzwbocHhjalTdlfJrEN_ZyozhQNT6yThLUam4Yl4OsvJeLQiN9w5b3Uxkbly1nQ929nQi4HvFfDSgHRrfkTAiD2Iqh-_-djWCLh14Cw0XbH4Yzv0bGGFrdL-TZ1RvYRRsPc0_kIdNDpGq6VBHp057z6T05GuU6HZ1wV4_7P8P1SaXAJ_ZjdWajTi10htr3K2dMPM-wfWTOzt45TUxkHmJIg-1EUIlZN3ZMgWCRH6NqAe_GDiUgnIdQAXNpIPp0gvKu_qR0L3ElkryzLygKyHGfO7lFKRxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Mt0d69ri3YA4Wvn0jsPbxPBWlWm_x8LOa6ag8TMKmgpE2yz-3tcRBDE_3umhuBMa0DkrSm8S5DHEiT38kG9vJTvGgJXiAuRCKRzC08oFcg2zLHib3OPcXsWmxUFsvsXcritaUxM5O0mgcaRhIyf5iF2gNKbI3UdTD3OhSnx3Pvgv0JedcozxR5riXe2KTqy9MUHqRxT1dW5nd2VQrbV7M7IjVKZ5GnMR0_CLcdsMc3Z0JKt1oGYxO56SqMyHBtcdoWtwjb3pATElcNMuaKJ65GZ9YvGqhg1lyH9xLbd0D3ri78hgqaRE6cWx4y57MU43br9Dn7svNEKA346jgTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcblIuLveXfRV_j8u8rmndUvETyqVAOwiJlqDyhu_Z0NeiPLvmV9V8JTiS6TKdDSl8PoOSJxyCJ7PzzSt9grlJbPILqmByfXqA8_pERT5xLw7CK-YPQhQ6susKeOJrMFzMfLN43rT2y7ev3VBRns-zOKk540EJCWzXsQBIPRDOUrxWjBuOO30qXI46nThb1TM2FnZIsDbNfxRYE7N4NAgAmM0-tZNn5M-BrJXf3uQiNnJP2CtHc0gtbrWBE8OR0KgmIQMwWAYZxtrzCJL1heD1i3tRKwOjpbjaxBWr6TPQfvW4CM7CLmdt3yVLQ8SysXdNTRmcU5WuaIxxmCjl23YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
