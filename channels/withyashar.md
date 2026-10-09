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
<img src="https://cdn4.telesco.pe/file/OLMWOmT61ifEBAgg6XRovOS1ior4sJhXzS7JPOyS5lOuUEthIkorQRlnIXcLF3cQMyPc_HOqi3HsFqQjvtIO8d1uxmPnTuXRwRFFXZ0W2zIKAHammhNoiljNpa1FC2cjqnEuNAwZ5I9xPHOoIAzOtHE0pkEA1qrGes5xRzEDIRnksrRBwLSLqBb3hK01I6Xgqocr-QBFaflIqSu8GFk5LpwN5Jr_mxQOw76enTEN-2noy8L92MtLBIP9diigMBdjifliKWRaqobunCikON0MMuiTKK1har911EvBNeqdVclWd7NjA_qQWr3cNzuO6X3-k7HLcMOIaF4EBp_ms9tzpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 489K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/25272" target="_blank">📅 18:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/25271" target="_blank">📅 18:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل: یائیر گولان اکنون با حذف خامنه‌ای و عملیات «غرش شیر» مخالف است؛ نفتالی بنت با عملیات «ملت شیر» مخالفت کرد؛ یائیر لاپید بخشی از قلمرو حاکمیتی اسرائیل را به حزب‌الله واگذار کرد؛ آویگدور لیبرمن می‌خواهد بزرگراه ۶ را به کنترل یک ارتش عربی بسپارد؛ گادی آیزنکوت می‌خواهد از لبنان فرار کند و منصور عباس پشت پرده پنهان شده است. اگر این‌ها گزینه جایگزین باشند، چه جای تعجب دارد که همه دشمنان ما برای سرنگونی نتانیاهو و دولت راست‌گرای او تلاش می‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/25270" target="_blank">📅 18:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIz0gbdjJHT_4pNq_ufPIsvsl1P_Qk9lr9XlwyqY2YyoOJ0gh51DmhouzfTBAC1qp1kgpkUJi5hamQXl1LF1B4ZXeeSjOBziUrpxsvnnCJCngNaZo4TchB79ZPlUHR8aaRGv7jPp7XQWvZNC_VUSIvxr3V531c0Jj_JfFKRfN00Kcd2d_2M1YFDKmOGoin9C8axACZUWL-U2_0VB3eU3Xx3GxOBjhIwrUAJcep5cMX1uSKw9fxgQ4MWBsz3po-Y3LhuF07gGcGSVrqUmBKtmEaKjpo5bYAJIXk6pfkXUeSCIY32bcKP3_v_TcbKm5v5xpQ5Xo4LRxZX6YNYmaCNw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=qNu-y8hHMmVWdNLlOvCN62tYFngehhFExBkNNTltIVafy-J0QPZPa2JKHa53XX2LIxJZa6xpPVP02YSwRvRGrcwGvELzv5onVWveWx2sykS6Ye-8Uijj4zmp91gvcuBireOTtSEvrMa72WyFhRiJ2lFcc06dMvEgZyqSSHDhStqP5OFvM8p6BW4FePte__oWshgUDfnKXy8LX_CrJj5sgfsDCp_r_kpy1PoyjkbfUW-tDnr9DgeSjknjLOCXIAvi0GNI0Za8axXjgpYVkvz0TxRwJqp4QpZOWWjpZ3_pr6wNlK3bcKmYjWYz_6QdWcQoNDQWUVIiehhrkM1pFJ_otQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=qNu-y8hHMmVWdNLlOvCN62tYFngehhFExBkNNTltIVafy-J0QPZPa2JKHa53XX2LIxJZa6xpPVP02YSwRvRGrcwGvELzv5onVWveWx2sykS6Ye-8Uijj4zmp91gvcuBireOTtSEvrMa72WyFhRiJ2lFcc06dMvEgZyqSSHDhStqP5OFvM8p6BW4FePte__oWshgUDfnKXy8LX_CrJj5sgfsDCp_r_kpy1PoyjkbfUW-tDnr9DgeSjknjLOCXIAvi0GNI0Za8axXjgpYVkvz0TxRwJqp4QpZOWWjpZ3_pr6wNlK3bcKmYjWYz_6QdWcQoNDQWUVIiehhrkM1pFJ_otQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند. @WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/25267" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/25266" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز: دونالد ترامپ که بارها گفته بود شایسته دریافت این جایزه است، امسال نیز برنده آن نشد. جایزه صلح نوبل ۲۰۲۶ به ناوانتم «ناوی» پیلای، حقوقدان اهل آفریقای جنوبی و کمیسر عالی پیشین حقوق بشر سازمان ملل، رسید. کمیته نوبل از تلاش‌های او برای تقویت حقوق بین‌الملل…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/25265" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیوزمکس : وزیر خزانه‌داری آمریکا گفته  است دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/25264" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/25263" target="_blank">📅 17:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/von-RjIKdxxAX5t3NbjcwS-m-z5NKkHW5HDFqrSV1Uys3yHdZkSRaukP9rrzWbEcZPYqEda_dL22aHK44l1CplHMjPNDmiu4IXSSxMDwggA7UhQGdbo6Ri9tYPEWOhFtZlzFarxdmJBfMgbW3Z41UwQ-09aUiC2pkhQB5Rv5NiON8OCbq1fhLpX0JPCV5QOpP1tlqIjawo1-k67rs3r4tuupw-6FvTp7YQpJusqflzzAA26hTpNJI3ZqGLIH_tBOpVW3IKXfBxZv9fvNzeQJFEpjbEQ2J_DDdUtu4_D3soW2FV8QE2Ktg8qsJsUdnh_8Q9Z4UoSBGwK2yG7qP0pC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:مربی تناسب اندام ناو هواپیمابر یو اس اس جورج واشنگتن (CVN 73) که در کشتی با نام «رئیسِ خوش‌‌اندام» شناخته می‌شود، اعضای خدمه را در طول تمرین در آشیانه هدایت می‌کند. این ناو هواپیمابر به عنوان یک شهر شناور، دارای امکانات تناسب اندام متعددی است که به صورت شبانه‌روزی در دسترس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/25262" target="_blank">📅 16:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بسنت: سپاهی‌ها دیگر نمی‌توانند برای دیدن جراح پلاستیک‌ و دوست‌دخترشان به خارج بروند
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اجرای کارزار «انزوای مطلق» علیه جمهوری اسلامی خبر داد و اعلام کرد دولت پرزیدنت ترامپ با استفاده از محاصره دریایی، محدودیت پروازهای بین‌المللی، مسدود کردن مسیرهای زمینی، و توقیف دارایی‌های دیجیتال، در تلاش است ارتباط اقتصادی و مالی حکومت ایران با جهان خارج را قطع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/25261" target="_blank">📅 16:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سپاه پاسداران اعلام کرد کشتی غول‌پیکر حامل گاز مایع (LPG) با نام اِن‌وی سان‌شاین (NV Sunshine) متعلق به شرکت نات‌ویت، هنگام عبور از مسیر غیرمجاز در جنوب تنگه هرمز هدف قرار گرفته و در بخش موتورخانه و سامانه رانش دچار آتش‌سوزی شده است و هشدار داد اقدامات علیه کشتی‌هایی که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد ماند و این شناورها در سراسر منطقه تحت تعقیب قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/25260" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در سرقتی بزرگ از کارخانه شراب‌سازی
مارکزی آنتینوری (Marchesi Antinori)
در منطقه توسکانی ایتالیا، حدود
۳۰ هزار بطری شراب به ارزش ۵ میلیون یورو
به سرقت رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/25259" target="_blank">📅 15:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/25257" target="_blank">📅 15:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آکسیوس: احتمال ازسرگیری جنگ با ایران طی ۳ هفته آینده
به گفته باراک راوید، مقام‌های آمریکایی به رئیس ارتش اسرائیل از آمادگی برای احتمال آغاز مجدد عملیات گسترده علیه ایران خبر داده‌اند. زامیر هشدار داده این اقدام ممکن است به تعویق انتخابات اسرائیل منجر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/25256" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سفارت مجازی آمریکا در تهران
از شهروندان آمریکایی حاضر در خاورمیانه خواست به‌دلیل شرایط پیچیده امنیتی،
حداکثر احتیاط را رعایت کنند
.
این نهاد هشدار داد که احتمال
لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرها
وجود دارد.
همچنین با صدور
هشدار سطح ۴ (بالاترین سطح هشدار)
، تأکید کرد: «به هیچ دلیلی به ایران سفر نکنید» و از شهروندان آمریکایی حاضر در ایران خواست
فوراً این کشور را ترک کنند
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/25255" target="_blank">📅 15:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25254">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اخرین ویدیو ترامپ شب حمله</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/25254" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اورشلیم پست : منابع اسرائیلی دستوراتی دریافت کرده اند مبنی بر اینکه ، اسرائیل در صورت شناسایی آمادگی ایران برای شلیک موشک به آنها ، حمله پیشگیرانه را انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/25253" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">العربیه به نقل از یک مقام آمریکایی: حمله گسترده به ایران در آخرین لحظه به تعویق افتاد
یک مقام نظامی آمریکایی به العربیه گفت ارتش آمریکا روز یکشنبه ۴ اکتبر، در آستانه اجرای حمله‌ای گسترده و مشترک با اسرائیل علیه ایران قرار داشت و نیروهای آمریکایی تا نیمه‌شب به وقت آمریکا در حالت آماده‌باش باقی ماندند و انتظار برای دریافت دستور نهایی حمله تا ساعات اولیه دوشنبه ادامه یافت؛ اما در نهایت دونالد ترامپ دستور حمله را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/25252" target="_blank">📅 15:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الجزیره : حسین موسویان، دیپلمات پیشین ایران، و آلن ایر، دیپلمات پیشین آمریکا، ارزیابی کردند که درگیری در هفته‌های آینده احتمالاً
وخیم‌تر
خواهد شد و توافق صلح نزدیک نیست ، آکسیوس هم در گزارشی گفت
اختلاف اصلی پا برجا است
و نشانه‌ای از کاهش اختلافات از دو طرف دیده نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/25251" target="_blank">📅 14:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شاهزاده رضا پهلوی در شبکه ایکس: «
تا وقتی این ساختار سر کار است، اصلاح ممکن نیست و سقوط ادامه دارد.
سقوط شتابان ریال، نابودی دستمزدها و پس‌انداز مردم و گران‌ترشدن زندگی روزمره، نتیجه مستقیم بی‌ثباتی، فساد، چاپ پول و سیاست‌های نابخردانه جمهوری اسلامی است.
تورم نزدیک به ۹۰ درصد، مالیات پنهانی است که حکومت از مردم می‌گیرد
و به جیب کسانی می‌ریزد که پول چاپ می‌کنند و زودتر خرج می‌کنند. تورم مهار نمی‌شود، اما سیاست‌های شکست‌خورده‌ای مانند دلارپاشی ادامه دارد؛
سیاست‌هایی که فقط ثروت خودی‌ها را افزایش می‌دهند.
»
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/25250" target="_blank">📅 14:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کان‌ نیوز عبری :
ایلان شاگيف، یک مقام سابق ارشد شاباک، ادعا می‌کند که نخست‌وزیر بنیامین نتانیاهو بارها از پیشنهادات سازمان شاباک برای ترور مسئولان ارشد حماس خودداری کرده است.
او گفت: «هر بار که ما آماده بودیم، ایشان پاسخ می‌دادند: آمادگی خود را حفظ کنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/25249" target="_blank">📅 14:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو شهروند ایرانی در بریتانیا به دادگاه احضار شدند , آن‌ها یک بررسی اولیه و مشاهداتی را در مورد سفارت اسرائیل در لندن، یک کنیسه قدیمی در بریتانیا و سایر اهداف اسرائیلی و یهودی انجام داده بودند.
در کیفرخواست ادعا شده است که این دو نفر از این مکان‌ها عکس و فیلم گرفته و راه‌های دسترسی به آن‌ها را بررسی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/25248" target="_blank">📅 14:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس‌جمهور ، زرشکیان : ما همواره بر اهمیت گفتگو تاکید کرده‌ایم، اما گفتگو زمانی ثمربخش است که با استفاده از زور و اجبار نباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/25247" target="_blank">📅 13:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GidlNwqxW27xOD8KyazSgMo3zpsMyPzwpEumZOhivwyDkrQEg5_SjLxOrrr15uDiAZ4esXNZHfUQAQj4v0nUNwh9eUYLI3_1vXnn5DOKx1JMbWBzM6cnMl7_Qd_MbzYpJYiX29TNJWi8rQWHN_p9e45vPqQpbJET2VU_tgUcz-i9R7jsi5qsT-znFjHJ2cKbAv03aTf5PjUMDn7GRqVmjdmwfvxG98XA3IL9U8f1MjUh3cmcoVvoCQHKRz6qvMoeN_kRE3Ot_WkP8zeFAV-mF0bCoKPjEMks1W95B9OaQuq8jrDRmG5xPJXVDxOD39tRvmGXKZm5NHQZ2HGRHBMYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا این بار برای کل خاورمیانه هشدار امنیتی صادر کرد !!!!!
وزارت خارجه آمریکا: شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، به دلیل شرایط پیچیده امنیتی باید
هوشیاری بیشتری داشته باشند.
احتمال لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرها وجود دارد.
ایران و گروه‌های حامی آن ممکن است منافع دیگر آمریکا در خارج از کشور یا مکان‌های مرتبط با ایالات متحده و شهروندان آمریکایی در سراسر جهان، از جمله شرکت‌ها و سایر مؤسسات آمریکایی، را نیز هدف قرار دهند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25246" target="_blank">📅 13:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز: دونالد ترامپ که بارها گفته بود شایسته دریافت این جایزه است، امسال نیز برنده آن نشد. جایزه صلح نوبل ۲۰۲۶ به ناوانتم «ناوی» پیلای، حقوقدان اهل آفریقای جنوبی و کمیسر عالی پیشین حقوق بشر سازمان ملل، رسید. کمیته نوبل از تلاش‌های او برای تقویت حقوق بین‌الملل و پیگیری قضایی جنایات جنگی و نقض حقوق بشر تقدیر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/25245" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اکسیوس از قول سنتکام: ما دستور حمله به ایران را دریافت کرده ایم و در حال آماده سازی طرح هایی برای حملات احتمالی هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/25244" target="_blank">📅 13:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل گزارش داد که ایال زمیر، رئیس ستاد ارتش اسرائیل، دو روز پیش از مقام‌های آمریکایی مطلع شده است که کاخ سفید و پنتاگون در حال صدور دستورالعمل‌های لازم برای آماده‌سازی یک حمله احتمالی گسترده آمریکا به ایران طی هفته‌های آینده هستند. این گزارش از…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25243" target="_blank">📅 12:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25242">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الحدث به نقل از یک منبع نظامی آمریکایی گزارش داد که پیشنهادهایی به دونالد ترامپ ارائه شده تا توانمندی‌های نظامی ایران در نوار ساحلی و تا عمق ۵۰ تا ۸۰ کیلومتری هدف حمله قرار گیرند. به گفته این منبع، چنین حملاتی می‌تواند توان ایران برای
تولید انبوه و شلیک موشک‌ها و پهپادها
را به‌شدت تضعیف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/25242" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ri0bcXaqvQLssiq6_ZBl9fRnOkKzYrTtJCKpMhRFpnrrSUkxREJl3Jhs7df2Ldf5RxQWvabIlmOv5duiLot3ZMS3UaVvpPUHQixBbaFL-Hcf8aaFVOfwh-rT8GOcKurykWvfaBPET_UPIyOvXQW-vliDsn8TjEiYr7zaQCMkuZnsbQkOjCiAUENO9I2PWeapXrDDa2Fr_91tNANzuLhvUYZEsP_N5fvVdFpGKXYpTh2Td3jJc6ZyMuWKKWmzPUjUgUWsgFmy_JbEig__a9ZttKqpQzDfoBV6SW_ITJ_NYtzcOKch_wOLdt_UKqAKlsuadJYRscRrIE8Fio7wh1RkoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkwBDSJXgZmZfysEBM2brFlX2rnizhKtlgKErkNfBMe0T_X9pWxKXHC_SRfpwWYtNR-bcaXnHgxkrnsbh-Jk0x_CC8iuoAwlm1hJSrgym4i2F0YnHVN5a8C3CEyhULpeKrRXNpGZ5JjxCVpoW6OTplCGV4nivHjROF4_hBMlwDO2Px3YBhiJ7sSVi2_0GbQa26opGQ50XMntkQrp1jK7KwhTKIU91PB4gZbdHHTX1z-h6mxyc6BywUsShOjk972GJvNkvohxMYokOe2eseTSZhkuosDABbtF6yzZJ30APorU3LhD5zAIiomiUfAv2GhUMUJVnH3WSLCQpaD-b4UBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJrO6Z1N-OfU0hvDB5b7sTmE1OQTDHU72B9nMT_kkQsH_FOi2wOsIu997MAV43aPZGulEEpMW3U8OvmmBjY8lMyk2yGRkNT68vw-JBmagZrhXLAEIT0K8oyBJDUMS8E44FDlNaHmEt72Rsun3VcgJaBgjDymUzuqncweSbbYv_85vxNe9H25R_dHHTeC7F-tUnGwUXaJJR9DnjM3SNTG2TrYjmHv0G8IFE7wH2HqibVdrR2auNyTJWTjIzfTvPKi6pe6KQVaBaHgC8QDDY_ihKfH10ChGg_ollp08LrCNpyWOPqFcYaBX7PDM9_bMPCOcsupyMvixy3Jc7aXIvw5GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یو‌اس‌اس مکین آیلند (LHD-8): ناو آبی‌خاکی تهاجمی کلاس واسپ نیروی دریایی آمریکا با حدود ۲۵۳ متر طول و ظرفیت حمل حدود ۲۰۰۰ تفنگدار دریایی است. این ناو به سامانه پیشرانش هیبریدی شامل توربین‌های گازی و موتورهای الکتریکی مجهز است، همچنین ۱۰ فروند جنگنده اف-۳۵بی…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25239" target="_blank">📅 11:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال ۱۲ اسرائیل گزارش داد که ایال زمیر، رئیس ستاد ارتش اسرائیل، دو روز پیش از مقام‌های آمریکایی مطلع شده است که کاخ سفید و پنتاگون در حال صدور دستورالعمل‌های لازم برای آماده‌سازی یک حمله احتمالی گسترده آمریکا به ایران طی هفته‌های آینده هستند. این گزارش از افزایش آمادگی نظامی آمریکا برای احتمال ازسرگیری حملات حکایت دارد، اما به‌معنای اتخاذ تصمیم قطعی برای آغاز حمله نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/25238" target="_blank">📅 11:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انیمیشن جدید حکومت از حامله کردن زیردریایی آمریکایی و دادن دستورات جدید با سی دی. وقتی ذهنت فقیره، همچین چیزی میدی بیرون
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25237" target="_blank">📅 10:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تایمز اسرائیل: ایال زمیر، رئیس ستاد ارتش اسرائیل، از یک افسر زن یگان ۸۲۰۰ با نام مستعار «و» تقدیر کرد که پیش از حمله ۷ اکتبر ۲۰۲۳ درباره آمادگی حماس برای حمله گسترده هشدار داده بود، اما هشدارهایش جدی گرفته نشد. @WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25236" target="_blank">📅 10:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25235" target="_blank">📅 10:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تایمز اسرائیل: ایال زمیر، رئیس ستاد ارتش اسرائیل، از یک افسر زن یگان ۸۲۰۰ با نام مستعار «و» تقدیر کرد که پیش از حمله ۷ اکتبر ۲۰۲۳ درباره آمادگی حماس برای حمله گسترده هشدار داده بود، اما هشدارهایش جدی گرفته نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25234" target="_blank">📅 10:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سلام یاشار خوبی خسته نباشی دم شما گرم بابت همیشه امروز جمعه ۱۷ مهر اومدم بیرون می‌بینم که خیابونا و کوچه‌ها و اینا پر بسیجی پر سپاهی نیروی انتظامی پلیس یگان ضربت کوفت زهرمار پر ارزشیه نمی‌دونم چه خبره
@WarRoom
سلام خسته نباشی یاشار جان
نمیدونم مهمه یا نه ولی بعد مدتها بسیجیا و سپاهیا امروز تو خیابونن خیلی زیاد  , من عبدل آباد میومدم خیابان فرشته پر بود , جاهای دیگه هم همینطور</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25233" target="_blank">📅 10:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی: ارتش آمریکا در حال بررسی گزینه‌هایی برای
حمله مجدد به ایران و اجرای عملیات‌های نظامی دیگر پیش از انتخابات میان‌دوره‌ای ۳ نوامبر
است. پنتاگون پیش‌تر از فرماندهی مرکزی آمریکا خواسته بود آمادگی‌های لازم برای ازسرگیری عملیات گسترده علیه ایران را تکمیل کند؛ گزینه‌های احتمالی شامل حمله به تأسیسات انرژی، زیرساخت‌ها و اهداف هسته‌ای ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25232" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکنید. این پست رو‌ ذخیره کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25231" target="_blank">📅 09:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نیویورک‌تایمز: برخی شرکت‌های کشتیرانی برای عبور کشتی‌های خود از تنگه هرمز به ایران پول پرداخت می‌کنند. طبق گزارش لویدز لیست، کشتی کانتینری «نیوویجر» با مالکیت شرکت چینی بنگبو شنگدا ترنسپورتیشن و مدیریت شرکت یونایتد پایونیر شیپینگ در شانگهای، از طریق یک واسطه چینی برای عبور از مسیر نزدیک جزیره لارک به ایران پول پرداخت کرده است. بخش عمده بیش از ۲۰ کشتی ردیابی‌شده در این مسیر، تحت مالکیت شرکت‌های یونانی بوده‌اند. گزارش‌های جداگانه از پرداخت مبالغی تا
۲ میلیون دلار برای عبور هر کشتی
حکایت دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25230" target="_blank">📅 09:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بابک زنجانی: تا وقتی نفت بالای ۱۰۵ دلار باشه آمریکا ۱ موشکم نمیتونه بزنه
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25229" target="_blank">📅 08:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جروزالم پست به نقل از گزارش نیویورک‌تایمز نوشت سه ناو هواپیمابر آمریکا به‌زودی در خاورمیانه حضور خواهند داشت و پنتاگون طرحی برای یک کارزار علیه ایران تهیه کرده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25228" target="_blank">📅 08:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رهبر‌حذب «یاشار»گادی آیزنکوت، رقیب اصلی نتانیاهو، میگه نگرانه که نتانیاهو برای به تعویق انداختن انتخابات، ظرف دو هفته آینده یه حمله گسترده به ایران انجام بده.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25227" target="_blank">📅 08:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پرتاب موشک از بندر لنگه
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25225" target="_blank">📅 01:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3JVYPTUSN_H_Bh9n23VlYkp5jsqhawBno4J-aV_xx1dRSaxOQRXojg8o4iSmzRhWoBICWktyJwZuBRkDd-DsdqSLchOHv1O9lEDHB7DcLi3AxR-Y0JPbP0aEnWDasW-igRU75Iqdj11MTa7eTxy-fIhl76Oll3zwXNZvsydy0xfZiMk2qSHnkBF7Q0eHkcqhM523fI9WrIyK1KRyPb2HVUEpHZPcTPX0S5gm3-ENNQaNcvydKZiBbauu5_D4fHzPJ9KZyV6Jclp05AAfUCUL8OlHTgZ-15sUga7X4tcCp1Tepx5l3wybc3t8AKe_hMUC_Xyx-9C3pNOzXkZxjN-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a3b0dbfd.mp4?token=bnIboZLKyeOiYKzywskIqLrIvSxpAMkgwuizGP46AuZfkMUOdi81EawZ4K5Acor-jzyNMO9ym0hbCCOCJ1YCNOIUYWeGUpwop5BiYLBFIKjoHF5dU-Q3f7XEYeRQ9O7IQjZgN2nrFE1wBXsJF5VyqN25F9TAPK2s440YFDZiv0Oy7mJOO0RWc0ut9Y1Xm7s4LbCha6rgHIYgjtMWYH5o85yAoU97z-Zj-wOwqN_0s4ewNuUu3ESRvMuvKvge5HupB6bhamB06F_BCACBl9w8_opAq9SAtb0NMiDVxHFWPVwRg5amdp2xzam-qGXDlgNt-myDnwAF1B1PKdF9gIx5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a3b0dbfd.mp4?token=bnIboZLKyeOiYKzywskIqLrIvSxpAMkgwuizGP46AuZfkMUOdi81EawZ4K5Acor-jzyNMO9ym0hbCCOCJ1YCNOIUYWeGUpwop5BiYLBFIKjoHF5dU-Q3f7XEYeRQ9O7IQjZgN2nrFE1wBXsJF5VyqN25F9TAPK2s440YFDZiv0Oy7mJOO0RWc0ut9Y1Xm7s4LbCha6rgHIYgjtMWYH5o85yAoU97z-Zj-wOwqN_0s4ewNuUu3ESRvMuvKvge5HupB6bhamB06F_BCACBl9w8_opAq9SAtb0NMiDVxHFWPVwRg5amdp2xzam-qGXDlgNt-myDnwAF1B1PKdF9gIx5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید از نوع استتار تکاوران نیروی زمینی من را یاد شخصیت «گریفین» در فیلم شاهکار «مرد نامرئی ۱۹۳۳» انداخت. البته برای دوستان جدید شخصیت گریفین به صورت فقط یک «عینک» در انیمیشن «هتل ترانسیلوانیا» نیز حضور دارد.
😂
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25223" target="_blank">📅 01:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد پنتاگون پس از نشست محرمانه دونالد ترامپ و تیم امنیت ملی آمریکا در کمپ دیوید، گزینه‌های تازه‌ای برای ازسرگیری حملات گسترده به ایران تدوین می‌کند. یکی از سناریوهای مطرح‌شده،
انجام حملات طی یک دوره سه‌روزه
از حملات شدید علیه ایران است که موشک‌ها، پهپادها، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تاسیسات نظامی را هدف قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25222" target="_blank">📅 00:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روزنامه جروزالم پست گزارش داد که هدف از ترور
علیرضا تنگسیری، فرمانده نیروی دریایی سپاه، جلوگیری از رسیدن او به فرماندهی کل سپاه پاسداران
بود. به نوشته این روزنامه، مقام‌های اسرائیلی او را فرمانده‌ای توانمند و خلاق می‌دانستند که در صورت رسیدن به رأس سپاه، می‌توانست تهدیدی جدی‌تر از احمد وحیدی باشد. این گزارش همچنین مدعی شد برد کوپر، فرمانده سنتکام، حدود ۱۹ مارس در تماسی محرمانه از رئیس ستاد ارتش اسرائیل خواسته بود تنگسیری را هدف قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25221" target="_blank">📅 00:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ادعای فارس
: نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25220" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فارس: سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب استان کرمان ،کشته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25219" target="_blank">📅 23:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار المانیتور , جرد سزوبا: سناتور کریس مورفی، پس از دیدار جداگانه با
شیخ تمیم بن حمد آل‌ثانی، امیر قطر
و علی الثوادی، دیپلمات قطری و یکی از چهره‌های اصلی هماهنگ‌کننده میانجی‌گری میان آمریکا و ایران، گفت توافقی برای پایان دادن به جنگ با ایران
در آینده نزدیک بعید به نظر می‌رسد.
مورفی در سفر خود به قطر درباره تلاش‌های دیپلماتیک برای پایان جنگ با مقام‌های قطری گفت‌وگو کرد و تأکید کرد قطر همچنان نقش مهمی در میانجی‌گری میان واشنگتن و تهران دارد. این دیدارها در حالی انجام شد که مذاکرات آمریکا و ایران از طریق قطر بار دیگر با بن‌بست مواجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25218" target="_blank">📅 23:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرنگار اکسیوس: فلش‌بک: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا وارد جنگ اسرائیل علیه ایران شود یا نه.اما زمانی که این اظهارات را مطرح می‌کرد، در واقع از قبل تصمیمش برای حمله به تأسیسات هسته‌ای ایران را گرفته بود.
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز جنگ اسرائیل و آمریکا علیه ایران، ترامپ مدعی شد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
اما در واقع، ترامپ از قبل مجوز انجام حملات را صادر کرده بود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25217" target="_blank">📅 23:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b8f646ae.mp4?token=ANGehQ6GwaxP30565ykTuzPOX97iE4nk_BXHVlTro2ZZqZcHAwYy0cwbZWJnhmshD8yA_SCWP_1p8t0vpj_vrKqM83uru3wYhLk3N36niMhYSuIvHIc5KmmxGl6ZS7Y3__B47VkGpG-e0HQ4K2WzEZVuXZlK8Zgm2XcWse1YSRiQw5AhvT3UWcDNfsnw_Nt_rljLxScnZRcH0UXrwFG6koBI5fBS_82M3BR8n-YZe6Q742seijXTb15_8GPn2hystD58hKxRZw4UPgjJKoOjEnOOokNwNHKu21ugt7Jy6zZJfX-7uABdwtZvkaVwWOT9ea72uZZabPiUj3IXsyZAxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b8f646ae.mp4?token=ANGehQ6GwaxP30565ykTuzPOX97iE4nk_BXHVlTro2ZZqZcHAwYy0cwbZWJnhmshD8yA_SCWP_1p8t0vpj_vrKqM83uru3wYhLk3N36niMhYSuIvHIc5KmmxGl6ZS7Y3__B47VkGpG-e0HQ4K2WzEZVuXZlK8Zgm2XcWse1YSRiQw5AhvT3UWcDNfsnw_Nt_rljLxScnZRcH0UXrwFG6koBI5fBS_82M3BR8n-YZe6Q742seijXTb15_8GPn2hystD58hKxRZw4UPgjJKoOjEnOOokNwNHKu21ugt7Jy6zZJfX-7uABdwtZvkaVwWOT9ea72uZZabPiUj3IXsyZAxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه با پهپاد‌های موتور گازی‌ آبیش به منطقه ریزگری اربیل، کردستان عراق حمله کرد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25214" target="_blank">📅 23:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پارلمان اروپا امروز، ۸ اکتبر، قطعنامه جدیدی درباره وضعیت حقوق بشر در ایران تصویب کرد. این قطعنامه با
۵۴۱ رأی موافق، ۱۱ رأی مخالف و ۲۵ رأی ممتنع
به تصویب رسید و در آن
خشونت علیه غیرنظامیان، افزایش اعدام‌ها، سرکوب معترضان، فعالان حقوق بشر و روزنامه‌نگاران و استفاده از اعترافات تحت شکنجه
محکوم شده است. پارلمان اروپا همچنین خواستار لغو احکام اعدام ترانه رحیمی و لیلا ابوالحسنی و لغو مجازات اعدام در ایران شد و سرکوب اقلیت‌های قومی و مذهبی و سرکوب فرامرزی جمهوری اسلامی را محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25213" target="_blank">📅 23:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaTGMGMTFSIDkUmuiLLsiawWXkQAe8Ih7L8e4UHZ2Sl_EujpiS7nI9_pI5URxO6zA4rZLiT9wFgVdN5epCoXZktvLXneaiHWyI2YEYAPQMauylR6Q2t7aYJk56PW_0kDWlPLk6t_ng1R3wJsLjjM7WXo0tzTO-Te36Qeam0koEVP9PheNAViZlFmRk0TCXF2ZlPlAV7AA6BvXz9ySUuSvMbnjgnvlHVyUuNzQ_KElNDN1ptSmAJQAWcruQAACjf30SfJIJVL_YsgvX-6KFMybDR54OMd_olpnsV46h-3vYG6KUW9KxgOzu4CndTOYwnMsbnzO-YA5cOoysn2avFByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث : رسانه‌های جعلی تلاش می‌کنند این‌طور القا کنند که من از دشمن خواسته‌ام سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که منظورم این بود که
افزایش موقت قیمت بنزین، بهای کوچکی برای اطمینان از این است که ایران سلاح هسته‌ای نخواهد داشت.
تصور کنید اگر سن‌دیگو یا لس‌آنجلس بمباران شوند، چه بهای سنگینی باید پرداخت شود. من فقط مقایسه‌ای میان پرداخت مبلغی بیشتر برای مدت کوتاه بابت بنزین و
خطر بمباران شهرهای بزرگ آمریکا
انجام دادم. همه این را فهمیدند، حتی رسانه‌های جعلی، اما همچنان می‌گویند من خواسته‌ام دو شهری را که دوست دارم بمباران کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25212" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ff0b265b.mp4?token=iUrtN1-cI8W15WxDr8yT5lDllthdNNZE8ezJe_D5pOxB9Kh0RKkCeenji1XOiU4ydYMTScir8UiNYf1a3FEdSv_ZRUiwquHf8ahgLnvn8xEGESsCpQ2iqc2ZWMccRI43wa6Ukr3DL1yHAyLMHUiHaZWI_Lmj4G2Um7dqkIbayMMLtJ3GP572CE_AUd3QDlvuQ4Ah16yEJwzGpHznQJwU-POqGTIs717uPSYEpkCAx5dxvcZzk0AFhXdKKGezIB8kxiEPxy3uyGhS_lwQLBLANjheiwBaCNK25umYmDply261NGbkcfHUzAcs50X0yq6W25a9rhSwuWxNcxrxEZbYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ff0b265b.mp4?token=iUrtN1-cI8W15WxDr8yT5lDllthdNNZE8ezJe_D5pOxB9Kh0RKkCeenji1XOiU4ydYMTScir8UiNYf1a3FEdSv_ZRUiwquHf8ahgLnvn8xEGESsCpQ2iqc2ZWMccRI43wa6Ukr3DL1yHAyLMHUiHaZWI_Lmj4G2Um7dqkIbayMMLtJ3GP572CE_AUd3QDlvuQ4Ah16yEJwzGpHznQJwU-POqGTIs717uPSYEpkCAx5dxvcZzk0AFhXdKKGezIB8kxiEPxy3uyGhS_lwQLBLANjheiwBaCNK25umYmDply261NGbkcfHUzAcs50X0yq6W25a9rhSwuWxNcxrxEZbYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا: ما به‌دنبال
اداره و بازسازی ایران از طریق حضور نظامی
نیستیم و نمی‌خواهیم تعداد زیادی نیروی نظامی را در ایران مستقر کنیم یا کنترل مناطق این کشور را در دست بگیریم. هدف ما صرفاً این است که به آن رژیم اسلام‌گرای افراطی بگوییم: شما هرگز سلاح هسته‌ای نخواهید داشت. اینکه این مسئله به روش آسان حل شود یا به روش سخت، انتخاب با ایران است؛ اما در نهایت این رئیس‌جمهور است که تصمیم خواهد گرفت. و می‌توانم تضمین کنم اگر آن لحظه فرا برسد، اقدام ما سریع و قاطع خواهد بود. این رئیس‌جمهور اهل بازی کردن نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25211" target="_blank">📅 22:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f244d9f33.mp4?token=aDpi997A2DSIy49GWY6R-upwRTt5znFS90JIPGpeP-AIQiPpH_wnGB6p2nJM9yVr-9qoZDMVZfoOTj3kmUNdFS1so07rj_C86SjjLlI_MJzzuWrrdfokMlWjrnkqBicxPtpbfnYkDStzzRAJnlBlLF8qssokajCP1VrgaezIY9rbe4DC7YYsTCncWEI5E46RVbzAl5RHMHkODzZbQ-6ZnFTFNpwsAS96VefV1_oIy78GhsRG87gZxWhkrvv6o9MfGP2Wlau5xPZo8tw8t3U-f3u2x0KZtnj1edyCEPPcEZ-VRuVySS1QlFWz-C4HLBlMnKxyx6adtBllc0crOwDBVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f244d9f33.mp4?token=aDpi997A2DSIy49GWY6R-upwRTt5znFS90JIPGpeP-AIQiPpH_wnGB6p2nJM9yVr-9qoZDMVZfoOTj3kmUNdFS1so07rj_C86SjjLlI_MJzzuWrrdfokMlWjrnkqBicxPtpbfnYkDStzzRAJnlBlLF8qssokajCP1VrgaezIY9rbe4DC7YYsTCncWEI5E46RVbzAl5RHMHkODzZbQ-6ZnFTFNpwsAS96VefV1_oIy78GhsRG87gZxWhkrvv6o9MfGP2Wlau5xPZo8tw8t3U-f3u2x0KZtnj1edyCEPPcEZ-VRuVySS1QlFWz-C4HLBlMnKxyx6adtBllc0crOwDBVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، درباره ایران:
ترامپ رئیس‌جمهوری نیست که بازی دربیاورد. او رئیس‌جمهوری نیست که
اتلاف وقت بیش از حد را تحمل کند.
ترامپ صلح می‌خواهد، اما حاضر است برای رسیدن واقعی و تاریخی به صلح،
هر کاری که لازم باشد انجام دهد.
ایرانِ دارای بمب هسته‌ای، اتفاق بدی است؛ نه فقط برای ما، بلکه
برای تمام جهان.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25210" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایلان ماسک نشان ملی علوم را دریافت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25209" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05da9e1cfb.mp4?token=Wjibp6x6-9lsf1OEhgzqofO4r5Y5JB8QD_sUMVIKnNIy_Gv7UzucPzDrXLH7Cju2w1hI5aDv2AecUMGDHTDFUD2g6PMGBR00TUPfsIlluZLFlyFewOAFv7pcMWegfn51XAsT2Na4U3onLFRVKuJLsXIps7Y6tqCOY_7eJ3oe7lKgDf0ZsOKwctaFJ_HW7ta8uGge5PQ1YNRA-BimbE-4KPsH_VnXRp6Q0Y2c7iBki37jdyqp-X5t7s9nA56AKoITL-OgrvjqZYQT7EfNE-Pfsn7-16jBe58aKkdQ3KiGL_cIJDAmZdnlz2ApNKanZy0GhPlKLMppZgrTyvxbWHIFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05da9e1cfb.mp4?token=Wjibp6x6-9lsf1OEhgzqofO4r5Y5JB8QD_sUMVIKnNIy_Gv7UzucPzDrXLH7Cju2w1hI5aDv2AecUMGDHTDFUD2g6PMGBR00TUPfsIlluZLFlyFewOAFv7pcMWegfn51XAsT2Na4U3onLFRVKuJLsXIps7Y6tqCOY_7eJ3oe7lKgDf0ZsOKwctaFJ_HW7ta8uGge5PQ1YNRA-BimbE-4KPsH_VnXRp6Q0Y2c7iBki37jdyqp-X5t7s9nA56AKoITL-OgrvjqZYQT7EfNE-Pfsn7-16jBe58aKkdQ3KiGL_cIJDAmZdnlz2ApNKanZy0GhPlKLMppZgrTyvxbWHIFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک نشان ملی علوم را دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25208" target="_blank">📅 22:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osrl4d5pm37-bxtCuRB3HJ-xtkIw8VYzetBY763BLo3Ws3i2uI2jP4a_YXxXWVGzA0DAUzm6TQtYz5eDnqXhrEf_LPnYBPi3NDO6nRME3rVAoHQ16E3xFvPBBK56RVJwohqNBchxGAXncJxFJnE90Gysl01S4uYdnr7QNkP84oKEyUOCw6772VGAlPkuzQRjo9gqGYau0mp3BtbEvauNNWl4R5KDiE06VZgTIIYfjG-YSUgPyOGdoyOLRtpBbuGFY7ZwFchR-mArpPlhUdo8VHVTXzA7nBZVEbbLIHQAOY0-wWicSReBJeHvE0YWU44Vr5-K6zuaPSywqUlZ_InF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان و پوتین در حاشیه اجلاس سران کشورهای مستقل مشترک‌المنافع و اجلاس محیط‌زیستی دریای کاسپین در ترکمنستان دیدار و درباره
تقویت همکاری‌های اقتصادی و راهبردی در حوزه‌های انرژی، کشاورزی، حمل‌ونقل و تجارت
گفت‌وگو کردند. دو طرف بر تسریع اجرای پروژه‌های مشترک و گسترش همکاری‌های دوجانبه تأکید کردند.
خبرگزاری تاس: پوتین در این دیدار وضعیت خاورمیانه را
بحرانی و حاد
توصیف کرد و گفت روسیه آماده است برای مدیریت بحران و بازگشت ثبات به منطقه، در کنار ایران باشد و از تلاش‌های تهران برای پایان دادن به درگیری‌ها حمایت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25207" target="_blank">📅 21:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال ۱۴: مقام‌های سیاسی و امنیتی اسرائیل نشانه‌هایی جدی از احتمال ازسرگیری درگیری با ایران مشاهده کرده‌اند و به همین دلیل ارتش خود را برای شرایطی آماده می‌کند که ممکن است به سرعت به یک درگیری گسترده تبدیل شود
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/25206" target="_blank">📅 21:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایلان ماسک
:
ایلان توماس ادیسونِ دوران معاصر ماست.
@WarRoom
یاشار : الان خرابش کرد یا تعریف کرد؟!</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/25205" target="_blank">📅 21:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/25204" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fceaa00395.mp4?token=co8asWnvgQ_5JbwKl-sybLjyAo7kYGHdb9v20OHbBIPfMiF5WkfCNDEklq701y0gblIgK7B7o1R1yjfMLr5zLxq92DoFz_bIZlqcbIp5mWBoc9ztg_Xq0yo2-jIndlykwnVxxZWgrkQQOfq0UrM2xqsZY67jnshLwevHeAQzb5buwSSI8UlqCLAyYFLsTkMn7Wtuv7oc7h2-pLWS-gaSvqwFzOekeMj6hvX3maSCYYe-bK_1CKhQhPJ_RtaHRHyfuL9OAOdS64hUc4yuHPQwVfeEjlcKMm20pMpyq54ucxeoGKLAJrFvvImw9p3fhZXo3bbJJM8SmCy3-d6-uV0ic6CaV9aS7e8OxLlkM_h71Llh7HTYrB_bjVM1QrVWZbN3-Kf9xPY1GXmcSEu62S0ihNKTJVhw6JD7pXjm5hCaro-AtJqaLWQb2hxLaJ9E4ZBkzdzj-efQG-RTK74QgSDdn2oc_nnEXAwqzwMZ6e96jUz8rdWHIXILXfWziKuRyeN000O5PgqoxsjM0-0HIaca-mRFCEXgZSpjigAAyvQGhfPbhP45qbMj9F8LH_cWwgzrpMnoII25CxLfoSZhZe4JLSjLs9nSXBziycO8PNbJ3338eysON07RU2g8xjztGdsXO4-leXIf0ljo8klEanl4glteFwi5__COWQTMgHhkODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fceaa00395.mp4?token=co8asWnvgQ_5JbwKl-sybLjyAo7kYGHdb9v20OHbBIPfMiF5WkfCNDEklq701y0gblIgK7B7o1R1yjfMLr5zLxq92DoFz_bIZlqcbIp5mWBoc9ztg_Xq0yo2-jIndlykwnVxxZWgrkQQOfq0UrM2xqsZY67jnshLwevHeAQzb5buwSSI8UlqCLAyYFLsTkMn7Wtuv7oc7h2-pLWS-gaSvqwFzOekeMj6hvX3maSCYYe-bK_1CKhQhPJ_RtaHRHyfuL9OAOdS64hUc4yuHPQwVfeEjlcKMm20pMpyq54ucxeoGKLAJrFvvImw9p3fhZXo3bbJJM8SmCy3-d6-uV0ic6CaV9aS7e8OxLlkM_h71Llh7HTYrB_bjVM1QrVWZbN3-Kf9xPY1GXmcSEu62S0ihNKTJVhw6JD7pXjm5hCaro-AtJqaLWQb2hxLaJ9E4ZBkzdzj-efQG-RTK74QgSDdn2oc_nnEXAwqzwMZ6e96jUz8rdWHIXILXfWziKuRyeN000O5PgqoxsjM0-0HIaca-mRFCEXgZSpjigAAyvQGhfPbhP45qbMj9F8LH_cWwgzrpMnoII25CxLfoSZhZe4JLSjLs9nSXBziycO8PNbJ3338eysON07RU2g8xjztGdsXO4-leXIf0ljo8klEanl4glteFwi5__COWQTMgHhkODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : عموی من، دکتر جان ترامپ، از سوی دولت آمریکا مأمور شده بود گزارشی درباره نیکولا تسلا تهیه کند.
آنها می‌خواستند بدانند: آیا او واقعاً وجود داشته یا نه؟ آیا واقعاً یک نابغه بوده یا نه؟
عموی من، پس از مدت نسبتاً کوتاهی، به این نتیجه رسید که
تسلا واقعاً یک نابغه بزرگ بوده و از هر نظر کاملاً واقعی بوده است.
وگرنه مجبور بودید اسم شرکت خودروسازی را تغییر بدهید.
حالا اگر من آن گزارش را تهیه می‌کردم، ایلان، شاید می‌گفتم: «آن‌قدرها هم خوب نبود.»اما عموی من آدم متفاوتی نسبت به من است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25203" target="_blank">📅 21:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece6af3331.mp4?token=msCTAtREI-cA3m1XA4Mtemfs-nnVq38neGStZiGN0RTom1JzSO9EfgxmM4ZUzsQUwpM-GZzuskCFbBCW8hZt4TZIseKTJdr4U0Tt93AC_1h_bP80wjHe3WAr-vZp-X89qOIHfMbCcJWnulX92CcRuR5VYLf9iuJPODVHP3PPRlYETwVkmZMGgsuxeTNCy34Jnpx_y1Ft3ZxD48fWcjl4vfBeVYKDvV1IdGg7yf-Cs0iibbwOk585VX6KNPW44wu4XUzKwmkkRR1QM703o1wz_Jfhr41oOQ17QFRrq6oLivdflspPZ2Ig_DVFRA8REWwCR8-Jy_zjy3Xn6LpiMar1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece6af3331.mp4?token=msCTAtREI-cA3m1XA4Mtemfs-nnVq38neGStZiGN0RTom1JzSO9EfgxmM4ZUzsQUwpM-GZzuskCFbBCW8hZt4TZIseKTJdr4U0Tt93AC_1h_bP80wjHe3WAr-vZp-X89qOIHfMbCcJWnulX92CcRuR5VYLf9iuJPODVHP3PPRlYETwVkmZMGgsuxeTNCy34Jnpx_y1Ft3ZxD48fWcjl4vfBeVYKDvV1IdGg7yf-Cs0iibbwOk585VX6KNPW44wu4XUzKwmkkRR1QM703o1wz_Jfhr41oOQ17QFRrq6oLivdflspPZ2Ig_DVFRA8REWwCR8-Jy_zjy3Xn6LpiMar1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : می‌خواهم به شرکت اسپیس‌ایکس بابت بازگشت ایمن فضانوردان مأموریت شماره ۱۲ از ایستگاه فضایی بین‌المللی، که چند ساعت پیش اتفاق افتاد، تبریک بگویم.
تصور کنید اگر همه چیز به این خوبی پیش نمی‌رفت؟ آن لحظه خیلی خوشایند نخواهد بود. فکر می‌کنم شاید ایشان اینجا نبودند.شاید شما هم اینجا نبودید. اما همیشه برای ایلان ماسک همه چیز به خوبی پیش می‌رود، نه؟ ما به شما افتخار می‌کنیم، به شما خیلی افتخار می‌کنیم، شما یک گنجینه ملی هستید
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/25202" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکسیوس: سرلشکر ایال زامیر، رئیس ستاد کل ارتش اسرائیل، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که
اگر جنگ با ایران طی سه هفته آینده از سر گرفته شود، اسرائیل ممکن است مجبور شود انتخابات ۲۷ اکتبر را به تعویق بیندازد.
زامیر همچنین هشدار داد که ایران ممکن است در پاسخ به حملات، اسرائیل را با موشک هدف قرار دهد. این هشدار پس از آن مطرح شد که مقام‌های آمریکایی او را در جریان آمادگی‌های نظامی برای ازسرگیری عملیات علیه ایران قرار دادند.
ترامپ پس از آن اعلام کرد که
آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/25201" target="_blank">📅 21:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIRxyHtPtJu3GBjLKfQV6YvJ8xOU3TXFhP5Fvbv7Cp28VoOEbxI301l0RbGRu6NbaCQVGFgOjmd-0QsUR3Op41e-KJ9ohHegcri070wDFrGWPKdP9j1Y_ErlSntAeANdWp_tTUATIMMOpLmzMoykVMbl3gpZAQNrs1vLPY4xWxVkK5rWMyL4F6y6sCKHkQ3QTDilqUaf5aw6dOiGNgZ0gH2fpUaz9QO3f38LVWEqODwrFOwiQnbkuMW1zWCBvDH73CZpAHaeOw4jApi9JheW_UlzVEcIR2N-hYWlpANCLPb8toSys-KuG3RBSyV66TL6GyCoVzlQXE3W_P9D3ciBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که، با وجود اینکه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد، و با وجود اینکه محاصره همچنان با تمام قدرت و به‌طور کامل ادامه خواهد داشت، در حالی که نفت با رکوردی از تعداد بشکه‌ها از تنگه هرمز عبور می‌کند؛
تنها دیشب ۲۲ میلیون بشکه نفت عبور کرده است، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به ایران رفته باشد!
ما پیش از انتخابات میان‌دوره‌ای آمریکا که در ۳ نوامبر برگزار خواهد شد، به هیچ‌وجه به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25200" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: دفتر کنترل دارایی‌های خارجی آمریکا، ۱۲ کشتی و شرکت‌های مالک و اپراتور آنها را به‌دلیل انتقال نفت و محصولات پتروشیمی ایران تحریم کرد. به گفته خزانه‌داری، این کشتی‌ها
صدها میلیون دلار نفت و فرآورده‌های نفتی ایران را به بازارهای خارجی منتقل کرده‌اند
و درآمد حاصل از این صادرات به تأمین مالی برنامه‌های تسلیحاتی، نیروهای نیابتی و نهادهای امنیتی جمهوری اسلامی کمک می‌کند. کشتی‌های تحریم‌شده شامل هوت، اوشن کوی، نورث استار، فلیسیتا، آتیلا ۱، آتیلا ۲، نیبا، لوما، رمیز، دانو‌تا ۱، علا و گس فیت هستند. شرکت‌های هدف نیز شامل پوروس مریتایم ونچرز، اوشن کادوس شیپینگ، میسترال فلیت، وست مِرین، بهنگام تدبیر قشم، پاروس مریتایم، وانسا گس شیپینگ، گلدویو مریتایم سرویسز و ایتاکی مریتایم اند تریدینگ هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25199" target="_blank">📅 20:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25198" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای در جریان است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25197" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا : دو مرد لتونیایی است که در نزدیکی پایگاه هوایی سلطنتی مولزورث بازداشت شده‌اند. پلیس متروپولیتن ابتدا آنها را به ظن ورود غیرقانونی به یک مکان ممنوعه بازداشت کرد، سپس هر دو را طبق قانون امنیت ملی به دلیل ورود به یک مکان ممنوعه با هدفی مغایر با منافع بریتانیا دوباره دستگیر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25196" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25195" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی آمریکا امروز در یک نشست مجازی با شرکای بین‌المللی حمل‌ونقل دریایی درباره وضعیت تنگه هرمز گفت
افزایش تلاش‌ها برای تضمین آزادی کشتیرانی و تردد امن کشتی‌های تجاری ضروری است.
دریادار برد کوپر، فرمانده سنتکام، از حمایت مستمر صنعت کشتیرانی و نهادهای دولتی آمریکا تشکر کرد و به خسارت‌ها و فداکاری‌های خدمه غیرنظامی در پی حملات ایران اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25194" target="_blank">📅 18:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6azXfQixveQGnUzcJLIMvF9Of1hWi3Jcn2fVujuR6Y_f9uy2Ae6RNBuIA9DRMAlw2d-yRzaBZkW1l7jZOn5rB_Ze3ieGVrL7HRfwF-y0N6x6SdxT57mn8OAL9F_EICPrQ3Yk3qCFmNF1cQcewpv55FLMD9M9B73zg4B7rBcdOJsllHF_dAtLNOsEQN63zZ3-MF7ARIHx_q5tTcWi4X56Psh3chupeHtwGnAwKDuQdF87O6BQNLV2tBqgxYwRFbruLrU8efIw1pGqfPhKStTJ9PxKR_tqPPjGBYRYtomtkJ-Zpg8pxq05cFxcDsJPBjOELDifACRVCFow1eQNASb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظارت دریایی بریتانیا (UKMTO) گزارش تأییدشده‌ای را از یک منبع معتبر دریافت کرد مبنی بر اینکه یک تانکر حامل نفت خام، در روز سه‌شنبه، هنگام عبور از تنگه هرمز، مورد اصابت یک پرتابه قرار گرفته است.
هنوز هیچ گزارشی مبنی بر وقوع تلفات انسانی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25193" target="_blank">📅 18:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/918015a856.mp4?token=oVzf6uc3M4Sq3_Vyc1luMwNJMJCRqMeaSYqX-U_NWoE2hVzb1_J3znlWL479LASOSmcIZW9tZMqgL2lI-gTH_iNI0EhJrSyZ9fppla-zV9-1Af_ZGNvGcC1sCECms35APwtX9JkwIKYrtYx4W4JQsG8E23sNCWnw-M4cER_-MiEVFhBiXXxYNVngY0833MlQWeo0DIW0kOXlotoo_CBCw2k7I-h-okM8UZyC1b4iAu8zcLEL3QcqEbcRFdw7GipoA0FVik4C6RI2Ny4vTRVTusOK32LkvZ7XCEeHOI2oWj9J8_2Kkq1N-yA4zx62BZE-8q1W0TzaP8A-5t_3g_PbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/918015a856.mp4?token=oVzf6uc3M4Sq3_Vyc1luMwNJMJCRqMeaSYqX-U_NWoE2hVzb1_J3znlWL479LASOSmcIZW9tZMqgL2lI-gTH_iNI0EhJrSyZ9fppla-zV9-1Af_ZGNvGcC1sCECms35APwtX9JkwIKYrtYx4W4JQsG8E23sNCWnw-M4cER_-MiEVFhBiXXxYNVngY0833MlQWeo0DIW0kOXlotoo_CBCw2k7I-h-okM8UZyC1b4iAu8zcLEL3QcqEbcRFdw7GipoA0FVik4C6RI2Ny4vTRVTusOK32LkvZ7XCEeHOI2oWj9J8_2Kkq1N-yA4zx62BZE-8q1W0TzaP8A-5t_3g_PbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
می‌خواهید مشکلات را ببینید؟ بگذارید به لس‌آنجلس حمله کنند یا به جایی مانند سن‌دیگو. بگذارید به یکی از شهرهای بزرگ ما حمله کنند.
به این می‌گویند مشکل.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/25192" target="_blank">📅 18:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4309370e.mp4?token=uS6U15nb9ob7vCJ7CtwJlSSdyG7Lt1GnpKMzVBdvEHMLwV42HQ28wysZ4g3VSqKWTWRkNFREdvubYGNrPKLEsSAH_XY4pDA-2hlwEYh5MyO74JWilsyVQrqQZJL7M6opsJk3tvo--gK4KgRvEz4HBxqXkwTPrH8vKOTWXzauiezTQUQ4_AtOZL5ozVq4dASKz9lL4Ztf9Ipa7Z82VVywOqcLepUELmo_ObTBAFgAVkO5TdV7B3rjgVfOL_FKiB6o0cXWaZrGSZlG0QinSGD72oU9D8J_okcV4X7gLvh1M2JzvFAVguFLrLRMPu_xfXbG-ynRn4rLu9kQTJipSaKyhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4309370e.mp4?token=uS6U15nb9ob7vCJ7CtwJlSSdyG7Lt1GnpKMzVBdvEHMLwV42HQ28wysZ4g3VSqKWTWRkNFREdvubYGNrPKLEsSAH_XY4pDA-2hlwEYh5MyO74JWilsyVQrqQZJL7M6opsJk3tvo--gK4KgRvEz4HBxqXkwTPrH8vKOTWXzauiezTQUQ4_AtOZL5ozVq4dASKz9lL4Ztf9Ipa7Z82VVywOqcLepUELmo_ObTBAFgAVkO5TdV7B3rjgVfOL_FKiB6o0cXWaZrGSZlG0QinSGD72oU9D8J_okcV4X7gLvh1M2JzvFAVguFLrLRMPu_xfXbG-ynRn4rLu9kQTJipSaKyhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
ما ایران را به شدت شکست داده‌ایم. دیگر تهدید سلاح هسته‌ای وجود ندارد.
آن‌ها در حال حاضر در یک آشفتگی کامل هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25191" target="_blank">📅 18:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af618364fb.mp4?token=r0plh7EWfCzygq0jusyrgV9Bmjg2hTBmUR6npw_vyqfwtFdM72brTMS0l5HZL7B1Wnd70QnbmLQyNiHpbgHyucSFnEYzSt_7Ns9Vo-iCF7AzKiIupmq0mtgOZFFvhagdmqWzrhfc7oX7wDwDfKNnCJvMH0AVoI-aRQJrfxLoSXeM7sqxmJsgXwhf80jx5zdF73tCu8TbDtL93i52_5dHa0iDh1iVJQ-w2XVLRc32qOIpSdUE3voa3Q4Y1TxPaH-JgURXysdn-HFUBHd6VoZtkUrjM4d3VTcyyRdBe2xlT9WnGufSup4audBjAYw1gCMjnB1uycK5dHjT8Aku9UE-1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af618364fb.mp4?token=r0plh7EWfCzygq0jusyrgV9Bmjg2hTBmUR6npw_vyqfwtFdM72brTMS0l5HZL7B1Wnd70QnbmLQyNiHpbgHyucSFnEYzSt_7Ns9Vo-iCF7AzKiIupmq0mtgOZFFvhagdmqWzrhfc7oX7wDwDfKNnCJvMH0AVoI-aRQJrfxLoSXeM7sqxmJsgXwhf80jx5zdF73tCu8TbDtL93i52_5dHa0iDh1iVJQ-w2XVLRc32qOIpSdUE3voa3Q4Y1TxPaH-JgURXysdn-HFUBHd6VoZtkUrjM4d3VTcyyRdBe2xlT9WnGufSup4audBjAYw1gCMjnB1uycK5dHjT8Aku9UE-1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
پیروزی جمهوری‌خواهان در ماه نوامبر برای برنامه‌های شما چه معنایی دارد؟
پرزیدنت ترامپ:
خب، فکر می‌کنم این به معنای میراث است. فکر می‌کنم بسیار مهم است. داشتن یک پیروزی واقعاً تأییدی است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25190" target="_blank">📅 18:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز: قیمت نفت برنت امروز بیش از ۴.۵ درصد افزایش یافت و به حدود
۱۰۴.۷۵ دلار
رسید؛ نفت WTI نیز به حدود ۹۲.۲۸ دلار رسید. تشدید حملات به کشتی‌ها، نگرانی درباره هرمز و درگیری عربستان و حوثی‌ها از عوامل اصلی افزایش قیمت‌ها هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25189" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36deea25c.mp4?token=XWpdNZN6uyzYRJSx9RIvHwzA1ylBU4tKWYflaAvktCpkcuKZA0w_jGnkL6O6e0Zy4djovbFWEoBUvQ6xokJMbd_RizkSzhaM9PhZIi9em0yvlE9ExeoxPiOe12N97fXNr-tnIgn6av2tY-IoyVq6kLia3avhJQay-wJFzGA_BG4hRKX1XOX-o3Y77uEpmT8QTW5B_JZ2dVJF7d_IyZU-ME8wflua_XOp54DErO3DCL8zZL8ZIkAVIr-A6k26IIp2aN8jThY4htZAa3UkANpMYOmz01i3A1ijCgkEwGc3bS1cntGEKZt74OB8Ld5RQDh8ewX8fHeDBFiDPb-cg37PQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36deea25c.mp4?token=XWpdNZN6uyzYRJSx9RIvHwzA1ylBU4tKWYflaAvktCpkcuKZA0w_jGnkL6O6e0Zy4djovbFWEoBUvQ6xokJMbd_RizkSzhaM9PhZIi9em0yvlE9ExeoxPiOe12N97fXNr-tnIgn6av2tY-IoyVq6kLia3avhJQay-wJFzGA_BG4hRKX1XOX-o3Y77uEpmT8QTW5B_JZ2dVJF7d_IyZU-ME8wflua_XOp54DErO3DCL8zZL8ZIkAVIr-A6k26IIp2aN8jThY4htZAa3UkANpMYOmz01i3A1ijCgkEwGc3bS1cntGEKZt74OB8Ld5RQDh8ewX8fHeDBFiDPb-cg37PQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو: حکومت ایران مجروحان اعتراضات را در بیمارستان‌ها می‌کشد
حکومت ایران وقتی معترضان زخمی می‌شوند، وارد بیمارستان‌ها می‌شود و آن‌ها را می‌کشد؛ گاهی حتی پزشکان و پرستارانی را که آن‌ها را درمان کرده‌اند نیز به قتل می‌رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25188" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز:
خطر حمله به نفتکش‌ها در اطراف تنگه هرمز افزایش یافته
و هفته گذشته بیشترین تعداد حملات از آغاز جنگ ثبت شد. ایران به کشورهای منطقه هشدار داده هرگونه تلاش برای ایجاد مسیرهای جدید صادرات نفت در اطراف هرمز را اقدامی خصمانه می‌داند و احتمال استفاده از موشک، پهپاد و قایق‌های نظامی برای جلوگیری از این مسیرها وجود دارد. در تازه‌ترین مورد، یک نفتکش شیمیایی در نزدیکی قطر هدف چند پرتابه قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25187" target="_blank">📅 17:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548fb32aef.mp4?token=qEwhbvc7fqHdYGkvrHuZNXMf3mztees5X04UnFUK-mBe_IfAVWM1SB3ZXOzx6V3-lohdw4gRJ50Cl6k2f62xT7MQdmuZxcnFUnd79r9606Htrk3mh1YTvV6yhJV5rkGVTUZ9tlttQjC5p_aMVvduL0evxa350kI0-KCgnPlZYoIbvTgvPctAvmzrxfDsnD_R4lBJe-WniyxVapOD09cA3myjEJetSigf6Y1dEOuU_6EB0c8EdRoZVLeUMf8O4JyuN69t8WEBvY8IWTiMdSwVp8KudQMjf68-zeXSLs8bcvGmQ-2vH5pfYd9vHmT6yVn03DXlBqWRyWT2RnTRyX815w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548fb32aef.mp4?token=qEwhbvc7fqHdYGkvrHuZNXMf3mztees5X04UnFUK-mBe_IfAVWM1SB3ZXOzx6V3-lohdw4gRJ50Cl6k2f62xT7MQdmuZxcnFUnd79r9606Htrk3mh1YTvV6yhJV5rkGVTUZ9tlttQjC5p_aMVvduL0evxa350kI0-KCgnPlZYoIbvTgvPctAvmzrxfDsnD_R4lBJe-WniyxVapOD09cA3myjEJetSigf6Y1dEOuU_6EB0c8EdRoZVLeUMf8O4JyuN69t8WEBvY8IWTiMdSwVp8KudQMjf68-zeXSLs8bcvGmQ-2vH5pfYd9vHmT6yVn03DXlBqWRyWT2RnTRyX815w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا :
هیچ کاری علیه ایران وجود ندارد که بخواهیم یا لازم باشد انجام دهیم و نتوانیم آن را انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25186" target="_blank">📅 16:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر امور خارجه، چپقچی :
روند مذاکراتی همچنان ادامه دارد و از طریق میانجی‌ها پیام‌ها در حال رد و بدل شدن است.ما طرح خود را که تحت عنوان «طرح هفت‌روزه» ارائه کرده بودیم، مطرح کردیم و دیدگاه‌های طرف آمریکایی را نیز در مقابل آن شنیدیم. در حال حاضر مشغول بررسی دیدگاه‌های آمریکایی‌ها هستیم و فکر می‌کنم ظرف چند روز آینده پاسخ خود را ارائه خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو هواپیمابر هسته‌ای روزولت قرار است برای نخستین‌بار طی حدود
چهار سال
وارد بندر
یوکوسوکا در ژاپن
شود. شورای شهر یوکوسوکا روز چهارشنبه از مقامات شهری و شهردار خواسته برای ورود یک ناو هسته ای آماده باشند، اما
نام ناو، تاریخ دقیق ورود و مدت توقف هنوز اعلام نشده است
. ژاپن قرار است فقط ۲۴ ساعت پیش از ورود، اطلاع رسمی دریافت کند.
ناو
USS Theodore Roosevelt (CVN-71)
و گروه رزمی آن در حال حاضر در اقیانوس آرام هستند و برای یک
استقرار طولانی‌مدت در خاورمیانه
به سمت غرب حرکت می‌کنند. بنابراین
روزولت گزینه اصلی برای این توقف  کوتاه ، یوکوسوکا محسوب می‌شود.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25184" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">BTC 82,500$
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دلار و تتر ۲۶۸،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25181" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مراسم خاکسپاری جاویدنام علیرضا رئیسی که همراه با علیرضا سپاهی حکمش اجرا شد @WarRoom
🖤</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25180" target="_blank">📅 15:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رویترز: هفتمین مظنون پرونده طرح ادعایی حمله به پایگاه هوایی فرفورد بریتانیا با پهپاد آزاد شده اما تحقیقات ضدتروریسم ادامه دارد. پلیس بریتانیا این پرونده را مرتبط با یک طرح احتمالی با حمایت ایران بررسی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25179" target="_blank">📅 14:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیویورک‌تایمز: اسرائیل به آلمان درباره افزایش خطر حملات احتمالی مرتبط با ایران علیه پایگاه‌های نظامی آمریکا، به‌ویژه
رامشتاین و اشپانگدالم
، هشدار داده است. ارزیابی‌های اطلاعاتی احتمال حمله با پهپاد را نیز مطرح کرده‌اند، اما تاکنون زمان یا هدف مشخصی برای حمله تعیین نشده است. هم‌زمان، تحقیقات درباره طرح ادعایی حمله به پایگاه آمریکایی فرفورد در بریتانیا ادامه دارد و مقام‌های بریتانیایی به احتمال دخالت ایران اشاره کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25178" target="_blank">📅 14:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1a2241b4.mp4?token=O8zdCUyeMlBYcjSyuvrMf1p1DlCUBkbD6xTh3i_6595rBn8MI4XItj3q9pi1ZGW7H8TgzKtn84UcKrJ9rCfWF1Zj253XNMjQU6XhDkznLrMKzPLI2ZnBTSvLdIDFMnugoVuv1k21P-4EHuGVCNHDiTns0tiH7P3gDjizC3K4b4r6SOeAQBnkhTKLYZiaAYE4f4D7RvFzdJ5b3eE6klnv5zSyBoldm5vNPCMznirYf1pE0sU_jIJH23OhuInLCsFEge1tGJiT4kjBvl7J2hXD4RFHzGKyZwhRmo9C8UDcdXuXNm1Aj2C_WnuMKIUQLPdLrGU4xJKswrsboE_4WFLXli6t1j4LvRLkmu1ibJdYxgqPFzSFPSsOHbby4y2-OkcILBO1Bp0Ajy_vFqnAN_ypw531JKCVbKmw6WC4SPSobxAmwi-dg-Nx4Tjp-rQCSeRQQ8aGEeOax8IwSmOY4du00LgBSecMgdkL8yf7wk-N30lP7gIN-RKzD7-jJcqNw8t6_2GShdXkhnOA2T2nTG2QbeGcTiBtSIb3vyNwSiq2Su-syuhI_YRS1aUQm0Y374a_zubuail4M64_KpaB0xyoscuo5HlICO82YjAo3StTU5ulN-XFlfiKNYX-8dh-HqAAiZdtmJ4NAlqsga_d9ELeIQvEMDdoSjdwpgfjB608ppY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1a2241b4.mp4?token=O8zdCUyeMlBYcjSyuvrMf1p1DlCUBkbD6xTh3i_6595rBn8MI4XItj3q9pi1ZGW7H8TgzKtn84UcKrJ9rCfWF1Zj253XNMjQU6XhDkznLrMKzPLI2ZnBTSvLdIDFMnugoVuv1k21P-4EHuGVCNHDiTns0tiH7P3gDjizC3K4b4r6SOeAQBnkhTKLYZiaAYE4f4D7RvFzdJ5b3eE6klnv5zSyBoldm5vNPCMznirYf1pE0sU_jIJH23OhuInLCsFEge1tGJiT4kjBvl7J2hXD4RFHzGKyZwhRmo9C8UDcdXuXNm1Aj2C_WnuMKIUQLPdLrGU4xJKswrsboE_4WFLXli6t1j4LvRLkmu1ibJdYxgqPFzSFPSsOHbby4y2-OkcILBO1Bp0Ajy_vFqnAN_ypw531JKCVbKmw6WC4SPSobxAmwi-dg-Nx4Tjp-rQCSeRQQ8aGEeOax8IwSmOY4du00LgBSecMgdkL8yf7wk-N30lP7gIN-RKzD7-jJcqNw8t6_2GShdXkhnOA2T2nTG2QbeGcTiBtSIb3vyNwSiq2Su-syuhI_YRS1aUQm0Y374a_zubuail4M64_KpaB0xyoscuo5HlICO82YjAo3StTU5ulN-XFlfiKNYX-8dh-HqAAiZdtmJ4NAlqsga_d9ELeIQvEMDdoSjdwpgfjB608ppY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم خاکسپاری جاویدنام علیرضا رئیسی که همراه با علیرضا سپاهی حکمش اجرا شد
@WarRoom
🖤</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25177" target="_blank">📅 14:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان روابط عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت. متأسفانه در این درگیری…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25176" target="_blank">📅 13:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9s9y0c1vU-LzUWJZD2J0RZxFEDw2qypnw9lcP92sNtYsuA8I_2XZHx0jUBtPyN_0lvgUlp2HemHpD2whBbHIULlfFmC8ePvARKuxdp4A513vJMXmDIYIprVAfk6uX4E1iP4ELGKLz95yLjDMBLKi1zXL6c2z8S1KQRSrO_zt2yau5wwP7-3-H2Pbzwkr4Lurd8ARKt1KcBIGHo_y0RoI1qIBdxTHzEQ7YQswyTxGsmTsEq3NmvCcrmNWDkPa0_rQGHh4Qb9hUbyzKaLOcW1MO6vt3gs__1d6mgjMBHFLT9BQG7jyzirWT8w5E0mXuJeGawyoUwI_Krh6R6NPp0jWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : دیروز ناو هواپیمابر آبراهام لینکلن آمریکا به سن‌دیگو خانه خود بازگشت و عرزشی ها آن را به تمسخر گرفتند، ولی نکته مهم و شکه کننده که دیدم در این ویدیو و آنها باید گریه کنند این است که نشانه‌های انهدام(کیل مارک) ثبت‌شده رویش حدود ۱۰۵ پهپاد و ۳۴ ناو جنگی را در این ویدیو نشان میدهد عملکرد قابل‌توجهی برای تنها یک گروه هوایی مستقر روی یک ناو هواپیمابر.هگست وزیر جنگ پیشتر گفته بود که ناو لینکلن و گروهش ۶۴ ناو جنگی ایران را نابود کردند (بیش از ۲/۳ام نیروی دریای ایران )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25174" target="_blank">📅 13:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mf-Rjk3MeRD1uWQBIf08ij7ga_3HkJuXOYOOTsYxeHXtBKmQ0SnmjDzex7yB_3-k0GTr53eVrLZ5CKguyg_vtxRkxOTa8ktuq5XRFP0pGRENLEZMjyLeHF8z0IgfbcaJ9bsNGQB5DXNFE6KfBX14t2bNl6sQEpDMGEBWorbL8pYXCRziEEWnPUGgqdigIHTfYOp23__DM-Mr35o-sqKgn1rGyXf4skd4Qf51trOyoVOjE_uAqRT6Zyd7kzkaZbpihvkxkzv6AXDDJUbSkqbEgdkysknFFU8SUjCSaxYNv6NVeMFFhrElI2NLQS6lvWUO2ltb3zeTbvffeDEChPG_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imNUQ1kYGSA0SKBtVATgHJG1MTYlXGRgy_UNA9JiPH4dbZoiidPFLfCSNrTetNvY2buxMczWzNhXhYMrquN7BoRKIfFlb0YJ_UN57COZjDUX3hHAVJUMuViRMdru7KOQNqLXKhM0cyiFckO2UEjobOF4lbKieTcRilCS0U4ZFjcjBPKA2ipj03lgm0bS_XeF23nA-hd-we1wihlslohCYs0y5arMAKvETv2HcDImEUJSMrtNfmSNJkJCvN9Cl8W13jShfycekD--8LUh20o4JMRB7fV4QXbuEItvng6yABa-01fq4xKY0POotw4qvxUU_9IhKoXf3alrSgFmJH2pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcbYYN0YLOV3BxexkzvqL_xovLHBoPMry0FJCCBT8Rn-sgiSLIFabUlJutH6WdNGdOYBA3SIXMfoFb-kBXxK6KP9s2PFuMlWLVI_DjyU-AmGS1t_K02hv71Cs-UTF-8pmTJZzMCkndinSvoWO30O1-mleb5WoXdmWZAmbMA1pnmCmUCYCNojlxpsveravIiaPAQybfHz0kTWP7LNHtNNL7wXP-o4SXDX005t_dKhWGWH-WuhixAcBlteEPujvnlGzHzwBjNNyIrxBo3UuOFNFZppfCW3QmoImjiAv860M3Jf8SI8TTEOBzElzr4vsgrkdg46AUWL4aAWGSqCB1MI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFEvz01CSBoOnXjRAAFTdDit1wk9SSNxXKqwAhhQ9UtXeSETkwtRoFA_P6o1kVv4d7EEDXThTsLy7z9oDOXgdVVJW74KvG3LvEm7PMrKjzWhm1VWKqvjsbsRvq1uyEiC-GytP66Cxe1A8zXawoaGtyi0L89X0C7F_Iza7Yeaw6pmjDkxnlWslmye2AcyLijQeCritRmCor6V9KTYjqU_9VyZU22vlUnsobpGe2jFcmLNyZ-iJmL0OPbnQiAW8mFaytadGepU3hGEObhFRf5qRbeNr-Jyy4W_hWWmRgnB8s7CpT74gAWFSq-dIqpYwj_eh2kNScWKpowRGEtvo_84Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک جنگنده
اف ۳۵ سی ناونشین آمریکا
از
اسکادران ۳۱۴
تفنگداران دریایی، با سه نشان انهدام زیردریایی در بدنه مشاهده شده است؛
زیردریایی‌هایی باید از کلاس غدیر ایران باشند.
همچنین روی این جنگنده نشان‌های انهدام
یک نفتکش، یک ناو جنگی، یک پهپاد شاهد، یک قبضه هویتزر، دو پرتابگر موشک و سه سامانه راداری
دیده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25170" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مرد خردمند ، مارک لوین : به نظرم سخنرانی
روبیو
حال‌وهوای سخنرانی یک نامزد ریاست‌جمهوری را داشت، هرچند این بدان معنا نیست که او در این باره تصمیم قطعی گرفته باشد. این سخنرانی تفاوت آشکاری با نوع اظهارات و سخنرانی‌های ونس دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25169" target="_blank">📅 13:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFEJXaUzfcrfnEe8CW1Y8zh5n-ytrMNfOU-NdAnAVusNINCm14au-6RYeXnuUkaulLQacFpRNdi7gTDlAE4KgZ2OZAmplN9Mm3DiUcC0inf3l8rbQQm1hj6UJ7HZZKe9Qk6MQEPj0eHTf5vNyMcX-Q2m88bX_Lif4p5YjRMXKv_SxNfRDNrC-73AwTuoFHr4xkUM_wofcAc0dM5cDWTct4RGGVmehqESCpnusHxMkTjHcCopHFn8VSmslZtKcWzrwYwf11WIrt1awaHLDO2mxr-Jyp-EPANWuTiPGteJ8lhy-5ENbB7brt0WFaggOXH956kPf5eHysRX9I5Vd7PwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ مهر، «روز مهر از ماه مهر» و جشن مهرگان و پیروزی داریوش بزرگ بر گئومات مغ و آغاز شهریاری او فرخنده باد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25168" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان
روابط عمومی لشکر ۸۸ زرهی نزاجا:
ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت.
متأسفانه در این درگیری یک نفر به نام «محمدرضا اوکاتی» به شهادت رسید و ۳ نفر مجروح شدند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25167" target="_blank">📅 12:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=dEkedDKL7r-alWHCSvC2tu1u4Ka0iEUHoSaXhnDtRpan0YvcRNqEamOASr6bmuWe8ZNCAslsy5OKvJRoZI81dUdQqM1cLJnvJk2Ba2cybQ3-eoFE74fRHKabHwzcFznTBur3Gvn811NReQqKlhtU3IhDXluxyx3vQOT-OBuqiITcxZHF8orghFUMt294HSi3v6wvoXC4SbIgUqwNRVRAIS6DumglSxYImbTkMAvirJIXDXIEcMTRHdzLLW3DhSBdDHe4we-iSUCs8ghblqGqk9l1_LqC-byXYfTse0p6lIQl1BpApjWFXxXjXi2wlcNg9nuj7FtIu-4dusSdmKwKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=dEkedDKL7r-alWHCSvC2tu1u4Ka0iEUHoSaXhnDtRpan0YvcRNqEamOASr6bmuWe8ZNCAslsy5OKvJRoZI81dUdQqM1cLJnvJk2Ba2cybQ3-eoFE74fRHKabHwzcFznTBur3Gvn811NReQqKlhtU3IhDXluxyx3vQOT-OBuqiITcxZHF8orghFUMt294HSi3v6wvoXC4SbIgUqwNRVRAIS6DumglSxYImbTkMAvirJIXDXIEcMTRHdzLLW3DhSBdDHe4we-iSUCs8ghblqGqk9l1_LqC-byXYfTse0p6lIQl1BpApjWFXxXjXi2wlcNg9nuj7FtIu-4dusSdmKwKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : زنم بهم گفت یه لطفی بکن، کلمه vegan رو درست تلفظ کن!
‏من میگفتم “وِیگن”! از کجا باید بدونم چطوری تلفظ میشه؟! من استیک دوس دارم!”
@WarRoom
😂</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25166" target="_blank">📅 12:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز: ایران ماه گذشته ۲۰۰ میلیون دلار به حزب‌الله لبنان داد تا این گروه به خانواده‌های لبنانیِ آواره‌شده در جنگ با اسرائیل کمک مالی کند.حدود ۵۰ هزار خانواده که خانه‌هایشان تخریب شده یا امکان بازگشت ندارند، در اولویت قرار می‌گیرند و به هر خانواده در مرحله…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25165" target="_blank">📅 11:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز:
بیت‌کوین فقط امروز ۱.۳ درصد افت کرد و به حدود ۸۲٬۲۶۵ دلار رسید
و اتریوم نیز ۰.۸ درصد کاهش یافت. رشد دلار، بازده اوراق و قیمت نفت مهم‌ترین فشارهای کلان بر بازار رمزارزها هستند. حدود
۵۵۰ میلیون دلار معاملات اهرمی
در بازار کریپتو لیکویید شده که بخش عمده آن مربوط به معامله‌گرانی بوده که روی رشد قیمت شرط بسته بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25164" target="_blank">📅 11:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اکسیوس: پنتاگون برای احتمال ازسرگیری عملیات گسترده علیه ایران آماده می‌شود
منابع آمریکایی و اسرائیلی می‌گویند در صورت آغاز عملیات، حملات می‌تواند تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران را دربر بگیرد. این موضوع پس از نشست چندساعته تیم امنیت ملی ترامپ در کمپ‌دیوید و تماس‌های اخیر او با نتانیاهو مطرح شده است. یک مقام پنتاگون به اکسیوس گفت:
«وظیفه این وزارتخانه، توسعه گزینه‌های نظامی و ارائه آنها به رئیس‌جمهور است.»
یک مقام کاخ سفید نیز گفت ترامپ در هر زمان همه گزینه‌ها را در اختیار دارد و آمریکا به‌دلیل کنترل تنگه هرمز و وضعیت اقتصادی ایران، در موقعیت قدرتمندی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25163" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
پنتاگون به
فرماندهی مرکزی آمریکا(سنتکام)
دستور داده است آماده‌سازی‌ها برای احتمال
ازسرگیری عملیات‌های گسترده نظامی علیه ایران
را تکمیل کند.
بر اساس این گزارش، حملات ممکن است
پیش از انتخابات اسرائیل و آمریکا
آغاز شوند؛ با این حال،
دونالد ترامپ، رئیس‌جمهور آمریکا، هنوز تصمیم نهایی را اتخاذ نکرده
و
هیچ تاریخی نیز تعیین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25162" target="_blank">📅 10:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه NBC به نقل از یک مقام آمریکایی، یک مقام خاورمیانه‌ای و یک مقام ایرانی گزارش داد که
ایران و آمریکا در ماه جاری میلادی در نیویورک، از طریق میانجی‌ها درباره برنامه هسته‌ای ایران گفت‌وگو کرده‌اند.
واشنگتن می‌گوید هر توافقی باید موضوع هسته‌ای ایران را نیز شامل شود و ایران میگوید خط قرمز است و اصلا
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25161" target="_blank">📅 10:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تنش جدید اسرائیل و بریتانیا
اسرائیل در واکنش به تحریم‌های بریتانیا علیه شهرک‌های اسرائیلی در کرانه باختری، دستور تعطیلی
کنسولگری بریتانیا در شرق اورشلیم
را صادر کرد. گیدئون ساعر، وزیر خارجه اسرائیل، این اقدام را واکنشی به سیاست‌های «خصمانه» بریتانیا دانست. اد میلیبند، وزیر خارجه بریتانیا، گفت لندن حق اسرائیل برای بستن کنسولگری را به رسمیت نمی‌شناسد و بر سابقه نزدیک به ۲۰۰ ساله این نمایندگی تأکید کرد. امروز تابلوهای کنسولگری پایین آورده شد، اما یک تیم محدود بریتانیایی همچنان اجازه فعالیت در ساختمان را دارد.
سفارت بریتانیا در تل‌آویو همچنان فعال است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25160" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: ایرانی‌ها آماده‌اند هر کاری را برای ما انجام دهند تا از آنچه در حال وقوع است جلوگیری کنند، با این حال، توافق با آنها واقعاً گزینه‌ای نیست که من ترجیح بدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/25159" target="_blank">📅 10:18 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
