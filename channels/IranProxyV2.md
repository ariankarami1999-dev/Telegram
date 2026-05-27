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
<img src="https://cdn4.telesco.pe/file/stJz97vneS5eqPgSMRq50ojLF_tKflX9pUd-q6YKeKn3_K2UM_uCIhZSrxN4Ju6b64sGdy-ZodBXx4snqqCG8TqobfNr7fNoP1OkuCfg42Q92gCNaX9TqmUl4Zx1tOc9wkgZYSxV7R-xiW26W8Zd7_tG6CEdRlsEKFgUBqXQv9G3CVukSACDA0MXQg5uxc87tpXF0Rd7U7y7dxhzMax2afcPulptshM342Yhb4ThMBtPJunyG-frzDpiwAJp2CHr6sRDa3iagmM2CZF7UZjMZWbr2aJKKKCwhnUNXicyobYejQ8uAUD61ML_eE4WoLSE4_pyfkXnnVPuFHeWFJunKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40.7K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 03:12:00</div>
<hr>

<div class="tg-post" id="msg-8620">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 368 · <a href="https://t.me/IranProxyV2/8620" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
یکی از دلایل اصلی اختلال و کندی شدید اینترنت، سقوط سهم IPv6 در شبکه ایرانه؛ سهمی که از حدود ۱۲٪ به فقط ۰.۱٪ رسیده.
این افت باعث شده فشار شدیدی روی IPv4 بیفته و نتیجه‌اش رو حالا کاربران به شکل اینترنت ناپایدار، اختلال VPNها، ضعف شبکه موبایل و لگ شدید در بازی‌های آنلاین می‌بینن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/IranProxyV2/8618" target="_blank">📅 02:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⚠️
گزارش‌های اولیه حاکی از آن است که ایالات متحده یک عملیات دفاعی را در بندرعباس ایران انجام داده است
.
🔴
یک مقام آمریکایی گفت: «ایالات متحده برای حفاظت از منافع منطقه‌ای خود اقدام خواهد کرد و این بر آتش‌بس تأثیر نمی‌گذارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/IranProxyV2/8617" target="_blank">📅 02:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8616">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/IranProxyV2/8616" target="_blank">📅 02:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/IranProxyV2/8615" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/IranProxyV2/8614" target="_blank">📅 02:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8613">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/IranProxyV2/8613" target="_blank">📅 01:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8609">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8609" target="_blank">📅 00:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8607">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8607" target="_blank">📅 00:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR1Mx3HtujUlkfzDUe316IGj9CBkahdiZc0Fx1HFFaQyi1nwUKWI2E-kcneQiNB4HyrnqeDncGD91HbOENUrJVD_Jz7u4xubkpqkhDZXDhhHRdCnTQV-kNvrTvNFILPcZXZJSYKtzH78w1R0E3zBuVWcAHipFlVWckgxQ50ALtes5eX597TlEEAgsl934KdLY90m6m9EpVxh6kqpaRvSZs4r6n2piMc1iu_EJzP7al6zryK6vQyNVl4MeuZqXrIxakAcR6uyF_deblJeMe2Op5Nx-C7XRURgb2INcq4p-MoLSRds--B8gJJ0NRfkHWiRSkFZJTxe0S3rHpfMit7VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت :
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8606" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8605" target="_blank">📅 23:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اپ استور هم رفع فیلتر شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8604" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
گویا گوگل پلی تو اکثر مناطق وصل شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8603" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8602">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8602" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8601" target="_blank">📅 22:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8600">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/IranProxyV2/8600" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8599">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/IranProxyV2/8599" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/IranProxyV2/8598" target="_blank">📅 21:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8597">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/IranProxyV2/8597" target="_blank">📅 20:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8592">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/IranProxyV2/8592" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ترامپ درباره ایران:
آنها می‌گویند که بسیار تمایل دارند که به توافق برسند.
تا کنون به آن نرسیده‌اند. ما از این وضعیت راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با جدیت بسیار کم هستند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/IranProxyV2/8591" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8590">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ: ایران حتی اگه اورانیوم های خودشو هم تحویل بده هیچ خبری از کاهش و لغو تحریم ها نیست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/IranProxyV2/8590" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8589">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8589" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8588">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
پروکسی متصل سرعت قوی
❤️‍🔥
⚡️
👀
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/IranProxyV2/8588" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8587">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینترنت بین الملل در حال قطع؟
نت‌بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPN ها هستند. کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPN ها می‌باشد.
تندروها کار خودشونو کردن واسه همینه خیلیا نمیتونن وصل شن یا سرعت افتضاحه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/IranProxyV2/8587" target="_blank">📅 19:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8586">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avCXF3tkcx_v8zB_cQFCmQDZqTYc4_H1G5fZfCFutHHSXhqSAWOYbLvbMvdahFPb1oIwZMtM5I70gXSn3qwynQI0uEp45bPfBHrKHsqstxFcY2WvqCcJMJkU73P_zXXrEq8_9lRJhAvdbr6SsX6ejA_oIrVJzxqtu7wGXnpornvT8GN9tzMzNYseMbYMhRadvPCSQu4oCq8NOIpBhTkcGDIEQbolD6FZaMYkK0bo1982_Rk6vgxhidDuzxSKLVG5FHPvzT8L0hMpQAuIWoT_cvqexeAbozyXouBK0-kwz6Xes_STxxmQb89EyV1T4q5aa-Bj90kjaAnis0XtK6onOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/IranProxyV2/8586" target="_blank">📅 18:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8585">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/IranProxyV2/8585" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8584">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/IranProxyV2/8584" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8583">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?mode=stream-one&path=%2Fde&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=de.lezzatzone.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=de.lezzatzone.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
همراه اول تست زدم، اوکی بود، مابقی نت هارو خودتون تست بزنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/IranProxyV2/8583" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8582">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5kUesWC0-ePhixUd8-qYbfbXHLPM6syko4stUmuG7sYN9zuFI81OoZXBg1tZuiMXa2-JTToqiESZd662iYzadLORWdQlSbWVbfMiI8kRjbp047Gn5Wdpf8bUKIXBJ4LL73ICKDpMluRGGv-WiDvjfWNSNprPEfKhbl2QywP_lGQgsnyug3ILIQZNHwvZQTajzsX0Eem2EZ9Jbk-P8IoeQuCE98cwn8-NyHP2r8wrkxpruyX0eaY0mu0h_0mBWIm6JxvI7R3ok8tPxpnRfxCF7pDbmG3fGGYmqNzyH82p6qQy78DgF9Sv_vHm-aGEPkSWhBFX1N-22MazNZRAodaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه اول بعد از اعتراض کسانی که اینترنت  پرو خریدن و گیگی 40 هزارتومن بابتش پول دادن اعلام کرد در صورت تمایل میتونن  اینترنت خودشونو به حالت قبل برگردونن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/IranProxyV2/8582" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8581">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZjG21HHifsQjTF1W0JvX9kOw1eObTAs2Bjy5wfQakPGchqrIpVb3E7mMEoHlJPPp8c_D-X69CcpytQAJYhB7m5-qbdhgrJWfpTLkKhKf8JCGHTVUxBZqXzSbXyueDltmy8bnaLCjuf8iU32AP4qfGMiz79MWKd2rmnusS96HqAv7NfaCNj4JB5C0dKd8B01Bn-M8D6rdIcizZ4mGyxe7FgLFAwm5QHimvn6D4Vxyd75LKjB2x9TnARMrBTQfsDMvlH5D_8N4U0PhIdEDdk0qYza8VKsmS6fdxFBcjI-ISZKm4XoxPc_0lLqtiJHy-RGw98xBFuoEjdpP3z1n9BOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخوند حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم
.
وصل شدن اینترنت پایمال کردن خون رهبر شهیدمونه، با اینکار تن رهبری تو گور لرزید.
عوامل موساد باعث بازگشایی اینترنت شدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/IranProxyV2/8581" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8580">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?encryption=none&type=xhttp&security=tls&path=%2Fde&host=de.lezzatzone.ir&mode=stream-one&sni=de.lezzatzone.ir&alpn=h2%2Chttp%2F1.1&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول تست شده اوکیه
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/IranProxyV2/8580" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8579">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/IranProxyV2/8579" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8578">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/IranProxyV2/8578" target="_blank">📅 13:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8577">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">vless://900ca7c5-6c69-4536-b0f8-efa4e3976016@51.79.89.68:443?security=&encryption=none&headerType=none&type=tcp#@V2rayngSeven
vless://ae0dd58e-e222-40bf-84ae-365a97532737@104.17.150.224:443?path=%2Falbum%2Fbt&security=tls&encryption=none&insecure=0&host=pagescm.freen15.cc.cd&type=ws&allowInsecure=0&sni=pagescm.freen15.cc.cd#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله منطقه ای، تست بزنید کمی صبرکنید وصل میشه براتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/IranProxyV2/8577" target="_blank">📅 12:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8576">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Proxy
✅
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
Proxy
✅
https://t.me/proxy?server=ui.geodns.info.&port=4455&secret=7nnjRIGHSb16xRkTAiDCXQk%3D
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/IranProxyV2/8576" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8575">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/IranProxyV2/8575" target="_blank">📅 12:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8574">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/IranProxyV2/8574" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8566">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/IranProxyV2/8566" target="_blank">📅 12:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8565">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/IranProxyV2/8565" target="_blank">📅 12:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8564">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">https://t.me/proxy?server=78.47.67.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
این هم یه پروکسی دیگه، بدون فیلتر وصل بشین، فور کنید برای دوستاتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/IranProxyV2/8564" target="_blank">📅 11:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8563">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺بمب.npvt</div>
  <div class="tg-doc-extra">4.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8563" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/IranProxyV2/8563" target="_blank">📅 11:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8562">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/IranProxyV2/8562" target="_blank">📅 11:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8561">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyltvH4CuARwrNEmX7kty6To0WPx1QCPyL-y_h3qwFydzTuaTN8kbg7e8aVqOlEBXcbH6t5jgN40HOpHonyBQqMYk5UpfPuRoGSOcLVqK5CHdYs-CcDX49F2MpF8rQoNx2txbNGLr4I38JG28hcLdjf9-jbLMnHAnh0pFVIc_xmB2iLn5uIamMiu4cYS9igmUpwZgxklDd1FzP04KazsAzOFzb_xCA6oj_m77uvNblpfk26h6RAu0vCLfVUjMV-4Dbgf31Ycwdw2qXlFu-FYAt5LW6iD2SNh0-x_lalKPmaAnHH5KFaAi6YW5OIubWxWYlzyx81k4Z42Vi_upXTI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/IranProxyV2/8561" target="_blank">📅 11:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8560">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwo_94gkC3dtc5sH3RN6S44zafQLuSCiANF0z8sK-2xJ57ytUxJsTg2wCHXqOR2K7Ztryt85x5yUELVyDDmJO5vAM0tx9ra0iNzlFAg97FesnHfw_vRA07HFcL9nlhp3txLKlIP2cBxzD0t84AHw_j8N6PAs8-H--XvzyEN0Wv5ilp-kQdh_vtk2jZ-GBQyB0fwH-_wJOArnn6oOP7mgO95G9z_6pP26-JiB1rM3iZ6_oyd7ViYlKSH1Wnpa4oQuYWoEhyQAIdYMjEaQJgOA9cmK4aKY-k9rgSspLkCGKkmFO9k0Fa0kuA-JSGrfFOB-kw1ALJBJE0rmtAd4eS04aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/IranProxyV2/8560" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8559">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول وصل🔥.npvt</div>
  <div class="tg-doc-extra">22.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/IranProxyV2/8559" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8558">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk5nvGgeUXu1Yt6-Z43LQSpLkWnryB_fb-D-fgTLO40DFi0G8UWw0gIU8Ff2sROk93cDUx42uHGlZOeJ_qqPOXVwBJb3FQ-kSRUyLnCAlaYJwKW_1CcnZhk7kxi5KQoMfItNkHuasNzh0pqRv2d9iYSNMitOpUOXDKGvVIcS8yRCmdcCfyuMJ103Pb_ovkarCjJxQs2c7crzbH26_ibkPvHHzKX1XrczUiOf5sQOR8cbwKNfog2N_TZKWLxnxh1THoxzXVicAXcmaXow2Z2Gnvey5jKcBpgEd8anfISkSWaveJI5gnIjCu5y5UPc73r3CIdt2yARgF72sCy8ut06rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رس
