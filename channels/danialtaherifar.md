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
<img src="https://cdn4.telesco.pe/file/uOUmQANU5AMjKt2LtcPmDtLMcBor7j-dWnAs_MewPY8Bk9GrvTo4r40FrGBxjfNM4kUUFlta9upflQdSena0yUmXthR63dQBTIOQ8ZqQzv_n0xoQIn_7BcFzRFfzgZ1mnfDQCvmJJlHPbKFN3sFul3vWwgjJ6trOaArfaPz8kmeH-Kpsq1IKlMG6JK_R-Zm2-kJNczrPEGPmgt_f2wX2Itg5LrcIwuiwCpCMuB5TXiN18SbEVSz99h-ZCCiUbWgBqTAb8PHZ0juYbdfm9xdljCuNYtXvA7-1aQBIjzZ5kCrlRcnSVtwdacVeyuaBV0sASD6sKL4Be8DBydUiey0qKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 11:10:51</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aprgGYzROiYm6hpNHsTlTsGk0XOyat8kuS_mmfwwgrmDiLRCKkMkjzX0xT-th6iJKHNsrHbR5wn-3p3KE6wFC6GQhBO_gljOJr1lLB3vL5MP453bLJ-L-T56tz3krQnip3oaYcZk2YTnx-p5NsCGttewXq-mkJ08061pRFMPBsWnDb7XymV-eKdV0Q5v8wv9hCCIW2HfpTkCeSW0WGVTMIaN23apULqvrkkNpX9GEelUB-EPorzsNqAqKh402XNfs2s50lh1L32jblmpmW2dy0_oC_F-moT6Vw1H2pwunMs_GADWTc00jEgAJ5uAK4YvlaMtXI7t6l3BTcN_bDHXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 177 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 423 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 569 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 614 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOmg87Rz-AGGgDURcD-OkUmKlxdeokeeVx8wSzk9aMpCXKgTrrfH69bxg-spcrGBFb3F40CCyDvBo7t0ZsoT-lb3B35Dr_p8rezfS9LtNVbua1iUrGnSxCirw_rGyK40Melt2-hZWm6q7q346afDHT6_MMa5bCITAiHvttmqbnXWIfaTrWWuC88Kl6hoh48YzOOf3L60G8cMy1mivqk1MpwuMkKoyVSK-wJxoNwGHmFet0Y1xNRPaWnZqee_5Ji9dqA5eGgdLRUa0cl2KWSDsE6zDQsyTDoQ8qKck0pYt9PNp8o13ziBIbS9kwAhHrZeBLfZdzO0xfSwzj7OCLpOpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 589 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU_qQqRr3La4PuITdlGmWB-Ndwq-DP1xpEUZiDtD5WQ3Rcv2zdamYzBf4-9c-g6GinaJtobc1ntb8eIZDGCJpYIz5g4OFnzDdmmvuDu1IstSBqimh0tapR6_5qiOJo0PAY30ZmrfwUiNyCJ9w5xusiKxnVCRMsRtvZBWqggRXo3niCkPRikgE6NVimkaMmo-2BHjELG6OvnAZ-LY7Y2kJ5JMXQWnes6I2ab0Fiw2M9FjcjlzhDS9A_58ISq4LtRjCCE7G0B8Za2Zys1rK8ckp059LMFub2nsfidN-SL9qO4WOyZQpgrD_Wr2zPvHOznycXw9R7cVqpK6o-i6zE3IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZBCLDUzrzcWfltwvfhtpZlO_Vjv3psIZQCwTxTDyTX37ckJz6kIX0A7BXo_pb9L0egh6LbIiBpCi228y7zw7wS64Kgs1sPs-eFaVUeR-DIn_hCioxTYRCD-a02YNWPBWOMFXx0xG3hmLF-EJkMRmsBVW_gVIMXbbN1Y_ffVCtVSatNKTAm4c7-330MBup8ca3LjPZ-MnYYnuNHEGCH0A--cXigQ9gsvb8mX7N3FwIPryrLmGy49ousLPqdF0Cpfp7TPnbms-cnI6eFOihgfD6QZl3OnsKUhfdLr8pEqqUNFX9Aw4esxJOhltLk8CpR1ZqHkzbbr9puHaf067W19vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_1K7K9GkkmSLyFEvOPjTF9QU6usL21nne1irxB0jKuU5Vv0bUWJTPJyUb44iIrqN6JZxuIr-bPwE9lfd4ZhhMnvT6P3cCiGE7uWHi-OFi3aeCWRmvD4nf_50PYLk2aHQPIO9DwwedJAmLoqLg0RZqnBuJ8bneJmUxcUUdZpT5uv-jdQ938uaXCSSbVRQdyIxuFJWH2CC9Oq3POAeIW3DmPR9nJJBXxL45wiMB9B0R8aQR0d5vMTykiw_9Ios4-PyF9YH3yjeI6OIu44LSt0FnsKz2tfOpeWqNug8phH1EPXVxkyRI7OD-LiLNwLwT5n74cGtpGEiWWKUdJnaJikyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_1ipfTJ4-ZfYHTbYU1akSKadj0cXdNxQkhqS0FtMNDlI1GhqOrcanEyCx36K9lXRtYHvxUajhmp9ufod8PVWVY9INW0uCqwISzF-Wg31V5gontYYti26Zw8brZous2LfdtV1CDFNrR4pd2l4YoPvBxfZqxV4B3LHxmtpR9fQqBk9DKCjENbMM1vlpC-j9GFHEcknbtG0_PNa3_gtBwlwK1Wmh-dSR5ae_aw3Qj94YxBFQfD9FyETfjTXnH9HhZ0OT1wstXbtROocsjET0y454KquvZVPhp18i34m334tJ3Nm7v3b_Fcq2nK_a7lQQT8JCT5UWP3emhnrpeWzjGyAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7dGdN_8Ii2oeyhlOeEEUtE2Dkfzbq8QYzHZFeEP3mf0ApTpcC2lZfOPVGs0mfxy8vMDHKySOV69PVr4nQkkVY5I2EAfqhnTikEaF_i8gAlSVL6Qguyeu6Al45qr-VxesQSbV5B_UyoEZwKPp4SnAXq5b5i9YJ6Ob6rOB2-Voav95w3sN8HbJjAGwTR9YBn-11gs5h5yP0YQFvjZYA8qmfZtAW0wwc7QR1Ujm01J_YUIx8BHb6JRrirvxaVtg-T9jGRUjlKnDazM3suHdTxrwD76BtLwIOBv119MPPCghviXkjsIqiHabaW-WkDJn8JiqGdIdnv-XCuO4XiOIj2AiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb6E0s-4pMUSp86L2dEOGSTtDQqMVWb0KzF8QYSqdOiJso3Igbv9wyDoA5LWkRgNPtbU92C0ZNnJot7WveB65hEfzt9lCTRq1LVtJkMpnEvKqcZsikeA0dJLN3n-gvR6ikeL-F3zRJvUSe07NCbX2PeAhic0ybUlojZi3eRSbUAV9qIL1sKXduwfDuQlp_3G3Ro_kEJ9lhKTCV7JpEr4xVK2qXoPEkCBBfJjmNHwSlJbgnZU9GdvFDVbB1XI_tQZNt6vBNPcU1-IU6A76X4FjgnGwSXq7neHxdMfSgxPZqGiaZQXljHJrkImvmkZt_kwTLSkhtDMynJYa9LbXqdEkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKfSijpNGxJFlYMVj3HJemGXcGdumLiOiXWFLSIc-p3gKXQ1o2HOfcOuosNskgpbym_J4kRsaK44N4t3v_KaalWXGRFKUW1wtykZU4RHDYl-AWjsKeN_EOl8rwnM9J5rSELDItJUD5ANJG7_DydbikrPNkb__XluBTrVl_gkI07PUXQJof9Ze8sgyvhzCX7VLc8SYf_OxbyqbzGozGxJcUpaJJnWiEWLKixZQ9MiiqU__709mmMWRALYqcTSZKrJe6fNf0zjgTxYhvFMyP1yb-jdASs231KEK8FyClfQMwJIPHUFvjDpIuXhOuZY-Rna3ceAkMb2RIy2Iku0SU2yhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaFyO_oOxMwfowCurznLB67U8Ok3L5Vz_v9SwHmkX-0ZBXnZr7fPvgdTQNZtJFGTXrnZSzszetsSc79dJCZYWHRABMDEPIf7erEaoZ6nfj8d3BSFjxPJIkfhCOIVmX50Sji9kTUiA0vtH341WCorY2fx9ovklKzIpOqA96wY5O3mzIyXBlIA0TfqXp4dd8tjmQdJ0jZKq9ZK6--gpf5sEquV9Yku8j9bzzAkJLbmCUVH50vHhNaGVQzQRolhX55A9yVgSJHvk5QOthJVXxIemxISKD0e57bsIYzJchJNF9x79D1sl-T8pVqmiEFuSecm5L-PSHLeDbqLkm3ZVuOziA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPpLfuD1wHLm4_HDr0P39tXRvd43Mk7w15yGkGe7OKNK3-jVnxL_ODtOQNb-TamFYG_IejILRlV0_oMkzaz-beFTWyARMif0AKIcnPItI9nfxLxwuB_1RZAvdkpbuQZXYC-2mnD3-xr20QbUUmNgRMesLUU-WysMlMpWFxf9a7eLk_UsAbngkspZv0g-6zNHT6vntnPvBeBpcQ_aj59PFJ6RD_xd-0BqjyEfbqNajbBu48NRTOSeN2NBGOd-QYiAOQ5Jnf4Vg-2129De2EW543_ueUbvihY-71yuOxdfPOB-O-btytYZ3QMNtg902N2GBwDwL-K61ylkNTPowXbxgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpUi2y0oM5F8lf4PM0LEnNTNHlg0qfo2rodGLfe7sozClwM5ZkAVujwhvaLx4OHskcRrdK6emOu4VeofnJcutqcIMwvNxehGwg90geenq3zCe0RLZtjHwlB_6rGrAinIGFH7gxlLz_8T76_WTkMv2QsBafmMZjHvBWFTiGkGEebg6MHB766ki37F-Xk1gj3hsvyOZqJHzqCMxVNGfITKxAkw8kfvnnQDAlPVDkQOnRvNzAnWrKdM0J4pNJ-5omth80sv45QHxyY3nH-g9slXGW1jnfIESstQWBsC8cO0zhe-9fwBZfhNToHN-7DW-gVX4YRsZNBuMW8VGy_eL9LCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAkyHg9XzSuQWjXKF8NvvWIGu2GG0pT5WqbMTM46j1xSc858rf9W3DuiisTryK_LpCksZn2Kvrz4-VWKdIwm5Hf7Z5I8KSFnjDKsCrXeXks7rY94ah9Sqr4HTM9T7Dz3h7WjsER5za7r8da1bKLN4dQYnJhGPqDv_vDAgH1ZkKQILevmaf9-mD9TFQJdgccQxZXfnxdoRISPgeRxtR4WARh5NRWzir5CfsT6BlzMQX0pmQ9IVH_sLjn2gPjIodR4PGOrxXBWA7_UQeM4ATe5H6UM01gP4ckrll_GI4AHe1ARadLkgAtQWMNkIZnMifPtX85MarJ2sRSVqRiLhn2ocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0YMNYez8ClPg8bS5rjeGBrmW5GmvfvYHuGssY3VSsK-OpdKR797gH4G8rFDJOAk4UsKTRwf6VykARQ865mSg1tHzX0wBGp_Xg0cOTHPdvU1x5GeGHupQANNmXGg7sOpjZ0H7ctJjLWKJuvfOeT6Yo0KIzWCZ2Ds6wgMCHPMvVl5wd13nF9eX0SFCcC_fze196eiRPCzxuqWWn2aq3LjmDVHz-I1LxqJWE4XGcy0rCtojB6Dh4IPodHPqsvXwYVQ6W3TByXPKYGeZ18xynxo_YsZ9L-W8ytFYJY3BFtbGBYYSEJGux0fZm64XuHkUfPt50Mmqy_7QfeYAFjIv7FSGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTpowM1BKELEsozv2TzGOqqPPS76BsD-y-xlHlxOGJalPKb7ed7YMFw_hjpqftDjTYFm7Q83u5uGjWxq8n5Uaw-MX_NR-XX67M63xfjhtPEP-Noa3flwguX2gEJp2FPiA7b1wBdHu66zIi0ikNFpQ_i34Qz1CizKY9GDXmYWCsooHuavLCegvCd-vJcJ1w2VubprgCFiUUUjcfYkSXXVkW7YatzC1nCTWAYee7BwHTXaaN8uhhgSA8jIX6rT-WNn9J0E6Zo96Cg0k7vkIUhXHXwMa9tFQG7lsXMRfPXzlN177Tamu_Ve74opmiX52L6slgy1TdcxUytUw70ZHJsEaQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=uM6vkU9vp6K92p3kMHZAhH6IA5_EyeyK9uicFoEAmCeUBqH9zQlAjrPPuHssPKnTzlTS5mXNGNqlVVT2m6WGnyiKSg8YaMZUbOaXdHxARDAVOinENbsyPrFmccu3VIusZRp9IwvRN8FJfR0Z2Ez-N5rGHWu6sTuTKNi_2TEhEe0O1RXOioF5GL2PhKNsCyh1te5e2-aQIHzLoApaghy_gziDzpG_5QQAN-nTEZQBmWl5Q6qzMDjRusCSxkMD7S139XVQ0ACdKsLKwjmb07GF7dZFE-rI44efxk3TCI0uCs42WMqz5x1EZ3gGInk_6BkshKQesw9g2KCgUp-xvATzzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=uM6vkU9vp6K92p3kMHZAhH6IA5_EyeyK9uicFoEAmCeUBqH9zQlAjrPPuHssPKnTzlTS5mXNGNqlVVT2m6WGnyiKSg8YaMZUbOaXdHxARDAVOinENbsyPrFmccu3VIusZRp9IwvRN8FJfR0Z2Ez-N5rGHWu6sTuTKNi_2TEhEe0O1RXOioF5GL2PhKNsCyh1te5e2-aQIHzLoApaghy_gziDzpG_5QQAN-nTEZQBmWl5Q6qzMDjRusCSxkMD7S139XVQ0ACdKsLKwjmb07GF7dZFE-rI44efxk3TCI0uCs42WMqz5x1EZ3gGInk_6BkshKQesw9g2KCgUp-xvATzzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCrbuhhgAsE-uKfg-1ZKmtZJ7oHv93s4ZVPYuzFDhyzbCRkupPbj0b3kPdVNRIbzrAc6NC7L_TN6m0TBF8CrUDpTB_q2lZ_jFqfDztq7EUYUCRgypSLPdRu_k2OTW4mJHZ8VqTaASCCpyJ-yzutVCmRvAaBz6tCvzqZCGL7GMgfjMx64VCpzd2QiLJNsKF7HCu2uRgUpxHPJak5iFjhKo4HCLarqQPcuaDGqFdjcYMHQ9laieiJqhHPb3rFEixwYHr4VzsDJwJHHcEiWlfnnezQKOIkUeyLrZGT9URKXJ3PG-UehKd8eG7UIXjnOKW1SFsexltSJhrayHpf4_VkJUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M67wdQVwdFurCvYGzAQlbNca9UMln2fMHhgzoWMWW-azyOwb3F2Qdidx1GRgzUEq2Ik2PJA16C_Ase2qpkP9TGKTuiBNYCbSOI1zi6jZZoKbSmSZ75-iO84rex81tEllt-cJcuXvWEh2pTZT78gMrBmhFCOzd0OgkUO77Ei401yYFZosnmc5WNAZGTccXxUwG2mOi7i0B8WgQBsdoQAiN4gehZgxz7tC1WmbTca2-l_lEQl1vNMOvn0luavY7tnEmVgO_0zx-H63X6X1roX29JvsDTV4f9e-JnYqHFimge0Y1iHZWWM4vaBMz2Iv3nlrcgo08wiXoYkI8GzMrGT0NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9UrKF_zQwHLTFOTljpl3RsjPQz9ubQ21UcJwUTg22lLYTsif09h7BZNN_wgSecPORHupnjnu-TxDI6S8jnNjrrSKAL-tKHLj5IuZxIc9D6XjWkZF-VUQP0afsv3tTeC4uXN9TVO7ntBOmHFXYsENfJ1uYgt63kuxNhYCvHsENlbdrnL8fj2OiY9PVyVtrIsoAHO170mrj-zDjXDJW0vfwMPjeURs7_nBEYROsmtSAPF7mcA_o_qw8CN9SUe-fAkbmTiZlrwNMG4Vciqf8lAuVbIvsvtCMuT7c3FCfFFYRjrEzTxZux9GwX6URwR-1qzYnpKZyTfDjNMzwMx9R58Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYx13dFZ7mB7Oi8ZEhsOsUiH11XzDUc61uag9ucRYILV64FxfBZ2ZxVg4Hhct0aZztxzNwcWFE3p_IX2cnTPcbefLDVCxDtgHwJMX2EB-sa8I3X5bjUdepLwGMQldG2G6YdTdaEonruiGmrqA32ecleUOaWvQzaabb-HdpxFSJT71kQb4ALaCsuAJi7wOe_4-7l6lOdrAqWVxw6HIST3YaHx3d136q5F7qB7FYqyoNhqGqohXY2EAiFuGfcZYNl9kgKw_tIuvUvHiCdfCFBGJ1z8ehBbUUcQNsBB7rZpUaXAuEmokrhmVLwE7-nKLqaBeWq4CDn4LRRulM-ar_1XNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euxTqkKWcSpr0tNQ5B1p5FxVB0jB_hZBstIHPcyUK5iBEiwQnpLvLFSS7h86AiThK3YyAEp2POghUsV0rttJCT7mSQfY2Pe11g7TQ86ITLH6kcXAPWaVdp2MGRlX-qx73oAaeiMyxP341EEUkTDijwAcg0Qd16-g6zOkWR5aRtfGHYyhoTXEByAes_23m5uiwk8R_D1ltAdc2aoFFP5aLxCVuqPtidNdoeukp7ygKHUaCEWuFFwxUmAb0WqaNDSnP9Byyxb0j3KKN7W3qiWYgTNsxynwVyn_L95Eg22w_LhsW-xpPLE3U50AwTyBqT-LRzWP3Wf2Bn7gMHDFAFmPig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXpH-44vYu-CL1ezrBFQeHd6SbzO5xXO8GEQz-OPLfSZrPUtRoaJx4hYX0y1f7Wr8h7kaeQpJmbuVaZdlCt7f95ZrIdQmyoWFzXVcnARexwKuHdEeybm2KNkzfPbHd_0Q45CxPsjwmYW0pVx7RTPw7a0HgniVmw7nvx6EPO7SCNazZ-Em7InBs5c407LQp8xRlWVluItyMfyc9UAPCXGoZ5992g9d5pm6gXw57gYmAlddmsF8ueTZe-dMzMOte9FFZPOWOqoHgYQyraV1mJJI0uSEdCs6AJJZrd_NfL8c78-MPM3xAD8HYH5DqbE2h--dlLSq6xHWcCyVortXNugBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-bopTPukIT5EQnz6SuPKRadoqdGwy9iOGW_w3oEGwgMql3c84p2v-Is-mZvF-nDOPOPRA8nEwox716MUHGacN3d4mFkN29kMSUXudZ5QsBzxkWPwdIPF3BhIGsTwbcMFY5-8bojRBh6UgDeT196NlskN53laEMTFPJn8j04kau_G-PKv6xME3-HjNfds9KdbBs-P6-4rQ_ECd-CxzoEmdAT7yZDBNL5f1Wy4gIs_xaB0hu760Md5y5vAWaHNmz0-8C0aNN2PNBzn8rKUTVl_U8bnn5QC4-cvWGrawr8M9clpFZOrorLZepEYdtzKlsh1ZDf7ott4-C39CFR8D_C6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmzcNHbIxyW95ZWNJwNQ1sGKQEl_XqlzRTsctvaETp_SaYu4_GucyIBl9H1sLm6aQz7FEoO_vdCc1MaqRMkC2vBceMywSoJnUEurOsEcNGkLMJ9NcKvNQNLrsO69KQdKiwa0f3hgusO-j35KdKLLIEvoio0aYuxJkByixQ357znV2ftbVbngGJgGkBOPatWjoPdSLQOp3e_2RrzpeGFx0qrFLWXhnq3b3GlyvVeIPwjkDfbXLQjuHycTkKLS-Z8ke3FT92Piu_xfyNQU4YmT1ke3pCDmWOWIlCS2gXUncXAN6zk3dA9wnpM-SSyPTjTf38vQO08evzw7glrOoGU9ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_dVruVKvsXyAU8XxDqct43fQ0hMm6dwpGricNOH2GKQddaXnmtM2gYt2UoK3Puh_rfigohiMNIdWCKfHvcmZF_vBg0MxMIK88RxAfRAKIsqdDnFyJdOaUbfQyDajDwB7ytpDB1_QcrOjxeZl334p5Ay5ZgVdXwxqwTlOqcvkCQJ-SELnPnXShElWaO8e9LrFXpyVvj87Vdn3eSgKWIR0a1pF8GvUDtH1GGGtEsD2OxglLudUBViRCAB_diSpbADGA0z4LWoqGFB1fRfbSUJoRLsAICS8bJW6Pk6NfPkCKq2U5DnBW-T_OVoJ5jVDMas-F98jtrKtEH_8EI-zeQAEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jub_bHqJ2EKPnax3GbXeg2btXJ3UXry1PuESl9S5A1FfKQzvGbyyjx2NYT06V18pSOBs4OzaVcJvgFgsiBMfkkbirimsN_t9UK3m5psEvMqpY37EV8lXjkz2mqx2AYlh_8GZ-VQBy0JU4ExBYVeiEq_Q-PYb2rEd5lcKLj3OkPD65iNw_SptIcMIXLZBi1KbwfCG49haHvjRzIfus_Uyqmtprn-IH0cws0esQI74P6cHggy1f36eIu5VrC2dkPV2v4sHgOvOyWO4pZVb3SWrEYpR0LeEutIJtzSXHvAa5cWpGbFAkRHoPJLT6IOsu1FYB4T8jIE6bmrS4619cCgqnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRgKTNIJPvRyxgV-_zjLFP48Crbz8kYYoeRmNnKcdgWk2vPPdxJkftTmt06GJXEnmcYNZ7HwmQDpZ1pHmCGedIOez0CGUSvl25kaHLYDEiYMNgZZ0kRlv4zmoFaIDlEnoFLuEz56Rc_FvFV0MeJAsM-PoJ6jOcGLFTWMJdidkRwI9Qj3R40BnhIqG-iXV3gr8h-CYG9RJHQ3pn_nLx99MKbCRUBCWBmVqaCb8aFG1FAQEcw9_y0EmCY1upY1XB1LFR-nxS4tgR8UqlWEZ8MBH8wxClrTB_lBRPyJ8x2NLA1OdVQPn2M27R7edxgYgvZ556ZTY2HhXMqOvfKWMw39-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbyUCbBxQNqpJoct3VCt3mmjXEp12m5_qSbwdI4ctPufT-p-LGB-zMb3BHuCnB_FvSzQT1z2oPCwlbQ268nE1s-Vbjz0JqghGT4kCX_8hnybR--sU22PxuQ1bOfWbodYjHllRe-Qo_gAUMSegfxXeVxvDvJLWbEJ63GpJK-MXbqTTHQM5UoOpVkeXsULH6QdH1tobhouMTNTf_zwaaPZnJqsj7uN5Fa7d1LkTHxwzkxuvVkd6bbDBuO2_jKaJuIYLkE-IeT59N-VNX4zAfQT4oDedwNDZ1G9xCu6GIkncwE399gm8RbPbS_suI-Yd4e1EaP7qO0YOb-0NtTxC309TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ML0Klpz7LxcZiBFQPIwrgaBlzJ6yruUrQ1QIMITztFcc1oUHlaJqjvZkDVPs40DV6IINiRBY_JLDe5PEFVyFcOMlhYKL-MnT_qW7_PKKKjIMF945k3VEQCDqjPKU9FxESYbRTzvoPn3s0xNUoZmzyw9BruhcBLu6Yy3Yaaa1UfBximP-KmBXlY9b8UWdIJ4HBgCxgZKTf5SEfJS0FuJDC-Tzdk-j2k1wUVJwhv105LN1unNdtJsdt4KNK9Jvl7oKVUkZKTPYvnZugP-xXAhBApxHTh57NKyN2DY8C44t-l_QxlXdqA9H63ZYggZRf7yl_GQhyB-Ioe3emFqNTBz9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvALC-zQrhMDQlF_D6fAAKC3oZXHWmVa9xAHHMmcEHkVuBLqyccvH7w6_vCEN_2rrNqwBggXNFm6bCoAlu1beG-fU3vyhMsn2OekfnOJsA2tPaDyHEGbIbSH3aZRZHpAyIT5jlPVMIt3N6QaIf6-FpnFhLhCUPiDAbJYOuMVGGWcU1TiuO9_oO7Wuvo_jtnhYD_itOt1A92KgD6brTKyC5ZyFD-5kJUsp5Vprf6FZEKHsfeAnS-uvd88o5u8sPMirZB2SypSnrFPmbmpVzIxSRjrtU64ZY3E1yH30-8xaujltYduugp7ZBKvmqRihudViZ6XRlirBMJPeXe-j_0XMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHbIrItQdxBHTlmbj1QANWDCtGJA08DHdXfOVx7WgsjqfWnz8_0-DEcPWggkQwY7HxoSLqigb8XeEAkxfpgRzMLmQ8DUQY3RtboUpo-sm_AJVPgHzQDneBCHWjOr0QFe4zTkYKrRBDkTOh_RjuMi_ikBVwYHPV7nnZ32YeHnhZOFI9LeI4QolbqiuXnuZFarvuN_nJABX6E_7fFwUV1065k06yLMjd86dtQ7J3dX2gwrUOKZdiwMGSfHUPmb08V3cYqeZ5bJKxuyrlYympgbRA3umsmC-I6o_0u32JXsPCXUFjRolcL_Cndv_c9T4IWNyHT8wmjk1Hwss2RuCTwaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H293kr76u5V5h_0CIKLTuNyDe-6f1XZy5qN14SWajQYUnGDgM7zqSuA-R30Eod1tm-rG9AM2956hqIA5kGrWD5rUFAQgc8N-ZL8hvp3Xn6jq7nSFqAwlq6wsAJF4PBruQJlxHpi4HaQkI8KUjh1Qebe4IGy13flBMH9HpcQCauukpRe-w4f_v2DQYOIT0j7AFjo0MtpVGyP58B9_rLyPVDsMPj1S6CR_s2_1PJncOpllWfb8va-pT2ZP12prd6MDDqAkEaGn_YSJsLnTPBbh9uVpeDLjNd2t7S6zHSbSQvxN40A8_9Jo93HfKQbqcQtTDhtT33vAmz2Tv6zy0O--uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLncEgy8hAPm8qTJVMlbYuW-GfGkVqnnO_V4sbjIxeUrVxmLma_AeY5LTs4OcTQ1TIe5Bf7T_U_ge7cbDVrElYfPjT_gW1lH6d3KAyWjOznRwtRXKoqWd73rBRCXib67PvNom8xwkZ7ZqRfmyfdvNTqZTr7CLhRRRyp0zQJrTA0smvDwVfIXfkABeFAilWcL05XqXQ-nLy0H3Nf3V8CorkjIAwnS0t1u4ampMe1J_XYDjctWSePc5_w4hIfLrRvAm9dJYZwOXpfV6HIpgF0FINeNglmOr0VNh2KFhKGFy1IuudTxMZKLT1A2hDxIuTZm4WggqakBQiWEd-Rrd2mGUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky_DxbLpyVhgaiRxJ95B7NRD8-uA9sYuL7asmpf-4FeyTkfU6nkVG2KqMPzo4BWDOSlPTlLFAvlHnkUi7vlcoheKPXPEOsnVFYKVGsFb5pp6Qp1ydQCmtMQBp0D_LjUznWaUQ0fqoYfDS5qng3Dk9p00vryxDkOAc_1IEywwNonGifJkyoVf8r6jtAXLAOBawysOjCmguth0FGFVowR_30cBscwG3fhXnPUEyRMevmyIIiDC5arbvjS0JamArc6uXwPgQ6fzf2r-pBTSjNi1N7GvbT_xeCDY1mlFE6vumGp9EhzVOfBtok-nA4Bm07JJaypc-0vngBP7KzhK6A1X0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS__9dpmvLWWC_BzMaeifQyIczBVlo_NhcrTyiznjdwc__JXZ9dIJ0__4jNe92AKHCsrPZFQUrgts0jttkslVdiFI4K0UiYuJjNrTKz33I_AI735HQmyCWwsFiTdHgF8f7NPunyed7X8q3t1Teel1je9WUMbqtOdQ7XFEYLmZECGT6H8lFBawVS4hkzQD7g5jNXhrA37TJQ8jC7Wrvmr8GdC7Rj6YjGAw6B1urk4Tf1ZZMTLBjP9QMTxzfIkO5eAGcmus5tUSLlZCzaeOyOaL9AfqwL0ogD4YSL_0R7mICaEIiq6FO-BsARwFqhF7sWFedOlnYktRFw03HPyY88YpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig64f87BhVQVv5jDJhZWT5o68T-YWsRTwtaWiquQD5pN2FcO2ml6c1YRKFjEn-0tLWuzbtco1OZ9uFkq5WjQx0pTMTIkTMyVLo_FGJi2T3kpkE2lGe2CWglxMNUnqqq1EH8yi_5D7Kl_AC-cY6VmCpUJY2obOlc6FihyeT9KZ8RZKXS72YDd-bj-3_EHPYDgPyEirJhwO3n5q3gr6_EmCGmEHGPatpk_3fsi7kz3LUBvt0VZ4irLgDXBy0hWyt7Ggc4MKcjC49i5PuB2c_UZvYz2nKRjp5FEuZk6gBwZPBNTWqaJ2AWzjVzsv-zGdhN8sH8C4nMEdEQXr9xTMOG_1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNp0C7DAVjVXVIYeGXVzrFCXMNUFHlkJP5iDFBAQRmxU3xiCNoCFNqDMn_MaX-qMFnoU9b84h1GPHp_VFH2j5lS4ndWSR52Ex4zU0PylnUzKUU6z06tvMQc_8G-8Oyuog-LRykCCQtPcNP3L_EYK_KZUFyx0NmMqmMVVEMrf8vFDNhGMDwHuxqgqi5JZ_e1Sff3OTIwlVUC6XPi90WMusgn-P3T7Nrzz6uKnwGKn7iSNk61q0i1dAHJ7LZ74uMW0WAMDo5ZoRGeKNwwDaPCRYRxvtSw63jcq3aMBh9sBG83EUS29gr9pj2wou5eZrzgWe00D4f1P7JQloG7hkJMB_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpEW4BPoXyxsZnfFtjXrtJgShouVA1q812Ad9xQq6SC-dnsT8lzXPZs6LA6YvUCY3id0lZSfadLllLHuAQS-A3DZ8ZPpoPBFNddPftb4ux5prwtXjC2cFX7sme1YsbneR68F-Q760CMjFzUhnVVacRK9JzLqWlVzjS6w5ECBYsDbSX2BGyQBnIeLV-ftKrej6ps6OA8ruvBjJ2ytHFrrCMfvwvkAVuRQ3oCEiA0rHSxTbwsSij1g6QxY7cGNPsAp8xKZ6m_hj1dyie4bWa82Fp4rIpfEx8_px4BxQEcB0GrIj3em02mOdg3fKE4-mCcOKGDub11OmXFEzWhwzawWgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ956ukVW4VvFHS3sfs3GVsfUpj3DfEk7By6ZYF4BAl0joNJHy4hoA_hERfUIv9Auo9JOKhs9CEJnHy4ceHycYEbuutXRpBkkTpu8T0GIxTt3biBNQvMxliHnco1xFaSQkfUBAymyPJvPAbqAyvo57rA9lJ6ZlQL9rwbG-lir34DEcq9i0QBfaDYg8UEe-zYFBXDu_XmZor9E60ysuozsLSZPv1NSIza82gWdS5k5kiiTiAQrmIZTtZj4JentFGCpNV-SxBgdqpA71A-wl6oWNppDNwJnNIXNwZPz6gvOIKLIfHg6_z6pGAQr2T1o0lMA1RAD7MnDLQnFT0aiV19lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhNmh_2nmsDPcjZlhZtOnu_MFU_E12kVRmkO6TUAd8cfrA_MxMrPNkXYTWDYjs42h7ybM2LguXfs_do6T_yqWr-_Ktpa2IhY_8ZlmOPo5E7RYzLZFwevSoh3HOPIwhVcIMrlvV-s7P3iSHhEOEpq4aM7qZSkdceEbtnxFYbWB037MMJtzo6NRxppzJp9lsMZ1xIMFdsf1-RN91RvTpeCMUesK8zJ4q6Es4mheUiyr7CYltHX6b1mEUuzmTRyTC659d-UrBoOp9_zPb03LJnIOe7wwhl_1E0buVRX4vYNcf7a9UjyUYCFYsJlYUI_ftTd7WZHP0FvcayO2zd7iyc_Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGDpKJ5E18GSORu7DfOeya24yS3mBkcp7KH1r_GTyR2Ae3_arnetWwks5M23hjnT-TEmOzlw_iq0bYwwRwptMfUysX-luliV7KlwXAeFdYylk0VVtTeH5RxOt6zXXEYnJu1JCMZd8hgivAvGnd5aoNHv4jgP4LbItctEnS1utbKekaHInuhHYk9qPide76DacHQcXsLjQrIxJUj0_FkJAphZypXdwBqT_5GZv9QkoLt4s6y8IfFh65fAVmV80zVXi0VgXRPaHO-k-x55i5AkdMhiouXv60gFiWsV_iwfeD3Erqi_2lkGzYYPQNy_0z6PsAnh7-6InrQk29uNreBz6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtgIxEN46vB8tqIEoPcp3Y3tQd-GMuo0oQocejKPUCdNI-KkXBuHU7aGXYFPb-O-EJL1-bKbtuLZrEmdrx6vEg-mYxSOHe1HnZ9fPqkVGH0RDbydatZCCH75uKmX3O9wlZivPainj4S8J5MqWWZ-MVAyKy3BRvsxjx4nU9GKR60bfG2sgCm2OoGsBBWFxjlECyFojM1DFypBziXCDAotByNJkxG5unUyuMRGrdkgXWdL1s7Ytn5e0FZh-wMLRE9AoYlFa0S5eZ58hhPp8F5CH8yg7HNmWpjvKxzMsm9V86DXZ7IYItaPzs1M3bg2jYP2EPy-rBG5SEFcv0ZzDexN3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TahgJN1AGFfiJJHhPeqoJXoRUaTjIZywLRIJX5F1jkLRn6WWY3C1aJiNRU4yhVnb7z8bX7EgrK71p-4jqYODHl2_k06w1Wro7HX5H12cx1oplzsav-W1Nv0bEqzbb-_mWKFxiiBf-Kr_nyzwfNmgFucO32lpZo2IzB2OsfEkZRzWx7fiUapOIFTOq2RKJOPRLxWYowmbCYiaIXD1g1_OhkYlynzGB2atKlH85rjf0b8Nz2pxriwu9G7Jp4wTXOprRP73wUdaHSgMTb5RDQg7WRJS5dubut7YU6uJcLZJMUeIW_7o0XonJ8IY1b7Kbk-L-YBHV9sMxhgyZBZDr0kvTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLKzcSf6anNwKnMEURzEfQoh75e85c_TylYPbQieZUf6WYbeQo0Mw3Yh4PK09ZwBMjX_b3EjnQCAS5zJLdAilezELl9IPk5uj_A6TKtyu2BnJAa0pbdJru2ymZX1AijxMbjJUL_qTebCu1AKuCB1ghuJCNTk5qJswmuH8DB4V6JXxj_pzQtlAd9cBjUN5lzQq1vQ6nRRRPsy3arFZLt7b3mtob1D33FA_KWjwYSuf_LliZqBqCUAdVSlD8hPGbgJOSy-9a7dD-hHBigpjIOK7iip0m6p3aR1yA4wFQ1EcxQ2lG3Ew7VHgNNKUIrCBSWtLdtJgW6lU-ImQhLlBjL5Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7sDzAzp2601_LMuoyszrkQsTEFxP4MqSd2O2Xbt9W7YgnL6SRtU4Lr7N98RYggjLPYFeQMzpyAhIVd6YiylC8Aedky2MOG5ovFHYv9TPTCKegdnBxvkEtyYP4AKS-l6z134A-ypk2LxWsI9NLrYgno5aYU-RFBTXbQy3Rj-B5aF6_IoQJ_Jdac8xb-RWlKweYWNomzLJRmEfFMuUlJD2tfwEXd-CKGemowzxa_3sJjdWyUtC27kIbWRuVvjRtfAnAbCpY61Ri0QxIoFsKsAxbXX9jMoF-6NaHc47uVNOVJwMdbah36nu7jhNYTi1ldRT3RO55YqtY2qMuIz1yrwUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsRdng8p0_ZOGtqhbVLtKjEPeOd6__jYmNhF0YCiYrAF5xx4hqhaEnrcALrwSE48xugRrmIYLrDdYXe3ntgdEZ3g9XmHIdPwV8qUD-hxbLvg7ImvrwjiOYDdXbSv_aV6y4Mh43xxkyKgn3rOxfmotAQvdZxQDqg0IJfhRlZoxpjTxOBA0ZUvXqfYT-cMGNGsUeRdLZIe2QxFGP02BA2KGkIlT6XOfsa5PfJgvd6XhFPSHKJneeu0SUgUd_tSSRhap4ZgRk-rqXOUi0trzSlEchbtnZaD9WoSGahoWnoHS-DTnTwZ7aJz0pIFvE42zmlj6WqOQySI6swVSbkkm-lvlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNmubWm0eUCgMvpVHIYPJ15suFoV1i-lX6iVgNJl0-vQk7AQZMQHSaHX73enLrftoG95dHEyAI4S0VRa2q4iu-eADCH7DHVLvHxh35jHrFz5yaZOMC8UWFKdOAfGUUVe8ESX5lkTN0c7rNQoiozLxLcrbzAN5HP6LjhPtM03yxOmNRfKucJC2hCz-oLnL2wanG8gHWuJTwHCbZ6An6sZwiTm-igZb-toO-QXDFkT-bN3sWOwOs-5d_2PuJrogELNLNnno4aqCFaJRI-rj0wBFoACvYZ_Z1PAxRIc-fFIXUNttez7ea_uL4HYRddb56DYpJSpAnyx0nAoT1joDyuASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skZQxbMl1-irZW2K_jEJppoaJAOqZKiO5yOgxDfc4Tzo97A1BOy0EdSdbdLb2AdoPvImtdpGFBtulw91VC2OtvsdPCLb_h7TBh_yuuKxt_Agi_YQEC4cBim22KHwZESeldakulXnxas0sUPEcXxc8O_7iVzuC-3I8KPzinUg0hqKkbsvBz51vIWyNbV8Dq0S-2sI4AvQ-nNJgu67TiNTeoAyUgku6WzMoEbwXurAfjZlqUos4-2iKFPhSomxWgUEE2H_FuLcBYEbSQ6e35N3r21N1VtSCXKNVa3YVbKYewBDwt-fn02vCAeHJsBuN69ego0w1uiG3VsWBB7oXf_g0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfvKGGnlmJrGRDk9k283lkWkk8vW94hoFY88VqrfP0kffRp4EpdquKOoLG2d6KIytbAaaLb-J8-EenTfpwNFMjZfFd7ZNS4Di42itYUWoQSuG7muxvmJT0xTLj1XwRyupM3jLdtSJPXTzgCVrp_8sCyI156jD5IV67FcHIq1zirYNBU3HH7ji40kU0mOPwA5qLUqFc2fYiph1Y095YjKnweIizsLxqMiq4g7nhVNXaPN55G8wTKq2CkKlA2kXOqSQUHSSn2zCW30EfTchDM1oNUwVcbkr2Q-zHF1XIhPGD5GPfxUuSqszAec3OR7W5qxDVX0ptj_IcTuF9sey6DDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYk4iTI76-79xhiOJEMcIdS5AXSe6YmchEIr4ZmFMoj1FNFOyi2cnhotrNGw2UZsP2Pg3v-8tD5lb7XGE5jWVXxe9oBoXWKIuJgxneT8GbAgAmj_pLxTVbQ9hZk0XIQDttqrQ3OYAm5d9nHkRhlf-tupCx-I9qZrUkfRdQ7ZkPyxwARGbj-DyIU-y3ZPZczIdu6RqxYLw3NBsOrQNSLc0O4KpAOrJD5X2o67vg9SG-1D9wAMvE8HEUylWxPiB0ULJMdfMFALlgauJ75RdUDJBayx94s-tyOoVWdfK_QyEVnyJN-dMH46A2jgqzJ77uV6cVxLTwiRS62PJ6AF4SepmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJJHHrqTCa1dLJiQowwAS8cNiV7Hp3s4SiRIgRxcrY0XoIR3ZtFPzwG-ggcqAuyX3927kD69VSpDhgKuAJERluyMjib1PJ8C7_u34KregP0WjNdeYHZ7thXuVl-GZGmssI99xAnATtaiu0ARe3ccT1Z9aH_hpV-1RzPz0nDn-YJUEGgXBJ0lrwTZ1-B-e-NIzGdLwPbMuO1Pn9tC0_xOJ3N86EkOyl-D33grhbYY38baxMyDaP2myQ6strOkGpQR3dgbIip6wtBn21gxTJAQj4JMIIzCAZSwisAxNTFl_Uu89j9IsoH2Z4umRSfND5SO_092JvjZAc7AhPzxyHFUAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOCmHy9pHBsLJmLQfC1zVvftAyHJ7P1nBHJYBr180PA5sQMroaizc-kVwX9FfENod6bA8Deti1eeVwXChyiJePlNdRczWslR6rGgrplv9obzMW7DSnqDzpq12EyjuY1ByqyvLDTCdX0CRkkagrqzbIFeVP-OsbRbpImlbLwztz2RnlCJyLdDLF1xQcWPeLMBO7LssNCmejU2FL7g8CJPBGDCxVO-A5Rqs1Ebn-qRGqr2nbNsLh9eokzRcUT-yVjGaCkvVjnWQzc_tTdCmytu814xxUz0W1FDuCwHUmrTRDbL6HARj24LKjfQFiqaoe78jAuZULjyfhNOTLs_UFmxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ln8wGIi6Uw8_kANBeAfoFL_My86hIvHrqu8w2QFxZW3YATmOVpY8ZTtvR3-sBjjLtFX4yZYKBicGXoQtMmIa5DexaJ9eEUffXoBABwTDjmLnjZ1foANnQiixcteyQHQ3MZ1PYVmr0Q71wrn9P2mSIOwZKJQiK0Wy60t1XGiHWfc5RKdm3tMtUOBt5j-bcB_Bou_4Z4qSt2575jCD7SwvNcw_oKBQAlgT-f6YAeuH7N1MjmxFGQwYzGag7lkWkLyaPNyp5kqDT1ri0RXjyvyEQJUmGIZsTpATOBgtTneq7R-hTLt1JK1xLU9kqYaiJu1Q0PAygPQ5qUrZZ2g3xqjpyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEtI4E32A55JbTT1Zl5Cfr3Vzl6h63DUPuvNEyxP5rnxZQ_kg813BteqJ5ujhXdt2aTzw7myl5E-NTAJnztoneZMIvfmy546cIt-lRdoKRao7WNOJNNHkrI5S2BJyqs5i1SS342xXyzvLtRkYKYfsH1KJkZ0UCHQWacwGcwheX2mkD7PO7CG__1eAVkgW9QO1AjqSn4vQDYtGJ8cpqQLxQOxinB6yttAc5MTsvfBD-sP9ha6zaW-XBdQ38GuQl2yUXRUncaGwXcN5r2XDprL1S6oBaYNol4hY5M6FzkzmgWCfroJIeu9uebXKIswTLhOQUa7MSwPe_zmL2Q_joFoFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBuDXPVaoEf49Pw7Ct0KjT0Id0xaTyPFl6Y1K8T_6Gy_bXFxxQbFFvXyHo4-pcHRTv64WctWtvBUbkbb1dVIfoQw7OKgKMGWIIJ1stLXqPKUfw5uigE8hwou_LsEyzxR4vyqeIUsXCE3accN9hhg8myFlCOer7PmZQhTHsE0kMj2vldma0Y1fdwQatMSCivEc0R1Ch2zdCVTOqmYqubdupggjlE8s2rweZsteNgdwCisGuggWC_qD97rfkR-0HwdY1fr6MRHp7LzqFQ5cz7xdScmZiQYKqA43zOc6NWkJlwmDvy2oGyFSvbpERRXSMh6aOxFs_Y8hrKMkaBG8rWX5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8wvTNLE-JI86wDzR0riT7BEcYToYVz9BJWf5hccsSndQaOCD7Y4fz8-m4Ve1eTIyyA6DcS0M5paIJMphWt7V5NT5nCFqmC1gJZQv9i4L0JP9pN-fq8nr_5JpkvOk-tQZVosx0C1KdbKYPjE9h0aN0pfeIRqUJ1W98_ADd_Ndv30hvaBFdWR26Zf4lSG8L36NfO7BOSjc-WsKMxczszXDng9dtAchKG-9oe7OFTQUrkNZq0TTbI79YOZayC5P7w8JJ_-DWp-1j6XVa9t8qO9mSq2yqPLpVArK5xXbXjp5zDwZshpuzfTi3Nui-GEKazzr-wQZNaTqhq7A3r8k6oQyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPTtHpWFtz5dohDtkhXJl7CmCLQCFX8RE4thaVvPMq7rY5EppE95wxG5Ga8DPqnz5idkCImgNmhZ7nhSF95rV4cdaxE-ah-TXsscCKBDMMbDoxd_Wm0_C-LUY69Le15nTuvJynLDKuNCQL5-crxSg7Sh7NZOLVtZYfqSlWh03XlKPBAaRIagzM-GKXXOf0Wo5NYgAGHFJFMIW9SikmjGxxPdt0y5bO6wLO4AgKLIBpkhMOanYqKYurBwVwzLMe8DGB3u_TDfUzUJEvuih54XkoR_0-LYgrOf6R4ZWS8nyyPIC5HPeRKZknjAC7RwEMNF2EqArA3_RixaUoK1V4FYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMtEa7PeLnMhmQzMZy9qelHzSAZswfoZVsm_Js-bPv-mtW9eTQm-KWipG489LT9o7y9fYSvxKWki26cScfIP6MRfE9dG_0dS5xNwagGHdbs75zcjowEDfV-Z-lkj81cfF_8gHSC7kRHF7WxoCOh4Q0_SLDreFVAusyQ7294fVPMwWZ-4yLDTz80X1q8kcPk2csnsYdUlTtRF1qrWQvFRdu4qPr-yoynIDHDffnxKxbDiVtTabEiOp3Qipbf7KArZsv0YLQwhjJ-26oND1OtbIQjSHDD-CDI8mlegnugE3HzYwn_bxaeMBD0iFBwbO7xPrm0g_zMh8RaifJUEjj4A_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWt1jAGkgj9nIkwFhlO7r8aPsSE_ilx8b0NSolX7aTUaGgfcGNxFSASuW39Dlb_s3N7BnTaEtGNo2HOmi_nVUYLtd05QL8ivVnp3Bmk4s66PIjWUWp9Mmq_m1hfEphe5NQKnQdSZLKPuVMHGvwongrc_vg2_Lz6wUxmWabTJs0a5iiLFimNXbS8dPu-BQ2xjkJbSxgpq-zMh4ajaARhNMfTkL214JYr8BfeDwgZ5Cpcjzvfg0b0_AQQlXXOC7smxbjkChv6Tmiu9UxJ78hoCuTwsSJhzujC_8IxbNuxlQLnYqGC0JMpbXJpIPlR0w9gF8NnpiKmSeUU0ZAcdctEmeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIDGfzCpuoEjsuXBw8POCeXEu8w7YTBUeQlIZMNyxA-DvFwbpnOzF6EP8HhswP1PYXyMPCIchow1_5jV8eJYxoXt7ef6eE-o9B8illq_M1G-70T1TIof2XHXuiqQpeVPUmOm5XfPJUaz47pNA5pIBn42zThi00MgVv5n0voCpyEP4j9n0GH-dDd_fQMBphoMuOL7nvJ_52Uvbxc8tiQuwr4_Ar41LVRgwIeCbDZhlDMZYV0jQjbjXn0aZhzqmYHxkkXpJ1RJ1TuHwvmcp4kAOjK9hxXuoRsYw2bHNSpt8kfvEiQnUUF7dRFzwOwspjWPrfVsYFYsQ8LiYPU7pScyIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ6JZCQL9D9tdQe1_-YOwuG07hq8Ufp1l3x9BXEh2wTCjZYCe-L9V0k5GWrDKVhX4xJXoaPzBjsd1mCZ-DgJ3UYObGTReBYZaJRXAbX8ee_5XC1HgP2wL58HLHCJz2pJMd1GmL_5HjG3IjRQ_w_QUHPkR8yipSjVwhROlSN4Ky5yDRTDabGFQtlytkMrjezEjbbgpew80eJ07yq6aUurHt7H2ETZmWEo0LyCXKXjQ3jquvwDypsv3XJj4vVo1qJKGS2RbcKCs_zUF4swACixnEQjiDmcc1C_XsTlqPu1TlM2xmqM0ZguaYDJBmz5GyNdoEHONWicfYmtUorX_p-UxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBNEE64IZPtaumDt5ohWr-Qn_o3_o9NzM7XlpTSK4FFeBFEfxOaWftdC6W_kNDdmnouoZqLzFy3nfDtSKtNFCSjAaI1hrvcV8s0YO9x4Agk6UQHQ-K5AuAf9N9YlCLTK9K6G0TvwL5l1PwPBALARpcUQ5_sWeXfYqxnwKVTC3VLHJaxkVGXo2bPXZ7tC1GJgVzuakMOl9nYRgnS3PLLLZ7WLRupzTQgXzAK2kq8WlqqHnAgYWIMr_1xVFgB1EsOHGLAYCDi9Xbe40rkfTrcdjhbK6aNqFmy3v7vVtDgRkVwITLldmqG2NFgvlq2jfHD3La5lVR0ARI1Vzht7el10PQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Zem-Hm5FjMmgEu-qk0pD_YTYuS13k6KocgP2UDcwJpD4y9hC6QAykL0koi_L96BNVKqTiSDSTJW8YXtESegvhbRfPpgXRaWvaIQYNJ-jYErW1DLR5lqxaYy-M26_ZDC58gv4C1O-OrYOJPFljgHOOvZ-VbhTlPzZtMt4eof76qDK7a7Wk7bveW_1WI1eqt_yi5nVAoGQrhGaQipUlNY6ibGWDR-xgMO9ZnhuPouD63yYlw91efjSBC5-npk1fTGcj_nwmRAh-u6UOT4CiQTpazjXtC7DKDFvKEC7G2Qq8DktFifTZtju0P53JKpPCxulC4QEVjF5FXWoKq_-3C5piA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Zem-Hm5FjMmgEu-qk0pD_YTYuS13k6KocgP2UDcwJpD4y9hC6QAykL0koi_L96BNVKqTiSDSTJW8YXtESegvhbRfPpgXRaWvaIQYNJ-jYErW1DLR5lqxaYy-M26_ZDC58gv4C1O-OrYOJPFljgHOOvZ-VbhTlPzZtMt4eof76qDK7a7Wk7bveW_1WI1eqt_yi5nVAoGQrhGaQipUlNY6ibGWDR-xgMO9ZnhuPouD63yYlw91efjSBC5-npk1fTGcj_nwmRAh-u6UOT4CiQTpazjXtC7DKDFvKEC7G2Qq8DktFifTZtju0P53JKpPCxulC4QEVjF5FXWoKq_-3C5piA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeoZg5KucoZ8PLu51Z0Vb3jklhPPr3HyTkC0zrE3-j7i31IYiXDIa-E-A-JjCgA32kohmZ5gjU5FYMqSW_jB2Oc5tSlyzbtXHKsIRIA1IRw4RfdthycQ1MfpFQm9cCwr_InpOPQ9BoCb9AsVxaRVR1Y8S8fYrfgLtN262ZauYVXhF1AJmkRaJQ2DlIvt8TvPDbKTm0qS8ekmnEaYwu52B68_hKoViE9Wl21JeAnDPU76yQSOv48eCyJGN1xgThhpwDoSnQm333gL5h2X0Hh06_zyUUa-ktVQvYO4IPu7uuFTZQn6IPMwVEu0fzc0mHjYXEY4id-bvOP4FcnCNmF3qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcYyz6QUZMMW7u84VMcW5ScYlaeBFv7eLgAXsTZWCZTiW0Z5o1-dXuMx47wOc9tqpk-QnvPM3NQrKG8nKugy7B2HTS2ywkrBMOGRf5P6aQFm_WZnk06umDnPDqVNQaln_poI4qhsdTu-Rv9Pv5myRqYESdE1AVk6fKT68ktmkwcaDqDtM17jHviaQMLt-BAJMKB0qENr9cCTgtQlF0jepZQu64FXq2Fcswjh9OV4QBnB9jIaWzGg19cUVXV5aWEbctwf4wvhxDPzY7wdrr637Xr3egBwd2u2Rbl1wuK56CCwWpaVG3eUmCWMlb0jwrvn34HYIQRCp097rEj_Pjueiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJ0YufssCdzZ7Ugz3tPf0NNrYnCrI918kzN1tAIx9ol6qEW7QCO9abueyB1rMQrEhIupuD0tIWbLxkSxsEh4q6EhanXeoJG4gjlp_SbrA6kYWaWuka_omogSS1ldQQRLaOZFYwJHt2XxLNEiOKHG3LQYzJFoaVcewHA8jkSODKe3UwEyTkybgYihcqZmEAcX6a8zOBg_bZbkfpOVoe8AaHReiNRFG8A6wfKy9OD5ez3OqVgCNOZsUzyE2K0LA4Ffe8fJGv69jI7E8C2omvuOPY8JkmVRW6SHE73FG4kfIr8M0iRTaW7WbZN1lBL99dDz0gaVn7q1i2i6WRu9eE973w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUt5WcAP_UEXLo_9uEwvrWS1M5TYiVUPgVcJlpZljKU40G1s2yxg20CJxnm_DT7Yog0Rvo49Ck5ogWcU2SBnmXIBmONogjjkFHRQxOaH6oe0w4_7YzcmJgZkLFUSiY45sXBTdjm9OQ4P5LAjvcmHYiwGNBi7J-hcixuWw9Q5teHjZAXu0Zq0zkS1XWdf2wL4aGdpco52hNy9gblQEtF-r-Wii4Hcfy8pixloa-V1C7nifI2A8Jd7NjcXlMQXld_mqALbzFC46hL2FwpElKMHut83wg7uZ6e1HQn1nrbX9qtpqy56r0woO3s1u8QlFkPbyurwEW_XABURH2_nAkDfVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbZvuMeHop1HwokvPaumrmtVZEBHuN6foZhIPDL-iaCSGA-HpDS9XE_QuZTR5VK54LBzagD5DohvO4mICGStPaEfZjNIuScp9_NKdYnhW12p7XLakQO-QE1fU2VcXxmPntZyrb5ChsVOgeKErX5TrIsRxG61KeGI159_EBUQ0-NkP1OZZUvPkWe8rn8AFgIspCrSpc9fKLA5jMAgbTtDTfz2jJY5M9Hgduxj4K_exVwvRDWnEMRmbTtAk7EYOtlZm99tVtimnDGzd_SM6mJEl6kJYKSATb8b7j8yFQnLiH6gsSCHKsUHun2Fyq8v71lLMPgA9FMYrFGF2zZ7vM3N5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eruf4jJhKVpBCkSxu4YgTDzw4lNNL5rWHX9bFRva2Zqj1b2FlIfJ9mc3P9L0AjHsu867vzaryicvvUGe3yYAWWl1L--tQFqWKchG9BmvYa1be9u2rm0aFYNb9e8h56zr_P82QTKKEsAY2WZPDGwLIzfQajPf_K0akZZl4cC8a6ncvM9VPTvK-_LMn5kMI0VkR51D2OTne--L4Ubdc0M-aelCQ0YrU1i-Kvtr4jJqiQA3JFq4AcVhMtMM0PukjBckVZSREXiEU9b2JKOlm1J78X8-PX2bsYV2j3jWbWdFeRrMNMQQ-HcSjax-6hCBTGtXF1dyOe7rju1b6gXvvAtJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFv17RbQux-FH_npLAlrQ-6ACnohRZmEWb2ne0K4fMhPO1j38KZ6NV2_xxnH8nhLQvBDNjJC91OK4A7-vzd69w8jy_JPFRY1tDDM3l0sMG5jn_U7jQbcl1VUFDI1tdG-KfKsscqWay-NiHZhoKyzyEvwK0NHG5C9PgdQfoXqaGluSb0W7ioGoBTu69M1DDAgPUaqmwgmQSINljzBCrp6mViyk4jwDPWF5aZSlxkS8qFFr__Wcp_H6vZmUJ1v4FpWQK9PhO4V2Rml6MJQlLpcYhSva-LJkjRTuK6Oj4dp1rdNHTxpKh4H4uPlC1NTrPNFzgos4gtbfBD5VvHrZdfq9A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=gTNzn7pm32BaCW_O_o-2H_HjggbjmXGJfZRB6bpZrA5GUc5wjAD7wdhyOnG1whQ2sM_DN14UHEERkImLHCijwyCfCv6DhRAcJOjeC9jS8iIvEqdZD_To_ohVrMCPESPGT1KQsZCJDOFuGB_D8EVTNAhGeGx4Pf2SbWSvEe8OH-8dKCh_4YV3lPbBB40YeqGWa9SLYg_ibseFrWU1U0N6TjtPmYtRa2Jahr4_-6K7KeWn8PLT_rbmLM8HDNBduxOZlD5ztWsHcSl7tYTE3RnTbp0ZvE9kWlvEOExAiTbXprqvdgSh1Ydh0JHH-vKMQWTGP7k96mRkb5lzhLA1Sm6DIEhRaixO4RjIT82Vz8SjZ5UYb3BdxJWOlwe9QPcPEsxfrBfzV8dlybst2atHdAhkveDZ2weKA4DtyENbuuPSwUggK2meE6vVHkTc1evkd5YRRVEPLDtMPtaaM_NkKjFV5itwK7ecVtSKXPVzDdtT6yA9dgNSOCNQus2m55j4J7AXd_COOgVUItO-20IuQnyQi2GcUCQ19p4CszHD7mbkHS9inEZ9Z0LDwkDH1fLORI9CHMIhR-25aDFFzobQ2eer8U5LWxYuCigqOI-7ZUYaceQ1COeYlGWGUEapPB7mBv9fdujgBkuGfst9Aufuvr-5TWtkIQKanaoUiVHHKF80qBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=gTNzn7pm32BaCW_O_o-2H_HjggbjmXGJfZRB6bpZrA5GUc5wjAD7wdhyOnG1whQ2sM_DN14UHEERkImLHCijwyCfCv6DhRAcJOjeC9jS8iIvEqdZD_To_ohVrMCPESPGT1KQsZCJDOFuGB_D8EVTNAhGeGx4Pf2SbWSvEe8OH-8dKCh_4YV3lPbBB40YeqGWa9SLYg_ibseFrWU1U0N6TjtPmYtRa2Jahr4_-6K7KeWn8PLT_rbmLM8HDNBduxOZlD5ztWsHcSl7tYTE3RnTbp0ZvE9kWlvEOExAiTbXprqvdgSh1Ydh0JHH-vKMQWTGP7k96mRkb5lzhLA1Sm6DIEhRaixO4RjIT82Vz8SjZ5UYb3BdxJWOlwe9QPcPEsxfrBfzV8dlybst2atHdAhkveDZ2weKA4DtyENbuuPSwUggK2meE6vVHkTc1evkd5YRRVEPLDtMPtaaM_NkKjFV5itwK7ecVtSKXPVzDdtT6yA9dgNSOCNQus2m55j4J7AXd_COOgVUItO-20IuQnyQi2GcUCQ19p4CszHD7mbkHS9inEZ9Z0LDwkDH1fLORI9CHMIhR-25aDFFzobQ2eer8U5LWxYuCigqOI-7ZUYaceQ1COeYlGWGUEapPB7mBv9fdujgBkuGfst9Aufuvr-5TWtkIQKanaoUiVHHKF80qBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJRUKIBQG2pkZcure2JW2lJMy_PFK9ZipDqlg0iqB1FhfLSRtwohTOiIV-GBvTh6BbPyV3RssQWMAOD2FaoSG5iX3Q5sXYc9BsFhCBroWjsweqt-A1pR11cBv5WS0ERSIGXCjglyrfhpx_NAt7M84j7hN13b4NwgJzDIq_KrY87WmBL7LF5QFQxSNZTWPNQ9ZwV7T2X_79NshA6bDDXbb-rGrr0t7hDBD7drIdjtkdrR9jaVNbJO2qlOlj8K6LuTUNJSwnNKXv5bkwJGgp1SyrABLVlBeioQ1AGZLayRDOc9ULh8rSoKLsSVWLpdEDqdBDnP-FAoGAnHpGJA1LsKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYBWRzD5aX8XLDLFFzaW5iU2Zb-fD86tP9jUq0AckyMOV68mR1S2H_dn_j-v-_ksINxnF-rLaTlGwtzJNsdVQcm_f-8RDTqRns-6oML0JRbw3WgpXL9lsFhFeRKrjSsxZBfO7eCUOnYrqK-lA3RbPZAl0J8-xyEm8OnpJYJ7NzoaO1Pkfgg-QrkAdbqZcz3sefydvgrwZmKkViwdBruX5zywk8WrsZLW6Zi6Eik0KPRKCM-OjurhNOuzttMJGb-Tm9i4P1NH9cyuF5PxqzoYWQW9yZyYm1hEndZN8MzGiPwg4Yg4-bmkKhZaUAgzX9Soj4p5EfKcaHIM1sNXfvBq-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CoRHDSzkQNjOQ1I30MWy_aa6WSOSRxr12rOf43CI52Fo7M6xl_E-kTYlOJURtzm6dX6aRz-bNoVM7ZuY0uKa-w4jxp-QVm9cDDI89WhY2fMSmu_A54qExJEfOwQOMUmBljbEZ3nw42FOWuz_N6H61EVguibOsYX3SmTWr2ZKK2mKP3hg6gyGuu5k_KqSuF2FUEEDCdfCB2ugumxH5d9HWAdkMt47EL0jSEu0A5L-H3DC_SU-SvtQD4S_BGPUfm6DmsfiwlZwUGGxvcurhv_YbJaP7y6rcjuSekurtqkwHzcLEvjfvwOujjcV7lci87kDQJZE-jIcJrwCBL4gFGbdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDmSUlFPeV-sopDYtE1LCrdxAvJ9h3PyYSeg1gekndYucjfonywlegUJBmPMZyyvNFimHf34DskIfY4RfEU9QiGmDvioUBXJekU2VIL7T6tW62rfmCEUN8bjpsME4pIhSstqX1-T_FTgi_F3Z_afyA_JasAryAKhg49LlJ342ZZpXBTAF_On6UraG9bPLbH8cEr_GDJZSY8jmqzdEY9_IO6ZAhd6GUE9KOuFw1b93tZQ-MZcF9FbwXHx4qAXaZxia7-rPhyMlDPPhUPaph9x4MgIHWgivtR9z7ZB2-Ly5mggjw0rPsE6VFIDchdodxwQTo8iaeNhw5KIPoHOjaOxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbPWGIpdvcOr9bKlN2cK2Q6YB-Aoi7NDeJZ98MIZB1lfJ-7CHohmAASlsYoKJ_KS2FORJ8wymLf_rOSsseaf1ZfSuqbcg4yzw0KVT0dpFiUrXPK1q9KTwl8NAR3Y7K6b64V_gMH3dO4sQfkXSB7g6fxzpyD9iEGKoElj4qbRna8sNSQrpbiXtO_HyPIs1lN15ZXHQ5DAQDCdSle-ZVmmaSXe_UtbHml2gPDWfjEfovWvhSwXC-igXGQqGJtO1giqf53FUvLd5w0jlq_xm8NbyA4-KLv_Zo7foksXZHjRmzw5td827YbBfqNk7JMmFf_n44irRxF5FiMUveigeqeTxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aUvz3XzyCGnWGtEna9zJpAXe0dYeVFKE8ddABorsORKG9YhxnMxZTha0spwdObuXTIhHrdUABU54VRPDwkYV1Yfx7BB-AwNNgTJW6tCP7QPHygahVnmFdYTLIXXf79tc_P9H041Ewh8rrLOswxA2Rx4WanL_m_8nO-m1NBt9fZigUYKJXHJK3OOaH6pdT5JxpqFmyyOvcj7J1YJTIghu2j4WXd0qk21_8rjWmRa-J68GKD4YDCygkkPAmRnFhevfXRdok4HH3xrS3h1FlpOWiXA9qTNfGBprKXb5luZUXsIDM0es0PPvRIeVwyZE0R5inL_M8inozAtiNSTh_GJ98E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aUvz3XzyCGnWGtEna9zJpAXe0dYeVFKE8ddABorsORKG9YhxnMxZTha0spwdObuXTIhHrdUABU54VRPDwkYV1Yfx7BB-AwNNgTJW6tCP7QPHygahVnmFdYTLIXXf79tc_P9H041Ewh8rrLOswxA2Rx4WanL_m_8nO-m1NBt9fZigUYKJXHJK3OOaH6pdT5JxpqFmyyOvcj7J1YJTIghu2j4WXd0qk21_8rjWmRa-J68GKD4YDCygkkPAmRnFhevfXRdok4HH3xrS3h1FlpOWiXA9qTNfGBprKXb5luZUXsIDM0es0PPvRIeVwyZE0R5inL_M8inozAtiNSTh_GJ98E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snbd3qNwu9tZ1EjZclA4pQzODRhH7y6prTuNwqWt5v4XLIIx51g6rfdY5PELQ6rK-tLt0FCuPHJ12moeYSDC8nByPqewk9FqQo1kEJW6yjHVm5SVtisrrOfaRmMhC-Ze2zfjocgfqXkn5gV5g4HHCf2qOp295XDr4gu8x0W75Ae4PgW0RLXsqr9G8eF-PsQPON6EKKb_u-4hhIyukDubDtiJ-X4SMy_KLnbpBDtprIce8nuG8vFPt9rSNnrOtbNFksVNLGfpJpulgwAl5Uptvs3qlE2F2oz1089WPibejbKTK-vnrM-KaGS-a6uR4yzyhf_5r1ziky9sVhJkSBDUVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un1HacTD_aEtY8NNh92PC65H72jkkj8Egqc2n4C28QmpW-paMlom0uthgCr1pwg11sbTxEALLuDjFMspZBFFdmCHVTgprG6r2HzoT4w6ANRH_p4gy7RlonSMHWrIqS23SSs-OSTaC3Ma5HAO-WAbg2ceCwkbtNjZ7ILfJ3Ho4oq_mzGzewA2piQFmS3t2EiI4JJzf5p9Dm8vycgbONL-ticJUMCp93iu7cQhMXQkQxWPLR5WumTjo8WUePbAFqXqtP0LIpr9cHKg08-4jANsThz7v6T5c7Rq5I4yhVwFVVVmqfGwBbaXTokOgnWX6euOoAAVcUkYDfHxHImgHCvHkg.jpg" alt="photo" loading="lazy"/></div>
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
