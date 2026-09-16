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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGcTFHTDm5rs0PQm4WiNL5cWFg-0IUOmz5FUZ4-lTaBjlH21xlcjdOF3D2y6-r59f-9SMA7Iz9p1elb6UnSp6VZriqDOXAyThTHfFwIH6J_BrR9IPDec0A-FKkAIn6d8rw_Wp15PdOmnnHx_UbFPwBAuYq-ByIgr4Du6XW7aA-vbUCo_J1Y39bxM0XwZclqNI04kW75GSex1P1x3ct-GmUztW0xkOTS4EU0NnkF3jUTYu26MCXXehD_6M4eBEfbzaV1xi_JmuKPqj4Fx1ofDPCMFVi-mrgY-p3JbIwmsYVaBuNiznX4wTGxgDmnb1lhdWuNKcD0f0Nrm66q5Kw0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0hQcdAe-Er8Ch6T8Pi5fXDj0ReIZnLfzzJV3CmfdUD7C5cGwBClZf_ZWW6A0LwbIdlJEpqzcGY11WwwjM1ZJ9LhU8d8FTYLhaAb6nD3cuGThwU-wcpaHOSIDFIbWOSs0fP05Yj56rhBK6STrZKwOl0O5S45MxwmILdnLmxOEbETBtiE1nOlly2Xhi2JEs3M-7FT__DiKKxSgzPnewND2GXia22YYTQ0tJI5yvdy7eXMY4wb4FpMd6DmJsJTrJN5QXm50wT4VwTAuNz6aKw-cWT8bNs_Hm_N9w7H3-REguS4KtIvZstiGqLl93RUnqTP7fmq6j8BVLtlY_cZqW76Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX6mKjU6CBm9VoY03IWK6d_4syPbXAuJTKMW9yGfkl9zyqpnDitZutV-bzRrzLWyQdtaBaa4gCoVt8G7vByiCMvmDOXF4mEeV2_eAbr9jykANHV_8RFqyAP5IOICzxbrNUeuXTte_f4zRhChjB5jrPV92Ji1PVL5MkIygek-K42Rvs3CNZ_1yxUp3bPEeTgg5eTYqukrvYz98rHz-6LC6tajwx3HDo06XVaxMjg8WHu5twnzBTCG-ChtTdDg6aMuf-pu6gHaWkdLc541MxmRmtkoSY1GJs7-P5VMfQPCJF7PJ__B7DeqK5znMUyLz1Viut4W1JfrKi1Xo_lv-YpF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0EuEE9I_NYb5Wiwt4bw5eABv2-y_dSH4r62ajo1ByzhrfJcc7ZBTDhd6SgB3bLtQ_FfI492qW6Cl4wDKGThpUo9KcWV84cqzsdy40LPpejuRBtQ4kOWvHizBYKmPNowuvyfrE5ug7Cat60OXe-kgLJnMPnu8bmhudfMgFNppLgQcBxwyhaZdKzG5Ie1nag9Isirtbmf0_eRd99lmU1uQUpaW5lAYxb_RY3_YeKfEdOiigWMWrBxHGNUafdPHoAobkRITcMxifK5vKYSMyFfW5cgDZCyAWcd-G8B1tCApdXEt2yNCBBt544DM5oLtGrm1hWFADuBfBakLEuHYl3cUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=W5JmuwjX4noNtWmsRYpDXG8a87q_5864iUPPwrBZLX5nYbEtnK0qQTV8zvFKXzH2L7bLPvjMbGXDaOPv_Ydu9s7ZdSd4fOPswsj7ZNCbiDNQaZkpDkFUxmb5_xWysTT__0Gq_gQLZf4Mgy2ixuyvQvqbJucy9fkY9XS-IQ1Gb_JClXLqLB98bFnM9aSZFG-CDbQZGpXDUwpfOIj6-Xu2CLb3l5jMHCPJPMQftMBaS4VTyXiGwkfCDmBTV0Lxl8rUkez9MP8pJTp3nHTSiJsWVBrMsh2Bzl-v5YEIYQbi9zxDCHI_MuSjf_VIkUBxINBQb-WkSyZYGf712uO99fV7EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=W5JmuwjX4noNtWmsRYpDXG8a87q_5864iUPPwrBZLX5nYbEtnK0qQTV8zvFKXzH2L7bLPvjMbGXDaOPv_Ydu9s7ZdSd4fOPswsj7ZNCbiDNQaZkpDkFUxmb5_xWysTT__0Gq_gQLZf4Mgy2ixuyvQvqbJucy9fkY9XS-IQ1Gb_JClXLqLB98bFnM9aSZFG-CDbQZGpXDUwpfOIj6-Xu2CLb3l5jMHCPJPMQftMBaS4VTyXiGwkfCDmBTV0Lxl8rUkez9MP8pJTp3nHTSiJsWVBrMsh2Bzl-v5YEIYQbi9zxDCHI_MuSjf_VIkUBxINBQb-WkSyZYGf712uO99fV7EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnOkKG4KBZ01e-18LYRzIZD5W21iLzodyQ9iNGCVxCy-_sYzatc-1t488Nj7n6WPsQByZuLDgdTpYwUZYvNlze3xjwVL0fQxBJWZfeqHPg9J-1jsvs80zPmaLdqSewjRCawMTjzwithO0CAiy28ullZ5IauCGOGRjVDTU_NJt2E0rcaGMPlcWWMtXzSXpf6zgG7bqCvkfPmcfB3nPnB7WExDfVsaTo2OCiHpI2iT1g7iWpmY7aA4PvHj4MInzlKX_ZnS8vcI5RBxJt-OgO8yBHd2J1Iz3lVr2EywqnV-qMzcDggjXjZazPn76D8bNce-zQ0wW871TleyLsQdUUq3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b__bqLa4Za7xoc3f8QC_JIfDblXVMDUTBHShfOjHQp71iFYI8WOvJfyzyzLhufFmcmC34ByW8c0PtTYBCVqtrMoT3QI_cPrOEK3XqmAT9XDMcyDMLWsnc63dM8JbBM3BUsHltKCdom62Q92WaQdyJMzsTMeQ4jnGoew5ERSI5qedjpOndDxo8E-10zxXFlUDVgbqGqNGJBNAQOI0M3SrS6JGmGR_IGWjHJXMinqn6GpH7wbZ32h67tb8rJmH3D-fyFi0YfSh4ycl4dBVFJQu5gSqaRIA_hSTx47WFYDND0IRAYnINyy-T3YNlGQGV3ph9aRliu1fskZMlv98My6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=K6udCtYmNbdzwuE3zXPkDMl32G6LSWJ8fiIkWJL54J-b_cjPwwUdNhrbHjX-KoJV0ARfq1BaGDnIPezXCeDswzeek0xl1uEmHDFd0-m7rj8lv3XdIndOlyR_FE4hhh5St83Ph-4RzQ5DAJ6NEw_uy64uTJnHNq249nV6MNDvs3s0FuTGojdjqXtHLNXBC1C7Y2DmL8Qc0CcNvJL9mA0mmbUincp2pS20Cg3Wm68KU9G27rm1MBgbw9IiKn76QWm03pgg3xRTJJ1Y52VcgojYFL2QH6yqFKzDwzpk3e8Ho7_V08uz0i98dMRAaSHAw_Ozg4gOU8CJo_z39F_VViemOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=K6udCtYmNbdzwuE3zXPkDMl32G6LSWJ8fiIkWJL54J-b_cjPwwUdNhrbHjX-KoJV0ARfq1BaGDnIPezXCeDswzeek0xl1uEmHDFd0-m7rj8lv3XdIndOlyR_FE4hhh5St83Ph-4RzQ5DAJ6NEw_uy64uTJnHNq249nV6MNDvs3s0FuTGojdjqXtHLNXBC1C7Y2DmL8Qc0CcNvJL9mA0mmbUincp2pS20Cg3Wm68KU9G27rm1MBgbw9IiKn76QWm03pgg3xRTJJ1Y52VcgojYFL2QH6yqFKzDwzpk3e8Ho7_V08uz0i98dMRAaSHAw_Ozg4gOU8CJo_z39F_VViemOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BZ4hKg42zV31Scb_OfXuNphbg_AGRxYJJfoZvGxWF35T_KDFZpILFh8OMRXsqcgn1sDQ0Ng4keYmu0RIJ76DX0hNGJDoKDsG8k-ngw23HNsWysHaKlyedPbNgcbnNwq3m-z9szRHUgXj2fUEj0lBNEUy94M2B_VrIAtYwMfWYFWL9uJVgpGxjHuYxwP2Od9E0li1wGuKTfeh2tHFbGgoghwT81za1S2OdEXvBKgEcGD9u87cHX1GtiQEPn6wM9eosAmf20ldL3c69nglPk2MT0m0Bubk-pYsD37UoyI3ipkdgskh6l7IG59BTyNa1MmchqVjNlxtB_FmI9cy9Y3vBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BZ4hKg42zV31Scb_OfXuNphbg_AGRxYJJfoZvGxWF35T_KDFZpILFh8OMRXsqcgn1sDQ0Ng4keYmu0RIJ76DX0hNGJDoKDsG8k-ngw23HNsWysHaKlyedPbNgcbnNwq3m-z9szRHUgXj2fUEj0lBNEUy94M2B_VrIAtYwMfWYFWL9uJVgpGxjHuYxwP2Od9E0li1wGuKTfeh2tHFbGgoghwT81za1S2OdEXvBKgEcGD9u87cHX1GtiQEPn6wM9eosAmf20ldL3c69nglPk2MT0m0Bubk-pYsD37UoyI3ipkdgskh6l7IG59BTyNa1MmchqVjNlxtB_FmI9cy9Y3vBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=DX-2GnnSXy4wIQEjYVvtI2clgXkJ6yK5hwpr3XzlNvwxXZWEnoGVzeAQxpn9tQVc4V3-XbtjkRP6rl4w11S4GY-C1VMWI1T1lNHNKHy_9ljuApDR26ASFg_0wpsAawwPeHtxLshVqcaS1zoxLKZFKyCABjpGo7AbKFXSKzIP5rqVhjGy94dDomrpnaFtsN4rOioFS3kKe7s5uVhZqflaPQJRLlAA5mFtVKq49uCgo8S5hVRmZL4of821OMwxnCwPKBfNEj2N74QIW40y0O0JwQpYvlpTl778TZV2AAOCXxVPJ9cKN0MqR8xmUT4M_a6ZOq-P95b1GdJwCftvujQJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=DX-2GnnSXy4wIQEjYVvtI2clgXkJ6yK5hwpr3XzlNvwxXZWEnoGVzeAQxpn9tQVc4V3-XbtjkRP6rl4w11S4GY-C1VMWI1T1lNHNKHy_9ljuApDR26ASFg_0wpsAawwPeHtxLshVqcaS1zoxLKZFKyCABjpGo7AbKFXSKzIP5rqVhjGy94dDomrpnaFtsN4rOioFS3kKe7s5uVhZqflaPQJRLlAA5mFtVKq49uCgo8S5hVRmZL4of821OMwxnCwPKBfNEj2N74QIW40y0O0JwQpYvlpTl778TZV2AAOCXxVPJ9cKN0MqR8xmUT4M_a6ZOq-P95b1GdJwCftvujQJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=HKoNDZb-UfGouBOxnxgUlmjaM0tXDAXmg5djH0ufsWEvzYo8pOvW3lKnlIzPh6pgeqmG_ZFvUxR-w3vvjXT3kwcgm89WtTuFLrjFxpZn0dRtDVCcbuB8AXhU7ohCJAqMMeUrI3K0vV_u7PGNbgkIUcK3whXgbv-oPMk5MWCYFxTfu-enw_b1A4L6j867OWhZFQl8opEdYW-cA5AnP8bWCRZzjX5nCIx74bAfBOTs3BmVX__CpARc7Y-phd09ySTMGmdnb-TiJjh6KbLAr0Ym9YOFM-lGX2Vpkm5WTfnKG7zQQrFXOfMEBsCJudgopoA_sova-EBka8EPIGTu3b1SaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=HKoNDZb-UfGouBOxnxgUlmjaM0tXDAXmg5djH0ufsWEvzYo8pOvW3lKnlIzPh6pgeqmG_ZFvUxR-w3vvjXT3kwcgm89WtTuFLrjFxpZn0dRtDVCcbuB8AXhU7ohCJAqMMeUrI3K0vV_u7PGNbgkIUcK3whXgbv-oPMk5MWCYFxTfu-enw_b1A4L6j867OWhZFQl8opEdYW-cA5AnP8bWCRZzjX5nCIx74bAfBOTs3BmVX__CpARc7Y-phd09ySTMGmdnb-TiJjh6KbLAr0Ym9YOFM-lGX2Vpkm5WTfnKG7zQQrFXOfMEBsCJudgopoA_sova-EBka8EPIGTu3b1SaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEFCIyNqlZJxt0-uCucJkHzqaXeXIKuNzu07Z1SprN_4oI_hU3YtG_xvSm3tGdT4cYyBQY7uKhvBLCGSpyWHKtRcWxxFduuxS5pyfWhzHETZrQojhD5pNXYlF3GcWQ99qq2E2wQAYiwa2rGVlrt0CFWPpaEEzDetdTkx6rZFfL9-El8svnEH3ax818pJNRem2CbMny_DEPpLcoN0YqIXzNXy-M6GZTZXzCfbgT7yE9pNEsOQ4KgWWkQDgU2HuuqJ5ry2Gqp62YPpCOwQaCnaeilH8M9j5NwPt_5uSmOhtuuZnxTbxy3JBnq_z2bqCrG6JZu5pHBqGx638wCfk2ebDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dYFTPrvlfVxHVM2Pu3JCGu8WSwrDe_BGeO96b270JestaNlVR85tw9SyaEztyY-Nc2smhDsQtkJjgWIbye2UzxD9lV-IZUvSiGUgYICLZBCgKm4fAQlADpZr-tQo4S7K4pCQKG7bfa6JUlfuSymzEsLeQ4jJ4KLnaFycbHHRwBD1zqwPvBrjabcSYtmpYs8O224EeqpNgJFmxjJp5pnR16BgH5wj8qCxWyDDfPFhLjF5bSBav6q5X56aZQHGE8Bf5uPlnGdHiPlLG8amhqd_GglHmrEj1HjjnX15zpHWha_JVckf9G_pFiPOaYRhQG4Xlerk40mP1rBj_WO5e8wXuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dYFTPrvlfVxHVM2Pu3JCGu8WSwrDe_BGeO96b270JestaNlVR85tw9SyaEztyY-Nc2smhDsQtkJjgWIbye2UzxD9lV-IZUvSiGUgYICLZBCgKm4fAQlADpZr-tQo4S7K4pCQKG7bfa6JUlfuSymzEsLeQ4jJ4KLnaFycbHHRwBD1zqwPvBrjabcSYtmpYs8O224EeqpNgJFmxjJp5pnR16BgH5wj8qCxWyDDfPFhLjF5bSBav6q5X56aZQHGE8Bf5uPlnGdHiPlLG8amhqd_GglHmrEj1HjjnX15zpHWha_JVckf9G_pFiPOaYRhQG4Xlerk40mP1rBj_WO5e8wXuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=bxpeKeNJrhWAmylhBVryRaiS95C-ObkQQjaCJZA1rAKiixhCu0axaw2KoH2E47p3SRiGlw0z-3UYDydby3eHGcP4eN3Ztr4zxVz9yKs77fi5EyjDUJGGzTaEoqg8lVC7SqC2IVyYlSZ-oEAGj67LuRc4uDNGKVDPQ-a0Y-jublAA_ShOlaB5qyCrP-ttO25zQxZJgY_nz6YJXfVBaNZOsYSxSVi4mUNXnFl0j_A9yueKqDqvxgPPfXirFp7_IY7vz48ZJWSI3-bg2LcN9yFgjYPqU6O1q4sDCaR0bDuzr8UI2jvDpYDxRXAISESOf75pD22BgCu-_3mkueWOsHccoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=bxpeKeNJrhWAmylhBVryRaiS95C-ObkQQjaCJZA1rAKiixhCu0axaw2KoH2E47p3SRiGlw0z-3UYDydby3eHGcP4eN3Ztr4zxVz9yKs77fi5EyjDUJGGzTaEoqg8lVC7SqC2IVyYlSZ-oEAGj67LuRc4uDNGKVDPQ-a0Y-jublAA_ShOlaB5qyCrP-ttO25zQxZJgY_nz6YJXfVBaNZOsYSxSVi4mUNXnFl0j_A9yueKqDqvxgPPfXirFp7_IY7vz48ZJWSI3-bg2LcN9yFgjYPqU6O1q4sDCaR0bDuzr8UI2jvDpYDxRXAISESOf75pD22BgCu-_3mkueWOsHccoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=rUATmLfzVT_71JH1iMS8myYoEhp6xi1ZV1XM0z1rrwdU78hnluwdc-OTZGPtVTLT-hfkIO05Cj6MIfrxyksdnLQzYmuc4KCQd3kb_oN55ivS22iyFWXgw8ZImEXSGfFqETvFOESqW9zzmjCaJt2nfiVLiJkrGolSkybxEqA7Z2RwnG8NibjboPGez2gaqlJP2zkw8uPEz-lI4vXZRgfNj9lF-oc0O1hu-kQzimaCXs6yoLbkmMDsdFU5_D8BJ4D1i80P-qtDUt7nVJRS0K3kGp9Du3JCLI3ZhcZp7JZ0AbiTDV6L2lCsski13RHC0rnogO2DiTbCyMqX7f50NyU8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=rUATmLfzVT_71JH1iMS8myYoEhp6xi1ZV1XM0z1rrwdU78hnluwdc-OTZGPtVTLT-hfkIO05Cj6MIfrxyksdnLQzYmuc4KCQd3kb_oN55ivS22iyFWXgw8ZImEXSGfFqETvFOESqW9zzmjCaJt2nfiVLiJkrGolSkybxEqA7Z2RwnG8NibjboPGez2gaqlJP2zkw8uPEz-lI4vXZRgfNj9lF-oc0O1hu-kQzimaCXs6yoLbkmMDsdFU5_D8BJ4D1i80P-qtDUt7nVJRS0K3kGp9Du3JCLI3ZhcZp7JZ0AbiTDV6L2lCsski13RHC0rnogO2DiTbCyMqX7f50NyU8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=jXshcZ1Bq7COidpo9zlXSBqJmlqyG-1EQohnf2wM5KhbP9mJdUeXBPx21R8H7HD6iHsYvxiXO7jnoy7_g9V0E1jSyJFRPTaMFXtyv7ZzvYOFEl-XnxW7zE_e6U4Jq7T3TdCeENEgZ-Tk_15VPTBPy3xKDxeJiY3SyoFsgnzn-hUOUfot8VMSp1ytM--k4YObQAgtPGJq6bYpdO_JVPTxt2bn7q77do8ECJkL2ecZUQOckge_ugCSx-SLcPpmKMoWLyvtohtVOu80DDEDONwqQgYzKu2_7Wr9QGVsaS6L8GRRizU9IsLtq7DxubRQKVqKhNc_wzw0bgHvr5R0y337pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=jXshcZ1Bq7COidpo9zlXSBqJmlqyG-1EQohnf2wM5KhbP9mJdUeXBPx21R8H7HD6iHsYvxiXO7jnoy7_g9V0E1jSyJFRPTaMFXtyv7ZzvYOFEl-XnxW7zE_e6U4Jq7T3TdCeENEgZ-Tk_15VPTBPy3xKDxeJiY3SyoFsgnzn-hUOUfot8VMSp1ytM--k4YObQAgtPGJq6bYpdO_JVPTxt2bn7q77do8ECJkL2ecZUQOckge_ugCSx-SLcPpmKMoWLyvtohtVOu80DDEDONwqQgYzKu2_7Wr9QGVsaS6L8GRRizU9IsLtq7DxubRQKVqKhNc_wzw0bgHvr5R0y337pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-P76P5etRtsb2pcbQk7ZOdcareEc9RdkGw6WeZp6AO7v6cJQTdk17eNPnFwbhlm0yigB7NqH8mGv2buIcRF0mqYXKrEaeay6KIOYyw-xl1vy_2QH8G-55kW_Yu_nT9CCfBJpFpCmO85eu8GYcwr7O_7-UGdz8ZxL-DeK6Hym4KnPU8O-QV08TpYSK9wr0MmOgNeixG79NyCYg2kdr12Pxn6dnhBy5o8twot6cGnc97Uyf-qhPI2QrIpeS0cwHeK8Pgg22_NAzIkP2UyR8HlJI8OFt2uWOHpl5Dt4ejWbZdR-5jJSOTUG-e2Zvvw8wDT1LtTCb3gD-kTMZkle_EpuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=IGv6wFyYHxEYMXjVROiMf9hGEZ77Q-i9Uj_M55cwg7fdElkkmeGkFFCZyfrpnyUXsO7NCCcZcQc2xhmW5xQcLfmCu0kB-kDZ-IHGgodLEICx23FI_WCwHiggSFClgZmYhfiWrsLIJR7Vg8u3F8m_pBvaxOwAxjorB4eX7QiWWWY0uWrj9_sqDzu0xgdAF1jcBgJdSxOIC2MsNv3mmTUKQSrqf0fjI7wbeyU8m3KVSu4fHUVoXAt4dUkAqQ2NPRsmaYS3E-KF71-pHvs9tyYIipw2DE5k_IQDoepteQdEpLHUhIzbyRrIM-e5uVMutVt5XkwlM_9GVrCvqbunolIl-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=IGv6wFyYHxEYMXjVROiMf9hGEZ77Q-i9Uj_M55cwg7fdElkkmeGkFFCZyfrpnyUXsO7NCCcZcQc2xhmW5xQcLfmCu0kB-kDZ-IHGgodLEICx23FI_WCwHiggSFClgZmYhfiWrsLIJR7Vg8u3F8m_pBvaxOwAxjorB4eX7QiWWWY0uWrj9_sqDzu0xgdAF1jcBgJdSxOIC2MsNv3mmTUKQSrqf0fjI7wbeyU8m3KVSu4fHUVoXAt4dUkAqQ2NPRsmaYS3E-KF71-pHvs9tyYIipw2DE5k_IQDoepteQdEpLHUhIzbyRrIM-e5uVMutVt5XkwlM_9GVrCvqbunolIl-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=OptdP-iISXBPlNr892sqdPvvstPFg8QAHvsync2EOvGF7yKQuC_ueDl6rX_DrLjYPLYY-1TpmYwdG3arRsAOOPRFhmizvpHILQHBksnjT8NnwFb6btnfkm8TVC2NYhqcacn-uGsWiQgF3xQCwnsKonlBTsDu3LHEV5iP-mpVMv-4ElVJYeVjze0xRSIhyUA1tmtiBpA77rEwQfAgxL_i0a6bAPzRsd4iMHkyvZQgGWiMj7GAxLHA_yONbeHIvAg_i0EJksVkQcxq5v3epqb0Vtqq73iKNOM9kTsmcNxeGllGLRTTqlqR6bnsjiTs_iJ5Ownq5avHc_QMlgSD-i1N9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=OptdP-iISXBPlNr892sqdPvvstPFg8QAHvsync2EOvGF7yKQuC_ueDl6rX_DrLjYPLYY-1TpmYwdG3arRsAOOPRFhmizvpHILQHBksnjT8NnwFb6btnfkm8TVC2NYhqcacn-uGsWiQgF3xQCwnsKonlBTsDu3LHEV5iP-mpVMv-4ElVJYeVjze0xRSIhyUA1tmtiBpA77rEwQfAgxL_i0a6bAPzRsd4iMHkyvZQgGWiMj7GAxLHA_yONbeHIvAg_i0EJksVkQcxq5v3epqb0Vtqq73iKNOM9kTsmcNxeGllGLRTTqlqR6bnsjiTs_iJ5Ownq5avHc_QMlgSD-i1N9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrjhypPlPrAVO_NnKVAswXc1yJNbY3ar_u0dDCrgK-7fv4P76nWr9ZgQON2EPU17024cZzyIzYYnFkOa3_w9ZZm4WZENDd81S_CyHNZ2gB3F1WG3f95H3aHE7qo_Wib98V9PNo384iQP9uhqQn0GCqVbUVbQvPBQZRoqH3bq0avFSX8Fqbk5KgupjADAV5C07uPtZ8B6Tol4xtoOPx75Vhc0FR5HDTV1zKrGjAdL26t6HXmQE5nG94eXzpLfBMGrqsu1khJHblP1bgOr1t4JkMcj6sDTDPGNJQOlOpm7kgEg-Oun2o0iJ1mFd_0nEfFpyn3qw1EojKyCTZJFH4jshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrqPOYS__68JVdhayU91QsLZdkbvm_HCEyuz_0G3dHWZYoXd3j_ELTJY-flan9_3BGhDbDOl-J2-ZvZv8daGsdWc8FB4pePcguHWw4-xKSiihbMk8ZWNwPNrr9RDA8Re79QOV-GZHAPNG8gVlGez_KgEX8lym0G8VQwuR943xsu-RnBnwLqxF8fCcyck5TSy48XzAszl8ux0QfdIyjmr7ugvtQCgZz9hHPFefbbKrzayMRZtACGUvcadOdRHL4qHMcmQG_G0wHQfGZT6yOCAsAnSRrnfEKODz2N-Aw6p2WjKwpHuHVWQZ9xLiq5myOMgsxTuX_82fNJyS6E-DgAgMw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=EDatWcoNvUVkyslYzQ7HP6ks-Ygkx_OkVe8JEvRDWKFFHDBT8r6dnYmsked8B7Oj2QGXkIudiu1Ty2Lx1gFuzr7TeFSSYraMWp1FgOQUme7IPL_uA5BNCZCO-yBcplKoThC8tvwLY_FEPZy4ftSbPrDWi-AzGUTH8men6BPgja7uJex1DvuiJvJRUY2dm0cC2YY1dgLglaPXGtde_HQdEeWP-LP9MCdSLJkSRGp0lutyC5W5zIaOP6bfqdUvTbJgHvXvp5gE6PNAb5sR9EoF4Xw94aCeVqTet3pHLHjkiwSnHpTF3DMZbWBIjZMdMWy20cMgJzviF-uLgNbXvJaOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=EDatWcoNvUVkyslYzQ7HP6ks-Ygkx_OkVe8JEvRDWKFFHDBT8r6dnYmsked8B7Oj2QGXkIudiu1Ty2Lx1gFuzr7TeFSSYraMWp1FgOQUme7IPL_uA5BNCZCO-yBcplKoThC8tvwLY_FEPZy4ftSbPrDWi-AzGUTH8men6BPgja7uJex1DvuiJvJRUY2dm0cC2YY1dgLglaPXGtde_HQdEeWP-LP9MCdSLJkSRGp0lutyC5W5zIaOP6bfqdUvTbJgHvXvp5gE6PNAb5sR9EoF4Xw94aCeVqTet3pHLHjkiwSnHpTF3DMZbWBIjZMdMWy20cMgJzviF-uLgNbXvJaOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6bCgr2W43Tu8xUGyIHwx7Eh7YByzb9Q2sAxi6-__qF6mqS6SrpUUChaFevIhndV2QVbAhvnnscU14r8CP50lV39zWywZWOb_Qbz92m8XulFyI_Mm0suxdeqd2q1RdWU2RczELKCKhDl6avwGKQrwuTg0XTaeEWoJkFL1qkaALxHFvUeYAp9TYZKc9R1tKGOAJRdm_VGCT7iWl5TxtYHjcVQOeWC30IGiSC9aAGp_E2otCx2D3TL-wUIWq-PeCHgMkw29XqLA3CevfkpEqprUovBTbjkMwtH_6JiKRlqIi4BSISBCH7cHkQdydxlJVGhKChjB7shcvppXpcOZWMywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHV7uN4sdM_FEqm2BgQzt7BdDC40hx7n5f7_P6AiS0QgDdeXlt_xrswMH1jV2RlqjCfAjXnk48qB38Rcr4vt4h-kqUU_-vcO_8ukBMublCyeGznPQppf2UdMjRSNVLbiOylKN8OfP0x0OXd8o_l1VoIsQQSOGiA3TdpeBG17OeX_5dkgIII8WtMhhEhCDTrJob7jWa3xzMuQLJf2a8mjf7DbyMprteqDoAdf687z8rj7RDtxJdsw2Vq34pUBDAqjCGunHN04dUMiPqLc175ZoQb-hw1B2PlIGma-K8qsw8_cEmWocUU7TTHn_ugr_KFicYlqPxbe_laKGBnu_s7Rrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6lpEMJDbEiwasK7q_y4uh9yKsh6Mbcuq0ocPqVszU2zHLd3FZDZ59Ei_of5oVeDp6j8V6OIKv_Y4BqH0-WbGGpg3waPtPTspFxQ_piDFjAvE9eIT_44Xx12LC_caaEWbirc6R73SESsG5BdukKS3_1klHhiEYyhcAyqApRkWSq0Rnly2VDxOiVlZ2_wQoazVeyb22mwEiixcevoE_zQKiTx6AeJVaXfXn2RFx56arUeo9lpP4BQwRqmPK4WBCwM12FELRCBctPdgeo6_sVU6EDVQ7BVwkPhk16mPnqfUDjr-QWvY0LMAUmy1DfeQnxL9vOPJfxmFS0ce5hjxmXufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Y520zZqDKEJKrKHBoFQJdBgNDW8hx4zoGg8B2gKVEX7QYAj31Dw8NenAEMikq7aCvwhk4EfJeSfXv-g6ch8RjkovSua42gYHoWLhDdCViJ9y7FGVCtFgAW8-uuAZyD-9WgFMIePVqz9ouMtinbUHlC0DiA4LAyQMh1sjI3ZIS93qgeFhOhi9aewfAm8uCXgbdtIdM6BzWagGRnPKe494oO8oJmdBuF8Oj-KACTHb0ddvBkAt04eNhWufmGX3LBRWkQ5DEDWv2ffmgL9b-j7LWRhhGx4_zzUSsO0y8rrgbv0tYdmzkR5AtRRjrm13SOTFYgSaWC06yJEwHHRgnSSUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Y520zZqDKEJKrKHBoFQJdBgNDW8hx4zoGg8B2gKVEX7QYAj31Dw8NenAEMikq7aCvwhk4EfJeSfXv-g6ch8RjkovSua42gYHoWLhDdCViJ9y7FGVCtFgAW8-uuAZyD-9WgFMIePVqz9ouMtinbUHlC0DiA4LAyQMh1sjI3ZIS93qgeFhOhi9aewfAm8uCXgbdtIdM6BzWagGRnPKe494oO8oJmdBuF8Oj-KACTHb0ddvBkAt04eNhWufmGX3LBRWkQ5DEDWv2ffmgL9b-j7LWRhhGx4_zzUSsO0y8rrgbv0tYdmzkR5AtRRjrm13SOTFYgSaWC06yJEwHHRgnSSUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=hFZ0BCHVskH7j9WfzHVBQ4N6TG_IV6EzLnNwrDSTrxQn8d8SpKU1HOVslhBOWuQUgmFBTiETA5_U6qW_g7-ADm3vjLEmv8cLMygJ-VZ3tlAw40qGUoq_YfkHU2NHw646tKpvRSlWFP-839Etd5bg6Yi52KD41TPpC3qLNSB-fAAlewHd62ROZYsO5CCvy5plZoBd4IUg-tm_K5k0_KUJL_OYSWRNgJD3a0_i9_SOw3mZfPkq628icJVybP5KVjX9r7Blb140Wb4YTZPgZJNxXVBBU6YgpFve3Wh_P3xvtpeF8XL1Bfcw34Rs6pfv6nw1c6h7jsvTxQkCeJ_SWM1rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=hFZ0BCHVskH7j9WfzHVBQ4N6TG_IV6EzLnNwrDSTrxQn8d8SpKU1HOVslhBOWuQUgmFBTiETA5_U6qW_g7-ADm3vjLEmv8cLMygJ-VZ3tlAw40qGUoq_YfkHU2NHw646tKpvRSlWFP-839Etd5bg6Yi52KD41TPpC3qLNSB-fAAlewHd62ROZYsO5CCvy5plZoBd4IUg-tm_K5k0_KUJL_OYSWRNgJD3a0_i9_SOw3mZfPkq628icJVybP5KVjX9r7Blb140Wb4YTZPgZJNxXVBBU6YgpFve3Wh_P3xvtpeF8XL1Bfcw34Rs6pfv6nw1c6h7jsvTxQkCeJ_SWM1rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=pvvxNIKF7ehFM6Djld4oLdPhjSfwh7ZsC5O9r7vibA5r3rE1sDHz8GllNFHahRdc_0-JJpDAl--yECxcsf3vtkLP6ct9sPCx6VXyNQBHILg1yIojmDbYL1dXeHWhS75xNly_FUWLietXzAbbnJ9O6V1mF32csBNKM57h8TpfOWvl5NAMAe5ArUUzGZFB0JUU1Q31bYops8jWILdubApZeteNfzcRVuGKj1_lVAACgO7pignxIX-p7n-r25d7rcES9ojcPZGnzIlYyA_vYwk2BhaQ598yz47seHq3gfBMwu9mqLfN-4DSphGBOiiqo1KATPoY6dy3e5Y2TCpAqCuMI45qxGQP5DhKyzONfDVEhCWFa4WsP0O2otFAeI9zqpVzT9hjKZBCVp8ISURb8g0iQ3kQGodB6eXLE4KavE4mlpD5bwQH1F0fMccSt0AV7Az6UyU-961t9fuQiW2AVXZtUWClCg17mD97ntwOp9UCfi0B4ySQq71sbDkrpjGhgcwdTJqO5CUqX0dUHvsmOTXktNu08PVOde_aTkKd3F6-8T9VdvNURTeiNcscB2hjXyIiZUlmul_CPRA53fQJszGneB1GLuFs-xR5vT6HGIBwj8eHYGso5Cv-xvhEHItPC-MqrDmKYY9MwoCG9IhI-YeDzduiZoGQkXUifK5akfnlf9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=pvvxNIKF7ehFM6Djld4oLdPhjSfwh7ZsC5O9r7vibA5r3rE1sDHz8GllNFHahRdc_0-JJpDAl--yECxcsf3vtkLP6ct9sPCx6VXyNQBHILg1yIojmDbYL1dXeHWhS75xNly_FUWLietXzAbbnJ9O6V1mF32csBNKM57h8TpfOWvl5NAMAe5ArUUzGZFB0JUU1Q31bYops8jWILdubApZeteNfzcRVuGKj1_lVAACgO7pignxIX-p7n-r25d7rcES9ojcPZGnzIlYyA_vYwk2BhaQ598yz47seHq3gfBMwu9mqLfN-4DSphGBOiiqo1KATPoY6dy3e5Y2TCpAqCuMI45qxGQP5DhKyzONfDVEhCWFa4WsP0O2otFAeI9zqpVzT9hjKZBCVp8ISURb8g0iQ3kQGodB6eXLE4KavE4mlpD5bwQH1F0fMccSt0AV7Az6UyU-961t9fuQiW2AVXZtUWClCg17mD97ntwOp9UCfi0B4ySQq71sbDkrpjGhgcwdTJqO5CUqX0dUHvsmOTXktNu08PVOde_aTkKd3F6-8T9VdvNURTeiNcscB2hjXyIiZUlmul_CPRA53fQJszGneB1GLuFs-xR5vT6HGIBwj8eHYGso5Cv-xvhEHItPC-MqrDmKYY9MwoCG9IhI-YeDzduiZoGQkXUifK5akfnlf9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=PowhBmzH-HHSMk23vfzZBOaNkpICw8J9gWDmNGkNSNUJCXoCDUG9mkUcKGzzLh8g-3SPQGY7AWYemkMrKbnYSsa0l9Tlp0jSESvP9G-P7ClN_brQ3LviOzi-7UURXqdfcNgwgYe6wRZTHcUfZjeTnf5ktvNWDiQxLUe7RpQVCo7diRI9zCmDRQuw-rTU5zhtMKk2CwipOa4iNPNl937hv74d8UR_DRMNErUHFeWRxYNeCxgwVHflFFcQPc4kTxZMFuplPcNQbiiGv42ugy8xQRr7noliYhHbHRq95534hDbSs2nAtKBgQR-FApb3aUUQ_NEE9QWQveTUje28C4AwXbqUCgklyD3wGUBYgTYMqxT4wOAcn6yY9ApidS2NKrshNV8bt3DJFA6EfzqdJwLv1DGCXcIG1J60mscTMCfH6QyY_BLjU_RpmgV_uaOd1niPKSUeD_o5hMoqY25vCSZmr25JaOEKSEpa133YB-fEfJQIMMiFu24gmEQFe5pqUQsERP7yEC5X9pX9RhCUzQ4U1oZqGmC1A2wpkfb3bHho0ABQrwKDxkkQjKsFvOpS7AYY4RZrRfI-IF-p_RIMPn8ve12M6veijH2ahDqgGYdn7Z2wAxiw53znypapvM1YGkcShExKGqRX_aw81CA-avZXF6BT9U9xKEHwQeI6eDulSTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=PowhBmzH-HHSMk23vfzZBOaNkpICw8J9gWDmNGkNSNUJCXoCDUG9mkUcKGzzLh8g-3SPQGY7AWYemkMrKbnYSsa0l9Tlp0jSESvP9G-P7ClN_brQ3LviOzi-7UURXqdfcNgwgYe6wRZTHcUfZjeTnf5ktvNWDiQxLUe7RpQVCo7diRI9zCmDRQuw-rTU5zhtMKk2CwipOa4iNPNl937hv74d8UR_DRMNErUHFeWRxYNeCxgwVHflFFcQPc4kTxZMFuplPcNQbiiGv42ugy8xQRr7noliYhHbHRq95534hDbSs2nAtKBgQR-FApb3aUUQ_NEE9QWQveTUje28C4AwXbqUCgklyD3wGUBYgTYMqxT4wOAcn6yY9ApidS2NKrshNV8bt3DJFA6EfzqdJwLv1DGCXcIG1J60mscTMCfH6QyY_BLjU_RpmgV_uaOd1niPKSUeD_o5hMoqY25vCSZmr25JaOEKSEpa133YB-fEfJQIMMiFu24gmEQFe5pqUQsERP7yEC5X9pX9RhCUzQ4U1oZqGmC1A2wpkfb3bHho0ABQrwKDxkkQjKsFvOpS7AYY4RZrRfI-IF-p_RIMPn8ve12M6veijH2ahDqgGYdn7Z2wAxiw53znypapvM1YGkcShExKGqRX_aw81CA-avZXF6BT9U9xKEHwQeI6eDulSTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=jrUApLRbHUr2PqSeGK9so4dlt9dwvMDdBTGOl4jc1bDv5Id1AAsZYo_ql7Td74KpT9Gp2PGp8x0HbuL1o5s-CHmTnWWm5cJrQDzscwk1jtnIcP0sjUVJfCxw7oSjMrPFVZTOWYhBZOAyyF2mW_GQaxHhAHz0lkbK15xLBztQEnmuKqV3DtNUEQg_4D3sIr1dlBy6sJe-3dGA7vJmjeMARNWtP6E7qKP4GH748zdcvs7DFGtDi7g6mFjG1WtTP1x1vZ2NyNuau-_6TCLcsZZqOtin4Y2xUHpyt_bl8_VIWGNnsks0JqBfQmLC-3yvVGipQ1nb_hvfyKYJ92MuPMHemA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=jrUApLRbHUr2PqSeGK9so4dlt9dwvMDdBTGOl4jc1bDv5Id1AAsZYo_ql7Td74KpT9Gp2PGp8x0HbuL1o5s-CHmTnWWm5cJrQDzscwk1jtnIcP0sjUVJfCxw7oSjMrPFVZTOWYhBZOAyyF2mW_GQaxHhAHz0lkbK15xLBztQEnmuKqV3DtNUEQg_4D3sIr1dlBy6sJe-3dGA7vJmjeMARNWtP6E7qKP4GH748zdcvs7DFGtDi7g6mFjG1WtTP1x1vZ2NyNuau-_6TCLcsZZqOtin4Y2xUHpyt_bl8_VIWGNnsks0JqBfQmLC-3yvVGipQ1nb_hvfyKYJ92MuPMHemA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmIvV9i8jQ4eV2wlgkv1Wj2r_HcRvNI-Pvavc0K2x7GohqOiuUnP0fBMatvyfpFkyIOkcQz6EgeGgeQNjx8Xe6HYFjgOkfThsekBh-Gli6wYl3kZhLIDzmJc8npcQ2tECH-6X7uwRddv6q6ChHPbMOU4hOatPTYZS39yPqFJvaXWEU00AsM_1gPeFCfjPB_tW6h6qHau8U8WCsYlRURWfaUjxq9SmEBEVBnz3en4clJsJGy7zynzfPaOQvDP3JlIZ5WmMf72ywqIogE-Cm2_NiIn5GqVDypUNo0YcTJCkpms694xaTvuFzjDWF8xJMTYPT6MPKbJho3lvYyDaWyRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=uKpm0otwAuLYZyp5XvIc7LBJV0GITqrhcrp19Z20--8TZxBwtQHU0f45ZRx1s-caG6GlPo073nGIyu4Qer3Ck8-LRmKqMLK5AWO_WAzUFCGRqxhkr6VhR-V1xpNc8Xy6G4G7plyhXegOGKnnByk5tiwv0eOJycdQMcdq8H267SPf_xJW-ihnC7Iku4CnQiFb12EyevFFY378MBo0lhfW9aXh3wVbZ9a_mphlBkgaZKRKsMdEa8FjuMDXX7KKB3SuZQhFWurEUQv-e8uxh46ndi1MNJRsFrMIdHLheM6uzB5k__me27leVFKSRoVfU_HuCVun4Z7UD9932bj6FXiTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=uKpm0otwAuLYZyp5XvIc7LBJV0GITqrhcrp19Z20--8TZxBwtQHU0f45ZRx1s-caG6GlPo073nGIyu4Qer3Ck8-LRmKqMLK5AWO_WAzUFCGRqxhkr6VhR-V1xpNc8Xy6G4G7plyhXegOGKnnByk5tiwv0eOJycdQMcdq8H267SPf_xJW-ihnC7Iku4CnQiFb12EyevFFY378MBo0lhfW9aXh3wVbZ9a_mphlBkgaZKRKsMdEa8FjuMDXX7KKB3SuZQhFWurEUQv-e8uxh46ndi1MNJRsFrMIdHLheM6uzB5k__me27leVFKSRoVfU_HuCVun4Z7UD9932bj6FXiTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=WAT9e4gPnjBfZ8n0IEa4aFRg9sAlgmYmHqWZI1LUGraEC6qedNkLKikfL9cxxTOEazNKuDmX3ow8cdhGfdbpmk1SIZLDsnVDxpHArs6z7o6TAaornaG59Q1vfZgWxkddsqP8wc_uP_7_w8tmjjSO1oFbzAnimiWr0XlHt6O4420eOjaJ32Hzh4FYTnFMTk8rL8tXOSe64QC9XPkILFWPAJsRJM5lzMWMSZVJCQcFJ2Bg_nWiwqqZmk-_NsEcPQvKKNZ--Ro4u4An8ntRYc1xHXDXjg-ncf5jgg240Dgu_601s4upts0RyhqSrrsZalU3ZI9pg6487P2YRydZzUCpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=WAT9e4gPnjBfZ8n0IEa4aFRg9sAlgmYmHqWZI1LUGraEC6qedNkLKikfL9cxxTOEazNKuDmX3ow8cdhGfdbpmk1SIZLDsnVDxpHArs6z7o6TAaornaG59Q1vfZgWxkddsqP8wc_uP_7_w8tmjjSO1oFbzAnimiWr0XlHt6O4420eOjaJ32Hzh4FYTnFMTk8rL8tXOSe64QC9XPkILFWPAJsRJM5lzMWMSZVJCQcFJ2Bg_nWiwqqZmk-_NsEcPQvKKNZ--Ro4u4An8ntRYc1xHXDXjg-ncf5jgg240Dgu_601s4upts0RyhqSrrsZalU3ZI9pg6487P2YRydZzUCpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGWIPCjyLS4M3t3u75I8YZaCn8vFLyenAnpZ5EfXiYXRsagdfJSrvIGc8F2BXWtHHvoqf2mJsp3kdqwTehrgvjCiUIscq6W8Dd2qrV0fCBSRKuoztMQws1JX_Z7XGI16FH_AfM1ovmr9_BPAHvmI6yQGpTjIupdhkLwAr_mjGKikckH_wy_djfNz_suMXw_b76DaKxYZiozuYKXbyPxjLaZSnn1m6umY_h0j6mBhZyLWgnqtfTAVOdD1GjhS74Sk-OFz4kN6ayEpU65Pk8nej6yA-shWjTSP5_SAq5qREobBgYNApATqSSGgyiYs1tC6V11uL5U-dGUqoMD7PQjBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJa32bKRb3gDup3ssb7gZePOEjQfwqXFfSUeSYxr58pqPc6allQuwYLY6bpCa8PASrGzIQ1sFpLLAY1AdVqujWUuvHGQJXboYXXq4jF8665CsdJoHSlIg9Qx5A-neq49iwRH-kECTxGl2eUvvc0aELncQEv_givhR2Gsoxg8WFYex6aU9TWKMBMXp24HzqLLmX1iIWAOIdfCTX9E-x91gX3F4rLrmwc50FjnzmyV9B913oFjmUlGst2JP497-09Uf0lmb2dTxexW_ce7YcCzOfT15MXzWA1GwfUnLJvIsPyk1hOE0LROt-KDtUsXHCsWrUxFJmLv20Fwb8vvJGf_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtyhCB3wiNyEPKvIvMcBGMy9woV9T_V2PN8tgvEHZD83VFXEUlwa-F4fS2_o8I8xfou18BErr1uBwWw6uU1YtIo5McVGqKO3VJnNt4TzIjpudftvpHiTZxjP1aKce8IjiUThFIl7HRj5S3PHiZd9BY4yzbZlQV3777qOgU0A1iR-7OtjyTYJg0nXLKx2huveEW2E0xIWsUB8yKxHFtprdAf1hAE6vR9eRBSfZp0383ENRaZmwrjIz3v1efsXEN-PIU34Utv0NxZbd7eOHhP7-z4A3tPLcnQQGkAA3PpDuTGG1FeoPOBD-dK-YHaGjgLYsVE6IBDuKz86wXXChzdm2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh3yGljo_4d9XrVxIT8cvbW_WrEhVtQqdKX5y-_cvW2U51YRV0TIolWKeWvJcO2z6t1FKQeVKOiCbqfq4CLedqC_Hsx-UHvZXClf1et5eQtnM9PQDi30IQYvem2M-tRlyAauh3OLjGknrjiVN3gE6zuDGnhWOpkVtT0Ebp3a2v1Zq-2YFV5buYo8gOXEh-vq-4cKIs583t696e2UhU6qbD07fTMHcz0uRkNX_ULUQlK-Hzy12v4OpYXatKdV3pyGHR94hRMi7x5OVfrbxPcjQUAN0jU3434OhSrztZHrIRcB90Lwgwauff4w4PtKTfuHb-_K73rLifpxUBbDzA_foA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UClyhJ-na0dOOb9eeTWSvjDnuHKVMr5botf-cxpBykh9MLav0oZt5fORgZZcwiOqRVZJrTTJUJHVCRkTxgSFjlp8SGVedHOOoyXibjv40iBh8F-Lc_018xvs7iB-cu0RIk8eIXa2RHjwOHtAw8Kx-kw6ADV-KpsrhfD-GZAUTKWSh2x7JjlFrTMQeiL8-k_TwH8PXTxQfuE6_apZu_5ItnVTG2oxq5P6p5fnM8ou3JHoXvPkUT3h9tZvtCNXdWMzI_MW4efUQee-Nyqh7MQUVOEl2Y2qU2AcsxO99c-nPWhRQQfS2ReAoY5WGbtqL6_9sw9XBQio2xXCiaF0Zq7BLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSzCHvhhFQBJVJJGoRgTsaplXl-C6yCTNK8GBcO2ag2yfHF5xZ26pAekM7eLvblM3J0o0HQ_3khuMVBy-7HKbGiEoRRKl7MIhj-GNZPbYFKCFIr9VwymB_tdPTnsqeXrVENO-IN887tThtEa0DGkjotpgnRitMPTvHTkMxo316FAmKCgTnpVd8ItNL1zPzmQnzX-edn1KUVtBw_wXZ5KdhbgbxhV1aVfBOQR05yZOHJRLb11V-msXsnOQqNwZDCONgU7MFdJkCvwjxZAcWT4BkUqt1uYKo7EW7u5Aq-Ty3B5DcbCDLajN8CiZv_mPwTGhPPSlwGXdCxrk7769Wmy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg1tQ-Jouo-utsyzvVCfWIgLLPHJp1Iqe39oATbAO3rxeReTKI5fLG9cBot-tqkGrZNZ6a-Q5ijKpbyrKugwGcDyUz6DXdv4J9MbgMRXwOdooS35IXQMJeA8g6bJM14_H4ufSRMA4U-5rJOnSwwn-S_oachJSgxLy0L2nyuS8Y_Ne_3xgkC-JhFn68axrBqnF60RQKj11TzMzk2HfHbeB8cdNrK2meJR5jDhw3ySsSOPysz_qQO-6MEsDIWD_d5Q-qIrMk9CH11wuGUdXN6b-AU9s1idQqNkip4soxIQyqq1SOum-RdIUXnntaPb4phZCbyZDxlgY0kUTQkeDrapug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2L_fKJC9B7C43j3vVs3vvnBxpNsVE5sTVCq14yLaX6MBsd_7mcGj6S-AJBtb5iRzqi9C5tYrOsI22gggQqvrk0JLxqdA1m-ogxEkdQSdeomSrz3biXQx2kZSg-oFWtncGqJDuUO3JJGzzsef6G8kh1gljTZTMv8U4ciivmdQZ3KbKKaEthXgRYwLRHoX3b7Q6DgC_SEG11TusXdiQk9pW4-PmFv0bt-v_w4fZzZN-LBRPrcf7mvdCj7Qqie8qPSXVqItHRX5H41ZCmFWpMfaLXc8BLJRocmgO9mLa6VJfFMibyu19RcHTVwIpTUsAT0iWJXh5VosJlLNMrNjFjFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmLedKvacZyTgS8plNSXk1ZV74Zyr-EjXxtKVmpH_Pm-9wSTu6mzE1FMxZ-9PGCoIf--QDAnWqjyHK_OzvakpRtGxjpNzmW83x_QvikVGYYSe9GXHaDc0K7kcfhO1liAggG4_g0sY9JkspVi17ty3Hi4fDXNDWxC4CUhS1oqdWM1Boe_4ksuP1Dw5s8v3AqfpUv_nzHpuE0okkNE18jGWUJ2wUYTTn41Fz_dxawf6hb1K4tKSXS-Vxfdjz0FwqjFwQmnNwmT0rVW-dD3OiBoYg-cQqZspQOeNIk-GzBY8TeQcaR4iwhXf2R7UMEHZOgvzOlFn8-4u9vFryf1DWjEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9cKDaryBze3aue56WaVUTRXE4XM4lL-5TKrVNv7pGklX6i2wR-5lWTrJKIyzKZICGdFo9SigZv2gFnlA_9GBZPkDDiMUSPaTRrXvQIlw2gAyMx8HRg9j5xPZWwFfQROrpcY58NsvLq6aYy0yNalIFJnpyXqrVtq1wX4c_Dwxx-8mWidJbrjukLOyUPo9GgvLPRuwttdx-_o1obCLs3UIzRYYRq04fXPUO8O1mbkHchTisi1CoYRTA5FRvPW1BZKxRi2qXJwRBHyLSfDmqkuYoY8QM_TQsfsnx6aF1YpkyDebFct6A2W2-QTUC0yN66FG8brjQxEnHxXYtngAtgVMg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=KSRzQ4weG1kikfh7gU1xLhRyA_0Qt99xy9P2FTCrUemNTCNDINx9Mky6QOxGiyWSUsieuAB0rymvXabB9RqxM8EWFuhnivwNcejpGEv0FBbroKqCt7ISzOf9eiKUbkDXMdhTsSOUvWVce_GnD_PqaXr3EBsTvwY-yRzuR5-5AnnVqYk0-42qQAMm8iex4-MQYLho8cJ0OH6_ZPJGHpPQi5XG5-35Pws9f2-P3NXMqWfbstzvzOARNODqZtD1P92dw1JzsnrmwQ2NWTfD2dB4U7dYUMh621GQmj0wfmIlNbDQOu8znEwAMsaLfqb7B2GW3hHd7AdWtVHBXwtOfFAZBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=KSRzQ4weG1kikfh7gU1xLhRyA_0Qt99xy9P2FTCrUemNTCNDINx9Mky6QOxGiyWSUsieuAB0rymvXabB9RqxM8EWFuhnivwNcejpGEv0FBbroKqCt7ISzOf9eiKUbkDXMdhTsSOUvWVce_GnD_PqaXr3EBsTvwY-yRzuR5-5AnnVqYk0-42qQAMm8iex4-MQYLho8cJ0OH6_ZPJGHpPQi5XG5-35Pws9f2-P3NXMqWfbstzvzOARNODqZtD1P92dw1JzsnrmwQ2NWTfD2dB4U7dYUMh621GQmj0wfmIlNbDQOu8znEwAMsaLfqb7B2GW3hHd7AdWtVHBXwtOfFAZBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-Em4rN7ljRTsNiagIFmsA2gh3PL1FCYq_D_b0qV7orxbtwmTQpeZhH_mT6bH37aEYOuwIgKn7W8XS9vWxebsktdmBq-M3RE3Jp60SIKnXgHoDv9cKbh4bAB2me0dmg8hw1Yn1LA_piTwkLxB1HGIW1S4PhMzQQa93EBtG_HTTBNAzbCnf5SB0Ifyi30a-htwGViTmZ3ZRr_5XJEFC_n4I90s44aFkDlm7lpEZhY669xyokNT7GuVV_OYbT-iK9jIfW0UXyU_kvDiRByhuJnR8gheHhFP1mGLxh429KrUPQIBa3mf1pnMKHtrawwAYxbzh43cU_fbBaiD7wyrFsTnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWAMddA3PamcNGOMiCHTcxwssOzcdNbmmx0y0MSHTJSR97fwn4rBk53B3n2ewWvgCE1qCW8jZaqAb6AJhKjgXlJAbgiIY9epnTBiuUYiBbE-QoN99EOwhGet6vJxHF2iigLg3Qezk7uUXcW8EIFuytPntkBE8OsfrjqB5dXK9y5PgQTJUGp_Kx3-TlaCRPGK1Cc0GuCQ2pvaM2B5B5nkRGN1Td6D7MtHxCkJVvfrGm_mCt-yTe39dVbEhfjybKRoF5s_xqyrtm2Ifwi6tyhtO7KhUBLB6Xvk7k-JGJ9pX-EFzupYEM2NXELLWqDiS1AxOJIb_OmdpPRrm24iJ3c8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=s14QePxMGzBbVhAvjxtoj6lCIdH4xw0xOqYc5mKtnJUGFy3GHCEKBRZYK-EiiYoMHoQqU6HgI3zogE7OKVH6cWEXqe9-cNPMAhUt9iA6bM8Sm3vp5bJa0WccEmIqnCGoTWLZvtT529O3h0R3lYK3z-y-g52EuF6parNKj08p9gjA-41ru4sXGPkRsbldg0uUpacKW70wLf6o8wC2c6FvvEDX2DUjeK44EEV-_W96POCjc2GMNcMKOsOl1HKsx_w2xFvEq4Xhye7SjtRBMnNQ26XM68zLvYIMMBw45ssUaSlLAXqenpae8w7i3EE0d95QKcKgL-lE2f-uCyAqqXcAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=s14QePxMGzBbVhAvjxtoj6lCIdH4xw0xOqYc5mKtnJUGFy3GHCEKBRZYK-EiiYoMHoQqU6HgI3zogE7OKVH6cWEXqe9-cNPMAhUt9iA6bM8Sm3vp5bJa0WccEmIqnCGoTWLZvtT529O3h0R3lYK3z-y-g52EuF6parNKj08p9gjA-41ru4sXGPkRsbldg0uUpacKW70wLf6o8wC2c6FvvEDX2DUjeK44EEV-_W96POCjc2GMNcMKOsOl1HKsx_w2xFvEq4Xhye7SjtRBMnNQ26XM68zLvYIMMBw45ssUaSlLAXqenpae8w7i3EE0d95QKcKgL-lE2f-uCyAqqXcAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YxRpNyYyuxKdwNQWvifHg0UO279gM7irLAcO8j2oECL_ecG5J4MC5OFmAGHQ1GALdz0YgENzjP2rlyVtJECobul9nC1i6JmcrWdXUH0dxe2guueN-WA7FRfZWexa0t_bFp3UQWYo2EkpyJ2kPYIBsLj5-T7axl_73KbFWvQpmeSrg6m6-ZLUtgjFg8kupcpaiHvOJwNVyEj8J8q6xXJPcf44_AnVz3889R8Tw6xpCiG802qvNTTPhjNNq4wGed0YVxSXVQOSQPUaBdmX6xJ0x-0H6ibrty8hmodGVnRJitoZUdJpN42HF3D8AydZxaVru7t6U7ZLALmGXuazmecwPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YxRpNyYyuxKdwNQWvifHg0UO279gM7irLAcO8j2oECL_ecG5J4MC5OFmAGHQ1GALdz0YgENzjP2rlyVtJECobul9nC1i6JmcrWdXUH0dxe2guueN-WA7FRfZWexa0t_bFp3UQWYo2EkpyJ2kPYIBsLj5-T7axl_73KbFWvQpmeSrg6m6-ZLUtgjFg8kupcpaiHvOJwNVyEj8J8q6xXJPcf44_AnVz3889R8Tw6xpCiG802qvNTTPhjNNq4wGed0YVxSXVQOSQPUaBdmX6xJ0x-0H6ibrty8hmodGVnRJitoZUdJpN42HF3D8AydZxaVru7t6U7ZLALmGXuazmecwPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SygWh7B26vKhE5V0TFMqA3dgwWwP3pG370ZtWVxaR9-6PPVgOSacafK-JXXYgqEfGB22wMNG2cw466VCIbu3aau0wzIcEIofC5_Os7k9lHbgSYveVb5IX4Gyo3-5lKdjtsT_5JMenA6wVDYymp6vXXqILe8JJjTcNJREVsvTQkHJ40B9gjjZLU5Srbi_xvoZduWgeyYAEuoVeR3BYwJMPFmfn_5bv1eTR3FTfA_Z614Ck0nbgfar9QxdNyxcztJqmjzRFzKSqXihYI8ja2knmXAHNY9ag-WQEsi475VeG9e266x9ZbFEQDPw4wQTwAlinque87UNdJaGB1zu2gdRLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG50E7rKRW7ouGC89WufiPit-fEcW5A_GQ5Ldj8qxmTryR1I5j5N2ybH1VdAPXJfLiC_kkAcKOHYFy_rp8mJ5a88Pb2WNo7Iw2vU0e22zQduEVZGux3eOJ_gJnFmjMnUYGW1ah2zUghfw6HHQ43b5MgrCMN5uj5J8TCtDuejg2m4rRU9MkzGXpPenTGUDbja8_AjHTlQJSer3GCKHu0PtlhCTBMuTPp79VeJvMYoMnhSDwtZAnA7shz2aELTEMxWG35b-NFpCO3R2f8uPyDUI1bn4IE49uRctffDEvfunDto2e8DswIfU6A4z7gMIKYwQn8dC7E2mlHsK9fBExOSKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cflbdDgGG2RZOxVrqH5yfWmtAaZKKAOzSiUySVFdjagmyBGkkpdbD6phgdhWxQt_kIkpYJ4K1Y3pvem801PJVDJ2bn3oS582nL8IDXYtQBULD1WDGBJ_aUVwLIMnJhyrE-6E-RyC_zoIq2XI-FwiOSRAHlWGgusTIe5GNKLXF_0PfIyLeJWrLszknMcCnS_11fCL8w2EjzPB4f1FXCI-tnnmG8drbv9B_E7mpqsoP9wi0zfRmCaB9Uzeu8R0SVRv0tKDxqZb2wom88QDYJ4UUN1dktt488KqNQg7s11qOkH-KCD11rMg7z0YeRVHmJ7kWn5bh83VcDc2kxMeFsYuyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvWW-pV22vrj1d9v5x78GwKRoK2X8QSDve6uSEjm28xEj9venU9dQN43etUJPTt_n8_O_8ZBeKzfL2vSfJn480owbA00-Z8gIWRYb_7i748AzFEd33wnaFLeOl6tUXHpliln4pOpasviTEaj8zrmkwcy7vJTYobjQ1KgXVjvG2KLfOyum29ova7oqEkqjHZAHFFE8AFEvf9dS_sVZr6RjiibvyYHN9bWk34Up6cF9NHJJHdbUDRVyyrFYsByJoVvd8aTYoFrsqX8KgLjbraVcgWZyPVEjwuiO6mGgVHQPzZSmc14YAlIrkJ0z6LMYHTMgTkARmaKYiVvAt4EuMMR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI9-vq7-_D-wvUjzwHHOfRKQPMDNVPOYnHpf-Sg9gZR8q3eXZBfdx_zyRV6vvZV64aWF4hlHPgPQNLHXaY7Pnhrg_Hw6NXC1R-iqmw0qc3811z_NJC6v_uTCIwirAEShVcnfl7l_sXjsIOTW43RlzigGW0LvZwlphCbV7K4BPkebDJqvZ9LO-BJFyUYxxNrJG8i2yNL9wANSnGly0F-5LZNAHQ1wefKKvXt9wIcbfeq8_3e5-nzIZMtpGD7fTnDFxdtLFjzIq8YS-jSxFXlrG9vmIBLVQUeX9Wkm7RmKiOJRupJBsMusJ7p45kx553Mng13KUSYywjToFr8RK_kvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdQOyIMvnVbk9CeUJVyYn1axwwFFmeAOVaR9tvH7sfpFTO1aGAoQ_VIOn3r6slA3cBHGMt7ata3cGvASdxWMQ-JpTaOFSlxnLCXulNsxNKPX_IavNvbnS_TdZwKVxsG1A9mGO-ZhqN8Qthe9FfBdr5dQTq01i6SzxGFhS2kXvENiI6RoZQoFKU5otEh5txMzT1kQuEtm-XU_Yg8m0K7QmeMK1FFsNgKO5ge_hh40wX12KqoDApxbahwom16x-AwAO9QxV_XCiSWeKt1pS2CtRcO51LzwI0BN6KUEiWp3G2mgOWFShZ5Lb1jNM6vvzyR1Dfkimt34PpoPe1IClyzpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCopavd3zaKPJrctNYLPhuW5qm65ne31lvFmj8rx6jIzvmomVXcjnTsJqJ3lR74pUYI5MbsrzYWKmCsXt25f4XCwXIKH7znkUf4jwjuTzgrH6krCNwNBgd9L1RKNO4nR5qcmwUGCiIFALJx2mwtz3gcTcDfOTyxWFZCNN48vG9s4z0MD-jusWIIuNpAyNsOeb9SOmQNzI2kp7CSjqhxMrLi_ZC7IZgSyicIEkaoO0VAYqwW0MbvEMZtwr0yYhLxyGhEVErqz8SjAMHMWZ4F77jiUwciojdaBC2tgUrLi2tvTkOXU_rWzLOZAkgypBb1DYILQOG9qROCg7pYYGc9Ncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1f2AkU0pf-DBRa4z65-8kmq5_ijv9G8Hsvzi-H1odlY3bXv4II3Fb488YMB29t53czykqkOGmApdpIGHog8PoQyYfGm4dEsOyJWCs8wc0GkhjJMZ7dngwQuyHOc38kl-1VXwWVOnwIBpeGj1dHoofgkWYX4lrNrtb4r_zKfbmsLBlAEBVLcg8_okmctDtb3WSgvLbOCPsPhyXwEHpsO0EN1DHgy-lMQcLuEYVUNnbbCgVh_mJ3KpUmLeRHZMJ6LO0vM22t3Xtocdo-ul57_KC3X7wvn-7gV59qCgXo0CQZxnlI4TemxcRlAFqM-ANy6Yc_sgFr4z-Vj-2eEWnfvzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YXy6Npd7sTCOI3uk2mRXuBag4lknDyQ6eSGfBQhvGnv3vmzcBzaKLzgY67LVL18lS8ASSjszdYswKMNGu_dbjP5hfnyzWHv059T5VVI2JwmM1UTaQPrkQRlWLpc2cfO4Ug2ZCR7zNxn88YGrEMqR46eQBoDStSR7i-8RIiEOGvpHSiZgmjp1f8b1Pz9YgTAH7Fe2ogdCHNAGGgS7WiLh6K3uc7r3_ODfagDPV6h-VNujLytfnTqNvZUkuiDAvj1gDo6MZETSXskhmxW_QL3G2kHll0OEwxe5kdaO6gm7Yo8Poc-3IVWL6ZsuwiYrNnzQg6eMqCkEChx11b0ZjfDStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YXy6Npd7sTCOI3uk2mRXuBag4lknDyQ6eSGfBQhvGnv3vmzcBzaKLzgY67LVL18lS8ASSjszdYswKMNGu_dbjP5hfnyzWHv059T5VVI2JwmM1UTaQPrkQRlWLpc2cfO4Ug2ZCR7zNxn88YGrEMqR46eQBoDStSR7i-8RIiEOGvpHSiZgmjp1f8b1Pz9YgTAH7Fe2ogdCHNAGGgS7WiLh6K3uc7r3_ODfagDPV6h-VNujLytfnTqNvZUkuiDAvj1gDo6MZETSXskhmxW_QL3G2kHll0OEwxe5kdaO6gm7Yo8Poc-3IVWL6ZsuwiYrNnzQg6eMqCkEChx11b0ZjfDStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMDX6loX7P8mn-yUdlGlUzhAnFvpIqYhJ2Z7SFGJpgZg7YYHRWXXChUEBIydiY_rwb0ckmb2yLt-AuahYUx7s7fO6eFb0j7-M8SMafp3iaPTMAYEhBhkzC5j0zR7uq74RrHglsonVIQtqucF7wcBpViP6kkoYGoqKF8fpzgGNPfXs29Ki9sEoYhpDufnmyqoAqIzVfvFmwy1H9IEds-lCJ7j3pPu_EyoozoN3dI4J3jb6VTfCAlVOmJzoDIRVjW4BM5h4l7nYp7CXnQq86cI6uSD5NE5kP4Gw2wpjad2SqevIPTXEYuAxBMoIZnHMBdPC5W4sDVM7fqvPIKFMIV1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=qo3UzOcgMZdGSbxccwVVCjYcTezKmKO_l_OxpfbFXNyKSPukpRGt78LOKlGJNW8pweMx0x-CTGYcARP0L6xOr1QBg4Ezc6oDKLuokOxmFr3B0O5Pu0nBRMIvEcGIN0-EOPLq9QNHonZhrZSaITeiKC6ExF8_hFJ5mVp-VebxCVyNeJBb3U9v2oFpcYqALe41YfiUxYb5lfWgw6nVFSn1c8sDOHu-UcdIvn2tS23kMc6CcYJH87Yg5cO2gY-whXWgL2io0_cFx0BeH3mkjlJ9wIC_s5ER_-NFgiHMkJAVI0V5t8QoHRmma3Q7D8pPZ7CndZUUsqcaHcg1y3n6ik6cdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=qo3UzOcgMZdGSbxccwVVCjYcTezKmKO_l_OxpfbFXNyKSPukpRGt78LOKlGJNW8pweMx0x-CTGYcARP0L6xOr1QBg4Ezc6oDKLuokOxmFr3B0O5Pu0nBRMIvEcGIN0-EOPLq9QNHonZhrZSaITeiKC6ExF8_hFJ5mVp-VebxCVyNeJBb3U9v2oFpcYqALe41YfiUxYb5lfWgw6nVFSn1c8sDOHu-UcdIvn2tS23kMc6CcYJH87Yg5cO2gY-whXWgL2io0_cFx0BeH3mkjlJ9wIC_s5ER_-NFgiHMkJAVI0V5t8QoHRmma3Q7D8pPZ7CndZUUsqcaHcg1y3n6ik6cdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=P28LJQwM7Nd0JWYdi4xP9x3ZnD9VIdwUkRgF_bMBiWnAkV-WKh0rvxegpB1eGF5FqHg011O9WDFmEVff8FJxZKN6Jv-TU0SH0pUekYbOKASldEbHqH3nxn7Fb2UJAN0AOP9-yB3KC05p-ErxoBQb-RU8cITz2231eotI5IYlSTqhDOhMclT71KppSlHkvndw90uW71U4W3XPw0HXDEeVUYeExu_yUy0eUIzgXVi5xEEvJtuOt3JZnqcyPnJaFg2wShGyoQQEm5Aj0-mbwyKWSmPdcshm_SsIdHSE5NC_C2X5nGmN_PEBNZkfkG3mfw8XXLLccV4EwmxEH_I9dU95uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=P28LJQwM7Nd0JWYdi4xP9x3ZnD9VIdwUkRgF_bMBiWnAkV-WKh0rvxegpB1eGF5FqHg011O9WDFmEVff8FJxZKN6Jv-TU0SH0pUekYbOKASldEbHqH3nxn7Fb2UJAN0AOP9-yB3KC05p-ErxoBQb-RU8cITz2231eotI5IYlSTqhDOhMclT71KppSlHkvndw90uW71U4W3XPw0HXDEeVUYeExu_yUy0eUIzgXVi5xEEvJtuOt3JZnqcyPnJaFg2wShGyoQQEm5Aj0-mbwyKWSmPdcshm_SsIdHSE5NC_C2X5nGmN_PEBNZkfkG3mfw8XXLLccV4EwmxEH_I9dU95uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ik3ZhQ9zyZErkBUhZNvTe47EuPnBU4ZQ2qcdi7Z-pWLEPMNbH5HwTafec2EQb5NxvPAPZEurPjsa7U3JiyLpVNFL-lfHjMSAFO5Y2by5IlAQGlR7Xv7tcHKHPMCqoNuwJ-3Es7nn1HlfO6a0TYMdSVOVb3bOmypkf6JDuRxFxl2y-nMyIrqnrFzSlmeyGJxVyMFegar8WzBhPrYM-3_Km9Jql1Bkxc52yy28piAE3XaEq51GkgJfynsm69Zhbfjx0Nqx7fdhXCpZHmcYnplrbDt6kjm9YeszwgLFG8sHjxllIWpUh-wHqA25dR1__xB7KPAfYw6V6KqLh_kewkEcOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgd7rYb3RepSZIiixk1FrF4nXmMfi0sHLmd_0c2cK1VTCPbUSlM72XHnnBdiKAFmcVc9p-6aSDT40p3NtRlihezQhT0VzQ_YUbpou0ybjYhR-Il7X6ytcBhwzm_Yyg_lVEnqn5VQb2Def1hneef9zHH7148h-WR-SRcjCj-bOV_W1oDzQ31IGvf2vOXSreoCIjlGydU0HWzB_k3Dm3AlqeystA6YWRom2G51_qa8vnmlf1my4nB-BWE4XGuozMXV6HYTKUSBzq31Z5kSV969x9Or8tdvBXZtzB2VVdhJpQYLWI5JSEoGifWqxR3t4tWXUXAqjaSTYVZrzzHlrvAJuw.jpg" alt="photo" loading="lazy"/></div>
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
