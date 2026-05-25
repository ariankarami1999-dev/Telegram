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
<img src="https://cdn4.telesco.pe/file/akb16bUfntsjDmVPmgcI30b_Jm8uoGLOy1YlPID2IxoTtv3O1tTm0CP1fn6vf2kPpTPoFPbfVckWWubb_LAY89Ehf-2aAGE4gGbKkytFI9oWqAHO6ZEQTlC-qPMfuHV5CsgtyV7tRbaaTqdkvLeeyhYceWLfCxnfnAdX4kFHMvXWQt7f3jfeK6yNN2ldqWpwjXrGRbTPRjJaO9l483BH7Oa5eYSCyRbxUFXb0cqfVPUgdVeB2Fn_0tuP0C5bDZM7GuevWadoILMg-s-xsqASlYyTtZQQewqNhA1vBupQBFcshKNhIZoGIiOOJhr40UUIM124ECE8E1-YfDYHEMlwpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 273K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 22:27:12</div>
<hr>

<div class="tg-post" id="msg-12453">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو:جنگ تمام عیار در لبنان از امشب آغاز خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/withyashar/12453" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12452">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایسنا: با توجه به تایید مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴ از سوی رئیس‌جمهور و ابلاغ آن به وزارت ارتباطات، انتظار می‌رود این دستور فردا اجرایی شود
@withyashar</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/withyashar/12452" target="_blank">📅 22:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پزشکیان: در جنگ ۱۲ روزه خدمت رهبر شهید رفتم و ایشان گفتند چگونه مذاکره انجام بشود
ایشان قبول کردند ما باید برویم پای میز مذاکره، اما ما اکنون تبلیغ می‌کنیم که نباید مذاکره کنیم
@withyashar
رفسنجانی هم با همین فن از قول خمینی ، خامنه ای رو رهبر کرد !
😂</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/withyashar/12451" target="_blank">📅 21:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: دولت ترامپ از تشدید اقدام نظامی اسرائیل در لبنان حمایت خواهد کرد. @withyashar</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/12450" target="_blank">📅 21:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">61 سال پیش در چنین روزی الی کوهن جاسوس افسانه‌ای و عجیب و غریب موساد توسط دولت سوریه اعدام شد الی کوهن توانسته بود تا سطوح ارشد وزارت دفاع سوریه نفوذ کند و عملاً با اطلاعات طلایی اش توانست پیروزی های اسرائیل در بلندی های جولان در جنگ شش روزه را تسهیل کند
@withyashar
قبلا به شما در اتاق جنگ مینی سریال بسیار زیبای داستان زندگیشو به نام The Spy معرفی کردم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/12449" target="_blank">📅 21:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: دولت ترامپ از تشدید اقدام نظامی اسرائیل در لبنان حمایت خواهد کرد
.
@withyashar</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/12448" target="_blank">📅 21:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طبق خبرهای رسیده به خبرنگار هم‌میهن رئیس‌جمهور زرشکیان دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد. @withyashar</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/withyashar/12447" target="_blank">📅 21:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e9a943ca.mp4?token=N_xqephuGGGf8HHUdq5woZhYCXD68VWqPMapf9NhUMEC72icpmrCbX6MaUW6NLfHkKEir6CWeaPIZr2R4QK0zoQTz9HyAiOgyN4t34yBdkewtxppBTNIf40uCVUN0EwXBL539R_8p8ILPJni2pQTpY4DGlgdshONteDl1P-efw9vz2XL39IVWBYPAhMRS6N39FNn7DQJzoRWlw_xANNpgBgEue3Z-N5w57tNPrIonMSqQc48bMb5vIemXtTs5EqdZI6fd01wZHAWSAZZgL1YT9rOKfz4W-OltTS758pCHPWKEQ-VJyJzJADdesBnxKWXfBQEhExWz9ehxbwGXJ43Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e9a943ca.mp4?token=N_xqephuGGGf8HHUdq5woZhYCXD68VWqPMapf9NhUMEC72icpmrCbX6MaUW6NLfHkKEir6CWeaPIZr2R4QK0zoQTz9HyAiOgyN4t34yBdkewtxppBTNIf40uCVUN0EwXBL539R_8p8ILPJni2pQTpY4DGlgdshONteDl1P-efw9vz2XL39IVWBYPAhMRS6N39FNn7DQJzoRWlw_xANNpgBgEue3Z-N5w57tNPrIonMSqQc48bMb5vIemXtTs5EqdZI6fd01wZHAWSAZZgL1YT9rOKfz4W-OltTS758pCHPWKEQ-VJyJzJADdesBnxKWXfBQEhExWz9ehxbwGXJ43Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ:
"در دو جنگ اخیر، مجموعاً ۱۳ تن از نیروهای نظامی خود را از دست داده‌ایم... در عملیات «خشم حماسی»، ۱۳ جان فوق‌العاده را از دست دادیم."
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12446" target="_blank">📅 20:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبکه ۱۲ تلویزیون اسرائیل به نقل از منابع آگاه گزارش داد که «استیو ویتکاف» و «جرد کوشنر» به منظور بحث و تبادل نظر درباره توافق احتمالی میان واشنگتن و تهران به اسرائیل سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12445" target="_blank">📅 20:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">طبق خبرهای رسیده به خبرنگار هم‌میهن رئیس‌جمهور زرشکیان دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/12444" target="_blank">📅 20:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ برای بار دو میلیون و چهارصدو شصت و هشتم : ایران هیچوقت سلاح هسته ای نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12443" target="_blank">📅 20:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">منابع العربیه: نسخه نهایی پیش‌نویس یادداشت تفاهم آمریکا و ایران شامل تجدید قابل‌تمدید آتش‌بس 60 روزه، باز کردن تنگه هرمز بدون اخذ عوارض و پاکسازی مین‌ها و برداشتن موانع دریایی از این آبراه بین‌المللی مقابل تجارت جهانی، برداشتن برخی محدودیت‌ها از بنادر ایران و دادن معافیت‌‌هایی از تحریم‌ها و فراهم کردن امکان ازسرگیری فروش و صادرات نفت ایران و همچنین ادامه مذاکرات درباره برنامه هسته‌ای ایران در دوره تنش‌زدایی میان دو طرف، می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12442" target="_blank">📅 20:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادعای الحدث به نقل از منابع: ایران آماده‌ست تا اورانیوم با غنای بالا رو به چین  انتقال بده ! @withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12441" target="_blank">📅 20:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12440">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق گزارش تایید نشده از شاهدان عینی که به دستمان رسیده است از وقوع یک درگیری نامشخص در محدوده میدان انقلاب تهران در ساعتی قبل خبر می‌دهند.
بر اساس این ادعاها، گفته می‌شود منطقه  تحت کنترل نیروهای امنیتی قرار گرفته و رفت‌وآمد در برخی مسیرها محدود شده است.
همچنین طبق گفته شاهدان عینی تعداد زیادی جنازه که از ظواهر آنها مشخص بود نیروهای حشد الشعبی بوده اند روی زمین ریخته بود
به محض وصول هر گونه اخبار تکمیلی به اطلاع شما عزیزان خواهد رسید ‌
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/12440" target="_blank">📅 20:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نورالدین الدغیر، خبرنگار الجزیره در تهران:
به نظر می‌رسد گره مذاکرات ایران و آمریکا در حال باز شدن است و ابتکار قطر نقش اساسی در حل اختلافات داشته است.
به گفته او، دوحه یک میانجی واقعی بوده، نه فقط کمکی در میانجی‌گری.
@withyashar</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/12439" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12438">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">العربیه: پیش‌نویس توافق میان آمریکا و ایران، برقراری آتش‌بس جامع در تمامی جبهه‌ها، از جمله لبنان را تضمین می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/withyashar/12438" target="_blank">📅 20:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادعای الحدث به نقل از منابع:
ایران آماده‌ست تا اورانیوم با غنای بالا رو به چین  انتقال بده !
@withyashar</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/12437" target="_blank">📅 20:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12436">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/12436" target="_blank">📅 19:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12435">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca508f5252.mp4?token=QibxweggHVqikDzKo5FKp-w_xZSBX5LFs56YE8idmTFCJ6NWeDCZjwk_jMMicYI-fjMcRgXelsM2vwfVPPjXcGYhkLb_T27nSzP8SIqQdH1ooJxoFRo7KDBSb6IVgyRbLqsfrysURgNNePHsIAe8_81UQqcLQ1CMYUY04ZjIIP7jecQrHFjkyKdnx7Mat6WK4t6RAHAo7KEaaeHJ0gG2GGhe1xUe0MuZnfKvpIOJQ_AvmEE2ce2QomuMuMrFmkJO1nbfl5txnZ1K-rsnqJxBsL3m3vGNMqM1HwyRCCRF7ItTe0NGu0C3Ylf-k-Gbt5_4KorsYmlqsb5RHloMAcJP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca508f5252.mp4?token=QibxweggHVqikDzKo5FKp-w_xZSBX5LFs56YE8idmTFCJ6NWeDCZjwk_jMMicYI-fjMcRgXelsM2vwfVPPjXcGYhkLb_T27nSzP8SIqQdH1ooJxoFRo7KDBSb6IVgyRbLqsfrysURgNNePHsIAe8_81UQqcLQ1CMYUY04ZjIIP7jecQrHFjkyKdnx7Mat6WK4t6RAHAo7KEaaeHJ0gG2GGhe1xUe0MuZnfKvpIOJQ_AvmEE2ce2QomuMuMrFmkJO1nbfl5txnZ1K-rsnqJxBsL3m3vGNMqM1HwyRCCRF7ItTe0NGu0C3Ylf-k-Gbt5_4KorsYmlqsb5RHloMAcJP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/12435" target="_blank">📅 19:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADiuE5U1zIIHaf7dfVMbpzjxyNVfw1wl_poVGfvW18scSw7cc5jCDUsrjDfbzdDDmmH4ZfE08Ve1YXCZ8jZE00HlR5d1dWwZsj31IU-xBU4ACRP3NT6dCjPayyGqkgR-tps6BzfPZwnVEfqemxFMojktzG2giJlcxzRYyr6DniaAYiSE3dp-Cmdse0JJTolLxiXvlE_z9cJHYEdS7WTOWzSd3NzPw9LPPyxTGiiIAQI-d3PcQQAWqL7t6UiH-wj0DHNDF_ClxRWZJbmcS0kyJP_LFpE1qR9JzaL6nrLxh-dUQsdS5ZnajGg_yroaoDfmD3VCLH5NzsTY-bEsiCKZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vC4z2bkfbeAytwEL8u1jAq2oZjN_t-MrIsz5KZOuD1Ci6Mh9-5EytPVLpvemANw7Ul0k09DI8ZFhL6LuYbhlaz2BFu21909HQfBIN_ppQmPKT372SXqtTeCM8O5YjV4S5KrPIGuEoaDleCg72dNbogzcghLTyYQzEoeP69jMoEoS5BIaQ8HniShvqc2Xd2GGv961SKGz8ERcYc-Fhsd11tLXe3shAD_4VE3YZ0U8Hr1oYMIeIqClBumss58mPpQLTPNjNAxo7bXYHPYGE7IKecU9heG2MpqfkOIrl1YM0YQR8BiV8t8bjN85DYwCJ2os1hnJb0mXVTi7CoSMHK3-eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ با مسخره کردن اوباما و بایدن عکسهایی منتشر کرد که آنها به ایران پول میدهند و مذاکره میکنند، ولی او آنها را منهدم میکند.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/12433" target="_blank">📅 19:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/12428" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12427">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس جمهور مکزیک رسما از میزبانی تیم ملی فوتبال ایران در جام جهانی خبر داد
«کلودیا شین‌بام» رئیس‌جمهور مکزیک، رسماً اعلام کرد که تیم ملی فوتبال ایران به دلیل محدودیت‌های حضور در خاک آمریکا، در ایالت «باخا کالیفرنیا» مستقر خواهد شد.
با تایید دولت مکزیک، تیم ملی ایران شهر «تیخوانا» را به عنوان مقر اصلی و محل تمرینات خود در طول مسابقات جام جهانی ۲۰۲۶ انتخاب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/12427" target="_blank">📅 18:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12426">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/12426" target="_blank">📅 18:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانال ۱۴ اسرائیل: اختلاف نتانیاهو با ترامپ عملیات فریب است
طبق گفته یک تحلیلگر ارشد امنیتی اسرائیل، گزارش‌های درز کرده درباره تماس‌های تلفنی پرتنش میان ترامپ و نتانیاهو بر سر ایران واقعی نبودند، بلکه بخشی از یک راهبرد حساب‌شده برای گمراه‌کردن تهران بودند.
بر اساس گزارش کانال ۱۴ اسرائیل، این جنجال با گزارشی از پایگاه خبری آکسیوس آغاز شد که مدعی بود یک تماس تلفنی به‌ ویژه دشوار میان ترامپ و نتانیاهو درباره یک پیشنهاد جدید آمریکایی که از طریق پاکستان برای ایران ارسال شده، صورت گرفته است.
کوبی مایکل، پژوهشگر ارشد در مؤسسه مطالعات امنیت داخلی (INSS) و مؤسسه میسگاو، توضیح می‌دهد که این یک فریب تاکتیکی درخشان بوده است: «نه رئیس‌جمهور ترامپ و نه نخست‌وزیر نتانیاهو هیچ علاقه‌ای به یک بحران واقعی ندارند. با درز داستان درباره یک بحران جدی ادعایی میان آن‌ها، ایرانی‌ها ممکن است از زمان‌بندی حمله نظامی بعدی کاملاً غافلگیر شوند.»
@withyashar</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/12425" target="_blank">📅 18:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12424">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وال استریت ژورنال ادعا کرده روند توافق بین ایران و آمریکا به خاطر اختلاف نظر شدید تو موضوع هسته‌ای و آزادسازی پول‌های بلوکه شده ایران خیلی کند شده (به بن‌بست نزدیک شده)
@withyashar</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/12424" target="_blank">📅 18:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71963b16ac.mp4?token=LW4BgQazy6fC5jzJsFvpB_kYuCK3Kri3lXWTV6QEqkMg4MXkmqcJdZsexkJkE7nMrZ6DpN-W9Tw8XkpRVj-XzKsqujGW-S13GUEf1v_PFTTjD_vwopByAgj8rCEfjedvbJAT0_FJjnLBwmDZlGK8698T1X_kVN8WztF76m15NOgyIFbCR_fWgOq-n8yUQFoluDcgRWmPG-_oHP9UU0_0eO3uJ-VvR6kj7cWGxxcreRu2Q7Hk2ebSkakqIoPdeGYcEz_6H3thAvKh-nb2amT4yD9CVQKFoAjtndsV-yIQa9RYZ6mu9oo5Q71C38nLgQu7WF0HTDPB2roTPuzRgimzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71963b16ac.mp4?token=LW4BgQazy6fC5jzJsFvpB_kYuCK3Kri3lXWTV6QEqkMg4MXkmqcJdZsexkJkE7nMrZ6DpN-W9Tw8XkpRVj-XzKsqujGW-S13GUEf1v_PFTTjD_vwopByAgj8rCEfjedvbJAT0_FJjnLBwmDZlGK8698T1X_kVN8WztF76m15NOgyIFbCR_fWgOq-n8yUQFoluDcgRWmPG-_oHP9UU0_0eO3uJ-VvR6kj7cWGxxcreRu2Q7Hk2ebSkakqIoPdeGYcEz_6H3thAvKh-nb2amT4yD9CVQKFoAjtndsV-yIQa9RYZ6mu9oo5Q71C38nLgQu7WF0HTDPB2roTPuzRgimzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خلبان کلمبیایی که در ارتفاع ۱۲۵۰۰ پایی پرواز می‌کرد، تصویری را ثبت کرد که به عنوان بهترین فیلم ثبت شده از بشقاب پرنده‌ها تا به حال توصیف شده است و بنا به گزارش‌ها، اصالت آن تأیید شده است.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12423" target="_blank">📅 18:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150a08d32b.mp4?token=bGU92hRMp4Swlu9JKPXojP3QczpOLTEtOqLIoUOEp6ZKDpZDY0ovanI-SntWKyS3n8E3niFQ-tJkCceQ0--91h1bwBiBVYgwHR40suG_saxKkrD1Ps207dQk8piV72d8Md0b3z4pflcHYSpHqvO46fQJX6CRGmJ8-bCAjI0GtaE5KAb8-MHFJzhTl5qIKzUWSoMjGiw6k-i33sZ_L9InjXGFjhnszxsnAoO7qsongpbQ-byvRh3zk29Up-prMzDGY9IGYNsI0iFsZbKpRVQWM9s8mtKsnn9QXuOfb7sXs-MIewoxF-YFNpDOzcgCcp4dNlV3MZxvjxydjVnorxfZNx4xP2Q1RbObueMF9jXhYG-5EuPipiYj4n8yBfNPbMMOwLtp8W_tlUERXw004djCaMzvEjxj5B354XnKumbRBeHduUyogiNqB1vq4oc8s8KHREYtXCS1z5Q4drNOh9awyPJB9SxbC_wBJReVUPlj6X2ugj5UmUTAnyfe_CHxIyLuQjnL0DPYXHjXEKWz2J2lDT7S4Gxl4X5w7_2aqfV3_TnjFWeWAVe6gWpJ4J9nk2v-R8hyt3TpTCFxZWvcTgIyRlL-9RQ13vpSGDaSajoNa4DJsRKppMfIwdnXBcO7WQcOI33bcNT0dTNgiaNfVlfOYJr_7bFFp0DsWOBZIHn-ilc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150a08d32b.mp4?token=bGU92hRMp4Swlu9JKPXojP3QczpOLTEtOqLIoUOEp6ZKDpZDY0ovanI-SntWKyS3n8E3niFQ-tJkCceQ0--91h1bwBiBVYgwHR40suG_saxKkrD1Ps207dQk8piV72d8Md0b3z4pflcHYSpHqvO46fQJX6CRGmJ8-bCAjI0GtaE5KAb8-MHFJzhTl5qIKzUWSoMjGiw6k-i33sZ_L9InjXGFjhnszxsnAoO7qsongpbQ-byvRh3zk29Up-prMzDGY9IGYNsI0iFsZbKpRVQWM9s8mtKsnn9QXuOfb7sXs-MIewoxF-YFNpDOzcgCcp4dNlV3MZxvjxydjVnorxfZNx4xP2Q1RbObueMF9jXhYG-5EuPipiYj4n8yBfNPbMMOwLtp8W_tlUERXw004djCaMzvEjxj5B354XnKumbRBeHduUyogiNqB1vq4oc8s8KHREYtXCS1z5Q4drNOh9awyPJB9SxbC_wBJReVUPlj6X2ugj5UmUTAnyfe_CHxIyLuQjnL0DPYXHjXEKWz2J2lDT7S4Gxl4X5w7_2aqfV3_TnjFWeWAVe6gWpJ4J9nk2v-R8hyt3TpTCFxZWvcTgIyRlL-9RQ13vpSGDaSajoNa4DJsRKppMfIwdnXBcO7WQcOI33bcNT0dTNgiaNfVlfOYJr_7bFFp0DsWOBZIHn-ilc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بار جدید نخود رسید
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/12422" target="_blank">📅 17:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12421">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMariam</strong></div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/12421" target="_blank">📅 17:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12420">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9a649e54.mp4?token=syv1X9ZiZ0FTOFbBE_apX3k39ZiP0nLHI03Uvc8CEbgSNOT-k9UPI6eyFUP-FphjwtfMo-m9BhabGievADXfHRbznvaTmbs992EIedUT2hqEQOzS1IgsVYhIqB3cdjzC-IBJwLWCiaaSdsbjnvTG9xo-Osw8t45JNPXpXBr1ECqwa7RlIwok1npQQUHIdvGZqvE_4Xr854IHtE6VOXMeHuApFw10_2WS_3WhCEVwpME9S73fB3KxHBOyjyhd2x_tBoYO5IEpsOILFdtM3aSO947qr_oCuCkdqnL6wK6NeHKtTpI5sYm0DG_bmS-7x3NGwWlbBFmpoIGYyZDLeOdx9jVmOl_gJeZhLvpt0ZVfKB4xqfUjW16m0AYKobST6VXIVAxZ2PkINrcLw10DmkGxz78NkTqocmEpmhueb0osaJZNmSH-MVDmsLxetxAMBOxFcQwoQazI00T3rpCaO2da366MknGBiEjqeDItkMNREP9HOXuiIrKvwK2RjbiiVL2FGhIyjnnAylfcrORqwwrOIHN2kWpq-AUdEKaohNgVdV9VX0aRZsj-YsYWPQjqHJ_4yt7Fy3XkFlPaaokAcABNpCSpa1zdcgznxon-EWWZi6d2tNMd75USOpzddzM7XcJhrw8jm38Dcgkv2oBzJu6P-1odQRJoZdDI98cK0pPJznU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9a649e54.mp4?token=syv1X9ZiZ0FTOFbBE_apX3k39ZiP0nLHI03Uvc8CEbgSNOT-k9UPI6eyFUP-FphjwtfMo-m9BhabGievADXfHRbznvaTmbs992EIedUT2hqEQOzS1IgsVYhIqB3cdjzC-IBJwLWCiaaSdsbjnvTG9xo-Osw8t45JNPXpXBr1ECqwa7RlIwok1npQQUHIdvGZqvE_4Xr854IHtE6VOXMeHuApFw10_2WS_3WhCEVwpME9S73fB3KxHBOyjyhd2x_tBoYO5IEpsOILFdtM3aSO947qr_oCuCkdqnL6wK6NeHKtTpI5sYm0DG_bmS-7x3NGwWlbBFmpoIGYyZDLeOdx9jVmOl_gJeZhLvpt0ZVfKB4xqfUjW16m0AYKobST6VXIVAxZ2PkINrcLw10DmkGxz78NkTqocmEpmhueb0osaJZNmSH-MVDmsLxetxAMBOxFcQwoQazI00T3rpCaO2da366MknGBiEjqeDItkMNREP9HOXuiIrKvwK2RjbiiVL2FGhIyjnnAylfcrORqwwrOIHN2kWpq-AUdEKaohNgVdV9VX0aRZsj-YsYWPQjqHJ_4yt7Fy3XkFlPaaokAcABNpCSpa1zdcgznxon-EWWZi6d2tNMd75USOpzddzM7XcJhrw8jm38Dcgkv2oBzJu6P-1odQRJoZdDI98cK0pPJznU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹۵٪ از توافق ایران تکمیل شده؛ ایران اگر بخواهد به توافق صلح ابراهیم می‌تواند بپیوندد/ خبرنگار فاکس‌نیوز در تل‌آویو:
"ترامپ به طور خاص از عربستان سعودی و قطر خواست که بپیوندند و اضافه کرد که دیگران نیز باید از آنها پیروی کنند. او حتی در صورتی که ایران این توافق را امضا کند، درِ ورود ایران به پیمان ابراهیم را باز گذاشت.
در حال حاضر، دولت ترامپ می‌گوید توافق با ایران ۹۵ درصد کامل شده است، اما جزئیات نهایی همچنان در حال بررسی است. دیروز در تماسی با خبرنگاران، یکی از مقامات ارشد دولت توضیح داد که ممکن است چندین روز طول بکشد تا به تفاهم‌نامه برسیم، زیرا سیستم ایران به سادگی نمی‌تواند به سرعتی که ایالات متحده می‌خواهد حرکت کند...
در حال حاضر، ایران میلیاردها دلار از دارایی‌های بلوکه‌شده خود را به همراه معافیت‌های تحریم نفتی دریافت خواهد کرد، اما به گفته مقامات آمریکایی، تنها در صورتی که به تعهدات خود پایبند باشند."
@withyashar</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/12420" target="_blank">📅 17:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مهر: ایران با سامانه دفاعی جدید خودش به نام «کمان ارش» یه پهپاد جاسوسی دشمن رو رهگیری کرد
@withyashar
گویا همین پدافند قشم است</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/12419" target="_blank">📅 16:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12418">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اتاق جنگ با یاشار : نقشه عالی پیش میره
😃
💪🏾
مثل بنز داره کار میکنه … از این جدیدایه فابریک صفر کارخونه برند نیو</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/12418" target="_blank">📅 16:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12417">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دو مقام اسرائیلی به رویترز: نتانیاهو به نزدیکان خود می‌گوید که هیچ تأثیری بر تصمیمات ترامپ ندارد
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/12417" target="_blank">📅 16:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12416">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9xcQbTRoW4NRALXqny9FYJQmHSKrir6K7bUUS_52nfTkMiXECzgUTqvIMheBqRX4d6prqM2cc9YetVlxMIuLfliZVWBXvccQKC7UoWAI_WVGEtPDW0KlBAjoyGZ3lC0gEhjXNsBAFrR8M5-pfBH2dy-etIDm13F9qdw5LSrcIS4E7hSB6xYR-91QZcvGjpy1GXiiveq6uGC3FpdfsGIIDx1FcwtZukCosBgu2BwbFX24XBZPcLkFvLw2lelqbeC1vXIR3RacMCj4EybS1eSv0Xcz_MWwpoMGNNN9CCyRNKh9ga1-qzcQGzM8WtJ7hpkyIGYI-DtZvSQCX13EFRk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «مذاکرات با جمهوری اسلامی ایران به‌خوبی در حال پیشرفت است! یا این توافق، توافقی بزرگ برای همه خواهد بود، یا اصلاً توافقی در کار نخواهد بود — وگرنه بازگشت به میدان نبرد و تیراندازی آغاز می‌شود، آن هم بزرگ‌تر و قدرتمندتر از همیشه — و هیچ‌کس چنین چیزی را نمی‌خواهد!
در جریان گفت‌وگوهایم در روز شنبه با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی، محمد بن زاید آل نهیان، رئیس کشور امارات متحده عربی، شیخ تمیم بن حمد آل ثانی، امیر قطر، محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی، نخست‌وزیر قطر، علی الثوادی، وزیر قطری، سید عاصم منیر احمد شاه، فرمانده ارتش پاکستان، رجب طیب اردوغان، رئیس‌جمهور ترکیه، عبدالفتاح السیسی، رئیس‌جمهور مصر، ملک عبدالله دوم، پادشاه اردن، و حمد بن عیسی آل خلیفه، پادشاه بحرین، اعلام کردم که پس از تمام تلاش‌هایی که ایالات متحده برای کنار هم قرار دادن این پازل بسیار پیچیده انجام داده، لازم است که همه این کشورها، حداقل به‌صورت هم‌زمان، به پیمان ابراهیم بپیوندند.
@withyashar
کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از: عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یک یا دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند تا این توافق با ایران را به رویدادی تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.
پیمان‌های ابراهیم برای کشورهای عضو آن — یعنی امارات متحده عربی، بحرین، مراکش، سودان و قزاقستان — یک جهش عظیم مالی، اقتصادی و اجتماعی به همراه داشته‌اند، حتی در این دوران جنگ و درگیری؛ تا جایی که هیچ‌یک از اعضای فعلی حتی صحبت از خروج یا توقف موقت هم نکرده‌اند.
دلیلش این است که پیمان‌های ابراهیم برای آن‌ها فوق‌العاده بوده و برای همه نیز حتی بهتر خواهد بود، و برای نخستین بار در پنج هزار سال گذشته، قدرت، توان و صلح واقعی را به خاورمیانه خواهد آورد.
این سند، همانند هیچ توافق دیگری که تاکنون در جهان امضا شده، مورد احترام قرار خواهد گرفت. سطح اهمیت و اعتبار آن بی‌همتا خواهد بود!
@withyashar
این روند باید با امضای فوری عربستان سعودی و قطر آغاز شود و دیگران نیز باید به‌دنبال آن حرکت کنند. اگر این کار را نکنند، نباید بخشی از این توافق باشند، زیرا این نشان‌دهنده نیت بد است.
در گفت‌وگو با بسیاری از رهبران بزرگی که نام برده شد، آن‌ها اعلام کردند که به‌محض امضای سند ما، از حضور جمهوری اسلامی ایران در پیمان‌های ابراهیم استقبال خواهند کرد. واو، این واقعاً چیزی ویژه خواهد بود!
این مهم‌ترین توافقی خواهد بود که هر یک از این کشورهای بزرگ اما همواره درگیرِ منازعه تاکنون امضا کرده‌اند. هیچ‌چیز در گذشته یا آینده از آن فراتر نخواهد رفت.
@withyashar
بنابراین، من به‌طور الزامی درخواست می‌کنم که همه کشورها فوراً پیمان‌های ابراهیم را امضا کنند، و اگر ایران توافق خود را با من، به‌عنوان رئیس‌جمهور ایالات متحده آمریکا، امضا کند، حضور ایران نیز در این ائتلاف بی‌نظیر جهانی مایه افتخار خواهد بود.
خاورمیانه متحد، قدرتمند و از نظر اقتصادی نیرومند خواهد شد؛ شاید بیش از هر منطقه دیگری در جهان!
با انتشار این پیام در تروث سوشال، از نمایندگان خود می‌خواهم روند پیوستن این کشورها به پیمان‌های ابراهیمِ تاریخی را آغاز کرده و با موفقیت به پایان برسانند.
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/12416" target="_blank">📅 15:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2fb5139f3.mp4?token=jnHWoBMvEghnSm8GWYs3LaulZhk6yhrCu-20cgO9BKs2axKcQ3iV_xkQKeoLV4VlK21JFZ-2V8PzvP-9lTA3Nzccix5vjz3xt4rT0z4Y9W-K1khbdb4jhPRE6RCXFwpzysNKoi-_eTLKf2rnv2zdEE3LWd4WcTWiyX2FHQHW33xF2v7xMvIzV1sYD04c_ZHnhPDVtp8AocmhRgsT0m5a0jDMgdeyeOlTylMp_RTXsc7AzW7oSNzIGJPPLAyp7MmscAOJjN4DbP4LBqLfclze55INOpLtS8ImR32SfQXWgxwd5l9utecQg9ejyKngGLf4HvdL5v5smDL6DltW66kuJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2fb5139f3.mp4?token=jnHWoBMvEghnSm8GWYs3LaulZhk6yhrCu-20cgO9BKs2axKcQ3iV_xkQKeoLV4VlK21JFZ-2V8PzvP-9lTA3Nzccix5vjz3xt4rT0z4Y9W-K1khbdb4jhPRE6RCXFwpzysNKoi-_eTLKf2rnv2zdEE3LWd4WcTWiyX2FHQHW33xF2v7xMvIzV1sYD04c_ZHnhPDVtp8AocmhRgsT0m5a0jDMgdeyeOlTylMp_RTXsc7AzW7oSNzIGJPPLAyp7MmscAOJjN4DbP4LBqLfclze55INOpLtS8ImR32SfQXWgxwd5l9utecQg9ejyKngGLf4HvdL5v5smDL6DltW66kuJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز: رئیس‌جمهور ترامپ با قاطعیت شایعات دربارهٔ یک توافق هسته‌ای ضعیف را رد کرد و اعلام کرد که هرگز به تهران «پول نقد تحویل نخواهد داد.»
رئیس‌جمهور ترامپ به لارِنس بیلی جونز؛ (مجری تلویزیونی، مفسر سیاسی و خبرنگار آمریکایی شبکه فاکس‌نیوز) گفت منتقدانی که ادعا می‌کنند او در برابر ایران رویکردی نرم دارد، کاملاً در اشتباه‌اند.
«واقعاً فکر می‌کنید بعد از تمام حرف‌هایی که دربارهٔ این‌که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند زده‌ام، من به‌عنوان رئیس‌جمهور فقط بیایم و پول نقد به آن‌ها تحویل بدهم؟»
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/12415" target="_blank">📅 15:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe86e64833.mp4?token=FGwRzg5KHWdwWtaSEs0y7ZeTrVD0Pg4E8A65QHei91LaKGzIPqhVPRyxcxlyWEXulx_kS8IdmGl2QKzu89sDLipLl0a3N-2TVRCQzkXMuILHk9Ke8YGdjC6PfPkxg8hT8pYCgse-EfSOm2gdoqYWrXPisl2fBHuM5tbPx4VnFmeyaB4Os9S9NGtfUk_JRel_Kahi4yU1jdmXoNux0sVqDe6v6pZCJICy_l6dM-xs4s8r-Ux1dH38cmRQYZbL4RiYt9J4K_u3PeQiOWjgOPl0YX0Yi9Z-jI8P2SDQIxYmD6Azn0dRW3KaQXX6eEppnP97QrYqK0L6aW6Kc0Caqj83ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe86e64833.mp4?token=FGwRzg5KHWdwWtaSEs0y7ZeTrVD0Pg4E8A65QHei91LaKGzIPqhVPRyxcxlyWEXulx_kS8IdmGl2QKzu89sDLipLl0a3N-2TVRCQzkXMuILHk9Ke8YGdjC6PfPkxg8hT8pYCgse-EfSOm2gdoqYWrXPisl2fBHuM5tbPx4VnFmeyaB4Os9S9NGtfUk_JRel_Kahi4yU1jdmXoNux0sVqDe6v6pZCJICy_l6dM-xs4s8r-Ux1dH38cmRQYZbL4RiYt9J4K_u3PeQiOWjgOPl0YX0Yi9Z-jI8P2SDQIxYmD6Azn0dRW3KaQXX6eEppnP97QrYqK0L6aW6Kc0Caqj83ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مذاکرات ایران: رئیس‌جمهور ترامپ با قاطعیت شایعات دربارهٔ یک توافق هسته‌ای ضعیف را رد کرد و اعلام کرد که هرگز به تهران «پول نقد تحویل نخواهد داد.»
رئیس‌جمهور ترامپ به لارِنس بیلی جونز؛ (مجری تلویزیونی، مفسر سیاسی و خبرنگار آمریکایی شبکه فاکس‌نیوز) گفت منتقدانی که ادعا می‌کنند او در برابر ایران رویکردی نرم دارد، کاملاً در اشتباه‌اند.
«واقعاً فکر می‌کنید بعد از تمام حرف‌هایی که دربارهٔ این‌که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند زده‌ام، من به‌عنوان رئیس‌جمهور فقط بیایم و پول نقد به آن‌ها تحویل بدهم؟»
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/12414" target="_blank">📅 15:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">همتی رئیس بانک مرکزی هم در تیمه و برای پیگیری آزادسازی منابع ارزی ایران   راهی قطر شده
قرار شده است که قطر بخشی از پول‌های بلوکه شده ایران را پرداخت کند و بعد آمریکا به آن بپردازد!
سید محمد مرندی، عضو سابق تیم مذاکره‌کننده هسته‌ای: ظاهرا قرار بر این است قطری ها بخشی از پول را برای ما تامین و بعداز آمریکا دریافت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/12413" target="_blank">📅 15:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فاکس نیوز : قالیباف و عراقچی امروز رفتن قطر برای مذاکرات
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/12412" target="_blank">📅 15:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">واشنگتن پست به نقل از یک مقام ایرانی:
بازگشایی تنگه هرمز مرحله‌به‌مرحله انجام میشه. اول مین‌ها پاک‌سازی میشه، بعد محاصره آمریکا برداشته میشه و اون 12 میلیارد دلار دارایی مسدود شده هم آزاد میشه.
یه یادداشت هم امضا شده که اصلا ربطی به توافق هسته‌ای نداره، فقط قول دادیم که مذاکرات رو ادامه بدیم.
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12411" target="_blank">📅 14:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: چیزهایی هست که از اول هم با ایران در موردشان مذاکره نشده بود
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/12410" target="_blank">📅 14:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دیلی‌میل:
تد کروز و لیندسی گراهام رهبری جمهوری‌خواهان رو بر عهده دارن که از توافق در حال شکل‌گیری ترامپ با ایران انتقاد میکنن و اونو اشتباهی فاجعه‌‌بار می‌دونن.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/12409" target="_blank">📅 14:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12408">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ در تروث : «من به تمام دموکرات‌ها، جمهوری‌خواه‌های ظاهری (RINOها) و احمق‌هایی می‌خندم که هیچ اطلاعی درباره توافق احتمالی‌ای که من با ایران در حال انجامش هستم ندارند؛ مسائلی که حتی هنوز وارد مرحله مذاکره هم نشده‌اند.
افراد ضعیف و بی‌اثری مثل سناتور شکست‌خورده تام تیلیس که به‌زودی از قدرت کنار می‌رود یا بیل کسیدی که تازه یک شکست سنگین در انتخابات مقدماتی خورده، یا نماینده واقعاً افتضاح، توماس مَسی؛ آدمی کاملاً کثیف که بعد از خیانت بزرگ به حزبش (و کشورش!) با اختلاف سنگین از یک میهن‌پرست واقعی آمریکایی که مورد حمایت «ترامپ» بود شکست خورد؛ و تقریباً تمام دموکرات‌ها؛ کسانی که کاملاً راهشان را گم کرده‌اند، مدام از سیاست‌های بد و نامزدهای حتی بدتر حمایت می‌کنند، اما همزمان از تک‌تک پیروزی‌های فوق‌العاده من انتقاد دارند.
این افراد بهتر است به خانه بروند و استراحت کنند؛ چون جز ایجاد تفرقه و شکست، کاری انجام نمی‌دهند. به زبان ساده: آن‌ها بازنده‌اند!
توافق با ایران یا یک توافق بزرگ و معنادار خواهد بود، یا اصلاً توافقی در کار نخواهد بود.
این توافق دقیقاً نقطه مقابل فاجعه برجام (JCPOA) خواهد بود؛ توافقی که توسط دولت شکست‌خورده اوباما مذاکره شد و مسیری مستقیم و آشکار برای دستیابی ایران به سلاح هسته‌ای ایجاد می‌کرد.
نه، من چنین توافق‌هایی انجام نمی‌دهم!
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/12408" target="_blank">📅 13:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12407">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خوش چشم (مرشد فیلم صمد)
تحلیلگر صداسیما: پول بشینه توی حساب جمهوری اسلامی میریم پای میز
مذاکره
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/12407" target="_blank">📅 13:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12406">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شبکه ۱۲ عبری: حزب‌الله استفاده از پهپادهای انتحاری را به‌طور چشمگیری افزایش داده است
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/12406" target="_blank">📅 13:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12405">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فوری/ بازگشایی اینترنت بین الملل مصوب شد
ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد.
این مصوبه برای رییس جمهور ارسال شد و در صورت تایید رئیس جمهور جهت اجرا برای وزارت ارتباطات ارسال خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/12405" target="_blank">📅 12:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12404">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بقایی: برای تنگه هرمز عوارض نمی‌گیریم؛ هزینه‌های دریافتی صرفاً بابت خدمات ناوبری و حفاظت از محیط زیست است
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/12404" target="_blank">📅 12:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12403">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربیو:اگر مذاکرات شکست بخورد تقصیر ایالات متحده یا متحدان ما در منطقه خلیج فارس نیست. 100 درصد تقصیر ایران است
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/12403" target="_blank">📅 12:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12402">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی وزارت خارجه:
سفر آقای عراقچی به نیویورک به علت مشکل روادید منتفی است
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12402" target="_blank">📅 12:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12401">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK312CkPMUS1AbyE4Oao9V0zub7tRV0FvO5cbfeQyx-1QUZM96N7UWuYyC-jY3MpT9avBIynhEYHpvZ1NkiEzjnZASHCzsU5S0f0x1sfaKH2PX7-adQd6zIiISqRpxiRaOm42k7YBJVAWBomj5aj37ofrSzg-QxKisHSQbCGprUvW0aKGWUKCs6T9bNhsYTEVdKyTa4K58FWK8gZguDl4g9aXpuD7AICeCu1XTTeibmlOcf-YZh6nwznFC5TJpsJiNXhAdTEFnpPIxaNgNy1Wts41xhKXEtceJcJamimMd3uGoqp_F_iFvlJh-fF4hFBxJe3IykJ4curNjkixWbcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیهٔ مارکو روبیو، وزیر امور خارجه آمریکا
محکومیت درخواست بی‌پروا و خطرناک حزب‌الله برای سرنگونی دولت لبنان
ایالات متحده با شدیدترین لحن ممکن، درخواست بی‌ملاحظه حزب‌الله برای سرنگونی دولت منتخب و قانونی لبنان را محکوم می‌کند.
حزب‌الله بارها درخواست‌های دولت قانونی لبنان برای توقف حملات و احترام به آتش‌بس را نادیده گرفته است. در عوض، به شلیک به مواضع اسرائیل و انتقال نیروها و سلاح‌ها به جنوب لبنان ادامه داده است. این یک کارزار عمدی برای بی‌ثبات کردن کشور و حفظ قدرت خود، به بهای آینده مردم لبنان است.
دولت لبنان در حال تلاش برای بازسازی، احیای کشور، دریافت کمک‌های بین‌المللی و ایجاد آینده‌ای باثبات برای شهروندانش با حمایت کامل ایالات متحده است. اما حزب‌الله، برعکس، فعالانه می‌کوشد لبنان را دوباره به سوی هرج‌ومرج و ویرانی بکشاند.
ایالات متحده قاطعانه در کنار دولت قانونی لبنان ایستاده است؛ دولتی که برای بازگرداندن حاکمیت خود و ساختن آینده‌ای بهتر برای همه مردم لبنان تلاش می‌کند. تهدیدهای حزب‌الله برای خشونت و سرنگونی حکومت، اجازه موفقیت نخواهد یافت. دورانی که یک گروه تروریستی تمام یک کشور را گروگان گرفته بود، رو به پایان است.
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/12401" target="_blank">📅 11:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12400">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سعید قاسمی نژاد مشاور شاهزاده : ‏شاید شما هم مثل من همیشه این سوال را از خودتان می‌پرسید که اگر در سال ۵۷ بودید  آیا اسیر جو زمان می‌شدید و روبروی شاه می‌ایستادید یا کنار او می‌ایستادید و از ایران دفاع می‌کردید. اگر امروز روبروی شاهزاده رضا پهلوی ایستاده‌اید و‌ دشمن اویید قطعا آن روز هم روبروی شاه می‌ایستادید و‌ دشمن او می‌بودید، شک نکنید و به خودتان و دیگران دروغ نگویید.
@withyashar
یاشار : چقدر زیبا یاد آوری کردید ، اتفاقا اگه در اون زمان بودیم جلوی اطرافیان شاه میستادیم !
جلوی فردوست ، جلوی بختیار ، جلوی ارتشید قره باغی و حتی اردشیر زاهدی  و خیلی از حلقه اطرافیان ایشان !
جاوید شاه پاینده ایران !</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/12400" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12399">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ در تروث : یکی از بدترین توافق‌هایی که کشور ما تا به حال انجام داده، «توافق هسته‌ای ایران» بود که توسط باراک حسین اوباما و افراد کاملاً غیرحرفه‌ای دولت اوباما طراحی و امضا شد. این توافق، یک مسیر مستقیم برای ایران جهت دستیابی به سلاح هسته‌ای ایجاد می‌کرد.…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12399" target="_blank">📅 10:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12398">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انتخابات هیئت رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شد، دقایقی پیش پایان یافت
با آرا اکثریت نمایندگان قالیباف رئیس‌مجلس ماند
این انتخابات بصورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت رئیسه مجلس شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر بود.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/12398" target="_blank">📅 10:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12397">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/12397" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12396">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نعیم قاسم دبیرکل حزب الله:به خیابان ها بیاید و دولت لبنان را سرنگون کنید
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/12396" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12395">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/12395" target="_blank">📅 10:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12394">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/12394" target="_blank">📅 10:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12393">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12393" target="_blank">📅 10:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12392">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/12392" target="_blank">📅 10:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12391">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">در مسیر قاهره در یک کاروانسرا استراحت می‌کنیم. نگران نباشید، کمی بعد حرکت می‌کنیم.
😃</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12391" target="_blank">📅 09:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیویورک پست : ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12390" target="_blank">📅 09:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۱۵۴۰ تا دایرکت نخونده دارم ، یه فرصت بدید شاید نتونم این سری لایک هم کنم والی همه رو یکم دیگه میخونم
🥲
🙌🏾</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/12389" target="_blank">📅 09:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شبکه خبری سی‌بی‌اس به نقل از مقام‌های آمریکایی آگاه گزارش داد اطلاعات ایالات متحده نشان می‌دهد خامنه‌ای، رهبر جمهوری اسلامی، عملا در مکانی نامعلوم پنهان شده و دسترسی بسیار محدودی به دنیای خارج دارد.   بر اساس این گزارش، مقام‌های حکومت ایران تنها از طریق شبکه‌ای…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/12388" target="_blank">📅 09:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12387">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکونومیست: گزارش‌ها حاکی از آن است که عربستان سعودی از دونالد ترامپ درخواست کرده است هرگونه حمله جدید به ایران را تا پس از حج به تعویق بیندازد.
همچنان ترس وجود دارد که اگر درگیری دوباره آغاز شود، زائران در آنجا گیر خواهند افتاد.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/12387" target="_blank">📅 09:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فایننشال تایمز: عصبانیت رئیس‌جمهور چین از «افزایش توان نظامی ژاپن» در حضور همتای آمریکایی‌اش
پاسخ ترامپ: ژاپن به دلیل تهدیدات کره شمالی، به دفاع قوی‌تری نیاز دارد
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/12386" target="_blank">📅 09:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شبکه خبری سی‌بی‌اس به نقل از مقام‌های آمریکایی آگاه گزارش داد اطلاعات ایالات متحده نشان می‌دهد خامنه‌ای، رهبر جمهوری اسلامی، عملا در مکانی نامعلوم پنهان شده و دسترسی بسیار محدودی به دنیای خارج دارد.
بر اساس این گزارش، مقام‌های حکومت ایران تنها از طریق شبکه‌ای پیچیده از پیک‌ها با او ارتباط می‌گیرند و حتی مقام‌های ارشد نیز از محل دقیق او اطلاع ندارند یا راهی برای تماس مستقیم با او ندارند.
@withyashar
سی‌بی‌اس نوشت این اختلال ارتباطی یکی از دلایل کندی در اعلام جزئیات توافق احتمالی تهران و واشینگتن است؛ زیرا پس از ارسال پیشنهادهای آمریکا، دسترسی دشوار به خامنه‌ای می‌تواند پاسخ تهران را با تأخیر قابل‌توجه روبه‌رو کند.
این شبکه همچنین به نقل از مقام‌های آمریکایی نوشت بسیاری از مقام‌های جمهوری اسلامی هفته‌ها را در پناهگاه‌های مستحکم می‌گذرانند و جز در موارد ضروری با یکدیگر گفت‌وگو نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/12385" target="_blank">📅 02:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جنگ مارکت ها با ترامپ : نفت اومد زیر صد ! هم اکنون ۹۹$
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/12384" target="_blank">📅 01:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Marde Tanha Remix (t.me/withyashar)</div>
  <div class="tg-doc-extra">Farhad (IG @yashar)</div>
