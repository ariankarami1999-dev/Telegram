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
<img src="https://cdn4.telesco.pe/file/kL8cEvtDEooGu5XRaCq5KlRFzJ8VHc7IGvEw6WxeN0PB3HCqlH821yKUaJxJ5bxZF5d8_claEr-CM9TqTBNTN54kmQqzDlEJ_M8YmwzuHNokJ61ZZyzVk_XJ2K4DstOaVEsQxdkcboEWb5-W7qI8yMy94VLObYLpPesTy_yIOBoHhPgdc9wZDIzJREQff5AO2Zs7HSSzLehjNoXxPEduxx89TvvG8RgvX4Wy4Elo7VgfPWu9wL9e8GaakemwC1T8kYIARkvAIIyvsVYpahPu6EVN1Rk7LbdzhYvYvs0ged-45fxSDszwfPX520NLox3ny3QZXRtp7XOxtmuoGM88AA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.2K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 04:51:32</div>
<hr>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUjdnfdNlpYOxK8p_Ewhw6NK-n2scN68XAfqLXriJyzKVMbNB4Y7q3MbVqQo9xcSwqYQLU9Y_in3G7PKjyyCeRwDwwZEfiHhwwmIlmW_kP-U_CgYcEmpoe_CSiX4jcObGtSvj_V49XQDVW2o0YmuVBJJQTywAPqLLtbS-Jgp8gV8gWlpuJsbBPy1zJYvvgAzW32RLL6MqN-Plylfvu9eXvWIV3OtcDN9kk3tFrAaLZo2oGp5dQ9Ud1EzpfpKx20-5nxx9SFP9FgapQgtB4w_hv9hpLRRoog24yDp-dVBq4W0gJ9EnuJWSygZtMwWwI3qREUYDo5YIUTRK2SLiMn_Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbcPdhHcGGmkwO-kaGq56pBTYnn8UgwocM9VKzrF-YTSIR5p7GF6Lm-MDbH9RDs2kk3BLRciZb8uFrJNynVIUyDqqLvpOs9x7D8oHV0LLK-IZYhp1p2L1VM131yNzN8JKAWZrEzewyiex7_x_4nEgFLw15PlCg4pF-QrkLvRsMD5178K3LaQJt8A-NUBG5Xc192tRYZJg8IckN68pPdmMKg0oUOG0xprZr_xvjHal206GiMElTV2Y5PjP3GJaVf-6aByPi4poQb5Us_6bVbJoIXbGj5aWVv3t6xtAhaTYjzqeC7yfo2Y8xRM8mifJOZ7cXSmq0Dvs4KKoCqA57tjbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9H4W8eJrVF1O1cQDOntYPoxjSZ1Zz1LU3k6RzbVRrzukUnspFZYEAkmjxKQTAZt0v_PJqrfojjtMvMOoIN0TgpxqJYJyCXTRUSzvSjHnB2lozDzC6PFCC74GV_r3kS10Atkopvd8ONdsYQHDBDRl_zxpDKyWH9QOMFJMgCT3CvL4_marY0sAWZBeJAt2yLeZgIsIl8KsVq6f_ArQZD05MJOmBm2P-uXJxYN9Otu251xhGhRHcHwHMxHND1n1qQsuvZilNR5EUYmZ3mklZEelwwcxMZtRE2ZKkj-i8gYzjAp0tjiRFQKdVqwIqnw7aLhks8o0APCarHx9leSbjcUvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-u7-R5MywmjvPqgCQ_ex_fge7imFaOFXlcZiufZxFuia55zKzGzXHFKuPerQq30bg2ULkBZjoHA0CopZIBDKl6N5PEBt3mD_QWDuyD1dN70B7Q4Ia4e-0-L1Q8Jpe4_aaLak_GLGtAiMMQ_jXXtREnz4Y1ocL99bUKaQ3pcbWfwSZlR_yJ0lTruYdPL3GDGjL2J5zR1XGuXW_tR2jPIPJa0zKXGy7EG_Eysq2xDn6qqjDZyql-FTSpPgcWkpspl9odJqDnGzQNeIWfBy_1-U1kAWU1qs4WWpOeT9FaLTK7fiCQ4JexOSSnXLliiebLKHQi7pZXlfiHVGCJX8CLfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfZq7f9l-ozQSq9VRowub8p2qaTEtvf6yXgGau-_fORJcACWNVov4B4dapnCIGguyZjt8uubLDLtzn9BXgzuBTZHd3x58ty6a74SHC5J5D_QJUSjqBsHXZS9EvaDjrJ78JW-PC8CDzkTLLByktwpqOMIP9qx0jFyYKF5j9eEsJVXLI43VR9oSiaz8W6BmKlh8fc3duclqZBiUI_oHS3sNDfi1Za01mCggIP1heK5jL5kxQPcKS2j09CYh2rlSNnX0uTb5N_1AxDzLmaD2fetcJqtdcAlw2TbXzkhkHgRcf4dbg32uPSfgar7S6zO9W8PtecW-3haYyzBxPtkrSFyGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEi-Q6Iaw7-Lc8x84dvP_rBzxcVGyRi1BDHPaapRUMw2soPgrpOSfhxBH4vAj_FW_INYwDMoI6bbSBk-fuGSIVldc_x4OIdFi3jujLUzQ72vhleYzQREF7vMClgU8HX1GP3S80C2cKCfNBu9PR8PTB8Bfy8CI4uHuQ5veBOA0yZUhpjtAvchuyewNil5LdpXFCu5GeFWy-nJUvmcwzyr1xzvBAI-8tmhRLC3AfqJlAo-r5QC7WSIYnYo7Dou4J3oUCv3DVf80HKo7WDPPGxsurTIGNba4Vc1dNG5d_TmvIzKvS3ze9KCFBsurE9UNT10YIp_LYm-NPzfI_EkTr0WEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js1YeLzyJ7LGq2odotu7VWCZUUgcOukUwHB8eUN0VmuoLa8P6ckei5b6S60fCrXSLM5aLKJfkeRM2CJQXJf4oGFxSpc67Z0Dizh7z1TjnC2XYgpo2Tn7fEIcdJrfaRo3VDN_xWEnCztZeiqBQBpMe6_2-O6FZIpHDCZXeD3XtUW3CKCp06WRf0KaW-Rzaj6WfWYZK_H-YyDMBOq99fdeD76eApjoeAsb9-O08HZ9-BNP2wFvPyzeCDmJBxO2bUK1h90WBWoJle_lz-WSL1D64LhGYCOEw0mfrGHlChcjLCgXpEsdRWq7CukfmZrXYiKvJil-kUXwk4d54jJx9fTX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=p8-hZcAs3a6y9wT-iS8LWmBXsIxXNEpagfAzts_xI7CSosWiIVD154iHx7zSbDDhYKZgGR5mIeZLaJ7DbpJDMD0L86TtbrVDpLBnDPHte14uZqU3FFvq_WFwTL-QFY1BQYh1iM4h7FGhy3WRrrheVR3sHBFEYtxrzgsyVnx9oahpz3JKzQ01NeZcA7C2vP_AIGQVfGqlviL7AOvsIeCah45RPt4lNwyd2OA63f-LJWVre5whoyAcroTMFtoRkrpQCJ4SqQE7N2Erct34goocsMtSL11GJuyGiF4BNsMNVcvEN6hzE_SDKm0CgcjsZZ08WaOgtIvFdgrSgTfjSmgdbUN3OahW4vdLde_pq9QokiMrzosNF9gjCplVvLnupKboCvh1b26_5J-Wn-msGlpCpp1cv1LRaJou1o9DhCvP21nNXiaUwjOsl_oyHgWMuUAt5n5eaE78jr4B9ev-so9sT8afUOKzm0k56eaMYLaHKuqjjOMTQ74uTj2qGuylUCh_q2jFukfvMoe8aSBTIbWNEfuLiwPfqpmVXiAKaU3EcpI3cQqlnGRExE_oQTzqKojPNHaAV5YngatTiZia-8FuQIgjR7xIuo6HCYc2rDHB-Hee1QBO830ZwfTDo5k5pqkdJT1va_a98QzUg8z7yZim4L7ywe5BejHQF45_7vrb6-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=p8-hZcAs3a6y9wT-iS8LWmBXsIxXNEpagfAzts_xI7CSosWiIVD154iHx7zSbDDhYKZgGR5mIeZLaJ7DbpJDMD0L86TtbrVDpLBnDPHte14uZqU3FFvq_WFwTL-QFY1BQYh1iM4h7FGhy3WRrrheVR3sHBFEYtxrzgsyVnx9oahpz3JKzQ01NeZcA7C2vP_AIGQVfGqlviL7AOvsIeCah45RPt4lNwyd2OA63f-LJWVre5whoyAcroTMFtoRkrpQCJ4SqQE7N2Erct34goocsMtSL11GJuyGiF4BNsMNVcvEN6hzE_SDKm0CgcjsZZ08WaOgtIvFdgrSgTfjSmgdbUN3OahW4vdLde_pq9QokiMrzosNF9gjCplVvLnupKboCvh1b26_5J-Wn-msGlpCpp1cv1LRaJou1o9DhCvP21nNXiaUwjOsl_oyHgWMuUAt5n5eaE78jr4B9ev-so9sT8afUOKzm0k56eaMYLaHKuqjjOMTQ74uTj2qGuylUCh_q2jFukfvMoe8aSBTIbWNEfuLiwPfqpmVXiAKaU3EcpI3cQqlnGRExE_oQTzqKojPNHaAV5YngatTiZia-8FuQIgjR7xIuo6HCYc2rDHB-Hee1QBO830ZwfTDo5k5pqkdJT1va_a98QzUg8z7yZim4L7ywe5BejHQF45_7vrb6-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvIZludxPww3UPSSIhSW0EW09AOvPC08IZXm4VsUApIZLGHgSwVGI7iXdoWlgh0guMLr1X6mXPqxvERg69OyG64H9ujtmvLK4mnST0DTKIhJwUe_92TX2kI4BV3dUzZcJ0etecXZfLjap8ZUaKbkEo-mJIGpJUJXhn1a3nD_YQ1lE2CZtpqYwVNycFbCQnZ_tr9Zn3jHtTb9C5By-_U1SUAkT43CJmcKaxZoTcpCrqzqsmYWuqlR3y-JTX5P30huwpWkYGbfvNJC1OcYhMXckdqo6e5Jqp3CgtqGIFZkyqFr7rBQAM9vsiS7-LCyKlG2XsLGThhBMG9GOJRl3RwaDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=eK-ZHnh8elTR107CVdfpI6SGuH72PHpAiO9HdOOKOTwlsXg3dBj5_LroCELD_0X3e4NpfVzHkByWNaM3fybX3TVIJ0rHQ8fJ4VOGSNy1Jf1kBk8UaXfe7NDJhGHKqV6gWty7GketmN1_ej8YAzZd3hPCWsAzufC3Nqprbwe1JYEzuIQAoTfeEl4lFIDk2j4vIHqjyGsQM2mPOsJUkENdpokRjLUSF3bFgOeqYLGmlaRyO_dvXhCVEfP_aKzS5P3cFhaRCZgL5Oh5fuZDRLjbLzhUKhlQ3Ub2UloLE0o45hRrTIvO4UBaNpNOHHgc0nVS07KdpWqcR8aRLsaEvAqE2U090KvhgpTgfgf--iTA-E5nFoLKfsNgg2fyd9X4lqVa_klY9tttpi_uyIzPr93VKp5kKZKrgFeRWrxf6awlTxFVHjqKk3Zyu2iDmugp4TMsBwzgoo41BmEvK8V8r0sik31oTDaLtwbQofSAxPxaFzv7HFRVodrQ6ukfVfko_GiA0Hyv9ZsTMGRW8S6d_pgWVCB--k8mUffbZ8yGxlCfEJHwyeYaI2WuGeLc5scSmBuCjb8VNQqBLrhCid9KlY6HAY598H7qrtvKZaPAmsuN0D_SUb1-xpeWDyOTuEAfcJBID-2ymLEzpWN8ZS0IMj6pxJqgxavFy_mPGVWeyNb_jOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=eK-ZHnh8elTR107CVdfpI6SGuH72PHpAiO9HdOOKOTwlsXg3dBj5_LroCELD_0X3e4NpfVzHkByWNaM3fybX3TVIJ0rHQ8fJ4VOGSNy1Jf1kBk8UaXfe7NDJhGHKqV6gWty7GketmN1_ej8YAzZd3hPCWsAzufC3Nqprbwe1JYEzuIQAoTfeEl4lFIDk2j4vIHqjyGsQM2mPOsJUkENdpokRjLUSF3bFgOeqYLGmlaRyO_dvXhCVEfP_aKzS5P3cFhaRCZgL5Oh5fuZDRLjbLzhUKhlQ3Ub2UloLE0o45hRrTIvO4UBaNpNOHHgc0nVS07KdpWqcR8aRLsaEvAqE2U090KvhgpTgfgf--iTA-E5nFoLKfsNgg2fyd9X4lqVa_klY9tttpi_uyIzPr93VKp5kKZKrgFeRWrxf6awlTxFVHjqKk3Zyu2iDmugp4TMsBwzgoo41BmEvK8V8r0sik31oTDaLtwbQofSAxPxaFzv7HFRVodrQ6ukfVfko_GiA0Hyv9ZsTMGRW8S6d_pgWVCB--k8mUffbZ8yGxlCfEJHwyeYaI2WuGeLc5scSmBuCjb8VNQqBLrhCid9KlY6HAY598H7qrtvKZaPAmsuN0D_SUb1-xpeWDyOTuEAfcJBID-2ymLEzpWN8ZS0IMj6pxJqgxavFy_mPGVWeyNb_jOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa8XGDzmGc9oJv_itnzKEAhMN7OKaHGsUx1dSq2ol5VU6Ncbc8FjrczTE5Re_xYS8oPyrCh9uxIMbWpiQ99P19X41ZA97FbYSgpMXXN7UVTlvUav6_lKirhCEiTl_FF1Qnvv_gewBO6vE_kD6qvFeytsHVgIhDWFkAYNK8ASU9cbaEsZAV5FyYTe7SXJQgTmkjgisUeM-m6yrP5VIjqp-PooqigIrJyucnB4fu62Ci7kIaOoE3Gy9ggVlC4_vl291g-nUQh5osXd11qdNk1KfmKadZQ2NqGgXmp_aPNH1PvutbPl8XJiFPrNmAHVmaiXzCWKWtVENd_oYjpRRsGbdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBi3PHfnlrR6sfXy00aSdjHIF4bJques9dxolFB1n9O_BEp4TED3pI4VchvKSd-TX5UaUh7W0O8bLkJTbt0f652v9QOIRuNqTpIAcpwmHdlQAqrOxRfG2CZDDvczKTXeJsmNchtlxF6tAVBGCaYljYRCaBFpFmS6Px8clOr5g1kQsgXDNgE74ZTygGkuR032eBm5HAsNDLIsbKzivRPGbWUEdF00H795QBn886JQUPW_guqHVJcPX1BEmge3KJP-L3hg7NABtQ0KbwZQN7XQHlKwhoW4yMhcRLQ_VKH2bceEJHRElxLFT8VejS4kAH2xLufJ8cGc9Wx7K6xY1ajSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7WwX6gk3c_k_w9zy7bAZ1r00n-g5pbVLndnADA4TUDvfpVZ0oon9VIb1eF3HkhfzSyCXOq6memeFmf0DTgcyT5iQCYLmOABLXXUkD_BCbIhfeZp9LYYDA4A1CLkeBq6EU3jgc74-oOx9sdh0IVaW1Z2XCr6YQ4RRcvREGbLsd54Tg6XUtuzEGhG2Ch-6dK8rFzESV6Nsij9dshuXChyeQv7IK_jiVr0t1OIoTcUJHPlas_cNtgECSDDq8QwK5Y3aljscWUou98Vb27w5UgZgbX2bc2gyNMBUAzUyn9BLrCxkZl8_BS09a7s-iyRkMun1f7KZbBjHGOGGnrUDFHNdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=tHJC-rmyDUK7CVseJzhj574nuEYyV8h29cc2kvKGIgNkB0YKpFrwuABSk_3DhnquaRfzfa-vmKzhWjj4U2wTDfcQrbuUVb1N7NdzsgNzgwQL7RERSRUnR8K0ib2uxoEdGF0bzm52JRW7Y6y-qpB5dbKc3oncQGgiIyHWT6XoOQ-VpB110F04O4Nff-XK0Gtn0MZ12RD9znM_vudwLz-bIqb7JI-gp2k6g4-BjyXk_YcQQnm-zdVaFVIE1qYXcwbj_Yb5CkGuAUfqdClxNtsoASpL-fcl_5c82tDJ9L5Al3mGdG9nNOiT_6elMI6eb1rn03YRze0zheXxmYH92uLOkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=tHJC-rmyDUK7CVseJzhj574nuEYyV8h29cc2kvKGIgNkB0YKpFrwuABSk_3DhnquaRfzfa-vmKzhWjj4U2wTDfcQrbuUVb1N7NdzsgNzgwQL7RERSRUnR8K0ib2uxoEdGF0bzm52JRW7Y6y-qpB5dbKc3oncQGgiIyHWT6XoOQ-VpB110F04O4Nff-XK0Gtn0MZ12RD9znM_vudwLz-bIqb7JI-gp2k6g4-BjyXk_YcQQnm-zdVaFVIE1qYXcwbj_Yb5CkGuAUfqdClxNtsoASpL-fcl_5c82tDJ9L5Al3mGdG9nNOiT_6elMI6eb1rn03YRze0zheXxmYH92uLOkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggjjcjfpGv8iuF6BXKXSoS9iHp4hUTUMGl5wv0xpY743WeVVIoSwKrI5GfB1eB4QbnRs4mMRVoPPhSl2vI_G_PrclkVDTSVAE4Kj3qgVCBM8uXmUpaZ7R10hZyTWpW-TS12hidRpksEoBkuJjPsVfMClgKlmSEfebJFv4cMWx_3Yq0v18SQtb71-vTgGH1rgfvQFC1E2DoQCR27koBEoAcoIe-m7ejsW7WZv1_uYZoatPGUmLLNoswZpx6EggHH2VuYrnsc8juAebJQZcf9IFCZtwb73MkUXLYVg1-dD-phcktjLbMhtmwl6pD-7Bi0Zby3fBEpU1kZ6q1NnZGs18g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OueWmkwnckvyIavWQFWqF0Lv2yJm9OjUTI9TBOjO9NqGgq5J8AYuNpyt34XgRHkZb0bFh-g43Yx1ajrDEu5n_Z3hznoMwzIX3i_5VoEIYKXJmM14kq1q9Kx5r6VRObVCBTKpSrCJlyVhP-v-eQkBazzpbEVggr-YDV0pWR51EMTwIfKaxt9BIapvrwAKlL82UDcNUdTGqsitLarX_IKczKMQclFxLQ1DG-6gJz9tXKhFR1oRJwQGGHYjL_g3L6euBcLaRttwKZu-2Mqb81VqjEwMW9meBQ6gp7w2Aqy-FYRB6wsfxwy4aB6TAMvs5BdnVRM4DCWeL7tpzsBnc0ALVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3QoRFflYRFItvECdQHH8mqNiEsEwRsBa1mgGfQnRSjg1a28zTT4qrsHzRt-EyqM3QHrgEZzqZPhLOmisF-MaHscuhcIUZK0XCfHfMEgH2wQGHv-xSFZidctE6hdoiopAGMTF5o5iS25hRSSJIOmdxHm5MSzdfSNtQ37B8mjoWgl-GtMRCvKAWWQnTnbT88EC3TE0xF0pyME7Xux82tc4CO99_eM52vTcO3qUWNKOoLtECsasb_epDGpMQRagVWppwNBmIvZ2007G79-fHmIH4SG5f3iRIi_l8AS8_HolzUA4DkHuuIQzgZaM9KTabBvi5BqvZ3YMGW73LrKnvJ3lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=SkrkO4PW4kl0QRS0wFBw9Zumlp6JOWfEvhSdMFAoHoqIFBGwgY7w7oNbYRPq4bG_SM1plSuNYWJb4Oku0C-iZJ8C0yO-Oc7E6NdWUKzKiVmJQ3mQqagMk6yD0b6lgbGkju4YR1yc_fR46N5BMIUo1xkqX2fgvmaFznS6wo-frdGn4iVZQRCSqXcQz4WGpbux0jeDvdEEe4k5wmBSH-Le4ZfLbm8oOtddc9kC0V9ES3zkZIr3CGJXzGnVCVsSQ20Bjsyxhp0XMwWvj9BI97K8J6feylrYSDTNOOivcdzhGyW-xCszqZKvqqnE2Zcps5KhkV2ESjWvPz-_waZdNcsATQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=SkrkO4PW4kl0QRS0wFBw9Zumlp6JOWfEvhSdMFAoHoqIFBGwgY7w7oNbYRPq4bG_SM1plSuNYWJb4Oku0C-iZJ8C0yO-Oc7E6NdWUKzKiVmJQ3mQqagMk6yD0b6lgbGkju4YR1yc_fR46N5BMIUo1xkqX2fgvmaFznS6wo-frdGn4iVZQRCSqXcQz4WGpbux0jeDvdEEe4k5wmBSH-Le4ZfLbm8oOtddc9kC0V9ES3zkZIr3CGJXzGnVCVsSQ20Bjsyxhp0XMwWvj9BI97K8J6feylrYSDTNOOivcdzhGyW-xCszqZKvqqnE2Zcps5KhkV2ESjWvPz-_waZdNcsATQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Ykd1n502Q2bQC-BhuPXHXHVq1xiujPEKIU5ygIGolrKGNGT7iBTtwuFlUwIN6Xs8Lq_uSDHq6koaiDK2OzLd-hqIUlhE5Mj_zPSEbI2q0xeviGGz5_1Ld6FP8cPtnn8PqIvXdu1cNZRq8kitwP4ESFEwuVzq-EPEVHROjce5VfsrfSpVx2WFLAfFZDF9RYVzS4YX8Phog6hyEw7wPcWd6oHio23WGD3Q2ju9iu5Jhk0fRR4sPCE0BfG0pKe63uO2NjW_mZoSiC2kR0OB3dobgD-49xLye5IPjUwcGDVqQ_wxvNRycLjmsERfcUmPcmZQhagSPkyezjtb5Un5dJRIvVasrp2NQ2oQU17BDnR3f7uIoOFDAW50mftPT34NDJkVLH9LjaN6FWjbjVNJREwdBAdbIb6dh5AhuuteRTKOa59lfIUVmSnbJdNHaDZDSxHjILMSWhsQ34sEb71wlOB1i1puzwtQmKibWKv8yY24WISfaCq-Q3F-NTBMYWrfORuaPWn3QnrOTGv21LffdVeGBNnruciKOX4--kkjyA5MFl1AJQXXLpZEFzCE2m6PgHsROHSdLbJkCm7q595cUdzseFJMx3fTRXHzz0vf_yUjgLPZYH3lxJ67Zxfsv2ncdtOLcdAthbZyxDABgZjmQFO3TIcFZAYSqo5refHWlArilRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Ykd1n502Q2bQC-BhuPXHXHVq1xiujPEKIU5ygIGolrKGNGT7iBTtwuFlUwIN6Xs8Lq_uSDHq6koaiDK2OzLd-hqIUlhE5Mj_zPSEbI2q0xeviGGz5_1Ld6FP8cPtnn8PqIvXdu1cNZRq8kitwP4ESFEwuVzq-EPEVHROjce5VfsrfSpVx2WFLAfFZDF9RYVzS4YX8Phog6hyEw7wPcWd6oHio23WGD3Q2ju9iu5Jhk0fRR4sPCE0BfG0pKe63uO2NjW_mZoSiC2kR0OB3dobgD-49xLye5IPjUwcGDVqQ_wxvNRycLjmsERfcUmPcmZQhagSPkyezjtb5Un5dJRIvVasrp2NQ2oQU17BDnR3f7uIoOFDAW50mftPT34NDJkVLH9LjaN6FWjbjVNJREwdBAdbIb6dh5AhuuteRTKOa59lfIUVmSnbJdNHaDZDSxHjILMSWhsQ34sEb71wlOB1i1puzwtQmKibWKv8yY24WISfaCq-Q3F-NTBMYWrfORuaPWn3QnrOTGv21LffdVeGBNnruciKOX4--kkjyA5MFl1AJQXXLpZEFzCE2m6PgHsROHSdLbJkCm7q595cUdzseFJMx3fTRXHzz0vf_yUjgLPZYH3lxJ67Zxfsv2ncdtOLcdAthbZyxDABgZjmQFO3TIcFZAYSqo5refHWlArilRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuADmC7kuEYAcw2ZXPaggEfw6konm7NWvBrhG6xsKbK4o9KNKm9CzZLYqbkU0Lw1imqbSROnJ8BvUdq8R1rbh87Pd0N6-2XYhYX1aT8XZdT0l_svExjVz8NK--Fhwt8O5Bw2hOqq7KoawBm854ZIdGs5N0p86Uk62WPr07zz0_ByAzWuQOp435SiRcHgLJ_Rn4qj2unSup6uivIHmRH5VxrEeXPrLuO7FIks12Red92mTbtoOmt2veFYHT25Gj81vxyPgIqTCzPzIzgxkP5KljTStd23BCIuav0utRYlInXsLTEPCMrZSE3CQ4c6GHWdENPVTcYr2-xrlnkJ7G0O-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH60IhTxbMTV9D0A3uPeIvYFf3a7iDVX54mNZyD8u_Mlw6OOnwrJ_Eft6qBaknVXbAnn5nRK_5T8MP_APlvxZUjwz5UvnVhdqNht0GSt8eQZk7gRfVGVHCF9y8jwKh69RxsqlYsDRfnJ2-8_8SMAWCwHuWpmSCcYF5wTeZvF86jOTorn242Npdc2q8q83LQvNrEYVZEhNILnCtgaBMn_JMGNKLQYZbg5-Tg5RtbvDg4JVkmWyN4NlZsQpJGM2VRNblRL7JRjTd-0QGNTmRYjtjSqVXDxoDnhsVljnOFS4NkMujyGwWNVyjUZobEGzpmJRtqxeKOVFuu-_rsGx7oU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RB39RsarvFo_BPWhVCd_0xcHhFrz88n47ZBR8Xn_bGncz3I2pDOukwEIzx_5gdAx83bfENaOGwfY6oeqV9R7Pr4qKXxR21aFAhQO-3f8I56tkz8sPkIZojkywRQMjBslEYAo4C5xJdbXvEWEHycrTU9lJ3GvKz3bZW4K3TH4PXhrEMQQ7VAD1g6x8TVKtA1ALae6iylq35bDfxgVlFhnEragCrP4pPbQOj8wOLXyRfBxhpadb5biLjyMi6ucz6N3AITaoG67C0mIHhOGMkfzu7p1Dfa3s3MCTjt5MNRDpgBks1q6V51lmJnehTCnyKjG0pV7vkBvFp5qAjlSizq6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=fVsOFx016_E7xXTz-fdW3aTvjygfF2cNyqs-guGrb05PiksiBRDrF55Z1ZsWi4dyZ_xK7OpvuYXl271VK-YGlk2pBrNAPF95zPWrFaLlwWNDb0kFH7nC_EPds6mGZfmBX9lAUmlMxTfWpTIVLr6IeKbDdm2LszWa9MGbqP-neTygd1V18Au6wE3iHZ1jx05GX6e3Agf4C5sr9ACv4wCOyERHEIsF43VVgNodvs1yZ6fWh5jl7gx8mpDpYZISj3iFm04IjnwvFOIsa3JiFZSgdj-YcALhQkN8H9xdV2uLrXMbwFxdLRgysOT0x9tfu944UhZ4JiaGcZ_vgOQmg610rEJlnxjT0muZJMsn_ovFiUdO0QYTyMMNWaCUnYDQ2AIWlGb8VP7MpcZ5311tQQicgqFUlA3dQD8TNprTl6PXXCfjInIFRqNS7qkEn07KheHnhjzij2YFoZdHNQ8tDAcsZnDtwaM4Lc2rNhzlqP_rXzaXPa6jcIdgd-2YWEPmvAToTE_EbbtdifLMYYSvLmnhz-Isr8E91Vw5T6xxxhhRY14FbPs5HWVSovhCiCHmOGj6_BAYJ259REAgRdXAdc7YYstixYfRTCMWW54oX72GccVIXkv4Oz-pHQlQOJWghUfsdqW2-x8G2V-Cz-WhSNX82mCS7Ojt37SdsNuAGInST4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=fVsOFx016_E7xXTz-fdW3aTvjygfF2cNyqs-guGrb05PiksiBRDrF55Z1ZsWi4dyZ_xK7OpvuYXl271VK-YGlk2pBrNAPF95zPWrFaLlwWNDb0kFH7nC_EPds6mGZfmBX9lAUmlMxTfWpTIVLr6IeKbDdm2LszWa9MGbqP-neTygd1V18Au6wE3iHZ1jx05GX6e3Agf4C5sr9ACv4wCOyERHEIsF43VVgNodvs1yZ6fWh5jl7gx8mpDpYZISj3iFm04IjnwvFOIsa3JiFZSgdj-YcALhQkN8H9xdV2uLrXMbwFxdLRgysOT0x9tfu944UhZ4JiaGcZ_vgOQmg610rEJlnxjT0muZJMsn_ovFiUdO0QYTyMMNWaCUnYDQ2AIWlGb8VP7MpcZ5311tQQicgqFUlA3dQD8TNprTl6PXXCfjInIFRqNS7qkEn07KheHnhjzij2YFoZdHNQ8tDAcsZnDtwaM4Lc2rNhzlqP_rXzaXPa6jcIdgd-2YWEPmvAToTE_EbbtdifLMYYSvLmnhz-Isr8E91Vw5T6xxxhhRY14FbPs5HWVSovhCiCHmOGj6_BAYJ259REAgRdXAdc7YYstixYfRTCMWW54oX72GccVIXkv4Oz-pHQlQOJWghUfsdqW2-x8G2V-Cz-WhSNX82mCS7Ojt37SdsNuAGInST4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgWLwjVWV30_GjUWIo2l0m1jWOJo73zqndCqkonb6elbsO4RTUFWfe9UtXAAlnYn4MppB5fK5M7UzpDhioVbEGUlOibh0RM_uBlYpdn9th3C7o5SfzQy5xTwIyrsCWX675dKNFNuxrcC8cL7oudSIKbkatN4JyQ_wFade2_On9KE-9Sqg6eIjp_x1oCtZZXRlaug9ceELr0qP7qEdH4kvMv-Mld5vrC5OS-QR2-ffpQN-VOZaOVm402Zq8_NEJDqhcEXf4lrtSarqlj_iHfo6HlK-O5yfIu4hk-GB9B2hmdGeG9Acr0894D5qEaLzDfz0q8OwaDFDL71Mnyf3uRW0ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgWLwjVWV30_GjUWIo2l0m1jWOJo73zqndCqkonb6elbsO4RTUFWfe9UtXAAlnYn4MppB5fK5M7UzpDhioVbEGUlOibh0RM_uBlYpdn9th3C7o5SfzQy5xTwIyrsCWX675dKNFNuxrcC8cL7oudSIKbkatN4JyQ_wFade2_On9KE-9Sqg6eIjp_x1oCtZZXRlaug9ceELr0qP7qEdH4kvMv-Mld5vrC5OS-QR2-ffpQN-VOZaOVm402Zq8_NEJDqhcEXf4lrtSarqlj_iHfo6HlK-O5yfIu4hk-GB9B2hmdGeG9Acr0894D5qEaLzDfz0q8OwaDFDL71Mnyf3uRW0ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyD6lKwkvoS6CIr7lld-pVuqowF8jure7aKOEUcum1VYJUJ8gOyCaMjGT5wmeaVsNq8pgSck3hTf5kRlRd0wkBM2UxbbFFjbaBSAbWi2ePSIqDaRqrKgZVDe6AqL1FkwrDDxML-pARzjex28PBqUaFGbRqffunVksq_cwQHi6F5kFItsZifo7g4U9sBs4rRc5aB3GWl9UwyzasR9PrhKqS5V-xAmrUEZknTqIzHRyihzw1N0bxS4ltlhpkSDk2RhoHLFHcG9hhUeXpzewyK-D0iXHqzfuFUYyewfN2kDfFBs1QwspxY88jSssirVFaj_UmV8VBkfoziAmDlSA-nhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0pXlCXpgMr3ixq0ISJaMTaRzHtpTonodBxLdCEI6TmdHglOfQ4w-3hmfcNR3KYttr9eJ_KWuM-jSQA5RHbxB4qry5_95-qA4UYgYIGQBYslxHlFlR_itNsLB5DPc9d-WBGpxeFwB08W-xv6COoghNM5_Nio-3tnt-zShOpMeKnTnMPUe7cCK1Uq5n3QmCO6TCbEe9BZvKmf3rCCyxIfleJb7uWVe9ebpZOfTILoNvUZT4nP9Mm0lBg9P0cS2RljYd3XNHk75zMI6KNE8YCmxl3wGqCQI6ruL7ZFP8XOrJ9QW6xHX_BOFzGCefqyHoozhQ6wiavkYTPybHMRbiqfDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=Ez6C6U0eU84AyU6_yhzXv2v40c3zkL0VZ-gvsuBBGEdRjvrscbkDyuZDvACioFQjh4sJYpOm7KOsl1uXmO_THQhutQDg1E_ZVh8J3xqAowO-4XVaiGx-2udcSxbkqPqv5SPl72i4vJKu78wWyZ4EzgKc1GD05nEGJeIFaWP847tNtvHo366albpGG5_UodUfWYSrpwmObDVlETBd3cnfEwd9KX_GkfGK2Fou9fNSgru7anIp1vrKW1hkPBAGJfrlCLwsTOYYmvYP4dtgCxtkuLruRaSGHryGYekudYtBJI80I-It3yDMp6YmHz3KCC-xBmBth9FG88xEC1C3XJg9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=Ez6C6U0eU84AyU6_yhzXv2v40c3zkL0VZ-gvsuBBGEdRjvrscbkDyuZDvACioFQjh4sJYpOm7KOsl1uXmO_THQhutQDg1E_ZVh8J3xqAowO-4XVaiGx-2udcSxbkqPqv5SPl72i4vJKu78wWyZ4EzgKc1GD05nEGJeIFaWP847tNtvHo366albpGG5_UodUfWYSrpwmObDVlETBd3cnfEwd9KX_GkfGK2Fou9fNSgru7anIp1vrKW1hkPBAGJfrlCLwsTOYYmvYP4dtgCxtkuLruRaSGHryGYekudYtBJI80I-It3yDMp6YmHz3KCC-xBmBth9FG88xEC1C3XJg9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3gQPPBS59cTAMarlb75IDsvDGrINIwASUEYzXf1AfdWz64PJMAoixlLRmUYHzJEnIJThmToalNSikbAMjbjg0zJkccICrGSJwoa_xo0p4iFtr8nDuubb6FqYkhbPB8nvIZgMmC90P1_i523qw39NsABGVjlgUeKjGDwKP18We8WU1jCwIFFxd347IauJGruVFscu4VPsmrjWrU50-0tWWcHQ_4WXqv3GioOJw0HNWDMJAMA5PiKRuBVQdqI-Zku_26Q3NZHwVnIQPFeZGma38ftXNaKZnda-dbRYii9igg2prGUXsbdLIO4Zx0B2xArsWmxUgoXfc4wcZfQBjuX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
