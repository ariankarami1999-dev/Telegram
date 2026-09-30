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
<img src="https://cdn4.telesco.pe/file/HT6EXeMy86Uzzq7Ray0uAXZyQ8jnql4YFm9JxTOqYbLHTELQebm1x3fj0cGGq0YqQAjuJ-yn40CGeZdqzIaK8eWymlt3gXOdnOlUQGMMl7keDLJKJJymDRB6gsgW00Ra9Eyzh0-hgdCehwHAavTCSV5q51FRLTLUUbuD6KJ2O0ZK1xjdv_ZpZyHC13gmVMmf9SpE5j2IcymPE4HQao3NSXKaQxl8Hh77Tr2xtr0YcVgxSUZvQvrvcPTKwF7XsQqoN0us5ln5YZNVinFxGad7zLuOIRKPl1ynsATt7maKU3hATIIMdfzWA4sEMU4GpskTHe_K1oTXWa_wUYoKKae90g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEJYSLfE6iv1L2wxFx3jhcCV86s527y9aOHz_WyFd-fuf0HddZbDkMALzr-1EGv_wheIDt4vQ6jhBA33pzReXv3ucwHNuIyOQbCk1BwAqdHmhXGre9auEXq9JRWa9xvW0z5NiAeaUn1hYDN0rY6upka3wtvTcW9anw5VOc6lHFsW30pvrtcHAl1cwe98LY0tuwIhh4-0PmaGlKP7y--7BwxFfnYcOkEEPieNUHogm5janbNnA5CCUkaeqDpXCCh5TVrhy3KXew07y5hZrDw5DM6BgoL-Kh3v2-21vMSQi0OClX4MyxD1FCK8GbgQbZC6qA-r8XOafvHXg4lrVX7sXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/140755" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
تیمداری مجدد پرسپولیس در والیبال پس از سال ها
❌
❌
تیم والیبال پرسپولیس تهران در گروه چهارم رقابت های دسته یک کشور با تیم‌های طلایی‌پوشان ورامین، نیروی زمینی تهران، بوعلی قم، مقاومت شهرداری تبریز، سروقامتان ارومیه، بنیس شبستر تبریز و روژمیوه زریبار مریوان…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/140754" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/140753" target="_blank">📅 16:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/140752" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/140751" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/140750" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/140749" target="_blank">📅 16:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=Jt24mCeikniJtAWD6c3ZhkAI3Yc6SJRqxSgCbomMK0SQ4AeKPOKRY0lQQdvgDrFONFBhO0e_oTxwuoBs40KKSqb94CaJxLHjhXzNNBNnvOOjlD2PM82y2sJNOqfMJQOQJQHawPEgAnV5kOAE7Zm5sprSpVHeuiGvt8VdF679oYVeLe04opTRWkI0M8ow5NOk_pUooOilyZWE5GRJfciZt1QmhikzZSN35SVHZ7pFmqFwW1CPAEuglgupCvspFwCrPd3u-kS-XKs-gmL1sHxAN436sRvJpvYI5TtJDpJiPrBPOUBdTDPbLTHyqrlwKzJaH_ACv0vvCV8o6JKBzI0mDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c1a357e.mp4?token=Jt24mCeikniJtAWD6c3ZhkAI3Yc6SJRqxSgCbomMK0SQ4AeKPOKRY0lQQdvgDrFONFBhO0e_oTxwuoBs40KKSqb94CaJxLHjhXzNNBNnvOOjlD2PM82y2sJNOqfMJQOQJQHawPEgAnV5kOAE7Zm5sprSpVHeuiGvt8VdF679oYVeLe04opTRWkI0M8ow5NOk_pUooOilyZWE5GRJfciZt1QmhikzZSN35SVHZ7pFmqFwW1CPAEuglgupCvspFwCrPd3u-kS-XKs-gmL1sHxAN436sRvJpvYI5TtJDpJiPrBPOUBdTDPbLTHyqrlwKzJaH_ACv0vvCV8o6JKBzI0mDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ملی‌پوشان فوتبال ایران پس از برگزاری دیدار تدارکاتی برابر روسیه وارد ایران شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/140748" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/140747" target="_blank">📅 15:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG4ETJ4a4Q9U1ANAsCSe9jsoFn0Bdf2g8Lla0ADFrVGKh0_g_x81rDi4C12pFXmfP3AGH8N8tq_m3QkEKbBWiYBIqIBuLC9f2fK4NvqrkAska4jbI0iNBbtKxP4zIfe7lBWaf7YoesuAAv0MgVSSwEElG9NJD0IUx0dSfXGUDgOkphTBnJSP4Bqib9-gjLtWsIVNCHAnD-3G6hu6VjDYhPM6pKHnlmxlFdNKqJCvItcjLnopw7Vk9EeYCrUFY58k_wE7xUe1ffNAR6CpG9hmRusmgJuNcSi9rPr2bwt-RkYIX4y1g2VbvKojZm4yg2dEgKenNisGtjEQJNIkid6w6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
اگه درآینده جنگ رخ بده و بیش از 90 روز طول بکشه بازیکن میتونه یه اخطاره 30 روزه به مدیریت باشگاه‌بده و بعدش‌هم توافقی قراردادش رو فسخ کنه اما اگه جنگ کمتر از 90 روز باشه بازیکنان خارجی باشگاه‌ها حق هییییچگونه فسخی ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/140746" target="_blank">📅 14:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/140745" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/140744" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی  امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :  پ.ن تارتار به شدت راضیه از یاسین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140743" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/140742" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKn4ZFi_wsCZD7yjYpSV9W0W-m6Bs9OlP6R9KvhY-G_oOIh7MPy2MnqfKz1_z6iFzQgtu19m9Gg2QUQKI-sVE9HnvXeUSuCVGaYApumW6E08pH3tzfyBgIT8IH9xyL_XyXR0_pDSEZg59F3FUJmcUAcBLSgJc4qkhfNiGrhlUJOg8DL-lEeXUgAMrGT-6PZcYIASqVHqL2dXjrFx9jz_f_FrdOWawhrDjRuwvWGEtQrENWBhHmsxSoFGZHbVV59XFYdZr4VtzFh9ymqeFSzqJ6sQHEhRrw39NGTh3hPWWqNBc8glknOmT46A99QmSKefSJfcfUoKDGnxGgYNYnV-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
🔵
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
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140741" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
آخرین وضعیت پرونده جادوگر فوتبال؛ تمام اموال نامشروع مصادره شد
🔄
🔄
رئیس کل دادگستری استان البرز:
❌
❌
در پی دستگیری و محاکمه شخصی که در محافل ورزشی به نام «جادوگر فوتبال» معروف بوده است؛ وی به اتهام «فعالیت تبلیغی انحرافی مغایر یا مخل به شرع از طریق ادعای واهی و کذب» به تحمل ۵ سال حبس و ضبط اموال نامشروع حاصل از جرم محکوم شد.
❌
❌
حدود ۶۶۰۰ دلار، بیش از ۲ هزار یورو، ۸۰ سکه تمام بهار آزادی، ۳ شمش طلا و مقادیری طلا و ۲ دستگاه خودرو تویوتا لندکروز و مرسدس بنز از متهم کشف شد.
✔️
✔️
متهم هم اکنون در حال تحمل پنج سال محکومیت حبس صادره است و کلیه آلات و ادوات مختلف مربوط به سحر و جادو که از متهم کشف شده بود هم معدوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/140740" target="_blank">📅 13:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
🏟
بازسازی زیرساخت‌های پرسپولیس
✔️
✔️
رختکن‌ها، چمن، نیمکت‌ها و سکوهای ورزشگاه شهید کاظمی بازسازی و بهسازی شدن. بازسازی کامل استخر درفشی‌فر هم تقریباً تمومه و قراره نیمه دوم مهرماه به بهره‌برداری برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/140739" target="_blank">📅 13:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140738">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤩
⚽
شاهکار پیمان حدادی در پرسپولیس؛ درآمدزایی ۱۳۶۵ میلیارد تومانی از پیراهن سرخ‌ها
❌
پیمان حدادی، مدیرعامل پرسپولیس، پس از پشت سر گذاشتن نقل‌وانتقالاتی موفق و پیروزی در پرونده‌های حقوقی باشگاه، حالا با یک دستاورد اقتصادی قابل‌توجه مورد توجه قرار گرفته است. بر…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140738" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl9XNwfUbVGKChhpSG4hYZbIdSkhB5UyeQEL9jx0bFKgT8H1hrSpmeKlRhGFNY-yIEd7W74pX-q5foQD582mOL5zIud6F1Yx_Aq6iHscrnTwMMxdIym4CjBfy12mJ0QhlAfZeJBOUqzWNOut8bSf-ZJs_OCl5BRFMMx9lxWYObmYH8V8DGo4of_yhtFnLXuF-DphUbU_2hvQTLMX16gYYUm_lI_EahnKE9FnONk-6GQumRJxMB3GhBZF4J1e10IGauxHzCEtPJLlXOB6AoA5m6JD0GBRQuhHqTtDckTJC_DtNMYGMN6pTdm1299RCkb8aLNGQmuc7ay7QFcA4lGg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/140737" target="_blank">📅 11:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=vOJiL6Sj83l-DelTNZ4CSWu5MASfYvfq3ruC_UPFKWj5WKuPB1oRCz_N17Aqk_EHBtoF30pDZaTYA6TrenN4IV1R6-rLdOvw14y07zT_yiE1oWjOhBJnolKtUo7ns4s7e0hQnPtcs17xpKcOwmmKxGLYgVsE86oCqnf-KCUOP3k2_ZK4cxsu1TARhzupgKADHanaBBXdnPhIcqBE1udATnHqpdjEDOEoRWCFOpupavcwIgQEaZVtaYJLvHD0VitzSgYdsnVK7WGmFyOVxh31SEI3BMtXkKCPNPAc5QMrLBiuNsv0rrlEqiw_Do__5ruyZe5wyILSFi1cssU6up7-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3297ba87bf.mp4?token=vOJiL6Sj83l-DelTNZ4CSWu5MASfYvfq3ruC_UPFKWj5WKuPB1oRCz_N17Aqk_EHBtoF30pDZaTYA6TrenN4IV1R6-rLdOvw14y07zT_yiE1oWjOhBJnolKtUo7ns4s7e0hQnPtcs17xpKcOwmmKxGLYgVsE86oCqnf-KCUOP3k2_ZK4cxsu1TARhzupgKADHanaBBXdnPhIcqBE1udATnHqpdjEDOEoRWCFOpupavcwIgQEaZVtaYJLvHD0VitzSgYdsnVK7WGmFyOVxh31SEI3BMtXkKCPNPAc5QMrLBiuNsv0rrlEqiw_Do__5ruyZe5wyILSFi1cssU6up7-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۶ سال گذشت...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140736" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140735">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
مصدومیت دانیال ایری از ناحیه کشاله ران پا بوده و مداوا روش شروع شده تا بزودی به تمرینات برگرده؛ اما بعیده به بازی صنعت نفت برسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140735" target="_blank">📅 10:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140734">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
🏥
دانیال ایری در بازی آخر تیم امید مصدوم شد؛ MRI کشیدگی عضلات لگن و بالای کشاله ران رو نشون داد. کادر پزشکی پرسپولیس هم درمان و فیزیوتراپی رو شروع کرده تا هرچه زودتر برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140734" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/140733" target="_blank">📅 10:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
❌
گروهبان قندلی: از بازیکنانی که به آنها فضا دادیم اما نتونستن چیزی که مدنظر ما هست رو انجام بدن در اردوهای بعدی استفاده نخواهیم کرد
😁
✔️
✔️
این بازی ما رو یاد جام جهانی انداخت و سطحش در حد این رقابت‌ها بود. برای ما بسیار مفید بود هرچند از نتیجه ناراحت هستیم…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/140732" target="_blank">📅 10:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3fpjkQ_Rd0vMeG2Wh-NMuo_a98CliZmVWZ5p3sLW8g4IP83Xzsrt_Lvclpuna92mofMe3KWrkpWGSuxlVqmwyu0639IwF3pJe9GZZZoXHdtSnUNk7eNSKBtUeeWCBCt9fqGhtvJLRk2yd2vBxbllR9IbZ_65xUhTS8of_NWUiNEzrHF2Zcf6YophAL0lH9NnIQlPkAUTLA75PAGjxVmzE-ApUgWcxjuxpEomlpL1MeWmcvanJHu7PUWYKgmoLqS2tjCa2_oRPiD2F41Sf2btV1ZiQv-UEhLlzTZUvv1BZkg9cvkRdLn7EZNLvcsu_5LaudGKDaBjMpFId0ZYLSmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حمله تند روزنامه‌های ورزشی به قلعه‌‌نویی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140731" target="_blank">📅 09:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7gsIHo6ZPIDlrI3dFUCCUNtcihZ46QbOkVZpA5LBsrc7e1EcrN6q08MoWVfx1EVyvsJMrHf1yvzwz6J2XOi2YjV3LWdphAu1yU9_pA4u7XIuwN1qEEJWRr85f4QQTx0dn9HXKsAgZjXiI6R6CfwVP233F4mKoCilhwTdi7M_kKY69WTY21EU8Yw6fGBn_PJQGdwULf7ZB618Jq358RSkYYwD4BkPufgfKNoWy39EfQUJMLUmCqpuZhQ-OPhX5yFtpXHiFqn5rXxaKvAPyOVaUn9MxXS2BtsQt41YbqXFm0H9uYI4xwgtXzM8q9QtTECJd08MlXzXZ-kP63KTTua-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140730" target="_blank">📅 09:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140729">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udTXmW0eWWHJwJYMQmxHqDCtJtW_wZj29C6VPyymj82e3Az5vnRnwXSVEMenadOZU_Q5_CwsgiVXHGWFQ3IYzG8O_3WNGGTmQO02bjS3YPa7dPE10tBh4LsrL-p4K0dRSA6ARK4PW-jGil67sjG-iykvyV_LGcgdvIRqmXRs5KGDbYRLZA3ctxjL6xeDfznPpqYqehGZyjmXBGZADbi8gmhpPU94qjfQXfq7PnJLHnUcKQ7eS3NEicakPphnB3SOYh3ZyV4EEA5g4mR59WbNIP2ObcDGkJNlgCYqMwm2NwOE_1C625JrIOPoUxyY8PDs2xkZ7Srav8os1nE_eD3YTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140729" target="_blank">📅 01:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140728">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKJErih2uDWybO-tMeyX4L3mXLNc2i41hpY36X7vE0OF09gd4SzUgeeZWNFoT5-V2PX-RE0g5JcrB7wtsXvFHH83_PRNKWGDnE9DxoA_n5G2lROCqx1GhDLKHpSfrmgHjkszDw7pTSS1-tBAatYMagfvL9si_RaPP8gMNvCF64W9GMax--LDITLMhKixo0ivyHNfZFZ_20uvCT-fDpJEQWFfBtYCIR9IbS0KUmYjYMdsOigbxeDNg6uoLk7taG_yRoXrGARUSPMkgvMni1-dNZbwjAy4HknxEdqQ9YqN0lwM1F2fcPJ1oM3SmevDFyX4p_4_SsiL5VoLecnJPk3S6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
در تاریخ بنوسید تو فوتبال‌‌فاسد ایران قرار بوده استقلال جام رو بگیره بجاش ٧۵٠ هزاردلار طلبش از مهدی‌تاج رو بلاعوض کنن‌‌. پشت‌پرده درحال انجام بوده اما مخالفت شدید باشگاه‌ها این معامله کثیف پول با جام بهم میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140728" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
#فوووووری
🖍
دانیال ایری به دلیل مصدومیت در تمرین امروز  سرخپوشان غایب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140727" target="_blank">📅 00:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140726" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140725">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHSca4q_NWVOEKS5DSZZz0RB6KFLfvmjDEYcNSZgOaHqbFHWY5wOeMCMSi0JzHBWKpYWT9KyxPsQ6CwwRuHVAebYIGBqboBIyp2hh13JM54HU0Iz7HHa8Rvh6uUEEo4aiDx12Gwk-wz03ddJu8ULWhJVViQmg91Ajk4FqLoQE682M01zUJjAU097zo_UWzlE1C53vSi8rMNMAZqDx8mEcE9jcV9Nmyz_I3gNnplG2zPnHw5VL3JFE9UA8nPrzfp1rV_y2OTOdL4LDyI97VE3sfMiMmn9Q5wf7MC9QUOaWkUpGkU5p9AxNBze2oJ97t2Qek091Qh2P3RxriAvp0Zrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
نتایج بازی های امشب:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140725" target="_blank">📅 00:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140724">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140724" target="_blank">📅 00:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp0Mg6Ed075itxo_dq947nHS88GDMPn3QhDtCOV_zakENV6FnSs5FecXdDIPGJvhGdBPXGwr4wNChThdygfYNAc7HN35axSsAeTi64YuNk56apc37JKjGA3-b4U1NfMyft4pofHQTjuO50c5z2fopjL4aI-d1yIie7a4MmzLcxwocS0Y9T00auGc7PwFRyHqDBzMvSmb5nqpgSiO_UB-qXHWJWYrmcpeEBd1bHsbTapX2pX8zVRozwZRukkmLn_Q-HNhvj-Pz7PftMcOoguGEWPtMu7HpL4UGtStiCZ5mzBKU0TGATzyi8s6XmMmAdtebQGxbNzg7-2kyisfrxPFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
مدت قرارداد احتمالی جدید نیازمند با پرسپولیس مشخص شد
⚪️
⚪️
پیام نیازمند گلر پرسپولیس که اخیرا مذاکراتش را با این باشگاه برای تمدید قرارداد آغاز کرده طبق شنیده ها به توافقات نسبی دست یافته. طبق شنیده‌ها قرارداد جدید نیازمند با پرسپولیس 2 ساله خواهد بود و گلر فعلی سرخپوشان قرار است دو فصل دیگر نیز در جمع پرسپولیسی‌ها باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140723" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140722" target="_blank">📅 23:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJby9p1HSSaHbhAk2taaF9SH82y6eCsQmcTKSR2TgCgXS77Ami1uUEvU5Sf8Rp5EnPKHSoiOaD0p3YuQOTVpNPcf2KJoSW6z65bjC7FrlDx2MlwM1DwooWT4VdsQ9xVEcvapepS-qiXJFVCfSEb1_bS_cfe4dDnTWnUNoovabBf_mP_mUQHdaq17LsuejqVr0cEy2AhINYpEdiB40VBbgwoevL4m9czpKh46zUOc05qUif0ikZ8uwCGRATvUan66mk4yA1_0SX4E9zyk4-9VbPg2gkB5mHdzen-lf5SQ0N-iMmJ9VYI3zM6IvblLA1vTBDKRo8ihNe0VYOO8qGm5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
قرارداد ۱۳۶۵ میلیاردی پرسپولیس برای تبلیغات البسه
✔️
✔️
باشگاه پرسپولیس قراردادی به مبلغ ۱۳۶۵ میلیارد تومان برای تبلیغات بر روی البسه تیم‌های خود شامل بزرگسالان، رده‌های پایه و بانوان منعقد کرد.
✔️
✔️
این قرارداد برای فصل جاری جهت اطلاع عموم بر روی سایت کدال…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140721" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z04aOE82aRO85-mCuepe-48W7VlU_SoK05yj9jqP8lWLh2OBDYDiPbxCQzTgGFA_5MPvjtHWGk7cFbdBwcPUmWvBjSrU1UvWGViJq-OFgXhcTtVrMt3IBUBqq5kxRC6an9uqcYO0jFELYeoMeSoEd-G2Cr-vu24zWHhUw5ZADhWK5i3EUAjZLMAvVTpyn_XjBXXUTXjyEsyZzNvWSQYQ3W2_nshfMxbT7BmFJ-mWeq_X3H3Q2KBe1rZsCe-7hH5qQ7KUEFWP86FAxP6xyBfdHTIRjZGrPQQ1S0mlCFuYGcHBpqPcUDEJClBhCIX8ChGO1NpUa4hEppV9I9ryLXDBeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اگه پیام نیازمند نبود، فاجعه بازی انگلیس تکرار میشد؛ تفاوت دروازبان درجه یک با دروازبان معمولی اینجور جاها معلوم میشه
❤️
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140720" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140719">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140719" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140718">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=mxoipG0QKASQx1LUyNuO1RaHNpSwp9ZJW_EoeK8HmEgV0YVG5yD4CKZhO45pYInL-30a1Rrgtdqs7wLgN7Jiwp4hHk9FsVG3djTyXA6WzOuDACUVgY8gLDUA_NTFtCkrw740HhdwF2A9FyBe107MG5QL_7xYWv3JdWmV9iBvwX8A5ZhQF5XuruNSeSJqOKLnvGcFDIG_4Bl8jjPw7n34JWZfL92Bv9T3Wx9EyZlb-0APqPsRnDJUmVXbudKnJy6oYzVOOnmTUp49ectge9ydIji1ypZ4MLkLtWYOhfms4mYi0MIqk8xCFXqRzxlqjnIjwYqmUB9F8BAUeMc3zcQazQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=mxoipG0QKASQx1LUyNuO1RaHNpSwp9ZJW_EoeK8HmEgV0YVG5yD4CKZhO45pYInL-30a1Rrgtdqs7wLgN7Jiwp4hHk9FsVG3djTyXA6WzOuDACUVgY8gLDUA_NTFtCkrw740HhdwF2A9FyBe107MG5QL_7xYWv3JdWmV9iBvwX8A5ZhQF5XuruNSeSJqOKLnvGcFDIG_4Bl8jjPw7n34JWZfL92Bv9T3Wx9EyZlb-0APqPsRnDJUmVXbudKnJy6oYzVOOnmTUp49ectge9ydIji1ypZ4MLkLtWYOhfms4mYi0MIqk8xCFXqRzxlqjnIjwYqmUB9F8BAUeMc3zcQazQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درگیری شدید در بازی رده نوجوانان لیگ تهران میان تیم‌های کیسه و شاهین!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140718" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
پرسپولیس هنوز هیچ توافق یا مذاکره‌ای با اندونگ انجام نداده/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140717" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140716">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
پایان  بازی روسیه 2 _ 0 ایران
✔️
✔️
یک نمایش ناامید کننده دیگر از تیم ملی/ با «مدل بازی متفاوت» هم باختیم!
❌
❌
در حالی که امیر قلعه‌نویی وعده داده بود تیم ملی با مدلی متفاوت برابر روسیه به میدان می‌رود اما نمایش تیم ملی همان همیشگی بود؛ نگران کننده و ناامید…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140716" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=LZ08swxDCfWxcPzUE8P7J0QJegd9BtQo8wjDZbllIHLeWJEiZe6YamsJeK_aGZ9-OMUGcUS6eGdq8K2m6I_3vLgP2vS7KpjkzwSFYPvZDzLs9RDwM_eRFDNWN0dM-xcuMrvSblg47Y-v6EsF7eZhC76AwGcei6MEciMYgeUMAYCl3DA7t2QGXU6sYT9QQZyKix4TOxYFPc6AHKRqhU-2NCWcjKxmTYpGjxQRXzapXqrI3_kgG5Sxa4SoP5yhU9r4MEa_r2sVhjTdxgR2m_TwzmR5wJCLg9NjNoGckIe0S_Ie3gNKDn9fj1xBtm_rb9sLo9gsmAMhKZX-3o_g_gmk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=LZ08swxDCfWxcPzUE8P7J0QJegd9BtQo8wjDZbllIHLeWJEiZe6YamsJeK_aGZ9-OMUGcUS6eGdq8K2m6I_3vLgP2vS7KpjkzwSFYPvZDzLs9RDwM_eRFDNWN0dM-xcuMrvSblg47Y-v6EsF7eZhC76AwGcei6MEciMYgeUMAYCl3DA7t2QGXU6sYT9QQZyKix4TOxYFPc6AHKRqhU-2NCWcjKxmTYpGjxQRXzapXqrI3_kgG5Sxa4SoP5yhU9r4MEa_r2sVhjTdxgR2m_TwzmR5wJCLg9NjNoGckIe0S_Ie3gNKDn9fj1xBtm_rb9sLo9gsmAMhKZX-3o_g_gmk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140715" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
سومین سوپر سیو از پیام !!!
⬇
دمت گرم واقعا پیام جون
🔄
یه تنه جلوی آبروریزی رو گرفتی سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140714" target="_blank">📅 21:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVTG678TTo0XI0sGGlmTX8EPQpy9sWWrz4MhfnHseMNqTRflCBn-FIhHyseOMuWmXIYJXELTIwGabmRGi_0xwN03xDro6lcbJ3wADoUF-FLxeifUkWSya6dvhh9MBgLCTG_2iT4fuMz7O5mCvodROXfTIDgQuBa9tezUcQeZRBynfVbCBKxy098FL4kPhUrQue4Z57Q2fdhibEtfDKOr31OUxTzDTJeBh7yMGK1nPG2WQpnHysgjHV37cffxFaC4EcNWqwwrPJx3swcWDBbZo1ppCjV9ZHYj3w05HfacUy9GxXZv2fwHzW32eZMuV10NN5L7iKez2Fs3rzXfMm0oCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140713" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140712" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140711" target="_blank">📅 20:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140710">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140710" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140709">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
کنعانی و علیپور به دیدار مقابل صنعت نفت نخواهند رسید/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140709" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140708">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140708" target="_blank">📅 20:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140707">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=kOZTH8xY4nKl2XozG4XH7Ob2sP59q5ei_qhZpCL3ahOKo2Ypu23r9cYwI5wWCIwDVYUVuySyn2_86Dk0R7PlIzwUVY-Tc6J-gGOYMXV0qkb7cMcdnmP4JCAkilQnZpXdYs03wR0MHaatemRjaGSPTbqzoBNbeS4XWfmPgKmQmvip50OfJtB8Mz3FvBiiFwvoKGbnmL-WXw814cLXafuan-d1hXnVdsjPm2nbBStiH4jvaQ2X7ktvprWr6YaPl5RwcN9hSBkh7qi5QG0BdHAij4eEfNiow-JyLifVJVibfUHiz7XfP-EF1q_PWSpwNxHc4ejDtcX2KzLDOS2sLZMG_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=kOZTH8xY4nKl2XozG4XH7Ob2sP59q5ei_qhZpCL3ahOKo2Ypu23r9cYwI5wWCIwDVYUVuySyn2_86Dk0R7PlIzwUVY-Tc6J-gGOYMXV0qkb7cMcdnmP4JCAkilQnZpXdYs03wR0MHaatemRjaGSPTbqzoBNbeS4XWfmPgKmQmvip50OfJtB8Mz3FvBiiFwvoKGbnmL-WXw814cLXafuan-d1hXnVdsjPm2nbBStiH4jvaQ2X7ktvprWr6YaPl5RwcN9hSBkh7qi5QG0BdHAij4eEfNiow-JyLifVJVibfUHiz7XfP-EF1q_PWSpwNxHc4ejDtcX2KzLDOS2sLZMG_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇷🇺
گل دوم روسیه به ایران توسط گلوین در دقیقه ۳۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140707" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140706">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXQDfKxUqrJbfjmnykd0mIF5O1-t0pfZvk6_Lt2ApPPSLgWgbybWrxoYPLRpTk0rb_82RPhYnUl9h56jCqD7IzzvOE9ULrSLvn2DTAah-h80o7Bt4MAMUajc3mCnMKe06Nmw3dkzIu-htlTLkxh5tyzMoD5x2OwrXGvYa-gNmG14z_SLOW2g1_MGaHWwlaM-cwNd6VdUGUjZwWHa5qWAVBAlOG85uLs5xgMIfprhi7VOCecbnGYWy-ckvlRrH59I5pgF8cdtCXD8jdb_KkKNrLmdLM4IaVxajxWVs6pzbt0bd9wiPWMVd6CzH6rhqKYwTQ5gtkmLhYYaSxeD3OzWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ماتادورها و شطرنجی‌ها امشب در یک دوئل تماشایی!
🔥
⚡️
[
اسپانیا
🇪🇸
🆚
🇭🇷
کرواسی
]
⚽️
اسپانیا بعد از برد ۳-۲ مقابل انگلیس با ۵ برد متوالی وارد این بازی شده و در ۶ تقابل اخیرش با کرواسی ۴ برد داشته است. کرواسی هم در بازی اول ۲-۱ چک را برده، اما مقابل مالکیت و پرس اسپانیا احتمالاً بیشتر به انتقال سریع و ضدحمله تکیه می‌کند. باتوجه به روند دو تیم، سناریوی بازی نزدیک اما پرموقعیت محتمل است؛ اسپانیا از نظر خلق موقعیت دست بالاتر را دارد و یامال می‌تواند مهره کلیدی باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140706" target="_blank">📅 20:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140705">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140705" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=KhjEUIAEBxlo-BQ7Dl9lMe5KijtW6vuHN5YMHf0MvunankoKPfZW0EdnfGwJIGSqRldNM_cbv4HPNzcGgJW9YHAF6DNLHbeYwr04ahp52YHfycJy3ROLch_Zn5zfy58Y_U6QLj1o76TO7RvV1Oxq9LVXW9l2ahyyukAOmCqIMp5I-TIZt01mk4xDvQf3yQwQWHiosKJpRvZtPP77zs3pMHfcRLns9BDDJxgE_WxtTTiwo5V7q0gmNvE19JXblf7v95eFL0g7oFpCZj8xvqwpnTq9nvCDyQkeGD4HSwx63QBSMPhyWXaaeyrqH7_PmeJYuH3YmCo33r-p-hYdi-wQ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=KhjEUIAEBxlo-BQ7Dl9lMe5KijtW6vuHN5YMHf0MvunankoKPfZW0EdnfGwJIGSqRldNM_cbv4HPNzcGgJW9YHAF6DNLHbeYwr04ahp52YHfycJy3ROLch_Zn5zfy58Y_U6QLj1o76TO7RvV1Oxq9LVXW9l2ahyyukAOmCqIMp5I-TIZt01mk4xDvQf3yQwQWHiosKJpRvZtPP77zs3pMHfcRLns9BDDJxgE_WxtTTiwo5V7q0gmNvE19JXblf7v95eFL0g7oFpCZj8xvqwpnTq9nvCDyQkeGD4HSwx63QBSMPhyWXaaeyrqH7_PmeJYuH3YmCo33r-p-hYdi-wQ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140704" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140703">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140703" target="_blank">📅 20:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140702">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=CCtvoFcBYQ8ZD_7Ew4k3g888dxflHKz-NiLEV0aJ53l3b7HbgZfIp8QRSNNPYWwF_57cYaPIIM6BX0RgYjDb5t_VgNqp0KZAILRyuGzAdTwZxcjEo5Q7OVZLE0FXwJLsub0htkYyCIZt8hiJVp3-6_Ie8djH_piEZEY26r541khhWoKxObzNHZw3B_Z7WdeW4WhfFRR6I9_5i48AE3nx9tyn6tgQ4n8pntsc3LVM2VDT6_k3e3PR8Hn4_GrrgKWDFLBlpbEOdnOX97NV-QvKT2v4QRvFldZJ1dCjbQ6XGMWzMRZ0h3qDnb27z12BEDUVexC9wVEJcsWOi46y4pFRJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=CCtvoFcBYQ8ZD_7Ew4k3g888dxflHKz-NiLEV0aJ53l3b7HbgZfIp8QRSNNPYWwF_57cYaPIIM6BX0RgYjDb5t_VgNqp0KZAILRyuGzAdTwZxcjEo5Q7OVZLE0FXwJLsub0htkYyCIZt8hiJVp3-6_Ie8djH_piEZEY26r541khhWoKxObzNHZw3B_Z7WdeW4WhfFRR6I9_5i48AE3nx9tyn6tgQ4n8pntsc3LVM2VDT6_k3e3PR8Hn4_GrrgKWDFLBlpbEOdnOX97NV-QvKT2v4QRvFldZJ1dCjbQ6XGMWzMRZ0h3qDnb27z12BEDUVexC9wVEJcsWOi46y4pFRJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140702" target="_blank">📅 20:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140701">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140701" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140700" target="_blank">📅 19:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=NIRVHe8FSEKF3ehBTeCQb_h1fTuFLATS82-QRdcCu86u_cTtJGaL3EBwtkZu__uxMLWWIvILyA1N6y_ZjT04Mgn8T0iw67oG0yxrGJVmWL_X-2p3PuNEJqN4G7l_NX1pF_g7UU6tFr2e9sABF7izPjJISsFO9F3Nb6cd3oEhLT2wxCMMXMm2v4ZM2qx6E4HgrfKT1uzxuouXaxwZ9g46Ar5CrMp0CAt3Iq5Ef_2nBX7dXKLl5XqOYQ5pc6TARfi5_DYyoT_NNDP9aAghB7Cwhlg-ZhQe_XLgIMsnZGaVCkSIKolNbf_hIxuz4q-fLW25iaqO0IytRErZfNtZGfWaehK-Sg-vFLlE8eE7WhcEWav0RuZdlRnZM215kJAWTu2WmVExNRe52ESTsC9cyO3xWtFn-pHSUS8PCjAcL_d-HDzdjNld866ZPLuEqlVr79koQCtt9C14kr3v9UnbecvgdSH8QfVdX6dG_AdKnDtDuhM3V2u5gT3bCRzcpmRT-EFGPwvDwlejGaa0kp8uSWWm9vQ0riVkQDzPDn-hG6344L3YucbRLy4jokVyXM2bW1WQblK6yTd-Pa72YtcN0uri6eo-uHxcxNJc1P6bf1a3JWw_UwhDYu1s1x9ffJokp8ECrJ_qEn9dsMm97oTdc0FMxENKAFi9XedlG0_5ut8Eq0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=NIRVHe8FSEKF3ehBTeCQb_h1fTuFLATS82-QRdcCu86u_cTtJGaL3EBwtkZu__uxMLWWIvILyA1N6y_ZjT04Mgn8T0iw67oG0yxrGJVmWL_X-2p3PuNEJqN4G7l_NX1pF_g7UU6tFr2e9sABF7izPjJISsFO9F3Nb6cd3oEhLT2wxCMMXMm2v4ZM2qx6E4HgrfKT1uzxuouXaxwZ9g46Ar5CrMp0CAt3Iq5Ef_2nBX7dXKLl5XqOYQ5pc6TARfi5_DYyoT_NNDP9aAghB7Cwhlg-ZhQe_XLgIMsnZGaVCkSIKolNbf_hIxuz4q-fLW25iaqO0IytRErZfNtZGfWaehK-Sg-vFLlE8eE7WhcEWav0RuZdlRnZM215kJAWTu2WmVExNRe52ESTsC9cyO3xWtFn-pHSUS8PCjAcL_d-HDzdjNld866ZPLuEqlVr79koQCtt9C14kr3v9UnbecvgdSH8QfVdX6dG_AdKnDtDuhM3V2u5gT3bCRzcpmRT-EFGPwvDwlejGaa0kp8uSWWm9vQ0riVkQDzPDn-hG6344L3YucbRLy4jokVyXM2bW1WQblK6yTd-Pa72YtcN0uri6eo-uHxcxNJc1P6bf1a3JWw_UwhDYu1s1x9ffJokp8ECrJ_qEn9dsMm97oTdc0FMxENKAFi9XedlG0_5ut8Eq0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
🔴
حضور پیمان حدادی مدیرعامل باشگاه پرسپولیس در ایستگاه 88 خیابان پارک وی به مناسبت روز آتش نشان
🔴
مسئولان پرسپولیس در این دیدار ضمن خدا قوت به پرسنل این ایستگاه آتش نشانی با اهدای گل و یک پیراهن پرسپولیس از این قشر زحمت کش تقدیر کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140699" target="_blank">📅 18:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
ساعت بازی ایران و روسیه تغییر کرد
❌
❌
فدراسیون فوتبال روسیه از تغییر زمان آغاز دیدار دوستانه تیم ملی این کشور برابر ایران خبر داد.
❌
❌
تیم ملی فوتبال روسیه به هدایت والری کارپین، روز ۲۹ سپتامبر (۷ مهر) در شهر کازان به مصاف ایران خواهد رفت. سوت آغاز این مسابقه…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140698" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
🔴
رسمی/ صنعت‌نفت برابر مس پیروز اعلام شد
🔄
🔄
کمیته انضباطی فدراسیون فوتبال در پی عدم حضور تیم مس رفسنجان در دیدار پلی‌آف مقابل صنعت نفت آبادان، نتیجه بازی را ۳ بر صفر به سود صنعت نفت اعلام کرد. با این حکم، صنعت نفت به لیگ برتر صعود و مس رفسنجان به دسته پایین‌تر…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140697" target="_blank">📅 16:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140696" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGidrRLZHLWGw5dCws_bTSmlV-VxKdiy1cscBFhwmUfGe_SyWA6BDsivLAa2ww_WIjdfGO0oGGhKLb0admxHnG9kflOj-tfr8U4aBIxygnp70DTyTmlBd7ZFdBTtOy-ovpULjWYYmDLCmxdroXnktfmEiF8xe6SUQ-sPP_Q-9mnuVtZf0KXPnKWSMGQZrDExag7qAPxvpfU_D-29odxjrscJVjY8mCkHI6h9HVWlIT1qfnTaOOBiXsMOST1Glcr4tNmUogVUb2AUpFr0lUUnFpTjhGpkKLo2D6r_uFVCaSPzZkCJSsAi5C3qHhjJ9QQnGJYqCltXV6x_X1zo6ZhC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری | رسما شرعا جام قهرمانی به کیسه اهدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140695" target="_blank">📅 15:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
افشین قطبی، رسول خطیبی و پیروز قربانی به عنوان سه گزینه نهایی سرمربیگری تیم ملی امید انتخاب شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140694" target="_blank">📅 14:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140693" target="_blank">📅 14:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140692" target="_blank">📅 12:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140691" target="_blank">📅 12:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
❌
تیم ملی والیبال کشورمان با شکست ۳ بر صفر مقابل ژاپن نایب قهرمان آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140690" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXWFVsMwfb2cC7b753ETZ0vH3BNpicL-vJM29YmKqIyXWKER111ASQLhKAP69G4VtorWM5zt2wjDXj-VFTr5AgHUnCwjRWrMPmNtaHU2o4LB2opP8ll0a1GUo6XNmE1KKBqfQz8Mhe9UE8mnZjRKNRratNvDFdOYCqN2JNKNo4Ibv4wOutlT5bOSFxCYVihIjTHdnknQiwAtKDiSLZNIqizhQuvbGouelTT55gp_oGM68mnmCFZEN8vyy79ClxfSvGwM5LJmICbIbIsSVdsVlShSJceIHelSDxQgGDplqK2E3KHff7Aef03jRK9E6eD3Qbx5u7SMYGNg7RbvfK77Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Spain -
❤️
Croatia
⏰
Tonight 22:15
🏟
Ramón Sánchez Pizjuán
⚽️
اسپانیا با ۵ برد متوالی و بدون شکست در ۳۹ بازی اخیر وارد این مسابقه خواهد شد؛ کرواسی هم در بازی نخست ۲ - ۱ چک را برده است. در ۱۱ تقابل قبلی، اسپانیا ۷ برد، ۱ مساوی و ۳ شکست داشته و آخرین بازی دو تیم را هم ۳ - ۰ برده است. مدل آماری پیش‌بینی، شانس برد اسپانیا را ۶۱.۷٪ و کرواسی را ۱۸.۶٪ برآورد کرده و احتمال زیر ۲.۵ گل را ۶۶.۹٪ می‌داند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140689" target="_blank">📅 12:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140688" target="_blank">📅 11:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=aoagBBLImGZ_EhuyKWJrgEMYc0vfW0bjvB2TzyU1T4D0ywBJTb7KsZIh9SDhiPwN3ZveeSD8GQYRAH9PEaZy7SRqk3NeV-a2Clf448jLxXUNzj_ZY1z0MfFC3tr8mMnAohjhtqtiVZ5TEbJmohpLnhZBNS1lQoK81Mb8n-yMTdwV9lXAq70HKNifD5MeRtCye1dSHqknKMiGyh39SUv3qZ3vF0dRGgIuhYdcKkD5QmdWYm6d0Zm67pQMsSRAbnuNlerjf5B6foQl0jQ7lM70awFtc_eZEZMUj8KtlwSSd6ociNDMkRg8GuZQeiE23kXsz7GT8rm1FrBFXhO6AYiB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=aoagBBLImGZ_EhuyKWJrgEMYc0vfW0bjvB2TzyU1T4D0ywBJTb7KsZIh9SDhiPwN3ZveeSD8GQYRAH9PEaZy7SRqk3NeV-a2Clf448jLxXUNzj_ZY1z0MfFC3tr8mMnAohjhtqtiVZ5TEbJmohpLnhZBNS1lQoK81Mb8n-yMTdwV9lXAq70HKNifD5MeRtCye1dSHqknKMiGyh39SUv3qZ3vF0dRGgIuhYdcKkD5QmdWYm6d0Zm67pQMsSRAbnuNlerjf5B6foQl0jQ7lM70awFtc_eZEZMUj8KtlwSSd6ociNDMkRg8GuZQeiE23kXsz7GT8rm1FrBFXhO6AYiB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه دور[سرجمع ۹ماه کسری]، چه سهمیه‌ای گرفت یهو؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140686" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
یک شکایت جدید از استقلال؛ پیکان این بار از ماشاریپوف شکایت کرد
✔️
باشگاه پیکان مدعی است نام ماشاریپوف فصل گذشته از لیست استقلال خارج شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با خودروسازان غیر قانونی بوده…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140685" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
تا نیم‌فصل بیرانوند میتونه به‌ صورت کاملاً قانونی و بدون هیچ مشکلی برای تراکتور بازی کنه!/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140684" target="_blank">📅 10:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
فوووووووری از بیرانوند: چرا فکر میکنید سربازی نمیرم؟ 3 ماه معافیت تاهل دارم، 3 ماه فرزند اول، 3 ماه فرزند دوم و 3 ماه دوری راه تبریز تا خرم‌آباد و یعنی کلا حدود 6 ماه خدمت دارم؛ اصلا شاید نرم تیم نظامی برم پادگان تو تبریز و بالا برجک وایسم موقع مرخصیم میرم…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140683" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
✔️
فوری و رسمی/ دلار 250 هزار تومان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140682" target="_blank">📅 09:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
بازیکن پرسپولیس نیامده جدا شد
🔹
فرزین معامله‌گری که از تیم شمس‌آذر به پرسپولیس پیوسته بود، با توجه به مشمولیت، برای گذراندن خدمت سربازی راهی ملوان بندرانزلی شد.
⏺
پس از پایان دوران خدمت سربازی، وضعیت ادامه همکاری او با سرخپوشان مشخص خواهد شد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140681" target="_blank">📅 09:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140680" target="_blank">📅 09:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN2izoxtMLY3VV1OvuYHFccQPwY2_woP5vZRr--x56KMgWYoH4jkyjCt_oAZB8ZBa-7nha_coSQxgsxGQaMVQ9AMlXjq7qECz0R03rNm3HzqVCUnB_zNC_BXhTuCeXVUxJYVeeqefsVPRm_FWjGAewSFBplmJK2Xs_BJ60trKA1W8_MDTcjolNqDTfJpgGPmZbAUQgXuznh6kKdS9Uimzm50tavuwBz_S3oTQPhmxsxH8pmW-GBHZ90H1vY3cTS-e30N45uCQTU9ygaPJHQbEseJ1fMErOyEai2i3QvA0wfsgRmTtUqVdiaTIhJzG4JB9fMP6d8jeMX8_9qnXXjtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140679" target="_blank">📅 09:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4lhSeUaEhuqTdHDDNrKhbgLDa6KVIwnqdoyDHp7vHoYb1DE2B-tTx3XcOwLn4fj6i39J_VzTCJpQGH4zJg6Ptim1LN9VVP_uXoFZEQ5pCi9QYXmSbM4qDe4qqV4My8vNN8dHb2EuUJhv1mk8IVDL5pH6oDBAJ4LenbGrlMqnmDgcv587VWUwMkW5fItyL0Y51XYhu0_LUluXQl99YER3Q177Go9qtfhU0AUaShLEVkWK1DO8zgf3iTf6CMX0J6iO7tShddyn3XzMGuDdftrVI2hh60C5_sRRnqr_8qsKgY39E-AzYNsnSk8KQdioqbHpCceBEz3wzSym5fKQdI6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Russia -
🇮🇷
Iran
⏰
Tuesday 19:30
🏟
Ak Bars Arena
⚽️
روسیه با فرم هجومی بهتر وارد بازی می‌شود؛ ۳ برد در ۵ دیدار اخیر و میانگین گل‌زنی بالاتر، نقطه قوت اصلی این تیم است. ایران در مقابل تیمی است که در انتقال سریع و ضدحملات می‌تواند خطرساز شود. تقابل‌های اخیر دو تیم هم نزدیک بوده و در ۴ بازی آخر، هرکدام یک برد و ۲ تساوی ثبت کرده‌اند؛ بنابراین انتظار می‌رود بازی درگیرانه و کم‌فاصله دنبال شود و سناریوی گلزنی هر دو تیم دور از ذهن نباشد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140678" target="_blank">📅 01:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال: تراکتور، پرسپولیس و سپاهان مخالفت‌هایی با قهرمانی استقلال دارند
✔️
✔️
اینکه ما از الان مخالف قهرمانی استقلال هستیم، اشتباه است اما قطعا مخالفت‌هایی در مورد قهرمانی استقلال خواهد بود چرا که سپاهان، تراکتور و پرسپولیس…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140677" target="_blank">📅 00:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🔴
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه کیسه، قبل از اردوی ترکیه تیم ملی بزرگسالان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140676" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140675" target="_blank">📅 00:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=g8q_ktO2i83OsT49VMV2YMYeWoY9PXU_84LZfHs5VbywVQhKUJvjY358v2mo1JN3qvdq-QzkRVH-u4RRPjCQ8Hpi7vb8-Bp5Nuklt8jzds4QFEVoDrCJd8b76cCz80AQQbaO5yZVCdBwnUDY0KtMuWuuRbOZb1g2iIYbksmSlZiEaKnbzDBzGbEY6bM6wDoEU7e7oKqh79oJEvnZZPgqwttW2X2q-sy7LvldwJ38OOI40oZlEQyEc7k303S4ZHXBetT9x57XeTOp-jFDF4AMZDS-mEIN35on8KcSTrRpsVCm-VXcA6y5xktqrXCWSAsMWfci2772NAB-l0zgnExv5j9C-AXRB_-ibAIdBG2L2_wR8DT5eRQA4kiqjLsDrNGmdUNFdP4jRvo3SPwqqUBsZMdEfWgU38Q5EJaZCHx95pfH40RLpr0w7pVrQbCfzaSTe9JA9DOzljLeK0tJxJWGnLRViEeiJth2XnYF6U5RWmZmyOWTHLzUEScitOwhRFWD2ZK4BGkjHdD6Ccf9IZ7c4_ZDMCEWh-Zf7HdD2xZd02zy8-inXrbYUESAidaano62xIjh8NEcngWk2lb2Wh4rtrx9ZksAcA0abmnQZFbwMNMg2Ne1eokcdBoQxzzV3O_wkRN6VI4MH98M7zZ5nd65WA8XUxqUi4KHmQreVK_X2qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=g8q_ktO2i83OsT49VMV2YMYeWoY9PXU_84LZfHs5VbywVQhKUJvjY358v2mo1JN3qvdq-QzkRVH-u4RRPjCQ8Hpi7vb8-Bp5Nuklt8jzds4QFEVoDrCJd8b76cCz80AQQbaO5yZVCdBwnUDY0KtMuWuuRbOZb1g2iIYbksmSlZiEaKnbzDBzGbEY6bM6wDoEU7e7oKqh79oJEvnZZPgqwttW2X2q-sy7LvldwJ38OOI40oZlEQyEc7k303S4ZHXBetT9x57XeTOp-jFDF4AMZDS-mEIN35on8KcSTrRpsVCm-VXcA6y5xktqrXCWSAsMWfci2772NAB-l0zgnExv5j9C-AXRB_-ibAIdBG2L2_wR8DT5eRQA4kiqjLsDrNGmdUNFdP4jRvo3SPwqqUBsZMdEfWgU38Q5EJaZCHx95pfH40RLpr0w7pVrQbCfzaSTe9JA9DOzljLeK0tJxJWGnLRViEeiJth2XnYF6U5RWmZmyOWTHLzUEScitOwhRFWD2ZK4BGkjHdD6Ccf9IZ7c4_ZDMCEWh-Zf7HdD2xZd02zy8-inXrbYUESAidaano62xIjh8NEcngWk2lb2Wh4rtrx9ZksAcA0abmnQZFbwMNMg2Ne1eokcdBoQxzzV3O_wkRN6VI4MH98M7zZ5nd65WA8XUxqUi4KHmQreVK_X2qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
🔄
🔄
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140674" target="_blank">📅 00:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140673" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140672" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmduXC_KjtOKpru1TmCDtfoXjU-6iLXzeHZ8skg8on60RURtYMd7yrURuSLy-6chv-9q6AhF7Z6_jKiVskWWvdXSlp70AGKYDc2zlz4lvnz7_rxQWhdZlRXY-Zmun-9U3E8GhlSKuZ7mnH3509L5PquVBfpyiU-V7YDbDfSeerSM7JMTqE0gWZhpyy7P21Y744EQwJk3OZp6oZbO6b_1ii0vzGyvwGokqPM8YWQKoHZqllXc9rsU_EsMnes7Gtz7nbP6QUhqykgVNFEafoFGes2Hs-SbiepJRtJlPpyTH68RlFy1m_TzJRrIoBPqqIhi2f4Ig8TmfmD9qfO_CiM1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
وارد فیفادی شدیم، شخصا از فیفادی نفرت دارم چون پرسپولیس لذت دیگه‌ای داره برام
❌
میشد که قبل از فیفادی یک برد دیگه و یک بازی دلچسب دیگه از تیم محبوبمون ببینیم اما کارشکنی‌ها جلوی برد دلچسبمون رو گرفت..
❌
دم تک تک بازیکنامون و کادر فنیمون گرم که کاری کردن وقتی بازی پرسپولیس رو نمیبینیم بجای اینکه خوشحال باشیم، حسرت میخوریم که چرا چرا چرا یه مدت نمیتونیم بازی تیم خوب و جنگنده‌مون رو ببینیم..
❌
بعد از فیفادی میبینمت پرسپولیسم؛ منتظر بازیهای هجومی‌تر از قبل و پر‌گل تر از قبل هستیم آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140671" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140670" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140669" target="_blank">📅 23:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
علیرضا بیرانوند دروازه‌بان تراکتور : من نردبونم و همه دارن ازم بالا میرن کینه‌ای که بعضیا از من دارن کینه نیست علاقه و دوست داشتنه.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140668" target="_blank">📅 23:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
#فوری
🗣
خبرگزاری مهر : تعویق خدمت شامل بیرانوند نشده و او رسما از 1 مهر سرباز غایب محسوب شده و هر گونه بازی کردن او غیرمجاز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140667" target="_blank">📅 23:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140666" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140665" target="_blank">📅 23:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=WOFh58s5GQs03famRsw4xyVyhq3Iok1YsscSLd43FUhkRuULJw0UFknCbq_75nzfQcQ0l9mxkCrPhGChChG1SMP-oXqyOgA0VwAc7dwHeoSCNAV90YuCnXhXkVK9bVmg8Vm13egdec44-RcQz7t1SvZtQiVjDo3xHkN7xWYHm4Hb0QN-A-ILYZGZpS3dEyWS-_SaNnAi13YDCrqmG-Kj-rhQ1DG9Fo7dBOoVo4Wu4zXplzgER74naoXApAp8dnPbKPOhdtAM9jbd5x8lS5WbgaED5PcUprHmFCs6C09wG9MF-HW42fwFHC1915lPKv-sDrBp8dmnvZXVa0M16POA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=WOFh58s5GQs03famRsw4xyVyhq3Iok1YsscSLd43FUhkRuULJw0UFknCbq_75nzfQcQ0l9mxkCrPhGChChG1SMP-oXqyOgA0VwAc7dwHeoSCNAV90YuCnXhXkVK9bVmg8Vm13egdec44-RcQz7t1SvZtQiVjDo3xHkN7xWYHm4Hb0QN-A-ILYZGZpS3dEyWS-_SaNnAi13YDCrqmG-Kj-rhQ1DG9Fo7dBOoVo4Wu4zXplzgER74naoXApAp8dnPbKPOhdtAM9jbd5x8lS5WbgaED5PcUprHmFCs6C09wG9MF-HW42fwFHC1915lPKv-sDrBp8dmnvZXVa0M16POA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140664" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140663">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
یاسر اسانی: ابوالفضل جلالی بهم زنگ زد گفت نمیایی پرسپولیس؟ گفتم حاضرم از ایران برم ولی به پرسپولیس نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140663" target="_blank">📅 23:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140662">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه: پرسپولیس به سند جدیدی تو پرونده یاسر آسانی دست پیدا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140662" target="_blank">📅 23:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140661">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
پوریا لطیفی فر: از بچگی رویای پوشیدن پیراهن پرسپولیس را داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140661" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140660">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140660" target="_blank">📅 22:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
خبرورزشی
❌
❌
باکیچ با وجود عملکرد خوبی که در فصل گذشته داشت، به اون صورت مورد علاقه تارتار واقع نشده و احتمال جداییش کم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140659" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش، دنبال جذب مارکو باکیچ در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140658" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
تسنیم:
📰
جلسه امروز فدراسیون که به گفته رسانه‌ها برای تصمیم‌گیری برای جام فصل پیش بوده ؛ اصلا راجب به قهرمانی و اهدای جام به استقلال نبود و این موضوع در جلسات بعدی فدراسیون مطرح میشه!!
❌
احتمالا درباره مربی تیم ملی امید باشه
👀
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140657" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgHCiDZBM8mSFLRgD9ebLA16y_-eFTAxsnUAn59KYU034XB0_JE39hFnDLbxGvSLXlrgjsh1aMNh69GCjdCkiknY5KmL5yweaKxVcxEkOU7BPZBWaHn9R9yzbNFnOiZtW8vATaIpY0fnyrrA43qHp-XilZYRNErZK-IoF_O4u9V8dcb8Uz2lIdSFDUixMr0v1enQ7DeQ0Ij7SwocvzKsv2_USzEWflTrO_QQvS4XQ6vhXo_vVlDlBmnVDiZNLqgbsZcKvMYWoIexuCk-DC_W2TOON2gNINZOb1S-IHbElhApizKPBsoE6m5nLoEUJsMacmsQBgJB6-ULC8hkl7Vo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Belgium -
🇫🇷
France
⏰
Tonight 22:15
🏟
Roi Baudouin
🇪🇺
بلژیک در بازی اول با ۲ گل و ۱۹ شوت ایتالیا را برد، درحالی‌که فرانسه با برد ۱ - ۰ مقابل ترکیه وارد این مسابقه می‌شود. فرانسه در ۵ تقابل اخیر ۵ برد داشته و در این ۵ بازی فقط ۲ گل دریافت کرده؛ ضمن اینکه امشب بدون امباپه بازی می‌کند. از نظر روند، بلژیک در خانه ۶ بازی شکست‌ناپذیر است؛ بنابراین انتظار بازی نزدیک و کم‌فاصله از نظر موقعیت‌ها می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140656" target="_blank">📅 21:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140655" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
