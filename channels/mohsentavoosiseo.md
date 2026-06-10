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
<img src="https://cdn4.telesco.pe/file/O3TN7zoDPLx73jaHMitBk1VjmSCHxxbES9BkgXEWaYiz5-u_mJfalyxWsBqWQtsmGxyLj3zweLqzqa0COyA3Kdoa6OmSs9z9dE3j8P3WNUkdnwe64oC0oIPeN1RjkJN9PrEPYY0nnLKWTtIr7JRHL0P4H1-haVAX8o5wSRGhHqncJaNwZTFPuZJm66pXFxKHKdf4wh7U1OZR7KG9eFcSC8wQvSBlErK4d9WdEbZe5vOKcLI-vCxM79_X9F6mqNL-oFA_w5DY6qXM316fQw0ZO9wWxtXGA_YT8yoQ1FgoqiWmrDftP_pIK47ZEanX4JxoPZngsWdKu5w12xrL4Mg3qQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.53K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا فقط تالیف، مستندات و تجربه هست. اخبار و ترجمه کار من نیست.دوره:https://mohsentavoosi.com/course/seo/یوتیوب:https://www.youtube.com/c/MohsenTavoosiاینستاگرام:Instagram.com/mohsentavoosi.seohttps://www.linkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سوگیری شدید و نگاه صفر و صدی در جامعه ما
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/mohsentavoosiseo/723" target="_blank">📅 17:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای پروژ های فارسی، ابزار های ایرانی کیورد ریسرچ کافیه.
زمانی که من اکثر سال ایران بودم هم من اشتراکی نمیخریدم. حوصله دردسرشو و قطعی مدامشو نداشتم. همه سه سایتی که اشتراکی میدن همینن.
برای پروژه های خارجی هم یا با پول کارفرما یا چند ماه یبار یه ابزار میخریدم. معمولا منگولز.
اما درک می کنم که یک پنجاهم قیمت اصلی وقتی پول میدی، باید هزار تا اکستنشن کروم تنظیم کنی که اون اشتراکی استفاده کردن ها توسط اون ابزارها لو نره. با دستکاری سشن و کوکی و وی پی ان و خیلی جزئیات و مکافات دیگه. که از نگاه بین المللی، عملا کار غیر قانونی هست. هم فروشش. هم خریدش.
نمیشه هم پول خیلی کم داد هم دردسر نکشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/mohsentavoosiseo/722" target="_blank">📅 16:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اون 20 نفری که تا این لحظه جواب این رو بله زدند، خیلی دوست دارم بدونم چرا منگولز نه؟
من خودم منگولز پریمیوم 40 دلاری اختصاصی میخرم همیشه. یه سئو هست و یه کیورد ریسرچ. کیورد ریسرچ شوخی نداره. مهمه. مهمترین بخش سئوست.
منگولز خیلی بهتره در کل. ارزون تر با محدودیت کمتر با کارایی بیشتر. البته برای کیورد ریسرچ فارسی، ابزار های بومی ایرانی کافی هستند و نیازی به ابزار خارجی نیست.
برای تحقیق کلمات کلیدی کلمات فارسی، ابزار اختصاصی و حتی اشتراکی خارجی نخرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/mohsentavoosiseo/721" target="_blank">📅 14:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🟢
⭕️
نتیجه گیری:
با توجه به اینکه:
⭕️
تعداد فعلی رای ها که همین الان که دارم مینویسم 200 تا "بله" شده،
❗️
این هایی که بله زدند نمیخرن. نرخ تبدیل پایین تر (خوشبینانه یک سوم) خواهد بود،
❗️
هرکس رای داده اگه اولی (همه ابزار ها) رو بله زده، دیگه نمیاد اون یکی ها رو بخره و عملا تعداد کل "بله" ها رو نباید جمع زد،
❗️
در آینده رای گیری بیشتر میشه. اینستا هم استوری بذارم. 10 برابر در نظر میگیریم.
طبق براورد من
❗️
خوشبینانه 400 نفر ماهانه میخرن. بدبینانه 100 نفر. بعد از 6 ماه.
❗️
سود خوشبینانه: 800 تا 1600 دلار. بین 200 تا 300 میلیون تومن.
❗️
سود بدبینانه: 50 دلار. معادل حقوق وزارت کار. بین 15 تا 30 میلیون تومن. عملا با انرژی که ازت میگیره، ضرر مطلقه. گل فروشی سر چهارراه به صرفه تره.
❗️
امکان توسته پذیری با تبلیغات و پشتیبانی قوی و زحمت زیاد در دراز مدت تا 2500 دلار. و با اوج ناامنی با توجه به تغییرات تحریم، دلار و خود ابزار ها و قدرت خرید کاربران.
نتیجه گیری:
با توجه به دردسرهای زیادش، جای مانور پایینش، پشتیبانی سختش، توسعه پذیری بسیار محدودش،
ورود نخواهم کرد
😅
به فروش ابزار های اشتراکی سئو.
بلند فکر کردم شما هم استفاده کنید. هم استفاده کنید هم انتظارتونو از ابزار اشتراکی 1 تومنی که همه چیو با هم میده بیارید پایین و با واقعیت های میدانی آشنا بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/mohsentavoosiseo/720" target="_blank">📅 14:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-poll">
<h4>📊 حاضرید برای Ahrefs ماهانه 1 میلیون و 300 هزار تومن (1300) پرداخت کنید؟ با ماهی 50 تا اعتبار. یعنی 50 تا درخواست(request).</h4>
<ul>
<li>✓ آره حاضرم</li>
<li>✓ نه! No! Hayir! Nein! いいえ! 아니요!, لا! Non!Yox!нет!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/mohsentavoosiseo/719" target="_blank">📅 13:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه برای سیمیلار وب Similarweb ماهانه 800 هزار تومن پرداخت کنید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/mohsentavoosiseo/718" target="_blank">📅 13:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه 1 میلیون و 400 هزار تومن(1400) هزینه کنید برای سمراش؟ Semrush</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/mohsentavoosiseo/717" target="_blank">📅 13:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-poll">
<h4>📊 حاضرید برای ابزار Keyword Tool ماهی یک و نیم میلیون تومن(1.5) هزینه کنید با روزی 5 درخواست؟</h4>
<ul>
<li>✓ بله حاضرم</li>
<li>✓ نه اصلا!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/mohsentavoosiseo/716" target="_blank">📅 13:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه فقط برای ابزار Mangools (کیورد ریسرچ)، 500 هزار تومن هزینه کنید؟ با روزی 25 تا درخواست.</h4>
<ul>
<li>✓ بله حاضرم.</li>
<li>✓ تا ابد نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/mohsentavoosiseo/713" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-712">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه انقدر هزینه کنید؟ماهی 3 میلیون و 700 هزار تومن برای همشون. ولی ابزار ارزون تر کیورد ریسرچ رو فقط میذارم:   Ahrefs,SimilarWeb,Mangools KWfinder,Semrush</h4>
<ul>
<li>✓ بله حاضرم. میصرفه برام.</li>
<li>✓ خیر. به هیچ وجه.</li>
</ul>
</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.  نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول. رنده شده به بالا به ازای هر پنجاه هزار تومن.      Ahrefs= 6.5$…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/mohsentavoosiseo/712" target="_blank">📅 13:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-711">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.
نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول.
رنده شده به بالا به ازای هر پنجاه هزار تومن.
Ahrefs= 6.5$ = 1200
نفری 50 تا اعتبار در کل ماه. 50 تا request
1 میلیون و 170 هزار تومن.
KeywordTool.io
= 7.5$ = 1350
نفری 5 درخواست در روز.
1 میلیون و 350 هزار تومن
Mangools = 2.1$ = 370
نفری 25 کوئری بخش کیورد ریسرچ. در روز.
370 هزار تومن
Semrush = 7$ = 1260
سمراش جوری نیست که به درد اشتراکی دادن بخوره. چون باید سایت ثابت بدی. عملا استفاده 20 نفر مقدور نیست. فقط بخش هاییش قابل استفاده است.
دلیل خرید Moz هم درک نمیکنم اصلا اگر کسی میخره!
Similarweb رو میشه به بیش از 20 نفر داد
چون حالت کردیت و محدودیت تعداد درخواست و روزانه نداره. این رو میگیریم 50 نفر.
Similarweb = 4$ = 720
720 هزار تومن.
این فقط قیمت تمام شده خود ارائه دهنده ابزار اشتراکی با این تعداد کاربران نوشته شده هست به ازای هر اکانت. سالانه بخره حدود 25 درصد کمتر میشه. ولی سالانه ریسکش بالاست برای فروشنده.
حالا هزینه جاری و توسعه ابزار و نگهداری سیستم و پشتیبانی هم حساب کن. من میگم بدترین حالت معادل نیم دلار و بیشترین حالت معادل 2 دلار به ازای هر کاربر. به صورت کلی باید روی قیمت ها بیاد. تا اینجا که هزینه خود فروشنده بود.
در حالت فروش دسته جمعی همشون با هم، باز 2  دلار روش میاریم در بیشترین حالت.
هزینه جاری در کمترین حالت ممکن: 50 میلیون تومن. ولی بهتره 100 در نظر بگیریم. حداقل 500 دلار. در ماه.
میزان درگیری ذهنی و دردسر فروشنده: بسیار بالا.
سود فروشنده در صورت داشتن ماهی 1000 تا کاربر ثابت(که عدد بالایی هست):
در کمترین حالت به صرفه:
90 میلیون تومن - 500 دلار
منهای هزینه جاری: در حد حقوق وزارت کار
در بیشترین حالت به صرفه(که کاربر کم میشه چون نمیتونن پرداخت کنند):
360 میلیون تومن. 2000 دلار.
منهای هزینه جاری: بین 100 تا 200 میلیون تومن.
مشتری واقعی پایدار بر اساس واقعیت فعلی هم، 1000 نیست. هزار باشه باز هم عدد وسوسه کننده ای نیست.
نظر سنجی زیر رو میذارم که عدد در بیاد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/mohsentavoosiseo/711" target="_blank">📅 13:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-710">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با توجه به افزایش تقاضای ابزار های اشتراکی، من قصد داشتم خودم به این حوزه ورود کنم.
ایراد هایی که به سه سایت ایرانی ارائه ابزار اشتراکی خارجی داشتند این ها بود:
- پشتیبانی ضعیف
- قطع شدن مداوم ابزار ها و هدررفتن زمان اشتراک
- نداشتن محصول مورد نظر
- طراحی و تجربه کاربری ضعیف.
حالا برای اینکه من بفهمم صرف مالی داره ورود کنم یا نه و شما هم بفهمید(!)، نظر سنجی می کنم از شما.</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/mohsentavoosiseo/710" target="_blank">📅 13:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-709">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZrWbm6MMLa3s1DYas04j0_ai2NTA3Oilm3mdEAbQ9YnkPMavsZ3Lj8D8LiDxHvP-GGNwkrNBFBd7WVV9MP6g2qWD-aByYUqxAxrjl4ufoiaD-5CPckn2XsMn2rclPTbQ-NeUONpQj6TC4LqgxIzDkzlJEmn1gQN9Nw56D5UVcCzumUHH7jJHO7Uwxx8fLiJst98cQT9lfi5MKhHzW9DIJ72ukM2z0VJtyqqxCfvrwhY1eNHpYrAyRVnMqPd3XAjfthweu54QyRZuXleloa8Y1yMOTicYzx4uR34Rq34KyuJbOJnEey9RznAWvXJdtLjJbLwm9n7GnJfR306ArTFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر با AI زیاد سر و کله زده باشید ارزش جواب کلاد رو میفهمید. هرچند که نسبت به بقیه معجزاتش چیزی نیست.
وضعیت:
گفته باید رو سرور نصب کنی. ولی به جای "سرور" گفته رو سیستم. منم اونو بهش گفتم.
حالا AI های دیگه بود چی میگفت:
اره حق با توست. باید روی سرور نصب کنی.
جواب کلاد:
منظورم از سیستم، همون سرور بود.
تفاوت رو متوجه میشید دیگه؟ خیلی تفاوت داره ها! خیلی!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/mohsentavoosiseo/709" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=BPlakjE9AkU27RR7-Gnn6WUyesjUDS_DivITtyhkS0hYxDwpZq0EPoDLq8T8RmXzhkO_H_o656kedqOYTtT1wsbobBaPsSdUDzmPTx4TgSHhyoSYwgsBn3QcH5TJv6UC4ftDkqBuZ3FgQvUCHMEIcxrXk1uRELdDCRvX2U3ZNYLdeCzXUVwnCwx7oKjUCEgFMHkvxi1A7fFnC2dXie8X-SY6wGzWyCaUZquvnbGSFqOW_ufeOheSt82S_Rj47hku96cMKL5aZOfe3TqrXF1Kb7pVRGCNrw0NEFAXErboMuj5Fe3YdCH8seRKPo5euy4k54Xw-0-miCCAKXgb4tFBVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=BPlakjE9AkU27RR7-Gnn6WUyesjUDS_DivITtyhkS0hYxDwpZq0EPoDLq8T8RmXzhkO_H_o656kedqOYTtT1wsbobBaPsSdUDzmPTx4TgSHhyoSYwgsBn3QcH5TJv6UC4ftDkqBuZ3FgQvUCHMEIcxrXk1uRELdDCRvX2U3ZNYLdeCzXUVwnCwx7oKjUCEgFMHkvxi1A7fFnC2dXie8X-SY6wGzWyCaUZquvnbGSFqOW_ufeOheSt82S_Rj47hku96cMKL5aZOfe3TqrXF1Kb7pVRGCNrw0NEFAXErboMuj5Fe3YdCH8seRKPo5euy4k54Xw-0-miCCAKXgb4tFBVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/mohsentavoosiseo/708" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhR050nljhT6f7CBE2GyfnAW7vZLBMnI5PcGZUHL2a57YCu13LGll1HOV5AT1kninaAkT9M9FWEtoPYSd1vTmymahuo3EyStZjvhv_LH7NqbH5wlqjRTuzHCYYwqECTRMpYfA5i0lq0ALY9MzytF8DffyPADRBQyYVMRaVsIAF-j5ggxgr2RkHAnAtpfT0qccsa4ef4IEcd2z7flMo1Ae_r7fdANN0mF-IekhgvRte-4NNG3kZjMsid-3-UInEVHiEL1IBzWgdEzR7CElwfglAwcc2Huf7Pf_QWVyn-UbrU0dngcdqZA9wgNyum1WVSppsF7g2vEsv1ktuVedba_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کم فارسی انگلیسیش چپ و راست هست. ولی همین کافیه تا عاشق کلاد بشید!
اه! انگار قبلا اپدیت شده بود. بذار!
😅
😍
😍
😎
فقط هم ادا نیست. واقعا بازدهی و خروجیش عالیه‌.
هنوز خیلی ها از skill در کلاد استفاده نمیکنن.
در اپدیت دوره، علاوه بر سئو بین المللی(که الان هم یک فصل داریم)، این ها هم آموزش میدم و هرکس دوره رو داره، رایگان آپدیت رو دریافت میکنه. فعلا زمانش رو نمیتونم بگم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/mohsentavoosiseo/707" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=BQ7yAwcT6-2yYXlaPkvfFsVBWdX1eAkYUPRbOabYzfgWG7mzmVRSZpQjVN7exfe2SR395hqIQIBSHey-q9TFSOeR1A17TRwCwGac_gohLzsRVVMPBsjcxSOyCRMWboC-R5hanuluiuNkdjH3TzAOklX4t8YYHDoFrh-56IPdryRJzaeuuiuNj3XBRHJAOyTTLE81OxWlbqIv-AB-5K8Fp1FLD40ED2NndCx6xNzjxVinh3xWdcJn3DIfl92ewG-JlBa9nMOkcmrYidYW5FaY-KkKDKsCJ7Yt0IkAct8Iz0EfmU_yrlwBA95XX2F3qtU4DDWHQ012tFLfx7KxNixHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=BQ7yAwcT6-2yYXlaPkvfFsVBWdX1eAkYUPRbOabYzfgWG7mzmVRSZpQjVN7exfe2SR395hqIQIBSHey-q9TFSOeR1A17TRwCwGac_gohLzsRVVMPBsjcxSOyCRMWboC-R5hanuluiuNkdjH3TzAOklX4t8YYHDoFrh-56IPdryRJzaeuuiuNj3XBRHJAOyTTLE81OxWlbqIv-AB-5K8Fp1FLD40ED2NndCx6xNzjxVinh3xWdcJn3DIfl92ewG-JlBa9nMOkcmrYidYW5FaY-KkKDKsCJ7Yt0IkAct8Iz0EfmU_yrlwBA95XX2F3qtU4DDWHQ012tFLfx7KxNixHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که بحث مقایسه مترو ها شد جا داره بگم، مدیونی اگه به ایران بگی جهان سوم.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/706" target="_blank">📅 11:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فقط هم کیلومتری مقایسه کنیم باید مساحت کل اون شهر هم در نظر بگیریم. استانبول ۷ برابر تهرانه. مساحت توکیو ۲ هزار کیلومتر. مساحت تهران ۷۵۰ کیلومتر.
با همین فرمون سرچ کنسول گوگلو تحلیل کنی تا ابد غلط در میاد تحلیل.
مثل نگاه کردن به avg position کلی برای تشخیص رشد سایت!
تازه طرف فکر میکنه چون حرفه ای به کلیک کار نداره پوزیشنو نگاه میکنه! اینجاست که کسی که فکر میکنه حرفه ای تره آمارش غلط تر میشه!</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/mohsentavoosiseo/705" target="_blank">📅 11:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKp09E5VOHtMEI46TcG8scKpXLEtSfBuEG6HQHgAOeGxO0xvX1JOIGbCxKuOHkoGLQPAnewnsxG5PZGxxfwOeGltcRtd2zyWPAMML2tfTFPzx3GxiGGwCDn3k3AJ9ZQ_qpc-nB5e5xASc2wQeLbdCLfAWQMK3Bpm_AatZzbxO_rn97ZNFjph3zN2cLt1de4RCUMcFHTKsEkXlYAkoqVgvY23uIuCoLEQl0YsWEBdu6rTRkOFLDNWpvhl9lkwjKU9QwpHrj5bU2lSvvMw6jQ8ZRGf8ZJH8jjuSQ1XyhXYVdmT15WYJMtMouuZ_1haNgyMQy1gvtPq29pdcyurT7kogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/mohsentavoosiseo/704" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLfqACdFn0E8jn3QnyvHXpeg3n0K03pnkaa9eYrFqgCs8UXI3bsN4Df1wl_g8bXZJr833GtXJbC7m4jmOg8v9qAPhKwwcdH3AOLmyM7VAqsU7R4qtL_oYhwOn1Tc98JluPE5mnmxo1KuhtC0r7Towkdsbu2U0WCHi5QdDKf1QQoLaLfT-sN2tTz3f5z1wasPOkNN1lnR_ZJBdXzWmM96rjgfvNcXlWk6PHwFTlvxI7KufEWHQzwfk6YsFuZNPS1TfoQlFxIo8uZjhhMFrDjf14em3FV-CEDpbRqAmlFVofQ1rwFvdwykddY8zhl5TMgk8i8ZCdBQv_l8OgCErXh5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سئول کره جنوبی</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/mohsentavoosiseo/702" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHaHL1-8QRzAOaNBFT9XuhgIpSJ-D27Bh32VPkySiiswfpAnxQ2TwZlxir0t6wlIRFFjm2sdkxEpjjELmLR3GtgNuNLg9kYizR_YWWtpMZ1kiTiWOqFifmmOID-UvRHeOeZyNKqIe3K85L6M7lFqMsquPBQeWkzICoxwAyjBQc7ZRBJ-7OTD74KzGf64Q-cbOmZsa6uBgA8pkUSVcXhxFRy4h4S_BIdp-PDT0_RDkNUH7ASWohgEF9JCOKs6OtSJKW1zNASGAhNS6sRYj9x0mF6xMLsDL6DqC5IlURFWoX11s5VzkAeye0dDIsNCH67JaFvuoP4li44tUeuSkxP3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/mohsentavoosiseo/701" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTZ-FpytiwGDyTjBsHV6RX_GaOLyjTVbzFvfC9wW2cOLGSGaJGVw_abKcTdBUwnJZuHXHMniLUT50y6__pQZCsLh9ixkjVXUC9cEqSHA3rmiwhTL0rHz3mNssDHKem3EtEY3TIM_wFLZwWr3DQnqOHMatt1NUTSaasU2aISUyunrXSqkyomEVgdpp_RwxWPGPBdPiqymwXbAuaEI0R_Bt7nHqbkDChiiMoIgiQdXgSsI1_sYozxCZxCObojDByDVY_DWABh_MK3gYwXk4Wz8p_SxQ82xRAhkie9RWbdsCDVE2w5YOC8u8X9L6aHdmLMEp7fFeIAmTxeNg9mttIyr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/mohsentavoosiseo/700" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/mohsentavoosiseo/699" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv5LtxvZXsI7oO3tMdg9r4ROVptia2zngi8dUbZWgAcBbUKfQrrdLLAzZoEPyK4RYOazVDZav3fCUWfmTATMoWbfjPQQl40ftIV2avqRCZ-_mdkSIbjL0kvNGvrlklBhakU18K9B3noJBNRKPxvGu4uNQszl6wEciTMVWI5-adgmjBuJMP7EuxJR6NLHHcTL9GI0Lird8D3SgGO60znmGsBnmCJET0wwp0d1dNAKbMz0M9QI4C2iQvjUZigrR_Fv4fMAPwqlVUEwVf2i-0gXAhsyC7ckal4AbO6S7kcKOIFVfHO2eZF9XDAH4P0rt-xxuiv7FSsRnxofzWOMUzGnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/698" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">احتمال جنگ همچنان بالاست. کارهایی که برای دسترسی گوگل و از خارج برای سایتتون کرده بودید رو همچنان نگه دارید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/mohsentavoosiseo/695" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJozhN32UvbmaNjYqtIsgcdKI-KLyd9svmiUEeGXNP4xIuc5vmB5yQLGp4auL6QxuQq10HbrwLLrzJRe2TT111grNJ5z4u028r79YW6Vl2qIaS4_hDBfvvEX7OmKb9O9NWf1ibm2r2bJhXjID56sUd2uwBckwZnKyI-6ckXaAEnCMClhY54WZR8RXNZrztB2fWSqXYSejraRpkrXGzbDNNtdSHVwyjGLjvmiBfs6FQ0PsLx2UEwJAFF7wGDDPtTodRZon6YzkA_tcDZzXDc7tGHPxEyYppnseR2PAjRQmjrSxCXUgoIHy_uGUpUtDEfZCd2SYw8UFKOp6L6-mrrTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز اینترنت وصل شد یه عده بلاگر شروع کردن به سئو مُرد گفتن که AI اومده.  سرچ کنسولای ما که کلیک میگیره هم توهمه.  لندینگ میسازیم بصورت گپ(رقیبا نساختن) ورودی و فروش مستقیما بالا میره هم تو دنیای موازیه.  پول هایی که به حسابا میاد ازش هم فقط تو ماینکرفته(دنیای…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/mohsentavoosiseo/694" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">باز اینترنت وصل شد یه عده بلاگر شروع کردن به سئو مُرد گفتن که AI اومده.
سرچ کنسولای ما که کلیک میگیره هم توهمه.
لندینگ میسازیم بصورت گپ(رقیبا نساختن) ورودی و فروش مستقیما بالا میره هم تو دنیای موازیه.
پول هایی که به حسابا میاد ازش هم فقط تو ماینکرفته(دنیای خیالی بازی) و واقعی نیست.
ما هم تو خواب، پروژه های کانادا و آمریکا و اروپا و حوزه خلیج فارس،  دستمونه. واقعی نیست.
کارفرماهای خارجی هم تو فیلم Lost مردند و تو دنیای موازی دارن کار میکنن با ما.
گوگل ادز هم جمع کرده ما خبر نداریم. بالاخره نتایج سنتی نباشن ادز هم نیست. این کمپین های ادز ما هم همینطور الکی داره لیر و درهم و دلار حروم میکنه. دیدیم پولمون زیادیه گفتیم ادز بریم.
خجالت داره واقعا. ملت دارن پول پارو میکنن اما طرف صبح تا شب رو تختش دراز کشیده در حال اسکرولینگه و دنبال اینه که چه چیزی مُرد چی نمرد.
اره SEO مُرد. حله. رقیب تو نتایج گوگل کمتر خرج مام کمتر. استقبال کنیم از این تفکر.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/mohsentavoosiseo/693" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">موضوع پزشکی بالا که ربطش دادم به AI هم نظر شخصی بود هم صرفا یه پرانتز بود و به معنی بی ارزش کردن کل علم پزشکی نبود.
علاقه ای هم ندارم کسی رو قانع کنم دربارش. شما پنتوپرازول و اس امپرازولاتونو بخورید تا آخر عمر و به حرف دکترتون گوش بدید. مسیر من برعکسه. هرچند که ۱۱ سال هرروز مسیر شما رو رفته بودم.
پرانتز بسته. برگردیم سر هوش مصنوعی و سئو
😎
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/mohsentavoosiseo/692" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c800f1b10.mp4?token=fikdRzAxvcuuhhkfwNGYoZhIAltN0kSVbheZ_qda_O4OGLDqX7RH3jIW_-fpwmQcaBoRah5tohY57lJbnQecwU2FkGg7VQQ7hmLlm9f-ExTJnQZ0P6pjtJ-qqXLHjE7WBg_nLjMo9zxcpeiD31JOEL52W7NXVDP-PhnwGBAZtl0xKIAjmJBXpaCi7sYYC3KU-lBigR2ejVM_-jU-qRi5Ox3pLriIIDDP35VqlE6g3aGPUzlDNEvDQuvo0qnup43PFGzGAbnm8YX0OcLCwNEuTl5v8DYJQudDJePgxIRsAedvgnk0S6V2rUuD5DETWVuYwyusJymLG8UASAE0LcM7EXO_ipkUQatzAbeeXO_PYIMfmfd5G0TM4QoG1td_pp646HcntdgcBTvkVQRoEEvCAWU5c6LXBsqcHI4qT-qYLJ0CMXt4Whuklr_D-SRBDv2L30F4My-ptULuISA-CTmWTP3zlbxBXmRfPkIYbndhaJk0WRt9ECNcKFSnlueo-pVSE3U4NdI5B9dDLU00FZjHbItL185HIH19mLPvhZiVOSTd3plpQMAu9S2Vm3bS6kCgfaYYJLoj_pSwoGvR6TxaaxE_wMZFXGRswlS8f5A1t0jkGgYNgMw3WGz-IsRwTFAWa6WHmWLqmVmD69qq9G3EEJCZRw8-fFDUN0dXb2vSQVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c800f1b10.mp4?token=fikdRzAxvcuuhhkfwNGYoZhIAltN0kSVbheZ_qda_O4OGLDqX7RH3jIW_-fpwmQcaBoRah5tohY57lJbnQecwU2FkGg7VQQ7hmLlm9f-ExTJnQZ0P6pjtJ-qqXLHjE7WBg_nLjMo9zxcpeiD31JOEL52W7NXVDP-PhnwGBAZtl0xKIAjmJBXpaCi7sYYC3KU-lBigR2ejVM_-jU-qRi5Ox3pLriIIDDP35VqlE6g3aGPUzlDNEvDQuvo0qnup43PFGzGAbnm8YX0OcLCwNEuTl5v8DYJQudDJePgxIRsAedvgnk0S6V2rUuD5DETWVuYwyusJymLG8UASAE0LcM7EXO_ipkUQatzAbeeXO_PYIMfmfd5G0TM4QoG1td_pp646HcntdgcBTvkVQRoEEvCAWU5c6LXBsqcHI4qT-qYLJ0CMXt4Whuklr_D-SRBDv2L30F4My-ptULuISA-CTmWTP3zlbxBXmRfPkIYbndhaJk0WRt9ECNcKFSnlueo-pVSE3U4NdI5B9dDLU00FZjHbItL185HIH19mLPvhZiVOSTd3plpQMAu9S2Vm3bS6kCgfaYYJLoj_pSwoGvR6TxaaxE_wMZFXGRswlS8f5A1t0jkGgYNgMw3WGz-IsRwTFAWa6WHmWLqmVmD69qq9G3EEJCZRw8-fFDUN0dXb2vSQVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در راستای پست قبلی.
مساله اصلی پست قبل، واکسن نیست.
صرفا به صحبت دکتر رابرت مالون که از محقیقن یا مخترعین تکنولوژی MRNA هست درباره بازار سهام توجه کنید.
که خیلی هم بهش گیر دادند که ببند دهنتو.
باید هم ببنده. چون زورش نمیرسه و قدرتشو نداره مقابله کنه. هرچند درست میگه.
و اونجایی که سخنران اول میگه CDC سازمان بیماری های امریکا گفته ما هرگز روی اون موضوع نمیخوایم تحقیق کنیم. (تو وقتی تحقیق میکنی از اطلاعات موجود تحقیق میکنی با AI)
وقتی نمیخوای تحقیق رو انجام بدی یعنی از نتایج اون تحقیق میترسی. و دیتای رسمی که ازش بیرون بیاد کل بازار و اقتصاد و سهام رو ممکنه نابود کنه.
پول، جهت میده به علم. پس تحقیقی که نمیخوان انجام بدن دیتاش نیست. وجود نداره. بعد تو میخوای با AI انجام بدی؟ اینجا باید بری سراغ تحقیقات غیر رسمی تر.
مثلا کبد چرب قرص درمانی تایبد شده نداره. اما تحقیقات پراکنده زیادی از اثر گیاه خارمریم روش شده(همون لیورگل)
هدفم فقط جلب توجه شما به جریان علمی غیر از جریان علمی رایج هست. و شبه علم هم نیست و کار  هم می کنه.
اگر قراره خلاف جهت شنا کنید، ChatGPT رو فراموش کنید. به درد نمیخوره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/mohsentavoosiseo/691" target="_blank">📅 12:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اخیرا جمینای من از کلماتی استفاده می کنه مثل ای بابا یا کلماتی که احساس حسرت، افسوس و هیجانی رو منتقل میکنه.  این در حالیه که هیچ وقت در چت با من این کلمات به کار برده نشده.  تفکر نقاد هوش مصنوعی ها هم بهتر شده و کمتر دیگه علاقه دارند تاییدت کنند.  با همه…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/mohsentavoosiseo/690" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اخیرا جمینای من از کلماتی استفاده می کنه مثل ای بابا یا کلماتی که احساس حسرت، افسوس و هیجانی رو منتقل میکنه.
این در حالیه که هیچ وقت در چت با من این کلمات به کار برده نشده.
تفکر نقاد هوش مصنوعی ها هم بهتر شده و کمتر دیگه علاقه دارند تاییدت کنند.
با همه تغییرات و بروز رسانی ها
الان نمره ۱ تا ۱۰ رو اینطور میدم:
کلاد Opus نمره 9
کلاد Sonnet نمره 6
کلاد Haiko نمره 5 ولی فقط برای خرکاری روتین و تکراری و بدون نیاز به IQ و درک زیاد.
جمینای همه LLM هاش در کل نمره 5 و 6
چت جی پی تی 5.5 نمره 2
چت جی پی تی با Thinkning نمره 2.5
انگار چت جی پی دیگه عقب موندست. نمیتونم آدم حسابش کنم دیگه. امیدوارم تو نسخه های بعد از 5.5 از این حالت آبروریزی نسبت به رقیباش در بیاد.
پی نوشت:
"خرکاری" و کار گِل (gel) معادل رسمی تر نداره. از همه AI های بالا هم پرسیدم اینارو گفتند:
کار روتین و تکراری.
کار طاقت فرسا و وقت گیر.
کار پر زحمت.
کار اجرایی روتین.
وظایف پایه تصدی گری(جمینای گفت. نزدیک ترین معادل)
امور تکراری و کم بازده (جمینای گفت. نزدیک ترین معادل)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/mohsentavoosiseo/689" target="_blank">📅 11:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/mohsentavoosiseo/688" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">احتمالا متوجه شدید که من زدم تو خط نادیده گرفتن. سرمو کردم تو برف فقط دارم فنی حرف میزنم. انگار که همه چی گل و بلبله.
علتش درد زیاده و خستگی. ظرفیتم به پایان رسیده. صدام در نمیاد. من سال ۹۸ گفتم فاز ملی گرایی بر ندارید هی بگید موتورجستجوی ملی. ضررش بیشتر از سودشه. تازه کسانی میگفتند که تو حوزه سئو فعال بودند. پست های لینکدین این موضوع هم لایک میکردند. اون موقع خیلی تنها بودم. تنهایی داد میزدم...
و کلا خیلی حرص و جوش ها. ولی خستم واقعا از دست و پا زدن بیهوده. از خون دل خوردنی که فقط پیرم کرد. از دیدن شرایط و صحنه هایی که جز فرو رفتن تو زمین کاری از دستم بر نمیاد.
اما اینو میدونم نباید همدیگر رو سرزنش کنیم...
به امید روزهای خوب.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/mohsentavoosiseo/686" target="_blank">📅 16:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-WDLnHm0G6a8VcFxog68jfTPo-zvKx6ZGZ0AFThmNgIpfIVz8K3HXqCZHvAV9A4bE5Q9R0EXJysAmtmFQsbcx8E4HozggUkoFWoyYsPBIT9ilnw3D1XBXj2OWvJYKlVTcb6UeHIYIBqTIwf4mez9ApE6-93pPkBt116jtwzsTdB-NFk0LR6z0Wyne4rn506-SsdB_4WtnMTHyzk47RpieS6Sz5I7CXb0yASjQ8w9tHBGqOKrDwww_iIR4qUrv9nJF8Oo1mEbC3bCqkMKKl5vPgFrm4tt-wYUjCMtlODWfm1UCAWrNBiC0Wk7pSO_FBg87qnqjSyYh3ThlEy-CgQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مرحله ای رسیدیم که هوش مصنوعی، خودجوش، خودش از دیتای خودش ایراد میگیره. خیلی خوبه. تبریک میگم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/mohsentavoosiseo/685" target="_blank">📅 21:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-o_RzJKSiDx2Zqr7-jhVsMJCwtuXYBWTO528ZdK2p7w0dALwoA8uTp38KGEBHITyLKPEA4-1vI877S9fvY4cWQlt80H9f-H63bxBywU5MQYnjkG2fDLgRhz4bKToqqr4oojh7DXGp4_Y5OabjmTAqu63S-6-nTkwOHT9FkJp0byfm_1kGbZ56kxJ9dHReLkrR7p-hVZwEuYZWFHk6_R7MZYQwFpMKkwnKVxWdaPs3C6EUfZQGujOroGwKerSlDbv2aKfdUobNUIt3pCRFFFNR7PSFDfFc0YzoDvOGIxDBjI7pDgD_kiynp0XGc_CKDNMAdajKNgCntfOeKJ8PMSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من یه معتادم! معتاد کلاد!
خودش پیشنهاد داد یکی از قانون هامو که بهش داده بودم تغییر بدم و پیشنهاد خوبی هم داد.
اصلا انگار بشره. توقعمو خیلی برده بالا. خیلی هم ریز بین و دقیقه. خیلی هم عمیق میفهمه.
آنتروپیک پس فردا مثل Horizon Zero Down و Forbidden West، ربات هاش زندگی انسان رو می گیرند و باید پناه ببریم به پناهگاه ها و ربات های Anthropic بشن موجودات اصلی زمین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/mohsentavoosiseo/684" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/mohsentavoosiseo/683" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/682" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تمام صحبت های من درباره هاست و سرور و دسترسی و Origin Rule و GEO DNS، پست های زیر هست. درباره sync بودن سرور داخل و خارج هم در لحظه نظری ندارم.
هاست های ایرانی که اخیرا میگن دسترسی گوگل بهشون باز هست(ولی از خارج یا باوی پی ان باز نمیشن)، دیگه چون فقط داخل هست، بحث sync نداره. با تست های من و بازخورد دیگران، بعضی از هاست ها اینطوری هستند و گوگل هم بهشون دسترسی داره(اما وریفای سرچ کنسول باید فقط با دی ان اس باشه).
چه هاستی؟ اسم نمیبرم. پس فردا بد میشه میفته گردن من.
این هم بگم که در تمام شرایط، اختلال وجود داره. الان اپ تایم 90 درصدی(به جای 99.9 درصدی) ایده آل هست.
راه دیگه ای برای هم sync بودن هم در دسترس بودن از داخل و خارج نمیشناسم.
البته که متخصصین devops روی سرور های اختصاصی با هزینه زیاد میتونن. یک سری پلاگین وردپرس هم برای sync دو دیتابیس هست. ولی من چیزی که خودم اجراش نکردم آموزش نمیدم.
تمام صحبت های من در این باره:
https://t.me/mohsentavoosiseo/620
https://t.me/mohsentavoosiseo/623
https://t.me/mohsentavoosiseo/624
https://t.me/mohsentavoosiseo/625
https://t.me/mohsentavoosiseo/628
https://t.me/mohsentavoosiseo/631
https://t.me/mohsentavoosiseo/633
https://t.me/mohsentavoosiseo/634
https://t.me/mohsentavoosiseo/639
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/mohsentavoosiseo/680" target="_blank">📅 18:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-wnSu4f-7-pAR6ww1NHsT9Myllo9yRzV3zba8jglOEL1Kxk1UN6JuAgL_b3yI3YcI9fR2oMeiHR1mq5Jn0Z63tlhg5zdjVrOMjpG3xHnyU6r6KTzEMz3PnB57YB6QT8ZR25ABAOtLKSnlEI5nYFJLtD9GFRBHnsd3ILvTMVkWZrErrVxs77tXelnp7PmzLVC43rsy4SuDWJLkhrbyyxK4jpcFsxd1xNMp9PqYF-heXGVS2OAplXKRPh9aogAuZFgVqIrAXoOTF1_1Z0mg9kbO2rc5mREDbwKh7qej8r3-KHaACrsOeLWxwm5cTxYRTnYXNO9l0kW2LBnoymDTKKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا خوشم نمیاد از این خسیس بازی بیش از حد کلاد. دوتا لینک کرد و خوند، یه دونه گوگل شیت دویست ردیفته و ده ستونه ساخت کلاد مکس(5x pro) شد 22 درصد!
البته با Sonnet کمتر مصرف میکرد قطعا. ولی حوصله خنگ بازیش رو نداشتم چون کار گوگل شیتش پیچیده بود. آدم هم مغزش از جا درمیومد با این تسک.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/mohsentavoosiseo/679" target="_blank">📅 14:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صحبت تلفط شد، خیلی ها خارج رو شامل چند تا دونه کشور خاص میدونن و ملاک ذهنیشون اینه: ایران و امریکا. ایران و کانادا. ایران و آلمان.
هرکس که مهاجرت کرده، ایران و کشوری که رفته رو راس میدونه تو ذهنش.
ولی بهتره ما جهانی فکر کنیم و کل کره زمین رو ببینیم. جهت خط خطی کردن ذهن هایی که ناخواسته محدود شدند، یاداور میشم:
خارج شامل هند، بنگلادش، نپال، سومالی، کنگو، هنگ کنگ، فیلیپین، میانمار، تانزانیا، گامبیا، بوسنی هرزگوین، مغولستان، لیتوانی، لیبی، مصر، غزه و رام الله و کرانه باختری، صربستان، مراکش، قرقیزستان، زامبیا، شیلی، بولیوی، گواتمالا و... هم هست و این ها هم خارج محسوب میشن و جمع کوچکی از سرزمین ها و کشور های غیر انگلیسی زبان هستند!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/mohsentavoosiseo/678" target="_blank">📅 11:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تلفظ Claude به انگلیسی با لهجه بریتانیایی و آمریکایی، کلاد هست. آ کوتاه. کلود نیست. حالا شاید با انگلیسی غیر اصیل مثل هندی و سنگاپوری و اماراتی یه جور دیگه بگن.
تلفظ Claude در بعضی زبان های اروپایی و اسپانیایی و کره ای میشه کلودی.
کشور های مختلف هم به مدل خودشون تلفظ میکنن.
تلفط Claude به فرانسوی میشه کلود. با صدای O. صدای اُ . بعد از d هم e گفته نمیشه. کلوده نیست. کلود. ریشه کلمه claude، فرانسوی هست. در نتیجه کلود هم درست هست.
مثل BMW که متولد آلمانه و آلمانی ها میگن بی ام وی. و آمریکایی ها میگن بی ام دبلیو. عملا اصلش بی ام و هست(نه دبلیو). پورشه هم درست تر و آلمانی تره. پورش رو انگلیسی ها میگن.
اما کلاد، فقط واژه اش ریشه فرانسوی داره. ولی شرکت Anthropic، که سازنده کلاد هست، یک شرکت آمریکاییه.
خلاصه: هم کلاد درسته هم کلود. آ و اُ . کوتاه.
نظر شخصی: برای اینکه با فضای ابری قاطی نکنیم، کلاد بهتره. چه برای مخاطب انگلیسی چه فارسی. تلفظ رسمی انگلیسیش هم کلاد هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/mohsentavoosiseo/677" target="_blank">📅 11:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNYe4lwum0rsUwqeg46_jIyicGL6k6DSRhMHXeM7FZiCFikDtsYt57pmKKttUZ1IloU-_iGfgHb4LT6wFBe4KEE0dfdEr02outhuO3F7Sfan5oEAdFtpnBkpAUpLi_L1AciQrbuOOAJd_zuZVsX6GFEbYMdacSceWrfsu8OPXtNb8u5nFtZtDuEIxQi_n-T02po8YsO5O_uFvyV_Qd63pFJOPx5cxvvxskGAv3YXyVL-Hl10yeyyw1crYQjMSGp_T-1E6dkyU_R8cqLk-llnR3rZ3pn85lwKhv_l6wPa7bSaCPZU7lPQ_ptidXz514Z1WsEdngA-iAEWPUBdHI6jHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه خوبی از کلاد گفتم از بدیشم بگم. مثل chrome که اندازه اسب، رم می خوره، این هم خیلی مصرفش بالاست و گرونه.
کافیه یه کم تسکت متنی نباشه، نسخه Opus بسیار بسیار مصرف می کنه و البته بسیار هم باهوش تر از Sonnet هست.
این سشن ساعتی بشه 70 درصد برای کلاد مکس(5x pro) که ماهی 100 دلار پولشه واقعا زیاد هست.
کلاد پرو برای من اغلب کم میومد. کلاد مکس 5X اغلب زیاد میاد.
یک سری نکته برای بهینه سازی مصرفش از نظر زمانی هم تو
این ویس
گفتم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/mohsentavoosiseo/676" target="_blank">📅 16:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حالا من یه جوری از کلاد تعریف می کنم انگار اکانت کلاد میفروشم(اتفاقا پیام زیاد میاد برای خریدش).
درحالی که برعکس اکانت ChatGPT ارائه میدیم. چیزی که همش تو سرش میزنم
😅
ولی بهرحال اونم کاربرد خودش رو داره. من خود اکانت چت جی پی تی پلاس دارم اختصاصی رو اکانت خودم.
اکانت Cluade Max هم دارم که 5 برابر Claude Pro هست محدودیت هاش. ولی همه اعضای تیم ازش استفاده می کنیم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/mohsentavoosiseo/675" target="_blank">📅 15:51 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-674">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
اگر یکی از موارد زیر روی شما صدق میکنه، یعنی هنوز بسیار بسیار عقب هستید در دنیای هوش مصنوعی. راه حل چیه؟ برعکس موارد زیر رو انجام بدید و رویکردتون در تضاد با این ها باشه:
❗️
- تو سر هوش مصنوعی نمی زنید.
❗️
- از هوش مصنوعی ایراد نمی گیرید.
❗️
- تفکر نقاد بهش ندارید.
❗️
- به عنوان فکت چک به حرف هاش و بررسی هاش نگاه می کنید.
❗️
- حواستون به سوگیری هاش و مموری که با در چت با شما ایجاد میشه نیست.
❗️
- از حافظه و مموریش برای اینکه چیزی بهش یاد بدید استفاده نمی کنید.
❗️
- بهش فحش نمی دید یا تند حرف نمیزنید و سعی می کنید باهاش مودب باشید و احساس یه انسان باهاش دارید(جدی)
❗️
- در صحبت با شما گستاخ شده یا به شما تیکه میندازه.
❗️
- از بخش های مختلف و نسخه های مختلفشون مثل instant و thinking و deep research و agent و کانتکتور ها یا خوندن فایل و لینک استفاده نمی کنید.
❗️
- موقع پرامپت دادن برای تولید چیزی یا انجام کاری، بهش دیتا نمیدید یا دیتای کمی میدید و بعد از اینکه تولید کرد تازه یادتون میفته بهش مشخصات بیشتری بدید. مثلا برای تولید عکس، نه سایز میدید نه نسبت نه تم رنگی و واقعی بودن یا کارتونی بودن یا استفاده کردن یا نکردن از چیز خاصی و... . اما به محض تولید هر خروجی یادتون میفته که ااااا اینم باید بهش بگم. تصورتون اینه که مغز شما رو باید بخونه اون بدبخت.
@mohsenavoosiseo</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/mohsentavoosiseo/674" target="_blank">📅 15:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تفاوت کلاد و چت جی پی تی درباره اتفاقات 28 Feb 2026 یا 9 اسفند 1404.
چرا کلاد بی نظیره؟
یه گوگل شیت ساخت و دانلودش کردم. کپیش کردم. و تو یه لینک دیگه بهش دادم. گفتم بخون ببین چی میفهمی.
بهم گفت: این همون فایلیه که خودم برات ساختم!
✅
شما این کارو با Gemini و ChatGPT کنید میشینه توضیح میده. نمیگه این همون فایله.
✅
کلاد بهش گفته نشده هر سوالی رو حداقل تو انقدر حجم محتوا جواب بده. گاهی یه "نه" خالی میگه.
✅
کلاد علاقه ای به قانع کردنت نداره و سوگیریش به شدت پایین تره. سعی نمیکنه راضیت کنه الکی.
✅
از همه مهمتر، کلاد خیلی سریع تر میگه غلط کردم! این چت جی پی تی، یه موجود لفتیست دموکراتیه که کلا فکر میکنه هیچ اشتباهی نمیکنه و تاکید هم داره روش.
فاز اینم داره که نه فلان چیز شایعه هست. شما همین الان برو درباره اتفاقات 28 فوریه یا 9 اسفند ازش بپرس. متوجه میزان و درجه حماقتش میشی. وقتی جواب اشتباه داد بهش بگو برو سرچ کن. باز میره تو فاز اینکه نه شایعه است و... . و یه جوری تاکید میکنه و نقد میکنه که فکر میکنی حقیقت تو دست هاش هست.
بعد گیر میده که تو اشتباه میکنی. بهش میگی سرچ کن میگه نیازی به سرچ نیست!
حالا کلاد چی جواب میده؟
این سوال شما بر اساس فرضی است که نیاز به بررسی دارد. بگذارید جستجو کنم تا ببینم آخرین وضعیت چیست.
کلاد 100. چت جی پی تی صفر.
البته من دارم درباره Opus حرف میزنم. Sonnet بسیار خنگ تر هست ولی باز بهتر از نسخه 5.5 هست و گاها برابری میکنه.
بی انصافی نکنم، باگش تو 5.5 خیلی رفع شد. شما همین سوالی که گفتم رو برو بذار رو نسخه 5.4. کلا در حد ناندرتال ها خنگ میشه دوباره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/mohsentavoosiseo/673" target="_blank">📅 15:36 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هزینه اینترنت ثابت فیبرنوری تو ترکیه 1100 لیر هست با سرعت اسمی 1Gb در ثانیه و سرعت واقعی 600Mb در ثانیه که دیگه Wifi 5G هم جواب نمیده این سرعت رو. و با کابل باید ازش گرفت که افت نکنه.
میشه ۷۰ مگابایت دانلود، ۴۰ مگابایت اپلود. در ثانیه. (هر ۸ بیت، ۱ بایت هست).
با وای فای 5G تا 300Mb میشه اگه نزدیک مودم باشید. با وای فای 2.4G تا حداکثر 100Mb.
یعنی با دلار ۱۸۷ هزار تومن میشه ۴ میلیون و ۵۰۰ هزار تومن.
بدون محدودیت حجم.
تو کافه ها بدبینانه(استارباکس، اسپرسولب) حدود 30 تا 70 Mb در ثانیه هست(حدود ۳ تا ۸ مگابایت در ثانیه). بدون محدودیت حجم.
هزینه کافه: رایگان. یک بار خرید که پسورد بگیرید فقط. بعدا تو هر شعبه ای استفاده کنید بدون سفارش. بدون خجالت. بدون احساس وظیفه برای سفارش دادن.
اینو گفتم که بگم انقدر ما تخریب کردیم بقیه کشورا رو حالا اینه وضعمون.
به خودمون گفتیم متمدن و باهوش و به بقیه گفتیم وحشی و عقب مونده و کم هوش و خنگ...انقدر که گفتیم هه هه ارمنستانم ادم شد واس ما؟ ترکیه که فلان. یونان که فلان. بابا ایتالیایی که خودشون دارن فرار میکنن. دلار دیگه به درد نمیخوره. دلار مرد. امارات بیابون بود برای ما ادم شدن. عمان؟ اون بیابون که هیچی نداره بابا. گرجستان شاخ شده بلیت برگشت میخواد از ایرانیا! ژاپنی ها که تا قبل بمب اتم وحشی بودن! چینی های حشره خور! عرب های سوسمار خور! اصلا همه جا ایران بوده. همش مال ما بوده.
عاشق توهم و چیز غیر نقدیم! هیچ کاری یا واقعیت موجود نداریم!
حله. فعلا کانفیگمونو بخریم
😏
...
ایران چراغ قرمز مخصوص عابر پیاده نداره. یه دونه به من نشون بده! یکی فقط!
چراغی که فقط برای عابر باشه ها! نه اینکه یه گروه ماشین چراغشون قرمز و گروه مقابل سبز بشه. چراغ مخصوص فقط عابر.
چون از نظر مهندسی عالی و از نظر کرامت انسانی بی نظیریم.
فرض کنیم موتوری هام تو چراغ قرمز رد نمیشن! (فرض محال کن).
ایران از این نظر، هم رده افعانستان و پاکستان و بنگلادش و ویتنام و هند و بخش هایی از عراق و کشورهای شمال آفریقاست.
تعصب یعنی نپدیزیم. خرد و عقل یعنی بپذیریم واقعیت رو که بتونیم تغییرش بدیم.
پی نوشت(بدیهی برای اکثر شما)؛
Mb یعنی مگابیت
MB یعنی مگابایت
واحد سرعت، بیت هست. چیزی که ما بهش عادت داریم و تو دانلود منیجر می بینیم، بایت هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/mohsentavoosiseo/660" target="_blank">📅 17:41 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کسانی که میگن چرا طرف رفت ارمنستان یا ترکیه؟ اونجا که ظرفیت نداره فضای دیجیتالشون. اونجا که اقتصادش فلانه!
باید بگم
قرار نیست برن شرکت ترک یا ارمنی کار کنند. ظرفیت اونجا مهم نیست! از دیجیتال مارکتر ها بعیده این حرف!
اونجا فقط یه نقل مکان سکونت فیزیکی هست که اینترنت داشته باشند و بتونن عین انسان با سیم کارتشون ثبت نام و verify کنند در سایت ها و ابزار ها و... .
ما انقدر خوشبختیم که کلا جز ارمنستان و ترکیه جایی نیست بتونیم بی دردسر سه ماه بریم و یا نسبتا ارزون و راحت اقامت بگیریم.
یک کم داره اندونزی و مالزی هم مد میشه برای دیجیتال نومد ها. ولی اون ها هم دورند هم سه ماهه نمیشه رفت هم پرواز پردردسری دارند.
بعضی ها که از اسپانیا و ایتالیا و یونان هم ایراد میگیرن! انگار قراره برن شرکت اسپانیایی ایتالیایی با حقوق های کم اونجا کار کنند.
چرا ذهن باید انقدر محدود فکر کنه که محل فیزیکی فعلی زندگی یعنی شغلت هم باید وابسته به همون بازار باشه؟ اصلا چرا اومدی تو حوزه دیجیتال اگه اینجوری فکر می کردی؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/mohsentavoosiseo/659" target="_blank">📅 11:19 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به زودی در شغل های در سراسر جهان و ایران:
استخدام متخصص فلان (گرافیست، مارکتر، تولید محتوا، توسعه دهنده و...)
ملزومات مهم (نه امتیاز!):
تسلط به کلاد
رسیدیم به این جمله که در آینده افراد شغل هاشونو از دست نمیدن. بلکه کسانی که بلد نیستند با AI کار کنند شغل هاشونو از دست میدن. (فعلا غیر از کارهای دستی مثل آشپزی و ماساژ و خیاطی و...)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/mohsentavoosiseo/658" target="_blank">📅 00:48 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">https://www.zhaket.com/web/speedix-plugin
این شما و این هم افزونه افزایش سرعت سایت وردپرسی در اینترنت ملی.
کسانی که سایت وردپرسی دارند(که اکثریت هستند)، می دونند درد کجاست.
این پلاگین درمان این درده.
✅
باعث کندی  با وی پی ان  یا از خارج از ایران یا زمانی که اینترنت بین الملل وصل هست یا اگه هاست خارج باشه، نمیشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/mohsentavoosiseo/657" target="_blank">📅 00:39 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۴
چیزی که بار سنگینی از دوش من برداشت
رها کردن چیزهایی که میخواستم حفظشون کنم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/mohsentavoosiseo/655" target="_blank">📅 17:20 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۳
مصاحبه بین المللی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/mohsentavoosiseo/654" target="_blank">📅 17:13 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۲
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/mohsentavoosiseo/653" target="_blank">📅 17:09 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/mohsentavoosiseo/652" target="_blank">📅 17:05 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پست بالا:
https://t.me/mohsentavoosiseo/649
درباره Opus بود. نه Sonnet یا Haiku
و من Opus در حالت Adaptive Thinking استفاده میکنم.
خود Opus مصرفش بیشتر هست. در حالت Adaptive Thinking باز هم بیشتر میشه مصرفش.
برای کارهای ساده در حد ترجمه و ویراستاری نقطه ویرگولی و...، اصلا نیاز به Claude نیست. مثل این میمونه که وسط آسفالت صاف، لندکروز ببری. سلطان رو سر چیزای بیخود بیدار نکنید.
تسک ساده هایی که خیلی هم ساده نیستند ولی پیچیده هم نیستند و فقط نیاز دارید خنگ بازی کمتری داشته باشه هوش مصنوعی، هم روی Sonnet. خیلی با Haiko  تجربه ندارم که بگم دربارش.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/mohsentavoosiseo/651" target="_blank">📅 14:02 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کاهش مصرف Session پنج ساعته و هفتگی کلاد.
مصرف دوبرابر کلاد در ساعت های Peek
چرا اشتراکی خیلی معنی نداره برای کلاد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/mohsentavoosiseo/650" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چرا کلاد خداست؟ Claude خداست؟
بدی ChatGPT و Gemini و Grok چیه؟
۳ Anthropic فعلا
Google, OpenAI و
X.AI
صفر
سه هیچ به نفع انتروپیک(شرکت کلاد)
سطح این ویس مبتدی هست. بسیار مبتدی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/mohsentavoosiseo/649" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴
در جریان باشید
🏴
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/mohsentavoosiseo/648" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیامی از بچه ها:
خود ما از این روش اقدام کردیم و ۲ روز تقریبا سایتمون داون بود و هیچ پاسخی نمیدادن.
پیام دیگه ای از بچه ها:
من هاست خارجم نت افراز بود بکاپ داشتم ازش
هاست داخل هم از خود پارس پک گرفتم ریستور رو انجام دادند ولی سایت بالا نمیومد در نهایت تنظیمات رو خودمون انجام دادیم هم هاست هم cdn بعد اوکی شد الان هم خیلی خوبه هم سرعتش خوبه هم قطعی نداره
از داخل و خارج هم همزمان باز میشه
نظر من:
سایت Down میشه. برای من 24 ساعت down شد. ولی ارزید.
احتمالا پیام اول، مثل پیام دوم بوده مشکل فنیش ولی خودش از پس کار بر اومده.
جواب ندادن تیکت(بعد از فعال سازی) و... هم چیزی که بچه های پارس پک باید بررسی کنند که چرا چنین اتفاقی افتاده و چی بوده ماجرا.
من فیدبک رو میذارم اینجا. امیدوارم چه با روش من چه با روش خودتون، سایتتون رو در دسترس کنید و دیگه از وضعیت "در حالت انتظار" خارج بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/mohsentavoosiseo/646" target="_blank">📅 15:25 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anwIxVP7KaNjrHCoCHKNJ9Ejic-ewIB4EGnrdugo4d5xPr3bLaZKWP_I_-qgAkwMqL_e-7qA3_YBKBewdpyjnYOUYBXsoEFf7JIWSL4QWAfeUeD0m-yDcHZ-SoBEBx0Fk_RrJW1G0s9pwIb2u8eLekrBi1FlWF0s2UWVI11AIQdXqG6gBZhsv5JVmmis6gjsu4_gXAmJXjmkm43P-U7LoMFkcNmr15Pxva6Emz3eet2hvcdrBXJv_akR7doxkxYlxMvt12uljtatMF3sgjukGlhshCs0Ap6DA-kpkihmParVrnm2GxtCXWEbqJKt98dZf6jHJI5YJfygn6EtyJzTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و البته ادامه دادن، یعنی سرور اولی هم از خارج هم از داخل در دسترسه. آموزششم بالاتر گفتم رایگان:
https://t.me/mohsentavoosiseo/623
این که دوره نیست. این که دیگه پولی نیست! این که با این نقل و نبات شدن اینترنت بین الملل وسط قطعی، دیگه هزینه ای نداره عملا.
دلیلی که انجام نمیدی چیه؟ بیا با طناب محسن طاوسی برو تو چاه! چاه خوبیه! قبلشم رو سایت خودم و چندین سایت دیگه تست شده.
قدیمی ها میدونن من نسخه تئوری الکی، نه تایید می کنم نه نقض و انکار میکنم.
اون میزان کم جریان مالی و تراکنشی که برات یا برای کارفرمات میاره کافیه! همه چیزم صد درصد باز شه چیزی ضرر نکردی! وقتی بقیه بازارشون صفر مطلق خوابیده بود، تو یه سودی کردی.
از همه مهمتر! بعد روانی موضوع و امید به حرکت هست. بخوای مهاجرت کنی پول نمیخوای؟ نباید بگذره روزگارت؟ که بعدا بری؟ انجامش بده!
رایگان یادم دادم و واضح و قدم به قدم(
اینجا
).
هیچی مستقیم و غیر مستقیم تو جیب من نمیره.
هزینشم برای خودت در حد خرید هاست داخل و خارجه و پول اینترنت برای انتقال بکاپ!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/mohsentavoosiseo/644" target="_blank">📅 13:22 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از اینترنت طبقاتی استرس نگیرید.
🔴
آبان ۹۸ بحث اینترنت ملی داغ بود و موتورجستجوی ملی. دو هفته هم قطع کامل بود.  خیلی ها ترسیدن و رها کردن. زمان مهسا هم همینطور.
🔴
الان که در وسط شرایط جنگ و برزخ رو به بدتر شدن هستیم، اینترنت وصله. وسط جنگ ۱۲ روزه حتی گوگل باز…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/mohsentavoosiseo/643" target="_blank">📅 22:43 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/mohsentavoosiseo/642" target="_blank">📅 17:47 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احتمال سوم:
قطع موندن اینترنت بین الملل و وصل شدن بعضی جاها بصورت لیست سفید و استثنا</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/mohsentavoosiseo/639" target="_blank">📅 15:29 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-637">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee89341378.mp4?token=jDGp0BlSK4Iu32vhLdRRVsXREkDzvZNqFIuxHHp0MJVOhNJcg5jlM1cFJ86ptB_c207GF9EO9keuaxLmI59Tl5zJ-MQZ0o4qyEGR8O-6gqkCNDXpHodR8avEmNLDsjdYHSHq1Tv3eWCXY3rmWx8CSHXo5GmjEbmjlLCtUzrKiJF5KozeBWSIimIWhN2XikDp-WYRq1QZIaubOaXolRO-mZUzUWqbphgDnGtyAuG_pYVOS91JWrAZ22PRVRKZx8za7xJdPlrm5W-zIYzXge29B3iYvdsP5odutrB2USld5KXM3Ra0Tr9jqbzsQkyK5fnKc4iNo44EonOqrr4IvSvLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee89341378.mp4?token=jDGp0BlSK4Iu32vhLdRRVsXREkDzvZNqFIuxHHp0MJVOhNJcg5jlM1cFJ86ptB_c207GF9EO9keuaxLmI59Tl5zJ-MQZ0o4qyEGR8O-6gqkCNDXpHodR8avEmNLDsjdYHSHq1Tv3eWCXY3rmWx8CSHXo5GmjEbmjlLCtUzrKiJF5KozeBWSIimIWhN2XikDp-WYRq1QZIaubOaXolRO-mZUzUWqbphgDnGtyAuG_pYVOS91JWrAZ22PRVRKZx8za7xJdPlrm5W-zIYzXge29B3iYvdsP5odutrB2USld5KXM3Ra0Tr9jqbzsQkyK5fnKc4iNo44EonOqrr4IvSvLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/mohsentavoosiseo/637" target="_blank">📅 22:07 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستانی که نگران قطع موندن اینترنت هستند، این نظر شخصی من بدون قبول مسئولیت هست و من برنامه هام بر این اساس پیش میره همونطور که قبلا هم گفته بودم:  احتمال اول: وصل شدن دائمی اینترنت بین الملل بهتر از قبل یک بار برای همیشه بدون ترس مجدد از قطعی.   احتمال دوم:…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/mohsentavoosiseo/636" target="_blank">📅 20:49 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قبل از اینکه حرف اصلی رو بزنم این رو بگم که دوره از داخل ایران در دسترس هست.
✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند: تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/635" target="_blank">📅 19:50 · 26 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خیلی ها نمیدونن میرور چیه کلون چیه.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/mohsentavoosiseo/634" target="_blank">📅 14:39 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/mohsentavoosiseo/633" target="_blank">📅 14:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روش راحت بالا اومدن سایت از داخل و خارج! بدون پیچوندن بدون GEO DNS!
امیدوارم هیچ وقت به چنین چیزی دیگه نیاز پیدا نکنیم.
آرزو میکنم به محض اینکه اینکارو کردید پشیمون شید بخاطر وصل شدن ابدی اینترنت بین الملل. آرزو میکنم زحمتتون هدر بره! می ارزه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/mohsentavoosiseo/631" target="_blank">📅 14:21 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فاز امید الکی دادن ندارم. صحبت من فنی هست. انتخاب های متعددی پیش رو داریم. ولی من همیشه دست و پا زدن و یه کاری کردن رو ترجیح میدم به هیچ کاری نکردن. هیچ کاری نکردن و تماشاچی بودن و منتظر بودن من رو از پا میندازه. ته چاه باشم ترجیح میدم دیوار چاه رو بکنم تا بشینم منتظر باشم بالا رو نگاه کنم.
دست و پا برای بقا همیشه مثل فیلم Pianist  نیست. یکیشم مثل وضعیت الان ماست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/mohsentavoosiseo/630" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-629">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
اما در این شرایط چیکار کنیم و خودم چیکار میکنم؟
✅
برای کسانی که ایران هستند:
تولید محتوای فارسی و کمپین های رپورتاژ و محتوای داخلی وب سایت و استخراج عنوان ها با ابزار های داخلی کاریه که میشه انجام داد و شما رو جلو میندازه. ماه های بعدی دیگه این مراحل رو تکرار نکنید. برای سه ماه بعد اصلا جلو جلو انجام بدید.
اگر هم سرور داخل هست، بهینه سازی داخلی هم میتونید انجام بدید.
✅
برای کسانی که خارج از ایران هستند:
دوباره باز تولید محتوای داخلی، استراتژی و عناوین محتوای داخلی و آف پیج! به کلی ابزار هم که راحت دسترسی دارید! بهتر نیست از رقبایی که فقط درگیر خوندن اخبار هستند جلو بیفتید؟</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/mohsentavoosiseo/629" target="_blank">📅 11:36 · 22 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-628">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/mohsentavoosiseo/628" target="_blank">📅 18:18 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-627">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درباره یک سری ابزار های جستجوی داخلی از اونجا که دوست ندارم این وضعیت رو دائمی ببینم و عادت بشه و تبلیغ کنم، اسم نمیبرم.
ولی اون ها ترکیبی از گوگل و بینگ هستند به علاوه یک سری شخصی سازی ها و اسلامیزه شده.
شرط اول اینه که هم از داخل هم از خارج بالا بیاد سایتتون که تو پست های قبلی توضیح دادم.
چون اینا خودشون از بینگ و گوگل دیتا میگیرن، گوگل سایت شما رو نبینه اینا هم نمیبینن.
اگرم گوگل ببینه و کاربر داخل باز نکنه سایتتون باز نمیشه و بازم فایده نداره.
بقیش همون سئویی هست که بلدید ولی یک کم سنتی تر. مثلا اگزکت مچ بک لینک با عین کیورد مهم تر هست برای بینگ. و بینگ هنوز به متاکیوردز کار داره.
آموزش سئو بینگ و چت جی پی تی ChatGPT
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/mohsentavoosiseo/627" target="_blank">📅 17:15 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-626">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پست های بالا ویرایش شد. دوباره ببینید. تو اپ های داخلی هم برای کسانی که اینترنت ندارند بفرستید شاید مفید باشه براشون.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/mohsentavoosiseo/626" target="_blank">📅 17:09 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این متن هم محمدرضا زراعتی از بچه های پارس پک و دوست شفیقم برام فرستاد. با شما به اشتراک میذارم. درباره SSL هاست های داخل:
راستی محسن جان الان سایتهایی که داخل ایرانن به خاطر همین قطعی ها مشکل خطای ssl میگیرن چون احراز هویت دامنه پیش‌فرض از روش HTTP هندل میشه برای همین ریکوئست های از صادر کننده سرتیفیکیت نمیرسه به ایران
راهش اینه که اعتبارسنجی ssl رو از روش DNS انجام بدن دیگه مشکل حل میشه.
تو این اموزش یاد دادم چطوری با CDN پارس پک بتونن هندل کنن(برای ssl بر خلاف ارجین رول نیاز نیست دیگه ابر cdn روشن بشه فقط از رکوردهاش استفاده میکنن)
https://docs.parspack.com/ssl/free-ssl-issue-iran-access/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/mohsentavoosiseo/625" target="_blank">📅 17:00 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟  mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود.…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/mohsentavoosiseo/624" target="_blank">📅 16:57 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سایت من از داخل و از خارج در دسترس شد و چه مراحلی طی کردم؟
mohsentavoosi.com
1️⃣
اول انتقال بکاپ. که بسیار سخت بود. انتقال بکاپ 10 گیگی از خارج به داخل سخت بود از نظر قطع شدن و سرعت(الان راحت تره خیلی).
2️⃣
دوم خرید هاست در دوطرف. هاست من از قبل آلمان بود. ایران هم گرفتم.
3️⃣
سوم پیدا کردن جایی که بتونه تقاضای داخل و خارج رو هندل کنه و کار GEO DNS یا سرویس مشابهی انجام بده (مثل قابلیت origin rule). که از اونجایی که از قبل من مشتری پارس پک بودم، این کار انجام شد.
برای پارس پک origin rule هست روی سرویس CDN. و GEO DNS نیست! به گفته خودشون دقت origin rule بسیار بالاتره و ارزون تر هم هست کلا:
https://parspack.com/cdn
پس قدم سوم شد خرید CDN با قابلیت GEO DNS یا Origin Rule (که پارس پک اورجین روله ووبهتره و ارزونم هست)
4️⃣
چهارم دامنه من از شرکتی خریده شده بود که داخل بود و امکان تغییر DNS نداشت. سر اینکه بتونم دی ان اس دامنه خودم رو عوض کنم هم کلی مکافات داشتم و تیکت زدن و... .
5️⃣
و در نهایت با تنظیمات توی پارس پک(تیکت) که واسط بین داخل و خارج بود کار انجام شد.
‼️
راستی میرور و sync نیست! یعنی هاست داخل من عوض شه خارج نمیشه. اگه فروشگاهی باشید سبد خرید و سفارش های هاست خارجتون با داخلتون هماهنگ نیست. من روش هماهنگ رو بلد نیستم. برای من جداست. اهمیتی هم برام نداره.
اگرم فروشگاه باشید اکه بتونید سفارش هایی که با وی پی ان و بی وی ان مدیریت کنید هم کار تمومه. اکثرا دسترسی از خارج رو برای گوگل میخوان و سینک بودن براشون مهم نیست. ملاک رو میتونید دیتای ایران در نظر بگیرید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/mohsentavoosiseo/623" target="_blank">📅 16:51 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از عادی سازی نکردن دی، رسیدیم به اینکه چطوری درامدمون رو در حد بقا حفظ کنیم تا به شرایط عادی یک بار برای همیشه برسیم...
ادامه موارد زیر جهت کمک هست. دست و دلم به پست و تولید محتوا نمیره. ولی میدونم با همین چند تا پست ممکنه کار چند نفر راه بیفته.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/mohsentavoosiseo/622" target="_blank">📅 16:47 · 21 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسید مژده که ایّام غم نخواهد ماند
🔆
شماره در زمان اینترنت ملی در پیام رسان "بله" (متاسفانه):  جهت موارد دسترسی به دوره، خرید، قسط و...: 0919-268-19-56  سایت mohsentavoosi.com از داخل و خارج حالا باز میشه(اپدیت فروردین ۴۰۵)
🔆
🔆
🔆
رسید مژده که ایّام غم نخواهد…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/mohsentavoosiseo/620" target="_blank">📅 19:27 · 08 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،  در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟  بر خلاف تصور عموم، به…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/mohsentavoosiseo/619" target="_blank">📅 17:27 · 18 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیشتر از آمادگی بابت قطعی های مقطعی اینترنت ایران و دسترسی از خارج،
در فکر آمادگی برای تغییر قوانینی هستم که در سود و زیان وب سایت ها موثره و بازی رو عوض میکنه. آیا خدمات و محصولات شما بعد از تغییرات بزرگ همچنان تقاضا یا سود داره‌؟
بر خلاف تصور عموم، به عقیده من کسب و کار های مهاجرتی، همچنان پررونق تر و راحت تر پیش خواهد رفت.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/mohsentavoosiseo/616" target="_blank">📅 19:33 · 03 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-613">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
هوای هم رو داشته باشیم
✅️
چه قبلا قسط دادید چه قبلا اصلا پرداختی نداشتید، سعی می کنیم با شرایط فعلی شما در این شرایط ایران، بتونید تهیه کنید: @mohsentavoosisupport
✅
کسانی که قسط دوره داده بودند و مهلت تعیین کرده بودیم و قرار بود قیمتشون افزایش داشته باشه،…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/613" target="_blank">📅 12:19 · 24 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ما نهایت همکاری رو داریم می کنیم همه جوره که دسترسی همه با مبلغ کم راه بیفته تو اسپات پلیر</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/mohsentavoosiseo/611" target="_blank">📅 16:03 · 12 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/mohsentavoosiseo/610" target="_blank">📅 17:18 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-609">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این پیام رو به کسانی که اینترنت ندارند هم برسونید: الان که شرایط جنگیه و نمیدونیم یک هفته دوهفته ادامه داره یا یکی دوماه تا وصل شدن اینترنت، اگر قسطی دسترسی به دوره داشتید، با مبلغ خیلی کمتر میتونید دسترسی رو کامل کنید یا اگر ندارید جدید بخرید. هم به خاطر…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/mohsentavoosiseo/609" target="_blank">📅 22:26 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.  اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.  راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان…</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/mohsentavoosiseo/608" target="_blank">📅 19:19 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگر سرورتون داخل ایران هست، الان از ایندکس خارج شده صفحاتش.
اگر سرورتون خارج از ایران هست، مشکل گوگلی و ایندکسی نداره ولی کاربر داخل ایران بهش دسترسی نداره.
راه حل؟ هیچ راه حلی نداره. راه حل اینه که کلا اینترنت بین المللی قطع نشه. اگر هاست داخل و سی دی ان خارج کار کنه، باز اینترنت بین الملل یک کم بازه. چیزی که میگم در شرایطی هست که اینترنت بین الملل قطعه.
حتی دی ان اس هم در زمان قطعی اینترنت نمیتونید عوض کنید. چون دی ان اس هم با اینترنت بین المللی هست. ممکنه آی آر ها رو بتونید روی هاست داخلی. که در این صورت گوگل نمیبینه. کاربر میبینه.
در نتیجه، الان یکی از حالت های زیر اتفاق میفته برای همه سایت های با مخاطب ایرانی:
1- از ایندکس خارج شدن و حذف شدن از گوگل (هاست داخلی ها)
2- کاهش رتبه و عدم دریافت ترافیک از کاربر(هاست خارج ها)
امیدوارم یک بار برای همیشه این مشکلات ما تموم بشه و ما مردم ایران، بعد از چند دهه، نفس راحت بکشیم و طعم آزادی و امید و تکاپو و رونق و رشد رو بچشیم و دیگه کف خیابون کشته ندیم
🖤
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/mohsentavoosiseo/607" target="_blank">📅 20:45 · 30 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟢
ساده لوحی در SEO
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/mohsentavoosiseo/606" target="_blank">📅 21:24 · 06 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔍
این به روزرسانی سومین تغییر هسته ای گسترده در سال 2025 است و مانند نسخه های قبلی، هدف آن ارتقای کیفیت و ارتباط محتوا برای کاربران در سراسر جهان است.
🔍
این به روزرسانی صرفا روی یک بخش خاص تمرکز نمیکند؛ با بازتعریف معیارهای رتبه بندی، توانایی گوگل در ارزیابی محتواهای مرتبط، مفید و رضایت بخش را افزایش میدهد.
🔍
گوگل بار دیگر نشان میدهد که ارزش واقعی در محتواهای با کیفیت و تخصصی است، به ویژه در زمینه هایی مثل پزشکی و سلامت که E-E-A-T (تجربه، تخصص، اقتدار و اعتبار) نقشی حیاتی در رتبه بندی دارند.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/mohsentavoosiseo/605" target="_blank">📅 16:49 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/mohsentavoosiseo/604" target="_blank">📅 11:48 · 04 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSiW3fWUDoFUWVHsrQrgtpZ3IOLgIUUV5WQnB8fUBgtsfERXC4vhTMi7oYD3vXoQm-EWJLB2BGt-Xnmibo02gxGQhCf-pT2ASwzUpqXC1VWMJTnVwf9w4UhaYmQJylmi65JeFcEqka4SkFLwy_bsP4ZneljSzvt3W-QHM-pE13xz946-L7igMQcYsEDEkEIJSdHYmymSRyRvK2FqPaPDNXG_SNMWGxu3xK4SgrET8jPNdu9kTwAxll9PmqwuvQxGPBOGeQT8VyS1HIwQ71jTQJ170WpyPEdqxJkA-Qo13dXDeKqMk9UwWRog23RMWZ2cs8K1HeQr_SdGCoPRCWo_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 3
💵
درامد این سایت: ماهانه + 40 م.ت خالص
⁉️
تو ذهنت اینه که سایتی که روزی بیست سی تا ورودی گوگل داره درامدش ماهی 40 تومن
نمیشه؟ آره با آموزش های غلط و بی بازده سئو و تحقیق کلمات کلیدی اشتباه و صفحه بندی و تارگتینگ اشتباه، کاملا حق با توست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/mohsentavoosiseo/603" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HE_bJBmoLOcyegAHc_3Qwuk0mmMgYNtceOK5fiGfkcdFnUYebJfP8HML9cTCfYMkXpOmTxGWWxaxNTJ9PD2eeDFw-YZKA2jctnJTayNUHb1UK1Kavzdicb2lpj9j9PivqdfXaq7eH_XnVn7omCnS55OpdT5ctMyusTYdO0qNxM96ZDKaoKSgiGgadjio8r60dfYOWCGosZaeN6wm3E3ozseAzP3e67R94Sj9elCHlly_MpiuHZj9opMik9Wi4xbkIICGk0ol4LoJouW8v0VWw6FToQKK7J8jzdH_ql2LtImd54K6PGIW2M73TFsnAk3MssanTSe4OZdoGxGzx0aiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 2
💵
درامد این سایت: بالای معادل 200 م.ت. به صورت دلاری. غیر فارسی. مال من نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/mohsentavoosiseo/602" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX2DCnheaQDgRe7enx41Xs_VBg7aQDA-S1MhVedi9tazZlWBQg9qc10mKIQG4IgXlwtNo3z1h-IoqnwswDlGTy5rvrZOFVfhp2FC8yD63AvcYkDXDmMP--fGWnMQpWnmEyrFtf4Ecc87A_yRE63YDDHwfAvqxeQNuZqVgzCjBjlelRB6qe4bo-NoOJSzfzou9ZMJi-xcySefSbN6keOjhkesM8cr5UeE5g8YatD2YJ-hDTUpEtTGmR4BPeRHCMv7l6-fFlKiQWryrv3NWuw8AhEng0IxV6JFsr-qPzoLEWBJvwQMl1zFEuMU2iI-IP-2-1ETjMkK-gPB7bi-9hLPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تو ویس های بالا توضیح دادم
✅
اینم سایت های من که تو اپدیت ها تکون نمیخوره. همیشه همینه. آخرین چیزی که من بهش توجه می کنم آپدیت های گوگله! چون مسیر من ثابته همیشه. به صورت کلی در دراز مدت رو به رشد بر اثر فعالیت های من و با توجه به رقابت موجود.
📎
اسکرین شات سرچ کنسول. شماره 1
💵
درامد این سایت: ماهانه + 300 م.ت خالص
⁉️
نرخ تبدیلش بالاست؟ درسته. این برمیگرده به استراتژی تحقیق کلمات کلیدی شما.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/mohsentavoosiseo/601" target="_blank">📅 17:38 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کلا این صورت مساله که وای الان چیکار کنم گوگل آپدیت کرد، از دیرباز صورت مساله غلطی بود، صورت مساله غلطی هست و صورت مساله غلطی خواهد بود.
تمام پست های انگلیسی سایت های دیگه خیلی از زبان های دیگه هم از اون ها کپی و ترجمه میکنن و درباره راه کارهای افت بعد از اپدیت هست، کلیشه چرت و پرتی بیش نیست!
مثلا میگن تکنیکالتو چک کن! بک لینک های غیر طبیعیتو حذف کن! عنوان ها تو بازبینی کن!
ولی این محتوای بلغور چرت متقاضی داره بهرحال. ترافیک میاره برای اون سایت ها. می طلبه که بنویسن. چهار نفر هم بیان بگن ممنون از پست مفیدتون! اما نفهمن خب آخرش چیکار باید کنن! فقط ذهنشون مبهم تر میشه.
https://www.linkedin.com/posts/mohsentavoosi_aebaeoaew-activity-7409525124615348224-5vg8
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/mohsentavoosiseo/600" target="_blank">📅 13:19 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-599">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟
قسمت دوم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/mohsentavoosiseo/599" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-598">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تو آپدیت گوگل چیکار کنیم؟ چرا افت کردیم؟ راه حل چیه؟ کجا رو بخونیم بفهمیم چه تغییری بدیم؟
قسمت اول
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/mohsentavoosiseo/598" target="_blank">📅 12:44 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-597">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">معلم زبان عالی ولی غیر تجاری!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/mohsentavoosiseo/597" target="_blank">📅 12:34 · 03 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-596">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😶
جمع کردن توشه برای آخرت و رستاخیر و جهان پس از مرگ، با تولید محتوای رایگان در راه رضای خدا و خشنودی خلق خدا، یا پول گرفتن بابت محتوا؟
😶
شاخص های تفکیک ذهنیت کودکانه با ذهنیت بالغ و تجاری
😶
قهرمان بازی و کمونیسم!
😶
چی شد من دوره فروختم؟
😶
شهرت باید درامدزا باشه و نرخ تبدیل داشته باشه! شهرت خالی به درد نمیخوره! دردسر های شهرت نسبی من در حوزه SEO!
😶
مدل کسب و کار تلگرام و گوگل چطوریه و آیا ما میتونیم مثل اونا کار کنیم؟
😶
تلگرام مگه نگفته بود همیشه رایگانه چرا پولی شد؟
😶
😶
آدم خوب نایس گوگولی اصلاح گر بچه مبصر رابین هود نجات دهنده، چرا سرخورده خواهد شد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/mohsentavoosiseo/596" target="_blank">📅 19:15 · 02 Dey 1404</a></div>
</div>

