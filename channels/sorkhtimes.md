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
<img src="https://cdn4.telesco.pe/file/gdnT9a2Km1EtncIAXjVOnE6Lc0Ze9DqLecu7qYnCJq-PKi2RzFoEVunvyIwdly1cOkQRqutN85nT5l-ZCFs3Z1yLK5iCkwvdiMBCLdsphUX8fPx-f2ORJxMUuogRZ5icsqPUqCGO-VpzbcjhYQgugMFup_SoEQLz5XPfEjp4m8vdUR6ToyDoYD19W26lZH_sAwQknm3DiKNF2GVmocG2hqjG0wOGpQQFK84RDI-QXtjMwgIvlrIM8CfeILo4qF4ok_cGiuNCisxnhjkVc-3nnwMrMMmtJOIdU84VaSl7eZJS2wjlxUBanT4LgyWljta08O9vOHQRliKp-JALWb1l0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-136934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SorkhTimes/136934" target="_blank">📅 18:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/136933" target="_blank">📅 17:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQOps95sVyd6RVr3uwlPUmmhQ8mbAs2dou5jX3o2w4oKmPfTiz3xLL3Abz26hrrBRNrx1-yOrl65AyuOwHT2958wnWkgMptfMvfLPhd4KzJcIE_tvdn_ELejjaQ-2FWE2JjNFgJkp7dgBWPDx9Ulu2LkHLRXMs7ZvLqCwyny5wWPwRPRmluFit2p6ONbgyuustwlXqSVa9_XosXzYQz7sUhppF6YSyY-UZwHywVK7MruO93ND4gh6o7E9mbijqbMzUqc6SKcsW8tj3Exm4FmTmojtAlIZGw339gNwSoC3Bx1ZVLc_YaP_Tz8p_eETFJgl5qDAdbAOU3GYS2wAs9Cew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/136932" target="_blank">📅 17:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/136929" target="_blank">📅 17:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/136928" target="_blank">📅 17:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/136927" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/136926" target="_blank">📅 16:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⏳
⚽️
پوستر باشگاه پرسپولیس که خبر از یک خرید جدید می‌دهد
🔄
به نظر میاد محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/136925" target="_blank">📅 16:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136924" target="_blank">📅 16:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpusU_zH6AKFacK4Cu3B0WKS-iJumvJUKBk8RTZ2fUaRobvHcKe08KRP8_qVU4hNdfWedEVvEGGtv6OpLd02FEN96PhoMnL23xMwrzeI5KNR5OPocH6FQBo2scwXaQRBGfUfjUizhvm6th8FVmoPqActB4WsVGJXj8mj1kMaNEwjIK_09XPi8fCpFPx4N2OwUC8wVQkEazzCz40gEgrSdZgMsaDiC5rPwErgBvk-USB2JocXsRZS38oqY9o_iH6J0F4Njxz23xBe2elEO9Ju3Qzze3P-rnZ88WNtKqv1HfIHv95E1907hv-eBE-msy4whMPNgbXedbw4EthWrYTuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
⚽️
پوستر باشگاه پرسپولیس که خبر از یک خرید جدید می‌دهد
🔄
به نظر میاد محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136923" target="_blank">📅 16:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136922" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡️
⚡️
⚡️
شروع قرعه کشی لیگ برتر تا لحظاتی دیگر
⚡️
قرعه کشی لیگ برتر تا دقایقی دیگر آغاز خواهد شد و مشخص خواهد شد چه تیم هایی با هم رودرو هم قرار میگیرند رقابت های حساس و نفس گیر میان تیم ها امسال بیشتر از سال های پیش هست چون لیگ هجده تیمی شده هم بالا جدول هم…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/136921" target="_blank">📅 16:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/136920" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚡️
قرعه کشی لیگ برتر امروز ساعت 16 برگزار خواهد شد  ببینیم دربی و بازی با تراکتور و سپاهان هفته چندم هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/136919" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💠
💠
💠
✅
پرونده ایری و طاهری به حدی جنجالی و پرحاشیه شده که مدیران پرسپولیس فعلا هیچ رغبتی به توضیح ندارند
🌀
🌀
عصبانیت هواداران هم مزید بر علت شده تا برخی از مدیران ترجیح دهند اظهارنظری نداشته باشند.
🌀
🌀
وضعیت به گونه ای است که حتی جذب محبی هم موجب ارامش هواداران…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/136918" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
در مجموع با توجه به جذب نشدن اخباری،رزاق پور،اریا یوسفی،نوراللهی،قربانی و...از دست دادن میلاد محمدی،ماندنی شدن برخی مازادها و متوسط ها و جدایی بحث برانگیز پیروانی و برخی بزرگترها، اگر ایری،طاهری و محبی هم جذب نشوند نه تنها نمی توان به باشگاه نمره قبولی داد…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/136917" target="_blank">📅 15:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/136916" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaarTEq7b6zC086JZB4TR8bKkI2qoOdbtSgT_nYSUP_AXib4EyWzE2wtjU4InrLH6XeZfzOSQkZ2QWP4daQQ1Jm3NQw8KPOc-aJLlKADxTZYH2BbEdhM_rqvRy5NYTfIPy0z7IBeEKVloHq2dZ8fR0kQy96wZ78H6bE6wWVTz6Mi1q4D8ltO71-sLOX7noUJT5x894FNobY752hR4VmgoaU9DNcxqPNGFGaitMM2PTWCxYHTbfpbupvzMFlRBUy5nQ9UJeIW0w3Tq7Hlpz8kiX0F6hN7Pj3EDCfm_XcPzrE4RxxpEdXh9_yYTQZ7-OsVWrgiDXLRCOzC9rQ5S5YX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
منهای ورزش
⚡️
⚡️
طبق گزارش‌های منتشرشده، اپراتورهای تلفن همراه برای اینترنت بین‌الملل ضریب 2.7 در نظر گرفتن؛ یعنی اگه کاربر 1 گیگ اینترنت بین‌الملل مصرف کنه، 2.7 گیگ از حجم بسته‌ش کم میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136915" target="_blank">📅 14:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EikYOt0c3vauYWK8VyOwhybcEMlzC49_qnGac-qUHYXH8Dcji20oAiS5lyFFhS1M7_sUNp0N9Eo8x97A-Uc7uc4Cr1UVGSluZBCl60TS7xIEV4VZwuEZFPR56RA-O9YwxHVKOyK6sLVm7kTbiQzq2ekjlsvKQrethG-4WQ9WxqzAXnOEyUwDf20ryWpAvG1MEBNqVWhMHo3hxz-DD4ekNzEkkD6gq33N68bnZd5-id7H67gylVRWJenqwPLUnO2KdrAQhZ8KZWCIi5P2m__qtVLd0MXXFvgRHZJVvcnBG7zzztu1xumTOhGLcgym_imK9UzVIbO3WvRBfrwwWjujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
از توپ جدید لیگ برتر خلیج فارس رونمایی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136914" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
فوری؛ قرارداد رضا غندی پور با شباب الاهلی با توافق دو طرفه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136913" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136912" target="_blank">📅 14:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myM71V3cq92mXQA-T8eQmO355BmIbSX_bkG3NB1kxV29aDqJHURDGMiysuF-ayD33m45U3eDlHFWM4P87JRlHfjkhLPJccZAnw_3SiXHH5UkMRznPv1E6Yh4SmVSMzeJjWRG4nIFpaj6b8mkJ6UPJn214OyYUNSdjwvYNC-JdoUh9_zxO6IsmvpOvKmR2UwaABAKJsS9nQd-5nhiMI9i1pE4cCyURYvG9RCvpy3RWUR9rvNo14-xSUrN2Y40sgkL_Y7z2KzDzHQ8y6-dZfJOa6ukAlOl-JuW3nlAt_1_AyNWc2urcXvFUvkvw9vhktWb3fEfk1_VwmCnbQ5JfVwobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136911" target="_blank">📅 14:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136910" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnsRhn8Dz5DoXPrBjxYmgvHn7hhx4OtEsmm6FmWrDd-srF84k8FMD3YYBKxtDjgE1vQvAvkOuu6k4hYqve61oJtwaSmf2tPyHMiWtNXmGci1sL83ysH2tJLcYmOysH0tHrcpejKo1PGgu8l6FbJ2ZEcuLXYU5O8MoglQXvdhnudhn2RGxpW5GRFxcfyaoaib9CmeCJD_IL4_dwP2oeMvdqLkMxcdU17uO0iB7Vde8U93rBDUv5zrzGGz5HeJYpQDmsHuVoZ3AhYKMgHyUxSRGhG486UlcN_1ACVqPUSoXCxLIXJUmuvp5mM2Tu4XTsjfbRO4yfpQDnsPWMtPffw0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136909" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
گاف نقل‌وانتقالاتی چپ پرسپولیس را خالی کرد
😀
فرزین معامله‌گری، بازیکنی که در نیم‌فصل فصل گذشته از شمس‌آذر به جمع سرخ‌پوشان اضافه شد، در اردوی ترکیه حضور ندارد.
😀
این بازیکن به دلیل مشمول شدن برای خدمت سربازی باید دوران خدمت خود را در یکی از تیم‌های نظامی…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136908" target="_blank">📅 14:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cqaqyon4O1Q8cR1a2fUojLsefxqiZfOdmFNS0ThgkHVShL14ktb_0onWRG7cnJ2WPoR833vhUJWLgAIAvSERCzP1_tqIH4EstYpGVkXZpgzhiYb1f2-3RGQ_ZzMRxj9LCQM67vV7-vCNSxqJGPyOxEmoHAUl0oIgjuMfx7q6DHpthXQLTYkMA_1GA0QOnaqfSeS8hYha_TkIyDMzFjk7-2qonUoUf9--sXFUuZMDLXe5u4bF2wPGE73rFwxxCOuaRuz9CfyepE4lv3RFrg12oueKIEVc546Czkt5zF8B7p6rn-SJ6kY8T01rB-iLA4zghWUZu7BONDqX5EfQKweoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
-
مزیت روش ورود از طریق ربات:
👇
• ورود مستقیم به سایت
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/136907" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAiRWDZioq9Hb54ygOoY8xoyP6hvKKk3Qucz5E6nCvNfzZKMqM9COuObHtkvG3skSPIc7u_jCUuIXFordslLjjeOFj62tZYSA1arQq5PE-FFvB746qSlNg2M5VtPdTtEsa6ibBvagBfDeIekTrCmPvdNveow421si7sjt4RZZtH-u0yw3EmwLsZVLl9azd0e5Vm--fVdSVZsGP1YAJsdpA0YFYE5_ne6xa8AzZ1i3gKPf4R6KN6yK7gvBk54iVNIIM3YPp1HUw7npwce7DaMfUp_xtvmDJdQsby2uSfwjZ3jYfdR5R6ATVDibqbuj-7Wkaqq2ETuXN2EM7hcfUhdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
زین الدین زیدان  رسما سرمربی تیم ملی فرانسه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/136906" target="_blank">📅 13:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJOVjydLFhTuMArXaeUEo-ym9rjPRzEyO0bh-YfbZkRYdHn3RLStChJCGa7o3Bx9hLi3mWqqauFG9Zy8VTQNSRyS3reGe8mK1eKRe6IF3-fQUTY0GcmhfdtYL-88HK60DOZwLDbqHUkEBctVKAsQ0tUkJLErr5sog9utGkbaiZsPgKJW0AmZT4Nvscz1it5hp0T-QBj3m6nZ9qxUd28q-67Bff5jou0e1skF3AMPRnSceC2td03jWosge8m4ivKeSzsWqVixYl4xisM31KkCX1QsL6bu4lkQxO1mVRPoU2rqireJx9FoFwxyN_XYOypbRGhFZ7YeRX12qCerz91iOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🤩
باکیچ؛ مهره محبوب تارتار، خاطرات ربیع‌خواه برای سرخپوشان تکرار خواهد شد؟!
➕
مارکو باکیچ در تمرینات اخیر تیم پرسپولیس عملکرد موثری را به همراه داشته و تبدیل به یکی از مهره های دوست داشتنی مهدی تارتار شده
➕
در زمان برانکو نیز محسن ربیع‌خواه مهره محبوب این مربی بود حالا بنظر میرسد بار دیگر قرار است این خاطره برای پرسپولیسیها تکرار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136905" target="_blank">📅 13:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136904" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136902" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136901" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136900" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136899" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136898" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136897" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ7bPTxsBCxbNwSAQ6WMMT5PG3r2YZuBAbQWHWJxcC20jEMOOASOUyVm4de1-NagCqm-FukLHkDP4QhRpWOehUhphfk6fZLZ7nGkSglsh7Lm5QrHnI4ULgsdoeuDhRSw4NgPm8MwKONAVefyGrpHwyMKE7qm5cdGEzrj-mQqr1XkhDn1o2x_KCsYwb0ufB6qu6MyM9Dmpj5thD1LKUN_d-aJMM1AOky1E_t6HsTITe9aYOj-PzkH9V7u3ci4faX0uGEg5ZdtBUcYBDph-Ek02OK_Biq5MAXOvSnn3LxlN15ev2cdI2jbVKMhEYv0x2elO_B9Vn9rqkY1u2UJcfBNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی
؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136896" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF3KcGQ26YJjgkSOecfadPgTZ5eNUq33YLPBAZP-KFfLOkZcC2R1G5Sb9Va-rGuV6evfJ6XWGHK2IQh8NpLSvb0KIQ8LX561w459q_eA5kyruJTJ9YFgDamUzIjPd78bc-oMHWpAxDO72OArONo57B41opGU4r0U6MutUdfTVYm6dl1_5zHt5r57ysWSuxvtlm5rCUN0i94_RTcUBa4IW-_OifaoicjRI3XjWKWDnaQYAH94DNL2BDyBbBFa8w0BySR5GmMwt31-qYbe74AK8YfFJ_LgsNCoAYmk8Cel2ls-wKEWBKRD7P_S1Nkp1O9QF77WDXnQGQPrKfEQFAUMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرسپولیس و الاتحاد کلبا به توافق رسیدند و محمدمهدی محبی بزودی با قراردادی ۳ ساله پرسپولیسی می‌شود
/تسنیم
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136895" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nUre_WzJbSsZ3F4Q9rW-XIJbWlL7_5wqmmbq4GqdCclLc7lX_9CQ2X0e2aSEDTq7Gum2oJWDkHYmSR1vanLmxHE3WOek-1mFOdlgb2gEaeHUyMNNsHQ6yhA_sjog4p58Xw_pxPAfB3Op7rT-3KXyCq70G8bc6acd8WcrGrPD9rnB16mkUbSAhHvAK7W4TPMlvhjakcVMwkjYU5lGWKVDHKYgMEEYBz7X1kJCQgV66JxBsNxCi7VkW_1Z1bNRyPFRyc3tBtC8NvJlQvWpkf3PxbrKLEKFiC_q4gnu3qWT6L69NjK4aos8LuDec1dn0gz2_ilwrGjYJeepkG87PKAywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136894" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uahXPRw1hPIUIZMDjxT4V2eyAsTvRPP5fAB7qE9P5GPaQH2I3mPpQS0WZDujiFeQAePSggEWGW3sSVR_qfKdaz64SlT9Yrf9AqC-g1l4VY8DNl2rwhil-NGhCiTWvC13nYzVloXbfVHHnl_auVQJIV3JRYCndr7sDEW0KM2SePAok3n_XhsDC27EuKV3DnNbx3djuzJeq2-1_RWYYmkawRx3rlrvjb3IkfQA2g3hpermcrrVIy2xeKo5WYRdeS_R6uK-76UalMxmA4u5PkxaOLkq0a65ByDwzXkDYNgeAcpQliNROJ8R3xEMc6BuObartEDJ3GmkQiKf5CqAsxukGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری؛ طبق شنیده ها استعلام باشگاه از وکیل خارجی برای جذب کسری طاهری و دانیال ایری امروز میرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136893" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136892" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136891" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136890" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136889" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⁉️
⁉️
فردا شش‌ مرداد حوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/136888" target="_blank">📅 09:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔄
⚪️
🔄
#فووووری
🔴
باشگاه استعلام گرفته و فرهان جعفری تا دی ماه قطعا سرباز هست و نیم فصل قابل دسترس میشه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136887" target="_blank">📅 09:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic5wObw4kpgvKov5Al_s4W_wkBPBbPGMiOOuSVjw7s03fzR8gV5KdjgUi7AxU_t1MgJL0vUl4wwSbJA00bwDF7pdj_juwVECCiw8ZJaIsKshG48Z-WIfBvWvt7pQBprBMzBqvh6nnc4xricmx-PhXVwDdwZ2A5OE-rStCDDDjBmwgbrviXeblw-PTbCX02jARtbSL2kAtIebBsKS4OWQbN6QBNk1acx9vO0G_nMiLy6VzwbcifmYW2T7RM9niwo5BNT3XSwvSoiw845DgwsCsr5nqJSBvqGUfPsvYL0XpBUi2VxriBEWhJLUGapuWkJRu8PvJ-rMGf9KD1RqR4aBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136886" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnp3VZqK__h37aDTbd_p2gdOH3PU5MT3gh9MdzsJ4nse-M4MGBXlO4G6Q6Boi1nJLMp54Z6Haucb-N7o0qK2aJuKIJQh-TB7m8s8P5sPPASc50K7RnhUl1U2of17C2iENQ47X-KyLMBWgoJSVO0TJuVTAGWXlKplErdGIpAEbevpfiFQeP-n7AmiM6zKv6evvWFLtu7dWnmIGKRq-wsBn2okBdEXSKw3RuluB82klN46n_YQhiKNFDooo4EUM4NE3lFxu64c5hKI-JN2918kHYPYqb61xRfB3bBxQpETT54hp-TmyTOhuYX73wuG_Hqa8j8pM6zN0lbRRpxwLDS84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
⚡️
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
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
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136885" target="_blank">📅 01:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136884" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136883" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔄
لطیفی‌فر فردا به ترکیه میره تا به اردوی پرسپولیس اضافه بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136882" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136881" target="_blank">📅 00:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔄
🔄
تیوی بیفوما در پرسپولیس ماندنی شد؟!
🔴
🔴
مهدی تارتار اخیرا در تمرینات پرسپولیس از عملکرد بیفوما رضایت داشت و به مدیران این تیم نیز عملکرد بیفوما را گزارش داده بود.  با توجه به عملکرد بیفوما در دیدار روز گذشته سرخپوشان برابر پیرامیدز مصر بعید نیست که این بازیکن…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136880" target="_blank">📅 00:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWuVpf-Ka3esAGcG6cc18ZucIM5e6Hcs766UEq-chWvxNIe71CqCmGvGccMCuWkpbFDBY1UGoHlaPOx6VNXJwDSKEbYZtpfREhZlMRsy3QJ-ZofqwOtWDOy4EZXJckmwpPewPzrn2XYmTawP1_l5XYV84h_D1VNsVnme-fi2eGvAFN6wTmJd7sHE2CQXWkMbV1DjNylcegXgC19xNMZUFL6M_0JPFJAwbKgmfh1DwZSBmBbJTKnyxTN52RjPsvnR3jRuqPMxQjfaQYvYnNDMYBGJiKUnjDYzyhfgvQ76HDBL6InviJpOQfoIVbGNVuyqURKNQ5fBwpiXet37jqMaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گویا رامین رضاییان به خواسته 200 میلیارد برای
هر فصل خودش رسید و در استقلال موندنی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136879" target="_blank">📅 00:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚠️
⚠️
قدوسی و حقیری: مدیران باشگاه دارن فشار میارن که گرا بمونه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136878" target="_blank">📅 00:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
قرعه‌کشی لیگ برتر ایران فردا انجام خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136877" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWAvITtBec2SmxL1SlUxmtcVfRhXwCdYh75CHoA9P3qB7bnc60hYY1-oI74ae7EGFW3_2DPzYRIB9y4OTf3m_yDC0P23AVVlQNlz26-XxOiRIe9HsrXJ7HpppeuF1SzVJtOQp61avCXMnpHEDzI_KNZ3zG8yAFsPR9-C0qt8fC3J17zvGZfyFxvMNAqx1hTmPQdD1SH2lF9vxFhleN5yVyGfu0zPUhJ7Yl3vVt76ycOFriP4f4srCbbowCP1mGcraQXHWq-84SLNDUaEBWFlcJlG0gEuh8kgXV8CnGtSVLaCzi2vlhblt7TNz3fUy8b2hR02XfP8rC9dfDRCUXS4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136876" target="_blank">📅 23:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند  #ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136875" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136874" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6YbRfLVulZnVnByF3eP23mwXUgwNP5tog3jRkiowrbZyhVG4EHY8Y81Po0RTWG08u2MRvIkYDHKlryYHSx7BZOBls1mXufoH6VWnYIPqVyGAjD2ZYt77OidF32pP65NnRegeH8Q4GN8LoM01kX6CQJC7rKmuCtxtlDNW0e99jMOAv89AeuDpAdp9ZMnfIvT8kzIGflNw-94sKpSIPYuJ9FMgpgv5anplCn8LmHVjFTVIgqVyBHQ_PlV5R-1_wwuhClRu6hwxuwCzKvMq2B8CbDcmeDWO3hMMfsDU1CQGUtMxKBlZbMNtZafCq6YPHQhmVId5snP4eIT867FkKedvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استوری حسین قهار خبرنگار حوزه پرسپولیس در مورد ایری و طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136873" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
گرا در بازی دوستانه غایب بوده و احتمالاً با نظر تارتار جدا میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136872" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqe-Rtufc09g_HunBABa40JXfS_AhB05WtIO2Kqy8If2OEhIS9ErkiXuenGmGKa0Z1IpLeNF_MSTukHimj0TVE5m2K7fcv-o0bUKWKN13bERsEEhr0BPImhWbfLbfecf8fwZ_XfWPPSv7fcFzON8TyYYIelscCwzCOcy1jR3IEiNcO8SJh8izM0uaXbERxuVH4I7ZfbY2PqPKrtD_XKQ7QkoDy-h_Qd56tYcnwe-ejYVPAWREi7h-4VelQnwBp86o3AVYXdsv0JPL7rEBckr_xEK0dHN55UMIvFEuttC-j5RyYFRHL_eDh-cMiGrYfgOvRmgWBkm6Vsj61BmXzvGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
باگناما از گل گهر جدا شد، نیاد پرسپولیس صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136871" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=lx70tBkI55d-nWf1L-TTpCSUWrgFlQ-eW11Pr0t4K2PL7tWjUsSsgesPs2l2hbsyBYXTrQ_oJJVb_sgEZV89VEIgjhKr5KCjeUAUaWrqvNmZ6fpbOk1M6Wf-zU3F0VwpTv2isjmHV-HrR_TxQjwC-hGH5DB7rlxdk6f0Pb_vV0kRWL340W4BEhc78BV3MEeCceQplUMz2Es_t1EB_W81_6ES3dBy_c7FzttG0TP5fga952bnH2qUzjSmvnlXlSbgwU0e6jIbSvJGTHOSi-H1J5NwZfdCXsKzbD1-4HQYuLzgo2eELog2Btji2gPXFCRo0npDBUM2sAh-4UM4WePkITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=lx70tBkI55d-nWf1L-TTpCSUWrgFlQ-eW11Pr0t4K2PL7tWjUsSsgesPs2l2hbsyBYXTrQ_oJJVb_sgEZV89VEIgjhKr5KCjeUAUaWrqvNmZ6fpbOk1M6Wf-zU3F0VwpTv2isjmHV-HrR_TxQjwC-hGH5DB7rlxdk6f0Pb_vV0kRWL340W4BEhc78BV3MEeCceQplUMz2Es_t1EB_W81_6ES3dBy_c7FzttG0TP5fga952bnH2qUzjSmvnlXlSbgwU0e6jIbSvJGTHOSi-H1J5NwZfdCXsKzbD1-4HQYuLzgo2eELog2Btji2gPXFCRo0npDBUM2sAh-4UM4WePkITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند
#ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136870" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚠️
⚠️
باشگاه برای بازگشت امیررضا رفیعی امروز مذاکراتی داشته….!
🌀
چرا مازاد شد که الان…
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136869" target="_blank">📅 23:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136868" target="_blank">📅 23:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahrooooookh Abbasi</strong></div>
<div class="tg-text">منطقیه این عدله و تفصیرتون کاملا
👍
ک پرسپولیس تو پست محمدقربانی الان بازیکن نیاز نداره،چون باکیچ،مملی و دوتا پوریا هامون ک تازه از گل گهر گرفتیم کافی هستن و بلاخره یجاهایی هم مربی این حقو داره ک با اون بازیکن هایی ک خودش میشناسه و خریده بازی کنه چون اینجور بازیکن هایی ک مورد علاقه سرمربي هستن و با نظر وتاکید خودش جذب میشن بخاطر اون رابطه ایی ک بینشونه یجورایی برای اون سرمربی جون میدن و تو زمین براش کم نمیزارن...ولی الان ک قربانی با این تفاصیل جذب نشد اینو هم باید بگیم ک تو پست ۱۰و پشت سر مهاجم حتما یکی مثل محبی،ترابی،هاشم نژادو...باید از نون شب واجب تر و جذب شه</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136867" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
روزنامه گل چاپ فردا:
😀
مهدی طارمی بین لیگ برزیل یا پرسپولیس به زودی تصمیم گیری میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136866" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
‼️
شماره 8 مرتضی پورعلی گنجی رسماً به مهدی تیکدری رسید تا جدایی مدافع میانی قرمزها قطعی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136865" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
فارس: تارتار از عملکرد گرا و بیفوما تو تمرینات تیم راضیه و احتمالا این دو بازیکن فصل آینده تو پرسپولیس بمونن. ( شما بخون نتونستن یا اجازه ندادن این دوتا برن..)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136864" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
🏅
آقای هوادار ۸۰ درصد نفراتی که تو لیست اول تارتار بودن جذب شدن و تمام نفراتی که از گل گهر میخاست، لطفا از الان بهونه دست کادرفنی ندید، آقای تارتار طاهری رو نمیخاست و گفته بود حد المکان ایری رو جذب کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136863" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#شفاف_سازی
⛔️
در خصوص محمد قربانی خیلی هوادارا میگن بخاطر اینکه تراکتور تقویت نشه ما باید جذبش میکردیم، اما بودن خدابنده لو،باکیچ،پورعلی و لطیفی فر به هیچ وجه قابل توجیه نیست جذب قربانی
🔴
البته باشگاه قبل از جذب پورعلی و لطیفی فر برای محمد قربانی نامه زده بود اما همون ابتدا کنسل شد، یکی از عللش این بود که ایجنتش منصور عظیمیه دست راست زنوزی و اجازه این انتقال رو نداد،قربانی از دو باشگاه دیگه ایرانی هم پیشنهاد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136862" target="_blank">📅 22:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136861">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
اعلام ساعت قرعه‌کشی لیگ برتر
🔴
🔴
مراسم قرعه کشی لیگ برتر جام خلیج فارس فصل ۱۴۰۵-۱۴۰۶ ساعت ۱۶ روز سه شنبه ۶ مرداد در سالن همایش های بین المللی هتل المپیک تهران و با حضور مدیران فدراسیون فوتبال، سازمان لیگ و نمایندگان ۱۸ باشگاه حاضر در این رقابت ها و اهالی…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136861" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136860">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein</strong></div>
<div class="tg-text">این نکته رو بگیم ک درویش با همین مدیر فاسد سر فخریان عجب دزدی کردن غیر عادل هیچ کسی حرف نزد</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136860" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
📌
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام عضو هئیت مدیره باشگاه پرسپولیس
⭕
باشگاه پرسپولیس برای جذب دانیال ایری و کسری طاهری به صورت رسمی از سازمان لیگ و فیفا استعلام گرفته تا در صورت نبود هرگونه مانع قانونی، قرارداد این دو بازیکن را نهایی…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136859" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136858" target="_blank">📅 22:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
فدراسیون فوتبال و شخص مهدی تاج به دنبال تمدید قرارداد بلندمدت با امیر قلعه‌نویی هستند! هیات رییسه با این تصمیم مخالف است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136856" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤩
#تایمز_توئیت
❌
هر روز برای من مطالبی تحت عنوان افشاگری از مدیران باشگاه میفرستن که بیشتر شبیه فیلمنامه هاست
⁉️
وقتی هر روز یه روایت جدید از نقل‌وانتقالات میاد، آدم نمی‌دونه مدیرعامل کیه، سرمربی کیه، دلال کیه، خبرنگار کیه، منبع آگاه کیه!
❌
یه عده میگن فلانی توافق کرده، یه عده میگن نه، یکی میگه پول نیست، اون یکی میگه پول هست ولی نمی‌دن، یکی میگه لج کرده، یکی میگه اصلاً از اول قرار نبوده!
❌
باشگاه رو انگار گروهی دارن با ریموت کنترل می‌کنن؛ هر دکمه دست یکیه، فقط دکمه «اعلام خبر قطعی» خراب شده!
❌
خلاصه تا وقتی هیچ سند و خبر رسمی‌ای منتشر نشده، این مدل روایت‌ها بیشتر شبیه فیلمنامه‌ست تا خبر. ولی خب برای جذب فالور و دعوا راه انداختن، ظاهراً از هر نقل‌وانتقالی جذاب‌تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136853" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">➕
بعد پنج سال به این نتیجه رسیدم حداقل نصف هوادار هامون متعصب،ناآگاه،هیجانی،و تو دنیای موازی هستن و اغلب دنبال کری خوندن و دلقک بازی
➕
هیچ فهم و درکی از فوتبال حرفه ای ندارن و چشم گوششون به دهن چهارتا از خدا بی خبر بچه ساله که گوشی گرفتن دستشون میگن لنگش کنید، هوادار واقعی پرسپولیس رو سکوعه که لب دهن نیستن اونی که تو گرما و سرما از تیمش حمایت میکنه و بالا پایین این تیمو دیده و به مسائل اشراف کامل داره، یه عده فقط لب دهن مجازی هستن و ساخته شدن تو زمین رقبا بازی کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136851" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🫦
کونده رفته به ایجنت ایری و طاهری گفته به بازیکن هاتون بگید استوری بزارن… شما که پول نداشتید گوه خوردید این دوتا رو خریدید به امید اینکه این وسط یه پولی گیرتون بیاد ولی فعلا کیر خر دستتون داده بانک شهر… به قران خود بازیکن ها هم ذی نفع بودن وگرنه هیچ کصخولی…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136850" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136848" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136847" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136846" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWWRlBKiC6jMdEr0AAR6JkPctsBtkMaqIqJinGjjTUMJyHgYixspEA8aRosN3QFP-_9_KJnZZ2l29_6BRQ_xkMinIP3SWIO1jtom8UPiyvedhGIfIMfiFfyhE48RmnVlsvs5UeSXUur_g8ViqXN_xKvueCGCqCFLBAzm_88xSGt7FAq8rBdQL9VTDUPwWphzDWGEyKcDVd3Y37pL1nHF8O1fd16t-jfui6E-BVWAOoDRNd3sCAwUBk0R8xk7Rxo6JHG3Jgwj0tp8cCWufDLxkCCEyVbN_ZNON8md52fO8MK8mqaXw7vlZ5ZmDcUlk0bOVnMppumweogPXjI7jwfdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری رومیخواهند یاکه خیر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136845" target="_blank">📅 21:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
✖️
✖️
آنا: یاسر آسانی به سرنوشت دیدیه اندونگ دچار شد و تحت هیچ شرایطی نمیتونه تا نیم فصل برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136844" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mysJVhspAGvq6aBrEIQ0ITFTg4b1CFPiTufQ_xgt8aT-UvRKrJ8qEhUniIfouSg6yWRgR2r62x0-sJIGCO0n28x40EfAx9cl3uyIGsq0Wb4Fijlu9eirZihwwmjMazPdcAQQ71bwVoHr7aW8VfHGS4P8LIShSQlfOtdVOp2ds9r1_oaXm5xGUN-fHbUPMbxEZH2rFsPjXfH9HrXV4g9x6ECw1MF6vIYmWYQ2YFqVp0r8eJ8jADBu4ZDHe8719XSWSC_Y55jIjerVpgIvPEvuwCi98mF7I5KoFBJv8wFPmXx5YUyQgdTyYsTlnpc7O169kfDLwdJe677BwN_BYpAm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
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
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136843" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136842" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136841" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
#فوری | ترامپ:
🔻
برای دیدار با مقامات ایران به توافق رسیدیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136840" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136839">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136839" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136838" target="_blank">📅 19:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136837" target="_blank">📅 19:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
🔴
پرسپولیس برای جذب فرهان جعفری از نظام وظیفه استعلام گرفته و اگه مشکلی نداشته باشه میاد پیش خودمون/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136836" target="_blank">📅 19:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎶
🎶
🎶
صادق محرمی طی روز های آینده از تراکتور تبریز به صورت رسمی جدا خواهد شد و احتمالا به پرسپولیس بازخواهد گشت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136835" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">همه چی رو کنار هم میزاری میبینی کسری طاهری و دانیال ایری و مدیرعامل نساجی و دلال این بازیکنا در کنار بنگاه دلالی ورزش سه دستشون تو یه کاسه هس و دارن آخرین زورشون رو میزنن برای تیغ زدن باشگاه صب ورزش سه خبر میده کنسل شدن الان بازیکنا خیلی یهویی با دستور دلال هایشان استوری مشترک میزارن هوادار هم که خدارو شکر سوار موج میشه</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136834" target="_blank">📅 18:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136833" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕
هرکسی از ننش قهر کرده گوشی دست گرفته کانال هواداری زده هر کصشری میخان میزنن، اون حروم زاده ها اگر میخاستم بیان پرسپولیس چرا رفتن نساجی؟! صدرصد هم خود بازیکن هم ایجنتشون با زندی بستن
‼️
یکم عقل تون به کار بندازید خداوکلی چرا هرکس هر کصشری میگه طوطی وار تکرار…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136832" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136831" target="_blank">📅 18:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل نمیکنه شروع میکنه کوبیدن باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136830" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWHpp5BHxlx0TCNyUuzZOvW4fAYWz6-XStTFE-m-juAYtLlOAl0g5aQKbE_T_s3yTJUqZOuZzuQq5IJPqD69cFNmmBvf5MRVSoMEx5qGhSjfQLTWDg9Wkh8Icp9rFw8f5yv2YXBiSSsgq56MfG-yg2e68T5Ar9WYVIuXlgIqDPFV8aIdvG8ekVsMNmf2E8drZdvZmtByWgZKHxgp1NnSAHs8HLyaErZfBDDRfI_1BtfaGrJUMeB56P-XOCnvxPRXqQb8qSE7yp-lsyTBkMg5gG_mKTOF1xGiq1wF89xoWMFYJdOjVyD9zCnJAsCWgB_L4A7Z7EHi857zReEcHVIqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند اصلا دانشجوی دکتری نیست
🔺️
رئیس مرکز ورزش و تربیت بدنی دانشگاه آزاد گفت آخرین مدرک بیرانوند، کارشناسی ارشد است و او حتی دانشجوی دکتری هم نیست.
🔺️
پیش از این بیرانوند در تاریخ ۵ خرداد ١۴٠۴ و در برنامه فوتبال برتر ادعا کرده بود که دانشجوی دکتری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136829" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136828" target="_blank">📅 18:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔄
🔄
ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم و این شرایط برای خودمان نیز آسان نیست؛
🔴
🔴
ما نیز میخواهیم هرچه زودتر تکلیفمان مشخص شود تا به فوتبال و آینده خود برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136827" target="_blank">📅 18:11 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
