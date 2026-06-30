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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWdGJ10-rC89ljCPsLTsFTFKNru3jRger5jNqLajPYWTqAWlAEb6NwUs88T-s2DYFwgEQLdOLu-3SiPG38to4bGhnUhJgfxKFKtGoZFMzWf-0XhgDp4A8U4jQ7Yq10xxRpL2iQ8K8rmeQRTxdVBMPWvxIN7vlF0ptLP7mlikm8YF1At_vkKASezqsTtFPCLLFv-0wDfZvUszVvxF_pClRPODIvnqyLZ1vhedyxmrrdULmrlDye5OhDYr9mfVfCJOwjZw8Kmo_ci7m5M2Qs1CLROOfJO9tDKlreTj6ejcdjaMGtH8wM5zINm3RoZFl3YHoAvvAHI0o70OXguRMHhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 284 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 508 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czHixWkQ8_ViC3ex0M225w2BcijttePIyQbBRRQMtFf-mdqfwq8EkHqVmOiNS9nEKGm1j8vSXUHZ4juFFfCJs0OfYipCMYQeDvhv_Liv80-8BwBz2n6DiHssg6OVcP_tmEUTlS-wljHF6LAao6FCLC7rmTykCQsKQImMx0xyExxb7lGCX-NvClr63y0_K2r_yZBW7nibAPvheNLC-ew-hj6Rs9y3KTeXJ0u7uzcFndJCdGOwiyK7E7eaZ463cgPnfTTbjoz1XMI2TwjxZCaJUIu01i1szEmo-Ag3Df8RqFtCepe_PF-BBLfVts8n-IPKT-6upKEcAEEWfv2kR_u1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk67864x-chnC9BAnrwsW_8pY84ip48v_aKk7BI7JtZUs44djZxlirEqRl3e0I3oNB0C8M7T4aPQVEatydRqbpfQm7XoJwKF4gOlfzqVYpkPTWmOmo4y2DfzaRLVRfSkunagMfaXlFuhTBJst6vA-1TzOndf51COsnPff3XHtIqA4Cf69vE4dhLOoIP0zik-tbMm-XUW5SQwlYLcJ31_1phCRz1ZS-exyHDF_SgrJX_ArCecDQJttvuLM6utL-AHhG5hemZOdaDMfj3L1qGB0Mn3dk2uJO_dt3ebAk3Ga_30MXR-Zr3qivAItm4MkAesqvT9vhpQhv01HwJssgtBfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3KLjniEXF9IfiZmaAslIgP0se5-mPAP-THp5vIkKCMCZyq1aIb62QcLcLM-yMIKmy-xCFChIDyaR8OYsGrV-XyBGXiTgPkDeqSC4Bw1kxbftT_GazsGCr4CBeknMByTV9bcqiMLyvhYh1O0qCa3wSg2-tsb0TjL1z529pOAmU5rPnPmAIe7p2SD5npneaY2FIX6oND_jTFRL8wyIhl4qQJdbRa2VLRINsrRR9fXE0ItLmi5dwD4S4s5ANq58eMLYZP3jWffh7aYKAvTuDWG5pdwFhjSzVqA8LKU4ibkxiS-ImKF4KQtMWVZcjjBEpA47nwlPNrsUhLQnu4W5T918Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0QJFO8aIjW1H2AO3_uPSD7WyRz_ldkNGqnF4roP9FMr26ONLZU8HxAiMGl_QUtNJsl13jrP9Sexa54dMcqJ06n2cFR3TH--5hPOQtkPfBRR7yqMFqG5cQEZpzwkvXo1T7BqVziVpWAPdvbBvFIbYr50S4Fcb3U6Q-GS8PfAvhZmkSQb7yA1Y5h1tKGQWt9u_yVp8CcLLGekYYHp0jEQUkUIDY9lUWIlQfM1--CJP6wl3b9UKt6xS6JO4pCwv2ZWsaoc5wW1QpqWIijGcG1VdV09WyheZTnJ43ws8KE8kKoVC488Ry8184g1KCGmuDJJ0gANWDicFEMEmF4Ko-4BNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wso4jt5SVnYuVtuj-yRr2dP1vFcPfCrualEGWmSUVCS1BlF8gc26RgW6NAPJeqVx6NP3xzsHO4GuAtMIby4YlxKEnuXNoa1khrH0sPFLFNr68DuokWxv61Rmh3AZaP7DVciewm1jKl8Alb0vtHIBf3Hy5Msh8a-XjNcqVoqUWO_XW9B7pNA9suIwMrN2-4I6A0_1IXB0Z1Lwor072fACgeJ20p9odLKAwHoLszL1--x-5a6S4H5IukBKHCHQLRZvhXbPWpCkrCOCjCloCnYzNeJNV6L-C3N3VBvn10bCsJE_Y18zLusIsAPwvRoX8Yj8duLPxCAaU0GULFyh53Kvcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5TlW5E9F54wYVD4xZNxjddO81swsEc1aBrl7LiRVxwNt-UINDu_ZiEJE85xEMLcATKNweBHyw_0eokSC9ya19RTGJrzc_nPrNwMYQKC0L6rqKD1svodyIk2IjT-K_HLDoPgHNnOLcd9OBpEFvX6oXWhyms4nTh1s5JUFnb4k2PcpoXWnvyLMZ7xKOEcoN5KziTv9jzwH4PgXFixKdyj03kZcVbt-iFnBgPPUObYM98ALZLfAqdjafz8qIzLZJo_Ge781oI0ktWq5cBcy1M7iZjUrUnAGvDe61-ivmnd9NHlHmTHBdhhXjyX5W-pT8skJx2AtuI1QHqk2iD6MUAT9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky8ggRXSzxhRC7OAVCQ5zqASX1jER_-3QA9wiQkHaHsRLY5z31T575gY8Po7Bqc31rXoFzWkrFJ7x0o0eZE-4pHZs0ZA7wzqyoOpCeD-NvMGC7_LTCAq7CBNKx5a88_ncUo39r7UayF_GJWxcUxsi2CBS7SelElVkA5fpDb1-wt2zrS72MTKJm1a3XxBSI2mM3M7Igl0Ar_E28Hu0TAuKJ1F34bySknxpnVfBAPzegculvKVJ1MIRzOfZwP-feetZWtOQ7Vn4NhNDc4zl9dBbhIBF3zZXKtVejJDUT1ojDcseJVTSGYTrgSPWDaGJCaXuOlmJ6NLedK_c1laavuPSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX0RapbuzJgLZ-xuX4oKFbJzeCQiB4ruvrEJ1Bn-xt3P8K-ofin-giEYwiqNXqfrgBZzHMNjDbAcdyNSXh543rnOZ4TouP6D9hueARvOvpN7PK1956V7x-h8iN8X4dW5RyJyUAmdzhfKat50RxpKPE7OReUDof7DGfHVu0X8dWhpOX49GAIjDps7_Sf9LvUBTP2mA5hF7E5qkaFh_Frh6XkHfrY5ydKXMgDxXV0XoBbEYqcbPCD-RqDtytFPphDjNpg6ETo-t0pPP5jOvH2A2SbVX9QOOPeYA4vVOIA8-yx3InBEhlpvyCrVmGvlgU79KnvJwWtXmgjVjX6s3PVWHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euDZ9Doci1tdPkDK7qG6-j18pHkyu0WGeKvI4vRzp1dP7HWJ_cLbzxa_OKXTQbwtQ6CCkDVxwG7-_TTDaT7WoeRCPiHCqG2Qx0v77YoNz4Zavjc_ZqYSR1iGfFanqsMBsTeZ4W3dLhJQBO2aXkeYdbcORgbDHwlJcu_sxnS8CGVyAdLQollHxHYx6a9QXBKOaSbMlAI7WmdJU4_RznX9hE-wliKHGHTXb41WZspIa3ak6CvAUyAiAJnQNOMoac0WRlb_qYcrQAtcngCBLkfQObhlU5hbbdQSBs8cnT6qqU21bM4SKEPfxljFQAK2OkZUTJVF2QZF5fv65ZCavKU1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPe1zcaYkq-F6JBN45JCxd_yLxXchbmVd9gsjWK89e37cwWpyOjX1YquRMQoGH6ax9XKYQ2Tntyv-AXFgNEqUhhjxWNVbCr-OkmqFoLl6T2Gdqr2R4rHntdwO_4wO-zxA4qUTfZhsgma2fT00221XLRIDHY8znvrJ-b6ysXpUpIeI4ki3RImUn1QIMpvicsLTArHiB8U-cjcMvzofUepXfYgGIIeAT4ngqDqqjZUuhCaTe5lh7wduwXliBHgHLaaLy_g9Gk9WbGVTL_F_jAFn1c2rVV5I9O0qRGemqcy0MtXOy0CeMsL7N5f6w5rAX6jvp23wV456bHqqLazGazI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AklE9vk3jvZswfg582Q39WgrNzmnv8G9z9qrerY-aIJsv3A8SFwLYiXicVoUoO2ep9dCINC6DfejMeYZpZ-4M9i-VlM1yiySQhnBOgXTM-aZs16l03x_IFH7WcsZI0weNDGIlUdQs4v9NheZlxO2BxD3buLlLpYK1vB-IRbXAzSTxFLHmXBwRxqcpYeK3dNoJQ48nJJZpE_rObyBUZX7LMwznyBjv2hDQkJRxkP1XmuJ_3uQfiSnJtDiiDOFhouIFH6IwFh67dfwabWbe0Q4kLf3r-EJdpngD1kP6ONeBc4wRcWaQV-BBZeKrCNffuUGw8IsRbCblVMOfZAwkpyo5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3Y3R81qjDasK7kBGnbmWLlQV4bZIm54S52uRCxyI6J0scpNdCDHQh2Jb6iwuhs9Nxd18G1hTNWXmes50vJ3576xtS7eLXvt8nF_SCrUBwle43l46qgnWf6sCVvPn8Vtj4AuUL2qx2_SkqqH9PqtV8uTag1hEFAUn2L8rmf2_kaXQ5_9dTtirARhQzIcHzmyoCKJ47ZxMxwdPjWSk5iDhhY158V68ITLOx8EDIWbAPnrA04T1Lq7WrJzbzOuoeqIUJb2NR8BgRuL7v3fZoqBnp61RPDogU7AS_IiqVTp_MGgW79xbkKwKJds0oqmrmBskRE0hpwHFLV5N8USje6vjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSoFarzFZtUhwsRAenauggg8fwpy5MNhCchnwr1Gm-XOvD-TLc-uOc0PKP4P5FgKyuvSXxZIAw8QgQWhlF8D4QO75rVX57GH3KFVz3ML3KAe_xXRN94Wx3lH5arY-QK8eILbBW1wsRwyuf5sX-kD0J65kGLAAvaWDlNx1qbnjkQk0lDh3IW3NKGKkt__niA8aPMzgaSw9czUoGar-5v6WUyHdjYMxcQvvXYpYH7J5EhAluluQCf2zxFod0oxaj2nh6kjg2uogRINJXInsRdvmYyKDhHdS7DsYxm0NROZs-9FocpbgZFD3l-5uj8u_cSW6QDpdcYS8u9rHZwe-Fka8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Dzwu-WL-x06b2iKmnPV1oVwqpT9EVwVOgoMJsXT7k7MPvUS3dcMA66BwzL5sj2jdtV2dny4odFKsF6sQM0QE8DDcIht4EcKDNFatdMg7E65WksF6KiuiQB1SHIBqiWVQGaXrgUN60R9mDpp03aK_tmAnR55iWuIi2sMpRotHWHJLC2DSrt06Yic3P7Ge1QLeHWB8dV5zb_DMLgtYOwwerFpM2T5nszxLQdyd445yNUpDU_O1sxdgyD7MUwOl89PlIExgeEH8qxFj_Rxu-HrlBQyCTm71-AJeneDYUpHg_ZYkXO87Mf1FH5fmelL88rZU-8HmjVTCVnKpqne7-yu6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Dzwu-WL-x06b2iKmnPV1oVwqpT9EVwVOgoMJsXT7k7MPvUS3dcMA66BwzL5sj2jdtV2dny4odFKsF6sQM0QE8DDcIht4EcKDNFatdMg7E65WksF6KiuiQB1SHIBqiWVQGaXrgUN60R9mDpp03aK_tmAnR55iWuIi2sMpRotHWHJLC2DSrt06Yic3P7Ge1QLeHWB8dV5zb_DMLgtYOwwerFpM2T5nszxLQdyd445yNUpDU_O1sxdgyD7MUwOl89PlIExgeEH8qxFj_Rxu-HrlBQyCTm71-AJeneDYUpHg_ZYkXO87Mf1FH5fmelL88rZU-8HmjVTCVnKpqne7-yu6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBrrMoJR3j4TMWPfMDxyr5cXaDZkKiKUgjLhLvX3-guv3BOWbQ-GrNlEDqbxqAFvAdj5QydjkUc-NXVE5C7DaG9oRO9lEyZ3xRnvdCp5YsyvZMeUUytk6jLSaLSPvQtLrZ70Df7rqz5zAsYnVMQ3Dptu2VdcjaUKKQnmOEF1fQ__ogVYy5SZ9jcVSo1M44MmCkVSLAp2G3CXGzxrd1zJ2u9hZ6IbTRhTYOZj0mJ-oDG4GpXszAo2-x7gR2U_YRgxk1Gh6ILSW72MjI_86_4UnE3Iy1X3aAemJW6iXyunX1wsDNQJNtjgJ_MK0eRt9eh8JS2lJ4yBLEd9pd11RvvHUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG34_MeZnUlg5RwxE5ZuCNvWu60CtfPlIALHAz0AAsTrA79TGbWLIBDuqsdILwQRXrmAuLe7TAz9ATFeG2yjhJN-mrMC49c765vmTkS43jTaxfjE1tUCh8GkJ-RUh7MimnxT5nCPW57P6fk65E9gHHfAooIljEK0Ua1QC5Npq7TRZzjbXKwUbMhtBdUCLxSVNX1cNAGO_qo7thFdqgfhoQ0kh8yWMsLLQtchC7YkZ8PG3UH90nH3JpT-DKvHHez_WnEnovDNaZBmtIa8yYLzgLqUg-rLxUlTl3_ZHNnARDUdimViaPiPNlPAjyranj40LG_2wzOzQpxLBylmUKRvvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnQyCF437xctoiLjbqa5KvB6cyzwT9bCDNxMABM9Osmr6t95cnNcw3CmcPVuKax25RH5ZT8n6Xo2-PX5AC8tXNTLfB1FYVrsFumWuLMO2yZ2C7-iajhGQgWqLm_FyRemZhTmaq4wFprOPKWmn4KwoX6Q5x9bcUO0qdeg5tC-SQ408UREpdaWp8LMk-nKeBYdmGlN-bpNWwiKroOC_UI78k_M4PLYYW1Iz3XQLJ02EKFcLJs6EPeTmPFiuR9VOrco1rZUOFsvQm_8h-kt_pWc3_1LLRk86La6Kw1BqmqivW6t89xOpSEDj0FxOo2zrmZC-h8tKP2Ha5cROiPqUMmZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8tbu6tPGwVNnzs7_jQXVvUyb4dFdKznrz_NTx878DypbDxzltox2vpOqxltEQneDFk7PMqfW1ook6PIq2I4iF9i_28yOWcxVT8tqWyJcebVry-GhUCl0VPIAjTCRmLTzi-qR1HlT1B8ZedxAInxdIfWwM913hTYACk1wXUX8Rh6jzpusPuZi4M5oYT8hcKeaU2tvSyojQ4WdthHDw76iu-v1URk1bbxaVV4gWqFvDtIwRM7dCmDDk740asvSAyYpGAacjli8hbs7O1TfANtuEt2D4Ur46WpqdCNJmevD2yq_TJkUwId-yzsD4Sr1gETLkoUbn_2LR1W3K6TykVJBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjSTdzW20FmtQvxOlVNW5XrEEW9oCBDfMVwYR2-5wmNOp1gQMLh7D8SihPYmo7SRL-4BJYf3U6qDFkymPJMwFoGZwmQU23fi4ZPO0kVZrLwlNgmY6OX-WqckZsXBbeMUymx1qNudOywbrdGwaxvJlUU9c6tPRg71CF8JhDiW4lu0WLZdT00uWPUzr95W1QaW79HIesbvBj7ghUZCXaERi0ZmXdcJJxr5ZBdWiQoge82UXNftrShqkPLGmwznBTobXnYIhDIUMKoKcjNT6f4nnkGmV1m0Nf2ZSatdNyqfgLGb112etbg_xRVdyJg0xEAebIPi3QMbAi1oiStP-7vpBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTASFD-OSGP3j-VC4KSmB185mZLiqweVuf5jxNqntutyxDz8RPwrTjOeXFj1w8h6553RIOPKhuEL24-OroZA0F8R8cWID2yxzMZLXVojKn9mILXKYt3dbDuEAsUvSEM3ZkMQajw0_cVOLd18Mqtyfb22RTkuXtHQEPoLcx1UwUPLJxIxLaioakHhfCElkxt_6MBfd0zAVEd77s9hXwnF-UhNw6kBF8eJiidvg8LL1szhdkZJX02ipypoK1EzXLJm_j8L1B0jhUFLA1SkXVHphTiAF5KaiqB6YohwyDICANesYigp089_v8KPepv_6Q9FFbInPOFM3VdLJvCx9vjM_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vvf3fk8w-1bx754yixzted7XAVTXLcBVqOTQ4DGwYTXv4XFckkeHlMT5rgwSkFRdwk_veQmee-l7z_PTukYmT4YF6IljqSSdAqcyf6CBoy69VN-rf2I13gTG9AiPNlE2jOZITGHbG01EBfIBTTpaIevdWa_SzI4pSaErdibOAgNTvj5E4gpbYJrnnzsqQsOC5G0942n0dMTEzlWmyjRvZU3D5yZJpOj_wbTtrW4FZKSaN-Fj0VHdcI4p8MjE1-No6TM1qGDOUxmGr2NkA8z0ERO083LolG_gZbFXOdcSqRWEIwmH3gh8r7l-yBl24ZcJb2ovf_y829PVpx0wZ168qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ksm7iPxnSD4TEDIuuKu1bKqv6b8eGPKhxBp-PuA7v5cIfkKY4qYCNLppEz0gIXriMQ_x_NuSiTpvgV8Zc9Lu3b4hFF9-lY_GtQA4tZDw6UFGxvnYbFKnVDz_eho0xvyu3h-UbMHUSyZDFq6D7Mqy4dGEvlB01g0OUtass-VCt7ton60Qtc2rBX-IX_-RSCBWnSblL3DKvkyZ5ABOO0d9MmSYmIKP50OmQJB_zKm7c6dVogN-6sjWj7tcKHBm05vM4YnfAa5VnnuOd6sX5MIjWQYsMNtzEM87Dg9RsENOrc6cgpmUwKaFydOo-ykP2hB8nAdDRvvRxNlUSb0l_Hz8EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNtcG8a9TTrPPP92xwZdB_d_sRpnYfO5_LN7V_jEOpAePSMaOVeQk7Cjr1Tbb0Qo8uqK_jZaTg3XZgy7k9lDYHjWSCgf9P_MvenlVypIW6h3MOK_RHIW0IbUc-f-cjTD0dBkuUjO9AERjXYqY0PSbntCb4-QrQamBGz2EKiUcgGE5Sh0skQeeGaV_tjReyEhYHIWWMV3FzbJAape1CegWfpwL34vq4nMCoB1OJhb01Nr7slY0ZVcpgOpmcTpPkfM-cr-1rbbAnlRz71hZTXExZDpOADver3-9DYNGjcRqepPKrwgPrKRq5_KUmktY75cs3YtZymjXYbXhFHK6YYcbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLnt3oFHFJD5KLHi3BQ8ZIVBsocfoJjMCe154RT4kIqfWRkaQDgg6ISzqnNGuZPl1OC_vJYTDxPf7WwHPwAYd-5sEEEWV0j8yxl7vQbiG5zxJ4XYRPU-EvKagT1VMGK1weKRNckzLt7cxc6x2c-RSdRZjiY7LiZWxAlwgsT8_P8WK7knuElnehsRe2ERJII8y7xyaVKA0s6DRIGbn0xi8dgwZFowG7ws8uKerC4KYlIIdhymYn70NB7HYxfAKTo45r6Wtld-2eqA3fcJZIhvxom9tEc18AnwbkUdm6C-QX5a0SOsbSYMb1FjCYNCkW_h6ZLAABb2KTlequufajK-6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFYqV7AgxmSoxBzjsD9IESuv7OMzQWEmnE8WE4pOyEZlT1B2GUALsrHJN-RQwrNk7WbEJ1PaHXgAT3SjWg64GY7YlHipiU9XCosCFl2tRCWfh7YoAw87gOjeUBHR4pU39guezA6XPME0yLGKhe5fMmWWppV4TONcJqjH1v0E8kPc-XwQ9PQrOrEtoh2yuSSnrs-5Nt0buItxtF9e2PDYgVWFR1kV71Js6mxlmFwljPs2ND0hyLIb5ihZK4rQ0Jm1XLvD9iWljjcx4ROPwQqxbSwUkRG5RchvCFR55vh0E1n-d35Byc2LwK5obNWCv7gII5v1nVXI5GFhsY0SA5MKJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu3o3yhPKNpJSscJYSm81Vs9-aBvLJn7CqfGKySiylfdt6OagHv0usVUE-9Fsd0PxpEaWw7ugvxDP-3dX4rKTp4DPFlGccjrwmQaEo1sv6z_C96sn3sFppFDbXknYCJjPQoIuLr_MMmq2hWBU9ADcjxDV8wzpeHSYUmMzrBZisVvw68EiFLs3PPugFxwRBrk80i-vQ98_ouMS8jnEa3TJBlftvJWPCMvflYfQfZx_75Yc_hl04rrvAb7FJJDgkr32C4uGmmgNFT6nnbOL7uyUxIRnqvlgkS_rVMmxWRz-I4kZT05_98ss01tJPbSWHYloavPsuq9cWdmOKQYdPtSHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiSoo1fRGtZEhdMGgDTIlyXk94u3aTyp-n2LiQyqJqjmgs0sOzTRqn6AUBGb__ubHcP4RYB1byOyHeqTUQmILnhZxlEQPvt40LfJ6jC_lDMXb9J-2gThcaLLQ86FHF85mJzPB0gqTIu3ho9tdQQNYhrVvbvURRvyH97KbPS3Lc5W5p9k2xCqoaT8tY3We_QXHB2zeO2i7mmZQqcSJgee5ULTrZsPoYGnt9pevXO7ypidUPFBo9-MUXXWcdGBxZybuAlC-WK5mIMrt-dEBox2FDa_-s6zECcVg8-n7rn3tKJFxKtDa0SkLntx2fhviDK9VwI1BgUfezMqauoPI_93XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v__StxEKCLVFE6bXyOkG4mbA5i6tVZSQppwyJLW3NcoJM_MeGjc8DFuiWlw5FWBZ4-kV3M5Bu2q6AvLCn3M1WiXbtJdqWfmsAnLPU6ndgBwrd6raFynSiJXV327jC0uSlr9hu2iJrvaBwDA3kWjPHWUPIxTptwIDCCrlBqyT7y7hhdUZlbjs36otAW8dst5oVROZAtKDDaAMrKGVm0rncjq5_VY3Sz1Wx7YWnVh75p1kddcl1yX2MXpsNc8NzI1IF5QqP7vcj4QMUxkKNSGvBrFvAStrkAoLMjKBTv0NlvKzjnlsU1SpSjq1bPBncdjxKJEwKrQ8YXFzCzbZBwNcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvEFUKGILZDTJyDfkpylmXWlRnE9v7q-idnJDrDOeRLahN-9z9SOWH0M29HxJfJDnH2cHGstK0pR6ES3_uPM_pw2PEWQ1ymzXrc51xHF0X1ONjsj99HjgosJTqQ9YvA83Vv_MCqMGsI7BIBwJ6hwQOwOGIxHZYYXd9pPuKrzXrlkgNjTWotHzG3JoQFXHbiHItVr1d4jOXuaCTxot4_mH1ZOTVNn9upjdYtpH03ALhssroruT0WoSoemtHHrzbicu7j8JbkSsXixWKBlUg5DG-W0LuFFate6waqEWSzhSrOiTLtUrNBvsH-Zu-cAkdOrUuRx01Rv5pSCwssBfRJLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlgH2SR9o6FA-vTUVsRx2BlKMWLSFUsjf1zI5tRYxMgWQmZjfP8vJ2X52mPt4C5pDVUaEBiFb7L7kHDobv9tm9k6Xn-C3z_RW3SLcbwFXBNOSKdTJkjla--bBRgxWD3VdWNvyCDPiEUhZEPTmJzbXQ8Uk_CbgjGSQDLPwFVnOT-OqxdD8Rdao6uvA9TPAsd4MKS1R-M_4dKRChKhg4Coqgzb5sUPdkqcDMpofTECCEMHlzMCfZjw9c-u-rvm5akLAinUIlxoDw55NMMRp9A4S-lGDc9j_uuqJ_ISJz3vpc5lApwwm7r1nYK6o8P3ov8N83PdvsIlCJFH1DEbj6alhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJwlzMpqotJ0ajJQXxWjcMTLPmrkxSPc9IkHlkiHG-7WRdOtq89eWSGHs6obWh_G9cNEFA5wN6ibwTXzV_fYfgqn8YHrUrgce-UI-frv02CS_-ltNG6hOGotL0kKgj3IPs-6x8Njg4Jl-pT3paEqIPXJxN056UiPvyq_riPs6E7i1K7DKuew7qQNiPCvCWkwcNTyUrTK8siRxp_7hsR0_y-xRLyZoe2jWEezWGGQ5mho7dYzhXQOJlta7YBwNjLhCYjfW_L_BxyMBN3B1m8P0Fwmtp4XwpJeDeYUOJSpGGlmLnY3c5tSvimffRaRaLcq_Yyxz0f8UbO-Xx_3xnB8xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuPdzOaRc3x2Cnd5Boy6lya3savot169Sc1phT1ghYj6Rgcs9GLclZQs5ieYVW8KPH2JMHxa-NSh1zZFzgtxeliwfJa2bGZF7p0KqTrD_69qR84DTw3jeoIa2ujWx8JBTh_Eo5G_lrc2IUls4w6pZjBAd5mLN_HmgAyWcXhDGQx1LLXKOMktJKeWvGUKmZIDRKroMwW5QyBKrBDWzQ4IuKgNI54-5TQ8Tk4ZI5vkk20aS2zi6zp8vnT5S-Mc9Oz0-Dw9FXLQePA60xqqlYDfDFJC6HnQgGO1sHeqitkibxtYGqde5sOMe1ifmOizT0zvIvZZ4TBjjYb2U2pTOkDeQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAS9U7joe_rEP9JH1GSw76lKwHLyIgcSNzIt7wjmuxZuYPAimhgGevTv3fioWgrJn34IozDUQ1b_jgBTmATTpNLJwFClVdCX3bTDacZA4cDNqfn1FGnq0pbZcl6RzfpSZbvl7yCBrHT4i_cpeNxFRz_z_wWq1P7pLGsTlca1xkuWDF0fyDdx457kjy-DlVSgan7WFKFsVDH5y49su6sxEBFDPoWmNjt4jW9_sWWcVg1D9qi0xoLD_K3fURVWmcu73kIzjQYrdGobFm6Wa1xjpsM2y1IUDFB0x0w1PKtlztObicPKfY13e9YjmN3qsIba-nZjn8MJiSYthIwe9_Ljjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtJiNTnA0uGpxQDyryBubjsR0-FYhrjkZ9rT8UtQWddU93oa6sRauR5iBixfvTh_vV0bMiI8d_DX0wWV9tRuA4ehO99nt6MMizq11TnUu-ZcV593NpBs070Mj-LobORtrN9pPWqleZTJ1a-oztNtZ1_Fzmxp_SV5F24_jHFg3Ze_Elt2nsanER0xpcejtIAcpI0we8Gse0lUzF2ss514qFSit6Lr-7zAnKZyzn7kW9ZwvIC4sbIpggc83nKz_vteoAtz1U9667dVOhfYS5Csvmtb1ZJXxo2_rhlc9Fws_OzqsDuvtd1_yHdb7WsbfY8JiPQOY559v7TFMetQbSPSVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcPw_00ApxjEUmlrZ3RWKMuQxcMMKpT6D0_kXl-hbpGT1eqW1B9hBVdDxNGdQMwlQY2qALxcbS26LdlS7WZwiuxV_49HuoicK9Xucj7vBBdC4RvdO9UA5GBdduJ7qNG0w5xHdbK0HjmbhV7jljG52wjFltK0yLro3ws7XqdH69L8A6FZowC4rz8FLpyxHWo_7JzxGZa0x1lg03af7VDc1wHAQeZk4VGLB0VIlzSET2hJwbPJ4R8uXAV21rqfHm8gyWbBSZSUqfYKMDuhBO7Ssze3T6jrJQcxOOOPRBuLi6OTLL0AGaG4eI0ctmqsKYLDjESLjrduhKsYcPAjCWVRGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOyIVF5m1iOPq0Y7cs63N3xY3-E7Wz5gZavxwQqJuIlISyfUSwee41Joqj9EYsPGyUkznF1Z_m_zIaBxxlC2lpK9HMp3EEceH3Gs5kcWd7rAPZK56TqA-9i7iHJawKClOYGl2cFAOGP5JCeGFSK9q0l5yHLIvzcpXXF6SVBR0zNBOhrmD4A-uySh6xVxm7Gg8YA1nETpSuzY-YF2KWYV3QCEQ2tIhVOeEsinaFE1RKk0WumlchKBqBaItsOx25ZFHn8QqYDFmqJ7LjIOPK0rRmCQ7qtFlek1cn5YCLzwP6oc1Lvp55PUBzopw3C_oXsKrbkVBSDr6I3I5HsOKFR8wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vxu78LLT6lA7TI1OSwfIsPj1ND0X0bw6DwfPaVzkFwgiokiVikY8yR3UZzBZHBgaIJZ5V-J-3FQMDOLhV5Nhzk9SAoTd5Wfj7LcJ2-tFo4FDUbCOXxxJMW6m1N2TDBmveISVDBDdkL_mrklioEeBnVM4seeeiRj26Vz6m6RPi2pUbF8ckcsw-Z87PZe8DGzaj-lwyKvdRd6LV-OGbHjt35xQ5XxI6obrxsmwZNLyhxL4zI7F04YUEy_lVCAb-0u7kjzBYSidsb4GMqBVFes5lPghtHhCBn_YZJOZnwBeToPuDnYkJs4ZvvjZQFfV-3ledafoxwjBCLST23_zyn_l4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgQ4oEDNpc_9LgfYdgEnnn1YhBM3R94E_nzMine6VjpMnfj_lGFDIk_uZdBkNrIvwqwSiyVYmB7pFO3jCRVK51DGdK3KLngySfEqfoNMsKBl5hllLygK4zYGpkssx0vh1ancP9yVuVVSEsJ1gAZs9nJaSoN-B_zRbjHcK641hm_oe2T9dD5I6Re3szl5nuQ4LgtmoCohLfXStcUvEuR7SJ0muY3UBtdVU98_nxVPouSgP0c48_Ubu_uMdYbXijRm4XWvv7lNJf_oHCu98NkCOvzEB5UgKPadIgHphbuiuBUoz8kB8HK0-lQdcw7UgnsNSaoaPsT2JmiMaNdNyOfl2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5AbvqYI3z6sUyRhoea5C_3s547Zpur3UrdULYyRupDuGayTwD713XJFlF1Moy1NSf-9sqgT5pkrsF4a_Z3wuw7xnzspVWEP4RhKuvKirNVfYat3mW6mi-fcmx5c1pnU-iKIfYZOxfD9BL29oySMv1oPWbOgPiqopSLwec3M0wNrEmwENA21Z3yEnfuI9kt-vkxEQXJNFCHZius6EqKl6hpi1Gnczkflc2vJl4Z6IGUkc9pcYTn7Xi9vcWj3hmVCXqG_b0Opvaz9Y74WxXf3-yyy8ppAt8LnSQZdbY0y3bBBjqtHcRTcaUMqr63LGS_zrWCG696mChSiRYi9jJupsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHpitbPAcCEVPm_RRNRTs5ApTe5pWr6e-S0AxsKPBNwDh93id8-PgsZQ8xADQrYwMja7gXJKPxJMHTK94RrYXNZ7iXjIME0VICbiGufZotwocEJpII0tfnDqHvPq8Hooe4azmUmbc4wmD1U96ivARtviXIRkFL9vRREY9AZXFJMls2ZF9nJEQVUCJDQritLTyOIwexg80jy9iMzn1k0TAvevl7ttMyLtQQwRpYwBacATb96Z1dZe9v4tX0ycWsn7XT2uNVIkGDmM6CvjCHe2yOWwQUsdZcAKdoMTzCln9CJw8DAJ7GpQg1NNZBr5tMpY3UTu0RLrjTyaUgnDZSO7IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro-qx3YM2iLRkQ3EqSCDckjz1-yTkh1eTCENPUGPPB9jFepMWfhz-67BlVgOWpnjGShgRHY_JI_pukd5XzJb_kVu6MVwOZnq3lDYGPuIoeKlK27R1wfWeREeblPoS1AMhLoJAkFEvW_LwVaUrtTpLgNlHIRDSdiwA3Imi9ODx4sNe91ErPVWW0scbwUdqiOz5V31Hte96-aP8VxtuqqS1rOF8xfyvb5QIT7TAeuSqQJL-Ife4XR0P51oiDhPsSrRmwsFs79A9t7r0YaI4oib0g4uKpcNGlR3uJ14uqYXxeGhoUpndKDjmiz_ApuHj9Ya3YDicSDUyVZl4rppaC7t0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTuBRpJvCGHYvuni7BvE9iaO7bQjft74yf_EznieOn2b3PV-FOKZWieK3YRIrg8DK_UvJnMHLkD_ilpfdrxvEJPHGZWPZTffYDWixTWVEBmerj-lReeHGv28pY4aL2GIQ-nIPd6cllNWwjmBS58lxPmozsAglf5P-r-U_1mFYbBC_VkCU2KeP_A3hMkJA1QGp5_L7kmkHdAH0P72RfwouWMrp3eZYT_fsF6z0r8Q-_RzyloSq9VvzBSD-zUq8qsySbAx4_82SPst8rsahIpxGWkdUYNYwrHzJLfbNyWcgksleOalGPVwtLmTCfPQ46c17fR8i48tk0qxdNrz4sG7UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTSFtdVNOZvGmBmTvfi_h9RAB-d2MBr6RlXVfUGRFys5Db6Hu2xaADgtw572ocQglPCL0rnuJIDugWCQiudGrISxwhST8IC0ok4l0XkxUAZD2o9Dgg01b9WRJGkqef4bAkUILOsfmzscLh_g6oxJpwe_CEt1O5sssZPSzjuB27fXIIog-fnqCvJ7ifFsaT-feQTLaiUOEnFd8bL_0xIT57sWByq13uqvne1b8kNUtj-At8CDKiMP87q_IFqLyzVnWo6ke07Q-juKBMeBxysRlDMd_ojosNh2NxXAHGkxtde7CgEPaeNOfj7RC7UwohhgnkHEn6LXozTdrHZ6B0e1cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBM9kVDIEiEU7JulzE6AEO45VEcJ9qdd-7KEzd8fE1B6JPy3PfWQ10cAUurqES7C954NiwYdvyTKfNoXsbFt2I2I7IQO8YuuKQBoynI3K6-P6tGPLk2zHQRrNlLMtunHaWnP8FNwurzMfAKuSw36yPItEDPhxcs07ldfcA1uXvWdZ0iv_K_-IR0ILq2GYmyFhA_fu3xuhH8-P0VFjPXdX33IgZ-6NVshFmCUFTxQRH_Dz1RybGfG-hyGjfIOSu2CAFBpw3JFok1s05Q71-d_cG-d7DJ9XcbvIDRN8o-Sxl9RnUFZ2gvmqfZnMFCL8H9c596jx6XLlhrThly6LhcAHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIbe0jxbNgafDyGxXTl8RiHT32YfO_WJ71qWRZLU7S4KRrKewvoUlFPsyIAfUNUwhZJF-FV7tdV_Vy9kDwT1FIclUiqGkbtUUWEaRiiZhADkq1yzgeFtgcfDbamYyoBhWqkCFqWBz7zZC9WxGgbpLdnT21Yy_nHO-AxlQDoRjvEZtuNvFexfxZpXEIFvFJvywiInMwBy7N_6DeSfiH-MtgIja1swdKGrOfsj_Dk-s9sxoGKDLFK19x3PQECYB1L20g4KG4wDuUaVpU3JuP2GltX_Gu62j4Y3g5sVk5XPXNAoSiTBsP_bVtm6zaB9q47obBxfSq33hX-cNs-VM4H_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6DlTSRbhKqtjXbOElIQoQvFhfCT2Y10PMD3y86SnnmMCBtA5nDb5zGfobS0ugqzpzedBPQiqRef3dK2CccuT1bRBWHGg04VwSfbzih_VDruZFeT6K6viX0JBaIYcBs_7cbmMYtmRy_IC6zTtiX1EaBY3TMm4Dyp4aj45eW94U3pcuY4JCcYijzvk88eLbFFg8a_lIWb-xO-4DTu9oxyPuv_pJvtGvHzMmDZknWceZDyOMA22jqBfTLIUjcVCGuo2O9pfHw4YJ8-LCeclh0WkqvmAP3k72U_T8b6QQpAn_63Yc9-eUTB3BvNZ9uPoTS43fnaYjAOj76us282yw4GHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyH99fsWP4b3wckq8FZErADpcl2HD06T3KIcARRrBCR5dwA-jk4MO1QKzH8ZXwzJqAB1Jmsux4y9Sf1kBGnmL2CTxVtJYiPYfvalVtFjr9eBQV3tRBCi91i6k5rIyLK35JjEAITWepe7MJBfPOfEAQ_w66LPOPF5XYZ68QENn5wYKBd8TGtNO2AJV7gqgrTVFIaxKs94r2VKzkP84yD-n0k_EyF2pKg0s0lqZVtcVYgDE0MQkeFmMBU-Jj2FUBZqSZLcTBau-DzWIHTWWsEZkqjvlYk9PI5xtjEhE1JjYihhudX9X_esoDisZ8N_SLXftQi3c_Y3tCmbagF6-EcobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAU-XSDp2BpKp5BNQdE5WvpQJVzP6HupIdWwZqcFHEQKvs9IK8Hg51EUgHoJxe1ybmSmBiXq2uyIzUegPF_-55OQ0JhOojBrjK6XZ5hN42lXti2Z8KwSq3Gl3Ii0bQ6CzPIVYg5igL1crgdS1ebEKvusL6rtM7jpj_cC_71r0Dcw_xRWV9eekjtMUtDuNCXUrs_xKof1NYDSP7T99wHcJEHCsc8aHfgOyC_VzOFPZQfzgTbVPEPetRbONYU-YOlHskXQWBSd7w73ZnLgQE2OKEwvKfC6Qf-ggdcxKC4lfm8wXU7LZtcn_8UmIHorCQ7ni0EKNs7SXTfCvxGm6RRyxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEc3N8zvTY0VwNGtdAVA9fRXFVwt2WAeUPS05o9hT1O4EVPg54Q-ByxlDh8OyO6bwc0RAmpmdcSlU7ZNzjsdFBdU9DEiySH6fsmlIlQb5-ZUwamlQ3o56PboJtz_xnk5-NhvTDUVGvNmSHJOolVDI6DUG4eHmScw5YGpL2xzshL_YO1GusrC3QIN2r8a4Ape9yHb1l1b6lIRA-ESN3rqiCVLrcgggrhXwPSuXacAnzUAz7-ytflAH1rDXAeCry2edqSk4uCURZ9euRGiDDGt_oidjC0kZ7BVqg6T4vbntbI2YsvPxOc9phrBb4yElM1R_InEyIfzfuxX5S7QDqwqXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5gLNXp25_R_5SLeq_uoIMItMV1L03tMY7p30jB2OTCiNkfTPyzOfqmb5jNNbqddi793o4H13LtbH5DKkOoR4Ya3d3f78AwHTFyJf1s3ppeVRmh5wnA52G4OCebIcgYM4ATvJRKoSEJBrh29IVa3Q9k4XojNymyebpqbUUnFnCr-jmANL8-YCKnhjMAkFTrIWBTIXTF_GmGr3c17o9UNXxOn8daiVTJezojq18mF9bAc8sa8BbD9o-nWmMsGOXvErgoJeEPS_mnIxH-s-1EZ_2XakRyXSmowg9LqUpd8qecRV0kyVVYYCvrNONNUGZS2tMuJamTk0G-G4MXq0EQTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXH6Xs3rQqjXFq86Tq2uBvKYSKzp084KOiysWOK28rom0DnyxnGhQF1ajBNwdDkM7ykwv1IXkY1LwbLUk4ZKQq4K5_TohppHa3u2HNpa13RepJJt_SQrBspfdigu9m-yMCFAs7dY6rT-cnqYUr-qio3aSwA1ZblFrWn8N5F_baJDm88cilun27UAce-9XVyDQxCSvA1UlWbo_ES050se1nZ8ld937cV1m7zSVIiiClYnwPv5I57meqw7b6jIh4NjxJUUYd010qJfTBeZfn15RmYGbQ_lQBebN43JN3OVhcqVHpfmjuACwCqMmRrdnxai8jCO45KVuJCJzhxCHtExMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkVK2JsEnsDxUsOYyZj737E5wErS6-kNmglhxxF5WwLBEJLCJRlRWAEVyaeHPKmRs_mxcbFVNCVIGlAHT6t6xG-42z2kEwoHedamImtIdHoCOZyG6m_u5J71vFJq0t373Bh9TsWU_nRLEaQ1hgx4iJsdqqDCSdPBaqkCWhobnNmrCfoRVyCn54kNuTDehWojGaobzpewdwkgb1dpScTgEqlvJ5CWxWK874Aeur6B1dYl3a7FHS6lTHHEnZ-6pq2nO3dWorAOrkNLgUWT9U0HjqboSMmSp4iIslK26B6l102er_Y88CnQuhGb1jpD-bHvLImewUmd2FXEBUIc2zushg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeADQIlEaR3IMtoF8KdlKxkpMNMHMjK6rKRTt0-HGcQZCh-t3_In9km4S3A850rI-w0Z1lS6i1-xlQPMi4tEXksIz55I_hc4GvfjrDFVcegniavVkUUm19GMAQOIaDqQsPXFc2K8gYykcy7iv1Ifm_MJ1dlZsJFkHocpliSTE3iDtUHbSG_YeV5L_yO7N4MfJlT8yj7H4-TJHuupk9kktb5UpA1YUg8ycPEBWXbARnst3xpfv8hAmL4_dEA9uyn1swrYGg78TOxXH3rH-pmu7D4PHFwHSl58sE4KPKbym3eUP6cD1lALyuf_3nvChqtR6_jJqVlL6pfGXbvfnfFOJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rk4asxyGuctMApllj4iKk64LjwNegXjk-DzZZdegDasqi_CKUgR-CnobicDYnO4sgKuESqiHguXWC0P1B2feOVIFEqWtRXEPYVLWqh1xswk8yTKXkUc8Bb93P6CVmkClSeA4834B9okSAIIAQQ0anZ1xmW3TMwqEt9DfrqVQXy8NpCg4w_isxUbOcoeyeUfBkMC09ZSdxDTkNC3OZ2_MYWOrQWbnbM2yYIDZBuBcVVyNbGrtvZS4Xlbp6COiQuIj74qi9Jx75IIWXla07AhTiEwMovKFTCbNJ3V5M4XqIHm2jfuI0xShZCUr5qO-6Fkgg4c4OOe8toPkpUahgPR9pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D11Fe04fMrOm5_De5v0Or6Poi1koVRMUltrir_MBKlTwWzRr6ftIW8liQbfBw87eCiy5fDT7V27QrCGj8N4le5NcNtt1Z5_M-XYKLM6hW34gpKFWF4v945yifna3k7SdKvR_nFj17x09HLmU1LguaAtHiCRYGGaUkc7EvkJgo040BCF3boua1riy9ca2tr8Ae8aZZfz-4xpkC2ZwvFUiwfQqBGsDW0tfvid6RWm5F3LlZTksSZf0qMqlF2fT3W910UfiU5aXVxl1yuwpF6egrNPZuTcv3M1t8xjZK6ll8wtKK6t0p7PKL4ZxXoUfQYdbTli4n-Jw5hZwEeB-tVw01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTWctpt2SJRt6PlCfZzpgJOyxyln14xnZjk2a2WnnJpzVwx5CnqExX94vFqgqYCf4vUNdI2JnPjj69pfuqmHh0HpYp5Q4e5AL31vjgmSUo6xl1WboORjQsXlMN2Qnu5IPH-ODCKf7WPveJkc5OfsPrTZoQL96VqDdBsU0MSS1CNj5aDJu6ybp4Qfq9xvfhoV9lWlUZZmP19922R9EkLLfAKWoWzQ0Xw5wpmF59hdX7CHTUXxTn8221ZBul7Nl54agIh8pRmKYp56M1KSJk2eOECRzi2pxUI4V51JdBEZZ-y0RlIEm3zlq3TaciDTBdFEiypxxJulm6QyTw5uEQPO5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_zSATktNOdntNTfKD8o71F8M_PgyA6HDW03wXDIUonG2QHNharFGqtowkt0obsENmwEy4k1oXKpbwqrHdZCpjOCSeDQCU-Yhk-KuGGc7yuH_Xb06LqzijgSdM77GJE487ejETpy4VAlP__-Y81HLPXxnS5gdXih8VKqlWLmj8at2Jc3e5fT2G7sAb7WyAxWmgWtKLTnq1wze4YEsLJU_IOtr9Ap8dumUPPn8c465SaC4tb-btHacxQKer6ay6hTItCtvMnLC1sfmaZdQ8vGqZ2bzxj97Prx2t5l3HsMsUl2GkGkONr0uosXEcx0ipflqkIxB4yZM7jg1Y_O9ymK8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9rppUh-zjS-hSK3R6hJqYYqHXo-MTYbvX6vhGX3_7QZzE5UPD4c2rjL959rknCvDhmBs9Lnhj_7qxWVW9OJOLo1HvfQpxAfCc3o67usxUifPz9vTEFCZnOJjXCyxc9jsGilC8zjBP4YCsLVTjj4sqFkOIKDwJ0DJ70XxTJJW8SNhw6nJ7S2-yq3iDBqV8OHUn5ASicGX2xKaKm7w825vl2cQNj6YoAOt-kFpo9AWpHl2B8grwjWFghJwZ-pRq-auV2LQkXYxAvZGdUMfvIMtDU4j22SSeXhKGmNUURp25wkHXqJabYvf6wtvpO4RQwmMbmITQf2p5mxYT4YI8oyqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdJB3gCAEpjAkeaf9PidVJMmXzixu1AdTIEIy-VIfp7jYKDmf6I_B6tOMSeI_xe5RYzKFeralxmpP2PuN-jKgHAiCmTrw7sXv1M_SZ-ZaukQWus7AmpH6SmodJ1gcS4dqNSuYWAzz-W9DBIaJEdezpGR5zq0ZDkqmmnPKBKQcFTvf9VHjAJ86FDSZl-IhuHRm5GxhS1uxfQtn_pric59rznzM0QkSvn4GSTTrybT7XhDbIzVsQeZVCIK8o1reNSd3_IgiVjv_w7TI35KHND_L8XaKU8r1bxRrgVQ-rgT7KACZKZIVbZXAyr4EY2fuonnuOdA4EgvNwQiNvlJKeg5ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USirkKYoWw3U6IXqMIt5-4efSwTNO2mmrXVoOsWNvoiJbmIuf5iZhAEB_z89mKmQnM7V7bjlWvxR708qQVQhMvhIyXOTn2DiIjMQgXeMLv20QDeiur8DSzKCrCTDXB3gHMWSCxxCnYW1DQtLIxxOWHMrCMAWC3xqXubefj9PFKPdRl05bNQ2m2gOrwfat5YBAE9igWrXpKS6ALm90riMBPJSiLxgYCRNjHXITJeZa8B3c9QgWolNfEL5LFzGHP22N8pyHWYxPo50T0_wOfjjkzSSFn26Vv-j6GEbyHXThuEK_KpRRZ1v0AL-S_hf_NMJbDzqljM_FPF84EnC_Wdeyg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=am08zOyhGqG5QJsuyXKwdHdn3o9LjJPzjLzxJRV2J7VFNZi55LrUi4ZVoHXb8zCBkVY5BJ_vQT8GB8FaBemPaPNJ_Vpb9ebc4XRzaAN2nIeIdqOH54vXgGWVqogZ7jpHhbfqtJ3pVuNxrbvjFoAA12-B-yvqCmkFE8OULXXTPBfdiKXf6Wt4aomPslyZhw9jNX6w35ouE7fYp5KX4TdXnO0RYnG5fFLdlVBS-L7gSa0WGqMuqgAPpNgpkN5X1U_qMYdBcWgxonRKmXIRaYctTd6w5XOhCGhwG0oLkhLad75oGJFztMyu2Is1WhOXMC41Mx4a1DWMj0ZRGLvESr2egQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=am08zOyhGqG5QJsuyXKwdHdn3o9LjJPzjLzxJRV2J7VFNZi55LrUi4ZVoHXb8zCBkVY5BJ_vQT8GB8FaBemPaPNJ_Vpb9ebc4XRzaAN2nIeIdqOH54vXgGWVqogZ7jpHhbfqtJ3pVuNxrbvjFoAA12-B-yvqCmkFE8OULXXTPBfdiKXf6Wt4aomPslyZhw9jNX6w35ouE7fYp5KX4TdXnO0RYnG5fFLdlVBS-L7gSa0WGqMuqgAPpNgpkN5X1U_qMYdBcWgxonRKmXIRaYctTd6w5XOhCGhwG0oLkhLad75oGJFztMyu2Is1WhOXMC41Mx4a1DWMj0ZRGLvESr2egQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3POAXFaSfi2vl-o_Rta3mtp8B755U5FjV7SQswINbgcyt5hgabfd1n4QfHeppa0BqXj4COolZXoRrWZGMILghQJHlLax-BvOzlTIEvsYTQXtU1jMDmJq6K9TAfWShhEMASOGRTo1hEPnVMOJqnHIWBhhsc1wsywz-bX3iiXREsYj9HQEdU326VbHm7UTCUNSPUAUWTkG7pCuPCYkc2VsO2TkXUum0_HlZGFyYGpvQVZLsLH3-cxr3eXB4L-_lWb9Ijb8_MZ0UOm1rywj2Box6CwFvOJNkoU8Cm4M6_uVx_dtNGJKgfqVX4Kil_PWIiXdQoow5DJ1gOIG3VPo9HyqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojOSzS0AzBRkhkTdZxcB9wjRxiqPD3Gh7w27AM1keCjxSRwoIRs3qgvITz8LYOCQgXXaZpNeY69uDgoLmwWhLikvWfRutzznBdGuMRasolzgDL6c9vuXDMw0fPtbJstiNG_f8Hvp99xHyrMHtrSm4pbKvigRW-ZKKJZNJfxOjHa7dQsUPlvWtj07OXaigyXZRCYkVU7JLt8uuGZBFDXcbGBwUO-t7_NFh_15graLPvFAWbfRXV26wQ5_46NsRK_U94eDU6mvBsTiyWQnvJwOKPBpd_to0a1nBunisakoXQD5IwlfuwuTjkYf_uJ1aAggOfwM2pER6Fq3FlLkfz6S4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mT4jBZXMa8p3Qi_UzdRciPunMXJfFVzkGyUfbhrJGMeF1YINKjI21gVq0VALVaGXzvy_Lz3fEkf3CzM5O_fgUdaoKx4CYO39HEGUVzfXVCyHCSuB6EJ338N5Ox_PdMWuWo9UvRI6dKmFliSgAVe3yniFt1L4fzTD6YA9k2pY_VNtOnteYoZsLllNrg0Ueu4kMNt9Ov8o8nLEgcjF44FHGAqXXfycp6diyXB_TzAc6pfOpvyirK3Nt0YoEwSmnsOGpAQ6GyKrXDr0Ct8T6px9suk7zNyI2CZLjBwnEcjvjjQOq-k0reM4eLBktH3ebJjjQLXG_JpISJykkIy73pgskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEL0iJIIMIaLhiKZJKccV1BYDL2M8WWWKYd_LW7AOu-KyTcXbo6eJbJImds6OMZRkcXCCkvg1ZoUFd8nLOIKfUXt6Ir-g9zuND3kHTu8Y5Yc_y-HudUwBxl7PQv8F8c9k4yJLYI-caQOdWP_m__xkAn9p-RfQRWBxcTJaTYpV6cQeOzekSbQZf4zGuICSYTPVemSjHqunITbyEEnGDc9sDTkkaRwdW471yQl5dQhmDHhQS4W6axfbj3VovSsqAIxR7gh-x4Y00kK5qh_lklZd3tbHK6gwi_jlukMJGswzrRqGLnGZhfpqObvg_tu52WVI03XnJqHzyuhvR7SAkTWhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkLqobJ2eOO36CpxIMfvw_3R0OORObgu-X2CFu8JzmtRT3CgdiQARJ7fHKbmeyXlVbxJGm8YAETJRaI16jjtw5oQ6dMfj_fgRtYLsd2tt50dgabY4vStOqRMBrSBlf_Sg6Q8-hZSsi3159Lvjk46VPsfFJCMZXoBv8SBPLOFf5-Pv9_mEKF8C0NGnr6pGlkhM0T1OMaJcONQ7QNbfaWKvjXKyWp5eivhMJqaia7jImmlFXzFSHAVjw9jn8eNrZjIl7MfePn2HIAqgHp39zZxs2w0SKh8Q5MUf3rohrK_9gNnbe75MJ_E2KIqKuMtc47xcAayVLj4hicL4jbpzl4VYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qr53OzimuEfG2PO4Zls2bmm2-9ApfCLqFkMX5SlhMql0vhexfD2zmilsakY0rMngmbcfbSaPdbCaLwNnWD54QvbAOzY1NhgQfJubRzs_D5qE6Jmh4035ZP3ES53YRsjqh85C4mwbZB7wk9V0xqrrsWA2idlXv6p1CKrai0KXYilFkiNhJ1VzDECQh5lzDUE9dTj3p_vrLYV9Vq0Ye1hVaZKGOuAkP3kAqz0dm-OvSiQbqSCZjmdJsqy6Att92EAlXX5V8-Enmrb-udygOcZopo21XGb0fTC4SnzfRQMxF46NyOP8dwaUBlJXT3ldmVkFet-2hpxUgepIQ4Z4-497ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwKlhTmSNITXtsXWrloGFUtUyMFLW9JT0Lg-QDrT7gRO2DSTsB5m-fuTRoKo0jJp8L5CUzSmWJjNLEKwiEop8JdeZDJrzuXISSIVDecyEpT0QrfnCoveMkmitbj_gTMfIhr5paIJgRoNEN9SOoruJvUKC0RF3TdHsXDaVEnzaktRAKYGAZbgmdMMkDmGV83acCLdk8vRiDM8EdIopa0MR5CkRqnd7XktOCklfohZTQOOz7rq8SJMY3N_CM5zT8h7bYpwdH6d-ruo8iIpVZmjw0SfG9tfpgHIGHH6--5E0oUNAbl5ef1f76lKox9ZvPFoql-DjAbQwgG-bi8LDLy-Bw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ITMxvtkJgbuT7UWl_ees547C9zAKrYuEkPWDx2EeGbPWqK1GiNDZTu4D2z_bVMU29VfJtmH9GnpS0oJsyptgphJYLCRCWfiNsCgrDUtyzwEjZlOhYv3pniIVAuwqI1nO1Hxn-Gc3v7OOQLwNPCeT0u90ZnQtAd29qP5s18aoCe6Y5YQZiJ0ZIMeu5ftNqoI0MTACtpvjTH2HArFzaI7c8zw2TVmmuBFlSkVTFlOYtfm0eZs8URuS3KCWSPQoA4PGDhSvjRV9N99rK4jZO1-PN7xQczsJI1CMhOpLC3K7Nn9ZZWafxHkNOCW2jIm6HK8uQ_u06QY6rdh3PETtCL3PSKwH_KWyVylpKb1_mEP3iTwZAezwWGiOuRc8s7NnvXrVUi1si-8mD_ynRFeYtjBrLVYvskznjeVVrOrQULk2xVipebMIEuq5uwCZIBwuGFpOnxIEbHRlJ4Wigst8aDhtIozwjISb3poRnpy1rZ4hw-oFBygK0nYXPnp8PMKIjnY1CRX9e_asAmI3nGfbUfvP1rbUHiilW9iRnYA9W4iEa8r4XMVQ0Csu7U5kK3AMNJuPh81w_dyFNNxefFV-BUMjUSwdsKmC99klHJQc-epKd4GkSxeDgn-3cs0mQFhSoxuBbD6QLnG31Y3Jbcrw_p5bXXOsM0dv6WXUM3MvesYD7jY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=ITMxvtkJgbuT7UWl_ees547C9zAKrYuEkPWDx2EeGbPWqK1GiNDZTu4D2z_bVMU29VfJtmH9GnpS0oJsyptgphJYLCRCWfiNsCgrDUtyzwEjZlOhYv3pniIVAuwqI1nO1Hxn-Gc3v7OOQLwNPCeT0u90ZnQtAd29qP5s18aoCe6Y5YQZiJ0ZIMeu5ftNqoI0MTACtpvjTH2HArFzaI7c8zw2TVmmuBFlSkVTFlOYtfm0eZs8URuS3KCWSPQoA4PGDhSvjRV9N99rK4jZO1-PN7xQczsJI1CMhOpLC3K7Nn9ZZWafxHkNOCW2jIm6HK8uQ_u06QY6rdh3PETtCL3PSKwH_KWyVylpKb1_mEP3iTwZAezwWGiOuRc8s7NnvXrVUi1si-8mD_ynRFeYtjBrLVYvskznjeVVrOrQULk2xVipebMIEuq5uwCZIBwuGFpOnxIEbHRlJ4Wigst8aDhtIozwjISb3poRnpy1rZ4hw-oFBygK0nYXPnp8PMKIjnY1CRX9e_asAmI3nGfbUfvP1rbUHiilW9iRnYA9W4iEa8r4XMVQ0Csu7U5kK3AMNJuPh81w_dyFNNxefFV-BUMjUSwdsKmC99klHJQc-epKd4GkSxeDgn-3cs0mQFhSoxuBbD6QLnG31Y3Jbcrw_p5bXXOsM0dv6WXUM3MvesYD7jY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnY870hDwTNDxIZUT11w6MXD9j0AkStaMXZlwjMXIv_pDosXfESFiLujkPAB5gjptCRA3xVuZEFWRnyS75ywP-8beZGTwIaEs6y8wBXfVTsu4qVvDBODhCydK2FbZ1DxfvJxdCBFhsXFS41y78pLYEKDHCrMr6FU00wr40mvAWCPo8keoy--VX3lq3V00fpR3qMzd_yCBGeCq4BlUtAEsF13fD8i4Msada2dI2bidad7NjpZExDosyBzSiZSd6hVGWpr815_IqFk_SVFj_FZzlZ_hgy2pSj8n-ll8_cD3Uqmzo5vsQsh0NWAsEZZpSSPVMY3678TCuwq_UxFvstDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALoH9ck5QTtsaRQINJcnqABUG0kNGHuCLahYQvhRzy1wkQGysoUholeiJLhxpHY5n8NQm7rrLmoaws6JEmvke6iSlTHcJFEt6Qhhq2peHdkG6qqS2-Fa7Qu2RYTNnki0U9AViJZ0WF8PIpatR37U0w35vjVGSn88TUjwOxEm_HMVI7k4Sb9xjv5D9avJZX84Dm7tWYb_GjpeYYWZahUq_VNiHXQADNVrOnBMFLL8dBO7qhiiqCTvEQi3MiKy8Y0xHYkWNLgw_DdQAei-rfruIkqI0Gz0L7sismIxO5J7dwL3AHuFtoAuOkZMPV9HelF_YcTVKpfu2N_byPh8BeBNwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFBBkfdXaqwBP1dnDmK0eX7od8qWtX9WV5NQufs2lsn2vm-2IAZZmCNmpYSp1ewnCYnayJLu69ahB-uDi0bMRHUR1JRoOAvKF1nP0_JhJ4MBUgdJwwIc7Ib6snkF2uqH1tZNL5OqZa0uVR_7pbwGvH8Va4bXFrRGaXdl48bNy0YivPw4a_mIZL_mOt8d7cjW8Lhs0x0eeOPSEC4ud-SVqbGrMatrbYBpPFOAOaF3GYkqdhjYTdwpBC1S7MdEslqg9QBFw0lQ9-F63nNp9ZAWgYHz55LB1yYQJW4IPXOKZdY_x7dewRE27MdRbtiHvP0mAZSqDi6CMCsPr7kusyT6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1zWtd3DGbS3itEkH50qffbx1Ch0QIYdbez57z9i7gTCZO4Yqna9c8vo_k6Q9ycaZc8ZoKzgIs3vLDI0VPkrLzVxEzvmZyQh_reJ2F9Ge7N97wupOhs5cFqlQFHXYuJAcLHI6Sdlr6liIglL50CdHTnzvDUZkjhoPNL7mwNE8YxuDELtXANYdUpjgk9aOBmnIJgRxpM7VX71SZCaekVS-95JjgkAWvEuRBPV-k-ZWfvxqLe_Ifv-39jXwOw5hJXVaBK8Eshorc41JwSSajmyHuu_Da5mVAkGNp7mQNM5c9z1OZo6-TyGmvDRwZhAIPCoCkoxSCris5MUR4j99FrnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhUq06wRnCoLJ2PRUasul3kZyCL3VYaxS0HcerxETds6_8K8YwWAXo0ldWm_9zoOOqtphCjoiho_nQ6m8vnKq0P7CPTOoGQoKCGtR_sTReKQyHZtB0R3ylOCTQiTrv3vSCiDCYsRANn9H7KjcsQ2Wl86E71-gRjmuwZ5OghSTP2HPUEozTnoeUYuKuIU4D-xef6DrRXNnU9A1wYQFyIw3O8iepfYvhY-RH541E-UCAa4qyC5F0NWY-RUemRqtUX7x4ctRmg89WxHNCFcTXrqHSJjW8gnVOadMwHV-WThR5hamWTonFm-CU1xsewVg3gtPCdKyJOs_iWZx6UM7okvlg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aAL7feJi9kfUXZ2j-x25lNtHuNx4TWTNA8yk-lBO5wawBXEGWVR5ImTkDTT6bnLW0GeVAxPB6Ph4UIbRO5bkj4Jaatn2p3NMPhc-QkGEqhnYXc3Zf__J5tUMxDQoG-nBY-0jc95CqwkLrKw7S8SA8f6ZnEGuLeUF06bd8iJ1qNO8m7EtiDNQh8NQE9gA6CjopPPrImMoqxeV3stzu49ZstKuD2TxwIaAX-lqhjWI1SeHrnJKmgs1bNB4kI3Vv7liJt4LVQuGs3_2iDD4g7TIE0TqKQ2Hc3ZqVQMnYCCu-AeLWIuSZBZNjHHsK6ynzx0RnCJioWISEHI7zSXx26TpCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aAL7feJi9kfUXZ2j-x25lNtHuNx4TWTNA8yk-lBO5wawBXEGWVR5ImTkDTT6bnLW0GeVAxPB6Ph4UIbRO5bkj4Jaatn2p3NMPhc-QkGEqhnYXc3Zf__J5tUMxDQoG-nBY-0jc95CqwkLrKw7S8SA8f6ZnEGuLeUF06bd8iJ1qNO8m7EtiDNQh8NQE9gA6CjopPPrImMoqxeV3stzu49ZstKuD2TxwIaAX-lqhjWI1SeHrnJKmgs1bNB4kI3Vv7liJt4LVQuGs3_2iDD4g7TIE0TqKQ2Hc3ZqVQMnYCCu-AeLWIuSZBZNjHHsK6ynzx0RnCJioWISEHI7zSXx26TpCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn8mUHWR2b8iJW4r8tvRcCpmqZ_uR9swFfWiNav73ax8OABEW95e15r44QOXd1Tg1QQz9YDd91TQvOMROITSLBq-iI-MqGnqVltGnIy2vKMl2anKlIVciGAda7YnMH5NEAyR44CwDMlAoZEBh-dvyRgYFTqNpaUWwSwNqu2muL4_MoxvtHJ29dqakPMyeLOGYC2DnCP7KBnWD6wlcpxffGzhWEdDeLAo3tyWXtDsC8x7mXRsM803knNQ14HdUrAV7grQWdMlrVcNW1ZBG6hqcz34UZdD18nrUcuratj-zt8UcDGo-ffdNh0PYA7exfQF73nn82IZjXifmtmrzCjI5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAc_LFkgq8Evd81kwiyvrZsMZKTDIu3RhdK9u9CE76sREveUY0ceMe-zVZBvMPub_5t2CXWT-UJSWr6WMRWuMOj_IIW1xXhSj54393Hgmau7aMPiLdy9mu73ukyB4-Jm5_qRyGL7E0AQ4Q-VlY2J2b8Sy8KSEhPZ1NSHsP6mOckRSJiVrrX89hKTfJLFU6U44j9XMvI5kkLde0WAIw72ZTdYvGN6KWwafRuCDRaRhsaU0v6-J5nCbgLbnlmYYlb6t2LSBen7jWE65dX69aK9tTSmJNpMyCxU1nhnF3W6OPo2r_z6LtSwdcHgvBAIzGB1dNh3JnQ8timWi5bquP_sIQ.jpg" alt="photo" loading="lazy"/></div>
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
