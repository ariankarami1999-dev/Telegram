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
<img src="https://cdn4.telesco.pe/file/koodlvyLFsB98w4LTMLm4g3MYPYW9NiNGxEE04oRSltRWCdgrxxlFQdb4czpJbu1TT4YDuPtXYJkkuMLvZdR3lThlHNMC76p-TL5Dn2LHUBMYBfdlcIZUvursf0Js7tSM_994se-ol2z_20vngoJoKs89KUMXTxLE4MHCpzFsiHcVP3VaAQgph2gbMFV36TWpNprHMz5zUCepCEjqazbfSUWZBoOjv-YuNNZqDS9fuAW5w2rFzoOWdZcfb1ZPLwR_GrZpMIf5uqZF7GQYxrICaIrURDbIBbibrrDB-rbyp5-SYslPYIrVEM_F4HTDTxqPBZ_tbeJlmYHysGOKAJFuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/139812" target="_blank">📅 17:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/139811" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/139810" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/139809" target="_blank">📅 17:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/139808" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
فوری؛ سردار آزمون پس از یک دوره غیبت به تیم ملی بازگشت و اسمش در لیست اولیه جدید تیم ملی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/139807" target="_blank">📅 16:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/139806" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/139805" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
برانکو ایوانکوویچ سرمربی سابق تیم پرسپولیس بعنوان‌مشاورفنی زلاتکو دالیچ به کادر فنی‌اش در تیم ملی امارات اضافه شد و قراردادش رو امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/139804" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139803" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/139802" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
رکورد تاریخی پرسپولیس
✔️
پرسپولیس با تفاضل گل +۹ بعد از ۶ هفته، بهترین شروع تاریخش رو ثبت کرده؛ آماری که فقط یک‌بار در لیگ سوم بازهم توسط پرسپولیس و یک‌بار هم توسط سپاهان در لیگ دوم تکرار شده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139801" target="_blank">📅 14:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
✔️
آمار جذاب پرسپولیس تارتار
✔️
گل‌های زده پرسپولیس تا هفته ششم در ۹ فصل اخیر بی سابقه‌ست که نشون دهنده هجومی بودن پرسپولیس در این فصل هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/139800" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5fRz5MJYirIkrIPrQz4K2y4kdqIK7P-T3_hSV0raTLXmaM5cdOkpE7O3wDyJazxiKaDi3oWvJIngb3NtmwDVXlicQjc2wG3Rogvm-D9Fv1AyGAwvAHbdJ1SLlvAlpNcn4lSHP3Q9oSuP7H5kegi-VsSr5rtkm9KOBu3tUILIkaG_7gxNapsCGYyuyXLJjnTjASrYbwRlkdKCWHKlhgjick_pl65BbOAGWHeMToPERWY9WBYFZmH3kjBzhHfXKi7esdobKQQ7qMWXjnoaa38YxjBdBUIr1iTO8KHu6ask6PhZ7cERL5F0CuljdzNydJqcgNQHnqMYaQ8hERrB1ANLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دومین شبِ جنون اروپایی
چمپیونزلیگ دوباره با نبردهای بزرگ برمی‌گردد!
⚽️
شب دوم لیگ قهرمانان با چند تقابل جذاب دنبال می‌شود؛ بارسلونا در خانه به دنبال شروعی مقتدرانه مقابل فاینورد است، در حالی که پاری‌سن‌ژرمن با توجه به برتری کیفی ترکیبش شانس بالایی برای کسب برد دارد. در حساس‌ترین بازی‌ها، ناپولی و آرسنال می‌توانند یک نبرد تاکتیکی و نزدیک داشته باشند و لیورپول مقابل اتلتیکو مادرید احتمالاً با بازی فیزیکی و کم‌فضایی روبه‌رو خواهد شد. اسپورتینگ و گالاتاسرای هم می‌توانند یکی از بازی‌های پرتحرک شب را رقم بزنند؛ در مجموع انتظار می‌رود چند دیدار امشب تا دقایق پایانی کاملاً باز و غیرقابل پیش‌بینی باقی بمانند.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/139799" target="_blank">📅 14:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZTrUiu_36TOTMYAfLRY_rSe0LAgduJgN7sDAieg1ATGlu8Meeneyz0ZW3Oy3S9wdQdoZA7jlZ3Qw6E3z9vZSkN47jygZmXMF41Ct5DS8j6j0PBas-2xo9py61Tf6GpTgsUJlkbMQh4fu7-_jLdMkUKxabW-xPvhK4xAhFYWvf8Cw5Eaj9ClDBkgqmx6PhzexxkcdiHFhO_da5reOyFxUNDkVuY2I6z8a0MA8PU9Lt0ZLS-kSC5Rme_v78-h-oNCMvIOudkRcJOknS3IwveYXm08mOORpRIb7Xt4Wx8RVtOdM2N1hhvKzXkabgJssxy7Z80h-ZYCEnpYpGqaYTA64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
فوووری از یاشار سلطانی
🔄
🔄
در پرونده فساد فوتبال برای تعدادی از مدیران ارشد و چهره های فدراسیون کیفر خواست صادر شده
🗣
🗣
مهدی تاج ، محمد مهدی نبی ، احسان اصولی ، تهمورث حیدی و خداداد افشاریان افراد مطرحی که کیفر خواست علیه آنان صادر شده و طبق قانون از حضور و فعالیت در فدراسیون و کار به طور موقت محروم می‌شوند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/139798" target="_blank">📅 12:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj2O0ospMOdefW_3oF-0jOb9Xm7EaBzU5Okoakgg0pfkI51atxgdO0Mce-gLli6If1niykf0kODhgXYnUE33CR0aGHBM-YqRCI5fYTtZGI-KsZ7WPKMymiJaRcb1g0SV1_IPaEkIW3N2KQrFXsO0GASSo2LQbumdv7VLpXbN6srys5I6d9PO_dofiUfOBvcq4bkZULkDcCU_Nray_7I_AFvNpB9HcREaV-CKriOjLoA3py0ptI2yMHhiwAlnfDsk5wfIJlnt_Kkkfo0zLSe3a_hQSSmIznLB68GQGlJvSMQ2RM1oNLZi_mXzNKbLtS423kxQs5ctNzlMt2Rz1naLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته می‌شود که باشگاه پرسپولیس تمایل دارد قرارداد علی علیپور و حسین کنعانی دو کاپیتان تیم را برای یک فصل دیگر تمدید کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139797" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139796" target="_blank">📅 10:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139795" target="_blank">📅 10:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
دکتر حقیقت: ما کارمونو بلدیم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139794" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=UQvFjPy6PWQVx2YDRGkM84y8ZuiDnaf_pch62Aiw5idQbl4GIToUJikPreQxJe8EnXli2_QEmDgnuAdRn3W1fDbvQOEyzULD_BRq8lHhP7MqisvgZ3lewqd67zuTl3h7o1rhbDCmja8TpmJ3WOg4XwTyfD2n146-hBqtKQmEXOXRSGm8CYKAMvzHBYAw1qEpt189NTgEP_mHMhze7mcRJqURl4XR9ulO-fX4bLIwWexpdG4yJ98vY1JPu8TxmprwCChOdmF8haYJ1sR_bu1rYw2odkC4gn2wNlrhNB-_B5m5NEJTvFqMhrjC6kNhqiZy3fOANMpUPVo9RfhlDNz5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=UQvFjPy6PWQVx2YDRGkM84y8ZuiDnaf_pch62Aiw5idQbl4GIToUJikPreQxJe8EnXli2_QEmDgnuAdRn3W1fDbvQOEyzULD_BRq8lHhP7MqisvgZ3lewqd67zuTl3h7o1rhbDCmja8TpmJ3WOg4XwTyfD2n146-hBqtKQmEXOXRSGm8CYKAMvzHBYAw1qEpt189NTgEP_mHMhze7mcRJqURl4XR9ulO-fX4bLIwWexpdG4yJ98vY1JPu8TxmprwCChOdmF8haYJ1sR_bu1rYw2odkC4gn2wNlrhNB-_B5m5NEJTvFqMhrjC6kNhqiZy3fOANMpUPVo9RfhlDNz5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔴
دو گل پارس جنوبی به پرسپولیس در دیدار تدارکاتی دیروز.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139793" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139792" target="_blank">📅 09:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR-AajLv4TppZ6DmY--0udn0SxkohvLGCLyOnBUJQX_TKFS1gcP9hGjkaNKuP-CHEF-ZxIe1HBPAmC6whCg8-CxgW4Q3JNBPEH_Be3mLAqIt-ArdMK0Djro4XaJ_DcmZmf4Oq_c-7Vlw64wqEKN6bs7xygDRoAAGivCPRPpoS3wrIaylKX5E8u-HFZYNMOm0vuELDYah7G-tAMTeFom39cSlKfVakK6WHq4Aqo5WrPyoAa4HhMnvFRLR2wcQytugLR75x8ucy9LBXA6wFlK-qisYmbzql4N1hmfQoBM0z_gpeUfysGxo7_zEBvOunv_J4C8n1k_Ofd-en6Rvfil89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبرد قدرت و تکنیک؛ در یواس اوپن
🎾
Ben Shelton -
🎾
Alcaraz
🎾
آلکاراز از نظر کیفیت رالی، تنوع ضربات و توانایی تغییر ریتم برتری محسوسی دارد؛ در مقابل، شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند فشار زیادی ایجاد کند. اگر آلکاراز روی سرویس شلتون موقعیت بریک بسازد و وارد رالی‌های طولانی شود، کنترل بازی بیشتر در اختیار او خواهد بود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139791" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139790">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
زارع: جلوی خیبر نیستم ولی تلاش می‌کنم بازی بعدی باشم  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139790" target="_blank">📅 00:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
زارع : حالم خوبه به زودی برمیگردم،  نفهمیدم چیشد پام به شیار های حموم گیر کرد و بغل پام پاره شد و بخیه خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139789" target="_blank">📅 00:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139788" target="_blank">📅 00:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139787" target="_blank">📅 23:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
شرط سنگین گرا برای جدایی از پرسپولیس
✔️
✔️
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از این بازیکن در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
✔️
✔️
دراین‌بین گرا برای جدایی از پرسپولیس خواهان دریافت…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139786" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
بازی رئال مادرید و اینتر هم شروع شده که رئال  دو گل زده تو سی دقیقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139785" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139784" target="_blank">📅 22:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZQJDDnjuQB04plP0odeqRiljOZ3oFz0X2ocsyrLAk2Oh2iHPWe_gsMyJtINXdC6EIyz2LCJ_L_2qkB2Zsk5R7sWv2PTmF_O52foAJTvrBcSiyBADVtAS7FFsxQunhgBJKhHeFg-OVPOYe5DekaWsux8tLS5O1CQOs4FcBdqEHzIYY_rWF9PS0BgAqKhariRa4mFp0edbjYAP0qeFsTYfdH4lLKNvt8lIjJt8WGULbUVwYolYGC1IZDOEXHD3geCWg9D1P2Kyedk2_kbhxSf7Cntue4RBsXY_ZBLDITDFcPNoCWxWMdcrQN8sjTIhQ-Hs6JmfmGa6pQ53hRtx8Y-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139783" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_1SkOra32L3TwXM-7H_zo1dNbUN99_LVYMV9vT8SzQBx6FLdDVsIRxns-dylOBx_ZPeqlx8wgvxa529iOU2BOINC8lVutIcCq8CeMOXyaHEg-5GGpUl5G_wCDN0J6vPM9ESMjc5Wk8ujL8xywvj8cuKNJaPGXKDZWJbwf5gRoM6NOgGYXiVfVTEANCz-i2OrIpDUvt2qivMkJHeAH5T5oor0uzK2HMOBcaOJ9IeV5ka1HnYoRSkajeIxgmgPzSp_qHqjMOw_o11F0dTICIann5mDUXskB3jSUAMPkEnwAKgBtzYhYYUY3mOsZUmmcwsOr9IfFRpTFaeTCn7QDyYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139782" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
فووووووری
🔄
با اعلام سازمان لیگ؛ فصل گذشته هیچ  قهرمانی نداشت و یه موز به استقلال رسید
😅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139781" target="_blank">📅 22:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: پارگی نسبت بزرگ بود اما سعی میکنیم به بازی خیبر برسد حالش هم عالی بود تقریبا بیست دقیقه پیش مرخص شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139780" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139779" target="_blank">📅 21:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqzyD20TjDifE9hACRlcN_ezb3xGiCuVbrvMuVNn7zzayQeqUNzQTqZ6NI0NsIEbRiQwtn-U2N-bnsQGPJ6c7i1vWfy-o__0M-_867VpCGK2K90WM6IKDi3SapaU2_emi_YNyfaOm1zBkTTxkx2Yi_vgm1oeD9bBcR12MPRKX57bjO11OC58dIvQZFD52mcqPam9qH1crbWxYlRY_R6l3nNRtjJX3uC8ZmmThO1PIpjM_LHuf59kEooqQd7Hu778rqov8LFhp5whD91BUXNPlL-GgnWyMVTrw0L-6ozWcjxmFoCF47hYjhag67FelvVo7pWxUQA8W8yqNW8M1bEpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
💢
پاسپورت ۱۲ پرسپولیسی دریافت شد
💢
پاسپورت ۱۲ بازیکن پرسپولیس برای انجام امور مربوط به تیم ملی دریافت شده. نیازمند، کنعانی‌زادگان، ایری، زارع، لطیفی‌فر، محبی، علی علیپور و محمودی، هشت بازیکنی هستند که نام آنها در میان نفرات موردنظر قرار دارد.
💢
همچنین احتمال حضور محمد خدابنده‌لو و مهدی تیکدری در این جمع مطرح است، اما نام دو بازیکن دیگر هنوز مشخص نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139778" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139777" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139776">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139776" target="_blank">📅 21:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acWNX29u4trm79IsWi3qDl2JagXQODWvYSNOC4Cfc7I-KA_ybF58a6lyttuW1bn_4g8VpMyjsQhWbDIV7UgS9f-sjuICdaOMWtOMotdcU7KJiEtfYTruu-8PrEV2HDMuL8mrjbf-peWjy69GVEoQpYBHMP3jQ1CelFbij8YscSwQ_3LdJ-ARrqUiRXq9Iyb5n8LB1wUGBe41L_Zf2lvj8sVxIUYUJfzwOoI2_2AzpJLEg_D53s8zRV_5RyNkTY70LMkng9ZPMKe-goa9PPze5ttkcvGxswB06_bvUXYv0IVy1qtHQ_O1SilFB7MP7YWAXD4QgY_PFNtfiYy5p2Rh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تارتار به ابرقویی آماده باش داده تا با تمرکز و آمادگی لازم برای بازی با خیبرخرم آباد آماده بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139775" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFYnWkcURelLpB3vGAdRSnDL5M2ySUGUEEMteSSiYBr4bINUkDCbgMBsRFIPbNpddiT9IliPt7hu2j999r4gqXf-xru8Wgrp8RdFEcIQrZ9D95mwU3Yp-86eV3ufN7mAi-evycNMQV08dtzZa3h3eMQ9VZ4OIiv1UKI_au9a3xPn0bJfnhl-uNW2qJx9dHDlGmIpS_Qgprb9AMdNl1TyRZPSELe798oDSEyn6KreG_xfLke2_mA-JTpKVqbgPH-uiO3N2dxTMvcQOkBIuWCicD9feqkmDelABSRvMncoWqkK5SfDr-BchJ12gz9xguS_vSoc7x75_ZjPRpn3Utp1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و فرصت‌دادن دوباره به پوریا، شاهد درخشش دوباره این بازیکن باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139774" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAcQhwCMkN5f7TcUlm_XuRpJyYi0JPSjkRmSX1pnD0v1ypiqQ6ljTgZ0XHyv61Ly3kHet4EdKQVxZjT4CN9d4DqeXtJce8THD0eUJ7plPsV0sSi1ruC22Q760s2d0LiNAkpF-CP5ZkRtK5fqOeJPvwE60rMd6iygesmMqUFO2Z24_rAV7-J0WvrvclvYDzaXzGwk-I8Kp_A0QgpB5w20PGXbg0VLXx_ZU98IOQDW2c1vkZnwDtjlyruqVgO1ArwxznEUVHYgpI8pnRLI99q-JhLt45epVNZPHH_1sn0dLxKOrAc9Wkc95GdqP9KnKTIQsg-uGnpw73msOPaPQmiaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری بازی دوستانه پرسپولیس - پارس جنوبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139773" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
با توجه به مصدومیت محمدمهدی زارع و غیبت احتمالی او در بازی بعدی، ممکن است پرسپولیس با حضور دانیال ایری در تیم ملی امید مخالفت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139772" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTouPIDFeJspjSfM4X3pmT6uFutqoyr8wZIBuXVoJoKLfqB-cLSIJx5I7JB4wMdask9qgaVP2Vd4QWMsqukKyZK12SQTsIGIQDlHuNyOg_C2lXcWjTvn--4eE0qbX69Mm401WZbdrcByQgtLVJHocEu3aM_ab9dH1Ixl5whmGLP9Rlu9AR3aaTAv6eT49givNXXFkF0sVw_va4dklTnILxX1Nb1F0iw2w2Im0BewVnds-P2x6i28nZUjU5l5kXaioAtptkI55udMMVGqgPURQ8lhCfl5czI2Wd6_zXP6wd3ouhHpWAmKhl4E_BB3G3QK4rgD_fn-eDnujDMzi1002A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شب‌های باشکوه اروپا در راه است!
جایی که رویاها، ستاره‌ها و جاه‌طلبی‌ها
برای فتح بزرگ‌ترین جام قاره به هم می‌رسند
.
⚪️
RealMadrid -
🔵
Inter
⏰
Tonight 22:30
🏟
Bernabèu
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
⚽️
برنابئو در انتظار یک شبِ کهکشانی
رئال و اینتر؛ کدام تیم پیروز خواهد بود؟
فرصت رو از دست نده و همین حالا وارد وینکوبت شو و پیش‌بینی خودتو ثبت کن.
🔗
لینک بدون فیلتر وینکوبت:
👇
🟣
wngd3co.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139771" target="_blank">📅 20:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139770" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139769" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139768" target="_blank">📅 19:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤥
🤥
دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139767" target="_blank">📅 18:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
بازیکنان دعوت شده به اردو  تیم ملی بزرگسالان از نگاه ورزش سه
✔️
پیام نیازمند
✔️
محمدمهدی زارع
✔️
محمدحسین کنعانی زادگان
✔️
مهدی تیکدری
✔️
محمد خدابنده لو
✔️
محمدمهدی محبی
✔️
علی علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139766" target="_blank">📅 18:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139765" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUl4TqMyVxu8MF92cwyqlqpvZiOYBu_IsEDodKr2rAoAroUWSTRgt5e4UiFHYVaQtxdafqXdRwPX_EncDijOhruWkr8Anvv3Mk5HwAWgtkDx4vVQmDwwzar8C7IBI-S6qDtjanTWD-2aEdKVkJ2vbURJt0rPYIuIIpA20arRGpF6ACQdN8UMvRbI_zXKppXbvW0acwR0qkzWXMfrYdzgsqng3TQUDAlxqvmMcPA0dATrrJB9WaLJ8FJrW9VmPN3NZ8cCRi-be52e-gIalDVLwiy7pTAx8YyknwSfvLnpeLC7CvKC9bdWwtLUyMnL7CgzcXv1NpBACtCaH_x5GaAO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139764" target="_blank">📅 15:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMjbA3Fy_NYh4UUGiOQT0zRBIZBkfYoVes2s8wNvyYDg-3-gwwG2oN7uAqErhMIPoXM3hZaD3BwYNbJZISFzTrebBcyOIPmk-X10H0nSOHSee4co-U2l5uMddOOcRKnjCs7KBMF6yJR1ET60_stLKDNyuj_jqUHQI-f7ITcbalV0ts-YZs2ym98_gcpQcxiBfZzKhDvq4SC4iP8ZdvbcWF6lqcg8mDVdnVGkil-4lN4rjwdlYpsHhxWCKcMQ4Ou9JNdjlEEYWLyLkSmVPTj28ej3Fm5ty1q4OsE2GKw7fawzvy-RFVko0zP7jI77Lp6DrOH3zds1JYb9Nv-CSARJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139763" target="_blank">📅 15:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhvufKweHezBQmUP4C5e4Abk6pOqjr4nlFTTmyrR1Q95sdwrnyTP5tXYF1xk1qQ_3Ne5D4tKlMgeBZgQuGygu20VJ1SVXQTJDDc6Hg-gyPGvdKpK8hU_akg8yAENSLQIZiLGds5IITRs_ZshsnX6gJZ9-wSeKla9jPDqwZtKQPbxiujmjRuFN2rKqbVA__Kjolhf0uadDvatFxc7eub84cDPoHYJ-RS0GwmG0amaYxT3dvzSC8pY0ez_wCFl9Ve1wBpueZc5C6IByeuX2Fj-jlQ9Apq94rdM3YVovptA4U9hc5w3R7VChnTpz03AUt-Xnu8RvxOAzUUn_vXdsZNkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🔴
میرور: فوتبال سرژ اوریه به پایین ترین سطح کریرش رسیده و می‌خواد در لیگ دسته هفتم فرانسه در تیم محلاتی مونتینی-آن-گوئله بازی کنه و انتقال اوریه به دلیل تاخیر در ارائه مدارک از سوی فدراسیون فوتبال ایران به تعویق افتاده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139761" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139760" target="_blank">📅 14:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139759">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139759" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❤️
❤️
بیفوما که به تیم ملی کنگو دعوت شده بود دعوتو رد کرده و گفته تیم ملی من پرسپولیسه و به تیم ملی نمی‌رم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139758" target="_blank">📅 13:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139757" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2FsqLXzCjyKrziXD8WC5ehB5dbhWb93LZDepPD4asL2eH_lk60Nx4bbQsh_2YOZV8nxjngogaTRbeyOg8vvH_p7JDT_btAUYXFkYdfIp-BYtWp_Z0a57s8oY9snDseqpMEu51_e3JezIcrdFjVTnWceIRKi81FPtayUUFl-0OIwGJRkl9ezAfnMEW_xjaQarZjtysfPL8tDay9Yvv-c7ejewMypmAKfQsmBLpMxiGjRpn7OzuYPfmg34nwogNVxwah1hey-5NOg5n59PVMQUeVgj_USFNbm1jfUo2GXITlR5gTHjtG1SyfnWpZs9oVDez6U9ZDjwtivwLBIS11JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئال و اینتر؛ دو غول، برای یک شب بزرگ
⚽️
رئال با تجربه و کیفیت فردی بالاتر، اما اینتر با دفاع منسجم و ضدحملات خطرناک؛ دوئلی که می‌تواند تا آخرین دقیقه نزدیک بماند.
[
رئال‌مادرید
⚪️
🆚
🔵
اینترمیلان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139756" target="_blank">📅 12:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139755" target="_blank">📅 12:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139754" target="_blank">📅 11:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139753" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdaDWDkoWrtkcDRe7oFazJn8g222IV20rHI_YChOg7Ko1FEWMLSC4Vr2aqtwf7KFisg8odEIf9W0cpqar8jajg-9eVcvJoem6x7aIDSZ3JqkVNzO7ngeUPMkuphlFMUeLD4EYr2wbHwAD8cuVHCssXdeGgIgKUIlDa7NwVVxkOrGkdCW7ZDWnES_q8oOOngR-XbuPLluycl6BHXVFF_2mCvWPUepvDPhdxsACYVJPOHqqR7_sTPh_p8zW0ZwTOzObGLX_hhtN3piUfh0QakVQtj9NQnnWVzd_cxmM4c0I8d70fVlo1y_SYdiUSGjWfDo8eY4FBJ1SsPir15-MlSJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ایری در پاسخ به یک هوادار: تا روزی که جبران نکنم، شرمنده شما هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139752" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139751" target="_blank">📅 09:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139750" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg0XNzXCaeZKHwXwpnRd9zvDCu0NBKDxq1ONCkNZ3BH3_vR5cCmpeA9hH14QYaGJ5K-7msAip05a5I43dRSmJN6pGFrp7SS-gHXXoXebdeS9Qotne8fkDPx-RBncwVitAMQA8-6C3NWnFJl42rQqgG8Ucnds82bk1fAHv1rHOGHl3I7-fHfpJU8KOSjoNYQ6-TihUbA42G_uvFO00iur7aeqOXp7I3l12uljo-vJR9lSmOnHdF2yIY_lGHOdy9kmk2y0jQwc4oqw7rR9SznI42220kptyr5i8bHdF5n-dZqAw7VQRIrptDfMpWOqtFQ4jyCFDdL7ASL76mIkNLT7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139749" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و اومدیم دوم جدول و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139748" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_tPgLiB17W-3WYcHvsVwpROY8hZ4sB5jTvw-Q9wGS3ENvFtei-oYoHqKmtFFPxNVH5bebRj8rxJrLz5LHUpp8fs5RM_7B-y_rFGOgiq-qVJtS_CK5sEFr3RmYCtWvF9by8ZGyLp-JKM5wOWqRf26kHUCno4EwRBCrwstBhPngpF7ZwFCc4w9ABKThwx_jmglXLXewovzk_efKqICQew0pn8NuCg-aDRV2djwpC6xZ870m0lNagDvxjvC2uSWlECbW5wrebcV5c5R-JnrNir9yOKo6SaqpG6HNmA-5yl8eYlR2cZIo_1rI_ckq2TbH-pSIAd5aeeVAea_fMzDWGTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال جذاب در یواس اوپن
🔥
[
الکساندر زورف
🆚
لوسیانو داردری
]
⏰
بامداد سه‌شنبه ساعت
۰۳:۴۰
🎾
زورف با سرویس قدرتمند و تجربه بیشتر، شانس اول پیروزی است.
داردری با سبک جنگنده خود اگر ریتم بگیرد، می‌تواند زورف را به دردسر بیندازد.
با این حال، روی هاردکورت کفه ترازو همچنان به سود زورف است.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139747" target="_blank">📅 01:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
پیراهن پرسپولیس را بپوشید و به تیم ملی برگردید
✔️
در دو سال اخیر گولسیانی ، گندوز ، باکیچ و بیفوما از پرسپولیس به تیم های ملی خود راه یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139746" target="_blank">📅 01:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139745" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139744" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=cg_d75hHt586YQflta5ZdHAy2FpExLPlbAgMsAtqFdWDU3kZXl3q1NDgJQo9DhoyKYDZChGDPCYZJCNTEtQQEKqOYX5nV9XW6dBIEYt1X-9nHRBLnDFrz-WlRGXsO1T_Mfp0xi59TFuPFcJrpLuHnrX296xaQIDboda39Xe7-D7bVaXKmstAGHObEjKeXz_4KHatlPY2gNCs62tv7u6Vw_90quuWaRw3wipjlmYgENTGS-zjkmubWcfhGHuscUVZAAcHw1incxoHXjH9gOjrWMFCob2hoZNAbrcb5DBFR-oLhoTC3T9l2HMKLbwT4iLyaPn18Y78tfTwHlZFHmN8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=cg_d75hHt586YQflta5ZdHAy2FpExLPlbAgMsAtqFdWDU3kZXl3q1NDgJQo9DhoyKYDZChGDPCYZJCNTEtQQEKqOYX5nV9XW6dBIEYt1X-9nHRBLnDFrz-WlRGXsO1T_Mfp0xi59TFuPFcJrpLuHnrX296xaQIDboda39Xe7-D7bVaXKmstAGHObEjKeXz_4KHatlPY2gNCs62tv7u6Vw_90quuWaRw3wipjlmYgENTGS-zjkmubWcfhGHuscUVZAAcHw1incxoHXjH9gOjrWMFCob2hoZNAbrcb5DBFR-oLhoTC3T9l2HMKLbwT4iLyaPn18Y78tfTwHlZFHmN8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139743" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=uBkEmoPRB1TAOS1hkfaRXBlhZO7AnAFY46sIHiAGYBmTlqfCDF2p4pC-Camo2H74oeDf5LfUQKqUk3qq-0P4BCVTvODJmH4XphuT1nxdRFfoDP8tSNfZ0C-RMtI61U0dufzUJyY3znZRLtz3bTDUefjRrArZdUj4Q52iP7LOvndu-S8CWzf28ESQGqwzNvRMlpcKnmhefR8H26ZruwzFp1qRxqnjGVBo8nHi3XEe1P7F92bugUkEsWmQAMW1-Ad22i1mi7aW62j9PdUDnO-izf3Bkmn3kDjDQ8-CI2xI1vONGXBRHGIQnpbf8uCxUwr-c392qxJUKlALMyL_qMmF-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=uBkEmoPRB1TAOS1hkfaRXBlhZO7AnAFY46sIHiAGYBmTlqfCDF2p4pC-Camo2H74oeDf5LfUQKqUk3qq-0P4BCVTvODJmH4XphuT1nxdRFfoDP8tSNfZ0C-RMtI61U0dufzUJyY3znZRLtz3bTDUefjRrArZdUj4Q52iP7LOvndu-S8CWzf28ESQGqwzNvRMlpcKnmhefR8H26ZruwzFp1qRxqnjGVBo8nHi3XEe1P7F92bugUkEsWmQAMW1-Ad22i1mi7aW62j9PdUDnO-izf3Bkmn3kDjDQ8-CI2xI1vONGXBRHGIQnpbf8uCxUwr-c392qxJUKlALMyL_qMmF-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
حجت موتوری: ویس های فحاشی خداداد را دوستان اول دادند به شبکه های معاند، اول آنها پخش کردند
🤣
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139742" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139741" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139740" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=JGX89wuYnGMGPRvvS7fFM4mx1PpFzBwmuM9JGG432tWstaqFBYQu80EE1Pfj33ByYRuncZSufe9-JCUfA48Cics8wzJLVYVUsgfBiKiAd1YGTIqqJ8bUdnunLxyYRFkM3Xe3aQtLSnd4xhZ74hixWzWluRHznmod0nk5RhiUp_jNBYK6x0JRdfKNyO5Nw09xpwSkbeMLvLIsIh1QuAi7T-7PMFedZwSy7fohqc7q45IW5l3QYE591wH7-6zH1imFOfyc4t4G0QIhoYo0Dgh2nvovBmtDHwCYmC-tvvERjxNeCO59w1vwvuum-xD4er4asOjtcCigrzM4ly9oTNFS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=JGX89wuYnGMGPRvvS7fFM4mx1PpFzBwmuM9JGG432tWstaqFBYQu80EE1Pfj33ByYRuncZSufe9-JCUfA48Cics8wzJLVYVUsgfBiKiAd1YGTIqqJ8bUdnunLxyYRFkM3Xe3aQtLSnd4xhZ74hixWzWluRHznmod0nk5RhiUp_jNBYK6x0JRdfKNyO5Nw09xpwSkbeMLvLIsIh1QuAi7T-7PMFedZwSy7fohqc7q45IW5l3QYE591wH7-6zH1imFOfyc4t4G0QIhoYo0Dgh2nvovBmtDHwCYmC-tvvERjxNeCO59w1vwvuum-xD4er4asOjtcCigrzM4ly9oTNFS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139739" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
تارتار سرمربی پرسولیس: هوادار دوست دارد تیمش هجومی بازی کند/ قبلا هم گفتم اینجا پرسپولیس است و هواداران بازی زیبا و هجومی را دوست دارند
✔️
✔️
واقعا یک تیم کامل داریم و بازیکنان دارند روز به روز بهتر می شوند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139738" target="_blank">📅 23:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139737" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139736" target="_blank">📅 23:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139735" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVoRrnAww7dfvn4ZGHAa3BaItInBaRoFm0jcNNP0XYeCTTU6IHTScEhekoWUPs1uqHTitbwXPitkoFNZhhZaaLsQcFmlq4LbHjBfXy_iiGXBfKpMpU44okblK9dhBnrMFPpoCnHRxZ0ue-ZHpgCrnQZstwF0E_60r28odIOQ9dN4zt7IMRJSjWDnQDQyejPmoS6oJlN5zsf-CvwrlcUSGzR-nirglCsOD6zrl_n8wHVOAzBBr9iCpw43SMvKqLJb26_z7VUUsbgGbXC8D1MOQhYwEaxxTDXEnm62blnQyhFSwne2BXeMLfBzZaDXI4OJ818fW-JVfn2ximzO6Mv-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/139734" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_byLmdjxCeo_uICD2jChA-VUVPBg6X8ehWXiAE1Z8YNSuXr8erVrFgUJ5tDXMzhBGUlSJbZJ7xLp6-iDUnMmVmfSM5T8jJgLw-3A5eCFfZ_uGBfw0P-RmmKSRwZWWLJRko8eZVKWht-LQpX-xqhObOI-ttdAC3xAYuQP33W9MLoc6EAEGw4GSKNjkFNj_-gU0DphbIUAgZeasyhhCET2Azt5Fjrp-MWTn3ooppAg-0eeig6O6-1rkIc8JC7y81GRMiF8Xbft5Kx8H0PFJXtBsDJfo1mqjVdNFSTUMrS86rdIG3Oa4s4vd0LSbjUp5LHiDXCmx4qagluDbZTHG4OFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج هفته ششم و جدول لیگ برتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139733" target="_blank">📅 22:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139732" target="_blank">📅 22:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139731" target="_blank">📅 22:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139730" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139729" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
تارتار: فشارها علیه پرسپولیس؟ هواداران ما امسال اتحاد خوبی دارند و تا زمانی که این اتحاد باشد ما آسیب نمی‌بینیم
✔️
✔️
کری‌خوانی نماینده‌های تبریز؟ فوتبال از سیاست جدا هست و درباره فوتبال، فوتبالی‌ها باید نظر بدهند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139728" target="_blank">📅 21:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
تارتار: در روزی که خوب نبودیم بردیم
❌
❌
سرمربی پرسپولیس در روزی که خیلی خوب نبودیم اما بازی را با پیروزی پشت سرگذاشتیم/ چمن ورزشگاه شهر قدس خیلی خوب نبود امیدوارم این چمن را درست کنند چون امروز واقعا خوب نبود
❌
❌
واقعا جای سوال دارد که چرا کیفیت چمن افت کرده…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139727" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
کنایه حدادی به خداداد عزیزی : در این خصوص نمی توانم حرف بزنم اما فقط به آقای خلیلی جنگجوی و با ادب خودمان خسته نباشید می گویم. این نتایجی که می گیریم او هم تاثیر گذار است و در کنار خط در نهایت ادب با جنگندگی حق تیم را پیگیری می کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139726" target="_blank">📅 21:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139725" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🤩
دکتر پیمان حدادی، مدیرعامل پرسپولیس:
❌
امیدواریم روند پیروزی‌ها ادامه‌دار باشد. طبیعی است که از بزرگ‌ترین و پرافتخارترین تیم ایران، انتظارات بالایی وجود داشته باشد.
❌
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139723" target="_blank">📅 21:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139722" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=SXQ2cBfebOx_V4TfILqACvQh2vh81MOJOL0BSjIXJyaXZkZVBTQMErGecFshcq5mgjHyj07uhcl_FZubC49HjlXeowuH08cDb8l2qxMlmLXK51MXDdafYMagPN1_-N0zYTDB93RaTuGqsTGXGLFFY_p34QuQbQBqI0cCJj_PDHmHCv3Wb2CwVd3N8Qv21zuYO1UK-3zirzla-Sn9VygNAXS57OI3tOFAPSkexW3WPYGSrVOp9k39BvTMRc7PXbyeFDOynrAvBdm5yN4lsJAUpn7e3lmb3FnJyZn5xKjyJupChrgh1RCZPe4rYzxY5dWnNgNJrdIIGyN3u_orp9Vctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=SXQ2cBfebOx_V4TfILqACvQh2vh81MOJOL0BSjIXJyaXZkZVBTQMErGecFshcq5mgjHyj07uhcl_FZubC49HjlXeowuH08cDb8l2qxMlmLXK51MXDdafYMagPN1_-N0zYTDB93RaTuGqsTGXGLFFY_p34QuQbQBqI0cCJj_PDHmHCv3Wb2CwVd3N8Qv21zuYO1UK-3zirzla-Sn9VygNAXS57OI3tOFAPSkexW3WPYGSrVOp9k39BvTMRc7PXbyeFDOynrAvBdm5yN4lsJAUpn7e3lmb3FnJyZn5xKjyJupChrgh1RCZPe4rYzxY5dWnNgNJrdIIGyN3u_orp9Vctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
واکنش جالب هوادار تیم به عملکرد پرسپولیس: بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل میزنیم 3 تا به رئال!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139721" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=h5gZq8ka8Z5SXf27G-mow6bGiDWlukKMfXOEeiGqHFLBZF_3tKs9SC69Hb-AchbLQ9j-ismgLryG0YnjuYmWcxo0nurl-kqANCEigqcRKuUJvymvIcsBf8N4lRbn7FsKtpIjXm4WpKErSWX740H6Qxie--c5LMuqUsCC_vx8GS7GRjV02NcbxA-ezervN79GKtL1ieqVI0hctsrrKb04nBNCABNLHMwLJZPIhDM92hoFKEshCdog7Ski_nQetG-hgo8fdwacJ2x-qeJewP0PPo68pXcAPzWvqe6w9ZX2idBKqCR7yy35FKPlrmKE4i87bNDodiBxRTzuEohisddE3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=h5gZq8ka8Z5SXf27G-mow6bGiDWlukKMfXOEeiGqHFLBZF_3tKs9SC69Hb-AchbLQ9j-ismgLryG0YnjuYmWcxo0nurl-kqANCEigqcRKuUJvymvIcsBf8N4lRbn7FsKtpIjXm4WpKErSWX740H6Qxie--c5LMuqUsCC_vx8GS7GRjV02NcbxA-ezervN79GKtL1ieqVI0hctsrrKb04nBNCABNLHMwLJZPIhDM92hoFKEshCdog7Ski_nQetG-hgo8fdwacJ2x-qeJewP0PPo68pXcAPzWvqe6w9ZX2idBKqCR7yy35FKPlrmKE4i87bNDodiBxRTzuEohisddE3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139720" target="_blank">📅 21:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSXlZlz3JQYwi6AC1vpt_bD46XbTyWVLbaQHBdIhL5cbJ-ELVhVetCzOrGtsz3vrwijuiLrbgcB94ZQdCM132tXG65MeNUaWKVCrv7qDcjX9-TUwQ3SAWOulMP-Dq0MTR43fsZWABNTPq-7orvHARAqG7JM8xZrdEptmmBu1Te0nX2GBXq7B8dSKWG2R4NW2UXLpU5aF2FPW5VplWSytk0NEQa-MbU4HM5W7gASltHuXCEiyj28vU33efVEGC2THdbfFkUj2bO2w8v2A6KgdeeiEf9-in6AGK3HuQMwwWxRGFpzAjTCb0vgJpgLYysopZn26Cmrk70ndX2OT1RtE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
علیپور تاثیرگذارترین بازیکن کل لیگ تا هفته ششم
✔️
6 بازی، 3 گل، 3 پاس گل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139719" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139718" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=qggAEOUYOGN8w0klEbqoQ846qYxTMywYT91pcZ9pVKg65fd7bovtw5q5oB8IEmfC21fjbr_3j57xFU3UgaIFLiAVfT-qKt6ZBdN0CReBkuVUNACennLgKJ7jQWG5v1lp4ahX2mqdQS-586Li-7O7aKe4a14Y1288C8MD6Zm6-HHd9ft3HteapjTegnTP9jd1eKTzu0LDVFZvugnbz6MD2fhA05O8wTncn5JBT42egDWIs1czOJN3VrZRCT0QyA4Aqc3JG4eh2anhyGwowxk_02mSyowAJd_jxJ4zOpq84urdUxfc2tUShLDBGhBNio1GLZtZ_VelbDgeQw9gemfAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=qggAEOUYOGN8w0klEbqoQ846qYxTMywYT91pcZ9pVKg65fd7bovtw5q5oB8IEmfC21fjbr_3j57xFU3UgaIFLiAVfT-qKt6ZBdN0CReBkuVUNACennLgKJ7jQWG5v1lp4ahX2mqdQS-586Li-7O7aKe4a14Y1288C8MD6Zm6-HHd9ft3HteapjTegnTP9jd1eKTzu0LDVFZvugnbz6MD2fhA05O8wTncn5JBT42egDWIs1czOJN3VrZRCT0QyA4Aqc3JG4eh2anhyGwowxk_02mSyowAJd_jxJ4zOpq84urdUxfc2tUShLDBGhBNio1GLZtZ_VelbDgeQw9gemfAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139717" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139716" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139715" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
گل اول و توسط علیپور زدیم با اینکه نیمه اول خوب نبودیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139714" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139713" target="_blank">📅 20:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139712" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139711" target="_blank">📅 20:12 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
