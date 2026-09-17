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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 03:29:40</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGcTFHTDm5rs0PQm4WiNL5cWFg-0IUOmz5FUZ4-lTaBjlH21xlcjdOF3D2y6-r59f-9SMA7Iz9p1elb6UnSp6VZriqDOXAyThTHfFwIH6J_BrR9IPDec0A-FKkAIn6d8rw_Wp15PdOmnnHx_UbFPwBAuYq-ByIgr4Du6XW7aA-vbUCo_J1Y39bxM0XwZclqNI04kW75GSex1P1x3ct-GmUztW0xkOTS4EU0NnkF3jUTYu26MCXXehD_6M4eBEfbzaV1xi_JmuKPqj4Fx1ofDPCMFVi-mrgY-p3JbIwmsYVaBuNiznX4wTGxgDmnb1lhdWuNKcD0f0Nrm66q5Kw0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0hQcdAe-Er8Ch6T8Pi5fXDj0ReIZnLfzzJV3CmfdUD7C5cGwBClZf_ZWW6A0LwbIdlJEpqzcGY11WwwjM1ZJ9LhU8d8FTYLhaAb6nD3cuGThwU-wcpaHOSIDFIbWOSs0fP05Yj56rhBK6STrZKwOl0O5S45MxwmILdnLmxOEbETBtiE1nOlly2Xhi2JEs3M-7FT__DiKKxSgzPnewND2GXia22YYTQ0tJI5yvdy7eXMY4wb4FpMd6DmJsJTrJN5QXm50wT4VwTAuNz6aKw-cWT8bNs_Hm_N9w7H3-REguS4KtIvZstiGqLl93RUnqTP7fmq6j8BVLtlY_cZqW76Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX6mKjU6CBm9VoY03IWK6d_4syPbXAuJTKMW9yGfkl9zyqpnDitZutV-bzRrzLWyQdtaBaa4gCoVt8G7vByiCMvmDOXF4mEeV2_eAbr9jykANHV_8RFqyAP5IOICzxbrNUeuXTte_f4zRhChjB5jrPV92Ji1PVL5MkIygek-K42Rvs3CNZ_1yxUp3bPEeTgg5eTYqukrvYz98rHz-6LC6tajwx3HDo06XVaxMjg8WHu5twnzBTCG-ChtTdDg6aMuf-pu6gHaWkdLc541MxmRmtkoSY1GJs7-P5VMfQPCJF7PJ__B7DeqK5znMUyLz1Viut4W1JfrKi1Xo_lv-YpF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHx64jqVOQsibxvmxecEi9EBgNJbrBJc0iOFpUN1JTlqUrm9JAt2_l8JOLz-MbB5eSm_2s8JwdhETbilzNE8LY5OzDsbPqnKvgr7pbSHJBuHAdMeBt0u2pMLLLKfAlUPQJrVm6OlqlWq6y5QZunHRotrfTBiKbS5LZeWeLf2-j3GH6P0Dy_YhfVdbzQ1EWYWX8ovVXpuoODnN_y_DMOxDA7qXqnZYQ2K62QGK6VTOO1l-xTNVrAIYuH4uyUXcFLrtFZVtc3c5KJyxV8hzXQJciH1uZPtjtpIR_3UXEm60S3sklLvXHLvyoZl0gbvmAmiJhEHqSBZ1AhYZVv3C5--5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnOkKG4KBZ01e-18LYRzIZD5W21iLzodyQ9iNGCVxCy-_sYzatc-1t488Nj7n6WPsQByZuLDgdTpYwUZYvNlze3xjwVL0fQxBJWZfeqHPg9J-1jsvs80zPmaLdqSewjRCawMTjzwithO0CAiy28ullZ5IauCGOGRjVDTU_NJt2E0rcaGMPlcWWMtXzSXpf6zgG7bqCvkfPmcfB3nPnB7WExDfVsaTo2OCiHpI2iT1g7iWpmY7aA4PvHj4MInzlKX_ZnS8vcI5RBxJt-OgO8yBHd2J1Iz3lVr2EywqnV-qMzcDggjXjZazPn76D8bNce-zQ0wW871TleyLsQdUUq3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b__bqLa4Za7xoc3f8QC_JIfDblXVMDUTBHShfOjHQp71iFYI8WOvJfyzyzLhufFmcmC34ByW8c0PtTYBCVqtrMoT3QI_cPrOEK3XqmAT9XDMcyDMLWsnc63dM8JbBM3BUsHltKCdom62Q92WaQdyJMzsTMeQ4jnGoew5ERSI5qedjpOndDxo8E-10zxXFlUDVgbqGqNGJBNAQOI0M3SrS6JGmGR_IGWjHJXMinqn6GpH7wbZ32h67tb8rJmH3D-fyFi0YfSh4ycl4dBVFJQu5gSqaRIA_hSTx47WFYDND0IRAYnINyy-T3YNlGQGV3ph9aRliu1fskZMlv98My6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=AXFTzo_LRpby55Pu_MFbsI1v9lqQyRBhXjWM7DKx_G4bWiRyrrRy_8tpTsoCVzXYSbn4GWKwEqlBfQMKTFEAbNkYV6kKR_ldq_9RWCC7d5FLAbMwUjg2zPMb5AZWjKEvai9hf7c_0Ezm4pAjkr53WXa6Qfa3xE8xFy2PlJwW3FKovSk_EfqaXnrcMLMD2Ic4_ZGhqGD7gH5dluYKNDBWVf6i8DU9B9le-x1y9Bf4tpu-yp06vkEfx_VImZSjj9tUtP922pwz27Rd5xMCWi1BwcRcXQi79C6aFli-ADQJzco2mgNZntmyC7X5CrIqnPGyhgIQEWwpnwxC19lggDCz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=AXFTzo_LRpby55Pu_MFbsI1v9lqQyRBhXjWM7DKx_G4bWiRyrrRy_8tpTsoCVzXYSbn4GWKwEqlBfQMKTFEAbNkYV6kKR_ldq_9RWCC7d5FLAbMwUjg2zPMb5AZWjKEvai9hf7c_0Ezm4pAjkr53WXa6Qfa3xE8xFy2PlJwW3FKovSk_EfqaXnrcMLMD2Ic4_ZGhqGD7gH5dluYKNDBWVf6i8DU9B9le-x1y9Bf4tpu-yp06vkEfx_VImZSjj9tUtP922pwz27Rd5xMCWi1BwcRcXQi79C6aFli-ADQJzco2mgNZntmyC7X5CrIqnPGyhgIQEWwpnwxC19lggDCz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=U5Afq2-toAcmMJb8d2bD8l6888aZ2yYaKcr-CC2ykPNFzA40aNvNVPHbcHX5w8-9X-hQO3qtiLoLIF6PEjOo1UJfzbRDjvnp-pPzWF2oCWXtlBCj3d_QBMBLahEmsoUJw6ouJ_1qJwnHW9hqeW4Wu_4mRteozIB-H4t7CGXxemTCxugiD8W5SqX4yCS_UTYCxAZ12OAgsxBqIDec270dQz0csoEdQmGSwiWISixFbcaBWypZBJ3qWnnQMNTxdYGGwQ1gbvPIwPAosPm9Xe077XXpcZiNLUXYJ3tfqxPnzi3RePvEBgjZL7p8Py3l6W-wlNRxycDGHexSub5BUOnBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=U5Afq2-toAcmMJb8d2bD8l6888aZ2yYaKcr-CC2ykPNFzA40aNvNVPHbcHX5w8-9X-hQO3qtiLoLIF6PEjOo1UJfzbRDjvnp-pPzWF2oCWXtlBCj3d_QBMBLahEmsoUJw6ouJ_1qJwnHW9hqeW4Wu_4mRteozIB-H4t7CGXxemTCxugiD8W5SqX4yCS_UTYCxAZ12OAgsxBqIDec270dQz0csoEdQmGSwiWISixFbcaBWypZBJ3qWnnQMNTxdYGGwQ1gbvPIwPAosPm9Xe077XXpcZiNLUXYJ3tfqxPnzi3RePvEBgjZL7p8Py3l6W-wlNRxycDGHexSub5BUOnBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qoDx7kXwQgjAVsjWAI-6M6qKDYrgdAjMa-zBt1pqt96AvxBxBC8XquFiwYZwpw4ifEzGwaej3PSyQchVoLvmvKjuEwn5jJXM9zsJ-1Qb0Gj3IDtrLXiWVt0nNSy7HM_zJmj95V8F0T7IQX1wlCh38iBm3L1joPNdWxXWVjtoWUwBULLOxr4H33hB62H-1IUixUHPYC3F1iOqVJZz_i5UsI5SICcQ0WKylY3UmjLRLvk2dYcB4ZQ14oXczvJmA6Zin1wRpFaMqIvQCPuNIO1s4YuLRfjAb-8DanFW_neek8kvzP-gM4e0fILmA3_H-u4mUWxG3lY21QF5Ui7RH8nCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qoDx7kXwQgjAVsjWAI-6M6qKDYrgdAjMa-zBt1pqt96AvxBxBC8XquFiwYZwpw4ifEzGwaej3PSyQchVoLvmvKjuEwn5jJXM9zsJ-1Qb0Gj3IDtrLXiWVt0nNSy7HM_zJmj95V8F0T7IQX1wlCh38iBm3L1joPNdWxXWVjtoWUwBULLOxr4H33hB62H-1IUixUHPYC3F1iOqVJZz_i5UsI5SICcQ0WKylY3UmjLRLvk2dYcB4ZQ14oXczvJmA6Zin1wRpFaMqIvQCPuNIO1s4YuLRfjAb-8DanFW_neek8kvzP-gM4e0fILmA3_H-u4mUWxG3lY21QF5Ui7RH8nCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=a6yGUIquzq1_whhwjofjGRW-xySnAt01KpI5ZuJ47V4Ed7qXl4CTcXXqUy5CLpFqUrjnodjxs1mJQfhCKlrdiu06vAmYvvsivEYq-1Lgq0a1FpTLyA0OE6qgHuSF5TZhBv248noSll9uWueQ6dr8-AZPOdotHdESTEHcok4DePHnZVc1hqVGgbFBEULIeuA9oepnri3ZE4bvF7zobW31wcpAFJa4VrH-GbqZx8ZCJ_sE136Klugzgzk4h0-REFGvunCYtu-asGNyHb75XFfbBYMM1tPn9uqL37UVHd13g7cbgFQSVMKyuyEPiud4v-XWuly4I7zyTjMVHqPJ0RVLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=a6yGUIquzq1_whhwjofjGRW-xySnAt01KpI5ZuJ47V4Ed7qXl4CTcXXqUy5CLpFqUrjnodjxs1mJQfhCKlrdiu06vAmYvvsivEYq-1Lgq0a1FpTLyA0OE6qgHuSF5TZhBv248noSll9uWueQ6dr8-AZPOdotHdESTEHcok4DePHnZVc1hqVGgbFBEULIeuA9oepnri3ZE4bvF7zobW31wcpAFJa4VrH-GbqZx8ZCJ_sE136Klugzgzk4h0-REFGvunCYtu-asGNyHb75XFfbBYMM1tPn9uqL37UVHd13g7cbgFQSVMKyuyEPiud4v-XWuly4I7zyTjMVHqPJ0RVLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mzurkc8IHT52XdXb0HJEjwEE7niHv1Fby7u6-qE3diO5HHQyMHDwDtb0tdp4-tXLIS5AoN4WKwniHaXt-in1j6cPCeLfjooA5thIBspDvKieZDK0qfkC1Pm7eubnaEV5OStyFwDTBE3gfkXsQiIS9AL9Wc4P_Hm-eJtKvVRUoG34ozYs66-LMh4j_IH0CXz6hJ_S3hR0teSCGaTZe6_CbJoEDQQqgelyDuj-rjaKdV2Lvi0ETL5PULhsJwi-FLiZTzXan4q4eWhVdmS84xVXFYk4GpemrgAQ2ekEb3noNXQLX2RahVf7SgUSpUZwumh3aLDULmb4OIltEQ0TZndwMQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=MbslnCmX2IY0cdSYwlrzoQ2LGzutxZHfubMzzJJo1Tgh-zXL_Ftn9YMMpiicMQA6Jk3hvbIfByB_FgoqGoAUMlE9IJRBQ-MWOQ8VQlnyeoM4G-pvBY09gdxLWb-mQitqM60-nn3laLpxlp1Ph0xKuo6HiQgDZ8Zvj69Y29UT0qCKeAAGRw0JAb8icnLFxgT5Fhzeuwlnwakt4J7vSznxF0cBNooZ8EecTepdZkZRZ6Vm7RAxsY75l7vLrkD5B363Fk0ZkNAY2LiqqN9UiGALmPAVtC1O0HXulfVt7RuQotmvRi9hUgvuffCtrxjjFwQEqKx5Qf1tWUr08DQwkt_CNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=MbslnCmX2IY0cdSYwlrzoQ2LGzutxZHfubMzzJJo1Tgh-zXL_Ftn9YMMpiicMQA6Jk3hvbIfByB_FgoqGoAUMlE9IJRBQ-MWOQ8VQlnyeoM4G-pvBY09gdxLWb-mQitqM60-nn3laLpxlp1Ph0xKuo6HiQgDZ8Zvj69Y29UT0qCKeAAGRw0JAb8icnLFxgT5Fhzeuwlnwakt4J7vSznxF0cBNooZ8EecTepdZkZRZ6Vm7RAxsY75l7vLrkD5B363Fk0ZkNAY2LiqqN9UiGALmPAVtC1O0HXulfVt7RuQotmvRi9hUgvuffCtrxjjFwQEqKx5Qf1tWUr08DQwkt_CNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=mHFXnfGTwH6ngB4EklKjn0WGARa-WYVscPTdsP9_tpHxAVK7qR5I4mTX0ZzUMfUGEQeT50ry8hC84wAw73PKGqmcQvOd8ofYzDUZIz90o1DrDZZwJ9lrRq8zY_yfTx3A9rGO6gkAMRlPw85rTZx4NzfbYdej4O_d2dAPUj92CXf7sGk9mIeh4fhPy5olrmeT62jh3R2n7QlZLPWZ2CrId71nODJOiCqRFp2S2lvzGfYAYEoCxvIXWPmTApWxRp0SzP5wUVATlfY_ecHcyCUAHaXH7I2Izt8JbIvqvso9RwnlIfiHogDzLe3mfTQmKbbJ5jmM7nCZAfY-bmkdy8zQig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=mHFXnfGTwH6ngB4EklKjn0WGARa-WYVscPTdsP9_tpHxAVK7qR5I4mTX0ZzUMfUGEQeT50ry8hC84wAw73PKGqmcQvOd8ofYzDUZIz90o1DrDZZwJ9lrRq8zY_yfTx3A9rGO6gkAMRlPw85rTZx4NzfbYdej4O_d2dAPUj92CXf7sGk9mIeh4fhPy5olrmeT62jh3R2n7QlZLPWZ2CrId71nODJOiCqRFp2S2lvzGfYAYEoCxvIXWPmTApWxRp0SzP5wUVATlfY_ecHcyCUAHaXH7I2Izt8JbIvqvso9RwnlIfiHogDzLe3mfTQmKbbJ5jmM7nCZAfY-bmkdy8zQig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=t3Dg59laKR6jwoAtHV6FpuHHY45SFTpMMC6OpfXprcmUHQcJLY4ZSRqjzA8-E7ZFizVKDCfRNiMq8xuME8MeF09laac9wFUfF-8Kci_pLHr-qhaq9PZ0v7zisk6b-8MKtrJR9HlohsKHTeixJ8Dj0xuKQjrvnXFE-R9er2PmbqzBwg7ScMrAhcZmv_rGg17EVVg5ITPEAWfm8A_J3_n4tUkc56eYwsvjewEYbEfyeTuxTdas4kaFozbKatOY_idTlCjLHkpgFnOVEkRGGaKT0EXdVQbHz-98c71wxtGz6V-sghtmn_KKfzmLMaahtcUbE4jGooW1AFwGOaVD6f14SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=t3Dg59laKR6jwoAtHV6FpuHHY45SFTpMMC6OpfXprcmUHQcJLY4ZSRqjzA8-E7ZFizVKDCfRNiMq8xuME8MeF09laac9wFUfF-8Kci_pLHr-qhaq9PZ0v7zisk6b-8MKtrJR9HlohsKHTeixJ8Dj0xuKQjrvnXFE-R9er2PmbqzBwg7ScMrAhcZmv_rGg17EVVg5ITPEAWfm8A_J3_n4tUkc56eYwsvjewEYbEfyeTuxTdas4kaFozbKatOY_idTlCjLHkpgFnOVEkRGGaKT0EXdVQbHz-98c71wxtGz6V-sghtmn_KKfzmLMaahtcUbE4jGooW1AFwGOaVD6f14SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=lmlS6LQGY7JCQUy2gAdhDjC2yErUjymp1QGLhgqWLCX6XMMKcGIWrdi9Ww6c9SAKrI2D43VfWhfjxfojxIosKznGtc6RuM9VhJz05BvfPXtFFQlQrcwKjGaitX1UzMyub_DUhb7P_XiLx1tLgMLMzrEw3ccFbKX6ToqBt8D26Z6IrRX_-hCxzeFqZyTYVA_xzZ8RR4tF8jgvLJMzcm_LLrYvsyV5yO2r5CMfliHmXm4tcKrFmrwJm5TiotFY3wZkbc1csjP6QSCtnWRtfGejY_ImnkE6QmCInOy-bLlQDen9eJfCo5gsor4B0J4rLdb0t1APumddOECuVMierKmkwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=lmlS6LQGY7JCQUy2gAdhDjC2yErUjymp1QGLhgqWLCX6XMMKcGIWrdi9Ww6c9SAKrI2D43VfWhfjxfojxIosKznGtc6RuM9VhJz05BvfPXtFFQlQrcwKjGaitX1UzMyub_DUhb7P_XiLx1tLgMLMzrEw3ccFbKX6ToqBt8D26Z6IrRX_-hCxzeFqZyTYVA_xzZ8RR4tF8jgvLJMzcm_LLrYvsyV5yO2r5CMfliHmXm4tcKrFmrwJm5TiotFY3wZkbc1csjP6QSCtnWRtfGejY_ImnkE6QmCInOy-bLlQDen9eJfCo5gsor4B0J4rLdb0t1APumddOECuVMierKmkwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNKHCLedchOTN8IgTBh34DwdwH0mrOpnfHHEbcvadB6UpgyY0325OAjlSp9VDOpsNHcOb8CzEbjb9upscFGjw-ooOitTrj5Pzy2YLFxUSaODTFar5o9y3me0sSZ-7OY6YvZI4FkZgiGvqi0xmzMzDVEHdWlH7ConAcViGZ8sWposz7zq5BwydD5t59a_2sqe-w78YoqY3m9zObepwe6WoxXRQfdr7BU618y_aOk86rkyjF34Yo2dyeLZ1qmpxpPUx9nYUkBDEePbH-kt_7-2p68Z4MZK97s4WUgpHji9ZiCBuVouDB0Fqi5yrJqDgurYoVS7p1FpzSjiQfMMInMLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ICANPR6bq5VwKnKOpwcuTjTxjFRWEQACjz83jyXA2COJb-MP6i7eo9KN-8dzuxDq7nizxY_4n9SgObpiIenWtLzxvKMvkwJR1aRzX_A7wSXd20RpDCs8gRkUWljIMQpN3mi7Et2Yl4oeLCv1wOriFfuHFgY6IqseG_yckG6i_riz67OtapeTcGAKOCsl0XBJw34pzXoUTn9BLUmBlHiEZ1Gn-Xcf7V_7-lmiPDJjZCzkeiWzL3IcwoxAjAid63kio_Nmdz3z8S30bLFSOrhRhw3AQstIxXlBh0HyLOpTsSNV0CV8UmCVmkMVcWmp0iX9g_hzROAy3ffawo-fZLiz6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ICANPR6bq5VwKnKOpwcuTjTxjFRWEQACjz83jyXA2COJb-MP6i7eo9KN-8dzuxDq7nizxY_4n9SgObpiIenWtLzxvKMvkwJR1aRzX_A7wSXd20RpDCs8gRkUWljIMQpN3mi7Et2Yl4oeLCv1wOriFfuHFgY6IqseG_yckG6i_riz67OtapeTcGAKOCsl0XBJw34pzXoUTn9BLUmBlHiEZ1Gn-Xcf7V_7-lmiPDJjZCzkeiWzL3IcwoxAjAid63kio_Nmdz3z8S30bLFSOrhRhw3AQstIxXlBh0HyLOpTsSNV0CV8UmCVmkMVcWmp0iX9g_hzROAy3ffawo-fZLiz6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=d1LZfwcwDSPEIoCmxZeHa-Lh-Mu80Lvu1vhJ-jxcg57nYl9BrbKncaRrM-1paKvJSDkZRNsxSfdaVZr5x4MgZg6E1tCefr0vm6QjolV_CmQwKo49RpMNREtVEl2_bbyeCEXbH4y7fXkhu78iWZe5Zi-qpKNlKJFfAdihu_gDZ56TPUuG9Wud1n08GSIew_sO_BJmI_8ukUymw-HC_5P1zw2MNH4jsH2VBuquyePQlsyN6oEZ0-_wOii5l0VeFFirTzL6mEekOBaqCjS2NifpiN_xmZkTOqQAKFYj_PwLC4ZKScXQ20WvRcw2YPFzLOkl5RUDUhLUX6h0wCVnwvkR2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=d1LZfwcwDSPEIoCmxZeHa-Lh-Mu80Lvu1vhJ-jxcg57nYl9BrbKncaRrM-1paKvJSDkZRNsxSfdaVZr5x4MgZg6E1tCefr0vm6QjolV_CmQwKo49RpMNREtVEl2_bbyeCEXbH4y7fXkhu78iWZe5Zi-qpKNlKJFfAdihu_gDZ56TPUuG9Wud1n08GSIew_sO_BJmI_8ukUymw-HC_5P1zw2MNH4jsH2VBuquyePQlsyN6oEZ0-_wOii5l0VeFFirTzL6mEekOBaqCjS2NifpiN_xmZkTOqQAKFYj_PwLC4ZKScXQ20WvRcw2YPFzLOkl5RUDUhLUX6h0wCVnwvkR2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q72wrFSSylsSjWxuYQRbRouSUxvYdLxiFzu95_uUchgWxSLvk2UG9-U7D9cabNSI3pUHGlCz1flZAzUjRK311LCiQEQ2ac4eTf-phI3zwK1UzkSJ94baRZuz-XBXNvL5bC8RMSzB-figtjYAH2aalOfJUHqDJ4v4TeAtVk_9t4VsxvVS4E9sUFvq3tcLLoCp4j7o1vRTPuGZ3ID7ed-m6b5y1m41ecJRu9XuiBCrW4Nzl_9KuNefac3z_PFZ2vu4Ovq_DT6cHQ5xzeODfRKHs0eqk5HXs0x-XEsdXcN_dq5OCqlIWoNgKll2APc--SLyo1ASP1vrXRW_GKxGup8NKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3VPMSb9B4k3MZcWMRq7RbTFvUrWlM9gRjqJbox-gasQe-CoSTWAg81zesFW2OKBUJs9GBpwLH6I_N2CVaIJHsu5PpvoLbQTfiJf7P7kPxx6Q8nRVjaPR7M36JHCcOwEwugk24RkTu0tcdqt1ApxA4c1ZENoY7-PEb0dvYGk6-nPBkIj9qUZKkjl8g1j0fmn-uNypQAt0F25ofDbzgX-tBV0j_oBW0DBH4BZRIypxhV_-QtjsYMC_51GojklcgHLRZQF8eoRkWVQCJYR9XONpFUYmK7oLR9gdFe7-j4cQN_-5XbGaVJ0QnEB2DgihqMuQ-85xz0ssUKEvzphjAsyQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Cf4ak6cHvy-Wjz5IUDw6_lQgPYo2WLlF4gSjhaklQ-LGq_vSgMQBtTBxVP0b-L1gyaK3qnEe0OFo6hnTmc5upMyFaDB9XRn-Ck2Z4FIN2ZHN5_KAPYWfBBbqLBhiPB9sf2RqZcEjP-6u8VXpacDaKW_K4jL7ojsyEL1DdFCKAxsSykobHt-7hoPmYAHxIuGfGTMxb2gBBqCrnQtovt4Gtk4XPtTlMGSI-a_DYaMVhYmAMvX1Ctgv_dUeOTYLlUvAUJsFMr33-ItF-CKS9VwVdXHbM5u8T83XlP7Ornp-AdcfMbgouc5Y12IwspTCbmtYx4cTVYiObhry3kAwucshqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Cf4ak6cHvy-Wjz5IUDw6_lQgPYo2WLlF4gSjhaklQ-LGq_vSgMQBtTBxVP0b-L1gyaK3qnEe0OFo6hnTmc5upMyFaDB9XRn-Ck2Z4FIN2ZHN5_KAPYWfBBbqLBhiPB9sf2RqZcEjP-6u8VXpacDaKW_K4jL7ojsyEL1DdFCKAxsSykobHt-7hoPmYAHxIuGfGTMxb2gBBqCrnQtovt4Gtk4XPtTlMGSI-a_DYaMVhYmAMvX1Ctgv_dUeOTYLlUvAUJsFMr33-ItF-CKS9VwVdXHbM5u8T83XlP7Ornp-AdcfMbgouc5Y12IwspTCbmtYx4cTVYiObhry3kAwucshqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1YWls9kMRtgGlSfSVfuphHA_oQVqH9flvV_Ubz-aEXbndnGizKvExNeQtqhnn7YY50NIeRHbByxwWHWAitmJNQmlbVN2nHfPe2odIW6BTO8pt1HZgpcIVMAlyNhzDH_hfDLOHhQ9kR9w3hYc-JNL01E18_0wE2YobPrFlMnkWgtaRQOq5MIS7_PZD7yGzoTk_4D4_l2Iu8AnzoyKRmU1xAFX32vTb2byMHMlzzc8EgBfkIKt--VG3gQts1-tLfh7tdMhrT40GRRpZOgMiUYFLxCNXBUOE1QWQc3zSkTwb_wjE72gYocMELaaWELsuh2rD5ocyx1ESsPDL_3zfAKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAjTFfgKVRSCcj5ZEwvYA2ETAqYyg8m0Wg3-PZuyHiWNI8phEwbhKOv-vyBOayvTqE_6aqXeCneaXmRPEvMCIWx0h4S0CgwPwMZxm6o6jKEDS6-6JAdQUPy9pjy5YTtFWfdDN_ujibKN48wKk75Omhn-bLruOuzr6RxEKGCr8dGdP1le3hs2aTZk_aqLZpbn0O74E20u-kQk-2DbM7oqHQICsmrPC2ZwrZ5gxf2ZNlinKEZ2VTtvSxKJXcQw2veVSEeXQg-sSj2CkgTKFwXW2-o9K0dTTqSg_KKND8psDqvBF35vJNjTNrHebIY2N7NWUZf8KX7n19L3ofaONJliCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwUXwnRex172JR0S1ZrtNPDsvcm00E-lovpdRI_WKkVmiRCD61RxDru9aifX-3__nBA4dgwBam31ApjxJJpzhRW0YAxMZutpwHNJlLYsI0FddcmJIUBDA9Il8Sqj8p5Uqayp_QK-69kCiC5H22Km5gnhhYat-g_j2dJ8GTGHIViYpYv8oFQP8hscg-Ptk7qtUSjFkkLpNN1bb8yh8BK0FKeR0Svp1KxuzpKzBDpLZGznvSu1XKTOaKcY97CaCJGiBjHQjx9QOTl3iikzGJzWldfFzo57Mkh4XBk2QmcVs_wdRzKcqoCOcHKotIUrgPxW6D50t7kT2kkpZ91zvqEwpQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kcBkTBatSZddOk2KZ9CVJkt-ETNxuOWdIB6c8z-eZVgpETtMIqVDFEg39UWYYGgSUEOaApNTU06U0UVWaPwTU_Gjaeq0LNVClZcLVTCHiqhWxbUeMkL_S92X1Eis5VLmghxj-C6J-aVdhi30uSJQhxtI_ZITwh1lfkVh3o1ikf-l4nJVAy0-QzNOj6fWA2qwZrF-1WiWyCMmzRrWh8vd931wKnU1HrfEYJIp0ERTlrfjXBVuYyMPszTIrowaVYgJl8HB9QoToF5v3XjzLuhNPAJ0khzAMd8yxHVXY651wS0Xlr6uhqfhBwfqUEBOkyxCDCR2DldE2IGB4zray_eRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kcBkTBatSZddOk2KZ9CVJkt-ETNxuOWdIB6c8z-eZVgpETtMIqVDFEg39UWYYGgSUEOaApNTU06U0UVWaPwTU_Gjaeq0LNVClZcLVTCHiqhWxbUeMkL_S92X1Eis5VLmghxj-C6J-aVdhi30uSJQhxtI_ZITwh1lfkVh3o1ikf-l4nJVAy0-QzNOj6fWA2qwZrF-1WiWyCMmzRrWh8vd931wKnU1HrfEYJIp0ERTlrfjXBVuYyMPszTIrowaVYgJl8HB9QoToF5v3XjzLuhNPAJ0khzAMd8yxHVXY651wS0Xlr6uhqfhBwfqUEBOkyxCDCR2DldE2IGB4zray_eRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=jH9Pkb3pgmIF2PkQOb0GDcolq-5neEOHZU4Ncs7c7hZdKEjI6hBlzlLokNL71FqLVorecZAKt1XSC005h-cbQYegndFYTq59t83f9VbkG1g_bj0IA0dNYOYBG4lgDTY5rW4MF5XrMCb7TFob_Ohq4vaFPhDiUZ0gnYoQcKCGQ_b5axQKjX3wbAUlAyuvZmLldifwDn0WSJmIC0t2GdBv4FRNETx0j_gDHbdQ_83XJEVNdhkswqtbhKtOU2YJWVligAea_Y6HL_cuuJZSiIqhisFDCQYW5nsni2P-dygVhRlldREycgalklI1gRRpT0by7EHXWDIzNU5rrxRp_0dgag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=jH9Pkb3pgmIF2PkQOb0GDcolq-5neEOHZU4Ncs7c7hZdKEjI6hBlzlLokNL71FqLVorecZAKt1XSC005h-cbQYegndFYTq59t83f9VbkG1g_bj0IA0dNYOYBG4lgDTY5rW4MF5XrMCb7TFob_Ohq4vaFPhDiUZ0gnYoQcKCGQ_b5axQKjX3wbAUlAyuvZmLldifwDn0WSJmIC0t2GdBv4FRNETx0j_gDHbdQ_83XJEVNdhkswqtbhKtOU2YJWVligAea_Y6HL_cuuJZSiIqhisFDCQYW5nsni2P-dygVhRlldREycgalklI1gRRpT0by7EHXWDIzNU5rrxRp_0dgag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=oTxnNfp8Sa-SACJX2KbmLQDJ-WW-1Vp17QmKY_WyXBuM6ShZTsNKj5TXZpyXnzPCrc2dADOdkrsy5FhJT-nfNJzqHSBP0qSo9whiF4Fi2CwoODMLqMzBcjb3vI5fjOJrxGZHZXHfnWDLF77w59lThm8kQMQW3TW9IEX7yCEPc2aEigaRmoheC4_Pv8FtFNf5rKzMbdDak9fyN_QG4NnAiw6xEGHXYr8mI6Tv5AwiIWV1Qs7Pth1tcdhcn39bBelT2zt4ITvM5T1q4ZC0jngiK8Yp3oke-tLMtCuo_IxuGqIFPV_jb1KEpGUtGHAgmmvbuARBX7ATkhgpoGbUOahzZ0XFpcUA0EwEyeXnSKErHaxIFdBVRsIODewPlTz8J5RkLYjNY0ezX8qEQlrxFtW73FJwwa-lmU3_CF3wBxAi7FtFOSyW6pCh1pxz0rMj90V4XbLWQB1TW4_Xi4SoU7JF2L-KrKvE3prtN8i2nlL3iRVbe5R-Aof3IlDA4v5ZlS3GjfTpgNQSsOhuVBrm1aKY0Ic60KacnzIv2IHiledeo2VAuTnqMXRuPqHKAvjTIpb-ikDAXhtSHJj51XmPmiZOxhwbpXpIetHgVjZ2FDmI5kLqStAyJeZ8eNWLQ9gNjNVcf1eHaj6He_5pOdQE5KNvCc9IjtrtUKcFs3mUVQw5ceA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=oTxnNfp8Sa-SACJX2KbmLQDJ-WW-1Vp17QmKY_WyXBuM6ShZTsNKj5TXZpyXnzPCrc2dADOdkrsy5FhJT-nfNJzqHSBP0qSo9whiF4Fi2CwoODMLqMzBcjb3vI5fjOJrxGZHZXHfnWDLF77w59lThm8kQMQW3TW9IEX7yCEPc2aEigaRmoheC4_Pv8FtFNf5rKzMbdDak9fyN_QG4NnAiw6xEGHXYr8mI6Tv5AwiIWV1Qs7Pth1tcdhcn39bBelT2zt4ITvM5T1q4ZC0jngiK8Yp3oke-tLMtCuo_IxuGqIFPV_jb1KEpGUtGHAgmmvbuARBX7ATkhgpoGbUOahzZ0XFpcUA0EwEyeXnSKErHaxIFdBVRsIODewPlTz8J5RkLYjNY0ezX8qEQlrxFtW73FJwwa-lmU3_CF3wBxAi7FtFOSyW6pCh1pxz0rMj90V4XbLWQB1TW4_Xi4SoU7JF2L-KrKvE3prtN8i2nlL3iRVbe5R-Aof3IlDA4v5ZlS3GjfTpgNQSsOhuVBrm1aKY0Ic60KacnzIv2IHiledeo2VAuTnqMXRuPqHKAvjTIpb-ikDAXhtSHJj51XmPmiZOxhwbpXpIetHgVjZ2FDmI5kLqStAyJeZ8eNWLQ9gNjNVcf1eHaj6He_5pOdQE5KNvCc9IjtrtUKcFs3mUVQw5ceA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=r2qbQTxrvlK-e5fRl3ayJTkudmuPZEuLjYpXEi2tigtyO7lHB67hVjUDyhXpENxEduMo2UpmtYdfNJBAnjsyOBosvAIGbsGRlizPn_6ysi1trZHWBJQyBIft7bDhC3FVCYOG5EfPF7zdUeJOLpCnIxyuY5TZ-h2MC7N3Tf7hIsjdUGR-byV2-UuL6sIY-DXeA7DZueWPRMY6WELzejmhJbTTY96j1iMJ7Ecmfu4BdZH5_a3i7pAU0x2gzNxlTYg5o8PvQjlyifrjkqwZbLq4Z82F13CYynALh5h5-FGnAxtEafdIhsu309GTzr6sJk6q7MB3HL_N8zfYRf1LClyUuheu_Z6-SRKRhQR0ZEcATc5dUOPr1btlp3_fQMcQ0hB9bKKnCYZEu7BfLXOZ7nSSuX-gXAkWvLyiBSyK5_zmr8eR6krd3f7V-i2EGaMphfw65u30tDstlrnfPyBLgEGVG79XrqSfHVOLWdL6GATadU2ympFloe7_a59k94je9XhEZkM_bV72c73Se4LA5aR6sDwBIOUmJ4G_fbQwiTl7YBfvqPuSJnrrmljun9dW7rkeTDcRd420P1G5_16Q1dBD5QM7FaPqjxhOUvzY78xbHxyDNH2TYq3ygnZkvusY96TEnUuORyIAl3cOVt3bvF0M9aj4rRM1lLGeP4pd_lD-YYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=r2qbQTxrvlK-e5fRl3ayJTkudmuPZEuLjYpXEi2tigtyO7lHB67hVjUDyhXpENxEduMo2UpmtYdfNJBAnjsyOBosvAIGbsGRlizPn_6ysi1trZHWBJQyBIft7bDhC3FVCYOG5EfPF7zdUeJOLpCnIxyuY5TZ-h2MC7N3Tf7hIsjdUGR-byV2-UuL6sIY-DXeA7DZueWPRMY6WELzejmhJbTTY96j1iMJ7Ecmfu4BdZH5_a3i7pAU0x2gzNxlTYg5o8PvQjlyifrjkqwZbLq4Z82F13CYynALh5h5-FGnAxtEafdIhsu309GTzr6sJk6q7MB3HL_N8zfYRf1LClyUuheu_Z6-SRKRhQR0ZEcATc5dUOPr1btlp3_fQMcQ0hB9bKKnCYZEu7BfLXOZ7nSSuX-gXAkWvLyiBSyK5_zmr8eR6krd3f7V-i2EGaMphfw65u30tDstlrnfPyBLgEGVG79XrqSfHVOLWdL6GATadU2ympFloe7_a59k94je9XhEZkM_bV72c73Se4LA5aR6sDwBIOUmJ4G_fbQwiTl7YBfvqPuSJnrrmljun9dW7rkeTDcRd420P1G5_16Q1dBD5QM7FaPqjxhOUvzY78xbHxyDNH2TYq3ygnZkvusY96TEnUuORyIAl3cOVt3bvF0M9aj4rRM1lLGeP4pd_lD-YYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=G-S4dccnMEPrK_gZZq3Ck6wQklgUw4p6_NsEmfLCnSStmdyRLtKpoy4c96U8opCF8WeBG7B2PHeJD8gbOnVUBD2FX0dXwOKP0jsieBuQTvKKbix0Z61bFJViuvYrJCbhmp5Zvv6wD4Dvux0dG4i7rxv7i0j8tVk6Sj6unkrmhENadiiwTekYEcvV781vOE5DBXAja4mssAvWQHmSMmvE0kBY1EI8xkkLMNy-o-HcMGOgievDX89LNqnY7EBhJR0SSoNAFGnnvdJA5E__jeFFBt_Qkl_-O0A6WSSb4N-g1sM7MDAupGT13X45grjv6dSuujp2hkuGqyc58zdvUq6aLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=G-S4dccnMEPrK_gZZq3Ck6wQklgUw4p6_NsEmfLCnSStmdyRLtKpoy4c96U8opCF8WeBG7B2PHeJD8gbOnVUBD2FX0dXwOKP0jsieBuQTvKKbix0Z61bFJViuvYrJCbhmp5Zvv6wD4Dvux0dG4i7rxv7i0j8tVk6Sj6unkrmhENadiiwTekYEcvV781vOE5DBXAja4mssAvWQHmSMmvE0kBY1EI8xkkLMNy-o-HcMGOgievDX89LNqnY7EBhJR0SSoNAFGnnvdJA5E__jeFFBt_Qkl_-O0A6WSSb4N-g1sM7MDAupGT13X45grjv6dSuujp2hkuGqyc58zdvUq6aLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPKFunU5uL-gi4xxTG7E07RGDMkAvguMWC33DYSg2Jj--XL6lFvqw4_hldaBw_eJyql9xoITVa7V5thUWBjBdBuFBD7evWyXiw6Nvc6I9j7BsOag4OT10zdQFz_ibSkiV0mGJWEZHpO-QCxtf2-PODFFDHi9mLx06Y-s2PebO5VnzxtvH7Jx5j8OOTIIPS9lLEWFp0S0A3PVpyQ_UDFTY6P9sJyyE9wWd5BLbe3rvFsLgdGaZoU4X9sSJTVIdkzJ9_nIAwC5QW9grR81cQOOeS7XTZwt05MHXPSE0f8YzJT86_NVp1iJrl9MkweqeF0SpQhvOYyYWQkXDU53XQnCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=nGAxM2_PGIAgTFfQk0AQ5S2wShO3uNKzSR3gO7GxoPg98cfPMEmeVJxsbRO3d-BTfncImVFmF3XCmxi1ZXMQH13jbqGfhnsBF_L4JgGrIoK3iaCgrxNrFaLu8Be358-4QfdwaFOqu716TvPwz0vW7KaHGOkFGjLevqERB0CcAL6VqgsPCUfe2RDfcs8lzwRzO08c05ilyzvKlkXVQpIHk1oIxX_XjpzF0kS1zDE7-6k98UnDzamECZP8GbMifeCGYIFubPHkrAkElswJKikbSxOy-yp1QftWlfvKUbUJR5kDIK99xAOCNL6JdYuH8EppR6ukIeDKsHtCLsFiSXiSMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=nGAxM2_PGIAgTFfQk0AQ5S2wShO3uNKzSR3gO7GxoPg98cfPMEmeVJxsbRO3d-BTfncImVFmF3XCmxi1ZXMQH13jbqGfhnsBF_L4JgGrIoK3iaCgrxNrFaLu8Be358-4QfdwaFOqu716TvPwz0vW7KaHGOkFGjLevqERB0CcAL6VqgsPCUfe2RDfcs8lzwRzO08c05ilyzvKlkXVQpIHk1oIxX_XjpzF0kS1zDE7-6k98UnDzamECZP8GbMifeCGYIFubPHkrAkElswJKikbSxOy-yp1QftWlfvKUbUJR5kDIK99xAOCNL6JdYuH8EppR6ukIeDKsHtCLsFiSXiSMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=kdbHy7oaWo66mmKWy7JIjmxfr_4zS9Pd58A3Gx3wJvz_FLAB__-YWtwKWrKR4YfVosVDED0N6KR96YcOPLIl0JacADU7iyHTnMp10TdrWHThPvGEwW9CV6bdZQ3MT_Ww-xP1kx0Q8T85q7vSKVtApK0scpF-XUbpc48HT3LAJw9Xdlo79cap28cueqY5waTvQZdVcmPVEVrBDwaQD1729k9ABa1LttTq4ETsmOsf9cBkRNNu8_buGk48st3fCgBlh-_nhTGe4CKPgd3V_GyuRWoSyKwvKMZxxh6CIYfophzNPRIY6HtZQsbK9oxZwtBdoLGxxbeBHmVvblzLX67_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=kdbHy7oaWo66mmKWy7JIjmxfr_4zS9Pd58A3Gx3wJvz_FLAB__-YWtwKWrKR4YfVosVDED0N6KR96YcOPLIl0JacADU7iyHTnMp10TdrWHThPvGEwW9CV6bdZQ3MT_Ww-xP1kx0Q8T85q7vSKVtApK0scpF-XUbpc48HT3LAJw9Xdlo79cap28cueqY5waTvQZdVcmPVEVrBDwaQD1729k9ABa1LttTq4ETsmOsf9cBkRNNu8_buGk48st3fCgBlh-_nhTGe4CKPgd3V_GyuRWoSyKwvKMZxxh6CIYfophzNPRIY6HtZQsbK9oxZwtBdoLGxxbeBHmVvblzLX67_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOqxpQ3gvmtaILH9Fc7kWr7cpN1ArapvpmNh-dxAocDTOv8hta6fyXm-0OQQvTQfnsMVYLmDg4yLt7qYpB5zXSH6s3QlvJiRKKDS0gV3Gl0FDyTLYsHxWGH10TOAplsrEetVANA9NI9ml0YaZQ3YvNFVW1h5ZcbeONyrWhkSSQ4WPYm4T1EoNifPbyhOMWcD9wmrv-lh-ig549EGbpzIAppBDEnfwIsJazSFi2mUBBxjMFiQD8XxoX8ogWxZ1-nPv_fi4qFkiyVklVTyPksSDs1g1Hkrdk9XMeaZoXP7DTnyI1fgvZr6Akc-KHABK9EKycFGHOMWD8f1hSC5KgHHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUmP_4Kp5oiqxJrnNMjPykzKjZ4GSPhWuoSgXoeJju0kOHe1hLmLl_vJYES8D4eDjuvYkZG92iel1ApCxn-0jJgEyW_YJuODPPzPt3IlN_LxU_G9M3lgDyjiYZQ5G0bMUxsCtIoki7RC9RoIpGJVy6v5eFa35Q3W7BhDuVdzfa02eXhy7kJZULdT0GtA4gLvojnuR7oJMmBhlBvKW4PZC7SnaXo7c-_xwf9DpuWxz2l-xaMmyjtx_5gdu99Il2s11ys8q4YkftjJ93sTcCR9thxQEUYg-E-WS4bfOuzdT4TMhadHNAlABWdu37TyZsnfhywOftCyPJweBops1Gs-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOvK-pqh325hDlCNAFGUl5dYKN1xsY7mnJAhVsxhYNIp94g-visv9TT91_vhSnL9vEPj36OkTZd_yes2jH41HqmE_J7KHaOnqjK4pUyQB4IMk8-DjZI6HpaReD_4CKWrSl_7Xe_CHkGRPMN-qtPIAvsfrzYiU-WIv9WLjRQex1Qp550naFYd45JuHPSGZ3OrddcOTFozklz-PiNk8bzrd7oM0K2o_Ui0NzBEvE7zo9GKeKeQRO11dD0CfNW6rKh0NUrR_ke-ynWLt17SZl4HOENtqO8SqZXcTVK9RT2EpOb_k8MVvCqwNtmWkxlexZJB-OSNfpMzaLpMsqLBgkqg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZvWMF7nmXBKVLJ5k0gEDnMRF6oUnrdt1PPqLR8SpcHsWylABQrK7T_Mwpyqtc8vMo5HIk8OmjZA9lTgGJrDKTD2s_i6Qww1wVWGy_wxlvenrhrykMX60EJQX3_BoxOq1uPliXBiPxp6ikKWaq2kNZIuhF2Ed8ra2E60EQXmuK-81xLNNpIpwacIERiFYvJj4xPf7OSIf2sZbXE68oiws05vw_Ye9bK82jG12117q_Rq9Mw66e_0PQpU51lrRN5uksJzE-FEpEFT1pkHEGU0EeFJUQ1eHFMJ5sL6OsIkki_VzV7WZntbRcHmv1h32bQ2MQzChmkhnnbiB0763EUXDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-BlVysJdnmZoZMPi0xvreFYodnrZabJu-XA2aPBYzobOO3KBSB_Qr-PvIKJYUhSAeTRnNEHxRgkn-efkwCw0FCK_wRuKLbcMrAzp23PENNLVfmhQftQfoRsVx7KF5RzOmXcsAwoIR9-rKjieOOji6ms7zFS43eTKtzUVxziE_x0wYmzeGvIWCc-4b19Y56BXXciYFP-_mASYutyAGp9IH4bGXH-SXAP5VmC4N7NIm_vBY_xkYubuXEe77jj6j7lNygdQk2Lh8BQryPxYx-0x-HjZsGk13IrJnXXDKSZO6DvkEbRKju0y-BrCYQ6kS8EjSOjDH_cQNUCSvBsVcYX5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgbhe4ClaK-l6tfHrGjFdIvP37zO92VHa7JYUWnJbCAleWdxVuEnkk_3r-BH7R3Pdr7dNBBi-ByZCM1SEtbEyVI_FIjxMUHjG3TkX7j-vxwx5YSnYL-kYsKcdqTpQDD11agoi7W3dDpR7xo1y3E36oNtYGhCFVEhpTscfoDOv-evP4zgEIo0eBFUYowXBb4QJYb_8OXhYkR1Km7PMMMoBpBaIF2dGKOOW7zUeOF9EP0cN6-ZPIirr_FpuT0DETuZ-AKk59tDe0IU-LY-npnJi4oapf94UcAGBboDdQjK-MX7mwCD8mRRiySHcjvm6AtLJASJJwVC_X_lmFozujYNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BecBs4IqmkZh5vWnOUVcvlMs9t_5QN9L2y85nPpbugeEekrF41cPrAl2elwDfQS5WVHG1wEiETtvNKklB2qEyCd06BTMU9s_tiyzqiYvuZPsO4Xjni-kuYvVL1Ds6m1fa6F7vTCtsJo86kvmHEUuDaePdjKf7qfiWsMx1V12c4U_z62KoSlRQOWJpn2HYKzR1z0K47z1xNNYovBpO8sdUr67A0q94uJI00uTvA8gKyeCL2NiD9htwFjPJE81wiwaWH7buuIUqJyhC1tryrpd9iO3kn_dzkijc_yiuv1gKkxnjnPM_ylhts23aAoJJDfswbBrGf-cUOTHlXBcV0STUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHa7_rtcg_umzfLb8luY0aa4YS4JnMBWvlBxQeod8puATlF1pYSM1RQGVgOOl7xBDro5mGPOEkNDbc5KgNtcYrxxk0fCciJC2v56jK6XwmJVDa7fKyqS_tZsWKS_fPmGgxo-geaVd0LOwnQFeG4xUnVKF_2_zcywuqEjE5V4j072HDWWpEP_MvqLI1O5k2xQvS3OLECk87W3AYtKxd5tZfrNf4iAtTP03RmDDa-spj8KaAhA4rvBtg7JQ3KXEGHkMADPKfKO7o9cX2sha1sfoECaoulSsRzbNcDieZwFomxfG9Yp6TLtDHWOfMUeYdO4pE49tEFd6iTng9X_iDcPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuMIbpNlBOxuo-EleNoOh_yX8G-eIUrFFscKGmkdTXhSV1zIUooodFMRFqCCucOC3pxkj2X5l0DFX_n-qa3F58mesqwJ-aeYDvvzZxhtRIJc6w_9Hkjb1YBWKuJGAlgsBhd-Yj6xlMpZI0VnVMa-FHDDt8CppEkMGHaFgyMPA9QKAAqsUFNp7-DtaeUm7JnBGcjMMovWQReKPTFHwA3kYEZngVdZZynFbI-AM0BoLQLxggxu_HuaqBEWj-oHWwfjEFGEMLNKbdNBHkAFmJDAJ7xNM07zQdhsiqqdF26uMV-hgkKpUOb6Vl2PcI00OeyCAN24RS__JKz47OLw2F9Jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmW1LuoayCUWivVX-cUHODdzoHv02PGdUbFe7MJaizoOBSaessGy1BHqipRlc_N4L6oIG3l2twXE-621bxo5yrf_WbDuC0e-p_XeP8pG-Afjr23T9aDs3aAdRV2SZ0r-HEV3FBadh3-yzl6N-NAE83Nk6zppgZWWoMeCl3Oh30WLvshquJjTC0VguAzoJvj66HfMLyUih9hgX8w2SIUG3McuRIQP7d0etkJMcoh9nMxGlQqJwojlq775bTg0CBS68TvMilZC4CLeiLaENrKg6rUJJOMMB7GpEmFkHSikcf6Gz_m8E8woeWCJgTE8XFWSlLcQ3N4wf80J7FVqZvIlOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=H1tI9FtR_U-nSJDF-BfKQTrY_rp4UxpddLboK1maQKNH2k1ehxXqXPde5cZQk2y5nmG4lUpGddxe4yGc4VE5T2jhF3txqJnK6fQDp4qZd4TFRO6rMs99ouT3Yldtb43mnq9hGeo6bJfzb1e36un8c6Xh9eaC09JUHCbjpX-8g7m8sRT75hduP86n6zHZhMKl7lSNmunuMqKj84gTyE0HNe3rbr2F1Pj21Ex1o943xt_zGiTn7II_5iur0V7u0igWrX-qncLM6opC3nuENuVJA38In82W81aMlOskbRN_y6YGTO-kGspbOgslnBm43DXB37PYUFBMweNEdxDohAhkfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=H1tI9FtR_U-nSJDF-BfKQTrY_rp4UxpddLboK1maQKNH2k1ehxXqXPde5cZQk2y5nmG4lUpGddxe4yGc4VE5T2jhF3txqJnK6fQDp4qZd4TFRO6rMs99ouT3Yldtb43mnq9hGeo6bJfzb1e36un8c6Xh9eaC09JUHCbjpX-8g7m8sRT75hduP86n6zHZhMKl7lSNmunuMqKj84gTyE0HNe3rbr2F1Pj21Ex1o943xt_zGiTn7II_5iur0V7u0igWrX-qncLM6opC3nuENuVJA38In82W81aMlOskbRN_y6YGTO-kGspbOgslnBm43DXB37PYUFBMweNEdxDohAhkfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9CFHWrC3tN9yYnsK8AbDkg4sb9TbZl87FRlWBLqDjBk00wqO3AkwXrleErsYg5fRs-fFJu3RdcLGuepJjka3ihUUH62xjcqEXRylhkygNvZHsneJM7hEOIptZakjOn3wIL9IveiQqDoL-4raXAj3z9zR2MAJ8mWVoXm5MKRxSU5XAuf7XGysE42_7evwRuxH-dKxJxXXt2rH1TrbhehT9DzlFVWhw-RP4fFOKXwVL_9mel6yqhbG_vCWDcA8sodzwUvvBz1Qzg8Fc8_bZ9377mYpuyAMzD4Z2GI-nbqc9p3t7YKZu3LYLwNguemXWGbF-3TsTY9mRF3ol5n85iInA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5HSaXG4Xu5AzIEMDpnFYVbNorH3mv1ylFkOGUAeg9PulmXTTkmv0gqfBysX3Jc9Abh2tuJmKUrWUOMPJPLQrD85cMUOk_Mus_bihxJ_s83CzB9GCMaRHVo41xzE6EKRXtiHYioyUICyiPIoy78RSkhKBNDY-Bed7p-50v0jSmJ3hUY2eSzS0nDbSGNciQFW7sOYss-5yi8n6VcR1DKl-z_l0Qk56aTJAP9S4V_N7hetNABM11slb9Lbk4seXriwgTfQ3O_0CvB2z2n3YQaIfPJoHoxuuMn4G8Ang0UbmMk2rkQvjmc6pAdeAcr-5lum9PAktZM87UE3j1e6dyPM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=CkyPoL232D_hRu-qdeW0jGHAJFEJf-drC30AC_kuqPsCNHzN2bMfxMJ5jIWtPhDmvkV-tHtgkd6c4mDdzB6Ydh3wbU7yoZEilMFmi7WH-tWGM1jPAgWLHtmUWEKxMnrFRHQx7qCEj_dKXZNQeM3WClIKUuPqhFeS3ttYLF9YwXC0ytbF2PqpwNO_aXsg9XhWxHom9SLO1_LS6ZU748WZ4bJQpW7_tJ18PSruzUPAU7dDDocpJTjX3IF-mN4bQd4PqfKwmPeWG-hOe4y7WBrLpztCYdMN2Vd4fNSG1Qoy57gDB5JndFz8SfxuoFhuL8us7ZILkVdIwDLo1T8kPTD5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=CkyPoL232D_hRu-qdeW0jGHAJFEJf-drC30AC_kuqPsCNHzN2bMfxMJ5jIWtPhDmvkV-tHtgkd6c4mDdzB6Ydh3wbU7yoZEilMFmi7WH-tWGM1jPAgWLHtmUWEKxMnrFRHQx7qCEj_dKXZNQeM3WClIKUuPqhFeS3ttYLF9YwXC0ytbF2PqpwNO_aXsg9XhWxHom9SLO1_LS6ZU748WZ4bJQpW7_tJ18PSruzUPAU7dDDocpJTjX3IF-mN4bQd4PqfKwmPeWG-hOe4y7WBrLpztCYdMN2Vd4fNSG1Qoy57gDB5JndFz8SfxuoFhuL8us7ZILkVdIwDLo1T8kPTD5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dO-gnitbp054KjtkgcdHDOzSdtuAGUgpcT3zvMIK8UBzFtLVJb9up1AFzHkmr5mQZq1nhkPKn5UuHpeIa-RjojUHJ2qnL_l1uFdmB3jjD9rqgJOPW0sVMNUx-dH1YOyvzxiojoq1Ro8mnb3ZY4koNKz_kvjx9UO_QA1s8k3NdMnPPGbgZ7WEqo_k_JZ-5oGn4pHGP_5a8JOfYtCQ3zenkL6zfmwSRbsc57x4OvY87OOaxdYyFFvjkZz9ODkIA8vVmE7LiaMZEsGu6DTFTG4BSggdnrAXk274kPyOrUAp0sL08NXe_Zuiw7xvv0CPuES7Gru_RoZfOA2Ao9xU80DN6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dO-gnitbp054KjtkgcdHDOzSdtuAGUgpcT3zvMIK8UBzFtLVJb9up1AFzHkmr5mQZq1nhkPKn5UuHpeIa-RjojUHJ2qnL_l1uFdmB3jjD9rqgJOPW0sVMNUx-dH1YOyvzxiojoq1Ro8mnb3ZY4koNKz_kvjx9UO_QA1s8k3NdMnPPGbgZ7WEqo_k_JZ-5oGn4pHGP_5a8JOfYtCQ3zenkL6zfmwSRbsc57x4OvY87OOaxdYyFFvjkZz9ODkIA8vVmE7LiaMZEsGu6DTFTG4BSggdnrAXk274kPyOrUAp0sL08NXe_Zuiw7xvv0CPuES7Gru_RoZfOA2Ao9xU80DN6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoTCeKKSDCxAPPx95xOtWv-ckBz3AaQufeS27xniu2eLtMtd2B4z0gGvNhWdjhx7cmWBfVwC9CtqIk0IdPoH8EAW5AlBJkQucwRuyafg0NEepo9AOLXSfDnW3wus0vaJpKim_XtccEC1xdS6S3VYquWfObhXtQ8EzUXEWJptDM2SYIO0R8e6avj8ZgRDxxrS5VV2FhbVIn26QTCp-M_yVpfrsZs97G_Qtmtuw-GbdXMPrW3ilPRp_bG0eWcRn6-mIq8MTXbquCO-YQ7aWTOH807LKKuMjHOe0TckKe4M2rdYA7aGWxXDUXqZn67Tszofhu_GGwib7e_76Hnwjdz7Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG4wBm4fzGqfKiMzFjSLnR4MfdoS74jdPq-4W3S-otSh_25JR6SBXhdRWqFybU2kA18mmiVFgIeCABnk9vnBuGyAnc8P2_St3UKroGEulKrUamCEMO2N7fJwp6eituB2SHqAPayU3vwzHm0lU8ZKAQpL_ivvf2z1csn-hvXgMTHrftXdUnwnWEUZBgEZyy30dG1fMths3HEVdHBJjE-DFMxa2oKGtTZxznNNRChm-V79ZCpUSWIT60QnTJj1taOoaeK9HmPixdW9PWS270KVPVjTlLCDKQLpBcKm4jWf7-iNEymbKmuSm90Pn9nEFW6gxod_GwEuaVPNveRY5aCccQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7jLOqYUJa_1kBQ2axfPLiqi3s9PUDvbEsezaqRiCmR7JTEhy5ggVaBCFGRJahYhkDqi50eSyyKLRq5FjA-RfXDVeqK8nHmV2imBww7zUcNqM6meYJnZ1fUEtiALZ-7UP0teyEZ0ysdXcZ6O8iJhhF2zngpaGg7WjslLBXaudiQC2UwD8a1I0p_RADblFDsnJe-55wJFa_roB8kw_8mZeZKECP346yr88YP1T6MuQG6IL-PVQHsqu4_LjQ6HdHcWfCk1qkiJ_5Ab4Qo8SwEYY3ma4RRqlAdQa2Hc3GdjPFdsjPl2V6kyJIaHpiJAoQY82kpqO9tqCbTalWxiTTOEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcE_OC139IhD8Kq128ewO_6nKI2w5FYfQVWnIERe_FCM5-5PjYAx9Nl02JhlSaJ_Ti48bV6wC1E2gJB1LH_Nq9cJjTcMH21UNlLsi6EUGavQfgiDN7pXJoiJGef44CAK97SfdQC6v9xHHTpk63sWoaZurYRLuDWlmugiF_Gd9zYpkPsHfS2N5qNS4U_uUG1w8nhOdFlJYvntKHDIsJqhj3aXvXZwUre4crLcNDEFDNe7te_ETlj7csjS-Hicshp96guC_hs6faUdifcyGBMmGtELN2YqR5bWAoKLLGc7XVBoojwFc4Xw6xx_DlCq9DkPaMr9mf5kWC26JZ1XaNAygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQgo1SH-o0mgDxdW1_ifpUvU5Nbkn14-DRShK6m8i9b3i21c5p_yBJjSH1RhbnzsGGXptodQiiGQTvGZtt1kXGr0bxpTKUT85fNJl1Bzh8NWjV-9G-TPhcMR5JQecohtlBcGI2NJnnMrkBvD2JuydSib4Sc1oVLppOg2yxq8wlQE2HTeF2M7YTlbGLpPEX0Ls4TYZsyH1EtbMMt1JvrGYJG8MIsjgY7132WXKt3nZZX7vXgMzwZ5JzDVohlTgQjidmtRjrFXYXy2O2iEDlfGg1qRTZT9PwPcymp8H_w94Q9fUmYFCbhF-Ry5eBBW5qwK-PTtfeUdQNoQ3teJGrqRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATGPYSdLB_pE2q41UgVQMe8F04FvQYcVtXJmX7ZXZjo69bmMBWGfptMgTU39gbXDICS5EPK5FckiTjWkoW5q6GGJOOWWtiiKPlIMIWRFSQXC3lhi7KY-mrzYfFP9eAeotq98_6cXVSbwHe645RM3pCviE2qIaAY6gfGB1GosJ-u0_xfVpW7BF0NXk0ju_rkeTIwHDI9-j3OZMNWljP15olyFSv8kpm1JRY6AfoFAC1gOMYHdUD1wNKi34ye3c8vSWMOQLUkF_0tERv_RXi1xzaFAik2uSXxoXfD6RbiECu6_SVudpfkzdfHJMyKOUP4DIqfNIX9OsfHxgnYq8s9PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcDg08MIS0qmVvMffbNuRcWXe4I0UYUaDV16JNYZPxV7X7aMAuMTtnj93vbnaHaPIAk-ZAcGPynLwAUhRlOgEmt3ZhSp9VQck40MBI8Y6oJa44fLkXG5_F729Bt1LOAYp2s6nEJ2xKOVSV9vVicOCu8nawBgqMs2SL7P2XDtt_cV0xyWCC7_jlgLYtWh_4yvFvLNf1ZjgsPsOELxhcoiXoMGcV6ZTTGNE6AjHY0EYu_ZSJlw2q3RJFAvgWDw_kKNbKLuVDG6Ohnsg3I-OJlLqlHCP0mobV-doa3s7_Y0ik3W0hdD-Pn0bvCl-pqQiFSRPVlqPPl-wIyHSI7DwOhEtg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YdwgqCzcPg17uvt53bWDiiA4I34w9QUw7QkHn4I7nyxuR4ckBSSKlYM7LZNCV3VzeOsjaQpDu9mb0OJic4zcGJ9hU9Xd6wQh4b_iKbDw1KD0-YWjw-F16BtNM9OjeMh8rxb8XCMnju8RgY0VGhR3YbmGRBtjM6vox0sq4Tgjp7fgap59B4A2qFPuGPfc0uGg8BkVbORZ21KFzeJfDF_wOY89jQs77YzCaW1RbUjekrc5MkPsUPdKHzeSYagO70qRFMh9NR1iMfS6AKQ6fur8lLeeex8AIqMfRXGPdnpGDTiow9Qb5w7KVhNqFM5wIRr6bucjAH4plBJSCsiCix4F5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YdwgqCzcPg17uvt53bWDiiA4I34w9QUw7QkHn4I7nyxuR4ckBSSKlYM7LZNCV3VzeOsjaQpDu9mb0OJic4zcGJ9hU9Xd6wQh4b_iKbDw1KD0-YWjw-F16BtNM9OjeMh8rxb8XCMnju8RgY0VGhR3YbmGRBtjM6vox0sq4Tgjp7fgap59B4A2qFPuGPfc0uGg8BkVbORZ21KFzeJfDF_wOY89jQs77YzCaW1RbUjekrc5MkPsUPdKHzeSYagO70qRFMh9NR1iMfS6AKQ6fur8lLeeex8AIqMfRXGPdnpGDTiow9Qb5w7KVhNqFM5wIRr6bucjAH4plBJSCsiCix4F5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYpSctW74yyD_hVfsCla1cj0lRjZbpmpdJNfXvFP1i4ksbhpRDOSmhOK9VaeWVIenB3K6dZyHhU97t4yFLBwfeVypU2ph_pxCNbwTReo9ELUiPEsaBqdLXviU2lRZ1BCMhd8HcbjKU4hBfekfsIxp-KbeczhqhTGNEvoFS8KNWoRAkS3gRiBpuBiwZd-3-e6nvdVJkvxe4OI1_ywzANTDQ103DIm1Lg5K-U9wQ-FhsSrrJ5Tww2f4UGDsN2MLTcsexfCx3w365XZBIXiHRZ7dv9qBwV8k995Aj-z537hHEZOHx_K7KW9Gs9mfbPgkbM1IAx1yiO2Wd-SM5DMh86Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=QnAF2xQAuQgTUNzBjKCufEpQnmvn8p6xuSK02YRD2_Hb1SCjQzGqyvaiyDCHvC0PBuhX-p_sCsiKyCDfMvczwr3k4Q4xpOkDyuOr-y1r0WwC_IofCiMe-p8abDiUpagKmf5MK3_7w43TKekz8Iv2oFdJEU5GkLnkfIYzxc0qZC2yyzt16o8JCTaBHWwxbC-vbslXb7A5lupO3FkQl-y5h7NmAwgN1oa40NXc3yywGyXz9KYbdPu2b9_Qswap3EWoVltkhe0NnH5ty2sbG95GvHJ08HcIrEH2CCnDpDGiqKp0lu4hIuqCfqoOGVRP-aGPMP8ha6bHscUI4bQdyYICMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=QnAF2xQAuQgTUNzBjKCufEpQnmvn8p6xuSK02YRD2_Hb1SCjQzGqyvaiyDCHvC0PBuhX-p_sCsiKyCDfMvczwr3k4Q4xpOkDyuOr-y1r0WwC_IofCiMe-p8abDiUpagKmf5MK3_7w43TKekz8Iv2oFdJEU5GkLnkfIYzxc0qZC2yyzt16o8JCTaBHWwxbC-vbslXb7A5lupO3FkQl-y5h7NmAwgN1oa40NXc3yywGyXz9KYbdPu2b9_Qswap3EWoVltkhe0NnH5ty2sbG95GvHJ08HcIrEH2CCnDpDGiqKp0lu4hIuqCfqoOGVRP-aGPMP8ha6bHscUI4bQdyYICMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=lyzuR1AQJ3pfPrtiNuL--_ieSPhv6C2DoC0Abi6IfrwMMWcO55EaW4kG3FKkqEVVSxCCeLnAdB4KaTLVjPz5pEWMFjZ0nCBQ9MPkf5kaf-_432lKfYPO7XgM5gTgtCKqRx78wFFL7ja-Wm_oiWjH4wm_oFd88FZRaJ_nGJsUNhnHKmI8qVj5eFbD0JMKSmgvgz-c63EGbBSjDQfFnABHqITX_G8lq0L0s19HoTmF5zllfct-kqIDCXeMo7Wjfqgy2f1XT3GR6PUA9eCfdvvQ796-OVfQA6mZm9_pruCqqlQIOVvfo7Ns37Lhe0cqLDK4vt2IpxlW-iR-hnXv1P-iSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=lyzuR1AQJ3pfPrtiNuL--_ieSPhv6C2DoC0Abi6IfrwMMWcO55EaW4kG3FKkqEVVSxCCeLnAdB4KaTLVjPz5pEWMFjZ0nCBQ9MPkf5kaf-_432lKfYPO7XgM5gTgtCKqRx78wFFL7ja-Wm_oiWjH4wm_oFd88FZRaJ_nGJsUNhnHKmI8qVj5eFbD0JMKSmgvgz-c63EGbBSjDQfFnABHqITX_G8lq0L0s19HoTmF5zllfct-kqIDCXeMo7Wjfqgy2f1XT3GR6PUA9eCfdvvQ796-OVfQA6mZm9_pruCqqlQIOVvfo7Ns37Lhe0cqLDK4vt2IpxlW-iR-hnXv1P-iSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWnfdtv4WJC9b7qHjpehsEUwroqtQhTn_ojkzYDuXC6e519cwmeOPQAjTBWBxzK_pZ3KfSn05R7O-CDrZRaadzY1Rt_XQMNT9uX_JvPJ-vG2nGw9__I_gUJtRcepVCuMiQUhHZ8r7vkPu1a4JdV-fQwjZI2FFebP-96wBoL_gT2TaiG_zh3hmtdPFdrqJQZSXv5aSE5Tfelqk4b9BkWWVkliBbGwyUWEoZ3kZQIVb9BzR3k-rTxAMfVZkf9LJhLTiDbM5ggY3YQcUa_Hp1PDzHDXSppzk92y2p_VIq-2IYBKPV99Dkwldx7oH7xigMxiGDmcIsU7BE-pbxJvJ9qutQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZt060p0DEwZAgPdiS-QxRNnCC88Yv8osrU15B-cwj-D4ePB8un9IqMCeWbTvW_DzKFeUMscMijOSnIQKshMHMv9UqSn2Vwd2N8AQanQav4Zg5nI0-F6or3vRpLRKe2H-ns-uiW9W9aeVyaf_Yb1HzW4vYIvqt4rrPZYtJO9OpZ4N8pDvhwQeSWabz0jE4FdAryGMsSAqYChACcqNINjWM6AhlVAu5jx7RuhDla3_LFUhUmN8c4jvv6xa8rd18pRFbiZxciDt2iC4LFLOmASmcTgXzIR5aAaLM7lIXZcVhwedx9Imq8ACuMd27ZocVGHHxIyXXl0eefckGaicXjWKA.jpg" alt="photo" loading="lazy"/></div>
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
