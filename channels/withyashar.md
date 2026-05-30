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
<img src="https://cdn4.telesco.pe/file/LFcuQXxrf274e7JT5cOiGo5yQyWuJw5afbfTOptWp3lSN3CrQeIKnUsonMOYbJL8CUv-8HFeFHswsF-atpVCPdGK_cFux9kDymmZnY9RPzW7xE5kUxnNtvGoucj9tQMFM9BhdpgVMg24mKAUkQ_C1Gazr7AFWkEu3Dka5OGgn_W0FoCdAzsyhiqusGo13bS18ZHDh-o3ZslMEqqOTHNS61pqWJY1vaZXD_eQbtjTH9nb_ehqrTT8TxzC-Ikl_I2jzmTeRz7iKL4TclgE-CPtcMKMi_5lkMFJHhux7l4Cpff0Ql9rTSO44G5iPRHTFBDFt3Go5AlKDj8b4aBS3nsxVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 282K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 01:00:47</div>
<hr>

<div class="tg-post" id="msg-12968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">@withyashar
JangHub</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/withyashar/12968" target="_blank">📅 00:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=e2c48k4EDbfefq45sFCS8ECSElUbL89_uS7-E3PTZi3F_xmqyUhErB7p6QlfYxAGzgT4WGPqZWDZ_HOGlhKZh_Qtf5hX3kllc04Ir6y3J5y0iFmsxq37iign5tZteAddV4kt3tvnNTQ5VTACA9KjtHY77WQVHJZ8KurUNH7bq1_-XcUh4tX0ybRBca5dpcXn3rZTPvebv-whtfPv9xaISnkjBavf9hSUgW5kFJ0ETk01BLGsqgTpn7ua4xlsaeyxe_cUzkCDm3w28-gNdNww0L_LYh0CErGbbgZ_rFLoMfNsb6q2umpdPDyyVhQbjN9PrGxeyFQunRFaDzJMw-K_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86254cf93.mp4?token=e2c48k4EDbfefq45sFCS8ECSElUbL89_uS7-E3PTZi3F_xmqyUhErB7p6QlfYxAGzgT4WGPqZWDZ_HOGlhKZh_Qtf5hX3kllc04Ir6y3J5y0iFmsxq37iign5tZteAddV4kt3tvnNTQ5VTACA9KjtHY77WQVHJZ8KurUNH7bq1_-XcUh4tX0ybRBca5dpcXn3rZTPvebv-whtfPv9xaISnkjBavf9hSUgW5kFJ0ETk01BLGsqgTpn7ua4xlsaeyxe_cUzkCDm3w28-gNdNww0L_LYh0CErGbbgZ_rFLoMfNsb6q2umpdPDyyVhQbjN9PrGxeyFQunRFaDzJMw-K_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای کانیه وست :
کنسرتم در استانبول رکورد ۱۱۸ هزار تماشاگر را ثبت کرده و به بزرگ‌ترین رویداد استادیومیِ بلیت‌فروشی‌شده در تاریخ تبدیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/12967" target="_blank">📅 00:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89387a1183.mp4?token=mnS9EF6WIm5kMAq-SHOIcAnSdMY1P6OwGGD1BjZqs7NPOloY5EiLMTezdnCrk1-ZMYee8I7D_tFKaFyBfM9UREimWOgUuFPqbbhkcmwxmUCQ5aSqzol7qwniqJ3-PCmvYD1SLlFA9G0VROnDTl6gc5SKmkxf0kVkJ4RAMPuz2cTfw2WrNt3pVohABsE0FecoKX9BJkHac9FM6o9kZanwmGuA1yejsxVbAvWeKdw2ksFtiJBvzeqgPvzbqmSNqqaElwdQuO5Re3634paUWVrtxGlRklmJTxzE5Rw9tT3BUctK99H_Idq3UsZfC0ICCMY-_-7duFQOlXyB-HOBVJKHlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89387a1183.mp4?token=mnS9EF6WIm5kMAq-SHOIcAnSdMY1P6OwGGD1BjZqs7NPOloY5EiLMTezdnCrk1-ZMYee8I7D_tFKaFyBfM9UREimWOgUuFPqbbhkcmwxmUCQ5aSqzol7qwniqJ3-PCmvYD1SLlFA9G0VROnDTl6gc5SKmkxf0kVkJ4RAMPuz2cTfw2WrNt3pVohABsE0FecoKX9BJkHac9FM6o9kZanwmGuA1yejsxVbAvWeKdw2ksFtiJBvzeqgPvzbqmSNqqaElwdQuO5Re3634paUWVrtxGlRklmJTxzE5Rw9tT3BUctK99H_Idq3UsZfC0ICCMY-_-7duFQOlXyB-HOBVJKHlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
۴۰ هزار ایرانی برای تنگه هرمز یا برای یک توافق هسته‌ای کشته نشدن.
ما باید فشار روی رژیم رو ادامه بدیم تا نتونه منابع مالی لازم برای تأمین و پرداخت به نیروهای نیابتی و مزدورهاش رو فراهم کنه.
اما بهترین راه برای اینکه کار به حضور نیروهای خارجی در زمین نکشه اینه که به مردم ایران کمک بشه تا خودشون اون نقش رو بازی کنن
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/12966" target="_blank">📅 00:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رییس سازمان عقیدتی سیاسی انتظامی:
حکم قاتلان خامنه‌ای رو باید در ملا عام اجرا کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/12965" target="_blank">📅 00:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6mHoWnfAqBpfyZT8dJI_IyOKtNcvV6n1_VDZh4qvGER554ZtwBkqVi_TJeWOqlyYOonFNwj2tYzRsJeL9qGaHJBkfXOvILE0oIilPBrn6nmLyGPI2owMCEIKrwsWvkgoJkdL8ztZkxVm_adfw7rhJXmMkxA7RMfo5qKbpr49mJwTAqW4jrXp8Ojls8_EmtERdnTlyGlp4w07TxSSysXxjcjKgUHdJyMt4soqf9B04itNoplfc2W6pwN0fjoNnX3ZWKu5rxtNMkRr5Yt6AZNvsZRycj1ObMcyu3wOgfCScWN0C--Ufesrss5PE6vobD8nBwYhUkHF568q7bwq17Cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث
🤣
:
«یکی باید برای پاپ توضیح بدهد که شهردار شیکاگو کاملاً بی‌فایده است و اینکه ایران نمی‌تواند سلاح هسته‌ای داشته باشد!
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/12964" target="_blank">📅 00:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=LikChH1HoR7qpy9--Uuhv-e80Octzhu3MA6BZCJVzRUD0UqeS6UX1vhC89BFW-Exmn4j6O7pVjqr-SZ00GWNSsWe8arTnjsT8rX7QVRQxR4yXCfN4skdb_4Y-mhe3iAqlQPp4AnIkJ9ViBC5bUKbbn5woJa7pNdEY1iQR3uxv_VY4e6oe7nwh-OoxmO4t8J1piWxjnfwVmlnKh6r0FAYW1xcW8Kl2etJe68nWOEVhqyeES7w0DTxi0FbJZeWwCBgFjf5DPtC0KX7UlRvWSAUcAotvou7yIJhU0Sw1lGXdwXJuO7yPoz4D96N_An-yVLlwGkSDUQA8jGbox3teTtB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31f4e3fc3.mp4?token=LikChH1HoR7qpy9--Uuhv-e80Octzhu3MA6BZCJVzRUD0UqeS6UX1vhC89BFW-Exmn4j6O7pVjqr-SZ00GWNSsWe8arTnjsT8rX7QVRQxR4yXCfN4skdb_4Y-mhe3iAqlQPp4AnIkJ9ViBC5bUKbbn5woJa7pNdEY1iQR3uxv_VY4e6oe7nwh-OoxmO4t8J1piWxjnfwVmlnKh6r0FAYW1xcW8Kl2etJe68nWOEVhqyeES7w0DTxi0FbJZeWwCBgFjf5DPtC0KX7UlRvWSAUcAotvou7yIJhU0Sw1lGXdwXJuO7yPoz4D96N_An-yVLlwGkSDUQA8jGbox3teTtB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا:
کشور من از همه طرف ضربه خورده؛ از داخل توسط همین رژیم، و از بیرون هم به خاطر پیامدهای بی‌فکری خودش. با این حال، جمهوری اسلامی هنوز سر جاشه.
بعضی‌ها توی این جمع ممکنه اینو نشونه‌ی قدرت رژیم بدونن. من اینجام بگم که اینطور نیست.
این فقط نشونه‌ی اینه که دنیا هنوز نتیجه‌ی درست از چیزی که داره می‌بینه نگرفته.
پهپاد شاهد فرقی نمی‌کنه کجا باشه؛ چه یه ساختمون مسکونی، چه یه میدان اعتراض تو تهران، چه دفترهای تجاری تو دبی.
پهپادهایی که آسمون شهرهای اوکراین رو تاریک کردن، توی همون کارخانه‌هایی ساخته شدن که زیر نظر همون رژیمی هستن که توی تهران برای شکار معترض‌ها، توی خیابون‌ها پهپادهای نظارتی فرستاد.
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/12963" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پست جدید بوگاتی شاه   https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg= کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/12962" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در پی حملات سنگین حزب‌الله، به بیمارستانی در شهر نهاریا در شمال اسرائیل دستور داده شد تا بیماران را به تأسیسات زیرزمینی منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/12961" target="_blank">📅 23:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شاهزاده رضا پهلوی:  با جمهوری اسلامی توافق نکنید، بلکه به آن پایان دهید.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/12960" target="_blank">📅 23:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/12959" target="_blank">📅 22:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpX1cuGt6QF6uWQBCJkebiK5fgWpJNzqvVJGQdLXr28e5lV1oGwYP1kTybJ_Aaoht7e0wHXCxNwP7YYlrc4I18S2xCDdtRT3I6qBHdrIsUijq-iqcAygxNY8YRSdslxgDHmDqJpZHT8lSU0Sqjg1GLhe9LnNrv2sFebqaODnUvpwyCYHQ9XNbGVm3nGt20kCKOeloresopHqi3IgH867dgzjIhtCCJmqen9K9rkkb8gbGr9rY3ECKXkzDX-AeZjOvDVNKbTBKW1tSZyCH8m_No_Y-d3YKkvmcsEilWYTlCCsMoOO1qyDw1VzYwnu41UalOaC92MOuvS_c7tbTz-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ادعای آمریکا در جریان این جنگ، دست‌کم ۱۶۰ شناور دریایی ایران را غرق کرده است. هر یک از این شناورها می‌تواند منبعی بالقوه برای آلودگی باشد. وقوع یک نشت جدی در تنگه، مهار آن را بسیار دشوارتر از حالت معمول خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12958" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/12957" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKiasha</strong></div>
<div class="tg-text">یاشار امشب ردبول رومی خوری؟</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/12956" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سنتکام اعلام کرد کشتی تجاری Lian Star که از یک بندر ایران خارج شده بود پس از 20 هشدار توقف و عدم توجه آن توسط یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و در دریای عمان توقیف شد.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12955" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پست جدید بوگاتی شاه
https://www.instagram.com/reel/DY-ObumIJEK/?igsh=MjQ5cGt6dWo0dGg=
کارای اداریش رو انجام بدید
💥</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/12954" target="_blank">📅 21:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12952">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صداوسیما جزئیات غیررسمی از یادداشت تفاهم (ایران و آمریکا) را منتشر کرد
‌
یکی از مهمترین محورهای توافق (ایران و آمریکا) بازتعریف قواعد عبور و مرور در تنگه هرمز است
‌ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار نهایی آن در خصومت با ایران باشد به عنوان کشتی تجاری شناخته نمی‌شود و اجازه عبور از مسیرهای تعریف شده را ندارد
تعیین مسیر حرکت و تعیین هزینه خدمات ناوبری در حوزه تصمیم‌گیری ایران دیده شده
‌
هر شناور موظف است اطلاعاتش را در اختیار مرکز مرتبط با نیروی دریایی قرار دهد و فرم‌هایی شامل جزئیات محموله مالکیت و مقصد را تکمیل کند
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12952" target="_blank">📅 21:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12951">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الجزیره: ترامپ برای جلوگیری از جنگ با ایران پیش از جام جهانی بسیار مصمم است
او همچنان برای دستیابی به یک توافق موقت با تهران تحت فشار است، اما پیشرفت فوری بعید به نظر می‌رسد
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/12951" target="_blank">📅 21:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12950">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شبکه ۱۴ اسرائیل : نتانیاهو، قراره به‌زودی یه جلسه امنیتی برگزار کنه تا درباره نحوه پاسخ به شدت گرفتن حملات حزب‌الله تصمیم بگیره
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/12950" target="_blank">📅 20:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12949">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12949" target="_blank">📅 20:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12948">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/12948" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12947">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌊</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/12947" target="_blank">📅 20:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12946">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhydrus</strong></div>
<div class="tg-text">درود میشه یکم ویس بدی دلمون گرفت :)
❤️</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12946" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12945">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frefrJq1u8y8a7lOgjUPhiH65RMA9KxMmHdtmelxm8jbAdy-q3jbAyL-8gzK4r0zDYtDZL4QI4Q2nEdJjUnJ2KPUXz_G_f5wsJ0o-9gS2I40IWNpfgeAc_8QDESSOinmH39AbkC05GpEo8ntSFeM5sZeGaNchtnup4j1JwlNrcYgKHm4HJh0ZMuzA5K-sqRE5k9iM1rgqABJm2UqePJV2vnuVO7ShfC_az72IWZoLMGq5P9oCPJoNJ4tXDgL2ZRnKVw7QTnjByp_Fzrx4LUF8SKFOi4HsR5XjpVb5X68RvzYTgyhhyScasLeqHg45sKiIVe6qY8YpdD_RHgNeZtsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پنج مرحله سندروم ترامپ هراسی
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12945" target="_blank">📅 20:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12944">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نماینده سیستان و بلوچستان در مجلس :
برخی از مناطق زاهدان ۲۴ تا ۴۸ ساعت آب ندارند. ادامه بحران آب، استان را با چالش‌های امنیتی و اجتماعی روبه‌رو می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/12944" target="_blank">📅 20:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12943">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی فدراسیون فوتبال:
روزبه چشمی به‌دلیل مصدومیت جام جهانی را از دست داد
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/12943" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12942">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تلگراف: دو ژنرال قدرتمند، احمد وحیدی و محمد جعفری، با هم متحد شدن تا قالیباف رو از قدرت برکنار کنن.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/12942" target="_blank">📅 19:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12941">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، گفت مردم ایران برای ساختن آینده کشور خود آماده‌اند و از جهان نمی‌خواهند آینده ایران را برای آنان رقم بزند، بلکه خواستار آن هستند که جامعه جهانی در کنار ملت ایران بایستد.
او در بخش دیگری از سخنانش، با اشاره به خروج اجباری خود از ایران در ۱۰ سالگی، گفت که با وجود گذشت ۴۷ سال، هرگز امید خود را به آزادی ایران از دست نداده و همواره صدای مردمی بوده است که امکان بیان خواسته‌هایشان را نداشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/12941" target="_blank">📅 19:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12940">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=i4thrGNSVcexxVe6A15H9mAcloK3ztnDqthKlRyE9w7OhcrQnk6uveqv_lv-vnhkCBmvWROzgPouRJcSn58AgEj_hX_Zwm_WNeCDptzTQs45kuUMW53dDfSaMzoq-t-17dwoQt6JBpNAKEXY25nKPxsOHdtn_HrnZ26uSZ-VoXtneX9PzDOt0j6uuIFDlhZcIntG1CqgtCNh62L5gSfGCPl3DVcrDdFhHSbt95_IRbhcdRW1P50HkBimnO2YeEoSf3RLDyfpmgYnCzCmAZLBFOFVofgJ8fQGOTEidW8qkLEVDBNUZWkdB8OX6gcRo7eNDNFjaKZJTmitBt6UwoeO7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654bf3851d.mp4?token=i4thrGNSVcexxVe6A15H9mAcloK3ztnDqthKlRyE9w7OhcrQnk6uveqv_lv-vnhkCBmvWROzgPouRJcSn58AgEj_hX_Zwm_WNeCDptzTQs45kuUMW53dDfSaMzoq-t-17dwoQt6JBpNAKEXY25nKPxsOHdtn_HrnZ26uSZ-VoXtneX9PzDOt0j6uuIFDlhZcIntG1CqgtCNh62L5gSfGCPl3DVcrDdFhHSbt95_IRbhcdRW1P50HkBimnO2YeEoSf3RLDyfpmgYnCzCmAZLBFOFVofgJ8fQGOTEidW8qkLEVDBNUZWkdB8OX6gcRo7eNDNFjaKZJTmitBt6UwoeO7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مک‌اننی از فاکس:
بلومبرگ گزارش داده است که حملات موشکی ایرانی چند آمریکایی را در یک پایگاه هوایی کویتی زخمی کرده‌اند. فکر می‌کنید اوضاع در چه وضعیتی است؟
مایک جانسون، سخنگو:
دیشب با رئیس‌جمهور ترامپ صحبت کردم. او کاملاً در جریان است. فکر می‌کنم رهبری جدید ایرانی‌ها می‌خواهد این درگیری را به پایان برساند.
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/12940" target="_blank">📅 18:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12939">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHgSr3rTf2e2IMHQoc2QEMVjAwMXLBZhNORqIlnx86q8f-wjRaFzodeqOvWQLOKRVtj3-DLNzQxH5iffbthpcJoveSmP3zQr7psspRchmD6NNebPus6waxJfI4vMCBclcgl0PAwNNj67FQf9MFldFTmlwwonSMIKFPUPC-gK2aqiuvB8iziH_O8w0t2Vph360gZayVO6wLeECxwH_2C28f_p_y8Z9Y_26PI3y5h0IMfxWTeGjxt3qrc6gMvy_Y87tgvT-neEt9Ii1NrZ-zJWaNBqTxTsEcAAX21d9YxeLfd87Ksk25sDHoZvjm7fI-alhtwpz-sDTz4gcUnyqCpEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که ناو آبی/خاکی یو‌اس‌اس باکسر (lhd-4) قرار نیست در حوزه مسئولیت سنت‌کام  مستقر شود. ناو آبی‌خاکی کلاس واسپ نیز امروز از بندر سِمبانوان در سنگاپور حرکت کرد؛ اگرچه اکنون به سمت شرق در حرکت است.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/12939" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12938">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست «امنیت دریای سیاه» در اودسا در جنوب اوکراین، گفت که دنیای آزاد هنوز متوجه ماهیت جمهوری اسلامی نشده است.
شاهزاده رضا پهلوی درباره تلاش برای توافق با جمهوری اسلامی با امید به ایجاد ثبات، گفت که یک سگ وحشی در نهایت دست شما را گاز می‌گیرد.
او افزود: «پهپادهایی که اوکراین را هدف قرار می‌دهد از سوی جمهوری اسلامی تهیه شده و با همان پهپادها مردم معترض خود را در خیابان تعقیب می‌کند تا تک‌تیراندازها آن‌ها را هدف قرار دهند.»
شاهزاده رضا پهلوی گفت که تهران و مسکو معماران مشترک هرج‌ومرج در جهان هستند.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/12938" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12937">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عمان: در آب‌های سرزمینی خود جسمی شناور را مشاهده کردیم که مظنون به مین دریایی است‌
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/12937" target="_blank">📅 17:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12936">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea39bc17f.mp4?token=ci6GgnY7vDNh6gchcMsfq3Zcx3klR4tBTkEWBDT3bypxXibWkHpwT1BkZfhpQfJvUfcw1nGh2GzJkBrZ09bW0JIM9UI18N9rbMINI6aOJtZlAvSP_4ptC_kZB9C_3Yf2Wj53wlnbbdNdmi3RImM34Z0vuvcLk08-QArT8WQNE2qDwGFDRRQ8EMtdtjWoQlUuLYuykPjBy5BMXMsS1AHszve4QYuzqwSMB2UGQR_Z4EEgRxS0YsKcQO8pFk0zJ-SpESIHq_rVycDxqkVZ3gh0JznMaNsuNBjIQAQFxYBWSbP3JvoLwak_qNv3R1rQ7Ru-84PZEtLB3di6yYmK3Ml3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea39bc17f.mp4?token=ci6GgnY7vDNh6gchcMsfq3Zcx3klR4tBTkEWBDT3bypxXibWkHpwT1BkZfhpQfJvUfcw1nGh2GzJkBrZ09bW0JIM9UI18N9rbMINI6aOJtZlAvSP_4ptC_kZB9C_3Yf2Wj53wlnbbdNdmi3RImM34Z0vuvcLk08-QArT8WQNE2qDwGFDRRQ8EMtdtjWoQlUuLYuykPjBy5BMXMsS1AHszve4QYuzqwSMB2UGQR_Z4EEgRxS0YsKcQO8pFk0zJ-SpESIHq_rVycDxqkVZ3gh0JznMaNsuNBjIQAQFxYBWSbP3JvoLwak_qNv3R1rQ7Ru-84PZEtLB3di6yYmK3Ml3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست درباره ایران: ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم.
و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/12936" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12935">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر جنگ آمریکا: به محاصره دریایی ادامه میدهیم.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/12935" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12934">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/12934" target="_blank">📅 13:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12933">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">#shahzade من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12933" target="_blank">📅 13:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12932">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓡𝓪𝓼𝓪</strong></div>
<div class="tg-text">#shahzade
من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/12932" target="_blank">📅 13:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12931">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#shahzade</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/12931" target="_blank">📅 13:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12930">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سفر قاهره با یاشار غمی ندارد فقط لذت ببریم از وقایع
👑</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12930" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12929">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صداوسیما : طبق نظرسنجی که از مردم انجام دادیم، اکثریت مردم از وصل شدن اینترنت ناراضی و ناراحتن. باید فورا مجددا قطع بشه
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/12929" target="_blank">📅 12:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12928">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تسنیم : با وجود اینکه ترامپ در شبکه Truth Social اعلام کرد که محاصره دریایی ایران «اکنون برداشته خواهد شد»، ملوانان ایرانی گزارش می‌دهند که این محاصره همچنان به طور کامل برقرار است.
کشتی‌هایی که پس از اعلام ترامپ تلاش کردند از خط محاصره عبور کنند، توسط ناوهای نیروی دریایی آمریکا هشدار داده شدند که فوراً بازگردند وگرنه با آتش مواجه خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/12928" target="_blank">📅 12:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12927">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!  @withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/12927" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12926">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/12926" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12925">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو خطاب به لبنان : درخواست اتش بس دولت شمارو رد میکنیم
باید بگم که اسرائیل تا نابودی کامل حزب الله ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/12925" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کاخ سفید به الجزیره گفت:
ترامپ تا زمانی که خواسته‌های آمریکا برآورده نشود، توافقی نخواهد کرد و ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/12924" target="_blank">📅 10:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNxlVL8dD6QbN7Dwssek1cnOBrUQUTCRvhwaA87xblT3IobCuOy7edLQKf5ds1FlAq5u-DfiQbV1Iz4HRjcQQ04LMM2Lx32JS7R1DjXpKbNBI0-Q3F9YDcmf6JyosZrSLqU--PbVKOYG3pycMCUzZUknM8I2yZ1IK4-C_j9-THfWx6z_uwZbaiIim7Kji812TGSbNbj4Ct37rcCh2CgroVHQq__IHpKEhWOPVV8MtotztaBKeQSbQXu7YHJcM3L24tC_KolbnOYegz8VEx436Uj5BkgI1AW2ItyPBtw1Xl8FugtijPUCWPHO0zM6HE56oTbWO3wJO0bqJpukvRABPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
این یک اثر شایع و خوش‌خیم است
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/12923" target="_blank">📅 10:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سنتکام:  هر شناوری که در حال انجام یا حمایت از فعالیت‌ های مین‌گذاری در تنگهٔ هرمز دیده بشه، توسط ما هدف قرار خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12922" target="_blank">📅 03:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=RCCG3GyMiv3LLScxHgul8zQbNviBSo1zPR6Dpctt1LIBOo08vqRaMKN75ZdjEZFsqu4ZXY0fJ3doQ-ehvk15WjnAZj1IX9F_pyv8zltTSbpyDGjQ5RcOup8oQKi6mU5AFK8tDek8CQn72h-UYT58qAbAYysHBij2N8GEHTtKxAh60l7g9m2bACIeL0337zkyeKRtMjq3rLG1umzRILq0N6vLsPVDfMjbvxzk_UbUy46ElOzXDMWyivyuS4Yin_0taitlg393Mc5HdS_GNay9kauxy1VZZpUU0K-dAgcq1xjidlt_EmDryT6EmGsfmRv4HcEWEnryoVPo6VgAD97tKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=RCCG3GyMiv3LLScxHgul8zQbNviBSo1zPR6Dpctt1LIBOo08vqRaMKN75ZdjEZFsqu4ZXY0fJ3doQ-ehvk15WjnAZj1IX9F_pyv8zltTSbpyDGjQ5RcOup8oQKi6mU5AFK8tDek8CQn72h-UYT58qAbAYysHBij2N8GEHTtKxAh60l7g9m2bACIeL0337zkyeKRtMjq3rLG1umzRILq0N6vLsPVDfMjbvxzk_UbUy46ElOzXDMWyivyuS4Yin_0taitlg393Mc5HdS_GNay9kauxy1VZZpUU0K-dAgcq1xjidlt_EmDryT6EmGsfmRv4HcEWEnryoVPo6VgAD97tKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلزار: نماز میخونم و شبا هم هر موقع بیدار شم شروع میکنم به دعا کردن
@withyashar
❄️
👃</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/12921" target="_blank">📅 02:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک مقام کاخ سفید در گفت‌و‌گو با خبرنگار شبکۀ الجزیره مدعی شد: دونالد ترامپ هیچ توافقی را امضا نخواهد کرد مگر آنکه این توافق مطالبات آمریکا را تأمین کرده و با خطوط قرمز تعیین‌شده از سوی او همخوانی داشته باشد.
«واشنگتن هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست پیدا کند».
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/12920" target="_blank">📅 02:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12918">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12918" target="_blank">📅 01:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیل هیوم: مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12916" target="_blank">📅 01:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12915">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">https://t.me/boost/withyashar
بچه‌ها عالی بود
👏
👏
، بوست ۳۴۸ تا دیگه لازم داره. لطفاً این پیام رو برای تمام دوستانتون که تلگرام پرمیوم(تیک) دارن بفرستین و ازشون خواهش کنین که چنل رو بوست کنن
❤️‍🩹
چیزی‌ تا ایموجی نمونده
🤰
🫃🏻</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12915" target="_blank">📅 01:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12914">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شکست مذاکرات پنتاگون
؛
اصرار تل‌آویو بر تداوم جنگ در لبنان
منبع رسمی لبنانی: طرف اسرائیلی با درخواست هیئت لبنانی برای آتش بس مخالفت کرد
یک منبع رسمی لبنانی در گفت‌وگو با المیادین اعلام کرد:  هیئت نظامی مذاکره‌کننده در پنتاگون، به درخواست خود برای برقراری آتش‌بس واقعی دست نیافت. این هیئت بر مطالبه آتش‌بس پافشاری کرد، اما با مخالفت مکرر اسرائیل مواجه شد.
به گفته این منبع، هیئت اسرائیلی از عقب‌نشینی از اراضی اشغالی لبنان خودداری کرده و بر «نابودی (توانمندی‌های نظامی) حزب الله» اصرار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/12914" target="_blank">📅 01:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZACNPTjijggevoHu1MtszI9KTMEh85DiQNT6VLnJIUpkeqk0fShmC-Qk7lyEIAbuiaSQDinFAECCpG-dCB8Sz5wzezqLMpeyRk-pmawoEd0xs32EHV34FNJFcznC84n-_gpN7VRHJ75kDstqUfrT8exRzLrb1Ef86RjX6wyfaAEpvq5XxGm9CcXfEcx_72OMih_n7Jkmt-ZErGzJXpwDZmb-RSwnYKHuW3Wrf3o9nJ84XSAOy_XnG7xoy9JGCiUb4N0AUPRX_DjHV9DemK1jwZQqqYIwvIzrc-MTrw1nFoX0C2pPT6dGtQut2BD74gYSPJ7P48-b6maU2-7Wi1SOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
@withyashar
زبانم قاسمه کتلته…
🥴</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12913" target="_blank">📅 00:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صداوسیما: منابع محلی از فعال شدن سامانه پدافندی در جزیره قشم حوالی ساعت ۲۱:۲۵ خبر دادند.
بررسی‌های اولیه حاکی است این اقدام به احتمال زیاد در مقابله با ریزپرنده‌ها انجام شده و با موفقیت همراه بوده است.
سامانه‌های پدافندی آرش‌ کمان‌گیر در روزهای اخیر عملکرد موفقی در مقابله با پهپادهای دشمن داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/12912" target="_blank">📅 00:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حسین علایی:
سه روز قبل از ۹ اسفند به شمخانی گفتم امریکا جنگ رو با تـرور رهبر شروع میکنه؛ گفت نمیتونن اینکارو کنن. چون نمیتونن پیداش کنن.
سه روز بعد هم خودشو زدن هم رهبر رو. اونا اطلاعاتشون خیلی قویه.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/12911" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8i28nuLE2_WiGmgtmAQE9lEhCA2nj8JmczGUI8OwU1I85nr1G9T3r5_1ebxmXcgpquHNCSphkntw9ylb0THqPF4WgN9liwfsen1N1DQSe_zfrsEGSoiSKkrg1gLK964aflUTfE06wIMdiQlqT-gfjybgl8QdjyBELFVzeoC-L4CHJKo81wosUMk0TozbpYthCISjRXv3Skw2MxWv7OADA9O4YP4TV4a77mj6OzQTn8J0ZHS--0vxao_SVtdP4O-RyYp2-VC9YPASoSzP5DhdGmMBzF7Dnx2liVzfT4ewVIqhhFnF23k9nE4NH5v7Z8AM5uECzGA2FW7ok0GXSy7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالک شبکه ایران اینترنشنال به ادعای فاینانشال تایمز
گزارش Financial Times درباره ایران اینترنشنال می‌گوید این شبکه به‌صورت رسمی توسط شرکت بریتانیایی
Volant Media UK
اداره می‌شود، اما ساختار مالکیت آن پیچیده و چندلایه است و از طریق شرکت‌هایی در بریتانیا و جزایر کیمن انجام می‌شود. طبق این گزارش، این شرکت در سال‌های اخیر با زیان‌های سنگین و بدهی‌های بزرگ (بیش از ۴۰۰ میلیون پوند) روبه‌رو بوده و اخیراً بخشی از بدهی‌ها از طریق تبدیل بدهی به سهام بازسازی شده است. در جریان این تغییرات، سهام قابل توجهی به یک شرکت ثبت‌شده در جزایر کیمن به نام
Info-Cast Cayman Limited
منتقل شده که مدیر آن فردی به نام
صالح حسین الدویس
معرفی شده است؛ او در گزارش FT به‌عنوان مدیری مرتبط با گروه رسانه‌ای سعودی
SRMG
شناخته می‌شود. این گزارش تأکید می‌کند که مالکیت شبکه شفاف و مستقیم نیست و در قالب ساختارهای مالی پیچیده و آفشور انجام شده است
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12910" target="_blank">📅 00:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاهزاده رضا پهلوی :اگر اروپا می‌تواند اتحادیه خودش را داشته باشد، چرا ما نتوانیم در خاورمیانه اتحادیه‌ای داشته باشیم؟
چرا نتوانیم در پروژه‌های مشترک مربوط به امنیت ملی، اطلاعات و حتی همکاری‌های نظامی همکاری کنیم؟
چرا باید بخش زیادی از بودجه‌مان را صرف تسلیحات و مسابقه تسلیحاتی کنیم، به جای اینکه این منابع را صرف رفاه، صندوق‌های بازنشستگی، بهداشت و آموزش کنیم؟
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/12909" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیویورک پست: وجوه مسدود شده مستقیما به ایران ارسال نخواهد شد، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده خواهد شد و پرداخت آنها منوط به تعهد تهران به باز کردن تنگه هرمز و پاکسازی مین‌ها خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/12908" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شاهزاده رضا پهلوی:تصور کنید که فردا مدل سیلیکون ولی در سیستان و بلوچستان اجرا شود. چرا که نه؟
هر چیزی که کشور نیاز داشته باشد از هوش مصنوعی گرفته تا فناوری و نوآوری می‌تواند در آنجا توسعه یابد.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/12907" target="_blank">📅 23:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام دولتی:
نشست ترامپ در اتاق عملیات به پایان رسید وحدود دو ساعت به طول انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/12906" target="_blank">📅 23:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12905">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیویورک پست:
زمان نهایی شدن تفاهم‌نامه بین آمریکا و ایران مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/12905" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=bIQOiqEAWNimpQTKb0RjGjlyFCjfemfB-5ir2ajHm-3PUsfRGFbzl3pchQqVd_zqQtBEWyU7xR5W8EnCnwi4OQmjeLqAbpNaG21dazUXuFVkyLYro_Kxgy8CACT44rgAX6iBVmN13dQ_Wkot1RM0OAhHlPq3ofBYtNHpeeQ8fGY3a-G5neg8-kGZ4Eu_Py1OCV4R5h6SJhKoGHhy9I-DjfK4lXVDNlUcaWag-3n3BVues0u4IsJCMDbafpBeh_fgxSaj4dQwNCCPKviUs0hwc3wgKTn6bZmhsBs_On8ZceMClCCnoqB5h402j7ajmvOzsKn_Ivdp5x-01oBn8LjeAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=bIQOiqEAWNimpQTKb0RjGjlyFCjfemfB-5ir2ajHm-3PUsfRGFbzl3pchQqVd_zqQtBEWyU7xR5W8EnCnwi4OQmjeLqAbpNaG21dazUXuFVkyLYro_Kxgy8CACT44rgAX6iBVmN13dQ_Wkot1RM0OAhHlPq3ofBYtNHpeeQ8fGY3a-G5neg8-kGZ4Eu_Py1OCV4R5h6SJhKoGHhy9I-DjfK4lXVDNlUcaWag-3n3BVues0u4IsJCMDbafpBeh_fgxSaj4dQwNCCPKviUs0hwc3wgKTn6bZmhsBs_On8ZceMClCCnoqB5h402j7ajmvOzsKn_Ivdp5x-01oBn8LjeAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت:
ما حدود ۱ میلیارد دلار از رمزارزهای ایران را توقیف کرده‌ایم فقط مستقیم کیف‌پول‌ها را گرفته‌ایم.
برخی از آن‌ها شاید همین الان در حال تایپ کردن باشند و هنوز متوجه نشده‌اند که کیف‌پولشان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/12904" target="_blank">📅 23:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شبکه کان اسرائیل :
نتانیاهو خواستار از سرگیری حملات به ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/12903" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پست جدیددد اتاق جنگ داغ داغ کلیک کنید و کارای اداریش رو انجام بدید
💥
https://www.instagram.com/reel/DY7xeuCRP_4/?igsh=aW9oOXNnbno1NDJ6</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/12902" target="_blank">📅 22:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZUrwJKame8wSs60BM5GsANTQgbqQ_vvdPwV3foJvEidWmNywPLRt7ACIypvTZrz1XcbZwvveW74MxyP3tfBUvVn2Up03EMjiTjjKq1uLDalXUuATGa7GGvJfAdABdWa0E6wBgpRjnf1Ou2Iqsh6Gur5Z1cQJf85PVsKsOmyRRcCoOQa23LFeH5iWPpvjKhL7SkSXJveRkx_LaDovBNrt4V2xAkJmyHMz8yePDrGXVOIFgSOf2U29h6iPaxfqsicAY37pN-gY0_zeOlI5sXoEeqqLvpR6svLnT20XfC4zc1O3heYa4eLdLZuqDVpgEOZypjMY8FC1ga9i5evFy07sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/12901" target="_blank">📅 22:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">المانیتور: تیم ترامپ، در اقدامی قابل توجه، ایده ایجاد یک صندوق ۳۰۰ میلیارد دلاری را برای ایران مطرح کرده است.
این پیشنهاد در شرایطی مطرح می‌شود که پیش از این، تهران یک پیشنهاد تجاری مشابه را رد کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/12900" target="_blank">📅 22:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش انفجار دارم از‌ بندر</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/12899" target="_blank">📅 22:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/12898" target="_blank">📅 22:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدای نوتیفیکیشن پولای بلوکه شدست دارن واریز میکنن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/12897" target="_blank">📅 22:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تسنیم: ریز پرنده دشمن رو تو قشم زدیم
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/12896" target="_blank">📅 22:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/12895" target="_blank">📅 22:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">منابع محلی ۲ انفجار در قشم همزمان با فعالیت پدافند هوایی گزارش دادند.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/12894" target="_blank">📅 21:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12893">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cf89fccf.mp4?token=Z4IZP55W1IitnYSjMZ2cRgKAyrRKMso7AtgdaXZMZgHE-MnSBLFYdQhZBLNfUeHDGL5Ay3aRb7gRFQi0xHTnm88Dnn8R3s_bwya-klru8GqrVWDyApDZdAJi4rhJq1DUV5TcLZd1oLOKVdA9f8LuQ69aOGVk41-ksDam-YL_pybe70MjY0ckxPbAZxqM_U3ECHzwNx4e4dRILS4BtjQv7Gwq3F3ZgAYp2XvAu1iv2FNc2V4q9wuAPSqIcjSOa39A1aXWkgmWfrJ3ZquHWjDADqYgb8NqHLxKZ0J6N9-UM2t8k85XaxJbWWTc0W7NXhLv9mxivgVaxsm4V9-HnzUU3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cf89fccf.mp4?token=Z4IZP55W1IitnYSjMZ2cRgKAyrRKMso7AtgdaXZMZgHE-MnSBLFYdQhZBLNfUeHDGL5Ay3aRb7gRFQi0xHTnm88Dnn8R3s_bwya-klru8GqrVWDyApDZdAJi4rhJq1DUV5TcLZd1oLOKVdA9f8LuQ69aOGVk41-ksDam-YL_pybe70MjY0ckxPbAZxqM_U3ECHzwNx4e4dRILS4BtjQv7Gwq3F3ZgAYp2XvAu1iv2FNc2V4q9wuAPSqIcjSOa39A1aXWkgmWfrJ3ZquHWjDADqYgb8NqHLxKZ0J6N9-UM2t8k85XaxJbWWTc0W7NXhLv9mxivgVaxsm4V9-HnzUU3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدافند قشم همچنان فعاله
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/12893" target="_blank">📅 21:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امشب از ته وجودتون خالصانه از خدا بخواهید امیدوارم که ندای ما را بشنود و بهترینها برایمان اتفاق بیفته
🍀</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/12892" target="_blank">📅 21:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12891">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">سلام اين  مسير دقيقا مسير قاهره هست  . درست داره ميره ولى ما چون مسير قاهره رو بلد نيستم فكر ميكنيم داريم اشتباه ميريم</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/12891" target="_blank">📅 21:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12890">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a2a5d870.mp4?token=rpCnQ8PEMDfYig1twMdWeNil2qRnvmm0rydUV-TLoh05CtQEHF7wJu-OYxZb9mLzfg7C4srkrC2XBYmbbR89on5nXmFWqLrYaxzEsr20SEijNTUHzzQGcUEn7X0qY5qlBlJjw9e4s4OV2aNSM23PavB6-nKN0CLh38wYI2rYHfhuclGYT-kF5VNPN3UUh5N757GnVZPK_PQRUt2gTY63eKsWZpF9Src6IA-Ne6B4VLn2sOlyq-DMXKaljtvBwS2HnRc3dT1wNbFDLzjzYDAofbK5_QT4Q7WKiA5Ca8JzGii29Yu-HsQnSoOvDZg5L7rrwEH-1EWhlJCRQkx6SKBL8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a2a5d870.mp4?token=rpCnQ8PEMDfYig1twMdWeNil2qRnvmm0rydUV-TLoh05CtQEHF7wJu-OYxZb9mLzfg7C4srkrC2XBYmbbR89on5nXmFWqLrYaxzEsr20SEijNTUHzzQGcUEn7X0qY5qlBlJjw9e4s4OV2aNSM23PavB6-nKN0CLh38wYI2rYHfhuclGYT-kF5VNPN3UUh5N757GnVZPK_PQRUt2gTY63eKsWZpF9Src6IA-Ne6B4VLn2sOlyq-DMXKaljtvBwS2HnRc3dT1wNbFDLzjzYDAofbK5_QT4Q7WKiA5Ca8JzGii29Yu-HsQnSoOvDZg5L7rrwEH-1EWhlJCRQkx6SKBL8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ :  الان پدافند قشم
💥
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12890" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12889">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
پدافند قشم فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/12889" target="_blank">📅 21:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12888">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری فرانسوی: جارد کوشنر مانع امضای تفاهم‌نامه بین آمریکا و ایران شد
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/12888" target="_blank">📅 20:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12887">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤣
😃</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/12887" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12886">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/12886" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12885">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مدیرکل آژانس بین‌المللی انرژی اتمی پیشنهاد داد که قزاقستان اورانیوم غنی‌شده ایران را نگه‌داری کند
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/12885" target="_blank">📅 20:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12884">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لارنس نورمن، خبرنگار وال استریت ژورنال:
این توافقی که ازش صحبت می‌شه فعلاً یه توافق کامل نیست که تمامی مسائل از جمله هسته‌ای رو در بر بگیره
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12884" target="_blank">📅 20:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12882" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza Rohani</strong></div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/12881" target="_blank">📅 20:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/12880" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12879">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsa</strong></div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12879" target="_blank">📅 19:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/12878" target="_blank">📅 19:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12877">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرزیدنت ترامپ در اتاق وضعیت کاخ سفید مستقر شد.
تصمیم‌گیری نهایی درباره مذاکرات با رژیم ایران در دستور کار است.
نیویورک پست: واشینگتن برای گام‌های بعدی آماده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/12877" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12876">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/12876" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12875">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAm.ir_reza</strong></div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12875" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jangal bedoneh risheh (iG @yashar)</div>
  <div class="tg-doc-extra">siavash ghomeishi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/12874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/12874" target="_blank">📅 19:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فارس: متن توافق که تحت قالب «تعهد در برابر تعهد» تدوین شده، در مراحل نهایی تصویب در ایران قرار دارد و هنوز تصمیم قطعی اتخاذ نشده است.
