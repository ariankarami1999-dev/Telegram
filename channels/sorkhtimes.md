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
<img src="https://cdn4.telesco.pe/file/QEeGzf522rtUOstugUVlc4i8NUVbKDVXZ78kUk9N_W1hI6DcFIDi6ZJKtQ13yNAV1E0a_DW6qW07uMmk2RKucMjxAdbb-vb1NAiie8Q6v0l4Lz4sm7Y_X54IkvK8Ftrr90PWiq_rD0TrOM4_9cRPGGEX2SQ5-mRxrmnlfovG57yFP3IFBAlUSIltv2uGL_9VHUSEDqmWdNULz7qty95odWjOKOeUQN4l3L66Pq8Ng_n0uazcUIBwNqqEtiIhjIVbEmLYab-7YRoiNtib9QprdAc0kxmwL5Su5xdaaGIaZotv1apy6BqJhc9tIB2A8QIYKqjftVwB8z-robbU7zNOGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-136376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136376" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 154 · <a href="https://t.me/SorkhTimes/136376" target="_blank">📅 01:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbhGB6mDTFJMjmOo-LyTOMQtiTOoEmJByL7756vZYdQHQgGkg7V1dCnQm76hp_uOxTHRIeBlmDUihROtLH_9TC2VT0xBJ056W6HcrVsCpGViDq0Kbn5MWNSKlZsOlS8gMc9rXk9Z7YTo1Wu05ex-TdFABZf1AX9Sbtwt4OSQO3JziVcFa_6vbf4QstPzhNEbultgd9RAksVDgR6n2-taoCjrLfHbfujs_JUpUwT5xDVCIg40TKKLNbb0rZywWxjM6sOX_zxWC0ex4WHIMVS6gCqkuaKMNKkubONHoA3r2vr87X2NCMPzVnMTfRrp727bGJwxmpoKhfvqVNzi0eM93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 184 · <a href="https://t.me/SorkhTimes/136375" target="_blank">📅 01:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136374">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/SorkhTimes/136374" target="_blank">📅 01:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136373">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
امیر قلعه نویی تو جدیدترین اظهاراتش از حکومت خواسته هر کسی از تیم ملی انتقاد کرد اونارو به عنوان وطن فروش سرکوب کنه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/136373" target="_blank">📅 00:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136372">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
قلعه نویی: ما ۳تا دستاورد بسیار بزرگ داشتیم.
🔴
۱. مظلومیت ایران را به گوش دنیا رساندیم.
🔴
۲. دومین دستاورد ما این بود تمام مردم ایران در امریکا با هر نگرشی، متحد و حامی ما شدند. بازی با نیوزلند بچه‌ها یک ربع دور استادیوم چرخیدن.
🔴
۳.  فودبالی بازی کردیم که…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/136372" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136371">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=R70ELsAnLkQFVGIMB2zjdL2UQHVQLSo1HqBsPA7-8eueC5pC3sJZigDcV4rizw0IbwuyXAwLyI98Y75MoVVUZlfIDfK34IFPtj7Ut1WshazRdyHAPW20f1UcxhFXWVa6tXfhvbWafkXcrIA6jcCYBybWmZVvHqbhDrJJXEZZe6U0YnhzKvjA8B-CBjBv9-l3QYNimDOaW-vYenSTpKDlTN7_fbefDNAtqpWi-B4TicERrA6JUFgyxOSLo7Xp1mjT2lLpJSidb2a2AWUeHr2fDfhrzBu1UQD3v-aqcAumWGMVw4tZEzzYBnorMN_OUuN5SRXu80nEPd4XASFQTtLseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=R70ELsAnLkQFVGIMB2zjdL2UQHVQLSo1HqBsPA7-8eueC5pC3sJZigDcV4rizw0IbwuyXAwLyI98Y75MoVVUZlfIDfK34IFPtj7Ut1WshazRdyHAPW20f1UcxhFXWVa6tXfhvbWafkXcrIA6jcCYBybWmZVvHqbhDrJJXEZZe6U0YnhzKvjA8B-CBjBv9-l3QYNimDOaW-vYenSTpKDlTN7_fbefDNAtqpWi-B4TicERrA6JUFgyxOSLo7Xp1mjT2lLpJSidb2a2AWUeHr2fDfhrzBu1UQD3v-aqcAumWGMVw4tZEzzYBnorMN_OUuN5SRXu80nEPd4XASFQTtLseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🎙
عادل فردوسی‌پور: سایت و اپلیکیشن پلتفرم 360 بخاطر صحبت‌های امیر قلعه نویی بسته شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/136371" target="_blank">📅 00:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136370">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
سایت و اپلیکیشن فوتبال 360 ( برنامه عادل فردوسی پور ) چند دقیقه ای هستش که از دسترس خارج شده و خیلیا احتمال فیلتر شدنشو بخاطر حرفاش علیه قلعه نویی میدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SorkhTimes/136370" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136369">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/136369" target="_blank">📅 00:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
گویا پل فلزی بندرعباس رو هم زدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/136368" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136367">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/136367" target="_blank">📅 23:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136366">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
قلعه نویی: ما ۳تا دستاورد بسیار بزرگ داشتیم.
🔴
۱. مظلومیت ایران را به گوش دنیا رساندیم.
🔴
۲. دومین دستاورد ما این بود تمام مردم ایران در امریکا با هر نگرشی، متحد و حامی ما شدند. بازی با نیوزلند بچه‌ها یک ربع دور استادیوم چرخیدن.
🔴
۳.  فودبالی بازی کردیم که…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/136366" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136365">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYEbACOKJJR18ui8LVuJGuNNjlC_L8KMEx1cAetCZ7EmXW5xO4B-Ho2PFTN26Ptx3finrJzWMRXxv0bgwoUgpabU6U9Li3svN__OA9gEP6TnBnAoNeRkBgaYZ9ZKy24yvKwJfpaRmysxIFQC500sihur9pcgLXKmVwitmyq0A9uBaVLpJnaHe4GRHuLGkM4btV0ku_OV2xlmHUsH1b1sBMymoI2bx118T1-aerUvrU985zgE-X_ABIN36qYWQkQYa_Z8MbH9SLMmznTTnBu91uWgkFVGQPFRuXi_VbykVML8bG88BGNFkdGlwgD6VHrKQ3fMnUtFTtv7OZD6Zgb5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سنتکام:
🔴
حملاتمون شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/136365" target="_blank">📅 23:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136364">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
فووووری/سی بی اس:
📌
یک توافق موقت درحال شکل گیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/136364" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136363">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
قلعه‌نویی: من می‌توانستم مساوی با بلژیک رو خیلی بزرگ کنم اما خودم اولین کسی بودم که از خودم انتقاد کردم. ولی یکسری بی‌وطن ِ ایران‌فروش فضا رو خراب کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/136363" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136362">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/136362" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136361">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
فووووووووووری :
🚨
🚨
سرانجام و طبق شنیده ها پرسپولیس و نساجی به توافق رسیدن و ایری راهی پرسپولیس و ابرقویی راهی نساجی خواهد شد. به همراه مبلغی پول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/136361" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136360">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚡️
مهدی تارتار به باشگاه دستور داده که تیم رو تا پایان هفته باید تکمیل کنند تا با نفرات کامل به اردوی ارزروم ترکیه برن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/136360" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
تارتار گفته خودش کاپیتان‌ها و شماره پیراهن‌ها رو تعیین می‌کنه تا این مسائل باعث اختلاف بین بازیکنا نشه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/136359" target="_blank">📅 23:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
امیر قلعه نویی تو جدیدترین اظهاراتش از حکومت خواسته هر کسی از تیم ملی انتقاد کرد اونارو به عنوان وطن فروش سرکوب کنه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/136358" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
قندلی: هرکس از من انتقاد می‌کنه عقده ای هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/136357" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/136356" target="_blank">📅 23:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXidAXHktg2KQrBP6TVSfgXSZhVUGzbeRC8CR59P_HCWA_wqn1uuSIPS-5NZWwpD3WfxuVEmqF2QkBMrQMBjtGQDEG9CBbzTuIYMTjjgACPyLBGGIIm52ReoPFM6W1aCnF-JP05jqBBCmLJ_t4n-QGkkhkS6KDomQluRy5FsxVCIkYd-ehYcPzPD2Hy3_VFC8AipTu8q9SYMZ6eoSpmWmI6lTGyIYWGFFl2cBzUELPZra8AtEInl1vJ2r-n2oT-23MtY4QrT0gPLh0XVbzQ_yK_55qg4-Bvms8WrQIB7n51gApr1F1Xh6uquklttL9wjrcaoYcTprPK7emda0dVBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136355" target="_blank">📅 23:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❗️
#فوری | کانال 13 اسرائیلی:
🔴
ترامپ پیامی به کشورهای خلیج ارسال کرد:
🔴
اگر در این هفته به توافقی برای آتش‌بس دست نیابید، خود را برای یک تشدید جدی با ایران آماده کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/136354" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
سپاهان برای جدایی آریا یوسفی، خواستار انتقال ایگور سرگیف و حسین ابرقویی به این تیم شده که با مخالف باشگاه پرسپولیس رو به رو شده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/136353" target="_blank">📅 23:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136352">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
🔴
اخباری قراره بیاد تهران و با تارتار صحبت کنه و اگه همه چیز برای رقابتی بودن دروازه پرسپولیس اوکی بود قرارداد شو امضا کنه. احتمال اینکه اخباری پرسپولیسی بشه خیلی زیاده/ تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/136352" target="_blank">📅 23:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136351">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
گروهبان قندلی مهمان امشب برنامه میساکی در شبکه سه خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/136351" target="_blank">📅 23:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136350">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/136350" target="_blank">📅 22:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136349">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
#فوری
🔴
یاسر آسانی ستاره آلبانیایی فصل قبل استقلال در آستانه پیوستن به تراکتور قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/136349" target="_blank">📅 22:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136348">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
#فوری | کانال 13 اسرائیلی:
🔴
ترامپ پیامی به کشورهای خلیج ارسال کرد:
🔴
اگر در این هفته به توافقی برای آتش‌بس دست نیابید، خود را برای یک تشدید جدی با ایران آماده کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/136348" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136347">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
دانیال ایری به پرسپولیس پیوست/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/136347" target="_blank">📅 22:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136346">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136346" target="_blank">📅 22:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/136345" target="_blank">📅 22:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
فیلمی که از تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است و در حال پخشه قدیمیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/136344" target="_blank">📅 22:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
مجید عیدی خرید جدید پرسپولیس با شماره 2 که سالها بر تن امید عالیشاه بود برای پرسپولیس به میدان خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/136342" target="_blank">📅 22:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
مجید عیدی خرید جدید پرسپولیس با شماره 2 که سالها بر تن امید عالیشاه بود برای پرسپولیس به میدان خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136341" target="_blank">📅 22:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136339">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136339" target="_blank">📅 22:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136336">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
🤝
پرسپولیس تا آخر هفته با چهار بازیکن جدید قرارداد امضا خواهد کرد / خبرنگار فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136336" target="_blank">📅 22:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136335">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/136335" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136334" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136333" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkpxpQy0RLZQ6HVTlReQILC6KDcFUrW5R7Ec6ieb1frawDEOYqzMqe-u4bpMUyCo0FeyUS-eb3q2J4pzb2GmECzxo92kktMu3HMzG1NV7ifF5vAR4Sf-riBgbWTy6bm7Hq7-ZaMNBAd5RewAU8wmK-fRMfI3DVx98hJlg98C4qVjv1-jDezPrANTFOUrUvX9uGUt2jQ8k_DfPhrTUPm61zAe0BL0SZIYSez7lk3EPsYmkNmgwHQ5psKB2_WK00o3mXp_wBNlLHgI7QnmT2wJuWatgIQ84KTzKi7Sa2ZCtLboQ8lkJ1mcMjDUv4f2dMk3gCWncbetQhLVY6jS8Ajb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/136332" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEfYUS339Qc7MG0k8yy53Mkt19I7reuqKqUf7HBVubkwLm_HPok0B4VUoLn3UKZdm1KyyGHWQa1zeQ-w0Qv5Lk6s_VH2dm53_wAsK93AN6E0qvNorwKEKTeW-lgkVqz60cNmm1StkEtn4BbhUcJ3Ixi64OBDgxd42U-ddtUGuljLXGOizRiSgkjHi5LGkyO4PQNpqpEzXFyDqsNXiQfEYdAKdzM0oyaodmRRZ12B8bUeMYrOlnalXDefA4boU6ukoJnfnsk6EE7zNYeyuNteItjdH7zojtrhx1NA5YQM6_7iIi6xaPE8C2cRmREUF8d-_CpIvipAniTHa5GRzxTRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووووووووری :
🚨
🚨
سرانجام و طبق شنیده ها پرسپولیس و نساجی به توافق رسیدن و ایری راهی پرسپولیس و ابرقویی راهی نساجی خواهد شد. به همراه مبلغی پول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136331" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRbDaoQ9fMsKxFe7UXy7R8bjm5bOHYDdOwx2v3SFSuIq7CvYEpFcPD7jgn3R8Cng9o7hve0wO60WN2OSTumV4L3jghZbKu9gsufp_Cs1fpdve_dMT5yST1lzw-A6HYsUURUcntTBfvhocHGmuqPC4aFfyjSl7XqOYsBhAJ_iaakkSMFKVOv04smw1w1UVKKyHmITJpJiVIGIxKWrCKRl-X4xZ2C0kQwZbOs75VPaR4kpd_gz7aBVpPx-2eZ9b1unZNQZD5-pYRQnLtWw1hShEVn2syOeZS7iD-xSbQQEIsqaSIjr-rFENuddhJjQRuPy3kzqnWfA5xQkuMMEXn15Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136330" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136329" target="_blank">📅 21:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136328">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p01MRwD7mnKCMrm4MZptWsw5fgRVk1tXDBaB7Ksoczt62xB0C5RYzFdwbwcbiGkOHnEFUItK90zMQokdsURKYdaC63KQBrbfxk6Pj-NBlm0euxPqfsVkd7MbI3miWqq-OgH0i7HO7M9-7xPaCGJhlVkuY0udTwPt5BEdwrEMaKarMd3L41uSgZqDAXTlPLDgATDaz7_Am5U1TQZM4eOumk4DsqmVXIdmQw_GSc1Rs2-_-QL8lHlOoE-kdMUm7D6bLcR9BmLtk36h7Sh023TFDWpWvIRIklOuN5gr9bg1zW1WsV9ir6iYBbl-R5DAYJbTTuN-2mbbcFSVvLQ8K22ZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی 2030 به‌مناسبت صدساله شدن تورنومنت، با 64 تیم برگزار میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136328" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
سپاهان برای جدایی آریا یوسفی، خواستار انتقال ایگور سرگیف و حسین ابرقویی به این تیم شده که با مخالف باشگاه پرسپولیس رو به رو شده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136327" target="_blank">📅 21:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از فرهیختگان
🚨
🚨
کسری طاهری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136326" target="_blank">📅 21:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136325">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136325" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136324">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
بمب سرخپوشان/ پرسپولیس با محبی به توافق شخصی رسید
⌛️
⌛️
طبق شنیده ها مدیران باشگاه پرسپولیس امروز با مدیربرنامه‌های محمد محبی به توافق رسیدند
⚽
قرار است در خصوص دریافت‌ رضایت نامه‌ بازیکن مذاکرات فردا انجام شود
⚽
محبی مشتاق است در پرسپولیس بازی کند تا…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136324" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136323">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
تمام تمرکز پرسپولیس روی جذب محبیه و خیلی هم بهش نزدیکن ولی  اگه اوکی نشه کاظمیان میمونه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136323" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136322">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136322" target="_blank">📅 19:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136321">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری / آنا
🔴
جذب ایری توسط پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136321" target="_blank">📅 19:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136320">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
سپاهان به پرسپولیس اعلام کرد هیچ‌جوره آریا یوسفی رو نمیفروشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136320" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
محمدحسین میساکی: درحال حاضر کسرا طاهری رسماً بازیکن نساجی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136319" target="_blank">📅 19:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فرهیختگان:
🔴
تارتار یه وینگر تکنیکی می‌خواست، اما بعد از مذاکرات با یوسفی، هاشم‌نژاد، لیموچی، کوشکی و چند گزینه دیگه، مدیران پرسپولیس به این نتیجه رسیدن که محمدامین کاظمیان رو حفظ کنن و روی خودش حساب باز کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136318" target="_blank">📅 18:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136317">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
فوووووووووری از حسین قهار
🔴
حسین قهار: هدف از مازاد کردن ابرقویی ؛ بازگشت مرتضی پورعلی گنجی به پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136317" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136316">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
تارتار از عملکرد حسین ابرقویی در تمرینات راضی نیست و به دنبال انتخاب جایگزین برای این بازیکن است‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136316" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136315">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
#فووووووووووری
🔴
تارتار علاوه بر پورعلی‌گنجی، برای حسین ابرقویی نیز اعلام عدم نیاز کرده و‌ معتقد است این بازیکن در ضد حملات حریف کند عمل می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136315" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136314">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
فوتبالی: مهدی تارتار به اخباری قول داده اگر توی تمرینات بهتر از پیام نیازمند باشه، فیکس پرسپولیس می‌شود. همین اعتماد به قول تارتار یکی از دلایل اصلی قبول پیشنهاد پرسپولیس بوده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136314" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136313">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
شهریار مغانلو به تراکتور پیوست
🚩
خط حمله تراکتور برای فصل بعد ؛
🔖
هاشم نژاد
🔖
ترابی
🔖
حسین زاده
🔖
اشترکالی
🔖
مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136313" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136312">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxybpTZbjLsPbp6XtC3Vs9eu_owudat32UTwMmxW9wudVFFSXJAr4YDqFbZC_N35Z_2LnHGWJJ2DpVHtbNWy_Xb7AD8jt_3_1s2Dcs5-5CAUB_phm8fjD-TL3IyZO04BIDml0u61BZIovCyD4SruphjUjBaowZT-2Ju0w5Z6gvRxGcyXS2dAfx-9GekPmJjg-HQZEnpXvjBmcPmMwhLBBvB8hz2ePG36grXSYDmAGwZ8SfPDUE5ru0BMaWJKMK0UKfyopgxEaYZ50HZPGv8PE3RASUM9HdfsKbK5EiNEh030NvotkzGPm_LKeDKkS7TWaWZ5NTYxELrsNIM8Si5Vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری / آنا
🔴
جذب ایری توسط پرسپولیس منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136312" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136311" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
شنیده ها:پرسپولیس امروز 40 میلیارد تومن + رضایت نامه قطعی کاظمیان رو به فولاد برای جذب ابوالفضل رزاق پور پیشنهاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136310" target="_blank">📅 16:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZMVt3SRH_7x6xLPZ8T4nWfW5cEkSaxa7FBLf-VfCA7ynoaLfu6_I74Hr14odApydPH6F4oncn_rNbNtyg7nDB0hcRtO__5-GBr79AhZl2Zen-Z1cN1oxsbhJdJaBIJlw5gi5L_okAgWVpD3zMh0HG4iToNMpVjDRvk27IbNNwZ9znsbc6Z5YehpqjcXjYdDjsC-fONPfu1A0e1u-0wrh5Sx4-Aw8vDj0FZYdrOMtj3THLfkqVI0Z0g9EOsBfS04yKGgqY6dLez5AxC_23_S1OhAZpbN5WsLc7nwXjbY7TlxtJvLdKkXl-JH85iCqJf7wT5nySbXhfPmF0tpBX8rHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد عمری 3 ساله با پرسپولیس تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136309" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
پرسپولیس برای رزاق پور پیشنهاد پول به علاوه بازیکن به فولاد داده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136308" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
شنیده ها:پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136307" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136306" target="_blank">📅 15:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136305">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
❗️
دوره حضور وحید امیری در پرسپولیس برای همیشه به پایان رسید و او از جمع سرخپوشان جدا شد
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136305" target="_blank">📅 15:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136304">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
مذاکرات برای جذب محمدرضا اخباری وارد مراحل پایانی شده و باشگاه منتظر حضور این بازیکن در تهران برای عقد قرارداد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136304" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YezngvovoJZQxFa9B9XVmIPm7IPyyPfTFocB4r-39zGkNne4nGAztSGz6Z6G3o_XCNVQlAQlh2BIqZI0hhWYKEgHWsf65NFvegm5ZFTjrY2h5dp7N0n7Hwhe8Tuenu78W_OsxdWk4IpbUhVyejXgdpROpXn2TgNg2vHLFY-Yk8vbmfrycPRjSEq5h4b-lanIL5BlYEyqmeJT7ptzexwFlv3v21CD6vvV29grMCqAxxcuhiiiZdR3Tar2GTn5_iKBgmClEkyLMWQne6xjDgYj1qb_Z7FQ0GMqCDKSJSDmQR-Ko9E181Tf1CnsQNlpBOvIR-zrc6UNt0mv9eBnjvNqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شنیده ها:
پرسپولیس مقدمات لازم برای مذاکره با محبی رو شروع کرده و این مذاکرات در حال پیشرفته
🚨
جذب محبی نیاز به رضایتنامه باشگاه اماراتی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136302" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136301" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام در Melbet با وارد کردن کد هدیه giftcodeir بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136300" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136299" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136298" target="_blank">📅 13:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq3_IfxuTlg-oTVEbxEHg6sDqDDuUW4xUyIpGaFaqo5eVHDCDJ3NDclrbJIlnEwJoxZzsH6o59wbgKhUaENxytZUiwUVXhN6f-uQyxHSQqDQ-v8N-42WQTPkPd_OxeJQhx8E_VQDtEO8j64JDirNaXAEE7LA_p8SOoVAOvDkLxt-0SEG8ACuZ2kP_BA1gw9rrex5R37TvXzmPaBbPPWYR48jTHClkT62P9twhjxHpFdALOquBd72pXEtGWpj5eHrlJAUFrD85_kyjiOlC-a1i9KMmd5edTtjXsUFPhUJmprOC1qL9jZsFd_YCZn_ab0x3-2z6Mf5sSahsXi5Cln1Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
تارتار همچنان ولکن گل‌گهر نیست
✅
شایعات؛ باشگاه به دنبال امیر جعفری مدافع چپ گلگهر
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136297" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
پرسپولیس در یک دیدار تدارکاتی روز سه شنبه هفته جاری به مصاف تیم خیبر خرم آباد خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136296" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBlfRCxiTNLxquUNSzDvWxqqyq0x8QdTllEDFL1pX0Dbe5ehXFOYwVZEj9AIGeh4P-NHJodgQqY3nzFwk0hPaf2Amcg8T6TL1CDxIQ7j6Yt9bq3nZK4Lvq6TVfUwBLohdv0fqL_IGMQE26CkltjJS4HARofkYQS1tXSMwf4zVdT05IFfgXcvCM20LGBe3rmsmti62pjls-8c73e7Vosw053rJSkJDVh4noRxRAGiAx1ToT1kKY_qETwXt2CH0mm6EUvH00ycZw7luyqy5m04YiP684MkEFCpeLCukX32jiy-SxD4-pxki5-n3YlWEpYN3B6Tysx0_uQOWZDMn61cZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان از ایران با دو گل و یک پاس گل به عنوان سی‌ و هفتمین بازیکن برتر جام جهانی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136295" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
گویا دوره حضور تمرینی وحید امیری در تمرینات پرسپولیس به سر آمد.
🔴
احتمالا از فردا دیگر به تمرینات تیم نمی آید//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136294" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e01fd378.mp4?token=J2MJaZPUDNcqZPOhAc0AwbwV96ngiazetfXCBnZvhwXhaM8boeJrSDhHxv7KWXmxyYOpEUxODP5LHOHZGDxs7yktT5U-naw6nO45Cx0c8XMs-shg-mXNgG82wB53m_L3dz2AsNhA2CnsR1srL9HfQnUNFoXZLRtWscPNueSzRTuLdVQawPy68pSE6MH4QKVPsosNgorAXHlpYC9czPwR9JoQDQZKRn5Biv2DNrUGpeusp9NlmS27wfu8pHoHpYJLhqjo8uWpLefmVq38aS5ywjTlVWjzKhtKH6gVD2TEDZTUrh9enKCAEKxvcbVvvoS0PTZ3y0KXIHKdnZ2HXj7hhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e01fd378.mp4?token=J2MJaZPUDNcqZPOhAc0AwbwV96ngiazetfXCBnZvhwXhaM8boeJrSDhHxv7KWXmxyYOpEUxODP5LHOHZGDxs7yktT5U-naw6nO45Cx0c8XMs-shg-mXNgG82wB53m_L3dz2AsNhA2CnsR1srL9HfQnUNFoXZLRtWscPNueSzRTuLdVQawPy68pSE6MH4QKVPsosNgorAXHlpYC9czPwR9JoQDQZKRn5Biv2DNrUGpeusp9NlmS27wfu8pHoHpYJLhqjo8uWpLefmVq38aS5ywjTlVWjzKhtKH6gVD2TEDZTUrh9enKCAEKxvcbVvvoS0PTZ3y0KXIHKdnZ2HXj7hhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
بقایی: با مردم آرژانتین مشکلی نداریم ولی مردم جهان قلبا دوست داشتند که اسپانیا قهرمان شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136293" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
پرسپولیس دو پیشنهاد خارجی برای امیرحسین محمودی رو رد کرده و می‌خواد فعلاً نگهش داره. درخواست شماره ۱۰ هم با مخالفت تارتار روبه‌رو شده تا فشار کمتری روی این بازیکن جوون باشه.
🔴
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136292" target="_blank">📅 09:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgN_opHSR3FO64DSoL1BzU54xjXSuBeNqfqlfTdoAJ9nyGFQuzfzYmKg7WVWUZ4OFxEL49ohM61X-_TTs453J5c4pFQjPwejET3JS6jbJw3SqFOkUSZILmCVNRC89Vhkj2v4orRKbva7Cz9E-ukAl4ZPRPpzRhZfnp1znEtJs7usXV8ezwZw0dtdloXz9XMtqA1FE3Q1FH2g0DIoSF-KIv9eUTxq9BsX5FUdU-qN8LiVdL1mXlZft-W4QxctnN4ZNpQFO-5z09_ObM_q7x_uyWrOINyL1o_0FIo27jEHdsB6EIiKWsMCxxBtml0EkZ5FgJSN0zoUTnYVEUYSwbFlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
کیلیان ام‌باپه به اولین بازیکن تاریخ تبدیل شد که در یک فصل هر ۳ عنوان زیر را کسب می‌کند:
🔴
کفش طلای لالیگا
🔴
کفش طلای لیگ قهرمانان اروپا
🔴
کفش طلای جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136291" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK0AdCgXqkTWJ5XDIYDvC9flbDTIznXudQrD_TibJDZb5wB6xUXPcR3VI_NKOYG_wc30AgPJFtZ_EBx-C_wP-DbUkfh2FjYVwNqeWSPi2qkLhj3102qbVWeacDNCX1Al-xCJmovVCggetuKRtglstLgW1ygQxHFatYW1HNmmllkxqcnN7kEsIGbBVPngeTXmGBZtWLGhzdKMKinXEGkPr6fDTCzA4r_GF3sStq1nqrpwIGpMFY6C7sryBEqF4YS8tpWAWSeJOqrioNUo0WaZtpY-8J8RmwsyAN4CrqkjB0xEZF8DizyCV4A8-W9ZbPxQ4qGX2qru73Eru93Fxn45rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
چه قابی شد ...
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136290" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDV5t02LoArwWwjv_ZyRFSRWT1YeyNTbtvyoBhVeYVQfWrbh0L23y6p7y0POYDGO37xRyDqrFSuHsJNmgzWdc939MOn7mp-ijpRu6qdtA_xVPK0qkejbwHshKh9rqelxEJN5k14Wj05X25ovkBUaQdCYP50qtLX8Y8m3JN2Uq74-aTTAju9NpjakRkOYLXMpTW9gz67J8RUecdC9-DMo-c7kBIwT6_9joK7VdOTZtEp3BcsSqDdDIEQptMEdOnLe2P4L8vIhhYDerHcDJdksoyAGtgNeTbRBuGikfmGqQlJDHTnYJDTz5DRx0CYzk4Ys1lnF_S4Yl9JudOGSGhUgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دو زلزله به بزرگی و شدید ۵.۷ و ۵.۲ در کورزان کرمانشاه به فاصله ۵ دقیقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136289" target="_blank">📅 09:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
گویا حملات بسیار بسیار شدیدی دیشب به تبریز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136288" target="_blank">📅 09:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
فاکس نیوز: هروقت داور بازی سوت پایان بازی اسپانیا و ارژانتین رو به صدا در بیاره جنگ علیه ایران اغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136287" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
ورزش سه: محرم نویدکیا رسما خواهان جذب ابرقویی و کاظمیان شده در این بین گفته میشه احتمال معاوضه این دو بازیکن با آریا یوسفی در قبال مبلغی هم وجود داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136286" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136285" target="_blank">📅 09:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwW26xIO8EAQCmXR-kvk5RCqNlXxqPha6uFrn49QLnrB69tn6f_W1RHGN1jMPQRJeJvFJaf3MoZsBR4WCZJIzLpo4rB-0hSBfk1w4n7m7Th0U2y2IKCfnVc4CnZSyxCkr4RaSXtGon62kuuU1r6_cN01y_tncWL_OGc22dYwlVnBus6VVSnNjeWpcWnD_yfjzWvNRdt6oNImVAraFKUa5LJisIDeB8Zpa4ApR71vTHYhxG4owMznSnxO8nqe7ryJLBqxmnafEMlpKTm8Le_dE1qrArh9J06HyBYxmwb-beiN_8Y_MJu_4MmeChz6NiOXVzdrs-DJsSpCXEWxdUu4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136284" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136283" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136283" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYRYCqw5lCVgm2baQwOaGilvB9LQ9PrClI6c-sR-FkezU13ijU3y9FbDWTfqp6bFDrgdqXa9scaPVpI7ZrZZF6G_KhTtvJ38VAuoy5TZcCJKASa9WeqtL_eZALudomYEW0k8REaLKjG42bXzzBq_71USut3HgZObeiuC2aXQNL-Mt8IvVJuDFqkfBPskugaQpdjz-a2Iwbli4-RHNL4oSh5aOPTXJIjjLwjEJO9T8MNLlA5fkWf7dL9l0K1Bwgv5PrEvLPNJ8PLzklvsZSB6g3F-gGKHzprhXQ4mXAbtnJ5JwEjhByfSVHrmVMFWYIVpNRS6X4xKP4i-mDZ6pFlYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136282" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2yDV4ca_Exoj-ZzL3rvqUdXd2sMrD2TiYO9fPos2E8rkiUGmVr3dfvILA5l2sbLijDzfaSvDV5OBUe-Sb19VyQZ5gGL_bLy3q70a1HJtbnSPXpw3G2aBbPdpGXWN_mOxIXyvFJ3vmdhXGcOLOiQtzwDK4KNtKtaN2exi6D_xcykzhukYdtOJk1zemOig4-Oomn_vCpx35I-__JSUnAAlEow1hdZLBAScLHqlF-XHNdC_xqrc91JgmMSL8m2M2GSYNopLN21Twv5tdeTqBgIk-mbpKhlQSganZgQcrTAqjVsCOB6l-dpTPEBnwfNtzkcxQQ56xW6bTG7Rgqr3kzdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136281" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚽
فیروز کریمی: مسی الکی داره گریه می‌کنه چون دید رونالدو گریه کرد وایرال شد
👎
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136280" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX2JkERC9zhWQ5kTd02bMTnvtUMY-LT6RQm04cui40LhthmHg1OFaXh_Y4z_1RlQQtQa--r9yqT609lpLx6CTioedQ1kkACMaaAVHlukhD558JFSM3COvOfMGtqHqJdPq8FCeBT_l1hIOlChWCV8Eo6Tb46ULB9N32IdLwlkNLmxXo50PHJVexufdzc8ijjhnTwRnwMwMjC6ByFrMRI_LCkuVVk1zDBYLZ-SLCn2yEMnzErWJZPooL9KnKTfS10QxhE1R1l-jOwe00lSgT6fiBFrYKsEvSScpOB4TyyEqJMeGahIE5dXE7bIuJQJD9PhbV8_euQ0wexa8eHtgzBJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
سرخیو راموس با کاپ قهرمانی جهان اومد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/136279" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsygYg-XAOg-sOnr0FpCuWH0Ew-N0EMs0joiNJYjQubB4oaj1q5DRhOs59W8SzLLVyWwCr3Q22NIf2ZdJ5slJ5xOv91NSyqxUbGHmBKm1wCo3daMjDIjoGz_futAQ6kQQ-msduP2IfwDvxipLVuCvsGyClLgucOQEAhthKHcl-T_Mx8R6SKlulKV7vRXp_dGOmMm9R08rUJSo8emgYNwBBuBd4UFjlYc7J9JTJFBQmi3FrbZ8t50YKyxUlhdrJKNVq6AcA1c70fgzztGePfn8ZTVNCiYyQ2HA86rY2uwUrblCouQSQjxsPmUa2rtTTAUGGAXyl3Bw2eVCSSkFZxBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136278" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇪🇸
قول و قرارهای عجیب ستاره‌های اسپانیا برای قهرمانی!
🇪🇸
یامال : ریش و سبیل میذارم.
🇪🇸
گاوی : موهامو صورتی می‌کنم.
🇪🇸
پدری : موهامو بلوند میکنم‌.
🇪🇸
فران تورس : سرم رو از ته میزنم.
🇪🇸
کوکوریا : چهره لوئیس دلا فوئنته رو دستم خالکوبی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136277" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c877f07487.mp4?token=lpSfafiJK8Sw2zxFH-ZSArQLALkffNU-hk0bN3_Ssoh6Ppt2NGu36vvqtjeVhTuobZlxdU3qucHEldKRFuyNq37-NmlN7tpjsU8LqLd20L8uDa7MeRArVgT2tM2_XUFSQbbPkz69KRLstVwZbg0TAI49uBcXmczoItzylLmBZrcssmhU3NDAuAkFXj4vZetonYjMfZkAhQH8Es02nIvypxrNrXtN9Hse1SlWZLDTYcOMhmUX9Xqy6Rj3E80zHkpfSDMyPPjLP-uefXZxgsrPbx3oVrbEoQdW7JPi4CxB07NNAHqyZijQoxDa80J3BQCWwqKPT5-Wny0T57pbjGvLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c877f07487.mp4?token=lpSfafiJK8Sw2zxFH-ZSArQLALkffNU-hk0bN3_Ssoh6Ppt2NGu36vvqtjeVhTuobZlxdU3qucHEldKRFuyNq37-NmlN7tpjsU8LqLd20L8uDa7MeRArVgT2tM2_XUFSQbbPkz69KRLstVwZbg0TAI49uBcXmczoItzylLmBZrcssmhU3NDAuAkFXj4vZetonYjMfZkAhQH8Es02nIvypxrNrXtN9Hse1SlWZLDTYcOMhmUX9Xqy6Rj3E80zHkpfSDMyPPjLP-uefXZxgsrPbx3oVrbEoQdW7JPi4CxB07NNAHqyZijQoxDa80J3BQCWwqKPT5-Wny0T57pbjGvLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چخه سگگگگگ
🖕
🖕
🖕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136276" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚽️
اسپانیا با دلافوئنته:
🇪🇸
قهرمانی لیگ ملت های اروپا 2023
🇪🇸
قهرمانی یورو 2024
🇪🇸
نائب قهرمانی لیگ ملت های اروپا 2025
🇪🇸
قهرمانی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136275" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWDXLcjuvuPmLPQSaxPOonqD8rrCJrmND4ANfPLZA04U6gOkCYC2gqeF2bx-VuPY0i2zmoYNqyk1d9Z2v2ovaICAAxozD4f4Hx2qlBdq7VaiXETlybbZxHl7X25bUEXHR-ID6HahcCI-FoPf7uITid8zyR6-L_3mE2YnnsXGh43cyj0SWerqaJZqdym02prRa52gDZSOPOJGcXGOV3E6MI2znwQGUDkE9-nD_FxrzxhxvOqA45neUAfhUWVN7xpewQzzqJYRFuIpMonePhEUWfpQltxF8wtcsXAKGw60LCC2ChqGkvqZheGsiLkt_CJX8ueZu8EuOmAI5XEbLWepFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
عکسوووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136274" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSQGxyqpnpLwUerCChMez4NeyeNdm3LEPOjWFRYLiFPnHkY3ly24iNyNenWIP9bqbc7o8h2cbj8fuNXtBQJ5KIgeuDhoQ-3Y7wnkTwBWSiVlUdnyrC-dGSwhBxtbgjH8qGNRqSmdu9rDycMP8H7jPMoT19RUN36gZeMNyzolXwUPQHbfMYORj0rvTVIHU1dGQRDpbLRZBJLOpdVxzomBe0TvZ1u9Yhhyfg1wUaz0hPvJPApIfJ0lI0ABDCHQqr6TZbyM30jnpBq9MZRa_Sb9iZxN7sye1hBLYbG0zoPILjEvBquZh6DzpUdaZWESts64rxn2ejHnptWitz97ceaDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها:فوتبال برنده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136273" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxsjDuZxNWA8kYJxoVATnE9O2Ox2knrJxqcyo6ZzzBcSKXM_tB5wEBCmdP3WJaAHznihJxqNRZ0oGRB5hI3OtDx55FUIdrT0J3iJVqtiIeMO-MvZapgREU3scfYdxhw4GJR2KYP8DAgvtixspnw9rIfPI-GGiT4R44SjmztPRUe59PrgnyGfvA08e3W1OPvJP9m6wWPtunbGtr-ieVDVEVLnWwbF3CpTp99KYCXFzdIpHfc4qwgEC4NYvemb4k7VRDb3ZsjuB1I9eOclvmRNjtZ6dV9by9NiAuO2Qq24Y7XupWQTqn3uMxm73Efa82PiFD-uyb8pZqIvIYphcg3eWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپانیا با شایستگی تمام قهرمان جام جهانی 2026 شد‌
🇪🇸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136272" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
