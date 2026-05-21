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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 10:14:44</div>
<hr>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAgp-u3WftXL4-MzjU7BupEV3oOewG7a8sqbcx43cS7pNDsn6KPliqAULPHg9iF70PgLNy1ldAW9KWQrM16lYYoGhj2Qh7kApdruKkFCb7wZvT95bmrD7SavLOj5GGe1Y11Q2ZTeI18FDn2thhDv782HY9i1giOUh6YoemVbOLz-s9sr4qPRs1BtDcZJTni8rCGMv1xJ51VlMbJqRldoysSONjcLfhyjM915_r2Goib9xg79CIuhgaSFsVd11-8nIPW_wxuQMIdrfoWlwYPGvLTDdWFqfbA2JNXRCbhjOKr86Pj69N_Vufvedx49esXLmuYDnRl0cDLsHQoBymTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG_zvnvpVQmnzaNC5q7l1dupiuasE3570KfH1bCUUQvypZn-qpmE2HaB_TzcV5V7-b2xZ9Oq64OQ0sk0s-YnsIA8bhw8mGWSN8nuIKSE_1tUSamKqevPQ9rrlCTbavSoyaUOg1rr1MHz0pWWESqmvP4md909NpL8QbgUEm3jvC5mAC13ylLEYbzxXBLMwVuKl6vfyiPkqv9GT90AMLSoRVtU8zriOCDmEkHoSnh3I_o3bDPvneLb-KfV-dKa8kxNQbxGHw9znW6gRRSmUrNHEPA1l3tvFtaCNKC0ATh1s9mlAjMtT1wuAiZ54wbNSozXomLBzF63LHTYOD65v_wAVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSo424Al70KNdjiV9-GqchKzRCL6Rmfq0DdK-PmjoMQRwWPePBljquCjkbJxjkQwt22E0URIcJImbxpkpt3GsA_45rVbZT5BWLjo8qNRNrwVj9d0Lvm3vdwnC1e1uZj_4WK7xS9ZCd77Z3DywZVASIa4N9O6N8kltWCuB5XpWf7u48LqkDNh1NgWn383Ci6xEfd1xjOxfB9w146f7gS8vRXpS-d9mImkqlXE0Q5OMpTbsEhaZ9IFn-8P2NZN1aTR0fPX94-xPK5B8GtiJNNPDaLjqYz375YKdc5H6aycvv-vl2EFS9pSD3nnRTbP1eAC49mXDMFRYp6joq2UBIJOpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=nFABqAYLiyIb5JCgxzE6OXFUnMGeZHMGGU_6e_3tuLMj9l2NabG8qE2G97qx6Q3oICgvlqp_FhrQqgtUJD6NOeJqb3tGiIz3I0nnRMT-uI4pAxv5eyxh0Y0sfbhrncYdscwUfH7D3QO84mqry_-37Nf3xdYs31nuyTxbKQgTq-MstXzvLYdr5z4olOtkKVC6anzI_YWFA-1mauGlgbmD6imJPAp7gzUHp3H4yvQCZCJNkFC_IsQ0RS3q9lDpWQ9b60HbgHXw4LGFjLubIkdfnv9k5sOQQ62VM1iBHbsIs_tb9XzkCkFra1eejIaogunK0LyzoiPFMTrBVm2gbWIPr6zbhcJ5Nvbl6rPjBVNT2-L2CDVhhLSGU6EbAgBaypm5w_C_olUmNhtpLMBv2sWG96bKN2xqSShNghb4UrTGiijN6MCm7kqn9jGF7zSIzEdp9Va8TPIF7TBDbztWposb6X1jCwnfP1IXhhpPrlXB3RcIxmGID7Q3n82JweA-wb-pKL3lPejNian4bCH84tOlCJ7PNsBsj1l1v3YzfrEUbSkirntDB_RFZqLipEH_c9ot9fh_Azi1TWbFKVcljvReEIkDPzWE4lckcMoIyRJpMOvv9JpmY9Mr4mjfK4Qx4DliBIfCtL-Mlcop5Tc6AjPHouvcYTkAcVvaPAJ_M4uQ-L8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=nFABqAYLiyIb5JCgxzE6OXFUnMGeZHMGGU_6e_3tuLMj9l2NabG8qE2G97qx6Q3oICgvlqp_FhrQqgtUJD6NOeJqb3tGiIz3I0nnRMT-uI4pAxv5eyxh0Y0sfbhrncYdscwUfH7D3QO84mqry_-37Nf3xdYs31nuyTxbKQgTq-MstXzvLYdr5z4olOtkKVC6anzI_YWFA-1mauGlgbmD6imJPAp7gzUHp3H4yvQCZCJNkFC_IsQ0RS3q9lDpWQ9b60HbgHXw4LGFjLubIkdfnv9k5sOQQ62VM1iBHbsIs_tb9XzkCkFra1eejIaogunK0LyzoiPFMTrBVm2gbWIPr6zbhcJ5Nvbl6rPjBVNT2-L2CDVhhLSGU6EbAgBaypm5w_C_olUmNhtpLMBv2sWG96bKN2xqSShNghb4UrTGiijN6MCm7kqn9jGF7zSIzEdp9Va8TPIF7TBDbztWposb6X1jCwnfP1IXhhpPrlXB3RcIxmGID7Q3n82JweA-wb-pKL3lPejNian4bCH84tOlCJ7PNsBsj1l1v3YzfrEUbSkirntDB_RFZqLipEH_c9ot9fh_Azi1TWbFKVcljvReEIkDPzWE4lckcMoIyRJpMOvv9JpmY9Mr4mjfK4Qx4DliBIfCtL-Mlcop5Tc6AjPHouvcYTkAcVvaPAJ_M4uQ-L8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=j3OZovlrpOM9Y_EBJEaq78lB7FKnEW0TTO2nMPumHiNGaCZSyznSXdCNMEO-Epyp_CMOHbw8C57FosyWYjZsnU6wQUWgW6IX3jtWvTee-D709uPcr6qsRhhVcSWakZrAWAZtjtUOxPrIdIjml009a_dK1w9TVqMgcDlGnUKZ6V4GTXFe3rZM5TEvdw4ZgjHRzxubmvATSL0SaabTPPI00O7PHPGp7vPzFQsHhSnVLXgAYykMJRxgTrEcJl89s839Sm_kqmvL8RtKlvYtW4flA7DGZLfhNxJrRZJoylLLMatbln9d9Z29T6aHjRWQ0gqgcc6oJQwyigJoIbDOfCsV03CEjCRWKe8MkFOnhITqVP3CacpX4PDfBK0zYmOYx0fivEHgZMUwSqwVESDkWcDjcCDTTnS0tLptdOqfiMTt78a4wAooO3JSXWwK9BtGikU444QOJ6z9mQwGZO_jQONWdIZRHshgu_BIZqmWdepCA-MlTWtOtUCOEPwqCOIpuVNUXguBJIKPae8941iaOQqAgIDnw6NjhWwskOGjI33BNzFxCljK-80ydcRfKWBndXt_DWRpkA8Lf4UCw3wzbPbpZd3o1QtvTQ0DMhnrde1dxl9GNhUI3qO03_pkL-dph7k0DFWnthjS30UcDHjSX69TihluNbsaKZ_aNFsLsPU_i_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=j3OZovlrpOM9Y_EBJEaq78lB7FKnEW0TTO2nMPumHiNGaCZSyznSXdCNMEO-Epyp_CMOHbw8C57FosyWYjZsnU6wQUWgW6IX3jtWvTee-D709uPcr6qsRhhVcSWakZrAWAZtjtUOxPrIdIjml009a_dK1w9TVqMgcDlGnUKZ6V4GTXFe3rZM5TEvdw4ZgjHRzxubmvATSL0SaabTPPI00O7PHPGp7vPzFQsHhSnVLXgAYykMJRxgTrEcJl89s839Sm_kqmvL8RtKlvYtW4flA7DGZLfhNxJrRZJoylLLMatbln9d9Z29T6aHjRWQ0gqgcc6oJQwyigJoIbDOfCsV03CEjCRWKe8MkFOnhITqVP3CacpX4PDfBK0zYmOYx0fivEHgZMUwSqwVESDkWcDjcCDTTnS0tLptdOqfiMTt78a4wAooO3JSXWwK9BtGikU444QOJ6z9mQwGZO_jQONWdIZRHshgu_BIZqmWdepCA-MlTWtOtUCOEPwqCOIpuVNUXguBJIKPae8941iaOQqAgIDnw6NjhWwskOGjI33BNzFxCljK-80ydcRfKWBndXt_DWRpkA8Lf4UCw3wzbPbpZd3o1QtvTQ0DMhnrde1dxl9GNhUI3qO03_pkL-dph7k0DFWnthjS30UcDHjSX69TihluNbsaKZ_aNFsLsPU_i_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
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
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVSqhy3-G_d6_2RkFr0zZklQ-k7FovHSgDE7l6n7AyLTcW7ZzBqSrKVz84unSSv5FpfRyLgyPKX9B2XY6Gffcu-MweFtYnyn8kHFTVrKODCMyU5R7gWX5LpCOnfikMW6fL1tf36QPvoxXHjqKy-26aRf9NaGjhT_52pR88fR6i73Wq5GQtkYcSyrnR4EG4_DTmRliB1OAZ6f1xlMeCei88ATkdRxYG6dOJID8kx4jvBTDnpyenM45-ImdcaeTwJ-ceu_I4dbv4qRf1JnSCEsiXAQqea2igafF55HIG7FY8qLiC-ejSTHCvUx-TzymFdbjNHg-lyBIxgxDoVKZqhBDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=v_-rOj79AP73g2SPMCrWlFRR2YX8XsZhH8kpcmn8zhZm-wXOaOWAkoAXveWlr9bw1Ic02qgWQIKfg-yLxlR5Tn99d_dDhWcx0oD4DPawvqNCNUkKBAYV0H8-ok5CP-gYVacdh8T2HbyLw9yOxtquev3641IKsm1fCihtbbzm-Gy3zCY1nwNZmXFVefZt7069NCerv2mgSCZBNZzbAUYvkp48JwHr7WY-7WtUgJYwAWyyMXIbJvy_t3C6TK3TuRxl6W61Y3dpNBJoTxLNUwlGwGY-8YqE9bZiuG3Jv8hlN61zeOcirwGGVW0kBVte6IQslOFnGmY1TVQCYv15ivs2yh0MHsTPGI1KC5Z9VBPC9Us7XnUnZgTn4U2UPfruWK-AgGDm555h7668gT4YqxRQ9hbdqBh_Mxx4pg0Qgarplrb37tv-rFc5RxhAlMtxErjKpeFrzPHoun5rVuinP_HlvF4rErngsz9kqOQ_aAVOx5EZWTtkHcu0F9kCYUNc4wXX-13MU2PyRHt4nAknx7FzJTbdn4u_58w3_MyVq8Jpr8MjHfiggBx7KG78L3Zsdtey1z_ToS4fWx2iZR7RJrqVG5hBgoS8HuY3sU06CTwMjK6RPEg07V8o3GXSNx3VYU7dA71Cgoksnapd15DNN8WUv_dI2WPHZy-lCfhBYyJEado" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=v_-rOj79AP73g2SPMCrWlFRR2YX8XsZhH8kpcmn8zhZm-wXOaOWAkoAXveWlr9bw1Ic02qgWQIKfg-yLxlR5Tn99d_dDhWcx0oD4DPawvqNCNUkKBAYV0H8-ok5CP-gYVacdh8T2HbyLw9yOxtquev3641IKsm1fCihtbbzm-Gy3zCY1nwNZmXFVefZt7069NCerv2mgSCZBNZzbAUYvkp48JwHr7WY-7WtUgJYwAWyyMXIbJvy_t3C6TK3TuRxl6W61Y3dpNBJoTxLNUwlGwGY-8YqE9bZiuG3Jv8hlN61zeOcirwGGVW0kBVte6IQslOFnGmY1TVQCYv15ivs2yh0MHsTPGI1KC5Z9VBPC9Us7XnUnZgTn4U2UPfruWK-AgGDm555h7668gT4YqxRQ9hbdqBh_Mxx4pg0Qgarplrb37tv-rFc5RxhAlMtxErjKpeFrzPHoun5rVuinP_HlvF4rErngsz9kqOQ_aAVOx5EZWTtkHcu0F9kCYUNc4wXX-13MU2PyRHt4nAknx7FzJTbdn4u_58w3_MyVq8Jpr8MjHfiggBx7KG78L3Zsdtey1z_ToS4fWx2iZR7RJrqVG5hBgoS8HuY3sU06CTwMjK6RPEg07V8o3GXSNx3VYU7dA71Cgoksnapd15DNN8WUv_dI2WPHZy-lCfhBYyJEado" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzGuMROVr7Fb9LmBFKY0goyw-z1PJQjlutB94en0uW4gEZGvyt-36SHuJow9zf3cvpJcuQQnwFsO_epGEyhc1CIRZi5GO89n1ZpKMNe2EXW4OzDTeL26JSElgQeGadX1siHTitfofzJD0qcIjWCoxmaU3OENWPJAw5_Bc_zqtoYlhcTwundmaKchbRlkCAuV_9q6zWMRFYTtljyM2MGPtBbop7GM8xs7mfVD37-64KBGKndpbQ9YCHFYHuI4nmdbeSr1aVEBmnh2pMhS386k0MCQ3nle4NFan91B0LIDHRyJBo3bw074aOnomIrpMR8pjU4V0eyZfIKvatYrakERCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwXM9H646iodpipU8VT_OmL33I0H5rfMKsTkOPPtUr9Pn2FoPXGEbCHlkRTziXzEbWqB8apDDRbIkZPKwBaD5L7iHv3KQmpv__I6PJA_aZd8ThbKiLGW1CsbVUSEJdacgJSkLC11cuh8HV59nverQelX5-67gsLPTCeYS7fjRLiDtDxEMKYDWObcCzoL0P8gFLXaKKJLlo_8qn1ZNiwFJHwq_uC6cDi2uPryEjxZIBf9V3GnnJreV_887D24QYmqnvrzr9KTueMYUFJW77pquQR4HOWmfsnjDHchHHduWXNuSIsiXL2vfe0uVmd6vdiXjKJdBnlEcwf-4rE7YpI_NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=pT37yZ1Y0_zZ0hHdHtPwXWSidfLFJxJEVhQT0ateV0ln9rZsyO7Yw-gXXxbvpdBfbjeVc3_ybqKGBN6uAqbKnwWTJrHC_A-lSrxYMC0WrIwtk8BoxofbIlxrrovY-dPkgpJY5ODLCV2lTYJmsU_xK_fOIZhWP4uw6WvYBOU2SE01M9JHYBm5z3Z5CRkRsHf7WFDcr3GyTVlb_1TzZz35dml_DBoU9dbtFwSOAbDKoH-JbuCRIpq2WcNMTEq_cIzyag6Szdye2qIFg418NZ5-Ea6B-b1APSASNyphaDpULjDK6eXef3oc_gGQANVgRQqKmwIVecsHt1dD5CtV8_FdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=pT37yZ1Y0_zZ0hHdHtPwXWSidfLFJxJEVhQT0ateV0ln9rZsyO7Yw-gXXxbvpdBfbjeVc3_ybqKGBN6uAqbKnwWTJrHC_A-lSrxYMC0WrIwtk8BoxofbIlxrrovY-dPkgpJY5ODLCV2lTYJmsU_xK_fOIZhWP4uw6WvYBOU2SE01M9JHYBm5z3Z5CRkRsHf7WFDcr3GyTVlb_1TzZz35dml_DBoU9dbtFwSOAbDKoH-JbuCRIpq2WcNMTEq_cIzyag6Szdye2qIFg418NZ5-Ea6B-b1APSASNyphaDpULjDK6eXef3oc_gGQANVgRQqKmwIVecsHt1dD5CtV8_FdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if5wmIL-m3qzdaPWX4I9Mb5kxop_SWmsVqPHgeQNj9TwyJowqSUfN1goavmssSc0rHA4mpFCjguXmFs5OZUsqek0K8eMyCFCeYnRJ6ExWNU4SI6ehG1XgTOuNOI68eSk-Ah1H_IZ5FU-ApcIvXj47W0CD_9M81kanU-2XrQCIyvti4xOujYf7LXtSlJAT_P-SUo5SjLA4PHtSHXNsNtQN7iTN1cZ_L3-ZmG0CF7qsKqXBALx_BSjWVEPbaIUgGHlbcCP4a3EyIVPm_RyRl9ERVDQQzBVWVqg6BwslnLIHNjBzOnG1jCS9A_Gdacf2BDVrfd31Xg30JGz1VcSaEKM7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl78GRYq8XxhdfwPgTAzbaZJ_MJfjafzAPl1puS2hv5R6xJeT-uL1ewWORAWynrwmg0Q5qK7ngDQWFfx92Emnqt4KCbm8L8-tW0ow4fUM8JnV_ixxUpssopfWEw5Qg3qloUcBOc-7PJVrOEo_Wsv2bENew4kk5oKfqGWFWU_P-xYaL5Bx0pLArkdC-0kHa-3zDUZmI0MFGPQZhPc4RYJNlsAZJxNllmZmmB7aOxC-qXl9xtmMYXqY5bGSAViQVt590D5tBFFcz1JvzERtUdQi_neGvFklovM8GYeTNmpzzIfK6wDiyzgkG6qvHvWr75SAWUoa10vxyd_gTzOE76PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=QUnzuX0zwMsjOSVfY0mh_gRdThN5dxUvr9m6xdX3m2a2MdX8am-YGXPLrzZ5PLSDd6hHEZ0OggnjAOV6r3AspjB7NFjwqRj2eE1wMspiVSaTYwwYvplUHkb3LRu9JIZDWWW4CSBQIqSpkaUzqxgpVayynd3F2lg2VbsxmRksBfMea0Y9LUqLo5TZ-YACghIudG8NfHSfJ6LeE10Gt2tB1y1OLRSDsufivmQalsVq6xWYp5bv2bPYM8YyjKVFjfQzLP-0n_OhJ404u9vBUy2d4zy-4mOq0YISrpV3X7e5PiWpZukickQt0hOyxMc6wPwIgWDy3mhwL6VdB-XBOtRwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=QUnzuX0zwMsjOSVfY0mh_gRdThN5dxUvr9m6xdX3m2a2MdX8am-YGXPLrzZ5PLSDd6hHEZ0OggnjAOV6r3AspjB7NFjwqRj2eE1wMspiVSaTYwwYvplUHkb3LRu9JIZDWWW4CSBQIqSpkaUzqxgpVayynd3F2lg2VbsxmRksBfMea0Y9LUqLo5TZ-YACghIudG8NfHSfJ6LeE10Gt2tB1y1OLRSDsufivmQalsVq6xWYp5bv2bPYM8YyjKVFjfQzLP-0n_OhJ404u9vBUy2d4zy-4mOq0YISrpV3X7e5PiWpZukickQt0hOyxMc6wPwIgWDy3mhwL6VdB-XBOtRwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=WGOZLEuANLYBsPj6XWtLszYTWgQHXVHm4v7yABvqwYmAqaglOyvP7VUPS_xfAnoPnSCHkLZyncZce_eEcV5--PzX0BgjQhFqJirN2BEtCQemTwcp03Qvaq877gsHOm2r8N34Z16LhTqyFzoub73cbE2cuCWMGfABlnASYNZgPsaj9RUsmeixYnPGHW0QahEjlBjo02PQGhs9M5iTxbIj1MXNfdLpfFvJaw2pY8RpkueWOS1ncukA0dCCVl1NM2mgWDkb8dlv1tKgOqLOZlhtyxY4pzPGSQSdIyCyORbp8P7Va-z78ISx-dYVY_XY5Wv6MGnTobT2iKEAySR9WoD_CK3kW45x7AJLASUXM5-anAZGyPbxwF9iiYScL0Cj5cV7CQz40fT4nMhSeQqpS5VQdiIKs7TDZGi14LP0Tk6MdT8nB6n7ABNx0fLglI406ZUWOfPTxHMzERgms_9o-xa8YUL5H0v8gf7Z-W3G8I_6ya-WC2H2BYiFl8kNTpcHYMlXWlCh0WKRaOaAlozsOZD3ZgTTaxRtObiAAnwxhd3k8HawLyX1hnYZqKB9d-UnF81e1nFF5KQwoNAG-uE3GI9NrQMqaAZ2a87WTIdt0fDZJlFhA0DllJZ4-Use9JgQVbeGAzKNMU4TgrZ1JrHgjB5suSXtwQ8QP2XuwGzIlEgsSp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=WGOZLEuANLYBsPj6XWtLszYTWgQHXVHm4v7yABvqwYmAqaglOyvP7VUPS_xfAnoPnSCHkLZyncZce_eEcV5--PzX0BgjQhFqJirN2BEtCQemTwcp03Qvaq877gsHOm2r8N34Z16LhTqyFzoub73cbE2cuCWMGfABlnASYNZgPsaj9RUsmeixYnPGHW0QahEjlBjo02PQGhs9M5iTxbIj1MXNfdLpfFvJaw2pY8RpkueWOS1ncukA0dCCVl1NM2mgWDkb8dlv1tKgOqLOZlhtyxY4pzPGSQSdIyCyORbp8P7Va-z78ISx-dYVY_XY5Wv6MGnTobT2iKEAySR9WoD_CK3kW45x7AJLASUXM5-anAZGyPbxwF9iiYScL0Cj5cV7CQz40fT4nMhSeQqpS5VQdiIKs7TDZGi14LP0Tk6MdT8nB6n7ABNx0fLglI406ZUWOfPTxHMzERgms_9o-xa8YUL5H0v8gf7Z-W3G8I_6ya-WC2H2BYiFl8kNTpcHYMlXWlCh0WKRaOaAlozsOZD3ZgTTaxRtObiAAnwxhd3k8HawLyX1hnYZqKB9d-UnF81e1nFF5KQwoNAG-uE3GI9NrQMqaAZ2a87WTIdt0fDZJlFhA0DllJZ4-Use9JgQVbeGAzKNMU4TgrZ1JrHgjB5suSXtwQ8QP2XuwGzIlEgsSp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNvshtISO_2eANwl2f5R7ROeOjQkgTWn2eD2oWem24zUyqmz7e89z_vZBqZo7xgJwPl0yeiqPN8n999w82B2DhsCSVjp_Rzr5irxb_NF8iFaupyB8_SC0TmexNk3OvUkTNdl3HI0u9B_sOmwOeXTV1tAU3yYH8a8uIFmgPce6bEI5jwySdW0Ao-6HSIY67toQuXvlGErmWGGFhJhnRhMwvbGeDoGk-7hw0AK-GaEnxiIw5vuG126YXQEmx6uxi2QAplxOaYsILWjjwaIBozXMhJ0IUwUkVbUx95Zzm3qrc0AN3gIFXhK1B9-Zb1keVwXQochsDaD_8y4A_yOQSPZUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErObYvlXKmNzDLnjrl720MO7GvgmNtdplsbnl8pcLOHUxk1glSSmLLImPRShXwK7EqYZBXwtmVXgf2povuPnNXTIXkiamvlaWUWQtSe1YcOkR5y0nJg-E_lpaq3Y5kt75F9owtLTa4cdVIafpKZfnSMwZxhmdlzFlTR9PdRJR-089XdilftdBibp087Taya_xKc32mSNndSrIKZnnr39-tAZIpEkHpwKtdtIXPm06y9aeBvevqct90CzbbHcFxFtgaAh9YJrxdwA1RU_Xt-SyIG0XMh9rLdKnxpAczb6zqGN2yGRrSPhcWsUOaNiC0QQmXQ03SVC6JppwUShYuyb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tf2A4RaFa5_x7Z9sPxAX69sQkFdaQCvM4DD8AvGUQFy8CfC8OsH-cc-nUqIUuoKD-8fpxomOjUroRd7cS_N4Dz2B2aBwpsIV-m8KY-k99uUSK6EvQxpz-jYDRwkX_6RQc-rYbM2nzaC2X9aTwBzqlt14oQVbNXtTBrdW7-HLrkVCx3s-MkVuhIZznpgduk4TFmCGlxXnqACRWelaA4qXX1HvVxFKm9ICQtnyXmNWw29PSFdcnqlAu0niR1wZnCXy-a737kR8lN2BZAoYq6fVoXJ1LFcWLn7YOHWR3sLF_nmsMjqC0L2pAmGbnoYG5UhrXAcHf1Xk0r0tiXeiRyxkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=SzK_g1pgPvqffj1zkJK4IuRLhEb1NJOzaFbTNQacuUsJmb_3je7cFkdgFX3TvPfeE0tLNaUx8vbiEYGbvlDexpftgtyb-iuszoEHM_PR02THhelByGkIFxnJaWgDvjP6nJqHQDkVIGTLByPjhOwTI7Q-KFfNapn9xrvmYaBbSj-Jm-a14iHGV5v5xAk6zNEydWxuX7rqKkdLZIMgwcnBuwarn5cgTLTRICYNQpIAD6psWHh7J95Hssk-oOiWgfPDu2E5pH-5YJJxkbxLpC5Uz6UwcKLNvcVHGib4xJrp4uMIQNifYvnxceOm3aLzct8WZ8br9Z1Z13RSDvxo97r7cKFFTg2GV4RS5VlBA1KMkBhS-HfXpWcegtNRQ7cwYqZjSufWt6D-Fz6VcDbEk_zR3a1X3x1CXhD0SQ5WB1HpGkdJyn9FeyqXqI47SSJ9CKIUyTie3ETDlb3LilNhb0t-qYvtvjFNBuqr4ba5wd4sI_cufYSe_AwGkiLar1F36tUKNAzlTNKSvtKXds-NsK98TFyh1RThlMw6-8giIkAJL9vWD1NOSKGQO7UsL2Qz8ghtN4SouIcbYTYkPKzT5UzAlmiEgCFhrAH2gquIL5-ngZHDi1AxZqBYNv9zpZx8FTMHhvMlaAPEuM78uhjKbdEVx0ncIr8u9qJzqo2H6tKNX-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=SzK_g1pgPvqffj1zkJK4IuRLhEb1NJOzaFbTNQacuUsJmb_3je7cFkdgFX3TvPfeE0tLNaUx8vbiEYGbvlDexpftgtyb-iuszoEHM_PR02THhelByGkIFxnJaWgDvjP6nJqHQDkVIGTLByPjhOwTI7Q-KFfNapn9xrvmYaBbSj-Jm-a14iHGV5v5xAk6zNEydWxuX7rqKkdLZIMgwcnBuwarn5cgTLTRICYNQpIAD6psWHh7J95Hssk-oOiWgfPDu2E5pH-5YJJxkbxLpC5Uz6UwcKLNvcVHGib4xJrp4uMIQNifYvnxceOm3aLzct8WZ8br9Z1Z13RSDvxo97r7cKFFTg2GV4RS5VlBA1KMkBhS-HfXpWcegtNRQ7cwYqZjSufWt6D-Fz6VcDbEk_zR3a1X3x1CXhD0SQ5WB1HpGkdJyn9FeyqXqI47SSJ9CKIUyTie3ETDlb3LilNhb0t-qYvtvjFNBuqr4ba5wd4sI_cufYSe_AwGkiLar1F36tUKNAzlTNKSvtKXds-NsK98TFyh1RThlMw6-8giIkAJL9vWD1NOSKGQO7UsL2Qz8ghtN4SouIcbYTYkPKzT5UzAlmiEgCFhrAH2gquIL5-ngZHDi1AxZqBYNv9zpZx8FTMHhvMlaAPEuM78uhjKbdEVx0ncIr8u9qJzqo2H6tKNX-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBmEulJmStlni2qno8mbRICHscj4WofrZpayElM34cYfM0FMopo1YCmsp3FvmAe5mD_F9RpmrJFIh4LjoCb-K6H4YeG-GDn7SxACmMLf2a-keJ5rT8CHEiozkHyXtxSijcqtEE30VaHOkJjyMcYv1c8Tn731NLTXOp3yb8RUWq5G1Tz_OXBeiQ65jgo3fb4nhfhaiLfKLqdsW7IAj-hHy9djzA0QAjsZKpUtf6NJrbbLcUhATfNXA6zYRIOG9e9j158I3c4_vL6dky0HDFOEzZJGaS3jFyHR_nIz0DPI_jWNHzIyTGP1fS4_JPLQF34P53Q-e9eaOGRb8IBPtkZPxT2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBmEulJmStlni2qno8mbRICHscj4WofrZpayElM34cYfM0FMopo1YCmsp3FvmAe5mD_F9RpmrJFIh4LjoCb-K6H4YeG-GDn7SxACmMLf2a-keJ5rT8CHEiozkHyXtxSijcqtEE30VaHOkJjyMcYv1c8Tn731NLTXOp3yb8RUWq5G1Tz_OXBeiQ65jgo3fb4nhfhaiLfKLqdsW7IAj-hHy9djzA0QAjsZKpUtf6NJrbbLcUhATfNXA6zYRIOG9e9j158I3c4_vL6dky0HDFOEzZJGaS3jFyHR_nIz0DPI_jWNHzIyTGP1fS4_JPLQF34P53Q-e9eaOGRb8IBPtkZPxT2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mPhckecWhOFroQjJ2madTpeT7kphPYIEREz6c6eiL_pUvDasIWCvHEQlMCGsb4_j1PlAwaX3OmnEiKr86VO7KVsqYDcsfGGCymquNE6PoQx_zoMaIK4AYeAn8mmP94BwbYHJZ6J3PlF2kXSgpZ1RiNqvmX1W8zX-GxuL9EHyrnkO1qtq8Adc87cmX-EXCAkbarFU4fhvPWCdjePB-cEMkeT3x4TKzCebBKW8eaUFI3HfpPg7ZKQN3yktgIvhxqRcNY9WAjCbyuolkc2pPRD4uLfHLuzi-Pj7kmtVjJqzm9611ZtriISVk3pkTQJSWCPGyQ-LCKJGJvW2o5eUf7UT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
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
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knGdd168fgBUMDETZQcj0nBnQILqa6DTfWnXaTulGWxK-MzIHC3zsxZMrzXT-bShEOc6TdDCRRDXPnFZb7ca2WiiticjNtJ2q8aZjY5lXpvMZ1jI-phTXtnmsuBLv7I0Qi32896Hg47IVArF9ro7SfKqIqHEg0ZbyYfQVypBb4V4aFAi3Ek0qRtNa9LvC3_LPAohXQSFEC8jry3jZCW2zhgVXpNboZswf4DxfGsuYORLBwJk9QSaNszkeg2u_kK05S44W087tm15DI-sKS0VdjeTGpfJrbDbJxXyWuxTfKMIpA4G4wdiUpdnhvnXdVCXp4rKQNIuyuLHpYOf2hUfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=Kn2-0U3qXN7ImDE0LnWsTviHEnJ55mdRSXW9RChwf9eyp9ESmCstU3CIRIdc_Quzc5bG78RT1I5r5DxHF7P3LebNguLkZxgCHqAYlj9kkxFfr8e5GgwwNf1PYrWjJ0V0_labbnzlWIE8PTLDjtlaBPnBapC6xiyawsGb_r5GA9mr_7CP61RpI5ZHloYMHysq78HotR_LHT9tgqLATOJ9jh9Nk7Ppuy18wQVNTI7X4K8AdtsRGoUQfvDxc4kkzZvUmSqqB4LSGAJssnEJmFfBv81cVMePiDOjSK3qBIjdVrRtlBEFib1JF7LQZw4ZagAfobBuzD1_CFb0xhJ7DqZYQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=Kn2-0U3qXN7ImDE0LnWsTviHEnJ55mdRSXW9RChwf9eyp9ESmCstU3CIRIdc_Quzc5bG78RT1I5r5DxHF7P3LebNguLkZxgCHqAYlj9kkxFfr8e5GgwwNf1PYrWjJ0V0_labbnzlWIE8PTLDjtlaBPnBapC6xiyawsGb_r5GA9mr_7CP61RpI5ZHloYMHysq78HotR_LHT9tgqLATOJ9jh9Nk7Ppuy18wQVNTI7X4K8AdtsRGoUQfvDxc4kkzZvUmSqqB4LSGAJssnEJmFfBv81cVMePiDOjSK3qBIjdVrRtlBEFib1JF7LQZw4ZagAfobBuzD1_CFb0xhJ7DqZYQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8ix5SbW4sbPPCAIMYS2FaufimAjaX1ie7VbBmIq9BChaJVSPq4ylbWoXjjIf5DMfc5n_iRn7YScnZ-_5P1pB5vIkg6ifunzlGElmMeYdWRUMjBD85Cw_Tz9jcp1Q3GzbP2-dDO8JCdqX1D-_Q4FPA4H7p0Tp8uWN5joKou-vNAcOBK5b0fpFNuT9oCp_M3kcNPmA4HZuhZu9lg5lncAPN2qkEAoX2z3knO17S-kj9HOkxTaO5kzYKMOHdRkjvtjUZAic3cBv7vWgJomuqtVtHkGqhhpkDQ008W7SI4ChvSk9vX7qa6hjSlr7IUAf7cCPfjunrz2Scr7q1G4YtWEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5xvhGP0ajezjFlSFnxe07lWtek304D1KMWP74nDCtYEEkFDkz9toiSJNeU2EYi9QAAm8uek8ihLw6OzfZntIFYRRQTR_zhXG9ULSkwlL9Q5u3WDz-yPqAA46VI0Rsvs-d2LvsNlxIXDENebfZ6t1LH3g3hRVBUkSNVLhP22Uznu39AxVkYLg26xB_qVkFi-knLhXFdelW3oPTQVqsPhAXHEkvLbFbyjOXSDLua9w3U90WNfNT3oa90pn5pEUv-jTdWjzcZbjDq9-iVx4DVMDOM6sWTcRhFpK9G4GcjPKaYqad4WWI3CKlqJtEcVP46i5QASkBPDAwTNfFYPLq1DiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld3dqnR-JuS08JJNWzikzKJzFtw7wq9lQVSoxspR5s0VFqo7ZuQxPKhSEHen2CGdUhKyObiK3o5shgb-nheNNqq1J5VwdR5qr2s2DI8X-JrrDXaEJ9hwUjdfCqHOzK2UA-Gal8wkJoz1vQTDHpG0x3Wde8HSDwvdCTqE_1zY-OoVyClIVgU54p4HI4-sC3ksVGYn1JQUdBcCxVKwcqgZIxgLxOij0LdZZMDTE8jS5WcI1axZzxrjfmgiNFLlYhRrrFwDV1h57bLA5ktuaqw3W7TL2clOkNdD2Q_ephE7mMqbFxWoGhYUES98NHZOLBW3BYlqiEa67N2KDBwKWSQ8bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
