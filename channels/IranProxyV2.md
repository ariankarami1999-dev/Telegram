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
<img src="https://cdn4.telesco.pe/file/bAUL85k4F6MUGjA0t0t8RsaC1W3NfqS3A_g1rdOb9uL1FgkafFv75IkMsdtAvYt4-p4XXLeIBQiIditImOrVXPKc0EHA9cE8XQQZtGOB0GFsLO-4saTKYuywY1FlZw16J5kMih9TuFDa50iSAT4QeQYyi2W31RuUSANxkANplSIb-E6041NxgfrZX3LTf1NMd-YaiSzW7N7rGH3YYJClutGBX4NYAZvAGLcK2K3a0YeWF5eqd99iWzb4TFy3k-XrrE_hK8xl0pnSwrfz1Ax8hqqTiDTJ2reH5x_avSJ7zLV0-LbqdfP_aD46rmjiDbTv5kZHMhN2wfqEzlGZXxKNPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.1K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 01:43:23</div>
<hr>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 504 · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR10199WQF9UugJYCzJ6-iMgboGpNEQFzTGzSeTjucnRdi5AVpKnmj0Eod-unpXaeW8qi9Sp-5eKRS6QUrS1w25ho5i8TyOzXdlhkOU1ZbxcKaZb9AYkmpXPtxjWekp2sOlp5eL-heePwJaJ3IL5tqzOv_Caw_Eqds0whrL5_iEyFxYhPaUSDMnthHfaiYJ7uA-4gLZbVAzvbpQ92znF_c-DPwiXmcPV6uz52XGEw6DZJoI9Cq8hYex-B62gSUhjjTfn0HeYM31lC3tgXEF4Yc4WtF5j-E2Xa4nhxVcavTffGAvgy1EW_DxN1Ro0_TjVzWWNkMSWLfEXc80azJk2mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MilC0Tgd3UWvNXqUaN4KnBaMqnB6mFwxpWrtraJdt6ubIG-QP8cBvKFzH6qZ0dhHEojW8P5BUXwNc4KoJRYI9z2HFM1vETvJi75fc9Cfvq-VDR2SzqDjeyscfH4e2wuOsa4rhyrPhdSAQ_OcYpN-FLruIAdjDHsG0A-3m_xiavN1Jp_0dtM5i6kCqJJP-noviKQdPetPKQQ9pZ2dLvCMkbdoYTm6guFyxeiqI2fhhkSlysc25fNZO83nfeCgQRJi1gemiPpYt7tZOtsn9UKB6NeifsWRkkyMT777v1DImZ1u9lfUWitE0OboAZV8cbaf7Yi-IENI8jEc9u7b7d-iJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEIKsXd1HbjXNfYewAzPI9-7wDOoXa59Hz9d3QceNMTDspF2m9oFvm7INunqAPR31uOSckiDAr3PyqLZaPIqJWol6NFnfpUSYZuDihxc8YXp8uFti09EljwPI7HozL5yoXHHGcLUkIM7W3Ybtze7AJ70fWj9Lta3_UB-DxwxcKqyEOS-RgTeGzd83sexj9A1O_GzWkBE1FZzLTXQBVHexRkCYNpkRaczrRkn6Vpam1-0u7E4oj4aQNhwrlql4J__3yqdl_l8_znZjbkrMV_jxcOWOAxg59GrKR-sRQ331qvVTqkqTDvJorIrWc8_NiJNF273uMCzZqvA60mnpalw_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR4naQhLChtHMANV4v1ATVQImxPObcr-2mfhu4lvnlvNwmFoMV2GHDvOxe-_XNaRof9v3POKoaaQaRwKKzUegaLiAhqbmWbR-Cw_9snQYFIBj6pbeNnWLoMYJ0lwa0ADnIuwWxgZkoNTardwzzB75z8pT-8M98nnQhIDOqq4ZbvxbuhrZlQhmNg76pCkkhMZDWjUt-HfHQX6JwRCoWuOHRLmK1DFbOWmimvAX-pUvk_tNiMSFfcPOTFwlTQmnGflLMKF5H3KDH3xFaZU1m88i0n4GGdjOM94mvyFDgiccKBIK8W_hKcJmxnRhIvwJnIQWyVRercwzJGr-BhR5pvIsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-gaax4CFILHESyCYLfd7o6h2dU-eyXvRF_bo_1psFzGQbpFHvpZ4MFANQ2HulJoio-JkISZi6W1MRFM-KpEwXcb2G7pOi2fpCKrVgsTuymQWcvycRUJ0uU3BZoTjxHGvkvDfUxWR4oE2TmW3QMFQ0u2CMaEzo5I1qHVjwJAwPSPFUamUaiiz4JRvk9WMBZGlOr94FyXsfhPt4h-5Qi_AR9h6_ZrjliCZuo8vS9SRbofL5kCUjQS4VZN-OxMzDhPWWTw0qJN2X-zhYGajS3oYgoPCAfYfdQpnb8JUVBbKGMIbfriboY_7yIfnRkzqYjowkSQ0YN9t_PRM-Cqlt_7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=Y8oxq744PkTS-kNc76Fplw9n0e7KVWr28g9E40ARmdbX7xHPgqBqj5_RZuqKBQSLScvFyDbNffkL7YgesOEEfWrVC_8JFLO8oK39a8WYaJuqh2sl_E6ZYbhdorzslw5nvQFtYT2ICKEThnlVSh3ZdCoynhGPZ3zZ6JmcOArjP3EkHZeDg6EtfHx9KidxUTrpW4W3c9tbRP30YpVfsvlpkAuB4Kkqvsw6k1ejER5vb6uHXJqLl7aSb-6JxCppwoCw1i98KF95KqzCzVVjBMphwFzJ3slrXscSaEd2SnD3pkzpFa5S2YVmz8SkfgsOZBvv5YSzRgxUwTmg7lB7GSzrvktOmIkR6MyNehV5mnKtNFzVXYzlUO9mkkCw2O6pe888dUpgxJPI1B13-7npFuakrDVxJY9h4RwCfufi_KfN0XnM41VBJ6jpFSg3gxrdglf6nySZcAjmMgfSSR2_-utfm819BvxhadgikKee65XySwVOkxfw4SevfWWqw_Ro8ucVG8z5BBfZWSyOMhsgq0SZIKqVKsbX2_B_WYlgjbACwjEiWF_yRMMmNUL310pLEDqOFghLlRQa7EayBtM9vY3YRUggyZQvXNFM-BhQR8yD0bScHbYX5QihOGnYhCHAZewZaep9uNHE51n0myfiHZQ0Rld8Of-BhysdVzX8zbuFFBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=Y8oxq744PkTS-kNc76Fplw9n0e7KVWr28g9E40ARmdbX7xHPgqBqj5_RZuqKBQSLScvFyDbNffkL7YgesOEEfWrVC_8JFLO8oK39a8WYaJuqh2sl_E6ZYbhdorzslw5nvQFtYT2ICKEThnlVSh3ZdCoynhGPZ3zZ6JmcOArjP3EkHZeDg6EtfHx9KidxUTrpW4W3c9tbRP30YpVfsvlpkAuB4Kkqvsw6k1ejER5vb6uHXJqLl7aSb-6JxCppwoCw1i98KF95KqzCzVVjBMphwFzJ3slrXscSaEd2SnD3pkzpFa5S2YVmz8SkfgsOZBvv5YSzRgxUwTmg7lB7GSzrvktOmIkR6MyNehV5mnKtNFzVXYzlUO9mkkCw2O6pe888dUpgxJPI1B13-7npFuakrDVxJY9h4RwCfufi_KfN0XnM41VBJ6jpFSg3gxrdglf6nySZcAjmMgfSSR2_-utfm819BvxhadgikKee65XySwVOkxfw4SevfWWqw_Ro8ucVG8z5BBfZWSyOMhsgq0SZIKqVKsbX2_B_WYlgjbACwjEiWF_yRMMmNUL310pLEDqOFghLlRQa7EayBtM9vY3YRUggyZQvXNFM-BhQR8yD0bScHbYX5QihOGnYhCHAZewZaep9uNHE51n0myfiHZQ0Rld8Of-BhysdVzX8zbuFFBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqGgJlBjYQ3RfQW0MlD4Bg69a5gEYbE0lJw9KhwFI2jSoXO7f7BJ3oC9-tHjS86KD1RMX1LDG1ZwLS3-OneqccYO3OQsNNSYPpGwF_wickve8GoWAEwvPx-I3yJXjxwf537orFO_80SIfHmlQS1HnXidNeZw9w6Dj2zn3zIVllAaWeMKEo50Nmeb1NIQgUvpWd8PI5FpYrtR155XtXJClTwh2eOlhXT-i5zZp4ytoEeEJ0cp97LEV6XBfb0SkbwdaDWspJj_e0bs_Ma3Vj7k19VI5TI7G6dWgRM0ud2Z2LnHkxDwN9I4FD3f5rzUkfk9LfpPw_pKkMRbKyNu7VZk2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwNA0XsBHofhbDSoDHE44SJUMpfcJVkDsx6t4lZuSa9RRGCG48YBskMjpEKW77xyUp1HI04ZUTN-G2fRvlSWJW66LfkMy7iMMPcGfSW2jZ1yTZgJNXtPwbccIFVQSn48cwZpCbebwow5ulDS9CjVRXnCZ0jq-xCBB4mrewyfB2N2Lv7OoFl74s-PPE1xofM5A-jPTo-5FV7muU1fs035Wp9rhdbV2uhguj0w-Fv4IWR_DSX6sKDpaCTRxjNmzdLqFNiLCCz9MaP8HlZLW0q2NKtw3lvr1QFrA6qtT1_9MOOaJKD9zZJmpcRd9tpIvkEiyLgiBuUjq9Zh5eAy_v-wxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMaMQ7f8GyIjs7mLZhosq6RjAmJBF_X10pHJNEmCGUv9TbH29vtA1KH5869WCitnZ-kt7F-gKrt_GjwF6J3rVlA_UgeKpf4f6E7mqQ_IpVUybsMzdbuh6v6sxrnA9oRVbTzS52PbIVGP6OiRO2Jx5Ku2YWo6JFw79Dz5uVZhBkQQHiciRsJEHXaVZhPLk7uqbnaOSAVjKoL6SURG13iQkBokBnrlGK4FDmRHlnJCSjqxUSD03V7xUv-PzW2W9JtSzgtmPZhP-Za4lR-YJQlCUcuHqfPPGzZDtwVJ1-UjEGWQP3YF_tJ8a6vrD_srdMGf7LdcVexZGpBHNJ0E_1P-CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=Cv-zSLdzNU3JKUXIwQd2_F_QuotJaCUbale6sLd89KtTfU1sOXZFhgvf_LcI34_OlrqgYPABilyKFQ0T24uPFGJ3GXgIkB388dX89ux4OzniMB-570C-Ew5s_ubE8GQ0iqxQZTtiSUBEKjrm3ZpctEp3p1vLpv8nJ4q28WywGBtyjcI5ye9IyBc3Gb5JxsqPiuJlCY3Lqh35BBqqSMfwK6iAyG_Mp7ePkpVkF4bnsXjvLXqvwLGNOHnTru7CBbMab7YrU5FilprUGilCxHzx6dsG6VMZThWP5zZshAT_ZgeMLQqN8WYi3AYMXwG0H_KWzGN48p7Z8bZEwePUftV7HDY9xN0HCm8u2-7Zl4uWl_wcNGA5_B8IKvrW3KFf-0ac2rDQcG0kPLise06bfOe4FOvTvanqMuIVXrt95VfHUfxGwjjzz5fxE0Am3Xk3_uW8VvPPehzmN66YsUL0cHM8jn83e2J-DBkTLWN3yKbOP70SbQOFL3oZ9PRVpo_hvtojJwwbsGkIuZk207OATA1vfJIP8Y6wVFNgBL5aaHQq34TOGpNrwE_zdT8VrwQvDjEnnYI4ICeQ63x2jnCUP6uxUpxzUFgzII7agUkOUscUzVbwKztF-uN638Omby-0IhPcRZBGiQk-dDKOvS9ixP1wV3v8pEffbNO7-Xi7mcU4V_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=Cv-zSLdzNU3JKUXIwQd2_F_QuotJaCUbale6sLd89KtTfU1sOXZFhgvf_LcI34_OlrqgYPABilyKFQ0T24uPFGJ3GXgIkB388dX89ux4OzniMB-570C-Ew5s_ubE8GQ0iqxQZTtiSUBEKjrm3ZpctEp3p1vLpv8nJ4q28WywGBtyjcI5ye9IyBc3Gb5JxsqPiuJlCY3Lqh35BBqqSMfwK6iAyG_Mp7ePkpVkF4bnsXjvLXqvwLGNOHnTru7CBbMab7YrU5FilprUGilCxHzx6dsG6VMZThWP5zZshAT_ZgeMLQqN8WYi3AYMXwG0H_KWzGN48p7Z8bZEwePUftV7HDY9xN0HCm8u2-7Zl4uWl_wcNGA5_B8IKvrW3KFf-0ac2rDQcG0kPLise06bfOe4FOvTvanqMuIVXrt95VfHUfxGwjjzz5fxE0Am3Xk3_uW8VvPPehzmN66YsUL0cHM8jn83e2J-DBkTLWN3yKbOP70SbQOFL3oZ9PRVpo_hvtojJwwbsGkIuZk207OATA1vfJIP8Y6wVFNgBL5aaHQq34TOGpNrwE_zdT8VrwQvDjEnnYI4ICeQ63x2jnCUP6uxUpxzUFgzII7agUkOUscUzVbwKztF-uN638Omby-0IhPcRZBGiQk-dDKOvS9ixP1wV3v8pEffbNO7-Xi7mcU4V_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=tsKpVaiPAs6HHep71HQE65Ey9mrny4DaEbkelJTEWGwyS-esmOzQwcMKHekeHGoG7-N-15XObiJP3DOe-pYDjWmQ8qVKPv9Crw5ZMQOW6oceZ9y8Kk5EHCIrvPYKIpdKRRoNh7oNhAPx45NdQz12nQmqRZZ1ceBvKDXBKcxqQ4t-uOB5KJBwlo6Qi5owcnBQC4X9T8haE2i_S0sNsIrWdecxWq8QpAMUEGF4dqNDKiRvMcMZw8LaZBnsM7YNL3VMJHIXFugzn1SSTmmg4K1Gv2e0s-Uh1XmT-aZuC4RcpnMSPkXogdVgknCmlt-MP8Rdx9hyMD-G3ttzpehf_QZSs4HpR8IUVcYReC48dhfRjTbgYUELxHVipYH8LO817EN40f1ixlh6il_5d1ubJCTrXVXSu2XICP3mpafYhr-SB90wHCP_CUStuBVyWCWKr9q9onCrp8w0K7qzGnstU8B-qvPvBqAAl2xyjPwfbOW0Bxxe8fjQsCTb60pLpRykczpTKm-JCcD4m8MAKQAWBezTHcWW5X42mfMvjkTdsrI3XdrKJL5RFP2TKnfmEhbr30sbLCXoqH0DdgQBnra5XSM4cjoJ8kCdaZLt4jlUh0WgrQd1LIbBCcAxiH5vQS6U1zn0kLNNbeDqKHcDSZFJ57xB6kmHnbzVTXaCyggN1sstZ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=tsKpVaiPAs6HHep71HQE65Ey9mrny4DaEbkelJTEWGwyS-esmOzQwcMKHekeHGoG7-N-15XObiJP3DOe-pYDjWmQ8qVKPv9Crw5ZMQOW6oceZ9y8Kk5EHCIrvPYKIpdKRRoNh7oNhAPx45NdQz12nQmqRZZ1ceBvKDXBKcxqQ4t-uOB5KJBwlo6Qi5owcnBQC4X9T8haE2i_S0sNsIrWdecxWq8QpAMUEGF4dqNDKiRvMcMZw8LaZBnsM7YNL3VMJHIXFugzn1SSTmmg4K1Gv2e0s-Uh1XmT-aZuC4RcpnMSPkXogdVgknCmlt-MP8Rdx9hyMD-G3ttzpehf_QZSs4HpR8IUVcYReC48dhfRjTbgYUELxHVipYH8LO817EN40f1ixlh6il_5d1ubJCTrXVXSu2XICP3mpafYhr-SB90wHCP_CUStuBVyWCWKr9q9onCrp8w0K7qzGnstU8B-qvPvBqAAl2xyjPwfbOW0Bxxe8fjQsCTb60pLpRykczpTKm-JCcD4m8MAKQAWBezTHcWW5X42mfMvjkTdsrI3XdrKJL5RFP2TKnfmEhbr30sbLCXoqH0DdgQBnra5XSM4cjoJ8kCdaZLt4jlUh0WgrQd1LIbBCcAxiH5vQS6U1zn0kLNNbeDqKHcDSZFJ57xB6kmHnbzVTXaCyggN1sstZ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
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
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJQtoMLpiCUL_TMJlH_pGwMPxnw8WNmxKaQxPTMil920_9J3l4me0whLhWIlvKOhWZx_28X-i6X03GrnROYu82wRjEd4O8iy3bf2e7FtSppvdyCnxhyMzR9M9Qd3JDAFB3PeZWHTp90zwaRshfoyKv55u1rBjZNh3gS4SD66oWqdeu7_xX48qE3PwNOrvHmW7wEnZ0y9ddWYrHFB_2fjrzi6royGw71VoEvQk8HsadEwq-JLPH5YuKsd5LVJ6Oa3cig3syLfg1t8mle0NQLY-NMDBiK9S06KIOJVir1X02k-jBmpOVH9HNJjs1l92xWlExa9eZ-O_uSg-4zd9MR5Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=NUK5xCWv2_i0rPFUVJqm-N1EN0x6SKCir_kBueDn5U5L6wiGF3k8RTuGzHoSNqM-kWyq5eWfDcm88WfooykgbJpqMG9T6zTE5gnqpcyYcg1ZLlfqr74dXV2FMzvbhB5dH7wFIHUobyacHIdq6aEayzpMniEUTcGxB4gdhzQNXgUW9LOTdu7TDTeZslX-HFreCB2xnWhptejkfY2qlHzDOkcM-KpaqjtYiOfGxoX8fLQR55WZCJBtY-zrTCkdgbYaWqjslAqtCyZrExVY37ey9P23UucdCdUStMZE3_wrdXeW-ymr5CKf1vezR32ZZwMXp74ENHMiNbuBP9hsAuZ2MXRfm_UQJbhiIVsjZrogy7JzWOXhfdn_qvAXIcj3Tza7wdbeeGct6sJsgASrDBAJ-za5Supws6v7s4FXwaODG8Stft7taDur5OfeDVt4UitL-AetPQNFt5YtXHajixzao_I05V69mOGkHiuSgl7mu6udd26qalpCAjltfsenhwKzcwl4uh7Koy2Qr-EbKq_IlZlK0DiDCO_3tEvVtAb_p3vsaTNY4bCIz-RVfxR960JKUL4qa_sia0Kvgj82BidfaR5dOfIQ3IUreSlIG261FIQhfR2Cpvc_DYLK7n8mc1rREGUG15QcqCMPzmz6hehA5LeuuxgSANUh3e-sAyWIbsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=NUK5xCWv2_i0rPFUVJqm-N1EN0x6SKCir_kBueDn5U5L6wiGF3k8RTuGzHoSNqM-kWyq5eWfDcm88WfooykgbJpqMG9T6zTE5gnqpcyYcg1ZLlfqr74dXV2FMzvbhB5dH7wFIHUobyacHIdq6aEayzpMniEUTcGxB4gdhzQNXgUW9LOTdu7TDTeZslX-HFreCB2xnWhptejkfY2qlHzDOkcM-KpaqjtYiOfGxoX8fLQR55WZCJBtY-zrTCkdgbYaWqjslAqtCyZrExVY37ey9P23UucdCdUStMZE3_wrdXeW-ymr5CKf1vezR32ZZwMXp74ENHMiNbuBP9hsAuZ2MXRfm_UQJbhiIVsjZrogy7JzWOXhfdn_qvAXIcj3Tza7wdbeeGct6sJsgASrDBAJ-za5Supws6v7s4FXwaODG8Stft7taDur5OfeDVt4UitL-AetPQNFt5YtXHajixzao_I05V69mOGkHiuSgl7mu6udd26qalpCAjltfsenhwKzcwl4uh7Koy2Qr-EbKq_IlZlK0DiDCO_3tEvVtAb_p3vsaTNY4bCIz-RVfxR960JKUL4qa_sia0Kvgj82BidfaR5dOfIQ3IUreSlIG261FIQhfR2Cpvc_DYLK7n8mc1rREGUG15QcqCMPzmz6hehA5LeuuxgSANUh3e-sAyWIbsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnjTx-qy0AKg_A1voyuqrj5xz76FVmNhn-PIrgKm5YmltLC42Dtw2EDkYM0ZjhTUmhrGAcZqbPTNjaFitFdm1o8YcUZOJ-GfVKaNbTuXEitVmBcfPEu3z7hh-CinJnCtNfl6cepOCyPb4X1Wwj62ltQzFqVJzQeCNSA1WVweEgiSlQbDRJ9mVE0UytNfwivQHYT6MfTCso3hU-MpgpKJ9uAFuI6WSqUND0-mENarqEcox08ero588O-Y-uFjBKyMreq7y7Aad2sDVOYygi0lCcW6i60GVfeVuSWLIEtKutCTipJsqNWz1r6Nune5r5JVlvK_whTbDs9iBIFWpqjGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZeDTELF7yVuo-L4hc4u1ai-YMHU_EgdLupSaxgpDN-ZaDpfgYC4fVSBIbPwiMKYUPbsQwQu_MYSDbmII71yKHgWQIdUmTexOAXG34jBltxBjym2j0Yf_Yo3BGhZ1agMO5qS00_NCkYfjQ35t0h2TOafF8dqBgElh7HY-O1Jfhx9t9iAI_7AXRMNoZGqHUIPoNsuApXbUYcJE6q04N39q5R21CtzN2DUpsCb8qzvWmzhVFLj5hFLFqTnR-JCRFmfTGr-n10UzAWYX3AqqP-ibzSkr4VnSpOL8ypcV59dQrd5DlaI-45swMnWNF2_Ws_QE6QMjd5AzFwR4Il4j9s4qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=SJfiwUMDt33ieTIyNFXaq8ej_geKWV0WLvw7pqQi_rIpzcYWndeceREvrMVTc3cNKbGmsWvC7rI9-COSOyghVrSdLob4rwsqpQbkQbwI5mxuIl4S9_DKDku7HNdttFrUX_xkNQLSsfF9kChre7LYqR2jqDTW9MyEliyUyXx-3nQeVINx8uwbA2BVHgU5nmHfOouZN2fNhN5d3OL1rXuEGr0Z5fSeXURtCVosehsWKQl0J5_ozVE58lNqMlva8Y4aEwrjrVLDZnUEZjZc1ZddGxpZ2nqkU16axBtlaAZ1ncpa5P85jGCPVT-rVlaWEBv2um65JblnHTwQJDyijjJcyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=SJfiwUMDt33ieTIyNFXaq8ej_geKWV0WLvw7pqQi_rIpzcYWndeceREvrMVTc3cNKbGmsWvC7rI9-COSOyghVrSdLob4rwsqpQbkQbwI5mxuIl4S9_DKDku7HNdttFrUX_xkNQLSsfF9kChre7LYqR2jqDTW9MyEliyUyXx-3nQeVINx8uwbA2BVHgU5nmHfOouZN2fNhN5d3OL1rXuEGr0Z5fSeXURtCVosehsWKQl0J5_ozVE58lNqMlva8Y4aEwrjrVLDZnUEZjZc1ZddGxpZ2nqkU16axBtlaAZ1ncpa5P85jGCPVT-rVlaWEBv2um65JblnHTwQJDyijjJcyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwPW8DEpy7ElQq1MKBcR_tarS_kGQx_Enl7dyE3DHDEZ73RD6XD4IusRLcOeuj2mjQxQZ6ZQ6Qbfhk0zrEDqw4r9gShIRKbA4dn5F-pYb1m2TEp4c81SNxKpzzoI9HCZvI8f8-igFxAxJLj6HF2YcHvPRipAmM7dd5kW4Ma1i2sZnqzsl3myeq2vmNhK2xIXkAFIs7H8wmAlE09liclicZQU5WlbgI_kHxvVKGKodLO9FH8VweQ0SPovhJxfvxIt1x9tg3LwALvd3WsD83R06m52J91dUAbOBNuJo3mzEs3LoSXXXz-Yu0BtBGpO445kmnXWr6bTwBuVinCVQLOfOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzFfLdRwuLo0SFmygQe6510fwd3F-RBbOgTLZQ9usz5HOelQdkNgSlxl6UspE0PEHjzesG-a70HkhKrxdGy690lV_3CeDmUgJJ6YyiY6jTSfjkPmHHAhXRdnMDM9XeN3zfBCRs7SdMLCcLhSTmiwS4G-0ttlX5rHnlUV_XA-W3fpUJPqAs0BfoeK1tfyfl5EJs2hu3h3JmAV_KH5ML3_sbIQqmP9vdOED50P6NyHQrb3dudIF749sdXdZN55W7XamG76BxR_nF58IqvvYs4_i_BKxvKJsJBFwux4FLlHiem77pkB7xAq2yU7B6e_xqbBgprZOLp3y2HnhukC9DsUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=ql1We-pEBv7TCXFHTUVPyDIPXyN9G9yG-puUOWNiMNOvvyTQyx0-xW9BMmc-ueGV6b6gqKu07ilT68KEAFX7YQ3yaJ3VknpKUY_Ft3m-1XYw1oyENQyd8YE0rwZNoRVfRIIkN_wMPYR3WuF3ezStVzQ6etKAZFIrfQpagDtPL2SHbuPfZTWgrzR1RgJE8QpVsCc3ztZFP_q8x42GuGlFSbYtg8Xrserr-U5xZfbueWM0fp5QNuMr06wsFqrlESdz5YaMl_6oWn3i2Sfh7U0ewqhz1rzKg_7tznqUItnn1xpJIyOFS22Ts7kDZy54zcZtcUgh4xzbhkETTf3liKwwrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=ql1We-pEBv7TCXFHTUVPyDIPXyN9G9yG-puUOWNiMNOvvyTQyx0-xW9BMmc-ueGV6b6gqKu07ilT68KEAFX7YQ3yaJ3VknpKUY_Ft3m-1XYw1oyENQyd8YE0rwZNoRVfRIIkN_wMPYR3WuF3ezStVzQ6etKAZFIrfQpagDtPL2SHbuPfZTWgrzR1RgJE8QpVsCc3ztZFP_q8x42GuGlFSbYtg8Xrserr-U5xZfbueWM0fp5QNuMr06wsFqrlESdz5YaMl_6oWn3i2Sfh7U0ewqhz1rzKg_7tznqUItnn1xpJIyOFS22Ts7kDZy54zcZtcUgh4xzbhkETTf3liKwwrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=uuLMH6au-80Gu5xWtwxUyc9NnvwWawucIPTrDdc8aVUi0sFWVEtHoDeTJnwgbGmVkCE6pPINJWZw9lzvCumhBcWQxROjH1C6jL08AYUyoPjnSyTunJ0_bgsOPjHSekyIR6dM-7YZ3GbfNfwDiK8BjT72fH3IKM7VA3PnmZp7x7T2O6m3wTp3zvrdIaQtaF2T2v12thfuw_pmGOid7e5AcdWjCNmtwHJ2LWrMAAxI0YoxwpkcAf8tiO9qFakFaO2Tuj3xGH8L3zVnFzIiWMs4ZXG0vwb0VaEbu2CxOfRXhrSs5pieY60l-A3UOOKOpqYUKQdP5J4jlOmwraY2yrPRrDuQ6ipFRxCk3E7hcFV1GzNy4pPeiuPpqqja_nC5vOYEQw9pzVTUfFolyTBWt-Rz01aoVOuQnyYSrF7LbJvyYpFanJAREB6G_piULLWH-Nmq2Gy2Z57KzSlwfaDINbg-7VspJtWMfyWKw2c9JTwiGLSzct7Qg5aeYvxBlRjU0VaMLLN0zEzKWajoC06Q8YbVkiHIa2tYbF4_0T5R7YEgyijEIrCH_HADzZ1l75DtRn4rSjYzOgQauZlgo_1LesrW8-SbNTtcrJKKusEPOyKyCLzfN9mV6J7EbKP7HSK0ffKW-W7dr4nDqxgn4YNzGPZIT20qmxhi-CRnvEGY_6VpGyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=uuLMH6au-80Gu5xWtwxUyc9NnvwWawucIPTrDdc8aVUi0sFWVEtHoDeTJnwgbGmVkCE6pPINJWZw9lzvCumhBcWQxROjH1C6jL08AYUyoPjnSyTunJ0_bgsOPjHSekyIR6dM-7YZ3GbfNfwDiK8BjT72fH3IKM7VA3PnmZp7x7T2O6m3wTp3zvrdIaQtaF2T2v12thfuw_pmGOid7e5AcdWjCNmtwHJ2LWrMAAxI0YoxwpkcAf8tiO9qFakFaO2Tuj3xGH8L3zVnFzIiWMs4ZXG0vwb0VaEbu2CxOfRXhrSs5pieY60l-A3UOOKOpqYUKQdP5J4jlOmwraY2yrPRrDuQ6ipFRxCk3E7hcFV1GzNy4pPeiuPpqqja_nC5vOYEQw9pzVTUfFolyTBWt-Rz01aoVOuQnyYSrF7LbJvyYpFanJAREB6G_piULLWH-Nmq2Gy2Z57KzSlwfaDINbg-7VspJtWMfyWKw2c9JTwiGLSzct7Qg5aeYvxBlRjU0VaMLLN0zEzKWajoC06Q8YbVkiHIa2tYbF4_0T5R7YEgyijEIrCH_HADzZ1l75DtRn4rSjYzOgQauZlgo_1LesrW8-SbNTtcrJKKusEPOyKyCLzfN9mV6J7EbKP7HSK0ffKW-W7dr4nDqxgn4YNzGPZIT20qmxhi-CRnvEGY_6VpGyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbpaeyaFbY1262pQgFV1BhSEW6UT4qL6HATlI1eOF7d_zHxwiYJCXIkYElW-Wifgbzc0q1zZ7zKE3vohTTQtYwTe_tKjxa-qrgjodghvfHLzkJTKyDQ9EI_Vb3wOcBh9s87NeAT2UXup0-JJ1I5fhs1CVwkZ5bpqcUvHQmENyzmEjnOtoz6DP0HMac0iTlcgyRbvDZIyZ3HNWIb8L5XmM4EdflU0vimJVX-IEI9hEtsvSztKrEdnAUlw-wnCq4oWU1ArTEjv_lgfvaAEs2UAmsegQr5lG-wBt5xgvhhSwD08gIrz6VkbhDKvp9QIp0tVSKshWbRkf7rY6ixQ6u-BIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9LIo9DJ0GoKd4cyVctGyey8UM3XQP0YtiA73CinCokgz-3YxEV8-eT12wuOHJFEum2w_LfkWfYYVixjNS-wnBEbgPMlmcJOkt8YQT52CPRamwkeldjYFtFfWbWkvaTYOpvudHPm7iH02OUZVJR2-YF_os4oxnuwpO9WzZuKnmzTZ8VzuyDTd3IP6EyDyV9NQ2SQPMS7fZp95kV36L01K13gSbvmHJ1y5kZYVX0FtgAcldHk2I95-WHX4qnfuzmJ9Ws3h2vAwNkHlNAVH9GVb29q9RCjT6-0UsWBHLUPGfoV7j9mdsH9Pexa061jl5WiiYxu_s_HUPOLdle1dCPslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XkTMxYirW1dPdrZDwwzbWvj7uJXcJgqsNJcFp-W-HOeUbz6x0tQajK7qwJYryK2YRL4vzvQ_sKPOZz7vjCdIkUKxOwsw-xQFPhP-RlsEfVjW9KlyVwk_UXaYdHifkvJSXwvKcOm3n_4ZUYeGJ2Rnd8kJ8BOnByDSLQXkF0XGiobArUix1Y2Pp3ySmI5L8RseQBeqatydCqMdks-WwWzFUSCG9TPy2NPTdFA8yTuB7xCOcNRUeOAOxMjLNWtLlKD5jS8nknWbqb80_zkgFibAioLBbhNV8ShByRDrqAlYw0vz8rD4gtrV4w06QcffYCnlsyvo8WD6UF4ye8eieo7heA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=r1YyB41pI8h4uLqu4nUdHDfawliE46W74mC4QjpAeQi0xvNaG6nGFyNvqaDpfZu87T2PeJKBRcqFGp2tMhD-oWR7E9nZoekkuoIYtasQhyZSfCFGLnIhyqaa8ICLDKxASmBBKA7g9TB-B6d68I2E9o9vEfL8cEe1d3u_2qHjuw_LVdB2vyYnFvLiS1KiX3_nflbcSVh0CVCwlF0MKSvXShaXjRpMNUmE4gL_Q2bmn6kpcPdbCDlDSvCYv322QT12-TKnJi8qqR0hUkcDCCrsr3xgLMOGv14EPs7lDPh79tp1fg3Wnm6DnhlIEG9DOvOyZPJ5kHJlP9_qqX7DRdCzsyhctOK4_Rw6JuVlB6w19dynqv9ur0s6_ho0WvYwXJBkZTs4qebNyDikWkWMSOrzPiKnfgFYBwCXZk16uOY-3Lmohh_69QpbdeXj6_EB8JkSv4LFuhPrx-tzNQooKXZ7bTEDnRWEzF1HVNvaLTfxHnFH0hzM6R2SAIQpLyVw3Ewc2QUgeSTNXSLoeeI6dKm-tWN_9zdBPN6RScnz8u8okvV9QXtntF0RhQTO4ilAS19fjP3juiqzvJJd_8nr5dsQVBm51Hb5jiaqbqoyXKRv0K9dqYQDlvPVKNYZ3Zm7FLJ6W42t-F7MzA0nw1EESq4L7XrimZcl35jhQPG3MDtOinc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=r1YyB41pI8h4uLqu4nUdHDfawliE46W74mC4QjpAeQi0xvNaG6nGFyNvqaDpfZu87T2PeJKBRcqFGp2tMhD-oWR7E9nZoekkuoIYtasQhyZSfCFGLnIhyqaa8ICLDKxASmBBKA7g9TB-B6d68I2E9o9vEfL8cEe1d3u_2qHjuw_LVdB2vyYnFvLiS1KiX3_nflbcSVh0CVCwlF0MKSvXShaXjRpMNUmE4gL_Q2bmn6kpcPdbCDlDSvCYv322QT12-TKnJi8qqR0hUkcDCCrsr3xgLMOGv14EPs7lDPh79tp1fg3Wnm6DnhlIEG9DOvOyZPJ5kHJlP9_qqX7DRdCzsyhctOK4_Rw6JuVlB6w19dynqv9ur0s6_ho0WvYwXJBkZTs4qebNyDikWkWMSOrzPiKnfgFYBwCXZk16uOY-3Lmohh_69QpbdeXj6_EB8JkSv4LFuhPrx-tzNQooKXZ7bTEDnRWEzF1HVNvaLTfxHnFH0hzM6R2SAIQpLyVw3Ewc2QUgeSTNXSLoeeI6dKm-tWN_9zdBPN6RScnz8u8okvV9QXtntF0RhQTO4ilAS19fjP3juiqzvJJd_8nr5dsQVBm51Hb5jiaqbqoyXKRv0K9dqYQDlvPVKNYZ3Zm7FLJ6W42t-F7MzA0nw1EESq4L7XrimZcl35jhQPG3MDtOinc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrrOMywR-9uhBxCbXFtA7mheqNy8ePLT1GwxEBdTGTcg63lOO0gXd507OaoP2JeErPDQi4mw0Dy3KCaq-0E5i-3lUDGp-nzkugs7Vcs0wHuNT6rbNqwCcyxkGp8W5eksObrBwHI9V0HLjLI2ngjUO_RWRgT3vlax36j_-EdWgEquVPxoCPpCpWll6xxDKRhVctvUkqHFEVrv5DgDVR0_6wabPzeMu2MR8F1wE0lf7mC5H1eaA-NXq5-OtBGiNQ3VbJX3rMBD1ftcawxZ-DSaL0CwWxtPjTiGMzf5K1Y8aYDbP6YJj6yRjVwLFWi64QUhWEFlBY1_HiemRGWPwwRNePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrrOMywR-9uhBxCbXFtA7mheqNy8ePLT1GwxEBdTGTcg63lOO0gXd507OaoP2JeErPDQi4mw0Dy3KCaq-0E5i-3lUDGp-nzkugs7Vcs0wHuNT6rbNqwCcyxkGp8W5eksObrBwHI9V0HLjLI2ngjUO_RWRgT3vlax36j_-EdWgEquVPxoCPpCpWll6xxDKRhVctvUkqHFEVrv5DgDVR0_6wabPzeMu2MR8F1wE0lf7mC5H1eaA-NXq5-OtBGiNQ3VbJX3rMBD1ftcawxZ-DSaL0CwWxtPjTiGMzf5K1Y8aYDbP6YJj6yRjVwLFWi64QUhWEFlBY1_HiemRGWPwwRNePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-k-FYG2W4VALZodhH1z7VAaU-8Gf8T3cR6QY4kMy50TLVu0_Wx65FMEJWUJm5JU0mUE0-m86ykYfHcb8iDmkScGvCZojbYcyykJ8pvx4XNlqcK83II3VgSsiNuHurJwGjHwSyAsPfExTP0fqJ8Qdh2lO-GvT-sx-eRFVE0wKXLmg8bT_yZw32yQzU7-5zpnNArsobFclU09GdSYqlhk6hlWw1xVlGaQs0IPXVIRo4imPcKfl_hHj4_tqesNtD92eXrq8_M382u4VKu5mC7uHoQhMlMaMeNofoRR8MPveII_6Y1rH_7VdHICR4sKXtZlTnLeP8fKOsz02iH7q4U5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSlNbJVpHrDvtccq_DZSuQ5PiSS3O-sGKnt8m9mEGlrs6op1WUsh6t9CAAJvw9apMtDjzKqnE0aZEJi9e1hktj6-_vSYbQE3qYBr6LkF_z5NUP2jvjCC_mRKUHHJSKbod-L7hCtnnLgWGwWMaRmscYla4kUjipi_tnDvXQoESjziq8fbwuiOYGFkvBBJWgspRFJ-sOSYdyfAlSMLQGzrN9yCnJE8AKROofwDwN76v0CBPufFzSGFJmral0MgBGQdIwkpFjmuhg-_W4VyOpXBzkKoIPJt_tsQW5U6mMkOqveYdaW1uof_qHXonqYkaIJx6YargisJxdZpSL95D5mgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=eKXpSaU_JcZauA9jpNPla-bQQjBczTXr3wnU7eHAGOAQ8ekhxkQaQZZlaX50EfSbS_PDkAq_udhq7qLrbkm6hE1Yt-oAKgNOfcFlalyp9j-6HXpqOhWtN2h3wvQ6e34kMThsxHFAQGYq0Ckx-rzgKI7XNr-dPX8RR43oqlWAvtHkif0V4j5JzVOD1rR0CS1YvP1nGmUGR8BDF7k9jYPM-0GSKXaGPcoyaolab0WrWeeCwZqKNjm4xiQIM7PC_8kzZkLZNdSitQ0tgXn_fPx4fpbLQD7sZFRxex5XGcQRTvZi6eqxUhKk_WwXKmyHjM_-LMtSPzwqLZQGuIoDNApxIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=eKXpSaU_JcZauA9jpNPla-bQQjBczTXr3wnU7eHAGOAQ8ekhxkQaQZZlaX50EfSbS_PDkAq_udhq7qLrbkm6hE1Yt-oAKgNOfcFlalyp9j-6HXpqOhWtN2h3wvQ6e34kMThsxHFAQGYq0Ckx-rzgKI7XNr-dPX8RR43oqlWAvtHkif0V4j5JzVOD1rR0CS1YvP1nGmUGR8BDF7k9jYPM-0GSKXaGPcoyaolab0WrWeeCwZqKNjm4xiQIM7PC_8kzZkLZNdSitQ0tgXn_fPx4fpbLQD7sZFRxex5XGcQRTvZi6eqxUhKk_WwXKmyHjM_-LMtSPzwqLZQGuIoDNApxIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sodZbWqDrsu03klUnw4jNXewhk-K5ca7fG3Er-kZ1J0YR0gIOLc3S4vm7v-wnTU2M0gAPupnkADEv9IL6o-xr527emgFJBZI5fn3zU9wbHAI7FNm7NjxKrFLsFbltHnti_FKq5KW2KGVnA4_GONIOj_8V7-kocM6_eZrVc2jZQTaAXhYSYR5QoONyFYX_OWvblDEf07BfmKB_Vb41aJOU9BoduYn-9ZJ3D2l1D1WvmQd552JTqPGou00JnDA_AKkDXFvOyEB2lVJpIMesH-Q3LSFq4y0KgoKkJowr4h1oGpExSnRVlrfBRgirL00E3fJX_dSIyCZb7S2tGeiEW-7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
