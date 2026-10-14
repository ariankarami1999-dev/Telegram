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
<img src="https://cdn4.telesco.pe/file/Kct_bWr6bykHBygcjDHUMRQEj27Rhf0q548toW-pVlLwFTc5BIeGRfdPRfw-4ZFWxi8nqN4NWrRj2wjydoBBWl6UDHts2mnyxxEtV2OY4GS62ncw9LsoubH-w-T1LlUprFFf6obJbxga73hqg6pEhhTNU00CIDqnv5NoEbh7Ph0oBsT2PWficvlV6qHug8oNr0QNBbL9p91DOaHjyeX5etkS1vw8Ht0AkNdWWYZ0iirf0QXEWpCZ6pbU9UGaJO_WS-RmMEEOcAP8gea_7ljWokjLWaC64c-_leSOg4SKS8t9OOGtC2INTf9Pfx0enX64Xu_LbEnN8QYi9ZOq6uXLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-141461">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎙
پایان بازی، کار گل گهر برای صعود سخت شد
🔴
المحرق بحرین 2 _ 0 گل گهر
🔵
گل گهر از دقیقه 55 با اخراج عرفان معصومی ده نفره شده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/141461" target="_blank">📅 21:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">آنچنان تلاشی هم برای دریبل کردن و کارهای ترکیبی نمیکنه قبلنا جسورتر بود برای دریبل زدن</div>
<div class="tg-footer">👁️ 215 · <a href="https://t.me/SorkhTimes/141460" target="_blank">📅 21:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚽
🇮🇷
امروز
به معنای واقعی توپ هامون تو گل نرفت البته که نباید ساده از این فرصت سوزی ها گذشت،کم پیش میاد چنین فرصت هایی که تیم به صدر بره هم استقلال آمادست و تراکتور اگر درگیر حاشیه نشه، ساده نباید از این بازی ها رد شد…
‼️
دوتا بازی این مدلی تیم نتیجه لازم رو نگیره هوادار میگه کادر فنی چه گوهی میخوره که مهاجم تو شش قدم توپو نمیچسبونه به تور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 216 · <a href="https://t.me/SorkhTimes/141459" target="_blank">📅 21:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
🤩
به عقیده من اورونوف در خدمت تیم نیست! داره کم کاری میکنه کاملا تو استارت ها و موقعیت ها مشهوده که ۴۰ درصد توانش هم نمیزاره روی توپ ها
⛔️
این اورونوف کجا اون اورونوفی که میزد تو دفاع کجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮…</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/SorkhTimes/141458" target="_blank">📅 21:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❤️
امروز برخلاف اغلب بازی های گذشته وسط خوب بودیم ولی جلوی رقبای بزرگ تا اینجا مشخصه که وسط باگ داریم و باید تقویت بشه خط هافبک نیم فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/141456" target="_blank">📅 21:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
🤩
به عقیده من اورونوف در خدمت تیم نیست! داره کم کاری میکنه کاملا تو استارت ها و موقعیت ها مشهوده که ۴۰ درصد توانش هم نمیزاره روی توپ ها
⛔️
این اورونوف کجا اون اورونوفی که میزد تو دفاع کجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/SorkhTimes/141455" target="_blank">📅 21:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141454">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر: بعد از پرسپولیس زمان برانکو این پرسپولیس واقعا تیم خوبی است و به مهدی تارتار تبریک می گویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/141454" target="_blank">📅 21:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141453">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPLKL8_rQhoJr6b6yZZi8733faDhA0ZxYYAAfSZ3zaitDGI5knArtlF3NoUUOJQ0KzxRDHqwU9ridwX6CsjQBbQ8eTH7NfDHbGuY3icFXUt0Op6gOmdMxhxC0TJzqLy8qcbrPFk_HWsaQTMgGqFhgPXcf0Dqw-GfgMm9JkMcPCK99uvnLf_hNqjFno2xE9K-hfI1h9Glam4dnx_zi1N2jja6gMmqMU4tunVW2WmyV-md994ITRcHc33SkZVwvhF_kG1HSMylCcNfanWB2EGRChmkCgVJ9w5JWj2eIATt5mXpjJF8k-AmxOYJiZ7GFIVKrPv02B1yOpxcMYj9iAoRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عکس تیمی پرسپولیس پیش از بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/141453" target="_blank">📅 21:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d462da9e2.mp4?token=kP5oPJRubPg-wYOPvy1_xkudOYoD6NM96BvGPyUr02l8JGIkKDVfmdzSJFrjuDfaHo_L81epQ-5PNOTsdFM-3R_ma0c_2np2ZVNMueyMCzY3_q9ar3qqZU2rMl553KM7mTUGkfMn4io7pnL0DrNQkhDCw9Qt3W9oGV-2PPutUOy5a_rQA7NJItDmDyOygHdoRJWfjefUFalrDAVQ0zH3_LS0h18R2353uFRH5FA4sktPBRshcvUhtOpiffSNluxA8Bjl40f_Ug4ogyMqQ4TnlzOs9hrx49D1UjUFyuv7KpQc_pF-J1bdy4GaQyGXrRGxB0-hlGoDl7vd1GYgLD0iYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d462da9e2.mp4?token=kP5oPJRubPg-wYOPvy1_xkudOYoD6NM96BvGPyUr02l8JGIkKDVfmdzSJFrjuDfaHo_L81epQ-5PNOTsdFM-3R_ma0c_2np2ZVNMueyMCzY3_q9ar3qqZU2rMl553KM7mTUGkfMn4io7pnL0DrNQkhDCw9Qt3W9oGV-2PPutUOy5a_rQA7NJItDmDyOygHdoRJWfjefUFalrDAVQ0zH3_LS0h18R2353uFRH5FA4sktPBRshcvUhtOpiffSNluxA8Bjl40f_Ug4ogyMqQ4TnlzOs9hrx49D1UjUFyuv7KpQc_pF-J1bdy4GaQyGXrRGxB0-hlGoDl7vd1GYgLD0iYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر: بعد از پرسپولیس زمان برانکو این پرسپولیس واقعا تیم خوبی است و به مهدی تارتار تبریک می گویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/141452" target="_blank">📅 20:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
مهدی تارتار:
🔴
خداشکر صدرنشین هستیم و باید به همین روند ادامه بدیم.
🔴
باید تیم ما تنوع تاکتیکی داشته باشه.
🔴
از کیفیت بازی امروز راضی نیستم.
🔴
از بازیکنان ممنونم چون این بازی سنگین بود.
🔴
من مخالف برگزاری جام‌حذفی نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/141451" target="_blank">📅 20:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141450">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
مهدی تارتار: در نیمه دوم شرایط ما بهتر شد و موقعیت هایی را از دست دادیم که افسوس میخوریم که چرا گل تبدیل نشد/ خدارا شکر صدرنشین لیگ هستیم و باید همین روند را ادامه دهیم
❌
باید تنوع تاکتیکی داشته باشیم که بتواتیم 3 امتیاز را به دست بیاوریم نه یک امتیاز
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/141450" target="_blank">📅 20:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141449">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb247kGYx058cLBBsRLDToRxW4skz7zWwci0IPbp9Jqe6uJHl3NzLYLDIE3NIFR67LlOq1dDulO6xD_6Rpy5ShQFjUg89PAF0bv50gM4AZ2RLZMRdA_bWq33gvSwy4pq4rMqihHqRt689ywVrU9ZN2PJK2_c4HO7NUvG1uaxwU5tNlQ9P8wRDTzdYNmH7NW8q6vmwcAxpJJxZOurEjLbF8eroa8z-pl30YK8fpKriNQyWsHuOV1nb-y4UPLgmsBoq4WkZLOSsdeachcW9FlK43XsyGGiUf88LvKcdd9GYEfynYaAe4AfVpReZN3ksqIU0Z0UPYn1mNtlno1rZFM4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میکس ویژه وینکوبت آماده‌ست؛ جدال بزرگ امشب با یک میکس اختصاصی!
🔵
Man City
🆚
🔵
PSG
⏰
Tonight 22:30
🏟
Etihad Stadium
⚽️
سیتی با ۸ برد متوالی و پیروزی ۳ - ۰ مقابل لیورپول، با آمادگی بالایی به این جدال می‌رسد؛ در سوی مقابل، پاری‌سن‌ژرمن با میانگین مالکیت ۷۲.۱٪ در نخستین بازی اروپایی، توانایی بالایی در کنترل جریان مسابقه نشان داده است. سیتی در ۴ میزبانی قبلی از پی‌اس‌جی شکست نخورده، اما خط حمله پرتحرک پاریسی‌ها می‌تواند دفاع میزبان را به چالش بکشد. نبرد اصلی در کنترل میانه میدان و استفاده از فضاهای پشت مدافعان شکل می‌گیرد.
✅
[ MIX CODE ]:
cfe622
🎁
کد میکس بالا رو کپی کنید و داخل برگه شرط خود، در سایت وارد کنید و از میکس پیشنهادی بازی‌های امشب نهایت استفاده رو ببرید.
🔗
همین حالا وارد سایت وینکوبت شو و فرصت رو از دست نده و دیدار جذاب امشب رو پیش‌بینی کن:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/141449" target="_blank">📅 20:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b9030706.mp4?token=ebuWDmigGV9qx_sbGYvY61iclmkcihnD6rCiWYYRDPgw8c1aRHVJ-oInbLYP-lqR9rHvtgVIFmQMVZBK08pDioTRFtr3sj5qhQK-QVTq-vt4Lln6sO5rv7pBKsytlBQsCKQkKpBg1CPu57MJOlf6OP6Y5_0mupSPNrzm9UksfSOP-7t6yvQsU3krUsMvWEZZ7gxMOih0m6FhCqB1FK7OmLWXSmjFC1F-h6aHPze463IpZR6SjxKsle0LB9iDjeU1oOanVVYFakdMtIND78ryaWO2kBX6c_BPVXw66SA7iL-BiXCrOM9i9R6wD252p8Umryz-NgPu6QlmoEwwYgR_VhetRXKiIaWSOdfMC5zzra1Jh-NjEBvoVx1kvc8-AeQnwJhBjaUE_5J5TcMpNGJXnbYDqgZ6nwfcmDV3ICb4rq3TfcdMPehOTj6prYRqPRSKyFkeit9wm6FxzSNuz7t_j7JLHz_KEnY_C_rCviOsDuIuQBY8pT4k2UfZ0YgnEngf8Yj_4sGvpt_hq3M4lH1op2Mra25iTMgBx7K9wNGqSEXL4q-IXp2LgfxQYxeux_YO1_DQAYJlh-7qs6-LH2fTcqp1SoaT3j2dwX0uSDfkM1VuAG-0gLvkHJMcsPpqD0L60suKjdELcFjWgSy77P7_39KONpSBJgur2TS0W4_O_lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b9030706.mp4?token=ebuWDmigGV9qx_sbGYvY61iclmkcihnD6rCiWYYRDPgw8c1aRHVJ-oInbLYP-lqR9rHvtgVIFmQMVZBK08pDioTRFtr3sj5qhQK-QVTq-vt4Lln6sO5rv7pBKsytlBQsCKQkKpBg1CPu57MJOlf6OP6Y5_0mupSPNrzm9UksfSOP-7t6yvQsU3krUsMvWEZZ7gxMOih0m6FhCqB1FK7OmLWXSmjFC1F-h6aHPze463IpZR6SjxKsle0LB9iDjeU1oOanVVYFakdMtIND78ryaWO2kBX6c_BPVXw66SA7iL-BiXCrOM9i9R6wD252p8Umryz-NgPu6QlmoEwwYgR_VhetRXKiIaWSOdfMC5zzra1Jh-NjEBvoVx1kvc8-AeQnwJhBjaUE_5J5TcMpNGJXnbYDqgZ6nwfcmDV3ICb4rq3TfcdMPehOTj6prYRqPRSKyFkeit9wm6FxzSNuz7t_j7JLHz_KEnY_C_rCviOsDuIuQBY8pT4k2UfZ0YgnEngf8Yj_4sGvpt_hq3M4lH1op2Mra25iTMgBx7K9wNGqSEXL4q-IXp2LgfxQYxeux_YO1_DQAYJlh-7qs6-LH2fTcqp1SoaT3j2dwX0uSDfkM1VuAG-0gLvkHJMcsPpqD0L60suKjdELcFjWgSy77P7_39KONpSBJgur2TS0W4_O_lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: در نیمه دوم شرایط ما بهتر شد و موقعیت هایی را از دست دادیم که افسوس میخوریم که چرا گل تبدیل نشد/ خدارا شکر صدرنشین لیگ هستیم و باید همین روند را ادامه دهیم
❌
باید تنوع تاکتیکی داشته باشیم که بتواتیم 3 امتیاز را به دست بیاوریم نه یک امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/141448" target="_blank">📅 19:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0297291b4.mp4?token=ES6VuCBCsUEzIQzF9MTj5wvs6SaSkG8wVijDXa4xhKTRO0bPCi5tRsgnkmMkWi2GWchRSjR3nUjtjS6syT95w5edAG5rKhjzfazcvCKT3Agl5oCx6v--RB4_qiW1PPMpbpxQtgnlPMr-3ViZ-cAfHSp6cpqXWoZaas2I7WX32VLKH7DKlHXvMvEwe1sYpFrVGDnXH5-YvQl9DvCq1AjH0BWZJlD-0Zvf6TDRfUCtCTiGGMhQUs5TcPOgjy7R_6Bc3zh1_7vdywGHuYaSOLCfIfIceZdew9okYnE83XA7AqKWxV2tqOzmYUCjHz49BHAHhAeFIRoOrewHMDBcJIXaOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0297291b4.mp4?token=ES6VuCBCsUEzIQzF9MTj5wvs6SaSkG8wVijDXa4xhKTRO0bPCi5tRsgnkmMkWi2GWchRSjR3nUjtjS6syT95w5edAG5rKhjzfazcvCKT3Agl5oCx6v--RB4_qiW1PPMpbpxQtgnlPMr-3ViZ-cAfHSp6cpqXWoZaas2I7WX32VLKH7DKlHXvMvEwe1sYpFrVGDnXH5-YvQl9DvCq1AjH0BWZJlD-0Zvf6TDRfUCtCTiGGMhQUs5TcPOgjy7R_6Bc3zh1_7vdywGHuYaSOLCfIfIceZdew9okYnE83XA7AqKWxV2tqOzmYUCjHz49BHAHhAeFIRoOrewHMDBcJIXaOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: بازی امروز خیلی پرفشار بود/ می دانستیم خیبر در خانه تیم دونده ای است/ خیبر  با توجه به تاکتیک هایی که دارد تیم ها را در خانه اش اذیت می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/141447" target="_blank">📅 19:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkEECENC-n49T_-iqjQpHiy6SQlWiufE6n0I3meUhsshQPuJ1VHCT0kOn5CXo5ccqErn1tJQP4vOFxpV3Lx7vS7UWqXmHe7pId_y8bgWkubJoLCBOVuEBQ4z3FxCE-B5geCook0wDVVa0HTlNPORZEhoF-HMZdg1nvpqvCf_hpUdmtBmE39nvbqPlMuuvM4hWYV_sL_g141FYstm2TWvHC8Ez7UmH28FnNtOK315_q7YlQNr_uLQOP-pgDAUyfQk0fE0ECFEmQPGnAoXxA9p7tKepbGkVlzV0J1lZkT3mn3ui38DSRLeZD8GqDC0VUBho0nHnJJWumK9Bc08MFCLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جدول لیگ برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر و پرسپولیس که با تفاضل گل بهتر صدرنشین شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/141446" target="_blank">📅 19:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dda191766.mp4?token=pJOkvSQi1L21OU_A3M0UvnhCPWhMxDozmCwFndzPEytEKIfFsdfYyocQY0V4S1FKHLLZw6OqiH_bcc8BNlnkVnFWJc2IWTJAFDdybavj_hdXVh6Fp_D_KuEiWxxojEs41adxypQwuTVsMeT4ytVcsG2XnS6j24WfIi4lQd6MmQ7tLwqn-lKXqGXdPiFGhs5F0ChdDuLtTgDhuymvZ7jCpS9nsOGsjhkBYskIuSzB4mJDNH7g0T8Fvv6xVoFxLTysdIYMLySwE5ig7eC0_mJgl2EenKwvMpeVMQ5_pVRIqej0iHjnUz3VT4UxN4Pa6_4X5GnXTxXfRcHb4UCSA2RyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dda191766.mp4?token=pJOkvSQi1L21OU_A3M0UvnhCPWhMxDozmCwFndzPEytEKIfFsdfYyocQY0V4S1FKHLLZw6OqiH_bcc8BNlnkVnFWJc2IWTJAFDdybavj_hdXVh6Fp_D_KuEiWxxojEs41adxypQwuTVsMeT4ytVcsG2XnS6j24WfIi4lQd6MmQ7tLwqn-lKXqGXdPiFGhs5F0ChdDuLtTgDhuymvZ7jCpS9nsOGsjhkBYskIuSzB4mJDNH7g0T8Fvv6xVoFxLTysdIYMLySwE5ig7eC0_mJgl2EenKwvMpeVMQ5_pVRIqej0iHjnUz3VT4UxN4Pa6_4X5GnXTxXfRcHb4UCSA2RyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
**حسرت تارتار در پایان تقابل خیبر و پرسپولیس**
❌
از دست رفتن موقعیت‌های پرتعداد توسط شاگردان؛ پایانی پر از افسوس برای خیبر.⠀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/141445" target="_blank">📅 19:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38f3d6db4.mp4?token=IpcfQrjB1WjpfqxUTZmzLi-BKdEn41pNeEptqyN81UtnKatQVm7dNPWtrnoTuO8tp_tnk8npwgtWsuULJDZMzjCmJ0blrjXEmeyDjjDEkpySoyP8DWIKVAyjgER-gbjN8qOsyBj7zkF1bFKlG7W-F2I-W3ceQpY13iL6-rL8Az62_cxEHLmWfTUf6oHM1I_bm4OqMq6o4JZS_Rz6EOTeFIOXS2nAhi23B2PGS1Pm8Kd3cPoW0pi0-g2cU5RXc4EMxg-ZnoAW9IRTzKhcDA9hnp0bp1lt_-UjdSbypziOvdM0VfkVwFAxdtsq-3h7KIMzeWHAh45dNyEylKpz5_djbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38f3d6db4.mp4?token=IpcfQrjB1WjpfqxUTZmzLi-BKdEn41pNeEptqyN81UtnKatQVm7dNPWtrnoTuO8tp_tnk8npwgtWsuULJDZMzjCmJ0blrjXEmeyDjjDEkpySoyP8DWIKVAyjgER-gbjN8qOsyBj7zkF1bFKlG7W-F2I-W3ceQpY13iL6-rL8Az62_cxEHLmWfTUf6oHM1I_bm4OqMq6o4JZS_Rz6EOTeFIOXS2nAhi23B2PGS1Pm8Kd3cPoW0pi0-g2cU5RXc4EMxg-ZnoAW9IRTzKhcDA9hnp0bp1lt_-UjdSbypziOvdM0VfkVwFAxdtsq-3h7KIMzeWHAh45dNyEylKpz5_djbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اینبار بیفوما هم نفهمید موقعیتش چگونه گل نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/141444" target="_blank">📅 19:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بریم سراغ نیمه دوم انشالله ببریم بازی و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/141443" target="_blank">📅 19:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
نیمه اول خیلی سرد و بی روح بدون هیچ نتیجه ای تمام شد ..صفر بر صفر ..
❌
چمن داغون اجازه بازی زیبا رو نمی‌ده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/141442" target="_blank">📅 18:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
پنالتی واضح روی اوستون اورونوف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/141441" target="_blank">📅 18:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=tAkiU4M5EPkpATeg4_CTfcX2KNg-RR9EhhCNlozgFUxVjLF0mGUJNkFZ7s3TXipSqCkQqUdTrnuRmDX_ca7kxdP69uH4CQP_iVhrvXSJn9rDC2uyWp0kZUzYPbp_hcpc2L9cXVfVjyLPZSBG0OOvSeIRSofOgH_8VGBhsnE9_fSngpJJ9UxmejQjUThwS36BmEwFktYrGuVd-qXQP9RZjGQSONoQ0LSnBCdMmRbmPgc9HWio9aI85FnVOEw-pUAEwAWmIMmxpWhYyb7P_KklP8DPcQOSkDaXeFIce-ZQWGopNLXr3qqL05V72xgg2abRUhPS4j1BjIwdlNVf2fhS1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=tAkiU4M5EPkpATeg4_CTfcX2KNg-RR9EhhCNlozgFUxVjLF0mGUJNkFZ7s3TXipSqCkQqUdTrnuRmDX_ca7kxdP69uH4CQP_iVhrvXSJn9rDC2uyWp0kZUzYPbp_hcpc2L9cXVfVjyLPZSBG0OOvSeIRSofOgH_8VGBhsnE9_fSngpJJ9UxmejQjUThwS36BmEwFktYrGuVd-qXQP9RZjGQSONoQ0LSnBCdMmRbmPgc9HWio9aI85FnVOEw-pUAEwAWmIMmxpWhYyb7P_KklP8DPcQOSkDaXeFIce-ZQWGopNLXr3qqL05V72xgg2abRUhPS4j1BjIwdlNVf2fhS1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پنالتی واضح روی اوستون اورونوف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/141440" target="_blank">📅 18:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881eeb179.mp4?token=qF366Lb9UDGLbj0cKN2PR7Dqk8CYA7pWuTCcUmfZH5HQMISWUCWMCwM9sZN18ObpDUbCnUNKuy3-dpnj79xihUYTSTNcAjlCmjK4jLXwU4-XRoNb6i2NMLWfuDBQU1TLICUPWAM2wG9MDv56eI6gPaHoKoZ-21bl_Zfy6MN4KkN_Jemjq8gDRPramlpAA4IB1nFaISssAacJmze1fVL19bsAMl5ckWcBQBUzVrj_aytHQVfsS7A3h6rONUGiUW0-A_55NnXfqZObHdDeTziRrqr79SsqnEVpRfGZd05zlUzNUPdvBMLYMnaqr3_lUKzfuYn7e8wIItgtABoCzHmjmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881eeb179.mp4?token=qF366Lb9UDGLbj0cKN2PR7Dqk8CYA7pWuTCcUmfZH5HQMISWUCWMCwM9sZN18ObpDUbCnUNKuy3-dpnj79xihUYTSTNcAjlCmjK4jLXwU4-XRoNb6i2NMLWfuDBQU1TLICUPWAM2wG9MDv56eI6gPaHoKoZ-21bl_Zfy6MN4KkN_Jemjq8gDRPramlpAA4IB1nFaISssAacJmze1fVL19bsAMl5ckWcBQBUzVrj_aytHQVfsS7A3h6rONUGiUW0-A_55NnXfqZObHdDeTziRrqr79SsqnEVpRfGZd05zlUzNUPdvBMLYMnaqr3_lUKzfuYn7e8wIItgtABoCzHmjmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
پشماممممممم از قیچی برگردون اورونوف که توپ گل نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/141439" target="_blank">📅 17:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
برای تیمی که روی زمین بازی می‌کنه این کیفیت زمین از خود حریف بدتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/141438" target="_blank">📅 17:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
چمن از بس داغونه چهارتا پاس نمیتونن بهم بدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/141437" target="_blank">📅 17:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس و سرنوشت ساز بازی ..الهی به امید توووووو...سه امتیازی که مارو به صدر جدول می‌بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141436" target="_blank">📅 17:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
اعلام ترکیب پرسپولیس برای مصاف با خیبر
🔻
پیام نیازمند، محمد‌مهدی زارع، حسین ابرقویی‌نژاد، مجید عیدی، مهدی تیکدری‌نژاد، پویا پورعلی، محمد خدابنده‌لو، محمد‌مهدی محبی، اوستون اورونوف، ایگور سرگیف و علی علیپور.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/141435" target="_blank">📅 17:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترکیب پرسپولیس مقابل خیبر از دید ورزش سه
📊
سیستم 442
⏺
پیام نیازمند
⏺
مجید عیدی
⏺
مهدی زارع
⏺
حسین ابرقویی
⏺
مهدی تیکدری
⏺
پویا پورعلی
⏺
محمد خدابنده‌لو
⏺
محمدمهدی محبی
⏺
اوستون اورونوف
⏺
علی علیپور
⏺
ایگور سرگیف
🗣
نظرررتون؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141434" target="_blank">📅 16:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce91480d30.mp4?token=snQWI2ZYBjf_3UzV5Y-YSIe1vmVqtzv3y-LAfxYuw9Ypqh_-XrZzoZ4I_kL82RBNyQRbqSuxibYJlVeEwNJMxUCCmVqV9hs2E3Xam5rqUjeH9cWdkM5aKBw5KgsbrXscZjchLL7M3PTMQuVk15uKUFuJpu5yBgz1ylD6kkbgXcgbNCezsJlz0h4NFowi0qMtayMekyhf14MkKVrAIYf0YYpD0ye-JcMR4CsXe16s4FFgFeV9ICwI3P_PWZC7jAm0LPGa35SSzEHIU928yn-b_6pciYXxaCD2zBRgsFny84exBlGLzonVpD3xlf1TJPVZnrZdJqQZa_lTqDj1afmJBnCZP8EXMRjs8X34bNwm79AmsOs6n57s21GsZWDRAzAU6726Ma4sqa6aKWFmDD7pFYziZcGrfjOyj1sAtonFsAZoFwHXWDg_Y0yI3O2UKrhL0EAV__vcaLw8vfuEcbmALya8JM7QqxkPclgeIzlrB1gtGnw2n67NjAO8ZvvbGTsdcgUEA6B_Y2hu6KBDeOjvLDkjXrI_hi_da3vSUy6S1saD8JK8hDOXEJFJ7mC174NSBkmOufm2i1L1-PvUW3y42ayw2GOnpyvlVw6tgxJ_W7qnWc6D8KfLqe8GDJUr13eIFg7ZGya2_GytXK6eMpU-wVdqHJ2zgieVhQpjJJTolSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce91480d30.mp4?token=snQWI2ZYBjf_3UzV5Y-YSIe1vmVqtzv3y-LAfxYuw9Ypqh_-XrZzoZ4I_kL82RBNyQRbqSuxibYJlVeEwNJMxUCCmVqV9hs2E3Xam5rqUjeH9cWdkM5aKBw5KgsbrXscZjchLL7M3PTMQuVk15uKUFuJpu5yBgz1ylD6kkbgXcgbNCezsJlz0h4NFowi0qMtayMekyhf14MkKVrAIYf0YYpD0ye-JcMR4CsXe16s4FFgFeV9ICwI3P_PWZC7jAm0LPGa35SSzEHIU928yn-b_6pciYXxaCD2zBRgsFny84exBlGLzonVpD3xlf1TJPVZnrZdJqQZa_lTqDj1afmJBnCZP8EXMRjs8X34bNwm79AmsOs6n57s21GsZWDRAzAU6726Ma4sqa6aKWFmDD7pFYziZcGrfjOyj1sAtonFsAZoFwHXWDg_Y0yI3O2UKrhL0EAV__vcaLw8vfuEcbmALya8JM7QqxkPclgeIzlrB1gtGnw2n67NjAO8ZvvbGTsdcgUEA6B_Y2hu6KBDeOjvLDkjXrI_hi_da3vSUy6S1saD8JK8hDOXEJFJ7mC174NSBkmOufm2i1L1-PvUW3y42ayw2GOnpyvlVw6tgxJ_W7qnWc6D8KfLqe8GDJUr13eIFg7ZGya2_GytXK6eMpU-wVdqHJ2zgieVhQpjJJTolSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
ترمیم تورهای دروازه ورزشگاه تختی خرم‌آباد پیش از شروع بازی!!!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/141433" target="_blank">📅 15:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=ig8TpamRrwLXZfQi0O2OCBzm-NfJhMRFxMdJXMLMbd57aEyXCQH6vyfyzRIpX_A5IeSnelUafO_A_Lniaf-QY20q1qIDaQpx11rnR50Yd-Jn5WOHhtwGoRVfcnWO3yGTDTBc5yYupXvel6m_OcQmeE04VP5AMBYgT-R3AeOdkKjCO-PDKH1aqwdO1X3UzdYdQLVNpPIyY9Lg9J_sr_kLfrXs7RsyNF1uoJNZH8ug6sQQIu-rauBLQwSL3v13vU-hU1_cKbUUHJRl9_aMQZLWOs1ycNpdU4WArV5wAcl76rtUSaoiKhc9wVNFjU32pyNTuD6VdNHHH11Apr9X1CxFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=ig8TpamRrwLXZfQi0O2OCBzm-NfJhMRFxMdJXMLMbd57aEyXCQH6vyfyzRIpX_A5IeSnelUafO_A_Lniaf-QY20q1qIDaQpx11rnR50Yd-Jn5WOHhtwGoRVfcnWO3yGTDTBc5yYupXvel6m_OcQmeE04VP5AMBYgT-R3AeOdkKjCO-PDKH1aqwdO1X3UzdYdQLVNpPIyY9Lg9J_sr_kLfrXs7RsyNF1uoJNZH8ug6sQQIu-rauBLQwSL3v13vU-hU1_cKbUUHJRl9_aMQZLWOs1ycNpdU4WArV5wAcl76rtUSaoiKhc9wVNFjU32pyNTuD6VdNHHH11Apr9X1CxFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
هوادار خیبر: اینجا اصلا پرسپولیسی نداریم؛ بیرانوند بچه سوم را بیاورد و معاف شود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/141432" target="_blank">📅 15:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
محمدحسین میثاقی:
🚨
روز گذشته بیرانوند با مدیران تیم فوتبال نیروی زمینی تهران صحت کرده است که از اول آبان به این تیم برود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/141431" target="_blank">📅 15:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b71aafa3.mp4?token=FB2kkHmgfA_YXJjm27xffsxslJHGN2xOK6NlBAOoOxXHfhnF0x0-Jgg3Vr-7YhI01EAJvMkL02eWu78IzgtVwIqaXfpTrJQg-a5UbsBqpvxzsBINHN_GNDPywn8_s3oPO7vCl0lBgyJlgIuMnZUHBtRDhGF1eVv0tohugy8mDMXR_vLWi8bJzvzf9ypky5qYeAQIqZZo7btdXM2fKPz7I0IN2X0tgK9m3MT8mJv6CrrGQa_w2iav3p6JJI7hAXxTaZV1aD3LIxfuCDrpVo1eP0trjKyCfJvrCnFulXdlgXkR6o8mTB3w6eknMmyeH4Cdicq0xjzfMM6RzmAXe0OFZmPtJrmtPbfSqyUyk5u3zhHWlnYsCQMuia6ncGSzqQ_cUDukKNSrpp-h09_aciUwHkOaPxF72kxsBkEtCkkCr00l6-xReaoxgQrYV-hGOF72CevjDszeLOV4dSZTndG5yd75a2KTekMV6trHAEWMKEJLCvsVrzw48itvZw2SpzK9JuumoF1QmKBI5waZbIkXhekUJs5fmtURSYVgwoPLJBN9uB_FFHtikOKOYGsDkXtAGEOem-F7bh3GRPYMpcizKldMhBbWG9wsNpGbxtibCu-til0u2W2C3zZmiSPLNxE4Q1RLEhRAIhbhmBwagNJ2GpPqKaBHhhO5XuxfjViuvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b71aafa3.mp4?token=FB2kkHmgfA_YXJjm27xffsxslJHGN2xOK6NlBAOoOxXHfhnF0x0-Jgg3Vr-7YhI01EAJvMkL02eWu78IzgtVwIqaXfpTrJQg-a5UbsBqpvxzsBINHN_GNDPywn8_s3oPO7vCl0lBgyJlgIuMnZUHBtRDhGF1eVv0tohugy8mDMXR_vLWi8bJzvzf9ypky5qYeAQIqZZo7btdXM2fKPz7I0IN2X0tgK9m3MT8mJv6CrrGQa_w2iav3p6JJI7hAXxTaZV1aD3LIxfuCDrpVo1eP0trjKyCfJvrCnFulXdlgXkR6o8mTB3w6eknMmyeH4Cdicq0xjzfMM6RzmAXe0OFZmPtJrmtPbfSqyUyk5u3zhHWlnYsCQMuia6ncGSzqQ_cUDukKNSrpp-h09_aciUwHkOaPxF72kxsBkEtCkkCr00l6-xReaoxgQrYV-hGOF72CevjDszeLOV4dSZTndG5yd75a2KTekMV6trHAEWMKEJLCvsVrzw48itvZw2SpzK9JuumoF1QmKBI5waZbIkXhekUJs5fmtURSYVgwoPLJBN9uB_FFHtikOKOYGsDkXtAGEOem-F7bh3GRPYMpcizKldMhBbWG9wsNpGbxtibCu-til0u2W2C3zZmiSPLNxE4Q1RLEhRAIhbhmBwagNJ2GpPqKaBHhhO5XuxfjViuvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏟
⚪️
🟥
آخرین وضعیت ورزشگاه تختی خرم آباد در آستانه بازی خیبر و پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/141430" target="_blank">📅 14:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/141429" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ما باید این موضوع را به پایان برسانیم، و این فقط به این بستگی دارد که ما می‌خواهیم این کار را به چه روشی انجام دهیم: روشی دوستانه یا روشی که آنقدرها هم دوستانه نیست.
❌
شما خیلی زود متوجه خواهید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/141428" target="_blank">📅 14:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141427">
<div class="tg-post-header">📌 پیام #67</div>
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
میزبان خرم‌آباد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/141427" target="_blank">📅 14:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💥
💥
سید جلال حسینی دستیار امیر قلعه‌نویی در تیم ملی شد و قراره در جام ملتهای آسیا قلعه نویی رو همراهی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/141426" target="_blank">📅 14:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F22m4dwXBGMi8yrfM83S1JezGM9vgsCxn6GQGzQ6lMtNEKN05y5TQzmbB0O3HEibzuBjmRxEU5jPKN-7n22AFFRnLq4GaRcQbvklwB2pWGgz7iLaQE_rRpK8yIb0z5K3dgbi_ttuyY6w_4tOIh0Hk03g7XchtiuBoJ7l80a3Z_gfbMFE1vq65_VjTgy_DlvjFU17w0WBu5SnozfUEPXiM3EXS2YJD1t0M9MaaOlJhvzLhSzQ8DbjAkT2gKzHDfDJkvbJLgx2HzKJxShwLW3ZETtN1uIQUgtVN9lasE0OW5NGfUv5TLuKv4w0oMhNB37zbRdllj9PZBY3DtQW3kZOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد غول‌ها در اتحاد؛ سیتی و پاریس برای سلطه بر اروپا!
🔥
⚡️
[
منچسترسیتی
🔵
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
[ نکات کلیدی و مهم ]:
👇
1⃣
.
نبرد مالکیت توپ:
سیتی با پاس‌کاری سریع و پرس از جلو به‌دنبال کنترل ریتم بازی است؛ پاریس روی انتقال سریع حساب می‌کند.
2⃣
.
فضاهای پشت دفاع:
سرعت مهاجمان پاریس می‌تواند خط دفاع سیتی را در ضدحملات به دردسر بیندازد.
3⃣
.
نبرد خط میانی:
تیمی که توپ‌های دوم و دوئل‌های میانه زمین را بیشتر ببرد، شانس بیشتری برای کنترل مسابقه دارد.
4⃣
.
موقعیت‌سازی و گلزنی:
کیفیت ضربات آخر و استفاده از فرصت‌های داخل محوطه، عامل تعیین‌کننده نتیجه خواهد بود.
5⃣
.
سناریوی بازی:
با توجه به سبک هجومی دو تیم، گلزنی برای هردو تیم محتمل است.
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
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/141425" target="_blank">📅 13:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/141424" target="_blank">📅 12:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/141423" target="_blank">📅 10:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKlhW3HTaTdCXkZGewU_7lgiOk2jtrKK-ggV8nQBJJQuGBhsKAda6sPz-6ILOWuo3ZnizjPAGxdbHfzM0hCGwsTPnEWLBl1kem0wAyBpveA0_uEmkpJLYO_a0irulN2TKlWMUGUwy4hOIo5AV7HnRaHEhxBZZtsjOYJi2AaKrlXOLofUwOzBaMgZs8KYorItH-c70B5_uhM6n6gfH319_YXm0CFeofX5fAsJ8TQjdY2VGUMIk12EXrRNv8WShUZP0aC01T4OBnhBl6RUrIVKGXFAzvgk5Kw_zuWsLd7_DNK7LFA0zL88L_fQLLngATedPbZ-357Zcsikn81OkpbUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورزش‌سه: دنیل‌گرا به مرز آمادگی رسیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141422" target="_blank">📅 10:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
حمله تند امیر قلعه‌نویی به عادل فردوسی‌پور: قرارداد من رو گفتی، درآمد خودت را هم بگو. بگو اسپانسرات به کجا وصل هستن. بگو در جام‌جهانی چقدر پول در آوردی. تو فقط ابزاری. هر وقت بخوان میزارنت داخل کمد، هر وقت بخوان میارنت بیرون.   «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141421" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141420" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141419">
<div class="tg-post-header">📌 پیام #59</div>
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
میزبان خرم‌آباد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/141419" target="_blank">📅 09:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlxoxWTVRzg-b9qwgcLNG37fXBMoD-SDAa_xLbK2Vhz_yULe7ApeB9MMXthkrLXGnJwUllFyIxoLPekKiGfWfRfJezkZqsbtnRtGKkR6iXbxFP2I5UhQOHUszNI5MP2dAcQC73eRJiwXJzw_fjbBFCC37_R9U1j0o0JrCNnEoYKYWWH8P0EJ6-wFFcTaN-wuxJHmBS1OYQ9vrS89dpkSbQ4z1_-lsn4N_DoxZkUOEBtDEbxFGO6vTrb6vVtGjKESih3p2PiNnCKvxJbK6GgS06J0EALXALfzWgYuOJKFPh4j07cuFZXq23BjkKIIlZ2IeWoD7qeoHnXDYrBht_ENfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب، لیگ قهرمانان اروپا در اوج هیجان؛ از نبرد سیتی و پاریس تا جدال تاریخی رم و رئال، یک شب تمام‌عیار برای عاشقان فوتبال!
🔥
⚽️
نبرد سیتی و پی‌اس‌جی، تقابل سرعت هجومی و کنترل میانه میدانه؛ جایی که کوچک‌ترین اشتباه دفاعی می‌تونه تعیین‌کننده باشه. رئال مقابل رم از برتری تجربه و کیفیت فردی برخورداره، درحالی‌که لیورپول با وجود غیبت چند مهره مهم، شانس بیشتری برابر لاسک داره. دورتموند هم روی کاغذ برتره، اما ضدحملات بودوگلیمت می‌تونه معادلات بازی رو تغییر بده.
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
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141418" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRlvL49XNuRq71emfmVNMz9MM8AWOwSfVUZov4IqoQCdZe2e1l474z1V_2czjeLhxYnkBtAI2g5329nCSN2FUfAriqREdBAmp8sdX6RncjwpjWyiMFX57k4f5WBbZPlqTwuxLS2EipjcONYgQZ9G4MKEPMO4UPQ7gzJJ_YCmJ2pOlPU0Hbgp0h6cKfkQ6fy21gHTV4H-dXjIxg73aqIDnzNz4pLYzoXl5cS5ERRrqIMkHKhkuxb2pixXT2cmL8IHVO3NA5C7A8BvoURmVator0lg8vtX0ZMJYTniJTLWJWNbRZhQLMZfg3wwO3iTxFW0KcEhegXJlCD4Dln9kcmFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مقایسه نیکمت پرسپولیس و کیسه در دوران محرومیت
❌
کیسه بجز ترکیب اصلی فقط حدود یک همت قرارداد بازیکنان ذخیرشه ، این وسط هم دو سه تا جوان هم گذاشتن روی نیمکت که مثلا ما هم اره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141417" target="_blank">📅 00:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpdLel2Dje8Ghf_mMM-EPkmAZP60AyuPsp7aCFkO5ri3aA6nVaouPru-IJWcESp7tKqJXRRbVobk58yWT7-FeUUYOWbmbpN2Gi4vm-dBKr4L00QsPFjJp8ckJ_rD5s-xo5Jki1M2V7RfN3FAuCDv9Zy9VHlGJbIMk0uR8bdDg0FalwBKMdyZYbk9RnKhQghFNoTFCcJGhYpSa3BRQmWXwWtX4BoCbx1Hj81ZZQBO_09Nu-EEmXj_jBGkB46J38lkH0mYQcUta27Ynuvvtpbquj2_wO3kPyWdj5GiawO0oE87bMWHuq_3Z7iRBCcZBFGszp4anypytDnwvZz55cbH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کریستیانو رونالدو : من کامل‌ترین بازیکن تاریخ فوتبالم! اگه کسی مسی، پله یا مارادونا رو ترجیح می‌ده، این دیگه سلیقه شخصیشه و منم بهش احترام می‌ذارم. اما اینکه یکی بگه کریستیانو رونالدو بازیکن کاملی نیست، یه دروغ محضه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141416" target="_blank">📅 00:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrTtQHO5kNU0F_647Q2qP3T_ZPFKvjxrTf-SG-o2HwiOT2gv4yG0jIREtqae069BZn-6U5WuG3O-zEZvSw9nWVqTHMbgPYRTMCCBmmNngjhXyii1kWValZvbqqgPU-Zq4bAbPmImNEPW2JlKnxKvCqRVVoVg2vR73R02KohOiizuFbfXoo5fXwe7uJsetKHOML4ExsPUtYyepHFvYUQK6j21CEqjj5WGywVlPOeJXhtLb7y86AkBX36T3l-cGcGpxeziOgvh2umgLGXNIYJI2E1GVTdgkRvJkVmOeL_weB-Wn9L14ug0dqtte7jLUBH4HuzOI4CAj-Le94Mk1ijDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
سعیدی: هیچ‌ نمونه مثبت یا حتی مشکوک در لیگ برتر فوتبال نداریم
📘
دکتر رضا سعیدی قائم‌مقام ستاد ملی مبارزه با دوپینگ ایران، وضعیت کنترل و مبارزه با دوپینگ در فوتبال ایران داشت تاکید کرد: در این فصل از رقابت‌های لیگ برتر و لیگ آزادگان هیچ نمونه دوپینگ مثبت یا مشکوکی نداشته‌ایم. باید اعلام کنم به طور کلی در ۲-۳ فصل اخیر هیچ‌نمونه دوپینگی در لیگ برتر و لیگ آزادگان مثبت اعلام نشده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141415" target="_blank">📅 00:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141414" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9243295073.mp4?token=fot_Mvyqgs7MFpvRv_GEXh7hVn7yUUuS-0pLVNRanZP1cIN-qGIbNm9R2GnlEsUkIURSDjvUlCCNl38SlyV0IUPBhXskEOG2BhsuSWFBqE-k0YllKEk_vyLql0rigH6Z6PCgG86JYpIs8cfKOzfccPa_BkVdQMHrlvl-33qX_SOtOaIfL7F2TdXYv4zDf19sZNrGXKn0ifO05rt8wXJyuwGOwAcOSPIVlmlsJqv_1byDpiB0H4pnE8AGnPbQtNDHhS7j_nXwtYq24HpTs92FpzOszDs4bwgOYuktpo0e7tI-z-Qk-t9e9LUhjeYNMjGro20bZcXrzD5EOcX5pSn_TXwEvicPlM9IZPut8s1LiDHZhYyRPulMqRWNUqOt0-r7pgHyccmQNNoe4tH50vnEImAq-kBm8t6VjvRq5ZD3rs8vby3jFjMoVDn-GARySmIrV6U0lEyZLDYalKrke52l66kG_DvKt_N1g5Us_thwlFOGb-UczVAShpH34dnG310EWtbwZcIIeA7l_CGd7LwZWM1TzMn-HRKxFuIQxHqocXe9WPip2PUgdws6RTyPL8a2KUOdRUgzpOBOKRmNdG2jx5oFEJQf6LqqJJgoQzkH8yXc47a0Fbz38LJAZcT_rc_F4vXlECgr3mJ_VWCh5JUTSAcJi6tUl3s-bzcvPN83d5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9243295073.mp4?token=fot_Mvyqgs7MFpvRv_GEXh7hVn7yUUuS-0pLVNRanZP1cIN-qGIbNm9R2GnlEsUkIURSDjvUlCCNl38SlyV0IUPBhXskEOG2BhsuSWFBqE-k0YllKEk_vyLql0rigH6Z6PCgG86JYpIs8cfKOzfccPa_BkVdQMHrlvl-33qX_SOtOaIfL7F2TdXYv4zDf19sZNrGXKn0ifO05rt8wXJyuwGOwAcOSPIVlmlsJqv_1byDpiB0H4pnE8AGnPbQtNDHhS7j_nXwtYq24HpTs92FpzOszDs4bwgOYuktpo0e7tI-z-Qk-t9e9LUhjeYNMjGro20bZcXrzD5EOcX5pSn_TXwEvicPlM9IZPut8s1LiDHZhYyRPulMqRWNUqOt0-r7pgHyccmQNNoe4tH50vnEImAq-kBm8t6VjvRq5ZD3rs8vby3jFjMoVDn-GARySmIrV6U0lEyZLDYalKrke52l66kG_DvKt_N1g5Us_thwlFOGb-UczVAShpH34dnG310EWtbwZcIIeA7l_CGd7LwZWM1TzMn-HRKxFuIQxHqocXe9WPip2PUgdws6RTyPL8a2KUOdRUgzpOBOKRmNdG2jx5oFEJQf6LqqJJgoQzkH8yXc47a0Fbz38LJAZcT_rc_F4vXlECgr3mJ_VWCh5JUTSAcJi6tUl3s-bzcvPN83d5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
فراز کمالوند: پرسپولیس آماده‌ترین تیم لیگ است؛ شناخت کافی از پرسپولیس داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/141413" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
دبل سردار آزمون جلوی الاتحاد توی ۱۶ دقیقه ابتدایی روی پاس غندی پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141412" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ترکیب پرسپولیس مقابل خیبر از دید ورزش سه
📊
سیستم 442
⏺
پیام نیازمند
⏺
مجید عیدی
⏺
مهدی زارع
⏺
حسین ابرقویی
⏺
مهدی تیکدری
⏺
پویا پورعلی
⏺
محمد خدابنده‌لو
⏺
محمدمهدی محبی
⏺
اوستون اورونوف
⏺
علی علیپور
⏺
ایگور سرگیف
🗣
نظرررتون؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141411" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه
🔻
کمیته انضباطی فدراسیون فوتبال با درخواست باشگاه گل‌گهر سیرجان برای تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه موافقت کرد.
🔻
کمیته انضباطی پس از بررسی درخواست باشگاه، با توجه به سپری‌شدن دو جلسه از محرومیت…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141410" target="_blank">📅 22:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
از تهران تا خرم‌آباد با کاروان پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141409" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
❌
محسن بنگر : امید عالیشاه اهل فحاشی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141408" target="_blank">📅 22:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785f027d31.mp4?token=nUpt5h1KDCDVCtJ6YmRr62fSx3vAxx3crN2ZKRjAYhg0pT0FZw-H60r3l01NWk5H5LfysB_ZjvTeZTYCBcYyB8brgUgQzkTKIrf9uiPZjmHOs9RUPp8UxiGi46fP1Le7c7COjwYcI2o_pK0fmiuUO9Dd-i0vweNTe_Us5IKmPvN1B1FN51P5McquuJInvCSf-i3eCjsVUQJvJoTcEen4L-DknkMpKgx7_oylzw8wv4IxucMzHXEJfSFM9BrdQPNXWBVYqnapgQvstk1szLl3nRmjjXpccpd33KtttXsYrJ2-2_eM4c_4PeFn8y9ZEOjia7rSJVCdNaWW9w5121BPgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785f027d31.mp4?token=nUpt5h1KDCDVCtJ6YmRr62fSx3vAxx3crN2ZKRjAYhg0pT0FZw-H60r3l01NWk5H5LfysB_ZjvTeZTYCBcYyB8brgUgQzkTKIrf9uiPZjmHOs9RUPp8UxiGi46fP1Le7c7COjwYcI2o_pK0fmiuUO9Dd-i0vweNTe_Us5IKmPvN1B1FN51P5McquuJInvCSf-i3eCjsVUQJvJoTcEen4L-DknkMpKgx7_oylzw8wv4IxucMzHXEJfSFM9BrdQPNXWBVYqnapgQvstk1szLl3nRmjjXpccpd33KtttXsYrJ2-2_eM4c_4PeFn8y9ZEOjia7rSJVCdNaWW9w5121BPgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
وحید امیری بازیکن سابق پرسپولیس پس از ۷۰۳ روز موفق به گلزنی در لیگ‌برتر اینبار با پیراهن فولاد خوزستان شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141407" target="_blank">📅 21:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFLgQRNnhqWZAjU9B4ukXz9ZmJBufLyVLrA9KoVhrfzW_CrZFkHh4G7Dys6uqGAzsVxUVBMqig6WKtI2u1eIkVxnggAMC0sYG4Nxe6LYDRvCxB7IDicGcdDhPeyk5a_QVMQEqQAIR84_uWfb3e_miuizbpS3P3fGoVEv2eUiRd1TtKepPhRRiHtAe_6hly_OmNR-RnmCXFsT8pFlIbJSbLRva6E9oTmZWIu4LCuzZQ8u4054BozJRkawyST9Bt4DkCz1McKrFQCaWRjwQeyWniRie2V5oRB94KMlxMkTFEWMxCRZr6PuGIkgh0p6dhUfrF-n-E-vmc4gparvd04Kng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تارتار به نشست خبری بازی با خیبر نرسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/141406" target="_blank">📅 21:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpeGVnCZbY7fxjNIqJM9AihsGt2LbRu884jX1vxeUaHmKUtxMqt8rZxLcW50urk-bwdGDLOKPZEXrzJvj6O0CwFTRvGoAwGU2VFtCj-GapAnk9M4T5KRYs3iWLhTsLu8E60rh9A4zlXH-YBxkmbxTwN3Z8qOJD4sEB82eyNf8QvpZqMJVUySl9jdfU2FS26ghr1UD08Epz_uW2ykjHjB13sxCU-HmJAKJFOw5_RI0aFGY56Qhnmrhl_3WazWzmc63byOla9pPKhIWW4XCoD8ddlVfxKsAHMujRVIzbR8BnqM7dLwcKgvB-kNXW97hY4zVpekbI36YIymq6N7-_CfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جهنم استانبول در انتظار غول کاتالان!
🔥
[
گالاتاسرای
🟠
🆚
🔵
بارسلونا
]
⚽️
از نظر آماری، بارسلونا در ۵ بازی اخیرش در لیگ قهرمانان و لالیگا ۵ برد داشته و در مجموع ۲۴ گل زده؛ گالاتاسرای هم در شروع اروپایی‌اش ۳ - ۱ به اسپورتینگ باخته است. بارسا در ۱۰ تقابل قبلی دو تیم، ۶ برد مقابل یک برد گالاتاسرای دارد؛ با این حال، فشار هواداران در استانبول می‌تواند بازی را پیچیده کند.
سناریوی محتمل: برد شاگردان هانسی‌فلیک.
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
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141405" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
مهدی تارتار: از فدراسیون می‌خوام که جام‌حذفی رو برگزار کنه و مام حاضریم فقط با جوانان مون بازی کنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141404" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=lzNof_GNSLU9iPB830j1vsWFA-NKadlG5xrIaOD4plfTSI1P8mPaNYjLXAOHsK50rEHhxjPGH-HNW0btTk5R76PaEgkBYN0rEqtkofni4QDf77MMPud7aAyjG4By8-pC5GuXMv0X8VfcKIq32fSU8V54rxCHzq6ohVxGgUeo-QvRNtmDESLFL3tWqaD9VFw7CwPDE9k85r7M3KrKwpMLdPJINlhVZ6aun3oAluOo_sZvlB0osvrfNJNwbLZ1jA-8HmxUDoA-ACG3_scHV_49g7jgMK_8kX61cFRTwJvCcPci6-rbuGvs20QzS6zKyPPjOtVswZ-VUBQ8OJnnSVNmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=lzNof_GNSLU9iPB830j1vsWFA-NKadlG5xrIaOD4plfTSI1P8mPaNYjLXAOHsK50rEHhxjPGH-HNW0btTk5R76PaEgkBYN0rEqtkofni4QDf77MMPud7aAyjG4By8-pC5GuXMv0X8VfcKIq32fSU8V54rxCHzq6ohVxGgUeo-QvRNtmDESLFL3tWqaD9VFw7CwPDE9k85r7M3KrKwpMLdPJINlhVZ6aun3oAluOo_sZvlB0osvrfNJNwbLZ1jA-8HmxUDoA-ACG3_scHV_49g7jgMK_8kX61cFRTwJvCcPci6-rbuGvs20QzS6zKyPPjOtVswZ-VUBQ8OJnnSVNmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
وضعیت درب محل اقامت باشگاه پرسپولیس هنگام رسیدن تیم پرسپولیس در خرم آباد با حضور هواداران خیبری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141403" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
تارتار : بچه هامون دارن به تناوب بازی میکنن، دست یه مربیم اونقدر باز نیست که بتونه 15 تا بازیکن رو بذاره تو ترکیب، انصافا استون هم تو تمرینات داره تلاش میکنه، من دارم میبینم همین قدری که تیوی بیفوما داره تلاش میکنه استون هم تلاش میکنه ولی به هر حال گوی سبقت…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141402" target="_blank">📅 19:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPhXb1exJn4dnMJm7qlIHeUbD5JTY2ZaGfz8oZbCALRVc0P3YcWsO3eJXjSuNe8oclMpB6V6_6QmXRGrm9jkhAG2A3m8Nqr9jZqrBbH_MLYV6WbWLsbNGjBmFXc3ZNkkLu-odgpOK9VpuRr4CnaaGG-MVLeKNp6AGGzeBEZtqk6LL2RhCqo06bFdYgJJG0QZfSe2b_JRWTWnk1WGFyrTlwvaHOhxVUzsFS-9zBqkQiMsGzKCh6d_cwVzaI2jg_V5HUyz-BmOBfpaP9OoXGZXpeRlBcGotk4pwJI2C7J14w178ql1pbckTLzqhWSeTler0FJoxbg66hmdhYeZtGHCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
جدول لیگ پس از پایان ۳ بازی معوقه هفته هفتم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141401" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
بیفوما در آستانه دیدار مقابل خیبر دچار سرماخوردگی شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141400" target="_blank">📅 17:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
شایعات : بیفوما با برخورد با یکی از بازیکن های جوان پرسپولیس مصدوم شد و بازی فردا رو از دست داد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141399" target="_blank">📅 16:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/141398" target="_blank">📅 16:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141397">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/141397" target="_blank">📅 16:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1L4fgXlGwL42IyezK3U18yK9mD-SSw7VVrSlEUou610D35PneWzLd7MOXIiTsDTN0RVUCRzyFdj1DCmz8p9yF_cC4zdxtn_3NUQ9sqcWDSS56GXis1EuyEypuPNbm3OJQ5K5YWnWuJKT2FIsOTLk-dwsgWjzGdWFVcrojcBnPPcBkvzSfisRp4qL0KD6lOHktoB4xa-wkVndnxdGiIfoonky2v9GALGE3PrpEEOv-T5dui-_gUEGhfRURYV7FeQPM5WfMN8471v_3cmKnvbjUP1Emeq1FE5c46fN5joEZDESxFpOrfFFkUaDkU8G5gfK4WOys_b3uCOQoPizbWohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی عبدی در دیدار فردا در ترکیب خیبر مقابل پرسپولیس حضور خواهد داشت/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/141396" target="_blank">📅 16:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141395" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I590FtDUaffF0kJHE8UKEawvAVuzhZflJ4-rgKEHGiweECEI1hDbaFgEhWvxdDfkjmpU5LPp-e0EYcETbtWolOxwNUfIBrq0gwen_xyuy5keJSYEWtZIHJqQSOSWIyhCzGYS8jpTe6FmULRH_Wh7ewiWRSX7P52GdgewnTgF4RKBeEkw4vz3gSMT4_4LEscTF5XAevW09yX-HZ6TGUcr_BQAcAkY48mkv3VwPu0PYxjSxm77PnTsCUVTpCZj1Vn_k4PuJJjwvcwj7HQz5WzeBPIeqQLAeND1pLNuQclBIk4vlXk1oYI1p6oLgWdGd9g6Vg7biBfAhgt7LeNxO0xJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری به تمرینات پرسپولیس برگشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141394" target="_blank">📅 15:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/141393" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C709TkkABu8gB6dM960tfnyC_5f8zJ2upE5b6NmoR-TeF0qEkkOK-q-sVXdRIW3vpdXOHdOLLe3xIafgLwMA3VqLDMSZxYiVTmY6bmMaKmYr7OJKsc28z0rlS1Ugp5Kx6PaTqC9CCe6ILBHxZCL3LhHcx-YNUB0bUJ8MMAHJdl_w4uS0gk_njmbcTt4z8aNcmw6ff2mQ9eSnbelDCHFkjc5w_0oE8IMeClu0AzVpBnI9qfJpj9c8oJ6-GbM450NrCpzQkxybJjqM5jNyNFSpDd_MRdxPBQ2VeewE3RHkzPQB6rnDchUR5lGlaqydZVoFXdxX5Y-O5JPihulcX1qaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برنامه چهار دیدار معوقه هفته هفتم لیگ برتر
❌
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت. پرسپولیس درصورت برد مقابل خیبر، با 19 امتیاز بالاتر از استقلال و تراکتور صدرنشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141392" target="_blank">📅 15:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
رسیدگی به پرونده محرومیت بیرانوند اول آبان در CAS
❌
❌
دادگاه عالی ورزش اول آبان‌ماه با حضور نمایندگان حقوقی علیرضا بیرانوند، پرسپولیس و فدراسیون فوتبال، دفاعیات طرفین درباره حکم محرومیت چهارماهه این دروازه‌بان را بررسی می‌کند. امکان حضور آنلاین نیز برای…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141391" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/141390" target="_blank">📅 11:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=hPKQPtAbvVxmrufFTzDRS9rIgyjPLChnprH3LTMC1ITYqCFEKlCancvsT_mjYmKQlQe7qDTNgeZ0untsMtPxvV1EUJo8VTeS19oHwrsL1FRGOZyqPFGJ3DP2oWly8wCeubphUaYOC40pF74M_K03tgMMVSFk03Q_5NRw9VfAjUTaHBiV7Wxac8yELwvFmBnb2dkmJZPCoQtwP09rAEd3KE6_4RYMBCx9HbyhB97FxwsBWDctsU5O4pD4OHiLU_Iab9EDdYTXZ1bUOI_O_z5HLZn-xCry7RlVxpQ35Wru2FQHkDM0XNXSH7e8pyJ8BqfMIHYWpxdBbCMNxV3ydjesVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=hPKQPtAbvVxmrufFTzDRS9rIgyjPLChnprH3LTMC1ITYqCFEKlCancvsT_mjYmKQlQe7qDTNgeZ0untsMtPxvV1EUJo8VTeS19oHwrsL1FRGOZyqPFGJ3DP2oWly8wCeubphUaYOC40pF74M_K03tgMMVSFk03Q_5NRw9VfAjUTaHBiV7Wxac8yELwvFmBnb2dkmJZPCoQtwP09rAEd3KE6_4RYMBCx9HbyhB97FxwsBWDctsU5O4pD4OHiLU_Iab9EDdYTXZ1bUOI_O_z5HLZn-xCry7RlVxpQ35Wru2FQHkDM0XNXSH7e8pyJ8BqfMIHYWpxdBbCMNxV3ydjesVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کلیدواژه همیشگی مصاحبه‌های بیرو
درصد، دلار، ماشین، میلیارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141389" target="_blank">📅 10:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141388" target="_blank">📅 10:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx5YSOulpeLGXiqVQGdc6uPmNsLWIW7DukOu-RlxvIEXzQIh9G2gW7CHoZIjSM0_NBVylLLUp3d6k_yOc6jI7e2zbh_Q0ewLZzdbiMUkX7n75rV9C-nhPw3Sgi1-nSw3_e1H7SyxyAyp5iaBKeeIu_7LRKfVS2Yai8aR7sbsrgZyY3-6CEtvKTVnWFcq41KlnV17HpcYHXkZre8aLTCKyclKnUWXX0FRPxqKJ75QkxqGOiOqYLaOQX6EfVE3baprhL3pf5ykMHfikD-ruOJT8KVjo11HYSou823_oKE3HH9ripgNzva-gwMx98o79Jkco1ZlvoRdYwuOtBIPO6bwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
همین یک‌ قاب از تلویزیون و دوخطِ پشت‌سر میثاقی که نوشته « با اثر فوری فسخ کرده است» کافیه برای حقانیت شاکیان و غیرقانونی بودن این آلبانیایی شارلاتان. همین یک صحنه بسه و دیگر هیچ‌!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141387" target="_blank">📅 10:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141386" target="_blank">📅 09:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک سوال نکرد .من گفتم توضیح فنی و گزارش را دادم و اگر کاری نیست برویم چون قرار بود تصمیم گیری کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141385" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
🚨
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد
❌
بیرانوند باید شرایط قانونی سربازی را انجام دهد
❌
او تمرکز لازم را در این چند وقت نداشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141384" target="_blank">📅 09:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=nvT3wKjxVeQ891twH849_repY5JE-Soxl1spCloHu24Vt5bOKK9ohYngEkgzz9DdgKy5E3ibpSb7icmIHEUYBPinAmqK3bK6b1YClcWyLk_x0bVC9-YdXD8f6BLti9K8m0-gM-WlAoZr1QSicepOnFYUh257HOvQQeyFcXPkwSuTayl3WQ2oDtSPbVokIRyiEGRJ-EHB4HDYtuQVf1-JB_ZlVKJmujhojQaVlsipGbo5sUN66EqtgfRa4tTH3TB9K8Kpo09AM8QksLnFudSpQKgUv8qxSab--sMNK3a5Mwzqal8eJYLSYB2Y_GULQdIgmlrwCcC8ND0I96sSppX78Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=nvT3wKjxVeQ891twH849_repY5JE-Soxl1spCloHu24Vt5bOKK9ohYngEkgzz9DdgKy5E3ibpSb7icmIHEUYBPinAmqK3bK6b1YClcWyLk_x0bVC9-YdXD8f6BLti9K8m0-gM-WlAoZr1QSicepOnFYUh257HOvQQeyFcXPkwSuTayl3WQ2oDtSPbVokIRyiEGRJ-EHB4HDYtuQVf1-JB_ZlVKJmujhojQaVlsipGbo5sUN66EqtgfRa4tTH3TB9K8Kpo09AM8QksLnFudSpQKgUv8qxSab--sMNK3a5Mwzqal8eJYLSYB2Y_GULQdIgmlrwCcC8ND0I96sSppX78Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه‌نویی: کنعانی زادگان و علیپور؟ کاش تیم پزشکی بود و می گفتند که آنها مصدوم بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141383" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=UU2FfAoWd_R6FbwKUeFbcIX_HQnDheBNRl2988on8FbYgI75qM4wdCGg3cbYGkXEjTsvMJQnMH5xvJZ6CKCwIDA11gyQEp8kbaZn3HcwqqqabD4R1-Bc_Ud4C00Q5KaBaF2ZrnMzMWG28-hWeLDXjRh0huDBadz0rZPKv5Cpc8OWqxcfignj23Dsz2Ln474bYsDY2mnorn-dxLV91ruVJbibI9tWb9ox1paHUSSsLy2YRRLcgBM8KPZj2sw47Zydf6hZg00ayR0V5CrSuB0np9xFMwQkelRqndlUpOAWf624AxDFCD4XUH0QneQWz4oyUedT1YDoBei67FSpdRJfuJNtqtUG1L9kFoQVZIcrb9G1QIuhoyRBrq3hqlxfLf5AYOXCiiSQBXCg91PF1Gri2YHqemZh-70avJXbcC_F3hfMOMjqhOEd-YzGZrUGEQcJ_1JPMtz8jZzg3gzBzOKfrI6QddhZckLfDH94ASiYZInp5FH8c7KkhgfQwJzTxzuYwFQOox1128nlVcduWsJO-WAnSEqwQR-cmuHM-75y8gIyO32ji3y_L5enkBkV2dJ26B2rN0PTnx5tlHppF4VzYJpBtF44UFLu74fG9wAST-dkfDmfCmNHDXas03JdI3VxBzENdqaIr__z3MXetJhBJL2iWeWTGXPmQjt7WoAr68k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=UU2FfAoWd_R6FbwKUeFbcIX_HQnDheBNRl2988on8FbYgI75qM4wdCGg3cbYGkXEjTsvMJQnMH5xvJZ6CKCwIDA11gyQEp8kbaZn3HcwqqqabD4R1-Bc_Ud4C00Q5KaBaF2ZrnMzMWG28-hWeLDXjRh0huDBadz0rZPKv5Cpc8OWqxcfignj23Dsz2Ln474bYsDY2mnorn-dxLV91ruVJbibI9tWb9ox1paHUSSsLy2YRRLcgBM8KPZj2sw47Zydf6hZg00ayR0V5CrSuB0np9xFMwQkelRqndlUpOAWf624AxDFCD4XUH0QneQWz4oyUedT1YDoBei67FSpdRJfuJNtqtUG1L9kFoQVZIcrb9G1QIuhoyRBrq3hqlxfLf5AYOXCiiSQBXCg91PF1Gri2YHqemZh-70avJXbcC_F3hfMOMjqhOEd-YzGZrUGEQcJ_1JPMtz8jZzg3gzBzOKfrI6QddhZckLfDH94ASiYZInp5FH8c7KkhgfQwJzTxzuYwFQOox1128nlVcduWsJO-WAnSEqwQR-cmuHM-75y8gIyO32ji3y_L5enkBkV2dJ26B2rN0PTnx5tlHppF4VzYJpBtF44UFLu74fG9wAST-dkfDmfCmNHDXas03JdI3VxBzENdqaIr__z3MXetJhBJL2iWeWTGXPmQjt7WoAr68k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی: در پست خدابنده‌لو، عزت‌اللهی، قربانی، حاجی‌عیدی و نورافکن را داریم و به همین دلیل دعوت نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141382" target="_blank">📅 09:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxZt_-3RH6nlNjxM0rp_Ack3OuOiz3ntkMOCl3kGHaJYXmjhTP_eYu2iEqYHgkOPi_xn8qP71PqKUfQ3laSKYdmw4dFwJyzhes6FKfoJRWZ2PukqYhiX58lNWsecWPS7cxF0oWm7iCwPTuUPVGqZX3pBtey6MHP1t2YpJjXFQJXGlPad5i-R6QinXl5JcgqE8UIo-5XrIQKTFAqz3Ys6bEGOD-Y1F8CJquX6RLaMVJ7Nq-vJM2OV_1fZ8CzgehB7q7lj-UMIzT-wFBlH1IOA4HugBwx203Dvv5olVOfoBUfrgzHX92BIUjmj_ewJwmvR59mOYTIVldf_GehkjYHAvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
به رئیست بگو خر خودتی…دستتون رو شده؛۳۰ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141381" target="_blank">📅 08:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141380">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2Vw5pAh4K6fAQX9XK2WchBihWIt2ZqLVN-lLhUKa1XKjSwWq_JFKL8JjcFpcBm2hDGFsk_MigWvLkU2DfkVRYS-VD1H1za6sRVrtT2CY1Hinki8Iuj6MQA0D6lS4tCm37kF4S1n4RhFYNWj3omMOXStwO_qGVQ4M1r6FSwBJe3SDGb3Sjy_-MNLIAVjAkvpzHjA1AlsOHy4YzHUEib8bu5PSiCh7cYDB07e5GJsiIv0TEhJE-mm2LjLHEfHbS2WfJFXTA7m_Im17RLCk21eyCpWqn-GRNwzjBF7rajKxLRPd4nHy4UVXQLD3ku_45IWrUlJ103lENyRjr7zyWNezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب اروپا در تب‌وتاب شب‌های سرنوشت‌ساز؛ جایی که غفلت، تاوانی به قیمت امتیاز دارد!
🔥
⚽️
فرداشب آرسنال با ضریب ۱.۲۱ و اینتر با ضریب ۱.۲۳ از نگاه ضرایب، مدعیان اصلی پیروزی هستن؛ بارسلونا هم با ضریب ۱.۲۶ شانس بالایی مقابل گالاتاسرای دارد. تقابل اتلتیکو مادرید و منچستریونایتد با ضرایب ۱.۹۱ و ۳.۶۴، از جذاب‌ترین بازی‌های فرداشبه؛ درحالیکه ویارئال و ناپولی با ضرایب نزدیک‌تر، رقابتی متعادل‌تر رو نشون می‌دهد. دیدار لانس و اسپورتینگ هم اختلاف ضرایب چندان زیاد ندارند و همین موضوع، این مسابقه رو به یکی از دیدارهای قابل‌توجه کنداکتور تبدیل خواهد کرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141380" target="_blank">📅 01:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141379" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
⭕️
هومن هدایتی مشاور حقوقی ورزشی:
⭕️
استقلال تخلف کرده و باید منتظر حکم سنگین باشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141378" target="_blank">📅 00:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
با توجه به مصدومیت حسین کنعانی و دانیال ایری، زوج خط دفاعی پرسپولیس برابر صنعت نفت آبادان، محمدمهدی زارع و حسین ابرقویی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141377" target="_blank">📅 00:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
آسانی که مصدوم بود و جای رزاقی نیا اومد تو زمین ...خود آسانی مصدوم شد و از بازی خارج شد
😎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141376" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=iJZjQ8jC-cQEkab-Vt4jK_0R0ISOtpLL9wxWmYjdlhRsBjSAag2IyjiEy5OpioqWoPBRqrlo8zriuaQhc1hDJ8jxvm94Olo6-LosqRDZPbrecUg8JkZ0EsW5_OO7mtJEs3UaVWqs-R2hkYbsw1ChWSpLHv5N4Q4YgJ81y8W5gyrjxo16gMNFurC36cWcUfY2Q_-hMagl1i1EC55HMm3IMizrB8K-Up3Yrirtfh2Jh4Lhg2HZT81HlZ4xEiCJkzyRS2-LzR-WXaVgL_1fQe5omImB46pWU1sQxfIgYxhQJfCsOjHEjctB9R9ifpzQf3IZ8jogx4Nr9Hi7BRSdcPvFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=iJZjQ8jC-cQEkab-Vt4jK_0R0ISOtpLL9wxWmYjdlhRsBjSAag2IyjiEy5OpioqWoPBRqrlo8zriuaQhc1hDJ8jxvm94Olo6-LosqRDZPbrecUg8JkZ0EsW5_OO7mtJEs3UaVWqs-R2hkYbsw1ChWSpLHv5N4Q4YgJ81y8W5gyrjxo16gMNFurC36cWcUfY2Q_-hMagl1i1EC55HMm3IMizrB8K-Up3Yrirtfh2Jh4Lhg2HZT81HlZ4xEiCJkzyRS2-LzR-WXaVgL_1fQe5omImB46pWU1sQxfIgYxhQJfCsOjHEjctB9R9ifpzQf3IZ8jogx4Nr9Hi7BRSdcPvFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
❌
پ.ن فقط 19 گل فاصله تا آمار عجیب و غریب 1000 گل مانده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141375" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141374">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141374" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8WOAt3giGga4rtepGJDUNLDPnsX4ikOYlOpSpsZtazdzVnU9wEKliqEDcRgd0WPYiYKeiqOgcrmE-sNqIfQVPgw5sboalWGjg_jDn4oef2tF5zmQY8D8y4LXALt1Mov-AeNkBilryXhFxTHSPKBcun9p-QZl-cFeDXfOlm5Rc62mtmYFwPiclit5QxCtFOAt5Gep1mJ6C3TqBI6xNoyHFepthWtTF8W3DTveUIO1WDkcOuANTttz8GHgdMP8iEhJ4UnWA4QsFAVWJ5zFtIZKKNKGKpIqZSKTyOc1Tw0yxyscimxnqx9jNmomKUWlO14Eqwan5_BE_Qg3uRFHNcsaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زوج خط حمله مقابل خیبر
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141373" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHjooA-c6FIO44qxDrXpzB5HUmXZODq0A_FdLcEeB81bSMb_VUFoiKjS6b-MECENgD3KZqYALomreoKZJaqscpKSfeTx6kDh6LvCUB0lKOt1GYe_wjU1i_66ma-cRzjgW4x7JULjl5_NOwOVREPpY-Vs0DHx6BIeDB1iC9tRf7QGfKg4G7bPvZH9cj8LVVQLXkmaP03AQuUTDfSj4AET0ar4Fe7Xaqap0l_B2Ztz5utLEYb88KG6vlLpZkwxt7AZJRyv1JnF8Ab0wxaa9WU6G_iUtF-6OqDhmmz2vZmB5fEjERzd4kFJc8Ici-_31Bxc4GTzPOXUQGxhhbF8Ivrdvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
احمد کونِ دروازه‌بانه الغرافه واقعا اسمش برازندشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141372" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141371" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
الغرافه گل مساوی و به موقع به کیسه زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141370" target="_blank">📅 23:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141369">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/141369" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141368" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7Qu1PSmmF72zm-csFvZIUErTyYEXTdAyE9fBBnvLX0p72UXdWjJIsSsNWMTp8uKXKG7NdwqcgQmbd_pO7_DvBBG4Z3LSB-vAu1CyYqaskowfXHAR33XdVeOZYrScWOnNyeQYAttN77-zjPPqSueqGhPBjvfnnFmtkZTmQovawtG_b8h5YgcZU3AZQHirxvp4cXQ4PcBrPRoXc4mEArgQFMOYhHD8OHEt3lfaKD50hsTvtPCnaW5CheAKUcA-eh3aP4XziUq1tRNSaydDEiTE_9k-tByS2uGO3F9ja1j7J7TRxDF-rpEmYikIq341oKgYYjSNbILCiofUhQXMeCDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پویا اسمی مقابل خیبر هم دقایقی بازی خواهد کرد/
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141367" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141366" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔵
💙
🔥
نماهای دیدنی از سوپرشوت یاسر‌آسانی روی گل اول کیسه به الغرافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141365" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
احتمالا بازی های تیم های بزرگ عربستانی هم مثل ایران به خاطر شرایط جنگی شرایط میزبانی و دیگه ندارع و تیم های عربی هم میزبانی خودش و باید به کشورهای ثالث ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141364" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141363">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
بازی کیسه و الغرافه هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141363" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141362" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=rfyR0iccsTl74FKuHt2cPUtJxiqQvLivx-oXLgpMQtZyohycIrC8UWM0gUGZpQIBgbw5KCozq2Rfyq4fJwwIXVummRFKdT6aSq4-1-Kp95VCW-QJyq_M0IUE5ZlQsmgv8adaSanY9MjAgZyPTp_6_IVvNi0Jq2pzdOAIngZZQVorVOtknGLLoLB2WisKCOwc7U0sMZkFGWNYCgGk1Oa3U7ldPqQs--U2s_3sFxuFVd9M1d02GSKMpTUg8mr2Z62JvSU1ukfptdlJu7VpjqUQ4shwYNFc5D5Y9O5HA_A7ZpGoYNI5QUidvr4TbzygCh-dHm97KMWaqK82g-zGGf9niA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=rfyR0iccsTl74FKuHt2cPUtJxiqQvLivx-oXLgpMQtZyohycIrC8UWM0gUGZpQIBgbw5KCozq2Rfyq4fJwwIXVummRFKdT6aSq4-1-Kp95VCW-QJyq_M0IUE5ZlQsmgv8adaSanY9MjAgZyPTp_6_IVvNi0Jq2pzdOAIngZZQVorVOtknGLLoLB2WisKCOwc7U0sMZkFGWNYCgGk1Oa3U7ldPqQs--U2s_3sFxuFVd9M1d02GSKMpTUg8mr2Z62JvSU1ukfptdlJu7VpjqUQ4shwYNFc5D5Y9O5HA_A7ZpGoYNI5QUidvr4TbzygCh-dHm97KMWaqK82g-zGGf9niA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141361" target="_blank">📅 22:21 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
