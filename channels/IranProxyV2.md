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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 20:07:52</div>
<hr>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 978 · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MilC0Tgd3UWvNXqUaN4KnBaMqnB6mFwxpWrtraJdt6ubIG-QP8cBvKFzH6qZ0dhHEojW8P5BUXwNc4KoJRYI9z2HFM1vETvJi75fc9Cfvq-VDR2SzqDjeyscfH4e2wuOsa4rhyrPhdSAQ_OcYpN-FLruIAdjDHsG0A-3m_xiavN1Jp_0dtM5i6kCqJJP-noviKQdPetPKQQ9pZ2dLvCMkbdoYTm6guFyxeiqI2fhhkSlysc25fNZO83nfeCgQRJi1gemiPpYt7tZOtsn9UKB6NeifsWRkkyMT777v1DImZ1u9lfUWitE0OboAZV8cbaf7Yi-IENI8jEc9u7b7d-iJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=uWovU9ID6NhDNGToVQYrriwsY1hCm_fADUQNMHh7D_9RqW6XvXxOR6SQUJ1bKO3z5ryt5L3D7YusA5d-SjKLxCTT7e7ksy_kxCprZT0h-Y1lwFmRWFQF7qye3iDhqRVR_N8cCVVPg7tZGd8ccvxXF_wwD9QQvE9dy1akHgua9UbubR335tNii8P4piy0eEXCNnoPZL9PB0m4vHl4KZGFvh4roVf9366vGUCcS8BkUOqKz9jFfZZStvaP3pU05VGvDLN5YpjB44IjVfEin_bAgylX7EmZHEcM00RAXknRiYoUzx3o6qmzOZ460z6oQBdQldGuUFWjfjIE5PoyhVLPxgddsF6gRUVVVwSc-zzmFiRI4dkQ2bn92BKcdN7g60C8pJw8w7MUjTEz-P-iMmNdnqctd9TReuqfXe6LtLBBwDjIBcZR5hCL42t_tg0K7t-oO0xBfqbXVdS4EYHDjLvRImo1umL28BCl3nkgFU4jKRT11q6joBzjh-xHQzqF8c_qtlHrqR5dJSpYgN044BgnJ-jlNB3d-xEEuNp7JX3MdODySA9JJMnQQ3-aHeJJhXNEHHFUypgM_S11OXjizjtZPEmFeZVguetvuDJzjdbU2VCGwCkWS1qPQBk1NAQh9Ofa0Pejv5d5iwouYrKbLbuAxLdryEaVIP05-MWdeS7WPq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=uWovU9ID6NhDNGToVQYrriwsY1hCm_fADUQNMHh7D_9RqW6XvXxOR6SQUJ1bKO3z5ryt5L3D7YusA5d-SjKLxCTT7e7ksy_kxCprZT0h-Y1lwFmRWFQF7qye3iDhqRVR_N8cCVVPg7tZGd8ccvxXF_wwD9QQvE9dy1akHgua9UbubR335tNii8P4piy0eEXCNnoPZL9PB0m4vHl4KZGFvh4roVf9366vGUCcS8BkUOqKz9jFfZZStvaP3pU05VGvDLN5YpjB44IjVfEin_bAgylX7EmZHEcM00RAXknRiYoUzx3o6qmzOZ460z6oQBdQldGuUFWjfjIE5PoyhVLPxgddsF6gRUVVVwSc-zzmFiRI4dkQ2bn92BKcdN7g60C8pJw8w7MUjTEz-P-iMmNdnqctd9TReuqfXe6LtLBBwDjIBcZR5hCL42t_tg0K7t-oO0xBfqbXVdS4EYHDjLvRImo1umL28BCl3nkgFU4jKRT11q6joBzjh-xHQzqF8c_qtlHrqR5dJSpYgN044BgnJ-jlNB3d-xEEuNp7JX3MdODySA9JJMnQQ3-aHeJJhXNEHHFUypgM_S11OXjizjtZPEmFeZVguetvuDJzjdbU2VCGwCkWS1qPQBk1NAQh9Ofa0Pejv5d5iwouYrKbLbuAxLdryEaVIP05-MWdeS7WPq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6imHQaboyUrpANAsyz-anz2Tls0EA_Wx3LbORNmarONl_0PezflKMEXBRHhHOVVkT9pCyeXGYke2gXVdd3oUffj4ceDk7lzc-HdsdZoDL5dvrTMs6OPcd_0sJxO2WgoIZT6HbT-XtJymFe-iybfJWlGuQfclEb8S1lnot8AuL316USaOH84SzZkcey57s4M301PGVKaLhwXGLZb4utybBaGOrhChOvNzMTr85K4SK-7UwWKPJteEFX4CxMQ3wB1-PdCu1lX6024iRecopmx-cnFyDmpm8bC_lIFB3ujpmUn8zqQKLOTx1yDQ5hmcFn5H_1PePzb8kj9dBpnCy4XfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX_qDwn2FkNpOlsmT4rI2X7G6NIzgRGXqenRQ2QhvA_oR_AwcZ_5_UxF0H8_EH8Yb7vQy-1Zp4SRe_e_dS8KUG3Ial7rxgCw2QyEGjGH9CmAlWXYx2hgKtvGUeBKVR4kGBkQBZCnRZpI38ZY5sBr8I20zUXKluOfabfg6qhMoiR00C67ajPnBI4X9quFaCHWMfYwW0DjpAb09W9IOKp5EwHH7KukvXLWlY3DGSjZqITkXTo3Kb2juOsViCVF2UIQ3-z_d2V7mNys0IUYCDqfu9VR_yoye0pKiyVJgmrWYEJarEXAnNqiu0KbB1uJP3NNLsW9SZZirrnv09MOKnCc2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpOKmR_n9lLSKpWhhsVfAUCGdKcgdOxDM0A6CpdM4pbk3xgYM2nla1Rwg0q3dlVrwTePf8iV78o4nJGm4RcCXIT77OlPuq-CNh7gP7-kL9eTUxvm8ESqwXVJXT_wUubIjCNzOhYbYO7h6XId9BXFX-quuceuTfbeDyaP8k9xCH-M98ZjIHcUsLmsV0_bsOZ52gUwveMdnH0VOWM9PacztoMuy0_sDS_sWiK_y1hmOF449yFd3XjgrMqcIGytSuqpYSaJg0pfuaoJhNyQ_ZMrpE974TZSHTDRw17RaWp4ds7iQC79bDV2mBdEhDvuQT3fC9V3jZwwlkf7eE-zX35b0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=YAdQEPTmOfyKh1jjMtDuYEkcVjEuZo9guu-JSF0YRhBZFk0UbI66sj7RsMVj3e2M_z6OTlOhzPi9iYUD-3hWLzLqkIWmOvLGfWYhPUERlRKS8h1D54m22T95QU-i204m3T2Xf8o14GYLG3fXzn6CtRtXPWozu5icVVlcg1KrqjMeRWExHS-6E9K-C3byRvKgdU0szSWSb9RWZnrV7UCYJa6S2t2mAHf9YXN9BYycE1GhDPGdeptcst0mTjO8VJUrPAHZbDB6MSUV835Orc8IzdV5HVya04cjvWmF_1grcAI_N5dM8oGXIJ7j8G900t3htR4U8JJNYJ59cqoBc9gRUAiR0Ci5bmhq2ov7MmmDWejsqGSB1C4IBmjYHkV8NGfNQawSLsmQb9dgGxyithzM-OacBsJlbfkP5QdD70OhoxMecJqu9dy5iHNQx4sG-_8bmBIXRJJYQxVsANOtS3H1aggqSsqk8Wc-hOOZzONSmcNJ8WA-nKgrIncyv7e8ixTuZwk0zKgVOIuVTYnQALFv3CQaGO_E1x6d1UJ4fAyTTpOpn96Knl6YCgnHXosspGA9ynVGsAm-DW3c1KaoV6DWXeSgbuFK1BqgUmQj_v_LDFpMxl3y7zkyjHXWD10pHijeGEERCt5yhINSTPn8YeD2iZWzqAKaXdIzvg-7LEYKlT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=YAdQEPTmOfyKh1jjMtDuYEkcVjEuZo9guu-JSF0YRhBZFk0UbI66sj7RsMVj3e2M_z6OTlOhzPi9iYUD-3hWLzLqkIWmOvLGfWYhPUERlRKS8h1D54m22T95QU-i204m3T2Xf8o14GYLG3fXzn6CtRtXPWozu5icVVlcg1KrqjMeRWExHS-6E9K-C3byRvKgdU0szSWSb9RWZnrV7UCYJa6S2t2mAHf9YXN9BYycE1GhDPGdeptcst0mTjO8VJUrPAHZbDB6MSUV835Orc8IzdV5HVya04cjvWmF_1grcAI_N5dM8oGXIJ7j8G900t3htR4U8JJNYJ59cqoBc9gRUAiR0Ci5bmhq2ov7MmmDWejsqGSB1C4IBmjYHkV8NGfNQawSLsmQb9dgGxyithzM-OacBsJlbfkP5QdD70OhoxMecJqu9dy5iHNQx4sG-_8bmBIXRJJYQxVsANOtS3H1aggqSsqk8Wc-hOOZzONSmcNJ8WA-nKgrIncyv7e8ixTuZwk0zKgVOIuVTYnQALFv3CQaGO_E1x6d1UJ4fAyTTpOpn96Knl6YCgnHXosspGA9ynVGsAm-DW3c1KaoV6DWXeSgbuFK1BqgUmQj_v_LDFpMxl3y7zkyjHXWD10pHijeGEERCt5yhINSTPn8YeD2iZWzqAKaXdIzvg-7LEYKlT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=cE_x6Mt8VoXR87u200f_16eRmtD_OGPNA7Tui418pAVmw6E0Uf5hwCGWvRiiYKvDcQArEmNNS7qQQSEHxUJRyQBm6-uhpbqjvi1iJ8wnkmbKgWKgJNAJnBOlZCXD_CK0JucP3hsFF2vBOQR8kvQ24oPG0YF-YRa0X4L2Ar4JcpGljjue9RjFlrw7RSYVEtDailjPIFZHzMZQRTtC0IJ4b308s_1vbc3KzjXEwZJyMRJfKNxFNRProRYtCv9x7MXBf336agKsvfhnX70W4WnWPgzccH2_TOq10HDUSkTnVe725SS4gVszCkrNnTXGWnDKAFQhJsO64-G5RLduFglxY5ecgjOGcKXCYvqyXT1G1f21buNux8FXie1NF3bMD_FpvnhuElHRuwGhS9pAMzp7-veiEyv8z21p3SVe-WebZ_kUnw7YmChXjLKQ-yj6WCCWlYTeB78KfoVsYdw2wOp8XWIyD1xiwLsy3bGggTdmLkhg-Ln8qNk-wa_ZCnd2CEUlM0H_FinCf5dziXvC6z9xe25LhvX6MYqmEjx4oY-3avMHQONeERJQ7TeN5HyEM0Cd76BcuzPryjqyJDUay0pdGNbLLQ5n5CWpvzqjbl9qKrSwgLt8YqUmQNPr2Lw9LgXaLq0SzbLcT5hixpA13b9LMM-VRKCECENzlivQYxcWt24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=cE_x6Mt8VoXR87u200f_16eRmtD_OGPNA7Tui418pAVmw6E0Uf5hwCGWvRiiYKvDcQArEmNNS7qQQSEHxUJRyQBm6-uhpbqjvi1iJ8wnkmbKgWKgJNAJnBOlZCXD_CK0JucP3hsFF2vBOQR8kvQ24oPG0YF-YRa0X4L2Ar4JcpGljjue9RjFlrw7RSYVEtDailjPIFZHzMZQRTtC0IJ4b308s_1vbc3KzjXEwZJyMRJfKNxFNRProRYtCv9x7MXBf336agKsvfhnX70W4WnWPgzccH2_TOq10HDUSkTnVe725SS4gVszCkrNnTXGWnDKAFQhJsO64-G5RLduFglxY5ecgjOGcKXCYvqyXT1G1f21buNux8FXie1NF3bMD_FpvnhuElHRuwGhS9pAMzp7-veiEyv8z21p3SVe-WebZ_kUnw7YmChXjLKQ-yj6WCCWlYTeB78KfoVsYdw2wOp8XWIyD1xiwLsy3bGggTdmLkhg-Ln8qNk-wa_ZCnd2CEUlM0H_FinCf5dziXvC6z9xe25LhvX6MYqmEjx4oY-3avMHQONeERJQ7TeN5HyEM0Cd76BcuzPryjqyJDUay0pdGNbLLQ5n5CWpvzqjbl9qKrSwgLt8YqUmQNPr2Lw9LgXaLq0SzbLcT5hixpA13b9LMM-VRKCECENzlivQYxcWt24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
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
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4Zm5152apmAhkbmpEK9MkxUdepO_vC3sXznMh4MLx4u4vZIFACaYp9Dsb-3s8xd9AAMWSf53NxORzm1tQ9Bwvzik_ANkw9QSUKkMAokeEa861Pet3w_zpJ5lAxEUCIzg6XQJqAVGZPQtaTWLBNoeYWQjxOKYEOEhTRP2PcJoFyn-RZbtot4ZUJc2_y0NuA-Uxrmo6tD9slrqVcM1aiHmoiM1WgaMPfuW6j4K0klz8UNXvvUaLkPLsVKW2TtravaZxfiRVo9bPrCGEgETlPKTxDOnohqb0BpEbkYPaZbMzO-KtAmSXmzfdL6wTX5n_Snk5XTSU3Bfd1LicNCjMJ_sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=ZygU7FlSHiGSbmhIWiaxHBffGXkbuxPtz2hKQcWus86IFMg_fpirMX9nAgLkwC2MT4SRIPMKzvauXGGbmdDDXeAGb5_WK_v3ig0h9j3f8SO0vIlHVzv1tMWn0QlrQAV6wxEG_jk1wKm-RaVGS7tQOKTUy1NO2F85W4-AQ8lfpipb9ZhDNPT5DasolZDNxZsWkGcaszrattCKGw-lDGf9CqTXoux3RwP_5oW8Rkw3qqv94hB142Hb4HVEDRGyNGzo5AHYCe0tVw087wLQMVn8vzOh5K8shIosq_j9lBDBLSTspq5MhtO3QSlrX0TTBwm9_zzaRO0aJ8i4xXCChzNZpgxr-gsZaEjrATb4FDm2puP6azW-TFlWZiCDahKKSqEJeFJpkcbMwIkWinuteUMWqOGPXOfwr23AiNLvisEGaKNsVDESFuSXtWu1KeG_3U2QDBpA22FRoQdL354EtnDagMbxCFkmcQ0D_QL2PIgzLrLquTVF8kyQyAqp-vAJClhVHJmk1wi-pEN-d4ew7gXgmMG8FllucITnpFFteoV0mL7qxLdR81HBOpodSXhncxaoBRXsAXm3HIVXkghns0kp8Q0r2ZdzjV5puCvOEdISAU7wLQ6ntpDzqzUNnvHnm3FBE3hRMpz6aGzEmRFN2wxiJT8z0cbmXwAN2HbbSP2arbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=ZygU7FlSHiGSbmhIWiaxHBffGXkbuxPtz2hKQcWus86IFMg_fpirMX9nAgLkwC2MT4SRIPMKzvauXGGbmdDDXeAGb5_WK_v3ig0h9j3f8SO0vIlHVzv1tMWn0QlrQAV6wxEG_jk1wKm-RaVGS7tQOKTUy1NO2F85W4-AQ8lfpipb9ZhDNPT5DasolZDNxZsWkGcaszrattCKGw-lDGf9CqTXoux3RwP_5oW8Rkw3qqv94hB142Hb4HVEDRGyNGzo5AHYCe0tVw087wLQMVn8vzOh5K8shIosq_j9lBDBLSTspq5MhtO3QSlrX0TTBwm9_zzaRO0aJ8i4xXCChzNZpgxr-gsZaEjrATb4FDm2puP6azW-TFlWZiCDahKKSqEJeFJpkcbMwIkWinuteUMWqOGPXOfwr23AiNLvisEGaKNsVDESFuSXtWu1KeG_3U2QDBpA22FRoQdL354EtnDagMbxCFkmcQ0D_QL2PIgzLrLquTVF8kyQyAqp-vAJClhVHJmk1wi-pEN-d4ew7gXgmMG8FllucITnpFFteoV0mL7qxLdR81HBOpodSXhncxaoBRXsAXm3HIVXkghns0kp8Q0r2ZdzjV5puCvOEdISAU7wLQ6ntpDzqzUNnvHnm3FBE3hRMpz6aGzEmRFN2wxiJT8z0cbmXwAN2HbbSP2arbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGGd-s7JgTRmC5qiDhKn5pZuwSmPgdglWa7RtL-su8OSqSoIzyGnMw2occ0nNsTWGbe6XkD0POSByB9MssijaKy83KuD0lSr8EzLJSrVh7kvfBBtoNSXabwGZApK_DcrIgHhi0UaoJvmKarTLI38M9FlTfyLiVzfFeDX3sW-MJC_Gas2zUtCNAdf6_hykzfrFV4kcQ2bhI3BWAA1R4s7X2GpnF_Q9pgbnm8R50Mo1TWlyq0jI7DGX4XR4PbsuLLDL2AUwmCgFMCZCOPc3AO6ecJ4HIQQn9VBG5pMSO7sd-ZEp3ZeUXBmCvlLGWCysYk1tqmrgBC7pRt-FhHCWpJDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXFqjvr_XpcH_Djn__u5fJ6Szmj4Cs77Zpxm3Mcwg0PjLIopoqt7jHi683KfWer1O2JgG8fZVWP7SBEuqfGTt0QRCiY2tqM91y9GnshaBd3Y6OJ91ysw7RP-oYsEzI68S9TWcsjmtG-d3I0NbTz6xRzHCQdTGHYkHTfFy-DUhM83vVyTB1rowI8FWHRnMXoaS9DmEPyIOKdDQ60GOKKNwaL-_S0jYtVPC9QoavqHE8Hgv3xpOve4BBgYNgi_Je77Rno4P6AwkPZrbTjt_NE-JYf2QnGOzeCNkOzYz6Grt_BM2SD-dR15iabOTb0q2qKOSSPksAC6_gQt4wF6yNWuAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=VB0Jqju7ZCqoSeOKhSDKCYm9-lQyLwE3rbMpGspTpAGVSriJgS25k031ySbJCb6wqmhEOz7t-BRWdgbS9AyYMz-K_-BIk8WCUwabYD8sIpx5K_N1VXQLSOGOe94dsGk6uJwf3NZrDV0IsUi3esCzcfy9zgos9e3Xg9WNwMcIws1AGaBWjGzjshJYUR1Dfsw_Zfx3mrtsdLbWA3RrkE0O0aPGSkMNeZRFuUByHkiV_sorGonZ7Rl2JAkvbwUxm302hY2o2A8DIo7mLZ8vl9TsObDWNaTpFHS90DXhYgihB-xftEdQHIbuAmHrNSpB-ad1XS68QiNmaZ0aSOameqleyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=VB0Jqju7ZCqoSeOKhSDKCYm9-lQyLwE3rbMpGspTpAGVSriJgS25k031ySbJCb6wqmhEOz7t-BRWdgbS9AyYMz-K_-BIk8WCUwabYD8sIpx5K_N1VXQLSOGOe94dsGk6uJwf3NZrDV0IsUi3esCzcfy9zgos9e3Xg9WNwMcIws1AGaBWjGzjshJYUR1Dfsw_Zfx3mrtsdLbWA3RrkE0O0aPGSkMNeZRFuUByHkiV_sorGonZ7Rl2JAkvbwUxm302hY2o2A8DIo7mLZ8vl9TsObDWNaTpFHS90DXhYgihB-xftEdQHIbuAmHrNSpB-ad1XS68QiNmaZ0aSOameqleyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZES0V4gj9HUkU_cO1GOHO0I7zSGm8ulEhcCuZ7LMQe7KtUpVHXehos1RBCGCsQrYRmX_RbrB4n4ga-PYPvbl777JqaDOJsPgI_Xy7FuU3WQvNDKlY3EVUMuuhHh6U47TwxX7h6QydEiqJzmR9aBPp1FN7jDNM0eLCkk-B_lAGH318PELbvKYoZ9944sew1IIcAAjjorqat9va29oZY54YAw8mcwL_YOZYFnhwT32fiBMCs3pabWyXO8oNKe3NJWLHw2W4x6p55xUDeDI7K4n9UB6a-_kJn2MD6v6iG2dVWwZyuH6s4e_gb_-7xBBBeineTQq7nvuw5OYYAm5MLuhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf6QO768caKqoWkLe2gp_A8hutANTjnpVUnt23PR1zF9GfRBn1biO0uqvwsd_mmd9JZHURq5ANcdNixSO3OvUBuRjb_z5BG5bP1sH9AnjGAn_Mi4Fh86CbJA8ZWH9ysdi3mMZvEGVEorIfExkDhen5jpZdLbwjSJhid4Q6J_r0BdYBTzJm9zV1_Nw7ncid41i-TIQ32pCv2lGed0a9E36ER9z0BFhqTUtE2i8Wq_B8aRuobDuEO7jsgsqjmfzyWJ7COc-PeEW1rFefq27wZr73vpoR6peI3Txt0FA8rZs6ZyVl8AEwykn3Jg1IEA1iWz_T6JSs4kxglBm63rytZoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=NiUgklXF6vQ75bZoA7jY87wnRdDEuOCApBYsPAHSF5AielFu5T_nB0y6eOk7u-5nJdsuUKpoLLh8W4o31JYpuJ0ICuvamo4xWQeiauEvsK9SXlRpOTjtf2BmzwqpPXx0zyJPNgBup1sx0omG5BS1Avb7x_AXVs5Sb3G0t9JEnJIV4W24LuKjmimnvVcG2OiGFtLDHxYlZ4eIJweAsFdoAZloohzbbprv7pJ4RG-T-g2oacaIa2KvoqbhqsTpnZCO_nmyBLMDqhFIcJiUoDtG1T5mrq_IRMWyxGgefkXreQ5XKlNl6QD_PoJDSyuEy8he5A0-kz6LqDvp6YLAa8dRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=NiUgklXF6vQ75bZoA7jY87wnRdDEuOCApBYsPAHSF5AielFu5T_nB0y6eOk7u-5nJdsuUKpoLLh8W4o31JYpuJ0ICuvamo4xWQeiauEvsK9SXlRpOTjtf2BmzwqpPXx0zyJPNgBup1sx0omG5BS1Avb7x_AXVs5Sb3G0t9JEnJIV4W24LuKjmimnvVcG2OiGFtLDHxYlZ4eIJweAsFdoAZloohzbbprv7pJ4RG-T-g2oacaIa2KvoqbhqsTpnZCO_nmyBLMDqhFIcJiUoDtG1T5mrq_IRMWyxGgefkXreQ5XKlNl6QD_PoJDSyuEy8he5A0-kz6LqDvp6YLAa8dRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=R-Yw06ml1on6T1mPg_M6-FefkbpARnXvnbzgvIxXxphRZ8JsSZou_LFSDV5bns69b49ZSKwPAQy6JZXuk_64O_5Na_mODpdL2WgDgCVwxHL0Z-NxglSd-IK9Tyvb94WT5OZS0QmaVnxQS22KV-uB5G1YpFq_ltuNTGFhCgDchDyRyt-SkX_PZJkcqRiCYeRytzdrnZc8V66mg7foujfklwPF1CcZVuJVOgFyAbIBUBx18N6FSlNjttIF_ZvwsR770KcltWvum0rCOLgP1AXkamaGhxZC07U-ZgzXXNkW-UReDZ8FZAICFXk_KH2R9yCu1Qez1zYeDIFwbxLj8LeB4m-PSHdTBUbczidUjQkKpppZMr5OXz60puQPhaOmmjRtileHmaBoVeGY8qYuYkie_11l72hPAx6DQx6_Gtq3tVtRE2PmSa3HFthr2bZZF3epEYSlwcz78gqvf-WB6Hf_QluacRNO5ufttU5uwDEn__0x_TG6bW8LLbLgU6csUPVinfxh3KuXNIQZ4EPhpmdw2dzgTi04n1vQq6BdRrIPHjSLYB_j1Nx-GRMVZrvU51ahZhg30fhLwL6S2Yq_EwHEmJm3_s0LOdqkl8rxmO0OUL-lgCNP_fSdJssVNzFikI8-sGwXrmZ9sjyjDNmMVGKb97G5ehFWXcE3bX8kxOC5id0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=R-Yw06ml1on6T1mPg_M6-FefkbpARnXvnbzgvIxXxphRZ8JsSZou_LFSDV5bns69b49ZSKwPAQy6JZXuk_64O_5Na_mODpdL2WgDgCVwxHL0Z-NxglSd-IK9Tyvb94WT5OZS0QmaVnxQS22KV-uB5G1YpFq_ltuNTGFhCgDchDyRyt-SkX_PZJkcqRiCYeRytzdrnZc8V66mg7foujfklwPF1CcZVuJVOgFyAbIBUBx18N6FSlNjttIF_ZvwsR770KcltWvum0rCOLgP1AXkamaGhxZC07U-ZgzXXNkW-UReDZ8FZAICFXk_KH2R9yCu1Qez1zYeDIFwbxLj8LeB4m-PSHdTBUbczidUjQkKpppZMr5OXz60puQPhaOmmjRtileHmaBoVeGY8qYuYkie_11l72hPAx6DQx6_Gtq3tVtRE2PmSa3HFthr2bZZF3epEYSlwcz78gqvf-WB6Hf_QluacRNO5ufttU5uwDEn__0x_TG6bW8LLbLgU6csUPVinfxh3KuXNIQZ4EPhpmdw2dzgTi04n1vQq6BdRrIPHjSLYB_j1Nx-GRMVZrvU51ahZhg30fhLwL6S2Yq_EwHEmJm3_s0LOdqkl8rxmO0OUL-lgCNP_fSdJssVNzFikI8-sGwXrmZ9sjyjDNmMVGKb97G5ehFWXcE3bX8kxOC5id0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4iJuItbX1QFW_WNJEiwfDJvfOMfstwmKbytLIc5Pq6xg4wXqb2Q2_yF9mrplGq5kj9TA1r4GRQS8qKcmkGTB7J-fSgrnhOOfAkjBgA6qJltwOMAok8Ayf36F2GyUYw1_egi4IddbB6MiSJ_WFgY3dGeR-oIbLFM6z4CTPolYxRy7P1LOjC2ARHxsVNQ4inHF5fcYI3bjnqYS2vfxuOIcZeFVF4PfXdCy09qFK_KNE-u_pyq1437hBBrZaAQ2tIFWt4HMHYaYHKghWL0q0OpoJv-dj_mJ8MlxT4iQ3y0E1SOzkzZ0tmd1InHZec8zla2xvobd7e5BbjhygFf4CUXng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbgxenGxeShtGHcVULTba-nXA75oxmhC7jfF6gd3xBekF43V5Bdydgz-IQ2g5-XgTr-6LwOXKhLxyqxCpsxWNoG7Rhr647ag_1pZ815a4Xj9My_kUtd-mWC7si_UM2tglX67PR9JWI2EflAFrysXTCCPfBbJookrF7dBVbwgNSGuCBn98ItK9dgys2eh-95Nn-9i-Jn_ZPO-ZTVDwOx2STEkJNvC4yvi06galeG5mITGdKlK0fGvrthP7uExYlhVrD4_cWsL6w7GFYZBL0rJ9dgQGcTz-aoZmTnC9PAkmZfvwqzDTvz61PHFKSPil3zvCTylkGRCmqAZOfOl92q6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XE1CbbsMT8GoKc_lRS3t5BjVpHkpD1itwEztOtWXPI6dF_lcyW2934CKcAz39UlNFSeW7UJ638i7m2HKXBIAexpUVSoaB7YphIxwFL3SKRz5f_xd7EhZi2oXPsDgMl3gawcpvAe8EItSCbIfxDuhEnLDNERe8Xzw6dVIh5oY4yhFBc02-4qMuVgllSA0XMmuxWa0tMpJHJmMvd8CS5PYSaH3ys6xZQT1d4EqHkHtLKp2fuvG-RXmquseKTkIXWMBYMYk3pe9v_j-SJRyQ7dF-3GKx9WaKP2IzZF97CpewP0GElm9V6ocTt6BYeA7lpvcpWgkBTqStrdPfvdbqm9k9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
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
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=e-KO9YN3Sh5bNprRULA3-SwyJodBgXw8L9CfqEoytkLuVulbt8ZhAjyyuQyvRZ_lr0-cgXKvfJtGQdVu0V7ipPa-jAd7MUdj7jAwjodo-kXwsbu4zljCwxKn7kvSbbrPJ8ZuAWv2ZmPYxUl0sgne1-L_a8vEldO7Xe9yxsTW45GL9v5BDuGFEDYrOiCDMBFR1yw1mRZJeyAkzpk7EBB85gdhkvYl3HLEPbrOzZUVbR29yNMn-EvRdAxbDN-zUzG02JiQcYg2PmAN0xLF2y8cdYTVXdwIcrZ_K5PapcOUR3M8n9KuOH3LzeZzlGv-RDsFJYTq_BKxqFnp4-oyr1nuGpnGPoWvJkv4S9rZU7SU84JvVrXNL1HSQ-PF3C3ZET4T4qP7vHyJ07yuh4TwrS0INfH4djfWmqYFZt7QussXsspb3dD8xcIUWBZN9q4xrHOsxukHhtk5GllPp0Q0phWx0TH7YytOB734-kBH1DwCBMxHaFIXrbo_UrVuL7wxlBID2ygmpCj5yI3PgQPrOdqO3jHO1f5Y8lueCj7Y5gl6Qssrxrax5ogO52VvYUiNBuThey6qvGXX8dme85DKlhhVANIMgoWubYe5ygUNKMIPSjzJnApXpYf3INcpB5iK1q_mKnGDw53s-4A19StYE70O_TU4hmUOsTTrm37NaccYG3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=e-KO9YN3Sh5bNprRULA3-SwyJodBgXw8L9CfqEoytkLuVulbt8ZhAjyyuQyvRZ_lr0-cgXKvfJtGQdVu0V7ipPa-jAd7MUdj7jAwjodo-kXwsbu4zljCwxKn7kvSbbrPJ8ZuAWv2ZmPYxUl0sgne1-L_a8vEldO7Xe9yxsTW45GL9v5BDuGFEDYrOiCDMBFR1yw1mRZJeyAkzpk7EBB85gdhkvYl3HLEPbrOzZUVbR29yNMn-EvRdAxbDN-zUzG02JiQcYg2PmAN0xLF2y8cdYTVXdwIcrZ_K5PapcOUR3M8n9KuOH3LzeZzlGv-RDsFJYTq_BKxqFnp4-oyr1nuGpnGPoWvJkv4S9rZU7SU84JvVrXNL1HSQ-PF3C3ZET4T4qP7vHyJ07yuh4TwrS0INfH4djfWmqYFZt7QussXsspb3dD8xcIUWBZN9q4xrHOsxukHhtk5GllPp0Q0phWx0TH7YytOB734-kBH1DwCBMxHaFIXrbo_UrVuL7wxlBID2ygmpCj5yI3PgQPrOdqO3jHO1f5Y8lueCj7Y5gl6Qssrxrax5ogO52VvYUiNBuThey6qvGXX8dme85DKlhhVANIMgoWubYe5ygUNKMIPSjzJnApXpYf3INcpB5iK1q_mKnGDw53s-4A19StYE70O_TU4hmUOsTTrm37NaccYG3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBm7QKUGZ51gJW_ZXdLHfaVQbojT7jSVGjI4M282K7UOFlKO5LmdUlLHFaXpmT4WcoMJe09oueMUxe1Og6ZQ3pq543I7ktI2ZmsLfK2yTzOmfBmg0zKE333TguwS2R35uQbB_p2Wb2XmmKlJqCCzaNMgxQDj1lNoiGXBi_SfFLCoYP10Ekkt0ER41w_ZaMKI2ROnyenkhhHiDCPI1WteFbNtOE9ALzZFynfb_H5HJYVe7R_o25tdTJFDetCOrz_Y9EpPoHperm6ruacP0XTUVPyghSWs0NOZLIANlu2vBTfarOi4A_1PHWHY5pqoJ-VnHmx1rYyOcJ2ZjER4G7bm-7kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBm7QKUGZ51gJW_ZXdLHfaVQbojT7jSVGjI4M282K7UOFlKO5LmdUlLHFaXpmT4WcoMJe09oueMUxe1Og6ZQ3pq543I7ktI2ZmsLfK2yTzOmfBmg0zKE333TguwS2R35uQbB_p2Wb2XmmKlJqCCzaNMgxQDj1lNoiGXBi_SfFLCoYP10Ekkt0ER41w_ZaMKI2ROnyenkhhHiDCPI1WteFbNtOE9ALzZFynfb_H5HJYVe7R_o25tdTJFDetCOrz_Y9EpPoHperm6ruacP0XTUVPyghSWs0NOZLIANlu2vBTfarOi4A_1PHWHY5pqoJ-VnHmx1rYyOcJ2ZjER4G7bm-7kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZCurByvjFl9GJ64AXshEy8oEt4CUgvQ-VlRMQK5kjyFH7m4Iw0EqCi29358fVZvX5TvvRcmoF5SPmj_PKUuFvooGwr-FD4LEgjaPZ5Kc7pk8pP5XYF9CNUJEC6akOz1RB1MXW8q72H9Eyb5WDokRXjdagK1N_Yg4RXDS1tM60g_BFthlYK4Ra3vekITY-bsgNdpO8opEyUoh-0iZiUJxc2HJ0qvFKDw9Vtk-HQkcTR0Mm83CMq9WBtrYMK6oAw6WdN6ubsMnpggCNOmxDetdqkTNmE-3KW9TlX053OiSEVAyb3EKGUZ8xYN_s8gCIJZt3xOyw1xX8Un-izufsE8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilYZDte2ZDTKT5iuF2xCyQb7lCOADiJ7t6cdrEqQia6Izq2Nni8hPNkmddx5rpTDdN8_GRr8Wjq-c04L4bdGN0BFPmh3aDfeH9MwqVX5AJ7XO1aHIkDrqloo3Xstj3_zXYZh0zAfxqtxBhhHX5ZP2EE_RC60_a6XC8jqLmutRVLcjymNp3BauD5sECpc9DFIf2l2Qpxf9f8Z-SkoQsVXKfmtP-vXSawJgY_sMwsl2zuedleMLnDIvFFPCk3ZWvgxU5WnZEj6zS8LqDs0IjP-Ju3eowD2EOyvta9z1OB573SMmYUqCDxSF28M98CXDFLuNm6pYo-Mg8mtyFVaeEnRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=LFWqJjz69fIw4ZQ6ol_RVswSTlg_9y1pW1TwZT5KK8D14_wf7XLfCJw0oMMtFk7fthVVNs3D1Kf9Xkq-GLQwPlczV2q0kaqe1RK8JfR5MYmMW1l0DnSYfplWIdIpf2aKoZpSwC2DEMkppDKcRCqc1hXgL0IGEg_Ck2G-jTI-3GOuKanhQQbxRB_CBL9TZyxXLkjDXwhDuxnbtWIX_hxqy1oLBcjcnxcuzKpXgqOsKQEeMb1didd6mmcBUxBKq0PSZRGaGItXW-KoeQEuksS9iE8z_eMcBowF1xKF9CSHWh1FUrupYuBYpuJtD_GsPp8xLXY7_y9cRF20-t5ObQtraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=LFWqJjz69fIw4ZQ6ol_RVswSTlg_9y1pW1TwZT5KK8D14_wf7XLfCJw0oMMtFk7fthVVNs3D1Kf9Xkq-GLQwPlczV2q0kaqe1RK8JfR5MYmMW1l0DnSYfplWIdIpf2aKoZpSwC2DEMkppDKcRCqc1hXgL0IGEg_Ck2G-jTI-3GOuKanhQQbxRB_CBL9TZyxXLkjDXwhDuxnbtWIX_hxqy1oLBcjcnxcuzKpXgqOsKQEeMb1didd6mmcBUxBKq0PSZRGaGItXW-KoeQEuksS9iE8z_eMcBowF1xKF9CSHWh1FUrupYuBYpuJtD_GsPp8xLXY7_y9cRF20-t5ObQtraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dph6JmjeNd7y0SfvjaxhsymRtqPy84nQWZ29jMyefwy6sOiJTK-MT_XXmIGSWVsuZJkomDZMzCTA5ZuEYEbtv8Uemet2vhvwAewPyHB6MYEmr_7cfQ__5L5ieI2-zTWkU77mlvjdwIGiTrkxji5eAWxvoaIBNHAwFlmhl3bj_cSuENsegzuNdk_Oy2oSCFGJn756eIdgvrVk9r0d_3q44WEZRCqLlOGcCjAueemKL_SpT_BXsX_U0B9IHdvUfqRiVD937nZTJFU--8myoplpmjNKa8MjiSp-FaIHr_i2s2bEs4Edj3lVCHpFEWWhKMQ2nqKalchwgfS9jPadJ0ALYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5MMBDWm8XZy4EcqnHtnjHJMGXaZk9CUQ434osqjylOPZ1UHHcdLRPbnwbFZRmROMXWAtqY3UmlYOjAWNoVhY7sixZHehs_Zdge3NpIYmxISLw4uBJhBnzw30qJD7rIBIz0p9DVYRxbJznYy-gUVulyYvU0prH1jSlfRy0NJnfUO3P3f9qb4rm4Osionl1GSwY4jh8x9VfK7UQmMV_l8SIckSsqTjwhbHQU3vyDO_AHilMl4_crsNWkKk3y0-O7BnOaSUa68JI7zGoLpi3c4b72m5kYFJpDgw7btMY556GBSLFdfGgiHoLMfuHRBOBD_uuvjmJKhl6qS-KWEBGEHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZb_nL4-H9vjb77mwtIh-t6Af8Rk3J5Uyl8DH3mJvKLH7wkqgTm_f368xTRUUcVn3IiB3zLO2T97Pr2dBKjEN7AACdI0ebjEXo2FhxWJylU6Xjf61S0pCrZiUCf_3Y89EDSZkXbB1RPJKSKOsl6nd8we5yhrZDYnEFT61kHFRlD2CBkC0V193HQo3JYeiPVoNE6HEwa-6YOPC4GAJEHkr-MI0c-CgfFKJh_70gB6S1R2Vq1DVJbdHuGjSL3jWAKeh3da1QKpQAs-U_psS1lAtZjhkQQZuo_RBX523U8bU2u1-7abfkcIaHj6ALcqqF012aCYhwfamJDnd-BXnht8wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
