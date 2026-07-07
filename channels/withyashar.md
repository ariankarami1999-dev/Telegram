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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
@withyashar</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/withyashar/16646" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: ترکیه به خاطر من درگیر جنگ با ایران نشد و نمی‌خواهد شاهد دستیابی ایران به سلاح هسته‌ای باشد
@withyashar</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/withyashar/16645" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بدل موشتبی خامنه ای خودش دهن باز‌ کرد !
این ویدیو رو پرت کنین تو صورت عرزشی ها !
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/16644" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ به ناتو : کاری که تو ایران انجام دادیم، اصلاً به کمک هیچ‌کس احتیاج نداشت
حتی خودم هم کمکی نمی‌خواستم. البته قبل از اینکه برم، گفتن کنارمون هستن
ما هم تریلیون‌ها دلار خرج ناتو کردیم؛ برای چی
@withyashar</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/16643" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور، آیا قصد دارید جنگنده‌های اف-۳۵ را به ترکیه بفروشید و محدودیت‌های قانونی آن چه می‌شود؟
ترامپ: ما قرار است تصمیمی بگیریم. فکر می‌کنم خیلی‌ها - می‌توانم بگویم، خیلی از افرادی که همین جا نشسته‌اند - بگویند چرا این کار را نکنیم؟
ما رابطه بهتری با ترکیه داریم و ترکیه از بسیاری جهات بسیار وفادارتر از سایر کشورهایی بوده است که فکر می‌کنیم وفادار خواهند بود.
و مطمئناً چیزی است که ما در نظر خواهیم گرفت - بله
@withyashar</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/16642" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قطر: ایران مسئول حمله به نفتکش ماست
ما ایران را مسئول قانونی این تجاوز و خسارات احتمالی ناشی از آن می‌دانیم.
هدف قرار دادن نفت‌کش قطری هنگام عبور از تنگه هرمز، تجاوزی مردود به امنیت کشتیرانی است.
ما از ایران می‌خواهیم اقدامات‌هایی را که به امنیت منطقه آسیب می‌زند یا کشتیرانی را تهدید می‌کند، فوراً متوقف کند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/withyashar/16641" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز: نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
@withyashar</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/16640" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOf3-V2lCIBsOCBUZH-jHIZ5wa-CR_gWAHcXKxiE1utrbTsl1TiBw7hqaAEIMH35WK-Qiy78K9nAq_oosX9GLZpbttZkQ6n6MdX4SLXpOBbZvnKoPK01Zv7Nt-IIbgMV_ay5mhXsrUHa3GXg5aKwJmSVRcJX0NJSeX8EVwoxS-RaD83x2rqFNVTq7Wxf5peY-_Ch72rcw_UReYkYpWic0YTpWPPS4LeohgIXbbHmBmbD2OZFJIJt__CP_eRnJOnHX06jyLmJzNALOt8J7lf1xZYVhTO5npXz8YSikLHmXG1sQNvq9gtnuIyvFUnmGEffZULAAYxiSrD63BFoOO9ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : کارخانه تویوتا از مکزیک به ایالات متحده (تگزاس!) منتقل می‌شود. یک معامله بسیار بزرگ. تعرفه‌ها در حال اجرا هستند!
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/16639" target="_blank">📅 16:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارتش اسرائیل و شاباک : ارتش دیروز در شمال نوار غزه به دو پایگاه تروریستی حمله کرد ابتدا، احمد یحیی ابراهیم بتش، فرمانده یک گروه نفوذی در سازمان تروریستی حماس و در یک عملیات دیگر  جنوب نوار غزه، حمواده ابودقه، فرمانده یک واحد اطلاعاتی نظامی در این سازمان را به هلاکت رساند.
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/16638" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/withyashar/16637" target="_blank">📅 16:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب سنگ به سوی وزیر امورخارجه ، عراقچی که با چند متر اختلاف به ماشین کنار وی میخوره
@withyashar</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/16636" target="_blank">📅 15:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال اردوغان از ترامپ در فرودگاه آنکارا، همینطور حضور سربازان ناتو با یونیفرم جنگ جهانی دوم.
@withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/16635" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">علیرضا فغانی کاندید قضاوت فینال جام جهانی 2026 شد.
@withyashar
🏆
😍
💥</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/16634" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان در فرودگاه از ترامپ استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/16633" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.  اما امروز، خوشبختانه، با همه امکانات موجود،…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/16632" target="_blank">📅 14:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.
اما امروز، خوشبختانه، با همه امکانات موجود، از تمام رؤسای کشورها به بهترین و امن‌ترین شکل ممکن پذیرایی می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/16631" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/16630" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ همکنون در آنکارا به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/16629" target="_blank">📅 14:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/16628" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ7ifgJwnfVggHDzuGrwCtfTBIRHRseHYALbntKxnGDxdjfpti0YqA6ZH6gMzteZjls7haUnJ___PKyglNM3Z9kug88f1bWP21LA8O6CXifaeTA7nxK1u5bF3En6sjrETOBuGXNaQydouTaz-zxQHVJAPlybol6HJKcFAYmaEf9E67Gnsbt4Jyo8oj_dhZRTq6OjxpuZbVKq4CahdE4zlX2y58fIIyTVmKwMMMK6T6ZwWor-TJyM_e5oCZNjjk0V7lDbuvmlTTQw0YfIgXVzrsYWxyhyd6d7OnRChLl_9zoEPGskgpRqjWDziU3S3X_LHULPRFfIyleyD_oEVXAkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با هواپیمای ایرفورس وان جدید هم اکنون در حال ورود به آسمان استانبول است و حدود چهل دقیقه دیگر در فرودگاه آنکارا به زمین مینشیند.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/16627" target="_blank">📅 13:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">منابع امنیت دریایی: یک نفتکش نفت خام با پرچم عربستان سعودی در نزدیکی تنگه هرمز در نزدیکی عمان آسیب دید، پس از آنکه یک نفتکش LNG در همان منطقه مورد اصابت قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/16626" target="_blank">📅 13:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfVLnW7NAwiGyT79VHbsUTxo_iUfVUG-T19k13EW6Iz4U0eBY2aIM9n-cKOCf6cMESGRY3f7aKE_F-BQAzi7jUfzmEjwhRyQUCNNB_vr0XqezeRLefX9LXAB8i3JtwzmkKe49xL30B-NVA31p04QRPbkXd_MEs3q6qmNuZq6ROQlD1upzDkM8SzohFHxRDegENXQ4SVjLQ4R4kNiOeHsqLt38qbySIbiyQeQKrLICGvMWobUsC56pP-SqPJzBUzYN6k5S-532Fv-La5yYkdd2n_p7E0YoocEFz55aDHkJ62Z9wP6CQXq5M_RBE5izYrm0m3BBkX6pRaR6wOveOZqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا هر وقت این کامیون عجیب و ماجرای تابوتهای یخچالدار را میبینیم ، یاد فیلم «سرباز جهانی» محصول سال ۱۹۹۲ می افتم که داستان دو سرباز آمریکایی را روایت می‌کند که در جنگ ویتنام کشته می‌شوند، اما اجسادشان در قالب یک پروژه فوق‌محرمانه ارتش بازسازی شده و به سربازانی با توانایی‌های فرا انسانی تبدیل می‌شوند. این نیروها با یک کامیون بسیار پیشرفته و مجهز جابه‌جا می‌شوند که درون آن محفظه‌های سرمایشی یخی ویژه قرار دارد و سربازان هنگام نداشتن مأموریت در آن‌ها به حالت ریکاوری نگهداری می‌شوند چون گرما ضعف این پروژه بود.
امیدوارم موشتبی خامنه ای‌ رو هیچوقت نبینیم و زنده نشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/16625" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات بالاخره تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/16623" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم مثل تهران دیدن جمعیت کمه
در مسیر فیلم خورش خوب نیست کامیون ضریحی جنازه ها رو از وسط راه اصلی خارج کردن و از یه مسیر فرعی بردن
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/16622" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/16621" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=fE2AN4K-764v2P0ZZBIIzNREcD4-eUk_az_0cr-NGFSU2uaDGDfYTLNUobrBjjcUbkokBGW8Zrz0AX34m97rQ6ahBR2YB8mtR7DcPqCgf6l4s2NOrNBtO9lgME-Ftpw5QfmD6J88qNrvhN75oMAz88aN0L7TA-Fdids4bo_7pXdSM79mrcgB6EHaWEhIN87dl1LcVAGkoEdMOf7eYoFig61KtVltPmpL3hRt5nV1T5I6CbcB0m3OAVTZREFqIpYMwmeRG4TZN7wH2pE-nkE2rKDJi838I7zMe4w5BYnBGX1Po4Pt8JftjzqQbmwRtE8kRb7yNmLSDpTJJSUuyh_vbgx2WoVrNQrPVJCNNQjt0CemiOsqWEWwZWAjRTyKkiZO63MXkGI88--iAbKNm9UED3xO-7ys6x3QD-adxU2H4apaOu_xPRkpJZQ-pbvuENXv6G4rp8xjwDeqyHHSUs1XsXXRA5lo_cxycAwZLY1qbVxqXqHQlkoGtUJBjJakB_UnmU32zEJWU2yk-yMzdQgeh9AXYKH0DDiMxawrIsGZTHa7VYZB_DH5qY8_-pyxT1TM1W9flUz6sZMfcGYko21s9DT833fKlobeNq3CbCLU5yeQujCnSO2L3HSBUG6wqrZvXJVW_96zCIz0aIDp_sQ53f59ws0xAO-vEu0629QFBvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=fE2AN4K-764v2P0ZZBIIzNREcD4-eUk_az_0cr-NGFSU2uaDGDfYTLNUobrBjjcUbkokBGW8Zrz0AX34m97rQ6ahBR2YB8mtR7DcPqCgf6l4s2NOrNBtO9lgME-Ftpw5QfmD6J88qNrvhN75oMAz88aN0L7TA-Fdids4bo_7pXdSM79mrcgB6EHaWEhIN87dl1LcVAGkoEdMOf7eYoFig61KtVltPmpL3hRt5nV1T5I6CbcB0m3OAVTZREFqIpYMwmeRG4TZN7wH2pE-nkE2rKDJi838I7zMe4w5BYnBGX1Po4Pt8JftjzqQbmwRtE8kRb7yNmLSDpTJJSUuyh_vbgx2WoVrNQrPVJCNNQjt0CemiOsqWEWwZWAjRTyKkiZO63MXkGI88--iAbKNm9UED3xO-7ys6x3QD-adxU2H4apaOu_xPRkpJZQ-pbvuENXv6G4rp8xjwDeqyHHSUs1XsXXRA5lo_cxycAwZLY1qbVxqXqHQlkoGtUJBjJakB_UnmU32zEJWU2yk-yMzdQgeh9AXYKH0DDiMxawrIsGZTHa7VYZB_DH5qY8_-pyxT1TM1W9flUz6sZMfcGYko21s9DT833fKlobeNq3CbCLU5yeQujCnSO2L3HSBUG6wqrZvXJVW_96zCIz0aIDp_sQ53f59ws0xAO-vEu0629QFBvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه ۱۴ اسرائیل، درباره مجتبی خامنه‌ای : اون هنوز زنده‌ست
- از مخفیگاهش بیرون نمیاد و می‌ترسه، اما تو دورِ بعدی درگیری‌، یه بمب اسرائیلی به سراغش میاد
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/16620" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید @withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/16619" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است.
‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود چهره سرشناس مخالف حکومت ایران به قاهره داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16618" target="_blank">📅 11:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/16617" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شبکه الخدث عربستان سعودی گزارش می‌دهد که رئیس‌جمهور ماکرون، ربع ساعت قبل از وقوع انفجار، هتلی را که در دمشق اقامت داشت، ترک کرده است.
در سوریه‌ نیز گزارش شده است که رئیس‌جمهور احمد الشرع، دقایقی پیش از رئیس‌جمهور ماکرون در کاخ ریاست‌جمهوری در دمشق استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/16616" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای رویترز از تهران در بهترین ارزیابی حدود چند صد هزار نفر را نشان میدهد
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/16615" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار در دمشق، در نزدیکی هتلی که رئیس‌جمهور فرانسه، ماکرون، در آن اقامت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/16614" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک منبع امنیتی ارشد لبنانی امروز به روزنامه "ال-جوماهوریه" لبنان گفت:
"ما در صحنه، هیچ اقدامی از سوی اسرائیل ندیدیم که نشان‌دهنده عقب‌نشینی از مناطق مشخص شده در توافق‌نامه باشد. برعکس، شاهد تشدید عمدی تنش‌ها هستیم."
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/16613" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز به نقل از یک منبع امنیتی: انفجاری با استفاده از تعدادی مواد منفجره در نزدیکی هتلی که ماکرون در آن اقامت دارد، در دمشق رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16612" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/16611" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره ای از ۶ ژوئیه دیروز ، چند هزار نفر را نشان می‌دهد که در نزدیکی برج آزادی در تهران، ایران، برای مراسم تشییع، جمع شده‌اند که کاملا برخلاف ادعا های میلیونی رژیم است
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/16610" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN3m7ICGIsYpIddRTA2xNyw-bbHsM1twKEyGpQNh5bBuXCe4djNA-p317rxqoGnWTm2iXSy9P_PzUbaiQGGyupzO8nyK6_zUJLWCpnOv33GjvxohuZSTvXCKaM4dfL-VpN5sk1NsxOgDbhkT4v7ZPO-tMsVHxl469MqzUCr1USK4zFpBON8gie-tpfFJ4W5AaQDj7V0TsByB-YkL8G5biQ75BlnkNJhNnB1niI3mE4WP8CKgnSdAQ5acPJXnD9pCcnMDJl9-X4XL1OkKQX2aKu8b47GUQrcEibMWUnpXGpo-7-9FSwZgL3rdjhbjgzAM5AxkILkECMmyGtcUZV6KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدل ایست نیوز : تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/16609" target="_blank">📅 10:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB7GtZtQ7gV2uuFzx8a-JytthMDbpAGtclfZtfJWGIy3tTi5fgWCw20SFYmebTBADpKX_XMun_OxHolXDqLZbnsgOX8FNdrIjLh4sfxJRogIxIPumfdSdZkx2ArHo-AN5l4ofYWzkulfMU6AsBy8QKtUXcKY55w7wdnTE9lDVo87M1CW7gXk3p_83LCBGMZEmgGwnslIHSXn0lTbXbE5mEmxTXWWbSUUkOXTZBFYS4jgNJE_utRAB7ZC0z47Qdl8OlvGaDqAdal5EehyiJFizwvQAhxYaQSSxsvIj7OKJ_a7Gq-xeHhgoc_-Jp4wkd7EkpUm_Y_2L6UL5KLlI5p8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/16608" target="_blank">📅 10:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی به ترامپ: به امضای خود پایبند باشید
تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/16607" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به وب‌سایت والا گفت:
حماس هیچ قصدی برای خلع سلاح شدن، تسلیم کردن سلاح‌های خود، یا تخریب تونل‌ها ندارد.
استعفای دولت حماس یک اقدام نمادین است که با هدف نشان دادن تغییر به واشنگتن و شورای صلح انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16606" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/16605" target="_blank">📅 09:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTWHSiItylAfhanwHch8it4yaJZ7xRwr1IQKt9jhu4Qwury5nNTQI8vtxn5mTvklhN8fwSe_65zFXNys0eQagcyLlidvovB9DNcsDMvateWaaaZkHta0g2oYTNnIA8Bu4ONw00SwmT4_kuU5h_yWVMkrVfu6kXiJcy2-EI5WMLe9lJqYTc7qGKgtA5pb8IW8w1lz3dHnYu4hg6Vd3u6ALGnnfXgdBqssQhiSNmFN_83A0SKhu6lo9kMcabzG5Z-gfEQ0rdSwac1oF1cirUsW0iOYuoGkzlyOjU71fDgOASD9zDWnKZMhv4cnL34rv-ulMM0pv0DR2d2VzF_awmHc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/16604" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=BguXC3BvyVmGH50YCg2xkEoJvHOrX7ocJLHaO2JXxOdWOVIxXYbqI-sQW_PFSVH87axDWRIYPv5EIfdaAJTxKGLRwASmT9be_l5r4iV5n09ceBR5gru_ZY0jJSMv9E5e-OYS1b1zcP5gcBpAKYdko02evZLt_3g9kJixSWw6wIJrwp0ZgwrTuMeAQt-Yix84b1Te3xzR64Mwj3YPQaSztuNN1dp76xRD47B0K4CmS8whPH7tTMU6x6fZU7HwCNnw9oENxRcq_uzV1l-lAZ3urUJ28LNJfjTOiKhTTTXeMrws8DDBe-e9KMsOYaUcrFCyCkmkGxgsbJh-vofLqXtkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=BguXC3BvyVmGH50YCg2xkEoJvHOrX7ocJLHaO2JXxOdWOVIxXYbqI-sQW_PFSVH87axDWRIYPv5EIfdaAJTxKGLRwASmT9be_l5r4iV5n09ceBR5gru_ZY0jJSMv9E5e-OYS1b1zcP5gcBpAKYdko02evZLt_3g9kJixSWw6wIJrwp0ZgwrTuMeAQt-Yix84b1Te3xzR64Mwj3YPQaSztuNN1dp76xRD47B0K4CmS8whPH7tTMU6x6fZU7HwCNnw9oENxRcq_uzV1l-lAZ3urUJ28LNJfjTOiKhTTTXeMrws8DDBe-e9KMsOYaUcrFCyCkmkGxgsbJh-vofLqXtkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوایی که ما تنفس میکنیم سیاسی هستش !
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16603" target="_blank">📅 02:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=anLyq1cqxsBOOwSTmQ5LFVqInnim43coJB3AoVZEywDFgJw38XA1cAmrszd94GyICN0lG1nSh9kU2z9Tqj0UBdnYvydnykELsRJmOnQ6YuC6d1dhAOCLGV1L7YKfyyeuRUSXxT9IVfkBQw8wZFZS3D1rZW3VYNPa0ZNEng7yTT6A0DLlJfvQ0I2gU6glGZpDi_ASec9Vre0wXmf5-1YDuzKmnYApAtxnhwSn-FU0WNY_K73tWyKDHuwVZ8MEEHxlO-BH2WcbOE7oNo_O1cvAgu4q-uAWohjbjrgYP3OoCKZ4xzMYaBi2rfcWI8KpCCSrM6kOxELvegGm9rjp0BsBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=anLyq1cqxsBOOwSTmQ5LFVqInnim43coJB3AoVZEywDFgJw38XA1cAmrszd94GyICN0lG1nSh9kU2z9Tqj0UBdnYvydnykELsRJmOnQ6YuC6d1dhAOCLGV1L7YKfyyeuRUSXxT9IVfkBQw8wZFZS3D1rZW3VYNPa0ZNEng7yTT6A0DLlJfvQ0I2gU6glGZpDi_ASec9Vre0wXmf5-1YDuzKmnYApAtxnhwSn-FU0WNY_K73tWyKDHuwVZ8MEEHxlO-BH2WcbOE7oNo_O1cvAgu4q-uAWohjbjrgYP3OoCKZ4xzMYaBi2rfcWI8KpCCSrM6kOxELvegGm9rjp0BsBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع جنازه انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16602" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDNVcoHcnzyCFw4e4eytzPPncgycHWpYwLBXsBZSH8RYh-sFbnATMKK7oOQBYY2XXszdNDdq5nli3RjpbdKhn-REWpiV1lYnVclIh7ADtCLUSfxwK2GLEiYQzm6NWd7vPKJZK_5MulrNBHH9KiU5tJ7GTLcZYN92KZd-sRMFFIo_B-sKw0MtB1SPE4S9QQo47xrVXA3WMN-dw51caOwTsBryxSXuHgXQGD2Rw1-T7SpH13tadfN7JffzivH2l7C893H5VOzYRswM7zTkTzIARBPiqxuLcRExG1ynujdlo21sBVtqKzI8ySOajn0HJgEsUQ6M-mPEqXaVm1RA6kEqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16601" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر امور خارجه آلمان:
ایران باید تمام هزینه عملیات‌های بین‌المللی برای پاک‌سازی تنگه‌هرمز از مین‌های دریایی را پرداخت کند
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16600" target="_blank">📅 01:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTqUTFHlMZcZ8VgF4tlxEJ1tpev4brjtuOJbSOGr2q_0ePo3YdAoEZs6nwqGrLZpDX63mIi24IcfEXEZt96gBKhf1e2SMk1RTWku-c0qUBU7QXvuaKa5HVPknbk5yI3fe5LUbYElHEiJhsaDdS7KgspyD5VT6A-UlDTTi-Zjj38OYV1JHrMWKK9MLiI7n_5M4vnl-YU3OPvhnFeRXu1pxyfZU2ZbM__Iwdx5ckAsq54z9NS5eCjTBLDcESjT3YmK3iQ6IzRcxlx4Xrgw08_ZZCi7q0uCWVMYujG2-5U2jcwAyhdE-fhEMM2usBSm4p3N8PgcgsTf6P4yOfTfz1Eyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg90TsdPobZsHIuT3A7LplsQaHXert721mFvvoep2CeTKwU4sVeauDRX3ZeVykztqZFvtv0TpRnd6gYTkFZqu67JYz-YoVJDKFbarEQsefB1ojOTMKIP4QN58l4SEOpsMNdHAWfeUcQ3jxNPitxqMqUvwouNs4jigHaiSyz6Ah8arn59wEABwoFHB2YZfR0dih8csqQ-GZrZ9gHQL0LqKL9pxDXxDtN1RU9cqZ7t3ZEHw9pzFSVM7MAGrSAAxB3cbuDJFUwJ9UNvQogED1OmgMY5dy_Hgd_7D2wFpWiG363YAKXj4Nb8gyAXuYgmtUVyZWw65S3HltF3bQZzGIyufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=Oe3YqwnygYrlqPrftbG3Lw6lrQ19c_BETExIunA5JXilNtBn768JMar8B-zdZ3SV_5rEL41PNRAScgV6ZoU3r-QK3V4D0F5CZGzc-1dJTUJAGHXQa2EpLLNV1oWKxr4o0qjUejCFuQRbIxF_zqSPu8Mi2xon66zNLb0STd32QGOxdrwSi8Ew7Z3PT8xvtLzYNcKNBNucmSVMqq6n8UTQ227gWzCFae-mcPv68SQ9mF88h6Dwu9K9OSUMbuL9rqkrKexyHwIV3HP7Yu5gJUw4usTwGtTmfasRyFlOl3NTt_ZQF1GKXxTh19zTuA8UWqkKzmrfXL5AKKLJ_TGLPqXX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=Oe3YqwnygYrlqPrftbG3Lw6lrQ19c_BETExIunA5JXilNtBn768JMar8B-zdZ3SV_5rEL41PNRAScgV6ZoU3r-QK3V4D0F5CZGzc-1dJTUJAGHXQa2EpLLNV1oWKxr4o0qjUejCFuQRbIxF_zqSPu8Mi2xon66zNLb0STd32QGOxdrwSi8Ew7Z3PT8xvtLzYNcKNBNucmSVMqq6n8UTQ227gWzCFae-mcPv68SQ9mF88h6Dwu9K9OSUMbuL9rqkrKexyHwIV3HP7Yu5gJUw4usTwGtTmfasRyFlOl3NTt_ZQF1GKXxTh19zTuA8UWqkKzmrfXL5AKKLJ_TGLPqXX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=NfZul6o0Ui6_sXiHYxhpyGqfzyKobzqfwxzy70Vr7AAvzYcPTaYY8-G_XivymR28jeieSUgBps8yOp3et6bRX_Dzp2a4xN1cVYnDEEeG4uEoqi6IqwoiObRi9dOBzbOT3BAeCGiHb7CUeoD4KnSBwoLV1WWc49A-wWVvutOWUve1c1x88toVH7ukfTsfKQE13FTXJjImUQ93Y4KY7GuTNleSFPQ1gGdX7fAzJ362GJjbK4-dgirTyqUlgvJAWUyXKzXbYGX18FodOszBDhMUJEbETsY-AQXXsatC-7Jm9Ax2yIa9Y3WcBgxBDlg3Flpx3rbKnht5twhRZkytQ2_LWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=NfZul6o0Ui6_sXiHYxhpyGqfzyKobzqfwxzy70Vr7AAvzYcPTaYY8-G_XivymR28jeieSUgBps8yOp3et6bRX_Dzp2a4xN1cVYnDEEeG4uEoqi6IqwoiObRi9dOBzbOT3BAeCGiHb7CUeoD4KnSBwoLV1WWc49A-wWVvutOWUve1c1x88toVH7ukfTsfKQE13FTXJjImUQ93Y4KY7GuTNleSFPQ1gGdX7fAzJ362GJjbK4-dgirTyqUlgvJAWUyXKzXbYGX18FodOszBDhMUJEbETsY-AQXXsatC-7Jm9Ax2yIa9Y3WcBgxBDlg3Flpx3rbKnht5twhRZkytQ2_LWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=MScoqghnNhaPl8Ak0UfsFNPQ6P__MwnrhtSnzXu3mqxfHLchtzrmhFgdOg05_vrqIISzQpFulRQ5U7iHDDqeS60mNM9sAGWpteiuUSqzv2D2wdIU7K1iJp-jC-a97rKC-XYwsm2G05gkW__R1RJouK7dhtpxjqijCCzkmhfKdBsGJ3wTh-fORANgCReT37L2VAyjHAdIIWn6jlqEVBnNhYNW8tAjmdB9b7tVOwzn0_e6kDalWTZ1nytIlqXOd5xapH137rd7jkZ9P7ABjmO4eI3-buXK7q0ECsXmX66pf-XLOpr2h5J2llXg7rsWIFM3tZIVXgm6yVqN-SCvOO-X13HhyM2M2OV6vj1WbunbCRFJHYgwQzy0jLs6LJA_pQhuGR-aLqREqwt9nopC0CySb8dj6fD79NeCxE49fRPHPdeUcS-gAQCYyemvquQOWng-VycX4MlsPmJRSsv2iRNBa53NEALJNBczKgWS2eZ3QWSGgwLrsOpwEF1-ZrwpheN9TyDaXQKX14JKnNerZueFGnCS0OWiYPtgD8i9vZibXGbTczL6eBmJdiIBrzqkuo8cjtQ-X0aDf-Dd0DT72wy4c7wxiHfdy2DaI1Mwyi1-Qr276NcTX5-zOIrV28gXcVHFSsfM3Wy_pcHlU9b1HTZXURStsRDIno1ard_KskCI-UU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=MScoqghnNhaPl8Ak0UfsFNPQ6P__MwnrhtSnzXu3mqxfHLchtzrmhFgdOg05_vrqIISzQpFulRQ5U7iHDDqeS60mNM9sAGWpteiuUSqzv2D2wdIU7K1iJp-jC-a97rKC-XYwsm2G05gkW__R1RJouK7dhtpxjqijCCzkmhfKdBsGJ3wTh-fORANgCReT37L2VAyjHAdIIWn6jlqEVBnNhYNW8tAjmdB9b7tVOwzn0_e6kDalWTZ1nytIlqXOd5xapH137rd7jkZ9P7ABjmO4eI3-buXK7q0ECsXmX66pf-XLOpr2h5J2llXg7rsWIFM3tZIVXgm6yVqN-SCvOO-X13HhyM2M2OV6vj1WbunbCRFJHYgwQzy0jLs6LJA_pQhuGR-aLqREqwt9nopC0CySb8dj6fD79NeCxE49fRPHPdeUcS-gAQCYyemvquQOWng-VycX4MlsPmJRSsv2iRNBa53NEALJNBczKgWS2eZ3QWSGgwLrsOpwEF1-ZrwpheN9TyDaXQKX14JKnNerZueFGnCS0OWiYPtgD8i9vZibXGbTczL6eBmJdiIBrzqkuo8cjtQ-X0aDf-Dd0DT72wy4c7wxiHfdy2DaI1Mwyi1-Qr276NcTX5-zOIrV28gXcVHFSsfM3Wy_pcHlU9b1HTZXURStsRDIno1ard_KskCI-UU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBmTb4IoMOo-d5Sa27HmQtsD1kR0CjIwQHHQriE_Nlvi86jZoufOcBVxk66P4sNW6PsA_ez9jTuhkWM0oK-LNPcn2OSbPlB9awCBGlYocqtnI6t0oM8973UFOGhw0xBUlx8yIDYRIrlsKQIa3a4lQnHC1Rclhde3IaB06xMPeEtCrZubIQhvvPpoU86K48O1J8USwL4pmdDUM4PTq5kHVJujZzoDd_IGdLK7rqCXZhWtJsld5_wH4HZzcpWEYikqapY9zyybpnmlV5oHYGwxhwZC59FKZ9npMe16xLYcSmq-3i-rPasFde8vaP0kucnu02qeU02ImbIbGkIPkBU99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=CwTo7ei0S6EegnfuV6yEsYcVLLqkMemQUHd64vzs1E2Wg0zjjHAdcNvRsvSEos9NWknAKsEmZMjaGC_RpWvxKkSgWRjL9TTH-SsQrk4hi0MMuDHEIEN29kHpiDdiijUNNd0G4m2BbO1gGJ1MwGP2L4b5uFRNfd46aZ4LFfGRmKqabEDOEqYTW2qqcxwK6r8sSKaA7JwZb0ncwGNdCa6ZSMIQD1j79sLxvokDYYNg2W7k-hUQX55R83h3jU8Q8Fn-inAK8x-Niqms3pnyc4JnbCI9wrgdanmlVGoB8Hb1u8KuqVYi6rEKLYcnYC23ZOjXRvemUICoWRegGbjVh8sukmmXPivjtZ7S8IhDMGUoQfYyALpsPLEj4--jcQvHoHr8ORCnipGKEFqfM0XjFOr6dWhWfSTsMIedzjUZbS70Td2zHi8DY9z70J7zKBFpUsacaXTMFsW6c0VH0fMvFiLVJI8OG0Ycy_LB_kBiNEpVkIQJsr5BPbOE4WHjH9zxVJWZ-06YFvbl-KeCcbih-XNtZeDCj4PQlCuFFY2s4K7DHGM948UofcSC2F--BVw7v4R2YGKAoluDR_7MrAEE1Ak_jfAcuJVm7IpVpZmH9t7xhr4926UnQMlkHrQv9ECerfHZuWkOZA2rMrL-TEo_oiTHuYpt2yc60P7MnbqVWtO-IEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=CwTo7ei0S6EegnfuV6yEsYcVLLqkMemQUHd64vzs1E2Wg0zjjHAdcNvRsvSEos9NWknAKsEmZMjaGC_RpWvxKkSgWRjL9TTH-SsQrk4hi0MMuDHEIEN29kHpiDdiijUNNd0G4m2BbO1gGJ1MwGP2L4b5uFRNfd46aZ4LFfGRmKqabEDOEqYTW2qqcxwK6r8sSKaA7JwZb0ncwGNdCa6ZSMIQD1j79sLxvokDYYNg2W7k-hUQX55R83h3jU8Q8Fn-inAK8x-Niqms3pnyc4JnbCI9wrgdanmlVGoB8Hb1u8KuqVYi6rEKLYcnYC23ZOjXRvemUICoWRegGbjVh8sukmmXPivjtZ7S8IhDMGUoQfYyALpsPLEj4--jcQvHoHr8ORCnipGKEFqfM0XjFOr6dWhWfSTsMIedzjUZbS70Td2zHi8DY9z70J7zKBFpUsacaXTMFsW6c0VH0fMvFiLVJI8OG0Ycy_LB_kBiNEpVkIQJsr5BPbOE4WHjH9zxVJWZ-06YFvbl-KeCcbih-XNtZeDCj4PQlCuFFY2s4K7DHGM948UofcSC2F--BVw7v4R2YGKAoluDR_7MrAEE1Ak_jfAcuJVm7IpVpZmH9t7xhr4926UnQMlkHrQv9ECerfHZuWkOZA2rMrL-TEo_oiTHuYpt2yc60P7MnbqVWtO-IEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS-qMeXp-d-fVNrfoO7IGPFVLDRyNH4Z97kjyTz9iMvCcgyxagvi6EUXaJWIZ0UsKEygvp879nnpcyUBlke1CpkdvFP0UZomHN95tW6jRmzUuAGg-IXiqOfWFSgADtwwbXYMZ1acFZHL_T0Fk5fBf4OVRv_EuNIiHIdNE3OiVYIwI839DdhHGUVYQ_r5QeOgCCG0-c69DzbdS-Ntz-DakQ6-cTMa1PjSQ45T4Lbr8MY6mie2ZJEA3hoyIFUwMIRvmbnE2SznHQWxGordj31BKW6G4CMrF_SopGcVWa_tk0rt4x8TpVpT9iLkDqpCrJEFRZU1YT-qlgQUpBgSt9FDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=DXAjNObnxGrxYTePl-dVk5b3jRynE4xC-UBL5sFEGJzOf40DOriVytdiVn9w_5L8l7FnhqsfOe6VVb5YPAOF_46VrS7NsD4oFpK0RESGFwvH1gvRcXWkQSLbtj_l7uJbuFLP8QBsED3VQlR4HvMUKSsHRr3U-CHUIqQqJ7GCvwMbELddU5rcy8xAtf_98Fvi7e3Qw94buBqnxrbUsxctykDWuTo3Xh6L3We-qTom9PMKzQLmPVTfpi7KySfNI6As45yT9eddo2yfazM5-bXhA9CQSWgSO3oBpsWtQJi34ZYo_P2XVfHh73h21Jj6UrabElZkpr2B6ZVnDHpeOtrBlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=DXAjNObnxGrxYTePl-dVk5b3jRynE4xC-UBL5sFEGJzOf40DOriVytdiVn9w_5L8l7FnhqsfOe6VVb5YPAOF_46VrS7NsD4oFpK0RESGFwvH1gvRcXWkQSLbtj_l7uJbuFLP8QBsED3VQlR4HvMUKSsHRr3U-CHUIqQqJ7GCvwMbELddU5rcy8xAtf_98Fvi7e3Qw94buBqnxrbUsxctykDWuTo3Xh6L3We-qTom9PMKzQLmPVTfpi7KySfNI6As45yT9eddo2yfazM5-bXhA9CQSWgSO3oBpsWtQJi34ZYo_P2XVfHh73h21Jj6UrabElZkpr2B6ZVnDHpeOtrBlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDztnvRFhB0x6tgBj5ENO0A-cyvwo5HglXX0quuGA-_w0i3pargYay0Z-nTzi3hX12BrQGdJ04f9yxYl2-sGLx6SeAWvgHGUSYKfj7vrBiRBhhK_9m5EpKsXlFUCO71DJ0pKHkRslfMMiIP_P2z5FkdJsJh958Ox7zOHzWTptCqIohVW41zLgciPu9Xsdh6vZCv8SLDMjl8bdEWTHlYMNinUXRH3Tu4p5ISnb1WWYPInaTzo66deucdIMgGmX7b5g2nTKPAalIBSRZgOtiCNWgNvN03O3R4gw3zMzlx6Y3908EnlBPKJCiVa4XUKwJIsxJXWUmzSfLb-g9lqdexawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=D6d687SthvxLQv_CH0cIuGgOiqUT_ThqmJp-hk_PDv95X7R-bxU7h9SdgN_GhR24xv6HpYbP_oTfAKYlrrFZFbon2_UvGajH7oDFK2BlGFZuRrqyHV34n2Du3FSPA6qvHtxgStAh9B8xL9m8c53eTCImfXlDyZWGFCTLuNaEEW7BsGPzC_aBcWenPwhNys-qgmQdp6F1MhaOVUfosoV-OqLu63isrw1j1ME08LKto82qiD4aRW_nQV7YDX4g-DJgvBRRBE9OPnaz5OrJyWuVU5dJ9Ul0GCNq8CrbPuc-rAapxlnAyE8-zuxAaKKCYFfHb-O-EgD2D8HnLko5a7QHBXdRJadG92PMsoDN5bc8HSPbLFivifO7Vp4cH27hgv6CGJQDGEgDlV4yUv56n6z9I5ZdGKPnFTMimbSh2-2UHW0ld0ew_7N-tJmtdiYqb9hXyIofpGpllLAEglI9ToCiPAZjcDP4mByban8j4UFi1MFnjILdH5S0ffKVk7Nu9QVymmPEqJJ-7F8z0IkP1VgD95yqew0_J8rS1uVtNW58RbwDFAg04_yQA_--9pLWFfQ_Bj7_OTmk8nu6EC4YPX_ZISxKoRgmHFUJ6wh9ZUI3PnEs_iV4kL1kM42cbvA15lyzDcpAqHNC-61Zlu0XJDC-gN076-dkFN3EA2A_0FmijAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=D6d687SthvxLQv_CH0cIuGgOiqUT_ThqmJp-hk_PDv95X7R-bxU7h9SdgN_GhR24xv6HpYbP_oTfAKYlrrFZFbon2_UvGajH7oDFK2BlGFZuRrqyHV34n2Du3FSPA6qvHtxgStAh9B8xL9m8c53eTCImfXlDyZWGFCTLuNaEEW7BsGPzC_aBcWenPwhNys-qgmQdp6F1MhaOVUfosoV-OqLu63isrw1j1ME08LKto82qiD4aRW_nQV7YDX4g-DJgvBRRBE9OPnaz5OrJyWuVU5dJ9Ul0GCNq8CrbPuc-rAapxlnAyE8-zuxAaKKCYFfHb-O-EgD2D8HnLko5a7QHBXdRJadG92PMsoDN5bc8HSPbLFivifO7Vp4cH27hgv6CGJQDGEgDlV4yUv56n6z9I5ZdGKPnFTMimbSh2-2UHW0ld0ew_7N-tJmtdiYqb9hXyIofpGpllLAEglI9ToCiPAZjcDP4mByban8j4UFi1MFnjILdH5S0ffKVk7Nu9QVymmPEqJJ-7F8z0IkP1VgD95yqew0_J8rS1uVtNW58RbwDFAg04_yQA_--9pLWFfQ_Bj7_OTmk8nu6EC4YPX_ZISxKoRgmHFUJ6wh9ZUI3PnEs_iV4kL1kM42cbvA15lyzDcpAqHNC-61Zlu0XJDC-gN076-dkFN3EA2A_0FmijAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBmD6vInW0BmtrzWyX_cHrQys_v0K-blFu7vwbDQD8Svb4Q80OIT-qVjbfYONW88aDTV_uyCT6-OXmmwiXYGBcUS2YoNsbf-kEyJbd1yYsxcQpzjIADq8MAM9w3EX1bS41TzHRzSBk_JVVbtE0kjtciXxnwK7UoaGApRWaX-H-KLs_BrBfg5pLtt8e6vHI3Y13nS_3Nq8tIoOPGLlPzIkPEsvo5SdGH5GAyvjbiLX-Btmd6fXWF-wzLApnP7bvtg9bh_FiX2HbKPwy8Kfk7WuxAXZUzPurPfByf8xi_TKQblf3x9v4x0lTVs-staaqJDxBBrPu7caBAACI-8XI9UYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEl_wuL-j8QOslsJR8sfss8-_m88qKjiScpQSIO-JTPk5p19_-Rsa4yaaZ7fIdEz-7m3Swg72uo7a6UUmq6IhMy8_Azja6Pf6K4iUOD1bfX7N2mIhhG0mYhlPe6fhE8GSoflFpKc_66yABp1UumlR5-hVlO3_9xJVx4ttE0s2nogpOzrpiHRzFq9rbaEPTQ3ESmzRWisouOcXFZz_ysAIdNAvGu-QjzOPyE_YUMxYFGBweIObamkRhm3gppixhfcJ3bE1fSZ5uUCjSv3_EovuUt6kQglQChbRpHIHvBxatvurxspZKYaPCow6avjMeLVvSdoeAzcHUJis5hZDqiRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkp7UOyRbwyXBZVhKnz88XLRmBaxRaUJWo6r-qgo7s847jcAbwbcK-U1km6bGTBD5EkzTxy8fcRkp35kJkDqo65MWgbhSa2EMRcZrfeN2Ar3pgTZW9VPTU3YgXzj6sYhpgWzeu8P_90hdLZh84vndDDP3M-ivS6WB6Kk5FS1qsuUGfOh4p9Ef1xf84556waIJKzVMQP5c1-FNJWEf4AtRMenduj0P0mehOyTV2WvdZQleiPCq3_PQdhilwkw8_5Aktk-kLRaOFyk0JsA-8bjMplo7l-acvsWW9d_ilGNRfnBqkFRYWpv9C2ZI2Nh5cHnA6_pM52l7QQvusXKNCTNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=UEBTSNhm0VFS1q8vO5b4_zqKUAayYeVDutO0iv_oKD6t-SHNgShjWcMm4HIPEH5v1VNrfPGRsfWP2op5uHDJwDPAdPqP1xehlpFb8dfth7uAfryFx2iICt7UNZq478j55pATLS273Iv5VwlVWOyUWuqyONerYYlsdKMmexQ_e4WlfrOeZ16lLt4RxAemQe5ickj_ZloQVemy1GezZAi4GhNzflxX7RPV8DeI9NSvYNGkZnTmoMeAov0f-7tUeXXeImbHpIdr81gpCRyupk7iwb19vcg03F_voSYL9nUDy1YDnlBGg2WeylLo8J16AsWHLWzJySdVX-9xbJ0_C1nXJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=UEBTSNhm0VFS1q8vO5b4_zqKUAayYeVDutO0iv_oKD6t-SHNgShjWcMm4HIPEH5v1VNrfPGRsfWP2op5uHDJwDPAdPqP1xehlpFb8dfth7uAfryFx2iICt7UNZq478j55pATLS273Iv5VwlVWOyUWuqyONerYYlsdKMmexQ_e4WlfrOeZ16lLt4RxAemQe5ickj_ZloQVemy1GezZAi4GhNzflxX7RPV8DeI9NSvYNGkZnTmoMeAov0f-7tUeXXeImbHpIdr81gpCRyupk7iwb19vcg03F_voSYL9nUDy1YDnlBGg2WeylLo8J16AsWHLWzJySdVX-9xbJ0_C1nXJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=qyxqEK6HZ4kH3fDUNEW_r4f0wkGxaT1N3Lnw2Fis3Bf3n-dzUxltLUwBCHdxbBXfMSoZvCDRo2VWr3xmgdJwxTF3molSBKyCimGfvWIWQtOlQje198ifkm5Oj3pz1qMhV411bjjU2ykaoP9XREmTP4IgKikfgREPHKTh1mPaVJLcPHakmHHeQZRXIHqWMXIZhHU_tfTwFigIaNLvLYm1IC2M6MyuyiJc2hnuP-6cqtx_vGD83XqD2a4_w7MErLiCM0KWCZ0wBt4YuB8TdPXV3-6Pb5pjas4wHOZHpohp9JHtx7XbbmwVOKIuLUQVm-z9btGhakjzHK4EfDRGGRTsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=qyxqEK6HZ4kH3fDUNEW_r4f0wkGxaT1N3Lnw2Fis3Bf3n-dzUxltLUwBCHdxbBXfMSoZvCDRo2VWr3xmgdJwxTF3molSBKyCimGfvWIWQtOlQje198ifkm5Oj3pz1qMhV411bjjU2ykaoP9XREmTP4IgKikfgREPHKTh1mPaVJLcPHakmHHeQZRXIHqWMXIZhHU_tfTwFigIaNLvLYm1IC2M6MyuyiJc2hnuP-6cqtx_vGD83XqD2a4_w7MErLiCM0KWCZ0wBt4YuB8TdPXV3-6Pb5pjas4wHOZHpohp9JHtx7XbbmwVOKIuLUQVm-z9btGhakjzHK4EfDRGGRTsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzGYvMLvlS1ECh9f6n3tRqF5f4f1RZNt7KPC8ylNbI4PwT09oSR1RuFlPEw1nDQjfMlYNN3m1hA5kgBz52UBx9FiqL_THaVDF3ScxoSV4s5Rse2chQ_oyQFL33UhFOFP-Agxub3CCr-JZF1_mrUWpWTBhD2ZbM0NZExmsviddCO2hK5HztvUJm5nDlSvjWddulWDRB9ODwnO0GGOWnklnFrC3WJtnGp0sYJrY21aeRqILwLFYQBf-FI7CMLxN83b-ovcKyelI8758i0k65bxXor3jcyJCFvvGjVS3Z1Kve1SMGO84ZgAxiVINEcBoK97RFYD7EpF0CAFab_ABjLPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=r3_wHu2boVO006CboQSCevuad-nvscKVKQbchoeeRzENCBgVTCnnUmmNiEMC2Ap8IdCySN73YlC5wkG1i8pl9kEjGI1DcjBnJic7uQYWuwGViW0hd18zzjfB4LPxePFK4oKa_i7np18QGnmUmeJwSnL0Rq3T53Io1CR8Kn5FOaBm9l5zSg9F-Krcvie2Ket892Rj_XoS-6mExO82QMCGSK5mSsyhKJ7gVWv38LKIYLqH09Vvw54JI-C5EYiDNs11DFh22ci1GskpYQW-F9EbNcAXhkLx6FA8s5rFCEPXK9o36MHpJNIvbn1HrN0is0dnMMB4xVSLU3RbT2XP6eauOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=r3_wHu2boVO006CboQSCevuad-nvscKVKQbchoeeRzENCBgVTCnnUmmNiEMC2Ap8IdCySN73YlC5wkG1i8pl9kEjGI1DcjBnJic7uQYWuwGViW0hd18zzjfB4LPxePFK4oKa_i7np18QGnmUmeJwSnL0Rq3T53Io1CR8Kn5FOaBm9l5zSg9F-Krcvie2Ket892Rj_XoS-6mExO82QMCGSK5mSsyhKJ7gVWv38LKIYLqH09Vvw54JI-C5EYiDNs11DFh22ci1GskpYQW-F9EbNcAXhkLx6FA8s5rFCEPXK9o36MHpJNIvbn1HrN0is0dnMMB4xVSLU3RbT2XP6eauOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=r9yrx66QWcg1Xs8n_qRyGeOS4ljfTDnh1GHxPOSaqEpBZvT8fcnuBDtoexErLlkr6H-4UvXMilUV1lxPtID9MwWZSYewaZbzy9A4OGcbvO0XcwQtlWSVksH0yuXarDjk9Lr7mIc0rPbKYWwgWRiuOWW8Zb6CbQRE61mTuzts5iNnyyVMDV-cjBCkOoweunYrCIqnxn3eW-9esMQ64i8J57FbGUnUzwzRtvw2T6elAqK_Pup4YEX_eAEU86NdRXEd50E_rD2bv1A1gVrAW-0mRssqBLowY9W5g5Uo1pP60dO4-0_5U-x3gTLkvxm8Cg-iH-3IaKH3BLPXMK-zGYWcOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=r9yrx66QWcg1Xs8n_qRyGeOS4ljfTDnh1GHxPOSaqEpBZvT8fcnuBDtoexErLlkr6H-4UvXMilUV1lxPtID9MwWZSYewaZbzy9A4OGcbvO0XcwQtlWSVksH0yuXarDjk9Lr7mIc0rPbKYWwgWRiuOWW8Zb6CbQRE61mTuzts5iNnyyVMDV-cjBCkOoweunYrCIqnxn3eW-9esMQ64i8J57FbGUnUzwzRtvw2T6elAqK_Pup4YEX_eAEU86NdRXEd50E_rD2bv1A1gVrAW-0mRssqBLowY9W5g5Uo1pP60dO4-0_5U-x3gTLkvxm8Cg-iH-3IaKH3BLPXMK-zGYWcOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=rZbcdBjOu79SV_ZcQuVV7BZAtBQJqNzqbnffYGdfL2QunXck70cQ6WnsTLXupNuyroe1NCv5V2oAAS9sOxiOTmc9gtU-0gxEiuAso5fmbkkLW0Mle_uwrk9VtfJ5bychiOhHvn2R4A5edoO3QVdGWiz0bRazsLpQxj5zABCmmDY6R4PJ8_ZijB8mg5QuWoovPstJo1RNJ85OXJ7CMREBCQiHymZqKK-wBP6R0pPtkfzj2JD5DbaZNqGM-uEEUTzMf0-5xAFliXBV1sCuicl0YVRUnwDGHDN98aXRZtKFj5udw_jMAmFUOrXgM3VFZXpej-Q5iFrS0j-61YAVHqjbuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=rZbcdBjOu79SV_ZcQuVV7BZAtBQJqNzqbnffYGdfL2QunXck70cQ6WnsTLXupNuyroe1NCv5V2oAAS9sOxiOTmc9gtU-0gxEiuAso5fmbkkLW0Mle_uwrk9VtfJ5bychiOhHvn2R4A5edoO3QVdGWiz0bRazsLpQxj5zABCmmDY6R4PJ8_ZijB8mg5QuWoovPstJo1RNJ85OXJ7CMREBCQiHymZqKK-wBP6R0pPtkfzj2JD5DbaZNqGM-uEEUTzMf0-5xAFliXBV1sCuicl0YVRUnwDGHDN98aXRZtKFj5udw_jMAmFUOrXgM3VFZXpej-Q5iFrS0j-61YAVHqjbuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=a8K_13abKfSoq_FDKUU5ONhnd87lloYjGkz2CJPpgDmgHA-os15nxGYm3Wq72eiQ7HdHCXet6sHrRx4FN4u0Z5Yz5vrPA01A7SB2_eRp1kqz95r2c6yXdxwrp8XoiaD9kLee7ZCPaXwjFe7PSt02MsHNXMXlAkZzqDyHoCsA7cA7r063Tr_WkV3I1gS1_XzsfUQc8VH5meqfRDjOMMYeM8Ewg1o0-ftWmS41fLSHKugMwL8SqODMBqDikuamaUrHxKC4shk-0wq7fPvijN6AeyVIu_xK76K1FKSHR8Tpaz5LRFwfYA_H27v3ApdnQBWeD30KlT-5pe0yyJWZyJGj8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=a8K_13abKfSoq_FDKUU5ONhnd87lloYjGkz2CJPpgDmgHA-os15nxGYm3Wq72eiQ7HdHCXet6sHrRx4FN4u0Z5Yz5vrPA01A7SB2_eRp1kqz95r2c6yXdxwrp8XoiaD9kLee7ZCPaXwjFe7PSt02MsHNXMXlAkZzqDyHoCsA7cA7r063Tr_WkV3I1gS1_XzsfUQc8VH5meqfRDjOMMYeM8Ewg1o0-ftWmS41fLSHKugMwL8SqODMBqDikuamaUrHxKC4shk-0wq7fPvijN6AeyVIu_xK76K1FKSHR8Tpaz5LRFwfYA_H27v3ApdnQBWeD30KlT-5pe0yyJWZyJGj8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5YMbsJyMjQGzLKVjbwuf-JK1K1yfy8kpalxAoD4k5GME-De5ctWPbo1ZygUPTf55zUuDpidm67bqBizfOpXBhSv0ITUoNO9d9d3BcONwkS-WZAw3WmWHIIU0mdsfMeKHCyRYNuHd3dbaZRVXgxJGdSqPIkx2QSJHBLuNdJswPqAsVOcVW64Cc7J0wP03VolSWjNok4dRdgKSuH0baS6zvBKkIq4vr9JMf_bBi5Wxqu_SZoZ0a_U6r3x6ynvxpsMkYkbp8yQGpgNUJFn1GKBvpiDYAOpp9ZbxiPwbdKoe66o2IKcbDpwd0Dp9Osbl_3PE4ZX50UUzdBIcA59yt7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcOHQjnoiz40lJahpMEWLiX2OHvhiCi8OClKHlas3hRiLVP7plMIjkOCDjy3AazxnKbn3sisV1i-6ZKk_nrS__6jKVQnTAjg8O4X95yp5_bZa7IBPyHouFgM6FRL0qFo5KOGm0y0YXrxDfykM2iZjEF0wU3-2NLa6P2P5t1OfFvRkQYiP821z8JuL5D7oR2nCy-lp3lPN_uqIgR5P8PYSpgbtnZXJK-IzlqH-SM6xbsb7MmdPJ96G_eTu45Wpxe7b3tFFI81vtAqndJ720ge7L-LoqOfpXK32cYDRtUGR3-dbkUWdT5gDTNo5-_cGb-wI8AOyNUvHVxWUhOGxdrwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PenRf_laJAdvwn89DcqrTyyHuRfLXLf2juUbOVa7O-hPSpkI_5r-XyuOV_i5YawkwzpA5ZWVEEXz60-YC7PtdjO5inKoEXCitB_cFG1f013Bxs0BNsV7jjc8XDQoceZWPE3qALaFet1JEbt8Mik-LsCI8hYp4Jl9aLEmsdWPFct96wxl0lBb_QUNxogO2T2_H-axqsTP6gf_cuowEkskB6ifoVmaaUjHRrJmHEWDqN31uvphXISKwzXTglZY6GH87zCG2wDNaeDYbq7KG5FMsSUMRB-sJJyHnOiW706RKmOmQeF1DsRw9fy02_SjmZbvjwtmNZi8CTSNIoj1NJr1YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
