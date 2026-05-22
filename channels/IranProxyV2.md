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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 19:15:28</div>
<hr>

<div class="tg-post" id="msg-8474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دارم یسری تنظیماتی رو سرور ایجاد میکنم، بعدش نتیجه رو خودتون خواهید دید صبور باشین، چنددقیقه نتیجشو بهتون اعلام میکنم
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/IranProxyV2/8474" target="_blank">📅 14:15 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am_mPDwp2PdcSVdNlCwdQj1uTVk0pi8lsFnLUWi2c6JeVwQ-YsMqmTDxFyQaBwNhMRxIzarAkOEP_EOWZLpZj0o2Ad114HicQPNUijEXmFyoldbfBHpvvyr7SSZQEWYxMuVfGsb7VtCURImjnLun5d1fFyV9XN90LOqNw2Mzog-ZNf2QRwknj82saiGpBP13-s_7jrTjpUvSWnyOjuhq-3J9rAdyiYmxcsHCA_6UQBrh1hE4jhp4fXBBbsJw3DTBKBu6mGB4i-kkPsMpubJVCarXV3BKGZTnBeN29awuUW2_FynXxavOOpX1dI7yQjJKsOTJ4qwo2K2zTYkEJqKN4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=m-Jx2GE0_XwqmPQYNh4IPRD2BsyzZjgmCfAr7IujXAo7ki5x2E8Yp4okihIX7IjK8ACNvTSzAkVMNH1KNWWD2Y-FEkNOcyi76NdXit2XOrCJgIRigop0aNdyalJMaE1BSxvefI99ZMAvtWToLkWKXkt3zGG8ZDaDuLv92VyRuDC3lLFuCOvvFCeH5jq5vpWRhQpKl_G7nUsbNL3lGSYdDguhxT4H1NbCgNY5ttjdtKl37_ChkP7GZX8zQkNx-xCozK8gjoLN6IjYI29Pty4hV5ijaJwO9CoVeKj8sqMo_RL4Hda7K4bVNO3eRKRHnZbpZrlqeDbFOhN7E6y4t4PEqRSkVDwe4iOUi6GC5cRNL9uLoHQ3ecN266B7WxXlMuAMy4v27hb7pbX8LCkwj0WgOL-kYFqxU6ezoJyuG5HLcNpIUpqBNCcRLcKMVnIwXLolUFbyXiiQc4F7GkqsOtK_YwWyw2WChshDnNtRKEFYHvW0MtGr3WLxS7wTl4BH1e6uHMpe7OaLgRAWxwDAFzD41Wez-PpAOI5eVGPEGUqpILhKkLdy_H_8CnOzFuewMq3B-axJYsaJGzBk0AARWU-Pea3AWgjU2RLps1MX4Kjr5CAt6ZRbl6qomY6vDnScBCiAQ_G3B7DCst7CpFgn_qQIcwDJ1wwZT-_8YRXRYt4B658" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=m-Jx2GE0_XwqmPQYNh4IPRD2BsyzZjgmCfAr7IujXAo7ki5x2E8Yp4okihIX7IjK8ACNvTSzAkVMNH1KNWWD2Y-FEkNOcyi76NdXit2XOrCJgIRigop0aNdyalJMaE1BSxvefI99ZMAvtWToLkWKXkt3zGG8ZDaDuLv92VyRuDC3lLFuCOvvFCeH5jq5vpWRhQpKl_G7nUsbNL3lGSYdDguhxT4H1NbCgNY5ttjdtKl37_ChkP7GZX8zQkNx-xCozK8gjoLN6IjYI29Pty4hV5ijaJwO9CoVeKj8sqMo_RL4Hda7K4bVNO3eRKRHnZbpZrlqeDbFOhN7E6y4t4PEqRSkVDwe4iOUi6GC5cRNL9uLoHQ3ecN266B7WxXlMuAMy4v27hb7pbX8LCkwj0WgOL-kYFqxU6ezoJyuG5HLcNpIUpqBNCcRLcKMVnIwXLolUFbyXiiQc4F7GkqsOtK_YwWyw2WChshDnNtRKEFYHvW0MtGr3WLxS7wTl4BH1e6uHMpe7OaLgRAWxwDAFzD41Wez-PpAOI5eVGPEGUqpILhKkLdy_H_8CnOzFuewMq3B-axJYsaJGzBk0AARWU-Pea3AWgjU2RLps1MX4Kjr5CAt6ZRbl6qomY6vDnScBCiAQ_G3B7DCst7CpFgn_qQIcwDJ1wwZT-_8YRXRYt4B658" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnN2H3hkFGkgTAilEcWCWA-JpWBHqPt6eb3g5rkYX3lhHI9IxTgsbi3paEmgwOI-6g8yisnz8r00tYy8u01e3cUT8mz5sRO6q7ZgcEQrUdrrLd8-EZeSfMZ9C-8PnmmCL17C6gIYll5FV7_IxlQP2H85YYoh00TJhNTM4fV-B3c7h0fV9P-hrPGERV4mwgMlGJnXU3ZulaeyIU7HLgE0Hn8G9bMaxVa5wOYqe3vpnmg5c4___ybKvYgX-EFRe4K-cy-3dMCWQC3RfmyiFwppsvl9_5TRTK9MKCez9mfbxtrKam2tNMTGy2IbUPGWlezOrnV7ib4Sq7HvrnCLmi-oKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMdlSOVP5QigheLTD7eRgEQ25vCbt2PHNmcPxEjQE8VDwHGSpxqFSNTFVTvgvr3dykVpuc4_H2XVOEK1_G5Hjz8WHMNFmzPGoTLZnuyJczBBsoq-8fFwBsLKpW_jzUBZenCI5zVvOaBa3yrKajDpMmkQhEY53W5KQ1Qp8JW39KdD3IjR-I2poDV5xEvs7tq_GLfbFky2NWTO2XKS1QgcwopJpOQV49jqnCb0Gt593_x189-urjnUbtRbrTZvZ3vN_nRhU6LA1hgso-mOX4M7_vSB1un_HHFo-zV4xYEcq2iOTVcKvqhpr0x6tOZOiM_jUBC178Q8g1H3qB3ZU2SN5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYQvwffikulNRe5fbz72EyqMRzxRvpb0IAR4H5tN837ymI2aQchz_0riwW_sHv-R4t3DLN6sgeGa7WZgmSjcnu2XItyGPNj6vjJq76BPQeU2KrfolHmJ5l84UDkuC6o7bm-N2dGDsZiAl25RQgl38IV6FN8eooaVtY-SEwSLSBpGjK0go-955WH9sAVnbbKTD-9cQihVSnG7HRbbnNY_VbRlb5qHMg7BR_5hSFxwO7GK-oYUGDHx1OAWBJ2ml_oHcn4FqSR4nA5BQPiKMFyC3BbxAGCFzpZ4vwfqJEOSpu4rr6YWxyxSiTS6Y14rxExK0OL8pmz-gzc8BpmYWZoC9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=b4kHSFEtEvQOpFSEmolN0k1Zqr85bg13vIEmItZdMabN3xTnyt7ar5i8-QG_NC4MSZ56pjVWxRnYiN0Xi58CtlK5tMancA_2YRVF_jazLvHjWQj4nZX8wWTd1W90fLovQWcJ9sLDaR84fTmT7r-Omrv6BPHBcUh2SNOfGK0O0G8FpiEJ3k92lK90nlmCys-GLYCRihZB7JBYQXd04H9gSACi73fHYoTp98dFMGwOjNAkPru803pug0wYukNrtVVeJQ-qW5DzdUEejR5-RADjXwg29d75lSvMqUeWah30GEMIWxnQFEmuwKgtLgDnZRCihqYXWyiTxyf3cSMEomlF5hI2Iaj8LNklFV99fxPTcKj06ISS1wOVOE7pAzkOzUxYynBP_PvUD_Bn5iOK6auySoaGXEZeZAfH5ylpjfIMUw0HheDP8VwdutgUp6QzTeNcFm_K8HwDYyBX2Uf_HxpmZDEo-iw7eAYgi-enLmPxQByVxg5SP3BjDjNB4KSiahiCa2wrnRItUYnPxKy5Yodyq_vnfwso-wUGAPq09oTWrCaP2-if-YbVHTW-xK45ozMJ3t__57IHttRVjYQC6_uJp1ekYCoA5d7x3hV11GdZ-8n4veVlVkFBoE-Ejh35PD7-XrPbeU6LhtKEUFXauh1BMHCWjyLAGoA-uz7UEwOr99M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=b4kHSFEtEvQOpFSEmolN0k1Zqr85bg13vIEmItZdMabN3xTnyt7ar5i8-QG_NC4MSZ56pjVWxRnYiN0Xi58CtlK5tMancA_2YRVF_jazLvHjWQj4nZX8wWTd1W90fLovQWcJ9sLDaR84fTmT7r-Omrv6BPHBcUh2SNOfGK0O0G8FpiEJ3k92lK90nlmCys-GLYCRihZB7JBYQXd04H9gSACi73fHYoTp98dFMGwOjNAkPru803pug0wYukNrtVVeJQ-qW5DzdUEejR5-RADjXwg29d75lSvMqUeWah30GEMIWxnQFEmuwKgtLgDnZRCihqYXWyiTxyf3cSMEomlF5hI2Iaj8LNklFV99fxPTcKj06ISS1wOVOE7pAzkOzUxYynBP_PvUD_Bn5iOK6auySoaGXEZeZAfH5ylpjfIMUw0HheDP8VwdutgUp6QzTeNcFm_K8HwDYyBX2Uf_HxpmZDEo-iw7eAYgi-enLmPxQByVxg5SP3BjDjNB4KSiahiCa2wrnRItUYnPxKy5Yodyq_vnfwso-wUGAPq09oTWrCaP2-if-YbVHTW-xK45ozMJ3t__57IHttRVjYQC6_uJp1ekYCoA5d7x3hV11GdZ-8n4veVlVkFBoE-Ejh35PD7-XrPbeU6LhtKEUFXauh1BMHCWjyLAGoA-uz7UEwOr99M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=FE5D9PPZPBuqoPMcEltMY4kTS15KSsQRANhczJSmo5Ka8hMFxDbM77iwgkodDIrp0TaCS5aZmkwqCMViKbM5dw2KIN2yIqbkgMEl7wm67yt2dCE5OtoAiUn5kN1lNzK9RegLCF2wgIeohHFczYrrj8zFwLePc-e67x-xm-9qkf2NQ9Y0oA2P3Q-FeQ0eXneiGXl4TxsSkDR11lBSUG73kIJ3eIpRPNWqQ4in28O_f5X3DTu9FjcUl9xt6-4TCsBTD-vrolHsoW4wCKDVsIUXVhopsEFT5NGVX-LTqTHS6kKj5NptJvcLU_RNp_m1TgsCbntUX9gBy_uNBoqsdUyLYqivX3NXOR29FNZ723WJdEv4bkQUhWgLK2DEXArw9-LzWEJMg6JdL5Bpg8GZOTOr9FZc2E1tgYp6f7XPQS2S9CPEcjjEYvWgQG3-J_4iixkfAR-SoKI6wmtqY6FQ2MrtuzhN889QAk6XlBdGVngt--Yo-hPqAyceOBtshMONlCA3dRYWpwQ2Bn7d9czV8o-ml7bPmJ9MzubAatRGKVHnS5pNsA93SjTFHgF6KnLXSWhQ-wf-zWlJHbyoichQfKHUeQZugYtP_5bZKLQDEA5MMA266mBlC6-C8DP3wGEMG9gvp3PBc3GpbRU5_f2PVvNSdhQy-niwbq_HWuWBVW0P2Mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=FE5D9PPZPBuqoPMcEltMY4kTS15KSsQRANhczJSmo5Ka8hMFxDbM77iwgkodDIrp0TaCS5aZmkwqCMViKbM5dw2KIN2yIqbkgMEl7wm67yt2dCE5OtoAiUn5kN1lNzK9RegLCF2wgIeohHFczYrrj8zFwLePc-e67x-xm-9qkf2NQ9Y0oA2P3Q-FeQ0eXneiGXl4TxsSkDR11lBSUG73kIJ3eIpRPNWqQ4in28O_f5X3DTu9FjcUl9xt6-4TCsBTD-vrolHsoW4wCKDVsIUXVhopsEFT5NGVX-LTqTHS6kKj5NptJvcLU_RNp_m1TgsCbntUX9gBy_uNBoqsdUyLYqivX3NXOR29FNZ723WJdEv4bkQUhWgLK2DEXArw9-LzWEJMg6JdL5Bpg8GZOTOr9FZc2E1tgYp6f7XPQS2S9CPEcjjEYvWgQG3-J_4iixkfAR-SoKI6wmtqY6FQ2MrtuzhN889QAk6XlBdGVngt--Yo-hPqAyceOBtshMONlCA3dRYWpwQ2Bn7d9czV8o-ml7bPmJ9MzubAatRGKVHnS5pNsA93SjTFHgF6KnLXSWhQ-wf-zWlJHbyoichQfKHUeQZugYtP_5bZKLQDEA5MMA266mBlC6-C8DP3wGEMG9gvp3PBc3GpbRU5_f2PVvNSdhQy-niwbq_HWuWBVW0P2Mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJewAXiE2D62p9TUpCc3yfDUlRFkbWle7kQpRABDd1Gd4mwFH-Aq_RRUErgUdzzom63mRlomDOJn7m3hbUZm6-3b83dWjQWYXYKTEXD_xCfLE89e8rsPTjwNvhiGuw0Gq8ogd88DynueTttg2R9njxpYReF0htUvTGrqT-EZpQq-eo1n8pJoOBWkN8aVwb9f6OdegUOENjmCCwCNwjj3NeDPyYfAfHX-2doUu_RZ327qbL7FdjW6nIp2Rs_vbomZdDVXumMPSa4V7RR1Yf5aZSBd3fIWYnX73oQEVzI_JoEN77JQETwrPMzVO1YJctWxIRKr9Eo2JfpKV8oj0Spm-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=NOGnMHWJtr5ioM8qIwK4CygoQawWK_Ua-iPQ0jApB8Ua6UDErullBgjrvP71HA80A2-a9EyIGa24xX6IzDTvIYrVyhJ0AUtiAh-JxlHbZ4e3fgbD2hEMCchOg0vDp0-nKS6wV87h0DaWFYtgVTXzy-QpjkCDVcTor05qFrcrzD_VTVvfP0v7RBWYkr0yKyBkhcYMRmDzJdKhEX_-GG8sovIjZI1RgFhH9y2_gC791bVUr8JDLsbX8heHajcmT-LGqEpexc1ZIRW6DlcJnTydjwSVtkKybKJrsSkeiZuammROgjrIMwR2zXoEt4vTw6PGQl5dNUNufnwhTxWIU2xFg5iNKn2IG3H8ZhGgJr-AoH___7NP8wrCMCblzwGU1OETMXEEKpgcYd9eE22tqSkdQR78pT1RTXXqr0Ixe_4276xszuoV1UK-cWzlfrujLEw9fQzPnY3nA62r90Pu-Ous8L6F5OEEE8npgAbNvOy66mQBTdr33Fyv5QBhdianzwYT_d8amelMAsS_pXtjIc00hWItuAy06J_zU_ftd3WhJrATg59G1lSrKKHa5xaqwoa37sD_2OVXFZ6fQchU6ppug6QSApDZVUBNazK_T5r06JfaEHQ1neHPjL5Xmb5AKvSOXZUe2j29adAGMz1pm4InWbjWKh16ipUTJG5CJUTspK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=NOGnMHWJtr5ioM8qIwK4CygoQawWK_Ua-iPQ0jApB8Ua6UDErullBgjrvP71HA80A2-a9EyIGa24xX6IzDTvIYrVyhJ0AUtiAh-JxlHbZ4e3fgbD2hEMCchOg0vDp0-nKS6wV87h0DaWFYtgVTXzy-QpjkCDVcTor05qFrcrzD_VTVvfP0v7RBWYkr0yKyBkhcYMRmDzJdKhEX_-GG8sovIjZI1RgFhH9y2_gC791bVUr8JDLsbX8heHajcmT-LGqEpexc1ZIRW6DlcJnTydjwSVtkKybKJrsSkeiZuammROgjrIMwR2zXoEt4vTw6PGQl5dNUNufnwhTxWIU2xFg5iNKn2IG3H8ZhGgJr-AoH___7NP8wrCMCblzwGU1OETMXEEKpgcYd9eE22tqSkdQR78pT1RTXXqr0Ixe_4276xszuoV1UK-cWzlfrujLEw9fQzPnY3nA62r90Pu-Ous8L6F5OEEE8npgAbNvOy66mQBTdr33Fyv5QBhdianzwYT_d8amelMAsS_pXtjIc00hWItuAy06J_zU_ftd3WhJrATg59G1lSrKKHa5xaqwoa37sD_2OVXFZ6fQchU6ppug6QSApDZVUBNazK_T5r06JfaEHQ1neHPjL5Xmb5AKvSOXZUe2j29adAGMz1pm4InWbjWKh16ipUTJG5CJUTspK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAbDnGNKUwTVmZyBEGB2xdXq6pPXQWKXJfsMjgshCafgbB7BFvVW13tt6TvJ9TA1ZBZ3TTuF2-h0djWMTZ9n0V9pfmamwVIvRutlbD3MO8ktvOY0ns1zcMmioZb2Q78Y8eWhPhmk7TfTf88d06BhETxLQbUKovDJ1GY3SnVowzcFgUN4fzH92cqDK4krF-eHsAM_rDSE9PIQNLTY18AD5-tYxvm-ugEb5ekhu-0RMheOLg8rfmKvKJtGRCUFbFvvP7fLGkhTnZ-TpF3Vg1td1QnuH9kC7VbDWCZuM8BCAMvgT3ueFWhItc-apkh3RPrEvJIqqZq9TNzTmIDQL-Zlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC9f7Ao-pAB0uygwIoBzlekoZT2rrUSwp63R9ObD7KIB-oEUjAzBYucUNv1pUOusHHf-11b0ZBSkeBULpBBwrI4fsJwZog4LYgcs0N1RmZuVvmkbddtqW42K5mPPVi8D4hSvZqv14PJUaKavRIsDfXjB-DxfOZpmrye75ndfuZRMLZdvdZ1RmbQQ7I_a4Pc--7gMEPE5wtQV9VIKmOkX9RKkWZ9e6CYzX3DvQaXTsBWa-vtWTAQB44u-PYHu2M7Wb2HYqwol8TsKaCKN3aWHkG2-gSC7NdxqepXQlgcnkbJ0uEZvyr-rLybvDzXo_aNZ7XrOlynrSN4YsFFNnj3-iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=SmWd0aeILDoicg0WIFXypfiZcxy2uulEZbLLambkqVqlcggO2CZtzQ54FxOzFNYbTZrGmtGeNYwqLshGJZqTAoEL1icfMFcN9xUFpRrewGmpeYXRe7mIi5Dz3nRqCJ6-2gGmwDr1PMH6POMJbfqCzb55OeazxA1y43NHogWMNKf8zujAlMJ06DxaxknV0pKe3k4A1-rbKpqX0RYW4Zr7Nw-xGyr31R_GqQYJBycEPk9v6EUGToi_n-JdDJq8ruAuCY2rDt_PlfOV3c5k0t3muJdyBS6GuwJoILeEWtYAXngWBIk1L-gfoJD9Q15dz5Z-phSW6C7jftzLqti-W0Ypyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=SmWd0aeILDoicg0WIFXypfiZcxy2uulEZbLLambkqVqlcggO2CZtzQ54FxOzFNYbTZrGmtGeNYwqLshGJZqTAoEL1icfMFcN9xUFpRrewGmpeYXRe7mIi5Dz3nRqCJ6-2gGmwDr1PMH6POMJbfqCzb55OeazxA1y43NHogWMNKf8zujAlMJ06DxaxknV0pKe3k4A1-rbKpqX0RYW4Zr7Nw-xGyr31R_GqQYJBycEPk9v6EUGToi_n-JdDJq8ruAuCY2rDt_PlfOV3c5k0t3muJdyBS6GuwJoILeEWtYAXngWBIk1L-gfoJD9Q15dz5Z-phSW6C7jftzLqti-W0Ypyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcv2OM5QCGpFE4U2CxWLbl4xYpl_xnBYxUqd6M0inIVorxwNIpa3fJinbp7TJXAx77vYvccFKGIVEmVoD0nJnz6nRlS8FFxTHIPuZLVbbspt0oF98QSqqdqf68iJ6ooaAvzdrYj_M5GEn05Ah6Rx2UxtufP3Vj374NedPAJpoy_VVCz8yV3sy7PKebGeKaf3vVAJfafHIyqC7SutLEU6XtCRLR_5suTJpp3PTDwlcmqAFAnm8yO6l3NhSWynK1iWurXxH2306MfgTkJyNbXDntpzKvyyfriHsu-V11xtFgq_pqBRsZVxbTAWFuIqNEwBjV4qeblAct-lJ7fosW5Y4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMpnhHeBNXCK27UoV5dKTDLeAOhcaWWXspe4JiIjXtvz_0-jJuWq1QWaCrjiQPmpIsZyiAVqiu3hb67q1BYs1G2qcJ8LhrfMDDSSV8NrNT2YMCGLJk7RDnee1OaNCOPACzx7Pz3QnvEMmM8FEbg9254tO3OFoQBHJuyuWvu9mh5FVkI3Q65ctjRWXm3iuH5RFDxqZME71qhpeBRt_nQ7BPejUMPlSiHyLMbFHHSVSz0mkdNTuBx-zz4ejLFhxtOv0dMss-kyfYBJusyDTVTAJjCVt11E7AzGYVS5GKz-8lBfd4XWHCEJ9llx10U1n8_2e4YkNC9N9vgMU3deQNiX3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=cgOSXXmaZClpJP998pyCmZyJUKlJroVzMVdC8M5DUObvUwRu8HZPIKE4F1q85sfGfwZnEbznF5Yjrv3Jtg_NsbK5D_E13BUS4gdjDScTl-wQHbQbDF_ya-fSlBGqsO6VJnttPOFsiAFkCwgQe9wCjioUoufKrep_jEtTvzJDl34Z0nMDZlENZwVx8gQ6nSTfPtjr41_r9ofs8I3SjQAWM0G_PQtmDANNqTaFXDuRg4eX_jdxUhYOUUT2fswTfpGerRTbJMcFGqba37JOHl9s-bLrRVnX-7LELnDizlXjcdfuJVcWyC4dVfjoh7A3pUGmd3kO-Cx84BI-aFDS6eVhdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=cgOSXXmaZClpJP998pyCmZyJUKlJroVzMVdC8M5DUObvUwRu8HZPIKE4F1q85sfGfwZnEbznF5Yjrv3Jtg_NsbK5D_E13BUS4gdjDScTl-wQHbQbDF_ya-fSlBGqsO6VJnttPOFsiAFkCwgQe9wCjioUoufKrep_jEtTvzJDl34Z0nMDZlENZwVx8gQ6nSTfPtjr41_r9ofs8I3SjQAWM0G_PQtmDANNqTaFXDuRg4eX_jdxUhYOUUT2fswTfpGerRTbJMcFGqba37JOHl9s-bLrRVnX-7LELnDizlXjcdfuJVcWyC4dVfjoh7A3pUGmd3kO-Cx84BI-aFDS6eVhdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=ALVgj6w_oHF-zzN0PPOs88WhTe29OSfI2EB4tKKmtOtAw2j6_bkMJXoFIvfxT6Sqh2iqpG6l9NMIuOaRI87YNQHX-bxXTmVH21l26XM2sm3CrQgjwSdtywz0B7P4nFfxGL5sdR30vDWdjUCZuJU9vZgO6lNhHaHYa7IUhe7wuykUmzdC-KRmsQK2Mv7TItD9m9pddZ9c-zrQCGM3yAOQaNvOUgmqoigmnZH5ycEM1e2bruTbNP2vXwzVJ8Pz1Y6Ij6qvVRV0CNGJBbkhY0faF79UPLBBIZf9ZWx8iD0M46ngSFMS8C3fQr0JqEtqNVs965U3ltJI1oy2X-6nJKYycaKP4n-i6imo645JDKqYS5LaX1SoTHoAThtWUs4Kop3Q7JoLiU5Xot3F4XAL1jCNIzttNakb_N6KMBySO6EONAZLvWVEt8mu5KTITfKs0m78D5h2R262R_acOsrM5rwLjwCxkykb_Z11cNlEum5v-Hfu9l8GttS5IKPrglZXFd4Fx3j9GBvNZ_OLKZpZamZ5mylrWpILhDzvuOQtwicXd5L8j6qpb02CwDGJZ9OqeSr4iiNqNldNtZ6LI4u2ITukgMJh2OGsQPa75ndJwIh8LEQLSYE245pDuF7dT6eM412JhdBK0170KNfkR_FEUOyD_ZiSOTs6a46v_a8YJHC8a1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=ALVgj6w_oHF-zzN0PPOs88WhTe29OSfI2EB4tKKmtOtAw2j6_bkMJXoFIvfxT6Sqh2iqpG6l9NMIuOaRI87YNQHX-bxXTmVH21l26XM2sm3CrQgjwSdtywz0B7P4nFfxGL5sdR30vDWdjUCZuJU9vZgO6lNhHaHYa7IUhe7wuykUmzdC-KRmsQK2Mv7TItD9m9pddZ9c-zrQCGM3yAOQaNvOUgmqoigmnZH5ycEM1e2bruTbNP2vXwzVJ8Pz1Y6Ij6qvVRV0CNGJBbkhY0faF79UPLBBIZf9ZWx8iD0M46ngSFMS8C3fQr0JqEtqNVs965U3ltJI1oy2X-6nJKYycaKP4n-i6imo645JDKqYS5LaX1SoTHoAThtWUs4Kop3Q7JoLiU5Xot3F4XAL1jCNIzttNakb_N6KMBySO6EONAZLvWVEt8mu5KTITfKs0m78D5h2R262R_acOsrM5rwLjwCxkykb_Z11cNlEum5v-Hfu9l8GttS5IKPrglZXFd4Fx3j9GBvNZ_OLKZpZamZ5mylrWpILhDzvuOQtwicXd5L8j6qpb02CwDGJZ9OqeSr4iiNqNldNtZ6LI4u2ITukgMJh2OGsQPa75ndJwIh8LEQLSYE245pDuF7dT6eM412JhdBK0170KNfkR_FEUOyD_ZiSOTs6a46v_a8YJHC8a1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYqTlBprcr90JZT2Q1kbigjlDvZNSIzM088kt9maKO0t3I-WcOGBgjI6Xur-4aHpfJkEdoppTo15GF8lbAUMB6bJSzFbIz9tIvNLOL9CYHcD1YB0AMLGNDlSIg1SbU55F-FBE5HFnvfKP1MSw_p-1InqwbonUJHn4CBFeBBps7Tb9WydEan_3xGdnbISAmGgM4A9R0sAcQgWUqDJLxI7prOPfQE2GLSz1n0j0RWY0Unyaqm0pNYJLv4GVPCFjSAY8IBb4a3F4d_oLpRE-NkOTsyGx6C_veyRtwSZw3x0FjMLbbTYmeEEjVXevAzPt0PYMmxBHUIenuXdUxWk_uybaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzQaSJj_fll7_oB69aDQc9PaF2rRUBNYq7_lVBE4GF4WfytWweYAhE6ZmkihzYOFDjIhmb3HB2IIblrj2OOmE1b9a21WyjFmGu9ndZVYF9e8eBOm7AGtwdcaquU5Nhdwg7iDPSHCCIhcji8Yz3gXtIG97P1--ud_xkkrTpPDi0YUCiwB1ROjFDyvOT90MBCUTMoCJE9EA9pbd0K_-HtNDulpEMZj078QrmgVia5nUnyoiKLICLBtVJLNZqVeFDOnUPD8SKLlE91teJo3OYJYBSeRZHXZ3s30bmu6K_VVS33Kgl8zFXwLD0ch8coajvGNtB4m3W5fZ33OUHXRCR0Xdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qj2iI9VDHF0fDSqVva67DSKzaPRJqq9UpC5pYWBoKucwbDfTRkOsYRgT-cmObO6li9H3SgZdccDGmYxCYtcpZW7TBcPGGlhP9KuorTfd3nEb-i2rb7rLAqUCkjkQxpAgKMnpOh6i3nTkbj3XHjaMuv6xsDoS_6AQlFLkliqYlxXWjBzjYXhvixt6f3130K_DY2_o_wMnu1KTpFB5gV2zRI9qUMd1XNrGLzeFYtPgGsqcuyISDEJy5of9wPmj147O132N8zU1LNc6j-Q6L4QJpClf1X4r9PrBikRg5Yfjdw6D_5en9XPdijP9dq4kFiWkX1Y6IKqGdvvl6qBjGdNasA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=rixGmZHtwNpQrzqlvObThQmRL8iEVOmuElpULXaE58CjKZyP1cIaC8-yMdgzkGVUkYZ7GAqK_Jf8WW2OFZZYxD3_vcdINkp6WRhbG7vpGG7JgnJpGZuoj7oYMSYpgNwCbAYumMAgNXHj7Z75XuoqXkL-PvG5MpFuKNU547nPc3OyIf8DMLqYV9Ys8nlN8YT4bZ0LNjzrf_3PzibFyJ5PAUWaBXAD53oB5CbE9f_FTactLdkruznBOux3-ET0H_EJDqS49X9TSZ4rVsv-G0xgy1LoVpicwn3r47qfYjKhFGIN0hoyd0WjR3d-hN0aMQ05t6S3UeWQ6jREfPvdd_eUzYGR4SIAPyiYzEKLQ0J6uZ0BVrHfJ0Klmvfzp3iJ6iCD8qHHp5jkXl9mTCxufJCXwbaGR4fE3wf6npJ1mEsXpMkbsThV6nofJc_LyzqG16I8I5Wywdq_sUkc9hU9c5NYJS2SYFEryL2pL6zobAeTmBgJfaIPJUU8p031P4V7vJ89RT_s1yFyYiywZBw7S0Z2qyrYYAaWnNLCAUfOJ7a8rWythdwRAQa9IDYejEKuDCaeRXyqPhHgFH9kNEB19K1TgHRwDxNiIp0DsWjGZfyovdYn4RX3w8DujLFWig-B_zHon7RRswwf8NcTrcCUD-yvEOrwoPCSffYfHpD4P-Vorbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=rixGmZHtwNpQrzqlvObThQmRL8iEVOmuElpULXaE58CjKZyP1cIaC8-yMdgzkGVUkYZ7GAqK_Jf8WW2OFZZYxD3_vcdINkp6WRhbG7vpGG7JgnJpGZuoj7oYMSYpgNwCbAYumMAgNXHj7Z75XuoqXkL-PvG5MpFuKNU547nPc3OyIf8DMLqYV9Ys8nlN8YT4bZ0LNjzrf_3PzibFyJ5PAUWaBXAD53oB5CbE9f_FTactLdkruznBOux3-ET0H_EJDqS49X9TSZ4rVsv-G0xgy1LoVpicwn3r47qfYjKhFGIN0hoyd0WjR3d-hN0aMQ05t6S3UeWQ6jREfPvdd_eUzYGR4SIAPyiYzEKLQ0J6uZ0BVrHfJ0Klmvfzp3iJ6iCD8qHHp5jkXl9mTCxufJCXwbaGR4fE3wf6npJ1mEsXpMkbsThV6nofJc_LyzqG16I8I5Wywdq_sUkc9hU9c5NYJS2SYFEryL2pL6zobAeTmBgJfaIPJUU8p031P4V7vJ89RT_s1yFyYiywZBw7S0Z2qyrYYAaWnNLCAUfOJ7a8rWythdwRAQa9IDYejEKuDCaeRXyqPhHgFH9kNEB19K1TgHRwDxNiIp0DsWjGZfyovdYn4RX3w8DujLFWig-B_zHon7RRswwf8NcTrcCUD-yvEOrwoPCSffYfHpD4P-Vorbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=PlncDGcUn8-CRaM_DjZl6WzmV5EClWoxImga0JL0rS7zoX4CeB45eoMYRs1jLa_kRmsVZxpRx0OO-y0RKB6BGbXyCqdYiM4Icmga1919qaf7IRKJ009fP3FpupWOjounMLHZGJFJQKaj0x0G3e2YfS07vx09VXdeX7VqdwFl8UZ3akQpJHEUYsBnjGQNXe7xX41ixPElewYdIeex0Pc9u-xF9ezLJiKwIH-DcsoD3URnuNau9Uer8dFzaWsfQ04Mv_jWchr02okRgWTqld36owxeGzuVwdmT9zO2slCCfS2UXOXrYmSdbicHmAG2koSbwKiWiA7ritoztz6QhTniTwTI81xDQVDKwY5sVmicylNzlgKlW3ZMdnDa-lOxrezlu0WVB53OuFOne62z1KzXLTwi020UlhLMhqEAaX2tQOTYCoJKgmFRNgfy0q_TF1MrwVt6-7Zw4jS07FxDbsgmVHjbPrN5CvvuwHnsf0qMm2gxY34pcvy46nD28yhr7VGnyFIztXcIVCKl9Y-uhgrjozI06Hmo-4K6xLYKP88UMj9slDW8NlIQpC9XKvtK9WRzwgvEKu56wa0EVRA_Adfv6Hp7J6hLEPykQTJyas0msYpDfNjjEV5d_TyzWqIZ6mAfQidCNec6eG0bAirjC0icKKkoiWe4Z8nBS4Qsz2Kr2uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=PlncDGcUn8-CRaM_DjZl6WzmV5EClWoxImga0JL0rS7zoX4CeB45eoMYRs1jLa_kRmsVZxpRx0OO-y0RKB6BGbXyCqdYiM4Icmga1919qaf7IRKJ009fP3FpupWOjounMLHZGJFJQKaj0x0G3e2YfS07vx09VXdeX7VqdwFl8UZ3akQpJHEUYsBnjGQNXe7xX41ixPElewYdIeex0Pc9u-xF9ezLJiKwIH-DcsoD3URnuNau9Uer8dFzaWsfQ04Mv_jWchr02okRgWTqld36owxeGzuVwdmT9zO2slCCfS2UXOXrYmSdbicHmAG2koSbwKiWiA7ritoztz6QhTniTwTI81xDQVDKwY5sVmicylNzlgKlW3ZMdnDa-lOxrezlu0WVB53OuFOne62z1KzXLTwi020UlhLMhqEAaX2tQOTYCoJKgmFRNgfy0q_TF1MrwVt6-7Zw4jS07FxDbsgmVHjbPrN5CvvuwHnsf0qMm2gxY34pcvy46nD28yhr7VGnyFIztXcIVCKl9Y-uhgrjozI06Hmo-4K6xLYKP88UMj9slDW8NlIQpC9XKvtK9WRzwgvEKu56wa0EVRA_Adfv6Hp7J6hLEPykQTJyas0msYpDfNjjEV5d_TyzWqIZ6mAfQidCNec6eG0bAirjC0icKKkoiWe4Z8nBS4Qsz2Kr2uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HQ0NEnKGbi9CqVBW1c-_HuCXRno6PVqKWqGJB09yx0pJUek9wotUMQSXRK17YzOiuaitfvDatKzsO7PqT_P-tse3MVfEZ2bX-jb9kY4rAePkVyf5P8Olr0lv831NlZ-6h99lBhQW46fsTKjVSVCQN7sKsVZD4oxenjfjDFYgVkESU_LAS21GmbnJbeP1Xo61XtSx6P-6047tPCmnxyGx6jZfPZ6OzEH5yRoDAQHV37umkYzuVfjcc7A2JMJ1zKFs62ESzn5D3G985LP6_IviW_ZzaYApP_IGQqpEYiJMu25D3do9zoorbI6wI_g3BYj1IG37UR255S-U3w4KnyagNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB4zOQMFXyUkdLYUCSzXcZiLMX3Y-ZTfju3Kzs5n12BQB7rR1czpFSj5VNHfVNisXGtWd2xnQBdE08dkAfbr2ZT0lCwaY7MlMi5lH2q2xetArjulbfOc8xWrgAsSoLJZ31_PWhjtvERRGq8e3SZp9XhlLVbcokC8gm2Te1rUY0ENCiVFEaP9zxb3fPzahgayXwX49knMlbblppr_YKscDrGJKx-hMkOoPiNKchUR-4oreEf6igr5S2GMcFL2NUw1Ocm4xUna2jHDUvR_weyPz1ucr0lssVezCaY5JrD03nYm7P9I7hJepJML9J5ZIfRV_l0b1Oy9NM5JLdqT1gTCoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=vqjPFaRRtFFz4HPxfUV3PkVVtWpHAKYsSbwHsCppHt1OI6tMDGZeLtkanNg29N0fDG1LAQLehi9MoaWHMXLWOo0JSvb2NgjE3q-76Z_ryj_1lcWOtLGUSeNYq1nN1ZGuG14p4TeSAYYDe6ZdMJaNH5GVVoXLbq8Pyty3Ew5dupMpQg_SL_9cTXaYPBzrv52QTQRRtcUwbmKRzEwKDgab2asaJPjHOjASlORDZOJBcseqnLoF2NxWj0sfHDCnmcl_80wyaEfzt6Tmi5YI1JQz3xplFgi4QfpAej2CNbFPEGdIt7MkLVdoluEJB-zMY1f27mdQEsRWwIj3aBcvP4u28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=vqjPFaRRtFFz4HPxfUV3PkVVtWpHAKYsSbwHsCppHt1OI6tMDGZeLtkanNg29N0fDG1LAQLehi9MoaWHMXLWOo0JSvb2NgjE3q-76Z_ryj_1lcWOtLGUSeNYq1nN1ZGuG14p4TeSAYYDe6ZdMJaNH5GVVoXLbq8Pyty3Ew5dupMpQg_SL_9cTXaYPBzrv52QTQRRtcUwbmKRzEwKDgab2asaJPjHOjASlORDZOJBcseqnLoF2NxWj0sfHDCnmcl_80wyaEfzt6Tmi5YI1JQz3xplFgi4QfpAej2CNbFPEGdIt7MkLVdoluEJB-zMY1f27mdQEsRWwIj3aBcvP4u28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o7ED19Uxiw87KJtVLoRnHWDrOnxTkXdOhOO_dw0CG8GxFaFCiuZCQ953Ke9dV1MjnxnRmJ5KAoL9yTryLUidvcbtp2F7N5-fq_7JwjC2H-X2AaiQK0t01qBNWqvBz4pl0QvqEks0sXch10VxpfGHfr_qgTP-ggwLMooO50wm6O04w0G3ZgDgUAqReNKb3zUPV9MmnF-neGortOzz2-q6MdqcMVF9FSvg2GXHW9dKcXcLltj_nruWqvOlaqG3ALpPviOXYcfyouNKgrvH8SeEzMdUCn75TNjMo1TtEHQbtxl57iXENT4Y_XRLtZ3aKIt9DeE2IKcJm57mgmR58eOthQ.jpg" alt="photo" loading="lazy"/></div>
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
