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
<img src="https://cdn4.telesco.pe/file/FWiGQUMtIa772MhHLQZTCv0gxTshBD1sMXATaDcI6xj2LF3qaxrB-tD9tlSpOzR5pXOY1r6O3xm4zPg5htS6PUYDVYLSXz4CV2IvwbMXaxzudx1SKSeYuwphiIxm1wuRWHZekaVut6S78Vi4lovoMYIMylbzqjAjLd8cE8a8QNKa3kdekzQL-ysvGbY23mdGleS1-6CAHIv-Ye5z9dLbuOnym_CgM1UoRaP-9-UGBGnGx0myjahlgU74CL81UqPy_wKyZk7ifer7WnlraxcaWnQD8SnL0b2eFf6g2PMSEJ7aFotfRdR7USNmt4yeW3FhZef3BkRr8S6WYVORtrTHjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 17:52:09</div>
<hr>

<div class="tg-post" id="msg-135501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
سرلک بخشی از قرارداد فصل بعدش رو دریافت میکنه و بعد جدا میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/135501" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔘
🔘
🔘
باشگاه پرسپولیس فردا یعنی روز شنبه مذاکرات نهایی و پایانی خود با دانیال ایری و باشگاه نساجی را انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/135500" target="_blank">📅 17:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🔴
🔴
تارتار گفته چون فعلا تو جذب هیچ وینگری موفق نبودید اجازه نمیدم بجز عالیشاه وینگر دیگه ای جدا شه و هروقت جذب کردید میزارم جدا شن
🔴
بدین ترتیب بیفوما و شکاری فعلا با تیم میمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/135499" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
برگام فیروز کریمی شده کارشناس بازی های جام جهانی کانال  gem tv
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/135498" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/135497" target="_blank">📅 16:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4YcU2MPmJGBeI8s2W7zn4IF4VXNb6lp8_4tFHgYlUYQjYTCDsttVTdWovZHOoagmGK0d3OxnZXMJVZHlBtlByT_DOU-0LE8quBJ4Da1w9Ovk_D_e01QdfiRIUn6WHXPuHntdFqZeedRnRpJLxQ9SF3nWEWZsNainR70n795lfkOs6OlnYv0-uaymNYXsohFLVjArIXslHq7mPqXecA4ccQy4Y_dzZ742HdzYJ8APaX1aDN-Sh4ja-d32OLj83bD3AtCdclPkjE2iTg251EwOHWy5DGlkj8F5u9IafzVTksK2y_M68sIeDyxCzpk9sdrSJbhe4ErIYeN7vPxEYqjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری؛ شنیده ها: رضا شکاری از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/135496" target="_blank">📅 15:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dOcJf5RKXQlu_Zye0iTrCm9jKYzeroNXXeYbSesva640ByVLIKsFIqVYfjV3drQyy9ZjIC6oZ-z3VAnxQxHKme62uCft21VvsiATLe8PgtSkNryArX8u78LVKm9QMRh-eBOR7GzCNq2aBMbKfSSmciOU9rImUr588jGBS-Exi1cp4yBcFt1qGPXkbRadZ_X5h_S9kdUvNO8NV3Ae2ySFeWsquaZStjYpQRitrPcc-KybYWT46pW9sTubPmKK7cuY7-an5cDfqZhgEFgmddOVNY4zoGlW-0mbE2fGMR2m-rCodl9rO4qvelmiJhQJRT5OmEnnTVnDCLbuVup9POLaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/135495" target="_blank">📅 15:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evgkWZzoPbpjQrWbDenluMazucA5fT8RrTSbxs019Ivn0AAg-a8BhHkAk1HkzqjJ3wRNGQfE3yXzFYCt_hN_xmLW0b1m5mlkFKxPhgsnnmCjKsKpjD1Qu0Os1E_G55O8SbV7XuBhf-9nPR_iwhqpMpcn8W4nG8tmXEerkTbBzW-VjD3RGIuFj-vqJT5CHG9odVr4HRPHpJEHJV2NFcD6sKWZfd6HRYsrYrqVBEjzVg5U6GCpJ_da8_k4dAgeHj0f1AKJOaPI8LckU3u6kI6c0ZTUnAev5OA6xr8ZwbNF0v0vjerSR3z65RD1k5FRKeWAzlZi6-NhucfhEu2oY2PJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏅
تفاهم نامه همکاری بین باشگاه پرسپولیس و فدراسیون کشتی توسط پیمان حدادی و علیرضا دبیر امضا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/135494" target="_blank">📅 15:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏅
پس از امضای تفاهنامه با باشگاه پرسپولیس؛
🎤
صحبت‌های علیرضا دبیر، رئیس فدراسیون کشتی
❓
دخالتی در قضیه خداداد و پرسپولیس نداشتم
❓
ما فقط معرف بودیم
❓
من نوکری ورزش ایران را میکنم
❓
از ایرانی‌های آمریکا تشکر میکنم
❓
بهترین ایرانی‌های خارج از کشور در آمریکا هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/135492" target="_blank">📅 15:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
🔴
🔴
ورزش سه در خبری اختصاصی مدعی شد استقلال به سپاهان و پرسپولیس هایجک زده و علی نعمتی رو به خدمت گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/135491" target="_blank">📅 14:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
کریم باقری از شنبه یا یکشنبه به تمرینات برمی‌گرده و مشکلی برای حضورش نیست.
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/135490" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس می‌خواهد برای کاپیتان مراسم خداحافظی بگیرد؛
✅
✅
باشگاه در تدارک برگزاری مراسم خداحافظی برای امید عالیشاه است؛ اتفاقی که در سال‌های اخیر برای هیچ بازیکنی رخ نداده و نشان می‌دهد باشگاه قصد دارد با احترام از کاپیتان سابقش تقدیر کند.
❗️
❗️
حالا…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/135489" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/135488" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135487" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/135487" target="_blank">📅 14:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jx2QtNN8wP7YAVlBFmUgW4GjfXmDhYpgOFi9h2rRmAR4J-6cHYLhLWsah5i--19s8Hs5XWgHyyN_S62q6B7Q7F4sc6bfy_2vwRnaxfu1lGj5Z2ezFaSod4ypwE6ThEVyRa9P4aMRmmHw-dWOEicPH9VRPMsZqbCKjuCwhgR47Mspm6RjZBjvP1jlU6D4wVqTUqQfQ1d_FBxZ08M1yk0D5-Lhzp29ziCdl4x8__ZhYFgwXSpabdu1Ztj4fmqMFBMAjomqohXAVai6EwlkVSj3lqSb8F6Vrjj6EZapq7xonollHiWHc35U7ZcsdyTe-BLr9Bc2o3faJm-5P8wHgL36CA.jpg" alt="photo" loading="lazy"/></div>
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
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/135486" target="_blank">📅 14:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6oTK7B5HgY6Rodjvt1XNBnIzrr5jhSBlIZx8AWrUZal2oKWcOKjQGR1LKktxW6ctWzot1nrdb2ol06ghrVEynBsJDPEKANI1A9SS3N_XiDklJIq8xyFuZzEj7qCKLH_FJ3GwJFo3IwNeykk5gtyPkc9Buky5PLb7aAmLpxG-c9SYv4a7Fuba2ip_iw0i--QTVgzsr0JsBhEY1SCsvRZPJ2Lzuf6_yMMyqtKiML4BQ40n8seNyxRNjOd_mIySo2jih_maHjRNK_Zrv0jBNgpkla1zlpU90V5VVeAEKeXWy3lUzVga30-ehHk1fQ5PeBYZruBRh52pTbyZO8aHYJu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
میعاد قاسمی، آنالیزور و دستیار تارتار تو گل گهر سیرجان به عنوان آنالیزور جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/135484" target="_blank">📅 13:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
❗️
باشگاه امروز به شکل رسمی نامه زد تا پورعلی گنجی، عالیشاه و سرلک در این تمرین شرکت نکنند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/135483" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO-IrMqf8gQ5PUoumFQ6bStP96piY_0hjoz3iw6FOI5sHsT84se4ZSsv8A8Ro2EiSrD64r0ZIR0yuvxM_tvNKGd7hOPiK4YfXJ9eDXcxcmcxN_f3uTWv5kcfUx6ojUpSZUmNnHlV7qny-FDA8w_1AIG8-M60MCSW1chC5bYWUxUlbfjaPS4_8nNfNfe55Imq9ajYum_LWhcFgD6k9Q6xxTp0pCzhCIuH-KKo2rSema9T7M4a4iTieHVCgZnnzQpWX_WXe7P1x1wITFJTfoIB9FhVs_UTaTeIrBBf-xEeR4X5do_dXzq47XUF4wYQiBYofburS82FzAk8fk82ga0jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/135482" target="_blank">📅 13:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135481">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/135481" target="_blank">📅 13:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/135480" target="_blank">📅 13:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
فووووووووووووووووووری
📊
محمدمهدی زارع در تلاش است تا رضایت نامه اش را برای پیوستن به پرسپولیس بگیرد /فرهیخگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135479" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
فوووووری / ایسنا
🔴
پیشنهاد پرسپولیس به اسلامی و کوشکی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135478" target="_blank">📅 11:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
📊
علیرضا کوشکی وینگر استقلال تهران در لیست خرید پرسپولیس نیست/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/135477" target="_blank">📅 11:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxjU944p3MkoXlqJGuGA4B1jUabgN84ruOTcTlsM7qNKTPeN8u1Wm5j6kWeixTFKZI0rQfqDWR4STk-BA8VWBynVD0PegYibGJZziPBcdo7My2g_Cq_4NMT3GxFWtbYLmkaG1JLsOH-XHz6jywv7vJW-ZaLzfVvrrSImuPNKGC_zISg3U-w9YCTMDQgBlV-XxgWtvygTg7PZdvU4BK3h0zxpoIf7uTpFzLqvQsnrO16SODwPIdq75B49TTQPqoZ2Yo7ws2RJNII5e4rP9O5MR2zBd6j4WQivzSOspNnptEkhdK2p-HJ3gMtyKXcW4Oc3vAU7xaO8j9TSFHbiCahiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135476" target="_blank">📅 11:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
پرسپولیس میخواد برای جذب احمد نور به کلبا نامه بزنه/فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135475" target="_blank">📅 11:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💢
مدیران باشگاه‌ موفق شدند با محمد مهدی زارع به توافق شخصی برسند و قرار است مذاکرات با باشگاه اخمت گروژونی انجام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135474" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135473" target="_blank">📅 10:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135472" target="_blank">📅 10:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
پرسپولیس؟باز هم نه؛ترابی بازیکن آزاد نیست!
🔴
فرهیختگان: در شرایطی که در روزهای اخیر اخباری منتشر شده که مهدی ترابی بازیکن آزاد است تا دوباره جنجال‌های بازگشتش به پرسپولیس برای چند فصل متوالی تکرار شود، براساس شنیده‌های «فرهیختگان» او یک فصل دیگر با تراکتور…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135471" target="_blank">📅 09:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFDZNhajNyTgtICZd9bwhUaGdncZ01Gx5Wd2q7htPiQXuhSsYyTg0-KkYtbGJZDIWpF6cLoM9rRuFol4eB0hl3OOlWrxzUVJDr3DpA9XQ6SJ6wWOVJyLpo5FOLfqSscYgTanLixXy2MX49RAcAIv7eZBOUwBea4XQiXmUKIhv_wG_upRDnSUOZiYn1SBCKq9Fg0Cmv_5oA0aCHlArAaIxnkhuueciCPZaQ0RimFQSkvqU7Y3TpC-3V3hxqV7XYg0x8oMNmDcUgGplyltmUCfhX5jOGSxB6Kj4-SdEBZHcSfH6eTlGemNljtf6QWnzILZZIXN2tqaCz8SqdubO730Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه پرسپولیس به میلاد محمدی ۴۸ ساعت فرصت داده که برای تمدید قراردادش به باشگاه مراجعه کند در غیر اینصورت باشگاه تصمیم دیگری خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135470" target="_blank">📅 09:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔹
🔹
🔹
شایعات؛ اورونوف فردا میاد ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135469" target="_blank">📅 09:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
ترانسفرمارکت ترابی را بازیکن آزاد اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135468" target="_blank">📅 09:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
پرسپولیس می‌خواد برای عالیشاه مراسم خداحافظی بگیره؛ حالا باید دید خودش این خداحافظی رو قبول می‌کنه یا نه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135467" target="_blank">📅 08:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔘
🔘
به‌عنوان طرفدار پرسپولیس، تنها می‌توانیم بگوییم: مرسی امید، ممنون آقای عالیشاه!
🔘
🔘
تشکر بابت تمام دویدن‌ها، عرق ریختن‌ها، جام‌ها و جنگیدن‌ها، اشک‌ها و لبخندها و تمام خاطرات ریز و درشتی که با تعصب و غیرت، با شهامت و شجاعت برای خودت و ما ساختی. سهم تو در سال‌های…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135466" target="_blank">📅 08:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hki-mo1aFSe0qTtwdd7F-B16Ez-x48KktYMFCab2OFBTAyFTW5EK1Io7mEwddQmyoWrwktYw3QEnj_RabErdNZ1rwusWR5W78PGt2K2-6cloKJUJRBAPHhxi0sQNZGVmlane7f4wRvBDeQVJnmhuJWk2ytCLjfbRldrpVK1tS9pNW0zA9Hk3qDJp-uQxyx7gb3DVy8C4uOQejkg3ioZMrPOanMEFuPM84P5_cM3HH7FDSHERiQPqXSAQgy0LDHXuPt8D-z60JQGmOFL9nM21wRLvZsnBFKxLeFS0tCrHfFasPOPJFUMh-SezcC_q9oiNySHGE-ERCKqnEKm9EOa8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
صبحتون بخیر ارتش سرخ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/135465" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135464" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135464" target="_blank">📅 02:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4_oa7GVbWrFiIAGv0LJ5kzJRScKpBozYCNdqg4bEqfNwO-alFA_Gjiq5MPOIreveBqjgRx5F1p8Uq_6-OoaLgNfVE147a3uuExCEyPnrvB0SJaRL90CJMLYU0lJFG_EzMCLMj1V0_KJJ5nBssJhEqHr3j-fXh3204kMi0Wqgax3dHDVIOd4428FzpUPokTNYI9edN1d0oC5V5H0jSXxnidMnQ0ArOLV2LO_4-jOp2rxxCEku2zy0-VsTRxfaLv4rgtBMpevicQr_WHfpAl3CUo598bDKcO5M1lbr7lRw4N_WARCbp6YpdCGndEAHKUJ5JL2_QPH8PohqAm0Fdbl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135463" target="_blank">📅 02:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
🇳🇿
محمدرضا احمدی به عنوان گزارشگر دیدار ایران و نیوزلند انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135462" target="_blank">📅 01:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhIf6wgr4-IqTANS0EiS6CM1PWPRaVVcCaIyWaNXyxkkEstG8td6BNoYcV0FBDrrHg6Izh1FrkULu87dz8qvuS0uUit8NUErPMG1JnBK9GxUn_8PrAPpJGfGfcCcFtXobF7qN4Mj-9b6_QpIFd3UTFOJHuaotkEsh2Dl14qGFrxXoytDXWD_noXH09YyEamQ9TQukMv2qYAPApaw7-mWBg04Q2VIOB4zHh0PJyh3WgQhJT5b2oGWVyAytuXQH01DRcb624xPaP_QxeMprpwsQdWboqTBdzLzltaR0kQFz0_jNTfXyp3HJpRzqQgec-qKIaMh_SGk5VelnM8AvEJ3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
میلاد محمدی هم با اعلام ترانسفرمارکت بازیکن آزاد اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135461" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💢
#شایعات
🔴
میلاد سرلک با عقدی یکساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135460" target="_blank">📅 01:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
بعد از منیر حالا اندونگ هم رسماً از استقلال جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/135459" target="_blank">📅 00:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135458" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5LQFYYekhnctpU99sVatgbZl_uQ58M4Gd57d5hGgwVnXxFmzh5_wLPMyQz__SR0RMr3v_9oFVZoVCV6oV_SYSxJatRp3J54He_tOL9yAFRuHlyDEBFNk1AmG12LMDw0wOUR9Q4h5o6FHj1jPXtiJCgtRJhQP5NDys6rlm9NrmwWdILLxMi95QQ3tx3OfgtlFP_QNjmMT882hH-aBi2sLmR7M6GYv_uGeIeIEaPW0Q7jUafHucjAIjZQXEvsjX0FoLLbKjvVxjcp1swJNtR7NinvGCNxMkBBDZmsXfs64rHi6y7uwPNwmP_ou_8jOFAF0HSRMP1pdKQdVPL6SVTHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/135457" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D87qTw8SDbCW4gVBtpSlzv5Jk0mBngTja_OrS4OyUVVw-r2c8YtEKf0blTrYEX-XkYXXdJ8_m73nmL2wgBPRpJEbb1BvdmuFhYG4EfWRlL4IcAMQ7EEiNXTNN64ylmktF5VDmXQtvJxumG-UH7TWqA7ecCP6OdaOBloJ2sIPpUTB-9TPrCOAuOdwQAx5xs3OeoilvZRHtR4Cqkw4kzqmxHG4NPdN392jjIWVUx_Q1eDAjHG1ugmwGxMQg5MoGwjBDv9fPe8n61qTpA6rQ1uKHmGW9FA3u8lNO6v8b2JALXXS0AuKAsWTXOdC7GwM8bGBvpURKUgpdQ1oh3IexdrTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بترس پرسپولیسی؛ رضا اسدی از گل‌گهر جدا شد!
😐
پ.ن نیاد جای علیپور صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/135455" target="_blank">📅 23:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135454" target="_blank">📅 23:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjdTMIE63oWXUfy9r4Xc18zIDLZiM0qxte5jt1REhnY_HCLQOcrcb3wcASRw2-UR0vtVwXLicswldeAemblz88qisV9ZK5qMBNbrg8x63KzISwHAx4eiRxTjP2lT_C1SHObFyIwk-k1cwCXcdAIJIUOwsnncEnColTtnaRICzB2sF8lCvDNLnevq_x1Ztjg-eWYIOC2VtqcSMvFpRQg-tm-n1-r688GAxk0zqBikK55-Hd2XOqtnmPkn2y1jmoJ-KxGr-gKE_1dMzlSucwYvfDfFfcBQ_esbpjAOQBz5Og1KcvvQ39RqFh3wKXBIbFei8xxZJEkPzCQnIPpPozQ4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135452" target="_blank">📅 23:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
خرید پنجم پرسپولیس نهایی شد
🚨
با اعلام سید مهدی رحمتی سرمربی گل گهر سیرجان پویا پورعلی از این تیم جدا شده و فصل آینده در این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135451" target="_blank">📅 23:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
خرید پنجم پرسپولیس نهایی شد
🚨
با اعلام سید مهدی رحمتی سرمربی گل گهر سیرجان پویا پورعلی از این تیم جدا شده و فصل آینده در این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135450" target="_blank">📅 23:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
اسپانیا گل اول و به بلژیک زده و اسپانیا همچنان تو کل این جام جهانی گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135449" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
برنامه کامل مرحله ¼نهایی جام‌جهانی
😀
فرانسه
🆚
مراکش
😀
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
😀
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
😀
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135448" target="_blank">📅 23:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCtrGmaTvJJP59hxSiH26vM8AmywdOaa6iX7qwG4u_Tmqqei8FtspEXIYdTp9PGGuK_A7sBdi5SNNnGmgtcIYfwB9EaYZXlY6JD4mFnoG6fsJlN9j8IPSZPEHippQ9LTJpuypWQOC_2s3O6lxQdmxwdM1JZOPdKKzg5qMjJ8VuJ5F9gEBYBI9Uko1Hz4GKp1h62j2s3S_2738KvWfxFE1ax0PcEGTQkQwsrcCe1jOtK3toLpocKjQ8y0B8nbkzOgJ6KMrcNmCCXhQa_5qOi_gOnsDhknsp5saYCd3kaSfu1A8Pav8ZlXyKLw2o1GVs32L8j9SSJN7YVV2ymakQFFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مازیار حسینی در راه هیئت‌مدیره پرسپولیس؟
❌
شنیده می‌شود مازیار حسینی، که سابقه مدیریت در شهرداری تهران و بنیاد مستضعفان را دارد یکی از گزینه‌های ورود به هیئت‌مدیره پرسپولیس است و حتی ممکن است رئیس هیئت‌مدیره پرسپولیس شود.البته فعلا چیزی قطعی نشده و در حد گملنه زنی است/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135447" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
قبل از آمدن تارتار با پرسپولیس بسته بودم،خوشحالی تیکدری، پسر حاج‌مهدی، از انتخاب او به عنوان سرمربی سرخ‌ها!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135446" target="_blank">📅 22:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
تمام ملی پوشان بعد از جام جهانی و مرخصی از فردا باید خودشون و به کادر فنی جدید معرفی کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135445" target="_blank">📅 22:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
اگر اتفاق خاصی رخ ندهد و پیشنهاد بالاتری نرسد؛ دانیال ایری مدافع ملی پوش نساجی مازندران به پرسپولیس خواهد پیوست
🚨
🚨
توافقات نهایی شد و میلغ رضایت نامه مورد قبول هیات مدیره قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135444" target="_blank">📅 22:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyAKVfeRGa37PVWMIbSnc1SKnYnklVf__V0e7DN_s-OKh69pVHcEoq85o0h987yzIxyw4vrHb3-gaJyatCQ0o2QnTL_bRRxZ-rSaDRXW1iTnocCgWOvs9ZxyknAHvV09GiWrdp1ZkL464GEQkzC4M4nFfLb8eSqOCLEAj5D2J4qpemL9ZFSHvOu4dtd7gPDLkI7qg6L-qs26NOLjcmcGU2SFjxv8PA_7sbX8chtBkfl7-MXIb0hH0vOAqwDOPVP-ePF68FHynPXWY8ObmPxGpHNHsT34nfjvMQ7saoabqURE2xb4JYDZNkD1hDO6kXpYf8uTQtGfraUNmZAyK4wVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا گو، مربی یونانی تیم، در تمرین امروز پرسپولیس شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135443" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135442" target="_blank">📅 22:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
❗️
مهدی تارتار از آمادگی وحید امیری در تمرینات رضایت داشته. احتمالا وحید امیری برای فصل بعد به عنوان ی بازیکن تعویضی و برای مدیریت رختکن و...دوباره به پرسپولیس برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135441" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b6deee68.mp4?token=jKnQAzSAjDHA3Pfzf11slOLIU3moNYE6UiM2tWxKml1mBKKzS2QhQAaTp8B1RJTo_c6-2DqwcWuKb4CqFmfQbghBK2SqIkuppi2bhJpnHpxHlpkDChXmTJsf_tYEQxEvT1z-MTw4MoFI4PSwwMjFr_qpOxTvhRfwQGOhlly6-Y5x8TKz3_QGFoLWivxQX3DAFbnRPF-KrLq8JSuIKuj6oWA8ZU-4DJECZcnuYYVTvPq5Du_l0hmVQNaldxRNJL1Fp9MOtjMWv96V6-KNq7vw1b5g91Q4s0wSw2VDK3NqWvz5G59z7TvkcvPawbeJtYPuazVgDNhiCFytpSuad8YkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b6deee68.mp4?token=jKnQAzSAjDHA3Pfzf11slOLIU3moNYE6UiM2tWxKml1mBKKzS2QhQAaTp8B1RJTo_c6-2DqwcWuKb4CqFmfQbghBK2SqIkuppi2bhJpnHpxHlpkDChXmTJsf_tYEQxEvT1z-MTw4MoFI4PSwwMjFr_qpOxTvhRfwQGOhlly6-Y5x8TKz3_QGFoLWivxQX3DAFbnRPF-KrLq8JSuIKuj6oWA8ZU-4DJECZcnuYYVTvPq5Du_l0hmVQNaldxRNJL1Fp9MOtjMWv96V6-KNq7vw1b5g91Q4s0wSw2VDK3NqWvz5G59z7TvkcvPawbeJtYPuazVgDNhiCFytpSuad8YkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
قبل از آمدن تارتار با پرسپولیس بسته بودم،خوشحالی تیکدری، پسر حاج‌مهدی، از انتخاب او به عنوان سرمربی سرخ‌ها!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135440" target="_blank">📅 22:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efabe672d.mp4?token=TTfex3yVuyfVqjOPzSpUsruc2--yxmW7hQF19M5-S_Oj5iZFbhiayLDQm1873yPONdyA0ufYpMbYtS7K412hSXquS5NXt_PHRkz8IzFuxTPlFLBa2iFX_dNDUpn3Opa2ZS8vkt6tpN3_YdIPscTMMWy27nnKM_diZ_5FcMPONWlVClIYnrgUv1zM4-4y3Pp8uvdkwKv7pOljTQVeswEJsPPFmtMafMkMNdPoUYWUdLV4NZCc8Kbz74qpvETE2-vv9AwLIDZEKVy8LZ4qPeByCsqqJdkGOoaIxpMypzoO6BBbWp2Ky9LPzr_4yeGTPHiKv_sGDJsHlnvlty6QUWOtUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efabe672d.mp4?token=TTfex3yVuyfVqjOPzSpUsruc2--yxmW7hQF19M5-S_Oj5iZFbhiayLDQm1873yPONdyA0ufYpMbYtS7K412hSXquS5NXt_PHRkz8IzFuxTPlFLBa2iFX_dNDUpn3Opa2ZS8vkt6tpN3_YdIPscTMMWy27nnKM_diZ_5FcMPONWlVClIYnrgUv1zM4-4y3Pp8uvdkwKv7pOljTQVeswEJsPPFmtMafMkMNdPoUYWUdLV4NZCc8Kbz74qpvETE2-vv9AwLIDZEKVy8LZ4qPeByCsqqJdkGOoaIxpMypzoO6BBbWp2Ky9LPzr_4yeGTPHiKv_sGDJsHlnvlty6QUWOtUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
قسمت بود به استقلال نروم
🔴
روایت مهدی تیکدری از منتفی‌شدن انتقال ۲ سال قبلش به استقلال؛ آماده شده بودم که دیگر هیچ‌وقت نتوانم برای تیم محبوبم بازی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135439" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135438" target="_blank">📅 22:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135437">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135437" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135436">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMVBQvxZt8mXRVNopoDMKY0fiIO4iuI52b_fku1sRkmb2bYUVwVVyxXUt6KoC1MjR5mUgT-kkIa75UriZQcW5XR_XK9uc84c_KlQuvjmULB9TJACDvWh6-i0oZ8oCGW8hW8p4HJDfTJQZ7oZqDlNsYOdqtiXtpBf3Gt9wGLWDPsUkex9UnrcW2JtU3BXJpBFBX0lyqCIBzwk1MTKrKScjX5SfIZmZfLUBs7kG_VHmgf8-g0c5yBKjxBduwK6kAdU5HmEvy7yzRC3qA2Y_JtixTp2_S56ImcRZ0xGPP3cH96jjf1W8M-Ax28gR3dSfsxCghBASZT9UL7LFu4dX19l5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گزارش تصویری از تمرین امروز پرسپولیس و اولین حضور ابوالفضل جلالی در تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135436" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135435">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
احتمال همکاری امیری با پرسپولیس برای فصل بعد چه به عنوان بازیکن و چه به عنوان عضو کادرفنی بالاست/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135435" target="_blank">📅 22:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135434">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
فرم های بزرگ ترین جام جهانی رو از دست ندید...
⚽️
@Tabanii_Mafia
@Tabanii_Mafia
⚽️
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135434" target="_blank">📅 21:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135433">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS0eS_Ff45z5IpTxIT4tct3Z6-dDF3nMIy8xo0jyRB3qL2Be8A0UBfzEbbVIKfzleEdWhq_3Pk7F69Bh-KX4avLk8wCDKOFtxlTaHWiRpI1jhfzLazh9WyT1cq5YNtvJwgP4klQ3-83dYYgi40kMyuq_HC0OImyd-0fWHWpUwuLP04u0oTf3spm0Q_c8lc8xPsho9yaCSr4i3jVYncH5WetxwrkmL1CWN4FR0yZHWS0T6GI7IThHBOvePQl0DZn7QcKOiBSJN7aBDS0tlKDxK0q35H92PZfYTNc1x6xcwDju7ng2NfuLV3EO-3eU6m8G7UDbksYSVQGMchZfSaYOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تک آپشن عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135433" target="_blank">📅 21:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135432">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
❗️
قدوسی: تارتار خواهان حفظ هر دو مهاجم خودش شده اما خلیلی و حدادی به او اطلاع داده اند برای صرفه‌جویی بودجه باید یکی در تیم بماند و یکی جدا شود.........!
❌
❌
تارتار علیپور را انتخاب کرده و اگر علیپور تمدید کند باشگاه با سرگیف توافقی فسخ خواهد کرد
😐
😐
😐
😐
😐
…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135432" target="_blank">📅 21:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135431">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
امروز جلسه‌ای بین کریم باقری و باشگاه پرسپولیس برگزار خواهد شد در مورد شرایط ادامه همکاری با یک‌دیگر گفت‌گو کنند/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135431" target="_blank">📅 21:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135430">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135430" target="_blank">📅 21:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1wQs_HaC3UMjpRPmbcLIP7yg8dbpQJ0RH0ZT8zB0jNX7Xa--sFnTKB2hkgg8gk42bumpDMpRHpK1kGe2AIiSDxLmvkB6tt4AB7Y8LdTPJeS6WTbtHGODrnxIwKRAZycCXI12VVCDMIaCG8H6WrRb4ieaJJxmqGJcaoE0In2R5f-dcVsxSY3oRsg8fHCrzwiIE9pS2jCKkDen_z-xaLcyrnEi8O1Ymf6sltE0ILHMfo07NuIHk_ZyaLMJv0XaXdKlPDQ1_aMsMxHtgW5sv5WBkSlHhbzs-Mt7PaAm7WumEgBjEgMe66baG4xu3ZBVzbaRLocizrFVCNbCUfTNeirUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعد از منیر حالا اندونگ هم رسماً از استقلال جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135429" target="_blank">📅 20:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135428">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💢
سپهر خرمی: پرسپولیس و رامین رضاییان در حال مذاکره هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135428" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135427">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
به دلیل مسابقات آسیایی ناگویا ژاپن پرسپولیس، کسری طاهری، فرزین معامله گری، پوریا شهرآبادی، علیرضا همایی فر، امیر حسین محمودی و در صورت جذب (دانیال ایری، پوریا لطیفی فر، مسعود محبی یا مهدی زارع و فرهان جعفری) را از اوایل شهریور ماه تا اواسط مهر ماه در اختیار…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135427" target="_blank">📅 20:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
🔴
دفاع راست ها :
✅
عیدی و تیکدری و براجعه
🔴
دفاع چپ ها :  محمدی و جلالی و معامله گری   نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135426" target="_blank">📅 20:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/135425" target="_blank">📅 17:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoitChPTgAXXYdI1d0j9blfLAuxu5z8YlCOf6SBUZ8IG8duKv3U1Hv8yPxkL8qnH31thYJW3aVfi4XyOuZCxX0Yo9x3Lu8f8aJOPwEtc9iX30sjhZOHVGBqj7ceexoN8QTNc3i-N7bduYkkgxZk2FtcNvoUhyVAps2sKz4zSdhTgavLlqGnmX0wxquNN2YRmLKpF0F42F2yQwBUj4qJB1AyeaNGspOADjvFYWKwrc4lYYHQEMpXX_GRpVDeSNyHNSa-9eGru5QNtjSQrsbVO_hNjP4h0DYTQegPxdS704awhO9cy7OWcH64wyRp0Yc_K7juJI1-QXOh5mUxo0MN3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار ابوالفضل جلالی بازیکن جدید پرسپولیس
✅
جلالی تنها دفاع چپی که در یک فصل ۱۰ پاس گل داده و بهترین پاسور لیگ شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/135424" target="_blank">📅 16:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔖
منهای ورزش
🔴
جمعیتی عجیب و غریب در تهران که انتها ندارد؛ تصاویر هوایی از حضور حماسی مردم در مسیر تشییع پیکر رهبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135423" target="_blank">📅 16:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR2uyZnW_wpp-eXLLu6LbFNVOpVVeIBl03xtD8gY1A8E0fQy13YreXvOE-AgXmL9bhZ5-4lxZgODYWXVATFxEOM7-o0Hq69UFT93eZS4dkb28VfTC7Ga7Jn8cy5pNgH6rU73Q-_cHVe5Bh-qfWVMy90x8JdTBQuISARJFaApUwYvu_2P8iOP4YRHToGAnrbVbS8A1fPO1S4W1L9BzQ0_HmMf_obmR8M3ufDelpfkHtfmNHDsAIhzmiVY1K05kJhmLQSaKg9L4fmhXarU_g786h0vNOoXIMn-ry6-D0lbRFeGFHuciMree9gdn5T7mQyMo2W3XWwkshw8EbpVP5PqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌های فصل بعد پرسپولیس؛ با رفتن امید عالیشاه و سروش رفیعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/135422" target="_blank">📅 15:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
یکی این شلوار شیش جیب و صندلی رو از باشگاه بگیره.همه رونمایی ها همین بوده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135421" target="_blank">📅 15:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
❗️
#رسمی؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135420" target="_blank">📅 14:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135419" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135419" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135418" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
سازمان ملل : شاید باورتون نشه، بخاطر درگیری‌های مجدد تو خلیج فارس، ایندفعه خیلی بیشتر ازقبل نگرانیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135417" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
❗️
#رسمی
؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135416" target="_blank">📅 14:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmIYFD27Twv56ARsHu7O7pyIrHJU_L_PhAgF-jJql7lrhf8ybOTbvrofqg078_tO4xJaIIfoMymD8hO_EIrcw7BluT6sMcLgd5WNWH8F2_QL4xe9iYC_FhR-0uhGMXsjpB_7hujsLO940IbIgegrfNcVYhW0x2QmrL1-ebht3b_TLecQrUostc78G-Gt4n1zFB3YiQJSc8FoE_qrdKR5EWr3R_QhDqzN23lpUY_yJud5Qkx_YM3p_9MHa7FXb4MhhtI6tmw5o_kDvuHqBoVHfZl64AXQNSnaY0eN6mL2XizbxREwI0bw2M8dtpBHcnC1A-C47GtYLw2ACfFGyzCwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باز هم تایید شد .جزو اولین کانال ها اعلام کردیم جلالی و مبارکه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135415" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
تایید خبر دیشب مون
🚨
🚨
🚨
🚨
تسنیم: ابوالفضل جلالی دو ساله به پرسپولیس پیوست.همچین پوریا شهرآبادی چهار ساله با پرسپولیس امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135414" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/135413" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135412" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135411" target="_blank">📅 13:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/135410" target="_blank">📅 13:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135409" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔹
🔹
🔹
🔹
#شایعات
🔹
🔹
باشگاه پرسپولیس با رامین رضاییان مذاکراتی انجام داده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135408" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/135407" target="_blank">📅 13:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
خوبی بازیکن های مثل کسری طاهری پوریا شهرآبادی اینه که هیچ کدوم لیست بزرگ سال پر نمی کنن و همین طور سهمیه لیگ برتر حساب نمیشن هم جوون و آینده دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/135406" target="_blank">📅 13:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
انصافا بعد از سالها تیم داره جووون میشه ...همه بازیکنان خوب و با استعداد و جوان داره جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/135405" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
با اعلام‌ ترانسفرمارکت امید عالیشاه از پرسپولیس جدا شد
🔴
خداحافظ کاپیتان...؛ بابت تمام خاطرات خوبی که برامون ساختی ازت ممنونیم.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135404" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnqAl-tJPebWFTgarBdtf2h9itbOW6xBZhmi838rOS4TbsziT2o6kc0BHSyhiiEYMmQKWjD4n_PDf0HI6oxRKSmHit2X-58FOogbPMOjP3Ttu81olNVRJgy3Mdt-NroC55ZoRWyLzeiX5lqfJf8yclrkpAZfSzjKSDp7sw665dTRHOwNBz-PQaHyI_TZcmwnOiXPDYawaku6iRRdvwd4cPsXz9THKz6W-MSC0V8rewJgHHYrsWfeMil8e9T5KZdD2JCtdPKWUxgHitgPJ7c9z4i7RSwmFGid5bu-7zYysYoTUHtNIf1-EM8ffPJUlL0lN7PMIBIPY9A9HWdRIuzP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام‌ ترانسفرمارکت امید عالیشاه از پرسپولیس جدا شد
🔴
خداحافظ کاپیتان...؛ بابت تمام خاطرات خوبی که برامون ساختی ازت ممنونیم.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135403" target="_blank">📅 12:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135402">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔘
🔘
🔘
باشگاه پرسپولیس فردا یعنی روز شنبه مذاکرات نهایی و پایانی خود با دانیال ایری و باشگاه نساجی را انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135402" target="_blank">📅 12:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPiN8C3l6DnFClGuvCWJ2IENO-zilQC-KOmT2ZZFX1zZCPQb5kNt_HjsWDUGUXO4v_eJ0r9kUScUj-E3NoTantomk2sT9S9guSVhxYJpict3AxSqzAG3joil9ilDktOYCoSeKNV5kTpFuO-l3r6lnuJS3AC0llqX8FwyyY1K5ZCbUwBXLd2Axh2RwY-rVypNBcyYW2egAeqOgRLrzveQmiWRdVDFLzJWGfk667Gbq-DwbDyhb-_3yAq_1vzweJmQAb2jOoPSGBfpnOHMnwP3Goj9MlEaUWhfH14Wx4NFf4AGo-2FtNJdjs7a_ejt0qfGArJ2wZxSBHpaKE7cx9tsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آقای گل لیگ عراق چرا بدون تیمه
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/135401" target="_blank">📅 12:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135400">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
دور جدید مذاکرات با ایری امیدبخش بوده و مسئولان باشگاه به جذب ایری امیدوار شدن/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135400" target="_blank">📅 12:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cugcy-jL7sZh_5K6w7B__ApspUroJWzXpsqhKG0XCsAavwyTetgJeKmwPKUN69uUaofAShDBD5hz6MwK8zz_TxhgCZLj66bYqKHsNVrmr5gJjmA-daYZVfndz8FK0CKpv2DaTDP2SkeZnWU6K1E8ImwWt4rh77Mc658IVzq_BOcdGd4KNFOjFnBPzXxBlA2OyvId-rIlaRQgHwmtqvRyMB-TqVcZfRQBKtai3cAaCxrTg-na1lvvMpTbfNNuNSiCrhggTTFhi8w-lffnUq1Vw5Eg_3dgNfrk7rdZCHk-Oz66nUOiYxbWew3iKEkpf0LSGaWjiUkzsBZZvOdkC984NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پناه بگیرییییییید، اریک باگناما بازیکن ازاد شد.
🔴
پ.ن اوه اوه .فقط مونده این بیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/135399" target="_blank">📅 11:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135398" target="_blank">📅 11:57 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
