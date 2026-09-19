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
<img src="https://cdn4.telesco.pe/file/WkXX0hb1EkrerequuKLBh1TVqyuNAUmcKlhB5_Op_Aelbbv_VGauzVpOiG_xLdFSLs29uEz5Voi50-cMcDpVARKC-_pRDxlu9R5IuKJVGa_Hlj5NNIxgHoA3F-Vhs0mHqdskLlp6YSxOeEGlaS-Oi7yEQaFhdN8n_AnRAOPZ1YzTRYA7jRBzjopHTjShz41hd1SXkigSbg_kPxlXX9B53bTRdZUEjNt6J50qkZcvP3b8Y9ivwVOssrX9WLstHBwkotEl3Wzu6uQ1UKlCUvGdb9Tmww8ftpM5IhgDta8shzkiWZtuq3ybdE2bL1VDAGoWPtgynFR25ZVWRsMOQmeIzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7BFJVTuUvz3Dq3sEO7cKxO-CcCY8t5nijCTLw4Kn5Wvb7dcPComv4Dz2GIY7qY_BjJHF-UY__ipQPfqdU-6bw_LbD59JAM74eu5vaeUVI0ra7zmNrHJ1gsPINR9_HS87osgf_Ehd4of7B7MVinrKVh0iKMa1PASUjEFASwWjwBCgFjR8qccoeYP99jbaHsmIAZoLYAMU5h97-g10nXdCDMZmPFKJKbCFRNPpBOwbF6sT6m1L9V8GNeEhiU-U6DRi329NUC7Hkn1lXj9IMtLSRVShgS-pNkGh83bqwNSP9fJRzbu_yBoOyvJBpI50obEAV6wReduulXwTOJavQpqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEFUlkVfYiKtZrgLbIfZlXQMes5CVA8xjtlQEA2RI_isR1jLIYev6TGaeltpbI8H0a3O70EiKax9TPSs7TzB_Rhj7YwQpRL1oORhZv0cPQBAmn7hCN3g6u3sE7wHCk50U3PTJTSKI-VWg0dow25tk9zU-bhZA22NbDwetibqE9wVxvOCX8KVZakOUT4Wt7Wjh_VBl1eD6FxXLSlQZ_XMELFvHql_P5VfluMLseOSaNM5vOsK6CiChZFeshFLHSzCtTtcY9E508Au4tsLPFJwYYMb7PnunDH4sjWU7rYDbDOpKsw1MnXH0mi-_-niIuJdKePzuUp2B9jXtft_4XBj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=SkNEur5Ewgfgo9U6gRv2aO-uI9BfiNsKSaB7Zb5F3cZvBDjtIIOD7dXgWRHk8v1rfSYaAafn-RoYpsFljAsOlNFWVWOkO323GlOD1E0aju4c1C8RT5o7Y9FizG8pyQfNT0YfhM4GR_JU7g-X2P10gkmk8XxYWBA9wnAzFzq3xPLntgSPmdNvD0ifKY9xYM2i6DnyOJqfUxcQ3O5NLDsGuu7Ge2hwABrYLA0wlPF5CV5dtsdFgcJRiYtwvqrjNQ6xIrr0oaE1t3dgAtrrO97IcQfbUrcghdQfPWhVc8QwGk8DffWPsPMHaeyYbw8idZjVpoOGTmaSx2HaFGfnZCvSUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=SkNEur5Ewgfgo9U6gRv2aO-uI9BfiNsKSaB7Zb5F3cZvBDjtIIOD7dXgWRHk8v1rfSYaAafn-RoYpsFljAsOlNFWVWOkO323GlOD1E0aju4c1C8RT5o7Y9FizG8pyQfNT0YfhM4GR_JU7g-X2P10gkmk8XxYWBA9wnAzFzq3xPLntgSPmdNvD0ifKY9xYM2i6DnyOJqfUxcQ3O5NLDsGuu7Ge2hwABrYLA0wlPF5CV5dtsdFgcJRiYtwvqrjNQ6xIrr0oaE1t3dgAtrrO97IcQfbUrcghdQfPWhVc8QwGk8DffWPsPMHaeyYbw8idZjVpoOGTmaSx2HaFGfnZCvSUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU2BDBDmdiFUzDPaKvZBVae3uXkOOWQ2epdFbXMEcC-28aT-Vjg1Q0HgdCh_v3kxRdcdRVXLEQK4r0BMvIm-YBGMwB6l-MVX5djGppvZx6qic-eFVZQhsV08xpVU92o4h7tyB80veEbsSctQQCWcnsbbsHcR9s6d2ozUbVpjSx3RUVPVIyJY-1OQxUVcP6ewpajJ-PshMfgwpbvvrDTXLnKCTlLbwjtwct07C0VhlqOlq5-lh6u_5pIgMOxzLVakL0mO6snZ_f4FUAOLm-V1M6Dt8FtnmddOj2JHzybD0bPtcDxqXMn4nA79suCFVy7Tz6ASFxE041WkktXwARqJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=k1L3YQB0tPdXLGCY0Fsfu3pz8aUC-l4lEuWK6890QXmRTviKaSBTXSuIhGwjBH1mmfcecbvuqIjVh0W5SKv3FldBte4YEJXFP8euDGen7D6n4g37eBBqAML4VpX42YBE_YZvDaaAMDDkJlTwUGF0Ti_6Z7gUBSQcmJTTHUcmQYoR-2HiEo7Z5axNAdalBfM-kWrfhLld-4jqRmu2gRdmjJG2XrFikfbAUD8OnpV2uBMEmd3sFUf0uxzswWN78MLYb4-du7dP1vA1Qmgf6oAYLoPtnKx6br39RT2fORTXNMgD9Cz0f-F1D3LfJ9xoMSsH6TA0RFIvcG1rPYq8MEk1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=k1L3YQB0tPdXLGCY0Fsfu3pz8aUC-l4lEuWK6890QXmRTviKaSBTXSuIhGwjBH1mmfcecbvuqIjVh0W5SKv3FldBte4YEJXFP8euDGen7D6n4g37eBBqAML4VpX42YBE_YZvDaaAMDDkJlTwUGF0Ti_6Z7gUBSQcmJTTHUcmQYoR-2HiEo7Z5axNAdalBfM-kWrfhLld-4jqRmu2gRdmjJG2XrFikfbAUD8OnpV2uBMEmd3sFUf0uxzswWN78MLYb4-du7dP1vA1Qmgf6oAYLoPtnKx6br39RT2fORTXNMgD9Cz0f-F1D3LfJ9xoMSsH6TA0RFIvcG1rPYq8MEk1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyldCaG_FBG_Zw0nypp7YqeNrou8rrbJIGG2Gs4g2JzV-1VzSAThSlGt7BF0pojx3KWimPBZZGTAoKQi_sbG_BaTCi7pCUeLdiaeHZVHHwUscwl9pMpmEH5yvN7yAxLVDmbxnalJlVHLIpGYqh4z0B5bZPegFESGfrQNvVgltL7-IkA5u7r3oD3V9iqc2jpQiJ-huMg-eVwAOkbrHnyAvBvbFNat6OuKrBPw7V7SB7efDF87t7J61UnGYWOCvt0Xb8oITfBN5E7xnxhh8PnQFVt-BQ7wK-s_FnEFsCYqVEdcM_mQucYGtCIKRKAYbSqVhmqifrg4pZsO_m0WkiXpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0LsfvaAuUTuBI0v3h3yYyXpzLdTPhrfjgaeMjcYc0jNIQj4L8KK3P89spNNyubSjMJFKtm0a7aO-zjNEcs11m9CLDzC0h0p5ySywPtiCVnUycsmFIJAnjJy7KP5McbvrYtyrP6pHEIkQyKqh-yPnG0LSETARZTqC9mnwAOr_hAVK89kxH9sr7HJljoCjfo9EsEN4ueskYumZX_2i9g2sc92XKzuZhV_nRVSwQNlmrn0h_xENyCjnaMFbEEVNMPCJoGkkBmNZyYDfRlX-8MSwmzLfa3oiz2_lYWG3NJhPieQKzc2JixPCVUrEPft_cg6g6YsXjf36f2GfdpIIRg32Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3AVvc2psLSYSu1ILC3bgKbeDi9YOUsKe0eVuwDuBzzmk7RFiKNOQC1axS_DtgI-M9CB6c1Hl6t2qdARNPPul_VQX2QpHeCRnOabDE-WSOGaX2nWSI9nHnCrVPn2X_5Ru1V2SGYbo9qsgbTu4DYuaUS1hY-DwKWlfO7uGEtVNsZNvBagg0srdpYwT0tkQPW34mn5v0PF5XtwsrYD4Ue-vQN1H4crXG5gB1RykPQ-dr3xnjLPVoZavrvFm2Mpb7bnSQLcxbrtLeTQqYAGkyD_Xpti518g4HdCQebsptH34CWIk2qHwMpof8Lffh649ftFlJNCaC0ETV8u7itUtiZ2sQNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3AVvc2psLSYSu1ILC3bgKbeDi9YOUsKe0eVuwDuBzzmk7RFiKNOQC1axS_DtgI-M9CB6c1Hl6t2qdARNPPul_VQX2QpHeCRnOabDE-WSOGaX2nWSI9nHnCrVPn2X_5Ru1V2SGYbo9qsgbTu4DYuaUS1hY-DwKWlfO7uGEtVNsZNvBagg0srdpYwT0tkQPW34mn5v0PF5XtwsrYD4Ue-vQN1H4crXG5gB1RykPQ-dr3xnjLPVoZavrvFm2Mpb7bnSQLcxbrtLeTQqYAGkyD_Xpti518g4HdCQebsptH34CWIk2qHwMpof8Lffh649ftFlJNCaC0ETV8u7itUtiZ2sQNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=baMwp-ImgWUyrjnshZZTTxNdx9S0gLJO5bXdIXnPxfqfZsHfUjTF___NM4n0vgaMjhGBkwfs8zQ799YFyqWRKoI0MEsD9dhJvYgNGHYYzE5Vk36uXSitM1ESKubD5N07VBbpl_l__h7fcOkv1_N8OXMIqc4s_mnsnsQ3OXe1CVaY4pfaDNrd1oC9oiL7rWqxy7gxlWHerOQS7505PecPFV0JIpTMwsjmMOo86wV_ol4Eyeso0h8CNmIyT0lBHDPaIGyTdirVb6LiJxboGrovN-DvkGI8kRB0Ivo9x-A1R0ITkv4m-cyuZ-EWvfRosEeYCVvD_P6FD6b7aWt8895u0WqbhZp6PE65egCHOB-UxL9VKK8xVyEaIDUqGkYtWwd7qH9qX8pc-jwj6ocYqaH8iLmxNt1Y60GxioGVrhH3-0_BH_P9x8qVApd8NuhpeOLtFpVjEW9i2tHS0MJpcKk2pHVUwOuA5hpTNR3qhuLalbJEuZxbEDv10dzYMr7hdXEq-ibpHzcu0vorX2N0CxqF-q6KmfTvUEly-EEhFVvD0_idNozn6-tVo9-5E6vtPvE9CxCSg1sNnf1eOZMIQyPfDxUP1AMqvf6PzIfvo_-HtNsu6_6ZWCdeDvgY0L2dgpxtJhdhv3CqBKedQ1pl-3HR4mhTuRU4a0Hexv9-itKts1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=baMwp-ImgWUyrjnshZZTTxNdx9S0gLJO5bXdIXnPxfqfZsHfUjTF___NM4n0vgaMjhGBkwfs8zQ799YFyqWRKoI0MEsD9dhJvYgNGHYYzE5Vk36uXSitM1ESKubD5N07VBbpl_l__h7fcOkv1_N8OXMIqc4s_mnsnsQ3OXe1CVaY4pfaDNrd1oC9oiL7rWqxy7gxlWHerOQS7505PecPFV0JIpTMwsjmMOo86wV_ol4Eyeso0h8CNmIyT0lBHDPaIGyTdirVb6LiJxboGrovN-DvkGI8kRB0Ivo9x-A1R0ITkv4m-cyuZ-EWvfRosEeYCVvD_P6FD6b7aWt8895u0WqbhZp6PE65egCHOB-UxL9VKK8xVyEaIDUqGkYtWwd7qH9qX8pc-jwj6ocYqaH8iLmxNt1Y60GxioGVrhH3-0_BH_P9x8qVApd8NuhpeOLtFpVjEW9i2tHS0MJpcKk2pHVUwOuA5hpTNR3qhuLalbJEuZxbEDv10dzYMr7hdXEq-ibpHzcu0vorX2N0CxqF-q6KmfTvUEly-EEhFVvD0_idNozn6-tVo9-5E6vtPvE9CxCSg1sNnf1eOZMIQyPfDxUP1AMqvf6PzIfvo_-HtNsu6_6ZWCdeDvgY0L2dgpxtJhdhv3CqBKedQ1pl-3HR4mhTuRU4a0Hexv9-itKts1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشته کریمی، ستاره‌ی سال‌های اخیرِ فوتسال ایران، امروز اولین بازی خودشو در قامت فوتبالیست، برای تیم فوتبال پرسپولیس انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL_MuNN-hWS9enSdCRy_-aUrq0HvHOJj1tQv0-AK-QIBAYbQ0DTBqZwMHjSRiH1T68bI3SDwkgnnOfYYR0MfI5Qe_g4yn7aVv7mbpfiedJEaD0K0OSpdY7Dq5obtKmOB0X-UOO-P48FpuiMx6wOdre9YgHzQZPThfj0aMBV28O1Zn-sgWSrKgaIs55qwaN9aUqxu2Fg_IN9nRf3ifj_8BhhS3Wirfr5qdE8RyOSpsZ2H118LpvHgvj2bD1sGQrKlgiXFV6iWNpYUHyF_mS4MlhEpkbDl5h6bL-Z2jd4I7RIXG06lqvQrU_UXBTT7xvBaIGJAKlZKsK8ol1qXkBVPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اینم تو یه دنیای دیگه‌ست
😂
⚡️
آخه اسکول، تو این گرما این چه لباسیه؟!
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8dnBqgmfe4CvJd1XLW3Vqt7IU9nNSc5YPzI9fKAFnpYvJ7tVt-Qya3Ur_ITGk0-l_bq8JOvBS6FNI-3PMlFYb-1eqavF_YORa-DTMSYVWbIzXOtUKa_MzjY-inqML9gwlR9Kx5QMhkzZko0HcFIHXHf0iccNdl93ockmonKLybIMXzrDOpZOnDpmgP0sMSCKKUlZ25otFHLpjKpFtYVj36ws30k1wgOKgREEU-fArWjby83pmhtmeTwzN7520wBJ8m3aHsf_2RCakZi9ljXjUJJuLepEXKIIFH_tw8ZWJ9If31iDU7a0hmFxGrv_O0OdJCowywVidvrlVoF8WXEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCRJ0behf_G4Uh6w7EPUmJxS4ewJODLVuF3oLl9lXBZiAnQvKl61bpGAH2wQy6T4ArH7YkxXeKfoxF86Pymw810FmnayGKOwH3eAoekZ4xay0MvMvbenEEptXPSm3WIcdyuxLG1GJVTsx5Ef9lAUxwZMdqRt_FSRH19CwJx01mJ6uziKRm5vi5WXKkjVs6ON-1ArMu9Y2LaI98JXmSL7OBehXBHG1FzMbzi9ktZfrgA6ERQB5YNg7zdQdHWvH7YzDY6GEuYg3mJTosS9HYmkc0c4sRQtTwzBL8IMBSsssPyPpn8FT_SQuwYqWqwLu0nZh6D3m2ca3ATaOdshxvdbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Brentford -
🔵
Chelsea
⏰
Tonight 22:30
🏟
Gtech Community
🟣
برنتفورد مقابل چلسی؛ جدالی که برنتفورد با فشار و بازی مستقیم می‌تواند برای آبی‌ها دردسرساز شود. چلسی از نظر کیفیت فردی دست بالاتر را دارد، اما در بازی‌های خارج از خانه باید مقابل انتقال‌های سریع برنتفورد مراقب باشد. با توجه به سبک دو تیم، انتظار دیداری نزدیک و موقعیت‌ساز از هر دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140240" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140239" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=p5klnHmbB_VuKnhwJ02StUPW26qmHBPQavm9qy9CfVDZU3OTuLkmdqhxeodxcghYuUHBJdn0FHEeiHruPfhB0kkXR9pZTXDx9O6TA9_rX2_WYrj_zwBjbA-GQqlT_Z2icMV31yMWD3NqUCWNEH5q-3eiIdhJSMlJ8VlnebCsyEsJnhJ99JDXiuvzEgqjBqAdIRqZBj9YJToc--Am6sAM1E6ADvzNARdtwqjI-s0oIZ-jfftzd63NmdL-suH7F8-lRVRHnNBPQtkOPu3RSe1eWi1vJKgRTSN2OdA_Xi-IPEAiRl81PQoSul3kVovExExLaJo7htqAo6V8oPpcRvnjfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=p5klnHmbB_VuKnhwJ02StUPW26qmHBPQavm9qy9CfVDZU3OTuLkmdqhxeodxcghYuUHBJdn0FHEeiHruPfhB0kkXR9pZTXDx9O6TA9_rX2_WYrj_zwBjbA-GQqlT_Z2icMV31yMWD3NqUCWNEH5q-3eiIdhJSMlJ8VlnebCsyEsJnhJ99JDXiuvzEgqjBqAdIRqZBj9YJToc--Am6sAM1E6ADvzNARdtwqjI-s0oIZ-jfftzd63NmdL-suH7F8-lRVRHnNBPQtkOPu3RSe1eWi1vJKgRTSN2OdA_Xi-IPEAiRl81PQoSul3kVovExExLaJo7htqAo6V8oPpcRvnjfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امید عالیشاه
؛ به جای عزیزانی که اخلاق را در ورزش رعایت نکردند، دچار شرم نیابتی شدم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140238" target="_blank">📅 17:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140237" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzNnLpa6-XcKhMAiBhLjXDX_rojIOxdHm7le2fXh6xmjdkmiiuoBUMc5hMFhlj43qVrVki8B-SPIS8RZpXnD9AmrmikqXvjMM4UhV33dKj4Q4HLBMEOSI2YFfbde5EIc8E6qqOBlP4YPEB5Ea9d0W7D1wGWJIvhk41y0tQBxOLHFXdeU0FgkpehNeJlaB41Vsm3kj1C0M4a6HuqSYzFgKhUHFoDmhUiqCFUbkbvPO02RLNRey0pryBm7kAzNv8YnI_dpnaAZicfUheWjA6XOc7LQvgNko7b1npwtEOVwSwA3unSKny6xTN91_TFaj2u6q5rhlWCuHJCgtAgXjOBoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
یکسال پیش در چنین شبی رقم خورد
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=a5f07_Mg8dQvkRpjqorKHWlhUVor7n6HcRYP99GovQbbhlLNuBgIaSTArMgmFYttWU68Jne3itXtEbqMM3K8eT_nHF7f5ylm5SnU2cQNTV6eSwwAw8eoZ266grGZVDMgXK5rbevRrEI7SpJ6ZQTXP19VomOOaEvcexN8GKjiHsUv_YgHp-efoEOMt-cwDwd3ojSt-goqMCy60ILOTy38393DkSNKWuYn0P-TIRj7au8uLY6AHFZMD3pcboZ_mUxzsXRY0HRV1UEUFXSV75fSTOdVPZ29821rdp1ee1KxjhOj97cFslccZywpZj1i9ldghyp8pF1RBEBFiJpe6Q1CsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=a5f07_Mg8dQvkRpjqorKHWlhUVor7n6HcRYP99GovQbbhlLNuBgIaSTArMgmFYttWU68Jne3itXtEbqMM3K8eT_nHF7f5ylm5SnU2cQNTV6eSwwAw8eoZ266grGZVDMgXK5rbevRrEI7SpJ6ZQTXP19VomOOaEvcexN8GKjiHsUv_YgHp-efoEOMt-cwDwd3ojSt-goqMCy60ILOTy38393DkSNKWuYn0P-TIRj7au8uLY6AHFZMD3pcboZ_mUxzsXRY0HRV1UEUFXSV75fSTOdVPZ29821rdp1ee1KxjhOj97cFslccZywpZj1i9ldghyp8pF1RBEBFiJpe6Q1CsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=VrwnR3ybJs4yiE0ZVuWsIN1XZccbebrlXCZ0qxXc0D0f0iteSZbMCTt0JvL_Uw8VCO5PIZpGlIYXw0IlV7GaJqfvQuOthseUpzHIkzUPHzElAULTb6_Cj8XQi5FA0SXP6RTQMSLYOk-GJW5MplUuI8BDd6ApX_2Jb4kFxAWnOvVczYA7YpIYqrLlzfP4LxwZysZWnKLD6wuEt-PHOtbU58ZCzXjJoh-eMJ1dsElX_ADvArYs4DKyU5BoVE7--9Zbrpt-lH0KpQ5AE5ZAEB-4vD4tdEnM_bkqgicmCbIHKUIz9fX8AA7a3enaGYTiHeuV3nTuKtRovGYRW2E1UJ7XwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=VrwnR3ybJs4yiE0ZVuWsIN1XZccbebrlXCZ0qxXc0D0f0iteSZbMCTt0JvL_Uw8VCO5PIZpGlIYXw0IlV7GaJqfvQuOthseUpzHIkzUPHzElAULTb6_Cj8XQi5FA0SXP6RTQMSLYOk-GJW5MplUuI8BDd6ApX_2Jb4kFxAWnOvVczYA7YpIYqrLlzfP4LxwZysZWnKLD6wuEt-PHOtbU58ZCzXjJoh-eMJ1dsElX_ADvArYs4DKyU5BoVE7--9Zbrpt-lH0KpQ5AE5ZAEB-4vD4tdEnM_bkqgicmCbIHKUIz9fX8AA7a3enaGYTiHeuV3nTuKtRovGYRW2E1UJ7XwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
محمد خدابنده لو درحالی به تیم ملی دعوت نشد که در 6 هفته ابتدایی لیگ دوبار در ترکیب منتخب هفته قرار گرفت
✔️
✔️
همچنین این بازیکن با نمره متوسط 7.37 یازدهمین بازیکن برتر لیگ از این نظر بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxDAsptlPm2KNMjrw6DBRH7PUP3ibl15x7yagMIKCCeeEQGVexI8XMouKAmY7ZKrdSE92c8YoCqqzsUL3fOTakr8IQNRe99ESH8wUp-ZtfiIhHD4epr29iVdYzsmbZppQ3sAq7tk6_hIPYt3ArZRTY7c1BN6XWVwwnTlliJtt59aesTKbMoIOM-c5LVAz7GZQm45jhpw52EBL1MdEivSBYdgul4OtACj7b8_ulU65NehzN65Hu9pf7V0i3B0eD1MzWwsgilanHbu6jbgCCIOqI4Cfm6z9WKdUO3pfqFROgH6Fa_PhGDHqCDmDGigDpnEIMo6Q7QlM3lKlh08IWmVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140231" target="_blank">📅 13:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140230" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140229" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140228" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
پشت پرده عدم دعوت کاپیتان‌های پرسپوليس
👀
غیبت کنعانی و علیپور در جمع نفرات اعلام شده لیست تیم ملی سوال‌برانگیز شد اما ظاهرا کنعانی از ناحیه مینیسک و علیپور از ناحیه زانو دچار آسیب شدند و حداقل دو هفته دیگر به تمرینات پرفشار خواهند رسید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140227" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUzh0qdX8-HAxMt4u8a8Gos5MvQJYTX0K63RWdwbsPqqPNLdBKiV4-_0rEIBwX4bSpojX1DnbePQBVAHm5etkcexA-GPGieVitOOMedEPzt9mg05_mvGXU9aKhoXsiCysMqOr8_PCOyil-kPSoqISAM7Ph0dlUGLHKZQ6kfFZPigblgKELY9ag7LfudHPp8rIeEB6ewyS9wXLgOz0T0a0bW_h1LpJZ1NxXSJ6tBhQBLQU_6bCE8zNO3i2x-1dteIa405nswiCNKuf1gWbQcumj3V_oQK3KEyH4Dj_Ltg8nnsv37BH35EqGR8bEfUyb45quQCa7YUaQoRFMkLGq5rLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن در خانه؛ جایی برای لغزش مقابل یونیون نیست!
[
بایرن‌مونیخ
🔴
🆚
🔴
یونیون‌برلین
]
⚽️
بایرن‌مونیخ با مالکیت و فشار بالا، احتمالاً از همان ابتدا بازی را در زمین یونیون دنبال می‌کند. یونیون برای دوام آوردن، روی فشردگی دفاعی و ضدحملات حساب خواهد کرد و فضای کمی به بایرن می‌دهد. با این حال، کیفیت هجومی بایرن می‌تواند در طول بازی اختلاف را رقم بزند.
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140226" target="_blank">📅 12:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140225" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140224" target="_blank">📅 12:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140223" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140222">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140222" target="_blank">📅 11:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140221">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140221" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
زنوزی به خداداد عزیزی قول داده که با توجه به روابطی که او دارد، محرومیتی برایش در کار نخواهد بود و از این جهت خیالش راحت باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140220" target="_blank">📅 11:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140219">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOw1k3RUebdFEGz6szNCSzEsmRBDSKWnhUjwUHzoHU1CsBrk6gy-ZvjrcPChfo8mZ7y4NbZLhDLi7C110PdEM1BAxD5ll7KXdaQp_cduxg376L7Fw2HHtCEO4lqm_G0jK8rrnFEaXs7zCdSlkW_aCLm2pIvARiYwmbj3Po4eParXWgKePqkUtrbddJEcaI6_1xY-rZtYmlraYGrf8Iie4nIBnVplnQxdhV-F5vtchuuBOCdllbVtB8_aYjgCLizlnu2Zr1YnP2R2U8tDgFH5pwMG1UPDbGUjAA3vEw8sk3e--zPzZi9A028Ly-jdnQ3G2jJzAv2J9R0tWr1P4Gge8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140219" target="_blank">📅 10:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140218" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140217" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140215">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
با بهبود وضعیت چمن، تمرینات پرسپولیس به زودی به ورزشگاه شهید کاظمی منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140215" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140214" target="_blank">📅 01:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140213" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
🇮🇷
محسن خلیلی خبر مذاکره مدیریت باشگاه تراکتور با اوستون اورونوف رو تکذیب کرد و اعلام کرد این بازیکن هییییچ آفری ندارد و در جمع شاگردان مهدی تارتار موندنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140212" target="_blank">📅 00:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxYVhDeIkQYD0o-byJ1wLi18zKN2udu6T0JIzADkUNiqfbgtFYK9hOcPyFxERmeGqb9nTXaJdGBPOKfbF4B7GonCa9MedcZ0pL0KZ0CN_zUY3QGZThSLoRwPjXqnaN6DFZyhRucAZUHTFmf5QxiiQCjYy9Gn6ajIr_krox3lz1fCFMDVGyscweJUUwvx7bW7Ajx7CfUuTRYgQWZDzD3B6u1FxTtg4rnY6fW_2in70rNss3yCIZr9TH3SXc62x4qapmtt27LBszGzlSHQU7QKIgnFDfV4laA05U-Pg0Vgif21MzHuU3yo_M9HFK9EpulYw2MZ0j4YsiUaT0c3bPkYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140211" target="_blank">📅 00:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140210">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
🔻
🔻
توضیحات #تکمیلی در مورد پرونده اموال توقیفی باشگاه؛ از صندلی چرخ دار گرفته تا پرینتر و آب سردکن
🔻
🔻
🔻
در دوره علی اکبر طاهری شرکت امین سیمای کیش(۳۰۹۰) اسپانسر پرسپولیس میشه و به جز اون چصه حق اسپانسری که به هزار مکافات به پرسپولیس پرداخت می‌کنند با همکاری…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140210" target="_blank">📅 00:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140209" target="_blank">📅 23:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140208">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=Wq4N3wYYfE4eFxSmdxwa9LHAXB7EQFnrikbLGmQvKgCialtJmS5Xe18hlJ3mJy6o-2ZzLVegBKEaFfV4HfajwBovflw7hLfGdyuTstl-BUQ7K6eCotis5GBpJTqltu7hGqXlQ-yJV8uKVoutiAusaa-ChUF84h7ZbsncNBh_jIH37jTg3Cf-aIDEee3bmV8kzBaSa4z-aEcRuJk2Zcdo6BkJWbnZO43TsGWaV6JNPRYfxayHeiBOVZS3mfjTSWmMffEEcFtTaaEPMaqBJq2MO_K6kDlKugIuGesemvYVtDSXm-KZHW96nyZtmP1-n5Ri8NXVCxRAFugKqk_EUmFCTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=Wq4N3wYYfE4eFxSmdxwa9LHAXB7EQFnrikbLGmQvKgCialtJmS5Xe18hlJ3mJy6o-2ZzLVegBKEaFfV4HfajwBovflw7hLfGdyuTstl-BUQ7K6eCotis5GBpJTqltu7hGqXlQ-yJV8uKVoutiAusaa-ChUF84h7ZbsncNBh_jIH37jTg3Cf-aIDEee3bmV8kzBaSa4z-aEcRuJk2Zcdo6BkJWbnZO43TsGWaV6JNPRYfxayHeiBOVZS3mfjTSWmMffEEcFtTaaEPMaqBJq2MO_K6kDlKugIuGesemvYVtDSXm-KZHW96nyZtmP1-n5Ri8NXVCxRAFugKqk_EUmFCTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140208" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140207" target="_blank">📅 22:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/140206" target="_blank">📅 21:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140205" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb6VT3hpRoX7DOe5cK8rcguhK3Gc7rDphBNM9x8VNT8dkJtCZKzFDIcupvzlB9dgXMoJhVoEcvPfrQFoJqjtncUQsVY3ewqECNUa1KtRk8jXYTlkZRSSAnsPgchzWzzFZ2BDJmMt0oqEbGLoY2dTmNcTH4Bx6Xa6klf1-Gi0kV_nygE1u5aiSxtGKipb8AnwcKQeEAEY-ZnAIStWyiajD4tQbfMOJUOCuGEwPBPMDGZWRBX8dCpSw6HhVeNzep8Mx6aQijK8__U8tpyjJ4PBW7V1WYQEnQqQSYLtxws1AMEOvBLXj7hPOEH0K_w5Ez37sk9i2-LHmDuDx-OhMw-ATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140204" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140203" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=Hxct3R36DNyiDMtZhRKer5j4bYN3uHLX3smhvnB4ID8PshPeB0E7Y3BAjcy_pD-vwfQUrexQlpe2LhQ8TO9VFZFvXKC4BKjihOXeIKlFR8KLIFkY9EEXIJKx71SJnRpy-4uW1-Gk2FXp3gahYtOsnDWH568KCr2w8VND_UHEo2bL8H9dq_h0ttOOeGIHTsR71tOaVLQF9D5s87zmjOAFxzorqxTjQWr3IkXAOEhfbpINbeCH0JtOuLDvTI1M24aXQa-B6bewCNMMpIpHOv4mUTp518ATx04Vy8kKB6mf-5d2mp021mawpRzYQpjq9D4GBNc6L0OV4TZt4F_zPda6WDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=Hxct3R36DNyiDMtZhRKer5j4bYN3uHLX3smhvnB4ID8PshPeB0E7Y3BAjcy_pD-vwfQUrexQlpe2LhQ8TO9VFZFvXKC4BKjihOXeIKlFR8KLIFkY9EEXIJKx71SJnRpy-4uW1-Gk2FXp3gahYtOsnDWH568KCr2w8VND_UHEo2bL8H9dq_h0ttOOeGIHTsR71tOaVLQF9D5s87zmjOAFxzorqxTjQWr3IkXAOEhfbpINbeCH0JtOuLDvTI1M24aXQa-B6bewCNMMpIpHOv4mUTp518ATx04Vy8kKB6mf-5d2mp021mawpRzYQpjq9D4GBNc6L0OV4TZt4F_zPda6WDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140202" target="_blank">📅 21:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140201" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
#فوری | ترامپ: هر اتفاقی ممکن است بیفتد
🔻
تصمیم بزرگی در پیش دارم؛ آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است
🔻
به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140200" target="_blank">📅 21:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDmdp13rBFHD9GjiyauqgJIcS7iK8BDlPLKQDFEnukBjCBkLsC1pd_kRsZpslzdcXmomc75T2iMQvxUW0S1HfYnSwWmdeaiIqRe_sqk0zbrwdXMyKFP-Ea7CVX-tpWGC1cUht4EwoQMsOdrEh2U8KqKT2qwTbhluRB35fN_D3vGNn359b0TbeyosPVLhb9dddVlqdfd0DnoAnptftUTH2Sf0AGtDZvXc5jpwpVlkhyekb2VTuNCUkU5lDcUzlhFcH8Ent5m3iPZqu_Ejw8LEZ7od8vLVWBt8eA__woML-R65FEd85E4psxEbhrcU1_YSuuDof0uIJC7R5n8efVGj_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
❌
❌
در اقدامی عجیب علیرضا اشرف مدیر رسانه‌ای پرسپولیس اشتباهی عکس لخت خودش و پسرشو فرستاد توچنل‌رسمی پرسپولیس و زود پاکش کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140199" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔄
🔄
علیرضا اشرف، مدیر رسانه‌ای پرسپولیس: خوشبختانه آسیب دیدگی ابوالفضل جلالی جدی نیست و با استراحت و ریکاوری مناسب، به بازی بعدی میرسه  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140198" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140197" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
پرسپولیس قصد داره قرارداد امیرحسین محمودی رو با بند فسخ ۱.۸ میلیون یورویی تمدید کنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140196" target="_blank">📅 19:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140195">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
سازمان نظام وظیفه به علیرضا جهانبخش اعلام کرده که معافیت‌تحصیلی‌اش رو به‌پایان است و باید تا اواخر آذر ماه تکلیف خود را روشن کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140195" target="_blank">📅 19:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140194">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvSPCKC4aAx5bqqo8gNN2DjmSDUb1gAPgIXZ8mNEMnfegMntpmGwx24II7Ct5h8lMPBilJK5oAfey0gcB9dMJ7qpVabF8DVIQ8m5Fgh4t2jBMwsAv-ptnVdPlUYgL1xp5uIVMZAPqOzpQrjkPbt9Q8P4LjjVLCHiuTeSOeWDSCMeuj1OC0uxO4_l8XY60uFivJc_OxU6k2SzW95pOb9OUHmbgMw9DNlTLL-VNyq6ULfo9HV01IIArLqp-zo9lzIpgEGVOyZP3mNsXfoQThM17s0b4IXlQJqZs52zb293-bUGFKeVgnG6Af8shh7L_K54BGcUDEzaOq_Anz4i5VQHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیتی و نوریچ؛ شبِ امتحان برای سیتیزن‌ها، با یک حریف که چیزی برای از دست دادن ندارد.
[
منچسترسیتی
🔵
🆚
🟢
نوریچ‌سیتی
]
⚽️
سیتی با مالکیت و گردش سریع توپ، از همان ابتدا برای کنترل بازی جلو می‌کشد. نوریچ احتمالاً با دفاع فشرده و ضدحملات به دنبال ایجاد خطر خواهد بود. اختلاف کیفیت دو تیم به سود سیتی است، اما باز کردن خط دفاعی نوریچ چالش اصلی بازی خواهد بود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
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
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140194" target="_blank">📅 19:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140193" target="_blank">📅 17:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/140192" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
مراقبت از پوریا شهرآبادی از دست ایجنت‌ها جزو اولویت‌های اصلی باشگاه در ادامه فصل باید باشه. پس از درخشش این بازیکن در بازی امروز و احتمالا ادامه تورنمنت آسیایی، اسم پوریا بیشتر سر زبون‌ها میفته و مدیریت رفتار و دقایق بازی کردن این ستاره جوان، جزو مهمترین…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140191" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140190" target="_blank">📅 16:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140189" target="_blank">📅 16:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
شکایت پرسپولیس از آسانی رد شد
✅
با اعلام کمیته انضباطی، شکایت پرسپولیس از استقلال بابت حضور یاسر آسانی در داربی رد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/140188" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140187" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140186" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140185" target="_blank">📅 14:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140184" target="_blank">📅 14:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
اورونوف به همراه برادرش که چند روزی کنارش بود، دیروز ایران رو ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140183" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/140182" target="_blank">📅 11:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
✅
علی قلی زاده: من از ته قلبم پرسپولیسی هستم و دوست دارم برای این تیم بازی کنم
❌
❌
اینکه به جام ملت‌های آسیا برسم یا نه بستگی به شرایط ریکاوری زانو دارد/ حضور من در جام ملت‌های آسیا نشدنی نیست و باید منتظر باشم
❌
❌
فعلا فقط دو ماه از مصدومیتم گذشته.خدا را…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140181" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140180" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140179" target="_blank">📅 11:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140178" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
