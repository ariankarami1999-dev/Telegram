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
<img src="https://cdn4.telesco.pe/file/icpwRYFWaXC4vQd5R6FHt5-fbMS2NKbv0bj-Bg29iMuKzS9rPp8ACs1q3WRUKQrRU6n3nqjOeAcdOQbOWXtG245dEeR_Yngmtw6MneHNaM2Z5TRIbSw-8oFft2iQHYDlosaFtbJb5TSiR9DPOwEoisrltC9Qald5F9OmNST_q731zFl2G7W1Ta7j66JIT8wbaM-HCs4obPtjx23Kev-XBFwOqBI3c4U74-ieKCtQn4M_wmaNQVVF4tZGbe41Ytl7dipm3EQJnE_Wn11xbUU_7mFnM2mYrR85e-ZfUqCo4eCNEKnNku_142JJXyumzLsPreolffe_V-HMO3tY-Yviug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
بغداد بونجاح و ریاض محرز، دو ستاره الشمال در بازی امشب که شروع شده مقابل تراکتور غایب هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/141353" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjpbeYpgJNR7I_jpHEajR1inRdTJm9oVGz9VuIkR1XhLRrmP3rGYmCBGlNW__8Jq4fuXblmD0Iuii83TWXw5_9czxM-Vu0L8L-v9dSIIhWCVxUM2m8ESh5vixs8-AhSGS0HmsaadX_fs8eSRNpEtHE-l-sLjOYzRjfyEvI6GJnvjuyWUwUn6_Th_PYn-PziOzAvM3L3a3LrhY29SzXnMxfWqshC4VGLN6pPz2oBCHGR1FkPqbKw1aoCo8JqvzlXgnDN7m0SqArOOEqFhmOISgEyy2alMlUMKzztYM6FW74jjNRyCg2pkk978bpSwCK-tLfuLM7dCWnNMIa3Blz33tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Gharafa
🆚
🔵
Esteghlal
⏰
Tonight 21:45
🏟
Thani Bin Jassim
🟣
الغرافه در ۸ بازی این فصل ۱۷ گل دریافت کرده؛ نقطه‌ضعفی که استقلال می‌تواند با حملات سریع از آن استفاده کند. استقلال با روند بدون شکست در ۹ بازی اخیر و برد ۳–۰ مقابل السد، از ثبات دفاعی و اعتمادبه‌نفس خوبی برخوردار است. با توجه به ضعف دفاعی الغرافه، گل‌زنی استقلال دور از انتظار نیست.
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
<div class="tg-footer">👁️ 966 · <a href="https://t.me/SorkhTimes/141352" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/141351" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
| ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/141350" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✖️
✖️
✖️
✖️
با توجه به درخشش مهدی تیکدری در پست دفاع چپ، پرسپولیس احتمالا بازیکنی در این پست جذب نمیکنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/141349" target="_blank">📅 19:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[ تراکتور
🔴
🆚
🔴
الشمال ]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/141348" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/141347" target="_blank">📅 19:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVpswjkvlO7IUdLbDQjLMJYdsXCs265wHKhMJpXpZO8qyoqfNs0YR3zBwGzI-YXbSvZpGKNEKMfcZRk93eib-G_KG-8evon5hThUh5t8ceeVtxWICVdLAgIJBqQGb1glx_tNlnonl8ifTuG1wRH-PK-0O8SO3zDcb-V7G8ezbcsbkyNrhoyZ8WOfdNYzoBj-PJMsSrVmmSwOTYTCE1YxGPc7XpAHKaI9c72Nr9Ejen7ppTBut3wTGecNIq3nzmDFtG555cX0FW901RnXZCzu1XK8-XJW2d6NgxTdCCnjdlnwP1nrsBdFRgGdHd7K5idOak87AZyws20AtoJuw7eQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/141346" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfKbdqhwqqm6PIk68QFTwvyfWWYwfDjpzySJo1PgA-WEo-395X1uMx4jDmYLRlrwbDjLYqzsB-cgRriD_cKMLPBuh8JBsiixsmF1rVTmijNjhP3oDSkkByw3_krAsvzrpPTEZ6QQpMnhAiZRI-IFoQkkDodGF-a0pNQA94H272K0JKXKwUCdpnBLjqOHLjneTIkrbHnL8JnKRU-rUx2FYviH1kUpKQNFIjZbQ2ah6fuVqB9GCr1iR9w3W7r1tKVUCHS19NdQf4VJlYRt51u_UJD9YdF3qLbcqvCU9OWR4rktoI-RdeuzL7Yw1Xn3JurnGeev4euXLaJyUAMq5-e5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
مهدی‌تارتار به مدیران پرسپولیس اعلام کرده که اورونوف غیرقابل فروش است و این بازیکن باید در تیم بماند. تارتار معتقد است که با وجود سن و سال بیفوما، حضور اورونوف جوان در ترکیب تیم ضروری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/141345" target="_blank">📅 19:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGelBa_HnPTKaQnywMxmA1EqA7GJjH7sBhgOHGud4NI9On7VjmKOYe_y24YO5ixk11RASDhrK5Hhx4N6Ee-YRsaMHQBIgJQd2-cfruuMzVvEtDnScjtDM9i-nDBK8TDX2h-jxiZQGFH4_NKEvALW1_pBpwN6FqYrguBrMFusYKaLDOZ6u_SpRJHjd_nNFuyjcoIDZ5IHCEtt03OZUoy_DXxEBZYmc2ha4YIu3fhEnY2gykFMK0o8YTQDSCwdb1IXjpNI-Zq-0MT3AYu3NKQYabEmC1BB7tgmmZpfPIGrqOIRTsMxB90BkLpdvvfn27Otj9VEjAMP1amg8KTcQG5SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
|
ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/141344" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/141343" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
رد درخواست پزشکی بیرانوند  اول آبان؛ اعزام به خدمت سربازی
🚨
🚨
ماجرای سربازی علیرضا بیرانوند سرانجام به پایان خود رسید و این دروازه‌بان باید چند روز دیگر عازم خدمت شود. دو درخواست پزشکی بیرانوند در این زمینه مورد بررسی قرار گرفت و‌ هر دو رد شد.
🚨
🚨
آسیب…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/141342" target="_blank">📅 15:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/141341" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
قضیه پرونده آسیب کتف، پرونده اعصاب و روان و خالکوبی بیرانوند در کمیسیون پزشکی پذیرفته نشد و به صورت قطعی از اول آبان سرباز محسوب میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/141340" target="_blank">📅 14:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/141339" target="_blank">📅 14:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141338">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
اول آبان؛ زمان برگزاری دادگاه پرسپولیس و بیرانوند در CAS
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/141338" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucfrIfVsF0f-m5sS8NOwbafHL04yJt2TF42dtbEAT1ykpRJCC0HRYnqZzil_vuB1-kdX7_iUR2r0bbYMCOtq1FWh06cti53ih_GZzf6Gxlw7gfqkpkwMpSk4T7FKmN96-uZnN--1IT0LCdnRHL2QChVwRal5QW7dRy5rHumfWqiNTKVJo6rkNwNRHs9GuHGpOd52IdH71YoZLeTxelUqqjlfB-Ciw3XQ1A6FS-gchY01Cx-uLut1aML_0LvCYLBfTLFRVgQOHDGoFGD3siRfhzI_rlT-1QvNyIECK5F8erJNpV2hd7rhx1XN0EKOYdhFWcR4AywZBDqP3ti9FN8KLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
استقلال در دوحه؛ جدال آبی‌ها با الغرافه برای یک شب سرنوشت‌ساز!
🔥
⚡️
[
الغرافه
🟡
🆚
🔵
استقلال
]
⚽️
الغرافه در ۵ بازی اخیر ۸ گل زده اما ۱۲ گل دریافت کرده؛ استقلال با ثبت ۶ گل زده و فقط ۲ گل خورده، آمار دفاعی بهتری دارد. استقلال در ۴ بازی خارج از خانه فصل، هنوز شکست نخورده و فقط یک گل دریافت کرده؛ نکته‌ای مهم مقابل خط حمله الغرافه.
سناریوی محتمل: بازی نزدیک و کم‌گل با برتری نسبی استقلال در فاز دفاعی؛ الغرافه با استفاده از میزبانی فشار می‌آورد، اما استقلال روی ضدحملات شانس گل‌زنی دارد.
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/141337" target="_blank">📅 14:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141336">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/141336" target="_blank">📅 12:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141335">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
باشگاه تراکتور به صورت رسمی به علیرضا بیرانوند اعلام کرده حق حضور در تمرینات بزرگسالان را هم ندارد و باید به تمرینات تیم امید برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141335" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr2FFXv7g1yBbg3SmtEnkMi6lkYj3vAgUEsjJo_TmlLbCEJMsIWs3dzsvBbroh0R3Y0MtCjb5Eig0N-Y5SrShi8gfFcbj1OAuHjYKqjrFHZ6gLk0RbyrEX3AQMRH2TyOOwKzPZZJU2Bg6CNGw_sMixGvQI1zhg3sMlrFYTj9jtCLtkeCKM8rWKejFbPGs-HhgHsEwM_xuuVueFZ2Arrho3r7oX3ZLBMxrxvKeiCZLjDqdSsl0B86SBIaStJGRF77aW9UNAXqdetFJhMQ14fqoinZIRvRPv70r-crsMUH95s7a6gMbjmaF-212Fjp5QsgWTAL0BibY0xDNj0GLYTbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی فر در بازی با نفت نتواست عملکرد خوبی داشته باشد و مقابل خیبر نیمکت نشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/141334" target="_blank">📅 11:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141333">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🆔
| ورزش‌سه:
🔴
❤️
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141333" target="_blank">📅 11:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141332">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiGBKAQlaQXpTCU4gxPcq7vHaWSLM9ryO3HMt6Pjt4wJZ0TPrqQVqtaAA4yxopQz8VXGBPdnzZQo_JRmScblcAbGiyVrRVPpnOfjFIzdrrCCuKLEBqYNvI27xu2spTmSScRj0wd8rfrKAk9lx_hMamCy-d2N_sok3STZkJ9ZD8luOlSVhlpjnL6ClucUMeI2-JqUmQiF3XzmKd-vUTf3M3qTzI7owWUZXDPzdp2zBAJKWoUel0YBeoDcOjH-LYqNgA91kk3ODP7BQ6otlRs-qjCUyGd0MzYkcyBc42EYJlJetp1FZ9qyiis8qCNN4LdYBWftPEZwy9bPuutCeYzElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اورونوف با به ثمر رسوندن 4 گل دیگه، تبدیل به برترین گلزن خارجی تاریخ باشگاه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/141332" target="_blank">📅 11:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141331">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
| فوتبالی:
❌
مدیران پرسپولیس در دوراهی تمدید یا فروش اورونوف قرار گرفته اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/141331" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141330">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🎙
تاج :
✔️
امیدوارم ورزشگاه آزادی بهمن یا اسفند امسال وارد چرخه مسابقات لیگ برتر شود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141330" target="_blank">📅 11:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141329">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141329" target="_blank">📅 10:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrPMmOBdai8ZQifOpfs5mQ1i7NmBt1DkCN5NDGhK_JzbTUU8lSukITxIPYQZnwH3Fnc9wCBbE-JyiRxTHYX_JtG9Z16WGyHc37zRi6tDK4EdKs4LLa60HHZirQDw8f6N1dT_yz0fuPA2FIKAL7TxoGmFJ79Ayf_twg_0n7Q56sDKfNTD4nRY8gLQRg7KBFQT-0pkoyhLuUMfGepqQsADZZA1WETtbbnSOpJnd4PmfPsiwEfy0ofKZRluAO7El6QRv5yAHWtGuE06TNlYqiLq0w8hR5QB-FRiXN33xZTY14cXMgnXPOS52K61nFFY4er132Mi6-v8njfvjSVqgSY5Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141328" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i04uX5Y_5rSQ6zbU42_H2Llfnf3WXNMTkIMbBYnMbqCPJMCDeE0Rhy9BCgWn6X4iPqJxmJWevVnwCjo8677BgShUpdmlankXg4KON_OP28VJgsvi4OdfM2qrVNuhuOrNQ77PvPkqT48GwBqzyPb6WSvaBMcXzWjWWOIMWkaVAIptTH0FaeWorMsx9Nk-xEe3DsnxxkN6Npd-4s1WJZe36-oyxRurxxj3OJQAOYZM4wgwlBUzVhvvnVEd-lnsPFT9ZPVwRfeZv1LWqN6S2sNrgBnsmTFJcaJV45qN76gTf72LLfOMn0UepVg9QYyIQa03yGqJDYjM8W7Okk1ozT-lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[
تراکتور
🔴
🆚
🔴
الشمال
]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط حمله خطرناکی دارد؛ اما میانگین ۱.۶۷ گل خورده نشان می‌دهد در فاز دفاعی آسیب‌پذیر است. تقابل قدرت هجومی الشمال با ساختار دفاعی تراکتور، کلید بازی خواهد بود؛ تراکتور شانس خوبی برای کسب امتیاز دارد، اما غافلگیری در ضدحملات دور از انتظار نیست.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141327" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141326" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAvERf5Ak9nfHWkJRfroxPAmPNfIDlh-kAd16JRD702EM_sdStY2GZG0NgCZyWHHEJr6IP1U1rrSOmDHKrjYns_HQH6sbmmGK6KhG32ai7gsiLcCXr-8oeAOeP5-Pkkixm7SfugFfI3JA3yGUvF7n6pVUETnYr88j-x28xk05mIGlLJdcE30Bl5ixs3SWbuVOV4RpmNpw2UtVKOdIaK3mMCq090ZNEkmRMg_L0A6uAHe6nc8flfy3Z0-_TWkCQQ9WwF52nozafwFyQtdiCftzZar58ENGUZ4oF9Rb_hfha2RI2H339un839wmWsuOAxHGAzYT_Ua2ghT8GESQ4EUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141325" target="_blank">📅 00:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=j2mFfFE54PzdTRUOtU5BZE9Yl5bNFRTDEg1kx5jaQzPjkcWsPwMHt4qfXhj3iYiUp7RLjoy3eZ37YJZ4KAM2zOCyDfyKb89wKz81CothOduxIRjccUrCQrS235E-Pgs6XSLGS412CApxyWVfeSDHOehfMobtsTzuhtjaL9AOPTnjZUkodQmGozj7dbKF_NPoOFwaGm1nGC0GXYpE_msAduPQYIb_q066xwA1Ydp2yTGDnbVaHA8oUx7f88mVPl8iGc0oA140KF39GPpOfGoOM31kZdKeYtN3jA7urajEQ6E3cw8fgZKvfH4FbBNHvTpWGtaY43-Q6DpG33CBUzTuKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=j2mFfFE54PzdTRUOtU5BZE9Yl5bNFRTDEg1kx5jaQzPjkcWsPwMHt4qfXhj3iYiUp7RLjoy3eZ37YJZ4KAM2zOCyDfyKb89wKz81CothOduxIRjccUrCQrS235E-Pgs6XSLGS412CApxyWVfeSDHOehfMobtsTzuhtjaL9AOPTnjZUkodQmGozj7dbKF_NPoOFwaGm1nGC0GXYpE_msAduPQYIb_q066xwA1Ydp2yTGDnbVaHA8oUx7f88mVPl8iGc0oA140KF39GPpOfGoOM31kZdKeYtN3jA7urajEQ6E3cw8fgZKvfH4FbBNHvTpWGtaY43-Q6DpG33CBUzTuKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/141324" target="_blank">📅 22:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
پشمااااااااااااااتون بریزه
‼️
🚨
🚨
🚨
با دستور مسعود پزشکیان رییس جمهور جمهوری اسلامی هواپیمایی مخصوص رییس جمهور برای سفر مستقیم استقلال به دوحه در اختیار تیم استقلال تهران قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141323" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=rA98G5ip5zO0MgfC89vlvXdkHPAF6zsUAOSiEPW8yCVUAad0atnqGNZzbp-ckd-SYE-5Mk9E7i9ayX2rkvLSLNHMxDunKnFHcKC6EAXYztJrHsXTfwE-z5tpAhRci4z1y2YzhZ5GxVkGLkdWqV3Zo_MhusrJL6-vkyTA4P16HryF-tFtD--wKyn6xvrBDbNuHxF_ZES-8ueyM49Em9pFIH7Ude0KW_5Z-YbXGJLJ39guFg2x2evC0oEzaeugk80mrxXW3Ic-eDof2E_Xc8YQoDrdZmmyXL1JDZpl2MpmJ2LJ50xV0oQxsmRunaylq_6n3CxYKQX7eVVkVIdbgVcyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=rA98G5ip5zO0MgfC89vlvXdkHPAF6zsUAOSiEPW8yCVUAad0atnqGNZzbp-ckd-SYE-5Mk9E7i9ayX2rkvLSLNHMxDunKnFHcKC6EAXYztJrHsXTfwE-z5tpAhRci4z1y2YzhZ5GxVkGLkdWqV3Zo_MhusrJL6-vkyTA4P16HryF-tFtD--wKyn6xvrBDbNuHxF_ZES-8ueyM49Em9pFIH7Ude0KW_5Z-YbXGJLJ39guFg2x2evC0oEzaeugk80mrxXW3Ic-eDof2E_Xc8YQoDrdZmmyXL1JDZpl2MpmJ2LJ50xV0oQxsmRunaylq_6n3CxYKQX7eVVkVIdbgVcyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141322" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbedlKgAOhR8krCoYm79m_KyzBdqqE06k5Z0Nps-IRJt340L39_CHzabLQ0W795VbMW5PgzWE5fEjchAdd-QzVme8boiVfSh05b1oVwg1W85k_BVuqjBglkpfYNbyzHTNJ1Nt3zizhtk20oA8tBAFZMvU1ZVEymBmTQ09WQT2thw_feByknBUUf_M0sdRmrSiEcsSJKmnJTr8b_q8VISSVHTvoc5Fa19fjksq3yvnrTklUyaMEX8GQ1Gn09n8ihmceM3OZYwlW_R2MiAi1Kkw415rRfr8F0HrZWDTIk-ii2EMU6ybMJPB5svGIb2_GtkGKNYkWLnr5ls50Jgr0BiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141321" target="_blank">📅 22:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpGumODFNCTugf8MDeE1XsgHz6r4XxesKt3TXAFaUdD6dzwEdaX_sD_gH1CqyZLX-AtnJc7la5wF8ZpGbhyJxjI4XFUhe_Hf4WSBN3ukY74G7nRGo59bbb8S-jHti3KRJ08ohajF9-FlTKEZQHLX4FwQVaJBg-u_utkpmqLXr4Tlw0AhnfMb7-BzikS-8zKmNYCFM8c-8m29NjdiTwbxMKetnQgsTpE-KH1z2GcCRujinGEyIle67LZDRyRc94X5-Xn7CTOHrCI79A_ZLfQ4x1Yw4hFpXLabLTFMPSAuNdFFX2PHh4yB03tWGFKtf7wHnLJPydVPX9eamIBEj4U3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141320" target="_blank">📅 22:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL1QAmmIKr17iQ9CNkwasgATDFRvvkDbrWtBhlzUIkTTSpYn2UxNu4LYKxkFVUl-pNJRq59SF4ot2zgZFV-kQdU4H-gBni5jwBHduWjg2x991axC9cJ8gSpawxa05I-PFIG3d-tRcuN1h5utj45Gf0AVStHDjwHI-SJoI2fLVEh1YTQ0RPYu8cP3huBGh74-PbFgOa0eMNUXdYlyv0b3DfwMQ83XmbIaqgl9SfUQ2xFCYorSOiTsE2ODa_98fW_0QkByUjj5D0OWrCbsTwdFeJWaLFxJj_PJL0ouJnL0rvGxQzS3f8YTWTRUanJwWdg1YK0oC-xJmXBs8CT94Q0bSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
فوتبالی: تارتار قصد دارد پست دنیل گرا را تغییر دهد و از او در پست هافبک تدافعی استفاده کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141319" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی تعطیل شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141318" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms03jlnJ5GsiOcjCgrrCPmzbZHf-KQfPZ0Vd0QJw9PBLB3J6r8c6A_hPLxtn7Z1jmtdFbPvTWTmFOAAR8Ay_-hN5LhoXQ-wejgQwCNmfaBAR4inWwhwosAUdtsPR836AqB6JPnI9Qk42ANWwGMxhyr4phUYZgUP6aixXG20irvkiWJEhkcF13P4wAmIOET_ISrQFo8vFogViTEtV_y6imUSmmOHRTHRuCXEhIEjJX84wHQJlxcWB3bsPThtWrPqdMoYWbMzvNSYgS5tWcBAC-3ObBSaUqYJ289BE8_MIlznJICW1ocwoGpZ91JNeTxj62LhQl79_WXdsk7pK3_9nWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیانکونری در کمین ۳ امتیاز؛ کالیاری سدِ راه بانوی پیر!
🔥
⚡️
[
کالیاری
🔴
🆚
⚫️
یوونتوس
]
⚽️
یوونتوس از نظر کیفیت فردی و تجربه، دست بالاتر را دارد؛ اما کالیاری در خانه می‌تواند با پرس و ضدحملات دردسرساز شود. کلید بازی برای یووه، شکستن دفاع فشرده حریف و استفاده از موقعیت‌های ابتدایی است؛ هرچه بازی طولانی‌تر بدون گل بماند، فشار بیشتر می‌شود.
سناریوی محتمل: برتری یوونتوس در مالکیت و موقعیت‌سازی، با احتمال بردی نزدیک و کم‌گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141317" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری
✨
میلاد محمدی در لیست مازاد تیم‌ بلاروسی قرار گرفته است و به زودی از این تیم جدا خواهد‌شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141316" target="_blank">📅 19:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYmVqAj0tPSxUnYWmfWpxatFxuVsM8oaXq-RFufz9LoNLKm0n0UhOLgo6wySONC6Y5qSRGW-Vg9Q6ObE2HfmCDh3jQHAmvU_5ER714nQLzyaE5GsmQqWmKeecyEhV51kXXkXIcmCL1B8MdnS6eFgKJM2TshxbEsLAhYARpaOpqHkhrnY3jBadJLG_78iH82x53W_2-rOzudO7DdhyYQBMPTWUf1Kj8CtRBxnXpvgz9Edn-uKGOjFY2lThfCh06yqdPQecSojryEvMcZJ-CLMtQQpyndFCWx0aP6jgP1sKNTVKzninFSUmSDOXrsMWcjF9ExN9_08xXxzSC1ujDRSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر فاصله دارن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/141315" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
پرسپولیس بزودی اقدامات نهایی خود را برای جذب عباس کهریزی انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/141314" target="_blank">📅 18:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGvWeCUakoroe7IXItWRHiSFBdvq5sKTA4b3l-sbFbo09SLni43chHWaI4_fOPbE4_PH531fK94G-c0OP3qoU8gkMm5RSmeTn7yoaNkvsOsrF3GaDsOfqdoccaKGxFo0Y7iLIBHO3JX0fTMpYKMn6xIr5mYM6_OgaV4Y4F4DfdZSf3XT8Ihv8hfOkZlrOw1z4YvjDqXiLnJF7c3xv-XaSUyGml-XxVJE3EeILh8uBrYIIwHi0g7ZbP4nrcEJE3wQiJm2ENswX90zS6NfclucsFvtjzWzwZMmkvJiZcCZeGYFUcz_hKgB1Wkoj-2w_mvXyJSN7wujImX5s810EGxdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
علیپور؛ کابوس همیشگی صنعت نفت
🔥
🔴
علی‌رغم بازگشت تازه از مصدومیت، علی علیپور در نیمه دوم وارد زمین شد و از روی نقطه پنالتی گلزنی کرد
🔴
او پیش از این دیدار ۶ بار دروازه صنعت نفت را باز کرده بود و با این گل، شمار گل‌هایش را به عدد ۷ رساند تا برترین گلزن تقابل‌های یک دهه اخیر پرسپولیس و صنعت نفت لقب بگیرد
👏
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/141313" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141312" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/141311" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فوری ؛ خبرگزاری ایسنا :
🔴
🔴
🔴
فیفا در جواب استعلام باشگاه استقلال ، پاسخ داده که یاسر آسانی رسما فسخ کرده است و بازی کردنش غیرقانونی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/141310" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
با تصمیم زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/141309" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/141308" target="_blank">📅 13:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141307" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/141306" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzBjkjLiP4q8SLvMho854gfvBuaWPH87-fFxFNtDaac-iYSvfZA3LFydRSGv6BAGW42OOlIzKeNSiqW-jEgc7c1C1hgk3slQwMoI6dYfQDXJt8l6w56rxN6V8UV39G5prtSExC250ZcAar4bpNtXh1r9dFE2AMBm_nzaP0Yj_bJ2lgc1XfTGBZAKctQNInSqossJu84RNeifCXHAatITjqoUCGK9C_9DWa5KTbr6FPqspPTs-ZpHC8nn5AmTrjIccaMNdYH2HcrjlSEC9ldFKAxeZ8MCEaekOAaialHw9lf7Av3ItdWoNRyFcpDjQBws8Ns976N7AqmZdoJgwySMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیژن حیدری داور بازی‌ معوقه پرسپولیس - خیبر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
😀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141305" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVVbPv4Zn-dMflY4UklSeVRSoWNsUvQp30PyRb0a3wa-78W8aJMVjVe97uHHQbLGoi4XQkL69F52TLo-f9Wa0h6AgxNdM1IFkRYuQog2_Mdh_m4PlYM4BToSq1IEGAuTlf4pzJwxyC4UoxuUQauD7Cai7-jm5wT_2Vvo2PUDWUoLtJmUatsdZja7Ro43FmBiIE7yifXlr0N0XjCCuhFWMpmA2SfcF2HCu0D_CG4mHek8zXri2t6_imt4Iw5WWtYSjFjgolzZOr0mr_ncLeeIGv8iL7ZeeVl59qt5QncQGkORvDn8KYYXsONlz9pGMVdA7ZIr8g5SM-MZAoX3H2E8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool
🆚
🔵
Man City
⏰
Tonight 19:00
🏟
Anfield
🟣
سیتی در ۵ بازی لیگ ۱۳ گل زده و با میانگین ۲.۶ گل، قدرت تمام‌کنندگی بالاتری نسبت به لیورپولِ ۷ گله داشته؛ در مقابل، قرمزها در آنفیلد از امتیاز میزبانی بهره می‌برند. غیبت الکساندر ایساک و کودی خاکپو می‌تونه قدرت هجومی لیورپول رو کاهش بده، درحالی‌که هالند با ۵ گل بهترین تهدید سیتی محسوب می‌شه.
از نظر مدل آماری Opta، شانس برد سیتی ۴۰.۷٪، لیورپول ۳۴.۶٪ و مساوی ۲۴.۷٪ برآورد شده؛ برتری آماری خفیف با سیتی است.
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141304" target="_blank">📅 13:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgOrXKubIo6T_XFd0N3wqZWCdJmplEhWsYIbiTqkYjO1Mhc-2lnH5fUDes9dONsr3GPW_pxIIFn-mvSAUzHiaH2yks6BlJ1prHtH_9wexFqiohkv5AfwD85tp0Aqn98wL8SH-YT51vtBU-qlI_Am3-HPSfzIx5VFkHZIkbmZkRMMO2e7FGqD_9ohvbIaejKwVzw6HNdbSUhzDqoJI6e88H-egQZhIvmSVpIDy8OYecbkBf0i-PL6AjcawqDthCC1Oe-YiLWfVGSY3eVbfVPxADSea1e0sONi8MrCyQ5oj85IGqWPaZOk_Vu9RJ2Voiz2lBlqKX-G5KNvp1g1XQDOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ابرقویی تارتار رو راضی نکرد؛ با بازگشت کنعانی و ایری، احتمالاً دوباره نیمکت‌نشین میشه.
🎙
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141303" target="_blank">📅 12:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇷
👤
🎙
برانکو ایوانکوویچ: می‌توانم بگویم بهترین نتایج ایران در 40 سال اخیر را من به دست آوردم؛ قهرمان بازی‌های آسیایی شدیم و به جام جهانی 2006 صعود کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141302" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
درخشش سرخ‌پوشان ازبکستانی پرسپولیس در رسانه‌های کشورشان!
🗣️
ایگور سرگیف با پاس گل در دقیقه ۵ و اوستون اورونوف با گلزنی در دقیقه ۸۴، نقش مهمی در پیروزی ۳-۱ پرسپولیس مقابل صنعت نفت داشتن.
🗣
درخشش این دو ملی‌پوش ازبکستانی مورد توجه رسانه‌های کشورشون قرار گرفته…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141301" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
⚽️
گل‌های پرسپولیس در بازی تدارکاتی دیروز مقابل فولاد هرمزگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141300" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141299" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=mlRL_on4DJT0VWrl5Z6UHJFzHtt-gcaUKbwKF9tRKSPZzI9DNHXR9FFY3hFPuFpBXiV3tQMItWyNYl43qBojfXJmykhSnh1Tq2WPcoZaJ0fZAhS61KJ0POd58uer3qwoCBiQ05h-Wd9O3FkGCcDDU-hvqQ2HMozBt2h8tQrAOhTZke5L7zgo7VHgkLImYR0pz-HNEgC8lkN-1tIULE3GWVNKOHQIiTeDr-UE5PJsG8_FOCNg7vp4Xcu23B7jJJOULoe08a3n8yTU9EX-iMnb2Q8cJ9JztcwRcYUD2-u97QtTMec2oT3_PchPNfakG4BYZOj4Uy2KyFYFOBstIgRZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=mlRL_on4DJT0VWrl5Z6UHJFzHtt-gcaUKbwKF9tRKSPZzI9DNHXR9FFY3hFPuFpBXiV3tQMItWyNYl43qBojfXJmykhSnh1Tq2WPcoZaJ0fZAhS61KJ0POd58uer3qwoCBiQ05h-Wd9O3FkGCcDDU-hvqQ2HMozBt2h8tQrAOhTZke5L7zgo7VHgkLImYR0pz-HNEgC8lkN-1tIULE3GWVNKOHQIiTeDr-UE5PJsG8_FOCNg7vp4Xcu23B7jJJOULoe08a3n8yTU9EX-iMnb2Q8cJ9JztcwRcYUD2-u97QtTMec2oT3_PchPNfakG4BYZOj4Uy2KyFYFOBstIgRZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141298" target="_blank">📅 09:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLu7ywhjPFhIxGh4LuQQ5409mmHbK4eAvN5Iqiix4oaa0ALbRajiYpufvCHlwX8FHxwWh4XDAMxx5t8p8QmemW1UQKQD1_buNCTGxXCwsDqowLWLPSTdf2zYlwXpnRUu_82FHNCixNQvm3HETf8gXaC8WN9bP_OzeM0PLLc1ipaj43tuvFXR-8Zie6dUt10IUdDxT0ZumTOpvuiLKG9dAQ2fP1ASOiheJKm9BuLS_-Gye5xrlAg-5MXLskiD6NbyhAawA-TWyS-oeraI4jms6zoIpYx_pS5FEP32wl7N12R2r0TxyxkJEvb3pBxkEMtV0oUjRDQ0q9ooRE67CnoZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهرآبادی از هفته‌ی بعدی فرصت بیشتری برای بازی کردن برای پرسپولیس دراختیار خواهد داشت.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141297" target="_blank">📅 09:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUkmQoIL8OO3hYt-5q-DVpq2JgKVXkRkgGZliUZYQZ07nwfNxiuXUyhV89lOgyUUNEH2D5t9TXy_B0-r2BjJbW1IbZnJzn0MJnKdlt5Q6Y--jZp6ye-lVCIfVtVbmsittN2f2V7MiA_I_iez-rm9gkvgJMoj6d2GHOny4gztlmMA85lNZpZFlFWrp_onyToD0_odclCnF3ZS9TUXAoXU_4ZzddSHplMiZz11W1C0e6NHNb-yzkuLjxvcQAP_-vPiEGc8I-7bVjLRcv_YvpoHQYyOmQRP8P77Mio1Fp-HemM3OVqjtvGhq3fXrfqNtt0754B9rUSjYkxCwuGObzGXTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141296" target="_blank">📅 08:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=soXZz8Ou_3NLwV9R-4dC2scD_gp5s4XrqeDQaNAy48hPR7InjE0mx7GWsTHyP-7X4o8q3xfFnEIxF6wULuLdCRKocD8y7NG7M1s_tIi-TeAueQeepxp5Lo7QdXvg3ouMk9MPGIIcQwuJUfjsMPw09Mvzd8tVux2tTnO5KeuXJaFMJbCj1J-sw6SWOI22ub5IrDuU3YvaqFYFKw_lO9BpJ0eHJRvt5GWYWd4SXdPf5JFW2piLMtZw8kopODRhjy3Y9t7eZ4B-wEPSOn2x8byaTLy0WntgeJpzDRxxgzLtagYZYrxDXDMfpteH-S8SrzcUGY0qefalNbP-FCXaMzm4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=soXZz8Ou_3NLwV9R-4dC2scD_gp5s4XrqeDQaNAy48hPR7InjE0mx7GWsTHyP-7X4o8q3xfFnEIxF6wULuLdCRKocD8y7NG7M1s_tIi-TeAueQeepxp5Lo7QdXvg3ouMk9MPGIIcQwuJUfjsMPw09Mvzd8tVux2tTnO5KeuXJaFMJbCj1J-sw6SWOI22ub5IrDuU3YvaqFYFKw_lO9BpJ0eHJRvt5GWYWd4SXdPf5JFW2piLMtZw8kopODRhjy3Y9t7eZ4B-wEPSOn2x8byaTLy0WntgeJpzDRxxgzLtagYZYrxDXDMfpteH-S8SrzcUGY0qefalNbP-FCXaMzm4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141295" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeEg_BMrH-FOaAt4J61Ne5FkY0vD21Ceu5rYiA_7ZH2HlRosxax3xq-x8D2Qbz2PgywIfpJaLt5OKatV1lOx8O_7gfp_Z7mYE1bKRhKMMBMrmQfGoSPcRNUn28FME6W9PhMS77Obw7KXix29er4tawvQ25qYbrZ-JpwFv9Yb89GVsskBivQCC1WCgFWK7L_lfg7hzBTppyLhSjZEmthp52xLrOnfx1lqVPvefd0QJtCAxOgtN8irJlyv9vnTWcpZHgC7_vAn4SopBl0G567MPqV0KwN9yxhSGYuN3g8FK3nnUQO-TnXi9gsF-wI7NiORKOGDd-oqcA47m3vybAvSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد خدابنده‌لو به اردوی بعدی تیم ملی دعوت خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/141294" target="_blank">📅 23:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EsnWU9YDldTf5_rnJKifKcP6b4ZU9YOOPXfSHETKHWHmFxDI-_2Dj2Wc09udx_AVxb6Ckys2tC50oAutgEQiF4s306u1iX-bNUozNy1bDZdfs9scKE154jukYiE0x88zL_jvN10lCRIJPNqYOWtAs7j2shh-QA4R49zA4a6PjRCS_jchoUxuyebEGXEAHQUYDlRrRm5LGzTdyS9Q8Utr2JgkxL3wNUYEdYnFd7PB3FKlYnwNgAGLWrcTlveDPRchXrby0cnojN56-3DmTw65bIzde1Zsbh7_M3KuCUaSY4Ji1h0D6-L7-_K_9By5rRYHN6nriE1VcYrDaWa2HZMYsSac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EsnWU9YDldTf5_rnJKifKcP6b4ZU9YOOPXfSHETKHWHmFxDI-_2Dj2Wc09udx_AVxb6Ckys2tC50oAutgEQiF4s306u1iX-bNUozNy1bDZdfs9scKE154jukYiE0x88zL_jvN10lCRIJPNqYOWtAs7j2shh-QA4R49zA4a6PjRCS_jchoUxuyebEGXEAHQUYDlRrRm5LGzTdyS9Q8Utr2JgkxL3wNUYEdYnFd7PB3FKlYnwNgAGLWrcTlveDPRchXrby0cnojN56-3DmTw65bIzde1Zsbh7_M3KuCUaSY4Ji1h0D6-L7-_K_9By5rRYHN6nriE1VcYrDaWa2HZMYsSac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: تو فرودگاه بغداد ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141293" target="_blank">📅 23:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cADbTiLaZs2nGMio0rZEUrKkzf5LzYgW-TNh2UQT1BO7596rDOMFq8Ep1VeE0MY26FOFLRjHp8_etOXMOqJwox6uJeOX5LL7ddzrcoMRvE6X1NrsvfO2Kg_cNyi_yRHio8LcVKxdWxzsbRekiXe02EdvPDp9lm0oHOIAAfsWtwivrPEd_ZKHQsTHGg5RHHbhvAMwYH9JhXmyVDm0sucfjJYNwm2OjpzWEdNO24A62nzArzyszkOo66UFAuupF0ByNidZ-B8h7yxsfCejJ7gxxfHoGveAvpKImLFE2x3QUGJdMudK3h7oVQbz6fs1Bjuz2bKHjTmkzDtNQVPbNlB2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
⭕️
⭕️
علی علیپور و تیوی بیفوما با هم مجموعاً روی 73 درصد گلای این فصل پرسپولیس موثر بودن
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141292" target="_blank">📅 23:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/141291" target="_blank">📅 22:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141290" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=Ulo7e9LfZHFEaFUFnqGSAHR7dRmaS251R5L_AgbXkTPRG5RVI0ivolEc9dwhhfldylVAw-vtrHfj78gOFKgP39LevnqFJr8mjQYJleQ_ncoLj5szaJRah0CiFhhQxeCkdnc-J7c4KRPs97GT_-m9pbYjgQH7D88jCBwwwILRV5dqRliruzSDzYgO0hfZGEdbYoKPM8QgFo9Wg-vGmcsHLoyXM7ItTiwlQolsieMm4jG0d9HAI2XSD8oHAi_g6LZJHxVNwEyyfI_-LnpFglDCw2FKzZ-T7aa4Ni8_4j6w1DAQhKS5zr3UhI8cvt3z1Lg_68rJwH_CH_gshtpC6yYMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=Ulo7e9LfZHFEaFUFnqGSAHR7dRmaS251R5L_AgbXkTPRG5RVI0ivolEc9dwhhfldylVAw-vtrHfj78gOFKgP39LevnqFJr8mjQYJleQ_ncoLj5szaJRah0CiFhhQxeCkdnc-J7c4KRPs97GT_-m9pbYjgQH7D88jCBwwwILRV5dqRliruzSDzYgO0hfZGEdbYoKPM8QgFo9Wg-vGmcsHLoyXM7ItTiwlQolsieMm4jG0d9HAI2XSD8oHAi_g6LZJHxVNwEyyfI_-LnpFglDCw2FKzZ-T7aa4Ni8_4j6w1DAQhKS5zr3UhI8cvt3z1Lg_68rJwH_CH_gshtpC6yYMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕
محبوبیت؛ فراتر از تصور
🥹
🔴
هواداری که با وجود سختی‌های جسمانی و مشکلات مالی، خودش را به ورزشگاه می‌رساند تا پرسپولیس محبوبش را ببیند و تشویق کند، به معنای واقعی عشق به پیراهن سرخ را نشان می‌دهد
🔥
🔴
آقای بازیکن! قدر چنین هوادارانی را بدانید؛ آن‌ها بزرگ‌ترین سرمایه پرسپولیس هستند
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141289" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV9pMZzp_GFbVR4p_cwbQNLUnajaS5tMCC16vMnNmOVH8XF-lVWqiIkkf-ac_LJ8XEZacr7EI96jpgJ8Z_exUaLJCeopSf0pBdnOAP6tvmgc6ofoodLsuVBG-AbBLu4OwP2zuv82AzD4xYcbwM95agv5aFgxYNcsVO5CDPhcoBh4kivPhb_QWA-UaVbIMi5xgtU06ETgJtbSPeMX4uB7PzilohcKiGjOueHQtaQSw1Ig3MBZ7huZKDG41Si2SxEvka6TQEQYyK0mShnjtJJoi826BPlvyWoVK4DT2NmJNWsUijWcsNv8pU3QXIRY-X1DsQbcqwnLZK92Llsw--HbOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به پیشرفت خودش کمک کند و هم اورونوف را به اوج آمادگی برساند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141288" target="_blank">📅 22:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
خطیبی از هدایت فجر سپاسی برکنار شد
❌
با اعلام باشگاه فجر سپاسی رسول خطیلی از هدایت این تیم کنار رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141287" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff2cGxHKKCFNQmUm5tLWb_dFjcLiujI0iHBeTQo9rtTZSoGJPoMhNqa0na2Gj037RQbdffC8gYTVpqoqeNd-WFAg35ts6Z2aNF6LTZaisr8Gc8Izb6ALGMSH7A_rpuDg8Ui2UUGXXGqhOlwnB-AZegE_lgmaXvIYLY7WN58MdSqYhzo6tzce5QFq2dmCfZ6hOZ00jmRKwYPSgIf_uGArMEYvLrG0vxo1cqFPEaTTGf_jNCJylATxyXJ_l6WSrngiSOmTPNuOUo1hfECP1JYbqrQITWg3CK9Vt1nF-yPJZTuH0oT9dPlTv56EraCfpJjhU_E2Iz3CkjLSePV73AktJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/141286" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSizO5bT0ZqdzBqAOwPZJe0LjczLIXYP0gKFtBv0ClmiBZCZYhd3KW58dIiSRt82ooYe-6CXFjZKahkozff4p01kte7Rgt3ewvt9pCS9de9di0oMOyNSxNoSp8oFgowxS_VNdibdUUZj5Gd7OacAtFktRBsARQ-L_8MSVcCgZM50UcFNirSHIU6RU_UeRMEtGDSsHO5HQSwgKwS2LktuVLxhuTjBzSLKBCAKliO4PpEBY9dUuJ8sow3uluvpf39ANIHIJrYpVG4XFoD5iZiZtZ_L0ffrEBddCku-064Y_NsUd-EjxhH5xb6ziGg88epW7jfMwdPEs1ATTXPZTNxHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جدول لیگ برتر در پایان هفته هشتم
✔️
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141285" target="_blank">📅 21:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=LBQQZ9gIGbk1Ci2Q3lkv1O495_EgGn0bqE6sjIuCWXIg3xh4kVwdqgIPEkwSbeab4X-PP27t29oF37St3hVY0p_w8CzR5kIJ2doEVM7XWlGJxUYa9CM6koKLL6F76nO2jii2UohtmUoLvqA85b56AlcDHnTYav_hwNkqWFw5EDeLxBapRRzovA8JmDjaJZUXdxUJH4Dw8Us9GKpgMlOuIU8hCw5zm4O7D_qC2ffM9tnFU0TELPJ3v--mz_a4MMJEc5-crNQCt71ImVsOfJYBjyhDWWjAT90yuoesbgUBhN05bjtKvYi8NgH_DGGbKWjDM54-5aBUd1XhoBjzDgdpEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=LBQQZ9gIGbk1Ci2Q3lkv1O495_EgGn0bqE6sjIuCWXIg3xh4kVwdqgIPEkwSbeab4X-PP27t29oF37St3hVY0p_w8CzR5kIJ2doEVM7XWlGJxUYa9CM6koKLL6F76nO2jii2UohtmUoLvqA85b56AlcDHnTYav_hwNkqWFw5EDeLxBapRRzovA8JmDjaJZUXdxUJH4Dw8Us9GKpgMlOuIU8hCw5zm4O7D_qC2ffM9tnFU0TELPJ3v--mz_a4MMJEc5-crNQCt71ImVsOfJYBjyhDWWjAT90yuoesbgUBhN05bjtKvYi8NgH_DGGbKWjDM54-5aBUd1XhoBjzDgdpEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پایان بازی پیکان و شمس آذر، رضا شکاری که پنالتی تیمش را خراب کرده بود، دل و دماغی برای خروج از زمین و رفتن به سمت رختکن نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141284" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=dWTg-03eSyfWELlmVJSrBR-gVO39Oqg-r6NZyduyLixGurql9udR-tWUJJSf2SRPdISwB2JZhqiTeAMPTmocbfNTazdDC_K88BSuBlnJOF209AgHHvuFBuC_M7OVfgROAObe8o1GotzPematjtt7Fs_qCqLFRAAI0pGiYLaoBSb8MM0YPQ2mtvrlQMm8-mrGHQ53D4xVU9JvuO1dWvSE_XDxDDyw43RUAEbPKiaxJYcHeqT1oysRP9gMAR0VOcKe_3yF9IofSJB-I2vM9P11tAdz-3Hs7n0I87U_sYMZw1ar7bZkip5hBZ_8rnZPclq2IhGR4Khx8o8wXzCd102ktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=dWTg-03eSyfWELlmVJSrBR-gVO39Oqg-r6NZyduyLixGurql9udR-tWUJJSf2SRPdISwB2JZhqiTeAMPTmocbfNTazdDC_K88BSuBlnJOF209AgHHvuFBuC_M7OVfgROAObe8o1GotzPematjtt7Fs_qCqLFRAAI0pGiYLaoBSb8MM0YPQ2mtvrlQMm8-mrGHQ53D4xVU9JvuO1dWvSE_XDxDDyw43RUAEbPKiaxJYcHeqT1oysRP9gMAR0VOcKe_3yF9IofSJB-I2vM9P11tAdz-3Hs7n0I87U_sYMZw1ar7bZkip5hBZ_8rnZPclq2IhGR4Khx8o8wXzCd102ktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساکت الهامی به بازیکن تیمش اینطوری سیلی زد
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141283" target="_blank">📅 20:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHxkWEkr7Ba2opzPzbubcilZsb7mch4SsyIZo6ME2pMsWaf8-uYJAXQ8C8y6i4eWjbXbwRmuk62eexKbJQfQJg1BxZEcLka6-XLjVX0IAqtG5Toe8JacqferHI4e_EDHSsg14tVTFAj6jde98QTVK911BqCAiXLiviNOn3Toqjz4udK67h9oD9TVnti9XRKdERnlo0AfIcS_sNqviwWF6CqoAA5mg59hyyRgraTtERZVxgmZBzwwbsUt3wcD6GNiSntpM2z1nDVNacSRWo07G5gokXzgAOCR7htLDA77skBGqZUAgg8yIAbIYJDAktHK_yBNIeOG_3fOXwjUorc52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid
🆚
🟡
Villarreal
⏰
Tonight 22:30
🏟
Estadio Bernabéu
🟠
رئال مادرید در ۷ بازی ابتدایی لالیگا ۱۸ گل زده و فقط ۸ گل دریافت کرده؛ میانگین ۲.۵۷ گل زده در هر بازی نشان‌دهنده قدرت هجومی بالای این تیم است. ویارئال نیز با ۱۳ گل زده و ۱۲ گل خورده، توان هجومی خوبی دارد اما در خط دفاع آسیب‌پذیرتر است. باتوجه به میزبانی رئال در برنابئو و اختلاف کیفیت دفاعی دو تیم، برتری رئال و احتمال گل‌زنی هر دو تیم از سناریوهای قابل بررسی این مسابقه است؛ البته پرسینگ و مالکیت بالای ویارئال می‌تواند بازی را رقابتی کند.
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141282" target="_blank">📅 20:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141281" target="_blank">📅 20:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141280" target="_blank">📅 20:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
🔴
🔴
محسن ربیع‌خواه مهمان ویژه برنامه تلویزیون باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141279" target="_blank">📅 19:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
پویا اسمی که در بازی دیروز برای تیم بزرگسالان پرسپولیس به میدان رفت، امروزم در بازی مقابل جوانان استقلال فیکس بازی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141278" target="_blank">📅 19:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
تیم پرسپولیس از دقایقی دیگر در دیداری دوستانه با بازیکنان ذخیره خود به مصاف فولاد هرمزگان می‌رود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141277" target="_blank">📅 17:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N6NK_moRyWi5m9tnO_Jdfsva0q1xt7o0d3N4c0UQXm1OYYDqax0k9kN_W_Fv2jROkLLGNVVZ9MgVdfFFd_kE9uwZnVyOvt8tuYJxBeb4_w6t4jgFHBgkCXylxNmgacCHbk3Wsgsil_MS8DaONJXqCGiB6gBSy9A5bsbO0gXrFrsc_9AgedEybHE8fkElSKkXdmTf39LSCc3btyupvN29tIMCeVN9eEANNxEw_-kcXwm6JwcF8rCbTQPKB5sGdJstMhV-t7wmDm71GS88MaXwES5Nog2vwZtjL7vUu_ndeMrwiRQdsNGitBTM18wvA_NiAhiqcLwqXN6-gKd7p5jp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/141276" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141275" target="_blank">📅 17:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141274" target="_blank">📅 17:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/podGkUc7oTtMa9SG0HDZypFUIC_-KST4ZDTv6b__3M3ZbW7sZAHHAzkeKFzeg_UdxtoiP6iUUZ2w-Zs27Is4k1xdhQ9FvUy8HcxE2SSZqSIt8la-a1dtY3INEqlbgADhzN7F8TVEVGz14z-r1V6ANO9xERkjne-By6SV_R380RAlQUwpcOwg5FMjtM4NbuFQng2MnPZbIg35kpAwIkmrJSxF97bzTgH36VxgqxFqnaQJtC0rQHfUt903GJwEQxKX2b7lrHQHmPrjzEcKNVVFe_zku1LO5FGLBQjp7Pirp-EyRRAowD8l5b0l5K7cXxmz1J0TDpWEk0X4tl0tC--x4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ارونوف با ۱۶ گل، دومین گلزن خارجی تاریخ پرسپولیس شد؛ فقط ۴ گل تا شکستن رکورد گولسیانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141273" target="_blank">📅 16:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141272" target="_blank">📅 16:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141271" target="_blank">📅 16:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141270" target="_blank">📅 16:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=mG9rui0SZdHu_TnPmiEttqLHD0EsKYl9H3uLin_75gtir90TE9KnB_opvCElnrrs4DDJugTLmjcZeVpY011E_xnjgfGjfDKHYzeM_z3L-tHnRrqGvoUgPbYcNhr_Z9aHlq5lPbMzislbc-XoRxjY_Duy7xmCmWMkqh6QsuG-cU2wuXuGpp7BtgmszZvSgsiP6OVwpSe8q4d1fZtsyJxY1H4f83HrZIprEKsoNNFzapi1LjpD0TWjy538FBTlm4x_qdgqVtQpchev6lO86tix005cTmhgHOU5nIUJxk7Dv_n9cI47BQlCgTPU4RMrFWEUusEvMuj6czxSVv79JmcYEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=mG9rui0SZdHu_TnPmiEttqLHD0EsKYl9H3uLin_75gtir90TE9KnB_opvCElnrrs4DDJugTLmjcZeVpY011E_xnjgfGjfDKHYzeM_z3L-tHnRrqGvoUgPbYcNhr_Z9aHlq5lPbMzislbc-XoRxjY_Duy7xmCmWMkqh6QsuG-cU2wuXuGpp7BtgmszZvSgsiP6OVwpSe8q4d1fZtsyJxY1H4f83HrZIprEKsoNNFzapi1LjpD0TWjy538FBTlm4x_qdgqVtQpchev6lO86tix005cTmhgHOU5nIUJxk7Dv_n9cI47BQlCgTPU4RMrFWEUusEvMuj6czxSVv79JmcYEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ضدحمله زیبا رو ببینید
🔥
🔥
🔥
❌
با ٣ پاسِ تک‌ضرب و پاس‌ تو عمقِ زیبای محبی به بیفوما تک‌به‌تک میشه اما حیف که این کارِ تیمی با گل تموم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141269" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEOl5gl8U2Kp4Ebr-zqjYgTFCuJ0ArUNQIH5CNeXT_Z0dap5ahI5YLmMtxYKXbd7boNQqL-Wak7NR3XPjcEzEXyuLFB_uKJ3y_o-ogqjhiv_CCAj_FhEJFjSSMJYvXUPizTSni4vlV6hfWG5vRIFfw7XLDE8Ps5LLrtoaihYGA4NS8ZNiWzcG3BFr3mtT1GmZZctPIf8VOCzHQEL7TZjoeD28tGxgtcub3YMqPjit1pY6hZYO0AgwbU_t70v0fBwmftS0gyb8U3uKw0Xqg0aJz-Mzu2K6ZX4JVkclvxl5rE-lyzPQmOyYPeoU_9_sW60-Q7ghyjg2KJvyemPuVrWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141268" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=tkp5RtlTtXIT7d5BibNDs1JrUCfCgxpnuzKNv84Ud5N8lTb1Ny_OU2YFY3bg6_6t0x9E_O3DLcVCTdlqiUov7Sx1Haib_fy4ajIsMQYLQGFUyuNRhEZsB8Xqn1AvC0ZxGizMCZrl-XpzX1gCQD-VuW2d2IhLVIAnAjeOs8sXrG7d3JA2XKnTc_cXp4lXFA-P0c6xcPzo1s_gjcjVHHkT3WqHQeWoir4qmP1TC9PAdV2v_L8qidy9QLnC3G96SHKjU58td3PLMrjdL5n86wtRjuqAwThfSUzMR7cc4XyKkRLd61o6XXWXgTzzNaZ7WPVFCdc89itcVG45qOVm25KNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=tkp5RtlTtXIT7d5BibNDs1JrUCfCgxpnuzKNv84Ud5N8lTb1Ny_OU2YFY3bg6_6t0x9E_O3DLcVCTdlqiUov7Sx1Haib_fy4ajIsMQYLQGFUyuNRhEZsB8Xqn1AvC0ZxGizMCZrl-XpzX1gCQD-VuW2d2IhLVIAnAjeOs8sXrG7d3JA2XKnTc_cXp4lXFA-P0c6xcPzo1s_gjcjVHHkT3WqHQeWoir4qmP1TC9PAdV2v_L8qidy9QLnC3G96SHKjU58td3PLMrjdL5n86wtRjuqAwThfSUzMR7cc4XyKkRLd61o6XXWXgTzzNaZ7WPVFCdc89itcVG45qOVm25KNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیفوما و آن فرارهای همیشگی‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141267" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گویا پویا اسمی که امروز به میدان رفت و جوانترین بازیکن تاریخ باشگاه شد یکی از بازیکنان مورد علاقه تارتار هستش و شدیدا بهش علاقه داره و بهش قول داده که بهش بازی بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141266" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
این وسط شله زرد هم فجر و شش تایی کرد ..رسول خطیبی ی تنه فجرو نابود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141265" target="_blank">📅 15:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
فووووووری
🔴
باشگاه پرسپولیس وویس هایی از ایجنت یاسر آسانی داره که به پرسپولیس گفته آسانی بازیکن آزاد هست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141264" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAwkPQyovevPY1kFYwfInT-VIO-BWba8JeoY47o7sGCPS_nmzkgjseLJKgkHWpVRnY3PMVg4cuG1XM5uXnE39rs6qdRs3F-hdIvsHe9UH0R5bJXmpk0TuUk1aTtYq_UtbU-JxnnHkFjAX9bRtmfIix_TpfwoOBFFyEVpOa-7ktoELRLyrxSJx4ikJEePIhwCLs5UG3SJ74j3LY6Tp8DZ0Rz-8hxMfUySdR0bvL2IwvKTvWK0OBBxq1SnYh7G76iOXf7JfKdyb1zZ98ct9ya4Ci2BhHIB3nYifjWZTWeYRsjIDbBDtJCWlGPkFTh6RHGWcIFJBrrv-eSBtxsauB1F1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
نبرد حیثیتی در لیگ برتر؛ شیاطین سرخ مقابل تاتنهام، جدالی برای اثبات قدرت و تثبیت جایگاه!
[
منچستریونایتد
🔴
🆚
⚪️
ت
اتنهام
]
⚽️
منچستریونایتد با تکیه بر امتیاز میزبانی و قدرت در انتقال سریع توپ، به‌دنبال ضربه‌زدن به فضای پشت خط دفاع تاتنهام است. تاتنهام با پرسینگ و بازی مستقیم می‌تواند موقعیت‌های خطرناکی خلق کند، اما فضای خالی پشت مدافعانش نقطه‌ضعف مهمی خواهد بود.
سناریوی آماری محتمل: بازی پرموقعیت با شانس گلزنی هر دو تیم؛ نتیجه نهایی تا حد زیادی به کیفیت استفاده از موقعیت‌ها بستگی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141263" target="_blank">📅 14:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مهدی تاج غیرقانونی بودن قرارداد یاسر آسانی با استقلال رو یادآوری کرد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141262" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiWkVcA2SZZLHLu8H6QQM3uSru5qJnktY3nIjgnFUy5f8LRVriR3gTzExrpzrd6nc-GzkvUrzzbYMI6x4eMMrjLQVfZKNwU4cuD1Les8QUCEFteecb95x-DNMj1z7m7qHAApdFZsLZAbasQViqZNG67m567Y1Wjz1X2TFseXa4EpyO1rYSlesbuGDgsbB9RhqLug1r6z1N_ktHYKDlJNFncJe_wb7U2uJBzGNidV7s86lOxdUPh3PpL2Z0eC1Gv5xaPOLd6dFxsS8fbYvkSNfZDGyZ9LYNNvxM8EMAgi2FDtPSQVxJhxengGQySJLHfVnVqae-siQ4cg4AsrQdikPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141261" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141260" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141259">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
تیوی‌بیفوما وینگر33ساله پرسپولیس با نمره 7.8 بهترین‌بازیکن‌دیدار امشب‌سرخ‌ها برابر نفت شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141259" target="_blank">📅 12:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8jCUzs5Pb0NivQyS7Ofs1PoPWxMPz-OBLUcT2nLXIcqAaOKyVPW1dqjH8wAAjk6QAf0YDkksbofw3Ju1Y100WgrtZUvwI61SuZVuY9uIlCQTi5ckdigLeCZIbeJrr6-z1fFla273E0WFaDIfpoJSkK5vxO-R0Srsofac5EFcIGveKxjHDvn2aJe29Z2rgNcwCA590MujoQgB1k-_di9zoUgLKFZJIbSXz6URJPcNM6rxuMgWhY0GZ8-hRTCwEJXy7x-giRUt2dk0uZ_SuuDQIOTsugYnkUF0s73uzuc0RcwoeRzoGoq4TB_lYufKXQLJKhF9o8I8DIRUHSfpQYPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141258" target="_blank">📅 12:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141257" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/141256" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141255" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373367fda.mp4?token=ifft89bPGyVrqLhjMn-XLWdYq4pDAKR8bfiIlNrNTomHIyxYdUWdm-nN8XUddyreNwNqkbIWzui6g5tePMm4QgYMRUKf2i6P_8hgmw4xUeCmUN2i8ZFB4gKNeRDene8rximjoYW33w6LzDvwryTxIxiYklAlbOcODZCanhXUDnLUj57FdLrupwcxTPcg5RHr99XqHAtxvrpOjWwzbqzLKSnFt8If-BqwsH0uJRCdHRC6OgKIKYSz6FvMc7om3FX7lAHqdHxb1QaNXGOdrj3yuldM0ZUwc3skVX5gF3bB_SBlOqz9x9i18WdR5e3Y5sFgZKK_0CYgDOXWySOzXwhJrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373367fda.mp4?token=ifft89bPGyVrqLhjMn-XLWdYq4pDAKR8bfiIlNrNTomHIyxYdUWdm-nN8XUddyreNwNqkbIWzui6g5tePMm4QgYMRUKf2i6P_8hgmw4xUeCmUN2i8ZFB4gKNeRDene8rximjoYW33w6LzDvwryTxIxiYklAlbOcODZCanhXUDnLUj57FdLrupwcxTPcg5RHr99XqHAtxvrpOjWwzbqzLKSnFt8If-BqwsH0uJRCdHRC6OgKIKYSz6FvMc7om3FX7lAHqdHxb1QaNXGOdrj3yuldM0ZUwc3skVX5gF3bB_SBlOqz9x9i18WdR5e3Y5sFgZKK_0CYgDOXWySOzXwhJrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آنالیز محمد تقوی از بازی پرسپولیس-صنعت‌نفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141254" target="_blank">📅 10:22 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
