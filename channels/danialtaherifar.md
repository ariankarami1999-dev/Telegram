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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 07:45:33</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWsNfi9jRQepCX1e5gDV4QqApUloUqiYjFkhcB9BVtqa-JrediIDJA9RUoBE-Hyf3g_G_LdT-j7whZa7jDreMWvdNpWL0q-aryu-5GUzgRiIU95JmTlrAUhfuREInxYeP2n0m8I8sEjWwqFsVF7QliMoajqmsnfkayNOD_EpjoJvRUYgp37nCfaFJRPUePqXdJw7E3FcWag4iguF7mPcYS2s6neOROx2D9cj_GNku8dZVl8GhtQW6Cgjwest8hfEzHiYtuJcy8PiGBADCpNTcd9ocAa0M-R0apmTt3cTN4hO8FmbDL7SFcPIPudtDwr-I3et1Oj5Zhe542VzPe3skw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-vnP5aDAIatPGkeBpC9AMVkOMbhdnxM9doEZUFYaCEI_2WVUdKB2uVD4jQMbRgPzniHCIaHn-DSXtsTpzfacs-nI-D4hPznu1pU94GMCEOY2xl5okFIoLkvelvMogUvBTrzOQZeGmBm-tjBn4COa9svLq2GLIJDUSfmf2e-mq0b4N5R14X7-d1lxpKEyecvpyd0zcnTcHJ6K-qGB7v66UgSu5Qy4r_HSumUy-OXtVG-LWBuG43huJ399CvYuhhYsMFiRLM8nvW6Rc0OrbXeG00lKyx9WCMFmM8Q1o_mPveh1yz68LsU-o81rGyE9ssf91p5Sd7nBK-UWzt7R-VJlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTLej8rlTeIbODJ8Ih3kJ-NLe_L-FfhsDw_lAmAaPCQGNxno83hbsr-MDUMgugx_UrQswXsIIbMLfYpO18HLjptjVTHEIKKCGFiFCvWXLVTjD5UsX-fcsKpvw-F7o5ht_kbyp8vxW4E_S1l95HghVDqBcETZXGPGR4qximp2c2jG05kovmhwWPhNFUiSl5V7dsvI4BHKUW6n3OU1UOs2aVWu8ecYHhgYHcsaQu7h5twksct5RAcOGVrWxylyNX3tRN3dDdXAbC-EPV45yiJKbSXe1MsvN6rVSgw1n6SVVKZNENZeVlByLiClJ2dWR9CnbyElNtnuobUu9jR3BjW-VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qru8mIX0JFJ36ehHLfZco_aixVBxxnhLfCbWVVjJHcFxs8ckQrxJQz7skw5t2NhoNWZ00qlsc-EB7eTx9-I9-4mrUBdVQr2mGCqUq-eXVPq1BO3XvbRiIB67do_dBnvfo93hOnclaKWUIMXoDlu7Q3yuzKKJT8AYnDsvmL04OyTEHMNyeWKpM8_u83J0Tk14N08wpXs45i6inUSkNjWvRkkefiuclag1lOfEzEh72m1Q02Hyob2foKycqZw8LZ9S__uxqzwsqfPFqtq2DC1SMT-fGqhOFLRW_SZ-LZj8WqwGMJjK4bm2Lza5LyFYVqXk_IlDibjn22CoL5OTbdLTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ii8vt9GkND-S5Phqdbl2jvL08ZrgLqxakYyC4p6iIa2ZDGSifEMeSGa23oyt54n9_gwuiZXJVMGpULXYOH3aASzryx1fLKYD-rgaPkDlFUXv-Shd7fa28fHlsAtlgkGdNamGSAFHl1EvW1_cfYhh5VAQAp9LtBckGyO08VX1fN6soonnrkxQ_z7yy7q3bOJbcmePtXtADL1q4bgmafScmIbuigaufh7BLMc45SefmTYAaqb4wJBMjv20jLTqrdmyyRo37a8BVICvfzx1A4B3Q9da_U67sCQNsGc9h5DJCjIBQwZY0jbxvC7qh6x75bjjf6UNx3yjDieWYdaVWY31fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4ppcvphAzHfXAKMSt2nSgAB662LaawBLzNK7d8ETDfuAoCKDyvTJtGLrcZ_3VJVL7NKjT1Ntqk2d_bwq4bF2Mg_w6IsrY9OXsuhPiUukceEOIRQ27NSD3pjC0jSQn0mSyLcD0d7ni9ZlwDu9xePq8nwEPvg3mFURO9Jf4aMVYUZp9jfOPPVMPZQArVhma5g9Wh5UXdRVTCoOilwdEFcdyg3NX7TINJUeOuhmzvpvzO2-RxyEvp-c_ETd8eDriGe8jjEmimoCuhE2nAf6N7Y5TXQYHSfZSLY1P3QLHnkNXzL1hhPTwuWsV717gfDMLsPYgFIMJF1Ww7QY_HIW1td6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8Wt2E-BB6-dgdKWI7gNJJlQGddcvm-EaW4G1XYCLge0zapJHW3XXTFi7Q85quTtXAWnF6iwTN4BFIOYH2IB5RYaRrDHM3tEYmCNwFoqliVZVgqugk1_FTl3jKH8g5vmOfajP7Ma6iDX6Czv_vke71lz67ZLX5d2fl32vhn3ljxdY2nCNiYjWSno3A5oR4-mKej3rrtJAuLONi2GPvJ65o3Z-IR2MzlgAO5fjsheU_8w-FLVrLhTZ4Yi0gH6XiL4eOrQ8r38NW6P6AtllGO5r0iV1kaqL9wdS-rOjSYzcefex0brJ6yLv1vxbOcHGLeqdgq6Y0fOGBGWpl6XhyIFnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1tXdgFI_cgEKXnwJcKKNhqA6RlfUq2vTu221587Au8zFsd2Mei8rRnWmmk9ZPHicereQYgNGgMn4XJapIfe6U8zbHfwJBhWdxtka97vk-uPEgMOPbQz-Oxh4q-QaZkocGT_PtP-cVhhyUje5O2ea-xFS6d7kSTW_gEC4NxTcgXdSBihUrwx5DxmLutgot6plHRPwvyTKtlcjFtVePGFYtVSOOmjWVxSy3RCE6NhD36E45_y0Q0TGYTZPr6IYLxiXFWKFu8RnkGipQAM2VKYWL_YXgOv3kTeG4HyiiP9XIBlcGMyJjKrQqDX5jvgRJQcrjHtgBMGnoF7ecm2zNAtSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZLMgC9TnRWXScrlBO9hQVR6nKM03y11TcJYU1yX4CrWxu4kizq55b-6tEYasMOvYeEo6Pwu87XDIUJDyA94BeKO7v1QvVbOZtr8DVGg5dpO5JJo9C2eJwvwqHKnFX_SrleBK1v3TtfNXUPRZRiTGU5C2PK5CMOjZlKOwraT-TTDsLUcRA7N4S1PlH71BFTl2bzFvERd0Pvb-4tcASWn6Hr_qGdfYpOUn4EodheIpB6BwmbM5uISflp7xctMB4fgmFGFZYYTw6epUXUYNAlYeGqwecD4IuFm8pQ8PVUY-GTcKV4PYsW-bJgKKPmlgmy4m2hwSNmLsj4pm3ufpvVtSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfamvyXS_g_AftX9cNg_cNB1RwTkl9Q3IR-X0RlpBaP2QlblwtUuKPmznpw3En0IwfTwV6la6SEqqxHXqezpxyLxG1VPOBv362WLKEPNjUhYlu9EgIA_k9Wf0bDC40yNvQA4T9XAev-B-VlKWFENbXrP9E0sLBFl3DTGcEMx72dK3QgddcX7kqgj6FcYpjoLT4XULJN8Vx07zFKYQ-oluFALYkoZVClSxeNMjzg1R1AnH2EXTzgVC3sGVa0c3TyN9XfMNUDzFx4WbiVqs_BKcMwU-uP1FRAytCVdAUZXyQn5p-ogBwYH2EdqSZi9iveVpE1SDb8UV0H1sFJKdYb0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8TIenRX7ebmxm8s9GGsiKpRFoRBC5S6KUcXi52Hpzq-LSDZQH4-aVZN885WFMfATErR6OSbyDGKa8rrGfWEg7PrSlEaqYrQ16WQz2skv4P3Tv9c4NxmDCMkGE4FtRar4vp-SjAWJVcM30gHtVoK4XhSWJK8pCJVTsx5AWI6O0xqz4aUByWuQaA6C90im3JByOtSDhBHglH1PeFYGRu7J3Fm0eH9uIKhklRVfe5W0LkoNDUmoXJi0HqkXAQsx5En0w9d1s6rthRljaMuwCSsjE5Dd0452jnUTZDjfSTI7VJ1tBLQbG3dBO8tTmVwFWbADPy_qw6TkwvpDTdaMiQMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxeAsfiDCxk3Nr2e86qgX5l4XuEk5dllXdTXqh7ZsLTZJBhE7xpFeKIp3qsjoWr_nMubpq-I-iKr-4agrqaPLxtz2pPMEZA1Xqxl8ViMugpjnVZLi0VVDNBjH1DJ841OEWKGa3SCjERF-XFeQfK-zZyiCmSnJuaMNs-BnS_5gFFbLy858oJf9_aYo6A8sYyiqy65b7jbmRczqR2KSkQ9xOwwPn6AXN0MbZFSkeYB-IkCftTQLHnuiNKh-HJLVT77vatwKZmkx7EEod7kudt1C_a2ZLPTdT0YEkMnIMgCP8YSmxFLLZOkmzLREiOBUj9UAXDTsC8zvJTWsaqtL2M0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDw-lxz2xq4WJJ2hF7AsaGInk2KQr6PDO2lPogZ3pLxB3eb4kcHEvGAFRy8g5g3Lg8kdcfKra8afUTr_nOkxRz1m5jAt2kXIFWi4R4ti1mG_UcUd-txa8gc6TOYxX7vbUqMJVbnot6R4o24g-NAeMeSHlwgKgHbHkmCiAjaLNHAEuTmUEu2LUl2DFbnpLGOt0241HvMGumewZr0U_r4S6YW5wGKOprj7OpP8PnO-k_Rj3YYAwTV3rK5cpdsQpL1HLGZa0ZEmui3MB8aoAPLgK1qd1WPdsYQh-tPjeeUQocIqmlGnPO--f1RMA2mrjouxCXVoNHAzGTU1HmSaQujuTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOCZoxT-C8OngVfRRSBrX8VyTg9TqCW3qileNRwQv76Y_P5O_E00NseEvLlQC9_6MrgGX11G8uYh0uUjVXfm90vqxLcVIxat1tiZ19bIKPD9QHvscLccRF85mH4KwzZjhVWcnhXB-Db5JfjKcQx-vAIlILQZdcCNSGox4OZ5wBgs7svLj0mRxhp2ENWRZ90QOSCbXnjoMqeCWhE5OrsjwHgJMYk9oNUYWCvKpV8FcuNoP7pP6LE2hQCw9wVCNoyZS_myb1D5n94kSFDHag09C3zRSifGyZb3QtV2wPIuLbAL4T1V8SBDYxJ4NJ3XsiZbooPbtZRJPqYfhyWrmrFZuw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=e2xh8i7R-O_8kvfdkB2GHo6QoveFfU3AdQoEXYVNCzG3eva5madALBj8n_6W04ZRtVxby5Va7k5YDQBRRFApSxUTO-xF5e37W8hf9fSqTDpfbkuD6kpm4aqj-ueV8SHr2MugvEpBdtD-VEn14jP1Tq7RQo6BiqllbCQtsvVhxD2eyYmUxxf0u7-mvFK8mfs8Lrp2_QwrmB5YTXzRer2pQ_szkDOUlCk-H4VkZJG7vdxAqxHn0irHSraTajgxOu4h4oSWOW7KAn8Yd73SkCW8urpXiAUO3rVTQyUYEO8RqNXKVeBFAGZEGUZfHuM76KZi_h-8koq9LmaSj6tDz9QA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=e2xh8i7R-O_8kvfdkB2GHo6QoveFfU3AdQoEXYVNCzG3eva5madALBj8n_6W04ZRtVxby5Va7k5YDQBRRFApSxUTO-xF5e37W8hf9fSqTDpfbkuD6kpm4aqj-ueV8SHr2MugvEpBdtD-VEn14jP1Tq7RQo6BiqllbCQtsvVhxD2eyYmUxxf0u7-mvFK8mfs8Lrp2_QwrmB5YTXzRer2pQ_szkDOUlCk-H4VkZJG7vdxAqxHn0irHSraTajgxOu4h4oSWOW7KAn8Yd73SkCW8urpXiAUO3rVTQyUYEO8RqNXKVeBFAGZEGUZfHuM76KZi_h-8koq9LmaSj6tDz9QA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_I0Iu3rCItULI66NkqZj3fnczXsK5pGm2ChTrNHLjV_i_WSbgSF-KTqRdSPqhJcOmbB7_5X3O4-slb0s_1krtqAWdo6NdBZ6aop1KIcT1hRQnVfNBP32ErbyQu9rztFHut5tQl54RgG9Z2bxJ9-zq7AKSwnq62YKVO9UeggJ3Qk3IxsWQhByjVsvUxgYxo9YUYb28LpftALLgzPd02fOF7MjiRG9uwlgCPHfVZvqgzXDYAMxFQB3x1zzPRau7piGm6paYsQn5jEw12UMq84u9bmEMnuB5ocvtuHza1zvjHo6eEL8gKdNJYMxcxxh--lE07_y-MDvByokuADeSiVoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBE8fLNjOvaTPmWmI_3yxTDd2rELSCIudXZoZXawyfN_ouGtWO59c0_uauYgaYDhea9oOMG6AE7URHStIuMA3v1EHdYgeA3_cD7PyUtMHWE0Xb31QMHSGLD64g5LZxR-xWsVmX6EuvZZGTCdxCZmu95EOnu4a5o2wJriYzVFA_C9TM1t6XZ3h_JB2ScZBkQM5APpG5CP9q7O44R5j01ChZKuii2r-vpxCV8C0ZMMYipjJ8_EYg2UR2HLglk84NDgP1NlEykzmeahAbqqzn1NXxZjPCXxJn09p-zTKRr5QfzhcrMzQSTYhDdUhcdKnsqGysoLnYuYjkQTDzW8dz1HxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uR9v09gEZUQdDu2WnGYP5HbG3uyFAbvZlwYlKupIlnyuXccWTc0g3m8TjXRXyZXUyshcl38OJLJvg3HIwonNQ8o8KMIw7tWxgf9b6vVhdTBboY43aGQ0XnGKi6274JcsCUaT5HSHmocp4K-4Vm1CjnZXLIRtWH5tp6aF-6zm6Wxkp70rH4Q8FxtwTb8Q3xbZNUViK0YC6bAvTc4jPEz01lj8-ia94lAXu7lZMZZR8KPQTsdM2khbanJdjCkaQHrqkhN37PpT5pUjEXIgNEr1qL9AUIti3S3VOdip1OdkLkaa2zqC9j2TyIVq4SAas17r8EIIuOBkJuZ56ZThFg70Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BizFkVEe1_V-QThTH1Xy3Aa-hf7p4sXXEZFpGJvET9En3qFFJ3ZQjTSPQFdSAgVxuVRAky1XwnIT1IW8Daikcuo4jb6mOSEbenXnpjW8lXQ3-mXpuVBOd22cT1hiskO0YloJu_IUBX6kr_Mj71VAsxWWrAa3bSWPQ5R3oq8dlCveM5MzVjunZFGD9b9n7s9H3-lrNcdJE1dFArzyMKL4jahKPEfZPDfLVDnx1_DREvO8FBBFDQv5b_XAzjUgOEp-qWtuSJi6NIMae_US8r0JuJg_FEeZ1znXfGL4DA4Wg3qTIi3sQ-LFrF0M_Wl3hrk0m5mYIrUcnqV6JRaSJ3P3dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGt5SUzDTFtzgtUh6hRq3vSd6uDwfSY_FM6hCQQn2Bw72tYEF2m5eid_0PA9BcUyCzINkEjXcW39b0In8s0R24MR58l75qc1n0fGeq3oCwWjeOnbPpEH1UsdXl9MWsYIbvNwLNfM3rtw5eg3af8OuQXnJyp2thl2mCw5QcizgpQsDd_2fREG7AnBVGZneVGK-1l7ROV9HcXkVQY-vSxxBwhVmEUjZe8IEoSWiqwGXx9avoUyFwONP6BhpZ5wIqgntXqAnhe2dma1WQ1601u4vBrC4pcbJtFWFqfYHoF6UZRqHWS62aHWjLtqISa7VWBAqBlv2UUlc8CS7ps56La4dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4OZsmaxNLCvD19-s_mpg9i5n2JKe9g0L0-25ZbtzsFWWjXdCt1XF61l2fZQb83QZrmU5xpoOq-TUbwVoD8rTzHsLkKmVmY0d7BbKirdu0_-TcLwX3O1Nz44fVEq-v3G6MPgawcDXaVT9y90TVRsZtRBpFGfWMUBOtBPJ6b8-rGGP9czcKSh7R89wQ6VsWLvP-_BzeC4QWwjHgNC5nwBhwEtkn-yiVD0en-837Uyb9P3PITJmb424cMltRNztowemvSUZ1xcYoyryVX8y5r2zo-9TF8Aa_qz1cRlq3yEZtGWM7FbQsiS_RNmwEZzeabVBr5Apy52HsbKUJQ5FyiD2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sxbtvd12eys7n3h2tWUQWQtw2j9cjXQp4XC-hmYRR6nTdN8V8ls7XSwqcDknr9veR3emskQydcl8OxxE-3YsFj_l0kE9GAolEm5U6qQgCssrw2xLdaE5MEkjGKNcmvypQoHt4zsuXk6hkqMrKhqj-lMblxjD7Du4OYpSc0aHJ5fqmlnZcvEfwGzU7Qbn96aEsZH9sM7vlDdyKAGFyBUKXGUGS_AHcWUN8n0tvuh9cENJgZ7xWZmQeoB3r0oQonPg2z0BC8EbGFKSAgObBeHc1HU-ZI79Amvt1H9AYRCwXFnlwL_HOQcosqsU6R7QPQ5aEX59Ez_6ktlmUuQgNLEdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRt12PBInDeoB-V1-UaSdwy8Fr0lp6t45lgt5cRRNfvVaIaTo9hVObMuOgLhY3YrnYqU0AjZqDVAHhEtiueHp0OxAOoTNUHxQf93D1DDCrdreURC5bftWKvMc8CLXPecNuCNltoDgbeO6G0fvUuAaKV7eu0UiJI0FX7IrbBlsYCMsG2J7QCpS7BElUS7quFFMUNH737qDIMGtQ177QA4nV4IViVmVG200nki8dXffgM5Zbp36AV_Cpvieb8QVnex4EYBff8sNDOrNewJgO3kHaA8i9_mYLiSVoTUydHCo_3Fqh61xZirTVE0YANRgEUTGvgwli0ivSQCj-SeC4lfBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxg_5se0TqpkhL88DWSob1qWJp8Hyqutey7OFJqAHNajDIwTTdt9HJF-B0W3cpaPnAxNR_8owYTVDHFIX53nsU_coDz55-adLWiXKajvLcyoMiQWRaAQev8p3TXNipuIPwb-0CwmJTYMlPcOxJuGLL092kXOjJX4xwl6N9Q_zswXGuP04lkXGYnBXXU-TXO4_1Y-8m_UtVtEB0eOTTiAqKyj8E60B6haNS2p4QR7Q_pqf_L-SLutn4W0rA1MZ60LRlLeWddtugJa6XjyZnbnWZy-bo1AFFQiSG33rfAYiSkv4G78yaH2xOdIBEFCbkl3Dw8H6REqRUtUmAIzk01Zfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHjN7fdr5oV_QtmNcLU9zfvwujHlp7JTAoBYC4D57z-Q_YM5Yy3lQYUqMcyodkZeYEKKWNzEXaM1ZjVbsdz88K7ymhUed69AhvB3eBIo4WiAO758CDMmF4ArbleWCk5oIunp0_AVTKiMe6HGSLVjs-e6BvrvBjSIjx_oz44qbtQhaFRUYofkWWxqu5hUJMWCxDg4FtAX_ykErET_KH9tYZrWVeyPeW0Nki5zaHpAXWVA4fyjeSG1REhiHYmGOdGW0RsQyFpNFsQbRMgEyYrj5G8G2lH1fwmmfKPxoI19hEVi42ap1rdVu7jiyLifIwNiRwyxCuoPBNTtkzy39MQ7EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvaSToC1RnrTns622xa_GQ4DQOCoB8fNSeJuiXpU-6jf-I3yBVkq55BWVyyPwFHRjeeca3bQGaIR25zGU2jAGohf6s5oVQjjPI82mwZ3axb3H-lfa4FGzsHfXh_aviiAQ9rieHml5RUjI3WcrRTdZ2gG3grB2UOuw_RSaxiW8W9PblyjAYyGyLjVKyJ-sIY0VhQj34HILPxS1C9V5mdtH5ohElbhiEuN7TYnwicK_VlC3MvlJpMYiusU7egmjv4J8GJOzj-AT5golsef4SMkv6DOTR3yBqURpkrGmrTqCqyN0LW57BDlDBziMVMtzWzBIk36xDoaC06y0M-IbW5C6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlAQUbV4NEdFnG4y5JM29ckLt0Gx2bZn698X0wvSDEygq1gj_MH2P600c0KWk47z432mE0aItuygHKOr21a-MYKR2SASy4Az8bAlaNqbXz2mZqLOQVg1M0AS6gmn6tTwuO62fRrLKYe_yv4n_UhIjNNqQS0JxnEfTsDBJ58ZA6tzy9sujpHPVk9BkjdEWLl0bjLurN31rzjPjrOpvz9IEY79yiKASMtoMSxwvO_LQyy4NHP77G5XLwqtLMBDW1TRJiOuND160peH_J0FYrOHDVd0rtwUSORzJoCinn1fVYI-EqQ_wmJMkty357pH5_3MxEyjCebVRnFyP1pCOUAP6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmxGbwiDla6D-dxHUaV4FuSmJaxySJBwZXa3SVRAU4kcdrLhFlE-1qUVHkGGZhbWA7Fkcz0cPBhFzmC34-OsTKnEVHfxjaxFt37RLE6lRnB8zZLLE9rqB8rcKOtVe41CxsG47AMCwU-nosnOZ5wI_924zprWP6HIym623JeRX6psZl9YSnfmYhgvxVQJW_M5l_rhBmGY6wCfB06-lDnf0GdgSAHvKgjNKaj76Va16DqRO_3gdls_djqWNWIAsdtCKlWxBmXihG52v25sOvQ3LVccj_ulbYZyiBVeeEII4KfYb93YGtgp3OMEQyXdq6_t4DYwv1fDCvIDfXjzptC9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXdA998mtGAO6TSV78TmfIOPWJzGb__LCGVrZsnzIk0Bh6Ab83y82nfGJ5PSJV_GvEAFatqO0xvv7CvFdYfNA4rKwCmey5eqTAmvnLJYt0YhsMd13SeWraWQyg44So0iH7h9BIL5pCYWEOGdcfoeOB_TJPbPKLNEWJ8_875tzJi5P3KqI_mxe8KwRiAdlQ8RseZZ-qGRi5U1Vd_jDH2BpTSn0M7_7kPZ6ttWO-Du0H5SiCA0iXsT7BvgxqdQbhf143N-O3eraqf4OtbeYV46VXQquxWghFVe_5DoTvxZFwATE24NTLYBmrEOklvDou_ngnjQyGgKfK0v6wTHnibFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3e3hu-wt58aEqr1ww5lhnYp6u8RhMn3qbELb2gklRbcp1JF3zFpN8EpxzvaHcHf-YAAeqDkXVQ7ZDhOOSvR-RYr_vLLlyiZPNo5lwMWZl-lK-Pn-aRHf7J-4YaOpTZ2JaOOKicTLbGhRpJKD-ziYnSgj_x91zU-dkEwHqPMsuntugDz6c4c-dhX9RoBjIwGg4vi9lBPw8RRK3z1YJzL8Csf6RpKy8GfTQsg0sEe_Su5mIzBGmDbBxZS_qLGgUMdqb9kRT4PFhTTbWqwnGLcZGwt4nOYL4RRG560R5c2kiztEiCUrCGGnQqg_kYL9798jOkzQhsxXsM2IE8i9oIxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsOtpgm3vR4CwXR_N6kBKXvEuaz4sqXxmMWbsvV0VWeIhhQIDWEwFrh4l-g9cDP6QmZSE-OsqrFl_MAKGigALpsiUFdv5BmQtXJxLBkR7Yvcc7cgMKMk1F256anr_aRiK22uA3hXrPkEJkT7Sa1JAUa_4npaR_-RF2FL4_gy8umcxr5ZA7LJHTC7w6iptQn90kXi9C2EKX3UkOL6-ya4OUtxFakmZ8pZ7nDESd5uzZ259rU0LBn0vpi4GqQB_JumPNbbOH-87IaklEb1fbnFPziPOFaTKv_XxGbFw2aIi5w8-v1RLDtEjFxT5EFhNs6TBDa6q_VXAMe5aWFtEE6pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDm_jqJxWS1qTzbsaSLWDDXLNqrydFO_ONdOCCaaFt1p9T6o3pFecJ8iWo8c5E2jkVR75x_vwt3SFZorSa0mPxOPnHpA1vV5REAGIBCxDIdJO2dg3V00CywsVN5V-zn3UspObG0fraFyE5aRNIceE7MazhpL-3ZpQ6JyTK_dfvItY0pFSTSx98TW8sC2PULTG_E1nDWWKm_hn_GaEX_H-mpwHEbpRwCEdlyuoi76TtJhpiHqi06SYo1d3xEMfNKL8mXNPyUrvNz27YoPU-g4H49hUgqfucOVGWvWIJtUW62pbUK5-HYtytPRz_oDL-_hzARd6G5BuZZm5bYrQDqlmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SELnqQh7wXe49b30Uo9f-f0XPoqWM9fFNlUxsa4N6ank8ugDMzbX4Z17hz1qWKclEVOJsPsfJ6EveHF-yK2xmFdYgyw1j4Jv2wGuGAJ4ryYxcAje6H5zs80Bq8jr7nGwh1FbTlGhnvYth-NmMUG6AyjPe4mFddlY7y1IyRE_qyaTjstimyI3AbBfcTyykE3iMUWcQcXlYcB13GNva0TBN3_PLDfkD6Bdb4_DSD2zLgf6N549x3m4m6S0JzZRb46OGaseGfyCidWAX6tDy6ehnw56GNpwiuoddwPGOqHN4wX34zjemmEjA64OKwklLUCtnKROQpwTAgXxdUa1ihx6tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmgWPC4jexGdJeOu1jAYu78gKDxrykXnw7eBnIi1o7CEjYP7rUmP48yjML9SvBoIg8Dhzcdo5O8-UaWeZYht5VPNJNwJQGwd9SihBgdo970RwPOidoYEp_QHYCxQ26MNbEr2dlBCFc56brWqNREf6FuCW-ZCw66suH1w0M2kIldRg65uRieefsrNzM_Ot-K3c72DT5Z9RHgi8Ycch3mhER1dIKU3rJeUZDqTs4z6HGP6060OIxKCzbXtMoLyNJOmLAUsd8_ij875Fl1S8DBP-Vs-P6561ovwqqkbjl0rTGArIZelKSIRNpEK3kY0nPLNOB8O-aJ1iLwdl6t64guwuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4cMjKC9kk3IvaDODo1rAy7HoyJi29nAdeLu0cv4aOfE6agqik4LQtDwgjfuRM3fdGd7ED4JnAmQSf5DkdfdWSKh8l-r7aXdEyUOZtIWPmUMHJL6dOesac-6wBeKowugG3erFxGoABqdVwYHVmhDXJecogTGFMjl8uzRbDq1APshYdqIBOr5l8935accWv_7CwH2eyqcctAuHaimD7z0sPM0HHVzsMdPgFN5jSJwx8ed-KfvuSZr2Motxerz5XEeTsSjuqaFzqlmuOWUEP62znIr0iZiahqVplMqxeY_e2yygcdsKE3R2jHHCud-POLx9ih_otfPcogdLU_N0w862Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwT0xJUlLuSq8DPZuKdl9QIQJ8_QDmrif6kCmJiWtdfYSaVqGVV8jA-uHk6a6SQjuION9BeJeE8Khy6tAd3XAzwSLoSH8VceCWOLaa-GMU4AlOBR2S8-_ffF5fV8yZCy1vftmObLp1qQ2m79NceKc-2QEmbtKjx2vnAQNyL_0WhfVsDoPW-SJiWpv9vmW6gGbFNDI8oY2EB9YWc41CMqxURiwloJRcW24CKApNrvkItSY5ZVfVoVS3aoUMW7KAdq8BoLdvbjStS-SvnoRcnB1RyKeWsG1CHj7VSLP4ZJSFWn0VqUW_1TzoYuMMgDJv6USBwr2tFolCTEw92-sgZviQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVP7Vb-d_06O5m9V0wkwYc35O3uz39TINT2cQXJ4Giu9UjDu9bX6Or72X-LZhENiv14eHyegeKCt2V1H51yVJSZRRuQuf1U6nptgaxFfFmznE8zQuL3FSRKotmOfIvD8x-6zbeMHh1-D8JQFMvZb16lF5_n2-5keIfG8wi4yOUZH6lGy7ASsSnyIiDGvnViJFzLnS16dpR_31i_tfbWx2CHpLdn9ov8wSvTfJsTzGuC9CkDbbrU7YJAHlzfBMa8IQAvgtLu4jFoNfDRcLHOzxttRfZ8UQqwm2YJ6Qk8nFbv6aW1xn903GYHzxe0RaHAvAy6RGat4s-HnSLrSKy5itw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvxh9pxKJL-M6lotvd6bjxDsxdEaAhOYOqTy5Ont2pcRvtSjp7t1U_bXlv7zUqNwl9yf1_kFTjdsRuDAdglFe_6wgaPZid9uKDWuoBIJ_WaLD7nCoozMDknWF84079SmtxcBUl8yi_mtPmomI-VgHIG_baNemQcui04L-wbg9OyLyArI1QEr1tPWE6kH-mqEdgL3Vd2U5qLvzRLhKj5lTukC53cEz45JsztamScZ_2M3Ytm0y4Me5eLiCXlPGOMsS6MiETZvDqG4H-dZh8cn5DVfA-0c1qYNIla5kl3uFwEGWtR4yIt4LZ2yywo7rRANCINY7sLmJu2MUe77UZ6bsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRdXCoN1B43d1sUDbdC7zoykhZqvvFNr-HtDfMFgSqwMvYOxPg6SQSBd3w6luCb_NaVsyEYVpbVzSqjF_xjwpTpPJI8OCXBIyGjcrVGrXYX4fBj2KZ__TITX_Hr5LkRCkn1JmMcFWHnr8jgRolppsV645n2CRD_oxWqTkb31mG3yZdIK5fq5QahjmGpyNUnGoXckwk8ygk2yTaJUs3VrjKANjMRkE8OZ5Jdv-cjuavL_oNz2EZ5-SMjvWBkXophzpqK4wpZj_J5B_bt6pwZbv0sey2AtA5fyVwP3AtpeLeRhBNDvSDAYISywAQ5jPEBNhzXnD-Q8yPrJOTf2nao_XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acQfIiZct1PTfxEYReQ7Uye5xM393tGD--WR6ws_4NvsObI4OnOgkRupJa9-IJdRuDZpP3jZ3GqxonaTis8gijrfH6CNLZIJTFkzxAtgD1MZWIN6Lm7Uiq4z2yQyfgvl13p4bNtisqdFSFTQISStMIKcSBlcZ07OEVMT9AS6sgx6uwBuqnKz1JAx8SE9tV_liXX33PMBOKnO8GMOxZAGRUXkHm8jKfWCLasX1ZIQqSqr9wAkJ1rc5wq75690drkJpmVy38AY1s-52PimGG4nrECeM482oKu1rrQI8u55hngDkhAGzEUA_gNSZjXoMh69kA7aP8SF3GwvWhRGWyEk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTmFKmJ778afOZKJFz3WyoIZsiJeJVv7kEctf_9QyrXXstDat8LV9FG209BPSe6YR9RRHUR1B2Q1Y9nKRo09JOSmPlFvmETe-0bgSNLDnd9_5EgqOuSEsejC1lvYSjy6r8DftMG1ZDPnck3sMuFRPEpt0LHLxgu-FRWw_weEQadO25CIbZIZRHFxoP7FJnlOBGxK-X37jsXViqBwD16QbPQGoImasi43yXv_tuD8WXjvH2-fp0B3HpjZ9BrTVMKE6m6C1jTL4p5SXJBRdpT0P5BSIYOFUjCBLYWkAfdqLDGPcEUEMqkqdelaqLDEE5t_RkgG9BEjyq8lqC5E-ZPTzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6z_-0jbu9-ZfDw1FMdAUk3pJn0kAfvx_Df-P6XCjoIQczzgrY-qQQPpSs9YZEJJpHWEcp4o5oNPh478dzPSTAwULff7tvwBOaR4l4n8e_cQ4nZrAjROJqAnwr17ACzv0naBB1e90vlHiH8REhDEgRILizlA0o-h5ieqykyhCzLcVLtOu3mJkffSx6TezUS5M6r7dLUQXFQi9ybBaLqJTREXQmPj39zb9WU2_TdXSknWYAo-_RyH-YsQdsi7ulA7YrltCNUMJY9WxMzpLHIXopBb3PiD8z9wMkvYjLRjjrW8JK63rOvAsilU5ndQUm4VArVth4ryPKD-BWRobFtnDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2DGPe4YqwED7k_BOazKQ0-AnjQFhA3o3CU0xvZY6cr6JziqnE8MbE0nUSkS0-Vz1gKFuMoNc9ugc_45iRxfrPCpwQczP3T4W2r_fLeKXz3I-n51Cf-v0Fza1_kcdoUL8T4UWiBvYzkiE7lmB4ns1PTLy8fXrnL5ncYY6ffEhOFBV6fqFAR-r2hogEnL92RDVlRKbTCpl1jPV2bcuW-jdNPIpEL8RJ6qlUsHyAOkBsHwVgm1qbgGTi-XAFP81unfAvKzkddJbj6AQCEqImG8psT39AEQF9AYZcbtd8j7ZF0yfi7vVR3LlOHrT7_OsmSQzjMk0eoTlUWYW-Z9GiWPcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJlIcuGbuMKW1CQuZtfZ3aC18P37NWmt5LfUf4GR2lr-Wm_Jv5euifHfS5HTjeGi4TRTVFkAsTB3tR6v25BmxiMw-mPB1nSOceOPezbROIO9D6J6wxKba1wFZm8I825jUJuy8rqScPNkTL0H2M7qNMjEK7y_3ihxxKQqgA9ecDBEM4PbCg8sBjSTa_T8SjSJ_j6QX-khchTlGHi0JjIxTHZnflLzFenErPukbRqlaHTLhNq9pTM7wKSedy_zvZSy3BcUTZ7lPvQ4C-LCED76fgKdLOuy0kpoRgM9FX7qNvZ0ZjKV4D4ElIHuvRWbSbBAGwtUAV2FX97tI1u4oggZ6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSyBTOEcOVBabjnguDD5-7HpVfAkGgWpeOC0ts2BZFwf834iNpwreKqfAyovUnuNvByjPo4TKucy8ZShFIWycdVClBGsrLHWAqHvSlsGDrA1lOo8dUSvyLJwN0H2Hy37D-L2tZYoz4Q0_b67pESXOPLaHaCTiobiU8kQV2n00PgqFVNh1dNtfjdD62P6rO0ODC3eb0hk2axriSBm_Viqtl5Y7zIHNHbP4p-uztZl7-Bgg_z3-yiSE19hb0-ynJ3ortY68F7BRsAZgko6evbzWKRROOfeG5chY80CCG0uNzRZ55Hnw1hkDkErQy4NK_P-XEWaumRi8T7y8Fi_9i6W9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_sciEhq5zQ9qlnntNUjnu9_JMNpNqo1-SpAyDkn8hKr-b-3cmvSmvKQ9-fX-_ff_C5Z8xfmAfZbHddfRq5l6wpEV1bC4uCsRkbZE6g6WsHqBL7HOU-2l72aJtzjL0TOQcHpzlLYYVYqnZuuliU10-0Nn6TctlAMddmC0e67VtIYlXPY-mpZmw9lhojRzPUV5r8KoIUwlaVaI9LeZQwcsJyw-DevY1z5SwgU_CwAHodISO_Vn1GMgzAfDJ6T8ZhAYclRfuiAUM8_gzJn-GXGwgZCOtepXb4Xk0C7iUzYWVWp9v7aO9zzcVqDhlS8w86HeiUUUi3KFZVc8gWGFRTufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKlmXmUWtm2nwr4dpPmY2XCn9oCPZW7iJwzkU8U4F2XwOFK0iffAGBVuOKVZTrB0ygRIvuAY70M8QF5ODfifT4UDDL683aGwNGbaotHy__FDlxMz9ZFjICAYE_AGLSh7sVmnsPoMxeAmE2vaT2Frfpuwbrhw_kaGpPdK2jqg3Nbz6GB8JvwPapYxy0u-cz9irj_5B3yIyqC6Cf6KYX5wVikHkJILCqYo3-Z8KbO9PhOgvZ0NnxWXdI6oCpy-hDZO5SBzjjbLwQo_sAd3Vj_CBq3JgNneZDwT9nJMsNcAyRlH7lzUF-oCRB4J8Yf64C9j17bydQDHUxo5xxQBZtCanQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkmkKMqQvTFZ5swirLoVcFFR7fDIsAiHtCUlbtrIrWxr1oB_GDbLNwS_whuL1db8HpcVN2o34Tq-IhAKeXr0_0iEEzDl88ocoLFHx6G56Grlt3LO8X3pN9coE8QWY_RGtCzHuxI4LU7eYeYSwJtCSO4hVSDtk1LvkU9ZFIvC9mY2pMtbr_PtqmXbl3-qbH61JiTPpckWEkpuCea4eWXlfRQJyyByaoE8ve1usJUHDo_6LIqKyno-B1Eawfkyj3oDHdGEFL-Ya50HfU0tR7Cu49bECyM_FtH-puuAafjbe-ewwwIru9WCkaklIHMJ9BqyDI9w5Ue8G-8qxilChpdu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfNfSCE6awsG21MSUxosh8jOBKOuUKuvG9oMo-6EdP2DMMDNN190lg5HPFp06KYqqvd2qLpR3gccC92nMhelvGWkl7nqnvbDYvw00s-54j23XkG2ihoJCadYUxHaYt35cXIKh_GWJ1q2vtpdjfdZmrRAAfW1Vcgs2k0lDgB57jm9gY2wJFDqM843mxV8AWHy8iFEGZEtnSeBvsnyIFa2yZLQ1F3eUBn2ReJtxnBwfIXb6zgZQReEHMhAv9fRTkgNmDTv3egIqPwuV7oe-iZV3_XAIdx-_caylPJIALlzgsivPxqSTkQfGmKnj6_iatnTHWKO7okJy8tHqB-R7uRtUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAprDdFbBG2wINOnDIor6-_kkSJ_FqW8n2p4jAg_b7ZHio9X_TsKTiKysxJs5ZwGx97cSlDtuneR_OhcJoDnp9yx-odJY06CNHu2xr79vXPWXgPqJzb1Mffz08ZltDkROiDr8hEtANiDqA7mISfD1qb9S8lknPht_IXOotCVHnVta9YMTWL5qBJycqsWsUAE6P2UB8sSXecI8p2nseIQf7ba2IbUmf2k9HbYLFmCYRV8gWOW3VcjF-uDkS2EsHPczgAZCsKbw7PxBgANohR2eb5QSfOwtGtn04Zp1SX0oCqR_E5v6f14522pPjFEmF6_95JyM85YmHblcoI8YJ5KlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzTXd9x45QObr0IEVE5yJrP-KR8ZRNj0KRrx7z8pqM7WNuFzMS_CP_KydLeP1dNRyo1ZKXSg75elFcNgBQ48_YO1XIDRddd-jJMVMhtcrSccceJ1TwUCHXGF1wJuXcol0x91AiZ-WITy8SAq02vLPyGXPOAMFRlGEwz0rQUa-2y1oplK4xeFGvrCuURaT2fkxxtVA2NE9Srxh3s8s-cfqMpVRAzSoWZOrFYFR7aqRVX_40-cltLddVgzW-mvhzgfOI8xGApSZPPyO2zySud2PxGUo8-XqZL7JbqXW7ko0jNwmgb2_4nn4jxOMUcy6cmuk-QJgBfBEqu3AMECwBpuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYamP51udV1gOxi-dScPzuJOil0SETCEkydrLiGJCAOgKehIKdocgqaE1x7xn52WD3xftRvRLxEpH5eVjReBFkwEuBEh1XhPKm_wWSDUXPdTP4XY9j9hMmuz_wYd12VvRvlWEW8UMVi050ybCT2LEmm6t13gvGKntcFigvivTV5HtJlZ1ZLkGA2ZHBwgH0Fi0G1j4dEenRHgGXbsoMioSOWTCmc9VQupF_lNkEdr6_2X7q-t220SNitkzNFlXfVBrYw3oP_7nct_vSi7n8G7pDuCa5ajcREHlWv5uSlXmIONlRybebNYHpB7LEuElyddo8vy5WY_TUMDPiPYwQv47Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWUoVNzUlwQci_zLKlPaW7llLj7rXBnaeMEgsIi7jdrO5gyu10vreA6547kOiVWOFe3AJnDcdob7aodnF0qukOGVL83svZ3jD4sJYTe47y4S5aj2AdJUT-UkqXroQRPP5UNMB18WgwBzbO9ZNX8nLnJAVv4nNRGssToJ9zcONz1AJQyZNigWWxaWkZq38w-L5ArJZVbayGt9ufecHCKEIWtJv8FDLMZCdl8p92zGSTbPkK0kNKXPhLbrqmdw5dG_fhcl4CGxl4RYww_ZS0Vtj3Q3gBFLHq1fDjfQevrTIk1n6N4hUitcUt3qCw0q_tAoi45lnwIc3peRBtMMXHM5nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2b_mtEsCiIgWLK4Xj1RLv1el8xQDsfMtVR0kWYoPv_7blyquk9iYKwRaxaZ70L1mgEm3sa5fvG3SHH1PyVGg5ylS61DO8vxbyhDptgVXWQO4b4q-7nf6nz_C5rsEwV1cQ-ccGWuoADvw0rkggKmUQtFrVwT7pKajb9R_siyUl4H0mg7oT4mbbOLSWymwMb_PRhrjJcoahX_eyZ5KFj41LeYw9gI9jkANBLQv2xbQvkOSZCHiIPXNXTg7Kcm8kV69uQ70tsCJyo9VxJI6Z1zDvVG9YedAudDciTk1q3HfvFNVNrVqLRmTerGEwF2e2RtubkcmFQ4KemrD8nUY7tPug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJiRiW6oK_PcQCMOQvEwyg9EJeJOsIeBoxcFulzHDk0ZRVZ2VJCxPe33IzxAE3CEFZDRyL-FYxLdetQYq24aUZyy0fosa9laz27SXY_fDnKXMsthFy08IkyWrdRdsjnHvCrjFsEHEgpih5sMHPlnHM_Mh38MaeLw8CR9nbwTwgU4LDfSt8XXI-iBp2tSSgdO8vEbG3zU5UEWOWXntMqKADXIUcgKPDCXqgnMXjWAR-ZcWCiKbe3B8Y9ocBnjZDWxbc78aBqWZMCZaAByMotydqF7w09hCFPTcu_Grw9USYPYfKKBctgWONvDFI0-YdnSnPjy1e02jZaKscpUwSXw0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5PuwI36fAp-Tdz4uqqWLuL3CGEuaMXXhHtwgM82IdmmUySSZvLVf3gkTiGh4cUm4N0kuIFsjeeRb113sbNO5JyvQnomNWYFLCLATMC4EkfyXH1VKnm22Nc06xFw1eIjRIL9VQbrqf5KcKDY3X__u-YSu18ijJQhq0yNCgK8WY-eYzu8n4fVJ_SwUKG-mIPIWQUYehOKJCSPII_JCHKYVfLKcggQXMdGN2nnWy1oH8B4gclRuCoX0ni_2y-aT9MHhhPLQbFa1UBYv5MxfrVf7rlSWTCrOoYrAfMFxyxr2fp6DB-H3oQHiz6mzMHui2eJFVfeZ5u0i0c0lFZGIh3IDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWwKkwieimiDK8MCstTGO3V2v5xQHMnSAKfxTL3YcE7SzlwaToONBnonaSX6q7FDgnWBaKQPfzH2eCLnYXAPlG0YZ21lmQ1qRIJZYoU4-wMcflqsy2GBoDLGk9Yca9kV7s-ElQ5Xxh6S58024OF4Q_0OqlZ-AFyEWlBpYChog2I1eReXtaPjbqeyVCuGu6kSYdGhfYSakId0sJhWjeHXYDUEio7MfpSpbAMHbNKZhmN9ach1-QC4InKNBUpn5KuZ9Ascr8FgVy27cRDxhgJ7d8qz9idMqPQMWsI1qWW1yA3f9RgmxGQZlMPr0EnsT7vZlUvko2-_LMiZIoE4PRyXpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTC1WY2AqiLNiQLlu8IN3bk9RKfK7FhFgCxhUw3zlTqjb9oofA7aJtVUOOqj8-lfDt2XX03b3w1mThNz-FSva6Rq3cFk5X6wX6SMWQsqp_DghdZRb_64dZOHCH7qlUiIzgZTI2McB0c9fOftiJLnBaIAouY5WWyxbqBbpoG7SBPrGXt6ulKzjJtBcTBdY0EtlbZFG82Q8kM8y8Bt5L6TumpfCWrTP7mutDMqTQnGtnnGdkP6JXoF18C7Tq1jsb0mHLaohxUEE39vEKKtrQdzJRFWYHZF7zdDje3jwKmO9f-hwkBe2QMzLzzsyx1X0avQ2jqwHUvvsqqB1Q3QA_Fi5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIMUjj0VuZp0_MPUIcMHmPvP2MsH_E71gTrxCVQS2qi8fNZujw8cYsPmhk5JWFb2DYe5e5IQG5gcjl4LjAYVRkfO0VnlbZAHd_ZFDdbihUCT_dCSm3vleSmguPDzL8i3UUQ_OV2oDBvAl6sedcjL8MocK4G-RXK81JFvl4G6flGGm8gEaXnbwDg9xsFOhuHhkKfLW45VR-bWQQHvlCBHFpNmDDS0PTPyqa61jWwtLo1HkQn-GcDAZLOTHqPj-WIGhg34Y2ls0kqux0jdvqYzaAHMr_gwR3iTW9_ki2otmVphczYwCMtvMYA2zP17y1YBzB6tDwp1DPy4GMgo1ZYzkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6UXGDRWV0R45OIkLqTwBto7lQj0YWYwCAQG0uc3ux1PEU-quxcMpmSd-MEVHjOCry2kxH57ya-ruqLCGw5C_Lw9cPl4_fs1TiTfxZr3oaRgwZosGjGS952tiYBzExG6oiyLONUiqZXdYPNjWKTxx6Y_FnxXQ_sXpdRgxKn-YN1RcskiO7Da0TJBbx_Hj24YPUueZtkyAu5G-R4cpMSIOicQy92vWDcJ2VFzNJUhJ9XLA4RRuqgY-WAztmRQr8cBfZ8tcU882Kn3hbkRFplvU8gLN0PDp709g0zjeJnSpHKQC45rMq3cSkrXBfUV7oRcqXJHIDI4t3fRCGnDKlXXkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx8uxJNKfj4q4N-ZAhPp6nFhykHGqLbgGFZSSm9r_yP2p6dDlUL67Zk-yEPGtnVq5fvNEylMiAkuSHiXyf7b7J9GRvuTwAAgpQTEjTAau5uXogy5EM4N1XRTKXOY0YJWXCGGLzrlFOKubGCcxNCrh_WNANEBo1qjdrtVZvvE7uo9QPV-q_LYLwcrDsUc4NP-3eGS1pSXwZ7gkVcMibU5XjKskE6S12BTOEg5iQLQa2JstS_wS8Ju9I7gxwSKbzyQtjMt8hU61-jL_B-V0t5bB9CnIXtfYIRzHOFop4cLQy9GbBZpbNnleeHU-EjmRzMB-wcllBf6pFT_kAzCaoZ3Qw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=GX8ZBJi0fWmXT1VLR2Ay1CoaOCWput2O7NjK7SxloBnKqFnSWkgafGbX0vuxv7Tr-lVzqs5amz9S0A-j0tSmfPd90jwxymJlscF122HFD8ipt_L2Bnv23j65bsNNzUxCVguN9dfmH1o9dldpQdKzk9H8fbu8t9hmdzeFE1Idq1ZESVy7Ar-RQL6s2RQCRmF54tS5LJX8GBa_XDz1FmPDgAXMcCpfWkkVojyDXOG5GXzzsatm94xmO6TFIZoS3_paVHS_T-YZDSwwwrxpjo1NQWZz6agOcJhyLLCQoWSZ8skyQ3SV9oMfuLd3dxVJrkQNX-EGszxkRXnGZqg2yr0yHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=GX8ZBJi0fWmXT1VLR2Ay1CoaOCWput2O7NjK7SxloBnKqFnSWkgafGbX0vuxv7Tr-lVzqs5amz9S0A-j0tSmfPd90jwxymJlscF122HFD8ipt_L2Bnv23j65bsNNzUxCVguN9dfmH1o9dldpQdKzk9H8fbu8t9hmdzeFE1Idq1ZESVy7Ar-RQL6s2RQCRmF54tS5LJX8GBa_XDz1FmPDgAXMcCpfWkkVojyDXOG5GXzzsatm94xmO6TFIZoS3_paVHS_T-YZDSwwwrxpjo1NQWZz6agOcJhyLLCQoWSZ8skyQ3SV9oMfuLd3dxVJrkQNX-EGszxkRXnGZqg2yr0yHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYa03osEkK2zw2hwCIvWaqNbYFhvtTdVbl-zVnuU7z-S-KSLg54kK-f3LrOQFiXEGidAIdFuUSYQ68NqaPWZJmhMmHMomOod9Uu7c9nIhoPysRVWn9SfM3FS-xI1-mua2C2vn74wGKGJRmtJwjdN0mAFfZeWb6wWKwAUps6d5cCDCsJliIWTd_bJobmAiWFJv0-oJiFG95-FGLhEdktGT2sSR7RVgzNZzH_4B98g7jajFEu9IKIvxzxSrAHRZb2xdiQOEsfyPqv7Flgw-TA6mQYOCLPs7p2eiFZrsXs5jwl1w6ksLPgM2nlQgXdWA8fy7DGi6SJU_Dq8xURv1I9mGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0aHLSraEXpnZQaJKwg_aqaCzphtIJib9qwnmXQ1t1p7ybJcb9dYyHcVYQXYPsljX4xOqBqh3iwYOF4SMWDvAvRe4Elb1p-kTAu9Z-3fF2OUYRZmS5OCbEjlhKODLYqx2QEk3_p_3e8riktuhYX6X233GVizdIay5JbyjBEJ2F7s3YZfdr01AXoIZWZ7IE4IKPbl-V8LEjsn7tIwEeHxB8ekV6QsdWIhs7748nYTvOFI4WgNwfRi5G6dKqnv6oBfIWQLz2rBE4Ng90oAvWqVA7cg3Of5TGZy-v5US9iXF3l8lvqeHpdB0qHsGyd4wFF2En54ojtDMZrwK1nTCxO3rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1Uu5ygk5i9VdDDfjU8xG0e1_GV5u4lXr9jZpPIA6RYhVcVAzoiC03pSPTJP0dx5ibLilNqGKekXfqnulJl-PV_XT6BryUCpOm8yu578jMFmWcm3-8SYzYaI5GXpf8Y1_msuYLHbgzh6N7elkrxjKw0igKijf27bnQWntMVXKOMlMUS5_94BFhCPx9t3brq7b_7igGOKUaRHOMTEHId1qtcSj9CmGdAhMCUaRDKJZg2sukWIQctqHfhab5twPqEKQ6nRTZX3-p8ivdU15UfomrTVZYQLWLpZ-DvO4_TruXnHfriJG0oYqtN2szqwzuj3mb8KghZJ2PgRrxpEw8G2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlSwCXhOhL_xckZVjZw5Xk4_J2AMlP-i2D_IpGLhjH3DJqG6kS_52PEFn28uPmBiOLh0iKNgeuo7w1hCwZiGWBR40M8LL_CwqvGBnRNHxUcuSW3uBxL3i6HOjyLED4zE0tkWqtkY7lVVnFNjr7Zcdmz-rBbAi0PfRUfveXEZaVOolF9MG_97lAnl3t-jj1tAueSEVisIxMlN-2LLKf_vg7H20bMuOOaWHHjuaL-DiWA_UDZOs2oJS0orARbtLEZD3U8EA85uyr0HMFQc95ZQ_NrXKAEvjpNfh2oLPmSqcuod90q58iz8DPe0Val5bELXQmrYoMCwtz6icJnz7JNS_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDcTFGdAjCOM8gbvWAbBB7lo7-rRedGXmW-D-RPzMX0_AEiFjKmpes9zAngbzyBVevaPHH6T2WrJZ3TF5qABvKEvOyVKqmFSN1L0PTaR8i5CuZB_Wzu6ctFVB50IDVP73zPd_2bU473gIDJVCGas5a8t03tQVhU7EdcX5JzduI1z4KjsJ2YUimqodrRAFQT_N7X1AxHhQMAFdmQDE0R03bAqy6n2mVIOhIHVb9xkThyTDoLBYhS3s8L2zWP0KjZe4TJEP0Olf20JC0riU-bsKfWASS4-OLpfsPT9RpZgpeyjKP9Sh-RkbxVTqSP4T8jGMiRj0cSrYSrG_IbRXr3s0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKtRNeYYk3rLfAUyZLZGhlmZ810jcCA3eTheB3yBbJOrkMJ3T6nyRluFoO4KH-N0ECokshaJr7wpbar6mYjfwLU28yC4mQYZ-iIHafx8b6isou8-7aypDjR0X5s_bjov3cuvg9_cXVlfUo_P7cRoT32kKbzjUu_jQH_kwsjsTfxBp2hBWcpwWUaq1TFMxOZukb0oc7x9UUlJf1VxX4wRg336-L9bcONxdUXSjL4AXZYYNNIBgfMksd4fVlfcdPqJNeUSbCdZ50cy6RGDqXyOt4GDPSuv44Htgz_6CgakSGpZP0lSWPjzllfV1b0wn5na-6h8BD2sqUBaZVEokehoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi-NRd6WRBWRf5GH0KuMOacx3sbOGCUo5fbQ6x4UgWLcWgdEgAJ4vJVQyxeQodiVir5LWPdbn4tXzG2_3SQa3FX8MINU3DQx0lrO8_SRacZassOmGbJO-KZBgOKcsdX5xrbNMP5O_UjmYVcEoS-1lfC_p8AOxTF_xGyNDOstXRTBw-puFjOxswQ-0WkHgUXYHDuCwLewrn7CzNujR7zVQVyv_dPgHY-2GGjzqoOorE_xpyJHM-s1R-GR0mYplk96a_WCqQ-RusNs2NYjdAjIEf7vtNquKWAXAa1ipqnOxBUrYuqJvbqLojLvYRGY8Zl3gYD7eN4Tr-mQjK-WrLXEDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=v7SRIvRSA4ty_lb4oplaHvoSAYZcLXupRCIiCKGKsjjTiVg3qW5FTxydns8J21ckxZ-YUSS-xOv9tRY9MacmOVRSPxmZLikt3tjrxVNkY25A3S_HlfZcpOTOzgdK8vak-9FVrWJ1uXQN3HW8mnO8as4HP6qPtVFzXLxEdAqd04KskdLAYK_z9yG08tuOIm8mdQazjFDQjv3-bxDns-PF5o5zwWygGAzlOM5oqgU4zvsv0P3PN-QR0kMiJogcEGpmdKuxZCZf8mazCucIqUdXUsku92BFMSWAxzS4EGC5OllLwPS4m4nzQwClOtUQrn1gV9UoRc3Nk0tSxXxXbAXnsl3rGwrlmi8kwTyR08w69qXMbqDLyNP3d6dRrenuysC29TnCTmd0BrTodoJIo3c-AKh-TXcoQQXgelZiYzuOqF1kZz0bCma3X3IKBQQeTZjE5X-LjFKablgt-l4ErQEUwQF3lukcqRQ8cWVZPLxkHsBrKavQu7jqU-8ecLdRwY52bgWvTp3XRa6CmytwXHu7nnQQXYYH_Agb0CL_Ic9gAcxOA7HRtfpNbtz-_avBDtToJgLxuOCx71GH9DGoFpBe2VsfYTbTIGTqYggm0U1TP-G3vwQnw9GcGhhAebOOa4wXeI2Q_dU-kkd8M98meUF_88yAk1wL-wQ7RRawgVABNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=v7SRIvRSA4ty_lb4oplaHvoSAYZcLXupRCIiCKGKsjjTiVg3qW5FTxydns8J21ckxZ-YUSS-xOv9tRY9MacmOVRSPxmZLikt3tjrxVNkY25A3S_HlfZcpOTOzgdK8vak-9FVrWJ1uXQN3HW8mnO8as4HP6qPtVFzXLxEdAqd04KskdLAYK_z9yG08tuOIm8mdQazjFDQjv3-bxDns-PF5o5zwWygGAzlOM5oqgU4zvsv0P3PN-QR0kMiJogcEGpmdKuxZCZf8mazCucIqUdXUsku92BFMSWAxzS4EGC5OllLwPS4m4nzQwClOtUQrn1gV9UoRc3Nk0tSxXxXbAXnsl3rGwrlmi8kwTyR08w69qXMbqDLyNP3d6dRrenuysC29TnCTmd0BrTodoJIo3c-AKh-TXcoQQXgelZiYzuOqF1kZz0bCma3X3IKBQQeTZjE5X-LjFKablgt-l4ErQEUwQF3lukcqRQ8cWVZPLxkHsBrKavQu7jqU-8ecLdRwY52bgWvTp3XRa6CmytwXHu7nnQQXYYH_Agb0CL_Ic9gAcxOA7HRtfpNbtz-_avBDtToJgLxuOCx71GH9DGoFpBe2VsfYTbTIGTqYggm0U1TP-G3vwQnw9GcGhhAebOOa4wXeI2Q_dU-kkd8M98meUF_88yAk1wL-wQ7RRawgVABNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5h1EVffkZ4e7AHc71pnPSUD9xMzsomEpTBg9GHQ5G7EuGjcK9oYflU96LmOdejiWqMujVBpEz7S9vVenC0HsWKlo6OAjLabiM1QELpYeckundg-QCjXa3bHfhxUc-QyMsBMe2dIhyFNpsaYA1AUtxNEgJeHrQZz0mNI1rNpM2R-GllmhN6l8chUu_dQWIbB905ARG78Er2Yjiaa1GjdfjnEwteltPOH7nalGVXm6Yo9iyU9XWO8vLWHx0FGO39S5gfCIQePNijT9kkBNb0utJmG9mMtvGmiW8lPkNHceIqwhDX-E4dQXCRYC0ibzUEn4yufMAi7gmQWMfuoP0vwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hipCO089U2XXWPynyz41sUldk6rIWmAL5c9TwieR7V7tJo-w5hsGbsGmRkVPpqUuemJ7S_rM1PLTZM_ZtTNWR0xctW4cEY9X_lf6KhftE8TqJdLeSKcDf2EuBc6qfgsv6_iyf3d7zNpomEWvKGD2gEfzcHticGmOe9s0rgImZRnV6fI7Qc7BCLlRe-r1eN_VqoZKVKEB2Na7C4BI_o1TTgv8lmW5lRSaWepa8EQ38PLUzF7Su15T6Rkw2XqQ--5XiGdV_vWpt1IHya66WxxsRkteXcOSzW-7NXVe3bk1RLkWaa0-3KUij7_CWSLwFQWuBhDrJHDDBZR7pqY3onbXnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHgWvw8bhYEx2C7ASVDhrzxPma6IYol_rwCIpfrWaY4zbhaT9Ay8JbUgKgObGHBJ2Q_3yMlj8Pf8FCES6_OcyfeXznjPMhxuIe8qsv2nFukfkD5ihJRP_wT3TIF8-JMVAcWsGFRKo7gu1VGf-b1PEMsWCQ6BLDkjszR45SF6nUbNGMyBSyqMB41HM4ukyJUmXGgJYnL5Ub7z-ASloxE1-SBc2YS9O_jv1VzoW9QTxSrCtk9mdeR6EM8_Quo9podTqyx-9buiGWMtV1WO6t-sdK36y2GHdZcvtn0n024eIKoru_xjnzMM5IHUxq7YvsaymOAAatQPKdu_4APb3KN6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h31VsEadq24qHM9JDOBFZclvML0qSmrRUZyNWqrfMf-vdJvNE5_ONVtmP06P9c48PAimLc4vBW6adnlovCVzBUfwmObzxWAQagEaBI1tuRZ6TofhG4bUzd4mfdwe-nrXAUaq5X8HWwgXwmR3DR9VEiON3FxOmDTiZyiPxi9GMpoHn5CRtvTMXy7KPNenBe4mBmHA5h0_o51oigKQvDn9NAWZqmgW5xhrF-ZuFamyyfESAYoKxXMq5GMRAK1L-V514MeZeDFEq5c2GsK2HZq-kASWlFOgJtYy1wmvfU0JUe8xtCoNlfX7Xy-NguUL9ro9v3nPztCdklPDaFJnw7dkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbELlHWk43I0-vGH3koC1zuRDx187KuUI3WXCBndBBuNlqvjZXbQS71U5vF-cm8jIXjfQsdlVmFR15TMeDVeFdXDdP5t0O-s-3iNSG8b3F6KoUrAo6ki38RDLzBDmRJWkaV1cMaTX_oSSwqTq_m1Ig-H5Rd6m1D7RRVM01OhqcQnmeMCQ0KT5cZ1vz8LGS9zEzUP1tERL1ehmHQCG-vSeEJWPtK0x8LQZqFztpohguKFrM-tOXF4SjYQVVh6NBfY0MJi71WPC_xep0o-AmG-Ah3SHdKZT-oHSJt5FmXQZR1f4SZjK5fOTPhSDYziCa192yb4pbzwJr8EFntfTAfFdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aBdliBBjcxKKx2H7erw9m03PtfM3QJzsUJXnFKVxqZeXMwPGK15g2UT8jSWnmWMFNQXR5296Bb-6MLKCtipfrCTJbpVBr9s2ErqGs71aFc-8vUurZtwYxj1_96seFFuCKBKMNJ3MQXuqYzYUDchOLq9l32N9CQpRNn4C0nwj6nxtqGwjdKhIMtThM-7FOPly-bWM6aua6tNFDxDcdcFnamlZ7OaHeScTQmSLwfcN3nE2GhxNiwN-ptq9TmaNWO8bvZRdfT_6wgMPwbzUs0XvfnWBBcPjoANANIElr-13d3AYYpAQJE2iQJP9_HuwhQeBwtM2hzSsIsetEdo8es3_Vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aBdliBBjcxKKx2H7erw9m03PtfM3QJzsUJXnFKVxqZeXMwPGK15g2UT8jSWnmWMFNQXR5296Bb-6MLKCtipfrCTJbpVBr9s2ErqGs71aFc-8vUurZtwYxj1_96seFFuCKBKMNJ3MQXuqYzYUDchOLq9l32N9CQpRNn4C0nwj6nxtqGwjdKhIMtThM-7FOPly-bWM6aua6tNFDxDcdcFnamlZ7OaHeScTQmSLwfcN3nE2GhxNiwN-ptq9TmaNWO8bvZRdfT_6wgMPwbzUs0XvfnWBBcPjoANANIElr-13d3AYYpAQJE2iQJP9_HuwhQeBwtM2hzSsIsetEdo8es3_Vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-T96FUefP8LhDNrtBj41lzfQC9FJPpOXPL4Hdin7kriAu-M0Py0o-x9ZRvimYht2n0clRas2VeX6dLJp-xfbAY3vFcboDjt3u3Vlvl6FNITI487Rt9PZwpYtVgnzrJ9YPZLuh8843nH9kvB9vBaJY7OsRcIndnAoZoYmBjEwJAER5tRa5YaRAQqmzfsFbGWdIVNeYl4tUx-PRdToNJVNlMYxaH5PI7uPvQM0132eJCXUjvZVKcuMjGtUXiwJPl0adiIfjiPwq5wAFJd9AeoMCQaSNH_cCCqw23Ew7h0YIOPdKVnkT2JPrpja1J0e5w10g_IbWCiUkHvfi7B3wuB1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxgkfDgMunXmvANiHioEe5BGTvGi6Y5cpldxHjy7VUAfzuZktpuztmQ6cvWsubFgNyNeSeiDNyyTSaOfve685v1VyiX66_Sakq3qUIQ4dIFrLaB4wRweFiENBqEHL0WmuSTNi1nCH49EHgnNOmhboYeSSp6mWTlau2zVkx4newUtWW6-7taM5gNyFjiCZeavVF9GK8lBwQi1a4QomaEcaZbfnPae4TOoOnBdt4Mo8k3CAeFMWPDPpyS76FjQ8zSXMHe38mInDoltOOxVpQv-u5BNSENyj6rQqwWOWiIcuJRu2pqk89A_hT00-tcl23RpfAlx5wrk3FcSF5WknMcPUA.jpg" alt="photo" loading="lazy"/></div>
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
