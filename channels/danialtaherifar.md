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
<img src="https://cdn4.telesco.pe/file/KyZtctFi0_cfjGWjjLKFrKLkV-PpfU7GLD-9pZmrMtH6KslLurrY7pj3qO3bxYT919-PfHTKsNVaBB6WFjwRPjCoH1OIdOnc1XpFpXQaQ3-XMbm1Y1nqApxa1sSh4DoFidsADi5TkJcxiUfj5lgwv4Vp5AnorCLm16ov8vaULKj7PjYYWy00kSjrvOiB2ebiAkD-Kw_faKLDSixRYxOWGmyZiiPe78-YzYUgsLQ7DevgTJw6-5q-q0RU2SdWC4anGEfBYmMAbuStN9wG_K3DXcspeCDLIOggLJ58IG-FWqcjLzYHzDoQvVcX62PCRdIYRoGzPOPr1SIqwREHqMlnUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPM1b0rZZ8inoLPTSgi1RLWAkV2ZsMJwyYEqjreS-YGtXkDIOdwXOjI1TOGGWcCVI-9aauI6Ntyi6QFU3iXrTwQeZuaNoQa29YdlGH96Yqb0zG4bbCLK9cm7JbuslSx3YCclGEVe9nZk6ypoV1R-n0CXd9X-cAj84Pljx-vhVSchSI2PWGM5nsYvjCfASAOhRHFSCGy_vH9dPvM7jzHwsApKl_jasbhQPZdnpvfGjvMOA7EDbS3CdrUU1TEXmcq67TFff95KVEgnxL5C72QXO6W0i6IzVR4ddYN3um-VZVaBMcqKhkTKsjAnKLBxsvFTeOVh92mrhrE09hdo66G0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 212 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 455 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=nu-0wyU4GBQF1cLNd5bmv72Vwu2-fJt6Ev1wwTYimIjDXcF8etzd56lgkLiKhocq_a9tGphJ5h1YjtAmgAeqyqcqYXgZADowQ1meHhSwdWTXmC3DuZBjwOxBEKFNTSyX6hjYj1Eznv8n1r_ssfcCeAEkWDk19PrihvAjYhfEg7Y93d_htukdXErbQFUieu2iL8P5I7kMqplfvkXy0xZLKP-vrfn_vjPU0wcdD4cSGHDNINx047J5isgbcyZuxWjGhAOd2gLTFjw1y34LDOKkMRJSqXqN0_TX6gPAjlhKYXB7tpK7BKyMJYwty0synGV3Wd4cn5U589FtC0rw_8T0yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=nu-0wyU4GBQF1cLNd5bmv72Vwu2-fJt6Ev1wwTYimIjDXcF8etzd56lgkLiKhocq_a9tGphJ5h1YjtAmgAeqyqcqYXgZADowQ1meHhSwdWTXmC3DuZBjwOxBEKFNTSyX6hjYj1Eznv8n1r_ssfcCeAEkWDk19PrihvAjYhfEg7Y93d_htukdXErbQFUieu2iL8P5I7kMqplfvkXy0xZLKP-vrfn_vjPU0wcdD4cSGHDNINx047J5isgbcyZuxWjGhAOd2gLTFjw1y34LDOKkMRJSqXqN0_TX6gPAjlhKYXB7tpK7BKyMJYwty0synGV3Wd4cn5U589FtC0rw_8T0yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 634 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUhinyGvvfrAB6W04jeGdT4Zj6WjTz4-OTlCqHJ-4eX_PVSLu19gBMLYoLSpK5cdB-cs49srAHDuid6q9-xsPiAKbvPy2Z9PHkpDe_I9Bce706nBzrEvO6iSzp4VeuaTq18l5M8dZknuksGrTvLa_b0eZR8O3qQx-I-N9L-UnXoXGhLjv_gxtntUfg8FD3U2Sw_C4aynCn8BVAEvg-G0dcuDNUP7NxolIk1BC_SUSeQjz2Mxjfh47H63i0J7Gl11yKgsKcVDN4dwgIl7Jqrj1UaKTealGPafld445Wl4qfiMiySsqKrBW6oj2FxMhPVZfa35IeRQKAw5893opifGZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 596 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 801 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU_qQqRr3La4PuITdlGmWB-Ndwq-DP1xpEUZiDtD5WQ3Rcv2zdamYzBf4-9c-g6GinaJtobc1ntb8eIZDGCJpYIz5g4OFnzDdmmvuDu1IstSBqimh0tapR6_5qiOJo0PAY30ZmrfwUiNyCJ9w5xusiKxnVCRMsRtvZBWqggRXo3niCkPRikgE6NVimkaMmo-2BHjELG6OvnAZ-LY7Y2kJ5JMXQWnes6I2ab0Fiw2M9FjcjlzhDS9A_58ISq4LtRjCCE7G0B8Za2Zys1rK8ckp059LMFub2nsfidN-SL9qO4WOyZQpgrD_Wr2zPvHOznycXw9R7cVqpK6o-i6zE3IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9lcXdWHDxe6YTO3HD8G6vT1Mm0cj4Ual-mvisOIpXTLU3TivfaFmflQVSaAzJV0tLZjuI_Wri53HLvJQt1dMjyG4B8DFB8ZO7Sj6p9FcOncwjgzl8vcEilHxEsaxTJshh--QGXfo2_6Ze90SCTk6ac9jP4yn-KNFf2EN9Zd2tylqZL3pkhfqnedDxmQZ5LYPpHoTn-BaP2Kz5-ciZWiltBtbjRsIvE5u3dC_rUqjrpWxZV4tKQqgXpCMr8-vQMzO2GYP8KuHonF1jctoQlUGsVmeAgXIhhZHd1BxXhNulDSmODCoSgiFqCcLEfWgNJAvv2yd7x9BuLHK-xYiOnWGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJrbyQFr6TJ_vTi9dY9_t1_UudpZbl74HQG9Q1YZvDju1GcRSkno2X-rUKILMlPipulg6YsL3EyJYNa9BkLmSLuinYPy4c54h7s47vsbxSiZfc3XeHo8u8sQRIyftu9RoiNXLSeAckwS96yizrO1G7U74Ao_XuOsjqUs4okMAh5P6wNojBjj50emGt9-C6JCh-tGnQwyVmhjVR3E14uGImUfID2p06thmqcyTF5v0CBqTTej5uXx4fi22Vtn6EvFgAd9K07zXPlUAL1up-mFaUaaaRTk5tKTt3i4XTVHrnTYVvDs0WGshILbKpTgdWdMO_uhNFEtYN3jov6kC2v5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPB2SX-uGp5sU1ZN5Zt7sEsBHXuomJyYjwXDP7cKlvVfZeaVJAww5xYBRCk_awC6jwaHg_z4aNicGVLAjDIAewfubbzaHSqcfn_VniFnGB4RWwnXti9xZOOyN6HLILaWSpch03qj5DdJEKgi1eGmeAF8D46fuq30FThg1JVV1VrFVQqSJ-c3DEkoOrvs578ZnYD7vg7Uz8rpTaXBPKbPN8bYrpgqbubrYdYHmFIo7EbQE1677l52qxb3ntknP1paXivkUbY__8wEuKLGa-MKAN39R5t09jChOeyiBVXDprILr7Cinw74TxlGUiGjgtTI5U0O-Au6X8TmZfUdnvqIHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtDuUt1mALK6kg7r9dOe3FjFsp1zYVNuSNqnhkS-qB3wenuPeYqTbNZZ7q5bKaYfFnA9AixvbsZrJOTsplq8Bw_M_kC9V0VbyBtYFLmOmvNNYpdHwj2WQNj79xUN_Ebttx2eqNjuU2x3drLyvcLKqKXPqlgjY7RJuzSA6zqcGJzHSHdlSJrSSvpxYTR_mlbNifhH2_GIq4i5AR-ADblTm2QEpfbP7jn6u5fg_q2kLkGVJ2_kagmwwuR1kgs1_bLN54061uue-WYZGHFIl1hgjGQAdn0wQMJrl0-XOVYKvGUaLDxVG2z0kErEfXdEV0VqFt-nC1LTwZS9L4jph9wAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 899 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 959 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFug4xA_V2vGCkekzMNpUm6orz_C_wdz9PgSt6fPYg82RJ5ByR7pVgsGWfFHdpk2igdc3V9C14mzSuH7d7iiaUooGXRLo2JSjCmbEmw84H8nZ-cXGxNo6NCWxI44kBp4yUImgUzwFLVe7d3DKMST0A59iv4bbT4rTvAVzdfbpiWSP5TRwswxtK58ziLkqjuH81ejihSGV4iMvXC2fMXNC6SuYp6BL8cM2r6b8m5CRCc8nhviyJdgrYpkUqAY278Drht2_G1AXPUt3o6p-nZTRQDoV8JNDs08_t61o0Kc0XWnA6xJKs64UjbboNy5RQ9LyW6vUNHgvBqBc47DgFusIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Thh_egAe_B6SFA8iEJ_Kx2hs189coeVWBk4TZ0alAb15EwzAMdyB8IQ_5uBXmM8annyw8AJkPZUTATNPfT8_yvzrgwRi_7FDyz0r10zWIJnhhmNtxFlzrAFHFOZmY684xYDIXXTn89A1S_HZG3G20cnyQGHnIOhbSXtxDOT4N4QtMmfdf2cfEYUrc89eaZg7WNrC4IeCw8KMmgyuNH9HlWcMnKl8GL5cvayjS3HjFdHS_yvfOsDTNXuUO07MaTDpfOgkNYMK2_B7rPUz6-GtonGdBtBxQkx4bql-2UwS6bMgp15j9yy-cKc2HIferrwnFhr1sdW47uUZjtkhlx-5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XH_NmUsp6VZZynL2JTQ-xUWpOXjIzcAqu41icO3kwyEysPGbPOiTksoTndgpy98y2e6T1-EhfgCrfol7IXAfpZv8NO3pEBEgXrHKPjUz33cuVcGqVdAFEPTSX3jMkzRMiCeewKuuLLY7dICmO0UiaOrBe9WsDlYK1OaEfCDqmBSDK3WhvMF2_1WZOxNH-14NumNn2ntnQUv3p_VVUSncLzy7U4dZwU7N5vJEBsPueRQsGfIJkkQ6ZA2p5HETl27mwTwFEYZNBEqPQTB0GjbbFMC7dnmKb8sEmAqGAR7P8t7_JzvT9SImgEkj6T57cm8528MfLF8QWifsb5dDSvFI5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNP9Yx152WQC2GMSEAxuYltv1thTfQFlyY69np1ymU6IRC8t2fa-kBcsaVCWdby-OXACyEXPP9nuw3WGPvC4JaQyYSVtty6XTxdirem54MAfLxhiYq2Fd5aJsehE4Hw0fU1FscIy3ge9ZvSrxYflkCibo0dkhCVB6J39BojqV5abFarAyCnTu-HxSH02_OTM1pW0XkF2MaOrncUzztJ-GvkQPBtK_5M51wd1_HU_MsYdFc_HxTNfUknIs9Ygw1CLvKAKGTuI6STEQ4hCy41cVkfxkAGZs3ELhn04dFi_PA6oDjfTXBt-xs_jLqodYGt1-ET1cU3WehMb05S35mqxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 952 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 896 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhNi_hieXr98Wtdtx2gyVh8M6_6slbORopPHpyX1BqVd60AZ9fxchFXQsel00k0FxphG_yxG8_OwRj5Rt1pdjqzo6v_BP_BlyVJV6y7MQYsEbt7c7sMQuMzgs5A_Zq968ScB7w8ze2PfdVJWrlVuN7h9Yh03UScXg36u7JDJmEia8lb09nC0I7zPC2hkiO-TwZIoc3xV79U8370pl1wRZpuTsp1cdyeoxUVIp29q7jISwP_0cKMGMFykZ5OKUl_XrsRdm-lkanf0-qiKoXljCi1Ckkp4ZYYCoOu0HFeyUIwb5wx_zRZ2t9inzYBT4Wl7NmzmrCmiY97L3vGRXNbZaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy92yymnk8IzrfuaMYWUZhmJKa5uXw2-U60y9DlxDy_NlCxMnvMcXSWX_Iz2ZlsshEISe4YeWCDFGatfmZtugmCZh7iIb3LVHlsDcoMNOqEFwxTSZWvYPurHj4B23yBPrItW6psGCcQyqnipVg5t8keOEVAfBI-Py_DtdEK1uPtSUmIsM2aTMFeAVSWOejQuAM7X7n5LjWb9uWXDophfu-ZOwHBwfr0KbVgvQa_bod9-qbU_UeCgAEv2NJOt7skeUt7y3fDsWK2NQRJwjW1ibnF0kuIrvuAOAeL4pVwg6Dc6veM9XQZwMZbMp8iSjvbmcIwP05x_BL-Mt-4xz8oS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 685 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg6F9qxCCa6QnzNG-7YHLIGJ9Bkw_9shZ_pzirKgNuACr8sRt9YeCf1gAvJmG3ONFIDZHZI8u81ipVg-ZBvZbJs-9QWjD-NqsKh7cIq6muPrQQFx_4Ohfg0I8egU0IsWAAL7uVXyhzsS_OCHIUalJfo1f5KPuLm5r--d4WeBBHnHmbINHLRL4HcACTk24TIWb7Fvd8IBMVM_9MPgpZ8G9bJ9KT27gMPMBI--WHcgFlux2jQinSGlaQECBRsJ6UW7rw2hdXZg6Xh8r5NbIsuNwFWTalWEGSRjY18qVVJ6VOfOU8KDoUHCFrGdG3ETVWlF5aLE-LN5VkIdbQvjc43qNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qb0pGsEVlo453Dyp7XAVcxEJb75PZKcf3FYs659OdK3OtZaLTw_s2jyzpsSFKbYqNYgYgThl-KItKtWQQxbrywBDAVMg17Y90FXnAK1117S7GPuL98s4hCxtju6grPXcUNSabefs8L_C41YHPvBMO-_8mZZTBFSTNTS8F73CFkm0i7zxBVIGfF1IaEQJmRDdXCuU_VhoCT81bC5V_07RT037IA5DLo1QhC4WjGt929RdU28MN467YUuz2S-0xgsnl39DspwO8WVvqflg5gae9oU6AQXVK_a5rX2-LNFy0OSnOHmGlSxO4GrQIF8wUUpAr3Cd-j_klZfEfRneGIUzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dN5PhvR09EtASc_d_smIaVQYtkf_fQyTONllxU32pO0ha6y2YIlsFs569BwJlwraIXHzedEuTT6jt2H5utpEExbGLEBTTttIu0RyE6qsw0S-94tLOWFsq05V2zph6NX3i6mVywIOwRbVqbIH-jNbWZY9G1kfFTIlnJNi6ynsib6LM0KLjEJPKsP-CDvhTpewqISEeJ_R3tpPyq7McC0lTah1RYGrlp6KPR9ixyYrb-0CD1ABJmVZdCEkopg7zLSo0BIk1ompSfYuLuxCBecWmFEuUbEp171tb82e113oxHjxQjmcMcJYySF1Jym0a7D-tSvk3WWGDpHYMxTtUCOR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBcKYiusLoxgW98vgdXQ0namIUpuiLM9OjPs6Tec0wLFv6y5VfhOjh6UsUh9OzhLZ4pGO0_a58qFLSJPSjz-bhUb9yBD4CGT-OmFpVYU8sXyW38QoAPMvRryTP_s1LV3WZE0TsNWjsXZTRVRUVojLcHSPZCrAeXHM81HKL93FhM5b9VHOeMp2w8eZmq94bB_BUtUmzV6fzKCofKYoRapIo1n7iECRO0dZ3Vt8_QHmk6AhRxH9wScWKL4i9gFwkivOQ2HLq5Tzah43AmKfZbtKCKsclclwBdoWYxFgd8TroEYK-2FRDCdXrM67i6-H7TDbF1V2icSdc1aeydrp4vVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHVCuzAdjmAujPEmuCwkYz_Xjuy0I_2kWjlxnmYs60u77_0tJMK3XFKm7LExFY2MyCjx4LxjK-3KqqWffpm8BaZCd8ldSQ0X09s3rwIRZOdcG9ll0mflwhAm7HPLoDMr7fvcqHiDu0rlTpKWN6d1VpO9VjKLeeC4dxCBUjP1-TcjxBRb19_-euoMesgD6SEogtabinc-fXzyPx-3eb_a8UnXmzYqojQCPnAvXDQ10oAvksNOdRUxM4zuCV7rIzsyhPNDBAQH4ckaw7ya2GITxIpcWsr13pmsTpkez7uOlV_frndySpp-f-9ldnL14ujGlAaSEfwoqtRO2V3ijEW36g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_UixLB1kphAhsSr52vKkbFI1kKaKFKXNSDf-xFERhZ9dbPJXZ6kX0DP0E3S-76Tc_36y9mkNvXwden4W5wZj6X_R1RZ3Exl_jpvSl5pfv7QZbgDilfxXDsACvsv3PjXBvzScDQAubjTqk51I8cKTVqt3i4ETkMvocMWDQMGDgOnCQ6_hgOPmvkfkguT8TWL3JnzLtIezuuRdVK0lz41GUX3Z_d2MpHTBbBvLlZiZ5cZcpsp0G3vAaGbMygKx8twCvquIyk3RJU17w-GBsdlb7YNZrtnTzrGaVUUr8cvTiCRzPrIqQFgRigr_N6_Rd9GrTmJDQ-f8Wwks9h_bmt1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=vvtWK-eo5TIYdO7ji3X-eCDhzVcxri4VxxnPOFv3E7xZ13tS55GI_46AUt4DCn8ggbmPnCML85pPahoL4o4lK1PySLHkm1ChYPKrgZeKEwQBDkReFWl11yehqcUEDqNuYEeLVv6aRp981uVc4qzAkU6RJHaJD1RY3l5T9xYujah1rgh6KuUmgZlYTM2NusyVq7AgkfjtW6K0xr7XQ_csHH40NPYacd5Y6kHVCsT2axjeHLQ7F_6pwE8XjYDfNfCXzoQOa61PJYsxhmBQ1ndH7Ses17LUDeKvOmN7hjyEOGw5WQKTl7xtjILPY4XHN2J8ZZUCVyrMMbtxwxB4NKhlEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=vvtWK-eo5TIYdO7ji3X-eCDhzVcxri4VxxnPOFv3E7xZ13tS55GI_46AUt4DCn8ggbmPnCML85pPahoL4o4lK1PySLHkm1ChYPKrgZeKEwQBDkReFWl11yehqcUEDqNuYEeLVv6aRp981uVc4qzAkU6RJHaJD1RY3l5T9xYujah1rgh6KuUmgZlYTM2NusyVq7AgkfjtW6K0xr7XQ_csHH40NPYacd5Y6kHVCsT2axjeHLQ7F_6pwE8XjYDfNfCXzoQOa61PJYsxhmBQ1ndH7Ses17LUDeKvOmN7hjyEOGw5WQKTl7xtjILPY4XHN2J8ZZUCVyrMMbtxwxB4NKhlEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVK0Bsfd-82a0zU0FBRPuP8B6Iau8uXSAg7xmegTi1m03dBSRAJqL031x49NymEBlFfxiPbPQM-pRo5-_elR_rq0kQZcM0Hn6c4GZME8uNMu_uXQ38MJdJxcYINI01Ef2FxSJ2VVlbOrD8j2TbMiqdbuoHM32fCfejg-9EU4HlP702_tr-L6vWzXqiXqXlLEqmf2oIR9_OXrZM7oCxXPTw8KKpuY2WenIl7D38Iu7Z8oMzZVwkSwxwUNJW1s8S8cwHzYxs2iq_sYb7hX50xy6QUJSj7tmAAZAehzxQw79IbatUF0PR7OpVG0Zqa_WYXD28Y37l8-zLCNoGBXFOZM7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFNfJ3u-vtL-wy_ncpea7w6Do7aupqMzgiO1h0JSow-pPGCrWbXoAq4-fVt8puh0kzyf1stYxFUwETxx0c0O4-ixd3TtsQAFFovSzgwQNWe7FaKeAY7amgONbRo7t28nxLWXSgTHJrQ2ZY3D_2T7VU2sPfv6c3jlvZEzA0UCMBeUhByTbQkYsmOjx7GTjUe_IhogD4OkDVG6PAc7afwo1T0qkLFaFj30U6yl9aUAhs1hbwmqzRn78ghsEHNl7vTeTJqDh7AcEqniTgOrQy3gdwC2tQO3-PpdityPF6V6UzME3bE9p1LM37WAwV-s4js6qMD_Xk2uTzS2GF5rKuLkuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_ZnFxvxbfNGy_1KzBLp0AES1NAtX_LTWAkukPLfMI1sJoDzZSlfw9aD7Lww5B9irTZ4lKozaBiBXSz3oIBa8LhaFP4cqO8PZN3S4zoqD_bJkQI-4hhMeefc7Niaj8RbaZiYD02rRvx7KxnlkjT9qrJvlsbDngm62fXojMoZSGcrZnu00omW5sOz4NSPpM8sOjQH8WiJq_k3NuwVCC-TY52vNV4DcBAL_oCehCOTwD54_Mj9UbZWUqryOYpQ2c9gaa8AuxC_kxSb2hzjuNg036PU9DhGyMZLYGiCYl9FuH9qAoYaw39X7rbkixqf-20-w53zD6NSX2xKGZZLwaf7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eipq41UcPj_K4wYgHSBGe6jAH5QUvpUqM-bnX9Vjp2DEzSX3b1m9GFWueBiDUmiywc3Sx0N26lokWtH-MM4IKk6Eqdw1VVrpx-Vyvtq5B7f60o79CcdWo8pbxCEvkpb8JCkQLfdc8e7FB3cCHzQlJiyowZsI9EReVkDYcVWIPdrZ-sVxp8wlTPMqcbTpnBmiTbwTyFhKFkkwoEFzJ1lDASJVt5MHlvyv8Z7c2qYq2H9cPSIwxlM5gezT5mBzBwK3geQ7OvpAdCvj2HIxwDmUIyLc6N_674uZrURTisvzEK0F8F81YbVtki8Vz8iEoOC4f-mp2JVXAyQonTaEBArAiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg-qKgGGIEdwfV69t1o046pA9I9EiOh7XFXPy_GRJEpb8Uqicz_EFdvsfTBXTDjUpP0UHfcLSGXKfXMdVagm8wZXJTmlgaO3gOKHBWjed5qRlY7PGQreCGJxsZEKIkldlmbJVtW_M1mz7YXPKWMCTdvQNQWEY6fD9hdhQ1NLwE16wHk7ZjHem88Qt5WQlGLGUvH6E13coX_xrzChMzIRUI_GbEvwMphaLHgn3iTetREwz3wuEZ_bAKBp7QHSyXTzOHfrPI_m9EXhEtMjX6CATDYM9zxKfWvoRvbzsRCxRrQFAuf9E4YgXVZLWKV_mUwQS7qA25FC-Feq9NN4gtDEFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EROlY8_3u0y-FfIglSaLR-LfnvCdaD49aK1oOFohokJgfVTHkrW_XX3BUMLaVyLiuTSJYuVdrEY3UICc2RrpF_omUgjY0MZUVg9R07yp0Y5pBJ3mPjmqPg-n92LSpvY98cd5Ktp2gdDbohFpteMgvgoCCi9jQLHXDLTlj-IO9hWoo93f69ZGD3XLvgGmfrqEhMkya9oiWFD1tjIxbfWilPCqVYb0Pfszdm8NEC-30EUDKZcwgVRF89NXOATEQZ8ML25CckUsYz10akX9DhBjSFNdY7w9k4q0a-nsrhEeOcIqVymvKmS4DGOcugAkY36Zj3srEPRJ0jUORNxGWV9a5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijHF0f2FR5ZlqonCbTpyv4KgD34eq0h08lBErvF5e5Pnr9IJ509xTCld-CI4aUTlVoJ3CrKNToM7w-R9SibEqnh0y_blATbsd-3r0aEAVGaVPscLCuuQ_folasqUaz3eXwOErIHi59Kvu71om_2I16SKqfMFlucqT4nehyxElE_QViCX7ujsIe8GNP3BloYYpa-VvLq5F6-eDQKa6goGMrnJIKEJrgmWAvy2MX7FLQ6eH1EslpFYUfudkFkNvWfkSDRYCvgQvwa3gLZK4S8X24SNAu2zry51qyRrDeAQrGeBSgzfuA_7ST5EInjoY--lSgMtYdjRhVGShVwv4S9_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C40DEwU7I5Sx4U3cNyXLleBZeF-FSp0FCTEUxBz8ZyxtYiEglRBTD_cxVoJLiFQ58qALjIQl8hRBKsGvaAFa-ofOevMK2vULanCgrWkOOWxZABOUid4NQx-jTPgMuro2L2IBCMfSASRob6SXEGkOwB2WgRqbfm4J0hgg-QaPNgkzDu3qw8bqqXzsBZYHwTar8ehBGva3Fg7rwe6J9m53pBQLXG7EEujm6NvJ3s2_mNykXCLgrm2tR-xXZCgGU2Czj8_BmF88SsY7xJF8_BOiaZtQQSQ2IO0iFUj7-LVV9HHNBXMEUP6e92R6QV_Te0pEPquvdAlYHwgJtDH0y-Fy9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b64MRkJYGGeD5jRDfRQ-w4WIAUTAhJpVj3jYDC-wWDzNg9Iz3l0b922e9U0napLawMNuF-gAhs6tt1C-Isnjoo0W5FuSK-Op77NAwMX2BI9Ob2QFCIm-OLm4J4w8SUc7eFgfH_xJfuczczb3cGQGdHD9TNCX9g_JfdEqggInjdm4R9qAUQz2whlgwxAObTHK7B-ubjoq6ySpjDfgtin9AQxYmXHjb5wzi3gO0zBc6uJZN6SECQPd5ZjExpuQjoH2cuOVnNV2S2yOnufNRJdpMFoJeLkKqcsM69A3R3kuo9ojHa5_YhuCefsoj6BLeVPwlLV7Re9gb9ytwEksyEMyTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHlyniHCHwrCnL_Cz62avsc5z-PiTp4LAPMPyT2tSlPUpaKfOSLp2CZeo3k7J_fkpJ3eDrO6GbBFWOsdwkt3ADXaL1Vb-T8SqohP6UZXDbKxBRuXgQtSmI1aH1llcxMawQlS5FIB00Z9j8iaR-Xcmzxp1BiRsSfKJZXMF0zbT1EWES1ynGJBT6SODfIv7njnTjMkyiPED5iri5XpkQmQIf693_OnoYywvWoTUmgCdsVbS69VN3n-hVNBeY0jR69BaoIrq-VI-rSVycY2tuIwxya4Sb3nPg4wwhxpaVkUe9FJdyJFUd_pDNmt1yispPw8KP5suWwmhvvVj0KSm85csg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi74ZbH9UXFhUT2WEXU5uy1uAt5GNs2juuxY6CW-T9-Uqy96TXkkOg7uJnvHQdBjODHZ4CQ85yEvxp_Lw8TrSSQSOi32335EWDFP1lrHp-dYwrZFAYCbqqx67I6w1rFx8Tkk8s44aXR33ljvdV4Xdtw3Q0nu1gdndCewpMYqfU4hkyLL_B-sBiW64VNh4yedQq-G78Mnr2JUvzOkazTObjTkn_vp2qlPXJ91Yu3sGsw7wxUeQYxEVo-96gRRH3RZhNJlvI-1u7g9t5Pm-oaUUUDrKieleiV4shLf-yDUOwhuIKwtlekMoLPC1c1h8ThT2YCt1ji0Ze2GoVIEAM5MEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxrJa6wkxBGkRs_zatuqDKTRsAjBdiNXtpEYqBsEPMvSxd76FzF65YttfN2M44aqeGVcGjZM3v5h5nZUU0rnSD_Wzi_I436rxL96--gSXxR6xxgc7dyaanrlNSu1oB3onvuaH3iYaIUsun4ZwC3F8NFVyQ3wn8jzAIB3BMb1SmV41zK2cShBercntaEM3Fw7AMwwZ0XQ6zoSQj54AkbCfXzgkRnl9azHVIuBuJp_6Lz5mr-gbw_wK4_SMcQleAfNSRKhYYzDPCk1TILA5zaWrYv8o4NqlbC7isZjKrlIwVPkbswxlageBBP6Roo03KDq8OvbQ6JYcVrOnarvsu3poQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 695 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_0YwTwdoO0mXAs4-oAJFrspMv8q-fkEkenuYFHT9CDi-B-HJ3kVbzwMegxUcx9T8Tfndq6zYq508ke9KppWxCB11lODuOcRpfmr_CUbql-Ubcu0dhTmZRIVWFftf9sF-fo1fyBngLqxsTgrjv83UTSeKi0_JzIcADH3KKYsEcxl2dR-b1BCfwIIZySLo8aLF4Hfd6-5IFLahglnYGUTrp2fh-sFjw7QvoL1XO8VUP3pOlA_HPpBSQkyBBGidyCXFUApqGk6PlkpU6K_NC092ouzq9vbN_q7HF9lPcQMxoEwPvjFYFBUyKpGU_f-fOecwaHccWGCtXMTg8qVOhU8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItJSOx1G_fNZeqvE2apRxdfkurdFHDFks6iu-Qzwspnc8yC5kUAw2vK3xueGLXvIDP1CFScg7TUEwLsH7m42gQRr71TY-dp_cx2i4kg32vnmPSBFTdSbV4A37RVgpHz7ihQnSaf2hIBUWSRqw9v8MKtWaRrL5548a97l9-FS1SaXkEwvl5Rxb-x5-aH0vl9i6bx1x82xWVQc_6OMCZy6JvtBsjax2J7EqA8dGaZifXY_JXXm1SYTObxTvfgPhE1MVTgmJDl0ViFD2dIjfV6rw9-QuJ7KQI1fgAI9gEMWrAWlk0uwm3tGNZ6W67O_moaz4gGEc8VSaIx_etT5BIh-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDsR0Cx_NJaR2UW_GMxpZIrNSKfKBaMlv5NSQf3sTcJ0R0qRLLzlz1Gpn_rt-0ldZFBCuLWYlCpzyvalL8WMyTcQ3Ci9vwvwnvbnpPAgIafRYsqrCLmNXXgKOk5pJXJVAdN-TkG3azh09lEMPPhZ08eG2GlBkcYTgYquJh0WSpCc8bbY2-6UegzBADJQ0NRvzuWHMFfBAbY_4aCiOcUkSZcQ607G6uXm6XGRCLZ33TerIevaMI01qGrDFeLxqAakNQV4U1YWUEFtOENyaBy3YjUKMZYZdtpTBpdSntwc7EZOZnbHSh75NmQ6spe9O1rnAvxFAEql62dxzcURrdErKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EgJZEWaT7dhMhXTmOQ7X5pMO9Mb4pzYubA29WnWLKkfxmqE2GDZfA_vUmrdjGADTRCtekFIeD9GZGMK2dPwoNeD04lWr53QtNIdF5MTaccV9pp403uYeVPWmqw_DT4AdqPLSFQWRbwLcoCLOdAGpobVTB6Arx-mwpOGDtAhUr43DziwdzvgskS_UgJZ77HahyqEMQ7paZyuAB4Jg6GWCXobxrMFd7fTWwG4d3BKf8I_eexHySFAVaSgyVT3o-mud8M4_0WK6ZBlHaQO16RspO3ffrg6R0IEReGwUY6n-jodISWiF8eQnc1gHzdplVtLcmsa_z_4PWb4vbP-3DCd85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYUHy2_D8RRBVO3-ldjc-XWYUZOCBNgTRp8rqtUPy-F9Md3FSp34YUvYVe5bDnZQgOJOGBb8YtYmpjOKsv2W-nzuF-C-FBpsBeQCGr2g9oiDNB-lI-qMZOEtXkw9eTbKrc5jWVULzed6n2kz4FRhf-h0244SM3CG42fRuL5Tw1B0JqGNABHQEjy32XLG1wKl0yBiwwP5ZCVlx5xL8Mt_1HTFBFrvdRqMWbKCmzpG5cAAl-R99BlKFnF9B6Z7g5UzeQ-6OVpckOh6bQWm3XIDd1vPTHIF18YWyiUvYsjNn_wzk79lvrSgXv1MRl2Pyv1e5BD4jfFbBytbWcCnPXy40g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcsXTv-R1SGfO5892Ni3lfKcV-GZZW34enZ-ZzgFkKNq0qW5e-sV4x--sRszvVHMmNXEKMvSYMISCeGCcesNDz70PxMlV2BJbKiqrWiahahcBUD3QRgGG4NeFx5Mii6Bu-ZZhPX7R9Mepob-BVGsv8mHynLdOCyt5EINN1EkbmbZXpU4bW8PYc6R4cSZmyvh8Oq3pb5kJ3M9p9a0LAN-y-pRJihl86a5vdJdC43C4ObLtpT-EL-OsxaFDOr4n0AmLXD9Zv0AczlhoroXn8y50yaxpJinrjuS95s269pu_b-bFD8knSzZIZohGbc-KRzZrlsOswkbXDFtq15CiqbIyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0QiTAiL6IHlLftur8HS6vxQhF76IkksehTo1fyMWFW8PvIoUlS56GfrgouMn0hPmGqE214kBS7q-iv4f8xp6qyaQy-1L-J7lI3c7KQBuWtieqWDnvW97moIyDatFBIT7GaHxN2LBafW1967cordsmD6ct9u1MvG2JCQKu8PjUaw_z0JAwjvddWYi0R4vKbC32Ux38AED4MFJkeGFZMEAykH0ooyK5OhXaYQ2HwhqYRuSHQ9qtu_9m6UDKbFhhphleVaEHvH5VEw8qrZ6DP4nX1y5W03PfyJPc-tobJuBsdvah-RxkkTB6GtR0rujuPDLqHpY5ZbCgGIegnhGqAi1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl7rXoAbYihKsl6jUuKzl_wYuFJDuTTeNpx9ZuqpsPgAjTj42qRTZPyN2LIPoFkxyCCMzgr9v01F57Xdu3BXnrNJrfG5uN3oL1CEjSH-vBKMmH-GgpkEgZagBBlX0sSCYIhiQpn7i9egvUsPW-40K9YQZUSzJsKsURsEfN-xCaF6KaUa68vhz5t_8UaQQlJ-cm2di7qdrt_CFj606HHIHKPSGQrFntgCjfSWVAwKbro6mHPRmh-G6FNKSNjvrSPxydlUK4IQljt3JiLmw0mO3Zhy02rLMWzoA0ix9g3mMIXmYori_AZdmvTDZGZF0O3PaHJwA6bMtum20wFlQn7r0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N22jLcYeppUH_8QQNSnN-XB-Hk17LxCUBbSqRKyMW0phs72L9AxiGmz0fSpI-iZxlIcl4RVFFBynC6ZUqd9MfFrq_yvxeBHlgGLJT9D74piHWmyumPTWVeCel5TY5kEuevM04wHsRWVS1ThR_jagaMmCSvEcj4XTLqe-b5FV9-8fPb2DWdV6ATKr8RIEPYj69gstwnE3q5Jsjw0J8uvn1I53Edch6kI_eA53UbKRnJtFBNa9ROYhhLJKag6um7LmLvbQ8ylS1Cm2OXmOG4eANWE93R3kqVpEe7qDp78sV2PoVneLYOkJ3AEfDmkChbBf5CcQxk1B6rce6t4nw7a86A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgHER2RLPvH0AFcmIVb8LMALaZs48inWu7SpCUF0IIDBofBrl683W-1ULN7Ww1Mt0bRJBt1ApEfRy2FLcJr8XwQqDqE_UWjRCMTErvlYPOFHJMwrx1crKai4Apvtv8nrrrB35VJRq5PV7VXQ36_IhTN1jCwuGPakwNKkwAX3RP5YAQ88nHHrIrtpGXXktdAiZgLiHbYMlHydZ_0JnycoN8hh34ct2DRVFfxt175h-P0xXyMKETNbB_ZAbGKceS2SeSohWctwotCgmjlU5S0kkZ57CJU8gc67BKp67oOQFpoX6ADDExeioUByF0Hr-2KB4fhao3cZBiatk0NF7NZnwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V52GP9VJsdb_AX85r04NKWp7iqbsZ4_oUJA99TmFN4062Fjm2XoifIgwhiNnRWxMfg1rz4rS8QslFaQBk7f4woj-kF4y4D3oKZJxFoXWd0OqUuXcGRqQALHrfgvGT8taamO-P45QFy9kr7Mrj2hFUNM21oIUWTXAN19LjXoQoXd8GAkH6y6oQ7AEw7ajBNyyUND0jXonjZhjAoQeDJXX1Nhh1IHLhR5r6-0zP8rEZueb7ejvXISXC0SSHOP-9j0Rkx5bPzPputlKN4fi9-dsteV-CNcAXHFN9YaU73J24jp5tUoIUOpxda4zB727VTkaV1-P8Bprtj8sUPOXjHzqDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbowHAvy2dCwunONs9fdu0fpVwhJCcwSuQ4_4w3B4khBhzLvd6mrt2fekFLzo-SpjNZ--iq_6G3BjQdNMXdnhF3WaHcmCLXmQaWqK-XixmGfiNmuvhaiJppVk9tIC--K77zJC8-N1DbbPZGuF_OOvaIs0RNnrJH0-dHAbh2_8lWE9EAkGbdULcgzYSA3w9Jp3jaMR8G79OGb5IfBB-SKv0GX1ULXeVB6nGDFcR1y7dRNpntMteuIZg0EqzCn1tgcpaUoGIYmJYUeHQbtNRF8yPXhOBHA16_-TMYP7vTWVJMlwrJYrZVcFFHuyXkOO5RemHBcjgr2sHG9eit5lEyYQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhM8gy4Pajt9WqL8eveIevC3quExwHcccfWU_BuvZSEg8a2O7InuwC95Or441TgWNSMqxmjhX0HO4YWzEzYgVGPPkkEgQ0blQSP0Fyf_3M2XGDhZ2F-4jqRNRgcu-XtJPQ3hLwDNC_qQHbykTXyfsvw_gokyNQbX3kOqhQ2piQH7r8U7IxZZ_z0_fA2ndFlPKo8ZUeHpQjEVBMEPB2liPTg_xRBPV0_6LR4QRFXwV5FnDhHA3dZWKKopmKdkEoUChjF0x4wESSQxOm7lmwSlYC5nKDfeZYFoX05X8KX1MTH8UiG5FCHdALvlHp0WphKx2MYlTrr1agIi5lg88EEqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5byqSfbKuWqKb2MSIn9ki9DurZPgEFlZubQhtsH6GuYj-pPkOu9z58imzwG1KCd4LDPt1zUMNRDXkgiLJFlMSBFiN07M7kpJ-LKafhkiDoloi5lZZtxoB-jcSZ_40oPku4JvsUMix92gogrEyq-WtR43CQicRMJ_Yee3BRQ6YoHKdbr-uVZh0Pb44IhLbO7PqVpenPUJkJRloHdcvurq1z1RuKy9LktOAPD0icIUovaPtK2Ki5qCyeb3n6WU_ndhoJ-RLC6ivtQOaSE3_DsAx4YI8_9zV8zvzz9RPwyTQc7OEcHxVNW9WIrPvT1_zMa_lnt1hbHsjH1pZyLyAFoTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6JmJ_ia67rLUhHdyS4yIx1SVe3q73xLwIpcsiLD5P2dJRGNtlE-J0uohqhuuaMfG9rs-oQ8cE3ydhxwO3NmMV-AEe0mepbCi97Ki1Jm2ABMXXZ5d56N7E03k6x8k1ixs3E_ypqgOZZAKbBb07Noj14D_v6B-fozvfVrQcLvV12mLVluIg3dzc46eLXoNG8qQIUBAO6tfM1aAJJPLESVfM5tRnWZkbnaEFSB_ZQzTAewdRK_ABe1NyMlQZcE0bdTDJ9McdYYUhQf-PBLK2xwqEJWGKbeMydqfwdcG5Lo0IaFo2JfDgMItJHFQz95jc29WnXo6D7pN8it1skdi4UE1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu54E3zZzpRC28mciF-_6m8OjTXqcIKilQ93hctfjuZKX3leajpUYSmezaZRihMtpb6O7xmDBedeKUFi-3uikNgOWctamZuVjtPk4wN9AT9qJArkvwvRgHWQwki7I9GvQOh3G9wwwyuns1NRrVBGR9w98vpRMhHSH1c2mNzbDlsgOQkrsyr6V_3958NR4V9AYr5akQxgfsseAEMBU7lfZTvtB4kWHHXNEg4Jsu9Q7HqMMcCKMpJDIWcxrlP8st6y9fUrpt1j0bg_gqvYkxnDqdacKrkp-ATUANQG7KuaP4P3RHHLtRkevrQtNCSJev8RuDqLM0O77g6Xi3t3ZDA88w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_xvVSZs2rlFNdhMkNzrMCdHCfT4JaYVJFiFTGDee5x7J25hPM03MUFaNqKHhjCQxyvhQc4ERPCzvDBYxXDfvdp9zWceLqKgvcQHkT4VDdaX0xPwAD_deGffPQfc2yi9Hg6EBorZaaUomuXzEkK8BGpRSpCY_LxE24b3Y9YXbyJBiNSWY76Wt5VFIGAD7AX1mkaz09SbpBZwGlDLYJ6wQ2V4903TINKCMaub_CfQa6UhxT3WZjhUHs22KeaGTjKGHNINX2ecbZ-Hh5PPrIbSDajNNgwWm813v9JwHICbAyuATZ1i9KWd9Erx6RBrPPS7aYMTgsIhH3eqT8EuO1DyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-WYTFF_yKbtvkEiPVqIb_DRl1qO_2Kk9fYXh9--NEmcMuvIN9msXn6W9rKNs9rwCg371wC9qkRIrpDM5JpBuwj_6cILBk0bVi6etaVT0Lj5gaHFxDliiP2kN6aloXLnm6TP1X1HmgltnZDp954imXFs-2SnwgR2V_llE2LXxhAzjd1BbLfTvtTNlNEXqTMuI0f_mjE9QGZNE2qMy37JTygmo3CLSVTSWAbGBeqcYszvzRWyd9YME5XjDWPYrbcmDnweE06P5p8QQYifs6Xn1zXEk8a2hQJRKzw-YmmgS7-6R7hFZDSZclWbbaeeut1WL2zyK-aV7Rq89K-fRDTVmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhnNrUCEIxXI5oqFCXz847XAm6QxGpoPx9tLhBMeC6nj5cO2gT08RlwBStVxxJYuUTVGezt2twYI1ax9H-rNNsQWaVSVfOMO2V127tK087kM1L8pWm56LbntOSiyka7MwHiop_KUMbAJ1AJuqTXcx-y7IQnhmDXW9zRwmuXfo3khFCqKiLg-005AhA79OcP_uCF12r2NGQL-_5Guz1YV3u4C-ECu2Q_C7BzuFcDLw8RmDt1aeetqyWaHkz2vjplyJeQesFLurjFc-5vVFAVhIe8kyzFB9IZPrv5JHPsAEuGFiq0HoR6MjFVzdl3Ytq4lI0OUqsB4lUcm9HAshI5-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je-1nVy80YikPKMAMCih8LDCvO38SC2CVR20AXQTxfS6BWr1kTalgUCxnbOds2rJjt5GFBwsMW02IRUFpH2h_1z5JmdpyKnRz2Lg-6U6l3HDZ6IeWll6lClLZX1Nz7BVHzbpEzvq7LM9Uwv1lvQkRL8h2hVmdDky1EiceQcSHR0XJ6_nxDDB95mRSBp1-6ciTlWFtQGEBXabs8XQhx72NFibvXPfRG35eADf8h-ttmSFJU2dhswopUB44vJqcHaH5xwiwJHlrInWcxP1QQUr5YtceJ9XNo0_yFokX0d0uL-NG9UAKlGyfGX4Zj6cVlf2T39MocGPe6RAjNjSTXbOxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJwtlcr251QWsABm_VzRCYoqy-ldacHC_J9SJy_oDyWBh-hPq8QBnOjqGnWidc3L_FdHaD4Q9bC43L4Hz9J3Ww0Yq6bemq31ikNxsilUB4bXaawvhfiNLcVom2WIE2hGlftBIPiWusO8IDIp5d_womUqPoq8SRR8X1Qt8fzCXjmQgZ8rGzM3-5aSHw_u-thmPZF-HLxk3v809_u9vZaNsnwA_q0xO60Z67V_-otpM2AN5ez1U9Ga7dlJX0tSDC5KhjDcqbwtq8kVwYCQIC6Pe1cq3KWpgs7YBqeGLn_HdVLEy1X6g1-S9-VNEvhcLPqhSjg7SZgbUYpnhW0E6lXdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRnHqGr0TsEdR1TBJrVc4WM-NW4bxlT6vOba0Mh3hKMJx024VCsxtGlgEXXEUZPisBsp6e807uEN7nA5z488T9uj7uwbcKwVVSY_pfwdawb5k0AmIOJavdg8_b1SnedkKgH6nToDhXjfJyBAfnGav2fxslfxtVhtBFoogZY1FDx0BsIUfdZGe6JL-VG00dUQXIb2qVyXSIsdFnqecyng0AQLqcCXTm7igUB1SHMY6B7Qm9G8feMssgLqc8pbYtvLNz6rz8kUxw1QLb-dcDNI0aoSyfJFu9qy3DlR2JFmUbxaP_vqXm3BLyRy7Yx37JaQTkSnPvrXhVC1HFMu8pFt6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TptFYC5MNiQmVVpwgJPpTkjwyJOy_bkSR1RFsfAxq2iFA9HMh9lsEIIywyKirEygYbPWLZPEE0KNZ-EHPeOMj3thYxQbKPI9ydIftY8t9ecygdzI_YLI2OpL9dXt1jip-IZkBZH3p1pkjxmGEZisRraBVzfvNWB-MzgiAVDmbO592oiNaxEQAxP3uD1IJIBooWcJrB_H6z7WjQshtSQAl7zg2iD--oHeQOiCqsxHfzrDXeto_OPERIbK7KxV_Hi8Oe0rdpW1SajbrgfqXDUWl7Bkafo5ZQhDs4DvNNNUaV4t6zP9-Cbixf-o1P7C1FvINfDIEhgBAXdzgq7TGyPqEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZx0yeo37Z11LqusPRpeWui5q1_8d2bplxBunWLdVmZQoMFkC8DlhwvfA1-GwrqFDYIzlxyuL2_8n1XvK-LLRL7MAOc85E0VoeVcLbzHO4oP83dh0o4CvkFV0wXh56ukPl20LeFXnsEtMTqKi3lNnhCQcFeHtQvwKnpGeu8GCs_-bAsgTuyIN9wY2cJ_MPpx05zNeY-69uRRQCxKBMigwn-EtIa3aqpuKu3FXsxGFK66JQFafAfPGa73oq0Me6I7sRPj-7N8vSTDqi8QtyB5g8Gbso5ht8LAwdaP26fhlXpXxVO2uJPYv9pEORIMGX9uNtC0rJnyveHWJ3kcoRxIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJSmqPxVbJ_wpwHbkSqj54v2IWLLNKB8Ci-3Xk-xFXF_HlvK90gEnJ9e1cJG8blm3LsH7-pEA07vb3AzkzppOjm481WfCu4_AywT2E3yIdgLoOMBDLCUBR3N_cKfxRArC51qKjlPm1jjf4l4w805ew1btgD-937SX2upAWtdnhlLgHl-f5674gMqCBJF8zNTVg7lvN9MpvlmWVKJg-vlGQkkmFUXzLWKQis7-Ga4aeqP0r1RAU1djU60loAMJP8f_uQZMcHWkZ5OHOVL_2tWz2KVK0EOAiq8fDnUFN5IkSb-sw5KMpExqYiVcENVMq0BQQk5KWe63teE408hUEeAZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvOPVq9KEi1ow0XzaH3Lm89WduJaEFiGLLIJjhakrKzpf1Zj-HkBRbMcov5tVKSiSCEikROGsUSE_t1bLTNoXCwGlnEtgLSkdFRH03s10zrO0kLi9-EozUS0SLxKpo2oaxkqSYJECXoONVsKWkE0HvoAkKKAFCtBUix2iM1HtUFnAXm22TESMoJs5EwcNNG4AOYcZgtddCwytnleVhSk61L7i3vb9dPxIC2Cn-wkJaqoGbq4f0yRrEO0-KVIDdCipE3flZPc3EeMWzm_czFT5kG5Q9XFMjfu0indVnXy744PukyHjqDXg-BQn8tAbfVh7Lqu3YUBlHR2pPnkaa3S2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx1Zn-WKw4XUPLXXREl6c_SziwhWBp-S5UQ-B7M6QLkx9NZ_3E9ajrtT0DO62yJXfzFPJnhrF-g4WZpt2OAtmRhrbjdgSa0Z5bEN_SomoUhjqVoOgkkCVYbtNPwvgsdzRMddrAp7vkQBZ9OMl-hFHqvs4-zXZg4JyH3hbOh_aHJESj7RKUQCm8RgHRYEEuMo4uZjLs76dxesS8zkeN73EPUZgk3pSmJxaIqCDavExF3smIwkC3njLMJFv_kCQlLihZW8VY5Ca0JAQxg5VSBtBXTP4QV-NVPxqktgwvRUni0MLWDK9CWXT_4exfjaiTizyts1-SaAoyydUJLXbIT0DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUATpmOiKbfp5S8uku_NQc1_Ty3jBoHjyOsbA1plLeQvqDQ56xHZpDaRb8mhU0B8Gv_b2mgRQtrM0rXnz9YpvnwxHntbtY50MOyOWURzL3SffmJuIsqZL6sQH9WWo-oB5c9t03f7H75nvmAXCqLEtbZbibKyihIgV-ukdhBPUQsuYggGzj_2Zra7xgC2qAp_nXG17fdZtRVGnFykWAmt1iugzK55niHcpiHmzMAx9kZFOiKnAWI-uEPqIVJ_9t6UQomr7RaxlwrSZkH8W5rNpqDRoUMZrBJZU9VuWKYr5xikOo5A5vF_t-HA0woVY1_yZZc3GdwiZfZiB8hWIKvKRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghDWxeXkQEsSXdhIUVHZIMQgAfYgsB7OfENHp3jgI60dm3opoo8zmGvDtAqYIJf2FiLPZKvRz712aAnjDC0EMw2r75eKhbjDscepk_Xb0gZmd48pmd5V4Dv7ULeXMrcREnWV9IzNTyfSN-nrBBPT1PLF1S5XAsvdQl51Ypy1Of4dNYnTKhlycqh3j1Cgc3aT-XFNFmURW2x8EsP9S3sQEtyYOFz_NOYhumnmTyedhcSs0zLJu6IXaS_QW8Y6NEFUEifRiF8jXhaDdJiEvsziWb48-4SCyfNyYeaN3OMOsy5RlzAUYoDrFj2Uy6OCI_VzcFSrpq04F-IigG7aBf_DTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kosNgJWCGedlKxdwG-tXD64KY_o1AyFOdBm1-zBW9e91hv0ZpEO9m0Deew-BQtsjl7O9w3nA77fJXh-cvh8GLYFlEJkHcqqMRYvqLClLSmQXO5H9lmJgC3lyWC0Gl1WIfdGnKlKwiy7YnUS-C4muqgJezkQtHbkdyUMGpmkSTwy__r40N8dKTdU23eXW0KEmqcrnKHLcynt2CoUvC7lYLb6t2MHv0_-aWTtyn0irVf80BMYeFQGKf4f8lRGyKv9mRXYtWjkWtN7W5RpD5tN_uPZg8NOm0eoNSMZ3yKKL_F9yn6xd6fRtSZmRZqubcB_v43zmC6rcIQlHvgc-uWtZGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggY96xLmyHp8seC-bxB_hmOLk0VeenmEs_dTHmKNKmpAr1vZiuq_sITIsBigEBsE_B2Lyqgr_L_1HyFvEs2dD7_O1A2ArvdUAtxCdS7dHlVB8Iu8dON8swm-O-_Xz_hLCZoNlOPHHAp9ogmOYpk_1DzljF1Z9wS8yfAadH9k47cOGdFhPGjlQS9dTWlsYHUCoS5vHXzNmnIYD2wMsZ6K-0Tx8LhsBxx0YhfPCwgNRC2GUUZQsX5AFX-6cxn3WfF3qE77OlQJ4VSE34B-u2Xz5l_FUarXIJ-cPG_CboZ6DxrVVvgiEnKyBpwWn1ui5mlQJpv7RqaJvr9S3kPgcnY1lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJspUcAeRXlI3weqeOwGCLWuko3Jr_3K68vtGpzBeYhfwPQG0lWC7sj0B1PxLRQg6o1ZUxonGlFBYlrlCJqxy_5IVy3rOt-IkwP72u3XDPoOWdV3dJNsTMuu8gUyfZAe06lhhYez6p7R_iaiou_TuHo_HuGotaCG3ZBvkw1DrcheMccBXv1j9NHm7mDq5-akG8O7fp4si5G4sAKgQY3QNgvVVeGl6HL7lrYcM2z6aEFP7U-oEzUDvo1vzP-vgji7q_blW6XtUd_riG05ovdcoCjt5M7zLgkyZN4HoLSqLLlCOWsoqoZnIq1u3gyuN0x8_SfVKGVSohFEVlFU-JKejw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_INEyjwNcAXS8zeSAUnoWbGB9IbLjAP7-Q1XZj9gyKl9qvnSFNf21OUWIEGLhZiEhy5pNkOujTByp1aAfpFOyUc0cUXWjStNjnspgQhOLAa2KlY3t2Z4ntZkl--ujzkfe_viz8v2rjLp5V1nkNX2Kv0meB2X6iSagEGP6Sblx3ld1R1wWdvkwdKbb3P19pPyJrPEvhuDzSIki7U31Ro3Z-ngD4fOInKad6utTCsqNjhaImsrYJ04qfM2HYohzv-0KsZkzYZVtHL5tUsXaLHG1LF34S43S_cJuswFMmD8vRkPiecOK5_Qmd3PzNeYT0mNGicmmwf12e2to0_MBnqjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h53wIEDehKFMO0nCvvpsTqTMAQWZxytGqHi7xh-uh_lPAMZIBjYj3K_WwtYtS32eJdUFdta6s-OaewoZKfgOJrpOF9hKk_dtwOiDLMyAb-JfJi4EF_uhYyW1oxdiZqF_eFDE8vvi73v_GlbqzPxurcMwqn0NBr65r6nw3mH3DaX5VJMqSEy-J-1H1aFK2a_TuSksi9eV3tPKajjG7HDOIbV0ec9Mkt7xZmu7Ph29gMvE392vSA9usFlb6wdlqP3BnmvtLmqpKrAkZywvhGpxJpgPcFqTJ3qewdEb3pGEir-3irclgpefwluQFTvoQInKV4cAHqaS0CRN7rcX5l4Zmw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=I6YzFPD_S-Y5C6K_yUSY_RTUMxaWK5QnvAh5-3V_y2IlE6psihsSCO17dqNwN_rM-OdDgF4-FTxb1o7rMDuAgPgNQpQU0mFfLi5F1L9-hh2PayYPJMLQp8drmNKsxhMLLuvUFSFlb_53GKBSls9gPwMjiJ3qbl7TW56Elbcht0IUquiIGc23CRIHzdvmFXin_ceVsZBihdxBL5cV5l9gZjo2gppsml56BN0IhU0zTS_c5UBAaksWi77DzULPCeQsfANbX5z0BMy_A-CfPE8INtuznzTzDXPJUqRWvfnV9Yol5Qrfk8F4q-3FVEYj1x5tGd943XyYt6tAMD3y5E9PNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=I6YzFPD_S-Y5C6K_yUSY_RTUMxaWK5QnvAh5-3V_y2IlE6psihsSCO17dqNwN_rM-OdDgF4-FTxb1o7rMDuAgPgNQpQU0mFfLi5F1L9-hh2PayYPJMLQp8drmNKsxhMLLuvUFSFlb_53GKBSls9gPwMjiJ3qbl7TW56Elbcht0IUquiIGc23CRIHzdvmFXin_ceVsZBihdxBL5cV5l9gZjo2gppsml56BN0IhU0zTS_c5UBAaksWi77DzULPCeQsfANbX5z0BMy_A-CfPE8INtuznzTzDXPJUqRWvfnV9Yol5Qrfk8F4q-3FVEYj1x5tGd943XyYt6tAMD3y5E9PNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUc4PYOnGsGA5_49DwK2FhdVURlTDNQe4eKSpH9yRXSJvzJ4B9_It7EBaMdPhxQyO0sGqg5r8mbc3l5IzTQ2ICX4su4sUIUWDpzyseSBtnRjdQzIYhnz_0mBvqkwZV6P17ObOkMCTkUyA9QnyWcCTcwFbjXRGv_aZfi7QsKS37rzx6LOuwwVf6o2zVepau1Hua-QKdTlCOvKTnkiN5D78CVG89AE1LxZRAhvkLh7VbQnx17B1BXpp6RYX0aqGlbBrEUVG9aobt1o1wS9b94J_iV-4hSBoRbN4qKmgTV13BX3fnX2baKUyiuKpOGukHMgriesUDeHvb-8lGZ8_PllFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBnJtUZermhtGeQIciR07SyL0LYrdThQVBQt-WQv7ZoUJS9ucnq2hirnyaGkexko7SwO9nTwisiVOEQAik2huio0OJV9liP4otr5q0YKFCkUkKnFaDp_tboyI8Gvdk_2gyBfmaC22wJjmGSkDOHwXzKq7PoiXeyvxvT3_JfEKv9IVrsdhkFz2nBte9sNaV4ZG8aW73_5t960Y7ZT1Mx8gnqPIePvmQ3Qk7J7T03RJdJSDmbpZZv7gU9W4ykjueFXtNPxXf1d69Kfs5_wLMW3Dxws_RsWKhlRGcHmHOA-oO72BQQJohGZp4m1rOuDBqr-Y1D3KSyXozG-AodPCDnXSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJPQD_HIrV-C5uu3nEmqUjTdCh2Mq61Zcyfi7PDfuOA9dJ84t3cB9uW5_CZF7lsWppphx6frUN0MH4wz2_sCR__ATFfq1GfpP60is-yZz7W-yJranVqrpfKhDqbOnGj4UlroppP_gPiFO1uR9HJTeZ3PbrtatUxW28zF69rZD1Cwv9ukQC8WzU7y4Gfpm7fFZ_-UTVPIj8dGCHdX-Hnh9GzmGVmNy-DPaOB_GGRyQ002Bi0UMLR6OYltFxFeCB46-E6vEbRwmZrh9Tk3iaTpFTV37aLAEOCSh834rz8VliK4KHm9jXgWZDYwPwANBEGw6fFeLhRqrHqvWeNGZ_hK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAqLWKt337Ri5rAoGlvCJQmBn822F2kf_zzFNR4XAVqULTTzZ87YBOM2_NBIrtXJ2FDMO9oPNLxtGUAFikLG7ZmDhYLGU-gNkq2o2azvREvaBlSYBgMfNByPiPV-t3Qok0MkmD7_bWTl7Tbq6nUTFG7HJoSJas1WQk80ASAtLpVQOkWL0fmENoHngVjo-reDkrzbthuT9x05R6t0v1NRMqCBAtYeFm_Q01Xk-AbKIhWA96k3cfhM37jHSxmwcnyeMlMALg2YjKd4JnZt1adaOhlzsnV_58Acs-5tw6hE5R3lMmJ-4ePBrJGon-WhuNoQYwOjmaybiQpE7dVRK60V0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0Sww2E-emKMiDykqsoc4Zy-6p-I83vFl0XPZO8-n0UfAZcpBqhoVmQFr2AqZNUaFDIHiisReEKbncV7oSMol9nhYlEl0majg75etHf3mrKWpz6WImN9Fm1-HyQrRPnMH6yWOqidMwUUBRg8OTiJWqtg6edV6xyr-rC-QkbssLcTq3TlMUYo8UGrTuen050FRFEaS3DPk_a3ylc1gdLBfTxuNdt2Jq7AOVY5OM6n8nLC5OiyH4Wy4TThLoJYRkGzxiUcKb7glqn5QNLmzNoheJSDCmYCL0hMOX2qtsnKPCxLmRS_WkswgvBMYFPVy6wmjWpIJf7WE3TsOXbaWfGKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fodxse3FC-OPYYpRCn20ywqLWNsnYq6TwmlfJxoROXIImRhQHiZ--XTcvHsN-1J19a0s7z2srn7fMSfjl9ktQHzzVKqJrvXKuhtq7XLOGZ160DioJVwNB7EepXWOe6tiNw5zoKrL8LIKcia6tjfDWh46Jz6CSxtjCBHVwNJSwBJX3uBg13c1eJ2uGFleplpcY_eMf61rkwKIM3C5RgD-pH406eTRHDZwhmoOXHJQt6FK0DLkEyMBzg0L6QJcOIT5ZCyZSfe6hMkjKFpC-2gWyMeRHSCZquuOrK0SSO2_RAm-NfsyI820R7RQuo-D-Dj6Du2atZbmms8sJ5Xaq_2Uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrTSpjT2KPUVAlVV6vcsoeoPD7Hnbeh4ObMo7rH2ypgx7VgaBAF4cIUQZxBgAjS_sW4Qa6h017mXANlxtUcoQj4YpUg-igptmb8ZuyrQaTTIiBQ6466Do0VjNyfu3ZP5MF4t1TyCIADVcHJDPjlxEqaVjHW8Df-mXzlvW_TcIw7IpfQk2kBrpyEO5wqF1dFTQYqsCcmMOHQDhodmEfpoaFhRI9zyEtnWyG6GxDR1WfuU3urdFRs89_uE9AX6Lmnucj1TwgKdeHJeRr5iNsgb_W7B_ziThgDPJXZNy1USbhxrshHTdtN-dtGN4TreX80zSbyjzVsfIYwUZQ7IPRJvAQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=XQQkLDxovGUWZAThbBdyB6zrCHKid_XDVsKQfqYYbUUGRj1jLAa6cPB82CdxihfNyNC98jLOqn6vdQESAcAkTaVJIPFNymS0NmIbSj_C7ezR5DLwtSbeZWfCz3iZ20gf1cA8uWPDMtiD9Rcamxh3MHJgyFtb1Zq1LfabSeEc8K8x--2iCYygFl4UqZN0toMt-LeBWEt_d7ZrRaKVBf7m0fE7mP3-g_jdhNM8JxMY4_p6ZFvVeKIYfp-TKEadz7ZP092Yivn4ePeaqF1ANIy6c660jxHAIhEGIU3lFj4MSlREYdRYw09yItaZvJ2lXJYJkRsasnk0Kdi09iMsl6yZcn_THR1yw9Kgi5G_BmUwpUSvVRaiIAF2fX62XTNzqlneRg1fWqYAgR6DvcYv9jofIAY9T4iMtz2PlvahBVQaF1-twXCGIMkSBWzRtVDnq_5ozsEk8pmSsaa1ELwG4A-ysOqBnmUTN9e6PHVswgJcG-LBD2gIdyeYWam8PNgPw18POS50p0myrq6ivJehhgGKbo_mwUdc-AIl8YT79QyMAMaJPzVPXQOOwvjYWskQXFREhmY70kv2UMBUhxL3wnx4F9QN0GqFqIeA2taP9xbWNhUYvfhFw66K-K4RhTILxz1E6b-HTkabnaz_TSEekDEie4eU7APur9lpez8yJj6t8wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=XQQkLDxovGUWZAThbBdyB6zrCHKid_XDVsKQfqYYbUUGRj1jLAa6cPB82CdxihfNyNC98jLOqn6vdQESAcAkTaVJIPFNymS0NmIbSj_C7ezR5DLwtSbeZWfCz3iZ20gf1cA8uWPDMtiD9Rcamxh3MHJgyFtb1Zq1LfabSeEc8K8x--2iCYygFl4UqZN0toMt-LeBWEt_d7ZrRaKVBf7m0fE7mP3-g_jdhNM8JxMY4_p6ZFvVeKIYfp-TKEadz7ZP092Yivn4ePeaqF1ANIy6c660jxHAIhEGIU3lFj4MSlREYdRYw09yItaZvJ2lXJYJkRsasnk0Kdi09iMsl6yZcn_THR1yw9Kgi5G_BmUwpUSvVRaiIAF2fX62XTNzqlneRg1fWqYAgR6DvcYv9jofIAY9T4iMtz2PlvahBVQaF1-twXCGIMkSBWzRtVDnq_5ozsEk8pmSsaa1ELwG4A-ysOqBnmUTN9e6PHVswgJcG-LBD2gIdyeYWam8PNgPw18POS50p0myrq6ivJehhgGKbo_mwUdc-AIl8YT79QyMAMaJPzVPXQOOwvjYWskQXFREhmY70kv2UMBUhxL3wnx4F9QN0GqFqIeA2taP9xbWNhUYvfhFw66K-K4RhTILxz1E6b-HTkabnaz_TSEekDEie4eU7APur9lpez8yJj6t8wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEEntogU-_9Pth9Yp99K69df-jO7Hklmh01d0jHC8DsTGWaNJqYW1_a2RU6pGTbTVlBurXGarjxXFrTduARgrtz3Z-MfnCW-s36ESZGOKQ902AZsovp_w8tyS8Uc7ojr7pu53V1Ma1NCrLEHKNpba6vvtpvZxAdRDokgf-fs_XJGneUb5E8OsToTVxSSHC_kBshdrrdj123xBxn0O1fPEB-De91rTF_L3iXHM1RcZPakcRadt2qyIeYEge76_L_2WE17qClR77trqwHvXBhrs7MhWejIKNx9gmuAMtgbsTSnKIh2PliPpQ2ZHt_ptJui_pmZeQIsYlKEvPTDnREI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5NPPQMDqmTLpYiM1tPxvx9LyxT0jh2cWrKzGphIoTkLSviWG9ibONzcy8uycj2srINYPd8seiIlpsojAFZ8JkLJGjrQvC0iLInbOFC4hkGU_4WAw2TTDVcjP0NO6SYvGgubKQSas1qY67V2Uc62dEwEeyKarRChYtyEJXzoe-ABh7Jvsvs19IDhlukIe3oPIYN2g54rgbwbFsa29oStmapIP2ezm_JKXr2dpSKM0sSEyn8eEa1MFNtGzCs0X_SargfQ-8Gd5_ygcD-l80fjsMsirFZtUHd4FTFRKe5993NAVpWxUe5Dq0XYUEYP2QOt3bntcbK0DKlcrsiEUjooDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHjokPuAfEGIqWXw7dUQXax9tFZY-71Lz6yiq0H4hv09HY0HwVVMJDf-EiknaDkiZYOWXpIWr216TrO4coF-4Thhs2g14ngh1iw2o-69LIZQCG551fepZ0vjXBrPAVKngViPRpp0Y1d214Y39JztZD7P-OhYOOpkWYt0fEmek9l4pjlfhSFhcjby6JPvgEDlNZ5UoH-aQrlGu-nLu5vBK5O8cjTWEP4g-LwIVgiG4C9AVxd-14Kh0r9Bu9bxbVq8bjJ6L1dph2AH8sHxGnfDEfWGWzZ53_OzxdnGlz4-si87Qe6L3Pj4e9Nr3oNf0RrljG1z0VmieDasKbcH2edcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3jf5yEyTwEMikXH1cz3QYwJmRX33E9LBw0jF_84j4iazxfLsEGiggFP7NIE21CjZ3WVeNNPEpdA-CKpdIB_P7eXCB-4L2Fk2mrRwqYYhsFTjEyACVegB0gRPfsfGzFqxlY7bOul4YpWKVSCiM_xTiddFLxYEHEh-HlcVIywbwhnHONBwtEnqaCAAtm6mei9er-9MS96MRIXS60xxZNKgvNmOo6ucwwjY9t1F0Xh2m5K5yM6O2NnmvKlbSWjUbX3AoaPRvm0rgNX-Ryq5EHVbEnBRAUK0yhQGjlKdrAjNEsrznKyFRCrtAbNzCC9Y_xkQvFPG9JlHkMUtbT0uBv4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6fOwfbDX8O_Cku5wuvHpFjksOBdpWKfnnRZixzpthOzMdasoF-CckY2uq6nvGg1s2xlgoYA2z0VroFksU0B17od8GtAJ3yH-HFe1ZkluFyXuSDcA2cFInb-LE2zNFvElZ7932x4S5BjSgF-ZcrMA4RHKQOBOy2Y8LksAxZZg04PU3sBdrSNfXX1fkRyavMLI-XLJ5UKj4mwmPvLYmtODA3Q6D_joy7qtCqq68DQJ_lXqIG9PpMiOF_RbF1LHsF5ML54fBG8z3U5kE-MnHCjp90hYs5x0-jIyke7dAN209A2YCYN2ZMtL00Hm8TFkb8emjVah97TlURjzefAHuyunw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UQqUEXyIhFdxQENbHixApGaP-G9Q4pRL62mRHFlgfvb4FogwBtJp6cJeBtlUxh6fVDxMOQ8xKc46HBpifJIbQ5Nyq5vkJ40DIsezNkKejdRiE_fuawaivOGg-5Qr79PPO-ybBy1eB1gCAWE2v4Aa0H7GhLOCwl7PJ33mBIl7ySEf4IDAwimGRGsShHmnbznYQePZmdD8mITutkNAFwarvWq7wCCg79IvZx30O598Or1kAYYf6AqyjZ3bUPL6og1LCFZjWTwK5-t64g1Hz9Fo7zRU0bx0xBQnu6dli0fQzVhzcNHqdGCTY5XXxlMH7BwaAkHl8iVp_X2z0AojXX88J0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UQqUEXyIhFdxQENbHixApGaP-G9Q4pRL62mRHFlgfvb4FogwBtJp6cJeBtlUxh6fVDxMOQ8xKc46HBpifJIbQ5Nyq5vkJ40DIsezNkKejdRiE_fuawaivOGg-5Qr79PPO-ybBy1eB1gCAWE2v4Aa0H7GhLOCwl7PJ33mBIl7ySEf4IDAwimGRGsShHmnbznYQePZmdD8mITutkNAFwarvWq7wCCg79IvZx30O598Or1kAYYf6AqyjZ3bUPL6og1LCFZjWTwK5-t64g1Hz9Fo7zRU0bx0xBQnu6dli0fQzVhzcNHqdGCTY5XXxlMH7BwaAkHl8iVp_X2z0AojXX88J0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK4V9XY2tUK-t33ha0jNz6qi0IVn9INKqVODveoS8FB9_n-0bq5DyjMBGfomVl7q9OX7nPwKexUNNoWtNr6-KePplSuFqDPw5qGi8o8OybX0o7Idstl14vLMJMKhpqigB_Gua-t4rQsW1BVqueUgmUa4t49_vdhx7jbB2eRuSqHtE2HG7XLNURVV7B7HyYsgyT6c1ZF1HQOrYSMqVZp26dXmQhdrQU5JmZNcWjk04sZY_1UDC-G4n-5hIRgSyasdjb2A_SE39OlL76vtyAwE_SoRAFhrtbTon2TOE27FG2_y33vY0RqXEU_JJhWd2laRFgIKJ1KwJifGt8tkWnkB-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEnW40V4HAY-_E9OmEa3TVHz9iFz0AhDucayywti1mrcaniHdA7D6NVawKP0NJzE58Bl88ihjbflNWWWogcQnQu7ZQPxb9hyvivlaaXbOjeFXS_LgGnNEDAWhQauyGpVHRwa360-N20jONNMQFkb9X97UBE4CNiC485Drt-URFena__1b9P6OiU85cq-sXR7-zAPWOSeKEtSLNZleWz714CY2bFobB2j3kLb1Vl0lLKaus2aJ-CHs3dh_Kla4wqPYdNu6kNXtaZIUMD6-l1bQtE5tTGthxjfe7yc2shZj8abtckY6dPTpqUtMvMPxGtATx3omsEyrb568XIFxd_xyg.jpg" alt="photo" loading="lazy"/></div>
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
