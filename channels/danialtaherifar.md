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
<img src="https://cdn4.telesco.pe/file/XtLwWUBR3X9IwkRFS3OKsU0fwT6jHlKeSJJ_PDdgl_6bPL5mkDin5l6INFw3hZhONyDiIdMkwWxVRhMe4fei4ZlhoBxf8RFUAHGeMabnt05C9xfi3H8KWZkuKo9Xi_SGRXGCMG__LKrd9bKLEr7CrSS7n1ubMztlf_-VgevI-X99cvxOWZyWBA6ceIdk60CNQfHVZ0iqtG-Kh-_b67fCExX87U0Db0NmP2ONXoyWAeTvHUhM7aPa4DXRjk-HB_bLZcwPz0lppPIJSMydy5unVGtIKaa8o-Uc60ByPUlDNH_LV6z_2X4460_GBAYpdrcq7Bfm9DsiuqmuLSPMYvPYww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQfxsTQRD1nT996AzZtqP76yNlFWX1uHh1LoXhUR3o3haLD349HEFQEBJLbilOQSjZ2kwrN_2FOlz_KdTGzBY5gWgKNEvvpJSxoIjGKkC9YqRLQYWZVDaqG7apW8EV5rWjuIe-peAgEPAnacKFd-pbGdgoVa5H-Wbh9nkQYXlLoKkEzUHqEJi2DXi-1KP1IfwuFOIcrh_UA8C7WMSciKSaraqSQanKzBJ8lOMwBbnAylh0fDZeLus5CJuIwmmIQmyyCgjsxRbC6lLcbbUo6_M7fpWG9TW3hhVzNksswAn1pjPCcLQS2W24OtCTepV0vcvXioeobtOZ9Llf6pPmvVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 289 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 510 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 627 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=QCK8waFOTtE60VIzRqLxTdn5V_4nMZi7T0mtr4g9FL3pPYWOOgxMLlkEvqZILWGZNUji21XzCQF7FFgftod9Rfn-zawcMDlI-izg2m5ZpDjCOLwYg5rcmfBL9EZL0b8Do4br_BGbt779PRRLPoQsblAJoTWQP1wVERJNHGTiBUXgkEgVOIts40EX3EuOf0YatqzWBAMgGZF_KUCYomwwaX4Y8oUlnpLseel4ZZEy2k67GHKuk5PNyFWX0FNoL8pYfr8ggeKeuBcpfE6zl2p-kztNiCkqiY1C4Z-xZHCQwBb6cVqB4s3-M0VqZ1d_hyy_NU5LF7qFYP21jKkuWjjobw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=QCK8waFOTtE60VIzRqLxTdn5V_4nMZi7T0mtr4g9FL3pPYWOOgxMLlkEvqZILWGZNUji21XzCQF7FFgftod9Rfn-zawcMDlI-izg2m5ZpDjCOLwYg5rcmfBL9EZL0b8Do4br_BGbt779PRRLPoQsblAJoTWQP1wVERJNHGTiBUXgkEgVOIts40EX3EuOf0YatqzWBAMgGZF_KUCYomwwaX4Y8oUlnpLseel4ZZEy2k67GHKuk5PNyFWX0FNoL8pYfr8ggeKeuBcpfE6zl2p-kztNiCkqiY1C4Z-xZHCQwBb6cVqB4s3-M0VqZ1d_hyy_NU5LF7qFYP21jKkuWjjobw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUqEP21m4ufNY01_xor6QFnsRc8MBIfUk7GwOcMW30_0IHcggHQaqDq9lSr2PUrtzrVkBjRlWKWeOn3rcHiSSIjByLFh1Jk4IZTmFFY20KdxhEu1ntDHJwGwuXz0TjlFJuWTwDFy3hZS4O7-AyNp0CMNwB7IhNm-TmrVa_COWcR9MN5_flkgAz5rB4O8pXX8id87lXJqOlx_u4JrHbNKKIJwieg9R5YEX1n3ZiCQ75FinYW29tvYRRqu1ZIvVIuofSkrXEzrEO07SBta4fODEN8RXeAJUqXlPl0lJAgeK1_bW3gwdg--tN8SM7tKbOdwoo2sjDHGNHeGEpVkI4Nueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv9VktpqxnDVWHCe8u-DdRJP0aIlddYOD3S6h8ymma9_2FfKUTSGRzqkQ_OtiEkb9n7GLZJRalBPDm3vmOnWvPhzyYPLk3lFQ_G9tIp4bhWotAJHpRMK9SMPJhkmouoyvat0QbK93mgdL2LA0HbbFZcUY6p5_DRbZ8-h2psloH7o5YKPpGeAAfu3JRnxZGk2hrs3X_lzJusAyf4bZy608oy2o2wx7Ug5EDQS2K2l1jK5ffXfwUZZVnv8iSLXvxi5uJmaBcdw_-w0wuWaOwsuY6dKOfU0v2fTASMRjGjkWRTZgqW5LneqhRKdKQNzE-KQFy_Z9K2iIC8DyHXQUNkZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE1hDnY9ZlTIBhwvxbufj9FUH07ZBn9tbhrFEYQIKfzC8wWzb4cCeXRlnZ4yCFVqngjWVashLnT1nSCX9vSltszWIM6DTH_B_T0U9nVPXk6RM57GMKek1xLIoUrn2T-bAYLSIPNFiGUsBAT7EzXbWxhvzZX2sxtIKH9f4BnGYMoBug14jDfZNCuOzdUeQnJtJJ7O_yc9Jhmkh43VaAi0w3iEkFS7hcYyBye_UC-UrfX6sPwLWQKb1x_9A3ymPsDuNSA40Miia-lRMBbpC77eWzjKipx_srn-Eso6Nt1KR3mEQ9DiTF4O5wz-_hlxHzZ_5yAMraMR7MzGIWt4jhLjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbXkwFS095Ik8Jimkyqn7F-kkFEMlqP32aaTporNeMTkEfvibOR9fzHQBM3CECBjwusCNP5JXAm-axaiNiBfW1HIusnBcWzAHHQhfoP_8hNWgTkv1LsQf5DakuWPITQx-ersC0qjGiTGxR3Pwmqrllv6zpBtQgdpFXNbs5uStR_lAF61KUbKczjGNfuSCUqhdJMk2Z3pFBHym0_62R4cNuC4WCjSsV1ATpd6Gg_v4m79RQW-P6ATL-7KuOMcAVZGmwIYdtjXyhP6E9jwcZcXHs5-nUeu3MfGS4En7Sk_3d0CKB8V7h8NsWm35xSClJO0yY7rhE6mWIOkT-wTRs25pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZlLgP9I65eMDmHEgPdyl0vaTEjdw49nyvIJ8w1UOlE2dhUsGcKqaK_GpMb2N3SFYsfAodWaGiBeUHBtmnft_S9MlMmHrZehIxHaAU3kdbioob2n4zVnKhKyJsP2NljiK4oGbf6pfbjGdO0YM0KfWpco8rcFS2ozWA8tomFV_rHCUlj7BOFkEDlGsUFHpOs3A61_mAoYlC2UoSYbWkc38fY4G151nlRg7rPR9D9VcUTjUdZu0frbVeyNzmh79CtPo0LvXtkiDf0Ruzeuqd5A6LDN266robH6N7AYacpFfdTnl_PLyzWbk308rsDpHmdDgj6mADkkigoj3pa46Ugwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikNWJv-4ggFsfyJdtfmYWaJVm7hF0NCeMER0C06xK5sqHFDX_vFY4s8dvAS-QJsbuGHvZIrkCSxIsAGrWYLVtmekBji-bC09VHHiI2Hwp5GceSOfybB9WV6YvGOPKzv59iHSb4QEa37wVW51VKzZVnDK5RYoRhPpwvRlmfa0wq6yOYU4VOPYSeRzW0jl8_BPzqyPrSmc5JYHIfL-GCaKf-2ppSDT71kJPelMqrMLHIOaXvgTl5PyctdEfkGy4M2yjYnZbAP2zW7PPLqG-dx3NEHw5D7BSmmLiGzgj0pGQ41DlbgZW3-oBZhQgDcj8_lVaMeeX7fP5nzm436MnE-Rhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VusEuMi-ArMZ6OWOMQ3VV-YQDuyg9p_NKmHM1qWknt-NONjvxsEzC_si5o1etTeAdUdI8hFEsRJyhWDXXrVO6I9ob4CdUnNNTX6faZIgmPDWS2BMf-YUlzW8qPe9AxhR1_NWQDscqy6EUR62fse2bI2v9Wn1u9EYk2OVjbeo3qQs7Z99BaQI-6DvuFHFlp0WtAnR_UjwNlAVYqtzU3ClQI3qeM3BWZTmptrggP1xlMzyQKOxBoofhYfLgVBEasZasDNyCDAdI6e4y4pl6ZcO1-03koDiOixzSgO9EjD6oOZgpJkxNgUM7ii5EX0YFwYibv7-XDjI9TNyOd97hqM5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laiHCD2hTCWqa6KWeaAhhgDY0N1lfSA3TSK3Afaaem5zuZQhXwcU580ChmuDqFJ5z_dcnLYd8z24M3bokBoHTZ7Cw565WaGedx2n11pP5BApgTrJVTc1Xi91CvI8oNVWit94Xnw4-E8FyA5JbNNoTj2yL4iEqWH5tYLeBe3lOXJlGpj99pmS_X5dExrYmkWt4IuWcyF-GrtxpRrn2ahMwHFGEpacjtPBnW8qBnR5DmrK82HJ7C16Di014X-J1tBp8l3KWYvpQy2QzzbaULBTI9R8zUEJq26OX2zLuHG6O7Ix4NFivk8EuNRzqvDohCr6Es9Qfq2_Qpz9wAxffKmkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvBeeXL6yYEyGewTYWhwHO91H4hF2VVMCox1uKnZ_n-4639AuRgLQp6RXxgi3FVRFV0uYFUcFLow1CMXPt58D3lMuNCjkU-fGaKEFi4yXdLVDX46DZcVto-l5d_JN8bLgJfg0ZwjhJShR6CVVM5_Y2rQvQIPNs6tXT_LMm3DqLpmhx8p8Dth1eM-7He2hrsurnSur6mGHImT8B4Sc3rSVGlmgyWaWZqKB5L5K7EM1cPthvu4wShnbWuIVlilaQN-Te5yTbETCoXyVewhyFFZLUWF5purd2gDjA2VLvlSeHYB4L2PjN_VaPjP3ASbTVds5BeMm-S9wZS-uUCffh24TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOPqD8OTjUea5PBRi8KzgHEP_fzBH8NVjq85bQmZyZnJKVFUYTDQixqAaVGt83HJddioF6gSJXmpPQok-BLby7Rr5mnnMqBxMA8vKxM-dzzY_Wxf4iJ4J7qxZ4wgGk343dXXJGtH2zZ-EyHp-UxviBL0csVxvyu9ryBPSOBnQT9hQ_oDh8osgVlwXKSAMA3P6IwbGjeH6P25WtXSfpVDki68TbD0iOBPiPrwRAiJnApEuIB8ElNcstoQZ2ydu6L5Oo-f6JnNuQZ5GbJalTUbOAaPQZ3Xtqm9w48_L4hADd50ihxNXRkaPYAtY5KTad5xIHn9wIZdYdApLlFTDJCe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgSWfW0LP9i6WpmknroWr0Vx_DvtcYIew7zicD5OUn9TM7ETKx8fxtcLVwm6s9_gUjiTmnTNYTu1TUeDMphqqZdrTzgG6gM_nV1QkMQaboJY0dOV050yROg6kcQZ5BG3OantWW0emSTYemQT_cTLYV0G5sgA8RLK8kShyXXPxZoqL_CmartR8lF4ePc0pXN3o-VrvgzywL4aQg6pxZrI89crMRgkeNDsegWHtsgYC-YJP-fQnuH0dG_mgV9MHgREvPz1q2g4eIZnMSqWYpD8IAmt1tDO7s3pOjmLDk22HPklcYKYEo-WvvbbgmxOuS_V7sZRo0AuheB6ro3lYxTbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSd826ryQB1FYJF5e4AYHuE14sncj0ti6zE8stI63FLNwu70nO8HtETXCfirsXP8lvcAAHhwmTChTm90bo96vAgqUzWEZbAxL48uNljGHfC2NPrjHQOCn1BirrhZ9iAoTTJEe0IQvZeIiz7pC6UQFWeYLM3t-l0KDKtsrWnbzWi4bwGz04IK5K8dq3xwzksYhVqKOoP44Sd8ak_upphP14gkvVohygjt8i2_6_wZcsez06q83Wt3CKvjmrN26dO9VV2h27lHi8afCamBEb_1cMf9Tj9Gh_jNGHuRa9xDBz9F74Q6xOWBh-9kOjytK8bQWLmgChepxFcNUUtiXIlzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUFMoclQDZaKFDCl3fIYW-HIWfiI1HF51nRzqU1hTbvFemjfjUl-ZKEiiqn04fdZCbD95Uui79fftaATDFx1lYAjcJSx4izpI8bzTx20ONP8T43BRFCyy6uhXDoSDrfE1AusQWbCJrc02SVIQIqg0qOZ_hNSSEcJn_Z0UiySBw9STmqkiCbSaZuEYCjd9WHB4Ghfas5t0zt0rPxfGXdQE1lxGcBPqj4-9JInebX_8WYFJWevOPv40OJ6g3u5GKSGdcwNEZ8uMd-3JIIfSz9ZXQd9cMTPzXxZ5cR3xbhDVyfWFx1v4EByxUCjKsyTkaD4u7TynMNfWiDn1jNUiIO7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOjXQnFGQJTunlGhvPXNAfZHiukN5to7EMTD7_rgMozNsIJ_SOH2O1ivPeFw3xT_vATJ_Dy1cXeceMK2l8Vcm3W-umAuNwZAZLvK6oboUO15jxj3cR63PLi2wg5YGAh3zGkZeGdqxMwzm_J8Vp22UiDjhqCEUkb0vQNDyS8Gy666twHAP56BskX1c6EJrfgra7cqy1MNGFQsWAMwOZ3mSTwRfWgjJDx3gosaURF2JWEImvH_fj5byVKC00luWDT09cl-Aa_NipZf1Bhw5Q2hAoEOeW_3aEGQa00g1HY-NQFgEzZL73JEcmiXJpLj4LT7yhFXfjU-qZMoHpZyhfZFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fjab3mRVi6m-SdlJuvBVsTfc8wIFWFfCpbMwAlJ8PG1jv8p2Xk4gWrq53599appkLM0_xRK4ctEjLkGOWcdvZrACdbZf-U3uc0R8dwnh9Lqe_cyVHUB05Rv5FnIAbs30y5E0ziLKl9eAfzKAiWy7kzcpi77xGQOcu-R8qzpcVQf0_ZTcBH7tMRCpq-Y5R-sr7fMo6XOeMKJoXFwiLXCtMfuMIUCyFqFcqmkeWqdtmg6gz7ltjks7bqqgSw_QUOj0KybSC5GZ_hNfKVTDr4fBVuyZ85ZjJAJ4uqDcPT-u8pNOIwKSlH7B86SScUzKEL8D73dSy9EBD6H7zH1mY0vMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXCb7NGLobVZ9AjHimXIIXublLcNDVOS1wfccON1WnaT9huEaFT4LS5DvqDIcyx7PRz81ndZc448BQdNj45VW8CQ79nzVtLCzB1ufNACGIWePRlZvv2yOXGSSSlxVOK2gQ_AkpEedTf-9PkiMNxX8ns6KzEXk5Mn1G3Ve0Qrjaviu5rsYMn2vCbXSlE7vU6dQhNyJ0CiEORICdLED5bbkvDRXOc4rYo4iNR_QiSe1yWvoXJQ4jLl5cKbhkMUbDpGpHcjsDEyJvIE0Ay-O6J8NDLd2nLnCKZq4zMoFBZAi1curOTnrtoY5vKnVXa_kwHg_SBwdd7XJeF3TdQhWWRwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZYZOg7-COKc7UoN5eG6HvSGtF5L4TM7W1C-1kjWkUat3U7NBdcXBJ6JABfmIBtkYw8RoFonsmPdo4cjsPJMUuv1e3SHeMQPL83wEbDu5d01taxNFpcxpyZTd8eFQBKREk5XuBeAY9Qyuzc4yvba5bS4ssx7nUXNCZXXD29FUCBAXlybDOrsarRqLBq3iuEt6WfxVbD_HkfNBEzXjLNPQquD0oXr4e84LbOmshrw_9nOnMtjSL6O2kD7AkYG3kNjdAHmrsOfOgg2lLyl9x2kmu32XfWbXve1ImteIpyiINezl1_hgEOdV7R_U3JJp8_mPJaBsi2p_g2n46B17U0iFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojHI1SgWEMOhxiC9Ig5zBs5oyq0mRi-xzCzzPKWNi09Q-9CUbWJM3sJQaFHlIR9DE2psZeFdbYAoOHk8XIsGVSd5OHvIB5QjH2jcAt2Yx6PyloPB9jJOy460dWa8zFo2c6x_b4CszYytbAThBvA5jXIM0zhp_ubfyoQuu2rsmM0Z0loQdNSG7ZcnUwVdQUUNcDJyRMIrShPMhrSiHwtU3DTMLZdIX4gvOEYak0yvRlhXs3qXLQtrwmih193h4xSfusxLri_uaOb-n1HX6uBaoSjr5Iz45ysxf6xfL2YXk4bk6xNLVwWR3JliGTgiB4LW01lwnV1P2L2KsFUPOTxPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=fJJmVW8SJJl3Uku1sbcd1bcUfvidJIDNZZCtqo7JbDuc31bLvaHlnVuRfxrpf7o3KGSxiHjItvItJ371oq6SsLLwIGXJgYBUXjfAQ99msv9RmiTd0Hb9yn3ZauxuWPrZSjmK7Dt-mphjz9MvYVXytlmvEIfklh-DV_ndaYzR970VVhHgz9gtZsZTEhWIOgOghqoB6Jxsq6EuFJ-33DarzaKg-NBJQPNdYJH36I0NRhJBMft3qzIkHuUSsxfjBFzuhxHwlvsDlm54T-ncknru1U4A4IbYo456eABlQcYpPuQjHPwc0ndhBL9aX3p1jmuxHwb4f9tK1y2zb8_taBbaig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=fJJmVW8SJJl3Uku1sbcd1bcUfvidJIDNZZCtqo7JbDuc31bLvaHlnVuRfxrpf7o3KGSxiHjItvItJ371oq6SsLLwIGXJgYBUXjfAQ99msv9RmiTd0Hb9yn3ZauxuWPrZSjmK7Dt-mphjz9MvYVXytlmvEIfklh-DV_ndaYzR970VVhHgz9gtZsZTEhWIOgOghqoB6Jxsq6EuFJ-33DarzaKg-NBJQPNdYJH36I0NRhJBMft3qzIkHuUSsxfjBFzuhxHwlvsDlm54T-ncknru1U4A4IbYo456eABlQcYpPuQjHPwc0ndhBL9aX3p1jmuxHwb4f9tK1y2zb8_taBbaig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzfx7OokrWPncbh-ep0ou8T0ss8459Xgm52ybqWMMI-d_sBrTlEGzbmARmGXTuT-EdTOWyr77OuZVhrT8anyKtP62QesX-HIaBPKqifyGtOLpF5n8UoGnEdFMX1PK4k3AzLOcWsQd2EGua_6j1RsovvzlVJwTSS2-oxoL7JD4-XuOVf969rD-PEMo6cSwAP7n6HO7XPYp7VCfXgciiSyOEcukysdGqbENICd_cubEsqgFTK96bFtzPq2aSShU2rGiwkap9Sbe7VunplAEr3Y4EtICX4FmQRKBFKCZkERExvrmu8fUMAq7hXAeC8rmSXaJiqba0DKiSn1rHIEH_VKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REZvd9F225NSROvoep1_9v679tVSt8yIGxzjHGcQYXV24vbdmX2HbDTJGGd-ZjoCjO_XbYGMAo5pk9wEIBFjf_9S3XLj5G5SF9pkrTD-74NNO7TJQyJ4fMrnsBMaFs8sof_cmVs0mjQkS_nbUnf2DBh36iEUwkpjNd_DSnJRoHoyjZJCoC57A691v2KFjj_jYisV8gXXafdY5EX9-YVduvprL3zK6nqcSkAyaQhRDJKhPdeK_Wj1jMHhbNBo3IMJ9AJ6SLuWnXlcSZdJUeqwU5YRyQ1jY8XlY3j-nw3Yb5IiB8aiyEolVxhjsNiLz2WTP-8XTRQTNZQeara9E9hXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtbnpIB4fzW0OnMusCA2YQ6q8FTMiBo2r_Q5dMaejdmMHtVcykVeQGoOayKqDDx6peGCpPmLaddZN1XcET-bjV3fhDI4u-7umDtcasCALD_i5LxxBk8MNFz_R-JdJPhzN8b_yKTJgQPAkln9v46cQR2ah-oyCjW-gpZ6V3XVOmmG8woIx7QbawOuRfaSa5jP4TD_G12m6qKmUnpmtmBt0RBkmFTYVfVxzy2Pt-CisHclOIRUjs8tXonB7W-Q5xM_I2AiP5tgYdwttRkQzPO_FeNIHXGfx1lMs_1HW_xzDN0as6MNZj7SQZXEalVWE0jNcPmonzr4GKQE-VZmEw47CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjwRw03zsHe1l-oz84bLGeid0RKP-T0krEtziDRbWV7rHImAxsk6d_mmrfaNQHaCH_YRX1TeVCQPjx7nBm4isA-gv5BBsCsdk3bLYlUyqTce1ClVZkyMG9mC84aXWQtCXckYtIFqUwPX7K4c0-iyTzgW_eKaU_1w8cTequFpWBSr6LHIN4ANrRNwkFiEoayPUn-aeljYFcij1RKzTEPl3v0C4CNp9FSrv7DpV8WSclENlDeD57Ml5o5OjsWdSnb9o5T0LPu0exewbLZFHqRWByVStyH9bdamddhllrBT9ZGXgH4LMFwY-wKPVALkLwQdvVrbO47CDAp8WZc4kZHchQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiC5tWTnSU4giqjC2IAmCw_0Qz2lz68YzOv5fzCWSX9y0El5200676cLvVf_WYKv-K19tdhpT2gRuqVKa7bejjwN1aYT8TwNmUghkvAVLvd7qbwhon8H3hiO5Gw91ZBOWaqYc-VMCxYQhECLJqerAMcauLKsfucKbg-OLJLjXMu5QNrPbyuYvr3BvCWDJilvw_BGjPF7TGQHP2GZvozGwDW79wqWljnnPrC7rmmSD5D8ICRvDjUDOzEDRQpLlkhyIXJfN3_P87GnGQ1mpQ3MDEzLGkeTbPhU9JkTfzVm7NJ7-6l-CTiq00FNJnN4IEoVV-cL7GVa38zBR8b-AJvcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhFurys_fmYxhTsYztEeDPdgrbjPLZ1OJDhh6VH-gYaQ-L9r691bOM8J5EjWMxLQ793UGuWAGmhupqrTMKaXZvMyTXDZhGejfFxZxtPpr3oA6tvEIEZSFyNaIBNFqecB1-usoDd_24LG4TbH_BAio8uJ1yM9wMm60L5E2r4fHDiFvd_AFK-3Qo5apOsWbQqlTXxsptitWYq64mz7NleVozpUcuTPyc2p-T_97MhTIKUjMigmGpTtFVEllBJAIZk5QtkDl6rGHlp5_qjv9KdQJbwsObpj16WzwmkMiwTzU33b1dBZzPsLFRApBAXCukxbiJ3gxupIcxBDBGfJqrIwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEpWlL8WQ2V4pghNV9JOchEgeb3yAySla_CTjsu8Y1kQhFWrLr5Jy7KxRdmILcRkZLBkEZlbwo-Hj7fGHV7-PGOe7OF0BK__0uaoNaxRjKcE11iGv-IzEu44bjYABBDTr0sKItd_rgnzDBSb3UokHijfAPYK8CTgS253hxZfTax_tY5O4a6IOTbHxw4CSXPtB3Ec6eUwsZKMDOe1ddluKF0870SWYrJAL8Sw8g1qpdzyYEswsZMg4OiqiAfT8mpYAIlbdFCBSdOWR0zxXRHrQjx8ByVZeNi-H8RiyS-d9Bs4EyZLl9Z25knxXIMIH6m9_DTEQ-m-PAkwcXfWw3-xHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHndx3j_srd0xATGNIBxXXMEjRhinaq-ouIXWvII63DdZEDZQsywvvXQjYNJTFn-pfE2S_C7gZ-tI88-tX4zUevIH7tJuhXxl4yZL6gWEFvwHGtSfvMaVQGNvMMRty52SGoKkf_38aGy0aRvUaNJ3IiTeyFKSLNTAGdDBWLv9-wril6PEcnjm8qTU_1KZFb61hqGrLgFzDDDGINc823vN2KxRytSThYhI5phFM0XIhZMZvpP6JaSsbNG2V-Yy8uOZsivfnnZA2t8PjwMPRCny84kvWmM5THcDZrwSG-WWFzdQX6epPStzg63lpw3JQT5ZjJgwUoAcmMqNuuEW3dFwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUtIBUTK__wPkkn8uGVj2urDuhC5wdeZTkbWaW7suu8koHUYaXghAI7hQ0JRmEMq6LTCuGQct74M_j3OoZosDF7UlT6fCJGXPoNSHyBzkS0_ny8AOS_SF2orBWqC33dDDYc_s8xO8EWZzJUiaTDTzZeoa5Wibg0o1WndLPDdHreuEMw0LT2IxujRM_zqG4v-OLGQQbzohbO9j2tFZfvAG3kOxAy-0aui4aaQiRRnaM9reFVAISrl_ga8q0AU2bs7VyFDVUD0_XbGf2B3iX4MSrfDZGWPmiObclycpzhXrp3UDoRoVMwIUTZbo_bXdykbvcKz-NGJGo6Lc5BOwQW5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7bgnUseQUE0yjHVhbRtsq-Bdo7FsLvhOkM5dIhN_UBGb0FYUhiADFDxc8o5ZGwnRf6moOzMFeYOp05nMeP2drfIeVRCDFExuTakgsdmrv-rq72otH-t0OkHPv5DAI_n0JSZFGg4HH5rtM42Sdx-TJek-P9jDt_ib-Cirt9jXmsUZfAdxryVkagyXWFM_LzcWzHeJ4tfbIBcw34SlGsFdslOXo5sy7z24vIJi-Uc9g2_qagKLgqw6-34qvyGTcexmysw3CUWOpDxQGmS6xxOc2TfTclc2TnQNGTaB7yA3pktmsktEU8m2Lve0b3Dl8HnXGR_NTQhxmmQXk-OEfG6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAU8Uol4kPAOhMrd1XgNYQ1WnSWLvuWl-46_B7dDS0C2PpUe47GsMYqL6lHGpxnK5TF-iCMDZ95d3FMPWjwBQiW7iJf8PX7vUFfsXEHLzRm7Axrk8wFuB5-tF5U8i1iMs2j4EaTzEmPLM07sTtra5_xeBRrxMdkNLUXE55EbtNdkhNjTIQfmPsr-Ug1WimX3fltoOUQDvVIBIvhHicBRW9rqx5a122MLjJwhpvSPOc-STotwxZuFZY5Kx2gHS9myLoL_toEzoKkv78jRiY3SnDgmRlXlNx45Kb3vU5826DIFWarlCMjPyw8ouEklRXJHl2E_JOsZDoF0X6aqYJkiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaJImSU2apgn4N6CQoaAJb_oTQ1b75UcGl4JyqZEym1BUH7FyiAGsJocYQKVeW-m2S2R7NY-166OgLaVpkf1HYUdNbw3J1cn2Aq06gSvtU8DlZF4TW-buWg58NXbG_oHSSMGIRT5NtwcHxlGvKAXBAdV2niMGiHgh-9OaNubWOKyCj1WJftQMqNppadj1EzV0_C-jAxJVC0C7r0SOUjsZBTIBGTiJdeWpLJ0poWQkpg_aEyitkfYAiEs1EjNWJ7rWmN78hKs1UmV6fQGjrjDGYtsmgnFjODgVYRnTYjunWyScwb-ZpX87vzIlxp2jfI-sjMZv_1aKtJ7-htWwxWV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1KiO1ooyGEezRM3fbhySKH5nrDso6LHcX9-A1knNMpQwGHXO0N6Hs4mbRELEClNy3Bm5vuhSZniJ9sCMsc1LKeZqdom2NOmI5YqZHTr5c163Bw_6zvpQ2fXUDIV685UloUh2GAvsXJ2eImJO6vnz5UYfuKHbXKQc-sl0aCht9YMogQPM-byg3i0cOi7Mbdi-i8L-F7kVjgEKkXs4W4ZvtdXIVjIt51AHWLlk2RmuTXHQ7Qcn7WzVGmE235uk98qCIYZV-zLv8aRgKwjuurorvsIMxzvUgqZCucwQaQEPv2OoTt7gjx_mRG_67c_xmBH4Mq1A3IT1tb05ermN2eNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEELd4Gc-y8z3cRrYzMsGisuuKz-4vAhdLrBj--eCjexIUWJaHX9P7dXn4qe2QPkC7hBdccX_aaIZl6asa3kGEc6TPsoAgedzLMvECiPgjYWZwKwv17h_ykzYXFidUeJol0MtsWFUsl7ot-XxN3cPJwEFJ1XZbwBL6wuqeLDEdc0CSXP9xHJt0uK8e7VmYq6Cy5hT8BKqBG9Ij3MQJXIZ0y5-1lPBXWxc7M5iU8Wcm9miia8mMv6WJXsZRX5VaA9mpkQPeHWSIOUte99lPIrFC5N7FIAWnw7jveIGRWYZzuB2FliZWPr0NtFbr6D0Da9PnuaSgrBbbB24M_XjawwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBG3JWWOtOGglTtJk9o5tQ4z9ou2GdE35W8ENiwSFBymhFwHl7Az3He-CXuZjXiAPj_M79JkuXtG-tTzb252C-3VFXuBOAExU8Lz_Kq1VKBbHUNcMwY4jBqDZkEC2UQAOOtKvBcvVU5iXP3GKy5ygSTlSunCI7PqFQ1BImm6TWiiBgA6Knho7bt-DHAgA_oQLpioxyqrvxz7mT7sj8MwzIHyfbSpC-O3qW_Bdh-WhdUZJ7nOYjaYKHft4bgHTTs_mvn2RrYJtvhjHX_3D4t5cC10_eLHl-TqsLiaDaPo3uAKm2qIOsPxcn2GI38TdV3_POBLFekrj9l4cN21iP5A5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJUvGFy7gwRuzy2eJWxHqOsayA99inVo1YE3dfvNdlFXBGZJvcFHE14oYxt20s_ubrgmaHv4WHB3b6PM204YndUJ7ZOkvbgOIuv8ie82e4-n2W0LyZWoqxNGjn7P1-R-4c4Tj2f64Gt3vYXHqXXHmRuDfFr4VlK1r6LgLaphzHakDc3uhCyoxTIegevL8pXYYrrZZVRPJV5PVlZ528bBxO0jSw-mYlS1KUP3AXkb1WXHxdI7PzC6RwoVC6Z7l2rRz5ReIdNGKv8j38hJFvA7JIWldgOpNPyR4H-EwHxYga7E0JRVFvgRZML42UYmzXQqmj2cQX-8CzPkIU6u9g0lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f83nNQ6RtkDJi55fYg4juEs2reUPotUPDqG6MB6EIIkV73bRYag7Yb2Oih9G3nxexuibIg0Q7jCMGleUHU80lmVksPQrzIA-Ld3EZpLK6OSGo6KlcSedpcMnNS9FTrbCCUUgTXnM2FPZuTcY6fSCe8gddp14s1gz5VBUex4lcFIQu98rs4eAF_WwlGH8xU-1H8bU6WOHXeBoHD4aTwtrCz7U4sGmkBFYcEdJgvv2F44fJ8sd0ZbSH_uDJCTIBSfyM-FHV5E4PLPkcuO_csCoOsdksxyzqlgLBqGpA-o1GIbgppTj-3NonDInLEXIdlJ8yQQ8bnkr79HZsOThdwAj6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzfX50TroOLeIVedOLhzIYiPWnkxw0u7sSNf2hGMsBSbtgtQiwXZzGrxLmtOBwmNV5dhIhKa1KkZj6gn_Wd1kvD3q-F0phzk3LjWv5y2q530oKhp0MCkX7bezjjh8KixPxZxPhbSDRmHeTRr9pu9SrGAQ2w2i8AVAhkTxf0_OA5ZYk2VCUTJYMTgsynfWB7S6aAT2J_z_nfVLs2-uLlYCZ5TfA9Tw8Nxn1jT8PVRuDh7E8ZZHsAevGabN4PwWnEMwRvCPHghsMGVkmboKLK3y3YtorOJNHCVXIHR1d0NlHfjZ_5O64lPQEFvb5t-SK0RAwdnjknP3iCKx3SSO7WdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 580 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORQPZTeSLja-PhVO8RIf_dfheb2jVjCt4EnFg5X0z1IjWfutUPOflaHxQvHoA7ogGVvQ7jZmYN7B7U0jFrAwharpYbXuk8VuxIyH3dVjxLd30u3DelCRqgPajiWSt9lPwsF_AkqZ7TpcWQjZzSx0jiYxJxkjnXzkRgiuOyiXdgz9hLVToacJ3u_RB0J6ro1OFLBh6CR9WLEz6I6c32Ioe1UqEDuUdcDddWTKgSvB8xP4LuitlMqd6iVcHx6rZI8WGz72meYTMWI90u0cJxi5CpoqjVoEnbeVlSjMSgc1ym39zWxcaAXcNuUwy3kkT_n8sg0e7HN76XxSXyK8Mu5M7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 591 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peFTsNga-N_QzIjhYxLNZ-RI6rLnr4p3KD-1nK8BxXaJcockYuX9z6aTUBrle3krC5lY98DFnU2RhETjOUqZ08jx0GcEi9tJYxWHBcUlBrX7CEMm1g_xRpsvlgkGEU_0p_jTaipxpQAZwlLmgBrxJahPT4FuUYq8KeHV9QVsDHLgpaqNvhLYfZUdNL_sJPEJDFSxQCqHnRJx4FHYDzpfdyvAygKd2bc-l7LSS0pXG-m6kSW3JuC-Q9ovBMz-gL9XSnJF3z3NEFKuM_ksQhCHjzHgOlYbvwxsErPRoCbQvXdeQoU7n8gbWtmOQ-S3lLgRYDEJlOm4UrdJw-Z5ftqcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8mAgz-qyRWBnbNhNtF7v5Vcdw8HSUuV5guF16418FpjCt_AuU5s0-hpl_lpYxoyqFbdsm61N4bSaWqYhvYBi55cz8sqVtphoJLnzjSbixvERlcCfzalMAob3aTi4iYg8b6LL0Nz_AftUBR_sc4id6iwIt38p5hnWPEHSyohb-rOd60n_vls1H9W9UKbtAR65E1jfc7EX4lnxqw8mh_1RsbL0gMzF1wn4982FWTk_dcMeeK8wAOG6404G0emYr5kicEKcv7ijE6qp5GDHIOOpWepwsbJL7bdPWGhI_VRGEnFIVMflC0xUX_gDSeSKkSESl3giAJEfx91-9piWaWuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQDar4ftobZtLQXqgPjsSTH7ltGZZo7WHFD2gchmfZy7IImNXrqJzbVG07VXehOpKomt7yP-Db5CZzEMbf0hzwfVmIJ9JAbVrAo2xU7vVWtIho3utJY4ZDMKDNmvDYHsMtmTJT0nFkR5R4OqjhtmRv5uAKubBa1uawi_ofLS_O6FLw7-TDEGFIzoFNUyQOWqsUlyGBGkLM8zEhTd492Hp1yNrczs-rdLkQU0jc_0sdY05zjhfpuUUzyxMnMUpfR9sWnDMlTwgyHat5uzjgUbhM-MWpgjXEMAVDNhkRFwjjvKekoQk3sJM2uU6IAGDO6mZS3vaQsqFeWiLFaOuuXlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN8-p4i3eiu8A4daz2bes-GzgaVQHir6xvF3WF0x-QTLo80fkNpToP47FU5dJ0wrpaeY9TpLn6MYQLiFok9yVKBeoPHABpQfV2g7kCERtns6r1thjk75CBkAxYdS1CNDZ0fxLhVZVvFNjBp6XLExDR9EVyd30veWPMdBNkL9h_ypMkXYpo94s4ESQlKxji-lo11U5AQ5TDrFLeJ7hRNvTID6jtcxK8RAABCa8CtYfPRLjQLUvy78XoH9HPM_DSbI3sZADTkTMfXiwiranVR_0Tj-Ct7gAsnYo-R-AjAozcZ4BogGhyFAAOCqUpXRHvPorJFWGRNnYNEc6ch23L5mSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0-S-AIk6nDyLp6k89upG0xxegbIe9vRX4u2xrYytxNTQhsRr9GzgX4DH7zCoHMe7RQtLvFSJa4sSLBtUfW0ji3sEvVgb7l5sZjOq4zhKETyEQyvKpCbzlomVruqTTC9f0eqb7KEY9zXTIaOCkNM4bjaO3kHMEG3eMmHD485ixRV4XOCGHt-_FyjBfSelRP8hDolLQ7TE8ChboET899RfLnPKDhDGrnU55W6A0rR8g8xKycjC9PEngSd3nBYOwtDq2zmxphplan5Tobl7fU1DJ8SiRgYbFL3TA1NkWCMYalts6qupYZ1FuJmu27pHq4ncXVlEexMRc7lJgSUpQudgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtWKv_SpJxx8L1kt-HUCoq1kNqZ2HHT7fXNs8dGM23pNv3dgxO0KKkZpRDE9pT_0G2SNFy5fF47kxzDv8mDeVn3pIhJNX3h9zocypkvkA4sLEYYhJAMKs_ep2Zfa20zDN6-liGrxrhbGNb7hv7uzAkwC4pOk7QO48rxrmpgUGPJ5Z64YKIF0C2z4gPiS0O4UkTgxUllO0TvG5B8aG9JlLJr2r69HvDa3vL8zx4NnPFxFy3SCohFZgxOQXHLEB8z5o2EL6T8-m1Mu-SU1NTTgyesEI-zKagDDNEQqhADH6CeZxK1RdGq9dW3llwQqUrU8Js7-SXFwKQrGxTL7DGobug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXNR9KiZytVfsNSrXuYe-rkbMvNgtWSUgD-wdtom4UFrzncSOi-rebxmpcfE_WBQQuAm9QU_B9TJmr9pkRtf5_Zy1YqjIhmy0FQnq8-e8c3fftPMURqM01dHZpRZBLDB6yYtGchoaR1YdLeuNqsKBtV-PU6gOsdvSYL4ebC9MB3njxNhtICGvojbSQAh6wIc9wgXFxz8SBwPtNQsKO46BWR0xQI7aANz2JbniStiRk-xxlQO9FH61dnMJ2djZsS0i14ddsLfhhhVBsJfjwWEkAHGfgT61nCLMUMIKIyvOaTaTCdHk6CEZ_4AmYXFdfoliYhr6C7CVBvTZTaHg4CT5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz5RDtAEiVIfYsOBSQhznKYVX3BwIZHJCVP6djTYeg9eGmgEGavwmyjZXmDEhC_OAp2BBKXOfZrmV1X3r1_6dFta7Ni0sXO57k5pcSVfg5fmfFtCquDE2YI9NVin1lqufufQogv24AA7YeblVH5NX24wjKM-XtrJsU3Qxvj6LUPdpwQqSsISTS-_0W-e6w8DWPMLUKvh2bjXTDLnHyy5mwP8Gkx7tdyQbkSBjTzLIdwF0YLAiSOUNBzZaUoZAKJW5mnZ1HnHivlYvEWtE3BmSMfumPHEgKeuWrRhU7sqw31IhQ13QfoEov1jpjliC3pr7CKIT2kw05oDt7wQPul-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfvdMsfPAymfXR7cJPRe60eENDr0ICQnCJ9yfxHcwEx8iyNUvHAJaM3GRSNV9S82uq2hR8zF83Hgemu-VLNbbUfPEgDTlWv8aUj5hrGbq-Fwd1n6sUfifo8XbPpEomic5zu28dmqLpYEwTB68C4k7JnnhgaC1fSSQyRoXb9Zjmbj_RMeDR6GVf7Ce04NPZCJiCqL-N59sQOc4SnuekHaaGiQ17VrXT3_LTDrYXsPk5JujkRlTJCVEZwH7ZtSr3Dm1YAr4_-ZxBmfJxxrHXdi-VkD52BWvHqZWWY4SjQ3WyQgJPwQz5afQWyvddsJ5Lx4oELyiGJbYNorwEHCXkiFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQIxdNzfRovZDwx33j16HFHvOlJJJdE62Mrqn3RS_xkS78pI1ih2cCk7Z6i8nApO74-mWi3BfzGQo1uJCJFO5UWykO4wOt3Yic_9OIuGpDCGon86ioXacLui4HPc2kNUpe809YEOSABmAsy278tbLOm5It-ABA1FXYkxJdVyMzOVhmRvLiFmHe5Fxqr0mtdKxTaCl6gZV3hRFhf7-i6gE2AicGfkRcAYuPpTTokrJUu_S7j2aTw5UoPNbcaVBaP32xEZWRqcanpn_bw0dcuQ7YsAcIhlhY0izUVbK3JjxYG1ypMKg6UFkOXJMOBEzctwggioryo4pdkpzTEJVm2BHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5adYmEodNMEM4XF-oaNJNQdG3ZH0-18M_DqEj25GVjAY2ZbAbVgIwrO1BTiShUSaUJqQpwEz2bFVshDYA6K-vGOvcEbr3p5XvGrHlCYknkUxyAw9W2SyjyzJqrjMGnm7zaFDkLMGPEWr41jP-NzW4nYxNjnk1iNMPfnafloPS67ITNBgZIovpngcV4i29OEg4liDXR9qZxEVBXd2857Svp8xoGL5CDxz8BHbd3gajI-kRjzrQ_CDBxgJgv14MmupdpPW6EvinW9k744cgObn9IVv6XIFWJ2FzcWW5bc9RdyhuQ3jSfjqN9g0QuVqFFCyPif6x5FiUuFBbWfB-mNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1dk-aeJruWWkCiSIVdyB48z2XOTck5ANhydeQrlWhmjeHli5gYQb-uc2xq5ihwC2rA7xaeU-e5dbp1hcvo0-5LH0ANRzJS0d2WR20uCCr6sT3Dm4K5--IWfQ3KunBg-s63X-x5bti9_PhnaAF0ZuxESxcZzx20qd_YDm4lympX5y-D6QVgMUrbKlfy5FRFyOVNF7p9jPFpHD5Shq1loWcme1xW8FmKsh2Lcc2h73NggC7EbjAUHQQ5McJgGDuGZYiJGzaCRbTVqLkwaWRW85fSUy5RYsOmQ6GmfNovsjqei9WgIbqtENKfBvPdOr196XFgzOM9zGHt-Sru8Wn_yzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyQJfVd9oV4IoGWPim2erg_7WuxDEzkDXl89b2zuaZvSYp_dTw8xI8exuY7_wvsWNB7epmHKw8tdG1IDsTxnVGAw45CaDPhrmLOKq45cehMHGdzC-dbpVpO5sPA6RZw_1ZnPlQ5J3_PW-_v-OSej8MhzuAZAAZ9fVKqdOeMK_qB4TH92Ip8O2DajK_gJ1XilzV_aS9SktbHQwNyiR1SJZHxSv2dDpl1YAHuBPojOvMSuANyFvidlQt5hhu0XZbK3gihx4nC9tSzbLF90f4hwRKQI5q7SsWPesLCJJyHe-MQcY_rRthRjEsY3gEE3tufUyCccCdr_KFm_HBLlA4yfXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTZU1C9-OxSjCYI2XYmPX8havi0vFpt1aD1Sa3OP4gD7TERnGgORrq7CgwgB29Y7w2oUTpBvNNP2iozarhJd2sWPflmVCv8nfXeP41yGGKkFun6R6fBw0h1W2ET7ohsVLjnOOLj6QQq9DrxOqw6Ljzexvl8TPg2EHwgWiSCqZcnz9G2gorYH51wuuvUcgltKIPhtKXifIGbnjlveWRdx7TqAbsG5uoA7fPB2disVTWUV1D9URGhVzU44PP6wbjwG8xeHHQp1o5cU3nyt9n5SdkrruAfHh5uuX53er8bpMvv0Xom4vMBL81Q98b05_b86T7nd1rKTF0oAzN_8ky01jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czMXLvVuXYG1F_PA9oCAp-9R-Y7HIP2e8D_50kjg6EVecXMkYKyEmERNeOorECnry4lLaLDrUu83UQWAjt58eDfIiQ_DP9imUpzg_DD4zrX4sqyRT-XOONfTebKHxoxofOE6mBNaymQu6mxQYgBz5hOf3t3dLTGlL-nxfSNbaZHVqzutVW8s0MKchsPPPorh1IWEbwOEObKDKVbMky6FtGMH5nCJzw7XYtpqvT57NXa5o7aazN0JEPfWYvChJfuz7kvnrEW7NGhjhHExAa3q1XAVJz96Q87-g76in1fWGKSekzNiOnJLufgnvJYocNihXy6mqiUadiXajXfpTlT96w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxG_9oaR2Ydk6tlFItbDYdnq2jdXmLz2Ah55Ev8SjzabsePmLrckc7m92-rmsL4YBh1e5qSPF5H8J1DzXpKc6ietybt_DP_-4VLXDjQlAP2GcfXH_gn3UVEM0nuuTvNjUYy0__I_odOHjIc6zo6LiOLpTVHg-C8bn9Oe_EBkSYHTWnNa51QZeGQu-_muenIUyPhizn-P8jeOeSFeMf5SHNqcUfZwJQNFmg3FtbNWIPq9ZK-YWtQnfNlZoSbc0RI7ZKmIh0vAGHetGO11YXMXWMm_GwiVamm29WKjfef9jFfvWftnTyh3PF7wnGT-wFvcfmogIVnK9pDsrnXurW06pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQ1nvfbjczvd0j7_oPdm2-Hxjh3_auCXz7yeAkv1Mnvs28mK5_3b_Q8AJyknzdPvnHQq7U57-dJTL0R94l-C4kx297HruFaZzsJ6fHriyedyiE6anlwdG8OA7Mgp5N45iUgEfo6Sqiwxy6v_eWwtLEKO74uWfL0bZRro2nK8eF9A-_JzcnwlofH4vCtRMTGKuILvZxQ88H9t0VCRM36IvtI4Hfgk3gtmE_etVk0AKBaTBCNR9fOD2UZuVdd9qqu0yhJ2gspmvFfTboD0Mht1gno9zJa42Vc8h9vwQQgu4rsS9fytu7Sw58bxPnJkXr8K_5oRajZboX_rFLWmbzVFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kedQpIVlTZCC6KsHUq3C3Hnf99GWV3y5YUj8d53Kn9gCBh9T3d9uLZJGyAYmkcDFQxq9dE5T3glata7Fj4osLfNWxoiYgtJ7c8lG_i4cg5qy6o4YsC0kfmKe_VrjR1KR1OB-QwCuu-8VFo3uLnJZi3QnYbL1k3YupSnJmNnjvCP7G77FTRLJwsPUGhTwfQQ9V0Q4_rYBT29BvgsCbceX12NSkxHqttn4vTiL1oyZYyzv7Td6dPgxbzM8wuCc_eypRHpbfR_kSer8AEXr6hyoTSGISaOCSeee7YygT3crQ5vFXOiPE11rAnY2GOEHLdl1MQmo2zuR9gdWWHI8pS3tAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY1xQBMyblj_U5z3noOrzhQJAjPvjOM7x_I3wZWscQ6RsyC4Z62GgjSezd_G4i8PQ_cV2nQNNsofNOgubduNgr6_ejsZiAqQeFFqm3djLGyTrDpsLtJ7aJpAmdhz4PtdvLWJ_Tt3kKerEdgmxTSVWo2Swx-u4-3sj69-7tumIZw4duFYlG3qADgjO9ZSzLDjQ2ulIZcCTWcxMvHIF8OsroQGqpKMhClA6dnIqi8c2jzWfeXR8GjK-Gk0_kbtT1S8otznv72f203Dnv-NrezqDzJU9NRgt2-A3dD_VG0t7vwpnwTEjjNt82lsYZGTA51jiOCq97YhojXE0aPiKX_ixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2vVGaEV-5P4qaEaPUKp4GZrUCuH3VWu9M6jccqUIa4nezRoVKCSPccE0yGxxmCigLbSn8tQWrY4a09sJTM_nxYGUSeK5ncxjB8fkYhxmoOb96bvB4Ap51Jpm0C_6uHvfs0aLP-i5Ndjvq6E3KaCEJ7j3SpWOmpGMvvfHIHeDHLZHyP6qQOA7fD-Adbw0mupm4AfhDNHzYqlNEDBI8y2MDUKxZ_hQ5xf8aXtoelU-Zpm78Tnx5ZvNDxXlizYtyLa8J-P7EfdnfQ5lE8sZSU3HB6Zr7HdOOHI3F8YCYPS1zIWUjuOLETEakEuoaH5E2QCtCs4B7On6GIcu0Sf1dk4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxVP9d8MpwUEG7VLtyc-Z11O081FbT2BD2J98oY51pMJE9onk_LLFD9ld8THRmk3m1jAZalO7meSYdMiZvtD_zLhQQvN_NgQjQi6MQomP7ziiEStqkCHurFYXPSLv2UXymmX3BJFoGerGbaPvAw8IvC9JXLo0YnEDykD-LoZM8uGXuE6Xdaj359_v662AJ48Ub5hjUcdx_G10-vyEohBnJo2jc_wy41gUmF2akn62dhsZz44Iwn7scLAnF89fd-_5KkTD085XUYhKYBxRtbCcBCL_MxcFGOefIJ9t6PhQ5QPbqusAuMq8rKmcbfAi-Mzvo6NN9wW7NZ-A4NOmo5guA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbZh7f4kuioLQn_K3zG9cer4BDkQmA5ZdVlU62rk9zK-HsE2uV2BZdArYF9KtQWaWhcUzodNkmIpysXw0fdYJLYVBhcbwp04v06VUdnUcCnu2DwYomtcfV9dEWPWsnwNED7ZGvRXHl3vPtHv_xuPj25Bfq0lKyDISWP60pe5TuGR64otZV0xy8Grkzrg-oJf1akIKvStoHRzrNDTRs_z3MA_ZQAc4Cxq4tHTg-_ol2plxYEP6mEZKaJETiCGA4vmEba5_P0SwQmVpu4sq058YlBJAoRPRJsqF3Lh_d5lQlH5A3c2ou7MCOAtj1uS-KIJesyaCsz51YVvlp0x1d4FAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LW_tv7eB3YpBeAqAt7hsdJHzCiJKg10OalaDUa0x8cdvnAwWqXL_zNMe77QmP6TFJTwd1Vscid0y4C6XOD51xZOS-9R-Jv9yvQPgR-rch_i9wMkA-CLjHk4REjzMNEICiS4aztqeGa51rWtUAUTgPsaNlTq0A7xn6nF7yIlsOY_ZQLru5Tc4C884STaI7uVI8cxZUmxptlUqoE_XNIMEh2QsAc9XOKR8VM4F5BeMM0tOoJybca1JQY9baJdM9-MfYeh33HXhCQYPz47hMODWyc5TKPcKF7MYME0geuHHHFNrKnig89FMHr7VEfz8Ioip6hbNisRc1G30i2m9D4GXOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFKzvfYPUonqhXtbBHc_5cwCQeN7fNkgXTQIqtuwmU5EWlJE-ZBxzepua2DrheuIoPxl5RQXg_s46M5eznPOEjeYGjxv9hglfInYfnw6tUBhseqiE3Z7AnGc4FlTtCJlv4gNf9iua3-IHoOnVYeCJdPtfJrZJOGULKu6385SYIOmLvRqbuCSeE6EIJkRLDKKEhLGNMD6q7Tu1NjDnRrgGyADS6c14XuoEgau7gfbbo-SW95B3yIayZHZJAcRl_I_S5T6NXhoIzCARK-05xtJMu8npyaQQSkTj15TME3qGGmtLKZVaV4Sm0JiYvFLpORUGWrs23rRCCwQqpVRr4HlHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT1sk6Vh4TszXMbmWkPlEO5Jxeq2GruVhYLGzU2YLK9Y_SnWMrBfJpgyNZlc8-oFObcJH5ev5VyOBumrDmn7CPUzo0B60wgA89yElX5ABEE23Rmtu6DSAMPnoJo4SlDuggQ-6XqWvikBs-i_vaBqULMgN0SW0SgIBemIFujodpU_4J4Tg5h6frjkdIsOIzrtD4fDg7S-K9YzvI-KlASGz8a81X1IXYpvrNaIkoVYlICuXlCvpWwiDqdMnCHrevo7rQJiPwhw_yvy98MemrJRh0kN3W2G-3Kwp5OZMF29GVV1rBdP5XM9ESPYiBqAZsQn75eq9Vu_a2ydJbVFyGwHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRKmXDuZoX9wGJ8aqfzPchHGAEDCG7ZAY1j-h_qSKfdc6KzDraE-xxQNpsZildD2NI3q_1ZYvN-cjrEdEE9LclfKi8NVVPgd3KGQvR57A4P2ISN5uxYKdUCpR8C9BUr4EAlYqh64YQoRHf7OEzfX8ScE13l1KB84FumgFRhZW7-FRP8bHJHG3lFFz7Nr4INf0-rr0I2ti7ArJZTmjK2C76Ujt8R-7_YtecUjpUflEoL7rKfA4hu0Ua8D9UPmomLEGm3L5zDHIfy2s3Wpj9KgoPdbh-vcp0dUmAyO0erH0hIrFC0ysNLYVLUGZEqQNqPdnvaAgizuOKuEA_4RSvTWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFhNPLHQJKjTxlMl7lJS1ir9KfxfCRyhaYydWPnjeQZNnM1lxsFLQgfAyjgEoenHW5FhaPPHqvruGtaWlmIONNq6Q8tCNmzrOWjP-JToAXUzQDE-A2VVq8SPtXs3IWxzlQgrm7rBkBmfVIWkRdbBcqRjw5ya4M0_YBP5cnGhW9UrrBt5PXQ6IyXBv-p09caagrBiQLncyKSX-zDf8QygDo5ltXf__3j2PyGphJZhIB17w6Wd2G78wBquuYXQTNjTk9q9hTWdFj8jw_91IRTkvIIlKk8afwFC7ijH8QICSZ9j4Vok63v_xE_GJ20v9KNSSRJlP0qrjjXzUFJJVqAA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EI8rUJiGSBL86KlcSz9wJW3Ssj_KKrOedHaFxSpl31WHmHAIFHBdjMkTSD2lgaK3NZ08MqLfPefbCkoEkzj3G03DYED_Vphbg3sDyZPycZcZIMArQkmA_dGNUcj4y6wYePL-wbaU2hXVFVM3Co1gs4hbVY3En9voyXLxuu76_ZAaHIKOYbojAU76VfvfilU-n4TTDvPcOuOzrWe8VqQkqWa8-8vwM0ovZd49zu6Nsv5NbVb5DekM__crkPB6ygpWA6I65dY65SRos4V__sqn3bfOJKftNYXsXgNiAho754b54x8_NdYRKvVTkbGFDK09yA48k78q07kUwd-ago085g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EI8rUJiGSBL86KlcSz9wJW3Ssj_KKrOedHaFxSpl31WHmHAIFHBdjMkTSD2lgaK3NZ08MqLfPefbCkoEkzj3G03DYED_Vphbg3sDyZPycZcZIMArQkmA_dGNUcj4y6wYePL-wbaU2hXVFVM3Co1gs4hbVY3En9voyXLxuu76_ZAaHIKOYbojAU76VfvfilU-n4TTDvPcOuOzrWe8VqQkqWa8-8vwM0ovZd49zu6Nsv5NbVb5DekM__crkPB6ygpWA6I65dY65SRos4V__sqn3bfOJKftNYXsXgNiAho754b54x8_NdYRKvVTkbGFDK09yA48k78q07kUwd-ago085g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3S9rG4agQKHTSsxDPMFeWGIWkfmE9a-OfazstZP1sVFmVDH3JSmLybNIUYHlsSbkALdREBjpI9aQDamYCWDjfcPMn6_n8LU8c90tln0NWOCvlEUiRejSPPC2oicZwlxEfL_Rz3QoDZv_v7C7-7j2z5HIuDOUnbJIrpTBefQ7PQb8rGsz3thMULlC_102FhBk3UJayIeB4pHiZO58bd-gJGY3UMI2J9VL48-FfnUhBcKotKgRDh0AOplJsgig5wsHrvffCOWk27JVjVCqZVHflDScKene-sy3qRiNF1FTdr8G8digEyUV7Ddizf9-RrTUE_D0qUTetBDROGjGtr0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3yR3Xp2aZHINAv1kcImAStlWkKjGV3qSQh19sMu9Y_K73pIu3k31soTQpgtxg07w4DN_xAJ0jTZWxUNi_h30Jp24MLZZdu52a1zt_IvsWM1SRjIRiORBMv0XVomOdSS4HbFKZguzZ8xiSUL3rFlbgEVD-0f81YEYtYn09qAiFWmHcmYHssGMKBzCLE-CPu9rdS7DkLacOzBS511dc9mPs_M0VERoZdEiR2lm0dmNy7MUWToDtHF-KQIojio1lI9Hf9cFCOmAy-UA9ZAQN9j3uPqzZly-eDV8feXshhjjgWo3hArCtgZXPzemzNtH1E9syvW2BvoyU9SJAs5a7_pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAtOhtWZ9QPd9czTrYAsmnb4jseF0OmgE09dpn6VkFCJeWuh0vg439HIzDiVUbYmrVWeI0gpbKNKZ8TMvyon3dV4mIDHw-ouCX1qAMphQepdMRlHfeH4PLRpvOicXeBi7aSQzHiZDQVLhhyiIM1OGa9E0tqX7_VQB2lRbKJNT5-kTWWqodLjY_gobxY6ZUfC-ABNoS5TUuqHTX__APcnSFlpRW1um7KTnFTMpcgBq5h-w_mNoH2f-1N9l-8VSDfKzqHjw7HOKNcUL_YkrHsTW4qSNw4tQYqom7l3IkqbM1j74RonjmjBvUKagro24nE7Cs0XlWBrN0OCSxDpBYhEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4HM5H0F_E8Ko44hjAN33czHtIqfnddEUI_ePK7ReLP4cSOYYRarI7CbPyPNvRYFsF1dPEjlbCk6gkNlA7UCGp10i68b2St3-FZDztAAOEmoVU7lZTTEtisYpJYAOEtcsdsp04zmTEUuIj-WaDEVtpbKhIXFFPdrs-UT7DLeaBWd_1UZ0oGE_C6Vsx_EU0_ouewv2nqBsQs6DdiYA2HeufPpqmL7UgZViV9SbgQnYFP8ukE81OxS55VecIgUw7DH-R6ntNlp_ASQhE-AtRYyPJ7_f16v6JqCjK3KwEW4WQy2xI_JCau1GaHLbkIWJJrhUWzhAtLSODDaKLrWGDxIyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1HbsuoXBw7bgHsHT0q6Qn0SPbSj-Yq2XViTcCa3_cx2rZPgXiiimx35qNDrttrbHdb_xDFEYlQ6_S2Cw9dB9T_Rni1e4rP_nZuW9UA_uiAUi46HUfKWZKVPnwACZpMCqgc9FryZEjbGh0_M15SXABs9Ga9ddW8rJKNqpzlQ980JRe68UjpatA5dnYprbbQwv_aS7xu0-yTGwtUOPnSRJuyEJMOYI9iS-_kqAc4P_qmkEr8MjlMoyH16f1WzIXafYQ0fhamLn5Ikx3kZCVQQPo4FaBLiYbjnSsdau0ZvrBKAPqydsn10hgjvIbzjHgPClaBycfHeT94oTUbOF7vhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1tSSEN0BNtJHFutL812alYXcXuRfjWkEEut7TrSMa8bseRN8JZwwhUZsfjyTN_N_5CDtqD1SpnQCEXKPzbCT_llmOao5D1PGYnGRIW9InSmhcqQ56E-N22-XPcYZktUkjsv6qVFJkWhPYR6vbcfS-Vb1uAZ8Ub2VnKPTf8J6iD8Ql5gtbzD6R_AQBbM39gJ1uyb_IeY0Pn13Fah9hKmqfcCI7AZWcpdL2LLlGJjdqhbHxeAEtQNS0qPvKP2JpeTRoIToF1DWjoUHDiZJBeWqhijnOsDQ_A1JnGEbeYoNMTR3UqB0BlTl6-Y2FFi5ICqbmwXpmA1Ibb28e7i4cOFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUGbRM56WK9uDm1ojvV-acbuc_XWTAnUFUInI-7nJ-QruEgVtSE_9YSnT_SikbDPcV1EvrKnuARoAbfqe5xe_riuja9VeENQcqTqC1ZaN3qm_2klg77fJjzIfIT7z9H3hyNP6GG2wPXcCLugbk855j6-P2TuDcR726tgzZKDkQj7qEuiSzp9hhBS34p-m9unosOiZeqlpDH-joLXe3l4inZ7GJynAxg8mCr4Zbf95oGACI8fQAhV7POmy1NBy7rbu-RxFvsh55p_rJjFUVazrJzsuK5wOhQD0MTmfD9LYTIa05Re3fZWVSZvHwmJh5arfmydZuFaI2pw-oRBGskeuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=AR5oGU_KhKJNSaRNANYtWCso0LdNqbCoMTC5tLQjUSI8_FGNCKQOiJd3QT_A4raV3ep9pOSTBF3FQafGCvfCc-S8EbMz31h0NK-oTv1FbiNhlEEBynuD5Mujmv3_HlmSG7mffciGyh-u5Bqw7s_0t7w6OCZPJrlMOBeH3n_QwhHdZzXY_p4elNywQCzloBw44Iyu3Z1NuQke9TrnFpwZF7mlQYFCkT6m0IIz_qrisdCLI5KVkip-pw_tXsYCOOEj5zMZDfMwU959qqSSH90m0TtyRi13INDZKYGcUu-UN8yZzxFOFwRPqJ953N6d9uaUWxCB-eX5CMRcdv6dENZ2JGiBGf1bByHGuEiO3b19c87SP4v2FIQ7vmHpr55GDPvgIeaZ_-Xb_rH-IAd9TdRADLRcRBFq3rr9QmpCtFO50c9-13dmiR5v4GpyGKtjSOzSGkVC13gwJ7WrryCsSD9DuW-fA1Nlxmt479OqtDrfp5PiuYU_SUxVmz3_qlpYbCDsyvZd7y6ZBAYa0iIRvAF4UvLBRLwmv6rHCK95ixnBFikEU42mdgNEZeJVLpxdu8LjrQkxsmP5yVI4Xu4WsM7jbqP91q9skXBZ1ihlS5kSZfMpxXfuRbfkVT9uIaiDC_WKLYn4bv7B8WRAIu1AzT-WCfLc_9Q_c0dUyN6KARyXfa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=AR5oGU_KhKJNSaRNANYtWCso0LdNqbCoMTC5tLQjUSI8_FGNCKQOiJd3QT_A4raV3ep9pOSTBF3FQafGCvfCc-S8EbMz31h0NK-oTv1FbiNhlEEBynuD5Mujmv3_HlmSG7mffciGyh-u5Bqw7s_0t7w6OCZPJrlMOBeH3n_QwhHdZzXY_p4elNywQCzloBw44Iyu3Z1NuQke9TrnFpwZF7mlQYFCkT6m0IIz_qrisdCLI5KVkip-pw_tXsYCOOEj5zMZDfMwU959qqSSH90m0TtyRi13INDZKYGcUu-UN8yZzxFOFwRPqJ953N6d9uaUWxCB-eX5CMRcdv6dENZ2JGiBGf1bByHGuEiO3b19c87SP4v2FIQ7vmHpr55GDPvgIeaZ_-Xb_rH-IAd9TdRADLRcRBFq3rr9QmpCtFO50c9-13dmiR5v4GpyGKtjSOzSGkVC13gwJ7WrryCsSD9DuW-fA1Nlxmt479OqtDrfp5PiuYU_SUxVmz3_qlpYbCDsyvZd7y6ZBAYa0iIRvAF4UvLBRLwmv6rHCK95ixnBFikEU42mdgNEZeJVLpxdu8LjrQkxsmP5yVI4Xu4WsM7jbqP91q9skXBZ1ihlS5kSZfMpxXfuRbfkVT9uIaiDC_WKLYn4bv7B8WRAIu1AzT-WCfLc_9Q_c0dUyN6KARyXfa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTaEeq4FE5b3pDdoCZp2T7kfF_IvtwtI-JCEtgjslspATGB0ZZkH7cYLPEpXBxM8hXkHj2a20lBxjyqOFLuZNkzhXFEXmW_I0uoHOkPpcoX_NW-NeE_j5I8IRPN9Aobmj0oQnPksGFksSJGSVY-Txtho6A-qsPfumjydpopwmJTrHFQh-kd-GR2WBp6r1B1NXea23ZvSpN3Ox_hISL8eq4fQcrl995mT4SuqeQFayp3cpIVbNiHmM2YSh3manm6j8awiTHMBbaOTZYo00xFouynl8mRfMfyX8RMU0mqVSRvqQXoNw9wIKnfmfzMPPc_XXpdPX29-SUxNoAq2Ev34YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdpwIAhiUXzw1G7L65ZcZQdD3LkiURT1SMRg-fLAbKRiEAWTLWKOdSuXzwM4XNrTdWF565QTCLZT3tkeMTUb1nGvJW6Q5iXU9vM20nKRPWqmD2dUDt7yd3Hw3T3NKAq4QnG8E76BPG9777CWow3j3QoobmXKL0Y6s4Uboezqe8T57-3vY-zQ8pEbR0UAaetoQfGJkMrFxOn4_jx0Lgn49XwTRP0wLLNKLC9hRud5ypGOs72-H79A84U3vq66kAT9NvIG058r-XppjOrdOk0lTN2Rf9XN26p281JpGjJeAw21-vraqyUAkMt62fjojQerbJFCi7BK3cIG6VYYRKPtlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vORXHjw3Tr8sZ4m2qFE3mtPpLYsDHpZJFBRLhKyUVmSw7O32oBD_gemt14TAOOsFVIMf4NDJL-KFiHC6aVWhq150NS3EeP6P2qx4iys3jWTmBfQWZfs6IKCR1KA9_8ndVY6aLTX4qidtPbt4l66udUKN9jK5n7cFwDNsvZ4LwPmLeDGwbS-kurzk0GWGvy9ncJIrCIWPV3pnDdBJPQyZkZfINik6aqkYGJ4wzQoSQbYg3W-URhdQU1eEsYUPgvMy_Xb4ILLo2Xm4GqscZ-hBg8PomRChbDt5AIrUdjzTznZjoyzc3HEuZrM4q28E_cc1o-sf-6xRQihUbuMzvmvBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGRQe6pyejOOJemHlY9z7Le7ucPAdWccxCTb7fbYQo4ZXtwD8gaEoGHDGiIfIIB8LZoWsX4GVx1OUdEkLMdhZODVuR4xrGPHVRk_UIlneFvWeX8ArEK1OmjdkQID8eUcWk3qWiMWfKTnZn-UVstYSEghB2DSxKzu8cr18KrlTzAIJOzcmkvf41P08zTPDo9J5zEHjfQqDXOW26s0czM5QRI0vm9vrg8Be2TlgKdEe-acglRHvdVXPfTCNsBfUuDrw4QRDd3kXgFe3ud3SSFT2QZErEh500ZHNoNx-tRMNsSZ49WA8gLKdPHGFm1KseJ-0dyoOK-ud0zMDPICK0LkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnadadgBaV4kgchcN_xWROs2HeEjYPvDcX7FQIqzBN213xmlF68OKGAanxUieF2boYnuX55fwE7kxNNgfQXVzjtenLw2MRofJLUJncVeGQdjqsWAenbqvlhL8shrAb_9gU49vsYcTwM7ggmhqtWG_-T4QZUjnmdhdYceJoHipWoJauSgav12pUj_iojb52c3IzJI4ZDTjM8RGAKTSr_Twfch5JNxfYwJg2DDK0EpmmzOm1mcalfAaMLQdqdZEenB5qG4J6nLiYmPdDiqR2qiob6ulaJ_RQ4Js3tAdDB67CKS7PHcso83VNVOI_NcRPptQ_u1u4vS5ZQJ7btVD-X-nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YSyQX1UqovFog5PUH_mp3rte9CM1fDp___2U2iVy39XWtpCWydwYZYg1DXyLxlXrsezL0dQAeolXm9iJSN02uWBkqZHM_cf2NMLBphXtq-MWbtYDX4MEi6ASbvHmHjspSTy2hUUnPYWZMET9QF93mguQp4NJr6hMCHN-n4hV_LafN1irlKYHlr1TvUhYgE6OHm-ZQq9UdB9vYvkMG62-evbw8OTRGZZ2AUlOFAF-oQVxVetj5hMuJ5Ia6jExXN_YBWktSFgqNvuIRCc1-LdkY_JSEvI-CvBkzXBEL626G7hR35qKRg4p_udCS0pPv9ytI5ExAcEXQIGCkCiFt2eZ7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YSyQX1UqovFog5PUH_mp3rte9CM1fDp___2U2iVy39XWtpCWydwYZYg1DXyLxlXrsezL0dQAeolXm9iJSN02uWBkqZHM_cf2NMLBphXtq-MWbtYDX4MEi6ASbvHmHjspSTy2hUUnPYWZMET9QF93mguQp4NJr6hMCHN-n4hV_LafN1irlKYHlr1TvUhYgE6OHm-ZQq9UdB9vYvkMG62-evbw8OTRGZZ2AUlOFAF-oQVxVetj5hMuJ5Ia6jExXN_YBWktSFgqNvuIRCc1-LdkY_JSEvI-CvBkzXBEL626G7hR35qKRg4p_udCS0pPv9ytI5ExAcEXQIGCkCiFt2eZ7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRPY-RNwRL9FH-_aZbWmt7AVDfJi34fGpFb4XN5rAu2l4oNyOkNLZZtjoGSqicJvHi2xjt-ZkDAtTI87SDyUEYeUzoLkklNNNIurk6K9rqj1dENyS_MEisHi3_j4rS_7NSsMFu_sqoeTU14Vj2LodXPJ5Mef24chpZYYc7UiokS6MEpbbEqRk083YCy6X382fdsh5VqpEFq0Muy4dX4O1kf1O-Bwj4GS-H7ZGgZzTjxu4OVVUpMX9irYwxZQ5aa7gdswBm7vUe7p_kmHIJWM6iJZeGGGsEz-8sl7RxgubEZLpPoduYAztbixnQ-70QxH6eAkSz3B21C9pTGdXrWS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIfTUiNUMvJxGKikzA8EzarEQO1mLcbuvX_8W_A4AxuVQDEGDwtb0zLGcl000XnDxAaszF7KqDRfV0Q-0iuHSpN8bpeVY9lDA_dKFH8rG_WnaLK1fjUaiX0mIbxVoSyBlXf0qtKPLHyF9Li-JQeRt6qq66cJY-250ajY2UggHxxyytN_O6IPJMBAuipCtavdKL23W3-2k6fIRH9LFjU-5okJr2_7vBs38FGXsIK80uswEm1-q9ZjfnsAMqtseSPOBYEKc0ywd7bXsxeR4aWFhyDBaETlPfWu0xyHUzp39H9dYifYl-M65U7ASSU1nEfh8ONlvdMDC0Vx_gUursjUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
