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
<img src="https://cdn4.telesco.pe/file/B1DSEy8FwGuQLmji09TJlHJRtE5kpcJemacL1q6ZoX9F48qzzsfUYSbBX-sFMYMMAxLRYNyp24Xdg2_EDdZcbGJZMLyp6HcPnxb4jffLlCKlTllTKe7buq4PQIDmj5Z2_-81r84xxC2IirGq-7UImALsdjiuzrsQk73jwlkHS3-lpVYQFnM7-_cpmLVVhNsEZX8Cb0zY-P_pbvV1OdS2CGuFP8O-6n3Ws5V10BPYAp0qaEt0aBd7vcSIFk5896Y5WC0s3CUlSnwkP5QRS1ib5JAEzS8JNlqujqkwYSB8V0bi0-ev_cZgoGChUMPWbZgSwM8LrJAXZNcBuge3xFb-qA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 03:28:51</div>
<hr>

<div class="tg-post" id="msg-8703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت ملی شکن⚡️.npvt</div>
  <div class="tg-doc-extra">29.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
☄️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 561 · <a href="https://t.me/IranProxyV2/8703" target="_blank">📅 02:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایرانسل50ترابایت نوش جونتون.npvt</div>
  <div class="tg-doc-extra">4.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/IranProxyV2/8702" target="_blank">📅 02:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایرانسل.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8701" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/IranProxyV2/8701" target="_blank">📅 00:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">100ترابایت♥️.npvt</div>
  <div class="tg-doc-extra">4.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8700" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/IranProxyV2/8700" target="_blank">📅 00:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برق تک فاز.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8699" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/IranProxyV2/8699" target="_blank">📅 00:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/IranProxyV2/8698" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8697" target="_blank">📅 22:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8696" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⚠️
اقتصاد نیوز : ایرانسل و همراه اول امکان خرید اقساطی بسته اینترنت رو فعال کردند.
اوج خوشبختی ایرانی خرید قسطی نت
😠
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8695" target="_blank">📅 18:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/IranProxyV2/8694" target="_blank">📅 15:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ALL NET 8 (1).npvt</div>
  <div class="tg-doc-extra">5.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8693" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ نپستر نامحدود
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/IranProxyV2/8693" target="_blank">📅 15:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه سوپرایز دیگ هم واستون دارم، بزودی رونمایی خواهیم کرد
😁</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/IranProxyV2/8692" target="_blank">📅 14:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=40T
💥
توجه کنید پلن های 3 گیگ، 5 گیگ، 10 گیگ، 15 گیگ و 20 گیگ تو ربات موجوده با تخفیفففف
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/IranProxyV2/8691" target="_blank">📅 13:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsl-XN-OCcOa8rXmrxBNnXxz0tsEr2k61xY3BacX1N4KAUeoJfy4I_wvsGbs8hCKWt8DKqP8_QZfqHT5YwlP0YgRlLXzLUp-c-cMehjt1SwzhZ3OPM88feYoq2jFiZgspRdtr5E2IyXmPCoHS7l4AdQPv1b5KGvfTGXIJJe6DblA-XtB4da_MNlTP_1nMLo0cqNTrwOPthokFivr1TGsj0G6UTDx-blb8EslEa7CDV3Ro2f6Lb0uj_TIGJ4OWuBzmaZdeXtrTG9zqHT9htdTHZnrm7JCMn6KaKxjJfQ5sGSYJiITE5yi1ME5MZxiIkUlB1Ar83HNcRu2l0SNCq7TQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=40T
💥
توجه کنید پلن های 3 گیگ، 5 گیگ، 10 گیگ، 15 گیگ و 20 گیگ تو ربات موجوده با تخفیفففف
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot
📌
دوستان دقت کنید اشتراک های که تهیه میکنید، مثل چنلای دیگه تانل نیستن، قطعی بعد دو سه روز ندارند و به همین خاطر قیمت ها متفاوته
، پشتیبانی تا آخرین مگ مصرفی شما انجام خواهد شد.</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/IranProxyV2/8690" target="_blank">📅 07:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@russiaproxyy🇷🇺(4).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8686" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/IranProxyV2/8686" target="_blank">📅 01:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیگه به آخرش رسیدم.npvt</div>
  <div class="tg-doc-extra">13.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/IranProxyV2/8681" target="_blank">📅 00:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8679">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">36.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8679" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ open vpn
