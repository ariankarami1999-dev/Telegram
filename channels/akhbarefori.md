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
<img src="https://cdn4.telesco.pe/file/TsJG-tXh4zslwA5kyaFRz6zZUfRB7uw_QZrhmkocBYuy7lty-Whvl21f3Wm5nTKdK3B03bMoT-aQU5C2zZrDl0OLvOCze6zp9xWXZ2-yTyoZZPAqB8oxa5keTSnxp-cPkKdICVK4t3FDstZzRgY4v-nxLv05N5fGyjx8yjbHM2ltJenkxVQDtsjYRm86INPNv8FUDgccCJmj-UxAjifGQtYxx4s9bKQB3K6zj3empbw2KpXTyaJqfK55rcXmXaflWHMO9DIcE_1-xmjeUc8cxvbR5JonH8r7vLV2XaOgmrYLeymiN9i-niPFcu5ioDIP0Mu7hJVLm9yIBaAZgSeYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-661347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcJfF7-c5Clwlzvtx0XPPb7eLv5IqccrPn9fry_OxK2waBq-Q3D5ixbS8ny0DkRJPqGwvS8U9Vk754mzKPCe262sw5oEqawzjbBDdgMUN5EG_EHhMM3EAIINSt2f3Z2-EzD95uICtfHU93TBFuuT_2raH3FOqimBNcjWZ2I5IW1nP6ZmkY3k76XqzAZe7riWrqpIfAN4_2YtqwICkXeIsgtvofQ1oSBf5hmVzZVr59lKlW4sfTgkfZn32eZ23P1zr0rHepRVhs2scytwaumKd2Xga0UyCgg7zRWD0RsMRuH1ApIAxpbhfu4vYl3prbsl8hF4ehSgCBEaeXCSZD4f8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26 · <a href="https://t.me/akhbarefori/661347" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
کمیته انضباطی دانشگاه صنعتی شریف در احکام بدوی، ۶ دانشجو را به‌دلیل نقش در ناآرامی‌ها، برگزاری تجمعات غیرقانونی و برخی تخلفات دیگر به اخراج محکوم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/661346" target="_blank">📅 11:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrNB-Y-nvcnTuv2p_SYN_iWCN-34ClaQ6QMFKl4lJMa-zUEXKywfnyFiNN2vKXPuHI0K7YMPuqiS37idedDMAreW2J3hbNsN8QK8o9Hx0HvA43MY6fz-NEbbtNz0lsLxz8-rRJFBhRDBoxIO8lVM3mw4XTDENF2u0bU9V2bpP9m72MDY7PHXh9-DS-VCfES4XDRcfALVZlCiFBWlSxCwD31XtZM44OZNVEEVEOjBbrGO6tUZvKUNj9VdToiNbFrqqNdFRxMVYT4i0vkM3gnVRMtbtiZ4FND4oSQ9tWEP4YQgw2ZE0yXMlpRAiHySjrLZj8CE0YBmGud2M_m0kdgoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تنظیم مخفی که می‌تونه گوشی‌ات رو نجات بده، قبل از اینکه دزد گوشیت رو خاموش کنه، این قابلیت رو فعال کن! #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/661345" target="_blank">📅 11:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUFfD70NdJXIO8X-zFzTiUBWyttZR24XPJ5VvU1lxsIF1hpjJIvLGCcjJw4DRuMlBsFlw3yLjgr3-KMr2AN_DH5OEM3CU9e3xLennMa5EtrmMZHk0ywSSLSsdjLS2-PgvnIkUX2uC_R5l9YHnabYQ2Ww1DRsyMaiPqPHe1Yn022PsTmip0_eagdK7Aev3n7zXOxcIbFrxhdSQJW77Q5VZCOC8dNhBnQAk1Q5owhiuMSv_aJUpyiJG1I9Y6mTUguN4_HqOnoi_nm68bI8yv1XwbHL8Fg-SBsIwQYxhFwF-tpbs4vfi24Pq4UB0lucrassnwzQ92Ll8oXTtRIEA4Yztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی به مناسبت روز جهانی پناهندگان: چرا با وجود دهه‌ها تعهد و وعده، شمار آوارگان جهان هر سال بیشتر می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/661344" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6aecc6ee.mp4?token=PGilxfiGkYD-18xfb3s6ICCzd6RUdLAeUexOXdElNAzGKLgTkmUQYt3tohThRrPrLGmxNDqu7pAhEmTY3aiiT5lu53W21d1kh7gPZe7kJcifwniufC2y37Gvcf6izuUFy79NRj_e3gkWqxakaQR3TBe1AW4oXGsJslOHPScZmozBjBznwxv5ELzHuaACuVPsxT7n0gji7FI9VSfsN0G9EdxvtVw9r8UwTdxN4tGUf5LYjqfj6DaUcDZF6aUVHn0Q_yTfHqPiXRb9EOMsafDhOQjlfG03pzNjRSORQFCt1BHicwZ42yjDSdVOe79ZQ6Rp3aiirKUOIgu_Q0yVrfrCow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6aecc6ee.mp4?token=PGilxfiGkYD-18xfb3s6ICCzd6RUdLAeUexOXdElNAzGKLgTkmUQYt3tohThRrPrLGmxNDqu7pAhEmTY3aiiT5lu53W21d1kh7gPZe7kJcifwniufC2y37Gvcf6izuUFy79NRj_e3gkWqxakaQR3TBe1AW4oXGsJslOHPScZmozBjBznwxv5ELzHuaACuVPsxT7n0gji7FI9VSfsN0G9EdxvtVw9r8UwTdxN4tGUf5LYjqfj6DaUcDZF6aUVHn0Q_yTfHqPiXRb9EOMsafDhOQjlfG03pzNjRSORQFCt1BHicwZ42yjDSdVOe79ZQ6Rp3aiirKUOIgu_Q0yVrfrCow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ شهید در حمله اسرائیل به شهرک باریس در جنوب لبنان
🔹
منابع خبری لبنان گزارش دادند که در حمله هوایی رژیم صهیونیستی به شهرک باریس در جنوب لبنان ۴ نفر به شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/661340" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: برخی افزایش قیمت‌ها تبعات شرایط اقتصادی کشور و جنگ است/ اینکه بگوییم صفر تا صد تورم و گرانی‌ها متوجه دولت است؛ دقیق نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/661339" target="_blank">📅 11:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtdwUCUlScYDj9jmX7ZjtX8mMulZL6NQR_Hm82ZYMM1td-qrC01guz68XMBwOGpayutpVif29_AEBUDK-hvQ86VTSpoYrKZj9uMf9gIx85oEiRiGpok_zhfI5oE0m06V5Bta_NYqB8_MBVBOe2_INnmTAzKhJiBgmCjYP--LiQduA_6xzCUiVvOmRsV11lGdtGRe3HmxcYacQXe1asXBfmoEzaMJP3Q6Zk8CXTJNGCdQ3Xr7DQyz_yEAb0gxCoHVsrfBSsc9LqTX-mU46KNeqnxjsFrvsVk39sbIrLvvGxlMWHoxLDbBx7p0mgGkoy3FiHo93BSlR2uvZ1XesXCgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم سالاری در آینه اعتماد
یادداشت محسن بیگلربیگی در روزنامه اعتماد
در راستای پیام مقام معظم رهبری:
🔹
آنجا که رهبر انقلاب با وجود داشتن دیدگاه یا نظر متفاوت، به تعهد رئیس‌جمهور در پاسداری از حقوق ملت ایران اعتماد می‌کنند و مسئولیت تصمیم را به دولت واگذار می‌نمایند، یکی از ارزشمندترین صحنه‌های بلوغ سیاسی و حکمرانی در جمهوری اسلامی به نمایش گذاشته می‌شود. این رفتار نشان می‌دهد که مردم‌سالاری دینی نه یک شعار، بلکه سازوکاری عملی برای پیوند میان رأی مردم، مسئولیت مدیران و نظارت و هدایت کلان نظام است.
🔹
اعتماد، سرمایه‌ای است که به آسانی به دست نمی‌آید. همان‌گونه که رئیس‌جمهور در برابر ملت مسئول است، این اعتماد نیز مسئولیتی مضاعف بر دوش دولت قرار می‌دهد تا در همه تصمیمات، منافع ملی را بر هر ملاحظه دیگری ترجیح دهد و پاسخگوی نتایج عملکرد خود باشد. در چنین شرایطی، مردم نیز با مشاهده این پیوند میان اعتماد و مسئولیت، احساس می‌کنند رأی آنان در عالی‌ترین سطوح تصمیم‌گیری کشور اثرگذار و محترم شمرده می‌شود.
🔹
امروز بیش از هر زمان دیگری کشور نیازمند تقویت همین سرمایه اجتماعی است. سرمایه‌ای که از تعامل سازنده، اعتماد متقابل و مسئولیت‌پذیری شکل می‌گیرد و می‌تواند پشتوانه عبور از دشواری‌ها و چالش‌های پیش رو باشد. اقتدار ایران تنها در توان نظامی یا ظرفیت‌های اقتصادی خلاصه نمی‌شود؛ بخشی مهم از این اقتدار از اعتماد میان مردم و حاکمیت و میان ارکان مختلف نظام سرچشمه می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/661338" target="_blank">📅 11:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: کنکور سراسری ۱۴۰۵ در ۲۹ و ۳۰ مرداد برگزار می‌شود و زمان آن تغییر نمی‌کند
🔹
نتایج نهایی کنکور احتمالاً در
نیمه اول آبان
یا
نیمه اول آذر
اعلام خواهد شد.
🔹
برای
آسیب‌دیدگان جنگ
نیز سهمیه‌ای در نظر گرفته شده که پس از بررسی نهایی به تصویب خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/661337" target="_blank">📅 11:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اردن دوشنبه میزبان نشست مشورتی وزرای خارجه عرب
🔹
خبرگزاری اردنی «پترا» اعلام کرد که نشست مشورتی وزرای امور خارجه اتحادیه عرب روز دوشنبه برگزار خواهد شد و پس از آن، شورای اتحادیه عرب در سطح وزرای خارجه خود، صد و شصت و پنجمین نشست عادی خود را از سر خواهد گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/661336" target="_blank">📅 11:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تداوم نقض آتش بس| خبرنگار الجزیره: حملات هوایی اسرائیل در مجاورت ارتفاعات ریحان، جبل الرافعی و شهر حبوش در جنوب لبنان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/661335" target="_blank">📅 11:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJzPQmDFQ_emlav0OCuzZ3_p_zQHH2NsOllyj4YNkv-9lkWxuD5gvjDrkuIn42cpVn-m2p_VdILMv_DfxOF65lBHhAiCBMmDGYLvd6rbpiV1H5YLkMHH5RLgNVf91nAzb5AIDeXgFCbNUGdtDTxnH7PKX2yl6zLicQABpUJjniCvRmA_mTs-OpdIUcfSQPbp9FNbB56O9b7dS1NMpl84Mt_mPnWO924BxfFv0cDcIlsQ2reQ6v74hWLxKIxl8YOzWsJcTqyMGfLxIpQ1dLTgAm244BNkU0TxnkUfCFniU5mzLUnyWnjhvRHIliQMM0FBC_VZ5Vtbgfa4pqiBDjAYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم برتری شبکه سه در تجربه تماشای فوتبال در ایران
🔸
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۴۴٪، سهم بله حدود ۳۱٪ و تلگرام ۲۵٪ بوده است.
🔸
بیش از ۷۱٪ شرکت‌کنندگان مسابقات جام جهانی را از طریق شبکه سه صداوسیما پیگیری می‌کنند.
🔸
شبکه سه صداوسیما همچنان نقش غالب در پخش و جذب مخاطب برای رویدادهای بزرگ ورزشی دارد و جایگاه پررنگی را در تجربه جمعی تماشای جام جهانی حفظ کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/661334" target="_blank">📅 11:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50088d0513.mp4?token=NtvPVyOiTcTH6dryL8M_Ygzh9BTMMeAqZgC7VxKKFZcCsDZvOOvH6eEnj_dAJ_tqQim35HWFUnNkP9u1yxvZaKz97c5_B_0f7XnngFQ8RLejdRnqX2n2Sk56g_Oscgqh0NtHSdyYHfAc8IWeWq5Zp5kp7b95Ij2HLXqvqDQUcuqmFg_6rlCOhZRefkiinwnFzdSpm4hTu2pp9ya1-R3T4w75o65_DznckJpulFHlbNy8OdY7Vodr5xAyatSH3PJfko-L6oHa6293rZiJm1aQLBI0tNcMI0EMxD7cCcnMprH0k_Ibh_vu-IbdwtW3uoWzlQWf7YFVQxU-pMr_doexwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50088d0513.mp4?token=NtvPVyOiTcTH6dryL8M_Ygzh9BTMMeAqZgC7VxKKFZcCsDZvOOvH6eEnj_dAJ_tqQim35HWFUnNkP9u1yxvZaKz97c5_B_0f7XnngFQ8RLejdRnqX2n2Sk56g_Oscgqh0NtHSdyYHfAc8IWeWq5Zp5kp7b95Ij2HLXqvqDQUcuqmFg_6rlCOhZRefkiinwnFzdSpm4hTu2pp9ya1-R3T4w75o65_DznckJpulFHlbNy8OdY7Vodr5xAyatSH3PJfko-L6oHa6293rZiJm1aQLBI0tNcMI0EMxD7cCcnMprH0k_Ibh_vu-IbdwtW3uoWzlQWf7YFVQxU-pMr_doexwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: برخی افزایش قیمت‌ها تبعات شرایط اقتصادی کشور و جنگ است/ اینکه بگوییم صفر تا صد تورم و گرانی‌ها متوجه دولت است؛ دقیق نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/661333" target="_blank">📅 11:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/661332" target="_blank">📅 11:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f067281ed7.mp4?token=q2hq0JKmWMUDX3dmazg5PXqlEERlfV1SACEvtNcmx5eT6qogt-rjGhgf0uSrS3IU28JVPjyKYV4p-Wb1zIvUA6At_focjyGtj9WFlIMNG8-cwBCjtlXxyMu0yDR1dOvR1THUrMSDyRS7dEuagS2ASEiHuiEV9xDVdzevddaNLFfDHXbHeCCskaUhhEUi15-_jiSM_BY5brPyzA4tZye8f-oJiXylxt2g16QYiPPWkJzZ8-wO8PPbvfZuMV__qUtUgCEnJH3jdA7vxvr4d8HlZDsCtqcrr33VsyQil1O_tL08q9PgAmX9QD38gEvsYNinapX9KgjtvAIBRTqNFOXgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f067281ed7.mp4?token=q2hq0JKmWMUDX3dmazg5PXqlEERlfV1SACEvtNcmx5eT6qogt-rjGhgf0uSrS3IU28JVPjyKYV4p-Wb1zIvUA6At_focjyGtj9WFlIMNG8-cwBCjtlXxyMu0yDR1dOvR1THUrMSDyRS7dEuagS2ASEiHuiEV9xDVdzevddaNLFfDHXbHeCCskaUhhEUi15-_jiSM_BY5brPyzA4tZye8f-oJiXylxt2g16QYiPPWkJzZ8-wO8PPbvfZuMV__qUtUgCEnJH3jdA7vxvr4d8HlZDsCtqcrr33VsyQil1O_tL08q9PgAmX9QD38gEvsYNinapX9KgjtvAIBRTqNFOXgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور:
برچسب تندرو زدن به منتقدین تفاهم را قبول نداریم/ طبیعی است مذاکره و تفاهم مخالف و موافق داشته باشد/ جنگ و صلح دست رهبری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/661331" target="_blank">📅 11:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661330" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxVIeADjhdcKE1pjgWQAvkDJYEhUGuM3aGh5VS-yKVGi9zVXqvs_EEZgP9Tyk33AqjuNoKqpmv3cjdTKeEdCbHrk8dqlXzjQdwLCBRtWqcWEdVR1f_HtCvn9Uc5TT_6xn0KuHIy4q4geojuQVWf1c6ScLygunyUBH_4PjXJweURMp6kcpmh8g-oxvWMZAcurrloXmn7NuJdn6uRt-yxMU7uqnFNeZLOrP3nlvpVf_l9I3BwOOeqXnJonPDRNGYT29MbGFkGHLe4SE3CrSknsX3WK8izIekZU5cKrjurcjoG_SlIXxwDaFAf3q4uHmcqgr6ayVZIP0neN4Vu0wpPv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
فقط تا
شنبه ۳۰  خرداد ماه
فرصت دارید
❗️
اگه بیمه شخص ثالث خودروی شما منقضی شده، الان بهترین زمان برای تمدیده
👇
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود! فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید
✔️
تا ۲ میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
#بخشودگی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/661329" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بانک مرکزی: ارقام و درصدهای مطرح‌شده درباره افزایش یا کاهش نرخ سود سپرده یا تسهیلات بانکی، اعم از افزایش یک‌باره یا مرحله‌ای، در برخی رسانه ها مورد تأیید بانک مرکزی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661328" target="_blank">📅 10:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مدودف روسیه: تنگه هرمز به "سلاح هسته‌ای ایرانی" تبدیل شده و به همین صورت استفاده خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661327" target="_blank">📅 10:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOqQQ8iNCnNH44bnMIvI7Oq93NnsVz9kireU_r-5IWpx3IFdPPRbk_9qxwwK_Wkcqm4hYoX9Il3h9pb46FBlsB01-pgkoPqH-GlaO47FHRbtXnwgINyjCff5fNAliucNAfRaC5HOsd6Y0futTM-7HZzUTLjoBe1JljZQaJtGIoyxwRCMiVpRdgI0mbOw5dzPu6UMUgO48Nwf-ZzGLcvBZe-MFaq9HVe7SQ7dYml0AqrFRxvzqVWPbJdWYrkQgP6KRuUxJAxo90i48zd33s7BqyD8-rAmzAWO4p-NtpaDBCk9nOie6qxi7LMybZcP831HTDkI7zDmiJgxjyns1qlQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج افزایش دما از امروز آغاز می‌شود
🔹
بررسی نقشه‌های هواشناسی نشان می‌دهد از امروز شنبه، دمای هوا در بسیاری از مناطق کشور روند افزایشی به خود خواهد گرفت. این افزایش دما به‌صورت تدریجی و پلکانی ادامه یافته و در روزهای اول و دوم تیرماه بیش از پیش محسوس خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661325" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دارایی‌های مسدود شده ایران کجاست و چقدر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/661324" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ_gsFWruar_pmXJs1iy-p_23EA3BpHzqkd5c_4ujBdrHGWuyzJfgU5RTYQqo4ij2Z6q8u8Q0P0cVN6tBv19pyOMT2sKlviQasjU5lXX1HWk9IIdHM76QDLQntDYxH-VaWTglMMavUbOYTQlw0zPp1iX1nlGLWkEWkFdtctWKK_RR6bzPLHNoAYPOG6DreAgo5HOaB6zIwyVkgm1boXL2n-L5tNZefCbQJNoSnt2781heOIIiuEi-3ttodFax55FJayHw8LbD0yfmDytcYczKVN-vzHAORSIN-P7XupH2FRoK-X6pyFPPJwRb_5lRALrAEV8GsO3nbTIVXJMJKAjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت  طلا و سکه هم اکنون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661323" target="_blank">📅 10:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تصاویری از بمباران‌های وحشیانه و پیاپی رژیم صهیونیستی در جنوب لبنان از صبح امروز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/661322" target="_blank">📅 10:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bc2bcd6.mp4?token=UbdW944YNIDbE4wM_a4d1NVnUmMPUEodTjg0NAgyKirMJ24IBd7mddySIqc3kqZQkzIPMJbm6ofZXIC-_a6ItBVrKEUMKOZa8HdVSo5pMu_6ZD72G75ttuLX3Ss3hTqw3BAH2Fap2WTmI5ZDVKG-e-X1kBth1QnkFSOv35tTQchyJOnjo0N-mpZYuqGE-WYmbHIXGoNwntV4l-Y5w5y_f0hd5QyvbB3EZVXjYbgWaBVHH6V8vcP4-xoq5bfs8QAEQpSJ9hOkSBOamosmABzw_mZyQH_7AuWhLD5wDRT7B_kbOJCE8ytJ5fgwt6CGsvvFqfuGC32r-cuhpemn2qVEOqDoyKyPdSu1x98CokHOvCd5iu6mAi9oI3Im0EtlIlwWGxc6iGBbg7U76fHr6wcwB2XtPkD-dDkc0vgxxHLLYABdnVmh7Z2_h7f5cd59EW4HMMsdBrc9z_JpfgDCE5kMXNu8LWMe2Y344W5AtGvBDvhHop6zy6HBw4kGQ99sRRgq_OAZLjceeNHeFNWLv1HH9HnGk_svQZ4rLKb0x4qRC1-w03QsToLBk8OOCJeWLFb-z1KTutvCqT-rVwOUG_99MdMCwSdAFt3KNB59r9_6akqeBbyWF7xN888_wbooiNrTX8il-u-ofwabSQfFOKwIsQYzWheoH8kjCcFHiq82mO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bc2bcd6.mp4?token=UbdW944YNIDbE4wM_a4d1NVnUmMPUEodTjg0NAgyKirMJ24IBd7mddySIqc3kqZQkzIPMJbm6ofZXIC-_a6ItBVrKEUMKOZa8HdVSo5pMu_6ZD72G75ttuLX3Ss3hTqw3BAH2Fap2WTmI5ZDVKG-e-X1kBth1QnkFSOv35tTQchyJOnjo0N-mpZYuqGE-WYmbHIXGoNwntV4l-Y5w5y_f0hd5QyvbB3EZVXjYbgWaBVHH6V8vcP4-xoq5bfs8QAEQpSJ9hOkSBOamosmABzw_mZyQH_7AuWhLD5wDRT7B_kbOJCE8ytJ5fgwt6CGsvvFqfuGC32r-cuhpemn2qVEOqDoyKyPdSu1x98CokHOvCd5iu6mAi9oI3Im0EtlIlwWGxc6iGBbg7U76fHr6wcwB2XtPkD-dDkc0vgxxHLLYABdnVmh7Z2_h7f5cd59EW4HMMsdBrc9z_JpfgDCE5kMXNu8LWMe2Y344W5AtGvBDvhHop6zy6HBw4kGQ99sRRgq_OAZLjceeNHeFNWLv1HH9HnGk_svQZ4rLKb0x4qRC1-w03QsToLBk8OOCJeWLFb-z1KTutvCqT-rVwOUG_99MdMCwSdAFt3KNB59r9_6akqeBbyWF7xN888_wbooiNrTX8il-u-ofwabSQfFOKwIsQYzWheoH8kjCcFHiq82mO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دوربین‌های مداربسته از لحظات اولیه حمله به نزدیکی بیمارستان سوانح سوختگی شهید مطهری در جنگ رمضان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/661321" target="_blank">📅 10:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f92631e03a.mp4?token=dpTTdA-pJNhrNpf30PBLbK6KDSvD3Lj65ClCrUrUi0obGEQOkO8tuOu33fKvJ_qjw0K2htTFv-8loK3Gw5ZsKuHy6us7WyBg1aDt3oncHCyH15PmG2iNsvoKZat7SK4Kj8gj7fPCjU0pJ5bBl_kuexXjeiSGm6t5Chmens1azVC883TkV5GalD0gwH9H8lRb61Rl3lDUUqYaQiiv-ez0aAhtVwjGsCROIb5BQNUJJL8lsPE4uYussm1gQiMahtS3LkFL8CbKigmTBcbO9KuuKiwpkWPNG3x48QYWmIKjc3M3lel3mbjKafHN9xbJYd4KLU_8IVx9AtgWr1asIgTuVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f92631e03a.mp4?token=dpTTdA-pJNhrNpf30PBLbK6KDSvD3Lj65ClCrUrUi0obGEQOkO8tuOu33fKvJ_qjw0K2htTFv-8loK3Gw5ZsKuHy6us7WyBg1aDt3oncHCyH15PmG2iNsvoKZat7SK4Kj8gj7fPCjU0pJ5bBl_kuexXjeiSGm6t5Chmens1azVC883TkV5GalD0gwH9H8lRb61Rl3lDUUqYaQiiv-ez0aAhtVwjGsCROIb5BQNUJJL8lsPE4uYussm1gQiMahtS3LkFL8CbKigmTBcbO9KuuKiwpkWPNG3x48QYWmIKjc3M3lel3mbjKafHN9xbJYd4KLU_8IVx9AtgWr1asIgTuVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هریسون، پژوهشگر ارشد موسسه خاورمیانه: بعد از پایان جنگ، ایران نه‌تنها ضعیف نشده بلکه اهرم‌های بیشتری به‌دست آورده و دست بالا را دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661320" target="_blank">📅 10:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
استارلینک رسماً وارد عراق شد
!
🔹
دولت عراق به‌طور رسمی مجوز فعالیت استارلینک را صادر کرد تا سرویس اینترنت ماهواره‌ای اسپیس‌ایکس بتواند خدمات خود را در این کشور ارائه دهد.
🔹
مقام‌های عراقی این تصمیم را گامی مهم برای توسعه زیرساخت دیجیتال، گسترش اینترنت پرسرعت و پوشش مناطق محروم و دورافتاده عنوان کرده‌اند؛ مناطقی که هنوز دسترسی مناسبی به شبکه‌های ثابت و فیبر نوری ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661319" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617e009c2f.mp4?token=KUMS_dtSN9Eh1dKugqTlwln4HBfZJdA3LX4wf4wFSHuqYTo1Xsc7u2QwP3ROQvxbpooL14Hdb244z0t6KAB8t_jn7HecdYeeqijEK63KNBusDS2Iu1NC7HWN2C4wPv0E2LtDLXJJm1Aj9m_kAeFmVPaPD8LTimJVN7GZkVFM-rXqRjgDH0rfOIlbC2GUvREj4HODlR83JFfMBB4vo7AmQDXoUnXREbg38xqwnWwwm1156ijYZloTvgVcao6rAjgrir_9q6VZ4TgPmhQQGIuucyzbWqX_Tg0D_k_dXffy6UDjAunGnj8LpFsv-B4I9WAkQw8qDV0X-AM_bGz95hNskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617e009c2f.mp4?token=KUMS_dtSN9Eh1dKugqTlwln4HBfZJdA3LX4wf4wFSHuqYTo1Xsc7u2QwP3ROQvxbpooL14Hdb244z0t6KAB8t_jn7HecdYeeqijEK63KNBusDS2Iu1NC7HWN2C4wPv0E2LtDLXJJm1Aj9m_kAeFmVPaPD8LTimJVN7GZkVFM-rXqRjgDH0rfOIlbC2GUvREj4HODlR83JFfMBB4vo7AmQDXoUnXREbg38xqwnWwwm1156ijYZloTvgVcao6rAjgrir_9q6VZ4TgPmhQQGIuucyzbWqX_Tg0D_k_dXffy6UDjAunGnj8LpFsv-B4I9WAkQw8qDV0X-AM_bGz95hNskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی متفاوت از نمای جنوب غربی کوه دماوند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661318" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9388f2d36a.mp4?token=lUCw1fXVE9iaPb0rTTFpt2mhVZT16S71b4auGEYM4lgeK-4VAJQRB81kTDFO7lZWBYizp9aQwlRvWLk4k26hXxvKqrbzkIxkoeqlE-KwO1eFPIPavpVOiBjz6BoAw9Ja-0J8Vaam5CJTTd8UYWGKbK3FmVpWFJd1lwwziHQXvLW9mjZB2_mCWIw2YRB0DoGg3O2b1KCmN_LDVc360IG3L-JvzXMmacA6IQhGzlzuOaqYLrU1oIRJz5YG4L5uzzjwSX3KyEpRKcDSYR6UdKSRqdOJNqIm_GOIW4K387j7MFpgMKiXa-TluTy0QIkjC3yBLqmq-IDltw25qHZW69V1Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9388f2d36a.mp4?token=lUCw1fXVE9iaPb0rTTFpt2mhVZT16S71b4auGEYM4lgeK-4VAJQRB81kTDFO7lZWBYizp9aQwlRvWLk4k26hXxvKqrbzkIxkoeqlE-KwO1eFPIPavpVOiBjz6BoAw9Ja-0J8Vaam5CJTTd8UYWGKbK3FmVpWFJd1lwwziHQXvLW9mjZB2_mCWIw2YRB0DoGg3O2b1KCmN_LDVc360IG3L-JvzXMmacA6IQhGzlzuOaqYLrU1oIRJz5YG4L5uzzjwSX3KyEpRKcDSYR6UdKSRqdOJNqIm_GOIW4K387j7MFpgMKiXa-TluTy0QIkjC3yBLqmq-IDltw25qHZW69V1Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصل گیلاسه این دسر فرانسوی رو از دست نده
🍰
چیا میخوایم؟
🔹
گیلاس حدود ۴۰۰ گرم
🔹
تخم مرغ ۴ عدد
🔹
آرد سفید نصف لیوان
🔹
شیر نصف لیوان
🔹
خامه نصف لیوان
🔹
شکر یک لیوان
🔹
وانیل یک ق چ‌
🔹
بیکینگ پودر یک ق چ
🔹
کره برای چرب کردن کف ظرف به مقدار لازم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661317" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e5bf166b.mp4?token=YkFPyLntNNkT8EM8PIVzY3EU2IYfKh--mcFtklnSQGrQoyB0jBISVTGaFDxLklUI30YmKY2wn2UHzqd2aTdHOav5QPiQFiNGa8CaYf5qvJ5CFA_LxFuaowRv0Lq-e5FW4eEeA4Le8a3lzkbs9u8DIxrneYiRIGhKtGZpsZ05zYiwYYjwgW_qP1XHOoK-362MSRCjlvtu038R89xhfuC5c-11CyKPZjSf8eJwM4Qm_jhq2Ew2qW3Jnm2Yl0gesaanqWT_2s2WAO-5ckG18lTprpUWPjMFj3Jt5nnn_D3T5Hi9vAldQkKJgdK1waB_PLetGY6bHHqmLfSu8TAp2Ey82JJ-WEgyF0rwbJmZD6yk2C4rGfQfRmjGwq6GhreqkZ2pCAOI_yzEylQGj3xER4NCgoWsXGYpqYhbPi6pONm_HLUPS4V0MHCAAy0ZWQz_uOCAOz9pYw5dwte0rNNQrsPFwz82JDsUOeylq9lg7ZvuqMV8jdoIzv1Csj0Hgyo4YMKIZZM2qK7NInF_tUqovJksr5P_hHraWqRZv8mnSEyOUJWRMcc_E1fn9BKjK41zi8zIZh8irO4BT4gUdz4YOkBwTSy8E-5dciGTiUj5BYefV0Odnp74xJsfSu2L8QlHA5fCk1opHzfp22yxvRgilHuEY2umqrIwBvhUemmvevOoHD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e5bf166b.mp4?token=YkFPyLntNNkT8EM8PIVzY3EU2IYfKh--mcFtklnSQGrQoyB0jBISVTGaFDxLklUI30YmKY2wn2UHzqd2aTdHOav5QPiQFiNGa8CaYf5qvJ5CFA_LxFuaowRv0Lq-e5FW4eEeA4Le8a3lzkbs9u8DIxrneYiRIGhKtGZpsZ05zYiwYYjwgW_qP1XHOoK-362MSRCjlvtu038R89xhfuC5c-11CyKPZjSf8eJwM4Qm_jhq2Ew2qW3Jnm2Yl0gesaanqWT_2s2WAO-5ckG18lTprpUWPjMFj3Jt5nnn_D3T5Hi9vAldQkKJgdK1waB_PLetGY6bHHqmLfSu8TAp2Ey82JJ-WEgyF0rwbJmZD6yk2C4rGfQfRmjGwq6GhreqkZ2pCAOI_yzEylQGj3xER4NCgoWsXGYpqYhbPi6pONm_HLUPS4V0MHCAAy0ZWQz_uOCAOz9pYw5dwte0rNNQrsPFwz82JDsUOeylq9lg7ZvuqMV8jdoIzv1Csj0Hgyo4YMKIZZM2qK7NInF_tUqovJksr5P_hHraWqRZv8mnSEyOUJWRMcc_E1fn9BKjK41zi8zIZh8irO4BT4gUdz4YOkBwTSy8E-5dciGTiUj5BYefV0Odnp74xJsfSu2L8QlHA5fCk1opHzfp22yxvRgilHuEY2umqrIwBvhUemmvevOoHD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس یادگاری مکزیکی حامی فلسطین با پرچم ایران و لباس تیم ملی
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661315" target="_blank">📅 10:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آیا پیام رهبرانقلاب در باره تفاهم نامه به معنی بی اعتمادی به مسئولان کشور در باره مذاکره با امریکاست؟
🔹
پیام رهبر انقلاب درباره تفاهم‌نامه، نشان داد مجوز امضای آن «مشروط» بوده و ایشان بر روند امور تسلط کامل دارند.
🔹
این پیام به معنای بی‌اعتمادی به مسئولان نیست؛ رهبری از «حسن نظر» مسئولان یاد کرده و بی‌اعتمادی را متوجه طرف آمریکایی دانسته‌اند.
🔹
همچنین این پیام، دوگانه‌سازی «عین نظر رهبری» یا «تحمیل به رهبری» را رد کرد و ابزار فشار بر مذاکره‌کنندگان ایرانی را از آمریکا گرفت./ فرهیختگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661314" target="_blank">📅 10:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
امتحانات نهایی پایه‌های یازدهم و دوازدهم به ۲۰ تیر موکول شد
🔹
رسانه عبری: ممکن است بدون هیچ امتیازی مجبور به خروج از لبنان شویم
🔹
کلید سوالات آزمون سمپاد تا فردا منتشر می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/661313" target="_blank">📅 10:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmvqS9n9ykTI9ZI-k27WcHtiwzd6MmHqyedqiWKN7A7wbfcfgsyYW0vt6BJRc-frBTFiRsZM4wO69HDZ1NE9mIuSvv4JHgauJ7sThTPGTeOlh0b8jiq1YKOWmwOWldQCwJk13bvBMhl6AC7oxmKdgQOWBeHJV1z7ViIL_1zis_YjgxGXrxWOUUU-38Jk9bo8fdTzTbgUYIY-muBpW5V_65k1ZltH7eaHlyJINQnPxTQAmP6AW_ln0OweG0NPkqCvkxOL-IvY3j57r2BxxmWl2g0ZRaekJywr4gLx0YghMP8246iuXSyb6qquFeyo-pf2vYx6KXwOOx7RlrA0GlHtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکر کارلسون، روزنامه‌نگار امریکایی: ترامپ فهمیده است برای موفقیت توافق با ایران باید نتانیاهو و اسرائیل را تضعیف کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661312" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/661311" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cdf2cf0ab.mp4?token=rbx5L9DOY_c7PniIMbC2sNn20zJsiaWmLtB6AQ58EToHUydsFrazk7A93ZDmh3Dw8whgorTEoPuMX7nKJRKOF-IfEb4NDmsZlc4yOq2Gskj1eylK4LVzPPAmPMKrR3AivDLmgwCYUdE8MNZVb9ZekwAhYhWdwBlcoW1IDzWev0MOm6uuYPEU03bm5allmuNJP3vM7v8Ka59WLwX9MRcU0cDQHGqW11_ORprBL_PqpXOfDwKO2lMdYosh6zVDGDhhA4BYPbeD6J01flS-x-Tk_xwM-xlxFU7pj4qb6AsIfwLjtkcc6WptLYLWNjIE4UcUz1yHJe7rjegUiRumrmc2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cdf2cf0ab.mp4?token=rbx5L9DOY_c7PniIMbC2sNn20zJsiaWmLtB6AQ58EToHUydsFrazk7A93ZDmh3Dw8whgorTEoPuMX7nKJRKOF-IfEb4NDmsZlc4yOq2Gskj1eylK4LVzPPAmPMKrR3AivDLmgwCYUdE8MNZVb9ZekwAhYhWdwBlcoW1IDzWev0MOm6uuYPEU03bm5allmuNJP3vM7v8Ka59WLwX9MRcU0cDQHGqW11_ORprBL_PqpXOfDwKO2lMdYosh6zVDGDhhA4BYPbeD6J01flS-x-Tk_xwM-xlxFU7pj4qb6AsIfwLjtkcc6WptLYLWNjIE4UcUz1yHJe7rjegUiRumrmc2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در جمهوری دومینیکن
🔹
آتش‌سوزی گسترده در هتلی ساحلی در جمهوری دومینیکن منجر به مرگ یک گردشگر ایتالیایی ۴۶ ساله و تخلیه ۱۷۰۰ تن دیگر شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/661310" target="_blank">📅 10:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvrIA12Xvv9r-NIf9eYVKN2a6m7e3V73D7VtfLo09SJGhmBGHr1xvRmbstl8FFsdCyc3yPa5KGxx8Ri4cRjhWB_nWMAIjg46dya939IcyIJ4FQ-1MY2I48brOjm0yuvpZkFtClnlvonHAz2P-FbCEAC69VlSUo46sbY-mToHjfM-xIKBJNmbS4jnti_TBdw7FzRyv5b8NKGb-tu7VlArk4jQdLgXg6899Y1d417XXCqVgR5WXbpzOuETWQW-XWQKMwkUl6RZfwZ4gsGQdF-WN532WER0qgVJVpAQxOH7SAqSBgmQRU9WdNUqRHDpx3vps3-W5ZgdKLL9ssRwCc_h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارایی‌های مسدود شده ایران کجاست و چقدر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/661309" target="_blank">📅 10:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سخنگوی دولت: پشت هر دستاورد دیپلماتیک، سال‌ها مقاومت، ایستادگی، تلاش و مجاهدت نهفته است
🔹
این تفاهم به معنای عقب‌نشینی از اصول، ابزارهای دفاعی و منافع ملی نیست، بلکه تلاشی برای تبدیل جنگ سخت به نبرد سیاسی با مدیریت عقلانی منافع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/661308" target="_blank">📅 10:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bdcc6dd0.mp4?token=vzCFFeRWLJFOrb34wrwrP8gNNDPRDC9aq2V7KebNyOpaoivex4l5hDA_oFLtuPz9i4Il77BXU05VxKKu4apMQULRTvAan8Cv120Eu1YAGwhKQNnJzpqP3aZ-mBMBi-ieffjLpDevKFbaRjtrU83tKkjAFIC5f3jdF8QP5YR4xcpV3LA3I0qmG5eGtEgbKYgYIXRWeG-6Qqtod52vUmBHdOU822UrlVMFDb3UfB6Er75oBr1dIFa_beqNgxI-Wn3o6D5BMt3yQwTnE38TaXrrocHOFdchk8LpVXxcP_YqvQzw7PH0aGewTaa98djdMbxXwPBUzVVjz-yIpKhdf-wWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bdcc6dd0.mp4?token=vzCFFeRWLJFOrb34wrwrP8gNNDPRDC9aq2V7KebNyOpaoivex4l5hDA_oFLtuPz9i4Il77BXU05VxKKu4apMQULRTvAan8Cv120Eu1YAGwhKQNnJzpqP3aZ-mBMBi-ieffjLpDevKFbaRjtrU83tKkjAFIC5f3jdF8QP5YR4xcpV3LA3I0qmG5eGtEgbKYgYIXRWeG-6Qqtod52vUmBHdOU822UrlVMFDb3UfB6Er75oBr1dIFa_beqNgxI-Wn3o6D5BMt3yQwTnE38TaXrrocHOFdchk8LpVXxcP_YqvQzw7PH0aGewTaa98djdMbxXwPBUzVVjz-yIpKhdf-wWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی بیش از حد فکر می‌کنی، فقط ذهنت خسته نمی‌شه؛ بدنت هم هزینه می‌ده‌ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/661307" target="_blank">📅 10:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سیاوش قمیشی در سفرها با خودش قرآن می‌برد
امیر قمیشی، تهیه‌کننده و برنامه‌ساز تلویزیون:
🔹
با وجود اختلاف‌نظرهای سیاسی، سیاوش قمیشی به عقاید او احترام می‌گذارد و پس از شنیدن خبر فوت برادرش فقط گریه کرد.
🔹
به گفته همسر سیاوش قمیشی، او در هر سفر، قرآنی به یادگار مانده از مادرش را همراه خود می‌برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661306" target="_blank">📅 09:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/493c1602e1.mp4?token=AzZg-ntJANz06iKgY7mCc71seGQcwsjnx28r4QgS7M-eyJmrAD_VtF5cMDYiF0awTgFVDy7WAJReFfa4Va2pxx9ORq0FMDDnE3srd6LM3JBvlCONmQrBuEuT7iV7sdHAYHJ559wSkR4EuYgVV5iDcNw1-fmaLWEZWXcdHdLsah_3yUJspbHsD3TRLnw_vFJ0BbCqIu5-RBZlOsW2XklbHDQ1l_pTyPaZIvn_ni1JJbk-zvKMcLypmg5JPLoiW6cL0JUaH5c-7exINoisCuP2psZo2xVmzBMepZTjiCisl36U0noeJaqG1xdWY3ZriEr3Da_Nd-k-_hABGwC343HdOanDV4iyCPXtoDH_Ku3plXrt1dmOnRCX27Zo3GGfai3JQlMg5L5_2laNKMc32TEIm49p80Cknr0S06HE9U9gXELP8MSilyx_PkDiaJmWhBNQsqw-5ZNbA31_eCQZppPNsAo6Ct5OUclrg1Odp8uQeWaQd4IXVzQW2QPdnZbmMqmhspg6SXQ4Pwas8sho353jSljOy8TR0833EqLgEBLbmj5u3DDNanBmi8M4g20Y_i65Sd33cBm2hmV4H1JDIm1kcwHmMf8rJHWOG1argiBwbsZOlEwWAHJ1fgcKRfciAUEBeUcIYN7DCeHsr8SlK-388DG9Jc82_kdjp7e-in9hGC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/493c1602e1.mp4?token=AzZg-ntJANz06iKgY7mCc71seGQcwsjnx28r4QgS7M-eyJmrAD_VtF5cMDYiF0awTgFVDy7WAJReFfa4Va2pxx9ORq0FMDDnE3srd6LM3JBvlCONmQrBuEuT7iV7sdHAYHJ559wSkR4EuYgVV5iDcNw1-fmaLWEZWXcdHdLsah_3yUJspbHsD3TRLnw_vFJ0BbCqIu5-RBZlOsW2XklbHDQ1l_pTyPaZIvn_ni1JJbk-zvKMcLypmg5JPLoiW6cL0JUaH5c-7exINoisCuP2psZo2xVmzBMepZTjiCisl36U0noeJaqG1xdWY3ZriEr3Da_Nd-k-_hABGwC343HdOanDV4iyCPXtoDH_Ku3plXrt1dmOnRCX27Zo3GGfai3JQlMg5L5_2laNKMc32TEIm49p80Cknr0S06HE9U9gXELP8MSilyx_PkDiaJmWhBNQsqw-5ZNbA31_eCQZppPNsAo6Ct5OUclrg1Odp8uQeWaQd4IXVzQW2QPdnZbmMqmhspg6SXQ4Pwas8sho353jSljOy8TR0833EqLgEBLbmj5u3DDNanBmi8M4g20Y_i65Sd33cBm2hmV4H1JDIm1kcwHmMf8rJHWOG1argiBwbsZOlEwWAHJ1fgcKRfciAUEBeUcIYN7DCeHsr8SlK-388DG9Jc82_kdjp7e-in9hGC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان‌های شدید شمال مکزیک را درنوردید
🔹
این طوفان‌ها باعث جاری شدن سیل گسترده و خسارات قابل توجه به اموال در منطقه شهری مونتری در شمال مکزیک شد که منجر به مرگ یک نفر و اختلال در خدمات رسانی در چندین منطقه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661304" target="_blank">📅 09:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeYZkFSWFMRT3Q3s9e-D6C9EdrNrxwSuBRqMtXwYV2XkNxBd3Vg_m7dlg4V3N0HKgl7qWAcucrT3O_2P6jQCxKLZnPrn4Mc9cqmPiE7DXvr2qIyRKmPTuHH7qQIcJgZYDhaBfbWnXdeySROu3Uq8G-o55tqkwxcjx-S11pJkhf4sFRr98tgQWqkJl1xhauYqjrqvki1vgzj2GomlYv-MtDfqWuHfKVheaGvyxFK3eRXWjy0TgNafw7nCop_vDL9VJ7SXnbiMiCXbThBCwJnURrDMN1DoTzcq7VoXPo4wktHKCSoSD1Bpohla0hVartmWAX4dCUq6P8MojYLzwvnVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKsuuix8mDRIQdByQCo3-eM95dITDFLdc6kdDccdz0igps8C_jprkC602QD1HOTJ3Z5y9p9x06L-FkHemXjjqOCR8l2Pzj2aPoxvHpMul5fDN-YCWHUCDLGnTeOV4K3I_DKXqK_ibY8DTCd0qDmjZqCVpHdSQDzh6nNPLSiIRnLSxf7cIirR1XVGfXTQow4kpKZ6h3k-VKHlQStAn7SQ0PmRzHux5Q1GaEPFjlCyjINDD_cnPKOMU-iaQurnD0TZaPUJk5VlVXRwVE0OL6IjW4eVPmZA1H4FamqrdbfjNT5Hb0IfRIQWACcJ8gN1_uXwT7OwjyvUPsp93HUzTNkuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwtGCTw3UewiYsTuLKrIBTfM8pfSMjKDJiBkiNwVO7BpzKjaxi29z1ikNtCDHhPdERSC3SnBI7nbVLrcwwwZXABGxKU6AZWprcTLL-sqxsJSzfoUzGzOxu5ixdxbwjxMPUrs-IG9YgDayZkthAYWNQy4bG0eeR7vj4yTwRzGftGO09gFBAfi1N5e45f6rhAA4BRxFJoPWkcBFrTtimaPT0xPEF8sGfZhV92dYVgrC4MNN3GUqxRU-FHjs2dYUZUxCKvZ2g_LzF1lqf3-lzXVwamIz0fvUFhKdBzGbTQ4wjlOMf3C1gM-e4j5nKoqh1NV9X-RqUSf0C3gwi53f1O36A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از بمباران‌های وحشیانه و پیاپی رژیم صهیونیستی در جنوب لبنان از صبح امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661301" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تصویر منتشر شده توسط کانال دوازده رژیم صهیونیستی از حمله این رژیم به شهر کفار رومان در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/661300" target="_blank">📅 09:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_RAFIx25JJl9a4UPQPjVu_YwaeZ5rll0S_9nVv8fJq3RJo3tLoImH_vNAKFKinlkiqBuB4VXzBsK-OfXK9aQiAQcBrvevVnWD_pPTbcWSWGtpkQtzJIjbzO8wiY8pmrlnpep9HOn4XYJaYMK0Tr6DvumHdjuIEjBYa9jLsuxe1kBc03IP9hq6B54U4un-ACUai3PblN4qvzrTb4LEybRp69_XGLm6sy7D1rZUOO39JL35yxysCsL6fptOm62RTGY7x0Ezh9MeZcrmzRNDVwyZUDisi3cA8ZS21g0rD30R87Ca7V9hLyEDf1Qrfe9lGHvGgIwRxpjBR93UyNxrrL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با تصمیم مدیران پرسپولیس، قرار است دراگان اسکوچیچ جانشین اوسمار روی نیمکت سرخپوشان پایتخت شود
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/661299" target="_blank">📅 09:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJkvi-vaocKrFjjW9ZGZlFzDYxu6cbvTTMO73upw0T8LA2ET5f02A9AysydyozjZJfFcrWslZyWfwQg33Bxp-uiJIf5gP8Xv2u6UZWnUtSmYO3552htEEzCDA5AYXAnDnIxfYgSbRdocqDn8F9eOl4S3MDfh7AWx4pfV30MF0JqsqOsyUby1hu4lZef0TllwbAu9cjVhdb9EHsok50z3iz5mHKFcmVe95E4O7whyRs6GpnRK0eCe5KwZ8iz6LSuxzx5beXKVlcQ_wBYEFcNePCj4j5T60TlYPXhASejgXQAK49CkSE_U5RBPNTPmw3sKKyb1be5unc7b52JIckmskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از حملات هوایی رژیم صهیونیستی به شهر نبطیه و شهرک نبطیه فوقا در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/661298" target="_blank">📅 09:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
معاریو: توافق، ایران را به قوی‌ترین قدرت منطقه‌ای تبدیل می‌کند
روزنامه عبری معاریو:
🔹
این هفته شاهد تغییر در توازن استراتژیک قدرت در خاورمیانه بودیم. اسرائیل که تاکنون مثلا «قوی‌ترین» قدرت منطقه‌ای بود، توانایی خود را برای نفوذ و شکل‌دهی به خاورمیانه از دست داده است.
🔹
توافق ایران و آمریکا، ایران را به قوی‌ترین و تأثیرگذارترین قدرت منطقه‌ای در خاورمیانه تبدیل می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/661297" target="_blank">📅 09:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
شکایت ایران به فیفا از محدودیت‌های سفر در جام جهانی  فدراسیون فوتبال ایران:
🔹
درخواست ورود تیم ملی به آمریکا دو روز قبل از بازی با بلژیک از سوی میزبان پذیرفته نشده و این موضوع روند آماده‌سازی تیم را مختل کرده است؛ به همین دلیل ایران به فیفا شکایت کرده است.…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/661296" target="_blank">📅 09:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تصاویری از حملات هوایی رژیم صهیونیستی به شهر نبطیه و شهرک نبطیه فوقا در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661295" target="_blank">📅 09:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
لهستان عالی‌ترین نشان افتخار خود را از زلنسکی پس گرفت
رئیس‌جمهور لهستان:
🔹
این تصمیم در واکنش به نامگذاری یکی از واحدهای ویژه ارتش اوکراین به نام «ارتش شورشی اوکراین» (UPA) اتخاذ شده است. این گروه در لهستان به مشارکت در کشتار ده‌ها هزار غیرنظامی لهستانی طی سال‌های ۱۹۴۳ تا ۱۹۴۵ متهم است.
🔹
نشان عقاب سفید در سال ۲۰۲۳ از سوی رئیس‌جمهور وقت لهستان به زلنسکی اعطا شده بود و لغو آن نشانه‌ای از افزایش تنش میان دو کشور بر سر مسائل تاریخی تلقی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661294" target="_blank">📅 09:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1dhDCvfmfN2xutTLGY10zpU9VW6xI-MH-g-VoyOPHELGERqFThJbKnDos_rEmwVxKQWFG4kULsawKIVZLeVtT9khBVKc4eCQD7ojKuQLs4NusZdyFOLbgEEoUbP7B1oBCUcCLox7dKl5R5wM5L5DsS3JWbC3IgyIGPbiEalEgNz7xjWcBXx2XMOtHYNrUQ-uK5EpHF2xikWvlB205gA8-PbZISlMNrfrAFLEzu3fRM4laLaG9-19f2ZQiWpZd8kiIyPu11NbH4tjTEHK9LHBQsytCWqmVhenOI9G4StvBQkPDi6cSsO1dgE0yagf6oCXdDMPI0WtVdGYDwmfmTATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tgwv39In_nQ1q2YEoBxvLhzC76lytgdf97GJ2z3WYeN3inKwkr9B4GbNI6v6teL2krbbQCS6-_KtS6e3L9rrSEPA7qOyY-GNulnYzQzqi4NybGftpH_VVZSiId5t1IgXFWu_tJSkSmnK0qTp4OL_sAAl6hzKNa_VZUrSJyXe0oF4V8wg1Rr8g1-CsQAHZc1MByGwSDTrLN6BEmq7Ug3lVgwsYJzA6G9OQunaogEjaBpl6YtVNRVP-YKaGkq06lzUktB6c3qLZI6v6Mx7LbOnPTpYtzbRygbcYwQvZO69_jUtJxsUuymYjk2sWWJGgdbILBfw5H7b7KxnFNKP7jW5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkTX34mnewgRMWKdXHjT3YlyrhGHIfamreVQsaxCpMmBKwRCQlXkrXhSez4roObky8i2khUzje0C2-hlw8j890iBALJEpPI-NMmto-l48yO0z5N7K82QlKoJa1uzsnuikCPyHvpp9l-WoJyVqxvRCjXrKf6D9ZE9XdJvqr_XICrNhwkt3c4ABnmKy08V7Nb9D5_d0kNgyLO8NAW7_hJ72RhSTMLQ_kR06vgeCX0QtTmBjrtYVkj6E7tLgQ1a-Yw8fkTpK93cCXm3Vluu2pTHpm2jd8xj2aAuHtEHqn83JmA_Kiz8100PZDn5p_D3cnSCl1VLxGTktS_g7FQSGW1vUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از خبرگزاری لبنان (NNA): جنگنده‌ها و پهپادهای رژیم صهیونیستی از شب گذشته تا صبح امروز حملاتی را در منطقه النبطیه انجام دادند و ساختمان‌های مسکونی و خانه‌ها را ویران کردند، در حالی که توپخانه اسرائیل قبل از سپیده دم النبطیه و حومه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/661291" target="_blank">📅 09:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaDj9T6ibSFqlxd0rvGayLk8zSx1AoUmnO0gqv_iv_jgfOGJVg-D9KlDOPPWQApN8dqiEuUPv4o9XJ0YofvjdpuQnMhQmZVKepe5Ft-kTpIsgmk8TqVVefpcI-1t1kQamPf_dvu87hJhylpENBuurYq10GSH0BSQ-RfmWZVNOk1aYEiFvBC7mxpMvakY46joGMTf9PruBd0ebS-_WB3RPkK1dY7zBQooNKQyfsu-NJOYJnPyLOS1NkEaTobbrqBos-zH0phXpTbl5bjtdRBgJ1R_nau0ktgpqD-qr2WYL5J7HqfZWrsGskDte5RI5tfG4V83WzlMdt5SmBDrVREF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس تهران ۸۹ هزار واحد مثبت شد و به تراز ۵ میلیون و ۲۴۰ هزار واحد صعود کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/661290" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مرز سومار به جمع مرز‌های اربعینی اضافه می‌شود
استاندار کرمانشاه:
🔹
با پیگیری‌های انجام‌شده و هماهنگی با ستاد مرکزی اربعین، این مرز به جمع مرز‌های مسافری کشور اضافه می‌شود.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/661289" target="_blank">📅 09:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihMsdZP6Ry-wac7H9Q5ziHJCPN9WyX32E4K48zqZVDx3ZPj5BNYIsA1q507PpM8I4h8WhKygkQs2SuzUY66JxFLAAXkV7WshbGThW53CaBOHyrN__zJ6WJEkUaQQB1W7qpYHELczHcNEzNzWItnVEY3_L8a2gVPFooV_d9b-q7Ur6M8X1Z-DKuE1YaC-uw7Eldzjp_3juLMFb5ZC2J8xPKnQUQREnwJ4YjCfDeu3zkBQr5HB_8jcafSRj9-tk4R9nHaj6yr4tvK_mFvScfm9NQbogN3RMNyKMrFKSNAuP8vpLLyyDeKchh_xNmuHTxKeqdpxPU2BufeeEt5LDUPuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: نارضایتی رهبران خارجی از رفتارهای ترامپ افزایش یافته است
🔹
جورجیا مِلونی، نخست‌وزیر ایتالیا، به ادعای دونالد ترامپ مبنی بر اینکه او برای گرفتن عکس مشترک «التماس کرده بود» واکنشی فراتر از یک تکذیب ساده نشان داد و با انتشار ویدئویی در شبکه اجتماعی ایکس، به انتقاد از رویکرد رئیس‌جمهور آمریکا در قبال متحدان غربی پرداخت.
🔹
واکنش مِلونی تنها یک اختلاف شخصی بر سر یک ادعای جنجالی نیست، بلکه نشانه‌ای از نارضایتی گسترده‌تر نسبت به شیوه برخورد ترامپ با متحدان سنتی آمریکا است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661288" target="_blank">📅 09:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
خبرنگار الجزیره از حمله هوایی رژیم صهیونیستی به شهرهای کفر رومان و شوکین در جنوب لبنان خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/661287" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_eyKrKZWIDTLW_Lscs_hd6PqZPNpZGv3QZBHjEVWW7yxjg-vRxtpxqevHA3nvhdOlJciRJAsdpTcWTqAxrOrsOCfL1pkG_DnXelKr76oHvWEbpA40L1UDtGEA4-xO0Y-SYD9ZgrXir2QEab1yFowrlx3iuu3-1oBr3kfQyTUj0un0fN-w9eFDAM3D8sH0GioHY9ZcArr03JWM6VQ1zIs2nT1zthR-cZo5obOBgUOYvrqL77jBTKnvkXrz_Q_zP0gd635l1KXH3O4tgQPZZq5qaoMP-zT5JE5WYkN6SuHNEP4n0rEZbKQL5b4atE2xJ91RAO2SbZXnTzYdwE73npqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: آمریکا همچنان اراده‌ای بر جلب اعتماد ملت ایران ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/661286" target="_blank">📅 09:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
قائم‌پناه: دارایی‌های بلوکه‌شده ایران به صورت کامل و تدریجی آزاد می‌شود
معاون اجرایی رئیس‌جمهور:
🔹
۲۵ میلیارد دلار از دارایی‌های بلوکه شده ایران به صورت کامل و البته تدریجی آزاد خواهد شد و از آن به عنوان منبعی برای توسعه زیرساخت‌ها استفاده خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/661285" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
احتمال شنیده‌ شدن صدای انفجار کنترل شده در محدوده‌ جنوب اصفهان
سپاه صاحب الزمان استان اصفهان:
🔹
احتمال شنیده‌ شدن صدای انفجار کنترل شده در محدوده‌ جنوب اصفهان وجود دارد.
🔹
این انفجارها امروز از ساعت ۸ تا ۱۴ انجام می‌شود.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/661284" target="_blank">📅 08:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920b1127f5.mp4?token=v8_O7SaRAONGl_5oqfp74Pc1ikUNNOvQhdEeF7aPah3HZQ-gvwYUYwN78q3SHVCCq7qZPW7EY88UVx46TxuUWFBf_LeAj1KZSS0806XCy_cTJcrEjEtWBxOVfEpIcSnE7jn-Zr1RNQGqR0hDt28psj6mvZgevenmiUppuSdRs0jLmOMT-3XLXkFsNs0LuQcd5NJ4KQGEm9C1FUrLGD-g4u7Rkx5j19rFTPXTu1tDyKGQDTjUxf0_AxeTJCxi0BtDuwTRmFdqOShOzO43UdcXfIVtup3p7b2KZk6fpcqObiW9A8gn7YZ-BA5iHQNhYXUqB-b4mkaRV7JFf9zoFgCb6Bk3Wli2n4GBEUhes17rGhW_AMmFCwzqpe5ALBavLLTHv3yRAjhHv4Nu5g40tcns4HkGVWetXVtoexM84eahieVunDFVUzPAdoCM4rZrq6gj0dFl6vWKmGghuU3Q-fKnfViqU3AIwpQkFzV-JU9l4JugTljlg8C-S0zN6d6Sg1ZCpI7pu89sGA6jnVFbXbdsW5f0frtKzp9VNNWsG-CNEECKCsch89P2MnPeHYu0pE1GjuVFoAq43DZvkvvGbeBeN_nrzBxD4P4ka2RNCBjy2yY_QoXwLxe3GC3imyNMZiLGDkVqsTMY4VMY7uB-PX3yScO-kq7OX_yb9qCS1hc6WR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920b1127f5.mp4?token=v8_O7SaRAONGl_5oqfp74Pc1ikUNNOvQhdEeF7aPah3HZQ-gvwYUYwN78q3SHVCCq7qZPW7EY88UVx46TxuUWFBf_LeAj1KZSS0806XCy_cTJcrEjEtWBxOVfEpIcSnE7jn-Zr1RNQGqR0hDt28psj6mvZgevenmiUppuSdRs0jLmOMT-3XLXkFsNs0LuQcd5NJ4KQGEm9C1FUrLGD-g4u7Rkx5j19rFTPXTu1tDyKGQDTjUxf0_AxeTJCxi0BtDuwTRmFdqOShOzO43UdcXfIVtup3p7b2KZk6fpcqObiW9A8gn7YZ-BA5iHQNhYXUqB-b4mkaRV7JFf9zoFgCb6Bk3Wli2n4GBEUhes17rGhW_AMmFCwzqpe5ALBavLLTHv3yRAjhHv4Nu5g40tcns4HkGVWetXVtoexM84eahieVunDFVUzPAdoCM4rZrq6gj0dFl6vWKmGghuU3Q-fKnfViqU3AIwpQkFzV-JU9l4JugTljlg8C-S0zN6d6Sg1ZCpI7pu89sGA6jnVFbXbdsW5f0frtKzp9VNNWsG-CNEECKCsch89P2MnPeHYu0pE1GjuVFoAq43DZvkvvGbeBeN_nrzBxD4P4ka2RNCBjy2yY_QoXwLxe3GC3imyNMZiLGDkVqsTMY4VMY7uB-PX3yScO-kq7OX_yb9qCS1hc6WR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوت کوزه‌گری برای پخت یک کوکوسبزی مجلسی و بی‌نظیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/661283" target="_blank">📅 08:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
خبرنگار الجزیره از حمله هوایی رژیم صهیونیستی به شهرهای کفر رومان و شوکین در جنوب لبنان خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661282" target="_blank">📅 08:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl8ceEXXEnbkGdYrwekMhnV18uUqnUt2AjsvNaWezpzjaf9xlRTuifdOLJbvbGoLeK1qMzAGvDuf1WCBOt9F4iivcA29-r460FNUDsWz4eh0w07fDk5NaVUNvbJ3ppRzP9shvyp5sHKqoDV8tcUPdNVa4yygRP0pxgio8n7_e3XvpN3wVBr_I2mWxVU1WZVVoWBPBuSSCFObNMk7gS5fi1MedF-zbAI5sNpl5-yTSSqlh_Co3hRs50aFPFSVKvi5032rZJBEO7FGfzXjcNoL8jXgkBSKydvzukQtLnnobKjCC9-5GWqJkaSn9TeuBWvIsJIOZNdZgumuta1Pj9xHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاجعه بزرگ؛ سقوط یک امپراتوری!
🔹
سکانس پایانی امروز - حذف شوکه‌کننده ترکیه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/661281" target="_blank">📅 08:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab59f856.mp4?token=vicVtPCdxnzV1qNj17hvfc3nGhP_LKcrTA0Pek62VRI6I2f-N2GUZNhhBaOX2QXhiwC-BnnVcik3eDw-wcINnvNwnMRmec6nMl-wE3kXuITR5dsd_2jlfp-FXCckmJ1GKrKtdp_vB330Sh7hgErVX9KZjQEnis9-0ftk0ZUHgperHHOwKfCk8gMqFlYebkxldwqIQGr-STUhxOa9gu7Md__TI7Y0EH6H3-Za5Z2agorQ3GsuQoy0aPEWUQkP9gGckwzDDeMvJ10egZLTAZKIvYt2SU-xAnkeKoc3mB7UQSklsPb_ngYZan52Ybkhr615o7gHpxttuWdjBWUPUAc51A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab59f856.mp4?token=vicVtPCdxnzV1qNj17hvfc3nGhP_LKcrTA0Pek62VRI6I2f-N2GUZNhhBaOX2QXhiwC-BnnVcik3eDw-wcINnvNwnMRmec6nMl-wE3kXuITR5dsd_2jlfp-FXCckmJ1GKrKtdp_vB330Sh7hgErVX9KZjQEnis9-0ftk0ZUHgperHHOwKfCk8gMqFlYebkxldwqIQGr-STUhxOa9gu7Md__TI7Y0EH6H3-Za5Z2agorQ3GsuQoy0aPEWUQkP9gGckwzDDeMvJ10egZLTAZKIvYt2SU-xAnkeKoc3mB7UQSklsPb_ngYZan52Ybkhr615o7gHpxttuWdjBWUPUAc51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم برزیل به هائیتی توسط وینیسیوس ۳+۴۵
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661280" target="_blank">📅 08:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beccc0a7db.mp4?token=CTmNNz65OiP326NpB766mNQuRJKtwT2KEeCT9hufABr1hb-XoTMF2jv2Qk-RZLpzWmapaoN__6wNwolOGyYpI6wA197jfqXQkuInzd5GCPGWHZTqwkqvR8xKfMiD6-31LuZRruIcVEUvskafNthAAs_8Lg5I99S8ix_hr3NNSQ3YH_13zTql4a35lCXYZ0Sjcw4iakLQ7TYMDuUqDWUIe3hGwmCkhGoY1sBwlCNElxoXmsBm6lJChiGERe_FZObzFEXhD2-SzS44c0UJH2Xw7svgLTeiwQpDCVS84idIW-sjk703UvU_whPglxolRrL8UoEP_STzwRFFgqAjRie1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beccc0a7db.mp4?token=CTmNNz65OiP326NpB766mNQuRJKtwT2KEeCT9hufABr1hb-XoTMF2jv2Qk-RZLpzWmapaoN__6wNwolOGyYpI6wA197jfqXQkuInzd5GCPGWHZTqwkqvR8xKfMiD6-31LuZRruIcVEUvskafNthAAs_8Lg5I99S8ix_hr3NNSQ3YH_13zTql4a35lCXYZ0Sjcw4iakLQ7TYMDuUqDWUIe3hGwmCkhGoY1sBwlCNElxoXmsBm6lJChiGERe_FZObzFEXhD2-SzS44c0UJH2Xw7svgLTeiwQpDCVS84idIW-sjk703UvU_whPglxolRrL8UoEP_STzwRFFgqAjRie1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم برزیل به هائیتی توسط کونیا ۳۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661279" target="_blank">📅 08:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5qdSALyyfCkkbxnxCXYwwMUCkNNNggqtEqMOhcfk4BRD_MoFu5grAheusO8D4-T1Cov-bh2vKjwjhkYgwTn6RiMfGRH81ZmkeBfbc2uAXDFqMPVKdSP_d4poyL1YjakwzMExtTIqLaP3un_CxpT9DwfdiG3dqcbSNHU4_3l_tuao6K7cOj7rdf0PXCzw4iis6IjPNHUC0WfHpsx9EG3yhMBStyPayJTU5PoSxU7eFqn_meWsRO51_Ff9v98oeK2KoOe8sGAUBlELNJGegiitFqOM4g38OtuvAWx3j47o1bl_zHmO91Vi6VU_lojwqov3jW646Shd7F9l_nAiyuPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661278" target="_blank">📅 08:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/661277" target="_blank">📅 08:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه: پیشنهادهای خاص و عملی ما برای حل بحران ایران همچنان روی میز است.
🔹
روزنامه هاآرتص: نتانیاهو وارد «روزهای پایانی سیاسی» خود شده است.
🔹
پادشاه اردن: مشتاقانه منتظر توافقی پایدار بین واشنگتن و تهران هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/661276" target="_blank">📅 08:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596213382c.mp4?token=dAzkjVT74o41g5YZ0Y_R7ehBDo9QvP_IZIqV5N5eJl-7sSlzf8LnOhzeXCseQiK4UOprYWQjURC1DR3F026OtVWW_HB3EN6UWbuJYAZgbP2eCUdAm5HeFJF3RqlmHBhEHjNqSSiLIGngRv8CREEmYTUJRk3VCwjTF9Gvpcuu3YSJVlc6ftLx02wKnCKJlmlXUhuWacemfb-Jrr5Zvz1acdNw7YFrTP7TIj2H3jkaxmn1kgkV2fopZVwKbWBp5B2suYr-mWb7X5Nd8YoZAUPeAJ3g81J5GDa92bfIOPwZyIUHFWuSpjo1wU1DLHTv5U2qixg7Iu927XjUpRKTlIDTtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596213382c.mp4?token=dAzkjVT74o41g5YZ0Y_R7ehBDo9QvP_IZIqV5N5eJl-7sSlzf8LnOhzeXCseQiK4UOprYWQjURC1DR3F026OtVWW_HB3EN6UWbuJYAZgbP2eCUdAm5HeFJF3RqlmHBhEHjNqSSiLIGngRv8CREEmYTUJRk3VCwjTF9Gvpcuu3YSJVlc6ftLx02wKnCKJlmlXUhuWacemfb-Jrr5Zvz1acdNw7YFrTP7TIj2H3jkaxmn1kgkV2fopZVwKbWBp5B2suYr-mWb7X5Nd8YoZAUPeAJ3g81J5GDa92bfIOPwZyIUHFWuSpjo1wU1DLHTv5U2qixg7Iu927XjUpRKTlIDTtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول برزیل به هائیتی توسط کونیا ۲۳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661275" target="_blank">📅 08:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c44f88a.mp4?token=FPY4mkJJAXW60NnmvhJbpuPc6KIuJ39FO9NovfUyW71ogfS-lFlLFrYtXXp2R6sj00B8nq3qup-53u1z8Y30Bc7Magb1Jh2RU0XWT77G2SQvdoc4CjfWIWIZWm-tihdi3M_X2gbTBRY9A3UoG4hL_tAhNe94tzkLAW8Afj0vc4YjesZLzlYUjt-4VPe3f4JVEmJd8AxfoCH2dtu4S12i4sdnkWovI6ABC4N6gHPBDjoN9s-WIRwvhXyvDxTcpW1Ntg5EfECHyn8Mu4NX_gWfEuYScvLz-Uf82R_dzntipUCce08XCsxZ_MwADzRygewtU6kU_BZFsWILfdzA6_NWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c44f88a.mp4?token=FPY4mkJJAXW60NnmvhJbpuPc6KIuJ39FO9NovfUyW71ogfS-lFlLFrYtXXp2R6sj00B8nq3qup-53u1z8Y30Bc7Magb1Jh2RU0XWT77G2SQvdoc4CjfWIWIZWm-tihdi3M_X2gbTBRY9A3UoG4hL_tAhNe94tzkLAW8Afj0vc4YjesZLzlYUjt-4VPe3f4JVEmJd8AxfoCH2dtu4S12i4sdnkWovI6ABC4N6gHPBDjoN9s-WIRwvhXyvDxTcpW1Ntg5EfECHyn8Mu4NX_gWfEuYScvLz-Uf82R_dzntipUCce08XCsxZ_MwADzRygewtU6kU_BZFsWILfdzA6_NWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حتی تماشا کردنش هم ترسناکه! ۴۷ متر سقوط در زاویه ۸۷ درجه با ترن هوایی در ایتالیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661274" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
قوه قضائیه: ۴ عضو اصلی باند سرقت‌های مسلحانه از تانکرهای حامل فرآورده‌های انرژی در سیستان و بلوچستان دستگیر شدند
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/661273" target="_blank">📅 08:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ونس: ترامپ درباره جزئیات نحوه پایان جنگ با ایران، با نتانیاهو اختلاف‌نظر دارد  جی‌ دی ونس، معاون ترامپ:
🔹
ترامپ در خصوص جزئیات دقیق نحوه پایان دادن به جنگ با ایران، اختلاف‌نظرهایی با نتانیاهو دارد.
🔹
رهبران آمریکا باید بسیار محتاط باشند و بر اساس منافع ما…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/661271" target="_blank">📅 07:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/661270" target="_blank">📅 07:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
نتایج آزمون سمپاد کی اعلام می‌شود؟
🔹
به گفتۀ مسئولان برگزار کننده، نتایج آزمون ورودی مدارس سمپاد
اوایل مردادماه
اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/661269" target="_blank">📅 07:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661268">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/661268" target="_blank">📅 07:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای الحدث: سفر وزیر کشور پاکستان به تهران برای پیگیری تحولات مذاکرات با آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/661267" target="_blank">📅 07:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23f31ea8a.mp4?token=BVSKpdEtDiVVlHBp0V731SIYUZBbXajMrl87oP26OP6pAb0BY8fHlwDd4RjE1n8ZhDgEqubOjs_pMjqCvjyHa564JPPKJ3VHew-23ENfUz_uyVp093M2bRe4K60o91XrO2IwrfNDEUWGX146UuBlMvCsb2ILmDQLttwztJrRI4FhkeqVcaYAsJZgGmeFYMpNqmoBlpV_np2p_gJQEcvYMf_wrEx0VxO6pv2ojo7z0TnUKIH4KGCdt8Nw3ANlG0ulFnKKulKEZ3ditWBS9Clq59qmYDnStwneeDxC5ekFegLA55WqH4JmqtB2C5RPoC31VQ7WmY7ORzoQa7l0rwBmFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23f31ea8a.mp4?token=BVSKpdEtDiVVlHBp0V731SIYUZBbXajMrl87oP26OP6pAb0BY8fHlwDd4RjE1n8ZhDgEqubOjs_pMjqCvjyHa564JPPKJ3VHew-23ENfUz_uyVp093M2bRe4K60o91XrO2IwrfNDEUWGX146UuBlMvCsb2ILmDQLttwztJrRI4FhkeqVcaYAsJZgGmeFYMpNqmoBlpV_np2p_gJQEcvYMf_wrEx0VxO6pv2ojo7z0TnUKIH4KGCdt8Nw3ANlG0ulFnKKulKEZ3ditWBS9Clq59qmYDnStwneeDxC5ekFegLA55WqH4JmqtB2C5RPoC31VQ7WmY7ORzoQa7l0rwBmFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در فلوریدا
🔹
ساکنان محلی با توصیف این وضعیت به عنوان یکی از شدیدترین آتش‌سوزی‌های سال‌های اخیر، اعلام کرده‌اند که شعله‌های آتش بیش از هر زمان دیگری به مناطق مسکونی نزدیک شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/661266" target="_blank">📅 07:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESF6DUHxqBbQr4UF8Ftcxry8XoOLu_aegxnr8HVEnPc6JMsEDqhfYlk9gt5LsJvhSMaqaF4Z6XVNd_TzGxieU3YEdIDm0D84HONP0ZjepN2RNdQYa0g_7qvrhykocOhWJeja8uAZcSiEjfIykvmyGvqnQD2IF5TuYtUFbigsMKGrTkv-fsL67vYtr-NdLcIc1eZPXXCDDYnAmyT48BHmWTrYWS4py7cwet4_VH4q0a_51pTp65D8oPV8WF7Vz-lx2q2tbgVLj--KACtbveE7Kb9t3YT0DL7gyvw8smkNgZEX1KXUhnR4JoergV_Rfc5UghVHoNa8by_UbAQfXzUhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین حذف شده جام جهانی مشخص شد
🔹
پس از پایان دور دوم در
گروه C جام جهانی، هائیتی به عنوان اولین تیم از جام جهانی ۲۰۲۶ حذف شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661265" target="_blank">📅 07:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ونس: ترامپ درباره جزئیات نحوه پایان جنگ با ایران، با نتانیاهو اختلاف‌نظر دارد
جی‌ دی ونس، معاون ترامپ:
🔹
ترامپ در خصوص جزئیات دقیق نحوه پایان دادن به جنگ با ایران، اختلاف‌نظرهایی با نتانیاهو دارد.
🔹
رهبران آمریکا باید بسیار محتاط باشند و بر اساس منافع ما [ایالات متحده] عمل کنند، نه منافع هیچ کشور دیگری.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661264" target="_blank">📅 07:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ae9133ed.mp4?token=NmvFxjev0gPnd-xbUbnvG9VTedxHjFPNdpzCN9Og5NeKi1v7yXHINUfMZD5xz9Ie_OupJapQ04hUW1l0imXEW6R5L8MA-1QZ3qaVy3xbWPFMUPyhwp7QuRjPhpYA6eYapNeeFlyXnkAHbBT8S9WGvLce7DO1WfOVrZTpdqK-q57-qWVAyf4cwX6Y8wrqyZi4fzlf2Sk2vnFyUmZP9By_yetTQQPqf-pheoFAa5oCT4pZWaXLpc0LZ1n6yOnnmLJOO2w7p-wPwBpqp_Cz81o-v2R9D9I56HjizklHGPNJCNVRHpL_D8PqvwjFxdigcaMeiKqfOvFK8cNTiOzz9shjJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ae9133ed.mp4?token=NmvFxjev0gPnd-xbUbnvG9VTedxHjFPNdpzCN9Og5NeKi1v7yXHINUfMZD5xz9Ie_OupJapQ04hUW1l0imXEW6R5L8MA-1QZ3qaVy3xbWPFMUPyhwp7QuRjPhpYA6eYapNeeFlyXnkAHbBT8S9WGvLce7DO1WfOVrZTpdqK-q57-qWVAyf4cwX6Y8wrqyZi4fzlf2Sk2vnFyUmZP9By_yetTQQPqf-pheoFAa5oCT4pZWaXLpc0LZ1n6yOnnmLJOO2w7p-wPwBpqp_Cz81o-v2R9D9I56HjizklHGPNJCNVRHpL_D8PqvwjFxdigcaMeiKqfOvFK8cNTiOzz9shjJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر لاریجانی: ما با چه استدلالی آتش‌بس را پذیرفتیم؟ در پیام اول مقام معظم رهبری گفته شد این تنگه باید حفظ شود تا برکات زیادی داشته باشد. ما از این تنگه غرامت را میگیریم ، نه این صندوق در هوای کسی هم نخواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/661263" target="_blank">📅 07:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cb0c9a6.mp4?token=R_0cXOCw6hBzEHOrMrYpveBhzWZwoSgmLd7_s9A1tpjYjBfnIAvwhMthMmI4R64aLwixZv218Vy82AMFZJGzfFyuOF3lQXJ24YhP2Cth7NGISpwFkg1515pznmmq47FQBahgBzXyrZsqtvadbVXTXKLJXCtCzaI68SsnmREp_saGBZLBPwCN-41k4s40IZ0bE671zLFQBQTy7m9QnkPUQqYRUs2v1YOKnT4cRCqD2kpgbYca03rWCN-O3kFT8Nda4hU6sP-EAsmofJP2fHxBfDEHssw4h5z0dkePL1w8MzkfdAUQSwkJMGehInzL6tL2gqNGLL2UmrSqBUpZtWvkaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cb0c9a6.mp4?token=R_0cXOCw6hBzEHOrMrYpveBhzWZwoSgmLd7_s9A1tpjYjBfnIAvwhMthMmI4R64aLwixZv218Vy82AMFZJGzfFyuOF3lQXJ24YhP2Cth7NGISpwFkg1515pznmmq47FQBahgBzXyrZsqtvadbVXTXKLJXCtCzaI68SsnmREp_saGBZLBPwCN-41k4s40IZ0bE671zLFQBQTy7m9QnkPUQqYRUs2v1YOKnT4cRCqD2kpgbYca03rWCN-O3kFT8Nda4hU6sP-EAsmofJP2fHxBfDEHssw4h5z0dkePL1w8MzkfdAUQSwkJMGehInzL6tL2gqNGLL2UmrSqBUpZtWvkaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری خطاب به ترامپ: شما دنبال تسلیم بی‌قیدوشرط ایران بودید، تفاهم‌نامه که شبیه تسلیم ایران نیست
🔹
ترامپ:  در واقع، احتمالاً تسلیم بی‌قیدوشرط هست.
🔹
مجری:  واقعاً؟
🔹
ترامپ:  فکر می‌کنم همین‌طور باشد. ببینید، آن‌ها دیگر نیروی نظامی ندارند. شناورهایشان به قعر…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/661262" target="_blank">📅 07:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
کپلر: تردد کشتی‌ها در تنگه هرمز بهبود یافته است
🔹
بر اساس داده‌های مؤسسه ردیابی دریایی «کپلر»، روز گذشته ۲۵ کشتی از این آبراه راهبردی عبور کرده‌اند که نشان‌دهنده بهبود نسبی جریان کشتیرانی در منطقه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661259" target="_blank">📅 07:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
افشای استفاده از هوش مصنوعی گراک در حملات متجاوزانه آمریکا علیه ایران  خبرگزاری فرانسه:
🔹
گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گراک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک در جنگ غیرقانونی علیه ایران استفاده کرده است.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/661258" target="_blank">📅 07:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STdzpn4BotsVw0hsI_21X9OxUsLSdKz_9QRyip-2e_o0CDRJWwLGwwYSnQU0ylNiiO9VVa801hI9IiHh_PthgFzQSVBJZLmAP4Sf_PWTTbmY3dn68sEiPQ3JmofyeVzjc3XSsw0wF-0Ca6H3elUV8NKlYoXb38-1hW6zUhGv1-h8joB0EmyqZzh8nKlwXBiFcbpASd5oLIFnhE18HpNzOg-nhHUt3-ZLKiRj3Kugm5MQ5xulhQB28pnoljyC1MWShoOB9ijnYOoURwlJMsRTphsLwEooka0iW1CdhXzlNLJWCxAa7HG707exy_m45DXOXJPmCnRH6ubbCxQm8p22eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۳۰ خرداد ماه
۵ محرم ‌۱۴۴۷
۲۰ ژوئن ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/661257" target="_blank">📅 07:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0PG8XzDLAIhZRGT4PumjYBWlaZQjKWuJwVijaoDj2h2DEdLL_nkAmYNihX_8veQ5un_p4--7oAqWPJ6JVR97UszL2FGde7mhc4BqrnTconVyMqid1ddbcrwHF70UC-vkr61m0otc6Hsv4YT9ZLJVnvPNttl7R_RerP_0sjxp-T05bTr3qCIX1KHr-BPAxXHz6CA0ZucUYYp7u8q7VVFix4tFkpFrG1auKmTVZzK22bQF5n7fusTiBpx5feMnSkC2iTkpnyWEcK66jph1ZaXeKiOI3zf-wzB_I-9wqYwulGwvyeyOTU5UyRCsahkYDh2etLqd9x3Hu3dERmbztbk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بسیاری از کسب‌وکارها تصور می‌کنند مشکل از تبلیغات است.
🙂
✔️
برای همین مدام پلتفرم عوض می‌کنند،
✔️
بودجه را افزایش می‌دهند،
✔️
کمپین‌های جدید راه می‌اندازند.
❓
❓
اما سؤال اصلی اینجاست:
اگر تبلیغ شما به آدم اشتباه نمایش داده شود،
📌
بهترین تبلیغ دنیا چه ارزشی دارد؟
🗓
موفقیت تبلیغات از طراحی بنر شروع نمی‌شود.
🌐
از شناخت مخاطب شروع می‌شود.
📊
سن، نیاز، دغدغه، رفتار خرید و مسیر تصمیم‌گیری مشتری...
همه چیز از اینجا آغاز می‌شود.
🔽
🔼
شما برای کسب‌وکار خود پرسونای مشتری تعریف کرده‌اید؟
⬇️
⬇️
⬇️
مشاوره تخصصی تبلیغاتی</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/661256" target="_blank">📅 01:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxELqmh5B9WjtsgXZHjshyr3VjG5ltyquiFgYlbffeJ2w0MqVma96s6nLc3hdm5l_-kKuQ2r1JGwErqZ9vDom8gvk0EnMd8ZjR_pK59EPZYbJ8OHCjXI3xiTUho6zBSQbV4HLspYXxDUrRVrBtOdBRZDBUsqg32OMxlDA2LoAkp5k3EocyuuxuiHRsTvAYLsctqdtSunR79QnDWknA-Kn_ZxI3EHzuVT3Vn9siQlPtD1C1jm08dmM-dfycqh3kXTbBPnArw5u6coZyxlOZ6b7K7iome2LIevSD-XaGKLpeonnZpUDkwTYk8hcxee7_iQBGoeLy2HVJ3DOi-7UnXq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌️
❌️
خبر مهم
❌️
❌️
🔰
دلیل اصلی مشکلات آقایون رو میشناسید؟
👇
1⃣
برطرف کردن اختلالات و مسائل بهداشتی آقایان
2⃣
بی میلی/عفونت مجاری ادراری
3⃣
پروستات/کبد چرب/دیابت/سینوزیت/اعتیاد
🖲
دریافت فرم الکترونیکی مشاوره رایگان
👇
https://app.epoll.ir/71553050?Referral=telegram
شماره تماس مستقیم 09211960273
یا عدد 5 به شماره زیر ارسال کنید
👇
👇
09211960273</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/661255" target="_blank">📅 01:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw1PoDxmZLTryreqBtHVF51z83khVbWBIBj-ThsWhQ_l3paCg9IIIRPDaqLKAHL8MKIX0fa3SpRNWl7fOeL6tfjtLcfOboLM87T_8xWNzw98-4z9W8flEjaIpDzQWjyedg7mSinqT5pRNVjSQ8GJaLB5kahBJ0EdBgwl2sCkbFEbiSSJ8rlDCKJOjY9lxkHDqkCl_OFktTf9jBWNTh2e13QCzL3kEWK4nPlhDRHZurOEHg7VSQm8XdTevWAKgbj5EBx8IwbqQE9_SYQaGMYXks3rCqQmzBT_Dm0_TM_j4xJrP3ivrFEnMB6e5rLWSDxGWm3KM_549febN1GoWG_hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌️
رژیم نگیرید ...
❌️
اگه چاق هستید و بیشتر اضافه وزنتون در ناحیه شکم و پهلو هستش، رژیم گرفتن گزینه مناسبی نیست، رژیم سوخت و ساز بدنتون رو پایین میاره و وزنتون دوباره برمیگرده
⚠️
✅
اما نگران نباشید، برای لاغری شکم و پهلو فرم زیر رو پر کنید و رایگان مشاوره بشید
👇
👇
https://formafzar.com/form/bgx0m
https://formafzar.com/form/bgx0m</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/661254" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اکسیوس: روبیو برنامه‌ریزی کرده است که هفتهٔ آینده سفری به خاورمیانه داشته باشد، که در حال حاضر شامل کویت، امارات متحدهٔ عربی و بحرین می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/661253" target="_blank">📅 00:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbodW62EJUcOFeYd9J2IcrHr89e2ktU2tYRAR8N8E2xp6iEo8m1Kr4aorkgT7JA5LCnKpBbqzen9au1W5qGPjfnYnkMJts0VxgGk0aWJRHa_ea7mLw3-VN9Tv4LEeynOV6fDxi4SXNTazMTUWgsRxRl6eQFkmiB3yQnRQ8eDG6qK6aX0kFTL7gMAluAIYaJ_EJPKr2VRKJ_mumINfESmSBrko8NQZ5PjMuN4uOFSSc6s7myrcEbV-K4EZBAJlTLBRpLtbq47ceSbP7Vi8-_S7r__CA2nql_A2GuYIcT65ZKzuujpO7T4tB4HHZVN4LgouCmYbgFo9-OlcRDP6pRokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صعود دومین میزبان هم قطعی شد/ یانکی‌ها با شکست کانگوروها راهی دور حذفی شدند
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/661252" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=bBr_azpi1TMCcT2AX5oBaf-JGhsAfjJtXz0T4yUlGujX5BWcYKsbl7liSquYw3GuVhXwUvA8IXonZ8v0gp0TUokMMPMZcrCUX9W4OgGyVXKYIo9GcKpYRC1Rl0UQJsSleEkmHxTaYXSR6fYCNACRLDBpp2E28lInjED-sGxgC_SyKs-UaP0HELoRxaSgxggqVZSiiJp5wLEIriUTJ4_HnPsOVxJGQpd0cu3Gv8zzpdWheqp9gLmLJ2LZw6l09ua3XzpJ3qvosqu1U8iSqJtWcj7K-hBdKLMRQJ8X_1B-B-zUMHpWWJdSZbomgwGmfVkLFgEekiHGhU_P_tIsKthAqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=bBr_azpi1TMCcT2AX5oBaf-JGhsAfjJtXz0T4yUlGujX5BWcYKsbl7liSquYw3GuVhXwUvA8IXonZ8v0gp0TUokMMPMZcrCUX9W4OgGyVXKYIo9GcKpYRC1Rl0UQJsSleEkmHxTaYXSR6fYCNACRLDBpp2E28lInjED-sGxgC_SyKs-UaP0HELoRxaSgxggqVZSiiJp5wLEIriUTJ4_HnPsOVxJGQpd0cu3Gv8zzpdWheqp9gLmLJ2LZw6l09ua3XzpJ3qvosqu1U8iSqJtWcj7K-hBdKLMRQJ8X_1B-B-zUMHpWWJdSZbomgwGmfVkLFgEekiHGhU_P_tIsKthAqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی مورنو، سناتور آمریکایی: لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/661251" target="_blank">📅 00:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFplJvmuXm1SyonTDFw6Ge6DOBljvqZ7oC6LkLvP8yxyDAB9ScsYTa9fM7AlOeX-egSFGqtBsMjpz2snK03fpOYEWCZrjStU7e4u44CMqJct7LaoS2zdT6OY0mom8BKIPPN0OZt3_JuzArXDeFtBa2DQTmyBkXEZybQWB6WupYac980Ud6x9Gjr0Cxq24iKLgofxZVf_uiW5NIHaAVRPWTVVaVR-DQGayFjgeB8RCJYToqe7cdhgOy0Qlh3O9IjWza8TciZXLD047iied3L4Uj3ltiv7nBP7LzHECRZb6oKFqZ5alLLspUpZEgfEaKwJzS0WVT02kAATsCU-ar6MgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعلاً گل‌به‌خودی آقای گل است!
جدول گلزنان جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/661250" target="_blank">📅 00:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
حمله رژیم صهیونی به جنوب لبنان با بمب‌های فسفری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/661249" target="_blank">📅 00:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=p95JhKAueFBnCwYQHCFY2hsz7NUZTIpVt9Bz4KAOYsAuo-I1G0rK8HmleCQoXvKRjXdjfQe0tto6Jk453IISIs-XvJSJ_FPICb3CUd0_37zeZo_deOGG569lu6rmtOnbn-NuoFDpNuW1v-AojolnVi7M5jXWyBBjcKg2s0qp19EbffHfthubv8ymGvVIhghC5n3pR7RCG7IOvtrl_vN58YgmXjlEoWN1dbIbfSlmpC_0ANQLHcJv8dn2DZrd0qqxXbHrLLQlrSI7cI8aGPd0ov7NSdH-KwuV-hGeGmQe1S3_4aWTzbAS1tCEp9KwToECORx45JxykcRe26VVf5Ix5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=p95JhKAueFBnCwYQHCFY2hsz7NUZTIpVt9Bz4KAOYsAuo-I1G0rK8HmleCQoXvKRjXdjfQe0tto6Jk453IISIs-XvJSJ_FPICb3CUd0_37zeZo_deOGG569lu6rmtOnbn-NuoFDpNuW1v-AojolnVi7M5jXWyBBjcKg2s0qp19EbffHfthubv8ymGvVIhghC5n3pR7RCG7IOvtrl_vN58YgmXjlEoWN1dbIbfSlmpC_0ANQLHcJv8dn2DZrd0qqxXbHrLLQlrSI7cI8aGPd0ov7NSdH-KwuV-hGeGmQe1S3_4aWTzbAS1tCEp9KwToECORx45JxykcRe26VVf5Ix5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: بایدن چیزهای زیادی به اوکراین داد و اروپایی‌ها باید هزینه‌اش را بدهند
🔹
من آخر هفته با رهبران اروپایی بودم و به آن‌ها گفتم: «می‌دانید، ما به ارزش ۳۵۰ میلیارد دلار هواپیما و انواع تسلیحات و چیزهای دیگر به شما دادیم.»
🔹
گفتم: «چرا شما پولش پرداخت نکردید؟» و آن‌ها گفتند: «خب، هیچ‌کس تا به حال از ما نخواسته بود.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/661248" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caTF4KQIKFyqesCkuU_9xL_QPSG9rWHfxS5iTwAcVZInog1l_tFZQ76XBLVGjM6hS7C-WJ-5TgV-xZJXJdvHNTzpN3IbnKgwsOQgbg0Gw0GkMlzmtpjKNo6jyjHoMANK1eDKK6EVj-P_HFohGhnYC6TLOkAXf7-mHp5oop7VqGxIwo_Fgk8CPEVsLUL8hreEPpJywL2Lw0czAnMoWyDbrgpmhXUW92PODqpp5Jrq--wgk6BJZYHB6p56KSxeJaY-8z23npiZpHCESDTGLumxHXhuBPXJu2CihEb8QITtA20dTZLEn8IC7DOFP3sZF-ZikCPA0vYb9yWv8xZg3psMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: خاک بر دهانش باد کسی که در ظاهر مقدس کاری می‌کند که پسند دشمن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/661247" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awMQ7019S7yB-Po9STD1XZqlehYSV8jFgNYQ3eAxeAqm0L8k3Vw4aWwuZ9i7C1DVcTw7skOACaufqUQwcqrWfdGCRCAWq7zOerlr-wjiDUqN8h7vOlGCVFlO0XwfCCEq3nFJ0FtYffSMUMMIZUl9Zu8LHOWmWW_NVSy7Ej1wVelKq_Vx87RMU3b_Yrm7vdqbXmgWsCw5ztSgBryhQEa4-n7Ip7WQF2D_OnkoiNCb-u7UzThHBBZB5iB1cT9CZDjIWwAfI9DCkz1IUKzkR5rYOkP-0HEOsvheghRR8Wv80GETvzbEQ72JGz8jD4lhLOsFkkxHZ9XhVkt5VxuRCWo8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی‌الاصولِ جمهوری اسلامی
🔹
«علی‌الاصول نظر دیگری داشتم» جمله‌ای که شاید بیش از هر بخش دیگری از پیام رهبر انقلاب درباره تفاهم‌نامه ایران و آمریکا مورد توجه قرار گرفت، پیامی که از یک سو از تردید نسبت به مسیر طی‌شده حکایت دارد و از سوی دیگر با تکیه بر تعهد مسئولان به صیانت از حقوق ملت و مقاومت، راه را برای آزمودن توافقی گشوده است که سرنوشت آن به رفتار طرف آمریکایی گره خورده است.
🔹
هفتصدوهفتادونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/661246" target="_blank">📅 00:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ruUU2bu4Ccr9KUyK9FLPkn8VYB3KzCX693jfULYNWfp3Uu-JuCR_1TABeFlQP9B4Tj0HVG1zVeKHP1ZUz2YracKxrJnWAE85OtjYazjO0A2TAAL3cLAQaTZU79H8tRsvVsSvAiOtF2fnmOqKFqVHBoFyhqLrWF33ueS67I-HwbQfSVN7rYngFYhMUirX-bpiG7imahO0g-SGUCvlsicZGkuffTDBbQwsCvTkJnOBXGuH959sJKGZsB7LBDLUgsubDKNk73yOjZ9foVTI1ASDrNC654sjeqe9FzVGxFsZt2h7mJvblnqGHaD_XSI5zFCMf81H8O_x4-mIQfusFqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/661245" target="_blank">📅 00:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe79MGuqY8UgB3y1XmsAcX6X4FefTRaAMkrTXk3-XplAjk8dDRB4TYPy6KYEDFrS-HYGoP3g7W8eH9bRlOzKS4l_A81r4-bCrEfrGMyyAXzhtBWBVPUQfOEoaaU3435DeZ_PMJl3NWEya4Lcql6YWiSGu4l-VG-mfzM54dPfTKr0uK1gS3cWtbuLp691Do4Sq9TCoMSP7LtP3lMhgmJD-ZeZfZcIZjSZWZ5ZxRU615Vxp9l6KG4QA2-HB_W57tYVSuucY8V1_zZqvTIHhE_Wj48CZNrmXY39RPOS1bhBGUJiIkwB7Yw_GlpStuuzHzGD9zWFElTgcEBnBNMWusH9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت خارجه به ادعای دلسوزی وزیر خارجه فرانسه برای مردم ایران
بقائی:
🔹
جناب وزیر، ریاکاری همچنان یکی از ویژگی‌های بارز فرهنگ سیاسی فرانسه است،  فرانسه در برابر بمباران و کشته شدن شهروندان ایرانی سکوت کرد و اکنون با «وجدانی گزینشی» مدعی دفاع از حقوق بشر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/661244" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=QgGY4j9pRMQx8Nrh58BWyQPn7NHGKPVHdXPy65gZq1QsnTsT6mnhHE1AgKGjM9Z7zVZxouJgHXDUEZCe15D_YP3_iVvKIIEpbxYRd9Rja-z5Uqj5aNQ67jA2T7u4ckn8iTiiBx_KfdUH9aZpbaMU2vN_wxNVWNUM6tiCUugoJStrbx6vTGWX1rb6S8Vgq0XECqHLCcGztVTw-WSeMrYPS095TgZ2ZooSOowodUP2tcV7YQYh3OBDi_OdK9JCwycZbD0qGzU_h6g7EUukc7uuXnCJRTs2K9h955EkV5TZVEwhuWlFK7TcFv33mtlKl6K-FPhQ0Iz72fULESb2iWofpLaprX-Hw-g_sWx68_beGbDghqOcceQCaVFElCMaf4U7VHVDHFBNuiMq8UOxYGvl2xiPKdjH7YCpkb6LILhlbRrEnaHi1nhkGXuARZ7GuVLpCKNiUKh1Av9Tu6E7IOxQHjE1-q--E1q0W031pBtpZe9LQeeAMChhSJ8Ik2iHee43Y24xitMcgKivjMhPCjOO2R5IugRWkkFQ0TdKo6UiUVx5HD01faJWQ9gGW8qyq51sFXbEKqDt2etORWr-jls047P_aWBm0IRXk3b06RwVyy5jj08BeTX0Jy9fjN-16w7ZacmDwdHRpwyJ9hAmz9Kvmj_chYHfy9DKeuU4-qMEJ1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=QgGY4j9pRMQx8Nrh58BWyQPn7NHGKPVHdXPy65gZq1QsnTsT6mnhHE1AgKGjM9Z7zVZxouJgHXDUEZCe15D_YP3_iVvKIIEpbxYRd9Rja-z5Uqj5aNQ67jA2T7u4ckn8iTiiBx_KfdUH9aZpbaMU2vN_wxNVWNUM6tiCUugoJStrbx6vTGWX1rb6S8Vgq0XECqHLCcGztVTw-WSeMrYPS095TgZ2ZooSOowodUP2tcV7YQYh3OBDi_OdK9JCwycZbD0qGzU_h6g7EUukc7uuXnCJRTs2K9h955EkV5TZVEwhuWlFK7TcFv33mtlKl6K-FPhQ0Iz72fULESb2iWofpLaprX-Hw-g_sWx68_beGbDghqOcceQCaVFElCMaf4U7VHVDHFBNuiMq8UOxYGvl2xiPKdjH7YCpkb6LILhlbRrEnaHi1nhkGXuARZ7GuVLpCKNiUKh1Av9Tu6E7IOxQHjE1-q--E1q0W031pBtpZe9LQeeAMChhSJ8Ik2iHee43Y24xitMcgKivjMhPCjOO2R5IugRWkkFQ0TdKo6UiUVx5HD01faJWQ9gGW8qyq51sFXbEKqDt2etORWr-jls047P_aWBm0IRXk3b06RwVyy5jj08BeTX0Jy9fjN-16w7ZacmDwdHRpwyJ9hAmz9Kvmj_chYHfy9DKeuU4-qMEJ1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری خطاب به ترامپ: شما دنبال تسلیم بی‌قیدوشرط ایران بودید، تفاهم‌نامه که شبیه تسلیم ایران نیست
🔹
ترامپ:
در واقع، احتمالاً تسلیم بی‌قیدوشرط هست.
🔹
مجری
:
واقعاً؟
🔹
ترامپ:
فکر می‌کنم همین‌طور باشد. ببینید، آن‌ها دیگر نیروی نظامی ندارند. شناورهایشان به قعر دریا رفته‌اند. من نیروی هوایی آن‌ها را نابود کردم، تسلیحات ضدهوایی‌شان را از بین بردم
🔹
مجری:
درست، اما هنوز هم می‌توانستند تهدیدآفرین باشند. آن‌ها عمدتاً قایق‌های کوچک تندرو یا شناورهای گارد ساحلی داشتند.
🔹
ترامپ:
خب، هرطور می‌خواهید اسمش را بگذارید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/661243" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575cea691b.mp4?token=r65jyywGhcv0WN67KzSiW1D_ZzThi5fkrkQ3fSn8EfWyjhWxvzc7JF70mNO0io-m1vO653dYLx2ocxr9XOAw36oQnqhoT4pbp-2g1vkO6kBlJQs6mssnYfQgksDmjIUynmeVUfBOPB7YDhriP2WFQ5_b4HT0JHJPUkmGQPi8XW0IHJfI859RjtntRP04FmmEhgQJ8_EiPuipkn1tc9fBrUgViS6rDyTCFiArSudp74zBmUunwN7ouH6E5bEsTPnnc_RYZXwjWPrizufO4YEokEd2ls1zAhl2v5bmpbe0_mRzEgoZygjzVY0SQ2LW97y4LnA4QE6X8eK_b0bJrtGtr36MIRV2Zf2A1GoMzgbqYqq6ubHv4C7WlTwztncHk6vE3zWjZLdq2psPZdPlpYLrOGKYdWMr4NrVom0JsK4_kjx8ME5_8GE7gHWePwE6rEhm1h-lKMOjApb8FNf4rxl6wJxsk8w5t_bXJfWaH5vWxojgUfxWH_IXJQYqtn0wBNNFYp80qX_i5fzkTffqkMpLpMFpwQNGDdAhuwNvmp0bOERnWqifSs3CRN5wu8YhNnfUwkNJSEPu1fQ6ryiYpZ6e6b0VNziC0GUsIh1dxI9F2rSWUrX6YGYB9mcgRlkp7Jgq-Et-uY8OqgjEO-GpBJoY65YL_h-CbyIvaGzzCIcWpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575cea691b.mp4?token=r65jyywGhcv0WN67KzSiW1D_ZzThi5fkrkQ3fSn8EfWyjhWxvzc7JF70mNO0io-m1vO653dYLx2ocxr9XOAw36oQnqhoT4pbp-2g1vkO6kBlJQs6mssnYfQgksDmjIUynmeVUfBOPB7YDhriP2WFQ5_b4HT0JHJPUkmGQPi8XW0IHJfI859RjtntRP04FmmEhgQJ8_EiPuipkn1tc9fBrUgViS6rDyTCFiArSudp74zBmUunwN7ouH6E5bEsTPnnc_RYZXwjWPrizufO4YEokEd2ls1zAhl2v5bmpbe0_mRzEgoZygjzVY0SQ2LW97y4LnA4QE6X8eK_b0bJrtGtr36MIRV2Zf2A1GoMzgbqYqq6ubHv4C7WlTwztncHk6vE3zWjZLdq2psPZdPlpYLrOGKYdWMr4NrVom0JsK4_kjx8ME5_8GE7gHWePwE6rEhm1h-lKMOjApb8FNf4rxl6wJxsk8w5t_bXJfWaH5vWxojgUfxWH_IXJQYqtn0wBNNFYp80qX_i5fzkTffqkMpLpMFpwQNGDdAhuwNvmp0bOERnWqifSs3CRN5wu8YhNnfUwkNJSEPu1fQ6ryiYpZ6e6b0VNziC0GUsIh1dxI9F2rSWUrX6YGYB9mcgRlkp7Jgq-Et-uY8OqgjEO-GpBJoY65YL_h-CbyIvaGzzCIcWpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت طرفدار آمریکایی از تیم ایران / راه برای گفتگو و تجارت با ایران باید باز شود
🔹
هوادار آمریکایی تیم ملی فوتبال ایران می‌گوید: از تیم فوتبال ایران حمایت می‌کنم. با وجود همه حاشیه‌ها و رفتارهای ناعادلانه، این تیم شایسته احترام و تشویق است. باید به‌جای تنش، راهِ گفت‌وگو، تجارت و ارتباط باز رو انتخاب کنیم.
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/661242" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTOKd1yyZ22zlloKDRbs56iot40VwnMsnjEK3EM_VaY1CEddS-NF0lc3gWtR7s4eAWEFvjiTQ-E7zitmeydL4Yfihvohb0Coqn5C2UWl3SNx-C7BbAgpVU4vpKk74g2m_wWALoPWXNKbd5a31xONT3_CDPybFOs8Bt_S31eXy2O4OmL9u-XvwANIO-b9hHNUvCgFQOj9ZKZj0or-ySzzU4L9zQWrZfi0Z8c_j5Sr7ys-BGPQamSHGUe_nUwur3WKn1sWQMYKvm-ESzbhx52rkjFgSjhdF9vz6vTDBH0HTOqM_nwQNOuvF4X6tL7iYcf7lgXjRbzfP9oQknQdlF7M-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس جمهور آمریکا با ارایه تصویر یک نظرسنجی : توافق با ایران بسیار محبوب است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/661241" target="_blank">📅 23:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66787826ad.mp4?token=QV9gywvjr0geNNYs_G7m2iNnyqvoz3NZrojTRw8k5PGWT0uObsc8z2TomhpV-yu7Ij5MwHi0aUg3ss09lfiCqKQ4nqrbjGqgcWGpeGYw1ePOt10PfSxYN0fFxvssVig_8WSGPx8_GXlZCtDmlCCYhgvY7TUS-LyRT4M18Udsk4fJdEohjpMgaClWhDPgQlghGPCfQTFuMXF2H4jo9MikmBf1bjSCJAZGipgx2QQdL1JhAqv6RpRlzU5TTD8vnCMnYbFI0vP1okEHH5ulDVKkQ9m0lD6RFQ78SOmr1haFrETdfUi84YULFFsv90zw3s_u4NQqvNGcO7sG200EkoQf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66787826ad.mp4?token=QV9gywvjr0geNNYs_G7m2iNnyqvoz3NZrojTRw8k5PGWT0uObsc8z2TomhpV-yu7Ij5MwHi0aUg3ss09lfiCqKQ4nqrbjGqgcWGpeGYw1ePOt10PfSxYN0fFxvssVig_8WSGPx8_GXlZCtDmlCCYhgvY7TUS-LyRT4M18Udsk4fJdEohjpMgaClWhDPgQlghGPCfQTFuMXF2H4jo9MikmBf1bjSCJAZGipgx2QQdL1JhAqv6RpRlzU5TTD8vnCMnYbFI0vP1okEHH5ulDVKkQ9m0lD6RFQ78SOmr1haFrETdfUi84YULFFsv90zw3s_u4NQqvNGcO7sG200EkoQf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اکنون ما توافق‌نامه‌ای داریم که دیشب امضا شد و ۶۰ روزه است
دونالد ترامپ، رئیس جمهور آمریکا:
🔹
آنها باید معامله کنند؛ در غیر این صورت، کارهایی خواهیم کرد که آنها را خوشحال نخواهد کرد، اما فکر نمی‌کنم  کار به آنجا برسد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/661240" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fu_C69kficEnJ1AsRZMPxZtrfpNTG39Vi8k7wZ9XpVRpRkpob8Q6KwML-XPXN7UoXyXSv2WGVp4M5hqB5oyMGNIpYFB29BCk4PjlnXt_PRnHCOo_Q5Z6M0xph7gI8M9i3Wxz4t5abLcuIUuhBzp96OZuv_OWSP_fYV2hcLk8mNk1Z49coDzy-qriJAXOWklkaEY7g3zVxsO0LWTbtxMFOAlAWIZ_1J9jSFlbBQuCsgFlRlbFsmPeEaunMaX59qps95Y5hVewMFmosGcHAwZKYAJl-bNpFt9KTHxm04Dk1PMd3AATJHoly9-fAqM4SzBFze2fxOR9mwV_sgUOLd-YLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدای چندین انفجار در استان ادلب سوریه شنیده شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/661239" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پل امید بر رود تردید
🔹
تفاهم با طرف‌هایی که سابقه طولانی بدعهدی و نقض تعهدات خود را دارند، نه موضوعی برای خوش‌بینی افراطی است و نه دلیلی برای ناامیدی مطلق.
🔹
تجربه‌های گذشته نشان می‌دهد که در چنین شرایطی، مهم‌ترین اصل، حرکت بر مدار واقع‌بینی، دقت و سنجش همه احتمالات پیش رو است.
🔹
در این چارچوب، منتقدان و نیروهای انقلابی که نسبت به نتایج احتمالی تفاهم تردید دارند، بهتر است از قضاوت‌های شتاب‌زده و تقابل زودهنگام با روند موجود خودداری کنند و ارزیابی نهایی را به نتایج عملی آن بسپارند.
🔹
در مقابل، دولت و تیم مذاکره‌کننده نیز باید از ایجاد انتظارات غیرواقعی در جامعه پرهیز کنند.
🔹
معرفی تفاهم به عنوان راه‌حل قطعی مشکلات یا یک پیروزی کامل، می‌تواند در صورت بروز بدعهدی یا تأخیر از سوی طرف مقابل، به سرخوردگی افکار عمومی منجر شود.
🔹
همزمان ضروری است مواضع مسئولان به گونه‌ای بیان شود که این پیام را به طرف خارجی منتقل کند که پذیرش تفاهم به معنای تغییر اصول و مواضع راهبردی جمهوری اسلامی نیست.
🔹
طرف مقابل نباید این روند را نشانه عقب‌نشینی یا ضعف تلقی کند، بلکه باید بداند تداوم و موفقیت هر تفاهمی در گرو پایبندی متقابل به تعهدات و تأمین منافع ملی است.
🔹
در نهایت، این روند فرصتی برای آزمون عملی دیدگاه حامیان مذاکره و تفاهم نیز به شمار می‌رود.
🔹
آنچه امروز اهمیت دارد، حفظ تعادل میان امید و احتیاط است؛ نه باید همه مشکلات را حل‌شده دانست و نه از امکان موفقیت یک مذاکره دقیق، هوشمندانه و مبتنی بر تیزبینی دیپلماتیک ناامید بود/خبرفوری
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/661238" target="_blank">📅 23:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxXalBBiqs1XMBSVhjHxsFMRqhz-TyrAf_ZTPRqlrg4VYMpF5TzzyceVsSI7YgJsvFgHctYm_ASdkDBc15NluOzhmFNKaisC6372FrNA5QB8j13OdokbZmC2ujrO2iTNvjr8HxZmfHWBZxWFXWoSDf8t93iKntFFUz1NbSuXWaEqr2qZYvmK7c-UC8H43v2fhylnGy0JSQACMgFcs8vA-JOIEA3cMw0y6zyBGRV-7Ye9W2T2UpyyZs8HgZGuWPkldrTERPIkmXzSgkr045DQ_tIGLLTw1NCAM3NPlQOiO5h924hfZjb-uSaFURN7IdIe0LA68ziuZ-1R2zc_JLowXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: ایران به نقض تفاهمنامه پاسخی بازدارنده خواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/661237" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
گفتگو با یک آمریکایی هوادار تیم ملی / حمایت از ایران با صدای بلند
🔹
هوادار آمریکایی تیم ملی می‌گوید، این حمایت فقط از یک تیم نیست؛ از مردم، تاریخ و کرامت یک کشور است. از مردم فوق‌العاده ایران، میراث غنی آنها و مخالفت‌شان با جنگ و خشونت. فوتبال اینجا فقط یک بازی نیست، یک نماد از همدلی و ایستادگی است.
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/661236" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGDReVf14JAKoalIkzv1hM3v0RauqRqwcZ6NnKlxxqhBxhdJeggFE7X9GoFBxXInPcqmy0pes-r9DN6BeG65IrxQPp5c3L0pGDosbMQPmnXnALBpfb4GQ7BJ8dmCzxydmk4AQmdilwiixDT-LXmUUU_PURZcolNjb4az0itbcY_hMCNTBlcAXZ9A8UxJesZLpvURxf8WtMw_yvPLiuw8uS2PTFWPowAJkvBQQ74uCtv0rNp-OAlmZqNGTTfxyfDbs3JaowhUINQnFb0sZbyAe8yP2w0dBMiqZ_oLc4z5PlgaZKZcV3_MhryfT_0abJcedDz1ZTEsBVnpeqBjpNOhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از هدیه قطر رونمایی کرد!
🔹
ترامپ در پایگاه نیروی هوایی اندروز از یک هواپیمای موقت جدید ریاست‌جمهوری رونمایی کرد؛ یک جت لوکس که توسط قطر اهدا و عبارت «ایالات متحده آمریکا» بر روی آن درج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/661235" target="_blank">📅 23:25 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
