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
<img src="https://cdn4.telesco.pe/file/AfMrgG01xJH-MwcF9HJdRs_4JsjKxzD-mmumJ8ecONi6I6JaVJQrOnT-B4m3H2upesWEwqCUMqOv8cSEXvIuS7uzuCxSG7LWIWrArohJuWh9iIcciLD88EoUFB1pWwlBAaKSXuGze-4mDn9N6SzHh3ZxTFpXSe0KLx-7kcwHlv5rvu5TWja07ZR9Xdx9uULkMyfK93NLMcU4E6DzsDDdinBtwA-5oeFPKKB-UDCSPpxsTB2IC6rgX15Ikfe9OLYdcsz4sZSiqlAEbVspH9d7PiuaF8qgIWCxJ5FxLtc3vX6fXzn90Xb5TXO_KZdKWqTdy7Ct7Huo6maFZBYaEfzNAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 09:36:27</div>
<hr>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAzhteIX_E-5ljSn_cmQnUmaBcwFy-fpaEgZHE_lQBwncSgleDIsUHKUYyYaIfYhdRVNETAESwbj5E2BLNWHyAzBh0XXVnT0tGtpaaGTHO0wd4dLRk7wuEXgl4ZGVuzVFqZV_mI5GVisouAKzuux247KPTGdPCAhITjI11kk22YyUkTtAWki0DgEoulVMFhDZKVpIAYhkms91vZ1cg_-oJ7wkYrWziOBhAdHcyc5SxMstLtkHz6Y0Syljtvrk30ZTJ6rcgGLOFqN6iLtqU5TlD7myG3o5ehoYh3x0GzCbbgVGFR7Atr0Gf5QNG-Usml7GJRQGqZ0VCiLm5IblVmiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره
و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 514 · <a href="https://t.me/SorkhTimes/140903" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭕️
بهترین لحظات پرسپولیس در لیگ قهرمانان آسیا در سال های اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 561 · <a href="https://t.me/SorkhTimes/140902" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140901">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvk8JSV6tGd6Qq6XYKDch5PQDpnQpPc-pFXR9g5TvLvJL8rv2mYGrukvnpmAK-ku9p1faoOqUlMj9pw-cqQCriQQlaw9eZYEhJgR67ubXwxEXtpZWetpSJYaje6bK-4hIJbhQe8Tbb2KYmTrHIiix8wijTs1ZfvVSUcvDDuPBL11Jxg2SSOxVN67rTMXhzuwe-BtpijOVrnfUJDLJ5Hcbwo21gcSmFgTRId8sPWSPDOS7zESooseDy0Pm-8JCotbOePargWKZ_8F6l8mxi3072SxN6y17YLHkrT6oCU1fIF03rTFvKWwPzd9KhKaGdENWrGyONowfqrQIpT4iFIBIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 575 · <a href="https://t.me/SorkhTimes/140901" target="_blank">📅 09:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140900">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">■ دیگه دنبال لینک سایت برای ورود نگرد!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SorkhTimes/140900" target="_blank">📅 01:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140899">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/140899" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140898">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
از این پس امیرحسین محمودی در پست پشت مهاجم بازی خواهد کرد/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/140898" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140897">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/140897" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140896">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FizFpYGUNdptJcQX8GwtwkbhyX1-073pZYQIAFBiKIVHXPR087oDQPpCNScS73PAVG2PAQ1x7sTIQUdx1XZ1a-M_hQDSI1EFQy9Qhu9TR1ibySHj5x9fux2NW8iuLH4KegzzUd0er_7LvOLTyAkEKWMJVK33FRsaRd5ZwUd-mf8gJwbNe5hup_IiQUxHd7mvCTmxpDhMvr1x2jWokHMg9Kgqv0tW-WzNdtfBhfuF_jsh4R0g9jw-uzPt17iI8oqAxtzRdZ-2mMEmAfs7_0cZlvRxLHUgeqIC7SgKjPkmRtARpXYnWmQL68Ns6sg8xYlAHd1rKFNKDpk9aYSLxIwdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⁉️
‼️
یحیی گل محمدی به دلیل اینکه باشگاه دهوک یکماه در پرداخت دستمزد خودش و بازیکنانش تاخیر داشته اعتصاب کرده و تمرینات تیم شو تعطیل کرده:))))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140896" target="_blank">📅 23:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140895">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
✅
✅
احمد دنیا مالی وزیر ورزش:
✅
✅
فدراسیون های ناموفق رو حتی شده تعلیق کنم میکنم. این همه هزینه کردن که هیچ افتخاری کسب نکنن؟
✅
✅
گفته می شود حکم اخراج قلعه نویی توسط وزیر ورزش صادر شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140895" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140894">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏆
🏆
اشک شوق قهرمانی و معافیت از سربازی
❌
❌
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
❌
❌
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140894" target="_blank">📅 22:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140893">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
گفته میشه که یحیی گل محمدی هم یکی از گزینه های جایگزینی امیر قلعه نویی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140893" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbRDJmvpP82Ef2-vt1x7IRfAuoBV7bUfW8ayeSye0xsrA84vaDSFLg1f5Cj1t0EP5NfRJomO_gzzgnwTFTIgKCN4vh773tUkRkBpQs2l6BsAChTGBvKZjBxxZiPmEDGUshhBNDU4OaqwL7VVtFXX4zhIyW8veHeGFbGjB79XP3ckvYB2rO4uJ0wJ-FsBBtM_H0QeRgPqHDpMyylhJHBSDII4Z9uy4k-M_5f02wBg0Wd5CZY-tJhju8ddLKr09-czNV3ASlqao64x--4EofCTYmhO2hJzVkEOpnQTXHJOllfIlb-ammPUoVK-qYAVM0ILAOSuEZOyxEnM5HpV_wJ0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
محمدرضا مجیدی، مدیر ورزشگاه تختی: چمن طبیعی برای ورزشگاه تختی کاشته می‌‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/140892" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCz0B0mm3yxB92-nBGvYxy-pwMb3RSBBI82tqKMD5PbJ93W5k2h5OMOecuXvQ7oK7q2Y7-6G0-UQCEjvMxaJXZA0yPfBZYRU4O1cg4VntOGo7CxEgi4phEm78v5pRCHowrD6Ay4p5hOH66K8-miShVxOhPybT5YDmVfYiyRlyxkgoar6X2Al86Vik4c4xpaHPJdHgtxI-IZI-qBszseZcWOJXSYNfFc3Yn2t4V7OQ71B-37fi7YEDOPOrt9s4bbxCShN04mFeM3EpjogqmQ8RUPyvdVYdtAN7mCrHPpATt7IRzixhJM87Xh-Zbvl-WQ2I0eKvrjXcXy9YHljM08sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک قدم تا سومین برد؛ لاروخا آماده‌ی شکار!
[
اسپانیا
🇪🇸
🆚
🇨🇿
جمهوری‌چک
]
⚽️
اسپانیا با ۶ امتیاز و ۷ گل در دو بازی، شروعی کاملاً هجومی داشته؛ چک اما فقط یک گل زده و هر دو دیدار را واگذار کرده است. میانگین مالکیت اسپانیا حدود ۶۳٪ است و در ۲۰ بازی اخیرش به‌طور میانگین ۲.۶ گل زده؛ در مقابل میانگین ۱.۶ گل برای چک ثبت شده. اسپانیا در دو بازی اخیر خود پیروز بوده و لامین یامال در هر دو مسابقه گل زده است. با توجه به حجم موقعیت‌سازی و اختلاف آماری دو تیم، سناریوی بازی می‌تواند برتری اسپانیا همراه با حداقل ۲ گل باشد.
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140891" target="_blank">📅 21:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
🔻
علی علیپور بعد از سپری کردن دوران مصدومیت به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140890" target="_blank">📅 21:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
۲ گزینه پرسپولیس برای لیگ دو
✅
✅
پرسپولیس بعد از ناکامی در راه‌اندازی تیم «ب»، حالا دنبال خرید امتیاز یک تیم لیگ دوییه. پادیاب خلخال یا شایان دیزل شیراز در صورت توافق، امتیاز تیم به تهران منتقل میشه و زیر نظر پرسپولیس فعالیت می‌کنه.
✅
فارس
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140889" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aftjj-DS4Z__E2QYyubSQU-pw7-8fSPxrRnRXMD0sldejOALDgE8m1sxInNkC4Sk52wT4FjBsz-JxTY-GI5g_uWK6gJHKtHGt4h_Zm9ZRZnccXAK9ZRtOoGSqSMR9zHZC2rRMmx1pVbod-5YoIPnljcWHCB_I8CDkyGcMpHHuVh33R_2l8P2MKxkpgdLeSc83AwYeCHw6m4AEgX2WFvwy_x6JO-NZGJ7gvXJxPN6GFgy9bhd3BOX6V2l1sArOqtoMn5aKnjs017YMhSsQ1ESni83ddTUxn4Zleiull-iqzkKQiLAq399G_Q3k1ofdkDGR_J-dszjaxUyjGWO42F_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
علی علیپور بعد از سپری کردن دوران مصدومیت به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140888" target="_blank">📅 20:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140887" target="_blank">📅 20:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
⭕️
بخاطر کمبود گاز ، از اول آبان به مدیران ابلاغ کردن کلاس ها و مدارس غیر حضوری و مجازیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140886" target="_blank">📅 18:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
⭕️
بخاطر کمبود گاز ، از اول آبان به مدیران ابلاغ کردن کلاس ها و مدارس غیر حضوری و مجازیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140885" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140884" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/140883" target="_blank">📅 18:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/140882" target="_blank">📅 18:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140881">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140881" target="_blank">📅 18:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140880">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ar5av3iZL4rS4bIFLUff4kpBFYaKNvSw51NHrSu94rie36NS-MRX5OWjWl5v54XvZhP4-OnmkCthzV7Q4Rzxnm2iAJDc-Rya30SuPZvTm7QoOEltIty4Vwm1qELI1jwIYGFgHLuz2BFuffcPIIEADxWA3b4dQDRGGu6qf1hODJ6Eku5e55kItx1bLkHH9YqxzwK4G0ZqKXxfDL5JyKokaM7jy4DRR_T25HyFWk4nvMg7dfuL-kCDKbWK54an2c8wT5DMXpYzB42rPAHP6x3CrwGdLu7dUfa7lc5p6-bLmErxB1PUY7OCsbKbFZvqQ0TnTzqroMW42fqbW2ryIRfiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
کاروان ایران با 19 طلا، 18 نقره و 15 برنز و کسب مقام‌ششم مسابقات آسیایی ناگویا رو تموم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/140880" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140879" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140878">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140878" target="_blank">📅 16:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140877">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeWcuQ2jRh2O4Cf_3tm8BlAipQ033ggO_gkGVbo1p5uiBK9IZOs2p5HR9A72toQHl7VLSEMrg3qe_UBfhFTDUz-FL9S1xAxmJt2dLoI6L0yBTx8n0tfIQbmIR7JZzd-nsQZjHRx1GwNakuf_oZ55P9_FApOiZTjkVGOUXCnbpus4SQgw6M6N4Zt0uUhMcKBfDMQfg3eB5Nq2nNlZ_hmUZChBSMqTBeZUCEr_Wzhu8j_H9EHSXhMuvIrBcepUS2Y-QUx0xkv0OuqIk4iqeIgmKvc-mmT2tjKQa-r1meSOj7br7HQpdQNz0tBzDiHzpKFyW5P3_c0wZJAQHcMk6qGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
SPAIN -
❤️
CZECHIA
⏰
Tonight 22:15
🏟
Municipal Carlos Tartiere
🇪🇺
اسپانیا با ۹ برد متوالی و پیروزی ۴-۱ مقابل کرواسی وارد این دیدار شده؛ یامال هم با دبل اخیرش همچنان مهم‌ترین تهدید خط حمله است. چک بعد از شکست ۲-۰ برابر انگلیس و اخراج پاول شولتس، از نظر نتیجه و اعتمادبه‌نفس شرایط متفاوتی دارد و مقابل مالکیت و پرس اسپانیا احتمالاً عقب‌تر بازی می‌کند. احتمال می‌رود اسپانیا کنترل و فشار تدریجی روی دفاع چک بگذارد؛ اگر گل اول زود برسد، بازی می‌تواند به سمت برد با اختلاف و کلین‌شیت اسپانیا برود.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140877" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140876">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A0PLmGVmPt3eEBRgvw5hiF5MRf7tF_amwK1o-hDSLP4Pwe5Pcl1bz5vZDti7K_3uAspF-aOxXj064K4Y5OrhnTPzQv02V6O3iPkaGiOYjfiDkPHZb5V1jJnMTYnjXntxfs5hhr2ddaHou2edTTs2St_36ReaVbIlE0DVcQsVu_5D3TkYkd9EwfAl0PBn7Q3hc1nYps9CU5pI1hjukbtY8MTRHzQqbYnXHv0UUKlduttsq2bZTkWliHsk6bKA_MWrO3RDK3cBmS6tOs91zgNMfZkyQgUij4OjEbS8GquIWYClRMf0bp9gDWwtdpxuDrjuMGhhLt55kD6FItqo6tc4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
تیم ملی والیبال ایران با غلبه بر تیم ملی ژاپن مدال طلای بازی‌های آسیایی ناگویا رو به دست آورد
ایران ۳ - ۱ ژاپن
🇮🇷
۲۸ | ۱۹ | ۲۵| ۲۶
🇯🇵
۲۶ | ۲۵| ۲۱| ۲۴
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/140876" target="_blank">📅 15:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140875">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
خلاصه بازی پرسپولیس و گل گهر سیرجان
✅
پ.ن چه کاشته ای زد یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140875" target="_blank">📅 15:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140874">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
والیبالیست‌های ایران به فینال ناگویا رسیدند
🏐
تیم ملی والیبال ایران در نیمه‌نهایی بازی‌های آسیایی ناگویا با نتیجه 3-0 پاکستان را شکست داد و فینالیست شد.
🇮🇷
25 | 25 | 25
🇵🇰
13 | 15 | 11  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140874" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140873">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140873" target="_blank">📅 14:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140872">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
عالیشاه امروز اصلا نزدیک نیمکت‌ تیم نشده! و هیچ سلام و احوال پرسی با هیچکدام از بازیکنان و کادرفنی پرسپولیس نداشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140872" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140871">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140871" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140870">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140870" target="_blank">📅 13:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scFce4oAiFMtZ9xHaoWSA1BUF_OuQv63A2FaqROBVWadhohw3WtVJ12jr3nLvkte0kZVnqtQ6hjNDqXd6zMq-OOYLRKWsrjHOXrQB93aBRSP9dxEK8nGF-gYRlUJM632B_BAYSx2SCSW2vhKmceORZu05rA_FrXxoOECSYrXvtV6nRTNtc-CVFPq_Oxstgb3lJxUL8UfUJ6-ekOTEfZOybjTTbTHAX-eorzW80Ql-57hPPfDNbR2jRchkh4obyiTorpdXlHJq50C9IduQTAV8kpXXlnJh37Ukd77qo4QwdrALS4zt-_GkG4EoVLEUFCdESJgxqtHNcMubWOF910tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
زمان بازگشت قلی‌زاده به میادین
◽️
بر اساس پیش‌بینی کادر پزشکی باشگاه لخ پوزنان، قلی‌زاده می‌تواند پیش از پایان سال ۲۰۲۶ و در اواسط آذرماه دوباره به میادین برگردد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140869" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKCE4RNYe81PTmC_7PxDUDwx2q4QgSxw5RrYX8d1W9_i-1SriXnXgU2LXykOaee5ARybu_9c3ENVkoIw3-aKvDpomFbaK6FvpIHxfy6_mkrThM5lSFpPc5YZiWD9qMt3JkDPZE3ICgGqofpYijq9M2Fxpgc9hz91jnvbmQcTg2Xck4ZpJz2wmEyPF1AGBnuSpx3VxG-U_S5rn1MFss5XQW_WMHbxbtkN0syuiYZh0_4nfMdSzNX7Dt4OP-QbrCEhbaY1VTYW0nECc8sOXMuJCGw_NSi8yUdGADrjdC__c34kls8LHMmFmmZLqzMgomm7pdhTX6hpgz8K3y6mC_vIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از ورزش سه
🚨
زوج خط حمله پرسپولیس مقابل صنعت نفت آبادان رو ایگور سرگیف و پوریا شهر آبادی تشکیل خواهند داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140868" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚪️
⚪️
محمدحسین صادقی امروز علاوه بر گلی که زد، عملکرد درخشانی در ترکیب پرسپولیس داشت و ممکن است در بازی‌های بعدی لیگ به او بازی بیشتری برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140867" target="_blank">📅 09:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140866" target="_blank">📅 09:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
✅
گرا: از پرسپولیس نمی‌روم؛ از زندگی در تهران راضی‌ام
‼️
✅
✅
گرا در در گفت‌وگو با «Nemzeti Sport» درباره مصدومیتش گفت پس از مشکل کف پا و انجام MRI و تصویربرداری، شرایطش بهتر شده است. او درباره شایعه جدایی از پرسپولیس هم تأکید کرد یک سال دیگر قرارداد دارد و…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140865" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqBxu84Vqt9B7WUE2OVIWvtVrwrGQUDLrAZDWNSDLO7l2cje3Xr3I31aDFRmrpA0CRv_oetdAO1DWh7IgUXT47ueFJmGY7M9TVolEtdzF1imW-Te9z9XmO_BSCfhcgBpc9CeQO60iBKSzokXYIDEEMg8gTEklmgu57OL58WdPNZCfFSI7Jvabub7pSClvoyQpxRXkYQHcf7_XwiNoJP0AAll1xp14BZeSStzf5h4eCV5eD_cZOIpCTUuNN_ZUZ_ASHh8z-wbXcS5FRessN6PfWrjIzKoCRmjTHvXB8Ld7PSO2WgpYTK4UljFQUKTJS44cwBW2p6_E-k1jHXef1VylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140864" target="_blank">📅 09:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsxfJFjQgfxkol90VT86wVB5vHU8kAUTQFeZjU1QgfJ-dy3Z5M-tvjE4N1PCUncqfAZVL-D8CtoSNIpfuBUkK7F3iJRYuETpLPWwUE8yrIrmHhWLrWiwOk2Nuw17uAKcxnwKVt8bSk6GUNyqeRecWZ5vOHwVjOYtoM1WI19K9IAkg4hOflO0MuV709ZjmxkApc6zeGkW6XCz__zXDZl4I9X2mC0jljkxazT_ulYvgNYQ-CXM4Z6Wk1bldTn_mW5YAfGpp_fQYCTEdLhbvZS0go5mgrqSZ3tPxvxxjTzJ7YRUerEQXpWhGVOjyHI1u-8m9wn2Ybb3CIJzv20RkfpnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
CROATIA -
❤️
ENGLAND
⏰
Saturday 19:30
🏟
Stadion HNK Rijeka
🇪🇺
کرواسی برای کنترل بازی روی مالکیت و گردش توپ در میانه زمین حساب می‌کند، اما انگلیس با سرعت بالای انتقال و کیفیت نفرات هجومی می‌تواند در ضدحملات خطرناک باشد. تجربه و کنترل کرواسی در کنار قدرت هجومی انگلیس، این مسابقه را به یک نبرد نزدیک تبدیل می‌کند؛ احتمال موقعیت‌سازی برای هر دو تیم بالاست و گلزنی دو طرف سناریوی جذابی به نظر می‌رسد.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140863" target="_blank">📅 01:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140862" target="_blank">📅 01:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
غندی پور، مهاجم ایرانی شباب الاهلی امارات، به دلیل مخالفت باشگاهش نتوانست به اردوی تیم فوتبال امید در ژاپن ملحق شود. طبق قانون با آغاز پنجره فیفادی از ۳۱ شهریور باشگاه‌ها موظف هستند بازیکنان خود را در اختیار تیم‌های ملی قرار دهند
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140861" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
پیشنهاد پاختاکور به مهاجم پرسپولیس؛ سرخ‌پوشان اجازه جدایی ندادند
✖️
✖️
بر اساس گزارش چمپیونات ازبکستان، باشگاه پاختاکور در نقل‌وانتقالات تابستانی مذاکراتی را برای جذب دوباره سرگیف انجام داده بود اما باشگاه پرسپولیس با جدایی این مهاجم مخالفت کرده است. …</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140860" target="_blank">📅 00:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
در نیمه نخست و در دقیقه ۳۹، شوت زمینی محکم محمد عمری را دروازه‌بان حریف دفع کرد که توپ برگشتی را محمدمهدی محبی به گل تبدیل کرد.
🔴
در نیمه دوم و در دقیقه ۶۶، حمله ترکیبی سرخپوشان با پاس شهرآبادی به محمدحسین صادقی رسید که او بعد از جا گذاشتن یک مدافع با…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140859" target="_blank">📅 00:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✖️
✖️
بی اعتنایی عالیشاه به تارتار و حدادی
🔴
بر خلاف سیامک نعمتی که قبل بازی تدارکاتی امروز پرسپولیس و گل گهر، به سمت مدیریت و کادر فنی پرسپولیس رفت، امید عالیشاه ترجیح داد، برای احوال پرسی جلو نرود.
🔴
از اینکه باشگاه او را در لیست خروج قرار داد همچنان ناراحت…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140858" target="_blank">📅 00:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
ورزش سه: امید عالیشاه به باشگاه اجازه نداد امروز مراسم بدرقه و تجلیل ازش برگزار کنن و تندیس باشگاه رو هم قبول نکرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140857" target="_blank">📅 00:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140856" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140855" target="_blank">📅 23:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140854" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✖️
✖️
شماره ۷ رونالدو واگذار شد
🔹
پرتغالی ها خیلی زود جایگزین کریستیانو رونالدو را انتخاب کردند و رافائل لیائو شماره ۷ را برتن خواهد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140853" target="_blank">📅 23:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140852" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140851" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
✅
پایان بازی / 3 برد از 3 بازی بدون گل خورده
❌
پرسپولیس 1 _ 0 وارش نوشهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140850" target="_blank">📅 22:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140849">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
خبرگزاری فارس:
🗣
شادمهر عقیلی مهر میاد ایران کنسرت میزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140849" target="_blank">📅 21:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140848">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140848" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140847">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=XvPJmt1fBvEAK5XXnL4-JlhvQg210Xl3SZV3lf-o_4vZMZUuqLRglXJbNg8LQGvTgPkyYxkBqdooIMZkCLdkBghsq6PzLmBHvB0y0kOuzciWkC5C-4FZ9C91s2CWcYVmIY-F2QqtZwnD7nlPI5T429A8ZrRFp1FRwHiWVYztiFdMcy2njhoe4tlfg3iAsnFunR71u-rtkBrAtYZsyktUF9v7yk1u85zXBFcFnrT_zp_Baj015J1P3S_QX-oeWO1Sgt995Fjr92W-xlIAT0TNT2HrD16_dEzrwx_rjKWx8j7MgC9FrdsrDQQBKMP15U7LSdERr2NTTmlYQZ_Gsw0A4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=XvPJmt1fBvEAK5XXnL4-JlhvQg210Xl3SZV3lf-o_4vZMZUuqLRglXJbNg8LQGvTgPkyYxkBqdooIMZkCLdkBghsq6PzLmBHvB0y0kOuzciWkC5C-4FZ9C91s2CWcYVmIY-F2QqtZwnD7nlPI5T429A8ZrRFp1FRwHiWVYztiFdMcy2njhoe4tlfg3iAsnFunR71u-rtkBrAtYZsyktUF9v7yk1u85zXBFcFnrT_zp_Baj015J1P3S_QX-oeWO1Sgt995Fjr92W-xlIAT0TNT2HrD16_dEzrwx_rjKWx8j7MgC9FrdsrDQQBKMP15U7LSdERr2NTTmlYQZ_Gsw0A4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140847" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
حاج صفی: بهانه نمی آورم اما چمن بازی با ازبکستان و روسیه خیلی بد بود. از مردم بابت پاس اشتباهی که مقابل ازبکستان دادم عذرخواهی می‌کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140846" target="_blank">📅 21:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140845" target="_blank">📅 21:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140844" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0RpKR6Nifd9vaYp7USmtSsTIYVYVkUyawH9pi-w1yMya-PG9SviqR5qVvA5hE9oauLm3ZfDbRPgGwfkgjPkW4WD4Y5ECvWcIyQuGhbJ3GWfa3UKMB9CXmn6r7YJTZ0qEMM9tlFpijlyWaiFM7NXZotTlGZwolZWhBv3mQm1KmxajDYS4TWd_aZDmAAo7xyDkr1UJu9_3KpOL0akS5GsYOlacsfWYqNg2l-1YMy19bNPfHzSZgFoNgzD45CQUNEwQXogOsUknCqK-fosIX_CM3IUA20JKuXxu7dMo--zqQgTHCipoah4V0TdMDkbqVi9QMGKUcs0nCVcVbFkiONwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
FRANCE -
❤️
ITALY
⏰
Tonight 22:15
🏟
Stade de France
🇪🇺
فرانسه با دو برد ۱-۰ مقابل ترکیه و بلژیک، از نظر ساختار دفاعی و کنترل بازی شروع خوبی داشته؛ ایتالیا هم بعد از شکست برابر بلژیک با برد ۴-۱ مقابل ترکیه واکنش نشان داده است. غیبت امباپه از قدرت هجومی فرانسه کم می‌کند، اما حضور دمبله، دوئه و اولیسه همچنان تنوع زیادی در حمله ایجاد می‌کند.
با توجه به فرم اخیر دو تیم و میزبانی فرانسه، احتمال برد خروس‌ها با اختلاف نزدیک و گل پایین خیلی محتمل هست.
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
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140843" target="_blank">📅 20:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzTAwoTR_N0vM5-VgJBhFCluSx9_g_ELrq14e430kOgAQnFLAESoRsKs1nGoZ333kOFDu_rkzLczsaevptIYrLVzFnPZdVQ25GB_DfGxpbbR3CtkyQKgyenjb0cCC3q2Rj--ukRtm04v9DJXzR__J99tnAaAmYEpsMSwUpQ94RCwrgRLXlxiteyx75bhYa2V5to41F0G4Jm2WwXVaryHeTgQ8hxPWjZ-FCbpyuYaCzWcv7Xqq0BtWsRZrLG5VbLSeyJd95IMG1MLlbuJ8e60f7XtxctmtCZWu_NJNCTNwtZF2wdeT2EtSTNzLO-g2Wwz5unNn8XZ48onZ18UyTCr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140842" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVSBDpvjFUsJBOYLbJXk61U0uRUYLIS7sLehuUUkowXlkv7Lt3GTGPIoXoABTyFQVT70eXJeq0gc54PI_BUyoReJ2z7bpp6-clUh8DWtsLILt_VmDMk_1bZz0afMAwIksJoZv4Jn2oLcwhYqVx2babBdBUgaQgeJvLZJj95xvARH_355BqZ3Q3d-l4vDjEH4mDi9mh6iy7UdCofvsvrk31dkf4qKxGPSJmuRZrPrs8pavLfzpc-l8GSZj6jhqLKPP5XlPOt7Vstfuk0QGLrwIUDnmGHixtowECV-rXF8aqKg6J3VYhvVwWA472f0K4fdeax8tWRaEuO6adNVsGKATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
کاپیتان پرسپولیس در دیدار دوستانه امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140841" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول  پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140840" target="_blank">📅 18:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140839" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.  #دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140838" target="_blank">📅 18:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOZs6wFPsZDRV7uHQkXNQgcQT6QukPNeBQmXMTUy6cFiUss-xh5duWsm8eP4QPJ7XX__7yc4CEosXyYO2oUKRoS9_L120zHdCsKJU6KfmWpoGsuneVVUrcVyeBfkLVCiIjlE13Of-xh8JRnIOIYqyHPMc9ZmjjXuvP9EpG_Vv-2a2iePZBqPkRwwLk_ZIzrN2c9fvuOgLSe6qtVdsq_CkSnvYR_uk8Kz4lItkiEV4YPy0G2yYoNuvhTZIzHCCPh-YvqexwR1w-AoCUEjSYRlim48BE7ixtHIUPguVkese2pYGs4vXr3bpSUYV9427blK_2LIFoVV5JQsgZ70FLOzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.
#دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140837" target="_blank">📅 18:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsxZd2Yj_3ceThiIbpFlhi4dnG8i44XiSsBRKGXlAHL38XKwqJeyYpFDzSsjEhb87BsK-dxUgdrbJMYouTnwU0Gfy7DQLrb5s7bnyJAjjeKsweFw1cleXPCW2ZUyTLsr1_P-DDlCWYbmKQnNvH2eAvFvAzvI_lYOI8sxg8_yzfzYSIAKUwoOZOcJls5EXodKtaajaL9w3YigyWhrvfHLvPAZJHEa8bB8isCU2CUiEGtlsg9Q_ogiZOhgmh7-vWfMH8jOJJD0wAlHJ6RHUn0pG5QTAuJkACcVSVE1Ij1GYHXst4N3KiPCUPTivNk95T7VibggccfHwJv6ZrwFZTKYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😀
سخنگوی فدراسیون: قلعه‌نویی از باختن بدش میاد به خاطر همین بعد باخت جلو ازبکستان اعتصاب غذایی کرد و چیزی نخورد
🗿
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140836" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f945d97990.mp4?token=D4OFN0Eyvd2Sdfo3IIea0ffP57ZHLH6keUCkGvJh0SApyiDkClpKMRvM7vvO7YLzbkLiTSgUzRFCsyyDotcMw5ypY3QVCbhobiELkh_AMZPeEKa5RBCS5ipMkIOWgs9j4HpApfXx-rmA9Td0Y1bnR8iTSQuHXx88BEEFDQbjwijNzjyRffpGNh0BzdYk0A5Lbyyd-EEU-8uxexMWN3Kjzv1LFpAqXs1FzJzaegkhhCFQGdn3XH3wKKipINYZPQpb7OYXQcC04nmoopR1pv_7WKDwVtOzIyFtTkSUalWlD_Td7-W3plu72s7cK0FwPNs91gDYDTmE7kqa34TKvx8WKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f945d97990.mp4?token=D4OFN0Eyvd2Sdfo3IIea0ffP57ZHLH6keUCkGvJh0SApyiDkClpKMRvM7vvO7YLzbkLiTSgUzRFCsyyDotcMw5ypY3QVCbhobiELkh_AMZPeEKa5RBCS5ipMkIOWgs9j4HpApfXx-rmA9Td0Y1bnR8iTSQuHXx88BEEFDQbjwijNzjyRffpGNh0BzdYk0A5Lbyyd-EEU-8uxexMWN3Kjzv1LFpAqXs1FzJzaegkhhCFQGdn3XH3wKKipINYZPQpb7OYXQcC04nmoopR1pv_7WKDwVtOzIyFtTkSUalWlD_Td7-W3plu72s7cK0FwPNs91gDYDTmE7kqa34TKvx8WKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول
پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140835" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_eEc6agXVSf35W_9D7hCmNuz-MfiLNi6C39clipHLKTKSxKS2qKUhqw-qF3M580GWiImRzZXG0cf56b_CBxcAxDk1kYL7f3DH0k8tTL4nEUCsVFOFOGzo-P4KKjtYAFgux-wjfRrNi8D6Y6AVse4Hm7pK73M1SjZNUPYmKnwD6PmqAQcLUwM6ALwp_JftTioopOALCTgn36LmmnN5QU6FaoVYYi6iJJHI5v5UNsiWaTe60oMl5nll0MYjaXXrrCOxQ6fI5wPMANMmxotsEW6o5lkGGLyoivZMweDCP4B239vbK7mCo9f4PzPR_t9pDz3yDwFSN83AuuJqQN1Sd5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پایان نیمه نخست دیدار تدارکاتی
✅
پرسپولیس یک ـ گل‌گهر صفر
✅
گل: محمدمهدی محبی (۳۹)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140834" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=tusZxPQihxMKztirRm-zB7YN0MqBg0bVqJfPrrPQ13F7MndUV4es6OpzPAOcQ-8GZLR4RE5eJDbk78Y35l9SGHZBycAfTiKirpYjBDECWugBPM2rBWA5MUdVKYiQroiBbynGi_l-ah-GyiDJHk39fvKBrHNDxpFfNXWT7kqqkJppPw7_zXLmcbDYItvNzQHTs48EqzNCgBakij6s6vCHKKxjHejMHv6Pp0s3okpUk9Rezp1wcHyexFQy6r9cdfLLe8wYPAys1xR3h1G9CZYgWJJg4BxApIMJakP3I48l96trcTyk42l8oKmZ6qEUr6c-_r3SMeyGxpZlfT8WffYdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=tusZxPQihxMKztirRm-zB7YN0MqBg0bVqJfPrrPQ13F7MndUV4es6OpzPAOcQ-8GZLR4RE5eJDbk78Y35l9SGHZBycAfTiKirpYjBDECWugBPM2rBWA5MUdVKYiQroiBbynGi_l-ah-GyiDJHk39fvKBrHNDxpFfNXWT7kqqkJppPw7_zXLmcbDYItvNzQHTs48EqzNCgBakij6s6vCHKKxjHejMHv6Pp0s3okpUk9Rezp1wcHyexFQy6r9cdfLLe8wYPAys1xR3h1G9CZYgWJJg4BxApIMJakP3I48l96trcTyk42l8oKmZ6qEUr6c-_r3SMeyGxpZlfT8WffYdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حاشیه‌های پیش از آغاز دیدار تدارکاتی پرسپولیس ـ گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140833" target="_blank">📅 16:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=EfUehWZxScRM67jEjjVUvZava4T194FrSkpZjBIC0bWz2azT_79NkaAUZ8IP4HOF5YoAbGiC7Ng-2deJUNS284lnIYaR7lCq3KM3ESz7-XijTo3m-hlIucnoKCHpvwb4oTdBmu8vwAO7sX2TgnZToRn4URKHnzbs5c0s5zeNQm11S_-qLf-knZ_Taoi6GRjJRs1nX-Kq7UG2v9ZB9MLH8Sge4Kzgkh1i93JK6dwU_I7CS1mpg9jMMU7xsxfw9GNSkO26cFvwyDdJoFmi8VwSuZ6chz1xZETbVIXTo8ZUEaURuVSOqOTIh45oITO-jvrQWTwvtjjLC-g3mwlSrboNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=EfUehWZxScRM67jEjjVUvZava4T194FrSkpZjBIC0bWz2azT_79NkaAUZ8IP4HOF5YoAbGiC7Ng-2deJUNS284lnIYaR7lCq3KM3ESz7-XijTo3m-hlIucnoKCHpvwb4oTdBmu8vwAO7sX2TgnZToRn4URKHnzbs5c0s5zeNQm11S_-qLf-knZ_Taoi6GRjJRs1nX-Kq7UG2v9ZB9MLH8Sge4Kzgkh1i93JK6dwU_I7CS1mpg9jMMU7xsxfw9GNSkO26cFvwyDdJoFmi8VwSuZ6chz1xZETbVIXTo8ZUEaURuVSOqOTIh45oITO-jvrQWTwvtjjLC-g3mwlSrboNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140832" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuttFkQSibQopPc5aBoGNluejaNHfmsQWfHzcr98VT8I9f79bwiQRvRKWre5gJoq9zqNT1LHs32EOnb6ck24rjSyn35doHzL5Ows3iuHvlLt-ogofl07ewAH_KF8Mte-w54j6eNrXcApYKvZJD1zUOL8i8Myx43cHv8TqJdxYQqALMJ1dvvr_GVIi-37KspC_mXJQa9cJXpTf4tbMfodel_DBCt4MywWus2Un9Rer69GhSTW-dLXY49ghP8QMPvqNf7GD6Mh-hweu2XmbFNHzjYw-tkjCgx_EGloBvSbxmS3Elf-U1ufqkAbF22aLypDzo45JFUCty6PxnhEL0oMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است
.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140831" target="_blank">📅 15:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140830" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7gURkmePZrkBvt8zguVtGM3VSEVXPBkMJ8xFMgVv6rZI-rBeqI4que0022IxD73GgVQgkFEZfX76aHMG0HNthtjAq34vXj4IhVUr-Al2j50Nx4Bd5vBD5P-obOhXnthN8NaHqBuLJG2ft0DaxYkeRSz9LbSK4ImPn3eOInMNlKjt_A28KPtDrClRtXUVCKa6zSSLwnB5DDskzVYD_ororXTPl9CU504Yolsqk76v4gtvw0VQsWAqONM0-qAnTlk3rWrjc8PEdKbGySM9IGbCQyp3dDPcu-93a8OYTcf3UAbLwBJvairg2Ht9azZs-TM3rYa43J3fXa9SqZQFivdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول مدالی لحظه‌ای بازی‌های آسیایی ناگویا
✅
ایران با 15 طلا، 17 نقره و 13 برنز تا این لحظه در رده ششم ایستاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140829" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EApM2LpDwDDgrlD3vKW8K5e1HLGEMPHpNc526cLkVS1963HibI-jyFDcANINr6NHSUZmNqUZFCyQLK1JTwVh-sYqOmZQ8v1zvPwFGAYxtmReG0JVy8Q5E_KlBcZQLz_u0N1UgjDM2M3ddoW_I7J_2Q4eZb4W2LCeldS8QhFttP5NKQosKd7yBL-PA2xlMtofPAredCWNh4Icg69NX0xYgbpsmfAdweKTK25YulmhRS8lhod1GMUTDahxyoN_OA-y7n1UWLklakJEI3JmUydqsPJyg1W7nfpmtCHDL9xYaA__Q-_k8J1Ncv0HMVvNZrH9cvnsR0UMT_sQuu9HHgcCJFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EApM2LpDwDDgrlD3vKW8K5e1HLGEMPHpNc526cLkVS1963HibI-jyFDcANINr6NHSUZmNqUZFCyQLK1JTwVh-sYqOmZQ8v1zvPwFGAYxtmReG0JVy8Q5E_KlBcZQLz_u0N1UgjDM2M3ddoW_I7J_2Q4eZb4W2LCeldS8QhFttP5NKQosKd7yBL-PA2xlMtofPAredCWNh4Icg69NX0xYgbpsmfAdweKTK25YulmhRS8lhod1GMUTDahxyoN_OA-y7n1UWLklakJEI3JmUydqsPJyg1W7nfpmtCHDL9xYaA__Q-_k8J1Ncv0HMVvNZrH9cvnsR0UMT_sQuu9HHgcCJFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
✔️
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140828" target="_blank">📅 14:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-7W6TjQAj0fjZMoWy7_UXWL_3IG--WyaoZ3Runb2oYDlRQ2bnhXSUsRriIxipx8y0Fo5siinEhJdTYWmV49OGwaDSiubVLQVZdghYlC5XHH7AwvAZJzxhcLt0EIO0xpfI1R5YiL9KRbGRn1Z7M-1s3Jrn3TTrmjmcYF8Gwm_hKQ5SPIAY6CkORGAHN-7aZ5h2o7hO6Hu2qp5e2P2aNpPir4coa0HDwWKgCW-qywAWt22UqI7eUX7GUk-0nbwaG3FkeM7o7VN4uTrkO_9Fw02-xMVBbAObokE_wzoNvSS1leNMaYK11my_NIFr7MsBchpLsujRivZc6n06NIb4Ky2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
چهره خندان و شاداب جلالی در تمرین روز گذشته
❤️
✅
ابوالفضل جلالی مشکلی برای همراهی سرخپوشان در دیدار با صنعت نفت ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140827" target="_blank">📅 14:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140826">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBqnyYC2d4xH7BhrRRoLL9PCXettq9XrMaB1Y1u-ZkGJ9j-yr-0oDPQApoCHSpSJHUCmx2C_OGONLqtbLmMvIlmz4ZXJoSOkMlGoL4R6oNzgFSTWHRfEAp8GCMutb2XmM8qm77xpFSfbONb7ZRHWvxb_5px6woIi_IO_0uDlRxkazqgW0EEcEMVaoYIrTyqII7l8mrIVRonunajsNnHWy9F_y-kmJLtXOD5-5JVlc1XIbM6c92bQK0H3DPP9xQZej9n0tAkxzMNmguKRfvNcS96IvpJIQ_mT0n1yW0tHgrKX_PkqYfi6TXaJWGxkWEvx3cHiusiCPHKygEfSx645Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد خروس‌ها و آتزوری؛ جایی برای عقب‌نشینی نیست!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇮🇹
ایتالیا
]
⚽️
فرانسه با وجود غیبت امباپه، از نظر عمق ترکیب و کیفیت هجومی دست بالاتری دارد؛ مخصوصاً با بازیکنانی مثل اولیسه و دوئه. ایتالیا بعد از برد پرگل مقابل ترکیه روحیه خوبی دارد و می‌تواند با بازی فشرده کار را برای فرانسه سخت کند. با توجه به فرم دو تیم، انتظار یک بازی نسبتاً نزدیک با موقعیت‌های محدود و احتمال گل در نیمه دوم منطقی است.
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
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140826" target="_blank">📅 14:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140825" target="_blank">📅 12:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
تیم والیبال ایران جلوی تیم دهه چندم اندونزی زانو زده و بازی به ست پنجم کشیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140824" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140823" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: منافع ملی؟
✔️
شکایت از آسانی را تا آخر پیگیری می‌کنیم!
✅
یکی‌از مدیران پرسپولیس مدعی شد هیچ توجهی به درخواست علی تاجرنیا ندارند و شکایت از یاسر آسانی را تا زمان رسیدن به نتیجه پیگیری خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140822" target="_blank">📅 11:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvSivYQt8KDglve2bbOO-zoryV-a5rGwRJ6wMCK7URzAOONYM5EkKcdkcYmCaEmkd98VQY7KqFQYWffPEhx2AijFiWj7l899b0YzlFuEAIFhqufQ8jxUHSy0qmE9XJ5jI5HsGZGvw9rFOyEE2vOQYtUL8bXBdIO98kShNzjSGUTjHl-e-dDQ5_zB3IuE04nVRxfV3TkhAWQOk-yOZlLgTfsHt5R0-SVrigIsIVm5O_1HnEey2xRpeFP9qvyWxNnsm8u-2XEYKngUFmtzMF0stxVY9xGJ1v8dVaXjCu5RuCXezsHAQuAwqJHLSQRiFW-4qvRtqbcK7g4p9b1hQZg59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
⚽️
👀
‼️
فکت عجیب ؛ مهدی طارمی در شش بازی اخیر خود در تیم ملی، نه گلی زده و نه پاس گلی ارسال کرده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140821" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140820" target="_blank">📅 09:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140819" target="_blank">📅 09:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go6ZcumCRKyK1_gdOxd76nyAKoKBvh4A-0IbqpiVpEUqGc-Q5_ueqr0demHVHP2sgV8VNfK56e79amULxO7_JCPTTQkr0zYB4OhnjIFxomV0CzS-8aRKiNDmmAjW44tkgR32VAtpJNVOd1moDLqT515RxVi8JI80Tdu7CbhFReFCYn8uAnPRhqVpqmEeCSe3xYIPtfDT2Gw_IxE3F0sTlBm-NUR8uhzBDPSNcLvqXGQgri6THAfVEE9vecVUXIw8xaC2mEODdpEsBRu0u7WrBEzWGvX5z1TnlXWX63uHw14ksmEuWUVjqmFRJTmoxoISIfWgwsxP62CFMjLfGdGd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امروز تیم بانوان با زنان نوشهر بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140818" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140817" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfHU7P18yyLDNUodYo2i0HSsLo9PA19sRiR_vyBtZ5dYVqWZawCgHXvEZC6IWmANCr45mrxIsuBoBa36zID68b4AaUdhAeK-gnhYNgksZpmFXHmeljPMmyzEYRLOurMJcMotv0Oc-zvpfq0djyoEVOahk4cph9HHsWbovPUlWJBRNXyRGAawFItDkbB83rQeepd4LW2Vq9xe2e7RDgEpND-Nl9SSiEam4Jf6YYM_Omn45Beo4QBLG_O6xe9sP_W-T8SiPL99sQNvbMjwl3_0gM1Fflz7Fmd6cTfvXAPfdcjebB1wi2HnWoP0gBqZG6_rJbgec4z3zGBi76zh-0PDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک شب پر از بازی‌های سنگین و دوئل‌های نزدیک؛ جایی که چند دیدار می‌تونن تا آخرین دقایق غیرقابل پیش‌بینی بمونن.
🔥
⚽️
از تقابل‌های پرریسک فرانسه با ایتالیا و بلژیک با ترکیه تا بازی‌های متعادل بوسنی با سوئد و مجارستان با گرجستان؛ کنداکتور فرداشب ترکیبی از مدعی‌های واضح و نبردهای کاملاً قابل پیش‌بینی‌ نبودن است. در سمت دیگر، اوکراین و لهستان روی کاغذ دست بالاتری دارند، اما فاصله‌ها آن‌قدر نیست که بازی را از قبل تمام‌شده بدانیم. ۶ بازی، یک ساعت مشترک؛ از اولین سوت تا آخرین دقیقه، شب فوتبال ادامه دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140816" target="_blank">📅 01:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/led2FuZW8ZqVzdqVT_oCMj9ByZrkMwLi7t5RLXu7vgXnm9CG3HfW5zCVLrrftTSW-pNJSIOAPi1wVHQgVJZDx9fiir5P3kGeZoyo1_EIqNwxAGX1PX_j1MqO1xkjNTsjw_53-62H8L0EKoNAW66ALu018qxCojVkU6DCZrM2WByE7KW6XTujPxuolQjVJT6R6osNb7p_CMsR7fZ81J0HA4hDJBKlHEgrdPuWM6FgfAAZjboKa3phweSTqWUuXr79DL_dpoNVr4XohQhNrRyhA_JO--inqM_Ls-wamXo6R7kr5vfPe3LjA9FBcxzIGjDfBU5YDoRyhZg5ThXX9jyZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گفته میشه که پویا اسمی ۱۶ساله یکی از استعداد های جدید و درخشان پرسپولیس هستش و تارتار میخواد بهش بازی بده و مثل زارع تو گل‌گهر بهش بها بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140815" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJXLA2LmjfgJ9WAgnzyCZvPuE4xgYD-64CX5qHdmDlTY3dLqALEfUQuDwB2mURDhENDUrWYz5Ge_UwtdUyfFkDngBFlB2BPihRYa_1_BE59IofZwflJsjBIbB2HBzPKdWuPNprcpg3n87JvSviLe29EocxlOf1KLbk6QZGGQ4bbDe4HXkDu8G76dUNZfL99z0r7eauCKHK1CB6ey9msLJQ5459Xf7zpkHKlZMXj2wJ4V2LwyfxbeRikugt-FGZ_iIz4sIOyu_vcGp_xeCcBzYh5o5-FRslCO_pM_ZcNOZixuRSKW9Wuv-AMJjso5egBjvVK2ABDWlWT3Q4NOtT4O5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس فردا به مصاف گل‌گهر می‌رود
🗣
تیم فوتبال پرسپولیس در آخرین دیدار تدارکاتی خود پیش از آغاز دوباره رقابت‌های لیگ، فردا (جمعه) پشت درهای بسته به مصاف گل‌گهر سیرجان خواهد رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140814" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140813" target="_blank">📅 00:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZleZPGj1oyIHwPwG2MI-9PZAjuPtDJjSBr37xttQ8M_mLXZWGatuV-x3DdrfBYMNGJRKvGNYuno5FntUX71W2F-l88B6bdv7kb-9iTGd5Laz1ny3WRQI_nPmAo56tPBFke740OecmPl9-RCZpKL_hbz7gFDigu2l6fro1kuKGuO8pe-W5324grNQR4TGiuYNV2GLPqumncTMH01w8W1UTYDLp4d3owOZ0kHCIeKmHF8U0hzG15OBxYo2qtH3K0VygURvJLP34GRHPFrg44BSN2FrEFCyRwH8ka8lKRhem8BNoZU5UyM5OCGLJRcpbxtEx3wDp6yKdpbMjRCMg-E0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت ملی پوشان پرسپولیس به تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140812" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140811" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
جنجال قرارداد گرا در رسانه‌های مجارستانی
🔺
رسانه‌های مجارستانی با اشاره به غیبت گرا در ۶ بازی اول پرسپولیس، دلیلش رو مصدومیت پاشنه عنوان کردن و درباره قرارداد و دستمزدش هم نوشتن. همچنین مدعی شدن پرسپولیس دنبال پایان همکاری با این بازیکنه و اختلافی هم بر…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140810" target="_blank">📅 22:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140809" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
❌
ادعای جنجالی حسن روشن درباره ساپینتو
⬇
حسن روشن، پیشکسوت استقلال، مدعی شد در دوران حضور ساپینتو در استقلال، اتفاقاتی در اردوهای تیم(دختر بازی) و محل اقامت او رخ داده که حاشیه‌های زیادی ایجاد کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140808" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
خبرنگار: شما ایرانی‌هایی که آمریکا باهاشون در ارتباطه رو «دیوانه» خطاب می‌کنید؛ چطور میشه با آدم‌های دیوانه به توافق رسید؟
❌
❌
🇺🇸
ترامپ: شاید منفجرشون کنیم. باید بین این دو تصمیم بگیریم؛ یا منفجرشون می‌کنیم یا به توافق می‌رسیم. زمانش که برسه، تصمیم می‌گیریم.…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140807" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🟡
🔴
حسن روشن:
🤔
🤔
ساپینتو اکنون بهانه دیگری پیدا نکرده و روی داوری تمرکز کرده است. ساپینتو یک مربی درجه سه است. صریح می‌گویم روی آدان در دربی نمی‌توان حساب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140806" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140805" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140804" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
