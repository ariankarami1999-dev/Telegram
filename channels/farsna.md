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
<img src="https://cdn4.telesco.pe/file/MDIU6T8CK08QS04VHiR5X31iLq652x4LxbOPRMTq2RpjQ8rYVUxvH0nxcZm0QfxnUVU6QXEoSjuYm9z458MmBPkq8kfIHuKq3Qx4O7qO-IaLA4mPovXLlff4O6fPLfWsQ7zpuF98vuTSE0Vekbhh-J4-iY2YY4A-UCXvKXLxa_pP6YUpeA5XhzyvBhTM36cfIsGOE4EVDc_GptHDjS3vTQE1xDWD-S04YwqeYMsqgqXkTVFrOhBMn0B3IHuJmdg2C5_ZNFTwuWsx-p8xbc7Taj7Rr4urrtHUzQVlY7uTJBEv9xmA_iDzVtRJYJKWXbvH4cucHoLRK-qGbpxR-AuVQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 08:29:30</div>
<hr>

<div class="tg-post" id="msg-451323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
گزارش زندۀ صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد.
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن آمریکایی به کشورمان است.  @Farsna</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/farsna/451323" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">معاون امنیتی استانداری خوزستان: بامداد امروز آمریکا به یک نقطه در اطراف شهر بندر امام‌خمینی (ره) حمله کرد.
🔹
این حمله تا این لحظه خسارت جانی در پی نداشته و اخبار تکمیلی اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/451322" target="_blank">📅 08:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
همزمان با کویت، منابع عربی از وقوع چندین انفجار در شهر منامه پایتخت بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/451321" target="_blank">📅 08:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
انفجارهای دوباره در کویت
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/451320" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌ کوزران کرمانشاه دوباره لرزید
🔹
به فاصلۀ ۵ دقیقه از زمین‌لرزۀ اول، پس‌لرزۀ دیگری به بزرگی ۵.۷ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/451319" target="_blank">📅 08:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/451318" target="_blank">📅 07:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زلزلۀ ۵.۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵.۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/451317" target="_blank">📅 07:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زلزلۀ ۵.۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵.۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/451316" target="_blank">📅 07:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین به‌صدا درآمد
🔹
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/451315" target="_blank">📅 07:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین به‌صدا درآمد
🔹
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/451314" target="_blank">📅 07:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
قدردانی سپاه از اطلاعات مردم اردن؛ هواپیماهای بزرگ ترابری C17 و هواپیماهای فرماندهی کنترل P8 ارتش متجاوز آمریکا هدف موشک بالستیک قرار گرفت
🔹
سپاه: مردم شریف و ارتشیان مجاهد اردن، با تشکر از همکاری صمیمانه و اطلاعات دقیق شما که موجب هدفگیری دقیق رزمندگان…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451307" target="_blank">📅 06:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دریای خزر تا فردا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را از صبح امروز دوشنبه، تا بعدازظهر فردا سه‌شنبه ۳۰ تیرماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/451306" target="_blank">📅 06:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0J-v2CQNFPJNkrhC-xaNhg5wQLD64Rd_TNiGErggRtJqt51y3YK5wqmN4gpB0BK19-c7T-qqHMQXmRmJieNeMeV3r06wdcmj2g_pskEVkYCLMIMiGdUmUqOdQBed3c1-P8Y_4OoflT0YTMZejxydbvQnOtxsEJSuK7aN6L41ChJ6dnZUb1qLVa0vt_7w2tuoO7Osq4rPiwMjbwwzfhJz7cjDqClEl7LcvuwQKe8phTE8B_C5-80ohsZSQW_34NoHdqOxmC9Ze51aupJFF3-nOBCN850omGj5AQgDgTMjFozHFXTQt98EJ885qEedlJNytSM_Z8GIaTZQmR-xc0OvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من، معلم زبان انگلیسی رهبر شهید بودم
🔹
من که روزگاری سرهنگ بازنشستۀ ارتش شاهنشاهی بودم، در سال ۱۳۵۰ معلم زبان انگلیسی آقای خامنه‌ای شده بودم؛ کسی که او را به‌عنوان یک روحانی «روشنفکر» می‌شناختند.
🔹
اما فقط این آقای خامنه‌ای نبودند که درحال یادگیری بودند؛ من هم از هر فرصتی برای بهره بردن از محضر ایشان استفاده می‌کردم...
🔗
روایت‌های این سرهنگ بازشسته از جوانی رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451305" target="_blank">📅 05:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
خبرگزاری فرانسه: بهای نفت‌خام برنت از ۹۰ دلار در هر بشکه عبور کرد و به بالاترین سطح خود از ژوئن (خرداد) تاکنون رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451304" target="_blank">📅 05:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
سپاه: دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
🔹
اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک‌کش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگۀ هرمز را داشتند منفجر شده و از حرکت باز ماندند. …</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451303" target="_blank">📅 05:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان اسلام آباد غرب
🔹
یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفته نیروی هوافضای سپاه در آسمان اسلام آباد غرب رهگیری و ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451302" target="_blank">📅 05:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور و وزیر نیرو وارد استان بوشهر شدند
محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور و عباس علی‌آبادی، وزیر نیرو، پس از بازدید از مناطق آسیب‌دیده استان هرمزگان در پی حملات اخیر آمریکا، وارد بوشهر شدند.
‌
🔹
این سفر با هدف بررسی میدانی آخرین وضعیت استان‌های جنوبی کشور، ارزیابی خسارت‌های ناشی از حملات اخیر آمریکا و پیگیری روند خدمات‌رسانی و بازسازی زیرساخت‌های آسیب‌دیده انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451301" target="_blank">📅 04:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه دریایی در نزدیکی سواحل عمان خبر داد و اعلام کرد یک شناور در شمال‌غربی منطقه «کمزار» دچار آتش‌سوزی شده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451300" target="_blank">📅 04:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd94dc223c.mp4?token=fVe7HkfGToYL5H6Ui7TUScU6h4RU50PQlWCR_1XheIv18JREY3xzU6KqBVWyPQLh61TBg6WTC-fC_vbUA7MoikDsbh-ObU7jGajChNadymvQv64_oUA_N7lb8Yo8gJqLvQZHv35QilANVOCQgdFd7SoeHXtQv2lK1ZUiD6SfsGIwg2VvoT6hWO5MqjPbm3dac0vhwwO5R9_fi--R1KBjuh4ZeolGR9d3w5CMLlF-vl6RC0wFiITKGERa7K1YRM2CrqR1ucKVNB1QdaRS1gsvCphe8P7NY7MlpZdSUwpzMP5uaQXH1RAsQEN56BrKel5jpYsDPOp8k3hAK_dPglA4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd94dc223c.mp4?token=fVe7HkfGToYL5H6Ui7TUScU6h4RU50PQlWCR_1XheIv18JREY3xzU6KqBVWyPQLh61TBg6WTC-fC_vbUA7MoikDsbh-ObU7jGajChNadymvQv64_oUA_N7lb8Yo8gJqLvQZHv35QilANVOCQgdFd7SoeHXtQv2lK1ZUiD6SfsGIwg2VvoT6hWO5MqjPbm3dac0vhwwO5R9_fi--R1KBjuh4ZeolGR9d3w5CMLlF-vl6RC0wFiITKGERa7K1YRM2CrqR1ucKVNB1QdaRS1gsvCphe8P7NY7MlpZdSUwpzMP5uaQXH1RAsQEN56BrKel5jpYsDPOp8k3hAK_dPglA4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451299" target="_blank">📅 04:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3415729dc6.mp4?token=CWjjGqGgwiCKUtl4j2RJG_EixSbsaOJb1zPUpGGFhCVnL_QuHA7DACujUTxqSfyIey5tgdAv00Rsg2S8VAqaXlU37Z34Tzc-OOXc-31dkScGoYLdSXXuR4_41swvhBfqC7kkUXf6du0tvKEdg5BGi-s6veDYuVjX2fR2Zybr_1B4tNKmGXsUhzgc88gkt-m25uz9HqtP1MfzPhOcydEcKqSPfjfDC0rhMNx9MZwvR06TC4UVzUZO2O9ys1tW8sVSZakB8qfyXqIY8vQWEZkRY8HhnJU3D5MQ30m4xv_lPtd-ern-QeXaFYYpUsS5-eL5d3BPYzqyuxclHuY5TS7ucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3415729dc6.mp4?token=CWjjGqGgwiCKUtl4j2RJG_EixSbsaOJb1zPUpGGFhCVnL_QuHA7DACujUTxqSfyIey5tgdAv00Rsg2S8VAqaXlU37Z34Tzc-OOXc-31dkScGoYLdSXXuR4_41swvhBfqC7kkUXf6du0tvKEdg5BGi-s6veDYuVjX2fR2Zybr_1B4tNKmGXsUhzgc88gkt-m25uz9HqtP1MfzPhOcydEcKqSPfjfDC0rhMNx9MZwvR06TC4UVzUZO2O9ys1tW8sVSZakB8qfyXqIY8vQWEZkRY8HhnJU3D5MQ30m4xv_lPtd-ern-QeXaFYYpUsS5-eL5d3BPYzqyuxclHuY5TS7ucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451298" target="_blank">📅 04:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQHjbQQUBU48qYpMfeVe0gPSh4IbMYh1jzrixBRmw--WE3a4-hNubfz6-U61IWBY1Nd7ZrbpySnDsKjvfOPLvefdlxrBecpI2UXg4lHiVriBxhbLX5qUIZtIs4FcogNRQadFXnAsx4bgU-hVRcx598yCvXaq5TNj0Ne6hZ8EV6lEx7Ap_kjxb2x9KaQvPkN3ZqncgUHMeUjZ_PjtR0FYXjpqSSlOpV3lolRFEbHUf0iPZQ0RGRnjSP_-zNboTTz6_CzPjC1BwUZmTkC4IErItM42feKIikBmVb3N7nlcTVxri9WJqd90GFgf39I0bZg4e4W_JTBK_lOvk8inJKDzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: امشب ضربات سختی به ایران وارد کردیم
🔹
این کار را برای ادای احترام به سه میهن‌پرست بزرگی انجام دادیم که احتمالا جان خود را از دست داده‌اند.
🔹
ایران متحمل خسارات بسیار سنگینی شده است و نمی‌تواند به سلاح هسته‌ای دست یابد.
🔹
دیگر تنها به جلوگیری از دستیابی ایران به برخی توانمندی‌ها اکتفا نمی‌کنیم، بلکه اکنون در حال پایان دادن کامل به این موضوع هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451297" target="_blank">📅 04:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451296">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=eMU53WFnzoVzx0kjrJU0lTsxsp-v5Lruons8lbIS9z6_Pf82IF1TI3drNBEmJfw947T62l_xsLTh0F5RG_i21KOd7WTlLiHipnhjrbJPflLYrbD8fZ7FiNYDWQnbN7Rhmsk4lHuVNoxJcvIdd5mivfrBjYGmMnfXSnU3PAcydikXtHGvm1fSgXvoQHGPK8RMSqUQgtQ16wROgswYpx4OBIA_Xp1I0H2pVCpH7dJcvU2QQUZTKrLd3Binz8fGN0k1XTkEF709sCzxdQDAf2XrRTyyn_qf2wAva26mHP4qbCdARsuRkIh4m-FY30LbxmwTc7OMK7b7NBjLyDk8SpjiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=eMU53WFnzoVzx0kjrJU0lTsxsp-v5Lruons8lbIS9z6_Pf82IF1TI3drNBEmJfw947T62l_xsLTh0F5RG_i21KOd7WTlLiHipnhjrbJPflLYrbD8fZ7FiNYDWQnbN7Rhmsk4lHuVNoxJcvIdd5mivfrBjYGmMnfXSnU3PAcydikXtHGvm1fSgXvoQHGPK8RMSqUQgtQ16wROgswYpx4OBIA_Xp1I0H2pVCpH7dJcvU2QQUZTKrLd3Binz8fGN0k1XTkEF709sCzxdQDAf2XrRTyyn_qf2wAva26mHP4qbCdARsuRkIh4m-FY30LbxmwTc7OMK7b7NBjLyDk8SpjiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
.
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن آمریکایی به کشورمان است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451296" target="_blank">📅 03:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451294" target="_blank">📅 03:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه دریایی در نزدیکی سواحل عمان خبر داد و اعلام کرد یک شناور در شمال‌غربی منطقه «کمزار» دچار آتش‌سوزی شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451293" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451292" target="_blank">📅 03:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451291">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
رسانه‌های عربی: انفجارهای شدیدی در امارات رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451291" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در ماهشهر و بندر امام خمینی
🔹
دقایقی پیش مردم در ماهشهر و بندر امام خمینی صدای چند انفجار شنيدند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451290" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کنارک و چابهار
🔹
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451289" target="_blank">📅 03:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451288">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سازمان تروریستی سنتکام: برای نهمین شب متوالی حمله به خاک ایران را آغاز کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451288" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd98ab8a9d.mp4?token=ef3MFq6AltGHVF7_yt0HNj0hz3dslrBUjmGPDRlGA3AifeEDw9TT5texkzGk2etbksAp2_q8IHp3E7D79OK8QG7fT6Bg0pfG65cOPfUGCxWW3rKCbgq-7wInel8XkfSBq933UgGQ5cfJS1L2mx-3hUIY_fXxvEJsmcPm_wQYguOeRveQGzJAkwbbm0LrlL_KF14D-qkN0oYZmGGxVx162yS2QFFnhP1nJAgbEuqskmZHiEDzvPruqsx2-5CFchEwrbBhud1Nvf_6jDNwA7GSNZaFYbrwDJAUNtCsuyTm7JJLnT67XBpZghyIdQnoo1VThLbJXP6_qnmN2AjUAkJ1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd98ab8a9d.mp4?token=ef3MFq6AltGHVF7_yt0HNj0hz3dslrBUjmGPDRlGA3AifeEDw9TT5texkzGk2etbksAp2_q8IHp3E7D79OK8QG7fT6Bg0pfG65cOPfUGCxWW3rKCbgq-7wInel8XkfSBq933UgGQ5cfJS1L2mx-3hUIY_fXxvEJsmcPm_wQYguOeRveQGzJAkwbbm0LrlL_KF14D-qkN0oYZmGGxVx162yS2QFFnhP1nJAgbEuqskmZHiEDzvPruqsx2-5CFchEwrbBhud1Nvf_6jDNwA7GSNZaFYbrwDJAUNtCsuyTm7JJLnT67XBpZghyIdQnoo1VThLbJXP6_qnmN2AjUAkJ1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن قهرمانی اسپانیا و شکست آرژانتین در ضاحیۀ بیروت
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451286" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehq-Xy7jlXGKWLj_DtoLFl-w6u9pMiljHXeFs70vABg8-h3Ob-UFfHqP8QJ_2V9yBRgwTND4N2Tqa4TXr1BCxWzkPXLKb4oHIL7vL4aQ_GAtkusD6QzyEi11T_iyUVxQHIw-Y0f8bOfXca1su07SbhMrpCE9yJDNc1JqahQFVjCxiajqzVZvohUfLXYXZAhHrERr3lJmiEpD6Lq2J5-gR41Wop3h6l5-m0i5jErvFbHjB2JbypDYMOp4rWlY23p1X4qIdie2o0qzMXJaMfNQDV_XhuGpbMX9A2eXD8SI5NNCp932Jl3jO6q2QGm3v3rQoTnxQgdBZUFln6AcGKlMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJFc6JU3q1u4F6HWVd4guS1OEcqR1QNg0YF6v_CPUllM0dI0qLZePoCUECHfiOfSiqmLl6IV78CYCw2_vXVdKhHXFACHTmpvTaK0Gt-z0KJ5PvDm0OoMBdYsobc7Pb0_JSk_KDPDZU3jj2Yn7-2NbLztc5Mo5nxi9DbsuwXCNz71dofMymi1mWrIXE4KqQ6q45zYCTCYpSaV7p2_NinP8-JX7KGf6J-6f1brMiB36pKPZWrTMNEpn2Qw_89Iu6QBrwOHZA2OwmoAl-O_RwB-wXQK5wIO7qWZlECWYl8-KtLtZxkS6aaz-2nD6JeF36n-gn66Ow75sENEftJ7GFyknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVwxoZovyMm7hhc-kN1240tRpa-kELgub6VADmsnjHYcBGjLQxMhflu8Ps8y6PSXZoCAtxQvsJUR9QdtdoK6Hg4zG9TcQFoEQFGZPubAAl1ilGyfzIgmQVQCqJdFC8n0lo-kgxZXnYSAr7aTU2fs6f9ev9nhNSBN8UhUryTF9xGVcUa9C6IC3XgtYMTqZj5EGrJ6aD_f3QcVaIjoGBI47KvNw_GtNL5LwG_HzKV6TQDCv7TLNKDeTgpZjEhOmFs5vGE2rOgDQBWSgZJph_40Nou5KVPC5eEDEFzubBZnHvO2QX6sWEWXmRwSHNExiPIBaIYv1K2yY1F7s9l9uayPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKDp7zSbBSMp5j04C9v2vxoMIFP9rZ_A_i6YyPZFmmQr7Cilg6HYvbWCRqSfcPgaSHUuEC-zGf-mOPqQmakdh-ejmcv5grICDJaFCMQTT3jlBv8nco9VYdkOMgYpePqtsP1LJMZ-WkLpTR9vkt4WTJvwljhmOez4NJSEPG5xEmgKZH-kRFwEI85GF-pBlfAfbSpnHxUcA-rhW85hAD2oLHEKEUBqu0GJBfryogBrnOufJ_adAq9ZloKOPThIjEThDT3nDDg3rTBAFiFH_xPp1RgGM-LEci2942zMVlvvFyzquXAOsSxSy1wkrAoi7-kF3PObQtm1RQB5hW-oVRGYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPnESLkWsghmtTNZ5Dm1cNOfSerQeWXbF8YPCy2WMEDUI9YFhdCVPwLDElvLhbygBnaPk6ZbVAmINdvLLWORfdzYFMyevxHSj_3U0lyHLWpPASfTGEEepYEFIOGBM_766A5Yym856rZej_5aA7shnWqlu2FoXOn9LPsCPQBv0Pm2JsBa8DNZmUPpnaTjJipIw7J7zuLfOawBCSYTYQs1_fhNK2DcKHeZjHWm86b-gCEfjmxO9hNY5Cvcn9hZ-yPptGYKWpq25CxlUovce62oZ-BaFxsMqmGOtNtW79Phexcg3SbG4Llcf6cOCBwQeHEhIYH39_oBLOgTRG6H5YWcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBatjrOdPwfS2LLY-wKamv3FtzlNGI-WmU5p4AqyhonDD80HK5xmpXYwL2u57uAdc9kPi7JNH2xx1g1SMduOSWOad4orMRwAcl0UkO13D50s7smCnPMf39wS61Ia-ks4SpCahWYwS82GfWe-H9209GO0AdEwlcXYCkkJgAZ189TcSKgyHaNINLoLZBfYRdoIh7S8-ivYoMktshsXN5te9XSaMbxV1S84Oumcn8nolMa5law8qjYZBaPKOhN9AXhabWHdlbVaneZqTDYSlWhhXUH6XLQ1CaK7Ze66cKrPbCb4rLJ1ytoEBhpM0gqaTmUaGpKqVzLJtJEnBRXgucC0BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سرخیِ پرچم‌ها در صدوچهل‌ویکمین ایستگاهِ خون‌خواهی رهبر شهید در شهرکرد
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451280" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsST8N_GSG91oAcQ7TMOZXp-WQkBNXx6aI0epGPTa7LFzMeSDXyMm7U0Mj5y1OEyXOjZ8_6HEbUiV5TIDJkRkoLSlJBkmaHHwmgpm-2-YAPpu3uVWGhYbx2paRvI5WQSlWvGH-TfjO8HpoSFY4YLe46E7qAwaSPlUAuubI6J12dtafIk3Yf1SaVpRvuvDHQ2wDW4ezN6N8ktdTaX3rH6VEZIlFRP_vEifS3nJjJwms2KKnI0eyO8_mQFMzMaotVVx_JP3Is3du-5YJZa_GoxPhAFSGcFYw9NYPcVyFTBjMQgZyQQKX86Glf6tqVmQtPbBR5zHL_gEQwQLXjbHJV73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBvQw6hlQMsjxV1SaImkvonxxpE-Qp2sN3y4EN5y_8Oo_wGisADC1edGdYb-hVa1xcJm8p2t3Yu82slxxqcljLEzcvpliKccpswcFpJq9uEmXKnufM7xaSOtQX9zJtPL5_AnHDgkSodet9RReVbgQQYpAB2CkvsJ0ArJ1M3ZtZXQRAkUPEymc_dG2jplbETzYUbfuFv-h8Ops2wV_IjGbAB8AIdJ5RNAABaiUoJ0PgbPutsua8Y3U_C2h1vC8NtHiPGrahIQH6MPHdcc8Z_xAWUMZtXDrxnjf7JPyhttoxmqsFd2i7Tb2xMkLpRWai9raBW69tvtbNe5zaHs4X_BIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQkE8qdU6atXUE4baVVBnIPSVfbfIXyiRZDPM0fJK8QEEmnwvXpRxOKIMV8UoBlUbGugAWtkCFurwsmiADRdFnEoBRHFBzTy0tkW0Ch5Mezt01S-lTfV95_0HvUbmafbG7wx7KDRwaUE68uWyCeJMQNr9R0q22pExRLyjH6sRmWZPa4CoMr33B-kXbC690qA6kofD8-EP-o4LjYSCXg0J3G7XxRNa5HkA5lbI1pBMZjjvz6RuztSsJSIjgTSkRWyVCq4iz5p2uOmK_q_TRKofNARQeTnfEd98F4WR8xFKRB9atSMejCp1-s-kGhvgqeHzQbcY_5QYvMX2ewGuppmgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بالا بردن جام قهرمانی توسط رودری
@Sportfars</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451277" target="_blank">📅 02:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
منابع عربی: پایگاه‌های آمریکایی در بحرین دوباره مورد حمله قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451276" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451275">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
منابع خبری از به‌صدا درآمدن آژیر هشدار، و وقوع انفجار در پایگاه‌های آمریکا در بحرین گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451275" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451274">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f565906dd1.mp4?token=YR-Np5S2ogJWL9WESXvZmWKS3j8NFuVS3P1Nj2vQyUJuLAeA8jL_4hmNi2aPust01c-xZG4x9C0z7YqVZxnIN0QkPvJEbi0QOwCpKi-QZC8srNG4lbz5Oz7qZ3wbzWrJOsmzCmp4jpDl_mLBJvg9dq9y2a3-f_FHvzO4PIRDfw2-4W2ByFAA0UvvYw5gCEx3I2JLqQJYVXKVv6JGuT0I-T_6fEgY3s6MmcT4BBrWAvXQZUFcNDfo9z9CUxzS5V5YfmdgV1Hh74cPBFxWoLc1FhtNmULSN4LDfYzn0utN4ELigf3MDSdYb5c1xvcdnodqyTFeMJ6Fbxj8jfrFYpsfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f565906dd1.mp4?token=YR-Np5S2ogJWL9WESXvZmWKS3j8NFuVS3P1Nj2vQyUJuLAeA8jL_4hmNi2aPust01c-xZG4x9C0z7YqVZxnIN0QkPvJEbi0QOwCpKi-QZC8srNG4lbz5Oz7qZ3wbzWrJOsmzCmp4jpDl_mLBJvg9dq9y2a3-f_FHvzO4PIRDfw2-4W2ByFAA0UvvYw5gCEx3I2JLqQJYVXKVv6JGuT0I-T_6fEgY3s6MmcT4BBrWAvXQZUFcNDfo9z9CUxzS5V5YfmdgV1Hh74cPBFxWoLc1FhtNmULSN4LDfYzn0utN4ELigf3MDSdYb5c1xvcdnodqyTFeMJ6Fbxj8jfrFYpsfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهالی تنگۀ هرمز در شب ۱۴۱ حضور در میدان خیابان: وای اگر خامنه‌ای حکم جهادم دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451274" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451269">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2j0gxlxmOAHndleXr9hKw8Cr-au8oC7XkSPAqFRevlAHzh6e0WmkP4c1qTFtfAXoCnyE2K5IS38i5zAZ8-nhEf9sy6zNyXBzJNz_ELV-T6DoEwc-TetpXr_gBkWwWqwNYzmtHVWGcZneytCpkIzlQb00zci1MJNJ20CQvQb2gJOU3ZWN_a472JJeUqmgXUwymGYLCfJyLCRWyuniAyNROpn5mJFOrhhF_uGrIS1PvQEigPeH_MPuRJm5TQTIoPFYJRvbUC_KbHWIMpbH_wvX49Bs1T_eaFNbskRGyVPpLJ8l2-bvay6igUGuHEh3yIDd3QRJi8Rv9uEPsIoGiVysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_FBNM8WOOmVHBPpD20UvH_OIPQ1mGFUTXAZjyOecGtoYghoPoVebi-VmhLwrKodOImcltjHvHmQTWEYUVILlMYMBTWEGL98MmB4doaPS7EHbI7b_kUq1kvi2ae1_iGTTU4nRWwQ6QrOGE_xpma0CU-d-DU4ZavNBURT7rINGmqiMEUWZz63fWi5dMcu-P0ok0i9ZoYd3lIw95VyxjVsBwah1d1i2UrHMG7bXNbI4S8tfUyIyKCZOaPkbw9qSmKTWPT1vHUS9LPgpKozEpC8r9ajVHoEo397u2zgw5fnPSaMLVAg8JOCpqMpdUFG4M_GI7c4wc3QR2d9rxlrMeF4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPQVdOyX-9sNWKYZS-TbayS0vU1geuWIx8tTfa_RHzlFM9tDd8sOYRU2uneeZMfBGDYAFxPi9PFkyYsEI4lfIpkXRzB9t83WTKVfQEa0TSWqj6s2p5OlWF2yLsyLm57PegHw3jkqZyh46a60DJ34h6wuPikvrXMOM6dWg6_SSv3qCJovIHBp-z23X45O0B-OGyVcwpm_Ko3_ltlNcJ0HzNYZ-EOonCgJ8lA6bZGHBKDF7qdc5JzuD-tsD1HyLVZ0SuqVYOXYEBrr4aT9W-5Qq9s16VX2zlW6skKRoE3z9OHcyseP8roBxACQhxqydVePwlL_JfOdoB2V5zt4EQLtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quUGS5PlFYMnnPBtJJ_g2SWdcimBxcHshdr9unGRIlESiNOkkT--y1UvUAIMGn7J1qsP_iVDMdF1ECwKnwIgdLbmOcQn15ebbWKWYSR6cf2TN8nCEjrdTgaMIwVLp-Zo36e7Q7sUCLR88xiLGhYQrRsK41Yw3RxJ4GE6gXCMppu8rkHDVpS0mAo8LpOBnbXcRswEujepkRfivTa6pEh_kWCOAGsQXzlmrS32KyNtsZol1glDJ1krtRA2H2mAt7SfLS-7AGJPap6HS2i_KSsKNjoKah5XAxjt5u0R3LO8wGy89ZV7kfakiFGQp8q6qA-CcF7s9iLpytv8rZPq80QDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8sChhu90uFPQAVQY10PCbUh4pp7D8SzlFKAnoSgl9AkTDp4K-aR9Ahni_0vWnmHtEaQG-oc8W9JYso_PhvUCCCW6SX-JkxD-9U2ueWWM4nyuG6njSo9P6k371Zgdo-124lmmyjY7r1Ui0ZMhAsZhKtNKEk-7UwIljDNuxxZ96m4Q9PnaBm3WTR9JIX4AuJ3JmaPAjCXHHAb-NrM_1Ir-cdPWZMbVquQbak2-xPznyV9Wjsr18YrTfHwBrdxzSQjOOcts0EhcsQtizPh9zSJCerME91MYqDR37W6ZqQ1vrajHXgwKTt5p8q4YXD7BOduKGgKvrSCwSNEO640smecEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر فتوشاپی از عکس معروف مسی و یامال، پس از قهرمانی اسپانیا در جام جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451269" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451268">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌‌
🔴
منابع محلی: پایگاه‌های نظامی آمریکا در کویت مورد حملات پهپادهای انتحاری قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451268" target="_blank">📅 02:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451267">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
رسانه‌های عربی از شنیده‌شدن صدای دست‌کم ۲ انفجار در کویت خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451267" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451266">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
رسانه‌های عربی از شنیده‌شدن صدای دست‌کم ۲ انفجار در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451266" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILCAMEqmBphed0OP6Nt8Kuei6tSty9BEPwho9q5_61FDJeJeVC4U3YE3le_cHIKEsUDJHp8uuoDME91WOgSxVsoqdruAYg3yStfshASiZMt-y58vAOftP2_cnrnehTF1Mmgz4WL5wF60Ouk7w9xwV0qSzaahMtV487ieaAzS0BvnxQ8DeK50KnfLqMhYFLTvr0I2Mn1YWz4zoKei5Yie8e6UeXOgf2CXD5EDK5mB5LfXfcjUmKs3gYU6iOEsyz9Yg4oQDL0BMQ3wu7S4bZ3bOJcU1egaSmiY7fdYiQ1U8LntvSuoYGGI-39AfhcE7Ms5XNUI-N26lUQ0TCIqHDwHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb67WtIqFi8Y9vrT3bjj04EuFfaQ_H6O0zyy2FmhehrKGZqmFAJhtnl5YlhyJGbX6lCqI0RjQxyj3kCSPN7s7sXdegH9TxcS6IfPbEBUV_0FoY_0nQh1jT5_Q80lKsX7qbjXgUT5fZOI986ABPqFYbZirw7QNoQBrNemzCCk8rgGoP6HE27wZQvvDkR4uE43uiYuuueTzjjqS2yEZM7Qdu6j9QQdJJg4Xol8UEnL5ow6h4uEEnzcSnMWHMQlGNDThwXWpbegWNxqX9-bQOgauvdb9ZDJa6NZyhWEvA3BKvNO7NN_K-D-VVKeQjbBHmZTPxMqN-AznjrryVBIiYSM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm9QBkpyucLNKS4pphciGMYrYktlm-AtOwRg9A05rYOuCvswI7l_0Ga47Sci0aSNglaCMzUHHp30_m9J47O7joBZvQWxR7kEJw8cUNMk3CXOOALsHJykzOc9eZlmRH0UbVg2q4AJO1vKHu-2DYIrJFhEw_Ds4onlCZnrEjvVPU4JLHF3heY-X1LMHhDTI3FS0eSyeuq0cpSgq5IkdSuVNqzo8JOc5WOaYYl-SGQm9Jqy69e1jJVMG7JU8dDvq44OwQhPIyyocrw6OjS_OqoKKiT2XB9SpSEr-z5C94TaldadrJlVOTZvN7UQa-wIAgFY4w8nG7Bok93sQQ8ZdA5YHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiZZ-BfWkKtZzvyryRm_5wlTtd6t0je2jEne0uIB3QNx7-sTEGMSd98fnE1ySGQy7s2OByZSTd3G_cca2lDGnQpEFmeqTF3GRh654-6hRq9z3uU2L915Dl0EpeuynsdKuzTEJcsG1n_0Z89zPCPl6CZfsRH3bwZoU1jadKJmbQq40Z4ygqIniCG9rOduTejcN8n-DRQRIL1HEdFOy374dn4laT9mFDQBD7_VPphBQ2-CdwS8TqG2nSnkcvKV7DENq7yMcucvRfp-KAhAhSVnXQKvrr8vbgsF2WKnyWV1sYl8MRN-8jElRgXKgavBcq3Pr2rYvVu9wi-f5KA1mDXfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMg2gTu1x_NL9Fwb6jYNhG9DSH7VciDGJWCiknH9VSBpnQ_dR-wglG3nnzd_uN9R4kgBZvzB8W_DmJ5Mrfov-JQxI5ybEGjVZurO2AqCNGapoh8RKzIeBi1ezgQ4IwSnCQNZ0jO8LcueDfGAwZ6dwNkYNPTeqUA8f3UmitrzEYbeRyPgfSbBxQssKPQ5P18XWotHq6xeQ0FwjbQaReS6a-ybmaW7K5o4xEgn4TFWHQK8LFeXflJRQT5rN9mTsK3dDh9TTNAQg7rldIJ9weQZHNNksHVPv4NDHH0TQekNt2eLqo0qby9aSYY-JXV9v1sy-boGIQrwKlXesNXZ5zCm5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451261" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451251">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS67bNa3QGhbo4U5aiwI2c5nENqvoRoKd5ZfNvmqQtH00qLAYtankgbDlNsrmHPIeJUIiL3ReOilcF-qe0jC4fDSu6SX5Y9zdHDRBhv5mUzFND-y3K2f4Lup8EQFYKoPJO2yh1HL_pr2AkNf9x4hpWkICLjIkP_fXJdEQZM8x_NFrEhxvR_4pLruPca1y15AVh4JKNGuB70X7rplS8VG7ynY56yHbJ_fHBEbBJUN0AEixIn-SOuCXQXSOgycpVaacLyqbFIBwYuAftz5A-g8lyA_NiP0FvX4uJm9JXcHknaYRAfM0TFr69FRiEax1Q_M8y7v0467Ml5i7bZygA90dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-qeIzJWpUweU_AVuyZCrn3-tgx1m7kIz16xK1AzGGoWV1VrR3dXDiEAjgV71btTTQ9wHjif7BVmJFk0C1OdLxPjlYTbhPOX8EkKRmF1O-6ZJPDqWH0SPZff5lWhu9AnkED1ivrCSDYpvYEx2EGXY3HavaxwT6fWWThAv9kMdyliKQmKHyKUL0wo6nImqv0AalDd-1IdVkS-JBpS9C343tOq6xZceCuwnRUI2VbyrK6TVZKmgkUWcGMsCb_xKwFuJCNPjlKXDe4Ow6rnrHGa1RgaJFEE6Q9KtClGyQyBDS4yqBw75IMQTN7p6qteZRo93RuOQJx1CB0BqAGAKu-cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dihOciHSBXw0bHe8Mxtd4Bw0bXsHc-3jUkHyLytfZStV7rFqr2-mHZzHLFjYFT__nX5usL0Xra4Gc5GmlOSfs_CMTQ5jSH3Zm56ZxWJ0LQyQzgfOd5Z1TudUkxxVP0vpFBgVJNSCQUVq_T2qTGTQBJf8LGrD4RSU9i3xgvNhCavLvnFe3mKsqX0Q1VUMCi5bkFwCi3cIuRyR4QrRMQUU6oBD-CwmZ3IZRCtOfGVPtHKSMjpoMVxtS3D5RETbj4CyLqkq7g7ouzKPvD0JiFXy8LYsOS9r74E8Ngfku2BuVb5VX2UI2rYXhl0YH2VCcqclhN-Pu38gsHNUBCKJmHxTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWRz6Zco5hQP54V1ZbZJMsSi_HeyauszHeuKPzkoPwzymx1PhG4xyxTS-eMgHOx7pgt9P8hEY04r9SDSaF8TucKdqdMmU8LPjO58n175WFMkJeFERAlPz2da1B6aH8f1LuN-nFskZK-edkUEGdTKfyuewd8fgntQ7RyAHbmHI4-okbbWD9BiPJ-ZLezPJzBsazEzZxzZ2b6WyusK9wQ9CF6Bofi3eXY1vxcorLSVXygeVn9u9W6iqKEto5IsXn6_8CL_pOMKdMIerk76K_9tUlOOIZ7dWeEZmE75adPCVZcZF9inSbYNLaPDNrJSUSG2B17uz41eWhuHQfu7WazSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHnAfEpiqmETsTIDn6Qj2U-lRB5AbpICBngj3dNSL2sV6NupSVbxFtduqLmDSHQmwpIAmdyH_U3PZe348I3G9GQI6rgN5N_C027nikddxRnv2NTMSzIDeyq_V2fS1O8CNfVCD8MKocSGsxrlbf8ZLbpy-00UwBnz7NHHO6nNQYrSCB-f4_5fQRj4iD_UhbpDoQ6GBMogzZuOlgiOS34UCMyVBA7f082EatxPHyNr9eOaIEHEFvGoqeUITnsgQ28NwxjH7EKDe3nTPj5C4iPSRguWBYIcR46X7p4_fK_eWHOdLdbwcFgdPnzz4tLQ5vYTc1yLe9CrzgE8CmnrFtAdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHWIcyVSnN2_zPGD1xHVKnHErd2huu_g5CYg8QgJsPYNJ3wI-M9bgEqURYYCfN93OYqlCwNgzQgXgV5xt8ETt1EiIk2OQeJW5dOpaKoJsaa0aSy2l1y_vtInXS2dc9ewsZNEeGWG3j8KwalB_ZltF_BI6gEk8Jc-qiX77zeHSDfkSXCK786uwosWAYEPuQswNZPOOhPMQgfGJYsDs4MflAQ_ZkExEYpTwmcfvHsa42Ttn8ne-89wLoD8Y36xE7pW4reyi1S8qQshW9tKp0FTgUAFm9FLtYcX2qdLc_IPie_8n2RhrFIl-os0YQL9PIDN3q76eOLhmPlaWoEfH8QgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elYHkwSkdiVchzD-geMaUKYcfnY-Sk73st48GOkm9NJrY2EGuvJAMGEcKlUkXnb38X7Y47jWSoidgc5734a0EbWigQLGdnmJRcLIKtytD4NBehbM8HPn9bkbzFK_lz-vzL-yiqt4XXU3QWZmiZMZXJYIE6aTtjZBh_11WxatzJ_rrEzSArubuuGgJxfzl0SKFncbzx8PeImpqbisQCFP8L2yQ19XK6wZ9OWc4-TpiLyPut4z9cqENpmVPU7JVgFvTpTNlOPqO0ymf6IDOyh1K8-BDeAPYYQl_DvTQPG8TcNffFrqC8C9bmG3nIvKlCCKoIIFIpfq8bd6Re9O-JBJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rO2kUSf3gl9th6efJcUZmo4aR05jRKIxH7m8X0AIuBPtB4iHwdujBCK3uWC0eyrGoHPnAL7Z8jeXWxxFV8fwEM2nUYxmUs5Li2ZvPr8bTahW309f48tviN50XQIE6pYEFEg-IgR1O9jawizHOcl4vCkAwAXsqMmJdPETbhyOs9MQUFc61Bg9dY1D4zmG9uFcp6MG3LePE7cQtg5hdT8wn0t1XtRNLwfNzELGyYvZvsTGz_X-yCqHDjZTZzz-4TRhBuzxuHVnYfblh7rHNJN9p4epRdDj3Ntwb9zE6Q70UPcFaqKrdyUsbcRjkNItSxHZ8AJXVGndMutv65RTvxDIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVX5pYqpKndyCNvQbkCrZ6lMbLO7-DNaHuMVPQvKR1-QP2GFo0fdTqP_9HpMcs6KXXMc2DMh3kJjHu0SFrM35TxdVj-kxwPwdK94JQYp0GxdEMoqH2lcL5oq93He0W-cPIh1m_7RL9eRD3naY0Uj6O5fUXRuxrBX61YmTsvaZfM0lkpgxnPTkhAB2TmnwKfdoZ0WKbin5ojfHhZZiYjO7tudhdER0fYjF3hFGkFkv9W2F7zxP5QBScV9ci04OXBj5Yjkgbaybw_8atiNoRr9H1lNM7Daxye5kUFUKx4hSXHa-oUPjDE8wAefBur6CMSyJUsfdrUK3zPtwiOMngOYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njGGWpC_RmniCkEZaVTTLjtHfcK6kZDUbU0zIZDVv_BG9OKL_FIpfRGYIGOXXEWrDRArzrBoVNdA3JfeLfY2oGVCSms0jlPH1_mrzTEBDX0dQKHFgE-cDjoh7jGrXSn30OpB20g8e_DHMTBFeEK48cp2BEuDsirF1aQZUguycKgbo1Chy2D-gJu5ZQK60yltr6eFQn4Fecq2xbLbvwoYObV29sD071BcOk0J2NAnCTCMEbIUHoJRP6N6Z39iUjM6MpiqDvXzXCRnOiGeZYxJIN9QtL0jEK01Hnk3VPzkevVdgFe1KAU6MgaLm7NyAMqUVXUuVHCx4yBsIkb9eDo5mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451251" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451250">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCaO1OryniJKRSFWg0grFT_KmyDIdWJO0nX4c_bny-OGvGFzP6GS7-8B6ZdAkxgZuGMrnRmokehk7ZvwLu3J8rsJL8rinFZE7Rm-emJiNydCeN_jOYlK4xjqxx_X6RvLOvnev3aFMwxkDhnyizKzCME-bptWAZ5OS6Ue3qVr5wzeGo6yN362MGHIuD0eaTYw_3SRCR98kMUxc7ulpFJfEvWXVkX3UbBifMMkJSEYSrFUYdE8jR986Bq_6W8drnSRqirkHfchpCK_jvhekIqRoaIxiWQDpjCKCNbUWj2tjBzrME_pT_wY3mh-5xf2xY0M1IeVIRd4BAs-nHQmmdIljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر فیفا برای قهرمانی اسپانیا در جام جهانی ۲۰۲۶  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451250" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451249">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxT0BsxPxMEp4ZpB8qdDs67CEU1I3ufPmtN30Z3RIzWK-1F5ABD-nd2OxaiELJAUuRTJA-90Uz5h5jDl_fDVigF6TLN_jAdfTj3EPw38msD1cLQZNc3wVXw8_bjBvTYnIgQO9rl9CHgwde_3yqH-SDcPNPv2Sc2M3MWOuIsoCV51huajh77fWLrvuTTqXbaY6KtNbGMQMgIHR25x404ChLZAX5okVSN7ThBBHLsUpy_x0EFGIt2TsNTF6Xwb4cT2CUC5TNuKGL7ebdkfa0tJ9Yc3xZUMJoiXFAvyivA9MMywfP-gBLkR1yjjX3_CrtZq1hWQ-pOIoTa1W_6--hOmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یامال پس از بازی مسی را در آغوش گرفت
@Sportfars</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451249" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451248">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1NOI8LZDVhChIWIy5iw3Dc0UFI8ZgycmVgLZwWSNRnMgb0zHeLHOzZvF8fvChBWKmw4v5uLmxwxVMKZSUoZGqNUDdwy4ElI-fPeuNu79cgG3FarIQ9GMXVnIaRl2eQzGejFEwG8jDDJv0gPR3dNKcpJDEIzO97vK2mt-wRuxeQg7waVpT8seQHvKT9_v8XQWPsJLwLTAMYGsPDtGlTp1P4DZY0VDKwnGZHh9ysPlxz8ftiCYQGagt3ttrfJIThmQP9KIELoxVG4v0djtQDiTHvN04uTd8odHQ4BndVUNOPdftoBO5l4k4KmMF5KwQ-s4PHJnZk0DxlOEm2Fmg__GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسرت مسی پس از نرسیدن به جام  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451248" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451247">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/715b127338.mp4?token=kd5JqqBieJBR_Ullst8USeyR_ibca2ztMkMUDHxN_RTq-azhrZ6mstvtHIkJSKiDN2DAypaRLXkygDXeTVCE-oNRSgcCHL_11Dz0N98hk-XXfta2kbKR21ZX-3AW_WW7Ci9P27iOAtXpLKOl6fQ5xuxe4cH3J1bAc7wq6z889g0xwuMRe7L3brIQ7vTU4AdFPKLnkmp3dnS8mtidYXR04uc_SP1nfBGqrqU83558Ms_ExeLQGG89bbFRlP4akwnMXIGgQmh0T0t-CZL6Kclb4ELFuJogRs3C1eWwdpm2jPUSnbeG1tMwYo7-48iZBJfjCeG8nNv9TE3U2mjVcpMWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/715b127338.mp4?token=kd5JqqBieJBR_Ullst8USeyR_ibca2ztMkMUDHxN_RTq-azhrZ6mstvtHIkJSKiDN2DAypaRLXkygDXeTVCE-oNRSgcCHL_11Dz0N98hk-XXfta2kbKR21ZX-3AW_WW7Ci9P27iOAtXpLKOl6fQ5xuxe4cH3J1bAc7wq6z889g0xwuMRe7L3brIQ7vTU4AdFPKLnkmp3dnS8mtidYXR04uc_SP1nfBGqrqU83558Ms_ExeLQGG89bbFRlP4akwnMXIGgQmh0T0t-CZL6Kclb4ELFuJogRs3C1eWwdpm2jPUSnbeG1tMwYo7-48iZBJfjCeG8nNv9TE3U2mjVcpMWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالی اسپانیایی‌ها بعد از سوت پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451247" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef11a7213.mp4?token=vvi2cXk7-e3BBF8W21d52jpAQ-Sa1yM-DmX7uPYv_cclkf9d2sS-zQFNsitMXSkl6bbthHMbKf3Pyy3OcTjZgZjr9UZ7Dn_TCO3RSIrnh721tAR1GBxEDzT7DU0fi0-aUh4kgiyuHsvBGjzRW7vwf7_jRCbnFQc-HYPJVU_xF8PDH5GzYb7Jy-Rs7hf3RT6A_nbZ1hnaDCvrdFAgxlDA5xoaBNktwINgfyal82CfOd5XPPVXO_-M_6-sE1LKct3szsPK9Sf7rIyHmxwpt7YYxYSigjOAcygsTZteWRTimAfyJC6QHXtJJjiD5R6iHEGuy98ioBI4j-vvAHZvNEtAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef11a7213.mp4?token=vvi2cXk7-e3BBF8W21d52jpAQ-Sa1yM-DmX7uPYv_cclkf9d2sS-zQFNsitMXSkl6bbthHMbKf3Pyy3OcTjZgZjr9UZ7Dn_TCO3RSIrnh721tAR1GBxEDzT7DU0fi0-aUh4kgiyuHsvBGjzRW7vwf7_jRCbnFQc-HYPJVU_xF8PDH5GzYb7Jy-Rs7hf3RT6A_nbZ1hnaDCvrdFAgxlDA5xoaBNktwINgfyal82CfOd5XPPVXO_-M_6-sE1LKct3szsPK9Sf7rIyHmxwpt7YYxYSigjOAcygsTZteWRTimAfyJC6QHXtJJjiD5R6iHEGuy98ioBI4j-vvAHZvNEtAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا فاتح جام‌جهانی فوتبال شد
⚽️
اسپانیا ۱ - ۰ آرژانتین  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451246" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuXEXGa5pvckU71A364m3I67FXWU6UCD1hRc7bvbF1m45IhGVM3xO1bQ7loE3_IOor7mRJywqntGZChBMv5w2RUSxis5hfEOiFoArqIF4sD6EJ_fash2prturV2IaV_samDmVSmU_yZuZCwexH42GLsgJa3aYu8VgRHKC9yem73-aHT4PaMhqKDeXymLMQdqzdQgYefdbemc_KRwb3kpufEoA9SjQ4rKR62uzD-vIc2s9OLm4AAn6ccZs0H8M-gsTiLc0W0jn9jhXyGKb4ykxlvN7xhuF-d515oEtYb6jvGuGSgMcNbjGiEOArVoWTKZQg3jHv2sPCRlLBTrQNLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آرژانتینی‌ها این‌بار خودشان توپ را بیرون زدند  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451245" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46057c427c.mp4?token=MzWlpLoRGHQbNND3yVdrjKQquyEMEeJFwWM82lMCgQkqxSAAjEQI5XqkbLs-5IUa2SBpls2qAcGkCvL-aHHD4kGJCc8zb8rM1o5kv3gV4NaFrk4IUdrN6WbguI1b_43sTrtF2iYS8sXeDTFA4GDUfJIxg9oWL3U1isVmTl4Th69hJXOgxU_Rg0hkQriOLpgko6ahd1fy8r-s0MXwZci-UGtIPI8s48KDapoaHB4vVRPla4b63ifbYzjhSMS69rh5XG6XJG9yOrHnLe5aqEeugchxykv5VhadmQKdJhb2S2KM5IYY0lgyoitoMM2dOH5qATqXtfyIf04Y-IV_fy8zIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46057c427c.mp4?token=MzWlpLoRGHQbNND3yVdrjKQquyEMEeJFwWM82lMCgQkqxSAAjEQI5XqkbLs-5IUa2SBpls2qAcGkCvL-aHHD4kGJCc8zb8rM1o5kv3gV4NaFrk4IUdrN6WbguI1b_43sTrtF2iYS8sXeDTFA4GDUfJIxg9oWL3U1isVmTl4Th69hJXOgxU_Rg0hkQriOLpgko6ahd1fy8r-s0MXwZci-UGtIPI8s48KDapoaHB4vVRPla4b63ifbYzjhSMS69rh5XG6XJG9yOrHnLe5aqEeugchxykv5VhadmQKdJhb2S2KM5IYY0lgyoitoMM2dOH5qATqXtfyIf04Y-IV_fy8zIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توپ آرژانتین با مقاومت اسپانیایی‌ها گل نشد  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451244" target="_blank">📅 01:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fba22ecb.mp4?token=G_6MuQLYGy8RXRv7V63ukq1XvUwdkYqf0p1ufvMGvAsxyV3BdtOmWrPnKZhG8Iw1EtYPE1eBM637BftO2XXBUydC4-3z7a1kQ-OoG7EtGFEziBYeieia1yVavd8O90aRVkQVZkX01g2kPcr-H7XVs5psAbzrZGX7-36xDfUzbk_q3bz_78qxxXrkoMZ-oRyiFdaw442Frd9ayjuY4gVhHOhONiGXyVAwbD5FEl-QfUxfy-eiS7JgxAZvbsdBzXBXwXA3XJrbqB5PJ46ChM_EqyasHfDpfXb6Gszeh5nBeilSGExgdWIh4BCZ1ro7KRWSqV0FBiRhpiwrfe5_Y2LS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fba22ecb.mp4?token=G_6MuQLYGy8RXRv7V63ukq1XvUwdkYqf0p1ufvMGvAsxyV3BdtOmWrPnKZhG8Iw1EtYPE1eBM637BftO2XXBUydC4-3z7a1kQ-OoG7EtGFEziBYeieia1yVavd8O90aRVkQVZkX01g2kPcr-H7XVs5psAbzrZGX7-36xDfUzbk_q3bz_78qxxXrkoMZ-oRyiFdaw442Frd9ayjuY4gVhHOhONiGXyVAwbD5FEl-QfUxfy-eiS7JgxAZvbsdBzXBXwXA3XJrbqB5PJ46ChM_EqyasHfDpfXb6Gszeh5nBeilSGExgdWIh4BCZ1ro7KRWSqV0FBiRhpiwrfe5_Y2LS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک مسی به صورت مرینو برخورد کرد  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451243" target="_blank">📅 01:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c479a78e.mp4?token=vi-XW4_efgClpT943JYf8fYyXSyMiWfmb7V5HcF9Ne8jrW3doTchlpjozzbCG9UwC7UNeKN0jg6fhO4Q6nBxK8KnGJsJQsgX6vLCX6OEFuX8jzb0qRorf8OP-NrJfEVs5ha6gWp2z22SyQo0iKUzA_Fot7fJu2P9EVp3PEmqh4xpbPVh7NbogpyOm-gIPxQEc7yB0YjwcNAbqmoEi3rJllt1iO0NHjVKmEuARYxv0CDic9LsK7CO_5-2l5OOuQsurrlgAdG4J9ofC5Df4zq1weR3TmqAgzw2KjYIKr0FLk61fXFbieq-loS8HnzmzUgKh30r8FyNhCNvUMhkWWeYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c479a78e.mp4?token=vi-XW4_efgClpT943JYf8fYyXSyMiWfmb7V5HcF9Ne8jrW3doTchlpjozzbCG9UwC7UNeKN0jg6fhO4Q6nBxK8KnGJsJQsgX6vLCX6OEFuX8jzb0qRorf8OP-NrJfEVs5ha6gWp2z22SyQo0iKUzA_Fot7fJu2P9EVp3PEmqh4xpbPVh7NbogpyOm-gIPxQEc7yB0YjwcNAbqmoEi3rJllt1iO0NHjVKmEuARYxv0CDic9LsK7CO_5-2l5OOuQsurrlgAdG4J9ofC5Df4zq1weR3TmqAgzw2KjYIKr0FLk61fXFbieq-loS8HnzmzUgKh30r8FyNhCNvUMhkWWeYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451242" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ab8e15f5.mp4?token=CTaNCd-BRJG4Y5e7wp15QxA1ey9LndEg6XvF0CdNa4-NJNja4F4Gr6SUgLjZ5vvzv7dhuWnOZhZ_zH6kVDfA__tY3E4yurvFINN614KkUeVt53JhK-7vuRafo8u2kP60J0D3NdfLvyM8sE3YLX6rJyaJIa9aU8tHS_ZYC6_uV6kmsJhKGBcb2WSdvPepRzolBViR_2BpZGd2J4dsgWE01PByokMciESYQImSN3MZFNw68jE79JDV2yIpCRXMq1LSMJFUafGgkeT8J7g2h23oLiaVPMjxHzxdOxUdH6LzFkM5fTI5_2truRnMjqEUu-2A94TpLzG44w4Q1NuB_AUApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ab8e15f5.mp4?token=CTaNCd-BRJG4Y5e7wp15QxA1ey9LndEg6XvF0CdNa4-NJNja4F4Gr6SUgLjZ5vvzv7dhuWnOZhZ_zH6kVDfA__tY3E4yurvFINN614KkUeVt53JhK-7vuRafo8u2kP60J0D3NdfLvyM8sE3YLX6rJyaJIa9aU8tHS_ZYC6_uV6kmsJhKGBcb2WSdvPepRzolBViR_2BpZGd2J4dsgWE01PByokMciESYQImSN3MZFNw68jE79JDV2yIpCRXMq1LSMJFUafGgkeT8J7g2h23oLiaVPMjxHzxdOxUdH6LzFkM5fTI5_2truRnMjqEUu-2A94TpLzG44w4Q1NuB_AUApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451241" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a07464492.mp4?token=G4ZhumYKzvUOy4leYTTrFlRHMSiYU00R3L2_AMTe3X64BQDnr1vMbGpeTE1Mt9VHl72V4MTc0f5i8eqzQEVPS2UjYeXHwH6ZlaDWavwQo-m4gXQ2SsImUWFVivdTK2lCTJfRj4U_RnAONZ4BiIgDtvDWiZEDudXMum8Pp9tRw3D3FdmIYIHsrtRuG2IH9z8X60nUAqTnEpcadb4-RVI8PpXdKutn5mcAnLy5Ni3loBBXXarASeuyXEaxGUI8Vd72JCjz2hAPoTWQFGMLXs80cj8xz8RkJSjZo74e5yk5QLrR2_wunT5v5QoX9IF_QYDYgexrdeI5TgkjFP_FOIhvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a07464492.mp4?token=G4ZhumYKzvUOy4leYTTrFlRHMSiYU00R3L2_AMTe3X64BQDnr1vMbGpeTE1Mt9VHl72V4MTc0f5i8eqzQEVPS2UjYeXHwH6ZlaDWavwQo-m4gXQ2SsImUWFVivdTK2lCTJfRj4U_RnAONZ4BiIgDtvDWiZEDudXMum8Pp9tRw3D3FdmIYIHsrtRuG2IH9z8X60nUAqTnEpcadb4-RVI8PpXdKutn5mcAnLy5Ni3loBBXXarASeuyXEaxGUI8Vd72JCjz2hAPoTWQFGMLXs80cj8xz8RkJSjZo74e5yk5QLrR2_wunT5v5QoX9IF_QYDYgexrdeI5TgkjFP_FOIhvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به آرژانتین توسط تورس در دقیقه ۱۰۶
⚽️
اسپانیا ۱ - ۰ آرژانتین @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451240" target="_blank">📅 01:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
منابع رسانه‌ای از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451239" target="_blank">📅 01:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833aa9b679.mp4?token=Blt5fjBLAWUNUJoE9EUN2xjD3_KYvX_9rxsr50-Hjexcic0H0YqLN3OUN5P_KoIdtJY_sLYEPjfcaolhj29lMobfce5Q_n0XJBdjSAJ-xjKVdt5ICpcuTIQUUOiDFoIOtv7GrgfR15ujYNYZyIY7u9184UsyFJpem98VsNagNg-Ix6u6w_KkzT28-9msXytnrwSeDX0Ftdxk9skIUody-CAPHsaevjUXGK9ulD4-djtyD1LHka-N_gb9Vf4BGmr1JrE1ZSNKJjsOpi0mp7DHuBJha1qlsKtmGt3mezkgSPvboEC18FfrfhT3pipgZthwG16gb50-uKa7lRYp86SpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833aa9b679.mp4?token=Blt5fjBLAWUNUJoE9EUN2xjD3_KYvX_9rxsr50-Hjexcic0H0YqLN3OUN5P_KoIdtJY_sLYEPjfcaolhj29lMobfce5Q_n0XJBdjSAJ-xjKVdt5ICpcuTIQUUOiDFoIOtv7GrgfR15ujYNYZyIY7u9184UsyFJpem98VsNagNg-Ix6u6w_KkzT28-9msXytnrwSeDX0Ftdxk9skIUody-CAPHsaevjUXGK9ulD4-djtyD1LHka-N_gb9Vf4BGmr1JrE1ZSNKJjsOpi0mp7DHuBJha1qlsKtmGt3mezkgSPvboEC18FfrfhT3pipgZthwG16gb50-uKa7lRYp86SpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه سر دیدنی مرینو از کنار دروازه آرژانتین بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451238" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a809a6b06a.mp4?token=L6Jg6lFF61Rvr_KUjqvMfLW7H3_-wddsDK5deB74gQnm5Efi_dsLAHn0qAfW55XPwwd8CZtSWMAFoxjDRlegGf3_BvU9jxlKF6NvSjpqlpSjjQw3ViFg29gjjL5SsiWid7WFqRv_Ls2AWkpRGYEuth5a06BOEmHbv9ly5IdCdsiBNkE2oDr0my3xCnDz8vSxHwtz67tYpC2nyG7RDQr62OBvvjLOqlW7VZ9JPW-j4QiJTYdKBA_DM7TXpt55PsYY0zzLwoyQGEW02dM-mfe-D0xDXzkImzh5Zmdft07jbeNJt0pkX-6heot0GHmvWAEcouBT3FVI-wOYPohOi12t6l2e9A-ZE9-zdBkL8LrdC8D773Q7lswYOX7nlWfp-rc7vSw_b-CNu3q1mPH-QAS_U29xf8hI0AC33pWZF-eElnOmVUETwfCkwuAjfpj7tIeUHaYfziWX0A2ny6EEyPblpiYBPQQ6f1ADaGim3H9G6_qLZqs22gb8LmSoAwbFPy4btm4Ksgd0wKt5PxmMberI6P-9JvzhuOctgcgy3LKs14rWTxYpmoaOj7nfBLYIQxnzGT5aCEzxDRqxmuWxH8B9tABCCs56MlCDTYIPVUir9ano3XCWEYfqHrAJ80nuIlVgqkqvQvCSVZDAmO1xRVytb5WlchOGI9pJREi-3bkxK2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a809a6b06a.mp4?token=L6Jg6lFF61Rvr_KUjqvMfLW7H3_-wddsDK5deB74gQnm5Efi_dsLAHn0qAfW55XPwwd8CZtSWMAFoxjDRlegGf3_BvU9jxlKF6NvSjpqlpSjjQw3ViFg29gjjL5SsiWid7WFqRv_Ls2AWkpRGYEuth5a06BOEmHbv9ly5IdCdsiBNkE2oDr0my3xCnDz8vSxHwtz67tYpC2nyG7RDQr62OBvvjLOqlW7VZ9JPW-j4QiJTYdKBA_DM7TXpt55PsYY0zzLwoyQGEW02dM-mfe-D0xDXzkImzh5Zmdft07jbeNJt0pkX-6heot0GHmvWAEcouBT3FVI-wOYPohOi12t6l2e9A-ZE9-zdBkL8LrdC8D773Q7lswYOX7nlWfp-rc7vSw_b-CNu3q1mPH-QAS_U29xf8hI0AC33pWZF-eElnOmVUETwfCkwuAjfpj7tIeUHaYfziWX0A2ny6EEyPblpiYBPQQ6f1ADaGim3H9G6_qLZqs22gb8LmSoAwbFPy4btm4Ksgd0wKt5PxmMberI6P-9JvzhuOctgcgy3LKs14rWTxYpmoaOj7nfBLYIQxnzGT5aCEzxDRqxmuWxH8B9tABCCs56MlCDTYIPVUir9ano3XCWEYfqHrAJ80nuIlVgqkqvQvCSVZDAmO1xRVytb5WlchOGI9pJREi-3bkxK2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مزار شهدای دانش‌آموز میناب در شب شهادت حضرت رقیه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451237" target="_blank">📅 01:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375b535f54.mp4?token=iTpx55hyd53xURL__wfZ7aNTH4JmRkV8bx8qxK07SKvih-EVFFwhhIpKNueu-UKaGW3Kfiy0lZVARTolaYY4iKABkAM2q2WcvAURoYGGvrf2VfId_psMScUjvyPZUrDdNmMa6qv0rzBPU-HnPmDub2MoU0H9Wo09alNAjTo0vg8gpMuntaLGSbd4aCB_d-0vQVpO8ZGcBg9rpPVwwIGGy6kbv0a7g3w8FTWOL4aiARCnitVgcMvVX17qgdulu1zQVQzH0XVNqafOSkEyQ5pKX1mrQK_c7rV3FzSe0HCkAfjLS7hW6U_umTKaN4PaX9lWSwe_9SM7Py4sbr4oTqncSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375b535f54.mp4?token=iTpx55hyd53xURL__wfZ7aNTH4JmRkV8bx8qxK07SKvih-EVFFwhhIpKNueu-UKaGW3Kfiy0lZVARTolaYY4iKABkAM2q2WcvAURoYGGvrf2VfId_psMScUjvyPZUrDdNmMa6qv0rzBPU-HnPmDub2MoU0H9Wo09alNAjTo0vg8gpMuntaLGSbd4aCB_d-0vQVpO8ZGcBg9rpPVwwIGGy6kbv0a7g3w8FTWOL4aiARCnitVgcMvVX17qgdulu1zQVQzH0XVNqafOSkEyQ5pKX1mrQK_c7rV3FzSe0HCkAfjLS7hW6U_umTKaN4PaX9lWSwe_9SM7Py4sbr4oTqncSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسپانیا گل زد اما داور پیش از آن خطا گرفته بود   @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451236" target="_blank">📅 01:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d04aa0f0f.mp4?token=AXo2JGsMDTIlhyQl2uQkPqB0kXbUItI98i2tFZmKwXlMCHMnFefelmvkSjeEavOZTD8FvHPpAlPeRuDFGo7x5agAEFChr9lVOe9RjOQbpjT_yHeEcZIGgv4OvywNKJL5tap7XD7wmVHaYG19KhtVzzdSp2atIDJEvEdqGTj5PP9ZSv6Il0BWTrCX-ubLmt_qmvIRbSvYK1aU5Z2bjBOPw8fDOurZFd98AGHa5znHhiawROrS_i9Jtq6vV_PeX5IFxKlpGVDxCfmU2vUm2bsQKo6qbIsCj3-pY4rPat6DhSBE9binC06Uy4AtdCil7o4amMNwLNo3rW4Q8r1BFYLtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d04aa0f0f.mp4?token=AXo2JGsMDTIlhyQl2uQkPqB0kXbUItI98i2tFZmKwXlMCHMnFefelmvkSjeEavOZTD8FvHPpAlPeRuDFGo7x5agAEFChr9lVOe9RjOQbpjT_yHeEcZIGgv4OvywNKJL5tap7XD7wmVHaYG19KhtVzzdSp2atIDJEvEdqGTj5PP9ZSv6Il0BWTrCX-ubLmt_qmvIRbSvYK1aU5Z2bjBOPw8fDOurZFd98AGHa5znHhiawROrS_i9Jtq6vV_PeX5IFxKlpGVDxCfmU2vUm2bsQKo6qbIsCj3-pY4rPat6DhSBE9binC06Uy4AtdCil7o4amMNwLNo3rW4Q8r1BFYLtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان آرژانتین یکی پس از دیگری موقعیت‌های اسپانیا را مهار می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451235" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4511c12bc.mp4?token=GCWn1HCT6JYL5HQBdRFJ4qCwYUcifNAMmaJtAXno6IuNLEHc-9YGFaEfbCdB4c89TxG3v8BOYFth5pskDyjZLoyzMYFBXU5X9YnGViIwqGG7LLUzWDXK0oOiKE4LwesLJRKC4DygNjKefkmgAvFQu2iVgWVgupIheP9ZCWB41kVYG-D4BzpgWjon3v3lazAQsprsEUGPulNkzgDQ9g_vzMmmLKr2O3Df_esWXCxmjd6bsk1-1DCfRtXPTEBPmdTv3QaZvBym0DGnZeaJ7YWhBmfPtcY7L86sZJE0M34mp51CH7qiTPnGUXPNsgsrc1OBiQrdTRDXVdKFKci6pVum2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4511c12bc.mp4?token=GCWn1HCT6JYL5HQBdRFJ4qCwYUcifNAMmaJtAXno6IuNLEHc-9YGFaEfbCdB4c89TxG3v8BOYFth5pskDyjZLoyzMYFBXU5X9YnGViIwqGG7LLUzWDXK0oOiKE4LwesLJRKC4DygNjKefkmgAvFQu2iVgWVgupIheP9ZCWB41kVYG-D4BzpgWjon3v3lazAQsprsEUGPulNkzgDQ9g_vzMmmLKr2O3Df_esWXCxmjd6bsk1-1DCfRtXPTEBPmdTv3QaZvBym0DGnZeaJ7YWhBmfPtcY7L86sZJE0M34mp51CH7qiTPnGUXPNsgsrc1OBiQrdTRDXVdKFKci6pVum2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان آرژانتین بازهم اسپانیا را ناکام گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451234" target="_blank">📅 00:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
مقاومت اسلامی عراق: در صورت اصرار دشمن آمریکایی بر گسترش حملات خود به ایران، مستقیماً وارد نبرد خواهیم شد و با تمام قدرت و قاطعیت، تمامی منافع و پایگاه‌های آمریکا را در عراق و منطقه هدف قرار خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451233" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع رسانه‌ای از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451232" target="_blank">📅 00:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb709750a9.mp4?token=GRHNtlUZyJTT74bKaCsuKv5WK19sleio3d9rKA3ZHOB0JzQlN8sKa2-899-2S0WSTE7AQownr4DC4Y_MDCWEGMHjEYfkS1mArlBQs8Tktg8sq1V5MvVIyofkaYXpgoqBLzNLihIwbM_tYTt1b4um5b1-tjYS40y6GRUwbYH_LXVHvan0bDl3wiQWTB-YLhraw29BCsv_m4ZMbe5k2rp_1AhYRXLeLqxpigt9QJdu7Z-VX3ZY2g4EqcxyMR83l71Qr-iyLncS8naTEgGyCiU6nYEA5I996ZXSesYHXga9q-jVSIUoml9Rbqsz765CJ_-0y5aixLfe-kWfAfwlo4yfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb709750a9.mp4?token=GRHNtlUZyJTT74bKaCsuKv5WK19sleio3d9rKA3ZHOB0JzQlN8sKa2-899-2S0WSTE7AQownr4DC4Y_MDCWEGMHjEYfkS1mArlBQs8Tktg8sq1V5MvVIyofkaYXpgoqBLzNLihIwbM_tYTt1b4um5b1-tjYS40y6GRUwbYH_LXVHvan0bDl3wiQWTB-YLhraw29BCsv_m4ZMbe5k2rp_1AhYRXLeLqxpigt9QJdu7Z-VX3ZY2g4EqcxyMR83l71Qr-iyLncS8naTEgGyCiU6nYEA5I996ZXSesYHXga9q-jVSIUoml9Rbqsz765CJ_-0y5aixLfe-kWfAfwlo4yfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرژانتین ۱۰ نفره شد  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451231" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f33f7f43c.mp4?token=AWcx4yT7vo65QNoHRvQLNWNeJDZo3suCsq3cBEyy9UGoIaOEmoe4r4nGJFOugRYSRstyE6mCiZ2YBWUSYAqyA6yU-9KJaS1iEEmTmv8eBu42HCjfTa20mjypTC85G_aZck7ilDpBFGWie8FLok4uZiMApBx9ov-IfDukOvknsSW1vQK_DWPWuFJhiMLknF33hCS_xI6hYN6Iw365txrv7GhayGn52yUKmf-7fkLP8ciro8PqAdXg0XWasF4r6jsCQVQM8NrFznlSPCAYKPIAw0rS2jrjh2bokFOMGZUTigdQrdJ6WvoV0zHiF5WyA9oYzvGWmPTALqaifoHxuWuufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f33f7f43c.mp4?token=AWcx4yT7vo65QNoHRvQLNWNeJDZo3suCsq3cBEyy9UGoIaOEmoe4r4nGJFOugRYSRstyE6mCiZ2YBWUSYAqyA6yU-9KJaS1iEEmTmv8eBu42HCjfTa20mjypTC85G_aZck7ilDpBFGWie8FLok4uZiMApBx9ov-IfDukOvknsSW1vQK_DWPWuFJhiMLknF33hCS_xI6hYN6Iw365txrv7GhayGn52yUKmf-7fkLP8ciro8PqAdXg0XWasF4r6jsCQVQM8NrFznlSPCAYKPIAw0rS2jrjh2bokFOMGZUTigdQrdJ6WvoV0zHiF5WyA9oYzvGWmPTALqaifoHxuWuufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان آرژانتین این‌بار ضربه سر لاپورت را مهار کرد  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451230" target="_blank">📅 00:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
منابع خبری از به‌صدا درآمدن آژیر هشدار، و وقوع انفجار در پایگاه‌های آمریکا در بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451229" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451228" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدای شنیده‌شده در اراک مربوط به اقدامات آفندی است
🔹
دقایقی پیش منابع محلی از شنیده‌شدن صداهای انفجار در برخی نقاط شهر اراک خبر دادند.
🔹
درهمین راستا، فرماندار اراک اعلام کرد که صدای شنیده شده مربوط به اقدامات آفندی در یکی از استان‌های مجاور است و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451227" target="_blank">📅 00:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bec5eee3.mp4?token=q-heD6VpZ6jvJ5JnWqHuko4d9zNHGH6pxlXV7o1meN_4eJO3oDvkXB4KzTSVaPeJcPxI5ojC5YBe2Rsmm4a30BO-5T1hJzDmUFWLIKimGPmwJck5C7AqObCYaJ8LdsnPccgA4AdZARcC3o3imhEHgBv9guQc2_mwtHEuE204aBdPC7s4fJVHi2YtV7Kk2V-SRxMdJaeDZ-ucbv2vU7Sw2TmJKiqMjaIGhTJryLEi6yA75dXflrc5Y_GGUgo03LwHaWYTrwU7VoMhwJ5xT3oEJ0qNPwa5YMGj4iavXYHWBB0AfAeHGKPfUOFTeP2Ust3IElaYmeJ3lzglekL6qs6yxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bec5eee3.mp4?token=q-heD6VpZ6jvJ5JnWqHuko4d9zNHGH6pxlXV7o1meN_4eJO3oDvkXB4KzTSVaPeJcPxI5ojC5YBe2Rsmm4a30BO-5T1hJzDmUFWLIKimGPmwJck5C7AqObCYaJ8LdsnPccgA4AdZARcC3o3imhEHgBv9guQc2_mwtHEuE204aBdPC7s4fJVHi2YtV7Kk2V-SRxMdJaeDZ-ucbv2vU7Sw2TmJKiqMjaIGhTJryLEi6yA75dXflrc5Y_GGUgo03LwHaWYTrwU7VoMhwJ5xT3oEJ0qNPwa5YMGj4iavXYHWBB0AfAeHGKPfUOFTeP2Ust3IElaYmeJ3lzglekL6qs6yxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه سر خطرناک فران تورس با مهار دروازه‌بان آرژانتین همراه بود  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451226" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شترسواری دولا دولای آپارات به بهانۀ جام‌جهانی!
🔹
برنامۀ اینترنتی «دری رو به جام» از تولیدات آپارات اسپرت، در حالی پخش شد که ایمان صفا بازیگر حامی کودتا و اغتشاشات دی‌ماه ۱۴۰۴ مهمان آن بود.
🔹
این درحالی است که این بازیگر در ماه‌های اخیر به‌ویژه از دی ماه ۱۴۰۴ به بعد، بارها مواضع صریح و آشکاری در حمایت از جریان آشوب و اغتشاش داشته و همچنین استوری‌های تمسخرآمیز و نیش‌آلودی را نسبت به کلیت نظام و سیاست‌های اصولی آن منتشر کرده است.
🔹
همچنین حضور اخیر او در مراسم ختم مادر داریوش فرضیایی با لباسی که یکی از نمادهای کودتای دی‌ماه روی آن دیده می‌شد، اقدام حاشیه‌ساز جدیدی بود که مورد استقبال ضدانقلاب قرار گرفت.
🔸
در شرایطی که پلتفرم‌ها به‌‌وفور نشان داده‌اند اگر جریان پایدار و مستمر پایش و نظارت ساترا بر تولیدات‌شان وجود نداشته باشد، از استعداد چشمگیری برای بروز استانداردهای دوگانه برخوردارند، باید بیش از پیش، بر تقویت نقش نظارتی این نهاد تنظیم‌گر توجه و تاکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451225" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8bce10f2b.mp4?token=GIB6kZSFIO3tNMP4j4RZHbQEdnz5eWjo0p06adbX5mOH2dir-vRN992UHWFdgRnZ8OkEMmkREyvXOSwzg_u15Cw0u8y4LtSiYu9oi6a5lVaXC_6VXwaCQwAvXrCdB5etrq7kLQ_oLTLPXBoFc2y0BksQCmHrrjCmFNjdgsCQsc79-yt13Azt22KLl8sEUkBX8jsM7yeNtWyE9pATuS_5CbyZBCvadnw3BhDwGwL4T-9bE93ygJZtH3RZ4-XBYFN7hK3ohWGFymGsdrI6WrDDyhyy4LIxIS1on_IFhiOfH0m9tV_V6iq-kK8VGzwujAh_lh6hHCQ8zGZyoVLCF-u4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8bce10f2b.mp4?token=GIB6kZSFIO3tNMP4j4RZHbQEdnz5eWjo0p06adbX5mOH2dir-vRN992UHWFdgRnZ8OkEMmkREyvXOSwzg_u15Cw0u8y4LtSiYu9oi6a5lVaXC_6VXwaCQwAvXrCdB5etrq7kLQ_oLTLPXBoFc2y0BksQCmHrrjCmFNjdgsCQsc79-yt13Azt22KLl8sEUkBX8jsM7yeNtWyE9pATuS_5CbyZBCvadnw3BhDwGwL4T-9bE93ygJZtH3RZ4-XBYFN7hK3ohWGFymGsdrI6WrDDyhyy4LIxIS1on_IFhiOfH0m9tV_V6iq-kK8VGzwujAh_lh6hHCQ8zGZyoVLCF-u4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صداوسیما: در بازی فینال جام‌جهانی فوتبال هیچ تصویری از رئیس‌جمهور جانی آمریکا نمایش نمی‌دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451224" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آژانس بدون اعلام محکومیت: حمله به سایت دارخوین را بررسی می‌کنیم
🔹
آژانس بین‌المللی انرژی اتمی با صدور بیانیه‌ای، صرفاً به اظهارنظر فنی درباره حمله آمریکا به سایت در حال ساخت نیروگاه هسته‌ای دارخوین اکتفا کرد و از هرگونه محکومیت یا اشاره به عامل حمله خودداری…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451223" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌ اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله قرار…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451221" target="_blank">📅 23:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=lRNzQhnUxANcllOqKQHaN7oAhLPzTW001XcTzDI0F13oAL5W6Nnw6UG0Bo0PJ6QHlQS1cxXZnnB2gIwJEt_XZqfLGCwzcSqivecyqw6JtbtBNZAa20CpXfMk9GSREXBqWsg7yHZinb9_L_5oGrom6jP1wqD541k21VAMedI6PcThRmOKrpR1cp65RC5w_LED-P9KGHeZEZmQoc142o0K6fTfhzQtUUF025fHnjC8l-bj2k86QRtyseVRJMDXm3aMoR82CO-OiEKIpX9M_QFp4AsaZwpon9t3XMZveqlQQ8SPD1TR-qxwOj6q2iwM52lZ51xyFsQ7LCCGt72nrGfP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=lRNzQhnUxANcllOqKQHaN7oAhLPzTW001XcTzDI0F13oAL5W6Nnw6UG0Bo0PJ6QHlQS1cxXZnnB2gIwJEt_XZqfLGCwzcSqivecyqw6JtbtBNZAa20CpXfMk9GSREXBqWsg7yHZinb9_L_5oGrom6jP1wqD541k21VAMedI6PcThRmOKrpR1cp65RC5w_LED-P9KGHeZEZmQoc142o0K6fTfhzQtUUF025fHnjC8l-bj2k86QRtyseVRJMDXm3aMoR82CO-OiEKIpX9M_QFp4AsaZwpon9t3XMZveqlQQ8SPD1TR-qxwOj6q2iwM52lZ51xyFsQ7LCCGt72nrGfP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صداوسیما: در بازی فینال جام‌جهانی فوتبال هیچ تصویری از رئیس‌جمهور جانی آمریکا نمایش نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/451220" target="_blank">📅 23:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93984c2740.mp4?token=ooq4eLdypAZQhb9yxQG6vhLj9PX6ZuBj0cMRqVrLzKhlshgQTdAkwVbgUwFoVP_X5g2RyhSVMjXM6Qht-vNG-kzRLvlKh6YnZo7E7HywPW9RdmDw5jMoXR_5JoqkKLyO6zI3qUniJNXccc1xC6s-XHc7h14gvh-5uLJNBc0yIo8lPRqzZBqyml6HqeEb4-PFGXjcOCkL-y1xaAj_2jH5YmLILJmC1jZ8_BCycBrF4TBaYtMsGGVvM-LgxuTWWav3AF_7wLw2SvSDFGo5fVQ5zcg_4CUROrVZWrmEt3axw3A0QUR2SW1ehY58iNklO-DYyld_4ZS50kM8HSDLO3JPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93984c2740.mp4?token=ooq4eLdypAZQhb9yxQG6vhLj9PX6ZuBj0cMRqVrLzKhlshgQTdAkwVbgUwFoVP_X5g2RyhSVMjXM6Qht-vNG-kzRLvlKh6YnZo7E7HywPW9RdmDw5jMoXR_5JoqkKLyO6zI3qUniJNXccc1xC6s-XHc7h14gvh-5uLJNBc0yIo8lPRqzZBqyml6HqeEb4-PFGXjcOCkL-y1xaAj_2jH5YmLILJmC1jZ8_BCycBrF4TBaYtMsGGVvM-LgxuTWWav3AF_7wLw2SvSDFGo5fVQ5zcg_4CUROrVZWrmEt3axw3A0QUR2SW1ehY58iNklO-DYyld_4ZS50kM8HSDLO3JPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم اجتماعات شبانه با ۱۴۱ شب ایستادگی در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451219" target="_blank">📅 23:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iefmEgovkPQGwDN-ISZK-kzJGR8pqGHliSZYbqsjzzp_w_lxto_VC1WEqaR2gUFDvCx-S78kufyZBcBtBSgfI9Cu1m3mlUUL-UmzE6vfQlnnQgxrDaOon7i0xk6kIVPvyu1zgtu0aAImPX9DzgskdX9swV8eT6ZJjIOovRQACHPidVF8cmYkA8tdagLW3QLNZYXFVvnpXU73mS9P0x7xbpldef6-Bp3KGX439k0PzHqfXk_R6bW2YWkabaefR1cECwUgC6v9jTjZ4AIyUUMTyDtvjKMpWYx6PC2oLX0BDo62CntDn7njuEhGVPmkdY7Q33ZNgWaIWlvDrT_TtXeTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ترامپ از پشت شیشۀ ضدگلوله فینال جام‌جهانی را تماشا می‌کند
@Sportfars</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451218" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBcJMXyLLRSBOhwL2RXHIc2478zMym7EHIKYKQR1ty2fP-G4TnQ1xww1caJBLh1AeMeblM93luV4nuWK5_cXr0gktH7nlCVgiH88hBIHqb1P3ms4Bpz-A6PJUZi-pBr6ShghglRWp48Ucb3xJP23ElHU9ST3PrfeBsvdMwDvtM6ddwJtEKt1wjjVAw9qqVcy2ZHym5uUxDumf68Uml-_hI-LDIHRTqEsdRTf1vX9e0IOvWVa3CUOT6PsVn7pFQ76f8J6kBp9SY8FShjLQrF1QOdzVChx_2454dorNj9SjfykO6Q1y4_WWATreDrF4IMYrDGoKtROFEglO_rUk3czPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر راه: تمامی خطوط ریلی کشور فعال هستند
🔹
در حال حاضر هیچ‌گونه انسدادی در مسیرهای ریلی کشور وجود ندارد و تمامی خطوط ریلی فعال هستند.
🔹
ایستگاه انشعابی راه‌آهن بندرعباس نیز به‌زودی به مدار بازمی‌گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451217" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451215">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG9QHyIilcsI8qXXyD8ZElNB1KeopW0b3k9gaW5cB-LGEHgtdwhk4V07SaEjoIPYsnqWSGD1PBFeJnbKVst1m2zo9x6tHhkdheA_sDj_qkTUzwtoXT8sR3rHNPhMqp369yk-ElnfnqTa8410YyF1ZzsEc22D3s2CTYTniL_evTiMrRnlic_G5oSUDPiRVClFrRupm9He285ci80Sc6iQWHn_nR6OueyPc84WLeU6G_rxNYRpn9bH-RCWFghKUtCryVKlmQZ5i6f77cwDmlaTBW2hlTNqSxazgpGAmEX-9lcGxXk06sV-rXfBVhDHQQ3cGeJDvGQregs2cMtVYcijZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9uXu151oIck5K9mx9S_KqAZKOgCMEWSulBa7pMKoN8EHzTMRqxd2VO6iHib0NfIo6V_Xxwitd7ARTOWkN--PN3zDXoG7jxZuHSNHlhvNnFLTXqTK7RIcRFqa4YXxqg3-4CQ0qK6zO6dSoCoCKsfMCh8XS6xYV1gXCZZhfb1K1dwEfHOxfv_KdCMGAYBLOgEvq4bNdXms-Ci808j-0BoFkPu0u8cOgHhqsYE07yJjWtvudlG1c3TkVe1cN54Kksl_TRRF0ZiHG2HsRX0Lx9q65IFZsekokGmP-pE3OHHdXIfa0AUfgQmJl_W_-4MGIMC8L9XsGsUgfy7m-AF-eGMgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451215" target="_blank">📅 22:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: یک نظامی آمریکایی در حملات ایران به اردن مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451214" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
اعتراف سازمان تروریستی سنتکام: ۲ نظامی آمریکایی در حملات ایران به اردن کشته و ۴ نظامی مجروح شدند. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451213" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrA7HWeq7WWu_YEz7BZp-aTHJAdcZFifchLvsVFALt-xNoSTOeiPK_VokfgSYy9vdgchXke12Gtc0JhXAjzr2hGHUTtSWJOGIF5mA6tGfAuYApGMz5BEZ_64s9dpbvbfKvtVIwyTGhQV2OwCBnq--EiAfl6Ix3tj3ZXfJvhCS3D2y9sWidyqKORQKq4WibX8KXE1hHZWMshIiX1qIqlHM8ed7Ynvk4kOpIAdqAid-jOLYVuTI8kNrV56b0PROrBMlajUauqf0PasgVUwZQzw4I_t21mFjOcUrvlGrg75-rw1p-1HxmZzqyZw52Vem7NNkZc1B8L4CoVWVBKlvDoD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقابل چشمان ترامپ
📷
نمایش پرچم ایران در استادیوم مت‌لایف کنار پرچم ۴۷ کشور دیگر پیش از شروع فینال
@Sportfars</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451211" target="_blank">📅 22:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منابع عربی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در منطقۀ سلیمانیه در عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451210" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc36bb3b8.mp4?token=mSJ7B8nSz5EDU6LCoyf53vUoGhCDNg2ohEWZoF_pZezuNm51zxw3vTJI0eote05FDWnlnxQcKefm_DVLck-oDsySvRwrpBucPJZT-8MZEhz_5XM3iGfMLTgUeeHdDJLYxCx-ccYV0V5YJZCoSC3-vMO3--3vc6RbEpzRHvjSxVPSCRF2YSWm86OCuBBv8pJD7fJneL_3TCtj_o6M-79fKPx6glMcdyT_NEZVI9V2iXd3p-BaEYS-MrLOH-Q30QghJah5wrJP08wSpwaZihxBpkFFMmq90WedPqQWB9yi-12Kkzveane-EwJFIIyT3gutGZDxHrg9Mq38yFwH2uCLIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc36bb3b8.mp4?token=mSJ7B8nSz5EDU6LCoyf53vUoGhCDNg2ohEWZoF_pZezuNm51zxw3vTJI0eote05FDWnlnxQcKefm_DVLck-oDsySvRwrpBucPJZT-8MZEhz_5XM3iGfMLTgUeeHdDJLYxCx-ccYV0V5YJZCoSC3-vMO3--3vc6RbEpzRHvjSxVPSCRF2YSWm86OCuBBv8pJD7fJneL_3TCtj_o6M-79fKPx6glMcdyT_NEZVI9V2iXd3p-BaEYS-MrLOH-Q30QghJah5wrJP08wSpwaZihxBpkFFMmq90WedPqQWB9yi-12Kkzveane-EwJFIIyT3gutGZDxHrg9Mq38yFwH2uCLIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی آموزش‌و‌پرورش: تا این لحظه هیچ سهمیه‌‌ای برای مناطق درگیر جنگ درنظر گرفته نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451209" target="_blank">📅 22:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آموزش‌وپرورش: امتحانات نهایی پایهٔ دوازدهم روز سه‌شنبه ۳۰ تیرماه مطابق برنامه در تمامی استان‌های کشور به‌جز هرمزگان برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451208" target="_blank">📅 22:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5VIb3atx2Hl1757OH0ySZSz2zdJ-EaQ5d6vDvMZDAGaMboy8fnw6KTeEqoY8beyblve45ZXuGADe6iaihab04nBnb8PWoEka-58oG5ZLMVXARTWCjwk7tFYGsmoIYz3t5RZzEoTEuu06bcOU7Fupc0KFpDRMw9wwVFoGqK9TTjnCmAs5ifIW4loR0HoEqtUa5cm1Bjw9-HXZEdawKZR6DMYuxYefmlUcIIFoFfl0qm9ZrpU45Tmh4kXTy7Ixd5Ca4F8TFA2YLwBTZkMClF5tEfckO4wTKsNsUP9lrtIei3DOM0O-yldvAKZp4dD6mY31wbrs-R2IJMXvwG9Nis5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رونمایی از کاپ جام‌جهانی ۲۰۲۶
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451207" target="_blank">📅 22:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3576da499e.mp4?token=HwJnsBQaYw0BiHPAMkIVOc9v9X0Q9tZHbiHNNq4U5jh0ANZA1Po58T-OtOKGIcxADH20FyxDutRPzJD548TJ9dNtuuSrxMen3mlfaOJuYMuc-X0BGKNPFGQIV0eTQLnXxEvyesktVhWESFYwDDaxCQ6pnfiiHYM64s6wGIiPUU0fc4sNj2nAjiLuv5b6hNJPFJwR8y5P6LZH_xWUP5Tn2P-3Vr54BcH4rEAz6WT6qLyuU-te7f6oEFZzD62zqmK3Z0xg8-szuI-yEiMM5YSsHD6BQ7YEof9EUXWYc5rRHDQwLYBOfuPgPbDTd8IZz9bsebRTOy8FZY1cKbvhuGYWww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3576da499e.mp4?token=HwJnsBQaYw0BiHPAMkIVOc9v9X0Q9tZHbiHNNq4U5jh0ANZA1Po58T-OtOKGIcxADH20FyxDutRPzJD548TJ9dNtuuSrxMen3mlfaOJuYMuc-X0BGKNPFGQIV0eTQLnXxEvyesktVhWESFYwDDaxCQ6pnfiiHYM64s6wGIiPUU0fc4sNj2nAjiLuv5b6hNJPFJwR8y5P6LZH_xWUP5Tn2P-3Vr54BcH4rEAz6WT6qLyuU-te7f6oEFZzD62zqmK3Z0xg8-szuI-yEiMM5YSsHD6BQ7YEof9EUXWYc5rRHDQwLYBOfuPgPbDTd8IZz9bsebRTOy8FZY1cKbvhuGYWww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف مردم دربارهٔ دلسوزی قلابی این‌روز‌های برخی سلبریتی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451206" target="_blank">📅 22:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2d11e6ab.mp4?token=oJjGvVgeYBa4jv7yeHkBlzHDa5fHLXjHbb7Ezoeb-ewqMP0oMOyhb2rbcTYqC1sPRjrJPIPrySiP5UMZhVHaFCKgyqNfAJcev3f3AaWN_ezKx8xlwdIwjBDD1EqH7m0FMKyO1MAKP5g6CWKf2n8VdrA5HM5dKkp1OSUy4fjg6wFpqFrw_l9elgv-tTJ2OuxigkVkQDnIy7QXtSYlWwNKWG-ea2Sk0uAJuBo8opirCKREKoQUohXn9goSWX1QwiXcdY0zIZCb5wIoMv0spH1dSJiCmcXMQbIF-1tQD-3TnvQx2jwi_fWwspbUfWk_h1cz9TpCslZJ3t845haxOlbSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2d11e6ab.mp4?token=oJjGvVgeYBa4jv7yeHkBlzHDa5fHLXjHbb7Ezoeb-ewqMP0oMOyhb2rbcTYqC1sPRjrJPIPrySiP5UMZhVHaFCKgyqNfAJcev3f3AaWN_ezKx8xlwdIwjBDD1EqH7m0FMKyO1MAKP5g6CWKf2n8VdrA5HM5dKkp1OSUy4fjg6wFpqFrw_l9elgv-tTJ2OuxigkVkQDnIy7QXtSYlWwNKWG-ea2Sk0uAJuBo8opirCKREKoQUohXn9goSWX1QwiXcdY0zIZCb5wIoMv0spH1dSJiCmcXMQbIF-1tQD-3TnvQx2jwi_fWwspbUfWk_h1cz9TpCslZJ3t845haxOlbSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: در جنگ رمضان، حدود ۴۰۰۰ بازرسی سرزده از دستگاه‌های تحت نظارت در سراسر کشور انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451204" target="_blank">📅 21:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
وقوع انفجار در اربیل عراق
🔸
هنوز جزئیات بیشتری دربارهٔ علت انفجار یا تلفات احتمالی منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451203" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4303a24a4.mp4?token=e8pyq6yNxFKRG0AQEhTmpULoAR466MNLf-CySCqg3az1kYPk3PAnY7qRKIu3CKhxST9zQPQj1U2fSaOjHWz9AMVXa85429dVUVrCYzwrTyA-I33ceCF6Sc6Wv5YEgjV6agSbVgvG7XDzhImWvMILQEuaY_Lmsm-uwyNs_5X8rJqQBBs1unwHk3MtvKUvf19nr0ycGqkvKOEBDFEJZ42Yj6TPbKIx7yvOLx8NH-RioaEMr6ieeSPppx6n53WtiYxTFzXE174K34kcIdYCpRcslRDPJ3mMn42iGIDzJFDcQF--Jv6TLtD8RN2u6yg3bwqPxBS7Ad3AWGMvp6-MpUd-lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4303a24a4.mp4?token=e8pyq6yNxFKRG0AQEhTmpULoAR466MNLf-CySCqg3az1kYPk3PAnY7qRKIu3CKhxST9zQPQj1U2fSaOjHWz9AMVXa85429dVUVrCYzwrTyA-I33ceCF6Sc6Wv5YEgjV6agSbVgvG7XDzhImWvMILQEuaY_Lmsm-uwyNs_5X8rJqQBBs1unwHk3MtvKUvf19nr0ycGqkvKOEBDFEJZ42Yj6TPbKIx7yvOLx8NH-RioaEMr6ieeSPppx6n53WtiYxTFzXE174K34kcIdYCpRcslRDPJ3mMn42iGIDzJFDcQF--Jv6TLtD8RN2u6yg3bwqPxBS7Ad3AWGMvp6-MpUd-lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرج‌و‌مرج در ورودی ورزشگاه مت‌لایف
🔹
درحالی که کمتر از یک ساعت مانده به آغاز مسابقه، هرج و مرج در بیرون ورزشگاه مت‌لایف به اوج خود رسیده است و برخی از هواداران بیش از دو ساعت منتظر ورود به داخل ورزشگاه بوده‌اند.
🔹
مشکلات فنی در گیت‌های گردان، بررسی‌های امنیتی اضافی و دستورالعمل‌های نادرست از سوی مسئولین برگزاری، باعث ایجاد صف‌های طولانی قبل از رویارویی اسپانیا با آرژانتین شده است.
@Sportfars</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451202" target="_blank">📅 21:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfbe95180.mp4?token=Dm-_i1l10WoyJBS_xyvawxrAfwFsSBCPlMSWEKrNhjfilWsZKy0kR52XRxF-XtqmYFFfafutDJTIaTgflKjzrGe7lFSxsxbX_AfXw111HGp4fu10pzq5-fantgD52hDJu0XNsRmQISPl0O2EZ7kCY-9xNnK-WE29bUuKzQgkzJkkHERFi4ICIqFHs83drNEAT8yvv-djw-XKIxS570GyfZC_VmUSlsClApvwYOjnOUhkxBthq4Qjb6sogBOhOpza1eFc9dsb4b_dmW9oB_vcAF5KxAEdVRFMFZ491ESjE0yUuwBNLwIWlmLI-bZF6dr6yjGDe2itQBeh4gV6Ty9U6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfbe95180.mp4?token=Dm-_i1l10WoyJBS_xyvawxrAfwFsSBCPlMSWEKrNhjfilWsZKy0kR52XRxF-XtqmYFFfafutDJTIaTgflKjzrGe7lFSxsxbX_AfXw111HGp4fu10pzq5-fantgD52hDJu0XNsRmQISPl0O2EZ7kCY-9xNnK-WE29bUuKzQgkzJkkHERFi4ICIqFHs83drNEAT8yvv-djw-XKIxS570GyfZC_VmUSlsClApvwYOjnOUhkxBthq4Qjb6sogBOhOpza1eFc9dsb4b_dmW9oB_vcAF5KxAEdVRFMFZ491ESjE0yUuwBNLwIWlmLI-bZF6dr6yjGDe2itQBeh4gV6Ty9U6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: آب شیرین‌کن بونجی جاسک به مدار بهره‌برداری بازگشت
🔹
نیروگاه‌های آسیب‌دیده از تجاوز دشمن در سریع‌ترین زمان تعمیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451201" target="_blank">📅 21:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31e7d7dd1.mp4?token=VstyjU50t5AqFMXbxgWf-cycBow61cwPzUWbeVPqS3XgAh4BaIwlMandHMv2thqgdv3TwArn9VGMSHjOsPkpzF9B4K2GaYKbrtdUtIbK6_N3o9tTr6cWwZJjLEm9yX-u9JXr7lxeDvOqT01tigBIarpgCFcSic9A1zcE3JfMNsSXfkRuwjo62OeinjY6FRmNZvXqq46yAG07kZnBdOUNS-uWdWVS_k_Rfa0Cnc5tKbG8pprxCcHzfWuVLgqa94ENEyeuTv3f7yysQeolgpvJa0YCjjBKHHfamonOutRlokK_lI5BTNvecOvDAAAZnEltNq5KERnEgkLsMmRUCgT-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31e7d7dd1.mp4?token=VstyjU50t5AqFMXbxgWf-cycBow61cwPzUWbeVPqS3XgAh4BaIwlMandHMv2thqgdv3TwArn9VGMSHjOsPkpzF9B4K2GaYKbrtdUtIbK6_N3o9tTr6cWwZJjLEm9yX-u9JXr7lxeDvOqT01tigBIarpgCFcSic9A1zcE3JfMNsSXfkRuwjo62OeinjY6FRmNZvXqq46yAG07kZnBdOUNS-uWdWVS_k_Rfa0Cnc5tKbG8pprxCcHzfWuVLgqa94ENEyeuTv3f7yysQeolgpvJa0YCjjBKHHfamonOutRlokK_lI5BTNvecOvDAAAZnEltNq5KERnEgkLsMmRUCgT-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بچه‌های ما همه سوخته بودند؛ بلااستثنا!
🔸
روایت خانوادهٔ شهدای میناب از داغی که آمریکا بر دلشان نشاند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451200" target="_blank">📅 21:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0538e2ee.mp4?token=HE07t8fCL0caP1kDQTmVPhgTYSY5jLqmDpXoabwNeqX2lTyX4fl_w5n3FPIIo2BLBv4kQ_yqovf0REFoHZPQB0tXtKz_d61s4A018XrzNfcfoB8CJ1BruTK5b4c502o2KsUhAlHMHgYEwJ_TbMREhGBhYE1xKkGOZRHLlC_EWKzz4xh8H0Eur7gL_QF-YpVzCQffnyuPyKVOFglsw2CJmJBwL4xYUK_haWoql7c7QM_QFUfQct30no2BM5JBkYgf1tc5ISHYevlnyoKLxayKEguT7pBLACjYTTLqZQ0tYRKPZe3xNBplw1TpGsVBfU1KHl96mb5-nzPT6tSoYO5d4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0538e2ee.mp4?token=HE07t8fCL0caP1kDQTmVPhgTYSY5jLqmDpXoabwNeqX2lTyX4fl_w5n3FPIIo2BLBv4kQ_yqovf0REFoHZPQB0tXtKz_d61s4A018XrzNfcfoB8CJ1BruTK5b4c502o2KsUhAlHMHgYEwJ_TbMREhGBhYE1xKkGOZRHLlC_EWKzz4xh8H0Eur7gL_QF-YpVzCQffnyuPyKVOFglsw2CJmJBwL4xYUK_haWoql7c7QM_QFUfQct30no2BM5JBkYgf1tc5ISHYevlnyoKLxayKEguT7pBLACjYTTLqZQ0tYRKPZe3xNBplw1TpGsVBfU1KHl96mb5-nzPT6tSoYO5d4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این اتاق برای رهبر شهید، شوق انگیز بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451199" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a8cb355a.mp4?token=NRE_JUK6u9J0pb0_UhHBO270b52W1-Sys1kB915xnvgyVPrkj8f_Y4expdfiQJSqJp9zoiSnlYfWF6IfmRNEJz26o3FmgGaDyUnEHoEQpDxF2u0da5bXk72Ap2WkwTlAivTJNWJ1sj5ag1NeOAygO6C1CJ35EI9Khcz6-hkiLa7n3ZetLfrac1r8qIi6dLmhr2TPuaYCvw47tNhvDJXKpBvBm8yLqHD8-G7otoEZuDKyhgAx0b4vF16LehrWHDjpUXRKJiv83at0hSgiUsbQigmcwf_ru3psho8e0KwQXVZRCd6p-wNtjR52PjS4Cg2dB7ZQHDUwGy2o1MxhqFn5-50D-J3OjmcRjw7fdm8dQxMaJaYgHXaVMTuoT0NEb-JSAkTM8kAdopXm6uZ_AeiXJCdxBTHULhcz6ENUB44g11aGg6W2VsImDY609K1cRlLpqBUSHMOeDblcdAWXOLwhYCY3-V6vUtFLck_WHwaIKrYC80RyyWwQ-CMPxYS69hZnVkQFSRhR6FLfVjENU80S4eqBSrBpvpW3ejfN-25b3HfQdx5psGunnH6ZFUzzfMQ5WnvSmKnrkMjA9Y145pAmOfIQkAVeRH4VcDnq7sI1y2dS_3HsSoa6eXFw6DYdEnrqONSjE_f1WXXz5x9qlUo1msZ0BYd_ZW8rdCKcKtGBidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a8cb355a.mp4?token=NRE_JUK6u9J0pb0_UhHBO270b52W1-Sys1kB915xnvgyVPrkj8f_Y4expdfiQJSqJp9zoiSnlYfWF6IfmRNEJz26o3FmgGaDyUnEHoEQpDxF2u0da5bXk72Ap2WkwTlAivTJNWJ1sj5ag1NeOAygO6C1CJ35EI9Khcz6-hkiLa7n3ZetLfrac1r8qIi6dLmhr2TPuaYCvw47tNhvDJXKpBvBm8yLqHD8-G7otoEZuDKyhgAx0b4vF16LehrWHDjpUXRKJiv83at0hSgiUsbQigmcwf_ru3psho8e0KwQXVZRCd6p-wNtjR52PjS4Cg2dB7ZQHDUwGy2o1MxhqFn5-50D-J3OjmcRjw7fdm8dQxMaJaYgHXaVMTuoT0NEb-JSAkTM8kAdopXm6uZ_AeiXJCdxBTHULhcz6ENUB44g11aGg6W2VsImDY609K1cRlLpqBUSHMOeDblcdAWXOLwhYCY3-V6vUtFLck_WHwaIKrYC80RyyWwQ-CMPxYS69hZnVkQFSRhR6FLfVjENU80S4eqBSrBpvpW3ejfN-25b3HfQdx5psGunnH6ZFUzzfMQ5WnvSmKnrkMjA9Y145pAmOfIQkAVeRH4VcDnq7sI1y2dS_3HsSoa6eXFw6DYdEnrqONSjE_f1WXXz5x9qlUo1msZ0BYd_ZW8rdCKcKtGBidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف دلِ مردم عراق دربارهٔ رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451198" target="_blank">📅 21:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=YXGUwlfEBTB15tr6mtHL76fEwSlfJ7q_ctdmQ1YRMqAsUvnYCLIBTJPhOp2Zy_zEHkXK_jShzkWgqyQXKuZ5mB9IiZG1OfnC02YABRanar5Vu1DgC4Yy3rxQRjzJnHvDtPCY4i8jzc7A12fd8rRJ255tGJiZXcAWV3b9pkzmhME9fm12x0bi9enKYwkCaYf0f7QIkywa1K6SO3IpB-aYgqrIPLaGDwHA4Jhs1jrHeorOzB_yKTovn77WZjeZJztxNV6clYUrtnWLzBVT4z4j2f8tQXupvZtcALMJNKV-4IidIGYZtN97nz1FX8yEvJDWvNxoMN_2y1n_M5lVGzb9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=YXGUwlfEBTB15tr6mtHL76fEwSlfJ7q_ctdmQ1YRMqAsUvnYCLIBTJPhOp2Zy_zEHkXK_jShzkWgqyQXKuZ5mB9IiZG1OfnC02YABRanar5Vu1DgC4Yy3rxQRjzJnHvDtPCY4i8jzc7A12fd8rRJ255tGJiZXcAWV3b9pkzmhME9fm12x0bi9enKYwkCaYf0f7QIkywa1K6SO3IpB-aYgqrIPLaGDwHA4Jhs1jrHeorOzB_yKTovn77WZjeZJztxNV6clYUrtnWLzBVT4z4j2f8tQXupvZtcALMJNKV-4IidIGYZtN97nz1FX8yEvJDWvNxoMN_2y1n_M5lVGzb9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحید شمسایی: در طول تاریخ، خاک وطن را قهرمان‌های گمنام اما شریف حفظ کرده‌اند، مثل همین مرزداران جنوبی؛ ایستادن کنار شما بزرگتر از هر‌ جام و مدالی است
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451197" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=ktotWAEFUzNUt7ajStD_8zPVRhNr-cdR-eiWV7-J7X0XOr1UTeMw9RhGzDmzmV4HTAn7yY5j0_k2jgce3gQ_y7SS_sNjZr3zqXJXzUkepn6uVBSUidg40YQItp_E0Ip7G71r8zvmh6qWhd2U16_djZ_nMD-WGLSXmYTCZk5YolHi_PxNAsvqN0Oa27BqNC18V2byWCPqHguafZ-Edx8W8TXZs7oLvF1Vd9AYqAQXjDiUFN4h_hXEcyxFOY4Ym1q8X1xhjfGLIqxbs6PtgzvKMFRenpuyDsG9YRuIsWYPVmLNAIBVhPhY6ybAhrIv8QYD774WE0cGWvtOk1RsCk2o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=ktotWAEFUzNUt7ajStD_8zPVRhNr-cdR-eiWV7-J7X0XOr1UTeMw9RhGzDmzmV4HTAn7yY5j0_k2jgce3gQ_y7SS_sNjZr3zqXJXzUkepn6uVBSUidg40YQItp_E0Ip7G71r8zvmh6qWhd2U16_djZ_nMD-WGLSXmYTCZk5YolHi_PxNAsvqN0Oa27BqNC18V2byWCPqHguafZ-Edx8W8TXZs7oLvF1Vd9AYqAQXjDiUFN4h_hXEcyxFOY4Ym1q8X1xhjfGLIqxbs6PtgzvKMFRenpuyDsG9YRuIsWYPVmLNAIBVhPhY6ybAhrIv8QYD774WE0cGWvtOk1RsCk2o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از طواف پیکر امام شهید بر گرد ضریح حضرت عباس(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451196" target="_blank">📅 21:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iiy3GBgn5tXTMdg5ZxKu2UJQsZL-clmwbYpEB5pZTD96Gs5kKnCKPpkc6r8H-M-x7cyB1HtUibhyCPeP-edQT_i0ZrSRfK_4dLVd0cpNZJ4M2IQ4OtyZN7vYVvlF81iOnc6mJKgJS713uvAheFBkTP-DFlSfR3uXEf8w9C380kpQI9kJiP398fi7wbxxfUrP7wcDYufCOaQioKFReT2N9mXpKU7ZzhLV3SVAw33MOGvNIkKsJdp7yXMWeXPbaafpN_jbkNFrPKHCnySgwRnRwbSkT32p3MlPxccrVTdDwmkymFlZ694qFLuDWFr1SN3cJ-gnAjLpfWbgl_pZsNqksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9ZYyEXISSXtDqgmqHI0jVpwwXv-0MiI5Sp_T12YWAinktsNU7kXjTTH9cib-yGzoxNLUBG36K4RZd1f3-H21-njd3pkr1-CwEvH2Wxz57oye9U-Xld1Jl2kDhRgrzu6kAfgADwe8yeC84GoXrgAFNZzjfRo1sxclpb5dsf52jbZzPaN7T6RWNjIcSaemWJSi8Xwpg4UGCkB2Nwho3-xDcI8nPODISBqzNa6vVslXIz_PAVPtuHeAFYFMMA2qxrXrsXcfCo6tw_jI6uhOj3YQrvoumRoFtvcgKxOoiIVdjSiLYp-FTakQuAJtiVd6np1X3C2HtzHiHXljijseR1czg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ترکیب اسپانیا و آرژانتین برای فینال جام‌جهانی اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451194" target="_blank">📅 21:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChLYB8ovwnzaNlEPOaHTgssplDFuy00yE5kF9KKVd-XH2CaHZHU-dT-BguF68frYTbxJML7uvAJ9XYkOdq8SnBOP4bqNBg3eYhmhr-q4H_kGEnYrciBDc_f3O7j3ToUAv_PqsdKySkBNbMVBH-ZcppMLj_M2cNLMPLnETMYNiCMfy2uV2FxETCpkhJMktyYnSq7-TqBQIUA2_tQneBFKFTAvMvWGIu_7M9Xq6WDEf5GzXei2dibxZc08CKEq54BR5aHNaUy6m09FwwvHuuNCQ2ogXEDjOMc6LXESDtN011NC3o4KrnfqKyi_brSKxJcgxA_Lje8bIOfPkQfVBN6ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق(واع): علی‌الزیدی، نخست‌وزیر عراق آخر این هفته به تهران سفر می‌کند تا تفاهم‌نامه‌هایی برای همکاری‌های بیشتر امضا کند
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451193" target="_blank">📅 21:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d34164886.mp4?token=GNMpFnJlaKYySa8yeWEkaMfX8pygkrFbiIlO1sJcmw4lHtWgBl5eZ0erAZsgUwbRYhc11K3DkYSgco3yP88_6UvtYXX0ZN-_OfCE9NfI9lMoVCBTR6E85x2qH-zP2Mu9YPEukkFg8hbms6DTiMkaP5LfTrLZHDRUu_MsM9jEi6MPHFgWGNU_F1bYhaaX6jTdg7Xk92gOKGW3a_L3XTlPfuyu1acq_aFEs2QFAx9IYqv9SVKrKRC6MrBMwR_rMifsvzfMqILhB01Y1zTkNQ6XsfR5YQdBMT0w1flyT7Ro3pTfmqubyXw_itWCgl6WCYVXtxqU37hi5H0QKR1-S48XvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d34164886.mp4?token=GNMpFnJlaKYySa8yeWEkaMfX8pygkrFbiIlO1sJcmw4lHtWgBl5eZ0erAZsgUwbRYhc11K3DkYSgco3yP88_6UvtYXX0ZN-_OfCE9NfI9lMoVCBTR6E85x2qH-zP2Mu9YPEukkFg8hbms6DTiMkaP5LfTrLZHDRUu_MsM9jEi6MPHFgWGNU_F1bYhaaX6jTdg7Xk92gOKGW3a_L3XTlPfuyu1acq_aFEs2QFAx9IYqv9SVKrKRC6MrBMwR_rMifsvzfMqILhB01Y1zTkNQ6XsfR5YQdBMT0w1flyT7Ro3pTfmqubyXw_itWCgl6WCYVXtxqU37hi5H0QKR1-S48XvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‎قضائیه: به هیچ‌وجه نباید بدون حکم قانونی، همهٔ وسایل الکترونیکی افراد ضبط و بررسی شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451192" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430b6db9bf.mp4?token=be_I0eZY8YJfAuyJK91_Cy_9frLbTlfZgTSmg7ZrUqi7bdoo0DoReO2fiosdogz7bAQbnyrQiSqUPjqQ64Lg9kELXY4NcH7MS8GmknLhcWUEIE09VTWCTUMt7DehKNaSn8llRTxgQa8_in9HCxVNzp5OSSTgPNV815ZGio9wAgPVoo2VOon-4P3k4U9euDVlnRnatugJDejE3oOdrS7-74EqhrU4nIsaPbJhu9-OZmw7zydwlx9ZSVE5p4WQS7uhHmzyvdQG8HwnRrxuziNX-j4E7l_-eoOYNN6TUdMuToBdcgmgeeJuxnK_Qe05wvuVedx2CPAzvZl0W4cgHWeYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430b6db9bf.mp4?token=be_I0eZY8YJfAuyJK91_Cy_9frLbTlfZgTSmg7ZrUqi7bdoo0DoReO2fiosdogz7bAQbnyrQiSqUPjqQ64Lg9kELXY4NcH7MS8GmknLhcWUEIE09VTWCTUMt7DehKNaSn8llRTxgQa8_in9HCxVNzp5OSSTgPNV815ZGio9wAgPVoo2VOon-4P3k4U9euDVlnRnatugJDejE3oOdrS7-74EqhrU4nIsaPbJhu9-OZmw7zydwlx9ZSVE5p4WQS7uhHmzyvdQG8HwnRrxuziNX-j4E7l_-eoOYNN6TUdMuToBdcgmgeeJuxnK_Qe05wvuVedx2CPAzvZl0W4cgHWeYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضایی که نماد بدعهدی آمریکا شد
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451190" target="_blank">📅 21:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e321f95076.mp4?token=W-VpXQsWi41mZAzDAj0LKmq9iMcG6REH4uX-wvDPwBr0JUIgprXCIbZwE9mo2CobWAaXPDiw2-IEQanBIrIaw_2cuCPsXiGKLbY5_pwUEPWcuKgmJKIzXSr2S3GumqxguRNpHzOTfVwBZBnCABdHgLaiCIG3dE7QtS-0W6uNinv_vwLptWnTjc8hYn1flJXoi9R1aAKWvZLbyIv1p5glDDsfENRpQi8RpPKJwpg7Dn3H60AUm06xw2-11Sh6mVBPFB96yUswrFfUns6BPaO0ZEMLRpkzhKRzFsiRSpC25rkYupfGpuj2Cu2jvGWSWtmBfr1hy4zLmUx3r3MfjoWDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e321f95076.mp4?token=W-VpXQsWi41mZAzDAj0LKmq9iMcG6REH4uX-wvDPwBr0JUIgprXCIbZwE9mo2CobWAaXPDiw2-IEQanBIrIaw_2cuCPsXiGKLbY5_pwUEPWcuKgmJKIzXSr2S3GumqxguRNpHzOTfVwBZBnCABdHgLaiCIG3dE7QtS-0W6uNinv_vwLptWnTjc8hYn1flJXoi9R1aAKWvZLbyIv1p5glDDsfENRpQi8RpPKJwpg7Dn3H60AUm06xw2-11Sh6mVBPFB96yUswrFfUns6BPaO0ZEMLRpkzhKRzFsiRSpC25rkYupfGpuj2Cu2jvGWSWtmBfr1hy4zLmUx3r3MfjoWDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ۲ نفر از عوامل بی‌رحم جنایات میدان شهید علیخانی اصفهان به دار مجازات آویخته شدند
🔹
قوه‌قضائیه اعلام کرد: حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، ۲ تن از عوامل بسیار خشن و بی‌رحم جنایات میدان شهید علیخانی اصفهان در کودتای دی‌ماه، بامداد امروز اجرا شد.…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451189" target="_blank">📅 21:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d20f8910.mp4?token=ga_LNhVhw5KsJ-uPF0w2Ro9NMKEyjug9FfedRsZxnTiYeNFKY1i4LOQ7Qp2dC7-W-HXjdkvRtGGMTJVsI_1E8qfAUwP9wj74X9ZdK4IxQ2TQvrsR1kAV3ajrU93zH7Lkp-pjdBGyFZEYb6Vo26d2eqV8trcmdkniYfod_8fp1ARSKG3Aaie35bQc8-4Gg385WBQTWPGby1arbY0JEUdpZQtPevsRRKAPrsQC5Hd5-7kxJ4wahng-Ot1T22zjcXJvGLtBXe74pVQ465tELGs4F6QyssCxxALozCNBL8j-mDxhwFZtqiGDCSZyFAuViVyeoOj1sjD78B8k2XHcwXKuZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d20f8910.mp4?token=ga_LNhVhw5KsJ-uPF0w2Ro9NMKEyjug9FfedRsZxnTiYeNFKY1i4LOQ7Qp2dC7-W-HXjdkvRtGGMTJVsI_1E8qfAUwP9wj74X9ZdK4IxQ2TQvrsR1kAV3ajrU93zH7Lkp-pjdBGyFZEYb6Vo26d2eqV8trcmdkniYfod_8fp1ARSKG3Aaie35bQc8-4Gg385WBQTWPGby1arbY0JEUdpZQtPevsRRKAPrsQC5Hd5-7kxJ4wahng-Ot1T22zjcXJvGLtBXe74pVQ465tELGs4F6QyssCxxALozCNBL8j-mDxhwFZtqiGDCSZyFAuViVyeoOj1sjD78B8k2XHcwXKuZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندرعباس، ۱۴۱ شب خسته نشد
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451186" target="_blank">📅 20:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
منابع خبری می‌گویند چند هواپیمای سوخت‌رسان آمریکا در این فرودگاه مستقر بوده است.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451185" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d153b0845.mp4?token=s5JWrDewBocvKdsvKHSAk83F8D9zRE6rGdJCDwDLg-Cy3a05LM2HTQ4TqAdT_lB6EPC3V3o7uSrKz9vw_izT6NdaBzbbb5lozzcpX26uUNcvp8hoMUvqz3YTV1rBMOIcADLE--pLi0VS-_Cj5Hkh1Yieyg9qsPoLCxOWJCN6frqJCVL73CT2fU7odIzLx3vsfkjRmTw86yheKEUs7R7lz4OHjXXvhNNaAuk7rq6FMgfgCjvU9SayRyK832ESonRkj4v6EGHaKNP1sLrfB2Uq1Irk5Keou6PIWbzI2EmQRycZwTom89I2bpGXV3aQuIfHLuW5T80PszmddOt0eK3I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d153b0845.mp4?token=s5JWrDewBocvKdsvKHSAk83F8D9zRE6rGdJCDwDLg-Cy3a05LM2HTQ4TqAdT_lB6EPC3V3o7uSrKz9vw_izT6NdaBzbbb5lozzcpX26uUNcvp8hoMUvqz3YTV1rBMOIcADLE--pLi0VS-_Cj5Hkh1Yieyg9qsPoLCxOWJCN6frqJCVL73CT2fU7odIzLx3vsfkjRmTw86yheKEUs7R7lz4OHjXXvhNNaAuk7rq6FMgfgCjvU9SayRyK832ESonRkj4v6EGHaKNP1sLrfB2Uq1Irk5Keou6PIWbzI2EmQRycZwTom89I2bpGXV3aQuIfHLuW5T80PszmddOt0eK3I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتش این‌گونه پایگاه‌های آمریکا را زیر ضرب برد
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451184" target="_blank">📅 20:51 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
