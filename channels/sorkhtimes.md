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
<img src="https://cdn4.telesco.pe/file/GGkIGqFbnJ6O-gauj7hrjlUy7aMIl7r9Cm1z4Ozyu3KW9Roks5lFom6pGbBIXxfxO8jq3x3a34R5DpzpZnlMVFyF3bKUUomT4rvMI9EZxCUoPmP8EdS8zrvODRKQKwwRmMhKn1WwtrZ1_-7CjElfcY-ls6Q4bzZA3s8h123HMTaTFBFrUHoipdu7DpV-s4Y8Ml8XWo4YA-FZo6rLiCaa9qUPXnQPD6KtO6ZJ6wJKPJnrzweATmDf62iZHFFTLtTB_EBSSRNNNeqSVbLvmIA3dj6AmQ5YO15bHdoXX3UNDJhcBVVE8lpqQJZ3U7IDt7LmSmV6g2GBgyQpWR4vU1Vwbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 06:09:09</div>
<hr>

<div class="tg-post" id="msg-132508">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxgAzmB1ctCCxpHmj8vALuYV8WBA_qrdXbuPZ-zLJxaapvOjAkJnz7p-RHuhWu2fYl7LIsIx0I0Q3zOYhwsCiJ7Rbiu92VecQUsRK52dQYK1nMfy3CioWlrP55LGBX7EPTCgzAkD01RDS3RNjpKAhd8aLBbOxYVWTxIKrX4_bcuhDJgkMs6QOgrporlEib_jw7Ava3Maw9AzZaNQ69Szs-5SVnkYzkCsD0YbWiGfyUxrclsshUcRkdJsb3RhGv7A_PjJ80-AmC1y3ZvmaluFR7oYVQzrLtnfoLfKcQ9yK9iFvTdIL1N6JZiXveXqD_5abForP2CXpEmGNfS9vekC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132508" target="_blank">📅 00:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132507">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
در پی فشارهای تاج بر کمیته حرفه‌ای سازی برای تایید مجوز سپاهان، مصطفی زارعی مسؤول این کمیته تهدید به استعفا کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/132507" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132506">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SorkhTimes/132506" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132505">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=h8q3rl3XA0TLpSFMkvYnbZZpYNW1bX0h0PPZHJ_0NGdQoiF855FvAqAb3Vz9Al30Zus0cHmb1YK55KceYc8I23ca9t6PklnX9CXGIXU5ueDkIbKMrKHHrd1RkQWZ-hjVrTICnNmxIZSOs3o410FUYLMXD7wFOgUXkXQTsFerQiUsulhnicXqQiw7rzWluNCulaW2puhWf2Er4-nRKc_p3lYE984AJxDXnFEf-PhWhsL-BjDbwTr3YUVct4Eag05MqHKDVD-rJ5MenRIknHsKjRx5zs2J4O8v0_hs7J4SbbiBPvJqMgFC1S6UtZt9fRHw7t2C1r-3oigtXmcocTMrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=h8q3rl3XA0TLpSFMkvYnbZZpYNW1bX0h0PPZHJ_0NGdQoiF855FvAqAb3Vz9Al30Zus0cHmb1YK55KceYc8I23ca9t6PklnX9CXGIXU5ueDkIbKMrKHHrd1RkQWZ-hjVrTICnNmxIZSOs3o410FUYLMXD7wFOgUXkXQTsFerQiUsulhnicXqQiw7rzWluNCulaW2puhWf2Er4-nRKc_p3lYE984AJxDXnFEf-PhWhsL-BjDbwTr3YUVct4Eag05MqHKDVD-rJ5MenRIknHsKjRx5zs2J4O8v0_hs7J4SbbiBPvJqMgFC1S6UtZt9fRHw7t2C1r-3oigtXmcocTMrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت بعد از مدت ها برای گزارش بازی فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/132505" target="_blank">📅 00:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132504">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوووووری
🚨
مدیران باشگاه پرسپولیس در مذاکرات با چند بازیکن جوان شکست خورده اند و موفق به‌ توافق با بازیکنان و باشگاه های اونا نشدن/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/132504" target="_blank">📅 00:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132503">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
سپاهانی‌ ها از بهمن‌ماه سال گذشته دیگه دریافتی نداشتن، از طرفی مدارک مالی هم بارگذاری نکردن و گفته شده استیناف رای به عدم اخذ مجوز حرفه‌ای این تیم داده اما تاج همچنان داره براشون زور میزنه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/132503" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132502">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc9aa4117.mp4?token=oUEUOOnOjYSDsMvUXIx8-8ltC7f12JY04ZWhD9RDy_5O3TuVUdNfYLm071AMwWzXpLnM87FsYEuU_wGj2ffcD0bOTDa0-0tx4qxlKgBnIrgBtYPiV2kdOqz7PWhdL5fC4dlXKLNJ9F9MoU8MFP-eMiyQ2DETb33gP88yFtUiMtc_XKVtVgvPLrp5jdPcmzOvrHPWLGc1D_smzqgayxTdIOtAFU-zZ-RcNAJ6hM6l7fnGNRx_hKZ_h65gnC9EQMz29XDJvUFa0B8XX1AaeSuqV1NZeg8zrEywqt5Axoc4DcJMWUzktDHMoic74Jkwd0sSmNI4ogcHDN8aTkog1v8qCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc9aa4117.mp4?token=oUEUOOnOjYSDsMvUXIx8-8ltC7f12JY04ZWhD9RDy_5O3TuVUdNfYLm071AMwWzXpLnM87FsYEuU_wGj2ffcD0bOTDa0-0tx4qxlKgBnIrgBtYPiV2kdOqz7PWhdL5fC4dlXKLNJ9F9MoU8MFP-eMiyQ2DETb33gP88yFtUiMtc_XKVtVgvPLrp5jdPcmzOvrHPWLGc1D_smzqgayxTdIOtAFU-zZ-RcNAJ6hM6l7fnGNRx_hKZ_h65gnC9EQMz29XDJvUFa0B8XX1AaeSuqV1NZeg8zrEywqt5Axoc4DcJMWUzktDHMoic74Jkwd0sSmNI4ogcHDN8aTkog1v8qCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗼
لحظه قهرمانی پاری‌سن‌ژرمن در لیگ قهرمانان اروپا با خراب شدن پنالتی مارتینلی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/132502" target="_blank">📅 23:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132501">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
🏆
فینال لیگ قهرمانان اروپا| انریکه جام را از آرتتا ربود؛ پاریسی‌ها در ضربات پنالتی برای دومین بار متوالی قهرمان اروپا شدند
🇫🇷
🔴
آرسنال یک (٣)- پاری‌سن‌ژرمن یک (۴)
⚽️
گل آرسنال: هاورتز
⚽️
گل پاری‌سن‌ژرمن: دمبله  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/132501" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132500">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
بازی رفت به وقت های اضافه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132500" target="_blank">📅 22:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132499">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🛜
سرویس نامحدود Open VPN
یک ماهه تک کاربره 1T
🛜
سرویس نامحدود وایرگارد
یک ماهه تک کاربره 1.1T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/132499" target="_blank">📅 22:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
5 گیگ 150T
🔥
10 گیگ 300T
🔥
20 گیگ 400T
🔥
30 گیگ 500T
🔥
40 گیگ 600T
🔥
70 گیگ 900T
🔥
100 گیگ 1T
🔥
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/132498" target="_blank">📅 22:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132497">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/132497" target="_blank">📅 21:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132496">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/132496" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132495" target="_blank">📅 21:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/132494" target="_blank">📅 21:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sontpTcNIhV3BAZg2IUq0FkuHv8YLgQPcvsLTUlbsNG9NyPehmApEVnnDFeutJbIqbcCilWcn0tck9WOtJKfaTJKUS98ohTl4AXTpzsaab_6shS9D1W07xzjTm7vzkNovpoYZObEZVMixo8ykhW5hN98hpc6B0-61gYgoEIcN99nv5vuALM1QUZPbc2OxsRAeEHsItWRFNiZREPZqv3N1ndDFQ_yjs_jgPLcz0J-NagjE7Sp8Ehdv48VucbgNRs6oOQZuR-sfTycgDxsIWvLaoDa7a5LNj2go6TXMJBLBWz5sS3a-kKaY1cCXWx7TUBcLUYZp48NEItavDrU3_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Champions League - Final
🔵
PSG -
🔴
Arsenal
⏰
Tonight 19:30
🏟
Puskás Aréna
ربات تلگرام وینکوبت تو این شرایط که اینترنت زیاد قوی نیست خیلی خوبه، چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
به کاربرانی که تا قبل از نیمه دوم بازی در وینکوبت ثبت‌نام کنند بونوس ۱۰ چرخش رایگان کازینو با جوایز نقدی و شانس بالا تعلق میگیرد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132493" target="_blank">📅 20:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132492">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=E0FHsUDnG8R0MWcoXF6ojv4kxgWBXs5--p25NiIsd88S_TuWGeRUb6X3QLBUH-nx-7HIiO4G3FNEWOZaSPg6t66xZ4UVOsx_F3CVaRjqDih3gO1fG0NOAzkwWckR8eyAcZnZMjzZjbWDaSMjvZqsz7gHB8NiPQqMWTCR10DgyX-5BJZtlvBbE3fgqOy3vDfQ4m0pEhL4nMs2mZhU7W7Bbq77KbLHPtfR7q5YoYZMovjeN39G4URA-2SMCfJBqEAK9wH94DocAP5vSUp1_SKm6BRr5-P5rqz3612D29a-IESEh9zxkrg9qP8V3jgz5u4LDzL9hkicfmun9u0ZSyyQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=E0FHsUDnG8R0MWcoXF6ojv4kxgWBXs5--p25NiIsd88S_TuWGeRUb6X3QLBUH-nx-7HIiO4G3FNEWOZaSPg6t66xZ4UVOsx_F3CVaRjqDih3gO1fG0NOAzkwWckR8eyAcZnZMjzZjbWDaSMjvZqsz7gHB8NiPQqMWTCR10DgyX-5BJZtlvBbE3fgqOy3vDfQ4m0pEhL4nMs2mZhU7W7Bbq77KbLHPtfR7q5YoYZMovjeN39G4URA-2SMCfJBqEAK9wH94DocAP5vSUp1_SKm6BRr5-P5rqz3612D29a-IESEh9zxkrg9qP8V3jgz5u4LDzL9hkicfmun9u0ZSyyQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/132492" target="_blank">📅 20:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132491">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/132491" target="_blank">📅 20:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/132489" target="_blank">📅 19:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY20R1V6VPKM0z5rN95Z0Gwtz9Qons4t4AsERDSKRXmTE512yUiigmOpPUjR4AeHCrLiPx7A1SCC_I0BNxjcfJPbp4MtJ9DarnCrcVLskv868dvQcQ83nvbxMGpxQYpmGBGsJksvlALCqyXHc0tbgfFqjQlzhEwlUEvq1Kb02CqovTJfg5oUoaQCFJK8HDFxcrZwdetEC7ZMwtLRS8V-chnMKXtH6dEp6MQlsVzPQ69vRTG4PSbxGS30dZrFWYH5x6JQcbQ_lMmQvX_1dy08hMDFz3auGbr9PRUkZ7m0lQrgmVe0ONeKPKmfBiTV9zkkx3aAuZJIMiPpjHtL8--PpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/132488" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GENe2-5SHqrK8B-r6DTYQS-rZ22HD_IUd04GPbHrp2MVPw1AV9LlRCA4U42p_9b33amrkpw1LShExx7QfIDj-xzQJNEaKdTVLNtd5zgS3N_eYcanOjWzaGIpwHjIPTbdCsjSlNVUglo4aS8Wha3yVgMyCiD3lbOAjlGWaCSeIYc3W_u37Df6zw3jLADi3CWM-Im0sdC2MldWpyLPpHoajWwDFg4-XU3_Y1L3L1tZ3-0dPLxyz2P_GAEgPnQmCLlB7nXnWVrfrR20YPCTCuITVVN6s94zG6VKverLt6CvxHtZwXTy_5Of9IAChx_o828ujQeJlP-8EdsAlbaLQmqsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/132487" target="_blank">📅 18:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
مهدی لیموچی با مدیران پرسپولیس به توافق رسیده و به زودی با اتمام قراردادش به جمع سرخپوشان پایتخت اضافه خواهد شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/132486" target="_blank">📅 18:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132485" target="_blank">📅 18:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/132484" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
امیر عابدینی: فدراسیون هر کاری می کند تا سپاهان به آسیا برود؛ لیگ باید ادامه پیدا کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/132481" target="_blank">📅 16:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132480" target="_blank">📅 16:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132479" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=GUtoAvKhxeXspRGVUTWgnBauVhZ_ZPcZ45uAVbtP7s1AwjOJNScSj7-ii_4C3klWUsyg_0LEFY4IJu3H7VUpbnNYtmVMaSEl0P9g9uniQm1R758Ops658cYq1fTjBnypG7yXf6oM3Ix0fagQ--acYjyvuiaNePG5AnI-d6wz0WMD_jRCpIj8geyX7tF_XOti2NyDtExFFWG2Vx1Pi5x3c-C4fr-fY3RknZISNdyt7_xZhaH5GRRQS7Nuqhz2T_cI6Uexnk1mD8jET_K-WdM4SYxuu2tBP_v5fJ22uk1WJ_WvX3jBBtl3cJfBa6ppgcCm-ykkspgmpbYiwTTK1K00CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=GUtoAvKhxeXspRGVUTWgnBauVhZ_ZPcZ45uAVbtP7s1AwjOJNScSj7-ii_4C3klWUsyg_0LEFY4IJu3H7VUpbnNYtmVMaSEl0P9g9uniQm1R758Ops658cYq1fTjBnypG7yXf6oM3Ix0fagQ--acYjyvuiaNePG5AnI-d6wz0WMD_jRCpIj8geyX7tF_XOti2NyDtExFFWG2Vx1Pi5x3c-C4fr-fY3RknZISNdyt7_xZhaH5GRRQS7Nuqhz2T_cI6Uexnk1mD8jET_K-WdM4SYxuu2tBP_v5fJ22uk1WJ_WvX3jBBtl3cJfBa6ppgcCm-ykkspgmpbYiwTTK1K00CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی، سرپرست پرسپولیس: وقتی پیراهن تیم ملی را میپوشی، سرود ملی را هم با افتخار بخوان!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132478" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/132476" target="_blank">📅 15:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
باوجودی که فدراسیون فوتبال رسما اعلام کرده بود موافق برگزاری مسابقات شش جانبه است اما در تصمیمی ناگهانی و عجولانه، بر اساس جدول نصفه نیمه و ناقص، نمایندگان آسیا رو معرفی کرده!!!
🔴
سپاهان که قطعا مجوز حرفه‌ای نمیگیره ولی جدی میخوایین گل‌گهر یا چادرملو رو بفرستین…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132475" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132474" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132473" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-ZKwCwzdzLx-TcJcHbfacGWvJpnDZiu1Eq-D95Ze7i60RdV9sBDu7B69t-HVDuumSKPIjhy1uoemOl56uu3TwDkYxzVTBkoVRGReonkIMOfCSZSIijJ81-zPITeoaHEqyAtdSOp2wSj0G-bNnMt0km1BNX0cSUkihwf-ZgK1sRbe9nwN01ufM7QzgHE2rRf2zEXMJsxcoXy_yQU4aIlpLiStu_LTwGz7bH_tAqdi_y-sCOoacWrlOcFtfldSx1AENJi5gUN2j_g8H7_iUeJ0zNQrGHPPvidkjynLVTeY79dVKSAeqDffzdE19_Sbw1g_Dg7ZbXKfiUhnBpsldLBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
فینال لیگ قهرمانان اروپا
[
پاری‌سن‌ژرمن
⚽️
-
⚽️
آرسنال
]
⏰
امشب ساعت ۱۹:۳۰
🏟
استادیوم پوشکاش‌آرنا
🔗
فینال جذاب و هیجان‌انگیز امشب رو در سایت اسپورت نود با بالاترین ضرایب و بیشترین آپشن ممکن پیش‌‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132472" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فراز کمالوند سرمربی صنعت نفت: سوال مردم آبادان این است که دو سوم شهر بوی گاز پیچیده اما چرا پولش در تهران برای استقلال خرج شود؟ بوی گاز برای آبادانی‌هاست اما پولش برای یک تیم تهرانی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/132471" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132469">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc298e01b9.mp4?token=NFtuZ9oVs3CsvbtachlRSFJy5yiIJNsdKy8ROxGfv8IwgZaW52V1b7NhxcgX9PxoMn8cbLFrDes4d51nP-JhDiezzI3fBGz7QRsi8lr0wM1kU2Kqua9kkpBJXIf_nn5CpJwN8A9xRta5Qbz4aoien5YQKEjaPFNEVk80uCbKuO4uGubjE9_gJ5-MsBadwYWWHzIBQ0x0iDdPRHzl0yxXF5WAv6EekpWGVVBvoUfg9LwBDBngxe0n7hddKi4JDQ2VJLuu0uANkBFzR4xfEizl9VFgayNealJSlxspM7qVZ5jpJAXowUhK7ZuauiQUrymQ-9AXX52xPe3arUu6kOiwrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc298e01b9.mp4?token=NFtuZ9oVs3CsvbtachlRSFJy5yiIJNsdKy8ROxGfv8IwgZaW52V1b7NhxcgX9PxoMn8cbLFrDes4d51nP-JhDiezzI3fBGz7QRsi8lr0wM1kU2Kqua9kkpBJXIf_nn5CpJwN8A9xRta5Qbz4aoien5YQKEjaPFNEVk80uCbKuO4uGubjE9_gJ5-MsBadwYWWHzIBQ0x0iDdPRHzl0yxXF5WAv6EekpWGVVBvoUfg9LwBDBngxe0n7hddKi4JDQ2VJLuu0uANkBFzR4xfEizl9VFgayNealJSlxspM7qVZ5jpJAXowUhK7ZuauiQUrymQ-9AXX52xPe3arUu6kOiwrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آشتیانی پیشکسوت پرسپولیس: از سهراب بختیاری‌زاده انتظار نداشتم برای بدست آوردن دل هواداران استقلال به همه پرسپولیسی‌‌ها بگویید شما فاسد هستید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132469" target="_blank">📅 14:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
وقتی هوادار اسیر دست جو رسانه ای میشه و ارکان باشگاه و بانک شهر رو تحت فشار قرار میده ثمرش میشه مربی ۴۰۰ هزار دلاری با باشگاه برای ۶ ماه ببنده ۱.۲ برای فصل بعدش هم ۱.۷ این ک.ص.کش خان همین الان بشینه تو خونش تا ۳۰ سال دیگم ۳ میلیون دلارو تموم نمیکنه… ایرانیه…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132467" target="_blank">📅 13:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
قرارداد اوسمار برای فصل آینده ۱.۷ میلیون دلار هست دقیقا مشابه دستمزد پابلو وانولی سرمربی فیورنتینا در سری آ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132466" target="_blank">📅 13:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v41PbIs6NeUwkHyH3gwj5ZjrG4cBO6WDLlKAurLqqd7Qx3SH6DOcCYtmx5bmGrVoBZf-BLSwc1txblF18GwUzS8ggniKxo12qe0bYXX_tf7KJiH7SWrVyhUfg0exW8WJKyrcifelVup6GHUUvQuh24IKCB4WFoLdpOjI_NfLH685vkCpkjIFmReUqw2P4hZQ8rNF2VXOXRxnSjIsH8KDeAhfyM8SefPNZVcRNcvoXPSjq6dDBV0mj1ioBEoGqlZmA5cRpq9O1MuI9Hixwf5r5Npao1NDwiVfXaHPc0QiE0ODqlwjxd1zg5eSKRWjaNddLlZjTRzESTiR3QQ9WsIRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارداد اوسمار برای فصل آینده ۱.۷ میلیون دلار هست دقیقا مشابه دستمزد پابلو وانولی سرمربی فیورنتینا در سری آ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/132465" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اصرار بی مورد برای بازگشت؛
🔴
«اوسمار» استخوان در گلوی پرسپولیس/ ۳۰۰ میلیارد برای مربی شکست خورده!
❌
خبرگزاری مهر: متحمل شدن چهار شکست در پنج بازی آخر پرسپولیس باعث شد سرخپوشان تهرانی فاصله قابل توجهی با صدر جدول بگیرند و با ۷ امتیاز اختلاف نسبت به رقیب سنتی…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132464" target="_blank">📅 13:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اصرار بی مورد برای بازگشت؛
🔴
«اوسمار» استخوان در گلوی پرسپولیس/ ۳۰۰ میلیارد برای مربی شکست خورده!
❌
خبرگزاری مهر:
متحمل شدن چهار شکست در پنج بازی آخر پرسپولیس باعث شد سرخپوشان تهرانی فاصله قابل توجهی با صدر جدول بگیرند و با ۷ امتیاز اختلاف نسبت به رقیب سنتی خود در رده ششم بایستند. اتفاقی که انتقادات زیادی را متوجه «اوسمار ویه را» سرمربی برزیلی سرخپوشان کرد.
❌
در این میان هم کمتر کسی به این نکته توجه می کند که مربی گرانقیمت برزیلی یکی از مقصران اصلی وضعیت کنونی پرسپولیس است. ویه را که به خاطر دریافت دلارهای بیشتر در دوره گذشته پرسپولیس را ترک کرد و به تایلند رفت، پس از آن که سرخپوشان نتوانستند با وحید هاشمیان نتایج مدنظرشان را کسب کنند، دوباره گزینه شد و پس از قهرمان کردن بوریرام تایلند با چهره ای مدعی به ایران برگشت.
❌
اوسمار در حالی به پرسپولیس برگشت که رقم های پیشنهادی اش چند برابر گذشته بود و جالب این که مدیران باشگاه هم با این درخواست موافق کردند به گونه ای که گفته می شود او برای نیم فصل یک میلیون و ۲۰۰ هزار دلار دریافت کرده است و برای فصل آینده این رقم ها سرسام آورتر می شود.
❌
به گفته یکی از نزدیکان باشگاه پرسپولیس رقم قرارداد او برای یک فصل و نیم بیشتر از ۳ میلیون دلار است که با وضعیت اقتصادی کنونی باشگاه وحشتناک و غیرقابل تصور است. این در حالی است که چنین رقمی در لیگ های مطرح برای مربیان طراز اول پرداخت می شود/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132463" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132460">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
محسن خلیلی، معاون پرسپولیس:
‼️
شانس داشتیم که اگر بازی‌ها برگزار می‌شد، سهمیه بگیریم. باید تیمی به آسیا برود که سابقه خوبی داشته باشد و اصلح باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132460" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
بهادر عبدی، مربی تیم امید پرسپولیس: امیرحسین محمودی آینده درخشانی دارد. او می‌تواند در همه پست‌های هجومی بازی کند. می‌تواند حتی به بارسلونا برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132459" target="_blank">📅 11:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
المـاس ارتش سـرخ فقط ۴ دقیقه زمان برای درخشیدن نیاز داشت.
🔴
امیر حسین محمودی در جریان بازی دیشب تیم ملی مقابل گامبیا بعنوان بازیکن تعویضی در دقیقه ۸۶ وارد زمین شد که اون تنها در ۴ دقیقه زمان تونست با دو پاس عمقی فوق العاده علیپور و بار دیگر ترابی رو در موقعیت…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132458" target="_blank">📅 11:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
باشگاه پرسپولیس تصمیم‌گرفته است بزودی؛ قرارداد امیرحسین محمودی را از لحاظ مالی افزایش دهد
🔴
به احتمال فراوان قرارداد وی 4 ساله می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132457" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS_p3o13zNtAuwSISIN4_0g6OM8EncJ99mJ8F_hUvLzNAbxDC901ub6ghpledAizN2Au7X1PUbZSDkM4qoMlMzLGNeRa_-U6UxNmfs5mg1o2PqzeM_LkzEhggiMkF_tBLVnTHLVU48bh_nl2rWIFAujo5Noy20j0XN10V-5T7kVKnALRCVdHpsxaOhDyd1ffcTrpiFI4x-JeFAtVB2edEb8N9SudQGNW0UQD3RbCQQ8ZOGHNEf7qgzBrgI1k4ru9aCLeYvgl5Q9HldNdtx2BcWaeeEXBhNSrwsMHGGl1yShj2sctyYgMri7ImXQjAjIYu0-rXbTMjTnuPlX1ThZh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132456" target="_blank">📅 01:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132455" target="_blank">📅 00:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132454" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132453" target="_blank">📅 00:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
مرتضی فنونی زاده پیشکسوت پرسپولیس:
❌
آقای تاجرنیا از اسمش معلومه پولدار، بابای منم تاجر بود، ولی آخراش، تاش رفته بود جرش مونده بود
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132452" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚡️
⚡️
⚡️
برکناری با چند هفته تاخیر
❌
قطع همکاری محترمانه پرسپولیس با کرمانشاهی
⚡️
⚡️
فرهیختگان: یکی از انتصاب‌های عجیب رضا درویش در دوران مدیریتش در باشگاه پرسپولیس صدور حکم مدیر اجرایی برای رضا کرمانشاهی با رقم قرارداد قابل توجه بود. جالب اینکه کرمانشاهی فقط…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132451" target="_blank">📅 23:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=DAEtD7nlTYKhyLiRuJE--SvYsz6_0Q22RnOC6OIu_DtWHCL1FKV5kLfH4t376lArn8YrbWJpDCT-j2nfwrC49ZUsOsp149lijYcvWelioyyIAuBs92BKIkcETgYjYLoiUfy6rmDauDft3H-Q4uL4bQFwxHv_tydsqQyE1CqvvdaB5Of9o1O_eAzqD9NJR5wKmSwDiAvVyHt4h9i8v-JjMGQ2QpZ8Z3xHgPsXLg3Hi1JiwfgdvGh_GPjroVdblDmo3uf-lyOpkSFsmQK_RBHWhQ37BzIidD6CaV4jlWn0E_M_lmZVBss1EkWo7q85FZ8rztCS9pVAKTOjSrsa5PN22A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=DAEtD7nlTYKhyLiRuJE--SvYsz6_0Q22RnOC6OIu_DtWHCL1FKV5kLfH4t376lArn8YrbWJpDCT-j2nfwrC49ZUsOsp149lijYcvWelioyyIAuBs92BKIkcETgYjYLoiUfy6rmDauDft3H-Q4uL4bQFwxHv_tydsqQyE1CqvvdaB5Of9o1O_eAzqD9NJR5wKmSwDiAvVyHt4h9i8v-JjMGQ2QpZ8Z3xHgPsXLg3Hi1JiwfgdvGh_GPjroVdblDmo3uf-lyOpkSFsmQK_RBHWhQ37BzIidD6CaV4jlWn0E_M_lmZVBss1EkWo7q85FZ8rztCS9pVAKTOjSrsa5PN22A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
ریکاوری ملی پوشان پس از پایان دیدار با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132449" target="_blank">📅 21:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVBS1qq1lDOkjU_4nGtfod6Zn1KwJqE8T4p_SISuK-SKBsAiZfNkFO1BQ2l-UONIe55SDkjaIf16_LTV2UnOY41xmi1PzkuHYyNePUv8Lxa-IaDBfjcd4PQ6kcJHU-YWscqn9vnpxs-e7Vc3Q6ZuaW09wjdKfv_A7yHeSpbTWy1XZTWxhYB2t3IxC4GVUPg0TdIw_ElxiZO7XsFBmqIKFKSDtfzGkQ-SpTs19u1SGDbC_xhN_SOBqcQVDhnbqZYPB67V7_3X7B2Vxx3gTMe2GVgAb_NQoa5wwqEhk5mfDHoi-LJJJX2nxA_QWOkvQSxssxY_FB-Nhza8bb8iYcR3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/132448" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=poJczfp87naClicpeyA7ZJ5n9p2ARYkybf2BcWM89TLFglpe_h_R_cqtLWFgd7hUfHQ7UPQLqmG-BOrzFzYkOVJHvr-WN1Tica3JRxy5EPY1LoiKESLUmjXj5-uqsvVv8PVpzQyuKNBI9YodZAAJvACA3snhBKlscFIQyVWx4iwgEY4sX6Tg-rsz8PGxccT3Tnf72gVGvaRQLzuxNV_rk8spfb0Va9hfJSsdsQ09vqOtKTX3Nj_-z3kU-diPsvrH1UQmGp1KiOalmoBLSqWKmefphLvxGXwcAisKCN7vEtD7L-erS2Zf963_hBCIihinYvBPM2-ALd8TNPvey2AtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=poJczfp87naClicpeyA7ZJ5n9p2ARYkybf2BcWM89TLFglpe_h_R_cqtLWFgd7hUfHQ7UPQLqmG-BOrzFzYkOVJHvr-WN1Tica3JRxy5EPY1LoiKESLUmjXj5-uqsvVv8PVpzQyuKNBI9YodZAAJvACA3snhBKlscFIQyVWx4iwgEY4sX6Tg-rsz8PGxccT3Tnf72gVGvaRQLzuxNV_rk8spfb0Va9hfJSsdsQ09vqOtKTX3Nj_-z3kU-diPsvrH1UQmGp1KiOalmoBLSqWKmefphLvxGXwcAisKCN7vEtD7L-erS2Zf963_hBCIihinYvBPM2-ALd8TNPvey2AtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| رسانه اسرائیلی:
🔻
ایالات متحده و ایران در آستانه امضای توافق هستند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132447" target="_blank">📅 21:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
تیمه گروهبان از گامبیا گل خورده و عقبه.گامبیا با ۱۵ بازیکن اومده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132446" target="_blank">📅 21:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
علی علیپور پس از پاس گلی که به مهدی طارمی داد به سمت قلعه نویی رفت و او را در آغوش گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132445" target="_blank">📅 21:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1699b581.mp4?token=I7Qvx4TByVrUCjbdoBJ-NX5B_Mz3d5A1RBaeT57yJVTK-h4PwTSnDlqV___inBHAjnHlVZgTRb5QrRROP9WsC2slD-T1btRQJDkxE1LPxHveICKZNhA8kH39YNYTXygSQnzDOReg4YWJ93nhchmJeh4rPinE3MxyBNv1qpnRdD7pPItm1dnLmMwBMpm3_0lXDALCyiApedve6kTN9__ZlaovgOsokJDqk4kMr7Gp6XecJ0VoNAeQHGt9l0MCAyInFyX1A_s0FZb9DLVdSKysXpDOrH48uFp3GjJ58NgeqYSTPsEDu_Rs3KM6te0Eua7P2y5UV8Yl1gIPEK8EYzuM0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1699b581.mp4?token=I7Qvx4TByVrUCjbdoBJ-NX5B_Mz3d5A1RBaeT57yJVTK-h4PwTSnDlqV___inBHAjnHlVZgTRb5QrRROP9WsC2slD-T1btRQJDkxE1LPxHveICKZNhA8kH39YNYTXygSQnzDOReg4YWJ93nhchmJeh4rPinE3MxyBNv1qpnRdD7pPItm1dnLmMwBMpm3_0lXDALCyiApedve6kTN9__ZlaovgOsokJDqk4kMr7Gp6XecJ0VoNAeQHGt9l0MCAyInFyX1A_s0FZb9DLVdSKysXpDOrH48uFp3GjJ58NgeqYSTPsEDu_Rs3KM6te0Eua7P2y5UV8Yl1gIPEK8EYzuM0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مصدومیت شدید کنعانی در جریان بازی با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/132442" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132441" target="_blank">📅 19:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
گامبیا حریف ایران فقط با ۱۵ بازیکن به آنتالیا آمده است!  در بازی دوستانه هم به ما توهین میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132440" target="_blank">📅 19:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132439" target="_blank">📅 19:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132438" target="_blank">📅 19:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132437">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132437" target="_blank">📅 19:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132435" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
شبکه ۱۵ اسرائیل : به نظر می رسه ترامپ با یادداشت تفاهم با ایران موافقت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132434" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132433" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132431" target="_blank">📅 18:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132430" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132429" target="_blank">📅 18:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132428" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132427" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132426" target="_blank">📅 18:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132425" target="_blank">📅 17:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132424" target="_blank">📅 17:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎙
🔴
محسن بنگر: وقتی که نمی‌تونیم حتی تیم های اماراتی رو ببریم چه اصراری به حضور تیم های ایرانی تو آسیا داریم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132423" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
سی‌ان‌ان: در این هفته خبر رسید که ایران با آخرین پیش‌نویس پیشنهادی موافق است؛ دونالد ترامپ به مشاوران خود گفت که برای تصمیم‌گیری درباره امضای این توافق احتمالی، چند روز وقت می‌خواهد.
‼️
به گفته یکی از مقامات، به نظر بعید می‌رسد که ترامپ…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132421" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132420" target="_blank">📅 15:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178f9cb33.mp4?token=L7hSXqvh5rs7gMdOGaD0cBp1bvdxdqiNT4N4w4S64spTtHWGHlBzl7Mf8cuPb2lCyzsLEWMl5Vkq8NXva9Go3Yb7yoIq0yyjJYpHzZ_Ck4VCbEhoA4hJcrMZLJ5U0sKgD_ewG3zNX5k_v1peS3_FY7SDOox8rThWxdN7LlPv9yi6HFskBV3chr0deyzR4ZQGrmjiW9-HfUAFbkdGb_GsiFmXBzRg3o2XaQfWcacYuKBZ1xvA9oly4x_DvX4ihAbqfO9KNd4ZfghQScjBgwsjSIgNuU14yjdE2NkHnNZQ3g_tQ9LZw7tecS7FHIWtzN1x7s8LDhRStOSsbBHrQsIcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178f9cb33.mp4?token=L7hSXqvh5rs7gMdOGaD0cBp1bvdxdqiNT4N4w4S64spTtHWGHlBzl7Mf8cuPb2lCyzsLEWMl5Vkq8NXva9Go3Yb7yoIq0yyjJYpHzZ_Ck4VCbEhoA4hJcrMZLJ5U0sKgD_ewG3zNX5k_v1peS3_FY7SDOox8rThWxdN7LlPv9yi6HFskBV3chr0deyzR4ZQGrmjiW9-HfUAFbkdGb_GsiFmXBzRg3o2XaQfWcacYuKBZ1xvA9oly4x_DvX4ihAbqfO9KNd4ZfghQScjBgwsjSIgNuU14yjdE2NkHnNZQ3g_tQ9LZw7tecS7FHIWtzN1x7s8LDhRStOSsbBHrQsIcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132419" target="_blank">📅 15:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132418" target="_blank">📅 15:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132417" target="_blank">📅 15:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132416" target="_blank">📅 15:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJb4lP0MsItuIKOFCpyzNvYrlabMkqxc646oe7xjMvY1GkxS1TUV9kdbam8EUp8vC8_oeAx_rf5jKkeXmwUBsjUUsc2bSYRzWwOs7ZyPUBcBo9hnqUyUwOKclHmK2GYlkFrpAV4yEyP_HEt3UUWHUejJEyZHsDMtgZlOOPRLHYN1h7kABqd7g1_4zF6WQFrkdD46ZEF5ElK_LhJBQCxJx1IThdkbWhpxSD55otzMwgvYR4Y4uDfKuTlyK8HxTxZgisvwMYAF0ok3tNSCK4zhouT-0hipGgVlbIaa6_B8XcrV5yt_zpLaC_lnz9Cs5YFxq8D1B4uE7iQwu2Z23pwdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132415" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132414" target="_blank">📅 14:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhneXm9CIT_Ut8ZW8AyhIV5aBTHVL6xvDUxXzOZA50skgxkjep7QIeh4mzP_2sJH40dJ916Sfneqyl2OcmEor_ZVbmiNu0eEBBz305DZx7-yMuQmFtB-XL6cAmhTYc-34-WfJ4uaNUrZXrwe9ow-K8xVwfVs4z_Bw-Ao8zUsKd_2tctzANSbFhkg2ZgWf0qQetpJM5Xc2JUXbSwynXZ9JQLbV00BjWaEV4pyP_ICLCugQ5XAJeOqC6W_qTzXCxeuDrVD2yJkJzyPZxEfrd624jEEyULbgoCnIZWyaHi-9dOiLZ9aky6wKfKkWkm9YdUcfHrODsKuZXttYqF-peX7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/132413" target="_blank">📅 12:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132412" target="_blank">📅 11:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فرزین معامله گری، علیرضا همایی فر، علیرضا عنایت زاده، سهیل صحرایی، محمدحسین صادقی و محمد گندمی به اردوی تیم ملی امید دعوت شدند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/132411" target="_blank">📅 11:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
مدیر برنامه‌های اورونوف به باشگاه پرسپولیس اعلام کرده که حاضر هست قرارداد اورونوف رو تا سال 2030 با پرسپولیس تمدید کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/132409" target="_blank">📅 10:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132408">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KY4iI0DKzn2dueLjcjjv7xrGW3vGUdenqXXQLVT5WdPINOJH8ugAxZ0JGFYVJA3hpAv0akvIelQbbaAemEyZH3hvZ-9opwQlVYSlC0nOyjpXM0sJu0mPt13MZ6Dv79Mt08FvtUnTsjGo78oeS15skfm1NsSWkqMD3OXWqpsa-BpoLlEY2EUFWoStF1OzyBksKz5eIyGIIQw8kGG9G7JHQF4s2nbmbyiDudQ6Bq6nvG5UzCnETqOOdfkzAjp77N20a3UtM7YZfLy2JX_FBu5ifdKc_8ITsUlWvXTM5Dc_u9P9exwnI0yihOWDyVqCMrgi-v1XqXpZJTuZs5s7xXUVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوسمار ویرا به سبک بازی مهدی هاشم نژاد علاقه‌مند شده و به مدیران پرسپولیس گفته است تا شرایط جذب این بازیکن را جویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132408" target="_blank">📅 10:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGhr812mMbycn7r4C1md1W3qi8ITDjNBirOT6-YmgujKm2dx3Tr4kqs9zwBF2TNzAB2NKONxzPrnl1OCROUuKCwTWyasF--JDazmEBG5KhOp4uc11rh9tQOryQrneynUl3obBFBybAzQIVruHYIiOaBv7Si_DYbVihHJFv7rMWlTc7jv55JJKXtG0etpUE7yUn_uSYC0UKtoROujrd1JOeaO-NqagkdH6sQ83r2tSpQm3ZnTyMhlCYopIY0_gGFJokzE38m-NTnnfomJSKfpZ562SSGEAsy_Izk8J_5jwWQFaxEMMwiNOjIT2RexhIKN8zP3De8FvdcJOQGaV6D7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آریا یوسفی علاوه بر پرسپولیس، از تیم الشارجه امارات نیز پیشنهاد دریافت کرده است.
✅
ترجیح سپاهان این است که یوسفی را به یک تیم خارج از لیگ برتر منتقل کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132407" target="_blank">📅 10:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132406" target="_blank">📅 10:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN94eQ7MQM9CiHayGWwIMW-8deuGD8Zy-7uKlRWPgB3UurnEKYnGE2CS5H7erJQ9Y_XK5AZDdZ0LLWWFjaqnnE_kXf0xoO6NmJAkSTKHcE4y_CzgevKqlY5iViojWG4lBHnNlmStDvs2hWktuftt0M44KfH231dAufpct2I3rnFoUPG2sYjtDJzQSxo6HtacK1fYB4RmT1ZPWDNSPNSVmMPUE8WkJFtdYTEbYUX70LL9_337urY-yMKkW_hmbu9NfswujHRH54f21ybCEmxkoofqEgQbhoqWaGlpZVS0S99LlwZ3dOAGxLlB8Fv75Qhh6alzayebnPmxIbZXzxy9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار ششم از فینال کنفرانس غرب رو بین دوتیم سن‌آنتونیو اسپرز
📀
و اوکلاهاما تاندر
🆗
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/132403" target="_blank">📅 01:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
خودمون رو گول نزنیم ، بازیکن خارجی با کیفیت نمیاد تو کشوری بازی کنه که ۴۰ روز جنگ رو پشت سر گذاشته و هنوز هم هر لحظه امکان متلاشی شدن آتش بس و آغاز مجدد جنگ در اون وجود داره
🔺
اما آیا این اتفاق و این جنگ باید بهانه ای برای انجام نقل و انتقالات ضعیف برای ما باشه؟ نه به هیچ وجه ، جنگ پیش اومده ، پنجره بسته استقلال و مشکلات مالی سپاهان  باید باعث شه که ما به سراغ بازیکنان جوون و تراز اول داخلی بریم
🔺
امثال دانیال ایری ، مسعود محبی ، فرهان جعفری ، مهدی گودرزی ، پوریا شهرآبادی ، بهرام گودرزی ، پوریا لطیفی فر ، کسری طاهری ، جوون های سپاهان مثل لیموچی و حزباوی و کلی تلنت دیگه تو بازار داخلی وجود داره
🔺
حتی لژیونر هایی مثل محمد مهدی زارع و امثال الهیار صیادمنش که جام جهانی رو از دست دادن و نمیخوان جام ملت ها رو از دست بدن هم میتونن جزو گزینه های باشگاه باشن
🔺
این پنجره بهترین فرصت برای پوست اندازی و جذب بازیکنان جوون و تلنت لیگ هست چون رقبای متمولی مثل سپاهان و استقلال در بازار حضور ندارند و پرسپولیس و بانک شهر در جنگ ۴۰ روزه دچار مشکل مالی نشدند و اکنون وقت خودنمایی پرسپولیس در پنجره نقل و انتقالاتی است تا سال بعد با شایستگی و بدون حرف و‌ حدیث به قهرمانی برسیم و به لیگ نخبگان بریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/132402" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47978b8339.mp4?token=uJdusDJBuQxuc7FBFN5wSGS_7323p2C5l9aTB1LyeIdVJRgaTsBtWdEHKE3biELPZ9aYW4smRzVPdk82ipDh3oiZqqUvZC01I_hBPylhLGT8ceF-crkKOd-B-KKRcDYhAm-7PBYPrGL9jgMYl5c_xt_rX0LF1kMei89stb4XWiF0ozdFqrkS6-4qfeNLsABByc8699ajP04DNRlVTvWe6Y1A5O1eUuDAW4pT0apdCAuyOr4Odfuu2z85vBxdhNAJGkvn_ICzjKf9VViz2S-k0GB7G3lNIfH2P_QKdbSAsTIhcanddB6imE-uqxPcTSWjgEjkklTMgm8L3IJYS4gCDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47978b8339.mp4?token=uJdusDJBuQxuc7FBFN5wSGS_7323p2C5l9aTB1LyeIdVJRgaTsBtWdEHKE3biELPZ9aYW4smRzVPdk82ipDh3oiZqqUvZC01I_hBPylhLGT8ceF-crkKOd-B-KKRcDYhAm-7PBYPrGL9jgMYl5c_xt_rX0LF1kMei89stb4XWiF0ozdFqrkS6-4qfeNLsABByc8699ajP04DNRlVTvWe6Y1A5O1eUuDAW4pT0apdCAuyOr4Odfuu2z85vBxdhNAJGkvn_ICzjKf9VViz2S-k0GB7G3lNIfH2P_QKdbSAsTIhcanddB6imE-uqxPcTSWjgEjkklTMgm8L3IJYS4gCDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری صداوسیما:
◻️
آقای حدادی چه گیری دادی که باید حتما در آسیا حضور داشته باشید؟ حتی اگر CAS رأی بدهد و امتیازات تراکتور و استقلال کسر شود و سپاهان هم مجوز حرفه‌ای نگیرد، پرسپولیس به آسیا نمی‌رود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/132401" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/132400" target="_blank">📅 23:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_0y4-tD-Lx-bIfyxa6B07dZOx43725Vhng3mMCI4Z1H5PlNbcDqVKQyWeygREg3Hl_lp-SuT3hLhXvQ6CfVEQmQHHSIC-9s0lYK7TaJYhC4fsGMoZEVP7oBH1tIvqO7_L6EoylqcF1l2MDh-2zOIWKnM5MBPcS55KpimnZEl9fiuLIu9HUnDuxcInq0pynf0hd5h-lj7Ld9z3x5ysjknxYXNsxwLUaHU61PKEM4hk6qiC0szr18kJlotHfI60gs-My3Q2QLT7lNZAnP1eP_fgE0QVPrtEKLF9Aih94HS53AO2CQ7xCnJeXKsy8pKvFXxf7PyW4SdwivewF0pjNj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی:
اگر با سروش رفیعی و میلاد محمدی برخورد نکنیم، توهین به بقیه است. به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/132399" target="_blank">📅 23:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132398">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس:
🔺
بیشتر پیشنهادات ایران در مذاکرات پذیرفته شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/132398" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
سی‌ان‌ان : ترامپ تو تلاشه قبل از تایید توافق با ایران، مشورت بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/132396" target="_blank">📅 21:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf8uF1Fajlw9pDFKV3apfqbX9BiYZoD3_lTI00ETmHTSqSBAUYypUJLNQglroLYH0WZxQyOTPhm2pX3FXOJaz_UnYKAmVaEvRdl4vKMkH83uUkr5xmr58G3AAiWtOok1hMFyx9wY3PR_HR5XwiCyVIx6GJy5i85XM2qtftwLu4bztvxM59qeNwZmNwQpHxWn_etkITlh3LncwfVespsy1D1IgTwRm5KkC_2f-xqKuhroSMzFKgRdkjNdw5XZT_kLq8tVSHIDxLqNAOpJ7xNpreMpWmp8kZIUfhbpwwV22sPJ3p3fDdfeyX6t39iPyFWIHf_gc6lcHgdDukIGWmQ9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/132395" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132394" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I0EM3wC8dSBOmUdceDPAhKYuA_cbu8kxUAqIhuRJu6YP4HwPff9YiRHw-mZ7r48s2yOgEe5dS624wJ3VxzwIrjcZEvV2pDTzXq1Llt7YkJW7bN3h6z5p0apFU4_XYHqbc-7gG28csRzU6gc5Jd9ngKGBklWCXUlqGouVbfYaloqNMrzZIPot6yfWTqx-g-T4fbYZRcA46Dn6oV5BDC3TlVcbUCst2Mq5merAuKtAhaiohzrJ2FAO9VHM8oVr69v98R07s2zXBpPB94_O-ptJL1TrINGLZjKBIySgJQlw8zU-Fh5AM5nKIJf6gT9nGGmUgE1k9_Mfrf1YGXUBDHYR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشور های دارای سریع ترین اینترنت موبایل در جهان
❌
ایران اصلا حتی تو لیست هم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132393" target="_blank">📅 21:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132391" target="_blank">📅 20:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5B6whICQQI1EItIZ2OMH57-i9jX0ZsL9B4ZyrXaPWlLVtxN9nnmRLpkjxm5ws9iu0jYjRheJxD4IOaCP1sgC0YdYpneNmlVvjOfU8OSTCYxdIDsoz6P4-DPZjRZ28zWGVDcRHjIyMjA9w5fE5PsmAEcMxeigjbsDM_w_0kh6GbsTzXFJRR8QuCJQkEdPrQ1O70FCQXDp8S_UAG0JBG41E6dNa-_Z5Y-N-_2J27aunphb-gV-yGOGlaH56OP3hf9tYkZBc6ZbXOz2Ij2vH-XNgVxrSkKEig2QwEqb4NAdC8dP2YUVCJihVTZkaFxxkvEutmVPUCKIGjZ--q-VA2xrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132390" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