@withyashar
کلان رژیم جمهوری اسهالی‌تو کاره فیفتی فیفتیه
🥴
🤣</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/12873" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فارس : ترامپ تا نیمی از پول رو نداده همه چیز باد هوا است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/12872" target="_blank">📅 19:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری فارس: ادعاهای ترامپ دروغه و فعلاً خبری از توافق نیست.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/12871" target="_blank">📅 19:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtKeOT-m9FrIY9vwFIZPz18bZN252ysZEsW405OzVpU2zOgcqKib5RQMfMaXuYiAHj85LGoi2S4vdgGGy2kUwZ5G04xcCin6IuhtCrZzwhtaTFULgiibl7diXaT4hYmfm1Bk5Tk35BcJeU6OvSQD67Y-XLD7R_sEp6_9W95F2ockrGN3Kt2EsYLSqrrsPX3ha3etPn5py-SkPU99dhfJ2RVPgocS_ydgYuWvsr3m2TEmfpMUG4RY3B0KY4LSmFaHJSG2iUJx3Z8Jac8pgfV5XCox9ZblodeiZxQTTjPpSonD2Rph85qRJSUbbeWmw6X0GTDKNm9BbHCacR4fS8LtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از پست ترامپ در تروث سوشال، قیمت نفت برنت برای اولین بار پس از 50 روز به زیر 90 دلار در هر بشکه رسید.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/12870" target="_blank">📅 19:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12869" target="_blank">📅 19:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگارهای نزدیک به کاخ سفید می‌گویند: ترامپ منظورش را در پستش اشتباه بیان کرده بود؛ او در واقع پایان محاصره دریایی علیه ایران را اعلام نکرده.
بلکه منظورش این بوده که اگر ایران با این شروط موافقت کند، آن محاصره لغو خواهد شد.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/12868" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسئ ادرکنی
@withyashar
معنی ادرکنی : مرا دریاب و به فریادم برس</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/12867" target="_blank">📅 18:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/12866" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۵ عبری: به نظر میرسد ترامپ با یادداشت تفاهم با ایران موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/12865" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
