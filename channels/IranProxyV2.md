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
<p>@IranProxyV2 • 👥 39.3K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 21:26:25</div>
<hr>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKjXAIw0wT7JZWw9GTj_ATX_GPvDxnE26G7icigjQpanCesp2wtvPvoaP8r93QVqRk1QD7-BmFYO5uEOBTGur6iEuElxvNDy7Sm24CEZEj8jtfC3ei6Q54hHZgBkkurQpDAR7jKQqXQs-Md1dyOl6FZncQVevCbefj9JE84XxxCPk6N8gOlNdtoSJPj4cQW4rxXkl2aylwKHcV4TM6woG8atSvYhVpcfSHZxFT-5VhFX-KTVPQx_DeUndltixTS8pR5E9Udl92QDsMDXFyJDKsKmlWfjjUDWrJuSln3LOuAkAtdJPGcDzn3nhOZVAPW7UR_4yy36zbWdalm4x6IO4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP95u7JnO8mtq6_3CMHEGp6XVCwFrCyCzoDEINmSPx81DXGpI0WypcmuqCt7UADh71MK0BfC4hDPQtLMioLZqPeOo5-jnbYXY0DSaZlF1pK_TTuDwusMbq8kSabs4XQHgzThud096rR3KeQ3eugs_pWrxBYkq5Htp3u_5kzgYqJB6IduJkNWie5FTetUK9N_veHjVZqw9Fm1psNu8sv-1c_C4XzY3G-VxQDPus_zYHrvfLBqPiNGlfkl7q-YV0GRgKnLjAkmJk_dD-MCkGPwTlzO0ICNPqIKuPF1vxqrr3L8PEkGDlMcAYC_SKsQHK5C10z1EJ1z-HwGN9a_QgoO4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsAHZo-LaJaa3XReMCp5Xw0a7BhPdRxJC_Hux7h8JKhyLjyQbIA9MXSNHa-TPgC61f1ldKI0MwazlD9n6hU1dO3nm37TEiaJ7y9YavXRp3Fah7hzaOchu-tq7Af-i7dtUyudI3yRYdypDlYcepxSoawp-FANJoPqVJfd7r2kenxV104nGFVodNC8izuAwN5G-1b7BA8vwm8EB7ndl7KiA9M6wzR_BS0-c1YRXp7QNoA1T4WeXoXOpsxnDj9GVGPVAEkhAPz9BTEmYTWwu92tJxs1RWi7cFE_DE7wn7zPsXEGpeZDkbmd7_HvyOIqP3o6yBFNy2OlgGsBkOi3ae8Lkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mafI1O4zvwe_1YHmFpdwl_s3S2NtcYEqHtTKzvyalX5yJAdsx28tPffLR_UFTrWc6XhQoUN5KHQQsmI96xsOHIYmcKcKuVk_qml8XaSW0-KCujOWL05gUGRQphgZPuHuAFssLoAp1voVGBII-M95Y7fzZ3jLRn-roC_raa2qZ2YIXH_XRTz0FzbwliV_TNb8-SF3XCdElwbTVxso-heVS0w1CDKgOISuM99XiOWObmLGnvq4_HSF1DBD4ND97LOiJR1x_s0XK3COVqug5aZ_T5yjIJ1M1uQ99-ZcIoEHxdveIAcAv7_jeQav_GYwQcNTPpn0UMSm_hAbHj2XjmPJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8UTswo3IshG-d7crjM7stL7_vYVk9yopgz1eIJyJRs9dT1CvJ2EjV3dXl6lWmR6ITs0hlprTQlHxK5pvwYZasd_w3xzkh5mWnn4v1s43c28oTe-5r0DH4UUO-C7-zi-smR6Yu6iXvFNNjRy-sLOntnJIF7m4vTBU0KEwM6_3D7AWt0no1Iox3-BRqpfTkbtgpT8YUGjrhgd6zJDrczXl74XMZiYhW1q_S6w14MTv6WJyK3885jq4aExL3W1Cq01wmtYWg4KUdnJvvImU5jsDYzHgMq8soQgb2ja5NEy4OTltQ36EZTEQawH2O6TDY2pZ1hgYf5DChdS3FiWRWJ48g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmgHKf3gP3n2rWHY4MKBLapLYdbvmnKMMARQO6P3K0J80akhEvhkohDIQNgCOMndgMvMRs0CzrzmMO8IIvEf5WF26oCURK7fbG8xBX5u5jvdbSfads2I-3ykthCLlMcp_IO9EqPlR0bIlC0-B9CgVivNqsxLi1Ngxrxk6GeBMhYAOX9T1Sznzin4Jt4YDkdKTXrpdTM107q34Jr1odq5hhwy501BV6_YOH-IFVTALOVIk5zNuh-WrcMtecbpvy74pm7lpyEcF26SI0Bknw2mCkj-LW8ugXlLmAKTq0aQAlE4gNNtaHJlPGOMdpO4NjoMwLhKHEyZ2bsvPrUX3TY30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW9jS2agIXcvZY_sHDIhd4QKOxyxak-tDJlHvsf2ZN3UNjvOIoryLmlxVlh4t_cY0k-zqLZVsuihFlHGDrcHAi4PP2R-FKow60qwK2cZH2kdt2C8FC7EsntVV-nOhoi10pf7bDbb8Ukkki0BfK2Yh7nWrSOUkg5RJjI4G7HnnBMM62lOJC7ZGwggHumhJDzO_7WhX9flfiIEHpHOvHCrG_3eQO7CwaqKDx3U7CaxJchRz7uQLEpKqwLcEVK-0rVkeBxIkMCaPT5pRhGaBVMhpFblm_-L9wmOEjkQlQ3fla_ysQYGVDNHR65UXXVmvpwct3CPEpH3cMG7NZ56iwSbBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw1hdEW7t7NEzjYL_bqtMCpmjKeBhL085wEssWJCGEYTJjEvxOZqXy-4DkdUiVMw6GbHDDzQ88wncTIMPKGp2rc5LjM9xPTw4Hz7Ooe3ARNUVyvsxTspCHKwANdf9F19ogOuDSqeqtP9THS_OSS3J7Iq7FJQOStmpnx8gScGtHW1myvMkLnKM5WjpfQqjzS7taL6TmGRe7KqTWu_-l6BvvtsfBET3wXbOEtGRoxRawSbRuPr5rfnkg5k4_GJyz4ruxRaalnbxUEx5636Tkk3_aIbJWL1AbYWEkiS_ZlG6H02RXs_xPar2jWtS7BfnK5gFeIILp04rhfJYiR087PTsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=vIOWs_RQPzVMhIuijMLByWhDSqjx9cEM-4XqwOEPD2K3PEj8TqRNZ3S9WKmeg3ZzikfaJmtef53jp0LrHbiWQ9zU18dkacBFWGeJHU2TAhZOsHrXKg-WLdnC0o6WQvMuneNLZ1EnzzBZTL_7tvVS6brg80SNqNYw_Xr_yJX_Ed_0qMYHVID1tGMzKI12g8_L7J_TVzSVd_PAIOLXWtEXco8dJddIrrHiE1djPA1jPXUdKufWpf71o5YHzxRx0IwmIDQ3O5R5ifJAjPFCSlcZTv8B5fwWwsWHUvZgd5vEFkIVoXVCMxhBQM0BjERkGQcfXhL2xspdJIdm_LARtI5Ya0lvIyDGSYfJK9hwKYaAH_tTws1FQ-DhRYhCXKDzDMUyb5EkQJ9UlDE73kyDYI-wzp249L79kY22AJvZrcTUsDMCjAFKIw2Ss2GclCoI6LZ8R6BtWKlgxIPLEddf3dOXuzX42KuTzjJh8RF6emlY1DJkr0wjhlMx2vwikZlkaRsBllxpqq2F2I7T0qi8t860YGAxzM8d5DstAZTkZnvlzL3PztNWzadhXPxjvadLOFxi5UPDTXncEyaICHC2Mq2hWKbH1BnsbDftwTMrrdAXJwcEaijEdzCXhHCG5u4hg0jX1gxkF0s2OEf7cKN-QCqeYDxOw5iYO9nVwNnygbB0fTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=vIOWs_RQPzVMhIuijMLByWhDSqjx9cEM-4XqwOEPD2K3PEj8TqRNZ3S9WKmeg3ZzikfaJmtef53jp0LrHbiWQ9zU18dkacBFWGeJHU2TAhZOsHrXKg-WLdnC0o6WQvMuneNLZ1EnzzBZTL_7tvVS6brg80SNqNYw_Xr_yJX_Ed_0qMYHVID1tGMzKI12g8_L7J_TVzSVd_PAIOLXWtEXco8dJddIrrHiE1djPA1jPXUdKufWpf71o5YHzxRx0IwmIDQ3O5R5ifJAjPFCSlcZTv8B5fwWwsWHUvZgd5vEFkIVoXVCMxhBQM0BjERkGQcfXhL2xspdJIdm_LARtI5Ya0lvIyDGSYfJK9hwKYaAH_tTws1FQ-DhRYhCXKDzDMUyb5EkQJ9UlDE73kyDYI-wzp249L79kY22AJvZrcTUsDMCjAFKIw2Ss2GclCoI6LZ8R6BtWKlgxIPLEddf3dOXuzX42KuTzjJh8RF6emlY1DJkr0wjhlMx2vwikZlkaRsBllxpqq2F2I7T0qi8t860YGAxzM8d5DstAZTkZnvlzL3PztNWzadhXPxjvadLOFxi5UPDTXncEyaICHC2Mq2hWKbH1BnsbDftwTMrrdAXJwcEaijEdzCXhHCG5u4hg0jX1gxkF0s2OEf7cKN-QCqeYDxOw5iYO9nVwNnygbB0fTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=biU57zg5OoR2trSPZz4OepPfbVGoeIJvo8Keo7Yam92cLMcpXBqQtafg8ZgySImsy-pI5dDhtenD5Lyx5BcPpZ8U-4yC8vdqLAEV8R2uCYoCAf1UrHMLKQ1x7uE5a3GUL3aO4lxdxpNwoozy09VTu8tV1QWIKbi7i_0D0ZXHgqMytoajJSp_pxgQxINsXCl3XAcypCp3IW6lF3l1RBSPGm5uTywDFKhNHdQ4WixdVvMnIYYTegxKyLaEnkljh_AV-eO2oREedGlwXk59Q1djhHg_BPPbVF6HvfqgvXJ5aZTrO09Nsjf319-B_G0CU-RWhXl1Ht0koFvfqNTNCyHNNxou3oXOpatEqvE5GgSOlJOzf2uRoYRxfMvjFqfQmxU1yv0hHkD_dnPl-NTZWodLhmQFf7ZfGNw4ElkNx7r5cWggkQGSeJyv7bJsDgvzb7I40nGjk4LtzU0uVI6W-d2SdIPhKGUj9fJUXwkWXjILlHDU_uoHSCxSqI9mQDXKBBKxTDylVRy3MDGON2wJDpoeJXwnhN8LEfA9p5-tVcOrN86-OY8qrI11oGGZ6jLQIn3NcYyFmA_6-HLOpSeyPEQ7Tur4LmcPexgVdpFE5GB4r2f56Fi3Bbi2PDn_SBINzvYHFgQBGM6J7wnI8NQVhVcD8ESOJCou0bPEQBOJAOJ85_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=biU57zg5OoR2trSPZz4OepPfbVGoeIJvo8Keo7Yam92cLMcpXBqQtafg8ZgySImsy-pI5dDhtenD5Lyx5BcPpZ8U-4yC8vdqLAEV8R2uCYoCAf1UrHMLKQ1x7uE5a3GUL3aO4lxdxpNwoozy09VTu8tV1QWIKbi7i_0D0ZXHgqMytoajJSp_pxgQxINsXCl3XAcypCp3IW6lF3l1RBSPGm5uTywDFKhNHdQ4WixdVvMnIYYTegxKyLaEnkljh_AV-eO2oREedGlwXk59Q1djhHg_BPPbVF6HvfqgvXJ5aZTrO09Nsjf319-B_G0CU-RWhXl1Ht0koFvfqNTNCyHNNxou3oXOpatEqvE5GgSOlJOzf2uRoYRxfMvjFqfQmxU1yv0hHkD_dnPl-NTZWodLhmQFf7ZfGNw4ElkNx7r5cWggkQGSeJyv7bJsDgvzb7I40nGjk4LtzU0uVI6W-d2SdIPhKGUj9fJUXwkWXjILlHDU_uoHSCxSqI9mQDXKBBKxTDylVRy3MDGON2wJDpoeJXwnhN8LEfA9p5-tVcOrN86-OY8qrI11oGGZ6jLQIn3NcYyFmA_6-HLOpSeyPEQ7Tur4LmcPexgVdpFE5GB4r2f56Fi3Bbi2PDn_SBINzvYHFgQBGM6J7wnI8NQVhVcD8ESOJCou0bPEQBOJAOJ85_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEz2G6rExtkvASyehcL6Pj5KFGDSgZcYY2saCGcE-sZ7qh5UepBscL1dGBBwQev7pbUKTGR0kSTejFWbXSMnFTDYm630ahjHRBKqtZAQW-abDjsSxG9a1qfZAYhpzAQVfKKbKgOihwVjOD7Kdnlam9bkYqpWHEZ_RrAlFyw99DmmjbinzPlbWRfmGehKXKabJbln_jKdnhminSX5HLAzPalyrJI4BBOfRPas0MLkF1rPq9OQ4j9UsnMBcXUoioM4DjIwDH0vr9gwblvhwcapTGBHGDMm8CDBccuAjv0wsUsCDXWYdvLFgjBWPl_rHH-ACs5YVISke-W0J_4Ac-q58g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=r9SmhXYkCMDf9VDd75H0OnsPrsGx3Y6CNDn1OiTfDrbiZ3Tf1RgaAazxKYXk4O5UlxVgLhPwTybjoA_sl_fn8WDHiiZJrr0nHR_8pbO_vB8EK_goWi8RBMf0o8h5ihfBO-j6og1BE-cc7VKzmH5kaZx_B3QdU_PHCSmhSeYN2MHtxrWM6YOp1-WS6F2yYX8CKmLWj3v9Fr9DWYrnuBaS6oeksbIe-5EXIZpkvYZk7NN2_12yczSA0hwm5RAmLhOfZjAFU1J8YTwUautG19OXZTAHxaGcsshV7VyENYuTuDWiFl6VqF1VXTOZz3tuHjQY-facDWfGk2L2-iToy0NUNUdSiNK1eKkciQzkPpN3ABp7C-Rzhk8cT2anTUfJpF8K9nTmwLAGwYq2J3pr-RU8QDY9uRYXxexrRjkOn-DDHTtxUmucoE6XBnEuMbfFiN6zmiUis2ONgRdc3hTS8K_Eo3qk7YzXjhxz5omMPZE_5i0Ie-HmW4b_QfaARQ6cldiF7fwSdmwG0T0lgMaJhDDp_8MuyfIzUluFjvgdxEoZvijOiGxylsk98KurC8NO97ppMgaG644nt4SB8EWm1dWt_xbBUzPrdORAsLbQOtr5Yb2mNL_cVXBfdk9srG1q8CTrvU3_stbkpLTzWIGgLzhND7tTbygjutiVfeyIFdpv_mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=r9SmhXYkCMDf9VDd75H0OnsPrsGx3Y6CNDn1OiTfDrbiZ3Tf1RgaAazxKYXk4O5UlxVgLhPwTybjoA_sl_fn8WDHiiZJrr0nHR_8pbO_vB8EK_goWi8RBMf0o8h5ihfBO-j6og1BE-cc7VKzmH5kaZx_B3QdU_PHCSmhSeYN2MHtxrWM6YOp1-WS6F2yYX8CKmLWj3v9Fr9DWYrnuBaS6oeksbIe-5EXIZpkvYZk7NN2_12yczSA0hwm5RAmLhOfZjAFU1J8YTwUautG19OXZTAHxaGcsshV7VyENYuTuDWiFl6VqF1VXTOZz3tuHjQY-facDWfGk2L2-iToy0NUNUdSiNK1eKkciQzkPpN3ABp7C-Rzhk8cT2anTUfJpF8K9nTmwLAGwYq2J3pr-RU8QDY9uRYXxexrRjkOn-DDHTtxUmucoE6XBnEuMbfFiN6zmiUis2ONgRdc3hTS8K_Eo3qk7YzXjhxz5omMPZE_5i0Ie-HmW4b_QfaARQ6cldiF7fwSdmwG0T0lgMaJhDDp_8MuyfIzUluFjvgdxEoZvijOiGxylsk98KurC8NO97ppMgaG644nt4SB8EWm1dWt_xbBUzPrdORAsLbQOtr5Yb2mNL_cVXBfdk9srG1q8CTrvU3_stbkpLTzWIGgLzhND7tTbygjutiVfeyIFdpv_mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgHoFIbFmezWbg2COHzSYM9LK-flORYXyUmLgIi8aqHp0C3BnnInM7xKvtJ1hsamzhkaxPylgIAPGGDyRe1wIGpu6Xc6446I9frHoKzII8Y609iZgrqZz9qkJG6B6aij_kZif-tJ40LrACwm47vBG8nTPV216zaNj29qBTC8mZ_JOVNwQZ2btoJrE1PtB2KIDUcbKzP0r3q3Ca4NRwLegexUhsUISp7fBY7e71h_gE7pTk3u77LclxC5_Nui4JT92kXu1kvawd3T64lKQf8xkg6JgAvsdA8n1ZRMT2-XYfBpVRQhBx-6NDapGLj7tZEMlh25tPJKVvjsQZPjP7SyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrzlSv0Ihjp8_M74zWpqpxcgHVFALMC4tjJ_UYK5q48uPbL0m1smgIn5EV-mUfCla0cYUgTjaiAE-hMgsF3LixCX9GYgHqjSwZKW_2JGOvCLa9hK1mJaccJ9T-fiDREevhaDFUGpw2pG6NIE8tFjyqWXG2qYLzFTfNEJYc8uGwyotPiwv_HOT8pDJrK5W88sOpP-IKhAwc4IgLdZJ0_vhUZqGiCRfptDqNu7jatTU4s09Fldl-4aYDakdrbjoFJ6NO6hT3bi1PqoVQpmqW-_PRMN9JXNPFVG2PES9_y0Aq4tnSrrbcEjzc_E8mO5dhCVEbVeO_rsrjbavA96d0DOiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OueWmkwnckvyIavWQFWqF0Lv2yJm9OjUTI9TBOjO9NqGgq5J8AYuNpyt34XgRHkZb0bFh-g43Yx1ajrDEu5n_Z3hznoMwzIX3i_5VoEIYKXJmM14kq1q9Kx5r6VRObVCBTKpSrCJlyVhP-v-eQkBazzpbEVggr-YDV0pWR51EMTwIfKaxt9BIapvrwAKlL82UDcNUdTGqsitLarX_IKczKMQclFxLQ1DG-6gJz9tXKhFR1oRJwQGGHYjL_g3L6euBcLaRttwKZu-2Mqb81VqjEwMW9meBQ6gp7w2Aqy-FYRB6wsfxwy4aB6TAMvs5BdnVRM4DCWeL7tpzsBnc0ALVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=r2pntmO7jjQkyezI5bRExU2s67VC-OIv5syNfWh_-qs6UcHgf3EquObs4Ytm4mW0PABKrUnoLftDwkQ7kynMK7pM33ERpnb08epd-DAzG5rso0aKR8321M87lT_eiaepxRLYPKiqpxKDXaI7PHTUp_KTH4Sn5ztfFEK24x95JVZwBvUdfIF3FYOayeP5rBuZY114sXkcFmwwpWkPvgJKMhWQpo9IP1wG8MXz8wdQgVf2GUWK8f2XJ65lkjEG9vHxmvvL_s48rIv7JHMnkm9P-6hK1NIaJz-Iw93-kEAHk3uoFtFbTxesIIvzuJiapPa57Tzna9FW6gmzQzcGDCqhDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=r2pntmO7jjQkyezI5bRExU2s67VC-OIv5syNfWh_-qs6UcHgf3EquObs4Ytm4mW0PABKrUnoLftDwkQ7kynMK7pM33ERpnb08epd-DAzG5rso0aKR8321M87lT_eiaepxRLYPKiqpxKDXaI7PHTUp_KTH4Sn5ztfFEK24x95JVZwBvUdfIF3FYOayeP5rBuZY114sXkcFmwwpWkPvgJKMhWQpo9IP1wG8MXz8wdQgVf2GUWK8f2XJ65lkjEG9vHxmvvL_s48rIv7JHMnkm9P-6hK1NIaJz-Iw93-kEAHk3uoFtFbTxesIIvzuJiapPa57Tzna9FW6gmzQzcGDCqhDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRrDpMJTLhJHAze4jc1zQ2GAVyXFm0njwSNkCpAa2ni_va-pjEYO2nWXp5-Cw54VFVwppw0yw6c21kx75u2Y2V8SqprggsJzb7tdUWnRAVOreuR3ACpk7R5qfeJLCf5P1mnqhJPWZ5Tg_RpAj-CXRlcFeAXUn5X3Fd-bPhlfBXJRsX83pLktzSVzqb7v849NZNth2Xxpyjge64TTBcKNcVVOCZJ4qW5XKx5R_Bx6MZ1mJNvLnol8Lkx9UsaZCkylygB-AYXV_BFbWj6g7QzHWZKi-bHhxDCD45quVVpNLsSSci0TZApLF_ij47xrg5rjoPcHCNq77G9gJemPdH5WFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqznTp-F1h0xLtZadx1Q20KDV7Hm31f4uCEgllLplpZt0b_JiinSrgVKz-_Zz3bbZG6tWhVNwQYsb_rkNN4mhVczwZC1bpmpFPa-j9eFu5Yq1u6JD-9RKyHtuNkk8cq5QrKblJjVjqCPiyDi3ovlqch0AqGbsOcj-ZMmPGzX7Ze1UYtQWlPsz8vXc1xNyHHJTV03oGbPT7ikbNg0wyWfc2wdovoRHNyMMHezGta5--1O7sYbQdQCewpsU3E3S_0a9Jf94Kq_AAtUbPNj7d6KWWIGQpY5j4HlZAO2CYayyzfefd-RWvRcih0lmyEjvpuY1McLcwr-B_scGfxT9rUthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q7_g7q5phYNC0gEXDawv6G_QMteUsj1RUMA6EtthTxneMoxwXUpO06u1TRH2NB3UWL0Ih5Jj_cGV7c3aeJtpZCkR2qkO8tO1cJLDM8L0CmbaS4k9BAzXciOA4K-u-w5P4uyFNgmcyPYaAs5-fEvQlvVLp0FjiKFA_2EasYkwFh2gkP9AUTQ9HUTb95uP-nrEO9nCMSp5ZhisS9-KYHbl19jJTUstR06pMZrth15pViVJUU6qMQHRQdQd4CGYZ03wyOk43CtRxmJEZX-gJhquxb-3fRSw75cOl-WFubq8tt_s6vPZ73zcUuhzgngwEXCz4bKlNNTZz6s2KtiBvfvStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=knDZCyP2EHv4gBGHwV67v5dsaVDNibrKrSITpkAjvMmho-4CoGT0cpQhLAtumV8WtOIjogiJpbAGOJGT5BNb6hcmqnHyhFezXVID2QiV6EgoPibHZZ6JrQC7CEjNUxJU1OhbprgCr1qzu8mxlMAgYL9xuu6nlAic47brhkuuwt1LCI5YKeBRbyo1M31KFmGvtSjpdDGvbc7ulJmGADYGQ4-7ov-W0STxKE-EHhEwMvgKXJzj9Bui3momTpzHAR3RuG3MHNjzeUDOAz13GbYcnYFvVa7biMQDZPw3wD4c9Zg-0ZfTzSIKU_7pejCt5iDhvvGXFfLMu0a504HL09xJfHpINNMwBNF_4QMYvX7thpHSOY62T4IJLsH_6tgQPT920AiL8TMMkhMDu3oTm2eGU6eBgU77lBwA8S2SNwJGw5uaNMdz2i0ReRQATjH-a0Q03d55kwKedoMKIag_S38lO0PNBAIOGHzoR0244y6Z1JYpbluFKGRe5WHYbHhO0FitfjjAIWuGFIA_akG7X9f8T_LA9jiEl6g7HChOAvp-qxHOo3y7hRxsi8qB6tOkbyIaSeCjT2KYybnNYZHkv9NUF4biLALKdwblMXGH_a8ra-2FYc2KbKbj4tcc4T28o0fSJXKyIT1zquaXWxDKvdulSHtLha-bOvFWNGHUd2kWswM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=knDZCyP2EHv4gBGHwV67v5dsaVDNibrKrSITpkAjvMmho-4CoGT0cpQhLAtumV8WtOIjogiJpbAGOJGT5BNb6hcmqnHyhFezXVID2QiV6EgoPibHZZ6JrQC7CEjNUxJU1OhbprgCr1qzu8mxlMAgYL9xuu6nlAic47brhkuuwt1LCI5YKeBRbyo1M31KFmGvtSjpdDGvbc7ulJmGADYGQ4-7ov-W0STxKE-EHhEwMvgKXJzj9Bui3momTpzHAR3RuG3MHNjzeUDOAz13GbYcnYFvVa7biMQDZPw3wD4c9Zg-0ZfTzSIKU_7pejCt5iDhvvGXFfLMu0a504HL09xJfHpINNMwBNF_4QMYvX7thpHSOY62T4IJLsH_6tgQPT920AiL8TMMkhMDu3oTm2eGU6eBgU77lBwA8S2SNwJGw5uaNMdz2i0ReRQATjH-a0Q03d55kwKedoMKIag_S38lO0PNBAIOGHzoR0244y6Z1JYpbluFKGRe5WHYbHhO0FitfjjAIWuGFIA_akG7X9f8T_LA9jiEl6g7HChOAvp-qxHOo3y7hRxsi8qB6tOkbyIaSeCjT2KYybnNYZHkv9NUF4biLALKdwblMXGH_a8ra-2FYc2KbKbj4tcc4T28o0fSJXKyIT1zquaXWxDKvdulSHtLha-bOvFWNGHUd2kWswM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBmWu8gdu6CmxxtzkycWLAB5PJenbCL1HfQ1F_T9pNBeqqBxcPTR3VcWnGWguGh5_PlZfZeNYEXPVZUMWgS_k67SRPvDaiL2E4e8EOSlmATkgi0BVhfPYcxOJdSzu9cgOzYNlJAo5JlkIKv2SUVjwodbn8l8z2wmMq_MUOgPzMAHRaQI6qBa7x4kpHxPZvhASvqjtrukj8M1WFEmFNT2IJJYsjEveuRdCcEXWtDz2h_rOuuKt5GFzP3j3XrJguBUUHBEQY4ebh1jl7nr9RD4sh6FFj31Ukv1JUOW7D8k3zpI7E1G0QHN6FEfT10Q3rjHQNMGQfgvlSh7frHVAiUwRe08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBmWu8gdu6CmxxtzkycWLAB5PJenbCL1HfQ1F_T9pNBeqqBxcPTR3VcWnGWguGh5_PlZfZeNYEXPVZUMWgS_k67SRPvDaiL2E4e8EOSlmATkgi0BVhfPYcxOJdSzu9cgOzYNlJAo5JlkIKv2SUVjwodbn8l8z2wmMq_MUOgPzMAHRaQI6qBa7x4kpHxPZvhASvqjtrukj8M1WFEmFNT2IJJYsjEveuRdCcEXWtDz2h_rOuuKt5GFzP3j3XrJguBUUHBEQY4ebh1jl7nr9RD4sh6FFj31Ukv1JUOW7D8k3zpI7E1G0QHN6FEfT10Q3rjHQNMGQfgvlSh7frHVAiUwRe08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MW4G4wjsplOqDlCE9jf04UWtUFe-qtsaQruJazrGSNbCnkGYaCs4B-g0f9KjcFdKC6vCD2hWx4Mpcip4VGy0JYE_S7tZ3jovTUtGnVte0XkcF1uLM_NkDgDdEXDPabP9fC9IEM2ec4z_S0MovURETYXnq6tx7z8HHHDoIuZZuCRlc7AELgZaHgYSolr_AE78f0jDv5n3UEeSaYfN3ng4KTexcKs6fKZf8pv_c1Jjb0kwPrZsoAoAac9eC5UyjSPM46pkpDCx4Nr86Q1MdgJTCAI3Q9gsFAo8D_ZifTQQD-Nxj1ae6d2lYJcZm97a3PecKBBAnjMmHxKA-y_yA7WKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA0tBGCxv4665pH--b28SMAbYsoYK58AciF7BUkfwAufInYoKfU95bqQTfBwoyCxbVARWOLKjrVDiWAvWcH6jCpRqxSvyJooekhnJMdeleuIyHmXbpbxV7ftLaiFBQX7VMNmzM2WGLWZx2aaSbg_5zQOEykgB-K1eDa8hbt5RGJoNnTu9vGdJBmKBaJA0GTiB0jYJS_8w62zpVRUsN7jllLJUj-TTz-h3cY7_N9xg4LcxnewMe4ovL-hZieA1vvh791eyKayWqPTTvwybXaUAy5QG_kMRJTrrf8eialLwCbya5VAPehbFXLXEN6_m7FBhO0pDrAeVHcSM51etVNo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hzyrfHaqtBqpSN2zxg_2JI2RZLqECgSH88INV5wPqRhBn7taXcWwRY74U0tlcWNfN6zTn2ty8TXqGlcPMZQiumNi_eZCGotNvnBMo965nASM2Tr21IP1vneRd9kmsFWEkb0ECNW_CojwsBEKrm5iw7QfxIpd13GlOm10um26r3jS2dpXdAKuUj7rH5N10aPksQEOCBgTFWj0jG5iIMXXHgbi8b99xVGVqX-KFJm_vQBtuQ5TZm7aSQQJKgPeciXWRnZ-jaBE0D1OdJaATSbmyXIkK1zfkvYZ--M5WjLzf3y2A60OxDyNdZTbQgqIYF4UX-doXYbsdLrlwJcrXnviBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
