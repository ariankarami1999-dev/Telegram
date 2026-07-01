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
<img src="https://cdn4.telesco.pe/file/mrClRRd2ewSdoXMzrcH1KSjc1gqwtYdi8XMBr5vQlHPn0vTD8afNsSRyEkOnGh5n55qjQZVBLdzCcbTTIIqsEo_o1VPx-OJAomTahajRYQB0qNqE17qE9vceQJr8hS3WHIpeL3-LRIh-1OoHmZFQEJhP_X9p_excf74YUYmQcEDLO_C-D-9fMgecEHYBHNv4N0Yco0gv6_72JZMbcZOMra5OJ-5CFBwHUoQPeMwhRmBX-c9MhLKhZ5DD6N-lcVa10w4U7-EdK56xqO71OVVES-ENWt15sJU8xsiKoPG9cvIUaxcrB2sPU4s1evQhqmnPZcECeSCS87ERtOeon0JAhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-134692">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
مهدی رحمتی: این حرف ها چیه که ما نباختیم. خودمون رو که گول نمیتونیم بزنیم. آره نباختیم ولی حذف شدیم اونم تو یکی از ساده ترین گروه های این دوره جام‌جهانی. تاج و قلعه‌نویی باید جوابگو باشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/SorkhTimes/134692" target="_blank">📅 10:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134691">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SorkhTimes/134691" target="_blank">📅 10:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134690">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
❗️
فوتبالی : شنیده می‌شود کریم باقری نقش بسیار مهمی در لیست مازاد پرسپولیس دارد و نفرات این لیست با نظر او و البته اسکوچیچ (که به احتمال زیاد سرمربی بعدی پرسپولیس است) مشخص خواهند شد.
❌
❌
قرار است اسکوچیچ بعد از سفر به تهران، جلسه‌ای را با کریم باقری برگزار…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/134690" target="_blank">📅 10:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوررری
🚨
اوسمار ویرا ظهر امروز ایران را ترک خواهد کرد و جدایی این مربی از پرسپولیس رسمی شد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/134689" target="_blank">📅 10:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید:
🔻
روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است.
🔻
روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/134688" target="_blank">📅 09:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/134687" target="_blank">📅 09:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
عملکرد اوسمار ویرا در دوره دوم مربیگری در پرسپولیس:
🔴
۷ برد - ۲ تساوی - ۶ باخت
🔴
۱۷ گل زده - ۱۶ گل خورده
🔴
میانگین ۲.۴ امتیاز در هر بازی
🔴
عدم کسب سهمیه آسیا
🔴
حذف از جام حذفی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/134686" target="_blank">📅 09:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
✅
عملکرد اوسمار ویرا در دوره اول مربیگری در پرسپولیس:
🔴
۱۳ برد - ۴ تساوی - ۱ باخت
🔴
۳۳ گل زده - ۱۷ گل خورده
🔴
میانگین ۲.۴ امتیاز در هر بازی
🔴
کسب قهرمانی لیگ ۲۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/134685" target="_blank">📅 08:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
🤝
🤝
اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/134684" target="_blank">📅 08:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترکیب پرسپولیس در دیدار امروز برابر چادرملو
🛜
سیستم پایه:۴۴۲
❤️
امیر رضا دفیعی
❤️
حسین ابرقویی
❤️
مرتضی پورعلی‌گنجی
❤️
فرزین معامله‌گری
❤️
دنیل گرا
❤️
میلاد سرلک
❤️
مارکو باکیچ
❤️
تیوی بیفوما
❤️
محمد عمری
❤️
یاسین سلمانی
❤️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/134683" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اخرین فرصت برای عضو شدن بعدش میخوان  کانال رو خصوصی کنن</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134682" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9jmEF6rPyMrN4pkMsnYoKOtZZe9QwQqMXTaFnXSEtU6hZ-KL4O6f5m77BF7ceFLTnKSSelF2lhl75QzmGl21lIqqRP8VcIfvQD_u5BrSejYqXZwTRDCPz2MYw7qO7OAOtYQzkE9u8syQ3HMVN46bAO__26dXbHO3_fD08ogfdN7QHVcu5sX4JcV20_G4gOZAkoHuPTWJ_gt9iOXr-IR09V04g83phR4VAvp9dlokkC7pDGERimdWi24OT99swUAiQrLVCBzLCCCKqBQHnxDc1zsBsUBMfTU7bm1l0rwcSuR4ZeThvXG3rXdPqozMfxpj3_GTPCU0gMD2l5lrJ5SoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
?
💡
کافیه یه کانال معتبر پیدا کنی که کارش تحلیل فوتبال باشه و دارای چند سال سابقه کاری باشه کانال پیشبینی تیپستر پرشین همونیه که دنبالشی چکش کن
👇
https://t.me/+iIi9FxzzcYBjNDg8
https://t.me/+iIi9FxzzcYBjNDg8</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/134681" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🔴
مهدی طاهرخانی
🔴
یکی از مسئولان باشگاه بهم اطمینان داده که صد درصد و بدون شک اسکوچیچ سرمربی فصل بعد پرسپولیس خواهد بود
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134680" target="_blank">📅 00:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
ایجنت دراگان اسکوچیچ: اگه اتفاق خاصی رخ ندهد اسکوچیچ سرمربی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134679" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
تایید شد
🔴
تیکدری به پرسپولیس پیوست.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134678" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین جزئیات از توافق پرسپولیس با اسکوچیچ
🚨
🚨
پس از مذاکرات فشرده مدیران باشگاه پرسپولیس با دراگان اسکوچیچ، سرمربی اسبق تیم ملی فوتبال ایران و تراکتور، توافقات نهایی میان طرفین حاصل شده و این مربی کروات در آستانه حضور روی نیمکت سرخ‌پوشان قرار دارد.
🚨
🚨
بر…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134677" target="_blank">📅 23:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
❗️
با توجه به برخورد و واکنش هوادارن پرسپولیس، عملا بانک شهر بی خیال جذب عزیزی شد!
✅
البته با توجه به حضور پیروانی در آمریکا، بعید است، محبوب ترین سرپرست تاریخ باشگاه پرسپولیس به شغل سابقش بازگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134676" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
🔴
پشمااااااااااام
🔴
صدا و سیما: مراسم استقبال از قهرمانان تیم ملی فوتبال فردا ساعت ۱۳.۳۰ برگزار میشه
😐
😐
🤣
✅
بخاطر حذف بین ۶۴ تیم اونم تو مرحله گروهی!؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134675" target="_blank">📅 23:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
خبرورزشی: امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال ۱ میلیون دلار (معادل ۱۷۰ میلیارد تومن) پاداش گرفت. ۱ میلیون دلارهم بازیکنا و سایر اعضا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/134674" target="_blank">📅 21:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
خداداد عزیزی: حضورم تو پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134673" target="_blank">📅 21:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
خداداد عزیزی: حضورم در پرسپولیس منتفی شد و در تراکتور می‌مانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134672" target="_blank">📅 21:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
فووووووووووری
🗣
فرشید حقیری: خداداد عزیزی به دلیل مشکلات مالی باشگاه، خونه و ماشینی که بانک شهر داده بود رو پس داده و گفته با پرسپولیس فسخ کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/134671" target="_blank">📅 21:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
خداداد عزیزی: حضورم تو پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134670" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
با توجه به برخورد و واکنش هوادارن پرسپولیس، عملا بانک شهر بی خیال جذب عزیزی شد!
✅
البته با توجه به حضور پیروانی در آمریکا، بعید است، محبوب ترین سرپرست تاریخ باشگاه پرسپولیس به شغل سابقش بازگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134669" target="_blank">📅 21:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
✅
حدادی  : خداداد عزیزی و خلیلی گزینه های سرپرستی تیمن  / هیچ فشاری از بانک شهر برای اومدن خداداد نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134668" target="_blank">📅 21:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134667" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2UbMWxeVFbUFzz42GhdtyGw_0nfgZ99yKhLPJxjpFLm235_N62Mfi1L7IpK1Uwb08xv9Yp5sr1U7uSCjECRRocqwIhmFPsML3ptwEFo7K_eliHNSdZJFMUaAQVPZafnMF6R8958WieUIgAVDYrtgklDGY2dB96kxJ7mtbFRgveUTyJyaEYfpGu1naLBg6EflH1wgZR_ydbOW7zaTWFEClA41wKsfS8o8xedaMhFnfl8Fol4m3DHHgVbVDxJVjsuC8FT8KsOzlXRcT-2-FMzUqS7M2GNraFv4G02uDra5sQifSmA5uPfxKl8eXY9YDqHetoPxdKQBq7dSL85YcN0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از جام جهانی
🏆
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
باضریب
⬅️
3.42
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+Bt80HN28Ils5YWE0
◀️
https://t.me/+Bt80HN28Ils5YWE0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134666" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
اوسمار به باشگاه اعلام کرده به رغم دلخوری ها بابت قرارداد سال بعد، شکایتی از پرسپولیس ندارد.
📊
به گزارش خبرنگار قرمزآنلاین، اوسمار ویرا امروز در باشگاه پرسپولیس حضور یافت و جلسه ای را با مدیریت در ساختمان باشگاه برگزار کرد. علت حضور این مربی برزیلی، ظاهراً…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134665" target="_blank">📅 19:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
خبرورزشی: امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال ۱ میلیون دلار (معادل ۱۷۰ میلیارد تومن) پاداش گرفت. ۱ میلیون دلارهم بازیکنا و سایر اعضا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134664" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
شایعات؛ چکی که زنوزی به دانیال داده برگشت خورده و شرایط فسخ کردن داره و خودش بدش نمیاد دوباره با اسکوچیچ کار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134663" target="_blank">📅 18:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
تیوی بیفوما برای جدایی از پرسپولیس خواهان 350 هزار دلار شده است
🔴
همچنین این بازیکن پیشنهاد بازگشت به استقلال خوزستان را دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134662" target="_blank">📅 18:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134661">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
تایید شد
🔴
تیکدری به پرسپولیس پیوست.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134661" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134660">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها :
🚨
باشگاه بزودی با انتشار یک پوستر، از مهدی تیکدری به عنوان اولین خرید رونمایی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134660" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134659">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
اوسمار به باشگاه اعلام کرده به رغم دلخوری ها بابت قرارداد سال بعد، شکایتی از پرسپولیس ندارد.
📊
به گزارش خبرنگار قرمزآنلاین، اوسمار ویرا امروز در باشگاه پرسپولیس حضور یافت و جلسه ای را با مدیریت در ساختمان باشگاه برگزار کرد. علت حضور این مربی برزیلی، ظاهراً…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134659" target="_blank">📅 18:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134658">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7wK4DbNjWZjg8s0ByzpaGMwmhzEIkFBh9c-PN9MKFk3wwA-1SNh1ny-gGjdOf7PvQxr8570iBbKCf7iLHcycV1fdezkTIXMOq0i8kP_Idk0E2QhuaSfJ2NcBNp64Wl-paJ-oVG1xBHZ47ShNCyafoCS8VkX8Qv-uIYwxCJtR0xT4WAfH0Dh-PvcCJ7yIAFnzWGTLMgCIbfD9VvzjRLO8x5fNGby5qfu6oL6_fnhzY-HWm4AjqRYgg4H_UGXf9KBYpQWW7QYlz4SU8vzS2TNpxBN-bHPvyv9l1393cO7NR77socLfkBxhY4umQthBscs3YifQo_zeuTu7IoNlwT0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ادعای فرشید حقیری!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134658" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134657">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNk4rrpULbwXYmEsN-eDX4urzfC6eNhPCw2GmJmKKA1C4xEQ-vAw3lwYaUpP_sKyXWzSpeXDpFIwWz8is5JKF7cZcT0SpW8PoyopRPfFunpwtM-HyHPqvshyX4ryPhfvmw4b2tNxjvVq1m1zIqlw6ORFSyVny9XmQ_ch-FWXSQNwcaiN4u6rpk_nKKftIi6IYxYX3_S9DnlHaNU0Zqx4lXYGi5DCZz2tJNCyeAkKrbrc_2CJdKfKACY5VyB54cenxuwvctrI_hrbWTmn2lfqEKdql5gD9eMN-b0oflrWifSqbbX1SqepEmdMjFapCyK5exuAcguFvFnm2NJoi1hFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
تیکدری را پرسپولیسی بدانید. طبق شنیده ها تیکدری تا 48 ساعت آینده وارد باشگاه پرسپولیس خواهد شد و رسما از او رونمایی میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134657" target="_blank">📅 17:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134656">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
طاهرخانی: اوسمار ویرا سرمربی بعدی تراکتور سازی تبریز هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134656" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134655">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134655" target="_blank">📅 16:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134654">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
پایان اوسمار در پرسپولیس/ اسکوچیچ به زودی سرمربی جدید سرخپوشان می شود
🚨
🚨
مذاکرات باشگاه پرسپولیس با دراگان اسکوچیچ مرد کروات با نتایج مثبت به پایان رسیده است. اسکوچیج نسخه ای از قرارداد را در اختیار وکیلش قرارداده تا آن را بررسی کند و از سوی دیگر باشگاه…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/134654" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها :
🚨
باشگاه بزودی با انتشار یک پوستر، از مهدی تیکدری به عنوان اولین خرید رونمایی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134653" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
تیکدری: پرسپولیس؟ پیشنهاد همیشه وجود دارد و امیدوارم سرمربی این تیم زودتر مشخص شود تا من هم تکلیفم را بدانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134652" target="_blank">📅 15:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
غیررسمی
📊
اسمار ویرا با جدایی از پرسپولیس به عنوان سرمربی جدید تراکتور انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134651" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید:
🔻
روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است.
🔻
روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134650" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚡️
⚡️
⚡️
🚨
فوووووووووووووری
⏺
اوسمار ویه را با امضای تفاهم نامه ای از پرسپولیس جدا شد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134649" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134648" target="_blank">📅 15:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
شایعات؛ چکی که زنوزی به دانیال داده برگشت خورده و شرایط فسخ کردن داره و خودش بدش نمیاد دوباره با اسکوچیچ کار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134647" target="_blank">📅 15:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134646" target="_blank">📅 15:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134645">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3be099de2.mp4?token=NQh4tCOVvjqXlRGC4NZaD7MOCKUdSW5YZR1dEMc36F7GT32d_9zjoq0K-FLAVf6eLVyNxoDqW1lylRuG9FB6FPWTv3Y-mje1x33k9H74RzaD0kO1N9YvViB7tockNV4UlamfRW_5ALZLcJpGHljUjsc6CwGrCA9bzJ4m8F1jFM5qk1UP_gUDApEvzZ1yelKprsbzqhzcbVzTGVzy3qT-o5fFr60vvbKkUW0cTJWokjPI5r4P3ZoOfg3-lsTySRrbHVFtPXJ-7iUARoKQeWZamGJmTWR47ex_HndD3FjDIDvo7c0sDJRPT20b5xtyz0JfNzrDCoJTG7OJ-DfLjz2NNT17sjMINpvk3zw0v_u8ojui_tgFAjtV-moMxJQ6Zyx9q_7Ht3IpHWmh-UBt2NVthLBBowzMg4o3AHpigZeZ-787C7cEbQgP9qD1iVUrD4Q8oYVyibMjjXe2jpYwgbV5JG71bP7zY_L5rfwPobUnFbg1k5MNx2fQmJ2QS54s9h5ZNmI2OPa0g8fXmpKCykmWT21JFZeW0Azf8bsQgTRsnzLhjTqF9SNfq2_wLA1vDd-filfxIo0RcawP0rRVVkbCPnxleqhAdgdS6M47v88rMkLvEyHCT1Fw09s0oigYqU3QK-0BIDfkbCFmV0rf2kCWm8GTK7kM9d5yXANXG6U3XCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3be099de2.mp4?token=NQh4tCOVvjqXlRGC4NZaD7MOCKUdSW5YZR1dEMc36F7GT32d_9zjoq0K-FLAVf6eLVyNxoDqW1lylRuG9FB6FPWTv3Y-mje1x33k9H74RzaD0kO1N9YvViB7tockNV4UlamfRW_5ALZLcJpGHljUjsc6CwGrCA9bzJ4m8F1jFM5qk1UP_gUDApEvzZ1yelKprsbzqhzcbVzTGVzy3qT-o5fFr60vvbKkUW0cTJWokjPI5r4P3ZoOfg3-lsTySRrbHVFtPXJ-7iUARoKQeWZamGJmTWR47ex_HndD3FjDIDvo7c0sDJRPT20b5xtyz0JfNzrDCoJTG7OJ-DfLjz2NNT17sjMINpvk3zw0v_u8ojui_tgFAjtV-moMxJQ6Zyx9q_7Ht3IpHWmh-UBt2NVthLBBowzMg4o3AHpigZeZ-787C7cEbQgP9qD1iVUrD4Q8oYVyibMjjXe2jpYwgbV5JG71bP7zY_L5rfwPobUnFbg1k5MNx2fQmJ2QS54s9h5ZNmI2OPa0g8fXmpKCykmWT21JFZeW0Azf8bsQgTRsnzLhjTqF9SNfq2_wLA1vDd-filfxIo0RcawP0rRVVkbCPnxleqhAdgdS6M47v88rMkLvEyHCT1Fw09s0oigYqU3QK-0BIDfkbCFmV0rf2kCWm8GTK7kM9d5yXANXG6U3XCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
مراکشیا کف آمستردام دارن جشن صعود میگیرن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134645" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134644">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134644" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134643">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134643" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134642">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzKB0whBjii-BE_rGcj8JpY9UkFXEMEeN-23NJJraZIKcP3KMJaYhsHiH-JFD0D3srfQuSrynnJfwga6Pd6pH4ndIA-JkDx8Ftwqoqw34mKldGp3r39PsbzbM219nZkQtYslscEENeu68yytJuXQtzMRCvKEieylv0Sb-Eu_wUd9Eo8jvobdEIDJwKzMVDDoZgTF-SJTjv0v_8Yjerbtm2dckT2K91mXN6_PZqHSK8C1qUZpIk5TcGyk64oFzkgaIm0NZ56cqrn2WUZ11GQNkOdkvBjoM5qMj6xlpOVl6kaX1wthXHZw75OacXkrwu9xiiY7ugPFe0Xmx7s46Xz3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
کریستیانو رونالدو دوتا هواپیما پر از تجهیزات و لوازم پزشکی به قربانیان زلزله در ونزوئلا فرستاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134642" target="_blank">📅 13:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134641">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134641" target="_blank">📅 12:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134640">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
پیشنهاد تاجرنیا به بیرانوند ۱۰۰ میلیارد بوده ولی بختیاری‌زاده گفته نمیخوامش و از بین حسینی و خلیفه یکی رو بیارید.
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134640" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134639">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134639" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134638">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
مهدی تیکدری از گل گهر سیرجان جدا شد
🔴
تیکدری برای عقد قرارداد با پرسپولیس متتظر تعیین و تکلیف نیمکت پرسپولیس است!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/134638" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134637">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/134637" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134636">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
برگاتون بریزه؛ بعد از اینکه شاگردان قلعه نویی نتونستن تو یکی‌از آسون‌ترین گروه‌ها صعود کنن حالا فدراسیون میخواد به هر بازیکنی 20 میلیارد تومان پاداش بدهد. دقیقا این پاداش برای چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/134636" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134635">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
🔴
فیروز کریمی: آقای تاج، حتما باید فحش خارمادر بشنوی که بری؟ یا روی برانکارد؟ باز میخواد بگه دوتا میله کاشتیم؟ بهش آب مناسب هم دادیم تبدیل به گل شده!!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134635" target="_blank">📅 10:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134634">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
پایان اوسمار در پرسپولیس/ اسکوچیچ به زودی سرمربی جدید سرخپوشان می شود
🚨
🚨
مذاکرات باشگاه پرسپولیس با دراگان اسکوچیچ مرد کروات با نتایج مثبت به پایان رسیده است. اسکوچیج نسخه ای از قرارداد را در اختیار وکیلش قرارداده تا آن را بررسی کند و از سوی دیگر باشگاه…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134634" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134633">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134633" target="_blank">📅 09:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134632">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
عینک مخصوص حذف از جام جهانی ۴۸ تیمه فقط ۱۳۴ هزار تومن :)))
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134632" target="_blank">📅 09:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134631">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134631" target="_blank">📅 09:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134630">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
برخلاف ادعای مدیرعامل گل گهر، انتقال مهدی تیکدری به پرسپولیس نهایی و قطعی شده است.
✅
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134630" target="_blank">📅 08:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134629">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134629" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134628">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134628" target="_blank">📅 08:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134626">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">من عضو کانالشونم، تحلیل‌هاشون نسبت به بقیه واقعاً منطقی‌تره. پیشنهاد میکنم حداقل یه نگاه بندازین.»</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134626" target="_blank">📅 01:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134625">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD193F3IabTdASqd2ejcUFK9-ZqKmLPlBc9hYQ-EXEUrahiT3-_i7OAJgaSZRmyBq1XcITIhhLufmRd3dQVpkHtzt8wxmkVAfzZag9dmL1PxCHqgg3Zr_Ti_SrT1N6GmWv0c07d3bRTby7RcdkcMdrRYvRs4wfWFIaVnHEe9zdvkcvG0PIfTw7xgv4xE3T6fSAk56MQevNnwH7gRAozC-J77aG0r3CBQNmHFtycZf1E-lU5HlrjLT06u32saXshZ_fKJrgbh4yTip3oZwlAOFTMmkaBXYgwTKvJ9bvUGTeFjOs3Ppq4gXyoIxyx-rIm4bWGHXRgPuOanUjEIJWV82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
?
💡
کافیه یه کانال معتبر پیدا کنی که کارش تحلیل فوتبال باشه و دارای چند سال سابقه کاری باشه کانال پیشبینی تیپستر پرشین همونیه که دنبالشی چکش کن
👇
https://t.me/+LTqi6B-mG8kxMzU0
https://t.me/+LTqi6B-mG8kxMzU0</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134625" target="_blank">📅 01:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
پایان نیمه اول | سامورایی ها در نیمه نخست برزیلی ها را شوکه کردند
‼️
🇧🇷
برزیل 0
😎
1ژاپن
🇯🇵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134623" target="_blank">📅 00:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134622" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
🔴
فرهیختگان : باشگاه پرسپولیس بعد از برگزاری نشست‌های طولانی با ایجنت اوسمار ویرا در نهایت با او در مورد مسائل مالی به توافق رسید.
🔴
🔴
توجه به این قضیه باشگاه پرسپولیس فقط قرار شد طلب مربوط به قرارداد این فصل اوسمار را که حدود ۳۰۰ هزار دلار است را به وی بپردازد.…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134621" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
استوری جدید فرشید حقیری : امید عالیشاه از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134620" target="_blank">📅 23:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134619" target="_blank">📅 23:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134618">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
کریم باقری: ما بد بازی کردیم و باختیم/ بازیکنان مقصر شکست هستند؟ در این یکی دوسال پرسپولیس شرایط خوبی نداشت آن هم به دلیل تغییرات زیاد است
❌
آمدن اسکوچیچ به پرسپولیس؟  تیم ما مربی داشت که بحث اسکوچیچ شد/ این موضوعات فقط حاشیه سازی  است
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134618" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134617">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134617" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134616">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnFXmc1ElNRmzQoJTrwFE8ZNkDUCgz4aV2YGdBRClkJkVJDMBER_L9s2wLoCPq_P7rPv93dZo1C8ulpFtYuyxXag42PAZziFcOdcUjVSw_ONScUDzATJzc23o6GUbduzkquxOi-gqVOuakXSXWHCuq2EUdGQ2q4lpVeCrRoSzRiRkwKZtCBmI_wcjhb7gQ_KRqfhY-U4Yez1cce0x4gmQkFIqlv6LYYxjwFzuzVnJh0DeOtl2pSkXRPRSThfPHkyv208IKLl9SkJGzfYMbD_U_novPLZda7tgicYj-_e8ptzbRCdcBdiKCBNXwf0gNu6jIpP1IWznThz6albfCHefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
میکس VIP  از بازیهای جام جهانی
🏆
🇧🇷
برزیل
🆚
ژاپن
❤️
🇩🇪
آلمان
🆚
پاراگوئه
🇵🇾
باضریب
⬅️
4.08
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+Bt80HN28Ils5YWE0
◀️
https://t.me/+Bt80HN28Ils5YWE0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134616" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134615">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
ضربات پنالتی دیدار چادرملو و گل‌گهر (۲۲ ضربه)!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/134615" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134614">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134614" target="_blank">📅 22:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134613">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
پایان نیمه اول | سامورایی ها در نیمه نخست برزیلی ها را شوکه کردند
‼️
🇧🇷
برزیل 0
😎
1ژاپن
🇯🇵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134613" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
نیمکت نشینی عالیشاه مقابل چادرملو فنی بود؟
🔻
🔻
گفته می شود نیمکت نشینی عالیشاه مقابل چادرملو ریشه در دخالت مدیران داشته است.
🔻
🔻
برخلاف اخبار منتشره امید عالیشاه، در لیست مازاد اوسمار ویرا نبوده و عدم حضورش در ترکیب اصلی و بازی گرفتن از او در دقیقه ۸۰ ، عجیب…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134612" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134611" target="_blank">📅 22:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
خدا لعنت کنه بازیکنان بی غیرت مارو که حذف شدن وگرنه امشب قهرمانی سه جانبه ما بود و رفتن به سطح دو آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134610" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
پایان 90 دقیقه بازی چادرملو 0 _ 0 گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134609" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlaxdOt42LeSqLAv0UxQ7I73fcsl0rVc7ZyS_xOUtcxDl8Fw8f_Kydh4PKc3Pkxeuy6CJ1HhCT1MD0R4wIlX1nyEGUOKLyrPY-laYCWGTY7n2t-3dC5krB1Ckrp_Q2XGttVXsFTfGsttdCwqwASXL3fIKS2umkG7VfKOLa4uV2zZq2IJ6AF29qI4-wLbRdqF4vNiccRPwjsUce0RTG9MsO8mXDt4Lc7zH9qEUyBBANxPEqTCf2Ng8j_0xOqRoYiicT1trX4b1G7ljU_MoBx2rvcM9XglLbUo2AJG4ghXBRjiOEZmqWNd70R7VcZPialpGE2DDnbgCN1UoUEEYQW0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل قاسمی دومین گلزن و بهترین پاسور امیدهای کشور و ذوب‌آهن به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134608" target="_blank">📅 21:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔖
🔖
تیم‌های چادرملو و گل‌گهر سیرجان امروز ساعت ۱۹ به مصاف یکدیگر می‌روند تا سهمیه سوم فوتبال ایران در لیگ آسیایی مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134607" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134606">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134606" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134605">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
آقای قلعه نوعی .یاد بگیر از ژاپن ...بدون اما و اگر صعود کرد و نیمه اولم از برزیل برده بازی و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134605" target="_blank">📅 21:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134604">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134604" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134603">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134603" target="_blank">📅 20:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134602">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
زیبا‌ترین گل‌های جام‌جهانی 2026 تا پایان مرحله گروهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134602" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134601" target="_blank">📅 18:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🤩
🤩
🤩
گفته می‌شود مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کند تا طرفین برای جدایی به توافق برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134600" target="_blank">📅 18:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134598">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6_dZhfJ1mBRKBR369itr8XxWBO-hRuxHZX_Pr4_mKck50qRF4dLc3x0if9KxNqZAeHe5-2FLuo-TI1EBRIdiTg6sNZ3xpqB284R5QNpwULdPZjkJSH_HFbzLV2nm7RRJIRCzb_HF8GFNpKmu1Fhq7VYcK0binSkpl9s9xWwzHWpHAARydDjctUi6I288in1AIMySWYF8ncqhVyrZ1AB7HwZGAztueNXeuDZjInxwwThkFZuQ7_Tie3b3cLZW2Xm17oT08zObreNp1TSm2cINWWZR0spNAwQwcsbc9oOUdiEkeUPGW6KfgfBtrq4eI8WSRdt2GBD7-M7w1BPaRH8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته فرهیختگان، باشگاه برنامه ای برای تمدید قرارداد علیرضا رفیعی نداره و این بازیکن بزودی از پرسپولیس جدا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134598" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/134597" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134596" target="_blank">📅 16:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
❗️
میلاد محمدی ظاهراً دوست داره برگرده یونان. از اون طرف، مدیران باشگاه هم خیلی تمایلی به تمدید ندارن و دنبال جذب رزاق‌پور هستن اما اسکوچیچ به سبک بازی محمدی علاقه دارد و شاید با توجه به پافشاری سرمربی مدیران باشگاه راه چاره‌ای جز مصالحه با میلاد نداشته…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/134595" target="_blank">📅 15:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134594" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
غیر رسمی: اسکوچیچ فردا بعنوان سرمربی پرسپولیس رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134593" target="_blank">📅 15:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJrsLpSdNZtMMNF22C-s53uV87BvQwYjeqpbyeZWQ2PsIMS7azVvfe8GOCoqDGiftcYJaI7PJ9NVcDAhi0m3vy2bZYYUx4vmGeQbahfZnGNwn6fnG8lqRMTSTdoOACuhJqsRIgHUMJPaxWhz_YY-Pm3jBlTK-iI5Azx1MhpFiKwJIOkGin8qz0vDDcXQqywq5XZDX2spI5D6FcdAGVUj4Wq4hvr563E5HH0KTLC7EgTcjVArALJP5xTAu9fR1boCNlJl7ft4obaqkL8EGp5Wl1x4xEyEnUyUu2dBJ8_CaohaIsMrNO1udIfe9fUGo4as8EAs8ipK8ylGN7F1GPLaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عینک مخصوص حذف از جام جهانی ۴۸ تیمه فقط ۱۳۴ هزار تومن :)))
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134592" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134591" target="_blank">📅 15:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134589">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
تراکتور بعد از دانشگر و محمد مهدی محبی اینبار رضا غندی پور هم جذب کرد ..امیدوارم باشگاه برای جذب بازیکن دیر اقدام نکنه ...چون بازیکن خوب روی زمین نمی‌مونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/134589" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
