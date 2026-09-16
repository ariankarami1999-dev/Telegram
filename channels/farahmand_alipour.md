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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
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
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGcTFHTDm5rs0PQm4WiNL5cWFg-0IUOmz5FUZ4-lTaBjlH21xlcjdOF3D2y6-r59f-9SMA7Iz9p1elb6UnSp6VZriqDOXAyThTHfFwIH6J_BrR9IPDec0A-FKkAIn6d8rw_Wp15PdOmnnHx_UbFPwBAuYq-ByIgr4Du6XW7aA-vbUCo_J1Y39bxM0XwZclqNI04kW75GSex1P1x3ct-GmUztW0xkOTS4EU0NnkF3jUTYu26MCXXehD_6M4eBEfbzaV1xi_JmuKPqj4Fx1ofDPCMFVi-mrgY-p3JbIwmsYVaBuNiznX4wTGxgDmnb1lhdWuNKcD0f0Nrm66q5Kw0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0hQcdAe-Er8Ch6T8Pi5fXDj0ReIZnLfzzJV3CmfdUD7C5cGwBClZf_ZWW6A0LwbIdlJEpqzcGY11WwwjM1ZJ9LhU8d8FTYLhaAb6nD3cuGThwU-wcpaHOSIDFIbWOSs0fP05Yj56rhBK6STrZKwOl0O5S45MxwmILdnLmxOEbETBtiE1nOlly2Xhi2JEs3M-7FT__DiKKxSgzPnewND2GXia22YYTQ0tJI5yvdy7eXMY4wb4FpMd6DmJsJTrJN5QXm50wT4VwTAuNz6aKw-cWT8bNs_Hm_N9w7H3-REguS4KtIvZstiGqLl93RUnqTP7fmq6j8BVLtlY_cZqW76Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX6mKjU6CBm9VoY03IWK6d_4syPbXAuJTKMW9yGfkl9zyqpnDitZutV-bzRrzLWyQdtaBaa4gCoVt8G7vByiCMvmDOXF4mEeV2_eAbr9jykANHV_8RFqyAP5IOICzxbrNUeuXTte_f4zRhChjB5jrPV92Ji1PVL5MkIygek-K42Rvs3CNZ_1yxUp3bPEeTgg5eTYqukrvYz98rHz-6LC6tajwx3HDo06XVaxMjg8WHu5twnzBTCG-ChtTdDg6aMuf-pu6gHaWkdLc541MxmRmtkoSY1GJs7-P5VMfQPCJF7PJ__B7DeqK5znMUyLz1Viut4W1JfrKi1Xo_lv-YpF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0EuEE9I_NYb5Wiwt4bw5eABv2-y_dSH4r62ajo1ByzhrfJcc7ZBTDhd6SgB3bLtQ_FfI492qW6Cl4wDKGThpUo9KcWV84cqzsdy40LPpejuRBtQ4kOWvHizBYKmPNowuvyfrE5ug7Cat60OXe-kgLJnMPnu8bmhudfMgFNppLgQcBxwyhaZdKzG5Ie1nag9Isirtbmf0_eRd99lmU1uQUpaW5lAYxb_RY3_YeKfEdOiigWMWrBxHGNUafdPHoAobkRITcMxifK5vKYSMyFfW5cgDZCyAWcd-G8B1tCApdXEt2yNCBBt544DM5oLtGrm1hWFADuBfBakLEuHYl3cUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCZUmRoP3hFL3LlRznp25nMjuQZfUnvtHFE2EIhu7uXs5bd82f0GysseEmUhXd3N-eBtfl7unInvctIADNhd4yWo1dTImqD_zdxYmC35FmDQteEWxAeojNgQxt1DtFMXIX6YKLuSEhKU2Z0vq7NLRpKThbaki3mrIGm2Z4zmauoukH41TqEja7gyV5ZQy9dAVQTEoPAo-FRTWzrj6lo5i0aiKzvSuZShmyUULfwsN7LZOAh_cd8-KpajzKyWlBRIT0dE5M87vs9I27JxfDtuG5nE0vM7xkp4Ev2_KEUymjixjW8LEvjahzHSlEHShbVfUgCh-R-Sna55kxk132pynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b__bqLa4Za7xoc3f8QC_JIfDblXVMDUTBHShfOjHQp71iFYI8WOvJfyzyzLhufFmcmC34ByW8c0PtTYBCVqtrMoT3QI_cPrOEK3XqmAT9XDMcyDMLWsnc63dM8JbBM3BUsHltKCdom62Q92WaQdyJMzsTMeQ4jnGoew5ERSI5qedjpOndDxo8E-10zxXFlUDVgbqGqNGJBNAQOI0M3SrS6JGmGR_IGWjHJXMinqn6GpH7wbZ32h67tb8rJmH3D-fyFi0YfSh4ycl4dBVFJQu5gSqaRIA_hSTx47WFYDND0IRAYnINyy-T3YNlGQGV3ph9aRliu1fskZMlv98My6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=HKdG2QR_ajB2N2dLF2RKLBZlSOu3YwXmFRURylNhCAGYvpCBEHYjr8GhX0XBi-zHc7UwocGDKRU4DU9NRehI4HeiuBEaEsg3dpJcGC6H_n9GWM8UAfvvsKVv5pCkth-koOdj1Q0tS4lRcq7KhNiJvNkUN3jaqWZtSjQAAoU3rlKhApZz46dM_T7lcuP3Y9bf2u1-P0QbhNjsnxCu8IF8SNYjV8Gr088quH4WT3ucctHSzedE22xyAhFuzeTmE7t0fFelpZJK4mf5gsqwIIz6PcvrxeSvPKqCY4kSmLwMO7FsQjw7LPjOZxRu0JL7VkuSofJ0NzvNx-eBYeXtV80seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=HKdG2QR_ajB2N2dLF2RKLBZlSOu3YwXmFRURylNhCAGYvpCBEHYjr8GhX0XBi-zHc7UwocGDKRU4DU9NRehI4HeiuBEaEsg3dpJcGC6H_n9GWM8UAfvvsKVv5pCkth-koOdj1Q0tS4lRcq7KhNiJvNkUN3jaqWZtSjQAAoU3rlKhApZz46dM_T7lcuP3Y9bf2u1-P0QbhNjsnxCu8IF8SNYjV8Gr088quH4WT3ucctHSzedE22xyAhFuzeTmE7t0fFelpZJK4mf5gsqwIIz6PcvrxeSvPKqCY4kSmLwMO7FsQjw7LPjOZxRu0JL7VkuSofJ0NzvNx-eBYeXtV80seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=cAmRXyFcApLfvp6h_ULKegs9bghm25OptcDaOd-kTpr9q8BwdJE3L8BQl-WxbNFT6JessQjP54GbwJHygOl2tN-k5BbuJRll6hXGhAYCuaMZtZGrwQVFlcSonDUoQyFNTkd5ovbnmw1bvki9_ekEgBhpUNHO-GStlnHVFnGjGNWAgHW1FYUHPeq_f3qoDgc0TrpLITSKIhqpr609TgPJQyTGDtNw93owrHz2Gg2fOs6cXA7yjfeqYASS4r_N-hugmNFaX_nxNPEUHmCemFf1RvdPY5d2S0isrxB03EVmL3Jrc-owo4D2SQDRLsJQ7M43EfYUYyFn6cJP0TybbvhMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=cAmRXyFcApLfvp6h_ULKegs9bghm25OptcDaOd-kTpr9q8BwdJE3L8BQl-WxbNFT6JessQjP54GbwJHygOl2tN-k5BbuJRll6hXGhAYCuaMZtZGrwQVFlcSonDUoQyFNTkd5ovbnmw1bvki9_ekEgBhpUNHO-GStlnHVFnGjGNWAgHW1FYUHPeq_f3qoDgc0TrpLITSKIhqpr609TgPJQyTGDtNw93owrHz2Gg2fOs6cXA7yjfeqYASS4r_N-hugmNFaX_nxNPEUHmCemFf1RvdPY5d2S0isrxB03EVmL3Jrc-owo4D2SQDRLsJQ7M43EfYUYyFn6cJP0TybbvhMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=A83yLug2Qzrota_erBpdDR9QWP9eMh3x6Xauk7W2q0DQSgVcW0Ol_uHrJXIs194mD8Iw7r4k63J6tEf-UxQ4Elo4n1YB7RX1N7NWQUyHLPWH_Xj1kwfU7BHqOlIvgm0p5cRZmrP7MdAyBvxr3jIuoOHVYZJNbvh2idxoibVxQgoy1TS7WvKpB4W-ikBWlgJNst8toh48ypo5_64V2gpXNWWgvnbJEJmtH5EyyHZTQ4K2QQFhnjVfoMhHvuM3AUzNuR99SdoVokjGDE5chpouVLkWhfswGDCTAaxM_PHc0QYbIp16uqhW2nTFZRUZHhFDs5_5WaBvBTslrHcnX0FZTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=A83yLug2Qzrota_erBpdDR9QWP9eMh3x6Xauk7W2q0DQSgVcW0Ol_uHrJXIs194mD8Iw7r4k63J6tEf-UxQ4Elo4n1YB7RX1N7NWQUyHLPWH_Xj1kwfU7BHqOlIvgm0p5cRZmrP7MdAyBvxr3jIuoOHVYZJNbvh2idxoibVxQgoy1TS7WvKpB4W-ikBWlgJNst8toh48ypo5_64V2gpXNWWgvnbJEJmtH5EyyHZTQ4K2QQFhnjVfoMhHvuM3AUzNuR99SdoVokjGDE5chpouVLkWhfswGDCTAaxM_PHc0QYbIp16uqhW2nTFZRUZHhFDs5_5WaBvBTslrHcnX0FZTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=mx6ukeObkntm3XF52maMN4UM6Dl98u8CWTzjz65omE8pMWluBKHV_hd51iTqOUEG4TKt2FtJKnQZizg6847hgPjUFE6WAtyJOVdq2RbtmG0K4ahKSQUiUB4Zu3jKj5wEKVA2K0CcDc97iBfDJ2Vu-zJm1x-d1timNaRkiIEolcMZHHOeEianLCdOD80YtEkqmXGF4nfIqO1D-1Enx43WLXQDFlYDrdDvMO7Ea4UBXEKgpghzKfXo6lsNJvEJKz2QQDlJA79HuE_3mczbMPZWFZXj-oK4_Liq36i5b4zJQ0ebMbHxLpR9KA6tO-UYwcEwcpazQO5GgLypkfXVpowKyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=mx6ukeObkntm3XF52maMN4UM6Dl98u8CWTzjz65omE8pMWluBKHV_hd51iTqOUEG4TKt2FtJKnQZizg6847hgPjUFE6WAtyJOVdq2RbtmG0K4ahKSQUiUB4Zu3jKj5wEKVA2K0CcDc97iBfDJ2Vu-zJm1x-d1timNaRkiIEolcMZHHOeEianLCdOD80YtEkqmXGF4nfIqO1D-1Enx43WLXQDFlYDrdDvMO7Ea4UBXEKgpghzKfXo6lsNJvEJKz2QQDlJA79HuE_3mczbMPZWFZXj-oK4_Liq36i5b4zJQ0ebMbHxLpR9KA6tO-UYwcEwcpazQO5GgLypkfXVpowKyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qytBALrNZJSUddrA44WLtI48SG6sGtZ8ktuEzTGMQ4HIn3u_7B336QeEtUrUUeyMb8VMCM1dsmbNIo__HqYT4cbLi_X8X1qBISuIDNKHzM7TnW1ngf_HADsQAgXEsxlNeT3PHT1iw5LOB1XD65giNFJ-hZxtl9cgkVI58taai81NdJ5TjQVDkfxJT3hh4ec_Q3ipUBK8C4A2kgUKT1RV89XD8PL3icbiM074MXG0ljGCt4vNadYtTlV1DrU4EIKj46Rr97cIpDyrnsFm4kXdI-tYpyr3Zk9LIMjR2-cKAbehW9dxucaTaHc2U8JxXMsa33ODCuLCNNxVGfF-b20Zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=FakXQMjoVFSoZ-sjzZYAN-YPRgEgV1UHrCTBSpRIsKSdzWeguM1gQfh3c4ncyqoF6JGr2GN5T-JMMV9Wn1EXoq4ovcpbYtOqEIGGs6PqBFqD9xVFCGHJeiLGAG8bakSJHJVYtNFcg3-tO3WtmDA6JNkBjYggW8YEI1wEygEkzEH6kuRGvlwKNtXKMJi0Bm_02vxxENXrSK5saiIhc3acb-AirHRCqqew3MkopwdxHXUVUGbVRK_52nW_JCzl9_oOW2ywxWgaCfqG04nWKuHfmG2pulnMbaSwCdU6PKobApHKSg59_Nn7VusqKtmuz4b5iIdWLUAgJLuT2uYU9BP2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=FakXQMjoVFSoZ-sjzZYAN-YPRgEgV1UHrCTBSpRIsKSdzWeguM1gQfh3c4ncyqoF6JGr2GN5T-JMMV9Wn1EXoq4ovcpbYtOqEIGGs6PqBFqD9xVFCGHJeiLGAG8bakSJHJVYtNFcg3-tO3WtmDA6JNkBjYggW8YEI1wEygEkzEH6kuRGvlwKNtXKMJi0Bm_02vxxENXrSK5saiIhc3acb-AirHRCqqew3MkopwdxHXUVUGbVRK_52nW_JCzl9_oOW2ywxWgaCfqG04nWKuHfmG2pulnMbaSwCdU6PKobApHKSg59_Nn7VusqKtmuz4b5iIdWLUAgJLuT2uYU9BP2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=R6asrjUh1a5ZlFoVwCl-wPbqpBVPdRGWmbZtOLUH-tsgB7M1IBVfcmwBwfbhRrJkIaWF7PlUVx-Ls4FDxMmxYvqgIwONWuGDMwypKgGRIYysTObis6IX4x6JfKWdoIG-SzKzndgJGMGBcIHlgLoUbl8Hdy4DSTPOPbC3E5F_YnQAk2bT7gy0pNBoJmCWjTAWX3EInnwajRHlcS_JM1K_O-FmC5ljteZ4bvJsNstbx_OGD1hyXgy5rnL60creGxeZUQdZds7vgNoBrakvyVNQwvTF5CjIhbxCDXAcPDdKW6J7uTuPnf-a9a_N_of5qCK_sC2K_WW1bbcvpUl9R0xxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=R6asrjUh1a5ZlFoVwCl-wPbqpBVPdRGWmbZtOLUH-tsgB7M1IBVfcmwBwfbhRrJkIaWF7PlUVx-Ls4FDxMmxYvqgIwONWuGDMwypKgGRIYysTObis6IX4x6JfKWdoIG-SzKzndgJGMGBcIHlgLoUbl8Hdy4DSTPOPbC3E5F_YnQAk2bT7gy0pNBoJmCWjTAWX3EInnwajRHlcS_JM1K_O-FmC5ljteZ4bvJsNstbx_OGD1hyXgy5rnL60creGxeZUQdZds7vgNoBrakvyVNQwvTF5CjIhbxCDXAcPDdKW6J7uTuPnf-a9a_N_of5qCK_sC2K_WW1bbcvpUl9R0xxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pThZ7Co7eFI4shourNj-uWuG7TTC7WbK_GfZcBx9CgfQcHNP3neiq8RddqdeqdzfaIOx5cuUNYfQmVb0pCo1mkqTUsG2MLxpoNYAMxJNwUQJe_7wn_8Uz9AjQ7wOT_VTJxqS6qXFmKzq8G1hYLw1U7KJ7A5PH8Af_Zb0F0UmlkllpQQoUYyLIcu19yszOzexBuemG9U1rILKCstjiT_tWAfdO7zoZtcGSbGojjwSdGQef0_d8SBJ4Aw0hNmo3K1C9yGDloNqOVhx5NVB7aFtMRB69Jpw97BPCZaMpB7ZdKdZh4TjLjhlbwSXwxVI7KuLzRTobPm4YaF4lOXPFQP4Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pThZ7Co7eFI4shourNj-uWuG7TTC7WbK_GfZcBx9CgfQcHNP3neiq8RddqdeqdzfaIOx5cuUNYfQmVb0pCo1mkqTUsG2MLxpoNYAMxJNwUQJe_7wn_8Uz9AjQ7wOT_VTJxqS6qXFmKzq8G1hYLw1U7KJ7A5PH8Af_Zb0F0UmlkllpQQoUYyLIcu19yszOzexBuemG9U1rILKCstjiT_tWAfdO7zoZtcGSbGojjwSdGQef0_d8SBJ4Aw0hNmo3K1C9yGDloNqOVhx5NVB7aFtMRB69Jpw97BPCZaMpB7ZdKdZh4TjLjhlbwSXwxVI7KuLzRTobPm4YaF4lOXPFQP4Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=kx_08eJoAxGXvrDlx_uGHLYeODHo2rK8G1_9EJU47bNlxH69DEqoFl7_JlGR0GVesUG8tts5TtcDknfS5cnAO3x-GtmqDZoQvhKEWh5I2L3xMryCWcXs4DRkcBBIGAggxNxUnYweGDDSSKTkDJulXDg3aannoq1KBe8C_2qwvQiL-XYDWxa_cwdlpWe8h_isQ6C-zTkowoq11E8btAcy2SKhr8H87qVMxxisujVeCFy-Rv5Te9iRXyrEHuikQDS6WiT19pPuwZ5PtdB0Usd6w39sNbaDFwU7k5LY7B91UoOWE742esCRj767-OXs_GwDjZtxHtyP5Uv_woEnlo-t7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=kx_08eJoAxGXvrDlx_uGHLYeODHo2rK8G1_9EJU47bNlxH69DEqoFl7_JlGR0GVesUG8tts5TtcDknfS5cnAO3x-GtmqDZoQvhKEWh5I2L3xMryCWcXs4DRkcBBIGAggxNxUnYweGDDSSKTkDJulXDg3aannoq1KBe8C_2qwvQiL-XYDWxa_cwdlpWe8h_isQ6C-zTkowoq11E8btAcy2SKhr8H87qVMxxisujVeCFy-Rv5Te9iRXyrEHuikQDS6WiT19pPuwZ5PtdB0Usd6w39sNbaDFwU7k5LY7B91UoOWE742esCRj767-OXs_GwDjZtxHtyP5Uv_woEnlo-t7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7bsVQZBLdf0sGeAy1nHfR1vOyTKq3KN4OOYdWH0mD422298BJWQqLElJcTZ6cc3ZNGYVl0dXrxEe1qMaL_gd5Zn_GnU48kSzK67h_ok6RPH0C6FXqFekPkh63OIlX2OIIpPoaQOmTUMeZdPGtDaUuEUXsjciASNvk-McnWnpfjp1oFEyRIyRbh0UDnmhWd6j0mLXws0xsEeDXQZ_nhKrx9bV7sJ7cG-G0v4baiUpO4FIbjDnmXsK5QYIPKfigPwaQL4V-4X3RsM1Qo9aDqO_6fmVH_0NZUmtmPURCtVpquf_8xNhug69XWdIJXFVSsKoq4et7G40Iw0hdUVQrqgAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FKecJVTT8aiu1w0sJYGr339zxB6ab_PYh-fWwBP-E73S8pXsMqouQWHVshRAA2LmUG8JXq9NGkI0kJkT4CWvosIJwra-8995Id9ybtiiHKYmdqjPcyakLhuoXEjx-7w2FSaVCSJcJizri9vk765rbaWysWMnkJgDZOM-VHkDSWCwpFUxE8aw4QQG2eqC-hBulR4JOYf1MfYxfCTNI_TWIqZy1iGlCHahxXunY4fKx_aRENbypVNHdY02KD-70V8iWpRsEBRSv5EJYi9RxtDJzEkPj1sijc1dHh0Br27WssBLSObX_P3D8wmZUY-Cj5UvrVWLf4ySJEt0QN-_6b1bPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FKecJVTT8aiu1w0sJYGr339zxB6ab_PYh-fWwBP-E73S8pXsMqouQWHVshRAA2LmUG8JXq9NGkI0kJkT4CWvosIJwra-8995Id9ybtiiHKYmdqjPcyakLhuoXEjx-7w2FSaVCSJcJizri9vk765rbaWysWMnkJgDZOM-VHkDSWCwpFUxE8aw4QQG2eqC-hBulR4JOYf1MfYxfCTNI_TWIqZy1iGlCHahxXunY4fKx_aRENbypVNHdY02KD-70V8iWpRsEBRSv5EJYi9RxtDJzEkPj1sijc1dHh0Br27WssBLSObX_P3D8wmZUY-Cj5UvrVWLf4ySJEt0QN-_6b1bPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CQ1VJiUF2tqj3-eLH-F9Skck8d_ckbuces5ew0ho4Zy81yZYpnlIfo7neZp6sndRVH4pao363ETV_luzs57mXUfcgCOkuzxNqFKFUBh9ouBCw_ikK4AHPeSMPndFgeJSjvqwnnWN7Kx2NGCwDeDiEnoukXci7ENlXmfkBWLpxa979K9l1yBaRToqkx8auA_cMdDMWCQ1bf5q6zuibhrv3KvSrkIX3lMRAGbJSN-_qh21jCDjPQX3Ua2lCCCpVTL5huDP6xZzbRuR9A1GR3K7wRrwOo6iCQ8tJA_2jRIt9O-x_UgbtHEDfXaCaLwCKol_7f97Nn_8RUrwt--xFdtVaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CQ1VJiUF2tqj3-eLH-F9Skck8d_ckbuces5ew0ho4Zy81yZYpnlIfo7neZp6sndRVH4pao363ETV_luzs57mXUfcgCOkuzxNqFKFUBh9ouBCw_ikK4AHPeSMPndFgeJSjvqwnnWN7Kx2NGCwDeDiEnoukXci7ENlXmfkBWLpxa979K9l1yBaRToqkx8auA_cMdDMWCQ1bf5q6zuibhrv3KvSrkIX3lMRAGbJSN-_qh21jCDjPQX3Ua2lCCCpVTL5huDP6xZzbRuR9A1GR3K7wRrwOo6iCQ8tJA_2jRIt9O-x_UgbtHEDfXaCaLwCKol_7f97Nn_8RUrwt--xFdtVaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwtGeDbKHRhmcXMJXAB0lNn_Ys83AjAPivPjDMIMhPJKErBxxRcAumO0_LgiNSGmKh3wsYozHyGQma1N3QYI-_oFRC_DyR4lyFETQllx40w2UJSc0N9bA32F-QXMT_2YzPCEYLXr3pMhYJlyCzArtOEWQgPxo-Dw9_fNNZzYqP3f6iqZg6HmftG96XIZAHVWAWMMJ69sjgjrAWtqTXY7ICzss_kyDE_BfGrfeeD4DumAF9UUBPSeJY47SXFPrVx4HkybWSLq4Pdojp26Z-jzI-hnF1UKRBlkir195TCEp7SvzdwW5vG3OQhu7KJZr4xuFEA772Gp1t5Qk_9_XDT5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pF--xAse3TkmdGC8a_u125TlkqaRGtfCc3Q8Ja_Xhmgmg9kTTfmxmmvTUKRXQFd5o8hskGKhVvtxF5zPbULUUfbSm0INLwGbAIkryyGoDQs1Nb-A3giVp2WBjC17L3LHTwPgGteJefyT2yS4VMyxnVEwvfaFuKpZ2GaIa7Y-J0fV3xKAZNFrWwPJzqvysLffIfonlNRbqmVFua1h82z28AAgwNt-Jhz_SSOKRjVPkonPRiMVRi7nOBkntMsP_fpscVR0CyuW75eni6-YuOYMJWN7v553rSs71KjTKK3XIEOfs9ACgNeaIRrhGM7VwrREtfLi4KD6GNyNyrjJDTDgrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=VtdlyF5n09s17Qlyh7ksYUdCa1IvbuAF1Xy1vFcnb6qIncSNqbgkw5-YSvHclXHGUgDgUzVGnNGWSawHLTgmIDlURjpde_uH1qWWIvZx2WwKDkTU-i9_azYgLuDbFw-MmYa5wZkcoOaRhTWM-pylWDe_i0yu8UZGuZy2rd51DWezYw3yGEeApMLEHna__O_SniJlLVTCgfRduG871jCrZDGWVqme5KBdZ0yxPSonXtSh6LlbP-F5qm3_NTFkmEkJCc-5Kh48rp6FYZ_TTkBNg6cbODgf9vkb9gjJdXuyaV26fkAswjiMKVmsL4-QSJt5EcbnFQHy_n2937pmRpL1vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=VtdlyF5n09s17Qlyh7ksYUdCa1IvbuAF1Xy1vFcnb6qIncSNqbgkw5-YSvHclXHGUgDgUzVGnNGWSawHLTgmIDlURjpde_uH1qWWIvZx2WwKDkTU-i9_azYgLuDbFw-MmYa5wZkcoOaRhTWM-pylWDe_i0yu8UZGuZy2rd51DWezYw3yGEeApMLEHna__O_SniJlLVTCgfRduG871jCrZDGWVqme5KBdZ0yxPSonXtSh6LlbP-F5qm3_NTFkmEkJCc-5Kh48rp6FYZ_TTkBNg6cbODgf9vkb9gjJdXuyaV26fkAswjiMKVmsL4-QSJt5EcbnFQHy_n2937pmRpL1vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReexHQELS44xeVdoDY781YEuEv49SM1n5k9WWVKK3lRRhHAVcaGgUhSyGY17w7Sh4X_UBMaw2jmKjlMovyhr_3RYmzbHm9TYHZnkqRWxwnApdvPDezz8b4S-wbul2krRD_BGRhMyD2pgIX1k3DLLRcFHvygVXroCkTcLrbdnh0apcSECpkcewkCtcfMyrEYN_TYiQMGI6dLCRc7jBKz2mp1HumS3AgAsUoU_kJBzekoAqAc52eyBjpBcWmfX-z6WTTjAMpcy8mEbUHYIHuMP1-wNEVgkZpwc4NJY_gI03wzuFEUM50Zxo6Ldx7-AsKW_Qyei847swHguYcPwRMswRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sONnLmIMdrD_LuDo1W4RNIbuprQ0oHLK8K310zRwfkk7--AlajRWMSoY69zuVB-Be_ma5A8IgCnxZbTLxSznMp4lPh-EpMPUGDF_vS_XcSpJoyt3eh9d7uQs5ugVSwwAp0zFvSZwoYRcRTIwvbCBxnX5Dt5VJu-6Ef4hzitSiYArwCbCUeq1WaUyO-PJUjm2gJC2rkCgg-81Dbqoqgtx0LVhUG8v1LEg4gxfj7QSJW7WuG9VredPgtyglBJBHnmkGdvzrorONIkndZkSIhNiL6IErTY1w_S_9zgahT-BS6_5_CB9S3g6APDJZuThoFPTFxq0x-XaaURZWT9vEuMVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtXTXEm0hLNotl2zPmVgG8gTCVSmKeQMS-wq74jDZpzFkCk4nJxjFBPWaQr5FAsu-WJxmTYP-MQnPpi318VZ2JRR80fgKtmGunMDJnvjxrdp6iEYpPkn_CYhLDcHrFy3lbgyZlN1qAO2fefMiDJH7LnWVn3GyldGnR3arfSTEK4WCi0jNiOvaRrRWx9VS_MkUIIshcNZO9KGughWZhY3OB1DNt6MurCL8-Y5IqORGMmLGb3YXqfd_oK7BVPn0fsTDNRxppGWVg08gmvVJRYav_rt_G6JENypPybPvho5LhCEBLUGFAZLtjWkSi1wGMNkQr-lkyLQyHR5lrEHJ6OzVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=g4l81k-e1v4T1Z4LIpxfAnt_6gVF2gyMjovO4a8hMPo9qpz0_wrHn7OBJdpFD6XCGYxgZvNtAQlbFWEqYIoHKApfeYGU6SonGXaPRk7G7un1rdisuf9rD75_fLDmqPp8eD6gsAAtm8F77Cz9ptJBbbGCoR3MfB6I_Gzrgny5K-WkcV66NXZl1zTUmBAVVTDjEbc49maN0TxvW1IySvqzpLe_zjnl3uT_P9ssLnlV8WYqeSnMugZukoLfM_o3pe_njHLCBzRzXK6MCZKNiXiJn4THhd36WYGA94LgNwYEvzj-eYj8l5eXJd3gDrLfddb2ahkeM5pX-rAuBrcJgNsn4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=g4l81k-e1v4T1Z4LIpxfAnt_6gVF2gyMjovO4a8hMPo9qpz0_wrHn7OBJdpFD6XCGYxgZvNtAQlbFWEqYIoHKApfeYGU6SonGXaPRk7G7un1rdisuf9rD75_fLDmqPp8eD6gsAAtm8F77Cz9ptJBbbGCoR3MfB6I_Gzrgny5K-WkcV66NXZl1zTUmBAVVTDjEbc49maN0TxvW1IySvqzpLe_zjnl3uT_P9ssLnlV8WYqeSnMugZukoLfM_o3pe_njHLCBzRzXK6MCZKNiXiJn4THhd36WYGA94LgNwYEvzj-eYj8l5eXJd3gDrLfddb2ahkeM5pX-rAuBrcJgNsn4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=c6KgdNL8spyB5JLdsEjfxYe__anV50se0HuUKGvQbG9reoL4CxO2NQqajLi-dA7n6neQVDfrEMp7gKpI6RRmFF6D2LUf47SFOoiDRzKRmUGNvmpErx7wYJrku1GT1-pkEjad-7J9rFBA3cMAaIjZQ2uVj7UPVBvnsQKKg68xVv3xNAd0twSS52J2k_6ARwhZtc6lBH-r30RTH-pmCCM5zOnbKPZnJcIwNO94k2X6WUnIrsiIPn-I7P_2hGyauM0NbvfZ1mwL9JxEiIkcmt4TE0leBrNR-tw6M9HlTLGKE4-g1JLaLh8Q3S_tumt_G82Y7NYfzlz4BcSdOIFQYItA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=c6KgdNL8spyB5JLdsEjfxYe__anV50se0HuUKGvQbG9reoL4CxO2NQqajLi-dA7n6neQVDfrEMp7gKpI6RRmFF6D2LUf47SFOoiDRzKRmUGNvmpErx7wYJrku1GT1-pkEjad-7J9rFBA3cMAaIjZQ2uVj7UPVBvnsQKKg68xVv3xNAd0twSS52J2k_6ARwhZtc6lBH-r30RTH-pmCCM5zOnbKPZnJcIwNO94k2X6WUnIrsiIPn-I7P_2hGyauM0NbvfZ1mwL9JxEiIkcmt4TE0leBrNR-tw6M9HlTLGKE4-g1JLaLh8Q3S_tumt_G82Y7NYfzlz4BcSdOIFQYItA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hOUEcMZ2VvNaZ1Y98phCYKAIMS4kHfoh_tEYROzH-dFC4O_V9WGqlYslKBYz6S94GEiMDw65WDHoouA1dOF9EjOmj0L-Zxb_vrbqzS1auWeUJOf2Se3kl1M84SjcK2IVzmTLemrr_JYP-2pdP89H-FksRQXjXiZCRJrYEhAej-2Lf8Kkwa-dlpq5hzc0FFKFqaZwiDgRCv8_oX4ej2-ZbPp6jxtlCNdWFDCepvqoS2LwZ1HkGkHZg8E-ntWHh0JdJ0nh_ftfEdaM9EKdES6pkpKi1Qhya6wBuba7HlRxd3JBRrp0unAeaGy89bYwL_wBikCn6m8qtJAr4ydt_UYUTTG6efxDf79Hp83NQMy1qYYjsm72zs4kiJ7l1gdoY2GuYGYX2Veudg9DFyNt6xdJi46D8GEE_4UInJiFqy9W7LGk03Ml3smfD33K_Sey672g856DNjaPK5xQ39T-QLzkOKvXQy2_shy-HEpWC0bWkoBjUEdqyXTPSwoZdaUJjWYnvmPQXI544MhaaVCqyWh_WVXFIlDYFVMrz2BoWGj6AbnPOR6-HSL_JqKVTMt1bAcyBkOcQagq1GGign_Whjk4BiZmAFqX--nHNZy7a48fMS9B9DLyxxb9zi74Ty3VWJNeD97XISghleWzZldxDPWEcBIURicOKTOaeIXtAnWDsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hOUEcMZ2VvNaZ1Y98phCYKAIMS4kHfoh_tEYROzH-dFC4O_V9WGqlYslKBYz6S94GEiMDw65WDHoouA1dOF9EjOmj0L-Zxb_vrbqzS1auWeUJOf2Se3kl1M84SjcK2IVzmTLemrr_JYP-2pdP89H-FksRQXjXiZCRJrYEhAej-2Lf8Kkwa-dlpq5hzc0FFKFqaZwiDgRCv8_oX4ej2-ZbPp6jxtlCNdWFDCepvqoS2LwZ1HkGkHZg8E-ntWHh0JdJ0nh_ftfEdaM9EKdES6pkpKi1Qhya6wBuba7HlRxd3JBRrp0unAeaGy89bYwL_wBikCn6m8qtJAr4ydt_UYUTTG6efxDf79Hp83NQMy1qYYjsm72zs4kiJ7l1gdoY2GuYGYX2Veudg9DFyNt6xdJi46D8GEE_4UInJiFqy9W7LGk03Ml3smfD33K_Sey672g856DNjaPK5xQ39T-QLzkOKvXQy2_shy-HEpWC0bWkoBjUEdqyXTPSwoZdaUJjWYnvmPQXI544MhaaVCqyWh_WVXFIlDYFVMrz2BoWGj6AbnPOR6-HSL_JqKVTMt1bAcyBkOcQagq1GGign_Whjk4BiZmAFqX--nHNZy7a48fMS9B9DLyxxb9zi74Ty3VWJNeD97XISghleWzZldxDPWEcBIURicOKTOaeIXtAnWDsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=I2lX7WvNhGG5BPcKVqMyNUhRXeBYcgYycCprrL3BoqyuJ2b-2TNLjGKM1zQH6ye2zjI8316KUIfoDZa4cRNseKpZgTSSZC-95X80KXndyLGSzdip_40IdMb-gtN3e3Bj6jirOd1UQD9yqTCxEKek6vunE1yjszWq6qZx1ltuOm4MGztvoX0WxO1l_uqHaSNsrJ9A4RSXWp0nuZV3Ua5e4T2w5Rw_-HS8bfupxN1cLthlbGLsBN-Ufx8UAtFnPXLdcs_mOodSCbOzJ6OT4C0dImZ8uvr5IsDHLtcvOiyoiXHpB8lx8DftJqiqCR4CxrzDasqjScZn_ZKBuwEj1J4P0mB-qk0hZByK7yU9mQXipF4Sm_xQ7x9DDuqUVAS-bMewAdy37kJCSh4mrpuNHMHp4KcAkNsxQy9ePMtolthdtHWUdrJf8LTA-zDYmUEj02rU4FKEO2VQbMuaA9N5MUMxG-T9qGZDhzjojejJZxTTLF9v-W6i0Eg69ZD-BnI1hKgjKwOkAQl5NhEsIgYq6UNRXvGnXu8dwdS0GUXKn6aKeUzx8LizCmQP7P04pmrhsa99zI6XYXNnTnbS2FB8SNOPKQ5VvevImD9JKVxQNZX11BR5bqCOtn8bQGlHo7t6z-rBmOAOUO5X_0aWQoX1iD2bz4eL4Em35GvbCxUgyTJfJ4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=I2lX7WvNhGG5BPcKVqMyNUhRXeBYcgYycCprrL3BoqyuJ2b-2TNLjGKM1zQH6ye2zjI8316KUIfoDZa4cRNseKpZgTSSZC-95X80KXndyLGSzdip_40IdMb-gtN3e3Bj6jirOd1UQD9yqTCxEKek6vunE1yjszWq6qZx1ltuOm4MGztvoX0WxO1l_uqHaSNsrJ9A4RSXWp0nuZV3Ua5e4T2w5Rw_-HS8bfupxN1cLthlbGLsBN-Ufx8UAtFnPXLdcs_mOodSCbOzJ6OT4C0dImZ8uvr5IsDHLtcvOiyoiXHpB8lx8DftJqiqCR4CxrzDasqjScZn_ZKBuwEj1J4P0mB-qk0hZByK7yU9mQXipF4Sm_xQ7x9DDuqUVAS-bMewAdy37kJCSh4mrpuNHMHp4KcAkNsxQy9ePMtolthdtHWUdrJf8LTA-zDYmUEj02rU4FKEO2VQbMuaA9N5MUMxG-T9qGZDhzjojejJZxTTLF9v-W6i0Eg69ZD-BnI1hKgjKwOkAQl5NhEsIgYq6UNRXvGnXu8dwdS0GUXKn6aKeUzx8LizCmQP7P04pmrhsa99zI6XYXNnTnbS2FB8SNOPKQ5VvevImD9JKVxQNZX11BR5bqCOtn8bQGlHo7t6z-rBmOAOUO5X_0aWQoX1iD2bz4eL4Em35GvbCxUgyTJfJ4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=f0Ov2PDCc-NnTx6PvUHI9ijZ2fXk6pkC0MoHhEnVIZZF7UjbC4L8sfVETc2zMRQUDW11ikyi8wZHGdDQP5XvJm8W7q0lPse0A-fj__P9ORH5eSP8X5Xf7Sp8n8TgzPGF6JxlHGDuh2-KzPmomYlhdAas057PELiKGyVwMDFeiCSbaPt5j8XO1Ar0wn9L4lZqjdxAIsb1_2clDdziU4TcFnPC1mlqcCGY7etiNskU7a1YcQaFytrA6GNInjV4VqT0L56lame0_s-pKCKRg3WFc8XoZ4e5x3KgmCx7170tA-_6_f78NcSbzTGgTEUw_GdQKu1Fmaw5EjCPqz7y1K48Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=f0Ov2PDCc-NnTx6PvUHI9ijZ2fXk6pkC0MoHhEnVIZZF7UjbC4L8sfVETc2zMRQUDW11ikyi8wZHGdDQP5XvJm8W7q0lPse0A-fj__P9ORH5eSP8X5Xf7Sp8n8TgzPGF6JxlHGDuh2-KzPmomYlhdAas057PELiKGyVwMDFeiCSbaPt5j8XO1Ar0wn9L4lZqjdxAIsb1_2clDdziU4TcFnPC1mlqcCGY7etiNskU7a1YcQaFytrA6GNInjV4VqT0L56lame0_s-pKCKRg3WFc8XoZ4e5x3KgmCx7170tA-_6_f78NcSbzTGgTEUw_GdQKu1Fmaw5EjCPqz7y1K48Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTyz2LdSldyBvycAbPpG_YHh6jNchlikV_u_F5SpbT7A3_cmmx4gFL07n7zsfPXM-w0S9uO6z5UHRXkkioMHkTEYeUZXVO1SMm4xtCoRoYKbPTKe7M9-Zvq1DrxYWVTGq8iplumsJRu6Z8bq_sbcQ0bXZdTjWxovVIx6kM18yLE9NAb7NRgLn4KIvTK-6dFzFgIAjBpiD6-bNMzYoe0ZGJL9-3qH5ek1kNhd-huzsR_8b22wWtalgiRlLJFrgk9wkj8Tuqct6KdPXv20M77KiqG1urnGz-EM6-TDvC3V3n7yAb0as0fAcGpVo7Cv9fYH7vcXJQRaKD1H8nPy-VduUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=BIjVBmZ0PwjM1OIPWRt95_x1gnvaKEJLCRVWFHcN5AksDYufsIBar4P825ikzmEIiReIFBI08izaGNK5udlp5z1eM8_XEeQKz5Qz1MtzVxcN2RFdGkQHl4IVKStE5GTwNUGri4jmIOVC72H6z4taBgd1GYAzHR6HKGyC3VsDnN3qoh8I5cpXQJozcnxKRpID33FurKMwlWW-E0BRaVPFB33VLxzb5qTDkyOlulmz2NqbFhWYouaUrtwyk9i9Fe3zKhb1yFKEXRI-y0p9X-7ddBxH41VwyV9_AZu39zGlbkoELtVeGV81kubUVOUj7bDErJrPp64AWqcrxIySJmAEug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=BIjVBmZ0PwjM1OIPWRt95_x1gnvaKEJLCRVWFHcN5AksDYufsIBar4P825ikzmEIiReIFBI08izaGNK5udlp5z1eM8_XEeQKz5Qz1MtzVxcN2RFdGkQHl4IVKStE5GTwNUGri4jmIOVC72H6z4taBgd1GYAzHR6HKGyC3VsDnN3qoh8I5cpXQJozcnxKRpID33FurKMwlWW-E0BRaVPFB33VLxzb5qTDkyOlulmz2NqbFhWYouaUrtwyk9i9Fe3zKhb1yFKEXRI-y0p9X-7ddBxH41VwyV9_AZu39zGlbkoELtVeGV81kubUVOUj7bDErJrPp64AWqcrxIySJmAEug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ShcOvQxH0EDqMwqn79vsKJ9FodOOCK9NC8P3hFrmslp2wfwHooa7-Vof1UwZmmWgyIs6KnTiCT8DkfhP9vPViQA2NNv7RyW15_StyIQ3r5E5VwnaURqzRmLrw54PjVRCk1J8TLtNwuolG5Y7sgi1Ilnyw4nJMxBoqZQqVGiXQHIRt2DM6TurR0BHE_pUuQoDEs4UmQjqcZuySKCaN863viUpt-McrAhYmxK5bo88ePz26GABB67uRDl6MSUuaOUpn4RIDzDkfvoUl7MjyNmiZkFOfG7GYNc_QWDQ_isB1uB_7YQAfOjc19ytSvA_0JKLsgAJYMg1zYsyvtT2vEWn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ShcOvQxH0EDqMwqn79vsKJ9FodOOCK9NC8P3hFrmslp2wfwHooa7-Vof1UwZmmWgyIs6KnTiCT8DkfhP9vPViQA2NNv7RyW15_StyIQ3r5E5VwnaURqzRmLrw54PjVRCk1J8TLtNwuolG5Y7sgi1Ilnyw4nJMxBoqZQqVGiXQHIRt2DM6TurR0BHE_pUuQoDEs4UmQjqcZuySKCaN863viUpt-McrAhYmxK5bo88ePz26GABB67uRDl6MSUuaOUpn4RIDzDkfvoUl7MjyNmiZkFOfG7GYNc_QWDQ_isB1uB_7YQAfOjc19ytSvA_0JKLsgAJYMg1zYsyvtT2vEWn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM5vZ5KxeQlljugVJaSbk2OXKmAJXUHDAcZuCUasyq4noOLWikfoUaa3_chjUZb6EBPAbEs2QDHL-LEmMu3Sg4gptYot2mccsViBWjViS-ETGGNmJ1wTQm2BGpJNCq2YR37S_1c_AD_dpdQ33LXSYqZIzFJ3Ay-gBPFyKpxUCObT2ByJc7c5A4SlGrCb8YZf3v6C0CQJlO3LcqDnqNPJ3JGgEbGU3_zNRUi8GrOkj8YQSvu64RroFN5ZCdHwcmt-816_kWqb1Kxg-3tYkOhLVfDVoJT1RSzvZr9BoeUGvLaFLbjTtgO1P4B2f_78RBZ6j5HvNbDy-9CiniQo1bhe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbvb20XbH785eoCLYA5RtZomY29SnieZCs7Gh0URHxHEr_Zmw2Ge-ELP91boHx-g3Z4x_WzcZ4R5fKrOxdSm1pQSsVTPH85jYfn0abEWmT80d9O6c3I5d_JHdduLGo2JbC9sPmVqmKMQ7R6r8fzJcXyJq42ATcJgN0CjPV5cTREIxbqkSeHXYdzXide631ZugixrR8Fcnpfvv46OyWKOoYH5SslVYB9AcLSUZf8j4Xi_jn_6HOxBSGL3VCfH-RdEtdLfV9K_LCeJeXiPynCdImXT_GVu5PWpxyn8wL1vjUcFt8TVYt1kRh-4wNgZlMrRt-1MXyQjWta1WqBHkYBO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKm7fMxuh0jM4sSasPMzS6u5zLTpgAK3jz-EkU9SBlTaR5IjbdBx-QkhmBUxfq25kSoBstrbB9GewmHLzXvlFnZg-nPgBozQ0iJtySTOUxrxJadylpWGHHVjtqZbvNUo83XmR8KQdTL75PKq8rl3f3PXXdoPScWSnR7hU-PTIaXhryW9yWG6FGpvQGsq52gDHmJkjoY9mRLwX6FcQ5jopK-zfWjLE84Imr986U8NgtHSDt8UQs-Emd5PH6vOLlgy-OUYnkEAeryHfQ8fwbalJNH0c9KpGa0w6iHBS69_JD2WeHmD8msidgT6dLutotAgIYu4SXIu86GhpR4TjoISng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u67grEdRa2-irEk55iADrsS0iTIumBR7YPP0eZKknL3UHWiV5aCyxH3wYO1OFuABuYyqlx8r5rWDNmi_K987uzFmBEjEXnXW6cl8jHEss88OmDWBXe7WA0ZG_211eun4KARiaa8voAy5Sf_HIxbMqfgsjXsbVv6Tv5aLp1rGhMqODy_X9Z01BhA04SDcCYGn0B0rRQgCqkH7lcjWBpYB32ocsGG4lkxzhurvszJeIZ1FgbV3zeib8nnZ09yszhinj5Ro0ap8lAxxACf9Q3ZIMDhEVWy5Ik20RtyOLnKktK79_6Eb4p95PhSwZV1qBF9RD5Td9Zh8VljxiVQnqAzS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIhaEopyDPkjFRhyQQUz1ZuQCNt3Fs0rLqOEU60T-XT5T-kGuqBcbV-6VjMczugFxTDSm3We7EJByupvOkEVDM21dYoEKyPvStpZXtgYXyKkeOrXRDyGCe1AGITek2fz_Y7VQP3FAt293ZZs7b3VcKqhtXAd4OylcT9JKfKpmrQQT0nmTuJ2wxCwDXpdBwNWiRQLaqoeJWH5wwal2ZGcR9c9BLHncis5mj_oRp7ZYx6R7bqA0RDklrRqr3Bb4Cx9l3y2nWk_Bc_JThUBruibnHYL0yxGk8_nA8EqA2lJfOD8n8JLhovhAye9GK9mCxxavPgb2oAa_8mt47YDy7DlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huCVzs43CNcbF6B6AHzt5Roq6pAp3CLs3rJKKYgd-pDeaL4vG5PK7TTNEKLEoPTJ57IyRDS1KqnKr9B52pti8Z-d_Xp6hdSFePr66WaBqjp5n4CqzEFVK_6lmJwApq7FZu0dVG9ZcrDELKuoeQyT0IH5Yd1RuXkldfV-xCFDuvYIe8SMJPHQBSpb4-qNKJG8K_LSE-57RiEUtCc48Qck1-WDCRfoSexMcwRUQeDGxMA3QvhKbeASIGPgvx3RRK4QOyAaB_YFvNLcSR-I9w0Yb6EPpgVUr2cTIsvbwh4tfsMy8kYB595FCRP55UahbvNXtNR1I0FBDCqrZ_H7yXqDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM1jPqeSEJ7sCruG1D6JHZqlylMH5ikHNhxP_QIu14I4WaB7bYCMpkm4m0wOm-peQJO0d8W9Ck5ylQUPi1Kwi7miXIHg50_MXZFi4MewbF5C3IMsl7ibDUNendeauQ8yrTXkEMT41bc4MUgaAR9QMek9NHCA95mQBlQoVXTF_BmbU__gMHEpXz8FRdAwhrEOmcQyEZRQIF-iHnUq96erB9_KWJdRFJxAviYdiu9_EVGwZsYmfj7jwOKhfvcG5j581xvKvbB2e2LnpcBrSwUTP2KYtvH3iNOEJniMrApinbBbUnvGi9oxmTyXBWfgCuIxT2boP7k6wiIRxjUoWRBVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1cZuLYAKI4PBLQBB4Ctn6yq8OecELi4sX7LYXK2X6LaDmj7LjCb8P-cFzPfLCs9b-oVE9tImqwFHor3uk8_NCslIHfCQ17xUUh8Sh5V4-F2iHkwEoL9W9XR7bNsc8FDqGi5G3IzWg_dFrwtu4ooCKXnUATzlhgGn58fyoR8zPQfBKGEnuFZgPlWPWveU37Ox75U8WwbYngWJKSkv3QtguCV4ERXVMVkeFaOs259DarVmX9-CZn6KqmaKvTStRcAH0yL1ptM0WXLPryuK2kEn4N73wodJxIMP0V8DeLYQ7oR-rQGwSz5inxrTy7BEwur8n_6GXx_xurK2--4BHLRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7Ccv-6HZMTXPcUVdhpOjRyQCwQjJ9_1hv0XzEUqyYdgWnpcpwKFMP_ii0U8mRKNZgeMVAUI6GgM5O8sE97mJi0UP6soibmTfu13BixvqxdZpuhCSfuWKdHLyuyiKvoTWHvYZ-B8pYF7JQbaU75d1PmVDgOVEOFatmXcrZ6glo4TsELWmfhcswH482dKtj_V2m2saQOZetvG_QKodieJ91ONhvH00yfjFrUIgyRRcbrto0k0iQitSXLq8672bPOpnf9UYggjn2fbwTxn_LGNGOwrJGzCU3vkgn65FhwvgMiQjdV_DOR0sUjgGNxX5v4l3zBZ5QplKUam3GSCed-tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUKYF7Ra5-Yq7JJyXMXXnrwlQI-Q3GSGSYqa-XMSzJNmQGZPXpb3a9d1VGOU20LRrPVgbN0KX2lrpd2ki_5gfB91-QVd7AdmSCFU_BAAlICmsrj0jEbh_ZftMSVGr7Kvkd6bL7IrwJGW8CyEgSNVl281M6gci3-GnQUSf8srIcAdPHh8o1B_n1xoIqdXS2HBwuzaG7LHYXQdBTIRXqOzGeIN8kyShC8kqwAytruO10eKBrQTrAKsuikjmnNpPObUjFr57B2l7I7XjQWAfJO-1EipJby6j_EtAePlQCFIbJ8dPSjly55m-iq8aBp5GsFPRssbegFIR2R0-SRYECsXag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=npUWAvuxbmL7utsrckTHaoO4t0MBFuVlnq3BmdnFfOtoUkIVObA1sWyQWPnNt4izhR4ICea2s3pllBSOUmpfbCLkMvRpScl5n0R_AMXXIIf_bh1xzwW_U2ZuMkCa0jk4PulV3MWa4WcLuT310m7LrGJsgu8k73Tl7qbEqGZhsIsWrix70Ic64UNduBYlS2rVU9VRUUk_r4AhTZu671PhdFhUH7osP3J9PSR_YxbC5Mu5P4A9MpANxkW8MMcdh0P12_0bU9ZjmSw83qzOXcwkcQQ-FLPjgAIba7VrFvGMSkMYJn5NnDfK06iIMNUIKD6qPUYHwKbNcbDI0AEsEH5lcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=npUWAvuxbmL7utsrckTHaoO4t0MBFuVlnq3BmdnFfOtoUkIVObA1sWyQWPnNt4izhR4ICea2s3pllBSOUmpfbCLkMvRpScl5n0R_AMXXIIf_bh1xzwW_U2ZuMkCa0jk4PulV3MWa4WcLuT310m7LrGJsgu8k73Tl7qbEqGZhsIsWrix70Ic64UNduBYlS2rVU9VRUUk_r4AhTZu671PhdFhUH7osP3J9PSR_YxbC5Mu5P4A9MpANxkW8MMcdh0P12_0bU9ZjmSw83qzOXcwkcQQ-FLPjgAIba7VrFvGMSkMYJn5NnDfK06iIMNUIKD6qPUYHwKbNcbDI0AEsEH5lcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxEcZx9omXmovO57mNEaY5NMVI_i1xVZHkgoKpaXJWCwH9mqNAgREaQ1nYEPMRDh3nfIze9CwQAEmrK7Eux2MtGuc5r9mWqIfHrKDBgo-LCEH-tGoCgaN1QW93iVxNP0NGVF9feWHlHAZKUfVj-K3U-7Z322pZLSfN047LOjUIpfaH8-90unW8MRH0GFTgXjNqrcVRlxhSGGbWYut5SmkobSntrnDSfnS3Hyp5RMC41AKkAwyMUHA2CsaqGebP7q7JQjPO6jzckqKyDF-Y1p-gksXFv29VeBZRcBWwzdhkMf_RyRRvE0DSqysCZL7fhW66K5_TzLVdbBgZHh3eQl5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUe7X4LtSd7N-YhWdnrxlA64az8ZtEjHUfnv0ix8J-VPiokiF9fdhhFcAIx-RdPf5ttDInJzbdpaoKftHwah3ay-up38zZA87xoIdE0oWu6RML6-qU1z-rfOOdHAjo1Jcq_nFUbCor6boPu4eJ0a5XNKqJfCgAxs-ynheEESlPE5Ng2z4P_chXSxL7Gj0lusysNRTIenGmfJMho79oOM6Zvy0TLDVzd2gDlUgz7xogfh0eUNHPamyOppXq39Z2rqMM8PMXakIyDIM-pa-8Gwu322fH7ccpGJg6RZz5D4ObdEOEp9sTEHJj2BKzMnujQm7tOSHHvsA0N7fKGXtgUjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WiBLsgmPCj4v8sJ0qpx5sbzwz0SYCVmWO5INi65mbaS0p5la9AfBRT_3N3zEtMROedzBfwPmO1gkw6_hcVlVu9wM6vyP2NFjQqrmhs19pKyBf9lSfe0B7-FMx6O8Nu6ONZp75kxWnnJns4-41fM_IJ-UbnNhxNfCvlj1WoevBf4Xir_GU7q80cHxhHUqaWCwbyhowgsNpYhy51v0xc4muZXt_1SyBKUW7_QdlNwAgq66PHo1UXNaXqdrLiaOwOzbi-ws38gzn21pgqHa46pG6BxUrdI9ZayMQfdi_bM1WYH2sPaWm2_P2U5-4lR-lEMGnUWPR2OWwmNKwBB6Ee07EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WiBLsgmPCj4v8sJ0qpx5sbzwz0SYCVmWO5INi65mbaS0p5la9AfBRT_3N3zEtMROedzBfwPmO1gkw6_hcVlVu9wM6vyP2NFjQqrmhs19pKyBf9lSfe0B7-FMx6O8Nu6ONZp75kxWnnJns4-41fM_IJ-UbnNhxNfCvlj1WoevBf4Xir_GU7q80cHxhHUqaWCwbyhowgsNpYhy51v0xc4muZXt_1SyBKUW7_QdlNwAgq66PHo1UXNaXqdrLiaOwOzbi-ws38gzn21pgqHa46pG6BxUrdI9ZayMQfdi_bM1WYH2sPaWm2_P2U5-4lR-lEMGnUWPR2OWwmNKwBB6Ee07EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=tZx0vy3JC88WG8fzaXNp7NT8k22zdINepJxMaSgeAEGCXe_sgWMEVcEs1v8xCbPpbLWMt2DDP911puFzFui14yPfRJv8luRvh5r3ezt9kUv5nKenUP17EtSGcuJ8naCwZRvGlOvlfY0uakt-nyvSYwj5Xu9ZTyWTdecv5vO-jzUuWeh1tWrj-6OER9wIRuuM5wZ91r4gTWWCGGHAFpWU7cKHGPBtARQsI5mJX2zf16TXn0HJs1GtdIfvN9DnK-5HpdvhC3kOjYgiIN9eRuHRGxarVsT4sziL7SORcjYTx7LpyBjmtYQggA8n-Fw4IkBVpU0tkKDlNYo0zYU97P6t1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=tZx0vy3JC88WG8fzaXNp7NT8k22zdINepJxMaSgeAEGCXe_sgWMEVcEs1v8xCbPpbLWMt2DDP911puFzFui14yPfRJv8luRvh5r3ezt9kUv5nKenUP17EtSGcuJ8naCwZRvGlOvlfY0uakt-nyvSYwj5Xu9ZTyWTdecv5vO-jzUuWeh1tWrj-6OER9wIRuuM5wZ91r4gTWWCGGHAFpWU7cKHGPBtARQsI5mJX2zf16TXn0HJs1GtdIfvN9DnK-5HpdvhC3kOjYgiIN9eRuHRGxarVsT4sziL7SORcjYTx7LpyBjmtYQggA8n-Fw4IkBVpU0tkKDlNYo0zYU97P6t1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRK-lvcBdtrB3bo0VkZORQYClLyamMAmRh4GCoqmKEPi45qd1E1oqAS3yHxwoskn3hnNrzl4O0lBAVFDsLh9ku_Vy9KJ_BS8j1Qye2zkS-z61C1hwceCByM5OGnK9q4tlnWnqqGGtuYCAwDwyTkd4WIJGGiY_ax40mnmPa65RfNBuy5Ttw-Mr1CropJx-T0saGj7hm5e1AVJ-RSSkLdTxmuWe-bK3ltluINCdCrFYhqFnFJVWSZCiZ0VS768a-ZybOb95r2QxHJ7ppeQjC1qv7d5BUhnup1vaKGu7WoJ3kydl3P1ry94mearwr6Emfxf-JYjf6aj253IU6uM4p4Keg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdur9LBzRMTh9-GHQTZtyF91VV2GP-l7_Cqe6kwHrDJhlBH3BwSopx-CKxxZCVAd_z-HiLOch6P8WX4jyMX1hL5vBVnpTZBE3gzlWNLUmhcqJwn9t7TvpkcREXk6bmcWroGAUyBO3e4csZINsEV0UujJ6XSnuqB40Mn5jmgFLdq6aK4wZPpDxbiUmNzlpU7s9ktWyjfAX0cAAYfKyhiwKit5irqbpHqali6e1deMOakrbZAgtUZ5NDZ0_BCMcY8YxYMRa1QFOd-MMnte1Tqet4fMa3An3x9bKjcgmFHUUrxkcXJg479yUp3uJyscM2QR7zzr7zzCn_X-qO1jI8CKWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih10YDrrG1Lebixwm2FLJkd-GiRL6DS1wqtx6YeqR7Ep9qwORIKicOBdJ8sf76QQhmaYOalReK-I9j8UqHzo_aMv5hNuXRHC2613F973FsRMT45vIVe7paDVdNo-mS-KatlHn8pqOMpkO8HYBQHmGYvXiRxnNsDK2K4gu-88adBh4nKDD1vWzf3W8iwZQZp14P-9yLsQDRI8_0k2fd5JKszhxv9oLQaOfaAZWPt7nPvrGVSwhXDm-ioJNSyeDw409Xa7qlTaJZiHAfVg877U7To4-_lOP-VonkajrFXQn4opTfQUUzyj4_aJcrszzOHOHvslXiYS-QV-XizJG8R4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUYsviUQn0m8nnRkYsQ3FIl1RKTPdLO6p-DPemuDH1q970y6NhzSc-BnoMEj8dZxnydFrEBIKj1qitJmukh2e_WJxpHbQmTBF9iEMSC2bY0tVxP82sKZBM4asKacvYAkZI0K4msz9-0wcfXtrgzguU2oaZqRV-1pRo1BQXmxHGb36Aw5l8ipHMSVXHs-9m1KxYAynz75SuUF376xN9tVllbQUV-dK1v1rK1yBU7X1RQ9ihBUceKgEhhScTPsLjG-cGVw-wYKwDaMBA5XTu5l0l1gbLSGf4ITNTrHtwKX0N34qpeK2-5qXfXEQNllAKLhKPjmQn7wPXBAoQWBMBBdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzE-xiN3O3o854XQwN8w2QlwPLYr5raWRp3LloX49HntdYbZWpF5RRRt-HVwA0F-DBUyPSyRxH7gcJKqVsfIPiL-xOiSp3u-m3DHpNHUiSOTRCJdAXfZUcSmSvtD4t4Ngtb7gMsZ9PBYOmyni-7WVVrOf0KU9NN750DZRTw1JuXZb4CRCfWQTtdxaEI6_YcjSOu1SI6aHL3bQcBYjkaPZXaK4SSenO4wJ_XR2lQTRgMANn-6Gy4WrSNe-_z-R-pSv1_aXxiGWqm9Po49ZBtatyZQYRP-AbiuJ4s1D-FpyTsMVLylDseQTRzx8Ic6UwXfhZx8-VTwnPxar_TjaHBg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms3D9b6fjkJ3KcgYsNNhMwi6GItuqB0Giqi9huowfOIl-NsvJW4BdvdsgZt244nB7yEeQks6JYS9Qbd5ZLeJfz9lmf4k0s3m4xqZmTyDMlBbSL8dLMWbVS43exlTPv8l2sZk8AIatT6zmHE2C9t_zw8NnLmf0ZUtWN00s6dxv6x3IsCgHjvksIrySIy8CT74zes6xdwqeq-UInST0qZEflAEOYHXDEfPkuZrXAOyhTtdBzTwDhhnj7lnzPcCDAnmpMOcNVuvwXfMk1L2qwGHVKG2OzKVM6Z26aBFHv6vtz0p4_INv80qU_xi8C9Mvkien1qU5UtAMLUuWeVdn8vpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toZwXAqIMG19rowSreI6tyGGh3nNZBkSpfCP4QrGsM4P01_eao07ebO6qYvOR4O6IAiHqDFsE8s_AKJcAFpQUllvJ72Fw-EsKLe1YF9I2oaCP5ZeAzhWL2iv66J_WIn9GDlu-VwtMoPdzT66mbLfHgdu-vrKywlZrsyxJVGOyERg-xhAmpJzYzvyhAJIEdtPrbpr2ybyaTpZPLxbykm8L__YYfsqpl6HSVu0JsZroalgSwBrxjFmaUKL01KjQqBQWGGXlcAUGPDNLi2gEdcGXaKBpz_0iTQjaYZLk949kwL7Wc47IvIDYR8odC1SPwvU19zhgnM8EdH8NnRXEpnrhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sYGRTQ8-EUMgzHOuaCQIz9pqrEwB-RQNyZU6sG_R2M4fSbmgXN4hGENeVrhOhxKfTHCr7fUNv14WhO5gXmng-K56TW4D_hCYJWgKCelutFAXOHvEqrWR7kCvx5B_SHq05ujBeyvOlKcWSTxjAV8ryfWb3WBlDxbQgwwdMNjMtRt3TEwFG7VKCIOzUmCDphvMByC67d9CD6ArKmTKJV4bVJJKyQTQ0Svz_srhJcGJnlMWxH0lQONZfJ4uCK7ej5gQaHJeQDnkwgqcedaX2PhEPaR-dW6jQXSEBwHv1DoA-o1ugnqxwAiFJKvAjQeCc2jDDHZ1juSl9BzhUXHVJ4faOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sYGRTQ8-EUMgzHOuaCQIz9pqrEwB-RQNyZU6sG_R2M4fSbmgXN4hGENeVrhOhxKfTHCr7fUNv14WhO5gXmng-K56TW4D_hCYJWgKCelutFAXOHvEqrWR7kCvx5B_SHq05ujBeyvOlKcWSTxjAV8ryfWb3WBlDxbQgwwdMNjMtRt3TEwFG7VKCIOzUmCDphvMByC67d9CD6ArKmTKJV4bVJJKyQTQ0Svz_srhJcGJnlMWxH0lQONZfJ4uCK7ej5gQaHJeQDnkwgqcedaX2PhEPaR-dW6jQXSEBwHv1DoA-o1ugnqxwAiFJKvAjQeCc2jDDHZ1juSl9BzhUXHVJ4faOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLwdOGLhq3uSQ3rQ67xpIwByU9sHJte0xg5MBYyNBhY0OLLMdADY2deWIGsbx3I8GbWYqu0FX7Jt_Nxdx60Xh3JsJZtCJsjZs81S5xzMWYA3bNCvW38oCOsAhNA-Qzy5aBOOh3Ra5wpIryDFJj61IK9W5gl330I1_OgUTB97_L3kjK6iiMjWCtbxhjN3rnylHOebpBe1-F8NK4P2QU_9rrXyiSP0sF1yfQhbmKzC80sZyrQAGrzz6zrF97FX_nReeF2V8L90IMvnTZV-7VTAzrtGw-TcRpZHyVFv8iVNKCBcf4_HNtLvaE5COtsPMF5XgDJpcPNUJ3lE-Yw3kGOxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=GHYGIlaMzkEuu2nAHXeORZ3Cxs41qQx_GLAz6ut3sWlwRq2VCDSw-Czi_cEqzEqG6hcFfBfLhaUbyNfTvsbJAuc3zAOY11Dhz8wYf5TJBr9tHp-WboP0yvgQ54AztEt9eTh4f57nxLUUdksy3031LIUporQHYbYvjWF4vozP6F_vmjU40PW60Kms7n92_N3sU8BYmJP06-b407Mvr7HYESLPosJzSV0PvaG4WjPMAkx115cLye7mxXVAih-tl0I6Kx_qhAmuO0vD-f3ylZYK9geZs8yMmNDeESf73O23_jpoe2sRVD0JLOXEdMa5GY88ficYxwlo1hkDE5rQJdL6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=GHYGIlaMzkEuu2nAHXeORZ3Cxs41qQx_GLAz6ut3sWlwRq2VCDSw-Czi_cEqzEqG6hcFfBfLhaUbyNfTvsbJAuc3zAOY11Dhz8wYf5TJBr9tHp-WboP0yvgQ54AztEt9eTh4f57nxLUUdksy3031LIUporQHYbYvjWF4vozP6F_vmjU40PW60Kms7n92_N3sU8BYmJP06-b407Mvr7HYESLPosJzSV0PvaG4WjPMAkx115cLye7mxXVAih-tl0I6Kx_qhAmuO0vD-f3ylZYK9geZs8yMmNDeESf73O23_jpoe2sRVD0JLOXEdMa5GY88ficYxwlo1hkDE5rQJdL6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=gpdbXDCySVgiWYtWvHIRHLZxEMhXFfSTlQfN9hISrabH06ezaCr1ZneCluxrMJvBI5YOcOgPOim-smNVZQVhUPkiSRr6Y8qyxCrFKxKzAFSq1RE139DklI9MWFegoYAUTLNRa7epSdK5iSBD4OXUBmHeRjByO2yfCp_QGu40kuGQcztqFiku3bS03szYpqdIfxIt2Qo4nIvXtCx5x8BOV3VoPdc5_4mAMFZAIwVwFsAFQvekFldgjL0dkXOZBCr-VXCmFVSX2f_dEuqEiVoEy1Uv6Qhgxk17UXBcEINwsP-slQW5FYfWXKngsLZLi74tkR6jINy30gT8u9Lrkzb7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=gpdbXDCySVgiWYtWvHIRHLZxEMhXFfSTlQfN9hISrabH06ezaCr1ZneCluxrMJvBI5YOcOgPOim-smNVZQVhUPkiSRr6Y8qyxCrFKxKzAFSq1RE139DklI9MWFegoYAUTLNRa7epSdK5iSBD4OXUBmHeRjByO2yfCp_QGu40kuGQcztqFiku3bS03szYpqdIfxIt2Qo4nIvXtCx5x8BOV3VoPdc5_4mAMFZAIwVwFsAFQvekFldgjL0dkXOZBCr-VXCmFVSX2f_dEuqEiVoEy1Uv6Qhgxk17UXBcEINwsP-slQW5FYfWXKngsLZLi74tkR6jINy30gT8u9Lrkzb7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px_k77uwHuUpfp28s3cQZo-RpoKPwHDTc5iumH38Lk54PMrL5JD1lF30oeDRejmMyXDal87c0tUKiKzlhgfl2JJ9DDETPk5FkrXv9ep2w3pY_llpmvoE5R0OBzpDz1lYz1IMsH0Nu3csOR8SrAv2t4F653p2tQHMenh2fWdCAyxrRNAYZVSiH-J-i1FoXess1PMvzg1Q3aQgn0PxUoBin4OTIdou7TbauftzFdgiI1bu9_yWu0RynvLjmSsHp3tgytdYg8l9mQmEzWqRqCaCs5JeFKtwoQ-gGpzjUOD95kFNSpYhqqEElx_yK0r3oEddbH3hTnBx35eJsv95JQUFDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbB65fnjfPlJm47kGKmFXOwCSuuCzX0ik7OmTLvlpP36QLROchrERIEjU_3UFHqBdBboP1Hjte_aspqzYwPBV8_VXR4yErdeHgZJEIwGruuYZyLa4jwAevpei3y89k0XUrdlJlsnxJAIfcUVSiY4d-UJ2nykcPiwcRg_p2p-H_WDMpdNtGZqamYzKEcldFHRnYTnQqqawngCpFKKXCL9kO0WxmCAtjdXgEih6e_Ktzivxqh5dRjCgceEfPIiqo3Jmywq31LgYu485EKGXT9QOtK1jXP4rlGVRJj7z4YwuQdeyPNDZ8T-uZn5nIOuOWOiuNdt3a1I8S9MdDFEmcWUQQ.jpg" alt="photo" loading="lazy"/></div>
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
