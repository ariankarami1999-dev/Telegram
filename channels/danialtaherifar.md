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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 02:16:58</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aprgGYzROiYm6hpNHsTlTsGk0XOyat8kuS_mmfwwgrmDiLRCKkMkjzX0xT-th6iJKHNsrHbR5wn-3p3KE6wFC6GQhBO_gljOJr1lLB3vL5MP453bLJ-L-T56tz3krQnip3oaYcZk2YTnx-p5NsCGttewXq-mkJ08061pRFMPBsWnDb7XymV-eKdV0Q5v8wv9hCCIW2HfpTkCeSW0WGVTMIaN23apULqvrkkNpX9GEelUB-EPorzsNqAqKh402XNfs2s50lh1L32jblmpmW2dy0_oC_F-moT6Vw1H2pwunMs_GADWTc00jEgAJ5uAK4YvlaMtXI7t6l3BTcN_bDHXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 151 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 398 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 553 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 569 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 601 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 791 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/canVxad_iOGZ1Er2SG4mrDhw7eWNTfIG8Df2oR_JQcbupccLTCtrTSd6yMQAJT6TzZekLyGVFvewvvoZ6PIOswgKglyQf-TSeSSj4EPLG7Bv0LVNSRQ8UT9mHgsxmu1e8cC17dqHdrIUbnEI9ahVAuIBRi7xky97tsqO4IwILLssAKaQgcsGp8Jm5ZnhonGlMwiqc-gPub9Fd5MaBl0TWKPQtqzI3tOB4lS9o7hSNvuEuToocIDFzw1bDNHDNVjmf_pZxS23O7Sy1kmPNbU9fPya7d4pDMqeM2poXFYCkeZSJvbz2Q2DzrC6CMZTsYZTs7kb_n3__OeXtmmItU77rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCeG67XkV7jW5E5OxN823ifTOM6u4d843Og1qFOPu7m7XoQjO9teXojv0-kxnqc7qsqrzIpFf3B6RPKzbPWMaxOveU9_0dpwI7stI0foVJLouPoYiVuw80oi_clye17exhJ_iP8kVE-r7aOiS3UhOLMqbjpZQT5HfrZqsd_wPcHeHwNdO84w6gfcmGmO0lI8-hGqrUECpzE72rpx_T0d9E3u_1Lce5mDwlDMVnjZBSJgdT96G2MZAxKR6lBBgX__eNdUCQKoDXbL1flYlF0yyap_5O72XtrAfuzot60kuqLf4I1GCxDTl9arHldiPj2DsxCxTAIj-myVyfbBhj_aLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZz-543yvTxjIi6_Cgqw10JUtPDiaKev_aeaIv6SwnE1Ntxzf8yuJghDtfFkBVHHZyAQB-sbaJNkDgXU8DMj9KfRQYCiPwAMWyLKw_TUAP_ewCHpJgqzeRWxiGx4ihKbba8kfKFnbiCVnK2CRq5DqHCmfIJK89V7MPWoz-FrYoyt4evAVqmCurxT0wXxp4bfvBiBEU0pU1tMWp8UmnZg5RTbHfEfbjM1GjIJbZMohNx_-txlXXbjIZSx15nAt-E1JpUCFW4Jq8E8fjnl0BPx8XKSlntxunq-qFUCN8I-DJy9WdEIW7ryh03DfaHObTfRHACBbvU719jO38AFXUnzNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxsnq1Unn_c1MOQiXTFo5Q3o7KyhE7VJB1EwpGi2KqgSCUqN0NbzyoHJGEawVWJXa2XSnlZIbkpMUKnpOMDUHB8LPSRP4z9M_nBqTJo_4Kj3fsp5E0-wtq1CDqPCaCcmpMYU68_AERsH4byfvLSIOMZJrQxMiar85GggNPr7dhFvOrPG3oIfck9rhGP59z5AdAsVjqJbZkKKIy9yT-20VfBLGqwfeHrjC9dBLMFu8icc-Y11xGlh-9oJR-cw5Lg025PNatSenqldJSsyNjAd3a4PK3hzFzNHT57NwQOj_il8qZx1kOMNa-s_ufCqsmHATLuc6-FEdmTHoMpTU7dR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6td3RbFTXR2QOjfUXceqhhuT6UwJfsAPKz6jh_K9BhtV-xMPmK78XOEcTggXIYCgKWB0VFSHxWyuzl6aZvMLXRKyNKDd8wFsjVTDW9BoAzQHbxqTsOR6o3T0MGiBgOpglIZHcWwucbJPrKhcEHZYMDamluyDgDHVHMbWxfcWRvJ3otn-wDr2R9cDMxzOrpY40m8c-Y88-p0c5dErh1UnPkvaJYkZBKk5QDcpGleShUb9kuwGeVWN0OdmCSltfgjAl_uvzFPdmWhF9KuL-yhB_ygbREFOo25v4QAdVeakP53TqNNRsY4XNzdpB9eH7SQcqajkbaJkHQPOJnOZLaKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwvcjmukBOl_Pa-jHqa5edw2h1dAjBwSQ5w_I0CUCJmRgLePrA-FuuUSU3XDqNtaaG5-WkJVrYJFzp-L2cwypI79r6bBYtzXVfSZfZhLBCkg0WXRvbR3pSZBiPYAztQxbbiNHKuqWq3S-NRWvSFXU0je42mIibjF8idAAR-6U7dhcfmihxZxJF9BxbyY26Z-2Cen-1Nu9SJxiG5LAdgInHNzUbjEThs6BMMS5R9KLLOt6HU2yyo4dFqLfl8w68PPPVAXNw_mT0qCXqFfejwlbqptGrNzzwzOH0as-B3Mqn988GtG_6BhXZAYX3vG5RU35hCywWoMArzQ1glOKSGxsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAGr6XCm8hiWzWhZegoKs5AGN4a8fzrLUoVnMimF9YrtsGafmBp5OVvlL8JgvqL3nxFYmeF3C_3LrGnwDY_M6-A-UeemvnU6nEDHS7xza0taVIKtqdoG4MzlSGS985lmXAfVkyB7ypOhqwATQ-YjlAzHnPChS4_8nLjZl4taiPfzAjA2v7hD6Hyq5F6RGVrxVMs-NU1u53uoqjgfb6tdIQhSRN_7kISMkDtC5dArb6VydGUv1BZ1NIyRQlFD3m0cmilNRCbtJKQuNodv3I-1Ebr56ofU9j3w5hCZLhybm5LC9iNstKTIfHBt5IeT-08K1QKfRVS0XUXEUdBczJPPLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMtezxuYDS99aNU-swWP-LXhtoBNOE9Ykq_nGZ9qM2uN4AX--GEMxsw2h_DOvHBiTTqDDtJ_CxXje7LXSUif0UVWSXcmA-MFEiF5XwS-nqnvBj_EEcR4zbswEVxuXkye37c1ZL4OnY_ZgJ58MXy0-jEPLAuOEOtoprGcyDuipELxUYmUk50W6EmPrfoNMGbhSo5QdPZvshzNg4MQRMNermYq1KGDVJ4v_GI07WjLLLARaHoHRA6NvXQvl3IRmwl2Hxi2SeVMNsSS7vcteiHXk2qHVYYQlUehFTQUatXchgkMCFRj8dn97GiM_uanR_4_gxQprUOni_yqRKA2jJhuQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwW4QmwtBna4zzNyl36pM4874Yx2yXZY5BA_f-zfDpv_NbkHgLFeXbtdatNRWo-dWdYIw9aLX3CV3DoWOfu0NW-bp7ORG5xnvkE81QSySnp3b3H0ib4cfCJuql2rTwF-A1RArH1ZhCh8hj8wUoLkGAiVRcVowCNcQa30rF_6utibxsjXM57HaZcVT6e9VWMEQWHD5NuP7GT8Ad9JX6BFP_Km0S9nsN_sUBKlnCHfZ-QiGCaHOh1IjVeValTwY9W2ct2AdInybvi2ZknafP_pnpEXNyIAjGO86ealNSdN3kOwivVbfxkZBGh2bME4hykgoD454lcoReJA6E4nyRPx-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsxaE_l2M1DPYCHsqeSzxx-pvE5Oj9u8NoX-rVLLY3I97rxrZTdnnKteKxpLvwKPmBvrnUbmv_EoDkokp-AdYwVhHpjY22iZAfM9EkFBNKdY-WKeCimRxxsLAUSG-umwMCT_vKJehIRyTugAT0mTc6TX7AdCUVymMbD0RblU-JH4v4zTKWaRjZOCAOKDkoLBwrSDGgHcY7Qq9VN9fu4dk4-HR4SeKlwl6jj-Hy_fig2mhfm75ecDExrpEeAuit6HXRQDYkbwGhCLJpLWX0L3a2UZ6DH1R-c4084cNvq7v2dtEhrzFzuMA4EiYBa9ynZd9Hs1w8tWUKz82q4uxiHU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvftYU7kUiWYr0pJJhd-bTxND9HGMLMWXOOkAhWK5Q6LKo_rVnUvQYJz4mqhxDH44tHPU5AHeRT0kl6o6jz5rcyKlXoK4wPk0MdNpFa9hdEbfJltYOYKD_9-Idxes_teKwHV5n3Z4k_x78-VQfV8P4pXUbagfjTyN-QTkZLtdFEHDaRpa1IMrIdd2KOW4GavFWfe9Z4dl1M5TwDIKv4p9HQUALc0SQ3Hz8aVcVJlOiJHAjQ-BkpMGtCD3JBGd3KgngS_p1HHs5HJ7Bz2s9Ws1v2-nLvR6CAOP_LBEdliOJk0XUPFqc4V6rh3PDtqycSmnCiwK0F0mJXCQSfObFL9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKobYMidy1LXO3aHChf70ZzCR5uFLNV0IDJ7Wcqha6hUHLMnMsCzqJknyD33mxoJBXc4GW3-V-W2i0MDaLGCnzjWc_Q3lKA2GxmaixQIk128MDltK8aPqUwIwGyzqvNKnkaGOI_Aup3BR78mpyZK01z6DSDn_rbwraXU4vlZ3kwH_yzNS38Lkk5uCmnT6ZeiHrCR0QkeVTqlWdeMw9eUVC5UwGXdT2EsbHB5UgMF2BGASQRFfzBnuTb9Dt7BLI-P8zDC7XeUYJ_1Qd59UmzQyXppAd9BQkD8J1IkclEyWb-8V0WuUybSUX3dFrOhrwP3NOFuoy934WcrkEEz-hI_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT_ggEtem-pl4FrC1uRGNCSbp35sc2DAMiyBm54Zj5UzjWz4G4YR0nS7ABrN4E8ZN4rg_kdXDT5Y67LeetTAgWBJyuhSGuG3gAdhIKejHWGB5VslXo3gNX-qHoEIsij3oAzGfLsAGr0EYlrhbdQ19Vmwo0ydC22SyG076FMDKQ7AmFURZWkpczgwZfzx3OKCyS-k0SCS15oTgddUNQMiPLmnhzZVNq48X0hLgvMg2WcFC-ImZDwp3r9e9ihC3h53WsuULjiu_2Pepj_PutuzpOO4Il9gzpbTHucEo7e1QVV6JRVjmaBTcSTHIVT-x-5qBy8KUUq8086xSR5N6E71cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txE_s_Cxs9pVJCpOPt21Fswvn8az2KE1164PGXlSyseZ_PQ1eamkCS4LH8hWaHk-JrUrvO6BT-T0DepzIju-ZYtgwQG9rZykKZlM1VFND5VEYxyWdAhHza4RMgclCfhlfrZ1cJlQSZl5Pj-plE7wkBqtwMOj4qxc8pDA7KE1509JOo6WPD8tvXQtp2AEcD4YxAokPROwzhpqsiFuU4Lcv9C1ePS1Na5YUx8T4cbE-iA6_fpmU-B0Y6h1HJb35DwG1CLQBC6ngpTC96M3r9upW6yHSPPRNT9MIWjOKEigF-DA9tiwSSa4ZVTw6VF9-EatODPT-iOKLtsRw71ra-3cYA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=O4LPrIOgr_JtpKBQRLGdu-UV3OFGhsS8hFC5m-2KIPcO9WBk6Ut8WhqCLhbYsB3LSxksZwytMMekDf33rykFl0fVFMsuF2Ks6DbjXED4-o0kEgLlvK2ECF5YeMYL0gQdn_xm3a6U-Czidk63LAyyhweuZ_BuSZJfEspLPMeR7ixVRhuebQzeVMtTIHo2Ba5hHNFm1lWw7QhNS30s72lYpYKkb9gymcAw4mNqLsnAQLon0_rZmx1gTBqVEjWuY2OKsD5ZbKNX09a77veTrRD3WCTDEtVE5YHIZGAp6u_K_cF-Hz6yUFFI2ki1_45Zyy-Fl2y5Tu9ktbnea2c4uqO3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=O4LPrIOgr_JtpKBQRLGdu-UV3OFGhsS8hFC5m-2KIPcO9WBk6Ut8WhqCLhbYsB3LSxksZwytMMekDf33rykFl0fVFMsuF2Ks6DbjXED4-o0kEgLlvK2ECF5YeMYL0gQdn_xm3a6U-Czidk63LAyyhweuZ_BuSZJfEspLPMeR7ixVRhuebQzeVMtTIHo2Ba5hHNFm1lWw7QhNS30s72lYpYKkb9gymcAw4mNqLsnAQLon0_rZmx1gTBqVEjWuY2OKsD5ZbKNX09a77veTrRD3WCTDEtVE5YHIZGAp6u_K_cF-Hz6yUFFI2ki1_45Zyy-Fl2y5Tu9ktbnea2c4uqO3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJnR6HhNF7mz2qU_4x4WtfKCWrBxN2_lQC-scdJxIkxuxgddwFa3YLsF2yfJphFDXjP00LE19E0u8syHo0Mok54r8K-iwkjaRUznTjyg9Jl-txwRBbA2rzdRXugxk3fg5tGvXyeu711R0M0wuHBjlf9IZrEnP-1FqqgKxsEBfNgjNDNJ_Md14qqHlFwI4Wp7BUDfxNjvuYw7NKma2hRLAhhDkgUAxpq1wvSddQ7_K4Arkh8oNrqxeoLsAln5YdOQDkgzjvEawSwEzO3x8ic7o8oOlZ5iOnzbdyEVUhsPh-CbwIwxO0tvvUXfXsP3PKDXJ2-9eQhxarw_kDlEgEAmrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjKi6BKrI27IrVLaLmCXQHsLFgIByyJOwCL3vf4BUCo3zYcYjMgfyhda3ybpmQkR4GD2bdbDzfLfooePcgEu7ofscwEaeJVh3O8SwDXXo9zP9kbCqmLQkWMGt64SIlmxUXphuqKYJFIjoKIwEVXWCqaK8XlWuo-BuD0DO5vlyg8PVKf2VEEaoGk5TWvn1cMjWxCvC0jT77AxN6q95VA8mxEGlR1WTdmTg6kviEkMPmA7_ugndoThjoD1-UxXWMRX2xcLTm8DTvqlBgsVUJcTQV3Gk5sle3ANjeFAeuTmwR8oDGot-Nq5jX4-uET933nmyDTFoXZj8Rfmi3a2_83zYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ig6hxCZx64y9BaOAPladvtoQPkMOuJ6ttAJuiC5FelV8LQIDHdG7gg7jjZx5Pkr3e7SY6T1i5IsPrchJ2BJMAxFsBUeRsWl-Md7r5B8hc8OalX5tCCNdXKaCk5-jmlhA80gzE4WgDvhX3NjAkgPlBX-_j7auP7zXfV44aS9_IHDmo-sJ3Oh42IkmGzbS_b-OhHT9tx12m_4QWyE4ele8myJrM7tGCs3xHgwFDH0CqgpJky9Xw2rshoCsd0kbEPiUm2qDXjBh61jQr6Lgd8eWA2xSOhzjJf6eU_XvDARPr1YciwhpifiYr4hLd0V0uChbGfqLZYv--yEWGieUGWhU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvdavcDZtrB7SMg_8jmw6GeWktznPiJB9MC5kZT6JYNnQhwbCJrtZJ3PrtgjYQsCEEqo4pgVLFw-UXNpFneonzeRcG8ZoWiwsuyboMOM8zgunGlm8TSuAFxWCrN-ZETBZHB37chhs189Qtxwv0HMfPNHDNDQoSXFVK08X6Qusj-NIVlvZtE8d7IVJ2A5gy68A9hq4Uh-SYpYaK6rtbw3lTZ1zuRrCwrqbYJaNjKNHtUJycO_jDOfKZE_kRVAjOy2vIxmOvAdAWImAbU1_J4fxwZczT4w098CdcGwQ-GQ_9TrjWopDO7sBfUDJsUhw5u6ohEowGSK1Vh2nBstF55YbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqELwJaSpy-F05GYrrwcgbWTrOdF8TOCEQ5nFiBM-6Hshxbtcn19UJFo-ZInOEtWqgRkD4d0EEr41kKZkXZqaEWxPYF87uEPO9ff-xq0kOckHO1uAKQnUH-ti7_zimo-UyRGAoQ1fOfcoP2ED3GuwEUPXwzl8YkcAbdnnSgReO_J6fC678dTsz0OtY0MPE4g0saD6UZYOjpZN9TaxW9q8hzS6xQZCFq9vmmctvaIJUxtvYHfOCSRwbkugG6H42FD6x9cav8VZn5Riujzi49oQj5Ef7zOlBBZwhqqaPAR0EcOoIRfLcGVsePdHh7yxg8FUGLDgaawzSD-h9O5Cre1Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5O2Redb_juuH5UPAXX7XodokoXqK7xACva22kiYsw-gNuNJpvaRdiyC7LXVhmVj5EY9f4Cnlq7eqkP4J6pqW8PFM3k-K-QFFPUaxhC0WAwwS5Of3y5D0WRJDF_gDw_t5OL8yTUoz1YZ1TIw38DZQ28KgmMqtCVvwsB-hNAVqnHlLJFVdi9oubkQiNy6UGe4qXzb0YAOFEUMCAHf8E4W1wFwr4rilKDRhjKFtto8aBAHLAhsdHA64ucMgklxmBhYqQhFokaMT7qeKR4LfLuUp6gEYQfunWlxtcsF1HQAp1lnzmFi8NTrEqi63Iw7TwoxoHxXRQgpWP5XGrZPbf7WDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1Wz93RazgxZsciYKlNE1CyAaIykCRgFtV2cV_x3pW-aqq65QPnjBlHO7dMZWkJlWqzxohd2oWFK14-KNC6daZTOMLxdNjgHIsFIveIRMpKbG0nSqH25wJbkjcAOmTZISweTgR9QR5wVh_n5f9L9JPLRye5ReExsZ9VMh0swlcMAyH1lJs49WOuC9lg9BQSCR9zHy0M57ySJT3FoP7rAXq9SvLdXK1ahoS8GY-fxRMzyJ9IdbvXa8mwqIaRCyH2mahVjxj9fv-S1sMOxy34-Vhsgeg5D6HgoX-YtRXueWvkjDFexNF9Dx-ngsLlfDmjfY34b-4CQ_UFfy1ivNbKLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvO4G7MgwJoz9SyFgxdGFmADeni5wFAQ2q6Yv5bmeWkChdRNukB3GZof5GjjafO69UN2-1HEMLUx57v6DejDV-DG5BQ4KA7GgHsN3R8oJkMYK4Ab8-b72d_i4FgzoLmeuX5EjRnb8ygZRsHI7-VI6Hu-TeTrKEKNtyrcH1fKv_o_ozwwagKRdNzKS1_JG3rT4uvNz2G63NuW1Iv7AJMOMvPt91o3eM8Fds_aV4VHZH2y5VJitTaiZi3Xk9qce0Tu5xAoJ9GoYfhJLfrFX1hx2gfZJWI-KNWV4v8kjk0LUJ_WcQ6WgtKw7wCE34ZJ6EIFLAPTcfEcOgxa_Xy1kxORow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ_9m1jqWpqYRQtrL6_ZaXunFryiOALGwcA4xDsoCs152s37Il6g_qlCkzQPIZb1nSbZS0zHFcCYUEWstFSN9M28k9Yplux-AM7tiKSeSOkyrs-wkAZMStn04lV6oL7GmQiFjnsLeBVzUV0S3_08pyFFTrhdHOqun0txmRdlz_7SLdbniTsddwEhJnqLiBXb7UB3CvNnvpJzfwhly9aULiQ7IrFP8DBtWEm8Tv2-rcbYe30C2DR5EElj2M6r4k8c8w8chyf9OJBi3I2HJ_yKwEQ-vy6Oh54zdepNMrJJwof2XkRKJEva1XYMTbbjzraPPOyu6P8Eh023CkgBjS0Bhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly8cf59rnHJVdcIAz3B4qUIEFWQeloxIifnNBrJLU6P_K0137aMWZ9KOAzsfzi_DFK1bt5C1A12D2h7Jzw16xhsSgPsW9_kxhWwVNjzfaql0hRp4qcmslx6tWMtsq_94EMiPODhjYVE7xqx_eIizjhfOhpvoemTaOjBjFXmcCyY0iw8ta7DrnB3VlhnvX4HOA0kf6aoDpuwXgSA26TNT-9AbmDWyjUCPHt6Lu6uiogGJbFMFBzbbPWnIJu6ldCDT7K-5UIp52pyewyMPgMOQaU2JIUNlVhwNSDYvKUOt89HrIHY_4nmtstyQqYlDiVXh15q2d2qcXeUTvxnLCyb1lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eS_hpaACtXoV-hWHdFEC0lkamb3uaTLcgV5CqGDYEE5uOTTUMXA5cdr8HkR45vAgQ6-yjhUiWwE5AqSiSu-66gTkY9mRVurKGvxmOPj7a2Ycno34cKVPOlh5M-T9GhOPJe9YbtolKcE2BQBUVlcjdhV8eUB1s2Hy3V4xGgGDtuKFJ5FbPNkT3IRa6OewQunIHVY7uWHtEDC3VDTaDLTO_gv4ZGh5-IG7NwH0rQFvE1Vyy0SQqTGCZXfXpaC_gvrw_A82BKtWL-t7VJ04705I_ZpWU1CSgHJeUeK0yIzMibgz1w20sy29cNwLX_ewcFm2ovncIqLjyW87kq5WvB-oqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfWKjpYDAgnHqPMAKnaitSSdqQxID2qa9THogKJLaUXGVY--65OCVogevN4sMB2IGA2bp4JP-28H2I6SOYM7zxZxvdgLgXZbmykxIGlKEVMz8cBFMPoubYCb1XIrcoDQlfEnjh5bXaJ4QVIE15Abccmx6JhLHdOW26TaHof7Eee_nAOAN6XVdlWVGdMxnRroXtdoZoaQtmOWifg8MU0qAUvuVePkOjm8xUFSU_2b4Y4K2SlTHRecuOrflB83_MMzXA4aTVr518a2Js1Mbx0GMqnGrXHPVfaVobswj2nXvT35yS1kkocvXphYqIppvHRD8WuWKv-10XMI80BibsZRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikx-0xYEtZemKH6adbyqGEkQ23fUAsG5j7DNnsrjT8diMaDv1whrRCep0AAirimKgC3GQcOJNJjETk2pdGx1bKbhAQZA7PgmPk6Euu3A5ThHDY2ZrUl4J6CoS6im2Gg9Q-eVoQBYBXrSmk8CC1pBg6WCOMeN1bX4UZEYqL4quNTE8SrCAhBdbmzm_P8P67dX1k5B8duUM3kQANvDStIGQI-IT5vN45Jf9TtnWh0Hri4euKtabcxSQytr5U9AavR1ftRbs3IX23gq1TfgyRF-F3QQHTxNATyMIBHytKZ8NV4Ko1D7MuIKZQN0yYp0tcan8r6sTfuNoEeFsLJNZOCUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPOrRZfIEVbJqbM5_bE3bVU3lUYsksQa_4kQn06WkzwQAx_hn3Qn7n_QftU8vfCRIyCF_MHE4V_RSW7nD4nO6noDYJ8iiPOP0yfCOJBBUqYU4Bamey1UIEDoquA3NlUiGQGpXwsqI93p9pWIqQawhtTbNqHXlQYOwfvXMwAYb9evCWj1ZGgwbfAnNe9M0hAcrY8S9ffY7E5CgYwCZdeXIY4IQZz9FY2sNQQcXsYnxpxFydjuVkwPfRuQgBW4uk7dkXSmr8qAZzU_hy7rDpSFop8bjI_RazwJxcqOPLgS7Sv0oLRygV-8L0bF-mR0mo7d0PpxLAKLfWAVubK4dfUuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oySj1ZM_JpnSFNKFDCNBmPQc8S0-n_6LCoqPlIS4X9OwrvhEkOD_IMKpkFZo7HooGM0c0BBvzRfvtNPpa3lVWRX04uhUxP8k1bgq5tXsFRAthf0RvUUkbtmltUJuqA0w4q1th27yBeM4pGmXY4SE58jPmDFTx_W3ngg5fYvJWnMLkXnjr1kG-CfHoR7g-F2xGCAU6gE163-Kvlx8x5YV-30L9Pu1gd4BigRcKbEr6k0YCm_VnlICnIYhlR4HlI9lCltAWk9b33lYkxQEywMXpz65-Hu3bJojc338_f7zjfHGoSc54WcoIO6PTbqp59mSSw56GUu7VbPvOR4yC3Zmkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grXirecCtb0iRzkzoUO4nZOpHnxXfi4h0A7sGMDZyOVR5QJ9gXbnAQ2rK98IDLK7tqzHPJvqA63rhpcO71UdrmX-H_5H79T-kb0nbHmHytOktRbjT623QpM_kwzq4n7D8Cdj5Tgypg_TXrachA62JPPBNqfzjRvigTir7M_6xJ-Oy4Vkumxg28i0KUPODk2urnTlsg8XjIDG6uV5yQFg0p-I1s5yHGuwv1aLArBPH3dpfsbjoZug05Kaegj4cjCv09fUF4mgixc8Pcou_7rvIk1uxRXmLmZ2Gxo61YaS37UKCwPlsdXMsbWPWvIDjamwQ8MbZZVNXSFEhTvEn8HRxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFJ5IMlEV-l9cFX0tPOOUjRVQWoG8A90cwP76a_DbEKu-SO-yB_T602D1uMkxC5DNiXqC5EowYuDEcuevH9_ivkjyVhil_ZSDyu_Sx9ReJD3T3HnGliRdfzS8m7Qm1ekJecwaCig11fo7Pm-pNHl_3MhGpbk7z29bp6_7lCt5vlHBbJwmW4TfDRjixkcJ8T025bLWwzqHHYcDy0w6qw567lzBMYhjntSzfPDWNmETRWnH49qy7LfXCDcP7Ua9HBcxgjRGiAQZxYOh_6SRZ1wcYzpbdeS3SgOZqw3H-JcPPTrmIU74-MRID7sS0wW9zbQN1Kwl19eOK1RgQ6XpgwjJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD7deyNvvnez6arow0ZLM6MAGQg-SLQQDHjzBW37W_nnxy3slKw9aYMMEg0oU8RhSkofOcnUeAauMBU6sA_8vETXGVPw-t0EfFvPNnpZ4IuSY_v9A4xo4ZPRBrYoHoa7hunj7Nb5RrWv2cKmBc4J7T8mThzf8p23-JiqLKw0KArXub_5k7b8NXYP5VEvUd_Yx4GiJwEcOylFS98ZFLqCct7Uprp15SW5putDgNG2zyTN4oQTC2bao8-sL4bbAsSXgoSNUCHt-q09lIJGrXfHOIKzazP_bTw9pwyjLv6H44LD7lQsrkciNLBknw3f4bmXwqb3b_HmWSe6ZwZDybpzHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZbnrlPbI4nGzf2mjoRvKPHm3CeeynXSydMAk2AYYtM_09dw10XmcaEJp3o3j2oHOBgqq537qPi7qrDLo5vt33wdMSRpyjGgz8kC0TMIZs9YHJ3UGFY1562hfOVo8wUZ827In6N2dlAylucLJHvPvX_2aJFyh8xlb1d879Uro6pZFZkKBuuvVKSMRjtm8iXAaDPReBrmwkDiHVhfGRfgVh-KIoir9LePZOChNqEx0z-2gr1pgd_KHe_M0YJh5UeRv86nwhq_o0ZgpMV3cd354t445jh677sMwOmh3RDN5U8xfxnmo_FEnUIIJq9925OF0i6HSaEVRuRaB_edmHukwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWV6ud7x9rGsu2IYd_p-DZJSodBWDA2Vagam-ViRrQcZ8uGTs-yABFsqjfkJGQNoh-S9VP0jp_IFuSFYoSo9dNM0UTSRi79ja7Ka1a87QLf61ke21A2YwCeL17ARRdc5KRBHuDfMUdXlUZw7607rS0SG8w-89hDzVBjePGdK8zEac-EZlKbSzV5o9O8mcLr0n9v4mxoNAQ0HDRvrNqTnEOybISJaIslyiN1bbck-Lfz0zkjHoUdN5mPEhym7KIZBZMzcqSeZwbRKL9L2Iv8RMlcxiQQeR1ynZLWaCqvDQljyQI5HmeTiu0TrybSAMzZsYFgubdi-kYMquZhTrgmvHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP5JGRSOIKei2sV4vNVW2cI8G77oXNmIhNQb3G2EAQPkVqcrYZ11RXMtYwV_AyetDeYJYoE2vyPzqsg1IuODK9c5Ev6C2Kqzrpmba-OhhJQlrhbBYL6zeHgxvv7_CqXFlrHyxJmaGB9W6baFt55phZbNkyCtcFpysiYE1LTSc9duL46umKOKzO6lrqj9SHrAtScMQ2fKlRhfTfu9YUvPS0cyWs4Lk7cBR7qXjo_fKeDsOmrQASr4W1r2HRxjX5LPBXBC0OwR7VGGN-TXPI156Hc4N-E_x6kKSYhBmb_ZmQjL-D41Tg-I7OQGDyJOw1HANZGU_LIERqu9GDCSh5W8aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4l1y90nPUGiETpaoTwhLyjJKQiTHeWvykw_iIRzgnjgg1Q6atclTCF08RsZU3RBC6GSsh2hJBLk_LAfQOJ9pBoZ2gWtd3cFCpuMQLD8viZgDmBHct-hqzNQesgr9oFBvd3gLWcvkYN_Iz-qCNHxcmdyY1V75Ahx6zQPaeNHLPlIQxZaRVOtPOz8G-5931yhf9xibWxbeN-CmSoO-gJsXg5JAr9rUZ_Xe9W3A7xFxcJ66jRPLETUV476n4dgj5-KPmT7bZqYyFEMZt_AKU_pYcIP_SVZDdN5Qa7__obnfXX42fijhPiyA0Bk7WB0XfWN3T5Q3slEGqt-fbacgKjX7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDPJ5qX_djRESpzt6qeYEYMO8NTlH4zidl7vsCM1PqiD-ugu-qxYfccnhKhqgSCKPHuKqiCeM9sY7fEu4k0aAowBnl_XBatQHtdlB9coZQVvdjqQ__luYvMT_jopVSCBayCJDI6TYd6el8mAu4l_XuaMwrQ-FoxJxCquSGdm4gUrIGHFFP3idQhdwD96vGJcRMN0eh6qwUpXeFpcYnC7GBM6hNU2C36DkTFIk0-_nxQlyKUTR5gYkCRwZKvvfL6ym6JxvTfj7Vz5f3plkHZWSzOgs_CtK3kgUcrRkTI6u0dGdeSo1bpeqgirJrDuPkgmjOcsG0Zv7x69ZfpR0N99NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0SHhc6ECOLO_4Me9vOTr5Ow0Ou4H4TqhpUHvjfDP58mQkg6qK3OR-jLZ0pphHHs-zrmUrIUu6RwB5MzB3ykA9h1zijL80L5oDhm1bx_Z3XS_iZS-wChF7PhOJ_yQ47ymlb_nXtyyFToFTOR3CC5Q-XcWKnYHH7ccBj-R8OTM-xaK9Nn53QWTohB8PwwbeX2M5TJZGGFGJu82FL4fpILpAJ3eLqswCKSd9VgWHqhKoyZm3nV3M2QW-S3_QZTc8YFHdclrfEoS0z1lRqUlWmYk0kR8eLXQUP1CBowbIcnpujYx08-7jV5sWotm11fnJTlmSIfDb7eqwuqbVfX4_a5gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slorxgLgfSswXiRLB2DvlyNjdChaRzMBP9WSsIyNyob3MvzuxCq31TqFesdOy5KnV1r_uwEQHrtna99v1KmL6cj2P_bdft470-CCIjxXKGzjWaHsuvLjCQVaPoP-i_gheB-vGJqz-xkYSKlAi4n-xGUvuPKYR98_RMfX4ZgF-GxBlfrm-sTVu-wMfYScb51mpQ_PCBP-07NB14Xbm7LpuOJjFQVcfSHytJMv2uISiebYxrqfzUUgqrAUprpc8DI3gH9x8Q7e44FqxbLTRJcIDkcW_xW3Hb2dwSxmbiLomUQixJPTkUi9jxtFZpB65D8MB7GGFfSq7scfAhFiXhz2KQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf0nAhzVBJNTx67TjooMJcnbBKe5HcD5pQOiHWyrVehqDmsOOZKXnGjuXInGflF5F-hTD8t8OQtX8RU7VPUJSCDPOQXdG7TGblKqrS-jWeIAGX5kMRp1L3FjNUYOt_ulCMdf3JpfE8_srvJyIj6VkbKkmtu9emI6LcG-LpiD9tAzrU3aUI6XVmop7MWjxUAySXaJM2r9AIf9hBSnTBwb3QO2A_vvCnv3v6q0RLO22oI85s7U7gvC5jL01V_MItDExqlAeyxHmDGASniCsD5QUgj7PTf8B9cxOCUWNlXZwIh2qwuwPWvUNOOjSU4OIeAIeVRgCpIy8S0IbbO3VEOtuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auSVFDTR_Q51sHvNIt14sL7xe_DKSzGlm91e9cPq98PgTZQAWxMo4k7SKDnoJMAEbIHLCWWTcF6aO1jNkICDQ4X4RxvW4Nu-QQ0IV5fsmlSTOExkGBjkuHC-Mr8fDlLZo4mJhz_gBi4h2Fhz3R6f5sYeeyverEaGDC3KajzlnfblNi8Oo7k7Q3f2yHdSgsAybrViaOIbHKYOp6QQckPgX0GFgGECwl2DWM8IUlUNCYhI9-N93PRPdhV_9IFOw44dsKBW2YkgwtaQiossaf7NYStNDfRMEddEWXjGUj3fZ4LxCoVSCS-lOyqHKkczMedwNb6evNi0pax_55ZSk2iQNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd0nay-yEb8bpT5pyigCmue2dqDaJI0gUHKGnjhwiWcB-ntXr61W4BeO4Si6RshxhWak38lBq8h2gb-Wirwe8TmqD26L7JMMNs5mJwvxG2t1DVVbDb6AVSgh7yhsSoIJF9zPC5_CJGMJWV4rpMasbBIi_DQ0M7O9lIlB0pnuSsEpvFpuBu8eqS6PZCxdVGpdNZ_-O6Dwv-Llgx49NlwAoXfLMhENDvoMZPi216pWaqMQxeYZksGDGyokEp-UPxFeqPqiCT4ESwYVLYiPEw0DgTJAIN3FyLr6eijZo_RxkSZBuGXIJ-jHL66ayiuS4M89d1ZLQbUZQOH_XVBbRk6aFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SE7WueWFJC_o_DpKJz2JqwJo1ImC5lDvR_Bp9vWu8HVECJJLa7F_c_9LK4OS7CelLGcOXcIrAjmHpszMxE1t97hVXrFuk97A8Q1gmkpK-m1Jx3r3eDbu1QZ95lOIimJ_vRHRVLZ9UZvMGwxOtcNzNM5HcMRPFkv81dfRhN4pp1RZjUyU5l7cKwqoEg3qG-ZDVEUJ_sA-KdyFozaGUAQ6DmjjJmPMIi_7SnupLAkz-HkMCTlXiNKKhMEF8c07_5jn-vd7aUZz1nhyZbhx8n385Nhfl_ikoiltLrbd2_YEOX3FxzmEdyicLQSYHOV3QAz3Ni3ctRkhJdjm5dZpneqivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TluVoKYa29A3axHivIaB0XTdAEUoiScbuL0k14f8HkxhQGHurQNX6U40enpGok_ZXOczMeSTKXqK6T61ojTw5jFMC4YN9j9kM0-hiDVHLM98IKdKkitbw6fRApXe36pSv0pASMLpJJXIdokGW5ie_swld4tFQWmfwM-xXg1-s_-58XSVBZ7hnaqHXIbQF4Qtl0GZwhcziA9T2721fx18DQ51mVfY6EEcoYBbulkX6CW67vvbzmFcLuZMZepALjlVImWjBJNslWTZlufSuF0IwXsaRf-IjaFyDbgM6TPYm089BQ2Q61_CH3m_zMNEKEb4wx5pgJTuHVO4Op7FDM9Z8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slIKrngB7744LTb59OfKpmKJveNrgfMVdZixytGo8JHStA29KQ0-ylSv8CcGYyyRf7b0unORX9xzHgAVQkWbzvugSMYYHulQGiMrCeSKh0NSeXKr8C9-DDlM2_PweTc_4R7xIdTIBa8-84YXHgOnD0jhNmdOaaX9DVZd4jf7jfWuAOWu7o5DY2uMBfUCHPqnaLwVpZrLgGs6atZ1_umcdogC6ZyGb3XoW4KXy58p1BKm8Cg7u_TsAraXTQthHUicvV1qLt-SQyS_XMbFZvHZNdC_FQb1C1BUm3Ft6tHVo40lUeCrQ6FET5nsTplPIwYzS63kHT4obf415EM5VfGIpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFG-JosY64BADHN7bAkp9NjuVPs2egkJxETtnHLvEkohQ_repzDDjxgaBACBEcyLmlOb0zYIIuyNeii0NQNUswwZ0fR2RBBrdrtmpz_vbKYp2xNM14OhtYptlHnZoPHoUarkNCXTjMdxKXLMRLZwihWGvALiaLWN0ykjAXcoh6vuMJjZlIvj5F91qUif31zSE05tjcGMkPL0PMCeVr05gxEoVo60h8uXBaPUAU1xr5rnxOgXa-1Q0NJX-pj6MApXTuVu8i0KWWUI1FCBY7OCihUEkkruUrGsZmVFsZDdbSGu9_Crklnylmt9m_1yOaapOkH9s-Y913vJI3tC4McgMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruc7X7gNtZ8ScNwGUHHfKgC-ZyB1UCQkxFWEqoAzF7JgiZGfPq09baiRQzFH5bNm0PjH13e-UESYSmbw2XSHb4dfILCll0QTSw451e4dWj7dKvWTRfM9gqiiE9Sp82gIg4heKwEtFwyOkna-EO7CjqBTPKW8wx7dBbJ9bC51efF2a53Pw--a9jq1GnfaMHvadDKf37NiZXujwF-pr1zkPkXJafV4Mh9t8mtEMFIJihr5NjDWQlWkT3uIeFc8Ja-AzwmS1yAgp6sAS0kwI-g-m7Pd9pxeLMlmwstiXfk7F85ZZWghRO2BRld2W1nhpE2iQ9JJTNA2ecpK5lmr41PH8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHJzmDa1pkLWayFk-SPhbsYJnx6GQKHUsCd36pUypcAFX34criBQKJFrWEsE8kHwyyhhxaMzGxpbQTt5IIhkbw3G4NyhQHbZ3jcpH-w0OS_iCl_rAhTXmMfMfFYtESQPpF31v90iqdTYq1Je_PbB_aqpvqILoSsJyDSiwQVlxEfJkXU5qQgc48h7xp4Ze_u4oBxg65pfW-Jwngyre84UZ4GJpOuGTF--RIyGSI4TlGusJZuKyWidFgtNTpkTdmn3rIJzRxl1sd4nOqEF_SuApIiJgv90ci8TWfY2BJIyT5hHBZvDPtiTgf9OHGkM1Hp2ZPePbz5ygMgDubnI27KKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtIjiiWLs25m-Rh94fgkzBKgOISfVZcFhnDCueYYwxnICfpm6Z5m9SDVjxVRUuHIDQ4v4J1c3QbL8uHh8zcDXn0yp4zSsjmaporVUQpZNM8nh3ZTKlmtJ0Ylbi4VMbAp2cRrlgOttZRHCeQVteG74cKiRLiWlKxnOu33N1fIW2PdXJVWyjvxxbV3dRs0V2FvrfebT3vIH_EluyT2nV4XCBpHPd98wPFTOsZX-hjkkmHBc_GmgR7lauqbRivU-wR2b-lKt9qHvooDMqIOGMsj3eyxQmgf2G8I3tauEjFMQKeEChRqf7I2p7zX5m2iOzQgT1kpqeqE2gf1kKBOvCqDtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvKNRH2KEZcwR4SbyshQAyWCeT9Oc7xdTOS7zGxCndmDLCDB3ajILkXSLFZmdK4eEboBkGNEhKNeHD9rSXVcn_L2u8PTtjTxla-ULBrz5TnEEjfKA1lDc6cIoi18EsXsTrxbEgVA65fohC6xTipkml1p9mNA6hrLaQ2sBuNLbruoYOkmfTybMkqU4ob3UTUM5z75eEj7wdg900kYJbytunJs_lLOHQkVuNmdCBCMKefR4QcNXY88N2dSxzXD9FGDrCDUzoeb2KQRL4qV25rVgey2HSua0kuTZKBhzO404Clx7QRIhiS5OXdWnv6rsN6P8QxVDNlGVfcaO7qw3R0_HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjEYC0qWgTBn4a9w0amaR-7A7xmydQnJfZIA81XzfNCiIO3RtVPzIz3QDJsneLhbFazMEYdjwcEgfvTx0_kHjVPalGi7mxhKuxMNmVGwX3_hepnTz70lHMMJFT7azkpSJFU07VnchT5GY8wQn-R4JO7BtssiIiL2W8IqkfYPXKQ09-clGv-KJuVHaMwp_UZoDQyYivjiOjsGrzfVoeEAdUWdWwTR-GSj9Xbkn-uumkMSmArHO94EcR8eLxpEZ-QhXb38AkvXj5AWDg_lknilLtyz1EuAbJB7Foj2o8BlJAQvS0liceqzRnpB9EFmP0djlGWSCseAf245rgl_XrVkUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3GjCMIneQj6YIqrRCgbAtTN6Evu-mW01SAjEATk1DYx03HyVupoEyoGrmJtgTWvrVcovw3bgJ2thYzJGlTT56HWyivui0blYo0g3BPeE8ozKAINvrDmRv_o5bAe7wksqFqNCQlvhI90ksOW1ypavvCv4pLJuFrSrSsKZ5wfRt-BTznMP9_hn9_or9UTZPCxoLSWq7OgBfWo2uwPFSKMY5iMD2U07190GmtZ_frooHpOsUMqIINocBvRoMe3rdFUDmwKFVnVXEWFu2CjMc40sY-amCsUp97BRhXfgak277Qp2DZ_pyS4BBMQedCG4N4vAcAlQi-aVtvcGCUVDS-hzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXkdX8mqZTzjBy2gkjt6xOXel46Kojo9_AYhshOwzjoftiWdGu1ffLLt_wrMQz40JA1uVMenvVRNJF8h807dJZNrNfnwpSjk9NMe2sTByxUeALGsuDdhyE1vFW5_QCyxU_7dhWCBoVnlohzXUgND1QwGZn-v9Q6-lpBlFCoLUtQ-SPZjJnQShXHaGTu2HXGVvvzf9s3zx3wIJKhR6ipym7MJbwKHwWPIS8mHLNU3g29p9L45CBpHID0f8yTFga_8XP_bwhOR0jJ_y4BmuA57LFhO5b1T9edDAHfbl8n76ceRPDdrtn48I80OAtOwGePUrkBpqyizhlGF-nFSqZlESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyjqMScBXwraiD8RRSdrN5nEO63bmdHIa4Jxx7rvxnezxbnKx2-iZr7KyfejAPxoD0CutOE_xUMnRR1beddEppDYnV-J5AqZuNoISQwxzh-9-GFlYAgv31tkfrmMRQwFCu0Sglvt3HJ5GSbseOelfZAFlgTTJVDiLrYRFzR7JhFnC9KS1rGfx8kXhs4G7WJxQFLcbj2S-XcEYtWWI-lZq9uQjQGgzXX3MFaRZdpjZlDiwhiVzrAI1P4XAVK43DyzA9Kv946cwu4xOSRej-rvZY_pbdQQKvNPRMZVqtXwxxNFXeuevRKzBROBcAcFP8d37AkSabxf8s2cybyMiJgQdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwfMCAZu7Bn35Q7lahknRfIzjQUZl3S9LYABs_xFkaGBClJag6PchJNIlbkjclfgRY2S3CU9HlT1wOACk4L7p2shmAYanFlPokdlhS9yYEK57eg_3L7vN7seAsiUaDkFQ6EBtSNero_8ipWDqIlFavUmIncEVv-4DqCSMxHyiv7Fmz5-Z9WHPcSmWKHBb390Dog7SzdEGEgiBJsSXiqlchYGndprVJ9JvQbANEXq3FePAffMQV_GpNGd4b_1llJvBDciuJgQ91M4d8PyDR-S8Bh19IpXa0G6u7P4zKEm0P3xzrZl-wdokx--jQ2oqqEWdkZcZE_ukaxyIe6vTzhTIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAW9WOsP9ddduhjjJUBG8Cp7Kagt7F72WJVQy4J6ZYesKGnTx6qmnCGoIkdODNDnkabayIcaG5mm54E1_y6XyrVlbj0XrZKemhVNXOtsnS5-GroroQTqjyOdl9jlJleoldQA6GEekHHVUQeBkaSn8rJ4PrH2kS8v1QGYzb1F4jK2FtyT1H0Y4IcifcMpw6LSNdbSLgdGUQJa-FNJ5ooprxZ6eZHomjTZTdL7c_ZPRXelmFUtx232h5-X4-vD1MTF26sktZ7oyN8WiAiqbdnrACqeYYghRjgjN5cViCSyW9s9T0Nq2AFKQa5VM1VakSWjhXZtWrZtqCPD_vBZQ_uocg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbpm6E7IKrVUuixNBEqRUOOw4S5SOqnPv6tq5vMvq6m5geexsj8BDEfyA9dLHgscdI5ZwGrCIUoB3NbcC0ABs6H_BsgDZpY5bGry88m8Tn5_Zd1OksETRF3PawR0Vp7FUECFRxKiKwQ1cFi1yhF__sH7TaeIa2adGVVRueDFyRdbKPPJG23KJz4iKnHfRWJoPzSSugPRNDRgChkhLmu6Oo4pwuxgXKHbyyKHlvfaP3hNTJKHX1ADEYRskS0ynmgDetkdMLuBatUr--O3S-WvJGN9QcAt91WkCRRPsy0DKQzJuKMTZBSTQ4KvIKU0mQbAXZuDQvvuptJzcYKv7tuxig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuzwSEeznAVTfn1cHw_R7IG30ecinBykIRxw_aOS6Dr7J0XrMI9M0R0jxDguiKTqm97s3RGR6KqdfzNjQc6wAfkSsKipj1L6JowltZr4-xm7ZV3PAC9_CpEq7M1T_IES1Xjt08ysrU-7rRlxE0E6DKGmH5d2xW63eiEdcqrc08YNTgPkXIPsWq9Ci2kLOgXVv1LSP8enDas3SUAsGYqIPu8tZ_3VWUUxGhEIJCfgkkKxxEDBabNFaf_PmapKqEMazB5cdoXRz_E6sI6YvxIt8hUcrWxP2TecZbBnU8IazwDox0Sr15bdiDu9WlmfaZ3NMWb3LYJR80wPWrmKzyN32g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=T6R2nIa1XlVHMYlTzMMx6PyhmGzUVsvydguQAg19S1FjzhfHm0SBfODveJWItwJW5hZ3dWpQnmwAT-cblTdbvQoPa8cBqIMBQrS5WMMi_qOXCR5jnMIrXX8PmOGX3scnYtBaHInUoEffg3tnYpEBBm--kNrrfOnPps9D5HZT_1OpEzvAJuvMAT-YAe9iID3lv5NU6FT9x9LuvjGULrmWr5ExjlHcNbB1o_KplQGqcj3ORDvN3BJrwaREstirUY19IRG6vfDenP3hQmEPa4dOI0JCAVQZnjFRwVD54bSiA52uDqLXAP78TG-sdsMtFS6DBbwMRcs2QwtqkVy3u5klWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=T6R2nIa1XlVHMYlTzMMx6PyhmGzUVsvydguQAg19S1FjzhfHm0SBfODveJWItwJW5hZ3dWpQnmwAT-cblTdbvQoPa8cBqIMBQrS5WMMi_qOXCR5jnMIrXX8PmOGX3scnYtBaHInUoEffg3tnYpEBBm--kNrrfOnPps9D5HZT_1OpEzvAJuvMAT-YAe9iID3lv5NU6FT9x9LuvjGULrmWr5ExjlHcNbB1o_KplQGqcj3ORDvN3BJrwaREstirUY19IRG6vfDenP3hQmEPa4dOI0JCAVQZnjFRwVD54bSiA52uDqLXAP78TG-sdsMtFS6DBbwMRcs2QwtqkVy3u5klWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw6ToXCPpHD1MG98ZUhu9JtgHWCtTb9auDWvOQQEhAjjRMBlBRSkarVq_CYevTkzo7KvGBm_hwB8WrKwxSuXKQIuH5NRbMgRrd_dX8igEdvpo8qpAYCYTWucpp3Q_3E8MBDAHxc9Ift-tSyUedvb2Ioxfy1CE9rPQ2hvMi1g_HgvDtee7fEFlHxf5K_odczO7fex1arbwEdxegsrY1m6MdOSMlF6QCCYUCMOy1i8i47cmfbSvLU1EqTiqF-IFKt7mqvBd-Ihw1xrQKeaBAtZ77564Pzzuhsn_QPMBqunVF-nqC813eWQxCbRf6wSXpiuYvM30mrJMHf0jQwPwagXag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHpdR_kb119qy8jvH6ikVWYHJJZeEoA1sOShWfoaSBh9NmC6T3smDocjqJfYf2LO2-adeJuIPhgwPhWqJwlqvBCaR9xxVe7KhA36DGgPFLNKR2UIMjqbwxOAGrPEGg_QEuIDVKFfV6ekNPOtXymOLXSJ9GRmc2AN2mqEGEeHctMpgbRF5grxq5LLjX2jaER4Q1RkD_YChIHRSqOzkY2npgA5zTTAuPVusUYYM4Op2Zrlo9U8IMns3Dt9phn2qncQBJkFgaa5-EAm2hVD-se47zk90mARjvabMsF4ca15PzDh4q7TNaWi8Rqv2h2TRG_61kC1DFCMmwMxqrD7NrFJsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABTPM5t7wx_iTlgLpINi6FCW7jksFedeAeGbq65upomYGgSwWvTVkKfGJCl_xf0WwnbaYKehfA63qc1uE1ip1aZ5LrynGXDY-DZhYrGFPWwE9VKqMY39HDClkZOWfU8GrG591jvY4LjgVhVY8qru8aV5E33CAxddDVwo5qZtqeAAp-_HXdDogsn_t0B_WFWE_2qLF_9_t0SukzDsbi40ZYS_wDPDZDLCneL20Abwn1bWy-RHGHz4nCBW5t32SSSVWp2WGyKEJFUVSgFaZFme1a6x8iuEqnC8Vxbw5zvg5grRb8yAfAw_HSZzmrCtiNqKJ4LJea-y1caweLJxn286bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob19bS1bMemRivsCKl53iLulNrRrDOC5P1hZW6qBNLEZb-3dcM1NWLnoynQfN4rYpTwil1G6Ht94dpQ6Fh6bPJUxb-2cR1egxtvtD5d1YP9WQll5wnX1J3EiMbeOQ1cxtzNMnXdIrirax90X7iooOCfQ8H60s3Ji01g4_Ep3C4GXray_h1w34T-R8WEq4aNR0YkinAAD0duzq_NJ1K3NKj3H2Yy_ZAnvQ17MlcvZ5LmiYbXBBOpW4_J0_W6Pbhj39PJV45Erh_1pylRhkZABPw16jR8pm21nP1CHOhfX7icst_ZbINuZUulCz-N1q5KV0FFCtMzGw2X20DQp9NG3Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptV63oZC9lO55HnqknQ7NOm-vgDpZf6kNgj-B_6TOP1mnr4GgHAT9ogY6Mu0l0ndHvNZCDghgvNqjKsdj0Y0D0dXVOM9B3Bf1z7kTH7JN7IJe2K6XXZWOpG2r2y0orHodOnbUIVCXs5Vh58SlVdesBpe4uvsKjK4fFGzVUBTNwqTP01BtHRAJLuDHTaZMySm-G8yhcP5brNQXRmkJSxHm4xHTrpQyxHFNZuuf4q2d55TMtHxW1G070H2UNoVtD6WrkuZrdN391fh25hoHhwxuK4sUBwi6Ye2qezN3y8_SCkxCSBj3TaU11XB858QrvU1gw48zZSOrTPjHepZHIvxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejQU6D-gSSLq-XsXN65MvpWkspnYy2D3Mhay6IaHLTjCQfjKVTNES-z-8wwZuDJusKhN6cNcSivcRi0TNWA75iZYZUP4LA4NnZB7jvrdjVUXK0qD-TO0xqWA6hOI3_V7VpttlIllySJ5sKkxc14QBg0gdRWiI3OdbBat2oo549eHyNx6fQwILQwivWEJyFmB2sZ26mZFnoLo2pOhdDxiML6dFnxLgVSdQ2pmkr7aL7PSyz3SEgbNFWIzQgzwypQ4zF7yGjS5K7hLXrYgOfec1UZUOHzUDIPTEk4v3ImOUUAyIhD__ITqCpWlNkAikZGvnTuKEVMblt0xkIBX7ZOctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGAdRE5mqlhdmQd3qvkHxHSPBFXQo0LYv6xqcsNdDbckiVQUCqBN-5EsDaUzmBJpjDjAXSUD2xSiXVWW64eOPtFyLvumzxjSqPR9r1Z9FLnyLcURHbyFB5iuBTM_vGLQ-DXw6-DTl1HSKG3O0qhrPBJJyWhxuf0VyM-0GU-aAGr2GNmhhTUq02w6DL9K-iJQ8biIOSrWO2OqLCfNnGGSi6jpSZM6B3qizNcMC6-ttgm66CxSOCD0ckqlo__QN2ZBIZBXYHN17h7cXIGmbFtJzhJTD7rdfkDoRXx4Bsd3MFx47Nt6FbyqxEm29IcBn7T5kiP883EcGgAFJT2O-BHsbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=AIeBCCZ2nCIRHiIjG2j6D3jd4LHZn4T8n9Ihdk5Zl4972-kT8z603snwkVL11ZeIE5ll_7NgqXg-XJYmOth68UwJ1UoZRtS50mPw-c1UP2Aq-Ct_lMcDfjrxLFptJj8yOZHgCTexQtNVjtB0iFzmjGuTAqpwXcTYI5cQUbo4jKsG-9QcEemT2Nd1_klj1vjrWgaOOq1rtMFp-VFXH5YtkxS6de3jx4xi2HWDnhL-G-yDWioBDdmR55SHjXZQjBMUIGN8lCcHfW8XLW4A4_eNpyj8zZv_X0N9WTCJB9DoFnvQL4kdhO538ZVfST0RTvAqJzF5e0eNWCS6GAT2lwKo2Jmm2PF3jQr92APQA4xvIH8_6mLoeVeyMOgZkmBZXDE3cVkOr94Cossr5h1ovdaEHExWO1PWXssSxZhuFA3vNfN-cSQruh2YCJ29Xb2TIldhpdrXYgR00KhsgO2foVg1tnd4wLuSvvlTRIulFMsYixw8e-7PwkZFY1fKZG1_-sD1IM2JXH9yRPyQC7Fn5-VTvlIZDHdlfR86zHCZYMfCW9MzHSazfeyngkY9kfIreQpLVbrOCgIKKkt0b03aksPg6oIuic6vvczDQy4ePAb9MmvGUAFH7pD6O_rfdbFlaptBjGUrquyILUTmKbSrC6Ae0EJa5jocImzEoSREbRvqOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=AIeBCCZ2nCIRHiIjG2j6D3jd4LHZn4T8n9Ihdk5Zl4972-kT8z603snwkVL11ZeIE5ll_7NgqXg-XJYmOth68UwJ1UoZRtS50mPw-c1UP2Aq-Ct_lMcDfjrxLFptJj8yOZHgCTexQtNVjtB0iFzmjGuTAqpwXcTYI5cQUbo4jKsG-9QcEemT2Nd1_klj1vjrWgaOOq1rtMFp-VFXH5YtkxS6de3jx4xi2HWDnhL-G-yDWioBDdmR55SHjXZQjBMUIGN8lCcHfW8XLW4A4_eNpyj8zZv_X0N9WTCJB9DoFnvQL4kdhO538ZVfST0RTvAqJzF5e0eNWCS6GAT2lwKo2Jmm2PF3jQr92APQA4xvIH8_6mLoeVeyMOgZkmBZXDE3cVkOr94Cossr5h1ovdaEHExWO1PWXssSxZhuFA3vNfN-cSQruh2YCJ29Xb2TIldhpdrXYgR00KhsgO2foVg1tnd4wLuSvvlTRIulFMsYixw8e-7PwkZFY1fKZG1_-sD1IM2JXH9yRPyQC7Fn5-VTvlIZDHdlfR86zHCZYMfCW9MzHSazfeyngkY9kfIreQpLVbrOCgIKKkt0b03aksPg6oIuic6vvczDQy4ePAb9MmvGUAFH7pD6O_rfdbFlaptBjGUrquyILUTmKbSrC6Ae0EJa5jocImzEoSREbRvqOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jiiidtIp7PZ_n5yZSF4mqoGFVViIUKP04_KGtN0zy6g_sJQDkBRKp6qPCOe93xvkHXc7KziS5D8kGfOnjESylTgbSGX1qo3GbkpABfQvYJPO4mlT2rBq-z4OnLoJxAj-pdD5sUT1KLxZbbSkJ6C62QzFgzQXh4yLemmkf7WBYeILBeBO7DJFp__9aU_1_vrfvZCSTbqNJB3M5YEMceowNsS6J9SCjYpCbtGF1bYIiGjatSOlnqLtAgwCaBouDF-Y1Q9JnZzUsm8gUYGd65t1GgZIRfxad8mlQj70j_4lpGoIJD6EG4NeFLWLOFpT_5_AAk-bjBB77ZagbVKgRjfmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fr6dptCiU-zvSjjXvgLQuJu4vQARCNQRPaXEpI_DJUUtO2dsUb9FjsHoFgeA7Q8HiBKcu0DEHShFFdKC-d8nEEx0i9iZUKRmVOvSy6HCEepJFUitmvNffgdOuzuVCOj6aNYWs3dI1UZPTlQokNkfE7MyEZnLqdvOOCjJzE-ghEWhbfYnnAWAOPDgQm_N61H8SsUqmHqFfnRyBntzIGrd0BlqDzRrbN-UwgB9jOex5TAplpntseCFKjTezBt0Dd2aoDUKouCFy4nuZ3PJrd5QJOtaNoPm6UooR_xadWAnBcIqMrNl5AC1MAzBPsPJJf_CtebtMgBuIkMzBEI9raWPPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mv5LXdSOIJ9uka87y0igT2PbAUAbkSLHJBTX5_UFZSZiWxIrqAbaHjtR-fB4roUHjxOOneWsF7h822CnSpms4Eu9ZhzIggMFeOtF2Ktr8MR-mJecruCSmDnV1IbojGjIc0XxSsVSW3aq45EKb8VTzSZuHgyKWwjIne-ybIasEqrDJgkjyQDzyzQ1ICcHAgj5MruqgZykDxVqmt3xXt-wwEhnx3ARMeZQtOVnV8QM45Ag64BaTmvH1UJnMKIdrjXRONhGPU7MIPaMFb3EfKEAS1Y3RzPA2EY_yetZ6wMFyIMMps5Nul-PQ5woTCNaBdif72UycpZ4D2EpQcOgGcMNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akSoKhIbeNWZ6wjqmzx9s7vfR9nLK_mKAcaTeTBJ5OuDPfs2RGCoYy9hGH_Goq20eg4sKK6Wd-jJLAKuPuJY7Juc0BYVD83czYBdHyM9UJVGdtuLLQ8n7S-E_Al6wlU_USTlsCzbieMwJIFf-BA-nJeAM8_7ijGkf4s0SqG5BdV5t_oszueOkEWLP1gUlwKMvdASo7zpJ9nFf2Tx3VRizjYvZWzg-5JGAjIV27z5iYhSl6oQjH8OtjBcqjoc54hHbJ3wY-OBRPaOAnXPzDFnYzGZlBYo4aN8EbYU_hyVqcaKzmpo03ZyO9DZVT8u7BglmWfQ531l3rWpSeayPPf-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHL7eZyayVcUB0Aok3QSBDtkWn-650JlpIsQKJKyux4YUmU3hOQ_ci1y9iA71vMMlAc-2CI7ExBh5i3E4WzZs-skHayGrVxBLx4YQn8S14HfyRJDSO_23pCS5It8-4mhMR6HHAyt1M7d7oHKEB23SQzLOOXUl1uz5ct3Leb2vuTsT14aX-nG3fFb-201JPUi9f-cB6PahgBvnp_5GRtdeRDTcUsduxIiPa17aNcl_0vGWKrYx4c5vIIL4rT1VyDvY6WMaL0ABC4HtPMsmQYj4U99tw40VsiUURK27ZzajH7zV_U2WEl6EusTpGdasrwiBL4WCdb5a-LV9g-3xw5oCQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QiFqNNdMQ_vEQScC6wYR3txY5KCus-y4fyM286CZWlV2ud9cfeu8HbIC4789iIyTqtnz7JSO8NvmPZ7VW-SroSf9IvJbh_fQiPpxPaDuxZnuf7seuuVOQY25DyeVxin4MvMKRO0a0aC5U5SpqtXfTKXKwNE1Sg6WnIEE7u5nfJSbcxt-A8lpfyrQXK-D15EdWy7ljf5Znww4FU65kaRZO3IFOEmhTPC8ocUGwcMSQfEP85cIbYVezgeHOyHTmF-48RMrLp4O-4CqmFWfM-Z2kbyO2UY2gKDG1XGc-WE6xUrXyfphkd9ZQ_WTtg0A2cHdd6TWPXlKgrORI5a4Sg_u3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QiFqNNdMQ_vEQScC6wYR3txY5KCus-y4fyM286CZWlV2ud9cfeu8HbIC4789iIyTqtnz7JSO8NvmPZ7VW-SroSf9IvJbh_fQiPpxPaDuxZnuf7seuuVOQY25DyeVxin4MvMKRO0a0aC5U5SpqtXfTKXKwNE1Sg6WnIEE7u5nfJSbcxt-A8lpfyrQXK-D15EdWy7ljf5Znww4FU65kaRZO3IFOEmhTPC8ocUGwcMSQfEP85cIbYVezgeHOyHTmF-48RMrLp4O-4CqmFWfM-Z2kbyO2UY2gKDG1XGc-WE6xUrXyfphkd9ZQ_WTtg0A2cHdd6TWPXlKgrORI5a4Sg_u3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLkek9g1W2LeWJpG2d68Vh-62Fu-FpngTJOggZezWS-pMcdiXL90NN7_vqnLr4D_ZYfvdSDTmhZuuedC8bOxm_XhfqKEQqObMBTSd3v50gDeNC1dQ60-k6EGiC7ertCe61ArBNMw50DDvih8xnuPX56jSBAoL05-cnR0C5ZVcX2cVsNUnJRfNaFeYzcT785VJ3hSseV4mglmOu7tMlSyXiF7q_Re5z-jk_VdII2tpyDDtUkjgaHMtzQl0bdogFQCVXiEI_l2Gpssq_yc1l05w9ZbDh8iVo23D5LRFvwo7e809pRJEmtumSZQ36y-xEVnVuTUuuT4jOi_LkI8mtzkog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC54pJy8LlU9Tc8a0DIRqoBFPV8F4_UsVxJBGLCf1lpG0n1fBo7aO2fxn6S2NBm1jJSQ71SnYxwyS4_sFpm8MpM8uba6-OT4fWQEYukvoX35TW-TYGorU5zKcXA4FjpdKeuoLx3ySlwetaSRzSwIJXdvvL-EBscUX3J1WyF7i8jnkoQdMg_TYtWEEK5UYDfj48AYVSnTP-0m5yJcdt2dCCtWnagngyo5c27hJJSnz6uvwppRjkRuwXtNUad1jZVkgJL-lyzl11kMOqyYLmtI3ygBV93x9CurG9CjI7fw1pIAlgHZkgR3qavft5krXSqN27i3Sy3zx_1p_MTUTiyBzg.jpg" alt="photo" loading="lazy"/></div>
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
