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
<img src="https://cdn4.telesco.pe/file/o9dZy5nQlUhSL222gtmk9640dRbnHsLVsUe3zxCjFF4TFWKqQp_lbfEj83AuxWBH7F-bqSoDBg3e_aDofWl_3soe6FsX_GxsDmhNyJ_Q_jggjpBsbNHt4jzZzrWlRAmqAKErtRZNKBGHQHrFr95JhJa9tTKvKOY75kUzqsxsdqdJGgcnH3lmm57gESSR1gmZ0P_LPjh594PNKQoFHInAmXSBTV5fPLgDhlq0kzxPopyHEh39las_X5QQu3vylqKd0-iNwwbiHrA8csi6qnfUqkBDRb-mo7R-TDkGG37_NxRr1alp4pXBtszy-gx6HL5RjPvvPSzu8aJ1RKW4Zi8NaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 14:43:39</div>
<hr>

<div class="tg-post" id="msg-137668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سنتکام: محاصره دریایی اعمال شده توسط آمریکا بر ایران همچنان به طور کامل برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/137668" target="_blank">📅 14:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137667">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین بی‌جواب نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/137667" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137666">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی سعودی دیگر در دریای سرخ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/137666" target="_blank">📅 14:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137665">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAeOaHH3QHp4F0IHrWgHtbY6xya0v-0ZOQNUYMxihQyrnG4y3m3hOmaZtTiSQoTI0UHdnPnB7bGy6D_dqjFIReW-utIq6IhHtRm6ZXTjKbNCFUDgWLcEShhd6lQLnuL2M7yDzXb4v6dqD6bBDIk2jb_vHdpcOGkbu_Nm6DkoNZ9z-0TogkL3csDT55kpHmi0A7RIIMNz9xFy_WtW2xhGtPc_2gRbpVNSCB36a09pnxBFqCGIqdK-u3vCq3WIMT_MO-XfNKOG85jpNbfJN22XUJi-vMISfqhe2XYVVC6Jhvyam4YhmBkAlkE67bSES7vSafEJqMWUoPDA1NU0Lax5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی سعودی دیگر در دریای سرخ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/137665" target="_blank">📅 14:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137664">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jogSyFJo5X4xnwe3aJwxlIIzuDZYi3jS5FT6g2chNyfX486E04nCsOrr0A1WLbxfm3siaMI9EhAfPVnXK9qGHNxPfOvDADS5LHx3RjSktkqpcZeVUl2LrrXH4jWOCoDhfguH5qcCrXw3l23BLLJwgGxwU9SBiPS-TPii9y5ys2GKsAUHq90mCzXuYlxnBfCxt9HqIQuLIb0kBVAuhws1gocsRm8IcI3v4YkJEWKcRi4Lp8Ee1DwlttfJcPbuTthqm99HLtcK-slqwuM29ydXK7byo3ch0Gb-sda-ooZfSjDsvjwvryy7IqA2BSm_rAgsjgIk9qe8hI7dmdAUyJfN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به دلیل جنگ ایران و آمریکا، گرندپری فرمول یک بحرین به کشور مالزی منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/137664" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137663">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الحدث به نقل از برخی منابع گزارش داد که امریکا و ایران پاسخ خود به پیشنهاد پاکستان و قطر برای ازسرگیری مذاکرات را تحویل دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/137663" target="_blank">📅 14:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137662">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: هر شخص یا نهادی با شبکه فساد «بابک زنجانی» داد و ستد کند تحت تحریم‌های همه جانبه قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137662" target="_blank">📅 14:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137661">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پزشکیان: حمله به پایانه بنادر و همچنین حمله به زیرساخت ها و راه های ریلی و جاده ای محکوم است و از طریق مراجع بین‌المللی این جنایات را پیگیری میکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/137661" target="_blank">📅 14:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137660">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUilH-39e4oco2F8p1QxyBaMOhpy9oyevOt3K6Yx4loTx1Y6A9NfeZorDtxUyFR1Gd6893w4BgBUKAx0234vwAEHrvjw2Xx0pOjNebEfrSyC04PTQpQslUGqpkhUcYB7GuU4zaV5a21_-ubZwiU6h4kKtQCNPwnbOw26W3zlXiVlrffoI9DUpEnGgINWy63MAtr1sSOXOavexhKSQpMMlfdPvtisFNWy6j08t5BNqxPEK1xT063O9SHcWVoXrdAoH0I0L25lDuBO7fGR93fcki7e4lwv_jq0FkesWCJZPHKGFul_56uqtfz-B7K9fj3CKC_xCiyMoCT2rZFIX-i-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گزارش شبکه NBC News:کمبود موشک‌های رهگیر به حدی شدید شده که فرماندهان محلی آمریکا ناچارند تصمیم بگیرند کدام پرتابه‌های ایرانی را رهگیری کنند و اجازه دهند کدام‌یک بدون رهگیری عبور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/137660" target="_blank">📅 13:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137659">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwAIr60z2AMew5vu1KH8r5qWphB52AQ7uMwIKCoMmZg68X28VmJbIks-UfZrpTBb9_qRnT6XA-ZPo4u91Zc-Rn-QaRZcoqMVtojQMVvLnfbf8iK9ydeV-2JYKD0kid4ZEGZz9eicks6Aqdk2c4CwmLf_2UXSiwmMT1xpVDVyXwCSfZkNod87ZEKdg4s6nZKb9RpjOemuvXzvdX9eMZEyuKEhN4jqy1gdMpq4gOEZQ3Oqezo8zsTepYacdBytuyOamhNbfYecrz6BwCkJCzyvSTKLQ-iEcF-A7Rq70gfqN4iY5fQ-0-7mg54SIyA9Oe5WdlMB6fSJWrWu-qeB_OFN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد الشرع: قصد دخالت نظامی در لبنان را نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137659" target="_blank">📅 13:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137658">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd19d716.mp4?token=GI--pmVHOjvHn5y5jbhI5JeM9H6a6EW3XWksCtUZHouStlNwgNKzz2uUfdFOWNc_WJ7hjSVWgX9RuIlfrJN0M1rTreqXVnUY8y147mzTdPx5JjUK7IOdoXIyUWKqnpQltk1vTpzwSFGZFVl_Km_F5oOg_xqBmhGJtDKw5xLzeEJribdCGebWTR_sQHmU7N9p_qONi19EW3cL30C2FpNEUMf6oZcsR6Li4exDDkdOkHbHmJe-YCbmbVx0vXNwy-ndeiTQndxYilhdD0HuxqwM1t_v2MIrVkFwQ7ahtL95mBr1Yrcv3jsjEg8ig36_SpkfqvCWK5qsqdOYNInkjRiGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd19d716.mp4?token=GI--pmVHOjvHn5y5jbhI5JeM9H6a6EW3XWksCtUZHouStlNwgNKzz2uUfdFOWNc_WJ7hjSVWgX9RuIlfrJN0M1rTreqXVnUY8y147mzTdPx5JjUK7IOdoXIyUWKqnpQltk1vTpzwSFGZFVl_Km_F5oOg_xqBmhGJtDKw5xLzeEJribdCGebWTR_sQHmU7N9p_qONi19EW3cL30C2FpNEUMf6oZcsR6Li4exDDkdOkHbHmJe-YCbmbVx0vXNwy-ndeiTQndxYilhdD0HuxqwM1t_v2MIrVkFwQ7ahtL95mBr1Yrcv3jsjEg8ig36_SpkfqvCWK5qsqdOYNInkjRiGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : فردا برای دیدار با ترامپ به واشنگتن می‌رم و درباره ایران و سایر مسائل مهم گفت‌وگو می‌کنیم
🔴
در کرانه باختری هم عملیات ارتش برای بازداشت افراد مسلح و جمع‌آوری سلاح ادامه داره
🔴
همچنین از اقدام آمریکا علیه دیوان کیفری بین‌المللی حمایت میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137658" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137657">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا به بی بی سی:
ما آماده پاسخگویی به هرگونه حمله‌ای هستیم که ایران علیه بریتانیا یا متحدان ما انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/137657" target="_blank">📅 13:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137656">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQVoVi77g0eAoUaB0_h4Poqu14LWGcU10QXYYLK61xep-Mpd5YFNL1byHXc8xeG4jvKLbP6GUHBp17ZcdCpyQH0JS7v-JjhCE8gk6IumPUd2riJgXE-AIQCqD1DR9haIeJPbs32xU_U6WiWVruC7vieUYJf1tWfZQAmfJ0hx_yxukLHud3E4DCtoQxA_dffplrhFXpLmgZ3SM45Yf36_Rt0rcbZjlnApp4ClhhZsdsihiIOeO5bqFSYBqo_huFFl98aJKxE3wttJGQibP6fF4_gEa1MfptwB2X0Npe1D3ex-izLGe5sT6Sg6a_5QDO6rGSjLk-6hZUQLKOkB2mwQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نرخ مصوب برای ۳ محصول لبنی تعیین شد
🔴
کارگروه امنیت غذایی و تنظیم بازار کالاهای کشاورزی، قیمت مصوب سه محصول لبنی پرمصرف را تعیین کرد.
🔴
بر این اساس، قیمت مصوب سه محصول لبنی به شرح زیر تعیین شده است:
🔴
شیر بطری یک لیتری با ۲.۵ درصد چربی: ۱۲۰ هزار تومان
🔴
شیر نایلونی ۹۰۰ گرمی با ۲.۵ درصد چربی: ۹۱ هزار تومان
🔴
ماست دبه‌ای ۲ کیلوگرمی با ۲.۵ درصد چربی: ۲۶۵ هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137656" target="_blank">📅 13:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137655">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سرلشکر صفوی : نیروهای مسلح ایران معادلات دشمن رو به هم ریختند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137655" target="_blank">📅 13:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137654">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عراقچی: ما حاضریم روابط خود با کشور های همسایه را از نو بسازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137654" target="_blank">📅 13:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137653">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da6ea7622e.mp4?token=Q34Dx2kGCEitCpl43dyNqF3b-ylu0nrzSRjsMsE7e8bLdFBezsCpuLos3kIXBNAPL95UhVoI8arggTv5H4DomzMlr-I7IGYq1hBwIwwhVlCTTpLfaRUOi87ZECid0_vvASJCgwMx1FwG9eZZQZy84OJczJBC1fF_Co3eatq4XROG-Fo4S37nIk7OGEShckM6jLb5Nh3gLgcQkho4VhCQ8WxhpLdSMTnmY2CCM01HHHoghy2HETqZsueIIshn28Se5sFSMlAc9Y9bkH6YMYJDC7eaqq6qTyxD3guviCc2PSRAzAgPpovOQ-yuGJtzj4ZVYlBBVEjnXCNOWhC7_WKd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da6ea7622e.mp4?token=Q34Dx2kGCEitCpl43dyNqF3b-ylu0nrzSRjsMsE7e8bLdFBezsCpuLos3kIXBNAPL95UhVoI8arggTv5H4DomzMlr-I7IGYq1hBwIwwhVlCTTpLfaRUOi87ZECid0_vvASJCgwMx1FwG9eZZQZy84OJczJBC1fF_Co3eatq4XROG-Fo4S37nIk7OGEShckM6jLb5Nh3gLgcQkho4VhCQ8WxhpLdSMTnmY2CCM01HHHoghy2HETqZsueIIshn28Se5sFSMlAc9Y9bkH6YMYJDC7eaqq6qTyxD3guviCc2PSRAzAgPpovOQ-yuGJtzj4ZVYlBBVEjnXCNOWhC7_WKd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جامعه عاقل میلیاردها دلار زیرساخت و نفت و برقش رو فدای لجاجت نمی‌کنه.
🔴
اما تلخ‌تر از شعارها، لم‌دادن و بی‌تفاوتیِ اون طرفدار حرام زاده حکومته، اون‌طور بی‌خیال لم داده رو مبل چون نه نگران سفره مردمه، نه تاوان ویرانی زیرساخت‌های کشور رو از جیب خودش میده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137653" target="_blank">📅 13:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137652">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLyNBJejp0YiMvO-H2Zu7qZRBnmL1c0csa6p7hEoRBPkfLJ5VrcdfNATLmRDZOhtMwTW1Nzbivt_6l0ZAgCG-eMGaRR-BUplebfygLiW8PKlDqoRj1woP5RT7qsJ_ROQJiZr1jRdx85m_D6EM-g4ZEel0jAfyC41DLu_aejmasq6yWKidrB1FNqnhr6nNWWU6Q9mYU-0glHxrHu9jIQJV7vz4fLjnjLrp8rwcmvGMeVI4k-t5gSb-LAU71agCV-P5cUxNMhG5TTFJ4WLOcozIzDXgjXxLC7wlWqZl2_lM4zt7gsRJHINeuse94ydCV0nbhiaa9BOB1r1w5Bd7sbmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته دو مقام ارشد آمریکایی به نقل از ان‌بی‌سی نیوز، فرماندهان نظامی آمریکا به برخی موشک‌ها و پهپادهای انفجاری ایرانی اجازه عبور از پدافند هوایی برای حفظ منابع محدود رهگیرها را می‌دهند.
🔴
با توجه به پرتاب نزدیک به 9000 پرتابه از زمان آغاز جنگ توسط ایران، نیروهای ایالات متحده اولویت را برای رهگیری تهدیدهایی که مستقیماً علیه پرسنل هدف قرار می گیرند، دارند و همزمان حملات به زیرساخت ها مانند باند فرودگاه، رادارها و تأسیسات سوخت را می پذیرند.
🔴
هدف از این رویکرد حفظ ذخایر پاتریوت، THAAD و رهگیرهای سری SM است که پرهزینه هستند و جایگزینی آنها ممکن است سالها طول بکشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137652" target="_blank">📅 13:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137651">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی:
ایران روزانه با نزدیک به 20 میلیون لیتر کسری بنزین روبه‌رو است.
🔴
واردات بنزین نیز در شرایط کنونی به‌دلیل محدودیت‌های منطقه‌ای و بین‌المللی تقریبا غیرممکن شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137651" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137650">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwspjOYe7WUJf08rBJNBU9stD4d86NE7TKz0DviCCRb56cRz8mi7b4HhzvCo8C7p32_IHGXYbMLW1_lF4aj_LpTUDzn8Ox3lvF2KRB2azMXoWSetzobUw2FbK_Tk9nz-HMNCIJzbbjT3nLqRk1veHsbT7VVUrudpkIjK5KAKb6MEX6wwsFdHJ2pFD6ET4VCk6mlLRYbXyb1-RO9UfZU7kgGO2Q01zjo1OpVi9UUhg0s97KFvOYYgk3rCqrR86dC0ddRGSTTPRhkkZUxbi5lSplXFzArteA3-d9WpKogQQFykgP06WNM3hvqAVdPULIkpIg8n07Vk7PTuGEt0eNYn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۱۰۷ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۰۰۲ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137650" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137649">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqStHbMnxuHiJEBjacLhrw83WcKoF6piK9RzIr6ttrA7cPvcvWq5F1sk3gN5yNjsc6Yh2tLpv2_oqp6_I-wdAJwSRBGwQhDd9NdZ5xGl4cocRXaP1Exui_GNhEDiuz2uV9kWnMpadkOV4uf9H5UJPcpOj3IyqqA17vPanh8f1IDIA2p6AGaV5foaIBEVUmtA8tqTADbvQSS1TmRLXbzUkIsFzY3gtOyju6ts-gIfS58q9FsoDzoY79yaaB1Y1TdNDMTQviObGJPw3pkx1xZYWGUFbWaDjtNVCaToTnpYjq4X3SfDBma0tM6er-KR_CWNxUHMv2AICme_NbHwVXsS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریایی بریتانیایی: ما گزارشی درباره یک حادثه در جنوب دریای سرخ دریافت کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/137649" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137648">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ، انرژی هسته‌ای را ترویج می‌کند، از جمله توافق با عربستان سعودی. خانواده و حامیانش می‌توانند از این موضوع سود ببرند.این توافق به ثروتمند شدن ترامپ، خانواده‌اش، مشاورانش و سایر افراد نزدیک به او کمک خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137648" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137647">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نیروهای اسرائیلی اطلاعیه‌های هشداردهنده‌ای را برای ساکنان منطقه الیرموک در غرب درعا منتشر کردند و از آن‌ها خواستند که از هرگونه مانع‌تراشی در مسیر پیشروی نیروها خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/137647" target="_blank">📅 12:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137646">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy0hNKDmpp9N-Qko91Kpm8v0X0d36jcuKM0X2MUc5yAnBpAtKNeeNYUOCXx_UIfi3ddt77fWDGLaiJ874G3zgISPzZFqN1JcoY9UblW8H6rnR4SD9vrY5mctgGCBG2SwWgut8x0lu3G7SvIyS3M7nk15nZNd3ZkrdO5B-vEK2jUzwmfY8LK_3DmCDPAA3OUahD2gEY90zFBe19-nJVuLv-K5ce4xB6kCFvsCZ_FRyFoGWdJhBgWCXHHn3-1yKdNkinZw5Jpid8QK_rgUu6DyK2Z5r2_iizQuX45Po1kfcYTdzG5QoiQa2Tye5A28R4EGeYBJCvxcDUVYbep8qaHo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازهای ترابری نظامی آمریکا به خاورمیانه همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137646" target="_blank">📅 12:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137645">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/137645" target="_blank">📅 12:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137644">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
غرق شدن یک کشتی ویتنامی در دریای جنوبی چین/ ۴۵ نفر تاکنون نجات یافته‌اند
🔴
یک کشتی ویتنامی با ۶۲ سرنشین در آب های دریای جنوبی چین غرق شد و تاکنون ۴۵ نفر از حادثه دیدگان نجات یافته اند.
🔴
تارنمای خبری «گلوبال تایمز» با انتشار این خبر افزود: یک کشتی ویتنامی به نام« KHOI NGUYEN ۱۸ » پس از بروز مشکل در آب‌های نزدیک صخره «یونگشو» (Yongshu ) در جزایر نانشا واقع در دریای جنوبی چین غرق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/137644" target="_blank">📅 12:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137643">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی ارتش: با توقف حملات آمریکا، عملیات تلفافی‌جویانه را متوقف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137643" target="_blank">📅 12:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137642">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یک آتش‌سوزی گسترده جنگل‌ها بخش‌هایی از منطقه مادرید در اسپانیا را فرا گرفته است. آتش‌نشانان و نیروهای امدادی برای مهار حریق در محل حضور دارند و عملیات اطفای آتش همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137642" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137641">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مارک اسپر، وزیر دفاع سابق آمریکا:
بر خلاف اخبار فعلی، ترامپ در آستانه تشدید حملات علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137641" target="_blank">📅 12:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137640">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شایعه مجازی شدن سال تحصیلی کذب است؛ آغاز حضوری سال تحصیلی جدید
‏
🔴
وزیر آموزش و پرورش:مجازی شدن سال تحصیلی آینده کذب است و متاسفم که بعضی‌ها شایعاتی پخش کردند که آموزش و پرورش سال آینده به صورت مجازی خواهد بود.
‏
🔴
از همین الان تمام تمرکز ما بر اجرای آزمون‌های نهایی و پایان ارزشیابی تحصیلی پایه‌های یازدهم و دوازدهم است.
‏
🔴
تمام اهتمام دولت جمهوری اسلامی ایران و مسئولین دولت و نظام تعلیم و تربیت این است که آموزش و پرورش به صورت حضوری از سال تحصیلی جدید آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137640" target="_blank">📅 12:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137639">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279c2568c4.mp4?token=dS3shC9ANhwkSH4c09is-8l7bG_7fKmHz8sMR2n5BXhaVut9ugLPx4yEpR6PNRKex1t4vmI9WKaTyEnfVwZCCzMvLlRpDZCi-gzeKFuM9EyWLv5kyh2XTDd8lcI5XkE6V0GbP287fbzWGr6HZByAR-mvD7EIqBQODeKeNoINP0GsrArdKPWAExBrcPlX2GQNO-Ny64exl_nMac6FwHWU9JntpRlbaaRPjDbBuMepfQ1p0h8rPorX0G-LbIlbecQ4iueikbSsLrDWGkyM2rtvLBJHWMPxK8JUK2CfAbmB4Qogh_LI5hvOnD-XEBH7c1q8zrWTm7NG1bKR6AWHOYOsH4Opv61RkD0_Y8JkMpwB_d-McjZseQmQeuPHeYoqZIFBc8wgTpbkfPIJdxs4G7v7XDSn-ojw5nOf_FPJa6jxWK_sR7qunJGhM2jNaehiCsDG1CezED3P90-vk7urtjuprF2b9Wqo0a_uYx7H3-WC5ndOOiH3akYN-U2RI7QGDZKBRTrAS-mDj3x7yE4fFiVGhD1XJsaJzzyBC5NCURENYeWb4EagGXKVIRLAwDizxD6JlMqU9zLnMHjBcGfZUPxSyTkEmnFprdBEym1ugQ21wvhV2nRXSd1YjfexyGeaIUzGXJTp6T4oFd2Lnvtmh0ZKiTpQorJ2ZSPHXop5M_92fso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279c2568c4.mp4?token=dS3shC9ANhwkSH4c09is-8l7bG_7fKmHz8sMR2n5BXhaVut9ugLPx4yEpR6PNRKex1t4vmI9WKaTyEnfVwZCCzMvLlRpDZCi-gzeKFuM9EyWLv5kyh2XTDd8lcI5XkE6V0GbP287fbzWGr6HZByAR-mvD7EIqBQODeKeNoINP0GsrArdKPWAExBrcPlX2GQNO-Ny64exl_nMac6FwHWU9JntpRlbaaRPjDbBuMepfQ1p0h8rPorX0G-LbIlbecQ4iueikbSsLrDWGkyM2rtvLBJHWMPxK8JUK2CfAbmB4Qogh_LI5hvOnD-XEBH7c1q8zrWTm7NG1bKR6AWHOYOsH4Opv61RkD0_Y8JkMpwB_d-McjZseQmQeuPHeYoqZIFBc8wgTpbkfPIJdxs4G7v7XDSn-ojw5nOf_FPJa6jxWK_sR7qunJGhM2jNaehiCsDG1CezED3P90-vk7urtjuprF2b9Wqo0a_uYx7H3-WC5ndOOiH3akYN-U2RI7QGDZKBRTrAS-mDj3x7yE4fFiVGhD1XJsaJzzyBC5NCURENYeWb4EagGXKVIRLAwDizxD6JlMqU9zLnMHjBcGfZUPxSyTkEmnFprdBEym1ugQ21wvhV2nRXSd1YjfexyGeaIUzGXJTp6T4oFd2Lnvtmh0ZKiTpQorJ2ZSPHXop5M_92fso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع طوفان شدید در منطقه روستوف روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137639" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137638">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1dc51b5c.mp4?token=gi8klRoK95N-y1X11MTOsXXJwceIrwzZrOTeqtfo7fHxYLmPXGtUdi6BOUbZZmwZC3fCRkYpuz5pNiaxUR6ay6ozL1vCyBFL0dNaW83GaQSnn-wiRwt_HAbd935QQlco7WleS5meutTQRSVjr4fDhYKUZr9QWxzsAeaQv6OLtSgFhxPyHQcwTBFxMHfZa76-7J2353cOEUTQo1DobmphtWVVl1INPZn9kw83voSfgO3s_IKCz9v3-d7ZpsFnsPpV34lmR1Wef3H3HLBZOW1YlWMh_l2SzAfgsmUO4A81izJOt0xUvuPmDM2NSg2ya13-WoYf9Eliyv--cORSlA3rTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1dc51b5c.mp4?token=gi8klRoK95N-y1X11MTOsXXJwceIrwzZrOTeqtfo7fHxYLmPXGtUdi6BOUbZZmwZC3fCRkYpuz5pNiaxUR6ay6ozL1vCyBFL0dNaW83GaQSnn-wiRwt_HAbd935QQlco7WleS5meutTQRSVjr4fDhYKUZr9QWxzsAeaQv6OLtSgFhxPyHQcwTBFxMHfZa76-7J2353cOEUTQo1DobmphtWVVl1INPZn9kw83voSfgO3s_IKCz9v3-d7ZpsFnsPpV34lmR1Wef3H3HLBZOW1YlWMh_l2SzAfgsmUO4A81izJOt0xUvuPmDM2NSg2ya13-WoYf9Eliyv--cORSlA3rTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
مجری فاکس‌نیوز: اگر آمریکا نتواند چند ماه قیمت بنزین ۴ دلاری را تحمل کند، دیگر نمی‌توان آن را یک ابرقدرت دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137638" target="_blank">📅 12:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137637">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo6ujMKDjVn5tVjcyLh1WTsnzIlDpTcE9qgEx0JO38v_KYyBICO_HlOz985p1Dmg2RXDq94G3M-EWVjPXxJrJ9NkHnoJMQ1tN11SX9DFYK1fSmJcdMNZT4gQAVGfxAE-rCynRwaW-13JqWCPnVniM6gpcb15oBXzU9oQMeeg8IBXJz03He7RxjiCCxWPiqEr0tG_FfCe-BPLrKWicOvcE6ieycfUqaJ0bmrt1DGwvG2-EJo_8GAElBySGMKSZbbYgmk7Jy-TP9VfXn_Xlbl7ThKiJSFHtGV0PC0akoqnfhq_28Oz_-5682YDUJJMpwx4VRV6yi_EgM3YBEH9z6kosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از زنده یاد اکبرعبدی و گوگوش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137637" target="_blank">📅 12:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سلیمی، عضو هیئت رئیسه مجلس:
برای برگزاری جلسه رأی اعتماد وزرای پیشنهادی دفاع و اطلاعات، آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137636" target="_blank">📅 12:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
روسیه با شدتت زیاد اودِسا چرنومورسکی اوکراین رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137635" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
علی قلهکی از احتمال استفاده آمریکا از «بمب اتمی تاکتیکی» برای کوه کلنگ خبر داد
‏
🔴
بازگشت تیم عمانی به مذاکره و آمدن به ایران برای مُجاب‌سازیِ تهران برای همراهی با شروط و امتیازات جدید واشنگتن و همچنین مشخص شدن سهم مسقط از تنگه کلیدی هرمز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137634" target="_blank">📅 11:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7154967b4b.mp4?token=uTImN2hcw-w4KHIOWOtLoG4_kCCgCpdDh4Fg9i8aSs1PrwyqJb6iTjrY3gnzNHxUNnS5zT9EsqyBZS4zmgErkOD_cnJdlc_wL47GmHvwVXb4H9a9lkOw76wNgMpU3pZ45m5rPDBXaM7D-1TKEry0QjWVGm1Ovj4kRV0nFE2zoAfPjlBVFGmfM_C_lpWfXCkjG8nC3SrzbBFGOisGpgB9NDWJs2bTtsYZdGQ5IJea2Q0rbyJkx-r-uGsvEjsiLkbgg4I97KDkN1yarZiHciavj1DSKHJuHD6PgmG07NbMzn2akxgTd8zIFx5GxHjIZpTIxo7qDtH8_Zabn5kbSapd2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7154967b4b.mp4?token=uTImN2hcw-w4KHIOWOtLoG4_kCCgCpdDh4Fg9i8aSs1PrwyqJb6iTjrY3gnzNHxUNnS5zT9EsqyBZS4zmgErkOD_cnJdlc_wL47GmHvwVXb4H9a9lkOw76wNgMpU3pZ45m5rPDBXaM7D-1TKEry0QjWVGm1Ovj4kRV0nFE2zoAfPjlBVFGmfM_C_lpWfXCkjG8nC3SrzbBFGOisGpgB9NDWJs2bTtsYZdGQ5IJea2Q0rbyJkx-r-uGsvEjsiLkbgg4I97KDkN1yarZiHciavj1DSKHJuHD6PgmG07NbMzn2akxgTd8zIFx5GxHjIZpTIxo7qDtH8_Zabn5kbSapd2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مستندی از دلایل سقوط شوروی که توسط صدا و سیما پخش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137633" target="_blank">📅 11:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، سامانه‌های پدافند هوایی این کشور ۱۳۳ فروند پهپاد اوکراینی را طی شب گذشته بر فراز مناطق مختلف روسیه از جمله بلگورود، بریانسک، کالوگا، کورسک و اوریول رهگیری و منهدم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137632" target="_blank">📅 11:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrDE_Xly-khfL-EDEZF3WAc_cbdhkMl0m31lnl-cCM4rGONgHXGIq-Hb2YAM-oNuTdlV3uZ-9Cti4BnyN6RCP9o8ae-31UdPuGkGNECSa-XTQrthWrMajNHvQ1buqR6pqRPZzQW9kziKmagUp1NeGvrKItD7O2nwRMUOOT3a6SRxWDoeFe1Z9CR1p1A2wcOl8wMxfDdOLvGFIMCexJGEhokCatIB6UX0kgLTwpAJCzWZAhF72_MNhIFRX21n6d97j9gHZGJhFmYdCEx5a0wfh_OOvBtcqNmqLY95Q1N1jWmLA66KjkHNE4EMahbSgrUGPP5Pk71D5qA8NkGo0fZQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش‌های منتشر شده در "جروزالیم پست": عمان پیشنهاد ایجاد یک اتحادیه منطقه‌ای را داده است که مسئولیت نظارت بر امنیت دریایی، عملیات جستجو و نجات و سایر اشکال همکاری منطقه‌ای در تنگه هرمز را بر عهده داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137631" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بنزین بزودی لیتری 10,000تومان میشه
🔴
هر باک 600هزار تومان
🔴
سر سلامتی بچه‌های لبنان و غزه و هر درب و داغون دیگه‌ای تو دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137630" target="_blank">📅 11:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfbncKfB0TH07U3n0Y-gKH3zXFH449MIduz48Ku_ROJV1Z8WI99yGT8WS-2DdyG9HYz1l66ilA8V9CNcIEvdgHJuqvecb3rjI0R8bZt6xhhFne1-1pwKsUXaNEgN4OeZq54Rdg0_YF0A-8_1w59nqqcQk6PR9WtS60DIcweiadcqHOtNN-OQBtpmxRVS_6v2hszT3lA8C7kY2dreXlM4Y1ZpI9DbwEZLiYjxg9j74mNLxooIVnO1wfAKSs0L-XQLk92WqvJLzCNfF9m8JJ18q9bEiV1_4lELJyiFpcvvuDkAsDErMQTM0ldGOwilEMMzoMU0EZnfiyexI7Pb5dqeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنزین بزودی لیتری 10,000تومان میشه
🔴
هر باک 600هزار تومان
🔴
سر سلامتی بچه‌های لبنان و غزه و هر درب و داغون دیگه‌ای تو دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137629" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2973ce0df5.mp4?token=YWbtBw7vjq0yuAXRhzRVlUbxlrhrgo0XWX-yMVBvPAumL9EYITHWN2clhuDa9pvmfXu1V0mQv3TVGZfuDQlnCJq7epIbws6DMv_Nw_uK90Csy-4QfvU39FfMOjr5-tQY6fsJhwE_oz-IaYo8uwoLcEIUmKMFqGx3AkZA5t756dFsh05M6yAStgr1GZdbBw8LNOzv0-IyvEoqG6XdtT6airLUeL0vF-KM-hC4nB7nq4TMYuPCeKx-1ym3hiTV_WwwADWSYsYwh00BmW7vO-9RhQO_q4W4SZfg0jRhFvPMswnzSneRQ3i5GHbAv6EToYZGGdEvfnR_DgTc9LvD_7JOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2973ce0df5.mp4?token=YWbtBw7vjq0yuAXRhzRVlUbxlrhrgo0XWX-yMVBvPAumL9EYITHWN2clhuDa9pvmfXu1V0mQv3TVGZfuDQlnCJq7epIbws6DMv_Nw_uK90Csy-4QfvU39FfMOjr5-tQY6fsJhwE_oz-IaYo8uwoLcEIUmKMFqGx3AkZA5t756dFsh05M6yAStgr1GZdbBw8LNOzv0-IyvEoqG6XdtT6airLUeL0vF-KM-hC4nB7nq4TMYuPCeKx-1ym3hiTV_WwwADWSYsYwh00BmW7vO-9RhQO_q4W4SZfg0jRhFvPMswnzSneRQ3i5GHbAv6EToYZGGdEvfnR_DgTc9LvD_7JOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاید باورتون نشه ولی یه همچین نماینده کصخولی شده قبله امت معکوس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137628" target="_blank">📅 11:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a6283cad.mp4?token=LLnAVZjO0wMV-8b0phN92_w-GCRS9G_wukBYLmVWhsiETspEfLA8auze4SsO0V70T_rl-d3xlqK80ahWFqAT5HSIqjzv3u8yyBY6TQVsspd-Kz40MwyJIoD1y9f_Jjk1XGuVQVi_dcrNK3zY3PeyGgw-TiC-LqpgiGyC2_4zdN5zTmRYgYfwHnYfAYKqRJFFgisz6Se0h1F3ZeE2ZZ4ytPcGH4EvPtWlEjQNmEJcFiSjTiiVxHyRfi1Ws4T_XdUMS5OvlhUDUYJre8u_HC-JVKaK_jR6gPqHUUy9agOoUq07aZT988TwHj4V7yQZXew62iYLEDu7Tq54clOtOF0B7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a6283cad.mp4?token=LLnAVZjO0wMV-8b0phN92_w-GCRS9G_wukBYLmVWhsiETspEfLA8auze4SsO0V70T_rl-d3xlqK80ahWFqAT5HSIqjzv3u8yyBY6TQVsspd-Kz40MwyJIoD1y9f_Jjk1XGuVQVi_dcrNK3zY3PeyGgw-TiC-LqpgiGyC2_4zdN5zTmRYgYfwHnYfAYKqRJFFgisz6Se0h1F3ZeE2ZZ4ytPcGH4EvPtWlEjQNmEJcFiSjTiiVxHyRfi1Ws4T_XdUMS5OvlhUDUYJre8u_HC-JVKaK_jR6gPqHUUy9agOoUq07aZT988TwHj4V7yQZXew62iYLEDu7Tq54clOtOF0B7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علیرضا خمسه: اکبر عبدی یک جواهر و بازیگر خلاق، بی‌نظیر و تکرار نشدنی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137627" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
روزنامه وال‌استریت ژورنال به نقل از یکی از مقامات کاخ سفید گزارش داد که دولت دونالد ترامپ، رئیس‌جمهور آمریکا، از اوکراین خواسته است حملات به کشتی‌هایی را که «متعلق به روسیه نیستند» محدود کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137626" target="_blank">📅 11:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137625">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال روز شنبه به نقل از مقامات سابق و کارشناسان هسته ای گزارش داد، اگر دونالد ترامپ، رئیس جمهور آمریکا حملات آمریکا به ایران را گسترش دهد، واشنگتن می تواند چندین تاسیسات هسته ای باقی مانده را فراتر از کوه پیککس هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137625" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137624">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9154c6df.mp4?token=ldRr_1aIl_iUto6ZQIkVL1N3ckqoPrVme4jZSADW-7LLbtrlPYuKCOd6maVfgoEdkgiYOlPhJWiH-jTLmW8Fb6EGDLSeMxCjbBKNyypHeU2h9WwxQcVJof6NWa9SGCg--GPF7p-ssRiJawA5OSoFgHdBUDuhJ0YxaCQIk8EaoZOyAFcuyUKgjis98rvYKAbMvSGamIFEgLNO1gjR5ZRHU3rBi1-xLU4HRDhRsVrTG2vem4IjS9xXSkKHuNiwHrwJ7jybEdBYevCz9zx3wBD8lFKhRg9NsOYnk7gj2UHUbEh-kcm8I0nym3Es_T-ptsWbm2nZigd2xNHEWqHR9EGSoA_Eltg51La1vrww0gr3y91xy6o3bCBeRXdyQAG8K0h6UKQdTJkSIgqEyVjI88yWKKkCkbDFk8zQu7qubtFTIbMAb--mj4JCCBVlWGQ9djU1JoQSI-F2onOrWZvF1_XtaI1XvG80cQflUDbouQoDW4tSM2H_PciIhWwAu2HLas8W9cHTUO7DXq5qZj_4FERJ9DkXy09fGnKuroeIqi__xfEIe9Ome-A_bVckd7fDqQSqoKKh5VRTB156gNVWf2tGDi1r60b206jLeZoSpnRQgG0P9Yak8NHRwoGgd3KlzD1GzPwr_Jxz-9vAiR2lqCkmC-HpYSJqCxQVGZJO4d1gbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9154c6df.mp4?token=ldRr_1aIl_iUto6ZQIkVL1N3ckqoPrVme4jZSADW-7LLbtrlPYuKCOd6maVfgoEdkgiYOlPhJWiH-jTLmW8Fb6EGDLSeMxCjbBKNyypHeU2h9WwxQcVJof6NWa9SGCg--GPF7p-ssRiJawA5OSoFgHdBUDuhJ0YxaCQIk8EaoZOyAFcuyUKgjis98rvYKAbMvSGamIFEgLNO1gjR5ZRHU3rBi1-xLU4HRDhRsVrTG2vem4IjS9xXSkKHuNiwHrwJ7jybEdBYevCz9zx3wBD8lFKhRg9NsOYnk7gj2UHUbEh-kcm8I0nym3Es_T-ptsWbm2nZigd2xNHEWqHR9EGSoA_Eltg51La1vrww0gr3y91xy6o3bCBeRXdyQAG8K0h6UKQdTJkSIgqEyVjI88yWKKkCkbDFk8zQu7qubtFTIbMAb--mj4JCCBVlWGQ9djU1JoQSI-F2onOrWZvF1_XtaI1XvG80cQflUDbouQoDW4tSM2H_PciIhWwAu2HLas8W9cHTUO7DXq5qZj_4FERJ9DkXy09fGnKuroeIqi__xfEIe9Ome-A_bVckd7fDqQSqoKKh5VRTB156gNVWf2tGDi1r60b206jLeZoSpnRQgG0P9Yak8NHRwoGgd3KlzD1GzPwr_Jxz-9vAiR2lqCkmC-HpYSJqCxQVGZJO4d1gbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اندی برنهام ، نخست وزیر انگلستان: اگه چیزی به نفع بریتانیا باشه، جلوی ترامپ هم می‌ایستم، همیشه منافع کشورم برام اولویته
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137624" target="_blank">📅 11:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgqtvWRTWsPk6_wbHV8AayIfDdzGtu1fUIJF4cBh7FnV8Qbmtc6cZuTv9unyMqRQSkb3uTOnxmFEoQFI6rZBwfgyLuyM2S8uzmgb0Nsu-Gt7875831yCBmv3jhb9VjScRR9cKYtE0VH73803BbLEEm9Z-lNGaUbRHTXf5xS4wAjeo8-HyhgmYyDgQF4YWME5jQYdyHUgKoS36xbYHXmcR1y2O6aJkHOIh_sIgZpaOwLHCM667PTcrhbexNRuKD0tiN_U6__6KyquHtKi_9RPinUjx6ljDlZHAHSadaG27lMz_t99rDFmwTyDNUKHYdtBe-LkwuSyCczuLE5D-g6YpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137623" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
استانداری هرمزگان: احتمال شنیده شدن صدای انفجار‌های کنترل شده در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137622" target="_blank">📅 11:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfGwrxIMzDtpF6g5cNdVnaHE6RzQ0IY_5qHGu4savkV2sX4nd3XmxnF1qS7Se8FZdUnezqBB8r3QZzS9ZuWfaRnWKgQW_KHiBAA-CzQ1T9Nijj7I4-Cd9grxuPWZjzQry1p3dM8f1C_38lAsf80izp_2Dzs5hHkb0UgM7ng0VQsYfAN7E3AA38CI6QX2JonEVTg5xo9jK_Xpbi7lzKdZTOT_KF1DPJv4QofsHE1EB_GFMviHlruywGBqJe5DR5e5ebwv22iUJwujv29CLnIxg_Bphzdad5ClIbFf3w9Eob7u0PWraTurBFiWzdoLgAmMI1GhwKfE1icZbtrRcxqtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
تصویری از تابوت استاد مرحوم اکبر عبدی
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137621" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137620">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پس از نزدیک به دو هفته حملات متوالی، ارتش ایالات متحده برای دومین شب پیاپی حمله‌ای علیه ایران انجام نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137620" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137619">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEXt39TK4SDZNBKU2cXOMyfkMGqRNJ5iaMRr6MciUW1wqWLExoW6GCkRl4h9gOMU9mo6hbZZI6ulW4lBYeJp3-I77DNLp04-CjG8wG_3fKfXTxo6bF57A8HHGRIiZdG2bXW2XmpzcW-F46hIW5Jol1rkaas4QOyTH2z-Cg8Nc4aeeP-EDBfoFZ7X_Fbmzam7Y6zTUD78sb3bRtFI5_yLv_6Ke3H7SoZxcHRq1IKt23h4LlQwrt89jxhFRpmD4ISrZw9SIYc5Jo1xlfbW_U5mziXjpzPtU57TXgsZU8EXaaoiFj-vJprBW5RRXTe1YbhKrAzQ3opUBxCHFVtyjrkOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
هرکی میگه با آمریکا جنگ‌ نکنیم بی شرف هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137619" target="_blank">📅 10:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvMi_UKdN6KqqeyFZ9wDvSwlJNa89Dtk-W9a6TSK4Il-3ao4WpDoR8hLzhtMiSpkpRHkQssi2Ac5gubnUw68dyzgYNECcrkMXmVv1C2K55oc9kRuSsb5blg4nKMqoD-0Te4ucfWerUxYPpZYjYmQwkO3D5UCxpecJt-sY32P20lIcpSzg6o8UFhNAK0ALYM4NpAX4sn77pHvsvaC_8rJoFU2yuOgixr4vkygxELpymyJHvenbH77pio8FR8PLNLATU_83GKtQazk6kzDcy-3EzZGZGfNEI2v3Q0oLVZAtXkwL3pj1GPcTVbLzCDWXptZ2kzi2XeZzKhZSe7850EnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9E8-dCfd8yV3YZyeZIRvfNQyiKGjDJlzMEjs74u_yBGkgqIXp4FobVdyT7mJWIcpUyYL-Vje6DfZEjHdBJGXJuGr9Pgk-Qem1PvuaFgTxBZ_CZuhc9x0guAX5vMVeTY1CfpzdINWfkfFBnXSwLJChbNuL6lKY2lrDI0SJGIvhNBhyBbIwxuO2DOw4RpVQGVbZTGmlo2596a4dkwej3JsxN5Azgc_aZFgb5oQidD8opKlSBGRKC4BXT2qj_2hFDYjEDW-kFyvUnH74RRRl0fv5j2Mg8IJIoXH-HpqmeCsMZa6ufET-ct1Fa9ElwD_jnK02HZU2URUSrVv94bdYMCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVqsdPNFdK2k-0aQ4pu7oLxDWk2lRkB5kyDbsxe34A8M-ddj50MJbtn9qXE8ZZu7j1wpFdaljRYyhfvRKE8u3fjzSGyvJW7SOYVC5uXxWhB8AXH6lddCGnj-k58j1Bod0WvKfY_5s5PX-xM_WkHIERMIe31oYWzsbet724Wv_PdjOKRbz365biiSDufSL5Ktb_30oqfK8PzrRt86a0xmg3uFhQDqkxI8jQClLFuurhr7q9C3Nq4s2rKp8JwNbtjG3I8zZGcPoYYbfsuS6eyKg0Dv6bnovGuFkBi9kx5YiBRgr63BsHylQr-fu7GvZ2yqdSq9Zj2wjtPUP5ydQyIDSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بنادر کویت و عربستان خالی شدند
🔴
تصاویر ماهواره‌ای نشان می‌دهد بنادر کویت و عربستان کاملاً خالی شده‌اند. یمن تأسیسات نفتی عربستان را بمباران کرد و نفتکش‌ها گریختند. مقرهای آمریکا در کویت نیز هدف حملات ایران بوده است. از زمان لغو تفاهم‌نامه، کشتی‌ها به‌تدریج کاهش یافته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137616" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6cd690f3.mp4?token=pgpKG7xAGt2G4kfyWOoQ7j_a_klknHpcRaBkaQp_vzMQ6W5Nel6j2kQ0a60zg2g9wZSzNK0AkdgHZ8QqVz0y50oEjnyy1eExxKI8X3qElZLs6QsuqrChIj81RG9KrbhfP2UB-aP4mx-EnpiEJZBpXy1pv9n_Ey6XxsfNpd2SXw1M0p4fR2T7oYOUU57gAsqQ3ywrzAr-69s_e_BHFk21f2VE0_vXaQjn1SRHgEGj4H7YdM7sggI-4f9aD7iRZ-bk-HIBtnfe4Vy3AJTkC0tNc3mT9TMltQN5poyK0xhoRLoMI2CLFRgy2EVLCdMx30Lq1dqNlw4cF0aflIgq_tYyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6cd690f3.mp4?token=pgpKG7xAGt2G4kfyWOoQ7j_a_klknHpcRaBkaQp_vzMQ6W5Nel6j2kQ0a60zg2g9wZSzNK0AkdgHZ8QqVz0y50oEjnyy1eExxKI8X3qElZLs6QsuqrChIj81RG9KrbhfP2UB-aP4mx-EnpiEJZBpXy1pv9n_Ey6XxsfNpd2SXw1M0p4fR2T7oYOUU57gAsqQ3ywrzAr-69s_e_BHFk21f2VE0_vXaQjn1SRHgEGj4H7YdM7sggI-4f9aD7iRZ-bk-HIBtnfe4Vy3AJTkC0tNc3mT9TMltQN5poyK0xhoRLoMI2CLFRgy2EVLCdMx30Lq1dqNlw4cF0aflIgq_tYyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چمران: در صورت ادامه وضعیت هزینه‌های ناشی از جنگ، ناچار خواهیم بود پروژه‌هایی نظیر جدول‌سازی، رنگ‌آمیزی و حتی آسفالت‌ریزی‌های غیرضروری را از بودجه حذف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137615" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: در ۲۴ ساعت گذشته نیز ۶ کشتی پس از دریافت اخطار قاطع سپاه، مجبور به لنگر انداختن و پذیرش دستورالعمل‌های ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137614" target="_blank">📅 10:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4114548394.mp4?token=vQ3UXVnd2UFpf-DK9kHb20MGRONInIFZTVif9_DqLZ2kDluhlb2jhrfPr4O_CCGMue__B9hcXwlslPHuFYwxur3Ef_xBIAkCbyY3yRoI3SUHNcIWXj64loLul1U715z3DyhhKKqj8d4GxELjoxeRyPpXfWjfT-liKPggszYSKp8W42lRz8APiycliLPxPTTOd7w00FYxsfal15CjrllrKO_wgcNG_BLrtjbyEi8xPsK-t3Mm5E1n-dIczW2hcx_cXcx7OY5nZ4q2shAt-za6tIjt_6o-9ADAzckKhiJ2s9J4YEXy7sDBa-5pQi-TQSIoC7LeWuqGiUzwXSBo80yOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4114548394.mp4?token=vQ3UXVnd2UFpf-DK9kHb20MGRONInIFZTVif9_DqLZ2kDluhlb2jhrfPr4O_CCGMue__B9hcXwlslPHuFYwxur3Ef_xBIAkCbyY3yRoI3SUHNcIWXj64loLul1U715z3DyhhKKqj8d4GxELjoxeRyPpXfWjfT-liKPggszYSKp8W42lRz8APiycliLPxPTTOd7w00FYxsfal15CjrllrKO_wgcNG_BLrtjbyEi8xPsK-t3Mm5E1n-dIczW2hcx_cXcx7OY5nZ4q2shAt-za6tIjt_6o-9ADAzckKhiJ2s9J4YEXy7sDBa-5pQi-TQSIoC7LeWuqGiUzwXSBo80yOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
"من به مردم آمریکا یادآوری می‌کنم که چه کسی باعث بحران توان مالی در این کشور شد.
🔴
این بایدن و دموکرات‌ها بودند. رئیس جمهور ترامپ از همان روز اول برای رفع این مشکل اقدام فوری انجام داد. همه این مسائل تنها در صورتی بهتر خواهد شد که دو سال دیگر با کنگره‌ای جمهوری‌خواه فرصت داشته باشیم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137613" target="_blank">📅 10:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
هم اکنون حداقل ۱۳ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M در حال ورود و خروج به خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137612" target="_blank">📅 10:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
امروز؛ احتمال شنیده شدن صدای انفجار‌های کنترل شده در شهر بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137611" target="_blank">📅 10:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwOuwDvOaKDMDGQGV72RVnkXsK0ykhLmZSuWRWZ-YffCBy_ezZZfNMGKUl3gt9KtxSOI4JL8rG22KkaRi4yE_bfttYVCFy4k3EHG8A1JWBWRxczrmf3fW6Yin9jfRC-e_Z7MLkzSpXD42QYLbXZEHgDmEdVVrnPbZ4oTvmHlig03jLKi-jsTIQ0bwNttkHm7gXZK-5gktzXfsIm8ajzafrgx2ZW6JW6e6rLmplQdxtX8VSZHFeo6TydTOLmLeWGbXuoxxFvkiT__zF-13R7FSuvqCvjYv58Dnl9IO2ou-VkA-BhRBOg344FwoyzxBImVb1Lq6LVNkmaHsmXZKNrogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حال حاضر، ۷ تانکر سوخت‌رسان آمریکایی در آسمان خلیج فارس در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137610" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
انهدام مهمات عمل‌نکرده در پاکدشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137609" target="_blank">📅 09:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان پخش اسرائیل از منابع خود خبر داد: در پی تنش با ایران، محل برگزاری نشست کابینه به مکانی امن در زیر زمین منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137608" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
شبکه اسرائیلی کان :  نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه با ترامپ درباره موضوع ایران گفتگو خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137607" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhnjhEGadDfSmFRUlGWf9gkpsYmxjQDx-l4KrVcKHMZAGnt8PWy_6awR9W654zU18kPmDwOiDRS8idjxW0L3gyhxdQ8wlgKaHNxNykbFDnmUblOpaYgkLNIxOhpEqlb2Qmox2mLqZ2zL7lxxfWIm5VugS08estdAIXb4DW-UUNZYR0nXvG-u6caoh_rkAjBj74J8ICI1omcbYpCO9iDgWoWhyFfBIDj9Kgo2y5ZyfL6QJQqh_e2X4ZLbMSJ2cVtRRBwbTcmWyAiHrK4FLWwocKOjUyoK8UkbSv9sQ6Y6AfCmPOzt72vCVwe0KxIqxBiAujG77s5naYFvI5yqr_VmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌بی‌اس : مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت داشته، اما به زمان بیشتری نیاز دارد.
🔴
دو منبع منطقه‌ای به سی‌بی‌اس گفتند توقف عملیات نظامی آمریکا با هدف جلوگیری از اختلال در تلاش‌های دیپلماتیک جاری صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137606" target="_blank">📅 09:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6gG1Igt13WWlgztPqUOWdMbg2dR7ybH9S-sVF2W_-k-We1mBK2l9XOSZZq34qhyDN1gusiZ9kjgjdkAfZao1bVUbj9rk0cRpRvf4udfEONJOz5wWxHwlRaL6-ovab-ic-dWsWd9eGgqee85dE-atSgJbto09tYTvMVDHZleYyw1bL7F2qmTYSD8duYMd0_zZ1ceqLLOpWicwcj5L-ziFktoCxnm5bZqQuV4Cw6yzv8DOjAliHk3r4vRvI3xoOIqsLgMa16AecfjLzQoAH-JOf6UMF6X2znKuF5AK5eXi3duSVEjgGc-I_5RVFUNlSOPQHe73NFFN90laNE1UKviUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی: تغییری در وضعیت تردد تنگه هرمز ایجاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137605" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فرمانداری امیدیه: احتمال شنیده شدن صدای انفجار بر اثر انهدام مهمات عمل نکرده، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137604" target="_blank">📅 09:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی شرکت آب و فاضلاب کشور : در حال حاضر ۶۳ درصد مخازن سدهای کشور پر است.
🔴
خط قرمز وزارت نیرو جیره‌بندی آب است و به هیچ عنوان نوبت‌بندی برنامه‌ریزی‌شده آب در دستور کار قرار ندارد.
🔴
مشترکانی که مصرف آن‌ها از الگوی تعیین‌شده فراتر باشد، هزینه آب بیشتری پرداخت خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137603" target="_blank">📅 08:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGE-_9p9Ez_XwBj_NmEz0poik9Mh51bz4-DYQfYSwqzdHOVQ8jFxkDWBoHYKMit56fkQUhZsN6hXyENKjluuMBv6WLu5SjqGa4VZIBQJl5ceNDzvsqJ2evWiN2DiWcMKM3tGLpnbMS2LrX9bJvw6TYuyjSeVZdLGXN9oS3ht76l-PpObY8vZ9TjYSowKZEke402TQGgXNLpUzs1mxT8VyUsdKIQUk1BO1yWxbMM3dEUGqgJDY_PyHJaa9cHCXvZAocVVCm7F1AAjupjN12fanZYf-8_8E-emzZDjinbUHrBlRJAKcsiWivYEiZIuPMf8gMCdJGaYUl21TPRYulfL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ترامپ قصد ندارد تنش‌ با ایران را گسترش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137602" target="_blank">📅 08:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو فردا ظهر قبل از سفر به واشنگتن، جلسه کابینه امنیتی برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137601" target="_blank">📅 08:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حالی علنا از حمله علیه ایران حرف میزند که مخفیانه از مذاکره کنندگان می خواهد به مذاکرات ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137600" target="_blank">📅 08:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-z1ntoeP45mrvlz_7NzQy-iQEtfklBnR4tNEgqgOe3zXc3KWWMdFA__7i5GqKZ2Bx6y7On-x4uA7mQxJmHyyd74IDerPbeno2WpeXDJNSc7WKheTFPrTGuq_iHZGBvXquVxM1y-ZVW1N568NRurFvFs_3TxWi7LI8z14oWUdVnDiyOaMFapPoDFRFDMQMB94mOq25AvkADvIUGFVwVlBwfl-qX29hMu5gbCqfeE4dVRg-BaLljs5y_S3viDhG1s55NB0lQuC4jA6T3ildiIxJaOsKJwY6wj0qYRGFHkBTks-_3CWbuiBSbROobmQKydu-AY0LxtcvjnKUFgXSThnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سی‌ان‌ان: «جی. دی. ونس» معاون ترامپ و رئیس ستاد مشترک ارتش، در نشست روز جمعه کاخ سفید، درباره ذخایر مهمات آمریکا ابراز نگرانی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/137599" target="_blank">📅 08:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb72TwlarWlVf4DknPP4zWYU8Utwm3KRMBKoD03a2U9CK9LqMYyRi4GuLoR_7DcFebSwtUK4c0gjpRTX1LZC6lc-KcCuVKSF64XaNWGbOnpS0ZwYZ9jbs1J1-F2y9YpteyypManWMHZDslqdOdmpAIjqAAL8sFejI_BYG-mlR8N0hFqlKWQy9Z4hHvPFz12JuucYvkJU9oXwLHlT1eGxdRzISsfjVFYvUj88wpvg1118RdPoWMhjToucf3QelEGoL7JScvPgDK6svoMzHOQkz-gf_nWa6Ib0Ec305xmkEMJFmmXA5-qfcsJMvV3thR53PjGcbTNpBKnFKxpGfFvuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: توقف موقت حملات به معنای عقب‌نشینی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/137598" target="_blank">📅 08:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmcoRviqEcuSZco-ud-q1alVuQSh82Shv2bdBkqmFEgn2TDo49VevjTF1BWQnI1fQoXiHRpYtTi0k-g5WW43no3RemMOomZnCazyucfCTh4k02wudsDQzTWbq-rwlv-OpNXFlVsGL1iEbNOcKSa61v3U0lNQeDwPwoyccmA_9eNqGaqmMXrwze5Db-bX6z6wEwEC21_sRjHK0RLiko4RjDSEv7ExDJFBBnIFsMZC40ADhRswxatwbQ6McFQXyRMrmJNoeM9yQydEjapEreZ-aZjD9QyyhTRdBD2xTs3JxtfiaSWrYZFCPe_y86eyPg77kqthze-5_Is9dNcF-EHkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا، ژنرال دن کین، در جلسات خصوصی به دولت ترامپ هشدار داده است که:
از سر گرفتن عملیات نظامی گسترده علیه ایران از نظر نظامی امکان‌پذیر است، اما این کار باعث می‌شود بخش بزرگی از موشک‌های رهگیر دفاع هوایی نیروهای آمریکایی در منطقه مصرف شود و توان دفاعی فرماندهی مرکزی آمریکا به‌شدت کاهش پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/137597" target="_blank">📅 02:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقام‌های دولت ترامپ:
ترامپ، دست‌کم در حال حاضر، از برنامه‌های خود برای تشدید گسترده حملات نظامی آمریکا علیه ایران عقب‌نشینی کرده است. یکی از نگرانی‌های اصلی این است که گسترش جنگ می‌تواند ذخایر رو به کاهش پنتاگون از موشک‌های رهگیر پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را بیش از پیش مصرف کند.
تهدید علیه ذخایر موشک‌های رهگیر، یکی از عوامل مهمی است که بازگشت به عملیات نظامی گسترده را به اقدامی پرخطر تبدیل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/137596" target="_blank">📅 02:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا فیلمی از شلیک یک موشک هوا به زمین هلفایر به موتورخانه نفتکش لاوین در خلیج عمان منتشر کرد و مدعی شد که این نفتکش تحریم‌های ایران را نقض کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/137595" target="_blank">📅 01:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozenIUcvFftmkPFPw7y6KvVsR5bB4W7N5RymTd-Tmg_vRHpX8O3gZukrSGBV3NCMahss_gKnqB1D5776cP9TKLS0lJg62oApd90CzfuwgvLsw4SWTsdaxdBrQairOuV3vuIT04IxMwFA7XZ_TAkSCVBT8Km2r5myEwB67ETF25rBndzvkm6Se3Wm1rOLpGyPYBfXq0C_feeJVOj-pEtGVUNtvJDVIuGIqR2aqflpHTIxbCDNroamCHVNHVOJN3_KiQLgjPFTFWYQzkT9OCbeDBXrUkJCrz6StLjSop1OO3rXxqAJj8pRcrHidSi8vq-Rdf3m_asy_kR50HN-LdbIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137594" target="_blank">📅 01:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سنتکام:
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/137593" target="_blank">📅 01:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحلیلگران در تجمعات شبانه در حال قانع کردن امت معکوس برای توافق هستن
🔴
یک تحلیلگر پایداری: با این محاصره اگه توافق نکنیم اوضاع بحرانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137592" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/137591" target="_blank">📅 00:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-y91r-HMTpW8gJcKe8PnsjofNhv3trMCp3TzqR5uFWsXQMrH3yab84ug-RXGoHOfPcRXWjMGpKWMneUIjwKCoNaNtdF5Ehk3tpXyOjVedmcm1t6O-yt368YI_Aphn5grxPuGxjEUB6hs_y6uChji6omOJ7ttlzW9zkR708CcWGjlBn1BxsvXbgpoxJFVME-MOR2TG2IdpaKoSrM1aP8uuWSZXhL1mlP8DioPCfY1XKSBsVbibEBIQdIW7uyfUPzi6ZU9rBrEX6147OZsA_QetPUgUWO2HbYotfXhihxyVQ_E42bPUBeQEX0bbD_18nirniuifDMAPSpZxdVPmFp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمع امت معکوس که تایید کردند تنگه ننشونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/137590" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره اپستین!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/137589" target="_blank">📅 00:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2m_vo8KGJkOPyHwSOWL4j7uzYwoxX9mmfxxtnlHHisBq8SmgpEEiDoC_CUpFfYvYACqTMqWt2ATK5LG1piWtNvTgop8NqE1a5WREs7fN54CNFwHHDEMj0HvFrGv-IeElguvegmVhiMJUfIPswpOapbbObxzJFTAb7DF1pfqLJOmLGn_nNrsx-MJwpQBANKyLT7CmAy2R01AJ72MJgsEc-dcspHsGC-ZVyEmTe390hwOxkjuZfAQ3xYyoKpxuJ1EVxm2s4b2jYwTXFWYx7GboxwSo9N2Yq6WrcvwIky_EXsl1kSYUMrjkgK_i96-zrvDSGfQNlGjTdC2J0OVP4s61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/137588" target="_blank">📅 00:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxXZnAbsUBoeOuY2-G6N0fEYL_SrY9Zbvt5UM8B4nEOKM4zvhPfuRr4uNNKEGJq7NVBYizt7W3UTih2sbV_kq2_5GOobWxIPVIBpcvQrswfjB37FapXGhfnEbyP5JT3iH5mtJGpL7ROdShcqoDa1yLux_gTCKbdo5QqS98YKJnwXgbsQDQsy8Rf3UFgKWn107c8l0XCFNesPhw2LjQ6zAht7SQ8ZyTgp6pEFbe_L7YxqhCuiMaQ0Se_aDUZSVHOSB1LapMcAJPlLZ6_bQBpXJ99mYldrBXorH6SEUfXJbGwI5Lde9LgEYLb4L2xeepKeS9Yh0rMcTO_6qkoMQ6Oqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.  [@AloTweet]</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/137587" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/137586" target="_blank">📅 00:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZMljDUMg5DRwCf-gW55bi2VSwZ8rc0sBP7NXw-9gAcSZ36l2OliTSt7HJ7K-mstg7uvw-FihwQ4Jp79nT6h-1yLrSRjpVtChc-iVcpO23WyN_c5BxasmW9cK8uQD27Vog591ja0mylsqKPY_6CGoQJD42k0p-UR4cya-wUMbLSJsPokFH2dAbUD-xjAkXQpjjy1u8Wjgxbkq_tRtCaski0pQA83KJ_W7Cz5cEEvTlU_f9o10q0Y9uUdimzCTPR1UsXqO_lK24HdGxdX1vjon3GRWvz4cUFmACJL8wlUWCzH3BFem_MIOPvQ-D4qwCLB3_f6tsVT6ka05OMakM0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری ایمان صفا :
من همونقدری که برای بچه های 18 و 19 دی عزادارم برای بچه های میناب ناو دنا سرباز های کشور و جنوب هم عزادارم
اینا همه بچه های ایرانن
یه سری تلاش دارن اینها رو جدا کنن و به نفع تفکرات ایدئولوژیک خودشون مصادره کنن
یه سری توله رجوی و چپول هم نطفشون بازشده هرروز یه چیزی میگن
من رو صورتم رو هم اصلاح نمیکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/137585" target="_blank">📅 00:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عراقچی خطاب به مسئول سیاست خارجی اتحادیهٔ اروپا: شورای امنیت و اتحادیهٔ اروپا باید رژیم اوکراین را بابت حملهٔ جنایتکارانه به کشتی تجاری ایرانی پاسخگو کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/137584" target="_blank">📅 00:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=py2F7bAueEhe2J9iGTps2bJdXx9mljvqJCHg3lLca3ii0kxKxyYK1XgvIc5Q3vRH5V5TtVgL9cq2tjqMu3bmZo5gpOjT5-9T39VbzfiPYTHFCn4I3n92S4SHNuygJ57UTqmps5pK9mMBD7_p2iPWTXbSPIjeMTz4NvFSd8TAx8mHnarDoQDNCKi0QWo-G8gf-P5UqVgDjYrFl0m4Ul7UQifJiukPnNTMsHkjiVDjqIs7tCZ7cEPEAobBV-IWlGxsbCMfCeGrNeDvOCmYBS0EfhPFIPuXXzCfjU2UMIK18DHgV7qjzzfDO7SoBZokLea1Wgvwyh0uwL_-cg9T_YO5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=py2F7bAueEhe2J9iGTps2bJdXx9mljvqJCHg3lLca3ii0kxKxyYK1XgvIc5Q3vRH5V5TtVgL9cq2tjqMu3bmZo5gpOjT5-9T39VbzfiPYTHFCn4I3n92S4SHNuygJ57UTqmps5pK9mMBD7_p2iPWTXbSPIjeMTz4NvFSd8TAx8mHnarDoQDNCKi0QWo-G8gf-P5UqVgDjYrFl0m4Ul7UQifJiukPnNTMsHkjiVDjqIs7tCZ7cEPEAobBV-IWlGxsbCMfCeGrNeDvOCmYBS0EfhPFIPuXXzCfjU2UMIK18DHgV7qjzzfDO7SoBZokLea1Wgvwyh0uwL_-cg9T_YO5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شریفی نیا: اکبر عبدی پرفسور سمیعی سینمای ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/137583" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
العربیه: دولت ترامپ در صورت به بن بست رسیدن مسیر دیپلماتیک در خصوص پرونده هسته ای ایران، گزینه اجرای یک عملیات ویژه و گسترده نظامی برای ورود به تاسیسات به شدت محافظت شده هسته ای و خارج کردن ذخایر اورانیوم غنی شده این کشور را روی میز بررسی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/137582" target="_blank">📅 23:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoPAxyp-Dj5NBczODqa2YDvnH8UckRIy--5OBToFT6Gu_snBynSHEFmW-g6E_KDvTL1EpdlIKqJ-dfpE2Z5D2C8E6VHce0llmlq4uKLTqT1scJxlxVDlci73vYNju4-c7q-R7rl-Af8zw_l0_wwqMJRE1wiS7zjFVK__C37sK7Oolr2IU8PK-uoN5vii8LESk7lycB0FdTEr-4giyL4zIfL3ZD_9QjlDI2c0xLs2e_LY3il5OqvsRktD6mpFXH3snaT6Cctoy0ge_kIw3uOmOXyuCIS4XL7j4gUDpaAzohzX_lhJ9daKCDp_uP8n2cOJEzzjY6Ryya5Yi37S6la1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس تو قرقیزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/137581" target="_blank">📅 23:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YoYkXUJibGV13XkLr6DYu7VuMJVYGYWcPOYGk4Gq-6xNxViDavREq-3kQWcdiqprZcvMdyOHzxjlpILPiU26hEVAYiQ0BE8wEKqybUGyZkn6ijWXOKiDbgT00CE5EpXRPyZ6F4fTgc7jqEwAnmQhV0EWVF_ochHqOxAmt30RRmHy-HIX09MIK8nAHB5lBFDmCbkTsiCXZyMKJ_dodJxfBByTH_WgBotdMVM9gqHWR5zXhDs8Y8g2FEHkyqc4xx8bh3MGxGbFZXp8uSPxYRKqEEO7SmyCuDZKqADqdJCgT5ZlcP3NBnd5ioIBYkS_wK-oFDjcFrUPg8JOPv-ENcH0cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YoYkXUJibGV13XkLr6DYu7VuMJVYGYWcPOYGk4Gq-6xNxViDavREq-3kQWcdiqprZcvMdyOHzxjlpILPiU26hEVAYiQ0BE8wEKqybUGyZkn6ijWXOKiDbgT00CE5EpXRPyZ6F4fTgc7jqEwAnmQhV0EWVF_ochHqOxAmt30RRmHy-HIX09MIK8nAHB5lBFDmCbkTsiCXZyMKJ_dodJxfBByTH_WgBotdMVM9gqHWR5zXhDs8Y8g2FEHkyqc4xx8bh3MGxGbFZXp8uSPxYRKqEEO7SmyCuDZKqADqdJCgT5ZlcP3NBnd5ioIBYkS_wK-oFDjcFrUPg8JOPv-ENcH0cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش : پدافند کشور بازسازی شده و بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/137580" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo4KA-XV-wkzLuHH-w3Ei1SCvsCQvsbQxNvPKd6HhhPtXk_ucHRJ5srEEfc265Ftmn926FDawKR_boqhAaF8KunJbY14KHUOcsK1D1RLUBoTUC3icbm6hL0MrptDf1o4vueWp7UdgO365grThYgB4t45m72YosgqtUQkoe7DooKgQ6UcB46FAWfwynII2MohjKu4t0FFO2vZJnqzT5a6LehIq2KFnqzaLDy3kn4gvZ65BA-iXk-qZuuqGdNXVxG01MK3S-ZAsgN6dhQWE79Pr-C-jDRlPLjXLq7Fi8BsbsS0zfSXusB-4czCoJRJZNw36uy6mm9eoIBaR33XjfqMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اخبار جنگ ایران و آمریکا
در سریعترین زمان باخبر شو
🆕
کلیلک کن
⬇️
⬇️
@Breakingpersian
@Breakingpersian</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/137579" target="_blank">📅 23:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/137578" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137577">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هیئت عمانی تهران را ترک کرده اما امیدها برای یک راه‌حل مسالمت‌آمیز و دیپلماتیک را افزایش داده و گزینه نظامی کمرنگ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/137577" target="_blank">📅 23:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRSn8I_tDH5maLaK8NQb2xI3Ca3gPIARPPlVfM9lBzMYvGlv5Ka5LM8vyZu8LqZhzz0EktjIQSkvNFcT7wGoc0VnjPnwCrPPPgoMq_Xb9xhuFpigYZmhwF33TCXeKBsvn-nssR78_Hb--9bshFNfzdOxaj4MFDDPoFAgs65Oxgeuuc4zmbpmW4hBGS6RCQUXJHt54TVAAQKhUl6us8xCZ_c6qjaNeRoYbnoeD0RxZQeMQ7PQQ4fn3FNQ6c2piLoVzIWZ3Kkzc3aHYPkUxfZjVQFhsL24q4NwUzQQErCvryX-06blprz92CpxNtBKCwRNBjLxZlHcGfVeukUc3UJvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:  حملات ایران به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/137576" target="_blank">📅 23:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینجوری که قیمت تتر هم داره نشون میده، تا یه حدی دوباره به یه تفاهم نصفه و نیمه رسیدن!  ولی صداشون در نمیاد…
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/137575" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رسانه های عبری: کابینه امنیت ملی اسرائیل، فردا تشکیل جلسه میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/137574" target="_blank">📅 23:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / شبکه ۱۲ اسرائیل: نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/137573" target="_blank">📅 23:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcOICBTdYp0LC7coRr9Q8N0FZzn5GUoUNXkYhYRlyewjBgWU5Uu0LZ9437mOdnQ_lDBBfLEMkBMbFXsUV5H0_AV7NmSAExVBrarGABi-ZLA-Pa2Bj6gjdmT-3IXDixCHc0m3FBodlWjuRHi1kmwQ10cabJFWtApLxBoq8idErP3DYHsvt9UtoKnkLvpeGQVmNNyss5LrTvZfCbOsagIrO7VFJk7LXJL4RJsh1CwiEgA3smnuS16WZ-8q8PJ_rriI0Z3kqDjDix8D2vlo3Ya6dVNnqlPz1FjKgn6LRAvdi90K7fGluHzBzK9rKDFZToIqr0L2hHLT2Au2VlPMGRVOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
🔴
رئیس جمهور اوکراین: از ابتدای ماه جولای، ما نظارت ماهواره‌ای فعال روسیه بر کشورهای حوزهٔ خلیج فارس و تأسیسات نظامی آمریکا مستقر در آنجا را ثبت کرده‌ایم. این تصاویر متعاقباً در ایران ظاهر می‌شوند. همزمان، همبستگی آشکاری بین تصاویر ماهواره‌ای روسیه از این مکان‌ها و حملات ایران وجود دارد – هم پیش از حملات، در مرحلهٔ آماده‌سازی، و هم پس از آن، برای ارزیابی خسارت واردشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/137572" target="_blank">📅 23:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iALSUxRnHtVFjIsUx6bi8zM0JU5nJjvHqtX9VLpJ_SQ4V7uLCCsy5UKXU5Ca3Um9eerj0T8bBPNyKTUI7hqS3B_YFgGkKwSXjohMikavsHAnbGbvIPQg-90FanKaqVDx7rR6P_R4Ylb4rsunCNc0cCBYRzK6KUUmzxEBWhA29kP0pgFLmaRorKAw-g45uoy1Cw3lPaqkuXqQXtL0La_tzUp9j4HaHut2c9BbMsuPgqkEe9T1xBE-xcNW2g9yCfzf1CLoJZT1NcToPF3t_THTkZ8ChdLPV1_JxEo_-Q5xC6mZw6lZYImriMfJf6pbiJFJWOx2wZvcPtU9Q1I6Y3E1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
یک پهپاد در نزدیکی خانه بن گویر در هبرون سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/137571" target="_blank">📅 23:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی ارتش: بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/137570" target="_blank">📅 23:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ادامه آزار و اذیت ماهیگیران ایرانی توسط نیروهای دریایی کویت به مدت چند روز متوالی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/137569" target="_blank">📅 23:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پیت هگست، وزیر دفاع ایالات متحده، به MTV گفت: ایالات متحده در روزهای آینده حمایت خود را از ارتش لبنان افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/137568" target="_blank">📅 23:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3_G8kvvZjSWcuD4--wnULZJdxcoAY9D-gcricB2IFbPaiYsuV3-DtCX6guenRsSk9z1aCKYqelMGbZ9k7UrOKMBXKQ5xX1ckIUf_Qu9pAPTHqdFMRta-DAtQK3XiqCQFWc4jTUW1zlJ6IG0SVwz5VcvmN2OLAX0Ix8_zxvRsNB8zldtSRxfRZhFKdP87dlg1Nm8MFYDtQHokE3VuRFHnA6kQdTDMjTXPatfll_xaA1dDTjeildVGnei8cgmLgJCuBS2IMMJ3S-u0APWOMPrsC2OK5fhX6OdybkPsImMod2VKz0UYwD2vcmjWRZi-wjKQqOpnhchHqTM2nPcNgfSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/137567" target="_blank">📅 23:03 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
