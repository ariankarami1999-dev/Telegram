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
<p>@IranProxyV2 • 👥 39K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 22:24:13</div>
<hr>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 16 · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MilC0Tgd3UWvNXqUaN4KnBaMqnB6mFwxpWrtraJdt6ubIG-QP8cBvKFzH6qZ0dhHEojW8P5BUXwNc4KoJRYI9z2HFM1vETvJi75fc9Cfvq-VDR2SzqDjeyscfH4e2wuOsa4rhyrPhdSAQ_OcYpN-FLruIAdjDHsG0A-3m_xiavN1Jp_0dtM5i6kCqJJP-noviKQdPetPKQQ9pZ2dLvCMkbdoYTm6guFyxeiqI2fhhkSlysc25fNZO83nfeCgQRJi1gemiPpYt7tZOtsn9UKB6NeifsWRkkyMT777v1DImZ1u9lfUWitE0OboAZV8cbaf7Yi-IENI8jEc9u7b7d-iJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=Vy37qRt9VMDogvr9uGb0YfIIAnC5unR1NoCJDPP2AOVmHraMw5h4xrksSmH2cLFWmjbNad81ZY3ZYV36n7CUqGxZhHlqwyYLzKDnMa9gj5foKbjHLO0kVHSExWhXlvWFut0JI7ptdYuNejNH-0RXvzn0acz1LL4yF-1yLthr-0KjJSG__lhp4sAvwQFVuKZAkD8_hLgJ-IZwoWh91LFwuCeDSI4k29_qRnzo7Jkf5WFvzxmCNYidhd_tpNatjnPBSScRRq7mCstYGgIiCkyp2XuGMl3o3K1xBZ3SDkzL8U9bEiSo2-Zp-rCEWQmJfYyilorsCfeY-AphBO1Kg0bT7ZMp0tL90Z82rgpVQDVCUIfiCsf-NR1aQiHmJxlXz5a-mMfREQRfj_iJLwKuQOrgM06nP3TQ71huw5sElH7LBidCHjI1RvAn0EiVgDEPy-J6ExAQpYZHHzALaAIdbP4DKaT7WvIEqANWTyeqXuBScedsOgiETkRgyaQMiV8QMHSMV-yyg3WLwugINzAzV4ZIWBPuInlFUCpBBzO2m1fHwOgrmsoMzWlOUAjffegWcAVtn3e1M-kemy-UFVotjIPCG9a7V2y0VKPTYWqNMLU1FXCX3qlZNG0QnChPSQpZXbiE24tIknsUY7AdFjQdNnNta1n8w5eIeSiPxYz8XsmyE1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=Vy37qRt9VMDogvr9uGb0YfIIAnC5unR1NoCJDPP2AOVmHraMw5h4xrksSmH2cLFWmjbNad81ZY3ZYV36n7CUqGxZhHlqwyYLzKDnMa9gj5foKbjHLO0kVHSExWhXlvWFut0JI7ptdYuNejNH-0RXvzn0acz1LL4yF-1yLthr-0KjJSG__lhp4sAvwQFVuKZAkD8_hLgJ-IZwoWh91LFwuCeDSI4k29_qRnzo7Jkf5WFvzxmCNYidhd_tpNatjnPBSScRRq7mCstYGgIiCkyp2XuGMl3o3K1xBZ3SDkzL8U9bEiSo2-Zp-rCEWQmJfYyilorsCfeY-AphBO1Kg0bT7ZMp0tL90Z82rgpVQDVCUIfiCsf-NR1aQiHmJxlXz5a-mMfREQRfj_iJLwKuQOrgM06nP3TQ71huw5sElH7LBidCHjI1RvAn0EiVgDEPy-J6ExAQpYZHHzALaAIdbP4DKaT7WvIEqANWTyeqXuBScedsOgiETkRgyaQMiV8QMHSMV-yyg3WLwugINzAzV4ZIWBPuInlFUCpBBzO2m1fHwOgrmsoMzWlOUAjffegWcAVtn3e1M-kemy-UFVotjIPCG9a7V2y0VKPTYWqNMLU1FXCX3qlZNG0QnChPSQpZXbiE24tIknsUY7AdFjQdNnNta1n8w5eIeSiPxYz8XsmyE1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxqzqXAFT5Fv3xNrpMpG5VLtD3mfkRK7BwhRUoR29n29Z0XsON5Jb2yFjfCeEqM8Co48-g5se7f6e0HPlc81fC-_dhgnxPAgF7FHOhYeJBFd-ofoP1w8IvqI3rrno1bdveopLccDfqqHx_NnSwsB1jQQgT2hDjp9ErRVyecqiniaICfvcxGCbT5cjFHpO4V8_XbxTvEzCRM5ooYvoWAvBa5j56-YzoB_qXar5xmcov3wbggWdci6hxsILwwiZvMAg4tjs-7pg-XvhOMDVd-YSNMZGTMn1iwlSPluakUPYYkG6sSJr9GZe8R-Jsad_9tv0UTa_YlS9Z3fd6YkbCAM0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBpLMpXMt6MyndUBz9EWvXzw7EWZwdPUIhv3gRgWcLUjdvJRyHUw0JdusI6YHR769wWZxjfojVJr3nc9CL4K_p8XiIY_Fzx2QcrvfAUM8mVSziETHdgXnCkJ0Ws-NHZhC8I54sg8y4k7xOT6URLQ5I85bMKYYQw4UZwLJchrjIdNhlPkOCNDdR2Rpe_4q8kySZsiLypdjJvagubpNwLS_ldK4iUuSxnslckokvS6U_1uUdB0cHl-TLmI6kR4AiSb1KHWqa-390fqPw_CA9jCfY231bFTn0Fcafi7844F_iCFvlM189Bti7zFtZu8kx0VIlJqHpLhJrjVvnSrN3PQug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyNfCRfinAuqmUd-NvWsZ8RmSqPfkrAZwdYMxdDAY60uiCYCVzQyJdnm00dFuhxXneAVU9UcO8ozSQHWxdG9ZXgc5cI6m6E-Qp1YEVc9KW4uBw5ey6R809cy3MAoPUJbhKGzm731deHxRX70qErAEyxtfWt5dpr9t4_MGfbhHlyJywL5yH11OUOX6wpVq8eHMs2eLKkONueSAl0XWgs_AhXsJzNB33s0MTKH8C_OT2jdsvzhvTuIS9y0CCpYfMMPFUToilD18gWckiOMGmPdt9LOzt-teVuzLS6x5020724yn-GjEy5u_swSdhw-lLBt_fMHyPTtqOTqcPHu1D2Rcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=qBmTUWINBQxjlAOonlmt6r5s-Yl-66e_GtVfmYBBqK3_7tZZYX6zw2n-Ru51NxaeRr7m4nA7mBGQ3k9Y1GDEfAISRn7D4TQXLj466f4NN8QUDHhaA1TSy8gl12quJ7lwv2tWnvCjLsWb0Rvm3suDEvmIQ87SpxdxwR0q3SGp6v4xYRoLfuhDYBnt1pkAXrKjbSStSs11eSDf_go2qB1uHIbDzSt4rg7V__ofUsiTVDUXm1KdMv3NrLIxYBH-J6L1zan-ol2EDHXu5rvJqX0rioA0eyk7gjArbh4-XNz9Kh6pW3bDT-f5mqxifohnJ_LCL4nWgQnyOnoGr_k3U4InSIoaavRhHgO4Bd6DxKpObdu1RK9pcinWSruah2_z8ZNnrepiCS-lA_7q8e1oHgcu5u3ZoCvWS_jSdzrJ3e6aqgESGnuy6miytqVkWkWGSt2K4x_3e5f4-cPBYsayI4T15VlNrDLuWPnWWxYJPoag8NumLZBbBPrp1YwBbWPXH4YG4eljYqwkTOz_mjmuk01qeRbLaMNUKuiwjZ3bMNjS6Kh90sID8GgMwxDKmh7A3jUAA5oEdrChWIZbG8gpxUvX-4vYPD12kH-61O-hf2o3QgX44p_lx5uZNJc7YVVB1Ft2ab6exI84-owAHBSou0nGVEMtZ1VjeI7BXetAGdcGcu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=qBmTUWINBQxjlAOonlmt6r5s-Yl-66e_GtVfmYBBqK3_7tZZYX6zw2n-Ru51NxaeRr7m4nA7mBGQ3k9Y1GDEfAISRn7D4TQXLj466f4NN8QUDHhaA1TSy8gl12quJ7lwv2tWnvCjLsWb0Rvm3suDEvmIQ87SpxdxwR0q3SGp6v4xYRoLfuhDYBnt1pkAXrKjbSStSs11eSDf_go2qB1uHIbDzSt4rg7V__ofUsiTVDUXm1KdMv3NrLIxYBH-J6L1zan-ol2EDHXu5rvJqX0rioA0eyk7gjArbh4-XNz9Kh6pW3bDT-f5mqxifohnJ_LCL4nWgQnyOnoGr_k3U4InSIoaavRhHgO4Bd6DxKpObdu1RK9pcinWSruah2_z8ZNnrepiCS-lA_7q8e1oHgcu5u3ZoCvWS_jSdzrJ3e6aqgESGnuy6miytqVkWkWGSt2K4x_3e5f4-cPBYsayI4T15VlNrDLuWPnWWxYJPoag8NumLZBbBPrp1YwBbWPXH4YG4eljYqwkTOz_mjmuk01qeRbLaMNUKuiwjZ3bMNjS6Kh90sID8GgMwxDKmh7A3jUAA5oEdrChWIZbG8gpxUvX-4vYPD12kH-61O-hf2o3QgX44p_lx5uZNJc7YVVB1Ft2ab6exI84-owAHBSou0nGVEMtZ1VjeI7BXetAGdcGcu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=T_Qwz0G20JwuaTC6KyvV1Rnc54Y8M8yNxNXSzzUgVxGajbk5Z80LxntssggSPUyXF8i8r8Z7S_D9pQv6YnRg3lisD5Ms2Hg7yfOR6ji-OxJGzfJOUs7oHdypiVcx0x0cSCI8oN0yUcWQFErHFnUJ-Zeo6VigN-ls646ND69UGiYEJ4wZaqLz-uicDwZ-Urb88uXAsR8vcX_CtijdPcASHsTQQQwysGwJMj3S71HY9DKfGMg1-cynhUWeq7_Kso3HIrbynZDLHtDc6NSuxFt6GbhFk5EQANVM7KtjMHXzJDA30Vya3UC4dvpWaly8hCNCWujCTZKUtrMob147JohwpymuXXYozRi_mXBBHdngFGr4zeiGESzUH7rlDp0yCYx_ReKb4do5_sXfeONVkh0wWa3JsgDbevCbV05Fvgc9lO-MJE4A_6Kj_hZ0H0f3kVkoFBdGRw4Tnh7KZVnKmjTNkjzNbr07wyfOFVk9jAe7OYeZ5fWOj0YugWDiRp9Rzv-tXrPV2ZWTk9Z-fj6Tg3C2l14x39lwLMjrsjJ-HRGdQ5GtEl1irrvyOcGJ2KjXGQSxKHmwutMGMwUhex4B59z0Slk-yJ83G_7NAh8SMAKzxHIOAjDo62BflHDXukY4yPZA-29KUoh0s6CfDG5GULqFOMSEYTyulTXNtJ1wMhi_ukI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=T_Qwz0G20JwuaTC6KyvV1Rnc54Y8M8yNxNXSzzUgVxGajbk5Z80LxntssggSPUyXF8i8r8Z7S_D9pQv6YnRg3lisD5Ms2Hg7yfOR6ji-OxJGzfJOUs7oHdypiVcx0x0cSCI8oN0yUcWQFErHFnUJ-Zeo6VigN-ls646ND69UGiYEJ4wZaqLz-uicDwZ-Urb88uXAsR8vcX_CtijdPcASHsTQQQwysGwJMj3S71HY9DKfGMg1-cynhUWeq7_Kso3HIrbynZDLHtDc6NSuxFt6GbhFk5EQANVM7KtjMHXzJDA30Vya3UC4dvpWaly8hCNCWujCTZKUtrMob147JohwpymuXXYozRi_mXBBHdngFGr4zeiGESzUH7rlDp0yCYx_ReKb4do5_sXfeONVkh0wWa3JsgDbevCbV05Fvgc9lO-MJE4A_6Kj_hZ0H0f3kVkoFBdGRw4Tnh7KZVnKmjTNkjzNbr07wyfOFVk9jAe7OYeZ5fWOj0YugWDiRp9Rzv-tXrPV2ZWTk9Z-fj6Tg3C2l14x39lwLMjrsjJ-HRGdQ5GtEl1irrvyOcGJ2KjXGQSxKHmwutMGMwUhex4B59z0Slk-yJ83G_7NAh8SMAKzxHIOAjDo62BflHDXukY4yPZA-29KUoh0s6CfDG5GULqFOMSEYTyulTXNtJ1wMhi_ukI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
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
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwy6VZ6Xh3HxImEr0LMimOzBBu2m56cdplWjAb6VLrA15wC5klmFLxBWFT850mH8JWQzmjpd9fmNOFf4waMzbqgN6ray8L2QecmnTAqZFgT9KRoi2125xEoducebtb18tLvdCt6kzSKcQASZZGxlpG_sw-asFqPLLU711SSjroMJxJuvFnmKuecWjeT82hDi0XAahC-S_b1Ipb22tLWPrdrTAKwCqUOTXLfZCD4QiAo2tuWCgCMXNatvinpDKGiLPJSgdjYZJzN4-F_WcUe3tef5n8FvfdWIUKkygHU0tCT_F_JVGDttcF4QW9vP880d3bKg4KHdkRqx3VokjHfJ1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=ooR6Ff82LtMsshmkG1x5Xo11NBWtuy09SJYifwX9HFFboJmCqvIm6_J1k9y08e9cBvHHbD_HlWUOY4P4PFHbyOSuLbW8LZ4EvAGCNemeXOe2jTvy8QC4dSr5NyPRdUMB49dK8HFEmkHzyUG2eqC5pibQ4tFJfn2yEKIYRXUU34ep4rjedEeY0jtZFfsSs_MwyI3tUAWtmV01dNF7phCxHlcRutzeS5OTDDBbNycwmvhY9VaLXLx8HDOiVaRV0VUM_28_5x0MgAEnFxwsc7bOUKtKQdVB9cSg3LO_r7kFiTISjMsU_wT8_NrTJW6G0vYY25WYoMpJGdkWIp8HBw5tt1Hq6skEthF_d4Y7RSBhUCfwnv6ZxyqDmGIGSlgzJfvB6D1ytM3j7Kd_V56nJykhhcuS55hN4qqG82PJnZJuHFIZLPV1CEQojRv0Nx2Hn1WTb1qt9EfGoa6AFGQ4E3lu94O3R-GuWblevQcQN4SKZxIS1qr52MnzVFO6qSfW-yiGQdLuF_isk66buP_4hDd3gEnxNEgmZqxmAsv0rwqKhBSQJFpoGe8eK7e6IwHdjexwK2dLTsS3ffGa_Gebk43k8ivx60IoHkaCLd-AT72wvmpodbO3yTMNWCiUjykR155RyCI8Q3ZNF_8VuR_2lv5eB30bFNJUOgxBIN6OxPv0R5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=ooR6Ff82LtMsshmkG1x5Xo11NBWtuy09SJYifwX9HFFboJmCqvIm6_J1k9y08e9cBvHHbD_HlWUOY4P4PFHbyOSuLbW8LZ4EvAGCNemeXOe2jTvy8QC4dSr5NyPRdUMB49dK8HFEmkHzyUG2eqC5pibQ4tFJfn2yEKIYRXUU34ep4rjedEeY0jtZFfsSs_MwyI3tUAWtmV01dNF7phCxHlcRutzeS5OTDDBbNycwmvhY9VaLXLx8HDOiVaRV0VUM_28_5x0MgAEnFxwsc7bOUKtKQdVB9cSg3LO_r7kFiTISjMsU_wT8_NrTJW6G0vYY25WYoMpJGdkWIp8HBw5tt1Hq6skEthF_d4Y7RSBhUCfwnv6ZxyqDmGIGSlgzJfvB6D1ytM3j7Kd_V56nJykhhcuS55hN4qqG82PJnZJuHFIZLPV1CEQojRv0Nx2Hn1WTb1qt9EfGoa6AFGQ4E3lu94O3R-GuWblevQcQN4SKZxIS1qr52MnzVFO6qSfW-yiGQdLuF_isk66buP_4hDd3gEnxNEgmZqxmAsv0rwqKhBSQJFpoGe8eK7e6IwHdjexwK2dLTsS3ffGa_Gebk43k8ivx60IoHkaCLd-AT72wvmpodbO3yTMNWCiUjykR155RyCI8Q3ZNF_8VuR_2lv5eB30bFNJUOgxBIN6OxPv0R5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZXsCbVVkpve3gk031BSD_SEN7mHUXcfW2Z15o-AnNXhMmPjDfQ6BBzRVvl_CRKxKpUALzCYOlW71KcAWT9HJ961wIcGZPBwqrCKRwr-IZwt49clNStPMbsXgbeD9qcktZ64v745JPuxZkAcDyuqKhlM1W8CMIuO_qVTsc9MZkAzBhdGB1gOVQzkQ1zpYNq81IEhJLEDGdDKWl6ggrGGVw7EmvF0UaUzIw92fCcSlPF3HpbEEMYLPA0b4ZDN4xliSmPriL0QYO8vG_UPLLKkTNKYfrbgxxyZ93AxT102gmWTxjuD1sW_35PEjL0nJ6jko8UVC_BONUTkrnAKa9Lf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFQS1nf7E74Ttq82pEsfLIrFuw5BxSi4Lpt2poArfTvsdoZ3ZoJJ6GhmW_sujX6BRZss10WqYsw-zcoz47tRaiw7rvCWzykKvXEnPZVzuJKNNObeh90vfxhuiTWnue3qeZ2HeTpST4i0E4g8T2x2ERLMyaKIgnWHPLFNhC3t1dJBm5r-SyC0sUgDUxBI5Qi0DBR0XHdcvqQbNB_M_LvfRGbGelZBRjsoEigIOyIPFMEkcp-9Ne-yisBqfbUi8w7rRvgXB5ztU_CdD9XvwRxZRaspjGJKleBO3Ah-h7JWyKR0ohn30SKAX8oSSEPr8u4Xrc61J1w5mUISqczHaYO0OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=JHKG2wbeW_tiOVw9WmgoFK8HixBELAMKOQ8_8ZF3-cQ4rNzjo1QJQ7-URjb4m8aFJbscHn_Anad0k_rZq5nnBRkOleTglOUcSC5OPjxT56kBMMLGb2rsj_mbrNdxoV_c-ReVYYBQ2prrPbnWLcq55VDHXTGXU17w18CltcP7o_e-YLcuGIkaH28by-AnJPVIAtjnxetErB2s16CxNpZUqfGp0Yo02edU_F_qYckOVosQ0Z9d2_u9xEvBzYqWfzg6s1F6kdu0Jehj_hUKkY5rrky4C-plQV7HO_ZkUq-xabRwopV3_7skv1-a1eEpxucATFhwRcC71L-9xvxlZRDY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=JHKG2wbeW_tiOVw9WmgoFK8HixBELAMKOQ8_8ZF3-cQ4rNzjo1QJQ7-URjb4m8aFJbscHn_Anad0k_rZq5nnBRkOleTglOUcSC5OPjxT56kBMMLGb2rsj_mbrNdxoV_c-ReVYYBQ2prrPbnWLcq55VDHXTGXU17w18CltcP7o_e-YLcuGIkaH28by-AnJPVIAtjnxetErB2s16CxNpZUqfGp0Yo02edU_F_qYckOVosQ0Z9d2_u9xEvBzYqWfzg6s1F6kdu0Jehj_hUKkY5rrky4C-plQV7HO_ZkUq-xabRwopV3_7skv1-a1eEpxucATFhwRcC71L-9xvxlZRDY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChrJLA30GUidyBg4CLyzs2e2OZzlLjjA5WjN7FiXS6wrJiJp_W2f7gRn25tUN4958vTK3q1daktysatq95W8anrXgwvahj1B0lT6feE8k87ViQ_mABmQ5R392HTzqsxXJkXtl-AGzvCSgtsbQROQmoKqlDYjgVUZ506S7GnupFYQnFqRQYXsDdD3CCRfwDdRsqx9GOj52N-RCCcbf73SIuiKPe0-Od30UGI5He-nD80EPpPUz2mDqFJPElc6xzABrPZ-JxxloNQG3FvDlrN4nAZe0cCVMgsCGL-8P3O6KcoxM3KlQIx3O1JTwNcSnXo13zVgwiWfEViB_CGo5lk22g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBF7929a9wIeCUUGRCKqrYq9uo6WBEdGDG_8Z78pQ31eSjrf6towa6Aamj8X5bt2ph2lJtmhHi0VMB_vXP35B__jS2PUxsdgs3PGbZ7S6ME6Wr8pi2Ylbwf2q4XGJjhgLZHe4Lw6xrpG0v3RXxp10szD3IFfADI0T4ccmAE3M9rzbQcVKQp1ORiIIG2J23Lrrd9eTIoNw3Ne3B1UHi2yEGxVkuLyRd0j7LUaQ-6bdKK8b8nyPFbJ4gU_VuExXGjprOuD72L3ROWBRb22szQCKTZ8JHqkhcrLlb76Xnar5tVpWJpXMa8wSsQi2YuVY72qWxK6FzPstx3NIQol4ajOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=fbaGU6L0AAcc999Oz_s0ANRoUUsEGPIPgvjTqrO5sPJcqNzn38A7wszH_m_uZ_3qD3m5Xk4NQza8Xo-0av2n3hrOqSgp2iy6O5Ku8E3o_ZKL9Dp9HkLPAj5YC0mmisiqygQWOHPF1-n1KDKYZD-kZF0KEg27qqZQSFqXhjAIt8IjxM84hZ3XUpETi_gTyc8Z_IuFHq0qZMy2p7eWwFZ-IiVyTZ6Ig7Feg2WJco1mapUuhJG5aBAyv2RgNfqA09JfEPKGlwX3Cx4FcLi8hBn3_PTLoicypLOKacTQmQf3kjr-wD_ploA-UMtbhnXOCUbnYz9cWISwIYoIx-1nPq3EdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=fbaGU6L0AAcc999Oz_s0ANRoUUsEGPIPgvjTqrO5sPJcqNzn38A7wszH_m_uZ_3qD3m5Xk4NQza8Xo-0av2n3hrOqSgp2iy6O5Ku8E3o_ZKL9Dp9HkLPAj5YC0mmisiqygQWOHPF1-n1KDKYZD-kZF0KEg27qqZQSFqXhjAIt8IjxM84hZ3XUpETi_gTyc8Z_IuFHq0qZMy2p7eWwFZ-IiVyTZ6Ig7Feg2WJco1mapUuhJG5aBAyv2RgNfqA09JfEPKGlwX3Cx4FcLi8hBn3_PTLoicypLOKacTQmQf3kjr-wD_ploA-UMtbhnXOCUbnYz9cWISwIYoIx-1nPq3EdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=uHX06mssiOwkB44M3Qb4jtTSYRszctPFwV2CWZeb2jBeX6kfb_MF6QVNLyDL-pO8J6GB87JjJDCK1_IqDluH2KZDL8euiBQgwqW7IwqOTNEynr2RZpdKe1a3p5RDRXbBXP-3VKV2Kb1vlmSCWF2YiDD-P1EO38sJgoc3S5kussAUeJSRrpzmaNEzxZJCFjUeiBuSBkS8D1WRiUQh07YcKbaLF7mtwBYg9KoTHnmWzY5fPKXCry5ANJtmIaDMkWk2hZCwqtC8NsX11jc-2R0QCuH-lBFCAdZT46OpGQse2Czbr0wfdDXVsUnWr0dPPTeV4RCrcrljrancReJJV7R-WpHGHIl8hCRaD3CBpIJsL9HRsIAUQbFhr_nVf0tQReKF4ziC9WJD_AFwdQh1E_K_C3WgAT9iEK05adr57Lzbe8vkylEsO8iWwTn-lCWcN1Q-2KwV9nDYm0YyiEtKxS-gCENOUavhjIB4AEW_oFoxOZuQy2GpCV01wxj9ARrIpEiXBLznT2M_i2sd-AfKpPZ16zguXDsXCv-3R_Y4Cpvxs4EVPQPXtvyw4TKzFel263wiph3rqHsmvPobQbBAtbWL5W1OBPW1nMccu-lUzCL7i3BBBQTYzXpX5ZwKp9FxAt1soRVDeRxJerxRctvfgOddqdCGzSxJxjuNyxkYV6Zrn50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=uHX06mssiOwkB44M3Qb4jtTSYRszctPFwV2CWZeb2jBeX6kfb_MF6QVNLyDL-pO8J6GB87JjJDCK1_IqDluH2KZDL8euiBQgwqW7IwqOTNEynr2RZpdKe1a3p5RDRXbBXP-3VKV2Kb1vlmSCWF2YiDD-P1EO38sJgoc3S5kussAUeJSRrpzmaNEzxZJCFjUeiBuSBkS8D1WRiUQh07YcKbaLF7mtwBYg9KoTHnmWzY5fPKXCry5ANJtmIaDMkWk2hZCwqtC8NsX11jc-2R0QCuH-lBFCAdZT46OpGQse2Czbr0wfdDXVsUnWr0dPPTeV4RCrcrljrancReJJV7R-WpHGHIl8hCRaD3CBpIJsL9HRsIAUQbFhr_nVf0tQReKF4ziC9WJD_AFwdQh1E_K_C3WgAT9iEK05adr57Lzbe8vkylEsO8iWwTn-lCWcN1Q-2KwV9nDYm0YyiEtKxS-gCENOUavhjIB4AEW_oFoxOZuQy2GpCV01wxj9ARrIpEiXBLznT2M_i2sd-AfKpPZ16zguXDsXCv-3R_Y4Cpvxs4EVPQPXtvyw4TKzFel263wiph3rqHsmvPobQbBAtbWL5W1OBPW1nMccu-lUzCL7i3BBBQTYzXpX5ZwKp9FxAt1soRVDeRxJerxRctvfgOddqdCGzSxJxjuNyxkYV6Zrn50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYLvPiP-dsSfphJpEq6LUYMrN6IhZQSjzb4QM0QpOnOj6c6GaNFQTvFgx_rlQMyN81Q2NoBddGuVE4zd_tVl-48vaNgxAanxYMSL7yUykuG05AFJ9bswwdxjK1o170B-prpDZoFIynpWZYvC6oryoJGXNAjXzQdfOc0d5yN3puHd9DqcUYLLYv81CpIH5hhoMSz-SHMTJHHZJAVKTlt-pJqKQokPetoYUcrYXJJYYVem6d1jOIN9amG8dOJJiIuMES2ySHOdyqWka_kWfDhr6BHNVf6lNF4vfuhDP_SZvFIKvCqgknCjT1EmzjnOsBnNa0KiwVgkLR17k9ZxiK0-PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrjyDHjRp_JwXUZgP_JQIuc3x_5UetFDlNHDrAFLWrZmQWOc0A_UoF9hOVrp-p6MCH4qjQesQW_2T_MLrOvKojG9cMyTnzSrkmhnTMqQz9lYgw2OKyEXjLHis8DDvTP55zAtFPXZE8WkgmqARFBHkR68Ek_QxZoborAqXDW0B-DUi3JrOMKMUMqt9taONOx_RKOuTn06UDr-RMWMNw2oH_yqyIPRxh-HmSmhxfD0tZH5m_U87pqtnR0nt2ui9Wa96ktMfkgo16kpp6HzevDh6qJiJihtWg9kom4cnKnRAkPdlF0ZmAYT12FeOsgCgqtJCX0FHr9L1bBv1u3Pxh5fDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-RSYXz3BaPHfujuK0cH5B4xOoFt4dT_C5uY9t1ODnm12m_d7qXbabJfzKrMDlWQ4OQFIdhNSMqtumfw09AtcofIqjLI51TqVB8katzeqgpRXkRqYsZMSWAYaQq4OOnEAAz9kidrE0Fi1eokdY6DGvzo9bDEi4C-GoYuEOG_6heXiht0yfcj5CuPSEZ33a8MixBhqUomBXbXItUM3o-fh_7r-PaBXsTL93owsBhPL8XCkSqtMPxUd4yhq7kawfNfcYTePF4f2HkeEdh-MbTCP4ETxDxAchtruHjAzbBszgQKa1Cv3Yiedki_2TlsbN8314XMNaur3eBZTegpCE0dTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=UxM6be0aCzPTJcQ9urKa19O0fEQPjC8Tk-mwxVO2dmuqUX6cBkUztXZtcEdwhkYTOCopvUtAk5Ot_obymnobG5h_EcGwt_mdGpWYpOBMkClfjIsY2k_NlOofzwphWnPJQMiOohiKEOpv2MF1WyaRIXgLXsYAD2UF0clVh-0PHN9DlcquZ44FZnECC7ZMHCroPErjJl5u8dm6DyZq5486_ZhMXcLpxAKTIb_KCVpHjWiV9mNcATIa8i_T3rSCfYeL6VlquqXNbRRm-SG7MH9ZwmghzMKdqOdoOn8TwxXXuGIo2rkt-LFK20BuGbeELwPvNnqBGVcnI-CZ43wBY_kOZKrprZPpxd0iI0DXcpDgEyjAl2mrjisyXelsRk8uf9skMEE3jHBuKn3kFzsWka8rEwcx9EQgyCplfW776bbi-ZpNvag44TpqrXOsn4Mc6BpcujR9-Q4v18QY4WINtSvNL9LlKd1fxvNbxK1MmuPi0giM2HTNJ7e2hnvh3wjYuCHQNsyqGz5oG3Ckvn1nQlHeBrtpjucnc9n6UB06MFuaO3OibjlHjzd4_34_Bj-_iuXSyWbRV7MBy4qEPmUh4uVD-IE17hR9U3BuHOL0YHnaU5EtCxPruGM-K14kqGbsltJ0z_7NV6fh_C95dHcaWKTuBGi9xyjpxbHu-qR_dVjHPFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=UxM6be0aCzPTJcQ9urKa19O0fEQPjC8Tk-mwxVO2dmuqUX6cBkUztXZtcEdwhkYTOCopvUtAk5Ot_obymnobG5h_EcGwt_mdGpWYpOBMkClfjIsY2k_NlOofzwphWnPJQMiOohiKEOpv2MF1WyaRIXgLXsYAD2UF0clVh-0PHN9DlcquZ44FZnECC7ZMHCroPErjJl5u8dm6DyZq5486_ZhMXcLpxAKTIb_KCVpHjWiV9mNcATIa8i_T3rSCfYeL6VlquqXNbRRm-SG7MH9ZwmghzMKdqOdoOn8TwxXXuGIo2rkt-LFK20BuGbeELwPvNnqBGVcnI-CZ43wBY_kOZKrprZPpxd0iI0DXcpDgEyjAl2mrjisyXelsRk8uf9skMEE3jHBuKn3kFzsWka8rEwcx9EQgyCplfW776bbi-ZpNvag44TpqrXOsn4Mc6BpcujR9-Q4v18QY4WINtSvNL9LlKd1fxvNbxK1MmuPi0giM2HTNJ7e2hnvh3wjYuCHQNsyqGz5oG3Ckvn1nQlHeBrtpjucnc9n6UB06MFuaO3OibjlHjzd4_34_Bj-_iuXSyWbRV7MBy4qEPmUh4uVD-IE17hR9U3BuHOL0YHnaU5EtCxPruGM-K14kqGbsltJ0z_7NV6fh_C95dHcaWKTuBGi9xyjpxbHu-qR_dVjHPFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBhqu6vGoavYf-TjIaWKdt8GIJxrdAdVOKbQJHuWV61MeAQZGrXoffRAMxVlNV5LJb9t0kgrvAIroZankU-oMl62odynYWFXuacxs6rycR-PO2m6bIM70Nn-oFpnERiC-CiN-eOmuy3W6dETD3wvROqUi_y9Yyx8K6l2ZBPQXfovtpAVg6o17EKeW6s8bRrW0UOINcmnHsRueLqTlXeNjmWBCmc7aQwGvdWMP-f4iC_3HLZNjQJykphbH79QIaqx3IaD3P5vV7cv1_owvjH7rRA3kIcH0cwgEnxqSrqh--8giQjUImN3qEXTkwFZFAwEIz9oMp0yhrMNBQebM0wjrkw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBhqu6vGoavYf-TjIaWKdt8GIJxrdAdVOKbQJHuWV61MeAQZGrXoffRAMxVlNV5LJb9t0kgrvAIroZankU-oMl62odynYWFXuacxs6rycR-PO2m6bIM70Nn-oFpnERiC-CiN-eOmuy3W6dETD3wvROqUi_y9Yyx8K6l2ZBPQXfovtpAVg6o17EKeW6s8bRrW0UOINcmnHsRueLqTlXeNjmWBCmc7aQwGvdWMP-f4iC_3HLZNjQJykphbH79QIaqx3IaD3P5vV7cv1_owvjH7rRA3kIcH0cwgEnxqSrqh--8giQjUImN3qEXTkwFZFAwEIz9oMp0yhrMNBQebM0wjrkw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oY_dEN9_XgG1NPKEc9lZIpMe30RfSTESzUn2up45ThmX3jC8RERAYRX64iroAMljkUrz22_ZfqdyCN8qzXj5fvvUgX7HxrchPUYdNIlwwZwy_PtmbyySrDJbFuMN_jLxMdc1E6jbOIy4__uXvF9fEbIduO-xzeaVBdYz76dTaOtJiwzd_vJqHzOdBkYRUF24TQVsNwaCkxP0Lrkgp0D52rxKMMo_L6gWiwVzPRzhOq4UcY1FSte9fvsnB1GSXcY0HJtTtqpMy9Y862QEnT7g5-kXu8SjR1DqQIoFAKAlpfd5lu8Jx5yQB2OYd51i6Pe8qRQVfUUcGxT_oryXqasOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
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
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVuiNZC5ViXWRSuL5jtMx0gmtKlYZgmdEhUiV6Iu7lGZZfnURN8Q9oVipgSSyT3yQ9vdJyAC2mCLgmexlJ2wuMdGFtGT9z1utqY270WCCai5SD4ROEAKZA73iAVRMM9dHoPBFUFwsUUx-AaFvQUUunVb0idFgsZjbCCG5SRkt60atDhwktAJW5ZviC_zq44Pt2XiTQmHQBAm9Ijy2u7_YdS2FzcFHgyxlfKsB1s0PkN1IZcPZW638uo6tOwFCYByr4_ueoREp0Uo8rnJZiXiZELx9Pc-arvvqIPn8xrGuLxDGWtz4j0hG34PotGkWhnCHQJ4231U0fIuA6kVCryxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ux722CfX5EcOU-8tWRbFqQ4K5f4SwcTta-SnicKnZTsgoZ6xyOLsVdevrxbfkPkEPISF8HKAlr28mIRhy5d0ejwqlP8FdBg3Hm1sKl-mLz2A3baPr6qGSXVXUbYvoJFvsdex5LyPSc7-mL0-pQeJ3jkeRS5AlieXDtYRkX7kOazMFP7rzy5lO9WBPwf0knorjcP-hJe1NaFWytMKDpQ4lXQUo8DgsqiEJBdsa1ns9dm-1XwfFbJc-86snsepM7HdV6dqKGi560FqWuZExBu_3zHceSaiAVlwCtpQUqUP5dQvR7o4sPQEA1jFgIRSKABrnVj07diyA3rW8Z2ysWYpCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjGc91LtEh6csI5aK0RplPs8Wf5IEpAbXKolgQoSLgS6Lbug2A05KxNr-rDhj438T22DvticQlfQN42HiDXKbJqSaIQx7t83mhyfftxYTpnlc3QgnNnoZO9hsj9VfdTDToB9lFvDySqDvKwNToemBUaeoGFFOwePwyKEG6Kc48mZrEW09-IJ4fCj2UKTeMtcF4gn6p1iEaX9CJICU6-XGcQTyUvqs_p5osRGeZKXgIr4eiF5hRp8e0A-iUNzEAlyEvVGw_-K6jhmttdXonZoerSXcXQ7d4BlRBKettggU2z0ejIVDJDJRZlSPwW_PpKSa1rOm-ySMaXUGEBEPQAEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueWV0-y_CwCNCAvf7LGOLTtKzGFlI3vc_c8ZNgsoPRJOOdh9X4hhXVi797afoW2n4oHX86R1S1m1KXLCPadOAPEqfKdtNaXTkDLrBNVTfA0C2p5lY3HOVWhMTtR_UqJLC_14yoFiQYBlLw_T_8673fE0FohjuqmBKLCaINlSr6qX8EN0y9D2j4HBXLez4FsCNYzDjsuYK0G8Uh1XEjejmF2g76Blb0cHjnX-fJY05w6AN381vp5Okm2f9bYb7tCBhtAYccReRN2FOyyOIohlyiPq9qDUDUaLlcy8uZ2ebWOTos0NqbchKJpPHsSyLQDRLmNFciUB0htPz-FSHwcl_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
