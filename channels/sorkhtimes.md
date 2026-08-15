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
<img src="https://cdn4.telesco.pe/file/ZyQ-8UIjjarU2Dpxih-D7j1gGTPTuTe6Fuhg8MCLkiZ0GIikuuPjQsAmEM7YeOJqqRQ63sgLxqAIR7HbjJ3P79a17iStAv1RPfDiKsaA59qiB5Rfo4MUYNSGuwOH7IP90cm53dE58GZPXOCSgnNB1S9Uxqe4BS2EpyINrsIDr35knl3zNzGy_MOz-lYGihIdLMZCOmsoZDN5BCDYFdT52PeEkjsa7URGXgRfds5b4hNlCo7Ftvpv-glw16Jc2ancNiwuTMxPyJk-LuPP1AXk6WLQuzWb44jxU_DwdGFLAfmiySV7op_wy2RT8hN1Y5QSKQvwIx88wjR0M36h2EraKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 09:17:54</div>
<hr>

<div class="tg-post" id="msg-138174">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💢
💢
💢
شایعات؛ امیر جعفری مدافع چپ گلگهر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/SorkhTimes/138174" target="_blank">📅 09:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🔴
صبح روزی که عشق بازی داره بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/SorkhTimes/138173" target="_blank">📅 08:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLshJqSCzzUiwqP9H14D0kNTgjBZ22nlrw-BBnFm0k7jzPcD4HdJc2NCcmmR1U4QCQIfUS8w3iLyqR6J9k0zBmTg-6LBghnPdwgYJ8jn6PQ_jCSTCkXjl9xkkpDym85XHVpMLr6DjLGYh3e2lk0UAiuRZ5FPKeUNd-WFqVyqGz74STggIXQX2gxNBtXYssTfELyfCpc-WIWtu4Kwm5MOBCeQRNSqfWySVK-HX-881IP5PWKSIJAP-repvfJ0Mq1U4n-TAC8C0LBMVjP44oR5IkS5iQTnGg8IEOh6LWhpmwdZqh3HjmOOO2GhSPXt86M_drdamS7UaiJpRjw_t3h5kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/138172" target="_blank">📅 02:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💢
💢
💢
💢
مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ رو بالا ببرند.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/138171" target="_blank">📅 01:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔄
🔄
❌
شایعه شده که پرسپولیس قرارداد یکی از خرید ها رو ثبت نکرده تا به عنوان سهمیه آزاد بتونه قراردادش رو ثبت کنه.
❌
میگن این بازیکن تو گل‌گهر بوده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/138170" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
با خرید امیر جعفری سهمیه خرید پر میشه ولی .....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/138169" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
گفته میشه که کارت بازی همه بازیکنان پرسپولیس صادر شده و پرسپولیس تنها میتواند یک خرید دیگر داشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/138168" target="_blank">📅 00:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138167">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
یک روز مانده به بازی بازم ترکیب تیم لو نرفته و کاملا مشخصه جاسوس شناسی شده بعد از سالها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/138167" target="_blank">📅 00:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138166">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
یک اتفاق جالب در بازی دیروز سرخپوشان
👍
در چند دیدار دوستانه اخیر شاهد لو رفتن ترکیب سرخ‌ها پیش از بازی بودیم، اما دیروز ورق برگشت و هیچ رسانه‌ای نتوانست ترکیب اختصاصی تیم را پیش از بازی منتشر کند. به نظر می‌رسد مهدی تارتار به وعده‌اش عمل کرده و پس از…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138166" target="_blank">📅 00:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138165">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
ترامپ: ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم چون سربازان امریکایی را کشته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/138165" target="_blank">📅 00:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138164">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
امیر جعفری که گفته می‌شود بازیکن مدنظر پرسپولیس است بر روی بیو خود قلب قرمز گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/138164" target="_blank">📅 00:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138163">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
عضو مستعفی هیئت مدیره استقلال به صراحت اعلام کرده نامه فسخ یاسر آسانی پخش شده و بازی کردن او غیرقانونی است.
❌
❌
تیم‌های لیگی با شکایت به AFC و FIFA می‌توانند این تخلف را گزارش دهند و نتایج خود را جلوی استقلال ۳-۰ کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138163" target="_blank">📅 23:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138162">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
به امید اینکه با این کیت قشنگ ؛ خاطرات و لحظات خوبی رو تو ذهن و تاریخمون هک کنیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/138162" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138161">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQS_05EZ6ZgWZav709Xq_DsEkHyJM00Qdt-kLWv54yltUwj73sF3mySr2brjimp7x2SLMSQIIW6l__4JBHoJCMEb4MXyW2ecsr7UpKD2knKISKaJSLdY1AhFd2nRUVHzO56oO5KJXAsWlx-YD94XbFMwYlxqEO3BxPyTZ8Atx_Dgjw6dSxwDMJ6Cx4FkvTcjCtked4vPiHzlLhJbkl4627xRwppEyDuHBkOxIXmiZQDsbxwWX4-0EKMNbmhbqINvVfjmJ_GQ5xCH9piUzJ-FhDv0DyZsK6EbZbk778I3mcOz_F1NT_y6MsT-PYrHMPRhWkk0wQC2-s6JIYvD8Xx-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
امیر جعفری که گفته می‌شود بازیکن مدنظر پرسپولیس است بر روی بیو خود قلب قرمز گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138161" target="_blank">📅 23:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138160">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
بازی کردن آسانی تخلف است
🔴
هیأت‌مدیره استقلال اقرار کرد فسخ یک‌طرفه آسانی بطور قطع انجام گرفته و قادر به‌‌بازی نیست‌. مس شهربابک بعدبازی بدون فوت‌وقت شکایت برای ٣ بر صفر کنند‌. شرایط جنگی و اولویت نبودن فوتبال برای مردم نباید باعت چشم بستن تیم‌ها به این جرم…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138160" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fea0075aa.mp4?token=Ix6KWrVuK0o1n_8tkD8IAExRkAraqryhujpPV0SFzPcJF4fhJ2UK9JqmQetj1tXNAn-f331kUP_SL3h1QpT4dzGeZ6VoOZpqT_WZx_7Ct0TceXMiY8WFx-s9--2riWAKXdY0bdwV9yyMmfAWHngYn0_eqOQNbqXWmP2ZBAox5TjEuvhUw75II00ZgjAWoalK0SBj53jvMm6MxvhhDmQjhLAlD8N2AezWrwYcYct3pADRG1pWG0jm_fqyVNAig0DZcs1Ww42NoovjIhhMXGPr5a7xtcfIRFtjXe_gHVi3if_iNMsQOJaXuGY1FdgdXWHR639QJH-olUaBAwznIpoUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fea0075aa.mp4?token=Ix6KWrVuK0o1n_8tkD8IAExRkAraqryhujpPV0SFzPcJF4fhJ2UK9JqmQetj1tXNAn-f331kUP_SL3h1QpT4dzGeZ6VoOZpqT_WZx_7Ct0TceXMiY8WFx-s9--2riWAKXdY0bdwV9yyMmfAWHngYn0_eqOQNbqXWmP2ZBAox5TjEuvhUw75II00ZgjAWoalK0SBj53jvMm6MxvhhDmQjhLAlD8N2AezWrwYcYct3pADRG1pWG0jm_fqyVNAig0DZcs1Ww42NoovjIhhMXGPr5a7xtcfIRFtjXe_gHVi3if_iNMsQOJaXuGY1FdgdXWHR639QJH-olUaBAwznIpoUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازی کردن آسانی تخلف است
🔴
هیأت‌مدیره استقلال اقرار کرد فسخ یک‌طرفه آسانی بطور قطع انجام گرفته و قادر به‌‌بازی نیست‌. مس شهربابک بعدبازی بدون فوت‌وقت شکایت برای ٣ بر صفر کنند‌. شرایط جنگی و اولویت نبودن فوتبال برای مردم نباید باعت چشم بستن تیم‌ها به این جرم استقلال بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/138159" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
قدوسی: 24 ساعت مهم برای قربانی در پیش داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138158" target="_blank">📅 23:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138157" target="_blank">📅 22:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhYcY3DavZSVr9hYcXCv5MCJ3iy_Pa3eKfvqOupyWiWZo4iKuFRSEZizeYTD_VKT6uBOxa-HeTdCZ43ahERu-E6NZtBNiOzE2g3DOPxD4Cl-X9PFLChr656wAlXYr0FYWTo33cw-Ti2cIitOHL9mWscCy45mU-jjTEEaELuq53EytlFyodVrYIjtxGjS9d9SXiqPoQst0KfEKMx3_n9Wu_V-SN64Qvc0sEm6L4i_dPABkRtnC7vXu6iwbvSujK52CVLd9AX0GGE0X-JVZ-CHzWwEEcxwcuiLr_rgHUs64xx6tBKuQfUUwZmTYMHeB37ZsLDnx9lkz7JDgG07vt52XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
زیباترین کیت 5 فصل اخیر از نظر شما؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138156" target="_blank">📅 22:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138155">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138155" target="_blank">📅 22:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138154">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
خطاب به مدیران باشگاه مس شهر بابک: یاسر آسانی طبق گفته ی خود عضو سابق هیات مدیره باشگاه استقلال، کارشناسان و قانون واضح فیفا، امکان عقد مجدد قرارداد با استقلال و نداشته و غیر قانونی بازی کرده است.
🔹
منتظر شکایت این باشگاه هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138154" target="_blank">📅 22:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138153">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138153" target="_blank">📅 22:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138152">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf45d8651.mp4?token=jcoGi8iQKUpdGoEKea1tNoLolXZsvC0KV5XvfnnVTKY5qPQmFIK_f0eu98631NdxT3m80F3_7LhZoxIVrD-82hCPAJT514BW9L7HjDkgrPrVK1duhTweJnH2dk0v6yaG9GkQglnARHYvoydl8Y-biu3XJaRnWMo4CTZd2Y77wIQbwHO0MOpfYlGKVChqN0yjn8jJolNXl8BD3hrg4U6yH9af7nTjjwMpuK7LcDc412izAngOMfKKg_myaIyoGxdujRv3hxgIy1o-MI7n3OuxvJ9cwWz7ib5LNCd5DjWkDptUBAXa2mxCLx1nNJSnU255kJzA9kICT-hhvqSx-jUg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf45d8651.mp4?token=jcoGi8iQKUpdGoEKea1tNoLolXZsvC0KV5XvfnnVTKY5qPQmFIK_f0eu98631NdxT3m80F3_7LhZoxIVrD-82hCPAJT514BW9L7HjDkgrPrVK1duhTweJnH2dk0v6yaG9GkQglnARHYvoydl8Y-biu3XJaRnWMo4CTZd2Y77wIQbwHO0MOpfYlGKVChqN0yjn8jJolNXl8BD3hrg4U6yH9af7nTjjwMpuK7LcDc412izAngOMfKKg_myaIyoGxdujRv3hxgIy1o-MI7n3OuxvJ9cwWz7ib5LNCd5DjWkDptUBAXa2mxCLx1nNJSnU255kJzA9kICT-hhvqSx-jUg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
500 تا دیگه رفت رو رضایتنامه؛ گلزنی محمد قربانی برای الوحده که داغ دل تراکتوری ها و پرسپولیسی هارو تازه کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138152" target="_blank">📅 22:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138151">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
چیه این پرسپولیس ..
❌
محمد قربانی بعد ورود به زمین گل زد برای تیمش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138151" target="_blank">📅 22:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138150">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
محمد قربانی روی نیمکت الوحده قرارداد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138150" target="_blank">📅 22:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138149">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
مدیران مس شهربابک قصد دارند که درصورت بازی کردن یاسر آسانی مقابل این تیم در هفته اول لیگ برتر بلافاصله از تیم استقلال شکایت کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes  پپ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138149" target="_blank">📅 21:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138148">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔄
🔄
فووووووووووووری
🚨
امیر جعفری مدافع چپ گل گهر سیرجان از لیست این تیم برای بازی امشب این تیم خط خورد تا شایعات جدایی و پیوستنش به پرسپولیس قوت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138148" target="_blank">📅 21:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138147">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
اتاق فرمان میگن که سانسورچی خوابش برده ندیده جوراب با لوگو مجیده باشگاه ویدیو رو پاک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138147" target="_blank">📅 21:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138146">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🟥
✔️
کیت رسما رونمایی شد
⚡️
الله الله چه کیتی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138146" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138145">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
کیسه سومی هم زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138145" target="_blank">📅 21:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138144">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
استقلال دو گل تا دقیقه 60 به مس شهر بابک زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138144" target="_blank">📅 21:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✖️
✖️
مهدی ترابی از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان دیدار هفته سوم با پرسپولیس در یادگار تبریز رو از دست داد.
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138143" target="_blank">📅 21:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138142">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138142" target="_blank">📅 21:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138141">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138141" target="_blank">📅 21:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138140">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
استقلال دو گل تا دقیقه 60 به مس شهر بابک زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138140" target="_blank">📅 21:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138139">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=Vd0yEqrJTokDDkKb4f21zoENDckjDTHu78MijrU9oj2v7A8bV3fGAhtq5uelko3BX_R668iBqKD6UNvPCjLIcuEN-VJOec3z5XFPWTjQDEqOgfTY57zOCMeRo7hp-CbotL8Ws8ePpbhcCoIzoMQVp95cnRNF4hUJgavVrV-vB1nLa-op8-i_aY3Pbw3w46hN6TuV241ce_2w_PnLkDAkiSWgGK7mXN7BeFDNiS-MauQ3KxEBqkrm1GELhntQS3160OLnu5E5xPYKb0KRLcvjdebyDOfKRDpEhwTZysQ3pw-aDXU03GnhuSOyuTl8u4oBG4_UaEqbBzpfLzAn9kkqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=Vd0yEqrJTokDDkKb4f21zoENDckjDTHu78MijrU9oj2v7A8bV3fGAhtq5uelko3BX_R668iBqKD6UNvPCjLIcuEN-VJOec3z5XFPWTjQDEqOgfTY57zOCMeRo7hp-CbotL8Ws8ePpbhcCoIzoMQVp95cnRNF4hUJgavVrV-vB1nLa-op8-i_aY3Pbw3w46hN6TuV241ce_2w_PnLkDAkiSWgGK7mXN7BeFDNiS-MauQ3KxEBqkrm1GELhntQS3160OLnu5E5xPYKb0KRLcvjdebyDOfKRDpEhwTZysQ3pw-aDXU03GnhuSOyuTl8u4oBG4_UaEqbBzpfLzAn9kkqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
✔️
کیت رسما رونمایی شد
⚡️
الله الله چه کیتی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138139" target="_blank">📅 21:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138138">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
چمن قلعه حسن خان خیلی افتضاح هست امسال بازی های خانگی سختی داریم
🤦‍♂
چمن داغونه
🔄
🔄
پ.ن یکساله معلوم نیست چرا این چمن و به دادش نرسیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138138" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
✅
مهدی تارتار: یکی دو خرید دیگر داریم که امیدوارم طی روزهای آینده نهایی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138137" target="_blank">📅 19:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138136">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138136" target="_blank">📅 19:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138135">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
نشست خبری مهدی تارتار، پیش از دیدار با شمس آذر ( بخش دوم )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138135" target="_blank">📅 19:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138134">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b464aa2d22.mp4?token=iOiegAyQv1Lo9CHBbRFPuBWCFnGNyqaIyVKOcuduNaY1Px0WP5j5-hFsdC8Mn-Fqfu8RGeJ8UgX953BjKcIgRhUiJh6ndVojvnlPOkR3u8Rf4-Sc--Gu46q76js9y_qh2n8T_kutt71UmmmtRvfJRGhkGgCRJr1zzTwp820VturX7zXddo_O9fxp7bxSjpF-D2do5Q65ZZlRJIG34aQMII9J-Firffj3W7vRsFvw6m2TktL8nmPeKbJJxk4mgEuRY8py9Px_df_Y-XLvGtLBZWi7SiGwbgFfmVOBqe5iJUFhxZuW0451OQ-JBuOCSCvZ_a_TVuHH-z0-DHhiSdEAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b464aa2d22.mp4?token=iOiegAyQv1Lo9CHBbRFPuBWCFnGNyqaIyVKOcuduNaY1Px0WP5j5-hFsdC8Mn-Fqfu8RGeJ8UgX953BjKcIgRhUiJh6ndVojvnlPOkR3u8Rf4-Sc--Gu46q76js9y_qh2n8T_kutt71UmmmtRvfJRGhkGgCRJr1zzTwp820VturX7zXddo_O9fxp7bxSjpF-D2do5Q65ZZlRJIG34aQMII9J-Firffj3W7vRsFvw6m2TktL8nmPeKbJJxk4mgEuRY8py9Px_df_Y-XLvGtLBZWi7SiGwbgFfmVOBqe5iJUFhxZuW0451OQ-JBuOCSCvZ_a_TVuHH-z0-DHhiSdEAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
وضعیت عجیب در بازی فجرسپاسی و خیبر خرم آباد
✔️
پ.ن چرا ابرها تو زمین هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138134" target="_blank">📅 19:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138133">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20949bf60a.mp4?token=eRckvYoD7q7CjoSJtI1BV4MxUb5sYKW2I7a-wsL26WSUqORuuS8CZOvEybuoxL8-LPZ5BHrFRfHWnmQdof_m7-W2QncI7K8q34-NT1whYiFMJhLBLfi1fi4xpHs_QPplmy0wu01Ahl8UungZyGyPIq8aXLoinqLGkX3C6UK9OC3aJVOeHRqoQAYSsHYSfFeKNtHvLd0ofXke0D_p_IwczxVk673X9guDFS96Z2ixNQYRq1xrr2vKpBnqkvAm-BLhALQHUmvYlPuBzio6q7AFJql0VpmORImoKnN-RzJChjLol4VNXzFRUZHo2xzgjVl46HXN1vcGnJH_NqUygcldtY8kzDIyD2hdVHrUw696wkr9Q497M1dPNY44d92C7ji3NAu-L4KXe7o5GTz3rDJAxGAWdkXqsCccM0Q2F935x60KKROaUjPsvuvFIcS7ad0AG3-IkcEPwkxDAzl_lBrEdKkrT5LG5xsopoWsnteTudkb69E-ahXAqxXTBkRl4nLBxgF8I349uUtRWKoEHGRkRp-zCeUu6bZDt1WIXaalL96ekPt4bWXZZXOIEbPO5ffjIdT1JXruwd5zGnJpC15Oa6Z00_iEKwj4cyGtH3t1mfTpFCfFZ7BMnc1qODIJ73RoejNVixe_xntOyWsV2NtAhnx1UYo63ePOKpTvezOe3T4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20949bf60a.mp4?token=eRckvYoD7q7CjoSJtI1BV4MxUb5sYKW2I7a-wsL26WSUqORuuS8CZOvEybuoxL8-LPZ5BHrFRfHWnmQdof_m7-W2QncI7K8q34-NT1whYiFMJhLBLfi1fi4xpHs_QPplmy0wu01Ahl8UungZyGyPIq8aXLoinqLGkX3C6UK9OC3aJVOeHRqoQAYSsHYSfFeKNtHvLd0ofXke0D_p_IwczxVk673X9guDFS96Z2ixNQYRq1xrr2vKpBnqkvAm-BLhALQHUmvYlPuBzio6q7AFJql0VpmORImoKnN-RzJChjLol4VNXzFRUZHo2xzgjVl46HXN1vcGnJH_NqUygcldtY8kzDIyD2hdVHrUw696wkr9Q497M1dPNY44d92C7ji3NAu-L4KXe7o5GTz3rDJAxGAWdkXqsCccM0Q2F935x60KKROaUjPsvuvFIcS7ad0AG3-IkcEPwkxDAzl_lBrEdKkrT5LG5xsopoWsnteTudkb69E-ahXAqxXTBkRl4nLBxgF8I349uUtRWKoEHGRkRp-zCeUu6bZDt1WIXaalL96ekPt4bWXZZXOIEbPO5ffjIdT1JXruwd5zGnJpC15Oa6Z00_iEKwj4cyGtH3t1mfTpFCfFZ7BMnc1qODIJ73RoejNVixe_xntOyWsV2NtAhnx1UYo63ePOKpTvezOe3T4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نشست خبری مهدی تارتار، پیش از دیدار با شمس آذر ( بخش دوم )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138133" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138132">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
نشست خبری مهدی تارتار، پیش از دیدار با شمس آذر ( بخش اول )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138132" target="_blank">📅 19:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
اخراج عجیب نیما احمدی از پیکان پس از VAR طولانی در بازی با تراکتور تبریز
پ.ن از هفته اول داوری به نفع تراکتور آغاز شده ...کجاش اخراج داشت و طرف تک به تک میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138131" target="_blank">📅 19:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
فوری از طرفداری
🔴
امیر جعفری دفاع چپ گل‌گهر ممکنه همزمان با جذب دانیال ایری به عنوان خرید جدید پرسپولیس معرفی بشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138130" target="_blank">📅 19:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
قدوسی: 24 ساعت مهم برای قربانی در پیش داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138129" target="_blank">📅 19:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a058c3af3.mp4?token=KYYj6wbRw3ErvccZ1KUtPlqqDH9yInbO0hhsLNfvQmpmaTXxMr274HR7mNzFyoQ9J2rAld0Vm94m8fyzMr-Ngqa1z_Os-VSRLCMCc0uzzoZ1PGwyeNjCsG2EfzT-IEFqOgJAES4J_wrWkn2Y-xIWAkKId-1tDdgfEC_OqCjPYRkYPproXUQuXkbWf0sVPNP2QQgd-qHMNJ-i2ozkBRREM5MTtcr03AWHQRD8joHqUsBBK4KgBEu9LygdzggJcjBh7x9IeRTKqi93xu_Px0tlBipUzMOhAIthzeXXsn9PQ-Lzmg6aGP20L5dZ5deINx9Oz7aV-3KhGeu8cHHlf0R53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a058c3af3.mp4?token=KYYj6wbRw3ErvccZ1KUtPlqqDH9yInbO0hhsLNfvQmpmaTXxMr274HR7mNzFyoQ9J2rAld0Vm94m8fyzMr-Ngqa1z_Os-VSRLCMCc0uzzoZ1PGwyeNjCsG2EfzT-IEFqOgJAES4J_wrWkn2Y-xIWAkKId-1tDdgfEC_OqCjPYRkYPproXUQuXkbWf0sVPNP2QQgd-qHMNJ-i2ozkBRREM5MTtcr03AWHQRD8joHqUsBBK4KgBEu9LygdzggJcjBh7x9IeRTKqi93xu_Px0tlBipUzMOhAIthzeXXsn9PQ-Lzmg6aGP20L5dZ5deINx9Oz7aV-3KhGeu8cHHlf0R53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل دوم تراکتور به پیکان (دبل شهریار مغانلو) در دقیقه (45+6)
تراکتور دو - صفر پیکان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138128" target="_blank">📅 19:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgY0udxA9vOsxLnCwNsV0FUM0BY3ndMpUxmnT1q7aVPzrwV6ivJbh7Csbh8WD9UnMIEW1OS0RBokYgO6cvC2cVPgcrb1qsuzEYexpctRI_kHrjuaIWstp4X_0nAzjrn5uipaJOWdJE3VKCQohH8YbCUzKDH0gcSr4oPExeK3iOULTFiyUDNs3J_BAFntw2wd-jMDyuTWAr-Io44dCq8o6HQ79cycdk_6K1nMH6JgtNRaKYZyKZsnwmtMp7x_OHiYV8pa41h4Sn-ojzwunGR6SEIzjSyj2LRW46aLgIIobIMFhzlzgboTSwfGtv2G8gKwabVbOEOn4LwbEJhfLp4ygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏅
شروع طوفانی لیگ برتر؛ هفته اول با چند نبرد حساس
🏅
هفته‌اول با بازی‌های نسبتا نزدیک و غیرقابل‌ پیش‌بینی شروع می‌شود؛ تیم‌ها هنوز به فرم ایده‌آل نرسیده‌اند و غافلگیری کاملاً محتمل است. تراکتور و استقلال مدعیان اصلی برد هستند، اما تقابل‌های خیبر با فجر، فولاد با استقلال خوزستان و چادرملو با سپاهان می‌توانند جذاب و نزدیک دنبال شوند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138127" target="_blank">📅 19:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✖️
✖️
مهدی ترابی از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان دیدار هفته سوم با پرسپولیس در یادگار تبریز رو از دست داد.
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138126" target="_blank">📅 18:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1831581867.mp4?token=u3EP5ZSd8Vu60Ewu-Ixg7x8FsQZiYbNTKk-enh5MuU5GoWNHoK5jiO7VI_3X5cMA66OdGzxOZ8R7uKVzZRGVH4PwkZ6k6pUO4ziSjAF1Mhsm72VsBkwmi_cskYJbszvgiFqJ3amIhi7iyG4UYLIkIjPmXYxfCQHKy6_hc3j2VnCFqUAZgWu4bPLPEIPT9a_IbDVIMDmRNCGLTcoydQpJn1RZof8IZOOXfhuGjzWTXTu6RaIURMf0zFXEE6VPZQKz2D0e5nlW7D9CVoWRvt4S7ymxtFdL04KIs9Ph9H36os8mchJwNiIMAXLZRaKE48V-WbtIlVRbxk4EV3f9c_3piw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1831581867.mp4?token=u3EP5ZSd8Vu60Ewu-Ixg7x8FsQZiYbNTKk-enh5MuU5GoWNHoK5jiO7VI_3X5cMA66OdGzxOZ8R7uKVzZRGVH4PwkZ6k6pUO4ziSjAF1Mhsm72VsBkwmi_cskYJbszvgiFqJ3amIhi7iyG4UYLIkIjPmXYxfCQHKy6_hc3j2VnCFqUAZgWu4bPLPEIPT9a_IbDVIMDmRNCGLTcoydQpJn1RZof8IZOOXfhuGjzWTXTu6RaIURMf0zFXEE6VPZQKz2D0e5nlW7D9CVoWRvt4S7ymxtFdL04KIs9Ph9H36os8mchJwNiIMAXLZRaKE48V-WbtIlVRbxk4EV3f9c_3piw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اولین گل فصل؛
⚽️
⚽️
⚽️
گل اول تراکتور به پیکان توسط شهریار مغانلو در دقیقه ۳۴
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138125" target="_blank">📅 18:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
گزارش خبرگزاری ایسنا : حمایت از بیرو و توهین به علی دایی توسط هواداران تراکتور!
🗣
پ.ن بیشرف های تراکتوری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138124" target="_blank">📅 18:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138123" target="_blank">📅 18:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
گزارش خبرگزاری ایسنا : حمایت از بیرو و توهین به علی دایی توسط هواداران تراکتور!
🗣
پ.ن بیشرف های تراکتوری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/138122" target="_blank">📅 18:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8c8204fa.mp4?token=Txkk7uJf_1HbP7PA-msOTuHHZtmhauF_x-RlQLlb-ai1JJiDngWgNzfzOJDETCBjYyVC-hLBANS7edpNbWeSVa4abAjqTavXhye6XFelEWrhWtvh2Ons83EhGCcjM7aleh9wQRyA7FmJcyBvky7J2nZ5lwnyz2EnZgjUVAgHiYrLzoNr1PdvzE5Z7MJnmtID9qw1DAxmIRraknzHNsWBAu8RR3vQeQu7nFuHJnyfkCak87GuP8yFNlUcwQOYKNqymWE_RQicXXC20_j0IWyiodOL3aOnRP_084elnCuXvZf9988tOZMhxS4rLwgE38cVUYe4oh90S5TDLBl42tLW0A2tLNWVeSHJggnonRL55gm01rgUfE87MAFvGcnBK407Qf6h7ANiiZwyLXT0NpK_UxyrTDZN_5p3pOSXXnbqabG-SdZTEkoHWXzs40z3BSAMuGWWSTSb44x2FGz4Ht4sxoEbRo4_-rJsDkeB8_uLe0gOc31x1JQaRes-aC8XblYhO0l-KHBFFpuqEgKNiuBe9bfhR-Rp6apKc09CWtDyvjP5NW810OakVKaGJoRgSLj4YFFDrhjcw2GEavo5PMABhoO6j2VHviRdyyD4acyPbK9UbyzMZ3Y47EKjpjxd29BwhM5h7bOg3_w1VKnTRO-_3ariU1fsgBYS3lejyPUYM_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8c8204fa.mp4?token=Txkk7uJf_1HbP7PA-msOTuHHZtmhauF_x-RlQLlb-ai1JJiDngWgNzfzOJDETCBjYyVC-hLBANS7edpNbWeSVa4abAjqTavXhye6XFelEWrhWtvh2Ons83EhGCcjM7aleh9wQRyA7FmJcyBvky7J2nZ5lwnyz2EnZgjUVAgHiYrLzoNr1PdvzE5Z7MJnmtID9qw1DAxmIRraknzHNsWBAu8RR3vQeQu7nFuHJnyfkCak87GuP8yFNlUcwQOYKNqymWE_RQicXXC20_j0IWyiodOL3aOnRP_084elnCuXvZf9988tOZMhxS4rLwgE38cVUYe4oh90S5TDLBl42tLW0A2tLNWVeSHJggnonRL55gm01rgUfE87MAFvGcnBK407Qf6h7ANiiZwyLXT0NpK_UxyrTDZN_5p3pOSXXnbqabG-SdZTEkoHWXzs40z3BSAMuGWWSTSb44x2FGz4Ht4sxoEbRo4_-rJsDkeB8_uLe0gOc31x1JQaRes-aC8XblYhO0l-KHBFFpuqEgKNiuBe9bfhR-Rp6apKc09CWtDyvjP5NW810OakVKaGJoRgSLj4YFFDrhjcw2GEavo5PMABhoO6j2VHviRdyyD4acyPbK9UbyzMZ3Y47EKjpjxd29BwhM5h7bOg3_w1VKnTRO-_3ariU1fsgBYS3lejyPUYM_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گزارش خبرگزاری ایسنا : حمایت از بیرو و توهین به علی دایی توسط هواداران تراکتور!
🗣
پ.ن بیشرف های تراکتوری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138121" target="_blank">📅 17:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47968981a0.mp4?token=gM1XoQU7z23vgM_aFwtDqVuEO9VbBE3AjgDY1QNxdHv20URjnHYotEKX95tNDujUA9x7LuzVP7LypVnBHm_nshcdJy2XdPJ6oBh9EqjCd336txADw134pwripSBf8bNFBtAC40RbKzPYFIvvuM4Qlh3Uy_5EGPFKKTnzyM81NLXiDVsEE3IG9lpvZgdxG7qXrMULSoSkFwrRN9DYiNeGTV_WCAZRYptaRgL_NGQMMJQNcGiGpbu2RRU-O3VJJP-gdPI2KBmvqGpkkMu1i0Qy8brCv4e3k4ICJx5Dh-anbMJrd61N84Neo1KcEtnkqLTCD7nE52sb4XIIS8CxV_0d4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47968981a0.mp4?token=gM1XoQU7z23vgM_aFwtDqVuEO9VbBE3AjgDY1QNxdHv20URjnHYotEKX95tNDujUA9x7LuzVP7LypVnBHm_nshcdJy2XdPJ6oBh9EqjCd336txADw134pwripSBf8bNFBtAC40RbKzPYFIvvuM4Qlh3Uy_5EGPFKKTnzyM81NLXiDVsEE3IG9lpvZgdxG7qXrMULSoSkFwrRN9DYiNeGTV_WCAZRYptaRgL_NGQMMJQNcGiGpbu2RRU-O3VJJP-gdPI2KBmvqGpkkMu1i0Qy8brCv4e3k4ICJx5Dh-anbMJrd61N84Neo1KcEtnkqLTCD7nE52sb4XIIS8CxV_0d4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
هوادار استقلال رید رو رامین رضاییان
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138120" target="_blank">📅 17:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❤️
📸
قابی از یک تیم و یک هدف؛ آماده برای شروعی قدرتمند در لیگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138119" target="_blank">📅 17:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9bcfqERLctLi9J-xThVwILRTHMAfaSsXKN1H5UIvoYcECPkGh3YRZQeSJqbwGZ28xMnlSB1trfyq84uKRhoJziOmgHoa8VYydtsBaaFwAfxVqR8OxvHcyXU4HA8CDqGVaquT1zUjHKoYZorFNG1FEy9TR7gGdDQIoo4HUqtlkSSK4rkV3-27Tv08kWUR-lD9GHnH0MIczctVfRcTqRbNtfudQHLEiSD1Fk7DwmFM4W4lI_dgiTIrdKSStyuMBb1tGVb15DOSoPGMxvs4tP9kjf-aJbozTPfIrkEORDuvg4-DPueR4BHrkfWoLUijGYK5T4H5wp4v2yf_X5KQnRMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
قابی از یک تیم و یک هدف؛ آماده برای شروعی قدرتمند در لیگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/138118" target="_blank">📅 17:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138116">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🏅
برنامه بازی ها فردا لیگ برتر؛
🏅
تراکتور _
🏅
پیکان 18:00
🏅
استقلال_
🥇
مس شهر بابک 19:30
🏅
خیبر_
🏅
فجر سپاسی 19:30
🏅
استقلال،خ_
🏅
آلمینیوم 20:00
🏅
سپاهان_
🏅
چادرملو 20:00
🏅
گل گهر_
🥇
نساجی 20:15
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138116" target="_blank">📅 17:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138115">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5528ddd2d1.mp4?token=g5a9RphNUw-Gne7TITCPSUowNVfHnRdI9qlx5PTCiYSE7QQb4nj8qknJtHnZbqweEBfnNhszpuFQsNxt6p2Nw6XKzdaJCxdcv1jB_shqOuu4DA8OXJ0TCepoJM2USlD1uqynawlH34MbWmwtdf_AOEqalMOIVsuphsAMXYc0aFo6fz4C3gDmBhzpCuFtdbvfbbT2dSjiieHBGWzzYP493EjFdB6txSNMIYx5q2YSMVTWvph-t0rNIw3HLQ3Fd1JIAireyFlxX_jzxyqGCNYgm45ZvYsjEoEg3twbH2TgJaXibgSDVrxobNbxvHWvfs0KmF6yF6FX02e2Tlvi0Vqb_XVFQ7Sn-Ag9ZioFfsHkJ_OSL7onWmnnyZHWYQ_9autjHa1yQ4U9kvLIy7FO39vhPbvPjejoMp3B3xyU0RtgSxpQylmyYk24ZW-9gyYC4zZ2US-zOIlEa83H7kQ-dFCdXIpP4PNFGitPDWERiDBNNQ8QSbdmRVCgklJU6jTsjhwKUG9cUDtrfVqF9Al-YlgOIcLnR7zztRK3TGAxUnPCBX9Uw8SvMT96YguvxG5KOz0QLx2ff2wSCjzj_0xX5-bqtM8DD72MYyBXqKpE65gdfCODEiGHIoJc0FLTDOnUFBH2b2h6yco68nO85IX4R-C0gngyLNM3lIykmj3nPLfb008" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5528ddd2d1.mp4?token=g5a9RphNUw-Gne7TITCPSUowNVfHnRdI9qlx5PTCiYSE7QQb4nj8qknJtHnZbqweEBfnNhszpuFQsNxt6p2Nw6XKzdaJCxdcv1jB_shqOuu4DA8OXJ0TCepoJM2USlD1uqynawlH34MbWmwtdf_AOEqalMOIVsuphsAMXYc0aFo6fz4C3gDmBhzpCuFtdbvfbbT2dSjiieHBGWzzYP493EjFdB6txSNMIYx5q2YSMVTWvph-t0rNIw3HLQ3Fd1JIAireyFlxX_jzxyqGCNYgm45ZvYsjEoEg3twbH2TgJaXibgSDVrxobNbxvHWvfs0KmF6yF6FX02e2Tlvi0Vqb_XVFQ7Sn-Ag9ZioFfsHkJ_OSL7onWmnnyZHWYQ_9autjHa1yQ4U9kvLIy7FO39vhPbvPjejoMp3B3xyU0RtgSxpQylmyYk24ZW-9gyYC4zZ2US-zOIlEa83H7kQ-dFCdXIpP4PNFGitPDWERiDBNNQ8QSbdmRVCgklJU6jTsjhwKUG9cUDtrfVqF9Al-YlgOIcLnR7zztRK3TGAxUnPCBX9Uw8SvMT96YguvxG5KOz0QLx2ff2wSCjzj_0xX5-bqtM8DD72MYyBXqKpE65gdfCODEiGHIoJc0FLTDOnUFBH2b2h6yco68nO85IX4R-C0gngyLNM3lIykmj3nPLfb008" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
حال و هوای اردوی پرسپولیس پیش از سفر به قزوین و دیدار فردا مقابل شمس آذر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138115" target="_blank">📅 17:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138114">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⬅
یکی از نزدیکان مهدی طارمی پیشنهاد پرسپولیس رو به طارمی تایید کرد اما اعلام کرد طارمی به ایران برنمی‌گرده/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138114" target="_blank">📅 17:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138113">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzRsWLGcgzqVnyJ0vehleKTqwXk9H5er2R3LEDJ_sWYI1_OyVJXF357baa6BPZjuVnkOph3zNc-Z71rn-qC2R6Kxwc-5lt13of4Fl-GiIZC_CApcYA6ZRw2RraW6Q_5Lm9HCRwmt84V3teqeAhnmjwbKmIeuXvXu6MdHS-rb2HxEDPa08AfS6IY4PEcbm5IeuFH4izrDfjkGbIp7qpDvFzTDR2SYo0cXbZ3hq31Ncun50D8q12foHkKy3RZos6_Sgx34cbPxViIyN1EzhYSf7A9GLIfwI4IbbTrvqIGDcwsv0XLs4mB2b_U6lPgW_cSqvrtVVLCE6Zk8Uqeo3Q7p1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راه اندازی کمیته پیشکسوتان پرسپولیس در دستور کار قرار گرفت
‌
✔️
با دستور دکتر پیمان حدادی، مدیرعامل باشگاه پرسپولیس، راه‌اندازی «کمیته پیشکسوتان» در دستور کار معاونت فرهنگی و مسئولیت‌های اجتماعی باشگاه در دستور کار قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138113" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🏅
برنامه بازی ها فردا لیگ برتر؛
🏅
تراکتور _
🏅
پیکان 18:00
🏅
استقلال_
🥇
مس شهر بابک 19:30
🏅
خیبر_
🏅
فجر سپاسی 19:30
🏅
استقلال،خ_
🏅
آلمینیوم 20:00
🏅
سپاهان_
🏅
چادرملو 20:00
🏅
گل گهر_
🥇
نساجی 20:15
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/138112" target="_blank">📅 17:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
امروز بازی های هفته اول برگزار میشه .کدوم بازی و نگاه میکنید و دنبال میکنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138111" target="_blank">📅 16:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🏅
برنامه بازی ها فردا لیگ برتر؛
🏅
تراکتور _
🏅
پیکان 18:00
🏅
استقلال_
🥇
مس شهر بابک 19:30
🏅
خیبر_
🏅
فجر سپاسی 19:30
🏅
استقلال،خ_
🏅
آلمینیوم 20:00
🏅
سپاهان_
🏅
چادرملو 20:00
🏅
گل گهر_
🥇
نساجی 20:15
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138110" target="_blank">📅 16:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
پارس جنوبی جم در یک بیانیه اعلام کرد انتقال کوروش اژدهاکش به پرسپولیس غیرقانونی بوده و این بازیکن هنوز با پارسی‌ها قرارداد دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138109" target="_blank">📅 16:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
✅
کورش اژدهاکش که گفته می شود یکساله و قرضی به نساجی منتقل خواهد شد  امروز در تمرین پرسپولیس حاضر بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138108" target="_blank">📅 16:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138107">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❤️
کاروان پرسپولیس راهی قزوین شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138107" target="_blank">📅 15:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138106">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❤️
کاروان پرسپولیس راهی قزوین شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138106" target="_blank">📅 15:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138105">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">هر کانالی که این اتحاد و پوشش نده خیانتکاره</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138105" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138104">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQrBXAYr4lUzI1fwSD3cZJa6Kr7IbSaSqHJ-yH2at_-9i-0RCSNIhS5jp8d49su8p6y6R53OA9MNOrDXcKoUyHXC1A3Qh2uasLLlu5ftO8X3BFVN0EmMygOswrf8Sv6b-O_MYC46AGMVWXxNcYNsu-3R3HtXhmLEbz752998ZoGaHgCUQ-fWl87tqYXjfI1jk8tSksLQCgV_DJF3Egw2775WUqSxzhQoXBP2Qi3DNF6hNTEPAhMWQmX0qaImBWJv9DZhJ9HXgLttM46V7xu8yWCg3L8SgqPfDrUoH6M1CzxKcQ46dBLVjIBEG8mx3A2PP6KCAGBolzDQ_pdoxqOssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🔥
تصویری دیدنی از کریم باقری در تمرین پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138104" target="_blank">📅 15:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GffHC4zAivOJnkZBEkInwglFY5hxaHBMO7vjR-2MUvvFScSEJR4NM09eBpyLTtLjWGOkp-w6GAmlkjzS5LH7tG0SiQIhDrrZ2SnzCVKz8Z9xT23DMBaUeiGiCzlzQUCg7FEIinij2Hlvcj0r4Il3gMNI8LdR_9o38k8gdhWSTz_wDjRfmjCex0D9Mz-auNqoGdDNI2GUcmNN0NYtGlGbxjpZHACqjkj0STrbIcAhIgGK5_jeWTP9_WM7olnOdk7x01Lfrk3H_w9SfCLq4K-2tfz-bLVk4kVrV0NzugLRX8iEk644fg9jX1iauF080jqmBOwE9SxgjeB4kuK-R4LhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
کاروان پرسپولیس راهی قزوین شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/138103" target="_blank">📅 15:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕
❤️
برنامه تشویق هواداران پرسپولیس در دیدار برابر شمس‌آذر
🚫
صدای هواداران در این دیدار باید هدفمند و در چند مقطع مشخص شنیده شود: پیش از آغاز بازی، هواداران یک‌صدا خواستار اخراج احد میرزایی و اینانلو و همچنین جذب محمد قربانی شوند
🚫
با شروع مسابقه، تمام تمرکز…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138102" target="_blank">📅 15:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138100">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕
❤️
برنامه تشویق هواداران پرسپولیس در دیدار برابر شمس‌آذر
🚫
صدای هواداران در این دیدار باید هدفمند و در چند مقطع مشخص شنیده شود: پیش از آغاز بازی، هواداران یک‌صدا خواستار اخراج احد میرزایی و اینانلو و همچنین جذب محمد قربانی شوند
🚫
با شروع مسابقه، تمام تمرکز سکوها روی حمایت از پرسپولیس و بازیکنان باشد و تیم تا پایان بازی به بهترین شکل تشویق شود.
🚫
در دقایق پایانی نیز مطالبه هواداران باید شفاف باشد؛ درخواست برای تغییر دو عضو هیئت‌مدیره و تأکید بر جذب محمد قربانی این مطالبه باید تا رسیدن به نتیجه، قاطع، منظم و یک‌صدا دنبال شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138100" target="_blank">📅 15:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚫
هرکسی با اسم رمز فردا بازی داریم خاست جو اروم بکنه پول گرفته و قرمساقه
https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
#جذب_قربانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/138099" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امام علی(ع)
: مؤمن اهل نیرنگ و فریب نیست؛ خیانت و حیله‌گری با ایمان سازگار نیست
https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/138098" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✍
کون‌گشاد دروغگو شیاد میگه همدلی؟! با دسته کورا طرفید؟! علی سه پستون‌ چرا رفت دست بوس علی دبیر ؟! نه جواب بده دیگه… چرا با لیدرا تا پنج صبح تو یوسف آباد جلسه داشتید؟! امر خیر بوده ؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/138097" target="_blank">📅 14:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🫦
ریدم تو باشگاه که علی دبیر بخاد برای ما تعیین تکلیف کنه
⛔️
علی ا.ی.ن.ا.ن.ل.و معروف به علی سه پستون کی شاخ شده ؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138096" target="_blank">📅 14:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138095">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
پرسپولیس اینقدر خار ذلیل نشده یه ک.و.ن گشاد دهن گشاد و ارباب تخ.میش بخان گوه زیادی بخورن مالک حقیقی این تیم هوادارانش هستن
🔴
پرسپولیس جای ادم های دو بهم زن و شیاد ق.ر.م.س.ا.ق نیست نجاست شما بر همه هوادارا ثابت شده و از این به بعد هرکدوم از اعضای هئیت مدیره بخاد بلند پروازی کنه گوه زیادی بخوره بلانسبت اون آدم حسابی ها چنان ک.و.نی ازش پاره میکنه هوادار و مردم که خیاط محلتون هم نتونه ک.و.ن.ت.و.ن.و بدوزه،تو دهن تون ر.ی.د.م که جز چاپیدن بیت المال و دزدی فساد رانت هیچ گوهی بلد نیستید بخورید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138095" target="_blank">📅 14:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138094">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
❤️
پرونده رامین – پرسپولیس بسته شد
❌
همانطور که مشخص است پیگیری هواداران پرسپولیس برای بازگشت رامین در حال حاضر به نتیجه نخواهد رسید. فارغ از مسائل مالی که در این انتقال نقش جدی خواهد داشت، عدم نیاز تارتار به این بازیکن در مقطع فعلی، دلیل مهمتری است که قرمزپوش شدن ستاره تیم ملی را کنسل می‌کند
✍
خبرگزاری ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138094" target="_blank">📅 14:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138092">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdkt0NrodKaMeE5lvUnpzLsTi8KN4E3IlGj5zypJ_GFC38E2fKPMadleYl9Me0kyAS3NbQiZ6RR9Pll9zG5K8t0N6z86-bZZ8C1R0A_3HNoeLCv1himUh8LC6CRG6oyjXhUPwBHNnSuNqXc757_KpvzHg0bTheMohzo9hDdrvMUKeiikypx6WLNfL7t7Lp42r8kt02oTLSTzCFizrHDHkU5sawVY0OD0xJc8Wdov1cvxio23R5jX42fcGmImCYmiJlxQua0qsmgjwybNp-vvs5IS1t4yceNNc-B9CDPQI1A2plgJFZCUY1CS6frcuqnuc248wysMHqDpEAA8MVzROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
🤩
نگاهی به
😃
تقابل اخیر پرسپولیس و شمس‌آذر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/138092" target="_blank">📅 14:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138091">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrVwEgavgWT0kwjt1EG9a1D_I7k5w_fsr2L47IJMbIzzFjDPtg1xvRmfVGM2zzMU1RdRFP3OfG_7-uTFU5gyRAIJHTLupNa947rgTGyZK5sMu4fb2SXAPFVSF5EQvAWXVm-IRfsW8nuTPFREmZpwsM2-0YXuiAVJp9XdD3AkN5v6IEwETEEEyfxKWpPAIWQ0itcJHgIVBlVT5klpLSywnhOZRddLHMQW__KtxXFAUhoS8qXZQw6ED5B-86q4PL9PbAXhLevj3P8PEo0jJdF81h5zvWKnLo2LxYM9yCM8XC8lzBUDgt4tArYhAGBwY1maFLU_kXwO2TtDknk1LzPBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سوت آغاز لیگ برتر ایران؛ پرده اولِ یک فصل تازه، مدعیان برای شروع طوفانی می‌آیند!
⚽️
امشب تراکتور و استقلال با برتری روی کاغذ وارد میدان می‌شوند، اما چند تقابل کاملاً متوازن می‌تواند معادلات را به‌هم بزند.
سپاهان و گل‌گهر هم به‌دنبال سه امتیازند؛ شبی که فاصله‌ی بین برد، تساوی و غافلگیری بسیار کم است.
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138091" target="_blank">📅 14:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
#جذب_قربانی</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138089" target="_blank">📅 14:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138088">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚫
و هر رسانه خیانت کاری که تا الان موضع خودشو مشخص نکرده توسط کون‌گشاد خریداری شده،خوب نگاه کنید هرکسی حمایت نکرد و سکوت کرد پول گرفته و کونش پارست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138088" target="_blank">📅 14:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPerspolis</strong></div>
<div class="tg-text">هواداران اگه امسال قهرمانی می‌خوایم برین پست آخر پیج بانک شهر و پست آخر پیج پرسپولیس :
👈
جذب محمد قربانی
👈
اخراج اینانلو
👈
اخراج احد میرزایی
( اینانلو و میرزایی ۲ مهره ضد پرسپولیسی هستند که مانع تقویت پرسپولیس می‌شوند و حضورشون سم مطلق است )</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138085" target="_blank">📅 13:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هر کانالی سکوت کرده
https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
اینو نزاشته بود لفت بدید… بعدا هم انشالله به خدمتشون میرسیم د.ی.و.س.ا رو</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138084" target="_blank">📅 13:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❤️
بسم رب شهدا و صدیقین
❤️</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138081" target="_blank">📅 13:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
بسم رب شهدا و صدیقین
❤️</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/138080" target="_blank">📅 13:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خدا هم حریف دبیر نمیشه .زیاد به پاش بپیچید میزنه باشگاه رو منحل می‌کنه</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138079" target="_blank">📅 13:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV.A</strong></div>
<div class="tg-text">خدا هم حریف دبیر نمیشه .زیاد به پاش بپیچید میزنه باشگاه رو منحل می‌کنه</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138078" target="_blank">📅 13:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138077" target="_blank">📅 13:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚫
اگر توان مدیریت و نظارت بر نمایندگان خود در هیئت‌مدیره را ندارید، حداقل با تصمیمات و عملکرد نادرست، آبروی نظام و مجموعه را زیر سؤال نبرید.
🚫
رهبر انقلاب بارها درباره مسئولیت مدیران، امانت‌داری، مبارزه با فساد و ضرورت برخورد با افراد فاسد و متخلف رهنمود داده‌اند.…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138076" target="_blank">📅 13:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👀
رفقای قدیمی فن آخر استاد رو یادتونه یا نه ؟!
👍
فرمایشات ائمه اطهار و مقام معظم رهبری…
🔥
چه آشی بپزم
💦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138075" target="_blank">📅 13:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👀
رفقای قدیمی فن آخر استاد رو یادتونه یا نه ؟!
👍
فرمایشات ائمه اطهار و مقام معظم رهبری…
🔥
چه آشی بپزم
💦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/138074" target="_blank">📅 13:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#افشاگری
🚫
با توجه به سهمیه لیگ برتری تیم ها، محسن خلیلی با حمایت اینانلو در تلاش است تا به جای جذب محمد قربانی، امیر جعفری را با پرداخت 110 میلیارد رضایت نامه از گلگهر بخرد
.
❌
گویا انتقال قربانی برای آقایان منفعت شخصی ندارد/ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138073" target="_blank">📅 12:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">چراغی اینو خواستی فور بده
فک میکنم همه هواداری پرسپولیس موافق باشن هیچ مدیری مثل حدادی نمیتونست اینجوری بازیکن جذب کنه خداییش کادر فنی دست روی هرکی گذشت جذب شد ایشالله با جذب قربانی کارنامه خودشو پررنگ تر میکنه
#حمایت_حدادی</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/138072" target="_blank">📅 12:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚠️
⚠️
علی دبیر شده همه کاره….؟! دبیر نفر اصلی هست که دنبال زدن حدادیه و آوردن اینانلوعه  #اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138071" target="_blank">📅 12:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from꧁༒ᄊﾉÐ刀ﾉムんｲ༒꧂</strong></div>
<div class="tg-text">این دیگه کیه شاخ شده واسه ما برو به کشتی برس پلشت</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/138070" target="_blank">📅 12:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚠️
⚠️
علی دبیر شده همه کاره….؟! دبیر نفر اصلی هست که دنبال زدن حدادیه و آوردن اینانلوعه
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/138069" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4133fa453.mp4?token=ICluqvlEsmFa7eqxfd1WI_NiYgJCkWyijeciBLAnX7VxwL_aV1AhK9vutxtPWnY71Jz-1XknOmUjshWO0lR7e0m8zArra3itEaHy6aWJ30fJgr7ssLvwJEFWYHWf7IROYTavUbwy_AXF4rLeq4sLJomlPR3E7oSvJIlqfxJ_vaEyli8Lbp_x-BAzBXGZ6uK5D8Vi_BsDA2eUk_uXDSqOoBc9jmpqwMYwxVGMz37a0YJZHlloh2dcQHOAJSoZHn-S31TwJEaaYBIU_FLkpvJm0wYYRdU4ITKvZVJv_0sgMPY4ae_aY2PLFh2fh6OTwd0Z5X-xIIwGxeAdGI7Q55a9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4133fa453.mp4?token=ICluqvlEsmFa7eqxfd1WI_NiYgJCkWyijeciBLAnX7VxwL_aV1AhK9vutxtPWnY71Jz-1XknOmUjshWO0lR7e0m8zArra3itEaHy6aWJ30fJgr7ssLvwJEFWYHWf7IROYTavUbwy_AXF4rLeq4sLJomlPR3E7oSvJIlqfxJ_vaEyli8Lbp_x-BAzBXGZ6uK5D8Vi_BsDA2eUk_uXDSqOoBc9jmpqwMYwxVGMz37a0YJZHlloh2dcQHOAJSoZHn-S31TwJEaaYBIU_FLkpvJm0wYYRdU4ITKvZVJv_0sgMPY4ae_aY2PLFh2fh6OTwd0Z5X-xIIwGxeAdGI7Q55a9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول فصل قبل پرسپولیس رو علیپور زد؛ به نظرت این فصل کی گل اول رو می‌زنه
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138067" target="_blank">📅 12:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==  #اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138066" target="_blank">📅 12:28 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
