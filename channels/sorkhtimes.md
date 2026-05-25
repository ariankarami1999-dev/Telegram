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
<img src="https://cdn4.telesco.pe/file/OQdFS8p7admIQ0dQJUIAhcgxEIYB-MWg6Hz2_WksEfOBMutrdeLYyYNyxB7sYsXl25UJjWq4-4wkffKK7Pl6g1hZD2LYS1vLZZBv6XmQX6WwyiT7wpGyaXZaxZu-jTBTyMpDl0IJZJTjXMieFgIVA1TYVWGJnfsJ21EgzBAVRtsYfbAU27itIeDXrQk8eH2Ld7x32sLD-oBAZNptMHYxDcoZsoeAEy9jRZt96X98YmD6lxyYKGK-0BE74ZG1XBTpcEHNv6UEUdwUXR7SCM3aPzg9uFfSJahFJ5LIpeJyFtLVrOy2W_o1idD3VbDFERdfo1HzhMiXfFZc64MifLfJiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 23:51:20</div>
<hr>

<div class="tg-post" id="msg-132219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 224 · <a href="https://t.me/SorkhTimes/132219" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132218">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
1 گیگ 200T 2 گیگ 400T 3 گیگ 600T 5 گیگ 870T 10 گیگ 1.5T  به مدت ۴۸ ساعت
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود  جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 298 · <a href="https://t.me/SorkhTimes/132218" target="_blank">📅 23:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132217">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOVix4NULxQoQd4jbhKwQOkVMzrQDqzgZfUFPlqubH3430gYfK2Qu5F9sKB9aNznv85CJ7Pbd8J9AcekSnL9QM-Vg3Is4vB20Yx2Kf_jGzrHYPD-CNnr9B0mEq_sWBI5ZXB8FBkZdQ8oVWT3pmGNYeYQENXYXX88YC27TFKJCUII8yYGbTXxOM_mtE9ysTffhGZ5hBp2TXq8wf3ilsfxt7ZgjcSZrNhZHj9Xnr4WuRUv07fve-cwQSFZ9YAna1LwEsFKxdqm3F-WNC_-j35jLpUnObPpXfTZMCzFB8BQX2f5z76inGcQkFSDGrGmmRrNAOujFjJN4mNp1aq-hKgywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پیام‌ نیازمند در جدیدترین آپدیت سایت ترانسفرمارکت با ارزش ترین گلر ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 376 · <a href="https://t.me/SorkhTimes/132217" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132216">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔰
آف ویژه
سرویس VIP
🔰
1 گیگ 200T
2 گیگ 400T
3 گیگ 600T
5 گیگ 870T
10 گیگ 1.5T
به مدت ۴۸ ساعت
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 424 · <a href="https://t.me/SorkhTimes/132216" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132215">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
👈
نورالدین الدغیر خبرنگار الجزیره: احتمال دارد اسرائیل پیش از هر توافق ایران و آمریکا، دست به یک عملیات نظامی بزرگ در لبنان بزند
🔴
با هدف استفاده از فرصت زمانی باقی‌مانده تا توافق ایران و آمریکا.
🔴
یا برای به شکست کشاندن توافقی که بر توقف جنگ در جبهه لبنان…</div>
<div class="tg-footer">👁️ 476 · <a href="https://t.me/SorkhTimes/132215" target="_blank">📅 22:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132214">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 558 · <a href="https://t.me/SorkhTimes/132214" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132213">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
و بلاخره بعد از نود روز وصل شدن نت بین الملل و شاهد خواهیم بود ...حال الان کانفینگ فروش و خریدارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 597 · <a href="https://t.me/SorkhTimes/132213" target="_blank">📅 22:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132212">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XbCX5XVIxrR06qiLQ6OVCY8XSgHXErEEN0_XRRYDhS0y1I9ZuTU9rwKC7qeAdAcZjwlLRPQb1670yobhVQvdZv1ogRKrxPd2eb6_96pnJFBSJ1G0TKAaG7vvPcG5JGLCqA1lAXI8Wz7n1vsCOngwc1u4qXAS0f0uBZEQK03WfjWas8BWCSxOXN_nwkoBcEKZt5sWRxXH1QlsJkRxlFBo2sKUyMsfk3ZlPfgwQHyHb7OQ9l7aPLng23V8rzz_fMcFXFzYMpeYlkSfrK_NGUejbwtkSqG_J0MctSBY5u_Bf5K1O3hI7fD1ZYY43dt7SBo3nWNLYEXCETGYX5Aqnrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 587 · <a href="https://t.me/SorkhTimes/132212" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🚨
خبرگزاری های داخلی خبر دادند که اینترنت بین‌الملل از فردا به تدریج در سراسر کشور وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 592 · <a href="https://t.me/SorkhTimes/132211" target="_blank">📅 22:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132210">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 574 · <a href="https://t.me/SorkhTimes/132210" target="_blank">📅 22:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">▪
︎ اگه این روزا بخاطر ضعیف بودن اینترنت سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 565 · <a href="https://t.me/SorkhTimes/132208" target="_blank">📅 22:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
ادعای عاصم منیر:
🟢
توافق ایران و آمریکا در آستانه نهایی شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/SorkhTimes/132207" target="_blank">📅 22:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132206">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/SorkhTimes/132206" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ورزش سه: پرسپولیس از رقابت های آسیایی کنار گذاشته شد و استقلال، تراکتور و سپاهان (درصورت تایید مجوز حرفه ای) آسیایی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/SorkhTimes/132205" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
خبرگزاری فارس: مسعود پزشکیان فردا سه‌شنبه مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه را امضا و به وزارت ارتباطات ابلاغ می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/SorkhTimes/132204" target="_blank">📅 21:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
تغییر نظر عجیب فدراسیون فوتبال با پیشنهاد سازمان لیگ
❌
در حالی که طبق ادعای مسئولان ارشد فدراسیون فوتبال قرار بود فردا (سه شنبه) جلسه وبیناری بین مهدی تاج و معاون کمیته اجرایی AFC  برای گرفتن فرصت مجدد برای معرفی تیم های آسیایی برگزار شود، هیئت رئیسه فدراسیون…</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/SorkhTimes/132203" target="_blank">📅 21:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132200">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/SorkhTimes/132200" target="_blank">📅 20:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132199">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
خبرگزاری تسنیم :
🔴
دستور رفع محدودیت های اینترنت بین الملل تایید شده و فقط به تایید نهایی پزشکیان نیاز داره ، در صورت تایید اینترنت بین الملل تا هفته ی آینده به حالت قبل جنگ برمیگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/SorkhTimes/132199" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132198">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SorkhTimes/132198" target="_blank">📅 19:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132197">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
تغییر نظر عجیب فدراسیون فوتبال با پیشنهاد سازمان لیگ
❌
در حالی که طبق ادعای مسئولان ارشد فدراسیون فوتبال قرار بود فردا (سه شنبه) جلسه وبیناری بین مهدی تاج و معاون کمیته اجرایی AFC  برای گرفتن فرصت مجدد برای معرفی تیم های آسیایی برگزار شود، هیئت رئیسه فدراسیون فوتبال امروز تشکیل جلسه داده و ظاهرا با معرفی سه تیم اول لیگ برای مسابقات آسیایی فصل بعد موافقت کرده است.
❌
این در شرایطی است که هنوز جلسه فدراسیون فوتبال با AFC برگزار نشده و سپاهان به عنوان تیم سوم جدول فعلی مجوز حرفه ای کسب نکرده و پرونده این باشگاه در کمیته استیناف بررسی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/SorkhTimes/132197" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132195">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
میزبانی مکزیک از ایران
⚪️
«کلودیا شین‌بام» رئیس‌جمهور مکزیک، رسماً اعلام کرد که تیم ملی فوتبال ایران به دلیل محدودیت‌های حضور در خاک آمریکا، در ایالت «باخا کالیفرنیا» مستقر خواهد شد.
⚪️
با تایید دولت مکزیک، تیم ملی ایران شهر «تیخوانا» را به عنوان مقر اصلی و محل تمرینات خود در طول مسابقات جام جهانی ۲۰۲۶ انتخاب کرده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SorkhTimes/132195" target="_blank">📅 19:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132194">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی جدول به آسیا معرفی خواهند شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/SorkhTimes/132194" target="_blank">📅 19:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
در حالی که فوتبال ایران تلاش می‌کند استانداردهای سخت‌گیرانه کنفدراسیون فوتبال آسیا (AFC) را برای دریافت مجوز حرفه‌ای پیاده‌سازی کند، اخبار واصله از باشگاه سپاهان اصفهان نشان می‌دهد که این باشگاه با چالش‌های جدی در مسیر دریافت این مجوز مواجه است. عدم بارگذاری به‌موقع مدارک و وجود بدهی‌های انباشته، اکنون باشگاه طلایی‌پوش اصفهان را در موقعیت دشواری قرار داده که اعتراض به کمیته استیناف آخرین تلاش آن‌ها برای خروج از این بن‌بست است.
🔺
سپاهانی‌ها اما در حالی به کمیته استیناف صدور مجوز حرفه‌ای پناه برده‌اند که عدم بارگذاری به موقع مدارک توسط آن‌ها کار را بسیار دشوار کرده است. سپاهان که حالا چشم امید به کمیته استیناف دارد، بسیار بعید است با قصوری که انجام داده بتواند مجوز حرفه‌ای خود را از کمیته استیناف دریافت کند؛ زیرا این باشگاه در بازه زمانی مقرر اقدام به بارگذاری مدارک نکرده و حالا کمیته استیناف هم همین موضوع را مدنظر قرار خواهد داد.
🔺
سپاهان که در جایگاه سوم جدول رده‌بندی لیگ برتر قرار دارد، با توجه به اتفاقات رخ داده در جنگ سوم، اکنون با مشکلات مالی نیز مواجه است و باید دید چه سرنوشتی در انتظار این تیم خواهد بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/SorkhTimes/132192" target="_blank">📅 17:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
پرشیانا اسپورت : لیموچی دومین بازیکن سپاهان که از پرسپولیس آفر دریافت کرده و اگر شرایط خوب پیش بره ، لیموچی به پر‌سپولیس میرود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SorkhTimes/132191" target="_blank">📅 17:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/SorkhTimes/132190" target="_blank">📅 16:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDqGcuh5c_BDpRtbtiBc44nvYeSANmD1KjeKSL3oGlizT8gt_42hqYEmf307FKpbzuvFJSgGV7VRHS3-RZVjuGTvf3CPx3v9o2t3XHeFQjDz16t5sf1vQaxqShQzsSyqyoM224rQXAOBml-tfUnh8inP13qDhL1BMFZiCWgFqFKwZZC7z0rsfsnqxsJPCKEHWOLs3gxl89AXAOtGrL3WcUYZEsyLD-8yVApxcHv7xBVjuE7zKqod0jJIDZwFEP_FHPFEM1L3BGZQeJoseWjX7yP_a5EGK_o96JjxSv-vP6NZVSRh6r0TQRl3gQ_eHei50XenkXHgh6KF9dRYbxpEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔽
فهرست ابتدایی ازبکستان برای جام‌جهانی با حضور اورونوف و سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/132188" target="_blank">📅 16:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
#فوری | خبرگزاری رویترز: مذاکرات در دوحه عمدتاً بر تنگه هرمز و اورانیوم غنی‌شده با غنای بالا متمرکز است
‼️
🔻
رئیس کل بانک مرکزی ایران بخشی از هیئت اعزامی به دوحه برای گفتگو در مورد احتمال آزادسازی دارایی‌های مسدود شده به عنوان بخشی از توافق نهایی است.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/SorkhTimes/132187" target="_blank">📅 16:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فاکس نیوز: امروز پزشکیان ، قالیباف و عراقچی رفتن قطر تا درمورد پایان جنگ و توافق گفتگو کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/132186" target="_blank">📅 16:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فاکس‌ نیوز :   ترامپ برای رسیدن به توافق نهایی ۷ روز‌ دیگر به ایران زمان داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/SorkhTimes/132185" target="_blank">📅 16:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132181">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔰
آف ویژه
سرویس VIP
🔰
🔥
10 گیگ
1.8T
فقط 1.4T
🔥
50 گیگ فقط و فقط 5.5T
🚀
50 گیگ به قیمت
40
گیگ…
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/132181" target="_blank">📅 15:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umUxa70bsHfH6e0DIZQU2hZfHfOZJKL0U9H9QoKncLlwxcCMvJusS1O46rBYl1KMcacan9E4rUvv5jSQko9q-hISiX_Ru7_fQYwwZgakG4dW6jf_lKa49_hLL86KFJu5MnF8kbvcc077glPh9tQ5EK5kWOtGHL4z3QDnAm829fprjrmrBf-oHPEaDvi9Vf1NWxU6F-Pr5q7vdWetjVD6qJ7W5VsU0rZ5JldKqS3Oyc7ueoB6bx5sLaCa-o2a3DFYQ1IVLzO0hXTgK9xPivwRNyvITNFT4w7n0X9XZG9LuDNAFf7SFsj6pGQZvQuBg2MCOx5dxd8asKUEw_z3W1GNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرزیدنت ترامپ : یا توافقات من با رژیم ایران بزرگ و بسیار مهم خواهد بود و یا اصلا این توافقات انجام نخواهد شد و به جنگ باز خواهیم گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132179" target="_blank">📅 14:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awp18ng6t_CncfjmdoiBCnVONg_AobMJ4kTCDsPfeh2tRLXKm1tuF3hbnXt-tg_3Sz5m_KwR-cZvKwGtA2yj51FxMaQQGOoRWLJZ2XZu27UAaLJOSuGJwS_j3vHEnLjsgKSC6BtPNOiscnHNpzssMZfW7GGbM4jKlUbnOf7CkAe7KujdfDKnpDjWueKb1O9tUHdjQDB95c_12R6dfq3ABW4TJZSwQDkIKNJXzG8gAAnL3yvHDAAiCX_t-TGg9xHcQSJ6kl2yScvxXtCMD0HX5YT0kIK33lOd31hm3CfOlb6V-4f3zUU87a9CSfnyeQpQdHJ2li-9MgEz7Gb11uMyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی هاشم نژاد یکی از بهترین بازیکنان چندفصل اخیر فوتبال ایران که توسط قلعه نویی خط زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132178" target="_blank">📅 14:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpnBVDkfR34pQOiW6kUpdch1o7i7aIfIz455TmJcUNehTiAwjUvsnwi9VaUEQdMI9NMOW97-aPKm8K8dkOdxNY83oRDuyjmQMbx470AghOOn3p-gdHZO_2olP1itipPPiUKDqksXIH2CARwa1HfuwUn98HBYBGoi5n58jGof4J6CIS9IKSOt07A8wuonnX1-R_xK3X41xx9vJ_hDUaHYT-JMk9xaNjWGiz0m3i7oJybFdHYuwuyJAPImsaihxPpKROMnFTPjbea12cZhgPKoQXx9VzGYp-FI5XkgEEQYjUDAQ0sPg2ov5XAXdo-72DuXr2WZIm64RVUyFOKEWV7u3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/132177" target="_blank">📅 14:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
یک منبع به فارس: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132176" target="_blank">📅 14:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
فوری؛ علی علیپور قبل از اینکه بره همراه تیم ملی ترکیه با مدیران تراکتور جلسه ای برگزار کرده و به توافقاتی رسید اما امیدواره بره جام جهانی و با قیمت بالاتر لژیونر بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132175" target="_blank">📅 13:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
یک منبع به فارس: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف
تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132174" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد
🔹
سیتنا خبر داد: ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد.
🔹
این مصوبه برای رییس جمهور ارسال شد و در صورت تایید رئیس جمهور جهت اجرا برای وزارت ارتباطات ارسال خواهدشد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/132172" target="_blank">📅 12:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
اینترنت بین‌المللی تا یک هفته آینده در دسترس قرار می‌گیرد
🔴
مشاور وزیر و رئیس پارک فناوری اطلاعات و ارتباطات کشور از احتمال دسترسی و اتصال به اینترنت بین‌المللی در هفته آینده خبر داد و گفت شرکت‌های فناور با دریافت IP ویژه، اکنون از اینترنت بین‌المللی بهره‌مند…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132170" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esHMTq9lrRjmZuBojxBRCHWeVmFoP8YGL1guIXslzlmGFasTxwojrgjOdmA8OSOLbdx59RJHFnKztqcvmTojIw_4rzoY_2_Xdzel0Qskx2liVmOLeiPza7YCm5GoY5zhPuaOOpTesEZo0XF_DcgVckGNgpBDzx6OiSBIfpUlciOo0RkR4IjJW_nRQSALrQE_Lfyz921d1odqESScXciOw-YEyYioE9Y1HWOBKnpBO_Vc_ri6wpQSLqUM7CFCSvMR4N1WZni-N8gER0QzLDONhFkmaR4K-XmltCKKghpQS-kpx25DJi44GhwR9HDY6LBG2poa-I4vC5joc1NSgR1GKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فاکس‌ نیوز :
ترامپ برای رسیدن به توافق نهایی ۷ روز‌ دیگر به ایران زمان داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/132168" target="_blank">📅 11:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/132167" target="_blank">📅 11:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:   معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132166" target="_blank">📅 11:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132164">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
به نقل از منابع فوتبال 360 مدیران باشگاه پرسپولیس
از همین حالا تماس های خودشو با مهدی لیموچی و آریا یوسفی برای جذبشون در تابستان آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132164" target="_blank">📅 10:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132163">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGlHM0mMr01WQnwXoxO6li3ZnL-Nb4h_HJgzXAZwevRbCZirv0cYxszUSVUAuuOD7HfWM0npHyL7gUysJSjRVLQsOQbVRSIWmnV1s-pOAQMguuR4yhcSo2IR_5w9s-kexXUjeAmjPabOv_Bb46DF790fIIAU7yI40brEw9OTW9sLew29OvDyzmhvVZztuyFxHPDhSVu6iVJq80wg1sIO4EsrxTZFwKmeJZEbRpYt8T83MC9pYzYLIZ2k4tJrifC72g9uMujnuVe0p5WVk7SeHThFzQZVfVUSW7hXOgGi1gizGPQjnGeaihi48TGTA_cT1Dk_JjOSHVyDAufuGpucfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه‌ تراکتور تا‌به اکنون مجوز جدایی مهدی ترابی ستاره خود را صادر نکرده‌اند و بعید بنظر میرسد این بازیکن در پنجره نقل و انتقالاتی بازهم به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132163" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132162">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
فوووووری/ خبرنگار فارس حاضر در اردوی تیم ملی: امیرحسین محمودی در لیست نهایی تیم ملی برای جام جهانی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132162" target="_blank">📅 10:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132160">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=rzl3eXqLOHCpptiZlMXW9hYbUAxpMsgLV9xnD8NkCxCfYAB0hg_17DpwxULHqENKhG7leCFxiZRiNLknQQbZgqXJ0dqnlooCwlsT6sEXb_dWTQIFz-3F250SjH2jJH6kEbCuZqWDA9crZ7yysuOem2-g7ZR569q7pR1f4l_kOgj0Za2G6hvYLC2jhHCCy1dV8BGdf3Bd-LNzb3xQUXhYwl33pr2Qtzu2G3xFtRJXpH38RcM-nliJ4kd514qS7l0tVj7QUFKUUx7aufo-9AEUp2YdA3roJuTJWoaonJwFER3VnWSImfJF89DpejeeuHxF8l1StpNY1_sdnbSJifFqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=rzl3eXqLOHCpptiZlMXW9hYbUAxpMsgLV9xnD8NkCxCfYAB0hg_17DpwxULHqENKhG7leCFxiZRiNLknQQbZgqXJ0dqnlooCwlsT6sEXb_dWTQIFz-3F250SjH2jJH6kEbCuZqWDA9crZ7yysuOem2-g7ZR569q7pR1f4l_kOgj0Za2G6hvYLC2jhHCCy1dV8BGdf3Bd-LNzb3xQUXhYwl33pr2Qtzu2G3xFtRJXpH38RcM-nliJ4kd514qS7l0tVj7QUFKUUx7aufo-9AEUp2YdA3roJuTJWoaonJwFER3VnWSImfJF89DpejeeuHxF8l1StpNY1_sdnbSJifFqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132160" target="_blank">📅 01:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5lmHnM7mQFUHLkmj5A3OUNtF8ix42SLTI6JetOyfdsCxky6VxzjlAaj45fNXmiWq67FBozHYdJDoMHkFY8jxelClwO9jMJHO6lLdpgbwsIUDAaZtoJrfkGOYmtijINwIggCeDgrGTCq9LSiIJlHnSGcAA-0XthBr1iGTilOexdqOknYhSkfq22UDx7jdWrmyoVUsRYZRJ-jAk8mtUzytBoWK8wqPjcQwTNEN5JDYyspMrjfEYROJxxnF9wN34p_Fmb-vHQ76HM_Qek-PaS5Ximg2i549hTidy3q14EqJXlmAWegdze60Hv4MwZkF65lDfOHsFf_RLp45OZs25JNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇺🇸
کانال 12 عبری: نتانیاهو در تلاشه تا توافق رو بهم بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132158" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132157">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو کلی توافق وجود داره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/132157" target="_blank">📅 00:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132156" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132155" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132154" target="_blank">📅 23:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RM4t_iMM6kquN33-Dfy_U-BfRWOO6Vxegp53QSS0LAvagyPuRzuR7DZAOpArPYgsrwcnu6HNsHRxSEqfAZMaG4OZwoSQYxAab97F-fe_SHqVQGfDS9m5IZGQnDoWrecYYRRPIdIiA2FP620iXMoetgJsJhywGU68PIlo8DmXzhgbAQ-6o8_AQbQ2BrTlT6wOregepnspYOlu8F-LzQ7VNYjuIIbi2Hk-xFRPFY_vGc_snqX6WKRLOreFe-KasrmzLrrpM1SaD5pRjO04UAdAowukGFysRHdlDUDdye6zkLxZr7hLPTtBdSyHJks639GDl3g2hhw6-mfupS57CcEr7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس قصد دارند درصورت افزایش بودجه؛ قرارداد ابرقویی نژاد را از لحاظ مالی افزایش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/132153" target="_blank">📅 23:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/132151" target="_blank">📅 22:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VburWRH_-1Ldphct9b-rAdtAuYpRGKrgyB1HMVl47mzfBD8vGZ4NP169ePzKyfC4oqO2dneZuX-n8zyt3X1jP3Mqxe9vCY_uKTcXv29EhLhwBF3vbvm1XnNbHu1kngtNjOMVyA37CGXZmDmnfK1wBM1eL_kjZh8Z8jmNtzhMzoL2nihoKiDULm4Xf1IRuCOQdvuaWhayKF70oaCoUojMqjELzxKYd6juZKMpz9fzQk9jkzQFcMnG_1gk4WMXEvOuych9HGB422_SR0VV7ZnD62w23fNRkA5MQE71cTkl-J0Q3InMMx-NYS1ZaHOGdmv8XecMD9pwTuzRQCOGq33N2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132150" target="_blank">📅 22:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um6ThO5EBBDFUSm9kBF1Fc_Nxbg4EJwqriz8pphImM5f0UwjEoVOwAGklgY6prjpH2uSBz8evWwKTyETOWBQhCbanrytVGH41PiKSlKzrZLY_l2DhhwxicFue6DvZ2dOfIUSDRTyHeHFCAjK993XmbV_K86qxQ-Ik0nPF8_V7pxzDhMrXgCdNbGBwXA6JER_2kYttYPH4YIkupmhw2u2NFQu87X7PvSVUSXf38lBstEsUgUP_wv4LkBRn5pEehh4jv-Tfe1OOK-6YfOqCqm7n29QlanU2foFbQi_TReENNxaWoFdbMQTQGMqF37gvet0uUFImZgZiQnzeicfvFBqfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132149" target="_blank">📅 22:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132148">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
فووووووووووووری
🚨
علی علیپور در آستانه عقد قرارداد با باشگاه تراکتور سازی تبریز قرار دارد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132148" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132147">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132147" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hINo8uYsGaFDNMKSrzXkVyjsE-Bnz5wzYnkt_nOIs83w6TjdPU9BzIhw-s5gxUt11RhY3INsKyX2xTxNpBYhhlgVL6_ZkS5dJhpCXJlnvm11kieDCQ8ROMwBGzjKqXWcMXgMAn5h9tydDmUWf6KzTBW8-UYVAQI59kJ-5pHlrNo61qmqkLK3dfQCkFcmlqXVhEY7SiX2qNkhJacDEhFj-cB1pKEppHpE9-SNHEsLfMbujMM5TluCCRbFs3AqQuigLzYm527VOf3F4wNQSZ9wadP3GzE93KRB92WKKntHw5CyzllLTLFNEcttz2ZXr9da_5wOzkf2DDhKmXw-r5SLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
سایت فوتی رنکینگ ، چادرملو رو به عنوان نماینده ایران در لیگ دو آسیا معرفی کرد
😐
😟
😟
😟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132145" target="_blank">📅 21:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=TwxhhqNqJn4qmpxmIa-BITtrXo1dPiUUfSbEqB9KFkWUa-fU5-ONawu5VH0UV5oMY3FgTIkHttNJxQyKqfoHGx11qxkefSsRcCVCsukDch8hUt6sJWa4kLkeSWZ4PFaoUumeXCsENNAek8J3Q54TvAeKTKcpks6T3CxUZQtMp6HFXCKveV_fnsdM7Gj3EBGOG_L5mpznsUSbau3XsXRwnUGd4THVUPfenspzlPbhlcYGyiX3GwM1p1AjcANk6dOebt-1mgoIMyQq1nlxUWy0UGX-QvbHdHx4Dw1-Yy4byG-kNsR03QedcjLnod8uezMoR2AUqFymwHqQ8cbb2OVpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=TwxhhqNqJn4qmpxmIa-BITtrXo1dPiUUfSbEqB9KFkWUa-fU5-ONawu5VH0UV5oMY3FgTIkHttNJxQyKqfoHGx11qxkefSsRcCVCsukDch8hUt6sJWa4kLkeSWZ4PFaoUumeXCsENNAek8J3Q54TvAeKTKcpks6T3CxUZQtMp6HFXCKveV_fnsdM7Gj3EBGOG_L5mpznsUSbau3XsXRwnUGd4THVUPfenspzlPbhlcYGyiX3GwM1p1AjcANk6dOebt-1mgoIMyQq1nlxUWy0UGX-QvbHdHx4Dw1-Yy4byG-kNsR03QedcjLnod8uezMoR2AUqFymwHqQ8cbb2OVpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی علیپور امروز تو بازی دوستانه درون تیم ملی به این شکل پنالتی خراب کرد تا شایعه خط خوردنش از لیست تیم ملی تقویت بشه!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132144" target="_blank">📅 21:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
فارس: باشگاه پرسپولیس قصد تمدید قرارداد میلاد محمدی را ندارد و به احتمال زیاد از جمع سرخپوشان جدا شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132143" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132142">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=O8onBgsWhSIWU8ZuzM3ZjyrFbHPFkSr_YG58Dh1vjRMGRb1bzBI9z8oTgvLIk1FGmP_i1SlApyfzrHpZaY05eiWVWYSpuhECKFrknEANu6fjlpEYxyh3cjoCKKd7w97VX7h1ua-8PlZ8dXZQu1xSdKR9vaKx6p1vdvvdzKqO78CtwZdOaW-c2QHX5-upJ4pRihdyut7i31bs5MgTu5GFlcVY_Ns2Wmwzk70okhtGqCkn_e6LO5cjtSTEHBoC5AyxThdJS4ncljHG0-d2PUpTo-CV_NGBsu63xZ5pmpQFGiUKw4cGJ8ZUz09DyUQSr-U-wK-RKPbPGbCWKfD71dKcig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=O8onBgsWhSIWU8ZuzM3ZjyrFbHPFkSr_YG58Dh1vjRMGRb1bzBI9z8oTgvLIk1FGmP_i1SlApyfzrHpZaY05eiWVWYSpuhECKFrknEANu6fjlpEYxyh3cjoCKKd7w97VX7h1ua-8PlZ8dXZQu1xSdKR9vaKx6p1vdvvdzKqO78CtwZdOaW-c2QHX5-upJ4pRihdyut7i31bs5MgTu5GFlcVY_Ns2Wmwzk70okhtGqCkn_e6LO5cjtSTEHBoC5AyxThdJS4ncljHG0-d2PUpTo-CV_NGBsu63xZ5pmpQFGiUKw4cGJ8ZUz09DyUQSr-U-wK-RKPbPGbCWKfD71dKcig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاس گل امیرحسین محمودی تو بازی دوستانه درون تیمی امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132142" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132141">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omr92HlQwx75IyomKI0N7euyJHJZD0HefcsfRoyrjeUltY4AXlL6hK1Oa_lPmj573MfWCG0kawq5D9wqXCtPJwBv1TC_Zsg46PNa7RM7UOZHgwJULRnPVRjcCvmerHCiS3Ql8N4TBEMmmD-dLpBL0hW2Fa39vLWXgRjHP2HPGY_tImEASMnjJZuSrlVVYqZrIgWdpu6Dg7VxBCxil1C85ztd-u46UJSvMUTIaFPr4gXrEzKpubLX_NiVYuflK_zdOidLX1rKk257U9PMbLXoNVFhLarIhyte7vPSr4jFTbLICj80apUAIGYXNxC3FM8TvRIS4y7Dmr1wr4Q005v97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132141" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132140">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚫
افکت اتفاقی :
❌
توافق ایران و آمریکا میگن ۶۰ روزه است، بازی‌های جام جهانی ۵۶ روز دیگه تمام می‌شوند
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/132140" target="_blank">📅 20:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132139">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEvo9KAGv-64utDHjgffuS0XhwH6Sacz1N8l2_OisecWKjO8WVsO5uacIxQBQtTGa4eexW1araxDPcxI3y_yWwgsSJMNYXcJk-QVJq1g1dEaMsCKWj5z3CPLOJRrW4dkROcw-6kEYd1Jz26_koQHSfqKOT16u-RlCc9LP5Hox6Q9yPq480yrZFq_2p4uc0CCLohwstuDAFokSWypwILiASlZNqmHdrE-JbOxv6jU_6tEY0KrJQhKWN73k2uVVv1eXV3BC8EJWOkwPzY-WUe5ajAUODmbXcYzy_VZ5uha6SNeBeTuMCL-_WfYDI67mlEcOJ3vIgSvm91q-uhnhXnwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ‌ حرف های امروز‌ پزشکیان که گفته بود آماده ایم‌ به جهان اطمینان بدیم که به دنبال سلاح هسته ای نیستیم رو ریپوست کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132139" target="_blank">📅 20:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132138">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">😏
😏
😏
بابایی مدیرعامل چادرملو: اگه سپاهان مجوز حرفه‌ای نگیره ما از پرسپولیس جلوتریم و ارجحیت داریم و باید آسیایی بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132138" target="_blank">📅 19:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132137">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚫
افکت اتفاقی :
❌
توافق ایران و آمریکا میگن ۶۰ روزه است، بازی‌های جام جهانی ۵۶ روز دیگه تمام می‌شوند
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132137" target="_blank">📅 19:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
تمام اعضای هیات رییسه فدراسیون فوتبال درخواست ویزای امریکا کردند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132134" target="_blank">📅 18:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
شبکه ۱۲ عبری به نقل از منابع:
🔻
اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132132" target="_blank">📅 17:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
شبکه ۱۲ عبری به نقل از منابع:
🔻
اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132131" target="_blank">📅 17:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
پاکستان تفاهم ایران و آمریکا را بدون نیاز به حضور طرفین اعلام رسمی می‌کند
🔴
به گفته این منابع، توافق اولیه و احتمالی میان واشینگتن و تهران تحت عنوان رسمی «اعلامیه اسلام‌آباد» نام‌گذاری خواهد شد.
🔴
این منابع تصریح کردند که توافق اولیه در واقع یک «یادداشت…</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132130" target="_blank">📅 17:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
جنگ هم رسما تمام شد ..امیدوارم دیگه بهونه ای نباشه و نداشته باشن که نخوان اینترنت بین الملل وصل کنن ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132129" target="_blank">📅 16:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132128">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حمید رسایی: به هیچ عنوان اجازه نمیدیم اینترنت بین الملل وصل بشه
😐
😐
😐
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132128" target="_blank">📅 16:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:   معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/132126" target="_blank">📅 16:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132125">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:
معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132125" target="_blank">📅 15:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132124">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
فوری از سیتنا، پایگاه اخبار اینترنت:
احتمالا تا هفته آینده
اینترنت بین الملل
متصل میشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132124" target="_blank">📅 15:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/132122" target="_blank">📅 14:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132121" target="_blank">📅 14:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt8GciGTr7CiCo0d23NN_vwT5IEI9fFEhLX6kACpNsuWwkhfguhdNwDNmchcGw0UayteLECx0gtjd9zAPNEG0tGt3FWLOq8pKIDBgsyhhc9FyOkX3P9KPVTb2Mc_5USSyG0Oo7s08zUsW5Omp_05GaZKQn51Abt_MilCUU_Fzm2EJJry6QgA-Y8Wc7ajIJEbI6lV6kzDR1dWjA6KjeA-XR-9jq36N_peAP9s0WS5PcdiGa_VmYONtFAQw5kWfo66Y9r-LZ8MUEezKJ9FKW06gVTM2h4XYQ5FlPTYkH54ja5AxPsJZRfesZPtCBgfS1sUKqIAwAQGdFJRNXI_v_M2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132120" target="_blank">📅 14:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132119">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=otcn1uxHkGv3LEyNh3cbNdWuP4HZYXSVxnKMU3j0nLwgQvHATJl1QvAOJU4Ivl2n_-5yo00V-mp0yuxeWS-ASwER7Ev8QzRP3-IIqr7Z7lhGZxR2zIiPsRGs2VDkvoN3pSWM_BTzgsltYc7imMIETvNyeIDcHg6daeAHuRwIk-Lgz23uoPGP7IASJuqxPpWqpS7Hw3TEr_Ttzlm2KoFunaKmDx8_mc6LWS7tsYi4NBg-s04_mX-IqlWY5QhfFbnDAPSklf5OIGZ7b-wZvuWdSthVuIzM22ePI7UfCUnzkOA_jiR5ErAZlxGFc1JjX7mWuGO7OgmTyPLOvvuzp4HwfxsG5_KYhGxBzTBb1LMIDVu6Id821T5z30RfgpvWEBR9PzljacHBwwy07Zwtgrt47Dwgvs_EvoWr4icI23TmF9OBiXOI_ehlC39wq03SgjyZH6OFB-fIx_27vvnPVErB5_gUinhPbLjOb41n4P6YfgM0dKAmfQJaZ3liVTi3OiXnxbr2yQPgA2aJcUHLBLwCZMS6Xop3_uhalfop8lMZMdzyFBX7bjqfWZBOSKpdIkrBMERx83baesdRuVubTq8ohqkNeOm-G5dXjHXCakJqQddh7zUaoN4MgNqiaxv98R0bKisRgw4cmWjmNVbxxm-cUKAhXULDeOTtY3ikxwVVdJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=otcn1uxHkGv3LEyNh3cbNdWuP4HZYXSVxnKMU3j0nLwgQvHATJl1QvAOJU4Ivl2n_-5yo00V-mp0yuxeWS-ASwER7Ev8QzRP3-IIqr7Z7lhGZxR2zIiPsRGs2VDkvoN3pSWM_BTzgsltYc7imMIETvNyeIDcHg6daeAHuRwIk-Lgz23uoPGP7IASJuqxPpWqpS7Hw3TEr_Ttzlm2KoFunaKmDx8_mc6LWS7tsYi4NBg-s04_mX-IqlWY5QhfFbnDAPSklf5OIGZ7b-wZvuWdSthVuIzM22ePI7UfCUnzkOA_jiR5ErAZlxGFc1JjX7mWuGO7OgmTyPLOvvuzp4HwfxsG5_KYhGxBzTBb1LMIDVu6Id821T5z30RfgpvWEBR9PzljacHBwwy07Zwtgrt47Dwgvs_EvoWr4icI23TmF9OBiXOI_ehlC39wq03SgjyZH6OFB-fIx_27vvnPVErB5_gUinhPbLjOb41n4P6YfgM0dKAmfQJaZ3liVTi3OiXnxbr2yQPgA2aJcUHLBLwCZMS6Xop3_uhalfop8lMZMdzyFBX7bjqfWZBOSKpdIkrBMERx83baesdRuVubTq8ohqkNeOm-G5dXjHXCakJqQddh7zUaoN4MgNqiaxv98R0bKisRgw4cmWjmNVbxxm-cUKAhXULDeOTtY3ikxwVVdJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132119" target="_blank">📅 14:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132117">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فرهیختگان: مشکل اورونوف همون همیشگیه و چاره ای جز مراعات کردن نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132117" target="_blank">📅 14:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132116">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
خرید اروپایی پرسپولیس خبرساز شد
⏺
شبکه ورزشی «M4 Sport» که مهم‌ترین رسانه ورزشی مجارستان محسوب می‌شود، در گفت‌وگویی با گرا اعلام کرد این بازیکن تصمیم حضور در پرسپولیس را بر اساس «حس درونی» خود گرفته و معتقد است حضور در فوتبال ایران می‌تواند چالش مهمی در دوران حرفه‌ای‌اش باشد.
⏺
گرا در بخشی از مصاحبه خود گفته دوست دارد هرچه زودتر در ورزشگاه آزادی و مقابل هواداران پرسپولیس به میدان برود و این موضوع را یکی از جذاب‌ترین تجربه‌های فوتبالی خود می‌داند.
⏺
در گزارش‌های منتشرشده همچنین آمده که این مدافع مجارستانی امیدوار است با درخشش در پرسپولیس دوباره جایگاهش را در تیم ملی کشورش تثبیت کند.
⏺
رسانه‌های مجارستانی از گرا به عنوان بازیکنی یاد کرده‌اند که حضور در فوتبال ایران را سکوی جدیدی برای ادامه مسیر حرفه‌ای خود می‌بیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132116" target="_blank">📅 14:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTFE2pyyFv0o_hIyPG5JkikTTYdk0y5ih9OM276DSwsjZE8G04IeU4qArLy7rw_DxAAHtYfC_RG1A7DPzsXHQpUsOR4g8IVGR3fIIDL4XTFNw76I6ObRUKYzhzrW9uuPVwShnr60u2IHWzFj8gKGV__MhLNQUFpzunepDD3vKb1o2FcwdPDFxXsqBpceZeKqoFUKIrVcBgqB0Yx3-Kr6je1diuGDiYlLn2txyU-1_DUfNtuygUN_LMlGkXJY9hQRkoFkFYMNMvIB28W4Iz6HbU_M1QBJ5ikTHyzqLtdpS_H3rV7-BMT9eHQ1k4q38ToAopfXrbijRm3fDSlZMyLgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
بزرگترین ریسک حقوقی باشگاه پرسپولیس ختم به خیر شد
🔺
شرکت سیما کیش حدود ۱۲۰۰ میلیارد‌ ادعا علیه باشگاه داشت که رفع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132114" target="_blank">📅 13:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
ورزش‌سه: محمودی بشدت آمادست و احتمالا راهی جام جهانی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132112" target="_blank">📅 11:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
تا قبل 21 خرداد حکم علی بیرو بیاد از جام جهانی محروم میشه / خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132111" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
⛔️
احتمال محرومیت بیرانوند از حضور در جام‌جهانی؛
💯
حضور روی سکوها به‌جای زمین چمن!
⚠️
با شکایت باشگاه پرسپولیس درخصوص پرونده علیرضا بیرانوند به CAS و پیگیری شدید سرخپوشان تهرانی، درصورت صدور رای محرومیت بیرانوند طی روزهای آینده، دروازه‌بان تراکتور جام‌جهانی…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132110" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3azlEqaRbD7pMkEVxrve3neS3ykZqnAncw45VKenKIzlzYDnljHvs-XGUcUtRqbHIXQaXj9OhvADks2Y2udI0hx3T_UqkenqtEV0KBSgHILRgvZ_1ZUHJj6V-KdR63rkfLjSpYh8Ris0h4Q9H1ARRyoYqE6f5rbBsWo4QdAYyMbJdhy3qNOsdcrwmklBuq_bfAiDx7MHAyNfa8edi7Scm1Vu-Vw4FHnqWlYND0Dyngw9TeIhh7zt-N8l7MGuqi97cDiZBfiFlvzJ-HAGWTlWgGEqnB51dnEgwP1cRbQQ_vqbapVlhcbjwngmKefwesr13J3VLs-YD4OEPdIwFz0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132108" target="_blank">📅 10:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132107" target="_blank">📅 10:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132106" target="_blank">📅 10:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/132105" target="_blank">📅 10:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132104" target="_blank">📅 10:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SorkhTimes/132103" target="_blank">📅 01:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/132102" target="_blank">📅 01:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
آکسیوس:
🔽
توافق‌نامه همین الان توسط دو طرف امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/132101" target="_blank">📅 01:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
علی هاشم خبرنگار الجزیره: طبق گفته منابع من، پیش‌نویس پیشنهادی که قرار است نهایی شود شامل موارد زیر است:
❌
پایان جنگ در همه جبهه‌ها از جمله لبنان
❗️
آزاد شدن میلیاردها دلار از دارایی‌های مسدود شده ایران
❌
لغو محاصره دریایی آمریکا و گشایش تنگه هرمز
🔽
خروج…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132100" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132098" target="_blank">📅 01:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132096">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132096" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132095">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
فرهیختگان: پرسپولیس بجای سپاهان به عنوان نماینده سوم اسیایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132095" target="_blank">📅 00:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132093" target="_blank">📅 00:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfOkyeKFCBIvflFyDp1N0F18lstbv6xqkA5n9cOev_nxHRACeEyUbuolEFQsUviY4m4uhHvwzxbGQZUXQ1vYFJWK0KGfj5C2T_t1hWQY65SPjQYzHPy3PMpg7YavWOeui3EPmUYTqfDZQahNKAPRRLv3EMjPMg6LRcmxSKPdhkW1oQrWRj-PvVJFFjDRuYJLfrcJCmkNN94QdOjEaQC-B5IoqHQBEzXiVycnx0Uqyez33OoZD_1eBOJZnm-NIJKJM4iuQvQWg48bgULyJcv1o1ieTEqEg0FlkkuMPw7d9-TRt_3zjlZ9EMXK3gNIEKRQEAEvrvSbqe5Q_TU4r9XoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ :
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین داشتیم، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان صورت بسیار خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132092" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
#فوری | الحدث:
🔻
پیش‌بینی‌هایی مبنی بر اعلام نهایی شدن توافق صلح بین واشنگتن و تهران ظرف ۲۴ ساعت آتی، وجود دارد.
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132091" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132089" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
