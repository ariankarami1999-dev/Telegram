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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 457 · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8465">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxs0I_MO_dzhxxidfVDl1Wb-F51173tUAvc4cxFvkc6PXGhV9F8jJNBGXVWmAt6WCQHwOcY0tSnRY8JK75o4z6pMeebwaubN7YDUC9dD_VpTWO2ErDnY3fg8RVUGL0Hc2NtCMWRSUvI6iN3xhdVEn9vV2zRtUV_q7oSwcMRzYfmnjKTuqpNoTyxh0IcCfktytjzNM-ETIl1fF7wC1Gr855mGdu4HifdaBC88pvhfvi73MqQpKLrTWaldl4VKnkoiwgJW8bMHP81qY0Wtiz93ql1TrCig7yL9KgCgH43zLV9cY5DYSsL118FqER_J5v86sJXLhN4sxirw3GKmERZVbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 409 · <a href="https://t.me/IranProxyV2/8465" target="_blank">📅 13:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_zosLAwpe1XMCWz_DY_5wQLmFO6NhxjJzQG09VAZF5kFtBOlQrDXcNZTbHnkBLax-K3T1xzb9CZOqOz8z-Dh7UgPygy9P5Bcixfj1_5mLCQ6VDEre6OlI28_d7PstolDoLOwmy6T3KX5JS8v52F_99tntWDMIgWMt0QPxwwvliC37h7gphuDKKKsXEtdQG1CAinI3gx_xy7R2_6tkYqo2qa-Q0xCZsspHCHATnhY4rq6Sj8vr_BMZMO5UUN7yKZpXaxR1Bbci6FkuEmkSvZOCydlGtiZzm1DNT5966qqYYklKVlbJdMSror7mZcCPGAdTS5prCt7L29Z1Ms8G7RfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAgp-u3WftXL4-MzjU7BupEV3oOewG7a8sqbcx43cS7pNDsn6KPliqAULPHg9iF70PgLNy1ldAW9KWQrM16lYYoGhj2Qh7kApdruKkFCb7wZvT95bmrD7SavLOj5GGe1Y11Q2ZTeI18FDn2thhDv782HY9i1giOUh6YoemVbOLz-s9sr4qPRs1BtDcZJTni8rCGMv1xJ51VlMbJqRldoysSONjcLfhyjM915_r2Goib9xg79CIuhgaSFsVd11-8nIPW_wxuQMIdrfoWlwYPGvLTDdWFqfbA2JNXRCbhjOKr86Pj69N_Vufvedx49esXLmuYDnRl0cDLsHQoBymTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=p-3moEaZoM8PfC6NugOInWccWRrFm1sqTqmRkb3cnxizN8h7I9RtkRTFvSbcqokMz4EjsCJmb3P7oY8-U06bswJRg_wpvhb8I3RhDtEdmXs0q4dmmPEKH_doqFQp4M9BDc6KcYzapunCCBHpH9i6YKt6WY8Ti9cY7yPzAd_qd30PrC5jQ30aCp_Ws6Dn8Zg2A7jbc8xS8Be0wUmInqopwOlGL6PE2jk5HLtCVI6fKlXx67fjNjBV6-13QNB6SnzVoCNgzaR2ivuU-svD-LbddEb_JkwsR0Km3XYJR9H2dBjZNjhW3mt4j6mnxuc3fufEChQMWzgHRXSDsIChfabAzysQDvMH-z-zxt0WmBosPvE0L8UQoMneolFkEBcoX9Yig4-wM9xHOaDSEF1QJ8zD8xL8UfSyhMYyPU8wWUGscXgRJZppAPL0xfo_Pu58EbhB9nNoBeiznjM17AMjMFQA8e9zu7pggurnNKKabA75emy1Fq_9KUTDtnkdYX9mi4e9BjKfAnL1SFIwnX9akmqtBaK_bwZIm8GEJWXXP7Uk4dKB95fTZGu7hpI4mK2bG-eqArzY16KZQWDVBXpgcR_6VaXbQGaGzy2Lw2pSX7cOLFvfpKEn4DPDUXYreEQz2ZOSA5xFCNjWTpFYC2KjcuhX6ADJ9peNJeY6Vy1X9f6U0e8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=p-3moEaZoM8PfC6NugOInWccWRrFm1sqTqmRkb3cnxizN8h7I9RtkRTFvSbcqokMz4EjsCJmb3P7oY8-U06bswJRg_wpvhb8I3RhDtEdmXs0q4dmmPEKH_doqFQp4M9BDc6KcYzapunCCBHpH9i6YKt6WY8Ti9cY7yPzAd_qd30PrC5jQ30aCp_Ws6Dn8Zg2A7jbc8xS8Be0wUmInqopwOlGL6PE2jk5HLtCVI6fKlXx67fjNjBV6-13QNB6SnzVoCNgzaR2ivuU-svD-LbddEb_JkwsR0Km3XYJR9H2dBjZNjhW3mt4j6mnxuc3fufEChQMWzgHRXSDsIChfabAzysQDvMH-z-zxt0WmBosPvE0L8UQoMneolFkEBcoX9Yig4-wM9xHOaDSEF1QJ8zD8xL8UfSyhMYyPU8wWUGscXgRJZppAPL0xfo_Pu58EbhB9nNoBeiznjM17AMjMFQA8e9zu7pggurnNKKabA75emy1Fq_9KUTDtnkdYX9mi4e9BjKfAnL1SFIwnX9akmqtBaK_bwZIm8GEJWXXP7Uk4dKB95fTZGu7hpI4mK2bG-eqArzY16KZQWDVBXpgcR_6VaXbQGaGzy2Lw2pSX7cOLFvfpKEn4DPDUXYreEQz2ZOSA5xFCNjWTpFYC2KjcuhX6ADJ9peNJeY6Vy1X9f6U0e8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDXyzmg0HWfMHE7DA-PSz39FwMiOFVXucFT-TNkUTn3ifq8-ClJkHhqygvOwkvnctldXWbej8LUYcvma_KOg7E8LR1uyY_geGCCxDlbtZYMb9JdfwYlSCg2_P_S6oH5XjCuz0p9skqQDGP_ZKNnE_JF5fZzpJ9Mxl7homGhCV-9RXN-ith6UTAtGxMx5Hx9W784yngndc-S5HKN984vghXsYy8qJ6SWOOCzecewxAteP_MvQjp1bRkE-O4UklA0Qirio4ZfSxvqbuM_Q897F-ToDvjE02bdSkVk_waGKRtAT24gO_lFolcKRoPU0tN_IjMN_nKeSSOZRgxcK2YGJcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFUvNj4w0HO2Hzdv7hPv2IOqnZptvfsemZldKLVuyLJYXymezTXmjHldWs6BUZP2AYiZLQAO4fjimwdHxKucoXmm6EitccyP0Pqip-ImYfMja08WNFC_WYYmaUHigayeUXTp76KmtK0QMY0uHxU_SK1cDLaumJkiDCsikN9q9uGXUuWAh0rYAUAYyY2UcVKQX1aQcCw7W-Yhd1r0A2-mNmp5mKz0WcTEi9YnP7keiIgRysnBpvr-UZ4mWMRxmsPUMNqJAnUYnhJDFSPrkqTNrnYlWwrrErHvyJQn7oy9AuHJu69KMraAT76zELSl8BcQ1Cc0HzvHCyzWIq-0PZmG8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-i82aYqeoevP4Xqt60RlNKiPGIXnclv6EMIgVKlTBgKgNfQOPWOd2cfE68ugfMv9RLGwTNhbPfbtvibP2MdYKJvZ3PYUtNVWuYRaTYnADjBOEagBIPvbCgu516dwdYoF7WM85UYIEjCQ3bNvC7s7Sf5H0q9WexLEQ_NdpKFfYcexndN06vWk76htSLm7D6-3P8dyQ6rK8T-XrnjtyKN6UJ9LXwAJysvUI6B0ZLwTZep0RFOtf6yvibLV0-8lNy_51LH2I5Ky_rV54AT8ZFtIKLzPYBndEfJVvn21apWxALNss83iEtAIihDnpj3gqIFbs4JCKPRJP46mILgSiJCmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=iVBTrqiEidac7CCeIi2uAZbaP53jwAVbZ99ODVcqaUJ-5RBoVvMNilmWsFod9EHs3N2uMxXztbXT_tK8LVJOaUd_kfbf02hw2lJU8tkW6dSmpND0SFtfLG3WvpEO4WxM9Ac_WYBsZL7KtvG2o-4W1BNVDi2VXTkI7E55Pop8rQjFa7Qr-kDi_4d1EVNNoeVI86YvCEcdO8AUo_7CGRzyyPiniUEhj4e7EsijZJ95tQUqMmrJAvb2kUpktqONrqzg6duMd83NJSYAyaa_WNQYXU0rcf2FMwxdatt3LtYuQe8A3IMDFQyBAoRBX1B_MJlOcNZ_pJA6C-YdsTqjP-UGSFF97CZn9iXyVSPqcjhLMRHlmVKdfk9MrOQnk8_g4iulNC--fxrQfmKet4W8YwH9nxAOS0O00gcMCtI6FBYWu3uJzZvSWgSyger24kP7uJTl6KMzBQJbLrfJKbMXUiBxaqwc9ttcWr6EYJrWZXg17tfz0xxRO429atKoCpi8_qoP9TSYA4VP-9CpdQfT1DIqRRIgiM3rqdswQjC9qN0_9j1mtoYj02HHj0F1DyQqYxud0bKFu8av1balFUAzb6Arj7B-jY7fJCRmpjn7diNhx_8jDU7wX7PGH5yhY01r4OFyf9ya_Ej2wNuJOmn9Z-Ox0WIHfCYVLizMSD62cqRI7FM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=iVBTrqiEidac7CCeIi2uAZbaP53jwAVbZ99ODVcqaUJ-5RBoVvMNilmWsFod9EHs3N2uMxXztbXT_tK8LVJOaUd_kfbf02hw2lJU8tkW6dSmpND0SFtfLG3WvpEO4WxM9Ac_WYBsZL7KtvG2o-4W1BNVDi2VXTkI7E55Pop8rQjFa7Qr-kDi_4d1EVNNoeVI86YvCEcdO8AUo_7CGRzyyPiniUEhj4e7EsijZJ95tQUqMmrJAvb2kUpktqONrqzg6duMd83NJSYAyaa_WNQYXU0rcf2FMwxdatt3LtYuQe8A3IMDFQyBAoRBX1B_MJlOcNZ_pJA6C-YdsTqjP-UGSFF97CZn9iXyVSPqcjhLMRHlmVKdfk9MrOQnk8_g4iulNC--fxrQfmKet4W8YwH9nxAOS0O00gcMCtI6FBYWu3uJzZvSWgSyger24kP7uJTl6KMzBQJbLrfJKbMXUiBxaqwc9ttcWr6EYJrWZXg17tfz0xxRO429atKoCpi8_qoP9TSYA4VP-9CpdQfT1DIqRRIgiM3rqdswQjC9qN0_9j1mtoYj02HHj0F1DyQqYxud0bKFu8av1balFUAzb6Arj7B-jY7fJCRmpjn7diNhx_8jDU7wX7PGH5yhY01r4OFyf9ya_Ej2wNuJOmn9Z-Ox0WIHfCYVLizMSD62cqRI7FM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=Xx7vTfE64KIdassbAPKfEp9J_4sKmqlefSJN3tOajMphck-_QJyZHeaM223fS5h6JIFhNG4tsabhMQuSlutFrBbUiUrfRiXA4ebtTOac82ssiL3CzfBhZ-qOaLH32zqeytCOf_mhH3yYq5c9y7asjR5_K8eAXTxHmQMKA1FtF6RrqIiahYGwuNAxeAdDbHMUvQPXtHHFDaiHtIWr4UpRFwiA1tSeu7W_EArPVPnQlXeUhMbC_hQhfLIA2RXC0KGkWq2a6mvMGQm6we0Ko-vILVbC0dpRciSr7zDRM2PTfeKxwhLKuHRod7sPhBz0aqZ1_pKzhKcUCo9ofXY_QYIJPEvmOCOWCPwS63K9Fx1hD3FXIc_qWdlAkPbLJdllgapWiQEVMY0BDqWa6qQOuKxAl0aWTorUNjfpbgoDJG3YsmjUHTjo6Sj0_94UBoHUh_QtournfdXQKhN8_3L4JnaAGSPZaNAMe2x8XPGX46FizAmFoDscb1LrrMN-jEDwTcaw2HIcjdDdF1QUa5ZH9wNYfGh9LBKyHAgaxobHxQQP9rfU9dzNBvkZtCTP7gLD7z3SDHw4c8AaywLDtKT5jWaLKyoKl9FeCoxDwmbt_fN9xPTMkyHSuRkcXaSrN4jlAhoUZPVZhKHcRbbUVQtQolhAXhAGKMHAPmY2xZ1Qh83YEns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=Xx7vTfE64KIdassbAPKfEp9J_4sKmqlefSJN3tOajMphck-_QJyZHeaM223fS5h6JIFhNG4tsabhMQuSlutFrBbUiUrfRiXA4ebtTOac82ssiL3CzfBhZ-qOaLH32zqeytCOf_mhH3yYq5c9y7asjR5_K8eAXTxHmQMKA1FtF6RrqIiahYGwuNAxeAdDbHMUvQPXtHHFDaiHtIWr4UpRFwiA1tSeu7W_EArPVPnQlXeUhMbC_hQhfLIA2RXC0KGkWq2a6mvMGQm6we0Ko-vILVbC0dpRciSr7zDRM2PTfeKxwhLKuHRod7sPhBz0aqZ1_pKzhKcUCo9ofXY_QYIJPEvmOCOWCPwS63K9Fx1hD3FXIc_qWdlAkPbLJdllgapWiQEVMY0BDqWa6qQOuKxAl0aWTorUNjfpbgoDJG3YsmjUHTjo6Sj0_94UBoHUh_QtournfdXQKhN8_3L4JnaAGSPZaNAMe2x8XPGX46FizAmFoDscb1LrrMN-jEDwTcaw2HIcjdDdF1QUa5ZH9wNYfGh9LBKyHAgaxobHxQQP9rfU9dzNBvkZtCTP7gLD7z3SDHw4c8AaywLDtKT5jWaLKyoKl9FeCoxDwmbt_fN9xPTMkyHSuRkcXaSrN4jlAhoUZPVZhKHcRbbUVQtQolhAXhAGKMHAPmY2xZ1Qh83YEns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJn9mAtB1h6LrzNk4KkBNFcVTaqUW0n3SMDqb-5R08y3jA0HdnhQPTzBtKAOeMssEFx1d91KnmX3IEk1bnMDGHVGm71844VU14pr4U7P3H88kiI8IbIgQZQI4JdhZa0hzLNaboFTBtsWCt7OqiJGV1SNyN8qQvw8G4s1s9U0_3lFpnVyE_umW7bCCZD6TWmdpmFZS5CCm8dEA0oOfUL9nFcaIkk_j1m3FW3eHt9DPmKDMY-_jBAgm47fYE5pDAAztmdqWfEaEE0NR6aXLMcyQYO8_UXe5xiyKk8mEe90Nrwnu00I0jQHBIorKDBAMk3fYAsAX6KY03gSFwLHg--YwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=ifCe68H4Nu84ScwzTAF-TtbFK9scqb1sBeJOuGRhlyaCXspNB_BSjNHeWCXVol-lOKYMC2o4EKKfTChXoFFVchZrfDAEBV1ef_od9lSm0bE3M8NEbh3-H-wpPIUIICaQBEeaucHd6HdqicM5b9IouLyfMwGY1rT-CMkMSb7L1rV7Ov-tCKl2EzwTMl_P7H6lmmFgPbwg1vxgELpxaP9fh7Xe1p2tTghANo4jjmbZ5IS-Uh13fbevAetKrm38iyJ11E3Ka9gHuwoIvVYFpL_TPhlWLvPiJaGzmBF6yg-EzdO85TyvYmQ2N4phhmd3OCvjToj9Xc0sHXj06AeUCv4jvH6T3o81XvwRl9bcrUTgTknkkfyqN-vt7GZ58ZMiTdzHSRXwY_9ZmKRr40T9YWfUQtepvkICeqRE89qkQ8TChbD9Cy77dn0Q20-KAp64hEHEy0DP7kZ0fwucnXgYNc8masOJXlD33Td8Thtd1l8AwVJ7HRi2N6E8luJAJT2KCgquXmXxEaDZs5eA3vPZxzE9Jnk25NhZZ4T9SHpNwv2LFhusnKsX4sKFUKgkE7dlYK_UIayDw9fXX3hUYTrWN-CQmZLA7Rrviinu2X0Ha09LGd69gyIp0HkYyDIYVI9Th2SjXvbQo79_A2zeNqRYRS1ibNF0r9TXOnQGG6mE2HE5qNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=ifCe68H4Nu84ScwzTAF-TtbFK9scqb1sBeJOuGRhlyaCXspNB_BSjNHeWCXVol-lOKYMC2o4EKKfTChXoFFVchZrfDAEBV1ef_od9lSm0bE3M8NEbh3-H-wpPIUIICaQBEeaucHd6HdqicM5b9IouLyfMwGY1rT-CMkMSb7L1rV7Ov-tCKl2EzwTMl_P7H6lmmFgPbwg1vxgELpxaP9fh7Xe1p2tTghANo4jjmbZ5IS-Uh13fbevAetKrm38iyJ11E3Ka9gHuwoIvVYFpL_TPhlWLvPiJaGzmBF6yg-EzdO85TyvYmQ2N4phhmd3OCvjToj9Xc0sHXj06AeUCv4jvH6T3o81XvwRl9bcrUTgTknkkfyqN-vt7GZ58ZMiTdzHSRXwY_9ZmKRr40T9YWfUQtepvkICeqRE89qkQ8TChbD9Cy77dn0Q20-KAp64hEHEy0DP7kZ0fwucnXgYNc8masOJXlD33Td8Thtd1l8AwVJ7HRi2N6E8luJAJT2KCgquXmXxEaDZs5eA3vPZxzE9Jnk25NhZZ4T9SHpNwv2LFhusnKsX4sKFUKgkE7dlYK_UIayDw9fXX3hUYTrWN-CQmZLA7Rrviinu2X0Ha09LGd69gyIp0HkYyDIYVI9Th2SjXvbQo79_A2zeNqRYRS1ibNF0r9TXOnQGG6mE2HE5qNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7H9WEvBx7QouHPPnzjaSHEKUgbLlFQjIYFXB2DyTgCaugsvVV2yZ3QYMSdCtcAbtTD_TpTGs1WHvS6oSkRzXO9hWZq4uwbKT2SoO66O-HVGUgKhFAl54K9NYol5fxj_PTnsseppCvHZ62FVCxffvwiPcJuc4XZ0NImZan543JlgKZwGL1O-fdUfoaUt175Qff-gDLJQYermC01_0Tlnj1sUvxAlrLQI1sA_gTXbnF2dk0JEuqqDWQ90ME1Q4TBdWpbeX6mTcO4RMAtJgyCmNrlb12AfRzhFSjHwCPAXPonv-wTltEipj6_PbaB_9d2OpRUCqVvsBW694NlGLCK8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmBu01Rdp5_AAxtLiHSWth5JwYCBhGvI9-F1hK8dOGlPkpbNZIlRxYG1_WIDrcksfoTdAMMylKAxFEc3bqrX399w-0py8owAS_yqwrOSC04NKNqZ6oa1ekssPU2pJfJS81KhR7fPYep7xGVyGF7mXNRkUrOXniU7Tc5G2XM-A-duhEd0F7xZf4iJYev2RoXbnjBJYluLuZzdRnlaw6USJkl9VrRf1q04bGRINzcLZfSEwO9qo-k9eWOrsSeoxhhBPM0ZY90TIZH3UAnFweYYrKi9w4wLJMiUP3zZTUEXRrjXNYYzV5F1Der48IxOxhgABYR4R33atbsS7O-HHF3I7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=MOT_KSHSD8y7pFb_afIpQu3IPvoHipgA-ohEUvs_F6yC_XylsnjxDOghLYxrs867Iz6XsN2m3_85hegXMKqhjaIg21UF2unSIHQ1AuPK9xeADEo7eTna5RKdoRRMAREUVvmU-NL2T2HXNWpiNlvGgSk48pTPjol8K8eS4G5tmyLuzGrNNvUYxYykWFUKQyonWzAAF8rNtVJ5VpYeV7zVsHt-zRc9MTckhokHS6Y-zmiVA18t-0jxf6_eqpD7fbbay8TzsRobrjSxs4CEEm5Rk5tW-ocVj1GBK6cNV_q6RP5mtwqGCs2aHrH2rZDD6D9gDEKMGsKafNz33rHJTn98Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=MOT_KSHSD8y7pFb_afIpQu3IPvoHipgA-ohEUvs_F6yC_XylsnjxDOghLYxrs867Iz6XsN2m3_85hegXMKqhjaIg21UF2unSIHQ1AuPK9xeADEo7eTna5RKdoRRMAREUVvmU-NL2T2HXNWpiNlvGgSk48pTPjol8K8eS4G5tmyLuzGrNNvUYxYykWFUKQyonWzAAF8rNtVJ5VpYeV7zVsHt-zRc9MTckhokHS6Y-zmiVA18t-0jxf6_eqpD7fbbay8TzsRobrjSxs4CEEm5Rk5tW-ocVj1GBK6cNV_q6RP5mtwqGCs2aHrH2rZDD6D9gDEKMGsKafNz33rHJTn98Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPvV99v7g0mAGcOZV9OqQaTkFKznossZjXulptcqdXprgq02VBu5V7X04i3MlCBfmAGdHigaQ4hpayD4YExr6QNiynKnPU1P-WLAHe1HhtLiL1zrm9dgFtJGWz0KTnSYRtHHr40DFuBL96MAIbFMRKLKDlXLWEQIiQRuOApImU0n8W8PslP8D-5uY_vFRe8-YGJAiLkdoFx5iKxEFqKZP1Dm1puhA5ARtqw2WFWbK933WbI_zB7lXPGu-EqN7Aj4ymmlMI_j8xJ4AIFJQh3AKZAlFQBjAOt7EzECBO-QgFK-NryUg0l-yzYl-Zjlv-zbfFw55RKXU5bFClVI-oEfqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIgTTkUmOFhJO7RuB6cm6W99Abvq2dPa-6QMtrwblVysNPrSTpbwajrQtD1pfEfjyrHcUOA0ZljrTNIXiFUM_67Mmx98jtJD2oC-lKdzNHne6eeyjsRVBxtu-95bkZsskucp8pa4eC9q97hQzaMum_rH4CFHq_8Q9IcY6V7pPRwjn8erG5T-vcqaHpLSTuqtdDlTu-20LHyhj6jcVe2-6sqef23Em__0GwyPTBRuVOxIKoohn9FhiQTMRXgKlvX9PIDvCNksO9WswmqzkpNpwkRUu8AAntrl0XGmPXiMVUXEoFdO0x97EOPP07ssf4Vsg2gVmlRNfVPdS3jrYnf5Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=cv9xOpe0GAYdTLXvvTu3faGSAF8zQs6Fg0fyoodp5QX9-boRo3ff7pFHqkyWBeAXXrWCM-jFgGFyLhIf517XlskuUcryomaUcnd-AybUH75PUJS2p81ujXiVGZCamMiQScCOjNzQd0d5aeOgi55WWXsKzHtHCssIPZtC3-1bloCg9wmia7pO8yuvgoM1b3ADuf5whQWimoukv2NDR4-mCWLrtqs42IySu90u8k-SyK2GSE5cGf8v6eAWhzYZjxpSljAPziFMrz_0nRhnfOfGrDyCyweoYre6gyQKn0hnxutU6_sVPG_vdGdzOKC1MxoGg6EiZVspo5UCbrhVt1URJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=cv9xOpe0GAYdTLXvvTu3faGSAF8zQs6Fg0fyoodp5QX9-boRo3ff7pFHqkyWBeAXXrWCM-jFgGFyLhIf517XlskuUcryomaUcnd-AybUH75PUJS2p81ujXiVGZCamMiQScCOjNzQd0d5aeOgi55WWXsKzHtHCssIPZtC3-1bloCg9wmia7pO8yuvgoM1b3ADuf5whQWimoukv2NDR4-mCWLrtqs42IySu90u8k-SyK2GSE5cGf8v6eAWhzYZjxpSljAPziFMrz_0nRhnfOfGrDyCyweoYre6gyQKn0hnxutU6_sVPG_vdGdzOKC1MxoGg6EiZVspo5UCbrhVt1URJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=I6oZPqsIoL-SzR97rNq6FTSc7jSyBAkQjaXAvD4-izMJ40M5fHleepR4vr4znjsqThQtYUqz5vN_i8OCFe66PMKHeXA2XoLhXyCchGKNFitmqg1Q34cV86DQ4eTG2i2TZTIIrSzatELWQLcoh6YqZhZ05LEtou32mD6P_Uoxd6oHA1R8LPj5IsbAjcNcZxNfvF0ZjbUbz-s0T2Bg3jq4MtXgi_1NpTMwNEe-uOu6ecghYhzypOZhgTUBPErmBkb2jWUwM1AigbhFn9aXzjLu89vcSmQh3sSSjhIM6vw8x20euouBCdLGaaRCRV9kzMAuCUVn-quc8Fmo5aGewV8iAm8t-UzGIdcz41I3E75SKNXpyuLHmF1IMZrMNOaHCCXEN-f6a6GhYyWajr9XLuFILnveboMv09CqpFSoY7Da6d-jEDayb_ZKin5tddYUnQByLGWSkOiYhSE3jbA6HGIGX0LhEvjYY-_A3eINbfXrQDwuC9l5Kk-8R5foA8xHQnWp5R3g6EEGBv-iR1N4unUVuSDDrnt72P_YEx6tZoPs-fqMZzl7G38KTbLR46IBsKUFbD9arLuCnfVtwECRMVFI7Xc60yzW3CcAR5jNh5cjmJDf49UUfJkkrHc8Ix97MSOiQoyA8rEyo751AAmY70gslM1ZLRQ5WmQDfLpgD7X4hDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=I6oZPqsIoL-SzR97rNq6FTSc7jSyBAkQjaXAvD4-izMJ40M5fHleepR4vr4znjsqThQtYUqz5vN_i8OCFe66PMKHeXA2XoLhXyCchGKNFitmqg1Q34cV86DQ4eTG2i2TZTIIrSzatELWQLcoh6YqZhZ05LEtou32mD6P_Uoxd6oHA1R8LPj5IsbAjcNcZxNfvF0ZjbUbz-s0T2Bg3jq4MtXgi_1NpTMwNEe-uOu6ecghYhzypOZhgTUBPErmBkb2jWUwM1AigbhFn9aXzjLu89vcSmQh3sSSjhIM6vw8x20euouBCdLGaaRCRV9kzMAuCUVn-quc8Fmo5aGewV8iAm8t-UzGIdcz41I3E75SKNXpyuLHmF1IMZrMNOaHCCXEN-f6a6GhYyWajr9XLuFILnveboMv09CqpFSoY7Da6d-jEDayb_ZKin5tddYUnQByLGWSkOiYhSE3jbA6HGIGX0LhEvjYY-_A3eINbfXrQDwuC9l5Kk-8R5foA8xHQnWp5R3g6EEGBv-iR1N4unUVuSDDrnt72P_YEx6tZoPs-fqMZzl7G38KTbLR46IBsKUFbD9arLuCnfVtwECRMVFI7Xc60yzW3CcAR5jNh5cjmJDf49UUfJkkrHc8Ix97MSOiQoyA8rEyo751AAmY70gslM1ZLRQ5WmQDfLpgD7X4hDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogTWQ9E_zhY88YfZBizuwbE-6-FRH27hacPYB26fvqyC_2VYY9WQouRiAzO6-DidusSkvhvWuzSW7Twf9IbHPqPxVbR4YJbj_NEGBKw7Kj7H0Rq2s9jqv2gcex6rFD-BuVLuftZeQjmvZsbRmus8DOKKph4qTQWkOkQWi1E1H1rKf2DH8U1OUzUsqZIbU0yiwxRhQ04_tHeNk-qRExs0W8KisLqQaEP0aFmT8nEPsTIgggYR1dMWtSO0QDAupkaVNHR59P1PaLQyn9au3nkdACReqq7Ff9_Is0MHM5it5TLkKcKa5jc7qiaroESmkFVm3n0HriFgpNjCcWQf7-Yy2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDL_GVExxaYiSNvem4OghaprGNqDtxgOH75zxazcGhRNUXzeBy_dH2VhucreDQlKpSwvmm1uiHYvgo3n8sEyW4itPViEjiJPZEmb60B_zQmrc_nkaYrVDi6auZVWJVG635EOPlm-vNyEBJ4PlX7HDfHdfdmpWFxbuJrHIH7Inm2ytHvOpHx6fpQZW6mvEpceKaCjaywrQB4x04PpnyCpBS_jXHIPqrJqyOMTHz-VaI9C89A8rGSjm8G7EJqOCcvnXT_ZOzfVLrneTSwwSQf7vVEWCT89BzCmqeHsJcDEZ8Gu2XDheAAv53MBv3896e-Q4qkhUu_LKaGpBXTguNsXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OIVlfrNO2Z3VQsTnZlSGGCaGO9aBaDqmP7zbqS_5Fl0WqBm1rdaruT6pqf7YkGM0o1AtHR34DksZT6sr6sOMaMD5KTzjMdGGXoRw5O5NGZR1XuQHt2wads4KL_bWYUv2nAG9aJWYvRwqpr8qkbkT0TRjuQjHSq-UF5AX6W12fZy-BBnMJQfSBW2raq42dqySjcYLKhTm8Q8a9pSFIaUbr-D64NMSnCebiWEMal-G44B54RoG2if_PMk0-3c_mt6nzN29C9CzT_8gCK9KugL5fp3u5mSpwyclw7t8Baf88JNFX7cZ5ue5Y9y2sN-wj5uJssRUueYg5uh0XxAKj11tYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=YLY1yzS_PuxSCoqyAxC-_or7N08PJOuZ9dRTY3SulVpf-T_afn9w6bnLBaKoleRQwzpOk0xTtx7H7tE0Mbk48_-Iz2UhZy5pfSzNrTCB2EsZt-Q-yxFRTdu9Ywp_hp3_rC4VDSr7BJuXchHYWHj3p2otvt7HEiNcwJLk6WH5AeH3-RVBChLrCLgyE3Jh0NqZXZnvUt3M4o9CNVeOCuvanVlAtlH9Mm0YTgMRg31w3ic3npM5lsisOF6eDj81EX8jMg85RYkoLb3ss3tlUPsQsafzRSOwzEOCp6adHrZNI1CsGZunw2PjgyuIglB_sG1AIXE-Sf2KQ4CtTWATIEel01ZzahLqJpuXuRWJClOo11zDxbukl_z60XRY_6CjVUi0J5MS6CJV8FJzhBRjNM62W6dbKb_KRuhKjZjAK_QpwNITRVq6m5jPHtXj_LqeXwMQRDZmSGrcQZSHnxF3bJsLV3Ra5MhjUVLbT3O9nRkjDttk34VvE4VpQmKhE2HFszqxb9Bh_Z8VRdbPJVJhwBH11Zz53_hSyUkUeiPjO2CcWbB1_v1UY5IhHtUr0A3xOCgLPByRKJ_OjL4Cx0xtJoMNxtKLGwEMtb7F35XH3qCXGJYKNz75RzqKOmZEibJu-Ys0jf2FrGvVZlrzFk_74QCsCKCWOtLl7B9Y7cnm9-4-L_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=YLY1yzS_PuxSCoqyAxC-_or7N08PJOuZ9dRTY3SulVpf-T_afn9w6bnLBaKoleRQwzpOk0xTtx7H7tE0Mbk48_-Iz2UhZy5pfSzNrTCB2EsZt-Q-yxFRTdu9Ywp_hp3_rC4VDSr7BJuXchHYWHj3p2otvt7HEiNcwJLk6WH5AeH3-RVBChLrCLgyE3Jh0NqZXZnvUt3M4o9CNVeOCuvanVlAtlH9Mm0YTgMRg31w3ic3npM5lsisOF6eDj81EX8jMg85RYkoLb3ss3tlUPsQsafzRSOwzEOCp6adHrZNI1CsGZunw2PjgyuIglB_sG1AIXE-Sf2KQ4CtTWATIEel01ZzahLqJpuXuRWJClOo11zDxbukl_z60XRY_6CjVUi0J5MS6CJV8FJzhBRjNM62W6dbKb_KRuhKjZjAK_QpwNITRVq6m5jPHtXj_LqeXwMQRDZmSGrcQZSHnxF3bJsLV3Ra5MhjUVLbT3O9nRkjDttk34VvE4VpQmKhE2HFszqxb9Bh_Z8VRdbPJVJhwBH11Zz53_hSyUkUeiPjO2CcWbB1_v1UY5IhHtUr0A3xOCgLPByRKJ_OjL4Cx0xtJoMNxtKLGwEMtb7F35XH3qCXGJYKNz75RzqKOmZEibJu-Ys0jf2FrGvVZlrzFk_74QCsCKCWOtLl7B9Y7cnm9-4-L_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBpEKahNZtcc2hi7VXrnLf7PENdc2MKWikwxVjO85QXXBnldQ8MXPrMs4cv4Dk3nwjp-rYmt6SjEJTkureGu6ZdGte6LvKrrl1LkxHIxw4KIPdJtMyIGzUtqN_6Gz7fpxNFe7c90NoWX5z0i4VSPUfIULdHbnc7TLpb-DW3XdCtbe1RQCjnNClYNCHGD7YYR0NhBBoV-jt1RCbQx3Cn260VLDvpndaRwCD9z5ROJl-aLHY5su6EdwV2rQhbvFOEHhZ-porZcnKMmecLWPNAPE1dfgLZifqyl1KM1MAndfiFz-uSUgd5sNGU6RL_S7zqG7rmADwOLrIqvlsYl3CKo--P4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBpEKahNZtcc2hi7VXrnLf7PENdc2MKWikwxVjO85QXXBnldQ8MXPrMs4cv4Dk3nwjp-rYmt6SjEJTkureGu6ZdGte6LvKrrl1LkxHIxw4KIPdJtMyIGzUtqN_6Gz7fpxNFe7c90NoWX5z0i4VSPUfIULdHbnc7TLpb-DW3XdCtbe1RQCjnNClYNCHGD7YYR0NhBBoV-jt1RCbQx3Cn260VLDvpndaRwCD9z5ROJl-aLHY5su6EdwV2rQhbvFOEHhZ-porZcnKMmecLWPNAPE1dfgLZifqyl1KM1MAndfiFz-uSUgd5sNGU6RL_S7zqG7rmADwOLrIqvlsYl3CKo--P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R99Kt2MwfG5XFqts5olkV-NCsh2PrlawwaVSDefu8Hj7iF2Ax2gJClVq8KHNoZlxzqq3JmcolykbZNHLJged9Hq6ZMST8NUEtF149QI9WmBuN-d5iLErQ2woKpwClkv6cmeiHJl4LWzYXkRY31uWmeZ5N1FHbaoIvGvinjNAbFto146wK-QoSQk1tGu-J0y2WYAOhpeoc8rk_t76IwbeEV8E5xCdSpg-re7gGoNP8kZ8i_KjUVDwcu67dfqta8tB_iFk3E-A-TvZmfzBK3V8LmvYk84mOb1pgbjCDG6bqOYa3jONgvq5vle1P8doToRydwKstaAPa0O3QT0AFJgLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-6d4SOxmEG3p1bf5hPmeu1ZSdETOU3iqYZL-08Jq3LW8Nn_xTXHg7_6BHRTB_cobhndQJGIonKHdUkHqIi3Y3LDBLknY9Q472rgga9LmfLK_0PN4sLBePRLPdzxyZG7wmPeFhKxLGcFegLKZB-96MDFzGVMfOETD4pKEO99_K1CCriZcRyaxoSXwxtACEql1thMcUVRBHjeT8do_dH3kyh5_2rxHjYCddkIzoSgWw3_PaZYjfanQgRvE-jGPWZAXqBuREIJYrOF5a8NUPwZGwJ7-PVIwspnsAmWM8goa5Rx3lp1gkQixu080mW-JETrUpxGGSkJSwQyN__Pl688pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=bw4zVCDqSkNgqUDid_ZvSC3mw6ZPprsHF3V4nd3vucFN-Rp8X9xq2jTI1rATtnrAFU4Sk53lSWKjGeM-meIR0Z_Wp2MGkqz4FnH8NPsOqQZOkLOJyYfO-CPFc8wsK7LhEyM7twSRllvL6WCwH9U6QHAa0UuI1iqsjfoQsuA1UGe88h1rMOQnP9pbppO2mliFD1hjmA9X_4xq-H_G9alvufwm5FOL7Ukqs9cdPE2-TNkNq9FYiTG-J2RotYk09bfVuTbs8Oq3QhRzAx_gok1euvQAV3KPWa_PRGuvb965iwMZCpkUZLJu7TEOE6cDJPbcYTBlFB1BmIh4wfco88HxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=bw4zVCDqSkNgqUDid_ZvSC3mw6ZPprsHF3V4nd3vucFN-Rp8X9xq2jTI1rATtnrAFU4Sk53lSWKjGeM-meIR0Z_Wp2MGkqz4FnH8NPsOqQZOkLOJyYfO-CPFc8wsK7LhEyM7twSRllvL6WCwH9U6QHAa0UuI1iqsjfoQsuA1UGe88h1rMOQnP9pbppO2mliFD1hjmA9X_4xq-H_G9alvufwm5FOL7Ukqs9cdPE2-TNkNq9FYiTG-J2RotYk09bfVuTbs8Oq3QhRzAx_gok1euvQAV3KPWa_PRGuvb965iwMZCpkUZLJu7TEOE6cDJPbcYTBlFB1BmIh4wfco88HxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i0ZLrj3cwG94bJKbT2fEi-mZxtmgDomJqDm7VFyzDN--mFCj0J2JiXWn5Wr-T0fged_nTQex9475v46c7GWNMrj-V5GvCI5YNt9LBtGi9Ltr7jkmhbOpimGZ4RqIlACyji6gf0QqS7HKiQJCPH7pgTYLWP2xPyhDWgrAmWtNNQju_0L_Jc-1rRAU3ifTcpp14DFqHBaWQOThGVCHlAUoRJ3MSsIJmgYROrzuO3EMcrII0LucVnGMXeYYyJdp_UtIXyg2BRoTynEQQUaCOJ0MWIkAyuhAEKDB9rE9S_GOmG81YIBPTweHbBWwHXYISdsQwsEGia7IhuldgWvsSZPUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MP9xJSUgIOdECCRPvtqLDN6eAwK7CYLIoEnIhdemo_103v2Eqyzayff-J8rfwgaJYGS0oMbiKGR4uVUMa1Szv-TBQk4hxKIKYKXBS5z4__9dxZw6ikcSnvd4Ri47BMAQB1Vraxs-AORSy7XXI-XWeCZj86KwP21NTP8usg261Wo93gQhvmQoK0_V8pGfmoHDqvVgnVhHIjNcN_1MuNADYrQzbtXAFCKzYNuzeANV9p4w6gjkDKCftbPUNn8nXT2khcfKu0Wr6b8680TdsNFjB__DKmwrhdzJK4SO2pNQLWeVwPmVNc7bhoyLT2RAkh6dL61Z3OVAL83H9uE99fRmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvO-5G7CzB0SP1nGt83TD0hNrr-UTDC8bd62Sw3duEOvO0T9L17Lx-kud-FUAhsf5PbMmrWlx5d3jCmgfj3Uj-cUJL8bTrB7yjSMe4lpuSylI2YN3c2xal1z1eRSLPI6GDk-J7z1mBM9DObG_rVhIliYSHOMXCo8nlY5HHjshXE1VwXz4v8hvd7ZpiLKkYcItbNAUuLaqH2KIMfI4d95BKpZvC9RnA9SwtfE5me_-lHGlMzebr3FZFN2H-asBDrPf2Gzia_pA7jbsiY7s3KE-Ra2a8CiX284RMhLVEhj3H5-W7QVRwB10WKjHYG0KrkUQtUI8ZZJgeKV7Tn5_7MbQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
