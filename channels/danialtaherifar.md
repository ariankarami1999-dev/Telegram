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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aprgGYzROiYm6hpNHsTlTsGk0XOyat8kuS_mmfwwgrmDiLRCKkMkjzX0xT-th6iJKHNsrHbR5wn-3p3KE6wFC6GQhBO_gljOJr1lLB3vL5MP453bLJ-L-T56tz3krQnip3oaYcZk2YTnx-p5NsCGttewXq-mkJ08061pRFMPBsWnDb7XymV-eKdV0Q5v8wv9hCCIW2HfpTkCeSW0WGVTMIaN23apULqvrkkNpX9GEelUB-EPorzsNqAqKh402XNfs2s50lh1L32jblmpmW2dy0_oC_F-moT6Vw1H2pwunMs_GADWTc00jEgAJ5uAK4YvlaMtXI7t6l3BTcN_bDHXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 202 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 447 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 628 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 595 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU_qQqRr3La4PuITdlGmWB-Ndwq-DP1xpEUZiDtD5WQ3Rcv2zdamYzBf4-9c-g6GinaJtobc1ntb8eIZDGCJpYIz5g4OFnzDdmmvuDu1IstSBqimh0tapR6_5qiOJo0PAY30ZmrfwUiNyCJ9w5xusiKxnVCRMsRtvZBWqggRXo3niCkPRikgE6NVimkaMmo-2BHjELG6OvnAZ-LY7Y2kJ5JMXQWnes6I2ab0Fiw2M9FjcjlzhDS9A_58ISq4LtRjCCE7G0B8Za2Zys1rK8ckp059LMFub2nsfidN-SL9qO4WOyZQpgrD_Wr2zPvHOznycXw9R7cVqpK6o-i6zE3IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9lcXdWHDxe6YTO3HD8G6vT1Mm0cj4Ual-mvisOIpXTLU3TivfaFmflQVSaAzJV0tLZjuI_Wri53HLvJQt1dMjyG4B8DFB8ZO7Sj6p9FcOncwjgzl8vcEilHxEsaxTJshh--QGXfo2_6Ze90SCTk6ac9jP4yn-KNFf2EN9Zd2tylqZL3pkhfqnedDxmQZ5LYPpHoTn-BaP2Kz5-ciZWiltBtbjRsIvE5u3dC_rUqjrpWxZV4tKQqgXpCMr8-vQMzO2GYP8KuHonF1jctoQlUGsVmeAgXIhhZHd1BxXhNulDSmODCoSgiFqCcLEfWgNJAvv2yd7x9BuLHK-xYiOnWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP6hOTjN4VbCWrKfLF77WHQoWpvcyODzP9pXZV6TrO46GNWL4rl7nfEM8y3HnYsRpgTi3ek0H4U7MDeM7uewLElZkabF1-pwGCF0atmEAOJMLjLglQ83Llj-w8w8G_8oqcD6uRzalWYKT8chdZSjHgBam0tVNnfnXKjcfAQoq_bjDvbFg8t2J0XoWO9yEi-nxUnr8-wrfBjazTfANCehUx0Eo2-uyBmmqTNrK_YMglp_5hEoX2rU_qZPsk85IMPuh737IB2GXxLBBgU4NDHVXYBEHhXHGoT1ZvROXt85BlNzUULwtlBqsPCVCqWknV2meQVud3WTvM59bN9PLY8C1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqdxC_DpxlCoixuBV9O3CdL1LIwzlXcRhYG_aXktLmoj9Kx7XP6yDks-1ZY7lq5ep6x6YUolN4Bj5Xf-C9SSIzqaIlvrC9xBGtWjFa90gpQxFiL7QZqUzdhZv7dm5kWTvqygsRCc1sSshyKFDhg3qHWBd2IAn50SoW3FJomUdGuKHmE9ehSEl4C_jOJIGddCDoY1eRzdWokmKQd32E1ItCdTJnDd34muVXJzJW2zV5NJF9L2AxnpoaoWgkKsYohBCYplHpROXh-uP_N1DV79HwB0WOqZndPhZaWKPeKDX98DhsDbkbD1rh2X35xjIcG5TeSAAr-gd4W80Y7-G0CcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6HlufQxka__u90xSN8TufxBei7EOoODwsWzTXMNBOZYQsb5gVd8Z0wWeOj-LSkkHsE9V6dvtQ1IqRQR7GVoNhhcvZoRGryhvp03wmzhj6ovokRPQBjeJomNvYM6eAsQIzeh_2PXOLb2zOCjvViQu6SGySoehDEclTB5fXFCR9tb2XT8rkHILAEFkinuubadByj2IrU4LzD3xO15jW8ItM4oAojv0qaqCCJwej2qvjS_Y3XFzWbdQmu81pDEBmKA0CTdlpeRvr9mG7PtpT9p0ABPIi7JakEPE5FJcxI57Joed_5JnUu2pYs-fGXAqix3U1IUmeSETot7Zy_F26j-sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/My4yCkVV0SrnfaoTGRJNVp9Nu_o8y3HBL34JyB4oF0pXIc81OdoARHdgbtGQuuwTAYc6Rwd0W9Vw2Y90OeGibaVqQQz8L4HaypwwqW-8mlcc7eK8ZOjSTfYapL9y7u2uGVO9EolLuMAYBK2VkcsWcSs2NwHzOfobMLoB2I5j8NOzse2ukCHah_wpLIlkvkJEPlM2mLrp0F6IjJDDnx8lEyPo5XgmZRQ-J0ZO-hUeDUYMa7QS-1HHJAB2TsKgzK1UaPyhjzi8y7Qf3eU3Jq1HsPVLWAunt75odGOOBdaG8_JmdHbQ4E54L5zNNws4BeGpd42pCfbiUONRKWc9kO0Vcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxWm5APhAkAYt-24_ZqXnNQwdEFv1Huykn8TS68BTGXMcIdewAtFeXnHpypS5bEzmsOyERHJp9hqFbLnRAk5Xu55py9IeyKsVSpzbFDM_j1216mPvOAD92Tu_LIO4oEjoQRiOLqpa7ozHL2s8lbBTNvDutnNcEJrrcWVprbKu0xhgpU1IO_vb5TCS80RySvD-HZpNGd9hQqi28Zuh_5uITnRWlpIbZVviwmB1-qKtSP2_iRByrg-zBQww6HzEW4SmqD6mW7uEcgOAQbdC_ErjIrGoDZ5MoSvjsdjp_T3us2lZUcQu4JnYd1FZ16v0pFDH2xadU9F1oalQTO6JBmdug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTp6RGN6mk2pvrpkkVrWnWhI4_JnIKaMG1rYXSBJqkUCCl4uM0OAuaIkmgdyYHLEFguK3eluYwGxJNmRTyR7D0EfzrC_GOBHPpLgM25DkJml3Z6eguAXY31sKy9SGsID_72zmXKIPFWxLWhvr_CU59yx0kQ1dxqJkMK8fXvuxga88UCaQCKqkLgxnpFjYpjRNcmTsiX_gP3pFxGW0Tq-FDqXuxl0TGeXr8B8HlYsIPYn9si6FS75cs8iiTIJMpgnyvlPCf9iCNA7ppJLAAsqDWC3xW7eYqhEroiqVv11tRUkh7e5G0wCp2iYcAHFbmQbIoJCvREp5Kjf7q8BDDP_SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhdE8EyossBpNiTiYU0eqhyps5WfjvRrek-9P5k43S7ukfmuPyEBE9VphuLey3LQV849fhT9OKVm55PBLXHZtlV5kiyIw3j2HBjbkuRwwPoTOML27BzGiTrnguBZUriKkGLtebK1jNSVQjqQdPTOXV42AiV9J3_m_UP20-1CCgoW0k_ysyu0OnPVJ_-nDh8qH5q7oo3L2IQnEz6HEeagUeHwQ0NBaWMe4iN7vVywlHJA1uw292ppWDFsSXvXRFe2fPhyAdF5jRbADKL7vtpjuR7U3kD-PrJaWli6aE_TKjHN_tvDgCriaC1kOGqGf71_mp3xvSDrsBPFQ4lDFK3VGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmAp-DdGES9gF2x3B7TigZS5dIb65sypbioT4L81G59oSsw7D6Cp9y7-0PyKix1x2fgPLeUPgiuJKg-LMvPbuX1UnLtRxXNK-S81PYIYnQ2yqVw5lwSLSkNaK9ideYvuf5Xu_XiIa_kyMG6Jsq8d1QtVacjFDZa8yDL8fVjpsAM5I4Ukk545SorYvupuIuiNqUXUDqzMUb678gZY45YeuonmncJOkFsXSf_vx89nKZVIvSmba5ZF_GOChhs0ODgbtwOYElxELJH3VyY_gxzZy_3amULhxs5mLzNI66AUdw8VoY2SDn41sCJaJnZLift40AhntK9tJ06xmN9Jdpr7oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1kZj0CTz0eURfuF7mfyi5qPqCUZKKD7lAkI3ZZ1lxhzNXeRKKPBteFa0VN-iI-aent2DaZiLvVlx45Q4p5ss_sqlJxNV7fjVCatySEP581MzakPfURxkM73mxAaK4o1FS46RGdu_GkX_nMx7tsizhn03MWIgBipP4bSs5N5-JvS4tCx2I9TNijylDD84iiZ_sGqv85WMZle-td5vC9fQgEkxDFy0d_ZkfWXpOvuVQplMKyanieQScPlbk-YVU_oDal66c_dfNR9Ov2NnIDsoxhA7krFuQrmbWTZxLxSJcIH6GYs5rHhNFq5OxzfGdF3ga5gzBUYh_EQgSaYEwNoyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9LmGX87OThwrG9HJQolx_rYtfy57ytemkW98ntBFpax4ZDJSEJKNU0H8H3DzDH5D5axPXTwIh0ryYKbFb22EOKrehvN_JkyUKc8klCrM7_1VL3sW7dEjytpCDBXfdzqirt7wNPXjlREI1Nmhvfo7wK1JvVUXoS2uhjudn1LbR2oseNdulP2acc4IxVxnPwIF3SDflczRakazg12yec1ALn916nrO3jdQaC762pj5dVmPUPAsrDF6m4kZMSftyCODEHHgH9vi41x5Cc6-EKNSeiDyPG3R-FI8gb0gt4G14GUuhWK1aeJcGvRYOt-IAaQItgmzpFFP_HnbUGRC3vboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9m9l3D8Y1yH955i2w-iz54qiq3ENM1eBkBoEDD5E40a1atcm3ngURxCr_wxm1kV8KEI1HZrGaMplscXW3M4tOXfaVdv1YCe4VmWmZ0Ug6yWkTc0FtVN7DpN7B-TLp3NUn--l7NnUFkPiz9whjCU9T5I1GRa4Qa43vY7gcPHE29beg_21j1QoKr4iIiLo1fwimGtiYRKDCjQyridfipSjaqG93BfGygS-o7t4Iin2kCzyGR25kcyh1F0mAD_rYaGL25uH72n4XREGwaJltJ7-6UvelcWqsdNxx9VZVwNJ57-glpBQV4xq2rubPji6Z3XjNIx4CzLqFx13_RCHLmB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4mKkXiWQ-uxYVqanFKlR5R53o7rDLI30dzocFxDn3m_cglNA3PomAOVkJ0OhVl3rj47wptSoFo3hAMioc806gnxfiu9y9b7EmJxArijNMFnXd2sEF8MKFCfWuPL-roQMMV7e_0xcL08Y5wgnMFx56Yq-byTmGPy7vnUCwOvkjsndVXOTIhHvxORe5iVEaia7ROPA4wb1hUX5uMLZ5g5xPyiKq8ZqKdtMSa-PF1diZNtAx-dmPcKnz3phoaDxn9AOsrGM9Wm_wIa_X64SfUwGNS5MPtWtu3qdBeJCKVABWwbrB4-Uy6uk-ZULrWbHrBJSKMjx6UOILdAP2nPyTa2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gt1eWox5qH9KsecXOjykVUBPxLC5ZOuObG9t4Wru874sw0SZrSWFR0hQ8cMgP2Q9JfBJnR-KFmmjF90KSyZoX6Cmcic5KJ31AhRstoK5WG6scIFQ6f9NL00LnItaGsTagT8D92Cr0Xj_aAjvKmb6vvd-kHGlMGGicmBgxSU-AWmAiBoU8U12k_vzWzFvX_mmI9Nj_c0yvJJRxynq9hZ8pfTbzI08bLoYB4FHJdAm7RvU7WUas831TtJgz2p5mhULkJDbUHPxLLKKuH3vNLzo8sYqF9Iqvs9g-PTg9yp4YcTa_LJvKxxixaqfKc5-49dhCf71JuIQh01BNSZtdwJWOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2QWA4m0mjZ_j_WiF2QEkgUkt3R38unFjdaY-hukCmwzjS7HbPs3dpxL0e9-vy4TbWnQTd0O0nC8f4pNpifBUzpBS8JIBhOMkdvhdDJ2eHckE1LVIZ32j_nQtjtAwZXbeSyuTBPQtAlOZGDrH7TAeGIwF__JTxp44zip41TPw2LyDbKcscuLJYeewxBYEJ1JPqpXSOtAc6VdbN7zQSJc_86nHrq-OpOKAAa4Ad--CC_ePNFcxbCRw0ARjREo6PH0_gb3wcSGpbKAOZyszzHWor-jAzC_k4fbs8UPJc08ZP45Qgi93ixm82WBwRsPRbe08Z8pL6IyO2peU873dSGl2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=rWU2psVQO-QqIs5aRf2pKm6Sh9ulFNtEZBcIyqBq_Ah4ibwcOtY5SESsna3QlL39nz7M4gR--AY54I2fyGf32v9-xQk9RRCv0QL4M_HwI6p2tBkkNYp0eIK9NXI3ZtcetMl0znp7xiqcTXM5T7RiyGqbaGJjmDjjfS2t-jw6bzQti3upgc9IyF4xAVyDAzRKSUuisJ9oTAOrPbi99jHud0AxBe7oKSzpeqO5zGT6ywldFK8uE4_VqtmSDbex7ftR4GI_T1XsvG6DiueVqenXtZmqxY6H4Oz4cG-O_qXEZF-NlUxX-wI2zC-GWj1vsrbzSDmIgPqdnj4OI0CSqiQGdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=rWU2psVQO-QqIs5aRf2pKm6Sh9ulFNtEZBcIyqBq_Ah4ibwcOtY5SESsna3QlL39nz7M4gR--AY54I2fyGf32v9-xQk9RRCv0QL4M_HwI6p2tBkkNYp0eIK9NXI3ZtcetMl0znp7xiqcTXM5T7RiyGqbaGJjmDjjfS2t-jw6bzQti3upgc9IyF4xAVyDAzRKSUuisJ9oTAOrPbi99jHud0AxBe7oKSzpeqO5zGT6ywldFK8uE4_VqtmSDbex7ftR4GI_T1XsvG6DiueVqenXtZmqxY6H4Oz4cG-O_qXEZF-NlUxX-wI2zC-GWj1vsrbzSDmIgPqdnj4OI0CSqiQGdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBuXPZOIBA9zthjD4WcDq7EuoOhagdwRK3g8SW8WhCgb4xONXazmClgUQFLFWwlgkSOL2LkCgFbKj8rxn4arV-4NW3HnfGol4FGMTO1o1ia3zDYXyNCaEfMYN1AQlhTl05jPBNQsO-0Y_Thno6Pn74nRF3ysSFEQnhf-zbIC54DGVZ70NNH7b8g-NZ3bRVyCGj8Wxd64mYSXiUsOBqa9yImIT8joNUWTycau46bdp_HKv5VvhU8xkJ3h6nYwSES207AprFL0KygKgEKV6BNjPHRnKv7KuYEAGDXwiJi7e7_qDNRyc0UgUhV9mYUeVYZzrsYnqCwrirBq_-RgmR0gmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr6_IOaU0__lEoQggfjPdIT35U8sE8GghngnkGjXzVTolemQT2TCzUqYEVnRpPLf_oT7H31OzqIZ7HZ17ktENCn5i6XpCMlgzgmI_kyj78SBdDZCpLpmCAFywyR84KDV9EBHtLBkjMxbn7ED2okva3UK0rYPVE78h2BHKoPyqJIh8cV_NG3Gh2Vg775PeFeql6DjQTvyIH1lALfxzR9vANf6L-67Uc6U0eYDitsg6yzLL7g_b0kgL0Hh1mif_Uzrm0R1VZtvTsqBgNNvH5edhkowP2Ri4O4PxAlutOWrYmcFZYuMtV1g3w2XyZar3ch9_5HxL4HQL5TfmocKMZTVsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufTpUMkSEtWKnYUPwUwyVfa-YP0iMmBPkNyK6xIiF8rAU_wRfAR2eVRFE8g8oulPBfh-1sbf0xppkPwU5a6Na0l6pAGt6tEU0bFmuuYGAKIBSkhG9iBOMILmxgfxe9oKD8dhHH9SsClklTxRVeucLkGXnDqFGcaHyp4SpIXeda4N7fjKIngWWKPq9gL-LF7kIzqVfP-48OnWsCzf9_RPryG88GCnkm9S7pnRTagjZwCEjdJLM7S34WUe7z5H0lr0c96wHO6OluVKHur_xhLa-YjcmvBPmltELNQj6cveU9of4k78X0kY-U7rJPENr9DWC08z-mPErVviolzw8wJDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqxncZ3MkgYuIR27-w-yqCwp7qdvTZa199a6WLivlh4NCqvPryWC6lyn2dheTaQt2HaIWztI0JKDkjQmxt8XQbQGM10Pbf898HdHeywrtMu8G83AzHqD1lzD4YPINItTym92H5fL9YbffRb9qV6OBX9oJtupRajhquOxTLaXsNsSBf3kxRDhatsDARLUGllZAyjHYiwzfDBUdbln0xmY4N1ztOv19REMvPV_G0PbHU_y-ZI_q1TUyayuZldXR5oso8fLjdY5fBFO5od1b98Lm1iYgVFooC-zwEGuVjzixvZsq7R1de2uIr6rOnGLgRTRyF7oeLz6HSGTLVWsHYQ6Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3STGcqdOBA303lupzg3omNqr4PywiITffYohIGwXoxf1n32DeSELVVbFTqaSuAH6rLb3SRpbOC0fEVCTBmFzWhghJp7yFsGTPvil6Feg6f9ITClKIkQ-KhFf97NtnDxTDjDGUC23RBsVXpku3PX9k2tojpGpdtAiYwXykGWy7jfJCQgg48uc65NXxVS1TmJC7oJtNDDjqg-PhQ_Cfm0kkw8QJGMGcvKnGgwxMEdj39HAmtMFGtyF5MG5MRCMaYP696U6hYryZHzVQDa5XEjk93tZzMBjnp-zbi4vrTk8PEylABerSk-5k0lQXUiqWtg8cKSc2A95f6AqwK6tbauhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwnKZ6zQjSseYWpoFbEywVxVLYiSJz4T1aSXPhdhKFWpX6ZDWrGL2BI6j77HTozRgxlCnuYYKajNVqdoKgsUS_7NPn0DQ1Lc72bxT65wEqiV7H_PoSvCRJdQiLtgFfPkX5ScJ17C2xlODZhMhpveIvNGFeK0-i4d8ZFkZWjA1J6byNUlyFzZISqQr-t5T9XsRhCq_yZJLcSkH7HE5bXnCbhFuWi3SeweVRqclAPtlo1y704fhVOmBuePrd3E0ub9zAZJFMqJq5hOsyThvhIRM9xJLNfg5jXv0hZ6o4VVx8UzBzTnVXfcbEWrsZu8LtWj8iaKSRMjXFnk4gHhSMzt8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJcVd8D6PU8oEOqWV66UjWTgeeRFjbL1s1C1um7xd_h9Mb6CqvTBpdH7AzSdP8rimnc9P7SXnz43igUmI4iJB5R2aMMAGPR57cfXo4LvjN1HHC-qa7iQ1kobJZDVRqKm1sFVwkHZZljhXdshrKkdw_0LKz1GRNpDYiyeJlqnX0NZv-K7W6I9R5mDr6ta9D6dRK8-8noJMZkqnqGfubqjXhXo0FX1KczpKn0DjgjuLfvDmPd25-huL_MVT7s4yfDnTH_L1acm1TWRrQvouDzC3GUQZ_yKUi5DFQdBv30LJnYB6DsC8z-UUD7KqXP5wqX7f0nNHYDhQ4jDdQ1EwtD71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiVCP3t_7i-UiwobEDBlxbffHb0OAm0tnkqcOMS2ped6p9d77vxHsEXA9PuDghI0bSk2rmxG3MvKt5ZhFF1i69_8CJf3tBdvwxftdpyS-AVfSAWlK6eMH7cVO2Ug-XV-HTiEutxAJ62WkolbuJiBGuQk3b4sPOuiTkniwT0gni26zC2x3lifgY36BBq0__4wksUzALyOhD5QiwwyUut8lGnj5C2zJkL5h7P68JF6XthRuH88D3TADR6htl2Jomm6t2HZuvv3XcDHarhs74Rq6kXylc76tj3sVt-CXbcItqidkqVBx6ejIdpKXvk3YDv-OVDR24Q_F8ZZVIPoP1wAeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Nb26kG69nXxQBouDh3kyfvF_QjMO3XkPmw2xMgUEv8-Pg-a7IpYsD8jSQGlltTreefzYQPAmA22OhlfTbpCbOz8ww6y_boBDKpmjHwXsCDFDvm2vDlDa4os7F4XMQCLcvfINpHfdqKWGfxQXB8p4HjlQnywzAYegGKQYf1ua2r7jNV3EHf0aazpLWRqlKFrlJc1-PZ9LUg3S-bBwkjajTI6bVCDC5rgkibG9-BnlH-2dJdKKEjzOWOEwD-jwzA1XJBGAoSdwHAWegg4ESN12Wm3fV5RiuxFOVhxqcPrv0FTQfNZojBfV1-jyW8AcJrcljVcOeCg6-mk68NE6qntA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC8pU9NxhPmlehz4JS0Pl-brlWwnLI_qsVgaQ_nYFUexJQ7qmPi114G3PN9CODukWHrF7_gkWai5gdAbweabqefIkZh4FsefPIlXNhUCCmzr3x4G5vW4xZFbtK2lv5jC7utNdzjFr0l2VqL7PJeHGCuJ5kxzsSGS76MV35bGT1tBn5SCBvRjubba6oN7gw7yRq6tqEgfPz5RsvERMa9hhIBD12VC4OoNulruWVD0rMcn9RCv9JoOBiUmgARdrXnJrIfSZYLetEAGlLFp9q3ALVANVY4vofK8IE0q8zqj8wSWr5G0GutZpvv_H3-xWNT2TNz5UjsgdVavplajDzYD8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orFgT5nfx35LWewmhdwRh6a3fqVFlrcya49_aB_xSJbdv9AFwVseMs9Zb8_xKV3VMNKBx3xpoYnyt3irOUtLwOfraIPSS7SiB3jdpGghu5YHjR1Pmr_ugdOo0hZlj9iz2kDDf6HNEGLY2ABmx3RpF1UZoqbqnukfpJLexyQnM_vBtI6qyIqbCqXvSF9WI5hZ-F4F0aPclPyNaUGc8pZlldcFSWraPS-aAOox_-KrmfzaTQ2VWBoodIjytyCCIumLxYI6YDLNwDhGOkj1JgQXq9xe1iNu1asemBt4hHPlulwmEVQQasnYwZHk2f0c2Ku_r6UfVX4M2fLsK13at2U9ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHRq4e1Q8Xdk_l49vNyO0EqEsN-wnNYBCzSC13YBy5PhH55An7m-EuRPuKsIN_ah3ktVAYxkmcY8B-kyavX35jMr-9uAfhbpxwyGTI0y_KeABq06hT8pi3BXXmHqbnLCMJ9Hya-7ECsf9PeiIx6cumvK4-shtcg1Pbm4Hwz____BgbmuxvDl5_zP8-tVHPjGP-rof7eQOJi2s12-8CJUbzT9wrXyCJbyVWhscZc2vYWu_G-9gcZvzBzJHuNUDxuI4f4rP4Ats-c2SkBiEfIEizStQXYECJXBCTMcKCUSM2QEBlITJv9zD7cXMlhW8uSUVCJkCWnjS-XolxydOlI7Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GejCMLKLtmWNB-6vQ8prYGeuHQwqKXEy-HnpXwoPYvbOpzDAHh66XkJXWbkaR0_gXwqrl4LmFoVqlaNqjly7msgm-cVJa66gzAJ7t7K7CviHHRGJGtvhauB5qytkcR0VPbW55pnNs62YPCCkqQZah9A8BC2IvYy3KjHm2q3Ofv2PQ4u5Ct3yz4O1ZxAqCl-fMIsalSeWDVBstep1xFzj8419AXV0a_ZesyyYq17-nxiBORqkg60XaFS1QsDqOomTI1t9nMJL_SxShBtNuarRzrNDDzM-oAND1h3wicJVjqqHqY0-xHO5rMVcFBSO2x1D2dmHJzZdH566UnJzZQudQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2Fdit0LQ76MzBWyFGNqSW4ZKjScVOxec18psbF03uYlRZWnYJR2Jr22CoMNv75Zlepkjg8gN_klE5ZT6GOQQekUz5TOmWNDqp6OeNBdaaNXret7LH8zTn2bMsFn9Bmd1pp_aSZ5fMl0ZOFMZ01AUIZTjgjnJBflxZKL1R5PGmEN5CVi_2Ju9fr71-2Q4ul9El5LbhtnHqH0mTVUF1aFS0YnumTnjGZPUi7jNGQxMkqf0u4u5jq-ogiWnMWjqexSsiZmyr5a6eJv79MuMsErz0aSSYEOWn9XawAXxi2tPQ3l-yKcdCGxbArEjq59SohIWhIN6KHtzwTesImh4m7sFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNVxMW3cSUgYqjpwQmOXVyL8EFPf7zlIDHBC0I-e_yiEMmwgg3G98d5sI65x7_8FHUOgc3gV7CZa-iLoovi6xobI43hrprYPUOgHNuUCKgkpBW3vvZizHiFUFU_owFuTghtzjmuE3k3maGt_X6urJ2cfhdWWtr1z92bQ5mMlDaU17zk6EppPjitRy9hYEh0Fonzk7CJNaOgdt79UBO5Ldov0IQeqVTQIT_9yz4HUkrmdq-PIu8marcBAsNQH1HLqbz-sIbeaDXBJPpxp33U2REIEGVh-jo_iI3BbSzqp94mXGa4zrlUKjmSIEkF8qYX_aoR5lJbA52-F8xg-HjKAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xs7V_ugLg8WOwfH0H0PT3oWYZkCEmnq5A_c9XRqlPX8CQ03ifunFHwk2Fthz8g2QYDPxFKjZFN475ELmegOoEuf0DURTObbI796QOrEJjze44IhIuoehHYvkQph9nmmLs4bnq-JL_ZlneIwm9jcd1uOsR0jwcAVBSrRZ6JoBfNCZsvLfVRCjEW-zTdv5dJd4_j6uOKTu8vGUkQCxlfrZmRoJxtYcAhLPot5sRIRa57ZAL-NR3yZOOY3r70p1vQHY9qPeq3cX_C4vHTiIzqpRgtU8Djsu67kl-Gtb32dcCwm7CzXylQOijKt43ItFsC-j5E_Xcdi3ywN8iNpuIkSJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNp4zMvKbxtXy3Bg6wSKDHb9wD1j3MKl5gzeVff4RFU5NolzNwb6epwDGjL8oMucB16qoiwsijpdmRqxfAd5gxWVfVMf9ijoh_PpxTPk2XSU2hXvQ_zThxkCyb60ITbBmKt3SId0Jj8c55fx_zDUd1LondPi966IHq8L81_qsFmvHuNn218giWF2IAIkQF2DcmE9YwtW6TJDX_fjtzb6b8bfTMk39UMcCamZXDOVjXz35g16DtT6FZXkfHgULnc1fYjL1c9wLS6-PMjGzY6rxTgL5jMHAFArJCvx-7OSuHWs5-w147tp2lG6-ROOrwk97rWRPxTshpkLEyige-nh8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbu8fdaPv_esREpKcOC9GpHyWCMrQVPl6gk5O1gYIXUqaX54q6L-iFV4DKa_EM6lRRbhZh96Gjo8hukmctdcoVblAYnvIybIIvVO7rgAqptbz5CegAqlsYvPaQl5WYxku4FT_xxnHp4bXhA3-HhY-B-5K33E_1K18Cf3d78m8jJbLE7blWS3xNAsQFQgB9x8ucRt9-1gTD7-CFGLlGDdGd3R2q9PLw92gUl6WLNGQWiCe2IMKnAiJ5xVOa1w3ZLp9ouSy7iaDaZljohoEiH_Q6Jyw6L_Z8vjeuSN2Z8AnfLMPq4-cmNx7Lrliol4m6kKrLN0jq-g2Kna1IVPs1cNYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIY4nFDPkaq_042fy1rCALuTU2CMSdp2HD5B35tjKTsyge8WcHPd9eEyoeQnN2f9Fzzja65tRn_BY7Zlj8lJbQlQqTnnoDHKTr-8djr4PQG6utNtw1Q6BL89g3XYSbttkFt9OIvk2Sdr425mOLdm0AiWPl0sB8QIzUUKSk0wiuHipPJextQUNHHjRE97WqQUsRIyXCtjH5bjXvi76w7auez0Tme8-F269_gfNuZae8yomqEwMpeB3_47rq-UcAX297o8MEv5W4WnNZ4xmb2LM-4xA-QTgyxG-Ba0dkDOelLtG5ToV1l6cKkA-kIlF3TovmGI7uFPczsWxbZIVWukTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktWYYq8QIwaTiS5lEgRZGjNUodjkxH-kJGzGYh4S6F8DPXSZG3LUoOSO236uhijYsorBYE4g9hbrHVGTyRlp_8_9-Ise2YM2kys158FjgVvDukNGiXWndo-SQufxYEhs0KzajX0z_mj9V_bh74Bd3Ui3nC8dxBJuAJyvrcj9ZiC7U6WbZffMOel9YvKWQ3lv5O05mQ0w5inV1p_0SHk5dwCbSzLEbDmfebRB2JJbixe0QoEygBcfSFxmMShiw48ucfRDmgd5oD_0F5dQh2zMURFuyaVZrLEsPWrcB8hdUH9aqVILGubAxJEbPQhB-hLBZCVKv7FqmlOprYS2N5R1ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO65bAJRRibaK242D5vGQldfv90YgT2zouRk8WYHprRbluaWFJnKOUcRu0lQF-bNgFUQiiZiWCmMjat_XWUaY3SMi56Z31kNwz7kfcYLMS49RWNjyu6C0lVKXJFtsHulwO0tPR4WJ1_PdhlLgBem1OZWudY2SEe85kDcdzGFNCi83Q_8w2MeB00ellYYRUEcEndE7iOL4YsgxZxv1qUBxxptnVt3a4sFWWJKzoVgQhtoxfmHxQA9JyKvSwgU3W91wmlahSA-m7mFNfPd7JYU3wlAZgBczn_nhGoc7TiRERUj2MN8xq6qAGzXaaI81q6YMJQ8s-KFi9wH_ddiVOvyXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWkSEpBnww-wBuB1564SlDVoG0C9w94yazWiVprFRD5JbFmo7kdzNMd2-bhO_jHUnMe0ncrEGHimGvzIfRJM8F4rrU42TruQ-GsDfL919JZX6FmHJuTi5Uyb_p_R731CEvrctreX5p-041yfhZhePZ50BocsBOM8lnRvMLhsoDSFIhyOX6ZXJBRax4ukbC7PFe-VEppOPIKpUO7aLHJe99fzTVdcAGS1TBFAQgWmcCH-4A403lS_-qvF26X5CBXohCvXosliTBny4zDho8mDf0OSHd5-JuF2Psd3zUqfE5YC3IC9AuzRcLInK7YFZX9tiB7qk5sKbFEQJBImutzM7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk3DwvPNaNnIF0aZWd-XZcbMI3t9jrdW62u64JF9E5stHas3nH8PFwgjGm3LafjZTtxGnsyct__EjOrm_0KyMvL_t6KG4zpScWwzqI16pIfz8aBEq0CsXl1BZmOUaG1Yq8eyuy4VpdEdj_EKiSw73zEiCV2m8hPFIv-HoLnQ8nrwi7WbJ52b_EVZ8wC2AHxzNSlKOmyXYfKV_ibPUevXmt_De63yHloQc7d6c_MeEER-MOxlHhPL-VaIKadpt39tkMTKuUqQtbnlEXVg4EBcahBzb32QzoO3uzO1GKnVKLJgKOMo5GcEItVnIi9vrV8LuWf4r2Dtm_KYGBNr6-BExg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsLnou2f48ZBhE5646qysBTPr85Ii3-Fzq6g-Yo3RzrWWZyZZhv3vF3_Jp_DGOVFCauCebRMZ_I2ZEGYTw1UrdM5wwFrBG25OhpSNVuiZDP9GpWBC43338lREWDaDUB33_SjSal8NCWGt1SSOFTW6GiHKaQAwd8Ao4s5Z-dK9XDfM9Fu3XOAHpYt7DJjlw8xC1C4R9nq5XXGutTOyDZlg1G_KWZS8yRaJ0MNiBJTAU7xMP8AuLKXfiuMHJ6mFXSaik0GSRzKsSy0s-qC0GbhTQ1j4p4Po6Vw1pkChm7EdhPwKdrx312Hql_8iTC2s8X4IqSrqaPWplVV_xns6dqNwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3Ssyz5VPD59KEgjjeBv2jVJ8LdYIHeabuWv5zT-BG3M-ieTpbblHEzN8aTDe0urWUlSr-S6Khy74xmTp3z7ocL_CiHU1GoVOQwjUcowa-zbdPOzETazCvsrdfn_eZ0q8jUCjE07MHNy2d_M0qWuFxNCSI4gnCa9yXZGcnQMf9Po11UR_U6ndTLCxIhN-T4UKlE0c0BAd_m10LRsQPloj6muD8o72ndHYsjMF-m8YMzcOhSwgfk-x1x8ZclVr2rGL6n23VMh5Pu0LuAPPWTAtRRJfGJGQBi0ZUzMfK2BgDQscIuimR8I5PgjEXY4EyxmqksCMl_GIt06Jdhm_4QAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mq_RzkTln0WLtvfx7CApWFpXzd0G1z3qibZHt6N1Enj0ice5lUcXbF9a8hh1Tuk6kc830C4ZxZugEJbF0iWFj5YSKIGoH5q4xwVX7tUqNO8Nw0my37BrJ7I3yO--W9PeoRIeUw0EsfcrZDAN1zgbnUaon4RpZqU_HV-fgo43H5s_67is-TIqOpmMtCN-IcwG6Hlah-8h4ZLXJQdHpxZ-38lCluYHA3urCp82rfJ97VwCUbLKDpAMf4Gc2b5eizLaa82RWrvPTmsM6c3IXoASDRNKRLJxAAqyqvfVLx9t9ETefQSJ60dCygKrA2kFSV860k6Va1ynQL2KT8da8sny6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6v_xNHESFtBem5hmTn8ZgNcKbx9yXHnk1tT9qTjVtin1jlv9EW-_Bhn7B27tU1-cXwdIr_t6danmnoTe0hF3tazudrcIETamqkJw-hFCPXS8_ybtLzXviAkcDnsOVjk7R0Vw44YWf0aHfoTDx-JVVyEp2TU8kp0eCMrgADeOjK4YxVnhBiIbT1v_t7X8fZz1b2o-4Rop8QOVX5_76rwtC5G-QovkvUNDTqe5hg8UBNZ-73pWvXvmAbEepANl38BA884BVuaEeE1sTNPBCZDRNJ1QnpXrp1nscroyodz7qwzUSrHkPixk9w2kUe05G2hWWb-tx1P80bpcFPrPnFKKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vllfLJSaFRap87SaD4GnlzLqXcowLBtLvlOFiQXxQrZEVpyOFRCw-eY5dnYdVPUGsQSNZThOBPYq0BHCCbhI8huDkZhIh_B9MXSx4gJ2OFeNg2TzL3aegW8-7b9l3B_kJHPw_GyxoaqQ2mdrbQHPDSK5-5KInyyOmZbXCuDW0gvS2uZZNogYUDvXjC36ABv9BQn80U6XSbBwFiXC45UQzrk-rIW18M6AklJJbFA2f6Uf0s2vpq65RsFPsbAAnNn1O5tpghsQP1hnYY8Qkeg4WieUui56oAW6H51rJ9XysRfbgh6qrppld1_u9aR9BBX-Njr98zMYMlg_ccN5nLtvtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFo7CmLAg7L9qS30xBkjuymYueCoPXv1ZBg9rRFyfJWHwFLbBZuJFSFngRGnHI694ComOOr30_m_IQgWyUpm4pqPCULx9F0D_XaAnCVYilOphF3qpTeJvL-FAVBJ0xMdZ-jPP5ZiqWBSTWl4LWPX4ctwUjiUQWSKArFRukUN3qIZGQ8QLSkgJMwJjav07YBfLPX8SKXnzcsMFIzMQpdcjWzq12NAROGqHHikkpRWcsPI0KPdg7dKBblfzAwvHvZ9DBOBf5rl9KUEkULXsiPJKQwRyRIAvrC6OFUpkBaAyv4TSjikFqn_hR-h-1to-k00cUZ_xSGCQphbbcIg51XN-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW08jlNRnCeJttoSRkXUqNsllPotVbLZGSAWsCf7wHcGc213sYY4BrBlVOlDD0Y6Dm_ohKtkr9Dr0KR3KP54KS5FGz5vjciiWxfxc3z4GdHgcnm2dtWrf_XtV6f9ojzfMbdydXhZ8zjKNorv0Ux-4j3Z3UC3ggW7wUsrtv28aoBFiZfCHV5Cty7PyUf9ZuciEdKt_zMnLUeYII2nSF-yUaUKBZRvwX-41yA6NdUYd5NeO2uroFKWhELL7gVJJKnJcnCs7n9_m1TIRYFgnIpEdBTeK9pZs7dx3PJuQNKb72lYaBl0o9jLpNNMLDh1bPLbs9PCvCueQYBLxbdeNJeOUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyIUop5PZSyme5gQY5IeVwzCcQ0nwf7jSuPDJu2iURFp87b4egaBEp8W590zCGf9uJK6wfD2eZJ8usOyndEYMQQ2PB_AdqgvAszD5RKYI7wdEDimKo-w7SSkoVW-eHMJJvPpDlk_9gdIDWJIul-NL2G72Q8WVBkoMX2XR1t0SHXEXUtKJtC5LWWLymYxE3lKJYmnfJgczNRii6S7Nk7fqJPXg5IQVJcneWpDVW5jvCLoMIezANLj8ukRfUjgyisGR3qnwwikMzNMJJLPzaAklqje1kNtugp-fcCefYaoXU5PT6SbC8ZJknZzJwXkvZ3WpcQ9cGQlo84DNsK2SwRvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EL3iKh8VPitoxYQ9kPdaYxiWXEMTe5v721RStvbZ4A6itoqOdfaCgn6f2cYY9W6O7SWpuG3GfL0KVefEeq38vnQN8yQrIdgLq59dvryxXcpsGZ1IRQiz0Lma9KdLnd-1KwU6pvWiZAwxdVmbS5rtxBRwQLMv3_ZWDI71guXEBLLBmYWBdns6w4qdPgKAUQOFslAugEwasiZ4jGULjl1Zu6ESt9UtRy25EjGt4AjV9p9TTO92sEG4kecg2X6-F-UNFoh087YrJ1aNgXmPEpZvyD9WeMMqwVB1jdPCmHlqZrJHRZ6l5cTf0wBsrhY84r2he66_ZcJ0Tsqy_VwXB7ov1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0BUPA24-KHxzPWxC95nWt0a9dA_eJCtFdMFNPRfNMEcavzkKE7kHmmCrOZcjIrNfslE8YvlkD5GSCpwNIU3Iem0nM8OROwLZ5z7uVp8CRFwFmgO-PwurCQqlhz0O8C0oF-9YfHWQfto8hPxvgmeuwqeYwrqSpPTn7CqNp7rUIdZlROa_NT0EToCndlOqBWGoLo4x2xOaAfPIMaxmA6--tD59mSWQAEyGhq-aIjtoBv3qIKiA-P2Zz6gJyoDl8x1HkYr4gPgPxawcH6Rx9qqkpxlwYPdAhn68rtk6zehTmw2c1qTeap8uAZVNdp1CzJrIqmpAE3jvxRU7K1HaDIoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWt3XkuQHzxgqUP80qg85qGWwzdbB7KKJMqcqPP6GgpO30xNPNNGkAxXqmyfkrbN3YE6qaq49FjiTo9vmM-DBppBzdUNeQbo1JPow8q4Eqvt55K61EOiLb9Leby-rTvY_DzXNKd3H1EeH1qS_dmKcKxuUVbySy0B-cqmUvqKrzvMp2D20IaRVc2YTffP0QBrNJhx9YqtccR0meb5udXd9zUKorl-4WWjpE_3hMaQTfZLP9z0Cg4HxpJ44ZPuzGlZlJBQHQet9VLzczp2vvkEDf_89NfsUM5zt9fB6qCFbYCpyDtpBGdWIrr8LTinc4Bni-2nWtV6L45V70-O3OWXLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-1gXtnuV5e437rYrK0OGOTXhuVZXwtHnZN91OtvpH7LOlLjDOjRG7wg_l4kd7AFxLNT33PdokLEkSqWfszl8EYztyt6qZtvlcaaiPzvzmXtX4BJ58rs70sgg70U4GzJxbTSFho96KCf7sPtmO0qDtx4-gd3gD4FLDhQjgAnzX40SP7bc20W3NzCRH3WB8T5HAg2StlVeqUVU1e5H4Y8fKoybKbI4uAz3ob-0d-Js0X8iti6TZ9HuVdjzmRaEfx1pvjzTJDbOBWh7N6M-aolCH-a3_Bw4ZWTX3DUOwHeuwvL40h9IaJgzy4wudCeZ25CutsYjspKt3h8Ma9FDfJLww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iks-TL6FEZfcJ63AdXsSwCBgnjeE75ZeYOGU3dITv4X6n-vfKrpkbN1vo27qBQOipj_M-pT0Hwbrul23UB39R_RhbVwXBJiDOp87z7QljAPd1JU_EYaplS8_7WqdcnD8Q780K9I-UlXONa9XNDBDdGRj6QgB8s8KXyDniAdCkmH6EJq5oaP3-u7aq5R11nZ1gX9dND2JJmqk6O4GY2MjnWY-18cT6O0mxbDCDGS62dE4wlkXhZMxZApCavlVdz92vYU0VVNuKiIZCnevdrnO0Ksfj1r7PHR30nKt9safJq3roEGr1ey7js1LSRIXy-JmArCvnrQOesJFP5IuA2YXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfY_HULn6EhswzVgnhfcn053BBXZ0rzSYLiOXd-sNWbS1l6Pn-BYPRvbyt5B-ZAHSTEWVmizJsLE1C4vVYYy4_mNVPanSE3C6YFjWlWEPR4lrEajWPcKE7OcM7hqqjyH1Cmz3wZS5nkcxzhDiJQgHs_Arzi_8uJEJBJAF8YBlIqEVDe2wEJ_oqy5dVudPGJX8_WuBLfkOFV9_4kfx4WW6Y9NzJZ_50xdc7z4GYlIoUMhpmaS_8m1UuSgYw6zHmEiLNFIql3NDHIg4c6VW_2-pYE_6h7IxQC4zxx-qko7qItM6CuE6JNCPseBeDqTTFm8dvmbwF3YYVNMP2c3q87mLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iifGIeF7RNoeLJQQDHR9sg_ZxrVjRQOEYNvQLQyqJWuPXAQCtBYkCLVC5wuoLwJKh9dKyCCdTk8aadQu2AMEmoi-2qz7vDjvmBCotrY0LTWQWM6smnZWKTITiI3A64i3hlqcfrIRg_cRtAOW05eJM71LcPA0tSOngAF1IAt9RdEVKnkA5at2QWBIjE5_YCqeL5vRSIBbEvGFX-CzMcWcGhED4KuIHH40VNeEapVhhxg0wX27Hv6Ufj0Ri0vIrSwgaVKm4b43MIwSdgf9yboq7f6BJsaOT6UMdS3xsk9Xfz2ooms4ztd5WcJ4rMXJ1QKlzunqGZfpDNAdwjep106-5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn7iiXY0upuumIgvehbVAFVDWMTRWaZBvjFZY5-gZe3liZmmE53suDpFksCfMAYf8_TDL1VsuWNq3-am2_0Y1ZttshcNBrrLzP9Y6pAgB2ZSsPxVN_ZklMwMfmzwTFHKY0ZfSWv7ZUo1Pgqn5PAzr3JLnqI65OZGVt1GC9SZ-PCEKnuS61VLxc4qNjHsJ-MiRCKbzqarOSFzuLDctAo9Y4IM0kZSm4qOPq3Yqx8JGJz5wzOVaWPRRv8u5F3zlOaZDPQ-L0RWg9vp40GaAMkA0_uMjQbngBvxtI46H-9olhUGh3o9H67_HxyqhBn9N5xhd5aqX0dDLyDVnOVLAd2OLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2vGuImqzzGKyqyxXzPmn2s4PyLkKit2cYhnB8P8HRJFBs8D8gChKql6RFJwcU_4aJnpZ94SqpgjN5iEbjeMF5RhP2ELf4piS11Hk2p1x-E3sCToZAMrGz43kismLid2p9gNVYWgCIy7HoLS5yBi2Htj0F_OV-vULET9HffHjfgm0Hr-K1pp0qwWMClDHWDukBvQXHnySEkkquY3sAqduOoi3XpRQsfbB-OSYztMWrptVbcGJNDglGiinHkKyxaKXVmtHgk2jBpI4UHbjAASWiNPkJzv-drR6vmUu14zOvBk1nK_rcRfxY4nRgAtQG6nt-Al9qbhzwNLa1n65nOjPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQKQz5HX6Pek78J-vkGOo_VmNz7CUtgfndnk6Vqo-Y4uMv_JfLYBaylMXSW7G_On96xZzURgTeG-2Kx3TabIOEk2JoQbaXnFy_x0I5-rsLWMplirkX4ajCXh98zGEP9M9djvGphp1JKZ_Xe23EknJ5gbp82e8yHxCCF-SHWWq4-4QVGLHKlFgbkB4AJXHZ31mN1fXlgp07dYXnayZZbfKUL4W368NYLQ7S6sg0TKvJ2CViKQgarekK8HNBPQEbTWqtpaU9XtQDYK__RctlCQdcn7PvTQrZKSkiO3x2D8Pr2s1IYcj7r1fuTtvRVXzlaK4XaIFbVmXOZkymLBNmzjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxE_SiGe_9HrHgGR8qrDaHyCIyafvVQuOuaRY5etdL4ePB2x0x2aLmtZ9RDfM9Jx7fsohNIStB3_NVOfLpvB_8DNFhXUZMJhNppx7KleaXsSzqOhc1QdPfoVZ6mcnTwxFHSJija2Koj2fv4kPwccreq-l9RfMpuKb4Xkxo2bpd3Z75T_l6oHBp9LMNVciGLIJEE4v51xGm5PjkDyR2-IMn_Yk3DB5gYlJNTC12lPpkujoC2YS_tI9J_J2oWqQf3PxQK7Z3O3HFLQLKSLPSCB_2SP9g1SxP7Mlcl3I7AIPnguxw6rwWc53ldfYQ_qRrgWECbtc78m6F9LWMkMIpsmOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9zSBdZpWlQ5viw2jL6ajEG-ko-xA3SGSLRQkKUu-qibc_8LDUKa_EbCD7of02UR2dxr2UI_MLkJzbvkAimUDfXM369zNbnmKpDEtBzvROd2pu1Hq04-T-yIdGj1D7ESJeFszdN-gSiH1IEXyGaLCLfuRBD1wUMgM24oEkF1qBhjBKvbp-oYVtQXYswneXxXkoeLbw6-mVM7b7fsE255Kn0iz4RP7zSbaVFrm9n9-UBWhEZfoWUBALF79NB7eFwiHnrNoWm-nWmGlWjc7IdUQS8ph017GEI1k74Wm2pqOJM_gPjPGc_nK_oliwV_UeFhSFXEMpGotPF84U3tB1dM8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1CteCzgyRlRy89S5qQdf5Srz6S24_sX90ryoJWeJKdooZok9QyIU0JQu7DwaStSaGS0oweCj3M0ccQWlPAC-c9vU3WvSC5MlbrqiT4P9eJP9_anbHj9EHSbzJv5ZeNtGXrm8-hjvudHxKPDD10aZIssliskyGGF_OA3_BYydMa7NK_N45nkQeCKke3ZUHl85nyvqaso4uoQHs7IvvmLoNUP66B-iQe_vqDATmCdBoXXDM-6fUGv3cKcs5fl9jw_MUp_BO230BDvPEbM-kKFZXWSKnfCj9D3ZXCR5HU41wAuyZylHJKefpEuVDbkKsOoxXAymzASm822ET42P90-nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNFTT1XmIVwnbHxFpLP_5V14hkCXkz0eZ5JS6ohGruaz6zY0_cQ5NF0r0BWxxTjUucVR1B5ItGMHaRFEQA_uxb8MATzL7E8Wgf_3c7NlnPHJQrxgJsHegHbe-ZslLN1J8ULmG8s6ac_PbOqnF-Ir4FQ3jFV2NTKNmkoShKKnHwTcqe2C6HwOoINacM9zp-W8d8IU1UQE2m5ik1dCYACUMYvR2VF66zjzw9L-n8gVjjSRVikI4KS_OFs1NljsbQT9rr4hhPy7sPPn5w3Zti4JuJBBkD-2iGNTrq93Z1RjOtFJnj6FMbCWcoMfIvhhndNgJwg-k-0ghB55mr-ohS_H1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDzjYzpEK4VbDIYuMOygCugyYbMjcxUxaOA1mZ-XPMxk-wmMw-3s2DGcCHcVk577WQoFMvQY83Znm0PxB8imJX6s4dHpi2DSP53Zn8uBE_yNUYjgqbVIsWHfGWdBd6anrZEWmd2AYVDzWXjDNNPZ2jvAVA4CufGWAI5QAtpqlDShIhpD9IwHTYQs2WfVvNZ-2qTkFokCq2syee8rDO0XtlOG0nYc5eMHuJ-5EreD5rWfupZ0R4bYUVw2_jCVnJ0H5NySdWCm4NmCNccvM_8uEoaka6QjqhzTCTzYqF8eRv1E4DvzjKNonwffUQM51aEL53jMn5EWjNETsB-l5puLTQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EMzlJjkCZUQPxhRMRBks78N-GmhOJNWEJS2e36Mdv3S_dDtuIeDMNdLPtAAWYnJ9IjiCHCcjDhdufDDlz9FEDJpUv7peo2dHaSz1T-7UM8fbnkW7OIe8HXU23NdKj4-OL68ltBYT-AtX1e_Bvgv0xFRhXf6A7d0sCUUoFFQYrk3FgelqYiRJsxTmJ5lUaV3_RrgI-cPgnMXQQnDoNeXdYYpdDkNm5pzk-stKL3nZiHL7M9w7SZCSBKrZ8kc2aTL7U9V7G4d-q_3B0HwdsmU5-lTuPq0jDVsXUwop2rBbiyRMoS90gxEJZTLi00zwssgLoQLNPY2Z3gsDR06jm28xzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EMzlJjkCZUQPxhRMRBks78N-GmhOJNWEJS2e36Mdv3S_dDtuIeDMNdLPtAAWYnJ9IjiCHCcjDhdufDDlz9FEDJpUv7peo2dHaSz1T-7UM8fbnkW7OIe8HXU23NdKj4-OL68ltBYT-AtX1e_Bvgv0xFRhXf6A7d0sCUUoFFQYrk3FgelqYiRJsxTmJ5lUaV3_RrgI-cPgnMXQQnDoNeXdYYpdDkNm5pzk-stKL3nZiHL7M9w7SZCSBKrZ8kc2aTL7U9V7G4d-q_3B0HwdsmU5-lTuPq0jDVsXUwop2rBbiyRMoS90gxEJZTLi00zwssgLoQLNPY2Z3gsDR06jm28xzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZTTVdiTIxAgNfhjTjluM3xi0bAy6BAynYSzOWs2KARq05hb5uWXL7fMio9vjZVGQTYjLW1Ysa5UfYm_lGuNMF2ihsnPQi0CFNAf4mz2IdDTZrcmHqtdDxJiGxdOexXXIhC-AsZvgmkbnOKSZzHwJRE_4WpnXrX4Vexd1m7z0imJcScfka8s1pY_zi7GD9eoXR3LMeufZUazP3Xhm6_9JXiCmQNjlgc-6ifJOuYZiAMGyAJM1kXPbvckPzyfiUvI6_vdBf4jU63B1zBpW5DfkqO9EpQjjrd22OHwJPia5-BejuFUQNXNESQN-Q-w6WXTb9-AWxOlKJBi6Ap6Hv60fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfAyxc-D3zKruQ4ZYEtqkMdm4AukLmnqxCupzhvfN3jimxdBJ34JcWn1fXwpgu2OTW1704Rfm-cnIb3H2LfmIrmtN35DBpCiC0QnvcwbUqLB1Dqj_l5PoJphXk3LMpliQHO7b4ix3YLkvtqwFay5uNghUyNlyE5Wurz-k2ZVEp0mozDzMPseKuU755feeAVxwh9mFeyYuPliX1NzdQBoATUCHH6RaJ8z77Nz4pXSK7SMektGnTwXLZHQsws4Ce7JBbiZQaejTvkDj2UNxIy7xR1r6PTTeC1iGuDTlliVyFW_xF9PD7tlSDwBdGd9IDaeSuHdFdcysPXKQlAK7XEq1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOYEurcrjBvwzQlCRdnhuKzPsapnqB0tVoh0CRhfQY5xgEHjqIYod4V1Dnzpe5URpLX84gCQgt8EJn_1Lee8G06u4U539O11ACLoCx9uM6hUiC06vJACDSoganF4T4bftkj5cwxp8pr5YxfbPtbHT40DK-PuVpBIQHq-eza3nlBtVxxcN7OVX8MLb1t59xGPZvpIwwWPkU_Edbc6QoLb4fD_FrVve7e6le6sV5ahC8elACX3WEIAwa1psWn5z45dY6IEEKe40_IFu7Z29WKFUPxoCsYTAxoGYo3ELCJ1dPlNSrLQm2OBOmZsQec0vkbD8cTX6GWDDrWD7xbfivw8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2M_kpC0cpDdHTYXm1IINqK7infWL6z98J2t3gIpMzE7IZwUC-J-60c6s-a4AybWlVgngHieCTpW8fFQzrTVxr73_pJ41WGK_D7JbCOgIzjwSnigR8DcYsKgh_lC8ENwIVb70Jn61YSuyxbsESM9wME277GGwrrk3EPS_ttaTFFeoreqzhGmjfDgaoceZenKONSpj947jnciiM3aKS9t6tFW_9NZc-o_qZ1T3l97yABqbhdjAqv1OprNxdnHnDTaIZzdQrDIau37qTU6zQjjwuB-NXb0E03PUrC8HQq4vIGLsW4xADeg4S93U-ZbOnpCRnFwaS2eIFC9E1Ld3YlFHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBQBFSSlrR-n2NsDPsE-1T5KnRahZyoqFgkezNSaRALehxDqAK9oxnEnNAmj0BxxCWgH59tEhb-xyOHnYbVnv8ydfkTuE1S5fFacZsM9sUpTSnkmAWU7gw5wijp6rfzaZfsFRxfMmVkAYnDhtQ3xi9u3q8T6JCPY-7acU5Uq0Ho-gVfFZEmCuqX8giqXv_vu3nzOldCkpQ_iutxImRlvIQG26NprTb429dbzqSNHfkwOjpiMpkkg3y_NuCYXBP_d9Aj4Hy4cEhzrAu4F70H01_3j2r6klXPN08ws0f5MkEL5CpjoND7dNhYTXGYY8JgrKPEYMmeOYQmav1aFoW_vKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZjoS8aWsb7YSh9PsbxXVHfbvoCnuHbaqD1foLOuisW45id-ufcJ6ok-Z9jwME0eGAEqrS80LcFIvxodS2hdJd1LrQ-1YQxy64JCT3JuaFFJkh8ZLKytf1WG2exa1XzfdA9LN9_xpvKZETEpmBadecANR5GF-bIm5HXvi0D47EZcphSrN60CRO1bBAr5sH9k3kLai4rmQMGF3xzbJTJJuyD7xrVrKV7dQ0Y5L_GaS7X5EsyRl0T6l_12sZ3VYpoFFHwgW00e0o9qIOeX5qxP47B1Jymf_pbB6QvmdMC6qlYtNGqPkDaCH-a5KQTkU_BczDW-jtGps_4plUT6mF-Xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkIWLPsL6WtEGxncKcL9hreREBF6DjFQg5XKdDCvSC5B-Tn5hFkobknuokb3l1fziZxa4_AvWL0va_zLz9mpxd_QNk9Md1ARLWgFef_EI7N5I6mMjHu7nmIpwg0nVSAqvffXh3bJnf1QWGn96cJbw-8mW8HR3i-sRaN39jowrTuFr4EVyE_0q0NldGkGdCd2BWl_V4Szo8JxXPpSEEVqqwiZz_53MKTgyWCk0aG95kbz3FD-EsTvNzGALEF9QZ6uhDNNTifQBr-cv8osLO19Ve1mGa-IrrmIySg_FEEVx4gh-aoDchigk4aJ08CF1GC13KZY5liNoWcFvA3RXad8_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=FXZf8DI7hWbypTtKND2wMz5f7xHwTYzbQU9ikVXavsJK016Tv46a6rU6AF9MMnyxAi_RKSGGoPA0RBBFlzF3q4wHUMyrjrRPfZX0utP5uAe8vvJPa2jUu3fPVIREmjUEktzTk3AmT-IrU4l8h8rZCf9yyoYgbrQTFdivA2cvN8JkPW9fGygNYexsQ_6K3BrOOxlKS1_MKfMSf2KJvfDjxljCkoFQRDoepbCBJI63HzU0v6eNj7cMUMTKdeeogRwl39WF0agWeSnolZSqHbTd9qlxIvp1oZ2cbFr0L-M9ZuufhxesvjTjeE5aEH8p5GfjzfUZH0gw-5p21cCRQGfndGQK_6sSHn-DYfP3CFzrJHVS91lg-gyaKqwYd9R9FbI3ecXIAe_WH4988d-sPxC7kZ7CbDPyteG7h_0VITbPHqP-pCpcO95epTDtzAvpv50VFlicBPvOCkS7PC8hnDn-LLPkoFtph-XdX3vT4zAWPgO0RNKNowJaWGo7k-mD6HMRxaTgzly3iY4iGdIRybO5y-JEXlP9rR2F3TdU9QGZqq3-ukfEMMAyyh5xOmW_ICgJDYMk0Tw7Yfj1BdoQCzwwWYDb84lQEPqfkgwqhXIZva9JkIFMoJma0Ujh1CzqbREf_ZCEjnYmOl9kJP-3LXfbY8nymKGvbRc4ARrfyEmJiLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=FXZf8DI7hWbypTtKND2wMz5f7xHwTYzbQU9ikVXavsJK016Tv46a6rU6AF9MMnyxAi_RKSGGoPA0RBBFlzF3q4wHUMyrjrRPfZX0utP5uAe8vvJPa2jUu3fPVIREmjUEktzTk3AmT-IrU4l8h8rZCf9yyoYgbrQTFdivA2cvN8JkPW9fGygNYexsQ_6K3BrOOxlKS1_MKfMSf2KJvfDjxljCkoFQRDoepbCBJI63HzU0v6eNj7cMUMTKdeeogRwl39WF0agWeSnolZSqHbTd9qlxIvp1oZ2cbFr0L-M9ZuufhxesvjTjeE5aEH8p5GfjzfUZH0gw-5p21cCRQGfndGQK_6sSHn-DYfP3CFzrJHVS91lg-gyaKqwYd9R9FbI3ecXIAe_WH4988d-sPxC7kZ7CbDPyteG7h_0VITbPHqP-pCpcO95epTDtzAvpv50VFlicBPvOCkS7PC8hnDn-LLPkoFtph-XdX3vT4zAWPgO0RNKNowJaWGo7k-mD6HMRxaTgzly3iY4iGdIRybO5y-JEXlP9rR2F3TdU9QGZqq3-ukfEMMAyyh5xOmW_ICgJDYMk0Tw7Yfj1BdoQCzwwWYDb84lQEPqfkgwqhXIZva9JkIFMoJma0Ujh1CzqbREf_ZCEjnYmOl9kJP-3LXfbY8nymKGvbRc4ARrfyEmJiLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKMocaPpUZ4eZkyd0hrEmjaSmU9DLEahbxC70F2hVz4yJuNxLTqwKLq4noHiiRU7avwEOi4CMAQWYGeBw4pQReBxq55ALYYCAfeqISLUNJy-JNJ1nwT1WcOMoRSajL3RNu661WNkAEeg2rhCaR93Gy38UhOY4kYB5iPZ-2aynzcW-ehBKBULZNoKxMD_1A-Em5nrRCHJ2BxYrW3GGmamluyzYaYGkBofR_Ny9CVEGTuS6jRIFp_SiEuF47Id3rQfnkn78yjAahx43S5pvo80XG2CugnN8XIgtAg6EXwHE4109U2-c4fX4dekTCkcSvNd6Ekl5vM5KS5V7zDPmSn5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL2da4Yq6zWCAj2uG9HHavxkdteyo5xCG3TndUxjqdksR258VcY-M75WFGDRIZgs2iCfp4Sddpj341WZOXhszM9ZkRqIHWXZ-xOJovap54YRgu3T6ADrDENtCek8F7vl6B5K-qTLGTp7w9fr93y-QOTYGKzGO6pUScPj5GRC2MmEh50yrVkn-5of_-OtGt5WABSRJtBNYrN5LSYRESay4vdbBlEmoTPGFlide2kjCiRkzQU2-bgk-MkXslrsW9o0M_AeV_ZF3sAfjHPHbd7G8AMKKbGdSY65ISMfo9JQh7E5CPx1X6EJqxlY5XJh3ynROXig7Ypqxf5BFYwJgn6e9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJCPhKhOPDoVL1rl95LWYHIG9nF8wmpg7uvqUM-tKstgsrzXuPV3MmvNW5pTKhynhEBHG4USzCDOYhVNaMLtsbMVpSLM7qtjGiPqpAptAoTujqtz6ph4nzPa21LvcVM78AMI4PK3_DUkJNKMiwMHtEDeKBetKw98u9dYkMIC40LxNyEMJdqIj_NU7Tdt913mdp_xSXKzxHkAU8GbRd1xdUGeisUbDDvYwQRMAzyx3JpxijRyU5WgsZmVqcjAYtutS8RdNDTIz_yBsGiw0wHSPeoNDmK8rk_eJFc1fEV_4Q6A_U-UrT5u6tTqr0tioz-LfrqMGA_w04Ks7kAT-6n7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4q08J6KgUJScz2_KRXp1nZevCjwFc47Yf56J1wMPqrpEoUtP9j15x4_IfoYfjwQ-Oqk4dVHRU_92Bk75Tc3COyweLP3ICi0Mm-lyTJqB-FXu1OJaVWZBYBNjUOT8LUUncgU7V8_ryudRI3Bn_XCfYQ40mNrz9tTKIh9SZR4npHEvvknVYIfjFJN7kiakMrcoAW30jenEC436n1q0Pjumf_HdVdyHyvwDqB83zNgfFFfHOhzZzdy4N_ClRqkFu0adEN_RMsklzQTI6V8wUUlZazC19un_4lXn1VksMeqP0UT2ddXLyQc1kSX471gXKbPo9Tb9ID7GOFBRCIJyawpyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpo6XfOs82_Mqr-bKhTz4sLTbjjdASwN34U8rBWpG35lI-Kgili5Gx0hQfDPSvzUzVJCLaMxe_Z70nQ5Lc30_OKeeGOUmn4wpIFnl0W9qstgHVX1NNVx1IZ3XE82BA-ZLw-Nbyg9-tuONKaJHb8i3orEPHbSTuoTq11U9zHhFJHV11b4EnxNQ_lW8cu-MwF0I9JxkRrW2Mv5QeTWWr_c_VqJjJY47WaAJtYgy4VyORzMrcoxLpMblcBOXaVP2Emz-sp5U_XXIosDarLEVOl-ojQcVEXJoPC_xAc2HUuXPFCHTip32JR1XbeiLwz3Xo1iVZk5hjX8q9Xax03ZXgh1Sw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m5vnaIJO8uztmrLrZBBG3IuBZnOWl76VRt2mMMN2TMqxPK0OYRz1Y0sFbE-dbzA24Mz_o9QL_xUw3cKQA4KfVQQzVc8GD5uN-Upn7rx7W3i-Zf2ZtCADLcx4X09xr3oJttIejQbsg676dkI9wHodGLuvnMkcWfsGpRoZoDQjVGXZVUMoGxq4qjFXdV_TjeAjDn-FWFfF5iyePItkzM5O0F4FjOGXu_vnV3ZAr5gPihmNYTPhb7RJwBfQmg8gjU-H-FCVLjqyzslrjRyFugrYn_-MNEEHoOqzas6vTSznnxseGYAuXOGIRU-U8OtgU8eLRGDCEv8vAn0Ow0eHGlwvn6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m5vnaIJO8uztmrLrZBBG3IuBZnOWl76VRt2mMMN2TMqxPK0OYRz1Y0sFbE-dbzA24Mz_o9QL_xUw3cKQA4KfVQQzVc8GD5uN-Upn7rx7W3i-Zf2ZtCADLcx4X09xr3oJttIejQbsg676dkI9wHodGLuvnMkcWfsGpRoZoDQjVGXZVUMoGxq4qjFXdV_TjeAjDn-FWFfF5iyePItkzM5O0F4FjOGXu_vnV3ZAr5gPihmNYTPhb7RJwBfQmg8gjU-H-FCVLjqyzslrjRyFugrYn_-MNEEHoOqzas6vTSznnxseGYAuXOGIRU-U8OtgU8eLRGDCEv8vAn0Ow0eHGlwvn6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LypveQm6TwUzl5EdpssKP3ECWePfN085kx46DPUE_CREv5uigYWiImwMMIggWBWBdLEQXe8kLrUY7Q8A6UngsTM1VLXBJUNIoLCSkZLAji5rtvQAAqXQ3vc5N5DQGsFdsni0m3srqPjNrv6TtAcfVahMY8RuaRNsP6j-P9tFZObjMF-JFB4GcmUj7ViITuXpQnRoEeAeu6Br-uny72bkIExFxq0RblwA-MjXgCGR_L1ge8A7OGZ__v_AYkUwZTQa2OEvBD0XOT9TY8HrMsBLME0uYhElOELpTl9OThYVsKaYZGmvAdEnE9UxzJPrhkRSqYIM4gpj9xG0IZgUZjpHPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY3PKdtrHjD0P-61DMrGm8At6ES66jp0fFNA6Pw9HXiWq27MFzkqyMHfET-bN6xxBKC7N7tqj9m9_YVhZmfm6q8hincpjz3sA_4SwMZe0eT2m4ZLzyeTjae8MaRzYLXyx4aU0y_gEmY-QUkyRTmEjtYr16TwY2v1E7uPokmEC3g-iNh_Ekn5NnE0nntO6iyAx3vllT268ptjrRrDO2ZfHRrQQetFCoE5ymTGLXOUNK2b6celGWwmSSii94XsmZicRSDUaeMHNuA-cINi0_0tsmoC_FY0tZ6vmlDw5sOV84psP-hdOCSNWxYXE8LguGVGhXQB-5BhgEicdiq2Rduv1w.jpg" alt="photo" loading="lazy"/></div>
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
