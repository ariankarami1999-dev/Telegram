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
<img src="https://cdn4.telesco.pe/file/BUz83Gbf2giGZ2WgEGO9fvykYjJRThPoQAnnPQH3T7jziiE1G-ougLx4QW6KImlIdGI5v9Qr-hqwayYhvqQKxi04k0W1c7MQuo3G5RajXupGP7GAFk2ovQM9f8K860SflBWKtFpRihyvlJR10vlP_CrPcewZUWJ4ms5U8rswO8W2REgehQ2BMButVKlfPjFotgXmTnHv5gjU9-9yTeWuCqGrTfNp5A6DpP9MhRYfyk2QNzMNGEhBe4OYEtN5DTXWKtnTgcjqKatBucOLBkP1mrXi2Yhcf3bbHwSRPvVPzI2WVD9r6bKs1nkbhTNQlVBaX7W9_zeodfQdSHiSR1aCew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 448K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-22351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMett</strong></div>
<div class="tg-text">سلام یاشار
روزت بخیر
این صحبت درست نیست
خودروهای لوکس از منابع ارزی فردی که در حجم بالا ذخیره داره خارج میشه و معادل همون مقدار بابت ترخیص پرداخت میشه و از این طریق به جیب دولت کمک میکنه
اون دارایی اگر بابت پورشه ۹۱۱ نره قفل توی کشو هستش
واقع بینانه باید پذیرفت ج.ا. در راهبردهای نظامی و اقتصادی در شرایط فشار حداکثری موفق بوده و در مورد اجازه واردات خودرو لوکس هم تصمیم درستی گرفته</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/22351" target="_blank">📅 14:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو درباره غزه: بازسازی غزه فقط در صورتی امکان‌پذیره که ابتدا خلع سلاح انجام بشه. هنوز نمی‌تونم بگم چه نوع بازسازی‌ای انجام خواهد شد، چون در حال گفت‌وگو با دوستان آمریکایی‌مون درباره این موضوع هستیم. گاهی اوقات دیدگاه ما با آمریکا یکیه، اما گاهی هم اختلاف نظر داریم. وقتی اختلافی وجود داشته باشه، آمریکا منافع خودش رو مطرح می‌کنه و من هم از منافع اسرائیل دفاع می‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/withyashar/22350" target="_blank">📅 14:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d1a681e.mp4?token=uUPbXA9w3q2kCNHo4MwYz9C1xd3xFY_UGr1em1M7uQVAOSOl4WfRhKq_5cRwmpMufJJPkbtQP0nvoniQZLHd9LeP29OKO6FzQ8L_dfgCiHirHAJaBLOSGRC9BkzARJegTIYWwP_JlB-vq_W4-ZA83DOOrbaIkBjL8gYNCc-mIgXyR4ZMg8wiPpzbi14hvqWJPYSRPp7RZRrdD95qO9eNnKrJoepgKmLqaj7EuYHb22WuxYj3aeaVbviwjQxSyo3lor5ztAV9Uci2LOUYy7vb9eTX3Pyc--GpQoc7JajdIMr0EQSBUu6KGTpTBkFIu5ILEMBxjPifbN4RB53N5j-8qDEMUONYT-_yNlu_u4E8mP81J0tGO_iUw_6wvBrRQ_wkN-KqusohAJjJtPMYjDT19NACBo6QGu9OxaAHTk9vzFFI6IrzvcAHDCKs2UgwuVqCXqoHn1wcLuLes6XkQcxljYISfatasq3BScHLhbcSTrGo1XKk0BSXH1KBzLOzUpb2R7Aa_k_oCyZ4Muzk3e8-pwUirDsPEJPIqtkKyZpMyzQCchHsI1nSCHbIyoXfTANphSSBWnzmh4ToaVYZqdmtz30h3gT8D2x7JHBmcbo20e80ya_beY7SSKmQTuU2YVKk5PfkBey_G022RvH7GSrCkouKpaX0LKynu6fRFKiCUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d1a681e.mp4?token=uUPbXA9w3q2kCNHo4MwYz9C1xd3xFY_UGr1em1M7uQVAOSOl4WfRhKq_5cRwmpMufJJPkbtQP0nvoniQZLHd9LeP29OKO6FzQ8L_dfgCiHirHAJaBLOSGRC9BkzARJegTIYWwP_JlB-vq_W4-ZA83DOOrbaIkBjL8gYNCc-mIgXyR4ZMg8wiPpzbi14hvqWJPYSRPp7RZRrdD95qO9eNnKrJoepgKmLqaj7EuYHb22WuxYj3aeaVbviwjQxSyo3lor5ztAV9Uci2LOUYy7vb9eTX3Pyc--GpQoc7JajdIMr0EQSBUu6KGTpTBkFIu5ILEMBxjPifbN4RB53N5j-8qDEMUONYT-_yNlu_u4E8mP81J0tGO_iUw_6wvBrRQ_wkN-KqusohAJjJtPMYjDT19NACBo6QGu9OxaAHTk9vzFFI6IrzvcAHDCKs2UgwuVqCXqoHn1wcLuLes6XkQcxljYISfatasq3BScHLhbcSTrGo1XKk0BSXH1KBzLOzUpb2R7Aa_k_oCyZ4Muzk3e8-pwUirDsPEJPIqtkKyZpMyzQCchHsI1nSCHbIyoXfTANphSSBWnzmh4ToaVYZqdmtz30h3gT8D2x7JHBmcbo20e80ya_beY7SSKmQTuU2YVKk5PfkBey_G022RvH7GSrCkouKpaX0LKynu6fRFKiCUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هواپیمای نظامی آمریکایی در فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/withyashar/22349" target="_blank">📅 14:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9102f4bd1c.mp4?token=viuB2qyM_9ZUE4BpiyI3XP9I-XZH8evKUEISDZ1WqgnwMPcIQPpH2aRzzwk28UzLWAl63XB9cz4sO77NsNpD-qL92Psa7UVd90KpnOANOC40rSEAIwaqzKZ5MThxlVOOWCnL5HGW4p_UyAdjV1Is9l9kYpW2-8o-cmk5wzNKIXB2WS4PSoIpm-6aWL2XHOTGR_fcMDyioj27Oxa8f3sBtd8SMU2lv0O24zlkcS_wQE-uytPpgnqw-J9NBMJ9ZRm7qXgEbYEfHLUKMPGKZ4bU9SSaZJI8RysFjG4lxWZKZszU0YOhi_bLYtzi9Jia_bR-2EQB2jikes6oPe_6HfsqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9102f4bd1c.mp4?token=viuB2qyM_9ZUE4BpiyI3XP9I-XZH8evKUEISDZ1WqgnwMPcIQPpH2aRzzwk28UzLWAl63XB9cz4sO77NsNpD-qL92Psa7UVd90KpnOANOC40rSEAIwaqzKZ5MThxlVOOWCnL5HGW4p_UyAdjV1Is9l9kYpW2-8o-cmk5wzNKIXB2WS4PSoIpm-6aWL2XHOTGR_fcMDyioj27Oxa8f3sBtd8SMU2lv0O24zlkcS_wQE-uytPpgnqw-J9NBMJ9ZRm7qXgEbYEfHLUKMPGKZ4bU9SSaZJI8RysFjG4lxWZKZszU0YOhi_bLYtzi9Jia_bR-2EQB2jikes6oPe_6HfsqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
: اونا می‌تونن به ما حمله کنن و ما هم پاسخ می‌دیم.
متوجه شدید ایران داره به همه شلیک می‌کنه؟ به کی شلیک نمی‌کنه؟ فقط اسرائیل.
چرا؟ چون دقیقاً متوجه حرف من هستن؛ تا وقتی من نخست‌وزیرم، چنان ضربه‌ای بهشون وارد می‌شه که حتی نمی‌خوام جزئیاتش رو بگم. این ضربه از قبل آماده شده.
@WarRoom</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/withyashar/22348" target="_blank">📅 14:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی) دلار کف بازار :حدود ۲۳۰ هزار تومان! تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی) بیتکوین ۷۹،۶۴۶ $ انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت) نفت برنت  ۹۶،۲۸$(آخرین قیمت) @WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/22347" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405d38bbbf.mp4?token=e2U--iDM69Bi-mpIxpGs1utd2VAZZoNaUBoq2ucH2fzVM3cmQm297I6TllA4x61XlC_2JPzJpwF-WdDMCBcZj9ZB_SQpshyZJSYHh72Ebrhn5KmJsMkgFfbkbYsQPejoOTov3F0kensDgsNronwSf2ZNQYTHWazpL4nojw4EM2e5hfUJ6VfOp1hDqXUE2BbMUKojRm05IuLyY6xf8Udhq98ueFeoF-V_QmYn50K_973Eivh8oDY8tAsBZ-88E2z0rG6o-tR2p788cuZnYjlDqZZy7t_NwpwXpub0wDytJtRzGg0jeAppUgAFaen11Jh91UWmz8N_bPfGKUK-6huudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405d38bbbf.mp4?token=e2U--iDM69Bi-mpIxpGs1utd2VAZZoNaUBoq2ucH2fzVM3cmQm297I6TllA4x61XlC_2JPzJpwF-WdDMCBcZj9ZB_SQpshyZJSYHh72Ebrhn5KmJsMkgFfbkbYsQPejoOTov3F0kensDgsNronwSf2ZNQYTHWazpL4nojw4EM2e5hfUJ6VfOp1hDqXUE2BbMUKojRm05IuLyY6xf8Udhq98ueFeoF-V_QmYn50K_973Eivh8oDY8tAsBZ-88E2z0rG6o-tR2p788cuZnYjlDqZZy7t_NwpwXpub0wDytJtRzGg0jeAppUgAFaen11Jh91UWmz8N_bPfGKUK-6huudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکسیوس گزارش داده است که استیو ویتکوف و جرد کوشنر، فرستادگان دونالد ترامپ، این آخر هفته به مسکو و کی‌یف سفر می‌کنند تا تلاش‌های دیپلماتیک آمریکا برای پایان دادن به جنگ روسیه و اوکراین را از سر بگیرند. طبق گزارش آکسیوس، قرار است ویتکوف و کوشنر شنبه با ولادیمیر…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/22346" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وال‌‌استریت ژورنال:
محاصره دریایی آمریکا از تیرماه صادرات نفت ایران را تقریباً متوقف کرده و بستن تنگه هرمز از سوی ایران نیز ترامپ را به پذیرش شروط تهران وادار نکرده است. طبق این گزارش، رهبران ایران انتظار دارند وضعیت کنونی و فشارهای اقتصادی ناشی از آن حدود
پنج ماه دیگر
ادامه پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/22345" target="_blank">📅 13:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پارلمان پاکستان برای نخستین بار به عاصم منیر اختیار قانونی فرماندهی هر سه نیروی ارتش، نیروی دریایی و نیروی هوایی را اعطا کرد
دوره فرماندهی او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت
وی در مقام «فیلد مارشال»، مصونیت قانونی خود را تا پایان عمر حفظ می‌کند و برکناری او تنها با رأی دو سوم پارلمان امکان‌پذیر است
@WarRoom</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/22344" target="_blank">📅 13:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نرخ دلار ۲۲۵،۶۰۰ تومان(سقف تاریخی)
دلار کف بازار :حدود ۲۳۰ هزار تومان!
تتر ۲۲۴،۶۰۰ تومان (سقف تاریخی)
بیتکوین ۷۹،۶۴۶ $
انس جهانی طلا ۴،۴۲۷ $(آخرین قیمت)
نفت برنت  ۹۶،۲۸$(آخرین قیمت)
@WarRoom
🚨
🚨
🚨
🚨
۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/22343" target="_blank">📅 13:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر جنگ اسرائیل :
منتظریم ایران به تصرف تپه "علی الطاهر" واکنش نشون بده و حرکتی بزنه تا از غل و زنجیر و محدودیت‌های ایجاد شده توسط ترامپ آزاد بشیم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/22342" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صحبت های زیبای یک کاربر درباره پست قبلی
@WarRoom</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/22341" target="_blank">📅 13:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : سوی دیگر فشار اقتصادی ، نمایشگاه های کشور های خلیج فارس با کمبود خودرو هایی مواجع شدند که در لیست واردات ایران قرار‌ دارند و تا مواردی برای لکسوس ال اکس ۶۰۰ تا ۲۰،۰۰۰$ قیمت این خودرو در بازار افزایش یافته ، بعد از صحبتم با یک نمایشگاه دار قدیمی ، وی گفت جنگ فشار بالای به ما وارد کرد ولی در ۳۰ روز گذشته ۲۰۰ خودرو فروخته ام و در تعجبم از این بازار تمام خودرو هایم که به ایران میرفت فروخته شده ، چند روز پیش خودرو جی۶۳ و پورشه ۹۱۱ هم به لیست واردات اضافه شدند ! پیغام واتس اپش را که نشان داد شخصی در حال مذاکره برای خودرو جی کلاس ۶ چرخ (6x6) بسیار لیمتد بود از وی ! و پرسید چطور پس میگویند کسی پول ندارد ؟! دلار در این لحظه ۲۲۵،۰۰۰ تومان است !
@WarRoom</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/22340" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81fbb27ca2.mp4?token=UX5-c4ZHQHVv_WobHvnZCRoz1KyAXefD8n6ay82GTI_WwfeORIzxnklLdmJSx1VkDHXqLorx3Ap59DH9NmLif9MIH729AcaBAcR8eYFff_SvYaAu7d8tDlr2eKw2SnYGa_knPe21UXuLWJCBOo6fqpIswgJ763PGYvk7SrK5XNdA5zCD3Ptr8FdQc6Om7o19YrYLWQlg2H1IyV0FrH8EvXk77Si1xaT_fe7o_H9IuqpJloylMoeRvbAyZMImDj1K5NVGAHapTKTTTDns7faDsl0KKDgRcaCu1F_oS8KExwAEcD3e4ziYKpHpmyTd3eK8gRsMM-LHamZ_qxpEc6Whug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81fbb27ca2.mp4?token=UX5-c4ZHQHVv_WobHvnZCRoz1KyAXefD8n6ay82GTI_WwfeORIzxnklLdmJSx1VkDHXqLorx3Ap59DH9NmLif9MIH729AcaBAcR8eYFff_SvYaAu7d8tDlr2eKw2SnYGa_knPe21UXuLWJCBOo6fqpIswgJ763PGYvk7SrK5XNdA5zCD3Ptr8FdQc6Om7o19YrYLWQlg2H1IyV0FrH8EvXk77Si1xaT_fe7o_H9IuqpJloylMoeRvbAyZMImDj1K5NVGAHapTKTTTDns7faDsl0KKDgRcaCu1F_oS8KExwAEcD3e4ziYKpHpmyTd3eK8gRsMM-LHamZ_qxpEc6Whug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از نفتکش هدف قرارگرفته توسط آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/22339" target="_blank">📅 12:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت بنابر گزارش منابع محلی به خبرگزاری دانشجو، یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22338" target="_blank">📅 10:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1lIUWnF2AaxCsTg5c7vCqxKBiqbTwlUt3jpvdSwjC9hlwGVv-wIFcLYPbyInIJ2Px5Q2zafgIzI0YyGwsaZYvdRwAmPI8om0xBIEBFesLW5bCJRmUtnnGaYCx_Cs86qpm-8oYXqfwhITk2IcbTn7K1ifU81o6E0_pn1QLDjjNcpf9mCYaGcQp_z6PutTRKRlI3wDwFv5U5WwWI66UMO5d2pcHO0fSM9meWqNIRaZ3y3JO8YuM-zgJOAdFogZAchGzk0_mpKD5DkIQE56Ef4xI7660CW3jwJ5noSlU8M_8rZ67eAAVJ8YB_g_yxq4iPJrF2nYzv3igdm3csFxTR5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای روسیه احتمالا دارد نیرو های روس را از عسلویه بوشهر خارج میکند
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22337" target="_blank">📅 10:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsaTUNZ🛸</strong></div>
<div class="tg-text">یاشار ی انفجار جدید شنیده شد
🚨
(جزیره خارک)</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22336" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAb Mh</strong></div>
<div class="tg-text">یاشار دوباره هم صدای انفجار اومد ۲ تا بود ایندفعه صداش خیلی شدید تر بود</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22335" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhcP32ZpKT4wMScrD9EPlACz3BW_MveI_ucazIOUskOwrsGaeHyQpq7bFwx_xjqDATIVzW2FC_Gz2V1Q7xVw9wu0mexfcE5RqFaoqQlTxzJs1cYX_D1oVE3ngvqwf4OwcXneKekDEXdZssV63oNk_PIK1tR5O0YNtveqDiIXZQAgx1Rbm7vryr1IqJBXPrBL-jEdIWf-zehQ-MlAC8y-zcr_HVNh9nc1L2nfdFUNxjDZvoj5Z9llwcdwfzr4-gJiQgOCjUb0VIu03UmrpGmgLUJUVK30PF4jUhHwLQSv46aEjf-ibIXly52SUCnwECNBGIFo25w4qpD8rdGnv0KXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش انفجار ،  پایگاه نظامی حیدر کرار در محدوده شهرستان دماوند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22334" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">یاشار سلام داشتم می‌رفتم دلی جان یه دفعه پشتم ترکید فکر کردم لاستیکمه پشتمو نگاه کردم دیدم دود بلند شده از لای کوه می‌دونم چی اونجا بود زدنش</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22333" target="_blank">📅 10:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c67d702f0.mp4?token=eD3unJv2EwR-YoiRWMWBFbyfSdx3-_6HVQHDssSBuXcgbJzYBBJbCDbL-v9hUg5ERC3KgfTRzFpeWx8BSPsJBZK2UsisBQvbFWjFrOJ22OORSMF99REsw5RDF-e5No9Rc6d2MWVfKLoO2Mh3w0hkjMN9ZYu4TOXkWlemuoV9dCApZw8ExwNjOwS4ecmK-VjtFNsxbbawP-Y0ltxlCgq6nbmpM1Tj0C-o93xBaClUBu7rm1Py9vt4HD2P9uXvTqcLSNj2_rQnlpy7LeFR0MNlnPwqzh5RqTP-aVlmvQT4RU6vHGvvPMaGX0FwcyGqvjteIekfusJDbBButjzLQP0Y2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c67d702f0.mp4?token=eD3unJv2EwR-YoiRWMWBFbyfSdx3-_6HVQHDssSBuXcgbJzYBBJbCDbL-v9hUg5ERC3KgfTRzFpeWx8BSPsJBZK2UsisBQvbFWjFrOJ22OORSMF99REsw5RDF-e5No9Rc6d2MWVfKLoO2Mh3w0hkjMN9ZYu4TOXkWlemuoV9dCApZw8ExwNjOwS4ecmK-VjtFNsxbbawP-Y0ltxlCgq6nbmpM1Tj0C-o93xBaClUBu7rm1Py9vt4HD2P9uXvTqcLSNj2_rQnlpy7LeFR0MNlnPwqzh5RqTP-aVlmvQT4RU6vHGvvPMaGX0FwcyGqvjteIekfusJDbBButjzLQP0Y2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : خوب مشخص نیست دوره ولی شناورا دارن آب میریزن روش
صدای ۳ انفجار جدید
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22332" target="_blank">📅 10:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش صدای انفجار جدید جزیره خارگ
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22331" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">طبق گزارش منابع محلی به صدا و سیما رژیم:
نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
بر اساس این گزارش، این حادثه تلفات جانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/22330" target="_blank">📅 10:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌋</strong></div>
<div class="tg-text">نیم ساعت پیش فکر کردیم بوشهرو زدن خارگ ۴۵ کیلومتر فاصله داره صدای سه انفجارش تا اینجا رسید</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/22329" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfIGzHJ5q9XMrGHeHeZEiN7nn8WXuL7z0Ymov7i_HsSfDU79jk5Ta5wnhZ_T4VSh8D3uxdwR7zN40-w8MJkO8BjVNUnPXfBjQ4kIjn53ouNcQd6dOBMH6H3adurrbto81G1BkDu846suspR0rVvkl7taOihBcmovsb7o7Es81Kbdm71TJP7kyr5NFuKzElR9h8g5pX4CmhnBORdk4FjliA-A0NqfTY8eXab1dt14U4Wb5hhwffwkMLuph21nMaYDZVHc3o_kp2uq0CGJp2MUQsziacnhso9HPreOlWAheG9co9OiUvKTR7eW9FouA3_3S4DElPtcm_PQbTCoiAoVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه صفه اصفهان
💨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22328" target="_blank">📅 10:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۵ صدای انفجار جزیره خارگ
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/22327" target="_blank">📅 10:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSXs0dR1Z-y52zfTr9Wg401eW747x9krWfReD2oK5LIR3RoOwSHTGqdJwLSMJMOkbJh6dO2ozSGak0TnG7CqmQcjSkKh4mE-jokIZfGlPOsZpCVvclv0v0qeXt3ivCoNgQ9A7QiiElZWhHPZX7OGbIJ0LHQ5_wFdedNLKPd8wuu4_aIcqAaX1wjO4BF5x9SWBVnH7b3Ka9wtzdjJdKjUO8WIsznNq3t6JqqLooFBfqYOtiJ-InxCblzMEfrAwjn-Jn9ZPG20aatRohXigJEijfAy1l8ZF_NxcFsJFXN3Um6swoMCoKjH9xwmrAtfpzcgOKBkIzJM3RTOqjd4mFLOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار کوه صفه ، اصفهان
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22326" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/22325" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت
بنابر گزارش منابع محلی به خبرگزاری دانشجو، یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/22324" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKSHmzDQWKtMFc9YCjJQZK9-I0w1yUhFrCE4Qo9rQzfZnI01HjQQrnEdZ79Y3n0VRgo3VbTGNwc95_Lsh3r56VjREJk5higHVzW0O09U3r2S-rGvURA6RK5TOR-awss3oI_jeZZj4NzSoZupvswMD87EBdx9-cujP1ZXYGfxIcDNQ13g-FgDOD2ckpgUB1STC66kMYYM3vvsOWA_t0LGdvh4GScQDUaMXrdJ0j-Qx4VJNJ9VGra7dHOcRN9ad3YH1JxuRdWTr-xKCK_itC7BHDQwQHYL3TEbk5aAJbotw6nvcKGFRD-R2aDJfnbB_peSpBk0uRsGXZ0V-Oazi03gpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اسباب بازیهای بجا مانده از کودکان بیگناه علی الطاهر!
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22323" target="_blank">📅 09:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیویورک‌تایمز: ایران فعلاً حاضر به پذیرش شروط آمریکا نیست
طبق یک ارزیابی جدید اطلاعاتی آمریکا، ایران بعد از ماه‌ها درگیری نسبت به توانایی خودش برای حمله به پایگاه‌های آمریکا در منطقه اعتماد بیشتری پیدا کرده و فعلاً فشار واشنگتن رو برای توافق کافی نمی‌بینه.
برآورد آمریکا اینه که ایران احتمالاً تا انتخابات میان‌دوره‌ای نوامبر حاضر به پذیرش شروط واشنگتن نمیشه و ممکنه درگیری رو چند ماه دیگه هم ادامه بده.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22322" target="_blank">📅 09:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش های  زیاد : جنگنده ها از مهر اباد بلند شدن
سلام صبح بخیر الان جنگده از بالاسرمون رد شد تو جاده آزادگان فتح هستم تهران
سلام داداش
همین الان شهریار جنگنده از بالاسرمون رد شد
هنوزم صداش هست تو آسمون
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22321" target="_blank">📅 09:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیویورک‌پست
:
ذخایر سوخت ایران، تحت تأثیر تحریم‌های شدید و محاصره اقتصادی آمریکا، ممکن است تنها برای حدود
دو ماه دیگر
پاسخگوی نیاز داخلی کشور باشد. بر اساس این گزارش، کاهش شدید واردات و دشوار شدن تأمین سوخت از خارج، ایران را با سه گزینه روبه‌رو می‌کند:
۱.سهمیه‌بندی شدید بنزین، ۲.افزایش قیمت بنزین یا ۳.ایجاد بازار چندنرخی سوخت
.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22320" target="_blank">📅 09:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در ارزان‌ترین حالت محاسبه لیست ساده ترین لوازم‌التحریر «کلاس اول» نشان می‌دهد امسال یک خانواده ایرانی برای تهیه حداقل وسایل موردنیاز دانش‌آموز خود باید دست‌کم ۱.۴ میلیون تومان هزینه کند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22319" target="_blank">📅 08:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏خبرگزاری سعودی الحدث : نیروی دریایی یمن دو قایق حوثی‌ها را که قصد داشتند الفجره و بندر المخا را هدف قرار دهند، منهدم کردند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22318" target="_blank">📅 08:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏علی مجتبی روزبهانی، سفیر جمهوری اسلامی در ترکمنستان: تهران و عشق‌آباد درباره چارچوب حقوقی دریای خزر در حال رایزنی هستند و مشورت‌های دوجانبه مسئولان و نهادهای دولتی مرتبط ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22317" target="_blank">📅 08:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیویورک‌تایمز:
مقام‌های آمریکایی می‌گویند حدود
۵۰ نفر از اعضای ستاد مشترک ارتش آمریکا
در چارچوب تحقیقات درباره افشای اطلاعات محرمانه مربوط به جنگ ایران، تحت آزمایش دروغ‌سنج قرار گرفته‌اند. محور تحقیقات، شناسایی عاملان افشای اطلاعات درباره
کاهش ذخایر مهمات حیاتی آمریکا، از جمله موشک‌های دوربرد و موشک‌های رهگیر پاتریوت
است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22316" target="_blank">📅 08:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی ضعیف‌تر از همیشه است و سقوط آن در دسترس قرار دارد؛ این حکومت برای بقای خود می‌جنگد
@WaRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22315" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrnvjG0F8mQbTS4Yn3staU43HvYcHsUm-wYwdWJoU68BIdmgy0uyHB206v7A7Q-JirJHClrG50RkqKTtIghxO40BCKjsTSgah2lwu5TEDryuJXYIoJ2I_IXk1TzkY7lXdIKD5DjNz5sKC7kLnxFdf0OdQOJ4gRy0fCJpetuWgSHIuSkreC8yBSGdhK_ooBapPSyRbclgnSDv6YaBCHEnYevkWMtxL5C9TGKLsCVHPAkGrkIk7ipbZVVFk5PUn_146w9pX7QqLCQrCLVV1j99V_Cctg7sYRA9RqDlQCi96PjqkEF56vg0NIk6bPYLg1joiWcd01Ou5QvHA6kAiZhUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی حامل گاز مایع "ال غشامیه" متعلق به قطر، مسیر خود را از "راس لفان" در قطر به "الفجیره" در امارات متحده عربی تغییر داد، پس از آنکه این کشتی یک مانور چرخش ناگهانی و غیرقابل توضیحی را در مسیر جنوبی انجام داد، مسیری که توسط ایالات متحده پشتیبانی می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22314" target="_blank">📅 23:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هم اکنون ۵ پرتاب از سیریک
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22313" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22312" target="_blank">📅 23:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c89a571e.mp4?token=muGhw_MTPbLZCCsdBInQsB-ppADjuK34gcY9s-wHrtnc0KCM-QW-HLrY4-OF2m6x8Q9CxKkdeYFiY_5V7ec8fiTOEs11Q8YiKTRWmJnMbQ3vWkbids1w7dVsOrl0HSELhSaQ6x_OGuHcJg2Pd1BvabfsGpX1zwmTEfpgd9aLXDoqP08SldGgoUwFocTw7pwNZV0AqHd05hiJzKtK_rcnFjgp3-6THALwW2pJf4GNiJywwuqowksjwZMDHsUXO7WmtR1jymBzHFrLD-koiJD_CfZcmgeuA5n6y98dsDcgTu_h5Ke1qohG-wuVM6MZOuTt--PD5e_JWRUP-liVOY3iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c89a571e.mp4?token=muGhw_MTPbLZCCsdBInQsB-ppADjuK34gcY9s-wHrtnc0KCM-QW-HLrY4-OF2m6x8Q9CxKkdeYFiY_5V7ec8fiTOEs11Q8YiKTRWmJnMbQ3vWkbids1w7dVsOrl0HSELhSaQ6x_OGuHcJg2Pd1BvabfsGpX1zwmTEfpgd9aLXDoqP08SldGgoUwFocTw7pwNZV0AqHd05hiJzKtK_rcnFjgp3-6THALwW2pJf4GNiJywwuqowksjwZMDHsUXO7WmtR1jymBzHFrLD-koiJD_CfZcmgeuA5n6y98dsDcgTu_h5Ke1qohG-wuVM6MZOuTt--PD5e_JWRUP-liVOY3iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: مردم آمریکا چه زمانی باید منتظر یک راه‌حل درباره ایران باشند؟
ترامپ: انقلاب؟
خبرنگار: راه‌حل.
ترامپ: تفاوت بزرگی است. فکر کردم «انقلاب» جالب‌تر بود.
نکته: در انگلیسی، واژه‌های
Revolution
به معنی «انقلاب» و
Resolution
به معنی «راه‌حل» یا «حل‌وفصل» از نظر تلفظ و شکل نوشتاری بسیار شبیه هستند و ترامپ با همین شباهت، به عمد سیگنالی گفت انقلاب.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22311" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دونالد ترامپ درباره ایران : به شی جین‌پینگ گفتم لطفاً در موضوع ایران دخالت نکنید. چین واقعاً درگیر این موضوع نیست و دخالت بسیار کمی دارد؛ در حالی که می‌توانست نقش و دخالت بسیار بیشتری داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22310" target="_blank">📅 22:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ درباره تنگه هرمز: همین حالا خطوط لوله در حال ساخت هستند. مسیر زمینی از طریق سوریه هم در حال ساخت است؛ در واقع، این مسیر باز است. مردم با کامیون‌های بزرگ، کامیون‌های عظیم حامل نفت، از طریق سوریه عبور می‌کنند. مسیرهای جایگزین زیادی برای تنگه هرمز در حال ایجاد است. تنگه هرمز دیگر مانند گذشته نیست
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22309" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم. اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22308" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795f134b33.mp4?token=FiRZ-WWMw5noOo0S-O0vIbKDl20x0Pdc6A1P6Yz9z6sjNIrPWRJm-lPuiLtfcEyLCzKAEeGkLmX2mQKJwx55uuODqHeitaKRJ2uXdMUqyY2LxD4024lc-VM-vsOBomShn4Ed4G9u3fZrPiZo3mzT8xQd9IE8uQJzRZ907fZbdNumWXmEzVM6okv1HSJM_MT1iVvP9gvqcQhV6jeNUrytrrvrbFAJNJk4K1HZN9FiLIeQ2zLIey_1NiSdL9NSts_3FR377ksNIdj3q5KPoiMdBduQxDcYNcUh4TxBaQxl19saA-XW_CS9cAAsGm1YBHGuyP7Im8iDSrOGZfsu86bACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795f134b33.mp4?token=FiRZ-WWMw5noOo0S-O0vIbKDl20x0Pdc6A1P6Yz9z6sjNIrPWRJm-lPuiLtfcEyLCzKAEeGkLmX2mQKJwx55uuODqHeitaKRJ2uXdMUqyY2LxD4024lc-VM-vsOBomShn4Ed4G9u3fZrPiZo3mzT8xQd9IE8uQJzRZ907fZbdNumWXmEzVM6okv1HSJM_MT1iVvP9gvqcQhV6jeNUrytrrvrbFAJNJk4K1HZN9FiLIeQ2zLIey_1NiSdL9NSts_3FR377ksNIdj3q5KPoiMdBduQxDcYNcUh4TxBaQxl19saA-XW_CS9cAAsGm1YBHGuyP7Im8iDSrOGZfsu86bACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: ۱۸ نفر در جنگ با ایران جان خود را از دست داده‌اند. ما شاهد حضور نیروهای نظامی برای مدت زمان بی‌سابقه‌ای بوده‌ایم.
ترامپ: بی سابقه؟ مگه نمیدونی ما چه مدت در ویتنام حضور داشتیم؟
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22307" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a52585ca0.mp4?token=URqkG-yJbN2eOPS0whYxkkgFJDtTHKz3A_SMe29t872C5VKsV9YTPFGeZCAJcGTxYI_6Tw6xhY9d2M07JX24RJMbeDupID6QYK2PDWdsJDommCcO9K7X33ym0dBtlJnCPXjB8120NCqznkGTdBnZ3YQd4SkG79dn0_Ro5sCNe-NXhqOhUnAAXjUuuSVJqPkaYudG7HpxsEAYMVjHzXeL9RARtWTd_vMvg7BdwlbAwH95CPbWs3p2aQ1R7M2oXsD6-AXkR9zvVvsswHsjQhVjmiRvIVRoE7KtiPpCeKXPvxfeD70yPGM8EZgS4Y5BaJPEMa1BUVmxyz5VpOn0ia6WKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a52585ca0.mp4?token=URqkG-yJbN2eOPS0whYxkkgFJDtTHKz3A_SMe29t872C5VKsV9YTPFGeZCAJcGTxYI_6Tw6xhY9d2M07JX24RJMbeDupID6QYK2PDWdsJDommCcO9K7X33ym0dBtlJnCPXjB8120NCqznkGTdBnZ3YQd4SkG79dn0_Ro5sCNe-NXhqOhUnAAXjUuuSVJqPkaYudG7HpxsEAYMVjHzXeL9RARtWTd_vMvg7BdwlbAwH95CPbWs3p2aQ1R7M2oXsD6-AXkR9zvVvsswHsjQhVjmiRvIVRoE7KtiPpCeKXPvxfeD70yPGM8EZgS4Y5BaJPEMa1BUVmxyz5VpOn0ia6WKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ممکن است خیلی زود به کوه کلنگ ضربه بزنیم اگر
اتفاقی در حال رخ دادن باشد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22306" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233e0dbdb1.mp4?token=MoxbIGJqIXhnAQRtH-xrn5q2pQ2pLmnLHqOnNzJTZcoiqQutQzPPhQUm3soHd8ElguL4jg6wxj1JKO4L3dtbbSx1fjHkFpfNCu9-uCimBeQCvHHvWBwwkgXBfLrJfo9XMgNgefCY3TkS32GybI2eqIjS359n4XOU7F1Lsg3ZvpidLUzAp2P_7qI81Dz-7hbKX7valpiOMEybONu2wR6GhYbiO_yFdlLfctLJcryZRAwJyut5DSIVXO4O39IeQUu3JOR61TdrIJJry-jbXtpRq1IyiuTdAvW7Xf5Y2EHJzuKb-cuPvZAR4_0orki8X_eDXgM_YsNzIFXS_BLsDYOnCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233e0dbdb1.mp4?token=MoxbIGJqIXhnAQRtH-xrn5q2pQ2pLmnLHqOnNzJTZcoiqQutQzPPhQUm3soHd8ElguL4jg6wxj1JKO4L3dtbbSx1fjHkFpfNCu9-uCimBeQCvHHvWBwwkgXBfLrJfo9XMgNgefCY3TkS32GybI2eqIjS359n4XOU7F1Lsg3ZvpidLUzAp2P_7qI81Dz-7hbKX7valpiOMEybONu2wR6GhYbiO_yFdlLfctLJcryZRAwJyut5DSIVXO4O39IeQUu3JOR61TdrIJJry-jbXtpRq1IyiuTdAvW7Xf5Y2EHJzuKb-cuPvZAR4_0orki8X_eDXgM_YsNzIFXS_BLsDYOnCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22305" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس:
دولت ترامپ در حال تدوین یک راهبرد پساجنگ برای خاورمیانه است که هدف آن
مهار ایران، ایجاد ثبات در منطقه و گسترش روابط میان اسرائیل و کشورهای عربی
است. بر اساس این طرح که هنوز در مراحل اولیه قرار دارد، ایجاد یک
ائتلاف منطقه‌ای با حمایت آمریکا
، توافق‌هایی درباره
غزه و روابط اسرائیل با سوریه و لبنان
و همچنین
عادی‌سازی روابط عربستان و اسرائیل
می‌تواند در دستور کار قرار گیرد. آکسیوس می‌گوید تدوین این راهبرد احتمالاً
چند هفته دیگر
زمان می‌برد و هنوز جزئیات آن نهایی نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22304" target="_blank">📅 21:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شبکه NBC:سربازان آمریکایی پس از درگیری با ایران، دوره استراحت خود را در یک تفرجگاه گردشگری در تایلند سپری می‌کنند؛ در حالی که فضای متشنج ناشی از جنگ با ایران همچنان حاکم است. این صحنه، تضاد میان فضای تفریحی تفرجگاه‌ها و وضعیت آماده‌باشی را که ارتش آمریکا به دلیل جنگ در آن قرار دارد، به تصویر می‌کشد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22303" target="_blank">📅 21:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قرارگاه خاتم الانبیا : حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22302" target="_blank">📅 21:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقام امریکایی به نیویورک‌تایمز: ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد ایران ممکن است به‌جای مذاکره به دنبال طولانی‌کردن جنگ تا انتخابات میان‌دوره‌ای آمریکا باشد
تهران درک روشن‌تری از توانمندی‌های نظامی خود پیدا کرده و ممکن است در حال بررسی یک تشدید قابل‌توجه تنش باشد ، ممکن است بار دیگر به سطح تنش‌ها در ماه ژوئیه بازگردیم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22301" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال ۱۲ اسراییل : امشب جمهوری اسلامی شروع کننده جنگ بود و به پایگاه امریکا در اردن موشک شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22300" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۲ اسرائیل و باراک راوید : مقام آمریکایی می‌گوید:
«تا این لحظه، ما از هیچ حمله‌ای به پایگاه‌های آمریکا در اردن اطلاع نداریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22299" target="_blank">📅 20:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش‌ شنیده شدن صدای‌ انفجار در اردن
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22298" target="_blank">📅 20:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHdjoFYRAP4zJua4P9eJRrmTqjSuqKtp4tUxtJYDi4XYaCZG7d8NiE-_viGuiRjnuNtRi5pl8uoim0evzkEtL2Nw1csQt1kollb4Y-mSP98CiSPSDa5IkybhXdGrvkqB2-iPmp7x7Eibuze2N-R7que3QKQPTWKtaZ3ZBLQRZWaISAYhqGzdRjmD9_CZj9gOVtZG2qFNeJVI4QauyKPGHmdYN7WHafMSX0qLT4d6Z9bhQl6IoObjsdNGRSf1TJELWsqsOW9Icndlm9hpRoMiuikehdGYP1oVgwu13HOP5iSlGHz_7S5g7Jbr6iBamNpc7-hNsPbAMP6OJBfEZHG-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: دیوانگان چپ افراطی، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ این جنگ را برای آمریکا پیروز شود. به عبارت دیگر، آنها ترجیح می‌دهند ما ببازیم تا اینکه پیروز شویم! این افراد بسیار بیمارند و از نوعی اختلال شدید به نام «سندروم جنون ترامپ» یا TDS رنج می‌برند؛ اصطلاحی که گاهی برای «سندروم جنون ترامپ» به کار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22297" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیروی هوایی آمریکا پس از از دست دادن دست‌کم
۴۵ پهپاد ام‌کیو-۹ ریپر
در عملیات علیه ایران، برنامه جایگزینی آنها را سرعت بخشیده است. آمریکا می‌خواهد پهپاد جدیدی ارزان‌تر و قابل‌جایگزینی‌تر بسازد که هزینه هر فروند حدود
۱۰ میلیون دلار
باشد و در نهایت دست‌کم
۱۸۰ فروند
از آن خریداری شود. نمونه اولیه قرار است ظرف یک سال و استقرار گسترده آن طی سه سال انجام شود؛ این پهپاد با کاهش برخی توانمندی‌های ریپر، بر
برد زیاد، هزینه پایین، طراحی ماژولار و جایگزینی سریع نابودی در جنگی
تمرکز خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22296" target="_blank">📅 19:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شلیک ‌موشک از اصفهان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22295" target="_blank">📅 19:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82539ca3a.mp4?token=F65Zkw1H_dzYNJmi7SYrYhDSRhLfsn8cAmPcE0U5gECzzSB7vXPeU57VuyocNI5XYr0zuKhsRctH7EBVnp1KIKeMPgWFn3QJ51qlviqCVPreLuU_LP4NHMG7vO7DYN0_osaPATtXW5Z6k9yX1i5vF5U1oJumhSrqqpHt-tLYnrHFnxu6KM_AT5uM42fMe5ydT78K7evc6ObrETLLmf3Rtmf6C9QRiDsVChjyJunxjdr-oL0rzmrUUctHOQeJ9Ft-Wgru0qXPhVxbfNXX5KtOWstbQNHKtdL3TwfBBm-ttdWRy57qgwwV29LbdYV9KpjVt22kHuW0NHHx2ByAQndZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82539ca3a.mp4?token=F65Zkw1H_dzYNJmi7SYrYhDSRhLfsn8cAmPcE0U5gECzzSB7vXPeU57VuyocNI5XYr0zuKhsRctH7EBVnp1KIKeMPgWFn3QJ51qlviqCVPreLuU_LP4NHMG7vO7DYN0_osaPATtXW5Z6k9yX1i5vF5U1oJumhSrqqpHt-tLYnrHFnxu6KM_AT5uM42fMe5ydT78K7evc6ObrETLLmf3Rtmf6C9QRiDsVChjyJunxjdr-oL0rzmrUUctHOQeJ9Ft-Wgru0qXPhVxbfNXX5KtOWstbQNHKtdL3TwfBBm-ttdWRy57qgwwV29LbdYV9KpjVt22kHuW0NHHx2ByAQndZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خرانه داری ، بسنت : نفت به ۴۰ دلار سقوط میکند!
در واقع فکر می‌کنم بعد از این، در بازار نفت با مازاد عرضه زیادی روبرو خواهیم شد. احتمالاً قیمت نفت خام را در محدوده ۴۰ تا ۵۰ دلار خواهیم دید.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22294" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991db756b7.mp4?token=MgkboSHvYbO0rDqqCgGLVUBoh5gSrzxc1yuj_jl1hjqTcuKSLzqCo7e2hr7TR8MGmedf_W2TokEM2s0t8JGGrCqfYc8AwTZlvqmlPhHn3h5-6lCCtOpwcGm1kLY7prD3NBaGhpLsXpzgc1JtCJdNPUljKxUIeaCQq9sF3xzjS9VVEJfWUitM8D5UfVFcWFuKnTUGfUFxVgPE_eC1u2PCLRTljpvWFlN8ZEB0oe9psSxY6izCsTjNCG-BOmf--t86pCw1ZHLax5YB6RqlDS5WywoCP2XYlZFYP3YrbtlOhItDyreHTAnjQlh24Q5uVAXvfbwZjrtafRMXWm24LTbpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991db756b7.mp4?token=MgkboSHvYbO0rDqqCgGLVUBoh5gSrzxc1yuj_jl1hjqTcuKSLzqCo7e2hr7TR8MGmedf_W2TokEM2s0t8JGGrCqfYc8AwTZlvqmlPhHn3h5-6lCCtOpwcGm1kLY7prD3NBaGhpLsXpzgc1JtCJdNPUljKxUIeaCQq9sF3xzjS9VVEJfWUitM8D5UfVFcWFuKnTUGfUFxVgPE_eC1u2PCLRTljpvWFlN8ZEB0oe9psSxY6izCsTjNCG-BOmf--t86pCw1ZHLax5YB6RqlDS5WywoCP2XYlZFYP3YrbtlOhItDyreHTAnjQlh24Q5uVAXvfbwZjrtafRMXWm24LTbpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بِسنت، درباره جمهوري اسلامي ایران:
ما یک بانک دیگر مرتبط با رژیم ایران را تحریم کرده‌ایم. هفته گذشته، یک بانک مصری با پنج شعبه در دبی را تحریم کردیم که ۱.۸ میلیارد دلار به رژیم داده بود.
ما امروز یک بانک دیگر را تحریم خواهیم کرد و احتمالاً هفته آینده نیز یک بانک دیگر را تحریم خواهیم کرد.
ما به سیستم مالی می‌گوییم: بازیگران بد، ما می‌دانیم شما کیستید. شما می‌دانید که کیستید. تمام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22293" target="_blank">📅 19:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efae7c8d8f.mp4?token=rQDr856EcgYK86j7pwDjj6-LhvjwdWuKofVwQATXzcdDmsVtVSpN7pfbiD2AwNkPEA_CI4qJOblgVqbOqzCqDifE13RM_Kx81-p4l8aENzOFedSmTkWIXrlipTgRBwlpkln17bI1Vm8xpMkew0xUs-3q658NMypH3zrXnq91etVB3UYGykO62K2JvVPiJWp3YtS9SzqwC9d9nUAneCDxZp2mg1U_DDouY7XWaQYMwKI-RF3aF1WdH4-xKdFuMa7WpHqOUywdkKvjtY7PG5QTLIX6WNsHlqqM_FKwPobpB_OhTFWmqiiYoBb-adI15oQEb4ujLPZR1CRibFEZZ7XlJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efae7c8d8f.mp4?token=rQDr856EcgYK86j7pwDjj6-LhvjwdWuKofVwQATXzcdDmsVtVSpN7pfbiD2AwNkPEA_CI4qJOblgVqbOqzCqDifE13RM_Kx81-p4l8aENzOFedSmTkWIXrlipTgRBwlpkln17bI1Vm8xpMkew0xUs-3q658NMypH3zrXnq91etVB3UYGykO62K2JvVPiJWp3YtS9SzqwC9d9nUAneCDxZp2mg1U_DDouY7XWaQYMwKI-RF3aF1WdH4-xKdFuMa7WpHqOUywdkKvjtY7PG5QTLIX6WNsHlqqM_FKwPobpB_OhTFWmqiiYoBb-adI15oQEb4ujLPZR1CRibFEZZ7XlJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت
وزیر خزانه داری آمریکا در مورد ایران:
همه می‌خواهند این وضعیت به پایان برسد. ۴۷ سال است که با این رژیم شیطانی زندگی می‌کنیم و مردم جهان از این وضعیت خسته شده‌اند.
مردم ایران، مردمی بزرگ هستند. اما متاسفانه، یک رژیم سرکوبگر بر آن‌ها حاکم است. یا این رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، وگرنه باید ببینیم چه اتفاقی می‌افتد.
ما آن‌ها را از نظر اقتصادی به زانو درخواهیم آورد. آن‌ها در چیزی که من "چنگال مرگ اقتصادی" می‌نامم، گرفتار شده‌اند.
ارز آن‌ها در حال سقوط است و صادرات نفت آن‌ها به صفر رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22292" target="_blank">📅 19:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز به نقل از دیپلمات‌ها گزارش داد آمریکا، بریتانیا، فرانسه و آلمان در تلاش‌اند شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای ایران را به شورای امنیت سازمان ملل گزارش دهد. این اقدام در صورت تصویب، نخستین ارجاع پرونده ایران به شورای امنیت از سوی شورای حکام در حدود ۲۰ سال گذشته خواهد بود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22291" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m565DHuq9fBN16m50IOnuTE9Zuuz_Bs4K3OlqTDbepfj_587SXN0lFzVDoP5q5RIPZp4R45kvDR59EqLtYNArqbL6gZRenlAprCwPCOjbEPFAYjjUBCJh7h7efGLtnmIeQTHfe_d8iX8hqtAG7v0sBh0hY0w8UqD8TE3yqWWuNDAoGP-1HjRjcPTHo3WaBTUJfH4ctEgJccTwRVXBJbUW5zFscmrZRHep3i9fhvSWxCOixXEZV_jJFMcROS_150g_wVJ436mdIpEXp0kV2l5t5U6Uot23ZI_LjT8tbeg5cF2RyI1nP8qPeVe8s-QvK9nCbHLEbnDlj4tk_0ilHVuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : چتربازان ارتش ایالات متحده تجهیزات ارتباطی را در مکانی دورافتاده در خاورمیانه مخفیانه مستقر می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22290" target="_blank">📅 18:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416629840b.mp4?token=HVceCZjUz1QLHUbvfl1JIjYHFMz0AO3w7y5pZhRsLf0D08w-s_Xe1favfxT0WSpZ2BWsWTjObTiollhLUGInSuUCAElRD-znmAykJ1tBsuL7-N7pvVSKWHvc20_FMd3ulNX6884kMr5uOUV5NvXccris0yGDwvGOON4AuY5XyqndtsOvIGWKGg8HRFOAN0o9mhMoMmI6m9sapk2HVGzjvY4kogWcSnGKDP_VcQGuzd5hMD3ZQrm1SbY5Wd-PTx9ga5CIiqoOtavzZrI-Ge18OIHwkRrN3o37Gd8m6kHYCERa4ZCJaS6fAgsLYk3iDOyuTjAGInYdj533SF219JCMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416629840b.mp4?token=HVceCZjUz1QLHUbvfl1JIjYHFMz0AO3w7y5pZhRsLf0D08w-s_Xe1favfxT0WSpZ2BWsWTjObTiollhLUGInSuUCAElRD-znmAykJ1tBsuL7-N7pvVSKWHvc20_FMd3ulNX6884kMr5uOUV5NvXccris0yGDwvGOON4AuY5XyqndtsOvIGWKGg8HRFOAN0o9mhMoMmI6m9sapk2HVGzjvY4kogWcSnGKDP_VcQGuzd5hMD3ZQrm1SbY5Wd-PTx9ga5CIiqoOtavzZrI-Ge18OIHwkRrN3o37Gd8m6kHYCERa4ZCJaS6fAgsLYk3iDOyuTjAGInYdj533SF219JCMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار جان امروز توی تونل خرم اباد بروجرد پر از لانچر بود
ولی هفته قبل که اومده بودم نبودن
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22289" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز گزارش می‌دهد پنتاگون دستورالعمل جدید غربالگری کمبود تستوسترون در نیروهای نظامی ۳۰ ساله و بالاتر را موقتاً پس گرفته تا آن را به‌روزرسانی کند. این دستورالعمل قرار بود غربالگری سالانه جداگانه‌ای برای مردان و زنان ایجاد کند و در صورت نیاز، آزمایش خون و درمان هورمونی را دنبال کند. پنتاگون می‌گوید هدف از این طرح، شناسایی مشکلات هورمونی و مرتبط با سطح انرژی و در نتیجه افزایش آمادگی و توان عملیاتی نیروهای نظامی است. دستورالعمل موقت فعلی همچنان اجرا می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22288" target="_blank">📅 18:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آمریکا تحریم‌های جدیدی مرتبط با ایران اعمال کرد و سه نهاد را هدف قرار داد. در میان این تحریم‌ها، نام «گلدن گلوب دمیر چلیک» (Golden Globe Demir Çelik)، یک شرکت مستقر در ترکیه، دیده می‌شود که وزارت خزانه‌داری آمریکا آن را به سپاه پاسداران مرتبط دانسته است. بر اساس اعلام آمریکا، این شرکت در شبکه فروش نفت مرتبط با سپاه فعالیت داشته و در معاملات نفتی ایران نقش داشته است
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22287" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a080330157.mp4?token=hwnIZDf26vpEbqDF7_GpemxUhCYF2BSey5BRpLgyOfGMvib_zFmosp-7PHqn5sFfGCYWAa6kU5ZDms02bVNl9M2wXO8H_BO9D58ZiU3eyd3Hrr1matZGVf-csqBUTLpCUf7Kau2l7jmjhNO5wH5v2amY3iH3GsVyaj8EVFE-9M-Jq5TGvFUFDSfKjkkewXYEXB32xByxGUs6kLUyMUuETMIHI14i1esyF2qwtBPHaIQfci7XcuwapClCAqLBpX0zUmqlYDWFGI6xgD0Lyes81vsCaKY9TTBI1lv4jnDLrlipob3CJbZRPImw8vCnQdOfFK-aqwT6N4sziEM1lUzzNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a080330157.mp4?token=hwnIZDf26vpEbqDF7_GpemxUhCYF2BSey5BRpLgyOfGMvib_zFmosp-7PHqn5sFfGCYWAa6kU5ZDms02bVNl9M2wXO8H_BO9D58ZiU3eyd3Hrr1matZGVf-csqBUTLpCUf7Kau2l7jmjhNO5wH5v2amY3iH3GsVyaj8EVFE-9M-Jq5TGvFUFDSfKjkkewXYEXB32xByxGUs6kLUyMUuETMIHI14i1esyF2qwtBPHaIQfci7XcuwapClCAqLBpX0zUmqlYDWFGI6xgD0Lyes81vsCaKY9TTBI1lv4jnDLrlipob3CJbZRPImw8vCnQdOfFK-aqwT6N4sziEM1lUzzNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از کرمان
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22286" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آکسیوس گزارش داده است که
استیو ویتکوف و جرد کوشنر، فرستادگان دونالد ترامپ، این آخر هفته به مسکو و کی‌یف سفر می‌کنند
تا تلاش‌های دیپلماتیک آمریکا برای پایان دادن به جنگ روسیه و اوکراین را از سر بگیرند. طبق گزارش آکسیوس، قرار است ویتکوف و کوشنر
شنبه با ولادیمیر پوتین در مسکو و یکشنبه با ولودیمیر زلنسکی در کی‌یف
دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22285" target="_blank">📅 17:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFwyxmjO80yWWJRiMIHO-MgfQeIizpGNB4Ei51xDi4SDEN5bvTS2ZW7uH96hMYcn6T5WhD1i-7ZPHG_oQIJivzA29Kzs-5RYh0PkJMF-j8UlOuJ-j2vmVoRCoUbXPXNUYA-nkCIB6cllAc4LWaLGHvrrrIoxky7kt9PdwNN6InS-5F85Wyaq4oPPrsGpzOCKu49_aSGowKgES9YsjLYUPQVZJhbDjXN1yIF4Agx5eDfALDjmN_LC9wQfeFaXoNTWPhVnihstJld9mEkQgaJuPfA8kgHopnPhpZE0Xev3m0gBAwcnFJ8IlKZkpZn1_DyGVuJ7oLxgkW9luhzTv6Ik7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از‌ سیریک به سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22284" target="_blank">📅 17:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پنتاگون اعلام کرده است که در جریان حملات موشکی و پهپادی اخیر ایران به مواضع نیروهای آمریکایی در اردن،
۱۲ نظامی آمریکایی زخمی شده‌اند
.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22283" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی‌ ونس : «همه چیزهایی که ممکن است اتفاق بیفتد روی میز است؛ فشار اقتصادی، فشار نظامی، فشار دیپلماتیک و فشار مخفیانه (
به شکل مخفیانه عملیات‌های خرابکارانه در ایران انجام شود
).»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22282" target="_blank">📅 14:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b10940b05.mp4?token=vUIxXYWUeZSgJNQnUhG_pJ6nNzeiOvA2QIW4cjOwKh94I4CLwdl5YFhYgoXA8D4nsN9WlhAA1jTr1BbE0GObsJUZuFCkKIQV6eLcoxIOqNEx1Y-BgmV7ZQYFy_S9_SOxJUfsuqTRGlPYKl0WlPOT4gHUzOrXwtHqP6ITJBXK7NKs0iK6obkSBmbrpDsF0BDZhzmn0FJ15dhwWxft4esm_wlKVnppTh6IBJ1xgUAAz10dF_nq4sInOazOtvHEUpkPO6MiXJLM__jH1hfr6O1AVq8SuqCss2Dzz3SJDkdtTjdQ39tZnWCfnHFEQAKDbwLoOwY0bJeFpW-7vOgiGxzgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b10940b05.mp4?token=vUIxXYWUeZSgJNQnUhG_pJ6nNzeiOvA2QIW4cjOwKh94I4CLwdl5YFhYgoXA8D4nsN9WlhAA1jTr1BbE0GObsJUZuFCkKIQV6eLcoxIOqNEx1Y-BgmV7ZQYFy_S9_SOxJUfsuqTRGlPYKl0WlPOT4gHUzOrXwtHqP6ITJBXK7NKs0iK6obkSBmbrpDsF0BDZhzmn0FJ15dhwWxft4esm_wlKVnppTh6IBJ1xgUAAz10dF_nq4sInOazOtvHEUpkPO6MiXJLM__jH1hfr6O1AVq8SuqCss2Dzz3SJDkdtTjdQ39tZnWCfnHFEQAKDbwLoOwY0bJeFpW-7vOgiGxzgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح…</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22281" target="_blank">📅 14:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b2ff651.mp4?token=QQSJW0QbPpz83ew9y19qyxM-yFM1Ij8QlC_6f9jRdMb_ZUIHen-qqIUEfIBNPXQtk-uMfFSuflEflaxUxOScWogknlyoYtlxH_YdTmW7gmBxeX78vyi7Zn0r9dMUah-VaQtZqgw0XJUwfJGDowNwY4BvDmY6tWhLO-uL6CwxuP07HyQambrcC4D9z55L4oR6nD-KNDYIT-PgumjUkUCXgekjCfcoDvKeKFX6D9FQQ1FrjyjWChjdMqHl5pntSHoCNFHYZU3m8jauTO3R_Lv-H9J2EJpcwZw4BShENfaUQAu_kaa0Dlfm9R-A9zULp1isgMh0JocswWpUMvi1KEDwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b2ff651.mp4?token=QQSJW0QbPpz83ew9y19qyxM-yFM1Ij8QlC_6f9jRdMb_ZUIHen-qqIUEfIBNPXQtk-uMfFSuflEflaxUxOScWogknlyoYtlxH_YdTmW7gmBxeX78vyi7Zn0r9dMUah-VaQtZqgw0XJUwfJGDowNwY4BvDmY6tWhLO-uL6CwxuP07HyQambrcC4D9z55L4oR6nD-KNDYIT-PgumjUkUCXgekjCfcoDvKeKFX6D9FQQ1FrjyjWChjdMqHl5pntSHoCNFHYZU3m8jauTO3R_Lv-H9J2EJpcwZw4BShENfaUQAu_kaa0Dlfm9R-A9zULp1isgMh0JocswWpUMvi1KEDwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله بوشهر ، کشتی هدف قرار گرفته شده توسط آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22280" target="_blank">📅 14:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز: برخی تأمین‌کنندگان چینی مواد معدنی کمیاب، از فروش و ارسال این مواد به شرکت‌های آمریکایی خودداری می‌کنند. این شرکت‌ها نگران‌اند که به‌دلیل همکاری با برنامه‌های آمریکایی برای بررسی و شفاف‌سازی زنجیره تأمین، با مجازات دولت چین روبه‌رو شوند. چین اوایل…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22279" target="_blank">📅 14:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رویترز: برخی تأمین‌کنندگان چینی مواد معدنی کمیاب، از فروش و ارسال این مواد به شرکت‌های آمریکایی خودداری می‌کنند.
این شرکت‌ها نگران‌اند که به‌دلیل همکاری با برنامه‌های آمریکایی برای بررسی و شفاف‌سازی زنجیره تأمین، با مجازات دولت چین روبه‌رو شوند. چین اوایل اوت ائتلاف کسب‌وکارهای مسئول آمریکا را تحریم کرده بود. مواد معدنی کمیاب در صنایع مختلف، از جمله
تولید تراشه، هوافضا و تجهیزات دفاعی و نظامی
کاربرد دارند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22278" target="_blank">📅 14:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صحبتهای زیبای یک کاربر : ‏آقای ایرج مصداقی، نمی‌خواهید این حاشیه‌ها را تمام کنید؟ صبح تا شب مقابل دوربین نشسته‌اید و به این و آن حمله می‌کنید؛ نتیجه‌اش هم چیزی جز خوراک دادن به پهلوی‌ستیزها و فراهم کردن بهانه برای حمله به رضاشاه دوم نیست. ‏شما عضو جریان عدالت…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22277" target="_blank">📅 14:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایرج مصداقی متولد۱۳۳۹ ، نویسنده و زندانی سیاسی دهه ۶۰ و از بازماندگان اعدام‌های سال ۱۳۶۷ است که حدود ۱۰ سال در زندان‌های اوین، قزل‌حصار و گوهردشت زندانی بود و بعدها خاطراتش را در مجموعه چهارجلدی «نه زیستن، نه مرگ» منتشر کرد.  مصداقی در سال‌های ابتدایی دهه…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22276" target="_blank">📅 13:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">من کدومم ؟
😁</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22275" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNokte_sanj</strong></div>
<div class="tg-text">من فیلمبردارو زنده میخوام</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22274" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جی دی ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22273" target="_blank">📅 12:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الجزیره: ایران لیست سیاه ( متخلفین ) خود را برای کشتی‌ها به بیش از ۵۰ مورد کشتی به‌روزرسانی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22272" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فایننشال‌تایمز تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22271" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">من کدومم ؟
😁</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22270" target="_blank">📅 12:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c519fba49.mp4?token=JrhwYEWfQd2lplMXqMr4_UyI535-TfLqLH6b0_6DmTOSmaRnIJXfpaCYBoXnb1javPvOWyPlOve2YNSJOf4NffHFPAvqAtfztWUUQq52WU8wceYFG10HbjAQXlzn1TDDCNArdnVrYxABPG9Ygv67Um7ACsigOMMmyPIW0rOs78Cnjou25Kvn8nH6YnfHerP1UyQ6VUmdbFMCrzhCdaohbNneVopPa74ft7_8xjLlqjJIR5nu9SZL4Jw_RYRcyfZM10ZYvrWerQhIYvlXAHYBUq5BN7R0NpVag03C2XmZIi1aqZ4BKgZ3-Ep6os3KZ-yAuRmFwrxErMrAVRFu5kw_FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c519fba49.mp4?token=JrhwYEWfQd2lplMXqMr4_UyI535-TfLqLH6b0_6DmTOSmaRnIJXfpaCYBoXnb1javPvOWyPlOve2YNSJOf4NffHFPAvqAtfztWUUQq52WU8wceYFG10HbjAQXlzn1TDDCNArdnVrYxABPG9Ygv67Um7ACsigOMMmyPIW0rOs78Cnjou25Kvn8nH6YnfHerP1UyQ6VUmdbFMCrzhCdaohbNneVopPa74ft7_8xjLlqjJIR5nu9SZL4Jw_RYRcyfZM10ZYvrWerQhIYvlXAHYBUq5BN7R0NpVag03C2XmZIi1aqZ4BKgZ3-Ep6os3KZ-yAuRmFwrxErMrAVRFu5kw_FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامتم زیر پست جدید و جنجالی نتانیاهو
https://www.instagram.com/reel/Dc25xWUsghi/?comment_id=18135318097727381</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22269" target="_blank">📅 11:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammadreza</strong></div>
<div class="tg-text">سلام یاشار جان
امروز بانک ملت شعبه مرکزی شیراز رو داشتن دور تا دورش آهن جوش میدادن ساختمونه شیشه‌ایه داشتن آهن دورش جوش میدادن خودشونم میدونن قراره چی بشه</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22268" target="_blank">📅 11:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیا:
به‌زودی دشمن رو در میدان غافلگیر میکنیم
رفتارهایی با دشمن خواهیم داشت که کاملا گیج، مبهوت و شگفت‌زده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22267" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ccab60afb.mp4?token=SA7R3VQPhiH3p88mRl1clBmMc9oo_mJpSOGoG4HAEGiDYuPiIn36uHZ5u-A9aEXkpr2A9g2cVgSKibz5t6_K0kdJMhGJrT7oK0TYFkHFwgepIRu_qlaHu_-I3ojatcVXF8zWCThHc_zSuqjgMqNKGP6eiCBPBY4LLYwd3Csxjd1S3l_cVl0NScF3Izk8ZwZZgGUOqSOeeny_WSgIaBi8kbgUSTQ_MB7RJhpqrWHG24QvekjegLM97dh14JeRuOrXUv-U-fpRJQBg7FSKp0flj7T6mbobjalW8zR5muNcQVu2vN_hfooIlyWtAJWQVRiAgb8PMXbYIbNsokVl6cIDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ccab60afb.mp4?token=SA7R3VQPhiH3p88mRl1clBmMc9oo_mJpSOGoG4HAEGiDYuPiIn36uHZ5u-A9aEXkpr2A9g2cVgSKibz5t6_K0kdJMhGJrT7oK0TYFkHFwgepIRu_qlaHu_-I3ojatcVXF8zWCThHc_zSuqjgMqNKGP6eiCBPBY4LLYwd3Csxjd1S3l_cVl0NScF3Izk8ZwZZgGUOqSOeeny_WSgIaBi8kbgUSTQ_MB7RJhpqrWHG24QvekjegLM97dh14JeRuOrXUv-U-fpRJQBg7FSKp0flj7T6mbobjalW8zR5muNcQVu2vN_hfooIlyWtAJWQVRiAgb8PMXbYIbNsokVl6cIDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰ هزار نفر شامگاه پنجشنبه در مراسم مذهبی «سلخوت» در محوطه دیوار غربی (دیوار ندبه؛ بخشی از دیوار حائل محوطه کوه معبد در اورشلیم) گردهم آمدند و به دعا پرداختند. بنیاد میراث دیوار غربی اعلام کرد که از آغاز ماه «اِلول»، بیش از ۵۰۰ هزار نفر در مراسم سلخوت در این محل شرکت کرده‌اند. این مراسم که از ۱۴ اوت آغاز شده، تا شب یوم‌کیپور در ۲۰ سپتامبر ادامه دارد. پس از آن، روش‌هشانا (سال نوی یهودی) از شامگاه ۱۱ تا ۱۳ سپتامبر و یوم‌کیپور از شامگاه ۲۰ و ۲۱ سپتامبر برگزار می‌شود
«این مراسم در آستانه اعیاد بزرگ یهودی برگزار شد؛ دوره‌ای که از شامگاه ۱۱ سپتامبر با روش‌هشانا آغاز می‌شود و تا ۴ اکتبر ادامه دارد و مقام‌های اسرائیلی نسبت به احتمال حمله ایران در این دوره هشدار داده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22266" target="_blank">📅 10:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818a226b89.mp4?token=jPLUB9cdMH9GgEKnsEnnIS0SsViGYC8IGywyUEFptGeQjGRXIFgiguxEqVv-td4Z3idDJdb4rXEtKH2n2acl6WzxCuCpWsc0Z1HPUjlIS9_OcH1dED8MofXKpz2nUJuMIzhHtB_Qdg9o2U3mVXY54DM6LKWh5ev3aB4ys9PutucVFa0OWTSI86wmk_T34lh7A-C5ragxBAWv7k6RKUzm6deeMoPbhJbAZUL9sJLM4xiSvRkSkYvJQyIYDdK7MB24U9eamaosq2YnK7zC6GL0ZezQsXi3dyjL1hSr4QH2KGjM4FEh80d513vSef3yx4wEXOlg3OBmblylNRA8PV6AIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818a226b89.mp4?token=jPLUB9cdMH9GgEKnsEnnIS0SsViGYC8IGywyUEFptGeQjGRXIFgiguxEqVv-td4Z3idDJdb4rXEtKH2n2acl6WzxCuCpWsc0Z1HPUjlIS9_OcH1dED8MofXKpz2nUJuMIzhHtB_Qdg9o2U3mVXY54DM6LKWh5ev3aB4ys9PutucVFa0OWTSI86wmk_T34lh7A-C5ragxBAWv7k6RKUzm6deeMoPbhJbAZUL9sJLM4xiSvRkSkYvJQyIYDdK7MB24U9eamaosq2YnK7zC6GL0ZezQsXi3dyjL1hSr4QH2KGjM4FEh80d513vSef3yx4wEXOlg3OBmblylNRA8PV6AIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در باره ایران
: «به محض اینکه به پیروزی برسیم»
اما بلافاصله متوجه شد و گفت زیاد طول نمیکشد و بعد سخنش را عوض کرد و گفت
: «همین الان پیروز شده‌ایم
چون آنها نمیتوانن‌ سلاح هسته ای داشته باشند
»
و اگه
ما امروز از جنگ علیه ایران خارج بشیم هم بازسازی این کشور ۲۵ سال طول میکشد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22265" target="_blank">📅 10:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22264" target="_blank">📅 09:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با یاشار : کره جنوبی جفت کرد !
رویترز: کره جنوبی در حال آماده‌سازی برای اعزام نیروهای نظامی به تنگه هرمز است
؛
رسانه‌های محلی کره جنوبی با استناد به منابع نظامی و دولتی گزارش داده‌اند که این نیروها برای حمایت از
آزادی کشتیرانی (امکان عبور ایمن و آزاد کشتی‌ها)
در تنگه هرمز مستقر خواهند شد و سئول قصد دارد آنها را
پیش از پایان سال
اعزام کند. این تصمیم در حالی مطرح شده که دونالد ترامپ،
رئیس‌جمهور آمریکا، در ماه اوت اعلام کرده بود در حال کاهش همکاری نظامی با کره جنوبی است
؛ بخشی از دلیل این تصمیم، به گفته او، خودداری سئول از کمک به واشنگتن در جنگ علیه ایران بوده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22263" target="_blank">📅 04:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اعلیحضرت همایون شاهنشاه آریامهر محمدرضا پهلوی
: هیچوقت به زندگی فعلی خود قانع نباشید و همیشه دنبال بهتر کردن زندگی خود باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22262" target="_blank">📅 03:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: اتحادیه اروپا رسماً به کارزار انزوای اقتصادی علیه ایران پیوست و ما از موضع قاطع و به‌موقع آن قدردانی می‌کنیم. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22261" target="_blank">📅 03:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز :
یک بات‌نت (شبکه‌ای از رایانه‌های آلوده) به نام
«سلیتی»
که از سال ۲۰۰۳ فعال بود و طی هشت سال گذشته برای سرقت ارز دیجیتال نیز استفاده می‌شد، در عملیات مشترک آمریکا و اروپا از کار انداخته شد. این شبکه بیش از
۱۵ هزار رایانه آلوده
داشت و برای سرقت رمزارز، ارسال هرزنامه و حملات سایبری استفاده می‌شد. هم‌زمان، کمیسیون معاملات آتی کالای آمریکا از دادگاه خواست شکایت
سی‌ام‌ای گروپ
درباره معاملات پرپچوال رمزارزی (قراردادهای بدون تاریخ انقضا) را رد کند. همچنین وزارت دادگستری آمریکا اعلام کرد
بیش از ۵۶۰ هزار دلار رمزارز متعلق به حماس (گروه اسلام‌گرای فلسطینی)
را که برای تأمین مالی این گروه در نظر گرفته شده بود، توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22260" target="_blank">📅 03:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چندین پرتاب موشک/پهپاد به سمت تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22259" target="_blank">📅 03:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: اتحادیه اروپا رسماً به کارزار انزوای اقتصادی علیه ایران پیوست و ما از موضع قاطع و به‌موقع آن قدردانی می‌کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22258" target="_blank">📅 03:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارتش این کشور شبکه زیرزمینی راهبردی حزب‌الله در منطقه تپه علی‌الطاهر را به‌طور کامل پاکسازی کرده ,
نیروهای لشکر ۳۶ کنترل عملیاتی منطقه را در سطح زمین و زیر زمین به دست گرفته‌اند؛ در این شبکه‌ها اتاق‌های فرماندهی، انبارهای سلاح و امکانات اقامت طولانی‌مدت کشف شده و برخی نیروهای
نیروهای
حزب‌الله و سپاه
حاضر در این محل
کشته یا متواری
شده‌اند.
این زیرساخت زیرزمینی که به گفته اسرائیل طی حدود دو دهه با تأمین مالی و برنامه‌ریزی ایران ساخته شده، همچنان در حال منهدم شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22257" target="_blank">📅 02:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیدبان اتاق جنگ سیریک :  امشب تنگه خیلی صدا میاد از ساعت ۱۱ تا الان بالایی ۱۵ صدا اومده ، کمی پیش پرتاب موشک انجام دادن ولی الان از تنگه یه صدای مهیب اومد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22256" target="_blank">📅 02:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f2f2934c.mp4?token=QiThxron06qCjbobEAs4XNztZHxASjjW0_48ciMRcm7InL7IBxcO750cJEYe0Yg4stO3KAmOjSajApeIQWMRetQUR3QvYRxNlcrBve6JAtE8naAuPCTmcG5WgnYX6BRg3N4WlWRrLmk0sQdzLFXNn4HzHys2eVqJzzNQ3LK9AB2L84_uvokpgmke86HMNwK01cUOpE65hQCAMhYEoSF4_gXfoHQtyD6k_PHJYYs09ifX7Dgb7oMdsjKr8kDTBvGt93KDkVg-x6vH9TqJi9ZuLPMAVAF7P-0h-GfJN6ikseMQ3AqiNkpdVw2TLGWsa4HrP9C-7hBWXpCkuAOhl7EAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f2f2934c.mp4?token=QiThxron06qCjbobEAs4XNztZHxASjjW0_48ciMRcm7InL7IBxcO750cJEYe0Yg4stO3KAmOjSajApeIQWMRetQUR3QvYRxNlcrBve6JAtE8naAuPCTmcG5WgnYX6BRg3N4WlWRrLmk0sQdzLFXNn4HzHys2eVqJzzNQ3LK9AB2L84_uvokpgmke86HMNwK01cUOpE65hQCAMhYEoSF4_gXfoHQtyD6k_PHJYYs09ifX7Dgb7oMdsjKr8kDTBvGt93KDkVg-x6vH9TqJi9ZuLPMAVAF7P-0h-GfJN6ikseMQ3AqiNkpdVw2TLGWsa4HrP9C-7hBWXpCkuAOhl7EAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی غرب تهران چیتگر
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22255" target="_blank">📅 02:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb363544dd.mp4?token=TnLry9BWa-9XLkTX5ApYwnoyhce9dXWg4IN-TcSTXmJqCl3dqk2Os5NLOgcL_7y6PoW7NatahuCj9XXzGDaBYwtaQ-4qQrNCP_aMB0ERgsH-18jvvNMVY2K-bp5pemxJO2IvK5FGJD2rwfFtf9Ry5n1VVDlAUmYq-H1XEPLAW--biD8UomtgC_x8ya9zy7AcpOgyp-Jb559pxr8G1mWKV1tbuI--2OQ4UYCaPKvatNf7ntOXVli93y9VDxdyOd9oNUFVawI-NOK9LIy_wIW1GqdlsUe92MSdDSd6cmsBRI8Ey27F7Majs-Upey8xzKtJp3RRmx5rmwElTvqdgHD-fgl8uZKCm8E6raxrNlxJyrZNHHOVZBBlhM-bVjbpbPhJ68HtTo9zivA3i6ywzJ8bgl0Ze9PjgbZkclzcP1QC6dqGF-wo2_51WxCb92xZsK-ISdgQbY95jO3RDZ5rni62muXh3SZZcgcl2kDRluNKS7JshNLSrqGgmm47Y_aVQdw43OO40lBvQeXZ_rMg8tz4XvWi3cft7GEMNjst0brrfmrzw1AZMgfSDq7ebZhhFaMxxqqZjg8oJ3xIdHuZFF07-uSWkBjIqwtdG_dOkr3muSdMVvg085Ume1EoDy8BM709AC0YQPmrDB99o7jH-6m-Uh7bODN20pjCros6toTItZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb363544dd.mp4?token=TnLry9BWa-9XLkTX5ApYwnoyhce9dXWg4IN-TcSTXmJqCl3dqk2Os5NLOgcL_7y6PoW7NatahuCj9XXzGDaBYwtaQ-4qQrNCP_aMB0ERgsH-18jvvNMVY2K-bp5pemxJO2IvK5FGJD2rwfFtf9Ry5n1VVDlAUmYq-H1XEPLAW--biD8UomtgC_x8ya9zy7AcpOgyp-Jb559pxr8G1mWKV1tbuI--2OQ4UYCaPKvatNf7ntOXVli93y9VDxdyOd9oNUFVawI-NOK9LIy_wIW1GqdlsUe92MSdDSd6cmsBRI8Ey27F7Majs-Upey8xzKtJp3RRmx5rmwElTvqdgHD-fgl8uZKCm8E6raxrNlxJyrZNHHOVZBBlhM-bVjbpbPhJ68HtTo9zivA3i6ywzJ8bgl0Ze9PjgbZkclzcP1QC6dqGF-wo2_51WxCb92xZsK-ISdgQbY95jO3RDZ5rni62muXh3SZZcgcl2kDRluNKS7JshNLSrqGgmm47Y_aVQdw43OO40lBvQeXZ_rMg8tz4XvWi3cft7GEMNjst0brrfmrzw1AZMgfSDq7ebZhhFaMxxqqZjg8oJ3xIdHuZFF07-uSWkBjIqwtdG_dOkr3muSdMVvg085Ume1EoDy8BM709AC0YQPmrDB99o7jH-6m-Uh7bODN20pjCros6toTItZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی در آسمان شهریار
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22254" target="_blank">📅 02:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22253" target="_blank">📅 01:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اتاق جنگ با یاشار: قوه قضائیه جمهوری اسلامی حکم اعدام شاهزاده رضا پهلوی را صادر کرد!
جمهوری اسلامی در تازه‌ترین اقدام خود علیه
شاهزاده رضا پهلوی
، پرونده‌ای با اتهام‌هایی از جمله «افساد فی‌الارض»، جاسوسی و همکاری با دولت‌های متخاصم تشکیل داده ؛ اقدامی که یادآور سابقه جمهوری اسلامی در تهدید و صدور احکام علیه مخالفان خارج از کشور است.
سلمان رشدی
؛ در سال ۱۳۶۷، روح‌الله خمینی فتوای قتل نویسنده بریتانیایی را صادر کرد و برای سال‌ها جمهوری اسلامی در تعقیب او بود، اما رشدی زنده ماند و به فعالیت خود ادامه داد.
دونالد ترامپ و بنیامین نتانیاهو
نیز بارها هدف تهدید به قتل و مجازات قرار گرفته‌اند و در
تجمعات حکومتی جمهوری اسلامی، عروسک‌های آنها را به چوبه‌های دار آویزان کرده‌اند
؛ هم‌زمان مقام‌های حکومتی نیز بارها از مجازات و اعدام آنها سخن گفته‌اند. حالا شاهزاده
رضا پهلوی
نیز به این فهرست اضافه شده است و نشان از مسیر درست ایشان و ترس حکومت از وی دارد ؛ فهرستی که از
ترامپ، نتانیاهو
تا
سلمان رشدی و اکنون با شاهزاده رضا پهلوی
امتداد پیدا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22252" target="_blank">📅 01:53 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
