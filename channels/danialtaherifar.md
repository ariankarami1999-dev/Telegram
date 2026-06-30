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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWdGJ10-rC89ljCPsLTsFTFKNru3jRger5jNqLajPYWTqAWlAEb6NwUs88T-s2DYFwgEQLdOLu-3SiPG38to4bGhnUhJgfxKFKtGoZFMzWf-0XhgDp4A8U4jQ7Yq10xxRpL2iQ8K8rmeQRTxdVBMPWvxIN7vlF0ptLP7mlikm8YF1At_vkKASezqsTtFPCLLFv-0wDfZvUszVvxF_pClRPODIvnqyLZ1vhedyxmrrdULmrlDye5OhDYr9mfVfCJOwjZw8Kmo_ci7m5M2Qs1CLROOfJO9tDKlreTj6ejcdjaMGtH8wM5zINm3RoZFl3YHoAvvAHI0o70OXguRMHhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 288 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 509 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnnNf7sNe-3qznwXc27Euj1HdyPphobBHBY5Cpvr-DXXfNTN1VB9l6Y4nBu7OmJrA5XIvbCophCdIKijdWQwC46_rxABbKAX1CCqVV6lCn7uBtHSYHPjNZIAG5yEPuCVZjkZkagzLfF9GbfM7a2jWtG-zHDt38ejtPhw7h8wKSUn1dJDhtfxJgcTZxhHmTR52nI8ZAxvprt3J4N3Py3UfAMTHjOk02F0gBv8Xb7QP7Q4IhNjm0sbA_7PZBuW2xdESIsKPIpas0c2nABII_U3wT-qalhNUUth7bf5a65cRg4R5uYaNsj688tIjbm0Ec51qsfkbcr5ij57sihh9Z23Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1D24iAOgVinrmaLXn8PXsaJKlnGLdSj4feodgrYMOEVebblno7xqjukCNAew5ZOaM22nq1P7X99dFoV6mdUSDK-U1v8yocgfQDqE_83CBBOGhjAizO0_hpybGbj645ssB8c0OE44wl8029oO9sJSCDXUODAutGSqOkNJdANgNPaDL0OdjkbJQp3gtyYub6p3VAdg-1naPTaeXKegH4o_-DMAVFGvlYkePPbaDkCfUUkEVPvu9JqxOnbnCOhV7fZv9PlA77iIlk7an4G75iheYIl0UKKtuJYf4UyagIWM5vf1Rv5cIgtvJoQXB8ywQnjkOjliJt5lNeTcL7gE2QhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9BUxeOaXl8_WuPNC2st6Cm3iQt7cec4JrcvOp3jC6C18ZB2qot5n-896Kw4QbWIRxsRogMKwLA-U3HmjCdfgbtg_P0knLQyfF1H8lwx_tB9jzWzhhJYlv3YLaNehmKF20ELInj3Cq5fCFXA9LgJ_VpEyNIKVW6n-5P-G4Hu_mJyjcy5zBqg-PtSDjQzngUILrviePMvsZAhOTnDUfphinpQQMsxyI8FzdzoA8YPi1EdDll1BXZOFeTdrEqm-Bux9MmQl1ywkIMT6VsNBpPAjO7L86Vl9Vguifr4Vy5RB_9BU_afYOaGvtuEK2pEKnuIcf2Ts02SJH1Q1LMc3FpVLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX4wUkGJOhl2s7NAJqB4U5Zgga52F-AUfgYAe0jJFThuAqeXokNJR4S5Ctu1N6YEOKGZz43slLkvdWO7zNExcHAcIjeUV4BleAoo6NdPeReityGqpU0EDH5wCdAh6HBSfpqww0cAyNuVWYXCi9h3fsqDLxlAPRAXOkbVZTm2iYR94gYeCd4LWDPuMpkaV3m0-yP0ET-j1W3HV5rkrzHqDyPi5KyOoUvMyH8LRh7e_NlSi4c3mE2b9P7IyG-viXAy-yk28Tdw4UoaKKc6H0VuOL4molvSUFSIMvc5h26e_FExyVbDB6IHUSoFEpDjQs-Owl9L_q-JIjrzuHe7QjnrHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O43BToeRoyNq0W-cGY6AiU9EqSY_lTtbudqBopfGhsCFLvg4KoqNpNn9-AKkrbvQs4rL724ql0fORpRwXC3QcNqCGlJS9d1CGgAmiF_CYzZFGV19hU0H8pSAy_65xI6gPXSvA_RGyw1In_6wOddWiwKtOAAGn8Od6qXE9sH_aOHyfFkFfwW8AzRgy3l7cilI-dFy_N_tv_qNiN-VxmzEDetI9iY3Uq4ZN-gasnnNyvbkP9RaoaB2DFxhPK8GFLq-Pt-BUcKxQ-ZFV7yjX6o_Ekjuwq0rQ8psPlRXkOq_0d7OLkrjyLXvClHL5LCNXRqQWIhP_P2OG96_gNYR4eo4jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8ZHY2zKa8FLVORTcmilPrQWojXDPCwSabHIksN6vPIBVgq_IdUW2UTZ19O5_PMSEn0uh1PdJfKKzZcH-AdoPSIQnGCU7NTVgFTuJicAbxllQluPZwcZgo82ZIB1kafprEohAY23UcqrCQ_5UzRQb0bum-ekjtJawOcyiMiVEt4Ue-aE5lcGdJvczPD9G0g5zDQg5f58UfAsl4BG1wjxVkmoodk0D6QB-noV2u1RZO1stnK-jZ3JCJCvUinhNV2RlIheu6pElaACHZrFR-SOHXxdQ92uWjyCUVx_0rcj-7FlRjWh3J2ywgdSXtZl2QrnQB-EZrEzlS597Ip71M6uKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYXZy0RcGU-sHBcBZ1SGHp3IcJQa90dmizGBx0kr2nWMBdhVEjbm3ZnrudRoqyX5BhcnKJjCPu5DMdQEBOnit345UigUC5Q2lP3RF8n5ScmrO4svprDa-OAKpew0j5ZTTa06SZemM_pzyIOm3dWz8EwsvMMQIvl-k9Z5j4k0RD1uletKjsgbnfwirRa5jDmez3VF5L0wCW6J_M5mhsBm1caO4DKjZDb59pWckYo3dzTB41iJF3QBcOFtU9MCUEfiyYB_HwCWytX4sZXr4PCK285GDZYYnRigzC-aGkqeitjtcoh5qB52cSqm9KeolwvyaveY4FKBsZSdT2TvUwEE8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGb-a3dBokwZHznpvVmgCWwsxSSgvbsIQEyyzM2H2JRy3TKc8u15G05C_oKu-mCSS2FkcL4AGOnkNza6bySzYkGs_QycBDmZ6w7nODj075IgO-N8SDPO3XMzPybOn4VldRwaJX4lBXwJQadql_-Lu1xoDad65OJcAXf5FW0dGUY9pGr1WTa9uxarGSd7DXQC0gsnKyTWjpObvPx-JdPIJXDDv3xdABkj_ig66dkOfEQdxM05nLdhUFx8P9yATs2vRJtweEhZxEAoz4mpH2IIpih6T3ZdDZz_IDdwifsGMjlyjjrjYtYP0NUMOelu174yhqMpVFsP375RoVa6mXadaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRAMv9AlL30OSWKCneYBZFfbnkdE741t7h2qjO1zfoEu22v-KCydzWNacJdtAVUQlmhS8tumsbvymi5wQPbhNRZZtyRpReLZyXKsOLhaAIoHVihO0CggRYD9KN6VyFagC08_VdFKIWPjjEzEwskrYIe_WaRKMrNR2EnZrzcDTJthFA0_q62mvrgEwXrQqYdd3c0-j1hmTx-cFjGnbpaLSq43DzOeS4V7oCZQ0lAWDdb3QWjdg_MGoF50jWNOnwyIMNbDIqOTkM-JMoDJhTVHlQTQwVd4Bkubu2588id_PlY5pCjbrcwmOazCdjtKJ5-lOBtVqy3rGGw4ElYxjIzYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGOJ30-u5V8FnzpPt5Ej0sWyT7ek4K3cvpE2_3WN-LUGSWaxltGpT9pmnmGmrCPOBKjWJ9DozKYt33C4oFtDRJlbU36yzV_v90Ho3nIAgkJAM8yKGbX9onVOPmlp2nfhc49_Lx5GIMJxESsIoLbF9-eZGUbZ32QHnFOTzwb31CD2MAbtOT8U5QXFrO_Nf_ubIO2LoX8U4bi_0-iDz6IylwBkKkGFWx6vTQyyS5hPG0JBkNZEQv6MYXeIGhT1Q-xWSCkLDj9bg6T73NSABatJifB5ZR1eRTT1XqyDxiCAAjce6b6Gq4JfFTXl3FkD9YT6ZdNwj8uVcLNq5iQILttEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFu7iM9glkOChrtmyGq7rCd51S_fev3DylfOIcK4ceN5I2QmB22ZjPAxseifVXtie-VH6QmV-OlyqtSjS-FfCrCcuHrVwHTHzEf9lL61sEq90Q7z9aNHLQqYA8iCeWl2bGU9BdfwAtzdZxF0g31B86Xc6pLLNzTtxsezlIzs7G3EBRZi-R7Km20QXqiRaZOQCz7viHMOXL7N_auIRdff6TknBcH5WKTLVWzrqQmJgkmSH-vLIIQSFBu2vj7zCdM_Q2UWyQU5PngXZhjHQnXuFgxfQMZRJTGDSKXeSIdlRw4WxXvAFBz5m_MuD96bvHDEkWAhfpxcfgLHnuszShHODw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uszej4sDNY-GSR5KqdvIHLrwbp38cLCGToNcJubCZHsFvtD3MHTDNFC2g4fUKQYypI9BsxBVQss4bgEpoehfAtc-P8YwJ8FF-Kpw7BYMpW9eqZM5yFE1oYM-q-08DM36GbhBs6yQ259NDuCXrRvezAEl1g-4x2bC6yL-0yXUBh656K0dVqWZ18Y3ZAksmqKQ_Od7oYlNaNQUUuse3dUlOHDPsygj4yP0vvPeWVXau318yUw4xxyBwWJh6N9HfTMycVf0yji6DE1Q7eqDjC2qYjCbzIFaBFTmuOkSmcATnsE76lbu6qbLrNUXRSsMWRsvkfLtS64GNo1f197gG-bBjQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ofkzKEHVVSWFEemZhCwMp73gjd2TXq5HMtfC1n-Hc7CdVykFWzUfFNJ7actmhViMvHfxGBoaFCmEupBeeUtKPWOGa_lLyOIXF3F5KKM83LEFTLtmCr_OzUaqpmHaJXCYhPluxvz5KIH8-aMbvAjtLq6th_jfUuVLSbK7fs8l-kPwWbFdiwxSurjqUPfUJL-0zWVYVyONF0xsVR-On93J8b84nNdtlR5XoSpYNVHTbTCiM4ZfDemAeKKicMTrdg2HNRDf1brUieghcIywUUoyVQVUhibBWZaVOgaXFbl9DocQdloa5Uix8oBQhppIaX1NbMIM_qrFVeXkdEAIgzVHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ofkzKEHVVSWFEemZhCwMp73gjd2TXq5HMtfC1n-Hc7CdVykFWzUfFNJ7actmhViMvHfxGBoaFCmEupBeeUtKPWOGa_lLyOIXF3F5KKM83LEFTLtmCr_OzUaqpmHaJXCYhPluxvz5KIH8-aMbvAjtLq6th_jfUuVLSbK7fs8l-kPwWbFdiwxSurjqUPfUJL-0zWVYVyONF0xsVR-On93J8b84nNdtlR5XoSpYNVHTbTCiM4ZfDemAeKKicMTrdg2HNRDf1brUieghcIywUUoyVQVUhibBWZaVOgaXFbl9DocQdloa5Uix8oBQhppIaX1NbMIM_qrFVeXkdEAIgzVHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZoWzIaOg3panWCe0BqpilQqTU9kWHB49F8CQosAcrTLApgfnTySYZJCDiavKUs3GWmwUPU3wX6l61KSzMztsSgJqfO5iy56ZXaf_hsoYY2FZFAB_yIhIr_-BAw-ZOWb8V1UX6zuDkJ05gk5zZP0nIMjkWY5pNQqEXwUOOLJnbRG9IHjmK2vYTTUoN5WyK8FBqVyLlmbq9SwivLyID1A7r4tl9OrUdn8j3Dwnion8rcEdr--lmGsvFH0c508DuI9tHrUPyQhNEJXnaIl0lavLnIxm_HWnsn7Zpzf4Yj-x9XZVeZRJlia85EIyLmvlV5ng-tKdMEd-xkuw-7oPagHzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU-KqpCWW-hFqjeWzOSZTcF0Ucgm8FgMG4zOF7_VS0qzvlJWM3kmwiBM32rF2SKx9lF2YfsjS7mw7aKe5HpSygIUofUs1KWx9HSgxcL9kUbd--M2eeWJcNzn1Yckef1SniYP5LgQ5gvt-6PseFLRcKt3oPD73ORCHc73s7FBcgHIzJBxjCVxC0HW_EFnpjHlWtTvp8cXMtZ34YOMMi9d7ocmPKpKABX95MrJ6Q6TN1IS1d9UERO3ji8wrJpBokohebNeIAmigABpvYB-39AMY_maMcJcFuyrjEeHZS9cJX3f7_WDCNvXfuBsqm9zt8TeFJJSwXTZw6FDxb3cRmKMxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLkMXnajkEBbDa8GJDY_ultxIS8-3V8URt92vM-ThusMwbT-K3Bo2BD3leYTuJWpoKxATEzBVkVNbzZTTpVu9IRgmS_2BVnwTXWKhFee6BzMvcX4fMOXavFBFKir6jj6sdP_VVBzYR9uVZdJfRD2bLBwtmt85T7maWqiRoRFytUfqzOj64feasKFaL7SQm2YQQr3XfYjUblaFB1MpjYaKVhhlnsVeKfoTTB_xLFkGBmy3usfkZfAu1KD91Y4spgLo2gDHy4JpIX0J1xbZvMLl1ZKwh7hchXusUqky69wTpL8xIsSc7rbZ0VdPwnUyNQxCg4IcgAUTOA_XnYFGl8erw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCF1ZpSmvRFLIuzjnw3nJ49uwqNeCw_znmuTJT-fky93ZGO2BZA-bF7p1drgOTNiYJz8TaKSKHIski6UJwp6z8aimCArEqGJIlntAZLjZK10l9Le2R8Hp8ziZ9Pk5J3yT_TibenflqofJl0hhdentxm8oZh7aGYyMCg9rmHULraONqpl1CTiEzOaT1AqKKSlSv1-7rwpJbRa9O-ZqIcU79p7jsNT9_-nLP4tZWho9oLmGJ50mpWX8O8rf2v_2AJWZtyKjpT5W1oXrFSF6CKfz714llt_26q93tYoYGKWdZvu1aRN1IagaqeYfELp0svRMLJcBn32vbH_z-iozXu3ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtR_kDFgOJzePN0dnTjz8K6j8HLQ4ShulG5KuIf1YXqQapZ2qnQgBPWiAob12Rt-iq0GjPjOXAgGOw-9Ncvwo2sI4mqOIdTalBdfdNpgqgF6l7GxWWOw8ATjsvHBPTXyRPJ_kn01tYKzX6r3BCCs-5EsOLUIIfu1un3wvdTfLKCres40NQoInZapMh5hsLysgTqPrsje6fbpLQT9uJmXs1y6Q0E6Cz8EdEGWGroWnzw19pXU81JOG028wxiiE5dnnZMw8-wVOLfOzNZ_w9mVZtIQfgZ7nYtBTUnheqVE0bFP3b47vCwiqJupjdIjgU300XWbRtNg29QLCiXQHdjwXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qexz2vOj2Ltj8Db4sTaLzINBvWg7ZmaaNHyHHdC_-xIRaX4aW4dDVOYozXcp3duNlhAEzfjrjoHPFG-PmOD4DIYDxkkVQS1lu0qQzmwNkNtbpetHiliZMEJLxSY1jfxQIm9uyHz7zSl3ZZeFoFOpFgv4LNhfdOBbB_JFfcdHCV5QHNRWh1Nbdv_2OaA98X13xcLBAWdTjgxgpMSnh6_lTA2eC8oei9sBox6bzPY3MIthLeOzCzNQ6UthZJYLtCeSaBrVzbJmTiznuC9knAZxjwNekM6FdD899eBYEio_ddg4dL0n2-N5nvEdVW13bjQ56stXYMmMkatotLEH0jSzhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7FzlOgmpMI6duLGUL1dCe8SpbgYBP_RHZoip1cDnEPwj2FJbjkiNqVElJcLqT_fR3AWA3LyPwL6bhmTPiMn4G193v5qbaYzDlJhsRnOBcRVHoUdrHr2SFQyuqu26xWFMwesr9MP0iOmaI0DyTk7u4Gq5e3uIhMsLWAvEHLo7Jw_l3HoLzQ2rrmta4yhlE6pTyxf44cvvpkU0FpYK4NHNZIOFUO-DetJZR04OMGvOxkyllSMiHHdU9oJT3eWH4NuYerd7Zb3qDf8zihhvNDk1XJvad5CxPpChQ61zNOe8WhVqCDYJLbdakEaHpOUvhFoG8rzPCxFvVZDj6QPFXj3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEmOjj65h7-7m8fq89rThH2bue6IqMwh2CJaXUsbbMm707-VJ9FuSbB7pTacF5OrBvlNyPF0yg32KhIiGlhwn7tGo32r-9-ORbj-d5uoygOO7J1pUOv6Hq1W7CH_UUZLSQ1wedIJmMx_nLYZViOwHLvBuQpaVAD5XYVZI1VI4P4QrMwqrjSgAutQ_D5NqjgDOIBJtpR0SU3tClyzB5KodITNKqQNMDFdG_6Rs2Il84I5UKRDLpkkT1zY6zEnuh7mgCC2l8kt2CdDAannFEIMol792KMaOXsRsVY8PC3Ovb5aYsaqcvPLc5w8y9YXi20v0Iu5KyyUEUKiiccyV6JRoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHHqUGvZSWp-YBnvHU_K6GBbZeg2aZjjeRLdeuabxewEIvQZAFpZxOtIDsX1wPjeLqg5-qq4iGZXmfXLasF2xOSX9Rh_l4ZLfiht9jzbq5cVMqGL-ZnRdUtZxhNVaxAuN2QxjhWXoLPYe4Wd3e81llZJTOOvceU6sooWezgt6VMf5JcB6GO6I7KWy_BACSvRoILx2RYS2-ACwI_pG63ZWZdwp4kmG3UgGdVil3QzGS3WW0uO9hy72H7vfnyzpDVwUG9Y4RhmNpft7ONOZMDrjv9_2xmOEFiaoh5X_Jns1Rgwkwjlrk_WOnzBpvaxO25HEzEnXilRfCu_L_KK0JAkLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YulTqvRy5lDffZ0liDh7vc-bd9rwuz81I1wJ9dzmzc7UiGMoKKggh9FS3EUhwalDhj320AB5RzDdgGUItuconv5EZ_QJfGcXzWYrqE9stVXNfb7qkfWHJh-m8XubWxCsGdaNaszIZr6DN1yyp2dHMH9kF6ATEh71gHMY3X3slG-2hqimbIuhhVWwHNxSD7Xm0IKJHkFjgFtXuVGPHpRTZl1-r8X8muhOainXBilAOB3vQYYsOKsISo6aOw_O_ha1LQsnzwyQMJkymNmWpWT0ZtNcz6um0E86drvHxhtXudEStv9l2T_Gf091UOcyclw9iH5YqmVFPwFX1i1cQ9m7LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSD9uxwCzmYJKrMKZhrkPBdzb0Ay0mFd7OJ-l2xYPSy0faCZVvT50acE9arAvCaQIduCHrJee6j5Yevv9on4QZB2i6vAiIELu1BhlOsvZ4getNnqHz9pQ0TohWGMiKp1YZp0BrJFWWur88q2s6UPjRo90bqi3NsyLx0luR1l8aS_hp74Gm09xhx4TqBcMq7FL9_irTHv4-VohD2UaT31C7uxtyt7ZibkPgR0BsM167YOLJTeRUFRH4amMI98xsVp8Th1GFiZvK2po1IhNI3CH9T-1W1HJaOkmQsD92NA3K-K7aFPDuye7o9_urG5wEePwJ_2wZC27OcudTAFjrXDAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWTrPKjquRYtjiqDMP8rUfo06Uh1rhLMbdAR4YMfTQOGiV-Q0JfqbNLs9lJbpZhUOyBLZSIaRiQ42_m98BM0AO9ONMu4BG5zdodGd0MR1nBR-ZteKOchnunPSs9puZHBWmaMcPrOTYNxNSpYvI8n6QfQG7Nvat1CZHTCh_QBUI8QQJFzlAsJChkJyZ6NIx1J6UKOdu--uknQ3FhWcIB0FbD_eHP9cKGadq_EkGt-0QGdK-QKHHgy2V3Q7GlA2IGDsJ82W1CUuF92niZN9On7SaoHhKPwdCXRhrD7K_eFGHx7UoKv24V9dukIfPhUyBNcZmSrjUmy-wCw0wQSB8aq3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ab9Shuw9-TrW9wl1F17tKlkhCKlxbV_N2WyrTFqFzezwMIcaBbuXrLyr5q7M9VpC4f6bq8rL5NB8qfJtaPceYSa1Nml-3_Voym8a0J6gZBIhUbR9_qFfdDzosWll0ZSC43Xtp4cHJHIw3mJky_uW3QoExJHg5hZ1kSp4T7yoEEKyH07dddZpicF9LZoUfluMzke4rJDbgX3jnASUEisl621ly2_PQZdL1sairhvxGLQxj1A0_8HkTLlYyg1ZijuvfnEmJ4eDXtUsI3JEa3gaOdAn_4zSQ8yTBA9SqruDzhH8OINxryR4ne7lrPYuXlU4X4Mn4qklGMVAzKdN3kgJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9rtAMmAtKhvzVAznCDarvWYkVzuaMLEpc10eMHs5Zz4ceki6yz9UB-SsbjU0VOOXFhoMfZxvCv1TxhPEdobMnJoKy986G6_rtsoJUSWrmPxDLo7Ivi_BfpDW_cT-nJuoXqZiK_AZ7fUpb79lXlkC77TpIRts9O-N1IiDCPAQG2tUu7ybuD30jwYLadNUzrKPbLvNl0hTneQ2Yod2bZ7AGgm4cB6fYzmh84jVrjHJ18uNS9tnwKH-vJWIoFRLcgwKBw70YWMiXzg5_AwUo7Fd_N65iqWwkJ7MjBPgBqUhlWCYCPifOWFvlFWONTCDXcibnuL0eiVOvaql3dO5UFS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mf1-fe8NW6Buswv6hKR4HZyzpiAc20xl_DkfV4UPRhBx5nWBDHsaHrPjWdGqnSslP-trop_9zXPZYmRXHA6hZzgzzUUnS8CjMRMZogcfGnq90iAA2mNhvnhxjjYi5rNKwOiiDXJq3eROC5SVUj_aTInrSvXfgs16Mst7Ocy5p4xH-lFQtOlYSSAVn1zk_fp4PIOxyT4PArKHV2oxwy6c0b9W8g49xwaI9uVo7KnWDw1P5RmRcHbUOMjCXaMqfsaLXiIaNIBI4nz52-Zf37AVG8qiBpgbSwMoXBBmaDUQRZbeeP-14X50v2F9GdrjOjAJXeiJ1cF5Kr23JcTHNHuAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdd0VRE1QM5prHA6USSfQp7q0CO2pDCo4DOxIqxxQie3tnlPw31YhcwjJZ6nW7z9HFSBbupE5D1LoTigmf7hPButPd-L4QL7fDdV-it2LxbflWVSgywTyHj9lk32RDGjRijTLzzEKribKoefazxxFeMZO2_u66eGO_wRNBVJZY0vZ41cOMr0ibehR5c0lHWAKPvYIYSH38NpzqIgRuT0_pjQLcfj8cWhArnp43KyuF19PsWhhWFbpOOqtd1atqTYRRux0hEvn3iYEvqcfHBwYnvUCFCrPG2O1pYI0dBd3zqTl4d3uk46y578Q2CkohPqjv44IYirl7ZlItipjLXz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naPJgJb0Scg2Cf4yazDRY-IU4vMejJHJC3f27-RnGPJ2pL54_AzvdSSk6YgHzcW6vvWKcJkHS1tQVVv_YADzmeJbVfwv7pMv1iSEd3gLTTkkHLXZH1Yhdt0MKpEVfJx95_XBmTQ8xYmNd0cjIjZPmuwbJCdao6Uw5P96YKJa8MDWLic-Ajxh4Ha9idfEsLf3r0CcEZVAOCue1IqqqC_CbgIIWTi8Zm6DuGbObdVkC0L_wmbaKzC-YrkVGopbwwz2Q1aowSGKQsgP-WZY9yxNQ0MmFJIcYpFkO_ZV2pLjtPCr9R3eVnU48ruMkm0pfOkbuLIc7E4hbSpG3TD_5vc1vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWFg9M-iJuo0TzChUqw1F_ueSA8A5dlKEGqlpGwZUrM3khe34X_E1M9qFI-1sqivHTC5pcFGe1UgBpDQ27dZrWmxVM9u2AGpvI4hRxk2G-f_zv_wU-YP4JZNlgajYz6jWysWVO_vP8RpRY-dX0W70xmWqruK8y-qWdaZPBOStmSNB-TcGyy4IrYwAqlWVeIF8ABcMh87swI7IxQ7VLQ9xWe4CkxXszBfSUro1OIrEYCQOuyfuDenEVusGJOa3JJ0Hk6cVmbQ9B4e5G1mrmnXQbkIe3prKOUviPBBlHmyvntYfH9pOxwoobpTDZN-huaZq0jddhaEkKxtY9pV8BpV3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_lG4Ymnyv9mqB_hWQV_eR4Wr-X7mXqR9E2GJ2ryJLMC1HNveDEXSibRtbh7bqFSLB1R-Uq_zKpsaiAdTnZCKZpgGKgW-RzprJTeb58SsBeupFsFmIEs6iaj767bOFCQF66DpoOnD21dL4gNa27llaslfcpr8Ji1OmcFhVUPpx4D8LOEe1tHx2ZjfnvMgsW_C57kCMKMRMrs3nJXjBwsiikamQjq0cI3kBcxPfSibyYNih--Gl-llRntXXl6rciGsVheBELsv64GWVUJl_p_Bn4rkRy5ciqYa1yDmSRilpkbqxP6SQ7v6RdsE05x_Bb6cZ6mDNF8h_nyr86bHy9c4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMxzehYXGSCseehLHm6I3C4upHTOJ_NQH575T5UtUFQuAVQVavdifJntgXx0Te4oaNA1tlAA4op-vWQ6cKM-D2PH6lisXDCiXNCoi45BqBw0F7lE0W5wg-CIJj0Zb2VpOEZ_SXO5tl1D6racL_-GZdMUuONKngCO1z3ndq_Am2RwJS-opZQ1GXyjvs6L9wbi9VFSTGJm47Z7JfLqW2A4tPsKNpi7SrmgX8v26Bt6oajYFxJeAMXIA0EgNOBbTpEAGM_2VfhM-B0wmw34tETuxbegSR-ShtYwZy8onMT7D3j7hhem5TPG3IhUkbeOW4lq-eOljgA1dkajIIV1otuG1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyLbTgtDz7HAoqxH08VX0m-_fY5KJo9ealyuLVofYjSTGX14ewkzbw2QMHC6cLYHWgIIcvCqqSEVx2EVhRGYEQoSF7n8CwZaMTZcLHY2MYG55GymGpo6o23LmHq0OO66sHxrQisQBBxlpeaPTHIJmDFSs2YCJJSEha6rGFVbGZt1JYKIG1mCZq6ai2smxsimzN4GX-0JGXNWXkHgSVqsOU4sNus6scpVBTiLlIJ3XZ1zkA26UkGjMY-h7BNKFK4mSI5S1tgBq73Y8_s4rEWfTD4Kb2LxfgwSFso918hE_0xxe1V2tsV1gBxSX-pIE5EsOI8TpcbYDRKDaeI_AJCyPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne1DtgfEFUxqFTdFePg38lIIBJGim5iy1C7pENKNAxqxR08zG7mK0tYm7U39EMivgVGhqVdU4cVG6nOlKl3qGrINQda5LHc2fcZ_8yZki725bSVE_Oaj-LamURFWNp4-qZWnGZVlHhQ0DFwBwnQxoVKoYRiWi0RbQa2gDhx0vYA_91MdM2232x9MRelvMyq2ctdXLtS_eyT68zAwgQ3QD51QwkKTiu1BIJ4-2hvxC2TGoXqUgvWCSb-rY5-Bj_3WmO4Xb1z8VBk-NjF0sgP-qaRscG9YzUl8hDLgio1S1h1DalGx9H2uEU8r20pEf551uRh7VEZL0eG_ZGovHAQY7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzownyPl8wB59bkd7ffEHvnnR3kMKDEI5G8ruqD72TpzFyzdPY2GxUyk9CRSVYKIqgHrj7BjDuNHqNkwGA3Y7LHUhxMNN9DD75S_er8r3PNxjNJx6UMbL_ydahDpuNXVkAveL2aBDz-5YvBgjtvQzjMvCrJ5jIMgxD3ElvfBAh_lc84UKMjNdqIxpWbdcEm02eDR_FeHLcZbT7rUeK4XMdMI8RFr20z538OnZ_eHJFdEl96I9_0NehFk59lakyEbo5j1hUHSOEASjGP_JOkgB_JQezuWuFZ4jPee2YNJTm3iP6fsAIYihZF5mlKkXIfRJBRGHNGwJ5rKU7Tx1-tJMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wf6yfSFjFII8comlXoKaFNgZ_fLC8CeItHQNhgIn0GVWDhn18SxLi86hZkWocCZsIDGqqrxEX8VQkN1F2rpyvzreFW-LaG1mkmIT2S61FJV1ZI2JgF4-b2fIDIuYho8-sO8JbujAcazTbH2Xw85A-zsDk7N8SklPmX8QksW2EsNESEYGSfVMb7xe48X3RYPnqFdCSHhE3ePzfn_B2l3r4aZo_nGun9rTvci-1SmInhUrl-t_JCrtWvKY9ShNKcllRT_3q_qgKcm_zxShE9pfrRtuv0TtCls7aCcnF2V-Buf0L80z-UQT2zTa-xEdoJ1UyjNfjNS6U8iU0ETZdN5Y6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooRrlWIDIWpvDFtRbfK95JpGENYIXci4yjO000aGZ8NlgzGJQ6PQ2n4t-BiltTXK4cHaDU0Jv28ZzYPTY4OxnTej_a48M_m5Subcw45k8__5tF2WcCdpNpWnhS1QzBuJSABEAvK5e3P4iLyVNuSwSZ7a7-NNibWkCnbLS7AtiwZO1rRsC-AGuAJRlcMv3HfboVpNNXY5_czXtQ-7op69ufRT2WBPuZU6SfXlHeZrkfFC6F-vQ0tFdylfRnOn1Ay9ff-0wrwhLJIVFWgl74-P9281BuvNxag0IBNe6A2rbG2CWvQNNvGbGaxjGrBpwNDnYl2ADpf6B2g2M8UiV5o40g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQCg5p1HrOjJbhghn0L3DP0Xe8crWHQ49EcPGG8xDcliXA9xYkzQlQx3AF9MqBqzKMjy5F4UezG1NDhOHXyDJyIqD6Lc9zeIHPlifstDo4473MXHk8imkzATEF01nc7vOefMhqBPz7UfxQuV2TLv_q1kCx3omasUxSqQVwqnKN0hEOWMjh7Dp1Qll9y9SQaUQ6OyO3C38iCVkZQchs8E-3jKaLHAFMXR76nA7dJx6Q6dryBZu9V_9zLbUZc6by-o3aLi00UkLSjwbpQ05jetHke6sof0TenN85NuEe3PgMySTilLN-gcYwRtgK5Hp9RiEH425PgNiPJF8fm0VkpA_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_THY2MGvHhecSOrdDRT--icY7CPBBBGA7mXFNhMYj9Rjv43iy44sfH3kV9r_ygiTw0kT8VQFlXAf0M3AwTx2SZ3RDq9nDgU65z-NUpd6-WHWusQrqSZZwyiFs-KYAYFM5JJano06XewvI5RN_U-ADhl81z9uCe033uX69lU-WzWBrt-6HdKib2jEsa-eg-CTeeI3I1Lr41Rux_3qFs14ARHP33N4tVQJ8A_06R-ti_4RskN5KmrcxGsHcjhVuDrvmlksrRqODw5UPvNcsF_s1aSEIawXBuWQLsDnN3QaOFAToWxhcDPzNHdqpI9zwC_vXxSGvtkUapn1kN3P75QuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_M-8d9MsENX8PdDylAliGCpIGxJsK9Rq1K2cZ7-AwY5XXBGdeJSpTIRNX6-pYMREhj9nBEoQQHAjqSNhiX7IPMtuWBs9f2rQ2I3F8jB7J4_IA6TP3AUZxMHdf7ps_mM1iSoti3AyPvBqkjZTNu3jjypR0yR2i1Y5x6T-8Nv35lxu2LQKcnEXXIr9h9z7ZDkWbFWD1q1620xTtTtSTch_NRfQp1rP-lN6OvCyTGNtSA7ye2cKyO0-x_be1XTBE0PRMI40umgkhfFIwZFkWBdbjD7OABJ529-xMByjWSACb3HnzXcFWsGgi_9d93syvsgDRkWCuJzwNa7UFMuqbpfXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq3bzyjCz3aB3KL6tBQYT8f7GPHpKWczpdWIVBy8XAY3SZ7Huzt--1m_yisHOPRaYBuOYjILqYQWOJJqSZXZaWplZbPzlGE6_DJW_L96MsZFEjMP0FIP7yHMkPlOzsbbJoTVCQY-t_jPf1vfDV3mr7iUyrfOxIj6JHqHl40zhlyZL_S35_eZdcWFyIT5EaqlhqeAFdBORegHoY8rau3tfQMQ4quBM9vrcERGmPeFqQ9ctEJOUCx2IMrQHhoxtWrEnG46Hklah1zy_eZdH50Kbvngeu5SQIhDIw-F42v9qS_xW148AQIOY7xMg-NMm8jjHHSng_ElXp470nfOOaicsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA1HvTCsNbWawpIenl5mxeb3bd9rgQzPIEovrmTqR4xjcgh2xqHpDd-3r2CmMr9nK2MYxV2LXXUpTfSIKpDlCRmtqK_5xgAz5p9NqLXOs6TCLe09mvQAxEqldi_AreVrW3gjgdiCOTAYZyNEw3L4NzhvCuUPFHur4teiwgLe6GwjHg2U2Nn2CPhlNj-C8cVFuDFmmGwOOfbTeUtUfCbBDR_lfX9MYdseLE3vQJIJnGAIkI3E9rWuH4hHJ3M-vnziwTqKeLG6NiSXWQRoC5zjlTj6Z6fuQ6idLLuOZoeGjQjLgSLzoTWNCV54ppWxBZFCyAx5dR_RIzIJofTAdeL2Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwIcID-uYdgpQ_yVV8z5Iy25Hgxt_Ym35jZjaBqnEiidCSqanAnvRYT5aJfSFy1Zo9DVwolE5ftvqODNu61Xo1AJpFNqTH6mHea_rGEauQf_Mg7P8KubLzqNU9U3TmjyVK0CJZFv0krBImTu9ewTf1wAUBjISCDQk0gvZxWbuDBC2ly7k7q4QsfneRvm_U3TMiCFtp20zk2e1FeJDwmYuS4tdywK9Iacss-daTAXPcsV5reggBOqu40hkiyG6qAWx1gcII0mHrui6b5S2R8uG_BwF7UHnL1kE55E9qywOlgOJazGWFqGpiFtylTnW6CmcPbWZUDPeSasYj0Bu8eEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3APJ6dgaonZV4KW_fxMbHiwdLz6hqdIT4fPejX0XRkKrl3X6QM1tXALW4FCHup-uEvrJJNmQ4-CAxKgYaV5FvpaZPDd2fZNKhfJMezU-IJMEi5d3C6L9m4uWl8qQhlpUOWUXZGvCulHzzP1975X8spWYLns4AQ4iZK2_n654nThegzYR3FWWEcULfwaPTwtlQUvSK-odlBB3V-4odllNJ8XWsXKEGiOekmD9FIIgdrV9O2T0BTiv2y0MBMYPRZGKM9pA2KDnOB1ZufaQLjFQQ2Aj6c4E7EdhfrEkgzci8fN9xcUaOBdG-W7ba-YB5m_HzYV6j1pKk0tP5N_St4YKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-miCfAKOahMSJraSQxUZ_P026O7AydePJoGf0XueJWP5pd2EFJaAPvFcgamtTpjdkfNHhoI_zb6qpQWrSZPd_DfSQgPy-ZQ_k1ObRR5SaDUF5CTPvoOrgI927aNAHUBYAegDB-hZFy3iD4xz6vvMv5wCmpgzYf7nIWX8ZZkRriaujqlLCjGgBhSJZEgIulofQ_qMUAgobItkCGAcSBsAELgx8gBEYwaoElbOr_CvVZXEwZNPBOOypNaCUsehFAt_L0mJq_ChX68gbmF0lynqgGKhAG0oPrelI7cfZp3XmUZWFuRi0wmta6uZHFNN_B9udd6hJW0yVKM8oxnSGlc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DP-CC83u5K23lB8RpxU5O6F_pz7WyOv9QgVp2PPvS2WDh4_JXrUNe5G4jjcFUo4iiL8mmuwMnrBaDD93r6bIO2mcxxLWlqeqgs4Nfu4109EVdVTXbe_TNvRKEgZr6DZtsgz2mhyreU5YRpCEvNEUzRfAiRQqGVmckzhyX8kbhAEndQpnMGw8iwuRls04lzho-RmLKnubKnlCF7bq_ImwLyiq9hwYeFYgofXQ668bO_soj2X3joZd3xDtky0Tnihd4mmh698h41MeNxN1G3hll3rM_lCJg1jB3EzGFN80FAsve8MNaNCCZaxBTgWCze_VLaHEW6t5auQI-2S0AiS0pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8w0N-mdnnPgbxmZkJQc8FWwFl8a1seE8Y2V3MdSrBitXC6GuBnaQyH62SO47RRqcBe_tibM5iVnpF216lHc7GsBIjaFpHQZlb9RvdX75cCt47UHWDgtfi3TXJbIkaQzUYgpNnrR1Vs1OJJukV2D4rf-iSMuMU4wlX-7URGwbZWzDAKNDa-f5icfDF54_lvo8K8QE9qqnS5XIQNcENkS_QE5gwB_ZAosLor7ybYN8XIqdkEuCBDgknsejjOimf-9wqq9xJ8BJnq8Q3u6Mz3FI180XsOrfI634cw6euVnlWKGwl5jljSDVnGIomaT2NDhKVT1YtmfELHbsGpuptB0Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWiDVhd7BPj3jMSoNdZPXHh5x03mIyuCxv88Mp1Yuw9Sze95mmk4FMDuGkSq0DN2lLugfg_gR6S-U5XUt63IIrLVx2ALsN8AwjOnsvfsGW6yYsdVlITWwNcW7c0Kp4zM51o9UFgO9xkhT_96v00FiiKfGtua3Z3fUpIQXWr-Uqelj_oFx6kbVQuu4zAro29MNiqB0XVTKRbcvT5TqPNAIM2ZPhcvg_-p4PdQmPIs9_5Cp0Bd3SX_kHBXyMx6TXGKn7-VGlIOJeQJIBVIq1AbfbWlcSMGF4C-UEVY_dwoBrAVMNcH8Jaip4TDiPpc382p_u0TqwANvBm5iJyVYAPpYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFgaCBe8ohIEpesAYYryvrYEPVSQvpV3eFyRIG0vPZjwly1dBKWpOyT_AE6jewAiNP7hk9t2rh7oQu6L4YvOxWUqXNIiSqn6s0Dt1vCgkcsp1WtzJnknZMUwXyjNBrQYCXWBnG-OLLJyI_w9rmQDKx2JDuCTo8-U1Cwy3OYR8X4VkR_l70yKa-t09AsAq2TswGEtUy-3oI6robtrcyIhjkq33bRiX3zy-_cu8wrpQj5Fh7LuOl-sTIXUCipBLneNdLMg-9UAPwFgSaPHIJzRZpjdtq5Yh1utFWpDpLFHq5_MFshjmxbNslldD9bqUsul0e2sOAUozx6_HGNga-QxoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYv2MPXHZ4OEVVp2ecbx-OQL2TiOTA9uT-41Us9_svHMkJlttkynhtaA-FXk1UujkP0h7A0w0i5TXv5uWGV5gX8OYRTpNL5TwlEmbIjRK1YjrL9HI6lZYFtGYjCP22Z0vLL5B7v0KgtaZLTieQSa9vUbOMU2KEAo-qLc1TSVZqQJ6NcLPtbR6C1ojy9h170Rzd04aQaZGuofNZNMPmkZy39xLZHRwbSx_42kmzK19uY8irRLAPXIE72M-vGhj3kOfyQHotwTBNf4u7XrUnC7vMGCctZMHknEzGhH7fSKqeh98s2iFWVbbeznkrzHPrGaqWSc_fJA3hNu_eaHJAjDBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3dpYswkzxIe2sVXOSkqErPW9nNFK_zs0ZBoobIG3LYDTuOtides6Pwi96qNJVkMNRIgBrrZ8uxcOYhCrECvCcVhGIWxtNIWRm7DjT-g9cKtIuKICSX7He--DUVRFoYKrlJnLNU40FQN-xgzVRjAWm4vpWnwYxK9F4tBfCPmqCRhsCu6r3DR79kBUs2RpEK4p_hJkBL-OC0gzOTKorLHu2aU-KX7J64mvEynaKOXqKSpRilI5_VbWVYFfr4_tYSkZkhq6iU59Zp5gY8SoQ21_DRQc43wlJFt7q8TkG9WL_20ipAxaooXQVgUEuMzqfdze0TCEICWPnWIrJnAnWhE5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfQKSfF6gfDrCMAH_KH4YPaMa1rdKtjbMbKQpokwtqwC8ub5uVzlb5dJyK3-7X2RwYCZg6ghtsZza9t-DjIRc2443Qdp7b4rdSIueROQcviVdPG-yzQz4erXQiFIcoUqBbswZFBti1uablfNbrunNZizYToNs5fDWI8d_RXH-GULg8G50EztVqGKjseZYbXNCnh4sztuf6kKmsfmbY9xCj_DV6R88QhdjNtE_6Yt4JBokPww5iEzmLAWgPcIQ_GqVzZcPX76HyBr1uwliRCPSHf2dZlXu5svtz4PPUydPu8VEvU8gPGVAWzK2WZmq-IdcYClB4mJvNSWUelITaLQFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPmytPJnXmfLUhhFC6nOvv2mGG6Q2sA7vaUJnV9nd7QATi49RO6bQegFneHCervCcySZNBkjtx6kyvLfwtc7VUtBa0Q7AAHEFK7AsgUh3S0ejbmJ-4H-yVca3R4FTGwhPAtozf0AcwxXVGl56or5ZL9Kbi2GncVaniV7AChHJPELyqB7leWmEGPvdpa7Yg65zvvOKvYAGXJ8zL6NsUMncMb8U7P8O4Lz_14sMo8uWHhvmGlYmx6T8b0z0f_D7F2KZzFO2oEsjVvhNk9CRvWGq4bZzJ73MLLAs2To9JvYYPMcN5Hg77LkDOW-Tj8K_htCgk9RgpJqyieql9PEjx0l9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqsKmOEa_WAgVKnA1b-V-YynVgwSrE648useyjQwNQ9XPOcETBI6kfliFuySMa6nG4ObRrNDiuW8UHdRMgXmWKIPPxd-CI9vWrn1cHQRZUYj82ejqtHMx4bG7N2Bf1yGHrjggP68rz6PgD_RQch_WGfkEIavT_-GBv_hJh-KabfSiSoQrGN3Ho7_C7eTuCpccWoLt_mlxNiFt-u_9xveaUDqXGziHAvBm_WD820_tgs_if1Ng_bzZa2Nn_xinAs8TM7dJYrE4JOk4dbkOKlxsQu5ccYuOsZJHtvG1tJd6fhKEFYvfCkgiFj7rjNziB-HtDKKbWhObFwFEn-iWycDbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoUMh0ShBTbuD-tJKs63rph-683kZ0DPncuK5JbC_LLz7mKlbw9f0sXMzwU5lx7_QeGGrFLmJBdPpmv1DR6PLHpIPCCoagu520z6wSk_qPuH48Sal_hpWMnF_T1mvTwBuesS6Aqpa1C3lnAzDkL0sTF94rLn0-tLNdYhezvs3GqWNV1yLFz_jpErKLyJxVZ3-bX74ZzRMg-NArwLVh--rza294UNsyvs9K7__6cJtpxdIR0n9cza36rPhxhdmTGfaQHsFGMEGwJnV7ReS57MEubXFM9ItZh24PpY668DBy5h6Y1ZsL63Q0EbnpmGiFr0XBIr8Mx4b35RlJyKdUS0dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAdS6U7B_9bJKc7j0D3RfAd8QjxhWtabzTBl-GQmVl5vwUMUYbUdoLrKia5InqVQBDpVT6ncp-7vlB_lK5iIbTN9_0aAhQtVS1yJ1G8kvTYhPrlhyKG2Syrkcaw3GrkoVB0L9cJJh-HoXjimovk4dxokJZDp38WDo8pbj8UI931jtUZFpQT5sFp1pxq4Y_-qaEtsG2itML4SCG-nisVIN3F3MfwuhRUdxI3sxw-faJrwySUO5ZkkfzCrwRN5JgPKtO3BJDBOINZ301t4Y3R_k7ZHU8pQSwUWwyY98iq0shUOCq3tfuZrucbXcmLEtHaezn6p55M7OpetmidNutHuFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amy3Bysvq_-FdolQM7ia27a7zcjAEHjQ0c0dtLaJPWQt4UMbyZ3O7cul-nOdcrgTfR8oJc3eFgSAgdCtNc9aoyzz4-4z4YStuEpt5Q6qgkQ-HA-GaKcQf1GrS1dRHoqwQx5U5vp04EpDKFDhKYxprNF1Lo5kfFwrryZiJmN6E5AeyGDxumaMJTW3gig06x5fw5-DI7y38su24uckTT2SWnfo8BmKa8PMuvqENj1a0cyvLISVI1-Aiz11AiRgcs_AGLoMGgW66fzGAbEx1TsZ5BnLIwmHZOCynYcaDvE3YC42jb4cpoF1lbt5_BDp6P0bcuh0P7nTPz46AB6lqSVSNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3JWy-oANqFAQcCUXamMpLeB5F8ev0k6EvMyzZsUIl688pm_k5C28SizReHW_wuCmuzvwkJZqMJJoPDu92cLFbGu2j-qHdwwvb4l0DjhRS2rXbsSdMpuLX05k4ZDY8Bl8GfmLkMwIzESyLkn7Ov2Iwis5ZX5GvSsjH-Cj8rM1GV0WksjQ242tIblXsb_7a06UaMgQG3EWAjucgaQg5xiSgGORecIFh2_6WbOz2BZqJ_U0KRE1nTjID1bcNCEmwvdlmLcqGLQdSF2pmxWwPg7vl4uxDgQX2d9p4m1dA7szCmp4QlOIR0kkaqEHhrXOxJzczoohrWvq_icbyjVWQoWFg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=aLZSgSXkwXfpbIKSciszvyCAzabKz2LO8x5O_zt9PXmmM_LWFXcNjIPFiUA8Ev-cAJOoViu5ZUUSdesAa-QoscZ9VSPQJbv3GfUyrCV3TdbBGwPu46_txAH8ONBUHhf7jg6IPN2HCPxvWLRWaOtG9rNc712D8ms_vyzyeIv0JnUEjzQmRPghNaCPaGIOVMECAbZZ7K7WocNmthSOM9GLazZn3XE5nsulkjihIBqWgTq36nnSSFc8K8H3Gu5cZLeYGqLxFcjOapb-DhQR2s45uipXNJtShT9ZQvI8CiRACmj0JaCoTERDmnLInpXJewIIDt8zHJPxyY3hMzxkWskvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=aLZSgSXkwXfpbIKSciszvyCAzabKz2LO8x5O_zt9PXmmM_LWFXcNjIPFiUA8Ev-cAJOoViu5ZUUSdesAa-QoscZ9VSPQJbv3GfUyrCV3TdbBGwPu46_txAH8ONBUHhf7jg6IPN2HCPxvWLRWaOtG9rNc712D8ms_vyzyeIv0JnUEjzQmRPghNaCPaGIOVMECAbZZ7K7WocNmthSOM9GLazZn3XE5nsulkjihIBqWgTq36nnSSFc8K8H3Gu5cZLeYGqLxFcjOapb-DhQR2s45uipXNJtShT9ZQvI8CiRACmj0JaCoTERDmnLInpXJewIIDt8zHJPxyY3hMzxkWskvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj-n9kbjD3uyAHSWOqOHm_5DSYdmr9rr3WZoW3wCOKWVbeGJvNvHdQYpsk8G9bKWEJ2ce7X-xuKtW2sAWtrBdgPJzPyswC9ozFUhM8PkfijHCl5csKy_71U4UElpRM6Cs_TNEtgNj-8O8FOJSZj2p6NHQJoeKcSnPPOiitmYhFzYxzlcPDopAeZU2RMr07up4Fq2KZQ_4HzkXfFv25IE7aHxIsLnFGkCE7Km7NB1R42YVQosQIhusJMcGzkMN7lPtvTiv7wVqkwhu2U2Pf6iY_18hM_zUu8MqUARvYZeu8PsEhL9X0mDRAdY_LK7UQSnBKQt9qAECVv4_u01raBW1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcc696lsW2MmyJucW6WydWTY_Bf2Ud3zrIE7tgz1ibq7zSUd59uO_FxU9k1NpuCvN8ctSCkpzkwnsq-_NQZ0fSEeV6uvwNW-FqJMBD1Bd34lMc6mRBUnF-P24yWvrDsxAUZKRw0M92K-GkHflTNZGo_SwFOQ7p9oZi3OADlfEbVhjrRMpl2pHUeW27nj13QmjDbQ4l-5-NFs3TdkuqhT0hnWMzh_ZuUunW_ab9kHk75Qwo189xr7KWmuu15EgJ4d2Wt-Lv1dyJdin2odi5Ya8jHATgeQzmry_jYy44_9I6CQh1ylkMesevcdUFzu3EiMVFQeOJke97BeP_j_KSMTNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8AwqIWWn23Ul6_kLj6xCvhz4qpASRYDTBRJVfLmeKlnZRLCv06jHUm9DGe41LVn3m_6jxXZo-RJPVyavcYfheyWYUIZ33HLhPpQ6ryZ81iqY8-XuPJ6Sq343Mrg4BY3K1hYS-ljlHKckFsqmpyCHqXdxKo5L268BHvrhoE-Fp382KxUC50YZ6ii3saELwMOwN-wBb9wvjuwzMPiJOBn3m-vqVn4uXnbx9Pp_QMkpnnoi2BIO_pOtXNSrTQ6Wf9D9ynNGRbzlgSJSEVcexfkw2AUvgI6EebSAWrkKFFvT_Hb3jSV3BTKt6WDUrpGGbhTOXa--z5cmF_zP-SGHkXWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DG7EcJkyx1riOQ3PVMaiK0f5tE9tkFihoWsu9Vr7Xk-5lkKmWpIBJtLRed7n2W5hrUzCObD9roRZINg8Gm0MVv-wCb5135LC9bbCAjMYgqehIos0_JunWEt72jxX_X2yyp_AGso98DnIKsLi0UF2VaKNBzCUqzKT_iRyn2eHs1jUPuA06VSmipWWfav3-MT1SpaWhwvAXC94iaFD9RgxDAWCuZ0kRmGUIHFVgCUvBQWN7oElDJVnTlr4P6fCrelwIsvG5398fNXJbaUd78ZUDZQs8d1JGK_WCcnuTICaEi1y9M5Y8BQkgZI7KsnSKVuo5Hf3KH7IUaXneAS9ydMmag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7foE9oC_wx1_rgbgZlfCxAW9Yqx5oqw0v6YxJUV9PRkWOQlNOOmT1B5BVNZCLjk5Vl8Fc929PmEbQwTsoNywVRUDGJkRwcXZnxWMy8J8mriicsJKsOPdWZVwlJJAi6G71o29Ih0yIKED3x3ov0oyf-xOgbgSgGuNw-mmnYUtUWzUjaL7ajU7s1UomEpTdeXJstTgBLA3UuyiK-M7pafASBST7xQ5s6UtUT-Yq3tV_GoFP79SzhPmXPGi6OQJzueE3B50Bz4teOqMtRoyETtKSWbIx4VeH8eD5MptTwRGfGD4KA8JflQaO7cnR6_xRGAzV1QgbOKqREgoXfy-65Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8UF047vDz2XtHwbJUKOluwN65VUT-vxl0ucXT2dGmVtdvT7gJcste36S9KQ7i0uKF1cd_KIoj54Iti_BLwJrPva6b4UJ6tDLUHUA9fqDi3tsUVvK18i0p_KG5jxGNwICdBncSJEpMC7Nzmu-TPJp9T7bBIeT1Yny2F8gNE9Ot12cAlHAiG_FEEGozlX_CCdSjBgWiBsi8ME8BECTYnIrPGhcN0wu5KNeKIUnA533Yu4ad0jAxjkuAtwVPZ_Hvxq9vgOfEJRY-UElGqa6bdtTVQ-jTxP3ounLVleAnp7KNcbxqvlhxCl07OfjFdpCRy3m06rrrQfQ3u4VVJ_pOv71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3QB2StzOydXJJu08t-CpUhHgYEXsrXV0-PENuwQniKp9U0WAVaCQzQt_G41yTXwdgu2DlCDcn43TmQQTJpaX7p4Ct64ka4kxH4ElxTGjUQhaViLSjwsz9EFyk_jic2i7lXRAE5Z9mgmN0nbUkgHmC0RUTIUxa2lwTp9tgKzNr4wuYCXGHwsLw40oa0X0rw7tF0m1CvyLr8XxaFj9Vwmd7g8GWWssGZh_Uyq5QdZHIoCodo0jtev2Ajedt7drZN9GJUljAEnB82I-TYyzVs_DLaniVUF2jH2n6XspzU8JLiYR7pjo-nv8qV1RTq8em81cScZtv7GuMWWDAriO6LfRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Oe60GFfIVDiFDx7BBqgZOB3buYJrAdUD9HjP8RFAP7ooeMKufVOOPaqP4zhSslllPCvAcdZj7TuK7rzApLEywA5uPAyG0eqp50294TYXoUnI5VLXegwEfex2ZheJrxZziVw_kNa0Emor-ZreJQw2fvQQXsGsJ7YUHo72ul7ze8MEDMdV_73uXB6ZndhKdX0eZ6SRTuyy46cb3TCJDO11YZI4W8NbcQTWAlDwDkipviKeRgthtlD9PFknjzr4vxdE86jZdCSnBnpAlzYHOiuvjnXCbEwZnz0erE8eHGKHP7_Hkvp017eE9VAPCms7raEMlhSAKQhU2oXhaVzS-F4q1ITSvrj8ZoeGzDY5AJbRcGDxKr0L8UhAWDR2EPjhiW4ISefs8T7kaeo4wbUBJkqvdCKmrqT3hgNVy1s_m6mV7RNCIRGBP19xqWEJc5tj1_d2HWhO-r_9O_os38Fy3JfYdpCoZ1rrGXVWyoqhXVU8-X2tQ1S52xxPi2oDBIUMUAzWmBgcuUGnMlDOuiZ92chIketqFbaLwPNq5UYq8Fu2Tqlt4JInRuRcA7e0WTTB610vjABAA8H_BNaauzirdyaWYc4-PT_FavjSojgAtGvJZhBj-FdxXjHETj_EpKsbT3KQdLvHQtMcA1T6cN6uiSNgJZFLmYUFD5KfU51keav8ViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Oe60GFfIVDiFDx7BBqgZOB3buYJrAdUD9HjP8RFAP7ooeMKufVOOPaqP4zhSslllPCvAcdZj7TuK7rzApLEywA5uPAyG0eqp50294TYXoUnI5VLXegwEfex2ZheJrxZziVw_kNa0Emor-ZreJQw2fvQQXsGsJ7YUHo72ul7ze8MEDMdV_73uXB6ZndhKdX0eZ6SRTuyy46cb3TCJDO11YZI4W8NbcQTWAlDwDkipviKeRgthtlD9PFknjzr4vxdE86jZdCSnBnpAlzYHOiuvjnXCbEwZnz0erE8eHGKHP7_Hkvp017eE9VAPCms7raEMlhSAKQhU2oXhaVzS-F4q1ITSvrj8ZoeGzDY5AJbRcGDxKr0L8UhAWDR2EPjhiW4ISefs8T7kaeo4wbUBJkqvdCKmrqT3hgNVy1s_m6mV7RNCIRGBP19xqWEJc5tj1_d2HWhO-r_9O_os38Fy3JfYdpCoZ1rrGXVWyoqhXVU8-X2tQ1S52xxPi2oDBIUMUAzWmBgcuUGnMlDOuiZ92chIketqFbaLwPNq5UYq8Fu2Tqlt4JInRuRcA7e0WTTB610vjABAA8H_BNaauzirdyaWYc4-PT_FavjSojgAtGvJZhBj-FdxXjHETj_EpKsbT3KQdLvHQtMcA1T6cN6uiSNgJZFLmYUFD5KfU51keav8ViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PN76T7__zTPli7Wf_Nq1g8I3OwyTBTU0KsaqE-jpWWSG6Ezax-vBEjNyPXxJoia-GScJ_vIyGzVYNwLvvumQRuzk2p89dZV3jx2tsF2Kp3B4FlolDVuexp51n3rOuHfOCgQMWK4fBhyqkdY7dxPhVRWiywJ6QcVxO_WnqmhjpQmVVbrUW1pUlGDEzKkxOusn4UreFbXhSGYBXh6LFxetH_A2CEM562Vb5N-vtrOu88GidpU8fbnzA7f1eh95rvETl9aHpAhCzYOISJEzqNnhc4pQxmP294PT7sKYTUv5dGOXuqN_xFP_p9FZIrel9w7brUUwxrM55MDEuftyrebdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vegz_1vCjp_wXmaRjZvnSTko2gZmbEdR9erb4_UDbM4cGg0-gPvpTP0ZlCUlXIHbVTyoI9d1kaTiw2Mv4zZshfCRMwzZfQnjg7_RRbk4eo46Krtwj5lLNTiaI8366RZTSv69wr9x3kQEOib84f5269Bs2BKUeUpS1pThA5ThxKNT10JXPqDwELrc11p5iMfjEjxRB8ktDQMVlFVMsOtbTYLJk499x6bueh8rZSk9CK_UeOo6zhHd9gyOh7OXAI71QRciCJwkeinx7L6QimvU7LL9Fb3xDQkbh63ze0BewIgkuQN4n8frDnfRCapKt94wSZoXXllEC_AnUGddm-qKcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJRWVQqadnr21W_YnTr-rV_jlN-K0AuUJGXZSIP6UkRbSsLVf0j9b1Mp_9NA-Mi1RoF41hAZqq-KcerGDKsa5fnPL8qhpuj6-c_GFOA4g2K0yTlYbGbsKhj3T6uiUVLmyng9Lt4YWeSK8q019i2rlniucAb-lTJFHZFhCLpNqAfKquEDOuKA-ioCc5DxKbFrt_kdIrt4s9NAHxnU_vDAGgBna8rBaZU4W0Wr26SJ4X2unPjgv8jsMrnubRN7e5Un04JWRu9nVDYI6Ldko8qdlswyV2-A2XYRclRKytm81c9ai-YItNsdJmobsAElPDnzsgegTSh_KoCnRxNpDcbG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbzwufZnsPID1JO5RK0F1bLIm0qmGGhiygrnmj0l_ubfaQGtiXe-tjapwGoKkHke6O39USx_-6kJnvhndGVSvC3QIsVAQl2iFRmnDufpQgpWSNB-eyNzRMrZkJRA-IW8VtmZHuVP2Y6VVT-9ezDgHqWdVsYcFQ5WUVrKVC4Gjc-nXPuQ1U9KgcQqii7zXylW6aFRWYxsSHWeK_0R8geUr9Rmo4bQIePh1zFq9TQyOkpKyw9_ucVNDlccXdX7aDDLbdk-fAlgFNBs3R5vRlFtvX4JDTgP2GL6cW0Je1zFUdhLmUC-3BK-sch_UxplZldrE1-noGd3Hb-PoBIhRHXhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAmn6GBI5nKuAORVFxfGuOKk-Qs5pvQo2kLAVJjAnJh7Dzi1HKxzuxMGhz6OlQPr6z_0sjGlttGcEYhQkrSpOVnYxTrLd31t8WeX31xF9krpJ0n4R78h5vTNXjipVxSe6ykPEmSScpnG2vw_FwzM5YnJF-dD6ST93XnmvqqgWndPoNFZzSqZSJwmwuXf75EF3SN4p86tGohjxH3r9UKE1OOPIG8TlCRx1pfUcOeFoSAKob38HUgPoOA_rqxZcr0d1xBB6bcXEazJNTTFv2iTM2WrZLmrDzGGxT1p2oqkpwY4cll5Ow_EgaGdwrSuyq7bi9EpOZ_--6fgIcl96JZZhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0VfyH8-uwMxPBwtsPn9FXXtKtHmVhBxo22LZAvvmv2Qu7BJtZOBJrg3_9ZOJ5AhU_vM1qSx124nRG7-POb2CZ3b1I21bLMY_rgqb_QYMO-8avYynMD6D0SWWqeD3dWnyZs0_IF_3UzvzGnB7cFowyo7RhD6SiGmXPa0-OzBgQIXr0MNJFou_MMsg1rFhEz62nCTZuh3jJKI7HrDD8CUp61yIHyHFfOBVjioY-XUEvMTXg2bPSWBKq7VWPd2wlqdh3BqMAWP1X8p2z_cyocQ5uv9uXmQUtxeQ-AjUpv78O6hB0IITFQij6qmFLYw5s2q09BZyxR1l0gmjSHNZm1KpUSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0VfyH8-uwMxPBwtsPn9FXXtKtHmVhBxo22LZAvvmv2Qu7BJtZOBJrg3_9ZOJ5AhU_vM1qSx124nRG7-POb2CZ3b1I21bLMY_rgqb_QYMO-8avYynMD6D0SWWqeD3dWnyZs0_IF_3UzvzGnB7cFowyo7RhD6SiGmXPa0-OzBgQIXr0MNJFou_MMsg1rFhEz62nCTZuh3jJKI7HrDD8CUp61yIHyHFfOBVjioY-XUEvMTXg2bPSWBKq7VWPd2wlqdh3BqMAWP1X8p2z_cyocQ5uv9uXmQUtxeQ-AjUpv78O6hB0IITFQij6qmFLYw5s2q09BZyxR1l0gmjSHNZm1KpUSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyjUxaeaWQjIXBWYMOhf_UTZ1fnpvd6QQFMx5bbBJYuQ9hLddwWQ97dRb6CJvWvYNSyV6PErsSZF4EEqXCefRl54lwJb2HvM_yQrwCQg2KjWJ2xLpGaLv9BiSgSpJm7ewLpQMTPtfaa7U15Vr0hZqpUpJd9rM_HrQbcVpI6OzZWqbRnkkWTsuXpjQbXn2g9mxntvtCC0DQ8C7bk-CIwbquDW25mT8xgZaQDnuxXkQcCM-wcOOY-p54HmDP6K6GsyA0xcxNspbeq02RH-Ff8FZ8aJAYCOolmd4OPm3C6yZS2NmdwpaKeUStAzJgNFisP4f1mAIPy9Nc4Oeg1jNfGBgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeqO1Y_gWaeQbwirqQFOs9JaiCIAmBGNw6fegy_STdgwMFnO3g9VzRG4nUmLlcRruy76GLLnZW8Ia6clLDnHzE5R1mRQdenznbEF82pOSJfDLaJeRmKsQ-MCuzzT3JrosB3lLya5quTl2tBmSxK6JJd1ynFsSNyhETg1EN3KCb0RU5kJt-MoMP-jjalh_wqTg1tT88lICvcTBnydN4alnTFSiYWcMhtVYYnl5vudZO6NR65Xf6jjosGV3rUYO7Uo35-lNU5hk9UuJc46Kbm73Xt7YuFWAGBhti9Gqdoa5oziYB-2h5csQwVulVq082-pRRV4e1pjm_JjKkrSwc50Og.jpg" alt="photo" loading="lazy"/></div>
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
