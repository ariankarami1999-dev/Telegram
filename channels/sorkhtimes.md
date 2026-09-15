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
<img src="https://cdn4.telesco.pe/file/ET7sHVv32Yf5FBZq-xA3GY3EjlOAJ91vNhftD7URCL5IpyhwnVBNZxr3VqVpZrYKnEbZbYq8cERHTKGbZM7zDlc6Vfj7pnq1jpNqJOo5sJ2Hm04n4HFbvw6vPOt-qxV3BVX3SI3FMVBgHhvDU2K5cuswS_1zfRWs-LRpqCFabDsz8n-ex_CHCBtN9EzwJUM06HsJHKNqo6HSQGI4F6B-KPX1QcjNzQ_T4A4L4xTXqjzL58mVTko4OT77mqfqvJ4hC72oXzUZTjhamu0SIaQRK8m7SmWqzB0-bDqpggbzZ9U6xa0PDEq_2deMrVnxrJGt6qkYms_IuBd96CNgIK7-Qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
⭕️
باشگاه طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/140113" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/140112" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/140111" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/140110" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
❌
پرسپولیس پیشنهاد تراکتور برای نیم‌فصل رو رد کرده و اصلاً قصد نداره اورونوف رو به رقیب مستقیمش بده. قرارداد اورونوف آخر فصل تموم میشه و موندن یا رفتنش برای تابستون هنوز مشخص نیست.
✔️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/140109" target="_blank">📅 17:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/140108" target="_blank">📅 16:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=T_ic9VAlr-PrqlW48cOfnNvScZdnWp_R-XtRD1tQ3rUH3GtzUR6D3GatQ5DzKZgiYKofJiIREmDqdnz6eNRudWZ9qQifSyIZOQdFRkptk7MAh0O5fgGORb11LuX-RPxJ2dnNL9Z8RCdqiZiWjvYOGEBhPGVwERV6wqQzdC0S90UIc3c89RjIm2fxPTEJSuJ9nW0f74tx2_8REH8R12YPlSV9DlMrr2_KFWqp1VezPyTEYf7YzIVwz3vBJkXYeMX74LM62x9jGAMm9S8JnOKi_T-V8g-Kb830OypPol-n_Idr-VEf4DPxJaTm7xzESL3cVA5huWNGCBAUjn-fLwgQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=T_ic9VAlr-PrqlW48cOfnNvScZdnWp_R-XtRD1tQ3rUH3GtzUR6D3GatQ5DzKZgiYKofJiIREmDqdnz6eNRudWZ9qQifSyIZOQdFRkptk7MAh0O5fgGORb11LuX-RPxJ2dnNL9Z8RCdqiZiWjvYOGEBhPGVwERV6wqQzdC0S90UIc3c89RjIm2fxPTEJSuJ9nW0f74tx2_8REH8R12YPlSV9DlMrr2_KFWqp1VezPyTEYf7YzIVwz3vBJkXYeMX74LM62x9jGAMm9S8JnOKi_T-V8g-Kb830OypPol-n_Idr-VEf4DPxJaTm7xzESL3cVA5huWNGCBAUjn-fLwgQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140107" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140106" target="_blank">📅 16:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140105" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140104">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔄
🔄
احد میرزایی، عضو هیات مدیره باشگاه پرسپولیس با جذب محمد قربانی مخالف هست و میگن لازم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140104" target="_blank">📅 16:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140103">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbakwTmJWflqAF9bIj1gzTCRtVkfXrVhDidLG7w8mOPnyZDJdVJv7t8tpY2lGSzvIyuFk86ZG7VGyIZe-Xm-cBL37JFdRZcO79NdDyONkOcCSmB2S446JNh2vzDEPMVvS9ze11gHDaPg3RuBSptCe5mdR6pWyQJsDVTzSbZjhGjzUPvxzZeQZY6gtuYCBZQoP2hel0ct3w6j7SADuzeYBHx53hTBrA6u0KI3Ep2i_JvsAAHMcS8HANWeHnOMhTcYr_K39yNeq7HlMItXFDgIh4ZbWoTg3d2uXBZmW3AWqY4gh_PT5kQFUhu6tyxoTM26Rh1CPeC8dqQV81NEh8osGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حامد کاویان پور مدیر آکادمی پرسپولیس شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/140103" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
محمد حسین صادقی برای اولین بار در لیست پرسپولیس پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140102" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140101" target="_blank">📅 14:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
عبدی: با ۱۸ بازیکن مقابل امارات قرار می‌گیریم/ بازیکنان استقلال و تراکتور روز بازی می‌رسند
✔️
✔️
زمان حضور رضا غندی پور بازیکن شباب الاهلی امارات؟ ما منتظر تمام نفرات ایست بودیم. مبین دهقان از امارات آمد اما غندی‌پور نیامد و متاسفانه او در تیم باشگاهی‌اش…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140100" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQDMldkTKxjlnr-Qf1gk73MRTM-7zhICW9sca925tmAeF_i5sS6Z5d0ydybY9vHuzeNo4mLKB2tW7dgQdXZ9jtCxVELUmtAeQgVkYnaE-XqGCwbeXEZYfLr97wz1I18hslHa2U7GVT4U15eLWUTUaKotLCELqZ5x6gFoppvrEUxi0rp36yxR9bv6lK51-pri3oqlr3j3jRDeadOOh8tNOWJa7ezColwaKM8c0aaIwWd9a2JQNNKnVmkJu7Adq9NR6EJzZnTu5MpMBjExUwsR6PdzWD5RoG5TYN1dFEf5e05VqD8Jfmva0wiVZ0QevjGTJAjLpGObMmUDoO6E0gGXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش،
دنبال جذب مارکو باکیچ
در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140099" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚽
امیر عابدینی مدیرعامل اسبق پرسپولیس: مدیران پرسپولیس عملکرد خوبی دارند؛قهرمان جام ملت‌ها نمی‌شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140098" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/molrU9cd7muofZPA31n9VhUSIotsSbGsFB4IfvEiHwrlcP0ChesBmrX-IJ0EmCFc5hhQM4UI0gpOXHnoU9n7fyWvXdaAwGnYY6NySHhtADaCiEECiatKR2hWUeMW4l_ys3oMesDd5DU10x4nLtPQZ5UcCSI_J7IrPZNmrrYxQjqF_j-lhJsVK5SNd7Kh5cYBtj-9CuwPuk7Z7NgwIlnp16O-LuMBeXYeR5GYLIclh1V7hNbURTSy2AAzzNdFVKHW6SmpNuBPoa96scdsTzbqcZl0ujsdixgMh-_Thtb0uwLGXJFYZ8KVrSMbgidoaCOipQQUxDmh01kwp7aNl0ZKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool -
⚪️
Tottenham
⏰
Tonight 22:30
🏟
Anfield
🟢
لیورپول با وجود احتمال چرخش ترکیب، در آنفیلد از نظر کیفیت و عمق تیم دست بالاتر را دارد؛ مخصوصاً مقابل تاتنهامی که در چهار بازی لیگ هنوز گل نزده است.
اسپرز برای جبران فشار فعلی احتمالاً بازی بازتری ارائه می‌دهد و همین موضوع می‌تواند فضاهای مناسبی برای حملات سریع لیورپول ایجاد کند.
کفه ترازو به سمت لیورپول است؛ برد میزبان محتمل‌تر به نظر می‌رسد، اما چرخش ترکیب می‌تواند بازی را از یک‌طرفه شدن دور کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140097" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140096" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140095" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paX62uvBDqTk3l-qjTPBADYIJLEo2NonQN0Y-46FXTnNmO_Cx6VHz92xQ05aNCNq17xoDHZWLdxUBR_AeU_QlVFhH_mHJlXqmVpOJ5gZ969wXT37XxLPjpD3BBtz3U9BQej97AaW71OOnJS-e4olR5BBySARn8aAfTItEiLhaHIIUnlAQYpQDB6NTMfKUtjTkzAf8YqydPxJpip2bWaJGKYYHu6eI5fWMBresNu8Kj1yegLepFBRQhhGEJUx-sTOp3eLSGwxXzKu6qjrmfcTmYF00DC-fbThdtkuqNA7jiVDiDlUzuUg9qI_m5iUNHRyGVPQd0dIJqAmog8LhL5FYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس؛ عاشق لیگ فشرده
🔺
اسکواد پرمهره پرسپولیس باعث شده برخلاف رقبا، سرخ‌ها از بازی‌های بیشتر استقبال کنن؛ حتی لغو بازی با خیبر هم با اعتراضشون همراه شد.
🔺
پرسپولیس برای برگزاری جام حذفی هم اصرار داره؛ چون با این تیم، شانس گرفتن جام بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140094" target="_blank">📅 11:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
حسین عبدی: محسن خلیلی همین الان بهم زنگ زد گفت سه تا بازیکن مون برای دربی بهمون قرض بدین منم گفتم با فدراسیون صحبت کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140093" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140092">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140092" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140091">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-N0iLQTE6FMcp0qleYEVNGQQOkpTvCNfRhybL_ucUKRxrgdZV01S6Uenw-nFN0v4PTfN3lVlnXdJk_B9ctv3oAa3HVJg8f2VYwIrB5rRp_FgqjSlGsEeFLjy7Y_XQijRkUVEpgN3YOpjs2W8ArYq4TrWHKUDsL5r82Rewt5V2EnWpl07XcjPLoknMgD1KaArVbHbE0JBxmfBEmiYnymJPwssF-J2ez9Pr-e3vlQntTfHhwXIetEbsxGdy4Pj6X80xBLdscIr4CUwE3PnnBOP-yhcE-hK75_dPp2-U5LsdYpRrs59D-t3WCz0YC0J8PHdv6QFUxh4xwu7bcKRzVFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140091" target="_blank">📅 09:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140090">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmNNXsIwDMZSXYUPri4u_wWZY93WAIe_GSUPCnNzB0Wr6l81yQkITQMHBm-Mmo9fIzoT7FuQz70Sf-t250Nr-YvWxlD5qoVpMjtUwygeb3SGbKowqpbTVZOSQb6d0TBUh5cK6suKFkpBYpbcuD2mdtTmBq8LIjXbvw28Zeba3JK5igF50LXqpPeAj-2SfPnNoEN7vmL3CjMtA89HeeFfNHjS-CfbvzWR5MxlL2Un1GSrQ0gUilVM5c-9wgfVbVGLSpK0zaCZ1HZtbeluCyPYhqAmVj4cWCLS9JR6SlMmUcOtH0m0xl_kNlcnxfvQWltc9hxck12e9ag2F6Ux8W2tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فردا شبِ پرهیجان فوتبال؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین داستان فرق می‌کنه
🔥
⚡️
⚽️
فردا ترکیبی از بازی‌های کم‌ریسک و چند تقابل جذاب برای دنبال‌کردن دارد؛ الهلال روی کاغذ شانس اول برابر الغرافه است و رئال مادرید هم مقابل الچه دست بالاتر را دارد، اما ارزش اصلی در بازی‌های نزدیک‌تر دیده می‌شود. لیورپول با تاتنهام می‌تواند از نظر ریتم و موقعیت‌سازی دیدنی باشد، در حالی که آرسنال مقابل ایپسویچ و فیورنتینا برابر پیزا با توجه به شرایط بازی، گزینه‌های قابل‌توجهی برای بررسی هستند. در مجموع، شب شلوغی پیش روست؛ جایی که تفاوت بین «انتخاب روی کاغذ» و «انتخاب با تحلیل» می‌تواند تعیین‌کننده باشد.
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
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140090" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
حداقل میذاشتین یه سال از حماسه ۷ تایی شدنتون بگذره بعد کری میخوندین نخبه های لعنتی، هر وقت رسیدین فینال آسیا میتونین کری بخونین هفتایی های جوگیر
✔️
✔️
کیسه‌کشا هفته اول آسیا: بریم واسه ستاره سوم
✔️
✔️
کیسه‌کشا بعد حذف: عشق فقط فوتبال اروپا
😂
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140089" target="_blank">📅 00:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk_wqyZEhshrrVkpQO3oJUB4KybweLJFKieR336Nm5EzMzgGrtTp17y2xR6a5-Kor-QrWrV1mfUwV5VkCp_B6ZRvEnZ6eU4tx6BrPA6t-plXfpc4EwFA-7rOgzhe2rjUDkf7LRpu0IzalO9Uzi9wGla3Agin6SQEzeWOaEmAi3FY9Th0k9emDZGib3W1WMz3c10eZm7SCqiQN5HP7RYzr_8rvl5saoEttDShQ84T043nkoxJedI0CCpyjYwnePFrjUhaSBLALlpvzm6VeSQOH6rU7rYLBEuZULX01bCI_BvzR3jTZy3k5M8KeLlKnbv2jplB5hfVYR9-jz4WyBleMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اگه برد تو بازی اول لیگ نخبگان تضمینی برای موفقیت بود که تیم جواد نکونام در فصل آخرش تو استقلال که بازی اول سه هیچ الغرافه رو برد هم ۳ گانه داخلی میزد هم تو آسیا نتیجه میگرفت ولی خب اون سال اخرش هشتم شدید
🔴
اتفاقا جوگیر شدن شون بعد یه برد تو آسیا میتونه به نفع ما باشه و اون اعتماد به نفس کاذبی که بهشون تزریق میشه کار دستشون میده ، حالا خوبه بازی اول بود و هنوز بازی با تیمای اماراتی مثل الوصل و شباب و بقیه مونده حالا که انقدر خوشحالی میکنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140088" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4rGCcOPtcyA8PtC0qG-SSGmYl8PIhDqzM1zUdlOh5zlkEvqo6oMi-X5bnJdJ0PJn2R3r1X8MdZa4CngGz363rs756MGjgRZkPW9dUoHBXMmVLqVK6gy9gM4EUVabqhuK9JLBD-jQP03ViRh5SxcjIK1cUqPbjqU_hGaoVThhpUbXa0U6BKSeb1mjb5NQ8dhHrN7BjNdUeWwfanTvQOehW72iRbBjCQUNOWsp2JCY2UCBzCbNjRoKLqUWLKwSw5GOOmwMqZtHGhW3B3FGl7YR8e67DClEg3WYyeTDLbtwcT97Bu5gCaCz07Uk41xscSY2UhreQzTvAtj0l7vV1w6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس با اختلاف بهترین تیم ایران در آسیا طی ۲۰ سال اخیر
❌
علاوه بر دو فینال آسیا و سه نیمه نهایی از نظر مجموع امتیاز هم عملکرد بهتری از بقیه تیم های ایرانی داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140087" target="_blank">📅 00:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140086" target="_blank">📅 00:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQqWi17OcUMCiL2HTv95OZ7teM6ULcrqI5cHuZPyKGV0wMnAJ2SeioAuKumefnlNkVI9exqbayJctqrqXaTyST2aArA4BfRIV4nEWwb-ySUyi0hbIGXGX8dknbY8EVoIjXgszW8MsEt8L9gzbyH-0AwXU3au-NlwvA1DAk13wDzdW7x_BN_pgF224CBuHugprB-ysT-XU7PIJ9RgI_WPc1umWD_znMYz-Pi_cPLz_ru9jL4Rlv4LZWXG2saf3sjKTdSjvtEyPr6qhJBlAn4wcmuH7ZFU4aU9gIgE5gNVgpK632j89CwAXOdiskF3NZeXfdhO4Zh4JbZku5DCWz4nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140085" target="_blank">📅 00:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140084" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
السد هم از آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140083" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140082" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140081" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140080" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
باور کنید پیکان هم این تیم السد و میبرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140079" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140078" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140077" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O2nPRXd4LMRwLCuPqIikvWPWMFm-HsLsQTDw_5CK7ONuEEFDZXnYhXbT1WGTWX3yk3cSeljCVOSismNPZLweiYXz5Dlqs43Lyjodh-uTWMC2gi2a8Xydl7xclLu-smu1-0DkcTr2od89tzcWf8oTuYsXcTHJG0G4whxbBlv677NmqVe-LBbv42Jp_QcbhVSQy8ziroKDKGn2X68kyamJ-TjTK6N5jAU3cQmpqMizrQPY3z70Eqs8UwMAb0l1gSx5comL8eQH-E0tUiCQIKaUKO7_jBnrN9X7YbXlNMzWsM4AekUkBBF_xYiTghc4ET_NgcD7dYJ_2Qe3QCYy6Z2KzCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O2nPRXd4LMRwLCuPqIikvWPWMFm-HsLsQTDw_5CK7ONuEEFDZXnYhXbT1WGTWX3yk3cSeljCVOSismNPZLweiYXz5Dlqs43Lyjodh-uTWMC2gi2a8Xydl7xclLu-smu1-0DkcTr2od89tzcWf8oTuYsXcTHJG0G4whxbBlv677NmqVe-LBbv42Jp_QcbhVSQy8ziroKDKGn2X68kyamJ-TjTK6N5jAU3cQmpqMizrQPY3z70Eqs8UwMAb0l1gSx5comL8eQH-E0tUiCQIKaUKO7_jBnrN9X7YbXlNMzWsM4AekUkBBF_xYiTghc4ET_NgcD7dYJ_2Qe3QCYy6Z2KzCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید دستمزد بیشتر بگیرد؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140076" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140075" target="_blank">📅 23:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140074" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⬅
➡️
⬅
➡️
پرسپولیس در آستانه خرید امتیاز بعثت کرمانشاه و تشکیل «پرسپولیس ب» در لیگ یک قرار گرفته؛ توافقات دو باشگاه خوب پیش رفته و احتمال نهایی شدن این انتقال در روزهای آینده بالاست.
⬅
⬅
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140073" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140072" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
حامد کاویانپور به پرسپولیس بازگشت
🔹
حامد کاویانپور، ستاره سابق پرسپولیس، به عنوان مدیر فنی آکادمی و مسئول بخش استعدادیابی در این باشگاه مشغول به فعالیت شد.
🔹
کاویانپور این سالها مدیر تیم های پایه پیکان بوده که از موفق ترین اکادمی های تهران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140071" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140068">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140068" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140067">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140067" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmcviMS9amUy90v4aeNH-gVVQujsnE54OTpNlPteBnUpxc8wNqrEk8V5C5dYO-MmvOfAhJfjdi694IFe0tn2O-wqr6nfWQLjNoetwVg5_9q_3FNYvfkRfJMuFyibzoINStox9W188AYskDqbIXG-bjzN2N6RHtSOrJiyNkbUrnCdqUshayjMxTpr4BIYepy6XuV1rylXwL9sxE-19o5SQaonIVd_xXdZHtCMhqB431rSTGXWb6xx2CQm5FuNfsBxGVhYHpSUoZn9YLAE46pkaVDyxdwlZtM-2JA2ITpkBGTeFoPzCQK-rhRfvbVPXKq9ZE3Tfqz6iyR0DlMTncQ_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
کیسه گل اول و زد به السد
🔴
گزارشگر میگه غول آسیا گل زد
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140066" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140065" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140064">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140064" target="_blank">📅 21:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140063">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140063" target="_blank">📅 21:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140062" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
ترکیب السد برابر استقلال.
✔️
سعد الشیب، الساندرو رومانیولی، یوسف الحناچ، محمد الوعد، پدرو میگل، محمد منایی، روبرتو فیرمینو، کلودینیهو، آگوستین سوریا، اکرم عفیف، حسن الهیدوس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140061" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
عملکرد مثلث هجومی السد در ۴ هفته اخیر
✔️
اکرم عفیف: ۵ گل، ۴ پاس گل
✔️
روبرتو فیرمینو: ۴ گل، ۲ پاس گل
✔️
کلودینیهو: ۳ گل، ۱ پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140060" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ1TB3H0pkzUSeiulmywBZ88NLPe_QOpsgtWYsfUtk1aXE4Zr64ieXS7P98QFgcvKfsacTzZVTN7FfeHD3C68ew5eE2ketke0vIhKvX08uuVghx1izlSDY2ZWWJXY9k7Cli9O4KxMs-ddncUoG_Q7EPdi1QUBq1Ijv6WeEJut6aO7N4aaYt-wHrwsd3RBZEpaROeDcXh3p6_r6Wi6IQjiwTNqSh1eBmpspooG5ovdYldXaX97vxEaf_MTa3q9_KPeQT6l9Sd0TIuAZDfGZ5sVSVVSKfAF5XkrJp7f92wLfo1c35im14yaqN8V7wwB5RMtNWeoRhXEPwqVjDzZ18uzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
آزادی 10 زندانی توسط مهاجم استقلال
❌
باشگاه استقلال اعلام کرد سعید سحرخیزان،  10 زندانی جرایم نقدی غیرعمدی را آزاد کرد و آنها را به آغوش خانواده‌های خود بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140059" target="_blank">📅 21:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140058" target="_blank">📅 21:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140057" target="_blank">📅 21:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140056" target="_blank">📅 21:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140055">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNN_ZoFuKh-lWjbM_Qdh_GtaMjMVuEQtdFm8hQ-1F_9r_NLQjOT1vhvdugeoJVmHSH_1m_vTpRRNg4hXiBYwCs3eptALlOzGJLQj24KfLP_gMBxSesqAX1ITWJlcLlYL_NT_wgXaqQuTRpFPzqeOkxBdwUN-_myTqNiZK2q3ZEOPhy5A6ftA4obrqaY7tkMAs1rJUYjRJ776wgdqFQUBW5-eMCQKTE2t5Pgy_AujIBaxZYzyPOLdJFq0AyU5jqwog8bvaFpszER2V2svNvxjfVttn6laVNNLEivs2VP53gl_IB1GcFs5dpiMghBXG58mfkicMdiX2jnFC5M0g2SdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140055" target="_blank">📅 21:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140054">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=AHvROUezMwY5xiI-e3O6h-CplDWRVB0vZzfHNhu4NjIzfWZmXeUES5s94pONEfAI51TzbyDzjbh8vxXDIlkoPYASelvskFsY5NdOgSgoOdLWb02Hz5ckcmkYTtDmOcXFgcKeqR8IetEDTS09QXbmTp2_j8WUtSAu2ee-Q-2r3uiUejqQAEaDHdDVm4Mz9SkiKuHLIMQ94wlvXhnayAo3uzGh-Mak8D687EvjlEozbV8BPWY5tCCLqBaDwqNXbyjU3nOCwIXU8uyh7TJnGTeehzoHT6SpHhCtoi-7znvjQxcujSyFOKgxnGilYcAKgOEkybYRndzzs4QY6wjiXFaVZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=AHvROUezMwY5xiI-e3O6h-CplDWRVB0vZzfHNhu4NjIzfWZmXeUES5s94pONEfAI51TzbyDzjbh8vxXDIlkoPYASelvskFsY5NdOgSgoOdLWb02Hz5ckcmkYTtDmOcXFgcKeqR8IetEDTS09QXbmTp2_j8WUtSAu2ee-Q-2r3uiUejqQAEaDHdDVm4Mz9SkiKuHLIMQ94wlvXhnayAo3uzGh-Mak8D687EvjlEozbV8BPWY5tCCLqBaDwqNXbyjU3nOCwIXU8uyh7TJnGTeehzoHT6SpHhCtoi-7znvjQxcujSyFOKgxnGilYcAKgOEkybYRndzzs4QY6wjiXFaVZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/140054" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140053" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=mCNvw-W98CnVIaUdDybpPibzF8VfvaPBlbpMBCVOoupr7giBgVwsHM2VUeUpQ0PliZHoprTQFkMi5fxIziFT-oyOduecOyyQFD6BRtjBZkDiHM_X30yzrgkeufMk7e-Sr-FRttila8uvX917QrcZar50HBrsKwI6UM6XsAafVdsHP4ACFfjzjd757TIuugQ0AstAgJQFl87JJnwwq0ucYDpvJy_5ujo_9kwtMcBD7MiZfp0irYRqMUP5UdJGHKX_vYDwk3wXDbiJ_OjsWvWX9yYV_1hmNPm7Cez5w4Df0MPVQ3NdrVl5fUTCPBCNL4geR_MPJb4ltlkzC7KQiiQEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=mCNvw-W98CnVIaUdDybpPibzF8VfvaPBlbpMBCVOoupr7giBgVwsHM2VUeUpQ0PliZHoprTQFkMi5fxIziFT-oyOduecOyyQFD6BRtjBZkDiHM_X30yzrgkeufMk7e-Sr-FRttila8uvX917QrcZar50HBrsKwI6UM6XsAafVdsHP4ACFfjzjd757TIuugQ0AstAgJQFl87JJnwwq0ucYDpvJy_5ujo_9kwtMcBD7MiZfp0irYRqMUP5UdJGHKX_vYDwk3wXDbiJ_OjsWvWX9yYV_1hmNPm7Cez5w4Df0MPVQ3NdrVl5fUTCPBCNL4geR_MPJb4ltlkzC7KQiiQEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140052" target="_blank">📅 20:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5804386d73.mp4?token=iYWG5kGMYJcy5AWQkjcn7o9inO96avO8zRPLF75bomZJ-aHV0XkjaFDhqFzpTuZoVV9hLqlHNUqlVlbVpuvOPWjKQIHmx9p4fIO3ToJcVTQBxxMqoh6csR1ZcneNS1ROmxod77wtxZKZDZjb13jCEs_wrWzopI-kMmFUAFZaEukkpjruf2EG9vTvSwpxbeNqFjViiBZS_rdMX5Q0zFYnU4PrqR-SO2KIZCRoWL9DDydAGanYNMZA0YotQqoYdb_Ia8vJRe1UQAJNE76m0n_G6jgeoCDlwviF-ZrJjhO0SpkHVJeTF5UKt3u0WAa2V-H59M0l3iQDJAIaOeX4SpllFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5804386d73.mp4?token=iYWG5kGMYJcy5AWQkjcn7o9inO96avO8zRPLF75bomZJ-aHV0XkjaFDhqFzpTuZoVV9hLqlHNUqlVlbVpuvOPWjKQIHmx9p4fIO3ToJcVTQBxxMqoh6csR1ZcneNS1ROmxod77wtxZKZDZjb13jCEs_wrWzopI-kMmFUAFZaEukkpjruf2EG9vTvSwpxbeNqFjViiBZS_rdMX5Q0zFYnU4PrqR-SO2KIZCRoWL9DDydAGanYNMZA0YotQqoYdb_Ia8vJRe1UQAJNE76m0n_G6jgeoCDlwviF-ZrJjhO0SpkHVJeTF5UKt3u0WAa2V-H59M0l3iQDJAIaOeX4SpllFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول شباب الاهلی به ترتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140051" target="_blank">📅 20:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140050">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASq23CbJIiE5enL1BGJGcqgfNo41UzVREToYm7QPxJatP1Xll6h-eEA2XFC7sBI5kFe3PouTapOaGnAvwp0Sk5k8nBkHYbNB4sIJGPR43flD7OeOAt_mVesTgrnSw866ZZqs5JzDLTsTN_8VmTtFVvqdD1U73ntdFR0ODE_Xff7UlkZ9-5d0w6mfk7grguCHOvIAaqyBEqU077DOhI8v5JaK6ukMOKSaS2_bdfgfrh774NpSL_zRQXtOqYn_pyHd3sQoaMlM8qL4xErDKcutxQ0cEgumv5x2M9qWOO9HU1O4BuUBU00ubgKFFcyBJVx2l-1vKHpKbpQ1-L3s3jSRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Esteghlal -
⚪️
AL Sadd
⏰
Tonight 21:45
🏟
Basra International Stadium
🟣
استقلال با تکیه بر ساختار دفاعی منسجم و روند بدون شکست اخیر، احتمالاً بازی را محتاطانه و کنترل‌شده آغاز می‌کند.
السد در نقطه مقابل با ۴ برد متوالی و خط حمله‌ای بسیار آماده وارد میدان شده و روی انتقال سریع می‌تواند استقلال را تحت فشار بگذارد.
با توجه به کیفیت هجومی السد و رویکرد محافظه‌کارانه استقلال، بازی نزدیک و کم‌ریسکی در نیمه‌اول محتمل است؛ اما نیمه دوم می‌تواند کاملاً متفاوت شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140050" target="_blank">📅 20:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=Lr4gIBpOso9axVAhcRqVqXNG3XKlfZme6PbB7EsQvkACfM95Q1BF1sxUcNAAkya8B15rIb9cyql1Em7sZtdPEo_piIP9WQwKo6g2YA9DdAp5K4ydZSPMWcgorro-PZdikDPmJNLMts2esFnPdslLSQbQ2Ez7VJP5OydmF4TvMq1eDvYWCM7L_IIRmh1Yz0PybplZrP98XjXyjQaQdPNaKdwfzSgl1TaOp4iMV6pOSTr-zdobuXaePKSOK5SDNhg76OD9xDfgcf7qPQMi4C8AiLwhw4vTMSaol34M3Huld60Fxal0EnLrgrNsc3SAT1KSe6AkVqE3gkroBcGEpAySSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=Lr4gIBpOso9axVAhcRqVqXNG3XKlfZme6PbB7EsQvkACfM95Q1BF1sxUcNAAkya8B15rIb9cyql1Em7sZtdPEo_piIP9WQwKo6g2YA9DdAp5K4ydZSPMWcgorro-PZdikDPmJNLMts2esFnPdslLSQbQ2Ez7VJP5OydmF4TvMq1eDvYWCM7L_IIRmh1Yz0PybplZrP98XjXyjQaQdPNaKdwfzSgl1TaOp4iMV6pOSTr-zdobuXaePKSOK5SDNhg76OD9xDfgcf7qPQMi4C8AiLwhw4vTMSaol34M3Huld60Fxal0EnLrgrNsc3SAT1KSe6AkVqE3gkroBcGEpAySSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
گل مردود سردار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140049" target="_blank">📅 19:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب شباب الاهلی مقابل تراکتور با حضور فیکس سردار آزمون و سعید عزت‌اللهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140048" target="_blank">📅 19:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk11XMh21ELtz6coZ8oZg5KcFjmkf5KO5juqTAfPDj4SqZkF4YFGVlJRr_DK6vrf0NFddnhmGRMEpSdNr9A28aOfY0uVpj4oXrLeOQaiXsGK4fdXyhwL3N4k9084r76b5Pz_j0Esg3ELXKJhOjN4DR9WANTzGxoLZI61Zih0xCUoa42RcOJIbhz1ZD6q7vLfpLsps1kdFlQBEzJo8aSzPF-UyXej7unZJQ8K-rps6wtfunbv_T1qbDDbXlvtYLmT6tjMkFWf51QWHfbVn29kO-BLGaWcRCOptTQRE-Ark5NyFUUT40emb820pBymlaL63LyJtErixroqTOrNJv53fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
علی علیپور با وجود اینکه پرسپولیس یک بازی کمتر انجام داده، همچنان صدر جدول موثرترین بازیکنان لیگ رو در اختیار داره.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140047" target="_blank">📅 18:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140046" target="_blank">📅 18:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140045" target="_blank">📅 17:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140044">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
پایان زودهنگام حضور گل‌محمدی در عراق
❌
ادعای مجری شبکه الرابعه عراق: یک خبر اختصاصی داریم که با توجه به باخت شب گذشته باشگاه دهوک تصمیم به قطع همکاری با یحیی گل‌محمدی گرفته است.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140044" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
🔻
دهوک عراق با هدایت آقا یحیی گل‌محمدی در هفته هفتم لیگ این کشور متحمل شکست شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140042" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
✔️
شایعات: حسین کنعانی، حسین ابرقویی، امیرحسین محمودی و ابوالفضل جلالی در دیدار دوستانه امروز پرسپولیس از ناحیه زانو مصدوم شد.
❌
ظاهراً کیفیت بد چمن باعث این مصدومیت‌های عجیب شده است…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140041" target="_blank">📅 15:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140040" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140039" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjGFOcRNZ4_uukth0z7E2HFhfj6jfCLoRMsV6kvf9G7DTSdlkBsrdl8dmqELd_kVnZ-jZN8s5_kciVA4xd3KTEgA4sT4O6h2CMH2gAUtknOWb53AmSzKy9W0g0ARzX4Pq0qxYcPtkNDUKVYypeDUXuQFtyBhkq4hp0h-3dEYfoD37aGCnVUX3N3UnuDCHriJroeGwofJPIg3Gj3eacJm0vNOj-tSXhBM9hmJydC5mQiS_0O_KmMnVsR-0eway8ZG1TWFda81reWhaaZtB4c4Rmdz-hp4a3WhNMJUoeGnN3DTk_RPvBEruCELd27OnqkYnjJY3Ech3m1cy7mb0raIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
استقلال در آزمون بزرگ آسیایی؛ سدِ السد مقابل آبی‌ها!
[
استقلال
🔵
🆚
⚪️
السد
]
⚽️
استقلال برای گرفتن امتیاز مقابل السد باید اول بازی را کنترل کند و در انتقال‌ها کم‌اشتباه باشد. السد با مالکیت و کیفیت فنی بالایش می‌تواند خطرناک باشد، اما استقلال هم در ضدحملات فرصت‌های خوبی خواهد داشت. در مجموع، بازی نزدیک و تاکتیکی به نظر می‌رسد و جزئیات می‌تواند سرنوشت مسابقه را تعیین کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140038" target="_blank">📅 14:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140037" target="_blank">📅 13:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140036" target="_blank">📅 13:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از ورزش سه
🎙
🎙
علیرضا بیرانوند از اول آبان به طور قطعی و صد در صدی سرباز محسوب میشه و دیگه نمیتونه برای تراکتورسازی تبریز بازی کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140035" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140034" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140033" target="_blank">📅 11:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140032" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140030" target="_blank">📅 11:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smQykZckJGCwPu8A1hHY9v_VBiHK8X9cE8vmah_4zV4L_8KWLnAGUcihHSp1qYfrI5u6tSkUE_YJ9O4RCoszy6i0Xd5KoddJdmO9eRcae60an67Rsct6Mi6jiknbu8R26aCLMJNDwP6_wA0AeLG9JnoNtDEPucY7nXHeyQbmECXCfLslXUI1WNcb9TEaOorOGQ09kkGMJGbPzXZoVzrwo9okt_szFpz-txnZ2f5usJ65_6xDHDw38-80tzCfK8hlWw0kYSbuhDLQLdt5hLjajkuOaQpbysfcIapIhrdt5AFRDVqL0ucbCF3dQWRv4u4snL6N3HPo2lfZoeMnYII2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140029" target="_blank">📅 11:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140028" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140027" target="_blank">📅 09:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGLT4licjA3JLhuzaliFQtkXQe1a-wJ93m8-2fNfRdsFZBcMGRZTZbdJA_XcRVCLU-sqdDrsdkfDH8HrSGtfB51qttrwwcUBaAd_nqUsEG1HYEUknlTyHLqB6cP-iuRfHCPM-t6_z8Pn6qPKN9WH303fbMGFLsDSTpOVyc6UeJrTIeXayjrP1RSrj__NFM5OPVPKpe0nBegjfZJ68Y__oLfUezKGiR9YEGcr5JdHzN03SBeTcdbXrwLNmtS1AohDwF93dZzwKi0jPq6Yw6XSXw_JLqUre2RknkFeFIJ_A7qZZVBuVDZ-etSiNlhoiVczJ3TUccrT1IDA9hyQXm6bSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140026" target="_blank">📅 09:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LX7eG3DOD2Dx4m09Nyst1ZsMfoidO3d3q1kdX_xhsTa93OVV1Zb43J2jqTxH4YuPENkGP3HbGSKqg5O6N4aMmp4u6ZchmQk3hQleNOohpxQhS6E74n_S85MCTz7apUTa-I8Lsgrz1klu_B3P19_1TKyGs53R9KGx4EznvgdUtNvOAVLQ9P4Mlq9h98bZOjiJAZ0kojUWXjhE5iAeLC7y-V-954EXnIfhFZ3TBCtwRGL4Bv8NnnKy0GvJKGKNLqGtjeUDnHvWx2P9oqGqlDUWWKSZLMn8VS0I3cupoZsSWLSomSdD83CJhAy7pti66mr-Y9ZgLwOnqBCLVB8IgXA-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140025" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140024" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
تیم دهوک عراق با مربیگری یحیی گل‌محمدی سرانجام بعد از ۵ هفته به اولین برد خودش دست یافت.
🇮🇶
در این مسابقه، دهوک که میزبان هم بود تا دقیقه ۷۳ یک بر صفر از نیرو هوایی عقب بود اما با دو گل ایگور برزیلی در دقیقه ۷۴ و ۹۰ به برتری جذابی رسید.
🇰🇬
دهوک با ۷…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140023" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🗞
علیرضا بیرانوند ۶ روز پیش دفترچه سربازی شو پست کرده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140022" target="_blank">📅 00:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
فارس :
⚪️
اگه بیرانوند مهرماه دفترچه اعزام بگیره شاید بتونه با تمدید تو دو یا سه بازه تا نیم فصلو تراکتور بمونه
🗣
ولی اگه امکان تمدید تاریخ اعزام نباشه یا باید تا نیم فصل بدون تیم بمونه یا بره دسته یک و برای نیروی زمینی بازی کنه تا نقل و انتقالات زمستانی…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140021" target="_blank">📅 00:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140020" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=J7xOBt8dhW8hHiw6G3fBzd6rMDa_O3fJwbqMyR6yaTKK0H_sIVvjHIsikfVYk_4HuSELmBue1o7esIdtJGgqfxYG6COqV7EeQ_oaAX8cAefeuFxDWriX-_7uTb8AqFWXOsfdeD6lM04o5WjH81HioDypKlWncVimXhAjs2Zcygcny1cWyafV_G3yv1UsqpOHBNQ84JZF9wvni5JM1ZcDJ_9Unw-cFxtcI2X7YTeaCPOBw5B97JhjYkh3wbw8nkIj3JJabeXBfZfO-F3BPIzxsuSeAzNIB0Ha5k9XGuSJtmPFYyPtEOccw-hzex3WHuDb04bzmHU1-yio6ddaAAZKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=J7xOBt8dhW8hHiw6G3fBzd6rMDa_O3fJwbqMyR6yaTKK0H_sIVvjHIsikfVYk_4HuSELmBue1o7esIdtJGgqfxYG6COqV7EeQ_oaAX8cAefeuFxDWriX-_7uTb8AqFWXOsfdeD6lM04o5WjH81HioDypKlWncVimXhAjs2Zcygcny1cWyafV_G3yv1UsqpOHBNQ84JZF9wvni5JM1ZcDJ_9Unw-cFxtcI2X7YTeaCPOBw5B97JhjYkh3wbw8nkIj3JJabeXBfZfO-F3BPIzxsuSeAzNIB0Ha5k9XGuSJtmPFYyPtEOccw-hzex3WHuDb04bzmHU1-yio6ddaAAZKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140019" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=pqslcmBLcZRbiTqsIrrdvlNxXgguQRCbJTVhQPH_pn2zBYAFngXcFHO3J-ZpP_TPi03RN6sXSZJYDBQ4oJf8Q7DgqdIiPnQEveUO_HtkQpUrsqRTE2uoeOala0yKRK0Ar5k1sLFxBcrZur61La1B-FjhwoWOgoszzXTTwoPBmdO9RyCFbG7jGKz7U7siRAWH-bi2zt588_6uYys3kd7ycm08-EJyo4F0cw8hzfoKhnHZdyiXUw6l6TK8zAvPaf6gcZXcKUmHvRKr4lJ0GZk3WDCn2MTLu3c73NfncN2tgu3qS7GR8fFJrKAuyLw32Lm6h0Nwoa10dPSeSn1ICT3O5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=pqslcmBLcZRbiTqsIrrdvlNxXgguQRCbJTVhQPH_pn2zBYAFngXcFHO3J-ZpP_TPi03RN6sXSZJYDBQ4oJf8Q7DgqdIiPnQEveUO_HtkQpUrsqRTE2uoeOala0yKRK0Ar5k1sLFxBcrZur61La1B-FjhwoWOgoszzXTTwoPBmdO9RyCFbG7jGKz7U7siRAWH-bi2zt588_6uYys3kd7ycm08-EJyo4F0cw8hzfoKhnHZdyiXUw6l6TK8zAvPaf6gcZXcKUmHvRKr4lJ0GZk3WDCn2MTLu3c73NfncN2tgu3qS7GR8fFJrKAuyLw32Lm6h0Nwoa10dPSeSn1ICT3O5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140018" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=HIoctv59i6LPFh8_JETEDjLauf0jHaImhIPo5GdVUKT0PwC4Sj7Vu0X3eLERSfjyYzWj3P91TZBmV6KQwG7PB1UjJJXDmKjPOmzbnD-mdoFq8uXW230hTApawkI1EX2AJDriRgB787phFdLUqo1zEPj7jUgkMIi6Id3ty1rl0LJBFGU4co-2p1DGGGX8wzkjSOuqBvbLl7cISEIIPsur9vMj6L02lsQvoUqWCFoPrR86bnJN8yH22zhRtJkZ7GUjciGgN3_N_-GZvhbTmU9EyPeWnzmSnxhE6FwxHagRh0Bc6uamJLeGgx63ORtSOg8-hghEeR3fS9nKKlSszdiMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=HIoctv59i6LPFh8_JETEDjLauf0jHaImhIPo5GdVUKT0PwC4Sj7Vu0X3eLERSfjyYzWj3P91TZBmV6KQwG7PB1UjJJXDmKjPOmzbnD-mdoFq8uXW230hTApawkI1EX2AJDriRgB787phFdLUqo1zEPj7jUgkMIi6Id3ty1rl0LJBFGU4co-2p1DGGGX8wzkjSOuqBvbLl7cISEIIPsur9vMj6L02lsQvoUqWCFoPrR86bnJN8yH22zhRtJkZ7GUjciGgN3_N_-GZvhbTmU9EyPeWnzmSnxhE6FwxHagRh0Bc6uamJLeGgx63ORtSOg8-hghEeR3fS9nKKlSszdiMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
کنایه تیکدری هافبک پرسپولیس به شرایط ورزشگاه آزادی: قول داده اند آزادی را تا 10،15 سال بعد آماده کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140017" target="_blank">📅 22:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f06355658.mp4?token=mb91zLbz858j9lSaJfShOJsckDBuH7W9LaZXg0tsGi88folmva0RlUMRYnG6r9jtjZ5txA_o3qMCAx2wqxFcjfRjJBt_tqQVLxVILqZkxbEU10xS-YDX6nS122qchkGkE1uBqeYZjS-kShCLWmKV7Y_7ZUoaF_SDiDGmyEG41qzvokXJpRG1n6VXt6cEpb3tV5V_MoDiot5jj7XdOOSufcTUmejXh4JSd348oHvtDA8l_25nAc1lKtPb82bVy29PS9rZoeqogaAR-TXli3ur3BlxCDRnz7AGby3j6Kq-QLoJ-mUK2QHTnRC3YnSZY9MM_VdDS3GRcQWYQcN5gLKrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f06355658.mp4?token=mb91zLbz858j9lSaJfShOJsckDBuH7W9LaZXg0tsGi88folmva0RlUMRYnG6r9jtjZ5txA_o3qMCAx2wqxFcjfRjJBt_tqQVLxVILqZkxbEU10xS-YDX6nS122qchkGkE1uBqeYZjS-kShCLWmKV7Y_7ZUoaF_SDiDGmyEG41qzvokXJpRG1n6VXt6cEpb3tV5V_MoDiot5jj7XdOOSufcTUmejXh4JSd348oHvtDA8l_25nAc1lKtPb82bVy29PS9rZoeqogaAR-TXli3ur3BlxCDRnz7AGby3j6Kq-QLoJ-mUK2QHTnRC3YnSZY9MM_VdDS3GRcQWYQcN5gLKrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
خدابنده لو هافبک پرسپولیس: امسال متحد شده ایم که هم در لیگ برتر و هم جام حذفی نتیجه بگیریم و هواداران را شاد کنیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140016" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ff628214.mp4?token=MXsySFhVZKMdiUFzzZtwhVFMBho7JCdf9ENkWgSkEjgEZkCywutzd9BqZJlzRQ4Z5L8MeMjjWnMvShCyHEXzz0aK8t4sGgLRKC_jfLxi-x-PP4i3HUYUO8o0vhNnjaniQQy-60TTgR12n5HBQJP5rwKUY8zhNzXlux1dde30AZaRq2zXyQxIuh3THpvGaGAIKKSkDKLYPaxSFsY_gYfVTbKYgQpSq-EICgCTmBJbXqdAZiIUuC7urnBew6TC45LJDHCK4bLOiHjXRURtErcGvR9ZaPSEgWmmEXycmcuLoO0SHrny9u6JK6Tr3yQmAB0OYO-s-ztF_KOw8SxMApnW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ff628214.mp4?token=MXsySFhVZKMdiUFzzZtwhVFMBho7JCdf9ENkWgSkEjgEZkCywutzd9BqZJlzRQ4Z5L8MeMjjWnMvShCyHEXzz0aK8t4sGgLRKC_jfLxi-x-PP4i3HUYUO8o0vhNnjaniQQy-60TTgR12n5HBQJP5rwKUY8zhNzXlux1dde30AZaRq2zXyQxIuh3THpvGaGAIKKSkDKLYPaxSFsY_gYfVTbKYgQpSq-EICgCTmBJbXqdAZiIUuC7urnBew6TC45LJDHCK4bLOiHjXRURtErcGvR9ZaPSEgWmmEXycmcuLoO0SHrny9u6JK6Tr3yQmAB0OYO-s-ztF_KOw8SxMApnW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس: از اردوی ترکیه به بعد ترجیح دادیم بیشتر کار کنیم و عملکردمان را نشان دهیم تا اینکه در فضای مجازی باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140015" target="_blank">📅 22:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e456b94978.mp4?token=aqrWShfF89Vc-mSqpzzn7dmaIDRl730M0F9xY-uQ321CEbv3SiHjU3Fpc68oEIacvS_Sp2GO6Gdrlj77VsMaKGTmA2Eb-ivIjZVhgsuY5XNNsjdp700uSfegR_GJOg7rMPo-6vPOz8GakPxDgj9cBPpE5fBhdGfqKzya3HrZu0aW-WFF8W4gkbkdCdfHD40TQDFMORxVuxAaWnQliOU8F1suhrVUilaIDnC1o9zO8Y75C_xNShBhcfoWVnyg-s5nQpBR6jUpR44znhLBAxO0Nu3oyISNskt4BMNPmTsFwWEkEpqT2OGPU0jaA-TwYgTKigVAFg1kEb_YE_4_GkfyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e456b94978.mp4?token=aqrWShfF89Vc-mSqpzzn7dmaIDRl730M0F9xY-uQ321CEbv3SiHjU3Fpc68oEIacvS_Sp2GO6Gdrlj77VsMaKGTmA2Eb-ivIjZVhgsuY5XNNsjdp700uSfegR_GJOg7rMPo-6vPOz8GakPxDgj9cBPpE5fBhdGfqKzya3HrZu0aW-WFF8W4gkbkdCdfHD40TQDFMORxVuxAaWnQliOU8F1suhrVUilaIDnC1o9zO8Y75C_xNShBhcfoWVnyg-s5nQpBR6jUpR44znhLBAxO0Nu3oyISNskt4BMNPmTsFwWEkEpqT2OGPU0jaA-TwYgTKigVAFg1kEb_YE_4_GkfyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس:
🔄
🔄
تا روزی که هواداران و باشگاه مرا بخواهد در پرسپولیس می مانم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140014" target="_blank">📅 22:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=gdkrOk1XubpZVscOZy8-RB5oqSpmh-AEY_U8xhUc178qv1aCr9_qoo5HLT8SSI9yJ7a6WYccxldS4pTAGf4V3wwcg0lpuZAwIvQMtZ94Gd6uhfehxTlCNTyYQuWbb_xLXps2Esc6qT606IzW3RztpQfP8StEj0P8Z-s-wWHgTxPAA3VUlg6famjSvgb2Xc1ZTUYbqDXyb_F7LPVMXSjvUOyQC1ZO-M1b6oZkI5erA5Eq9v6XBlJC7Rlua0uoSapryVFEcobMcDG8StX2tKlee5RX6YIg_DCk2aClgurJtq9ojHS460Rz1kOqxkhK1zGcNgWqII4tcySC4b9fA6kJvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=gdkrOk1XubpZVscOZy8-RB5oqSpmh-AEY_U8xhUc178qv1aCr9_qoo5HLT8SSI9yJ7a6WYccxldS4pTAGf4V3wwcg0lpuZAwIvQMtZ94Gd6uhfehxTlCNTyYQuWbb_xLXps2Esc6qT606IzW3RztpQfP8StEj0P8Z-s-wWHgTxPAA3VUlg6famjSvgb2Xc1ZTUYbqDXyb_F7LPVMXSjvUOyQC1ZO-M1b6oZkI5erA5Eq9v6XBlJC7Rlua0uoSapryVFEcobMcDG8StX2tKlee5RX6YIg_DCk2aClgurJtq9ojHS460Rz1kOqxkhK1zGcNgWqII4tcySC4b9fA6kJvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مهدی تیکدری بازیکن پرسپولیس:
✔️
امسال یک تیم گردن کلفت داریم و نظر همه  هم همین است که امسال حقمان قهرمانی در لیگ است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140013" target="_blank">📅 22:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=MZw7kRVFXDF_HQ2p9QMwm4mqJ3WsxM6NWI-YSGryn13hT0mIjltgfOWVt2V-2ohRrz7g3EcG141Ua2mLBchpHYSXuVtAZ6TNIaEzE0Z8Bj192-yGnD-a-Aw3Bnibi9w5-CTSgP8rSbnNUZbY3nGve3Mw6xEl5zkac7qhfeQBbLVrQNHSNCXpC8nT2D9PQtM6jW7AYXaMT4hb6OctS7DzLFHzXHuxNsklsb3kuc4mViUfhDmQ4vOs_rZB7oyI9nK_j_AG-LxZz-zlnAZl3Y4AxOPD7_d72nUyIS02o0if3Nk63DSovGJn4YZRmINku3kwkLT1tm-7Bc0lveIh6wdBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=MZw7kRVFXDF_HQ2p9QMwm4mqJ3WsxM6NWI-YSGryn13hT0mIjltgfOWVt2V-2ohRrz7g3EcG141Ua2mLBchpHYSXuVtAZ6TNIaEzE0Z8Bj192-yGnD-a-Aw3Bnibi9w5-CTSgP8rSbnNUZbY3nGve3Mw6xEl5zkac7qhfeQBbLVrQNHSNCXpC8nT2D9PQtM6jW7AYXaMT4hb6OctS7DzLFHzXHuxNsklsb3kuc4mViUfhDmQ4vOs_rZB7oyI9nK_j_AG-LxZz-zlnAZl3Y4AxOPD7_d72nUyIS02o0if3Nk63DSovGJn4YZRmINku3kwkLT1tm-7Bc0lveIh6wdBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140012" target="_blank">📅 22:22 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
