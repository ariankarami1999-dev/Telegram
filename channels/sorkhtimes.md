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
<img src="https://cdn4.telesco.pe/file/hthAthw_kPeEEk0EXkbbBPu8b6osLTkGOYeA5HuBaHf_hDrayCeVvCagfClVPrV701y7_LUYgjwcc8UMn13TMRYINaT8FcEsvenOR2rsCIAht54T-CCsiNAm7x0kIqwZdYNLo2TlNZ0VUIY4e0noHWh5Fq7Dd_CFI1x-W4S2JECmprFuemG5GNF24YiGO5Joi7UVO1KslZ9xx2ajYmt1Gs1ZT29sLlyf8NqE7J2Nz4xJGMNG7HL3rP1EDa5yw28D0tg8rXcb94Jt6lZ_KXYDL9Q4F_FtoniYFG4OxnlRxMOWJSXBZsCPwe6p1SooZjtFqfwnlLMPFR0fOtAuEHB6mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-135687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/135687" target="_blank">📅 17:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/135686" target="_blank">📅 17:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/135685" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/135684" target="_blank">📅 17:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135683">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/135683" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
پیمان حدادی : ما به میلاد محمدی پیشنهادمونو دادیم فردا آخرین فرصته که قرارداد رو امضا کنه اگه نکنه از لیست تیم خارج میشه این پرسپولیسه که واس بازیکن تعیین تکلیف میکنه نه بالعکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/135682" target="_blank">📅 16:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
عجب بابا عجب
😐
🚨
🚨
🚨
تسنیم: باشگاه نساجی مازندران رضایت نامه دانیال ایری رو گرون کرده و به ۱۹۰ میلیارد تومن افزایش داده!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/135681" target="_blank">📅 16:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135680">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
رضا جباری به کادر مهدی تارتار اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/135680" target="_blank">📅 16:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135679">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
پیمان حدادی : صحبت از مهدی ترابی، دانیال اسماعیلی فر، آریا یوسفی، رامین رضاییانه آیا تیم رقیبمون به ما بازیکن میده وقتی قرارداد دارن؟
✅
مثل اینه من اورونوف رو به اون تیما بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/135679" target="_blank">📅 15:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135678">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
زندی:تیمی در حد قهرمانی بستیم.
🎙
برای خرید محمدجواد حسین‌نژاد با باشگاهش‌ به‌ توافق رسیدیم که روی مبلغ ۱.۸ میلیون‌ دلار این‌ بازیکن را جذب کنیم اما خودِ بازیکن حاضر به امضای قرارداد با ما نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/135678" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135677">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2T3ao3YIQw_d2SjLdyiiNN7F2L1xqCGncHDETPCTh9bVb8nKjET1SOQn4llWD7msCZWAiS3spSFJe9cENjqHD_fB5TQp2EdWkOP8V5Yk4qn7s1R2jGl24TkaNNKO6KweevyCMpAvCl26cbmyCtevSUwnPoqi4JsKrk6LyZ3d7qiHIb06l4CShhjSbz-_tB81qwXl88SU4R5sNj6hzxOpF98-vIm_BuroxydMqM1uBSiWNAPFZfWPXbR2FnOI1tvNOWmMKr5aPglYmZ-3pdmA94p0AqQMOl7Ad-zj-93h8owcso-pRdrpndLOqY2wyjVsbMxovvs1iWvDzr_hS_Qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/135677" target="_blank">📅 15:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135676">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135676" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/135676" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135675">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/135675" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
عجب بابا عجب
😐
🚨
🚨
🚨
تسنیم: باشگاه نساجی مازندران رضایت نامه دانیال ایری رو گرون کرده و به ۱۹۰ میلیارد تومن افزایش داده!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/135673" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwGVrqir6hrPczyLMEe24nDvM2JAMCbzR8dRqgFpvTWpSxDa1X_VXvDXboFODOKWBLCFAp-uxVzE4zfGF1Fpt-j6AeHrLUSJVR4Tv2IK82fUCdBE35YkWczUjltvyHpyun0yUiAf-l2V4LolzmcNfPFdn_XkNqIAayrJJHKMMA5VO4boLLFugyprPhN0ih4GRDUbxrzSAXICisMj5nILKiWMRAK23uTd6HY73I0ShyWcKKJeub2KXh-nWpW3CqVd3Ir0Xb456bUI3X7HulSrdGkBJmvOpjCYePrJqFRZAoLqgfu80KEPz5Ght2Ho223P9QdH6dOCNuvZy7gdP-FPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/135672" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
شهاب زندی: دانیال ایری بازیکن ماست و دیگر قابل فروش نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/135671" target="_blank">📅 15:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135670">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/135670" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135669">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
🚨
فووووووووووووری
⏺
حسین قهار خبرنگار فرهیختگان: پرسپولیس می‌تونه کسری طاهری رو بخره به یک شرط که نساجی با همون مبلغ به پرسپولیس بفروشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/135669" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135668">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia1SdwXllrMKqXbpEQTuSHWTdiuSD8EusgWGqSKdvQEv0a5ION1OCMbW1SI2hXZ34zmylKQ4Flx2q9nKjbXwYl5ALX157ZUJZXuic4HRzLO88nh4fL_9nnVaJLs68LpFMy3R3tr3zGCP5EebC2SNuvAuNBzAbv0QeVaumkD3I7t3on3WcWmO4HpAcNPAofqJZo_UFiwKV2pdcfWApPcat8l2VKpQSH7vbaL_tnV4iHi4ZjqHQr-owpTLmtkK3tHmOYGYMrR3CzixGRinBpbEr8czn8CC6ohg_5j0r3ogw6UHwBJ2sNW7IOTzK33VgDOd9p-AC8XtXOnzXrz3Ml-gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/135668" target="_blank">📅 15:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135667">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
🚨
فووووووووووووری
⏺
حسین قهار خبرنگار فرهیختگان: پرسپولیس می‌تونه کسری طاهری رو بخره به یک شرط که نساجی با همون مبلغ به پرسپولیس بفروشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/135667" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135666">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❗️
حسین قهار خبرنگار فرهیختگان: خداداد عزیزی از انتقال طاهری به نساجی خبر داشت و سوالی که دیشب از کسری طاهری کرد برای به حاشیه بردن پرسپولیس بود. حاشیه ای که با جواب کسری طاهری میتونه سه پنجره نقل و انتقالاتی پرسپولیس رو ببنده
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/135666" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135665">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
فووووری؛ پیمان حدادی پس از عذرخواهی بابت مصاحبه ای که انجام داد ، موفق شد رضایت علیپور رو بگیره و قرارداد کاپیتان جدید پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/135665" target="_blank">📅 14:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135664">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
شنیده ها
🗣
پس از صحبت های تهدید آمیز پیمان حدادی؛ علی علیپور در جلسه امروز با پیمان حدادی شرکت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/135664" target="_blank">📅 14:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135663">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaO_UvSmWtPsetwYjAMbVAGdCglj-YhgfyZZr2J4Y6-lOWbl2tRRyHOJ2Oj3YP2Jy8Tdhkxz1AEsf_EuTDG1TdqQgMqirTSq42pswx3-pT9luntIwlYPQ2Z3fI4a4LNrhZuOcybzJCww8CM3ScUMcDyhOSpiKGS5HOJ012VmM5TrFY_Ta45ufdOcpkADaVUUqvPrB-CWHeDBZhgkg3ZPR2i51hM1SOLxNCMA4Qa0_y-2mJx-acx1H6m_6X0sv2FQ02B4shyBHjDi4PH1DlPpShye3SFSsy3vNf0b_dLzgGPWQ5StNvuZ6azzTb40VFmIfXVs9Gy3l1W5499KUooH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
علی علیپور مهاجم ۳۰ ساله و ملی‌پوش پرسپولیس بعد از توافق با مدیران این باشگاه، قرارداد خود را با سرخ‌پوشان پایتخت تمدید کرد تا در جمع قرمزها ماندگار شود
.
✍
📝
خبرگزاری ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/135663" target="_blank">📅 13:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135662">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
باشگاه اعلام کرد با کسرا طاهری قراردادی امضا نکرده و هیچ قصدی برای خریدش از نساجی نداره/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/135662" target="_blank">📅 13:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135661">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlcYc_YWYZw6k7m4ZM5iX-ObPMgdBFrN9pAWA9BzbaJg8GDpPT4OF2bn5ajkpDDJpdrJFVvLJD17Icgs-JZn5h2fn8WY9pKj88sHMlaSXCB__mdcf-3NSH57Qq9izsPzlhpEXo6rF4_MLtaeOocxxI98_ENO3t0yvTO9vIyfiOt3hJkTxB3Hot8EbGHIylJiD-m-ILnzwEK8xzu9vGW_8sAVSc5PGkY42j6Oqr7D7fbkzwJqrwrYg7jkoJuKwuZpRAKna7W35IgkEc282F-Ec2u5qjRvmCa1O3R3YPCckg-Q5AeXDfMylBoSSYNJwo_tSOP0FyUjwrCOgBKzNislFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باشگاه پرسپولیس با تصمیم مهدی تارتار به دنبال خرید مهدی ترابی است. اگرچه ترانسفر مارکت این بازیکن را آزاد و بدون قرارداد اعلام کرده اما باشگاه تراکتور با اطمینان اعلام می‌کند که او قرارداد طولانی مدتی با این باشگاه دارد.
✍
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/135661" target="_blank">📅 13:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135660">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
دوخریدارزشمندنساجی دراین پنجره؛ وقتی مدیر عامل حرفه‌ای و کاربلدداشته‌باشی: برای جذب دانیال ایری و کسری طاهری 200 میلیارد تومان هزینه کرد الان رو هم 450 میلیارد مشتری دست به نقد دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/135660" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135659">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
شنیده ها
🗣
پس از صحبت های تهدید آمیز پیمان حدادی؛ علی علیپور در جلسه امروز با پیمان حدادی شرکت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/135659" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135658">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس اعلام کرد : طاهری کصشعر گفت که فردا پرسپولیسی میشم ما فقط یه توافق شفاهی داشتیم بعد که دیدیم هزینه جذبش کلی ۲۰۰ میلیارد میشه بیخیالش شدیم رفت نساجی
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/135658" target="_blank">📅 11:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135657">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
فووووووووری
🔴
شهاب زندی مدیرعامل نساجی: کسری طاهری به نساجی پیوست. قرارداد ما و او به زودی امضا میشود. او فروشی نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135657" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135656">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135656" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135654">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135654" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135653">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
فووووری از تسنیم: باشگاه پرسپولیس به طور کلی قید جذب کسرا طاهری رو زد و این بازیکن رسماً به نساجی مازندران پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135653" target="_blank">📅 10:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
بازیکنی رو که می‌شد با ۷۰۰ هزار دلار خرید، الان فقط باید ۱ میلیون و ۲۰۰ هزار دلار به نساجی بدن تا شاید بعد از ۱۶ مسابقه بتونن ازش استفاده کنن! پول بیت‌المال هم کشک ! یک نفر نیست سوال کنه که چطوری و تحت چه مجوزی بابت جذب کسری طاهری باید ۵۰۰ هزار دلار [معادل…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135652" target="_blank">📅 09:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135651">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
تصور کنید، پرسپولیس با سابقه چند ده قهرمانی،  از نساجی‌ای هایجک میخوره که هنوز وارد لیگ برتر نشده !
✅
پرسپولیس درواقع از تیمی که هنوز مسابقاتش در لیگ یک[آزادگان] ایران تموم نشده هایجک خورد!!
❌
❌
یک درصد هم این انتقال انجام بشه، از اون انتقال‌هایی است که هر…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135651" target="_blank">📅 09:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135650">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
توضیح تکمیلی ِ حقوقی:
❌
اگر از سوی فیفا انتقال کسری طاهری از روبین‌کازان به نساجی، صوری تلقی بشه، دردسر حقوقی بسیار خطرناکی برای کسری‌ طاهری، نساجی و باشگاه پرسپولیس باز خواهد شد و ممکنه ۳ پنجره نقل و انتقالاتی پرسپولیس و نساجی بسته بشه.//خرمی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135650" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135649">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
این قرارداد درصورتی که منعقد بشه، ریسک بالایی داره و یه پرونده حقوقی سختی باز میشه.
🔴
درصورتی که پرسپولیس بخواد کسری طاهری رو برای ابتدای فصل بخره، فیفا قطعا ورود میکنه و پرسپولیس و خود بازیکن باید برن جواب بدن که قصد دور زدن قانون رو داشتن یا نه...
❗️
کلا…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135649" target="_blank">📅 09:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135648">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
ورزش سه: کسری طاهری با عقد قراردادی قرضی از نساجی مازندران به پرسپولیس پیوست
🔴
تفاهم نامه سه جانبه پرسپولیس، طاهری و نساجی امروز امضا شده و طاهری یک فصل قرضی در پرسپولیس بازی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135648" target="_blank">📅 09:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135647">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎬
حمله و توهین زشت بیرانوند به مهدوی‌کیا: بازیکن نسل گذشته تیم ملی تا مکزیک آمد با اینفانتینو عکس گرفت، ولی حاضر نشد به کمپ تیم ملی کشورش بیاید!!
🔴
بیرانوند:  آقای مهدوی‌کیا از چه چیز ترسیدی که به ما سر نزدی؟
🗣️
بعد از بازی با بلژیک کدام یک از اسطوره‌های…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/135647" target="_blank">📅 09:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135646">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185e8a93ff.mp4?token=cgzdxIhlwG3501wqpxu9-VluiWKDc1aIlbe-DzzA1usFPjM0mHqbH2TixrJxtoF3cczY0Wdnz5iJ4pwaSt_v7Ky3jyu_gDXEeUUiNGmRKIHvE4YoVKQFTkFs7E8B5abFpsn3ZPaphd198GvEMBQheCt1UkY8_v2lbiWGxpGmfN12xG6AKzkeaZxkuxQbQBak56jqFE2X7Dh_RqV-2-8SjHrLCOayeEaK6Sv8aMqXuBME45vFovBw0JQaGLQjvpPGIjbKXSQ3X2AtQ5cY17cduwBaZXP9t3FhwDqNrTAlG6nupD4Lr3klQbrm4z3tEPqFsgqiWQYxH3hvWNbUSfDY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185e8a93ff.mp4?token=cgzdxIhlwG3501wqpxu9-VluiWKDc1aIlbe-DzzA1usFPjM0mHqbH2TixrJxtoF3cczY0Wdnz5iJ4pwaSt_v7Ky3jyu_gDXEeUUiNGmRKIHvE4YoVKQFTkFs7E8B5abFpsn3ZPaphd198GvEMBQheCt1UkY8_v2lbiWGxpGmfN12xG6AKzkeaZxkuxQbQBak56jqFE2X7Dh_RqV-2-8SjHrLCOayeEaK6Sv8aMqXuBME45vFovBw0JQaGLQjvpPGIjbKXSQ3X2AtQ5cY17cduwBaZXP9t3FhwDqNrTAlG6nupD4Lr3klQbrm4z3tEPqFsgqiWQYxH3hvWNbUSfDY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهدی تیکدری: دوست دارم هواداران به من لقب تیکی لامبورگینی بدهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/135646" target="_blank">📅 09:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135645">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFINQuzmnzug0pnSAU9DAYlnE1oFIppScuEBxX-BgXSXHdJ0Fj2u_d14R_JjvqRiM9vHCWBb0OGADLH7QLDjvAM2L22YlBUB6hVC6XkRvYABMP1y_ZTk_hFHmoYLFgUx-sLXKI3pFE-M7-BJ_rTKg1RzrEsySAAsEvLrKKWkJPomwvRjrizzmN2wXwp35v6BRZLL8usgAlxmQuO6oz4HJoenKpeAgKvzn4afS-61gDactRMoOQvHCzRlA7RIu7TbCfopXxLXsOiwdQ33fr71F9JxbXQ52JlsXPmkhQCxItGrynXhtMf9-Y_sz6Xjm48OjWjnnpefoGzz0-0Ey4UaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوستون اورونوف چهارشنبه‌ وارد ایران خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/135645" target="_blank">📅 09:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
دختر بیرانوند : بابام استقلالیه و دوست داره برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/135644" target="_blank">📅 09:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a6a5812d.mp4?token=nB7dM9IVQdF01QRqRuaHRMEYAVywu4VAbkZnIqeQtMDaa2PGLUywyR0lwRueC7eArZNcnisrJUN9wMeZ49NRuUChkwBu6T7lEauIxpg0tBHHVukNphC0_5mwDb_xquGcXcVWVXy7iflQH2u-LqR0VTRs3FszmYz3IZPSrmapFqUWk3yieEMyNYTroJo2r0v-k3NXwXd_EILLfaK1hvQBvB1UmzvZlkAbi-l1tC0iaiYK_-grBfkTc1NXaOVTJXAjvJgCr28rR2pXRpwWDf9BqRxnEUAPYAcGCbF1Dh5l-gfydhRlnHs3dDb_peSQJ-emHy-OzCiiaaqX4mdyCWBMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a6a5812d.mp4?token=nB7dM9IVQdF01QRqRuaHRMEYAVywu4VAbkZnIqeQtMDaa2PGLUywyR0lwRueC7eArZNcnisrJUN9wMeZ49NRuUChkwBu6T7lEauIxpg0tBHHVukNphC0_5mwDb_xquGcXcVWVXy7iflQH2u-LqR0VTRs3FszmYz3IZPSrmapFqUWk3yieEMyNYTroJo2r0v-k3NXwXd_EILLfaK1hvQBvB1UmzvZlkAbi-l1tC0iaiYK_-grBfkTc1NXaOVTJXAjvJgCr28rR2pXRpwWDf9BqRxnEUAPYAcGCbF1Dh5l-gfydhRlnHs3dDb_peSQJ-emHy-OzCiiaaqX4mdyCWBMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دختر بیرانوند : بابام استقلالیه و دوست داره برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/135643" target="_blank">📅 09:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135642">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889c05b23a.mp4?token=pKu3Hgcm4hlU8gibS8CsTMLu-Yd7ysdrXpbl190BfmfcyZ-D-yvMKucNpFWLvSCiBiPx2E1EpBUwm5dJtILY6ope7idFgnh9K8oADBbCXgEtiizPieg35KwQsbZxtgtllwwEmoxUwcIzmqAghi9hMaxf_5AXbpsDX7lujXScxEximxRTpLWLuzhri_5uEBByhphdS8CCExIKgH3_RVCmCfaq2ky23R8jkefQHnmMd47KXLoCnfEJhyqyz3kBRYxj-MIbL2kXReb5iWkOmX7RulHX5jvHt2dWeMWfOMRCt-VhMXSdr4Oe2PpBPBfaq55bhfxqPfV3DP5cvlO0pCawT4eK7l2yS7PsDK4p9ryjdjjVubrUN6D40M27sX8yBi0-XA6v9vUwxgxkg4Sm6DvJd1rijCPgKgZnrQTSCdDDGnhy_6bSOqdaZL_8PZy_z-xzl_FqPcEWdkSLf7pNM1kF4z-GMnc-U-HYmbeGjwI_gXeVJ1dg9nn6rc2X9IKDHiDbTVuGeBOclPbxSWYmshZkflAehHPGqJ7Gt6ZIRkH3K8Xr_y5F-H9bx-HbqdOMnOnxSwlcMpko7sYRmWvLZQh5le4uOwdBYhsc9E-3LZ8REtjWG2uLp6JoSAUhtwpdqPQRGCfmoBSRgTldLEcNQcY5tCGcjCti760TaHd8naUCvh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889c05b23a.mp4?token=pKu3Hgcm4hlU8gibS8CsTMLu-Yd7ysdrXpbl190BfmfcyZ-D-yvMKucNpFWLvSCiBiPx2E1EpBUwm5dJtILY6ope7idFgnh9K8oADBbCXgEtiizPieg35KwQsbZxtgtllwwEmoxUwcIzmqAghi9hMaxf_5AXbpsDX7lujXScxEximxRTpLWLuzhri_5uEBByhphdS8CCExIKgH3_RVCmCfaq2ky23R8jkefQHnmMd47KXLoCnfEJhyqyz3kBRYxj-MIbL2kXReb5iWkOmX7RulHX5jvHt2dWeMWfOMRCt-VhMXSdr4Oe2PpBPBfaq55bhfxqPfV3DP5cvlO0pCawT4eK7l2yS7PsDK4p9ryjdjjVubrUN6D40M27sX8yBi0-XA6v9vUwxgxkg4Sm6DvJd1rijCPgKgZnrQTSCdDDGnhy_6bSOqdaZL_8PZy_z-xzl_FqPcEWdkSLf7pNM1kF4z-GMnc-U-HYmbeGjwI_gXeVJ1dg9nn6rc2X9IKDHiDbTVuGeBOclPbxSWYmshZkflAehHPGqJ7Gt6ZIRkH3K8Xr_y5F-H9bx-HbqdOMnOnxSwlcMpko7sYRmWvLZQh5le4uOwdBYhsc9E-3LZ8REtjWG2uLp6JoSAUhtwpdqPQRGCfmoBSRgTldLEcNQcY5tCGcjCti760TaHd8naUCvh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
حمله و توهین زشت بیرانوند به مهدوی‌کیا: بازیکن نسل گذشته تیم ملی تا مکزیک آمد با اینفانتینو عکس گرفت، ولی حاضر نشد به کمپ تیم ملی کشورش بیاید!!
🔴
بیرانوند:
آقای مهدوی‌کیا از چه چیز ترسیدی که به ما سر نزدی؟
🗣️
بعد از بازی با بلژیک کدام یک از اسطوره‌های تیم ملی یک استوری دمتان گرم برای ما گذاشت؟
❌
👀
پی‌نوشت: دمتان گرم بابت چی؟ بابت حذف و نرسیدن به جمع ۳۲ تیم؟؟؟ چی میگی تو؟ دهنت رو آب بکش اسم آقا مهدی مهدوی‌کیا رو میاری. خوبه خودت هم می‌دونی اگر کسی با شما عکس بگیره فحش میخوره. چون محبوب نیستین.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/135642" target="_blank">📅 09:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135641">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
بیرانوند: اگر به استقلال بروم می‌شوم یاغی پرومکس؛ هنوز برای برگشتن به پرسپولیس فکر می‌کنم
😐
❗️
❗️
سال قبل از استقلال پیشنهاد داشتم و قرار بود اتفاقاتی بیفتد که نشد؛‌ امسال هم این پیشنهاد هست.‌من اگر استقلالی شوم یاغی پرومکسم. خیلی‌ها دوست دارند من به پرسپولیس برگردم ولی خودم استرس دارم. هنوز برای برگشتن به پرسپولیس فکر می‌کنم.من تا زمانی که تا صد مطمئن نشوم که پرسپولیسی‌ها دوستم دارند برنمی‌گردم. اگر عملکردت خوب باشد برندت حفظ می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/135641" target="_blank">📅 08:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135640">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
جدیدترین آپدیت اپلیکیشن 1XBET
🤖
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
حتما
بدون فیلترشکن
از اپلیکیشن استفاده کنید
🎁
هنگام ثبت نام کد هدیه 130 دلاری vipfarsi را وارد کنید.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135640" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135639">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyXMiU2F7fe_21KY-cQ6GcMmBXGIYsHGHQzzWq0fd71xvYisg43K-IABX71HsJghb9jU1C7jhV3RCP0tYCyxnVPw0h8qS0KMASod73VegQpq4WqRqcwCUs0abEhx44LEOQrSWwaBaiybfNiPjebvD7aChg2tnDXQUat7gzU2gH5WGU9kNh-fhtyRUFf5p0Tvv98I_iGYTp0BPHNE7X9xxaSOq2EwBQW5cdNCJaDMPw9_GeLATAODQ6VC7vzPPd1s6obyE8KneujLXZdsGCcpavOVQRmVtVYz157nzbYax5t3PHh1iXso3GhU31k-Z2WL1V3xGwjMc8Dm5aLreJ1B2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
همین حالا در وان‌ایکس‌بت پیشبینی کنید | Bet now on 1XBET
1️⃣
🏆
نیمه نهایی بزرگان؛
فقط چهار تیم باقی مانده‌اند…
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⚡️
وقت آن رسیده که قهرمان واقعی خودش را نشان دهد.
بازی ها را با بالاترین ضرایب پیش بینی کنید
🔥
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🔑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/135639" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135638">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#تایمز_توئیت
🫦
یه مشت زنا زا… شدن کانال دار و خبرنگار جاکشا نون زندگی شونو از خبر پولی و بولد کردن بازیکن های ایجنت ها در میارن هرجا کیر خر دستشون رو نمیگیره همگی میریزن رو یه باشگاه خاص…. جمع کنید پوفیوزا ۵۰۰ تومن بهتون بدن تخم های طرفو از دهنتون درنمیارید…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135638" target="_blank">📅 01:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135637">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#تایمز_توئیت
🫦
یه مشت زنا زا… شدن کانال دار و خبرنگار جاکشا نون زندگی شونو از خبر پولی و بولد کردن بازیکن های ایجنت ها در میارن هرجا کیر خر دستشون رو نمیگیره همگی میریزن رو یه باشگاه خاص…. جمع کنید پوفیوزا ۵۰۰ تومن بهتون بدن تخم های طرفو از دهنتون درنمیارید
🫦
سر شب آدمو مجبور میکنید شیلنگ عنو بگیره روتون…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135637" target="_blank">📅 01:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135636">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali habibi</strong></div>
<div class="tg-text">قهار مدعی پرسپولیسی بودنه ولی از وقتی تو رفته فرهیختگان بساط این روزنامه همینه</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135636" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135635">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⛔️
من نه کاری به صحت سقم اخبار دارم درخصوص کسری طاهری و نه قصد حمایت دارم، اما یک سوالی فکر منو درگیر کرده چرا خبرگزاری فرهیختگان از بدو حکم گرفتن مدیرعامل فعلی باشگاه هر روز در حال زدن مدیران و باشگاه پرسپولیسه
‼️
دوران اقای رضا درویش چرا صحبتی نمیکردید ؟!…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135635" target="_blank">📅 01:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135634">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⛔️
من نه کاری به صحت سقم اخبار دارم درخصوص کسری طاهری و نه قصد حمایت دارم، اما یک سوالی فکر منو درگیر کرده چرا خبرگزاری فرهیختگان از بدو حکم گرفتن مدیرعامل فعلی باشگاه هر روز در حال زدن مدیران و باشگاه پرسپولیسه
‼️
دوران اقای رضا درویش چرا صحبتی نمیکردید ؟! همه چیز گل بلبل بود ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135634" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135633">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
ماجرا از این قراره که کسری طاهری اول با نساجی قرارداد بسته و سه هفته پیش برای انتقال قرضی به پرسپولیس توافق کرد.
🔴
درواقع نساجی اینجا به لحاظ مالی داره سود میکنه و با زرنگی تونسته کسری رو بگیره و بعد به پرسپولیس بفروشه.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135633" target="_blank">📅 00:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135632">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
❗️
جزئیات عجیب از هایجک کسری طاهری توسط نساجی!
🔴
فرهیختگان مدعی شده پیمان حدادی دو روز پیش به باشگاه روبین کازان نامه زده و خواستار جذب کسری طاهری به‌صورت قرضی و بدون پرداخت مبلغ، یا انتقال قطعی با ۷۵۰ هزار دلار شده بود.
🔴
اما در ادامه، زندی مدیرعامل نساجی…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135632" target="_blank">📅 00:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135631">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
طاهرخانی فرد نزدیک به باشگاه :
❌
یکی از مدیران باشگاه پرسپولیس این موضوع رو تایید کرد و کسری هایجک شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135631" target="_blank">📅 00:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135630">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135630" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135629">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
فرهیختگان:
❌
باشگاه پرسپولیس امروز تازه نامه نهایی رو واسه خرید کسری طاهری زده، در حالی که شهاب زندی مدیرعامل نساجی ۴۸ ساعت قبل نقد پول رضایت‌نامه قطعی رو پرداخت کرد و انتقال رو نهایی کرد و امروز هم کارت بازیش رو گرفت... حالا هم به پرسپولیس گفته نیم‌فصل…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135629" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135628">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
فدراسیون  فوتبال روسیه آی‌تی‌سی کسری طاهری رو تو سیستم tms برای باشگاه نساجی مازندران صادر کرد و نساجی زودتر برای جذب کسری با روبین کازان بسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135628" target="_blank">📅 00:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135627">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
فرهیختگان:
❗️
مدیران باشگاه نساجی با روس ها ارتباط خوبی داشتن و کسری طاهری رو ۸۰۰ هزار تا خریدن و می‌خوان با 1.2 میلیون دلار به پرسپولیس بفروشن.
❌
امروزم کارت بازیش واسه نساجی به فدراسیون رسیده و تا نیم‌فصل حق جدایی از نساجی نداره
😐
😐
😐
😐
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135627" target="_blank">📅 00:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135626">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
طاهرخانی فرد نزدیک به باشگاه :
❌
یکی از مدیران باشگاه پرسپولیس این موضوع رو تایید کرد و کسری هایجک شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135626" target="_blank">📅 23:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135625">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
طاهرخانی فرد نزدیک به باشگاه :
❌
یکی از مدیران باشگاه پرسپولیس این موضوع رو تایید کرد و کسری هایجک شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135625" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
فدراسیون  فوتبال روسیه آی‌تی‌سی کسری طاهری رو تو سیستم tms برای باشگاه نساجی مازندران صادر کرد و نساجی زودتر برای جذب کسری با روبین کازان بسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135624" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
برگام
🚨
فرهیختگان: کسری طاهری به نساجی مازندران پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135623" target="_blank">📅 23:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
فرهیختگان: یه باشگاه لیگ برتری دیگه کسری رو خریده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135622" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135621">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
پس چرا خودش میگه فردا با پرسپولیس میبندم
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135621" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135620">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
فرهیختگان: یه باشگاه لیگ برتری دیگه کسری رو خریده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135620" target="_blank">📅 23:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135619">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
انتقال کسری طاهری به پرسپولیس منتفی شد!
🔖
فرهیختگان: این مهاجم جوان در ۲۴ ساعت  گذشته به عضویت یک باشگاه دیگر ایرانی درآمده و عملا طبق قوانین رسمی فیفا اجازه پیوستن به پرسپولیس ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135619" target="_blank">📅 23:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135618">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135618" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135617">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135617" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135616">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
فوتبالی: وحید امیری از باشگاه خواسته یه فصل دیگه بمونه تا با پیراهن پرسپولیس خداحافظی کنه. خودش هم گفته حتی اگه بیشتر نیمکت‌نشین باشه، مشکلی نداره. حالا همه‌چیز به تصمیم تارتار بستگی داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135616" target="_blank">📅 23:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCENLmiVuWNz-ANrEQuow7qzEvXBilg3c759T9GfxSyCXgWnhTUOc2FQdNo-0QlkV5MWanmo5_X5MwEKszDe40t3jk51jJuDuAQKlyoXol2I24nZmoUa6Gm2h6e3uOsO8J1RHNFGXCNK1qjqPJKO54sVvc4_LkDOuLGNYontF-hmW0MbbpPS_qL5_UZE3b4bs9M5MoYw2sBchew7K-OaHVdH56940SSbp_A4rOnOMV_m05UWQ45XQoywaKwYE4vX3-hbo5iomSE8XwdEDDwNqHIdG05AOaAPSit-lg-qseF2KXVEfHUeAVs9pXQ7onub7qQO1neAu7cpwwrPoCDK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کسری طاهری اولین برنده جایزه توپا (پدیده سال فوتبال ایران) شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135615" target="_blank">📅 22:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32499e90a2.mp4?token=OtbaUjIP9wMokN6JaVA_BQirlYK0XR9UAY0lWk3wxJHrUvEx0en8yenzr_PIb_gn1rY8NeUHRyTPhZGOI5j9TwQRcqoq1OzEZcQG_fDjrNF7RiYxmUHTNf8mP6xLH4OEKQPh2H1RC5Qcly4KbUEajA3fBrvGQKSsgMF9wwGX9_uZVfEjX89Ux1bveDxteSULVW6AKhCTh_LTKbgwNIbjxxFy1DiDD5hk1eGPsNSU_-kwQi9lHhVQb9AgTk_sFc3vuPzwE6j_Wd83Cius799On5J_uZLqesx2riBVRlsuQbW5IiKoDntmuQO3aPpuxC_E0yx7RqJPjjcBCCayoKm98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32499e90a2.mp4?token=OtbaUjIP9wMokN6JaVA_BQirlYK0XR9UAY0lWk3wxJHrUvEx0en8yenzr_PIb_gn1rY8NeUHRyTPhZGOI5j9TwQRcqoq1OzEZcQG_fDjrNF7RiYxmUHTNf8mP6xLH4OEKQPh2H1RC5Qcly4KbUEajA3fBrvGQKSsgMF9wwGX9_uZVfEjX89Ux1bveDxteSULVW6AKhCTh_LTKbgwNIbjxxFy1DiDD5hk1eGPsNSU_-kwQi9lHhVQb9AgTk_sFc3vuPzwE6j_Wd83Cius799On5J_uZLqesx2riBVRlsuQbW5IiKoDntmuQO3aPpuxC_E0yx7RqJPjjcBCCayoKm98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اشک های مجید عیدی در مراسم معارفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135614" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135613">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecbd7633.mp4?token=Gk6M414jcGZsOwi5yZwP_YC8gRUhW2v91NpO8iZLYjYP3R23GIEjjSgqTRHqBKjegk8k3bN-Fy_vIzMBJGkBeKmVQAqpY-rhKqs16TGdeVzYvYFlTteXb8cQ7CTC9stZyqhxwCQZJlZZ1XaK99MUoBFikjQwiuIIBdqTwJhbx_THv9F46A1-JISCaUxzXsAAyYxP8yiwLcBt4CyUKv7E5fKG1iOfIoXAb5tJgiusXQAtsE1M-0RWbByGOcMQb0IEvGNPgHd00bzLkQaNPSeN1GJNZj7pCIAowj0AChvP4akekpxBE39tEgnJtFNDEJAguKjje1ZRgVOxcsGlxrgiZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecbd7633.mp4?token=Gk6M414jcGZsOwi5yZwP_YC8gRUhW2v91NpO8iZLYjYP3R23GIEjjSgqTRHqBKjegk8k3bN-Fy_vIzMBJGkBeKmVQAqpY-rhKqs16TGdeVzYvYFlTteXb8cQ7CTC9stZyqhxwCQZJlZZ1XaK99MUoBFikjQwiuIIBdqTwJhbx_THv9F46A1-JISCaUxzXsAAyYxP8yiwLcBt4CyUKv7E5fKG1iOfIoXAb5tJgiusXQAtsE1M-0RWbByGOcMQb0IEvGNPgHd00bzLkQaNPSeN1GJNZj7pCIAowj0AChvP4akekpxBE39tEgnJtFNDEJAguKjje1ZRgVOxcsGlxrgiZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شنیده ها :
⌛️
باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر خواهند کرد. …</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135613" target="_blank">📅 22:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
پرسپولیس با سه بازیکن جدید به توافق رسید.
🔴
به گزارش قرمزآنلاین، کسری طاهری در پی توافق با روبین کازان در آستانه معارفه شدن از سوی باشگاه پرسپولیس قرار دارد. روبین کازان رضایت نامه قرضی او را صادر کرده است.
🔴
رقم پیشنهادی ۴۰۰ هزار دلار بود که با چانه زنی…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135612" target="_blank">📅 21:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135611">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO4tg0Mo7l-YY_1VOa_-odEtSxh1N5BYFNEdewKr970iFkk4SuVkjXyQfr-5jikVC3XERJJM_3nrXu1o74C4O21ro03poTfM9EIwfhAHOyIaQoG_p1E3rkQUADphH2o1gCjCq5gqWCvMt5-0LI_ts2-etsaKHJm-fCQLgfYjIJa5V5Bi8NWfxvnzPPODO-fvUgQ4Tq_YrmnUJElOg8-3t5Q2MgNiRTF4HauDDr-nd-tMOY5LCevG-R2sOs_H3bXhJOFF2H0sDXSG8zlBDaPcjyVl33Q_K6R3eQFuWRj4T-Y0GH4-CastIGY-LXbnJnY37-pOc7ijNLvy2HJhPNXdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیسی‌ها عصر امروز تمرینات خود را در حالی پیگیری کردند که پیام نیازمند و محمدحسین کنعانی‌زادگان پس از حضور در جام جهانی ۲۰۲۶ به تمرینات تیم اضافه شدند و کریم باقری نیز در جمع اعضای کادر فنی حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135611" target="_blank">📅 21:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135610">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
مجید عیدی : 7 سال منتظر بودم به پرسپولیس بیایم/  قراردادم که تمام شد منتظر بودم این اتفاق بیفتد و من به پرسپولیس بیایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135610" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135609">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مجید عیدی با عقد قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135609" target="_blank">📅 21:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135608">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
مهدی تیکدری : خدا دستم را گرفت که به استقلال نرفتم/ خوشحال پیراهن پرافتخار ترین تیم ایران را می پوشم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135608" target="_blank">📅 21:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135607">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
❗️
مهدی تیکدری: بهترین پنالتی‌زن ایرانم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135607" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135606">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
پیمان حدادی : فردا یا پس فردا با آقای علی علیپور برای تمدید جلسه داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135606" target="_blank">📅 21:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135605">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
پیمان حدادی : ما به میلاد محمدی پیشنهادمونو دادیم فردا آخرین فرصته که قرارداد رو امضا کنه اگه نکنه از لیست تیم خارج میشه این پرسپولیسه که واس بازیکن تعیین تکلیف میکنه نه بالعکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135605" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135604">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
خبرورزشی: مسئولان باشگاه پرسپولیس و مهدی تارتار علاقه دارن که ترابی رو بیارن پرسپولیس و مذاکرات رو هم شروع کردن و پیگیری هایی انجام دادن ؛ الان پرسپولیس در حال استعلامه که که ببنین ترابی قرارداد دارد با تراکتور یا خیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135604" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135603">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
قدوسی: پوریا لطیفی فر جذب میشه و فصل آینده تو پرسپولیسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135603" target="_blank">📅 21:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135602">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135602" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135601">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8sQU9WFYvbIeN1VKKQkq7n4P8zJEbCuiVt9fOWj7BOVV4p6L6mPXEr0rVmCzwDsnO7yj6ht7ZDAZEGkQexRq1hduhFu7Rnq-WBT3ww8RYLo6kJG--jjKx3kUrI_JMxCIUVaJvln63TWSW9Uz5YkVLlQKmBcKI0PdSsSdrEIj8PVHbnavCD1KDOJxXUCbHPLhVOjOKwLYCyu2QX2jv8bVY8_Blwj58OE4m0Q2BkdCIX_bHI3CRwxU9PMMoSwtPbHUsx1XJXvI-xMCbfCaJ53u1xdkyOqico9YcDud85mhHRuewAMnw8E1k3VlZOY3N_CGS301eIW2iv47IVuUYqtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135601" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135600">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
دونالد ترامپ: دستور داده‌ام در صورت موفقیت جمهوری اسلامی در ترور من، آنها را با قدرت بسیار زیاد بمباران و ترور و نابود کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135600" target="_blank">📅 19:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135599">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
بعد از جام جهانی قرارداد امیرحسین محمودی هم از لحاظ مدت و هم از مبلغ افزایش خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135599" target="_blank">📅 18:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135598">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
میلاد سرلک به شکل توافقی از پرسپولیس جدا شد
🔴
پس از مذاکرات انجام‌شده بین مدیریت باشگاه و میلاد سرلک، هافبک تیم فوتبال پرسپولیس، طرفین به توافق نهایی برای فسخ توافقی قرارداد دست یافتند.
❌
در جلسه‌ای که امروز برای بررسی وضعیت قرارداد وی برگزار شد، با موافقت…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135598" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135597">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🔴
پیشنهاد از اندونزی برای سرمربی اخراجی سرخ پوشان
❗️
❗️
اوسمار ویرا که به تازگی از پرسپولیس جدا شده از باشگاه پرسیپورا اندونزی نایب قهرمان فصل گذشته لیگ اندونزی پیشنهاد دریافت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135597" target="_blank">📅 18:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135596">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
فووووووووووووری از قدوسی
🔴
حدادی میخواد از بین علیپور و سرگیف یکی رو حفظ کنه و اگه علیپور تمدید کنه سرگیف جدا میشه 🫪
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135596" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135595">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
هو شدن عیسی آل‌کثیر توسط هواداران پرسپولیس هنگام اعلام ترکیب ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135595" target="_blank">📅 18:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135594">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-EcrOLfP8sSyP-db7Heey3K5ACBpNaBjanfzj16-qjaxHuX1eglX2n5sDnpukVQu35jrODp5JVPhjucx7wL8Fa0udBElWpnI6-VjgFpPa8V1tvNdWdEWp12SMzPYILM8lrivlfIpWFZSGwTo7I76FMcKf1HHIgAQBVb2AWVkQfsepIip08s933JjXglEk7UR7oM6WpODlawple_eME884P2V6xWiQA6OZOdEBdzNTmx5zBkzi3YwWmDV30tn4wPQgxrDha9RIMszsKb8aeAWLpa7cnU-4wk4mk-v8VoRV5pfoDjpneW7nkJOW5pFbSbHm70TcGkvwl7n6XJ0Hgnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبری تکان‌دهنده برای همه باشگاه‌های جهان؛ علیرضا جهانبخش بازیکن آزاد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135594" target="_blank">📅 18:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135593">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🔥
به ادعای فوری خبرورزشی ترابی با پرسپولیس توافق کرد و تموم
🚨
جواب استعلام ها بیاد و اگه اوکی باشه رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135593" target="_blank">📅 17:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135592">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135592" target="_blank">📅 16:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135591">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135591" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135590">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری از عادل فردوسی‌پور:
🔻
ترابی با پرسپولیس به توافق ۲ ساله رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135590" target="_blank">📅 16:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135589">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔽
رسانه‌های داخلی: ترابی در آستانه پیوستن به پرسپولیس قرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135589" target="_blank">📅 16:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135588">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
فوتبال ۳۶۰ | ترابی در آستانه بازگشت به پرسپولیس؟
❌
طبق ادعای فوتبال ۳۶۰، تمدید مهدی ترابی با تراکتور انجام شده اما هنوز ثبت نشده و این بازیکن در حال حاضر آزاد محسوب می‌شود.
❌
پرسپولیس مذاکرات جدی و مثبتی با ترابی داشته و گفته می‌شود توافق نهایی روی مبلغ…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135588" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135587">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
علی علیپور با پرسپولیس به توافق رسید.
🔴
خبرگزاری ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135587" target="_blank">📅 16:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135586">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG-fpqc4AenB2djIWgY1lmAVH_vLrmMxRltzawBoVva3FsjiCNfr5kQhMmC70TixxSuu9F3SMNH41zEpzF6Wv5UrJ_3Cft0J2rSbiSibe0OiMJgUN86jEhmBA7bQCOYIafiIMY4_Ewm26IiPe0ZU2KuV5aZOdECWULnrk_vr3zaLtPcbKkMTAclLvQyflCd64t2qSrO83jSKDJNM2DT2TYt-DEngUfzTtRgyu7VCzIh_Jb61L7eJMGPWtoncQEbjCEMPtQhhFCyiys62eHx0fPvID0oQPMr9Xypcc3fvyN7ky_PNuRxuZk-x_6qrYGTjNwigzL12hwqfDtgxyRT-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍
رییس آکادمی؟ محسن خلیلی
✍
معاون ورزشی؟ محسن خلیلی
✍
مدیر نقل و انتقالات؟ محسن خلیلی
✍
مسئول مذاکره کننده؟ محسن خلیلی
✍
سرپرست تیم؟ محسن خلیلی
🔴
🔴
محسن جون پستی هست که تو باشگاه برای خودت نگرفته باشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135586" target="_blank">📅 15:41 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
