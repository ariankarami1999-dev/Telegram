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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 23:33:35</div>
<hr>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAgp-u3WftXL4-MzjU7BupEV3oOewG7a8sqbcx43cS7pNDsn6KPliqAULPHg9iF70PgLNy1ldAW9KWQrM16lYYoGhj2Qh7kApdruKkFCb7wZvT95bmrD7SavLOj5GGe1Y11Q2ZTeI18FDn2thhDv782HY9i1giOUh6YoemVbOLz-s9sr4qPRs1BtDcZJTni8rCGMv1xJ51VlMbJqRldoysSONjcLfhyjM915_r2Goib9xg79CIuhgaSFsVd11-8nIPW_wxuQMIdrfoWlwYPGvLTDdWFqfbA2JNXRCbhjOKr86Pj69N_Vufvedx49esXLmuYDnRl0cDLsHQoBymTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRz0TUwCDuKo6AICKxJ23Don7Ig0m6TN5NGIBRhtc4Eb_-ssrRnGgLmhmTz0oIYxq3MMfDWNK-bVxHuig9GdXjzHhxANCRkFMXDxnfLlgPwuHyB5pQMtGToEtjH7DiHv6nL50vK1RbLFrqlzyYZ9ZY8oNDoIIJ9k06PyRhC-2AObNJ_9T1bLAbZQ45gQcRXhxXi-zJNAnu1q1OiE7z_yLF4bRoTP0GW3TIXl9w2AkoGU_sVfFXblNn2UHD3_W330a5OSLfUJg3xcaELwWENEYeY8rI_aAHakyOvoRi_E5htgJ9q_V5TWfclWBrAz3klxDSBPOTTQ1OWNJE1x3hBJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knCkEY3XzxSfKy8BRnxpmItpMRIXrSJchKSPrkjpRbuDaYncx5bJIluSQdif6A2L_AkEraQgRoc9E1QMifEuiZjstl3u7Cpz8jeazNAJx3q1e4WHfx6UGKOCVj1k6KvzxKxX86I9m9so5FXW3mfVR29Ia8aX3uZu350ZudYpKPe44FMnyNWvELfI2cy271oFtNaHFRAPZTRVu5lH0pjd3WArkIOTI-eVFGfMM-GkapE3tuu0phmTyau_jbstbytkyPP2k4x2Irt6RoWXUsBb6rmeCtKQpKwoe6akOpgLkWGdQm2pvCbIJaQb_0cvC0aqojiDmTYFrzBg9bQg7ULJDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=AnsaM4Mw8tXW6jtqPJhwi1Ayc126G67zkRdeBRdiD4S0fAfWi5hZcimMtxK6fj79Ml9M3ZAV6tKBlRLtliOdWLVm5dwybbpl-xJfnowCWKUeWumFZ5VDqV2SRIFzM0q6RtzInuXySIDK3u-nl7n6soWq4FjVtTYM8g1e8Ha28Qp7DD9_-doLqKiDSxcPuZVJm5TTpw_OIv3Oku-QDtz5HDi4OIcS2rd9gQ-2qZUUE-9SYGRdj2mRVES6EodrLHg16ka5p8GLlD4m1iHGYsL1ytodgaRl1EuyBI_BtNrVEbwNXhPNw8KEfgxw5A9f2mSkQetNzwiClvwIGbcpCxSNMk3jBtHBLp6c4PRsauk5PGNMZn93FMxnBnzBhY_b_qBEyMWK1C55YwyWA_IQa9GkWB3iD0GQ7qFW503IhjobVAo3j8XktR8Q5__CdBvqcs2Y3oGwXkrZ0tv4wGt_TWcpQ2Y6FUEGpMS3yagQTGeNw-73o2oienbtU53DcR1mqeE2NtH0makEI_Kg41FW_y7WobTXcv5pRPitDBYtVKNSF2Avlti7Vm1hFeH1PJ0jS1S65NAJAnLLxvVomyYe0psH33g-C915nMOgpADx-l1CTQ_nETuX10NiEaROtIi8dFmEmBvoG9ahUcfcEJjqxHLeBx47pDzZopX2CpxeSqsUGw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=AnsaM4Mw8tXW6jtqPJhwi1Ayc126G67zkRdeBRdiD4S0fAfWi5hZcimMtxK6fj79Ml9M3ZAV6tKBlRLtliOdWLVm5dwybbpl-xJfnowCWKUeWumFZ5VDqV2SRIFzM0q6RtzInuXySIDK3u-nl7n6soWq4FjVtTYM8g1e8Ha28Qp7DD9_-doLqKiDSxcPuZVJm5TTpw_OIv3Oku-QDtz5HDi4OIcS2rd9gQ-2qZUUE-9SYGRdj2mRVES6EodrLHg16ka5p8GLlD4m1iHGYsL1ytodgaRl1EuyBI_BtNrVEbwNXhPNw8KEfgxw5A9f2mSkQetNzwiClvwIGbcpCxSNMk3jBtHBLp6c4PRsauk5PGNMZn93FMxnBnzBhY_b_qBEyMWK1C55YwyWA_IQa9GkWB3iD0GQ7qFW503IhjobVAo3j8XktR8Q5__CdBvqcs2Y3oGwXkrZ0tv4wGt_TWcpQ2Y6FUEGpMS3yagQTGeNw-73o2oienbtU53DcR1mqeE2NtH0makEI_Kg41FW_y7WobTXcv5pRPitDBYtVKNSF2Avlti7Vm1hFeH1PJ0jS1S65NAJAnLLxvVomyYe0psH33g-C915nMOgpADx-l1CTQ_nETuX10NiEaROtIi8dFmEmBvoG9ahUcfcEJjqxHLeBx47pDzZopX2CpxeSqsUGw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5LS-VBK1ogpWmbPI8HJbJtJkUSdSik1L43TzI5MXbizDQdJjOhYt8r6a-5XDFBUUGiYWMlgKEhVO4-azmzpG-vHZkEAEw1q7tOIWpjXfyd-ABBa7HzU-AyXxRXdY1oVtsGGeMeDnGIdJs_30XTjd7hkkGW9Jlya5qeYvTk12y5UVqnP9XVeRxtpn6m3vH8nM8MamYiV7LSknhpWOwh-EJ_wbnXSN-PnMx2zQpYC2aORBCsgjFtLgIWKlZFO2_t293Dt1mLUnHACPCeCx-zecUKml23BLYrzXO-wit1vD172MmHgSRuTiFwkk_9hFS0twka4d6ZZxiY6eV-gMQTStg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuBHkb-WZBvtZcI6EUIUQEZbszwgZKf0an3fBQVrSPJa0eTLGFg8LZtSPk8rVQOS_O6JuPGxoJP_-S008ITXT1t-q8iusFbqUKPBiSZhp1v_lJclzK2MioOrsi-BBWvReAT_sXe1SNJ2fzJbxiu1gNVjvoqChZfzkEH2-FW_8nResSSZP9C_a0OfJc_WTtdfoEkllMr-gf8Z1fUYc7xkWSPpBJZoHD8UFxOByCFcBvLDcPAROEV8WjpuxjNHY6Igry6Ug2PVXaWDeK5DuDPDqpQd6fRd1qR2OaaLKZpi4c1DnC0jW8YUxwuUl8dYqxwJEJ0J-ohJ1JG2r0NqTqsIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=e3BPb_e9ye72cFU5LXsiz9eDBweUfXzaqV8COK_H_KHS627XyUldskGd-fsoKdX1PYI8EcaJkiEQ2haJLphRcdKn5b2HEwwWM3OjQEt65yQIeYUcfPsUT4QkZ3y2Q0-TaHuvU2bW2lwhvONisoBnVaDxLd5Q4expos4e3SFCfY8_Ih79DCzLSfHqAgRYLG27Qghwr5m6_wmt31jQpjPc_FE-z7SXXADGMZrTVfxh2F3vd0WVUWCx1Wvs49ODsxx2HZt_KL0lh1o0ILNrZzPF1gkTbrvRLxWFcx2i7jIufIuaqBU64Gjpi4hfHUmzqK_PgTxklI6W32v0xrGXy2fP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=e3BPb_e9ye72cFU5LXsiz9eDBweUfXzaqV8COK_H_KHS627XyUldskGd-fsoKdX1PYI8EcaJkiEQ2haJLphRcdKn5b2HEwwWM3OjQEt65yQIeYUcfPsUT4QkZ3y2Q0-TaHuvU2bW2lwhvONisoBnVaDxLd5Q4expos4e3SFCfY8_Ih79DCzLSfHqAgRYLG27Qghwr5m6_wmt31jQpjPc_FE-z7SXXADGMZrTVfxh2F3vd0WVUWCx1Wvs49ODsxx2HZt_KL0lh1o0ILNrZzPF1gkTbrvRLxWFcx2i7jIufIuaqBU64Gjpi4hfHUmzqK_PgTxklI6W32v0xrGXy2fP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmtBn1w2i7n08fgNoGYf_TzHmYVBatXqhdaP21bfjHSFTUdyp61Jrpkpc4eq_eCdZyrQp_-o2T060vxlJfwpeCCB2AiYDno7B7WHv0uEvipuPk8scN7LNakCG445WHJq5ERUxjX4AEAbsdk0Sq0c9ytz4JC25YsFWfNOIvJe3WjI0FEN6FwqUqYqkqaGAWdLjBDsj-dHckH4Kme6ojtpjjipjGnWI7guYueypkFaVOlT77N3GzYoHNGiI352ubPOguHeTZ1MyhPOiRDLYj7pS44sQhsD_rL1PO2P6xhmw1GPf3MKYVvXRcEGUv2uiq35OEbYdte5e48EZ0wQonoDIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlP6AQKg1uPU5n6jfSfnz0T-ZOdL1UP7U1c0nxIQqq5UmrnQ_HczO1uM81aNms8hEgtQc1m7KXj_PaPPj2PvEcKOq3YVb7vFv51eW6h24nuv2a3qj86cWEPwieZwY-2xg36A507ZIWbdcRcw34WJgEJxrLV7epZH8KM_C5jeqenK3O3RVvLtiW4OLYhY98K-1CwW3rWzLP3pCF15prTP_JFjvZFTJ5PMqB--93Iszf2lEz-SpnM73JFTVcSBQ_j2HuSWgdR78XUm-jLU0rAu8DmS2DDq6BjjFR-MrDu3COb7KcbnikZwsSSZIVFmVCp5I00lHp2ufUs0Jk9nCpk2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=tyC8C_ls2N8HvJ3qb7q7rljU_bn8fx-lPb2GjW7LhJg-eojocz6YCAofTomj3FSyK28CnVb2t9AIEVzvV4RGfR8hzHXviV8sPcPRQkOZv156O4BVoicKd_cHxx19hJT-KqcDmzP9nddWLt29QZYGPRiFcW2aQk8cm5l-Ml73IcqW8xR1396GzWGt4sRwJnPxh5r_M3R8cvpd4icx-4_bQHUgBKus80SRs_s98nJa8SW-mKtQSJTE19AFxztuevHxlPRBi5ew8YMMUbBKgd1DTrLphdXmL46wpfrEsxqQyNaI8HooaFwzfKB3H3Qh2HbYm8VPtg-xsV0-1d2X8zf2kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=tyC8C_ls2N8HvJ3qb7q7rljU_bn8fx-lPb2GjW7LhJg-eojocz6YCAofTomj3FSyK28CnVb2t9AIEVzvV4RGfR8hzHXviV8sPcPRQkOZv156O4BVoicKd_cHxx19hJT-KqcDmzP9nddWLt29QZYGPRiFcW2aQk8cm5l-Ml73IcqW8xR1396GzWGt4sRwJnPxh5r_M3R8cvpd4icx-4_bQHUgBKus80SRs_s98nJa8SW-mKtQSJTE19AFxztuevHxlPRBi5ew8YMMUbBKgd1DTrLphdXmL46wpfrEsxqQyNaI8HooaFwzfKB3H3Qh2HbYm8VPtg-xsV0-1d2X8zf2kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJY4WHDphE4_gemBrnc11G8BzOPUorZwCIvIQHl9FKFqz9o8Q5NGU5rE8ahRCiwxyu10KiWIu7j2GcZ6oS8TOsxjVxAE5Mxzzf6RbYiRtHOzNvcNzHD6phwpbaooIGSQxUHus6nkcXV63G4BfbHGFAj9Y75RICrIN_rA1Vk2b4VC4DBQFZwaMltGuetGfhg3xImnxgQF5v4RdOYlYlbY4GNT8AXvF5YPsyly3K_gh5S2QeUbW8WCcsC6I74lGRySSsJFElovkCW_0OHP0JIj6yrxiuoHpL8bTjPfInw5bFsu-SGlWcKXq6qAABihKausHyJNjKresk4-cE1TwEoZnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIwCjcD2HI3mzh94B_zJYVi9l6okY86lSAY47vDHjZlEaz2drvQ5wSsuQLGJy3fbih_C_6sflaQc0TpsmOEHah1potqAMz5xuXVVt1oqgyAJDZitz8WAks_or0SSgpMQN71GNduPM4PEK8PC9m8XsSLEcbhfRBxGpNadDA_3BuiNmNcPlHgsY50DRgbQoiBTT-3pVyZidMvyqU9qohRLfysh-vP643q7mo7ta_ngRN-l8-tqS8QjY-MbOggWsDoU1EzzwNs4r0kTPsyMxttgzhZG-A5By_iTEeFk4Eb7z7ZyyaMpFOFlKra6RNUiYup7i9sMkJf7gipux4KiespL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O9SjbyUumNpNJ1-gcsxDRBdS7heCzzrhKzOxlC4Wm-MDM6WvQ8D0nXv4-RfTN2PA0TnLuzeKfss1Utm-Bl_cT5gW8ltGJH8aO8HP-SLksM7iSdNFIPyd0N83g0O8uw12jDf8uuu0pykaCVIFfATKyBn0EIgKYqr8BVjpLAFj5bjxsnMiZAI86h8MVSbvQWIQj2gtr9B0Zth4fDY_vEQePRcOeHoxmZJfaufrixNq9A_9QCi_cyYyKjx2ufdD3SKkcG85v_2InGKPlncvyLpsNhWvzY1ObGGGRgioYRXr4d6KpLrzIoeUuk6UBYukAKIFTZYgot3WPvRVLFSRmLJnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
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
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=pw5q01RP0qN50wlNxdTPWhyJ8cnXSSvn_9MzQ79uU336HznHKIQ_NIXBpYTmE9dG7S8OoN1ym4Ak0y2-Yw6TQYLogSRaDMeRdBTVAthq47EYaj_V6fHc9DDwcUsCoDuIfoQ1ps9Bi4ZT9VrBPSMHuXgpzwWd2SE0dS823Sq3HEgEe6bH73hWxgQyggjVOUnth8xvKX9qeCsIokOjUJtEvf1A1YO4Tdi8weA5P8eXnspTMxQ22cxbbTn6vuGPtLbH9Jl6CQxumfmTao6ntLgUCq0vcXoNUzv0pp-eRfwcpy6RcuT0vCqVV-9abhiIvPy5RnIyJ0_hdkP2YQtN9VZ0crMA97MLB8cS1tF7pSe3-NTBnrlgd3AMHpmX8EZggsg3p1cXmNbJ7hbgwEtX7eUejNvvazUC6qdNO4kFThQF-Z-iFQylFvdMp3GQU4OYL2loy9Ansxna-a8MejSqRHvbUcv5sEKKS_Lngjl3pI6AJ2vLBDbX3exhtxAW32Z1hPB5kByOlSno3irXnih2tzDd8ARDaJQHx7WlW3lKSgfaEHA58LitH8dq2nSKdTDmEBnkWbUUcaqxOzJrzHkeolhCYla1ey0h9nfgBYjoYBt1RKBdrW5PlXXAQ7xnTjNHONKR-KvQVIJnAoZ9s4MUDu8V3OtJ2LXaYPu0uTiiJr0mm5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=pw5q01RP0qN50wlNxdTPWhyJ8cnXSSvn_9MzQ79uU336HznHKIQ_NIXBpYTmE9dG7S8OoN1ym4Ak0y2-Yw6TQYLogSRaDMeRdBTVAthq47EYaj_V6fHc9DDwcUsCoDuIfoQ1ps9Bi4ZT9VrBPSMHuXgpzwWd2SE0dS823Sq3HEgEe6bH73hWxgQyggjVOUnth8xvKX9qeCsIokOjUJtEvf1A1YO4Tdi8weA5P8eXnspTMxQ22cxbbTn6vuGPtLbH9Jl6CQxumfmTao6ntLgUCq0vcXoNUzv0pp-eRfwcpy6RcuT0vCqVV-9abhiIvPy5RnIyJ0_hdkP2YQtN9VZ0crMA97MLB8cS1tF7pSe3-NTBnrlgd3AMHpmX8EZggsg3p1cXmNbJ7hbgwEtX7eUejNvvazUC6qdNO4kFThQF-Z-iFQylFvdMp3GQU4OYL2loy9Ansxna-a8MejSqRHvbUcv5sEKKS_Lngjl3pI6AJ2vLBDbX3exhtxAW32Z1hPB5kByOlSno3irXnih2tzDd8ARDaJQHx7WlW3lKSgfaEHA58LitH8dq2nSKdTDmEBnkWbUUcaqxOzJrzHkeolhCYla1ey0h9nfgBYjoYBt1RKBdrW5PlXXAQ7xnTjNHONKR-KvQVIJnAoZ9s4MUDu8V3OtJ2LXaYPu0uTiiJr0mm5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBqftw7Y810afMfQpRIjL8FKhJmItdH2BwC2lkmTsiu4Hpl5EFUxqXdVll5NDDoW1NrrGywqN0wnSwovW8sr_9JyeGlm4eCnL99XUBqynPyzNR2ex65aoYCw8tgJy2Fsd7NwWnqeN5VsP-nHlNcbD8SEPeDtvHWf-6bZYaiZUkMDef47xO_SokXv4S4RMUrveBCvmV21fMLYS2vna1KrYWUcTpju6McIUNjBLNRO1QfV_EJAjbwH9bvs7a7fJynmsmNu4ZwpU3XkQC_JXH-Xa9_G34GcTs82Bmxz9QTlAbzdJ4wrcAS7RXThRPoH8wHorcMtXrN-H2d6IFE4I_ZK5yAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBqftw7Y810afMfQpRIjL8FKhJmItdH2BwC2lkmTsiu4Hpl5EFUxqXdVll5NDDoW1NrrGywqN0wnSwovW8sr_9JyeGlm4eCnL99XUBqynPyzNR2ex65aoYCw8tgJy2Fsd7NwWnqeN5VsP-nHlNcbD8SEPeDtvHWf-6bZYaiZUkMDef47xO_SokXv4S4RMUrveBCvmV21fMLYS2vna1KrYWUcTpju6McIUNjBLNRO1QfV_EJAjbwH9bvs7a7fJynmsmNu4ZwpU3XkQC_JXH-Xa9_G34GcTs82Bmxz9QTlAbzdJ4wrcAS7RXThRPoH8wHorcMtXrN-H2d6IFE4I_ZK5yAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5XheA1rNZoGtSv3hFroa3qGj3hkvYQltlL12ZLce_kY1PwXIwj16nu3w1BBR4qouEWCm0UOHrWI0Abp7r_7YKEPWqixoGNYSSeJcP35P3OxdnGZ7mL-MHZ32dpGVBEtb7Z-NMdpFAeS9Ago9xXUO7bdHbsPlr9QrtQuSRrJ-6w6WOZMaEorNkAtB7XsHTfkyx0XlyyPcFvld71ijANfpFUc7vazzhFasIp-CTQKp9SrvI6J6p0oU47wdPJe4fmUjqSkZxUit_cRmU3DSykqHKwtg_fMDYWlmM1R87sXLaynQ2JF9TEbGlh0SnBsMcv_x178MBRlnmtShcdqIdyc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4Xi3TqB-FZ9LO2XLYpSMPi1BEMHYceSejU2sltr0a5qddLcxs7SumdJfGe6pOhU5IPq0bpSMmGFtlJAVqdnjQjz_gVZIUVg7srVHu6Jo7u5ivOA9Sp2gAmSqqWpI6-G6DUG-XMMla_-XoHNasySvzN6paMO5DgD-vJsFG63CjuK_OBJGPKiqG6D97kYzFGGDIsPnHNu2DQZRP6sLnjbTKVZmWHqzrFGwnbMVACYPnhN6fKaABRfUxIZqPjw6I2Q9aEU_YBf2RA8Cep0NkC2Vd1Hdg8Z7KzI3s_yvSDC4rL2ozFIb5mIu_QXFgfRFLJhvr30edI20nAzVY3pP2KCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
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
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BR1sjR-Cr5UZHfU-AtZ82oN6DgtjmKKKDJOdjybM6KMdK9lShuYKzHHHPi-llsh1P9yCfulJHIdEMNIwjei3AClJJ9tG_nfbnIxZa7GJiGtu7twlzEumVf5R_NNFh_r2hsdtKPWM07KpLLXFTwaWSjnhFYyd4q4ODjQY_lySamnLxeTzOCm_8HfvZi6NDgYZju2mHUu9JqBWu3J5Gutf1ZhWxfqBqrjHM5RysUN2B8Id9krukW9FlsgIDclrEIIJ3xifPuhW5ZnRQbgM7D6-VcrzUm1WkRfflJdjv_EWacY9nkjoa4B3Ku8F__Hoz8cF9AuY3SUYtUBc52g5cmq27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjTsfH4EQ0jMndnwY8VLvf01b3pTymLyR2PdyrVIC31u7JymtT8_fJJAfezgBsRBZddrnU8iSW8x7V0Ndw0ypVf9tbeybeqYOGrh_iZ2UYz1kR-OlNyg_bblJ7YVVeb56982lAEQoAidjH4LnCCsSKcNgZNPoMe-CLmA3jvoOzmd0kEmRz1RXZFi68-fnc7NpYnTU1IFG1kZRAcCER5o4FFp0-ZEOnSI1l4I5wQdIbu6hUWjoJ_k58Ar5B-tmF5bwTcnHQJyGLd5qvX53KW2ScOhrO3SExW2HNdvhaOHTa38WXtGIBA2Q4ffhvzjQ9UkNH-m14TelfG23u3XgfWi-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4yrejvoggqx9L4JT0yxLiweROV4r9EAgkkNYtVf88ULoVl4Mcf437wR4Uh58lRiZgeyBZW3pyIAtLRzjeTrSlUdMZ9kZHgGo0MD0SpSgFD1e3lUhQSh7dS1G4a59YUd6fkPiuQ-1bnMErUgYOQnqOOMh8256mfGUBZ4brjlvjFAaQaS0NJiQPqJErPDNruvL0z8nWcA3P7HMl52aOyNWOWhM1Zv0vtlfKszLWJQqh-5YQxGqZtTy-Nh9b7-mCUwyg9-O-SZOLzW41SEHIvCy16outU7ibaKlhr4du94x8ojNUgDyVKwDqZHVGNcm9qCqRNC3SLYvz2woLEtqNZPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
