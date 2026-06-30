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
<img src="https://cdn1.telesco.pe/file/NTKk4VkrvHtQZgfU-5a_1KF6xG8ZDbRrirAsq4m-mjfG6Prj_0nX3hj6YHHyffE5Ie9DdGnnplHIWhL8vDe_hRqwG-yQKNbcSa8HLvbNg9cdVJ1Ch6yP-q6valPGr33oIq5ksHhLXXUyC5RbCGfDyy1q2rKuvIk0wIyZdREStg6pz822ybDNwMnKTnmCT7QO8UhkB8vswUfD4f9OzssQgoJPNBdggbRUVqqh2vVdMvo52IKf9-16fMjJEd3QQ-tIiowaGdMRmoF-gxOAq4lAHJ1Fsefgqpad-33FRxPtjjDz7FwqOqUiKFKT_SrUmaCUR-5LnTztbS2zX2cbivAYQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/orNYfEf2JFkRa0-xuuhjkI3lgxF8Wu0ocYFBkKfEv2kmS-KPJQrCf7vUBPO6PRlq7nV6XXz14R-tHCtVTEw_TEh5WUDjc3RZEfQiAQIdaGCQc4dJ021qQ5qSf2lbNTk-09N9t2iTFYpT0tJO8IJb0NgNrRoUFT318niOF4AXaN2k_vZMBK1E69vFzqbz5i8piQm4bcZ1ZvPrsVQfDWpV5QqYIg-LITvngimKVZKhEDCmeZED3PvJAnSC2wSxFqnPoehXWtXdqS4F-r7ZyErtuKnrXWQH5L-LeMLzLG5vfwyJ0mq52zo-Dd0aB7jQb5pWOAk-01r3M-eBeQKS5p5AkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ERJehBhDVLigdNxBZr-wW5uZ-nkO__iKWnKvRdQlBDJPksKlv5URtGiU0e9nF6x62wqDiQxW1hDGB12NeGj3jBGweT4LxaLP54O-gzhfAXQX-1BDOjMMZFiLr2IuIed4WT8VSqAgRIQqxjbtRutrPp4BnuFHdAl3bmKdaeac32qCak1PrPf-NEPb0W00DAQZXqn2JvyhI0CHqzrQZJd03l0irdIYg-NNPn69VcHy2uM90S-F1fb1-uTYTDLxHZA3dX8mnweKxSBnDBQcyEavpbdasEk9_GfaevXV-8k0SPrWMeWm3vLsNatdoNoPn-Vx0r9GNFsuScrT0YkpUH9tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FRBkAfH9aU4TXJmKup4pfFALVMKXue_weVHr23nV8pcXa-bfUXyaUgaTHgfFo0Gul56dk63SHUiQp_nVdMXDBIZbdqhgMMi6sZYuouUXX9kRSwDPiRFC9rf69OWs1LsA-9tZoklAMucLISy63yqaI1oznxmbvyi01bQfnQHvsVlFkhN4HmNo6beF6ohbyuZTcYkWsyp_p4TTeuL0MhOMLAmH_hsrwkBgdshcqrKWSeDmtuj8HGtUepFWeX1aIw1WTxg5VYcr2AjntrP3K2EzAYJsVJEN3TeYrIdS2_0PEJNp-8z9l2e--H7A02jPfjxaDX9H1MhvxXgquGdYObBinw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atWtaVnC_dNH1ifxu_0C8RhaBugmy13JpzGsluZ7-ogBGigxo5YtfLvMJVhwgZx-Wy8IqO2r1DIAgkI7m1khZ2wVYwSIgRiwqtIVrfFfqNPuKfUlt7c76Ijaan9vCUOBlg586joT7YGWBTTb-O4ZdyMBWurHcOO8LcptG9f3s-iDWJ1Kr15-q3dSZBpO1Dw8ZXAzvWqX3pCWHt-S1JsP4VbfSXILf4Pt1wUDqRIimd_jALTwyynHCPddvvuavukepJXe6IQDigiZI8dta_uIzFIgbtPnDLndr1Ub_DXXs81tIgQRdkES426qUxzwM7HWYIFN4aW6-fVhXRbRrct8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=gF_300pfTvMXfnQ85LtjLV--QAG7YwTllvr3zNu_Un2EZUkaVlkcj4i2Pqj94JQEH-3NNZCt2PzFrmOoZocXyqp6_jJol-Hle0ZXmFZV48WJ0eXfvorCEytOnXEThW0f2f_oiEM6uHq0V9-zwYYUq1ZaJk5VzW8RzaytKkLdoXaJeRPdPh4THGJK3jcp5X2SKVPjEJOP_4ZtTIi5CnAO7eDy3eVF24PNKOicDq5f7L-_jslBTWbGv1eth1UybFKEps_VQtLoMEXP3LEPhJ_oWI7OspKIFsZOGJh30-vLZ3sKh41jNigpc31Te51IjeqOPrfm-dAC82DEllAvIvM9YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=gF_300pfTvMXfnQ85LtjLV--QAG7YwTllvr3zNu_Un2EZUkaVlkcj4i2Pqj94JQEH-3NNZCt2PzFrmOoZocXyqp6_jJol-Hle0ZXmFZV48WJ0eXfvorCEytOnXEThW0f2f_oiEM6uHq0V9-zwYYUq1ZaJk5VzW8RzaytKkLdoXaJeRPdPh4THGJK3jcp5X2SKVPjEJOP_4ZtTIi5CnAO7eDy3eVF24PNKOicDq5f7L-_jslBTWbGv1eth1UybFKEps_VQtLoMEXP3LEPhJ_oWI7OspKIFsZOGJh30-vLZ3sKh41jNigpc31Te51IjeqOPrfm-dAC82DEllAvIvM9YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/evIWP05AkkMdg__Beotz54UMkLEVqyUv1Dn6ZFwX4OiU2SIG0eNeTnhUyKk9-jodIff0caTTKGMG4lj-ePHgw8YLW5o33QmcHVQ2C-hrw_GNopZbeo_RA2fCVEzIxrhTNYxFcOqz-W2niPP9dG6_jEa9LKmmYASM3ZEgS9PgZLjTFBRHcgaaBwCvcY-Zn8ga8vKq9QF_yb6j1uDzjAvzdyx8DsJ4GGrxT8m12wTzqu5BaaaDmP07cPD-uEj2RLKaLkhfq5mvpH7cE-5LUnFIAVnzkdcc3uKwHc2JTWkPE7Y3lfNxZ8oB4FcnwPgaXaqbwy2rWtPanpHWo0B0n1lSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLGljtQmXNP8bxG4VEVpGQsi1mK9-6PeulYnXB12zsSWfKdSoQcQQc5F3vfAASBrq6uzX3NlaCU6BXYP0iQ07yZRFzJum-qmTLiTBrvoAB3x2nDg3pm6NiNjHKFBTVHE7RCA0Sc1HjZNofh1R_obG7X7PWrtJNnTLqQ9yypTggfM-Jhh_Hke5vWiHyY2caa0EqWXynbDCnorCDRUx-BTH7-somHMuRe7uv2PleQbEox2ANP-tcslZkucbTYXxXh2P0agyUjdIOXCCls3c97YfKsdlWPkYyZ6W5qz577unDRsSp3gaqWNLjIueMjrVgFEUgYwwpEFQ7ZdynfUlk2nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V7YFtnnsrfIjaWJ5YEpVXrVHXgq0ZLYJCqrawr64HBroCdcrSnMBFXL1O6aMVIBu2snSstEyG7XWZ2vwM6VqYuQt_vxGILfmnz2gJjjHsjJN3dX9b2mK81AVwGZOzFzJBfiIjpSOLITO0ju9BqVCHNDD0HgnCw1VsJ9A51Yz2L6sBrDsV_4o--7iQICMcCgcX-dQ2Dqa5JG0Ng-e2mhecVUIihIFUuZeggePSoTIaIEUGhAT-z-VX5Wh_HsTuq6fKdU2xWKWLL813y4JYlHs012abczYK1cwOnqRWN2YKOKWqcYlsG_WqMCaCOR3-CLByvuwz34MNqGQ9NTN_u2nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gO796KjqMFsW98KF1HdcvBCVmEHkWrw_Lzmhp1bE8Faj4XXYhEoXuyhxhuRFPv4SUTWzM2tA7JJbC46_1ur4c-B4Toifg0Ew8bBSOuoTSj8E3s4PDhRbOCu5j6oWuM7KIEQP-g0yK5Bh93yJJ8muipaiQT2MVPweYbZC7Y-aavbkDBaR1Wm0gLxJ86kz_BhNQuC0tRtytatUqAlK4v1OwTBq6W79f13YRh_28O4F7OVNK-Luxr-BXETxVSxcvC3w-KT16sXzPEMtWexZWPRwIp6QQ1hzrshet7_q64uq8NfS1zxzWdJXhrsiFgGeuG47nc65ERRhOPzEX_jlMcc6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hkacEgsKe4o8KRKw67A1NxeZc1OVexBOJlrIaE6portrZbcJ3D7TpO5IqvKUGy5dWrljMSRStv_q_DIqyW8_bS_pWQdDpIJ7B2ZB6wqBLuoJTPb14IFOX9apUIwM_n4OWbK3inGqvazSzrlWrqOcXptxdku0znaZmN-FFBJXXqi9pBSLwYm6Lk6vvf-7jXwTd9vUs5jQx4F7Y5n58GGWaizTumx0Ch7NrDaC5lTwNj7-xytW7_hj6dfQ_K5L7_wZo3rDBXFkngmr8AeJg8HRk5mSf95Y74nKtNHeONM3d2SyPYvAnMAIJkoDl5zdCe8bqIObWvR6S_hP1b3bJsP3tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Owxp9xZw1xx8EBv-4k5-Bh7LljMrptSm85FuSbOuSWS3MBNpY2VLlSJexLCuC7SDbaf6tSGSjYg5ilfoqoREPcV933sFhFtEvzarNCbPlTnow7nPuniZKHFRFj2WPxWPsa2xcWqi5iJQB0FVkWcrhfpmKDFOEtwGRdT47XZTLRbU_GiEpJlB7BxdSvaFZjlSfmfsQoFBHfvQn2zVzi_uWyeLtaSCoEwv6P9MPxMa5PIcQBDC-qYSnIACRh93XzVrR9sdV0EIJ9tsqKyahsebHuRj8Z4TN-ev314ayGfehlm6MtJkqbIDNGlsuAvCiRYuy81iLRfr2-bLFmMcAa91RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T6Z_zJZKODWcaryN9MkkkTgxjlb9-SpxX3hJYyqFhQX9UrceWnAkS86S8dJ7LRxC1dMQRxepkfia6ObkIF69XVEifTPOnbF-5IBmWFgMdAKxHXAys61C_dZ9PmU9NvX6fuCUihCYDUnsKudaSHbn-Qd_hC_5Vg6MAOmW8e_6qsZ9SWhkFRYuGc22NRagxcB3ic-3gNAo37Y32k3Fg0qMJSahuTGa03WyE5i3lFeNc81VEhIdNqEFf0vrt-eizsmABZU-orJKMRbO2f_IJKI-mMneMy1Ns71Myzz1nxfEzH-m336Zsj9OjaAwFcj9HxY1mwOVUqVXUHSMD4dxVWqbgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uKPT_B-qHJooa92HfUozbR4nPyUQfr6WXHN9y96XBdh5Vuoi9IzD5VIlao6yNB2hagnQxKLZNAYpQCzbmPG3Pw_kx4jIdwNPNIobTjo7WajBJyYQQbELyqkALGlr59UHviaDXpPrNYhpXlmO3QM14cTNVqH4vv2XIDChozDXtQo4rCEKl1dZ_4MVtRufdAbbMQPWDHCaJ8rAmzQgfpt4ikftBgRL1m9uCxUHhfH7dP973ecRdYtKvG8Fr1wwt2h3vd-pzrxLDRNYVr0ZKnEEa8bfFOkyT3ZOGznHZgd3GpCjVVm9FH1UC2sQTzfRbTuFzYlaCFTKXlLrN3OpyWWSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIgn70KmzhfSvAzPGc4ya7DWAohpelbaKWaF-gm8VKQbsxIKnYvt0AktMfGvaSElFjt6DptLMZ0IAu7H5UnIf0l0lKrc5JKssXE58tMmXzDPnKjuugiTsYFJoLXzPFONkSa7T1Vvgu_mrX81iFdMoh4L_HUbCqDhbBQhI6vqWrYVhITaoxEiJh57QPTs4a44Zp2AIazX2SA8yCZHhhkZ0tnrkFIGYBJVvLADjjXBa-TEUKVdvZMg7Tyz8Xwt8VBdt7FhNTeZhisNpjYVQZsGMh8Nb4mc42CdgpvP3h8I1NZaGSIjKIkVbsEhD9cu_oQSGxYulb6l1-Nw0YbO6NQCDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rktgxvxOCiJLw61hk9I8EtmPcq3CEIgwPIqC4ADa6IOM-m0Nxd0XUfKQdlPdpp64dRGjw977vV6EEh3RIGLMD2qEMyNJPl93bfWfjLb5U1ztWkFh3lZCVlLVAVbPO6EHQehGP9sAad067zKgjkLkbAaarRDhjCmzdyGzLHKR5W01oH1m32ykluoqP7LwxAg8qH-dUhipMRW41oClDVK4i98aMVguHcMz5q1sPOH51d4aiPHdpJuzDpLIhiQZm0-UiHgD8AU57a2uXqEBmCeDmLgJwdcyvhMk-hg-lVKU4tyDqAppRPDm4JvUztqEoOy9zYqDA9hw2A0QZ9sqkhUEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iH8zXQsUINytGBAzJWqM9Qxe3q6dJrwO4WcjQQfGwKu2pO6GNJY_7E_1-Oiqb2izaDCQd4f4hYC49_fNu8FNHhjFbnHZ47YZL2lWH3v5jyuXbYKmdcRY4OwiHPSKPRQjVst-GbG5278rzr3F0eBMVWm3NIPOo83IWQOoEwpyLi1dwwLHKrvgRgecTli15USm4KmY0Fesx_sKkcPSKW83gEgWrXLmqz5IDr2jI4MwqVGUp7sjpBZHqD5V55IGE3tmGDJbRe8_vIhfyvjvc832O4Tm-Ow1d8WpQHrfDmm3p8oB5theeN2kKjAfk28shaFPG4CYcFme7YNmZkJ9FM0ybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DtI9_Z4XtYZXi42O_ZVi6LMozIGxlIlv_2fuMvw6acY-akmy_zecHrWjB3jqsWC5GwIQFLlxAGOJU9zobjZ5bERZ8JjTLRrkzx8HXnLlj1q3XL60gvhVunN--geh25GdD-50VvT_Jp-3HQ7xipxbAGmYghupPZ2RULCtIXuJF-rM4qTse4XCGHUxATBStyBNRZK2kT1y8CX3Bmf17ufTIaamUrqaaxZRyNq7FqkZI9jyfveoNivBYipV3aMAxwMalaiW5BylaAkh5ykAmVkwAq_Y7mYxNjRfIvoCYk41RsgM1VxOsPMWA_do8WRZw6oqP8lWPpPn_lcRC0HMqhMdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tpCkF_0l498qKtCUGemB2bmv6TBoaaJaObjZ7i42hk_-qpH-tqA6SRxSTsPjjrKNGSeJpgTfIU5X8lX9u_WXqFuMLo12Fndg-auNPQQmZVMRY9xZJGUADpjJaaVWO9yGknmFgpMJHksCrgKVwYThemSSjoPPzHuVP-8TZImZXlaLpDx2zHsR4zvu6oDDzxS0SyhqrlppMjRWZHMrnklhUqqFLuXj4PMtpMCjgpz7lZU78hIKwrZDhkYXSDb1MeBs7luYwfqRM5uPooSWw9svt8vW5h5VeF4zNoJCwBk8-64hcQG71JwBHihfkcq2RB_W5EuxpzW9sF_29ebpC6oxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOegGdLg3LszNeANBP9-zy66Bsiwi7mspO40J4LewKP6O8m3CRxz13GXGveDLItmGSp-CMpLWYjVga2b2Egyhs4W2Zvo88RegtlLzx6jqg6kfsBfG1-sya0l0A0Sm-bwtQ6O0l8GlBPHxwdkSrziYDFyrtqtrxDQg0QZau1Pt1czg5IMZ1e71T766aKTPlRT24bFwY3F_DHqmqHcGIcpQxEZyWUeRMPUEj9veUe4r_axEbjUxmY0m_eDF7oKotPGMhuUZAWyJCcj8FlE8f6Nxf_370T8QW0E9yAp9fNOs1qtSoi-LzXMHpzSv8cdy74Unrw9rni4vFvmYpyQZn7zGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMNKmmHLIzLMR_5S-tUdL_ZCWmG9h89Mv0hKNLBeiLlFgdqPGLfYwdJDtB9hb4Hdn7n9vJhHXYUp50FAPpih1Z95VZtitEpxVOAC_B-vtQ8ny_tvP0o3momyyWKbpmia3SWPNo7AvQVWDZexF81bV_tcj34-y810m8rfT_djeEt6nFKHpQuQ3q_mt6-wH55-1fw14cQZmrHHVBeMXx9ciUHh3ip89VygEqKp78z3ZXg52B0R5lt0f5mHkomRHvTaJXXs8nNVGqtN09cQRkCnNd8AKlc3O-zm52J2a5UDWb2hgk_KeTwrhgV4WeSTQxX6OKVvg1UgfwCVuHcjzV8SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hODCGTu_VXE1_Ra0484-OMavN97esrk05fYA8D5kfjuJZuacgVW-aeJeMfQkqzmz0LzxwpC9kQSKPxbF-lu_9aOOZjym5DbwJH1MBzkUoVg_4eZPpxBYCMlFeSP4oBlvNUHG8lsLuOvMSzqlk2xnNUXU1oJU4cUBy_IbiLWNafbzXiur6RcAj0ep1iy5gYcsEfegV35kEUyMMo-bE3yrbik8dCFcnOsFWPhoWjPwgWMYiU54KngEPRH7tVUZPF68lUWJbUz-6zVBjfDgRBYpiAALdlk9Rv10KKRqGM1rp3A7To3LY1WroOqgWnhV2C3tWaMugwa2jF0ro5-qlak1BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ov498EG0EwZ62wTVqL9RLdidCGwg7CvlczeaiMl6Q3JD5qphezFUuYWxfbGWOrDMrStd-ZgRGWdUG6Pkzt4WTYwF6d5BV8I_c59bKoCAGrOvmfd3H7kU8j7Wy3Rzyf5UJFMg2vyNnkHvCQVo07QeUQ4wwUtFgUGPiXmh3lau56F8QnK33ZozLPuU1O3RfnjFs2CsBmbNwOiKpNbyu5YvPQ5vf4ncm9GloPGJlb9vlZae4avVhoA0DdYUBIP2eUdbdzyZUBiqAh4ILZAi-wiDqQX9lnyuCHs3UrUejGwAJS2buYgrldZZD-uybVWupL-YcAziNycTdvOANkKXamX4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqvyBs5MlGpXm_3urPVLak8Ug0O4Hm5S70RfJeo1on26LkQxnI5WT7s777sVaqW7fq4czJ3ClVOlcqCpHdSICQX8V852AcG0V4VnLoNkVJTrTRMguK7vr5wCfAkXMVedZFg826e6oeLPCXAnxtJYCw298CzqeP75KMl73Skr2dDZz3SpS0bAnivtYAYwRAUj-kW3z2OKlTZAZisqa738tnbkriKaL29XbwxZc5xV8jd89J43eYDNis7t6abPXydih7blKmqnFk8jEnkzoonpgt8IippB7v18LjMasO_YpDy2RgK9ND-1CS1GUsFPywpQj3zPsYS0GnauH4f69miYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugxdQxn26kwKU2XAQVJqNVBn4Y0ri9eEjZJnPLdl3p_qzZ_ov8WR_7KLXv6-NA_8uLvLLMO_APR8XAdpo4rnLTQNOOyHcRzx_rf6rxGAhYjUy7Ft6papt1X0xIzRnOWOTP54Td0ThbRO6UPjOuD94kp9tfQORQ4hc79Ekjxit23kc7hlhpA3KPdphpjgiDriygaUbeOuk3nqQzWt0pZVyaL24g-P2krzvsLEIsHgM0qAfibn-9N_xg2i07RE4_gnDvlyUZ34V5s-4FDaDnHvauABId4TNVU9VE7-BVRwvNFvkUE7duTNsd0F9J5a-KmM4MnEG4WYtHCrGAikNrWP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npbr3mUO1hWBlKTakvvafZ1FixBCtTIem3sObHX36GTEgVIKvVz7CWax2DXRy7Jyr93hnjXmMxyEj9eKWCGHCwIgFHk3uUKyF7ipvQu4zQWOGIdr7OPNbzi4tz8bXscJMUCqoL48iIUDXICvNipdnGzq6WBN0zfwdlp9YF9wqzfAY9kq5ddF_-No0x3sUq1WBSoW5_b67S6cwLzNbbMixm7w_KrbCos9zSXiNycBXbbZcQbD6r8MNaJ3sIB3iCzEOMYE3T85WaFc7TNlNAGFb2zOxKq6YT7nfwE1-TA6z3TGyQwncaJTGm758uKghkjOK427lLySph8WCsKNJuCGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IIlrU6kYDbTpVIadEutnobrEo7XOluQIRnmnljf3wsfoc4iGMjq1zzju_Dr1K-ClRB464oW3M3E89OKq7PocQJ5wCmHHFyCrDxfEeJShhVH431bscfLoogc-sUG93oUK6Bz-pG18VGu07GLloTLIYIqp6Cb440aCV4hSrmUCTtYy8_0Xvg5TekWzAM3EysxVtdokMnBn_TDO1h07YXvtWZdbl4L2NFa0glqsIP2pA9tvwSrYffOlkP_gUiRyCVzdK1abMXYzEWXA1jXCuLFCdhnzUOs6WUEn1K0quIf50Hc2ZqTPSkZhkzkuu1OXVhwhMsYkreSPh5nSMTiqmiX3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kBBcRblc8JTWLdWjSNJjInRwPZYYJSdeMgEjq2QpvEQopWEfwJS28an_8m_WCK63rhJ1bygEyvTUa0rhKsxA5tmt_oHEhfJliC5utaoGz-tU6hsXGO4Q9jI5V1NILYIOQPCy1DPgI42X5d5C4oLtD9dT1j_1LlLIjISh2o8g9MkCOAK0DEAv96sEyU4O0ovqTTeDW_F33L6iEZijaI7RD9gWv_5ANNGifWIloSghiqq1JOEyX-btsz5kuM8Z-qUIIYSoSgYRwTYHTAkTBRWEl00DROWWuNi2oSVf-IoWrwA2G0MdjdJ65J0sMYJ1KeMPm6Hkqnl1IzoVZnuplBGw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fS0JZvolOI_aVxgOKFxpL4Bst_C3vJJIy6INKsOnXdu29gmYpHn7ZzIRuFgV_bIDU-VPaH30v3QiQn2d18mBELLOVqGgrLRee9OJvVrExyHLMF5fvoYGYYklYrVYRAZD7nLPltcS27lu6DjDdZgZa0cUXbkg5BfX9cNn0fzIvf6vkGYpgQAzNl9DSnyz_tMytdM-TbKGEV24mSyQiiqUdnvwDncH_srs5hztPf16LO4tbiyI5QWoxBcgdMtFskXa18MMhY08nrAEJmFw6QKfxmbnJHYMl14z57YPf88jVvaQNSPAd7695wpLJp9WpbXsOoP3dbGmVJrafy4dr3wMag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rd8ClEsbkp2Euu3h2z-wzrUL3bApL4fqOJdNyhyft_Z6kdI7K-ysWBujvN7PGpgzLVrazd7pFAWCXmQZEoJfgmD-yMuEcRartS-7DUf21tqMqSk0e2bzvdJXIxQyDltYSJLFkToLQp2PxrfdQVYpihlhz-06JWJAPwTzeLShyJ0BaH6om0Hro397pHurnbR6KEaTykyGM0jmRSN38OLKuBpmJ8fk54XcPGEFKr_Az4HVW8YbRw3W61bFcqMoTsL2NX4PzsnVY58ce8Xx5Y5O0zVwt51PQjDpO_EGg_137D91LMp4V8NUoTGuuSSXalwniN-qUk_fEwSN2SkkDv3CkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fEs9Weqpjq-f1C_jGa0-nSL0EguPrEoPQ3I2FzAQvDgOWZ8-eoKcO0ycLdrmAaWsZA1lxWWf027_v2EXOIxvmr0TxMdbDme0SZveuE5pfWrXkHILCUD1W8dka3LvRDQeMxZzLga-h94s9neDt6IEv2zWQvkLiv6XIp3OY8O55DkBboGISxhU0QM9TuU78dG-5igYSXfK2xHiegMKlPFoF_kUxaaWH2du32TmjjULou4oJt4_UABgbw2yOueneq2dgxxhRqQcukD8DDmfJu22aItIyMV41KXkmSYITWCPFHdk7zmb7RXfuueoxf2SBa5FnwnapxwOQxSlgdaCeZpbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l5-3a3shTAglZ9k48gs6KYQcbM7UC3d-U_I8a1d9jWq_ljvDnUNHnHPWLMCXc2vhL-D9tdM3EzhHCSClOIDgBDP41nYKZcDinGbbft3J-KTZ39GTpQHMbdcS3wMinqIyR6oeR0facqvX9DhbAkBI8B8fRgb7jkn3Id8NxRa-3qsZ2MYzO94hAxKYwTYXWy68VFUB4WU1SeWyJby89N4JBpPAv2g8n55okEbz32juVI3vZ9RYtQAYjZPiX6Mb-t_MzHvl5RY5o87o3ublkOcyH3xVVx4T4neiVIOpHLCrFbuB_qB-0l1uW8GQHrIqXZdFLKbnPj_Wj48t6I0i__5xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=ZcFli2OSprxTzA8TgPPR_qBx8XAdFWaIQcVu4IICIFUbVqYoxVGI6jZISVGhC0uLDJrQqjcAnsYjtVEB67zFMPnNS7i5x9v9TNRQPySKAIMJpCGnvXyo5eUIUl44QI1rWZJcLRqx2bAXPGgwKVQ0pgCf6r09x-eX8w4ql7mLpo21CQdtCOq0HaALSuLaNrc-YFMykhJWoJPUrsDS8zIVCSOwo2bGQSvR9wfco3YAb-k84u1jPWLnwi76CRbmytCC-KMkvP7Uz9rGHKks-nogye61rBNWae6P7F3RCBvftBqH28AeeOm9IyylMoig8ofURznWoB5gLTaXZuUDMwyKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=ZcFli2OSprxTzA8TgPPR_qBx8XAdFWaIQcVu4IICIFUbVqYoxVGI6jZISVGhC0uLDJrQqjcAnsYjtVEB67zFMPnNS7i5x9v9TNRQPySKAIMJpCGnvXyo5eUIUl44QI1rWZJcLRqx2bAXPGgwKVQ0pgCf6r09x-eX8w4ql7mLpo21CQdtCOq0HaALSuLaNrc-YFMykhJWoJPUrsDS8zIVCSOwo2bGQSvR9wfco3YAb-k84u1jPWLnwi76CRbmytCC-KMkvP7Uz9rGHKks-nogye61rBNWae6P7F3RCBvftBqH28AeeOm9IyylMoig8ofURznWoB5gLTaXZuUDMwyKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3dfgSzAGKALPp1638Ds3TgWkPDpGJe3rkLJokRhd3k3_8SqJLTsTIcvfOPdhO-KHDxyB63oEGliQPnuflwG637VSt8YkgobbZRJmYOJc-mHAW-Z-m4HeDNB3qpiccr6Pie2urHA4wGVCApLBN9RUQ2IOyhKHEeHDcqz3kHmi2KVtytFBMalxGnhXPIFm-dGERzr3eRhZyTI1hN69Sj0hPNjfXSJ5E4-4rA5-d7XltmvkRPfs6VYnTseNeW8bSGhRrtmMSLkfSjLc-v-gpTL9uVToOS_M-SgAdFPKaOG6BInWqPjhwNsMkLpNbtSxgf5pi5zeKuyPHuCWh_MdWjfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLEI96Ar9BI4IOgfhaxdy3UiuIb17AT3sO8kfGAZjZdvbJTh755fU5bmWxXCr9lLL7wkUQvEBHl1RlpNGOARoJkWYsd2-aEQT751s8hZPZuIkYbVkcCCER2GwMsQAvDZzyeNDdTCkm0zRkcm720FaeZZS_0Yo43gCBnpN-CF0YHz1p5nELMpDnDzz-CPsS01WhMlw5Q86iW67DvohkE62cZLVPY_EdzqlJQLUVLOomFqS-88BTeo4wWQ7JcyJ-cS3JwIP4SsUvdeIke0kWAjsfJlxBYLDcR_Ldf89vQfx--SmZ1acaNRF8F3hjKmCjWJn4mgMtStHmZuazSZfDst5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVEd_y2pp9_3i4lCOs4WyEwO5FQNei8pzOKJSaGOUec8xjhU7eLUt1NKzH_y2DN4ki8lo0eKXhfG0hptiKTUn4QS1Z2RUZe2G4s8UaHLAwYktGAQo8hao5NLV1ArVT89PlvbReL6huAs-IYlaiG94AQmdKemEOf-aCAfpNLvSt1GmFsN3rKYS94gwtEpoZMYRsQCRAUtJI7oAyNI4Rgx9CqwjJz5Mn4oBO61HUrqzcXbj3blqg9CLt87ICTqtrGojapvNWxWFC0wwxUy6qaFaLvZhaczC55WhmeScM8YLVzKCJawBbTcS6EJgxtR4hMs_KuFoDvvRFJlnH0jLMrffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ai-news-bot-MatinSenPaii.zip</div>
  <div class="tg-doc-extra">50.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1- باید فایل .bat رو ادیت کنید و مسیر پوشه‌ی خودتون رو از فایل پایتون بهش بدید
