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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 11:55:20</div>
<hr>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQq1eKHfXOzmfXc3_QtlxaZTdB0gE3v7j5WNtXCfffCL4D-OiqV-KSHEhyjFZNPfyqLIKYj6YOKS8dF7tWskqqW7_M-_yaY0g7gEQ1AEJZhZ5UdtxSZrWuucZYUCXZv5k8OH1NeK_6lRaV0S58UejqfCYGSrAgxJwLAacdIj3gwh8Du64xmMoH29UUpSuSDYcMXVQwo-Ognj7iJ8xxZ7xh8Wy-uxakVNySKphRz22mGVGkiDjNScDl0kihsHWk3UJYHD-owL791I8A1QsJarXlN_6yUAmtr58bIrP-RTCiQSga4EAfxYUHe17lwy5b6Z66IUy2K5cwGaRQti3bCdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3rPlQcaPtPh8U4_ICqlXV44a-Fzuh1Yny4rIq5WJSuMK9d_XN65XBxA5xIC6UgRppWgqHPqmdw3fH31632N8TerC3kJvMtLBeBmEWzqW8fayeBqo-foEYhigZ-uoctJ5hekQ8X_icVinxPQQiLrqQXqYbZhDneR0aiQ7zMhVYdoB2Xqe7vSYLiNoMTzX2vIjM8OHjLTBWNX7gK1jH_L-ckPJl-b-RlcKG5OqcVQVoYUqbbSjyGi-UNE1noqOiao87-HzUO9wbgMp6X3JLMrURINjjz8mFgh4JTn_Ysy645N2pCpgQupH674P8dcTmfzbAZDs7pi4Z21QP8ZH-UEvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8391">
<div class="tg-post-header">📌 پیام #87</div>
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
برای ثبت…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/IranProxyV2/8391" target="_blank">📅 14:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JYES9QLXFNskB4tWVxChLoSreMbr7xgmBKe8HIpRkN9__R5ii1m7HD5HUZDTPZQ6j8TxemdW5SLegkcrsABmChmH1U1SQ_HveXXQBWvhoUxoseRtBk4YX-h4-Pzgpx4ZRRZG5q5K7hJ8_KJ_48jQaMLg39omVRINNKW8KXueCXpyH9jF-okXSkktXBSaB2NUEFyJ-z4EsEJms9Ig95JHmAadqBt1iOe0jhJTG_TyIxogVYKxWO9Pvn7Sg6DRzF63KwjaradK6wo6-oDMDzlQjJ7y5RfsUYJXSMsuy2A8sGtsEQlMzo7Mny4b5swyYQSpSEWRn7aRDcHNCEqh58YC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=JYES9QLXFNskB4tWVxChLoSreMbr7xgmBKe8HIpRkN9__R5ii1m7HD5HUZDTPZQ6j8TxemdW5SLegkcrsABmChmH1U1SQ_HveXXQBWvhoUxoseRtBk4YX-h4-Pzgpx4ZRRZG5q5K7hJ8_KJ_48jQaMLg39omVRINNKW8KXueCXpyH9jF-okXSkktXBSaB2NUEFyJ-z4EsEJms9Ig95JHmAadqBt1iOe0jhJTG_TyIxogVYKxWO9Pvn7Sg6DRzF63KwjaradK6wo6-oDMDzlQjJ7y5RfsUYJXSMsuy2A8sGtsEQlMzo7Mny4b5swyYQSpSEWRn7aRDcHNCEqh58YC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=KtrAvclS45jr6fdO28MYv5f5Inrp77u3Q4VZOfV2wdM58RSG_AAzc0P90x-ZpOzXaLDjHpcRB9_UyaHwdb_QINaZwt7ZSaGtKapQDcuZ2bUeH1zwgko4M5TxBp3isehyWVx18ZKVuP1ivOGbf_8dhVH168dN1L42KhUEgR5Y78cfLB0syRlxbYlK8M5rYcSvOlApEk7fgTAk28kGDAdnYbaRy8DpigQwI6Dln8qJFBZeXuy0a1MeWc2NRlDUG1hYoqkOZ2TGbGgstYmnGfmKPU2FVrLeMtwX6fCoQQWzfXG0HJhkYKeKUFCmkk1WhpNzo4itqVYKZkmolczqOd24JU4Gl5l7OQWchJH81FPplPjHnw83TJnHiwj4QZxj52_yjy6gW_bAM026Ot2boFpr76P_l5PJd4Yvt15QFMXQI-kjVG5I6VqaiJTk_zG80uOWrU5HWSchkJXEYXqeE5-qGePAa2-qKEwfgdp2VkANbiaL6tqY8SBkeYSekYzY4D9tvXoBPE0A_6jR1J8s9lkKVyOFI9733UaGt1BzNFEGHkd_mJb8gdEahKBx6XgMyHUFCBGhJujRz0yYls-AIWMPPGoR1AeGiFmnWnKbx_YO5Ldmf77G2XA63TFFJ38M5Rh3qvRvpUM1lpiKfx54S-nkDI6lg5o_ASUoTnqoHFIZb7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=KtrAvclS45jr6fdO28MYv5f5Inrp77u3Q4VZOfV2wdM58RSG_AAzc0P90x-ZpOzXaLDjHpcRB9_UyaHwdb_QINaZwt7ZSaGtKapQDcuZ2bUeH1zwgko4M5TxBp3isehyWVx18ZKVuP1ivOGbf_8dhVH168dN1L42KhUEgR5Y78cfLB0syRlxbYlK8M5rYcSvOlApEk7fgTAk28kGDAdnYbaRy8DpigQwI6Dln8qJFBZeXuy0a1MeWc2NRlDUG1hYoqkOZ2TGbGgstYmnGfmKPU2FVrLeMtwX6fCoQQWzfXG0HJhkYKeKUFCmkk1WhpNzo4itqVYKZkmolczqOd24JU4Gl5l7OQWchJH81FPplPjHnw83TJnHiwj4QZxj52_yjy6gW_bAM026Ot2boFpr76P_l5PJd4Yvt15QFMXQI-kjVG5I6VqaiJTk_zG80uOWrU5HWSchkJXEYXqeE5-qGePAa2-qKEwfgdp2VkANbiaL6tqY8SBkeYSekYzY4D9tvXoBPE0A_6jR1J8s9lkKVyOFI9733UaGt1BzNFEGHkd_mJb8gdEahKBx6XgMyHUFCBGhJujRz0yYls-AIWMPPGoR1AeGiFmnWnKbx_YO5Ldmf77G2XA63TFFJ38M5Rh3qvRvpUM1lpiKfx54S-nkDI6lg5o_ASUoTnqoHFIZb7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8385">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که در شرایط جنگی از ما سرور پروکسی تهیه کرده بودند، الان میتونن بصورت ازادانه برای همه پلتفورم ها بدونه مشکل استفاده کنند، مشکلتون برطرف کردم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/IranProxyV2/8385" target="_blank">📅 03:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_-VrcKSujupXiswUaZwnEybL8WuYm8jQsOS6i5L0A2KqwvqQoqJ79pmjahIFp389ArXr0jR0ggtxj8FA9NrBkqJfauiQQilpn2ztlC-GULiqJ21xYPMR3_s7mrAkBOchJ3PKhdXCNQeB2NqI_mJfhHWtk0egJ8nDsKi663F65EQ2Hwmd5KPz4vTIRflsmAcpO-qMF945fwHYOGyOxjee-R1CZz3x55AXZxfyA0nxha4a7EZZH12HJia5rZpXnoMoAf6TNKX85EfxxdQo1ol8Kbtabfh4Od9I-9htlWXDrqdwjUzPEAGG9JSJSJBJtl0okYhmwTXfRKKBsVytIdg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم سفارشات خیلی بالاس عشقا اگه با تاخیر تایید میکنم به بزرگی خودتون ببخشید، الان همرو اوکی میکنم میام چالشو براتون برگزار میکنم
😘</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حجم سفارشات خیلی بالاس عشقا اگه با تاخیر تایید میکنم به بزرگی خودتون ببخشید، الان همرو اوکی میکنم میام چالشو براتون برگزار میکنم
😘</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8375" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZ2BBAqhVlqUoDs2yfwXe5CFQw7t9S0ZXutjq399cPPg1zB5P5XEARMN3Ze9RG3MvvEB5IfbouLHr4OtMN1XTrawAiI-xX_tdV0OL4Jcf0hkUaQiBjpLkG7dXuguCCvjBAWkdKvMwTAURvaibnSU7YT8uxdEs9o_T_3ONXdOQaVeH2J0CK9WPQeWlUQtGRVONkAke5JSvtRd0frefIybcQuw2n4l5cQFk4KOnlx-f0m9IfdnXvI3A2sWX2NBZRlT4XZ5eJHHi8lmB8s9UVuOq7CRb9-SHCo5J1AdC8d4YXXKzAw5aWw58nQ38f8kc8w2puV1ksZ2YA9RzTIkONWVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8370">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بشدت، بشدت حجم سفارشات بالاس،صبور کنید دارم یکی یکی صحت سنجی میکنم و تایید میکنم قلبا
❤️</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/IranProxyV2/8370" target="_blank">📅 00:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBo0b2MYLTvK1DH-EPBsmO9junBE_aPBvQQxYN__rKpSznUlMaXibRpO8Ih8bHDvMyuwxND4hjs3RSrditK-vHSthXOjeOajYwak6H4dabdY27g6yylqLBIEF83xuTApNP-eQ3Nk-mxofK4sfEAcsLUI2WlGUw9kdHD4a86Hdza5DeqfLa0oS8_tMrTZdkdnqcy4mTDzNcJZ2oonTgEio1ZbNleN57GvksWKllZtABfsTcmy1Pu9MzFz6GShNXFx-04xo2FCpuGKqukil-nHP74tGYIb6BDXAYD5jbPCWiU4PHFhT2TYNgEyL_GrLpjWo45IvIAqVa0vWnotjA9XdsiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBo0b2MYLTvK1DH-EPBsmO9junBE_aPBvQQxYN__rKpSznUlMaXibRpO8Ih8bHDvMyuwxND4hjs3RSrditK-vHSthXOjeOajYwak6H4dabdY27g6yylqLBIEF83xuTApNP-eQ3Nk-mxofK4sfEAcsLUI2WlGUw9kdHD4a86Hdza5DeqfLa0oS8_tMrTZdkdnqcy4mTDzNcJZ2oonTgEio1ZbNleN57GvksWKllZtABfsTcmy1Pu9MzFz6GShNXFx-04xo2FCpuGKqukil-nHP74tGYIb6BDXAYD5jbPCWiU4PHFhT2TYNgEyL_GrLpjWo45IvIAqVa0vWnotjA9XdsiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYno3fTGxvw4_g8-c0ZWw1ACf6uq0DTcFtFpGiEYtHGCch87VT4LHu3ah7M1XjLfpZhOlnVy6-2RstXL7mH40ArGEEeB7iAiYVQWize9ZyBkx7I6tEZPdBFVKe87AunMNQ6RRZkqqfRXrFSO55B2ZNOGEnVoUAKipGPPtg7dQOqBnvD2_rQQmXIBNAHioY0MexdddZ1XnKvL9Taz5wgjsho-2DMvBHeGGJl-aR0-Wg5lcIYIswcKFGp3Em2exVSpA-1pZ8LDq0piQhiVqFXuJCIumHvYjc9xVW6KcCOJ4-W3bcB3-IItkmYBG-7l5Cp1m4nNcRvXWSvTwFVn-neCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB-fyx40lHG2pmWD1eTlUaVGWsWEQFCJkd4LRdekiYUgj5w0Q6fjeob7gT7OFm9os1ddjQ0tIYxtF1w3CoV2r60VJJQtNP-YDJvAFSAtpQsXYNPNqU4bIJRzil8e3jipkQgyQs7Sftv2DSk_UTG0YrjJrrvtQSKky7YWeXLupY5PR7nC3rqt5tW3NCxlQSrD81-BivWM23ShZaChQZKxaUE2UWqz9-cR10eEAPgGUpkMbJzc4cd3cO8cA6sDqiN66O3KibZNOyVb74ve1Mb_tEWf-fuIwm2F0V-ta8-D_uOJ8GrNdELoGDHgE0MlWEOPK92LOYBL7iBl89h0BjgGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZOH19acWsjl5hCcgyI88qpUFySWzfn-S1d1vQJ4jYkuM4XpuqZu_-mK2flJWaRFgp70ypDB-1x1ih8k5Io4y-1q3k_aSN1g_k6-aJmQL4VR__dHEhU5dl5zlADbpEDFUH5wf11WSyqU-mtJrqmO4kwsYjNt_1UFtKyJKq-vhIVRAcGPbd8HetxGypDhCBJ_SgMp2X46BTC-AQ1zsSHvLPJBr7qwh55geN-m4B3u5dCfpXajjGfWOMqXKfPxqbXb8fPx_KAmZNC8ibwCsR63COYDuFeO7LMrn5BiBLlH09-GzehPUQg5rZx7nt-fUUtpIFJ5upmA7ExrTKvtQZv6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfhpVhWwgE96QSfTlyzAQWf57w_Bv8gbVvz557I1Cg3DDrQX45P79BJ3HxnTrEYmmgU-omJdMAOSUhvu8lMVp65aXhID1EN9117iOd9a70eCqZBk4neM1e1E9aUy7cWiBS8-N9TGNkaPfBucQ-9wegfDMlpLcXrhssTEv0aiz7w1XPeMGNzF0lx5svreAiPQO9gYpu4ncaDiCNVVqIfxnqktp_Dxr_3O1cS5T4q1tf-0aVER7XiA0826YlzxB63AtVcMi4EH8ht_sgcFBcVWUDMviLiXrgPzpj9CFHtVV9vQ7w4Mu5uRlONqmLNxWeCIyA6i5zLhtYQEG7KM0TSlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq68a_0CAkhHeLgg9myVRKR0Akk77yJ94RNzuOSHQ-s3vkNTlltY2gIB9VfO_uDIllBtQWvsIHwGJH1EvlBVqHTjqFwbn-eUUahzXY-uh3JU_aYQbQSzpn6QyZ9lx8KfRQh0S2r635bTqUy7eoCK65CE7rdgSzQnTt2CVWfzW4MkUxdF3bFMkdTPLGgy6SVto9Kl7hwMO4ZaLYRF6-eRXMU9e9w-CovKRHZu0IlEZpCG32RE1XtAdPwBJ8Y0Pgkg6oD4TrLfhDup2wVLWunppJhV1SQ9CBdY65B5GRuFlxttFkpEn4kWn6hz7WMXW2tZkIMWzUuh5BIxi0D4hHYRKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJzomjmqkqpqhSKSiTFt56W9eIKDJ-beEtx6SKmNzPZYvPDph-07NLlmlyD7N1vVpUglmWqAU4Kun1ATM8wqqjDvlQPsfA3G9M1WA12bi8VDgXqSlTv1Mj9x_5FlTUslhJiPDJaSfOapCPMkopieNq0HowY2oLDJGkFUuwWuHaV4tvNEWeE4efvqJ--uryEQtG9fCOGmjvHtdTzkW6Cm7UT5h_G_wpvpABXqXwZ06sz96ws0UKYO36EJMi8HB-QN3_r1uC80Jwtws8E4mBtXj7FmyuKPwbLZqc5UMA2GslwzQlsypVqnDPUDRcImhbdb71L_cGswr2PW0txVlKOENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl94jCJ1-RuKekyr7cWbiSE4qgW-MQkOg8e5X96scpNAeIq4cdB2D-77JIRJKmsvAwgKa5nLtoL2_xYeUe70Fel4bsdkVsirCFjfo1ZG8NJI7O07l_tZ1GuWVIK47ScjVWZZUDWP7FIXiNE_7L1JZwbosY55cUMBFvy-HBRVJw5DpS7pJ93uzXmp1CHPSd2c-yS5lRgxL1XeXd1Cm8Z8tB5G6VfphaLPICirhaBFfmia8GUeSGy3ZpAHFzlTlw4EPdXcrgHnO9LgSfCtXGgPix6dcriBmerfBHKb8GdAa_RQUVIS5TVOW3QWqSCBXKt6ww80Bz4b2ZwFWlT6OxYv8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=p0djApDsZbJpQCgr_Cp9y8T8bAFbZkJvQwEZ-sFWXVnx9lmxIw2FYTurFZUgQcKuJRfRFNoqazacOX9yQpcR1rK88jXYnTg15mwQ1pPa5n3BJ7WqaF1PkE4BREUXAx4QR7zyWV7n8T9yqFffOWL6t3Dp-MGPpRJBTpk5DUGrC0ozXHnm9Ue6NsTHYxj7s4uO5SCwPAZchp2JkaiZ20Ki2OntWLA0EIZ7Z8UMYX2SND4PJd8oKwgm1lhZNH1AuqXsXpa4__2WQRESYhLxzTm9w2JiSyT__iG9ZeAkaGxBAfuaXVVKpTU-7JCKcEvp2OEg4JM8JWDAe69vRgfwFQzAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=p0djApDsZbJpQCgr_Cp9y8T8bAFbZkJvQwEZ-sFWXVnx9lmxIw2FYTurFZUgQcKuJRfRFNoqazacOX9yQpcR1rK88jXYnTg15mwQ1pPa5n3BJ7WqaF1PkE4BREUXAx4QR7zyWV7n8T9yqFffOWL6t3Dp-MGPpRJBTpk5DUGrC0ozXHnm9Ue6NsTHYxj7s4uO5SCwPAZchp2JkaiZ20Ki2OntWLA0EIZ7Z8UMYX2SND4PJd8oKwgm1lhZNH1AuqXsXpa4__2WQRESYhLxzTm9w2JiSyT__iG9ZeAkaGxBAfuaXVVKpTU-7JCKcEvp2OEg4JM8JWDAe69vRgfwFQzAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeZ4fnIVqL0gZeeI-2hysimHyLzn-I6PhNr8wbqB5GOXB1JToYdIdr2ztVKu3V5aE-GqlZKk96UfqS1QW1zBskOmL_juTHktz0CHOewqGPTrKzGA_u1PCy71PY4yhwVcKZJo44JOiRxu6IvsZTALg4WmLIdSv4tywOuJCB9faBxp0vGb0pjndYaT9U5JDFwCjuvXzEzzMPlpWsY55xpnF5iUUj1GfqJcRKHruCMxkzbTqi2Q8piI3h0_vWofJjZgGgRKj-aZeDKE_PS7Jhazde5-_GwGdEr625OkkiG2spHzEnkOs1G5lpDAYcD1lT_me9zpdGIo5K_yExnDR2Jl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=noscHqF86rte0Hrl7mS3vTe1DIgAWxiFtMOJjxRtjWhBLb1qvpNpvU-YikE2D3aI6GX1WxIXNbJLE0R48zvkHl278qETzQL1jnlenkVN_TKsNvePS5PMg0i3__GQJ-PojS7ib16Nd-jQa4Kxnng3OofT__8l_O80YG9XjoYayYyOxKIXKLEHCLWC7DL8EaR_YONlo5rz2ZlcqjecwKB7w0edSGUruWl-vdTE7xrBh_OcJPP8KYmwgun5jycTRlkZGK7BxtrV-OpwO1UqOU8WBJUQC5HfaWqKNxyo4g_3SwmJCcQJWLvMKuT4vZE4AAjfFjBKxoyc7VlIHx4_SsgMNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=noscHqF86rte0Hrl7mS3vTe1DIgAWxiFtMOJjxRtjWhBLb1qvpNpvU-YikE2D3aI6GX1WxIXNbJLE0R48zvkHl278qETzQL1jnlenkVN_TKsNvePS5PMg0i3__GQJ-PojS7ib16Nd-jQa4Kxnng3OofT__8l_O80YG9XjoYayYyOxKIXKLEHCLWC7DL8EaR_YONlo5rz2ZlcqjecwKB7w0edSGUruWl-vdTE7xrBh_OcJPP8KYmwgun5jycTRlkZGK7BxtrV-OpwO1UqOU8WBJUQC5HfaWqKNxyo4g_3SwmJCcQJWLvMKuT4vZE4AAjfFjBKxoyc7VlIHx4_SsgMNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adzlOrqM1Qv9KrVeztUudzRCstUw6NmlMFknw8zJB_PGvlKjwgIACopi_oNTyTEsK6AoeVv5zGSTpH6WpkGAjGXq9J7zZTcWxDSqpwc5wBjS05lrvl2NStp1Aq7rpJFFCT5eTsfHFvzUgs3uV-gCMDPlw5wvIi2Q4qMN1scGXeGzddamihlWSPbKn_5ZcnQkMr7m-Dir4Z5F-e4OTFcJqmyPBeb4RGlrV9JOnF1URHUv2j1dwX4Dggc9VKEMxaOI15TNZRsKiaPNk6qb_RcUw6Fz0heEjQrPm3_13dv89CVHQVJtarIOutcpMlpEdHDk1Z1yNcwfTC8xCi45zmgs5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8295" target="_blank">📅 00:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbdq4QB-Z9QYZOmU-y8XGEBH_IhT9rvG-X3GVxSBTWcFQnDHkAa4GLWmkQv_xAObMObSEGcJy6S1MFoxbAiahCgr97xiRbLft3etl6CeJd1WnmESTAEE4AeG3MA8iiZzoXS6YX-TLC2dXrMjmWhkBd7NgPgabG-kNUHxwoVwlx-Pw8nSQZIoKtEalfsErJawGDO7aFmEgXQwYkW_XBoGJPpMMl7f_PSHURPSyZiX9iQ2BkxpIq7XhmqZcIvPbU8lBDt8T5AppqPSDqK6ClzZdE0eqYLOzk7jmmbg61Xq_fzmIDKwqbwoVZOBrE7MPnuB89Z0w0t8IZiIOZK30PMb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8294" target="_blank">📅 23:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8293" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=JXQ-q14JrzWTlq0eFJEZZGFJG-EVQwSBRKHMuTTAhIyOHgVp8ayCW6ojE470w1LonC6KQNHUyxZcGpSuDR65PwWTlQQ9si7nIQ3MeIIvZOC6JLAEsuB6o9z4Qa5RGvyJMItu8e_iWbYfWF4yA9P9cMzzHw85QxL1h_Ipoqm0zzv0zIPDwLhKHWkmZlUQQ0yvnQSEfk0BMGtgtkBA_m2sT0OdD829Z5z-dPZUnwnk0XOWdKnqahvQeYU500MFwKQc-4XcIm9y1l5rT7qtY_RTMk2rIUqckX9Wyk3BoWmiXQVJZ9l0xJQzgJ-g3RSa8SQ5BiBXRzh5RSqSaNtwsQLV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=JXQ-q14JrzWTlq0eFJEZZGFJG-EVQwSBRKHMuTTAhIyOHgVp8ayCW6ojE470w1LonC6KQNHUyxZcGpSuDR65PwWTlQQ9si7nIQ3MeIIvZOC6JLAEsuB6o9z4Qa5RGvyJMItu8e_iWbYfWF4yA9P9cMzzHw85QxL1h_Ipoqm0zzv0zIPDwLhKHWkmZlUQQ0yvnQSEfk0BMGtgtkBA_m2sT0OdD829Z5z-dPZUnwnk0XOWdKnqahvQeYU500MFwKQc-4XcIm9y1l5rT7qtY_RTMk2rIUqckX9Wyk3BoWmiXQVJZ9l0xJQzgJ-g3RSa8SQ5BiBXRzh5RSqSaNtwsQLV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی و فرماندهای سپاه:
@
RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8292" target="_blank">📅 23:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrZRs7zPrNTRLRpzI0OJoQg7ZgiohLkjR7QVpEzlTnc9YWztXNQMzReWrWV5gnO_Yd-wQ-1UFl9gFLkg2y3H783GopeTFVioHDnUIC1uUqfiXomWUh04O0QiYUf0WAsqy6STdtnZV-5l_OBqhZOOl-lIBp7gEO5Z7U9NbkUjcFZQG4rl0L4v_yJn91DP-GiaCnrbvUCPHf43I-AB20T9-VfK7N9P7QupI15jGMlovJ8uQr7mBFyBKU7_dqQUG3X9WzeqlDIuu1r0GOUBdS3Q8-yLIMGkDZXS2h8FIFQC2uiLAZubfO5imSIr5mmaI_3gHYBqvPAVe6-UAmFpGM9u0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)  و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.   او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8291" target="_blank">📅 21:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8290">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/IranProxyV2/8289" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8288">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8288" target="_blank">📅 20:02 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8287">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q99XG-85KBRViiaO9USpWY2eDEZZVKWSiM1TYNDT89EtYzq_3T-fAMCOjmEKIFo24kpvAtu_t_25NY_gMQGSTSF_s9h_VQsz6FqvxK-UpM-WLpPt9yNSHc2Yk4dNa-CG5O_wS8fDyCeiOcQlT--16ez0VuWP5A8xp9ehgErVvgZbpvjh3DiCEuML33kBTHKl-6INcJxR6SP3r2XGjiOtuGHC8RLW2kdmyXI9bGvXc-8zxq1HGiiracIiZu9vCxuUOhHDXkRk4eChy7xM6KqvTYCs1hESwi8y904tTcCmpd_JKeKbCwRN0BeiObyNmUUX3M1_YfbV3T-Lsso_ICR7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رییس کمیسیون انرژی اتاق بازرگانی:
سال گذشته هر هفته ۳ تا ۴ روز خاموشی ۲ ساعته داشتیم ولی امسال تمامی روزهای هفته ۲ ساعت قطعی برق خانگی، تجاری و اداری داریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8285" target="_blank">📅 13:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید
@RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8284" target="_blank">📅 12:32 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
