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
<img src="https://cdn4.telesco.pe/file/muMlJUM7BOgs7H-JFIjmhVMWT4eX9_yf0mq22cKJWl-A5zyAF4XP9x05njvXtvXoKEAYuDa-g9jF-3-0CiBFJ5X1f7kFToeoqnA42q01AXJd7TacLdhZO97KY_RMdoBNIsI7CpeeXY3cF44aplVffkazqpHYfS7lS9lPX9Q0E-DwVb2cW1_Z6XiETy4Lumy9O1n9oeWwVBvGsndLBOCD21ghTJehb9-_m4Z0OBdjMMGOnCSW56jdwUl6mEVyuy8Z-O8cG6ap-ft7Ew4icqnqUENvvyI7U2gigu6t0RabuUTWXm-D-AwqRpZe1QUwXKLuzEdk0ccx2yIJ8X8SSUiQ6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.4K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 09:05:40</div>
<hr>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7O76YQ-sojtTX1Cij0gdVpwMK1rCSLQFcWIXLT-3SskQsj4bthEs9cb3XAxLBiUuGLM7AVLoq3E0qodrUh5jAn-MdO8R0QHnF_QhJFpiho-_FaLETX5pasSB-DfaJ5hC3id2aUbrJMbHvcE4XmcJjnrGuFpyj1FkPgkQXSZd4MqWaDEDyGpcDTD79VQiZ4KqY49mzrzKk_iEgbiegLvW5kpR3NcuYYOUdoopAmPWkbclc9FLKCLBj7vmtusWcLd2hFGTP6S9HaGa-IKnZjCdof_X4gGidLR-a8X92BYsAHCTrhAeRJGZG89MO_8ZogdRqDkckaDHj-fYTw4DQG6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgTSrfQz1LT-VxIera-gSPxSWoTp9ywXhTGRmKqJR3ai-LI2eHGZA20RSEOMKnI_wmD2gyYEBAq2pKUn_-nqmGmKfm5KcL5A7HDj7E6HVRGx6kFgMW3IyOsS_VFcqStZgjp2m4uZ8Hw1A257CTW1DrPwcFd1sMytAg62Rc5AqaGRD4uzSnEX6JKwk54mY0BViRbJqcbtK2pRedMdvD5TZRXcULBJTMDD8odV96vXl7wC8qAu3Kf91bqWvE1PnIOAZMFt_PV1-8Nm9104sq13YBdcZNA2xJDI3Q4J9nuOqqe1JOZtxziFvYVCjkmFZVb_f93YIFxvcWu3eyvYss-yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
طبق تلاش و زحمات تیم russia proxy بر پایه اصول صدور ترافیک خالصی بدون پکت لاست
⬅️
آپتایم ۱٠٠ درصدی با سرعت +89 مگابیت و قیمت بسیار پایین
گیگی ۱۵٠
⚠️
🔡
براتون پخت و پز کردم، ۳ روزه نخوابیدم، سرورارو بهینه کردم با بالاترین سرعت و بهترین پینگ از الان میتونید باهاش حتی گیمم بزنید، اختلالات به طور کامل برطرف شد و هیچ قطعی نخواهیم داشت
❤️
🍸
➡️
@RUSSIAPROXYY_Bot
⚡️
آیدی ربات جهت ثبت سفارش
⬆️</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4A24P7dtSqJFWfUwp-uIlPn5VplBVyMKrHmYNOahHKIRwLI4sVgEstMcAS6ZzwzyOHss7OkjlyWFUkzWEQ9n4iGPqHBriEu9rurwD6defuPJwNVyc7s6qVdOK0D_0rWUBEiJJKK5_0AdJH_X5SxV4BeY3e08mMTsaFJcqjo8ilHxxIdkiVvy5y7fy_iM17CWbSJJf5U4cOW7HPGSvnbd60t83bRMYsphcVMBztaHXDiQ5LsF2yJDvXcP0s3b65FIFkSpAowX5Vp0b6p2__-ajNThfLlOsB6Ijb7i0Tpz-wklzCd1ghoETDB6_m5lYU7sWDzps8sBfwTRQeHRLSZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez_Gk1polAyH4Dmk_qIHcMtY92B496-h9Bege0J6lfkgZw2-taMNARXo5Imf7QMgF44gydEXDZNGtq8xIH3DwVEsGxZEONS-Z9r2t44qMigeCcCI-I9qjeYV68Gf5oyAY5xwHfdzlmOE4sTGdQA_vB78QQq5fhEQjik1VBI2vzUQz0nUZoOWTIMKqArfaSJWoSsOyVxgUDS5dLnl0yQbgEVhKuOEXH8taLwXJMsok8W4yoONLwNkJ01gi55VQSsvOBvM1d50q62Jk2FTStlU3Q002y6q3MX9J5Tb4lPqthRSe5UfV3tVxsG_A0JxDR0XhiHodYN61YkXRLIkg3u8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZNnB10abtf_mjh78TsrYhtKCCDJJWeu5Ppj-V7Mw2o1anWJhdQzO2QpQqhi-FHbWVC6aizk5_ThZTSNAXFgKPsQrRzl9TuTGFXOz389nH0qg0jPYIrcoFwrugK-Xg6Y6PEjCIJ-d11Qu-ddZR9KUZIbCnKESag-ZCDJGZ1kdGm-PgBLjgowO4vVvhvlungYBElz9Adbpz5HSQG1ewa-v6Lzsywm3dQbTPU5fuzMnWOa5eGIycAMTPrcWKy7wjncVq-Q9DC1pCc8nmBW4gVgLFO6bFYBC4jbw08DEY64f7JVc42tRwE5JbA7btOuoA6iD0u-vNVhz79iV7GziW5prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW1Dtd9QpJybSFXf6se99CwhVMoZu71iW2UBf4ui7KeWR7vK7vRTKAf6I6MI5YHlcdWFYL_qt2tjxA7C_szxihHh7Ca86oG538vnjZdM3qf-_KtbRlU_K_GJOQdAsF3QMIotTt60qogRMAAUnxh_c0lkr6vJgbObHxsqob25LBBKZTuZg2S_l0LZ2QzRowGPna9y-dIEFdYx6jgsnfclOHtZT87qG9wy7d-pASre2w7FkGgQvAyMj5QYp7xCei42Wz5DcrrA3mTrRKKIRncwC004rfaLAaCr9lqjBs8nGyF3wF1tj667k0zV-TS26BCtmc7A0pV6zhxOwRiJKbfL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mafI1O4zvwe_1YHmFpdwl_s3S2NtcYEqHtTKzvyalX5yJAdsx28tPffLR_UFTrWc6XhQoUN5KHQQsmI96xsOHIYmcKcKuVk_qml8XaSW0-KCujOWL05gUGRQphgZPuHuAFssLoAp1voVGBII-M95Y7fzZ3jLRn-roC_raa2qZ2YIXH_XRTz0FzbwliV_TNb8-SF3XCdElwbTVxso-heVS0w1CDKgOISuM99XiOWObmLGnvq4_HSF1DBD4ND97LOiJR1x_s0XK3COVqug5aZ_T5yjIJ1M1uQ99-ZcIoEHxdveIAcAv7_jeQav_GYwQcNTPpn0UMSm_hAbHj2XjmPJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfPfx0K4EUQfrIgL3ICEC2lczj29TRE35tzSLt8P2GXLS58PQbfXHnJYSkoicWzPwka0EnbFnBcWs2AsBIdJRdRVLS9ytC0g_IfHG3hONNKiBTfWWftZ5BefvWz9JL5aP4RBpSXmUro0P-h3PtMAekpNdZr9iRzmN72w2EWcuUvPvUN_Gla6cNDK193iaJ2YFrUlHJExI3ZQcVfF4ixgUcQUHB-j1A5JwTff8vR6ThsPUjB7ARuJpYAxVizmrWzdzXnWrZjN0KSpPhVX0Rv4JuS6vZBHEyUWsNRoqHtTrx4qqsmpM0YqJnrWg0TYO2S1KHUF8Pdd5RWuih-eNLr1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4Ll2thuL_8GaJkqo0yMTC2Ee3eFN-5se-H_W6xFi8RzKyRKrZWM-IslzLUWOJpG37lmQFHLPpYiHwwN68HbK2glrAINsc3r3lh6x2Hb5d5N1DvhfgKDDCuQxkBF-vNzjdeMkqEr-WhNgaZu4VzxRHxTn1tUCW7TjeZNp5cMbHjzPPFr9mdYYsalzveYurCUHfZCwaNFMCSNPLXB8GqBExTqDcJUsN2zSzMyzMjJvXXaWtloW19p3wIx5sVa26UnYD_N3jMwoPl8D7s04NL3nZZUSC-s7HiFhSc8WRvO8sFIdrE_Z1Pe9VQlIQZL5LG-VTqGxnAjIyn_bVdnwYwU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvoMSfE0DTe6zFwWYJPvyPYJ-YS5r--iGeoYa_aDZ-lVBMil-kifFQHKgrkC48Pz4ZrdouaM8C4zMcfyBT60NoV3tVnpRSmLVPN1pj2VsIpl5fVuJTgyvkVJYb7vxhtr4qoVTuUfbK1YEUfnQcdF1xZjnAnZnBfTtb-xqnMhzHjzNnyoRWWHuGKx6jhwNmQy8GrVQv1PqOohIgQrgEncYCLnPXGv-v0od91m73Ybr7d8kwuydm1Dw0kWK7NNvgS6iVDm-y6ir5Qo-73nG9kHG9UrrXoxJ_pHEG2FHrkcLP7LrjyDpI_N-FlI73TMH2DCGGdEDp5i8KiX_4GTBBDRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=mPCfyhTo6hEUPWRpl0CVQMzLvwQ5g-rUmrSmIXAXZl3Il5xE085wA00FEfGPiqeVmnYPMx0eId4n3AvqwmiX_r4KBtijwhlHx1SqJZqGlb4HgtfxEXon4OH80-uZYootfjUQJPR79KsezUxyT9apXckFBdzXE8VtFurI1eRmHEkUA1_3xUUJLfOsglOHMxZeaUM9_OnTbT7eztkF_jXjPKuSxPkokwgjODmt7BOs2E8nI_zEZ6VUjwCrIb66xSTXFGph_EiWSuUVYiUetqTRnLpcS7Oced8INMyZVUr2-awHX4jYOzO1nA0IBbnsWBHTePvkbamMDAe-dA_QmA264ZhZDzm4l5G8iG-XUOyBfjj9rpVmxKLy8kKpNUAlBNx5rLbEO6tvHkbvW55u4VdLXi5wmY0iMp1qhDOE6JxNPQkwqCcGk63DUezcC-6j4XNtujqjcM6oQIaPEqXi-kJE4t8RQcg3NQiZb1qnp8m6FT264dW6EcFvFNFDboihj9zCw8kcZVss8HxOfkHBT4AUlvMFyDlt0UR8-Zrs9AsR4bef1S8cOTVesmCXzFvhfxcxhcw2qE35sdPXpn3hGzGGWNZrc1O_Ok9702zS7A5BT9POPOTdIneBYu4sF1kjTKQZxrtJfLCBy1SpKQDUsmznJAr0AP1-HhehngTMF1fOVW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=mPCfyhTo6hEUPWRpl0CVQMzLvwQ5g-rUmrSmIXAXZl3Il5xE085wA00FEfGPiqeVmnYPMx0eId4n3AvqwmiX_r4KBtijwhlHx1SqJZqGlb4HgtfxEXon4OH80-uZYootfjUQJPR79KsezUxyT9apXckFBdzXE8VtFurI1eRmHEkUA1_3xUUJLfOsglOHMxZeaUM9_OnTbT7eztkF_jXjPKuSxPkokwgjODmt7BOs2E8nI_zEZ6VUjwCrIb66xSTXFGph_EiWSuUVYiUetqTRnLpcS7Oced8INMyZVUr2-awHX4jYOzO1nA0IBbnsWBHTePvkbamMDAe-dA_QmA264ZhZDzm4l5G8iG-XUOyBfjj9rpVmxKLy8kKpNUAlBNx5rLbEO6tvHkbvW55u4VdLXi5wmY0iMp1qhDOE6JxNPQkwqCcGk63DUezcC-6j4XNtujqjcM6oQIaPEqXi-kJE4t8RQcg3NQiZb1qnp8m6FT264dW6EcFvFNFDboihj9zCw8kcZVss8HxOfkHBT4AUlvMFyDlt0UR8-Zrs9AsR4bef1S8cOTVesmCXzFvhfxcxhcw2qE35sdPXpn3hGzGGWNZrc1O_Ok9702zS7A5BT9POPOTdIneBYu4sF1kjTKQZxrtJfLCBy1SpKQDUsmznJAr0AP1-HhehngTMF1fOVW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGoGdcHYQa1HlHL5p5zaB_qxI1FLuzgqm1y9MIuWhPHnI6RMRLvIKKn-UKZ4ZxzrsfyZZCLd9E166H594VYrMuqQGC75PYoDF9Q2HWTDpfyAFSeRcIfm3nmG9O414TUBOkd3AIkgWSP7X8A1Dwatw4xoCiYfcC4_LgD-pAGhJBkYkgWSetV2fU03_mCJrNpxiNAdCrpkro-AzWf0t-kgS9dk5JPBvcpszp0Yq_yq4IvBlX4CWD5AvpY6KzWC8-aZyxDAYSMn74llIIwyJRU5W1DPyKQFYB1EvWRZlFTaKHFvOo-g3_3s_LZbBkbZdy9wQjQ8ZdQ9ED9MTeR1C-S50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0m8XnHsT8wTsGTMRAioi676A7NHVa_IXTi41m-Od_yHA9OjHTvm87mymAbczeZPJFrf3agwBRG3JKyGqBGkkBQwqIzql-LJSgAf-K1DIts60Nj6nEw-4oYBqFibVNM9859n5ONzCB0qWjxf0PAmMJmhG5nU-wmglxYIUgjmUn_-wms5MObyM0VXQoO-vdfauUVn0DlCH4y222tYnbrJdEf4L261h1DO3_4gggcVp6V545pRD_081LEffZ4TuOLFI8AbD4DhwUbu6aOY_tMzdJRdFBY-ocRa434ZY-ZhRZ5O9RKLm_n12B7uH8WKwnSfASB8dV4fr8kn6LG9AaBikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-g0ec5Zt5deB2GNHm6VVT0Ifj-dzeH478QdTkKFL1JUSmaBr1jJrygzs5vixf5y7vyARAdf0RQw3JedvBOcMWkIBADwpg-CVahijOn1okNFMdFa063_ooeeRPZjv5-EqBI0-6g3tSqjHvu8hpjHXEYD3VSPImXP29N6wg3IfC4m3Cm5vrH7htLvSsizkrOlGJWWnvfOSVN1TEfYY6LSkCqb4jEWyRl4oE9ZMFLFWAo2IRC9xAF872Svs_XPoeaKr_88DwsViGleQTUzzGp2yrnvuly7Z7gtXVhezJY_w4bNWr9BQcUOIxcEg4rjBOgNd80NfBl0x6LXjqVixLgbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=CMhGsED63pWLezEbkNbKuAVwSOBVHj66GJuIOHWI1ul72yW0S5SpzCAmDn86uXL1KymztY0wNorJ7fM71iEgBQM3L9XzmOhiXtQpdxgjF1EW_RN-yp2y5w-JcJOAMRBRugHq5Oahzum-Y_yF45CtnXaBgvXBsbhUa7ZqBnBSobN-vQFe1oUKiAjd4-iJIiZEhXexQN4R7Z567yJBESF8oFzCTdrw4H1l0yyRZjzSUc34q-pOZStwzu1kI6gMpXFAoPvRl3M2aN_vCiaAHA7DE9LIETnzwUNf-XbOhMZF3IKQjkIaIvgJN6gLIbAhi-3bY-DMdqHcwJXC7O5S31KifIGIPDa5LYa-chJGDipRWT-mANL_-c7_BSdKgtGWeeV5HVzvBHz04drLAdvCGsoCTMjVhqbc5E_MfaixZEzwa4mAISCVQGmO5huFCXHCbC-8UrvCR_UyaZn9948adHQ-U0hdETZo9uZYiJnw3JNZ4l091gbr7hrZLEKOQX8xzeJYwuZ1PYCzmplTb3rloFfn6cRQtcxLsEm9SgcL2ZOCmlmhB7fI4Wghluoo7T_TIL2ZA4WhuPpRYWSnyamyhMZOvT0MkjpkUPYZTYwlMePoHXE-bHXHeweDMEuLPRsLwcAw9yiWrc5Wl7w1ATsMcWuYeV-iNL3KgVrb_TUrrCIP_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=CMhGsED63pWLezEbkNbKuAVwSOBVHj66GJuIOHWI1ul72yW0S5SpzCAmDn86uXL1KymztY0wNorJ7fM71iEgBQM3L9XzmOhiXtQpdxgjF1EW_RN-yp2y5w-JcJOAMRBRugHq5Oahzum-Y_yF45CtnXaBgvXBsbhUa7ZqBnBSobN-vQFe1oUKiAjd4-iJIiZEhXexQN4R7Z567yJBESF8oFzCTdrw4H1l0yyRZjzSUc34q-pOZStwzu1kI6gMpXFAoPvRl3M2aN_vCiaAHA7DE9LIETnzwUNf-XbOhMZF3IKQjkIaIvgJN6gLIbAhi-3bY-DMdqHcwJXC7O5S31KifIGIPDa5LYa-chJGDipRWT-mANL_-c7_BSdKgtGWeeV5HVzvBHz04drLAdvCGsoCTMjVhqbc5E_MfaixZEzwa4mAISCVQGmO5huFCXHCbC-8UrvCR_UyaZn9948adHQ-U0hdETZo9uZYiJnw3JNZ4l091gbr7hrZLEKOQX8xzeJYwuZ1PYCzmplTb3rloFfn6cRQtcxLsEm9SgcL2ZOCmlmhB7fI4Wghluoo7T_TIL2ZA4WhuPpRYWSnyamyhMZOvT0MkjpkUPYZTYwlMePoHXE-bHXHeweDMEuLPRsLwcAw9yiWrc5Wl7w1ATsMcWuYeV-iNL3KgVrb_TUrrCIP_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=ZyL2exUkD1SfsVC27Z3SaEBDrPiUNHxBdZRP-CQjAC3wfB4zbZkdpSqCi2la_5mz2iRw1g87a3DihvUO1Y5VQI2H2z3UX35E4Zv1dwosiqDA6w3hRO7rNwnRuXkMCNPT6sTGc5cgJctPu-up16z3vlog_1iv6lboi88uHoPo0eub0OOT5QwQzsUn5G7i0Epg3Lwk21Vsq-b19GoMgyuu4eyXmqOc7TM9fuuM5l-mFEVd8xjH1Gv4rDUsqWhz9BwT79fFpHwFVbVUNcaMY0Jwd5xpdi7IDEnpyX566J9SvID7fE3JX3BNcUeIFy8tUeKhqAIsmKCz5G4Ps7Qau4-8aoQZSQRmcOp3pl8XcJbL5-k40xp8DgXY4xfEil8d7pFyGtwSp1XYkiS4Mvs5WkQe38ZOSHR4BqRosRDHqBKP_ho5_kaoMQ-MBqVrTnjmPouNyJ4olVdKqN0xxV_0mc6iHAqpavCMqMyCrA4CwJE9t8nHDBVAfZHbzmHeSreGc-mKw568_a-hTrAIDr1ha9o6ZX4RTfsU3D2KK4r7yqsNQmsi4bzdwpvfm8j8snYAsQsJ5tWrRU4k5unAUqnj9pCpO3z-ACbK6qWEC_SnnWxEJjXWCSxp9YiquCB0g4EYnStQ_1bmkACo0pR3NjWuYEEefuQacA598sEwDSsHw9g_cYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=ZyL2exUkD1SfsVC27Z3SaEBDrPiUNHxBdZRP-CQjAC3wfB4zbZkdpSqCi2la_5mz2iRw1g87a3DihvUO1Y5VQI2H2z3UX35E4Zv1dwosiqDA6w3hRO7rNwnRuXkMCNPT6sTGc5cgJctPu-up16z3vlog_1iv6lboi88uHoPo0eub0OOT5QwQzsUn5G7i0Epg3Lwk21Vsq-b19GoMgyuu4eyXmqOc7TM9fuuM5l-mFEVd8xjH1Gv4rDUsqWhz9BwT79fFpHwFVbVUNcaMY0Jwd5xpdi7IDEnpyX566J9SvID7fE3JX3BNcUeIFy8tUeKhqAIsmKCz5G4Ps7Qau4-8aoQZSQRmcOp3pl8XcJbL5-k40xp8DgXY4xfEil8d7pFyGtwSp1XYkiS4Mvs5WkQe38ZOSHR4BqRosRDHqBKP_ho5_kaoMQ-MBqVrTnjmPouNyJ4olVdKqN0xxV_0mc6iHAqpavCMqMyCrA4CwJE9t8nHDBVAfZHbzmHeSreGc-mKw568_a-hTrAIDr1ha9o6ZX4RTfsU3D2KK4r7yqsNQmsi4bzdwpvfm8j8snYAsQsJ5tWrRU4k5unAUqnj9pCpO3z-ACbK6qWEC_SnnWxEJjXWCSxp9YiquCB0g4EYnStQ_1bmkACo0pR3NjWuYEEefuQacA598sEwDSsHw9g_cYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKeEyggqHIHj445dg1Wvaof6sYbXmPlVKfShXdouazSQxNqXNULbtil0CFkDhMRv-82gB1oWEu3oCNbYaRXUS1yVd_4H46cRW1xe-Yx3OY8FCkfz_5fgqlR7_FWwQE1tRm3PE_1EE9TzPPpzUVTLm1gO7VTcr6jsSzGSf_VwAfv9raorhQs__cf6-2dB7_kF3l-j0NyKPTnGnHHe7l9akj6UNyU8kUMN5_a_LAO5Z1iQpEpkVdvsYXNNRANUpauvDkOQXLWmdbDXzuBSTGBVrpROu4ZktJJ5vcdHYbovdbqJf15aagVf0mCS4PUpg_mnQG0OJVsJVOP8qD8ebvZQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=KG8Fpy0xqAVhWKDX8-MdHq4SscS4YRdoz2CaYs63l-lTZOY-PJDOKWqjbQoJeRIBmFrQRgRtQ_-mJ5J8omQmqCnR0RB4XhAKZR-ZSZDqbMW3TuNc-Iv84O84gUOgSc0fd02U5S3lqL2bCQ82fKxDa_SVt7ZIip0h4H6_X2Hs9Jy7hk-vKpeznyDd9RldVvx_JFqHyQPPcYT8Ls-Or9F62BId6nlvJoqf-copBo-r8ML_zFKRVp6hK3yUPRaogRvhpLf0pxtUJCRlWL0DGyUxFQzUqGQ5NZfg04seW8g0w0rn5KLhAG43KqQ15uDTjEM9CcPQH2nQniCjNE0LnB6Swreqma02e4aC_dBK6_fDSzpZg6ub5HACYHrv5bHbwsBhVVczr1QmkiS1LaHtmJnV1XPMl9CZqVQNMYswa2SKsGzTfqUmsBykkbrdRieMpyFNgcnRkfA_m862qRWUZdAdT7sz04tEqo2YyCphLQD2fq8pfWcSijbejxRxCtNTMmqbZ3Dd6rOGcaI94qZGp5pfOcn9Qk2FJDxXadRFuMznARAF8VRwrkyQuVncLUTb4THr6fkxmhISdtR7d53FAMu7d-a0qbsEMN__xVYIYbZwvi5IiDrn9zb1wlo4ra35AjRRk8bovyL0suLkBMAfJaLkHkW-uqwDEPzfWJ93sRQfJGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=KG8Fpy0xqAVhWKDX8-MdHq4SscS4YRdoz2CaYs63l-lTZOY-PJDOKWqjbQoJeRIBmFrQRgRtQ_-mJ5J8omQmqCnR0RB4XhAKZR-ZSZDqbMW3TuNc-Iv84O84gUOgSc0fd02U5S3lqL2bCQ82fKxDa_SVt7ZIip0h4H6_X2Hs9Jy7hk-vKpeznyDd9RldVvx_JFqHyQPPcYT8Ls-Or9F62BId6nlvJoqf-copBo-r8ML_zFKRVp6hK3yUPRaogRvhpLf0pxtUJCRlWL0DGyUxFQzUqGQ5NZfg04seW8g0w0rn5KLhAG43KqQ15uDTjEM9CcPQH2nQniCjNE0LnB6Swreqma02e4aC_dBK6_fDSzpZg6ub5HACYHrv5bHbwsBhVVczr1QmkiS1LaHtmJnV1XPMl9CZqVQNMYswa2SKsGzTfqUmsBykkbrdRieMpyFNgcnRkfA_m862qRWUZdAdT7sz04tEqo2YyCphLQD2fq8pfWcSijbejxRxCtNTMmqbZ3Dd6rOGcaI94qZGp5pfOcn9Qk2FJDxXadRFuMznARAF8VRwrkyQuVncLUTb4THr6fkxmhISdtR7d53FAMu7d-a0qbsEMN__xVYIYbZwvi5IiDrn9zb1wlo4ra35AjRRk8bovyL0suLkBMAfJaLkHkW-uqwDEPzfWJ93sRQfJGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixtIujegg7QY1PzOxTvMfedl01Dj1isuLrTvKadQzsE5B2uJqNMgMeL2qTOSamiRX6UkOQe0RAMbyzm_nCBwWDzsgCY2wwuPiNPxvqJFoKgUq4W_o2YuVZnift1Y0n4DO3q11HCxr0e35-3EBnFikDk1fANiPa9POWolnIHc5_KoZRLUfK74ypotLhbsuWmiFvges56i9Z6Hm0lRrtdf-3EzfJRNFEFza254z8R3UZCN-Ub6mUyEX0X0kKARknmN7gHXy95ig1ozmrtfFm85xMh9-cVRL19-oUAnr-IhEi9tKvXqfl3rt4Q8dji3xbJqqeoYotnGG3M--ajj53wffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye0-9CzhAjFnqTzs8it7dTV78JGgtGtSoPzj9ppTw2Blc2KIy11P7hYxZXTxC7sxgeG6uYDuMuwSaWKZVFDLUtxh83A28U4j7wjSZrMCALbn-wkZZ4znLYYdf6bEsQZdS2Eh_davfR4uac3ZbXHYPC1TqldonO-XFL40OgZhDPjJZYVg0Vk-Raav28-g0gnI0CJ9ViIawcmkmLuKMYeP1XemmfFYCjG1E806ABrYrVVKDYJoW_vUaSSs0ImQXcwy7CIo5gLYXC-Y1xMeogMb8FbuKUO9VetskLgY4eIazxiUyAHl379AP_pLdRbV5200pWbQg2DJVc0pZTjuMDdj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=C_36mJg-HBcyIj-PFTAX3sDu0qFNig0diaXzAUGYTMzlneL_GMtS0BZEdOJ-jpHvKXPUc3PdqPutYhRBNvmYFBPflQKh5RiFIfsosQJtDtZSyYBU9ZfI9FcCV6500wFDi97xVJT0hiKVkxTDP7HldOLEga92y9pUggus0wc_EYV0CgWAHsnDBYJ0VmEJDm38OJdnNnvTDihe7XprNDW0-dQf5HFTrgjm7E3vRX3dYAnJ-niZDtrShkuIot9Q7KCOxVskQrjKe5FmqZ42p6liBgo1bTtLtMoteExRl3grZ_lVqpjQkkJrjNlkvyuf-3NWIObFizf7kO_kGMQ_14m9PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=C_36mJg-HBcyIj-PFTAX3sDu0qFNig0diaXzAUGYTMzlneL_GMtS0BZEdOJ-jpHvKXPUc3PdqPutYhRBNvmYFBPflQKh5RiFIfsosQJtDtZSyYBU9ZfI9FcCV6500wFDi97xVJT0hiKVkxTDP7HldOLEga92y9pUggus0wc_EYV0CgWAHsnDBYJ0VmEJDm38OJdnNnvTDihe7XprNDW0-dQf5HFTrgjm7E3vRX3dYAnJ-niZDtrShkuIot9Q7KCOxVskQrjKe5FmqZ42p6liBgo1bTtLtMoteExRl3grZ_lVqpjQkkJrjNlkvyuf-3NWIObFizf7kO_kGMQ_14m9PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnqr0PBRUEHeKSMD0S69m47jMGPQVGIcLzQwqWFdYfqDdBGa8Nb0cmwDXqDxL9XwIf__4tSTlWX272YT2hCjqW-adMwUCkpI1JBZZ3cn40qe6juJDR8uWCWZ0USF54BAIbQomdW-TqEVj6jvux7G_dV5QJPI0duv9z8mzN9xupsZ5SoVABBZGwAvkTJTgEL4jFYkAM8KTkd7rEeNb2iCZPKoTnwCrl_k07esSMJaEuGdzKrOWpewc8M71UojdAg0rnOsiQcvi-ooUnLpZI2o-9P9U11p_5SH3lUTgBSPw8d8UbJxQAuKNnn4LpMMvGMMR4EuhkIatHUAeyx9-sKovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUxEPr3apFquTZ_8w_S2-oNGXmvCwey18vk9tiFoCb8yXpqgmiOEQD4cByF_PNGNBIiTJMBqSa2RJbqFA10c9gocawTwsYXlQsBZsnWZaWLCZwasKd_tsZ_KAt0ZqSSByfO4JALgfY0nImw80nk9G3tZUDeEY29EJbGwgDs3d7G6eWjsVqrQf1-Bj7OChxAJKex7SNpnkskeJ7yhNxJzcfqk9cePq3aNgMHlkrOml99BZ0r8AAlXp_4lHtwym-jQeznOZZLvvFM4O70Qa2uS7GwNe-ZS7XDLCIoznGR66uQVbApthzYz0ch-4SCQtWAyRa1MPAoBSFoy6HOBbm2GwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2A_URXUIKu0lifoTk1PYXqA0hx-lhG81NzYNSJt7L86WGYf0WquyIeM0wZcBylP73fE2GrAc6NNPk4PLaXP5IEo37XZt7PWN-6w-PqXds1k3XZo5hXwqwu2S6dALF6Mz_drHyor-hwvKKKhSwWTqdL3xeu-8otuQxYEfQaen9OZ10eq8ytliY_2vaLL9NImjr0DrR-UlLo9_7uc8d2EP8Tzw5mqqk6zw3KGC3csE3SDqT_D5T2gn901-C6OkkwEevMlpD3m9ZTwaF49QmAe1v8y7XsWrTKRYIYzj3cyod4t9X4z8rnmoy61H9cZvNTiJQOGNyLNp4IlhJwzjCWbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JZv-gnE0zmG7oWGMUbXJ0mSQko-aY38UAbeJUqadeT_1BDDqoMuoWwwvWDUhAXuULiWqnSeRwNRfz8akq2Ii7BbVBh3TmT9sGfb9AGiBmvpvCuigbYR1BpgqqTBa8buf6MjAztE6kNOUrBqNlCMrx_ktlL6SbAoUrIut_y8L_Gc6IbJQshWgtRjQvgUPgkcsGEYIJaSd9AakuTQxptXqzMRHRPkTgSQY8tIQRZbsGoEFnqOOXtA3xWWcQ03V7kAi9Nvhg8kEy5YjNyA1TXIzmBF4dY-Kh1A1flU0guo2b7LWg0MviPkMIeMDtSmOcLWHaCF6JHcQL_TEQX4BTB1aBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JZv-gnE0zmG7oWGMUbXJ0mSQko-aY38UAbeJUqadeT_1BDDqoMuoWwwvWDUhAXuULiWqnSeRwNRfz8akq2Ii7BbVBh3TmT9sGfb9AGiBmvpvCuigbYR1BpgqqTBa8buf6MjAztE6kNOUrBqNlCMrx_ktlL6SbAoUrIut_y8L_Gc6IbJQshWgtRjQvgUPgkcsGEYIJaSd9AakuTQxptXqzMRHRPkTgSQY8tIQRZbsGoEFnqOOXtA3xWWcQ03V7kAi9Nvhg8kEy5YjNyA1TXIzmBF4dY-Kh1A1flU0guo2b7LWg0MviPkMIeMDtSmOcLWHaCF6JHcQL_TEQX4BTB1aBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Qb-M8UofxWuv06q8DtXsDkgiPi85qC3YlrL_J9M4orkAKuenM1piCkUjEAAlz6SgNiZQfNZhk0YcpD4J2DyXOEHywl0fuMJXvqFzvOqWJ7LppGO0wIIUgsAVXjJXA0KiEDKOysCdMB1fMB5xz9J1etBE_u_0seTZ_tOAlGfmTqztbuA3zugv_Wphx4r8h2w96wKc-9xVA8Eo23dn6RLYsYVxwfSK_pRXchEEG1eP6Zh0ywn9JAQ1ZcTNjZwGHsOBuIIO-0CfS7FgLcLq32PmsSQFYqGLLonSA0iFpXkPA-ivFbLK8zHsvC_-kqsQ6gHC9HDctT02bgGkLoXw1rfcPJxBvp9s9slx_lmtqnbjVtCEOY7fGmuOnnPRi2MJnQFllgPbxNPAAg1VLm1TOlViTNPAcsUXKaVD9ichimYya55jLryVNOGUEKCvw1SZgmwmmoyNm9YIrgJ_RL24Wf_j0f8IgGNv0CyO1Ze5yIiKaM5Xk9S-limDqNjFnM2pUU577ufVOIYywOoAuAlNeN05uYw8Quh0RKXegM5imDWy7XecbZI6HXpBri4Q_5Cg7cE1hRnDVl4NzSZOorubTra06F9vrCfBIvhU-yrW721XEMjMRyZTd71SGuihWNY7FhS9Z8SDlWH4BhO2e3DdwiSIM6e4WINpBtGKAj25Jv9Vg-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Qb-M8UofxWuv06q8DtXsDkgiPi85qC3YlrL_J9M4orkAKuenM1piCkUjEAAlz6SgNiZQfNZhk0YcpD4J2DyXOEHywl0fuMJXvqFzvOqWJ7LppGO0wIIUgsAVXjJXA0KiEDKOysCdMB1fMB5xz9J1etBE_u_0seTZ_tOAlGfmTqztbuA3zugv_Wphx4r8h2w96wKc-9xVA8Eo23dn6RLYsYVxwfSK_pRXchEEG1eP6Zh0ywn9JAQ1ZcTNjZwGHsOBuIIO-0CfS7FgLcLq32PmsSQFYqGLLonSA0iFpXkPA-ivFbLK8zHsvC_-kqsQ6gHC9HDctT02bgGkLoXw1rfcPJxBvp9s9slx_lmtqnbjVtCEOY7fGmuOnnPRi2MJnQFllgPbxNPAAg1VLm1TOlViTNPAcsUXKaVD9ichimYya55jLryVNOGUEKCvw1SZgmwmmoyNm9YIrgJ_RL24Wf_j0f8IgGNv0CyO1Ze5yIiKaM5Xk9S-limDqNjFnM2pUU577ufVOIYywOoAuAlNeN05uYw8Quh0RKXegM5imDWy7XecbZI6HXpBri4Q_5Cg7cE1hRnDVl4NzSZOorubTra06F9vrCfBIvhU-yrW721XEMjMRyZTd71SGuihWNY7FhS9Z8SDlWH4BhO2e3DdwiSIM6e4WINpBtGKAj25Jv9Vg-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOB5zrFtsUeigoqWwzxrM2afxTgBVeTM7Usm1ecl2lxgJ_-Bclcn73WlPuqn2l_RgkmpLESOvdXNJC_3Z8JII59xS_G6jjfdjlmVZ_OLJvWotkS7aZzZmGIObE5MHb0eMcTZbdyEbxBGmn1dQDZiHsl2Tmps-RATxXxM6UTscYYXLkogi3bGtvfRS5sfMPyC1i5qBo24RoFpRxtzMZchn21EJJh4xyyga5eV0M_7_MPbUjjHUnFpoJ5Jit9Si8QJgKhgJWoCo4413LFjdSLC60atkJw2_LrmMpgtGmq-kHeXDZ1_kaZUgRyoGoGB233noDZnHVPkIydbBs2P6-TP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqznTp-F1h0xLtZadx1Q20KDV7Hm31f4uCEgllLplpZt0b_JiinSrgVKz-_Zz3bbZG6tWhVNwQYsb_rkNN4mhVczwZC1bpmpFPa-j9eFu5Yq1u6JD-9RKyHtuNkk8cq5QrKblJjVjqCPiyDi3ovlqch0AqGbsOcj-ZMmPGzX7Ze1UYtQWlPsz8vXc1xNyHHJTV03oGbPT7ikbNg0wyWfc2wdovoRHNyMMHezGta5--1O7sYbQdQCewpsU3E3S_0a9Jf94Kq_AAtUbPNj7d6KWWIGQpY5j4HlZAO2CYayyzfefd-RWvRcih0lmyEjvpuY1McLcwr-B_scGfxT9rUthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PEG2WMw6VyxBvePte51YHLt4et-lwhpVhXj1p2LHr9-h43MSdGhZ5RTkzBB2jQJyw4UB6EzgeCTmEDiLotTA7NKPgTRiENfI98OtMkfqQ7oLnSaeJyGAXRrG5IK11x9l94BlWJPE2NJNEzpdh4pGjbwTPS_UIWrPD-gPQPebOSgbk6ro_EBdhs_Q3vedIRA6N9JTVSgr_UtxzS_2VJONkKNl2lSF_Y_iJGFOqjDi5IgGOuhMRgMJX_FgLg6I1i27vfiy-SOGyGiT6gNfLI9X-Jg6uskbNR7AAbFp5-vmiAKAEeL2ZLRWwEl9uQZcDw3jbg2_tNJke7I_zf0c5q1f8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=OiPmOwo_DooSSYvpP7F-oPipFbSxr5N-ILDOE9swkJBX7PsagC7t1yhIYqoZf9El5x4573h74u7DOs9iPu4zYIYPWezkweWq9Xyb8N8RcN7NxhjUDRwUVSMczdDkvPu0ho4hZ7x3KJaTqrzjN1eRc5nJuWurKMKePVLmalvrJr4vMupTkkIK-S-wQitXUsoAuOk4b12rVHaX8kz7BYFKmvA_wsqRvTXUkz4ItB2Ld3cqbgX3bIF2Cz5nlFBOBwzbQRc5hCmaSu2Kl1oRmNLLoiVAkD4OJNDf-9lQLyQ_Y37kH303rXt2q--23xnFQiq3HtEuk52BTTzTwEU8L3gaSx8hecNh8EPbbeV7wLodW56KdsmZA3_zk2cQnE73rCH6r97xwLYNIIoSQHd93XpXi4OTL2sHMjeAxOkYBVfbpRzlG8SFy6moMDzXFh9-wOP-uqaLeNLkRwpiaqWVk2vdsWvHx4hP0jOorSYNQgur2aoeFt6x-h_TD4XYcBRLA4XGHGXPl_FLMecrjr_1ZTb5P7W9qU-cf10rVYtpjMk2rD0ke7R17_E_tiAUlA81hSf8vTTtSPy7vSNsoj5ced_qKc8ZOAghbRUq8saQS0H9XcJ3v0-pneXunml9syVegrIpjQMv1g04bgNhyXllPsVcy_Sz9Yt5dBkOETcGK7R4MPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=OiPmOwo_DooSSYvpP7F-oPipFbSxr5N-ILDOE9swkJBX7PsagC7t1yhIYqoZf9El5x4573h74u7DOs9iPu4zYIYPWezkweWq9Xyb8N8RcN7NxhjUDRwUVSMczdDkvPu0ho4hZ7x3KJaTqrzjN1eRc5nJuWurKMKePVLmalvrJr4vMupTkkIK-S-wQitXUsoAuOk4b12rVHaX8kz7BYFKmvA_wsqRvTXUkz4ItB2Ld3cqbgX3bIF2Cz5nlFBOBwzbQRc5hCmaSu2Kl1oRmNLLoiVAkD4OJNDf-9lQLyQ_Y37kH303rXt2q--23xnFQiq3HtEuk52BTTzTwEU8L3gaSx8hecNh8EPbbeV7wLodW56KdsmZA3_zk2cQnE73rCH6r97xwLYNIIoSQHd93XpXi4OTL2sHMjeAxOkYBVfbpRzlG8SFy6moMDzXFh9-wOP-uqaLeNLkRwpiaqWVk2vdsWvHx4hP0jOorSYNQgur2aoeFt6x-h_TD4XYcBRLA4XGHGXPl_FLMecrjr_1ZTb5P7W9qU-cf10rVYtpjMk2rD0ke7R17_E_tiAUlA81hSf8vTTtSPy7vSNsoj5ced_qKc8ZOAghbRUq8saQS0H9XcJ3v0-pneXunml9syVegrIpjQMv1g04bgNhyXllPsVcy_Sz9Yt5dBkOETcGK7R4MPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlqJPtq5rBvYWWqUNgt6q3SBcDqUE0O-lSRnSTQvBhsZ0c-4dM353VGC5zXwkBMnb43K8TwvRRfn5p7hWfKw3PQzebJwpGbIFNIspA7hcMCeXoa075EPXqHvOjaQd71ejhbLdhFMlXlvok7s9dBcl6b7qaOB6J0_hb9JkWUilOWOPsqs4qOosdm0-z73wdylM_MDHn_0eAD33zli4Mv2LBCf8tiNjRkw0pJKa3rPINV3t2Bk2XYdIVjSWoChBmqXm4sbHRFxafQsSSZ3-P4hgWUjA2lHXmWF7Ixgbm8Vabo8OLnLHGnVvsaNqNWvU_bOGjD_X8ydXBdPJgXTFdMLTog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlqJPtq5rBvYWWqUNgt6q3SBcDqUE0O-lSRnSTQvBhsZ0c-4dM353VGC5zXwkBMnb43K8TwvRRfn5p7hWfKw3PQzebJwpGbIFNIspA7hcMCeXoa075EPXqHvOjaQd71ejhbLdhFMlXlvok7s9dBcl6b7qaOB6J0_hb9JkWUilOWOPsqs4qOosdm0-z73wdylM_MDHn_0eAD33zli4Mv2LBCf8tiNjRkw0pJKa3rPINV3t2Bk2XYdIVjSWoChBmqXm4sbHRFxafQsSSZ3-P4hgWUjA2lHXmWF7Ixgbm8Vabo8OLnLHGnVvsaNqNWvU_bOGjD_X8ydXBdPJgXTFdMLTog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MW4G4wjsplOqDlCE9jf04UWtUFe-qtsaQruJazrGSNbCnkGYaCs4B-g0f9KjcFdKC6vCD2hWx4Mpcip4VGy0JYE_S7tZ3jovTUtGnVte0XkcF1uLM_NkDgDdEXDPabP9fC9IEM2ec4z_S0MovURETYXnq6tx7z8HHHDoIuZZuCRlc7AELgZaHgYSolr_AE78f0jDv5n3UEeSaYfN3ng4KTexcKs6fKZf8pv_c1Jjb0kwPrZsoAoAac9eC5UyjSPM46pkpDCx4Nr86Q1MdgJTCAI3Q9gsFAo8D_ZifTQQD-Nxj1ae6d2lYJcZm97a3PecKBBAnjMmHxKA-y_yA7WKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhfBn8gRFCM9zke1uejF7wvATN0TZdDj4a-Eify7WlcFn6MQdTxWKViopDv7ZLM6KtlJoe3PpItNBm7qT7IWYdhG8YZMsS7XXhgygRA5ImYJq0jCp-hqe4gn5X3wjJySaZ0k1UnNkQ7HzltUSVSvTtEQVbHOnsBiTlqo4_86C2__soeFVJIvKd_cYrNkQy_JlOZ8S2xjXYsdvbnyelK03NONmsLnHzKPnK71iQE3fGA0D24EgVjTjUr2fzwQFtLInRyQiWD_hpfHDCjHME2O7qdHBmkWlZ0bFwzJtjygIlf-__8FXjHPovVEtnFLukJaqRrr4ccr4bZ-8g9e2ZonWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=C4OP7EE6WsJSSPM362pzZdE7nVJa4CjKL_DWI0miYDyH1HCe-F-27UMzayD3wBDCAU_9AbkHe6pOI7IAmiZx3Jyp_LYHu_lA3PJQVwoHW1q3zyWeaU0PVTRt78EQjcfAAo3tc3yRZ33Aa4xPwDjkU2S64vj_tldtVc1V2EgcOaIuv2BrP28yU7BdJ7Q7vwXb8k5BzqLHc1kAAy8psGRq-j04mp2KjD6Wl0fFIlpT6fRmh3Ut-lHAfuG74ug9FZVv3ABddFPIAiBEQsUdpbk8LPNvXvJzFHezExCvblZ6dhe6tOm3P_jSAhLDxFdXRIR82QUthzxrsErKl5fI7QJvHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=C4OP7EE6WsJSSPM362pzZdE7nVJa4CjKL_DWI0miYDyH1HCe-F-27UMzayD3wBDCAU_9AbkHe6pOI7IAmiZx3Jyp_LYHu_lA3PJQVwoHW1q3zyWeaU0PVTRt78EQjcfAAo3tc3yRZ33Aa4xPwDjkU2S64vj_tldtVc1V2EgcOaIuv2BrP28yU7BdJ7Q7vwXb8k5BzqLHc1kAAy8psGRq-j04mp2KjD6Wl0fFIlpT6fRmh3Ut-lHAfuG74ug9FZVv3ABddFPIAiBEQsUdpbk8LPNvXvJzFHezExCvblZ6dhe6tOm3P_jSAhLDxFdXRIR82QUthzxrsErKl5fI7QJvHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