آموزش اتصال:
کانفیگ رو وارد برنامه کنین
بزنین روی connect
بعدش ۲ تا گزینه میاد بزنین روی continue
عشق کنین
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/IranProxyV2/8679" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8678">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIDiabSbg-BjvDDohOnj2Zu3_hWHgtOaK_c6qhyywl1sdlC60uL6WWeFu2pleUcA8STVqoHKlxJQYuA2S9ZNLVn2SV6GUmEqsjz9CzSL3Zpp_nuv0VfS4qXhZO8Lf_Q8yJzK3Vt7eI0yhz1RatZmgGQNbHE4LYw8d8gmnhhhnKy8PZjnwQEeQfqKPaiJ7RhEg31KBhUGaucajvRWaXhCOJQ1unHvY4dnxNCCo9Hi3wAXzFC_yn3BKWTQfWIOr383Vt6c0aa6iNek4OJrtqgQ9RdSpZNmYz-ShKRjuE-7jZv7EnvdkI8GGap3PEh_nu3CqY1NKbJQ6wGZcs-HR87HVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بررسی وضعیت اینترنت ایران نشون میده که پزشکیان هنوزم نتونسته اینترنت رو وصل کنه.
▪️
اینترنت دیتاسنترها قطعه.
▪️
اینترنت خانگی به شکل وایت‌لیستی کار می‌کنه.
▪️
پروتکل‌های IPv6 و HTTP3 مسدوده؛ SSH و UDP پر اختلاله.
به خاطر کاهش پهنای باند شبکه هم بسیاری از کانفیگ های پولی که در دوران قطعی اینترنت کار میکردن؛ از کار افتادن.
خلاصه میشه گفت اینترنت وصله ولی فقط به ظاهر
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/IranProxyV2/8678" target="_blank">📅 23:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8677">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">vless://309f5aa1-2665-4ceb-9cc1-17eea907a927@185.143.235.201:8880?path=%2F&security=none&encryption=none&host=sublink2.ionosio.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
اختصاص کانال
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/IranProxyV2/8677" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🦕.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وصلللللللللل پرسرعتتتتت پخش کنید
❤️‍🔥
👀
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/IranProxyV2/8676" target="_blank">📅 20:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8675">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">باطری نیم قلم (1).npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8675" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وصلههههههه پرسرعتتتت نامحدوددد فوررر کنیددد
❤️‍🔥
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/IranProxyV2/8675" target="_blank">📅 19:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8674">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwZfKjOw_gr8ZeRbDGnBlJH5bVBzz0jyv0jyPG0sLH-IWA1FHKVSLUWEdpfIF9UYWkF7z3tRfU-jqAheBk4Kei8L8_49ubsrNYGlUWEGpuA5L0vdkyprWRyFM9xKoOkozhvm_ySrqjwC6JVJx6uF97zzn0l4CFYZGjVdi9yOsYX7_0OBTz2AXGnwCewdvIQXaQHA79ZOwWBnkTXYlXx9mAT42JhVoYcWxR6OE5_doRBR-sgFVWBYRHnBR6q2iWtm3-XPxiEierKe95rUd0m_SCqKW1VX9DDyrqSutA0BiExn4cf9yGQ4eclfVTo56fE-Qn446uoIgMTvN4cgmy0e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دوستان عزیز متاسفانه دامنه قبلی ما فیلتر شد توسط آروان به علت عبور ترافیک زیاد و دسترسی به ساب هاتون امکان پذیر نیست، درحال حاضر ولی ما حل کردیم مشکلو، برای رفع مشکل دامنه جدید جایگزین شد که باید لینک ساب هاتون مطابق تصویر تغییر بدین یا اگه ساب رو وارد v2rayNG کردین نیازه فقط یه اپدیت بزنید مشکل حل میشه.
◀️
لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته rezaz7ziranisa به
russiaproxyy
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
✅
دوستانی که لینک ساب رو وارد v2rayNG کردین، فقط نیازه یه اپدیت بزنید از منوی سه نقطه بالای برنامتون همین تنها
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/IranProxyV2/8674" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8673">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ajex موشک متصل.npvt</div>
  <div class="tg-doc-extra">12.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8673" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ـ NPV حجم نامحدود
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/IranProxyV2/8673" target="_blank">📅 17:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8672">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">vless://dfd2bd8a-aedb-47d1-b87c-c22f18495592@f101001010.imsoon.org:80?encryption=none&host=play.google.com&path=%2Fsoon&security=none&type=ws#Xhttp80-iao93lhbdd-1000.00GB%F0%9F%93%8A
به غیر از همراه اول، مابقی اپراتورا وصله
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/IranProxyV2/8672" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8671">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
مدیرعامل آروان کلاد(ابر آروان):
◀️
از نظر فنی همینطوری که میشه توی یه لحظه اینترنت رو قطع کرد؛ همینطوری میشه تو یه لحظه هم وصلش کرد. زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست. وضعیت اینترنت در حال حاضر بسیار ناپایدار و ضعیفه و اصلا به شرایط قبل از جنگ برنگشته.
ببخشید که ما ریدیم تو نت دیگه تکرار نمیشه روانی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/IranProxyV2/8671" target="_blank">📅 17:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8670">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYRW5aZWRwMm1rVGJUMXFD@4.168.201.246:443#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vmess://eyJhZGQiOiI1MS4xOTUuMjM1LjcxIiwiYWlkIjoiMCIsImFscG4iOiIiLCJmcCI6IiIsImhvc3QiOiIiLCJpZCI6IjU5ZTI4Zjc4LWMzMWItNDYxMy05ZDlmLTFlNjczMmEzMWY0NiIsImluc2VjdXJlIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwicG9ydCI6IjIwNTIiLCJwcyI6IkBSVVNTSUFQUk9YWVkg8J+Ht/Cfh7oiLCJzY3kiOiJhdXRvIiwic25pIjoiIiwidGxzIjoiIiwidHlwZSI6Imh0dHAiLCJ2IjoiMiJ9
vless://9ca41eeb-4b30-4271-a123-22021b1230d0@104.17.121.71:443?mode=auto&path=%2FTelegram-Zedmodeon&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=mano.tll-far.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=mano.tll-far.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
trojan://f6d3aa07a52dbcedcb4731029e2fb6ae@18.163.128.27:2663?security=tls&insecure=0&headerType=none&type=tcp&allowInsecure=0&sni=www.nintendogames.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/IranProxyV2/8670" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQebihkiRfpxtWo3Gf7N6_Jd3tGK1SzYmnTljsMw6DqYMaIpVoPliS_JFRURgV8eNJsupcEWYyqeYnl7KQrH51Ij-MUFr1RT2CDdqttnF1bG8p4-QYxb7YW1PUeHDAy6Fqm6eFvbq3QzG0JUUpT8JyFfL-iw4T7pGd2-GcPtw4gDBX_KwTsl9nEyFb23BEY4ekk5OB7WNxIzp5_vO0eH4RnLuEd7aAuWBrLLPD44zwAl1aU3_0dFXU6Kex0_PRUH0EWeIN1PECsAsHZDfcGf7q0TzJWmWPBwlxqqhmLHT_mvUFBK5m0c3LhYkVVvmCQXq81whKqU3iv9YHrH59nNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این روزا سر به سر مردم شریف ایران نزارید
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
|
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/IranProxyV2/8669" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8668">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(2).npvt</div>
  <div class="tg-doc-extra">19 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8668" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ پرسرعت نپستر مناسب تمام‌ اپراتورها ، مخصوص دانلود و وبگردی برای اندروید و آیفون
