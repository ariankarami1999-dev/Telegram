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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 03:29:46</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQfxsTQRD1nT996AzZtqP76yNlFWX1uHh1LoXhUR3o3haLD349HEFQEBJLbilOQSjZ2kwrN_2FOlz_KdTGzBY5gWgKNEvvpJSxoIjGKkC9YqRLQYWZVDaqG7apW8EV5rWjuIe-peAgEPAnacKFd-pbGdgoVa5H-Wbh9nkQYXlLoKkEzUHqEJi2DXi-1KP1IfwuFOIcrh_UA8C7WMSciKSaraqSQanKzBJ8lOMwBbnAylh0fDZeLus5CJuIwmmIQmyyCgjsxRbC6lLcbbUo6_M7fpWG9TW3hhVzNksswAn1pjPCcLQS2W24OtCTepV0vcvXioeobtOZ9Llf6pPmvVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 290 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 511 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 628 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyEhozztnQ2CkiYC3eZITlgDr6qxYxg3EwWslEVSoqDJCb3_A8XClFp1IDD4LqQpyW2cc7e3Zbi1ElnBq-vjwRrRTVvfytxNSi3PlJz5JMZdEJ0_d6uhRJbO5JwLKellZHMUbNVniiS5FwNV8xPOmSDpaGRRaRU_jevFPMYOO2zcLb-C8UFRu2Im6qhIe8bOjAcbEDC-c1_KzGOGx8V-DDUjHiahasHUdRf8rPVjK_7gnaAna7mvALbEfacNvN6sQynsuL537y5yjmxaIKYrmCx1wRp5qL4rEtKu7H0s-ok2US7kqRYEkW_zMp-LlXKJ30qVlbtFpWayidJX7jLeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuRwQbHBviguNOX8xgj02QvS8vdRDimbMM7NdkAszWY3AU8HcOigtmz0AjSdYKCgMcTf6vgI0kI7OVXZ5RYRrPx7CKTT2hsqDPQgaP8cn3QDnaADFRGvrOmftreO-szfSV4gUQvomHLUjPpnWKzPZR2A1vQwkRP9J07jBdIx2NldlaYoWbo1bX4y-c5M4-hR3QnBVoRpGqSqGWoZ7FybWe6OmZBQDroPLCCMn4cvD1nm7W3uoBL2L-JSHECtrYefpbxZDsg3ICL8cdkwhWK6Qi8NF1J82yVn5vnlomfO45Et-0OoaFfQPtiFBiLHxurv5df3-P45tzK3hDrKvVV_vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXrGhJx03AEe8glyJABTLldXLuRYRPaQbfASoW2DNKvWVRturg3zCkuqhs37n5QXiSHOZctiRAHPfd1gczb9T30q77tWto5gFvAkmacyRMn6HehPKgiOjbGHbZN_Pqw5CLuUC-kCnh6PxZ3xkb-hF2_3eSLaWQem2abqdrwFHGTOpJz0be7hNwkHoIFDfFutsl30snxA49b-1_FFFvcL6wQWEQ3XnoQg4RZakXs8mBRf0YIkZu7IYEB2vJXyj6oSc4sJqSu5QLlCa9Svr6p7T16WmjtFnwgc6sgiGOkborjAFFmrEedy1onOFRyWD5y7Wmr7oNngmlj85SlMa5D5VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eg-8j-2KYWbCDUuH1V4U8L-ZEVMEqICWutNw3Mw4YSbE3SKuJKlJnDZDOFrTjMzgq4rxTQ1iGvdNwF_n2CkJbSAnA7Yhhnl4_IHRZ-A-o6Z9d5OyMq2h72ensJnV2npn1d22eBcPgs-XcfEZQ6_HuzJJ1OiUqLaQxImPFIgvk0h_mA6gjjdE91nWX2X65JcL8-3_uqhb-vWGsrbo9xjI_ilaIZj3F9aargrISNPeuhmVZWvaTXohpFwiBN0fG6-_gjdHrigI8AnVs2X1J2TgGX9XD-fP5_Z7AdqTT_Zq4dtGdxMjMXgLAsum9Evfsw9c4N5aYUylxhRMCMuPIl54GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHo9Phv0vYWUQW_UWIAApveH7exLzsU6mTSFS_s-iI_RElxUdBdVcuDiogsRZJKvExdgUPBlXrU8iYf4caa8sCvLN94g4IBllS0xZMh_DiFExddEJLK0KlQ6R2WYaAYseu6r5zGPBBdekL0VcY4N6S9L-d2vdZCv8ytdccQzHGCtEsHz5-CTgQ5PokAbJEUX2uAQOuNd_GRd1UuULf6k6FsNY1uGisGkBGIvr3Jukh0gBiTq5Mp0wy3F0akISXZCgW8l1aLD7wL8hzDGjipXGjzwjSh-p_JLv_S26CwnXADRDDX-VHK6e2lGMhJAIB9n91Ndsgtpl9qIm5gaeuHnAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFmNKoJhl3xIpYAp040mXkH-iRZOFSAmwwuirLLs7RpoQFAflybOwuyjhn0NHam0d8O-jnuw3AvtZbLJdZgthCit2FIKJ49z7La_d_KVh41ZnTR_CBwBvVFCRwxnjYdqJNxsDQyyNszRJ3qk1XoFq5HoazPoEXLojb-3mECLCdQ9KVTWwvXAHVyEdzmYbG3IdHJRHXYaKU6kbxkb5Ya6UUv--I1BaGB8Clr0yVsVNVH-H5r5Nh48fKfxBkusrfOO2iBGeRUth8bOq_3MoOMO1_-YT6wDKP_5-JBZr2X_RHFao33U2xycLobc5jeJuqrD1giMZ_QuSG1ZxTFGdEO5tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh1ReeuhyDuY7OI5bTsGGIOjxWdYY7cqLp4gxWqZAMWf_aiiL-C_UNXjrfLd0ZwdCGS3a8_q_opcd6YFz9mMF3a6fQqlgKAfu7SVIqY29HlRC0mZbqS31qV6HdJYfnf56Df7mWczUBMTo8uJOGiMiinPpQsnvienf9nBl8FhKLbHGYoBd6H-MYPF1TgP_q-WSvTHm1N1fh3n_gGYyVLXbWR_IRNEVhjVrYy3r2r591sl5oSl_nxbyZMJllOXHPaU_xOtkkUazQlKcqoLVDe72SWaYX35RzR779UgCxhLvAi85IRYycMq8r-IUUc6uWyw21vQY5VcMLz6XVdm1WSEZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koxE3OYoVZu_IMyDHFQ49sReVdmdLl9j8x6ltHlWYCP0BcfouerzQjssD4PNpN75qFGFhkDnDnZ0jIcTaKdsQEzHxxLgZvjBjzPbUNEbIhvihCBG49_9eb_oa4Hc_p0QsoonGCd3oDvhBW6HgWgj0kaUrqqiRxxt9Xnvb1IOKwz892LXi8DOmGGfwUuPSe5Cq4iMOiqKA_uCZF3-_Ip3gn1LxzKOngMmrpjD7U4mMroxTbe_KhC4Zi4ihHAPcG0rFH6F6IgARaLtioVOxNuC-15SJiO7WRV_1En0DAXK4P1-lYPfgeAlDJXCDD2NhLxp4fBJv2SXsSvHArHD5teh0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 687 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3JdXFAI8CSU4hilts6hIL6u2184q2H7Bdrp8-UuMyWJ-ThOgaaEOwUN6y172GIjatcGftYmjlOVWk0rc6Ki0_I61vRpc0klQsY8olIAmV4FctzlQVLvmLGSwnYlfKFcDaQMXHkkgkpP31vPz1D6I5geTCKu0dSlVppZ6yEtApNYZ-clwrzmQFxAGAKY9lb_SWW_sfA4lOcvffX_WqGQuZhS0pN28e26Fn2pgLgA1xhcCUEmOVYk6D14I51zo-mKjU8QcjoOFXYl9pNFXiMcgBuOosi6zL6JdGImDsV1E9iE9qs3plNMZWLN6kkpSK9FiCWM0H1TkgpSlpbipxBGsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TftrmtLNew6ucqjnRIwK9pLwGdht-cw4PHu7WCES2d0dPlycSzSFrEbD70COuzwM2S07mX9MmAgwi7s4WXdVds2SuDQIRHr-fAfFjgj2hMNPNVBKKUqzkrc3tfAFNEfNQC_kc0E12pvEnXUD7hcEPD0YcUHWQWN5iWrvly1OaXdY6-GLXDIXbiRHYxtrvWmV6Cok1YAqGEEPdfUrgXy-sT55XzfJcU0dfISLkRUxbpXUm8SQb3Eh7i3fJA_BW8WTKBie2-fP3yItQKpY0VHRcyR1D8psHSnBQj6Fd2qsEv1CsW6gHXInaT_6BCvoJff_wVNsgnu1QY0Hr82Sd-F5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zp1UyPAGqS4R8fv1xwLXQPYUA44aLc5K3BM2Tsce6vRffNMh_J_wLXi4ikJ1o7p9tvQBXwhBdbFxKXUz1SqyOo1m1lqj5HcN_sOXk0Jz6CKCPckuXu1lcJFJUrT0rmVtPeOeGrt1KJSE6NhKa06a6F-1fXs5tKIIfUsxJkDVNc9OTlvYFRSGxSh3sB-ytlajjkqcMc__o5GfYgjsYRAK2v5K3XNWQuYf7JxaLGvYw_--cvV3v5wEtxCAQz6km_oh-R5Fi2zG0vdfiBFyENIxUAt66ZV15OpTLHah13rMnYjho6CO33kiB7gKDbfQDp7XG9KJtSDuFG5qPlTKPbFPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXRdRN1aUMLBRJKbHdyfOhMJDMgCevdxvhFshxi9wC1T5ebeCRrpesLoCqGO1iWcBBTsnPfC489vuxPENzyWiVsOmAP3AvSjP9l5Lo3MyNabqpG8APTg4XmKpIMaPVUD0zGzJxuOUvHHRCZnU6BK--9CUbXPvUWg3SAADgGzru-AV3If9pJnmBry-LDa_QSj5DOqH51HYU_ZImqvpKhExYg2-nh8qN28HauZJpWw7ydBw5e9-lO0UG9HPohOuY98gcHZbWAdF5kr-kjkiTbE9J4hWMqWMjg-31-a1gSv4k3RDaADswBBceGZVtpuDEssu_EBpSH20iow4xsnzeMXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ol3WBH49h1sQGbtzQjWaO6ZXpH1hb1tqAsaBYqWlcTIbzlFLQ57Yszw4aPg4HZuNWivHYrgW7vb5lCO96HH8wb1jH94KyudYAButpAYljVB-GgUiZEIOdDSAEFr72uG_8YseyN5Xel3u5Y-q2sIppdHMq4aYAb1xLrThiddqiDJWBpqrPuewUjSDOUAc5viJ9py8hrtzGjA7lOMi9Hz8bt3UqCDJ9IvFkgdVBNmzqPxeFeJkP9UfXs9ucRjJj77vZRPt5XafpOBB6PfLkF5Bs7Rlf2nmHamZfCI-ZJD74fWqaKqZXa2p3lGf3HXHT15-JYZ4rMxSYa1X9yt-ka2WNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEJKG7Vn3KzfPYQrRhazV-1mnA4nfl-6QOn8zAJK-KaOtYVonclXOU9mMGrvli6RsvTKVRM093kY0DGaYbAKE0IWRIS5E9ZGZboE988opIHrlSkYY6bHHvpiPOHZDASRO2T4hpdsbgzzTIvWlCKGkP2ppAaiV3rJ-IiTibBm0vH5wy4NnX_08H4i8brFyolXvlUYyvCEmAAePMFUO9AqINXlK05VS2tU9WYOoVwL2dvmnl9RK4NNnzl19fTQiDic38VktR2mK0DcqN964vLowA-aIBRvs0BzQY9Ub3mBB2WF1Cfl_JxRumsVcfaR2b53Z2weMgUTHdrRwWCdO__vLQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Aixg7VlJGqUDIUrmVXDPGjJrqh3WHSAabJ2yI6aDyYQ0bL91K1uqVDMlN2YVAHhKxU1aJG6WaEEDVx2AuKJrQrZhm19t0u8Jvb_wm4K-R-3H0PUhi9sKcKXMsSC3J-51PiSpgld9GmKty_PtgQF75aogjB4MpNlZb8Ph3iH4j9xQwVgoYwwc_xGmS89tImCKgi1WmDg_FJnj37ZNj6cIHjVKBBOrDpBz0OsUri3oOEg5Os1cp7aogDTD7bwcAl21D-vfLI4JJQqESsPXUyncw3Owi4EL6tCYPTk27YGFTr0CGbXHoPN8hOOUz1fcwBCJ1l67qNbC_7L4DYOX34IgSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Aixg7VlJGqUDIUrmVXDPGjJrqh3WHSAabJ2yI6aDyYQ0bL91K1uqVDMlN2YVAHhKxU1aJG6WaEEDVx2AuKJrQrZhm19t0u8Jvb_wm4K-R-3H0PUhi9sKcKXMsSC3J-51PiSpgld9GmKty_PtgQF75aogjB4MpNlZb8Ph3iH4j9xQwVgoYwwc_xGmS89tImCKgi1WmDg_FJnj37ZNj6cIHjVKBBOrDpBz0OsUri3oOEg5Os1cp7aogDTD7bwcAl21D-vfLI4JJQqESsPXUyncw3Owi4EL6tCYPTk27YGFTr0CGbXHoPN8hOOUz1fcwBCJ1l67qNbC_7L4DYOX34IgSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUNTeMXZl1lyqjUnFcezRnKotWMDGUjhgZ0wH2PmlbApZePy43GU6ot1iESHbFB6TS8i6dIdDaU5Ithq2QwLclcXWxAhXhRbbqzs4c4W8Zb2TSbj5rEnWDrYyZQQenwq19tr9Kf7vpxpJctDKMTMOlbJRsBU56wBcnyO5-u30heLgzZJ5T01MThS90ZDagtp4e2qh8Pn6X24yCWzrpBbnxkNxeUzCCKifYO8-LvqdubUQ7Hs-syMHldUiUetA5zS8737u_BocvSw6IgCJIPPwYAEiV0qDC48QpiDh1n4jSNTyTWGYH3fgzgsWpGHqAE5ZJM4n01B6L26WKS-d-aWOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROGCZmEsQ8r53GKyE1qIl7xlxfvltjH1SHb8-zkJBXwU-I7O8cD8NALc2YmoE-BNU97WIZqu-PQozHC6-WyMASfSekCI9yX2znpY3UXsB529cen0NZdxqSla4siFk3_gMEs_bu-1nJTDYTdFwlGN8s3J47T-NEEwqeAD81jW0B6GmP9P7SILW07p0AeadFKZuKcx3G_sgjl2PzWMKmW2TQVrG1RtGBzKzOUBGHeIUqKgq9rx9H5FP233_nd_wUKLhXbHQ-nqIN-lmuQ89sLVB5X29m3x953Ff1zJU0SdHmO80QruDywuD8BlqoRwk6FH597j00eeOCLbVKLjXRMcug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aS0UwunNJMO22D3UcllOBNjO0-VfslcKKppBmpHd0Pav_3rXDjHzQ2DOqkWw27SP-1zSDOQbKvzJR5IpZ2si3mkOghoQiy-Dtu5xhu9fW30t3vw81vmugTmOaxrqNcP59nUV9dashn1Ho3thC96H5XN3TT2qA8UzhXDuA8LwV6nyXwWENUOIBRVyvPcpaEdv_3l70Zba0OTKrbrs0PKGhAiNoto_c09TFScYQBpCR2GsMI0Dm2p3_wR_aDCG82-WjtcxJWTbryIQDXQ27RKhA2lrdRPOK_hXNC2WSytQDvW3ISCLFGKQfeby75dnzFKO9MFlegPxYdczLmloMuoqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HT7NP-sbe0fO2h6byKsn1v5qPwbtZFefHRDgFdZHqxrxUtRyEXmEyz9dhOpinRCOpYG2ezd7ffV0HEiK7_qIYxrrDu_mehtezym7z-M94l9CqWNx4_S73EirMI7J66ez2Y-wow4AL9lUYKG2OxmxOkXy5QYE63_CwEhbQ2xhmQubaSP2fbBjDAeVoBEScemG14K_DNvC63iZL8mgARErhuuEN2zGS_XHCP3svFz_5AN-vP42hOcZL1VQLhdfuGXhFYFthinlR7q4p4NA5uF3S0I7kNVw9mF322apoLqxeFTfA0CI2UcNkjT1690sqPqoFhsbZWfBorf4Y3yTw-NFpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYvyS9NEXdvZ8YUUtOKs5jQ4PlqnBw7B2asK-3g4KjN_DcIVYs69WooeKhDsr6T8ZzsDfvry3hNUZTPvSg58GLbpLBI0jpCskPdSrf6w-Xort1ijCO2MXq_-QVlpt3szAtiY6RvZU9lTKsJg1-MOHX-BdlLLPKtCz4qSci_lom_nFFP0rD65ohpGtYl1EHllMBWPGOn-wf_VBurcgZyawg6T5iXFyaAgSyLzmPKW0HNBzrA6yOK9EN2rmFGPIHhtWKxM4Wx9HT3Jgtpxbp4B4cdqhkXKrMmaKkdD5YCyxx0mop_rC0zyBkJaJwYEo3aH6Ujg3RW_JFIqlNm3SceT_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0eO4rEeRZWQrUdPQJTMHko4s_gX131AKiYj0h4pBjwIuPIPuJWamwS9NdBNdUiEl7tBbI0y_YzQw571DJp43SineBz3jN-BlBmvPX_pwi5zhZj1yRD1By2KbKdJLFFXD-zFa7o22cRM9Rvn6msQ04J_g0BSf7Rm8mFJtWVPu4EdmkowEdVfPuMJwslcqSNQgr6P8o3kvsAyr8iD3kp01g6u2Oq80x75gtvaPf3FGtEBZzhj3D-X0OGEMsHDRBV6ymEvLVtLmyJzsMk0AULOOyEf_8BZwYicSBEZtmjjYCq26jwh2qAblyKDKaMMs-7NMdaICMtprbJcHqGFzEX_CQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4cFlSawoltmVVjqt7gI96SUwPL-L6RuuC_2lzFlRtzuvpbTM-MP7UCYRFDhe5Am1ztUS9cLa3JcCUZnfXmlD06MJXfGsEKN65cocRohlBPftp-Ne_h5FtTMGh_2zeWZameE4T-CtXDLfjNDewRci261bOC0EAVawT7jRjnHoBtzXZdpXdIcZIGgYRBUbqC4HVn7Juq4zCIIuAUmmxzKV6hShpUGvkUgRX3gRJK7sjEzqKPaUG56HQo48kJLe2J9dW0VCYzt-vVCvWlWBXOhAOE3EHP0H75eHayNnayoNCPw_B2n27_8UL9puQb6rL3-vzm1uHSVEHN0jLTPmakQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfXrWhdO9_Ze51kXpLADdvJSae8HGePCgm5qWY_5axtzOQGUNrwfLcrOOvpSmz-63JgLb0qbShgCyd-477XCw2cy4BYX9TDz2Qnu76FFtEoYzxGboKrwSf3E785A2pSd-TWROipZ1eUDgiC-bwhV5_XKwe02g03Cumrf33W1w33OoVGPKR5uaTellZg_cdTVdO8XIsttP1xvCE1MF4M-y6DgadkjxZMnI8H-pZzhnauis2J6LG3KatGfVGQayO5Wbj9KP6VWxkSd6T6Ss4JiYhrGIepabQ7uVcnqodmgIYH1NzrdggAgWo5q0-cTXAI3Y56I5TafSWT40SYbGPuOEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQZhmhjk2E6B-YkiePw0GRvk6x1HRDdDyLfeBaIA9KFfQ79K5H8Qj0hMFkiU2GdH4wleIaETlI3M15FXe1dVV10eNDQ7tYluhZvdPYSilSasWuytxigle988Gg-_-iG6q2v_UsNpBCUXfK5TqTDp65jP7K2mcR-rucA86ILd9wrZN8HKumcG8mUc9HurwzL7B1VzNKOzen9ZuyNQD7WaFkCuaq29r8GrR2XCt9CrpzFgvBaW4cSmKPcb_U1A_8mGjXZ6ez8Glp0k0mHB0jMbUMbZ1iBRlHi4XUo0YY7fxkorfkYM89bT5Tl1c4IeGLu6XlBrE3iM7_kvTruwYfFHJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obVQG8rzBG8RHaFXn8moeP_Z_r2yetLTmBKKboaJrWZgETVtLHC4x8R3tJqsk8jGZkr4XxScMAuP5kMdzdR2lFQY_xwY3uUDVF8_4cahEniEUo2SobITe8BpzlG_OoV5hqNh3JQYSzCo2FTbTMReev2GSfbzjmxJqUOP1ThvZjcRNHuvPt2pbcPKFEUDwa2JSLsNd8IsucCAXTGwQTCZb0HY2Ix3A_EyiCH9vBo9_95KGsyY1ukdZn030VgiQcdBI5HOjvd1ZFFXx0ANb-PPcnEpaXv8PI1wlD92zQvSVwZI0mjuC3h5OtdN50AYMP7RiORbbQYgHD5oOe-SHabiRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8afn-lvuWx7SGa_aoGZYOqe4C05sQwde9ggMZVqpQSHOIMpta7CcHdU01gmWwg96B58vxPzhVQGH8p5JINlujJ_lfzPhhFWoyukId6QMq_hUZseY5UApZNz2U0hM3P_5icB-20vjHKp4eYWek4xChGNio0QHQ7QkyC21R4psUs9hBC9JZuW8aRH6YVZnLJRWCCCLDmmFr5aq8c3tvFI0y9piEajm8ZdBA4_lQAop1Flx6Xl4aMjNcNCIzG_10s5Z_feZWyEEYrgDVcO0bStH0w3WNJiyrvDqgFmtkkRzy-WJbA_1GYca-FwJczR8N3QXUYa6F6XDG7yZ2g9JxYM1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL-i5jL63Z7wOWA-_Rb71XyD36zQcET-lEMLVRYGvagntiM7avv0nQht1FPjiKxypJL4BUCgCVxhHfVoxxBYoeCDN1fQvi2V1wNd0P961022R2CL5KpahVwgvzH0pH2N5ssT0V786hej-PEtvDFgaLG1oA5h-xfvqQg12326D_BautpQU2GNl9pWm-izwYdw87AaIF3v4Or6TRzNTZEhn16mkvOeC3mym8i8y0uPfTjuYocvUctZDsTzPDR0DGAmrZ8NjkDuX_7cg3WWHYb1fZRcAh8pXkwHE8FGzp8hH0ZY1L5fEDe0xHmRfOpQmynzobvbFH8Oe3X-6YvAEx1NDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-rNaKYjQO5neSTLufPoGFCVL2dGc1NgEhNGGZu1_ptMD0FYxOyDAOcrWZFlDyCR677x6TesNsMgQ8psMDQYW_MQx0czbq9ft1bANMoW_3-Wv_m3kKCG17EpTkHP3njyGNnT-FTxKLuzQME73sDPoX1a_WpRhnkFf-lBICDqWxstV9rA8eL55IG4IAe5Yc6LT2ZkzgDBzGs_fbB8n9LhFIfsUZxxUzdys6kG59PwuV4OuFZvFPOog9cW3h2d7cHAjcMmwr2i25fTygIVoC1MnUi1pc-cynbSNTgU5FqrLW9nJcsfiT2CgVlB16Wn2_v5tykXyOCuysEsKuKm3v9jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuhowOQijqrMbZWhIHV9JREtTpkqtWotZjDGwTZ-gMM7guJfKkU7Jb0ZTovreyxoI3hlHf-yZrp4kGjt8u-OaqXEGSsNsDpiCe_U14i9cAjX0TEobfZQBGwFwqIAngsH6Z6VHP27vslnaw3EvBeV1pEsg5IJrV7J7M6ACVjpGF5o74yPr-iNg7v0UMFGwVdogJIEOxof67b9_VflU4H1kNT7k4HmiaGdAdQsIes2I5aW1mvGaVgdK-80w5nkxMt9AJ1TY1dX1CN4IsVUoArkq-pDGUJuzoECNu3aAcGXzBqyZYuYwr0LnV4xbL0OCQHU0S1CzTHZwnTKJT57kh_xSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJh3tmw8KntVTk-CLT2kfwqq2RFq9ilOrT05aC2QUfgAPjD5G3TV_Q-LsyYRJJjigbEnqoQt6L9j5HGGDQ0rHyLmAQpLw4TrPIVSLqUBHcY71WojzCKgpUCZh1l40QQyFd8BDnC23iarB00BUU11zbjZiNZxbFBGcpfG2BdcLU7NbeEAsedAKuSgJUDh2SuUj1d4S_PGt5mvJmR451uSk05MLJ4dpUDNNOBfGWpLxZIsNoJd5w7K36JS7IfLj2nroMfhpV91Uh_VT22F73vS2p5a1VlBiXp-yC9TDcs0YTbsuiZCcehIkX0XTr-84Z-dlfHEK6OsyyZMnjXvoY6QsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfvO12d-r08BouB-dFvmswjiCbToLit9jJbOOBk4vQC29Y6Xrk6nUWg-xnA1Fwrx_00dlvT1KoWENPiLhwmu9qGd8aAeNj9V3IeshakHwN73MDXIrwizNiXMRQVMZFR0xMc70rnKzW_iA8qh8wJTjMLKi0orJ27IYDmtzTdNkTMTOgBhcwpplIeO-177fBfcM_rE-jvwuzqUaZzFnIFdikTBWWkwq5qhzakkK62RuAFZOo5IKGKEoZpECQCpqYz6pucugpDZ1mpT5BYbrsmEdxDTwL840t4yqg_hLf0QtUl8OwPh2H1uy8ggDnmfM0aO14WC8DOuDPjEgYPzfIUPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlAMCRgaf5y2sW_NUXXAJ-Y6ziTcfYC-5DRXFoob_UrhOZA6ZldhyZi6mNfXGjIBeL6k1_4N7QWLvyXNHDunYzq_8cppm4TykpNpnAO04Rd8aSXOBwrpM9BRVO31_bJ9B_lKNYaDxStBuRrhvLgokbMfqYyPPtrTs0FZM7Pna6uikWDigGg-fuoGfDy0XtKsIwhDjAPeOE-mIx-FN42MrjpcAaB1q63hspXDHGvRkIGYnKCRSJLmUKltuhk3Kbmvm_PDvT_3gSmJQdS5pl9iHRRJ9xRdtT_a-HCJPvwdUHTZOIiG5DHYwUjx_tk1HNqRPnhiPnLnC5SWxIlsWY26-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnss0QqWqyM1tPKS87-TvpGt8YIns9uY9CMCHTb9UTVmhj2LBYlQynBCttq4WiBEu1nUGIBZGDt1f6Oaqt1sYSXwiOUl2Gg-7Phwj-PfuoYsOfaZlZqsfEyQDdiJwdh4XvDgxlvQsVMSJuPulpAH082hinIzaIOnsEZgSMBs1FBhvf7xR5wtQHWrFSqFzGwzvfl5ugMHhvicicYUT2RwRONvhVbwOhmVozUvLQpZjEzJ9vpPCV0fANWxEye6FHv3YuTimGNuVtSk5jTj4hDcfNtTWFZ9Ps59g0sXXUpfs2vsCfRcf4KLMue28uzULljSpfRqufsyRbLVXB6hyL6wIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSKY4z53mbMzqXmXZ9695YpNOGR__qreX0kIk1T6RkplzRLBNeUSoaQXWjWHXbgZKH3aFiNV5PEXphx0NFhE-YrK6J2J6QHnAlRtwBSNQiRvah32g53hj8qBnu6or_wrAGsFeebueTxUC3UIcFYGkVc2SKoPeZ6yTeBroc94lAFQG9BsqmuuxjKXaGM11KrshZH_zV800y4GeT_eyxRS5qESw9lraN6O_YL-uMlDTMDqvXwHuj7wVIfoTOCwqSWPfw1wbQcRBqzPXAIvY9HfVIhi5QbWqr3bJNfsL_LQdBtTLZdpgXhLJUptHgR77Cltw4ImPxnvUHdExgzY9kwKXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqtqxdm6kHjl7zMiMlj5-gacq_s5GWNxCDuJIhigKRos-9ETGNfhaypOZSVLnNfEMFA7NcQ3snFl3am5vNSBGPyH_keClnWL9d_wP0W7ALTAwTMv-8DE1OzkmiPMoMRiYY35yKxmwd5Fzy_B4SDorXRS6bnFXU9Hvkw4dIRe-0R3Qxu0ugqH3m6OPnTGg9Y1lMmzLzyc7-v66Bsg6VCfr2LHeVoZEkqDaEEejKkJhcUWrvoyiBdwyrv7j1NfIErE8C8sRIivfOdr24wwATeBttzxPQjD-Y5mW-5SmWzPXNkKXhe6bbm0WmxzXjsQCF7CsXENOUzCBvCV5dkBDkM-ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtMsGMB9atoNa_NtsgN6A9UIVCZnXi6N1Pq-jtcs6Gqy-Sdbs-VzCcyFLaj9y-Pu2hTiIToCY6jQWmj3qdS14WZGoaSNFgI1NmTFoKJue7iy9V2MshaYsg0qMkQMTAKgHUJzNkxDzkrEDo_rcASsDXXHat4_p2fQPFFAzuFaKkqiizgiUrp5UlqHM_dP3lf70Ipmxc4nT7drg8Quc4b3csIvS6YviSZ6q491gFgJiVTsRRivyIJA6mh9cKU6yAL8hDNKhrDGIaT9Dst0JuqiOKkoMGzpemBqxSAYbpTjNmkCusMEXgH-jBvHxqdcx6vrhdYHwSEWUTGK-lNJPbGjZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th_zrnTlyYYwfTIB3q23q1-_fH8fX2HhzYYSBoi8wEmh7VLUnUVdOSxbfkntI-LaRuxP17jdLkBdrTlDdhWCu0qkPd8lyujGsCh6Vuq2KPMktuVqayNep9FriyES7LS6w1K9EEkuahKCH3OOVyBThAtZjWMpGK5STmscHdGFhvnRLqtU-uSva4Mpx0Ncuu83seOvdvWqWgF-PPr1zI7iHODo25SBk34Ld1HeL5Gv0-szz99XDyodG7Ad_WG191CnczNdhoNicg8CsdAu9li6d462gMuZKYwKWTfHtG62iaocbBfifVD227k8h2YrfzFRfDcCHHFssiE6gi8OplNhrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCNrugkwYAiM04EyfLRU64-LSFtxLb-oWdOgpjppx7ZQQV2oNwGLeApWxVJgraV1QQ3GqOM4TCJGbXfz4aPRtqiqqsBGFiw2y532XUnsc1D8cxW2MCJ0lRxDz7FNrSXqFZ79uAko6TM5LsKdR8w3cFncmFgz_sMeqVgpLOPNu5GQLSqMdME1eDcdGZ6vaAVt_gh7yNP8fqmEskBElRBuaQMgvbB0bgtkE8Vv2YjHXIl0xJKSv7FG-8Tua60rrsrK44uQ6m4qUyozVAvdnqENXrEIF03jLCOWGU2V6YQwHcCfB9ctdSsEJzi3e-884zZm6jmwvaCwDF6XDjfAO-MnaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRk851dN5sHaHQUtEQn-_Zg_cBXGF-A9Bt89GMUCdo1I6FwHNSfAwKH56FJiJb745jEDnZhz_sQhQ-sPrzqXnMts8Nhf4KqAoyxeHwAac0s823BwrxlQBdsIjIsxph1iYG6JphfBBq-iy3RCsRfI2gZXyDY6PS9kd7twh6inQ9NUeeLxqlRvnhx1-5kLjES06yviBZE_bINKbOWddifajEQA90ugSwf3NiA9RUbPK90khXNljyqfITemkbnkPeGSEK6PfwOS0AS08QM4AZIxvY_jrP6r3KH-4TlNfDi-NGHquTexOlf0W8x29cDpn-ZF9aXRitJCpZKCVc1ovZzKow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-LoVesgWDhNKwTSs823TmQ8dkyqd6iShHRwXfmDu73LqwBi-Ux41ArpD55LsvDcyNep1r0DerjE09NzHCCsfuYHMNDirba6N8HmPwCTsdv21R-0_eGQAIlqH8R0zYYKKU7oNWj47fGRQr4vy5lXk4yyVKXdPW6zEq24xt9OR0bS5zJ8I5FvRP6xTSjXYSMtAjIwE2DP8hgaY_9xQI8px3Z9E98Ra1D1hyiN9VKAWk2DHh2QGUNl2KzkBMh0FPjGlIZfJ0-fhh3o0Hd9N96LXK6e3CFgVg8cAIrVzU7GuPhU9bWHryNtJyTj2CHz3Zy0QogN9F6XOX79w9uZ9ECG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LREu-LjuMVrqcYf-Lf2irBhcGgFnkG4yk3zBLQfPyy7wjrmgbrWRTE1Et1wPqAtlgnKsR6MTz-JjTd6NHIo202N4ebVLtOUO1agZ7sJ75LOBBHXk3p5IKKBRCtvt6jE4dIzcHw_s0PDA3P-QOYDy1FwOyT4VZnIzV3KLS9WdzXjZ3kFs6vCT88ZHYfeRgbDjw3UNknhY3CpkwcWYLPR5h1FAqmN_2SF4ZQK0fo_7MMIIHCTlia7KoLH9Nh5wXQrtNfAUseYn2ba7FC-HKlwjhSxz-1FFQGqkoxovCF9RqjELD_9YuFLWGqh9bwbl6tq7SlactDhxcJsLDYEzEGoRWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Xk26DSFYJdyZ-ek363BRBJtZxcc-v3tyYy2RPEJQZqjbcG8o1InQFGqi4YqAjgP0koX6w672hCvXLal8tzd6Dtg4TS-PFFVZpdOqqO5RqsTr0Dh6h6uA1evzDu3TzeWNjLLqefURUvDMB3K8aCZ5X6gr6-tbTrz7QQFvN4B2BA5iOvhBIc7r8cb0DE8qh_MtnsnzDdDSg2WeV3n6NKtNIlkQplY80hKYAfVen9uBHxI_MPRKFFZZuEIfXQesEcBLVippS2sAtpVSroYUBUSHoop5iSaqi3E7k1lSRlV74_HNRtXETQDetW8rDZcTQZOnwbqibUP3dktUldeYMFxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX9T7wEL842sbytwR93ThUQMRxTadV049O0gyh-fuoK87OB5Go-ioee4KgrRC-r4ERPHG7swMd-CqviBQpzv-zKm17bO-EJzKhvpPPSvoor-J9MKs7G2dfpx86kb9PAFQCbw1bzXEmm5_8ow5oHUrEHehBS1PRWsH-MzdyNvJB52XZI3zsN6jiAhulYOGZCkpKHOHsaYOvICXk82xPSyhcq0s4VRpm-BTmJKCLtZ6MVw_VzoWt0YHZ2qs0fG2LGh7UZE6GH_Y-eL84a7cFFWivSVKDQbqigjn0DR3zGYYvhfAi5WsUQ1hfy-9KsQN0Qk9yMY8ehCCFOpTc9dmRSHgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-B7ibCVHPK3xw2uCCfQpY496fpz5lEIoY2L7vZzx7eDYSjWaHgMJB9WjhkvpRTJgvrDqrXOfD81piGVc6CruXC3P1Ic5A8C14MsGYfKA1vT1dZ4v9DA59yXejwLG8izOAiKF7F5_5BudHmW6w9oghHAw0EM2Y_ij0SAQFGn4Xjg3lqVkxDdb93NYo8CTXZoaaFPsCW-4pnJ4X95qQEJfbHOAttHdIbeOgQVFwfOQBpVMlL5RR6hw-iL2Mb6a9KFM5ixPbqTmjyxwKrpT0A5QuNQ_H27m1vgite_UWAhGvTp2wJWyY9TSWztoTjO52tPGf1CXzR9Wp1-8SRpRZH0Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td5apnQuDgwp-Zj9LuUMJLoVVWudW_QugcvsEOkGOv8sSOq2kkicJk7Hfvpi5wQK4kKHazEH2WqQcPRg7fyQEEu60u_LS4VI0_nOHiaRSV4DTEPtKHimfmaXiSJr0EiuuVPFUBY19CeZ87icwmWxZ6VJbtHrBMwdhZRL24euyKDndzfcpXA5Bs-APosR4QAYDekDcCb2MfRZCFsPZs5Bu3AUIU51hdwbnltk0BFz2fKGB6SpXv5FazZW8Wpk_EsLjcJ6K_bDjWEVW7eu0HKB7P2xPrT3IDuhzPXxFtmZBVe4cZ-ibDoObvqHlVcxL90hQZTX7pc1DZfupGnHoSd4lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwHf8nbuUwDWmPOjdOZEpe02n8NiEWFRc_r4cgWt0been9u35x9w4i4L_KKId4O-aiQJaMC-Uz32jYECIcVoklxhzao09j6WwPxDxM4B-_dIllWiwZqEvRFKinpMqwaTZKvdDm4q-A0RQLB_qLXhBAKBQZcgpWTC7qtZqH-eyug3LGO3khNjzAvs0FEBZNftep5qm7LfM6xqv7lz51meSKs-84SB1bvEDoqxpYrFnizDPSXraUhVJ_Qc1o2scG-eh7Elmny3pCcgHn70eH5rGxxby7B8dSY9AO1o0-RWJw9lWdW1rAkNy2wlg95PJSCmi9xW7_XSJ3dRgWhz4RuVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BByxi6mjMpiJ3rmjI6A_-B3zXNDUy375bav1HO0qzfmjZY3Ne-uvC8bRHDNiZRZZvuMwWeG7QcLmsPZ5LSMVwwUe8IeGXCqUKMMBPtWjH89aHhAwgiX39tTpQPOH7xAqOmDBjQUUkIhCE2AjWLQXQovaXludX3ZZAgmfo9PEn0WrSOi5HWBMSr3QT1i7yplsoz_JgVkTMW_PN-yhSu4mJ3XrZaSo8BRawasUgAqjfXCf6WOj2qK0fvAkw4cNbXh2uujs6LcF7kNv3D4N0OIXRBDllvjud_d09vv71vlIvfbR2IqnPaRuHQCzLt3e0gkZ4QCVlE7O-4bi9hqlmT0t4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nw4Vh-ANThU5BUZSpWloPb-4N80KGZdSguA6aY6QdwTlIYpEwIEuNmTMbN7AJX0actR88Oy5rOgw1QXcD-HBPexfE7DSyOlgmUNsTfO8fsiwRCb7EGhc8xf0talYg_K67QOH5mYleFsb_K2UcecNAZ0gNvjSfWI4RZtRA-PjRL5jmB3nl1K2q_C7kwt_dgXH10AemWUwhg5F6V8sdeRWYmgmyRFpMtcHzB-spbYICFfMdX7Cqq3FIKLJT6cNOmR-deWZPTVcJz3Ik5XrwEUi3JhlLd5ApxUrpU4y09G_85JZiVyWD6D2wQb07hTJfjMOUHfGXGahyZoRQum8fa7jFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWfXeI8JpK2mGsA1JJLygHOItfKvbvo_phdULj7yO-2pulCHeRaKqa5_PEGeSMUf13hfmqdbzqXThwx2O0vltNUntVziNWencENPYCs66IHie7QezCfCbQl9HI6Rk1ku3sekVpxeX7F5PhJCEUvihUBg0W4mgZA7dFJO3qLo0mddG7KletzFULKlgeytZ9hkCW35CryUexyPlqERcpJGmskjlHI3FZC0H6vSXQPNYs_RdSXNOvrIocSrSoepUReZaRuiyBdt7wea0ywtkHhLoMyYEAbRTOVVWxV0eYNPbwvpVxHDqqPjrEIdG3C3yGhJPtIN54IuEClZnHRg_ROKcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFuflWbgzUYUKP76MucJhRdGw2gGNxLF91WmYQhyqRL2HzoTbH1qc16EGe_trrHRr-mjMfOLEi7bjCAaEZwheKjvtIv7TFmUGLE9ioSNtbI748bYmT__72arj-y1FFz-b7vsW2wgA-erNUBWEih9vYu42RattESnLYcVZE6R-0-NJtjdETqbjaDraYLM_6Ma4dkHX7u8MJPaXs-c8tVnVuvla_lpZ2aGHZzP7bAqSC2b-dydI4HletQFZKpT_RSQTC7r9EMI3NvXbDQD8Z4stQ9imNrLu_kMgqoCElGOvTaFkakz9g9q1689FMvaU7agY5GX5OrBRDc8PUzdU1yLPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO1PwHDtjmCMoSxk8D-Oehu0SEb2rpP4FoJJNFER3mqOoDU5X5uQ62c4CSok7TkP7WzDiwOSw6DKRE00W2VTrQTW3wHrvs_mK3D_xajxasHAI0zwo6bub3axeNsJJKacG2w6rq7PT28CSPdUHfXzpriytEim6f9ICAwgorhdLbV4NJs-9b8vuzlhgEbC-_vP6a0lAs46nQDIxdin6VRC1tcB20Tj-wvBRwDkX45j8m1tv7fwCvlU1yGryJrAZncpwo97TlE-MkGII0MfjgjpNPxQcwvk6Q2MtPWKcciuOTxyJekKKPRdkh_jQKXN0RUWdbQQ7v2I6reqB9ufKjrqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EESA4-I75_sPL1FucRXCYkeFkd9tNU0mWkzRaF2jZcxyc8idWMdd0_vbAC4HPpWwsyEylTCI9nZLScN-3r5MSKr_mJIbDSqSCpHNaWUYZR-yif1wOFe3qwD5SF1CP0mKQe2pAIKPBI6OFhSMDSVp5EHeUqoqhRu6tX3F14TrH-yknmWdlFL5OSppCZQSucvI3FsQ4KkUtUziJfIuRu-BqGYvuRIqRFQX7Fr-5w5eKH8nZcHqnaZldyT84-72vyz4VWffLf8qw26e9PNqKYoZtdZbO_k0bcaJFHWAGWR-6BvDHuTcXYCwttpv9zZS75cmx_GrExrNNQ6KETC2SQHinw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfJYjAVe3EnPaYZ2w6N7JpzNSZp2okhB15AxXHVPaiIzrowf_8wf8cG_Z838t-McTqu_XDckWgWD90yDH9_lP2iXLxtvmNqk7jooFP4pneZKCt3l0VEESXAGN4QAdOcVKANrLADPsXsailJA22hPjE2HVGDMPFgmzM1LSE0juHKZT7SrMTL25cv7Yp_eHlzE8BAKlAYvTfYwn4d-VLzJpsL2Wh_T3_5yGRktroYcqZHyJuhAQc8-y6MgFnuzGSV051gOqFML7JaNyZBI2muYNqt6ntfEsg958Zaj_LHMtARS3uNxoelnr43XGsDaR8k6VUTdaNv7XAa0j8WHFXWdww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzkLPOQeBa10Kfahm9qIecmbwbys3GZafumL-_fjZ5LOGN8H-S3_IHUJD11sNcjBl_KwpKRqzl8pKWkK5a1ng49Tq81r9ys9EBD22gM1b8E5_YoZWMDnhQ0mU4jr7ftILc0WwQq_Y2n629lPOTXddAdFAmaHhiMcUDoScqLr_TzI5w6m5SbqzuH2ArTEipHEwKACTHbU7PDQ2TSTcSB-Jlz-RPX2B8eH0KZmGRFTEHB7n7hRNYJs3imQtxF7x7G_nAevScJIAOfPBm-wXqur2J29QQyCBFN0ULmGVdmNch3iUHn8pwDoRQseHLpaUW6WgqnHHLytc34iZqh5vnrldw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTC-7KVWCFi2U4Ai3XtI35Gcz9TOlzzLkvqdbIcQHH-3jWPJnT5jHByYAZBmTuAtsakuuQk85idK_G3kcWCjVJxYwOCrltxQwZj-QGiLl5F6kriAzOWAFPHqPadGttcICla-wO1qWeZQbPqVpwfhh4P1hYIImpZVfhcOKbUQ9hGLKLCFX97LCIyt0zgm2Md9Nc4SYZbRnL8EhJOcuK0FU4k5iEK7wB72nBVHO4x-t_Z6lPlOyDHbGS7TwRpiyS6-SmAfM5IpSPO84QYXc-L8A_hzDcrcwL2ga_G-oicRaI1wGrr8BYDQe3j2r4ZlRSHSjUg9x8OSe2qsyLV2WsDT7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spGb6Dn0GO9KRAEwzgG5Hcwqdu3rsJ8emaiOAQ0adok2UGMCvCZ8UDp0ExdCKgIkk2szsix-eKHFbvoKmYXNvUaV-6xVNOjQJebw8kyj5oAimRyfFlgotRiRZW9PbNLr6nV9QhbEtLANCb2mLFgjLMyds-nRbwXgGIFLb9pzfocfFIgZm9KI-QEDRv6vMYUmI53mw-_qcBuaT-L9hKN_cjJ5vyD0YLIIkY14TqKp0ZiU3He8YplwFm0EcFrk5OI7EBDU7cbMupCDNGAF186lRllQwfYgPLAQxvg6NuPF10AJRLeAJ2r12eap8vY_vGCS448KPArQ9Xpn_8t77GDRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GisVUXrer_ovPKROr5QTkpDhzO0MdZETWXriPhxXYWTKJVMLQvz1hc7EQ1prW8y6a5iudRXGgBoQFo7ohZCVFU88wA0HsZTaJ3_IOjKYEgGnvYaeYmqzMhtGp4lzw71pxq49BQFd-9QzI31n12CcJIFWlsZKI8ibbHaE2D9fJVR4-On1ae1f61s0l0GnjZQ26n76-Zybrf4hHi6X_q2fjOZOekYqkHY2BmeUFChNiy6N94Cp_cI_hwbFdxp0W1qW8XfzAlJLMa8D1iRWO7uzoDbj2vp8V3DG2p76Uw-NDwLFjdbnWp0H6w7ngQuAHhCR760IH4EwgbwD764HIACBlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjkfNhMSvbSRR5SLHfhLyjJ5ygrCek-oe5QvV08W1f2Excaom6aaX7uFQPGiqgBQUjhIXhfbNuSjqjvznsnuMFQ8b5wdPK1I3rBhSHSa52Mdrr2lFzZ6A-Bo0NCpKFS7oUNxdk0nA2LywxEtbWhircLom4nAsBHsV_Xf_oVfn7yw5Rt3cqZp3hHqMbwFMc47KWnTK-H3NW3RlfJaZnpGnFB0nXAXRau9ca8ygpLVDgTW8wuaZjSn1_q_smuDZs6dbk8Md4R2R1_a66m-X7_Otp05VBFrFu1K11dSKD_FPfx47nBNlmx1JMrdWQTJgGiBfzFXvfPlPf6m__-kjtZ53w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8pXyqPcb375CyxQ3f3L-9eCN1YdHMwoB_U0vBvxTDGdpGioNG9aMZIi0ALnxZJ4f0SXVqRZLXx71ivckwjrCZXzErKtW76aKYxoARfDgixf2ugLFowvoc7BvkeqzA40ojZJD2e-pWfVP6tkyGPX8InuCaGuoGJ94YXhXcvYkAhJqSZ5-9Nzr2XOFketcV6eHEdIMIsCmbfmmZEdi5u0DXEfJhGEbi-jKRY6gSUUd_sRansgirn1dEwmbzcLHuvpX9iXNoZuaFpNMcL2zHzwleRHnp8stpuGq-HxBTNkDCUGG3U53cS6URs0WFfBtZ4ZUKhTLk_uY5MPrEnmMuKgbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6tux-KPAteJ0wVwu0mZxWkeLus-HVkkM0MvzSAo5DyX8USRQgocA33yuhwyW1117YkNwh9xREvVKpFI9Kt2ENp0_DeJYdRinsEkMhIxT4-6tGK4_KP_jUlmBqCAhDgIPpgWuPg4zBSJZdjukNxnBebcSn8fCZX7GmcQWztaMcZ1i21SGXHONAYcdk_LDSG14Ckbb1lQ_LT6C5suQz4xu84Vi00Xnsj-b1GgVIPFfV33VIdAAcsFLIwP6jmEtuO-0Nfu2NHrbg8GsQx4PAsLg1MAH7lx6B8xtb4N6cMpjRv-Pz8OW3mLBJynMxmUjpH71JTJZay7v2O3I4-KAsWrXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwGR4QbWcSSEXj-Yc53oNy_MuyrtjmipPbYpU0bO4fTlfbxAPk0srTyL0SIJVasTv7zJd8wKrN37pYqYt7zEp0Kc1sbom-T2Mc87vTH4yd-VjbZfRa2wsu3PP0gTsGDqZTjJ3vDA_DMW5JoRG3Jv8T2QWTSk9RvDN80PwcX4iX9Ig7vnDHa1OjNrKnfgMI2N-NAVTlHmPQWYf-oxi2s44jqLiyVux5Kr68m2f380F5bbGFA5T4myKkxQ4ZefiftajY_nFaDLMegPtrEH-zqF3qUDseYEKaRmWg8miLSa8jqccWpRoJ8Y5tHPCsTgbbNjZIgENXyH2MzPavPCLHX_6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=WuhshI-0Kno8C93kJim7bCwGA394Nbxd5sdHV2isOM0STK6xXOz0C2H34vgDV1V_UPeZdgPPDdyqj9IFXPCg76YFX7kWYeQvyHvcz7Qok7KFxz0F9ZzZorZ0qK4JqDX2xCZUoWJ410dq4w5UDhD4sSrS_mzHAcke1_QGVQX4DSGtPLiZCnE6X0LSPdvQV_5yIiiC4mcGgWs3sWmBRRPskphB4k0vDdhVDt7mX-PMTu4_ZsM0bibF8gGVkwvz7ChsIn0xrZCaBEdtudhTG1adnj07j8TYpVW6TN0Ng6XL0yuKtkrR48NBW_KOYc6Sgubu18zC_mnsySOTL4VRI2ukvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=WuhshI-0Kno8C93kJim7bCwGA394Nbxd5sdHV2isOM0STK6xXOz0C2H34vgDV1V_UPeZdgPPDdyqj9IFXPCg76YFX7kWYeQvyHvcz7Qok7KFxz0F9ZzZorZ0qK4JqDX2xCZUoWJ410dq4w5UDhD4sSrS_mzHAcke1_QGVQX4DSGtPLiZCnE6X0LSPdvQV_5yIiiC4mcGgWs3sWmBRRPskphB4k0vDdhVDt7mX-PMTu4_ZsM0bibF8gGVkwvz7ChsIn0xrZCaBEdtudhTG1adnj07j8TYpVW6TN0Ng6XL0yuKtkrR48NBW_KOYc6Sgubu18zC_mnsySOTL4VRI2ukvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4jNmdzpWwSdinWbw-FXMlpbYcXFm08LqOrsN3dvElEUmGJpK22NDSppVmqudiwJG5uBtgw20ghEBpZEfTLdUG3Bzl4i-6QdSeGhLD4QjQWk0Z6OjNhIHJDgSM1ODk_mldG4EQny5C4kIicHzQq-fH70IU1wK-WBTmbQsPX_VIj2FrgsHd5Q9N_1h6DEsofjbIVTPSiHoSYNpFbdsG_-dYENtCoWlQQh0YnMWSEI21cd-uo64LkdPz9TOD_T1gBYiB5K7DtVjy3rEg6wA9-Bbrzjy4FagXyJ2LN2kc4qEWkAs4GE6D_TZHM6NRNSW9uUtNiG_7M7Yl-xDm7J-3okGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvckY9Cpo1_v23oR5-DpjiThZY_s_6yZCF4W5YKH6C6rz8pUeFJYkz5sZRWHBb5vhXpiwL5xTmqEHygzu3fhB-rsKyCvhyazKjrbTNUah3sPZRAM7l-HvkXqUxt_RpgwjiqMOnqf2Km-1FflWZESmZTi2q3NZ8EwbznN85UtFHGygy1KzCBfuCFNrAKSwHj_IbDD0yO6gbLGOMPfOxe0_a3YcccuQ8S944djF8QoAMAk13ooYh-tfHmYe9AmGx_YyxidJ94ItBzdFQnUilF78L9W66R3r1K9JjmGW8p8G6LubVSY9XnqbSHYiB6cjd7vSNf9PCWk1-1PzT74C4pQKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJheZ0XnCtdYTEtQtlRkpBkb5JKpfZwivw7DkIDWeIix_K9oYZnVBqfjdM2Vci-8Nzpneapk4vuh6qdkUTiJMdE7VrJBMkDeHe7QZyjo96hg4ZhUHdm9p-3yJK3hpo1uGkTwMv26_c9N06jjSwAamxtED2lgFx_-HypgYWYGS1dmQc1oiwDEsyhgXqgncw-X_LAJ1IZqrSwHJeH3GyLcdHs8y_uuWKI7ry_j21gDyMggsRcEXptyHQMjR6DqE-KvLLVDxF-7lJXy-yxBZco7TbM9mgtlN1iy0nTvBt-UlmdLamBzFVBuMhbcx2dLwQAlPfcbRjRc7fmiAtrfszkuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8UjKnesRCRulgM2ATk2LKYsS8NouYDerYmQTrtk7vlErWkD3ntsgVE4ZvhjjVRisnSv9OBZp3e1N588Iild26HkNSMxHpLtwjY32bCxAyPnQYtXAVWAXwwK-g_zxUVIPLUBci8xz2tvBJIThn2Nqdq51r0oMt7SQnCwTJACNEr8I1SxujxaGI_9Imwdf7BAsuN9BJ4pYkN0naxLhXbYy6Z-PXSGR5jAm3d2SxMeefHTGYhUChEqV5c51okAlATudwD_uG1dAaVl3jhlQ7_7yWUJkU-ezyBraGmq0Z6XqUesKd3CE1N2iz1lhDvzh2QQ3PGClk7Rk-RidkNdW9I1vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsxJKUHuK1tN7w5GalCPeJKnhPJmOsZWDEu6YTcbN2A71lfrwkLkQxo5uTTZTWTY146H_4AY6YrNDRpkvL8tUMCDJS5whtr_OPawtj95T8svUm1BKX8aF38iRyAIC8SZkHG1pQ2ZvgykSC4ubSGtA2BBUeQBAIKSmNTZvdw_T9v-Um8K9bQZm6RNMnKPlsBF2EtKUNnE42qKySPSq-2-MwU_bHDmB712dpxSrPGVuI1ztq9NapvENZqgiCPZBus63-Yj3NVCjufr4FlqBxDlHjYWX4frOvK62pO9URpV8KcoXpzZu-5bZXGD-weG6W79VTqIlofXlOFgmgdKIOxAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3xmIKr9q38Y8hUUOTsaCD8n1_ykwcz0TraMoK7SMHC9cfWcQHd1SN6r6FbcWNN5K4ZnHiptUnOBSJvXGJ6tbY40JkI0FCAf7yi9PiFklqIujvQBXRyBWACnBlJqU_XxAvahHtNGrJ4Tec7en4v-B1urHewW3QRfzmU1yDb0FgLNXfFS0FGxc72QWSbrqXROB0hg2UpXPqMLDNvwevR9Q_0smZ-xpBBjdAzoZfwyvHZ2DUVXHSLBVcqhtPsDQBpoM2oo40gWQsdP39zECHk6q83wwj6dc0dav3KwyprPxeoCaaJGiKQcZv_n-qsccb_q33j7YPJoGouwDjTbm7VabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwwmgLc6x9xK1M2i2bC8rfYHp7J-GlEK1qBhE5j44W-pmzeVX6kL8T2MTyEU9kHdeIkwMiefgkyXKL2oPvqYDlfwE97d0NhezYdgTHapN_7OJSsvoCvUoQSdXKXrWBlzfu3Q0op0n3DoaMixJin3PoNwQH6u5E3xYQPUdRjFXpwDZ8fPyByW4U_sGch-rERJHFZILJBJnNjoPuMNk__WBYrYeAdv1yXGvx7yqj6f1qsEP943ndBxjZ9rdc6P6FewAUfyB1pWozcw2VrC4ti0My9adOeeMzK8SXVG3dz1imaItMvgSnet_1nDm14mRhY-kPaSq_Q6lXrBrSJhGh1xiw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ZwOrx7lfpfVtYxB1yjQF04FmFbHOqe7yEgKaL5K8WAGoYO6NHGx3SeLR9NBY1m8X4-UqXQG3TBUkyluSAtBZv6T4HvxGIjV49bTfEQ8QyU3T3SGIOm4nYV_U_3hglWDPYLZHSqdfGllzh5i1GzoX96A7yMePBsCzS71QNpYN9B9INhiB75iJBQL9rDvD3cFxTUGeGDedIp4lD-iP6pWEvjDBwsHKWXVTv_CK1suOF7-8oToW-NxJzUURhRJVnSsCA9E7RTlTy4bujjpPc6z12y0bR9l6DoZewvdrnQdmpzQJP3mwRK3KtC08rTzgL1clq5FVXYPQa5kRP-NWbWWolYB6QHe61jmG6hXlQ6BA03iqWDJaUnCnH0IDj0wBBxtNTy-4Ams1Kl7qtvqeIL9ndr7ak3j7m_Iq1fSQ6HrpjM0TL4Bb6dzZ2K1bNNXa0TWbprTFnIlTPR68waD0UkfoQrF4OYOwfi9y9sNybDkAgnMcy_ywjNW-Xw0GzRzdsvhyj1iCOjiVs0f3lI1WE9zrH66NeE0oUlIKUMqmDV-Ve5Nd1UhxJ3fgrURDJQkqxot-SNOZ2gTPpjFl3a5leLVl2jiAPLhr6R-n6o90ka6P-ByjP9If0-tnkektM2y3V88_62gKWAEb3vWK4rnIWHZmwBGwy-FUOubltqwMlr9qOdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ZwOrx7lfpfVtYxB1yjQF04FmFbHOqe7yEgKaL5K8WAGoYO6NHGx3SeLR9NBY1m8X4-UqXQG3TBUkyluSAtBZv6T4HvxGIjV49bTfEQ8QyU3T3SGIOm4nYV_U_3hglWDPYLZHSqdfGllzh5i1GzoX96A7yMePBsCzS71QNpYN9B9INhiB75iJBQL9rDvD3cFxTUGeGDedIp4lD-iP6pWEvjDBwsHKWXVTv_CK1suOF7-8oToW-NxJzUURhRJVnSsCA9E7RTlTy4bujjpPc6z12y0bR9l6DoZewvdrnQdmpzQJP3mwRK3KtC08rTzgL1clq5FVXYPQa5kRP-NWbWWolYB6QHe61jmG6hXlQ6BA03iqWDJaUnCnH0IDj0wBBxtNTy-4Ams1Kl7qtvqeIL9ndr7ak3j7m_Iq1fSQ6HrpjM0TL4Bb6dzZ2K1bNNXa0TWbprTFnIlTPR68waD0UkfoQrF4OYOwfi9y9sNybDkAgnMcy_ywjNW-Xw0GzRzdsvhyj1iCOjiVs0f3lI1WE9zrH66NeE0oUlIKUMqmDV-Ve5Nd1UhxJ3fgrURDJQkqxot-SNOZ2gTPpjFl3a5leLVl2jiAPLhr6R-n6o90ka6P-ByjP9If0-tnkektM2y3V88_62gKWAEb3vWK4rnIWHZmwBGwy-FUOubltqwMlr9qOdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJhKbuzd35WDnu1Xn-RQPqcyoBRZeyl1Jd2SRjrwJay2W4I4XNMWwBM3Bx3KY-a7T1CNcz4HgH4W72ErAmE3w3y1NUCPGWay3TZGTUWUs_xNIZUJCjEgrh4uVG9OlY4V4gQ4BZ0yhs2Zysaj3rzx8xVSvL_ZZ8kq-BdbujSJzVBuVokXq8lJQNRhVifEAqnqY1X8jYP8C_KxLXlZcS85kUbFdPM1FF7O1FcyEbN7D-LGQpMTvpthewvCu5y9-ZR5SfdNvaVC4C6mBlwrSEZCLIwy6YEpCeo2Cg2Y9wiaY-KKsyhqP6fX_9h6t-7ttFZfUqfsVkT9AuuzTWSTfjbE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msSdY3A5LRCgxg5fSLSEiMBJZYFfbqST3Aw3nwbdlv1laG1EppHMkuDKAXCOeOCb6lrYzZ_PlFHhgCOm4dNXoAWD3eRWInwm1o8UYxX0eG76KwNaOdQCUJyriArrOR9nUXxoS2Dfir1Wy7csUjUb2nUXFS2CixCwwxiflJUa0b_pKPDvzltgzLEhQOLyARReVIkvMTsjcz9slRk4UaJUxhtYzkXctW6EfJH8rXzPQ2hCrmrgd-xKksknKXaGHfzVud4eyEslWH0hf_3xnQ7EFTZC9v_ilYOwyHvxqJL4JoQLy7Hsp5wsBMlzU7KMrLHpeCMNsZg1J8mYcqoEunXxAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEdUMATkNvUVJTIsIc_taFzrfxizmZge3bfULhGGzWafTeRn6crGva7ByV0PzqvoFoxmrmN0T9zx75V3KDwu6aE2K5N6W1JGorh5QYuvsFyhhLFcxZDAMk5jUFjSPfWAa3Np8DdbVqQi4TR87_9jZvdVzEo441wBdjiiGItHctWe0ZsoCmucKDMcAwy0N8rpAi-PhngpTRuKieval1_CCmE5iVYvSFGX8SlfFXH5VnVGI5B0cHYoc5ypQvHNRRySa_kq2aU8yDg89dUIFccuuPO-MoWJ1wnvS_M4eEH0ND9bTfaYyVMul0wmvSE6KSl7RZKaAHyVaL_UroVsJC35bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-XBJ2pMACKnnspmg8ZkDsceFBl1LbFODaybuR-Q557m1CCZTOCyJey7jMlVheIb8d8nzn2DzNZ6M4m5tn0wBo7vG0TrTX62QrBsFvmg55zxyulQ-3lCX3a6jMuPIOmj5ghc7bTQzcJGmi25hPT8jiojNj5G9_gQWKnH81IEzp7euGXgGsgs9iAcV5hEIVyGltdj6KwXwpu0lyERvUa0SbnFIHUFkhfLgMRZBYQW9v5dmyLXyF-UtSFnU7r8QoTKalCHtzzDzfsg3gwF6xvtg0lnQcgBWmpMRWtJma0_q3M6bCA3ma_rVrxYJzHqOTeDdCVRL9HSYIcIudWlX5FGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzmM15e9HslTRff7J-tyEXUT99zmVr0PoiaVekPFIJ6QCwGjTAL2Xyr_pKDep3jyz1_GM4GO3TCDEUTyw5AjzMguX5iCFEMnCcKnoBO1570gUsaaoBCPXBhhDDaaMV5R68e5slAG0eda_v6ozTyqzTWas6wa1EH0R-C99Dic7-pksAl10IdUu7M6RG90eJSC8akRfxD8WBa9q11S8nWFQtjy8tl2ugIdan6_Mc1aarnMOYtzjqVO_w_TBEf92e7nB3TjZFu-rJyyOdOd9TsItrz8cYaXCvarrGUR3vJ7_7S8NrXmK60mMYhIHS9lNeHqhl0xx86zpYZp0J5v5oLR_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m1TBuc2noXVp13MgQkO7d9Wj_tL2FUpnVlAsdTVXgc9Pnslxwtad8t4nFVnT019Gc10gBeDk3d_9jOsOSrkZy9hh_tuiC31jDhwgY9ONQVkEgRfsAcGHzt-sQjwliJKH2xAtIwEztP6kEgMDMjnpfXbp9uKmiodB6Dat9Dpvhw8boLTbfcPch_Q0_iBKptnygO0pjafH291HSnUS6CGktPOLOUokPDKPxL5SLz-rnc5uOvUDRKo39IkKXH6lIxDUKKp5PqCIuqRqRM2118pwR0PqrMXEyKv9swdKVzZa6AKg3PRUTSPOozEU2AvVkI-IMD3rofxTLVabInbqZ9r00eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m1TBuc2noXVp13MgQkO7d9Wj_tL2FUpnVlAsdTVXgc9Pnslxwtad8t4nFVnT019Gc10gBeDk3d_9jOsOSrkZy9hh_tuiC31jDhwgY9ONQVkEgRfsAcGHzt-sQjwliJKH2xAtIwEztP6kEgMDMjnpfXbp9uKmiodB6Dat9Dpvhw8boLTbfcPch_Q0_iBKptnygO0pjafH291HSnUS6CGktPOLOUokPDKPxL5SLz-rnc5uOvUDRKo39IkKXH6lIxDUKKp5PqCIuqRqRM2118pwR0PqrMXEyKv9swdKVzZa6AKg3PRUTSPOozEU2AvVkI-IMD3rofxTLVabInbqZ9r00eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2NDTwxWg2MOmy6TOOQBe1C8m8q5knK2IHQ8EtK2RBDUtVugfa2soYMoq3npzcr799jrQqgpvtnW3GOZf1pLy0HmiPmuOyWEYbhHib26JnronKvT9YQ7L_I6A7JwS07dF1kOcDdgaKoLoz5ksw3aURikfAVRg6ZwmUUFmzUySHmWk3mLNd0LmJLxUx8p1RhErnZGaQEqzcL64HWiCSnztjUnHP7JnGh0i3ZmhbBUBORSnroMKUjFnHjA5cCWCD4pYCQVcR1Pe3jb5tQm80bcwa-cuoWZi-6XSfdl8h0xUVAuSCtfzVt3lAYgGGH5rOqOijcMPDefrZUFWCbeM41Fwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVOKurYsKyXXpMWTNzpvvtQqoKg5PgSCGu43EcdL5uX1uKP3E6WGVPcvbWLSKYHH5LakDF1_RyXCMvnHBTdHn9DVBjdnX0UFWCAT_darNDOvIpW1qBY3HC4xSGH2iZKknR9bIIpbHMOwleQrAJvpnbbmtlVoF1akMhSJPvZXaYK7rkuxWDOrjgGkeWxWVxQMMoHj1AFZ5av8XPlyVNujmdgpKrUMLkVyvS6QBnhkmKW6l48SLEthirVMnhVDAcjk_2BrYFQ9FUmDMqnM8VK5dfHzJuh6L08U-gPrHlsOoc7IXb1yHW1aJ4rj3LY7Tw4kq_p5x19pwEqfXIouzkn9nA.jpg" alt="photo" loading="lazy"/></div>
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
