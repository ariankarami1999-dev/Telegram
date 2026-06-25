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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aprgGYzROiYm6hpNHsTlTsGk0XOyat8kuS_mmfwwgrmDiLRCKkMkjzX0xT-th6iJKHNsrHbR5wn-3p3KE6wFC6GQhBO_gljOJr1lLB3vL5MP453bLJ-L-T56tz3krQnip3oaYcZk2YTnx-p5NsCGttewXq-mkJ08061pRFMPBsWnDb7XymV-eKdV0Q5v8wv9hCCIW2HfpTkCeSW0WGVTMIaN23apULqvrkkNpX9GEelUB-EPorzsNqAqKh402XNfs2s50lh1L32jblmpmW2dy0_oC_F-moT6Vw1H2pwunMs_GADWTc00jEgAJ5uAK4YvlaMtXI7t6l3BTcN_bDHXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 163 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 410 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 561 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=StjFACChKlODqduaYhxNKgeJYOH8Upho5TKUIHD_98EhYnrm8ek0LCWw6DlFtzUVVmPtQiB1jb4ZFt2LLZVhdidu6BQvIFT9Vf7tmRj1xw4x3fgiZZS9-97FZJMVRHkVMxQzIEUyak7hb_9vj3-IBxgVJF6biGsnQrWLGV_uIqhrKkbgbEisa3xg7USymsDt5mLxxFfUQCEXfuxVRIe2q5LH6_E4-zGARpsdOPYqxMhRnVKfeDlyNMRDtSYkKtsnLulF6YafMoIsQ5O4sOSgt8FVXEujk5mchobojSMba5tfrgqsTdTS_eszvmj9t3HkkTtcqcQEe7qZPYzFJS4qIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=StjFACChKlODqduaYhxNKgeJYOH8Upho5TKUIHD_98EhYnrm8ek0LCWw6DlFtzUVVmPtQiB1jb4ZFt2LLZVhdidu6BQvIFT9Vf7tmRj1xw4x3fgiZZS9-97FZJMVRHkVMxQzIEUyak7hb_9vj3-IBxgVJF6biGsnQrWLGV_uIqhrKkbgbEisa3xg7USymsDt5mLxxFfUQCEXfuxVRIe2q5LH6_E4-zGARpsdOPYqxMhRnVKfeDlyNMRDtSYkKtsnLulF6YafMoIsQ5O4sOSgt8FVXEujk5mchobojSMba5tfrgqsTdTS_eszvmj9t3HkkTtcqcQEe7qZPYzFJS4qIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 587 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU_qQqRr3La4PuITdlGmWB-Ndwq-DP1xpEUZiDtD5WQ3Rcv2zdamYzBf4-9c-g6GinaJtobc1ntb8eIZDGCJpYIz5g4OFnzDdmmvuDu1IstSBqimh0tapR6_5qiOJo0PAY30ZmrfwUiNyCJ9w5xusiKxnVCRMsRtvZBWqggRXo3niCkPRikgE6NVimkaMmo-2BHjELG6OvnAZ-LY7Y2kJ5JMXQWnes6I2ab0Fiw2M9FjcjlzhDS9A_58ISq4LtRjCCE7G0B8Za2Zys1rK8ckp059LMFub2nsfidN-SL9qO4WOyZQpgrD_Wr2zPvHOznycXw9R7cVqpK6o-i6zE3IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju-cGrHXj-F-j1V6cdWXUK2zWaZ8c9xksHILsrAYMW63MUJvmOp5OmPsmKwvr2FV0gDVyDWbNnHv22o0VKTh7nPtU1ee74_XS2VBMjRwbzy3Bou7G5Sm_YlsMjtzAX3CONXqKOs47mPmV_j6e38x33CwWVv7t5IcrIpaMhLWC5n6wgWmkd1I-B85WWcsgyFA6ZjCYssXw7lLWCv6MLLaO1GRnZQNQzo0TesLHWSCiAasAZagFy6757dcCbdH_ASYcloLqbNAB1cCBAjyKOnySAQODdVvSJpc9z0OqaXmmR6PaOuUzF_7yxuMZ3Vky7aSeK82zzBlxBqQwhEWXDKfbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq8BkmRqWvIT2RpBuz2EvplFP9nyhvGJAWVk18uDq-X2eTN1iMdRMYnFfnZbYisz9gJC662BY50j37ifwU9x8Vd5FDUWjupOsDIl3gQWirh7VaSW0dytfrp0XAN9BO-1-7DBGYJGx1JRmWM6iW866KFFTo0hPtLPUNA_VOYJqzWKpNnKW2tMPgo02au8oA4GExxJ-f_olflrBjT1X2PPixsjexh74VQor8ZR81zAp3xR29PhPX5UEzsSOCWzK3ypFmQ3aN7FSOcGCVKGf-LISebKnDxWZtMbAUCApdQFrb13Ly-Qvy88JYTHEwIHcOLkIFcNXXl9P92eIgAPBxJTdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiqvzPJcZeJn4XFdtAJpKIkVZPm0Ljje-a9s7IZgyj2tcUrVIcsUOPQjev89A6WIE366-mp_IZg3Zpmdb_8LKWnTFvHaRP99ucBsZ0-Iyq99D4LGflxCUwL7TAfgrxfOdqJS65oC9Z5xmPbn35J7RfXCZ0PDDh2dFG4bGUvqQziE3JGzC1TZ-iCgEXwxQOfcnaayl5vECgC26zUi32uJk7GuUfWwfy8WKSEQHe8nlQ8c5v2Z2LEX_6cUZr2FiINiPKv0xmSUvwJGYd4hi6PMgS1sXeZb5-I2GMyZdcYzHSk4mzVvUeY3JNrWXwGQBBqK0_o_xmWrQIop5Dt56j9L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L28uszVC2Y0r0VSOZ2LFlvaJz_VXOO_-ZKCvv_iVByFsGlvTjrWyHh5MWy-n3A96f3U5FI3utvpsG15Kx2UBZoT05wjLG_B1HuK2RLSPm595XRtYsh-wQn52kAi1zyJzN4Hh-gl1tRAAgGXBjoqGs_B6CtMTIK15wwibljEYWulYtg8lFOnTEFzZnIDN0dB9XyF6vueKHZpVVu8iqYdQr3vDsL1AmRa2LcuMlunarsjVGeMzFhB2IeW2f1S5bhrfRM7UqC543abtm7e6k2HyAlWFE-iwMqaxofFI--xbmhnJEA_WRCBOy7Byy-PqEl3fEiLL2pu4hMVCyxDPGprwkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2HAKCkxb3Bi1IwqFxM4SZjnYlDkj8Uioi0Foi-oPzbJhTO4o259tWbInhDnfBBw25htrpb9g5GEpaheTGclNky68X3G7UQMrkBvBqY7YpbHhKXwy2HSTT4pnaX-9jpIKlqJdFYVHDt9BsVccNTxgW-51qtyaOrpHGoh6pnRkO7rR7-pPnR2vDYwt_u7vbi1M1lj6taX_v6asi-S0imlJmQC_Zv70hCFWBFn-STu4cYBN9FTCAg0uu-5UUPkKHg373oi77Afaet5SnlDwIfC6E_rxyBA-hhtoV6_107g0eA9d3NwrJDMhU6WMTbkZy2O9F7LuHR2wrhDhssSmU9o3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 829 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUFbcMZ_sew8IeIMyYSIlgbaxAHaH94usg_wMUfOBdJmldhKTE15VVtoKsPY9CcT7yJ3MsQEx2E53sEhzpKgWPprKEMl3DxuKtlbXbqWN4g7Hn7-4TdFM3KMSFLwvZ_Bx8ZNyRZpvh-2GIMgexS0gFqLQj-l_P5DRTMLP7h6RnntJBSfL3AUfjhzdN3ATbUSjBGwzyeWYQ76GipF_QNsOO5TFs9kId9tguGl06X2Dde4dfk-ghqwnfbEgm_wvDhKH5nLXOAiBQ4EebrCVvvEUZEigc9G6DMY96tPCJjidJdDG1_4YV46eHtbCBNoT20QztfHf3Krqg20O22WoMiZtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j36Cl6h-3cHzvHQySQfZpkFBgz0LJzDYCI0XpJT-PxhyarQY6kBc2sYOrC3uEHSeP89hQq6J7CKlxEoNPO6cfCGuJwHMJFdIlflySR8GigbV217CCTHGK-ideQWs-JXznDIvu8uaVtBLFT-KlQKEhee7rFhsmhvZtLw9N2Tw4HW4XdaoNPCSPRAGWUrlUsbeGDylCIAd8xXLkx7dL3JtZhquC5QuHeZCuh2Cs1y8aeI5LvRNfjGidapUIe7oMLc5slUdyZEc3xx4V3V9HmvBUscB5y2f89rywZhcFFAIA92Y5dJIOxjnUPJ6YESGGjQE_IaE0wWD7uO5U7CgtLdMSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Aa2DOUTUOg5IVZ0SmBDo407LHXhZrYEsH6VeZzc3STip5UdHKNvxV5RLsbkbGOlQU0tE5ctpGCdsBglDVIopvjKX7mGdYstg7G046BptiIGYTk83ZEy0xcxbOrg19u6ybmxLaujXPgeNrGDziS1a84Enuu-8rk2WJG1XMjDAgMI7yeXzHUPC3uzQmSprfZiEF8CxiKs3P5faMSRijOzXexWSt1iHS1c1emKkRNNFw0yJ-SVkv_L9FwTivDEtqWmQxKMY-JPWnflITB4wQd-8XdmdttzdY4EA38Ql2KUcfLbpt_nLSWJTDG5JgXZc2IKZmQ_-8mcKtpLfmnDEgL4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfdmqbpifqSPqHXx-K_K6UNiC_XZ3-wHsa0-JDk9vWRoadmz9VCcCrtWeC8OmFeR3_D3O2w2EswZaLnaVOX6JKbKbMPDsOb6Xt2Hhy8u1PaiSKwPt9cfWIqAvqggWnhoFWWnVG5g1v7Kw6G8tqaqvbcvxnfl4ZrbSf3Z357ePz-cUglKvOJW0fI7_K_QVtbQdJCoVBIZuqZ110kePXLEH3gpq8-Ibtc4XWf_lD7dvZst7Ob52v-tiGnEMfBCg0tCoGvguNaj_nsGohhmdwsn36IBpz3rIm2Y5bQ9IHF_LlswvyuSiJTs5qCZc3dLyIHJsO55TXosjNz98v5KG3BfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B26QGjCij8LxCrZ9J6lkWPu9WwHr1a4KD9hcAYSEv2MChyR0Lf7hLhemVMLamgo_U6uuAU_839_ko7rIBxVA6xEa2ArlrWtC__vq1sQc-w4jAlqe045c7ikEmOT8zXsLLGyda4odngHAtrzmmJXInmTMo8VUpIeVy9PCdyWAIHbCAwlM38YLK6TQOARSXZuaaK7YWe2vShxt2Hx8La3mmZnSUzkLQffYyIa4R3ohaVnlm-nw8NQ55wLSs0ivFJTNSz4D0bUlvFNGhuYiwZHqHY_XDaRvRekjfXmL7Zu_i92RVzSBXBX61hx2QWvwuO7NrcyUEQDvR8f54xGPlaLY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHrwGn-39vlotS2YAUl-sBr3QjpFzUqajikjal5MgFYsBj6OAwMK7v86ah0M9mTnL5RezkNBPXVwIPrQlMOZm2PZPIZiticpv5gsj8IZ4n6eBZz3HV15fCw77_PpdU83kvwsdAij69BSMHLICa9TKMirk3wkUFLP7hkWkvmX1abP450MS5KGtQdT6PjL44wJ6l-O66FFUZj6pU0VAl5R-J8QH3Jd-huNopnPa1GwJ9gE1zmjuyZAm5HgQc23go0-y04NlvKIP4e206hizy31for_pIbqMcSk7TB1tPFUNkIBC-hrJUS_hCxQr0ktHfBt7NlLzISlD3Oi49at52ymfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi0K9yPqDzpSvF9lwjcugP4UQr_J6FeOgqyszsYBq_QV-BghU_KbXkL156dcbvjhKKgxsMBaB-Y14m5cv60nY5BWZ8jMrik7t8cCtJGGf48vhPB4oFOV-OFueK8o08HQTMOZxB1gdSkInANwqQAtGoC6L8726SwbitYGO6CFz2EXXrIZ916qqJe0EKtmSV8AYSUxoklDWihKNA32kruQ5wIfa1Zx3f7sMA6KmCQ__M7CmKO0ETgbzkN8J8CDb-CB5_NVPAss1YRQvamT_oZDlYMfOdPMmRcdlV1tT9md1-hzjTd9kVyPnxbdCZJDJqxxMBHq3W1T3PwCQgKP-KWMzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhbPaN5dW3hx6hbMfQRFHz8Kc_gjIbJw1tx3tFAUDEt7a0ObVzsvLBT0YSRXRZrZFu4vXs50r1Myq4hJ7nP3G9Y_qi_CF3-fAcLu9sXSIhMOf-9CdfadEULcLTOKm9n8dtfzWWVxCAIbwrPCOOrU86zOS2dhch6joJIUuL6MIhO7xVuGFfuBRiOMFG6hY0CQ2YNh-55wKn-c1OA1rCuR_d_VZQUog-53gkPmJqQoUb6rZ7vzmroy5qse8nFp-PVrzypVzkXkl-k9usMI6Jj__dsbz5SA7qzvdfTLFGmh8BAyG7Fp0bsPmdZAprj2CDV-pgkV8284OGkMe4JPugtKhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Co0MlCw2wQkw4MRiVecBoO3CBwcLVJo6fo8TlATb9AnKUH1ZdGCspWyv72jezYJWzpKeInmInSMSfqthLdPCHTh4XlxkNH3CV82laW9D8P-UU5G49CnLWOLBQflcOA1T271-81bAH1gdzxC3Ze0zEkHyLEFXtb83bl14YlQHq30EJ_jUtJ7NEbX6E1snsn8C7Vj1KnduBlu7olaoeRbKinrr72LKSsLTdbtxMN3vrDO-lNzhzq9x_9nkiv7IBSw4yQI9hzQUb2c1qI5nv-Cy4wKDhosW5E-NzObNIpP1CtorjPKyVA4yXsF8zIk1lHIHCKd4WQT-r08iryiMg-ukUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Co0MlCw2wQkw4MRiVecBoO3CBwcLVJo6fo8TlATb9AnKUH1ZdGCspWyv72jezYJWzpKeInmInSMSfqthLdPCHTh4XlxkNH3CV82laW9D8P-UU5G49CnLWOLBQflcOA1T271-81bAH1gdzxC3Ze0zEkHyLEFXtb83bl14YlQHq30EJ_jUtJ7NEbX6E1snsn8C7Vj1KnduBlu7olaoeRbKinrr72LKSsLTdbtxMN3vrDO-lNzhzq9x_9nkiv7IBSw4yQI9hzQUb2c1qI5nv-Cy4wKDhosW5E-NzObNIpP1CtorjPKyVA4yXsF8zIk1lHIHCKd4WQT-r08iryiMg-ukUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syakfS0fYTJtFNMswM0Phc4J2aU4E9qndP4UJegHi4nBAxgZv6uW4g4Ic7yovxMOCDuB_efjzATxr_NTBB5qFdlMs-oq9xHK0lubXU3ycpfRpKJx83Z7LdIcNZ7yppzAUNtpWYyAtesuxxvPdagJmFh-rG5JuIf5Vk4MwxlNfT9H-MbIrsfSnEWaOv4GZ6GYr8hKA2b3B5Cs5e3AvEicrOAA-uaBI2ZQr3533cMa3z9fvb5yLqJqi6QUU7ZgsRY6bhyiZZUJMrHY7BzFeJkAn9wXYZPFJg7c1sm_bvIYetkMeqkBUcWhRNViDlPGi3JpteSnakmUj0LDE4jbGAlfHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBWi5fkbboD2XeMx2zSlX7N5aFPDC4NHphc38gt4bat4CDPrAvn0NhOGnZZF82eIxSw52uBqXPBCKDtOPeVq-JVqNaNuIwEz3P9R4pl2nbqTgwVXScbEeUH_8aaRoaGApmPI26TfcApsQgyY2k49U2QtlgIe9ewN6TCXqaNSf2YG1zqSxi3Bk90VK96BtDtEF1-Jyp38zNAuqcOH4rLy1cq8u7DN8OCP8pVAQhI-0pJ7tqdRTvGBvzdorn56Fvk5Ajm4-DyivezBD7k1roVsRMyyebeTuE_MoIOoSdxCOupFoY9AUYBqL17vcBQvVG3Lw79sDf84ZKvJUY58EBGcqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkma5jFPCeDR00Za8bjENfu694VQ_sXGKBnBOG4dQWs3Mn-xKMfCXAlTXrJjOxb3PLFK2vmAB6pbFkJWy9jVccJBQwMDnvbDK-Pf0TidmBQzbyMJ9cVT70eduOAknLyry9zrY3-9fspajtRzJfQr9_TEjv34Mekb5VoRHhwX2v_Pa42LLguje0vQGpYRQwLYPvGhL78f-BmsuAhopdcUtFlb6wiGxlXVQkz3M8F1yR7Cz2KW8t72-z7UdeyZYT7yuOUdAlSV3LQisGCnVGPzFZivXzfr-Bv2GwLiGwbZQqs_mpQdyjUvHT3W_B6oK-t3l7AF4-ol7XMq4Hu35JzZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcSDz2IvNFcBJDTqngI4R_dJD4awF2G73k5DgRnodmahsO_dBYWoLZKE7IwBPzCzDWc7SPnhgD4NNW0ngW0c8A0crR5PKZ7ZSR-RRWADReSF6T0aIGsuIiJcgXs5ONtvZ2SwvYU725VfAK1z8gK8qKdlcQpZ2Qn_6oVzRa06B8gWUEmeeNBIk51BJ_pIt8bQD1KesQw-exLKVIxsauVPK6NpBYuKaa1zwAjWvgezRer4dCqECdh33WYe45_AThqUs72RXw1dXCEg8fgbTFjwTWm5ZMLyLGfnVDQgGIgmweDmPCyOSmAY_xNahT2U4m0_DTylM7Ntzad4NQv5iCIRYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8oeovx6B89FXyg80yidYmEx7IUUAos4Wftj71ZB2_O_NbbbjQbtDMeV0jwWtWCujczGgxmY4RPW4clUbTJaU16k0uuUjjPF-i4CDGnq1h55SzNmdlnl2B3A8lNqkTJFnIhENACt9BQo2ibrheY6trK38T5M5-amOwRY7zPTB_otKRnN2JgBxX7IHS-WFKnUnb4t_9nGHtsjIxkHV0KlYxA3U5vc1W9u1XpoJtEd8MjR3bkpyn337dm22xKaQ9aXxxVePdkgApPgNcQuNlCVpHHQHD_z0Z7hLytKTdkEwWMXGgfYfe99U1lhsVZupXsqnZg6fsR0bJW5CPrmoxwv8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at6OYfu0hlmcmTLB8rApi23SHoObyfLLdeJmWh7SosGBzeT13HQ_l1r91qBkAosDOupO9v4dfbdjLIQvXs8nThKf5GRcvddk52oTeAJ5Es4YniEP1Z_vtlqphhM3q2f8yAiWwdGWgf4I6y-tu239cgqJP8cwgeBDKWgdVZIom7NBenN6D2mCyqJ_YTQ-HUjUJD_y17YyBOA5YgS7jvrnUlWmgFKF9jcAKe4i2mes1mBj3HWFSmdUtpteHjMlbKy9wayfRqW42DAMh0fYphxEcGumBzsZ8DctFlkC7ScwXTyV846wfcdehR7C7Sgfo2nJBg4Y5EPG7ng2si5wgFYQ-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbTu2T1nvm2430XqMvgs5VUmLzFw4xmTq8W1Pe9DhpowYxy6iv7t9P9ikXkEXgFXAm5y_ysrqK5mJVDzEDxTjF3uK3qidF4yfPcUiUyeUELlw-nnJCQv0C3z-b1xlh1lIX2kTSh4HT3A8DvGt2Oca_n8aiECjWqidlsklQvAasI7DIHV2pVfCwTlrRGLOXu6Ojg_Apjisv-HNahnkeZqSq5RujMNWOzSoEVWrczLRAjuAEcmF1tgyyqoiqegBIG-w3_heQxHVqAJKezn-CJ8JBp5YJ11vnbgG9KTBCdGh5oQwzx5GrMyPIVAYaeh9eWGNDdmkOtFyRrYYIbBrCzkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGNrp-qs3OMUBNuNCSAdBCvf7VDOFxLgKIFzfRDfnVNoWwN4jL7c25EpGJ4uZZHRyYyq61hpR6kQJXLx6pAXWfhfTurYJJyOc96HDQEUjLmKjMFLFqooKwyQYLnRt7wUISKpba-CUki2p4wRxBsh-T-QyIhccB6sKXbuvbDbhAg2mrCIWCx3w2qnYAMnJpka7WJ9yynoYfnJX9pVEvLj7j8gcCf-dxY58Um3WHaLvMlvEBzYX6-JzRcBqK4VHCndFZsoaGcdhPH9iRBi5Zzs08Ur9rSHdy6iM673FIYreRwVAbl82QuPp0e4i7plscuVdELzx5y92Hx0AITia0MdHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOsL2fGzupx0j8U6H8m1P6cha46GbN2vg9I4_A2qOPO7f0goVLXutdIrkQz97oj1h7k53IKYTXfxInwyvLFxMYEp1P0Zvd9Ewwf-0mPZVMYoZSkNW2pY2ZS_QUNMi1bKVgP7PRkPhO_F3xBvlrCPSsVFzIGP2rabFv2OX6nedm6dPX78a5e2djcg4sScjjAUdrP-YidzRXvzuZMnRFkfJuw82ithN9qsVNk2d5PiK59OAbMPPXDIotnIg0gW5Jzg2Rnc0Xg-8JQewwsezbl0QDx6HGPlD342emM8dkQcmKxsMFPRk7oHIXARpQ_wiwJeVpGKQLYK6G_zulDd17yXeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBYI2ueKSOjUGoSzOj2biTRbjD0fsMzHpS-nMTDeY5w05eGen6sm8itjC7vSjvYTETCJZ9rXv20VGF8QW1a7TQjNT4m0T2aYyFOFsY44thx1URw5tnu9SbZHT4dSGueEnF96_EUuCu7d8U6TgJtDMoDO5EIugIaicHFcoiLoUAJ-8no8_LyWkUKPhM54uCx_JblgP0lQvv7-LmWTQ_1QsNAVYF9gWU4O9UdJ2GckEyJWa2MmhBAj5WMjh92i_LRZSiQFEwo7jSfShhPnRDXcXykwRqglsHH7ekVOPKSfXsDCnHDj8EK4yHep6xPfGOctnyOyt4tZ7ZipMykfTULK6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoudLulI-asi-gZbwV98W9Gw3dKwAY-RUjdr0fVkuhRIsjEh-dbRDFp3vjnLmMtKdASQkhccLGq-5ijNmzmNIrEku0lZ9ZFNrujYdY0ZzZjZ0qppqjsoTCR3rE0YgJdYTIlEfogI9MItql0poeYvUpX78gN4BDsoTaI6t8zMFfVuyJm7THuTW3o4FpYoODA3lnSppc9Y2fw2u2ObNT0U8JQr9iPjY9TUd0mBxnXk_m2uksDZXiMTqssMONc9FwfkKrbA_ZMW4l4pdciIDdQ9mVHeocw90lsQtsOgvYgTmGDthJ-cHF60biQAZfcTBG2j3ZkiPJwHinPu9i2W7CrYFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9E2LDaSrgLV5OX_TInDLhipfdtmpFwXZeoiXOl5tojQxM5d0Ydnme1M1iUhrOM7CK1tGfWj36jI4IB9rIJiYgxVmrIPQLGW8uKH7qZM9tNvUJ7M9fPWvjvmD_a8z_F0MnZDnrsnfrxMU8INlviv3FvRG0hXfKLh9OAbOjCuRvTK3EUsxEDfleU5IOq4FPeJWR5Dzo7sH1Ftm5CF3dXgzion9o4hLHG0R8yg1EQhunYxgmAmI4AT0T4C0qtdctbh8a5bPmbf3isFd0Wn-lTmjJrXdeLaT9vDG95Bn2Alx0yK4sFxe9huhlxschtzL0mO0khp0A54-2U_cCDrLaQU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhGk6SwVAsZIUYY9VLgx97hcM3VHfbxp5PP67GiTjfOMaDoQEWVRE0jNM96kmkPKy2M3y2FEkxhiecYmqV4tTjygO52O7t4AiOErARRina1MW6yvyk_JOtGbpYUyEdber9NYLnYDT5MuNXWDXsKDGgF2Xyin3AgVp7gp7WyoaUtmRguV_QplVg2A2oTlIrkPGLTQQk9rYU88JEwWUoe-aIOSJOpJztmpJP2hKirMbTbPhtpaQfXHvKW9HbwGDuCJJUAv9RGmtYfCWOakz7zcTr7U0XP_1Fqo1a6DtqYUX6MZiI6lY0Wj0R7-JAdncZeXMgj2lJhBfAdZqUlak1PHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHbIrItQdxBHTlmbj1QANWDCtGJA08DHdXfOVx7WgsjqfWnz8_0-DEcPWggkQwY7HxoSLqigb8XeEAkxfpgRzMLmQ8DUQY3RtboUpo-sm_AJVPgHzQDneBCHWjOr0QFe4zTkYKrRBDkTOh_RjuMi_ikBVwYHPV7nnZ32YeHnhZOFI9LeI4QolbqiuXnuZFarvuN_nJABX6E_7fFwUV1065k06yLMjd86dtQ7J3dX2gwrUOKZdiwMGSfHUPmb08V3cYqeZ5bJKxuyrlYympgbRA3umsmC-I6o_0u32JXsPCXUFjRolcL_Cndv_c9T4IWNyHT8wmjk1Hwss2RuCTwaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHptaOlkYd5oQ_o0HgE-f2qTz1LcwoRAvrCgUyH_kPTBrj8v1eUFdA0IeJX_ApgUX4m1DLE9Hb9PuPBA4hr15iSoHr5IC5koeUzSOpEpbay0brCnSAkA1qFpqb3LTghKdra07EJMNKFh442Hq3axpvWmSmFUjh00E4TUiyhlQJxwI9dJqymwF-boePGN0okn_hZX34g4uLtGEyU783SxmhxRAFSIGEpB2ulGxCs_bZ2vUmQOeAr3R_o0nzWDmuMXSHAEfZmuepDTG6GJramD5zQ987x7KY0a68damY5OMZzwy0xU0SKC-JcCaYluK7XmxDC916Pjz0UiWpEQ911Giw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmDWNwlcY5pE6PjMsHSsJXoz-9XJKQAWiB_1Nj9_xA-TBUkLZ7xex5CrMPe_aL4qpKrHd6u5ptQbWLndj4SLbTTkeLTMv8z3lyi6Z58hIpSJ1eRSeXthyVhOoJ3RLfuDXjSkvosO57rSUDhr35i9RtowGLYUbixskDAV2AGUFHCIC1p66nhQjSMD86SBYC-n4L67To5qraV9kbJ5axgqDm7rFKaz-fmi-Llm4MR8wX5t_75o413UETUKHval3ZGTNt3oP8WNvDsZPZgu6aJkbGcONYcYNm20S6ofTG1LebIXEgQSaNnf81l4zDfNsEPCzm-p2a_1x_Am0GuoVO-WUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPKSm57ynki01rPy-OE3P7lKFCVF0bfermE8hyEhe13kMjEnNxTPymBHlCJ2NlXqRBEN_j9Y7ZqTy-Vddljm9BjLhenbAM_18XcrE81VQTP3rmolNO5FOJPJTDhh3YC7lEAuvhPExB0ZLPorlPJpfJHqe5bORt7ixxgbLrmUBogl2IbCRttPaVg3_QdbJcvOLB36wE5eSrzK0s-neTaKXt4mhVk0wberlskLRVz29JboeszrVsYbDcTAOF_MRNKFQbtJDTY4InewCqGh2CNXaWDdW2m-GQYQvfXP1mBk40F7tjh6WImuxHY_b3XmLjV29H4CM-B_Ly0na2e0k5jxnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE8qTxCn9n7JbyGCNy_dtUlC9OutupsRJMyDvyZLR0-z0cPtV_urh17kaNnlNcTR6Zc58TnrTyIwvdPSQiZCdUJDWyE1O84-blvO3b0d8AzSaEMj4wEP9upraLTdNUTMp5sEddH8nUyO1NxhjuddF9pAKiawbqsVz-ntTsWM1d3E1W6vP9c60jN9hiwzSs0F_rj3GGAvAdSIhzIg8pmztmCMZZBVGAOdWkM_9g0YK5gYYUULK0QeyzVaIdLymcalHlhkp70I37A8z9ldmDRphyizW1aTYkLVd4V9jzqQlHhQTg4r0cA-7tPaZOWC0n8w0A9tAoUeIM7Gwfiz7oegLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrjTMFYcEX8MXBhJDbg5KeF9KS5UfV6juNvNCa2UVFjMxRRzDjKYkRmOoewicU-50zriqfGD9a1UivpQuFDVTtboy8VBnG9zIP7Bbwd7lZjfVFqL0wkQ8DQ0DyaayBWWGQhFInDK9rYiHMWRiA5YMDWnCbKrkF4nXSBT7lmptCwsQEX8N6h6IvX43SOcQbN2IQFeFRJ4AifA2icXtGarOmPrzZ0hrOyeyVifSBtdVJOShn-Xc1MeD-8LHndZMiwdpg1CPj-s97vpnjbPm6eqltSL-Mn9J8Jm8vm8NbwWWMC_KYiqvlgCXuAh5Zh9RSb-CJA0Dzc6u1B29RjqdIuv7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA9Ky0G_aRXZEV6uv60jTBze48pB5usZ66h3yKukjxw9JFH3OEc_1ilbA1kYpww0q4mQYuGS4IK1_nUk-5Ox8pWWFyfaP0XePdt8D00MzchpKGxCEiSRmu29AvYwWqs_G0pA1jPpkyxmfICipho9d5n7iyL6InWL6ICIVHukqaOePynpaa8Xx3uWpmr-xF7qClOwQCdRrpglShS6cxa0Bt-M9nqg-B_IJj8qsmi9J5l6BqzmclS2mpHxhyUqdsFefR_2IrVcHh-G2R90u8DVmPjtGc_PdxzC4ivejsSHFcpWjMYP-sAVAodu8_CYU3CffPQMriaZ5ltYqZAPjENSGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz7PKuu_3zNLRV8LyTwFqyikwkhTufbJ2zshNe0zT-Od7BRKfJxi07NmPororfDtS_tB0Augd4U1dK421AJk4djEp69J8-PVsot1OA4zwPE9s6x2qnIlK0f0cjXaNEpOSRe5SUQD1zMu1G4ifJLZ5gIMsFgN95gXloZTa9-odvvWcwDuwcgFjroLrioKFaEODCl947mYWBn-g8pRGjAG_fN-7SzdWSfQJQVdRJk-YWTP7M2mYnJZjUBR5_Q5gWRmHqCNKNpUoXAjPXwRYX6Idk97pKq2HxxEN1OgEuRm7mMCqG_PwCabDfIoZ4VVVpffctpCD0TtRkKexDCvsCPHVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz6tzAnm3ufBJaYz7JNfTNGReB00Z2OUS3LvbwxnOOUkeXRSoxNv9UvvJsimrDb5C0nAS1GsOstWWwY9o45wHPlFLVm-X6Afxt0qZu1x6M4phCLf1wfUUtZVheK1Fc-QxNiZVQEbbOQmYdV-wCHh_GDPoHZa2DH1f7uuwixyATiT00xYCQ0nZUsAK5bl1slx2WEdaaVCc8LZPTf_56poAuhRa2AtCz3UewmQDSUx6LVW_zUFTMLQtjE3teIzLOPRdnv260HTYfnZLB3cnhz3ytD7rgi7ahfBJYG9sIy9R7tQrMNgUyMSCdvGQ6wwXMEdijU0A_5UHyz44tpSuQgNtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHmP7-IPCmNCqYB4g71DNH0Ig9syuWiEmEQfrINw6CKhwV8PnnvTcofoxXhEfEM0L1jKR1Hp6Kt_4su5eh8FdzXmFpKvmPN777sNORBI_NiJB6RoODhdFtwZjPiFnKlyO_5ISuB06rrufK3XpeUMtQsLfsuf_cBL0IyYo4XvnAV2f6lIeNq75AVtQf-BbFekkLeV3oBXQ3GjGGIefNFD-pLQhjU2uPxum5reDtKMP8IRJIUyk-fbSAS8NQNPkF9n8SnRvtzpcug8gKzk6rTy1N9CUoqcXbcbNPEMSygOAL96sAWFns_7LjOu85fEiBb01E2aGSFye5oyJgLxeDHO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIYQ5WTgk_MB2MJjj9vkn_tW8Aa_fCoQgnAKyB0lIYibNIglZEs35E1YLOLOmqJ5Qd_7QgZDi3OnQdL1Z6ersoAm8F-cBp-sKVMX_1UBecCiLcCFrYTQOykoWfVXq6GBXrbUjBU5cFX1WKI1VmMx5DTYzLziGKrV9AS09p9q8-0zRhAE1SaJj7pifV4wVjBH0yyAQ7NTuflKUqcdMN-641EqYUUTIkT-eX05tj8aPd_xy4mpYGQCsaKlB9lrHA87WU9UanKfqrZpS_nPJ38S4tqYbGwCv1ngV7P9A23soDH2tJMX12mOOT4MqXr3mi-XGgkJmKSPT3FwmPju8oE1bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FANExERufMOa2or0WhBpczwGvJ_ByqEBHWzw8v3jbY_48lKcDrd57SFSQoPO2EC68bsbH8EjecPXs0mnaiZJN4H2N_LQkWWmmX0T40z9IhVwLGyYHUcsQ1TIxayGoQjskF2jwf9CRvw4YmNW9VS2Ar8BA3Ab39rnZ5wNkVCVWTw5jx88FQADoyyX5ap0Y27laSLGZrMs_5Tndv4phuofux2oZyjrB6EkFIMiHds3MmLZZtUyUIsHPfFg7I9dSf9GIrtyhGl2kCAg5sHCtKthcJA0jg6FOsoUWjRIGLLOESuwlOH6sL9TJ7Aw5iqHDcHSNBYjqQZHSQiDdcmF8emFyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk0mB_oBunL6bVbGdgvROzAoZmAfKxMiugyTXz48oYZm9zE-RBq64KPkzC4uLM0PVMyMTtrixvs0LDc9QihZvwKLlR66BPGcjckE9cAUqX3s5AJP5yxwq1EOhlsRkGNTRE74zPV9JJNVLM9t-1GOdRNzg8ppR7n_9jN28tedkhB3-bw_KUe63i2rQpG4TJHr5lQdogCZvTmf5Z28rEXoHSo1PeJdVQIBh9wmWf5ykOJpDMnba1ebpUopPZyBaYptZuCJfUsD4qAhyhW-eOht7AJiLXszdvyGTYrPE14WuMKet_NOtALK090J-wsWpzaTsJCUuWJoISzfKcZQl1pzLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCinqXMAWP1beJbFnNh1Ypq2hPXBtFBPWGnS-eho1T0EF68-9NpAUV9nQBOgAP9XsaWl_kliYsasuh1NMUTGyieVPPm09JwkRhWR__pusqjYXZoDg_OSBufkFXMDqexOzJXLcv0SMSfD-JrNpjoLt71uvrohuMLdx6tJrO88fX1rwy6Ym9Xju8Ypp1kZoZ-oSOX_DezLggfS4BvBmTJKe5i9Gs_gFL4UK3wulRMLkiZwXF7NxopfvenSx2OL5IvhteIm-AByqB_9-x4RjG_OvxsIwQFQ4HCGbmog32KfXf8_3yUXnYnGpdwuK-7V0oKX_qTi5UBEIGw_ofpKKOHp4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPcKXHlRSK4sWlFXjEgj0bTWerylwRHkvdChEA1Xwfn77YJ5XUIE4yinQkelo7cmMFGKkYUDzNXFF7CbxBtGJ-_-WnrCSI8g_DgYR5lNOMZXUPjq8xo0u7OviBvd4tfQhDWvgMgl3MujO3O8ucKs3DtOveiHwdiNFsQW4P4OQlM-mBeiZ90bLRsl11FqLKHSz1UZgAwcTgJ1oHWf3o2Y23sqkwXrNE-M6Zp7cawYN2M5P3bNnu5klczPzJ5JEcIcGqR-5VkTRvUHoz-zbh7V6PQZ7gWYsfSaFLkMPbnzqAUuo--ndIXDTbUhFOGfDVD0mY97e_FqYArDjbs988I5tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouUF8ms1D39ZKXXkz8ySx-PyiA2Af5HlI-A94Ht3Bs-yMUlKfR873JIgCoKCvUFZuf-Ms_gyOwYqUzdEhnL84ZdpjEpdbRUkpalgmD0U7-JQIRVNsIijNr9BzGj5lgRttBllrdIX6umXTa8gFEa6g85N01DXJv5jaN2Usg4wtpU9UABcYl3iOUWSQp3VZv6vatarVWhSQKpLbMQq0tg3zOXPFtjP0WU9rrAAfRoic525RmVauQ6HJtB5TKnQJnloCllTHWuG_owGQx3uLPWZ7l4fj2Utr_MhZ5c_RjWFp-ZuetYRrXwshaZ0huViRqyOYQiLtBuGw91NTHjg4HdlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdL1GS32HmAl5T1mTabmtf9cmdgT1Y_3WyB7xC7LSHYuvJYrbGQmwTTs3_lOCXpub9BKjJsMTKv02iJ9vZJjw8Hj6kEjI_UDCMwWAiN5WewptCOZZm1yVLy1ZfIaMlUVHHNhnSYN-vJqHvuRzOghfPoeLwKnZt9Q6amE0OyER7jpXCEPYFTP25dHN8ukUtISMlt513JcBLPEeMSghbiU6Qme_XpaQOK-gvA0xilcbVxS03c3y4xIw-nauwWm5S4wxA3iZole3CXCXzuXl08axj5aWIz2Jqo45eTSzwZzJKTqblwQDUwlQ8gTtpdJoDSuzI-hTBaNCQGM_E0PnyoRDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfE7U8qi40QeMNzFM-YjCosLDrvp482x465SncjQBG_aGlIe7e9UGHOVxTOEkPlUtefCxLctETB7gnvqTewAq2nT0c65aTOZ-cWEX5_HUGqhESLjTPQ2L_pJ799cDZlOaDDpawBXrcD0Cqm3aoeG_LttT0xd3fklGs4JYnUVf-hBIZZpiAOisSVAwJWMB81qSoEpkXTY2REKMsiQfGD2-p1U_HC3Tl-IW9SC_lX_5ps_S5VaMc_Zf3kSzB_-dXPxPuk2u_frmbBTPbEuimcM5yZ1HDcAKOLVW7fEIwog1NczZUU_o12CaNJly-UALe5s1f8j1QvkGO0HKyWe5XDW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjr9tqrM9-9RyUUP8yE6L-MYEh4apot9m2zmrkjL_QPtRvc94X__gpyfNz5z-qq6JboJVrznqLmMAyvosL4zQURppMvs-2UdPL1OPsfvRKAWCzJ7MCgcobdu59UANvsKjVtzBOZ3wAWpONlWRttBRLN25-Kn4Xzl_nOGF1E5qlugSmbrfPdAKZntkjn27TAhF4G1JIFjJoPxnlG6aKfGkgCmvgu52GExRgbwnffV3vTIXcPYpbDBMCsig0zmnJyyHosSeWxLBSOSAOZlM6fvqwwgfKM-VAus314SDTfMyBp5Dg_S0wMnJjwqCpp8WnUtg6WDyXVLDDid08sVeTc2Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhpyveBW_1WcmYDzcFYQ94AgY6HMKWlwIae0XaXILqVGnBthOX7UpCqaeKUx9enlvGJ9-vWM5yFCcuugh2Qa16GbSS2Q6dHPMAoDQL8848rRYz2Wc5yW2NAZhYyATMFBztcmycu8eBxAj_cotd7ZgcZ3vPr6Zb49e458dnBjIfkKtwlMzn1WACKHTkaoZcnr2UeSmLA2NV26eCygSELblLDfv3dDEmDxkA3A22awkW5H4yMKmzQ9Wnua8mY-5ye1nhMsQ_971KaRCJfSVuzHY_AwX_6ogsZsIwnGkhokbmC9UQn6UpvPuiCFIERPA662ZRV6SX2xU-12_hsJ0ueQsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0paHPL7Fd06vM95dY8QaGxVX-LfFZCRkLYuxaNLIIiB2dIBrlE8j-jN_OkWCaeeHZEF5XPL222MjxmhxaPD_apY3OCOfaCJlmcAd6Ni_8TrRxuJZ38-Df0HRi2GSQPROWVn0daYKIDdZMKcKMPGXFlS7NccQxUhwKQ7pJXxlx4J18W4ZhnTx12GCcAtmNDGjNwkpE-cTKaj3c4hfnpka5cXFLhQXIoo9p-RAGVaMGkVzqYx54yUZLtnW3n3t8FwF9HYbQhaiha8rrsjCOgypaPR92M_vvU0KKck-Fj63B9rx0SYN6LWsjpOLdFGrNwhetlPxWS1hFag50KwTZ__Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMQAmxRuph1IXpFzv_w1AlJGQjhiBeNpeCoObRwPjcnOkirEgdL3UNkf6dCFGSjmBdpJZ_is5VAwQ6vySeyWW-UaxZuU2QpRoykAphuypqHu4lKOSGRGHBrc3leqqySnWC011O-FoA_QFFY7qQi1uXyJMlUHeqHGFlKMuZLTmmdXIQUKOgC0i6sAB40iOYot_RQ1XncShYRs6mS40bRQ6I_0gQDuK4Bq_LnujvvuG-PUIQS0GfhFyQIMnJK-pDhUXuxfaY8DLxAVbO7Mt6E0CQyDm9rB5LkYGxC5f51Swhmv2XJwE50povtwuxJD2u_QuIcJNZhUi5xPWo6yObKEIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVKK1vEZRxcgMVu9EAGfYGgyJkW4gy6mOQODDAG6Qj2LPDZ0gZk2Yka_hN3DvTXCzFJvEim2bsLM67O1yqmRZzW6gC6VJQilLRFhbEE2Bz9-86j4PJx3KyKrZWijvBAacrTUQBcDAbYZXjwMMSBF3DrMlWjUwhp5Q0tLXWbLCajPZSPH5icdlpWA68wVFsrSo9ylbbTCWSg90Bgv_gXA9TZwlL4HUuR0aGtv6nYAquDy9OgjRd8JcvtkdDIqmvkbu7nU1X_hEL1igCwHEHxW2ykd46bGDOwDhAmus4e6WUGxnk5Vavi1tdBqPtZ1G24fx0gNmJNe5H-I5Uu5OKp6Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvdP0NXksQy4SUgAUdtjYGue25t1FrOps6TsjotLvhPbJLEsJ_X5lU21-ukxdM0ERBdXSuyIiGelq-VZl4WjJA_l7oyzDtOaEok6micQcAnMUgUw7-G50_Ii5h-pWihvv9BOPI2rgrJNK2Bdk72uw0H2I_TqSNFR911vyr5nZCQ22ZEYF8bxFWp7qx7t5j8bkznkn3OZbEeUEjboT5LYCAbGSe0L7ZjdaQxm_Lv2ZfSO9BEmtw3ZvWE6qCM41NP-heLwOUbS6KSh5KbczdhJqg6QSEcZopxFfqH8L9dnlTHebB11Hl3JM_r9l4HTcSCOurFRvV6sGJYQDU2wnHsdKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQwvTTS0xirDECE0wIZcTg83zqePBkrz15C30DLgi-XQmn51g9VNXHDwmQFvoYyueOwvyiQt3B1uDfb0S2UCJJxrjQVWNuizq3oyjrf9mSRGw7Zxucj9Id3GPKZavlTp7FuPzBXvxtU9LZO94_zx1RFSMfAm-IdypdYMsAqObDP9tr9MMwek9tRvAoTgymdZ9ztAGcwxZv2MjtANGKE8emB26oC9XZvWjGfnn0O1BJlKVbOPw-hmkifdD72mV549FeBnCN4A5tu4HBrv7RTOH9vt2LH7IDgcTNQfz8C9LVSSoxpprhTGbQdThxeA6RmMNr2er7q3TJO_ZuCEfQI8Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T38DtnMQm1TuAwTyq27Aiq1WxUf_zMFrnjw5qxZd2yp2zXtFMi29T99YQfYQ5iYx0JHQCKzWSHmXc9JXNF-5zxgh9ACpTgGbLQgFTl64jmvVHn3BtiDhv9j1q40hDfTuwlyz8R5XZyIBJLtQXWHL-MX1fVnaumHHE_GedclWWa0zTjTyH8q4ZcUJFZGkD4CRa7_EvKrrFzCVvVUuMOYB_7XRUFG9C1-a0ysaBSg1nA61d3LW97K7YvNsTspxZTd7eareaUuuz1a2r-gnZWygJA1_EaNurW0E3OymUrra0RybVy2n9elCLudnCy9JM6aiSszoppKQZeHnhUDQidk-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Byyci67mB65hZhPTBS9_qiNnzJeH61j_RmXTUeIh7jc8D73bsmrFHXpOR3clN8uJgBYJl8PNj5kgQiFsLGEARtVH4oqDB7aRRKp_mFOECLc4lKeg-6fvjnstNOgi0UH5Qttjew71gT2mesNPHVcY6dOgZlu7widPWYKmQzhcDXhNrDA4IO6SRCuJZAOESjz6lgfNSVnIgIB2_M2JgJKsCGnqP6yGICprZ3Dlh7FkHNrAwX1T2Kc9c1JBfx_RNAUXekCVuPhx4_iP6Wg6M28G8LwJho8Bg1MH9soM3WExDtYXK8OBVcXKd06goXgWYPwC7QwSY7g5yDaaby7nLbri4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stxo2f_GORq1EzVeiK5Qh6sZiccOIKAvR0OTO-ZckEsYbBIMrnynNvXFjCSFl514m3x9dxl-PlYoNYQv229xmiyHHnTaDQCpwoPh3_1k8Kbp0FTM-jiAKTTP6KionZLSr-Xlap0C6zZvQm2Dtlbr1SYtgBYfy1aUY1-XWtJdYeWvwJ7t5i5zkedjr1wvYA8vEL37xWUhUxhngTooHPiKiU81yikeozZoBi232-fVDneXkNebKf8ePNahk0JOFayOf_hPgvGAxT7COaaCr9X6YmCmGL0C2TPQp_9FdXr9lBiw0lJuTlx3Tan4KuDxZxEsllZWlSfRI8lOlZgZxFWJXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTXDoYWFMkwZQHflV2mGzC9zWvT8D5JhK4RIxDnriY4eHkk1EXUlryppHOsCHYPN95n54XCLrqSfdbxkSodV1kk1I96u4IrU3-4igkPaD1gh8PDRhQTKRa6NSfonizVQKgD5s-39s1D-GkVU_NGvxZu9V3HLJyg59jnfb2tWWbhnr7UO5Iw1ZzHZh301Z3oygY4oVghr6uzEjOfhgHdZCiy_lvRZAYWjnomqiSB0GLFogMu5MzKvjLwPciBTZFABCdRpYnyT-a8t4GEVHNUHgdUjfDKyH3Gr_GCC8sCZ7Sn5bMzPq51zxPk23XZJTzJxi5qOaKTaxdmC8rlffKWenQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ycyrih649HjqJ_jxPjB1yqccx4slcW4SkH8yrvrGYI3CpCuD-Dmxtf8yN-04JWsn1nFZDYE7Y_nsNTwks2fH1uzVPwLCLHubcsiMkQTj0PYZZURs12V0kHI4I8O4lbbtrg1_ZpIXgRfTIurue5Un08T7kx0zFjYWX9RkWx3awCf_oxrgS-nuMJ8rjORznQsoWDt8VedALGBw6aVH6wc6NmOuIlqsqvKPTmk7MdsCtNhetWTe1dQ5iuXtll52fziE-0DU55ULMObPqwjvJL4ZbxTEoXScJhsoOGeeE9-8SaOu5EScE2zBDhVIeg6v1FW4lSyN_dZnc8OIDj92SXMaew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nceR71INXOI8Y7TEGNcmMRv-NymxNkHsxFnsU3OLmNo--lDscQZ8EsteXQaVr-Z6EH_J3eIeVUIl9zzg1wczXoNQDD6h1PG-FwLywzkzrKgd9shk4q3aRb4QvRUxIpnJrx86hQQ_KDDMg_0j6XGJ9O7vbar-tLyAaaN5J9sDGkZuphIzjxDfQ23VL0tceD01-VXfbkxQY9h7wY7aGt6nW8LZjkpD4givaf02-O0_dFMHtyVbgYCvGojDf-7Pz8Q9X8uqlZ5Yi5Qo9mKFLmRJVt6QnjYFzJIa1Tbd4jlywAf8aBLHBA4AbWTRqLgNEEWLz7BvX3Wu69YlU2HXyBu_cg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Hpg6fumJnvxo8YQe0oz43rfodA4QPTtcSw8lDg40YgMsMoTJ7V62rpx3sLntbqcbdbZKNB7m7CkCYOTC64q4frT26ezyqxBToKujiTrIMHEFZC1r3rvXAGVycwM1Pv7rJwAP1b1VzSmJPNcUSX8yXebelRRwo0xfnad8zNUza21uQlmTLcPPJSYak70KLsFpbk6HRQywA1glMq7YLP280REvzwOs-hxixjwDWNxD-KW0bzY_UhHcgC-m5KFCTaIhGLJRB-JGVCpVrHBX4oJ2VKRB2mwT1UAE37opF9mJNm4X38w-0_x_yMJoyz3bzNP1hQIRDmdQHZmBwSqitDn0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Hpg6fumJnvxo8YQe0oz43rfodA4QPTtcSw8lDg40YgMsMoTJ7V62rpx3sLntbqcbdbZKNB7m7CkCYOTC64q4frT26ezyqxBToKujiTrIMHEFZC1r3rvXAGVycwM1Pv7rJwAP1b1VzSmJPNcUSX8yXebelRRwo0xfnad8zNUza21uQlmTLcPPJSYak70KLsFpbk6HRQywA1glMq7YLP280REvzwOs-hxixjwDWNxD-KW0bzY_UhHcgC-m5KFCTaIhGLJRB-JGVCpVrHBX4oJ2VKRB2mwT1UAE37opF9mJNm4X38w-0_x_yMJoyz3bzNP1hQIRDmdQHZmBwSqitDn0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmzOlUWT7LHLPAG2dGW-i2rNjojC5rUghmkCpzPcqarjs5KRDvzvL9I78ikhFUs_sxGPn0NLRenTRGGMFRasjc1ie0jDPSZrXiqlVeEUFIrrfIah7KMASQNQhg5swc8WbNHTeQfovlJsoUa9kH1fdk5TkkPjRXx1UFccYRdlb-EOJJCFVEaexkI4CNP5HvMq8RBCmGDr_VgLP2Qa9azZgs0TlDAkArQMlx1Sr0zc8bHJ2C22wdRJSES5hpLgkCCXaFx_iY9f-v-a8hl7oNkDQaxcM0_kMck__R1s4ArdU7naKtglB53oQpEcHs6X0JB57oGYInWvXNASzLH4Hn7jKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O65TsWKzNrySMPhDMoCSiScncqKa_FfpoEVgdHygvUZJ3fmKBdil7zLdqpsbX_wfob8De2EnFCDVQAEL-d-kbP8rmpq7vrQxjFBLUIG_0BY7mm3Xp5J3hugNbAQ36Jm1EtfatwqbMo5hoZCgrvQzSBLkBBp9ONRaOTVwhO20UY-v0QKnQ-I1oRh3WLVW9IXxWtyCRkbWx0dHEovLJWeoB22cVvn3S7DVCXoU0Wolss5JamxbjkOAbh7Cyp9j2u4lhFwlgnrSOnLnpFML5tS6JL0UHHuymOGgseKk_p55feszumsD-waFPcJYGM9Sm4E6k2oUlFH8-VfSJPQ9MnM4Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFleTQpkJ44RZ5QaRyh49XBgyU5oEIOwugpp4y6ocIAyvBk-HP5XvTEnHcI1_p107qw6vK7rjYiqLfVrs4QacpaTh0d0MWYT30P86BbAXfyi6NFdr-OmZ-NR1rIvmmMWDnWDhO86HkrzGtTXq6gzA8Ngbs8thgimnXgQjJCflIfMKit6CHfEC7kEq0Gr2QizV_pf4V8b1reeNK8zNjTbWXvnw9f2Thckx7klutEfteqWoPyiYA6pXeJaHuahb5IAkRyziUbZs5dG54he2_jHJKjYS51GNfARUIiXpPx3B-Zf-jQnEw2R7RTfJiLkPvzqp5dhwpCSbY6CNVnMUKmuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUQVdYjpXb9tZ3WYgearzoVMhZ1zizvAawOianp2YhZXstAh7U854-w8ZJxtZZ7KYzcAfM_Jk5pJ1smU7hJsjfysMeZTb_QVgWrJWOzPuEZ2-EcG3WXtS7AicWEZMzz-wyA_ZrGmnCgqCQAcP9NNlSBmIkT2PQEycSdAdWd34BlB69c8Ugkj4CCO3pe27tDSkoxaPlJqAW_pT9XWAs7lR6jdqyA1Wxi9E1qqggnmhZ7_e2q14EXT2qAS_yYvP-X46eZsHEhs4bc7Q5i56xDFvarWDoxUInKfTeoCITKPWun_KQ9m2vAjwrngrnCpDepyQz6w8u-6yD2Tjv97dxTMIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAE14aPnexqCLtXiwmVLBlr8NGVPTaYdYM4voXc64rQmtH-Jl8zg_M2WdZ1xQz8Zvq31OYJjReK-6He6aq4LTf5oAGJDXj4b16bFH0Dirhl2IQuMfjFfh1HmG-tjHxdexFHJyb4ZHnQ5fGaCzKBHvWxiXSX09gcSXDhpHCq2jBXv_SIpsq2gFubePuXnFwG_FcEbKhFWfewe97osXEbyjDwyw9S8xbRQ_qjvNq1N9T9A-VJ5t48MdZZLmRtHooAf0w_TosA8PDcfrXWJHXuDs8EpTVL0Jzut8mgxFupB5FLwW00lwGIqY8v4Kg-zVAUSUla2rBh5_64gHLZ240dgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAMV3eRgCvyQWxDS-uaQXZx96Q4Rs1MidypmFIAFb3rluI9XpgY1sJ-66H25X6M3ael8sTt2wY8ljS99i7zHMxhZ9juzLSQyANc5BTmRziqKB9HZdqinymr1KaQN16FaKW92UHTxRzegFr8TcXK37pK9FT4W_Q5ygYcxWhHy-Pbg6NkipYueZb__pHExDHKKhFVexIc7HL7VH7cYXHCYVTkl5VM4wY-hs_CUfs-0MFtJtvlP3MFbnobWTRBhZk8L6PIWBU0dDxG3Zb4f2XYAfvlNcjAtZeHjOffZWpd3-syGfduknQKJSU0dip0ly-0DjNK4vID3cfuTikFC09KuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKCltD5gjpNvpQc7cWJzsdvNvFfnyn6WukN_QbcjKVRZe9hxGa_DERhG5eFbfaM1aQvK5F1RDcoZArVvrg2zDI7yEHqK8tEDiHTybo8BvCFK3MevWCflb-w09RSVdtbhxrTAZIOUoRXiFm1b--WB51zWGYJQrPqy8oARGENHoCHhKrQduFjhUvk-1cPrfQ5ek7th9yE3KFCkRk5k0I0dCmmP9myfOTEOV1a24wAxrc5QgYHx0GW5Ys1dCF7H76VHZShOF6dZG8ZEEZ8Pj9l-UK93D_oxxRiXH343VUnMfgLLgUJOxzKLSPNdcDNeYTi6GJaWgI9d6VMOiReE4YLKXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=FJa844vS9cs_gpiEeMMwQk1gXflR6aLZwkopa_HL2GHDgpsbH5YeIQ4ORONYrBKCpFbXBHAFi-QKTzaJ1Mg2HPNrZhYMpXL-SBXY3uiSjgjTU87AHhfvFCNLQZVVQACoUvNyUWf-sLSrOtvx5kZ2zM_BnOn40aT6CgfOzZ9kjofoNPsi86Ogy4YbMKv_bLp8GdUu-wLa_SxK_YG4oFlxhOPzM5kMmmWoEtqOMBmXvtRQKk27OMZ-HJqI3SAFFHscrqdfKB5Q5wuu-yx0dEkmmbSoZaPkn31untpRJk2PmyETcVFWoXT3DdOD6NbxDG0TLAKpwfupnKQJ-oz4T-QIu79L7syLRuC0l5T0lPjnKe3fCAc54Sw5h-x2syIt9Ll6hwBJ_qxlZ7qcgo8mZt2KxagbxdpZAn7WGPqbMr9Uy2fBwThe0QAWm0_xUyj1qjlFOnXjBhay-0QZciOLMAT7SLM32npv4QagnaodxhdunORKHnhOwOe71EB1oazi89as_62b9pBKL_eJTgKfq6cuT0pwgfDQRPRM9HqNt0Y4PJ4oDLj2SayedTTwEbj_M2EvkZO-M4PR-1rAvCW-DhAmH6QCGwocoGzisIcGKVlft5Jmr4bcr5G2jLvIEXvin0H3ck7puW1a6J455OLwTyp8xX4mvdQKsmVMtZEbgEYypKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=FJa844vS9cs_gpiEeMMwQk1gXflR6aLZwkopa_HL2GHDgpsbH5YeIQ4ORONYrBKCpFbXBHAFi-QKTzaJ1Mg2HPNrZhYMpXL-SBXY3uiSjgjTU87AHhfvFCNLQZVVQACoUvNyUWf-sLSrOtvx5kZ2zM_BnOn40aT6CgfOzZ9kjofoNPsi86Ogy4YbMKv_bLp8GdUu-wLa_SxK_YG4oFlxhOPzM5kMmmWoEtqOMBmXvtRQKk27OMZ-HJqI3SAFFHscrqdfKB5Q5wuu-yx0dEkmmbSoZaPkn31untpRJk2PmyETcVFWoXT3DdOD6NbxDG0TLAKpwfupnKQJ-oz4T-QIu79L7syLRuC0l5T0lPjnKe3fCAc54Sw5h-x2syIt9Ll6hwBJ_qxlZ7qcgo8mZt2KxagbxdpZAn7WGPqbMr9Uy2fBwThe0QAWm0_xUyj1qjlFOnXjBhay-0QZciOLMAT7SLM32npv4QagnaodxhdunORKHnhOwOe71EB1oazi89as_62b9pBKL_eJTgKfq6cuT0pwgfDQRPRM9HqNt0Y4PJ4oDLj2SayedTTwEbj_M2EvkZO-M4PR-1rAvCW-DhAmH6QCGwocoGzisIcGKVlft5Jmr4bcr5G2jLvIEXvin0H3ck7puW1a6J455OLwTyp8xX4mvdQKsmVMtZEbgEYypKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSt3LIoJMQc26OkKxkOUPfixYXBCT_Hq-XnRoq-XJFG_80_xppWA2bUp7FCq8ux5AFF070_yv_Vl13qJlqm1pBwq-PHXEGPstPoNAm9m91sls2RiWyG8mif2ncu8Ij_X6Pjb-gPULORpRQBQGokU50YdAzlO_UrO5k1yiOn-l152AbO33BTiRfuNubNCF4QT7FZmWr3AqO8AXU8M9mgHP-sXrqVSJdPbaPLWP2Aa8_L-TqmdXoayV8TE8-zpjQR-WS5frvfR7LTKf3keqn8rVYrpgWFHsL-lCVUtr6hOIuvMT842AIq7jFaUwFf4XHEFMva80FgxSV7yhXQnsiZ79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8QRNl3p5T5SMrMSvyN96SvCfevkC1wYprPa7B_-l2a4Zb2qX8uh2796aEPx-1OCU7hP3_YUO2lZRFSh9y1ZaUeD6MGSZb7z3fPf3AqcfgZnqGV1Qk6PuMBlJEBKPDdp1ClJG2rhgfep2yH9sd5syOoHSl_pKebX8FKNxmTvhXkIJDHMI5mRxz2NnSZ53PExtpI40gIlS6UhMwd-8-6bu9r7Y65mc602turD2PwIlG5fEaxUyNswKpBwgP7QlGY4ICKFCvJGpp9jXf77iEBZJunad3m_cnB5RLXpWXF0Yq3PjEzIyGVB2fhv1Jt6LEYJCCTyfU1wNy2wG7i3c2_FgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUftY6rg9TtV7StOzhd9-5bnC4anYCDLxvmfYb399r9ILfYZBah-uOK8i_JtX3t4WTxTIYL6Z7JKAxGLgVaFW2eZu600U0AViC_TS69SnqsTZVLPliTWwQViDZVyCmXX1i7LDwxK72APomEoVjpTt-fUAfrnTEErjqUlr9ShBxgmrI3v03vppgauQu8EQXaswi9mqm9O4YzhbWk_RPXMWwA6MhPEba9JwwfAFi5S5a_p1bAlpqF0Qtd-WwONPOyn4qR2xXP8iulSRu7NXqFrb44FfcnyyvRN5He7hiALC7SYH6AjHTHV84q-lEROV-vxk5RtVE5VM9pbrG6lN0gL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDpm4Qac7M1A1bc0Rf4RZzS8fdCGAxsollzCvQKZrPALbVlu-gpEgok_BmtkNvcBg_QUNAD-W8I1zN1yIZeyOyqDrjLhAjHSrJozXv9kGNIy--t_DzTuFGR_P3SeSWfuTgUpztMeG_kjOVj4VeHvs_Qu48yPhZdMZiCUKlZpnmL4BNZW0UG2i9S1p0Cwi8Xrah69ra6oZdHYT-96Q-Rd073dT14TqT6fSpP-rNaRS4zJoXPENK86IhgFmwuWDDQTXwSxGWFz9VFGsRf3v7YMQQ32QT5waW71GPzwTtZ-a2dtmo5ZzrU_P0tCD0AwLfZJ67644Qf4TrQgo-0_Eg6jQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlPgcmpTJKNCoWfr9YI5el5SfcFsNvIdzCXdSOBKBLY6Cu3VcIRbdYqM_cplp7_pcjwg3x5ZAtPe_L-9js02swVISsg0_eagzlnm_dkjctNwHPLRN6jmC9PU91Sfu1Sf1UuD_Ht3rKeWqU8sS2O5LQjsiCoSrlkMy2MdgYVxSyuJSUV_V_7ouUwiKS1BocO8fr4WsWPNxYbqDWHb6wEN4wNYpIGjhqGqApBBC1OcXIAlHwb_lCUvw2oAhhkWZC0quK2Dj_orpJ9aqACwyBaYvR69S30KzBdU9ZEMusCxVS1Oi8cAgT26G9j0WV8DAmQsacnM9Fg58cU_69xNYliDbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QLYnrVq8FGLfH9iFO9qHFGEM7MoTxVofJC7z7ugQPUyqA4k__sxp3eE3KBFXow6rYA1LzdQCy-NKBZ16ab7RpvNqMCBo_fJ-WvTDq_IJKUFriWV8-YB2xwaxRyLOcKL7IlgtP2vaSec5BB3HH3bY7OyPkL53uEx833I-M-wKoiDrWyExBysletRxzncKz8JKB0ryw0qL29KlM2av90dUTEGHyxn92_dk8mNsJF4Zi6d87r7HGTfoLLiHE1ROojr7knYg2BFBUlojaUBZt7uBa5SrrZ_aBrhTKMZvFZb9x9o_HD5_XBndXdvolMyfeZRIUgfbLHLP3MMNfwbFkCDz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QLYnrVq8FGLfH9iFO9qHFGEM7MoTxVofJC7z7ugQPUyqA4k__sxp3eE3KBFXow6rYA1LzdQCy-NKBZ16ab7RpvNqMCBo_fJ-WvTDq_IJKUFriWV8-YB2xwaxRyLOcKL7IlgtP2vaSec5BB3HH3bY7OyPkL53uEx833I-M-wKoiDrWyExBysletRxzncKz8JKB0ryw0qL29KlM2av90dUTEGHyxn92_dk8mNsJF4Zi6d87r7HGTfoLLiHE1ROojr7knYg2BFBUlojaUBZt7uBa5SrrZ_aBrhTKMZvFZb9x9o_HD5_XBndXdvolMyfeZRIUgfbLHLP3MMNfwbFkCDz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFwjhvBs2gqBj8fdb2HZWwc-U48T_IqaoyWsrM7s8cqylBQNIMg0YvCuuW0pcGYt33PaTURZgjMwbwfnoeef_clGme384kk3ePwwidO2PT_R7GQiAaZQVxyop3WCsEzYfPLkg0NvIh0o9u6G5JExKJT4ZqjMkDIKcmmEK4zwigqYvDQqXrkHlAFADOcDt86hDie6WfkbFXd0FHMjKWvGWfOXPIz4gUZapImxvh3wC1M8NaB8v9uUreNjl60_vzfNoqlDY7NemCGR5j7gG52ef0VK8mucvEU54FdPc6GF7jJfWTRNYbZ8tEfLsp_Ai0TKs4WfvhlEoWL5eS96Tp97sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0zHEOh0VGvDQNxnBhv3kiLwjnWvsfBvmNDIjxkj9-XcHtMG54VgCl4KqZVu-qUKUZ7kHZ5tG0zEuaODyPbhV1AtSE_vJiNMKZzSXqSgrL8tuX77NlKyq-O0iNYnPLMjrLAmrFrR_8D87yJCggmbCn_yAq51fN7Mtawp1qu-6uvUk40QjbtXKlosqVdpBnv-4E9XVd_yah8CORygIFYf2UrUEjXqnBuHHqGfj_0d17JEuKaCxa8A7CnrN8ctV83df1wyLoFx7tBwp4b41AVdqTB8tprkhFIOE0OKZB5L5N4QelCHp75sjbr3gJp9jHXPCudldRgJ4SDO-JVLkG1qTg.jpg" alt="photo" loading="lazy"/></div>
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