ایی: عوامل موساد دستور باز کردن اینترنت رو دادن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8558" target="_blank">📅 08:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8557">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8557" target="_blank">📅 01:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8556">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇱🇷.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8556" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رو اکثر اپراتورها وصله، فور بزنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/IranProxyV2/8556" target="_blank">📅 01:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8555">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
😐
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/IranProxyV2/8555" target="_blank">📅 01:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8554">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQiu4eMPuM6i0fZZv1WeQ-BV2JyzCmpJacKx3qP3qB4ZawgiHcpSpASJf5aWgM4D3Ahly1q8QRV9yloBMJDQnIuBiwFvzLYahmAtjU-RWT1tIFHZHA35a00WpH0_1xz3RpiowJEWKSspj2I1nO785sSICY6QTRqZhul8Z1hLo8M6GRE4Bevg49zgcArP_xnM-0x6DH_VcVGd_yxcV6VDNdSIS1cljQA01vSE6MlZumiECJYjwFPYuxPcbx_8Do-HNNH_XFWuHudbH3ahG8GK4kBp4FSr5q0RWLz8dHpDISY3FWMfiG78p7yy66hP2B_GeOnBIForEz5wmZ18Eiz3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/IranProxyV2/8554" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8553">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/IranProxyV2/8553" target="_blank">📅 00:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8552">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
https://t.me/proxy?server=178.105.241.184&port=443&secret=99902e5742bd34a3f26434fadf88cde3
سرور وارد کنید، و بعد به پروکسی متصل بشید بصورت ترکیبی، رو همه اپراتور ها اوکیه، فور کنید دوستاتونم استفاده کنن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/IranProxyV2/8552" target="_blank">📅 00:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8551">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📣
دوستان، سرعت جوریه که نت قطع بود، سرعت بهتر بود
😐
😂
📌
درضمن، اینکه سرعت سرورهای تانل ربات پایینه نگران نباشید، برای همه به همین صورته و اختلاله کلا تو کل کشور ، حل میشه ، ولی خب پایداره و وصله، خواستین تهیه کنید تو ربات سفارشتونو ثبت کنید
🏅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/IranProxyV2/8551" target="_blank">📅 23:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8550">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/IranProxyV2/8550" target="_blank">📅 23:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">vless://b64ced11-143e-4ded-a985-a8de25461061@3.27.234.120:51808?security=reality&encryption=none&pbk=XHnwfyEySdx57QT_8P_7vDVFzdLHO4tO9BQOsHxxlEk&headerType=none&fp=firefox&type=tcp&flow=xtls-rprx-vision&sni=yahoo.com&sid=8810c789eea55c28#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل به همه اپراتور ها، بفرستین واسه دوستاتون هم اونا وصل شن، هم از ما حمایت ریزی بشه
❤️
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/IranProxyV2/8549" target="_blank">📅 23:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">vless://28154b7e-afc2-449b-8a78-bf1eba31bd05@a.darafiq.ir:8880?path=%2F&security=none&encryption=none&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل با همه اپراتور ها، فور نکنید حمایت نشه حلال نیستا
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/IranProxyV2/8548" target="_blank">📅 23:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۲ تا کانفیگ دیگ هم ساختم، رو یکی نباشین مختلف بزنید که سرعتشون نیاد پایین یا قطع نشن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/IranProxyV2/8547" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">vless://abe09a99-7346-4c5b-9476-16774c032ae7@104.16.89.120:443?path=%2FTelegram-%40IranianMinds&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=1&fp=chrome&type=ws&allowInsecure=1&sni=mcia.po2pco.top#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رایگان جدید رو همه اپراتور ها وصله، استفاده کنید بزنید، فور کنید برای دوستاتون چنلو داشته باشن، حمایتتتت
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/IranProxyV2/8546" target="_blank">📅 22:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/IranProxyV2/8545" target="_blank">📅 22:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/8544" target="_blank">📅 21:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8543">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=PRnxk8cii9JCL5mhBpWY06Bkq-HMv39orKSU2MsU7B6PBFfzGSY33L7by1YNyZYq7LyjgutrogkVU87nkXjRGHRTvQo3wLo-SehuU2mS1FJDTm14NK27Mf5keaT8t9Lyfx5QpEJUffiaspZ3mqbMSNzvXpqVkW96Q3qwIOAa5v9tQsAspeG080PfN1bBUfGoB67ZPYouEhnktihDaVZS-1y4KjCiF6w7YUbx0tfmBLlIM1KVeFNvUOy16Dh2agTS0FNbFHOGtmXryifFXmjWILR9Yi5IzTwsPw_3cm4a6mQqM7pUz4Mw7eUF8Xa4yY9GeLtb0tYn9uHc8d0QNWhRRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=PRnxk8cii9JCL5mhBpWY06Bkq-HMv39orKSU2MsU7B6PBFfzGSY33L7by1YNyZYq7LyjgutrogkVU87nkXjRGHRTvQo3wLo-SehuU2mS1FJDTm14NK27Mf5keaT8t9Lyfx5QpEJUffiaspZ3mqbMSNzvXpqVkW96Q3qwIOAa5v9tQsAspeG080PfN1bBUfGoB67ZPYouEhnktihDaVZS-1y4KjCiF6w7YUbx0tfmBLlIM1KVeFNvUOy16Dh2agTS0FNbFHOGtmXryifFXmjWILR9Yi5IzTwsPw_3cm4a6mQqM7pUz4Mw7eUF8Xa4yY9GeLtb0tYn9uHc8d0QNWhRRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ، خداحافظ
👋
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/IranProxyV2/8543" target="_blank">📅 21:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8542">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید، خوشتون اومد فور کنید
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/IranProxyV2/8542" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8541">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?path=%2F&security=tls&encryption=none&insecure=1&host=sni.111000.indevs.in&type=ws&allowInsecure=1&sni=sni.111000.indevs.in#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
کانفیگ با پورت های متفاوت براتون میسازم، سعی کنید همرو تست کنید، ببینید با کدوم راحت تر هستین، حتما برای دوستاتونم بفرستید
✅
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/IranProxyV2/8541" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8540">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@104.16.7.70:443?mode=stream-one&path=%2Fde&security=tls&encryption=none&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=de.xn--q9jyb4c.online#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
چند ثانیه صبرکنید وصل بشه، هنوز پهنای باند اونقدری زیاد نیست که پرسرعت وصل بشه، یادتون نره فور کنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/IranProxyV2/8540" target="_blank">📅 20:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8539">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">vless://8b84b146-3405-44f2-98e4-f0ac7dbad0c0@104.17.147.22:80?mode=auto&path=%2FTelegram%40SoonTeam&security=none&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=uk.im-eb.cc.&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
سرعت عالی، رو همه اپراتورها، بفرستید واسه دوستاتون وصل بشن، حجم نامحدودههههه
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/IranProxyV2/8539" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8538">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همه اپراتور ها متصله، وصل شین لذت ببرید
✅
حجمممم نامحدودددد
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/IranProxyV2/8538" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8537">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@172.64.152.23:443?path=%2F222.167.202.31%3A7443&security=tls&encryption=none&insecure=1&host=2026.hhhhh.eu.org&type=ws&allowInsecure=1&sni=2026.hhhhh.eu.org#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو تمامی اپراتور و نت های همراه وصله
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/IranProxyV2/8537" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8536">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👑
اینترنت ایرانسل و همراه اوکی شد و باید فیلترشکن های رایگان برایتون وصل شده باشه
❤️
🛜
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8536" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8535">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول متصله
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/IranProxyV2/8535" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8534">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
اینترنت بین الملل روی خطوط همراه اول هم وصل شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8534" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8533">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانفیگ رایگان برای وایفا
✅
vless://4493268e-2083-4a18-9c24-72c1f8f604d5@92.42.203.168:443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=dl-server1.tpchat.ir&fp=chrome&type=ws&allowInsecure=0&sni=dl-server1.tpchat.ir#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8533" target="_blank">📅 20:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8532">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8532" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8531">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8531" target="_blank">📅 20:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8530">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پروکسی وصل
✅
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/IranProxyV2/8530" target="_blank">📅 19:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">vless://fe23b0d9-ab91-4f7b-a5a4-89e4ae9b094e@www.speedtest.net:443?security=tls&sni=broken-mud-0a9a.rigacihir69.workers.dev&alpn=http/1.1&fp=chrome&type=ws&path=/eyJqdW5rIjoiZEFtaFJ6RlAiLCJwcm90b2NvbCI6InZsIiwibW9kZSI6InByb3h5aXAiLCJwYW5lbElQcyI6W119?ed%3D2560&host=broken-mud-0a9a.rigacihir69.workers.dev&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله، رو وایفاها
✅
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8529" target="_blank">📅 19:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر ارتباطات:
اینترنت همراه تا امشب وصل میشه، تا فردا اینترنت به قبل از دی برمیگرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8528" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📌
بزنید تو نپستر با ایرانسل تست کنید
🛜
ss://YWVzLTI1Ni1nY206WldZeVlUVTBZV1k0T0dNME5EUmhabU0xWkRRMFpqRTNNR0l5Wmpneg@ir.npvnot.com:10112#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/8527" target="_blank">📅 18:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8526">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔸
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8526" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
آمار لحظه‌ای وصل اینترنت کشور
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
‌پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
‌افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
‌همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8525" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8524" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از اونایی که پرو خریدن چه خبر
😂</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8522" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8520">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✈️
دوستان اگه در راستای قطع شدن بودین و وایفا نداشتین میتونید از ربات ثبت سفارش انجام بدین، آنی تایید خواهیم کرد و اینکه درنظر داشته باشین،
اطلاعیه
رو حتما مشاهده کنید.
📌
در صورتی که نت بین الملل بازگشایی شد، تمامی کاربران که از ما سفارش فعال دارند، به دیتاسنتر خارج منتقل خواهند شد و به ازای هر 1 گیگی که خریداری کرده بودند، 3 گیگ اضافه خواهد شد
❤️
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8520" target="_blank">📅 17:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">😼👊🏻.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8519" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تست کنید، منطقه ای وایفا
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8519" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این پروکسی های تلگرام هم داشته باشید فعلا با مخابرات و برخی اینترنت های خانگی متصلن:
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
ممکنه منطقه ای باشه، بهتره تست کنید.
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8518" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎁
بفرستید واسه دوستاتون
❤️
vless://27d6de57-240b-400e-a036-192608ae0459@mbv.followern.ir:443?encryption=none&security=tls&sni=tino.protag.ir&fp=chrome&insecure=0&allowInsecure=0&type=ws&host=tino.protag.ir&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله رو وایفاها، قلب بزنید ببینیم چندنفرید، برا دوستاتون بفرستید که وصل نیستن تک خوری نکنیدا
😶
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8517" target="_blank">📅 17:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درنظر داشته باشین که فعلا درحال حاضر تنها وایفاها وصل شدن مث مخابرات و آسیاتک، شاتل و... اونم بصورت منطقه ای، مشخص نیست اینم اختلال باشه یا اپدیت فایروال باشه، پس صبور کنید تا همچی مشخص بشع، فعلا اپراتور های همراه مث ایرانسل، همراه اول و رایتل و... وصل نشدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8516" target="_blank">📅 17:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
پروکسی متصله، رو وایفا و مخابرات منطقه ای دوستان عزیز، اگه وصل نشد تو منطقتون ذخیره کنید داشته باشینش، صبور باشید شایدم اپدیت فایروال مشخص نیست هیچی
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8515" target="_blank">📅 16:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو وایفا و مخابرات وصله
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8514" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مجدد بستن پهنای باندو
😐</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8512" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5ywkJkdGYcdmY2JvIvDsSUNdZ5J3DztNjvSbdwcSCuQjD9zy3XlqNUqW6uH1qb4OgI2BWhNkPCfslS4WF3Jzxa6OCJ2cFyVrIZfYJOP_7w1vL8LmVVLF0nVH-FMwxKHcSG-QFx_iI09gZTeRSB29_lQXr6HRze6lVfi3ka53eTvHz8ccz9P0A7EEJ1Dmc30dX96sfAK0vrOQR5VdS5Yt4E2D-Rwtm9xhploW8t836vDJEUVMGZnWiFneDpLRSnV9bp1oAHSvALNsNylvTJcVZYFKsrfimrFvs8DnLEWEdSWOiltUHZSWdmpT9xnkVZzVm5m6vT6e9LBkBeqGdYS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/IranProxyV2/8503" target="_blank">📅 14:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روح و روانمون بگا رفت، از بس حرفای چرت و پرت تحویلمون دادن، رسما دارن مردم خر فرض میکنن و پاسکاریمون میکنن، من یکی که دیگه مخم نمیکشه حرفای اینارو باور کنم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8502" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVjkRZLTs-W97FFOOeMAsy1aj1UuuKbdrZLFbHoDOYh0X0OVuU_Aci5U0HrvvYpxigqEI5kAeefR2YiigPhpNKRBXBlfBgJAxvK6F2p_jleIfghHJhQ53H9njT4k3yOo60kRP3CF0wUlbHHyQqeMEqkSfJMessbhUotGokyO2YFRs_XwVlwoJS9p7I8WiRHKkDFPDrFKUMkIY4Eiu8rMPtbZ4cQyhqYCNCZMH5x7s7zRjV7nkoBCOhC4hfXVwoAwrn03QePdZkNyZlhLz50hf71Wp8LEqk5GJkXKOFZX_JkFzKAEfMcDi60-EYZUBNMty0jQUOJjViQpbM12U_0wBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا حتی ذره ای تکنولوژی سردرنمیارن با اون کلشون
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/8501" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8500" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رئیس جمهور کشور اگه تا آخر هفته اینترنتارو باز کرد که کرد اگه نتونست بنظرم استعفا بده بهتره چون نه اونوریا حسابش میکنن که ترورش کنن حتی نه اینوریا حسابش میکنن
اونور دنیا رئیس جمهور یه کشور ناو میفرسته یه دنیارو بگا داده بعد اینجا رئیس جمهورش اینترنتم نمیتونه وصل کنه
جدی اگه نتونستین وصل کنید خودت و کل کابینت بنظرم استعفا بدید یه موز بزارید رو صندلی بجای خودتون حداقل فایده اش اینه موزه پتاسیم داره ولی شما همونم ندارید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8499" target="_blank">📅 14:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فارس: چندین نماینده مجلس که عضو جبهه پایداری و تندرو هستند درمورد مصوبه شورای فضای مجازی شکایت کردند و دیوان اداری دستور داد اجرای بازگشایی اینترنت متوقف شه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8498" target="_blank">📅 13:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پزشکیان داداش نقش تو چیه دقیقا تو کشور</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8497" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWzeE7l2EocnFOdN8ZmCYUCh5CKPIaJeCihobltO2tcl1ZLkdVCdfh-Frbcil1t1YoOt_SpLQ-ZJDlG2ylZOX7DkQw6zRJpZClLjJDa1e6tmzUXNiGCkNV0n2AzJmZDFyV6nAL_---Mv6FxlWqAl5sIKt6JxbZLbzZPomUK6AFhwC150PwJiCLT5cmGe1XAeAa5K9MnBNjR_GeVHyuPHAn92KsbHkKN9yMyHYDFg76OPAHtxKo9G5HXh2l_DsRngzgfFV0oLbWk0In1QEULPQYTyrvQN8QT-MxTYzgwXhzJZlEjrfg3a9KGhyA7IAbzhVpkZoArgrm1VUZMJlrIKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8496" target="_blank">📅 13:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8495" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی با خواسته ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» مصوب ۱۴۰۵/۲/۲۲ رئیس‌جمهور، هیأت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت مطروحه صادر کرد.
حرومزاده ها یعنی چی، هی پاسکاریمون میکنید، بخدا خسته شدم دیگه
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8494" target="_blank">📅 13:37 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
