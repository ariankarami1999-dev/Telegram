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
<img src="https://cdn4.telesco.pe/file/jRkPfbcXsVn1kKLK0ntU9OWXcBrumO-l33yy1J8_bCpTZIN5tcvSqGF5YJvVT3t1HKBg7Rf2cdu2UplGARy-gjd-RQdHbpOO27VcQcnbBdd1ol6ZdW_t1N5O1MdPmZySth7h2z0fM2vIhAzTOOUEy6K9L1Z5e6Q0zx932NAJZqPj_a7BCQV9taEwJBvBVeumE9Flb2E6woy6HCwaACTzebmeVZHII0ALqyRbJnpiNv4bnXohDvLOQKHe9TqrGOvfPrCPB3v5_1RZJJc__4x-FdCIOBoNapSEcdJ7lu8T_xh1ZoRJ1N4DoKY5jYswPsiferRUrIhJ60047RYsK3H9_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 21:39:48</div>
<hr>

<div class="tg-post" id="msg-139008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=gofSZ6Cd5aRJcOOXbugviHJcHYGPE31nM34ilcWrBp0DKj0Sn-mxfdR5mgoQORrNbBoM1EayAdnnwqpp1cjQuZlDaIvhiRXrdtVPuLxv1-GrAZ7WZM3PO97H0A0UqBaIFvthfbKNB_qMFqlKKuorUE8y45dSN5qM9j1338yvQdF7-lyFPBUHa_5zf5xlS8gL-J8vRz3Uuf9HBHlM0wSROL25U5TAZ0hisVZ9EKKWnI9OqlVTZDCRsbRabE5pn5VCt-7j6mUCLP-Eel-y9sXpTadXosftls4sR8U81_UzPJFreasFStRRBeNg7qzvNMDOwc8lf9lRfw3Nv_90UnA8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=gofSZ6Cd5aRJcOOXbugviHJcHYGPE31nM34ilcWrBp0DKj0Sn-mxfdR5mgoQORrNbBoM1EayAdnnwqpp1cjQuZlDaIvhiRXrdtVPuLxv1-GrAZ7WZM3PO97H0A0UqBaIFvthfbKNB_qMFqlKKuorUE8y45dSN5qM9j1338yvQdF7-lyFPBUHa_5zf5xlS8gL-J8vRz3Uuf9HBHlM0wSROL25U5TAZ0hisVZ9EKKWnI9OqlVTZDCRsbRabE5pn5VCt-7j6mUCLP-Eel-y9sXpTadXosftls4sR8U81_UzPJFreasFStRRBeNg7qzvNMDOwc8lf9lRfw3Nv_90UnA8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 395 · <a href="https://t.me/SorkhTimes/139008" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
اسپورت عراق: یحیی گل محمدی به شدت به جذب محمدرضا سلیمانی که 18 ماه بود بازی نکرده بود علاقه‌مند و تاکید داشت بود و الان این بازیکن به علت عملکرد به شدت ضعیف‌ای چه از خودش نشون داده سران دهوک عراق میخوان در لیست خروج بزارنش ولی باید تمام قراردادش رو پرداخت…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/139007" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=vbXTd88YOUmShu56idUyAvLb2ORUzfLbS0dMhWBIVuTeVc_jx_rsd68HOuwJ5jMRKFpZVVNch_e8UC20s0XfGPJGvBYK_-IA5xObSkw_ENfylzBx62DEKL95utM3MjJQgUoRuuSL8F-YZa4ojgjhNGisvmx-Czv5BgKmoB0D4P8CPZ6WUfJaCTvjMjTuXFBjKdlkjaapIEl6Twma5A9DDSwHmtW6zXBMDVJoCLOmWY2Hz7BxrB15FkAms7W58SljI8khOeE01-yQMERuwmCUlZR_aRlyzCoy7v40_l9MxLhN4ZlVG2yq_av6XhNITtAdmdQerqMlfmy2VHjYkLqkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=vbXTd88YOUmShu56idUyAvLb2ORUzfLbS0dMhWBIVuTeVc_jx_rsd68HOuwJ5jMRKFpZVVNch_e8UC20s0XfGPJGvBYK_-IA5xObSkw_ENfylzBx62DEKL95utM3MjJQgUoRuuSL8F-YZa4ojgjhNGisvmx-Czv5BgKmoB0D4P8CPZ6WUfJaCTvjMjTuXFBjKdlkjaapIEl6Twma5A9DDSwHmtW6zXBMDVJoCLOmWY2Hz7BxrB15FkAms7W58SljI8khOeE01-yQMERuwmCUlZR_aRlyzCoy7v40_l9MxLhN4ZlVG2yq_av6XhNITtAdmdQerqMlfmy2VHjYkLqkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
شهردار تهران: قصد داریم 3 ورزشگاه 40 تا 100 هزار نفری در تهران احداث کنیم که شامل همۀ ورزش‌ها باشد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/139006" target="_blank">📅 21:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/139005" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/139004" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود  ببین جیشده صدا چراغی هم در اومده چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/139003" target="_blank">📅 20:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaeid</strong></div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود
ببین جیشده صدا چراغی هم در اومده
چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/139000" target="_blank">📅 20:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/138999" target="_blank">📅 20:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب بروز مسائل حاشیه ای میشه، ایشون کلا توهم توطئه داره تو هر تیمی که بوده…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/138998" target="_blank">📅 20:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
فووووووووووووری از آنا
🚨
مدیران باشگاه پرسپولیس از جذب ابوذر صفرزاده انصراف دادند و خبر مذاکرات مجدد با این بازیکن رو رد کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/138997" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/138996" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
فوری و مهم
🗣
🗣
سازمان نظام وظیفه اعلام کرد قانون معافیت بازیکنان تا نیم‌فصل لغو شده است. بر اساس این تصمیم، علیرضا بیرانوند تنها تا ساعت ۲۴ امشب فرصت دارد قرارداد خود را فسخ کند؛ در غیر این صورت، او باید برای گذراندن دوران خدمت سربازی به تیم نیروی زمینی…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/138995" target="_blank">📅 20:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
تلاش بیرانوند برای تعویق سربازی تا بهمن
🔹
علیرضا بیرانوند در تلاش است با استناد به مهلت قانونی یک‌ساله پس از فارغ‌التحصیلی مقطع کارشناسی ارشد، خدمت سربازی خود را تا بهمن‌ماه ۱۴۰۵ به تعویق بیندازد تا بتواند تا زمان برگزاری جام ملت‌های آسیا ۲۰۲۷ در تیم تراکتور…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/138994" target="_blank">📅 20:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/138993" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/138992" target="_blank">📅 20:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVJDuDNohyjSiujCMPCltKHF3TtFYNCIjZJiDnuVP35xbHClG986g4b1OwVgTY2i1NfRZwQ-mk05P26w-oc9_Z1WB0ePHJ4zCsJb-PcUoI8niV3zZZJp0eU6s6fGXJMNGrbIBbhQEFzGpR6uAyvpzwjrDA1Z59c6bNzGdnlZRyQlXqhN1fcIF35VoDiwZnVWLHbJGRu_AQLF5MxRj6-XCAeiPtJ-q4V9_4XLxUPNt22QGY5zQOEU7QXDfqORYSNB34PRRo6oWluwUkBbB7DeDALXkDW0NxgVPMIZum2-iUgWCNLGrYemyhGb6IWyiXNJWSiMYLQveoMODKPNZ5UdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون و فنرباغچه؛ جدال برای یک‌قدم بزرگ
دوتیم، یک شب حساس و پر از هیجان
کدوم تیم امشب صعود خواهد کرد؟
[
لیون
⚽️
🆚
⚽️
فنرباغچه
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/138991" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/138990" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/138989" target="_blank">📅 16:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
✔️
جلسه مدیرعامل و سرمربی پرسپولیس برگزار شد
✔️
✔️
جلسه پیمان حدادی، مدیرعامل باشگاه پرسپولیس، با مهدی تارتار، سرمربی تیم، برگزار شد و در جریان آن آخرین شرایط تیم و همچنین برنامه‌های پیش‌رو مورد بحث و بررسی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/138988" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💢
💢
💢
طبق پیگیری ها، جلسه مدیران باشگاه پرسپولیس و مدیران باشگاه خیبر از دقایقی پیش آغاز شده است و تا ساعات دیگر احتمالا قرارداد صفرزاده با پرسپولیس امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/138987" target="_blank">📅 16:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/138986" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/138985" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/138984" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/138983" target="_blank">📅 16:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138982">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
کوپال ناظمی و موعود بنیادی فر دو گزینه اصلی برای قضاوت دربی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/138982" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138981">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه امروز از بین این ۳ گزینه، یکی سرخ‌پوش میشه!
🔴
ابوذر صفرزاده
🔴
ابوالفضل رزاق‌پور
🔴
امیر جعفری
⏳
باید دید کدوم اسم در نهایت پرسپولیسی میشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/138981" target="_blank">📅 15:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138979">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
پرسپولیس نا امید از جذب قربانی در تلاش است از بین رزاق‌پور، جعفری و صفرزاده یکی را جذب کند. فولاد پیشنهاد معاوضه رزاق‌پور با همایی‌فرد را مثل پیشنهاد معاوضه با بیفوما و ۸۰ میلیارد پول رد کرده. رحمتی مخالف جدایی جعفری است و خیبر خواهان معاوضه ابرقویی و…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/138979" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138978">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGu3AaLmixEkLuFvMmIn_0kXSBKxJ3ChR9tyHj8jCheJ-BqE11oCB05ICxJkxgB2BV9tjeuLerbO3Cwn36ri4JuSRSVJtaIaW-mxo28Ui46SctxXs_P_VUkZ-MH3RoACRaixEfTIbHIcy8HS1C80WkQ2mCGInhT4p8FaX9azv4kVjJpf0KXNl92DLU2KPGEK2-cGA_DiyXXycFSTET9S3ezjNZRk5xYKoVd-Th3sYd4bbzv9VN2D-J_9lObufTvp-G99Lwp1q92qYXOYFIdcMcDDdhzt2KTCUOoZPQMbTsZ8ARpxBzwbwuOtAsl8K1EoAA5CJiqBXnvsI51TVFbqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا برای امروز دیروز نیست برمیگرده به محرومیت عیسی ال کثیر در آسیا
✔️
✔️
پشت جوانان تیم باشید نذارید رسانه های وابسته به کیسه نابودشون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/138978" target="_blank">📅 13:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138977">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚪️
هادی چوپان: مجتبی خامنه‌ای پرچمدار دفاع از ایرانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/138977" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abzXT5XXBfd1YcOYImonSiEuUgqPk5pGYg2C1-N3FZ8OxU6KcxEwnSxko4M0MRhJjTKSijmhn4HP4IzJUhdhdd_BGDXO0ker-NdCNCuwBF0fdoiI1dXA9pW-UuKavIOcZ527VPtSLHsw2NGX9EBD_Z4h-cBDfpMXagrrEdY5h1vbdpn9NYnPez_NEDC3LN1cf-rJYe6x7qmjF5vmIuy-2KGdhbmYy_6swSHOIZMRJY5iOss7xd1Tt1aJSu5mWIr4ifE2vDSEwN_ousp3-H3peGf76RGps2Y1LxrEQUEqKmGw8QhKmSbMO6SkRbAq6jzlv8q-_3ZwU_Bsd0Fyb20kTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال در خانه؛ سه امتیاز برای کهکشانی‌ها یا یک غافلگیری بزرگ؟
امشب؛ بازی‌ای برای شکار بهترین انتخاب‌های پیش‌‌بینی!
[
رئال‌مادرید
⚽️
🆚
⚽️
رئال‌سوسیداد
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/138976" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138975">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138975" target="_blank">📅 10:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138974">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138974" target="_blank">📅 10:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138973">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/138973" target="_blank">📅 09:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138972">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138972" target="_blank">📅 09:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138971">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
منابع مطلع میگن پرسپولیس علاوه بر رزاق‌پور، جعفری و صفرزاده، با چند گزینه دیگه هم وارد مذاکره شده.
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/138971" target="_blank">📅 09:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🗣
🗣
🗣
باشگاه پرسپولیس در آستانه توافق نهایی و جذب امیر جعفری است اما بخاطر باخت روز گذشته و ترس از واکنش هواداران، برای رونمایی تردید دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138970" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
دلیل نیمکت‌نشینی اورونوف مقابل تراکتور؛ پرس نکردن!
✔️
تارتار از مشارکت کم اورونوف در پرس و کارهای دفاعی ناراضیه و معتقده مهاجما باید بعد از لو دادن توپ، برای پس گرفتنش بیشتر تلاش کنن.
⌛️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138969" target="_blank">📅 09:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZFS0f4DjGNEf-Es2WcM0s2w5eol-YYjcCUdd6t-ONMBKKW7Iv-4hCPwXCmcnAQtJOz0t6NxnOW2gkxgVnV1W6EjGxlXdUt87K3GpRY9JOOKIZ1eoAsfP89q0-LRbCAw07wBzKn0tM9YWY3W1-BVuvAjOVe8JPb1MoAhQjepYA1q1GH2YgZDsPMyFggiEEPQLVuN9Tst2lFABYW6li28Q5drOhKeT3jVQHeXs-F_DsFgI12djqYwbwVH6Fia0RloW8O56egpP38I--pR_wak_3-xLRvfXBX9jIQPWFrCP6R5gQmEwvRn9woE_r7aVkOqMCHveczzvkql2NoyblcYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138968" target="_blank">📅 09:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138967" target="_blank">📅 01:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
دلیل غیبت محمودی در لیست تیم ملی امید این بود که او در اردوی قبلی تیم در کایسری ترکیه شرکت نکرد و حالا عبدی برای حفظ نظم تیم این تصمیم رو گرفت/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138966" target="_blank">📅 00:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138965" target="_blank">📅 00:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138964">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی تیم پرسپولیس: اگر از بازی مقابل تراکتور درس نگیریم به معنی ضعف کادرفنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138964" target="_blank">📅 00:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138963" target="_blank">📅 00:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
با اعلام باشگاه اوستون ارونوف در بازی دوستانه امروز مصدوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138962" target="_blank">📅 23:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b9a82ba6.mp4?token=hCsdpzgP7sK_nPC7cIyILQsUZL_JeRcc3QDoa60yZOTmgyVmkdepcq3G1OCQ2JsP3gMCoKYlI87Yi669_Mgt3dP3FMDG_JUjSYRIyoXzelIiMqUEFxct5wwpJI08VuEVCfAT3rOSqtQ2mbGr2lxsRfVx5Vyn-_OESUb_HElQLCisql1M1uqrqINxi11Jy5Ra-TXM3dMxgio9mkiU37j8H8idu21K3TF8u3gfFvbO_cw_NLnn-ENcvi3iK_0yGmqR1meNqcjs3frd1zu7WRU8XE9Log1m_jNNAnJRRymxL6T4_slTXFzAo-hkL5SKCquYpBRF0zV_INNuuEZ_Z7ngQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b9a82ba6.mp4?token=hCsdpzgP7sK_nPC7cIyILQsUZL_JeRcc3QDoa60yZOTmgyVmkdepcq3G1OCQ2JsP3gMCoKYlI87Yi669_Mgt3dP3FMDG_JUjSYRIyoXzelIiMqUEFxct5wwpJI08VuEVCfAT3rOSqtQ2mbGr2lxsRfVx5Vyn-_OESUb_HElQLCisql1M1uqrqINxi11Jy5Ra-TXM3dMxgio9mkiU37j8H8idu21K3TF8u3gfFvbO_cw_NLnn-ENcvi3iK_0yGmqR1meNqcjs3frd1zu7WRU8XE9Log1m_jNNAnJRRymxL6T4_slTXFzAo-hkL5SKCquYpBRF0zV_INNuuEZ_Z7ngQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/138961" target="_blank">📅 22:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138960">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی پرسپولیس: اینجا هستیم که فاصله‌مان با هواداران و ابهامات کمتر شود و بیشتر همدل شویم. از داوران انتظار عدالت داریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138960" target="_blank">📅 22:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138959">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138959" target="_blank">📅 22:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138958">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فاضلی: مربیگری بی‌رحم است؛ آقای تارتار با هدف بردن، تعویض‌هایش را انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138958" target="_blank">📅 22:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138957">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
🔄
🔄
مانند یک هوادار دوآتشه دوست داشتیم بازی را ببریم و تمام تصمیمات را با قلب و ذهنمان گرفتیم، اما روزهایی هم هست که آن استراتژی‌ها درست از آب درنمی‌آید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138957" target="_blank">📅 22:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
فاضلی دستیار تارتار :
🔴
اسکواد پرسپولیس بالانس نیست و ناقصه ، حداقل به دو تا سه خرید لازم داریم
🗣
🗣
ببین وضعیت چقدر بده که دستیار و مربی تیم اومده مصاحبه کرده داد میزنه بازیکن میخوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138956" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✖️
✖️
برتری پرسپولیس در دیدار تدارکاتی برابر تیم امید
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف امیدهایش رفت که این دیدار در نهایت با برتری دو بر صفر شاگردان تارتار به پایان رسید.
✔️
✔️
پوریا شهرآبادی در دقیقه ۷۱ و ایگور سرگیف در دقیقه ۸۶ گل‌های پرسپولیس…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138955" target="_blank">📅 20:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138954">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
#فووووووووری از قدوسی
🔄
🔄
یکی از بین امیر جعفری و ابوذر صفرزاده طی دو روز آتی به پرسپولیس می‌پیونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138954" target="_blank">📅 20:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138953">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
🚨
الوحده در پست قربانی بازیکن خرید
⚪️
باشگاه الوحده امارات با پرداخت 3 میلیون دلار رضایت نامه آدام چرین، هافبک اسلوونیایی پاناتینایکوس رو گرفت و این بازیکن برای عقد قرارداد با الوحده وارد ابوظبی شد /سدد امارات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/138953" target="_blank">📅 20:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138952">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwes4gk7EVrSRmuQ3pY1P11IBmfdReYGXHIfyAlJj0m7SoJl8PXBFQ8sDniM-B6lIYC1zwyL3NqerpmW-_rxFxS7NJQpZ4GZiePCO9_gcfYpb5QWYbqWewmnss0hwC4yp2eLBo9iwEcup_uotfx5ELSCf01VfIFfCRpGrbEmcSeH4i_Ucx8-1Yh5reN_32RVn7613tCjbCgzmcNWsu8Us7Vb39GYj2esA_QuCKj93QdMb6Z4FIbjlhJBHYrbuCtPi4q7fUzvEDq-q08PtK96sZDm9cZVhS0Ip8quj5AGGY0rjosESAu5lwaPW_wyvYBizEViZDdnXcETlmNiKD1u5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138952" target="_blank">📅 20:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
با اعلام باشگاه اوستون ارونوف در بازی دوستانه امروز مصدوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138951" target="_blank">📅 20:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138950">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138950" target="_blank">📅 20:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZcn5EJhXGcfA6sHJW748Mx8jpEahbiOuX1UXrIg5R_soxV7Mk4RDNkFnBPADf0o81qN8KRBgdllDzPQMEwykWUu_fd3gFU3adOzQBxrIoQwgHKQmQj2XnNJuU9ty2sNySN65rBtmumrAQ5ZHyZxiaNBKb2NUElbfDtuaOqpApHtaO5cjXhtp901rxQjf93edDh6mp4duePy0jAat3Ie4-YuJRSAuPb76gAZWbIv0pWzeLDpImDCDB5oJxFWfAoAkkI0F4ILt1vLgdfZ7I2EVe95BDkL8QyrN_VVPuAyn78hVsWvWY5kkt4QpyDg2G29VkGx1E2ga2A2Q01WDu71bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک دوئل نزدیک در مستایا؛ جایی که کوچک‌ترین اشتباه می‌تونه سرنوشت بازی رو عوض کنه بتیس دست بالا رو داره یا والنسیا غافلگیر می‌کنه؟
[
والنسیا
⚽️
🆚
⚽️
رئال‌بتیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138949" target="_blank">📅 20:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🗣
🗣
تارتار:اورونوف و سرگیف به دلایل فنی نیمکت نشین بودن و من این تصمیم و گرفتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138948" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138947">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaYhxfYExg_Wl-fF1FPixWN7lK6EqP9QrhuOVbkoRjC0eDrfZSNBQcxY4FHFRlLC5ViqTcQxNqoapan6pdW2l8JtWhduQ0j62VDJDv-1ktM5CE2PCgo0OV4kk-Ugak6gqLCcVDj5R8jVikxGC6fc-bdK-uZ8266wELOpLqAQzIQ5R0SqnZq67Z_hHyQKdG5SuN28T18ONmpZDUTQqVPVBfjTy32hZ_9MiFmXhf9Quu7G1RhwTZ-T-BG2cd86LTqQEG6Gi6CS6_um7vOmVyM7kcOrq8c9nPUgptCofws8XT6Xzl2WyP0VEi3gpQcI1FJHy8hiEwbNxVBbJtyHZ5UHAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
برتری پرسپولیس در دیدار تدارکاتی برابر تیم امید
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف امیدهایش رفت که این دیدار در نهایت با برتری دو بر صفر شاگردان تارتار به پایان رسید.
✔️
✔️
پوریا شهرآبادی در دقیقه ۷۱ و ایگور سرگیف در دقیقه ۸۶ گل‌های پرسپولیس را در این دیدار به ثمر رساندند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138947" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138946">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/138946" target="_blank">📅 17:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138945">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
پرسپولیس در آخرین پیشنهاد خودش به باشگاه فولاد برای جذب رزاق‌پور ، دو بازیکن+ پول پیشنهاد داده است!
💣
🔻
همایی فرد + انتقال قرضی صادقی + 100 میلیارد پول پیشنهاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138945" target="_blank">📅 17:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owiOwqpX4v9tq4qmepmFd_FOA07hKMmNwcC9H1DcHdMM5Y2gXvx61L9YrQRE7uyLgBSPyARZjnrrw6A9owUvZnA8iZ6PD-3oXDqsvsAvQLqPBR_Jmti6szBaO6F_XFS8Yjj1CPmWHT2tlsJb0IcIFaAIAEONbWrwtiY0OUGfzzzGR7It69RhRNdttu9ogLegqwHU1nvua6T9CVr22bKIsv7dWiiJpp0e81eX0nhMh8Dwraed_JUx8FfNopkpSYHfm9LwdIz1S2Q6eRnQfCbfR2n2UeXqiFZxFeSvB6JN0GBuOZuI1TChUcqvpg0x1FiAJWIA0emA7KpV9OOjrPn4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
مرتضی پورعلی گنجی از دانیال ایری حمایت کرد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138944" target="_blank">📅 17:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
با اعلام امیرحسین روشنک مسئول برگزاری کننده لیگ برتر؛ دربی پایتخت ۱۲ شهریور ماه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/138943" target="_blank">📅 17:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
🔴
ظاهراً درگیری تارتار با اورونوف سر اینه که این بازیکن در تمرینات دوندگی لازم رو نداره و برای دفاع به عقب برنمیگرده
❌
❌
بازیکن ها درباره اورونوف گفتند که این بازیکن به خاطر اینکه مصدوم نشه تو تمرینات صد خودشو نمیزاره و با بی‌خیالی تمرین می‌کنه و بیشتر ریکاوری…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138942" target="_blank">📅 17:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
عارف معاون اول رئیس جمهور: گران شدن بنزین در محدوده 80 هزار تومان قطعی است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138941" target="_blank">📅 17:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2D94PQSAiLaLvBenpO_IOtPX5BbwQEfq1-thEM954DdRI2YAIkl65FRnamAwNnr-SuddSrj33Wvd4oLVG22HJCQ_Owe7UBUThSJxzghOawogCRoWMtqvSF1v7YLaP0jl6yUgIK52_6O1w0dRWrx9j3Gm2VlvGlTtZmafkx3puh0yPbsNddMzZzzzdp8qTqaA9mst1HAXZUzWY5DNb06bba6PEWpsVARFhA-x_1UBTGXKGhjwXcAxaEank11k4arSh5TjhZ1VqeQkuCj8urDHNEk-9A-jqq06GOcdMDJ7CGr9M71k8Nzx_CGzuppKMeq2Lg0tLibs_pe5P2HKt4zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
💙
❤️
بااعلام‌رسمی سازمان‌لیگ؛ ظرفیت هواداران استقلال و پرسپولیس در شهرآورد یازده شهریور 50 50 خواهد بود و قانون 90 10 اجرا نخواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138940" target="_blank">📅 17:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138939">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUrefIGW37XkvBLGoF0j6f8ZU37NVFz-NEfXGRcsrHZ3As4s-uC4inblpvu26Rq5QY8pMvdQunkUBI-TV8NQ5LDVfZe24j2Ne48XsYXqqXrYWZgikqI8dflrX7yKGBwzvSHNOT-kUUvW2G8Ls299JHgcQImUsPMgwe9oJMJdsEuKhoQ4KOl_VjhBYm1DyQ4hGHXU3jc9LRfIYZKXBsh9k96TeGS0m_S425-OizK_QNYP_jjof4HTsGVlXCTJNtgmQ0RzIkw36S0FigrQhHJtHL-OH1Px-Sj27T9oxlbF0PNRIIZMRfrRN0UTWFKfop2WpWzaX9VwW_A-LFHk5zYvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
استوری مشترک بازیکنان پرسپولیس بعد از شکست برابر تراکتور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138939" target="_blank">📅 17:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138938">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236791415.mp4?token=XmCQiJJrQfptL_v58NL0YgfiyGMhFVqLOXBvNEEH8Fqg2BR6QfFo6Thf3hqlqQCOU1WvuQBiCZQEYHS6BR_SwZfOfOiGhIW6-x0YaO7MLQM8Ckew6BQ31OzwydfKOy1H7iwHOE8dnBLMpRhx_RLMrezeN6cnQebU5DgSykuxfztY3KyKNQLj6dyGGp4OCnUeHXIfyiyZUYK8Vz9LqOSABwFarmZEOtGqjd4mSA6nGzfDLigQY9fIwl2PmJq15HsD2UqWK05fEmjBfexrvySU7z8YOljN3RI2We6cUsGjky6YXZhJcGRaFaKmqJSI_uHHGwpNczwfYHakjmrv4X2vdbr66YTlP7NIRFylTrmRf3_Cz1EVhwTiiOgawTV01Z6h1EOli8a68jbqcuLtORsNoz6PIe3IrHHVXwJv-sMTM37j7YOusp2P_pwTSZS2ZkZo_x1f3wLxSn6PKcYh9ao8c6i8lsDk4QXBcYcsxhFC15TnvTmfheZU1gpE7yaIzJBa_hrJDC4ZDJtAiFLaFn6Ox8418jq8A0PcYfVo9Zqev8NMl-zNU5uYBsP18QJI639a9SU3Rr5hi1dr9P7wY55RG17oCo3T0pF2X6XmJ0ZoaSEBdUEG8TyJTc_LqJ3mJC1YFxzTdvb8UDDt50iKDIfmLFSltHwnyihyOZF4ERB4Cak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236791415.mp4?token=XmCQiJJrQfptL_v58NL0YgfiyGMhFVqLOXBvNEEH8Fqg2BR6QfFo6Thf3hqlqQCOU1WvuQBiCZQEYHS6BR_SwZfOfOiGhIW6-x0YaO7MLQM8Ckew6BQ31OzwydfKOy1H7iwHOE8dnBLMpRhx_RLMrezeN6cnQebU5DgSykuxfztY3KyKNQLj6dyGGp4OCnUeHXIfyiyZUYK8Vz9LqOSABwFarmZEOtGqjd4mSA6nGzfDLigQY9fIwl2PmJq15HsD2UqWK05fEmjBfexrvySU7z8YOljN3RI2We6cUsGjky6YXZhJcGRaFaKmqJSI_uHHGwpNczwfYHakjmrv4X2vdbr66YTlP7NIRFylTrmRf3_Cz1EVhwTiiOgawTV01Z6h1EOli8a68jbqcuLtORsNoz6PIe3IrHHVXwJv-sMTM37j7YOusp2P_pwTSZS2ZkZo_x1f3wLxSn6PKcYh9ao8c6i8lsDk4QXBcYcsxhFC15TnvTmfheZU1gpE7yaIzJBa_hrJDC4ZDJtAiFLaFn6Ox8418jq8A0PcYfVo9Zqev8NMl-zNU5uYBsP18QJI639a9SU3Rr5hi1dr9P7wY55RG17oCo3T0pF2X6XmJ0ZoaSEBdUEG8TyJTc_LqJ3mJC1YFxzTdvb8UDDt50iKDIfmLFSltHwnyihyOZF4ERB4Cak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/138938" target="_blank">📅 17:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138937">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_78ohIfCfr9sI66tAV11mMUlph4qC-3Q05fYaffZbD9HR7tDzBSXIUmrkBVw5ph0o5elOYfgDEpEhIKMmi5gg-V5GEs5e9jEkSyMsV7GwtFZscEagT-yftCG_WdSjmyCe65Us5tzpUTyj1lb7OxpCF8VShSJHxHaPLcipVoQptujdlobOyx4Rf2tT4g8NsauZuleuMuCxvIolPewKwDZ7qi2ZU-B8PorjmP0paxb_DcPZsW6DavwoKi7JBYOmJ8PvvOJ3Z-ffyVito4rHW5uOUV88AV_AMWEGJiAfRQB6LMDhhCkGrLaC9L1n0NI_wjLDXXYTx--wn4yfgog5XrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
آقای تارتار به بهانه جوانگرایی فشار در رو ننداز روی جوون‌های تیم، عامل صدرصد باخت «دلایل فنی» شما بود نه هیچ‌کدوم از بازیکنان جوان تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/138937" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfObfkPKsQDPz2Hq79vyJceXpr6VeUndbSCnDJEiHJnJTkuLpB36OZ4fI2fVNI0DumuvP0zniMrT9JSQNYkvIk0Nw-GY2ss14YnI4KgtA548GF8l5vT09oVgwpKVgjnCtxJue0rnWlpoYfTsFuDcMco6NFCv4_3jpEuorZQyyba0IlssYsZgAZ2Mj7lXq3A-XV5EXUAHDz5XWcDjLrPJZM4mH4GM8VHH5EOyoZVDQozy4AZdYFyMD9Z7iHQNbm72WhE664TJvIrJOoT5wukCGSXAqLPGqTdRdo_CAW8lpt6QzVqD90Kvsk-4gG7OtsLAx_b_oDIlsYItu-19-NHp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چند بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
از تقابل حساس الاتفاق و النصر تا بازی‌های جذاب چمپیونشیپ و لالیگا؛ کنداکتور امروز ترکیبی از بازی‌های پرموقعیت، دوئل‌های نزدیک و دیدارهایی با برتری نسبی مدعیان است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138936" target="_blank">📅 17:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
💢
💢
💢
💢
شنیده میشه که اورونوف و تارتار به مشکل خوردن و به واسطه کنعانی اورونوف کوتاه اومده و فعلا خودشو نگه داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138935" target="_blank">📅 13:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✖️
✖️
✖️
ابوالفضل جلالی در گفتگو با مجری فوتبال برتر گفته مصدومیتش جدی نیست ده روزه برمیگرده و احتمال خیلی زیاد دربی در ترکیب پرسپولیس قرار خواهد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/138934" target="_blank">📅 13:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
بازی بعدی
✔️
هفته چهارم
⚪️
شنبه ۷ شهریور
🔴
پرسپولیس - ملوان
🔴
ساعت ۱۹:۱۵
🔴
ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138933" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
علوی سخنگوی فدراسیون فوتبال: سرباز شدن بیرانوند؟ تاریخ بازی کردن او تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138932" target="_blank">📅 11:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138931">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
✔️
۲۴ساعت تا پایان  پنجره نقل و انتقالات تابستانی…پرسپولیس هر بازیکن و میخواد بگیره باید امروز سه شنبه بگیره وگرنه بعدش فقط بازیکن آزاد می‌تونه بگیره بازیکن آزادی که مثل همیشه ی مدت بازی نکرده و مثل هندوانه سربسته اس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138931" target="_blank">📅 10:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
گویا دیشب تو رختکن حال دانیال ایری خوب نبود و ازبس گریه میکرد شرایطش اوکی نبود. بزرگ ترای تیم هرچی سعی میکردن ارومش کنن فایده نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138930" target="_blank">📅 10:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
فوتبالی: ایری تو رختکن گریه میکرده و بزرگترای تیم بهش روحیه دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138929" target="_blank">📅 10:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138928" target="_blank">📅 10:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138927" target="_blank">📅 10:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138926" target="_blank">📅 10:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❤️
❤️
صبحی که بازی و باختیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138925" target="_blank">📅 09:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔵
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔗
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138924" target="_blank">📅 02:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
آقای تارتار! بازی هفته قبل تراکتور با سپاهان را ندیدی؟ چطور دقایق پایانی حواس تیم تا این حد پرت شد؟ مشکل اورونوف چیست؟‌ شفاف به هواداران بگویید. پرسپولیس نباید بازنده میشد دو برد اول چندان مهم نبود اما این شکست خیلی غیرقابل هضم بود. به امید بازگشت هرچه…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138923" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138922">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/138922" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138921">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
فوتبالی: ایری تو رختکن گریه میکرده و بزرگترای تیم بهش روحیه دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138921" target="_blank">📅 00:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
آقای ایری؛ شما هم جوان هستی و هم تجربت کمه و فراموش نکن ماهم اونقدر بی معرفت نیستیم سر یه اشتباه بخوایم تخریبت کنیم
❌
❌
اینجا پرسپولیسه، قطعا یکی از تلنت‌های فوتبال ایران هستی و جام جهانی هم رفتی و ما انتظارات بیشتری از شما داریم. در آخر فراموش نکن هوادار…</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/138920" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138919">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=HOD5CeEqKNANmxFNw5wfvULIRaUg6PMFjJ8BQTIo_iqgJ4EQFexyeFY7Rt9cz-pDJ20x8rmiEQvvUB-aDLEXUEabvEZJv2Hd2lh37s-SjXU24FMICTAqJO3zWGC3egY3jatmlJPCiXBDddChxTM3_f7iYKjFwQ_zYBR_sQuQhDn3ZIKykWYl9KvZZ24lHTHEiIN_vCTLzbZ4F4Hf2I12MO0QPSsMyhIvfi4RcESGd5DxdHvOv8vY4BMKilr0WAFMhSo2OofDoymXZ2doObZpajYgIOWwP81HM4zTBCza2RwDNsmAAKJB8bGvgXn7SkUr-yIb4zdlSLonN_-JoF031g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=HOD5CeEqKNANmxFNw5wfvULIRaUg6PMFjJ8BQTIo_iqgJ4EQFexyeFY7Rt9cz-pDJ20x8rmiEQvvUB-aDLEXUEabvEZJv2Hd2lh37s-SjXU24FMICTAqJO3zWGC3egY3jatmlJPCiXBDddChxTM3_f7iYKjFwQ_zYBR_sQuQhDn3ZIKykWYl9KvZZ24lHTHEiIN_vCTLzbZ4F4Hf2I12MO0QPSsMyhIvfi4RcESGd5DxdHvOv8vY4BMKilr0WAFMhSo2OofDoymXZ2doObZpajYgIOWwP81HM4zTBCza2RwDNsmAAKJB8bGvgXn7SkUr-yIb4zdlSLonN_-JoF031g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون فوتبال: سرباز شدن علیرضا بیرانوند؟ تاریخ بازی کردن بیرانوند تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده است و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138919" target="_blank">📅 00:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138917">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
حدادی مدیرعامل باشگاه:
🔄
🔄
ضمن عذرخواهی از هواداران محترم همه ارکان باشگاه در باخت مقصر هستند؛ از مدیرعامل تا سرمربی و بازیکن.
🔄
🔄
اما برای موفقیت، یک راه داریم؛ حمایت از سرمربی و حمایت از بازیکن، بخصوص بازیکنان جوان، اگر جوان‌ها اشتباه می‌کنند. مقصر من…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138917" target="_blank">📅 23:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138916">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
جوان بازی دادن تاوان داره
🗣
لطفا با یه اشتباه اینده های باشگاهو خراب نکنید
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138916" target="_blank">📅 23:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUMh6DQD1hLHIRPD_0a2vdU-mFG3ena5FMgsanjpqpveqiiPveT4VJr4FSP43uVQGpfPO7d9psBO1thPT5SjWdGm7VVlv0ACbYA_aDEN4MAKpSvibvMY-W6Q6OaZSWfWh6RUk4FK1iHDXX_bAHkUIlYFtzOxy6WXhOtjrjDMxpC7B4lrByFyKUzMqfRGA7G7Ob-9WyU0K9_l_k86KrcT6VYZOL_8Odmk19bfFrMn5wI30a5-Q4sO7wga4-0gs8DVZVmw37aGOrtYbgMbWbbYGV6WEgx-fqjdovgRveIZ48HxyIZl8NdugAzuaeJMq4y7WinSbQ-Hb3wYvNvAPnSBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
جدول لیگ برتر پس از پایان هفته سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138915" target="_blank">📅 22:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138914">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
باید بچه ها به خودشون بیان ...فاصله بازی ها کوتاه کوتاهه ...امیدوارم این باخت و جبران کنن ...با فاصله خیلی کم شنبه با ملوان بازی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138914" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138913">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚽️
⚽️
⚽️
⚽️
از بین ابرقویی، تیکدری یا عیدی یکی دفاع چپ پرسپولیس مقابل تراکتور خواهد بود/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138913" target="_blank">📅 22:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/138912" target="_blank">📅 22:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138911" target="_blank">📅 22:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Q8kKph3h_nLo39z_RX9GQkRAE3E4kiYcL85FIpojHsw3pVujsPDIIuP0D1RnfKEq2R_jLp0byfIA8oLeec2g_qJa4WJnHG-xPJlC_PCUIVdaEfPyWp4lTRX95ZlfLcren3pruoooX5pLpMgHjCXvmKCmB8KoBZLZH-A1vl2JQ7Byg9sBjOkHvgWZRVSnQ-rTYmUnb6l4bHTrs0sJnopny58j4E8oqdmpdkTaV4q5Z-yKlobd2JZnJLVgbXMFY8mIoyc9qsKXTaeJbi1Z8xpQEq638L17tUDOkxBi5UHcQH66Na9uXdVZUK-wRuP3ba5kGoUPryq9pDVda4-TC2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تنها فقط تا آخر امشب فرصت برای بونوس ویژه بازی Scarab Temple باقی مانده!
🔵
کاربران اسپورت‌نود می‌توانند با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
🔵
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/138910" target="_blank">📅 22:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138909">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138909" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138908">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
تارتار: مسئولیت باخت امشب با کادر فنی است؛ فوتبال همین است اگر اشتباه کنی بازنده می شوی
🗣
جوان بازی دادن تاوان دارد/ اکثر بازیکنان تعویضی ما سنشان 20 تا 22 سال بود. نیمه اول موقعیت های خوبی داشتیم/  امروز کم شانس بودیم و کم تجربه، تاوانش را هم دادیم…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138908" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138907">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
کمال کامیابی نیا: هواداران پشت دانیال ایری و دیگر بازیکنان باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138907" target="_blank">📅 21:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138906">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
با تمام وجود امیدوارم این آخرین عذرخواهی شما باشه از هواداران ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138906" target="_blank">📅 21:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138905">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/138905" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
