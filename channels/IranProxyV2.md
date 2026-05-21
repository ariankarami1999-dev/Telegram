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
<p>@IranProxyV2 • 👥 38.9K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-8465">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 91 · <a href="https://t.me/IranProxyV2/8465" target="_blank">📅 13:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی از ساعت ۱۵ تا ۱۷ دردسترس قرار میگیره
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAgp-u3WftXL4-MzjU7BupEV3oOewG7a8sqbcx43cS7pNDsn6KPliqAULPHg9iF70PgLNy1ldAW9KWQrM16lYYoGhj2Qh7kApdruKkFCb7wZvT95bmrD7SavLOj5GGe1Y11Q2ZTeI18FDn2thhDv782HY9i1giOUh6YoemVbOLz-s9sr4qPRs1BtDcZJTni8rCGMv1xJ51VlMbJqRldoysSONjcLfhyjM915_r2Goib9xg79CIuhgaSFsVd11-8nIPW_wxuQMIdrfoWlwYPGvLTDdWFqfbA2JNXRCbhjOKr86Pj69N_Vufvedx49esXLmuYDnRl0cDLsHQoBymTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvstZCMnb3Lg6Xe5cHSl-dMcMwukDyea2pB99Xfgn63DUKtdQXUH_iAXIu5WdCMk3FbKBbeIwwC8ZQ7hsHgMW8TT1TZcdn0GG-1lMVwrHMzoE3mzA0RH5slvdZxTavC-VoB89t69CAKmgA75O2WILyiUabLXBT1gQvFvC6yEActbxoc4q6_VX6z01IRYmcBJ4Zo5qDdNV1N0oY2aeZMahQzIG-L_TNclCuAVONays3tCdyI6dveH78d0D1P9nR4PaUyayepyce95Znk7Y8Ihc6tvg0ab86J6RSlgWVWWsiCAkewfidIRKH-S-RQ8bC-07YIJQDN5GwYkWZmgPmdJ0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9kowwDwFv_FKX4oh8jnIzWEjIOjFWMLUmKQ7eRAbn5kcOqUO5acvFLZQEDKyE-TDR2qRzazD6Kb_ci4Lsbz45dFwC1i56GqPvY2vN6icdouybPLi9rRQjTDyxcrUg64Cp2dQiGJSZ99Za-an-K-gGXcsWjai1WfO27nCUkknTFQYoRntkRl9cK97qohRh3wJiZO5X1MobsRsnf4YNCiSbFCP9GtKDr9cAfLi8H6yDSNsK59xM-I4qbgRP0gdKFQafQM4OG3RaWuQe-PJszSe4um7J86YMoVs14QPP29mNKfN4IOm5cx6h3rEadoaBzWx8mTqS-o17mok1C8ojum5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b68Q1i5BbyLfXf8jr2lZJqmsemk0vPZb00MQoUzev5m3FZOOM5TiI-KXWD676ELnSUGnb4sKPLthXp8OsiGpzzOux-pyK-2lV1X4y9IERpOofxR8tXHDeg6KBvlt1aSN1GcKOjVpgID4HQsk-kitvfGhvCEpAKjooUWfHo48T9r0UZT1zoT4B5H0ArM3jO0xFDq43MhGUxCrWU5d7cpxfgkYh7-lMzxwuQ-Vo_vWZ-ZvyBHUPz1W3SIYOqZqNB8BQNSDG3193_C7Yj-J3AM16GvUUI9fx9Lzo2KwjQUj5EQsvmOoMZWY1ZDFpUctIsM2G5z5cypCKxcWQbVBztgkyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmI1A4_mgd_0pyr3TgHzcnGafH-kQ5H_G1uZqOQ4zfvuAKBRstZZ6iBrmWMuJrYVvaec92FSTobZXcSc6Y8PTBSv5PDmrY80l0oyQFv1I8P89mxG3vm0sp8T2lfAj633NpsszLxTcun6PkRfZu9Hkp8E9fpHPIPwXPCto7SBLxcSv9icWjg-WEtmCGMDGPeQ986H_4OMCk7YZBgJ7voDAX6LkHwI1rPW-9HhmIZ8fVC6mtnGQvl27e0jBryxqV5tArtAnsrcu7EO_Nm0gdUKjHSsBf4-oRXVCbD050QlzEARLqQZ8FA4qyaNsgzmlrA7MBEuDfFT3qjLsKS9phXAiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=ix6JMYOfKoy9Lh6iA58Qb9i676IlGXAi_TbDWwur2MQQBBuYx8GLXD0MSgFzVG0atyHQmy7LNonDGufn9IPH_XCQPCL15jqt3Zi-MI9nL8z7nP9gqKBC8nHp7IIuoI0YWk8BmMGgdiIQV_wabLpK8-FhiBnLNTl41TinfiJ5ESCeu3dsWKXFj4sq4XqLtFL39cOykFnco-VOHKX9KgYDJATEO2ufx4Hp0pgLpHPG9CSAl0sKWg657M0nP3A-GUQbyg3IIo4piJDg1MOmvRperYG9oas99xM-VG96_ZXY17Rsyer_gGfQpqP9CGFzXMegLaHnxeVfZk0w4AJo28TKJZICGcxStGYrVHkszGdGsKvWMV8NK_GlITIg1lQf1x6Ju3y9N1FPDJV7HEGXHXmMPKXJAW6KFj4xjoqtk1zKzLVuxjgzjtPJXS_EUlrFoFpuRfFOHRdoQS6FGXeKp7vPr7w0sGDOd5uuQBX9OGzReNWIc88551iqLZhtVtfLQSNRqW_q7dnjanZX89eynNYzFzUiFUv1bxn3qSDJEnd_Njwgimu97V4-emCzwE613RyhAasNz7kjrhg6ODjbidrgAdBnHkTws886WLJB_pWwyeYvIRPgUIAOEjEg5ZpwWJTerPwbwAzzJDd6z88IKg7gvK8qJPt9HgKKhMqa3FkE4uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=ix6JMYOfKoy9Lh6iA58Qb9i676IlGXAi_TbDWwur2MQQBBuYx8GLXD0MSgFzVG0atyHQmy7LNonDGufn9IPH_XCQPCL15jqt3Zi-MI9nL8z7nP9gqKBC8nHp7IIuoI0YWk8BmMGgdiIQV_wabLpK8-FhiBnLNTl41TinfiJ5ESCeu3dsWKXFj4sq4XqLtFL39cOykFnco-VOHKX9KgYDJATEO2ufx4Hp0pgLpHPG9CSAl0sKWg657M0nP3A-GUQbyg3IIo4piJDg1MOmvRperYG9oas99xM-VG96_ZXY17Rsyer_gGfQpqP9CGFzXMegLaHnxeVfZk0w4AJo28TKJZICGcxStGYrVHkszGdGsKvWMV8NK_GlITIg1lQf1x6Ju3y9N1FPDJV7HEGXHXmMPKXJAW6KFj4xjoqtk1zKzLVuxjgzjtPJXS_EUlrFoFpuRfFOHRdoQS6FGXeKp7vPr7w0sGDOd5uuQBX9OGzReNWIc88551iqLZhtVtfLQSNRqW_q7dnjanZX89eynNYzFzUiFUv1bxn3qSDJEnd_Njwgimu97V4-emCzwE613RyhAasNz7kjrhg6ODjbidrgAdBnHkTws886WLJB_pWwyeYvIRPgUIAOEjEg5ZpwWJTerPwbwAzzJDd6z88IKg7gvK8qJPt9HgKKhMqa3FkE4uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=OeqkzxJJQ1syGeBll6TD895tUND3YLlu6MeKtByWB8q_DdfVaY_gkQuWCClKWaq-ql5fCAzD_aSHVDbqFWiuq6oxFwmlfZBgfIFX7o2JorImvoEeTde7yyi5RgVW5o_KqLjATb_34r5vMh2vkzou9NtlJNCY7UmEVxFgK-m1fPDHlC948ri2NbBPSnHt1HtefAiPUowhTXigherqLqFLVVAlxtj0bWtGluVidERk79mZgZZah-uvQSKTAz6YqvHoj4AyUh70YqAMIlGakJ5ZkA3zpPu_9Z9XihreOC_FohPJZi-Jhom3k6ZzLW-QFcrvTh1_CqYdILO2Wq0ZpR_StDSASCGIhWXztEuqs8nrgtYfN6pFAuVeoccDHqIRPnJd0FNJJh7CcZ4dY-ljtf6c5Beigfw5WuLasJov4JrfUPBv6s7XmZjZ4Pa1qnjzxMjHv14PzNUJ0BoSezp0MVk8HOIGwX65p82B4Z5JOqLzo3I8WiDcNqafed1EYMsWl76Y6h8x6Aezl0jgOL7M4jS5cJflenSSuFl76-nslk9chGmRofjEmXRoduMjohRT96jheS42094pdiTtQYDpowaP8u2_juqzIcD9PKaWO3ulBK_2UCf9Lpl7uL3oHV0ELCOoBblAfjpf718Ts65u1P36kvvGdvngRcbCDbiVan6iVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=OeqkzxJJQ1syGeBll6TD895tUND3YLlu6MeKtByWB8q_DdfVaY_gkQuWCClKWaq-ql5fCAzD_aSHVDbqFWiuq6oxFwmlfZBgfIFX7o2JorImvoEeTde7yyi5RgVW5o_KqLjATb_34r5vMh2vkzou9NtlJNCY7UmEVxFgK-m1fPDHlC948ri2NbBPSnHt1HtefAiPUowhTXigherqLqFLVVAlxtj0bWtGluVidERk79mZgZZah-uvQSKTAz6YqvHoj4AyUh70YqAMIlGakJ5ZkA3zpPu_9Z9XihreOC_FohPJZi-Jhom3k6ZzLW-QFcrvTh1_CqYdILO2Wq0ZpR_StDSASCGIhWXztEuqs8nrgtYfN6pFAuVeoccDHqIRPnJd0FNJJh7CcZ4dY-ljtf6c5Beigfw5WuLasJov4JrfUPBv6s7XmZjZ4Pa1qnjzxMjHv14PzNUJ0BoSezp0MVk8HOIGwX65p82B4Z5JOqLzo3I8WiDcNqafed1EYMsWl76Y6h8x6Aezl0jgOL7M4jS5cJflenSSuFl76-nslk9chGmRofjEmXRoduMjohRT96jheS42094pdiTtQYDpowaP8u2_juqzIcD9PKaWO3ulBK_2UCf9Lpl7uL3oHV0ELCOoBblAfjpf718Ts65u1P36kvvGdvngRcbCDbiVan6iVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
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
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OADW1PNECgVAXd2PMfYjmSMTR1DXZR3Oy5V4fzpnnNTvRHH0lMkja4dndnBZXnhdCWcnRlZnBIaKV-4PfMthYOdwFO7DvdcnPkUQY0KX5qYCusDMHiSi9iAoVKo1GnS3h5PjtlTv8GSAViUu3vAdS55NjhGHABEpRb4kEc_NitI0C6BL-4tO26EvSYhZmeTGy2xqJxtvLTPFzjY8r6Mc4xPx7FidtsOpMykss5vHGiiFu5M9MJar7ezn-KcFMcvX13Hc7JLY8feZbH0MR6b4Tji_iyihlUEJllQVt_eB3Bs4Wqw5873d8aElgaKMTMPylcwIQbSC1HQhuWGcklZKyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=HY9FmgIMrkKwyZN0OeUAhuX1uHgEV8BKYKtdFDdBo4-7kQjiZFIP2AaideGOfcMzPNddReTGvcSFhQ4RMz3TEI0Lf4OQgwr4W4ZHx42jnA4Gz_vUaZH0iz3GgdL9gRVs0NzcYIduWFX893BuaJfCMBCNK_d8SbtcdG89NKLfvzT63gfmMo-JTxDRSnlCBVmYZgMrMniLZDinmN5Y7Ud51NJ69rNjQ9uF6tmljCM3btc20rmk-HlqiXJSw3CCS7diroBNMYO7MgvePydZilVfvJdbp1NG2IdPw5hyWM9ZlvFAZfkz6UsjL0uZOSPBwKdB8zuEsaGamdem8pBGg4mJChCXempeqpQQ2EtQsUAWKFJ6bguJ1ewGohvojX5-Dw5mXbjcGx3dDGLdnsv6OMEcXjArZEZaNeWZyCRaMmKCbr-C_tA76MJMcO1QQ2puMTfu6f0k3_juqYFrqdXD3qbFMIehPn9H4pSR7yw_-Km1WGDk4reRyhNtlDUbqn2qqncfSt69E2Kqt80JnaMO-m4tFf3McD9at6sE8RbhzIvhVpUAU-uzFqzF2d0t3DpgNNP0v0WRRZDrQwSzIGQos0sBTAmNdKgZCIkYaDdVvl0I52896rlErgsCr5NB0FKJRzJkP8gJRTuaP3x2cfIwDHRdlcWinoYz2iOnFmLN48XduaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=HY9FmgIMrkKwyZN0OeUAhuX1uHgEV8BKYKtdFDdBo4-7kQjiZFIP2AaideGOfcMzPNddReTGvcSFhQ4RMz3TEI0Lf4OQgwr4W4ZHx42jnA4Gz_vUaZH0iz3GgdL9gRVs0NzcYIduWFX893BuaJfCMBCNK_d8SbtcdG89NKLfvzT63gfmMo-JTxDRSnlCBVmYZgMrMniLZDinmN5Y7Ud51NJ69rNjQ9uF6tmljCM3btc20rmk-HlqiXJSw3CCS7diroBNMYO7MgvePydZilVfvJdbp1NG2IdPw5hyWM9ZlvFAZfkz6UsjL0uZOSPBwKdB8zuEsaGamdem8pBGg4mJChCXempeqpQQ2EtQsUAWKFJ6bguJ1ewGohvojX5-Dw5mXbjcGx3dDGLdnsv6OMEcXjArZEZaNeWZyCRaMmKCbr-C_tA76MJMcO1QQ2puMTfu6f0k3_juqYFrqdXD3qbFMIehPn9H4pSR7yw_-Km1WGDk4reRyhNtlDUbqn2qqncfSt69E2Kqt80JnaMO-m4tFf3McD9at6sE8RbhzIvhVpUAU-uzFqzF2d0t3DpgNNP0v0WRRZDrQwSzIGQos0sBTAmNdKgZCIkYaDdVvl0I52896rlErgsCr5NB0FKJRzJkP8gJRTuaP3x2cfIwDHRdlcWinoYz2iOnFmLN48XduaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsXV-sAkpzZ2Qnf7k3kIxr9gMzrtK1q5cfNUT0qKoB5U0Yjv7rJ0rl0IiHjJjdvMzIReY9rESMNcEvwBsZ4KvJ-wnTleboq0VXFk9R3NsWLqoLEVhUblfR8rHuZZuVUNcl2V6gUFaCdwPYt2P2CUvAMwcQsxYP8p3MipTQErjDRwG0aAh7Ot_Gg5-CrhQ6ZrLflMcmbyXI-uBp3C4uZx8WCQS_Bb0PnnB8MbmzO_zMiEGGn_4oAIpotB8QXau6Fkkco_ItO2Kov3LJjyRVOcctF1wdMu5qgJ_SEOb-H7a-r2FLpPpANTxazGLTnUMHK8LG3Ep3Vt11gS1mhpVsU0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwnUqjO5Z_SrP2sbp2B9pqloy2Tu4E5o2OQzZ4g42D3uu5MGAcm_EslyMGXPjK1efhnQd449z8zkrdNydQXkvjcXyhlEP8CTMYmTPtQ5yZBWfNJ8pT9UhInAAlR297LCwnM7PGUeyvTXltYahqQxSErXTddeExrLCKbiw-RWPBXeDrZi98-XIP1EEHiXSqFOgrdHDz3D1hYtbGHgrhtnkRzRwqYeu1cCrHr7aGtukIEy5bgjVaDnFpmC6pT5VIthVbW43nFKJhH7xGHXSqsVIfxl2Tj1NAuQp4_Lssq6l6zIJeaBspXU2ZVRBFcqBEkKfWxJ_gdswHU1pwc81rEZ7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=gz6Gyfme8VKI1YpoMUUsIkw3Fd3wL1vOq9NfmpgH-DF2l2lf6Cmiq94eqhnqK7ecip3D1pbOCrly_XEvAHiwYjYb7daadYJ7sLS-KjnL7SP1sqTfMdtuw3F2jZ8RC-bj_WWNrzfeTC2sKZ0D_r-HFT3KtfbrdUg_eU1mYH3LqCQuu95Q8mkeI7EPQCXc-nPYRX1lI8_JFFvnUHRczD4VbOdAPNLxdiK4AYl5k1WzfRFLqwMT-yejmsfjwv2I_KkJC_18PyRi1aM7yKVR4TylMZwreokj_rpduR8h6Pxbfi8TJG_QQrfnUDo93vcPpoIM5EGUYzdHW-TRPEHjWQjEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=gz6Gyfme8VKI1YpoMUUsIkw3Fd3wL1vOq9NfmpgH-DF2l2lf6Cmiq94eqhnqK7ecip3D1pbOCrly_XEvAHiwYjYb7daadYJ7sLS-KjnL7SP1sqTfMdtuw3F2jZ8RC-bj_WWNrzfeTC2sKZ0D_r-HFT3KtfbrdUg_eU1mYH3LqCQuu95Q8mkeI7EPQCXc-nPYRX1lI8_JFFvnUHRczD4VbOdAPNLxdiK4AYl5k1WzfRFLqwMT-yejmsfjwv2I_KkJC_18PyRi1aM7yKVR4TylMZwreokj_rpduR8h6Pxbfi8TJG_QQrfnUDo93vcPpoIM5EGUYzdHW-TRPEHjWQjEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmQWiesP-VsizwroQYvAO6MDCc8A7ECSSMWd6i27RFAHGJvXoLNFfX6C0HR_L5gSr7gW9Zvns7gVGR2Mi8rVOdXxGQRNS4nKa-_0Qajds1DdGVng8USO39XQf2P7kT3tVUKKTJHliy0IZgJnvnzY_tduhcBt9sa3da3k3BlKgnmXEDMM-Nrze_GobeKmzaz04GjZGNFeV0riPj7umcGUsuWxoB4gQ8W67HFYC48arR8gm_iP5ZEysxv2uJDxVWWWmQ4aK1QqQAO39Vn_PbCUeM7-8D9mZyxYCSp8-cDrzHMuNAgEbANa0A8_x8-yen4Ptae-6XklQc_uEipKsm1Lgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2z44-77fuJkRwf0L9T9pWSvRWZhZWrGAQ6YEaGKPf3l3xKqMhdMX26I5DJwQYWKRbuYj_pZhF_0WezaXTX0vFAAXzp9Dzc-Cb1TY0lK0JrX2qAjkPIxqQ94vVvrUS5NYm1KOzA3xwrYck_-Ivw0MmUQ3pSdo6pWKDhwBzGh2fPzY7caAN04KYXiwRV8VMIt93S4p4-f4wux57dc94aaXjcVpxFGJEYcGnE4KMN7D-QdUzm8gkn6dATuLnb4Fzdr_dggOim0xgADNJYVJvjFQN8XHnLkiP2eI9vtiJwVPaJiSTK6e_JvmsDebOBcrQacVmBKsJ_jKf35DwH_azvhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E70ReEgNfjbUulguYpsMd0efILdzCpv7aC74hBsILHV-esrVjGjnfD6MkKw0vDLiF6S7VnLyitNG9Tr1TjxmJ4p2UJgw_-saKMipDDacAiSVZwhGUzSFpp3IewZFCpBzkL5jM7JbnivZw2p9964XfXsthT-VSgrdgJy7_o9AjhTm46Ixaz66ut1vI8T6vXsC5mfMtwlDVc5LD_y81JvfhR1g_wXlvij7_X9Y_UdhhHdJ2PFdgYHq7pGLpEZ4ZZOb0BwPReVTy0MsrSqOWRTlgqCNUi02qALnNOm_zPznCE3Z3-Z_bTn60PDMojsi7cwtFkpMUJ6dmON1JmgN4q1diA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=CG_ZwhRrU006HcDrWw7koxnbOVc4tHy8EbWCKG26_NMStmyhUCZSrAvGaNMARaFOhv2HnTbp8kcXETxBVZkrtOE5fU5VWVtnZcgM7Y3Jp68Ggm-_JJxVWs3fIScF4490Glz-I8Cbl9uMvfF7WxH7G1qdsismla3hysR1roc4kk1Hns0dd81Tr7XoBHPDUrBmxRVaPVD0-Jq7Z6Ujj4c_1WpyGl4xK9iRjMDxVic1oY0Iq1jez1eNoON5oxGVkCxCbi6JLZJppXGGooOUjivgs05UIqzYjHJ1Fwuvn-ozlaCkZCg3gmoaw8gd6qZLC82DbVQ7G15ekISclnKK5M_0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=CG_ZwhRrU006HcDrWw7koxnbOVc4tHy8EbWCKG26_NMStmyhUCZSrAvGaNMARaFOhv2HnTbp8kcXETxBVZkrtOE5fU5VWVtnZcgM7Y3Jp68Ggm-_JJxVWs3fIScF4490Glz-I8Cbl9uMvfF7WxH7G1qdsismla3hysR1roc4kk1Hns0dd81Tr7XoBHPDUrBmxRVaPVD0-Jq7Z6Ujj4c_1WpyGl4xK9iRjMDxVic1oY0Iq1jez1eNoON5oxGVkCxCbi6JLZJppXGGooOUjivgs05UIqzYjHJ1Fwuvn-ozlaCkZCg3gmoaw8gd6qZLC82DbVQ7G15ekISclnKK5M_0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=SXOLhT6IwW3X26l4buKF2VIYtqBY2Ic2QZsa2pN5rpFChc5a8k0wZfwrfQTOWme9m1EVurAqRHU0AEbVg2OnNQWV7bduSso998WvgByvcfAuIcyVeNIUTQubr2nM_H5XU2pJwrTM6xRQIxUe38NigPdnQjMk9u0YIT_40QDR_gV2r-5eHRbq9rMdhUmPMQp1XEAtkbbl9WAotK7lbcthF5UFMX6b9MMJYq6Vnl_i7XlLwBJHATZe62ez1J9voK7oxntFoJQmR0U2sPdak4GVlkwBsDknfMd6lH26DapCcVgOCTY9OxobAAqyVHcQTOV8R-SFyCui5eYH_IytEdd2g311T-VC1oQ0iZtC3rG6H-K30keQ-WiXp4ifKk6RJ2MR-qSV57kYRSYWCkBu-Vb0fW1gtW55RaflM9vOcx6IoFz3Vbo_AtVdAC5Zkmvo3cnkeVQDXfFWKIkXXQQQr7yvcNTZau2ShkoWcWouT3zjMwYomtl7H8uWq-ll6ci8ht-SDmRQHInW-ezP0pWKz3ZcGxtS_S6CDzy3PVVdyDQOGVhQSq4vbgsfgZL9le_-vg2ko-WbmjWU_X4fxX8_11DP0-oimztIbzmrs24qwnwIpNG5JzLhNthAIEaqm-mZjQuhbGchZkQl4D7-0jFalQulzyS2vGCHbOsoUayGmmXZUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=SXOLhT6IwW3X26l4buKF2VIYtqBY2Ic2QZsa2pN5rpFChc5a8k0wZfwrfQTOWme9m1EVurAqRHU0AEbVg2OnNQWV7bduSso998WvgByvcfAuIcyVeNIUTQubr2nM_H5XU2pJwrTM6xRQIxUe38NigPdnQjMk9u0YIT_40QDR_gV2r-5eHRbq9rMdhUmPMQp1XEAtkbbl9WAotK7lbcthF5UFMX6b9MMJYq6Vnl_i7XlLwBJHATZe62ez1J9voK7oxntFoJQmR0U2sPdak4GVlkwBsDknfMd6lH26DapCcVgOCTY9OxobAAqyVHcQTOV8R-SFyCui5eYH_IytEdd2g311T-VC1oQ0iZtC3rG6H-K30keQ-WiXp4ifKk6RJ2MR-qSV57kYRSYWCkBu-Vb0fW1gtW55RaflM9vOcx6IoFz3Vbo_AtVdAC5Zkmvo3cnkeVQDXfFWKIkXXQQQr7yvcNTZau2ShkoWcWouT3zjMwYomtl7H8uWq-ll6ci8ht-SDmRQHInW-ezP0pWKz3ZcGxtS_S6CDzy3PVVdyDQOGVhQSq4vbgsfgZL9le_-vg2ko-WbmjWU_X4fxX8_11DP0-oimztIbzmrs24qwnwIpNG5JzLhNthAIEaqm-mZjQuhbGchZkQl4D7-0jFalQulzyS2vGCHbOsoUayGmmXZUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI1h8kM5KHk4pJnQbPupolfz-KrJf5cmyxDMmaOZmQzrAO_Zo1OiAQgLJd3SfhJf6V7_3wQ3UDccvM9NgYLNV76UKuS-R_QR6Nt-p5c8BjAwvcCT5UnCfZ245XjyvID9E_lzd1FmwNZiYmgImoyGFGvqsRlONlQZGtEzLB9Q-Sk8xYk-jsITcFz2jhIy14ZBMBBE5g-2EsNGGrlxQK5sgSTRbFQJsWHYdDSjnv_NUl9yiC1Ts-Y06VgZ5giqQj4_K3maBdqMVzQ_-Md1VbdO1fcNYRh4amNR1OSEDZLYGmGNxP7gsUnCSJs-xWFDwiEBruH8C8ToPY1nxK8Mk6ScoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDF1if13YRvYFVqUUa4q9GWWbxH3So9ZzsIXmUvd2LBsVGZiCGBeU6UnQW3DB7ZrZ8yRvYqkpChZq2305pVC1kieEKVKMEdBrl7UvQkRa36xZ1GsgrxLvMpSuYW7obvkGaQEd5CfXWHw-2eVcF7er7EsZFFR_wvuNJxfCagBYqChoCavHe1whoOpS0qwdPXSncVn9IBJ2vkS5ajYVFTKoF9kMj_2lOhpusEhlody2tFxJdvQe0kxkHEwCm_2yQUhzyLCKCTnMgQrB_GMLBuqbHh-ewfIyGJXjEE2OZ9bpaw9XDnqWYWRou9ojdla8PhtSXcGDhBQioYEYHx-MX0dZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Git-JFvP9pbadYX4-jWmMb9BfeBAAcHslAp3BSUT1ZmdaYEpFv4VkvN_LKwzRGVCrwzX2ckspowb0sMru-YK7OmeMFn7JAXPD_SOzF1SQtN4pEV2oHWNiog2e9kcP3aew3i097rmprKe36gym-MBrHR--cI17dDq0MHoPCaKUNWKlEsfycv5j5OvReLW4G3d_BmQlO2OogJtVx55kNlKq5WsOvQw9kCNxgwivuMUJVU8kGz5bUSLMMEXIhcwcifJzTkx9vxkT091m8IkcHsAhWKZdcg1gtoAekm8TvFslr_mIqTunw4pIyUmKerOHj2cOWataXBVTkfPhCRIWRZvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=dlvQuVwaIiE1kH2C6quTzLJPVXYZ2awFgQHQWE4FOb9pF36y9Ky1qRo1Qfds5HlrdDGybrqKvVbVhPxrRC-iH6we4APkb3r4ki9RKCeoVgokBO0iWy9sD3Lv5xBZlZ2R5OUeibSCYMxo-N1GdUWzM-HHKhtX6a8fnVgjPS2DWZHAC9k-lh7S_D5o_6y_o86ENxHjnSib6hyxHS-JrtRLEEkhQYeMkM178LrUWo7OGSTwI_lbz5Stf9VmD9UV5gL_uB2RM-4msmmYR-8je7ZErkcW3MIjRFPhaqdgDbXC1WNXLnuYMWuUyl9zse9FbDqp8M_NvxpP0ndrkWdzCE1315yMnUGtpkKfeEA4RorkMN3j1b7eumtb8TLacldA9gn_mGe-WxnFOIOX0gXdjFRUjOupovI_A27PokAvql_1tztlwZTs2h929Ma74FldzXlOAHNMmtzVf82pjiBubFlIc6pq4BZB8uY0g9rSfRp3EQwUvwgouzRUvSOLsjWy-2NcUq0Fr38HgccIrjpXR16wPKiaf2RduZAYXY-Ts7yBso6rSC3sc9AmVUI9xFXPgF0hBFyKB3_Tfw1lAv8mbpeTJ6qPWkjkcYgJGLO31X-0RgbGUN3TQlH3GjcMZwQWTjplNZSc63WBmPUPxblWckhOsnf2DZnBv-TlkuSVTHWkvJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=dlvQuVwaIiE1kH2C6quTzLJPVXYZ2awFgQHQWE4FOb9pF36y9Ky1qRo1Qfds5HlrdDGybrqKvVbVhPxrRC-iH6we4APkb3r4ki9RKCeoVgokBO0iWy9sD3Lv5xBZlZ2R5OUeibSCYMxo-N1GdUWzM-HHKhtX6a8fnVgjPS2DWZHAC9k-lh7S_D5o_6y_o86ENxHjnSib6hyxHS-JrtRLEEkhQYeMkM178LrUWo7OGSTwI_lbz5Stf9VmD9UV5gL_uB2RM-4msmmYR-8je7ZErkcW3MIjRFPhaqdgDbXC1WNXLnuYMWuUyl9zse9FbDqp8M_NvxpP0ndrkWdzCE1315yMnUGtpkKfeEA4RorkMN3j1b7eumtb8TLacldA9gn_mGe-WxnFOIOX0gXdjFRUjOupovI_A27PokAvql_1tztlwZTs2h929Ma74FldzXlOAHNMmtzVf82pjiBubFlIc6pq4BZB8uY0g9rSfRp3EQwUvwgouzRUvSOLsjWy-2NcUq0Fr38HgccIrjpXR16wPKiaf2RduZAYXY-Ts7yBso6rSC3sc9AmVUI9xFXPgF0hBFyKB3_Tfw1lAv8mbpeTJ6qPWkjkcYgJGLO31X-0RgbGUN3TQlH3GjcMZwQWTjplNZSc63WBmPUPxblWckhOsnf2DZnBv-TlkuSVTHWkvJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBqakX-hX8TUqVCGbtolDx9BAY0y3eIBKRd5ACuHk3yShyMYik_CB9yX0YotAUgsKumGk82KGVMVsaxY7ibfqzpXMVqiWGF18TTTofVXrbDLjAvLk1S6MEFD5bosRNwz6R1Rt6uWm94QDwUupZOSZ56uW2Db6d-1h5jb9LFUS5VKygVBLhQxRY8M1VLVwc6LjnJqZrwpjZG7mk-OxM0TvOPvlcri7xrV70GaPVqGcqT2MMYQmLA0s1Ajy5Kq-WF7gQmZA-syvVoAzuKn9QBDcyBU16CcXeltNOT-Wn9H2_DTwCiRMxlp5-QqLDyj24OuXo6hXsaytzCBqsrGqE9e03cM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBqakX-hX8TUqVCGbtolDx9BAY0y3eIBKRd5ACuHk3yShyMYik_CB9yX0YotAUgsKumGk82KGVMVsaxY7ibfqzpXMVqiWGF18TTTofVXrbDLjAvLk1S6MEFD5bosRNwz6R1Rt6uWm94QDwUupZOSZ56uW2Db6d-1h5jb9LFUS5VKygVBLhQxRY8M1VLVwc6LjnJqZrwpjZG7mk-OxM0TvOPvlcri7xrV70GaPVqGcqT2MMYQmLA0s1Ajy5Kq-WF7gQmZA-syvVoAzuKn9QBDcyBU16CcXeltNOT-Wn9H2_DTwCiRMxlp5-QqLDyj24OuXo6hXsaytzCBqsrGqE9e03cM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NRVgoKishXgSZOgiSSq5o1A51hc2NWwg4ORr8TcsZ8Vd3LN7G4vvlKlglVB3duebJYYr3rZ_YvPT6_wh1T4uVJQAwHJDqATLizxHEo6QzTJCIgvk3gvzY14b1v2FrLk950r3K2revbkW9di0HN_B9uk0_GCb0qA3K2ZgpNt1Brfm2VdXx5VADr-FO-RzgF1LrGzmF6Dbh9hexa_XFcgGP-dMUqgCxa4o9z_TLx-eV7iZ38Pjky73CREa3ze4l3xALtH7updSof_2MlNA-iD2lE6Qe6yqME9wolxbDUyAIflNHY4Nfup2Yrg6n-R0d_UmfHGfC-sA4VSUJxMW7aDbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
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
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8DevVbWk6scgrhvNjjeF5m4likJPCyWg_KT00tE94d5wzlPcGSRZT67cXypV5X4JEmvb8my9s3_79VUxGDQ3cOzrtsqqjzMHds5pwjB5K1r9tVybqF_u1lPTeEk1tTjRcVFlQcyoCTItf-eFyOJHSgEu8jFhy7lNdqZMQg93ayB4XTixZE7CXObEzxu97a_4k6DzxL25iutvHXp4TLDB2xb9D5HD2wBSZjuiJm3dzuFI4N72BD5YCMBNBPLxonH6PIIUh1DBtia9A-i8FQV06mUrEi7GCCkfQVcVi3yDr0QWqrV4lGY-8xU5M4VUXb1s_fLKYPJBEWP3TFvzds8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=PBEAKluCi-cXEo6egX-YkUJKZggdbaXYHZXl5X4F_3-ZX_684cY9sDCvWRSNTGvahlJJX5nYXmc84BDUBMhAdn0uRoTgYlCeV1HSVwN4ked4I8QqhkdDyzRIB7DbfvpjtXa1DzbUBv-8rozPk6kPQjLj2hh9r8uDtAMmbtwXbbcSydu2GVVHpPQJw3wjm5av2DlfGZvsw2kGa9SrvjQO_QJZlyA6MVyKKCsH47vlP3QixYGDazaqgMBUyAjnNHqR1_dFWkFdj3D-Xab-uyWzD0y6HU8vRcQAc96p0XbMCy4pAIun7NUUQ88vBZmKef1cp0LzJyJf3mT1Hvj4Nozr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=PBEAKluCi-cXEo6egX-YkUJKZggdbaXYHZXl5X4F_3-ZX_684cY9sDCvWRSNTGvahlJJX5nYXmc84BDUBMhAdn0uRoTgYlCeV1HSVwN4ked4I8QqhkdDyzRIB7DbfvpjtXa1DzbUBv-8rozPk6kPQjLj2hh9r8uDtAMmbtwXbbcSydu2GVVHpPQJw3wjm5av2DlfGZvsw2kGa9SrvjQO_QJZlyA6MVyKKCsH47vlP3QixYGDazaqgMBUyAjnNHqR1_dFWkFdj3D-Xab-uyWzD0y6HU8vRcQAc96p0XbMCy4pAIun7NUUQ88vBZmKef1cp0LzJyJf3mT1Hvj4Nozr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eMJBA457Poxkxly5OgDqeFCq5BJofvIobQZcKWA3kdoe6UdWvBuc2-eJ5E-uh2fqd6lrMstONevbmKXNcWU4_w1bf2pG3wKvNVpXgIvLVZTJHwdueH5eULXlS13HYAEMBWh8NCBJGUViasGe7Mw1Gzin7x6Vd1Gcvrx2_ewXQNcVva4MYtO2w1cNyTrt6WsuxoJzxgzJdfIyubd-Zbzd3s3mtI2iknmC5bzkbWniFwMZHo4CkpcNqqv9rSYiwO2topNTWgtTuStfgNUHQyrqpB4zXfixJAau_l00J-3lY4X2gS-fuu8PzEm_qJZJkRGJBnjMIsoRnoaiuOwtB6tiMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAS0SUXforKEkMC6uWGw6Rgq1ZVF_5ei-kCuU1n22zY-P43PdEkPsRbgAMetOMfokv8GWD8gSIfYajR-tH4QV6TvZpLrVy2hPLyADNiUnpBXp_TwVjt4L0fdsfhbW0ysmx_gsQ7oH-BvJObUnhmWhMYqqnovOD9eAeA3Gw_u377fnMArjX_wAQ0Ta__BSF1_PWxIfHtNv8b2Xc99A-NK3usbkjjQhwNfz6HMlrQaGvIM0sFw1fUfc2_BQMugE2ASZJ0Refpdc0dy3w_MCRVJ_8SWxJbLLhzrnhIHhMBpLYWrjXEGGSpF-FuIK0VMYz4w83rVGP6SSCuNiyxqAE0pbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKuXJ30OuaIfmI6K-892YXSRTbySJvoBWR9PKMv3aDVc7T0QYmA1HbmDGdE2VIpWFciYnwRXFItadPGSqORTkdVKdcvkVWhLVJn-U4VV-CFdAZ_nRAZcxryOSQvCGNgNTmLqsvOIAsoYIPowWo_dTseoovclM4tPSOorQU3nEcyqLoGi1dbgqBbW04gcaLTYrwihzcgPIWk9Z3pfSWPWHIc3-eHxcLQ93lZNAeIbZ-LrN_DtTROAnT3bu-VuUJ_6t6BZEKfGkaWE1xalhcancBrjGMTh6QDIjiGm1dRX00kBPjCvoA2vSqIrPzqNSd1qHLNlL0L1_x3F5xPvcZk6ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