<div class="tg-post" id="msg-595">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🟢
حرفه ای بودن به سابقه زیاد نیست
تفاوت SEO specialist با senior seo و junior seo چیه
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/mohsentavoosiseo/595" target="_blank">📅 18:08 · 30 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-594">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تو ابزارهای اشتراکی، قطعی ها و ایراد ها و اینکه یهو میگه تو حداکثر ظرفیتو استفاده کردی(با اینکه نکردی)؛ رو بپذیرید!
طبیعیه. همون لحظه رسیدن به محدودیت اکانت، نمییتونن درجا شارژ کنن. دستی انجام میشه.
پول کم میدیم که استفاده کنیم فرقش همین چیزاست. قطعی، یه روز یهو از کار افتادن تو زمان مهم، غیر فعال بودن فیچرای دیگه همون ابزار و...
بدون مشکلش رو میخوایم باید پول دلاری کاملش رو با مسترکارت مجازی یا واسطه بدیم و بخریم با ده ها برابر قیمت اونم به ازای تک تکشون.
ما اشتراک ماهانه SAAS, software as a service رو نمیدیم و بجاش با نیم میلیون تومن ماهانه ده تا SAAS رو همزمان میگیریم. نمیشه انتظار بیشتری داشت.
لیمیت پس (کد تخفیف mohsentavoosi)
نوین ترند
فعلا اصلی ها هستن. هر جای دیگه ای ارائه بده تفاوت زیادی نمی تونه ایجاد کنه. مگر تو ظاهر مثل یو آی یو ایکس و راحتی نصب و دسترسی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/mohsentavoosiseo/594" target="_blank">📅 21:00 · 29 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/mohsentavoosiseo/593" target="_blank">📅 23:16 · 24 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🟢
تعداد ریکوئست مهم نیست
کاهش تعداد Request در سایت اختصاصی و وردپرس
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/mohsentavoosiseo/592" target="_blank">📅 15:29 · 24 Azar 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