👀
💯
ترافیک 12 ترابایت، زمان نامحدود
⚡️
❤️‍🔥
مخصوص شرایط نت ملی و فیلترینگ شدید
☄️
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/IranProxyV2/8668" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Moshak.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8667" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن، اگه ارور retry داد، چند بار پشت سرهم بزنید وصل میشه سرعت موشک داره
👀
☄️
Fast
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/IranProxyV2/8667" target="_blank">📅 08:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8666">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺.npvt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8666" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ پرسرعت نپستر مناسب تمام‌ اپراتورها ، مخصوص دانلود و وبگردی برای اندروید و آیفون
👀
💯
ترافیک و زمان نامحدود
⚡️
❤️‍🔥
مخصوص شرایط نت ملی و فیلترینگ شدید
☄️
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/IranProxyV2/8666" target="_blank">📅 08:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8665">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/IranProxyV2/8665" target="_blank">📅 07:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxY4jyGcM-Zms-H9gUVHXaRRpEMNTMBJIeRZTnoWzarG4e0B2Ls2dpUYsSL4LCcEhgOkbJ2PufTBkVeWV79-mnumkK_MeVNCJwspHwVabdaQ0GDXYiyzrlMlKZlJVrbEmbEKsWe5X_yapPhHsfhgJxJzKmBfOg06A8IT8AIH8n7YhzOjreZhnGqqYDTgyfDOxFu2VsJKP5f24B5Y51qtH2122Hghoozirwp52f74AQFL7LpDFPK5ze6NNGEOx0jNHlATDFCF5-hihZVRXblXW5iQVwfJ4OmlggFcMUUDP7U3EVluApJlLbv5raGhYnTPhBZPiZ8u9qW0nocu7KBasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دوستان عزیز متاسفانه دامنه قبلی ما فیلتر شد توسط آروان به علت عبور ترافیک زیاد و دسترسی به ساب هاتون امکان پذیر نیست، درحال حاضر ولی ما حل کردیم مشکلو، برای رفع مشکل دامنه جدید جایگزین شد که باید لینک ساب هاتون مطابق تصویر تغییر بدین یا اگه ساب رو وارد v2rayNG کردین نیازه فقط یه اپدیت بزنید مشکل حل میشه.
◀️
لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته rezaz7ziranisa به
russiaproxyy
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
✅
دوستانی که لینک ساب رو وارد v2rayNG کردین، فقط نیازه یه اپدیت بزنید از منوی سه نقطه بالای برنامتون همین تنها
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/IranProxyV2/8663" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8659">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">108.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خطا retry داد ۴ الی ۵ بزنید روی retry وصل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/IranProxyV2/8659" target="_blank">📅 21:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3a26wQOeVQAkZzcEMaIBgYQx1cUMskKMDs_Nj71faJ1hIfeyqvoAHqGBmQr7raI0OnbOoL0qnRco7dJB72F-m0QU0QNLu4vUALFCSqmHuAjeyMYRm2vjlZ4gdDZBaCSPZ6OfcZeNMZ8zCTcoCT-hneONVBAvgwARisaFW7XI8hZJUQ7ujGFT1H2Vk1Kn5BhiiTabbaWb-YuAArsVNtn7z4f7ifl6XkS0UqRnC65WZIATBeuqDRXlljlhcMyUF-lb2EXssFEgeVGL4mzFctAnj6pDo-y4PLPDp7fHY9L_AUpH__jTsxCx9r_trzIDlj6WvrGRnE285OprUa40ydj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سیتنا:
علت کندی اینترنت ایران اینه که IPv4 بازگشت کامل داشته ولی IPv6 هنوزم بسته ست.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/IranProxyV2/8658" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMYtIoXDexHcwLnnMF-JKiG1OKw_a2JBvMPWXc2v8f71Tk6hQ61xs6J0QfjsRnuaxc3ZXwcipStEyTe-k45GoQkZIEXPZ7bsAG5Uh4IFQ8CPY6cxpZKZfi2Pruplmpjr5d8HXDhnx2Qw68HjEnWijqKg57Sjz-lhOUj9UiM_6klVmNnvY5ZUJTWjD08d0Q3vzYrqAOgnutWFjiqqiwc8LwjM2FjPuH9FZ2E3_W2K4AG3cf6x2o_BKjMM9UtWcTylwAkvw7VQQ7x4YlWqtxLhMREcIBdbKy9-LUs7MyukFjdCKMoKJCb1J5LS8d66RIKO9jEXPH1UMMgjue2kAdKdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
😬
😬
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/IranProxyV2/8657" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8655">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@iDeathBirth🐰.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8655" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اختصاصی نامحدود.
بفرستید بقیه‌ام وصل شن
🤍
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/IranProxyV2/8655" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8654">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PRO71💎.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
کانفیگ نپسترنت ، Npv Tununel
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/IranProxyV2/8654" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8653">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHUdAvHBEMujyfb-VUEEPF7lwFcIZhiRXRSaGsQQIYsNTZkDsgj_70NbjZelaiEMNV9lQDwF_0dqagLEa9d_3hpWlFkm_QUhfK2AWj7mNpAVf12dVTn6fTFflowvxlTik_6-zoIXlrSQc3RKPniOFJEcHnWzRbgiJqioubODSf2r8-yaTxWYcjVqTO0A8D-nfgHkh9FOxio53xllEotiaqIpGfpCBBNEPkuejc4o8UOO2cjKzKZzfQ5zsduvpXes7-FPIyDSgeydvWqH6UmmFGibxKvPBgM6QfkwZLpAuVx54Tnli9S6SBbEOcwzVTpRLj5nEe-o_kBNdwevrlcq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مدل محتوا(دیتای کاملا جعلی و روایت ساختگی) که یسری از رسانه‌ها(دلقک‌های حکومتی) دارن منتشر میکنن فقط داره به قطع اینترنت و فیلترینگ مشروعیت میده و اصلا جنبه فان نداره!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/IranProxyV2/8653" target="_blank">📅 17:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8652">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/IranProxyV2/8652" target="_blank">📅 15:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8651">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گلچین گل های غربت⁵⁰.npvt</div>
  <div class="tg-doc-extra">9.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
