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
<img src="https://cdn4.telesco.pe/file/OlQqS6egUC9pjFtoAQ2EnpqFCq1t6tnBNjo3a5VB2QLbxmFP1UiAvH2dWVsJymzJ4z00GufhgEJKLvhUCMBoXOqiRL5TYDpsN9_gzk5WCWHkBeUEVHx-AMm9lEGS-pRN9Y7g0dulTXUR_gOzsRG3FA7SbFH9DrObBtEmM7Kf4OJu2KhbMvI715MKQLmoQfY0FExakeRkYdndFuhIX6kvFuIO0mbu2k0vGiZ4h48fdnmiMbUB2XQtT6lVldZiwWyxO9sKwoq0_Wqhpy0blmNEEkQpEeqJX1qW3ayaFfxanQHD2EvneI67eRYqVyc7Es-jBmhdIR3QuvR_Z87n83-BFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.9K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 03:15:52</div>
<hr>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 196 · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 230 · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAgp-u3WftXL4-MzjU7BupEV3oOewG7a8sqbcx43cS7pNDsn6KPliqAULPHg9iF70PgLNy1ldAW9KWQrM16lYYoGhj2Qh7kApdruKkFCb7wZvT95bmrD7SavLOj5GGe1Y11Q2ZTeI18FDn2thhDv782HY9i1giOUh6YoemVbOLz-s9sr4qPRs1BtDcZJTni8rCGMv1xJ51VlMbJqRldoysSONjcLfhyjM915_r2Goib9xg79CIuhgaSFsVd11-8nIPW_wxuQMIdrfoWlwYPGvLTDdWFqfbA2JNXRCbhjOKr86Pj69N_Vufvedx49esXLmuYDnRl0cDLsHQoBymTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C304P-nsLVKM-von7U7xm02ayAZlLbRbtcXFehuWmxWlgEPDdY3vLhJicDzD-L495UnaTs_MQVA6BgpHsda3IRGYBg_1sU2m29Zq5DGMUHY6sUG3O02byYU33ujsyF7_E6ydXWXoRxsNlcizfVjxe_zy1OgarT8JIAZxSsUXQuqG7FD-meZ4DcZqdc4glr9ytthkCju_CVUgRQkBJNO9KkiD0X11NdjiTGz8g9ErGJkyDt6h8-sJyNbwb7x18lLdkQtzyMQePdACv6z47ULiuV416LluFekWW-GwfoL0VR61EP3A4yUgtQ0GwZUZm9sVUbGIay3WHeMd59vOkLV_Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmNKYmMxYUjJSckXmkvwH49mnEjlDEAipjWiXR5K3E4-_LOxELmh137JPKLxDl8aYmaIAVJp6FaOUU1KyDxkYy1JKJ2uxbINYLNOJ7Oz9XrrmFjQv_kaM5HEkXgU3ycc5_-uGBP0iA7YaXEMyr0Uc1sgjiiqPts753IL7o-Lc5CNlyse0fxPf3y46-z5KGT6LOTf9tZAqwjyNt4EsMZP01HBLQ-vX8-spi0aPDOvyk09TMmpXrXM9z5UsIZ2i0kwpP3oa1tPj88gPuyOB6EFvQtWzZFRS6zPVvxHrTmt9vc6QecW8o5rmz_EvhRjTVqVsRiLJJgbl2taez3tDn4kOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRYY1bScxOHbS-DdRzZhImzEFnK3NcLI5r5Dpa7ElFhkRKOtlpx1O6xE2RlFzKQif2NsaEEmg8pcEVfVEXUWjAShE5ipDUp3gFODL3AcpwH6fDRQNTfAToiXsZkxXq1QgSENPj6FfN11Rxm36cURHA3yWC0FHvXy8HUfDYSiCIcoceBZt-KImcV3ZCYXHVPsCaW1wQDOc9T0oAEjAS1XCN0MuxfzDQekjQi57BtIoa_-heJjugBufvtzLe5w5dGQUoxkvECwdCgSAqmduM0isZeuVOE9i1jEjMEk0TsGGC-QGjjUEMCJTKQeJSoMjXj8Aw90h46Em0hTntO_D3yiiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=lFXomHdOn6MmXzNHOe0XI8FSPwAjm6tE84YSb_LYlJEd4bWc6fdOXvMlLbjV6khSUzgEY-SOWNlIU5ugE5GWGUhbgBeakAhuFzsQ2UlzIxc3XWCAvuT4P7i8eLmZG0BDzdQ_nNjTPSlClX1Ol6ZEf1Uj_DddQh1r5Km5nKBWtAieAzNpJFeF2uFO4jyH_7njLEi9N3iTxuPZtPQ22dzspzbfN2PVmduVA1G5vS09RVFMXh5TFvTz8DKjllYrSUvXKWESnaQx7IQWnI0ti944N80eSPmw1O8i5NbO8_3QmZtzR6YGOwN12YCHLJvWbkNIkjQ8m-jv1tdrjJTi3QVJZTz_KuxPQ0xufWmPiSzhbhsBnRSd0254B1agydm0aPfPRmP1m0RReGcqNnrCHo4z-i2TqgULXt3h406curP5ElHPUqBCRsf55pA6aR1LR-pZWgwWse7YoVsF22lcfFedVDVnFrk2tfoFpv51TUvIui_jCk4c6GFXSnDZBNeTevpReIimmLLzlTR45PUGnLV6Hun_MqNPoHPOLoiQGlrvh4-akfU44y4YDMvH8bHp-wNcCE5fZXTEBk1kiuSV2R4CNnMVTV9UiRRkSNSWGv20e1X51OsWs-SDXBAole4zMu9ISEUCq3Tk_4vhNq8zcGHUNvDmSPUwWtXCV1sONLtr15k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=lFXomHdOn6MmXzNHOe0XI8FSPwAjm6tE84YSb_LYlJEd4bWc6fdOXvMlLbjV6khSUzgEY-SOWNlIU5ugE5GWGUhbgBeakAhuFzsQ2UlzIxc3XWCAvuT4P7i8eLmZG0BDzdQ_nNjTPSlClX1Ol6ZEf1Uj_DddQh1r5Km5nKBWtAieAzNpJFeF2uFO4jyH_7njLEi9N3iTxuPZtPQ22dzspzbfN2PVmduVA1G5vS09RVFMXh5TFvTz8DKjllYrSUvXKWESnaQx7IQWnI0ti944N80eSPmw1O8i5NbO8_3QmZtzR6YGOwN12YCHLJvWbkNIkjQ8m-jv1tdrjJTi3QVJZTz_KuxPQ0xufWmPiSzhbhsBnRSd0254B1agydm0aPfPRmP1m0RReGcqNnrCHo4z-i2TqgULXt3h406curP5ElHPUqBCRsf55pA6aR1LR-pZWgwWse7YoVsF22lcfFedVDVnFrk2tfoFpv51TUvIui_jCk4c6GFXSnDZBNeTevpReIimmLLzlTR45PUGnLV6Hun_MqNPoHPOLoiQGlrvh4-akfU44y4YDMvH8bHp-wNcCE5fZXTEBk1kiuSV2R4CNnMVTV9UiRRkSNSWGv20e1X51OsWs-SDXBAole4zMu9ISEUCq3Tk_4vhNq8zcGHUNvDmSPUwWtXCV1sONLtr15k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=cuUGSOKeJvDEOdzQxfEVsV9u9x_TSnFCUxw6fns6I4VpPymwEWAjw2wcmCou4GE9ZwliBIFXDyhMn9ovslGay20iNtjMNFzHh9oMAc2SBJ3YAY03pfV_pRTHRENd4H8M8Q2sC0LtS8IKS6ivnED7Vo12O3HxuJE_B88Fvs04QSDN6xVYS5Im6opY-77Ci8fErjvXK1j-QhOQJbBqIE1G6nAgy8KaewC0mBsT1UcsYBrgTqshgSfmHfXRdW5QxaBXCfHwxAKMDxuI9sxfC6EP1kmGWxNZ-m8ebELUh3Sbha2pDDbWs5RiYbfuAl9-WW740ybuy2MlHOu8OsdL7HcvHUESNknQTUWsTTXxs63q7Sa9ZU_vTEDtg8NMhJXgu9DPtd5JImbt9nz1abQ8Pa2UQTEci1hmcLjkzfZbZL9jUQtVQBEToiWDsvc-eLDpeP-vtyTHZlJfRg_ZPbz-VedcDJMKYDjR-5fdEFZylh2y5vjoNIzb8WS_APM_Cdp8S9Gn5wO4R3TEX4iDTbp3RUalt-QlWDndtuPho6rlQ7CfzMd-9GCLYx1Wfns3kJRfflyOJpEq83oGkwa3hdxTAV2-XtahcEhw3t2jxsm47xsYECuKxQb1BC__GbF_h4-3ukqIAJTulO5bDA9noPtk0KlYglP4ClzGKsRyt1EYMKnjaIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=cuUGSOKeJvDEOdzQxfEVsV9u9x_TSnFCUxw6fns6I4VpPymwEWAjw2wcmCou4GE9ZwliBIFXDyhMn9ovslGay20iNtjMNFzHh9oMAc2SBJ3YAY03pfV_pRTHRENd4H8M8Q2sC0LtS8IKS6ivnED7Vo12O3HxuJE_B88Fvs04QSDN6xVYS5Im6opY-77Ci8fErjvXK1j-QhOQJbBqIE1G6nAgy8KaewC0mBsT1UcsYBrgTqshgSfmHfXRdW5QxaBXCfHwxAKMDxuI9sxfC6EP1kmGWxNZ-m8ebELUh3Sbha2pDDbWs5RiYbfuAl9-WW740ybuy2MlHOu8OsdL7HcvHUESNknQTUWsTTXxs63q7Sa9ZU_vTEDtg8NMhJXgu9DPtd5JImbt9nz1abQ8Pa2UQTEci1hmcLjkzfZbZL9jUQtVQBEToiWDsvc-eLDpeP-vtyTHZlJfRg_ZPbz-VedcDJMKYDjR-5fdEFZylh2y5vjoNIzb8WS_APM_Cdp8S9Gn5wO4R3TEX4iDTbp3RUalt-QlWDndtuPho6rlQ7CfzMd-9GCLYx1Wfns3kJRfflyOJpEq83oGkwa3hdxTAV2-XtahcEhw3t2jxsm47xsYECuKxQb1BC__GbF_h4-3ukqIAJTulO5bDA9noPtk0KlYglP4ClzGKsRyt1EYMKnjaIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL6AX0cH4OzKcvK8WCdBX-cmFOdgo-bXZtz8mR45bBKTbWYUsxbYRhm_ya15twoj6xUMn2UGMWVWmAc3PDSXuwvRIrGRGPx_PyD7v0tMu5n6727rgQ-FHMROaYse-IaDZScD7z-mqQh51MUYa7EzfnGQWFPkWz9tP5yERKpyoR4Y5lP4eIipxMwGQosyhFbkdwD4cwWtK_GxkrbaovENxGm845s12UYYhHytqIfqXg0OP38e07jGKO-noRI5_51s9x0wWfV47ipA8zru2HuWWrmoSixgJVe9DOTm8HdKqc86JPuTe5eJS2jUFiSbKq61lVnmiGTiBWI6mdJX35FqoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=dw8lyZbmcPIGGCECiNeDH8VIJY2bfGZhUHykYFKrAiFJ_y3_RfQxKPWU2RfngjYWmwuWUSmXRKosJ_7KEBgD0zVrAJM0gWO0qXGXBI-TDMs0DmuIQhvqrtbvzs66MXMWbhW5Yy2oRsz-taxYZsymC6_iO9O7PkpmMi-PIiPLWqEBVcjMWFPGRtMfVpEMvHDq3Ba3-xxxWCgH3YslAIM5O0_iEAyS6emUnO6OBckfz8ixr_OkYZKtVoeFcyH7J0l5pUMVx8UlOXk7BPk_dKxVYd7ZwAj0xefLMICfYw6o9Jzchp50pL8oOldxbD3B3Ecc7WBbrIZkI_a6vV88upWsAWVaB6bIEjYKUxL_pViZRCEi50-XWpfWUmTjpxsyeR9ztlO7lF2_JJ0oufI0y7VDilGNJ-9V2TIcRK7FJZn1Sp8WZuUJvmF2Fg8wmEguqTETBqYKluyQdMHEn6kR6lQTaQCklC4br4-L5hltV1zfbDAdXsyRQWgjr83ifa51XyFS34iVLqisQ0BzW_T4breGTd1McbpJH2mt4_L78cJA_2vdsIX51yyKpTOWeJRseRakyv8n_KU53MulN6zwYisqv2GHx1i6XFWI_ZMSLUuRJjs0xpBWkyE5qPeMsaX3GCFUUWN8jORCppXYFbruitg-5ne40ftjHQPzL_-aKMisoQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=dw8lyZbmcPIGGCECiNeDH8VIJY2bfGZhUHykYFKrAiFJ_y3_RfQxKPWU2RfngjYWmwuWUSmXRKosJ_7KEBgD0zVrAJM0gWO0qXGXBI-TDMs0DmuIQhvqrtbvzs66MXMWbhW5Yy2oRsz-taxYZsymC6_iO9O7PkpmMi-PIiPLWqEBVcjMWFPGRtMfVpEMvHDq3Ba3-xxxWCgH3YslAIM5O0_iEAyS6emUnO6OBckfz8ixr_OkYZKtVoeFcyH7J0l5pUMVx8UlOXk7BPk_dKxVYd7ZwAj0xefLMICfYw6o9Jzchp50pL8oOldxbD3B3Ecc7WBbrIZkI_a6vV88upWsAWVaB6bIEjYKUxL_pViZRCEi50-XWpfWUmTjpxsyeR9ztlO7lF2_JJ0oufI0y7VDilGNJ-9V2TIcRK7FJZn1Sp8WZuUJvmF2Fg8wmEguqTETBqYKluyQdMHEn6kR6lQTaQCklC4br4-L5hltV1zfbDAdXsyRQWgjr83ifa51XyFS34iVLqisQ0BzW_T4breGTd1McbpJH2mt4_L78cJA_2vdsIX51yyKpTOWeJRseRakyv8n_KU53MulN6zwYisqv2GHx1i6XFWI_ZMSLUuRJjs0xpBWkyE5qPeMsaX3GCFUUWN8jORCppXYFbruitg-5ne40ftjHQPzL_-aKMisoQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ahq17xbV2fpjqWAoC6p2HKO4SCahIRx7AUiEP3S2lE_p70A6VAHHXZuAH92O2YJE78psFfoqZMGpwaVSgAve0aoVw4KHC5Om7_uowjCzqkBjOipi0XEIe0xgf55hq4TMkM8i2J-8-JZVFGdpy3Ux_vBv9bl8hnSodwVKb8GhborXSDJiuym90QbUD4-Yn8V0V4qFoP-fCbrMGuZvt4ayPoLqvtJe-_Xn2BQ_2uS6NZQCHsecFghPsdNEpmUvD0jW34DqFhOD-1OQ_kjy9wDzOB6Q0RzkYY32dM2HNAb9DolaKnoDtOVqc7moCkof16D7u2vhsyjJuKBRhPmL2LEOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=f_9QM0s5HFrtqAiFG2z-GSavynnrPefxgehogcqdmMaNEr-i5wVhNj1JqbvLGVyEgj-s8vZUN5EoJXdaYtkDh4ibBZAzFGe4FwL4kdxisOMKTv93x7sOkZUj2Cqo7CGUfsN2kAA09CCM7kCdmXhSjg-D8nzxPwJxtL1-TR_vuDWtojOL6C6BgsUlxbus_dnX7Ztbj_GyvnfqTv1SJJjVoKDzFsJwTLCmp9L2RkPQkVG14uNn4rR6GVgud-w89Z-5uLNTdiR4IS-g_7qfWPLE4rvL8yv88U9sB8OCptvQP_tDAtjvBUAGEK5LsUynNOww1uDstObLfHUl27WxMsTMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=f_9QM0s5HFrtqAiFG2z-GSavynnrPefxgehogcqdmMaNEr-i5wVhNj1JqbvLGVyEgj-s8vZUN5EoJXdaYtkDh4ibBZAzFGe4FwL4kdxisOMKTv93x7sOkZUj2Cqo7CGUfsN2kAA09CCM7kCdmXhSjg-D8nzxPwJxtL1-TR_vuDWtojOL6C6BgsUlxbus_dnX7Ztbj_GyvnfqTv1SJJjVoKDzFsJwTLCmp9L2RkPQkVG14uNn4rR6GVgud-w89Z-5uLNTdiR4IS-g_7qfWPLE4rvL8yv88U9sB8OCptvQP_tDAtjvBUAGEK5LsUynNOww1uDstObLfHUl27WxMsTMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFYSPOwR4V25pbkeDZhdRiVP5UHkNkC1_hYYDBnS3Nzm6n3WqtuHam1wN7GDLwbl3fgPd21HxYnZiT2mIJ0iv98dneVR5CWOpV6qtMpn3jZF3_eqIu4NVOMOfjCOox2hSWRnH_gQjs4sEyjeKf8GAkjKMrTPcIEgnoxJBcwXH0O0jsCazTEKyKTPHePpsixUj-085gMK6_ruinfdrGKES2WATtl9qqfMX6s3qxR6tXVix9t1VBNB5b-9Nx8V2SJCceFoKhxf3eM8w-9YVIpz1Xd3z1h6_wsPxwlxnGWchfS4dnqx6QdiuKZJI61rvzyPmFZYPS2HgdQGPkpzjaryWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwC9aj1BoGXZgJ4F7rMDyYMN8Zxo-7H-EYkVoB8b8qIUHqGvX6PwpzIvrgxP1_fRv_N2jKCRdjL5e4yrdCAK4-vJG99X5uCJ6hhYH0erHgZe6gYZ6FEGAd5i4Io_3jgDdCSzquH-bOkbxkAfbXGXfDCu-MxxpMNmMhCghKEmLW_3jgPNOdj-uv-AIH102a7huFcz_dfPbzFuhNxEjVOZzFxyzEEOs6n2HBBaNU-QtYnU9usdh5_aY4EDALc_gl7zuASuzZ-AKIY3a-i7m25ZUeTJ5y0CdgJGxc5TTC4iqfWgoayLObiSg7yOH8LHLrcvjaCzjQsJJtvt-o6iegi1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=W_DJCr5axOxgF1GJNOt4Vb3XL8gbUNVdCBS3h_LTV4es7UtpJjWNMONWYwfC7aTgswLySqzhol8IpZNJA2QbOhp91R6ORPK3Bv9NpLmTuIH-PVbCXGtuBc7EOveRhJ_Tu9wsy48JG9SKGFrrUGcBsKArERvpLUTyroDzEmrsZkD445Rv2CGXbUztVzkc8D2Hh0bEKjqfLM0UiH6FQrd4BseFIWy_CBIU3pVsDUAkG4yf1kdK62paS085bGz3fkoYrF3oM8X75X-Qnd5ryWF7leKO71VKBE_vCIC1rIF9oc5I2apSnzfYDHDYuh2BPX5D2B6CV2oemPurqfDZZHZLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=W_DJCr5axOxgF1GJNOt4Vb3XL8gbUNVdCBS3h_LTV4es7UtpJjWNMONWYwfC7aTgswLySqzhol8IpZNJA2QbOhp91R6ORPK3Bv9NpLmTuIH-PVbCXGtuBc7EOveRhJ_Tu9wsy48JG9SKGFrrUGcBsKArERvpLUTyroDzEmrsZkD445Rv2CGXbUztVzkc8D2Hh0bEKjqfLM0UiH6FQrd4BseFIWy_CBIU3pVsDUAkG4yf1kdK62paS085bGz3fkoYrF3oM8X75X-Qnd5ryWF7leKO71VKBE_vCIC1rIF9oc5I2apSnzfYDHDYuh2BPX5D2B6CV2oemPurqfDZZHZLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=tVsCBEkFSR3BL-yL9k5jROQUW2f6eE_k8XCdIK90MGEjXuCxByjljVkkCfUbEvhdOW6pljFOgYELxF6jHJOCcy4oD0sJJOeVCglzvl8ZSDbtE8EflE3mFc6kMtJClGfgIETxJ7rosXbjbxeF5v54HpVAv3f_BE2aYPzBxd03GGqP2d9g_QyKUWbCBa7zJCftAWEhfaUsNUhH9OK8lugHmOvzRuzlcLx9cBIBAEgzaseYmy5BLx4wdoL4tzm2drtBb4NYc-Cn6NLZIlqJJ-W6dU6QkEwhYHAB-AP0y5WsT3ajWrT7Ln7qFavP_Xk6XQta4R70RGtZe0Ol0MdAUAoj2gj46a7aMGtDP5SLMI5QfLavEbeDBnntnJMkrNsk8F2HXGR05o642Mbvligy2qEkVPzaaWbzCWfgKJdFqADmJnY582QGCen5I8aDLLEbYPheUJMd48r-aAKI1ylhGoSKepwUtqz3lLARRsYUrBUruOip7KlQlBCYT0w3H_8uEEfxxWOoPTAwnV4Gm6pM4APkbkmr8bOaqFW4wHLBDIDgbnwEc6GrkA6Rr0vGifbw8pEPfDAp8pR8NTr-sR5SVQdF-wg56ymwdzniQJHAgzbOf1_t7Wya4aPwG8jhX6--7PqWydNqKy_SJMNYArrcjwRXR7vx8FG1xyXTxL_EOaiqCik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=tVsCBEkFSR3BL-yL9k5jROQUW2f6eE_k8XCdIK90MGEjXuCxByjljVkkCfUbEvhdOW6pljFOgYELxF6jHJOCcy4oD0sJJOeVCglzvl8ZSDbtE8EflE3mFc6kMtJClGfgIETxJ7rosXbjbxeF5v54HpVAv3f_BE2aYPzBxd03GGqP2d9g_QyKUWbCBa7zJCftAWEhfaUsNUhH9OK8lugHmOvzRuzlcLx9cBIBAEgzaseYmy5BLx4wdoL4tzm2drtBb4NYc-Cn6NLZIlqJJ-W6dU6QkEwhYHAB-AP0y5WsT3ajWrT7Ln7qFavP_Xk6XQta4R70RGtZe0Ol0MdAUAoj2gj46a7aMGtDP5SLMI5QfLavEbeDBnntnJMkrNsk8F2HXGR05o642Mbvligy2qEkVPzaaWbzCWfgKJdFqADmJnY582QGCen5I8aDLLEbYPheUJMd48r-aAKI1ylhGoSKepwUtqz3lLARRsYUrBUruOip7KlQlBCYT0w3H_8uEEfxxWOoPTAwnV4Gm6pM4APkbkmr8bOaqFW4wHLBDIDgbnwEc6GrkA6Rr0vGifbw8pEPfDAp8pR8NTr-sR5SVQdF-wg56ymwdzniQJHAgzbOf1_t7Wya4aPwG8jhX6--7PqWydNqKy_SJMNYArrcjwRXR7vx8FG1xyXTxL_EOaiqCik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCYU5vL-1HLmkkxsCWuO3czPQ-W1--oNa3-abDiijlxlKLj1GZ3rd1Psrts3CYY4Z3ZiWuWVmmlPF686nJClb6uoaOJGFo4e6CJ4fQnzq4HhaUfbQtWASRBZ9LGh5lhvFxnqJZ0Amq5DQvomRo2hM0n8fs1bQhFJtna8rfXsl7Zqw5-UBS248Rayw07XO-mLQyvtZJuYr1w0aak8Hghsu2GC_DUlMohCUnhRJb-cvM6JuRD2Vvo6mitZ4rOxgLWTplvyW2mXdRalaz3CfR2wTTOwbgmOfz-Ct-UGskZsYn12c2FIm5ZitLtXJLGe3cOlRhcrwOdyn_aEKAhDKFsI6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIwCjcD2HI3mzh94B_zJYVi9l6okY86lSAY47vDHjZlEaz2drvQ5wSsuQLGJy3fbih_C_6sflaQc0TpsmOEHah1potqAMz5xuXVVt1oqgyAJDZitz8WAks_or0SSgpMQN71GNduPM4PEK8PC9m8XsSLEcbhfRBxGpNadDA_3BuiNmNcPlHgsY50DRgbQoiBTT-3pVyZidMvyqU9qohRLfysh-vP643q7mo7ta_ngRN-l8-tqS8QjY-MbOggWsDoU1EzzwNs4r0kTPsyMxttgzhZG-A5By_iTEeFk4Eb7z7ZyyaMpFOFlKra6RNUiYup7i9sMkJf7gipux4KiespL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lj4WZRpLvwgA90_RyQ4I-Rp0BImMpIgZ39l3vPWtBqANdiUaRedZ9ta1ivVjkb7XZiUckXsQ5YNl-KU0DqAnYjSIGq20oRQFyRm7r2v7wzPdJYFc2dTZ9A7vnfTCSLyKVq6dslWCbT0C4ouk-ImR2J_T5IZ3Fj2v-jwQUeKn_ibRaKZmwtBenCJMynJhdDUQ9VPB1HXUtjh_uThRXkjlHR76LpTxv41rxvtIn3pCyc0e4-EjK3z2koqszMmF0H4_h9gtmJCs_-p5hPhBKqji2_7CLqq3uiRdht4033vEReY3U3AwxJEbGG9Nt--9kxI7u-oHZRN0ySvYB_0nfBUhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=ivdzBGsRDGiIsJ6FMo1USAFajtmzlDGNovYA9r47BwjVgOIh3WxmzDGbpU-b4emb9dIDVamWiBxjxVNPsQ9s2-6Mt2h97yFxt3E-K0zZtc4a2gHvdOR6HW8f77DbI05lE6sJjiM5RNF2WIWW3Znh_kbOEldNZLMFBHDHQWHs4Ahb0YRUyYeK93eJZ3OPOnwxvbGdSIFNI-Fquk5ZSIOZYaVqVM9_xGuZ_keSEcqIbiJvliIS9HH4JRTMPIYT2BNP3oEcRKwzifAT0_QIlXriIS9m6lDEHLqgj93qTZn-Mk9fASfEqHuT9tqhLbWTim4ecujTwtu4IAslLReKnEAM6USWs3CROHjZ1pbQM8A5TRmrqU0BI6naqwb_ahsvuFUpQDpGu97iTEON0SqCSWFe8DwKL8h5oMe7YIOVmewKv84FeIofgtWnJyOwPq3lpyz4s8GHZgCzKx3ddrM0uIrxn6useZIXraFSsE-ycbVkSHARLnmAetIRmMQ11sIga-5MwWYKoQ-ec5tGtF0LpCYihghVd3KXHY2h7cAuUW7Jhx1r7M59y24g3g-MniFDot1WVaWfdNJxml_ReEKzodSBO8uEBpiPWxH_K0x8vL6Khz2H2YVFiMeHRwMxulGzGfxfRpLjMcRPjGkNk6uy5HflmG9PZI-viIKqrBObZ6ZqUyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=ivdzBGsRDGiIsJ6FMo1USAFajtmzlDGNovYA9r47BwjVgOIh3WxmzDGbpU-b4emb9dIDVamWiBxjxVNPsQ9s2-6Mt2h97yFxt3E-K0zZtc4a2gHvdOR6HW8f77DbI05lE6sJjiM5RNF2WIWW3Znh_kbOEldNZLMFBHDHQWHs4Ahb0YRUyYeK93eJZ3OPOnwxvbGdSIFNI-Fquk5ZSIOZYaVqVM9_xGuZ_keSEcqIbiJvliIS9HH4JRTMPIYT2BNP3oEcRKwzifAT0_QIlXriIS9m6lDEHLqgj93qTZn-Mk9fASfEqHuT9tqhLbWTim4ecujTwtu4IAslLReKnEAM6USWs3CROHjZ1pbQM8A5TRmrqU0BI6naqwb_ahsvuFUpQDpGu97iTEON0SqCSWFe8DwKL8h5oMe7YIOVmewKv84FeIofgtWnJyOwPq3lpyz4s8GHZgCzKx3ddrM0uIrxn6useZIXraFSsE-ycbVkSHARLnmAetIRmMQ11sIga-5MwWYKoQ-ec5tGtF0LpCYihghVd3KXHY2h7cAuUW7Jhx1r7M59y24g3g-MniFDot1WVaWfdNJxml_ReEKzodSBO8uEBpiPWxH_K0x8vL6Khz2H2YVFiMeHRwMxulGzGfxfRpLjMcRPjGkNk6uy5HflmG9PZI-viIKqrBObZ6ZqUyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlGIeODfgwuW6ZOP4wqVn1CiCKlhdkceLgmbrGpQCx-6PDZqyLn0fvzGOFlaQg6tyhc0IhcupWLC14XVpZiouVu2i79yij1AL26TMNXfTsSE9eij4g5QJHTO3IcF7mF_UpQQAL1328-nPEoorUGw9Xd4oWsGTsmkk89pZRke_ojRAz_5oGnqAA0b3oNG0nC9GPsmdwWwdVu8gvhZMr05mHoAy6QEVZKLXwEq8wHoWiO_StQwUsOqcp3u5vJ_S7Qsuj9G0i7jOMEMzn2rx7oZa9AaAB9LuGCaMxyQ9HAMNU6ZN29MxJ7wYl4Ahop7LSUSV3QjCZLGjOdhHgRdzZlq5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlGIeODfgwuW6ZOP4wqVn1CiCKlhdkceLgmbrGpQCx-6PDZqyLn0fvzGOFlaQg6tyhc0IhcupWLC14XVpZiouVu2i79yij1AL26TMNXfTsSE9eij4g5QJHTO3IcF7mF_UpQQAL1328-nPEoorUGw9Xd4oWsGTsmkk89pZRke_ojRAz_5oGnqAA0b3oNG0nC9GPsmdwWwdVu8gvhZMr05mHoAy6QEVZKLXwEq8wHoWiO_StQwUsOqcp3u5vJ_S7Qsuj9G0i7jOMEMzn2rx7oZa9AaAB9LuGCaMxyQ9HAMNU6ZN29MxJ7wYl4Ahop7LSUSV3QjCZLGjOdhHgRdzZlq5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5XheA1rNZoGtSv3hFroa3qGj3hkvYQltlL12ZLce_kY1PwXIwj16nu3w1BBR4qouEWCm0UOHrWI0Abp7r_7YKEPWqixoGNYSSeJcP35P3OxdnGZ7mL-MHZ32dpGVBEtb7Z-NMdpFAeS9Ago9xXUO7bdHbsPlr9QrtQuSRrJ-6w6WOZMaEorNkAtB7XsHTfkyx0XlyyPcFvld71ijANfpFUc7vazzhFasIp-CTQKp9SrvI6J6p0oU47wdPJe4fmUjqSkZxUit_cRmU3DSykqHKwtg_fMDYWlmM1R87sXLaynQ2JF9TEbGlh0SnBsMcv_x178MBRlnmtShcdqIdyc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
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
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPindDGIm9md-fNWzbWKgWzLSKy_0ifBUsHU-6SpJftJMS7za7TqP1FbQMHtqgUlCxUGl1Yx3tYy-eDRmaO33CCeS0EfMVL734HNyaoW7IZmvLN3Q4jSQWrIOHuN3pyrHd0BHfgdn6CgUXM9ORICD2Ugt8mnmAPssrVqb_BWz-NqVymTV2CNPAUysOLvAW1diqLLwj4U3PGkusfNb2zH-iFVqYQTF0FzY75MD75gXk1dlO5HfW6FhQhVtlSeOcaLcumeEIrD5KFSzmUIVxYEprFAPg-5kVxk55cgYOkjl_GxVUfqHsVz8IoprUNBeuXlJUswbTHzzLsynODag0Nwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsYNc3j_YrYvMZ0EYS6tEzMk7_nIu6ZfbF3DSTrEk7UQUOkz7-BoKISumfgwGAQ-5rDw9-oTMIZsQIojVwCqicGsS8nU-ENbTI_rZfnjKKx3nd4yG4MDIW3j0GuRsjZaod-9AGYplTDixI6kT5CJ6n6hOhGwRkDRuGKdV94cd5lQyvPry0BCJYBnGkitzC9RJpxC8xeHcJ4KLaN6erX-5g9CLE-gudLOTlwDIHTgsDrYWu1B2GeIDs1nMnQsPU6LitPIfR3ThdW5bw9WDLRJ7cCeYoRu1QUR93n8b2PGDDPTBKNVLyDAf9ChCqkXrBHo7qTcb_VjWzLv6Mng1TLEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O42wgb3FHkx9vyDlrLYm2OBuozMn762lUQbRE-LQrvQoGybRWroo1zE5FOA729ISaq5LcNcbPAjzzqBEhoLMOzZGRWDzPXyKt0Dxqz2byNECCFcJFqEF1bZ0C9nRgGYn4B3n0Gw3ZolfaXW-5pE1U1NfL7CoC11jios41fc3Mmsmqp6MWYuSD7S4KHmJDm66tdJLjoKTft3XFdWokt8368jlbjV6qGUv8edHqvamNTs_hn5KItCbK1WnBMAoaBSp3F2Rd5xat7AQWS6gc8Tp7bReqznNONhfsmuOm1Qa7jlfiIoJbvpKZtqpPl2vaiSVmu_hvUDxnIw2gEp153SeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnAszPVWz5C2v0RoJHr5OeFvFbTnrR8YT8lbLTAydsuAFBRajFbj0dkLHq9ebDSi8PlCMsooBnLvWcy4_wvQpMSXkF13qqwPOJ0lYcmOwBDVFqBgd94iREjwSi-hVgkFvlm6Z5sOTWn2qZuIH6GaR_wmCu9uusbLoWXqykhQWDHBaH_wQXFQrQFkoLo3yhECjgZTY-sa20ggbvigEkx5b_SJZFhu4b8bbXiO32GMIIiTKUCwbk2XjGlzCzsGFXprmBtrKvSoJ00UPSPZahy2jW9c4YeohYt2deoafWLLRCEEhNhuaEABXkxPjzSOe7j5u7Rogdga-2Apt6b7bw84RA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
