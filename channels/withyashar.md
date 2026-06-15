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
<img src="https://cdn4.telesco.pe/file/sm34u3GX-FugpzXxNJZws_30XSj_ZCYJqvCElZwthPaVd-zLvbG-yQUz3_1gbV-yWh_2Lln7JQzHrWcdh-JS5tJbB_ueNsWTWmd1D1-xLQ2eI9cGFU_ptInRD8ck6-lk5h0D8lxkDQ1i_bXSdHAHwIk7RdrxiGhA0WspqYVdC0u-EP26RI_XWLH_ihOEgJBHWluI41VN7mc8v4qNI7cRE0CesdaRp0PIdVljHVSMYDosrEjAGMxkSFq0rU7lMYVwxWEs1f4FD9XHKZruWeuZum_-8-y2uFhhIKurg3c3c_1z_BQnW-nTSZJ-cs4irIALxSbGNu6DArus2hlPkVpO0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-15004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/withyashar/15004" target="_blank">📅 22:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پست جدید که در اون هنرنمایی هم کردم براتون کلیک کنید و حتماً کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DZngOTKRtYt/?igsh=MWwzcTZmaW9oZndxcQ==
⁨ اتاق جنگ با یاشار : سفر قاهره «ملودیک»⁩</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/15003" target="_blank">📅 22:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو: از موارد مورد توافق بین ایران و آمریکا مطمئن نیستم ولی قطعا در انتخابات پیروز خواهم شد
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/15002" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSMPGHtKuoVggtPrrnefCQxcUoknwx1nCu9dz7p1JcXiv3BThtqGeBGYAn_rD8g9yPxVGDPEfJFMjUzhF3mGPM1ik1OYVM7LdrI01wa8-KCZMsV5eaZLZyBJFrSIk9cfIkv3H5PC8KPfCZ0WUcqu0Q95OgCDccNZ3_BnXz0gwzM0ZAiTFyDE_zs9OPKA5GL49aJ9wEGjx5gkgnK0nHEq4jyv6RPHEDro8xXrM7t4PmS-w02pFOgs9V7BkaCPJm6VGp8iAL3L61BJA9w63oNrFiPp-_PzzPkz5PdDHq1nxE-MxgsPozsB3yg8f2MAJkAPS6G10iTaCexJRqzHHwsy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/15001" target="_blank">📅 22:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو: تا خلع سلاح حزب‌الله، اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد.
همون کاری با غزه کردیم، با جنوب لبنان هم خواهیم کرد؛ همونطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست، حزب‌الله هم در آینده نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/15000" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهو: توافق با ایران توسط ترامپ منعقد شد، این تصمیم اوست و ما منافع خود را داریم‌‌
ترامپ رئیس‌جمهور آمریکاست و من نخست‌وزیر اسرائیل؛ من از منافع کشور خودم دفاع می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/14999" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو: من نگفتم هدف ما سرنگونی رژیم ایرانه، گفتم میخواهیم به مردم ایران برای انجام این کار کمک کنیم
@withyashar
یاشار : توجه کن این جمله بار حقوقی داره با این حال بنیامین نتانیاهو بارها این حرف رو زده</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/14998" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو
: مبارزه تمام نشده است. ما باید همچنان هوشیار، قوی و مصمم باشیم تا از خود تا حد امکان دفاع کنیم. این نه تنها در مورد ایران، بلکه در مورد بازوهای تروریستی ایران نیز صادق است. ما به شیوه‌ای بی‌سابقه به آنها ضربه زدیم. ما این کار را در غزه، لبنان، سوریه، یمن، اردوگاه‌های پناهندگان در یهودا و سامره و همه جا انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/14997" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو: من با ترامپ موافق نیستم،
بنابراین، اسرائیل هر کاری که لازم باشد در برابر ایران انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/14996" target="_blank">📅 21:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شبکه ۱۳ اسرائیل به نقل از یک منبع:
تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/14995" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=SJ72WpBt3mCJPcZeUFwG8ifeB6qhqyG3rEbIMAk4KTmvYuarFKIzMfQetP_d7FTGA66-6IAiE2EB9aZOnLXxem0CUbx6TNHZ60-N66y-alr3WaIwGW46jDQutyaixIsIKcptM4_Py8HHfUkg-NIlMeUJhr7I14Sgjo6kfYx7tPr5Qo8diPo1Yq00tjMx41eEeZHrUJX93PrdjerjuNdj4mbda32LoZ7fn-_mijsAWm8cWw8P3EnIJHzXAkscTidC3QgUvKhaA-VVt3zOOD0gep9hHu7HXhjZksR-_8_a-Is1y6bVeNQUk_BRUfpLPPGkGOIVtpRjPSQLtzCQ7zvTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=SJ72WpBt3mCJPcZeUFwG8ifeB6qhqyG3rEbIMAk4KTmvYuarFKIzMfQetP_d7FTGA66-6IAiE2EB9aZOnLXxem0CUbx6TNHZ60-N66y-alr3WaIwGW46jDQutyaixIsIKcptM4_Py8HHfUkg-NIlMeUJhr7I14Sgjo6kfYx7tPr5Qo8diPo1Yq00tjMx41eEeZHrUJX93PrdjerjuNdj4mbda32LoZ7fn-_mijsAWm8cWw8P3EnIJHzXAkscTidC3QgUvKhaA-VVt3zOOD0gep9hHu7HXhjZksR-_8_a-Is1y6bVeNQUk_BRUfpLPPGkGOIVtpRjPSQLtzCQ7zvTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:  ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/14994" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/14993" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو: «اسرائیل تا هر زمان که لازم باشد در “مناطق امنیتی” باقی خواهد ماند.»
«ما شراکت‌های جدیدی را در سراسر منطقه و فراتر از آن شکل خواهیم داد، در حالی که توانایی اسرائیل برای تولید و تأمین مستقل تسلیحات خود را تضمین می‌کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/14992" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/14991" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مقامات آمریکایی اعلام کردن حتی با وجود توافق قصد عقب نشینی از منطقه را نخواهیم داشت و نیروهای آمریکایی در منطقه خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/14989" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/14988" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما از لبنان عقب‌نشینی نخواهیم کرد، اما از این پس هر عملیات نظامی قابل بررسی خواهد بود.
ما برای دستیابی به توافق بین واشنگتن و تهران قربانی شدیم.
معاون رئیس جمهور آمریکا از نتانیاهو خواسته است تا حضور اسرائیل در لبنان را کاهش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/14987" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو: می‌توانید طناب را با آمریکایی‌ها بکشید، اما نباید آن را پاره کنید.
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/14986" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال ۱۳ اسرائیل به نقل از منابع:
گفتگوی پرتنشی بین نتانیاهو و معاون رئیس جمهور آمریکا در مورد حضور اسرائیل در لبنان صورت گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/14985" target="_blank">📅 20:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرنگار : آیا قصد دارید در تشییع قائد امت، حضرت آیت‌الله عظما جانشین امام زمان علی خامنه‌ای شرکت کنید؟  ترامپ: بله @withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/14984" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرنگار : آیا قصد دارید در تشییع قائد امت، حضرت آیت‌الله عظما جانشین امام زمان علی خامنه‌ای شرکت کنید؟
ترامپ: بله
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14983" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fba57ac4d.mp4?token=l-O1WPsVPO1P2z1HuUJGsd_z4_8TbX-coopLj0vuXlBeNpDiq70U0qLGNSYbk9ZaCjZbsRevmaiX-5rguvIGsQp5vyh0zVdRyT-J5CPs8QvsbfJIJHsUlieT7GGg8Ti1I2OpMLksnqJQjqUVbL3-YBtkny0VahTGRKId-rBbtruU_WFnPJ3wkORFa-rktK6kChyfmbN0S4xmA4ENIK1At6i5ku0xFexwWYX2aPTGlyQjdnEB1SbYzuRYzdmBrira-0R20DGCIVAmpB70A2NfgSlX5xuyfvt-EtK25eoOVEVb3YM-rqeFWgL0k3vxKVzBho9zl3Avd1NjW67CrOU0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fba57ac4d.mp4?token=l-O1WPsVPO1P2z1HuUJGsd_z4_8TbX-coopLj0vuXlBeNpDiq70U0qLGNSYbk9ZaCjZbsRevmaiX-5rguvIGsQp5vyh0zVdRyT-J5CPs8QvsbfJIJHsUlieT7GGg8Ti1I2OpMLksnqJQjqUVbL3-YBtkny0VahTGRKId-rBbtruU_WFnPJ3wkORFa-rktK6kChyfmbN0S4xmA4ENIK1At6i5ku0xFexwWYX2aPTGlyQjdnEB1SbYzuRYzdmBrira-0R20DGCIVAmpB70A2NfgSlX5xuyfvt-EtK25eoOVEVb3YM-rqeFWgL0k3vxKVzBho9zl3Avd1NjW67CrOU0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار به ترامپ : آقای رئیس‌ جمهور، آیا این توافق شامل لغو زودهنگام بخشی از تحریم‌ های ایران میشود؟ این موضوع از چه زمانی اجرایی خواهد شد؟
ترامپ: نه، چنین چیزی در توافق وجود ندارد، این توافق بیشتر به رفتار طرف مقابل مربوط میشود
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/14982" target="_blank">📅 20:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: احتمال دارد جمعه حضور داشته باشم و با ایرانی ها دیدار کنم
از اینکه مجبور شدیم دو شب دیگر به حمله ادامه دهیم، احساس بدی داشتم. و فکر می‌کردم برای بار سوم هم همینطور، اما ما قبل از آن توافق را انجام دادیم.
فکر می‌کنم اتفاقات خیلی خوبی قرار است در خاورمیانه رخ دهد.
قیمت نفت در حال سقوط است و بازار سهام مثل موشک در حال افزایش است
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/14981" target="_blank">📅 19:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: می‌خواهم یادداشت تفاهم با ایران را منتشر کنم زیرا سندی مهم و قدرتمند است و ما به زودی آن را منتشر خواهیم کرد
تنگه هرمز پس از جمع‌آوری مین‌ها به‌طور کامل‌ بدون عوارض باز خواهد شد
کاهش تحریم‌های ایران به رفتار این کشور بستگی دارد
اکنون ما می‌خواهیم ببینیم چگونه می‌توانیم مناقشه در لبنان را حل کنیم و باید در این مورد با اسرائیل صحبت کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/14980" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: توافقی که اوباما با ایران انجام داد، این کشور را قادر به ساخت سلاح هسته‌ای می‌کرد
ما خواهان روابط خوب با ایران هستیم و اگر این امر محقق نشود، به جنگ باز خواهیم گشت و امیدوارم این اتفاق نیفتد
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14979" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: ما با ایران تفاهم‌نامه‌ای امضا کردیم و تنگه هرمز تا حدی بازگشایی شده است
تنگه هرمز روز جمعه به طور کامل باز خواهد شد
: توافق با ایران به نفع منطقه خاورمیانه خواهد بود
ایران سلاح هسته‌ای نخواهد داشت و من با این موضوع موافقت کردم. این اصل موضوع مناقشه بود
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14978" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فوری: اولین سخنرانی مجتبی بعد از پایان جنگ و توافق با آمریکا.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/14977" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81cca2afa.mp4?token=QcY_B3jHB2TZmrWeYZlnI7YXA0_dCu1vDAidlxgkKCrLn-_0IHqC2sow6osfVvfmjoD9Q5KMsjdykNsVcr9BqvGfhDq2xPIEUqOsRz0hQoxb2MuSlk5q661lU3CGEM97LBVBaJtdPnKT2M2k2WWdYJEihFHF1V1B4oYInfID_O5u0pHp5K9r8RP7riNMMA1sU2gfBFffuw2bhKLNo9vK_duQ9h0LuR--tlvwbJJL2X2f2jz77vegilEgrIfiSzUjyT3BciJXv8Bm_q5yICyGVDQbTONJ3jVRWiFNa-8YGUeZzmSJuNPgcpMt04JQAC9NGk--MREFsCNV0WEyyET3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81cca2afa.mp4?token=QcY_B3jHB2TZmrWeYZlnI7YXA0_dCu1vDAidlxgkKCrLn-_0IHqC2sow6osfVvfmjoD9Q5KMsjdykNsVcr9BqvGfhDq2xPIEUqOsRz0hQoxb2MuSlk5q661lU3CGEM97LBVBaJtdPnKT2M2k2WWdYJEihFHF1V1B4oYInfID_O5u0pHp5K9r8RP7riNMMA1sU2gfBFffuw2bhKLNo9vK_duQ9h0LuR--tlvwbJJL2X2f2jz77vegilEgrIfiSzUjyT3BciJXv8Bm_q5yICyGVDQbTONJ3jVRWiFNa-8YGUeZzmSJuNPgcpMt04JQAC9NGk--MREFsCNV0WEyyET3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای شرکت در نشست سران گروه هفت (G7) وارد شهر اویان له‌بن در فرانسه شد
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/14976" target="_blank">📅 19:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpfN8FRCecCJloIowEQQYeDz0szQ2I2UA1d7DY6LZLcEsjOi0BXUSENusAKhCWiFu0uA-IrLYrUa9GNOZ0l6yMJzY9ot4iUKFQhBkV-wFOAlXn2qMJDh8_Qo4zrJOvlv0-Ug-1CggFot7W2Hfoql0I59DWLkqwJdeurlYSTg3ptayzolqgN0Y4Z_GqrNWKlgaLMy1WHEC10kMVGf3oP4ylugJasmxKltc9J4FeWSON4DKsSI3Szehz8rau13h-G0QaC04XaD7V6eC2HjyIuRk5btRklCB1odakaxILAWsk7TrQD_ZL3m7-Y8VJCAiOlxs-qBMr0J8IUX5B3ez-Ar1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر ماهشهر همین الان
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14975" target="_blank">📅 19:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
به وضعیت کاملاً غیرقابل قبولی رسیده ایم که ایران در مورد آزادی عمل ما در لبنان «حق وتو» دارد و این یک واقعیت پوچ و غیرقابل قبول است.
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14974" target="_blank">📅 19:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/14973" target="_blank">📅 18:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye4u7suXDDa3S8ZIUvmr4_CmHyDwVGSV25169ZGrJTegCwf4B_2gZWW5O82vWawbLyMtAGAV-USykpIV3fsZR3AGUdrOsa0fd6vEVUzMreLynvss-pfydYzITB6KbHMI6O2C27MMCptzhY99ghG08w4Z_yu4DLpThmSIjPguuV1cZlBVrPK1DvjY9ktzifxtuWCqW0rnc6B0aq_9iVYy6WG4NU9vOydoQtxNtZDCUN1lea21PD1yAa7KJd_uWQc65gssmpu8HDy7AR4sei6imlQvxbOXHbTpj8tfqB9dEG398CsBmmAYcQhS7bfh_B_vt7AAPEbU8t7Me5uKIhTXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرجنگی عمل نکرده موشک کروز تاماهاوک در ورامین
این حمله چند شب پیش انجام شد و ده ها سایت راداری در سراسر ایران اعم از کرج و تهران و چند سایت قزوین و جنوب کشور توسط ۴۹ موشک تاماهاوک منهدم شد ( به جز یک موشک تاماهاوک )
موشک های تاماهاوک بار دیگر نشان دادند از دقت فوق العاده ای در زدن اهدافشان برخوردار هستند.
@withyashat</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/14972" target="_blank">📅 18:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو تا چند ساعت دیگر سخنرانی خواهد کرد و این اولین واکنش رسمی او به اعلام توافق پس از ساعت‌ها سکوت است
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14971" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14970" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/14969" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جزئیات دیگری از یک اتفاق قابل توجه درباره ساختار تفاهم اسلام‌آباد
یک منبع نزدیک به تیم مذاکرات در گفتگو با خبرنگار تسنیم، جزئیاتی از یک اتفاق قابل توجه در روز آخر مذاکرات مطرح کرد : بند 13 تفاهم‌نامه مربوط به این موضوع است که تا زمانی که برخی بندهای دیگر تفاهم‌نامه عملیاتی نشده، مذاکرات درباره توافق نهایی یعنی موضوع هسته‌ای صورت نمی‌گیرد.
وی خاطرنشان کرد: تا پیش از روز آخر مذاکرات، بند 13 شامل بندهای 4 و 5 و 10 و 11 بود؛ بند 4 مربوط به رفع محاصره دریایی، بند 5 مربوط به آغاز بازگشایی تنگه هرمز، بند 10 مربوط به اسقاطیه تحریم‌های مربوط به فروش نفت، پتروشیمی و مشتقات ایران و همچنین بند 11 مربوط به آغاز آزادسازی اموال بلوکه شده ایران است.
بنابراین بند 13 به این اشاره داشت که اگر این 4 بند گفته شده (4 و 5 و 10 و 11) انجام نشود، مذاکرات توافق نهایی آغاز نمی‌شود.
این منبع مطلع تاکید کرد: اتفاق مهمی که روز آخر مذاکرات به وقوع پیوست این بود که با پیگیری ایران، بند 1 نیز به بند 13 اضافه شد.
به گفته این منبع آگاه، معنای مهم این اتفاق آن است که اگر جنگ و هرگونه عملیات نظامی، از قبیل ترور و ... در ایران یا جبهه مقاومت از جمله لبنان اتفاق بیفتد، طبق تفاهم هیچگونه مذاکراتی برای توافق نهایی صورت نمی‌گیرد و طبیعتا اجرای تفاهم‌نامه (از جمله بازگشایی تنگه هرمز) از لحاظ ماده ۱۳ متوقف خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/14968" target="_blank">📅 18:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی: جمعه تفاهمنامه ایران و آمریکا امضا می‌شود
اقتصاد ما نباید خود را متکی و موکول به این قبیل توافقات اقتصادی از طریق مذاکره با آمریکا بکند
در راستای منافع کشور، نیمی دیگر از راه مانده که باید طی کنیم که نیمه سختی خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/14967" target="_blank">📅 18:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3gJ-K4mdRwKJxBKSdyntkU5TbW9eANzP6ps-cu_jpqWzgHX0HpForTIgYgLU5MV_emlgsAOm6WTpAP174vubJtsMQSmsv49GimemEL7S1RCoEQILNCkqG9anYnaTOvE4_3eEGhgDWBcYGIvia-KZIkhTe6kPUul65IhPJCR1riU-Ysh6oCchK8FLTBQ4C07M47OQKDFP8OX9GUCmS65CbsueNYtZENJvxTq8k52ySKfuuWoeokOLUZ4n8QSHWuPq43uY88-Nby5mj_7ZTwAgFN6s1Ib20mv8a4R3ObUXYjnAr7r1GbwyRY1Sv0cthfFHNTWZCrbKMbSApXWsViKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث: متأسفانه، اگر افراد را از کشورهای جهان سوم وارد کنید، به سرعت خودتان تبدیل به یک کشور جهان سوم می‌شوید و هیچ کاری نمی‌توانید در این باره انجام دهید
آمریکا را دوباره بزرگ کنیم!
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/14966" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادعای جی‌دی ونس درباره ایران: ما دیروز به صورت دیجیتالی پیش توافق را امضا کردیم
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/14965" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=NiZewHQpNYihyGg_ZhTI-OQjf72gz14dM5ZhOI1fnSH4U-ybkGtWFM5CWBMNxco6_CiA9moNR_1nG4MxZaLVie7XKfclzjhor4LA62TXVbonXbIbYXDKvopYPu5OSomnPWTJAyShXORYKMTK4kT67b7VtSyf_2Km3hUSXdwWWhhY4FzHZjAV0Uv3OE3fC9ql_rFDlDUVJXWi0XR9maSlK_yg0i5wC1lUmKfWAScNlDAnDsAoP97xSYuOxGDdKATpXOGo0Eup6zjxLStITtGVV8Vj1HYK8hEumRjWbOTvUcmh9xZQRWWYejmihbYf8D02j2EDxx6ai0yq0gt1iLexP7ha6SmIhYacZ0aHEjM99ROHiIW7BlX_r4RMRoObmJHzJHpk5oIyi4WnYRSIWvAdIf8nva5d4Hpd3ggMolF7pzo4bLIBjvyKt9A0hzOAlBgvvfgWVVzaTGAO1qwhStn7xApoGxLTOYpuI1GN5yNGm6hEs09WRARr-8bzxW1CPWzT5o6aba2ZcGOa1DLG8cARZVPF8MYmRSf_zmCDD_1agf0AHaRa58inUC5sH9hMXTLHW1ZTvQmsTrdZbUHWSGEzBvgMeoMDZ55UUQrYSbofDJfIdYcy3-frsOhzXHRvUcZ9h1renWm3FcqzP0C0se_VY8E5stkDq5rC7WdDDTeZB4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=NiZewHQpNYihyGg_ZhTI-OQjf72gz14dM5ZhOI1fnSH4U-ybkGtWFM5CWBMNxco6_CiA9moNR_1nG4MxZaLVie7XKfclzjhor4LA62TXVbonXbIbYXDKvopYPu5OSomnPWTJAyShXORYKMTK4kT67b7VtSyf_2Km3hUSXdwWWhhY4FzHZjAV0Uv3OE3fC9ql_rFDlDUVJXWi0XR9maSlK_yg0i5wC1lUmKfWAScNlDAnDsAoP97xSYuOxGDdKATpXOGo0Eup6zjxLStITtGVV8Vj1HYK8hEumRjWbOTvUcmh9xZQRWWYejmihbYf8D02j2EDxx6ai0yq0gt1iLexP7ha6SmIhYacZ0aHEjM99ROHiIW7BlX_r4RMRoObmJHzJHpk5oIyi4WnYRSIWvAdIf8nva5d4Hpd3ggMolF7pzo4bLIBjvyKt9A0hzOAlBgvvfgWVVzaTGAO1qwhStn7xApoGxLTOYpuI1GN5yNGm6hEs09WRARr-8bzxW1CPWzT5o6aba2ZcGOa1DLG8cARZVPF8MYmRSf_zmCDD_1agf0AHaRa58inUC5sH9hMXTLHW1ZTvQmsTrdZbUHWSGEzBvgMeoMDZ55UUQrYSbofDJfIdYcy3-frsOhzXHRvUcZ9h1renWm3FcqzP0C0se_VY8E5stkDq5rC7WdDDTeZB4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: ایرانی‌ها می‌گویند قرار است به یک صندوق ۳۰۰ میلیارد دلاری برای بازسازی دسترسی داشته باشند. درست است یا نادرست؟
جی‌دی ونس: چنین چیزی می‌تواند در دسترس آن‌ها قرار بگیرد، مشروط بر اینکه به تعهدات خود در این توافق پایبند باشند.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/14964" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLo-DfizU2EnGt-MpCroH01ugMoTL5v7DyFq6aTYN6QUEj2p10E0QM9Ex4fOh_CiGTJ4kQ6_Z9sDXOVrpY_UZU_2fEaFS6ceL8dKoCDejJx7d5YMD8hXJCU2Vyb8w0pnN0JlOfZ74XUUA_oJ9r3pBM4DsgIAkp7wk-58WhEeTlno85F4ICzcmMNXkLAiWLrugJWMYh6YIEh5yIKrDCwQVJ108m8sIrGMP80jgOLRdSdU3hxLck9hF3i1bbOo7ZKw3AT6jM9boveasxyb6Pbu3DiITv4GXzK_QXs-vUKFikkf6Xtq08aY1Jyceg1G6WH54XKm4dhPhoqW0OokbJhOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند.
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً ایمن، مطمئن و بکر است. مناطق دیگری برای سفر نیز وجود دارد!!!
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14963" target="_blank">📅 16:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مکرون:  پرداختن به برنامه موشک‌های بالستیک ایران در مذاکرات آینده مهم است.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/14962" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تسنیم: یک منبع آگاه در گفتگو با خبرگزاری تسنیم، درباره وضعیت نیروهای آمریکایی در منطقه طبق تفاهم اسلام ‌آباد گفت: بر اساس ماده 4 تفاهمنامه، 30 روز پس از توافق نهایی، نیروهای رزمی آمریکایی باید از محیط پیرامونی ایران خارج شوند.
همچنین بر اساس بند 9 تفاهمنامه، در طول 60 روز مذاکرات برای توافق نهایی، نیروی جدید آمریکا در منطقه اضافه نمی‌شود و ایران نیز در این بازه اقدام هسته‌ای انجام نمی‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/14961" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مقام ارشد کاخ سفید به آکسیوس:
هیچ دارایی مسدود شده ایران پس از امضای یادداشت تفاهم نامه در روز جمعه میان ایران و آمریکا آزاد نخواهد شد، همچنین هیچ کاهش تحریمی نیز برای ایران اعمال نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14960" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ونس درباره توافق: جزئیات زیادی هنوز برای حل شدن باقی مانده است!
انتظار می‌رود طیف کاملی از نمایندگان ایران در مراسم امضای روز جمعه حضور داشته باشند
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14959" target="_blank">📅 16:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بقائی: ایران و عمان امنیت تردد در تنگه هرمز را تأمین می‌کنند هزینه‌های خدمات ناوبری و بیمه کشتی‌ها طراحی و دریافت می‌شود
مذاکرات هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز آغاز می‌شود
به اسرائیل اصلاً اعتمادی نیست همون‌طور که به آمریکا هم اعتماد نداریم تجربه هم نشون داده اینها در عمل به تعهداتشان هیچ‌وقت صداقت نداشتند
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/14958" target="_blank">📅 16:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدا و سیما: تنگه هرمز تا اطلاع ثانوی بسته است و بیش از ۹۶ ساعت است نیروی دریایی سپاه اجازه عبور هیچ شناوری را نداده است
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14957" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14956" target="_blank">📅 14:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253e5fb18.mp4?token=gOswsR3u3nhwpGF5FeryS1eowd7a7-H46e_8vXcN-VCXWEMyVE_POFJvPDMb4pVrXvKcTpe2DYkuMaSezc5oLT-s9M6QXAT0Vwr_zQFjgDl_4i_VaJ-Y1o71ig4dj4zXRvXn-EMlUt18MP6iDKYYWNhbTU4eIpR7-50CQwc3zK1eT4Rtckg1e7vf4o8rGwmrgyrLcHnaXNF2eKhhPAxbSP7gO00Ib51X_yw1af7DzVFB6YEjYSNrdSk50X2ihu0dUBYBFUzD7JAltuzes1N9mG3GA0yph9FjDMXv6iLLnq1ojYwpO0kCKhxmAk4OUCNL00jO0Pjhk85WmvfHVLJU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253e5fb18.mp4?token=gOswsR3u3nhwpGF5FeryS1eowd7a7-H46e_8vXcN-VCXWEMyVE_POFJvPDMb4pVrXvKcTpe2DYkuMaSezc5oLT-s9M6QXAT0Vwr_zQFjgDl_4i_VaJ-Y1o71ig4dj4zXRvXn-EMlUt18MP6iDKYYWNhbTU4eIpR7-50CQwc3zK1eT4Rtckg1e7vf4o8rGwmrgyrLcHnaXNF2eKhhPAxbSP7gO00Ib51X_yw1af7DzVFB6YEjYSNrdSk50X2ihu0dUBYBFUzD7JAltuzes1N9mG3GA0yph9FjDMXv6iLLnq1ojYwpO0kCKhxmAk4OUCNL00jO0Pjhk85WmvfHVLJU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت تو اجلاس گروه ۷ به فرانسه پرواز کرد
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14955" target="_blank">📅 14:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">والانیوز عبری: تاکنون هیچ درخواستی از جانب امریکا برای خروج اسرائیل از لبنان وجود ندارد!
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14954" target="_blank">📅 13:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرگزاری واس: شاهزاده فیصل بن فرحان، شاهزاده سعودی در گفت‌وگو با عراقچی اعلام کرد سعودی از توافق برای پایان دادن به عملیات نظامی استقبال می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14953" target="_blank">📅 13:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f0a7cffc.mp4?token=rkaoj6POP7QUC9F-Aopjxooe4Pz6TkaK2NDLk14ImGbftwuHEB-83lw4_jklrtagkoC6sqx6ogce9cKc26NXVfl1BK-GrW60tboMVvISCtsdaltHsfptelz08OdsjhlxHq3XGfjqJeSwSbcMoEU6mdZyEDnHc_XPvnregDtDmUnRnoXDrjocnaN-28iRL39Ckf5svq739TBknDwFtJcDbVWISMiCQSOfTkcOphXdW3HzAmrE4Vo7dLvucKLvik5FKy3_9Y_ZpwE-1dChBHO_tQeBdBujk6h3iZz0ixGKHsOGUOkD-_7dpY27vH4A1ex-QWx8tus1RMJ-Gxi81q2XOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f0a7cffc.mp4?token=rkaoj6POP7QUC9F-Aopjxooe4Pz6TkaK2NDLk14ImGbftwuHEB-83lw4_jklrtagkoC6sqx6ogce9cKc26NXVfl1BK-GrW60tboMVvISCtsdaltHsfptelz08OdsjhlxHq3XGfjqJeSwSbcMoEU6mdZyEDnHc_XPvnregDtDmUnRnoXDrjocnaN-28iRL39Ckf5svq739TBknDwFtJcDbVWISMiCQSOfTkcOphXdW3HzAmrE4Vo7dLvucKLvik5FKy3_9Y_ZpwE-1dChBHO_tQeBdBujk6h3iZz0ixGKHsOGUOkD-_7dpY27vH4A1ex-QWx8tus1RMJ-Gxi81q2XOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون امام علی نزدیک خیابون دماوند
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14952" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تتر ۱۶۳.۵۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14951" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۲ اسرائیل: حدود ۱۰ ساعت از اعلام توافق بین واشنگتن و تهران می‌گذرد اما نتانیاهو هنوز در سکوت به سر می برد
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14950" target="_blank">📅 11:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نشست سران گروه هفت (G7) امروز در شهر اویان-له-بن فرانسه برگزار می‌شود؛ جایی که رهبران کشورهای صنعتی جهان درباره‌ی مجموعه‌ای از بحران‌های جهانی گفت‌وگو خواهند کرد.
گروه G7 یک گروه متشکل از هفت اقتصاد بزرگ جهان شامل آمریکا، بریتانیا، کانادا، فرانسه، آلمان، ایتالیا و ژاپن است که از دهه‌ی ۱۹۷۰ و پس از بحران نفتی اوپک شکل گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14949" target="_blank">📅 11:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایران فعلا در تنگه هرمز پولی دریافت نخواهد کرد
ایسنا: براساس جزئیات تفاهم‌نامه، ایران تنگه هرمز را مدیریت خواهد کرد و عوارض را «در تاریخ بعدی» دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14948" target="_blank">📅 11:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">️ترامپ به نیویورک تایمز:
«کنار آمدن با نتانیاهو فوق‌العاده دشوار است و او باید از ما بسیار سپاسگزار باشد، زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل وجود نداشت.»
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14947" target="_blank">📅 11:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر دفاع اسرائیل: همراه با نتانیاهو سیاستی روشن را دنبال میکنم که بر اساس آن، ارتش در مناطق امنیتی در لبنان، سوریه و غزه باقی خواهد ماند
با وجود تمام فشارهای فعلی و آینده، خروج ارتش اسرائیل از لبنان را نمیپذیریم
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14946" target="_blank">📅 10:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=dLgfNEXYdvnJO7TjzlLoorsNK79UcW3IATv0EOvquU4kjssIKu-FFPNwTmEaVTZ6blkAMlhl63Xv7y-GjzURzBDWR00ur9fTfz3wsxz_IfiGJJ-ItoRnLCUeqOxBFh5v4F4-NuF81fbO1pQ9CjIxp1cympeC0uuJkZyQrTKAciHX_e4Kg-jj4jtws2o1evCu6qs7_Ymqbq72uG8DC1TcoBfa8Ql5-7a32T4Zrs6f8EeYXJAbWqFIIzMK74vfrntmcdjt8sBs96NUrYTe0UoATnpdpdbjXy0lCeonI-RllnfYPYBMMyyhKL9AhRDJTX1XGY_IiaEBxyyubQU7uvGwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=dLgfNEXYdvnJO7TjzlLoorsNK79UcW3IATv0EOvquU4kjssIKu-FFPNwTmEaVTZ6blkAMlhl63Xv7y-GjzURzBDWR00ur9fTfz3wsxz_IfiGJJ-ItoRnLCUeqOxBFh5v4F4-NuF81fbO1pQ9CjIxp1cympeC0uuJkZyQrTKAciHX_e4Kg-jj4jtws2o1evCu6qs7_Ymqbq72uG8DC1TcoBfa8Ql5-7a32T4Zrs6f8EeYXJAbWqFIIzMK74vfrntmcdjt8sBs96NUrYTe0UoATnpdpdbjXy0lCeonI-RllnfYPYBMMyyhKL9AhRDJTX1XGY_IiaEBxyyubQU7uvGwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین شناوری که پس از اعلام توافق صلح میان ایالات متحده و جمهوری اسلامی ایران از تنگه هرمز عبور کرد، نفتکش گاز طبیعی مایع (LNG) با پرچم مالت به نام “دیشا” (Disha) است که از طرح تفکیک ترافیک دریایی ایران استفاده کرد
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14945" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حمله اسرائیل به الخیام جنوب لبنان!
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14944" target="_blank">📅 10:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۳ اسرائیل به‌نقل از یه مقام ارشد:
توافقی که داره صورت میگیره فاجعه‌بارترین توافق تاریخه. از نخست وزیر گرفته تا رئیس ستاد ارتش کل غیر از این فکر نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14943" target="_blank">📅 10:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XurzgpPMjrpQ41TSqn44XYSSP0ZaCgCMlm5tlgkWpXPzeme5e12Y1GOounmBh7cnOsSBE-DpVta4oo4myeCUDsyNOKj62ITE8kCY8IDNJeua1J9ReOFNLc6kV7DgIt0DUySZDWJKum3NW5m3E_YvkQKv-PWd45TC-jdWAqrhubgm70Hm1_FRMjU93og9On9La--7dIEj7ex1TxEJVVHOQfyLuoEYiaYBRLHL513vkxvJHSTJji2ui0zUnMt7M3A-4rcYaLqQNZtoNIOzFBh4cTbUVl_gtlCRiUPbij5pQZyR94VX9uK3vV3HmA14DCGBn4vZQdPFiPXmO1Nrn11Kjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق خوب، توافقی است که هیچ یک از طرفین راضی نباشند
-کتاب قدرت مذاکره جلد سوم صفحه ۲۳۶
یه توافقی بستم که هم ایران ناراضیه هم ملت ناراضی هستن هم براندازا ناراضی هستن هم آمریکا ناراضیه هم اسراییل ناراضیه
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/14942" target="_blank">📅 03:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک تایمز: تهران نهایی کردن توافق را تا بعد از نیمه‌شب به وقت محلی به تعویق انداخت تا از همزمانی این لحظه تاریخی با تولد رئیس‌جمهور ترامپ در روز یکشنبه جلوگیری کند
اختلاف زمانی هفت و نیم ساعته به هر دو کشور ایران و آمریکا اجازه داد تا جدول زمانی مورد نظر خود را حفظ کنند، به طوری که ترامپ گفت توافق در روز یکشنبه نهایی شده در حالی که مقامات ایرانی تأکید داشتند که این توافق در روز بعد به پایان رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14941" target="_blank">📅 03:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به نیویورک تایمز: نتانیاهو فرد بسیار نمک نشناسی است. او باید به شدت از ما بابت انجام این کار سپاسگزار باشد.
زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14940" target="_blank">📅 03:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پرزیدنت ترامپ به نیویورک تایمز گفت که در صورت شکست مذاکرات برای دستیابی به توافق هسته ای نهایی، حملات نظامی خود را علیه ایران از سر خواهد گرفت.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14939" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14938" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">@withyashar
khatme kalam</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14937" target="_blank">📅 02:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14936" target="_blank">📅 02:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیویورک تایمز
:  محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14935" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14934" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14933">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14933" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14932" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14931" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">@yasharrapfa
👻</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14930" target="_blank">📅 02:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14929">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قشم شنیده شدن صدای انفجار از سمت دریا
🚨
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14929" target="_blank">📅 02:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14928">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش های از صدای انفجار از فرودگاه مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14928" target="_blank">📅 02:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14927">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جزئیاتی از یادداشت تفاهم ایران و آمریکا
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14927" target="_blank">📅 02:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14926" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شعار مرگ بر آمریکا دیگه کنگله
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14925" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpPFDLq0_XfWBMSOcYY9eOh3fm16gaQ-86dabPxCUpGJAnDAINElwaMg3eRBmne4rvibSFFbFeRFS7Rk4x7Z6TSxjTt3XMGZcXNYT4z1xhs_DWbjsPRYmCK2pZlq1Yk87uN0q57hzC_BqjtSlyBwrldluJy2hnGpQaJsUgqNWVpkKqIWaWLu2t4nzVe4zdv3GkmZ2c8Ai0K0l67Jm-xaXSKDQJd8fEpvFRmiOdGzW9JdNGEsDE4sGDENrwIn_fTwxDPHk2l8p29dfLJRt68Phb7FjrTzOjpV4IzYsLzhyqiV3Jl3g_FiJEG3MXCrQBesmFVuq2-5v5WpSaZGrOozyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14924" target="_blank">📅 01:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش از سیریک پهپاد شلیک شد به سمت کشتی ها !
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14923" target="_blank">📅 01:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">@withyashar
⚽️</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14922" target="_blank">📅 01:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14921" target="_blank">📅 01:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جنگ تمام نمیشود بشینید و ببینید
✌🏾</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14920" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ اعلام کرد: من برای شرکت در امضای توافق با ایران به ژنو خواهم رفت
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14919" target="_blank">📅 01:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14918" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14917" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14916" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فارس: دقایقی دیگر بیانیه رسمی دبیرخانه شورای عالی انقلاب ملی درباره توافق آتش بس منتشر خواهد شد
بر اساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که از سوی دونالد ترامپ، رئیسجمهور آمریکا ارائه شد، از جمله حفظ تمامیت ارضی لبنان و عقب نشینی اسرائیل از مرز لبنان و بازگشایی بلادرنگ محاصره،  متقاعد گردید که از انجام حمله خود صرفنظر کند.
همچنین مقرر شد نظام حقوقی تردد در آب‌های خلیج فارس با همکاری ایران و عمان  تنظیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14915" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14914" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14913" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610e7fc5e5.mp4?token=EOK_z5iwCuQSfMrcX1b_y9qcBD4Gi5JTOPGJ6xaDkEB9_DW4irRkVSy21_r4vnnIcAMJY_89hZhdMA55TUZB6JfaSZ7pJZm-TezLyQvxvAEuvk8vcgyojuaWCGej0SkqKqzqwb4DBomDrHPgrKRf-Lkvp69k-40vzz-Wk7bAreXDUPgI7-Y1GSEA5gQ7_EEL9HMvC6098gNNQ_A18pvPHnmiSq3xdpCtpx-OTBQNV3NZ61ikXDG-nWEp-jVofdfAbVoNUvZIapE9Cf63beR4XketVo-bDtJsXslqhBuZqFlSKU-efA84fOtpxTb5Bi7NqnK9wyK1w944i7xTnZ8uRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610e7fc5e5.mp4?token=EOK_z5iwCuQSfMrcX1b_y9qcBD4Gi5JTOPGJ6xaDkEB9_DW4irRkVSy21_r4vnnIcAMJY_89hZhdMA55TUZB6JfaSZ7pJZm-TezLyQvxvAEuvk8vcgyojuaWCGej0SkqKqzqwb4DBomDrHPgrKRf-Lkvp69k-40vzz-Wk7bAreXDUPgI7-Y1GSEA5gQ7_EEL9HMvC6098gNNQ_A18pvPHnmiSq3xdpCtpx-OTBQNV3NZ61ikXDG-nWEp-jVofdfAbVoNUvZIapE9Cf63beR4XketVo-bDtJsXslqhBuZqFlSKU-efA84fOtpxTb5Bi7NqnK9wyK1w944i7xTnZ8uRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صدا و سیما:
پیروزی رو به ملت تبریک میگم
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14912" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCxtmVkc6kUfd_bjfmJKgTFUbyM4QwLNB0zWdwOrbHiL_2gDpxIuP7TXbumYdUC_ogd9NZcUOu_oU8IcO_JMzTcnrwy9Gi1tuXSx-zAk6BsuwJ1sIZ9QzE06FaQIAxBUgOlt8ynaGzWEfNEAOlkYAoN_H-7pcI9YiIWAgSwi8SQRESCL3paLP6JIj3_tC_cjK8qsw_1OLBhtqf9fefZu387n3-Sp2_ggzZJBSte8J0gYJBi2LX_gVURaolZWqHDnbwC9B_-UnCeHnaijLpOlIM2A4bmjbnDWhamW2cCBojvienLC3WjfzSqJsp-KuoNQxLeRbkASsbEw6L6AfMaF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداسیما : ترامپو  وادار کردیم در همه جبهه ها جنگ رو متوقف کنه
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14911" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتریوم داره پرواز میکنه
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14910" target="_blank">📅 01:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za__fXjKx_fvpycgn_aNJtdx9zhOUIumMxQEXsFWjeinxPVGyLpGFzeuYhQl6-Cewv2a5IgXpDvi2oOSBd4409r1mj5eE50eqR79LiJVHFnI1XUOkrswXjd60wko0pdyaV9e0HrlRz0_N-_uheOagD5B6YUOGzWHIJQkqgyu-Kf4_Q5qQYGUb413uPrNCnGC522dURUlJM8E534thnayEMeMkw7McX58n4fwuBfHmGwbA9rGO01_dXVpPZY3HDqv8Hy7qUybD4df5IvI5cRNcmXtCIWqCipV27eiI2_tau3og2whTKXHK079TnszBTkAPrXLnxmQihgCFaGlEyTilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «توافق با جمهوری اسلامی ایران اکنون نهایی شده است. به همه تبریک می‌گویم! من بدین‌وسیله به‌طور کامل مجوز بازگشایی رایگان تنگه هرمز را صادر می‌کنم و هم‌زمان، دستور رفع فوری محاصره دریایی ایالات متحده را نیز صادر می‌نمایم. ای کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جاری شود!
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14909" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14908" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14907" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چیزی‌ امظا نشده
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14906" target="_blank">📅 00:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1enrLMs4asJWhmDTY89rNvS1HBAKtidYhuQOxVkWGQ8sDXINd31eaPsxEJXVwwoKrbsG-ZBW_szo5qHiQT7VNxWpwF5hXwEE1csscNW26Q4iYZZVwl-RJZXK9DdNDjz_p-m8ZtikeXjqnAIz1ETTFMYMhY0qUQ2EtoQ51rp9TttZg2OskrnbJt5A3aLrBnTYix1_QSYe94V8Z_ZydL-1liAjiuQClXCkEnxbm5Pc4nfX2EKJLQ-1hwABOlVc3oCaLr4O57AFvBNdxn5UrG5_seAU346b1W7SZjfHObVpY6oRyTzOcmzJ82wbkoU9elbrH1mSTGKNLV0SA-j0B_5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر :توافق با امریکا انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14905" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نخست وزیر پاکستان: پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف توقف فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق‌نامه روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14904" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
