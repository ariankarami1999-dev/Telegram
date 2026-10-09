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
<img src="https://cdn4.telesco.pe/file/TYpCHI7OhRB_ihME0vi5QUjmqQTELvdNXq8KuSYTn2eB33Ga3rS6BbRBvQ4zwA8qid5Z4KIdxIaMhRnMvbQ_8RQuY66G-Ks51zhOD1Dca2lqSTcBwJVWzt9ZYTwVHo9JlOetGTJTMYulzgifRZJ4ky47tnqIfuUM0huLnf3Sio9PXPVnZgh5zafwU7zPZE4K6ZDPx4jWgkFomkQs3mDaZ-vpW6OJ_1AZXxdEoq8RYM9YyVQBx1J_gRNeoUU_UryhvLvCEGkiqMu9GgBrCgnHHHqqb80wsW0X8bFeNyyFQM7bRB5RMDbtjh-0tbeegxdt-yHA3_nwNo0HVu68E0KWSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-151707">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTURBO VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th9zySOR2ou6xMLKXagXlBvJ5zRb-L81x21mavhQY5QFeYYNIcP0jsd7rw02LIMZky4iELXY4atIQV5L9_icM4UGr0Z-ezkRRElRqbKoDO2x1pbh7g4-scWULBFsJ85OOJsBiZq1KRC3r7QYUwLQefG7Q28g2RGNsXnKFz22FGeZQjfubrMIOeBTZXmyKJt0UEqnOa3jJzTilg9TuD8ksga6j8_BRyaZpD_kcol6IQCGWNgEuq-Bxxi1zIvLowm1WB8DSZgFjncc2NSHqmBovx1pTZ1YZs-EsgEyXvai0QkVmSs3qVRgYYe601aEnZwVQnVoULgd5EmoaLH5-0_AvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
TURBO VPN
| اتصال بدون محدودیت حتی در شرایط جنگی
🐇
ورود به ربات و دریافت هدیه و تست
🛡
اتصال پایدار
حتی در
سخت‌ترین
شرایط اینترنت
🌍
بیش از
۳۰ لوکیشن
فعال و پرسرعت
🔄
آپدیت
مداوم سرورها و روش‌های اتصال
🤖
سازگار با تمامی
ابزارهای هوش مصنوعی
🎮
سرورهای مخصوص
گیمینگ
با
پینگ پایین
📈
مناسب
ترید، استریم
و استفاده روزمره
🔥
🔥
دسترسی رایگان به
فیلم‌نت و فیلیمو
🎧
یوتیوب
و
ساندکلاد
بدون تبلیغات
🎁
۳۰درصد تخفیف ویژه: ‌
TURBO
🛒
خرید از ربات:
@turbovpn_new_bot
👨🏻‍💻
پشتیبانی ۲۴ساعته:
@kasrazandi
.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/151707" target="_blank">📅 01:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151706">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e2c521e1.mp4?token=BeQtkvWMGw9roSGsw2XEe3PVaTH3tZ49WokfCMGpN7dawDFL5bS6plSe2oxotQYbr_bwy6m7ZzXxfOj4hvHo83nGK4wVhDF4Flcmy7WZhMfPXxTqf6XKFR1KmMLT2JODR9j4nwNJRMRjrg4F7gLUBsyvQRTGfapgInIQ47AVtwubMI0qolGOuFM1kQRNO0qIJDvJ---5N_qTfCwspHjS_5f7gDu83HWJmyX1MdeB6KVonMdDo4IMQl2SEyQUn_lJxcZB03TFrz-D1swWfZATpaLIBHM6k6SIHThxw5bujnw-ZXeGH7t_eMPnRXHY3Hxng7Wvs7LRUZE7cQ1zSbaO1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e2c521e1.mp4?token=BeQtkvWMGw9roSGsw2XEe3PVaTH3tZ49WokfCMGpN7dawDFL5bS6plSe2oxotQYbr_bwy6m7ZzXxfOj4hvHo83nGK4wVhDF4Flcmy7WZhMfPXxTqf6XKFR1KmMLT2JODR9j4nwNJRMRjrg4F7gLUBsyvQRTGfapgInIQ47AVtwubMI0qolGOuFM1kQRNO0qIJDvJ---5N_qTfCwspHjS_5f7gDu83HWJmyX1MdeB6KVonMdDo4IMQl2SEyQUn_lJxcZB03TFrz-D1swWfZATpaLIBHM6k6SIHThxw5bujnw-ZXeGH7t_eMPnRXHY3Hxng7Wvs7LRUZE7cQ1zSbaO1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های مارکو روبیو، وزیر خارجه آمریکا، تو آتنِ یونان درباره امپراتوری هخامنشی و لشکرکشی خشایارشا به یونان:
🔴
480 سال قبل از میلاد مسیح، ارتش خشایارشا وارد آتن شد و معابد این شهر رو به آتیش کشید.
- تا اون موقع بیشتر مردم آتن با کشتی به یه جزیره نزدیک فرار کرده بودن، اما تعداد کمی حاضر نشدن خونه و شهرشون رو ترک کنن.
- اونا خودشون رو توی قلعه سنگی آکروپولیس محاصره کردن و تصمیم گرفتن تا آخرین لحظه مقاومت کنن.
- از بالای صخره‌ها سنگ‌های بزرگی روی سربازهای ایرانی می‌انداختن و تونستن برای چند روز جلوی
قدرتمندترین امپراتوری اون دوران
(هخامنشیان) رو بگیرن، اما در نهایت شکست خوردن.
- ایرانی‌ها معابد رو غارت کردن، پرستشگاه‌ها رو به آتیش کشیدن و آکروپولیس رو با خاک یکسان کردن.
- وقتی مردم آتن برگشتن، بقایای بناهای تخریب‌شده رو جمع کردن و توی همون تپه دفن کردن و چند دهه بعد، در دوران پریکلس، معبد پارتنون رو ساختن.
🔴
ما این روحیه فداکاری رو در مقاومت افسانه‌ای 300 سرباز اسپارتی می‌بینیم.
- اونا در برابر ارتش عظیم ایران محاصره شده بودن و تعداد نیروهای دشمن خیلی بیشتر از اونا بود.
- با اینکه هیچ امیدی به پیروزی نداشتن، حاضر نشدن خودشون رو نجات بدن.
- ترجیح دادن تا آخرین نفر بجنگن، اما موضع و وظیفه‌شون رو رها نکنن.
- این همون روحیه‌ایه که بعدها ارزش‌های اخلاقی تمدن غرب رو شکل داد.
🔴
اما این نگاه کاملاً با چیزی که امروز در بین متعصبانی مثل ملاهای تندروی ایران می‌بینیم، فرق داره.
- فرهنگ مرگ‌پرستیِ اونا، کودکانی رو که عملیات انتحاری انجام می‌دن، به‌عنوان قهرمان ملی معرفی می‌کنه و شهادت رو به‌خودی‌خود یه هدف می‌دونه.
- اما قهرمان‌های ما این‌طوری نیستن، قهرمان‌های ما ممکنه حاضر باشن برای آرمان‌هاشون جون بدن، ولی مرگ رو پرستش نمی‌کنن.
- اتفاقاً چون برای زندگی ارزش قائلیم، کسی رو قهرمان می‌دونیم که حاضر باشه جونش رو فدا کنه، اما به اصول و اعتقاداتش خیانت نکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/151706" target="_blank">📅 01:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgdeMH2I4smvvo_wy2qmN-GrGoJ0g3TahJSxA7xFia94mmvovEXbZbNo2b17P10AJqGfXfYwkl9CdmplBzNsM4mHmYFvrbeMr_XFXCi1PkxfzuhJILLsKoye52G-NLnZUH1nt2RKR8amZrQ8krohFNFCMtpC-ahgQe8P_1VrnPYIMmxFeqyEc0yJxjesOindD8VzhHVj4wnOMr3jn3kP4QfnPBmpt1lACJarnB1WGJIdxa00wwg_WxQkcn8kG6PS7rUDKvN8dzQCc7JcJCe7HkfgLRp0JYhzFEKFaSv2cxJNySU2KnBYMLaqBJP-OrKb9yeN8cRHj_OvX31HBbDbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو یکی از ادارات مملکت، کارمندای یه شرکت همگی دهنشون بوی بد می‌داده، اسهال، دل پیچه و خشکی دهان داشتن!
خلاصه میرن دکتر و آزمایش میدن معلوم میشه الکترولیت بدنشون بالاست!
در نهایت دوربین هارو چک میکنن و می‌بینن هر روز صبح آبدارچی شرکت میشاشیده توی سماور و چای می‌داده کارمندان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/151705" target="_blank">📅 01:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151704">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون طرح‌هایی برای بمباران شدید سه‌روزه ایران آماده کرده است
‏
🔴
اهداف شامل زرادخانه‌های موشکی و پهپادی، تأسیسات انرژی و مقرهای سپاه پاسداران است. ترامپ در ماه‌های اخیر ۵ طرح بزرگ را رد کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/151704" target="_blank">📅 00:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGmkUk9ekub9l-HBvUeHKHuoyLP5Pn_sFi3Zyg_dj36SkYPhW3U1Pc29ok4P362yglYxLzaUA3cn_maBQDT1vItoOC1isNDJ6u--M2LzT-gUYqzPNY5I-Xyn-LFxC5w0W_iFMdAHg0e_75vNwyDu21F3B-_EjgVgB1nFeTxC8vSaWj8LUAgSiA2uHFV_1RFeoFpfXVYIlvSB2_GrDBaRf091yQ3A577tsLX0JTcMCDXg3_0bdzCz5y4Zptvtt-llU9tRxhNqsGcJepkO_xVvqMOGQCXNzYm4lDZ-X6sJAbQFdXIxPgkbJPRZ3y0_ULZGKSxQuLf37ld53LDbfaTmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اورشلیم پست: ترور تنگسیری برای جلوگیری از فرماندهی او بر کل سپاه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151703" target="_blank">📅 00:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB9gqa7RYuT286Z1jMDYLFWodP0uiUa5B9wvaBw6TN0DA3aV2SW5mHX5Pf4P9Zc_Rym85Ow-NcgBBdrt2z0nrTMdA8giJew6THZY02xzr1s-ng9VTuAp7zEa03d7focLRC1i2YbqY_-JMZZ9Nu2Mbp2xfUB5kwbasj0Oj96y-2ktG4Ihx06GcuihJn5C-TKnN6MK_ysBHwqX18nnGwczU5-sagocylpnPOGAMCdMwtlkthT8PgL4keB6Ii1_vImsguCY5lsTIWmacBQZkROoQTWFukTgQrX4RcN6gJslRTfRFCIBm-tiAhBSJOgWYG5HT6BzT-XjXagPnRqpknXF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس:
نگاهی به گذشته: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد که ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا به جنگ اسرائیل علیه ایران می‌پیوندد یا نه.
🔴
اما زمانی که این اظهارات مطرح شد، ترامپ از قبل تصمیم گرفته بود به تأسیسات هسته‌ای ایران حمله کند.
🔴
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز حملات آمریکا و اسرائیل علیه ایران، ترامپ ادعا کرد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
🔴
اما در واقع، او پیش‌تر تصمیم خود را گرفته و مجوز حملات را صادر کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/151702" target="_blank">📅 00:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=mFT2DVXhWyGAp1HdoH03PbBJ0CrU4eNGbw30UbGtY2OTSz_GGyEHUzYlgjqf3V4Zv8PaJn-XkUUmLUy3ZbIa4qxa03Lwa5wLWtMjSpiSbBHYNkpw5ZJVmTlL2O3P9Jyho245vGWh9QrZ20POjywwWE7jLbJaIor2OF9HnuaJJapDIhIFeVyApdcwBEqG4xXmpHi28cRIAPROCpZmtE4gvW-GO-Uoj6-YECSEM0Xm-xnveEil8n778X9FyN-bUvbv1WYjt-v5W0HVYAsl9syT3L1eO0mJeycL-YdzxfWtAJEl74Ccs2VfhAsrfmODbxBkSZ-ZVTju9psq9wpoG4KMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=mFT2DVXhWyGAp1HdoH03PbBJ0CrU4eNGbw30UbGtY2OTSz_GGyEHUzYlgjqf3V4Zv8PaJn-XkUUmLUy3ZbIa4qxa03Lwa5wLWtMjSpiSbBHYNkpw5ZJVmTlL2O3P9Jyho245vGWh9QrZ20POjywwWE7jLbJaIor2OF9HnuaJJapDIhIFeVyApdcwBEqG4xXmpHi28cRIAPROCpZmtE4gvW-GO-Uoj6-YECSEM0Xm-xnveEil8n778X9FyN-bUvbv1WYjt-v5W0HVYAsl9syT3L1eO0mJeycL-YdzxfWtAJEl74Ccs2VfhAsrfmODbxBkSZ-ZVTju9psq9wpoG4KMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
باهنر
:
ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/151701" target="_blank">📅 00:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
👈
جرد سزوبا، خبرنگار المانیتور: سناتور کریس مورفی می‌گوید پس از آنکه به‌طور جداگانه با امیر قطر و میانجی ارشد دیدار کرد، توافق با ایران برای پایان دادن به جنگ «به نظر نمی‌رسد در آینده نزدیک محقق شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/151700" target="_blank">📅 23:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ارسال تجهیزات نظامی فرانسه به عربستان سعودی
🔴
وزارت خارجه فرانسه: هدف ما از ارسال تجهیزات نظامی به عربستان سعودی دفاع از زیرساخت هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/151699" target="_blank">📅 23:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151697">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ead6bb1f.mp4?token=PysDjjU5Zi7i6wVjtdtW0rb9H9xR1uS5nzq6mugJn2a9VrzMr27ruN7DBjy1SBBNS-H7gVn56LCylzFUvJK6OJtKI2NNS058R_HL6K5nMjcSr9OovxtX_WnY8ceL-bghNrgu6F6gUQZ778CxMxsAG15MAjRgR-8vOxMVhkCp20MmK92mqOxq4uERxduxGobwTFCZXTiQy9QFOX4cVZdPOtGKPAixkJTqL5lAOO3LNmYQaee7eOlLFlS5TyJ1KBY6RSorY2gbIQip_lpg1y9bRY-HVqiFN_V4gZZx5JP8KlQm5dKbO30hn9RqexL77t-FXbfLwgw1lMAkGfRRdFLV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ead6bb1f.mp4?token=PysDjjU5Zi7i6wVjtdtW0rb9H9xR1uS5nzq6mugJn2a9VrzMr27ruN7DBjy1SBBNS-H7gVn56LCylzFUvJK6OJtKI2NNS058R_HL6K5nMjcSr9OovxtX_WnY8ceL-bghNrgu6F6gUQZ778CxMxsAG15MAjRgR-8vOxMVhkCp20MmK92mqOxq4uERxduxGobwTFCZXTiQy9QFOX4cVZdPOtGKPAixkJTqL5lAOO3LNmYQaee7eOlLFlS5TyJ1KBY6RSorY2gbIQip_lpg1y9bRY-HVqiFN_V4gZZx5JP8KlQm5dKbO30hn9RqexL77t-FXbfLwgw1lMAkGfRRdFLV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه به اربیل کردستان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151697" target="_blank">📅 23:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا: ایران بین دو راه انتخاب داره؛ یا با مذاکره و به‌صورت دوستانه این موضوع رو بپذیره، یا آمریکا از راه دیگری وارد عمل بشه. وقتی زمانش برسه، مشخص می‌شه کدوم مسیر انتخاب می‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/151696" target="_blank">📅 23:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151695">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پارلمان اروپا ایران رو محکوم کرد
🔴
پارلمان اروپا قطعنامه‌ای تصویب کرده که توش ایران به نقض حقوق بشر و خشونت علیه غیرنظامیان محکوم شده. جزئیات بیشتری از این قطعنامه هنوز منتشر نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/151695" target="_blank">📅 22:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تو اعتراضات فرانسه هم شیشه میشکونن اما در کنال تعجب هنوز کسی کشته شنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/151694" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151693">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn9MLNO-Y-TJVx51Nekx8HcKCrXOsZ9SQwheOb1NL6U4NvWbvlxIsPMn2bs5OGxN_Oy2Qd2TASojCsWBJL5bZg8Gc4lv3DHPDZ7FW_WXRJtp63CnShkpqC1RptNMdD-lIofTItFE58Q6CVWaQ423GxuL_0QKxgapdzy4zzihlbryCOfXUjRRXpgCm4fpGgQsxNlix3h5IGpdsjZ1eQQv9y8pS22B6vVBGU2feNZ2Ska7gLPPzOCOjahn3pWYBp7_pxekPka8JNz_RbcvJIm7uk-mxSfQBTI29NcBToaVApoFqjEBZI43AQuHmYFtdkSoUs8LP91LFOORa5cmYc3N5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال:
رسانه‌های دروغین و ساختگی در تلاش هستند تا وانمود کنند که من از دشمن می‌خواهم شهرهای سن دیگو و لس‌آنجلس را بمباران کند. در حالی که در واقع، من در مورد این صحبت می‌کردم که افزایش موقت قیمت بنزین، هزینه‌ای ناچیز است در ازای اینکه ایران سلاح هسته‌ای نداشته باشد. و اگر بخواهید بدانید هزینه واقعی چیست، تصور کنید اگر آنها سن دیگو و/یا لس‌آنجلس را بمباران کنند چه اتفاقی خواهد افتاد؟
من فقط در حال مقایسه بوده‌ام: پرداخت کمی بیشتر، برای مدت کوتاهی، برای بنزین، در مقابل بمباران شهرهای بزرگ ما.
همه این را می‌دانستند، رسانه‌های دروغین هم این را می‌دانستند، اما آنها همچنان ادعا می‌کنند که من از دشمن می‌خواهم دو شهری را که دوست دارم، بمباران کند.
منظور من کاملاً واضح است، اما این افراد، افراد فاسدی هستند و فکر می‌کنند می‌توانند به طور مداوم با انتشار اخبار دروغین، از این کار فرار کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/151693" target="_blank">📅 22:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151692">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
ان بی سی: ترامپ قصد حمله داره و اینکه گفته تا قبل انتخابات حمله نمیکنیم دروغه
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151692" target="_blank">📅 22:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c550ea18ef.mp4?token=Xp-8NXFFXLwxL0ZTSJDJs8_t2p9IKbP1y3f2mQPhsROYhKJCGlKM7JGFNxHoL9krGAUMHUU-yJG9Zbe2SgG6P-xyxd-V7xPwnlUHDycsJmp4Q0HXnUmUePTirAsU8um7ZFrMd53JI_PLwPxe-Wz3aBITDfI00o9jnvWCsykfhTSfrkzLpCqoXcv5SW-3m1yz0Vko4SfkSmBu94YYCt1eVpB0WYihOB5OYKF9hQjWy0N8oJkJxvCTr0mgx3uR66JMP9eT8jKDmz-1EMKiNJSM4DXmzCTj1Sug6MFew8KEXeHcZtaDuIY0i60e8fu9Z5g6zbkKV0asBWX77uwpEQB17DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c550ea18ef.mp4?token=Xp-8NXFFXLwxL0ZTSJDJs8_t2p9IKbP1y3f2mQPhsROYhKJCGlKM7JGFNxHoL9krGAUMHUU-yJG9Zbe2SgG6P-xyxd-V7xPwnlUHDycsJmp4Q0HXnUmUePTirAsU8um7ZFrMd53JI_PLwPxe-Wz3aBITDfI00o9jnvWCsykfhTSfrkzLpCqoXcv5SW-3m1yz0Vko4SfkSmBu94YYCt1eVpB0WYihOB5OYKF9hQjWy0N8oJkJxvCTr0mgx3uR66JMP9eT8jKDmz-1EMKiNJSM4DXmzCTj1Sug6MFew8KEXeHcZtaDuIY0i60e8fu9Z5g6zbkKV0asBWX77uwpEQB17DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست درباره ایران: ما قصد نداریم در ایران، یک کشور جدید بسازیم. ما قصد نداریم تعداد زیادی سرباز را به آنجا بفرستیم و بر مناطق آن کنترل داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/151691" target="_blank">📅 22:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ به ایلان ماسک: ایلان، تو دوست من و یک فرد بسیار، بسیار خاص هستی
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151690" target="_blank">📅 21:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9PrSm9MJnKuLPpRhOHAXkdU7K3b1TL2lhJJchD6SoDpmevXQH7s2KXzzYLm3sA4uT0hhTNrhAR7pUjoXnfviZJ__ugEKQJ7aI8-CM-u9e232VxWgNv_kEz1PeErpYqX2aRsNYdsRvXHgmxts4fAb0wa8p553T-M_sc2KyFVw7AA2lcYNtcbLy1MiUYFJ7yj_8XJGHOyspVMUkEWloD-zQ75Uqj59Os1ly-Iz1onmsLBhie-qY1DhtNl4uOJT0-sNLCCzjMDlpvSe9V_CMmJQRRM3ZEKn3NvllrFR4ZWAHNXT09YPXlUZZXc0Y_17nD96FV7uFLPL9BcmRiCYKQcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان و پوتین باهم دیدار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/151689" target="_blank">📅 21:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کانال ۱۴عبری: اسرائیل در حالت آماده‌باش کامل قرار دارد، و خود را برای بازگشت به درگیری با ایران در آینده نزدیک آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/151688" target="_blank">📅 21:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de2f5f8c0.mp4?token=eNR70mRKKpc8gRNvdX16K051-ZoE5hrNDqwZDmPQbj962GzQBXuzusToF1c-DRpCxrIWOpAITqtSG_7LHc_5J9lrg_kRTO9XHga1Km4sxcHy4_eWCj2cbJIO0NyHrHUmB5b9Q3zYH0uWojYeSe8BrQZ-8E-hs1HliCQ2JuF8E1filjcEkvr5l9sesvV94ToxjnsumVVrQ_T66H-m4gvjTD84Kamva_FNusCSYKX4L2iRneOLbsGDh86SSCfstI5ygXyn26c1VDeS4iTBHqeiaxLeUqfCUpqUFOURDENxg6txyFL08MR0psTKZh4Wpo5vnvB1UCm-Gznwu8hLgIiG2IrsYdP29g_tfglPFsj3Ly15tohSuNwQO5uM24Yjr4VT8WtKSc9T_mKzrv49wPvoFfMxCpPnlqQBexop8wT9evE4fWwFBSTlIyXnicagh1bIVZFBWLocJN0ozUeOSX8tTlfNjGydQEzbmXvI-5fWJ_7IGmc1Fl8_h403gR2-GW0tPYR9N8rfFlKDjOvZi3_OKQB2Gt_EXxEPnESRhAU9JcXbUWL5JP6jgPTII7u70RV51gOUoF3ldD9bZQoEpsMd9MLp9R66IUj04UAUMqR96AkuqAY6TDiu6Zf1BaWaqGpaday9MgLHz8QKNPgK8r0FbqwU16Cl1ifkcZlxf81QNc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de2f5f8c0.mp4?token=eNR70mRKKpc8gRNvdX16K051-ZoE5hrNDqwZDmPQbj962GzQBXuzusToF1c-DRpCxrIWOpAITqtSG_7LHc_5J9lrg_kRTO9XHga1Km4sxcHy4_eWCj2cbJIO0NyHrHUmB5b9Q3zYH0uWojYeSe8BrQZ-8E-hs1HliCQ2JuF8E1filjcEkvr5l9sesvV94ToxjnsumVVrQ_T66H-m4gvjTD84Kamva_FNusCSYKX4L2iRneOLbsGDh86SSCfstI5ygXyn26c1VDeS4iTBHqeiaxLeUqfCUpqUFOURDENxg6txyFL08MR0psTKZh4Wpo5vnvB1UCm-Gznwu8hLgIiG2IrsYdP29g_tfglPFsj3Ly15tohSuNwQO5uM24Yjr4VT8WtKSc9T_mKzrv49wPvoFfMxCpPnlqQBexop8wT9evE4fWwFBSTlIyXnicagh1bIVZFBWLocJN0ozUeOSX8tTlfNjGydQEzbmXvI-5fWJ_7IGmc1Fl8_h403gR2-GW0tPYR9N8rfFlKDjOvZi3_OKQB2Gt_EXxEPnESRhAU9JcXbUWL5JP6jgPTII7u70RV51gOUoF3ldD9bZQoEpsMd9MLp9R66IUj04UAUMqR96AkuqAY6TDiu6Zf1BaWaqGpaday9MgLHz8QKNPgK8r0FbqwU16Cl1ifkcZlxf81QNc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، مدال ملی علوم را به سرگئی برین، مدیرعامل شرکت آلفابت، جنسن هوانگ، مدیرعامل شرکت انویدیا، ایلان ماسک، مدیرعامل شرکت اسپیس‌ایکس، لیزا سو، مدیرعامل شرکت AMD، مایکل دل، مدیرعامل شرکت دل، و ساتیا نادلا، مدیرعامل شرکت مایکروسافت، اهدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/151687" target="_blank">📅 21:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151686">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ : امروز، به طرز عجیبی، مخاطبانی با هوش بسیار بالا داریم.
🔴
به طرز عجیبی، این موضوع بسیار خوشایند است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/151686" target="_blank">📅 21:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151685">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ : عموی من، دکتر جان ترامپ، از طرف دولت ایالات متحده ماموریت یافت تا گزارشی درباره نیکولا تسلا تهیه کند.
🔴
آنها می‌خواستند بدانند: آیا او واقعاً وجود داشت یا نه؟ آیا او یک نابغه واقعی بود یا نه؟ عموی من، پس از مدت کوتاهی، به این نتیجه رسید که او یک نابغه واقعی و بزرگ بود و از هر نظر، وجود داشت.
🔴
در غیر این صورت، باید نام شرکت خودروسازی را تغییر می‌دادید. حالا، اگر من این گزارش را تهیه می‌کردم، ایلان، ممکن بود بگویم "او آنقدرها هم خوب نبود."
🔴
اما عموی من، شخصیتی متفاوت از من دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151685" target="_blank">📅 21:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8eaa0146.mp4?token=QMRyKFE8uTmLEqZk-NXDTqbjKgKIoZXm3QCf7tQ3PKpGupcMf2DB3aSr4XcePziNwO9NQeAqTe8WIKEhUE2eDYq_XIvMxoUOIe5qnosF-amqiAC7vrx5XZf-TKeFAGh0nISUteqYIHDNQMpJBgY9xnNf9ykzogewcZcUSyXMI8y9mgytteNdtyUWkufc5x2JI03Fq7HQjOePgC6zuFh4EQIxzZHHLJukZI656xDdEExPgVHAFtiYvqY0gOYI6GFTnP1-K-DLsh_TH_e7w4KzCmHYDEbIiNf6q0XoWuNU7rMKmZdAAUuFGYBjtwguetKQ_poicmN4uVkSww2wud6a6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8eaa0146.mp4?token=QMRyKFE8uTmLEqZk-NXDTqbjKgKIoZXm3QCf7tQ3PKpGupcMf2DB3aSr4XcePziNwO9NQeAqTe8WIKEhUE2eDYq_XIvMxoUOIe5qnosF-amqiAC7vrx5XZf-TKeFAGh0nISUteqYIHDNQMpJBgY9xnNf9ykzogewcZcUSyXMI8y9mgytteNdtyUWkufc5x2JI03Fq7HQjOePgC6zuFh4EQIxzZHHLJukZI656xDdEExPgVHAFtiYvqY0gOYI6GFTnP1-K-DLsh_TH_e7w4KzCmHYDEbIiNf6q0XoWuNU7rMKmZdAAUuFGYBjtwguetKQ_poicmN4uVkSww2wud6a6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: می‌خواهم به شرکت اسپیس‌ایکس بابت بازگشت ایمن فضانوردان مأموریت شماره ۱۲ از ایستگاه فضایی بین‌المللی، که چند ساعت پیش اتفاق افتاد، تبریک بگویم.
🔴
تصور کنید اگر همه چیز به این خوبی پیش نمی‌رفت؟ آن لحظه خیلی خوشایند نخواهد بود. فکر می‌کنم شاید ایشان اینجا نبودند.
🔴
شاید شما هم اینجا نبودید. اما همیشه برای ایلان ماسک همه چیز به خوبی پیش می‌رود، نه؟ ما به شما افتخار می‌کنیم، به شما خیلی افتخار می‌کنیم، شما یک گنجینه ملی هستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/151684" target="_blank">📅 21:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151683">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
العربیه: علی رغم توییت امروز ترامپ، سنتکام در آمادگی کامل، در انتظار فرمان ترامپ برای حمله به ایران قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/151683" target="_blank">📅 21:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151682">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
الحدث: میانجی‌ها از ترامپ خواستند پیش از هرگونه حمله مهلت بیشتری به مذاکره بدهد
🔴
تغییر لحن ترامپ در قبال ایران به معنای دستیابی به پیشرفت یا گشایش در مذاکرات نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/151682" target="_blank">📅 21:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151681">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا نام ۶ فرد، ۲۷ شرکت و ۲۲ کشتی را در فهرست تحریم‌های ضدایرانی قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/151681" target="_blank">📅 20:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151680">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj7VF143KHXzBTQf9YYcSUF1Glbzwq7i_PQVoQPSDSLUtlMLROFOB6fxS2rSlrXCyADM5mUcYGFfLmqIfwr55UHFc8fInEl5cpHMn5Q_jKDby5FGbLq57JLl7r7tFrZBR_gSTpa2QmeNi81Uyw5glaQpx7ZzSIBHFw3jwqQkiLbgEKcj0Dz_878cIRTGUab9aX7cBQqyiHpu_e2BcqBsZohx7k4AzHDEpl9CcFZ2ZZ4yh_n75dBJ2Bwk8IRjnqMiJoILDZ197q1-chViw5yav6-hoQJCn96k7uYfqIOcR2BDAaX4xVfFgRa8i49z9tBgpmNq56peBZGDqIo21iEJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا اعلام کرده است که از وقوع حملاتی به فرودگاه ریاض مطلع شده و از شهروندان خود در مورد وخامت اوضاع و احتمال بسته شدن فضای هوایی هشدار می‌دهد
🔴
همچنین، به کارکنان دولت آمریکا که در عربستان سعودی فعالیت می‌کنند، توصیه شده است که برای استفاده از فرودگاه بین‌المللی ملک خالد در ریاض، مجوز ویژه‌ای دریافت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151680" target="_blank">📅 20:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151679">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نایب رئیس مجلس: ما خیلی وقته منتظر حمله زمینی آمریکاییم چون بسیجی های ما قراره شکستشون بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151679" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151678">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دراپ سایت: تردد در مسیر عمانی تنگه هرمز آنقدر برای خدمه کشتی درآمد دارد که انجام تنها یک سفر، آن‌ها را برای تمام عمر ثروتمند می‌کند
🔴
در هفته‌های اخیر چندین مورد تلفات جانی در نفتکش‌ها گزارش شد، زیرا باور خدمه این بود که ایران فقط موتورخانه کشتی‌ها را هدف قرار می‌دهد
🔴
با توجه به دشواری کشتی‌ها در یافتن دریانورد و خدمه، انتظار می‌رود انتقال نفت از این مسیر به طور قابل توجهی کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/151678" target="_blank">📅 20:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151677">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=K4XW4AiNc7jEJld4bXXW8HaX71M42rxA0BWsgP27gZOb3neveuMiyRZurxPFLCdhjngMbJDpwv0lzAtBRq5CN8q63a8XqEcZV_QqF1R2sdtOSmsxVH0tHVB-4aoBiXON-fAcgTGAksDv45NUnC466UENxpiJ6_nW74FSTPczVTlBPD0bbYSianzbLAu_0Mo93sOTf10D3VWOyIk-McvZTKHku9TUOhDK56aaMjXg0Sj6YTdaLdkIOaPNI278oR0r792wGf9T4n7_z9A-FOAMf0MYcy4-N6u0orlBd_0ORXKfBF9uSkeJyFYUaen31eQ3JfQdasPQ2uFMDE_OLj4_IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=K4XW4AiNc7jEJld4bXXW8HaX71M42rxA0BWsgP27gZOb3neveuMiyRZurxPFLCdhjngMbJDpwv0lzAtBRq5CN8q63a8XqEcZV_QqF1R2sdtOSmsxVH0tHVB-4aoBiXON-fAcgTGAksDv45NUnC466UENxpiJ6_nW74FSTPczVTlBPD0bbYSianzbLAu_0Mo93sOTf10D3VWOyIk-McvZTKHku9TUOhDK56aaMjXg0Sj6YTdaLdkIOaPNI278oR0r792wGf9T4n7_z9A-FOAMf0MYcy4-N6u0orlBd_0ORXKfBF9uSkeJyFYUaen31eQ3JfQdasPQ2uFMDE_OLj4_IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت غذا تو یکی از فست فودی های مملکت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151677" target="_blank">📅 20:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151676">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
طبق گزارشات، پلیس کنترل شهرهای بزرگ فرانسه را از دست داده است و انتظار می‌رود که ارتش فرانسه برای برقراری نظم وارد شهرها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/151676" target="_blank">📅 20:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151675">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcZneHbN4FgfhnBMbv22qMmYXvkgLfAziA2zgGKSTLlMfJXuR0sm2YBl2dvjMn0pN_pM39nrWVTG4C3uNxpVQZBCO4BL1DZbwfoFqf7TEiOVbUuCemYYAk7nt3GL7HkMIo-WnhHleW0SSR16HxmWGN9rhi-DNMotjTuJ1d36ngpvy5snnUdLBrIy473VzdGpUsBFhH0se7mXJMylXSo24j58Vd1VnTJ_YRf8OkBUOM295ylHI8DlxY-6Utfdswq791wwIU1H9ol6TwlhKMseRrozA33P5mMHSjpIQmkSLAqZSOyF-NjITsHYoSCqoh6GQ91SmiBg6b5t11nZVw8ZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزمایش موشک هایپرسونیک Blackbeard آمریکا از لانچر زمینی
🔴
این موشک ۵ الی ۱۰ ماخ سرعت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/151675" target="_blank">📅 20:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151674">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4FmqBK1aiWF-Pt4dudKfn8mTbueI2elQ7v6Mptp55BhEKLSI3DgoUMzXoCWR3DFyFAKzv5aJEnx82PyM0DI1VLeF-02X_k2Z-dLEUGzJT1zHYt7cZzPLquZgLYbB9dz5yR4VU1kMlm3GKwyfymk3bb7r7H6k1_8ae_iWBZoGmZw4ySUz-PME04UQjTQxFuxLBQoS6oqGzDdhAPMaqo2qYAzxaGGITUdgN-ZfE_1d98A--BH82wO8TveigAK8qyK6zCGUZu8upY8CbIgxL8pOCI6jcB-3u97pjV5z__gGbWHE7_wxFbRZHr9Qa7pPxZMoPiVeDXFFkfbSXGrKlHrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش خلبان جنگنده میگ ۲۹ اوکراینی پس از انهدام پهپاد روسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/151674" target="_blank">📅 19:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151673">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRtibgBnZXF6jVnOKwdMOKE7QvqVBAajdcYxyRIVAQ_wUD7zvGYTi_n4_1wHEhEOTJv79N2Pjww9zJA-Gf2Q0KMCSu6PXzUOSGQrjOk8rDiRjylurLbeNoGBmMPsXwypmp-q1IEPO-u5PDrggak8UcwBXVTNs46aWeuUbLdsmQ_UR-fVVkOmAVH0LaenwkX5YkUR18zryYg0emojClSnFcAnyBnh4ifVNIbNw1Je5XzNcZe6kkDZ_jIBCgZdpq-t4J2LFj8hzXssWMHki2l_z_R0DKhKt3NGimL_SMoahvtcomZMGT3E6oC9Am7auZjU3Qnl7QUPhSdszYKPy6-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : کاخ سفید هر کسی را که از عبارت "هوش مصنوعی" استفاده می‌کند، در حالی که عبارت جدید و دقیق‌تر "هوش فوق‌العاده" به طور گسترده پذیرفته شده است، به عنوان "دشمن" تلقی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/151673" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151672">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D32ZT3oviEdtycZaZ2IhXXBdgJpddZ46sUYuRrkSdTNEwPIkLzZI55-H_7XkMQNOpr-UgB52rNtEumL1dFcoopodrIjEKUFxjikYhG8uEOXYzfjsDdjuZV1goSckYZTfBTLl9w6LMFRbev5wYvUcRuMUeCESzOitJmmK-CBXGuMENAeuJOFI9Kfb74AjQogYzrTe0UL3rnin5RmenV3qBp3a1ECe1_2-gG9-8ZtERryUyudoNVqnIi1hea7WtOWCtpIjoS_2ZWycRtjiW0W_4ZGlJpqQMXfRuXfQpT_7cC97DAf_5Bu5smEx7QkjJ5DSehOg6eSvfOF79DOwaPk1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
🔴
می‌خواهم به همه این موضوع را به وضوح بگویم که، در حالی که ایران از نظر اقتصادی و نظامی در وضعیت بسیار نامناسبی قرار دارد، و در حالی که تحریم‌ها به طور کامل و با تمام قدرت اعمال می‌شوند، و در حالی که حجم نفت با رکوردهای بی‌سابقه‌ای از طریق تنگه هرمز جریان دارد (دیشب به تنهایی، ۲۲ میلیون بشکه، و هیچ یک از این بشکه‌ها از ایران نبوده و به ایران نیز نرفته است)، ما در هیچ زمانی قبل از انتخابات میان‌دوره‌ای که در سوم نوامبر در ایالات متحده برگزار می‌شود، به ایران حمله نخواهیم کرد.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/151672" target="_blank">📅 19:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151671">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۴عبری: مقامات ارشد سپاه خواستار حملات به اهداف مهم در منطقه طی سه هفته آینده شده‌اند. این درخواست با این باور مطرح شده است که دونالد ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151671" target="_blank">📅 19:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151669">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr5pciDeG9-lb1_-uZUgmaAaw4bzumECFcH1mdwW3AzGgEWNrjLspAzJKIseMdteN9iZa43MZ_uXx8UtPGDo8ENkQuWNEnAtPjg0FaoO66BHOfrH1-es4AEaFZ5Nb2jmvJvVfunU_y7eTflz2OJTTR2jbdlSiL8jWteWaYnDH8clRt5OUvf_d4yKYZ8o1YLIede36rVrj5NNyvkJ9uXsgPxaGt87FNYlgnss8lc6YQHkjCemX5Q6qDFI0lqmsGJ_1BJV__e-sZpFADQKX6gOqncF_i7uzBd4ckZr4fZWhHcfkJFZ6tN_cTPsC8a5sot3KzeDuoGr9TJubKPaqMdf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b42cc54c6.mp4?token=tam3t_YNmT8qWmyRMLBZ4xJEXe7I1iiaO_CZBHfLsN65pkZwgD3rZBK8WHKxIgibDNgDhpJCpBXDfTUX6zZ71qyJHRGkeCl18hysZJBYei4HQoGcRNH466jhIufJp42VniA5gf0bDLv-tQnTcba8s4f-BmQFrhcN1L5rtq_nzBLC58JMHuMF--Oqyh_GscM1tQdfh70PPfplS7zxBojQZjdbGv6froTd2y27RIv6Zl53V0lUNa7ydLN1c7bWrMLBZ5GJwKaQjowb4GtJKOhD0IVxzcHNgB0eZER26NzVOsSIMw4cmr_4Kb2-8_KBxKzNZ3yz8pb6w5I4dikwghWFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b42cc54c6.mp4?token=tam3t_YNmT8qWmyRMLBZ4xJEXe7I1iiaO_CZBHfLsN65pkZwgD3rZBK8WHKxIgibDNgDhpJCpBXDfTUX6zZ71qyJHRGkeCl18hysZJBYei4HQoGcRNH466jhIufJp42VniA5gf0bDLv-tQnTcba8s4f-BmQFrhcN1L5rtq_nzBLC58JMHuMF--Oqyh_GscM1tQdfh70PPfplS7zxBojQZjdbGv6froTd2y27RIv6Zl53V0lUNa7ydLN1c7bWrMLBZ5GJwKaQjowb4GtJKOhD0IVxzcHNgB0eZER26NzVOsSIMw4cmr_4Kb2-8_KBxKzNZ3yz8pb6w5I4dikwghWFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر نشان می‌دهند که یک هواپیمای ثابت متعلق به خطوط هوایی سعودی در فرودگاه بین‌المللی ملک خالد شهر ریاض، در یک حمله موشکی اخیر توسط حوثی‌ها (انصارالله) مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151669" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151668">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIEQd0FrfAog4QPya2910RvY_ia9O081AAUJih9bji_n9a4jOuTHmDB8_yqjN4sfv27goRIGlephqfgXKSh1z-phky9OJG_rQtNC_etCoE5QDbeYib2eVfABUoyvr6aG6Toyi76hCnc5njoGOxsgRKO4OlAcgii457QCm9N1m2xgkmrOrrpv6qqKJh4Eb5HmjaT7MOIbjelq0K7zq_301upnjJmd-pc3E1pPesyy-xCYACxvxQS1f7Ym40Cs-eI4EWzc8IkeqLJJr6LH0o3nn3XTjeThH3h0D_fzMNwmb0mQIXwSvWqrSBJqAHgqTbnFEsuGlCItVmyNz3oga6IPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سهم قطر از صادرات LNG جهان به ۷ درصد کاهش پیدا کرده سهم آمریکا هم شده ۳۱ درصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/151668" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151667">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzCsLpXBm48PSZXJeWssvFVxtjkcjHv-POKMdu88UBfgE24tkDKH0Ezr-ffRgzXNGr_dL2Id9PC0E-tKfQDXN33mHPmpIJgc97uiXAg36zyMGUfOkITkT8aOokuUZLHxsgLGbgMKk83xTBpErys_OG8PdLHk9HzUaLe1pvxO8jJq22SO22M1URTvdZdvyKZIbemyWwBd-wS_qCpKXqIcY6nI3nwRUlmBkglORHpLeCVw-YN-FdELYWXBHzftiahzj-DpQey-6vqWJYGx8q8GtRHqTmaxf1ZKv_8ViHxrJI7ztodK_kaM2t6SGJCiAlJWG_w7s9nYgJatJgHdDNBozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیما از نیرو هوایی پاکستان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/151667" target="_blank">📅 19:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151666">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=boqNhjJu7YD4eCQQLLXJOMAYIA538ecw6P6kKQkius8RH1-kaOPDkfBpTw4gKP664h-k4P_PctXC6LpMRaMjfK3zXQ-cPJhGQGh1y-2z64zGGtLe47kndBnz_mm9B_4QUoN0XT0L6gWdIAlqFQcJ8_rj4VHGR7IV9_c6wxlD5drI5ayOKkg72oX7I33tz2aHCNpkLbGd4KIZ6fZ3iNSp8DChOx0sw_r4lsaN1qC4rJkdnRf_Z7nswVb0rXJGiow7eVEXXm9xzpg2vtK_ZJbpWQ1O8ea6aeMBeEuxdlexLeru8f1RIP4F6EWy-UYqsM9QsBSlQBywnSFSfNyHzKBUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=boqNhjJu7YD4eCQQLLXJOMAYIA538ecw6P6kKQkius8RH1-kaOPDkfBpTw4gKP664h-k4P_PctXC6LpMRaMjfK3zXQ-cPJhGQGh1y-2z64zGGtLe47kndBnz_mm9B_4QUoN0XT0L6gWdIAlqFQcJ8_rj4VHGR7IV9_c6wxlD5drI5ayOKkg72oX7I33tz2aHCNpkLbGd4KIZ6fZ3iNSp8DChOx0sw_r4lsaN1qC4rJkdnRf_Z7nswVb0rXJGiow7eVEXXm9xzpg2vtK_ZJbpWQ1O8ea6aeMBeEuxdlexLeru8f1RIP4F6EWy-UYqsM9QsBSlQBywnSFSfNyHzKBUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه برخورد صاعقه به دکل برق فشار قوی در رشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/151666" target="_blank">📅 19:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7666e6713c.mp4?token=XA9GZTFYXqlUONsbuq5Oxr0BjgYBJrJ-ep8qV1RhMeONetbOjd9s3wrXH2y3Jm8wzjOF_10oHWpu_BPF9iQtAK7orwCSPrpa2JBrm5j0OI-ayP2k2kjnVUqhdup880O4ATXI4jcRt3h-I0-X3nsDSCw1xWy_JwWEm0dFYk8fs5oW2qNnmW2bDd3eAhHpJ4mPeK792HOj9KC5AZO88ICbHwGwbqAugm_GPhrgd2Bpix_so4P63s-jILt7pmuEIx3opaFjGfi49wvOTV9VKqlNx5LgSNsLkAr7Bey0-FZUxTX16fKgSEhEObrm1gJaYbf8XF9uGpFT0ze4vf3ZUbll9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7666e6713c.mp4?token=XA9GZTFYXqlUONsbuq5Oxr0BjgYBJrJ-ep8qV1RhMeONetbOjd9s3wrXH2y3Jm8wzjOF_10oHWpu_BPF9iQtAK7orwCSPrpa2JBrm5j0OI-ayP2k2kjnVUqhdup880O4ATXI4jcRt3h-I0-X3nsDSCw1xWy_JwWEm0dFYk8fs5oW2qNnmW2bDd3eAhHpJ4mPeK792HOj9KC5AZO88ICbHwGwbqAugm_GPhrgd2Bpix_so4P63s-jILt7pmuEIx3opaFjGfi49wvOTV9VKqlNx5LgSNsLkAr7Bey0-FZUxTX16fKgSEhEObrm1gJaYbf8XF9uGpFT0ze4vf3ZUbll9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تظاهرات ضد سربازی اجباری تو اسرائیل که مشخصاً اکثرا یهودیای متعصب مذهبی و طلاب هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/151664" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وال استریت ژورنال گزارش می‌دهد: بین ۲۸ سپتامبر تا ۴ اکتبر(۶ تا ۱۲ مهر)، ۱۰ نفتکش در تنگه هرمز مورد حمله قرار گرفتند که بیشترین تعداد حملات در یک هفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/151663" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151662">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43f0ec404.mp4?token=DHwUGFko6uZI1GFeaAA40uAwdYh2KHKdweqbD6cK9Ml3iykfxxyne2lOCW2QraqcqrXS2Cl3llIdm07un0x8cchykL8Rt5D4h0PCW2uFuFdYdrFnAmlFhJvK7hlhIl1SJdxVS7iWlY880fy37-URmkHXZlnEjDiZuMLu7E83P64HV97wolx70Ldig18dkte0SzGB7i-RMx0Tnuz3LeMyK-fOgRF-3C7iCSwTNKmWJXmDvihojTL9EiSqKkWFUiZkcPjKfmSzCqg1-JvQU528pf6RKfH35btSBJXznSR9KnDeUqHCDA8O4wn08hPFogbJh8dfOcEzIGopd9TZE2AbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43f0ec404.mp4?token=DHwUGFko6uZI1GFeaAA40uAwdYh2KHKdweqbD6cK9Ml3iykfxxyne2lOCW2QraqcqrXS2Cl3llIdm07un0x8cchykL8Rt5D4h0PCW2uFuFdYdrFnAmlFhJvK7hlhIl1SJdxVS7iWlY880fy37-URmkHXZlnEjDiZuMLu7E83P64HV97wolx70Ldig18dkte0SzGB7i-RMx0Tnuz3LeMyK-fOgRF-3C7iCSwTNKmWJXmDvihojTL9EiSqKkWFUiZkcPjKfmSzCqg1-JvQU528pf6RKfH35btSBJXznSR9KnDeUqHCDA8O4wn08hPFogbJh8dfOcEzIGopd9TZE2AbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور:
به نظر من ۹۹ درصد از شهروندان آمریکایی وقتی به فردی مانند ایلان ماسک یا لیسا سو، مدیرعامل AMD نگاه می‌کنند، می‌گویند: بدیهی است، اگر آن شخص بخواهد وارد شود و چیزهای بزرگی در آمریکا بسازد، ما از او حمایت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/151662" target="_blank">📅 19:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
شرکت‌های هواپیمایی ایر ایندیا، ایندیگو و ای‌آی اکسپرس، پروازهای خود به ریاض، عربستان سعودی، را تا تاریخ ۱۰ اکتبر لغو کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/151661" target="_blank">📅 18:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی شرکت هوایی لوفت‌هانزا:
پروازهای لوفت‌هانرا به ریاض را  تا پایان روز ۱۶ اکتبر به حالت تعلیق درخواهیم آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/151660" target="_blank">📅 18:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060004b037.mp4?token=A9KJNUXwfGX9N_XK3x5JpOxxAijLbcegw0sGS6e-WzuDqIKqhtOREIM-bBRXBD7u6fUAzlWczgRSEijEunhrKj08diiBhiyKZMoNUs4sFG60zctLWbJc5jUy0TqNHfSBugOnJK0GuqQ-df5Qjr9Cx3LTI03VytHv5hkOSNWIh8xHlLYfZSC7_dVFsIMdD-XqgwA4gWw-s2gMTagVrpnVEDSZfgz5Pj6fStJfoB0nC9giEZRoLVJ_hj9TQBZe5eTQ0m5MeKQ0gjvp68xftB43m1exP5wz3cZ43zRqAOPqDTdG-Wv7k9hPStkeZI5NGmXNdu1oEp1b2Xvt3RopEHd8dzR2afGbd1Xc5vBbWVTRmoIpTh4q3UmmPZJEpKYkOr4xfWWNZlxWJGUKSgQI3OnqWtPZgYmoJZZ6Z-KrI-_SQzaBmIOQuchka6Vmd3BzNXL9fwhBWdGN54ufShxUqs6_hq1pIglEY9Qh_65VQ2VNMCf9LRiMzZ8B8MyxKZ9lUnu-z8zFcsZz0cPi5nLjx2chp6_gfxYdoLTlZVuH0zcIOG8j-BLMe5N2-zYdZDSx-cLdPUNe_hTkhj9sHymPXTfBxSx4hQiJKwcUbMJ8eE2tMf6aIYrBmB6iYCs7j-r-3SG8AyfExIcHTMKtOXyVWgEm5c8eu8O2K7cC7q-X6qkoiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060004b037.mp4?token=A9KJNUXwfGX9N_XK3x5JpOxxAijLbcegw0sGS6e-WzuDqIKqhtOREIM-bBRXBD7u6fUAzlWczgRSEijEunhrKj08diiBhiyKZMoNUs4sFG60zctLWbJc5jUy0TqNHfSBugOnJK0GuqQ-df5Qjr9Cx3LTI03VytHv5hkOSNWIh8xHlLYfZSC7_dVFsIMdD-XqgwA4gWw-s2gMTagVrpnVEDSZfgz5Pj6fStJfoB0nC9giEZRoLVJ_hj9TQBZe5eTQ0m5MeKQ0gjvp68xftB43m1exP5wz3cZ43zRqAOPqDTdG-Wv7k9hPStkeZI5NGmXNdu1oEp1b2Xvt3RopEHd8dzR2afGbd1Xc5vBbWVTRmoIpTh4q3UmmPZJEpKYkOr4xfWWNZlxWJGUKSgQI3OnqWtPZgYmoJZZ6Z-KrI-_SQzaBmIOQuchka6Vmd3BzNXL9fwhBWdGN54ufShxUqs6_hq1pIglEY9Qh_65VQ2VNMCf9LRiMzZ8B8MyxKZ9lUnu-z8zFcsZz0cPi5nLjx2chp6_gfxYdoLTlZVuH0zcIOG8j-BLMe5N2-zYdZDSx-cLdPUNe_hTkhj9sHymPXTfBxSx4hQiJKwcUbMJ8eE2tMf6aIYrBmB6iYCs7j-r-3SG8AyfExIcHTMKtOXyVWgEm5c8eu8O2K7cC7q-X6qkoiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه بریتانیا، اد میلیبند:
امروز، ما تحریم‌های بیشتری را علیه ماشین جنگی پوتین، ناوگان مخفی، شرکت‌های نفتی، ارزهای دیجیتال و همچنین تأمین مالی جنگ اعلام می‌کنیم.
🔴
ما خواهر و برادران شما در این درگیری هستیم و تا زمانی که لازم باشد، در کنار شما خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/151659" target="_blank">📅 18:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f0003b79a.mp4?token=AsoMlAU3Dyj35fWzs3j6VcYZ-zCsxAfd3__TMcbeRgdLOp7OlS6ouV2APCNUwd5wYjEUQJjlszTCRVV95-HIimTIdmBsDFtxqzjVqQz7nAYSQbiaPjO7GJ7K9_LMTNN19xzFBuULT_5imMtcaTviCHTAfsic78tLZOhnBKr--vhrkwreaOY1zyDkFDFMS0xB6xBQRf7tTguy4VM2H4Iidiy5M3dLdHZMoLE7yUvSMsONwA5Mui8CD9rEgK5BiF740MPg0mvFxsIkqCNoi_rdiM14ww2DUGbNhH856brf5T-ZA-00DMq6EsvuUo_UrrOoM2vvTpD_X9WPR57JYFcCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f0003b79a.mp4?token=AsoMlAU3Dyj35fWzs3j6VcYZ-zCsxAfd3__TMcbeRgdLOp7OlS6ouV2APCNUwd5wYjEUQJjlszTCRVV95-HIimTIdmBsDFtxqzjVqQz7nAYSQbiaPjO7GJ7K9_LMTNN19xzFBuULT_5imMtcaTviCHTAfsic78tLZOhnBKr--vhrkwreaOY1zyDkFDFMS0xB6xBQRf7tTguy4VM2H4Iidiy5M3dLdHZMoLE7yUvSMsONwA5Mui8CD9rEgK5BiF740MPg0mvFxsIkqCNoi_rdiM14ww2DUGbNhH856brf5T-ZA-00DMq6EsvuUo_UrrOoM2vvTpD_X9WPR57JYFcCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
🔴
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/151658" target="_blank">📅 18:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqbVrBtcexHPNpFEsGjJf-Q687-1sEJg-q_bFNqnm_1cbRpaef_4hhd698h8r_XOBPkCGrgcxhJm4dE39hbrLHb5jit9XRRqw5rM9C872YBCwAtcjeRX5XYoFn70KCAcNM4ARQd7ORQTKbpq6F3HuR2Ar8hOFqE2rkSmqUEy7TuCk1aiFRgX1pgeICx9K0t7PtXAjQzguI9JUWQh6nItkyMm5iU3xQzKN-ZFSwtYkY1wGfxJm7vq1rveDEWy0iy9oHX4mVLcu4dxFwc1RzxsE9BbUr4noxXjlZebsOk_Si76ZHkOYBSLyNJH8IgvDdk8snRYgNy8QnA9YVi1Puja7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیکلاس مادورو، رئیس‌جمهور سابق ونزوئلا، در یک کیفرخواست جدید که روز پنجشنبه منتشر شد، به اتهام شکنجه و سایر جرایم مربوط به نقض حقوق بشر، مورد پیگرد قانونی قرار گرفته است. این اتهامات به اتهامات قاچاق مواد مخدر قبلی که او با آن روبرو است، اضافه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/151657" target="_blank">📅 18:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2HMfbqgyiRV06817BDL_IhE0-vLPgjzi_az74H47CoxMNBL_JVEy5RPcGgUodNhUNA5fV_q4b4MSnKAQpuEpWMZ4lMssBunMJDoM5aDoXk2z8Uii7l_QYvlhL6Lh_OpEe_ao2TUBni97WCYWGkDpu2UwL-KWxiYOuQSTiQEh6nU6GBk-4w487XsKRXTmkEk-Iiw7xZhwBFPqsrmUGhy65J0xNU6BWxItzUMSgqtQ29GYUf9cO1xvCpy8nlfwyvdrTV9klRtabUaf1MtISc7FdxQ4_7NkEPM_RpQO4NMFhv3t8VeQlTA9CqpVquMJkqcR_6-Xn6ZHgr7cBe_ADvb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
امروز، فرماندهی مرکزی ایالات متحده در یک جلسه مجازی، شرکای بین‌المللی حمل‌ونقل دریایی را در مورد تنگه هرمز آگاه کرد.
🔴
رهبران، بر اهمیت افزایش تلاش‌ها برای تضمین آزادی تردد دریایی با افزایش حجم ترافیک تجاری، تاکید کردند.
🔴
آدمیرال برد کوپر، فرمانده فرماندهی مرکزی، از رهبران صنعت و سایر سازمان‌های دولتی ایالات متحده به خاطر حمایت مستمرشان تشکر کرد و به فداکاری‌هایی که خدمه غیرنظامی به دلیل حملات غیرضروری ایران متحمل شده‌اند، اشاره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/151656" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182d6999c7.mp4?token=VYvNUV6-kuaXCO98e8D60aEdLMd49czPm922glTHuwtlvgpfE4l_n3HWub17G57pPkQ96vSmr7lMND7d3yDb5rEcMnYXMLN07I-nkAjHx65EwjZm3bOq7kdkLPSTR8S-PdyMx0vB7K_a-KIDfLYo__9iDYYmd2IdSS7sdzS9CUAIQCp5qkpDKYDLYfo0yutrz8N0nq3ulqiVpT9AzOp1TcVCeSdsiwdWba4BQ3vX1tDrJCEEVEEuGJYvkW1ccB4EA5V7HFMrxRlzyHOUHT53nUl8jIhqgDJbK36WLQamvgsvJjhxanE7yky59juWoJXUkQGL3BdX_xZsW4baEV86gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182d6999c7.mp4?token=VYvNUV6-kuaXCO98e8D60aEdLMd49czPm922glTHuwtlvgpfE4l_n3HWub17G57pPkQ96vSmr7lMND7d3yDb5rEcMnYXMLN07I-nkAjHx65EwjZm3bOq7kdkLPSTR8S-PdyMx0vB7K_a-KIDfLYo__9iDYYmd2IdSS7sdzS9CUAIQCp5qkpDKYDLYfo0yutrz8N0nq3ulqiVpT9AzOp1TcVCeSdsiwdWba4BQ3vX1tDrJCEEVEEuGJYvkW1ccB4EA5V7HFMrxRlzyHOUHT53nUl8jIhqgDJbK36WLQamvgsvJjhxanE7yky59juWoJXUkQGL3BdX_xZsW4baEV86gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه بریتانیا، اد میلند:
امروز، ما تحریم‌های بیشتری علیه ماشین جنگی پوتین، ناوگان سایه، شرکت‌های نفتی، رمزارزها و تأمین مالی جنگ اعلام می‌کنیم.
🔴
ما برادران و خواهران شما در این درگیری هستیم. و تا زمانی که لازم باشد، همراه شما خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151655" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474de313f9.mp4?token=kRvaEU_IKNZ4gKwnDAYS98vnn58W7hWSZR523e2glGFV6QBJ9Lcrenf79SGjLh65UQA_8tgpSYy7Pbt-sfvWeyRbMev6ZFckGvuLfg_5L9D7Pt0EsPIV4bE0wQnL_LvAVFhBGJamBfTO1B_huZufny07Iw_Y7Ub8McoVv7O3i1e2OgmqYeoW2DzdPdFKgimolZOJwlpIMNEq4mrEso7j1UjCUoYAXXtfjJCyozDduLgEf-Ux-nYbJTXQaDVt8x-syWFnSGtxAY3sQc1_qHAJY4apqhzoQiZ_x5nw_9oO92m3LXOw4Ko-sp3OQ2zVhUEdjEdERMoEDyvUns8Xk2AlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474de313f9.mp4?token=kRvaEU_IKNZ4gKwnDAYS98vnn58W7hWSZR523e2glGFV6QBJ9Lcrenf79SGjLh65UQA_8tgpSYy7Pbt-sfvWeyRbMev6ZFckGvuLfg_5L9D7Pt0EsPIV4bE0wQnL_LvAVFhBGJamBfTO1B_huZufny07Iw_Y7Ub8McoVv7O3i1e2OgmqYeoW2DzdPdFKgimolZOJwlpIMNEq4mrEso7j1UjCUoYAXXtfjJCyozDduLgEf-Ux-nYbJTXQaDVt8x-syWFnSGtxAY3sQc1_qHAJY4apqhzoQiZ_x5nw_9oO92m3LXOw4Ko-sp3OQ2zVhUEdjEdERMoEDyvUns8Xk2AlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان و باران هم‌اکنون در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/151654" target="_blank">📅 18:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
برخی از منابع عربی مدعی وقوع چندین انفجار شدید در تنگه هرمز شدند
🔴
برخی منابع رسانه ای از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/151653" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
شرکت Kpler گزارش می‌دهد که برخی تولیدکنندگان نفت در منطقه خلیج فارس
ممکن است به‌طور مخفیانه به ایران عوارضی معادل ۱۰ تا ۲۰ درصد از محموله‌های نفتی خود پرداخت کنند تا در ازای آن، عبور امن محموله‌هایشان از تنگه هرمز تضمین شود.
🔴
این ادعاها هنوز تأیید نشده‌اند، اما Kpler می‌گوید چنین توافق‌هایی می‌تواند به توضیح این موضوع کمک کند که چرا قیمت نفت خام برنت همچنان در نزدیکی ۱۰۰ دلار در هر بشکه باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/151652" target="_blank">📅 18:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc65671ac5.mp4?token=vcctH53XkBEmsdUUpTsagURk2fA8sNV1rvh8JUQ9OCLmTOtupWVXvwhEVt9058I6XG7VAi8Kl0x8HjoaQNlNQicmO9JJVFTW0ExtUhpSrUUUtZujZeBS_T4r_tNwfJYwPFDHCOb_XebRH9gtfYrBf_BJVJ17IwAtYCHdfKU3lTWnxPh14QhARGbNz3aIen_SFA63Gip1dLFk0Z4XFzhxYGw0_PWhHQyYDUB2HjJkVab8h3iKRcz1zO3SJ_rSwv-YQy5Vo-pmOCLuKdIrJEiZyXn-5lYzbj4ivsDm3-EyzEgvCMfG7AupdvTkWf14ln4Y1DWmghei9a601coM0dHBWYxIeHO7V3tH5PGuHneybRfjyWxHPKvqZ_RQGAduU-T0pRLX1k6lDZiabSabSYX9WLwAKHK0pdzW1CcFPY6XG9vB1P-7LDZmXWIWkeo20POEKoDo-ZonvTUXOzLxpHGj6sYJfH_EMhfKKpRbNd1mkxPbCoSzeBbhSpww2u6f1Zxup-DOndsMgKqKt3Ioz-u0lJNVJ_un71VTtS2_Qb26WekXimJcpeUC40w2RwCXLmbeCY8SzBbNn8ronkV1Q9nWf8sJdV72MIAnJRfexIQsj9GmzbWuQ4_z1iQSce3aNVLKCp4f3ECUj9TXHbOKhWigBibIKAFVZtUJAUo71xpxzGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc65671ac5.mp4?token=vcctH53XkBEmsdUUpTsagURk2fA8sNV1rvh8JUQ9OCLmTOtupWVXvwhEVt9058I6XG7VAi8Kl0x8HjoaQNlNQicmO9JJVFTW0ExtUhpSrUUUtZujZeBS_T4r_tNwfJYwPFDHCOb_XebRH9gtfYrBf_BJVJ17IwAtYCHdfKU3lTWnxPh14QhARGbNz3aIen_SFA63Gip1dLFk0Z4XFzhxYGw0_PWhHQyYDUB2HjJkVab8h3iKRcz1zO3SJ_rSwv-YQy5Vo-pmOCLuKdIrJEiZyXn-5lYzbj4ivsDm3-EyzEgvCMfG7AupdvTkWf14ln4Y1DWmghei9a601coM0dHBWYxIeHO7V3tH5PGuHneybRfjyWxHPKvqZ_RQGAduU-T0pRLX1k6lDZiabSabSYX9WLwAKHK0pdzW1CcFPY6XG9vB1P-7LDZmXWIWkeo20POEKoDo-ZonvTUXOzLxpHGj6sYJfH_EMhfKKpRbNd1mkxPbCoSzeBbhSpww2u6f1Zxup-DOndsMgKqKt3Ioz-u0lJNVJ_un71VTtS2_Qb26WekXimJcpeUC40w2RwCXLmbeCY8SzBbNn8ronkV1Q9nWf8sJdV72MIAnJRfexIQsj9GmzbWuQ4_z1iQSce3aNVLKCp4f3ECUj9TXHbOKhWigBibIKAFVZtUJAUo71xpxzGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مراکز داده:
مردم معمولاً با مراکز داده مشکلی ندارند. خب، مشکل مراکز داده این است که آن‌ها بسیار عالی هستند و کشور ما را به شدت پیشرفت داده‌اند، اما باید به نفع جوامع محلی باشند.
🔴
من چند روز پیش به شرکت‌ها گفتم که آن‌ها پول زیادی دارند. کمک‌هایی به جوامع محلی ارائه دهید و این جوامع عاشق آن‌ها خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/151651" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرنگار: پیروزی جمهوری‌خواهان در ماه نوامبر برای برنامه‌های شما چه معنایی دارد؟
🔴
ترامپ: خب، فکر می‌کنم این به معنای میراث است. فکر می‌کنم بسیار مهم است. داشتن یک پیروزی واقعاً تأییدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/151650" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اگر می‌خواهید مشکلات را ببینید، اجازه دهید آن‌ها به لس‌آنجلس حمله کنند یا به مکانی مانند سن دیگو. اجازه دهید به یکی از شهرهای بزرگ ما حمله کنند.
🔴
این همان چیزی است که به آن "مشکل" می‌گویند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/151649" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=XDGzZRWkD8X0HOwa_kEGync9EaFNTeJVO7-R0GWGUMQU7fUac5nsp3IU0zWdDcrxSFzO94Cl2_Nsm0ubEoxavyzHjYaKJSBfMyEs7c0IY44-D1sf5HrOtYayA71G95wEwbJ2T-IPAJhp-nheom_l2eq94Cga9wppaayQzAZ05iTPJ5pRKeHTj1n1R78Ics4dNjUNibwrOcgus5qxDIyzvAPpzX16SnYnPBJIbRbw3cijq6Yf34s0UpBQrdQBAV7SFVpgRf9aohC6X_WJHG4eEpl5ZGmvRMXO6WCJhBG-OVeF1PPpn_XtXvFcIRziBu30F7jTvGHZVaq3UxKJpe7Zug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=XDGzZRWkD8X0HOwa_kEGync9EaFNTeJVO7-R0GWGUMQU7fUac5nsp3IU0zWdDcrxSFzO94Cl2_Nsm0ubEoxavyzHjYaKJSBfMyEs7c0IY44-D1sf5HrOtYayA71G95wEwbJ2T-IPAJhp-nheom_l2eq94Cga9wppaayQzAZ05iTPJ5pRKeHTj1n1R78Ics4dNjUNibwrOcgus5qxDIyzvAPpzX16SnYnPBJIbRbw3cijq6Yf34s0UpBQrdQBAV7SFVpgRf9aohC6X_WJHG4eEpl5ZGmvRMXO6WCJhBG-OVeF1PPpn_XtXvFcIRziBu30F7jTvGHZVaq3UxKJpe7Zug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما به شدت در حال شکست دادن ایران هستیم. دیگر هیچ تهدیدی از سوی سلاح‌های هسته‌ای وجود ندارد.
🔴
آنها در حال حاضر در وضعیت بسیار نامناسبی قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/151648" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما به شدت به ایران ضربه می‌زنیم؛ دیگر هیچ تهدیدی از سوی سلاح‌های هسته‌ای وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151647" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
به دلیل وقوع طوفان در برخی نقاط تهران برق قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/151646" target="_blank">📅 18:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd3faa3c1.mp4?token=HQvgA2wOfmsXCZ-PEnRILr2zsEpRpFbna_G3T_5blBzT9jlm39fkprV05nxl2gUbn3SgoiPf3V59pR_Bu94wgg1BC53csraUD1lMVGJfPrKOKOJZBtE50pQmCX7Ofx9PzurZeIq_JnaXZ9NQTzptFb4q6WB6jTIqH1Te7hVmkBLD5M2V1lGrSNrLyHBlbsUZ-z3KbqxaR2FZpqh0OtZ-9th687HBfeNmlesB96T4Msiuq8AbQS-TFMbl13pARQwv-c0Gkbna9Tr5Y2WlJy3RCQOKzu_tAqdtnu9SiDCVMkISuhK9eEYm_XnC1El0K0DrcbhnJGLifK6_hWh9S5nTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd3faa3c1.mp4?token=HQvgA2wOfmsXCZ-PEnRILr2zsEpRpFbna_G3T_5blBzT9jlm39fkprV05nxl2gUbn3SgoiPf3V59pR_Bu94wgg1BC53csraUD1lMVGJfPrKOKOJZBtE50pQmCX7Ofx9PzurZeIq_JnaXZ9NQTzptFb4q6WB6jTIqH1Te7hVmkBLD5M2V1lGrSNrLyHBlbsUZ-z3KbqxaR2FZpqh0OtZ-9th687HBfeNmlesB96T4Msiuq8AbQS-TFMbl13pARQwv-c0Gkbna9Tr5Y2WlJy3RCQOKzu_tAqdtnu9SiDCVMkISuhK9eEYm_XnC1El0K0DrcbhnJGLifK6_hWh9S5nTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی تجمعات شبانه یه رپر آوردن و دورهم میخونن و میرقصن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/151645" target="_blank">📅 17:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان عازم ترکمنستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/151644" target="_blank">📅 17:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQsigQlomkOaeW19BttkuVN0QRdTGBYTA6FrRds1L8wIhnC8TjtFwuYQp6Ub3xSnDZrRAISAaMPJcuobANljn6Cu_N02o8zBpWS47lPU56m2OSrKR7fsY3xCLZWyAl3tineTUPD-r_q9KYlycok3b3fdvCJXSGQhbjgZNb7QcioaDMIbvavLXt-ZTfnRrWDu_Ibg1z1fQw5rkqPB4hmHu0YtLLorExxkFXMN7o7dNUHMIvt1bs7y3e8NiRwYprkv7mSeqPEKLseiRl1kkhiU-jDIq6MwpVMYxxMf2LJvgToLBZPZNpJUz8OqGI6BQA7oh_ti2fKWWljB6Ktig6kZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود غلیظی از کارخانه پالایش نفت بقیق در عربستان سعودی به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/151643" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انتقاد ایلان ماسک از تبعیض علیه استارلینک
🔴
ایلان ماسک: برخی الیگارش‌ها برای حفظ سلطه انحصاری خود بر مردم هند، مانع فعالیت ما شده‌اند
🔴
دولت هند: مطرح کردن این موضوع که چارچوب مقرراتی هند ناعادلانه یا تبعیض‌آمیز است، بی‌اساس و نادرست است. همچنین، مجوز فعالیت برای سه ارائه‌دهنده جهانی خدمات ارتباطات ماهواره‌ای صادر شده است. تمامی شرکت‌های دارای مجوز باید الزامات امنیتی تعیین‌شده را رعایت کنند. استارلینک نیز سال گذشته مجوز فعالیت در هند را دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151642" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حوثی ها با موشک بالستیک به خمیس مشیط در عربستان سعودی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/151641" target="_blank">📅 17:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: جنگ اوکراین که اکنون در بن‌بست قرار گرفته، یا با مذاکره پایان می‌یابد، یا درگیری‌ها در آن تشدید می‌شود که بسیار خطرناک است
🔴
برای این مناقشه، راه‌حل نظامی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/151640" target="_blank">📅 17:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=uoQGLxO-qRIGykJDlxRIhaUs1-co3RJ4f8te2GYMSWwOmlYR7Lq0qsogG3wDPLDjfSmembZFvX2WsW-RjKNWPCcP96k2qEH_5Kr0Eiahm1d9dEIazSNdF3g0_THOKJzcA30pgQEpBT7eVzPTF8F_Pt63W5EBtU8WwT0KdqtWwgmkHi32YKgfN_gDPT7XQBttRXZlbEEg5UZyyn-hTfVdRSuxrobIb4FLKM099Wm1VBZAwNo2eqy7Ud2F78rYQ4nkcohn_Nt6qLNZmAso08Qly4RK-1HFwWJVe-hna6redhiTO04jGx3oIASz5Uk-nYTQ3S4L1YRF2pGsAxt3P2IApA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=uoQGLxO-qRIGykJDlxRIhaUs1-co3RJ4f8te2GYMSWwOmlYR7Lq0qsogG3wDPLDjfSmembZFvX2WsW-RjKNWPCcP96k2qEH_5Kr0Eiahm1d9dEIazSNdF3g0_THOKJzcA30pgQEpBT7eVzPTF8F_Pt63W5EBtU8WwT0KdqtWwgmkHi32YKgfN_gDPT7XQBttRXZlbEEg5UZyyn-hTfVdRSuxrobIb4FLKM099Wm1VBZAwNo2eqy7Ud2F78rYQ4nkcohn_Nt6qLNZmAso08Qly4RK-1HFwWJVe-hna6redhiTO04jGx3oIASz5Uk-nYTQ3S4L1YRF2pGsAxt3P2IApA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۱۱۰ هکتار از خاکِ ایران به افغانستان واگذار شد!
🔴
محسن زنگنه: قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
🔴
البته قرار بود سهم بیشتری بهشون بدیم اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/151639" target="_blank">📅 17:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پاکستان مشارکت خود در حملات به یمن را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/151638" target="_blank">📅 17:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974cdbcc57.mp4?token=BNzoCTOhoG0C3FrtovkmZbjhrhX5fkSmCfrmZh7VjuUdmifmP5ssdCS1eUcpOlr_JB-ypZSRBguQrJphzV9nYFE139uXIptd6teMFCtEbih9mdzpAFNhNdtWoJCLYoSN5DDY7GSOUh5YePLV46RAeThlO04Lou77pA6WYj5JL8oniKuRIf2QgzJrUR2jtTbYnDLpSY4jcNlUuhSOBbkCiIezwqh5c2n7gDKSXunbxveovCN8reXMaYnpQ3GkjBuXOmoxDzySye6SQXpcndqEoLV1h2DKlMdEfm76UAmi3F0WvySbScXsWtquZojJieHUHxdDE3zrg_RbBNV-EfNkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974cdbcc57.mp4?token=BNzoCTOhoG0C3FrtovkmZbjhrhX5fkSmCfrmZh7VjuUdmifmP5ssdCS1eUcpOlr_JB-ypZSRBguQrJphzV9nYFE139uXIptd6teMFCtEbih9mdzpAFNhNdtWoJCLYoSN5DDY7GSOUh5YePLV46RAeThlO04Lou77pA6WYj5JL8oniKuRIf2QgzJrUR2jtTbYnDLpSY4jcNlUuhSOBbkCiIezwqh5c2n7gDKSXunbxveovCN8reXMaYnpQ3GkjBuXOmoxDzySye6SQXpcndqEoLV1h2DKlMdEfm76UAmi3F0WvySbScXsWtquZojJieHUHxdDE3zrg_RbBNV-EfNkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداد عادل: نتانیاهو تهدید به حمله کرده؟ آزموده رو آزمودن خطاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/151637" target="_blank">📅 17:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر اقتصاد: می‌دانیم تورم و گرانی مردم را اذیت می‌کند ولی بسته حمایتی دولت مصوب شود خبرهای خوبی برای مردم خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/151636" target="_blank">📅 17:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0031620b80.mp4?token=mt-2VflubMA_XlFKsmJ9W-rdlpjy7CqT9oXRjlqM8HCddXZ6HO72QMltM10IzHc2qbl-qieCvp02F5vVGF0GQ5BdtryE2AEXNt55ebERnkgMM3zV2TdmtMAqdNSuxnlj-1EWO4MXH-MrtZUxhmOuN2XBgk0Sppr0EzAPZtsJlxU3jogEOJcjKFn7j_HXVfEQACgiJzKGkwaACGjn_B5q7MZMalPxdPz3RxKCFvhUtnc7iuxD5ZhHsEz8KfAAMx6TOUBh4KsaktPripn-c1wX9rYPrjL1zddCo-JUqMwe_-ENHMIc-gO2pKa6iyA0oLe6K_Tb56NccZGj4ue0itm4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0031620b80.mp4?token=mt-2VflubMA_XlFKsmJ9W-rdlpjy7CqT9oXRjlqM8HCddXZ6HO72QMltM10IzHc2qbl-qieCvp02F5vVGF0GQ5BdtryE2AEXNt55ebERnkgMM3zV2TdmtMAqdNSuxnlj-1EWO4MXH-MrtZUxhmOuN2XBgk0Sppr0EzAPZtsJlxU3jogEOJcjKFn7j_HXVfEQACgiJzKGkwaACGjn_B5q7MZMalPxdPz3RxKCFvhUtnc7iuxD5ZhHsEz8KfAAMx6TOUBh4KsaktPripn-c1wX9rYPrjL1zddCo-JUqMwe_-ENHMIc-gO2pKa6iyA0oLe6K_Tb56NccZGj4ue0itm4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: ما هرگز حاکمیت هیچ کشوری را نقض نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/151634" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2acefea4.mp4?token=K33H_0xEWZwNLtVrlavy8QlQ0r2Gl9Hg7-2i1d61jCgpZSeYvNZwwnxawtF5-yMl0O903CE0SyHmfhYJWLHm5TM_x7uddN0QGzmarzczVi6tPEt4oQX9OE5T69Q41fKeOI5_ABRtd5XVUYslPlHRWA_wPZa0CI8lIhS0HR2WB6sBNcyv0XX-W9999Qaj-eBdXyAxJJ9qQBLz0cBsHcm-l5055zwfpFH1CRcPG30dwa0YkZoKlHNk57s5rpUO-MFI4HReoUbMQ83H68f5MYQYy-oK0STnnmvrUkq-O_oJAoin_7Yiq3tm9W_kcJReQVUMvUuuPAWedxLlpHCvQ68BIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2acefea4.mp4?token=K33H_0xEWZwNLtVrlavy8QlQ0r2Gl9Hg7-2i1d61jCgpZSeYvNZwwnxawtF5-yMl0O903CE0SyHmfhYJWLHm5TM_x7uddN0QGzmarzczVi6tPEt4oQX9OE5T69Q41fKeOI5_ABRtd5XVUYslPlHRWA_wPZa0CI8lIhS0HR2WB6sBNcyv0XX-W9999Qaj-eBdXyAxJJ9qQBLz0cBsHcm-l5055zwfpFH1CRcPG30dwa0YkZoKlHNk57s5rpUO-MFI4HReoUbMQ83H68f5MYQYy-oK0STnnmvrUkq-O_oJAoin_7Yiq3tm9W_kcJReQVUMvUuuPAWedxLlpHCvQ68BIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: پرتغال باید اف-۳۵ بخرد
ما فکر می‌کنیم پرتغال باید اف-۳۵ بخرد، چون معتقدیم این بهترین جنگنده جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/151633" target="_blank">📅 16:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257d408199.mp4?token=e9opH5ZoOWbCzcriAQGzg29S5JcpZgU8evZbDGuqch0SUDKUQfziBqYZgmuRd2gEOqxtDwUifMk3KWAdX2DWAWi4e68YQcM3QFWGILui24zLCp7AiEKoQp0uN_82VwsicqitIBwDToYz0gSlJOGjkDi6lank6mYHSHnfuLcniR6J-JGSNvdyHkSaqWwRAjmzT61NV8KCtv0jrv5noAo49Ie7_rT9wIVZvCcve-k2fhF3W-I-4LMRT5arvF3KuzkpjckhD-WlubPauJog2Cr5pTCXsr4JTuAsmJeU5VqzIRMzNaVag0ucLWUWoxC5eeQBAMncULuQWCDKYaqL7BRX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257d408199.mp4?token=e9opH5ZoOWbCzcriAQGzg29S5JcpZgU8evZbDGuqch0SUDKUQfziBqYZgmuRd2gEOqxtDwUifMk3KWAdX2DWAWi4e68YQcM3QFWGILui24zLCp7AiEKoQp0uN_82VwsicqitIBwDToYz0gSlJOGjkDi6lank6mYHSHnfuLcniR6J-JGSNvdyHkSaqWwRAjmzT61NV8KCtv0jrv5noAo49Ie7_rT9wIVZvCcve-k2fhF3W-I-4LMRT5arvF3KuzkpjckhD-WlubPauJog2Cr5pTCXsr4JTuAsmJeU5VqzIRMzNaVag0ucLWUWoxC5eeQBAMncULuQWCDKYaqL7BRX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: حکومت ایران مجروحان اعتراضات را در بیمارستان‌ها می‌کشد
🔴
حکومت ایران وقتی معترضان زخمی می‌شوند، وارد بیمارستان‌ها می‌شود و آن‌ها را می‌کشد؛ گاهی حتی پزشکان و پرستارانی را که آن‌ها را درمان کرده‌اند نیز به قتل می‌رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/151632" target="_blank">📅 16:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7fed9dba.mp4?token=QH_Nn2dvKn5EvRv3YCV1VHzZ518cx-OMyj6OsOCNdp4boic1tDupDBNHOaXrUOBi7bOh-ilumXC2uE1YvsQjbcdGo4z6xE4zPQXAuQG1y2Nv6Ky4JV8XpxTiT5Ty3pO8IrZNHAlsq2ZhMP6euBgKyVAezAAHAQ813n9013rQLlhm5RLUB6deNH0mlf9nt5kBaADUS7ns51HqXMgpg7jB9XahSEIGNLWHqtSaIQWziAr1JE7vHPDXTCj8NoE5uAj_b0EwPXU_Pfpm4kCgRiG23k9VcNhlvHrxDvPVJkqzatckOimIw5IIEYWGCk-H85XqbfsYN9yWdsWDnVAr2mJoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7fed9dba.mp4?token=QH_Nn2dvKn5EvRv3YCV1VHzZ518cx-OMyj6OsOCNdp4boic1tDupDBNHOaXrUOBi7bOh-ilumXC2uE1YvsQjbcdGo4z6xE4zPQXAuQG1y2Nv6Ky4JV8XpxTiT5Ty3pO8IrZNHAlsq2ZhMP6euBgKyVAezAAHAQ813n9013rQLlhm5RLUB6deNH0mlf9nt5kBaADUS7ns51HqXMgpg7jB9XahSEIGNLWHqtSaIQWziAr1JE7vHPDXTCj8NoE5uAj_b0EwPXU_Pfpm4kCgRiG23k9VcNhlvHrxDvPVJkqzatckOimIw5IIEYWGCk-H85XqbfsYN9yWdsWDnVAr2mJoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: نمی‌توانیم همچنان به انرژی بخش‌هایی از جهان که دائماً درگیر درگیری هستند وابسته باشیم
🔴
ما نمی‌توانیم همچنان به این وابسته باشیم که بخش بزرگی از انرژی جهان از منطقه‌ای تأمین شود که اغلب درگیر درگیری و جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/151631" target="_blank">📅 16:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پزشکیان عازم ترکمنستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151630" target="_blank">📅 16:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a2ba7726f.mp4?token=IttPSmcdbD2-MxWLyusd0C9mdO3shAc4RnDIM3H-ZxkvqlOgMMhAdjyMjGz3vz59vD_mz7mKKWnyM3jQqOfYVJY-GINddDinc0od1n3IkJw6HClXuk6PQElXNjRvL_XDRrsXbxfuD6U7mKLUj0ZQ81ilEB0EM2nZd9iTUoTGQ4MYFDdu241PBCkgYA40wWFPSbbm5dC4RcJLyzGsHQtFxLQIqBrphszOVtI5fw-9b5CK72kip2otGN0f8pLQUKn2PRQ_3PUuNn3udF9uni3QBKdbt0-ataQX4yMxuMvs77o8uqZ9ThoNkrwjOOYQNiUYuyIjo5AdXvVQ-nyxXL0zGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a2ba7726f.mp4?token=IttPSmcdbD2-MxWLyusd0C9mdO3shAc4RnDIM3H-ZxkvqlOgMMhAdjyMjGz3vz59vD_mz7mKKWnyM3jQqOfYVJY-GINddDinc0od1n3IkJw6HClXuk6PQElXNjRvL_XDRrsXbxfuD6U7mKLUj0ZQ81ilEB0EM2nZd9iTUoTGQ4MYFDdu241PBCkgYA40wWFPSbbm5dC4RcJLyzGsHQtFxLQIqBrphszOVtI5fw-9b5CK72kip2otGN0f8pLQUKn2PRQ_3PUuNn3udF9uni3QBKdbt0-ataQX4yMxuMvs77o8uqZ9ThoNkrwjOOYQNiUYuyIjo5AdXvVQ-nyxXL0zGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: کابل‌های زیردریایی در سراسر جهان بیشتر در معرض تهدید هستند
🔴
کابل‌های زیردریایی در سراسر جهان بیش از گذشته در معرض تهدید بازیگران مخربی قرار دارند که تلاش می‌کنند به آن‌ها دسترسی پیدا کنند یا در زمان درگیری آن‌ها را قطع کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151629" target="_blank">📅 16:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بلومبرگ خبر داد:افزایش ۶ برابری هزینه انتقال نفت از خلیج فارس به شرق آسیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/151628" target="_blank">📅 16:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بابک زنجانی: میخوام ماهواره بفرستم فضا تا به مردم اینترنت پر سرعت بدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/151627" target="_blank">📅 16:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رئیس کمیسیون کشاورزی: در صورت جنگ برای ۸ ماه ذخایر کافی غذایی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/151626" target="_blank">📅 16:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzKRy4vu1PGgz4k8Ye5Qm3aiyFBtBsnkZdCVCXr1E2hQz8sL8-8Ul-bCw-r0rU3Hw_Zhyc0EMTD0RFP2y6GqwdYLA9aP1sCwWTqx4dVl5QBmnp3HI6qwuIU8Tj81Zjg4Fi35t0fXgEYRlCb1IleUGKkzqUPxThNOl5NcrCgvIwC7eBNK-87aT2rJq2hUznQD88MnOOdYqrajfAU9U9Z1D_NAYjKjBIMtjbm8COGf7vC3yjH9Q-M_OXqHcaAhh3V2uRPlMc23-zFqPZGEKfOmbnt-YiXlvyWsGBBTD1LBxU74Bg90rPd-SXKSkr96fI5NcUE9YxaN1w6-XRWhjzoG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاهی کلی به لیست افزایش قیمت خودروهای داخلی در بازه کمتر از یک ماه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/151625" target="_blank">📅 16:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: دود از یک هواپیمای متوقف‌شده در فرودگاه ریاض به هوا برخاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/151624" target="_blank">📅 16:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: مذاکره هسته‌ای در دستور کار نبوده و حرف‌های آمریکایی‌ها از روی استیصال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/151623" target="_blank">📅 16:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c568889ae.mp4?token=YgSG6QRPjqgrneJvXsSUvMNv8eFnTgFqvGQvzTNNDNLdkNaIedXBRQwb_-RV-Yvz1ruqOD4hJXlfcFxJ5RIXTHNiwwOYlfvyJsMfkyZI4yaKKM_IZPOBbHva2nyPCEjds7DDGLPUjbNZ6Dh2QRH9OhT5rrxCpD7XJOj1lCu9nqP_KIricBzWmmCXI6B-7v3Qe7msJtzVgIxT7JRClG50YMXuC1VUjb0aqcf-ckk-ouvWIfq_hTiNfdlIer25rhWNWcl3rUVD6K43f-xN1byQbu6uQIqkTxn6DuTvlqske1iewqX8f6s_gKEwcw40aaUmVlQuoCIM53SKgNlxBVLktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c568889ae.mp4?token=YgSG6QRPjqgrneJvXsSUvMNv8eFnTgFqvGQvzTNNDNLdkNaIedXBRQwb_-RV-Yvz1ruqOD4hJXlfcFxJ5RIXTHNiwwOYlfvyJsMfkyZI4yaKKM_IZPOBbHva2nyPCEjds7DDGLPUjbNZ6Dh2QRH9OhT5rrxCpD7XJOj1lCu9nqP_KIricBzWmmCXI6B-7v3Qe7msJtzVgIxT7JRClG50YMXuC1VUjb0aqcf-ckk-ouvWIfq_hTiNfdlIer25rhWNWcl3rUVD6K43f-xN1byQbu6uQIqkTxn6DuTvlqske1iewqX8f6s_gKEwcw40aaUmVlQuoCIM53SKgNlxBVLktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو درباره ایران: هیچ کاری نیست که بخواهیم انجام دهیم و هنوز نتوانیم
🔴
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: هیچ کاری علیه ایران وجود ندارد که بخواهیم یا لازم باشد انجام دهیم و هنوز نتوانیم آن را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151622" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzmfQ0qlQQulBbGBXW0PohPq16Ru7W5ao9sB4S59HuM5evGDoq9jr0lIJyEQUcknkFUox0EJjtxapzhznVo06tMZzAtwAFgOYLjxAWg-0bHQfs7sCUwCtgDVmQFZlitCA37h2msWLQfYfXEb-mkzDwarcIAXzfpspV3FetgPTZnsgSyFRDmKU4EWEZxyOWf-9nnfSLAHB-y-l71qpF-4NhLe3cUEv2UFdtLG92ICTn6AV8ZNIKbJgsfmHw53s6yvhj2AxogsxIZ3BGpC_MBkCUuySBDUckqLOtu420dIEIwnRTcigL_yOZTSro7FosJp-pVnkz_RZwseI-sNLJlG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فلایت رادار: فرودگاه ریاض بار دیگر تعطیل شده است. بیش از ۸۰ دقیقه از آخرین فرود هواپیما گذشته و بیش از ۹۰ دقیقه نیز از آخرین برخاست هواپیما سپری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/151621" target="_blank">📅 15:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151620">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
یحیی فست  خطاب به کارکنان تأسیسات نفتی عربستان: از تأسیسات نفتی دور بمانید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151620" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151619">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1CP6xcsg-4-JImvYpEFSeVVHueQSWsFx3_4w5DBO7OcRBDhP3h4Nzg5yzn_nc39stABFyOoQ_BEqtUPbzrA1oJv9WPCdaMIFbcBqRWvmhWkDaRrPgQ1j1eGUq8cd79YadHsq1KZfEZRwvrJF2lhazHnTRvIpm3DLjr3dmcE73LMi9_MqjZ6Hh_NWn881J_-_qElCBr2td9kgSBqYKUimrP-AvE4BAx_9KM3MvTlT7c1DNayUVif_xRfYmzPQKVOpYYtoAikLR_c9ofjlg-xqvmMqpQW0h_SghiSj7OY8EyxCcVgtnRF6SSUMYOq3GiwwM2-KbduUTRVynIkanBjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله خونین روسیه به اتوبوس‌های غیرنظامی در کراماتورسک؛ دست‌کم ۳۳ کشته
🔴
رویترز به نقل از مقام‌های اوکراینی گزارش داده در حمله روسیه به خیابانی در کراماتورسک که دو اتوبوس شهری در آن حضور داشتند، دست‌کم ۳۳ غیرنظامی کشته و ۱۸ نفر دیگر زخمی شدند.
🔴
مقام‌های محلی می‌گویند این حمله با بمب هوایی انجام شده و محل اصابت، ایستگاه و مسیر حمل‌ونقل عمومی بوده است. روسیه تاکنون درباره این حمله اظهارنظر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/151619" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151618">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3IyA29wykPXcceGsM8wm4VXK2BZDbv9nmIeOAyNfOAV65f14uvmt9AZh_lc82SYR-p-HVS8BCInnNKPDPJlU1xfx9OYPVo9Spnd3_rpi1Pe6oXJXovbPyRrIkMVySaGGh0_KP6A715Sz2YqO6d1vhB4pKPRVppxoJKLvdIcY_yWYmwCZrNny1xYJYt_AOiBsFeQn8itEwH4XKw2Jc0wWQrRPCjBTNl3LUtAHJN43CpPvI2dv9NxTXP1GZvhyYjjoVtJRCSqwhCH3RQJfZRJbVpWzYvfZxd9ZRlSaielPattEsUAnMOlLvXdkOECNcz8yoC6D7q0H7Ht6x4byzSZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: جایگاه اصلی مردم و کشور ما بسیار بالاتر از آنی است که الان در آن قرار داریم.
🔴
همه باید دست به دست هم دهیم و با اتحاد و انسجام و تلاش و کوشش ایران را به جایگاه اصلی خود و قله موفقیت برسانیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/151618" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151616">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb0d3431a.mp4?token=kjYWtapc1l0seG0JCTTlOd8nd85HHhjOm4BteZ3Q-du2DtAvBM-T8wIyZUCfKUCxue12M0SjPygxVrqeHhcjxKsXJ2mVrWAhZ6McZsrHiD-H0OykSYnRiln3XbR_a5cb6Totv-hXggxMdY2s0xLwJ4tm36-3Ss0Ba1OrctLgltm71zzkKODtmoxmOytBi9-X0XM1D7K6d2O8GpEK3mnBbCfg0Et8mtcZqTT2Xu73VNnYI1HQ-GHPj1yZulO5Z-yX5rDd_3bxGa-5sjs4Ra5PR6xXiu4aXnDyJvJAqEEqgz6T6jEPHDh-9YhmmRYnm1tcCYSIkcTFXVdrkO-suG30BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb0d3431a.mp4?token=kjYWtapc1l0seG0JCTTlOd8nd85HHhjOm4BteZ3Q-du2DtAvBM-T8wIyZUCfKUCxue12M0SjPygxVrqeHhcjxKsXJ2mVrWAhZ6McZsrHiD-H0OykSYnRiln3XbR_a5cb6Totv-hXggxMdY2s0xLwJ4tm36-3Ss0Ba1OrctLgltm71zzkKODtmoxmOytBi9-X0XM1D7K6d2O8GpEK3mnBbCfg0Et8mtcZqTT2Xu73VNnYI1HQ-GHPj1yZulO5Z-yX5rDd_3bxGa-5sjs4Ra5PR6xXiu4aXnDyJvJAqEEqgz6T6jEPHDh-9YhmmRYnm1tcCYSIkcTFXVdrkO-suG30BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: روند مذاکرات ادامه دارد/ ظرف چند روز به پیشنهاد آمریکا پاسخ می‌دهیم
وزیر امور خارجه:
🔴
روند مذاکراتی همچنان ادامه دارد و از طریق میانجی‌ها پیام‌ها در حال رد و بدل شدن است.
🔴
ما طرح خود را که تحت عنوان «طرح هفت‌روزه» ارائه کرده بودیم، مطرح کردیم و دیدگاه‌های طرف آمریکایی را نیز در مقابل آن شنیدیم.
🔴
در حال حاضر مشغول بررسی دیدگاه‌های آمریکایی‌ها هستیم و فکر می‌کنم ظرف چند روز آینده پاسخ خود را ارائه خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/151616" target="_blank">📅 15:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151615">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بیانیه سازمان انرژی اتمی کشور:
از حق غنی سازی خود به هیچ وجه دست نمی‌کشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151615" target="_blank">📅 15:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عراقچی: روند مذاکرات ادامه دارد؛ ظرف چند روز به پیشنهاد آمریکا پاسخ می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/151613" target="_blank">📅 15:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
عارف: همین روزها کالابرگ افزایش پیدا می‌کند؛ در مرحله نهایی کردن تامین منابع قرارداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/151612" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۵ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/151611" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: توافق مکه یک توافق دفاعی است، نه تهاجمی، و اگر به یکی از طرفین آن حمله شود، سایر کشورها در کنار آن خواهند ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/151610" target="_blank">📅 14:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuVk1z6Vo0YL2LWZXcNy4Blj1rQrmqGGVZ6xB0EqsHYtkV_zotlaDx9Kyj0YOrxxjAvB4Iztg4u9cwOxZAuRqUj544-2y5swMbVBLsBQsOrbg5Lt65uVDmT-VYaJbUg4wkuCz6q-VK8QPS48t02aY_P9A96NCD-0SSRczz79WSSv15yGFrJ0Jt5SL4JCgKiTPuH0Spj5g8Suk30WoHlKXRDB5WxPV9wPBaBdlTgRS-O7TtRYrFUCpTtrdLPP0mlowY9S2Im6q0eyn6UMUHyFYWACe7KPhUqTfJAqePKXdk7WXLHIh0x6X4odqDA4PcxoE9QRHKNtgqnWFXjSlfNJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/151609" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
علی مطهری : در نهایت ترامپ مجبور میشه توافقی رو امضا کنه که خواسته‌های جمهوری اسلامی تو اون تامین شده باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/151608" target="_blank">📅 14:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: نباید اجازه دهیم دریای سیاه به جبهه جدیدی در جنگ روسیه و اوکراین تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151607" target="_blank">📅 14:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIrk1zGU0IFY6qmAy8nWhihW0DjutMeb61iVQ4akm3JCLpbnWgDSXPow4xFmx8yp3l-NDmwvspqOGLOYz-M5qVrZ19LgR0BZn7zQK8jFRLk4nxHIX75n6o-3KWGQkt-oe7R_VVN_R3dnhRgtamTJqypg7FuOuiQbUedkb0jI_LlrXR1W2YV3p0HDGagRGi73kYX7RaKbdm2qniDGFioDcMsV0fZUBNgoWtjzmMHEWKSZL96Vt8-Va9WO3qkVIvUWwYIn8Jw4Kzt4pK6eSaWvN7QjoyZnEzACBuR-4Empeg7Go6dfKw-0Gj3m1pcS2trA32qdaBfE29SS_UG6GmzgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این فرد ۳۷ ساله آمریکایی از خانوادش شکایت کرد و تو دادگاه گفت من نمی‌خواستم تو این دنیای مسخره به دنیا بیام شما باید قبل از بدنیا اومدنم ازم سوال میپرسیدید و الان غرامت میخوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/151606" target="_blank">📅 14:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هشدار درباره احتمال حمله به پایگاه‌های آمریکا در آلمان؛ رامشتاین و اشپانگدالم زیر ذره‌بین
🔴
جروزالم پست به نقل از نیویورک‌تایمز گزارش داده اسرائیل به آلمان درباره افزایش خطر حملات احتمالی مرتبط با ایران به پایگاه‌های نظامی آمریکا، به‌ویژه رامشتاین و اشپانگدالم، هشدار داده است.
🔴
ارزیابی‌های اطلاعاتی احتمال استفاده از پهپاد را نیز مطرح کرده‌اند، اما تاکنون زمان یا هدف مشخصی برای حمله اعلام نشده است. هم‌زمان تحقیقات درباره طرح ادعایی حمله به پایگاه آمریکایی فرفورد در بریتانیا نیز ادامه دارد؛ ایران هرگونه دخالت را رد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/151605" target="_blank">📅 14:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3d2ed693.mp4?token=RtUxlT1dYSYuVed7uIIRsf9z0lwm2Oek-hMgZWXvPJvULJwswH9_41zyX8aOLzj4SpMtqlg5-OtvpwPHMeodjlz56ZvdHvHJTKgWV5mKWglDd5up0ujEtjPiZf86oJNb6n14VWsOVe2amu4BG_JqPqF2L2VQmFdpQjs-gZb7gwYPt4tIkDGXHBvoWZ_I09wObyXAndYDhuL4CjWueBmns9-UHjW6mFUOouF8dd1Pknd1Q4XHxfuJoswKBFRmfgTsZNdGtWboeIciJ7eRKO97LB0YJdf0ROBrL3mLDxbHVO-RQhqb_GQqS-8uIED1qSxn4bpLseUI1zFvTC0ltCRc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3d2ed693.mp4?token=RtUxlT1dYSYuVed7uIIRsf9z0lwm2Oek-hMgZWXvPJvULJwswH9_41zyX8aOLzj4SpMtqlg5-OtvpwPHMeodjlz56ZvdHvHJTKgWV5mKWglDd5up0ujEtjPiZf86oJNb6n14VWsOVe2amu4BG_JqPqF2L2VQmFdpQjs-gZb7gwYPt4tIkDGXHBvoWZ_I09wObyXAndYDhuL4CjWueBmns9-UHjW6mFUOouF8dd1Pknd1Q4XHxfuJoswKBFRmfgTsZNdGtWboeIciJ7eRKO97LB0YJdf0ROBrL3mLDxbHVO-RQhqb_GQqS-8uIED1qSxn4bpLseUI1zFvTC0ltCRc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی خطاب به وزیر خزانه‌داری آمریکا:
🔴
فقط ۳ روز وقت داری!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/151604" target="_blank">📅 14:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
آکسیوس: نتانیاهو و ترامپ در 72 ساعت اخیر، 2 تماس تلفنی درباره ایران برقرار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/151603" target="_blank">📅 14:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20116b71ff.mp4?token=NdgXAzL4Lj33XR6PT95qRDfLiDrSwNdo4S-d2ZN9Pg4MK-uTuJ9nNU7oNziwnRQzy1gRUdEGkTJZX9_xBurYi9AdtZ1lt3ya_NXanEhcGs3KSnDiL5roUyIQwH7OX31sRSvV8vmXThIKAX-XBwZgVXHC43QorOTsHJwBB3XOfni89Z4J26l8eunipC5mGSXvBclbQTBjUcRl9FQ6AQmw4DtG_rxb88Nl_FLj9RgBgJA5aDdBzRSbdf6KhAsegaU5IED-udcPJzNl7eXmmcggjsE9SCV1djWD3priTmEYPkqCHvRNhRaJIzySxFKnid3R5evpkoJ8s9fnW_dQ-3BJBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20116b71ff.mp4?token=NdgXAzL4Lj33XR6PT95qRDfLiDrSwNdo4S-d2ZN9Pg4MK-uTuJ9nNU7oNziwnRQzy1gRUdEGkTJZX9_xBurYi9AdtZ1lt3ya_NXanEhcGs3KSnDiL5roUyIQwH7OX31sRSvV8vmXThIKAX-XBwZgVXHC43QorOTsHJwBB3XOfni89Z4J26l8eunipC5mGSXvBclbQTBjUcRl9FQ6AQmw4DtG_rxb88Nl_FLj9RgBgJA5aDdBzRSbdf6KhAsegaU5IED-udcPJzNl7eXmmcggjsE9SCV1djWD3priTmEYPkqCHvRNhRaJIzySxFKnid3R5evpkoJ8s9fnW_dQ-3BJBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی‌گیر در مکزیک با کوبیدن داور به تشک در داخل رینگ، باعث مرگ او شد
🔴
این داور 75 سال داشت. به گزارش رسانه‌های محلی، ورزشکار مذکور بازداشت شده و پرونده‌ای با موضوع مرگ ناشی از بی‌احتیاطی تشکیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/151602" target="_blank">📅 13:55 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
