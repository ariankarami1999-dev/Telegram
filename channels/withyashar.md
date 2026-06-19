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
<img src="https://cdn4.telesco.pe/file/J7CrJOBKNgmDvdO5bIZs5mFAzD9UO1SCVYtqipE4XFFYaVH60gCuQ9gg-JIo4GL7cwo7fxUbaJkv3bTI--Cz749PCqjEXan3hGO9gg3ySTHBEq9k2_pSH3Krxl_UTjVFfb5JHl-OFvkZdRdNW8slTmDUKMjGLPbEoHHcLHy5-JRrQA-T5PY9kAgMcJ63A_Q6o4Dg-QXXbw1X_BH5mFfLrl4mK0S9vSg2yFDkGlwZPCp7Dx6RRKgfThJ4qmI1KINF-3j0uK35QpwYBJ2uRjubQjTyabTm0E3Lw8dQr8hpo7TT2EBTM2ZGETOxdvD600UsweWPGHkmCOo60CQFCS0JBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-15292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه  رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:  https://t.me/+hLt81qXCGTQzOWQ0 https://t.me/+hLt81qXCGTQzOWQ0  لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/withyashar/15292" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه
رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0
لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/withyashar/15291" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15290">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش های محلی در جنوب لبنان،
از حملات هوایی سنگین جنگنده های اسرائیلی خبر می‌دهند،آسمان جنوب شرقی لبنان به دلیل شلیک گسترده منور های روشنایی ارتش اسرائیل روشن شده است.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/withyashar/15290" target="_blank">📅 01:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15289">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.  https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433  ترجمه :    ببین ترامپ،  می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/15289" target="_blank">📅 01:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15288">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.
https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433
ترجمه :    ببین ترامپ،
می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این دیگه درست نیست. مردم ایران از این همه انتظار و بلاتکلیفی به مرز دیوانگی رسیده‌اند.
این داستان را تمام کن و کار را یکسره کن.
خیلی از ما در این ماجرا کنار تو هستیم، اما باور کن این آخرین تغییر رژیمی است که حاضر به حمایت از آن هستیم. بعد از این دیگر چنین چیزی تکرار نخواهد شد.
عشقی.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/15288" target="_blank">📅 01:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15287">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر دفاع اسرائیل:اسرائیل توانایی انجام عملیات مستقل علیه ایران را دارد و در هر لحظه برای اجرای یک عملیات آبی و سفید در ایران آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/15287" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15286">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل سموتریچ:
غزه در ویرانه باقی خواهد ماند. در نهایت، مهاجرت رخ خواهد داد، زیرا در دهه‌های آینده چیزی برای جستجو در آنجا وجود نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/15286" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15285">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ: پیت هگست قراره خیلی پیروزی های دیگه بدست بیاره پسر خوبیه
من فقط مردمی رو دوس دارم که طرفدار من باشن
@withyashar</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/withyashar/15285" target="_blank">📅 01:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15284">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.  https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==  اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/15284" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15283">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">subseven</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/15283" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15282">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/15282" target="_blank">📅 00:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15281">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.
https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==
اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/15281" target="_blank">📅 00:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15280">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfpGymKndKBQPowJqchYHqmJUoU1627eCCKWIaEMpFCykPoxwrhsJk-RnJu-P4ujRbSrPNV-1b984z_tfkIr1XpiZMZ_o_ACZe0XWzi0-XUYQxifU3fj22bH46R6d8fxUA7LNXQ52FVaLVO-kF7iPxt0ZBeQjQj2zLSqQQM6-JxUE7iN2tBcqyAjQruIJTf4ROnt9JTPzNauMQ0cvgUWszY3ATeQfsg4xQlnhUerEWWCscr73noWUGS7FAgUN5KeNtBrkfNCzUxQWDrcGMyWvjTI9k66G1Uv4uuvtlhMPmAPsC5OXMW3ZAM1UHcmEFgBrVzUEcofdzemy47X_JQMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/15280" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15279">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر جنگ اسرائیل: قدرت ایران را درهم شکستیم، رهبران، دانشمندان هسته‌ای و زیرساخت‌ها را هدف قرار دادیم و برنامه هسته‌ای ایران را از بین بردیم؛ اکنون باید اطمینان حاصل کنیم که این برنامه دوباره احیا نشود
اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/15279" target="_blank">📅 23:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15278">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/15278" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15277">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYjMiVmPna0K7Az4ojIUTnb-ZeiZXudnnibHxGZGDnmw01HP1bxnyjCIVsGTgjSFIO6qwfbZ2xLzODAivxTxz04IUVhbseWa4XdjJW3Ya-HqI_TrQliMWeEkqyKRvOu_TP-lc8vzSJX6Qy-wKixxs_SJMfuCc0zFwBM9b-70HRNLLsp_tdgSGCZzXwxQbhiEJvE3Lx66OS3IhyUOUBOu0QyZ_UhY4TEH9DAM7erm2tUWdNJWoIKMWpPTAn39hN3V_8NZzhE6Wjl5BuukHtvXHMWgEDeVkMDLqIwzTput1G8IyBbRE80YWBApO-pKJslUh6I-vXfdADrwVXRjh3UEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ایالات متحده به صلح متعهد است و ما از همه در خاورمیانه می‌خواهیم که به تعهد خود برای پیشرفت عالی مذاکرات ما پایبند بمانند.
بازارها از آنچه اتفاق می‌افتد هیجان‌زده‌اند:قیمت نفت به شدت کاهش یافته و سهام به سرعت افزایش یافته است.
ما انتظار داریم آتش‌بس کامل در تمام جبهه‌ها، از جمله لبنان، «حزب‌الله» و اسرائیل برقرار شود. از توجه شما به این موضوع سپاسگزاریم!
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15277" target="_blank">📅 23:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15276">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شورای عالی امنیت ملی:
بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/15276" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15275">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyegi❤️</strong></div>
<div class="tg-text">به یزدان قسم فقط کانال خودتو میبینم و طبق تحلیل هات روانمو سالم نگهداشتم وگرنه با این توافق الکی که پیش اومده خودکشی میکردم
😮‍💨
دمت گرم
🤍
من به تغییر رژیم ایمان دارم و میدونم طبق گفته شما زمان بر هست پس صبر میکنم
پاینده ایران و جاویدشاه
👑
✌🏻
❤️</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/15275" target="_blank">📅 22:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15274">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آسوشیتدپرس: کاخ سفید توافق با ایران را به کنگره ارسال کرد
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15274" target="_blank">📅 21:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15273">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فارس:  تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات به لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15273" target="_blank">📅 21:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15272">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رهبری سیاسی اسرائیل به نیروهای دفاعی اسرائیل اجازه داده است که در داخل «خط زرد» در جنوب لبنان تیراندازی کنند.
انتظار می‌رود مقامات ارشد نظامی در ساعات آینده قوانین درگیری و راهنمایی‌های عملیاتی به فرماندهان میدانی را به‌روزرسانی کنند.
این تصمیم همچنین شامل برنامه‌هایی برای نابودی هر «زیرساخت مرتبط با حزب‌الله» است که در داخل «خط زرد» شناسایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15272" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15271">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15271" target="_blank">📅 21:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15270">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-LpCRUSCe0F4HdVfwE6VnmNYqAP0SwZ8tnKlgvN1bxFn_VJRxLL50Hg7Dvyli6R-2m_FNW3nG-gL70sxgoLp7rVSBDhQKJUklGLPTJuBk7HvJZCv5uqQ9TkRWqj1I5vBI2sjWhS04Sui3wVw-lKe2V3ipsV0yaFxL_nUEW3P3KgnBxxxPpLp16OITpWX4-7PulNz3scGpciBBuIANfelbwT0bDYeahKSetEkWgVFkK-rRHwHXlJpFV9_NaYNToVpHtUTDMSRBXc6LRC5Vf2pMSjByjJ9s73r7ETLC4urgH15nnhYyjWzfX6lW4FKlQY1Ri_Jq4_vZrb4EChLNfY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:  پیام جدید  iRahbar
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15270" target="_blank">📅 21:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15269">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15269" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15268">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOTI1Ma4610HxDhzEDYLj9__eUtDcnBuauDXiuR-FINq3qZ2DHm3yaJugXwLmOgGSPV5QXrbFxkpwBmVEbEvsy-9ba6G-yhUzgS8mcfiMDjgSLTW3TMQ7QRdJ_SCrHtKyp_D0TZMeTogYtAL3gw29HtTphooao_u1YA861OY0f8yydF-m6g2TIVAwEcQ5M1eDleBK3idk4nc0EoitUuHob6tTbNc0f8nF-snqsD_aJsoR6Wi1n3XPshmjyOWvwvpSIlwYwNst6tQevvcwV2dT4eteXaU5K8rACh1InwT99wsF1np4mww_M9m8tNKvkT0-x5AUzObquIay6TS2vulwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : هیچ پرداخت ۳۰۰میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15268" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15267">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/15267" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15266">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvzQU5Gj_M8yufoe2Sw9GsCpBdzMSIaaEbMKxEeA8JtayDxaO4SW3L3hyfOE8gOULAm-ozD77aBKUKFVTAUsJuWALi9RR_nTj1XUDbN1i3gOI2c5m-3rsCnVPRLfmltZW__FcaR5Kz8KhwbqGgg1Xrv14Cwd2uaR3w2QF7YPOdMKwSpicfRpP9HxZZ_3iomKjwFksT1-SMv2A2d-R4GW9T2dGtl1IaEARxeWk39ujAEwFdEyYOd8KMN54kL3yHqr5Tew8-nL0BdaqJquyqK3TaxZqf9v5e3x_W4Pa1bqhnOHf4Yin5at6p0KYrPeMtzlUAy06UVf83ChuBCHkXHsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نیروهای ایالات متحده، بنا بر دستور رئیس‌جمهور، محاصره تمامی رفت‌وآمدهای دریایی به بنادر و مناطق ساحلی ایران و از آن‌ها را لغو کردند.
نیروهای آمریکایی دیگر مانع تردد کشتی‌ها به مقصد بنادر ایران یا خروج از آن‌ها در خلیج فارس و دریای عمان نمی‌شوند. تمامی اقدامات نظامی آمریکا برای اجرای این محاصره متوقف شده است.
ناوهای جنگی ما همچنان در منطقه حضور خواهند داشت تا اطمینان حاصل شود که همه مفاد این توافق به‌طور کامل رعایت و اجرا می‌شود و از قدرت و اعتبار کامل برخوردار است.
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15266" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ونس درباره نتانیاهو: من گزارش آکسیوس را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15265" target="_blank">📅 20:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=iA_T_beZpXTL0WlJXYim-ZURdKL-Cey3eVd6h-M55bNGTALsSDMSG3zNaYN-1jOmRvLmGag5kEAYH5zeHCA9gjle9nRPaj3NuY-KC8H61YN7IdMYBg0By_8H4h95wDtUUH0yvT00fOO2UnZp1THElhpCTgKZXoyj3FNDMdFq_4bBDm35agbunvxAStdSuSl9cZ5U9_acS_OWEamW3ODyTV8MyjVHAIJRFP5-xoeuRY4zbX_XAklnsfuBilczkxtowHNxk7fhDA8DDiOzirSm1hW9rrn8tiQ1eaFnJOQu_I_j7_vLPlfvRS-l7U4HoziFiv8hPzTbY06Ib5R4fXzYcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=iA_T_beZpXTL0WlJXYim-ZURdKL-Cey3eVd6h-M55bNGTALsSDMSG3zNaYN-1jOmRvLmGag5kEAYH5zeHCA9gjle9nRPaj3NuY-KC8H61YN7IdMYBg0By_8H4h95wDtUUH0yvT00fOO2UnZp1THElhpCTgKZXoyj3FNDMdFq_4bBDm35agbunvxAStdSuSl9cZ5U9_acS_OWEamW3ODyTV8MyjVHAIJRFP5-xoeuRY4zbX_XAklnsfuBilczkxtowHNxk7fhDA8DDiOzirSm1hW9rrn8tiQ1eaFnJOQu_I_j7_vLPlfvRS-l7U4HoziFiv8hPzTbY06Ib5R4fXzYcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/15264" target="_blank">📅 19:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9uTCS6UmkLU-Gjdizs-VtqhSpcRndlM9cB1Clf4FwLDi-8MqlOuwdVuhBIrddWnG3GPnhJmyaQOCSdYpzjAqfVbI9dWyLZOjkokrkJU7Fss0HCSjNpnYm9jN0V_iWlMAcPorQOndfUvHhU1cLCAb62-4-f7_vyRLHOvk1jMtCGlBWKQ2zRzgRWfD2g49Pa0XG1ghP-XRyWV-Nyq7zLcyvUSfRnlVwcb0MtcOp9Qqav41dqcWQYJ0OkesrxTnh_G4wGp711kA8ZtJPghuz_7ZpuFdk98Pq0NfiC1VrkjbZLZ1qD_WwwGSILtzmyKhuOIkvFNb7JqcNGLUTdlRUUyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ترامپی که امضاش اینهمه بالا پایین داره انتظار ثبات روانی دارید ، موج مکزیکی هم رد کرده نوار قلبه
😂
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15263" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ونس: اگر ایرانی‌ها رفتار خود را تغییر ندهند، ارتش و برنامه هسته‌ای آنها همچنان نابود خواهد شد.
ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15262" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آمریکا حتی یک سنت هم به ایران نمی‌دهد
جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15261" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">معاون رئیس جمهور آمریکا: دوره ۶۰ روزه مندرج در یادداشت تفاهم با ایران از امروز آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/15260" target="_blank">📅 19:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15259" target="_blank">📅 18:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15258" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15257" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5wtfMT7D-7GBBUKvy8aB5GVUu_5V7pOqTvsAUv3eKZ3sC4OQ-ISDzVVC2VB2oGUIzWK7f6P7Pqo6vWiVknPLxY4k-3FU1uqn-Xt1MX-hHLuM92hWH0hRi5uSmTmUcRBqr3O12NYbCP504keOWflwf__evZFQvnGCbmR3Hhttx0nxTwjNBNxo-fM22ld1Uih0yjxb6bv31UxBIg0Om88Q_ZkXKTaSXTar-tSCKGoYcjqJied1cnzcf1agBTQy1Nq_xV3Ikg39MJRqyacObkyy8051hOWHhQu_ZA2dkgbL_gfKW-1KW5tn0aL6hKG18MKz5cRYlv9t-7c9lOBozlfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نفت در حال جریان است، ایران هرگز نباید سلاح هسته‌ای داشته باشد (جهان امن‌تر خواهد بود!)، بازارهای بورس با قدرت در حال رشدند، اشتغال به رکورد رسیده، و قیمت‌ها در حال کاهش‌اند (امکان خرید بیشتر شده!). کشور ما قوی، امن و محترم‌تر از هر زمان دیگری است. “خواهش می‌کنم!
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15256" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15255" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">از صبح حملات اسرائیل به جنوب لبنان پر قدرت ادامه دارن
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15254" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3483473645.mp4?token=TrHjPkqVlg_rE4MR5dNCa_BePy5QfyaCHzvYCe6Rbh7fuXo7bO-xzJTV0sSChMjSavhLM9lsQf12dV7QO_X24eI_qaYx3Ie0ifju8SvSW_isL3qwaacvc-e6qPFlXg2lCRA4FMSMSBbsX7XDQuc5Np0u2yjSbDWy9ENmkSaZ8nZ4rWAGaE6ALEu4GFc7IzjU1kEuCOawhz8u0Re8QGzDsR-T7CYCyoYMwotAemtzGs8x4m-bI-m_KEDhndQndtbgaUmcc_d-Khq8Z468jt_g1VJ4SpQYJ-ukZJepFyN9pH1EF9ZvBsGP5njTY4WK9puzmxNG2tTWf9zbmiDpO3rkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3483473645.mp4?token=TrHjPkqVlg_rE4MR5dNCa_BePy5QfyaCHzvYCe6Rbh7fuXo7bO-xzJTV0sSChMjSavhLM9lsQf12dV7QO_X24eI_qaYx3Ie0ifju8SvSW_isL3qwaacvc-e6qPFlXg2lCRA4FMSMSBbsX7XDQuc5Np0u2yjSbDWy9ENmkSaZ8nZ4rWAGaE6ALEu4GFc7IzjU1kEuCOawhz8u0Re8QGzDsR-T7CYCyoYMwotAemtzGs8x4m-bI-m_KEDhndQndtbgaUmcc_d-Khq8Z468jt_g1VJ4SpQYJ-ukZJepFyN9pH1EF9ZvBsGP5njTY4WK9puzmxNG2tTWf9zbmiDpO3rkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز شبکه پویای صداوسیما اومده و یه برنامه کودک در مورد توافق کردن و سازگاری گذاشته که تندرو ها به شدت عصبی شدن
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15253" target="_blank">📅 16:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AicMqNaDcrF8v-m2UVuiYOkXkfKr5ndKEXKLJUAvHY1fxGaud490i7_LW8Q8w-4tq6GVbAZod6kR3asUe2Bm2LdUkNzDvRbUvjUTJQ0CjHztIxdDu_a2ADPQCh6ja5Xn-IC0DvSfOu6yhsOosg2Z2cmaphFnQQf75ccHJVxVTSsMLZzvBN8MmylnkgOodzSWGoVTkLUohyhT4roPTHgBT7qefdBin4VvCX5BWmndHDZ5JuCDhSXGzZ8CdDJvDbqZ69VcbyRr_KIqldffpN3TI8wgbJ8Cvc01nxw2527Km2a9JwT_mXK3v4es9pBpSGSLbaX-0U6ivU7ph0psGR8Hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15252" target="_blank">📅 16:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله... @withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15251" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/15250" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آموزش و پرورش
: ثبت‌نام برای ترمیم نمرات تا پایان هفته جاری امکان‌پذیر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15249" target="_blank">📅 15:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=Kxua71oMSlhnEJuoHZfHLETKaEWl8M5JlKOoK7zR4SXUyNrsQskJ87vGMeA3OWae6tfmSgX58OmwYUnyZWZ99eT2xvQM5o9WvlFCSwjVoEJAXGNneV9OVGgGxVpEBSuAC4MaFr4mgts01BoH-j7SZ61jQUUVOwgcb0HKVCXy0S6i8pMs5R_j3t4BuREoaZ13DPwnU2JMN3EvJjEdM-MxJAZNQuP2Cv5LvS4tSvExBi5WASyU7Ov0MxASZPXAk2EK3yzd7YSaCy_yN88IqFhQx8m65ZM1GBLRwcUe_cy7XqXd-WNxEZIto9b-6-P69--zDhdymdzUFCVxFvEqTO79yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=Kxua71oMSlhnEJuoHZfHLETKaEWl8M5JlKOoK7zR4SXUyNrsQskJ87vGMeA3OWae6tfmSgX58OmwYUnyZWZ99eT2xvQM5o9WvlFCSwjVoEJAXGNneV9OVGgGxVpEBSuAC4MaFr4mgts01BoH-j7SZ61jQUUVOwgcb0HKVCXy0S6i8pMs5R_j3t4BuREoaZ13DPwnU2JMN3EvJjEdM-MxJAZNQuP2Cv5LvS4tSvExBi5WASyU7Ov0MxASZPXAk2EK3yzd7YSaCy_yN88IqFhQx8m65ZM1GBLRwcUe_cy7XqXd-WNxEZIto9b-6-P69--zDhdymdzUFCVxFvEqTO79yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درست خوندم؟ Porngraph?</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15248" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirAbbas</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD6qObEucJYEmG-rUyXbA-HWEWxwSQZy-o4gGv8fc6JplhbPyuLvMdlaR9E7C5JzCrsJ5sJIOjJhWwKUB1j4DkbSbvDDk30IU9mAeg424vKfvEI9PKP9JqQH7izsq7gmMaovZRpPNUFRy3yZN1omWcrlOzXyFNF4rPScF2xKengD0KViG3LJU374QB5cpkeTCydUcaU6q6IYMC3Qa2nHxcTmCsKEG0sVS61UooAYU5eqDMNdPcshCh_NIMM5xK8ABXdE1yYYHgoej23yrlbkQdR4T9wKBtQunEoPrA-r4qRNSFMoyzMvqBVfgFxcpgJBd5XsiBrXwIokL8C37aMnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درست خوندم؟
Porngraph?</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15247" target="_blank">📅 15:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15246">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15246" target="_blank">📅 15:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15245">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شبکه کان اسرائیل: موضوع عقب‌نشینی از لبنان هفته آینده با هیئت لبنانی در واشنگتن مورد بررسی قرار خواهد گرفت
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15245" target="_blank">📅 15:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15244">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرگزاری CNN : نتانیاهو معتقده توافقی حاصل نمیشه و جمهوری اسلامی با پایان دادن به موضوع هسته‌ای موافقت نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15244" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCjjJIiviy8kzTeiaD6goSZDlqxtDRZO84_36IQHf271m5KE71_4rSVvjxGZan42-qGOezmFKVPeaqiJrZWeSdnKNB5SypBe0IWjgkmW36bks6Yx7ZD5l3eZxZBkcLVi6mYIxPc50Q5g9qKWy1BYpVPtjYmMcXRK1kbwplJAwYJ1XJRCcnDr0s7fgnMZFZ3XknvkUxcrlpt-hh8QnQsFE5gCma5-GHtets28pcA8_z8tkOMeUNFTwmgPtrm7v5glcWLdsFKDdVg3n_yrtLBBhC_R0pL0yDaSpHLCjz9gKs287N7rGNtHqBXz7JEuFYWDOUoOgzDXHySUGzMa9r0bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oazdKuRnERGuoCJBrM18Ex0nFVsKrO0PRaHJs12GC1lZt_FghjKv5fcXdLBCRrFT4QLDa5oYtkPDkkErhO9PL7yiCwXiae4FKsLd5fJJy0p4Id--0RZfUgGEZm3_g6hXiVJpt3UrCjhCSLMfMRgt9OuY2LcBXi8-lCtnwIFcY-rcplHc4rgulkM1Ag2sNXzxvePMxOkcLA454b8T2ZQIHVbwaMgc0fz3p4kkENib9OuP9BPa2wACrYC5Q_ng1Ern5xm0r2kcc_uq78Jmkc4VO4hR1MZrM20_QDQ5F1Zq9rH0vxWYLceGPOX0g0eMHBy3Lx9NOmGANa3XyLlzE5RHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhrOF-ANOJOwU8mmYrYtNW8_Hqt9m1Xp0LIZ5BOpZ4L3mlCo9vc3k_OA-LY_2sg4x4zEahjfAX2ksTfZsvSWCw2mWLdzeF4-ZolDcmSZRMzvczdEo1GvmFK3Q3k8MgVkj59z3VS3eTcmA4vnBVI9pTaX3u28KWXMF2ufUEIiw2OtBnV4mw4fzwlwUaHSIr3QHICKqzePOh0zc6lBHUz7vTFIBC0nE8nKbkYb9ftjQlt9j3WR1hPaeZPms8W1BJHUcYVjnmBTQPJGnBqB60Iix_tMxWGc7dzsLNOaVEHeXB43UT9Wj8QQhrlVLxexmrboeiNpJybWnsC7p9U0lWAERA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکان نسخه اصل سند امضاشده را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15241" target="_blank">📅 15:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36518f3c9.mp4?token=PbDOmMQ16I-Cp3qyTmckwLHUjjwilIwe98FeiIw3EPnA0eu7NUgF7seSBBjyU267mUq8Zx7tHmCDkHaW0mCclYSDTGiGBmI1FQbCp5JC9DRxqE5jZhXVKrOqMIP04OLQ8i-T-K3xU1UDnjaUp559wP23Si2fwvlElZHRF_wvu5DdU9FuR-KsD6A_Ii4EZl-xmdsDttk6tsh4kdkuq4PlufxM3IcwqEtBoBHZYFIjam_zZc233Uy1-I_H5Kzz4AX_FAGiFQVjlonKNzIfWwdrlYpEMsOCHacrDgC-_5n1u5JcgY70NpVVRhfLF2qfKU0qF8uiaJlGalk5ArInyy_gzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36518f3c9.mp4?token=PbDOmMQ16I-Cp3qyTmckwLHUjjwilIwe98FeiIw3EPnA0eu7NUgF7seSBBjyU267mUq8Zx7tHmCDkHaW0mCclYSDTGiGBmI1FQbCp5JC9DRxqE5jZhXVKrOqMIP04OLQ8i-T-K3xU1UDnjaUp559wP23Si2fwvlElZHRF_wvu5DdU9FuR-KsD6A_Ii4EZl-xmdsDttk6tsh4kdkuq4PlufxM3IcwqEtBoBHZYFIjam_zZc233Uy1-I_H5Kzz4AX_FAGiFQVjlonKNzIfWwdrlYpEMsOCHacrDgC-_5n1u5JcgY70NpVVRhfLF2qfKU0qF8uiaJlGalk5ArInyy_gzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
40 هزار ایرانی تو عرض دو روز برای یه توافق هسته‌ای یا باز موندن تنگه هرمز جونشون رو از دست ندادن.
اون‌ها برای آزادی و دموکراسی جونشون رو فدا کردن. اما عجیب اینجاست که تو هیچ‌کدوم از این مذاکرات، اصلاً دیده نشدن و هیچ اسمی ازشون نبوده.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15240" target="_blank">📅 15:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15239" target="_blank">📅 14:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">راستی از لحظه ای که ادمین بیارم به شما اطلاع میدم ولی دایرکت رو هیچ وقت به هیچ کسی دسترسیش رو نمیدم و پیامهای شما تا ابد فقط دست شخص خودم امن خواهد ماند.</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15238" target="_blank">📅 14:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دنبال شخصی هستم که برام ویکیپدیا بیاره بالا خیلی کم لطفیه بعد از حدود ۲۵ سال فعالیت در حوزه تک و کارهای انقلابی بسیار بزرگ، صفحه ویکیپدیا نداشته باشم و افرادی که خودم به مارکت آوردم و معروف کردم داشته باشند. امیدوارم یک فرد فوق‌العاده قوی در این زمینه کمک کنه و واسم بسازه.</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15237" target="_blank">📅 14:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15236" target="_blank">📅 14:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فقط ‌یک پیغام</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15235" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e87c2bd5.mp4?token=Jq6GTBvnoDBX1BK_P6lT4oTZEbUdzpvErdTmnngv13Al3STu_ABOlO9_Jy24jBhzS5WJGmwBy4kiBC8pt1kuW8owsKze8s5Uy0-So4jkeNx0bXnB1SY4Gg-CVeKmiSde-IseurMd5kjbF9S-nOGnmrv-ET1E1XxsnKw35xWCv0k0ksOgpFRzjKXgDHTGsaAz6ytfE1hZmIftFAkwkNwqukIOnpSkk8kK5x7ihMCUo83flly2PdXU0Y5pU2KA0HTEh1lStdk2dJlx4urF-p2mKvQMEBhJ8e9FQ-LDrqc9kwQwjnRQyrvcNOr3tYADd-F9g831orZ6k4Se12HqQqF4LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e87c2bd5.mp4?token=Jq6GTBvnoDBX1BK_P6lT4oTZEbUdzpvErdTmnngv13Al3STu_ABOlO9_Jy24jBhzS5WJGmwBy4kiBC8pt1kuW8owsKze8s5Uy0-So4jkeNx0bXnB1SY4Gg-CVeKmiSde-IseurMd5kjbF9S-nOGnmrv-ET1E1XxsnKw35xWCv0k0ksOgpFRzjKXgDHTGsaAz6ytfE1hZmIftFAkwkNwqukIOnpSkk8kK5x7ihMCUo83flly2PdXU0Y5pU2KA0HTEh1lStdk2dJlx4urF-p2mKvQMEBhJ8e9FQ-LDrqc9kwQwjnRQyrvcNOr3tYADd-F9g831orZ6k4Se12HqQqF4LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه سر حال هستین بریم برای مرحله بعدی کارا و گسترده تر کنیم
👍
یه ریکشن لایک بدین پر ریزون باشه تا بگم</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15234" target="_blank">📅 14:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15233">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر جنگ آمریکا: به طرف ایرانی اعتماد نداریم و آماده هستیم در صورت لزوم حملات علیه ایران را از سر بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/15233" target="_blank">📅 14:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15232">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a485ae7493.mp4?token=AjVPWw3wpeP5DfI9YAF9g4dunUA-QVgzY8aF5KfF90B3uU1xolRuGfma04qntBrzW6a2OEZPC5gJmUv4qpbGktSt5Ja6raZIofKStS4YdguxvatwaoFe7AzQHtNttPCIEey8Ovknp4T1ZXKD29qRF0FHklv82BUsZ6ju4WcRz1p4KV88ziTotIJcuQUsHwqS5DLD8OLhkmYX7OQP5lniQ_4uwWtdY15Kdvr8zjDwUHCE-1ABJRF3fHxMLDd-XYNKYM0htVmU-u2eL0IV6ONHid6lRGJnhk4ZwnhQueUf6QqJutl0n1nNBwkV1MrWJO0p9HbOlrb33s2TiHatjwfj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a485ae7493.mp4?token=AjVPWw3wpeP5DfI9YAF9g4dunUA-QVgzY8aF5KfF90B3uU1xolRuGfma04qntBrzW6a2OEZPC5gJmUv4qpbGktSt5Ja6raZIofKStS4YdguxvatwaoFe7AzQHtNttPCIEey8Ovknp4T1ZXKD29qRF0FHklv82BUsZ6ju4WcRz1p4KV88ziTotIJcuQUsHwqS5DLD8OLhkmYX7OQP5lniQ_4uwWtdY15Kdvr8zjDwUHCE-1ABJRF3fHxMLDd-XYNKYM0htVmU-u2eL0IV6ONHid6lRGJnhk4ZwnhQueUf6QqJutl0n1nNBwkV1MrWJO0p9HbOlrb33s2TiHatjwfj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله...
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15232" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15231">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اگه سر حال هستین بریم برای مرحله بعدی کارا و گسترده تر کنیم
👍
یه ریکشن لایک بدین پر ریزون باشه تا بگم</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15231" target="_blank">📅 13:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی اعلام کرد:
در حال حاضر، سطح تماس‌ها و ارتباطات با ایران در پایین‌ترین حد خود قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15230" target="_blank">📅 13:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15229" target="_blank">📅 12:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزیر امور خارجه اسرائیل : روابط با مسئول سیاست خارجی اتحادیه اروپا را قطع خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15228" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منابع العربیه گزارش دادند «نخستین دور از مذاکرات فنی مستقیم واشینگتن و تهران فردا در زوریخ سوئیس برگزار می‌شود.»
به گفته منابع این مذاکرات فنی میان ایران و آمریکا شامل جنبه‌های حقوقی و قانونی مربوط به رفع تحریم‌ها علیه ایران خواهد بود.
منابع العربیه خاطرنشان کردند گفت‌وگوهای فنی ایران و آمریکا پرونده دارایی‌ها و وجوه مسدودشده ایران در قطر و همچنین پرونده هسته‌ای ایران را در بر می‌گیرد.
قرار است در نشست‌های مذاکراتی غیرعلنی و اعلام‌نشده، پرونده‌های مرتبط با لبنان و حزب‌الله نیز مورد بحث و بررسی قرار گیرد.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15227" target="_blank">📅 12:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzHk8sPmmiN9EwKlPDHOFOvT5UV76wyx1LxiEbsZ65IG8aFyTjxExju9N3v_g2CMbYENekKIalkaI2Zs8w8uCI_AOxAcGZpzYwVK0-1da82BrASnEhDUZOAR-vcZ8zgCVFbuD0YJNv71P9Grqr47GpEdIJx4LMomd0l2cktyWDJQWuPFIZoMYHjBYe3N1ozh3h0phRIHDkVH2DmtCXu7l-WNvAj-vQzM6DakuEwL-EmZoIXh-aNQGE7o-qn_2VN0Zg1Oc1Okvgq19r10jVv4Pv460iSIvgenUVBrwnWsxkzeoBDwojJuRCZShG2cD1dYponvOVsK00UalPpAu8gFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث:  این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سختگیر نبودم، در حالی که بازار سهام به تازگی به بالاترین حد خود رسیده و قیمت نفت «به سرعت در حال سقوط» است، یا حسودند، آدم‌های بد یا احمق. آمریکا را دوباره بزرگ خواهیم کرد!!!
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15226" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد @withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15225" target="_blank">📅 12:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5b52d5b0.mp4?token=VWa31Mg712upWKN6FV2Q-wldbdRc5MsDbX64LX0d2TTTlV3ftwwCoTvJDqHG-FUE7rYmIGP7MqaJK8gUwmOmvCHFif2XBmX_hMyu7eiwZUi8j24E8-31ASBmV_e8SMYxowurrvraHWeMfxZHBd8-wjqEtocEnL8sx2yThsh8TaLb-hBb93VlDZAif98KAIXVxBmzAKKiGk-zA91nxbQNI3HgLpWka9WD_8loRaJQaddEgzjv5JcFsUbXWnCaamPls3fbnaiRYzbxW5g9-PhPC09L0PDLZMybhTqYv1atg1cquGgKWKUaEESN5hmh2X_IIv9aTnPiFkoTS8I-5ZWuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5b52d5b0.mp4?token=VWa31Mg712upWKN6FV2Q-wldbdRc5MsDbX64LX0d2TTTlV3ftwwCoTvJDqHG-FUE7rYmIGP7MqaJK8gUwmOmvCHFif2XBmX_hMyu7eiwZUi8j24E8-31ASBmV_e8SMYxowurrvraHWeMfxZHBd8-wjqEtocEnL8sx2yThsh8TaLb-hBb93VlDZAif98KAIXVxBmzAKKiGk-zA91nxbQNI3HgLpWka9WD_8loRaJQaddEgzjv5JcFsUbXWnCaamPls3fbnaiRYzbxW5g9-PhPC09L0PDLZMybhTqYv1atg1cquGgKWKUaEESN5hmh2X_IIv9aTnPiFkoTS8I-5ZWuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15224" target="_blank">📅 11:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حسن روحانی هم اومد:
اسرائیل احتمالاً سعی می‌کنه با ایجاد تنش( در لبنان و …)، توافق ایران و آمریکا رو به هم بزنه؛ همون‌طور که قبلاً هم برای ضربه زدن به برجام تلاش کرده بود…
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15223" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر دفاع آلمان اعلام کرد این کشور در حال اعزام دو کشتی مین روب به دریای سرخ است تا برای یک مأموریت نظامی احتمالی در تنگه هرمز آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15222" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjaIepKR7m8QsnZY4cBxLY7hw5rrMmJN1DE4CIsQWqRx7pXF5OnIKOqW4BvpLkg3WExpiEZzePl25Hg4eJjcNXQKHBrA08FvI_kHzxPQSB2i6PV9jM_QYflWbo6nVbD4VGDNCQkW8tz3bhJeNOzPUVcv6vc-UHELqtCZ-sjpM0itTyJUeM8ejyaw0Gw11JEjgn0nrdL1U_Ui4_mEAqVQUtUmCGxAIO4TIvxkEECWtAOQqAWDB-SiwUwxPwQ5jC89zo2Vss9RlWFDEx-DLds5BMO54YbuSBNw3TO7KTgKvzJU1qm5p2VvNLgi3AhPLzxM6nmxvkBVGqsan-R4qwmU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری متفاوت از ترامپ و مکرون در ورسای
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15221" target="_blank">📅 11:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رویترز: اسرائیل قصد عقب‌نشینی از مواضع خود در جنوب لبنان را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15220" target="_blank">📅 11:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گروسی (مدیر کل
آژانس بین‌المللی انرژی اتمی
) : در مذاکرات سوئیس شرکت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15219" target="_blank">📅 11:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15218" target="_blank">📅 10:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با شما : درود و خسته نباشید
ما که می دونیم به قاهره نزدیک میشیم
حالا تو این راه تفاهم امضا بشه یکم از لحاظ اقتصادی و گرونی بهتر بشه
به نفع مردمه که یخورده تو این مدت نفس بکشن
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15217" target="_blank">📅 10:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/15216" target="_blank">📅 10:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
مجری شبکه ۱۴ اسرائیل: ویتکاف و کوشنر یهودستیز هستند و اسرائیل را فروخته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15215" target="_blank">📅 10:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQFogPciVJumvQRjZcmk2wMwE3g72DFIFQpJeXk5MiwThdQQpQuDiJ98e-t5Xwblp21BR8KMGUEtmyx9u1arJRG0L6y2xhO2qJUyGUe5bnYNSATa4eDAiW0ICjCSCak9W4sicE9f-V5IjB0jNH5968Kb5gGY87wqCNRX57DllAMiVLsixearoe8z54mDTdBNi1plfEesabmHRNJtAI27RZFDlODxG-ZcMBtPlyFV9tHwhrlHjqPXlxFF-D7V8HjS6rCGK9V9_sn97y5qbtUdSeJNifpiR3pQ5ot761ZECYFtjunA3TAQSRbrHxpFdhy11nbkH4G7rmuESqdg5qH2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای مضحک پزشکیان که مانند یک شکلک کارتونی با دماغ بزرگ و دست دراز شده برای گدایی است.
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/15214" target="_blank">📅 10:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15213" target="_blank">📅 10:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردن
@withyashar
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15212" target="_blank">📅 10:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15211" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بلومبرگ از عبور یک نفتکش و یک کشتی حامل گاز مایع از تنگه هرمز پس از توافق آمریکا و ایران خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15210" target="_blank">📅 10:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a024bb7519.mp4?token=VLsAc5ibWf2J1ImKRatDTkg-Fuu95mu6qB2QnpYk7UqOPqvfRDEwXDRytWfDhZNKrpLqYvhzeepHeWUJe-TAK8TsVzxpg_5TXukLHa1vTfJLIFTkNdrSNCUxf6xbaZs6B7ojN27btJu4eLzvN87Uu-LOAw7nXYOATeMhkiNGuld9nddY1slLBE4yuek-9XdIs1JDcYH2RIXgOEBRH1flccq_qANiAwpyFnlfMqwY_AsxsOUMX4Sfe9ijyeflmOOmPeGXF8jHyCBk-UUcXr1i0QhSWwYW4vOe5bG12yCEuD4y0bnQijoQq9c-O8W-aiM3Kt9UZpmpEUC7IYtoBd9qUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a024bb7519.mp4?token=VLsAc5ibWf2J1ImKRatDTkg-Fuu95mu6qB2QnpYk7UqOPqvfRDEwXDRytWfDhZNKrpLqYvhzeepHeWUJe-TAK8TsVzxpg_5TXukLHa1vTfJLIFTkNdrSNCUxf6xbaZs6B7ojN27btJu4eLzvN87Uu-LOAw7nXYOATeMhkiNGuld9nddY1slLBE4yuek-9XdIs1JDcYH2RIXgOEBRH1flccq_qANiAwpyFnlfMqwY_AsxsOUMX4Sfe9ijyeflmOOmPeGXF8jHyCBk-UUcXr1i0QhSWwYW4vOe5bG12yCEuD4y0bnQijoQq9c-O8W-aiM3Kt9UZpmpEUC7IYtoBd9qUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضا توسط ترامپ در مراسم شام کاخ ورسای
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/15209" target="_blank">📅 09:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIu2txy1dP9p2vsJf5VVbxcZ2-nsOrzGvMCIdf-3FSquw3SFhoIfk8xfBo7ed9tP6QG7BMkbJGxtU3S76N-G9HEWi6eF0pg24me2z46H2TAUMB8CIgQ-nlsCWAI8xeKh3FCzJbvCNtvjI7fWZ1RNIm6YnFuCebLNSQw0Mne8ws4yeW1g5U2RKjz3ZyUYu5ealoKT4oxlGmSEdFkgy65s5obW6IlJhVfOtbh4VmShHHUKhmRm9i37ogKU94hQ5Q5rR-ivZRPrIr-HGe684jz9XFaBZi1S14Ksc2M_ojm_BVf5GTJOZZMssEZjqhBTMECZEbLVr2IwMbLwL2tsIFhx7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضا توسط ‌پژشکیان
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/15208" target="_blank">📅 09:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دلار و طلا تا بفروشیم یا بالا میره؟ سوالی که اکثر مخاطبین کانال در چند روز اخیر می‌پرسند   اول پاییز اعلام کردیم که دلار تا اخر سال به ۱۹۰ هزا تومان می‌رسد و طلای ۲۲ میلیونی را به درستی همانند قبل پیشبینی کرده بودیم الان هم قیمت قطعی دلار و طلا تا پایان تابستان…</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/15207" target="_blank">📅 03:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دلار و طلا تا بفروشیم یا بالا میره؟ سوالی که اکثر مخاطبین کانال در چند روز اخیر می‌پرسند
اول پاییز اعلام کردیم که دلار تا اخر سال به ۱۹۰ هزا تومان می‌رسد و طلای ۲۲ میلیونی را به درستی همانند قبل پیشبینی کرده بودیم
الان هم قیمت قطعی دلار و طلا تا پایان تابستان و بعد از آن را در کانال زیر اعلام کردیم ، حتما عضو شوید تا با آگاهی از قیمت دقیق در روزهای آینده تمام سرمایه گذاری های خود را مدیریت کنید و از تورم جا نمانید
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/15206" target="_blank">📅 03:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a8394a.mp4?token=RYNu7Q3IupbaIc8HTnR9wHv3Ad-Gpfu8EP4aFMeZZMI8K777WO30F4eT6K9Ue_e_4gHqHFxm6ZZ_4nmEZglKJ-w0BwT8ufzzdFEMtnOMQfxOO5BWFBm7eqsK8ObCpqDdMpEZ2MhmS_It1am6Jt_lbZiUAxD8H1S5r--zaKq4e2mmxtH1yMUWrj-6BIvYSvAcn7V-85kWOV1OXt-XE3unvTzfyecLkxZ81svIMezjUZnHUJeiUj5X5DFaIR6taL2qm156vaqEhi5qSQqSyBKSLE-yRuZAB9TBfEEfl7nPq04Ahn0e734hTHpUrmDvjMYjsuN9OAJARjPlk_FjG9iGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a8394a.mp4?token=RYNu7Q3IupbaIc8HTnR9wHv3Ad-Gpfu8EP4aFMeZZMI8K777WO30F4eT6K9Ue_e_4gHqHFxm6ZZ_4nmEZglKJ-w0BwT8ufzzdFEMtnOMQfxOO5BWFBm7eqsK8ObCpqDdMpEZ2MhmS_It1am6Jt_lbZiUAxD8H1S5r--zaKq4e2mmxtH1yMUWrj-6BIvYSvAcn7V-85kWOV1OXt-XE3unvTzfyecLkxZ81svIMezjUZnHUJeiUj5X5DFaIR6taL2qm156vaqEhi5qSQqSyBKSLE-yRuZAB9TBfEEfl7nPq04Ahn0e734hTHpUrmDvjMYjsuN9OAJARjPlk_FjG9iGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعت ۳:۱۹  صبح امروز (کمی پیش) چند قایق متعلق به سپاه پاسدارن درحال اقدامی نامشخص در تنگه هرمز هستند.
ناو آمریکایی در بیسیم به زبان فارسی متنی هشدار آمیز را پخش می‌کند که می‌گوید:
جمهوری اسلامی کنترلی بر تنگه ندارد، عملیات را متوقف کنید و به بندر باز گردید، وگرنه نیروی دریایی ایالات متحده به کشتی شما حمله خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15205" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مذاکرات جمعه ایران و آمریکا در سوئیس الان قطعی نیست
بقایی، سخنگوی وزارت خارجه:
جلسه جمعه تا چند ساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف (ایران و آمریکا) تفاهمنامه را امضا کنند، قرار شد درباره جلسه جمعه فعلاً تامل شود.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15204" target="_blank">📅 02:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15203" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15202">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">https://x.com/yasharrapfa</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15202" target="_blank">📅 01:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15201">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15201" target="_blank">📅 01:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15200">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کاخ سفید:
ترامپ تفاهم‌نامه با ایران را امضا کرد
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15200" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15199">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">طبق گزارش Axios، رئیس‌جمهور ترامپ شخصاً نسخه‌ای از توافقنامه را در حین صرف شام با رئیس‌جمهور فرانسه ماکرون در کاخ ورسای امضا کرد.
عکسی از توافقنامه امضا شده به ایرانی‌ها و کشورهای میانجی ارسال شد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15199" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15198">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تسنیم: متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15198" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a3d37ce.mp4?token=QglUtHr2fD12_ouOYZUMCDIVB1hrVd13LyPP7xh_7LB7XfDE06hf--JoCJb4wV9BwpQiCVjTrwyaver09W91_rZb05pZfB_v_vhfR30Ceo4hYk0DSyzhidh-R0TF1sjG7LGqklonTZcJdhwRJdT53bRB3wQUwdjOROW2wWMXy_iXCd-CiGs9Nr8uORJgDXDiEalar7YwjJ8o1F-mT57QXhnzWwfcUsKWlQo7ZbZVd6shtd0B6jBeBuatYyQmiCH_DshpCYT8BesBOgD-61DMuFYjOjxeFMtdCvigGEcteW2MKM5KRnvOyNamBMFWoRPWIYY1VdqYtS_CEXlJQd7UhLkePx1LnY-BIfyLwLK7XwJ4tNcmfuBFpsZ7dzkgMJ1XIGqT4Y7VSFDZKcrlT80YCfI7uciLFQW3znDGnzMvJKJAP7_30kB3lqzz7bItQ7nxhhc-UxsFHFE41SwR7GD2jYeIsBt4o21rHB3o-AKRpM6Ksu7B5zMkGSDtkIiFHX1zfeB451g7OTXTHN5pu5v9uqLxLYoJQyE9eFql_ne4aQAii791E8GK8ji1CWvLxp0BAidtwhJ49L5X4H9VqOdg-A-UszDLcOpPFFTtY4tYk4-1erb5ZmbUfNvGv4nPZViqSd40kGxH2ESEvaq01RlDOe7dMMOh3nsP_DHqd7L2dc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a3d37ce.mp4?token=QglUtHr2fD12_ouOYZUMCDIVB1hrVd13LyPP7xh_7LB7XfDE06hf--JoCJb4wV9BwpQiCVjTrwyaver09W91_rZb05pZfB_v_vhfR30Ceo4hYk0DSyzhidh-R0TF1sjG7LGqklonTZcJdhwRJdT53bRB3wQUwdjOROW2wWMXy_iXCd-CiGs9Nr8uORJgDXDiEalar7YwjJ8o1F-mT57QXhnzWwfcUsKWlQo7ZbZVd6shtd0B6jBeBuatYyQmiCH_DshpCYT8BesBOgD-61DMuFYjOjxeFMtdCvigGEcteW2MKM5KRnvOyNamBMFWoRPWIYY1VdqYtS_CEXlJQd7UhLkePx1LnY-BIfyLwLK7XwJ4tNcmfuBFpsZ7dzkgMJ1XIGqT4Y7VSFDZKcrlT80YCfI7uciLFQW3znDGnzMvJKJAP7_30kB3lqzz7bItQ7nxhhc-UxsFHFE41SwR7GD2jYeIsBt4o21rHB3o-AKRpM6Ksu7B5zMkGSDtkIiFHX1zfeB451g7OTXTHN5pu5v9uqLxLYoJQyE9eFql_ne4aQAii791E8GK8ji1CWvLxp0BAidtwhJ49L5X4H9VqOdg-A-UszDLcOpPFFTtY4tYk4-1erb5ZmbUfNvGv4nPZViqSd40kGxH2ESEvaq01RlDOe7dMMOh3nsP_DHqd7L2dc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/15197" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15196">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15196" target="_blank">📅 00:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15195">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15195" target="_blank">📅 00:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ: ظرف ۴۸ ساعت آینده توافق با ایران امضا خواهد شد و احتمالا برای مدتی ارتش رو در خلیج فارس نگه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/15194" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">@withyashar
Reeee</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/15193" target="_blank">📅 23:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15191">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مجری شبکه خبر : چرا ایران در روز آخر مذاکره حمله به اسرائیل را متوقف کرد؟
قالیباف: ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد.
قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/15191" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15190" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
