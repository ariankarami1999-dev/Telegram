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
<img src="https://cdn4.telesco.pe/file/gdnT9a2Km1EtncIAXjVOnE6Lc0Ze9DqLecu7qYnCJq-PKi2RzFoEVunvyIwdly1cOkQRqutN85nT5l-ZCFs3Z1yLK5iCkwvdiMBCLdsphUX8fPx-f2ORJxMUuogRZ5icsqPUqCGO-VpzbcjhYQgugMFup_SoEQLz5XPfEjp4m8vdUR6ToyDoYD19W26lZH_sAwQknm3DiKNF2GVmocG2hqjG0wOGpQQFK84RDI-QXtjMwgIvlrIM8CfeILo4qF4ok_cGiuNCisxnhjkVc-3nnwMrMMmtJOIdU84VaSl7eZJS2wjlxUBanT4LgyWljta08O9vOHQRliKp-JALWb1l0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 02:01:21</div>
<hr>

<div class="tg-post" id="msg-136966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/How2Y_aywMHhyJrCnUK_N89OMXVn3CTCqUEnTZqnVdBRaxk54_b1KZ88Q8St7Ob2G4LEoIutXKduF_JMuZNroVJGfh7zCsQuI7pPYQEZdXCFer1HoDBt2bvWk5Q-1UnHUk9fcKO4CBJhp9Zebiyp4ZD6Sm1nouutXKQDjCx8y8ON9Y0UV_u24Pc0_vs0QAW5HcBlx4hOBf5v_or1Wm-bGl9oQ3KiphT6SJhWVpdsuK34rz7tgSIFdbW22655Hv-ycop0LwAa4GJ-xvVjBZj7ByOdzxB66S0xWfbkD18_R3cpa4orWYdak7T3XfbeGEKs6oPXwlTRR4_X7mmFcrXEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/SorkhTimes/136966" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚡️
⚡️
قرارداد دنیل گرا با پرسپولیس ۶۵۰ هزار دلار است و این بازیکن اعلام کرده تنها در شرایطی حاضر به فسخ قرارداد خواهد شد که کل مبلغ قرارداد فصل آینده‌اش را بگیرد. گرا در مدت زمان حضور کوتاهش در پرسپولیس به اندازه‌ای ضعیف ظاهر شده که نه تنها باشگاه‌های لیگ برتری،…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/136965" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/136964" target="_blank">📅 00:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
⚡️
شنیده ها: با درخواست مهدی تارتار؛ باشگاه پرسپولیس فردا برای جذب مهدی گودرزی اقدام خواهد کرد
🔹
پ.ن: گویا خیبر هم مشکلی با جدایی گودرزی نداره و به دنبال درامدزایی ازشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/136963" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚡️
فوری از مهر
🔻
برخی از دلال سعی در فرو کردن قربانی به پرسپولیس دارن ولی تارتار گفته من چهار تا هافبک دفاعی دارم و نیاز به این بازیکن ندارم
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/136962" target="_blank">📅 00:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
شنیده ها :معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن باقی مونده.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/136961" target="_blank">📅 00:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/136960" target="_blank">📅 00:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svc8ZydE7O6lw5fATHojFTrWEvq7o4ZXcy_dcqI4p5YEXiyL0KsGO83FY6FMVFjqKh3Smzxeek742hvfJcwMUlEHaAscIxgF7zXHjOKJd5HRqy_v-JiaWX0rHKHiu1AVDMRbjTKtrEbq0Ve_lKhaV6LtcGafejwvySkKjNCMKZT8ny8NvLdvDTSYL5O9UYrqeHUgR9x9J64JA5ArPYRhjJ2xX_4Q5cSXyAESRWzqhuJ1M7rU3Z1lRb99aJeNP3qRz0ngQd-4jc4tTYDkRmYdjO_3pmfZkv4uWTBG2VYik37D_S8lpR28yUiyS4g_jGciw60Z5ZbnTZ08vKWc5efxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
سرخ‌ها در مسیر آمادگی؛ تصاویری از تمرین امروز تیم با حضور لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/136959" target="_blank">📅 22:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🔴
🔴
دو خبر از قدوسی
🔴
امیررضا رفیعی به احتمال زیاد در جمع سرخپوشان ماندگار خواهد شد
🔴
🔴
تراکتور مشتری دانیال ایری و کسری طاهری شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/136958" target="_blank">📅 22:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS2KPc61AX5JrVl_Hl3tZXzCftO1iUEqFZSzHvyoRPpXbL9KCYyj9ELsHIQ6uJQY0ydJ5Y41NgMFAt8WAsVyjK2nR9D-NGUpC-fSvsxswNY22mARCtl_2WLGeW9SqXGBvcqB6Rt_JFDSWzxt_jLVmADNFGVRchZTo3RANhU9xd8GG2cs19yB6kWhW1wAuXp46I2CvXZclnr-6VpvqLgq50Yc_iOQROJAjXcgPMBPUHySqCddiulSaM7NjjVHPAqHuDsKjiKG0K78-oKfWGUxuJNrBWDevOLzEkdVAyaBxwxqD8ozfd2i2UGi_wFtxw0X39a9C8h3HnFhjqiU2rKuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه می‌کنند. این چهارمین بازی دوستانه پرسپولیس در فصل جدید تمرینات خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/136957" target="_blank">📅 22:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚡️
⚡️
خوش‌آمدگویی پرسپولیسی‌ها به محبی
🟪
🟪
کنعانی‌: بازیکنان جدید باید بدانند به چه تیمی آمده‌اند. خوشحالم محبی به این تیم بزرگ آمده و امیدوارم لژیونر شود.
🟪
🟪
علیپور: در جریان بودم که محبی چقدر دوست داشت به پرسپولیس بیاید؛ به او تبریک می‌گویم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/136956" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/136955" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
محسن خلیلی معاون تیم پرسپولیس: دیشب با یک مدافع جوان قرارداد بستیم. با یک مدافع چپ نیز درحال مذاکره هستیم. با یک دروازه بان نیز به توافق کامل رسیدیم و به زودی ایشان به ساختمان باشگاه مراجعه خواهد کرد و قراردادش رو امضا میکند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/136954" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
🔴
تارتار: حداقل ۴ بازیکن دیگه نیاز داریم تا کامل بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136953" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🔴
🔴
تارتار: حداقل ۴ بازیکن دیگه نیاز داریم تا کامل بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/136952" target="_blank">📅 22:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚽️
بیژن طاهری: مهم ترین دغدغه ما امروز جام قهرمانی لیگ برتر در فصل گذشتش، از سازمان لیگ خواهش میکنم جام قهرمانی رو به استقلال بده چون ما صدرنشین بودیم و حق ماست
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136951" target="_blank">📅 22:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚡️
۸ خرید پرسپولیس در این فصل راضی هستید   پ.ن البته هنوز ی دفاع چپ و هافبک بازیساز و گلر دوم به شدت نیازه و جاش خالیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/136950" target="_blank">📅 22:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff7jaDRdIyY9aipgGmbi1AS8fA6YdW6jpT8TCY7aRCIsPkt8M30wBMlhghlpTqGJ8EXFHIOxR1TINnEuiQ13dShtxCyqJ3d_4BCwM_b5ajTtT7otiRFyu-XvE_sCQAXcgTWJUTRt9RttI2tIgQnbB9m2MrSiqTQ4n7_bdOKAqz-LOsJ3BScDcUlFCkdK52W2TFW1WrcsemBjIyCcp9kx6AGYsB9_eHkJQhDQrpkaDXlogx9H2y623IWciOWCNjZ7-YLi5raYtwoRiKaR-3rJIkrSogloJ01h-R3gWBlw6mkO2ryhLN0_EPS0CpLsKuVfSx4r-y808syhKb1-YFc_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✅
کسری طاهری رسما توسط نساجی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136949" target="_blank">📅 21:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
🌹
رسمی؛ دانیال ایری به نساجی مازندران پیوست  پ.ن.... و همه سرکار بودیم و از کسی بخاری بلند نشد برای جذبش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/136948" target="_blank">📅 21:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136947">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات، نشانه ایستادگی در برابر تجاوز است. ورزشگاه تختی تهران بعید است به لیگ برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136947" target="_blank">📅 20:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhF8tTltkw5Dlo-irWsqzMicUDXDkAGktPBurdjOYKt9-J6qcLDo3JAaNEe-u4wk4sOmnlbYOh_IgzxlWfgRBvf_YBpAY9vs4mBUndgs9sU435b1TMn8sMEOAztbf2BdxxAwF1TT0Vod3lAy4GDI5HdTnMLoblmd9TZAWQ8g6BHiTTPVicrvs7R14-yQRc7y023AVTCKxFSQpHyL-NnF87-bXvtUbMyscV5S7JX33zWqYPeCDM9iQytUQ3I1igO0c8aerONsD4Pcex961uR5UDzFGhWvlDsIv3DW_48fYDMK3_FFpXt7cNpXBHAeYqfRqvLB_nyf38N6RInbP4AKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
⚠️
امید عالیشاه به ذوب‌آهن پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/136946" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136945">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWHX2C9zt9Gwtp9lD97ma9lju_k8h6jIqB7M-1VKVhp_QeSLHHBux0ZitiJw3-4xFQ7hMORfzLYLlbJReJyB09AYIbw42VVaouMwq36LsJXBImBJH7DZIW9sXS5ml2l0LKYf3Fdp7WIK9nOipbg3kRfqEu1Vaaiv3KC5kVclT1T6DPeU5_dEmr_ZMUacvayzevBOq85s4Yxo0PybJaCIfauE9sqlzSeb_q_nKfur-Fdt5hTZ8Oc4-lYfaC5qgL3RoG-05s8aFSkqxWJKT6VwjBLfoNjxm11NMD3AAReIUybh3zrVSCgnKeEFtf2dKv7J3ofGxdmO08xAiaUv31ClDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🌹
رسمی؛ دانیال ایری به نساجی مازندران پیوست
پ.ن.... و همه سرکار بودیم و از کسی بخاری بلند نشد برای جذبش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136945" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136944">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHXpUbRP7w3r7Tp2re79ySi9elRXrVn2yc1hfc29LJcsVyHdt_JaT7nw0zAs68Z0Q0nNjLqXJ_mJrYaDDE752OjcBDxP0OqiI1ok9BQ-ATatg68_Y-TN5agG_kUqxOGN4eYRmmnObg46mmgilIwv2MObb5LdoGxbHZaTzG0QCnMzWGQxcjEukXrvIVKIL06St3XYsfCghz9IWhvlTbp_1w541Zf_qZ5rXBsJ_VUOiM07MGwJibo1aE9LPMgakmMXb9171JvFWvwEhjASI9a0K0-z-U9f0BxEUqGB4De1qioPhyfpaye2Rfj79gXhZQs9Pu3p4b8OumY7WSxC_DFfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
امشب خبری از شانس نیست؛ اینجا فقط جسارت، تمرکز و یک تصمیم به‌موقع برنده را مشخص می‌کند…
🎾
امشب یا فیلس دوباره قدرتش را به رخ می‌کشد یا جودار انتقام باخت در تور بارسلونا را خواهد گرفت.
🎾
Fils -
🎾
Jodar
1⃣
هر گیم می‌تواند جریان بازی را زیر و رو کند.
2⃣
هر بریک‌پوینت می‌تواند معادلات را به هم بزند.
3⃣
و فقط کسانی که زودتر تصمیم می‌گیرند، از بهترین ضرایب استفاده می‌کنند.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136944" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔵
🇮🇷
باشگاه نساجی مازندران انتشار این ویدیو از دانیال ایری مدافع جدید این تیم رسما رونمایی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/136943" target="_blank">📅 20:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=oh0BDKA8n_S3AkscahsLy5StJq7MIEiEncj4TTuUEuJuVaZRY-BYvqMj0lgx-eY-A1DWzgV88FS3YQvfdnanVxWcwF040Aj7JpNXJz97OHln2EiTFheYfRyFJjxaLEyigg4aligguFzfI1NJWCbWvYS26MIEkUkHcURA6rqw6-gPUolelceqYUKkGBwQuT-SRPmXCHkoWgYPgNauPR551lwF3Oh-WndsXX0qYROeDOoyBUwKjmqNDSHTQYLlZ5veErp395am1iK3lR0Hliv8t3gFMzKASySRPwx3G3fNXFlv486wC-CMRKQ3-reQrTenEG5LQwQ0qxXPcSyZ59TFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=oh0BDKA8n_S3AkscahsLy5StJq7MIEiEncj4TTuUEuJuVaZRY-BYvqMj0lgx-eY-A1DWzgV88FS3YQvfdnanVxWcwF040Aj7JpNXJz97OHln2EiTFheYfRyFJjxaLEyigg4aligguFzfI1NJWCbWvYS26MIEkUkHcURA6rqw6-gPUolelceqYUKkGBwQuT-SRPmXCHkoWgYPgNauPR551lwF3Oh-WndsXX0qYROeDOoyBUwKjmqNDSHTQYLlZ5veErp395am1iK3lR0Hliv8t3gFMzKASySRPwx3G3fNXFlv486wC-CMRKQ3-reQrTenEG5LQwQ0qxXPcSyZ59TFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇷
باشگاه نساجی مازندران انتشار این ویدیو از دانیال ایری مدافع جدید این تیم رسما رونمایی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136942" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">#شفاف_سازی
⛔️
در خصوص محمد قربانی خیلی هوادارا میگن بخاطر اینکه تراکتور تقویت نشه ما باید جذبش میکردیم، اما بودن خدابنده لو،باکیچ،پورعلی و لطیفی فر به هیچ وجه قابل توجیه نیست جذب قربانی
🔴
البته باشگاه قبل از جذب پورعلی و لطیفی فر برای محمد قربانی نامه زده…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136941" target="_blank">📅 19:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136940">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPi2g3W85qHK-wntr1FqXFEEmznINw32pWqYF7OfTI3U295nsnLhgjx1r_ds9zx4wsuZCnm0sd09CYKbmbx9HazqacsMxlHjnEAmrs27lhCFEirZcnmVu76h_02VjK0074gj3ZGuBar3zqXofgC2hXeS4Ml07cna5CWZSmfLLZD9Zu-lDn0an2yN03UfgFmM372CA029YYHDPgFVH0lwEN8je9_OlHrwoyT_gV5P5-NfoucpKIcbv8PGGYY0uWJFmxNTdPTinUgODZUN8RsWzcHBbFuyVdFTex3dc5bWAk8ydvKu2h8Mn17M1LOI2Yj-3rQ5vkOV2Np1lkzg3swGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت عدم جذب دفاع چپ، از همایی فرد برای دفاع چپ استفاده میشه
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136940" target="_blank">📅 19:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚡️
⚡️
#مهم | ادعای جدید ترامپ:
🔻
ایران در حال حاضر با ما در ارتباط است تا به توافقی برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136939" target="_blank">📅 19:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136938">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2oSdueqwvDb524GJInml-G50IiGpdha_i0HJSyfywVuOyKEhRD7DcTRGz0kwI7VkqYwmOwUnUKHw7TfFO7CwPY2alN7bW_fX2q8JnBgNtk6NSnR3n291vvvB_QlxwtNpCtvCAw3zIiGbH0t7yus8QoeCfOHUnEkkt7T6k-FZetQTYgqSM7Nk4IaX2twenuMJ-U83yOvQGi_9AHVGNq_Mat6rSbbeH3EUbSEQHIfTQ9hzbcwbqjPGI1cgZgVomA87yZJnE_N1ywexhSYhay6zo6CArr7_EHN3Z68XNlz8WtoE52fNwChZbxWN52aUiyRAwJge-ppNnN6AIUcNCJd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۸ خرید پرسپولیس در این فصل راضی هستید
پ.ن البته هنوز ی دفاع چپ و هافبک بازیساز و گلر دوم به شدت نیازه و جاش خالیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136938" target="_blank">📅 19:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136937">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136937" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c4177448.mp4?token=gQtnWJD-fzLht7TOD206Ud67gHJP1pVNP9jO6-WcJZSujiV9tNy2gdDCMMMfB5R0f_c7rVr85L1Em5xUA5cRzyo7YqBS10cGqywdDUwllgswZIf6SZttU0I1nrhoyxLghJvFHYWfx309yRnqyRa7qT48dvkJ05GWlWh5l8auuZ1R_NmEUZlH7mJ1v7aH4ofiXweXHvWEHxlyuT_Am7Sf699RVyZChX4Gd6raOA9ckzW0ZLJletracoxLT9xFA-vlAhBrCkjqAFWKAYVP76YJtsLV89XIZMdYqCsIb1j2nz-0XqiGWz8QaHRgz3FPuX-vZqdYi114EVdORjwZRiYbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c4177448.mp4?token=gQtnWJD-fzLht7TOD206Ud67gHJP1pVNP9jO6-WcJZSujiV9tNy2gdDCMMMfB5R0f_c7rVr85L1Em5xUA5cRzyo7YqBS10cGqywdDUwllgswZIf6SZttU0I1nrhoyxLghJvFHYWfx309yRnqyRa7qT48dvkJ05GWlWh5l8auuZ1R_NmEUZlH7mJ1v7aH4ofiXweXHvWEHxlyuT_Am7Sf699RVyZChX4Gd6raOA9ckzW0ZLJletracoxLT9xFA-vlAhBrCkjqAFWKAYVP76YJtsLV89XIZMdYqCsIb1j2nz-0XqiGWz8QaHRgz3FPuX-vZqdYi114EVdORjwZRiYbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
بیژن طاهری: مهم ترین دغدغه ما امروز جام قهرمانی لیگ برتر در فصل گذشتش، از سازمان لیگ خواهش میکنم جام قهرمانی رو به استقلال بده چون ما صدرنشین بودیم و حق ماست
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136936" target="_blank">📅 18:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136935">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwOQk5rLsBErfxJ29c6J3JBiR_TN6FO0NaewXtxJit9p_mZ1XdVI-P2SU4U86C8uBFyw_KRjbPjyyBWNGHhFKOIRexlF_9MuRBNfkHqigHD_AkI8q96g9b0EBuQDm2NulhRbET7kCm8KpHGQYmQktM5gvpezmAsjnrGTbkRq414XDd_bf_jPEh8v6zGIx3dFMH6538u-nOwZkYJ-wElnZENFuyLBAKRBFdLPkmx_8MUormqQVJcmyhHG_bbudaPIT0UdbnOqsARJ_HGXz_LwMeWs9UsD_Eg9HXiSVBCjLMy4_dMYJw87UBRK_hmcqhahVI2OABzoEY2uc6E3eCWPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136935" target="_blank">📅 18:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136934">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136934" target="_blank">📅 18:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136933">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136933" target="_blank">📅 17:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136932">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQOps95sVyd6RVr3uwlPUmmhQ8mbAs2dou5jX3o2w4oKmPfTiz3xLL3Abz26hrrBRNrx1-yOrl65AyuOwHT2958wnWkgMptfMvfLPhd4KzJcIE_tvdn_ELejjaQ-2FWE2JjNFgJkp7dgBWPDx9Ulu2LkHLRXMs7ZvLqCwyny5wWPwRPRmluFit2p6ONbgyuustwlXqSVa9_XosXzYQz7sUhppF6YSyY-UZwHywVK7MruO93ND4gh6o7E9mbijqbMzUqc6SKcsW8tj3Exm4FmTmojtAlIZGw339gNwSoC3Bx1ZVLc_YaP_Tz8p_eETFJgl5qDAdbAOU3GYS2wAs9Cew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136932" target="_blank">📅 17:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136929">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136929" target="_blank">📅 17:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136928" target="_blank">📅 17:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136927" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136926" target="_blank">📅 16:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⏳
⚽️
پوستر باشگاه پرسپولیس که خبر از یک خرید جدید می‌دهد
🔄
به نظر میاد محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136925" target="_blank">📅 16:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136924" target="_blank">📅 16:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpusU_zH6AKFacK4Cu3B0WKS-iJumvJUKBk8RTZ2fUaRobvHcKe08KRP8_qVU4hNdfWedEVvEGGtv6OpLd02FEN96PhoMnL23xMwrzeI5KNR5OPocH6FQBo2scwXaQRBGfUfjUizhvm6th8FVmoPqActB4WsVGJXj8mj1kMaNEwjIK_09XPi8fCpFPx4N2OwUC8wVQkEazzCz40gEgrSdZgMsaDiC5rPwErgBvk-USB2JocXsRZS38oqY9o_iH6J0F4Njxz23xBe2elEO9Ju3Qzze3P-rnZ88WNtKqv1HfIHv95E1907hv-eBE-msy4whMPNgbXedbw4EthWrYTuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
⚽️
پوستر باشگاه پرسپولیس که خبر از یک خرید جدید می‌دهد
🔄
به نظر میاد محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136923" target="_blank">📅 16:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136922" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚡️
⚡️
⚡️
شروع قرعه کشی لیگ برتر تا لحظاتی دیگر
⚡️
قرعه کشی لیگ برتر تا دقایقی دیگر آغاز خواهد شد و مشخص خواهد شد چه تیم هایی با هم رودرو هم قرار میگیرند رقابت های حساس و نفس گیر میان تیم ها امسال بیشتر از سال های پیش هست چون لیگ هجده تیمی شده هم بالا جدول هم…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136921" target="_blank">📅 16:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136920" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚡️
قرعه کشی لیگ برتر امروز ساعت 16 برگزار خواهد شد  ببینیم دربی و بازی با تراکتور و سپاهان هفته چندم هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136919" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💠
💠
💠
✅
پرونده ایری و طاهری به حدی جنجالی و پرحاشیه شده که مدیران پرسپولیس فعلا هیچ رغبتی به توضیح ندارند
🌀
🌀
عصبانیت هواداران هم مزید بر علت شده تا برخی از مدیران ترجیح دهند اظهارنظری نداشته باشند.
🌀
🌀
وضعیت به گونه ای است که حتی جذب محبی هم موجب ارامش هواداران…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136918" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
در مجموع با توجه به جذب نشدن اخباری،رزاق پور،اریا یوسفی،نوراللهی،قربانی و...از دست دادن میلاد محمدی،ماندنی شدن برخی مازادها و متوسط ها و جدایی بحث برانگیز پیروانی و برخی بزرگترها، اگر ایری،طاهری و محبی هم جذب نشوند نه تنها نمی توان به باشگاه نمره قبولی داد…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136917" target="_blank">📅 15:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136916">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136916" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136915">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4NH0NOZ0yH7ZVC_6Nk7h67Gnq1aEqHTR_neWgcx200qq66nS1y3Gt0yMLyXfMPfuc1_R3V26mBJXqLb5eO7oRlIfwW719PgTywyx7Qs3Y4wynrZwgfIgJ9GWr5TxCdtt80YOS4rZ4rH2Gexu_GMAbbkSOll40Tk2n6g167AMTiDIrJ5VMdsFgnIV8ZQym9to-0jmDwsmuGCLRwlY4Y9h4lxGj62sd0cP1bZZ94EyxZFeXWKFeliJwfBxFGsOQ-JtlcStHwNYt_rlOWEZrF1Qn5CukN6jpMYJilx7xKHJrpWfNlUG4bwzCalAIDckcuz1rxauPO0HbnufOt9mOr9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
منهای ورزش
⚡️
⚡️
طبق گزارش‌های منتشرشده، اپراتورهای تلفن همراه برای اینترنت بین‌الملل ضریب 2.7 در نظر گرفتن؛ یعنی اگه کاربر 1 گیگ اینترنت بین‌الملل مصرف کنه، 2.7 گیگ از حجم بسته‌ش کم میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136915" target="_blank">📅 14:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136914">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EikYOt0c3vauYWK8VyOwhybcEMlzC49_qnGac-qUHYXH8Dcji20oAiS5lyFFhS1M7_sUNp0N9Eo8x97A-Uc7uc4Cr1UVGSluZBCl60TS7xIEV4VZwuEZFPR56RA-O9YwxHVKOyK6sLVm7kTbiQzq2ekjlsvKQrethG-4WQ9WxqzAXnOEyUwDf20ryWpAvG1MEBNqVWhMHo3hxz-DD4ekNzEkkD6gq33N68bnZd5-id7H67gylVRWJenqwPLUnO2KdrAQhZ8KZWCIi5P2m__qtVLd0MXXFvgRHZJVvcnBG7zzztu1xumTOhGLcgym_imK9UzVIbO3WvRBfrwwWjujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
از توپ جدید لیگ برتر خلیج فارس رونمایی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136914" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136913">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
فوری؛ قرارداد رضا غندی پور با شباب الاهلی با توافق دو طرفه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136913" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136912">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136912" target="_blank">📅 14:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136911">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbObDtNFQ5ErbSnZ1wiVnRf398shk1TEg6nB5pHQ88MtXFvWtgWyk19B_R7HsJ__FbZU_8uKHul-xy_fT0rLGzCpvcy9rzFa-lyeMgpKgwHgKjPv_A5RBBXZXhZkzX99mkmSZrMlwn1lhXOF1AMhA8FpWOJKnwHoxtLBLBNddm2oyYDRFR7krIPl2Q6c1VqDeW3a_ejbkcA_rQVNCflLihIGCm0splvvQoyCtZnL4ChvclM2fGab4ah6GD5XknFaTy3U3w4gp-pFY1UzxMij2IwV4bTsyTrxyjrmwPVNcbIDv24zD24tf0TsJPe5bjxAkYKhVlkQ4drxm5XvIeSm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136911" target="_blank">📅 14:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136910">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136910" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136909">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnsRhn8Dz5DoXPrBjxYmgvHn7hhx4OtEsmm6FmWrDd-srF84k8FMD3YYBKxtDjgE1vQvAvkOuu6k4hYqve61oJtwaSmf2tPyHMiWtNXmGci1sL83ysH2tJLcYmOysH0tHrcpejKo1PGgu8l6FbJ2ZEcuLXYU5O8MoglQXvdhnudhn2RGxpW5GRFxcfyaoaib9CmeCJD_IL4_dwP2oeMvdqLkMxcdU17uO0iB7Vde8U93rBDUv5zrzGGz5HeJYpQDmsHuVoZ3AhYKMgHyUxSRGhG486UlcN_1ACVqPUSoXCxLIXJUmuvp5mM2Tu4XTsjfbRO4yfpQDnsPWMtPffw0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136909" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
گاف نقل‌وانتقالاتی چپ پرسپولیس را خالی کرد
😀
فرزین معامله‌گری، بازیکنی که در نیم‌فصل فصل گذشته از شمس‌آذر به جمع سرخ‌پوشان اضافه شد، در اردوی ترکیه حضور ندارد.
😀
این بازیکن به دلیل مشمول شدن برای خدمت سربازی باید دوران خدمت خود را در یکی از تیم‌های نظامی…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136908" target="_blank">📅 14:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cqaqyon4O1Q8cR1a2fUojLsefxqiZfOdmFNS0ThgkHVShL14ktb_0onWRG7cnJ2WPoR833vhUJWLgAIAvSERCzP1_tqIH4EstYpGVkXZpgzhiYb1f2-3RGQ_ZzMRxj9LCQM67vV7-vCNSxqJGPyOxEmoHAUl0oIgjuMfx7q6DHpthXQLTYkMA_1GA0QOnaqfSeS8hYha_TkIyDMzFjk7-2qonUoUf9--sXFUuZMDLXe5u4bF2wPGE73rFwxxCOuaRuz9CfyepE4lv3RFrg12oueKIEVc546Czkt5zF8B7p6rn-SJ6kY8T01rB-iLA4zghWUZu7BONDqX5EfQKweoRA.jpg" alt="photo" loading="lazy"/></div>
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
-
مزیت روش ورود از طریق ربات:
👇
• ورود مستقیم به سایت
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136907" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAiRWDZioq9Hb54ygOoY8xoyP6hvKKk3Qucz5E6nCvNfzZKMqM9COuObHtkvG3skSPIc7u_jCUuIXFordslLjjeOFj62tZYSA1arQq5PE-FFvB746qSlNg2M5VtPdTtEsa6ibBvagBfDeIekTrCmPvdNveow421si7sjt4RZZtH-u0yw3EmwLsZVLl9azd0e5Vm--fVdSVZsGP1YAJsdpA0YFYE5_ne6xa8AzZ1i3gKPf4R6KN6yK7gvBk54iVNIIM3YPp1HUw7npwce7DaMfUp_xtvmDJdQsby2uSfwjZ3jYfdR5R6ATVDibqbuj-7Wkaqq2ETuXN2EM7hcfUhdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
زین الدین زیدان  رسما سرمربی تیم ملی فرانسه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136906" target="_blank">📅 13:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSG-XIHHiwT7FXy4wfwr2fVIrPz1EvuhcnOLioh2aOtRoNrF5IwqPmC5nn52riCvQcJlBr156oCRcafZUwzfrj70PJqWMoCVTZ84FoTApU6t_37Pg_3VgkWoM8SldZXcph1Qr3DDtv7zjsGzIQYo8-F5Y6_fko-4ZK8B4kxCJiTucQa-XPDvcoBzqciDo-GP_1y3vEZHIp2BsDFQWNPgVubZA0pjAoWXluqe5L_SPg7BAR6hKZ0N-RQODJxdMNmnmeNcJWrseTdCPaAgRiUZsTF_oySk6pHNK98BHvfITAV7uAa_AOilCnkh73kukHDOPcDHqk2sjNZXBHLsh1S2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🤩
باکیچ؛ مهره محبوب تارتار، خاطرات ربیع‌خواه برای سرخپوشان تکرار خواهد شد؟!
➕
مارکو باکیچ در تمرینات اخیر تیم پرسپولیس عملکرد موثری را به همراه داشته و تبدیل به یکی از مهره های دوست داشتنی مهدی تارتار شده
➕
در زمان برانکو نیز محسن ربیع‌خواه مهره محبوب این مربی بود حالا بنظر میرسد بار دیگر قرار است این خاطره برای پرسپولیسیها تکرار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136905" target="_blank">📅 13:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136904" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136902" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136901" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136900" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136899" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136898" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136897" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ7bPTxsBCxbNwSAQ6WMMT5PG3r2YZuBAbQWHWJxcC20jEMOOASOUyVm4de1-NagCqm-FukLHkDP4QhRpWOehUhphfk6fZLZ7nGkSglsh7Lm5QrHnI4ULgsdoeuDhRSw4NgPm8MwKONAVefyGrpHwyMKE7qm5cdGEzrj-mQqr1XkhDn1o2x_KCsYwb0ufB6qu6MyM9Dmpj5thD1LKUN_d-aJMM1AOky1E_t6HsTITe9aYOj-PzkH9V7u3ci4faX0uGEg5ZdtBUcYBDph-Ek02OK_Biq5MAXOvSnn3LxlN15ev2cdI2jbVKMhEYv0x2elO_B9Vn9rqkY1u2UJcfBNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی
؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136896" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj6xRLmjBF8Yb-hlsj_gAeKnaRPzJg2Cd58DMLvFdxcxgLj87gJ8ZEh1fnp_ItZVNVsQRJgNTcuHKtdpVK383kkcPWqrcwKEPpJjA_xINVPGigdOAu6kRIkYjmGzqkLJEwVrQ4ZiGpSUNAOHvx71YOSzMPHan6q5e67sxeltZz36fln-sW4aape81QZI-bDjmFD_rfHlFkUNcnUbMVXTJnfoo7th4u9w_AMpmrAZGVpS0AbLumkq2X8TuGFMqtOGcJQvpCKx3y1wVrM_tb7E9XE15Wb5Cr3qOQAkycE59lHYA39JGBrdyg8dnn9yvgOL2Uj5aZ4eggVOUXaku0y6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرسپولیس و الاتحاد کلبا به توافق رسیدند و محمدمهدی محبی بزودی با قراردادی ۳ ساله پرسپولیسی می‌شود
/تسنیم
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136895" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nUre_WzJbSsZ3F4Q9rW-XIJbWlL7_5wqmmbq4GqdCclLc7lX_9CQ2X0e2aSEDTq7Gum2oJWDkHYmSR1vanLmxHE3WOek-1mFOdlgb2gEaeHUyMNNsHQ6yhA_sjog4p58Xw_pxPAfB3Op7rT-3KXyCq70G8bc6acd8WcrGrPD9rnB16mkUbSAhHvAK7W4TPMlvhjakcVMwkjYU5lGWKVDHKYgMEEYBz7X1kJCQgV66JxBsNxCi7VkW_1Z1bNRyPFRyc3tBtC8NvJlQvWpkf3PxbrKLEKFiC_q4gnu3qWT6L69NjK4aos8LuDec1dn0gz2_ilwrGjYJeepkG87PKAywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136894" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uahXPRw1hPIUIZMDjxT4V2eyAsTvRPP5fAB7qE9P5GPaQH2I3mPpQS0WZDujiFeQAePSggEWGW3sSVR_qfKdaz64SlT9Yrf9AqC-g1l4VY8DNl2rwhil-NGhCiTWvC13nYzVloXbfVHHnl_auVQJIV3JRYCndr7sDEW0KM2SePAok3n_XhsDC27EuKV3DnNbx3djuzJeq2-1_RWYYmkawRx3rlrvjb3IkfQA2g3hpermcrrVIy2xeKo5WYRdeS_R6uK-76UalMxmA4u5PkxaOLkq0a65ByDwzXkDYNgeAcpQliNROJ8R3xEMc6BuObartEDJ3GmkQiKf5CqAsxukGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری؛ طبق شنیده ها استعلام باشگاه از وکیل خارجی برای جذب کسری طاهری و دانیال ایری امروز میرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136893" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136892" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136891" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136890" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136889" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⁉️
⁉️
فردا شش‌ مرداد حوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136888" target="_blank">📅 09:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔄
⚪️
🔄
#فووووری
🔴
باشگاه استعلام گرفته و فرهان جعفری تا دی ماه قطعا سرباز هست و نیم فصل قابل دسترس میشه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136887" target="_blank">📅 09:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic5wObw4kpgvKov5Al_s4W_wkBPBbPGMiOOuSVjw7s03fzR8gV5KdjgUi7AxU_t1MgJL0vUl4wwSbJA00bwDF7pdj_juwVECCiw8ZJaIsKshG48Z-WIfBvWvt7pQBprBMzBqvh6nnc4xricmx-PhXVwDdwZ2A5OE-rStCDDDjBmwgbrviXeblw-PTbCX02jARtbSL2kAtIebBsKS4OWQbN6QBNk1acx9vO0G_nMiLy6VzwbcifmYW2T7RM9niwo5BNT3XSwvSoiw845DgwsCsr5nqJSBvqGUfPsvYL0XpBUi2VxriBEWhJLUGapuWkJRu8PvJ-rMGf9KD1RqR4aBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136886" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnp3VZqK__h37aDTbd_p2gdOH3PU5MT3gh9MdzsJ4nse-M4MGBXlO4G6Q6Boi1nJLMp54Z6Haucb-N7o0qK2aJuKIJQh-TB7m8s8P5sPPASc50K7RnhUl1U2of17C2iENQ47X-KyLMBWgoJSVO0TJuVTAGWXlKplErdGIpAEbevpfiFQeP-n7AmiM6zKv6evvWFLtu7dWnmIGKRq-wsBn2okBdEXSKw3RuluB82klN46n_YQhiKNFDooo4EUM4NE3lFxu64c5hKI-JN2918kHYPYqb61xRfB3bBxQpETT54hp-TmyTOhuYX73wuG_Hqa8j8pM6zN0lbRRpxwLDS84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
⚡️
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
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
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136885" target="_blank">📅 01:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136884" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136883" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔄
لطیفی‌فر فردا به ترکیه میره تا به اردوی پرسپولیس اضافه بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136882" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136881" target="_blank">📅 00:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔄
🔄
تیوی بیفوما در پرسپولیس ماندنی شد؟!
🔴
🔴
مهدی تارتار اخیرا در تمرینات پرسپولیس از عملکرد بیفوما رضایت داشت و به مدیران این تیم نیز عملکرد بیفوما را گزارش داده بود.  با توجه به عملکرد بیفوما در دیدار روز گذشته سرخپوشان برابر پیرامیدز مصر بعید نیست که این بازیکن…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136880" target="_blank">📅 00:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWuVpf-Ka3esAGcG6cc18ZucIM5e6Hcs766UEq-chWvxNIe71CqCmGvGccMCuWkpbFDBY1UGoHlaPOx6VNXJwDSKEbYZtpfREhZlMRsy3QJ-ZofqwOtWDOy4EZXJckmwpPewPzrn2XYmTawP1_l5XYV84h_D1VNsVnme-fi2eGvAFN6wTmJd7sHE2CQXWkMbV1DjNylcegXgC19xNMZUFL6M_0JPFJAwbKgmfh1DwZSBmBbJTKnyxTN52RjPsvnR3jRuqPMxQjfaQYvYnNDMYBGJiKUnjDYzyhfgvQ76HDBL6InviJpOQfoIVbGNVuyqURKNQ5fBwpiXet37jqMaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گویا رامین رضاییان به خواسته 200 میلیارد برای
هر فصل خودش رسید و در استقلال موندنی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136879" target="_blank">📅 00:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚠️
⚠️
قدوسی و حقیری: مدیران باشگاه دارن فشار میارن که گرا بمونه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136878" target="_blank">📅 00:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
قرعه‌کشی لیگ برتر ایران فردا انجام خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136877" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWAvITtBec2SmxL1SlUxmtcVfRhXwCdYh75CHoA9P3qB7bnc60hYY1-oI74ae7EGFW3_2DPzYRIB9y4OTf3m_yDC0P23AVVlQNlz26-XxOiRIe9HsrXJ7HpppeuF1SzVJtOQp61avCXMnpHEDzI_KNZ3zG8yAFsPR9-C0qt8fC3J17zvGZfyFxvMNAqx1hTmPQdD1SH2lF9vxFhleN5yVyGfu0zPUhJ7Yl3vVt76ycOFriP4f4srCbbowCP1mGcraQXHWq-84SLNDUaEBWFlcJlG0gEuh8kgXV8CnGtSVLaCzi2vlhblt7TNz3fUy8b2hR02XfP8rC9dfDRCUXS4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136876" target="_blank">📅 23:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند  #ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136875" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136874" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6YbRfLVulZnVnByF3eP23mwXUgwNP5tog3jRkiowrbZyhVG4EHY8Y81Po0RTWG08u2MRvIkYDHKlryYHSx7BZOBls1mXufoH6VWnYIPqVyGAjD2ZYt77OidF32pP65NnRegeH8Q4GN8LoM01kX6CQJC7rKmuCtxtlDNW0e99jMOAv89AeuDpAdp9ZMnfIvT8kzIGflNw-94sKpSIPYuJ9FMgpgv5anplCn8LmHVjFTVIgqVyBHQ_PlV5R-1_wwuhClRu6hwxuwCzKvMq2B8CbDcmeDWO3hMMfsDU1CQGUtMxKBlZbMNtZafCq6YPHQhmVId5snP4eIT867FkKedvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استوری حسین قهار خبرنگار حوزه پرسپولیس در مورد ایری و طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136873" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
گرا در بازی دوستانه غایب بوده و احتمالاً با نظر تارتار جدا میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136872" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az4UJASwbxljLgUNRVsyCKfoJqvDTbItehbzZWhcNXbHZLwGNfuSZwR_UTF2MTUqu_MYP0817GUUnGURHrxyJqAXURRHdpEP98wl_lzhdih9QxxYGF_23Rsz049KDM3zIbAg6Ez8nhkZvuWcV_UTEYviGXJ93f_q_53jVVq5ZamFnJfBFVgsFlS6cAAPK1lhym_SvbaMTZZIMIuaAGP0s7tlJjpP8iB670AhuXVxtJH_DJokgMq5gUQo3Tcbgovi4GE331Ci9BpqMaXFdARlzpqGMHxi58pBn8jF3KzigW4CMoQHb4mZW8ELVNsLJj3XVeNQwjxM_0w1QGEHzcprWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
باگناما از گل گهر جدا شد، نیاد پرسپولیس صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136871" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=Yv2KEhfBrQRaS_8IaOO2NKjYq2mqmOueKEfhoAoVqgAKRc0rwUw06dTYddFoEpqeeRWLA-ZU2yBDBWoEoZwhNokAdMBC5RSbgm4vBEQOfLA4YZMtslCLhuG_r0vqN4MEcYbelebEyoNZlo06S7G1JUqJ0cir3AUhLcU7POfBQAISyH6UTWK2GjajSb-__bc5zH70EP9XwiN3p4jm-P1nJOZ5T5bLpyeKGWyMYl5x6cLigEQ7DA9A0IImIaWPYMwg9lWewC3bYzLvCmYa3VY30vbpKY7zmW0Ld9ASoSJejymDTvUA3R-BiexOFInGU0pkmdIhXrlHReBt_8z15h_n3oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=Yv2KEhfBrQRaS_8IaOO2NKjYq2mqmOueKEfhoAoVqgAKRc0rwUw06dTYddFoEpqeeRWLA-ZU2yBDBWoEoZwhNokAdMBC5RSbgm4vBEQOfLA4YZMtslCLhuG_r0vqN4MEcYbelebEyoNZlo06S7G1JUqJ0cir3AUhLcU7POfBQAISyH6UTWK2GjajSb-__bc5zH70EP9XwiN3p4jm-P1nJOZ5T5bLpyeKGWyMYl5x6cLigEQ7DA9A0IImIaWPYMwg9lWewC3bYzLvCmYa3VY30vbpKY7zmW0Ld9ASoSJejymDTvUA3R-BiexOFInGU0pkmdIhXrlHReBt_8z15h_n3oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند
#ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136870" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚠️
⚠️
باشگاه برای بازگشت امیررضا رفیعی امروز مذاکراتی داشته….!
🌀
چرا مازاد شد که الان…
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136869" target="_blank">📅 23:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136868" target="_blank">📅 23:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahrooooookh Abbasi</strong></div>
<div class="tg-text">منطقیه این عدله و تفصیرتون کاملا
👍
ک پرسپولیس تو پست محمدقربانی الان بازیکن نیاز نداره،چون باکیچ،مملی و دوتا پوریا هامون ک تازه از گل گهر گرفتیم کافی هستن و بلاخره یجاهایی هم مربی این حقو داره ک با اون بازیکن هایی ک خودش میشناسه و خریده بازی کنه چون اینجور بازیکن هایی ک مورد علاقه سرمربي هستن و با نظر وتاکید خودش جذب میشن بخاطر اون رابطه ایی ک بینشونه یجورایی برای اون سرمربی جون میدن و تو زمین براش کم نمیزارن...ولی الان ک قربانی با این تفاصیل جذب نشد اینو هم باید بگیم ک تو پست ۱۰و پشت سر مهاجم حتما یکی مثل محبی،ترابی،هاشم نژادو...باید از نون شب واجب تر و جذب شه</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136867" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🔴
روزنامه گل چاپ فردا:
😀
مهدی طارمی بین لیگ برزیل یا پرسپولیس به زودی تصمیم گیری میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136866" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
‼️
شماره 8 مرتضی پورعلی گنجی رسماً به مهدی تیکدری رسید تا جدایی مدافع میانی قرمزها قطعی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136865" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
فارس: تارتار از عملکرد گرا و بیفوما تو تمرینات تیم راضیه و احتمالا این دو بازیکن فصل آینده تو پرسپولیس بمونن. ( شما بخون نتونستن یا اجازه ندادن این دوتا برن..)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136864" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
