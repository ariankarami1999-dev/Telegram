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
<img src="https://cdn4.telesco.pe/file/e1rw8L8-aHP8yel8QZq5_NYn0zZ0z5UBiUu15mPsSa8dZuQ5FiPdX67SfqZ3ECpnNvhqgKw95RnGcWKofMOQaI4HQmyvVNnxYSC7v6LgqJtD3He9yDFEEsLu80fuHMn0_3LFUopNulup4SYERN4ow7VqBnJXU2Q_-rsYqiGtVYeQfw_xunUySA8Qhw782mpAa-qFd-bb2fD3SUo0JwXXtQZ_Bh2Fd3osRyQ45MRBKjMiRzC_y4JHdY7we6VPbNwxqCj1-zKBoupDLqP3rep1vfPbV_V4382ovmbCpeC9QVbJ_wb0xrZIJDLFvbAUnf8kVpgpzUW8KLKZ9TjvuD8JAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.1K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 15:06:57</div>
<hr>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_k_X2jrUJw13SwIUi43idiuvuew4osSg4CLMy2U8A-WKLb4sHop0QMEqMxdBbOkDQpbQ4ET6lB3orDxzSHTqNO1c2WZj9DC8ft0GmGo3-FqE3iOzV35DViypiarbbWJswkfck-78HaMg3qEDFfX2VBIazvLrvtwW9qRztx-CwP8D6oNpRcWvr4ckll9AyOixPEa2bsVu9SH19vK_gxZPQYN0f-OoSdRfBKeOP_EByvPiG81vHXln1EME-8M4aNtPY-26TCLD06PMdZbn77YDLio31-Wls5HpK3M4I-zN2IryamFmWa7uoowm9xpCXVT0JbcDLZ0rXALN4UwaNzrrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=E48Ve9IEtSJgp5v2rshDXPXcTL-XH0KNpoFSe1gRcs2Gejsk9FUp7uHa1VcCWYtt1-dCuUY9gT-BAmb37NQWpTjjLfr4Dr2g7alNyZThdtgJNX0pkigLj2ULBCC-3ZnecznBVOE_O6Unet6VdhzKHL8165itMKJTiMlbzLvRTOihK1cVHb1bULIeB0JMyULoXk5lDVXfMq4eFkJ2hr1vOuEM4wLmjzkXZ3WB_JZ0BoW1xjxGP_5b1HTqfXJVwmJKzy26IhgJV2m7Pz4Evntb0gxS-fiDsZhXeikHsWBsnYXjHhTa8tJjNWmkWmYEca15z96wxzfqveF3axNA-RZxkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=E48Ve9IEtSJgp5v2rshDXPXcTL-XH0KNpoFSe1gRcs2Gejsk9FUp7uHa1VcCWYtt1-dCuUY9gT-BAmb37NQWpTjjLfr4Dr2g7alNyZThdtgJNX0pkigLj2ULBCC-3ZnecznBVOE_O6Unet6VdhzKHL8165itMKJTiMlbzLvRTOihK1cVHb1bULIeB0JMyULoXk5lDVXfMq4eFkJ2hr1vOuEM4wLmjzkXZ3WB_JZ0BoW1xjxGP_5b1HTqfXJVwmJKzy26IhgJV2m7Pz4Evntb0gxS-fiDsZhXeikHsWBsnYXjHhTa8tJjNWmkWmYEca15z96wxzfqveF3axNA-RZxkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D56HpibQDd-A3xeByt62E_7l-wfUbrqTQbmEB1UUw9JaBM7xlkM4wGgLSdi2JeOqO9MjU8Vv2-T7kONo_1AIob7nEJXPacs7AMfksaQy2bdSajBTkvU0rRNpu0mzlQMbW58xsOWGYYEZ7tOVYY_rPx2hyn2RZb49j1WUB4uH8XsJFJYlC0iRbqtpnGImIa98LZClioufftVt7GsaMJAN1z2LlxHWh1f6DWT3Eo59EcQmXCZUvi30GrMz_G3DMyDW9yGZp47Rsaal3Fd_Mz3CKYn9yf2j09vSZYDQK2dQcA9oJ4D3DEG-nDvlNJ-j9_7cALOnPHELSqdbOzVnbP3xjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQq1eKHfXOzmfXc3_QtlxaZTdB0gE3v7j5WNtXCfffCL4D-OiqV-KSHEhyjFZNPfyqLIKYj6YOKS8dF7tWskqqW7_M-_yaY0g7gEQ1AEJZhZ5UdtxSZrWuucZYUCXZv5k8OH1NeK_6lRaV0S58UejqfCYGSrAgxJwLAacdIj3gwh8Du64xmMoH29UUpSuSDYcMXVQwo-Ognj7iJ8xxZ7xh8Wy-uxakVNySKphRz22mGVGkiDjNScDl0kihsHWk3UJYHD-owL791I8A1QsJarXlN_6yUAmtr58bIrP-RTCiQSga4EAfxYUHe17lwy5b6Z66IUy2K5cwGaRQti3bCdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkCINZeAWaz2fVAMfRt4LWGSpMZWDsKcnlwInPqVp-aCU4DvFZ0PsDLkBIdO2neLWnSnT9AnvZQJaL0Y7uQi3GbpimECanBM7hF8wvth7SY30CLg5lF8GO_Dn9AgSSOaIWyZ7uwroq1_ArGWPt4B_2g61FuQgplni_eyyCKEaWGWsJP01I06bYX9DCRrCkJWk9ee5n_8gDtGa9wJRvHCRxusbVo8wlticLtiia6UP5lF3MFzBfbuI_83_bgV18upSlM63l1MHRKxYYYFjrfsYtI7-1a4SN19RHRCLAGoAFJIx0c8uOP5_sURe-CKxBKgbj8R5KFGqMNzG02Zbrgz4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=hrv1gb4dk5l-qMOZ4dJH43o1yNOrscpv-aKXRi5R1ug2NX5QeKxBWUnAGsmp5xEuyXNTR_XQuLksrBy78E163GhGxD_7vBWHzS3EOCleXqjvkM0ZAwFZKHsJ9xsUpZnkEKuLfkm4Pawq39k5DyejPTObfc32cv4b0ACEhTo1dExHnIIA2grXtYTVw1eoph3BTA00RBAOw40QkW9YtCHGJYsm7OZwsxgvMOog0o5eqHPZ_C2D7qcEQ5UUtGTm84lRLdV0-TWMAgeRmHc8hZmIYKN0jxGN8N-gs11vJqS4An7d5vgrXFBBEXKCajVzBecGz6A0uYYgC_CnztVy2LICkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=hrv1gb4dk5l-qMOZ4dJH43o1yNOrscpv-aKXRi5R1ug2NX5QeKxBWUnAGsmp5xEuyXNTR_XQuLksrBy78E163GhGxD_7vBWHzS3EOCleXqjvkM0ZAwFZKHsJ9xsUpZnkEKuLfkm4Pawq39k5DyejPTObfc32cv4b0ACEhTo1dExHnIIA2grXtYTVw1eoph3BTA00RBAOw40QkW9YtCHGJYsm7OZwsxgvMOog0o5eqHPZ_C2D7qcEQ5UUtGTm84lRLdV0-TWMAgeRmHc8hZmIYKN0jxGN8N-gs11vJqS4An7d5vgrXFBBEXKCajVzBecGz6A0uYYgC_CnztVy2LICkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=GK7FWFDCEBmRZDAl8muXHGXoGF8dW8dxLQuWiUlJpMgAvDDJtvIp-rphnml1vydOsnTnlA3Jn73psQoerFvu5i0c07fwOdZLwhefgN7RcY5fsR7feP3J9Q-LloQxywvJdqDjycsDvnq7FpWrCQPcLRE37wrbCHJEhfW0-aRJXiauHMU7W1U7iJ_QyD8dRWPBI1Iugjz-eUDZU00jyepOzl5wn4W22TSY249R9nXTkuj2ekOQvJedDRmYAHhlFxxpwxtp7cy6mDcZa4Oas0VWybt2zAT9tDMg03u0lEORW_tJz3f2JwDl6XSBFJdv_9SQig07iv3JCIL7BykXKOAWgpiUriFEAhkIOJ4eTIU0nX6vGAYL9Qgw_cJD085Jy5zSFpGeOQQ1eKoO5k7nrSTaqzjApHT2D_QZPBXmTHWuf0Lk49ePgM-vgcYLZXcB-v8wLVUVqoF3t-qPYcxqTOduLdR95ST7aPIEg-TdRu_nPH4JqQAHWbugIW2O-AfA5wzlug3lXZ86fQRGTaocpKGATSXKblz41gXqFosyvthZbqzrel5REq-5lQ-ORFZ14oTh9NVx6Ki-SN6HvuxT6F9h0DkiqDtEkpVm6UYSiw52x4Za7Ofz3KeQFZ6Wp2slQWg5vdT4sI3qXVEAC_b6DNOaDhiH7FwoyFhQ-4CuXaE4IDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=GK7FWFDCEBmRZDAl8muXHGXoGF8dW8dxLQuWiUlJpMgAvDDJtvIp-rphnml1vydOsnTnlA3Jn73psQoerFvu5i0c07fwOdZLwhefgN7RcY5fsR7feP3J9Q-LloQxywvJdqDjycsDvnq7FpWrCQPcLRE37wrbCHJEhfW0-aRJXiauHMU7W1U7iJ_QyD8dRWPBI1Iugjz-eUDZU00jyepOzl5wn4W22TSY249R9nXTkuj2ekOQvJedDRmYAHhlFxxpwxtp7cy6mDcZa4Oas0VWybt2zAT9tDMg03u0lEORW_tJz3f2JwDl6XSBFJdv_9SQig07iv3JCIL7BykXKOAWgpiUriFEAhkIOJ4eTIU0nX6vGAYL9Qgw_cJD085Jy5zSFpGeOQQ1eKoO5k7nrSTaqzjApHT2D_QZPBXmTHWuf0Lk49ePgM-vgcYLZXcB-v8wLVUVqoF3t-qPYcxqTOduLdR95ST7aPIEg-TdRu_nPH4JqQAHWbugIW2O-AfA5wzlug3lXZ86fQRGTaocpKGATSXKblz41gXqFosyvthZbqzrel5REq-5lQ-ORFZ14oTh9NVx6Ki-SN6HvuxT6F9h0DkiqDtEkpVm6UYSiw52x4Za7Ofz3KeQFZ6Wp2slQWg5vdT4sI3qXVEAC_b6DNOaDhiH7FwoyFhQ-4CuXaE4IDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa5JDJ7xu2iHDewqW4oSnYHyPuOOKSWn_0n8DF7XT0o_TS-I7lMaAn9RCQSjxwyN06rBrkT41eNJHRfxZfC4nprqZLjDfiVb5RY2gMZmBuGhwycEcd-9JHIuiKfPFbPPwanSyh35XrVDLvlWFFt2OtQVcUw--5nl-2URuWM_3oIbTHNpyWfFPYSFXKP2e5j5bQXytK5WsdR7sho6Xl-cBCVfGixfUnGNKhqVG8GTN4Eo1a5hgv3EA_B_KOoFvxk7RINWl9PLafe2RwrZrpSR1bzM0nzOGv7doJbtzOywqaVYGbKtzlVrrm17uT9IRkrTSwmX_Vjid2294M4C8uhXHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_-VrcKSujupXiswUaZwnEybL8WuYm8jQsOS6i5L0A2KqwvqQoqJ79pmjahIFp389ArXr0jR0ggtxj8FA9NrBkqJfauiQQilpn2ztlC-GULiqJ21xYPMR3_s7mrAkBOchJ3PKhdXCNQeB2NqI_mJfhHWtk0egJ8nDsKi663F65EQ2Hwmd5KPz4vTIRflsmAcpO-qMF945fwHYOGyOxjee-R1CZz3x55AXZxfyA0nxha4a7EZZH12HJia5rZpXnoMoAf6TNKX85EfxxdQo1ol8Kbtabfh4Od9I-9htlWXDrqdwjUzPEAGG9JSJSJBJtl0okYhmwTXfRKKBsVytIdg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/beYpk-sEb4DaVNiZ-35dPwwiRVg58zDMCdldNqUkyJ1Vk5JNal4QJAFx__FMH-JXOSgRSn1G4gz1FcVkKRjhVRrhvEEuBDtNLdr_dWC5s5WZHy_IBpwXWLbvBKsoEtoe6pb8c5xLvTg7xT51m6VZuiWqA8osHupuh3rYmkhzaXK-hRwd3UIAYB5OasBQu8BB_Nr615Oweokv0WnhDrWyVvKo0bXmSmnb6ujcHr3ko6Oxy4aDTz14jHMkV3lmBwDZA2OGisMiyV154lH9Uy3IhueBXlbw4LPXH-64X82yptj3admqMTurT-eqiBmzWoQhCo85JZ_qXfIpy_CyI1-jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=rni9Odt5jVZUrDHrApM3Bx25fUl0rcib89vY9z6BNWInrM3hzOh0m-6XoSo6uD0Du4y_Rn2vO3aj57M795LN6LI5A7jDMIfibawmUcQ5y6wpZMQv1ybJRC6gqyeTVHh4hwtZLjN001DAYApEflesNgMDN7HWRKlL_gbANz9NKVeSUm0f0WTLqgJXBm9VfmuFldvlcYXGVoRrKw-x_c5AGzlOTqhZp50CfOyqMWSVZ1zOBqbX56iTUYRXityecGcLljX-ESjB_7m26o_ACBrm_EsPZe9v2GEzhhm2jzyTuYCpP0yHc6AIIfFbIj8btFpJuo2tdq89In78w4BQa56520BAk4XSDXQkq9RwEEMqS0W_sXdZw0GUBYc8-biN1Bft06rh2MewXt72JJciAjPGDZ3eCN_GeW0fw248wRlXEVjnQUujuKfApOkewOspUu-EjCDWtlZC1Fg2xqa-hKcxy_Lt8syeLFlB0IPSYgRzdc-kAUalo5RKqyiSjuL9YT2EOkTgARXj6ddqFtFb8jqpGEOzAdQMR6b1akYitZvzc09r69oTpKLZ_4ayjvw1L09KqP-WsBFD1ueQAbOyGVAFskvmh085c5Wt5_ZR0kLlC83eSAWxcNM5ias6jblQgjgS-RJj105LOfvkSWuU_HAbfUb4c7u9vS2eTzT299SETwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=rni9Odt5jVZUrDHrApM3Bx25fUl0rcib89vY9z6BNWInrM3hzOh0m-6XoSo6uD0Du4y_Rn2vO3aj57M795LN6LI5A7jDMIfibawmUcQ5y6wpZMQv1ybJRC6gqyeTVHh4hwtZLjN001DAYApEflesNgMDN7HWRKlL_gbANz9NKVeSUm0f0WTLqgJXBm9VfmuFldvlcYXGVoRrKw-x_c5AGzlOTqhZp50CfOyqMWSVZ1zOBqbX56iTUYRXityecGcLljX-ESjB_7m26o_ACBrm_EsPZe9v2GEzhhm2jzyTuYCpP0yHc6AIIfFbIj8btFpJuo2tdq89In78w4BQa56520BAk4XSDXQkq9RwEEMqS0W_sXdZw0GUBYc8-biN1Bft06rh2MewXt72JJciAjPGDZ3eCN_GeW0fw248wRlXEVjnQUujuKfApOkewOspUu-EjCDWtlZC1Fg2xqa-hKcxy_Lt8syeLFlB0IPSYgRzdc-kAUalo5RKqyiSjuL9YT2EOkTgARXj6ddqFtFb8jqpGEOzAdQMR6b1akYitZvzc09r69oTpKLZ_4ayjvw1L09KqP-WsBFD1ueQAbOyGVAFskvmh085c5Wt5_ZR0kLlC83eSAWxcNM5ias6jblQgjgS-RJj105LOfvkSWuU_HAbfUb4c7u9vS2eTzT299SETwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBnW-bNMkqXa1JKZrvlyrBHfhlFf_0s8M-sFtLyzl3xfMGaRYsvea53kh1aZLwEfBEPlBvM1CCEWjTMz_ucr8fAaCqH9yBvChHY26oJDHoHUJdtonYOQf0KahGyibxhr46tCPt823icxEmZGHrymRPDhTk1P3danQCgm_axmTuOGGtROsJ2XTu7r1mjH-DUVjZL4MajMkB0N7STqpVOpNxn7HlBjYbYEbMbnTa50RwBJV_Bi_sLjN47PmR-WZxj6d1mHQ6im6JFHFVBrGOOPmM-QHw4KR-jHH9cUaxCK4qeesiZpV7eBBWBeK9TgKsUs3FSqBO_I7uwRk99pdKiuvoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBnW-bNMkqXa1JKZrvlyrBHfhlFf_0s8M-sFtLyzl3xfMGaRYsvea53kh1aZLwEfBEPlBvM1CCEWjTMz_ucr8fAaCqH9yBvChHY26oJDHoHUJdtonYOQf0KahGyibxhr46tCPt823icxEmZGHrymRPDhTk1P3danQCgm_axmTuOGGtROsJ2XTu7r1mjH-DUVjZL4MajMkB0N7STqpVOpNxn7HlBjYbYEbMbnTa50RwBJV_Bi_sLjN47PmR-WZxj6d1mHQ6im6JFHFVBrGOOPmM-QHw4KR-jHH9cUaxCK4qeesiZpV7eBBWBeK9TgKsUs3FSqBO_I7uwRk99pdKiuvoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sm8ToTOJq7XJtP5AA5xKzcg_A1zkYkG1AnJzxlOLkH70x_V--ODZvYCc-aZpKJSOyfHU6JoCmRoqxXGu9-5rBzbYNDtCPpYLazYIuxYS_GWXFSebTTVoXgbYz35Pye2_1CjGFIEd6uiuddaE1BRFGHF2AKTNDPfHm2M8ai69g_i14xCEDz-zB_sqF02kp2Y1lpK0DkNd5VXWVz-XLFcko0sYfF7wQXqsVCttOkh1Kn2guG7R5QOoSWNandinrwkieUbqT8xIG0PWxppdn_Xo3_RsiTnL4j_CMPmSDzN12vFaJX2_0detECM4DJLDbigLapuikUn7sBWWe_07yhuK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WieIhg0tOtwIWuzu_U4QfGVBi4EKArDyL7f5ecOh74DoDbpwX4tZLdnJ0pWb3m8IK6ETL4VTbHUYrBbEufcw2jeuMqB65b8Flkcqgd0rqB5Ykuce-D9nXZPnUM9ASiXP05zKu-hf0zB9PVpo_HTYy_7IYzk_dW5RX7gWk24pgFt7nV3tPNniQWDn-Koxn0FYmsAsAnEMVtsxx0gafQGug1KkpDFjJGzyAg7clW0XS8ZfigTerbKi6s4mk8a9Xm9aDuUjSSf-HeYhhDqvJ-t9hrbRfqLU1VBU7WJNMt0blZexmrUdEj8aslc-9wq-8Wmc7QpyIXf9AASYwzR6dZMPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=rREP8VWKaoj8wi4O9yKWxVy3eAKpWA67zktsSjWbkEkVMOejQec1maOovfkYGtLb3zERxa7Z_CQqxhhJiEybQoaYoiXDJMBu-3BhxFMybcIG_wEOs0_hEc1CkFTAxXljQ8rlAr005JnaggIZduWtvC2GyPTXdOPItGBY9aDQnwmD1M58xwVuwk2GIzzo5BLlzvoq474MabGrqjC-TWIrQ7WDR-Bim3UjTyKsOqqK5_v-QSoLftclYP5vG7USQb0Vf5FcM6zsXCnNu-xfU8-N6pfYmJloEHV1z7Yop1xVsjDftghEa99U_C2g0yHOPanIu0lWifjJHOdNpqIehkvgpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=rREP8VWKaoj8wi4O9yKWxVy3eAKpWA67zktsSjWbkEkVMOejQec1maOovfkYGtLb3zERxa7Z_CQqxhhJiEybQoaYoiXDJMBu-3BhxFMybcIG_wEOs0_hEc1CkFTAxXljQ8rlAr005JnaggIZduWtvC2GyPTXdOPItGBY9aDQnwmD1M58xwVuwk2GIzzo5BLlzvoq474MabGrqjC-TWIrQ7WDR-Bim3UjTyKsOqqK5_v-QSoLftclYP5vG7USQb0Vf5FcM6zsXCnNu-xfU8-N6pfYmJloEHV1z7Yop1xVsjDftghEa99U_C2g0yHOPanIu0lWifjJHOdNpqIehkvgpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZOH19acWsjl5hCcgyI88qpUFySWzfn-S1d1vQJ4jYkuM4XpuqZu_-mK2flJWaRFgp70ypDB-1x1ih8k5Io4y-1q3k_aSN1g_k6-aJmQL4VR__dHEhU5dl5zlADbpEDFUH5wf11WSyqU-mtJrqmO4kwsYjNt_1UFtKyJKq-vhIVRAcGPbd8HetxGypDhCBJ_SgMp2X46BTC-AQ1zsSHvLPJBr7qwh55geN-m4B3u5dCfpXajjGfWOMqXKfPxqbXb8fPx_KAmZNC8ibwCsR63COYDuFeO7LMrn5BiBLlH09-GzehPUQg5rZx7nt-fUUtpIFJ5upmA7ExrTKvtQZv6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfhpVhWwgE96QSfTlyzAQWf57w_Bv8gbVvz557I1Cg3DDrQX45P79BJ3HxnTrEYmmgU-omJdMAOSUhvu8lMVp65aXhID1EN9117iOd9a70eCqZBk4neM1e1E9aUy7cWiBS8-N9TGNkaPfBucQ-9wegfDMlpLcXrhssTEv0aiz7w1XPeMGNzF0lx5svreAiPQO9gYpu4ncaDiCNVVqIfxnqktp_Dxr_3O1cS5T4q1tf-0aVER7XiA0826YlzxB63AtVcMi4EH8ht_sgcFBcVWUDMviLiXrgPzpj9CFHtVV9vQ7w4Mu5uRlONqmLNxWeCIyA6i5zLhtYQEG7KM0TSlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqexXeeJaRiXZ1jDw6W1XqYFfJ_P661bjrKJlHBWTbtAkSzLtXE2Ed8yDhdxwROGXMNYRQu-S3AIizbi_WvCltxadaT7GHX19rSEFW2EERO_zDrI5gzP36azhWH12tlAP8SajSKS0Ll3Md9taO7ZZwIraVMbhZO4DqD84prhEna0SwH9DpzO9cyo-CIDRLJJbykihiSGOgoCpsPR97KKT7b-6s9q0NkcGfkAV5P3bYfvSP8XGYomB7qMV4S2BWLgMBjSHa-LjcBc46S6wqk_IVgz7QxeYUik-HvtPyX-yJyZT950yzfy_7Vf-691zXZcOmjcOqBmW2msL5jvKOM7HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbq9bCdg6xiWpddWnP-vQxS_m9wI29vjH1crEkoz7tJUngs4rrnVkVgy2Zqbl4sk7h5ZtXupPfzEb-_XgyGPOt5bmfOQZ2-i-CVBYuBwDq26b2ZAlXoVdHEidmDTk5kF6Y6FgTXAdkUA0-gkLltx7K8teF0XhDbq47Qx8lC01QswuUd_gG15S-pl1rcDEDaSKLps-zrbCzB2NhjrpXx0QqhfnnT7YbEyYvNot4ggXzveElYB_0Pqw2Ay9x1cZK5LJ38IMuf4qK_Nsw00NWoVR1jfn9dAbqIAIzkz4I35AOMuG7NEVFm0MRUECuM4zRjNplYvcBW0qQZihlau4JNiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2jNxVYHBc8fYL0JRWPA9QNgfAyWLJg8flUUQqQgY_hP9i9EDRfcFA7uisfjzdDR8lp31HK0IzatqyPBOI5TfM2KgqPMqSyRaleovl0MX27RSTs-lYuS200WGRf8Bqpg36G5UD-M06ionkZPnKmHf-AmRpRH_eRECrBgzoNVftIM8soVB7HwfbnuRamis22DmFbVzqk2Z3kZogIqMnBzEIrWarOv0hLT-dJx-4TcoO6uBErr_JlfcHOZwJhQeiqbPow5ibQ7lq6KB1k1F_hVmXRvzdij0D41YEIKTraIoDfjNIZwJFI_HWL5AexUb2T_yypa3HgvszyOEj8kcFkbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=QwRDC6y7ckmeUEE-PdZMZD5EOPRV7LlsO7OvBQtnwEV7WFTOcBK_-4ca1v0tTkieMc61qU6wYsTj6eESM5NM0UhKH91nxL9mknqoMKKTFQkhLqg5KATptkUp26HhcsDwhlWct84BKE-IcCE2EhSZdhjyvGKiJq4J05qbb8AGXx93ZlNItPk4MvA34bspP0Zb1Ieho5i8crMfiRBxBMZDoF-MVC5_9YdV8jgzCH1BADEoznRIsDIlpQuj3wwjQODc4CsJAL4tpMVYjnB4fww47NdAW3BITzt9X6Yzkx9hweOH5jCvX2Rv9u9QAjj7xr-As1cuTetE-BW_ls6yAebEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=QwRDC6y7ckmeUEE-PdZMZD5EOPRV7LlsO7OvBQtnwEV7WFTOcBK_-4ca1v0tTkieMc61qU6wYsTj6eESM5NM0UhKH91nxL9mknqoMKKTFQkhLqg5KATptkUp26HhcsDwhlWct84BKE-IcCE2EhSZdhjyvGKiJq4J05qbb8AGXx93ZlNItPk4MvA34bspP0Zb1Ieho5i8crMfiRBxBMZDoF-MVC5_9YdV8jgzCH1BADEoznRIsDIlpQuj3wwjQODc4CsJAL4tpMVYjnB4fww47NdAW3BITzt9X6Yzkx9hweOH5jCvX2Rv9u9QAjj7xr-As1cuTetE-BW_ls6yAebEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=qVzD5T9XETC_CefLwqQOU0lBDGpGUoqThHK22rViSzU7suMf_QciikVEd13P41z_327WQ1o-p_1oq-8asgZiqMlvZJpNJ8Ndgw8mjac2bryTOp9yoTnlkSS0aQt5IbrjfwDdaUB8UbE3WlLVDmvlhZldDlQgPKcURMnNRgPEsfAzTjQleyX0KJncgkNI06uYIf6ig_capI2su9DyBirMUn-a-o_oClFiQzvKTQoi50pZKLWQBSOAstQPdyqs9YbRh9eT09EjEV-yqmqVMk-eO7FkBdhhrIWKzGsYLybbKtCqLfv5h8Zdj0v4pmRZ6aIPjg07mX8eo0VerRfunGkERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=qVzD5T9XETC_CefLwqQOU0lBDGpGUoqThHK22rViSzU7suMf_QciikVEd13P41z_327WQ1o-p_1oq-8asgZiqMlvZJpNJ8Ndgw8mjac2bryTOp9yoTnlkSS0aQt5IbrjfwDdaUB8UbE3WlLVDmvlhZldDlQgPKcURMnNRgPEsfAzTjQleyX0KJncgkNI06uYIf6ig_capI2su9DyBirMUn-a-o_oClFiQzvKTQoi50pZKLWQBSOAstQPdyqs9YbRh9eT09EjEV-yqmqVMk-eO7FkBdhhrIWKzGsYLybbKtCqLfv5h8Zdj0v4pmRZ6aIPjg07mX8eo0VerRfunGkERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xseuzh2gGq8r3RkNDWYA7Yn-epsykuFwG_16M4gk0y6f8nz1yVhXRSDS0ld4Y_2S0U_4Pe6F4vbd1mV7Jpmzzabcv5TSakeaaOV_H8K8uYQrRAggm6uHsiFqE9GSuU8-hk7AmTF3NbBfCEJsvFzRVZs6EUCQ5WIvtm2-qmMr7Kelg0k_01Dm5y4ZfNqLNEDM-4qXojHjpCz6Gzx5coZmPiK5EiMAwQgi_AGHlMzQde-3fcKZurEw6xKyjWqbTzPGma8c7S4UiXtv6WEoKsPARSTFt3e5LY1tnngmfNu9VNk5z1GZSp5ovozyDS8QIGvvur3mkurPN5EF62XXwyCm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=nL878o0Mljqk5eP1UIoZNCAgPIrJAdiEff88LeAakXGKi_zUXhJbjbhRnbf3uL0s3LHWWCVVWTzSVr-b7iqgZjZf2qxHSIrrlq6BKYmCUk2kBHhJ1RDInfmqRvaqmVh4nHb04BeiO69M8pGFTUqlfwW8rPXfYyxddC3em4yFVKFOMqyHYKxbY2nMBKxVLjlJREC0qX6c9_Ec2j4LkY58fqNqRHR2N4BAGaE8RwHuBEi5cgZ93KkdM9L3KGxFmGUDJPXDnzGAS1Eqdbi__036mJxP36uwCq-FfG2vIqRdUTnpEiWf9ao5WuG0I004chwvIpqlvPL5S7LktK7nJbdd-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=nL878o0Mljqk5eP1UIoZNCAgPIrJAdiEff88LeAakXGKi_zUXhJbjbhRnbf3uL0s3LHWWCVVWTzSVr-b7iqgZjZf2qxHSIrrlq6BKYmCUk2kBHhJ1RDInfmqRvaqmVh4nHb04BeiO69M8pGFTUqlfwW8rPXfYyxddC3em4yFVKFOMqyHYKxbY2nMBKxVLjlJREC0qX6c9_Ec2j4LkY58fqNqRHR2N4BAGaE8RwHuBEi5cgZ93KkdM9L3KGxFmGUDJPXDnzGAS1Eqdbi__036mJxP36uwCq-FfG2vIqRdUTnpEiWf9ao5WuG0I004chwvIpqlvPL5S7LktK7nJbdd-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dalage pezeshkian 2.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbH8WHMXdmdwdNGytd2RpDClbr_3e_yKcMhCCMDjUoM2r1yPTqSYnxSfxZry0y85s-pJWtZVWrgwvz28WXUmtB0PIyKA0BRclEwuFfDE3m8jtyrrNLU83VfG30j3TY4G0kM9APprLGh0PSx5l0xwpjWuMs2-IcZcuFcRQG7Q6kSnvOf_MKl5AKlkgHH5ZAggRkODxtCpNDw58KldBR050FS5Wm0MHak-V1kaTORj-1VlReUNzlTrTbn3bsHDbMtN5VkcDqUkzIlDp03TVCg66huKb2CwKVNAlYHPFGioc-tejjzVTbXviy5d0kHeswL1JGd21ywnVOL0H_jHK_38ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
جهت اطلاع رسانی مجدد همچنان در تلاشم، که مشکل دیتاسنتر خارجمون رو برطرف کنم برای سرویس سرورای تلگرام، درحال حاضر همچنان فروش سرورای تلگرام از دیروز تو ربات غیرفعال شده، نگران نباشید برطرف خواهد شد
✔️
فعلا درحال حاضر سرویس های تانل با بهترین کیفیت و سرعت ، تنها سرویسمون که روی تمامی اپلیکیشن های
🎥
📸
✈️
💬
📞
🤖
🕹
📱
🔍
قابل استفاده میباشد و برای تمامی دیوایس ها واپلیکیشن ها اوکی هست، در پلن های (1 گیگ، 2 گیگ،3 گیگ و 5 گیگ) تو ربات موجود میباشد برای ثبت سفارش
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اختلال شدید در اینترنت داخلی
🔵
متاسفانه از دقایق گذشته اختلال بسیار شدیدی در اینترنت ملی ایران رخ داده به طوری که cdn آروان ؛ سیستم شاپرک ؛ سیستم همراه بانک برخی از بانک ها همچون بلو(سامان) و... قطع شدند یا دچار اختلال شدند.
🔵
بسیاری از سایت های ملی و داخلی نیز باز نمیشوند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8299" target="_blank">📅 00:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8295">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8295" target="_blank">📅 00:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8294">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbdq4QB-Z9QYZOmU-y8XGEBH_IhT9rvG-X3GVxSBTWcFQnDHkAa4GLWmkQv_xAObMObSEGcJy6S1MFoxbAiahCgr97xiRbLft3etl6CeJd1WnmESTAEE4AeG3MA8iiZzoXS6YX-TLC2dXrMjmWhkBd7NgPgabG-kNUHxwoVwlx-Pw8nSQZIoKtEalfsErJawGDO7aFmEgXQwYkW_XBoGJPpMMl7f_PSHURPSyZiX9iQ2BkxpIq7XhmqZcIvPbU8lBDt8T5AppqPSDqK6ClzZdE0eqYLOzk7jmmbg61Xq_fzmIDKwqbwoVZOBrE7MPnuB89Z0w0t8IZiIOZK30PMb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8294" target="_blank">📅 23:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8293" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=tEbYPHEWn5ofMxNd7UiKJv5hFHGzvpy1Tig3WBdO2lhF8K2i0HrFMC16XU5DHX-iYMa2EnQJ_YlO6XYOcRFnwy0X1HO728SYLBC6xlM7kQkF2hxNSxLgRiOi8zJSRDIiZAA1doKn7Bt5Ed9RIXnvJ1vwdMPRFgEWHHDPMOAhCVxS0C2ktg9QMJFY8QjF7R8nLj2FADr1gpNyt511uvRdQTsTEuh-HUch1pcWeqVWIlDKzJBz8Sw9f6hzuH-pTYO-OVcV9EbvEJQucRdO20IEvYi04RjN0qM1m3QrBS9UDT9S2SMN0MDKc7iP9sMFb7eiAUYfa3--HA7ZRMi1yMfAdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=tEbYPHEWn5ofMxNd7UiKJv5hFHGzvpy1Tig3WBdO2lhF8K2i0HrFMC16XU5DHX-iYMa2EnQJ_YlO6XYOcRFnwy0X1HO728SYLBC6xlM7kQkF2hxNSxLgRiOi8zJSRDIiZAA1doKn7Bt5Ed9RIXnvJ1vwdMPRFgEWHHDPMOAhCVxS0C2ktg9QMJFY8QjF7R8nLj2FADr1gpNyt511uvRdQTsTEuh-HUch1pcWeqVWIlDKzJBz8Sw9f6hzuH-pTYO-OVcV9EbvEJQucRdO20IEvYi04RjN0qM1m3QrBS9UDT9S2SMN0MDKc7iP9sMFb7eiAUYfa3--HA7ZRMi1yMfAdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی و فرماندهای سپاه:
@
RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8292" target="_blank">📅 23:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9y6_CCq-qULIOpTHsqGzVwOJDfKHugwDNZzz2VwHVezqrJrRe8kdLH6fiUPWIjCX803MHxdp9t2_-GRyfHsjYxsVjh41M-D0m-crklQmRBESPC_Pv9Zy0CnGdjqhPD66pvqZc5tZo2a1-4sU9FFTyTZZGpKCi_UoF0KhSzKQdYaUQaJPv8vO3v4jwMErQvhglJjyQ1v7px0TfmBO7vNfaFpxbVfNIKHbRSwa0jxbFIqDzo1ImxG8DucRJwwHL_sKVarqtxMtFwkjnq0fw8Hnj2dYWZRvchmwcu4p-SF0GjDL7SA_GUmykNl3C0uOLRQ2LuxttDxLBn-jSCL6hCY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)  و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.   او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8291" target="_blank">📅 21:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8290">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Own_xLecw41DcTVJUZUdKqkS1ITZ6RRe1zLlc9SmJ01QZrLBiM79xbrpTll-o-G8glz5ZiC_m7MXk5YRPwyERrf-9mqTHzyjIMivFOnj7eb3II3h7nZLgu22E3WaLy899K0cFcGVhmD5Ira4eJOICSoAebWZKG8X8Y5GpnHftK_z3hiKX_nn1o8wPjvzGp7CWQDerEJatUoFv0hTiNDO8RBRaZYr2C80AdWIvZIuhFsO4-iwV0KImIxLp5QPj_pmM8ddnOTNpCUeA6jQVwdTAXWZFljap2aWVEBCH6_vNCbTcDzh8SWx0szNnVDgJUuZMcZO1bLPlf8hohOzt0TJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)
و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.
او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت جدید و بسیار قدرتمند برای زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد.
هر بانکی در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور آمریکایی ضعیف و احمق. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
به مدت ۴۷ سال ایرانی‌ها ما را «گول زده‌اند»، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8290" target="_blank">📅 21:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8289">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✈️
جدیدترین آپدیتِ تلگرام
🌐
[ ورژن : 12.7.2 ]
- لینکِ دانلودِ داخلی ( بدونِ فیلتر ) :
✉️
Telegram ( Direct ) [ v 12.7.0 ] :
https://uploadgirl.ir/d/c99c188e-57fe-469c-91ce-843a37e803f3
📌
خیلی مهم : فایلِ آپدیتِ نسخه ی Direct هست و در صورتی که نسخه ی Direct رو نصب دارید دانلود و نصب کنید ،
+ فایلِ نصبی داخلِ یه فایلِ Zip هست که باید استخراج کنید و سپس نصب کنید .
+ اعتبارِ لینکِ دانلود : 3 روز [ لینک آپدیت می‌شود . ]
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8289" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8288">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8288" target="_blank">📅 20:02 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8287">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_ypqdplDcZ_gKbl4D2zsavo6jRIFAPfOnKLgMS1gwBynfyX4NFUiQ70mqIo0MTNPkfqtN4FZuO2UBR4qG89SxSLomhKTf2RNgUPKEz2aOlIRv3c4WbK-40QLzUr-kc7oOw8ijIgbfarH6wYqBr4Kqo2RRwiabHJl6eAEEinFnk7a9RA7lMHq8ghZaGORiwaMXKpWBYf8RaUfsFL9r_K0UnAXaiSaB6ooHuacYeU8oz5r8od6-cTrZp566yy6y1-7L7N5JYuOW9DlptZf5Gq7OPJfpDQEOJ2ea6zHFst1-YYXY34UCUl8dwd2XII9lsrsu9iodQBLQeMUHVsL4AihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/IranProxyV2/8287" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOwOwF653nodbS6pqBHiKan23tMldnmwQCcKp1KyUuW-xF2StSfwvDtmK9o1N7uxGZxFnW6t4v-QPi9eLdW8kBdEc4i284wX5pm0_YMacr02Y8iLEN8YGnKX5wBYLALTcTakcXy5hDzoUPDv8vJPICWJQpoq6rdBqsSSfYlcivn74BmZkpNSoBRUZkWRAFBSym9yY5Lcka2c4TRzZ70BbPnbxdV3a1skjVtJoOsTpo9x_O4o58hMrC35N8tdGb6zBubqnQA16Z0gxEBtiS7evnD8ONqsoxsYyzfJYWTXEZpHBFgToBSfwi7KouGJD_GzTaqA_VEoDs8zrDn5UXf1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رییس کمیسیون انرژی اتاق بازرگانی:
سال گذشته هر هفته ۳ تا ۴ روز خاموشی ۲ ساعته داشتیم ولی امسال تمامی روزهای هفته ۲ ساعت قطعی برق خانگی، تجاری و اداری داریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8285" target="_blank">📅 13:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید
@RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8284" target="_blank">📅 12:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کامنت هارو باز میکنم پست بعد حرف نزنید فقط نتیجه رو بنویسد به نفع کیه
از اونجایی که خودم بارساییم 3.1 به نفع بارسا میشه</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8283" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه چالش میزاریم هر کس اولین نفر نتیجه امروز الکلاسیکو رو درست بگه بعد بازی جایزه میدیم</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8282" target="_blank">📅 12:24 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
