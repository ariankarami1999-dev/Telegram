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
<img src="https://cdn4.telesco.pe/file/WhhBM6f7AkA7Y29iNqYOcm5u7-34VwaAw3uTeaz8iFB6shMOp7MkHoIINx8QghLj1j7sJw3rKpZATo5lFn8bwo7PKXa_eSTJQwf7Ae9-aP09ngCkYAuKfuX8t9LdonEv7EHIUk1jo4ZmOBVFaIQwiWOa5BSjs4IeHdjl3VHMc677p5FV_61ZRk2krC4RkTTzwbHvZ2FhAZSSE9ppHI5qrCSKTXsDefXZdtcEc5BKgRHFb_Q4TpoJY87-a2E1CzvzJ8WRdM0f_axdmeKv4aJBvy-RfEKveve4K5gAWFH77dLQNkU89r3ZyDrsc87cAPw2jE4Cab3FQSWZZAzH4xsDKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 14:41:23</div>
<hr>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzM0AvsKTBU65iyzCJJpw3MosZqds3LBdNkj0zy83oOlRFXkbz99A0aqjDpwI9-Jo83mcJC0F_jffrpmPEEUOAi01ixbIDYOG_SMkdon0rVzsZWJvleAjvYmLwod8H_M_bb-M0bYlt4R1IlE7ATa8x9N_NinUvm9JMKg2G3kbNcxyaxTq6eZCx4rH-IbG90cwQ8O-Paf2jD50GZiQEdxvtWwGFKjZS1jxeZEIRUrSs71RWXJJwNQnEA8yfVq--4NWnniv24Q6d50RewpjzBxYePegS-YVq3EHCPGBPriIH0__B8jATjOfpkR3p8F7Yqsjcs22w8TFbY5oSZHsfNa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی بریتانیا تأیید کرد که یک حادثه امنیتی در تنگه باب المندب رخ داده است، این در حالی است که یک کشتی سعودی صبح امروز مورد هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/withyashar/20813" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/withyashar/20812" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه عبری : مجتبی خامنه‌ای، از احمد وحیدی، فرمانده کل سپاه پاسداران، خواست تا برای «عملیات تهاجمی قدرتمند علیه دشمن» آماده شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/20811" target="_blank">📅 13:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ درباره ایران: ما سه راهبرد داریم , همین کاری را که الان انجام می‌دهیم ادامه دهیم؛ فقط به همین شکل پیش برویم و ببینیم اوضاعشان چقدر بد است، چون تورمشان ۳۰۰ درصد است. پولشان تقریباً هیچ ارزشی ندارد. حقوق سربازانشان را نمی‌دهند. سربازانشان در حال ترک خدمت هستند. بنابراین همین روند را ادامه دهیم، چون این وضعیت پایدار نیست.
خیلی، خیلی سخت به آنها ضربه بزنیم؛ یا در واقع، راه سوم این است که از نظر اقتصادی آنها را شکست دهیم. البته همین کار را همین حالا هم انجام می‌دهیم. این تا حدی بخشی از راهبرد اول است.
بنابراین از نظر اقتصادی، آنها در وضعیت بسیار بدی قرار دارند. نمی‌توانند پول قرض بگیرند. ما کنترل پول آنها، یعنی آنچه در اختیار داشتند، را در دست داریم؛ و مقدار آن هم زیاد است. آنها پول زیادی داشتند و ما کنترل کامل آن را در اختیار داریم.
من بانکدار آنها هستم. من بانکدار آنها هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/20810" target="_blank">📅 13:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ : می‌خواهید یک گورستان پرندگان را ببینید؟ گاهی اوقات به زیر یک آسیاب بادی بروید و هزاران پرنده مرده خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/20809" target="_blank">📅 13:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جورسلیم پست : ترامپ از حمله گسترده دیگری به ایران خودداری کرد ، با این امید که فشار اقتصادی بیشتر می‌تواند تهران را مجبور به تسلیم کند، بدون اینکه منجر به یک جنگ منطقه‌ای گسترده‌تر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/20808" target="_blank">📅 13:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJwa14lNoxMcWUtqA5-jgITPrzf9jSBkyxMqiEdbifXpIr756gcd84WBIrTJF7pRU5-9JuFlxUxNYi3X8m2unWdvVBHazlAxTcarE8RTwei4Bc0QjFQjfSnWyLww0I70K_1A3YrdlscUkUxi6dXzPxq3a-uhoRw1wxjGoRwEtdyOnUBqZqmGse3XoZSnQ-lE5REXZioHLNKlBpmcwy4L8hTga1X0OmNqMCjtYf9YJMl3fewSV_hS8Z-AvuPI3OpOGhNJcCiOAvSJrJDQkckUsdDVbqaBsHGqGnQ_pr6-BRUNLkYrHhSz7U9Ly2eJlYQU7wFQPK1yYP2sS5xKD9Y7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای برای یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است. مقام‌های مربوطه در جریان این حادثه هستند و تحقیقات مرتبط همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/20807" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKefenrtjK3gcAV2aIMuifdQbaQ2_llbH21VF7I-RM6_93x4mj28mK8XqPKeW6ZRtUXGg7lOhB0ZrPHSArMqTlkGLjnX-lpvN1xZ0P3oekUBjMm690Sxm2sj3yeve-4QMEwa5w3UF9h4jsd4NJnBuedOJorhanRnRiLOrC0qTsJMRY3zdd52mx_TfimxCfpgrQgMnoQM7Z91_vYGvC22V8uKnfKt-Eru2_-NdiSOLVjk1dgshubHxNwkgs8SnltULedXSWYnvDThQJEFSA8g6KwHPdv5sQ6XTfy9UEsv_oZoJ2MxU0FecAaHgzxxBU1XQ7Y_mVn3tfqmywy3J_C2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/20806" target="_blank">📅 12:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دادگاه جنایی دمشق حکم اعدام برای بشار اسد صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/20805" target="_blank">📅 12:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">https://www.instagram.com/reel/Db5HBuLozsg/?igsh=ajBqMW82djZrZW96
استوری که درخواست زیاد داشتید رو به صورت تریال پست کردم</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/20804" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارشهای رسانه های‌عربی حاکی از کشته شدن ۳ نفر در پی حمله حوثی ها به یک کشتی در تنگه باب المندب است
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/20803" target="_blank">📅 10:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If_a-DPCFsPm0Vkd8X_54HfiwueUNoY4bxwP4ojvjZqsS3ZG6ABRSAOWh3KUFPb-kn6FkqXRKi4yygSz_7EsDQFzFlUULGItWFY7U_HND2vtw3HZy3HpbPh7BdRYXbt6LS83r_G-VrDWJ0C9M_KTk-RSHvQnh1SGIhttjQ7lxtgp_s2W-c7KUaa8-ZaZq1MaZHgURyyuxh6OwjsZLB6pWJwc0y0cMPFOjki3z34E12u9z82lggTqSMu_zYkka7-MA5KaL4oFpiPDEkB6PKluL7Le4ASz0-VvntzxPqhTLz9o9chyiQ6ZbAXKV39kF81GHDEkULyGMPX0tS3qMTsbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برای عبرو از ۹۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/20802" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع. @WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/20801" target="_blank">📅 10:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند ‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند.…</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/20800" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏رییس اتاق بازرگانی ایران و چین با تاکید بر لزوم پایان محاصره دریایی بنادر جنوبی ایران گفت : «چه با مذاکره،
چه با خواهش
، چه با تهدید و چه با جنگ باید این محاصره دریایی خاتمه یابد» و افزود: «تبعات محاصره از جنگ هم بیشتر است.»
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/20799" target="_blank">📅 10:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز: تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند، به ۶ فروند در روز دوشنبه کاهش یافته است، در حالی که میانگین این تعداد در ۱۰ روز گذشته حدود ۱۱ فروند بوده است. این کاهش در حالی رخ می‌دهد که امیدها برای دستیابی به توافقی بین واشنگتن و تهران رو به کاهش است.
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/20798" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع.
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/20797" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=l8J-vVmmnRB4NcICMZ8vmhfvHE-ShJLQr1O6TdNTIZUz1O72_ofO7Owlk9z_Pqf3aYZjDNc4hGovhLUctYgfCnA_gTVVnLj4va4gJepT0vqBCgPQn8jpPCtnnomecmMjvHZQ9nPeBwgjB3RQGFjzBycZLx5EV8Qe_K-p_ZDcNUtE6EWVbcPLEK0XQKLYZjdUW9buOLGLIcntHyzRttEzyJPSw3zJ9JyPUJJDrggFsuyuP9fkpN5jN5-5nA9hNBCDuOh_-ojasQLUmAcn4EM0ch3dEoEBxTQsFK7Bvn2o-jZWKTm3DZyo6TKyfDZTC1DTbq3nE83d5gZOUrKjjjbRBjLggHFuqkurukihvSH9xBGby0EZ-G9lfdDR9tg9fD43GsnILUQmIv_4FEmjESWz7PcGWnjoUjoTt4XIYTzupSbDIw988nNr4FgTid5oEweglpYF5AKRRVx_plGoEiPQRPBzmjF5sWksLuRfQ5kBKgRfDHDBDYYXVScpSmi4db-pxU2MJtyF2D7X6gmDUD8mkd3Zx3nAnc-89a3xN_vx5UK4dNGeUNFEMbk2L5e97iABURJ15WLSusRlm1bR6LmovE4YTwXFX5iuQ8Gv1Ygl_fzMPdc78N49XxGE5T0YMUfd34OumXUB41P4rC4jjV7vxsMhhYXwz9h0ubeCaNXXqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=l8J-vVmmnRB4NcICMZ8vmhfvHE-ShJLQr1O6TdNTIZUz1O72_ofO7Owlk9z_Pqf3aYZjDNc4hGovhLUctYgfCnA_gTVVnLj4va4gJepT0vqBCgPQn8jpPCtnnomecmMjvHZQ9nPeBwgjB3RQGFjzBycZLx5EV8Qe_K-p_ZDcNUtE6EWVbcPLEK0XQKLYZjdUW9buOLGLIcntHyzRttEzyJPSw3zJ9JyPUJJDrggFsuyuP9fkpN5jN5-5nA9hNBCDuOh_-ojasQLUmAcn4EM0ch3dEoEBxTQsFK7Bvn2o-jZWKTm3DZyo6TKyfDZTC1DTbq3nE83d5gZOUrKjjjbRBjLggHFuqkurukihvSH9xBGby0EZ-G9lfdDR9tg9fD43GsnILUQmIv_4FEmjESWz7PcGWnjoUjoTt4XIYTzupSbDIw988nNr4FgTid5oEweglpYF5AKRRVx_plGoEiPQRPBzmjF5sWksLuRfQ5kBKgRfDHDBDYYXVScpSmi4db-pxU2MJtyF2D7X6gmDUD8mkd3Zx3nAnc-89a3xN_vx5UK4dNGeUNFEMbk2L5e97iABURJ15WLSusRlm1bR6LmovE4YTwXFX5iuQ8Gv1Ygl_fzMPdc78N49XxGE5T0YMUfd34OumXUB41P4rC4jjV7vxsMhhYXwz9h0ubeCaNXXqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واشنگتن پست:
در پی تهدید به ترور از سوی ایران، دونالد ترامپ هنگام ترک نشست ناتو در آنکارا، ابتدا مقابل دوربین‌ها سوار هواپیمای قدیمی «ایر فورس وان» (بوئینگ ۷۴۷) شد، اما سپس به‌صورت محرمانه به یک فروند هواپیمای ‌کوچکتر
C-32A
منتقل شد. در همین حال،
هواپیمای قدیمی ۷۴۷
به‌عنوان هواپیمای فریب با شناسه «ایر فورس وان» به پرواز ادامه داد و خبرنگاران و حتی برخی کارکنان کاخ سفید تصور می‌کردند ترامپ داخل آن است.
در ویدئویی که از این عملیات منتشر شده، ادعا می‌شود
انتقال ترامپ با استفاده از یک کامیون خدمات فرودگاهی، احتمالاً کامیون حمل پول آرمور(زره ای) ، انجام شده است. این در حالی است که
هواپیمای
ایر فرس وان
جدید ۷۴۷-۸ اهدایی قطر
، هواپیمای رسمی جدید رئیس‌جمهور آمریکا محسوب می‌شود و با آن به آنکارا آماده بود و در این سفر، نخستین مأموریت خارجی را انجام داده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/20796" target="_blank">📅 09:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M70cfwI6hEkz_XS5Qvnm3-1ztUFIpqXE6ksZ9oMba5txMOuPed66PMQnCdjrMB4rUYTA8Tl55zBQTezAGiKyvuvkiRTn-h104zK2UTCpqtO6Tl9DaN9sFq1JiPCjTDDTKGz9ADNhO_Nh3V1Q8mmoZtmqc75YFd2aBx1rgJoKOXbNHIt4G20qxrCLsQ0lQp3yWX8ornMcFsQDQUfePVElLn0KlOVeaZOdFaQqmvgi6wZzdCOSmDvHeK_gU4pNGPo7susvExHewP1anC1D4ttrJmCDouHD0DE413S0EmFgqH4LPvsdp_EgPC8OTUOHMFNasb3sPtV1HHRAFOa1MR3Txw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ آخر هفته را در زمین گلف خود در بدمنستر سپری کرد؛ در حالی که یک سامانه پدافند هوایی کوتاه‌برد
AN/TWQ-1 Avenger SHORAD
نیز در محل مستقر بود.
(سامانه AN/TWQ-1 Avenger SHORAD:
یک سامانه پدافند هوایی کوتاه‌برد آمریکایی است که روی خودروی هاموی نصب می‌شود و مأموریت آن حفاظت از افراد و تأسیسات در برابر تهدیدات ارتفاع پایین است. این سامانه معمولاً به ۸ موشک دوش‌پرتاب
استینگر (FIM-92 Stinger)
، یک تیربار ۱۲.۷ میلی‌متری و سامانه‌های دید حرارتی و هدف‌گیری مجهز است و برای مقابله با پهپادها، بالگردها، هواپیماهای ارتفاع پایین و برخی موشک‌های کروز به‌کار می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20795" target="_blank">📅 02:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ادعای وال استریت جورنال : مسئولان ارشد دولت و کاخ سفید به ترامپ توصیه کرده‌اند که تشدید تحریم‌های فعلی و اعمال تحریم‌های جدید علیه ایران، ممکن است موثرترین راه برای وادار کردن این رژیم به تسلیم باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20794" target="_blank">📅 02:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20793">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=KcC_PpB8WYb-B5RBYJ4Ve-Cfza92-VKk0nsDVBsN7IDYVTmOd0oVk6HRbL4n_8bkcEpeDkIaGCjqCXUyu4hhPTqiTuAidpAXuBH-Aj7hzQeuhfQZ_aVMZZHbFqDyxVtrEgqOPwevFsO3GjztotOxevRSprtycMoNlQzdULgvLGJMkQUDUwkOpqRLI3kOJCVLsCmJIyCIVkZ-v1VaMAEtHHj5xGj1frszcIs_L9TB-KbFpbtI5xEeL-dKwOWG2mwWgcJNKEHQwX5F9hsar7UlXU21x6Vk4n9if_XyJXGqYA-9szq0XnYxBkWJZkaqSJyZ1nn7ii4Ew9IUDdy0VrBzC5DdyiDbz6hjm66sezDMYXHYVxlu2aFtPRZnMMSmHECdtj4rDckRAEuWEoIETVLch9Q4ORxWVHzBCGONU4veVRs4x84uozdTpjLVHdwbIkjKGLR-AWKLfx3Xub-TSggPHCy8Wuhoz01TXml34K18XXmOeHFzRnoYcst5MJjl23LKPs7gg0u2hrjQvKTsG_VRjmaPvSNziqzR71xc16I7ZCUSMZPLhNErWE9oXMLMVqRHm-1eoxI3h3dZCoYS-SObgL_DaOxscxmPwoz0XtSuBV4NutjhRliemWPhjYmRkRS-kMHt_dUCmIabwjqL7OMgxXEQK7wv0sXi_KqXRMjocKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=KcC_PpB8WYb-B5RBYJ4Ve-Cfza92-VKk0nsDVBsN7IDYVTmOd0oVk6HRbL4n_8bkcEpeDkIaGCjqCXUyu4hhPTqiTuAidpAXuBH-Aj7hzQeuhfQZ_aVMZZHbFqDyxVtrEgqOPwevFsO3GjztotOxevRSprtycMoNlQzdULgvLGJMkQUDUwkOpqRLI3kOJCVLsCmJIyCIVkZ-v1VaMAEtHHj5xGj1frszcIs_L9TB-KbFpbtI5xEeL-dKwOWG2mwWgcJNKEHQwX5F9hsar7UlXU21x6Vk4n9if_XyJXGqYA-9szq0XnYxBkWJZkaqSJyZ1nn7ii4Ew9IUDdy0VrBzC5DdyiDbz6hjm66sezDMYXHYVxlu2aFtPRZnMMSmHECdtj4rDckRAEuWEoIETVLch9Q4ORxWVHzBCGONU4veVRs4x84uozdTpjLVHdwbIkjKGLR-AWKLfx3Xub-TSggPHCy8Wuhoz01TXml34K18XXmOeHFzRnoYcst5MJjl23LKPs7gg0u2hrjQvKTsG_VRjmaPvSNziqzR71xc16I7ZCUSMZPLhNErWE9oXMLMVqRHm-1eoxI3h3dZCoYS-SObgL_DaOxscxmPwoz0XtSuBV4NutjhRliemWPhjYmRkRS-kMHt_dUCmIabwjqL7OMgxXEQK7wv0sXi_KqXRMjocKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند
‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند. او گفت: «همان‌طور که رونالد ریگان در قرن گذشته در برابر کمونیسم شوروی ایستاد، ما نیز باید همواره در کنار نیروها و دوستان آزادی بایستیم؛ چه دولتی طرفدار آمریکا در برابر شورشی ضدآمریکایی باشد و چه مبارزان آزادی‌خواهی که برای رهایی از دیکتاتوری‌های کمونیستی یا اسلامی تلاش می‌کنند. همان‌طور که پرزیدنت ترامپ اوایل امسال بارها گفت، کمک در راه بود و مردم ایران باید آزادی و سرنوشت خود را دوباره به دست بگیرند. اگر مردم ایران به آینده‌ای بهتر دست یابند، آمریکا امن‌تر و جهان نیز امن‌تر و صلح‌آمیزتر خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20793" target="_blank">📅 01:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HktMPEgQil_dgNwi2qcr6yi15GtduENj4m9FVwj2CfttZmypWE5hZUi38hicE0b5dFL8ZFYoVbOpkHF88Mbc5bToLgCSdnz8HHGB7MLC-TmrxkjmIs8-PdvYsPrtl5Qqqk3U8D2ueHqnWeHxPrJ5ZbN2j98yrD68jJcSrPpn0bAjZfLVEQWZQURCGO1xa0O0KXjmuiUSnjqpuDKkkEFtbZ7R4SYsK6iAaTW1pHI1g_f1yZYzYWXQSNF3uyn5RPOwCv9peZPI-r_RFHOT1xzuxgb4GoRQdCILNyCeSM6-EGA-WJU7rwqQbx1Mbwev3chQzwrW1V_Ebf0bJN4jhOCeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۵ نفتکش مرتبط با عربستان، که بیشترشان نفتکش‌های بسیار بزرگ و خالی هستند، در حال حرکت به سمت خلیج فارس هستند.
ترامپ همچنین امشب اعلام کرد که تنگه هرمز کاملاً مین‌روبی شده است. باید ببینیم میتوانند عبور کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20792" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اتاق جنگ با یاشار : کنگره آمریکا در تعطیلات تابستانی قرار گرفت.
سنا از ۸ اوت ۲۰۲۶ تا ۱۴ سپتامبر ۲۰۲۶
عملاً در تعطیلات است و جلسه عادی بعدی آن
۱۴ سپتامبر (۲۳ شهریور)
خواهد بود. مجلس نمایندگان زودتر برمی‌گردد و
۳۱ اوت (۹ شهریور)
رأی‌گیری‌های عادی را از سر می‌گیرد.
حالا اگر آمریکا در این فاصله به ایران حمله کند، تعطیلی کنگره از یک جهت می‌تواند برای دولت ترامپ یک مزیت سیاسی ایجاد کند:
ترامپ همچنان فرمانده کل است و تعطیلی کنگره به‌خودی‌خود مانع دستور حمله نمی‌شود؛ اما نمایندگان و سناتورها برای تصویب قطعنامه، محدود کردن بودجه یا اعمال فشار فوری علیه عملیات نظامی، امکان بسیار کمتری برای اقدام سریع دارند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20791" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20790" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کامنت جدید برای ترامپ (کارای اداری)
آقای رئیس‌جمهور، فن آخر استاد را اجرا کنید
🎯
https://www.instagram.com/reel/Db30SjjS-Wl/?comment_id=18183518170406206</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20789" target="_blank">📅 00:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
رسانه‌های سعودی: اسماعیل قاآنی، فرمانده سپاه قدس، به بغداد سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20788" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عراقچی در تماس تلفنی با همتای آلمانی خود: تضمین امنیت تنگه هرمز مستلزم توقف اقدامات تهاجمی آمریکا، به ویژه محاصره است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20787" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: رئیس‌جمهور بعدی بابت کارهایی که من انجام داده‌ام، اعتبار زیادی دریافت خواهد کرد.
لطفاً یادتان باشد که این من بودم، نه آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20786" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار: آیا پاسخی به نتانیاهو دارید؟
ترامپ: من امروز آن را در تروث منتشر کردم. من یک پاسخ دارم، یک پاسخ خوب. بله، رابطه خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20785" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6383d52564.mp4?token=hHtSHoAekO9-IGNF2hwChxDPWK9nssUzaStgk4u5Rm4Pu3YMvIi6qXIF8KU197q5jE4RzwovfKEsIIiQVStbt9E4UrT7FcBx0xgMuxsM9nF7UBIkgYEw0aT7biJSEsNQUAiOWKoCg0uexMXK-yMBygP6IPVjBjuyys75DuqZYpMkfgYna26uzCVejkZBtOKFpUB5W1g9gj14IpUeEuH4125eOQqYiixihnd5EelnGkCPl0THbLbhIGDL7gSK3TUMTJoLAzPKx7MUOStmrx3bOhxlGzQBBz_TRghGwfTgKuIkwbUEust6tppTEkUolSilgSsQubbtSYiLwm9L69yt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6383d52564.mp4?token=hHtSHoAekO9-IGNF2hwChxDPWK9nssUzaStgk4u5Rm4Pu3YMvIi6qXIF8KU197q5jE4RzwovfKEsIIiQVStbt9E4UrT7FcBx0xgMuxsM9nF7UBIkgYEw0aT7biJSEsNQUAiOWKoCg0uexMXK-yMBygP6IPVjBjuyys75DuqZYpMkfgYna26uzCVejkZBtOKFpUB5W1g9gj14IpUeEuH4125eOQqYiixihnd5EelnGkCPl0THbLbhIGDL7gSK3TUMTJoLAzPKx7MUOStmrx3bOhxlGzQBBz_TRghGwfTgKuIkwbUEust6tppTEkUolSilgSsQubbtSYiLwm9L69yt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایرانی‌ها صدها هزار نفر را کشته‌اند.
حالا دارند تاوانش را می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20784" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها می‌توانند دردسر درست کنند، اما ورشکسته هستند. آنها پولی ندارند.
ایران کاملاً ورشکسته است. آنها حقوق سربازان خود را پرداخت نمی‌کنند.
تورم آنها 309 درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20783" target="_blank">📅 23:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=qRvmhlbTHgf02NIIdp6GB9OcRv7hQeEm6RMqclbM-L006O2Ou6WScT_JX6QzP4l-XF6WLh72prw7VUGx7oWi0ggk7q1sIv_oI7G5GKQj25outXBLjpASz9JracdMxNY-H8p0ZhHq2Sc96Ud7wH1vLjHuRgHC1u131GnG5fuuDzcYd7xwNwyRJvZT-Ynb-4U0lf0TUzgq6LbZ1Lgtu7BkVEvjq5GHxNKZoG-21_svV_7N7jHAdgF-plGpOzL5GhAdvMjV4wGhktMMCdG6poSUybuSyB3nbK61hSbS11TkGAEjBZ6dgkCxgaC9uhCrWKQphh7O2D5xFR-V3Fq5jATT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=qRvmhlbTHgf02NIIdp6GB9OcRv7hQeEm6RMqclbM-L006O2Ou6WScT_JX6QzP4l-XF6WLh72prw7VUGx7oWi0ggk7q1sIv_oI7G5GKQj25outXBLjpASz9JracdMxNY-H8p0ZhHq2Sc96Ud7wH1vLjHuRgHC1u131GnG5fuuDzcYd7xwNwyRJvZT-Ynb-4U0lf0TUzgq6LbZ1Lgtu7BkVEvjq5GHxNKZoG-21_svV_7N7jHAdgF-plGpOzL5GhAdvMjV4wGhktMMCdG6poSUybuSyB3nbK61hSbS11TkGAEjBZ6dgkCxgaC9uhCrWKQphh7O2D5xFR-V3Fq5jATT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: تنگه هرمز کی باز می‌شود؟
ترامپ: الان باز است.
ترامپ در مورد ایران:
همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را مین‌روب کرده‌ایم. شاید نشنیده باشید.
ما ۱۰۰٪ تنگه را کنترل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20782" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ: اگر قرار باشد خسارتی پرداخت شود، ایران باید آن را بپردازد
ترامپ: تشدید شدید تنش‌ها همچنان یک گزینه است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20781" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرنگار: شما گفتید این آخرین فرصت ایران است. حالا چی؟
ترامپ: خواهید فهمید.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20780" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ درباره ایران:
هیچ اتفاق بدی در نتیجه اقداماتی که ما انجام می‌دهیم، رخ نخواهد داد. هیچ اتفاق بدی رخ نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20779" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOA4keGb9aVVwirohPmXwdCemJAeNWZovVHqD8hTOkvRgrHWqNp42hlznRw5UwC-aMwOnKXmC50KU-DYy-HwfzJ5FemHfdA60uEpdgT9uPMcs1bnubr33AzxU_AIYu9pngzPMWMmPgkq0n30-7kQpcrxADOD8Aqofyhc6RMKpn1iDn3fVY_gxJKghu20I3jnw3wR8v2Szddo9gkHkqTUKDh6_LHPepICwB_JpzCE2ASC3LqGpiTmFAshU6GVDn8OW2IiigbDgGKD5N83Ada9OwOsVE2BvUz49J6OQHvLiGB9KjmmFgDegBh77SYi1kveXR_ijSi447OSqcyE4W5y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20778" target="_blank">📅 22:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20777" target="_blank">📅 22:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7OqoJTqrYJStDGYWL4vX1TJ__KbWl-M0KUx3zA8GRFDRas6etQN28MwoXbZRhqCPUqPkcOwrHrtHJ11YVjD3CqR_TOwxpZcLsSqX9JSSVM87uEM_zT7jPjUR0qyDtgwKKvLl1YFGFssRw8ubqS5-xg5opXOSd9eTjYSZxi2mmsNHohsnU3WU0Iv5Ia6JYqAH0EqeND8RpV5Kfd3Hg8YyJkH6Pmv82AERWlQrksHJoWDQVfu2HGgVJyjfaOUbINQ44M65PAxxsJIBa-a8-FGFndtOBU5IAPFRAxWopxesmENsp6PHCvoWZ_SxlUzHibrTzwB4yEL6CmWKOHy2IUZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای پرمصرف (احتمالاً بمب‌افکن‌های بی-۵۲) به انگلستان و سپس خاورمیانه باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20776" target="_blank">📅 22:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏کانال ۱۳ اسرائیل گزارش داد که این کشور به آمریکا اعلام کرده به هدف قرار دادن نیروهای حماس که در حمله هفتم اکتبر مشارکت داشتند، ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20775" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=Za2ooU-u6EQQR_sk9RLQGrImOZADtMPVoG0g2THNxwr5-6jncdYtM_2mZtqnVfgk81KY7bOOAL5rWobvjTjKnGImAh1sU5wXf4WyA6AE4Xxa9ErgzETtOSO6dghXOjw3HoNpmRdZ8XIjInI7QUDRQEZiC7-eC82-1dtGHwAC0036tpcEotKSjCP9us_hdTvle7H_ZGuRa1cCRJO3TViSO_HYZGMXUB0dGDx5TTQ-x5wIQJqRb90lFGNCfJsxvfBpsd7pd6iyIKlxzLPo2-t2UHZA39lhd5TOCsb1RLW8uoo-S44ylkQNggcpdTcpu7LsrEnbs2wyCsYRVxIAZtCMSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=Za2ooU-u6EQQR_sk9RLQGrImOZADtMPVoG0g2THNxwr5-6jncdYtM_2mZtqnVfgk81KY7bOOAL5rWobvjTjKnGImAh1sU5wXf4WyA6AE4Xxa9ErgzETtOSO6dghXOjw3HoNpmRdZ8XIjInI7QUDRQEZiC7-eC82-1dtGHwAC0036tpcEotKSjCP9us_hdTvle7H_ZGuRa1cCRJO3TViSO_HYZGMXUB0dGDx5TTQ-x5wIQJqRb90lFGNCfJsxvfBpsd7pd6iyIKlxzLPo2-t2UHZA39lhd5TOCsb1RLW8uoo-S44ylkQNggcpdTcpu7LsrEnbs2wyCsYRVxIAZtCMSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل در کنار فرمانده سنتکام: "ماموریت ما این است که بر واقعیت تأثیر بگذاریم، نه اینکه تسلیم آن شویم."
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20774" target="_blank">📅 21:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20773" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جان بولتون : کناره‌گیری از رویارویی‌مان با ایران یک اشتباه است. ایالات متحده ضربات سنگینی به ساختار نظامی رژیم ایران وارد کرده و سال‌ها طول خواهد کشید تا آن را بازسازی کنند. صرفاً به این دلیل که نمی‌دانیم اهداف نهایی‌مان چیست، نباید با دادن یک پیروزی سیاسی به این رژیم، برتری بر تنگه هرمز را به آن ها واگذار کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20772" target="_blank">📅 20:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e884864.mp4?token=BU24txsH2kM8UA6pHIBq32bN_NBpx_06Gfxz6pyB4blLsCjIWy97TU33AmiPHT1YfW_T7Jo6F1j_z2ls6ysqM6UDbTsNevHGG4PGuc74UuJi_8KsX4yUa22t8e_gU2zwIn4kvBUlQJsWHUjM_wqDSXftKHNpIJ9g_XKlCSmZq21-I3mhYytAG2sqV6eUX_IPDFoFQe132z93QcCteQ6Hz5YxO01cyjaIsIWvhU07u8XXWlzILXl3GYR_nksOydjgQxZjaSqj6rFy9ASEFxS6Uhnlcshq-WYAblgfx3Z6uT8SuFhe4SMhf_W0ZgiEhlb1-ZsjuexBvxOgi0BB7TbJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e884864.mp4?token=BU24txsH2kM8UA6pHIBq32bN_NBpx_06Gfxz6pyB4blLsCjIWy97TU33AmiPHT1YfW_T7Jo6F1j_z2ls6ysqM6UDbTsNevHGG4PGuc74UuJi_8KsX4yUa22t8e_gU2zwIn4kvBUlQJsWHUjM_wqDSXftKHNpIJ9g_XKlCSmZq21-I3mhYytAG2sqV6eUX_IPDFoFQe132z93QcCteQ6Hz5YxO01cyjaIsIWvhU07u8XXWlzILXl3GYR_nksOydjgQxZjaSqj6rFy9ASEFxS6Uhnlcshq-WYAblgfx3Z6uT8SuFhe4SMhf_W0ZgiEhlb1-ZsjuexBvxOgi0BB7TbJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه مشترک چارلستون رسماً به پایگاه مشترک لیندسی گراهام تغییر نام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20771" target="_blank">📅 20:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrD-Wzw3VvgRmL4m80kANAoCvMDA3Gh5yguh0iGm4SD5Eb51gIL2-85KAYu9lUcIpIMKcU4hJJvn-ZJ2J0b8H97HtznL95Ct4P--hdJZUYYyrXfMbAOdiDEFmDVKmS0SuLi9qxFV4yPEcux1YbUlBUAqXYUmx4EAYEF82MLAtzFfFoY7jVqijoZyNlB44RLVr2JKZiaIpnb_bOh_ySjrHXMFShQrjQl602u_6fyk0FsT075E9TXCWbOfADizdSjLFAM0gBoi4cykeBvUMuKGCxYs44-odkS67q4B8WTJruMJ381iUE49xfdEg8uAbwm9yyyftT5NGSC1NykIAqz3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین موضوعی هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود! اما این ایده جالبی است، زیرا حالا من نیز از ایران درخواست غرامت می‌کنم؛ بابت تمام افرادی که با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که به آن‌ها شهرت دارد، کشته یا به‌شدت مجروح کرده است؛ اقداماتی که در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد. این شامل خانواده‌های کشته‌شدگان ناوشکن یو‌اس‌اس کول و هزاران نفر دیگر که در نبردها جان باختند نیز می‌شود. افزون بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه برسد به ۵۲ هزار نفری که در پنج ماه گذشته جان خود را از دست داده‌اند. به نمایندگان خود دستور داده‌ام که این موضوع را با قاطعیت در همه مذاکرات آینده مطرح کنند. از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20770" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مرندی ، مشاور تیم مذاکره کننده : جمهوری اسلامی آگاه است که نیروهای دولت ترامپ در خاورمیانه در حال آماده‌سازی برای یک حمله برق‌آسا هستند؛ حمله‌ای که ممکن است با همراهی نیروهای اسرائیلی انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20769" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">با حکم مجتبی خامنه ‌إی آی، علی عبداللهی فرمانده ستاد کل، احمد وحیدی به سرلشکری فرمانده کل سپاه، کیومرث حیدری جانشین رئیس ستاد کل، ایزدی جانشین فرماندهی سپاه، عظمایی فرمانده نیرو دریایی سپاه و طائب رئیس بسیج شد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20768" target="_blank">📅 19:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhMcK7Fgg6bghxZpubMPLVpXgD_VX3Pv7IX1fse5_BQ7IHY-llMQw_JQpmGKrTrFnFdjxM8_HF9ZHTv5CStesVUd3tS9GAUxDONDu6Mqd-ZZAaKwGCiNGRXnCun3SB54TeYXTVMort1O6_LyOD3S9LlRJQPLfX18PBKdHoUWezH5oqpleV2BOh5RhYE0KZSQsxccR3S6jni3ehDYcJMys8nw8JZt31ADkYfM4hFa4HzrnpUYwsUPg427p4DU62lKrlqbwlZmTQqB-yLC77bE5yFnc53Z4_c0RPn1H2JXzNynvbbw0g7FM70Va_MrRLRCSyRb8c0y_9x1z7ybYp5ulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : جمهوری اسلامی متوجه شده که با بالا نگهداشتن قیمت نفت، حمله قریب الوقوع آمریکا را به تأخیر میاندازد. امشب، ساعتی قبل از باز شدن مارکت، این حمله ها را انجام داد و هم اکنون با باز شدن مارکت، نفت در لحظه نگارش این متنالان حدود سه دلار گران…</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20767" target="_blank">📅 19:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHl3r-kFR-piaRfoAvwgqz4gTeSDGAxkRvvGtovr_bgy2j83MHOk4q6ktUdns3xkGcmZSF6cKubpwPCI4aURksxuRnXKDYJj71BHHxyzn1iuEoR5plWn7EMzGy02t-xOfZACZO-7jFvyuOGvcZ8JZ6gDall7SHMeYLxY3BNId1QTq8v5eFiDrWMT_ej7zvm4hr6QEhve-bxx5Ta4tMfyPmbdFLsRTM_s7EyOY_ZwIkCW35yjDtIRxa3s3ZxpZh6tgurNYT3Zw_qxzDL-8kV0vv8cddBvEW28OFpHGbeGu_tCyE8iyRoygx_tg6ix6_rwQMPxmuRPEiZIR6jYWu1rjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : عاملان کشتار جمعی اکنون کنترل ساختار نظامی و امنیتی ایران را در دست دارند.
ایران به‌تازگی قدرت را به‌طور کامل در اختیار دو فرد تحت تعقیب اینترپل قرار داده است. محسن رضایی اکنون با اختیاراتی هم‌تراز با رئیس‌جمهور، ریاست شورای عالی امنیت ملی را بر عهده دارد و احمد وحیدی نیز با اختیاراتی در سطح رهبر جمهوری اسلامی، فرماندهی سپاه پاسداران را در دست گرفته است. هر دوی آن‌ها به دلیل نقش ادعایی در طراحی و سازماندهی بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در آرژانتین، تحت اعلان قرمز اینترپل قرار دارند
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20766" target="_blank">📅 15:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وای نت : ‎نتانیاهو قصد دارد انتخابات 27 اکتبر کنست اسرائیل را تحت تأثیر حمله جدید به ایران قرار دهد تا ائتلاف لیکود متلاشی نشود
گزارش ynet می‌گوید نتانیاهو در شرایطی قرار گرفته که
تهدید ایران و بقای سیاسی شخصی‌اش عملاً به هم گره خورده‌اند
؛ زیرا اگر بدون یک دستاورد بزرگ وارد انتخابات شود، فرسایش قدرت نظامی و نبود موفقیت سیاسی می‌تواند برای اردوگاه او هزینه انتخاباتی سنگینی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20765" target="_blank">📅 12:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPKXBvaCMMTFlZxrQPfBOQomSo8delWU-6h-w5uqYRfTbRvqK1eL_zwYS9Wk3kWqmbJZ0yRyCqa1xFdN5PQWKGeXnGHWQHcUYIfKwVXkLyXA8oTgfrO-eUUWIwIhQI0dXaeFdKioYeCDOSw0FqV16AKUE5XLzQB0F0dIV_L2QYx3GHq9hyRnD6-rUoCDTnJtAkMbILyNFD2_W3r0PivwpKErgzBq0TgVFcTEk5qfl_2BRg9sJ1N9HgM2yotU46FxtDBuAzx12R08OKKZ_-8qjeL-8ADsJdQZ3Gs83cqKqYEl9K65KJYgjEvSdRUlbXpScBJABx6VvGRDhOsj5jK1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود بوتاکس در جلسه دیروز مجمع تشخیص مصلحت نظام
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20764" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقام ارشد به کانال 14 اسرائیل: بزرگترین ترس دشمنان ما این است که نتانیاهو در قدرت باقی بماند.
خب،این به چه معناست؟
نتیجه بگیرید.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20763" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مجید شاکری ،مشاور قالیباف :  ترامپ با ما توافق نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20762" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">باراک راوید ، آکسیوس : یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «نگران یا ناراحت نیست» و آن را بخشی از فضای رقابت‌های انتخاباتی در اسرائیل می‌داند.
این مقام آمریکایی گفت: ما نیازهای سیاسی بیبی را درک می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20761" target="_blank">📅 10:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMkQMbmudxqUJI-ODWLl0z0sgBx70XEmJb3PsI0d0r9GPpd478YJI8beSVeDiDwL6v__QRPAU0x_1LsLeCCG0QI6uroYaWCsvfefOXAVzpi1TR699V7i9rtqCN08ncaEKYN8esCB7jQfq1jI_py90TvtJPY6MCIGjsBYQXww8oiuNwTSs8MpkttJwlvJCIxt45s1sohAaKckLR9vThxoARNUFMTDmRIA3uFukuYk0lHzu9gamyP1HkLG8Tw-XpWD0dkL6FMYPHyaqzWgrDjaZIuXFF3CPONGImkmXh3NFzFj7aV4wzqAvOcPc-7OgbKauIIxRhnBWdUW8p4LiYOLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیز نیست، بی بی داره خنثی سازی و بازکردن ورودی های تونل ها رو براشون انجام میده.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20760" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">مهم نیست داش یاشار مهمات عمل نکرده دوران هخامنشیان هست</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20759" target="_blank">📅 09:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-psOaV9mbvDAKh9cQTvH4JMh6M3QP7XA43hljp84uVHL92lLcoLNg26o5t-BUFlCqw3Z_RuudD6McSBmNCKWLc3NRcdoCr05svDoobh_UF_3E65t90eyHo3RhAud8jnwTcQ_MvbIhQH1Wq1JvWxwwn3mrqWdiegvlP3kMCaZYTRDJCwE4BbOOTvmwjpdBWCY618N295PPHnhNo2RKgKAkUEzY1lEY20ECmKzmGHJgxPfC5G_MlHwgmO2q5idM1luc93Xup6kXzWVFhSeLtlbR4Aqrlt9VR-W8OH0f6KerYu1aGiIFmwtf52X4uFkEs98G16Gmzt7N1LZsjeGMKE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان سمت پادگان ۱۵ خرداد انفجار جدید
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20758" target="_blank">📅 09:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqR7tXL9K2A8JbOJ9zLO6efgfsm3vSKQHTaxGLKs59fgHsQmwWv8m-8bfAFjk5vZMQwXOD7d2UuVJdQQCBUizKvBozNxoX8PDrQi_zb_vlXxsk5N3T95FOOpmHGPd9lqBdy0U6gjvN-2o2g4KCUniBL6pVlR87G3h_7mGXipD4xxT9jnzl51EknSnii0QjtlhlLQPPtMBD_6xVnk9BmIUeCOmF9pQZR3dYysOEgZigNKjFhaHrqAyCeMXzp92bgk814h51DOBEw7ZnIHbJNXBufYPrAjGnD9Cco7KLOxo4FagmwnJXjcPkiOgGLBl0JGl50U9zMZsYw3AsLCi__LJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار شدید در اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20757" target="_blank">📅 09:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAsXGVDz6c1LUEfPbFwF5gx1fZFkw2w2P1KZ5pT2rtzRlA2V1C_xn8zGLbCyfujy376dZCf-Wo-6SVQcjgiquKB3YxaSgnVqi2gm7k5iN7z51VQZIhwsSjvuWF7gJyMXzVmv_SORFRLhx5SLxlRkGEDUjyuJTYfeYCsc5kLbVEpHR0dtUooUV6LtmXvtuNMeoaLEuE3Q1ckRJeinBks_1iyhbeZlFjwrb23m3kS0oqyn_j23zha_dl6SE-4u1W-xkRvAROI5KrjhRdCPhnGZUxEp2scaZB_v3oqyHxkTEJtIRwh5BZHttkZwoWVCc8uVe99ejDo-QDBaIq-jSRhQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد.
این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این بزرگ‌ترین زیردریایی ساخته‌شده در آلمان از زمان پایان جنگ جهانی دوم به شمار می‌رود و به جدیدترین موشکها مجهز است
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20756" target="_blank">📅 09:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468b68072.mp4?token=aXqbGPTgJdJYuI7iv5UJbeLSrxpMDrpu75IfsKsp01QWiGG6-SQ9rq_gRcPnghnk9KXuF4VUPw7vX4FQFmHj2MuHAa-6DKdZyHTGT6_P7MIK0opZPd9VWjLv9lEY-oprDfLwuVPrXqSfnRbyXj1UJf3FKvJ377s6ovLcPmEVq8AQezXgXjy5nZ5WKuJh5VDIW6NmJhwj48Wc765enwbkRu-_Z0HVh7xfzBIGoe06iCACjLWzhw-ZFvXCdC8f7w3k41IayvEFzssLsHwGPx42E7gVqq-OBpqCnxWF1YkuTivKUkW353SSBrURKi26V8k9OQygGr1uBq1_5vfXWK2e6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468b68072.mp4?token=aXqbGPTgJdJYuI7iv5UJbeLSrxpMDrpu75IfsKsp01QWiGG6-SQ9rq_gRcPnghnk9KXuF4VUPw7vX4FQFmHj2MuHAa-6DKdZyHTGT6_P7MIK0opZPd9VWjLv9lEY-oprDfLwuVPrXqSfnRbyXj1UJf3FKvJ377s6ovLcPmEVq8AQezXgXjy5nZ5WKuJh5VDIW6NmJhwj48Wc765enwbkRu-_Z0HVh7xfzBIGoe06iCACjLWzhw-ZFvXCdC8f7w3k41IayvEFzssLsHwGPx42E7gVqq-OBpqCnxWF1YkuTivKUkW353SSBrURKi26V8k9OQygGr1uBq1_5vfXWK2e6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در واشنگتن دی سی، در پایگاه اندروز فرود آمد و مصاحبه ای‌ نکرد که به نظر من بازی با رسانه هاست تا در خبر های‌ زرد و دروغین خود غلت بزنند تا غافلگیر شوند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20755" target="_blank">📅 02:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbyT6763zswtvq6Pnc40ej_YPKrXGr0nAsTxfzSLnjLBL6IzyCFxD3lHR89B8FsC-RXZFpfW7WJCp6CduP_MXCt8sba-M7Gbv_MgUbO34ossheztzyk8LWUDllNeZBK9Nrd2QJF5Qs3TDcYehMU0gLJsNhP_A7MH0ers69m4mHdBts3jQ_l66WewGSg_x5og6jFe4IEWc96QDUzG8K7gTyriri9EcrdHjANcpxBV10NQl0B0zSlqUtwaV2yZdYGDm0BSf7b88I4MdmnL5QoPeWvMoSsWUxcSLDijR7DJog3MeKDwwhedV7Cvcukhx4r6zRl72WMUFGt0-SicT3vgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20754" target="_blank">📅 01:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی پهپاد به سمت جنوب ایران پرتاب کردند که پهپاد سعودی توسط سپاه رهگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20753" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bItmNcoP8VVDdp93iVBjWZ-f2aAWingtzGjZLyw2Ogv8zzOGUb0hNQMe5bD2Csvcz9Mt2nOiWPfXpYr7toGPOFFktnPt1chN9ku3zcUt3IiUlHpH1j6knCwDHJdszGjbYAyeYtDmy5qzxZFfVg2rdupxem2ubfuZW4iR4piIpfvvQ-CzCz59jWCiWREhHQ7JDn2d1lcVmueisiRky0DFkPJU4AIMgKyZQEVHnqHmFOwvhN_1FbkYJ0oOSMgaWTvKV83ZKzWD2epbAYRz5M4KuvHkwe6TmOjryMo09awcBK7XzoyyXKAmjMVRs1y4MP6rxJ0Nq2tydgAAYaR-9lXhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام :
ملوانان نیروی دریایی آمریکا
بر روی پل فرماندهی ناوشکن
USS Ross (DDG-71)
در حال نگهبانی هستند. «راس» یکی از بیش از
۲۰ ناو جنگی آمریکا
است که برای پشتیبانی از مأموریت‌های نظامی در خاورمیانه مستقر شده‌اند؛ از جمله اجرای سخت‌گیرانه
محاصره دریایی آمریکا علیه ایران
. ما، تا
۱۸ مرداد ۱۴۰۵
(برابر با
۹ اوت ۲۰۲۶
) نیروهای آمریکایی
۵۵ کشتی تجاری
را تغییر مسیر دادهایم،
۲ شناور
را از کار انداخته‌ و برای اطمینان از اجرای این محدودیت‌ها،
۲ کشتی دیگر
را نیز مورد بازرسی و سوار شدن نیروهای نظامی قرار داده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20752" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بلومبرگ: توافق هرمز همچنان دور از دسترس است، با توجه به اینکه ایران از مذاکرات مستقیم با آمریکا امتناع می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20751" target="_blank">📅 01:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20750" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">روزنامه کیهان : اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20749" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=r-EAMudFjgMsO5Q2YEqWFIOfbvAnZUwQhkhDgHQiMQIKsEVnGMILvlbUbEzFFqJGNVlLnKxXskEaK1nTUo2x0kOm2JGGpzLFACZgpodkdO2rokMDFP_EDTfFzLBcAv7QSqf5GVq7PfzjtPAlI6A6BJ_uBmL0UhBwFtrXStakKt6PP7ybNXXgtY12ugXPtAFp_Xjr3212uZ8mruHSGJYwOh30YfD9J3bWFg-v0Irl3RgcWXW65-7dbUzhzVu5jEiSJ4zdQeFyE3yb3ozdb_FOTgVmMf1f5Wts_bCLnrx4Y4InB86yw26yoQYIatHKAQe1RsMtH35dfpiPWwQha_Bz5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=r-EAMudFjgMsO5Q2YEqWFIOfbvAnZUwQhkhDgHQiMQIKsEVnGMILvlbUbEzFFqJGNVlLnKxXskEaK1nTUo2x0kOm2JGGpzLFACZgpodkdO2rokMDFP_EDTfFzLBcAv7QSqf5GVq7PfzjtPAlI6A6BJ_uBmL0UhBwFtrXStakKt6PP7ybNXXgtY12ugXPtAFp_Xjr3212uZ8mruHSGJYwOh30YfD9J3bWFg-v0Irl3RgcWXW65-7dbUzhzVu5jEiSJ4zdQeFyE3yb3ozdb_FOTgVmMf1f5Wts_bCLnrx4Y4InB86yw26yoQYIatHKAQe1RsMtH35dfpiPWwQha_Bz5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پهپاد ساخت چین که توسط نیروی هوایی سلطنتی عربستان هدایت می‌شد، در سیریک، استان هرمزگان، ایران سرنگون شد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20748" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بازهم صدای انفجار/پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20747" target="_blank">📅 00:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwPLpi35TFE9ss_x3PoKFDlmrgGn35TmDj-g8rjEAKAEJ_7AYexbV_PtNN_p9W4pz9onULV4dA4oUG2GLcvFSEKicHOx8H8lZJZIKVfJSsPk2toQMCeP2b1SJHZQ8qJLk7wZkIBHXfdn6eD3asLEvNOSEBG3xx_AidklgETYdE_c5xoHYshw3Dw71p9SjNmISZs8btSWXSkTJytiK7tPqSnQ5vrNriQwMhitdJ5Js72US9-E749JqMLOzhG2Qz2ppgBysV-eTzJSdYFfMtMtLVmnJGBTSDp71hUv4UAnL1tsLVxiEqzDfUfL7xdSAKB2Ecqy-rSzvzduXuofIU503A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث
: 51 سال رفتار نامناسب ایران!
@WarRoom
حالا چرا ۵۱ !؟ ۴ سال آخر شاهنشاهی هم قبول نداشته ؟!</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20746" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=N2PduvbZBrm8lncLTvjGMQaSfQWPJt_99iUB9Zh1l3khaBscYzxkkHo_v6TFjFns_GoKh9vHLk2_T5PbR7ad3M-tislhsuWOtdnp3HdDPuEvSMZapGZs658_2TEhX5y987viMFeqx17IOj8tSb2ocVBNKZRvnnoqXZlNAyNVDux7alBT1u9iN-r5EBpr5yU3gOJe_jEY0lPFqskYSpecWtxTSLwD1-wj6tsYnvWCHaxhtAYibEsp1ypwQ6kR9S814NUsCsaDWnyka4t9DdOD3Qr7Gf9JOsKeS68yddd8hHMio6ZU7mgUUAUiS9LIjRi5pJAxmG6RO8bf5zFInRP63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=N2PduvbZBrm8lncLTvjGMQaSfQWPJt_99iUB9Zh1l3khaBscYzxkkHo_v6TFjFns_GoKh9vHLk2_T5PbR7ad3M-tislhsuWOtdnp3HdDPuEvSMZapGZs658_2TEhX5y987viMFeqx17IOj8tSb2ocVBNKZRvnnoqXZlNAyNVDux7alBT1u9iN-r5EBpr5yU3gOJe_jEY0lPFqskYSpecWtxTSLwD1-wj6tsYnvWCHaxhtAYibEsp1ypwQ6kR9S814NUsCsaDWnyka4t9DdOD3Qr7Gf9JOsKeS68yddd8hHMio6ZU7mgUUAUiS9LIjRi5pJAxmG6RO8bf5zFInRP63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20745" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20744" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20743">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوباره از سیریک موشک ول کردن سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20743" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20742">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJuF8D-tK9iMFjiuNm4enrBQXSTBiiDO_zR0wTwDcptJpRweD8NBxqM6rKRwlEgUOApnVAc0w0Lg5u3SY5irG56l-_bexE6lOUAJloKMTXU4Xlt6rIIGfF5do7c4SZn3e1dQFJ-C0w9migEdn6Sc3TRIiuPWaKhNJLj0lmGzAEorGGdV1DeNB_EtQEr3o-0DcHnkZekL2dtoNVmCjDS00pZYdrboJ51eznvAKSKKwLElXPTR6WDoxMIzdvoEaPtEZPrIpO9vzKY1lB-2dUEMkLBWnrkDBTewC4OvWi8DT-z-Gc2-muoBiEN_W-X1ALINp-ZRTa4ZWLJjZhAyTeWPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک :
یه نفتکش میخواست از مسیر جنوبی
عمان عبور کنه مورد حمله قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20742" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک @WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20741" target="_blank">📅 00:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=kQTbMc7OgJlSSeLrjviPd_L34OOhRqcajzkDgPPzHfGFDesE9NA9Nv06d0H4x63XzgYkOS_y-HqZiWnPxn0FplVDZIJ38wJBQu453hfxWBd3Yi8PTFEbLO4Ixm9e2DkQ-hMxhu3NudneE_oJoo0cN7TZsqLJpmfGeKU2lUWpRCrm-5Z4AImMV0qQjUotwX6CNGI_HcUtEIyPAva11St1Vxv0x7VS9vk7jDfSBXRFU8VyT9qcpLGQ0PqjKP4CV49py3F7XygwMsvyKMCxzTrko8sw7NCIel3xRGn2LdwWB3FM21dErcukQ9vVDWqHZqKoKA1piozfAGazK6zQ-FeC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=kQTbMc7OgJlSSeLrjviPd_L34OOhRqcajzkDgPPzHfGFDesE9NA9Nv06d0H4x63XzgYkOS_y-HqZiWnPxn0FplVDZIJ38wJBQu453hfxWBd3Yi8PTFEbLO4Ixm9e2DkQ-hMxhu3NudneE_oJoo0cN7TZsqLJpmfGeKU2lUWpRCrm-5Z4AImMV0qQjUotwX6CNGI_HcUtEIyPAva11St1Vxv0x7VS9vk7jDfSBXRFU8VyT9qcpLGQ0PqjKP4CV49py3F7XygwMsvyKMCxzTrko8sw7NCIel3xRGn2LdwWB3FM21dErcukQ9vVDWqHZqKoKA1piozfAGazK6zQ-FeC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
نیوجرسی را ترک کرد و جواب خبرنگاران رو هم نداد، تا ساعاتی دیگه میره دم توالت شروع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20740" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شبکه i24 NEWS: اسرائیل فاش کرد که رهبر حماس، "باسل صالیه" را از دو سال پیش بازداشت کرده است. این خبر پس از دستگیری او در شهر حمد منتشر شد. این گزارش حاکی است که او پیش از این با سنوار و الضیف اختلافاتی داشته است. اسرائیل او را مسئول شلیک موشک کورنیت به یک اتوبوس در سال ۲۰۱۱ می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20739" target="_blank">📅 00:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZqIXSRJ_mUWRSeHbL0GuHTCeR4XwvDaZr1ErGegWveEv8q57qPL63Z6w3Q5spwov15ubMJQmn2CdN_zz8Er3ntlExQ1KUMiSBCYkKYzg7zLbqQiAhcBQj_u2X4coL4brNug4djOcooJEfKas4ZZ9R_SjlAr8fNf3_50wcEvEKfgwz9YnabkZdm0djV_WxOziNgrg2LB9LjO83lhEwHUNP0rxatz2LDZqK2B6D9W0Y9myT06_CxETIoK-p59p9ADQLYTISvUJNLmJx0KpGTSj7AApRKxRpZuAcM0ksnFQPAhKW-jq5GArifb6EYBhJubXXLRvXgIdm0oOFRh9-kV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت پیشرفته‌ترین نسخه عملیاتی خانواده E3-Sentry (آواکس)  بوئینگ E-3G Block 40/45  از پایگاه رامشتاین آلمان به سمت منطقه خاورمیانه،
با مشخصات :
قوی‌ترین ارتقای انجام‌شده روی E-3.
رایانه‌ها و نرم‌افزارهای مأموریتی کاملاً نوسازی شده‌اند.
توان پردازش اهداف بسیار بیشتر از مدل‌های قدیمی.
لینک‌های داده و ارتباطات پیشرفته‌تر
و موارد بکلی سری بسیار زیاد انجام شده
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20738" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20737" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=QuCejPfpTErdoCzsjfw8dp0Ndd-LMjDXkic82jqLadaS13OaluTQ-KGc-dgRYao3B_XegshIt8o-S1pnFkxPGZpepKSk3-E0apFcxswGwzAGK4Pi6eRzDvCGMS7NgT1-Jj9feztblmjMGM23aaGY0HDNYehHCQHkK8zhY47Qa6YALT_B3Vz5clfIZkPdYf4GzQBykiQPqIaElGC6f0L04jvZzGulKsFIXT9axuqTDk6BsfXX1Sg_XcCvGnD1KnE_gnF1S1FhmhCcLoUh5--rOkuLyCGqL8yuu4n8FD6aZ-ALZv6jRmAPCnLjkiHvVUUE4bKyAm6g4Hy7wnKpQgs2wyNIQuOhIRvul73BmDKAku-QV9LqQzL6KB2Hgakncd-kxVVe0DVHyaIme5zgrxGOCr7R3ShpEqgTm5lIcvNtnmK9HAs6VVJRBvZ_zukCXMzfrAmthw0WBV0lLb911Lgb_K8rC--vRPDhzI51Cohb4qeqyc4XLc5GfEPmULmmFjC6jGblLog2Gl4D1dvyuc4wSep__3zdi5HzHKYJgBFQDzttoaPuHFpD_prS6dU25dfLuHP5QotQSpkQpfwQIDHsmsyCWU1G9NfbK8HA952sjM8Brub4Mw6r5hrqQ1IpokRRtzp2McfaHEwkN6iCMVbXQpV_I8VrCBP73e3AeqEy4EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=QuCejPfpTErdoCzsjfw8dp0Ndd-LMjDXkic82jqLadaS13OaluTQ-KGc-dgRYao3B_XegshIt8o-S1pnFkxPGZpepKSk3-E0apFcxswGwzAGK4Pi6eRzDvCGMS7NgT1-Jj9feztblmjMGM23aaGY0HDNYehHCQHkK8zhY47Qa6YALT_B3Vz5clfIZkPdYf4GzQBykiQPqIaElGC6f0L04jvZzGulKsFIXT9axuqTDk6BsfXX1Sg_XcCvGnD1KnE_gnF1S1FhmhCcLoUh5--rOkuLyCGqL8yuu4n8FD6aZ-ALZv6jRmAPCnLjkiHvVUUE4bKyAm6g4Hy7wnKpQgs2wyNIQuOhIRvul73BmDKAku-QV9LqQzL6KB2Hgakncd-kxVVe0DVHyaIme5zgrxGOCr7R3ShpEqgTm5lIcvNtnmK9HAs6VVJRBvZ_zukCXMzfrAmthw0WBV0lLb911Lgb_K8rC--vRPDhzI51Cohb4qeqyc4XLc5GfEPmULmmFjC6jGblLog2Gl4D1dvyuc4wSep__3zdi5HzHKYJgBFQDzttoaPuHFpD_prS6dU25dfLuHP5QotQSpkQpfwQIDHsmsyCWU1G9NfbK8HA952sjM8Brub4Mw6r5hrqQ1IpokRRtzp2McfaHEwkN6iCMVbXQpV_I8VrCBP73e3AeqEy4EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) اعلام کرد که جنگنده‌های اف-۱۶ این فرماندهی، چند هواپیما را در نزدیکی باشگاه گلف ترامپ در بدمینسترِ ایالت نیوجرسی رهگیری کردند؛ زیرا این هواپیماها بنا بر گزارش‌ها، محدودیت موقت پرواز اعمال‌شده بر فراز آن منطقه را نقض کرده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20736" target="_blank">📅 23:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۳ : اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20735" target="_blank">📅 23:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به گزارش اکسیوس، توافقی برای کنترل عبور و مرور از تنگه هرمز بین ایران، عمان و ایالات متحده مورد مذاکره قرار گرفته، اما چندین روز است که در حالت تعلیق مانده است.
مقامات آمریکایی می‌گویند اختلافات فزاینده‌ای در درون رهبری ایران وجود دارد. گفته می‌شود یک ساید به رهبری رئیس جمهور مسعود پزشکیان، به طور فزاینده‌ای نگران فروپاشی اقتصادی احتمالی است و معتقد است که تهران به توافقی با واشنگتن نیاز دارد. ساید دیگر به رهبری فرمانده سپاه احمد وحیدی، با امتیاز دادن به ایالات متحده مخالف است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20734" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دونالد ترامپ، به آکسیوس گفت که ایالات متحده در قبال ایران «فعلاً با سر و صدای کمی پیش می‌رود»؛ اظهارنظری که نشان می‌دهد واشنگتن اجازه می‌دهد فشار اقتصادی افزایش پیدا کند.
ترامپ گفت: «ما فقط به‌صورت نیم‌بند با آنها مذاکره می‌کنیم. ما فقط داریم ایران را زیر نظر می‌گیریم؛ با این تورم شدید و این واقعیت که پولی ندارد.» او با اشاره به وضعیت اقتصادی ایران مدعی شد که این کشور «در شرایط بسیار بدی» قرار دارد و در پرداخت حقوق نیروهایش با مشکل روبه‌رو است؛ آن هم در شرایطی که محاصره دریایی آمریکا فشارها بر ایران را افزایش داده است.
ترامپ درباره رویارویی با تهران گفت: «همه‌چیز درست خواهد شد. همیشه درست می‌شود. این مثل یک بازی شطرنج است.»
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20733" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20732" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv2XAh8njzf8k7hEVQGSO95llA3jQ-oDlbClD8ZnAhjwRn5hzH7OR3elbFw0DKARQS5hcGEbmJQMiY2FQPeXoYiyvAYpx8z1F5Yy-hrBP1fOwFDt6OlAzKOaPu2x-UEIRMDSp_4zcvZmElXpmwHWfQhRWHxSPO61MxOkWxSr-Hz9lH7bY-MyEc6wyGs5gfAhung-HkxfGOqiWF5KKG79iyGEabBWyJwDPS6eE7fwmD6_YyKgtm_x0lHCqMkAVEUIX6X01kbD8wMD0dAydEaUCDVwVNcjFhS1ibyJHoIFmuImfrQLb7OS2Qw2-KE7Bc4tVk8CelPQ-JtovPyxqmojYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : جت‌های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت‌زنی می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20731" target="_blank">📅 19:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20730">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حسن قشقاوی، سخنگوی کمسیون امنیت ملی مجلس، اعلام کرد کلیات طرح «اقدام راهبردی تامین امنیت و پیشرفت تنگه هرمز»، با اجماع همه اعضای کمیسیون حاضر در جلسه به تصویب رسیده است.
- کنترل بسیار بیشتری بر تردد کشتی‌ها در تنگه هرمز اعمال کند.
- برای برخی کشورها یا محموله‌ها محدودیت یا ممنوعیت ایجاد کند.
- برای عبور کشتی‌ها نظام مجوز و در برخی موارد تعرفه یا عوارض در نظر بگیرد.
- از تنگه هرمز به‌عنوان یک ابزار فشار سیاسی و امنیتی استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20730" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20729" target="_blank">📅 18:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=tg9haB45_RsRth6jxR9mFLJJDYNnAdVOAkFDDvatncivY3qY0QVMhBpqixn2RzNiz_-7a4axs-rGZdOuVp2jTkEDh1hMnq4VRYnoujVU4s7_cvUzNL_6_N0lytW-o3rLblRBkmsJY_M0bGX583jyeL26L2XLweU-tdM1zv-FzVIVYIM4XIodTSRaN8r9sN7jCANQh2dd-RMrb9lOahXqJMEY-NXwfQ9Nx8YlXV1hQICLGhU0rr8nYawPo2RUBk30IHyiKhMGu8C5C1Mcy7hZEXrg9cC9NQoTCT5PmJfFsUh8JwP8D59e95DwLMNAMcOpbyYmrrnCTG_QShMmeDGam73yQvTBOPHpbY9zCzgdmKHtjrbiyZQ9aucDQPZuv6jdKBuE3OCnTPs6LJRJz01SyeToKKid3D2d4SVFjamkUxt6xCVU6uKEJAGzfE0uC0lgfN4ebpbauqJPyyuIaz4IC0WuoEawU6PbpK3IHqDP69LDyJ7ybG3qzFbcIRyNmvdFA9eLY7rvmuqR069SXDDy-q8CaCCkzasKoNYYcoi75TCJC8rmU8pTD6fypYvYPct0qPg6riYrgCHKryM19Zxs9y65xI3ZwKegbIFL8gwKVVrp2LMv9ydWNrC4A0_PCu2JYBz_svJoINsRR2zYF-c6i96ACv2iOMYyQ7coiL7bj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=tg9haB45_RsRth6jxR9mFLJJDYNnAdVOAkFDDvatncivY3qY0QVMhBpqixn2RzNiz_-7a4axs-rGZdOuVp2jTkEDh1hMnq4VRYnoujVU4s7_cvUzNL_6_N0lytW-o3rLblRBkmsJY_M0bGX583jyeL26L2XLweU-tdM1zv-FzVIVYIM4XIodTSRaN8r9sN7jCANQh2dd-RMrb9lOahXqJMEY-NXwfQ9Nx8YlXV1hQICLGhU0rr8nYawPo2RUBk30IHyiKhMGu8C5C1Mcy7hZEXrg9cC9NQoTCT5PmJfFsUh8JwP8D59e95DwLMNAMcOpbyYmrrnCTG_QShMmeDGam73yQvTBOPHpbY9zCzgdmKHtjrbiyZQ9aucDQPZuv6jdKBuE3OCnTPs6LJRJz01SyeToKKid3D2d4SVFjamkUxt6xCVU6uKEJAGzfE0uC0lgfN4ebpbauqJPyyuIaz4IC0WuoEawU6PbpK3IHqDP69LDyJ7ybG3qzFbcIRyNmvdFA9eLY7rvmuqR069SXDDy-q8CaCCkzasKoNYYcoi75TCJC8rmU8pTD6fypYvYPct0qPg6riYrgCHKryM19Zxs9y65xI3ZwKegbIFL8gwKVVrp2LMv9ydWNrC4A0_PCu2JYBz_svJoINsRR2zYF-c6i96ACv2iOMYyQ7coiL7bj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز آپدیت آخرین تحولات تا دقایقی پیش…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20728" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYmB_uvNiA2vWS59zwuKG_vhvNiYhWfIDFMK9ISPYnXivYBnJYnBV8NvPhg4lLZosq8JzMrOw4ilIFBW2k7KYgpjiIujPj2jfjxXg2Bj7iPj7VX91PmARiUEsmZ2epZqpUYdpH20Rr7BvCV9xkEnOu5wCB6ipTht_OSIRtUIRPPsnmUDU4JMqEtZHkkRJ_c2PTqUbnPMaMG3I5sMZy15f8wA1EWdO35YU5wvkNIQ3Td-dQhxmi8rzS_C7CAY5yNXzEGQflpVC6OuNPoSHm1C49Lhq573SmgYG8-3KLWjYmf8P5yMzGr8O8wE6aw7p8uA0hEf0hTz8ciuuseIKwtrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود و صدای انفجار در اصفهان
چیزی نیست بی بی داره خنثی میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20727" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77914048f8.mp4?token=NmNkkCt5dnZqqnmZxx1imaBLQUpqZ7K_1cbJLmj-XNqTrlm2JtVdTK_9K6wWj2VvKEFaPGvwJttju4qWduJTpsDcyQHd9acLvEpi4aMuGBFP_A2YDB4EFs2P9JEy09tI6NsIuN4H_E-MNsXUWTzTqzKWciKbJOM8V49h-h2Enq3jkL6FxBj-OMl-4xOCSV691Te_X60A2lhzQeQOR1mNti3AFCeBWLBHNjXF78F9rT5LwV462VZzP7KDcEGmrzS0B2nK8lJgaQLpqPCvMTZ8fMO0BqHnbt36vdtASgtEXJOu1y39bjC8PR4DwNu4UJ6U0itCUaMQdNz0JYACCA_rmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77914048f8.mp4?token=NmNkkCt5dnZqqnmZxx1imaBLQUpqZ7K_1cbJLmj-XNqTrlm2JtVdTK_9K6wWj2VvKEFaPGvwJttju4qWduJTpsDcyQHd9acLvEpi4aMuGBFP_A2YDB4EFs2P9JEy09tI6NsIuN4H_E-MNsXUWTzTqzKWciKbJOM8V49h-h2Enq3jkL6FxBj-OMl-4xOCSV691Te_X60A2lhzQeQOR1mNti3AFCeBWLBHNjXF78F9rT5LwV462VZzP7KDcEGmrzS0B2nK8lJgaQLpqPCvMTZ8fMO0BqHnbt36vdtASgtEXJOu1y39bjC8PR4DwNu4UJ6U0itCUaMQdNz0JYACCA_rmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی با جمع‌آوری ویدیوهای تیک تاک از آهنگی در وصف پهلوی یک دابسمش منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20726" target="_blank">📅 17:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD0q0F03H1R7UCIkIw-5xEpSajzm9laCgT3FhY3jrrr-_J_XOEqZV9IHWS09X5FsGrs9MyJK_2dMcV_nbGvWOeUF5laOZAzRDo4u84DHl2v5DBIFU6xU_B1o1mNOAysLEBrzKf-hm6d8f_YpFnJNXjcmF3KFY99XiO4GnEef_k7X1fbESc3RpON0skDpx2i_EjUYCfv_RFxNtrWb3OFQDlqboLI666nvpXdNLuOG_8ZYvq2TT6i-0YNJrg528GFchJn9FUdATzKKEvI6JjQ_bN9pysDTfpShE8JqJi7tywiXupj3HMlP-atI4DWh7TrmTat-5ZRPTO1xlzvZ87-3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین با خطاب قرار دادن عراقچی به دولت آمریکا : این بیشرف می‌گوید هیچ مذاکره‌ای در کار نیست
یاشار: منظورش اینه بفرما این عراقچی بیشرف هم میگه مذاکره ای در کار نیست کار رو تمام کنید
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20725" target="_blank">📅 17:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یکی از معاونان نیروی شبه‌نظامی بسیج ایران ادعا کرد که تصاویری که مجتبی خامنه‌ای، رهبر ایران، را در میان مردم و در خیابان‌ها نشان می‌دهد، در آینده منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20724" target="_blank">📅 16:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyH-MOZnh7wJnH_n2P-HybMGyBG77JYVmQ1HzwRRKF6VJp4OKM7boWVOZoJ9SGg4BvaTob7TAxAg74OMtkPV5R4VpC6QW0lyL7gyNYvyQvQAcXQHjfTW2GmRzlWb2Bf855g7uP4heIv8cgc8bejErr0ebY7mTbtjsTEXw6WjPzR4ggM4d7ebnsfn47attyWF6rW_wPiM-QL5PBwtcoSoqJSqJvgF1uPioV_H8yLADKRW9Bd_584-ZBq_WpNfz-ymXRfV7v55AYjYQ1ylYZ0FpgXO7dDrPxnz5arHIlw-TMERkpqHBOl4s87cXn_yz5CPJwuUhvCC1dRfOllaRYYw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هر روز پیجو میززن و برمیگردونم
پیج اصلی :
instagram.com/yashar
پیج دوم : ‏
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20723" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=ATrqLRvqKEW-IIE_D9EGoB-HuzIBC-PqRtW9MnkyJve1bVSkXvcxvyvrtwAPD4jwVi_IeuMZu7ahZ3kmetpnvEdhKxn-Z_YLMuXHIk4KrIVeflVJnrzRH9QDB7_38ESKM7g35sCQQB8PkSbBXL8C8tmAr3GxGs1SFCH9SVOIUkUSosyHGcDUFfHLaNNehTn_3vKuvd7OW9F54j-VGCmFFHq-nDcKkpckD0d2jG1c8eEOM9LXBQozetR7l2d4FEnPkv7X5xfToaz-Rc-bWmzhTe51-TJ0bSAiy_wH6i2x1yDmbOgEmuUn5LuYn53gVh6TfVKEjuv6fleC2Ej0Q6vm9mrTy4gA3CF-J094dxgtTxtSq37yjoqAtbTeC6MO46RfBtJR1lBOoYEu-GuQDjYn3B19Qx2Tda_F-RXTfGNdWcfKoejT8F5J-bJnr2KNIPAN6O5jEhuQHXFMG_qpedOaBzBiajcb37ZpVEYAuatoNJmfYkOo9M2OjR-E7TfgzSMim1Y3_V7NclB1Ie4UgYdILRkrUmTcG2mD8PFzA0RHRRXDEIIdVUTkol3KjzqHNKLE25vFOxkidtBfTytq6re9cYWX2Jj-i1qBVngflBpS1cleCNiZY6ZulG-TlPTcbCly_o_5jpM6b4BXaLJx2M4ltbxTuEfuUWbCa-YWV4P0w4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=ATrqLRvqKEW-IIE_D9EGoB-HuzIBC-PqRtW9MnkyJve1bVSkXvcxvyvrtwAPD4jwVi_IeuMZu7ahZ3kmetpnvEdhKxn-Z_YLMuXHIk4KrIVeflVJnrzRH9QDB7_38ESKM7g35sCQQB8PkSbBXL8C8tmAr3GxGs1SFCH9SVOIUkUSosyHGcDUFfHLaNNehTn_3vKuvd7OW9F54j-VGCmFFHq-nDcKkpckD0d2jG1c8eEOM9LXBQozetR7l2d4FEnPkv7X5xfToaz-Rc-bWmzhTe51-TJ0bSAiy_wH6i2x1yDmbOgEmuUn5LuYn53gVh6TfVKEjuv6fleC2Ej0Q6vm9mrTy4gA3CF-J094dxgtTxtSq37yjoqAtbTeC6MO46RfBtJR1lBOoYEu-GuQDjYn3B19Qx2Tda_F-RXTfGNdWcfKoejT8F5J-bJnr2KNIPAN6O5jEhuQHXFMG_qpedOaBzBiajcb37ZpVEYAuatoNJmfYkOo9M2OjR-E7TfgzSMim1Y3_V7NclB1Ie4UgYdILRkrUmTcG2mD8PFzA0RHRRXDEIIdVUTkol3KjzqHNKLE25vFOxkidtBfTytq6re9cYWX2Jj-i1qBVngflBpS1cleCNiZY6ZulG-TlPTcbCly_o_5jpM6b4BXaLJx2M4ltbxTuEfuUWbCa-YWV4P0w4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ناتو وارد میشود
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20722" target="_blank">📅 15:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20721">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو : ما می‌دانیم چگونه در موضع خود باقی بمانیم، حتی در برابر بهترین دوستانمان، زمانی که این کار ضروری باشد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20721" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20720">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏مسعود پزشکیان: «دشمن افرادی را ترور می‌کند که گره‌گشا و حلال مسئله هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20720" target="_blank">📅 14:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20719">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست وزیر هستم، هیچ کشور فلسطینی، نه در غزه و نه در کرانه باختری، وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20719" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20718">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو : در روزهای اخیر در لبنان عملیات هدفمند انجام دادیم، از جمله در منطقه تپه علی الطاهر، اما وارد جزئیات نخواهم شد.
ایران به اسرائیل حمله نمی‌کند، زیرا می‌داند اگر چنین کاری انجام دهد، ضربه سنگینی به آن وارد خواهیم کرد.
من طرح ۱۵ بندی «شورای صلح» درباره غزه را رد می‌کنم و از غزه عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20718" target="_blank">📅 14:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20717">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یکی از رسانه های رژیم نزدیک به جبهه پایداری، با انتشار پیامی از هوادارانش خواست برای سلامتی مجتبی خامنه‌ای دعا کنند و «قربانی گوسفند» انجام دهند. در این پیام ادعا شده که «گروهی از علما» از در خطر بودن جان او خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20717" target="_blank">📅 14:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20716">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با کانال «12 نیوز» پیش‌بینی کرد تنگه هرمز طی 2 سال آینده اهمیت خود را از دست بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20716" target="_blank">📅 14:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20715">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌ @WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20715" target="_blank">📅 14:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20714">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20714" target="_blank">📅 14:08 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
