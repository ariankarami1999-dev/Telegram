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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aprgGYzROiYm6hpNHsTlTsGk0XOyat8kuS_mmfwwgrmDiLRCKkMkjzX0xT-th6iJKHNsrHbR5wn-3p3KE6wFC6GQhBO_gljOJr1lLB3vL5MP453bLJ-L-T56tz3krQnip3oaYcZk2YTnx-p5NsCGttewXq-mkJ08061pRFMPBsWnDb7XymV-eKdV0Q5v8wv9hCCIW2HfpTkCeSW0WGVTMIaN23apULqvrkkNpX9GEelUB-EPorzsNqAqKh402XNfs2s50lh1L32jblmpmW2dy0_oC_F-moT6Vw1H2pwunMs_GADWTc00jEgAJ5uAK4YvlaMtXI7t6l3BTcN_bDHXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 196 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 439 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 592 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 592 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 947 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB1VWdxX4IUBLR4a12VyD0BvF7yt80_MtQ5fqIkanjhjxDd0Kzl5mJlDiswODTUb0sDP-O9KEKXkvXGJDQ6NiYtvdaFnWDBSARFHX5nBlsoJ85Wg-fABFfNcNqEpcPiLxYU1E36lQAJGUJSjtDyvK5FfI2f_2lZsNq6pNrh0nRjfiUySa1s2C7C8pm7sv3Mp0YWZH5WlA6KvxDbT48NHQP54BJl3tb-87vBALD5VVBLyqICE_49WfRBM-FipdREAs3gumSuE0RWDMg3nQ6X0wo-f_gi85e_nErxhCI4s0xWOG4mATnholT29QEJukWjUID2xDfZFk5mKtnrgJdr2fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9Vn_p6QsS0Eoy9zEwbuoV8raebMWDji9ZoBYQRWqYhIpOnvyTDnCt9I5KBldOJtpYR7wkMtitRV6_SPLdpzyS9LKwCnfZPvSrQ7OWi_-nY0Fqcya3dtsCPg-km2uoZR_sE8eWiqp9p6DcDXaRF3JZmDFYaj6WzRy8rX-ut8-r2VbOvgJfWvCs3TOQb37sqlP3A6veFEZtUbGHOu8DrQjPpMcItYmRDl5zCp1Z8i7RO22m9xhY7CJyPABDuC4G77IDonXU_Xqyx5_BBnEgX969UdEnQps867PdqrmKSjWhrp5snlBlGRmMn_Qz0Tl5WJCIvTZkmKycbPDRD2bv72EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiDT5ooU34FK40voyFG0DZsg00d-RyvKmGoImvdr23vKSG6y08q-kbwK7rFvu3EVQ_hPvYk6r4Cp2HfDwzzvEjPq9rLtbUfVjgWq_n69nJLZZdTiv0GglQjmrYLStU7Z7dYCsFmkq6fNgTIjjIvdVZPRa8Ot9Q5hQOZk8HvCCVEtEuoBRnge9Z141pomfP-mZkCp5oSgUeCgDwUV_wK61HZDPOoFlTRB6gOhJsr97mJ-9ej6xwUs_Lu--WdU8VvF0OyqTQLST0bj9Dd7_B6z68Q7cTT_0K5YEeZko41Z_TlOcy3_4jXSW_7xBUcLty3JmvCEgcL99qKy-mwmqDJXsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBPezXAcqs18KlD3e5Y_8cpudhZZMbtpwu4c2vcyxTos24uSBi8ou1XtdyIRE5ylQ7WsEO3d5RqdaFXT4Z9iYUXYIe7cObB9ozrvF0SK3N7g6aKNDgDOuoJTCR5jV6zTRMQml9JfkxMIekbiJZFIP2rhAs6gSdoKLW-OiXH1sCItT9I7hhoWH9ceQNNjjiAYpE6El5jIMSV6BUaMTtcsYsyMy33j741AH9uQ0qidowX4uE5CNQUuar_CZZrsxsq215VAoj78L-btmVdVPk37gZgR9QMX8J2kvcK2p6e6WcJmypyLOfCDf6LqA9rNHChOFReM2X-s07eYSeqpPoxz-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD0zhXjgQmg9bfBb4-wHYmrjgTqgbqxe64YOU6h7PUqBoqYE74IaEVDHW2yXW4JFxXFBJ5kpq6jI0DZ-0AIOS_eX4XxUwceGtdOz7e1eTwxOED5wUP2dU_AuRCyNjkgPzwlNxQkB1w61XAwxr_H864J6cYz3GWn276b1SmDlyWHvyVAwKNvU-tM_7LHwDhh9DSENb9QyVEsO3d-AHj_bRwocwZ_OolzNKwwNMLsilUe5TiF3XxN1fs2PIfiNC3zLoRgfmOfJ33DLZZRiKESMGrYPyf9EQd07CsWeZ1W-N32xdVmXdRVnfTuIjujiuNDM45ZIEcTpW1FUXjn6XCCcyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_PqLIUi8FtYemFefhDfIMuC5OKfQqo5VhJ-zv7Gm_F0FVacFpCoC8qyRYNeXj7g6U4-gc_IVjjn7C8jgLwDP0bJbDIjgZ9QNC5d8wCgqRk7S9sk__F-ZpWFcrsVR__4o2q8C7XeImltQ1mIb8Eu_qPogDB21b9o_SYxYGcYMUYQET6g77qX_BIiHF88d0e8QtKWAlAxcvw1QFdmTRiEqwtP6q1E0F-l3Mml-oXVRbDGSV_GIJY606PX9wbH--NxUMedAxmFt_ktrIRO3_yDZWAxRaMASR_tKHHd3PLnIebcKo_vSVuh61ky83AgPgJtAcfDS8GfBOW-MaN3LtcPWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPBtgsGrZsbFNEgzZzkGVIE9iBE8QNFSn0OEBUfVxd6UCzGLug3m5u-i3BZPsfJ5wBEG_2Ff9r4DWvGdmbFaYrDbPE3wsVFj3x59Cl7pleCb9AJ7WV7ul6kR5ZYowmN_d-sAhEmM2aJIw5hezl6LRfaPNbcQdtmwX9ufApBQi7M4Ox-KWmpXHfbZ9fTrMBoXv2X9Al4D0kwPNPo3PjaG-W3u54FIwhFmEwzFbKY7_saOmRVo-yhz8JgGLXF6d345pdfd6271xZrl_fRRZJWy6bgZnAOAlrDTBfAe9E6MwtSAsVkQ_MVgS4NvOWnbxHnyaHO3OUswkElOfhSFxu8TuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_RFTCC8km3Nr_qwa76lSIxkzQrKp5E4yowXCCiX1phT1Wp2AFLGKLi2QNFPnJfrwAVCCEwgv_EeIzoMxSBM41uOMY8ZZOvSlu7BniLarASHGU2i2CtbnAW_dDkao8KkejcYALP94uETKGD7ZNVpdrcU4u_H-GO5dbk4Ub1r3FzP4VL9h2mgMye3VkF-jY0LqD62bHiANo6fZVuCyBCo_6yyQdeEBuAs4v14ER9BCeFJhoY1dPuakmz-D0pWD4pOK4P4HL7znATsKDdxxCtPINzVKFjSXCCvAu2djnG2rAA_qK79guGfRApLcrXjyVVUSAUdmzZ3T56l17WaS1XuRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijiViQ-r95_AF8uBOCBONhRqLqLpXhNH6JSDN6mlHNpjWipQ8Sj-Tyti5DUHUzdbxGsHsm43YhkzUNR6452CxFBydtHZ-6FmeVnQ4l6eCDfoTW5UONJQkREr7LHAbS-TWVcGC7D8tM9JWVVzh0AR7tMU70ucFN2dEBdgPvb2Zazq0NdVPv8c46X4BUOXkR3m-H7-7D-kbSjVKoOyVJjgMSZiZgxoDhLQ-m3Iqc58RSBSwH0-Fea1qiYnNsjcHGx1c1Lrc8o4_5HSPNQT9trtGU1t0YMHb3jiK-hdAGFuNarUMf5gCdWCuh4bfkgGWkVRVR2-5B-daB5diy8s-sfZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJaF6pRyi6cYok1OQKysDi7Kg6HcFxE8Ph0kfttauzaP3fpl3germVHjIa4tUeiulf5iiAQURQ5vPXq3ckCZ7PYh5OO7C1IoL9qCnuixyaRkAo9FTo1S6x_emd75E2zSBjKL1sUAKh7wJJKKHl6EjzPZoNmDYt-MKujpw5agwOR9sJa0JdC1X3qKyfZG6-OANDGknKoLs3CjvUytGxupqGBqQgm7t9qt38-xWHMuWOsOH9audIroVPwZFHxskkH8jRszfavPlnewzoovFSPyLbiV601xqwjejW6gm8Uu28lHzO5xYlR7W61zvof1Si0ZTvx8i_5FCvzrn_2Q1p9tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGlHcEqoiv0tV6eIidibnAHRxSjV75BeDmLkiObKXYcsDAYisxtJq99iwSWMgeNFSp7aLtAze_V5Y9wdEdWjCazTmp3gKjJQkOWXKCAZFVv31DdHIfsm-u3oUIxc2ZTxCbylkU2UaSnCzlyJRK63TAZbhR52xXvMnCuVm3pI08GoaIWArBh_4d9dsd1JzsF_UwOTZzrgaFnaPkC53SxzdDVJpXFnxkhpvEe6hvGVo8JNlXFNIeocmcl5pxmhRgLR-rK6_W6Luj1bLCW6qXUwbNrQ4GtUkuyKfwO7njU4X0N6z-SOVC7Q6dy70r_3EMtT1JiMPLTnNg9WRuewUVh3Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt9INaTCSi0B2b4PbZZYtiARDxWUEal7fJebUFi1fgMcXex_489BcCj1eBg6fvSJnv81KY_YuVzX4SdWWbvIodSF0QGY80Uwz7u4fM0CF4CfkVAAAsruUhryjVll8pIbeRVwmTvxhxD3M0495sTWAsQ-V29k8WlOHYudxWpiZovkWzAmICTHq2vZ2okkP0oXmyFqDfWCEUmKYS883U8SnwmrvJQozii0iViTFTOeeBF0PkAulLrXVG8QKXPI6BfFKhRJrfWyYceKFe1m3PsAR96TqAzQRlcovcX7Sa-EH-ve1A78G70AEGYR4vAb0oylgVxxuA4iyDs1_NrE5vxOyg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=hT2UCc2p8xaB7bVvqSLWskOoCrzxXcvp7s5dQaqyNRQko7kxUzpL2eT4sf4Y4rEHhb2XJGod_vBw6miJCK0yv-ARTB7LoItQLbVsG3Pmb05iBNX7zFjAhg3NaZhVi_UWvP9pB8CjnTQMnW3BovcHkg04nwUgLIQTOcbjlvbJwr1F5t2rTSfMLj_1mqN4iOV08cZ8uYly-BgYUy1JgX8AlGsvLxKGLyS79zT-nKne_jMTNZlWSl-H36r7xuXQElGqtbKrAWGdmtGDCECA2lScA0l-FDIS_-qrZ5e_KD5H0Edj3qhTh4lOe-xR7Ga6FFZBI786iRPZnTAbEy_LWR3XjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=hT2UCc2p8xaB7bVvqSLWskOoCrzxXcvp7s5dQaqyNRQko7kxUzpL2eT4sf4Y4rEHhb2XJGod_vBw6miJCK0yv-ARTB7LoItQLbVsG3Pmb05iBNX7zFjAhg3NaZhVi_UWvP9pB8CjnTQMnW3BovcHkg04nwUgLIQTOcbjlvbJwr1F5t2rTSfMLj_1mqN4iOV08cZ8uYly-BgYUy1JgX8AlGsvLxKGLyS79zT-nKne_jMTNZlWSl-H36r7xuXQElGqtbKrAWGdmtGDCECA2lScA0l-FDIS_-qrZ5e_KD5H0Edj3qhTh4lOe-xR7Ga6FFZBI786iRPZnTAbEy_LWR3XjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI2n6k64FrO_FuC61BsqngoXdqNTQtmBdpPRQ-5teRxUFHHnTM8gMAb6PPVO_XvHKxjWbcF8Qm0HsyfQ5ius99pvh3ihOEmRXb6ebheAGlmJW6j5OzSkL0y9qIuGqY0Lpgs45ojO4qvZkwVaSGuOQxBvHf5wYetEKHqYmJuDKFJu7_7_woKjz8TSBH_ZBwoiNmqbfNjw-WdgdkSjPNgKpclc4Lf1ts7j-YZy3aDSPpR-80zYeAGqKzrSLx93-YwbFlUT4w5LQDmepmy-Bc8ZLF5zVgeKMNGkUXoekDF26jBJa1S0hC28lw6Q7zMdMF9uepWCIv6oQT4kxvQLiwen-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6AqzaG-8ni9y1bTFvzEPK_Q8uHB14Ax8TFey-LLmNc4x12NNTeKT61nioHbIR7KWzKn_F1WNXv5KmvoxYmP6oEqTCS_3XmesM2VN3JjdL-IuclvP-Sl0uNVx2cerI9Evnfi1vcGgVpme169NLK5VDdPrQV27A8krMcL_M-uvTlPLycmVb63Q_YKhNMnwT_AhOdVLI51YsPxzfqCvSSNMMCj4JJw6CTzAJzZqAZSK1VxqisbuBJk672KpEOXcBXMIttTS7rIF1XN4Z1o02ofRndGlYCwrmPnITsv4wmJNkHHnSrPhOmiuCr9ZjrqH1ypzmcD7uOLnTXmA4Htujkyvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKcV8h6XtROQtRAvuYHz_6BEX7QOGL7zpGuiK4zC97R2FWDiOCh-iKnRbC_P5GDYY9U1eWWK_qSZU-5bhO1_Wp7Q_EgUPn99CuaRKt-bEMwO-jsYPXeEXHcZaFGnWB-C4VwkJIqZA4ccT2C8O_7-hlq61OfYsnuNueZmetRkax0K8gjUg_yfK_SFlhcWQKvfk9xsp6bggzHjnNuGKZi6SQpro-B-I4jTJ_xTQ31UAWzsUXiKEZhX9IDNo8AhJijr_2kJ3mpCXzxTJHXDO_9NxosFIwcPrZZRVaXPCSoJYG0OWu_0yRA-x0FokkqDP1FUuuNGShUDksbvKq8B5PU0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MS_owz5L5CmE-mKSL1xLFSg3b3U5cIIa1Uy-r8fEStVmwjGHmtCJ4U75JF0lWrpCHTEzESeG0bK691938876Y91VsGASL6Pqq4YEpPG2NOQJQ11FG39g3qCkcXlDm2O54J7yBRz8QYJCiqYbU9aGW2HXoMKF6hYVKmnvK5nMYuSvygzNMr2zf7WpeEInvA6grioGBJg3gW_M_iEK2YgJKwOdEciz7aobTLj2nxPTCAzYhULQrI_oz3bY0vCkaWTICSOLQ03yFFANauZ385AJ4EYrV_gBnQQh9w3jJQ8ez-ZbeX16RoCR-GdWQdUeL7Y3AKa-V6i9UDp66T7T3EW19Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0ozFqSOl4KM4PvShws4EGIce6mPgu-zOJJeF87k8QQvtt8A6198W3F25-ZXNbowcBZSrOLV0OkLaHBAVBvGvKQ7arqqUyFRozs0X6DqVFeRFtEyylmgQ4XJuQXMfBrAiIHinaI32oGxftnLp1e6snV7_4o3vaPwhMmkoSrwISyNQ86RQtilaTSBF_xzd-2lKMziQ6OU_OeyRvUG3mmPsDBQFslA6cltXim6rbuvPjNh6tD_ozvZoYTFKKHzdy6coi3iYj2LrIKG43dbZ3AJpuabHP27cxlRsywnUZ_bwKIKcColg7RpE230ghii3EQDd9SZuHecPFhagGU1aZ4Jkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbDoR1blPDV-1fnNgh4D900DZiv60MhJZ0evoLFqoSIjcjYXd1MrjeGLS2IU3RC2A_Tnt_56jwNCMCspDJlG4wfMfuYG1K7c1b1w8SI-b4HLdnzRMIlMQYp1nHxYEytgKVcXw0WK4dWR_xVz7lFjBqzBtAEkWGWZIFXmjd_jwgwMu2a-GF-6omXW75W7ivDyj0V15qDuRpZleggULHCm2KLJxHZCpf4Ini2xwy6CPMLAHDjy6uYHBioGiIfebDH1Q3EAbKVuxMB_mk38zV_Vy33ZO4VYvB4yDgD7dQG6yE3ZpkSL0U7AnfkKJ5-iXY_WA6O778WZREkqhwfo28KGkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeadssKfgpmThVM-xMN5fvrGXkZc00F5vV1cf_DhlB2cPfSmLl63CfT__hRstW-Jx3DOxE2s2srcZEaev-SEjPJ1DSYNFputR8CK-jRVLQw9dUfzExZ4rfC2wCiM9qrteedXPYtf2zryuG6vs38359YUmEdOOw2kximgDHU96J2YIkhokVVm7HmdVFL7criklv-xv1QCHR1H6htjatYH02Dquw8aPojLEvXQbSyIoGpPOP50FkbIpbEFP5UJ0krTQhirk83z46-Onm1wSGitW2BDjWaonnGsjTzysjA6dp8-_NX--NPgCqV8EBl6fj03QghT4H31wo9V3M8Tndeqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUqw3LD_5YnckcCNjEzIisrCaWG9Izlp1CkQJm80d1UbR_ESc-zFUUMnK4zfCt3EK6CxLDpSzzvtiybV1k3Tw7d82naWxxtAN8RMOwoK__OW0SlR0qTeZVAvwKdmn8sea6bp9BPGX7GmZLINPP4BXV18YDgtqFdwqcAwdq39eHtZt4EX8Um9hsYTaD-6I3NY0xLz9JuAaWHGPepIPjOdgnONSNvC1A3Barj_vRSmfOq4kVRPNGJW12KaD9VhBeaGfYrOtg1hRScF5ArCqVh7HzfkpFsri58wZjGqyA9q2R0PqBLZUNHytFogHMSNy6GrLpcIQygoBXe0qp7gcw4RqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2ItsNvDUhO2W957YPX08LO3WHdxXstQ_o5uRPdRy90cNEYrSQCVpyAkrYVmeuZKeXV-Jh4C2iTSW9N-mOlx526TcbfcID7ePFLhvtVwI4W9pXedyGJ0vvozxqEgP13dcYEGeG0vU9UXAzt3joJYJg9MbKLUDm-VSgTAXgyUbfRuNMBFsgEQAKqFX1xZ4Aj_GEuGZ4zyyhNMXs7uDDw34l4c_W074-Feim8H1fY7LFas6waxKEfHANl4riSduLEj1ruWKXrpw2pkZZrbHrKEtQTT6D1suZPoVQFcThPEJF7SEF_RKfk5-CxPx95-_G19RudICP141W2b8gMdKLrwcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndkCoclzVoxksHFTbFdGkjJeMK_efk9vGtnRNCK4uEA0QUuVi0WqkwvMqL6_YRihxd-uCcqgOy9V8aD_iuocg35wnyePmC6YM3vyJvXJqreOY9kFJT91eW-5vMfU6RLEah2M7HdP3mgfNGUO8bcFhe-NYqOIbjQscPGZ7XRmU_hSrWckXZ8VetJdpbf4-SFpDYt0UgCEhA0DtU4hQPrP2uVgSPPwfzQJhRuxagye5AoW6nO0uyvxyrPk2_HlPkm3bknFcG0GxhEeEPGa3UqiLPv2ZZhTBb2eHFyYx4IFe66pTXAIIVUPi9GyRe6ZCukdfR6VLdlD2NVKdbVbwFWZCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5vm9TS5vQ-axOwx3VZd9F_hjoWm8SL0-LueU01XS_nBtjmI1OyFKzHcYNPpTWj6MXyg6UVKpgfJYDreSFC-5NdQnpOu7IhwhOeyF8S53pYHql_paRzd3C5_ZG3AQdXZy4o21p-up3sQYZeWJ1HerAxqWafmDPB3XaYV8UM56DsPGyEENI59SmJxEPyJ7RHqnu4kDNq8KnrsEkT9-NA-r-FX1sX-R2Xv4Jh5nAySCYWomOw6yAPU0E6iMXHWkrJNo-Hx8fQnn1taTvKbhNm-_eidBnxK-aZMJfYui320-KIbBHTBFxXWmukmF3cB2EseqOPCrtRCBHBSKX66_hZmdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YroumpuhFV2qRQIiqpiZLzKlJJL85QpLz0wjXAPdp4YtcZWVEAiWR77LP0lKV1UV9WW-hIgSijmH7RfpFSZ-eoaB6Rj60nJYsseATVbfqCThn65UcHmStktVHj4tBkfZmtqSzEo9ylC0ROKJ4ttgPqoF4gCBJUjNM59wt1MT5FcYW8eyzj_8gHvnM-2QabzyyDB7LJsOSARlotyFoyB8ur0nlFFPav_kDp4g0MBFV3IPHLN4qYG0bG5UR9KJkNTPHnaDc626uJ3dU3piF_rbC4L2bW6An-wuAX8f7Bd_-z4UlBVFCNhoM3GUiRcj6fkMfOjpqPwVYvxCm8KYu9OQUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QiNxu_A_1PI8TYIoZPTbYaL7jKr6Whxymy2KBjYOxHeWUFK5tRuCj7KVuAwTpm47OynRLA5goCxKo9EFChZ8gOUC3ZhItKXTuaIMtaJldTBUqGWv71FiYYX5XygpVw5SXQuO-X3RFFpBrBJ2Re6kQmfOhP8MP5Yb9R1QnWBsR6DeNwT6SyYStwSJeXeaBx0U-GXnsIU1QWTUboOvJXkv1t3zLMPOGIU9SfPwpc9FbCeLt50MZbpFyyIflvX1s3Q4Rq3lRLDTd0yAra0VO_qY2agqIyk7nm5I6S7Tl1ShH4OQdf86cVk2Y7NyuvV5Ih-JYit6rW7jFCtjElXRzq4sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stICnZmRE8M9OGQKSJKXUrgMpDOzwpHrW74Wjf3pbI9SW7Seze7rsLGehzONnnUjeO8QL6H19BjiGF953-YXcJCbFlq22NpEh9vBwWaRFaCKTFl_HzxbVxMIZJ5wtpVrZiZsVW8ekmxFK0MtKhR1Vr_IHA_PrmAJrXXfjDOdwBF9m13ZofI3QwHIca0yKu8ICMWC70Su7fLiJq5PXkvL363HaPM1KVVOPmgnen88Fryc4h4pg9DqInKkypTLyzaVCQ7LPJu91HnVhfx2xcu4ZB-vbm7hZv65ayWbfe_qZZQB5SAq8z1MzlJCsYd0R-BFpNhvKx_bRgNz26vN32ZR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POMWKbjHPn2rXOh_BHbpMiVs0kTQyh1fVAgzZtV20galpLe9fnBdDKaKdqMWlroPKWjDronoy6V2xVIySBty9EGTJuXC_04rFzOmwI0aSddA_jOn3upnmpogcH5XfOvo-XuLKAGh9MrqMLcPt6vbMfzP54KnFDhR3vgD7KiYSBt4ulhtWz5Fi4pJO9uo2B__DXWe7cu3gwFph2QiXKryBHnQXY-1OS6r7teS5ocQliEdchTDQ6rdxlprNJaNeaaOsiptAprATwBP5A8KiCQLZ5MaLrOMXDi9Hme8qGYENI3wNXf9SV3P2mtff5kTQ_2laZFS_LdXpEe9yk7PgTk1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rd8xP5dhZ8_5maBBJRZMEPhcRCEp-YbqCNiva9pCfK7VqdFZQW4mvFJ7Bje8CLg3PgIIp6StKqqH43jmLSkoahWADaPu2iLIJnHmJQbnUFV-JS0arG_KuNLkmo_DXtG0MpLvK7EIL9C6WFozoQmMUNallnptbIk10W1T-BGFmkzSkrcKiQERKe08XtoEv1195TBzdpQk0Zxznrh6zT-UyR-kPXNAn4198wbMBDys_eA0meN3gjicbBBEfDJC12t00pkNJ0Hw7nW48akDX_77V-ZambekfCAHNIDrRm6lICzxXDKQc4aizX4R6nGtXqp9Tu_9CYlEwgqKmwyVGaPF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBWwfqZAqTj5Ve7Ii9pnqUr4KdZlrLoVckpfvgDciHUylJaiC155elGO4Rr1p4sWEwjJkUgXJEhx_oIGYbSa-Pg822QRU9bvoD3Voj3EwnUIWNBd1aCYU0_iGPdtKOzFIASdps3n003kP2rkhC4PHlB0daRTkrWirP6UW5MYD9XOq60gWGDnu1jMPprYizBm7N84Nk1XWmW5CfUF9QRQKkWE3SrrHZwg2wpQP1T4gMFcQbHMNCs6wj4iNIS24sQDFgyV0jJ9-OwPbKD6_Bqp7QLbRfAiXA0CLr4RvNGjIi8D-0ALxKxztxMT4C1LRiYOMRo9tELc67M-GAzV-V7YUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjyaAJnU8HPy23mYSlCaIas3uEAKvnFsL8jbHugTnuI7rRMP1L8JwPeLb7lX2O__6UORL1p4_-_Xc-N2bUtnFPz63_X89N8MeFballRU7icKf2a9dVCkqP7yEttoYc2BchPc1Uxb1iPjKtd0tKeTAfoOZjR16hRzeTAVh46q_j1lK2vn390WLRQimonZVWd3h7436Q6_ldQuv3hE1emOopI_92Z4sC-q24UNOnOq-hZV3_MwSDAL5E5ALpMu-jeNKHmZOHK1p_DH5pIpcP3UfDlX9u6YqKc2JmXgoPTxLQ1N3UqMXLV6dFKsQJ5hJTvRqgA3glnP3sfC_SzWvNFU3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIAO3iLhm6K32z6kuj_yAS4EQTBGxGCyJSFiXJbtmRmsQ4atD_j5J3FJCKLYM-XTT83pTXFp5cdo1VouLn3JTzCzHQBXIWQAiPmHGcSpDW9dqnI8EVFtWmiiVqo07-WeZTRA2rggqcVcOMc5-8BLC25zB6-zTaPdnuRhQ19YXE20sde1fE4gOUvnSsvbr2mRqmzqXdeFVxTLPLGdUsApvA9KpIP08AZ0hhvhBmhtqt6gFd0Dl8ReqFCVP1w7jjOp_1beiy357tVSkvB28uQfXnf6iVsFRo1v2mcfv0F87Kxy1FxHmkaZVekJ7KhtZabaxye-nvDKP-IqR-Be_h1RdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTgTCkb6-JALQOh6Lv1l7h_q4AUGsoD3UzC9E7q_cBvcYW4NavUjetsDKphi9bkuY60lCVH9QvTsW6X4JtS-1fqYXIwPwGK9vqlwj57LpuTLQUpM2R2aYokbXzoSlFznfZX7ZQcwsQfTZ0pB6Ad0Mf7Wgrbc0Zm1Q22NA2xm2Pcl2Dt714U9E_rJ25LLQW2PW878o0tnAowGyNbFz1m8xxQ2fbTpZMXq6dNHjP7Y9BkkM90E35p0Bhl3HRYDsDbREDAN-y0lxZShPtqvbdK4BjU9Zgt4DlWXPDSXwuM0sZTpNLxjqd9HatuB4M8461nZMAtB6AJreMFs2tA_FWDk_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xisk8Y3s2a30vyiZBHcNW0CAQr8oL54p_aXrknkMzWhvzoOqVHXQROZ1KlfNDgHe7EFjvWlV5f1UloxtRNwWNzgFfi2cdNnCo6w6OQGqt_0SUKIAxlKRobAsGLbR4WgMidyIIoTLC4kDkkpErRnsq2ASe6lOaB8vGj96vFHB_B0SQECmGbs6jfUMIBx1sxY0sSNo-1N6rD8HFOBBB2Qq3DCsL1RGYYXZC8AiQLGdlmgjI7YwuTREBzN6R1bVae5XmH_z5w--w8vuDQxKGjnAkXPQSd6q7eoiekzZ5xYKSkoVg9GfZ4IS-0zAGNQpZJa4qKcsL2Co8DuZD5oLqZFL6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1DgtRi3UgeFKCZfke2w6Za-bPHW44vXRViNOo_UirGsnPZx89i-TddUQcZX1TGxQb0CT11K1ckavwSsqZgWQwS7Q-APIkUv5dKTaXaPchYuWDB2J5bsEH__HnQJrGU2vfLEbXfhgRP_10rLTXZNXZ6gGsbyqr4jp8DqXvsd7O9pTm-ogCXZ2PwdnATh4vn7J-STng1XasfmE6jPq5uVSFu2KFBUsWBPC7eBgqkCHE2jkzolkzTzbSrpuIsbarc0oUzPOHTCsEdjb8HxxrwHPxMiTLiOlA5s0DGsU-fsnlkS9w62TN60nWhDeXBnuiQlOwQ6h_wNKgyfdY9aN41daw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu-A9FkzAFgc3QXnYPjayjqR9i34JjYM91drr1mbXKooBTl-cGUALOjUZ3vX_IEno8HfNhdL-dE0SOiWQmLbA0vuRarTX28CCx06n6ZqQaiV2YdwmyCTvF3QD78BlUg5DPJ0iZiR5nk7ulq21y61L_QYF52qofd8-3FPfLB2_vmTPd6vL9s5lOCv0OYE34Jk_pqV3L3Ggv7hwFyFhtuvuMahEGnegLhk2uBBR8kOmUPtOFuGf3WKId1Xv3g5qWxl7JVHd9vblXlYpk5W2_NVw15MzKYxyq0eWCRcakBdTFXSPL2Pi71_pqlgMZxEZtdo4WJXum9szIfASIZSLHDijw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbbPkN75sNyTl3H_wbFhUUJ0s328ju8MOQH_4UQJ4QsxxRAqpi3NmeIRNn5omn-7DLpBOUIxpAs0VbvLw_ocFWxvAQtQAe8bi2E5SwPuUbKmSGEP7Bn-6InMFKGgiIggX13lrPr0LQCCe7NEs-CJza-XmMQR5iiG0f4P1rnSvFHhATHypiwxgKJjVk4KDoc4lHp3jjj8ddkn9dIxqYZZ1YIK-7mTOAK3EjsUTrZw1nGUUdb0B1LkYp3eJzUwlcYDUXmVdc_cEFwNxEBvCUsLcLOeg-rjvJcS6micE4Yy7pntLWettX86XOJWbYRCo7qaZgH3VctfSGqTULYwvPw2AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeUnXPx9wbPTkVM9BXY2OlODp_SUCz-xUmvqze1Ec1iR6uYPwQwkYulZgygLs2crpDF2Ocy_eVEzBeosuWGA4flrXCQ4C8-HpkqFpfakOXVLJELNYjJnBRNUYqKl6gRgCQCYw7uu4-hAAi1Q5HbcFGY9X4hr2WC3N_OBE0sDy63Z0zs3t3gMIl18QLkmqtn8jIXFx1RJVSQiqeZC278jLj_uL04lIOt3PZno09WDFNVyupC90z3F6UxuNyqfpM_adoBOJa06sDeVriTr-zE6EiNdYkOifVElCLWvVljlsN5jjV3imhOuVLp121pMShJykedxQSVQV3WDaN1VGaXSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1hHRD3xwFCcWN9dCwwVyK7vZkzac7aiVfPob3tjYWbM4ReCBcB6A6ee8EfkClc0YFh2wDipWeAg8QdVol5s-6Mv908u3JRnFC8hCfH4HBix1P_5UqCdF1P4hRMjVtDo2kDvCIximLm6vGjwb6byzCThfnuOJmsMq3kzMi0xmBrGrUj92C8wSvEUuD5a80uWXdn7r_cUhREHEvF4kfw4sCSLCUJhQrrBxMZ0sQ8WlCgHJPk3DH9KTbtOJ_mY0iYmzulYDVZHRfGzVRx1JhPiwpXbdge123dP8OHyfIp7nKXdnTxbY6iD7IAKITPuMDEpxk3xSCnl-5aAwneYFdnshQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMTZaDkHUKk6i1IvaFPh-ktuUPvbEXoGDbOF7j4jAX6umVKA3dqdMUGP5F9rdm9skUCg4jKen2qk5oRVlitusOB5fPCEzDkQgeVL1lmaT_EvPu3qluL-diPqgFsp6rJE5bFjjYvOo9ivQlV2arQ5l5hPesPcjpBzzL7rDIXvYKS2FpEXKtIavS0ZHRfZVRN1C8WOvUEPZZHcnHP2erjYYA0g-7YU8_jMHvs9QZCLlZBT4KFQMDf4UfN5jHL7ZcduJs89oZidZsJTQQtekRYEDgRD2hmkoBhieMc3eez26sxS8272tFzRO0WPVBHWnBMloRlreEj5IoZtzu5WChTC_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaenpmpBD4FDB4brHojYGO6uW3hNbiLm6CCvTfAen0xx5znRCbDAELwu1tht6gJUj41z35Vn9X58v9zGlOSXCr8c9beFMQZKH5rF1Ui5luUwX5w7wYizrIHdw3KmDozl_L-iwuS4v3XJ3oiOHYSWAsZSwrlA5Adr7GmRzn05atBUjx1F3hIBcvk5XPvHvfuR2mxlmAB1bKg0ZACv48UVgdcC9RccdtVAuo9KYWpVfKHrBiWx4H3ae2Z3UUjo-mKmT0fUsnvprTI9n21CaTUhJXoFArlDkuz-eJHTCGc278F7ykdv5ET22VBhreFynk8GhudLbgdUJtlC0K3cSYVu3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2HrHeEGfR_jVPosNDoJ42LVzEK5pzo6gE4_-GC5FDbAxUodghYy1E9wJ9zrqWtH2isaLUVg97cmeaUtv9mvUV8eMnHSIfg7EG7hkoBDGRJkMMzcdg3ymQCCtn-UokoUpx4XICy55yPQ9gVaG_AdbfTSO2QaLv5ze6wxFAya2FTQiqNx_h46ePyVAO_0KjkRIqSLrCGp_Q8fEsKkEZsucwjWdtTjXU9rkwZlmw8ZBpj_aOrGzv4dXCk7u2sBcoEiJOmR0d7ZbvEy-TNTTMaDHVpAakNuK7YLHmxS1apvNKNf3sDknZUSAUN1iN-YDQ5x3slF0jQyVjqAFl8OSCiJaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfETao8T-UPBinV3fz7jz6dYSeLoTt9A3B9UBIbW1pp1AQlfskwDj_UgZKP1uQDc999UJ5iKnolZ3V2jYBDZ1T-h8gb0ATiM_P0sDXSoGpq77Vbf65DtVmBL-z-YF_sOWQH-26SAT_SrahdXzli2dASVz03Bt-gAtkIF-Yhc2GTpWAWPHpBIthNjZY52L7M-HtL0PKteZWvQSqrDpourPtx8L-7oppBH90YbNPwr1jbHlFQGX_DT4E5OFWJ8lu0FtVRgCwsuZi1fOB1PR1CE4nGQ55rGigWtKRhQyBViXcBFSeEze_h08OdsHLJAkoYfHfMR6MEcun4zGTwChIxc8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrZncnkO1n2FTcNy-0G7caTA7ynhSIZNdTBY2V7PyB9Gvb0t0HUs-q4tyTXEA2Z4voM1L_60Ggia4mM-Yl2Dx9J6XVZBO_f6RjuiYnroZeiBC70bmFjYGuMWda6BOaBLH0LKJl6vkhWhvlFmOTPOsuxIamTuQ53MJekmt4XL3pRPNyTsfJStx3vjxkjLBKEhp-yXOPRLuq1syBKzVClxuR5O1IOeLbMKlLGPAg-aNjC-9DjTyuVwkVgP1WXDkU_xGpM0TOSoukkE5yg_BrS05rEP5bKYSVCZ98nx2ngSGdmUiP_oZ0j9FwDY78CJWyCtO9ssPVBxHnNeYBcpGz105g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEFb63VbHZBYBhuglq-wYTyR-XXLgW1qT97jcPMRoLjaa5okh_9x2KzCPvRu47KRbwC9eRwAdNTyv3hsxWKH3cpiLYMMQJCyMQRW43JC1TfNo6oy71P6eP2McA23D9Z6RSulYJKmA2nxDPvwNjI-ScxSqPVhpkwooGDUEaUta27SjkyzkWnMSITzms5SGfEF1mKTG2z5t2-dHsVsaBc7QwBVMkhk5Fs-JnrjOjyjvYjPxIWayWIDN6Hq7iXlvR_uluH2jTXWfPD_nYrAGKtMxdYPoRxm5njyZFRKY5hTFfgvdZDRq5zFth0T9kYwLX0D8-cNVTpjeKuxDlCxzqf8bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJlOZKt1QXP64evkw1t9yjUYwVoQeMkHk9RrOBRabyDI-8tzg-OVGig3mwcKPDEP35DkAlIUHMoc3HC0-o6cD4EHyT8fpOUtotVj7H-a2Y0lBU1iZlSI7LnNG_PFl77CCGjhtdLgnxX1keAxVAoxLjP-f6KKKPFVAv6V5SA7y_wJNhbL-7u48FC6EpNqnnREl8qJXaZIBrEou8Vz5PTV9r-lSqU37rDueK1yvcSO2BIirbgN1Qk3Rk8rUfkxEYOXxqETOYKWt07RpSzUpCSGuOq9GiQM_ZdnLszn0USd0m76ZHevQbrsGxFNB8y6hAqf_Ei7eNrcqRTm5AHjB1BBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQAp6_c2TzYg41OLRD6KaAUNQ1Mtg8YASSNtOcKPvmUqBGN-9ymSfNrWUoiYhLEHzPO5O0qnHADBwiXuw2kAf7xTmuLjxPVh-jL84N8Gaw52B8lg_8-IFSkRfT6YhLnSQnh7A7diTxK9QpC5e6c96YytZRhDmgTBW35GUVwD7XNZ8gK0NFoO8pxv8y9pc3xyGfyQMJ6MLUbmTry241yYxphrxOCosKqndLx5sycRv-hsdfdJtBoacN9efEzRCeRZU5zh3VBP24aH0I15jdIoqGPDGjcxGpP14Ggqfov1XCf9oIQIazxQwZIOKrlCN3MFNnqHPLXC9FovDuGcqjW2HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyoTTq2r6jyOjcE5DJAH_Hl893XIWVbW_5udg5lW-O21ukCi67UY19VFkXCokOuBs3dC57gf5jMU_QeOApBQb5TBs1rBBS6XhyLCY8IAYBKZyoLxtOKI6wb7c9wWabOQrEdCJFVBPObx_sYMOPD4ZJpEkBsCeCNKB5ybJ5HNbwKRkt6Q1poMwxtfImma5Ik_kKYVm-qX8xhN-iB2TatZxu-t9_RVbDSBUg4bYt19nNvSKNP2-SkjjNISf2jQ8hl4lYXrzB2Sfu85uHypqad1iY3fyBELJaRptBNCZAi6uVAi8ivvn0AHgmrv0ywqjLZojxXVkQ9wEEHJrSdgzEfXvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjQNEj_bDlG4Wz1IR834726-nNuSJri7B2OMMFsnJ4UYPdmddda7vBZWRuOELDEk22rjX40bDckXvEehhCvkgXcf-0quY3zZM2KmeOXPGacY83Bg2ZcHamwtrLc3IblLgBFzrwbwafKIbsM5XOKGgGrXG_DsuqJSlx5FNY6lvS_A9K10jigYCyKbBXBmsLxiTZwkESO4Pdz7mkaey5kU2fUeqlWCMJBKFngY3bRRcBg_j7aR3yUtmZA1pOMEp2CmPUOy-taRaiTvrCS2sRlL8vzVO78rvZa8sfTK8fi_NhojdWQqBdky3H2biuIJd2j_ypL29ii5Afk7dZBUnoz5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afD91RTYfr0_qgytlUKzCMDPCAHMIt27Fje6dYDW3WcxE8GYT_-qCNt4mmrOfcQ38Z28jfy3QFSHSDDHmbaSowulBkmD1Zg8KzG0gIF_ugz7tRooT10qrzT03SV3hvfS1xbUsWH5WNaXmaeABjB-Rc5fLTxWDywOOMOCz6qtb16F5Crh5p7YqZA1M_Ed5O2MMkpsunjdiswgQ8wVypwnNyAnxRg418r-U8p7CbXoktY41qZj_cgVD916QOFq32WGqYK1Pd4qxU4U3bezn9_rLZgYziF7K5kVUV2t9dJdWv1XD_SeSxEPV6EsE07YGhU3jPYs66yTcnZ6IvgmTF7eEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmvqBx2fKh-vGTpjYjBCGqAwHAZtsS8Tdh6ksZjGUo6Nl4G0dEM0CM4BCrJpHsDdn5siDgNLL4SGFDXwfs1V310FYYZmMJiVlZvPW4DZ-VnTQ7OuBCZRSY8TGOHPmuzwRofg_OufEB8DqZv36Em4_PneMTDCS-KX6qLie77oKB47b92ptdvm7EIZeqQOQTamFbzdC0l3XDJyLpOECiSAOZTuereyR_UmkkyUnvlAHLKWku7Yf02N4KIM43z5BDMLVxPfQdRneMkAmn2KLChtQKCMuqKW97KpC-D7BwJ2radVsX-PoayvhjEO6B5SBgG-OUMA_mOKW-UmxPdMYs16cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3b9fz_tn9dF2zxiBO2bDsGvCc3oodLIaEsiPLEz3bEge4NR4BDqUUXBGrRVdHlgcOkGYmS6U9tQJ2EDCYbQ8i4by_VuFpgSwJ-HCf_CyZdFdLz0ArJI2suuh0zCYdyppiBbO-nLeKqg8527w1jbJHQ5YBVYirLMOwEbX2I5_-0VGOOzO7nC-LOvXQtp9laMLjzqgSgWBprVNcqkNQVN8ea6MM_LBTdpJwH1kUelH_dMBnegQkb1FIHncHeXptbRqOqiqv_FPPub-j-oHmouL-3YNa6qjpcljbAC18BFwQYhrt7LpK3u9I1NEtSUeTiXjeNw4P3ZEOSX5DErswZJvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfBpjO6DLxelqUrZnpISilhVgrIkxYjVztfNivGcupuwUNp6aOPS2XV7Czrxt-8C6ZTmP_HYhmhT54poqXyWeoH0ivY9tc98LwnQLwQByBXeQ3dchNH58GAlix_SgvTlF8cI--C0Ayx5N38K9og70vEtNXbOOj99P8p220b7qNFr2s1MgpFCtWiakB0jIQ1ZlaOlPREe4XQlUj0dJoHUbozoxIYMJAQMk0bOYjM9QPabMGhMSGA_cJy3jXsrcfQbUNcveCGfnM5coCFRq9MEJzPMbW6q-BuncgGfo6OLjleBaAFIg2LvTx4sNtW2EVyEcFu4nnK3bxPJOStlfSL4uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGdO8vXTR-8KhFUZBYUkrdxfQt4kKs4iqdJ2UkqFLzl8mQf0IQxyN5RPx82PgNBDn83UUzLveaLDD7ocP8EnPbNWAcWQ4R-FJY482PbwB_PEymxN23Dx6qSbDWFzWU1WmbmJLzkhBDtzOv18ZY_O_neuUhtnwWv_IcBmwF-F0XbbXwZyzJL6tUJDXP_A9n5s0mtHEsGteQGuctj7CM-hL9NPO2AQBpnI9BmuVYQjw_cguhqW64YuaPJjtWXzuhZdh690Mzb7qAFIFtlBhbFLThTgT6Ul9EsnAntVar_IWClV9lGy-CK_QTwE95KXP8Du10_X20kK9nz2oD_IzMpcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5bEXkA_FDjX57ixxs1aE-sFIcTC-Eu6g1E0_JqeB8mlfw5DQhqkswACOfLNT5FRRdpH1f6E56Xl2WUfcT4PGno1ynnmxGXsFOecEgREXby3KVxQfL6dR-RiJUy0OXJ68FgmvKqRUt1yoiEc6AlEBV4RT5_LWoKha9sJ6bZ4Bsq4ZDSlUHme3hv3URAHQFZ8qE46DDmnZXfXOXobSyj_2hZgW2H4OL9SyJyMaEYi_uQ5gJBNw-O8_bvhYYZlxWDVAEK_VTbDdnp8J68r3z_rqhUEwbVal3EHypZGKUQ3Yt2UBvNjh_tPdXkIrHYC9Uh33Sycy5OjTCrq8BlrYRFfmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEa8DlANes8vv2SLTBw6eSvsX2LwGdevXiSude7Extypmo1-1I-Ev11dSoqJd2Y77tmDueQuwC9PZ2uEJcH4c3Ouv0f7tC84RdlHYZafRVh5z_wv731tCxD0cF_6hLphh1ktZxT3mNmzbJfhrOKks1QN8JXEnA7Wdii3Xo2bPsh2Z_OjgIGlE0HhJwU1jL6y3uWQjPpxKEndBL8YJZi2636s2YbwqpN8g5i3AcnHMSz8MBIx9WAWmM0LID2-d6xwfFs9ovTrIEo_8r93ksDn01ZgOy9IEOE8bawLmsXfeeccSUVFYvZli1it5EctDQL5ZhGWUtDZ_uwYKGRo8QEEjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXwALNFA-fFiyGMF7GCVjDBoQ1949OChy24m81pvR8wE9UhRk4YPbdJmh7lquh6qoC15uwgp6LgML9CjJAvCe02DTabAG161HH7xiA4TMjQwoLmrMEkolNO44whH2hveC3nTYv6AO35MpFKTSlqjzRtcqkd3DPFlkfz-b6wuBCpt-qXP7FS8oonYp-quoxufCi7luVXTqFgdhcTtyrQrzA8_O1KAMdINOmy6PGcq8gkB2LSR_C-ojBRajCUs_0IPya_WEQaJUCR1WGqjjw-VwCfME3b-vh4FYR6uURHLxY7Jyr-0ptQhy5jwsADFDtF1a02imSTcKJkm8qk1yWeovA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MumXLc6FSuS3tlNDK-aE4tZCkbWNLCzEMpglO7hrooOwhLq1ITWw2jboM6N7SyHJBuyzTS3TaNj9n3zQXBxIyj0AdlbcxT_BldO_pUYD8ZxI_3AjsPri08yEfQZx0OUBcHQ3bdxt16uszsXxxjoZDf91Vt2DLGTtXLLBv4DkNaB5rEJ2yeVRSSgxCZva60fGDX-i5lTNjOi1qHRsmxHx-_nf3ULaLQ9y3kRxbctG2YppjJHgaBKjWlhJJvpWKMr_NC9ktAJp-XufMJDiFSGNYb-Ho19vV1v6zJBkd1AC-dXBc6t6r0Mb1k_hs2km_gFnjOHRwyFLuPtGki6dC4rHiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpkTxV9MKcATE4w6Zit_VZa0m5RIfwkY4RCLnSnfAXI2jQ7f_NXDtKUBVYMfcb8kFBD9WUVY-kHjlS90WSUqnfmNHQWUUQSaM0tFJ-_IuhVxdgDQSZhx6-Qw6o_B7HCa5gUW3OLkKcX8uGxlHKYqM3FSevjctGqoi9V87mtqF4q7XUd0NTlw74UZlQEK4GWsG5AbUShNQ7MUgFxh_Nx8T0Qrrs4BkD8YbQUqQFPNhI6IEbVAnf3zAFggd9uBTORww-CwjEvP2TQ0CqyLZ0XAy1nPz3xrupG2q-m8Xruqd25SCCqwTvO8E1xtZgSCbJMf0Vx1V__Z_H8FG_h7NswWkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Hf7PlvcZi-k7Dfk_cbtBLQyv7AbulOut0p0FRoQcptI3KdX6VRW_j7qwFw9Zv06-KB9FV8w7sHPF1PU0rKZRZEnPNBw0tlBW7Vz2M6zzjOuuC0yDN2r4q5xtP5OlUNS3anzXJjQ3xHf9_Q_VTmzKjYflfUXIUzfWL4EKSA-JYjXzCE8TYOkZKA7_jxFQUTOTt277u_HDH0CwCg72if5ByZg1NWktJYdLRCPGKGcWepswUaNtgzpMtvw8Kgz4iOYksgVdk2ydyo2x3Y9iE667VLBDJ2TOKnVTxqVjVuzdyW8exkvKAXvr0O9StMlincWVpM1P382JaQoBntH7dMkYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Hf7PlvcZi-k7Dfk_cbtBLQyv7AbulOut0p0FRoQcptI3KdX6VRW_j7qwFw9Zv06-KB9FV8w7sHPF1PU0rKZRZEnPNBw0tlBW7Vz2M6zzjOuuC0yDN2r4q5xtP5OlUNS3anzXJjQ3xHf9_Q_VTmzKjYflfUXIUzfWL4EKSA-JYjXzCE8TYOkZKA7_jxFQUTOTt277u_HDH0CwCg72if5ByZg1NWktJYdLRCPGKGcWepswUaNtgzpMtvw8Kgz4iOYksgVdk2ydyo2x3Y9iE667VLBDJ2TOKnVTxqVjVuzdyW8exkvKAXvr0O9StMlincWVpM1P382JaQoBntH7dMkYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwZ-JTcdFArw7sf-VKoZlziCXfvHDH_1GEA5W57GBqnF2e7rBbZV0je8kHjGNeySxxDEpcoqKdscmeYQl-KvgXKBRlEP5JpKF_bKsRnfrdgbXUsNk7EDzH9VaTpyLaHLaqZjY3YoCTl3Tp6DDCXqymjbo7l7Wug2CONVjgtDv3MBJwcN5DDsnaHnvHyh3o6_fJGgqoGypufFix_SvYhMnKNrpT8LYwxC8SbppfYgnP7VTZUaFcrbSFn5eMtxMPpqpdPWCb5dFcY6NhshJpPkcsF4LR_-AGJT40qLQ_1SHqWL9fk3jRlBO_UulYeX0Z92Z-fwwKjay1QBXGGrAXMe3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3NMp4LiXSMSH43iQv0t9OQk1TO8PN53ATZ6x2BtaLIu1Hge36FHOuQdevvTPyYHuDsAKKxkyLjgptq7YGn-2aN7j_v29w8vXzNPRmosyOzuDnaS0oKfy4uTvovoX7vU2FyNCyHoPhxYZq-R57hs2PQLwaAZPFOCBK1bo4-8utL0idO32tyVYRw44rnRXtt4Wjg4Yr0pYpZLdUpNzLsNqGaO7scJoUvW7h9sfxA9m8-zuxcBT86kghmOPnszLuSUQ2TsPtM7-CFxVW1b6GukkAz_Xnboea68nHObDvMvMI50K3H2mF81GudVtvOeQosRjvLxQ7JhmInZNeSk5usMEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1eHPXzgT8tCQn5DIm9nFB_nN4ouNNE8ExS1QGTG23fqSRjvz5V1CtiX2slLg4UcCkuXJ_6sBMafttBhaW3UWxFj9PqiXstJmKVudQFQD4EPUT52nhFcH3OG-kR_l39AJNxxXB-XMKkbrdzr7KLKaLvVX8meTDEPKAa_7PM0SehR4ymSKAsy15p1kgSElfbrFnYG52n6M8RlClDytr8l6hSDn4ycCwaqtXj0YPDzQFt3foRAe2xyYwMpCAlSE51p-TO9-wp24wzDmFITyYmT83JNuJolMUxtAwA62X2w9zLLQFeuU4spChsOsY7hcJoRly7752sP6g2Xx6WBqznoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KF-PoHVnrbxLEJoNTPFAlPkBmdQkenMQuHRH6s6gUbrOI6toLHbrOXFI9Ajjuejlr6NdYQsbZHDJ3UHuHcIKxw4j2Tp9giGWEMdkizlnJIgwDBa7slaLBsgNOr7UlDpjhNyWf4O7rzuBkMOl6dITPmXJCQj9FT6LXFadRfETr1VOdnDAc8RPZyosRLyVl2REgsaElUTmVxJg8LGS_ETGqrOBQyMD6h3gL8YVieRYLHOEYDpVn9uzFXFgmdpdxD9cAbCbQKiuFmB61gFP-iufum3bUBiIR5I-lucbyNGAgqYlXdY-G9-8YP-kaOBZKuyOP3XFhCGpAf3yGw6gaLMDqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUEPD2fk7OjTO7os1bgxbhQdAPQwC7FOIEpreLsjH6bf6TjGxYIDh2GoG4ie8Lpkrnsw3WgRTH1TKhonuQ45g0P9zQAIZVa10lMl67ytbMhaQxGNBmUA9lIX1e0UUadoHXSDnPjR6sYEZcnuM024tX0Hl8V9Gc07YXL-HKAwAJkPT9XEam8CYlRpEasjIFbX7g7iMINJs06Ly-vWos7AaO3Q5eQKQZ5Lk3gUxWdsur5lHKJYC8eRLoZBOZehWL5tqxdLexUWM-KhM6lQtWzVf8SkdOz8KAUJggjOMbTqob5LCa8se5YnP3yvtchALce4fzkmJ9Ktd0nOIEq54Ujahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMyWB7e1nNvytShROGObm3SAIkJHNQ_0Lafmim9wJINYvIqRvr7lrW00ni2xWaNkR-nEiffExNz-K9jdSkIlk8WcwQedzzBf56S-vgkMyJyLQP2owEZ5tQfJ2vif5b1eueV40GX-tu3EXEPj4XYDz3RbXb8KLxhiOUlFgEy8h4FjGl_vdCKwA-mWm3JGAl7mN3bT97pXk3BpYiSCw4QgO3qL81pYshaEZqYGKD6Xi4AoDiHrxbjw5ID7VWVT-2S8f3yfTupOMnUKa227VBiUQxsL_JZtWhnw5uUws_JvHuLYKVLNeCu3DH0r5r0TO3thLLsEZ9TMceMLydmpDXBy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uekqylLCDqEgCbfUDlKLmbZNiNHDUyU3imAON8F0_4Jaz4yskPE4bxepq-st1x-Ssn_4yS5GdYyqZ2h3_4eu-7-QJUmsw7S2NcGonjSfjbFW7XgVSZYnLn1yk_TCzqsKiY-zOJ6rBv13te-dc-fVcJDEObjFggMhRURubUd8gf8OxQ71kGSJDnvrn1UEuySuMndw6DZvBuzLHVg-omedARcfMBrGhHLBaj0v5oBI4Quh4x-wtGHvnPi3IbMGry5ou6XfLZ-SzdJEI3EnD_rQOW5Gj0c7IalBjS9peQ0vMseLo8_laRDjlgAfzrrhB81YRxbuJE2l2GNyf2WHol68NQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=nQWj_e38xya-p5EjnHR2eniOBxcT7eP2F1xCF9xArHvn7wiwsuwrFJo7_g5QfGRdLACLOrR01Gdb89LSAaHJ3JOFLX1LfbKQGv1sUIDfMTiMQR0dXiYZHdgogzabbC4XfMEUwa6qeFKFaXAgAORN-ESyuBwEZT1wRFTjqACPXh5PITZnqLGqNbbCBdb4owabnuSpl-FmrO7TKqnxQlpkmHZG9Xf7sRTMl0QFfJ2WZdECoDswxpuCya0ty6OQJgyQibGT01E2oXTwecXRuX8zt3O00Zypw8WxtyqPYd-BtYt7S899DOdazrK1HZqfWMTx-S1ha0-d6XYrKBbAcQlwPG1AFuZWULGhNBo80wkruGfqOSoGmBUQvNAILzSY8czmrDDwBIJqGVLJZBd7yyPJC7nGwzZnkTyzbUFZkOY6P7qwB9vhpZLiOm2Jw_9aiuZc0vjNbZi40SbiBPYaDGQXlrSpqeyN3IV0xJLVEMUuu15Qfsvuu9yOzgOUw-bUYRmmz9Hgqj5sCJl_M0tFrYhWZdPi2XE5TsxkWaNz9JkvzzdfOtWNP77RsVOgS9xpI-8kY73YKPCuyXWbC7iUiZkRMj8ootOQT2QAOjDFVa1tr2fvu1ovv0OAP5oA2QWf7Fn6I7ifo1y3fHfY_jlv8guasf3PHx5YgjUQdkia8Cr8vOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=nQWj_e38xya-p5EjnHR2eniOBxcT7eP2F1xCF9xArHvn7wiwsuwrFJo7_g5QfGRdLACLOrR01Gdb89LSAaHJ3JOFLX1LfbKQGv1sUIDfMTiMQR0dXiYZHdgogzabbC4XfMEUwa6qeFKFaXAgAORN-ESyuBwEZT1wRFTjqACPXh5PITZnqLGqNbbCBdb4owabnuSpl-FmrO7TKqnxQlpkmHZG9Xf7sRTMl0QFfJ2WZdECoDswxpuCya0ty6OQJgyQibGT01E2oXTwecXRuX8zt3O00Zypw8WxtyqPYd-BtYt7S899DOdazrK1HZqfWMTx-S1ha0-d6XYrKBbAcQlwPG1AFuZWULGhNBo80wkruGfqOSoGmBUQvNAILzSY8czmrDDwBIJqGVLJZBd7yyPJC7nGwzZnkTyzbUFZkOY6P7qwB9vhpZLiOm2Jw_9aiuZc0vjNbZi40SbiBPYaDGQXlrSpqeyN3IV0xJLVEMUuu15Qfsvuu9yOzgOUw-bUYRmmz9Hgqj5sCJl_M0tFrYhWZdPi2XE5TsxkWaNz9JkvzzdfOtWNP77RsVOgS9xpI-8kY73YKPCuyXWbC7iUiZkRMj8ootOQT2QAOjDFVa1tr2fvu1ovv0OAP5oA2QWf7Fn6I7ifo1y3fHfY_jlv8guasf3PHx5YgjUQdkia8Cr8vOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inkKNOewz9mNskySd_HfXGdb5azhnVP_Qf7MRPjweClilk5MOGJLPIbQ7efr8l7bE4HOn5b7LGDyvayIovy2QeQw15abulTyl7qOtMzD7lDvBgeEhk7_yp6rJtFIPKGAxRGvvYlFshzcq6UM1y4CqT1ux9-QFXxXX6a3dN0whaaks3QVbRPZa-Eql9LCGmJalGW650gPltPzQUjkIN4kgRO6Xxt9N-veyjmLa8pK_vvNfrFTqbLm2QofcLBhkdiCPsPto3BqC5oJICeiYIU30XXcMwa9FbLr5ibEi8Ny2rd9xSeSmsC_CRqt5-Dn6754k5JgQKeGVV1cZfKZwnFh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqQ7I2BphoZ1c0gTfmpC08dPYlpU8PhhxvMytbc5-qWAI0wWmp1qUVdiJXry40jcjdARtQk9cWXLaf3KWL6IrdcqAHy0EyGG553cbAjmL-HqcbTmBWg_i6hLsbd1PLHBkw64xT9lbBXJSwj1zo2dXW1EsQsyyucAywOA7rblDSnvxpFMCTZLGPSHku8BC7CUcx2wSbG2yBdGY9L_BSAGuqwSqwSI8o4twSUbNZEHoMb6KMki219puUeYm6rvREbmUIsbzJPfcKr2xGLcwTqfG0tvN7BzbyRATriCQJZXsCPHMjSvxkmCmBddUGNmz4D2ATSoyRCPz78qy8l9eKIwPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkYpH26H4KzEp1IcrIm5nTXeKgzwt5jhuYxPtTrJNIDD0QYtzyqvg9gUVGnRQku4gKDaObItzNUlLsY9diAD9HCQfi7gIMrc1wugiFbbTn280SLQmiz5-5kErEkL7iHS2pW3V2uH9Gcwf8Rceg0Aj94ecTv8To8njacBpxgz30ucPe4KSKJe7NGPRMjWLihHOAMWbNvrofd2NK5r5kBRRP7EgMM5MI0AfdVmXJ01h9d8GO8zQRI57OOu35ce7_EyCOgSTTmUMndE3qeedI24UcIAWTCFQAE0huTkENL72dHOe1wl3iLrYAojc3McM6lFYyURiupqPNhxAGqHrL0KeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_UfghcAdjOfE7jggt_WUa28nYkCVard2Ea-DxfFIUplGW5a0ZUjJRy4DKpRI367Rwo-kStHLP0kmFnfcMSinbJnNBKMOeLQoKqa7r0bNWO5nbE3Hf5Ir6-gk5vKIEIUowsfzPBWItYjE6wtlJNFacndOS1AUAS1_rBZBBPYQNU-jcd909I7W95YlRBx6CaOwjzvtVRAi1HACMUsCvo3zAKceCOCmCBsStotDvtktqtf_4pQU6GtcDJkM_YnsmB8-rw514tHljtc0g7RsFsPJckk1dr_9EK7LFVx-mxn_ixGU10oRs78WceqhhYv-57ERG7Vkmy-bGkB4aazei1-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvA5RrdxT1ty3jj4ySm6rfxWwuzN5b55b51ceA2k8JrcXDQJu_xzp34mfojHXBjUrO0-O9ObG0f4QlJBN0kPJiDYYJGAUJgzMqtMJ_ME2BcR-Z9KTgHUeUy-KfW21RB9tPOOrocGAmS6XjvkOkIIsj2NpH7wGTjax-ZaL24_KbVppuXHtngvKyAaiXxAyKsOzndYblha2oPNR57FUuf99EX9F9E85F260KFftyuq80fvDTYqNhT7PIaMnirAKlndOYiNBzLNnFFPBrdYcJxeavMSOXrVXOGu_5t2XSwbGGcMAUq1JtfF5hHxE3D6KpW5KERnDllSuiITEoWGGqryHQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Ubw4JrXYVR9GQZ6EcEoiJsIcJjXxeG2d0etVIj1ZBhcnbxD4-5IUNRZcpW1tlw_qq7pCxxuImNFnFewfdBdIwnyFh_q9trIDSRqtB7VytzXqXvx3_Zm_NXj52pl9wYcYf6tdfTSmqU0aHvLj4zgs63XLYmRMUw4i96sz0ljD9A4w48IIBTe_a0gxk3t_O0mlpXe2UL1xX34uRUcSWs8hUuvVqHNL7b1b4OE0vwg6wmOVL2-lPk6lMnFjXCOT9v2IeVmPcul0ahcnJc0rpG3baoFn4txeV39IUZkghEvvdJ4ytnF0PSIcZXMiuk33VpAHW5eEttzSGUu7oeTBBIaCzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Ubw4JrXYVR9GQZ6EcEoiJsIcJjXxeG2d0etVIj1ZBhcnbxD4-5IUNRZcpW1tlw_qq7pCxxuImNFnFewfdBdIwnyFh_q9trIDSRqtB7VytzXqXvx3_Zm_NXj52pl9wYcYf6tdfTSmqU0aHvLj4zgs63XLYmRMUw4i96sz0ljD9A4w48IIBTe_a0gxk3t_O0mlpXe2UL1xX34uRUcSWs8hUuvVqHNL7b1b4OE0vwg6wmOVL2-lPk6lMnFjXCOT9v2IeVmPcul0ahcnJc0rpG3baoFn4txeV39IUZkghEvvdJ4ytnF0PSIcZXMiuk33VpAHW5eEttzSGUu7oeTBBIaCzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOZv3WzIlIdv3ViPTQB74CrMafahDZg4q54fUFOrF43sKZzxM054iNX2dAFO-JxE2qFyeAhkwSfWesfwY1uDFyiB77uUzcUEfBa6kQCE4Iz7H-uXGL8htnNS3AfogDpzUj4APAlRPZQz0b3ZJOK9u47mqV78ryFGbJgmfljb3Z_Z0c0GN-EDr3fCGZUCMMjSCXhddBAsXvZSIP74CCO6D5-v84mMEG9oDzyHE7hgC6086r8pdIFLUSntDDYT6Dw6yMv26gA5x4Fz9aSeZMjDRbrfzaMgsNGCmVMHV43ahRnzoXPgxKaggTTEf-3pNgdHAKUrabukKIoVzDar3-vUWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqPYhP3EMX9tN3zU9Vh59sYR6RwP8tjPvdQLSLFOvIR9JEZQqv7EOLZz2milK15SNwyqL8jXXd61Po3NWL90koQ94U5hodz-9HdItOKRupgNMSEyBMHOAH_IdqpOW9PnLq4wqfJY_iYQLEQK4VlQGpURI4nVocxWKpUMGjFslhWlxGwHyOoGWN6-I6Va_T5lJQPBQdAqemOqMo0xUOANvP1gIrzhLrSTsLgRqFURUPzK4FzM68EVuCmCkSsHRkX87Ok2p5eFxqMfsL4uSiQGqIPpW2gOqD9J91ajB8yzZYoHvHFuWR8DFEkiu-lOcTDveVeGt1i95BH0XmrTv8vYfg.jpg" alt="photo" loading="lazy"/></div>
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
