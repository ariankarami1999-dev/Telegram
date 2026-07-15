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
<img src="https://cdn4.telesco.pe/file/Znc5Ez7D2EcnZAIT-wOU_XmllE09aud7leeRyX1G2ADfrJ74XK5LmAK5uDiFFcyjFKsKFl6P7fKfdi9-2nm6D7zQ6qr9BwnL-GuForAMJnacC_Wz9HkS9iYfUD7rWJVlZI1lcyYEyy42HCtIf3nsPkzsDuHe68pMmhHRyGbleruSzFl7IeHz64fJcwUtq4pVTtrBet8wiOSiUoD77YGZ00w3IaeaD2wzBp1qc2MZxSxAo0FgZpQFONwoH30IPmmI-SW0OWGkBXa4waZ6Tv6G32deIMN8V4950g9pPF6cxT3QGZbg6xNTSnyhnSEQgfGchih1NVfBZEqxMfxjBcuD8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=EtNn8ix2Ku3GQcl50exYI_6BEHAlO3CqoU3DzhAG9Zd3JvyOAlLj0nqLTW039K7V3-X3NTJyeLXuzO5g3E0zaZa2dSzfpDD9BtbXwNOG7hHp6Fp1nW6nUl-9IOVT9427R-ueHfeRV7Y5z9VqHc_hZBX8_s-p8K-s_CbG6IjEpZ5_uYq_2F_XNdkqzXGZdIwNbHAOt5x0nHB_CuUstG5Jw8i1HbGp0Oelt3PLW4yAinOs6XgwEnsNF028vjMbRw-aILWgsQAYDMbfYsOaEUbyxNvLx6JIeHSTLfpBj-6Lv_f_T1x9bqj2doCY333EloUgTJWa8VVMTYFm8tvoL7TWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228cd1f66e.mp4?token=EtNn8ix2Ku3GQcl50exYI_6BEHAlO3CqoU3DzhAG9Zd3JvyOAlLj0nqLTW039K7V3-X3NTJyeLXuzO5g3E0zaZa2dSzfpDD9BtbXwNOG7hHp6Fp1nW6nUl-9IOVT9427R-ueHfeRV7Y5z9VqHc_hZBX8_s-p8K-s_CbG6IjEpZ5_uYq_2F_XNdkqzXGZdIwNbHAOt5x0nHB_CuUstG5Jw8i1HbGp0Oelt3PLW4yAinOs6XgwEnsNF028vjMbRw-aILWgsQAYDMbfYsOaEUbyxNvLx6JIeHSTLfpBj-6Lv_f_T1x9bqj2doCY333EloUgTJWa8VVMTYFm8tvoL7TWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/135869" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
کریم باقری، کمکی که هر سرمربی آرزویش را دارد/ چرا او هیچ‌وقت سمت نفر اول بودن نرفت؟ پاسخ از زبان خود آقاکریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/135868" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHvP4pFRP_uhBY324L-coDU2L_b_D-IgGPv6CDpQmpgT1bqNUKU49yBGseHqlVEnlX9hS3lLD3mmvZBxXdO045JkX8qZA4P_ylsC9kfbJAjnemT64aNh5844nPm-e0pT7y4aWSFpG5mQU5n5IZBgb8GMN-jN6eABmbdZRHqXxMd0M8VfgxjHweRrY5SUkyI8QpotljSPULqhexgqL0XXaM2kCpoX4dGlSUUfYD572NL2JLecONe1JKlDQnTRPzcQXEQPrBFbpZTXjpXMAqf1LgR4zK3sXsjyOWFe_OV_G3vVfwGyea1c7WyxcosaQ2Rwj4MDxS2Cm-4zZCfBRHB_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/135867" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🔴
ایجنت محمد مهدی زارع دقایقی پیش از باشگاه پرسپولیس خارج شد و گفت به زودی همه چیز مشخص خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/135866" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
با رضایت مهدی تارتار از عملکرد مارکو باکیچ، این هافبک در جمع سرخ‌پوشان ماندگار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/135865" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
امیرحسین محمودی ستاره جوان پرسپولیس امروز ۲۰ ساله شد
❤️
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/135864" target="_blank">📅 19:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📌
مارکو باکیچ امشب پرواز داره و به تهران میاد و از فردا در تمرینات حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/135863" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🟨
🟨
دوکو بخاطر زایمان همسرش اردو بلژیک رو ترک کرده و احتمالا بازی فردا شب مقابل تیم قلعه‌نویی رو از دست میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/135862" target="_blank">📅 19:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/135861" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135860" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKrxXOPvlnnppd_X9PITTDwx1maVq4fUox1oAwyqbkr5gbzcedcLwafulRLxrC5d4liV73PdJcLlTtYBTdj2lOUtcxXO1szGXCuaqipphaCrOjkT_RYD_gClPVPFTKxjMFVpXLRh6bSgDZTsTUiFrxLEn6kLbM2z1xaf59KXr3UW-ykHgtuNYtnnJ-MJrTeX_PX5cfviDqgHdMeKnT-DmvmNtEDn5nVT-9RaT_XPmPiejK9pAJHOoZxrwTi7hKgggb4DcO5eaBeSHSqLxLLta5oMS59oqmC7JpQlOwSSQ7o29Oa8PMgsqNuMXyiX6OFfCChviXe5tfcSo7g5GrIe6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قرارداد پورعلی‌گنجی با پرسپولیس همچنان معتبر است و هنوز فسخی میان طرفین انجام نشده است. از همین رو، اگر باشگاه در جذب مدافعان مدنظر تارتار ناکام بماند، احتمال دارد از پورعلی‌گنجی برای بازگشت به تمرینات دعوت شود. ضمن اینکه خود این بازیکن نیز علاقه دارد به حضورش در پرسپولیس ادامه دهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135859" target="_blank">📅 18:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">😀
😀
😀
😀
فووووووری؛ زهره فلاح زاده خبرنگار معتبر حوزه استقلال:
🚨
🚨
🚨
مذاکرات پرسپولیس و یاسر آسانی از شب گذشته آغاز شده است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/135858" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/135857" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
#فوری | ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/135856" target="_blank">📅 18:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
علی دایی و کریم باقری امشب مهمان برنامه عادل فردوسی‌پور برای بازی آرژانتین و انگلیس هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/135855" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
طاهری رویای بازی تو پرسپولیس رو داشته و توسط شهاب زندی مدیرعامل نساجی گول خورده و حالا هرطور شده میخواد فسخ کنه.///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/135854" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
🗞
کسرا طاهری بدنبال فسخ قرارداد با نساجی تا ۴۸ ساعت آینده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135853" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135852" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMYtd4vayrN2nCQodd5xNSe5KFqZMtIaRE8-7sD-2qp1GYXyGRK2EUo5hDzJfxeNmBl9W2gM_CDV0CV3MOLQSRbWE-y4eVqbZR1xgpsgPFGdisIzTZIhCcrSU_ZSOMZ0Fw2dF--Hu0IC0wqcSEPn6jLLyZ6eIQsl73DijCIW1SI1vKmCM7JWO_VaQ344dNUreFRyRtERllwgfl7wZzbTmwNxRNvjYcbG4dlyswJUZyLB0-RZSdpTnBRt6qVfs36MODGQd-tF8n71syBc0c1b1exs0pec4lv6TWwUBDB4ljbqggvJvLUapoFHGTjelEL3ruxUiINFsRljJ28xRufUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
😀
😀
😀
فووووووری؛ زهره فلاح زاده خبرنگار معتبر حوزه استقلال:
🚨
🚨
🚨
مذاکرات پرسپولیس و یاسر آسانی از شب گذشته آغاز شده است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135851" target="_blank">📅 16:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/135850" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z29o6YODsI8L8xmO_UxeD_hqt6CB9qx7wtQmVxOPb6GlT5kW0ndXvkuBFX9BFhbQpWpnL4IAcodu3Iw_XQ0b-tlWkj_MaUe1IBZUBIolWHRWDzOif70Zh2nPmIa3SKSZteQRRuLrZt_dqihrNYsm986uHCCLRTIubIyOgc2_yi9TnLZdsGMDfF8Co2dK60SC5eTIi1N1RpY3qZjMCX31KasUk_lLtNBoLERir0bHIgRQiWtXxJAIuNhIncwJ5QdZjsgQHeUmmsXUUXbpvaGRNb10qXGa89HgSD1BfEYMGaia-UhC0nZEPbSoEyWHiQ2_YDeu69ltUoQRiFmM70LF_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از ورزشه سه: اگر اتفاق خاصی رخ نده ظرف 72 ساعت آینده زارع پرسپولیسی میشه
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/135849" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
پدر کسری طاهری: امشب یه جلسه مهم داریم که سرنوشت پسرم مشخص میشه
❗️
❗️
پرسپولیس کنسل نشده و بعد جلسه امشب همه چیز مشخص میشه، بعد جلسه امشب با رسانه‌ها صحبت میکنم نمی‌خوام پسرم ابزاری باشه برای درآمد و منفعت یک سری از افراد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/135848" target="_blank">📅 16:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
#فوری
🔴
یاسر آسانی ستاره آلبانیایی فصل قبل استقلال در آستانه پیوستن به تراکتور قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/135847" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
پنج کاپیتان پرسپولیس در فصل پیش رو مشخص شدند
⏺
1_علی علیپور
⏺
2 _حسین کنعانی زادگان
⏺
3_محمد عمری
⏺
4– محمد خدابنده لو
⏺
5_اوستن اورنوف
🔴
پ.ن: در صورتی که وحید امیری به پرسپولیس اضافه شه، احتمالا کاپیتان اول تیم میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/135846" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135845" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/135844" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135843" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/135843" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMOvsN5W-vMlOvOqbi9NRdVQndFZMv1ogg-lHT-aIDKXk3Qb9Q59BgUuWhLktxtRXnppw1ltbUV-OCxRkX9vdXy3lobrLUugrxZtw5pBkjn9PmerZs52WgeJOdZTITybMjlt1lFPKDCyS7ouu5g8QpGSGju_hlcamaiddNEheYyIlnb7SRj91G8YhmvpcAHwrLez_-fhtBM2K6bM0TM2lzvVe5U8HsOqAmU-yHf3byWzlcQy8xqfA_I73ueug2X0PYNQ783xl_ZTHskM4Zg7opQutUlBREM-gcOArxyvCNfSDoPLBUjtJCLX5blJ3UoYXWKxSuPDr7DDM2jwEKHxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/135842" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
#فوری
| ادعای اکسیوس:
🔴
🔴
ترامپ جلسه‌ای در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔴
🔴
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت
❗️
❗️
جلسه مذکور بر طرح‌های جدید برای حملات به اهداف استراتژیک در ایران، متمرکز بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/135841" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
🔴
با اعلام فدراسیون فوتبال، کمیته استیناف درخواست تجدیدنظر باشگاه پرسپولیس در پرونده علیرضا بیرانوند را رد کرد.
🔴
باشگاه پرسپولیس نسبت به رای کمیته وضعیت بازیکنان فدراسیون فوتبال که به موجب آن حکم به محکومیت به پرداخت مبلغ یک میلیارد و ۲۰۰ میلیون تومان داده شد، اعتراض کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/135840" target="_blank">📅 14:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135839" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده ها: یاسین جرجانی، مهدی زارع و مسعود محبی سه گزینه جدید خط دفاعی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135838" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiARCvCwAKis3ScAfWLwJve3cw0UnlvCeKrjH67ry5Xh53jGwVPzbwVCIyS0_wOQvPYxcTR2vugHWoYo7hRlxnblQesNY3q4L_X0nhQSxhot3MGL2TKm31RaVLI78nXaryhg6gOgFZoNLvY1lxe6qcyB6zvELpYyvmC0lSwZs4yN2aib8oTGciuj-ql-54dw_5iaJ8_5h7FW8zpqB2eHbP_YmcMVep3v2BzscC3-RhkKVKO7Ej4f1bFUSdH01gFUrenxHKWmp8eIhbI949ECMZ1VgUfgGlwS9v3Ey9Duwy35GdGGuIWFNAm4En_8IjSKZ6gitoqJpbBojaHKCljkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: یاسین جرجانی، مهدی زارع و مسعود محبی سه گزینه جدید خط دفاعی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135837" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
نظر و حرف دلتون و بگید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135836" target="_blank">📅 12:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_zEi2Iw7sH5I9AaoLqa9JAes6MB9HhPniJYO2MC90uzY6SRUc0n7roSgBX7jmttbAMAKspFd2kqp0_G6wVHgF7T-w0vpfp6DX5Yn0lkO55kNgAVBeHOHo6aRNslM__QTxffdB34GXDUap7qbSMLaMUptuUnQaWjIqN93PU32slmDeEFSw7AndaGjYXVOC5-x_nzckNPZKYNv96QEn90OYuMMEqg51vjX9BKZGh3Vs91cUsE9oQa0jVRYbWyPAp34KTQL5vVd8EG_nDAIZkSm82eIbH1VcgCCZ_cs1DWgUVD1jxBWs5w8FI58kC8qQuswUE4ND9soSHhBN0ePy4VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی
؛
بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135834" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135833" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135832" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKbW57egbHGy-dqHbnkTW9ZzwvLS0xcZfYn2cV0zbm30Ex0io-VC0petcSZztV_yjo4kVqKELwI8_hALyWQqKQxBFbt27FMGZQbcx4mDJmFLFaaoKGeP6-4xd8pWipoT2RPxdcupRyCBJrm14qzK1XfHma-6A3BKByP3acqkUlfSasqs5cIYe3aJpAJEHaO7R59M_iULykCzEEka3zShGL8CbkGinsHJXtWIinSSbcP6uMoC92cJNu-rAYCLfSlbq39dY4TuymdrlElywN9EzseCKHb29BQXOiwpkbR36GAq3PpXkQLhxtSp0EcFxr_D7j5vrixUw_JWA6gL80ijCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها؛ گفته میشه علیرضا جهانبخش گفته تا یکشنبه به پیشنهاد پرسپولیس پاسخ میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135831" target="_blank">📅 12:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135830" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135829" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135828" target="_blank">📅 10:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روز گذشته جلسه ای برای چذب پوریا لطیفی فر با مدیران گل گهر سیرجان برگزار کردند و با این باشگاه به توافق رسیدند / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135827" target="_blank">📅 10:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5ia7UbLkQRUk9GM5VIVc1UQWhbB6Qw26LCvnOq6HdE9A4k6jGph7y_KA1N7BGOBm_xsGRVb3Auq3NSxzbmBInz4tYHHORh8-JSKNXW8EQizkB8DpCFVsFeCvbE9ezzrer0_bVpht6qbRPJGFy0kfBsGaeM2QqIiJKE2dI7tsAna0UVJdgSqWVNNq5bEfvqvyWi3nu5JEUkgKiOUHQvbQYrCEwcwO35wbKj6cT1A6cq_410ptujP_-rzbmY7VQYNKGCqO_GjfepMzIVXd9Z1poA6_SeRkvb-4iJx2SZj_1O2_83gfoDLXJVBtpJv0W3WypDNIlSzkNyJRSbBT3hNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
جدول خاموشی مناطق مختلف تهران منتشر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135826" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
🏟️
ورزشگاه آزادی تا دی ماه در دسترس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135825" target="_blank">📅 10:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135824" target="_blank">📅 10:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
پایان بازی، برتری در دیدار دوستانه
🔴
پرسپولیس 3 _ 0 شهدای رزکان البرز
✅
عمری، تیکدری، میرشفیعیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135823" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
❗️
فرهیختگان: مهدی تارتار با جدایی محمد عمری مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135822" target="_blank">📅 09:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135821" target="_blank">📅 09:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvat9KAHiZIDmZfKKw4_f_y_6g68jjZK3mR2PhRMOm86aIIg_Qusg7MamitvKufkBfnGVkEjZE_nXkr_JAMWrCe-cxd4qtTwCbCa1fCz0u7PA5fnU9r3mBerblSdDYCELAFNzRqriSxeiS-C6p2xGMXs8_NqodF2zr9_d4u1s09Au-O5DcdnYGigbRozKDll--7TDLZh8KFWDMY4GCLTMrSycx7NatMACiLmxqkT3LuHRSyCdY4rnwKxTNjysPTwtA-TGm0mElvlKISEcPVaeLQo5OjwsQaRpEB95fThX-4PwsiCdWb42GNEd5_JqVa7RW2UZbvmQS1puVe1A3m6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با اعلام ترانسفرمارکت، علیرضا کوشکی از استقلال جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135820" target="_blank">📅 09:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان وظیفه جونشونو از دست دادن و امار مجروحین هم بالاست
🔴
🔴
همچنین درخواست فوری از مرکز انتقال خون ایرانشهر برای اهدای خون در شهر بمپور برای مجروحین ثبت شده
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135819" target="_blank">📅 09:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ترامپ : امشب و فردا، ایران را با قدرت مورد حمله قرار خواهیم داد، توافق‌نامه همکاری با ایران یک آزمون بود، و ایران در انجام تعهدات خود در این توافق‌نامه شکست خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135818" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhAV06xw9hhGDSnWdxlLCkptBWOqx6CziqEk80te7mQStY-DhId7xZAY9otPPD3dPs2-6Yx8-neAAAfKAAcWjtTxWsli1DFXmKXG-zEsP3k7MjC-zytpjI95MnRshT_JGYI-eGdG-MS83krRHxYLRd03-P7-jDqO19dg-2rCeCLp3iRq6VdhjpmBLb4wMts5kh4H5c9vV9FUl18wvfBk10PMCz9kZYv0B42ZBvuuGeFDGdzOEfyYnFmgG_IUu8opDRX260Bjgkf8Lrw_vbuYhvJNoaktzB_a8d2znSSLJv6FkS_RcTArgKtZUv3VoOKJPzJDAoZzMLVN9_f-CoWlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135817" target="_blank">📅 09:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135816" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135816" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9cDC8W5yoDjlocFFppw5DU4GAhgblzSc_nYZrrAzIssSOpc-9LNo9XWu8MtedUnIuMbRRbzTrqjU_VXgy5srWd9NZVmmRtSQNx5Ilej1FqyrAChhGXVMBnuzImqiW4nl5i6CPKLOPSPJ5FXTOIaspRL3zRKPlPS2T5qNBES1-IE6ukFGOQIizXT0sUPmz2m6PWCnn_HEBNZ91k-oI8yAnIjjFyIC4cL7qe8UvxX-W57CjZOLCMurmiwIpxS6K_YO0p0MEoPKiShdxKg8pr5eD_k_pK4hQ11pXG_xEUo88TeXEQIZr7NZr4RZOtK6cKXp8WpukSgtRFR4_zrJGJfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135815" target="_blank">📅 03:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
فرانسوی ها ساکت هستند و حرفی برای گفتن ندارن تو گروه  پ.ن رفتن اسپانیا به فینال فقط با یک گل خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135814" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
خداحافظی فرانسه با قهرمانی و رفتن به بازی رده بندی ...خداحافظ آقای امباپه ..سلام اسپانیا به فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135813" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135812" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOltZSCQ7zmndvi4usO8uk-GBbCBnYY26Nx4aeBvs3ySKOPyvpWc59c0Wq1nCCFYNY1FBzebtMezPL5y9ufugdwYnFfW61AQ9Fb4gmZXyZ77Y5ShxO3iybt-ueB3w0Qd9D9Y4_T1s9sQiVIyV3jiiNycc4xNAvG83gKuwTrrJk0YOJpSto_Pt2lJXmtMtskxXJI_UjQdGeTLFeDQq0_5uA93DF6btWIfvUag8wvzGYjftNhNtKboy-fwW3yZ5Rx7YUek_dNWy-h0dPV8WkXE34o-_ouikoXWYL5qdRP4kDhK96CnHHVMniX7bY0ble02lCXRX6VRsKZDxSMh3gs25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135811" target="_blank">📅 00:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135810" target="_blank">📅 00:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135809" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135808" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
❗️
#فوری | محاصره دریایی آمریکا علیه ایران از دقایقی قبل مجددا آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135807" target="_blank">📅 00:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
گل‌های پرسپولیس در دیدار تدارکاتی مقابل شهدای رزکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135806" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135805" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
گل اول اسپانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135804" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
❗️
مرکز مشترک اطلاعات دریایی به رهبری نیروی دریایی آمریکا :  محاصره آمریکا شامل همه کشتی‌ها، بدون توجه به پرچم اون‌ها می‌شه
🔴
🔴
محاصره، کل سواحل ایران رو شامل می‌شه، از جمله بنادر و پایانه‌های نفتی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135803" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135801" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135800" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135799" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135798" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135797" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=oEKUVAE90CHrJzOizS_YVegq361Uzk4TEi9WyL5r3eZExRqBpfe5dw7s-cAkIe71al7WRFpah_CrOc5AWujg-HMblB52mSH52MvAhfGu07b35gDZXVSFc7NK9z1Ho80qktZ9_ULmaNvxy5bHygirogoGVBdIirSkq6fHAyvL8jEI7EwBMXiHAZBO3SNv1Z1jui3_nQ24qjZ7w_Df_c2Dr_KWcwW5z7FZFC6y3oKHGtPscz5cm5g_I3HPGVD_cEbbY9KEtH91c7b_rR0HCc9z38p4t3O-9tdpN7cEU42RwbgEZjh8XesoPynt122aL-gtZ1XOOlct4ew2TrZLYVSBXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=oEKUVAE90CHrJzOizS_YVegq361Uzk4TEi9WyL5r3eZExRqBpfe5dw7s-cAkIe71al7WRFpah_CrOc5AWujg-HMblB52mSH52MvAhfGu07b35gDZXVSFc7NK9z1Ho80qktZ9_ULmaNvxy5bHygirogoGVBdIirSkq6fHAyvL8jEI7EwBMXiHAZBO3SNv1Z1jui3_nQ24qjZ7w_Df_c2Dr_KWcwW5z7FZFC6y3oKHGtPscz5cm5g_I3HPGVD_cEbbY9KEtH91c7b_rR0HCc9z38p4t3O-9tdpN7cEU42RwbgEZjh8XesoPynt122aL-gtZ1XOOlct4ew2TrZLYVSBXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است و او زودتر از ما سر تمرینات می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135796" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
جااااااااااان کیسه سوزی باشه؟
😂
✅
جلالی : دربی حذفی خیلی اذیت شدیم و گل عالیشاه خیلی قشنگ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/135795" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135794" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
❗️
خلیلی :
🔴
دیگر مهاجم جذب نمی‌کنیم و با سرگیف، شهرآبادی و علیپور ادامه خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135793" target="_blank">📅 21:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135792">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135792" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=EcykMu7MXzIvntxbbZWNkhe5j0XMZU7d8iPbZ5cV1sYO8mUDzkdO0ip5soTXArtZW48p_MJ1YR172LdMGK--h92BKfy5HsMzTQd8Qe1A_1Ikmc1-Z0c8Txf1Fipi6m8nCIWyJTk2nJqp-Zu5--xEACprEs5WUmdeDMBZWE83Zm72Y4hu15BtDHXia04lA7t9etlYEacnAaaabszzLgzkATDigKeALjkgtA6c1ymWkgYqRGX1PwQp1hglPRut40HUXKaPEOnHR13P_8w-grdzYVnauKRfJ6a-sVdkjvrcUCeEE53z1pkj62WEnv4xEnuHDaINEDbbvX6qQOky4LpgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=EcykMu7MXzIvntxbbZWNkhe5j0XMZU7d8iPbZ5cV1sYO8mUDzkdO0ip5soTXArtZW48p_MJ1YR172LdMGK--h92BKfy5HsMzTQd8Qe1A_1Ikmc1-Z0c8Txf1Fipi6m8nCIWyJTk2nJqp-Zu5--xEACprEs5WUmdeDMBZWE83Zm72Y4hu15BtDHXia04lA7t9etlYEacnAaaabszzLgzkATDigKeALjkgtA6c1ymWkgYqRGX1PwQp1hglPRut40HUXKaPEOnHR13P_8w-grdzYVnauKRfJ6a-sVdkjvrcUCeEE53z1pkj62WEnv4xEnuHDaINEDbbvX6qQOky4LpgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135791" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=W1n3A0oQ4uUN2MBEDvdAArUdyrwglFEahUsVeKIjkcL5_j13ry9NbD6rMF2Aa1zDO2Oxb85Go_YemO76BYw0tUpoH3nAKuAUqgBKQK3Nt-qsj7iCPNigxvUl07b_gZ_eKSo7GndR1BYV34Rqdanv7RO4dDMUF38hcwFuH4vjYwns7c-RjC2g0PB413hpAWyFbkl9ntPLwj6V1bcXCP60YTXc4dF9HlYYFu3A2iLGN7b1JLzqhg4rAk4WGL7OzLgtWRfNf68CAkMGHiXtnL3TsumSF7bJrxoaRFtxUeUnb1wOFZ5u9YudaiPN2awiBQiMPHgj8ZBdHUZ6E0X6IALpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=W1n3A0oQ4uUN2MBEDvdAArUdyrwglFEahUsVeKIjkcL5_j13ry9NbD6rMF2Aa1zDO2Oxb85Go_YemO76BYw0tUpoH3nAKuAUqgBKQK3Nt-qsj7iCPNigxvUl07b_gZ_eKSo7GndR1BYV34Rqdanv7RO4dDMUF38hcwFuH4vjYwns7c-RjC2g0PB413hpAWyFbkl9ntPLwj6V1bcXCP60YTXc4dF9HlYYFu3A2iLGN7b1JLzqhg4rAk4WGL7OzLgtWRfNf68CAkMGHiXtnL3TsumSF7bJrxoaRFtxUeUnb1wOFZ5u9YudaiPN2awiBQiMPHgj8ZBdHUZ6E0X6IALpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: امیدوارم امسال بتوانم دل هواداران پرسپولیس را شاد کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/135790" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267f8866.mp4?token=Fp9sGGVSaf4xGpvK4J1ENzioVrfRuPWBD-WrXy9aPDykx_51EzdN96gmaxSgYZWdtesBFA4YXWpKhGoJN2Za4ky89JpYfWaZ0iPfTspkRZ3xkMjC9zQISoxDtsRD2gPrMfiWsNHt9IVLtzhAq1tCB7rKk7iKocCUbHF-A0alilJjS1OL1DkiYhDzpml5K1VqEFkq_oLKTBu2u3WnxUWSjebVCh6lpXa0uvDzI4THJyB04ObFk3iTpMIsGtXbxUp187wM1rIw9021Swy8HP8NLpPGN_PoL4BU83tDXn2Z4QbJZHd-Hho4BbKzK-HCnwnzKnC9VjdXoauiORXuoqR5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267f8866.mp4?token=Fp9sGGVSaf4xGpvK4J1ENzioVrfRuPWBD-WrXy9aPDykx_51EzdN96gmaxSgYZWdtesBFA4YXWpKhGoJN2Za4ky89JpYfWaZ0iPfTspkRZ3xkMjC9zQISoxDtsRD2gPrMfiWsNHt9IVLtzhAq1tCB7rKk7iKocCUbHF-A0alilJjS1OL1DkiYhDzpml5K1VqEFkq_oLKTBu2u3WnxUWSjebVCh6lpXa0uvDzI4THJyB04ObFk3iTpMIsGtXbxUp187wM1rIw9021Swy8HP8NLpPGN_PoL4BU83tDXn2Z4QbJZHd-Hho4BbKzK-HCnwnzKnC9VjdXoauiORXuoqR5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135789" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135788" target="_blank">📅 21:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
یاسر آسانی قرارداد شو با استقلال فسخ و ایران رو ترک کرد / فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135787" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
خلیلی: ما اصلا کسری طاهری رو نمیخواستیم و از لیست خریدمون خیلی وقته خارج شده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135786" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
محسن خلیلی با کسری طاهری تماس گرفته تا در تمرین امروز پرسپولیس شرکت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135785" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
بیفوما به‌خاطر کشیدگی کشاله هنوز تمرین نمی‌کنه. بعد از اینکه برگرده، تارتار کیفیتش رو بررسی می‌کنه و اگه راضی نباشه، توی لیست فروش قرار می‌گیره.
✍
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135784" target="_blank">📅 21:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135783" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
❗️
برگام
😐
🚨
علی نعمتی هنوز با لوسیل امضا نکرده و پرسپولیس زنگ زده بهش تا بره مذاکره حضوری کنن/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135782" target="_blank">📅 21:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
به خیر گذشت
🔴
فوری:علی نعمتی راهی قطر شد!
🇶🇦
✅
علی نعمتی، مدافع فولاد، با امضای قراردادی به لوسیل قطر، تیم تازه‌صعودکرده به لیگ ستارگان، پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135781" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135780">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135780" target="_blank">📅 20:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135779">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135779" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135778">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135778" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135777">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPXhkLKcQQ7afdqyWIllg9NrkkRzkpwvDNRBWWwb4oGNbsAuwCWgQNvbt-yZuVCbsaz78wd1zgBEiRfEuofQuscQ7DB5xSz8xHSFBwCFFDboGf_-Ttp42hIfMhLCfbsw7l8_2PaBJ6iR9BET_77j00udK5nPyEUvTBfg5sWT8CBAnx4xgULsRnloIfGNmu5GOmrnMnBVKM2NyxdXS_IpC0P93an1Cwq3lP3LTWbZMGGnHz89ELrxvEyG_jnaG7LsBBae4mFNVDsv8ZX6e2G33JfN4bObdrrGEHI8TqGMoSI1ScnmM-YRxMcUDD8aHD87nQeBC9TMeNVIaGo5JNJR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135777" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135776" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW0c_RN7it3OCPtAr_YxSsK-NQnW65IVH8_7ts3sG08hc6VUYqhNaOqHfLvHSk1BFGmHbv9Wa3E5sOuVIAX1r2UsamkJ8Gbk7y4JhgZYiaJUWHsojGeTrFkFZ13M0vk9Eo3ARCG8K9f7ucApvnEz1GJLQl1Z8u408Accg6KmXSG2EGpW3DUt0M1IcqwrnxQ6fiw5nF1ktot6IVn6U3Fe3StTmcWazzNK0ByChYhXtlNsKxhvuT-YCuiW1IgEvPHxp_8NyqyiFBW294sDXdqPSZWUFoW-eW6CDO9-i9PC105T4Lyq8L05sJk3ZUZmeGIcGkkqaN6MQZjlnZVAxuYG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
✅
💵
✈️
@Bet_Giantss</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135775" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135773">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=t_-d9gg4bdUQwTsghIBZbyJi4z1LJvycSQirkRLGRVQPqaGr24qbFX3_HH10e_3VwkDik6V4Qv79uqRZ2jmFSR3kjH_-kNAzjMWKGmYaM7-Pa_ED9syWRxDhkg3GVtAwReSvdtjdw-o0iOXtugJl7QLjGBBRK0wtWEdAbDbDhpSTLKYM__7me-mSc9C89Lr1qiErxIqCae8ERLUCaisJXiu9iPdDHvn-RAlyFXOhxkl-0bXTKHrdxyt8ElwYwng7KFQttmLXPKHVnQ76zcfylkkS8EReHDDT6ZFmwuQXQpj-CHwVwnfu0YpP6WGGBDNuqpiSgUi7Ad00KT6XVxbZfH1IweuEVPyaY5lxdPFugduJeok-iYaBecjouBsNxK-0QmZQpsMQUlZaXtYJtI8Yxf90y2YUaxO1eh2hLSJUyCm4cU0daWizkyDOurri2SiZBWp23mlTDCt8-iE-X_LiVYs0x1YPTSA3RRGr15sF_ejB9S34DACQA1P6o3xmKsTUEWkXm9G118QBv-ACrb9uu20XIjHRWLrSepS2OZNKxm4cp-ctdcuauo2f9OTicqNv4aCFbm4EVBVwvCZuqpvAId6bPAzdw4Kobec2hk_dr7EnLyYWXYl0ZEJ8Pz2kNQ0V1i5uUB1iV4wuuwNMhq_FeTkEeMFBMskJqsRPqB0vsfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=t_-d9gg4bdUQwTsghIBZbyJi4z1LJvycSQirkRLGRVQPqaGr24qbFX3_HH10e_3VwkDik6V4Qv79uqRZ2jmFSR3kjH_-kNAzjMWKGmYaM7-Pa_ED9syWRxDhkg3GVtAwReSvdtjdw-o0iOXtugJl7QLjGBBRK0wtWEdAbDbDhpSTLKYM__7me-mSc9C89Lr1qiErxIqCae8ERLUCaisJXiu9iPdDHvn-RAlyFXOhxkl-0bXTKHrdxyt8ElwYwng7KFQttmLXPKHVnQ76zcfylkkS8EReHDDT6ZFmwuQXQpj-CHwVwnfu0YpP6WGGBDNuqpiSgUi7Ad00KT6XVxbZfH1IweuEVPyaY5lxdPFugduJeok-iYaBecjouBsNxK-0QmZQpsMQUlZaXtYJtI8Yxf90y2YUaxO1eh2hLSJUyCm4cU0daWizkyDOurri2SiZBWp23mlTDCt8-iE-X_LiVYs0x1YPTSA3RRGr15sF_ejB9S34DACQA1P6o3xmKsTUEWkXm9G118QBv-ACrb9uu20XIjHRWLrSepS2OZNKxm4cp-ctdcuauo2f9OTicqNv4aCFbm4EVBVwvCZuqpvAId6bPAzdw4Kobec2hk_dr7EnLyYWXYl0ZEJ8Pz2kNQ0V1i5uUB1iV4wuuwNMhq_FeTkEeMFBMskJqsRPqB0vsfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شهاب زندی: برای فروش ایری قرار است هیات مدیره تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135773" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135772" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135771" target="_blank">📅 18:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135770">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTXQVBByox10JXOmS08VzmORN0JwCYahjhK9pZ81MvZQ1j4MqdiOkt-IoOSYY9XwMsRsJmTC2UxiuesSlEcZ76BL5GNMZXCvk4NLBr-680QcIK5SRQ_in4KI85G6WVpQ4ZlTi6knnSXbC40sPtswT97I9Lkxk4aZmttonVKtNs7xRKIX55OynowBErcAnx0oEsVndKrTgsmzY0N3gapQULQmK2-N2VPWc4ZwAKudrVF6MeEdCoLvhf7imxU9okrQg_HROOhHA9C0jkX4bgubVpFCT8gCO9Hn5VeWB7VOAUFFv5uO50iFaglbbMcYvn4VE3aPOdeVfzScOuRt1bEiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135770" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135769">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=u6H6_9jd1FfEliGAd_M-CxGdcx2L6b3DYjGDbi492ZqvOtQRoxxo7QsV3ocd28C701AcrGIqSqUQ1mzDMrOEda9Q_PC6inYU24MN9f3G839qPpOssIWh0z7hkF5__oEQXQk3Om2lUsu0vZp0cykg2l-wzEUDvadt5bIpJuZ_3DHYp9CRSw5LChcwoKTP25DeQnY449J5xWN9FGJAwc0SqxPQ1dPACqt8ehL4r7yC7jwv8pFxkaT2sRyxB7F2_jjpvtKTbCYvmugzQKrszSIfibGw8JpNa2t6c6zQUH6uYVhE-R8cUc9rsTZPpkPH5zPlVUowrTXyHFikAdHX_CdJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=u6H6_9jd1FfEliGAd_M-CxGdcx2L6b3DYjGDbi492ZqvOtQRoxxo7QsV3ocd28C701AcrGIqSqUQ1mzDMrOEda9Q_PC6inYU24MN9f3G839qPpOssIWh0z7hkF5__oEQXQk3Om2lUsu0vZp0cykg2l-wzEUDvadt5bIpJuZ_3DHYp9CRSw5LChcwoKTP25DeQnY449J5xWN9FGJAwc0SqxPQ1dPACqt8ehL4r7yC7jwv8pFxkaT2sRyxB7F2_jjpvtKTbCYvmugzQKrszSIfibGw8JpNa2t6c6zQUH6uYVhE-R8cUc9rsTZPpkPH5zPlVUowrTXyHFikAdHX_CdJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بیژن طاهری، سرپرست کیسه، بعد اینکه یاسر آسانی به فرودگاه رفته و ایران رو ترک کرده، رفته راننده رو مثل سگ کتک زده و گفته چرا بدون هماهنگی باشگاه بازیکن رو بردی فرودگاه!
😳
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135769" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135768">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
شایعات؛ جهانبخش عصر امروز با مدیرای پرسپولیس جلسه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135768" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135767">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ادعای فرهیختگان: محمد عمری از لیگ قطر و امارات پیشنهاد داره و ممکنه باشگاه با دریافت ۶۰۰ هزار دلار از این تیم‌ها رضایت‌نامه عمری رو صادر کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135767" target="_blank">📅 16:53 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
