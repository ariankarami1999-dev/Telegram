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
<img src="https://cdn4.telesco.pe/file/vYWFBSVUQR-9ocyZRl6YzwP3kWh2Ew5AklnCZlAfJn1fB0OVpbDyZ-2KKglFZ8xJ6Bul2Ua-grkpp6_MU9GD4MesW40q8Gl0ymgUGtqPx7HS0xJv-LvO7yC-_WRbtdi5me45eefXzOdlIqrmLeEbC_2Ddz6Cxe4_iA7WUWdSpOx1L7x2alnDyTDui2RjjgUYqgodBE-ESrz-UxoBPCOYwUDVfxKIQKxCyeRiUmrSMOZFTGyBE3dDIaYmkNCIv1jVyfFP5t0DfY3rJBX6E-lfRPwOXJN2UCGcxSrwI-tKKPptfQxng5XRKKA8Y7JnQ0X2yFy7jHSKf_SyjYnkBYX-FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 02:44:12</div>
<hr>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آمریکایی ها دارند با هیمارس و از کویت، شهرهای خوزستان را شخم می زنند!</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/SBoxxx/18635" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18634">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZLY7kw-SBu480GhvUXgEYecegrLP3T7B2f4s_JXmIWb1ZsHSSqyeoIUzAyIcwja5eQ9EJ24jW6YR8ia8ba6uQ2ur_KSWubS53tumnL4d21P1_pjZr7N5TGHe2rkx7px-3uNgFMRckQHJeXwfM2UqHJxV1JI2oe0sGG2kL8JX-jMHZWZeINx48kU3xp9eFz7ed8bIOpt4Vc5zoZQW1XtRRAlU90FfYYT2OZBDqdfIXhzcms6teurJ6EKKCUMSBZY9xmKPM7RZlc6N0J2iY9-YFYJ1CbR9BrCwtHSR1r1wsx4_2pCGA_ermyJp6HrF6vMiThL9ORvfA3qqNjqok6_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربها وقتی میفهمند دوباره ما برای آزادی قدس داریم خودشان را میزنیم!</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SBoxxx/18634" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18633">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:  با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/18633" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18632">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:
با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را به خرج دهید.
در صورتی که هرگونه سامانه یا سکوی پرتاب موشکی در نزدیکی مناطق مسکونی خود مشاهده کردید، لطفاً در اسرع وقت آن منطقه را ترک کنید. همچنین از پایگاه‌ها و تأسیسات نظامی آمریکا فاصله بگیرید و از نزدیک شدن یا عبور از اطراف آن‌ها خودداری کنید.
از تمامی شهروندان و ساکنان درخواست می‌شود این مناطق را فوراً تخلیه کرده و بدون هیچ‌گونه تأخیر به مکانی امن و با فاصله مناسب منتقل شوند تا جان و امنیت خود را حفظ کنند. ما پیش‌تر بارها و به‌طور صریح به حاکمان شما درباره خطرات ادامه این مسیر و به بازی گرفتن سرنوشت مردمشان هشدار داده بودیم.
با این حال، آنان تصمیم گرفتند به مسیر تبعیت کورکورانه ادامه دهند و تصمیماتی را اجرا کنند که نه بازتاب‌دهنده اراده مردمشان، بلکه تحمیل‌شده از خارج از مرزهایشان و در غیاب هرگونه حاکمیت واقعی است. بنابراین، مسئولیت کامل تمامی پیامدهایی که در نتیجه این مسیر به وجود خواهد آمد، بر عهده آنان خواهد بود.</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SBoxxx/18632" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18631">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سنتکام:
ساعت ۵ بعدازظهر به وقت شرقی امروز، نیروهای فرماندهی مرکزی ایالات متحده آغاز به انجام حملات بیشتری علیه ایران کردند تا توانایی آن‌ها برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که به صورت آزادانه از تنگه هرمز عبور می‌کنند را تضعیف کنند. فرمانده کل قوا دستور این حملات را برای پاسخگویی نیروهای ایرانی صادر کرده است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/18631" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18630">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/18630" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18629">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجاراتی متعدد در نزدیکی شهر سیریک در ایران شنیده شد: تلویزیون دولتی.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/18629" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18628">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=v_rIl1duUCarCzTmEpnvzTbSQh3R47Uw6KhPkbyk5_EwvmGtvcWfx5vdlHq0jEkm-UsN3k4UwkWWL2cr59qiCVchKCGwoiclrKRN1Yrznuhu6EF79fkqPRaxuOmo2bQSuGyLCE10nT2_n6vtgUYJ3kMUR-lXiFOOSQ7tdIACkorzoH3rky57QG5rrIUadHbOJKUf42eySc7-3QnukDPPhfLxbsyz8cJ4A2IRNoRq5nzTg730j-2SiIKopHDSNNj3XVN4Nf2Q31t45zdJXd6AkAHfcsusNEa5BeWbuIP_zHGC8d6wh6Y3825QK9Ckj0krBXMhrrv8IuDZxYxAvaHFZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=v_rIl1duUCarCzTmEpnvzTbSQh3R47Uw6KhPkbyk5_EwvmGtvcWfx5vdlHq0jEkm-UsN3k4UwkWWL2cr59qiCVchKCGwoiclrKRN1Yrznuhu6EF79fkqPRaxuOmo2bQSuGyLCE10nT2_n6vtgUYJ3kMUR-lXiFOOSQ7tdIACkorzoH3rky57QG5rrIUadHbOJKUf42eySc7-3QnukDPPhfLxbsyz8cJ4A2IRNoRq5nzTg730j-2SiIKopHDSNNj3XVN4Nf2Q31t45zdJXd6AkAHfcsusNEa5BeWbuIP_zHGC8d6wh6Y3825QK9Ckj0krBXMhrrv8IuDZxYxAvaHFZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/18628" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سنتکام:
🚫
ادعا: تبلیغات ایران امروز ادعا کرد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✅
واقعیت: هیچ گزارشی مبنی بر کشته یا مجروح شدن نظامیان آمریکایی در این منطقه وجود ندارد. تمام پرسنل در وضعیت سلامتی هستند.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/18627" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18626">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/18626" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18625">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این هم یکی دیگر!</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18625" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18624">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/18624" target="_blank">📅 23:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18623">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjynQgfM7gtbKzaAvql2oXFM1nID_R0fTVdHfjDxQ3oW8zUQ_Kyjx9qMqPFcxq08xx8LTpyKe27z5Q1ubGtUzFJNSBnnleZ2o582OJZAxQ1DBKu8GAC6QYdHnukZ1imw7Mb4vGif5CYQpAmFj1JKMKVBGEMVyz95dhQlCBo-tm3hfMJUtlpnuV7fV8G-tW5cWSTgbLuQ4o9LG8JNNeRbuphK1XWD4p4xUaqQ-B2Dkao-jG_9BqBv_OHbDF19a2ZehN6fuE9HWRvTDXh8jKQ5kpw9-h1AVQ6X3V0p2KRKiJtlCSNIPVikf9tGks7CQR2uVg9_kZdXUrxF4bv_JNZCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/18623" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18622">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGDZEXgkx6CFlLFm4lFDDJKSoRQmcBCT2f7owjkX2Iyhiyz8x_t9d07-R1GWWVBI8PAOlZZ6h2H32eUW1iGZtyIUWKE5Wb16CLGmHtqy96Q3rGPgzPjEfOyzvRmwsurL45taZkjguI5mm15QCNO1l4drKfDqgPfe4A5iIezl2BVoP0P_4AqEZJgrC2e7FeoBKnu1-QaUjVxpeyRakivrybipFvod-abRDt7B44n6tRGbNszgFk5B6eeQJXjJIRcmJS5kCuxRJfJcqD62lL7EdNOZSyjn0YQyasMNT-i2YNbP9ey0OSlBWIOtH9S9L3z2Y60l4DRy7fc6lYusG1LF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/18622" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18621">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منظورشان همین هفت هشت هواپیماست.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/18621" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18620">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF4v5m4rGAn3omi_fbMlyCdgV22F79IN12x7ip4dxLEFzsB-QYzP2vvgX3h-0LeQ58XBV_6rLeS6gfPfSGNGX6ZAH9Zxgu82xR4GmwJ1prcwlTuIBm3wEX36_wFFchX9OJGR79JFy6aOn8Dzx81G5F4a_VbckqeSFWoO848epzLr9HMn5BfzthvxPbbr3aj3b97X2l17n3Px53PHdGw0Rme27Ryyyljt2VlKsCyq_KgOzkh-NG2o2LgBJP-7NzDY0_8bpeYiyqVy5QtcWE2F7cEJrkOTzYAYJ1nFzIJanzjyxhEL4CuCop_tRirgTPy2i46PXrNXx5AP5FSagWoHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های ارتش جمهوری اسلامی ایران بر فراز حریم هوایی مناطق مرزی غرب کشور به پرواز درآمدند</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/18620" target="_blank">📅 23:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18619">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آسمان کشور در حال کلیر شدن...</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/18619" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18618">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خداوکیلی این چه زندگی است....</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/18618" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18617">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGQTwxoZezHBGM19v1kVSDmDhpSlC3YNn2cv_itdOxeioeJcG2UoCPLZQHEn7ajVOE8XLDFRdND_HxW32z5-Ze-rC45i9sis3jehF-o-YIdJIpk3lWYrcPy4L9cRlP3yFnNZhBHW0rWibm97Vkcl4RmqX8lHisOe91Xom1XFisJzMhgLXgPcKOCPNk7J-YCTHxfZNdyoAuUIU56ZNctiQMjLHXXg4QRRxxa7YCWs3LrXaa-QH00CJWRqae5SabV74RJPzMqyoj3qbueZlo7s0TcBTBZ-UGSsw3bGJERGGKQIiOUdUKGaPLBNAMhz46SkpAOVpWWwhVgWIlSwJr-D6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.  ارزیابی‌های فعلی حاکی از آن…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18617" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18616">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— هواپیماهای هشدار زودهنگام نظامی و سوخت‌رسانی هوایی ارتش آمریکا از پایگاه‌هایی در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده‌اند، در کنار فعالیت‌های مربوط به یک فروند P-8 Poseidon که از بحرین عملیات می‌کند.
ارزیابی‌های فعلی حاکی از آن است که احتمال حملات نظامی در دو تا سه ساعت آینده وجود دارد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18616" target="_blank">📅 22:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18615">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18615" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18614">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لازم به ذکر است که جناب خضریان عضو کانال ما هستند و پوزیشنهای سنگین Long روی نفت دارند</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18614" target="_blank">📅 21:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18613">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.
اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور در پرواز بازگشت به واشنگتن تغییر کند.
— یدیعوت آحارانوت |</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18613" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18612">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تکرار حرف مدیر Secret Box از سوی دکتر خضریان:  علی خضریان، عضو کمیسیون امنیت ملی مجلس:   مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند  آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18612" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18611">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینها هم رسماً بیکار هستند. خود ترامپ دیروز گفت از دید او آتش بس تمام شده و دیشب آمریکایی ها جنوب کشور را شبیه جنوب لبنان کردند آن وقت اینها می گویند این کار نقص بندهای 1 و 5 یادداشت تفاهم است!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18611" target="_blank">📅 21:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18610">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.  به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18610" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادامه پرتاب موشک از ایران</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18609" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyxiSN8R6dHV0UA0IpsiODgn508QEZF9-jd4-UsfS45oHI_QN5wTW9IvxjbycNUQKBnivLID77f8pKp_R4wix15X34X00oqewxEwi9goMfddtuRUCa8pxFTw6NFvBgxcrTxjfzVWJuV_Y97tzDE6ZM1NB8Q_6wE2dlhmb6enKa3sFyh-yiXcLWoXvahymz2_Oct4qtknOEu27iug4Khx6KX6JMY7Nak-zJhKVaH9ol8FLC2EXWTmLHfXzT7oP9h5XUBM_mAtfhB4R1TyUIMKCM54A1REzkoxgLcIzQsbcIBqyYOvNk2fzQ5RXFpp6VPlPIXVWmp5Zzl_QEGKYVBC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی این حرامزاده هم دیشب سقط شد
مردی که قطر‌ را به مرکز ترویج تروریسم اخوانی تبدیل کرد و از حامیان اصلی حماس و القاعده‌ در سوریه هم بود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18608" target="_blank">📅 19:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18607" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دود غلیظ پس از برخورد موشک های ایران به جایی در کویت</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18606" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18605" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/18604" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUTTGL7NPIkGZF2US2_o6PADqWcEG2eNmnBieRItoe6cBXpV4Nj_UgdrL0WJgBLfL75aD4huLO60sD7b2huh9EC4HJaPaUIGIBilz886IcWw0QIGYav9KUNNxFovPRnXRd-MWRDnA9CIG9kCbLvQEcTOSOeWYIgL_Lpg9dHMxLUDzCLO3Dn910Dm3wpK8ijCq1wPydjua0WhdHQvKgTuV9cSqB2PlG2gTV1Atpj8P6-ML8nTe_y2lc2QMGZXTMa0nBjoPsX2vCjCGEu77tAEn6u-blFBogndDZNtsGpEbU6iE0QoNEUhf-BUQieBY6DZ5jILqKyu7fIaDiXWoSHw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18603" target="_blank">📅 19:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18602" target="_blank">📅 19:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.
به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18601" target="_blank">📅 19:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.
همین</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18600" target="_blank">📅 19:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX3Sh8E7mpZ09poyQ5nQLD1mEGF6-KOCpatEUwYf7_20MmHJVTDp09PETDpzp4j3Wm-wfcBAwPB-CwykNYxqe3PoV5RurByR1TWGbYCvN18NNRTbyUijIsD05cUITpavF8QN5CBDTqoy2Ju45YclksodyY6fk4CymyTRqwu6oajayqBm-rcHBU8ETT4bN8iD3vCnMaM-2bfBRQzLiYhzpRJrdIoOKRHhMMOJ_tYlRixomy_sCNremJwYZOQ8sL6SRIJ0tA9faH_tgCnCENrqBxCXPahZBoy0KzDJd5_cgXalJVlnmVuCCbg1SDCd1-eWPPUDPmlTrpWZ4BctFDD3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18599" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18598" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ :  آنها (ایرانی ها) دیروز با توافقی موافقت کردند که از نظر ما کاملاً ایده‌ آل بود،دیگر هیچ برنامه هسته‌ ایی در کار نبود و از همه‌ چیز دست کشیدند  اما پس از آن، اتاق مذاکره را ترک کردند و کمتر از یک ساعت بعد، یک پهپاد به سمت یک کشتی شلیک کردند</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18597" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرنگار: تنگه هرمز باز است یا بسته؟  ترامپ: «تنگه هرمز باز است و من نمی‌خواهم در مورد آن صحبت کنم چون می‌خواهم به یاد لیندسی گراهام باشم.  قبل از تماس تلفنی به شما گفتم.»</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18596" target="_blank">📅 17:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18595" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18594">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18594" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwwIs2X682_b6D156Q-9RLiEfDT53GmwM0Nme79CQP7JyY_Zn9JYC_L2JhjnAC4RjHYUWbjiuFCkILhn3OaVwtrXSw2euRVWscCP0vM4PxCBjCZQYjO2aVOVIfyAHjMTgvYVt2JHlLT-rr6_captWyS33t7ikQQ_dU_vfaYOas_eYXvnkqj_1l8USTpUDXur6sAVrYCy1Vb8wADT_6lciemcgC3uKhPTW7YwZTZdVjA7lHjMpckdjz1YV33EpL0MzCpdyq7Iki8mS5owbUycf4aQI9AX69pCo7F7BV3_KPhnOD1-s8V5jp-VSNHdFLhIhviqQZ_dk_KSxlY2IWZwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18593" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان یک آبراه بین‌المللی باقی می‌ماند. نیروهای ایالات متحده مستقر و آماده هستند تا اطمینان حاصل کنند که این وضعیت حفظ شود.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18592" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">توانیر: کاهش ظرفیت شبکه برق به دلیل آسیب‌های گسترده‌ در جنگ
‌
مدیرعامل شرکت توانیر:
حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18591" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1Pk21mvQTpn3eF21QpXHmlZms7r0z8Fxvu953--9yTyqnrJZiXJleaf3SZVNsRhducv1lpQV8raHRox-tGppUzGkvd6k-9rnKQQT8jvXIobi1QEOnMRHCLruOwSoDVdv_HihoeTUSduCcK6Z1P700Wf_Ubf1razdXze7kuIFmGuaodFHClGYaqXYccOfkn9ljpF3zu8hcse8sp-cDF0S4wgN5AQBN6cWuWY03TqWKv1a28u0AwOCTPXlJ1qGfcr4WEOwEDQiln7qJBpWH_TA5WBtcDbGneDTPGHlyIF9lc-iuPas8Q_qmz_SzQ3ktnHMlWKLq_QGmDZrwF8P5blTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان:   ما از ایران درخواست می کنیم به ارزش های اخلاقی و فرهنگی که دو کشور را به هم وصل می کنند، احترام بگذارند</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18590" target="_blank">📅 16:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18589" target="_blank">📅 16:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18588" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18587" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تنها راه نابودی اسراییل این است که با آنها رابطه سیاسی برقرار کنیم و بعد عباس آقا را بگذاریم سفیر دایمی مان در اورشلیم !</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18586" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18585" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18584" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک شهروند هندی پس از حمله ایران به یک کشتی تجاری در نزدیکی سواحل عمان گم شده است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18583" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">من که قانع شدم.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18582" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عزت‌الله ضرغامی:   علت مرگ لیندسی گراهام دیدن تشییع جنازه میلیونی  امام خامنه‌ای بوده.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/18581" target="_blank">📅 15:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18580" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قول میدهم هر ۱۸ نفری که گم شده اند هندی بوده اند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18579" target="_blank">📅 15:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">طبق گزارش‌های دولت منطقه‌ای که به رسانه (SCMP) استناد شده است، دو خلبان نظامی چینی، از جمله یک فرمانده تاکتیکی ارشد، ماه گذشته در حین تمرین‌های پروازی خط مقدم کشته شدند.
پکن که به ندرت تلفات نظامی را به‌طور عمومی افشا می‌کند، علت مرگ این دو خلبان را اعلام نکرده است و هنوز مشخص نیست که آیا این دو خلبان در یک حادثه کشته شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18578" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=n7HOlXeVh67Ou-ICDj8QBPiiEgOBfgJOMb__Tf3ZHxmuahvOSjp61aq9YQR8O1VjFaXExZ77xYK-KYkspg2tqNCjDVoJKQ1NyosWn36fPad7Kz4YpDurr56c6ZkO2x9k4nKV5bg0csOX8IYjh1a2x0NM6Gig3jjAQLzLegcDNq0BqoRK-ADZAq7KHzVum4D0snkGH-Y2PhpVayHYJRiWTQQRypKG63rMJLEjnchu_zsa_gaonqOta3dn_WCX-3gDovOsLtvI6gu2LJngTmgAGirIKpoASmmWmzN7XcNK984gQvSUC_t5EWlN5tJ2I9eB2zdgje432rECcHDNi2nl8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=n7HOlXeVh67Ou-ICDj8QBPiiEgOBfgJOMb__Tf3ZHxmuahvOSjp61aq9YQR8O1VjFaXExZ77xYK-KYkspg2tqNCjDVoJKQ1NyosWn36fPad7Kz4YpDurr56c6ZkO2x9k4nKV5bg0csOX8IYjh1a2x0NM6Gig3jjAQLzLegcDNq0BqoRK-ADZAq7KHzVum4D0snkGH-Y2PhpVayHYJRiWTQQRypKG63rMJLEjnchu_zsa_gaonqOta3dn_WCX-3gDovOsLtvI6gu2LJngTmgAGirIKpoASmmWmzN7XcNK984gQvSUC_t5EWlN5tJ2I9eB2zdgje432rECcHDNi2nl8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر جام جهانی در ایران برگزار می شد!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/18577" target="_blank">📅 14:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOGG3l0cO0HaUgV8MN8-LE0M2BMQEKcw5P0S733Q0L76iMGhR8KBtruaOwoGMm4_gzX_37EdkLQwkIaQnpZtcGevD6U3EULKydU_cCDnN_k3BNZhuR1i0bXngEpUh3yn3co-7cKJKM3XBXTMXSANzLU52qyCrs4j58lt6dQ9F6Lxuwi07RJwVpCbMdgYUZhSiDrHLZVP99_dpKqPpxp-RS1FcfV88SWoALFfaTUCmszAY0eZhAWAGXrYHJ6q1J5KITXXDXF3qAezAKziffipJP3umuKINMXCVnGKt8NVZjv16ekUvNauPEDH5nlT9rf53f79kSTylyZLSA3DRCVkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18576" target="_blank">📅 13:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18575" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو ممکن است برای شرکت در مراسم خاکسپاری سناتور گراهام به ایالات متحده سفر کند، جایی که احتمال دارد با ترامپ دیدار کند.
منبع: i24</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18573" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.
مسمومیت با پولونیوم-۲۱۰
(در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب مغز استخوان، ریزش مو و در نهایت نارسایی چند اندام شود. این روند می‌تواند طولانی و بسیار رنج‌آور باشد.
مسمومیت با عوامل عصبی مانند نوویچوک
معمولاً بسیار سریع‌تر پیشرفت می‌کند. علائم می‌تواند شامل انقباض شدید عضلات، ترشحات فراوان، تنگی نفس، تشنج و اختلال هوشیاری باشد. بدون درمان فوری، وضعیت می‌تواند در مدت کوتاهی بحرانی شود. فرد لزوماً مدت طولانی هوشیار نمی‌ماند و ممکن است به سرعت دچار کاهش سطح هوشیاری شود.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18572" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پسکوف سخنگوی کاخ کرملین هشدار داد که در صورت تهدید موجودیت دولت روسیه، از سلاح‌های هسته‌ای استفاده خواهد شد.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/18571" target="_blank">📅 11:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات ایران به کشورهای جنوب خلیج فارس ادامه دارد.
امارات هم هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18570" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18569" target="_blank">📅 11:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080aef9062.mp4?token=fV8oPuxVLKjEQ06A9r-H3NDHdOCM5_Cv6tYdzrY02C36Sd2okiWk4kdlE53FLYF-869q0qHC1WDo4jfe3DnLc6BsbUBT92UVifap9BLUxnUf5h5LxA63xOJYg62STNQHy0RdRcQkqxZp9JuW0jsbVBhR9IR_7WdVDwLQQtInQCG3-PotnnlFgNobKzPo6Ty6-beC2jzXhnEangRSmDfhnuWLvMPbcXhPxg_FSsBNxcc5b5NuXku2gdwgRVCn3szMmKA6BfTNoWC7JXskQuXlvG0zh9VX0MAWX_ZpeGV78MeOLNyhGQofbC0nCXHo2Q1bWuzBB0kSucpTAD5XVxqiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080aef9062.mp4?token=fV8oPuxVLKjEQ06A9r-H3NDHdOCM5_Cv6tYdzrY02C36Sd2okiWk4kdlE53FLYF-869q0qHC1WDo4jfe3DnLc6BsbUBT92UVifap9BLUxnUf5h5LxA63xOJYg62STNQHy0RdRcQkqxZp9JuW0jsbVBhR9IR_7WdVDwLQQtInQCG3-PotnnlFgNobKzPo6Ty6-beC2jzXhnEangRSmDfhnuWLvMPbcXhPxg_FSsBNxcc5b5NuXku2gdwgRVCn3szMmKA6BfTNoWC7JXskQuXlvG0zh9VX0MAWX_ZpeGV78MeOLNyhGQofbC0nCXHo2Q1bWuzBB0kSucpTAD5XVxqiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18568" target="_blank">📅 11:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:
سناتور لیندزی گراهام، یکی از بزرگترین افراد و سناتورانی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود. به شدت دلتنگ لیندزی خواهیم شد!!! جزئیات و مراسم به دنبال خواهد آمد. بسیار غم‌انگیز! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18567" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایران بزرگترین حمله خود را از زمان آتش‌بس در سراسر خلیج فارس آغاز کرد و موشک‌های بالستیک و پهپادها را به سمت دارایی‌های نظامی ایالات متحده و تأسیسات لجستیکی شلیک کرد.
اهداف گزارش‌شده شامل پایگاه هوایی العودید (قطر)، پایگاه هوایی پرنس حسن (اردن)، ستاد ناوگان پنجم ایالات متحده (بحرین)، پایگاه هوایی الظفره (امارات متحده عربی)، سایت‌های نظامی ایالات متحده در کویت و مرکز لجستیک نیروی دریایی ایالات متحده در بندر دقم (عمان) بود که ادعاهای اضافی مبنی بر حمله به کشتی‌ها در تنگه هرمز نیز مطرح شده است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18566" target="_blank">📅 09:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لیندزی گراهام، سناتور جمهوریخواه آمریکا، درگذشت!</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/18565" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gejEE1_eU2jDeA1pPM3QrV4W9QInvqt0yQ6ZSs4swnH_NSV3VnAbk5UQ7arsgB-B9OoSA74IIiQsc398NsIJ0AmAQy23OKrtlv1lTvWINeRY4d_roqj2SpTijDYhi2LSE6zqyFGLaP73bL1YBrLrkiGNL2LEV4HMJTN72xQtLC_b2fi3uPLFb8bQbSMoYDENqo09g01PiCQJMG3ae5LQ4wtV8rCdb5shBvCeySivWIUnCAl3CQyczVn0tie6CaeC4Zs4IfVyXwoPGtWcIw2N9fxqJ-jQEY2CLi85MtXwJlq7hGnafQWn7__47LYm4VKeA_ytGcf2coyYIY4qh9wNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
شب خوش</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18564" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT6pLCM5o4b_C56xbAyyUTuQ90hkaIWZqiFO1lyZqRYVSYFhgRdjplAA3MsqvW8BniwMG1YcdqJP5ZUpujPR8VJux3i5xA2SCS-Xk5Sueyw-dyIZ55rKfewFSZ53MvcHRlx0nZjBBcKhef42kVQw8euvULbqIXUdp5FEVrvr3xF5d9omG_Ly2jL65VZm2ea2NhP8VPH1cB_N8gPIHzNF_gkn0qeNac7whSVBcJxH4BK69lt82-M0QJr1I3Pg2-xkOgjW4Cubl3hhHYjS7fzUI6SwsHNQWJkEw9GqPC8Aq-xCQoLp_mr8T_r82nyEMFGP6iwJI86Vz5y39hqCwK1DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدیم ما به اینها میگفتیم موشک ولی باز هر جور صلاح است</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18563" target="_blank">📅 04:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پرتاب راکت های هیمارس از خاک کویت و بحرین به سمت ایران</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18562" target="_blank">📅 04:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله سپاه به یک کشتی دیگر‌ در هرمز</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18561" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برنامه مان اینطوری است:
نیمه شب: کل کل خداداد و جمشید خیابانی
پاسی از نیمه شب: حمله اصحاب شمال به جنوب کشور خصوصا به دکل سیریک
صبح: گزارش اژدهای بندر از نظم ایرانی در تنگه هرمز
اندکی بعد از صبح: حمله موشکی پهپادی سپاه به اربیل و بحرین و کویت
اذان ظهر: پاره شدن گوش ملت در پاکدشت به دلیل امحای مهمات عمل نکرده
ظهر: مثبت بسته شدن بورص به امید نتیجه دادن اکل میت
بعد از ظهر: قطع برق
عصر: ترامپ از خواب بیدار شده و می‌گوید ۱۰۰۰ موشک میخواهد در ما بکند
سرشب:سفر عراقچی به عمان یا قطر یا پاکستان
وسط شب: توییت های محمدسامثینگ درباره مهندسی مالی بعد چهارم سقوط بازار بورس آمریکا
آخر شب: هالند!</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/18558" target="_blank">📅 03:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">باور کنید اگر انتقام را به دکل سیریک بسپاریم زودتر جواب می‌دهد.
یک تنه دارد انبارهای سلاح آمریکا را خالی می‌کند!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18557" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فوری | خبرگزاری فارس: دو انفجار در مناطق ساحلی سیریک، میناب و بندرعباس در جنوب ایران رخ داد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18556" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18555" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18554" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر جنگ آمریکا:
ایران انتخاب اشتباهی کرد و اکنون هزینه‌اش را می‌پردازد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18553" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کارشناس رسمی ارشد ایالات متحده:
از میان اهداف مورد اصابت، رادارهای نظارتی هوایی، تأسیسات ذخیره‌سازی موشک و پهپاد، سایت‌های پرتاب موشک و پهپاد، رادارهای نظارتی دریایی و پرتابگرهای موشک‌های سطح به هوا هستند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18552" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش‌ها حاکی است بحرین و کویت در حملات موشکی ایالات متحده علیه ایران دخیل هستند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18551" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18550" target="_blank">📅 03:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of Hormuz. A civilian crew member is missing and the vessel is unable to continue the journey due to an onboard fire and significant engineroom damage.
Iran was provided yet another opportunity to demonstrate adherence to the Memorandum of Understanding after being held accountable for earlier attacks on commercial vessels but has again failed.
In response, the United States is imposing a heavy cost by continuing to degrade Iran’s ability to attack civilian mariners and commercial ships freely transiting the strait. The strikes are being carried out at the direction of the Commander in Chief.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/18549" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فوری | مشاور سخنگوی وزارت امور خارجه ایران به الجزیره:
تأکید می‌کنیم که حملات اخیر آمریکا بدون پاسخ نخواهد ماند.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18548" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بندرعباس، بوشهر، عسلویه!</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/18547" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18546" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18545" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18544" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امیدوارم کار به خوردن گوشت ناحیه خاصی از الاغ زنده نرسد.
سبحان الله!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18543" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18542" target="_blank">📅 02:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18541" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
به ارتش اسرائیل توسط نخست‌وزیر و من دستور داده شده است که برای یک عملیات نظامی مستقل اسرائیلی علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18540" target="_blank">📅 02:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18539" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:  افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.  آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.  امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18538" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWUstnPLayOEc72XlklzvuX4qzmimskdUxKtFxGOAy2LZbe2y2wOcILNGmLeLOZRJNUHF0_3ssx_Mfm3ARtEGyPfUyRLEBvm-pkT_cSZy9q550Z50tPWZsil2boIs6SgqjSZwdNnMtGaNlDHqDci07gVLZ_yzvWFrNnwRTYoygXD9fLhef2nmQu0koLctyUUrv9AnfG7t_GKpeHWmk_a_BvGH1ZMfvalyiTo0ghIGvrKxPoKchDS-bcru3wkegxkKmhvHTE0MS8AEFQO_v5zFYBkEwEpm286j1lk61Fv1EwYyEaXu8dED9mY6SgYjoEkpT9f_oEc9dSCGC7_MIVe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.
آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.
امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار و کمونیستی، آمریکا را در بر بگیرد!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18537" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2vBjY6rbtPe5dxI4HOLvikD-ce-OLx9C3JDll5vdCFRpScCuNdabcaGvpz3QFSwhOJ02e7wIKefznbqOPJZGBg-QTSga_-mSPQAIaftrxpfPoCtp2KWy8mJQy0jOaaSi-wE_DXNTlpnPROqDPxt9G-AdMJ5gO011-04-XIKeu_lrvRHGgvad0tW0Kmi6y93fGsWm3D5_0f8OF9tEoYrdsCody2BRTfqCOQR-jqZc-5TSteGtTPAbx_M_3pYryCjC4feEG2bXc0vUG5ews5jy28ERw4bC-5xARU15ZcIj6zB_lB2-jeVLDTlT1aoB-4c8t45mL-YmN-USg5qPVCfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا من منیراً له لامنیراً له!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18536" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18535" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18534" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18533" target="_blank">📅 00:08 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
