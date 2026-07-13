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
<img src="https://cdn4.telesco.pe/file/psBNEYzGOhjKhtYICya7om-37gmzpbKANDXURoXRMeFfAEZF2YOyKiQNskRRB4_DMW3dHM6vEMbfUKP4ti3bVJdJ-FeKkP6vyipk4cSN8f-aNGSliXYFSCoR5NxhUoMff5U57Tf5jc6G_llnDMhts9NA88gBmDt-ut89zdeerCs8uAkSA9foawYYgmMNxLBW98nHK5lg1zZ9HqhFNqkZxbD9UhBgRwkh3gw6BuIrsZdEapD1hzgV9hg5ccQDP-a5qr8mHI-3xv7DfWK_-R7NO0ve59edjAjSq9BFQ7F2MhkhKPp7CmXb6u_urgd-lEatSsNgbiBEoZ-AAnmMXcP0_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 380K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-17829">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک منبع آمریکایی در شبکه خبری "i24NEWS" اسرائیل:
هم‌اکنون، هماهنگی‌ها و آمادگی‌های نهایی برای اعمال مجدد تحریم‌های دریایی علیه ایران در جریان است و انتظار می‌رود که به زودی در این مورد اعلامیه صادر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/17829" target="_blank">📅 19:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17828">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">(تایید نشده) ترامپ: امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/17828" target="_blank">📅 19:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17826">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vn1SPOKRJowoH5q3em286cE4yvX5zA-N6UkpKlM3TL8HT_D3rkVV5xmFOZRIpoSBUTFl91MLKA7iuNAMrmZoCF2dpu1yXlI9szU86JE6ZInsSqxOTIUZh_whSm3kJgg-ayfWXMzUHvqBV738DMnkCLyUVGrpds-QjGDXSBk5zU_l-bBlzoz8B2iRrUYJb_pHelp7A7YY2jE1Ofqda56g1P_w4LllbPXAtGoGQshGy-4BXItxnFn3bFx2P9J6lUucaG7rtZhDfgocje575SOjPZX8MGRLWAzkPSUVCYY_4rmZkyJEmNnyK07YcYgYO_Tm__PAwOJ8ZaMMVHmTZ45QmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJDYQ5UsKQl-nShx7Ejhflo3PhZpaULbUyF875kAPpdGG3apYaocjqS0zFVYu_eLy9Qf0Pjf5caPdvQ7SMIMmaW9Fbd4L7AikqA-6_awG6gklBFG4zsJWQn9M3N3llwhIGVg2ZxlJd4emdjWBJ260i8Dj_0HkADiKCv63Gs-CGnE-YD7NTXQ00_XLEgOgh15SJrVBXmtjIcS138AkRGjipJkQpA_aQKVx0G3Q5G7Jjpac0YBqUxmf12fXCExkddktT50p05-MaLxtvAoqoM8kxNZM58pfXbifTbFqkjy3_pCG4XBrauhoFGjfE_ILqMFoYa2mbCZLuS9Q4rXCyVUPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مرد که یک سلاح حمل می‌کرد، توسط پلیس ساختمان کنگره آمریکا در بخش شمالی، خارج از ساختمان، دستگیر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/17826" target="_blank">📅 19:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17825">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue-qXn4yjVAvK4NJ8qrMgeo3EspSy1LEwEOhShYo_mD_7KpErsJbiXEPIkc3QNQy7xgcQzDQmQ1ap831oYcxUPLPh9ofBDahlG-kSt5rPCf4aqU1JbWIN_sj6OUY9jq-5h7elgy4aPPTU2Ke22nAScENtt-M4hzqcfvBohKXNDtXs5DkFhnpI3l4Ojfcd-PMDNm4-pczYuwSqPtDt-WT6yFBShrD9Tet2MH5mhmvM4jt8OjXGtGQbD8X4xx-2aHSyFJpYhULuUdlcSHI72orOBae8Ns8mZlZxW6C6bYn6Gh_1jSzKCY2uhHC8glWmmPLlFZm4Zq-TX1ATqjRojZ1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای دیگر ماهان‌ایر ایران در حال پرواز به سوی یمن  @withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/17825" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17824">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سلیمی، نماینده مجلس: تنگه باب‌المندب به‌زودی بسته میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/17824" target="_blank">📅 19:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17823">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6865d289ab.mp4?token=GzZMkmGC-qAhmNG4pZX0fQDEEwEZej396x9VNuC2e8bxxNojkkk9u7j-v46PsJg0BKMZpkQXdR16SpV2IlfmPMv8nH9-fpnaIIn1q55xhIh8sxQeWMSyrnLGaYyi1b-Yqk5iSpc9DMRYNnpyDC13daLT7x9zd7uGsuTDgV_EnsJMdcBFk6sMGX7zJW3pSvsU9Nv2ToMZq-c-BERt_C4DxBkLKkDEohAX969HqH-is9qlx7zBQcoHL6azX-Le0ApHosRedGH_EbuGVqVG7s6k0K1AYVgzrYe1DwPz7izM4a8cuprxXZbA5ZqFgpBHZas8NbaoNEmwLHxEznZx8SSJ6wjZGP_PuZlc2b-i6dottAoWFdNbXQtpfsolGptGshmnf0IOF3F9rXMTYgjuSSgON0AjUi-rY3V4n67Q21Rcb61yWo7oXCmJGz3Q7Je_hhjAyqg0MjiiDuC6kobvI_LxYxVcKPaHaNB1zw7ZplJIJevH5R-9U2HPg0rF5kjjBX8ZTIZ3aK-CiIXV9pY2zd5crOGfc7MaSM7m4eK7HYkp5u3erElMYaQLmKyDMKkrx50hb9nkpDMfX-sLtWeXOdrgf7GMiaQio-5K9Aw3u69AwK5CqLnCC_Az_BBm8gSWg6B8fIeq8Mvd3fkzWZYJpS5wQSw7cPwWEH1UEBrdWJZpTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6865d289ab.mp4?token=GzZMkmGC-qAhmNG4pZX0fQDEEwEZej396x9VNuC2e8bxxNojkkk9u7j-v46PsJg0BKMZpkQXdR16SpV2IlfmPMv8nH9-fpnaIIn1q55xhIh8sxQeWMSyrnLGaYyi1b-Yqk5iSpc9DMRYNnpyDC13daLT7x9zd7uGsuTDgV_EnsJMdcBFk6sMGX7zJW3pSvsU9Nv2ToMZq-c-BERt_C4DxBkLKkDEohAX969HqH-is9qlx7zBQcoHL6azX-Le0ApHosRedGH_EbuGVqVG7s6k0K1AYVgzrYe1DwPz7izM4a8cuprxXZbA5ZqFgpBHZas8NbaoNEmwLHxEznZx8SSJ6wjZGP_PuZlc2b-i6dottAoWFdNbXQtpfsolGptGshmnf0IOF3F9rXMTYgjuSSgON0AjUi-rY3V4n67Q21Rcb61yWo7oXCmJGz3Q7Je_hhjAyqg0MjiiDuC6kobvI_LxYxVcKPaHaNB1zw7ZplJIJevH5R-9U2HPg0rF5kjjBX8ZTIZ3aK-CiIXV9pY2zd5crOGfc7MaSM7m4eK7HYkp5u3erElMYaQLmKyDMKkrx50hb9nkpDMfX-sLtWeXOdrgf7GMiaQio-5K9Aw3u69AwK5CqLnCC_Az_BBm8gSWg6B8fIeq8Mvd3fkzWZYJpS5wQSw7cPwWEH1UEBrdWJZpTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: اواخر امروز محاصره دریایی ایران را آغاز خواهیم کرد @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/17823" target="_blank">📅 19:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17822">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سنتکام: اواخر امروز محاصره دریایی ایران را آغاز خواهیم کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/17822" target="_blank">📅 19:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17821">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:
وزارت دادگستری آمریکا و پنتاگون یک کارگروه مشترک تشکیل داده‌اند تا افشای غیرمجاز اطلاعات محرمانه به رسانه‌ها را بررسی کرده و عاملان آن را تحت پیگرد قانونی قرار دهند
@WarRoom</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/17821" target="_blank">📅 19:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17820">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS 💓M💓</strong></div>
<div class="tg-text">چرا من کامنتی که زیر پست ترامپ گذاشتی اشکم در اومد
هر چقدر هم که واقعا عاجز شدیم از این زندگی وقتی تلاش های شما رو  به عنوان هم وطن میبینم لذت میبرم و ازتون ممنونم کاش همه با هم متحد باشیم</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/17820" target="_blank">📅 18:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJNj6dJmXAQouek-GZ3GZzgj0zDmdN2pb82D7_1UwCP88nyO36oIlGBll0gShGMncJWhe6Izeu7lG30uWv_71thvYC0J23II0nq-XJIPghH08M3v53TR3sYIvLiCFI7_8SbVFhuEFsahR8XP9eoYBUp1V4KRH60yynto2rHX4ty7EgB8Kvo9bVIyUVcYuEguaccKpohCH-1oHqT_SWSyDU3cqM-G3wBZXq-YwoD8hkswayUlDJDpYsL30bLK0En18B7SvwbqW9BsrT6CmTGyFtXwKSxF_6kwrLzUK-kRUtPSo30tyEpHzVQSBAjp8EYjy3uT80-4LVkeSa4TDVDKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کن وارد اسکله نیرو دریایی باهنر  شده اینا نفهمیدن
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/17819" target="_blank">📅 18:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17818">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اکسیوس: یک منبع ارشد در خلیج فارس گفت که آمریکا موضوع احتمال دریافت عوارض برای تأمین امنیت تنگه هرمز را با متحدان خود در منطقه مطرح نکرده بود
@WarRoom</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/17818" target="_blank">📅 18:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17817">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طرح جدید ترامپ؛ ۱۵ دلار بر هر بشکه نفت در تنگه هرمز
خاویر بلاس، ستون‌نویس بلومبرگ:
ترامپ از بازگرداندن محاصره دریایی علیه ایران خبر داده است؛ طبق این گزارش، واشنگتن قصد دارد برای تضمین باز ماندن تنگه هرمز، عوارضی ۲۰ درصدی از تمام محموله‌های عبوری دریافت کند که این رقم در برآورد اولیه معادل ۱۵ دلار برای هر بشکه نفت خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/17817" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17816">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de05ae188.mp4?token=N3PLO0wdR4106ooePjQNxMx3dc4tuxUWFg5MysZYjDTAWH6rUMZNTxTc_tBMnRo4Us6fyj0Zn6LIHGoin-Fw3yNDCttVwqKiX333kzJc6R3KnCjS2G7AWq95a3yWYFJw-aBHAIC8xQaH54CSaK6AgqtwLXqdUqkic6aj-gj0jQLFpoiEQHcdEwTPsjnZRncK8Cl1WhiLFbE6DkU3tx_A39gjr5cCVKVCdK9cjIJIsmAKcX2Gg_nEUSw8TlFjbN1eeXnwopH5QzMKwQ7D4rIRjZgkBnWkqkQ7DCVlXhBzBi-mJtB88KiDICkjVAxpC_CAIiYJJ9SrSebclD9FX68zoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de05ae188.mp4?token=N3PLO0wdR4106ooePjQNxMx3dc4tuxUWFg5MysZYjDTAWH6rUMZNTxTc_tBMnRo4Us6fyj0Zn6LIHGoin-Fw3yNDCttVwqKiX333kzJc6R3KnCjS2G7AWq95a3yWYFJw-aBHAIC8xQaH54CSaK6AgqtwLXqdUqkic6aj-gj0jQLFpoiEQHcdEwTPsjnZRncK8Cl1WhiLFbE6DkU3tx_A39gjr5cCVKVCdK9cjIJIsmAKcX2Gg_nEUSw8TlFjbN1eeXnwopH5QzMKwQ7D4rIRjZgkBnWkqkQ7DCVlXhBzBi-mJtB88KiDICkjVAxpC_CAIiYJJ9SrSebclD9FX68zoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنت‌کام: دیروز، نیروهای فرماندهی مرکزی آمریکا (CENTCOM) با استفاده از چندین شناور انتحاری بدون‌سرنشین، یک مرکز تعمیر و نگهداری زیردریایی‌ها و شناورهای نظامی ایران را با موفقیت هدف قرار دادند.
سه شناور بدون‌سرنشین سطحی Corsair به تأسیسات بندر پایگاه دریایی بندرعباس اصابت کردند؛ این نخستین بار است که نیروهای آمریکایی از شناورهای بدون‌سرنشین دریایی در عملیات رزمی استفاده می‌کنند.
به گفته سنتکام، حملات شب گذشته توانایی ایران برای ادامه حمله به کشتی‌های تجاری را کاهش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/17816" target="_blank">📅 18:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17815">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByHdt8NsDscd-iLu9Sgs35aNdnWGtgK0phX8n2PLfTRfE92qeLZaPT7wBE1SDt3x6oJvgRFteJ8ejITh2qrDlb60b_mz_rs01o5d24WUSXTc55R1-o_rt0MN6vwIRWHQyT6FLiEBd7eUvb-S2J2IFpp9A6nMWTCOUH6SPRJd7-LVIdL73EmVC5rYeYqhqk_HHsBYHPCtuydCpVbAFHd0UxNNkme6nJkCqxNxwaAq3mnYCb8AlK8swgnx9aoe36tEazNC82SwdGeeOb9VSvERTBEKz-fY2VIz-UEJBY1-eJRCAlNim6sgHK1cLdlMz3lcWFTaL16dKO2ezwJRNR3sVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
:به فرماندار هنری مک‌مستر پیشنهاد دادم که دارلین گراهام، خواهر فوق‌العاده لیندزی گراهام، را به‌عنوان سناتور موقت ایالت کارولینای جنوبی منصوب کند.
این بهترین ادای احترام به لیندزی خواهد بود؛ کسی که عشق و علاقه زیادی به خواهرش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/17815" target="_blank">📅 18:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، فقط فقط همین کامنت را لایک و اد استوری کنید. ترجمه در چنل تلگرام.
https://www.instagram.com/p/DavJyXLhhos/?carousel_share_child_media_id=3940411242254309932_347696668&comment_id=18112905515304028
ترجمه :
،
بسیاری از ایرانیان باور دارند که صلح و ثبات پایدار تنها پس از پایان یافتن حکومت فعلی امکان‌پذیر خواهد بود. در حالی که شما تصمیمات خود را اتخاذ می‌کنید، با احترام از شما می‌خواهیم چند نکته را در نظر داشته باشید:
مردم ایران گرسنه نیستند (لطفاً ویدیوی آبدانان  را مشاهده کنید).
بسیاری از ایرانیان از شاهزاده رضا پهلوی به‌عنوان چهره‌ای وحدت‌بخش برای یک گذار مسالمت‌آمیز حمایت می‌کنند.
بزرگ‌ترین اولویت ملی ما، داشتن ایرانی آزاد، دموکراتیک و دارای تمامیت ارضی است. حتی یک وجب از خاک میهن ما نباید هرگز مورد مصالحه قرار گیرد.
لطفاً به این حکومت کمک مالی یا توافق‌هایی ارائه نکنید که جایگاه آن را تقویت کند.
اگر محدودیت‌های دریایی یا محاصره دریایی اجرا می‌شود، با احترام درخواست می‌کنیم که این اقدامات با بالاترین سطح قاطعیت و جدیت اعمال شوند تا کاملاً مؤثر باشند و هیچ راهی برای دور زدن یا بی‌اثر کردن آن‌ها توسط این حکومت باقی نماند.
از توجه مستمر شما به مردم ایران سپاسگزاریم. ما همچنان به آینده‌ای بهتر امیدواریم و از تلاش‌ها و حمایت‌های شما قدردانی می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/17814" target="_blank">📅 18:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17813">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRKf3V5inaMbKqAa-RdpIGgv6h5c0OU9wkQyuIiydodfVbxdG0qHu-kpw6AkPzIP8YI48xDkqjlkoycPSyGZrw5vl8F6_YAoGmkMKS29Pr4fPjDJ2w06ikNds-KMms-txamC4PwJuyBUYCsc1npump3YPizWFRVDsp7NM5vwIBG638IrcTNqnMi733M6xrwuieU4GOTqRq6Ol3h1-JVsXnP0KH5L6bt0VCzAz_QPVqgYTOgPAaK_-5-gOBXzFs8J6euM6YCkckP2mLe1tT4QcWC7gpYk2U5uuZNfHHv7mSmcB-9Qs9ZBbLnHISdsmcudhmJqjxx7MKtP8RYNNa9-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : تنگه هرمز
باز است و باز خواهد ماند، با ایران یا بدون ایران.
ما در حال بازگرداندن
«محاصره
دریایی ایران»
هستیم؛ این نام به این دلیل انتخاب شده که این اقدام فقط کشتی‌های ایران یا مشتریان ایران را از ورود یا خروج متوقف می‌کند. همه کشورهای دیگر همچنان استفاده‌ای منصفانه و آزاد از این تنگه خواهند داشت.
ایالات متحده آمریکا از این پس به عنوان
«نگهبان تنگه هرمز»
شناخته خواهد شد؛ اما به‌عنوان بخشی از این مسئولیت و از نظر رعایت
عدالت و انصاف
، هزینه‌های لازم برای انجام وظیفه تأمین ایمنی و امنیت این بخش بسیار بی‌ثبات جهان، با دریافت
۲۰ درصد از ارزش تمام محموله‌هایی که از این مسیر حمل می‌شوند
جبران خواهد شد.
فرآیند اجرا و تشکیل این سازوکار
فوراً آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17813" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17812">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: محاصره ایران را دوباره برقرار خواهیم کرد
ترامپ مدعی شد:
تنگه هرمز چه با حضور ایران و چه بدون آن، باز است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17812" target="_blank">📅 17:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17811">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ، محاصره دریایی ایران را از سر می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17811" target="_blank">📅 17:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17810">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17810" target="_blank">📅 17:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17809">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV-zAk-RwWSweDI5Re3_He9R8mv2LGgDpjl2JJXgGaoZoMhX2f8hIRUa5ZEkPGCwTOagGFeIV-QQYUKpApVikzWQkMlfDh8gcRGMkpxZ_a59dP3dAC48eBgJNOvz9ELyKEdXQb6qdlVm3ha2M2LAXtMAMCm-a6cbBIGkWCkOY6PgOBrCIgcHqpVAPMLJK-KHyK-oLQGLIKKcgndWea2Mu_wM6FKHgVKSmENlj5o1RKvW94XedLk9ZO1qQOkf6NsXQssCBFUWxjV6q4kQEgQoFqJe3_XLFSSjFy1xKYH5pookR5e3hzZ6l5oSQStNolEgTyYT3wlilrx5wQXGpsxzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان دزفول
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17809" target="_blank">📅 17:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17808">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی قرارگاه خاتم‌الانبیا:
نمی‌گذاریم آمریکا در تنگه هرمز دخالت کند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17808" target="_blank">📅 16:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17807">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e7483b64e.mp4?token=WE75SUPI9lDUe6KNEnsY3hbQn3GwwUege8ZJTq8tg4MjZ_SOR2EVaf5XhVdYWsPAYyApUFWVbJaLvJZLPbY9_FoLJo8YUQDUEujmeT2mz-9tibLjuJkhemWZWUdSPXcf7hfaVfz6DwdRcw913zsA3sezFRedZVDKfkvTnfkVVHWf568wpCybfJk4MWjc71ogQpXvPU7RiQCQlpRsEsMwq4oRfdjv_JoZLkRmYqZ4SPe-_IXAA-NuoTwaOldOUMMuk6vlcvVtq7uMoO4Z_88fCEhP16fm-5PSqpWrNMGXNuNoFZ-ioBAgUbfiPSE1if7daEdIbccDurgEVXROuz5Q8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e7483b64e.mp4?token=WE75SUPI9lDUe6KNEnsY3hbQn3GwwUege8ZJTq8tg4MjZ_SOR2EVaf5XhVdYWsPAYyApUFWVbJaLvJZLPbY9_FoLJo8YUQDUEujmeT2mz-9tibLjuJkhemWZWUdSPXcf7hfaVfz6DwdRcw913zsA3sezFRedZVDKfkvTnfkVVHWf568wpCybfJk4MWjc71ogQpXvPU7RiQCQlpRsEsMwq4oRfdjv_JoZLkRmYqZ4SPe-_IXAA-NuoTwaOldOUMMuk6vlcvVtq7uMoO4Z_88fCEhP16fm-5PSqpWrNMGXNuNoFZ-ioBAgUbfiPSE1if7daEdIbccDurgEVXROuz5Q8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه بمباران فرودگاه صنعا توسط جنگنده‌های عربستان سعودی
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17807" target="_blank">📅 16:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17806">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ : نرخ تورم در ایران ۳۵۰ درصد است.
شش ماه پیش، این نرخ ۵ درصد بود
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17806" target="_blank">📅 16:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17805">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5be7caae.mp4?token=WdYzHj0wyqrGcghFontPd2xKJnyWXKuJCOj1T-QeqOOKGIE8tl9FPMz-Ifb5BEdtwsteFLXhA15Iwzt5MCRMQMoaPsLA1EpamXQYrntvJevfMPLJ7gIuUpFJ6yZKaAbSv0VR1tTVRepB6AgRWDrBI6Ek3-d5ZjcQ6r52N-sCPjBDxW1PSHNbiUrWMM2_orCv-DuaD7iVhdMb1jDR3Xu9oWytJgQ3AhUTYIlYnnLS_DlPFt3bpB8UeEoIRZTBwz8jgYSW9NTrQZCXSf64mqAxGi1IT18v9zsJSzFVF2KL5-M_Sc15iqkWlPXTiCLF_Ve12-7VEmY-krjyv58dhdWHdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5be7caae.mp4?token=WdYzHj0wyqrGcghFontPd2xKJnyWXKuJCOj1T-QeqOOKGIE8tl9FPMz-Ifb5BEdtwsteFLXhA15Iwzt5MCRMQMoaPsLA1EpamXQYrntvJevfMPLJ7gIuUpFJ6yZKaAbSv0VR1tTVRepB6AgRWDrBI6Ek3-d5ZjcQ6r52N-sCPjBDxW1PSHNbiUrWMM2_orCv-DuaD7iVhdMb1jDR3Xu9oWytJgQ3AhUTYIlYnnLS_DlPFt3bpB8UeEoIRZTBwz8jgYSW9NTrQZCXSf64mqAxGi1IT18v9zsJSzFVF2KL5-M_Sc15iqkWlPXTiCLF_Ve12-7VEmY-krjyv58dhdWHdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سیگنال سلیمانی داد امشب بد میزنه !!!!!!
من خمینی را کشتم، که یک ژنرال باهوش اما دیوانه بود.
نه ، سلیمانی دیوانه ‌رو من کشتم
سلیمانی یکی از خیلی خیلی بد ها بود
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17805" target="_blank">📅 16:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17804">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دونالد ترامپ درباره وضعیت مجتبی خامنه‌ای چه می‌داند؟
ترامپ: اکثر رهبران ایران کشته شدند. خامنه‌ای از بین رفت، و
پسرش ۹۰ درصد از بین رفت
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17804" target="_blank">📅 16:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17803">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a88ccf72.mp4?token=g09eaj3LRbjHdlvpArfi5rnBz2vxxJMhqlnvdaFVmhmwU8GMuLzQJG_weS6ftncgHhVEFFY9hcyE_b1ujNMlFMTufUVwECNDjfHRAdE4uM47eCxIayXLzH5xlUDdvNAEQx0jC659nkXvgvOUgCek-M1Io-NQriDIA5JGNxvmvqL5ThI0KJpLwPjQA75qK1mwUEsC6HOEOJJ7XKW2HexduGxGrKLR_ram2IjiWGoSdmKC-VV5rrehlfqF5JdDS3BvAwXMt2ao-aVikLQUees3gOvF7OJjKXK7DsYzKzhfTS-R4E6iaNQ0AIjM-SKoBtFxSg-hbtKazXlF90m_B500Boi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a88ccf72.mp4?token=g09eaj3LRbjHdlvpArfi5rnBz2vxxJMhqlnvdaFVmhmwU8GMuLzQJG_weS6ftncgHhVEFFY9hcyE_b1ujNMlFMTufUVwECNDjfHRAdE4uM47eCxIayXLzH5xlUDdvNAEQx0jC659nkXvgvOUgCek-M1Io-NQriDIA5JGNxvmvqL5ThI0KJpLwPjQA75qK1mwUEsC6HOEOJJ7XKW2HexduGxGrKLR_ram2IjiWGoSdmKC-VV5rrehlfqF5JdDS3BvAwXMt2ao-aVikLQUees3gOvF7OJjKXK7DsYzKzhfTS-R4E6iaNQ0AIjM-SKoBtFxSg-hbtKazXlF90m_B500Boi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  تنگه هرمز رو نگه می‌داریم و احتمالاً از این به بعد خودمون ادارش می‌کنیم؛ ما میشیم نگهبان تنگه و وقتی این کار رو انجام بدیم، هزینه‌ش رو هم از بقیه می‌گیریم. 50 سال از تنگه محافظت کردیم و هیچ پولی نگرفتیم، مفت و مجانی نگهبانی دادیم، ولی این بار قراره…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17803" target="_blank">📅 16:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17802">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای ترامپ: ما دیروز یک نشست ۱۱ ساعته با ایرانی‌ها برگزار کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17802" target="_blank">📅 16:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17801">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:  تنگه هرمز رو نگه می‌داریم و احتمالاً از این به بعد خودمون ادارش می‌کنیم؛ ما میشیم نگهبان تنگه و وقتی این کار رو انجام بدیم، هزینه‌ش رو هم از بقیه می‌گیریم. 50 سال از تنگه محافظت کردیم و هیچ پولی نگرفتیم، مفت و مجانی نگهبانی دادیم، ولی این بار قراره…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17801" target="_blank">📅 16:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17800">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ تلفنی به فاکس نیوز :هر بار که ایران پهپاد فرستاد، ما آنها را خیلی بد زدیم. آنها تاوانش را پرداخت خواهند کرد. @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17800" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17799">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">@WarRoom
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17799" target="_blank">📅 16:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600234548c.mp4?token=p65KDTZujBwbuu6PQJJuuM0mswlLFZhRSeNrOdY7KBak0SQWI0DO74aUz2wnEh-ui4PC0mhzFOSXbE8K3Fj8lC33S0w7tWE5IswZ6c_fH7dZxg-0BAyy0Ba8VcXDAs7Qg6Xzg5aGd8U1tkJXLPxiauTJ2kctXCohlqYjgm8cF2wwUd6IjyCdn62g_erdHYKwX2ZucTWj8cMDA7DSVBXmovPPjxmykRehxj9c2c5SYwiuQwZl9aCoDygeoCZqVCfEHt01mDDJIq3mkhM9MgU4sY2UZIK6KhHzSAdH6h0PTdr1WCKPnEbKOygAMUbL_Km6fT9MsYXbuTGUsi3PGRTjDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600234548c.mp4?token=p65KDTZujBwbuu6PQJJuuM0mswlLFZhRSeNrOdY7KBak0SQWI0DO74aUz2wnEh-ui4PC0mhzFOSXbE8K3Fj8lC33S0w7tWE5IswZ6c_fH7dZxg-0BAyy0Ba8VcXDAs7Qg6Xzg5aGd8U1tkJXLPxiauTJ2kctXCohlqYjgm8cF2wwUd6IjyCdn62g_erdHYKwX2ZucTWj8cMDA7DSVBXmovPPjxmykRehxj9c2c5SYwiuQwZl9aCoDygeoCZqVCfEHt01mDDJIq3mkhM9MgU4sY2UZIK6KhHzSAdH6h0PTdr1WCKPnEbKOygAMUbL_Km6fT9MsYXbuTGUsi3PGRTjDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ تلفنی به فاکس نیوز :هر بار که ایران پهپاد فرستاد، ما آنها را خیلی بد زدیم. آنها تاوانش را پرداخت خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17798" target="_blank">📅 16:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: ایران مجموعه‌ای از « افراد بد
»
است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17797" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ: ایالات متحده قصد دارد حملات جدی علیه ایران انجام دهد
ترامپ: ایران از من چیزی(پولی)دریافت نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17796" target="_blank">📅 15:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسکای نیوز : دولت بریتانیا، سپاه پاسداران انقلاب اسلامی (IRGC) را به عنوان یک سازمان تروریستی معرفی کرد.  @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17795" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: ما یک توافق داشتیم، و آن‌ها آن را نقض کردند
ما عوارضی را برای اسکورت کشتی‌ها در تنگه هرمز دریافت خواهیم کرد
ترامپ: شب گذشته به ایران ضربه بسیار سنگینی وارد کردیم.
@warroom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17794" target="_blank">📅 15:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: رهبران ایران مذاکره‌کنندگان حرفه‌ای هستند
ما کنترل تنگه هرمز را در دست خواهیم گرفت
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17793" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هواپیمای ایرانی در فرودگاه حدیده یمن فرود آمد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17792" target="_blank">📅 15:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یوزرنیم «اتاق جنگ» در تلگرام مال ما شد
@warroom
We’ve secured the “
@WarRoom
” username on Telegram.</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17791" target="_blank">📅 15:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تبریک نمیگین به چنل ؟!!!!! یه تغییری‌ کرده
😋</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17790" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هاآرتص:  ایران در حال آماده شدن برای یک جنگ همه جانبه و تمام عیار است؛ بیش از یک میلیون نفر نیروی نظامی درحال آماده شدن برای جنگ زمینی هستند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17789" target="_blank">📅 15:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17788">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo5JMSst7XnMhP4v42BJ7Lg6EKR5x0kPBo8X39WR7EKGDfcaVjR4sRt50DlOx5D2ZRY3Ruw3Ioh7jE_aJSLjRU89tZpt61-0j1LOwLJXDu4xheGveyDzLlhC-GTohNABCZ8Ajr1zm-UDSEUt3fmg7q1cELo8AxtbQda_G-ExeWB50kKU_ySrbDTGnukUErbXr_ljytAVBNKuIXe8-Q0rjyxctjQst2le9wrS0TG2AF5paXaDANhIw2PhBwpjh4xi7AsFd1ruBcbNdiVF_Fkt7H6NTEVfverRruNpIyjo8LVzvHj_NYcouR-uumhk5kcgQ6hZCFUOqEqqU7e_isoJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان UKMTO گزارشی درباره وقوع یک حادثه در فاصله ۵۰ مایل دریایی (NM) در جنوب عدن، یمن دریافت کرده است.
یک نفت‌کش که در کریدور ترانزیت بین‌المللی توصیه‌شده (IRTC) به سمت شرق در حال حرکت بود، گزارش داده است که ۶ قایق کوچک از سمت راست کشتی (starboard) به آن نزدیک شده‌اند. یکی از قایق‌های کوچک تا فاصله ۵ کابل (حدود نیم مایل دریایی) نزدیک شده و تیم امنیت مسلح مستقر در کشتی (AST)، اقدام به شلیک تیر هوایی کرده است. ۵ قایق کوچک دیگر در فاصله ۱ مایل دریایی (NM) باقی مانده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17788" target="_blank">📅 15:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه ندید افشاگری زم رو برید ببینید حتما ، دقت کنید این حرف ها مال ۸ سال پیشه !!!!!</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17787" target="_blank">📅 15:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17786">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتاق جنگ با یاشار : آیا بسته شدن باب‌المندب در راه است ؟!
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17786" target="_blank">📅 15:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17785">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت امور خارجه تروریست های حوثی‌ها در یمن اعلام کرد که «رژیم سعودی اعلام جنگ کرده است - و باید مسئولیت کامل آن را بر عهده بگیرد.» همچنین اظهار داشت که «رژیم سعودی در چند سال گذشته برای افزایش محاصره و به راه انداختن یک جنگ اقتصادی فراگیر تلاش کرده است، در تلاشی برای به بردگی کشیدن مردم یمن در خدمت صهیونیست‌هاست»
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17785" target="_blank">📅 15:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17784">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیروهای مسلح یمنی مورد حمایت عربستان سعودی: باند فرودگاه صنعا را هدف قرار دادیم تا از فرود هواپیمای ایرانی جلوگیری کنیم
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17784" target="_blank">📅 14:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17783">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسکای نیوز : دولت بریتانیا، سپاه پاسداران انقلاب اسلامی (IRGC) را به عنوان یک سازمان تروریستی معرفی کرد.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17783" target="_blank">📅 14:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17782">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17782" target="_blank">📅 14:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17781">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">افشاگری ۸ سال پیش زم @withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17781" target="_blank">📅 14:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش تکان‌دهنده در نیویورک تایمز:
بر اساس این گزارش، احمدی‌نژاد در اوایل سال 2024 برای مذاکرات سری در بوداپست، پایتخت مجارستان، با مقامات اطلاعاتی اسرائیل دعوت شد. او به بهانه‌ی یک کنفرانس علمی به آنجا فراخوانده شد و طبق گزارش، دو بار در سال‌های 2024 و 2025 با مقامات موساد دیدار کرد. منابع آمریکایی و ایرانی به این روزنامه گفتند: "این بخشی از یک تلاش چند ساله اسرائیل برای پرورش احمدی‌نژاد به عنوان یک دارایی اطلاعاتی است، که در زمان مناسب، بتواند به رهبر جدید ایران منصوب شود." این در حالی است که احمدی‌نژاد، در دوران ریاست جمهوری خود، برنامه هسته‌ای ایران را تسریع کرد، خواستار نابودی اسرائیل شد و انکار هولوکاست را مطرح کرد.
در سال 2024، حتی ددی بارنع، رئیس موساد، شخصاً به مجارستان سفر کرد تا با احمدی‌نژاد ملاقات کند. موساد، این جلسات را به سازمان سیا (CIA) آمریکا اطلاع داد.
بر اساس گزارش، اسرائیل به طور پنهانی مبالغی را به احمدی‌نژاد پرداخت کرد و مقامات اطلاعاتی اسرائیل در چندین نوبت با او دیدار کردند.
این تلاش‌ها در اواخر فوریه امسال، در روزهای اول عملیات "غرش شیر"، به اوج خود رسید، زمانی که یک عملیات جسورانه برای انتقال احمدی‌نژاد به یک مرکز امن موساد، به عنوان بخشی از طرح سرنگونی رژیم، اجرا شد. این طرح شکست خورد.
در 28 فوریه، روز آغاز عملیات، یک حمله هوایی اسرائیل به محوطه اطراف خانه‌ی احمدی‌نژاد انجام شد و هدف آن ساختمان‌هایی بود که محافظان و خودروی زرهی او در آن قرار داشتند. پس از حمله، یک خودروی پژو مشکی به محل رسید و او را به سرعت از صحنه حادثه خارج کرد. رانندگان این خودرو، ماموران موساد بودند که احمدی‌نژاد را به یک خانه امن و مخفی در ایران منتقل کردند. با این حال، احمدی‌نژاد که از این عملیات نجات به وحشت افتاده بود، تصمیم گرفت خانه امن موساد را ترک کند، اما جزئیات این اتفاق هنوز مشخص نیست.
موساد به درخواست نیویورک تایمز برای اظهار نظر، پاسخی نداد.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17779" target="_blank">📅 14:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک هواپیمای دیگر ماهان‌ایر ایران در حال پرواز به سوی یمن  @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17778" target="_blank">📅 14:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg0N5HJam4CxR18NO7GcyuvWNcFbbDjtENLzLhKxUgRRiHDMCEFetla2F2KiUbCR_x6C6MZmMAj5X1AgyMa1Xg0y9-XfwQsNTpzv6dDY8XptcLFrk2UVSrqLYku7TvZrwUm98w3NJ6rskL4k0YhCqJw9xPBbEFa36z72mO8ZNrhB0eH5Ur8sZuJV7u_004ehVzrhcOMPbl7-5MtZN00gJLf9a4UCXMBj3ttC10PSOIb8uhaY-xRTRzpEFuLFR-d4dRglal40p5a1wBu_MrR2VTOSJ1kg6kwb5ce6N57bvMnNPHygm6sYfuVQiYfaKD6zDzcmaFG9L4uVXzwdC4nlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود یاشار
۴ انفجار هم‌اکنون در پایگاه موشکی چمران جم بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17777" target="_blank">📅 14:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga8mWO4XLM3m8_QR3LZzMLLDQuLMJL0GngwECE1-uLjXA1MOsgIc0lwTQLRvfVxFeGlH7lz-8Md9mv0kILA0Kgg4ibnpuIdDbJrk37pPSa-BlMuLbh0gqN6Xiov9YhHihYVSM4ojdvl-p0zq36jfsWGngy4gFwpvFPtNsssJqPThEGmmLjjg2eVNc6V3WE6naQE8Xd2z_7Bf2iNFwJbkQ0X5nz-qKG0ZEaVTfoqkaLtwmxDCMpe_4hDnGxxgVqKTH9ywiGeahf7rGMDqu-lnNUx0EaIhxsycsAiPiZYX7Lov1lcCBF9_XfcjjHjKigDpwQqxLEY2kmz4drL0o1WinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای دیگر ماهان‌ایر ایران در حال پرواز به سوی یمن
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17776" target="_blank">📅 14:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e8ca3a0a.mp4?token=MpvOMm-wSlhcfRqC_jI1RbFRaOCPGmJWd9rRM-lyLetmyngIQlsmB5WWdsV_1j4YFmytqbaWYKRogwPQ6BAEx1-AnKcnrmzyWc1DrCsW1ilsZEviqfCvvQBXn31lucDmiYQUqPXmLbw-K6dUK-uJjiJyuB3pBXr6CBh8my5nSow8ZloCq2f0HF8-c3a380U7Sm9dVOLQeVRp2PDnUDOmaqzbOiS-cs-GlxjKqW_MsWthCFXiILikPrJkslkcQ7Da2Mzk2-Jq4ozjlp6jCk_kMBYEN6ob4VA-Kawm_sCaQAuz54D7SshtbJ2r8BzMDmFaaYqJznul3wmeWdtG86hsGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e8ca3a0a.mp4?token=MpvOMm-wSlhcfRqC_jI1RbFRaOCPGmJWd9rRM-lyLetmyngIQlsmB5WWdsV_1j4YFmytqbaWYKRogwPQ6BAEx1-AnKcnrmzyWc1DrCsW1ilsZEviqfCvvQBXn31lucDmiYQUqPXmLbw-K6dUK-uJjiJyuB3pBXr6CBh8my5nSow8ZloCq2f0HF8-c3a380U7Sm9dVOLQeVRp2PDnUDOmaqzbOiS-cs-GlxjKqW_MsWthCFXiILikPrJkslkcQ7Da2Mzk2-Jq4ozjlp6jCk_kMBYEN6ob4VA-Kawm_sCaQAuz54D7SshtbJ2r8BzMDmFaaYqJznul3wmeWdtG86hsGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت هوایی جنگنده ها آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17775" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17773">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rt1xIjIiyLX21VnOiEG0NrnQANLApVT8BnL8_1qMW1vzHbpS32XgdQixWBTfCT_JpDklsBkp6iLooX_Ghwoqt0e9sn-vGcI2OKtWuTxM6hRxeGQ20gAvFfDKwQ9TPrihtHZOqbDblMz7Y38oVrZlslM8NfZcHWn90KvKcc1-_uriBQG50SBpLsHwM_OhFKbNzW7xj3Wp5nW58_Mj5oSrl8k6_2W2bTuaoyUtahThXA5PgYBsUDlmP2WHNpH-Dl-X2hR0Sfw9fCP54Z0oiawACI1teucBUYPRHle6BU85E40H_wFw4PU52gziGW5ar9UiaOj5CU9sPp7USvxf8zULBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhslbFvosOyW63_qYOCprMirTZVMJ792w0XYJv6wWYUIZirUDqMh2rbjuzL_VMlqUA9tW0Mf34Vua4v99mlAfyoGAPysq0HWb2mA5IsORWdFrAKjVMRiCe-txznGzBnBxd6xDW9AAs--oufOlmuW2eqKl8sXqGPxVPASl_hxFRVqzaCEZPauD9wFbWIxmkur7NOAu4WA-doEjy5MHz1RRiyHghp5XsnbfxDkOBlXEcuRdOaWKQJ11T3a_7AkiYAfFioChLaeeOaDoJIMd_J4KL0J1OLviABIyd01MYsV7Oj8Cib5Er53UOxpLNlzmkYwfDGw5Hma1xiVB5KlHTMiPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتوبان تهران قم , انفجار بسیار شدید بعد از فرودگاه امام دودش تا ۲۰ کیلومتری قم هم پیداست
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17773" target="_blank">📅 14:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17772">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش زیاد از صدای انفجار آبادان
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17772" target="_blank">📅 14:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شلیک موشک‌های کروز از جزیرهٔ قشم به سوی کشتی‌ها و ناوهای جنگی آمریکا در تنگهٔ هرمز
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17771" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17770">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارسالی : سلام از زندان قزل الحصار پیام میدم همین الان ۵نفر رو بردن واسه اجرای حکم اعدام
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17770" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17769">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرده است که به‌زودی مقدمات ادغام پنتاگون و ارتش اسرائیل آغاز خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17769" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17768">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در آب‌های خلیج فارس و تنگهٔ هرمز درگیری رخ داده و صدای انفجارها ناشی از درگیری دریایی است
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17768" target="_blank">📅 13:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17767">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تنگه دعوا شدددددد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17767" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17766">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دقایقی قبل پایگاه شکاری بندرعباس مجددا مورد حمله سنگین قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17766" target="_blank">📅 12:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17765">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁮</strong></div>
<div class="tg-text">داشتن همه شنا میکردین دریا دیگه صدا زیاد گفتیم بریم خونه با خانواده خطر داره</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17765" target="_blank">📅 12:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17764">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi_sp</strong></div>
<div class="tg-text">بندر رو بد زدنننن یاشارررر</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17764" target="_blank">📅 12:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17763">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دستگاه قضایی عراق از توقیف املاک و کارخانه‌هایی به ارزش 69 میلیارد دینار در پرونده معاون وزیر نفت این کشور خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17763" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17762">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ارسالی از حدود ۲۵۰ پیام : سلام بندرعباس طرف پایگاه هوایی رو الان باز زدند. بعد از آتش بس بار اوله این وقت روز میزنن.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17762" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17761">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بندر عباس رو زدننن الان شدیدددد
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17761" target="_blank">📅 12:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17760">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">امروز  هم رفتیم امتحان دادیم...
به امید خدمت کردن و ساخت ایران فردا موشک هارو ستاره فرض کردیم.....
💫</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17760" target="_blank">📅 12:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک یگان از ارتش اسرائیل، همراه با دو بولدوزر، از "خط زرد" در نزدیکی اردوگاه باربره در منطقه الشقوق در شهر رفح عبور کرد و در حالی که به طور متناوب شلیک می‌کرد، عملیات تخریب با بولدوزر انجام میدهد
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17759" target="_blank">📅 12:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت امور خارجه ایران: صحبت‌هایی درباره درخواست ايران برای مذاکره، بخشی از جنگ روانی است که ایالات متحده انجام می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17758" target="_blank">📅 11:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17757" target="_blank">📅 11:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">استانداری اصفهان: در پی حمله آمریکا به یک پایگاه نظامی در محدوده شهرستان نایین، ۱ نفر شهید و ۷ نفر مجروح شدند
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17756" target="_blank">📅 11:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارسالی : سلام یاشار جان
دیشب پایگاه امام حسن کرمانشاه هم مورد اصابت قرار گرفته بود
دیشب صداش رو شنیدیم
خارج از شهره برای همین خبری پخش نشده فکر کنم
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17755" target="_blank">📅 11:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارسالی : یاشار جان آمار گرفتم بهبهان رو رادار ماغر رو زدن. یکم از بهبهان دوره و صداش توی شهر نمیاد
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17754" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیروهای اسرائیل هم اکنون شهرک حداثا در جنوب لبنان را هدف حمله قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17753" target="_blank">📅 10:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار سنگین دیشب در امیدیه @withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17752" target="_blank">📅 10:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش های از مشاهده پرواز موشکهای کروز تاماهاک از آسمان شاهین شهر در‌ ارتفاع پایین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17751" target="_blank">📅 10:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17750">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I13LqUqvpLtDut_sN3SujhES_CvtLt9Iix9Yzn6DN-fQozRfu0DfspzBc_QvoRfjf1sqsY3hrreHqwOBM59-pty7z-qNjjQfrM5ONBY9l0Mx4af2QpgH0N5FiRCj2MCjz6jDRHdozVKHj_9s1_cM8s-ksLO6Yb1skL98ThJtLL8isaUMc_vq6MPaLbB87zZ7JDjQZOzgfIWZ7taaS7Jrl8EHIJcJp7wyPYCp0c6SR1UtxEu-7wOZ5RaQ3lY4RHVLoLEIbhVR36qq_c8NT2i0PsnDLfTYf8m9XpnfmF2bSD6mjE4vTQ_cdA36JyJG_dZJkpEFTX1UyANE3_qLMJBzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار سنگین دیشب در امیدیه
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17750" target="_blank">📅 10:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17749">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f7f8cbe.mp4?token=c_KmZB3TTQQrWP_umqEkPYc_iqnVOwdzWTq1cLxocMgKcUGV-f3xTEKvekVJnaFo_6XZtc4xtO43TivCb88D4H_ugzejz14U3f-dZ8bm1WJb2Kvh5WnzPtisjMPu43mG-Vle0_t6edpJNGrU96mwIMRYRwFVhrWPRG_iP_S1nHE2yD6M24OYNVJVEhhvf6DY2ggCI9qnFYF4BsTqsuaEoK9LUHmIpebvrjW78W2OU6nIvhcMGDKuIT_d762OeALVH_mp2j5AE5DsjsFOj8kuGfBEbG-D0A2oHC-NijIxSTmpJ2O9wNsFsKm3R_lUxQXZByka_tjjOz81Q5TC2OFcqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f7f8cbe.mp4?token=c_KmZB3TTQQrWP_umqEkPYc_iqnVOwdzWTq1cLxocMgKcUGV-f3xTEKvekVJnaFo_6XZtc4xtO43TivCb88D4H_ugzejz14U3f-dZ8bm1WJb2Kvh5WnzPtisjMPu43mG-Vle0_t6edpJNGrU96mwIMRYRwFVhrWPRG_iP_S1nHE2yD6M24OYNVJVEhhvf6DY2ggCI9qnFYF4BsTqsuaEoK9LUHmIpebvrjW78W2OU6nIvhcMGDKuIT_d762OeALVH_mp2j5AE5DsjsFOj8kuGfBEbG-D0A2oHC-NijIxSTmpJ2O9wNsFsKm3R_lUxQXZByka_tjjOz81Q5TC2OFcqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : شلیک پهپاد شاهد (بهبهان)
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17749" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17747">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جمهوری اسلامی پهپاد شاهد داره میفرسته …
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17747" target="_blank">📅 10:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17746">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEdCLkewApN97dkruSgrTBHsNMGY4_8KGhrbGVgZoYfzr9BlwtsMcnk0BCk0u2bBzIvp5YDDvuQ-WE7MRkxdrUhj5VLLD8B9oM6bHg3K195NWjGox7UpQSI-zRpChvf151HqBZEFT0V40By8iaGs5Mo0G3PRDwP2XusdkKjPECTyelN_4K5-9JNAwRGgDL1Qza9rJupHBtD6y4Zjn910TFivFXGHsVK8nN6VYW-cBCH3NPbvYopisarMKAJJpkfWr4wvO_-L7cFvVKdOKyqhehFjUvI9FYVPcCnu4mYRjnUOa9snfxezHgqnyeXkT0pCX8df0yIVDoAgD9okDnYQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر کوهستانک , دیشب
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17746" target="_blank">📅 09:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17745">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSILusnItCbjYQW_2O2sXIb2M74fYGFKCcY3RvWo-BYo2wVM2Nl4CDyhNuofouaL7pcTqSOvANP3X3IJOW5dfKQiCG1citbaL5-JWCD8AwEVvIeJhUcDQLKXjZZleuLTV49Z-Kt_QFqYYiikBqX4TUvT5CUwsGP2woXnn4UZYR7vF6nEmquRmJ2DzZyb9jgCugOygRK1aUVfWMMFDW7QlMyhlmU39Hs0mDNct2HS03_j0lagXrLFp40zP_Xod5WZeqXOgw878MKOsWgDpeIbQ9dKclsDRLFW7P5rSl-arZRKkHsvXAWDSf_hb_XR3Dr7TeuYH4mw9BSDuAlTUWaIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17745" target="_blank">📅 09:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17744">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شرکت کپلر اعلام کرد روز یکشنبه تنها ۶ کشتی از تنگه هرمز عبور کردند که کمترین تعداد در پنج هفته اخیر است.
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17744" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17743">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارهای مجدد در  بحرین
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17743" target="_blank">📅 09:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17742">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش انفجار بندر دیر
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/17742" target="_blank">📅 09:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17741">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دفتر پزشکی قانونی واشنگتن: لیندسی گراهام بر اثر پارگی آئورت ناشی از بیماری قلبی‌عروقی ناشی از تصلب شرایین جان باخته است.
پس از تکمیل آزمایش‌های سم‌شناسی و بررسی‌های میکروسکوپی، علت رسمی مرگ و نحوه طبقه‌بندی آن به‌صورت نهایی مشخص و در گواهی فوت ثبت خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17741" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17740">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
تاسیسات و زیرساخت‌های ارتش آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17740" target="_blank">📅 09:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17739">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-dks7GRbK8aEUoaiV34IuD1FFNAfZoMPdUiwxHe6LkfJY4dYnTtSw4j0DMkFxiS6aQtiVXJUOFt_y0HtEQnKY-FgTowJcdwtAH4ofVzjERPwryDcAk15ZAX2mL9DFx4_4PrQ6iHm9hADEuSYAjcLjNfFDJ-da79SEP8I1e9vVHX-ALGKq-egNUTlGpO_LT1RYtR32377KrA9oKtBiKhyUBgMQtK0PRHqfHCLXwK3XvEvOFXMSp2FEP1U9iQO-uAixMsBzJwGAYISXj1ftE77ikHsIvc4f6HvGGgMHtTWStISK-seW8yVIpGbXg8rHWjjOPXIN-3hPtYfkJYUMs8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث عکسی از لیندسی گراهام منتشر کرده با کلاهی که روی آن نوشته :
«ایران را دوباره با عظمت کن»
Make Iran Great Again
@withyashar</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17739" target="_blank">📅 08:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17738">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">https://t.me/boost/withyashar
امکان ترجمه اتوماتیک و ایموجی‌جاوید شاه رو از دست دادیم یه حل بدید ، اگه پرمیوم دارید!
اگه ندارید به دوستانون بگید</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/17738" target="_blank">📅 03:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری سی‌بی‌اس:  حملات امشب آمریکا علیه ایران تموم شد @withyashar</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/17737" target="_blank">📅 03:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بندر صدای انفجار جدید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17736" target="_blank">📅 03:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۵ انفجار در خورموج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/17735" target="_blank">📅 03:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری سی‌بی‌اس:  حملات امشب آمریکا علیه ایران تموم شد
@withyashar</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/17734" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17733">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8ecf8e41.mp4?token=ORaP1vX3XC2YkJJIrgEbyFrRfv27GQAAQz83ON5l15n9bJwy8v4_r4Sg7HgMiqH9zkCfunuChaDpbqfTZa4Fz0dYGclqN8_fLG-5E5eVQu28ITLmcGPGbwhv0nzDJ2S_6OvvTlrp4OQvbHQjxKKtyMvyZpReIDcbPHkuBtsG5tq48bHcxHIzJXDwJrrztZE8qPz2PX7m3XNK5Pm50nA7nQ6L7LcOmd-xWJ_XXFeDgm5IDZpHvaSLG94l9P--nNlaBJSbIQCZFfG-84MGCxnZYm11B0EVdm6NSp2qdEN3UqKAOdjX2V5awwTTdruYdy_PpUTxUa3L_FQAy_bZzdKqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8ecf8e41.mp4?token=ORaP1vX3XC2YkJJIrgEbyFrRfv27GQAAQz83ON5l15n9bJwy8v4_r4Sg7HgMiqH9zkCfunuChaDpbqfTZa4Fz0dYGclqN8_fLG-5E5eVQu28ITLmcGPGbwhv0nzDJ2S_6OvvTlrp4OQvbHQjxKKtyMvyZpReIDcbPHkuBtsG5tq48bHcxHIzJXDwJrrztZE8qPz2PX7m3XNK5Pm50nA7nQ6L7LcOmd-xWJ_XXFeDgm5IDZpHvaSLG94l9P--nNlaBJSbIQCZFfG-84MGCxnZYm11B0EVdm6NSp2qdEN3UqKAOdjX2V5awwTTdruYdy_PpUTxUa3L_FQAy_bZzdKqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیدیه @withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17733" target="_blank">📅 03:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17732">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRxUVB4WexyZNO9NdDbCVo2RZ1tzPZy07DSZK2ymm7xAG1iKqPPfKaEUIt_l9lvnwuPjH1jXhgsS_UlKeX0BQ-HYbBiAP9YqcxGw99LqRPmXCel7vhO62tFuBdVyrpGvATdeMHj0F-wMOJTBpJBcL1ai3gx_nGA_AEuuxr2n7LEQh4z37Tjg9JjFb4KMo3t-EnS4QWgqTPoXxoIwlX9EnTT4PaT0dc9CdaL-kCjg1MMmYOh6RwI4SENWdITRYM_Wb44RkiAWHvW2a9S5ZU1qQVWG5J-kSBzzvitN5Jdq2NdYUbKCD0L6dqDmD6-CjWc6CtUs4LMHzt8lXUrTiMvBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۹ سوخت رسان در حال انجام مأموریت
@withyashar</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17732" target="_blank">📅 03:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17731">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAnq4jRl_Jr0UgYqeKOgR9OuS0WUCv6x5Ondy9q-Oj_lGj4QYm1kqY-nQrjaToRSXSluvXDIlH_kYdlebIY8_zQ8XIRH63lboLS3QMQDAFuy9suC2IPBkH1EYR2N0f0iH4_b56al9HCj3m9mHhVlxJuZBWebsxb4PGD3zHWVaAAmAbjqnb61Z0CFJNmq03A_IS6Jy46drwjFytsDmZxBl0Dm60sT8z-sJednlxsh5da_YgTCTRkw-wmUPN6xA6oA6MkVbyy1BX-VUexVJ_4nYi12TPiY5Q9qNrAtyeDWntKtDMl7VMR_GMrUF7zwy9iDNTSJk0iNEQboSXErrCF_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدیه
@withyashar</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/17731" target="_blank">📅 03:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17730">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">افشاگری ۸ سال پیش زم
@withyashar</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/17730" target="_blank">📅 03:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17729">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سوخت رسان جدید از ریاض عربستان بلند شد و به منطقه می آید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/17729" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17728">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842f62bc5a.mp4?token=CqKfdrrh7K0onfd6OucBD58KkgQk_SzCSwiakO4aj2WZDEikl1Y8xGh0PpApQKaDk7ABDxxOluIf8yTBLhYZyTMTwzYMIZ4omVexLip4c-3bJpVKPfjPeCHVi1EKa635i-smiE01oGtfsKoTO6OXFx7DPQ2Ie7w0hNCdtqjNXaJQkVTq5EB-KrrIrIJAVnp_UWr72l2EgzWjnRzpE0BZ43BSB8nSXgx-5GddmSfyzYi7qVGZVeOPFF1hsbi5JcU5hR_mk3NiuZdKlwCwMAMu2qqGqnbc7Y_d6e4EtpR5mszS17_RTXJsRQsFMPW15IDvrwnO-JS9URyn9fAHVdN6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842f62bc5a.mp4?token=CqKfdrrh7K0onfd6OucBD58KkgQk_SzCSwiakO4aj2WZDEikl1Y8xGh0PpApQKaDk7ABDxxOluIf8yTBLhYZyTMTwzYMIZ4omVexLip4c-3bJpVKPfjPeCHVi1EKa635i-smiE01oGtfsKoTO6OXFx7DPQ2Ie7w0hNCdtqjNXaJQkVTq5EB-KrrIrIJAVnp_UWr72l2EgzWjnRzpE0BZ43BSB8nSXgx-5GddmSfyzYi7qVGZVeOPFF1hsbi5JcU5hR_mk3NiuZdKlwCwMAMu2qqGqnbc7Y_d6e4EtpR5mszS17_RTXJsRQsFMPW15IDvrwnO-JS9URyn9fAHVdN6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی از اهواز، لحظاتی پیش، آتش سنگین را در فاصله‌ای دور از حملات هوایی آمریکا نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17728" target="_blank">📅 02:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17727">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شهر هایی که مورد حمله ارتش ایالات متحده آمریکا قرار گرفته اند
💥
قشم
💥
سیریک
💥
بندرعباس
💥
جاسک
💥
بوشهر
💥
خنداب
💥
بندر ماهشهر
💥
بهبهان
💥
اندیمشک
💥
دزفول
💥
اهواز
💥
آبادان
💥
خرمشهر
گسترده تر شدن حملات ارتش آمریکا نسبت به حملات اخیر
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17727" target="_blank">📅 02:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17726">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام آمریکایی:
باید انتظار حملات گسترده‌تری از سوی ایالات متحده علیه ایران را امروز، نسبت به روزهای گذشته داشته باشیم.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17726" target="_blank">📅 02:49 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