کانفیگ نپسترنت ، Npv Tununel
▫️
6 تا سرور (پینگ بگیرید) نامحدود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/IranProxyV2/8651" target="_blank">📅 10:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8650">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">trojan://humanity@www.calmlunch.com:443?path=%2Fassignment&security=tls&insecure=1&host=www.calmlunch.com&type=ws&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e258977b-e413-4718-a3af-02d75492c349@45.130.125.69:2096?path=%2FChannel----%40VPNCUSTOMIZE&security=tls&encryption=none&insecure=1&host=jp.aniua.qzz.io&type=ws&allowInsecure=1&sni=jp.aniua.qzz.io#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/IranProxyV2/8650" target="_blank">📅 08:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8649">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(5).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
🏅
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
💥
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/IranProxyV2/8649" target="_blank">📅 06:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8648">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/IranProxyV2/8648" target="_blank">📅 23:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8647">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(4).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8647" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👑
کانفیگ OpenVPN-VIP
🌐
📶
آیپی ثابت بدون نشتی DNS
🇵🇪
🛡
متصل برای مخابرات و یکسری وای‌فای‌ها(منطقه‌ای)
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/IranProxyV2/8647" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8646">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">درحال بررسی و آپدیت جدیدی برای سرورا هستم، کمی طول میکشه ولی سوپرایزی در راهه
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/IranProxyV2/8646" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8645">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8645" target="_blank">📅 18:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
سنتکام: حمله ایران به کویت با موشک بالستیک نقض آشکار و فاحش آتش بس بود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/IranProxyV2/8641" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8634" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
کانفیگ برنامه Open VPN Connect
Password:
@KurdConfing
🌐
تمامی نت‌ها
📲
اندروید و ios
❗️
اگه وصل نشد چندبار retry بزنید حل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/IranProxyV2/8634" target="_blank">📅 14:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ایفونی های عزیز جامپ جامپ استفاده نکنید اپل ایدیم لاک شده سر این فیلتر فیلتر دیگ استفاده کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/IranProxyV2/8633" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8630">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">54.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8630" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟠
open vpn
🛜
برای ایرانسل رایتل مخابرات چک کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/IranProxyV2/8630" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8629">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیشب آمریکا به بندر عباس حمله کرد ایرانم در جواب به کویت حمله کرد اما هنوز اتش بس نقض نشده
به این میگن یه توافق درست حسابی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/IranProxyV2/8629" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/IranProxyV2/8628" target="_blank">📅 13:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGg_ss3NsDss9tugjMlVBaZ63N9-n-0yPIiH-PSSpNZtA-ZeVoGhC3NYOaxQo28y2jgSEJufRKWsz0dvkZBVTcOZELVHpsmKfLUqnNaOjtzvurB24r6ibKiTdyQVeLbfSOzflcccJ5FNpt35DmdC7vwxwASGqDd6rw5NHUqyTvnsgXb9vggrCkcp6wjcv2g6AsmpjWz1q_hZM4lEu81cRCz3rjZ3kKX94217npfId4b8LLeip7Bla9wbCctUGTUMjesJ1-n6oTbCYzMIIrNO9YH06ODxOckJhoFZoqywbSMhgMU6afDv1XtY9aaj0MooJxdKBtR2P9TyO8fDKJx14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین آپدیت از وضعیت اتصال اپراتورها به اینترنت بین‌الملل!
+ طبق این لیست ، ایرانسل با 38 درصد بالاترین اتصال رو به نت بین‌الملل داره و باقی اپراتور ها و شرکت ها همگی زیر 30 درصد اتصال دارن!
++ یعنی اگه اینترنت رو مثل یه دریچه در نظر بگیریم ، الان فقط به اندازه رد شدن هوا این دریچه باز شده!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/IranProxyV2/8627" target="_blank">📅 12:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBTpl2s58JeHnm3AJFfdXMipSwxUd3pd8Howhgyar_-MMsByr6Lrf2h41zYjcr5itAHlqtmAUdhVQ1oeUK_OOGbTEfpndkId8BnfN-8S_ljKtYMqsOs7m4KQ9mI4D3MF8VgZMt47a_ivm9TR77-exfBkXq8E2lD7Y7nb0ApRTmtelZQC4sOsWsmlE8iqxCab6-HI1MZeK8NMr2JWi-PLGks2lO71LsV5Q2O9mUebfaL1W8Pf2ppQXKDY6t1AmOkwoMPZOjRiKHPnt7hitelEu_7CZOgGhqecNOEFlaztosmGk2xbPRastoOytpV56ppbDNFVByX_CCNZWdrxTt52sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍽
فعلا درحال حاضر تونستم تانل جدیدی بزنم رو دیتاسنتر جدیدی که پیدا کردم و تهیه کردم براتون از خارج کشور پینگ میده، با قیمت مناسب و پینگ بینظیر، باز مجدد اگه سطح دسترسی ها افزایش یافت تانل های جدیدی با قیمت هایی پایینتری براتون موجود میکنم حتما،نگران هیچ موضوعی نباشید تا آخرین مگابایت مصرفیتون پشتیبانی انجام خواهد شد
👀
🔐
1GB
➡️
60T
💥
◀️
جهت ثبت سفارش میتونید از ربات اقدام کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/IranProxyV2/8626" target="_blank">📅 11:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🟢
پروکسی متصل با سرعت خوب
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
https://t.me/proxy?server=tg.capycore.ru&port=443&secret=27ebe852539fb8ec5f327c73262bb721
https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
برای اتصال به پروکسی ها حدود 10 ثانیه صبر کنید
⚪️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/IranProxyV2/8625" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">vless://f172c28c-14f7-408b-b41e-838f4f32a15f@185.143.234.122:2082?path=%2F&security=none&encryption=none&host=tl2.axepart.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله دوستان استفاده کنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/IranProxyV2/8624" target="_blank">📅 09:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/IranProxyV2/8623" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">❤️‍🔥VIP❤️‍🔥.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8622" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/IranProxyV2/8622" target="_blank">📅 08:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(3).ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8621" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
🏅
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
💥
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/IranProxyV2/8621" target="_blank">📅 03:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/IranProxyV2/8620" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
یکی از دلایل اصلی اختلال و کندی شدید اینترنت، سقوط سهم IPv6 در شبکه ایرانه؛ سهمی که از حدود ۱۲٪ به فقط ۰.۱٪ رسیده.
این افت باعث شده فشار شدیدی روی IPv4 بیفته و نتیجه‌اش رو حالا کاربران به شکل اینترنت ناپایدار، اختلال VPNها، ضعف شبکه موبایل و لگ شدید در بازی‌های آنلاین می‌بینن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/IranProxyV2/8618" target="_blank">📅 02:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
⚠️
گزارش‌های اولیه حاکی از آن است که ایالات متحده یک عملیات دفاعی را در بندرعباس ایران انجام داده است
.
🔴
یک مقام آمریکایی گفت: «ایالات متحده برای حفاظت از منافع منطقه‌ای خود اقدام خواهد کرد و این بر آتش‌بس تأثیر نمی‌گذارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/IranProxyV2/8617" target="_blank">📅 02:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕️
خبرگذاری فارس صدای انفجار رو تایید کرد
🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقۀ هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/IranProxyV2/8616" target="_blank">📅 02:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/IranProxyV2/8615" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/IranProxyV2/8614" target="_blank">📅 02:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/IranProxyV2/8613" target="_blank">📅 01:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کافه پروکسی💥.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8609" target="_blank">📅 00:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8607">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ open vpn
🎀
آموزش اتصال:
⬇️
کانفیگ رو وارد برنامه کنین
بزنین روی connect
بعدش ۲ تا گزینه میاد بزنین روی continue
عشق کنین
🍒
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/IranProxyV2/8607" target="_blank">📅 00:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8606">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V41h2j6vNi42THD3SRVgCpJ0EAquhy8eMKglFaoMec9YcRtl-X0pHvRS-FmYykEfV5S2CxscQIryap4x15l2RTcd68v8YfqlEsjTO4Yzwg-BlH0-7rKqmt3-Et29mJ7-YkviXEDTnAkyihyN2adhk3-M1B47sA1mX6ij54eqAZC9eZuR4g_gmJUkkZyR8jtuAC_Y1PVq12ZRcapg1uxzq1RJ2YDNRdeAIB2m1OptzgSQ8RBniKUx9ceWhoNlRpGY3yKQbQ51Q2klHtcKXKvC9IJMqPPdMn_f3RzuafuWM8moWQkVjKtqP_H2VSqnSM3bgXWURRb7RY9MNZLoxSJUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت :
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/IranProxyV2/8606" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8605">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/IranProxyV2/8605" target="_blank">📅 23:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8604">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اپ استور هم رفع فیلتر شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/IranProxyV2/8604" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8603">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گویا گوگل پلی تو اکثر مناطق وصل شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/IranProxyV2/8603" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8602">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(2).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8602" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
🏅
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
💥
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/IranProxyV2/8602" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8601">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/IranProxyV2/8601" target="_blank">📅 22:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8600">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/IranProxyV2/8600" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8599">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/IranProxyV2/8599" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8598">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/IranProxyV2/8598" target="_blank">📅 21:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(1).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8597" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
📍
آموزش اتصال تصویری
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/IranProxyV2/8597" target="_blank">📅 20:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8592">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❤
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/IranProxyV2/8592" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8591">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
ترامپ درباره ایران:
آنها می‌گویند که بسیار تمایل دارند که به توافق برسند.
تا کنون به آن نرسیده‌اند. ما از این وضعیت راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با جدیت بسیار کم هستند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/IranProxyV2/8591" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8590">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ: ایران حتی اگه اورانیوم های خودشو هم تحویل بده هیچ خبری از کاهش و لغو تحریم ها نیست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/IranProxyV2/8590" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8589">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پروکسی‌های متصل
♥️
https://t.me/proxy?server=49.13.35.164&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=mt.corph.ru&port=443&secret=dd2ed7517b077ef414e24b106e0729335d
https://t.me/proxy?server=free-mtproto.flexiblenet.org&port=443&secret=4da47f00c2291d55696fa3ae954ffd78
https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
https://t.me/proxy?server=91.107.182.200&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.131.45&port=25565&secret=79e344818749bd7ac519130220c25d09
https://t.me/proxy?server=91.107.174.85&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/IranProxyV2/8589" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8588">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
پروکسی متصل سرعت قوی
❤️‍🔥
⚡️
👀
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/IranProxyV2/8588" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8587">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اینترنت بین الملل در حال قطع؟
نت‌بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPN ها هستند. کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPN ها می‌باشد.
تندروها کار خودشونو کردن واسه همینه خیلیا نمیتونن وصل شن یا سرعت افتضاحه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/8587" target="_blank">📅 19:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6PFAYbUMEPuIwnyd_eEi6f-EyvwaUOWSOodVhcF9VEA4Ti2fcdSdRiVB5Y7TgzdiL8ePed4OUBbVyUKXZEjHMMcDX0jwtmHwNW_sticHQyXCHr3OVQy6bqqTnPjK4Kq9M1K9fPOFQaVV-V3Krg1ZJKAmRDsPK-zUMfsMOU_hUW9Lk0tGOF93LwHG9BolOuZiulox8NeEusRo1lcAvPvI_b2HVa8yrP5onmTPHi7i3h-GuavThV7ZdVR0ls4oPAhRUHYI5DN3qp1OsqHm71R09zuv8IRjX0mxYqUd3A_HH0PCoP6SisteCrYMstKmHQpFL-OoWL74d0Z2TVPXmsZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/IranProxyV2/8586" target="_blank">📅 18:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❤️
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/IranProxyV2/8585" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این لیست پروکسی اختصاصی رو داشته باشید باید با خیلی از اینترنت ها اوکی باشه
پروکسی اول
پروکسی دوم
پروکسی سوم
پروکسی چهارم
پروکسی پنجم
پروکسی ششم
پروکسی هفتم
پروکسی هشتم
پروکسی نهم
پروکسی دهم
پروکسی یازدهم
پروکسی دوازدهم
پروکسی سیزدهم
بفرستید برای دوستانی که نیاز دارند، وصل بشن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/8584" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?mode=stream-one&path=%2Fde&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=de.lezzatzone.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=de.lezzatzone.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
همراه اول تست زدم، اوکی بود، مابقی نت هارو خودتون تست بزنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/IranProxyV2/8583" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO1PoMl1GqMLgBihWkAdohh04pPQsvlDQQsX1TrENmI8rNW7HX6lX4QVO1dbrNeJvqimdcrky269uyPBM-sccltGX-EYbAodH7cBvq_x62VAecxaUQClZRzDda_RLmdsXSF7Uk1n5FJc9vBGJDLVkJAFEgmBz0GXtUfFJgVlYjP3Bj3iP_kjuHCsftth8zLtBlAxhGqBMVLZyDJJLvgp9WWpP7wV31X_JSZGdYfAJm7iDPzxBTZC3UOreQFQ5ePEB1Fu77G1yKMION-2iUfhPgoCloBtUf6_BAvEkDcYinVfzGQg2jKFSppktUHqSXSvDvLaqVsXNJ-mmCmHJ3tE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه اول بعد از اعتراض کسانی که اینترنت  پرو خریدن و گیگی 40 هزارتومن بابتش پول دادن اعلام کرد در صورت تمایل میتونن  اینترنت خودشونو به حالت قبل برگردونن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/IranProxyV2/8582" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNf-xp6KzWdE-tky_zG7KR0RTW7KcBWfLH8BIlXeB8CMfwVGxQfX1F6FNT-CpusNCk2dIEJv9kgjLu1dXdW46GdDEQ70F13aLmX1vVmyviuFMCd5RoWLqBlB3qtPBOzW2Ys-hPheS0mLvx2M3eA2HpwhjIr35SQJ_rPJut3BcpEjlk2i8Ohwt08K2Bpl7Hb9zciB2R_mmaeZAhZ898AEWBxArku7K0tO6FoyEXfcDkTJ0xZxw4K7hy79wgAojhAHlQi6HIircCqUaNCvIsiEkCRfJ_gqZp1FBAwk7QtGMpwVauMsVBmo0P7xUFHQF6WSe5j1XE89GcCOx2_n1SKjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخوند حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم
.
وصل شدن اینترنت پایمال کردن خون رهبر شهیدمونه، با اینکار تن رهبری تو گور لرزید.
عوامل موساد باعث بازگشایی اینترنت شدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/IranProxyV2/8581" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?encryption=none&type=xhttp&security=tls&path=%2Fde&host=de.lezzatzone.ir&mode=stream-one&sni=de.lezzatzone.ir&alpn=h2%2Chttp%2F1.1&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول تست شده اوکیه
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/IranProxyV2/8580" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8579" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/IranProxyV2/8578" target="_blank">📅 13:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">vless://900ca7c5-6c69-4536-b0f8-efa4e3976016@51.79.89.68:443?security=&encryption=none&headerType=none&type=tcp#@V2rayngSeven
vless://ae0dd58e-e222-40bf-84ae-365a97532737@104.17.150.224:443?path=%2Falbum%2Fbt&security=tls&encryption=none&insecure=0&host=pagescm.freen15.cc.cd&type=ws&allowInsecure=0&sni=pagescm.freen15.cc.cd#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله منطقه ای، تست بزنید کمی صبرکنید وصل میشه براتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/IranProxyV2/8577" target="_blank">📅 12:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Proxy
✅
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
Proxy
✅
https://t.me/proxy?server=ui.geodns.info.&port=4455&secret=7nnjRIGHSb16xRkTAiDCXQk%3D
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/IranProxyV2/8576" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/IranProxyV2/8575" target="_blank">📅 12:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/IranProxyV2/8574" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">DE🇩🇪- SpEeD🧨.ovpn</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8566" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های OPEN VPN
❤️
🕖
اعتبار : 30 روز
🌐
لوکیشن :
🇨🇵
🇩🇪
🇬🇧
👉
بدون محدودیت حجمی
🔋
تست شده و متصل  - روی ایرانسل
🟡
📧
Username:
SDPXCQLdnbnQiGi
🔑
Pass:
@SoonTeam
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/IranProxyV2/8566" target="_blank">📅 12:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/IranProxyV2/8565" target="_blank">📅 12:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://t.me/proxy?server=78.47.67.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
این هم یه پروکسی دیگه، بدون فیلتر وصل بشین، فور کنید برای دوستاتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/IranProxyV2/8564" target="_blank">📅 11:33 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
