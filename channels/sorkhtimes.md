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
<img src="https://cdn4.telesco.pe/file/Bi6SIu6nPB16H2vm_GTZT6hUZReecImamRTslMnGpQAFZFBmGbneHaaL4ePfqUKG6wWMSzFCnFOxjaPssqcwnWFuRRkm0G4VF6_ZrC5j7hOjU0xtxHqgfa9SMIKXE42JsF0ojDjeJOzl-AfOOJNZCQFMenCRYGpWK9ikiZcuCsaMT2rFcVYWBrQ28caRLqsgRULZdF-Ra3kMfOh0kQ1uQ7fpAWbZ8E0-AX8vwEeVY2pIdF_XEy2Nl55UYG9iuTs_2zD_ZWcSFa2p63dQhYHDAzq7A0SmrufpSHqZcihCt0mN5wRokAiOeHTqI1e7gzs4tE2xkdgVf6uWhTXQMIJE0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-133734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
خبرگزاری فارس هم اعلام کرد:
🔴
مهدی تیکدری پرسپولیسی شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/133734" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/133733" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
خبرگزاری فارس هم اعلام کرد:
🔴
مهدی تیکدری پرسپولیسی شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/133732" target="_blank">📅 16:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133731">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مهدی لیموچی به پرسپولیس پیوست/ خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/133731" target="_blank">📅 16:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133730">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
با چهار بازی امشب و بامداد فردا دور اول بازی های تمام میشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/133730" target="_blank">📅 16:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/133729" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133728">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
دنیل گرا: در ایران احساس امنیت می‌کنم
🌟
شب جنگ جولیانو (مربی بدنساز پرسپولیس) به هتل محل اقامت من آمد و گفت که پرسپولیس قرار است فردا اعضای خارجی تیم را با اتوبوس به مرز ترکیه ببرد. روز بعد ما 15 ساعت در راه بودیم و پس از رسیدن به ترکیه از آنجا با هواپیما…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/133728" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe69dca3f5.mp4?token=V2puGI60wd3kF2xD3frUJ0-HWeBo0PbapEmLvo5meDgi9y4LpogZR7lB9xArH0fJSvEyFTJ0e4caNdJl3Lkb2H4a7OaLzYB1xbOHfxiyxtQPM0QHnDGUee3pM8-65L0Lwv8mRBnmGtqk-GzKR4EtIekQ3ypxYHjhUEgJhH73ZXtZuqDp6gHSx41mD3XeW7uj7kTskthWk103sVTl5CPHhVYTSlpLqbg7KEEQjaUaUV9l3hO2xGts61svrgk1mVyjhTPk_EI36dk3OeRcgfo-6YfGVy78IJIkpFNNF4p21TbxP-5LbNQK75Jg4VnE5jJZaBI4pJt8LO8Nchq2RnikOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe69dca3f5.mp4?token=V2puGI60wd3kF2xD3frUJ0-HWeBo0PbapEmLvo5meDgi9y4LpogZR7lB9xArH0fJSvEyFTJ0e4caNdJl3Lkb2H4a7OaLzYB1xbOHfxiyxtQPM0QHnDGUee3pM8-65L0Lwv8mRBnmGtqk-GzKR4EtIekQ3ypxYHjhUEgJhH73ZXtZuqDp6gHSx41mD3XeW7uj7kTskthWk103sVTl5CPHhVYTSlpLqbg7KEEQjaUaUV9l3hO2xGts61svrgk1mVyjhTPk_EI36dk3OeRcgfo-6YfGVy78IJIkpFNNF4p21TbxP-5LbNQK75Jg4VnE5jJZaBI4pJt8LO8Nchq2RnikOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دنیل گرا: در ایران احساس امنیت می‌کنم
🌟
شب جنگ جولیانو (مربی بدنساز پرسپولیس) به هتل محل اقامت من آمد و گفت که پرسپولیس قرار است فردا اعضای خارجی تیم را با اتوبوس به مرز ترکیه ببرد. روز بعد ما 15 ساعت در راه بودیم و پس از رسیدن به ترکیه از آنجا با هواپیما راهی مجارستان شدم.
🌟
با اولین پروازی که می‌توانستم به ایران بازگشتم و به چیزی فکر نکردم چون من چنین شخصیتی دارم که اگر خانواده‌ام به من نیاز داشته باشند، من همیشه کنارشان هستم و اینکه ببینم چطور می‌توانم کمک‌شان کنم.
🌟
هر جایی که بوده‌ام و در هر تیمی که بازی کرده‌ام، تیم خانواده دوم من بوده است و حالا پرسپولیس خانواده دوم من است، به همین خاطر تردیدی به خودم راه ندادم و بازگشتم و حالا تمام توان‌مان را برای آنها به نمایش خواهم گذاشت. من در ایران احساس امنیت می‌کنم، عاشق این کشور هستم و خوشحالم که به اینجا بازگشته‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/133727" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133726" target="_blank">📅 14:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
جلسه آخره اوسمار با باشگاه زیاد خوب نبوده و گویا یه سری اختلافات وجود داره
🔴
به گفته منابع نزدیک اگر اوسمار با باشگاه به توافق نرسه مربی بعدی تارتار و گزینه های ایرانی نیستن ، از مربیان خارجی هم اسکوچیچ دراولویت باشگاه قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/133725" target="_blank">📅 14:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
❤️
حسین خبیری، گزینه باشگاه برای مدیریت ورزشی باشگاه است تا جانشین محسن خلیلی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/133724" target="_blank">📅 14:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
جلسه اوسمار و حدادی پیرامون قرارداد و مباحث مالی سال دوم سرمربی فردا برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133723" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDAbPGxHLwWnSc-sap0YoFoWXbYpr6HsXBxkjNctaAI0eVgHlyWmuHB2pHOlGKIaBJ56Ybam8GgrCD8vorDsfMWdnv5yd7lYKWjxJmRzusJRG-nYRtVcAyxs6nasz9I-wpdRa3tGYGtbqcD6Ezck06Wf7BfKhNZD_9CgOWTfXCLswejyjH-cIngYgtiMbaRnkyIwAwEJxGbUguvnIjSsXCfI5ImGRUBl202mPXLTeaJiGdK2seyyVQtNiSwbphVg5i_74z6VeHe4JanCzATVPX63jfrEbA-j5xc0LJrXkvdQ2xsfyG5B_goJcEDeoPJYD_HJgtUhVSdOj3ruv2zMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه K جام‌جهانی ۲۰۲۶
[
پرتغال
🇵🇹
🆚
🇨🇩
کنگو
]
⏰
چهارشنبه ساعت ۲۰:۳۰
🏟
استادیوم ان‌آرجی
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/133722" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133721" target="_blank">📅 13:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
خداداد عزیزی : از طریق یکی از دوستان با پرسپولیس صحبت هایی شده، من اگه بسته بودم همینجا جلوی دوربین میگفتم بستم، هنوز قراردادی امضا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133720" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
❗️
خبرگزاری فوتبالی :
🔴
🔴
اوسمار به مدیران پرسپولیس اعلام کرده برای شرکت در تورنمنت سه جانبه به ایران برگشته و برای ادامه‌ی همکاری در فصل بعد باید فکر کنه و از خانواده‌اش مشورت بگیره.
🔴
🔴
باشگاه هم به خاطر این که فصل بعد در صورت نیومدن اوسمار به مشکل نخورن؛…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133719" target="_blank">📅 12:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
❤️
رسانه‌های بلژیک نوشتند که تیم ملی ایران بخاطر سفر از مکزیک به آمریکا، دچار خستگی شده و این بهترین فرصت برای آن‌ها است تا پیروز شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133718" target="_blank">📅 12:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
لوکاکو: بی صبرانه منتظر بازی با ایران هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133717" target="_blank">📅 12:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/133716" target="_blank">📅 11:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#شفاف_سازی
‼️
تارتار هم محصول مشترک پژمان راهبر و فرزاد حبیب الهی هست و در کل ریدم تو دهن هرچی مربیه داخلیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133715" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_iIS0QfdbaJmF3g8Ks54XW6DBYdNZBd30Ue2QiHqpag0EP_r9YhVVAyRRXTxpLXXWUhbkIRBYHWT-vcSPAkvs0hjlpdzgWBA_n03cbjDvzDorjDRJWK7p3jxwvi_mn1mdWJ872hLoSMjtReaDvdIdA3KfU6I0BKSdAvykFzgbfVnLKAxeLFH-Au54fVZwF8Nx61DaASonCmsDfKDjsnK_RtVxbJl4Q4OxsbJsblJGzIcdwtmRXyJN6ndgG4L-kdR4ezbJjdKzRDJPuuJ7gH0Gvt4hOX_MaB7LeLOzXuHZ-nhnlZs2-RvEtxnp-lzKAxqrzrQ5FHhKl_qMUD0n9Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اولین هت تریک جام جهانی 2026 توسط اسطوره لیونل مسی به ثمر رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133714" target="_blank">📅 10:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133713">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh7gEQyJS8vlZKcRr8nFuRv6UYuelTcxP_Fi7I9SgSksBm8YgJgKB0CAx9rGZNTj54-IOaHOSZLK7XUs9HWD7bobJXXL3W6O-NvsAzDx6-ceG8CUrJOCKj5lL-L6PAW1l7mg5d6-PzfkT6fg9qV-WGjK93A12-w30rL8NMtPv36-zggep0lBtYs6doP0DIUGRTJ8LMS1rBXU63MbbZAiX19-uZgW9pwbMp3EEd-A3rQZtwxoD7AvNpflBW-TjW9PziG2VfPGQYGvatuqPfpTIURrS3xopI1CsU9JvnMRzu_jNaktUM_c_9VIhfxW-_EcY6rzhMLE3WM3DBCmq57rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جدول گروه J در پایان هفته اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133713" target="_blank">📅 10:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133712">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
بانک شهر می‌خواد نقش اصلی رو تو اداره تیم و خرید و فروش بازیکنا داشته باشه، نه فقط حمایت مالی.
✍️
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133712" target="_blank">📅 09:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133711">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
گویا فقط ویزای مهدی ترابی باطل شده و شایع باطل شدن ویزای طارمی اشتباه رسانه فرانسوی بوده
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133711" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133710">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efadb3452c.mp4?token=ffhytqyssrblzF3IMJEfqvNCAewj3vjHme6qQEp5Jkq9xULLAL3AO3PafwMjDZ0CZrtY2NDkpKJhaMir3SVFaFrIvbfUKbPdmrugXKUokRgZu7HfeEL5X5hzxXhdL10yjDbpMmk0r7nEZzDRuCwTQ_6FEcdecfUdRjNy270kIG_IdWysI5v1QvluSAtLEWxrdQ_UV8k1YHeqsiS_VUr8q4-xNHItKEHnL77w2UsoCXy1p7zrId_hYbJWkPVB7tqTK37B_mz8esMKA5N-Iqe1yhe2i4zUWk27mfa0bqZuBuiPHTH5K_4q1O61QIZTGfwZRDiZjVFgzQolnmTponnEQnBdjVh7U3-4B_UJGG5unmaftxD4fWhDbX5eQSYIRmsn9BcM8goUmEzHp71uwTY4vmqILPh9u6uC-hvrfP-51hT2pA8KisgAFvWUdMPtn-hA2pQ2eiwaw7XWCXmB2CSzU0fJUoSKEWFZTssPS1dov7bAWnFHsJcrcye0lk6Iz2LVE-jzcqNUR2UT1gfYaISaERd-lG9xhnMC_R393j6nbT2UW7UfzRwPo5ElBWNCkPWL75qUGbiTD7ec2yT3lYwHwmbMMO-PQynWEntVJK9848tchdcUWjwhNp55U4gpPHeRhNaFjFFZPb0cNVlTgjNHlt-5Fh2w4CrTxjfxSpJrMv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efadb3452c.mp4?token=ffhytqyssrblzF3IMJEfqvNCAewj3vjHme6qQEp5Jkq9xULLAL3AO3PafwMjDZ0CZrtY2NDkpKJhaMir3SVFaFrIvbfUKbPdmrugXKUokRgZu7HfeEL5X5hzxXhdL10yjDbpMmk0r7nEZzDRuCwTQ_6FEcdecfUdRjNy270kIG_IdWysI5v1QvluSAtLEWxrdQ_UV8k1YHeqsiS_VUr8q4-xNHItKEHnL77w2UsoCXy1p7zrId_hYbJWkPVB7tqTK37B_mz8esMKA5N-Iqe1yhe2i4zUWk27mfa0bqZuBuiPHTH5K_4q1O61QIZTGfwZRDiZjVFgzQolnmTponnEQnBdjVh7U3-4B_UJGG5unmaftxD4fWhDbX5eQSYIRmsn9BcM8goUmEzHp71uwTY4vmqILPh9u6uC-hvrfP-51hT2pA8KisgAFvWUdMPtn-hA2pQ2eiwaw7XWCXmB2CSzU0fJUoSKEWFZTssPS1dov7bAWnFHsJcrcye0lk6Iz2LVE-jzcqNUR2UT1gfYaISaERd-lG9xhnMC_R393j6nbT2UW7UfzRwPo5ElBWNCkPWL75qUGbiTD7ec2yT3lYwHwmbMMO-PQynWEntVJK9848tchdcUWjwhNp55U4gpPHeRhNaFjFFZPb0cNVlTgjNHlt-5Fh2w4CrTxjfxSpJrMv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رختکن تیم ملی پیش از دیدار با نیوزیلند و صحبت های زیبا و انگیزشی علیرضا جهانبخش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133710" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133709">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CldN1Odu30b8xP8qz_mEv5FjcgAjf1IXttCQ0fbzXQUkTb2bzSV8g4UfrpdC002cDoTEoTwY4Ii55LHIfsaDdkE3-nek9L9e_stOpwUDpC_ViyDpx5uCSLHbuNUQ1e-daQf3Mn0RqDnW3SDWAZKlpj1uHMcl1XbrAdWfDyylUdwsyTsBHzCDjuPYimeE_xWtXpQYd1p72EJIm5MV0g8mYWnT-erjkWWkS2Ajo_2BA9WJLCfpacDoM5xMaJwvpMRsqxDaagfXP9s580VSOYeytYfBhJ67IfPyCxeLMQ_XlHdRj8wxtgcFmlbRPnAiO8yLZMmbZ0CubHsXGhqx8mhdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه J جام‌جهانی ۲۰۲۶
[
آرژانتین
🇦🇷
🆚
🇩🇿
الجزایر
]
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
استادیوم اروهد
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
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133709" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133708">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
#فوری
| سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد
🔻
سنای آمریکا روز سه‌شنبه با اختلافی اندک، طرحی درباره محدودکردن اختیارات جنگی «دونالد ترامپ» را در قبال ایران رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133708" target="_blank">📅 01:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133707">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLUCQNzzK-xtIvzHIoyxOU0RdJmqatRLtrz6V2g4jE3eClSXYyUAXMrYHrzbMQAz2JPcC7dUyDFqPnhKtTIn7CAh33Ube2IGoUmuQUrQT3avT14wagLNqqdO-1lhvbAhAHajBrszw0C0OJb_c11eHPYgT4eQHSKixCCqBTyG2xAwCJHjWqN9QOprurr4tRa5PIS3UeNnRc1HT0dxPyUyIuA5cQSQmzhLdoXTt0yD7aweIA1pqK5pbfmfrAM-yzcwGCxOqNyQ4Cklwl-Eh72Ey4uNdJ91ojiYpQUKWXYA6QoVMHY69wwUhRKO9WADDzGD_g3B-y2_z0C37P2r2ZO_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
پست اینستاگرامی اکبر عبدی با عکسی در کنار علی دایی در بیمارستان
🔴
علی دایی، اسطوره فوتبال ایران، با اکبر عبدی، بازیگر سینما و تلویزیون که در هفته‌های گذشته دچار حمله قلبی شده بود، دیدار کرده و جویای حال او شد.
🔴
اکبر عبدی با انتشار این تصویر در اینستاگرام، از علی دایی بابت پیگیری احوال خود، قدردانی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133707" target="_blank">📅 01:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=jwo28gfftulsYRLzfW7d_CgAJ88YZuWD2rJc-HcvAriFIL7MYSbzSAD7Du66t5AlSVVCWNW0rA7PBjHlKMRy3aW69fyAZuVgdHycPtdjBek_go_Udl6xwvBSqPIY_DHcsGDKhCbctnVJ7B6QKm7aKOCjzg0qIZVf15G9jRbLM8IyVYlzEskJhry8tzLsrzkb3ASZXGGRtKc5xOYM4wTL1yl3wC01UlhYncxspqbgfNGSU7Uy8TKJ712HH4uZr2PZbJkvvW2hmU3ifk7xQkOeDHafyJmSsCzhgGGZ6cFlLrs7ptq8xIEELKliUO4pNKOJinNUCJ4Ocev-Z_bxjNo0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=jwo28gfftulsYRLzfW7d_CgAJ88YZuWD2rJc-HcvAriFIL7MYSbzSAD7Du66t5AlSVVCWNW0rA7PBjHlKMRy3aW69fyAZuVgdHycPtdjBek_go_Udl6xwvBSqPIY_DHcsGDKhCbctnVJ7B6QKm7aKOCjzg0qIZVf15G9jRbLM8IyVYlzEskJhry8tzLsrzkb3ASZXGGRtKc5xOYM4wTL1yl3wC01UlhYncxspqbgfNGSU7Uy8TKJ712HH4uZr2PZbJkvvW2hmU3ifk7xQkOeDHafyJmSsCzhgGGZ6cFlLrs7ptq8xIEELKliUO4pNKOJinNUCJ4Ocev-Z_bxjNo0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133706" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133705" target="_blank">📅 00:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT16Qa_dl6E00CN3b5Oo0d6yhNwTT-PGaNbz98KlcuwSXYcTHEvVTfQXiiCLQXJkIy8oqYX1mwRe22TLchtFBraV7w0ZDjCJ4WbMkemMoMhFT9jo1H4HF_MWVrcH5yA2Wz1Sp4jgCv31gKIK1y-dX1WdW2n_fqzNaLAdzwEMuWLgIQWJoulmke1M-DU3LyMxLL8i49IPPWZ7-CxU4ut2ik_ofTrPqEHPD_Fy8qYYWjaoQ9zVQNz6OduJaXO9O2o9PIGmArNPOLqyZV5uCl1sO9Qmp851fqyL2MY4IZEWpGHSray0p5QAfSUdBPfFM-MwPHQGBL2hOuqmtvqplizdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سیدجلال: اوسمار پیشنهاد داد برگردم
❗️
صحبت‌هایی در این زمینه انجام شده و آقای اوسمار هم پیشنهاد هایی داده‌اند اما تصمیم‌ گیرنده نهایی من نیستم. این موضوع به نظر مدیران باشگاه و افرادی که درباره مسائل فنی تصمیم می‌گیرند بستگی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133704" target="_blank">📅 00:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=MmgBAMCu8dqbtaXDqZnQ_XC5wEAdI79fm0sRbJoL6gAWX4pRizih0l3-x9OluekFa_dhbNjQi5dgiF1uqkUCLHwTaMvv6QbJ1Wfm3Da_Zt6AaId_cl9jMDcHDjZBv7RFJVvVDGCSm9ZnIBFVxlLyjfZPQtTrjg9Qt46MegZLmyRbc-_q5PmcFU7RMkDH2DVFdNvsHdNxsg4Ev6DVsTyyvMcOWnlPkp562oSP4EW54g0jnzFjbQ4oyI3rCMOLn3TqepI25I4KEDvTQnevsHrqheoyncBm0p3G5jgqHnaOv0X1VtLf3sjQZ-nSJpP_jeTv_zqBq0clvN_4XO7y6Axoww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=MmgBAMCu8dqbtaXDqZnQ_XC5wEAdI79fm0sRbJoL6gAWX4pRizih0l3-x9OluekFa_dhbNjQi5dgiF1uqkUCLHwTaMvv6QbJ1Wfm3Da_Zt6AaId_cl9jMDcHDjZBv7RFJVvVDGCSm9ZnIBFVxlLyjfZPQtTrjg9Qt46MegZLmyRbc-_q5PmcFU7RMkDH2DVFdNvsHdNxsg4Ev6DVsTyyvMcOWnlPkp562oSP4EW54g0jnzFjbQ4oyI3rCMOLn3TqepI25I4KEDvTQnevsHrqheoyncBm0p3G5jgqHnaOv0X1VtLf3sjQZ-nSJpP_jeTv_zqBq0clvN_4XO7y6Axoww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
‏پیروز قربانی سرمربی فجر: با
بچه‌های شیراز نیوزلند رو میبردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133703" target="_blank">📅 23:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133702">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/133702" target="_blank">📅 23:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSHYIo7WR34VMvkcuLN9v45ARzwjVt99yQoedDoTLH7YLMNtQpvY3QiGk_3aDH0qbPwfJ5wGwSqz8lBfTY38CfrqvimOlPFT9QwxkCuzf4_lqDOIkdPE3zf_dB7WP5idV6AM41YEz2OOVnhoG_Flzejyer_ekdu7XUqoMa8dpyeU8C9ZDOo3_baDN9U_Ss34xIGXl9OCL_UxXMwjd1_TxFJnao8uPrSg9dZzEOq1S9ygKLT1ER3ndEqmkV1oj69UFnzYPN3X_nlxB7HzI4YogIHsFCud2t6Qtyx82XOnO-eMXJmYuH77F5ycu4fzh5SM_VFyD2yHH-Xd4BkgniUANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در بین ملی پوشان: میخواهم تا چهل سالگی دربالاترین‌سطح خودم فوتبال بازی کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/133701" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/133700" target="_blank">📅 22:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133699" target="_blank">📅 22:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uS7_Qn5PCC2rp5qm02j8mZo1IIeaJ2GHCRh0ZMd5MAO0Ds_CqxBtXTpZ4DStn4j-wGAKNUG5kOrXVdYVBlkmiyUVwdGpiiyurtyLKCTU-XE5Som8rCT22qHmNb55CDO5qMToNkvkV9EiXOPTI2vampsQiKbG42Nyqi4ayoRwU4yL9SDTMBu6eoEmCvNcCp_dmcT0Oi7fp2-Pa9UGRqDOmeo69cvMB7rkxF47SkJXntML9eUZahWlcBN-VryWzLgIBb916pAbFzkJy276OEF6HrMAOZXBfpZC_a6NCbv5R-nuShTGdN5HGM43A-E4LhsSwcOCAxt_q2tDKTlP8vXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/133698" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133697" target="_blank">📅 21:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaEbwEMV0rUDlPmYMjGGBYjbQdvhNtXluLJW2yCfFetO4SUScjPswyu3v33xr67qE4Hhan5HQjDEeqPaST0WqA-eEwM1j9JfBaqDO-J5aasV-xzAH9MNqFAynjw5T61SSfUylSkJctw_cuvR8i1AhHdee4nEeEwzD9g8AG0-H4pLokuB8_a-fnDbI_Bus6XD3LARR_cGR1zeWek0JwbVG5frRyFh7cFfsEk26_z2kaBjp3BdEFrfKoDBFmditV9Ak4UamglQT5A9anGSz-FJ1qwr-0iIFIcK8aRDHXfgF58x0n57DzELcOAyOZPRqZT8eIn8TPmClpB0QOwJF1BEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133696" target="_blank">📅 21:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133695" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCRHPikJNqn-vuMplOBZ-NJwlI6576nxdchQUKnivZuXBfDt1Xmya2Lu8hO9iAt93FkCJg64HyePD7wOlsfcuoEKIivXxr8rv-8Q5EldRQO1ozqJFYKS_K8fwOoY35A5hl3IiKeZbWB2oX0yLyq1XYn5Uz3p9WkpT4Jh4i94biZFLex9dJ3UmTf6ejtWvwldx8j8tJgGleC-6y0hpOWINKn_p3thYUktpa3oX3tShf5_T8x8xNAjKecyBHzcM01Z2bfPeJXSvyG8_SX8dOhUGSXLFwGp-HcVJzVgP9BZE86YhYnIUGjKFQ8OCI5BRff53vBDaBSQKCA6JTDDEaiiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🔵
FRANCE -
⚪️
SENEGAL
⚫️
جام‌جهانی گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
استادیوم مت‌لایف
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133694" target="_blank">📅 21:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
مهدی تیکدری نژاد مدافع راست گل گهر سیرجان با عقد قراردادی سه ساله به پرسپولیس پیوست/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133693" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133692" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⁉️
⁉️
حضور عزیزی در پرسپولیس قطعی است؛ آغاز فعالیت‌های سرپرست جدید در امور نقل‌وانتقالاتی
🕯
حضور خداداد عزیزی در پرسپولیس قطعی شده است و حتی او پیگیر برخی امورات مربوط به تیم و نقل و انتقالات نیز است.
📊
📊
عزیزی خانه خود در تهران را حدود ۱۰ روز پیش در جلسه که…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/133691" target="_blank">📅 20:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6WRjo3-D1-x8te4hxeAAgiLhiWteQJ4DJdHSXuwzj-IH6-Ei_RAa_r0K_uVRrbl8RRZZBXzFFgitqA-6xK8h4XIgYyX20dwYrF7ClbeIXVCQbEY1QScX8lv1OGyLvDYYY5TK07DWPqBt1ivxTfpbwgWhUAqUwPrejhiig33-GIuv-jDC4xQmK3vUUZkcu24E8aIBzu7qbTMrqKMAWNoQRL07CHDQocn0YCfb8lqRamHogvS5Azd4zH9Ugf-lpD21cPhwhWAOVeFBzlyG88tCqaHIpmsR2FhX1trAPOj22pazqA2QjfOdwr4whyXJGN1L7FzPmg-j7YzxeimDSFL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
:
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133690" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133689" target="_blank">📅 20:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90353b1248.mp4?token=K_5DfZYTbN1pxYDnAup5iAv9Y5dohn8sDRZn2GnJgDI5jH4hvAgnaPHRBEzt5aC0hsy_RgRi9FppLZmKA1KVt0OAGk5QUs5TGnujZ1hTWfkRCRqx31m6Dw__f-2kzrQCs2Hb1V0sUEjJVGa-LFbpsor33KlozlgV55FzGHI_NnNr30pDZ4xVG5fVl7aH-pnqWzggAuWa2M8RIQk60dTnFMTZ7zJyCqzogeu0vbInBl3Sq1n73FlctEPR3aFKLDXnySYtSyBI7d7gAsvmxHqxN5QWhDeiQF4weYTGRXfk6YFmQ0vK432aNhN5xGfo4PBaLZiwDJ8AqQeLlG-C6rukMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90353b1248.mp4?token=K_5DfZYTbN1pxYDnAup5iAv9Y5dohn8sDRZn2GnJgDI5jH4hvAgnaPHRBEzt5aC0hsy_RgRi9FppLZmKA1KVt0OAGk5QUs5TGnujZ1hTWfkRCRqx31m6Dw__f-2kzrQCs2Hb1V0sUEjJVGa-LFbpsor33KlozlgV55FzGHI_NnNr30pDZ4xVG5fVl7aH-pnqWzggAuWa2M8RIQk60dTnFMTZ7zJyCqzogeu0vbInBl3Sq1n73FlctEPR3aFKLDXnySYtSyBI7d7gAsvmxHqxN5QWhDeiQF4weYTGRXfk6YFmQ0vK432aNhN5xGfo4PBaLZiwDJ8AqQeLlG-C6rukMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرمربی پرسپولیس: خوشحالم که دوباره به ایران برگشتم. منتظر تصمیم فدراسیون برای برگزاری بازی‌ها هستیم. آماده‌ایم به هدف هوادارها در رسیدن به آسیا برسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133688" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56204fee3b.mp4?token=JL2W2BceqDD3zxGBzaIOB_ky_jVzZmfG9tual5ESo_HVyA7T-GP36mTEW83_GuLlbQ6sJUz3b03RKn7viE1kcCdDwG6y0j4gCRyXWaPRV57MKHY0qC4Fn9XX8lXmyh7CE6YAOUP2BZXesdeHOR-o6JRmxd4lz-C0o1q9dqEhqSK4SVsFAcwMw91qoZv4jqKb07GsNOnsU44LTU1y0JyhYF-kB7DK7wo00nkvwnqfNp_GXljVLare6kU9Ul-C1atZi9TIEh_jKL_mTD56AePAZNsenu_Vp5usEBo5U0kCsSrakNTP5x0F-wtJ88xreQR5lw54iR0JTRxeysKWO5XHP3h7NEtVgjNnju04IQazZxHmWGH0VfK9kntgP6CgFpHbx0YTdqtMP2BBx3vsnDySgDJPpsr3B6VK8ZvLAENZRiU0k4osU0GDKw7N2TzNYBppSACMMebORef7n6SewK0rFH7GZFsaHWRhHH2F-bqpyGYe98faIKEZu1hFudfye2IejQ9UJhHfOcLr1wWP5iL5t3dL60MdCOF6IIDF4eQXC1cqqZ97OGZ10J8y4HaiLuYeJ0tf20aO_8kZaM-5lypLMyukZr75E0AhG59fK-u3KN_8G7B8hP_rAniHhlVQj-VSae_EYbFu1H38CbT1TNcbijvGy83foY1kj98uWhlRrOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56204fee3b.mp4?token=JL2W2BceqDD3zxGBzaIOB_ky_jVzZmfG9tual5ESo_HVyA7T-GP36mTEW83_GuLlbQ6sJUz3b03RKn7viE1kcCdDwG6y0j4gCRyXWaPRV57MKHY0qC4Fn9XX8lXmyh7CE6YAOUP2BZXesdeHOR-o6JRmxd4lz-C0o1q9dqEhqSK4SVsFAcwMw91qoZv4jqKb07GsNOnsU44LTU1y0JyhYF-kB7DK7wo00nkvwnqfNp_GXljVLare6kU9Ul-C1atZi9TIEh_jKL_mTD56AePAZNsenu_Vp5usEBo5U0kCsSrakNTP5x0F-wtJ88xreQR5lw54iR0JTRxeysKWO5XHP3h7NEtVgjNnju04IQazZxHmWGH0VfK9kntgP6CgFpHbx0YTdqtMP2BBx3vsnDySgDJPpsr3B6VK8ZvLAENZRiU0k4osU0GDKw7N2TzNYBppSACMMebORef7n6SewK0rFH7GZFsaHWRhHH2F-bqpyGYe98faIKEZu1hFudfye2IejQ9UJhHfOcLr1wWP5iL5t3dL60MdCOF6IIDF4eQXC1cqqZ97OGZ10J8y4HaiLuYeJ0tf20aO_8kZaM-5lypLMyukZr75E0AhG59fK-u3KN_8G7B8hP_rAniHhlVQj-VSae_EYbFu1H38CbT1TNcbijvGy83foY1kj98uWhlRrOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: اگر تصمیم گرفته شود که بازی‌ها برگزار شود ما آماده هستیم/ اول باید تکلیف کادر فنی مشخص شود بعد سراغ لیست بازیکنانم خواهیم رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133687" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: بازی‌های لیگ می توانست برگزار شود/ تیم ملی ایران نیمه دوم بازی خوبی مقابل نیوزیلند انجام داد
🚨
بازی‌های بعدی تیم ملی می تواند عملکرد خوبی داشته باشد
🚨
بازیکنان خارجی تیم همراه ما هستند/ سروش رفیعی؟ تصمیم شخصی خودش بوده است که هراه تیم نباشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/133686" target="_blank">📅 19:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b067e8b9.mp4?token=M3SompUEMWCKSagb8JrQMIAtIFHoTMSQ3MX38tYn-uXGi12S2I3cevaCHYbc09WNqng7Oor3hkbqIwJeNRx1dunAMhVD42TKK-jECO0M_v_xKbQ0yqTs0HHGieKiu00BPUkcA2JmQnkJDWLoItbcVLSKNhmCpa2qRA7eUe8Lh4sZVURfkFvNmQ7VjmS12-cacTrgoDJxVQ4kWeftQEa3VP937Mi0nJpUxIJcBmcGP0ffrEi1shrAUDWNKJcv-ZkocXjkw2pnUdSnYfCGMq78LEave6j-rfZ8OF_Lts8hFfaxkyr-XqUK132lVJAe-g9jRX2pQ5jZAAbDo36cgrxJzGguNyQVG9kjF8Jm-y3flTQYX3uPWdaP4Abfhgr7S3ak2GuaXIdRAK4HU2fhK405asl2cmxChgswrD2lPhjUaYc-9dCssQGM3vCRziAeUJm19rBlb1xgJKgaWkMptM8fvSrOrTPJ8naxXSzg_J3kNCBa9y2A1L4TRI7V5I6bXqQW1fhjrBhNotzxuO403DjBvDgJYzQ_ZDsDkNF3r-ee8uskWphwJYV_g6P2QHnO4ihawuegXJ-7nhIKrh4kaf_olzLkCYzrvYqSYWFf016BeSXAOgcBVeG59BrMxUjFG7ujENYOj2nPpV4jHHsqqEWog8v9pIkGPBbJej16Q3mQw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b067e8b9.mp4?token=M3SompUEMWCKSagb8JrQMIAtIFHoTMSQ3MX38tYn-uXGi12S2I3cevaCHYbc09WNqng7Oor3hkbqIwJeNRx1dunAMhVD42TKK-jECO0M_v_xKbQ0yqTs0HHGieKiu00BPUkcA2JmQnkJDWLoItbcVLSKNhmCpa2qRA7eUe8Lh4sZVURfkFvNmQ7VjmS12-cacTrgoDJxVQ4kWeftQEa3VP937Mi0nJpUxIJcBmcGP0ffrEi1shrAUDWNKJcv-ZkocXjkw2pnUdSnYfCGMq78LEave6j-rfZ8OF_Lts8hFfaxkyr-XqUK132lVJAe-g9jRX2pQ5jZAAbDo36cgrxJzGguNyQVG9kjF8Jm-y3flTQYX3uPWdaP4Abfhgr7S3ak2GuaXIdRAK4HU2fhK405asl2cmxChgswrD2lPhjUaYc-9dCssQGM3vCRziAeUJm19rBlb1xgJKgaWkMptM8fvSrOrTPJ8naxXSzg_J3kNCBa9y2A1L4TRI7V5I6bXqQW1fhjrBhNotzxuO403DjBvDgJYzQ_ZDsDkNF3r-ee8uskWphwJYV_g6P2QHnO4ihawuegXJ-7nhIKrh4kaf_olzLkCYzrvYqSYWFf016BeSXAOgcBVeG59BrMxUjFG7ujENYOj2nPpV4jHHsqqEWog8v9pIkGPBbJej16Q3mQw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات خارجی پرسپولیس در تمرین امروز حضور داشتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133685" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00ec62d09.mp4?token=NrejpX2R5OM69GKmjDO5ml3ueae93mmZTrJMVGKe1pBuubEdWbv2W7-k3e9sBk32Gmp6u7sNTSgR0-schV-cTMW750B4Am5B3HF9F2QweAR-gSgvIO-XYdzi9I4N1TiXL2kwbjAfsIsCAASDyRhr7gLJaVry2Rb-AsdX_VXMwm5BleET3wT0DUkAtXuE5MYn-Orw2dtQtgXo8j9rZ5uwGprrwj4RzuIOkTLCbloV5Kvy2eYXHbNv30jMqnyoeJrAy-wonJKM4XYHdlx1OA5J0gN0kDwIZQ5FO7yi4s_kEd7sogoRsBWE6XhnvqEvI8IdZcMTTIlFGs_7bIl_rAcCag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00ec62d09.mp4?token=NrejpX2R5OM69GKmjDO5ml3ueae93mmZTrJMVGKe1pBuubEdWbv2W7-k3e9sBk32Gmp6u7sNTSgR0-schV-cTMW750B4Am5B3HF9F2QweAR-gSgvIO-XYdzi9I4N1TiXL2kwbjAfsIsCAASDyRhr7gLJaVry2Rb-AsdX_VXMwm5BleET3wT0DUkAtXuE5MYn-Orw2dtQtgXo8j9rZ5uwGprrwj4RzuIOkTLCbloV5Kvy2eYXHbNv30jMqnyoeJrAy-wonJKM4XYHdlx1OA5J0gN0kDwIZQ5FO7yi4s_kEd7sogoRsBWE6XhnvqEvI8IdZcMTTIlFGs_7bIl_rAcCag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: تا وقتی این فصل تمام نشود لیستی اعلام نخواهد شد/ یاسین سلمانی؟  خودش فهمیده است که اشتباهاتی داشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133684" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
❗️
اوسمار:فدراسیون می توانست بازی های لیگ را برگزار کند.مدلهای دیگری هم برای انتخاب تیم ها برای آسیا بود
💬
به خاطر فشارهای غیر فوتبالی روی تیم تاثیر گذاشته بود اما در بازی های بعدی جبران می کنند
💬
وضعیت سروش رفیعی و تمرین امیری در کنار پرسپولیس؟ در مدتی…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133683" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133682" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be8a9600b.mp4?token=sVqtdMRBBpo9Ht4QyeaNBx0wjfzgYXdRqvT6ulXTxAaB_fZDnCUYIyrukz105l4DfuDcJ1hngVJpvOMR6nAeWpp4EAo6gcKbvgsFOScrIawXL9YkL0VPAOXkEAwdh_IjjjiJDjA_s5jF335RJIj58Ezff39H6Vd_APn9HegyxqxaND9dIuuS4t_GTT5S6xvgtxyKqn1gVkQOFXMEXAN3XV_ILJmPsvYnM3EpfDLIx_z4J8ycwkMx7g98kqJXlKyrG16-AGo5x1GZegX0guxeTJzTwRmTqze5uQ1KIC_0c5KgEHCAqlU-Kvs5H0_5AT_8jA3a8vI_oB9QZD_hEMht_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be8a9600b.mp4?token=sVqtdMRBBpo9Ht4QyeaNBx0wjfzgYXdRqvT6ulXTxAaB_fZDnCUYIyrukz105l4DfuDcJ1hngVJpvOMR6nAeWpp4EAo6gcKbvgsFOScrIawXL9YkL0VPAOXkEAwdh_IjjjiJDjA_s5jF335RJIj58Ezff39H6Vd_APn9HegyxqxaND9dIuuS4t_GTT5S6xvgtxyKqn1gVkQOFXMEXAN3XV_ILJmPsvYnM3EpfDLIx_z4J8ycwkMx7g98kqJXlKyrG16-AGo5x1GZegX0guxeTJzTwRmTqze5uQ1KIC_0c5KgEHCAqlU-Kvs5H0_5AT_8jA3a8vI_oB9QZD_hEMht_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133681" target="_blank">📅 19:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
ترامپ: متن تفاهم‌نامه را نه تنها منتشر می‌کنم، بلکه احتمالاً یک نشست خبری برگزار می‌کنم و آن را کلمه‌به‌کلمه می‌خوانم تا رسانه‌ها آن را به‌درستی پوشش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133680" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1srkvDRTSB6HZRoEE1LGi1QwfENAy7g8vyY_pJSgaHeoqbjrEvShcq-BnOR58i95P0YUTP9B1Ci-5XQfo5h2cKDqSh7yQDtX-JFa_XdCmfr_hxgjiQhap_nvppU9LVaCQU0FGs4NnB43LFtDNFzF5rkGC_AKDCtcJJ9lwE8P5sGgzEuE4aiTaab6HssBjcNAcl1rCRoPadC0UEBFQuo31xFaEJDiQIJ0LsmQBnO48N_KUidZMmfUpsbe41IxACSHGjqdDqnrzt1uZxUnEzJ3-1PaeGjyMTglq8j2Ko6Ua19ozh9h0vbQEdhsLoPumvfrR_TtNWALHh2TBjoCySrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
مثل اینکه قراره جمعه توافق اولیه تو همچین جایی امضا بشه
🇮🇷
❤️
روستای بورگنستوگ تو مرکز سوئیس که تا حالا میزبان کنفرانس‌های صلح زیادی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133679" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123eaa1e7a.mp4?token=vSppA_BGkvllYMXwm6vCZbayNoyVcnpWHjV0H0jIoz3WR_Nd4Mz0hGzq2sJKE6ozfM-KO-16t1QKfmJkRaP9W_vGer26fPSFPD5SzQtODYpY-G1jSJm8HtjqG12nfbzQhj4vZzzjjxa_umsNo7LM_ZUdMYiSmdy0vkRlYcEreZq7eNn2mzV8LA05ArQpunBNkxmPVTJ5DtZfIaAAhtsYcoIPp1VYwceBc63BbF7NX4NiDYUHZL3tZa8JjCMhb0o_Oxr5Q6AjBj3tsRCYU0TiE-02_8Hr240cIeR5PsEchpDikynfqybT1xkYNgI6mii4o_Q0M88wadCWe2KCwefjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123eaa1e7a.mp4?token=vSppA_BGkvllYMXwm6vCZbayNoyVcnpWHjV0H0jIoz3WR_Nd4Mz0hGzq2sJKE6ozfM-KO-16t1QKfmJkRaP9W_vGer26fPSFPD5SzQtODYpY-G1jSJm8HtjqG12nfbzQhj4vZzzjjxa_umsNo7LM_ZUdMYiSmdy0vkRlYcEreZq7eNn2mzV8LA05ArQpunBNkxmPVTJ5DtZfIaAAhtsYcoIPp1VYwceBc63BbF7NX4NiDYUHZL3tZa8JjCMhb0o_Oxr5Q6AjBj3tsRCYU0TiE-02_8Hr240cIeR5PsEchpDikynfqybT1xkYNgI6mii4o_Q0M88wadCWe2KCwefjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظاتی از تمرین امروز پرسپولیس باحضور کریم باقری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133678" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
ترامپ: چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
❗️
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
❗️
ترامپ: ایران طبق توافق هسته‌ای به سلاح هسته‌ای دست نخواهد یافت
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133677" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
❗️
خبر پیشنهاد به اسکوچیج دارد فراگیر و جدی می شود.
🔴
تکلیف کادر فنی را مشخص کنید بعد بازیکن بگیرید.اینکه فلانی خیلی خوبه و همه مربیان او را می خواهند استدلال زیبایی نیست.دو فصل اخیر هم با همین فرمول تیم بسته شد و یک سوم خریدها هم با نظر گاریدو و هاشمیان…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133676" target="_blank">📅 16:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/133675" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133673" target="_blank">📅 16:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/133672" target="_blank">📅 15:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/133671" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133670" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQAcEONx8-2gq9aq2OkiyeeNJIwfwmyPsN1uuD_2Ppqep8O24ZFT2u-ewZ3rTSc8W3NEHQleHKXn1sn9GsjAVux_N2WAnY-ST_dfT2AGU3LuAuqt1LdCI3ZOurZvVbLtcIsPhs5Od8X5eoM4rGaYnq7DEyGfJHuR3R6dn4wXCbKhXM1Vbcxq5dRNJvVHaA8O-8jOEWQ7X1wotmWvDJ5vJ6hBCkBAcPi8SzvF6CCvF2v2NjLFtVrjr7x5uGjJrl1fvHs_Ns1AzUY8avt3vWSDAfAQarWh-RX8a4NLv5nYrjEWa8gE_UO77wqevxo8cr30mRIFCyayKN-cpfbXofwAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133669" target="_blank">📅 14:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8JO71JxiirImbEXV52Y_fgcHM_FwF_d2s1fKsnu5d4f3olrYZoqbWMTgZvwDHRun0bbqs8eFs7yxSSX0AF41T5TN4ZWaxAEd1qX3ESG3TUyImPvi4F9msHS6znPZRlIRyFFHYoQy6nMOsCjZpydne9C8wFiyB5Ls-NVgRJmsHooDTzUkDUWLtO4vhKggKZVP9oLnyqd5s1DaXH2NGVT4kwL8N4HCxX1ioHq9xm0riEafPuHBbjraBUot1moO8_vQlMy0-dVFeljiwgNhXs3P4Z8jgmBVSfdFn1DifXh2VObhYQyCvh29YR3Oqm6zYrC6wpy7-mAA4Z45WMPAcWxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قلعه‌نویی همینو قاب می‌کنه میزنه دیوار منزل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133668" target="_blank">📅 14:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133667" target="_blank">📅 14:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IE_fUss-h_zHvPRrM5bIFuA1zTsmlI49aiGZUwmWpziDaVFHxk3hrgP9h3MMRaQgpdomtixbJ3Xw_65Zb5XWhUJ2nIrIwfEE9zG5QtTQ5MHW42oMwwdb5Wuxn1a7aV1grP3ZMuwtI5-zTDuJi8j3xA3J3D94YKvYKNjtfyC-h1lqV5AtsBw5fv7vwrdOodJXnO29mK7LQ8Wfdo6ZCiSdl6qFUXGAy70x-8mDzyQvHA_nLPlLt8X4Z2eEsWReFoCxYNOwhH1wJQUPRdNwPwahxPp6IhbAv0MtYkles58Cv23_WhzmMwlZBPEsFm9GBfb_99VM2AC0eTpZ--K2K82dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/133666" target="_blank">📅 14:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
فرهیختگان: لیست خرید پرسپولیس شامل طاهری، یوسفی، لیموچی، زارع، محبی، نوراللهی، مغانلو، ایری و اون یکی محبی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133665" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5B2qpzSEjsyr3PEKKamIoxOg8D82P32-FME8sYDXO71Yz2HadATEZ4uV_NQtwXqV6ufrLUZmXutJlUYB5qUEgbzh8-iHgwtYpkOXzAG_ymwb1QPY7hQ7l4Q6kHybCTYIPdTjBvinIjj1k_oh1DFGE1ZouStXJCBcydFVRqkjToL0QNaMByyEuB-fZF8gMUXFljA93_5pbtK6PzbPwENEgaL3OOmFOcie-DWda_21xtjpKGpvs7pq0fIbJnFhC5VwfCJosTTzrVIBUQ_KdBNKZL4pe0nWZHTJsmPlwwEXVVZRf6TJebPkTdtaGGJF2x0njEeMTMMObrOXO-V3VDlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🫪
برگ ریزون
😳
🔽
دروازه بان کیپ ورد که جلوی اسپانیا کلین شیت کرد توی کمتر از ۱۲ ساعت فالوراش از ۵۰ کا شد ۶ میلیون
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133664" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
یکی از نزدیکان احمد نور به ما گفت؛ احمد تو ایران فقط و فقط لباس پرسپولیس رو بر تن می کنه
🔴
همه ما زیاد از این حرف ها شنیدیم اما تو این مورد، مادامی که پرسپولیس خواهان احمد نور باشه، این هافبک تو ایران انتخاب اول و آخرش مشخص است.///طاهرخانی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133663" target="_blank">📅 14:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
ترامپ: من به تغییر رژیم اعتقاد ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133662" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/133661" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133660">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ: من علاقه ای به تغییر رژیم در ایران نداشته و ندارم. تحریم های ایران طبق توافق برداشته می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133660" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133659">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e24DB2j8U0PaLvLhEpSfe8C71fSEJzObecvafYttDrsoyCksS-Qa2RLSy0sR_vQhFHWUOIHrXW2sX041NvDNAHg3Qszk3aXIjwH8PHAl8B7n_WQew9qhg-NShlSrY4k_2VuIvvkKco9bUgZd_S27cmqNouJeOWyCra780Ms6RbDYHL5okCqtuYnNihscRqHeApS77qimqGim7Q_QbPMkY75GC65feoKuEo4PfJO1zIvLarasJtafqmKdTmXZAgswLoI8yKRKVEji1TpqAAd-Dya-2xOnm6jmBruWo26fBwVfMxYZLiDVPckXPBguzYKiprT5Hj1wN--_uCarPcHV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت انجام میدی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133659" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402b94c148.mp4?token=hQ3lntTnx75ojnofm2fw2TRgrEjAjzcftBnBqytzYgDv2U1N2_F5EGc18iicgCyYEVBy8P0dKSNASoguF_Vh5pfbxi2UgpgS-uZbXDGrgvjXeu9wbtpAlN0DWvAU90umN81WtmhDQDhGWGfVwqdnuwDF3mwl0yQqf84fBm-HNTRwDHR03D5w4Z8xNZGZpAhjJqkwZf4Fyk5RCfarvZPN0aalVNxS1n63CCYOxUqinX-0YtrE20tXKAK45CkNHoeJGIhZffkQ2pJWd3LnXHB9W67Obq0-WM-P7_8VrNBNTsRfgxg6__nSimXgEJ3Qn-vh6tZ842UFKTE-X4PqMVg5ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402b94c148.mp4?token=hQ3lntTnx75ojnofm2fw2TRgrEjAjzcftBnBqytzYgDv2U1N2_F5EGc18iicgCyYEVBy8P0dKSNASoguF_Vh5pfbxi2UgpgS-uZbXDGrgvjXeu9wbtpAlN0DWvAU90umN81WtmhDQDhGWGfVwqdnuwDF3mwl0yQqf84fBm-HNTRwDHR03D5w4Z8xNZGZpAhjJqkwZf4Fyk5RCfarvZPN0aalVNxS1n63CCYOxUqinX-0YtrE20tXKAK45CkNHoeJGIhZffkQ2pJWd3LnXHB9W67Obq0-WM-P7_8VrNBNTsRfgxg6__nSimXgEJ3Qn-vh6tZ842UFKTE-X4PqMVg5ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب رییس را نداریم و برای مثال آنالیزور تیم مجبور است کار رسانه انجام دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133658" target="_blank">📅 12:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133657" target="_blank">📅 12:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
مهدی ترابی: در گذشته زیاد آهنگای تتلو گوش میدادم و تتلیتی بودم، اسطوره ورزشیم علی دایی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133656" target="_blank">📅 11:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
این شادی گل جنجالی محبی که به شکل اسلحه به دست هواداران بوده، به سوژه رسانه های خارجی تبدیل شده و خیلیا این خوشحالی رو تهدید کردن آمریکا تلقی کردند و سعی دارن این بازیکن رو محروم کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133655" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133654">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
❗️
احتمالاً اسکوچیچ سرمربی بعدی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133654" target="_blank">📅 09:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133653">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
اسکوچیچ مربیه خوبیه هیچ شکی نیست ولی 2 میلیون دلار ففط خودش مسلمون ها؟! چقدر مگه روش میخاید بخورید البته حق دارن تعداد بالاست
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/133653" target="_blank">📅 09:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133652">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoQIGWRGIvOTMSvLWncx76A9NqXcjod_W7G-gWkXqQPKXs0B8RhRvSV0jGgDril9_SxYj8rElN1W7MjoTnAi0ezkzVfxF5Ep-oUsPySqVi0hoVDXIHKy4AQi2EMopEeCuA6Td8C79IJySH2hHzs2Fsbb1pyhUXNhKjY0b8ftMHp_inlvhFnVVOTdShx6_IwEbYhLggn298mqBFXSDOxS57NwsAmdrN2HXtTpn3R9dpnm3RQhJ_T8BoKodYjEp9RAJ29AhCYOuXJFjKQ9IGIoyUffHWOWae9GqMamxJt2mxnCF0gi5q6w9zRJq01n79tf1ePhzFz06bIBR0L-O6aaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
استادیوم سوفی لس‌آنجلس که بازی ایران و نیوزلند توش برگزار شد گرونترین استادیوم جهانه و تو ۴ سال با ۵.۵ میلیارد دلار هزینه ساختنش و سقفش از بدنه ورزشگاه جداست و بزرگترین نمایشگر ۳۶۰ درجه ورزشی دنیا با کیفیت 4K رو داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133652" target="_blank">📅 09:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133651">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=ZD3iPiHnseufFd97XovKVjg2DqtT2dDbkiWofsY0m2F7_1gisnv-UZtop7XaoP5sLcpx5Y0rf49b0_FlUG5nu235PXp4bpKm4YyUI9nGTLOZAfi00mjKWlPxr_92FA3WlXE-pfFe6A8NmUHeNrLuHkqXoUzcKK3FeFhYCoCxbdfwvdeE9rPaM8e4SsTsCAgiyIizTlzKrJJmeZjQgfu9-9o4PUECndACNKfs9I9DcLLkhYz2CegRUrAnNXlvjH5vOg_ieI1AhWuRQugYJWVGVg1BIYWL2tle-T5Tj1nlsPOgBWvvfp4RJ5e-htRxjqiM7wBzlMUKhjbUNrfAnPeBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=ZD3iPiHnseufFd97XovKVjg2DqtT2dDbkiWofsY0m2F7_1gisnv-UZtop7XaoP5sLcpx5Y0rf49b0_FlUG5nu235PXp4bpKm4YyUI9nGTLOZAfi00mjKWlPxr_92FA3WlXE-pfFe6A8NmUHeNrLuHkqXoUzcKK3FeFhYCoCxbdfwvdeE9rPaM8e4SsTsCAgiyIizTlzKrJJmeZjQgfu9-9o4PUECndACNKfs9I9DcLLkhYz2CegRUrAnNXlvjH5vOg_ieI1AhWuRQugYJWVGVg1BIYWL2tle-T5Tj1nlsPOgBWvvfp4RJ5e-htRxjqiM7wBzlMUKhjbUNrfAnPeBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
این شادی گل جنجالی محبی که به شکل اسلحه به دست هواداران بوده، به سوژه رسانه های خارجی تبدیل شده و خیلیا این خوشحالی رو تهدید کردن آمریکا تلقی کردند و سعی دارن این بازیکن رو محروم کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133651" target="_blank">📅 09:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133650">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
اینفانتینو به رختکن ایران آمد
🔴
تمجید رئیس فیفا از عملکرد تیم ملی در بازی برابر نیوزیلند و گلایه قلعه‌نویی از رفتار میزبان علیه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133650" target="_blank">📅 09:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=UcQSflXUb3QiNj62uL1Gx-tSBQPfvS9Ny8neRZmGRcMTR52SGSEvX6xEluD7uXi0_Ou8sNqnGi5dn4owrypsoong0-30JHggnsYlKAxhpOf9j2FDs4Qhb4V9BXGPk5wMr9SDk1AP5Q75T1ZAO7weiqYxdB6X6nAGNtx9gDLv6Y3HRNfoS30KsZnjTAomgtdfaOaSlA4R7I8qs8GzEjjsT7BbV_wqqAwI9IJlEJNZPS6J-8sUypKFaR5V0AjQRi6_iEKPiGpYLaIy0lEhPhxAxWa6UY2KpmS_Ey9NuCGuodYOLo_lFu61FOeDqfnx-VwYgVIDjOIDD-KyFXKyy4YUCGVhbEnl_EtxYmNUxtuUT2SirNhyqsNoJMkZXLlB8hY0bq278M-AOIc21KBvYMSmJ_h9R6YQU6gn5aILpbRfdLElzUDWDdyTjpAX_6vufZeqcnvUlr6dVMeSZFAlZ0qRYopsLlRI9YESXedDAzeagQ0zmZRESsCcfWj955Wuu6AUJBd_s-az17vkSI5g6ssz5dhXWFuPaBAVFs3WSp32FXqhnJBJ5RNvbePgHSohlxKDzGDy-kYDoNoRhtn8oXHX0ZiDgAPd_QEa8fI-wRQ1TejgihqMCd_kB4v6PAqFb0QlbGrZKuRAGFAfYlCqIqB0nch-bcvsPVCFbcfYATNXMiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=UcQSflXUb3QiNj62uL1Gx-tSBQPfvS9Ny8neRZmGRcMTR52SGSEvX6xEluD7uXi0_Ou8sNqnGi5dn4owrypsoong0-30JHggnsYlKAxhpOf9j2FDs4Qhb4V9BXGPk5wMr9SDk1AP5Q75T1ZAO7weiqYxdB6X6nAGNtx9gDLv6Y3HRNfoS30KsZnjTAomgtdfaOaSlA4R7I8qs8GzEjjsT7BbV_wqqAwI9IJlEJNZPS6J-8sUypKFaR5V0AjQRi6_iEKPiGpYLaIy0lEhPhxAxWa6UY2KpmS_Ey9NuCGuodYOLo_lFu61FOeDqfnx-VwYgVIDjOIDD-KyFXKyy4YUCGVhbEnl_EtxYmNUxtuUT2SirNhyqsNoJMkZXLlB8hY0bq278M-AOIc21KBvYMSmJ_h9R6YQU6gn5aILpbRfdLElzUDWDdyTjpAX_6vufZeqcnvUlr6dVMeSZFAlZ0qRYopsLlRI9YESXedDAzeagQ0zmZRESsCcfWj955Wuu6AUJBd_s-az17vkSI5g6ssz5dhXWFuPaBAVFs3WSp32FXqhnJBJ5RNvbePgHSohlxKDzGDy-kYDoNoRhtn8oXHX0ZiDgAPd_QEa8fI-wRQ1TejgihqMCd_kB4v6PAqFb0QlbGrZKuRAGFAfYlCqIqB0nch-bcvsPVCFbcfYATNXMiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
قلعه‌نویی: این بازی بهترین بازی دور اول بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133649" target="_blank">📅 09:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133648">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBahCJN-b84VjVxxiuEo0jNz2tUC9JEvsWyjjkgoLUO7w3CK19EiGhEs1hGuMj5TsuMFvftue71ZjtiT0erSY0J3ek1FumG2UmmwHX7iGegJS557mo0ZR2cLycnrUtAyKbCENprGcYiMw9uyzukqvg5dfLuYdKWgaUG13UukDiioylhOguyMqbuce_n6kVjcBkmB6-9aTGY2lQqIHpZN3B1iN9iYiHlBo1VOvIH3_Qc6d3djz84R4Rj0Pn78kwMPAi9sKHcNL4qKAXbEwxR7kiDMZvx4irWtHompswrwQrIlfBQJC4u_u_1wZanJDSNeqSoLm41UiDcQ0iL2ovphrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
70 هزار و 108 نفر تماشاگر بازی ایران - نیوزیلند در استادیوم سوفای بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133648" target="_blank">📅 09:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133647">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdcC3NxK_rYXPD3R0cGegJeEySghZF2PEU5Z5u5HfZRfRqtE4v5JPISYvlXUdRhgqZbvpRm6GGOq2dJvSZCd01URyQdB5jeo_sJTfOG765HJCn3Eq-Cz206UA4SqkZEOlgUmyIx3g0-x2jIVKpbPVbZbY1Ov6HnP1HhuMYxQle23agYQWlZYdjVrMzmDNoocn4hHKdc-AaswUiy9FQ0LMUI2adL7hO-54-11MSIXOb9IqVd5Ysm-XqgrnHdyF4ruBOerq65NOdidtcXW-GCOYOK8ecyFalJ7fHWwa7tx_FyNgE3abCQ2XSsH3k5mUREB2DiQtxmrQ7rCwXC8nPuxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از هواداران ایرانی به یاد «شهدای مدرسه میناب» در استادیوم سوفای لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133647" target="_blank">📅 09:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133646">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJCqTw4F9vWVNXqVRCtk-Yggm2vIs5Li__bFs5M1wXSA5IwLH81AsvnBj33vniacABMXzI2iUB-qiFV_HK9qW5_MZ5GRcAkI08Y8kkk0XEjOH3ZosPZJXzDPkOTxhhkawKwL3N9gdldACLEa18xR68i3AjU0tu4zI8LqaeZo_GLtOwq_LuT_OhDPaH6q8O1dnSeYNVs8FbqcCqCjxa_d2C0pkFTYq7YoHzexR0hEHKy_lPcGKt4mlq6ioyI9PNCzU1DADKbpKG4TMnba-gLN87y9smtCb2ES6LsbuX0AfvIuOcSKm13KBVeZX2W4fVbbIXqRndfgKLiv1UDrdfYOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام جهانی وینکوبت ادامه دارد!
⚪️
IRAN -
⚪️
NEW ZELAND
⚫️
جام‌جهانی گروه G
⏰
سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده ۱ تیر ماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/133646" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133645">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🔴
و تمام بازی مساوی تمام شد و حیف که از این نیوزیلند ضعیف ما سه امتیاز و نگرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133645" target="_blank">📅 06:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133644">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
گل دوم هم زدیم و شد دو بر دو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133644" target="_blank">📅 06:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133643">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
دو توپ دو گل برای نیوزیلند ....آقای نعمتی سلطان سوتی   پ.ن دو توپ آورده دو گل زده نیوزیلند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/133643" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133642">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133642" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133641">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
هر چی دارن باید بزارن ..راحت میشه سه امتیاز این بازی و گرفت ...تیم سختی نیست نیوزیلند ..مهمترین 45 دقیقه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133641" target="_blank">📅 05:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133640">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
نیمه دوم قایدی و علیپور و حسین زاده میتونن کمکمون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133640" target="_blank">📅 05:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133639">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
راحت و با تمرکز بیشتر میشه سه امتیاز این بازی و قشنگ گرفت ..نیوزیلند تو دفاع خیلی ضعیفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133639" target="_blank">📅 05:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133638">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
گل اول ایران به نیوزیلند توسط رامین رضاییان در دقیقه (32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133638" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
نیمه اول یک بر یک تمام شد ‌تو بازی که یک گل زدیم ..یک گل آفساید و یک تیرک ..و عالی بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133637" target="_blank">📅 05:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
❗️
گل تساوی و خداروشکر زدیم ...این نیوزیلند و میشه برد ...در دفاع ضعف دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133636" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133635">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
همچنان توپ و زمین دست ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133635" target="_blank">📅 05:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133634">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
ما داشتیم خوب بازی میکردیم که نیوزیلند گل اول و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133634" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
