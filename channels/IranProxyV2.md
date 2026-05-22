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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 16:07:16</div>
<hr>

<div class="tg-post" id="msg-8474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دارم یسری تنظیماتی رو سرور ایجاد میکنم، بعدش نتیجه رو خودتون خواهید دید صبور باشین، چنددقیقه نتیجشو بهتون اعلام میکنم
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/IranProxyV2/8474" target="_blank">📅 14:15 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2uqPrJ5c7WMP2UmByuv5i1Il_SvZSsZ9uuPNo4Z-uz3sAQv9jRydHfdJqt6T1FFDhpvMXDaH4BOUF70GxPuyhky0oQd9JhCJPCKCG_Ekdm4PexvJABMvydCsxBiFeTBCxUTDr-dQ9W3Floq5II0T--3mY4lOLFQEMsSIF7mbT255Xh3uhPrWXECnNRZF8LXEKwAwftfojRXkWeIyxhvZi-fAZSSb01zwPHH05F2GaDiFGYMctZRYBjxy-mjgxDbGwW1MDFMV6VMuFj2XpyUJn3lt6y5Y2Uho4hw4-ijsDH2ao_E502z_Oj3g65tHVHObimk-34B4gjtJZPgf6ppkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRwGb_NMq-HCc3K2lYwJ5w-qq2K-GXFZXPynLCV1MC0sxLhCOCLFa5Fuj40rbaXwtTrpsN7SR-qSNbfAfAsaqtcEFAAnameRyHNh2BcvM4bIvweyJCI6tJbVgU2dX_dEQjFVmt8gaVuAsFu7-Kj3YFaYmbRmzrpU0NmUr8YMZMUhjvmNY2BhsFBIPnc1YvVLZ0heUsRta7kDTVbNeX7vjAa2-xdnoeyMEuwKnJtVJHZEqlkYVhdiUSCMGBeoAUwAEuCFCjGrTXdqyrHhzlh_f_O9cDuTt7ZDXFtNCfJFOA-2fqekv4f91VAHzUsG47x2i1j-KqRY48Qi0EhDjeFvhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MilC0Tgd3UWvNXqUaN4KnBaMqnB6mFwxpWrtraJdt6ubIG-QP8cBvKFzH6qZ0dhHEojW8P5BUXwNc4KoJRYI9z2HFM1vETvJi75fc9Cfvq-VDR2SzqDjeyscfH4e2wuOsa4rhyrPhdSAQ_OcYpN-FLruIAdjDHsG0A-3m_xiavN1Jp_0dtM5i6kCqJJP-noviKQdPetPKQQ9pZ2dLvCMkbdoYTm6guFyxeiqI2fhhkSlysc25fNZO83nfeCgQRJi1gemiPpYt7tZOtsn9UKB6NeifsWRkkyMT777v1DImZ1u9lfUWitE0OboAZV8cbaf7Yi-IENI8jEc9u7b7d-iJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LknYST7YzSggy765uWkUe92Vk_LrMCdkjxlw-WT18cROFVgtbW3sPPZgeohNlOA5OQ7BTRMwZBoFMOxDf4LPkf9tHfctTbFLHDXvO817zfZLiDlBO8jeVv4tAc6YIMSYv_o66O5YK2oVOCTqP1XQuj5gvuVUOcj5mcQM9an8mlTYgZQyZ-jyIrvsdyf4FUrmlcYS1VO1LB6yDtkNNP9DEQvxrdWhsUIp0UPYJyg1iPUbpnonfkCadiFOx7yN8zniJ7FDZPDhZPXIBXTNnqgeqltK5r1UV-LN9usjoNaVKZRm8KznVJ2mKsfbLdcYFp4MeV5Q035_MmuNGIuGmwEhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=dKfI4ag-LdI-Cz8rNiqlfTOPYaHfCPhsB5g-rWl73MwbgrWnja3OFnX5FYqqn3CVcdhcMnhCB8qH3NYFKjWdCCMPjV3QouGQVdSfzIF2xGY0rkcHRk06x8Nn60zEjWhGfUny8DiDRBlSAcRNatjJSDVKvD0EZMvxFdVgDAqoV7T2_jxMWiSSkg1L1ZNvIclHlGtmEvknrT8CFPbEaUOlfCHhefK9JyzMDBT3CdKIWI9FypsliJNIqwSIBm85oCAA6pZCD-tmag1SvbclWkhTiZfnLeQn6fFxVCvRiyp08JTLYFfY53D-bs96oWGg-oQ__z_NMHhZZz8RcQZWoysHhWGUJICWLNI9YguK3KKdbAeEEw9K0fKBZpt_xf31Wen99oDikt_ELdjesgE-K_hGPDWcTzdGduZhZSN_-3fSg_U4T-lkt8zyCaFVDl0dTjQ4__aP6aM_q-p93SpUoKD9tpzd87stAtB6yPSRTk7X5xPId0wJ3zkxHFz0jGgbVaKnTzAqVHj9fowgQHGctfLSjnG68QBwktJs6tUbRUxzbg2pI0g3aoCbz9pv2KnB8vqvvbd6d1daWquEjT1VR-HgGosbOHkEqdNMmLyFyeb7qMQ1h27RtE6J-E7PixU_VzeSFYEkc2OQaSGqTKeuh0ALzCReDcze-BD1oNG75DgpUkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=dKfI4ag-LdI-Cz8rNiqlfTOPYaHfCPhsB5g-rWl73MwbgrWnja3OFnX5FYqqn3CVcdhcMnhCB8qH3NYFKjWdCCMPjV3QouGQVdSfzIF2xGY0rkcHRk06x8Nn60zEjWhGfUny8DiDRBlSAcRNatjJSDVKvD0EZMvxFdVgDAqoV7T2_jxMWiSSkg1L1ZNvIclHlGtmEvknrT8CFPbEaUOlfCHhefK9JyzMDBT3CdKIWI9FypsliJNIqwSIBm85oCAA6pZCD-tmag1SvbclWkhTiZfnLeQn6fFxVCvRiyp08JTLYFfY53D-bs96oWGg-oQ__z_NMHhZZz8RcQZWoysHhWGUJICWLNI9YguK3KKdbAeEEw9K0fKBZpt_xf31Wen99oDikt_ELdjesgE-K_hGPDWcTzdGduZhZSN_-3fSg_U4T-lkt8zyCaFVDl0dTjQ4__aP6aM_q-p93SpUoKD9tpzd87stAtB6yPSRTk7X5xPId0wJ3zkxHFz0jGgbVaKnTzAqVHj9fowgQHGctfLSjnG68QBwktJs6tUbRUxzbg2pI0g3aoCbz9pv2KnB8vqvvbd6d1daWquEjT1VR-HgGosbOHkEqdNMmLyFyeb7qMQ1h27RtE6J-E7PixU_VzeSFYEkc2OQaSGqTKeuh0ALzCReDcze-BD1oNG75DgpUkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-ot5UaTaEEvWCp_0CIp0uRlX0ry8rg4w-q5eHzyJkJlWVBYGhTNXw2a7RfkWNld4a-7sVHKoZ1dy06ilqrvVAWH4cw5wCWomynlXzL1yyRzakJMCm0E_ydXp07_sx9gnP3nYYYgIkg4fI1I1xrR7NKylu6kQB0ea4Pkk1gDWjkksK5OfomcrgLwJkHiUo1tQZN2zvP9bnPZkP86x-3Hb8DLWqzpOSkBjB5rWpRl7z41Ui6jtDDb4fY0GQ03h9Oo3cewK7oDPFitAFipdCu5K6YQS5a72hrz4aE1ribjDSc7BsXCIbW0Bl8zS2M5FljVr710-9tgDLhiFhVUIMPEkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOj5BH-0YWkCVXlgtMMkRFXMsgUGmDTKIShEAMi45EjcVPDi6lRJ0QnjVPDjZzZ52eAt8yuDonWOpYOkH7uDzZ-3bc3-5-yWA15ZReoegSZNjP1QhAqly_AcueKJ2h_T6RpESSR8X8VPXQXdXmtlF8TGj-Uo_5fIEkxiL81jQRtbyltmJ1PuumzbDABjIzVrwv0eB13BQGI_7ULKoJujA-gcbnDdnlg9rqkT7Li5R5sxDM8mHeIRHaqZx8WXG6DiqCIvp8sHPc0ohmZidQTs8JlCyTt_Un24MIKyl68N2AUdE2YuvPu8F27KnZX5H2x6OX8U4coWxeIiuQ20C8-Zwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku6yBpZfmSzlzGoVuvFQgYTU8bFzsuUcGtc1aeKZSPMJx9EvWsNt2cy9QGXneCgy2sSHU_CmKnn1UG7W3n0RbqsDCDPC4YOdYnBjGAB9XGqd0kIk5KtI-EbsTSawdJHL_DGY_aU_CrKvXSdVVUAdPv5tEJPneIE_58srp-dBPysh8YzOgeqM2Ry5I5IRrCLlmyauxqsiuhFCQKjW-iB_yDQK-fkKc3a9N0ZGBviBI0TtzugleWAYca9k4xffuVZ8GxlLPWBglxGlynT-IQHgpH4-ir0giBZ8A04oxrzfBAmqdpirarOpj0CWjAzZoSdk9_mTkQzw5PqWHSeQ0-ESuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=rlmnwSkAoY8uRJFGGkheGvpkc2YYyvaBd4gjHwJEyCIAt-rS9soZ_0imtyk-Sr0BxXAIXNnMw8FEUpZ2aqpJC6DcjEE2b3VNQkESPHs2m4FezxCmLNpL_3YG5cTACKqTi1IvrNkdl2TQF9aVdyaOn29Q_8ghflpLnAQWCC9ce034cMIC4SnS6zE61o73IL8iX3dUYbWXvnbuwx6KZUNWLkcXg-c6Nf33JIB7Sng0CIU16dqVwe7tdKglALJ6IC_VYbST4MzBaozcliNKvdgfxdU6KOeU9I-F1061htv7MmW3h6mLydcnCozVhqXGZ_gdDaFb-dSDVeSk_y-S78UfBYdzG3hfC1YgtjQMCNrlhv68vb7X_phZX1JeWC7Zluem8cIq2D02PpFZ3s7L06K1E84E7FNxCnjnrLXGGbQdaPA_lDYlZlAxxRVFxAFG_FszZSep2vIbfszS7aeIXUPVsE7nMJ1xOoUvfjxtufrff3DfFJM9Del4sxzGVFXRw7gN2WsQ7fdUCimQHIzmLmbQ_FxIdEytTHxQ4zzO5qzY64nSHHdPRchVE2EvddHN4XMr01-I0DBD9R2gLMiw4lVTYd2bOgFlWF2lHX7bXHtbzYgXaV3wihQDQnD1r4-uf3ybeuyxtDQ1TSoKzY9M2WsmcpXVp0dW6SP3KS6YiOx4WUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=rlmnwSkAoY8uRJFGGkheGvpkc2YYyvaBd4gjHwJEyCIAt-rS9soZ_0imtyk-Sr0BxXAIXNnMw8FEUpZ2aqpJC6DcjEE2b3VNQkESPHs2m4FezxCmLNpL_3YG5cTACKqTi1IvrNkdl2TQF9aVdyaOn29Q_8ghflpLnAQWCC9ce034cMIC4SnS6zE61o73IL8iX3dUYbWXvnbuwx6KZUNWLkcXg-c6Nf33JIB7Sng0CIU16dqVwe7tdKglALJ6IC_VYbST4MzBaozcliNKvdgfxdU6KOeU9I-F1061htv7MmW3h6mLydcnCozVhqXGZ_gdDaFb-dSDVeSk_y-S78UfBYdzG3hfC1YgtjQMCNrlhv68vb7X_phZX1JeWC7Zluem8cIq2D02PpFZ3s7L06K1E84E7FNxCnjnrLXGGbQdaPA_lDYlZlAxxRVFxAFG_FszZSep2vIbfszS7aeIXUPVsE7nMJ1xOoUvfjxtufrff3DfFJM9Del4sxzGVFXRw7gN2WsQ7fdUCimQHIzmLmbQ_FxIdEytTHxQ4zzO5qzY64nSHHdPRchVE2EvddHN4XMr01-I0DBD9R2gLMiw4lVTYd2bOgFlWF2lHX7bXHtbzYgXaV3wihQDQnD1r4-uf3ybeuyxtDQ1TSoKzY9M2WsmcpXVp0dW6SP3KS6YiOx4WUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=AvCewqYLryWUlCE8pdFYxZ26bFaAypkW82c-jEwcDxRMluAHdeA1QgxBLQdY_ZKTBJKyWFOy7yWpoQffurVyf1spMllJ6nUWMr7YowCj48RtMxPdBpfx0iso_ceDcWS3L3AmeHWjYSsA0hg29rJj1FT4NeijAXoyxq4scvq_nZXonaijU_DP0imu7KDT8MBiUVFU7VlpAeQB3uQUev4yZ9QJnHH-31kNn-HGwzMZIQMzX1tV6i2JQ2Y7r2uMDByI37Ei1e92nr5LadQapSgaLKIxqr2TFojzp-T6XawuXsz7JyWVgISj4UAfLqyBPuNxA-0Y3jKboACMlWrVOaM_jzA4IKm3lsHpcPwznVXfqVTWqYuNvsEckdQ-nci_qRixgD1LKxuamKS7yGQ2elTmQGm0pL5ZHwSDfXtxjZYox0V1JtmXGMjS5-Ir4ISSsa-TZe3oxwR399VcsyCYB2qWiP_65FKfb6TfNyB3WDVAAqQG-Rkr4b-aaVDbPIKH7J0EJQ_BdjFN9yX8ixDVkv0z3uUgKhqx3QV7fVgPCZBJ4lc6VIatLghumbmASDzNUKre2twZhwCB3OUe1UAGdvT7UF2DrTTWXchcQFLHJxW0Rou1fMV1_FjwRBevE-E0GiRVtqgOTZc2LAzuckoblueKgKQBiskFaCcyxIcfZQpg-qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=AvCewqYLryWUlCE8pdFYxZ26bFaAypkW82c-jEwcDxRMluAHdeA1QgxBLQdY_ZKTBJKyWFOy7yWpoQffurVyf1spMllJ6nUWMr7YowCj48RtMxPdBpfx0iso_ceDcWS3L3AmeHWjYSsA0hg29rJj1FT4NeijAXoyxq4scvq_nZXonaijU_DP0imu7KDT8MBiUVFU7VlpAeQB3uQUev4yZ9QJnHH-31kNn-HGwzMZIQMzX1tV6i2JQ2Y7r2uMDByI37Ei1e92nr5LadQapSgaLKIxqr2TFojzp-T6XawuXsz7JyWVgISj4UAfLqyBPuNxA-0Y3jKboACMlWrVOaM_jzA4IKm3lsHpcPwznVXfqVTWqYuNvsEckdQ-nci_qRixgD1LKxuamKS7yGQ2elTmQGm0pL5ZHwSDfXtxjZYox0V1JtmXGMjS5-Ir4ISSsa-TZe3oxwR399VcsyCYB2qWiP_65FKfb6TfNyB3WDVAAqQG-Rkr4b-aaVDbPIKH7J0EJQ_BdjFN9yX8ixDVkv0z3uUgKhqx3QV7fVgPCZBJ4lc6VIatLghumbmASDzNUKre2twZhwCB3OUe1UAGdvT7UF2DrTTWXchcQFLHJxW0Rou1fMV1_FjwRBevE-E0GiRVtqgOTZc2LAzuckoblueKgKQBiskFaCcyxIcfZQpg-qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2uBeTrfphshKdSURygNw3ySiJ7ZSyPQjytlgwO3O8FLrXPRuGVzENg2wm5w6dPeiL8GiSve4Bf9uKmQAFvrL2s_o2rK_tZnC38zDM3au23ooi9PH087h4GMBMTJZ4mOIBJY-1Tbbht9iBS8XX-uAsxtDMxr7N7SINzTD5NOkvPblTvkhJD2bp40fmM4bUflzB7ajihZyB0tdPRRTbNk4JSKGWzRmItu-62IQdv6W-X6hGGZa1rZY3WVM9fUmu0ixmT-jEszdzcpg4jngRoZ_kwaTkCrweqQHXpfM4KD2DOYMgB68Y5wMj-sWgdnw53UOSLnyHkHHX_Xw6YlAY5imw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=HdFCrN5qcZBWDAwLpx3ES2thcwgkMo6t7eNxk2sGLk2uxPSCmL4doRCXbsQBYVw8tn7A6xFuvFBd9OuCsoEuRp2jsLswVmAH-0tFySbv1ySN7bhJKzKbhM2LCwPH0x6l9Pv09gfthU9iuW17aqial5oHC5RbdyxrxD3Hvy_p4AIhMlQpSVzrQzRgQFcEQDYUHc-l2ovpciS0X-hJCpftdEiEb5xHyPljAV0KIZIDR9mPPDx-izfvhdpkfeQSmb1sLp_vj5vELENaii9XCB_zbFvumUrPDFUKNUYds4zlpKfVbvyF3RqEIVzdsLrKB6N2FvRAhiEvcBGtK-wqPbi1UI7K7t_9J6HcwAQ-43j0r8fg77_klfqeo0ESAF8pVl2Rvl679klJn-m2mxC6L-vctnd8x-hEC_QC1WiQWFX-Ft5xar55waIsiVPR6D1FvSvMThsegQm6fzZw71v35J3c-bo13Av06FlAtkyt35NIWFVDj1fcyLT72ZkDjMJcV3mKpF9Ky8LbWUybd3iT1NxdMfZXRQJcxtvl4piwbJUb-Ixs_ZFkg0eih09PqiVo0Cql70V8v6j5WVxL1_9iOwEiYtP4Ky70zJ2N7SeexeUoYv41VLaSLaA1ONtRdUfqTAqLB9-1MPQLInHKeqZQ7OfNteYWU1s90o75iBc7_cz1myQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=HdFCrN5qcZBWDAwLpx3ES2thcwgkMo6t7eNxk2sGLk2uxPSCmL4doRCXbsQBYVw8tn7A6xFuvFBd9OuCsoEuRp2jsLswVmAH-0tFySbv1ySN7bhJKzKbhM2LCwPH0x6l9Pv09gfthU9iuW17aqial5oHC5RbdyxrxD3Hvy_p4AIhMlQpSVzrQzRgQFcEQDYUHc-l2ovpciS0X-hJCpftdEiEb5xHyPljAV0KIZIDR9mPPDx-izfvhdpkfeQSmb1sLp_vj5vELENaii9XCB_zbFvumUrPDFUKNUYds4zlpKfVbvyF3RqEIVzdsLrKB6N2FvRAhiEvcBGtK-wqPbi1UI7K7t_9J6HcwAQ-43j0r8fg77_klfqeo0ESAF8pVl2Rvl679klJn-m2mxC6L-vctnd8x-hEC_QC1WiQWFX-Ft5xar55waIsiVPR6D1FvSvMThsegQm6fzZw71v35J3c-bo13Av06FlAtkyt35NIWFVDj1fcyLT72ZkDjMJcV3mKpF9Ky8LbWUybd3iT1NxdMfZXRQJcxtvl4piwbJUb-Ixs_ZFkg0eih09PqiVo0Cql70V8v6j5WVxL1_9iOwEiYtP4Ky70zJ2N7SeexeUoYv41VLaSLaA1ONtRdUfqTAqLB9-1MPQLInHKeqZQ7OfNteYWU1s90o75iBc7_cz1myQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EswDxhoKidnMmlU7Ua2aIxyc48-xmhxF_wSr-sRrrYw5HRQg_0NRoEKxhcR8rWAIy7rv8p27SYO9-6884lvAlqG7qHdiLsLG3F5GEt5uHMyMX80kbve4HTOFIpg_4JNt9C1H9zBDkzqOQBsmCnabOWyevVE9CU3YmljWupd-R14i5xkyeVl_SBEzUk4N72T8dM6CDqa5C99p5KvwzbBaIOHYwnhpwDShlxheHC_JhEJPWogzsfgMdg-M_eMpuR3n1Tk7UvxNb0DGU5V1K44w9QZHrhRs41lgdYE-3Qe5HhpkxC9I_u-aaVLNxlYWIfNTWS2oxHPda4gC6gIu246OXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIg6RJcz9i0ILfZjO_gmpL64DPWYLbsOBeKEjllxwpVZ2UA6D9h6hJhezcD69Q9WdJN8z9AXhAqY1ULsW51HpukckmOBPrUt4l498etrS8OyOF-Q9VzOlsOoXYCdHribGgDmCR1WqGJss44q9pAWsD_XP9p2Cco5jMyOWBd0jSnBsZigGlxQxlCcxGY1HaPim5TrkQYtIYCcTR95FjU7nKwAaoo-PU8tIQ2b2jR3IFzHNsLgz_4pvRJh4ybwM7ryx-06x7He0qcmQQI62FM5hzRtLOfT9X9qbvYU7R8Pl1KJ77RwA9jg0XE4BuUh_NCUKUop_3IWC2Ej0asCO4sV6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=eKLu-revJEYzEYU_HoxUaTxoxJb7SLv_lleccbxxRC_dEs9emNFBfI6p_ZoYhpuEhiAV6Zjup9jZ5JOIf4shZe4-W53AJrkcOk5e7hHP1oF2yttleAH5lImjJwJuQRsE7hchD5jM4rFeMfZKIzLcyn1JFVT8x2_ysibTZ14p2-GSGS0cOZ3cJ8p9p5YQEruAnxqfKluffzPRhgl36Pc3YAJN04HZMP9m88mTfa8PX2LUteta47lEkfBzodFpJeYR9Nym2WPZCyhy1pFrAKu0A9Q24aUyGEn0yTtlMg4nvLAE7v6fS0vhqRvoITS6Rodyo-0xIkVArDLH36cGn0AELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=eKLu-revJEYzEYU_HoxUaTxoxJb7SLv_lleccbxxRC_dEs9emNFBfI6p_ZoYhpuEhiAV6Zjup9jZ5JOIf4shZe4-W53AJrkcOk5e7hHP1oF2yttleAH5lImjJwJuQRsE7hchD5jM4rFeMfZKIzLcyn1JFVT8x2_ysibTZ14p2-GSGS0cOZ3cJ8p9p5YQEruAnxqfKluffzPRhgl36Pc3YAJN04HZMP9m88mTfa8PX2LUteta47lEkfBzodFpJeYR9Nym2WPZCyhy1pFrAKu0A9Q24aUyGEn0yTtlMg4nvLAE7v6fS0vhqRvoITS6Rodyo-0xIkVArDLH36cGn0AELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhVXSpSNEO9fJ27JGm_8z2V6wSaAPOPVfIXxWCGeWIAkkWcyIUKURfAWOltrbmtjlzFlhea2LQ_3otICpYwo3ne29BcS0Yi-BzeC4VSoYPi8Fd8TlyMG0ERXnOoaWI9wX5vQ3E5C6Q8TxeLEDuQYObazWiTqLokmixClSU_wsfuFDACSd5Dcd5DLy1_A7pZF7aycPUx7ZpKET6n53VMziK6IqlEeP861AnTA05c-3nf6PgGR1WQgoL36XncqGtpFZwPw83XrKqbYKtT61p-MvfLA5aCXXTEAwEPdqQ0ljTNswU1mQKv_7XOLGM4ve17UrsuN1_nhV-6zbF5HepkdZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIV6UwL1g6QHUs6NqmEF-1cOlnJoScFSiWNvx8a_rhyVsndeQmSEf9_xthVmUv2pxFg3dVi3MYjf7uQH5dNIuBaY0L5OWDfok-pioyVlPZJdlPid69IbMies4vkduXJKwFrMftmVBK00GwWbTTw1K9-uiQ-0BAOfFo7J8Hl6hapuYLs2q_qlHJIu5yXDbn-J5_PugWMPhQKw9GWYN4xmaQMxGC4UXHQCq8h4bRI4sWFgSuwSbKVgSkWzHh1f2ccBbFgaYkNLgox8tfL41ymTYFtJTbC83HZxSTbjRDnLCIkFhux3fkPvbeYgflJHNaomQI7DECdq65qH8y0WqJR-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4QhLgnMckM94SprDotFMaCWdFHxZYS-rBQzvvkIdHbd0HxIMrGprTIaii5UGzrBXwUgoh_Ku1OGMAXwIvy2QaJrChXsffW3NGEt6jtA_eGd8rqDXA_v0PHTu8_nOCcIUFuKD26V1lXARe-D2C485g-27e6MU-EQZ92OhAIx4wHrtaP1gDcaHE2wAUqvh00Ye6LirhnnH1Pnb4autTQQjD0Lr_GY3Lhenvvmk9svA2F0NEXSTh37Utz9GBc-RAKF-aYS8lvr-IQ7K6kCb1pr61rspADBW9VQtY3APBTSDGvQ7hIZwUU7sdhdaJCFmiXDr9-rotFEFVb0KzEuzJDVsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=GHgoogeAUYPYu4QVXIiWnC0LT5-jvBHBQbAB7Ftd9vapZMm4qnUL-fMmOOFUjtDetDNymRzipoViAt0uqQhrcuGKC6zDamPCA0pw9AnrXSft96WxMz18lq_uIU-gzgf8hhjjkE8bNPU6yrDdU46rzmK2CeaA4rHZSfXkSS_IsScpqc96T3GtK4j8hksn_ViqkfXsY8T7jRMinry8ik6TD2Oat5E3rvbPUeqSIbGYZPiXjdC_gd8JZp5b7MzQlmR9bi8InRX-WyTKsbN9Ldw85IOvRBNRauFzBdmCnkDIlM6NEPzudwlF1pq_9X05lPMEpkTamGAnRKFcKLiVfuPJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=GHgoogeAUYPYu4QVXIiWnC0LT5-jvBHBQbAB7Ftd9vapZMm4qnUL-fMmOOFUjtDetDNymRzipoViAt0uqQhrcuGKC6zDamPCA0pw9AnrXSft96WxMz18lq_uIU-gzgf8hhjjkE8bNPU6yrDdU46rzmK2CeaA4rHZSfXkSS_IsScpqc96T3GtK4j8hksn_ViqkfXsY8T7jRMinry8ik6TD2Oat5E3rvbPUeqSIbGYZPiXjdC_gd8JZp5b7MzQlmR9bi8InRX-WyTKsbN9Ldw85IOvRBNRauFzBdmCnkDIlM6NEPzudwlF1pq_9X05lPMEpkTamGAnRKFcKLiVfuPJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=BkM_ZgZbMWez4Lxz7s0A_aSJ4xK5dCvwhsrVRiC84n0ImwId1usBabnMcV7haBuCBN17mnxtwnkKIt4Uf9Yb9bRoz1Dw7Kmof2WCIILulXlGzMa-1Cum8vD09eTPxPAnAeBWD4RGXERDvi-oQ7H5UweG3rxouINUDHVPhU8i4cAhsBo9qQjE3hoNcfp5ZlqxNuWf4qgzjDtarjgq6JPU-80s0XL9Vaw1u-TGt_hVDzhWldWN8-r4_AN-IGA46mm05mJJtltnBU1xneFh1doI_tR6iJvTBkItc92_ROxcEKDkzVQ0UArs6N3auNVGo0dBvU3GbOWfcFqgzOX80ra7tiZw8RkeAr5a_rPH5EQt05btnywej2lKR30avuKG85rABNOdJEBQj4XcZL7bmSNFTp5SXPoJFgOCgQKSOZ9FXPgCVCOcx5hgnndjkwW6m1tauIvLcR3X0_yf0Evf-qfZo_moPbkVmJzES-qImx-HlhyCG6g8NHiOKYjfJhYqNMLl-vG1XvkWg8Vdy4v_n2uFNcbxgvntfR5KOg7MEBrmEpb8eQ4oHEEqcZrgt0aFR620U6GXtoSnCqYHVEzzquDcJNrZ-sEXTVpkfvBB0Ig-OmAXiurBZRnlJCXbrEmHu3q-canddmTgBw-zqaxV15SgBNeTnx4gju82cRenhYE_XUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=BkM_ZgZbMWez4Lxz7s0A_aSJ4xK5dCvwhsrVRiC84n0ImwId1usBabnMcV7haBuCBN17mnxtwnkKIt4Uf9Yb9bRoz1Dw7Kmof2WCIILulXlGzMa-1Cum8vD09eTPxPAnAeBWD4RGXERDvi-oQ7H5UweG3rxouINUDHVPhU8i4cAhsBo9qQjE3hoNcfp5ZlqxNuWf4qgzjDtarjgq6JPU-80s0XL9Vaw1u-TGt_hVDzhWldWN8-r4_AN-IGA46mm05mJJtltnBU1xneFh1doI_tR6iJvTBkItc92_ROxcEKDkzVQ0UArs6N3auNVGo0dBvU3GbOWfcFqgzOX80ra7tiZw8RkeAr5a_rPH5EQt05btnywej2lKR30avuKG85rABNOdJEBQj4XcZL7bmSNFTp5SXPoJFgOCgQKSOZ9FXPgCVCOcx5hgnndjkwW6m1tauIvLcR3X0_yf0Evf-qfZo_moPbkVmJzES-qImx-HlhyCG6g8NHiOKYjfJhYqNMLl-vG1XvkWg8Vdy4v_n2uFNcbxgvntfR5KOg7MEBrmEpb8eQ4oHEEqcZrgt0aFR620U6GXtoSnCqYHVEzzquDcJNrZ-sEXTVpkfvBB0Ig-OmAXiurBZRnlJCXbrEmHu3q-canddmTgBw-zqaxV15SgBNeTnx4gju82cRenhYE_XUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdqkSYXXWEwTUgaYp92YK-hNKQdaBAJ7mmtYqrISUOyLFVDAkqeNzCrCazMphhh5UCJ5lBlzhb4jvKqWfPi3qm2_TOdNVEPWRWcWIYDRHlCOboFmgnUclUN_9mpU-3gIGxwX6Me4sDGQvcAYYC7prfzDDWd0Va2c_rchaT2tKEhzG8nuk5odA0Z1YPFDwz4lTFHrLxDy9ICV7bmafFBdY30rQG-UXUhCx_1ArD-F8K2yajo24NU5Aihtb-MiL6-NPOwbB1FmA0aHhmKD3lWOHyvbpCdaz2L2lN0k1OxOCPUZTwXAt1d36CQnX43WLvCXU9sI-pYPb7myRO1dxA7SwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEyNKM2zVlQukGXZzJ2beWkGibnqzxwTHYM1Hr-axsx5BB6URJ26D212Hp9_Z4cPvdbL89BG38Y6R4Jjqdlbwk0DU97hkwOYIgWBWNt78UvvQksAsroYGZs9QM1F2tcM-JzdLyuO6IHD_OoRJnIuGNdrAax1EneZYvUnjhM_sM30Og60K-d3AoD9dAG3OKMS3rq24-cvOkhnEeNdpCESFVvV3zM1MC3dIE-p6EjMtNca_7WzhOOeO96fJ1-xQWvXxWyB6SzTNwZBJtrheAqBLjidMup4U_Tk5pViqj45Ufs6u9LOjmYHn8K1jLa8dCV_phX1-4SUqVF-KOBhA4kQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k357ZMRVNbRtdsGs7IOwlD0lIVu0CdqkUigZhQZhGyoDQwcYBR0BNg-Y73tG4B2APc9h_C-HcmPttqH3R9as7M2OslMAm1If7bqSGsuU7hLP15fMSs33MTzZvjGOM9I3KBi14B4XdXc4CHrmLNPPRVTSuuSycW7R47VS-po5y02PO7ppufD5YUGHGH_HCzZ_UI3IMcT0cwLr6J-elstYrN-VI_1qPdja46i74EC00vhhkPPtQmUJV4z6N1ktv85qp32EtltZo3CwUcM7zw43jMcxWJrDbkPShmgfZp2e1Wa_pTfbMQf2I88ssjFdc_qbrkS5gjhEZQYNpLH2XIcjrw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=fh98JzMiyO10dy3VEjzx5VzIfS0ZM3BTxkvyw84JiIF61we81X8W8Oe77_YY0pXO2TgDDl2KMJsGRgd1sps5VE7OTYC12FU8ysY0Gm9gFPWiB6vj0I3oqq19gb39GqpHUBv1wUOiLjomd1C4l6bn1xfyns4RZ1XVIjGPBQnaG2EMy4NJXMz9S43TAiojpRWHRpEW93dwqe0aWHU9ITakJ_lSm5SGs_F_9BwXGCsYsoQWuj5nPWKajeKSpPKduDq1Jk47d0QU9jiY86zB-W1FYlG4Yf408xcSWl8o9apv3kpSAQhFykYKBbrlFothFb3XMWm1HuB1stKeL12Y-48uD2_Mnvi7JlWxXNvVQ04iDdF84LxFsCgJazUXno0mv2Qj0ILfKj2VZ4TlwE8fzt9Xys6Ryn_sCIx7sPAdm1MRCXoKuNr02B7a74mxxSX4XtDsb_3yFg6mOMEGsewdXgUOzqE0JHL5vmITmHRkAKW8Z7kXXjSM2_dAoClY59NRbeJc0Dd7fCHUk635Pi-GmrcZgGZC3XvTrSZKxvxLh8QC2bvsA2LrPoXO09eEbIirMtRQqgs2BozmCovSM2wXRNHHDt9rNW9nc9IhVyDA6JnUKcE775fJtXdD8yCt4ffc946M8w-9KSOBP2m5oqMaESNnH1zIGDniNCU2dJDMN0AK1I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=fh98JzMiyO10dy3VEjzx5VzIfS0ZM3BTxkvyw84JiIF61we81X8W8Oe77_YY0pXO2TgDDl2KMJsGRgd1sps5VE7OTYC12FU8ysY0Gm9gFPWiB6vj0I3oqq19gb39GqpHUBv1wUOiLjomd1C4l6bn1xfyns4RZ1XVIjGPBQnaG2EMy4NJXMz9S43TAiojpRWHRpEW93dwqe0aWHU9ITakJ_lSm5SGs_F_9BwXGCsYsoQWuj5nPWKajeKSpPKduDq1Jk47d0QU9jiY86zB-W1FYlG4Yf408xcSWl8o9apv3kpSAQhFykYKBbrlFothFb3XMWm1HuB1stKeL12Y-48uD2_Mnvi7JlWxXNvVQ04iDdF84LxFsCgJazUXno0mv2Qj0ILfKj2VZ4TlwE8fzt9Xys6Ryn_sCIx7sPAdm1MRCXoKuNr02B7a74mxxSX4XtDsb_3yFg6mOMEGsewdXgUOzqE0JHL5vmITmHRkAKW8Z7kXXjSM2_dAoClY59NRbeJc0Dd7fCHUk635Pi-GmrcZgGZC3XvTrSZKxvxLh8QC2bvsA2LrPoXO09eEbIirMtRQqgs2BozmCovSM2wXRNHHDt9rNW9nc9IhVyDA6JnUKcE775fJtXdD8yCt4ffc946M8w-9KSOBP2m5oqMaESNnH1zIGDniNCU2dJDMN0AK1I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBp432KaW1xDzMEGlbAQXp0NBfVKU6F85A-TsiqCAmdrKZz5OjqLloHTyG-nOV1Dj0b1gFSJUiaPewAXsOCOl_1-HZb_3B0w80dEKzaXTIdAhQXUeJw4yCZwAWF1edLP20KnxUUWIxp8iqnd07lnw54OerSzIR7LJn1NKY078cU_epbj46Hw4K1xc2G-6OCB_d6LvfnZmJW26Ys-kLgxWIiQnYh_r2nkJjbbe4CLFxXoFe6WumBGUc4lC5Y0feSRNyXULoT_GZ5-FUPSoDo01QCMXsLaSQfeiX9muLolrAJdS0zg-57ogOolFjwbkSL1OPgoGiVvjKeS-vtv2mc6o2jY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBp432KaW1xDzMEGlbAQXp0NBfVKU6F85A-TsiqCAmdrKZz5OjqLloHTyG-nOV1Dj0b1gFSJUiaPewAXsOCOl_1-HZb_3B0w80dEKzaXTIdAhQXUeJw4yCZwAWF1edLP20KnxUUWIxp8iqnd07lnw54OerSzIR7LJn1NKY078cU_epbj46Hw4K1xc2G-6OCB_d6LvfnZmJW26Ys-kLgxWIiQnYh_r2nkJjbbe4CLFxXoFe6WumBGUc4lC5Y0feSRNyXULoT_GZ5-FUPSoDo01QCMXsLaSQfeiX9muLolrAJdS0zg-57ogOolFjwbkSL1OPgoGiVvjKeS-vtv2mc6o2jY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQpuppS_z1im2uk9-ade2aRJ5YqkgoFE_OMHLKWiMxLpyH7SWz0emS-wqbTeDUvOmyCYNy5CDxdoIa98JevVlN-9oED-EWfKdKYklV2aj5GGEnhFDUN8s8YCWbqFsmKlc3iDb5k8tJOqknjK9nAKLAHzU5CD5U28Imz3mdyzEZcZnEF-Cpzz7Aix2ky2Ae7et1Q8VZXR_g7o8bi9DkTp8mETL0WtfcCWIoW3JV2rh8WzeksrpFhMGYKolTW1UlEAQ17lZWnefNnFShjLhb6A0KWwnz5UcGYoKTCgHGJr4Eia7ZA5nLe3NjVUTNRrAoBWgBPaQXlLpn2CzLHSzNYTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCsvGM05Btn3tXY7azX9MKmDp1J31w4hcM2kZmF2_ovWoUSuBIVKW3STcskQQmXmTlZJDAq1wW4yzMfNcDz9O22O9hxOFkfwPscyRD6lxn0nBG5-Wh4163qdTcx6B_Njnay4_7b1kofYR3wR0wFZ67fkQu0xoUnLguQ49wb0JcxPtlGkIoDc3Xaoup6OzDEFJliKZg4Wtlvig068GKMJvJCTLZsUdVE-4gCqnxvByWSoAEVsblKW_LwttOq5JTp0f2DqySAqkMEqhUHIVp_JAEtyLThw9ODDyA9hj7mvr-fL3deF212IIYZz9YvLzfOfApGGjTTTGAy6nb1KMiZJqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=mvy9zDfjnXV9zBp2vFkpcbXKeIcWpWTqO2gGYY_4zXTBWMUy8VoUV2RSKy8FBff4r4ueiTLkSn2beezauUCWsw_ZUz1KoAGHOKgssIMvHR9qsDToBPbU5uDf_NwPUxxN92PazVysh0TP3aW-eNdVm9D2MwCXii-_K0ToJpTsaYQEyTubF-iWl_F0oEfvFH6Pn_s2Piwr-VrdkiPUV3aqUMQr9VbiviA6tgdnoVY0L7lhXK5Ul1242B3ANxPXw7a2yLQDQk-xp398grDpk8SzhtQV4laA8SWGrquuO-06tnVJ47QzhXaEv_AMJpYXyQSwPasI0t4SD2LkQMCObtgDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=mvy9zDfjnXV9zBp2vFkpcbXKeIcWpWTqO2gGYY_4zXTBWMUy8VoUV2RSKy8FBff4r4ueiTLkSn2beezauUCWsw_ZUz1KoAGHOKgssIMvHR9qsDToBPbU5uDf_NwPUxxN92PazVysh0TP3aW-eNdVm9D2MwCXii-_K0ToJpTsaYQEyTubF-iWl_F0oEfvFH6Pn_s2Piwr-VrdkiPUV3aqUMQr9VbiviA6tgdnoVY0L7lhXK5Ul1242B3ANxPXw7a2yLQDQk-xp398grDpk8SzhtQV4laA8SWGrquuO-06tnVJ47QzhXaEv_AMJpYXyQSwPasI0t4SD2LkQMCObtgDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fGJ-CmhQbsUh165gAM2_8d0cl1rIeoINHn0pjDkpRqLseQFJMljRr9bWBXdincerFNV33aob_XPREXscQyFn4DztMUNu8s3If0LDdEmP4VokOMSXRs5TPu_u_Sq07eJFRzq11srw5tp1abfyFtMbYK6-x7KQhoqR4O6FrNsoV0NMXBeKxEZoNj4JudQJBCo988mIqBqLlDBoUF8afGcq02JpQlTLpwj-AGIgktAeu_vDNnkEYKCdhqxm8D14iOirHgfqVe2oqCs6rVj-j_Q3AVt8T7vWKyvyEQSHdCzrypBDJqw0XjpFcwg21dYN3u3jhEBapQeFO9g472DRsMHd3A.jpg" alt="photo" loading="lazy"/></div>
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
