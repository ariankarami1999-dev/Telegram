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
<img src="https://cdn4.telesco.pe/file/Oqe5BVaTAGytS1H7e0wiDACyV9cUVR48IMCqMDGZ_N045Yt8AnhZN9vl9Uw2Lg_QPBtdcr7pwpc3rLCbaDqFw5hAn2ZWnuYr8srwYve0oAjs-hye2AMQiP_6-wszFxTBwC62-qnc5Hrvv8UoTtEMHpu5NfEQ_ZGcfjgaJ6FF2DnLbm8xBnxQLJUvDCHv6g44LDoLYg00bLyNGHlpxrjoo4y6bkWXvohyTukW1wePZsWcqkqv6dfJTDf-R6UaTvyT4DGsapN9b671ulv44Wmqf_2L6RDkTvLKK-O1wSl-6qiESu501xjLupWxAf_HctM_yTo8gAHA62HtuWOoOQm5Hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 260K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 01:20:59</div>
<hr>

<div class="tg-post" id="msg-11354">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات آمریکا:
دستیاران ترامپ برنامه‌هایی رو برای بازگشت به حملات نظامی به ایران آماده کردن، اگر او تصمیم بگیره با بمباران بیشتر از بن بست خارج بشه.
از جمله گزینه‌ها، اعزام نیروهای ویژه به ایران برای هدف قرار دادن مواد هسته‌ای مدفون شده است و ممکنه از نیروهای ویژه برای کنترل جزیره خارک استفاده بشه.
@withyashar</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/withyashar/11354" target="_blank">📅 01:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRp3u062d5Q3JgITttJkkRLoqQh-54luzkieqw9KlWGSc6eKBNEIhh2gFN4xMPi5igkBD9sGKBlwA-No91CrrAx0TvWddYeD7bSK51Ir_rmtEc0gJT2BDetzf34j2Q-5G-B3cLitfKiEaS050eXZhgFEj8teJH-FM_Pcr0KCWEkmp9N5FnamQu20JH1gdlbLKVgW_MPSoiMnsgampVmKj5E7cmaHGurit_-wOtbpSzsWYgeU2hdvndhj5qJSbmN9IBhd3Mp6T33l6xkzxXOxkvli2dJIrVQ4RYz3dOiN0jN_6NuOp-2ERI9G_jy9Oy5cs-XkudPfEVSQ_xKk2kHirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد جدید مجله تایم: چگونه دیدار ترامپ و شی، نظم نوین جهانی را نشان داد
@withyashar</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/withyashar/11353" target="_blank">📅 01:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ خیلی عجله داشته هیچ فیلمی عکسی از رسیدنش نیومده بیرون ! عجبیه</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/11352" target="_blank">📅 01:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11351">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11d28292.mp4?token=eFW9_EdNj6siI-q4b3qj3oq54V-KRDp62j27VDztisvDUCt98nxkMuKBqDCXAt4lAhiS_AHue8Pqgf8Zv1Mv-T2A_gDfDumjikTYKFyAkv5jDN2zgFds5ItfdXJxECPp82VwdCW9N8LtXJvm9SKSbZa19jBw5zxJgyrR49262iBsv9P8_yRDPo6P7XkXZupfjXY0lU-7P8UjW2LafnLfkdSGZAjdAIOdFbHzjz8q4NYuRne4YYzh6owdYFJ3RPK80ojVau-e2FvjXlFXqM-2yCaK5MzwLGCr6rmnm2gXkXJjtupMZTZR9cBHHuV3x1TZ0Dfvc10PW7sldErWVr4TzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11d28292.mp4?token=eFW9_EdNj6siI-q4b3qj3oq54V-KRDp62j27VDztisvDUCt98nxkMuKBqDCXAt4lAhiS_AHue8Pqgf8Zv1Mv-T2A_gDfDumjikTYKFyAkv5jDN2zgFds5ItfdXJxECPp82VwdCW9N8LtXJvm9SKSbZa19jBw5zxJgyrR49262iBsv9P8_yRDPo6P7XkXZupfjXY0lU-7P8UjW2LafnLfkdSGZAjdAIOdFbHzjz8q4NYuRne4YYzh6owdYFJ3RPK80ojVau-e2FvjXlFXqM-2yCaK5MzwLGCr6rmnm2gXkXJjtupMZTZR9cBHHuV3x1TZ0Dfvc10PW7sldErWVr4TzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/11351" target="_blank">📅 01:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11350">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حوس لوبیا پلو کردم
😅
امشب که بیداریم درست کنم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/withyashar/11350" target="_blank">📅 00:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11349">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ در تروث : تینا را آزاد کنید
@withyashar
تینا پیترز یک مقام انتخاباتی سابق آمریکاست که به‌خاطر دخالت غیرقانونی در سیستم‌های رأی‌گیری بعد از انتخابات 2020 زندانی شده و حالا ترامپ از او حمایت سیاسی می‌کند</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/withyashar/11349" target="_blank">📅 00:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11348">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/withyashar/11348" target="_blank">📅 00:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11347">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/withyashar/11347" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11346">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/withyashar/11346" target="_blank">📅 00:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11345">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیویورک‌تایمز به نقل از ۲ مقام امنیتی:
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه جمهوری اسلامی هستند،
این حمله ممکن است از هفته آینده آغاز شود
@withyashar</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/withyashar/11345" target="_blank">📅 00:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11344">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه مسیج درست اگه تو دایرکت دیدی به من بگو ! انگار‌من کشیش کلیسام ! یا کلانتر محل !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/withyashar/11344" target="_blank">📅 00:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11343">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer"><a href="https://t.me/withyashar/11343" target="_blank">📅 00:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11342">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">امشب حمله‌ست؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/withyashar/11342" target="_blank">📅 00:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11341">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSea</strong></div>
<div class="tg-text">امشب حمله‌ست؟</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/withyashar/11341" target="_blank">📅 00:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11340">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYG02iHJlF3X-wrijhFXyar630gg7OuIJHa8smEOBCnK8as-FZx6B5Xhwif0R_Qc6sBH74xtQtDLJR9Q9pxqq3YJkRQjSW2duSqibepHtMvswJXu94C_BBQy3Z5dmzFeP7iOz1ib1Zf-SKPI007LPHwzTyk061tjK6mT79cO7E4CCwA8_LaTZpEHoJeo4tqUAfAdmz-HsG2Z7PuFKV7-CZBipCo8kMxofje8MbJJ5yts22Ykr0faN9Js3uUJmZcrN4WRWOM7Pth4j29yErkmuCcnPdiUnN5SphVP77EfRjqI-Qw_fMH5x6HHQUcQelGWUydcCFI3pU84WPAZV2d1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما هم میدونه چی میشه داره آموزش کار با سلاح رو میده
😂
اینا رفتنین شک نکنید
👋🏾
👋🏾
@withyashar</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/withyashar/11340" target="_blank">📅 00:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11339">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگه امشب شب‌زیبایی‌نبود و امید نبود الان رد میدادم ! با این پیغام هایی که دایرکت میاد</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/withyashar/11339" target="_blank">📅 00:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11338">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">عمو یاشار ما امشب منتظر اومدم اومدمیم
😂
🫡</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/withyashar/11338" target="_blank">📅 00:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11337">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یاشار یچی خواستم بگم روم نشد ولی کلاهبرداریه اگه امکانش بود اطلاع رسانی کن  ما پیوی ینفر رفتیم برامون خاله جور کنه واسه معرفی ۲۰۰ از ما گرفت بعد شماره طرفو داد گفت یک میلیون ۳۰۰ دیه برامون بزن گرفتیم براش زدیم بعد اومد گفت برای تضمین ۱۳ میلیون بزنید بعد اینکه…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/11337" target="_blank">📅 00:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11336">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahd</strong></div>
<div class="tg-text">یاشار یچی خواستم بگم روم نشد ولی کلاهبرداریه اگه امکانش بود اطلاع رسانی کن
ما پیوی ینفر رفتیم برامون خاله جور کنه واسه معرفی ۲۰۰ از ما گرفت بعد شماره طرفو داد گفت یک میلیون ۳۰۰ دیه برامون بزن گرفتیم براش زدیم بعد اومد گفت برای تضمین ۱۳ میلیون بزنید بعد اینکه کارتون تموم شد برش میگردونم حالا ما بهش گفتیم ۱۳ میلیون از کجا بیارم گفتم کنسلش کن ۱۳۰۰ بهمون برگردون اومده میگه اون مهریه بوده دیگه میره برا خالهه
ولله به این پفیوزا اعتماد نکنید اگه امکانش هست بزار چنلت بقیه هم در جریان باشن</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/11336" target="_blank">📅 00:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ رسید آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/withyashar/11335" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11334">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیویورک تایمز: آمریکا محمد بکر سعید داود السعدی، فرمانده ارشد شبه‌نظامی گردان‌های حزب‌الله درعراق، رو دستگیر کرد و علیه‌اش کیفرخواست صادر کرد.
او متهم به طراحی حداقل 18 حمله در اروپا، آمریکا و کانادا از پایان فوریه شده؛ این حملات به عنوان انتقام از حملات آمریکا و اسرائیل علیه جمهوری اسلامی برنامه‌ریزی شده بودن.
@withyashar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/withyashar/11334" target="_blank">📅 23:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7f890274.mp4?token=cE_ewtMU91S2W8Fzx6ES4uR9MWOq3Ie1_8i9yXeEUPDqIEDhuvb7TuXlkICkpSi5AYpvqU-UxmeIRTuw7RXOIxQGLVmHzI0V-5fHBKM0P8ul8sPNIwkzJy1qjzTQptn-IBIJmhC5a_5Oqg-iyvbyAPefPgtBzKwnOOPM5zmVRBpfjHfgLdyXrD9XJ7sWUBB6dXvWuK9AyCxZ1ohxdLNCN8JLu1JTvdhbdLj6fLNBNIahVyn_yH0opQb_RRMPFktkPOquO-reoerYCKwtiIfdsyI14LsGJm_q6yZCJXbu2XGu8UaC2FqnHmSwJUHOOM1q_IBwkpnWyJuFs7XKRqV-CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7f890274.mp4?token=cE_ewtMU91S2W8Fzx6ES4uR9MWOq3Ie1_8i9yXeEUPDqIEDhuvb7TuXlkICkpSi5AYpvqU-UxmeIRTuw7RXOIxQGLVmHzI0V-5fHBKM0P8ul8sPNIwkzJy1qjzTQptn-IBIJmhC5a_5Oqg-iyvbyAPefPgtBzKwnOOPM5zmVRBpfjHfgLdyXrD9XJ7sWUBB6dXvWuK9AyCxZ1ohxdLNCN8JLu1JTvdhbdLj6fLNBNIahVyn_yH0opQb_RRMPFktkPOquO-reoerYCKwtiIfdsyI14LsGJm_q6yZCJXbu2XGu8UaC2FqnHmSwJUHOOM1q_IBwkpnWyJuFs7XKRqV-CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه خداحافظی ترامپ با شی و خوشحالی او از سفر موفقیت آمیزش
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/11333" target="_blank">📅 23:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7aab5fc3.mp4?token=t_MIYOdba2bdzSz_ciXaXwPwOl1HCfI1eTuAPldHEzmd1t_69_azeb3HB0EHWHe3jxBnntFEzImO65rb-K6ldX9oG_0IvLfgzL21Cif5TxiwiNi3mMxOLwlnKF6YauKrN4MN7GSj-B2GKtl6pyLxHz4eFKUl2Kc7JbbmXcwI1-UjYv8i5Xceo7TOQEw6YHeC65uevrI8-1tdf7w9rgUwz7YIiOD1dcBLB6ebgeBV9-8dWCVRcBTh3S5hOkRtyWcFTLM4m9iTofniQFPRGV8g5BE2yAm8wocNI6AsbD9NZdCBVAY5TC-GUFeoTF_C9V2tiqx4A61WJL3Xu3RGE7Adkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7aab5fc3.mp4?token=t_MIYOdba2bdzSz_ciXaXwPwOl1HCfI1eTuAPldHEzmd1t_69_azeb3HB0EHWHe3jxBnntFEzImO65rb-K6ldX9oG_0IvLfgzL21Cif5TxiwiNi3mMxOLwlnKF6YauKrN4MN7GSj-B2GKtl6pyLxHz4eFKUl2Kc7JbbmXcwI1-UjYv8i5Xceo7TOQEw6YHeC65uevrI8-1tdf7w9rgUwz7YIiOD1dcBLB6ebgeBV9-8dWCVRcBTh3S5hOkRtyWcFTLM4m9iTofniQFPRGV8g5BE2yAm8wocNI6AsbD9NZdCBVAY5TC-GUFeoTF_C9V2tiqx4A61WJL3Xu3RGE7Adkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک والتز، سفیر آمریکا در سازمان ملل ، می‌گوید که یکی از «نتایج بزرگ» سفر ترامپ به چین این بود که چین موافقت کرده از ایران فاصله بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/11332" target="_blank">📅 23:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منابع عبری :
گویا ترامپ با یک حمله محدود جهت فشار بر سر تسلیم شدن موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/11331" target="_blank">📅 23:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">واشنگتن پست: جمهوری اسلامی واضح‌ترین بازنده دیدار ترامپ از پکن است، با مخالفت علنی پکن با اختلال در هرمز، تعهد به عدم ارسال تجهیزات نظامی به تهران و توافق بر اینکه تنگه «باید باز بماند.»
@withyashar</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/11330" target="_blank">📅 23:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">l وزارت خارجه آمریکا اعلام کرد آتش‌بس میان لبنان و اسرائیل به مدت ۴۵ روز دیگر تمدید شد.
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/11328" target="_blank">📅 22:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11327" target="_blank">📅 22:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed7b9efa.mp4?token=MP-6Hi19bpS1Rzeb7lgpiQnIIFrugf7OncOPT8BFGfyeBNhaqsGH9k7Wvu4-Fyem9FuvzinV1KdYCX_6LYlMFmEDGQ6XnVYnmNNsaMN-Ci4Za2Harb5CHRc5tfWzPh-ZHYL56fcsiYCT7mAp7B4-F2w8nlGRUngDxo8HQt3fOyOB9DRctJmrgR-cEkOskqbPA5pGF3OaA64LNJctkgKWQ6uMUCboWUdSc14WVRBmqGhT_sc7qNZYyCbSd3PlPnh5SzdaCCFSUC6We3fM1gVDUytyRLC29HeVLBfUExQWgQRFnUHDk5LhcajJh_bV_-3_kbbcsLnpJVuQZJ-NqjgM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed7b9efa.mp4?token=MP-6Hi19bpS1Rzeb7lgpiQnIIFrugf7OncOPT8BFGfyeBNhaqsGH9k7Wvu4-Fyem9FuvzinV1KdYCX_6LYlMFmEDGQ6XnVYnmNNsaMN-Ci4Za2Harb5CHRc5tfWzPh-ZHYL56fcsiYCT7mAp7B4-F2w8nlGRUngDxo8HQt3fOyOB9DRctJmrgR-cEkOskqbPA5pGF3OaA64LNJctkgKWQ6uMUCboWUdSc14WVRBmqGhT_sc7qNZYyCbSd3PlPnh5SzdaCCFSUC6We3fM1gVDUytyRLC29HeVLBfUExQWgQRFnUHDk5LhcajJh_bV_-3_kbbcsLnpJVuQZJ-NqjgM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/11326" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">میگم فالورایه شاهزاده داره کم میشه قبله جنگ ۹.۹ بود الان ۹.۷ شده</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/11325" target="_blank">📅 22:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirali</strong></div>
<div class="tg-text">میگم فالورایه شاهزاده داره کم میشه قبله جنگ ۹.۹ بود الان ۹.۷ شده</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/11324" target="_blank">📅 22:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/11323" target="_blank">📅 22:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-hnFff_Iw_-noMHXrV3f7UYKid5EmP8ZdK28lkrW8d-Vxuoh9R2SzdmWmilbWUKxxc_7iTOEqty7qaCzbTl4ZDHDqs7j9CaXdBQq04yfxCLqOg-A98uU6J62n__3xEhwIVM-VqtOozR3BuPUj6rCKB2UOIEKYQ4qdZnRyc3Mw7PPDd06tyX-b8AyT7BPOKRXhDYXzpqskwgtKZB-RYbIpQzl4m6jz_JORp1oCmgOpWfqg47dgPtWHz1HlOPgOHk8O-Xhd6-zDVO9Q2QoN8sLBj_G5uFJ8fUq7NWWML_udxjWTmpeBpB8QMlY5L8sjSjKGQIzSMU5ZbK0iXZ7aij8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ آ۴ هست!
واقعیت اینکه شاید الان بشه جلوی اتصال به اینترنت رو گرفت ولی تا چند سال آینده عملا غیرممکن میشه!
@withyashar</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/withyashar/11322" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هادی چوپان، در یک مسابقه استعدادیابی که از صدا و سیمای رژیم پخش می‌شود،  گفت: «ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم.»
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11321" target="_blank">📅 22:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاهزاده رضا پهلوی : هم‌میهنان عزیزم،
در روزهایی که شما با شجاعت در برابر رژیم اشغالگر ایران ایستاده‌اید، این نظام منفور و منزوی، همچنان به تجاوز به جان و مال مردم ادامه می‌دهد تا سرنگونی حتمی خود را اندکی به تعویق اندازد. در چنین شرایطی، وظیفه خود می‌دانم که تصویر عدالت در فردای ایران را برای کسانی که با جنایتکاران همکاری کنند، روشن‌تر ترسیم کنم.
در این راستا، از «کمیته‌ تدوین مقررات عدالت انتقالی ایران» خواستم درباره‌ دو موضوع مهم، نظر مشورتی خود را ارائه کند: نخست، موضوع مسئولیت کیفری افرادی که با ساختارهای سرکوبگر جمهوری اسلامی همکاری می‌کنند؛ و دوم، موضوع مصادره‌ اموال معترضان و خانواده‌های آنان.
@withyashar
این کمیته اکنون نخستین نظر مشورتی خود را صادر کرده و پیام آن روشن است: این اقدامات، همکاری‌های ساده یا بی‌اهمیت نیستند؛ بلکه «یاری‌رسانی به جنایت علیه بشریت» محسوب می‌شوند. هیچ مقام، هیچ دستور و هیچ بهانه‌ای نمی‌تواند مسئولیت کیفری فردی را از میان ببرد. بنابراین، هر فردی که آگاهانه و داوطلبانه با ساختارهای سرکوبگر رژیم همکاری کند، چه در داخل و چه در خارج از ایران، باید بداند که در معرض مسئولیت کیفری قرار خواهد گرفت:
خواه این همکاری از نوع گزارش‌دهی یا خبرچینی باشد؛
خواه از نوع مشارکت در ایست‌های بازرسی‌ باشد؛
خواه از نوع به‌کارگیری کودکان و نوجوانان در سرکوب معترضان باشد؛
و خواه از نوع تحصیل، انتقال یا خرید و فروش اموالی باشد که در جریان سرکوب از معترضان و خانواده‌های آنان مصادره شده‌ است.
@withyashar
از این رو، نه‌تنها افرادی که در صدور دستور، اجرای آن، یا تسهیل این مصادره‌ها نقش دارند در معرض مسئولیت قرار خواهند گرفت، بلکه کسانی که آگاهانه و داوطلبانه به خرید و فروش این اموال می‌پردازند نیز باید پاسخگو باشند. این مسئولیت، استفاده از اموال یا دارایی‌های آنان برای جبران خسارت واردشده به مالکان اصلی را نیز شامل می‌‌شود.
بنابراین، به همه‌ کسانی که امروز در صدد همکاری با دستگاه سرکوب رژیم هستند هشدار می‌دهم: پیش از آن‌که دست به اقدامی بزنید که به مردم ایران آسیب جانی، مالی و یا اجتماعی برساند، به آینده‌ خود و خانواده‌تان بیندیشید. به آن روز بیندیشید که ایران آزاد خواهد شد؛ روزی که حقیقت پنهان نخواهد ماند؛ روزی که اسامی آشکار خواهد شد؛ روزی که هیچ متجاوز و جنایتکاری از پاسخ‌گویی در برابر قانون در امان نخواهد ماند.
آن روز، ملت ایران حکومتی خواهد داشت که حقوق ایرانیان را محترم می‌دارد و ایران را به سرزمینی آزاد و آباد بدل می‌کند.
پاینده ایران،
رضا پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/11320" target="_blank">📅 21:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11319">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11319" target="_blank">📅 21:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سازمان سازمان مجاهدین خلق ایران (که در آمریکا با نام‌های MEK یا PMOI شناخته می‌شود) به‌صورت رسمی در تاریخ ۲۸ سپتامبر ۲۰۱۲ از فهرست «سازمان‌های تروریستی خارجی» وزارت خارجه آمریکا خارج شد. این تصمیم توسط وزارت خارجه دولت هیلاری کلینتون اعلام شد و همان روز اجرایی گردید
@withyashar</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/11318" target="_blank">📅 21:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/11317" target="_blank">📅 21:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAM</strong></div>
<div class="tg-text">یاشار مجاهدین الان دارن از کجا تغذیه میشن؟</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/11316" target="_blank">📅 21:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/11315" target="_blank">📅 21:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آخرین فیلم مخفی وحید بنی عامریان، نخبه ریاضی در زندان اوین که از دفاعیه اش در مقابل بیدادگاه آخوندی می گوید. وحید روز 15 فروردین 1405 اعدام شد @withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11314" target="_blank">📅 21:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11313" target="_blank">📅 21:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSALIH</strong></div>
<div class="tg-text">یاشار مجاهدین خیلی دارن به دانشجو های داخل ایران پیام میدن، واسه خودم تا الان از دو نفر مختلف پیش اومده، شروع میکنن به توضیح تاریخچه خودشون و همه چیزای خوب رو هم میچسبونن به خودشون و فلان
نمیدونم چه پروژه ای راه انداختن ولی از طریق</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11312" target="_blank">📅 21:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11311" target="_blank">📅 20:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRst28a0dtbUsvJB3T5E1trxwF6KZmblRld5CGlsTwoR8AeVXNrgIMlT0AFOQrQqHPuc2oLQ0yB1hX3qgHM_SPZh0xr5x1QmqJ1XngFUeLSp39Ha_dHn3niH9s1iu1MoNtKYgcRG41r02UYs9GjUyoQOfJEk_PViM7SsHbuA-_6l2B8TaCw_UYaam3qQI_Fm-8PndiISgPy8X_fIaUgWHtxqCTvzxzGvNpfDjqKtkJY1vpaGK8ccRbHXtbumv06JDkt22gw9olo_6BnY2VqWy72INHMJIxYOODQ0vOef5FWpsPGUZgsHhSK4kGpXldLauPJDYpEWTg5vfbZn21Kn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر و وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده
@withyashar</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/11310" target="_blank">📅 20:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11309" target="_blank">📅 20:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11308" target="_blank">📅 20:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromN Niki</strong></div>
<div class="tg-text">امریکا زمانی حمله میکنه که کسی منتظر نیس.</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11307" target="_blank">📅 20:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11306" target="_blank">📅 20:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c3c99b.mp4?token=G_s3Xtm2e7SeapiekOc0KZ0rPXRzk1CvGBXcw_nha3GTFYpXxpxsAkXV-3VTMQ73yZh7Hb7QwyqxlEz0ooC5DoQ9YlIAy6JWQnCukl3HZSQfr9LxLWRp1B9-nHXUKe1c8I5sco-kELNXreIWPQpu11IiHvC_RWh5mvsVhzWjVE9DmvN7HixvITgnOlOEBEQTe2GsFlVf83rvcgPqur3PMdJnNrUZs2YHRTIFIIY9Dzl_RPfn4-HWA77HW-EAHseJcFIloCLf7p6oalflLG45LfH3ubGb9LE5FheG1PYCs2EqL1bEC8FswBwiI3aJfhIG9KZDCJbzvqzqfPgYIpaQtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c3c99b.mp4?token=G_s3Xtm2e7SeapiekOc0KZ0rPXRzk1CvGBXcw_nha3GTFYpXxpxsAkXV-3VTMQ73yZh7Hb7QwyqxlEz0ooC5DoQ9YlIAy6JWQnCukl3HZSQfr9LxLWRp1B9-nHXUKe1c8I5sco-kELNXreIWPQpu11IiHvC_RWh5mvsVhzWjVE9DmvN7HixvITgnOlOEBEQTe2GsFlVf83rvcgPqur3PMdJnNrUZs2YHRTIFIIY9Dzl_RPfn4-HWA77HW-EAHseJcFIloCLf7p6oalflLG45LfH3ubGb9LE5FheG1PYCs2EqL1bEC8FswBwiI3aJfhIG9KZDCJbzvqzqfPgYIpaQtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11305" target="_blank">📅 20:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/11304" target="_blank">📅 20:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
سیستم امنیتی معتقد است که ترامپ با حمله‌ای محدود به ایران موافقت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/11303" target="_blank">📅 20:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/11302" target="_blank">📅 20:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsi</strong></div>
<div class="tg-text">یاشار بیا مثل سیاه جامگان یا حسن صباح یه فرقه راه بنداز
😅</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/11301" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اخرش مجبور به همین کار میشیم
🫤</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11300" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr.Moradi</strong></div>
<div class="tg-text">یاشار خودت یه فراخوان بده بزنیم کارو تموم کنیم
😂
🤦‍♂
‌ دیگه نمیکشیم</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11299" target="_blank">📅 20:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بیداریم مثل پلنگ
😾
💪🏾</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/11297" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11296">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsa • PERSIAN</strong></div>
<div class="tg-text">درود فرمانده یاشار
فرمانده نظری برای امشب تا وقتی بازار های مالی باز میشه داری ؟</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/11296" target="_blank">📅 20:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11295">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSxF2zeNbkndB8zYMP72vZKX3wf6uvSnBe1ua4ae9tGICJG-X993WlrWhwYb0SAEp27VF6A531hpamXMXyAoNw46E6Qlp0J82bu2axOKlxA3sel-CnDRgT5ZjOv_ZrjZQ6huwpFkYFACeDSEO71H8AGim7as1kF_opf0Zmp635z08lHkOYCjwOEbUOQU8TAZcHLbRNeHxzGHoqfVt6mFwtaY_2rwiMgTN_3Imh3nd1n8NM5zzMskvWSt126X9NSXOZ2dZC2EPCslIf-Ehyg2z-B6ECiGV3NT_1dA9BWYvB0c0DwRRlbdm8wvUT2RYeedDQq89uSQJnjPC9NOS1xG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پهپاد اسرائیلی مناره مسجدی در محله المحطه در خان یونس در جنوب غزه را هدف قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/11295" target="_blank">📅 20:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11294">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر خارجه چین:
رئیس‌جمهور شی جین‌پینگ طبق دعوت ترامپ در پاییز به آمریکا سفر خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/11294" target="_blank">📅 19:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11293">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">طبق گزارش خبرنگار همراه هیئت آمریکایی، پیش از سوار شدن به «ایرفورس وان»، کارکنان آمریکایی تمام وسایل و ههدایایی را که طرف چینی داده بود از جمله کارت‌ها، نشان‌ها، تلفن‌های موقت و اقلام هدیه جمع کردند و داخل سطل زباله انداختند و اجازه ندادند چیزی از چین وارد هواپیما شود.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11293" target="_blank">📅 18:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11292">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر نیروهای مسلح فرانسه: ناو هواپیمابر «شارل دوگل» در دریای عرب مستقر شده و ماموریت آن «دفاعی» است.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11292" target="_blank">📅 18:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37fa8adaa.mp4?token=MNkJjvAUdobrPP2sa3GSg9TWKz9EhmlKLYqeKBbJZ2-sHCdcBDvwKdfLcIxQosFzUXnHg-fmQVnHsyMVgj2fGtl2Ib6dgB6wNWJ9dunMXPHlaepSuniLq2kW1_4CvTxeSMWbRaqzLb4v1iidC_wVs-eaO5JpdNhTwS7KDGUe1YP6AWRQnDYZMVDr0ZzN_tzI1wKVWhAjlBHEXgVlcn75V8K1ZazmRpSHjQscJ8dLc0EAtFyY3yebniLz5xAEMjW2GbPdpg8bGtpwomkajF4y55vChx_OWxbpN28ISQIVUUq1U_MMnp9Cjl5h6U3GU7j56CGqD2n4R4s01ij9xKSvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37fa8adaa.mp4?token=MNkJjvAUdobrPP2sa3GSg9TWKz9EhmlKLYqeKBbJZ2-sHCdcBDvwKdfLcIxQosFzUXnHg-fmQVnHsyMVgj2fGtl2Ib6dgB6wNWJ9dunMXPHlaepSuniLq2kW1_4CvTxeSMWbRaqzLb4v1iidC_wVs-eaO5JpdNhTwS7KDGUe1YP6AWRQnDYZMVDr0ZzN_tzI1wKVWhAjlBHEXgVlcn75V8K1ZazmRpSHjQscJ8dLc0EAtFyY3yebniLz5xAEMjW2GbPdpg8bGtpwomkajF4y55vChx_OWxbpN28ISQIVUUq1U_MMnp9Cjl5h6U3GU7j56CGqD2n4R4s01ij9xKSvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: دیروز از دریادار کوپر درباره حمله به مدرسه دخترانه(میناب)در روز اول جنگ سؤال شد.
ترامپ:  منظورتون همون حمله اولیه‌ست؟ اون موضوع هنوز تحت تحقیق قرار داره.
خبرنگار: می‌تونید تأیید کنید که موشک آمریکایی بوده؟
ترامپ: شما از کدوم رسانه‌ای هستید؟
خبرنگار: بی‌بی‌سی.
ترامپ: بی‌بی‌سی فیکه با من حرف نزن.
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/11291" target="_blank">📅 16:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc3a3a9b4.mp4?token=nwLzFS6H-Lf9MOGh_FrJ6nL0vg6Qn2mySRouTpx0NTdWXJ7Ex4Wlq4kJBxGwnddJjtSAUp_2TQ2M_bmf9yHzq9H4xCOJ7C4Sqy9eQSRtEyEXQP7kfHN21UBFn5cDzCJijj56824oX7mCl4wtzAMI8p2YGc6gJlNSgChTnvqvZMPCT92edo5re0AVRGu9Jc8lnK3vYSbMkAN7fb7ZXiBD0YDaPiWsETg31wsBTmyl--cOF2niWW53Vy20hMseWbziDekUuanuFt9IgYsDMMpgTQDe4gTysgoQI69wCun5vQ6gHCNWJfdjscB1pUrBS_M4_EpM_JB9ILpUcZx1ttI8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc3a3a9b4.mp4?token=nwLzFS6H-Lf9MOGh_FrJ6nL0vg6Qn2mySRouTpx0NTdWXJ7Ex4Wlq4kJBxGwnddJjtSAUp_2TQ2M_bmf9yHzq9H4xCOJ7C4Sqy9eQSRtEyEXQP7kfHN21UBFn5cDzCJijj56824oX7mCl4wtzAMI8p2YGc6gJlNSgChTnvqvZMPCT92edo5re0AVRGu9Jc8lnK3vYSbMkAN7fb7ZXiBD0YDaPiWsETg31wsBTmyl--cOF2niWW53Vy20hMseWbziDekUuanuFt9IgYsDMMpgTQDe4gTysgoQI69wCun5vQ6gHCNWJfdjscB1pUrBS_M4_EpM_JB9ILpUcZx1ttI8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11290" target="_blank">📅 15:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238609fcd8.mp4?token=XMi7pehevpegMHZSP6wTfhAon1qrjk6n_1Ktfg-BV_uLNuD4C6GQYF93Uv571ltK4ZnFUJ3f4uAu2LbA90238Wc9R6YwAZwYf6Ox8jfNEkPmFqTuVhAGCgISF7nHDOPMbN47ZwwCVJ06T4pV5p4asO8uze63UQ3-usOc12KowbEZHUBDdWVtQy8fVUp-tZqxFAjWc-skIMe96VgGriIdqKUtJCyoqvVGLYBtRee-lyojJIsnCSnJPBmUadpGW9NXspm612ql_fFZykNl30H5eHmDtxYbKnwmcrc9xoY9ajgBoQLZtbFQgmftQ3cZzwDE4i6PRm9UCNX1tZVIFlSlnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238609fcd8.mp4?token=XMi7pehevpegMHZSP6wTfhAon1qrjk6n_1Ktfg-BV_uLNuD4C6GQYF93Uv571ltK4ZnFUJ3f4uAu2LbA90238Wc9R6YwAZwYf6Ox8jfNEkPmFqTuVhAGCgISF7nHDOPMbN47ZwwCVJ06T4pV5p4asO8uze63UQ3-usOc12KowbEZHUBDdWVtQy8fVUp-tZqxFAjWc-skIMe96VgGriIdqKUtJCyoqvVGLYBtRee-lyojJIsnCSnJPBmUadpGW9NXspm612ql_fFZykNl30H5eHmDtxYbKnwmcrc9xoY9ajgBoQLZtbFQgmftQ3cZzwDE4i6PRm9UCNX1tZVIFlSlnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 25 اردیبهشت روز پاسداشت زبان فارسی و بزرگداشت فردوسیه
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11289" target="_blank">📅 15:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4486529b5a.mp4?token=uy2xKt02W_WhIxBpmPwNcrKPHjlpkTCk-x5hq8MVrmgYW-h_GguGKkVZ5v2g7i_9mV0celcgFUX6ILMSkex4EtpItTwuf_tKDT4wbIKunF6mBBKKJeXc6xHik4H-PRTyeaO7kncPSmlx86I3JCtLyeVp_fEeN7C1dW_yUvZjN3-6CXcWsHKiLFF5Dx0VTnpspeWrDosCqHX4V8IZgEZbVj8hNP20rtSJI80fCq4CAhr3fU2eDtvsGciH_am6X6GYwBzyFFq8wW9BDw5HOyKDyRewfWqu91Lwxxbbdrf6O62U9L8xDgZVJSiaVZOBZAABuFGQ21mTeaARJDCbYl-ZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4486529b5a.mp4?token=uy2xKt02W_WhIxBpmPwNcrKPHjlpkTCk-x5hq8MVrmgYW-h_GguGKkVZ5v2g7i_9mV0celcgFUX6ILMSkex4EtpItTwuf_tKDT4wbIKunF6mBBKKJeXc6xHik4H-PRTyeaO7kncPSmlx86I3JCtLyeVp_fEeN7C1dW_yUvZjN3-6CXcWsHKiLFF5Dx0VTnpspeWrDosCqHX4V8IZgEZbVj8hNP20rtSJI80fCq4CAhr3fU2eDtvsGciH_am6X6GYwBzyFFq8wW9BDw5HOyKDyRewfWqu91Lwxxbbdrf6O62U9L8xDgZVJSiaVZOBZAABuFGQ21mTeaARJDCbYl-ZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روانه شدن نفت در سواحل جزایر خلیج فارس جمهموری اسلامی داره نفتو تو دریا میریزه و جان موجودات دریایی و زیست بوم ها رو به خطر انداخته
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11288" target="_blank">📅 15:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bba1486b.mp4?token=pLnDaFr-3feCYO_irtXUm_BfPj2T6Ymm1O4rAuCttedNCHqFzYY0-Qi8OgjYjNTEfHSZm1V-mXYEN_y0PPnJDGUJUcjihgIKplJiryydreIWQ5eeVqpTGqGC-dBnq7q_-6N3TK0jNcRxWiWTZujMr8DOs1Do9gWGbvzByYeM2gh1dY99KEiCw052G5l-v5xYN9c-ysF3IkLCc7Bdqsduf6zyFZdQTR2Qv4H7dg059jADLTsJwqP5Z_z3zVQPBroqDJDZWhCNinBUMsIT3dcxE8P7yIUUyxfqgLflP67fnThxhDcpNUVxxjL65O9ctdWQcy_1astjEBvWxoHnPh-SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bba1486b.mp4?token=pLnDaFr-3feCYO_irtXUm_BfPj2T6Ymm1O4rAuCttedNCHqFzYY0-Qi8OgjYjNTEfHSZm1V-mXYEN_y0PPnJDGUJUcjihgIKplJiryydreIWQ5eeVqpTGqGC-dBnq7q_-6N3TK0jNcRxWiWTZujMr8DOs1Do9gWGbvzByYeM2gh1dY99KEiCw052G5l-v5xYN9c-ysF3IkLCc7Bdqsduf6zyFZdQTR2Qv4H7dg059jADLTsJwqP5Z_z3zVQPBroqDJDZWhCNinBUMsIT3dcxE8P7yIUUyxfqgLflP67fnThxhDcpNUVxxjL65O9ctdWQcy_1astjEBvWxoHnPh-SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداسیما : نتانیاهو نه خسته شده نه عقب میخواد بکشه بنظرم واقعا مَرده واقعا مَرده و میخواد ایرانو
از 100 درصد به 20 درصد برسونه
همین الانم اماده ترین عنصر برای
حمله به ایران؛ اسرائیله
نتانیاهو نه کم آورده نه علائمی از خستگی داره نه پشیمانه
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11287" target="_blank">📅 14:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ به فاکس‌نیوز: ما می‌توانستیم پل‌ها و شبکه‌های برق ایران را نابود کنیم و می‌توانیم ظرف دو روز همه چیز را در آنجا از بین ببریم.
@withyashar</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/11286" target="_blank">📅 14:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم.
میتوانیم نیروگاه‌های ایران را تنها در دو روز از بین ببریم
اگر ایران اورانیوم های غنی شده خودش رو تحویل نده وارد ایران میشیم
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11285" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11284" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJvd</strong></div>
<div class="tg-text">مارو به قاهره میبره؟
خب پس بذار هرچی میخواد بگه</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11283" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
پیشنهاد ایرانیا که برام رسید همون‌ جمله ی اول متنشونو که خوندم برام قابل قبول نبود و سریع ردش کردم
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11282" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df234526d.mp4?token=O_2xlkyPdLHSXgujYu1iKbtIgjz7DzMuOb-N6mir_NfdfjJbMrs8eq1EQ5LWAda963P6OJBDK_czB-Rd_fafLMYvk8HHi7tdXfRnS753Ys26FU_kivS0Yf8KsZ100atpBP-GoZia6-rjQYtP_xgjoiIiKdpzw6hLSQuIzGFJvVY_Dqh-axI6NX2r1_r8_DbEepXgfkKnGJvWnoc5G4x5THc_Yuvk-IvOpQxYm700VqqEE-BvqN_jm3mxBpObf-K1ZWBeXuoZrDpqwzz3GbdpuAvqQNwnNVj4oX_9_9E41WPrVbv7LoOw_sDLNXcXClrGPlhdTipOEH2dg_aCnHRqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df234526d.mp4?token=O_2xlkyPdLHSXgujYu1iKbtIgjz7DzMuOb-N6mir_NfdfjJbMrs8eq1EQ5LWAda963P6OJBDK_czB-Rd_fafLMYvk8HHi7tdXfRnS753Ys26FU_kivS0Yf8KsZ100atpBP-GoZia6-rjQYtP_xgjoiIiKdpzw6hLSQuIzGFJvVY_Dqh-axI6NX2r1_r8_DbEepXgfkKnGJvWnoc5G4x5THc_Yuvk-IvOpQxYm700VqqEE-BvqN_jm3mxBpObf-K1ZWBeXuoZrDpqwzz3GbdpuAvqQNwnNVj4oX_9_9E41WPrVbv7LoOw_sDLNXcXClrGPlhdTipOEH2dg_aCnHRqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز اعلام کرد که ممکن است توقف ۲۰ سالهٔ فعالیت هسته‌ای ایران را بپذیرد.
ترامپ:“بیست سال کافی است. اما میزان تضمینی که از طرف آن‌ها می‌گیریم… باید واقعاً یک بیست سالِ واقعی باشد.”»
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/11281" target="_blank">📅 14:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ وسط‌ پرواز به فاکس‌نیوز : «من دیگر خیلی بیشتر از این صبر نخواهم کرد. آنها باید توافق را امضا کنند.»
«مواد هسته‌ای» ایران، ممکنه به چین یا آمریکا تحویل داده شه!
@withyashar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11280" target="_blank">📅 14:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11279">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
اما در نهایت فکر می‌کنم الان آخرین چیزی که دنیا نیاز دارد جنگ است، مخصوصاً جنگی که هزاران کیلومتر دورتر است.
شی درباره مسائل مختلفی مثل ، حملات سایبری و جاسوسی صحبت کرد. گفت هم آن‌ها جاسوسی می‌کنند و هم ما. این یک واقعیت است و همه این کار را انجام می‌دهند، اما معمولاً درباره‌اش صحبت نمی‌شود.
او گفت آمریکا در چین جاسوسی می‌کند. من گفتم ما هم همین کار را انجام می‌دهیم. این یک واقعیت است و مسئله‌ای است که همه طرف‌ها درگیر آن هستند
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/11279" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
شین گفت برخورد شما قوی‌تر از قبل بوده، چون ما با انها(حکومت ایران) رابطه داریم و ما درباره این موضوع صحبت کردیم. من گفتم این مثل جنگ است و حق با من بود. موضوع قدرت بود و همه با آن درگیر شدیم. این موضوع روی رابطه ما تأثیر گذاشت، اما قبل و بعد از آن رابطه خوبی داشتیم و الان هم رابطه‌مان قوی است. حتی به جایی رفتم که او زندگی می‌کند، که اتفاق نادری است. با هم ناهار خوردیم و درک خوبی بین ما وجود دارد. فکر می‌کنم او معتقد است اتفاقات مثبتی بین دو کشور در حال رخ دادن است
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/11278" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
نیویورک تایمز هم گزارش‌هایی داده بود درباره تحریم شرکت‌های چینی که نفت ایران می‌خرند. درباره آن صحبت کردیم و بعداً هم صحبت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/11277" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز : شین گفته جنگ باید متوقف شود. من چنین حرفی نمی‌زنم. فکر می‌کنم او آدم خوبی است، اما از بعضی حرف‌هایش خوشم نیامد. مثلاً گفته کشتی‌ها باید بعد از پایان کار نفت متوقف شوند. ما هم از نظر نظامی تقریباً کار را تمام کرده‌ایم، اما هنوز کامل نشده است.
ما حدود ۷۰ تا ۷۵ درصد کار را انجام داده‌ایم، نه همه‌اش را.
برمی‌گردیم و بقیه را هم تمام می‌کنیم
. بعضی بخش‌ها هنوز باقی مانده است. توان موشکی و پرتابگرهای موشک هنوز به طور کامل از بین نرفته‌اند، هرچند گفته می‌شود حدود ۸۰ درصد آن‌ها نابود شده است. تولید موشک هم بیشتر آن از بین رفته است
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11276" target="_blank">📅 14:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11275" target="_blank">📅 13:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار الجزیره:
تهران به‌طور رسمی پاسخ واشنگتن به پیشنهاد خود را دریافت کرده و ایالات متحده تمامی شروط ایران رو رد کرده.
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/11274" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😂
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/11273" target="_blank">📅 12:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ در تروث : پژوهشگر چینی به CNN گفت که به نشست ترامپ و شی نمره «۹.۹۹ از ۱۰» می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11272" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEONf_M-WuYrVL32B2UDArWZOalfqpKb0EAS42fXbAUbCkW9jBq07W6XoTLIR6QiTXMSDmVG9mZOp9aBJDg7RL4elZQpoz5wu4G9YT24ClwN3ycN-8hWhfY_B8hA5Pr6SBHl_anrg8RfVRx2m_QQnjtrNyEtRMXXBw28UB-A2-HTjbbyhoi9i_bIbH4Of08x0ojYMFZyo02J58zWj7y094Ovt3n2gh9wOTIEMmCid_1tyjOun7o2_GUJVfSsaCyUEFkwmNILGTXwXVAlnBf5eAsAeXDbQPNdhH9AoNrh8iW6V1qq2-F9yyfI72BKePKzjQQ3T64Mx-nsSqsLuVV0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد قنطاری، کاردار جدید سوریه در واشنگتن دی سی
😬
🍔
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11271" target="_blank">📅 12:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">@withyashar
part3</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11270" target="_blank">📅 12:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veQjoz8CJqAJQJO0lrU12Ge8qWVEheeEUhBKU3Sswi7qBt8CiRWlvcOiYrQgWB_4Z8Tbt5k97wkysAVgzs1dtLOaJ4rUwWav3nqh4KIoNTdI8zsBVFa-h4A8P1QwnJH7_tgB7ekhQei9-dFOwTrTZ0I1SSqRriH-z00SgldeHY3XVAU-eZ9gJMchW4afRtwLuGioyp5tY29iY_5_2yT5QNYB3ypVfjSVtI0IRQ05bG6iA6MTqTuXRkVO9-6AODLjd-5aBK0dj_eZevNmwUkj48_rLLRmnqgq6HaAtsN5CkhJZqexk97dTa6LrQB1Pi0m-vqsRhDcykVgvgfzUFcJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11269" target="_blank">📅 12:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هم‌اکنون حمله سنگین جمهوری اسلامی به مقر گروه های مخالف در عراق
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11268" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">طبق گزارش روزنامه «ساوت چاینا مورنینگ پست» و بازنشر آن توسط «بلومبرگ»، انتظار می‌رود «ولادیمیر پوتین» در حدود ۲۰ مه به «پکن» سفر کند؛ تنها حدود ۵ روز پس از دیدار «شی جین‌پینگ» و «دونالد ترامپ» در پکن.
رسانه‌ها می‌گویند این سفر احتمالاً فقط یک روز طول می‌کشد و بیشتر در قالب یک دیدار کاری و هماهنگی سیاسی انجام می‌شود. همچنین برخلاف سفر ترامپ، ظاهراً خبری از تشریفات بزرگ، رژه رسمی یا استقبال بسیار گسترده نخواهد بود و این سفر در سطحی ساده‌تر و کم‌نمایش‌تر برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/11267" target="_blank">📅 11:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">@withyashar
part2</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11266" target="_blank">📅 11:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ در تروث : «وقتی رئیس‌جمهور شی با بیانی بسیار سنجیده از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او آسیب عظیمی بود که ما در چهار سال دوران جو بایدنِ خواب‌آلود و دولت بایدن متحمل شدیم؛ و در این مورد، او صددرصد درست می‌گفت.  کشور…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11265" target="_blank">📅 11:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">@withyashar
part1</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11264" target="_blank">📅 10:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ih9AObi2nU2uZD_47cidRudDuIrfNIpoB5hoSmj-FdOxBWdtVvP0LDdqzdyueXSKgAhB0gq55kJmUPbEcY6_HZsInnkiILRPnjaVpOxTxkyw3E-CVrIfCeG3ODGiCzYFhkUDRi4q6Qkf66f_MlZaqOS2d5FQH1Bjty4zW_K_JAaz2ZpBh0TBLJNT4er2moYLizzzfGBS0LOCwsWztJ7YV0ZP74wVIRn0S7Ttn4M_OG9SxVSQzvohnKCKOhGaxyKYxsNPDDpNOnEl4ZKkCR3dwe_LnQ_EcUcZSa2H85DAMt88lp7OuHE9-Co6rHdR-kmejW5qChVjhWZTyGtmARkxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ih9AObi2nU2uZD_47cidRudDuIrfNIpoB5hoSmj-FdOxBWdtVvP0LDdqzdyueXSKgAhB0gq55kJmUPbEcY6_HZsInnkiILRPnjaVpOxTxkyw3E-CVrIfCeG3ODGiCzYFhkUDRi4q6Qkf66f_MlZaqOS2d5FQH1Bjty4zW_K_JAaz2ZpBh0TBLJNT4er2moYLizzzfGBS0LOCwsWztJ7YV0ZP74wVIRn0S7Ttn4M_OG9SxVSQzvohnKCKOhGaxyKYxsNPDDpNOnEl4ZKkCR3dwe_LnQ_EcUcZSa2H85DAMt88lp7OuHE9-Co6rHdR-kmejW5qChVjhWZTyGtmARkxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر ری اکشننن</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11263" target="_blank">📅 10:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromayoub</strong></div>
<div class="tg-text">نظرت چیه؟قبل جام جهانی میزنع یا بعد؟</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11262" target="_blank">📅 10:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال 13 اسرائیل:اسرائیل انتظار دارد حمله احتمالی آمریکا در ایران از فردا با بازگشت ترامپ از چین آغاز شود
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11261" target="_blank">📅 10:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9469892534.mp4?token=P_5M7TwDuV4n_r2zF4YUzUAkvxF2dEPJ9hd0XdG3kfhtRki3ev9TxS1z9RgOrPGtfiJSQTGLiczuRQG1rmFioWjEr66kmFGK6AvG-nEUQdno59kKgiU_E-a2GxEoIE1tt0skbAzsGkVZJSn0MxiLFuX5ZFe9kDavevBg4zSIPBz9Vb74mmZf4bcNtqhobWkX1Pj8Od5Bw7OvP05Q5SspT81uD0Xo6cwyRygbAyVE_JsDSxPe2fFj5cO0hv7mCKs8oT-Tk9AGzEKLwn8pPGofFYmNf5olah3tbpE_Jh3qqP09r87Pp0uYSK2YiCHYvnDUui24RKZYuds2R83pP0CdpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9469892534.mp4?token=P_5M7TwDuV4n_r2zF4YUzUAkvxF2dEPJ9hd0XdG3kfhtRki3ev9TxS1z9RgOrPGtfiJSQTGLiczuRQG1rmFioWjEr66kmFGK6AvG-nEUQdno59kKgiU_E-a2GxEoIE1tt0skbAzsGkVZJSn0MxiLFuX5ZFe9kDavevBg4zSIPBz9Vb74mmZf4bcNtqhobWkX1Pj8Od5Bw7OvP05Q5SspT81uD0Xo6cwyRygbAyVE_JsDSxPe2fFj5cO0hv7mCKs8oT-Tk9AGzEKLwn8pPGofFYmNf5olah3tbpE_Jh3qqP09r87Pp0uYSK2YiCHYvnDUui24RKZYuds2R83pP0CdpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان سفر ترامپ به چین
دونالد ترامپ، رئیس جمهور آمریکا، پکن را ترک کرد و سفر خود به جمهوری خلق چین را به پایان رساند.
شی جین‌پینگ، رئیس‌جمهور چین در آخرین روز سفر رئیس جمهور ایالات متحده گفت که دونالد ترامپ به دنبال بازگرداندن عظمت آمریکا است و او نیز متعهد به هدایت مردم چین برای تحقق رستاخیز ملی است.
شی جین‌پینگ همچنین تأکید کرده است که چین و آمریکا می‌توانند از طریق تقویت همکاری‌ها، روند توسعه و پیشرفت خود را تسریع کنند.
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11260" target="_blank">📅 10:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1169f33889.mp4?token=fD4qi8aVVKJSMeXHbr0Rd79XoTxG_ngkbHtOBhXfNEH6I1KkZuFUpHolbZcRNjQlBimldOudbIgOyK9CNHEpFDk7fUH4gQQxUB9J7RcO7PCA-LLX13oMZ58TdPpXChv-RWo2ET8Qa5QkDNaxVRHm58zosqjBR6o2J9b38b3ouhUtOndhTehRXrKIhU7C17aVteHYCsoWYiRugLcqBF0wrgZBL79zY4Y-F7cUl3UwzeExjCfeS-MViOphRL5siouOkUT2SkfztpYIi0xe6pTjVf0Np3kqw3lKPvwYhlQ2B_mubXWwnot12Ms9L7JSGuWTpIfRRfzBMF90od_khHIuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1169f33889.mp4?token=fD4qi8aVVKJSMeXHbr0Rd79XoTxG_ngkbHtOBhXfNEH6I1KkZuFUpHolbZcRNjQlBimldOudbIgOyK9CNHEpFDk7fUH4gQQxUB9J7RcO7PCA-LLX13oMZ58TdPpXChv-RWo2ET8Qa5QkDNaxVRHm58zosqjBR6o2J9b38b3ouhUtOndhTehRXrKIhU7C17aVteHYCsoWYiRugLcqBF0wrgZBL79zY4Y-F7cUl3UwzeExjCfeS-MViOphRL5siouOkUT2SkfztpYIi0xe6pTjVf0Np3kqw3lKPvwYhlQ2B_mubXWwnot12Ms9L7JSGuWTpIfRRfzBMF90od_khHIuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدوارم ایران تماشا کند. ما دقیقاً می‌دانیم چه چیزی را آماده کرده‌اند. می‌دانید، آن‌ها کمی استراحت داشتند، بنابراین سعی دارند چند چیز را با هم جمع کنند. آن‌ها موشک‌هایی را از زیر زمین بیرون آورده‌اند. همه این‌ها در یک روز از بین خواهند رفت. امیدوارم این رو ببینند چون همه کارهایی که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@withyashar
یاشار:خوب دیگه رسمأ داره میگه جنگ میشه و هم داره میگه حمله خیلی سریع و محکم انجام میشه همانطور که گفتیم</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11259" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ در همه جبهه ها شده و در صورت تحقق شروط ایران، مرحله دوم مذاکرات که درباره موضوع هسته ای بود، آغاز می شد
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11258" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مجلس نمایندگان آمریکا برای سومین بار طرح دموکرات‌ها جهت محدود کردن اختیارات نظامی ترامپ علیه جمهوری اسلامی رو رد کرد.
این طرح با نتیجه ۲۱۲ در برابر ۲۱۲ به تساوی رسید و در نهایت با اختلاف یک رای شکست خورد.
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/11257" target="_blank">📅 09:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11256" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641dc900e.mp4?token=W5J62XPL3MlKGEvZf-hAIFxRt_4RnnXsbppm7cVG1A6PcFFCDF219RxAuJEynNnUgJ7jh3OufvE-X4KyAEHtFOBzruLq9W0LZ_Uk3AjZ_uWrGNLkEkafs8rzeo2WaelIODSbJoFUChJWufHMOFVVGuWhKvW_CaEgXx-bXSDp78coStauOVJwsBSOMFAzs6VRAW5c9TuuPN4NyRS-VtUMEhzVMHIlv2qq6f2v9ufR4b6rtUCRXgzz7ozptjUtgck_bP1CcQN2NbFfPjKGR0i-Ub5YYGhgJUqNnh_H8-ixPBo2fKN19boFPuelSm2SYagxOkoioU44DlNdU9eu4KpcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641dc900e.mp4?token=W5J62XPL3MlKGEvZf-hAIFxRt_4RnnXsbppm7cVG1A6PcFFCDF219RxAuJEynNnUgJ7jh3OufvE-X4KyAEHtFOBzruLq9W0LZ_Uk3AjZ_uWrGNLkEkafs8rzeo2WaelIODSbJoFUChJWufHMOFVVGuWhKvW_CaEgXx-bXSDp78coStauOVJwsBSOMFAzs6VRAW5c9TuuPN4NyRS-VtUMEhzVMHIlv2qq6f2v9ufR4b6rtUCRXgzz7ozptjUtgck_bP1CcQN2NbFfPjKGR0i-Ub5YYGhgJUqNnh_H8-ixPBo2fKN19boFPuelSm2SYagxOkoioU44DlNdU9eu4KpcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ ترامپ: ما مشکلات زیادی را حل کرده‌ایم که دیگران قادر نبودند و این رابطه یک رابطه بسیار قوی است. فکر می‌کنم در مورد ایران کارهای فوق‌العاده‌ای انجام داده‌ایم، ما هم صحبت کردیم.
‏ما در مورد ایران بسیار مشابه‌ایم، می‌خواهیم این وضعیت پایان یابد. نمی‌خواهیم آن‌ها به سلاح هسته‌ای دست پیدا کنند. می‌خواهیم تنگه‌ها باز باشند و ما آن را برایشان می‌بندیم، آن‌ها تنها تنگه را بستند و بعد ما هم روی سرشان بستیم.
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11255" target="_blank">📅 09:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد
تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند.
هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/11254" target="_blank">📅 09:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11253" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
