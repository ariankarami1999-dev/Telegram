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
<img src="https://cdn4.telesco.pe/file/gh9N0Hke1pXe517XlndyDM_mLhIkNwjYMI4ZDR078KPRQu2M-xB1RVATOBGZuyzUG9hWa6tvrsaqLsS2VXUgHo-k03adIpN6IGv0g88J3isu6j1KR2skzq6ep_nmFwA-8Q0S14j64GQwTllOyIcWr4XQNRcC48K-0LQJeUgRtFHD8CBIyJA2IECJiXpaMpg7W0BrzEf9cPKX2bcIWxbMwH0uQGPa0YY05_EH_7zBOn434E3IoEiKDlfHJZ0IaGLyLsJcKKUnWu_YmrzDjRutXKonY7MreQJFg0BuAbEz0iVhEGHVyCs6K_5Qafuw3cFQF1-eiYCEW3TolY0MtoSehw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 01:27:09</div>
<hr>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: حضور من در ورزشگاه شهر قدس خیلی حس خوبی بود/ دوست داشتم لباس عوض کنم و به زمین بروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/SorkhTimes/139340" target="_blank">📅 01:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
پیام صادقیان: حرفه‌ای ترین دوران فوتبالم ترکیه بود اما زیر تمرینات پرفشار آنها بدنم دیگر جواب نداد و فوتبال را در ۲۷ سالگی کنار گذاشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/139339" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: بهم گفتن سایت شرطبندی که میزنی قانونیه مثل نیمار و فوتبالیست های بزرگ و اسپانسرش هستند و نمیدونستم قانونی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/139338" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
پیام صادقیان:
❌
شرط‌بندی هر نوعش تهش باخته و فقط شما می‌بازید؛ من اشتباه کردم و همینجا میگم پشیمونم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/139337" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
صادقیان : شرط بندی تهش باخته و سرابه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/139336" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: با محسن مسلمان تو تیم ملی زیر 10 سال با هم بودیم بعد هم در پرسپولیس و تیم ملی با هم بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/139335" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
ورزش‌سه: در تمرین امروز تارتار به سبک بازی با تراکتور بازی با ۳ هافبک و ۳ مهاجم رو تست کرده که مثلث خط حمله رو علیپور ، بیفوما و محبی تشکیل میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/139334" target="_blank">📅 00:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
پیام اومده فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/139333" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/139332" target="_blank">📅 00:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=VpB1IOBedIiCZS9eFxSg5L_wQAUFwKF8qtp89G-uyGnUpHk8BoOnXpBrURjCholznsVxngv5UFbuQG_bArrw661FCkOX-7OQxkTB0oujvMmP5WIwAQXTYAx08rE3F5jeg9cVcTtD5cXkAQoVLm4mW4sDxkRnwsbEFmm_V6e9wXxt-ROyOfSbWyvVnO3leFI0qlSlD2lzIBR9t-cK2hz5NrU4LxubolWTsQFDW-cNN0vdtDikGK476mMpU3zeGrGL-0rGoa1Tafxr4b7RCi4lp3FhYXZOfrd_som_Nbd1zg6neESfPXwQ01_tRSg3mJdCbW5DLito_NAERFHNSvnjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=VpB1IOBedIiCZS9eFxSg5L_wQAUFwKF8qtp89G-uyGnUpHk8BoOnXpBrURjCholznsVxngv5UFbuQG_bArrw661FCkOX-7OQxkTB0oujvMmP5WIwAQXTYAx08rE3F5jeg9cVcTtD5cXkAQoVLm4mW4sDxkRnwsbEFmm_V6e9wXxt-ROyOfSbWyvVnO3leFI0qlSlD2lzIBR9t-cK2hz5NrU4LxubolWTsQFDW-cNN0vdtDikGK476mMpU3zeGrGL-0rGoa1Tafxr4b7RCi4lp3FhYXZOfrd_som_Nbd1zg6neESfPXwQ01_tRSg3mJdCbW5DLito_NAERFHNSvnjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/139331" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/139330" target="_blank">📅 23:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❤️
❤️
اورونوف در تمرین آماده بوده اما وضعیت جسمانیش همچنان بهش اجازه نمیده که ۹۰ دقیقه بازی کنه و قراره نیمه‌ی دوم به بازی بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/139329" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
‏ ترامپ به شبکه فاکس نیوز: ما امشب به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/139328" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❤️
❤️
10 دربی بدون شکست برای کاپیتان
✅
حسین کنعانی در آستانه یازدهمین حضور خود در شهرآورد پایتخت قرار دارد؛ کاپیتان سرخ‌ها در 10 دربی گذشته که به میدان رفته، هرگز شکست نخورده است. او حالا به دنبال حفظ این رکورد ارزشمند در یازدهمین شهرآورد خود است.
✅
پیش از کنعانی نیز کاپیتان دیگر سرخ‌ها یعنی امید عالیشاه که امسال از جمع تیم جدا شد. با ثبت 18 دربی بدون شکست، یکی از ماندگارترین رکوردهای سرخپوشان در تاریخ این رقابت را به نام خود ثبت کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139327" target="_blank">📅 22:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/139326" target="_blank">📅 22:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=h3nqh2KbwlI-SofbRbUscyTxzQrKwjkLKCw8uG6oGDJqEFsMps8R8wZ0rJfIxmKtDWTYL-6qxzGJ-er0sYL5hby9xp62hIDr2a6_Kzazc_up8HsZSNC6QdYkmxJswldsX2be2M6B3uVzUowm44OpydtN2PsiiL_0TEEyRhsMP7-vBRRSL5oKcStn7O_maq2xDmDtBMfE2I_vsECL22ft7xsKpwqd7vVLJmAcZKWEUIEKfFbCbMeMH5lKLgmirr2Et79lysd3ca014HZ-Xcnrq1U8HiK95iJXgJksI7xGXDBjbOfoos4abZB5Fv9G3v18c8gzk-0iMHSkmwnZH9Gabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=h3nqh2KbwlI-SofbRbUscyTxzQrKwjkLKCw8uG6oGDJqEFsMps8R8wZ0rJfIxmKtDWTYL-6qxzGJ-er0sYL5hby9xp62hIDr2a6_Kzazc_up8HsZSNC6QdYkmxJswldsX2be2M6B3uVzUowm44OpydtN2PsiiL_0TEEyRhsMP7-vBRRSL5oKcStn7O_maq2xDmDtBMfE2I_vsECL22ft7xsKpwqd7vVLJmAcZKWEUIEKfFbCbMeMH5lKLgmirr2Et79lysd3ca014HZ-Xcnrq1U8HiK95iJXgJksI7xGXDBjbOfoos4abZB5Fv9G3v18c8gzk-0iMHSkmwnZH9Gabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/139325" target="_blank">📅 22:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
تأیید پارگی رباط صلیبی «مهدی ترابی» بعد از MRI اول، در انتظار نتیجه معاینه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/139324" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdz7NflgbQfxff8SxIpZamyz2iuON0958qjiJ-fmz1Dakt3QJm44F_v99eYeHbtTQg4CeQLPlEivMk-28h7deq8TIxnAgiP-GEBmAoLH5-W2IWFPwJiU9qQbIRoX3YzhWJby6POlZ3Znh5ib5WVbgU1Hw6TXuZ0q4al0ASO5Pb32FCiPdtvHD94yTwJh3SUk5SKmDfhO8Xi1CYabBIEo6_-Lb0RXks1yoRi2MAJuY7mYYqzUeJAHq1uv_vZxi-1r9LgOY8yglwmhkAqopwCi6X3hxTWNNX_RwdjTvBWD4M6R-Q9lJQyvq72dwSJZ99i7WAM65tQhXChTdSUCwn-lOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139323" target="_blank">📅 22:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/139322" target="_blank">📅 21:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139321" target="_blank">📅 21:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139320" target="_blank">📅 21:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد  هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139319" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2oZBOK3wAv1vGdPkhRJIgvIQuKiut9vnirRJ-0VYGJ5b3yTKSSgva83-Fy1JT3wfhbhhbffDQwyoH22EQcdMFl53Iubpl0hT0xkqXvma20As8kOTTLq_gZ1eR0OiC6Eb3osw5vm1ML_J7cUPW9614B0o7tFzG_9RdL6g5Wc783shxlkD_BcbLUrwdNkGCwJ9gkm-Ikqz-5WQaEFQ-HOr_hUhx0zG71ovzDjtu5ostTxrmZXEQdQIEjyJRSxB9jwoWEYomq8KhDCBRHUdYWUerHoZkl7m0IMqjVupQcI0gjP0yZIWdUghJVbW9Vynb7zo8xamIypeCHalw6G40igmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139318" target="_blank">📅 21:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_PUCFbXt1OHpt8Y3kCE1DkUv9RhkdzDSBeQtZOYUAcR8ZIrQgu7vee1frS9oh5rsHSgRlaZ5-I3VrQ9R_QSisgA81gxaPAOwaXQZf8vB_ukam76m7PSzylBbTN1WDW_VSsMDpXtMA4nvzuIdvDhZnsURXIDPq0-Rl1hOpRbXyf_tKsMMrDLxW6_bEoRHve346QS9W3wH6mZ373CZrH-GGhB5ohrtxEbAP58JHafluLyZpjRk6ihqTv85td9iMFuA8m88vRVV1h1ATnyXNFBuCTmKtH0UIs11kzrLd31_yARXSfid6sm0UomQqtb40u4chMF04ZyVMpKSkBE4FZHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد
هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139317" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WprF-r1orTYstjavr5zKJMxE5z9_Y6bwpGxoeBv-GvGOgSfjHqTJZCwEs4yE_JQ_jaHn3y85VTqAeHgnUxMr7Cct9JCnkXHxeJXTnx2dYZSx0APT0np-1o1KvCEb3cfPC4iQYNQWVTVj0jUdD-G4q3phbdzm_bl4H6_93YXOhjjITZ53_ZRqzW-bOC7VvNQS3QAhPg4T-p40HiYaJKIi4Y4clqQUaf4EQb75QxpEXhjWpR0ssfB3uWFXLKPiwWfQXX1MujwHnYcwZLi_oqEytsABGzdy_LDKvMe4RKr_3I3BC4cQFrSqwsZy5cGF-tDqy2QzFNUdCmpLFePJuoYdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بارسا به دنبال ادامه مسیر بردها!
⚽️
رایووایکانو آمده تا کار را برای کاتالان‌ها سخت کند؛ نبردی برای صدرنشینی جایی برای لغزش نیست!
[
بارسلونا
🔵
🆚
🔴
رایووایکانو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139316" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139315" target="_blank">📅 20:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
احتمال زیاد پرسپولیس با ۲ مهاجم بازی میکنه و بیفوما هم وینگر چپ هس تا پرسپولیس تو حملات با توجه به ۳ دفاعه بودن استقلال کمبود نفرات نداشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139314" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
کامنت کریستیانو رونالدو برای مسی:«لئو، توی این روزهای سخت، یه بغل خیلی بزرگ برای تو و عزیزانت میفرستم. خیلی قوی باشین.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139313" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139312" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139311" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
تارتار نمی‌خواد ریسک کنه!
✅
به احتمال خیلی زیاد جلالی در دربی به میدان نمی‌ره و تیکدری مثل بازی‌های قبل در پست دفاع چپ پرسپولیس قرار خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139310" target="_blank">📅 15:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
فوری؛ هدایت ممبینی برکنار شد و با حکم مهدی تاج، حامد مومنی به عنوان سرپرست دبیرکلی منصوب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139309" target="_blank">📅 15:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139308" target="_blank">📅 15:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139307" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saWZWR_Syw18ueTRp3NgZIYG3tXy8aSVVTdKZl5wGA4DvpvW5Oy1oT7L9uS7dZYi48ScfSlNa87sPvMlb3DbTSJzqnBPxFjcgT58h_NOnPVFX27o6ZbTvTZNrw92qK5Qt3rOKBisz5dNDAegB6UDRx84xfdkLjRtBS8qVXLRGtLi0cK6jaoE_fQ2to-0GmFmYRBRPYFjklHuX_6WnaAyLPWn6bAi_19-NOm7CAOw5VKfb_JS4NkLe6N2lDVfJsEtwMtFRK9jhDHCugKKO5e2pvuJtYHYCzhB2QqiohSwW89uKj-S1vjQ_XV9dAxa_mLEmr7Svzg77fyXDHY_IhgW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ویلا پارک آماده یک شبِ آتشین
🔥
استون‌ویلا و آرسنال؛ جدال قدرت و جاه‌طلبی
اینجا هر اشتباه می‌تونه بهای سنگینی داشته باشه!
[
استون‌ویلا
🔴
🆚
🔴
آرسنال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139306" target="_blank">📅 14:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
حدادی قول داده فردا صبح پاداش پیروزی مقابل ملوان رو بریزه به حساب بازیکنا تا قبل دربی انرژی بگیرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139305" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
‼️
بلیت فروشی عصر امروز شروع میشه که ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به صورت ۵۰ ۵۰ بین هوادارای دو تیم تقسیم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139304" target="_blank">📅 10:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🔄
🔄
با اعلام باشگاه استقلال بلیط فروشی دربی از ظهر امروز آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139303" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
بلیط فروشی دیدار پرسپولیس و استقلال خوزستان شروع شد . از طریق لینک زیر میتونید برای خرید بلیط اقدام کنید   https://footballeticket.ir/buy-ticket.zul;jsessionid=23B55854CCBC6E89F276AA81C2DC01A1#  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139302" target="_blank">📅 10:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139301" target="_blank">📅 10:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5lICGObKy_ceA1EVpLjbCYxoGwQ7tzjlEdRXTFW66HFeWY1qCtW_Hf0Ih1CcL8nYRmnwG45HLYpx9rvXnhGObxtVGRU0iwWXn0A7VcfuUj2mfHVUGZ8e6yRdkSj9rbriahCjMGmMquKt2e0hEiiH2CbCYYxaPUwJspJubXSr_KtmSHz_emg16i6qGv6v_QMFLW5Qs5mIJ0__eqIYt-doDWAhw3nEEqIEyBDkKLt3XBEjtw2i9S5OSfE_1CxxMZ71LNUYhYBxqw9soT19SxQPrEMN80APbLnUJTJ3BisoRULAvNK73tEaFPmRixGYV14gt8qkhQW77wV6MmRzkqSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139300" target="_blank">📅 10:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139299" target="_blank">📅 10:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
از هتل المپیک خبر رسیده است مهدی ترابی ستاره تراکتور به علت مصدومیت ادامه فصل را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139298" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
چند دقیقه پیش تهران لرزید کیا حس کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139297" target="_blank">📅 08:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139296" target="_blank">📅 08:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ..
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139295" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1fMC12QgfJOM84xtiL_XqaFiP0Fo_EVtSk9kCRPAEPMiFseqOAv2SYRf9cHtRKhmjzFqLRcXjE8jbFVts55ipjIc6rjqzbBXFaqk-7J_PqG7_5H_hLcRPMrU3TnHl8L1J3g3XqmG6b9PHkbNhL8pdIMxHfqOvNsGa7fSqUyA49lGvNCIJFle-0DICGYJ_AFfKZbLhWXCmDA-t-v3oGnxDmtx1rh5d7PmI5lzLq70Zij6fui7Bpy-IDPPHG7b40OD8FrWqTzyy2OXd6ymKZqEJQFM4RmySJLIxslWtg7Zl7Ire6kIbp6nesNfduF18nMXrP9c36EvXcoYPVnuldpvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک شروع شد!
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/139294" target="_blank">📅 02:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
سپاه پاسداران انقلاب اسلامی :
🔴
🔴
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139293" target="_blank">📅 01:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
قیمت دلار برای اولین بار در تاریخ به ۲۰۶ هزار تومان رسید  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/139292" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/139291" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
درگیری ها بین ایران و آمریکا دوباره بالا گرفته و درصورت تشدید تنش، احتمال لغو دربی زیاده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139289" target="_blank">📅 01:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139288" target="_blank">📅 00:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">💢
💢
💢
احتمالا دربی پایتخت لغو خواهد شد .
🟥
چون پرواز ها فعلا لغو شده
‼️
گفته میشه در صورت تداوم شلیک موشک ها از سمت آمریکا و ایران هفته پنجم لیگ برتر ایران به تعویق خواهد افتاد.این تعویق شامل دربی هم خواهد بود
⏺
همه چیز تا فردا شب مشخص میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139287" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🎙
🎙
تمامی پرواز های کشور از جمله فرودگاه مهرآباد تا ساعت 6 صبح فردا لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139286" target="_blank">📅 00:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
فرودگاه مهراباد بعد درگیری ها تا اطلاع ثانوی و معنوی تعطیل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139285" target="_blank">📅 00:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JShvompsaDVfSnCVrFFP3N45Yz5Vlmoh9iNF_vflpphgkiPJF3eS-qRKDCd51MFxvUo6SOTdhG-lT-pNzq2SypL7NipPt1MAe1qpDNelxbrJGCceB6k-0QPKe6tRzHPQuDCQK9pNJwAYFBpSRMAfQEVK4TVOKIdvS34JO3NaB-KheV9JYwP9q_XYLbgZLxHNsDfYQyuRbo4sIvBaLRqVQHA4McoPPkRO_vR4__I8UFUk7P0n_CNjmW1HKGqE-NQO6DOh-70Ub2_CTSbJS5GNSFE3fOCoYj0hvytiYbR-0VfKjt2yXgZ6nLsGtGxlu90nG0_ucNrkpYYUZtX-h0c-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
فوری، با تصمیم تارتار و موافقت علیپور؛ محمدحسین کنعانی زادگان بعنوان پنالتی زن اول پرسپولیس در دربی انتخاب ش
د
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139284" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv2vWungzbIAWifxMKqoxQfWWhw6nh2E7pUeO5fUR-UdGH4I2P_1us7UWZDwnnF48RZ7Ytjaboy8u6Ao4OLEO-GrLl07WLlva5s9z0IQhHlBg7zY2WFZKjcgQHXNb76BcXyruxZbxiCJvnFALK7t_V840t6-LcLAqMBG0KhDvmXKKi-N8208qjFjlcPWZmggVy6weCWkp-y4sC3VkGnDd5RuJo72eeplas7LCZkcL52IYJj5QLHiCgBEVwAzVicuS8569bBGs-h5xkDYsCQiMwos6wqYpVdRktcFMw53w7Acw5taMtfRKY33p4yT6ElruaoY3ouJp4ghQTGUFILnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139283" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139282" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🟥
حاتمی: پرسپولیس در این فصل تیم خوبی است
❌
دربی‌ای که در ورزشگاه آزادی با نتیجه یک بر صفر پیروز شدیم در ذهن من مانده است چون اولین دربی من بود. ورزشگاه آزادی باید به این فصل می‌رسید اما این اتفاق رخ نداد. بازی‌های بزرگ باید در ورزشگاه آزادی برگزار شود. امیدوارم دربی خوبی داشته باشیم. پرسپولیس با مهدی تارتار عملکرد خوبی داشته است. همیشه هوادار پرسپولیس خواهم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139281" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚽
نورمحمدی: هت‌تریک ایمون زاید در ذهن من مانده است
‼️
دربی سه بر دو و هت‌تریک ایمون زاید در ذهن من مانده است/ هواداران دیگر مشکلی با حضور بازیکنان استقلال در باشگاه پرسپولیس ندارند/ زمان ما تغییر تیم سخت بود/ من پرسپولیسی بودم و استقلال را زیاد دوست نداشتم/ امیدوارم شاهد دربی خوبی باشیم/ پرسپولیس در این فصل یک‌تیم بسیار خوب و کامل دارد/ پرسپولیس در این فصل موفق می‌شود/ جذابیت دربی به ورزشگاه آزادی است/ اینکه دربی در اصفهان برگزار می‌شود عجیب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139280" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ
: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139279" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❤️
🤩
کنایه مدیرعامل باشگاه به برخی رسانه‌ها:
‼️
این سفری که به ترکیه داشتم و چند ساعت دیگر برمی‌گردم، از چند روز قبل برنامه‌ریزی شده بود. خداراشکر همان‌طور که ترکیب تیم‌مان لو نمی‌رود، دیگر سفرهایمان هم لو نمی‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139278" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=IWcJ4zFtqb9-tdG8oF1_MpLQJjJdBfu8uOmnsdAnVx8duwnhtzW26yNRkLLN72u_vxNkYQOuTV5yLErQ_KnofoymZB2hlcs5dhfVYnVZBCdVEPywqPrE29IOjMABGJga_Tnaa05YtISU6JM3Uxob1_n0mAsh5omyo69N7RyR012uf44xnOlF1G8FCX7nNhawwO1opSMpvX1JK66OsKMXulXA_pFg2RxvFCfiDWW7vQAeH1Tfp2nhrk4L8NBpndEOTyEGFKzhD_EKC6fGFWBkANH0eYz5U3vkX8qdlw4GlJPqkyqeEo4lBJunYP1sFKMiSwtqWj_WGPdWQB-Vg5cw7UKpYPhVgZd0Pq0n4CiHwOmW7UWGVjVlOoXJ0mdxP9aWwDuDbkjNNVnMAlOcFvuX_H5Sg-9b9wvhdNabvhpDNoQXddmOp5Wv9QT1h05OTFhF_HS_WLk_nhsSskeLzmGcZTSBrFmbczrCVT7z6NGu_5xVZ5qj683fAT6oHov2DOJteLEUG_LeVZE67puFDRnoc8xmvo0rJwVr_r0RCxGcrszqp36uASP2oj9hOnRtbsjxSJmWS9IfQVcqRndMGJbo4UQRMbhRXM28vfoMvLhEAAtwFGFTqqtrco3hOflQ7vauSTszJJSKkAx4R5VOr5_sr9kg0brbY0_ZFkOPuHWDxmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=IWcJ4zFtqb9-tdG8oF1_MpLQJjJdBfu8uOmnsdAnVx8duwnhtzW26yNRkLLN72u_vxNkYQOuTV5yLErQ_KnofoymZB2hlcs5dhfVYnVZBCdVEPywqPrE29IOjMABGJga_Tnaa05YtISU6JM3Uxob1_n0mAsh5omyo69N7RyR012uf44xnOlF1G8FCX7nNhawwO1opSMpvX1JK66OsKMXulXA_pFg2RxvFCfiDWW7vQAeH1Tfp2nhrk4L8NBpndEOTyEGFKzhD_EKC6fGFWBkANH0eYz5U3vkX8qdlw4GlJPqkyqeEo4lBJunYP1sFKMiSwtqWj_WGPdWQB-Vg5cw7UKpYPhVgZd0Pq0n4CiHwOmW7UWGVjVlOoXJ0mdxP9aWwDuDbkjNNVnMAlOcFvuX_H5Sg-9b9wvhdNabvhpDNoQXddmOp5Wv9QT1h05OTFhF_HS_WLk_nhsSskeLzmGcZTSBrFmbczrCVT7z6NGu_5xVZ5qj683fAT6oHov2DOJteLEUG_LeVZE67puFDRnoc8xmvo0rJwVr_r0RCxGcrszqp36uASP2oj9hOnRtbsjxSJmWS9IfQVcqRndMGJbo4UQRMbhRXM28vfoMvLhEAAtwFGFTqqtrco3hOflQ7vauSTszJJSKkAx4R5VOr5_sr9kg0brbY0_ZFkOPuHWDxmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139277" target="_blank">📅 00:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139276">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8jAa5e2sMvI0kNnX7p9FSaEMGL_hngoI2okqu3eslTqmMA9NWkzYsRmobqU20OlOhmU8NZ2s-3uZ7FgT3OVlsijL1eXpvfGFVnR-XCJ4bDDsb1DwTg_QMLN5ztxsW-47Vn4QXQ8J1k9gV1jcHcVTFofS396_1446eBPPYKoefJRtXRSq8I9jXBi0ug2O21x0bBgRGZikjnGRn7kMUBbNqtOA1m2IfYKRRbH76IYUe98mXgQQDrsyLV7Qu3OG5bwK9Fxer-gcpUcktuansyzxoRjhPg2grlLHrxrLS23gccI4QL-dQIqR5-Ewio-tSatEVKBvz2DeNMRBEFKWWFBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139276" target="_blank">📅 00:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139275">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiVWABLtbyaczJXeyk2TnaGLAKELTC4OE5Bndzkm0IN5v6nIfSRajse9reNRhMchT_n1YdwWbqP9FgQ62c6hlNSHN8hvgwQovPCA-3CIo7jACTReCRqwqGhJg_wCiLOgBxTHuhP0fXRXPVyA1Oqvs4VIv7fA-HyT4tWMJrenBG_JpMFs1VkGDzBgK-gSmHPPHBnf79KcMvWG4M9FoECsQJVDFG7MM_o0lxBbFUUGWh_7jTYkhv4GItcX5mkfLXnpb2FBLX_YH1ECNPxwjEMHd27yDn_b77CFbAzWH1XPiyFuPtTvF1YfpRIxfIeUZtCkJi4wX7mKk8Lm4plxb3knaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139275" target="_blank">📅 00:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=MP4I-x3Wq4TZ1Rn67pmvyaPicGitIbV_4JiCkwhpjj1ArFWnOCKQw3gY6w-4xLemMKY1_uqKYGVO3qrxPr9ZubYwFrn0Y4zaCtGKXCcQLxF80bQIANtqu38j3Mq6YGAXFb7gDHSfqMv499I6pdqiCYazlP38cBKUQlKUOWcqu_KgkBd7vGb93b6Fc7kQi8tpuddOqqRx1BMs8JPVlOkypsvpkHds0-twVvmyo3skwC8zlb-k4fgeu7CL3fh0nWRYmcCY1FJR0M0Ult3UIgglXwy6QcJslY5VPOpetxkiJf0xXjbb2UDPm4yKBYZ4h2Ts-FredFV0mj-UJ3lJLIsJog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=MP4I-x3Wq4TZ1Rn67pmvyaPicGitIbV_4JiCkwhpjj1ArFWnOCKQw3gY6w-4xLemMKY1_uqKYGVO3qrxPr9ZubYwFrn0Y4zaCtGKXCcQLxF80bQIANtqu38j3Mq6YGAXFb7gDHSfqMv499I6pdqiCYazlP38cBKUQlKUOWcqu_KgkBd7vGb93b6Fc7kQi8tpuddOqqRx1BMs8JPVlOkypsvpkHds0-twVvmyo3skwC8zlb-k4fgeu7CL3fh0nWRYmcCY1FJR0M0Ult3UIgglXwy6QcJslY5VPOpetxkiJf0xXjbb2UDPm4yKBYZ4h2Ts-FredFV0mj-UJ3lJLIsJog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمد تقوی، برنامه هت‌تریک در آنالیز فنی بازی پرسپولیس - ملوان گفت:
✔️
✔️
«حسین کنعانی‌زادگان در حال حاضر بهترین مدافع وسط ایران در بازی‌سازی است. از سوی دیگر، پرسپولیس با تعداد بسیار بالایی از بازیکنان در فاز حمله، به دروازه ملوان یورش می‌برد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139273" target="_blank">📅 23:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr_5kyyavt1zQ7l2_Abb7EJz6fDPL8ds43VSMBG_N-sz8OsT2OFO1U5drIxdtMl5xvm-q0nxL6gAWwelxRQKIosXVYkk3yqDFk79496O8hxnxUB56VH-4zQq6BAidEMLkSCg1tSO7WOrIIWTSpo838wqGbvtp0Nog8HvwP9YkHaT3N0cyhmDZNIYyclC0QhYv9rm2f3aMvZv8bn9p0hhJWmfjac-e2pYQtNWhngEGC15kYZzkuMLSDx6MRqiZvZQ1DyAcg5dhLMETtz4Nt11tldawl3Rt--qR8AD7Ds1FUPAKbc6MlWwETV0rTyJVJtMzAvxWjJvCurpkq3xIzf_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
وحید هاشمیان: همه اعضای هیأت مدیره پرسپولیس به جز یک نفر موافق سرمربیگری من بودند که به گفته خود آقایان، این عضو هیأت مدیره در صورتجلسه نوشته بود که وحید هاشمیان ۵ بازی بیشتر نمی‌ماند و امضا کرده بود. سردار دورسون هم به من گفت شما تا هفته پنجم بیشتر نیستی!
‼️
👀
وقتی فصل را شروع کردیم، سقف بودجه داشتیم، اما تیم‌های رقیب شروع به هزینه‌های زیاد کردند و بازیکنان اسم و رسم‌دار گرفتند، در حالی که پرسپولیس نقل‌وانتقالاتش را زودتر شروع کرده بود. بازیکنانی که می‌خواستیم را به باشگاه معرفی کردیم که هیأت مدیره و آقای حدادی گفتند شهریار مغانلو گران است، آن یکی پول زیادی می‌خواهد و آن یکی هم گران است! ما هم گفتیم گران است اما وارد فازی شدیم که تیم رقیب ما بازیکنان گران گرفت. این اتفاق فشار زیادی را روی باشگاه و همچنین بانک و مدیریت آن ایجاد کرد که تماشاگران می‌گفتند شما چرا پول نمی‌دهید و بازیکن نمی‌گیرید. آن موقع دیگر دیر شده بود، بازیکن خوبی در مارکت نماند؛ بازیکنان مسن از قاره آفریقا مانده بودند که برخی از آنها هم مشکل زانو داشتند و آوردن آنها فقط بار تبلیغاتی داشت و مالی و فنی نمی‌توانست به ما کمک کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139272" target="_blank">📅 23:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139271" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139270" target="_blank">📅 23:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139269" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139268" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
✔️
طبق گفته رسانه‌ها؛ به احتمال زیاد داور دربی کوپال ناظمی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139267" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139266" target="_blank">📅 21:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔄
🔄
یحیی گل محمدی در لیگ عراق :
🔴
3 بازی
❌️
0 برد
❌
3 مساوی
‼️
عملکرد یحیی مورد انتقاد شدید هواداران دهوک و کرد نشین عراق قرار گرفته زیرا که دهوک بیشترین هزینه را در فوتبال عراق انجام داده اما تا کنون بردی به دست نیاورده است
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139265" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139264" target="_blank">📅 21:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139263" target="_blank">📅 21:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kruj5kfu3yihq9NlduaEQXzRCgWwn5pB5Wlpy3NP6Nu3oZI1J-En9AogaFGiX_PQK4sO5xmTVMhSxBtpDouO3lYQdRa9XkjNCu6CCR8vAH7RPnl3Z5QXw2TQFwYWW5cXkGFPS7ODlU8GgfiXH4LX0plBulPErR3luNqtfphMs-vt4uJlytBsCrPGro5QTx7_iupE433BrIPxQXJ_DKYeL6FzJ_g1QRmUnk_lK20IFCBsYUKcOV-dPw8T5WxzDD500u54KBi9kPpxHi4QpbsQvJevwDdWhQ0Taq8Vsiom9m6DnVwizGa4nrezE-JFD18KUVaBo-qCh1NArFMfo-JA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
منچستر دوباره در مسیر برد!
شیاطین سرخ مقابل ایپسویچ؛ یک نبرد برای سه امتیاز، اولدترافورد آماده یک شب پرهیجان
[
منچستریونایتد
⚽️
🆚
⚽️
ایپسویچ
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139262" target="_blank">📅 19:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👾
تیزهوشی و تلاش علیپور برای ثبت این گل کافی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139261" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
نگاهی متفاوت به گل‌های اول‌ و دوم در برد دیشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139260" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139259" target="_blank">📅 18:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwgvUc7itGD_zfVpuonraY8kvzC-rGfMVkuCxxNvwroiz5kXX7TXn-RUuYRU_LaxFn6CJ-iZXrggMqX_o0V1k0maMJkg2vouPJq48EzQ3o6YtGlGpJVw3DAY52rEY87HLkhEFewe2d_WIut6_hq8nG9uVQkxG7ynYQAnngMNAFfFTOpk0XGNCNhG_9LAg-A21Gre7PgXTTxpOyMzQAkwjeGZCY8wHodRXHLh-xtVfe-9QiyumFmFv7oq_n1PndeMWe7Mae1ZucQb-m2LtNhNHWI2K3k2lCq-zt2GFGbTTz5xzWFRL1JEZv0jqyTiQUmaxJHHS9bxpA4oTIais_rpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال مادرید آماده یک شب متفاوت!
⚽️
مالاگا میاد تا جلوی کهکشانی‌ها وایسه، نبردی برای شروع قدرتمند و یک برد شیرین!
[
رئال‌مادرید
⚽️
🆚
⚽️
مالاگا
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139258" target="_blank">📅 17:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139257" target="_blank">📅 17:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
عبدی : من زارع هم میخواستم، پرسپولیس گفت نمیدم. هاشم‌نژاد هم میخواستم که شکمش رو عمل کرد. کوشکی هم جواب تلفنم رو نداد. حسین‌نژاد هم بعید میدونم که تیم خارجی به ما بازیکن بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139256" target="_blank">📅 16:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
با 5 بازیکن چگونه برویم تمرین کنیم/ می توانیم برویم گرگم به هوا بازی کنیم اما فوتبال نمی شود بازی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139255" target="_blank">📅 16:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
حسین عبدی: 23 بازیکن دعوت کردم فقط سهیل صحرایی، مسعود محبی، پوریا شهرآبادی، پوریا لطیفی فر و دانیال ایری آمده اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139254" target="_blank">📅 16:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139253" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139252" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139251" target="_blank">📅 15:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139250" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139249" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
تیکدری دفاع چپ پرسپولیس در دربی/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139248" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139247" target="_blank">📅 13:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">☑️
پرسپولیس برای دربی اردو زد!
🔻
با تصمیم کادرفنی پرسپولیس، اعضای این تیم بلافاصله پس از پیروزی برابر ملوان، راهی اردو در هتل المپیک شدند تا برای دربی ۱۰۷ آماده شوند؛ تارتار بعد از کسب این سه امتیاز به تیمش استراحت نداد و باتوجه به فشردگی رقابت‌های این فصل،…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139246" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139245" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIaiN9-WVNNkXwMd25EZqgQUgGRhDLXbxtvZ64p3h2FeYUZ4gnSufYfii-e2cQRnUAap6kCIOnAZ4WPk7OIOk4c9Q_czMSyhx_IIFQCESChzfiDK6Qgvtnv_l-N6HbNU7f1nyjrh0Cbv3ZfXmBkA6yDIQz4-uaq9MLr6wlnTEeV7xuo_kh8Ue7VBLOt0WB7N-YwLFZjW96Y6MTcvpROW5jlKx2c90Nfu1CmrNu3RtUOll7uvgFeJC6fZyXkeCdFOldQ_gOF8UzXI2aAbSDsKo-MYVylaQKAbAGFx2yNlaYucAnAhoJc9SsRFl52tivD6ckDhcaLHI6n7w-yDVke9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی علیپور با نمره 8.45 بهترین بازیکن بازی پرسپولیس و ملوان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139244" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🗣
🗣
با تلاش کادر پزشکی تراکتور؛ مهدی ترابی به دیدار با پرسپولیس رسید و از روی نیمکت بازی را آغاز خواهد کرد. هاشم‌نژاد غایب است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139243" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8aZlAxcaZfJoNAhdOYAWgfm0mftHQwymTn8GqoV1X6u3T0gGtX5vCDkqIGDX1DDcNBHDXi1MqeYsJgfqs_3QI0Q1sDll9PDryVknkI_3xJ6Lm2BhPscPasBYtMMv2hZHRoN8YthPHkCBM8jWLUDF7pEimzQRR5FuryvBZ7MSlUWs-K9WoT9sf64CCy8pGtKNv_4f-MyYlkboy5653hc48ZZ1Z6zuShlvcuRV_8ehqEzWnpf7vKPHPzi7L6eAuoN7vr0rsntt6WMBUz52Ipf_yBUFDznIYHqOkpIw75MuYQqbR0KkRGlV0zdlSWvVwuhdNJDKUIJrm-EKBS0IGXPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در آستانه ۱۰۰ تایی شدن ؛ علی علیپور به رکورد علی پروین در پرسـپولیس رسید و به دومین گلزن تاریخ پرسپولیس تبدیل شد
✔️
✔️
علی علیپور با گل‌زنی در مقابل ملوان، در کنار علی پروین با ۹۵ گل زده به دومین گلزن برتر تاریخ این باشگاه پس از فرشاد پیوس ۱۵۳ گله تبدیل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139242" target="_blank">📅 10:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139241" target="_blank">📅 10:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5yfBgwPzuB6YeHDCyyiqnWgw6xGYeAUZzgTvNkHeTASyFwZTSHS8ebEIF6ChNrCtqRTNtcQRDNsr3ms4SNXTWf3ZdcQGJIqudZgm7aQC6a8Bd5VLluoo69WLTCf3oErqA2r9xGiYdLjhpj4d5TIRT8iXy2BLBvPpVs5RSr7ITwft2rAh2hLJqyuRdcyRG6hppsnFMxdb5UMZS3B3DTi0WVZtlK10Aw-SMjqfkq_bmTwTFthrk2u4NJKL-mOx-f2QfxuS7al4oSAUyQZIx236iJVYpQG5grK8a43lntIND2H_o1KDUrkhMqtHmfXSqVQV0Y5ErGULIJE3uSmIJVTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139240" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
اردوی پرسپولیس برای دربی بعد از بازی با ملوان آغاز شد و بازیکنا به هتل المپیک رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139239" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