2- من با venv و همه چیز گذاشتم که دردسر نصب یا ... نکشید
3- توی config.json هم باید api جمنای و توکن BotFather و آیدی عددی خودتون رو قرار بدید. توی این ویدئو اینها رو یاد دادم که چه شکلی بگیرید:
https://www.youtube.com/watch?v=7qYPK3dGoK4</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qDA_2mv4R-a-3QeOyECgaerdpcLDcLIFrUFr6l0V3DFoAKfus-d335hdkK-m_ZZqgebx6p0g5Yr286ZQfkwMGlUkcVkjGW5BKbxaNHOwWkMQLXLxR4Znn3hA8-4hGPcd3nJg2cvfE-v1wTPbs2jW_gLfeLe-UHKjml-wqxslWrJrrdoYpWEuZ36pydQ_IW0MoHJRGkJKrlusfXLI3uX-3p5dbs_0pQcdM_5GNibT0pK3r2gVBqsnNLDJdZrDYvWxV3nm5nuWJEHb_APi8oQTSaClNmmYBzD8PLdWiqAlJt56HI_vQ8JDuLiY4U0Z4TWwY3GM4El_Bb5cZuSlRPgCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJfOYblzl1gMtcV90Nji2wM8dHfcfaEcTu_JO9gXZIWoKZR_7RauNRw7sjHt-KKqrNpkId79MluR5bAD43jAV6gclecWhBAIu_-RO7xo6GYVb5176R3i6c7XwzNZwHraYM7hGuW99TTZYhQ2g9oQSBSVZZ-9PR4PyV7yvVGKOK5h0DCHfqTyAVWaPQgBl59EJF7U6QbTpHmH8tus__z3AIve6WhYpqzKFQm8UncokOnLlh0C9V8kiBHlnlwWnMJ7U0uT29gTXSTVpJT3o4hHAeogcwrGe2L5YQgUxiJEsrGvtEv5uePsBCuIgzvW1xJHv_gDq9uuJbVYYVyPsNTWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fj-yzFYTgolXLaH-U7-3Uf7et0Jf0crlUJ0dxu6ZWbdEtGETW7mkBh2q0RQMXFdD866LI757Rzyu_BsyVvm37Ax37qiSi5mhN0KNK7fGl3cGsyZ2SwsTjwrkUwqVVfbM3aHfBYI3BfgrFHrka7pUs34cYdIxvM8XsRLi6G20jgusK74SRLwXPsFVkF5o213xm8GHZZBjBf841LJyc6JIT-HKV9jWnjBFaHU-WuYnlYw2rz20Jc26t6-bGGSccAiBnEpNJms-YZ70vxfgBrvXKYb0rOsVgEBkfbBKZrey2IJSyKncMZAUHpC-AWq4OuVMMyawHqqVMj09SDHMeLijow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rRUXRa-77JFRFCQF4_wspev7XW9VmxUNI7nh8uEy9L-OZzQUrM4NB6xFRtQ5T-23oPMolmTTNDVwMAbZhZkCVoaR9a6g6Sh7rTiwaNDbLSbrBYnZg7JOV6gJEK1whPxEW31RZFuntsf34UU7vuIlp76iVwE8PAMdrU5uzqiVNhU5hbDAPS5uvhZHUoEXtWSD3kxV2zwaPlVHwyofUkc0SOu-k-e9e6Ypw7UfJgqQwmeNVsztyJIbAYcckSAf50s8DnARs55Wawxayy0dVHhvkwomcrLfTuobZT4lESOBlXVBuRud9WY62tqWf476iQXMbWhBauMozJvkSglaudmZ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!
توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini 3.5 flash lite ترجمه‌ی روون می‌کنه به فارسی، و توی ربات تلگرامم می‌فرسته پیوی من. که خب کار ساده‌ایه و بهتون ایده میدم چه شکلی می‌تونید پیچیده‌ترش هم بکنید!
الان، شروع می‌کنم فرآیندی که این اسکریپت خیلی ساده رو ساختم، بهتون توضیح می‌دم.
1- اولین کار، گرفتن API ها بود. از Nara Router تونستم 7 میلیون توکن رایگان روزانه بگیرم که اینجا گفتم چه شکلی:
https://t.me/MatinSenPaii/4061
و همینطور از
https://aistudio.google.com
هم یه api رایگان جمنای گرفتم. که مدلهای دیگه‌اش به درد نمیخورن از لحاظ لیمیت، ولی مدل Gemini 3.1 flash lite واقعا توی لیمیت‌ها خداست. 500 تا ریکوئست روزانه و 250 کا توکن که اصلا پر نمیشه. برای ترجمه عالیه. اما برای خود Hermes مناسب نیستش چون که TPM بالایی مصرف می‌کنه و Exceed میشه.
2- توی Hermes، از قسمت مدل‌ها،  Nara رو اضافه کردم. خودش اتوماتیک تشخیص داد و گفت کدوم مدلش رو می‌خوای؟ گفتم mimo pro 2.5(که در حال حاضر رایگانه توی Nara اما خب واقعا توکن مصرفیش هم بد نبود برای تسک من).
3- وارد چت Hermes شدم، و چیزی که می‌خواستم رو بهش گفتم. گفتم که می‌خوام یه ربات تلگرام بنویسی که هر بار رانش می‌کنم، آخرین اخبار ai رو با api جمنای بگیره، و حتما از مدل gemini-3.1-flash-lite استفاده کنه و عینا همین.(اگر نگید دقیقا یهو میره مدل 2.0 رو میذاره بدبخت میشید) و برام بفرسته.
5- سری اول ربات رو ساخت، و بعدش بهش گفتم یه سری قابلیت اضافه کنه. مثلا زمانش رو بگه که چقدر وقت پیش بوده یا فرمت بندی رو درست کنه. همینطور گفتم که برام یه اسکریپت ویندوزی بنویسه که هر بار کلیک کردم روش، این رو ران کنه( این شکلی راحتترم خودم)
6- همونطور که توی تصویر می‌بینید، خیلی تمیز برداشت خبر GPT 5.6 که واقعا هم سه ساعت پیش اومده بود رو پوشش داد، همینطور خبر های دیگه که یکی از نیازهای روزمره‌ی من رو برطرف کرد تا حدی. که یه دید کلی نسبت به اخبار ai روز داشته باشم. سورس کدش رو هم براتون پست می‌کنم که اگر دوست داشتید، تست کنید. هرچند چیز خاصی نیست؛ خودتون می‌تونید بهترش رو بنویسید
7- چطوری می‌تونید بیشتر درگیرش بشید؟
بیاید با همین "بات جمع‌آوری اخبار مربوط به ai" مثال بزنم.
شما می‌تونید این رو روی یه سرور لینوکسی ران کنید که 24/7 ران باشه و هر خبر جدیدی اومد، درجا بفرسته واستون. یا حتی ببریدش روی worker کلودفلر. و هر یه ساعت یه بار چک کنه، اگر خبر جدیدی اومده باشه واستون بفرسته
همینطور می‌تونید یه سیستم پست‌ساز نیمه خودکار بسازید برای تلگرام و بدید که پست بسازه برای چنلتون(و این وسط توسط خودتون یا یه agent هوش مصنوعی دیگه review بشه!)
خلاصه که راه برای درگیر شدن باهاش زیاده. کمی تایم بذارید، و کار با این ابزارهای جدید رو یاد بگیرید. من هم خودم اول یادگیری هستم طبیعتا:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9TPfIu-nnjT1dsuZEQEZ83-RNADC85tQ72I7JnVOm2EzzFFK7kYDc4lYzSdkxruQ3iOHs-R8AuPiVTSFQ8t1fGWrsIFplItA_twfKWuNU9wO1AWYTzmAM-vTUMPOiWj0oqj93auL1qCU0Mgeth65UG05czuWeKgsGaVw5nLsQRf0NmZd9i5HVNTQb4lG4obfUEjBI_5jc4XDoINcELNcE_xNxrSgkwCI9Q4Sg3usdySjz6je32B_zYnh3-DZjAMaCQqHrdC2MEMOdKfdgy-ljpLqi9eHa6m1vkZrfYRTWpSDbWD3SIxQQDownFrIKwo_vSYA_6RadmD4oTl553Byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=na2rzal7di_MWyJOwFHPM3nmfODzr0ERD-4FG0dbGbh3PB8qv3oip_FlvA66OSeHoK5u8kIqPNXKQSfhHyzBx1z289GuwDzuT6nO-R8MB3XARSUL9tmnYPgc1j9WaFetkcx6PaPSP7ORfXd0a46DEWWf4qOePWGwH-EvFdMoa1TTyZgOA_wvWKIXJ7BpfSLJ2uPnxqB9itnK0fYw_R6X48GFzThpgpkqKHqoK4EGs8mYj4Pn6L65nV4Rt1-_d1auOblT3Rj7fmpZhgrUrenc3OSueVmuZsbZS0TuRkHtX7rhflxcuKRnvYeTZhHlWWJc9k_pk3gcJ6jUgNufq7kYt5w2SdWtMKKiM57NKMd99i4h_8t7hHI8LfS9fZcXy_BhczbfxNH2_JZPbVbCNGf1yQZ2zvPddYVAoPA0w1BrKBruptYC6CEESK_LPQisEmY5kz-0tmj6977tI1w4KKP3C3ST9zY76zQkGHktfFq_s0U5EwZ5u8O06b3ZVfI0-w5HBKlXRldPrxrSjNDi1tcJX_2IDAEAqyXp7JR3fxfM01MlTbTEYRzbEJHiiG0JVWUFjmDFTjNgU6-Be6HMHnbEh4FCtzMBMwjO6Dc1TRhmmUUvJRmeYM1JD9J8tYoEHwaTX_-3mbUEbCk5EsdA9Drix1wbz0-yVLSs1DMMYBtanew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=na2rzal7di_MWyJOwFHPM3nmfODzr0ERD-4FG0dbGbh3PB8qv3oip_FlvA66OSeHoK5u8kIqPNXKQSfhHyzBx1z289GuwDzuT6nO-R8MB3XARSUL9tmnYPgc1j9WaFetkcx6PaPSP7ORfXd0a46DEWWf4qOePWGwH-EvFdMoa1TTyZgOA_wvWKIXJ7BpfSLJ2uPnxqB9itnK0fYw_R6X48GFzThpgpkqKHqoK4EGs8mYj4Pn6L65nV4Rt1-_d1auOblT3Rj7fmpZhgrUrenc3OSueVmuZsbZS0TuRkHtX7rhflxcuKRnvYeTZhHlWWJc9k_pk3gcJ6jUgNufq7kYt5w2SdWtMKKiM57NKMd99i4h_8t7hHI8LfS9fZcXy_BhczbfxNH2_JZPbVbCNGf1yQZ2zvPddYVAoPA0w1BrKBruptYC6CEESK_LPQisEmY5kz-0tmj6977tI1w4KKP3C3ST9zY76zQkGHktfFq_s0U5EwZ5u8O06b3ZVfI0-w5HBKlXRldPrxrSjNDi1tcJX_2IDAEAqyXp7JR3fxfM01MlTbTEYRzbEJHiiG0JVWUFjmDFTjNgU6-Be6HMHnbEh4FCtzMBMwjO6Dc1TRhmmUUvJRmeYM1JD9J8tYoEHwaTX_-3mbUEbCk5EsdA9Drix1wbz0-yVLSs1DMMYBtanew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XrUM28TFolUxriUwgNsgueVNlQ8dQID6xD3sXAKjzlZGMJaC5sMvM2JdDgQ8CFcH2LmqYxUsxMTsl-aPaffsSOu8nXK-GseJeHwbkanSMtHtG8gzaUhoAuWZB6kd5pcajhE6NIMPWZoULFhiixR1sCVMdAa61tfN2KSyCYXdNsFVKqJbjtH54iO2NLzVY11H3TTa2tbBB_1ngyhmBWj7ACaM4k2xXVgCa91sE5NDxTM0g4ahoc1QdOqdGkHjA7kuz53wpYdAwxzcqaU6VUpZD80_e4zWQt0KOJCcgLhXGN8SJvnKM9esGoxt_NrULjo0ub8R9jd65qhOZNgUrpxOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/db2tNqxKd99kF7FDoaO26O3Ba1V9FxNUPycu-6x5lTO2xf2OqhA0LVgdpAbxpQo25Z9t_0DDM39TBGB-msUp3xNQ0Bk3KHz_jjGhXCfCmDbquGx9ISszDsmIvajHDIgSSR2luZZDYQ1M-3EhgLmOsSYG-6LdWB81hfPn5UNJAYn4-tkeWe6C6MOgY66ebf0NyLrx61jnLc7B4QRhZszKL4S2STwqJaC3n9sI2lfvNHjo8o7oZ9pRgHv4sDO-Xx2Eg7jlfRwE6iVr5FWWRDifZd3fwJtDFDdQwBEMRBa1Nn20cDKsn2vOS9OQZ4A6xRjnTkUVOfVryHamLj6DEOI3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4046">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این نت دیتاسنترا کی می‌خواد مثل آدم وصل بشه من نمی‌دونم.
فکر کنم جدی جدی کابلا رو بریدن الان نمی‌دونن کدومش مال کدومه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4046" target="_blank">📅 13:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">موشک ملی‌شکن
🔥
@HexConfigs.npvt</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4045" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYKJp4Y-H3hnQrHaRIF-3oC4S2PP9wtw3ClPXgjFS2Wp2yv90xYKE2W70hRUJ_62UDWE2neoV_SWoPf6jEuHvkUalFe2Ir436rDnJVj42_7_3_V2PT-ltXmBgukfC06bJryT1qGoWLDwAszSozemMZX-kSVoYuN6zn92XxaGNTupv6NjD3a1KBaYVIBwZHGP4o7_PZaXeXjSIO3QYXtSWqO7fxTwoeQcwCARCNcnXtce6BIhCMrUUYUBvVmOozF6LyIN0ePyc2hAyzXjEtMpEq6E4N0pZ4SQfmrPV1juWYKJtAPtn1HgSTFIVyi5RL2xcI86hAvBrki66b24QPV0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4044" target="_blank">📅 13:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB
۱۰۰ دلار میده
باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4043" target="_blank">📅 13:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چندتا نکته:
1- کاربرا توی ردیت گزارش دادن که برای استفاده از مدلهای anthropic زیاد به باگ می‌خورن و علت می‌تونه استفاده سایت از apiهای دزدی باشه. بهترین نتیجه رو با GLM میده
2- اگر از GLM استفاده می‌کنید هم، یا به ایجنت فول اکسس ندید(که .env) و اینهاتون رو نخونه، یا توی پروژه‌های حساس ازش استفاده نکنید</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4042" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlZ76BwxU7OuaIPXCqjdByRjBgR2iCBznUb-wn6rgBoTO1lxHjO0TF5xRwkVjMLnit4c0XLbt3D0rBPTqk4DKx8wiuBVQGzGTKNlEHHYM7abSNORoyHn7nNRcl9v-iW5GWYloneNAX8_bQIiyWuQO7dcWY2kRwk1yBlPkFstgKeZb1bHkYvNqbzCp4Uz1dPFVYEiwDobX0Gk2Z62qidnYx-GLTQt6eyd-Px1GC8yiJbeuUbnuxz4Kcrq3flV_rmco5qDcpjLNIWF58Z450tkT9GqXK61knOt2OYEA2zmUgj_-cQDwSeTXLJn05kEmHaEuRfR46w8AhkJtcPFy8HQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایپی 188.114.97.6 دیگه سفید مطلق نیست و با ایپی های دیگه کلودفلر فرقی نداره. /// البته رو بیشتر نت ها به غیر ایرانسل کانکشن خاکستری نداریم و به راحتی میشه به کانفیگ های پشت کلودفلر وصل شد. برای ایرانسل (و بعضی نتهای دیگر در برخی مناطق) هم با استفاده از فرگمنت…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4041" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MubLsOJ6gom_sm00ujUazKICCSfrgBhcA2suJcQu37Y_5SwWJTKQaDjeb9GNGCiTna9L4U1ZJWlKZq3gMYVrR2G6bX1zjM2lgCHFuqSU_MWs7qV3SSUwufDH1fOuCbzx1kZs0_CTzIrWFeVd7mG9aQ3OQrqF9ugGQLtR5tW4twMl7aXzgNPSW__0X-tSlzKCPF48JKgG-gcJWhSQ9a2WkR2Hge8x66Afcpm3DxErR_hXur-lNJZOzSgEQlpewsfuAX-ynWWOkLOdoqZcj058E3l5F2bKC7JxQQByFWmIfJCKazaHRW_bpOVR13xzFy5SApgg1uzYyfaSFFRwETq2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4040" target="_blank">📅 07:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BO9jR72OYhZIiDxg9kvyRcb1nGd_GVdMyOHIVHo5B95SXPa1ESTr95GzEqTOd7mAQm9CrFEdbj6S1IRyz_eVvuBX9TxjPlGVUKJuASRIdd-1WK-Yg1GujrV13cn3RWJ7NI6Pf4UurxBMBec1tpF4p0Sr-jJerWHiS66y8_Q5Wn7O8qzT64kMKWvcs2GHcNdi7V2lLKCibkTg4Bq_Z6q6qWfHSqy63VeNuDGe7zYNzdM613-oswpTxqMJ12zzSZPtVzc2ZIQ4vEC4Gf0JFDkH5TQmEK5rFJxAqRrU7VPJteqhydPGyyQnyP_Z0OMEge-VBBjl-5XBsyAuzhDKap8skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/McrzWpTXL9_UjxRHNzFPyAC7ASeoTT7gw5nfkPITlc4UtP6_1-wyj9qID0KDtpfnp3Rq0Gg6kG_Rbh32A6f_S1rhuKU-9BXUgrCAsaHEsIBk9q9Fdf22VLbFgoBix9f3H9WAa3TnyjBNrAOkbUzUsJFq0e68sO895y_F2wezUIkOcHXlGQ0F_gR3BpplMhJP0sKdtFbIlJ5vXpo3KY7qnB0CMX4CYGt1bX7WDrur20xLlKXnKozkAgBmJ_XEQ9aZtBoC0Mf8aOWssm8dQ5q6QuADcDt-bxDWFLpoD8QqDy1TLiZRuYW8KYtaMQzziyh3ZuOUd-sJdpFVDrXpGcwXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.
عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:
https://t.me/MatinSenPaii/4023
)
این ربات تلگرامی که One Shot کرد، کلی چیز داشت که اصلا من بهش نگفته بودم اما چون صرفا فکر کرده بود که "منطقا" باید وجود داشته باشن، خودش نوشت. که خب هم خوبه هم بد.
و واقعا نتیجه 20 برابر خفن‌تر از باتی بود که با MiMo(که خب بنده خدا مدل رایگان بود) نوشتم توی ویدئو:
1- بعد از اینکه ویدئو رو میفرسته، خودش پاک می‌کنه( از روی دیسک )
2- به لیمیت Bot-API تلگرام اهمیت داد و محدودیت حجم 50 مگابایتی دیفالت(قابل تغییر در صورت ساخت local-tg-api شخصی) گذاشت.
3- کدها به شدت تمیز و مرتب و با structure درست نوشته شدن
4- خودش چندین بار همه‌ی فابلیت‌ها رو تست کرد و تا مطمئن نشد که هیچ مشکلی وجود نداره، تسک رو تموم نکرد.
5- بزرگترین تفاوتش با MiMo این بود که میمو صرفا تف کاری کرد که یه چیزی باشه که جواب بده. یعنی اصلا فکر نکرده بود که این قراره یوزر بیاد روش، روی سرور ران بشه، قابلیت سرچ کاربرا باید چطوری باشه، لیمیت داشته باشه حجم، و... . اما GLM کاملا فکر اینجاها رو کرده بود بدون اینکه بپرسه حتی
6- مهمتر از همه، یک بار فقط بهش گفتم و همه رو نوشت. نه گیر کرد، نه اشتباهی کرده بود.
حدودا 5 دلار مصرف کرد و حدود 140 کا توکن، که به نظرم ضریب دار حساب کرده خود AgentRouter برای GLM چون اونقدرا زیاد نبود کار، نهایتا 1 دلار باید مصرف میکرد برای همچین تسکی.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4037" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">می‌خوام همین رباتی که توی ویدئو نوشتم رو، با GLM-5.2 و همین api رایگان agentrouter که گرفتم بنویسم ببینم چند دلار مصرف می‌کنه. با همون پرامپت و با Cline اکستنشن VsCode</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4036" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4034" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/4033" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4030">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3OtbCaThgH6DhL0Wd3lMuApfTO8kqOsVzkNxbL5YAb7YlWx2zeuMpSOi6DfGQSgGUqFpWsGNqqaPK85_IYnW6Nn7bx2-lQcdhLUWJKlo5yt9taUUI5RxzVvdsX0CT0RA24CP1nDee6j-3iIp3QZhr02HGiC8FJvzMrSD8bZg5lLu7-1DOeg97iZY9CcHHQ5JxbMtUtjn1n4mTA4fJWwPlRDUSEFSNh1zj3186k9GDAFq3444_kPwr4UrRs_O6RCXyVyYYYde5q7IplKulOkQq8y0aNGP4-ejbuTasQMxDq0Yd8N2P4vT1WJM-Ur8LfReCEEsCyDa5PY_SrjSohGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر براتون سؤاله که چرا OpenCode انقدر شبیه به MiMo هست، باید بگم که میمو خودش Fork اوپن کد هست و بر اساس اون ساخته شده
🧮</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/4030" target="_blank">📅 23:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4029">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واقعا یه سری آیپی‌های تمیز کلودفلر، سرعت آپلودشون خیلی خیلی بیشتره. الان که ویدئو رو آپلود کردم متوجه شدم قشنگ.
خوشحالم از پیشنهاد دوستان که تست سرعت آپلود به اسکنر اضافه شد توی ورژن آخر</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4029" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4028">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شدیدا حس میکنم یه چیزی اشکال داره راجبش ولی نمیتونم ثابت کنم
😂
۱۵۰ دلار آخه؟</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4028" target="_blank">📅 22:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4023">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K8DJvtOBDu44gj2BXZoomY8qVno87gK6Cfubv7v_EZbJLnM2h87YK9QzaXJHPYGbafO3FWXD0ipQVoXl1CzHyAqK02t7lkSW0i2-UichZzZ2qCnqXXc1NPUObVGetxwcMkzJTk5Se7GzPAFbL6-4J2ZWRHGGd55SyRDjVP1ssXKT0x1nOePFfILVvAtIfLJB43F_LnOPTS8Lla6MxLbKN-0sRpt7Vj18AYKTfzgUYK92CX3N5LLvGfLMdZTnQMrxoAxwGM9gmf9xrl7ggg9HnIOGhr2YfL8tL2_ewca-evM-tdVoMZQBCnIK_JY2hUJZlwNzR5haVO5AOHGadrHqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AV4AHQYOKqTSbsMrxlCnaRxTv0Eo_KQKb1u2zSotX5GvLpNDLRd9jeALNzDCDYdwYgajZRbOE-7LyYYDQakyPuCzvluHDvmf0PFWVIIJxzbravzWmzg57S5l2OCXR4XSU3ReEeG1ztGVIffAZH36ElIsZfgLMcMy2g5uXfa9ByblRXWsz1Zng5HKdb3D8VtuwS3kTmDXP1tZiqyAeEcYrCf1YhpcELFYHACdSfSQzsrYOxvLIntqFrjaKsqQ_Cmb4GFROFKyA_TquRITRHh80W8eGPnZDAkX_oGX6XCNKfeSzoA-XhfXPC7fZA6wJ8O1boez1UYUtJVDXQ9RVBgoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XtPi1c2Xf6JUAOXJ5gG0c1lyva5TowpuNt6kgX0j3qnfZL3aJ-KlquuU-TgZRu-tT2e7AWT9kRYxKQtdF1AcA8CFh3mIZBwVSCgiPhYYAj45IlTSnkHub9oYUtQnBPD1ZYRkME47gIj2Q94PwleoPEBVWrTETfWmEaP3bHzDbjjOwawhFhhCaPR53exDai0GwvJuKESSNQUhhrN5L3rOYMVKXE5VF8iBYdTCn6HmbuA7L1BSUGwv7GmXE9lAhcd2GLORJUTzgBfAOyF2-IeyeTAZOxal96KTIfd_T2qHNVQqCVlPPsYyfAqemZ054MNSEXWX62ls7UCBmrX_9uvQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nIuyuX7-_ffouB0M2vGJTkSJ0zBR1sxAt55lmjG6BFgzsWc7CSxJt4sLxPdQwIEcHpps3IqecfjDGXnZqTfmZiYp7RSvROoj-c6g6nCBL1Qxm6ZuWRqLMfiJNxbkYctgGep-7rN7Hhp35jRXHNe9_BweVq18n5hOPvOMJhoeZHRN27ho-GsCM4NxoI8oxHorwme55gz34ltyZEQqo7PJT-UNodcjcPYNnXsE9s4qc2mprjdf-6RwNrrtkX6FHM4AQnU_jYNMfAkLBAMxjLKKYugil_zroLY-QsiCkNbV1TcBf-Y1-Fs0vXD3lWK2-DygqS1wBNvi-ZkCwLgVo1AY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p9MwsuLoRPI9UIt4fqfZaJjY58-Jyj0LrKEjITud78J3nVnD3e5mCYtM6hoSdYb9Fto2NPB82m4Y4YL0HyG1RMqjh_PRpl52X_fdn-c12j5sE8ezRdx9uo8M-OlHplhtqRNGFrIghQyRzCuVllKKRSuV1qqjwQ744AuFI5SmijUnNGHyXnwfPvIP_TYj-0KEt1WB5Qdy1qDS6OkEm9B5qhaC2mcPBynnMI_CcSM75QSn1Lwf6BJ71UPwpSFyWIAGOhklINaRDBJdhqOaEbmOWYHECTFwMx5xAu8i5Gnnpx0dRK5gR9zbj-i-AH7T3T1tJ_3FZi0oD7Sfsp9jmLMCJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این وبسایت، می‌تونید 150 دلار کردیت api برای مدل‌های
Claude Opus 4.8
Gpt 5.5
و غول چینی GLM 2.5
رو میده.
مهم: به این نکات توجه داشته باشید
https://t.me/MatinSenPaii/4042
منم الان 150 دلار رو گرفتم. با گیتهاب ثبت نام کردم ثبت نام عادی disable شده بود توسط ادمین.
برای موجودی بخش wallet رو چک نکنید. از منوی همبرگری سمت چپ، account settings رو بزنید، درست میشه طبق تصویر.
با تشکر از
شهریار
عزیز
فردا استفاده می‌کنم ببینم چطوره:) ایشالا که نبنده اکانت رو
من خودم با لینک رفرال ثبت نام کردم، فکر کنم ۱۰۰ دلار بیشتر بهتون میده(به جای ۵۰ دلار، ۱۵۰؟)؟ نمیدونم. این لینک رفرال منه اگه خواستید بزنید:
https://agentrouter.org/register?aff=PvaZ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4023" target="_blank">📅 22:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4022">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پارت 2:
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
پارت 1:
https://t.me/MatinSenPaii/4021
#MiMo</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4022" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4021">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S8L9LdwLqnrS-qShTI_6KYz_GjJy1dHDxaGQpnf9mm-zuxx7bRkxhbdyDVz2-JB_d91rC96b171b85mXnQaFlTnt7rcwE3AbGF5BYop7MwtijtAWJQUY-ijiyhDaTdarNrIO6o-5_WYJmSngCp-z-ZnqOd-MrInpK-zSuxjkBRKTns213phdnf45kYSfu8b9ZkUplj5Z20nTK2Nf-yls2e8scG9hXaJHJqpFQkKclCazfdk0JaKsfLjuzhZIde8lXpvuM_HaWUU0AWkHnfjgf646GXwWV7Y7afcwOSCPTgMEobxjKJu7hHKyPeOqJ5x6k8kskFX5U6PXA_b0VwJJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:
1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید:
https://grok.com
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای مختلف رو نصب کنیم روی سیستم عاملمون
2- ابزار MiMo Code رو نصب می‌کنیم
3- کار باهاش رو یاد میگیریم و مود‌های مختلفش رو بررسی می‌کنیم
4- یه ربات تلگرام تیک‌تاک دانلودر وایب کد(5 دقیقه) و وایب دی‌باگ(50 دقیقه
😂
) می‌کنیم
🤎
اسپانسر ویدئو:
شمع‌های دست‌ساز لیرا:
https://t.me/liracandles
❤️
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
✉️
پارت 2(بخش پروژه‌ای که می‌سازیم):
https://t.me/MatinSenPaii/4022
💰
دونیت</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/4021" target="_blank">📅 21:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توی ویدئو از عمد وایب کد کردم صفر تا صد. و قشنگ می‌بینید که Vibe Debugging ده برابر Vibe Coding زمان می‌بره
😂
😂</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/4020" target="_blank">📅 20:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ویدئوی امروز راجب Mimo code شیائومیه. و با پلن رایگانش یه بات تیک‌تاک دانلودر تلگرامی می‌نویسیم با یه پنل مدیریت کوچولو، که خب چون یوتوب به شدت حساسه روی ربات‌های دانلودر، مجبورم اون بخشش که ربات رو می‌نویسم و باهاش از تیک‌تاک دانلود می‌کنم رو اینجا جداگونه آپلود کنم</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/4019" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/4018" target="_blank">📅 16:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4017">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aPYjjyidLFB-uR2Tpkw-iubzjg3jBZrNcDTJK_oDftVB2z9eUZTuMyAHuQrrmh8eu8tfkVxPf_hNMee9PblVKuX1gnzpODzRNFAeB_vfK9sowQy1mp6khJKAeEA6ls7BP0R_meRBlgh7rRuIiin6vBYmiIqBSovzedAw6BAKLxnZ2_E-iofBU1tcO1Ot7bXcNXhN0cZHc_p77YZa6-aTsKddij_H0Z6-i2bNS5gHpGR6eQMihtvWD36_Llav7oWlmrlHUS84lF1qlTD9SOMg2-ydNBxOtyHz0yi3tHhA3msXxslM3N5AvxJHdFcb52GVuSoVO1wPO_KJXK3ByzGELQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تازه فهمیدم میشه با توییتر پریمیوم از grok پریمیوم استفاده کرد. بازم دست اون عزیزی که به من پریمیوم هدیه داد درد نکنه
گروک بیلد رو دیدم، جالب بود
خوبیش اینه که وقتی رقابت زیاد میشه، 1- یا قیمت اشتراکا میاد پایینتر یا 2- کیفیت بهتر میشه و میره به سمت تسک‌های ایجنتیک سنگین رو خوب(و بهتر از رقبا) انجام دادن. تا اینجا Mimo و GLM و مدل‌های چینی، واقعا توی هزینه و... همه رو میزنن</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4017" target="_blank">📅 16:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4016">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/St-8ZimdWOaEEIectJqyL8TLlgdsn3kZIV3h3js0aStUn9QmH2Hy0SsEJbOgg49Ckem1tCa45nyaRsiFuIrH5whqJ_hD1z-3Zgjp4uMQgsGwE5kHE3gWTapu-45QxP9owecP5KF2xWFOLbfwJFw8PdRUrOyXJG4LTbPqkCfzAIgxHTlDUAh8AuRDyBze5HmC4y9mr3r5nRz8iMeOYuIdi1xebbLiKwnnP71LnjYjPirmupSLt3l8Rg1SjMkRGlom7pgc07KA7EwNXr4lLpQnNW0BzBcBMUBqwC09bs5-9UND7hVF7T0HHKLhG7cgPKwCrCpGmSBJPRNAj2vk0pV6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه بیش از ۱۸۰ هزار star گیت‌هاب گرفت — یعنی سریع‌ترین رشد یه پروژه متن‌باز ایجنتی توی ۲۰۲۶. مجوزش هم MIT و کاملاً رایگانه.
تفاوتش با بقیه ایجنت‌ها اینه که نه صرفا یه دستیار کدنویسی تنهاست، نه یه wrapper ساده دور یه API. هرمس روی سرور/کامپیوتر تو زندگی می‌کنه، از هر تجربه‌ای یاد می‌گیره و هر روز کاربلدتر می‌شه.
مثلا دیشب که من بهش گفتم جدیدترین اخبار فیلم و سریال رو برام پیدا کن.
رفت که توی گوگل سرچ کنه، اما گوگل بلاکش کرد و نتونست.
به جاش از یه راه جایگزین استفاده کرد.
دفعه‌ی بعد، که اینجا پستش رو گذاشتم:
https://t.me/MatinSenPaii/4014
بهش گفتم که خب جدیدترین اخبار ai رو بیار
دیگه نرفت سراغ گوگل. چون یاد گرفته بود که گوگل روی آیپی من بلاک می‌کنه، برای همین مستقیم از ابزار جایگزینش استفاده کرد. که ما رو میرسونه به اولین و بهترین ویژگیش:
🤔
حلقه یادگیری بسته — قابلیت اصلی
این مهم‌ترین ویژگی هرمسه. بعد از هر اجرای task، هرمس یه لایه ارزیابی اضافه می‌کنه — نتیجه رو بررسی می‌کنه، الگوهای قابل استفاده رو استخراج می‌کنه و به صورت فایل‌های Skill ذخیره می‌کنه. دفعه بعد که مشکل مشابهی داشته باشی، به جای اینکه از صفر استدلال کنه، مستقیم از Skill آماده استفاده می‌کنه.
ادعای عملکردی‌شون هم اینه که ایجنت‌هایی با ۲۰+ Skill خودساخته، task‌های مشابه رو ۴۰٪ سریع‌تر (از نظر مصرف token و زمان) انجام می‌دن — که توسط TokenMix هم تایید شده.
📚
همه جا هست، با یه حافظه مشترک
تلگرام، دیسکورد، اسلک، واتساپ، سیگنال، ایمیل، CLI — یه ایجنت، یه حافظه، همه‌ی پلتفرم‌ها. به علاوه دو ماه پیش هم پشتیبانی از iMessage، WeChat و اندروید (از طریق Termux) اضافه شد.
💪
ابزارهای قدرتمند built-in
جستجوی وب، اتوماسیون مرورگر، vision، تولید تصویر، text-to-speech و استدلال چندمدله — همه از طریق یه اشتراک Nous Portal یا api ای که شما می‌دید بهش(اگر این قابلیبت‌ها رو داشته باشه مثلا جمنای) قابل دسترسه.
همینطور با Nous Portal، OpenRouter (بیش از ۲۰۰ مدل)، NovitaAI، NVIDIA NIM، Xiaomi MiMo، xAI/GLM، Kimi، OpenAI، Hugging Face یا endpoint شخصی خودت کار می‌کنه. با دستور hermes model بین مدل‌ها سوئیچ می‌کنی — بدون تغییر کد، بدون lock-in.
:
📆
زمان‌بندی طبیعی
زمان‌بندی با زبان طبیعی برای گزارش‌ها، بک‌آپ‌ها و briefingها — بدون نظارت، از طریق gateway اجرا می‌شه. یعنی می‌تونی بگی «هر صبح ساعت ۸ یه خلاصه از جدیدترین اخبار ai بفرست پیوی تلگرامم» و کار تمومه. مثل n8 n سر آدم کچل نمیشه.
🏆
اپ دسکتاپ (تازه اومده)
بیست روز پیش، Hermes Desktop به صورت public preview با نصب‌کننده‌ی native برای ویندوز، مک و لینوکس منتشر شد. اپ دسکتاپ از همون core مشترکه — config، API key، session، Skill و حافظه رو با CLI و gateway به اشتراک می‌ذاره. یه fork جدید نیست، فقط یه رابط گرافیکی روی همون ایجنته.
😎
حریم خصوصی و امنیت
تمام داده‌ها روی ماشین خودت می‌مونن. هیچ telemetry و trackingی نیست. از آپریل ۲۰۲۶ تا الان هیچ CVE عمومی‌ای برای هرمس گزارش نشده، و به صورت پیش‌فرض اسکن prompt injection و فیلتر credential هم داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4016" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4015">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب خب، دیروز فرصت نشد؛
امروز Hermes رو یه معرفی کامل می‌کنم</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4015" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ewud--E7XYPl8AqOe4sDaBGmd4IqcpYB83Qf6v9QqLryLIOIjjKe1312IqyAdTEjXVksYCSS8Ls1I2SizdslCAw-JdHjAEFDqrCyEhCmm1FMSxnRnqCQkVRJIYvkVym593BARohNzZiTXAwqPZOyr7pRRFQRv9Om5vwY8kGYksobcFdmXxcXjmw-k7eJjtKUDT2w9CZ9wnOqUVQraiaOv5K5woJputgo4yhGnSpBg_ETIhLg5jP1UzaiLgAUApGqCzhXvAMFLLZT6YghCj5scMjhEzBWy7PrMya6ufHY3Gy3Yj18gTQ7mCOs8Kk3bbwcHghi_7mMlbHr3I5wLhQ-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DlZVkjJunlPqXiCT5vPJXDMyZZIap6HKlPtV3LKIZyoZnzhyl8H-22TtvgzVNX_I-J1PfSH_rqYPPpgXvofC6nJU1DYCHqUdSJl5EY6UoKKRsRTE3wI-XKblA4vcOlt-ycFOi5DBhPZl3QGaizEAi994sZlRFNC0lHkHt7jXNYCN5qNPIfxcVke_6H48GERXahyHWsbVOBWKsfYOZfy7R8tYZzvqJwibmujjoeivU-MuQ3uaEbuNlwLpzZ7KLIp97FjveIpPJyFTDvCPNzSbGUrEL7a-uocgP-v7Wi3EXHp-N9yqERJtUDQRfjg_T1hsCqt22S2vOAzShc_FUve1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o4LF6mmmItktUK0tD38rmuYHANItUb0b0Nvzvp9F61oQSWUj-9fG2bw_Fxh-qham6bDs4wBCMSxeBEEELOKqzHc-xkdYjCJfIRyxE5NEkJmt55drH6OUY_EUR7ZhmC3bfbdq6rreg2P84Go9oK5gEvZok8kW8lRBZ_lltW89VPjsxPvsRxjSZxW-kUsvjBOPjcedTNR612J4ULCPRm3lUj4DS8Jo9NeApJkmFLyTGBxmRvyH6lrQMwjytgtmpoOAmcrJUgr1FVm0JYaps5V7bj1mmGmRnHzRVjfy1kyzfy0vqLlGKdZwdjxCNG0wJ1_2EDvxCbQCFplsFuQ25WTFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgLX9M-swfKE7cPj4O83HcpzblXsuxo_-nbx8D9A3M25LL6g0mMnAMpvdaAmo2tVtmVllxIDcXEv9plZx98BthF7U0fNRHhpEOdcZVFljXDBlHEAH2hsM8xmTF6K4bItr5AztVeOizkNBuiXET0dMmA5nw1YLbcgvQcTnKpA_fEik7BbKSPPp_zHiencKgehWcjdPmiMvBBarw0dTjP_RuLkEiDEFZfZe9T8nG3uwjzSSsJBCr46CKER93Ml390R0TIRAn_-Cpw3wrm9P-jiQsyKimFkmYXv73OCZWO1yeEei9h6QbK5FoaV17xz3jdN4AXuZlQB5UJ1iDU4R_AP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDClRn6fTe_6pIgN0z57nmk8Q2m_xr2n5fAxdZMK7tHc8ya-_1-gIiBwwpfTffSt5ixAswJZLsjGVWch1rgq0A735wpZEWwYKMmszUg2KJb1zahcgvyGF-KSKgggemyzmQO_CNl7HqBpmY84TRcc1Fup-h3ytdnZTptZQOy0jKzvguk0xGeRhVZPnJlhkiHmkYW9WYAuwDb3H7whVGdNfWdFrVUFta3Y2NWqayq1_ztLyXPoZgOR7PlDtvDVNZTy6i56j32zIS11zCi00tiWui0ETd7gDzsYqHFC6ys5pGpTlBTSqfnsPlOM7PDUJfrG3RxVIBtd9CTmKYx7-fC1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pak_JuGTv03Cyx-2GJk41wz2REmBYgFWQKI8crmZR_q7QBE_AUUbp9KcTjW8yFZf1ehflQ1mD0t9ueaeLkobOm2e9kuZuxcpc_lBfstVgwFVg6au7Yn2c9IlfXfn7SuuGAcywFeWh071iWwQBH7dWnStQrwGB22sc_ht9pFBVflxa7tzBdB-IUO--J8DEr-3PYxKee-jhiRjMPNFBWtd7Ls2Y0yJmvVrjHQH9VKzHm-JGElVZQ-UokSR2f2ehm4P6phUwrLslGyUfE8uvaWq-ZqzvT4NqGYTWVLEoxM-I2VxjMAxE5V9fRyZnthG313W2u0Q0wG25sGcui9XL3V_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
