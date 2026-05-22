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
<p>@IranProxyV2 • 👥 39.1K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 21:15:36</div>
<hr>

<div class="tg-post" id="msg-8474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دارم یسری تنظیماتی رو سرور ایجاد میکنم، بعدش نتیجه رو خودتون خواهید دید صبور باشین، چنددقیقه نتیجشو بهتون اعلام میکنم
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/8474" target="_blank">📅 14:15 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsV6QTb0A1seaEHNKBJ-gkcwRzjGrSW1UIVhCXZpjicP8K50Ymsza39GEeT3pUK5WyapIx8bd3yJuMRUm76m0tlQ99MoiYf1s3nM_RjHQVFvmyad_DByD-77L_Z-dScXHpU6aysOz7aHkyFykxWEkALEG3nuQv7nRAo3KXSGVYE0MBHtswKEdI0keBf2p32a-nMbFWpGMSbEJ6iMJqfp7u_tHEjTA_vrr-u6e3wGQwgG2w8KJPKbn7NOVxbpJVVFGTxUKVTWwArAs9EYYCPtJt96uOvwQW_K-LrAxRMjAPkjyh-Qg_jkQe4ayc48cvhpzC8JAfCr_8cQN9E5R9NUow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-u7-R5MywmjvPqgCQ_ex_fge7imFaOFXlcZiufZxFuia55zKzGzXHFKuPerQq30bg2ULkBZjoHA0CopZIBDKl6N5PEBt3mD_QWDuyD1dN70B7Q4Ia4e-0-L1Q8Jpe4_aaLak_GLGtAiMMQ_jXXtREnz4Y1ocL99bUKaQ3pcbWfwSZlR_yJ0lTruYdPL3GDGjL2J5zR1XGuXW_tR2jPIPJa0zKXGy7EG_Eysq2xDn6qqjDZyql-FTSpPgcWkpspl9odJqDnGzQNeIWfBy_1-U1kAWU1qs4WWpOeT9FaLTK7fiCQ4JexOSSnXLliiebLKHQi7pZXlfiHVGCJX8CLfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4lyFs-jEkqnklE_JAQn9dPQjJNs2-X8iFopWZlDpTJEO9WUsae3SrwYYHEYJIlNZb5nNtn_SB3LD_CRZQiMz9ulGIbhcnF6XOqMTlakrjjQlCxj9t8yTbRWGC0v_sx1RAymQium0UfA2hUZ_HnBx-YKlykpgqeS2FCZLp2-ZlDd7LyPlR-3J38zU-7rN55m1LHs27S7oabDtQVa9SqQPIQKO1aY3OF2VW_IcAStNSbW6YmMqhAOlJFsXtfB-BeoLrhdQUm2RMU9zy7KHZA72RT1vWR54mZ-Q_n1ghd4d__bjOKQ9IclpssSJ9ZUDNp9SffDNC8gDcCFKQzhMPKSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVv9q3O8-npCeJk4wE_-Jlne0K4u77GaXzXjOcOdna88KMUOKIOz4DKsBtlo6j0pPIJqDCS6vIFarOAjLRG0Cdd0P3Zy4NvJ2Baca_V_E25nBN5KGNTQNJlffibUhv5Jin5KaUiYojeola9_v6bwMsT0lqeqGVEHH8qXlfosJIh7EoRE_S3Kr73-1zTJSxLMrPIuddyi8lNvsiq9bqFRAcrOYc-X4XNXXBjzb2kJa6i_RleZe3vnHjms3Fa_vdbZxQOLd29c3ll9iqHizb-TNfsMoMg5sQLejBuqsyqX-CPkaMYtd9jbGjBByavfZTEwE8lEQ5vGx5_ZF0XyD92r9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqeAWrYtZkuAEziFQZ3FVJvqXWCSB8vWwdfSbxje6CBwdRX0gEUZ4dwbuKMW7oLjyCJRJSqfPB40V2NjwGhFy0NI0DjMZS_u5Zg3wrB63Rt2ENhRC_IoFLeQHzoDhfteXTKC96Pkxo_W6cyYZhhW_QMJgqVVp8ChiuzIl80r7Kbwg4ddmXFRC9SAZsT3WJlAe40jdSrGg4AMdVQMgIxkVwJuogO_f3e0wD7WClzmzjaSphCP7JTrVkZRjaLfUvCggvUAGjMdRKA6fPkDOAFdVOCgASqdfuBc1lmu4w1CghgcxURd5odHpmgoDWVC6d0xDRSwqwwl8fIbvrhSvPIsHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=TvZjTKiaPdxNwzHOYKsosxAjKuS4nS55eLfpIZt8BWfeI5B0NpRVLO5lRFU02slgn5HG9SrbXocFZY3n7achsVXhOCOqECripQP9RZez5DG6ghtquewZiWcxqzLj0DypLSdVH8nZisvuo_gSQHqs2SQhvrb418qcqka3t0V27HV4VV65l8fYuayFYxw0-eBmhY6979-pG1BKfIE4Y9z_Rt3Ev-23-ZbnOsNDr9EMys-coPIdCItO9MOHgGmfGZAypWXqg7Y20jeDsW0P7yz-gvlI0fDQe_ZQiAPvfCvTu3oS1uK1hgfdUbuAp2V2q0rQ_U71mVVxUM9ILh2qdzmbJ4wPSQ6SbxznmqQi1BDl5s-R8uaJwT0M7rMcOaxY7YdHn2Nwx-aJuekh1AqXzBI2f1agM-vNf9_oHp6Y1alOxUsHax98Mx_7rtTvASeEAHkWybryrxjCfctGGK-DRLl0zY9Ss_5HItIlUl28CiqZdmXZC1g2xkniGE7C0-ZDQ2xJ7mmYWd7wa7JZhI7NkgqK1za4QBigmQ9Rq4F_9HhNsnQKjBLXsc-LywR2ZqkH9w3MUx72Qpl4c7KStHA2yilb_MPS1JHSlJ8UXiVFfyUzUaEQqS2JWjvbcKpq5oGVrHgViVM2nuMXStydlsrfYs1L4c8Nnrjex2V4FhovrPzDSJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=TvZjTKiaPdxNwzHOYKsosxAjKuS4nS55eLfpIZt8BWfeI5B0NpRVLO5lRFU02slgn5HG9SrbXocFZY3n7achsVXhOCOqECripQP9RZez5DG6ghtquewZiWcxqzLj0DypLSdVH8nZisvuo_gSQHqs2SQhvrb418qcqka3t0V27HV4VV65l8fYuayFYxw0-eBmhY6979-pG1BKfIE4Y9z_Rt3Ev-23-ZbnOsNDr9EMys-coPIdCItO9MOHgGmfGZAypWXqg7Y20jeDsW0P7yz-gvlI0fDQe_ZQiAPvfCvTu3oS1uK1hgfdUbuAp2V2q0rQ_U71mVVxUM9ILh2qdzmbJ4wPSQ6SbxznmqQi1BDl5s-R8uaJwT0M7rMcOaxY7YdHn2Nwx-aJuekh1AqXzBI2f1agM-vNf9_oHp6Y1alOxUsHax98Mx_7rtTvASeEAHkWybryrxjCfctGGK-DRLl0zY9Ss_5HItIlUl28CiqZdmXZC1g2xkniGE7C0-ZDQ2xJ7mmYWd7wa7JZhI7NkgqK1za4QBigmQ9Rq4F_9HhNsnQKjBLXsc-LywR2ZqkH9w3MUx72Qpl4c7KStHA2yilb_MPS1JHSlJ8UXiVFfyUzUaEQqS2JWjvbcKpq5oGVrHgViVM2nuMXStydlsrfYs1L4c8Nnrjex2V4FhovrPzDSJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=gR6w4ERhUhDxGljzLnn3XS6L9c0sP_Tf8CpcuHuJNRaF26IgXbdJi3rJbK1mXsdMuFpYwfKokvPYGZ6vXMoJOxsRPgw0t-FU0yWK2wPjiwnkVdnqoqvxUCkOLWdSB-RPorFmt4l8bhAUhlN974nrYeCROw8t04viVhj51pi7C8NxTzM_A7hEfDG6hEZJ-vPEPYylyh7XF8KuY1XjUoXfIkLQDU0RmPChjwuv0QwE2yhx37tc8S3a2AwIxYbf1x1Em5VYkteZA93-cV4NUZ1w9C_r2RmTIrqb-_Z0Q2pTNtUCeP4pZmiya5CeaN5QJkjL37T3UuCQMjy1IXLm1v4HqB9hLR_5Jkt3N-rgIl1MoPKd8ts5I20zDxj0HUQib2mvaxWGz_Pb4xNoiU1We8O_RQRE2iNbsI3WGnUfz1b84TZqdfgZY8cGTmsu8F2thYmQGbHYXfV5lq8rV5rTdyLf3KIQfeVEP0SjGFtMgHhfUg1t-09L27zFcoNO6z6XpecDwotA4Cs0CVcZgSI9K_mtqpJtNNKCJE27tl93DAlcKNRCEAoZgzXk8V12aCbo28YD9T-uTcxwdP2nNBHKyCn9mTCYpuX0rnQzJNx0Id9BygXdkOPHT9KHWPG11cuT98nZRUFRRCgtKvRpHhgnkLFfFteL1N1irbc4WUmOAIOkHu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=gR6w4ERhUhDxGljzLnn3XS6L9c0sP_Tf8CpcuHuJNRaF26IgXbdJi3rJbK1mXsdMuFpYwfKokvPYGZ6vXMoJOxsRPgw0t-FU0yWK2wPjiwnkVdnqoqvxUCkOLWdSB-RPorFmt4l8bhAUhlN974nrYeCROw8t04viVhj51pi7C8NxTzM_A7hEfDG6hEZJ-vPEPYylyh7XF8KuY1XjUoXfIkLQDU0RmPChjwuv0QwE2yhx37tc8S3a2AwIxYbf1x1Em5VYkteZA93-cV4NUZ1w9C_r2RmTIrqb-_Z0Q2pTNtUCeP4pZmiya5CeaN5QJkjL37T3UuCQMjy1IXLm1v4HqB9hLR_5Jkt3N-rgIl1MoPKd8ts5I20zDxj0HUQib2mvaxWGz_Pb4xNoiU1We8O_RQRE2iNbsI3WGnUfz1b84TZqdfgZY8cGTmsu8F2thYmQGbHYXfV5lq8rV5rTdyLf3KIQfeVEP0SjGFtMgHhfUg1t-09L27zFcoNO6z6XpecDwotA4Cs0CVcZgSI9K_mtqpJtNNKCJE27tl93DAlcKNRCEAoZgzXk8V12aCbo28YD9T-uTcxwdP2nNBHKyCn9mTCYpuX0rnQzJNx0Id9BygXdkOPHT9KHWPG11cuT98nZRUFRRCgtKvRpHhgnkLFfFteL1N1irbc4WUmOAIOkHu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfynE5Pnk4AIo9yFYJ4MzsadiamGyblRILPd-qVb7TJmCnWUi5rwK94QXCe5djHgLlq-fll3e9HKFF1g6JM3jYP0uVa3R0OugDqaSv7eXU0u7vf-vAkhMm87JcjMV2bX_aKrJd6Py1gcLvsUC-ZVtNdONSXRt5koA_xpaFJNuGpPTkBSJt8Df45uUUTOcLg8cBWEm-q_4y0d2EUDC-vAwWovP9mIcSZ51W3GhDIpp6N1nj4sww3zPLIsvvAlMkc67zsSfo_GuUCVuirEsSNAnjeAeNMJArOhvwCwVb9MzDJKPYQaU2Y51PuUofkkqW7IHsjk_fsfCAfwwNdwITNzdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=GNYABHrDi65zrvbM0aU2cbVHWzR1cRCfTlm4NsiElRtXi9JV2pvk12-xBByTAoRUTOEbYYrs-1ci1ITChPdPzyrt9VKlXogomutV_wMzE4giSWAuiFvzaXLD_wszwDV2a-h4_pOGu6eW7PpbViessAlPrLz7O5wOQs3kvmjmFoVJKQXc9zjzxh_P6d74CVIA1Q1nBFitqGOzZjChr0j_7KTVjQVt_ts5XPQhrPbZkSfcSQ4zEQLn1qZYsnfWfYYprDjzPq3O-ni8AFBH--qYwqBTnKanPVA4zYQ_e-wKCXY9OokJfAcOE8gi7Fh3K6xMNjaI_iyN0DsQgcIWvFCsonpMtmFPLfQUku9G1ZJWkhPlv7s4yEngm6CVwazSykXWQhDO7ESTw3btxK0LhxCXIOR_DddzOQdDvLITpQ-M8OR85GFj7XKKvC9Vz4kknJFLwxcoAO1Y5WunMGpITfAt6BfGS1jwtZCPPpTyttdCXgoErCCTwb8K1QocMJ89Rs18FcqXfhHC_KsKxbEJU7U5TTj96MprsVi27n89qfYoRdCUl4bSN-oFV_9g2tWFJEg5pVobl7qH0tvjuB_Uun5GG3z5lyzknYXz61YObkNPHMO4PNimtmFr_g-RQKdxp9r3LNfR_RvXwGs5en8vCYSucXdp3ufdGb2JmFK_Fx0Ek5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=GNYABHrDi65zrvbM0aU2cbVHWzR1cRCfTlm4NsiElRtXi9JV2pvk12-xBByTAoRUTOEbYYrs-1ci1ITChPdPzyrt9VKlXogomutV_wMzE4giSWAuiFvzaXLD_wszwDV2a-h4_pOGu6eW7PpbViessAlPrLz7O5wOQs3kvmjmFoVJKQXc9zjzxh_P6d74CVIA1Q1nBFitqGOzZjChr0j_7KTVjQVt_ts5XPQhrPbZkSfcSQ4zEQLn1qZYsnfWfYYprDjzPq3O-ni8AFBH--qYwqBTnKanPVA4zYQ_e-wKCXY9OokJfAcOE8gi7Fh3K6xMNjaI_iyN0DsQgcIWvFCsonpMtmFPLfQUku9G1ZJWkhPlv7s4yEngm6CVwazSykXWQhDO7ESTw3btxK0LhxCXIOR_DddzOQdDvLITpQ-M8OR85GFj7XKKvC9Vz4kknJFLwxcoAO1Y5WunMGpITfAt6BfGS1jwtZCPPpTyttdCXgoErCCTwb8K1QocMJ89Rs18FcqXfhHC_KsKxbEJU7U5TTj96MprsVi27n89qfYoRdCUl4bSN-oFV_9g2tWFJEg5pVobl7qH0tvjuB_Uun5GG3z5lyzknYXz61YObkNPHMO4PNimtmFr_g-RQKdxp9r3LNfR_RvXwGs5en8vCYSucXdp3ufdGb2JmFK_Fx0Ek5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hExuy3srHDXGghKKRuCY3TFkmoo9nUTrECtVuD9Aah_ZH2HADVLy6lzx7qIdHgakqU8-3i94RD5mzSgRiWRzvLT_VXKg_iNx1fAV2D8Zm_bEuf3TXd56236oGh8ABkzpxraVDULc20RwsCnRfKt1gZhXWmGjTjBTGWxfGlQMUvCexwJmK8QFhtkPvBH8S3kTx-V239lsHjbHPRdS_nR1rXLjTANcvlT288sIEooMcZjTcr3S2BmzN3ufnDBYp8Q44RK-OZUIumojcOWZpGdRzKSwedAuxFj2timqZt-HHStW0WP9MDb4qtGgEQFTd6ISYWJTU3wEe07IZ3paq6Byhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwUthKWMaLEAaeywAr-r9pOcbldy3cilvnPrml_VsRCp6LB1XhQsWzXX2mQh4XjgXgNQR7wECO1ZmGObTTLTBKve-a8aIizNuk7x-gTkdvm4BxVf3i4dvjcjdtZmWQKcKz4qKkNemGYqx3QA-ndnS2nY7TLyRxCXTO-R44cCUz2uR-yfRkzJRooHw6YvXzT9IPlKxZE21KKkVzETpig7E8704ObOzCaOQzwwGEvJ_15tuaaSBOMUc4j_h14uT79R7H16KuEMoQ0CaCtbJcnmbEXZQGu9d7CcS7B_suVHoYcTmyQlIM1_RMPj6JjQallo4SC9IjoavQl9p0zj7ImZmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVlkOUjPL-lYcZdGNOnMxwcNDgf9yF2SNKd5ZT8b6iw-yC-K7uyWjtE70cF65pssEhYq-2MnkXdMd-PHnpt0U-bU4TODa9bYFc1vOpaZX2FA6qq97C3Px9V_YGQlYL_-KVawvKzfugpv1k5mBqLGTc0mkx0sjgNNhegH1Kf3ztrJG3aqunV20Uyv2IW4LOQ4UiocAPDlmfuaScQWijESlDnEPoJLkQlv4LZYA6dEmZpQswfq94XLKKAnN70LsjmyH5ibdy3w5nNOVfnSe6pjGu4NryLFFiioMWu6kmV_hPzJzNpBOlmh_PLVoMhE3fHW2hjisRwVBHW6WV-oZqA37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JDLfEHUxIQS5WDFUSukD29y2ufM1gbv-n6Ltqs8lhlUefHYgFe0jpps4Cz_Sq_wRemm7PxVGNS7QMU6r9tHXyPjWmJ-9OsmRggamK7i6UEOIpg5LG_zIMb_2jqj4aMHSaVnNuVEnrtHntri6kcDBP7laBb_D7HMsc0rMKKl94-XLimvA1axttUO79-Yu-cOpPRNMwKtk2DMS4O6hE1fgE3I6tplSaKF11vEbg2uW0A_-0upv6A4GVeBMjJ8U9WjB7qohXX4a1gGE8BM_sWI6yCm3HYfbgK2mflUuT7CwIYxo1rJdSXhv7CDuE9fJ8Ym1a2AyrrWvu13V9LBveUP48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JDLfEHUxIQS5WDFUSukD29y2ufM1gbv-n6Ltqs8lhlUefHYgFe0jpps4Cz_Sq_wRemm7PxVGNS7QMU6r9tHXyPjWmJ-9OsmRggamK7i6UEOIpg5LG_zIMb_2jqj4aMHSaVnNuVEnrtHntri6kcDBP7laBb_D7HMsc0rMKKl94-XLimvA1axttUO79-Yu-cOpPRNMwKtk2DMS4O6hE1fgE3I6tplSaKF11vEbg2uW0A_-0upv6A4GVeBMjJ8U9WjB7qohXX4a1gGE8BM_sWI6yCm3HYfbgK2mflUuT7CwIYxo1rJdSXhv7CDuE9fJ8Ym1a2AyrrWvu13V9LBveUP48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhsAfbWR0qBxdRmGBGdRfTPuTPrV46NJFZ-ODRRnH_JBwNteDuQtMfNnOL3GjemKQFtGRBB01a5RYCvTLRfQEZdJRxuLPNzYfCJ9Ck1Iw7gxRmRkgVtJsE_38RebFV85bf8UY6kXNrvXoxsMTGz6W8B_ilMpHYXSwvVJiK8uH0yjIHGpEVR8xuM4aNyEgVpMRH04AvFOddxkvY9IMqvSwvMeiDBRLEY-1sTirUQQ3t3_TziBDQK1nyld9nfqdU--B_Kp2GIQB4PcXp2AfBYHpIMefMH7Oovk9iA6q3-WVopFBuwdHdMdlJry4JJjROkBHW5ZvYagPtHfxfFEEWhQrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH60IhTxbMTV9D0A3uPeIvYFf3a7iDVX54mNZyD8u_Mlw6OOnwrJ_Eft6qBaknVXbAnn5nRK_5T8MP_APlvxZUjwz5UvnVhdqNht0GSt8eQZk7gRfVGVHCF9y8jwKh69RxsqlYsDRfnJ2-8_8SMAWCwHuWpmSCcYF5wTeZvF86jOTorn242Npdc2q8q83LQvNrEYVZEhNILnCtgaBMn_JMGNKLQYZbg5-Tg5RtbvDg4JVkmWyN4NlZsQpJGM2VRNblRL7JRjTd-0QGNTmRYjtjSqVXDxoDnhsVljnOFS4NkMujyGwWNVyjUZobEGzpmJRtqxeKOVFuu-_rsGx7oU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JsFpY8CxhcWNJrCpZdKlolGUlmH0Si7tx8DAEvT9dH1A-PpYxOoYPEomDDF3lgABBORWl0PifWywij3PpQBIYZ2kPem2ja30ZbYRT7aU3tzvoYk2G7VZliJlSRx4F0aEsOo8XTP9ZIAQmA1V5IJBv4Qbyja5N4-OroO9aP4olV9FJyVBllPXfQR28FHWTHSNtxBXYRGWlYMwdaQjNMUaGrr35F1lY6VufpgjiZs2FwyfAUnAGUmoQPs3hkfjvMGVl_aYuKCA2H5UNMCokff-OWy9DMHayi0rzUuRKzUscNNXxGtAezEzIql2c3XhZbjEHMB0hwzMkowgBaWhNqoruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=D-oEzLLwf8Y-np9aue_a56Hcd0OdvAkuzNQHq_2hnLNJ6zsHwmHLn5Cuox5BJLmURd0IJQp_Wxn8mzlJM1YD6YtTxMl64_efOpLbqzjGHaaQP3rsKuuGZ0C1hC8PcbfT-XotCiisC_asGT-IeeYupSrFqeaBZIbqD1YlNKqarOzk3v6NS_Rs-jm0bOtNkkWIZF1K7N1ibtaZ3wktjwN8hD2WTc7dIwlaKnjNW1XyJXmJi5Kw-qrqadF-EwuyWTZH4OLqnr1_XcsisLyp8u8EPy15YyTMu0F-Lb6vmmuL-cKaqoRyf3IXki-quTXB1RXNzVaBp4mwpXKGw10GxB4mSy6pIGBQKwgXDdeDO3qiBh4wusDCbaA68umoEtozULfEpp036Okd--P46Zzw0Au2hJMx-EeBANLYkHWj429vRqNx6hcpumGBoPKUV86t5NNfJxDTtKr3KoH6J-Lf8AllzUZHo2xJ8maKODH-x551k2AB6qWcW8-1qFE-e7PrQZyn_9OqFQ3cmYroBkbTA3PuZ6GHkd-Eos3V-7BOPoJt7AylkxUSvBSM9qGeQQESBQqmyZNfJ0_SGqNZ8DXqZTK0ZAhjxWnVMlFcCVHouWl6L4FRwHhghiThZ5eogwisn4g0IylhteRwMXlR8mwUL--u4ACGPhY2bIAJme_-W99x63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=D-oEzLLwf8Y-np9aue_a56Hcd0OdvAkuzNQHq_2hnLNJ6zsHwmHLn5Cuox5BJLmURd0IJQp_Wxn8mzlJM1YD6YtTxMl64_efOpLbqzjGHaaQP3rsKuuGZ0C1hC8PcbfT-XotCiisC_asGT-IeeYupSrFqeaBZIbqD1YlNKqarOzk3v6NS_Rs-jm0bOtNkkWIZF1K7N1ibtaZ3wktjwN8hD2WTc7dIwlaKnjNW1XyJXmJi5Kw-qrqadF-EwuyWTZH4OLqnr1_XcsisLyp8u8EPy15YyTMu0F-Lb6vmmuL-cKaqoRyf3IXki-quTXB1RXNzVaBp4mwpXKGw10GxB4mSy6pIGBQKwgXDdeDO3qiBh4wusDCbaA68umoEtozULfEpp036Okd--P46Zzw0Au2hJMx-EeBANLYkHWj429vRqNx6hcpumGBoPKUV86t5NNfJxDTtKr3KoH6J-Lf8AllzUZHo2xJ8maKODH-x551k2AB6qWcW8-1qFE-e7PrQZyn_9OqFQ3cmYroBkbTA3PuZ6GHkd-Eos3V-7BOPoJt7AylkxUSvBSM9qGeQQESBQqmyZNfJ0_SGqNZ8DXqZTK0ZAhjxWnVMlFcCVHouWl6L4FRwHhghiThZ5eogwisn4g0IylhteRwMXlR8mwUL--u4ACGPhY2bIAJme_-W99x63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBozkFAEuSJFdBIqEXEHo2DNBGYQWQRaDTepfUhiDGzOgEsKgLOa3ctVDFkhre4QlmNfufuab0x6FwE27KcGJr2rVkeYX8M7QSWLJF4bNGhyp6T9khZjO-6YPBGfeiuDcKjW3x6Kffc_8JsrWympmILCvjRYsbyj0ZisgJIlc5_K0i-v_nvb-aHkSPWTCYbwYdlriQEcMHrNleen_8sEf_PESqsW8LUwsSMiM91oWUIbxk4svQJKQFutHnn7MnIox-5PPy5OJx20q__2E1kOiit8YvuQle_wrNWwXnDVTJx07eIAhYOhdhV1kmE-0D1-3pQMDNhlOKzXNw8OSPnjW-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBozkFAEuSJFdBIqEXEHo2DNBGYQWQRaDTepfUhiDGzOgEsKgLOa3ctVDFkhre4QlmNfufuab0x6FwE27KcGJr2rVkeYX8M7QSWLJF4bNGhyp6T9khZjO-6YPBGfeiuDcKjW3x6Kffc_8JsrWympmILCvjRYsbyj0ZisgJIlc5_K0i-v_nvb-aHkSPWTCYbwYdlriQEcMHrNleen_8sEf_PESqsW8LUwsSMiM91oWUIbxk4svQJKQFutHnn7MnIox-5PPy5OJx20q__2E1kOiit8YvuQle_wrNWwXnDVTJx07eIAhYOhdhV1kmE-0D1-3pQMDNhlOKzXNw8OSPnjW-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyD6lKwkvoS6CIr7lld-pVuqowF8jure7aKOEUcum1VYJUJ8gOyCaMjGT5wmeaVsNq8pgSck3hTf5kRlRd0wkBM2UxbbFFjbaBSAbWi2ePSIqDaRqrKgZVDe6AqL1FkwrDDxML-pARzjex28PBqUaFGbRqffunVksq_cwQHi6F5kFItsZifo7g4U9sBs4rRc5aB3GWl9UwyzasR9PrhKqS5V-xAmrUEZknTqIzHRyihzw1N0bxS4ltlhpkSDk2RhoHLFHcG9hhUeXpzewyK-D0iXHqzfuFUYyewfN2kDfFBs1QwspxY88jSssirVFaj_UmV8VBkfoziAmDlSA-nhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-8bIOynbmnrPI4AurzCTfU63sEHVC9j2T7oX93PtK3P6erETUxNft5PbZBJPGDHX3-tcllc1oo1K380ehkp1KcZHteqVKA9f2r4o_-qfS9crMnn4nbdKWI7rkHRQxacPzwuH8tpT6OjKoD3pC21EA-zdBpZ1P-4qgEx_D9oIOi_UNtw3yVHOyhdBqYJgVi0rhZST9iWME3URiMHRh9Jw1BdsgqAtgoUGnUC4J6i59_o_Dz_RTu2rwWl4n8b08umu00YH994Bo7ysdt_LnCajbjpjM1QYigbJTIbWeAnf_oYkPynldIAYsnj7Qvq_T2419-oU5cGe3-uV_QUyXBH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVB406W4m15UG5bB8HmbW903EoF7A7thXZ2aZCP46MSKQIICyLQI0rjCv5y0VKxqtPATOrM0AasSKXSONjGTajp6ZdA5lng04BammOrmqjp6CD0neMX7kdCgAo0Ue3rvtu6d42jjXBAFOIARxAMgxsGXNNqvmdLPBU7FSaZbhBnaN-OowAv8ApB-ILTXDZv9h2wbAR5RB_D82TsiF02pBoUaldfEfV13w9Xke6qUNul5N6RnIyanh7xUEWz6BQStcgDRzVOezo4czTLfliZ2IpPt0KXGDHJXK7O2-mOvnzD0TODY6zd9LsKX29hDBsHmikAEuxgmq1VvUhd5iSNxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