</div>
<a href="https://t.me/withyashar/12383" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12383" target="_blank">📅 01:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
۷ روز دیگه دوشنبه شب ۱۱:۱۱ دقیقه تهران به شاهزاده پیغام میدیم تا من با ایشون صحبت کنم ! و حرف های شما رو برسونم ! این یک فراخان اینترنتی هست ، هر شرایطی که میتوانید فراهم کنید که افراد بیشتری به ما ملحق بشوند ! حتی شما دوست عزیز که فیلترشکن میفروشی ! خواهش…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12382" target="_blank">📅 01:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۷ روز دیگه دوشنبه شب ۱۱:۱۱ دقیقه تهران به شاهزاده پیغام میدیم تا من با ایشون صحبت کنم ! و حرف های شما رو برسونم ! این یک فراخان اینترنتی هست ، هر شرایطی که میتوانید فراهم کنید که افراد بیشتری به ما ملحق بشوند ! حتی شما دوست عزیز که فیلترشکن میفروشی ! خواهش میکنم اکانت تست بده تا همه باشند حتی اندک تا صدای ما شنیده بشود ! همین ! انقدر این کار را انجام میدیم تا هر شخص دیگری هم پیج ایشون دستشه مجبور بشه این ارتباط رو برقرار کنه ! خیلی واضح میگم من عقب نمیکشم !</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/12381" target="_blank">📅 01:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به خاطر ایران به خاطر تمام جاوید نام های میهن از روز اول این رژیم و اولین جاوید نام محمد رضاشاه پهلوی و تمام ژنرال ها به خاطر او سرباز وظیفه که اینجا خدا حافظی کرد ، اون خواهرم که پدر مادرش ۸۰ سالشونه و مریضن و تو ماشین گریه میکرد به خاطر تمام جونهایی که پیغام دادن و آرزوشون او موتور بود که هر هفته گرون میشد به خاطر حتی اون بچه هیئتی که گفت من اتاق جنگیم ! دوشنبه شب به همه بگین هر جور شده بیان ! و پیغام رو برسونیم !</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/12380" target="_blank">📅 00:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حق گرفتنیه دادنی نیست
💪🏾</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/12379" target="_blank">📅 00:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12378" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه تا دوشنبه دیگه  زدن زدن ، نزد به بچه های ایرانم بگین تو پلتفرم های داخلی هرجور شده خودشونو برسونن ! فقط یک لحظه همه باهم یه پیفام میفرستیم برای شاهزاده رضا پهلوی ! و هر جور شده ارتباط میگیرم با شخص ایشون هر جور شده و هر کسی بیاد جلومون زمین میزنیم فقط برای ایران و شده ۲۰۰۰۰۰۰۰ پیغام بدم شبانه روز این کار رو میکنیم شده اعتصاب غذا میکنم ! محترمانه به عنوان یه جون ایرانی تبعید اجباری شده ! و نماینده همین خونوادمون !
میدونین که من شده انقدر بیدار میمونم و نیمخوابم تا جواب بگیرم ! هر پیغام هم اسکرین میزام !
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/12377" target="_blank">📅 00:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیغام های زیاد اینچنینی گرفتم چرا با شاهزاده صحبت نمیکنی … ولی امروز شخصی نوشت تو نمیدونی ایران چجوری پشتت هستند ما با هزار بدبختی پیغام ها و صحبت هاتو میفرستیم تو پلتفرم های داخلی !! اگه میدونستی انقدر خودت رو سر حرف بعضی ها عذاب نمیدادی!!!  در نتیجه این تصمیم رو گرفتم ! امروز ما نباید مانند دیروز باشد !!!</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12376" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">توییتِ سخنگوی فارسی زبان ارتش اسرائیل و طعنه به ترامپ : کس نخارد پشت من جز ناخن انگشت من !
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/12375" target="_blank">📅 00:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار : حجاج امسال دو بار حاجی میشن
😃</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/12374" target="_blank">📅 00:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مقام آمریکایی به سی‌ان‌ان:
آزادسازی منابع مالی ایران منوط به گشایش کامل هرمز و اجرای تعهدات هسته‌ای خود است!
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12373" target="_blank">📅 23:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک مقام آمریکایی به شبکه «فاکس‌نیوز» گفت دونالد ترامپ، رئیس‌جمهوری آمریکا ممکن است به ایران هفت روز مهلت دهد تا به یک توافق «قابل‌قبول» برسند
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/12372" target="_blank">📅 23:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkU7EuQjzBxJT73TMuBC8ARVR6fbdiFfNa3b_3uMXTr4qjTVFIDiTIK20j56M9YemlRsxfbxWrGlgkK03tH4NrbCcC-dycA_EzIarSc5Q3VzTJbWq9ano4_zlDnbKLRMJjZZDAWiZ7j4A00Uh3n07oFHi3gNdS1z5TytOksbK7phyVDPvvrFwnAKPYawdH8I3jgq4oyqYb7q99M-nciSW0XJH68lkwyEOoQirNJwrXxsTgekn5TAQQ9p6SqcR3TPvk2Q_7TvgY33SR77JSU8sbKi4VehaZaO-DtLV9pP9tAxbiVVYAikiMcVWc1yR0QD2TWhnncxv9igwrgXd7PrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث: از شما بابت توجهتون به این موضوع متشکرم.
@withyashar
😂
🤯</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/12371" target="_blank">📅 23:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حوصلم سر رفت</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/12370" target="_blank">📅 23:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رسانه وزارت خارجه ایران: در موضوع آزادسازی دارایی‌ها که مورد اختلاف است در حال حاضر راه‌حلی برای آن وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/12369" target="_blank">📅 22:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چرچیله زمانه را بشناس…
😃</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12368" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/12367" target="_blank">📅 22:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر امور خارجه ایالات متحده مارکو روبیو گفت که توافق احتمالی با ایران حمایت منطقه‌ای دریافت کرده است، اما هشدار داد که یک توافق هسته‌ای نمی‌تواند «در ۷۲ ساعت روی پشت یک دستمال کاغذی» به دست آید.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/12366" target="_blank">📅 22:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/12365" target="_blank">📅 22:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsL1fuc54_ISreq4lqrFnh90D7DRF7pXXuc0xo1TDOx9n8DVHG9USIl8fKrlOSNhfyxeQHmC_Ca82NdqoStouyn-X5AEdMN4le9sEUWdE4ILfajZpbFac2fXjrFalBDarRRZjoE03gN1g4l9WaKFuBCLg3sbOrMI04SYJ535pDlnSH_mtWlDwd7X6YSiw-cpzUOc97sy-dAL6NNPjnYe4qzH-A-Tq2Va-FDwnSytFH-pghv6s8JkaOIyiQS4AmvRw7RhgJBFyQbNvtxl84c7DsDtBbqN0mAXwUmeyEt-CCaOuJZI0kNBVbVpoSqCZAu2_KW0GqQJEHGkeaOB6aPUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در شبکه Truth Social:
اگر من با ایران به توافق برسم، آن یک توافق خوب و اصولی خواهد بود؛ نه مثل توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد داد و یک مسیر کاملاً باز برای دستیابی به سلاح هسته‌ای فراهم کرد.
توافق ما دقیقاً برعکس آن است، اما هنوز کسی آن را ندیده و نمی‌داند دقیقاً چیست. حتی به طور کامل هم نهایی نشده است. پس به افراد شکست‌خورده‌ای که درباره چیزی که از آن هیچ اطلاعی ندارند انتقاد می‌کنند، گوش ندهید.
برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد امضا نمی‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/12364" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:محاصره دریایی علیه ایران به صورت کامل ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12363" target="_blank">📅 21:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12362" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12361" target="_blank">📅 21:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیویورک تایمز: یک مقام آمریکایی می‌گوید ایالات متحده و ایران در اصول برای بازگشایی تنگه هرمز توافق کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12360" target="_blank">📅 21:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12359">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12359" target="_blank">📅 21:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مقام آمریکایی به CNN:
تحریم‌ها علیه ایران نمی‌تواند قبل از مهار برنامه هسته‌ای آن کاهش یابد
وی گفت: ما در مورد آزادسازی وجوه ایران به عنوان بخشی از توافق مذاکره نکرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/12358" target="_blank">📅 21:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو توافق وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12357" target="_blank">📅 21:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به قول مانوک اگه الان آشمز شدید این رو هم ببینید…
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/12356" target="_blank">📅 21:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">طبق گزارش فاکس نیوز، ترامپ می‌خواهد توافق پیشنهادی توسط مذاکره‌کنندگان او، از جمله استیو ویتکوف و جرد کوشنر، اجرا شود؛ اگر این شرایط برآورده نشوند، هیچ توافقی صورت نخواهد گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/12355" target="_blank">📅 21:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الجزیره: یه منبع ایرانی به ما گفته؛ آمریکا داره از چند تا توافق قبلی خودش عقب می‌کشه، مخصوصاً سر آزاد کردن پول‌های بلوکه‌شده ایران و مدل آتش‌بس لبنان؛
تو متن تفاهم‌نامه، اسرائیل میخواد دستش باز بمونه که هر وقت گفت «تهدید حس کردیم» دوباره تو لبنان عملیات بزنه و بهشون حمله کنه، ولی ایران مخالفه و میگه آتش‌بس باید واقعی، کامل و دائمی باشه.
پاکستان پیشنهاد داده فعلاً بخش‌هایی که توافق شده امضا بشه و بقیه اختلافات بعداً حل شه، ولی ایران گفته نه؛ یا همه بندها کامل و تضمینی حل میشه یا کلاً امضایی در کار نیست.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12354" target="_blank">📅 20:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فاکس نیوز نقاط اختلاف در توافق ایران و آمریکا را اعلام کرد:
1. اسرائیل خواستار تضمین «آزادی عمل نظامی» علیه تهدیدها در لبنان است و ایران این را رد می‌کند.
2. تهران خواستار آزادسازی فوری دارایی‌های خود است و واشنگتن امتناع می‌کند و اصرار دارد که این موضوع به فرمول نهایی توافق مرتبط شود.»
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/12353" target="_blank">📅 20:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12352" target="_blank">📅 20:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نعیم قاسم رهبر گروه تروریستی حزب الله:
ایران با رهبری مجتبی خامنه ای آمریکا و اسرائیل را ذلیل کرد
@withyashar
🤣</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/12351" target="_blank">📅 20:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تسنیم: علیرغم برخی گفتگوهای امروز، کارشکنی‌ های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
بر این اساس، در حال حاضر همچنان امکان منتفی شدن تفاهم وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12350" target="_blank">📅 20:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">علی هاشم خبرنگار الجزیره: کمتر از ۲۴ ساعت پس از ظهور خوش‌بینی در مورد امکان توافق‌نامه ایران و آمریکا، حال‌وهوای منفی دوباره سر برآورده است.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12349" target="_blank">📅 20:18 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
