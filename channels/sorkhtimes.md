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
<img src="https://cdn4.telesco.pe/file/QhBahW78tnnvtXEaJRcigCOOhEBKcrOEhYm9EEG46Z4UXBNu97Z_pHVHUn16PYNlFugGGFxHcam57mRylXjoBIWiwchCJF-A9upKRJpMYwlVP-Imte7tIIx6aPZSqPVknOAfvd7Q_mA-v2V-CoyNMPsmDvGw6PuPMbRKQTPz_GJqeCtmJJtgS7RsfjQTeb587KqDHWlJrhw2D6QC1S5iEpAqJZeUkLpeJ-IFexrZYU65I0tz2txoS370Pq97Z94vBeT7544763tOfHEmbT8bv4XLEL3tGc_P8PognjisSOqRph3Ac9ZnAXrHVrWyXQk-pSdrPJDz9IY0ne7wHw-qnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 16:52:44</div>
<hr>

<div class="tg-post" id="msg-138483">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حدادی: دوران بازیکن سالاری و دخالت هوادار متمول در پرسپولیس تمام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/138483" target="_blank">📅 16:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138482">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
حاشیه جدید برای سرمربی زنان پرسپولیس
❌
باشگاه ایستا البرز مدعی شده نیلوفر اردلان با این تیم قرارداد سه‌ساله داشته و فسخ یک‌طرفه قراردادش قانونی نبوده است.  این موضوع در حالی مطرح شده که اردلان چند روز پیش به‌عنوان سرمربی تیم فوتبال بانوان پرسپولیس معرفی شد.…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/138482" target="_blank">📅 15:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138481">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
جدیدترین گزینه پیشنهادی پرسپولیس
✔️
✔️
امیرحسین ریوندی دفاع چپ ۲۲ ساله زسکا مسکو روسیه به تازگی به مهدی تارتار معرفی شده تا نظر نهایی خودش بابت انتقال اعلام کند
✔️
✔️
این بازیکن در بازی اکادمی کیا با زسکا مسکو مورد پسند روس ها قرار گرفت و در فینال جام حذفی…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/138481" target="_blank">📅 15:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138480">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
⭕️
قرعه کشی لیگ نخبگان آسیا شروع شد؛
🎁
حریفان استقلال ایران: العین، السد، شباب‌الاهلی، نفتچی
🗣
🗣
کیسه خورد به پدرش العین و السد با عفیف و تیم سردار و سعید عزت الهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/138480" target="_blank">📅 15:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
با رای کمیته انضباطی دیدار استقلال تهران و مس شهربابک 3 بر 0 به نفع مس شهربابک اعلام خواهد شد. این رای قطعی و ظرف چند روز آینده توسط فدراسیون فوتبال اعلام خواهد شد/ همشهری  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/138479" target="_blank">📅 15:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EalFJza7NNKKSPkb4rlyyz-UegQatbFA-71m0o9SMg-W-KOzwFMKGWBTT8cSaHQXfKJFCdS5Iw3EAcZQhVAzwKnJzWB7TVL68VfoHpz5U22RGw9QeaNwoW8VWKHtqTABQSOgypK1dByrI_7D4QwnBjpfKB7P6bv0OB94dZfzy-hGPFoZ_orErblSutYLtFJ_B2JTaPpRvR6fvuCXjH4ZFL1lX0mq5C__d35B7YMbeSxR5UySGpUzzlI_qoFdtK5KrbHvqhq3jK95Mg3U6Xj8lqT0PQnw0NjqhPWWBzXYmebNRPov2Kpv_5YQ2Q-c3xcz6lyTwh-cz_vrHIX3WFc_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
⚽️
⚽️
خوشامدگویی باشگاه پرسپولیس به استقلال خوزستان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/138478" target="_blank">📅 15:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138477">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
شهاب زندی مدیرعامل نساجی: به مدیران ارشد استقلال هم تاکید‌ کردم مستنداتی دارم که آسانی‌ بازیکن غیرمجاز است و اگر مقابل ما امروز حتی یک دقیقه هم به میدان برود از آنها شکایت خواهیم کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/138477" target="_blank">📅 14:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/138476" target="_blank">📅 14:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138475">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/138475" target="_blank">📅 14:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138474">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/138474" target="_blank">📅 14:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138473">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
حریفان تراکتور: شباب‌الاهلی، الغرافه، الوصل، پاختاکور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/138473" target="_blank">📅 14:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138472">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6XWQtIXEgCZCyK1dcOLA0t7a5TSlLEL-GrIKvWZYDTiF_W9Oe-9Rd8zht-iquyZkIvLvOPGik-w6WNcs-khn0et5gek1uhBt_BeZbBbKtgpTiYV3VrWHBf4hJ1Vx2ZaaUoY8DSE6f4mVrRM-VCOze50i2L21KimvMTkdNd2i0_nCwayVPIARSd1Pf6yAiUqRwtf6PQZMRrq8C8nLRfzbACwUDWBmPJKH9m-K_GVCBWocZAiK6vHNE7dJDJ6ZmxtlRTmFVc2lGcmqo18RkMUtp8yDejEslI_fkhBUbNiLUxBrTcpI3OGAvpTyh-tHT8WFnwWBf949g9B9HWfRCTPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽
جنگِ آبی‌ها در جهنم وطنی!
نساجی به‌دنبال شگفتی، استقلال به‌دنبال شکار ۳ امتیاز؛ قائمشهر امشب شاهد یک نبرد تمام‌عیار است!
⚽️
لیگ خلیج‌فارس ایران
[
نساجی
⚽️
🆚
⚽️
استقلال
]
⏰
سه‌شنبه ساعت ۱۹:۱۵
🏟
استادیوم وطنی قائمشهر
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/138472" target="_blank">📅 13:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
✔️
حریفان استقلال و تراکتور
✔️
السد
✔️
العین
✔️
نفتچی
✅
شباب‌الاهلی
✔️
الوصل
✔️
الغرافه
✔️
پاختاکور
✔️
الشمال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/138471" target="_blank">📅 12:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
مبین دهقان در مصاحبه با همشهری انلاین اعلام کرد دوست دارد به پرسپولیس بازگردد
🔄
الوحده هنوز پاسخ نامه پرسپولیس را نداده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/138470" target="_blank">📅 12:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
باشگاه تصمیم گرفت از رفتار اورونوف چشم‌پوشی کنه و حاشیه رو ادامه نده/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/138469" target="_blank">📅 12:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭕️
⭕️
⭕️
😰
😰
شانس
🚨
🇮🇷
🇸🇦
رسمی؛ استقلال و تراکتور با خوش شانسی تمام به تیم‌های عربستانی نخوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138468" target="_blank">📅 12:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
⭕️
⭕️
😰
😰
شانس
🚨
🇮🇷
🇸🇦
رسمی؛ استقلال و تراکتور با خوش شانسی تمام به تیم‌های عربستانی نخوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138467" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138466">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
⭕️
قرعه کشی لیگ نخبگان آسیا شروع شد؛
🎁
حریفان استقلال ایران: العین، السد، شباب‌الاهلی، نفتچی
🗣
🗣
کیسه خورد به پدرش العین و السد با عفیف و تیم سردار و سعید عزت الهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138466" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138465">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
تا دقایق دیگه ببینیم کیسه و ترتر به کدوم تیما میخورن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138465" target="_blank">📅 11:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138464">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
🤥
🤥
گفته میشه مبین دهقان آخرین خرید پرسپولیس هست و رضایت‌نامه اش هم زیاد سنگین نیست!  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/138464" target="_blank">📅 11:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138463">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
الوحده تمایل بیشتری داره که قربانی رو به اروپا بفروشه؛ تکلیف نهایی همه چیز تا ۴۸ ساعت آینده مشخص میشه/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/138463" target="_blank">📅 11:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138462">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
سه بازیکن برتر زمین در دیدار پرسپولیس _ شمس‌آذر از نگاه متریکا :
✔️
✔️
محمد عمری: 7.84
✅
✅
ابوالفضل جلالی: 7.81
✔️
✔️
محمدمهدی محبی : 7.61  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/138462" target="_blank">📅 11:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138461">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
سپهر خرمی: پرسپولیس امروز آخرین رایزنی رو برای جذب محمد قربانی از الوحده خواهد داشت
⏺
آخرین تلاش برای جذب بمب نقل و انتقالات که میتونه تیم رو تکمیل کنه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/138461" target="_blank">📅 11:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
کنفدراسیون فوتبال آسیا حق انتخاب کشور میزبانی رو از استقلال گرفت، مدت زمان معرفی استادیوم دارای شرایط AFC توسط استقلال به پایان رسید و دیگر استقلالی نقشی در میزبانی خود ندارد!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/138460" target="_blank">📅 11:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
کنفدراسیون فوتبال آسیا حق انتخاب کشور میزبانی رو از استقلال گرفت، مدت زمان معرفی استادیوم دارای شرایط AFC توسط استقلال به پایان رسید و دیگر استقلالی نقشی در میزبانی خود ندارد!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/138459" target="_blank">📅 11:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf88a6445e.mp4?token=kCAAfxPmbuoNHarfvaerLZw-tuRtIT2VqSdMKVReZ-nSHsem8yCrw7ifY8l_AUw0AqVDq7ObH79NBGh0QDzXGLfqApf336-DrlLdcYuIWz3rqONPlQwK-a9wkDClwkfIWeY9a7PFt14Bda70MCxgyqgbIT-VNk3OnfdisvEcrul_bIixLSS0h4IKXug-WAMkeUxZNbavegD7Xq5yecuGzgUSiq1JOUXQvzY1AtSOKdVaW4fDti5hJ5eVBXVhHadQrBt55nqTsoty57TPaW-zFwoQe_da5fomhAG15dLQl6vmLjNVNZKyNpXFH3lWriMtndpFSeS0rl5wyRKcWsg6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf88a6445e.mp4?token=kCAAfxPmbuoNHarfvaerLZw-tuRtIT2VqSdMKVReZ-nSHsem8yCrw7ifY8l_AUw0AqVDq7ObH79NBGh0QDzXGLfqApf336-DrlLdcYuIWz3rqONPlQwK-a9wkDClwkfIWeY9a7PFt14Bda70MCxgyqgbIT-VNk3OnfdisvEcrul_bIixLSS0h4IKXug-WAMkeUxZNbavegD7Xq5yecuGzgUSiq1JOUXQvzY1AtSOKdVaW4fDti5hJ5eVBXVhHadQrBt55nqTsoty57TPaW-zFwoQe_da5fomhAG15dLQl6vmLjNVNZKyNpXFH3lWriMtndpFSeS0rl5wyRKcWsg6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاس گل های برتر هفته اول در لیگ برتر در فصل ‎1405-1406 با حضور پاس‌گل ابوالفضل جلال به شمس آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/138458" target="_blank">📅 10:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
✅
پ.ن استقلال و تراکتور بخورن به الهلال و النصر بخندیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/138457" target="_blank">📅 10:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/138456" target="_blank">📅 10:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
قیمت بلیط ورزشگاه قلعه حسن خان: 300 هزار تومانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/138455" target="_blank">📅 10:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5ezt_tJJMzAS9d7BRnmrIIW641RqV2j8LjkqPnEJSh48Q4RY2glyFo9IVaf4iJ8rjUiSiSlv9BAE1Cp92Tt_mvBhncN4JeFfY67jxcUs14z0mM0LJXbs1ineVat-oP-LMxqcfDwfmX8Ga66uhnBlfE8j5hkqkMt5IrjjZoklCsgcgWrUegwkVlqN5TU0sHlvmCcxMsTfSRUoGCyeS95Vc4AHFLlh1qn6PzHkFy98VW_Gp0fW0szvZAuYKsVfCKu0NOGzcICVdz1Wx8ZkSw7_QKifSHEfI67LfXh07896UYLLvlsnnIeuN2lwOVqVNqIBTkF4LB19YD1UdU5boowjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/138454" target="_blank">📅 10:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">موجودی حساب : ۵هزار تومن  ادعا : ۱۰۰میلیارد دلار  ۱میلیون دلار بدینننن قربانی، ۳میلیون بدین حسین نژاد ۴ میلیون بدین قلی زاده ، وای تورو خدا اینار جذب کنید، دلالی کنید پول بیت المال رو ببرینید توش، من تو جیبم عنکبوت داره روپایی میزنه اشکال نداره بدید فوتبالیستای…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/138453" target="_blank">📅 10:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">موجودی حساب : ۵هزار تومن  ادعا : ۱۰۰میلیارد دلار  ۱میلیون دلار بدینننن قربانی، ۳میلیون بدین حسین نژاد ۴ میلیون بدین قلی زاده ، وای تورو خدا اینار جذب کنید، دلالی کنید پول بیت المال رو ببرینید توش، من تو جیبم عنکبوت داره روپایی میزنه اشکال نداره بدید فوتبالیستای…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138452" target="_blank">📅 10:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_g1vJPyTx5vo4QlD3pVGT5oU505I3wQqBmrsxmlXkT3ZnNXy6S8osNV4I9C39uySefDt_oVI-cAQza0rZHik1fhKicuy3MeOLsbFb_JLsQaq-UTe-I_2dNvtEttCwaXDnMNR1ldLVrEvQYzjTdSMkkO57puZrrjqeRrqGz0cmH_8MxRio9eifiHKxZyljbbIyl3oep7iQf4SEzjUhjeeGvfNYekXUzdvV4y6kAvWf7UVhbvOuKeaacCg_prOK6N1rgxWNeFN23zB0NBqvRZ_lRCb4F4Du8PSth97TI0RKihLyyVy3bTdLHjpS79QgUwkr8afrJ3vDxBvwtsvWsucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس در یک پرونده حقوقی برنده شد
❌
❌
باشگاه پرسپولیس اعلام کرد دعوای حقوقی مطرح شده از سوی یک شرکت علیه باشگاه پرسپولیس، در دادگاه تجدید نظر استان تهران رد و رأی به سود سرخپوشان صادر شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/138451" target="_blank">📅 10:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMhmdrza</strong></div>
<div class="tg-text">موجودی حساب : ۵هزار تومن
ادعا : ۱۰۰میلیارد دلار
۱میلیون دلار بدینننن قربانی، ۳میلیون بدین حسین نژاد ۴ میلیون بدین قلی زاده ، وای تورو خدا اینار جذب کنید، دلالی کنید پول بیت المال رو ببرینید توش، من تو جیبم عنکبوت داره روپایی میزنه اشکال نداره بدید فوتبالیستای ممادر خوب بخورن
🤣
🤣</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/138450" target="_blank">📅 10:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5L1oZDSwIC7T0-2itoqoCNqsMy3nzGQs3hlJWpAVGRC9y6q7WXK1-ryd7jSFEl9HGG9DDcH7Bci2y2U49T1-nZg1PT8dxeXhcTT-rXHW2uPO5Y9TR5uYoUcON1mJS43jlx-5rn_ahKiMBAUrTiU7RKIiTX7OuIy3Tgl0lCn7N2MCw9L6J5S8hMF70XQ7MwvKOr6IW9HbMb3obDDUhELG-EyeDkyVjU5iI-kGriaHj1fK2o-ti0zoK-Cw-a7el2khshsx1YYrzxohfeMwi7TSJ0J-JZKcMBpkpsxmfeS2A8j_hI6x4TAUij28Uc6MMApicAxGKGh6VUIDJCRAljDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بیانیه باشگاه گل‌گهر علیه میثاقی در ماجرای تورنمنت 3جانبه و پرونده چادرملو
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/138449" target="_blank">📅 10:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddw9ImfEqgci73GymsDgoJOmXw7PWC9RoqJWCrG-A004ili0e0H5XQHfC4M1918qnJWnnAHJw_x_mR5zEK87YlGLelhvH1zFTqvtAu8u7fUYIk-vLwtYEGlupsqVgeQwdf_N4B68YQ2KWRjv1NjMfij8KrINK2YSafANTQaTHVVNRkkBb0PEIN-oVciU-fk-qmewmMjdKeHFds08Jl7I4firKMOu4anB-tzeXQgI_eoeA93dMceAwQrQCGDebz1jtzsQ7jG27aEnDLwUnmTmb9753dVlBvp2cp3s5F3Mabdsdqo8f3L165CoUFey589QHFlqfntF7Ki1hZHfbFizjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازی های امروز لیگ برتر:
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/138448" target="_blank">📅 10:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
💸
سود 355 هزار یورویی باشگاه نساجی از فروش 2 بازیکنی که حتی 1 دقیقه برای این تیم بازی نکردن!
🔴
دانیال ایری:
🔄
خرید با 405 هزار یورو
🔄
فروش با 600 هزار یورو
🟡
کسری طاهری:
🔄
خرید با 703 هزار یورو
🔄
فروش با 863 هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/138447" target="_blank">📅 10:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
✅
پ.ن استقلال و تراکتور بخورن به الهلال و النصر بخندیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/138446" target="_blank">📅 09:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اصلا چه جوی راجب باشگاه؟ باشگاه مگه بد عمل کرده تو نقل و انتقالات. یه تیم تو زمین داریم یه تیم کامل رو‌ نیمکت. پنج ، شش تاهم بیرون از لیست که هرکدوم یه زمانی فیکس بودن. همین هفته اول ۱۶ نفر بازی کردن که همه خوب بودن ، اورونوف ، سرگیف ، باکیچ و چندتای دیگه…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/138445" target="_blank">📅 09:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromhamed</strong></div>
<div class="tg-text">اصلا چه جوی راجب باشگاه؟
باشگاه مگه بد عمل کرده تو نقل و انتقالات.
یه تیم تو زمین داریم یه تیم کامل رو‌ نیمکت.
پنج ، شش تاهم بیرون از لیست که هرکدوم یه زمانی فیکس بودن.
همین هفته اول ۱۶ نفر بازی کردن که همه خوب بودن ، اورونوف ، سرگیف ، باکیچ و چندتای دیگه بازی نکردن.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/138444" target="_blank">📅 09:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/138443" target="_blank">📅 09:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
سپهر خرمی: پرسپولیس امروز آخرین رایزنی رو برای جذب محمد قربانی از الوحده خواهد داشت
⏺
آخرین تلاش برای جذب بمب نقل و انتقالات که میتونه تیم رو تکمیل کنه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/138442" target="_blank">📅 08:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD1PbUHk73sCW6R3RwvXpLM4cwktVz3zZl4qjzv8MQz-PjDs5mIuKm3Xaoxs3FTjY6Szp_cR8t0wmup_np7_itRCpJ7e4j7YOQbTPUS-nqxz_NXk_t7YBE95h8SmRo6ZtTr4FoUAv34b30-TKftWyONvUm-lTyr2P7b56585sxOuhfxhShiDYpBEIZbYqvSAg81fxcsXSKSw-kFi17n1-GOeHHcOXC4k8emoEhrh-SzlfuQJh6ReZosJYgxMekvCO-860bP1XZSZnwlUgEWlEOmbNS4c7AVLee6LeG6uOiAo_sI6lGsv2TyCnk3c0hwvxdyFH_W091JzT8MrP_QSkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/138441" target="_blank">📅 08:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnx9Os0CU66NdubOp6YrGspapfzwkU7goRYSIpJMxR_hbrx2fyX2m7dL8Bsf1975h2blJFkbh4imB2Zxy9-hjPSWjSAM-iG3PDpvpElUhpUbGLO8iDBs8DlRUP2kExtno5H-34dnEuOMFU1UvZQfjXoehxns7rmIGvw4wZ-OdXWHFdT4OkkA9yT4VtiasHEZ1nYlG1LvyjjVPtFYl_TmuIsOM1g6XWmDdyPk0kz2s4HGVMFazQa9gdnITR2hfEadaIFTDyuhA99tC7E65IwCuCJg6G1HxNC-4JDY2PUcIcl1Wod77HeF_mxElVuOAQHNiwjXApk60A-EW5iAjantSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
رقابت‌های پرهیجان فردا فوتبال؛ از لیگ برتر تا نبردهای اروپایی!
🔥
⚡️
استقلال، سپاهان و تراکتور برای ادامه شروع قدرتمند به میدان می‌روند، و در سوی دیگر، فنرباغچه با لیون و دیناموزاگرب با وایکینگ می‌توانند جذاب‌ترین تقابل‌های فردا باشند.
چند بازی نزدیک و غیرقابل‌ پیش‌بینی هم فردا در پیش داریم؛ شبی که فرم، فشار و جزئیات کوچک می‌توانند سرنوشت بازی‌ها را عوض کنند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فردا همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138440" target="_blank">📅 02:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOVOH6B526BofsOZVUuYF6aeGxkNi9e2092VCF8XrHJL_mAzyNCfdXiU7wqdqekecZvo-rA5mbDNhE3j2eYvIlZ2rT1du43zb6Kp8j5fsBLhBsRPgOFn7rnI12fB7Wib0I9MiT0fG0-ueaAjgaQtwg8x3Q9opXqMmyTtgq1BAPNCher39rNg6OksjMscbUX0LLk3CaqXnAHE_Zz208WDNe94QAr1GrHHabeou3qUovzUY16-j_gpeDEo_mngv7IkQaeqbvSTJNhW5Rxy0zdbCF6wa7m43jXNZ4AmQf3Xcw49OzSj1-ezGiv5YrurZSaB-WYKUZif3Dks7Lr1uZe8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
دردسر شیرین تارتار؛ ۴ مدافع برای ۲ جایگاه
‼️
⬇
⬇
⬇
با اضافه شدن دانیال ایری، تارتار حالا کنعانی، زارع، ابرقویی و ایری را برای قلب دفاع در اختیار دارد. زوج کنعانی و زارع در هفته اول خوب ظاهر شدند، اما حالا رقابت برای ترکیب اصلی جدی‌تر می‌شود؛ مخصوصاً با توجه به هزینه‌ای که پرسپولیس برای جذب ایری کرده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138439" target="_blank">📅 01:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
محرومیت علیرضا بیرانوند در دو دیدار ابتدایی لیگ نخبگان آسیا
🔄
🔄
علیرضا بیرانوند در دو بازی لیگ نخبگان محروم خواهد بود/ تراکتور در لیگ نخبگان آسیا کار خود را با پارسا جعفری شروع می‌کند
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138438" target="_blank">📅 01:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
✅
پ.ن استقلال و تراکتور بخورن به الهلال و النصر بخندیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138437" target="_blank">📅 01:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138436">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
کوروش اژدهاکش با قراردادی قرضی و یک‌ساله به نساجی پیوست؛
🔴
این بازیکن از عصر امروز در تمرینات نساجی حاضر میشه. / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/138436" target="_blank">📅 00:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138435">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiu_-0HdoZ9C2jwpJmCu7QB_4wSGmn0xOTb8yVmiVXnizUo7RD755thyFadp5bOyPlB4DXuwXLj5LGSPUS-mnTZIDX8P3x0gIjpWSpjbab4bW8hnMENEr_j2zIQSylbgjuwV8Y7ARJh86jAgPOzPQLj7BrdP52hzkzr9g18KyldbA66RL51EtA5xxq9rZzZK2TJnwOam1UUqPysDD0xNvb37WJVbwi11ikcvTjZMhcjpiaz6t2dSlAxrDYGoWkAHyz6qM01aVoKSGJ2paB6P4UAo10lIic5UY70B3U8b5iAgsISxb0k4zoJXJW9UgB_fO6-VOxba5_nhIjju3sFwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
سپهر خرمی: پرسپولیس امروز آخرین رایزنی رو برای جذب محمد قربانی از الوحده خواهد داشت
⏺
آخرین تلاش برای جذب بمب نقل و انتقالات که میتونه تیم رو تکمیل کنه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138435" target="_blank">📅 00:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138433" target="_blank">📅 23:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138432">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
❌
لیست بازیکنان آزاد ایرانی با حضور محمد محبی ؛ علیرضا جهانبخش؛ رضا اسدی ؛ مهدی مهدی پور ؛ مرتضی پورعلی گنجی و رامین رضاییان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138432" target="_blank">📅 23:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138431">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
کنفدراسیون فوتبال آسیا حق انتخاب کشور میزبانی رو از استقلال گرفت، مدت زمان معرفی استادیوم دارای شرایط AFC توسط استقلال به پایان رسید و دیگر استقلالی نقشی در میزبانی خود ندارد!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138431" target="_blank">📅 23:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138430">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138430" target="_blank">📅 23:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138429">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138429" target="_blank">📅 23:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138428">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ad56d37c.mp4?token=kKkdd8e02a6bX-BFrAJw1v-nk-Lk_axcOj6LNn1_fpjskie3q9Flr0zuYibQFg0by__kFIC2UpFH22gE2H2tq1T0BaFCNfXc8Xp7Rx18Bpig2uypRSYT2ng-y_K5SfDad74cyLlucyJNpEhAjUweMjUJ0HVjY5_l43JzxMjr5a6OcAIEgGX3j1rDnVuQI7F9fDV0Fsvkhp9sq7JQe8GpMnkGW5XZ0Eij8knjNnIzIXXXL8aPrVt8gLwQZgw1V7xyQR5R_yi8cmNjT4z5zM9g5ZsEMqp-o-0toBO9ikg4S05lDyQ4GwWq8sflbxmPxnuoirSOPnbQvKgK6uyFd3_jyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ad56d37c.mp4?token=kKkdd8e02a6bX-BFrAJw1v-nk-Lk_axcOj6LNn1_fpjskie3q9Flr0zuYibQFg0by__kFIC2UpFH22gE2H2tq1T0BaFCNfXc8Xp7Rx18Bpig2uypRSYT2ng-y_K5SfDad74cyLlucyJNpEhAjUweMjUJ0HVjY5_l43JzxMjr5a6OcAIEgGX3j1rDnVuQI7F9fDV0Fsvkhp9sq7JQe8GpMnkGW5XZ0Eij8knjNnIzIXXXL8aPrVt8gLwQZgw1V7xyQR5R_yi8cmNjT4z5zM9g5ZsEMqp-o-0toBO9ikg4S05lDyQ4GwWq8sflbxmPxnuoirSOPnbQvKgK6uyFd3_jyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
🧡
رامین رضاییان میان تشویق شدید هواداران فولاد با شعار « رامین، رامین، رامین ما دوست داریم » وارد خوزستان شد؛ فقط کلاه رامین رو ببینید
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138428" target="_blank">📅 23:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138427">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
خبرنگار: چرا کسری و دانیال رو خریدی!؟
🔴
شهاب زندی: من وظیفمه برای این هوادارا بجنگم. باید بهترین بازیکنا رو بخرم و باشگاه رو به سمت درامد زایی ببرم. شما نساجی را در سه سال آینده ببینید. قول میدهم بیشترین لژیونر و جوان را تحویل فوتبال ایران بدهیم
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138427" target="_blank">📅 23:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و استقلال خوزستان مشخص شد.
❌
❌
نشست خبری سرمربیان دو تیم در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:
❌
ساعت ۱۹، امیر خلیفه اصل | استقلال خوزستان
❌
ساعت ۱۹:۱۵ مهدی تارتار | پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138426" target="_blank">📅 22:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✖️
✖️
🤥
🤥
#شایعات
🖍
پرونده نقل و انتقالاتی باشگاه با جذب مبین دهقان بسته خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138425" target="_blank">📅 22:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gml0BeAekSk6L7Ro_bBnOeC9dbuk4ANOnnF1bYAEUu_btLpqR6as3KwSPoO7a6A4Ih4ZOYTxk_lcwvG1H4s13-oZyC91HXyglbYB7GJqjRuwnhELmqIssBv8va4ZaP98lKEsA88M0qMSAuO9ITPDAA7H67dgjl5ZZinSLqC7imnDTWkJJzpBC_T7QBVsbJmb5RkDfWR9UsqXCtE-c9wDPNpm-jutFhamPynuFUFKqVJN0Mz2koSw0VDlizqEsLosWkW-hM96DcG2liAurzXWiQpzGHwAxcdit2e8eL45T0duFsVvsTe4IT2PSVcE6UbC8HbeFSCDapC2tnoDoVJy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری تو تمرین امروز اینطوری ازش استقبال شد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/138424" target="_blank">📅 22:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
💢
💢
💢
به احتمال بالای ۹۰ درصد از بین مبین دهقان و محمد قربانی دوهافبک‌جوان الوحده؛ باشگاه پرسپولیس یکی رو قطعی جذب خواهد کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138423" target="_blank">📅 21:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyD_ObJWIfwovRILoF52q8pGVfPfjdiKdbUwX0yThG9QBLDKpysd-QRiQhr69fHrJHaG8IV4V9iRX2eZJe6fhw-uhO7Xjx_a0LidzaACh8Y_4sfi75s_XaFdchOKh8RFMMv9iKrvpRbRgoS1998ygfCcL3sZ_2qyHd4m176WAdc_90flkpII-0A8H7dqkpcPWe5DI2UGsuwfM80xeAfaL-sfZVL3ODlAXk04cwoZKoeYWV1NBWkA8vSU3ZeDiPtOg8jYiU9I1uYXdUTpHtXbmmvtglw_Qo_qiYtAdmVOqv7p9Xe1Tkp0gqaCrNIx0gRRt8QjQ62nf6n-b5folm5nHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
#تکمیلی
؛حاجی‌محمدی‌خبرنگار باشگاه تراکتور:علاوه‌برباشگاه‌پرسپولیس باشگاه تراکتور نیز علاقمند به‌جذب محمد قربانی ستاره‌الوحده است اما گلزنی او دربازی اخیرتیمش کار روبشدت سخت کرده و رقم رضایت نامه‌اش که زیر یک میلیون دلار تعیین شده بود به بالای یک میلیون دلار برده شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/138422" target="_blank">📅 21:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">➕
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
➕
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
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
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138421" target="_blank">📅 20:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
رامین و فولاد سر همه چیز به توافق رسیدن فقط یه مسئله کوچیک وجود داره اونم اینه رامین 150 میلیارد میخواد و فولاد 60 بیشتر نمیده یعنی حدود 90 میلیارد ناقابل اختلاف دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138419" target="_blank">📅 19:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138418">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138418" target="_blank">📅 19:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
گویا داره میره اهواز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138417" target="_blank">📅 19:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138416" target="_blank">📅 19:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
شنیده میشود مدیران باشگاه قصد دارند در صورتی که رقم قراردادی رامین رضاییان کاهش یابد و او تا ۴ شهریور با تیمی قرارداد امضا نکند او را جذب خواهند کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138415" target="_blank">📅 19:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
حجت کریمی مدیرعامل تراکتور: دنبال محمد قربانی هستیم و همه شرایط باشگاه الوحده رو هم پذیرفتیم ولی فعلا باشگاهش اجازه نداده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138414" target="_blank">📅 19:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
باشگاه تراکتور گفته اگه سپاهان کسری طاهری رو مقابل این تیم بازی بده به فیفا شکایت میکنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138413" target="_blank">📅 18:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
❌
پرسپولیس نامه زده به باشگاه الوحده و خواستار جذب مبین دهقان شده / فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/138412" target="_blank">📅 17:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
فوووووووووری
🔴
مبین دهقان‌ در لیست خروج باشگاه الوحده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138411" target="_blank">📅 17:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQJyoSzThzn8mgbCmifq8RlAuIvi97WN0XI8LuwfAkxfyAgCw_V8n06oI0H6Pnjw0uIYbziazJLosTnCXauYH2gpTtH-l01sdBSIU7fFvhaDzq8UoRnfKl95mxww_9JDqON7OkL8wCZb2BRg8pSlJhP7nwL9kO5WRZ7nRy3exxY_VUhnK5Y4yjNP6P-STCskN50X89UusXuRRddGoyeK-iLXLIn6PAhkJFxy1kMNSRNqswGbTA24HR7m38vSBt_osHQ-qwbVHXVnPit1JGeBTFF1Xe35NmiEZOzZz-uFWlZEtTB_4OdPJhyXiyMzgBxb0m2LVFij-17XPPpwYd0m9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
عشقم (دکتر جون )فقط یه قربانی
🥲
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/138410" target="_blank">📅 17:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138409">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqWEmpCoUJoycLxgQV9evr3jK3EtT1XOcV6iGUM-V0HPmmEuKmSDZoLyZtSALVCQDpwBdogeFY2qEAudBfmgSrFAM_3LDhhtUtCJ4TjvRsgkTYR-Qr4q4VAkj2hBoHvxtO8RbBNFlFDVzjwgC1_Q-cwJxisRLSN6xXnp575vfh0Wz3ZowRvAoFVMBDi6gxXwqCRq2zSA-5b_EJjG8nnr7pKmiiyokC2-2Wu6RiOTSIom1S6Vx_gAyrR8eLLm_Ybw03HX2ImM49uLEP4ayeGd4JfeG_PBvrGqnxOsOU32BN0wAAzoQgYdh1VIOBdSw-5ZqJC7O80fXqt6q538zjGkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس باارزش‌ترین تیم لیگ برتر شد
❌
پرسپولیس پس از خرید و اضافه شدن ایری، تبدیل به باارزش‌ترین تیم حاضر در لیگ برتر امسال شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138409" target="_blank">📅 17:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138408" target="_blank">📅 17:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138407">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138407" target="_blank">📅 17:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470685323.mp4?token=M1MukYah_89ReI-xMCrDMRlTrGElJybT4ULRnH3CLLqXb629sajH0QUZTTKRlBfySaJVORdEIdfqK_ohVnjd_GJvSfMmovf3IK85ZlfbXsWJDatx8GjRPCL2zMqfwUpCCMjKkuTpximPy5hDzOi9UNvMTVSDAmk1wUI8Oj9im-lG9zU0OrncK-OFb5Do9c1DxJXqbDy6sAB4FsClH8OBqW3SwjmlarOQfY6jOYl924wIJoVyLhKi_nlnutG-h4g3LEJbT78wV0tuk7mLtoiEkVx3hxbh2iqCANSyp0w1Zvc0eom_FgomMFijhZmsXw-Vcg4lQ21dHltnW5f8oEJFNV8Ene24De1NvR1bo5Qpmbo5xmIyk-r0Ac2drGFcgR7WaWOvMo5wct2XGNOPVR41PcuOxOTq7-sy2CfrHMganjhFtW48PpUPHhVBpitwTSzgJPoiYJDxobXKh6XAuSxsTaE24yHbhysXsoXGJk_PtmGJ-pBH4Zh8HuDDmxHniig4YS6cl0hM5yIBUCjtsYB8bhLBgg6frQlPCxipYNV4bXfLYY1aaGpnSd6JbFQ-n9MasIBFFiLHKf2NMPre-1Y6OTyxY7wK4xYAYD6W4wd5hBefWjYUTwK9Z-MJS1Rqxxe1hE0-y9ILAjeRRBG4uY_THin-4CvJq2Iyw8m32_mgE38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470685323.mp4?token=M1MukYah_89ReI-xMCrDMRlTrGElJybT4ULRnH3CLLqXb629sajH0QUZTTKRlBfySaJVORdEIdfqK_ohVnjd_GJvSfMmovf3IK85ZlfbXsWJDatx8GjRPCL2zMqfwUpCCMjKkuTpximPy5hDzOi9UNvMTVSDAmk1wUI8Oj9im-lG9zU0OrncK-OFb5Do9c1DxJXqbDy6sAB4FsClH8OBqW3SwjmlarOQfY6jOYl924wIJoVyLhKi_nlnutG-h4g3LEJbT78wV0tuk7mLtoiEkVx3hxbh2iqCANSyp0w1Zvc0eom_FgomMFijhZmsXw-Vcg4lQ21dHltnW5f8oEJFNV8Ene24De1NvR1bo5Qpmbo5xmIyk-r0Ac2drGFcgR7WaWOvMo5wct2XGNOPVR41PcuOxOTq7-sy2CfrHMganjhFtW48PpUPHhVBpitwTSzgJPoiYJDxobXKh6XAuSxsTaE24yHbhysXsoXGJk_PtmGJ-pBH4Zh8HuDDmxHniig4YS6cl0hM5yIBUCjtsYB8bhLBgg6frQlPCxipYNV4bXfLYY1aaGpnSd6JbFQ-n9MasIBFFiLHKf2NMPre-1Y6OTyxY7wK4xYAYD6W4wd5hBefWjYUTwK9Z-MJS1Rqxxe1hE0-y9ILAjeRRBG4uY_THin-4CvJq2Iyw8m32_mgE38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138406" target="_blank">📅 16:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎤
🔴
گفتگوی خبرنگاران با دانیال ایری، خرید جدید پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138405" target="_blank">📅 16:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCWc8DB-xAd0i4ucKV0RX4dlRWISwcc9JDvbaAGKRnKh5xsMtva39RRMEBCL3WCLsAtV_9CEXTBIBlTG5cJUOpOWVB1CIJ8rophyxk9opC3zOIUHu8jeKPIxXxaBVYtMxozcfQJkZLrj49qDMoD-Sr54NOYVGpVZio51N59hlFethOufEIOFi_sLdS-vDpsrhdKU8Ho4UI__D4AtmgHZNFpi8OTge9U_CjTQQXofLjbq7Mbdh6NE12FJ7KRZSYtVzkAtQ1Q-zxpR5Vq8F1Zso2IBHU9OiiuI-JzXykM4WAjtEHac5t1MYSn0XWPXwpOf4HltwC4Zf7h9ptL2ECbJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
دانیال ایری، مدافع ملی‌پوش و جوان فوتبال ایران با امضای قراردادی ۴+۱ ساله رسماً به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138404" target="_blank">📅 16:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c01b72802f.mp4?token=S0Lj8IbkNFwOXyNqUG5BeVsQA_rjOLBPb-vt2QE5Kpsg6zGEKJm9cShBFd3LRmhCv1ExLPRxPUalc0zmvDvgHkOReIMHIhDdNB3g0WtsrTEu7J1h7kAKEsf8WXXlvF6XVnZf73Ph8CtuNYVmIbKvaTwwLx2u1GPqmI5xLzaD3_txkM19Sczjl8T5lGbiTJwasnxD0swfgEmtQF0MJV8sBVG8_G97uE0ekQ_xKYYvRAa2M2DXNcRHx4m_QpgaOwHUh3mvHZ6MPmVOk7wSMgXBvqlR4Z7l6UncSqBnvhakKGeeQb_H6OzSOwGf4Cqna7enncDWN5vk5n7ankIpaNBdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c01b72802f.mp4?token=S0Lj8IbkNFwOXyNqUG5BeVsQA_rjOLBPb-vt2QE5Kpsg6zGEKJm9cShBFd3LRmhCv1ExLPRxPUalc0zmvDvgHkOReIMHIhDdNB3g0WtsrTEu7J1h7kAKEsf8WXXlvF6XVnZf73Ph8CtuNYVmIbKvaTwwLx2u1GPqmI5xLzaD3_txkM19Sczjl8T5lGbiTJwasnxD0swfgEmtQF0MJV8sBVG8_G97uE0ekQ_xKYYvRAa2M2DXNcRHx4m_QpgaOwHUh3mvHZ6MPmVOk7wSMgXBvqlR4Z7l6UncSqBnvhakKGeeQb_H6OzSOwGf4Cqna7enncDWN5vk5n7ankIpaNBdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
ورود دانیال ایری، خرید جدید پرسپولیس به ساختمان باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138403" target="_blank">📅 16:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
تنها 30 ساعت به پایان ضرب الاجل 60 روزه ترامپ برای توافق با ایران باقی مونده و هنوز نه صحبتی از تمدید آتش بس هست نه مذاکره و توافق.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138402" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
برای اولین بار در هفت سال اخیر ترکیب پرسپولیس پیش از یک مسابقه رسمی لو نرفت  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138401" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
ورزش سه:
❌
مدیران پرسپولیس بخاطر ترس از هوادار از خرید امیر جعفری انصراف دادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138400" target="_blank">📅 14:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138399" target="_blank">📅 14:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فوتبالی: دانیال ایری امروز ظهر در ساختمان باشگاه پرسپولیس حاضر میشه و قرارداد پنج ساله خودشو با پرسپولیس امضا میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138398" target="_blank">📅 14:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqg7yJZwS_DD0Bnc-7VKthrEoYTpVB0JhIBofo3QDKaKZGh-YFCpFVwaakC-eiYAh6FwyYwPhv6dS6e0twaIDerkL8TRzOOtxIXePjLzqLo6qQZ3QE0iB6cBEBTBszayaoQLsrXZs0StOyp1V44J-gT3t6AfSAnclaPm-VukohSS8KzANNNa3L7sKY7vk-XxKh4uORjOBzyLeOdMtlnjxW82Odm9-MAMbZj5Qrf5DRh6sc_QHj7Fpc5QuGH8o9z6bBIxeZue3Nd7NgKeLpKFrAWMh6o5RU3Vz5JQ_u9TVembVpfyVXBOIzEUEblVC7FaNEQscAasAaqK_J84ZLju6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بعداز مهدی ترابی ، مهدی هاشم‌ نژاد بازیکن تراکتور هم بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138397" target="_blank">📅 12:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Van2yQXa7rBd0MLMbhSXGBsQ92OjOArmSVILv0WvUNAOzXQ2aIf37rZOso7gNnTvHWyaJQb6pvSqGhZXwGp6wdePsXO07O1VXVG8v1JP4nULMccnXjXCC-fVaTDP860Pl2aANtd_GmGTMBKN1KQFQ7jW0MYQeccANDgPXbcARwhvx2xTJaMzVfMbRuNfMeiwI9RFBrpCgtBqFLiv_9i2kWA-s6Sjo52A4iAr6urf-QGob1yaKsBL3Tp1lyXfjvOKVmR_YKTNbURSENivGHEJEmxE5YV3Sw_3sucP3OiIqqvVc-zH5kmoJSmCtM5hS6ZtElvq8llzahzp3pj_U-QMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
نبردهای جذاب در فوتبال امروز
🔥
⚡️
چند دیدار مهم در برنامه امروز؛ از تقابل مدعیانی مثل الهلال و بنفیکا تا بازی‌های نزدیک سری‌آ و لالیگا. کفه شانس روی کاغذ به سود الهلال، بنفیکا و ساسولو سنگین‌تر است، اما چند بازی دیگر می‌توانند کاملاً رقابتی و غیرقابل‌پیش‌بینی باشند. با توجه به اختلاف ضرایب، بازی‌های مدعیان برای انتخاب‌های کم‌ریسک‌تر جذاب‌ترند؛ در مقابل، دیدارهای کرمونزه با سامپدوریا و دپورتیوو با الچه پتانسیل غافلگیری بیشتری دارند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امروز همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138396" target="_blank">📅 12:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138395">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👀
هد اسکاتینگ پرسپولیس دستیار بختیار زاده رو تعیین کرد!
🚫
فرزاد حبیب الهی هد اسکاتینگ باشگاه پرسپولیس پس از فرو کردن دنیل گرا به اسپانیا بازگشته بود و سمت پرسپولیسی ها آفتابی نمیشد حال با کمک پژمان راهبر پانادیچ رو به تراکتور برد و حالا هم ماریو توکیچ را به استقلال/ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138395" target="_blank">📅 11:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138394">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✖️
مهدی تارتار:
😀
ایگور سرگیف مصدوم است و هنوز به شرایط آرمانی نرسیده است وگرنه او جزو مهاجمان اول ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138394" target="_blank">📅 11:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138393">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blYcRBb6ZOow1oDGFiFQQB8At23y3pnmeM___wN80QFzqHG129m2Y0ciw7H9f1mhOm2fTL-CLyweaEIhtouiPSmYUscVxgltkRf9YDGYezqycHdwaJOGA2YZ6Rtov4yJyQmJ_zfDcY1CSmixgEtvQFO29xsJELlBwY2hJx9upaoQAfX10h6TLgwtwq3aWlxxZfSr6VmHzeURGKRKDEnz71yzNZ2Mnn9PJgFOClSyAtL-K-vtf6oMhsrArQrKBBAtqy44kfCqGN8dQLM3XceFkUZ0z0T9wmbzuqu7VA6s1qV8AcylGNHPu16zIHV6fdTflB_09PiANWHTnRsuTGETzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوتبالی: دانیال ایری امروز ظهر در ساختمان باشگاه پرسپولیس حاضر میشه و قرارداد پنج ساله خودشو با پرسپولیس امضا میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138393" target="_blank">📅 10:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
🔴
🔴
ادعای فنونی‌زاده: قرارداد خلیلی با پرسپولیس 20 میلیارد تومان است!
💬
برای رفتن پیشکسوتان به باشگاه هیچ هماهنگی نباید بشود/ دوربین دارند و ما را می‌بینند/ من، بهروز سلطانی، مجتبی محرمی و چند نفر دیگر رفتیم و گفتیم ما در زمان رضا درویش استعدادیاب باشگاه بودیم و شاید خلیلی برای همین می‌گوید که ما سهم می‌خواهیم/ حقوق ناچیزی می‌گرفتیم و در آن زمان 30 میلیون تومان حقوق می‌گرفتیم که مالیات از آن کم می‌شد و مجموعا نفری 27 میلیون تومان به ما حقوق می‌دادند/ محسن خلیلی 20 میلیارد تومان با پرسپولیس قرارداد دارد و 6 پست را هم تصاحب کرده است/ لگد زدن به در اتاق پیمان حدادی صحت ندارد/ پرسپولیس خانه دوم ما است/ در را آرام زدیم/ بلانسبت ما مگر حیوان هستیم که به در لگد بزنیم؟/ بهروز سلطانی دستانش مانند نان بربری است و دستان بزرگی دارد/ سلطانی از خلیلی پرسید چرا در را باز نمی‌کنید؟ خلیلی گفت دیر متوجه شدیم/ خلیلی با سلطانی بد صحبت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138392" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7e369898.mp4?token=GXNZgHWmxWiZp7pJmiKP5QUf8zqQyziA3fTe4pfygFfo6wBkJ6BBwP4ZNIONmXfyRJkjIGMElrMYZEKA-y2b20xdEOsffYjOXrJf5UvVcxZ2K8x4CkVC9KR55lWUyL0v5C18TqUlc25NxnXQ9pY8edpdR1UZpJzwRBy-lXWr7HcByQugrgOsfzs0S5lA385zmQCuXF7mw-pfoh82HsfptSVsjklt0NEMHsYFf6p_QS3VNjXEQC960NoE9UW76LD_zcsUGL9HaFLpwr6McGWUZq7RxS4OevwEqHJPa5aSi3Ge_FjJnHned_S491S9GpVQvnlyOrlC6BDQGd7YynRlPbf9au-bIEzDC_ydHHIaN-v7h265GSrUoI-htoDeGiTo4NcV-9lP2ezndJ4BgTRrjk0Nbtre2ffyWlwLgIjEGyGNy6orK3pHaLRT79yszAFAklPnEwT-8zb0JxESMrwTWj09UAt3mNH3_GNaVkqASXb4AxwzHbpfxRMbePH4AKEOfZQahDQqi4AJkNLIHatMAjsC_jkZNnx1u6PSqCPi2ioYhY1B1jOqI7XfvBVR36OZMQDq5O4k2QZ3Fyh5HmzQoSKulY6-pI7Ujxy5VWzrpHfTYGbQYeFubHtZdXYpwt9Ua5-t5VF36dAWm6t5TE6S3hIH4f8sric0VZP-A8cM4-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7e369898.mp4?token=GXNZgHWmxWiZp7pJmiKP5QUf8zqQyziA3fTe4pfygFfo6wBkJ6BBwP4ZNIONmXfyRJkjIGMElrMYZEKA-y2b20xdEOsffYjOXrJf5UvVcxZ2K8x4CkVC9KR55lWUyL0v5C18TqUlc25NxnXQ9pY8edpdR1UZpJzwRBy-lXWr7HcByQugrgOsfzs0S5lA385zmQCuXF7mw-pfoh82HsfptSVsjklt0NEMHsYFf6p_QS3VNjXEQC960NoE9UW76LD_zcsUGL9HaFLpwr6McGWUZq7RxS4OevwEqHJPa5aSi3Ge_FjJnHned_S491S9GpVQvnlyOrlC6BDQGd7YynRlPbf9au-bIEzDC_ydHHIaN-v7h265GSrUoI-htoDeGiTo4NcV-9lP2ezndJ4BgTRrjk0Nbtre2ffyWlwLgIjEGyGNy6orK3pHaLRT79yszAFAklPnEwT-8zb0JxESMrwTWj09UAt3mNH3_GNaVkqASXb4AxwzHbpfxRMbePH4AKEOfZQahDQqi4AJkNLIHatMAjsC_jkZNnx1u6PSqCPi2ioYhY1B1jOqI7XfvBVR36OZMQDq5O4k2QZ3Fyh5HmzQoSKulY6-pI7Ujxy5VWzrpHfTYGbQYeFubHtZdXYpwt9Ua5-t5VF36dAWm6t5TE6S3hIH4f8sric0VZP-A8cM4-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: محسن خلیلی در حدی نیست که در مورد پیشکسوت‌های پرسپولیس صحبت کند
💬
به جان نوه‌ام و سه فرزندی که دارم ماجرای لگد زدن به در اتاق پیمان حدادی درست نیست/ محسن خلیلی در حدی نیست که بخواهد در مورد پیشکسوتان پرسپولیس صحبت کند/ محسن خلیلی سایپایی است و نه پرسپولیسی/ محسن خلیلی را حتی در کارخانه سایپا هم راه نمی‌دهند/ محسن خلیلی آکادمی پرسپولیس را در اختیار داشت اما حسن خان‌محمدی را اخراج کرد با اینکه خان‌محمدی قهرمان شده بود/ خان‌محمدی برخی مسایل را به رضا درویش منتقل کرده بود/ خلیلی بگوید چرا درویش او را اخراج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138391" target="_blank">📅 09:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: کنعانی‌زادگان هنوز هم شلوغ‌بازی‌های خودش را دارد
💬
در لیگ برتر بازی آسان وجود ندارد/ می‌خواهم به مردم آبادان هم تبریک بگویم زیرا صنعت‌نفت آبادان به لیگ برتر برگشته است/ حسین ابرقویی می‌تواند دفاع کنار هم باشد/ محمدحسین کنعانی‌زادگان واقعا خوب بازی کرد و تیم را هم به خوبی هدایت کرد اما همچنان یکم شلوغ‌بازی دارد/ کنعانی باید قدر بازوبند را بداند/ با حضور دانیال ایری، خط دفاع پرسپولیس خیلی مستحکم می‌شود/ شاید پرسپولیس در یک‌بازی 5 دفاعه بازی کند و حضور مدافعان متعدد به تیم کمک می‌کند/ مدعی‌های قهرمانی زیاد هستند و پرسپولیس یک‌امتیاز هم نباید از دست بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138390" target="_blank">📅 09:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328262c761.mp4?token=igTXhhEJa8V0cjcVkgxQ4vrLweZK5zEYP7Lb6cblRP5mH4xllMQTstrxLsMPdXRAeVubpDYQrTuYVANqNN6v2sVcGai05AlVn_KXP9Hhrs-KvfzZ8zWUlOb_-8sT7HfyglWYG3bYSnv1-xmRD-Sjy6uRxyoiaBsg-Awjt_W4cc371X4H9ubmQOWaCJCr-4SVb4oIn5jdLytcrz7JGOejfjyyS6jnuothHRy0iPgaqhv_cpKF4U0T3XCD7-mwqb21fhzRbgeHvzZ9iLJggLa2eqfIV-uuiWb2EGcpBVzzoW7vkuW_cCnFCx9cklGdcficm8oYifQkaq0KojdsjuY0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328262c761.mp4?token=igTXhhEJa8V0cjcVkgxQ4vrLweZK5zEYP7Lb6cblRP5mH4xllMQTstrxLsMPdXRAeVubpDYQrTuYVANqNN6v2sVcGai05AlVn_KXP9Hhrs-KvfzZ8zWUlOb_-8sT7HfyglWYG3bYSnv1-xmRD-Sjy6uRxyoiaBsg-Awjt_W4cc371X4H9ubmQOWaCJCr-4SVb4oIn5jdLytcrz7JGOejfjyyS6jnuothHRy0iPgaqhv_cpKF4U0T3XCD7-mwqb21fhzRbgeHvzZ9iLJggLa2eqfIV-uuiWb2EGcpBVzzoW7vkuW_cCnFCx9cklGdcficm8oYifQkaq0KojdsjuY0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: محمدمهدی زارع مثل جوانی‌های من است!
💬
پرسپولیس بازی نسبتا خوبی را انجام داد/ همه بازیکنان جوان عملکرد خوبی داشتند و به نظرم محمدمهدی زارع از همه بهتر بود/ زارع دقیقا مثل جوانی‌های من فوتبال بازی می‌کند/ او کم‌اشتباه است، زیر توپ نمی‌زند و ضربه سر هم خوب می‌زند/ این قول را به هواداران می‌دهم که محمدمهدی زارع 10 سال در تیم ملی و پرسپولیس می‌تواند بازی کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138389" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba104efaf.mp4?token=coQMvFE2YGoY5CY6Y3h3Rs2wAn3w-Un4AlWdc2v5i2Ic1zaXsW-3ovZDpH7G3AkLc1VYHq_xwe_rI8Tz91312HrfHX1TVj58kA0BYJUV3VFrD4fjerl49zEwV3cokt_sYhhiD1kaXqQo_7cCoUVvd6WmS8iYMJSW0mOAJYduqCnqg5jRXQeH31wLBPCh6wK1CUzfZikbcBEtcjS-0F4PyXOvlkl9VPH-xGwBcYUNJgmpc0OoKRBl6E0mAhExSYLqqr6S0S2Q_rTyGS8R6ae1dQs9F2vxTvK3EQ4FPfxquodASDlM4xLWGBivMaF6xYAXY1F1hlB4WU49P_f3xc4s0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba104efaf.mp4?token=coQMvFE2YGoY5CY6Y3h3Rs2wAn3w-Un4AlWdc2v5i2Ic1zaXsW-3ovZDpH7G3AkLc1VYHq_xwe_rI8Tz91312HrfHX1TVj58kA0BYJUV3VFrD4fjerl49zEwV3cokt_sYhhiD1kaXqQo_7cCoUVvd6WmS8iYMJSW0mOAJYduqCnqg5jRXQeH31wLBPCh6wK1CUzfZikbcBEtcjS-0F4PyXOvlkl9VPH-xGwBcYUNJgmpc0OoKRBl6E0mAhExSYLqqr6S0S2Q_rTyGS8R6ae1dQs9F2vxTvK3EQ4FPfxquodASDlM4xLWGBivMaF6xYAXY1F1hlB4WU49P_f3xc4s0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: پرسپولیس باید از گل‌های خود محافظت می‌کرد
💬
پرسپولیس باید از گل‌های خود محافظت می‌کرد/ فکر کنم مهدی تارتار قدیمی‌ترین سرمربی فعلی لیگ برتر است/ بازی تدافعی هم واقعا هنر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138388" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5fa4ac23.mp4?token=ejC_vWslgRe1wuJpFSpV2wWSgd68SDf5x28VLpCECjCpznM-CWH-z-HI4Hibmm4_x46kvSqCYMFJP68nkPGVFvq1e0YJdA-cD2LdbDNi10y_tXK-bgDf-0sTkTlvH5CrJmy1LcTaukTqwWDWUaYEA7hpbh77OYiUWG9ylOHvI0vgcAaq7PZaazDW5UINgtlPjJ58MX95tU5w8nuBQStUcEViXO-trJOIwSNncs9RWUcercLgyZJGndt16Hc4wJztpNhkmyL0ecsGxLxJMFmTPomWZZiR8yV5-vlmlLTmlSXqyckUCS2yfhadsvp5PNTNsIIIDiSDd--fEmfw1_X8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5fa4ac23.mp4?token=ejC_vWslgRe1wuJpFSpV2wWSgd68SDf5x28VLpCECjCpznM-CWH-z-HI4Hibmm4_x46kvSqCYMFJP68nkPGVFvq1e0YJdA-cD2LdbDNi10y_tXK-bgDf-0sTkTlvH5CrJmy1LcTaukTqwWDWUaYEA7hpbh77OYiUWG9ylOHvI0vgcAaq7PZaazDW5UINgtlPjJ58MX95tU5w8nuBQStUcEViXO-trJOIwSNncs9RWUcercLgyZJGndt16Hc4wJztpNhkmyL0ecsGxLxJMFmTPomWZZiR8yV5-vlmlLTmlSXqyckUCS2yfhadsvp5PNTNsIIIDiSDd--fEmfw1_X8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔴
🔴
فنونی‌زاده: پرسپولیسِ تارتار در دقایق ابتدایی شبیه به پرسپولیس دهه 60 بود!
💬
به جان نوه‌ام فکر کردم پرسپولیس در دقایق ابتدایی، پرسپولیس دهه 60 است و واقعا به مهدی تارتار تبریک می‌گویم/ چند نکته منفی هم وجود داشت/ پرسپولیس دو گل زد و دو گل هم نزد/ شمس‌آذر تیم بسیار خوبی است و همیشه پرسپولیس را اذیت کرده است/ پرسپولیس در نیمه دوم به دفاع رفت/ سه امتیاز را عشق است و همین کافی بود/ دلم می‌خواهد بازی هجومی باشد و اصلا 5 بر 4 به سود پرسپولیس تمام شود و هواداران لذت ببرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138387" target="_blank">📅 09:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQIg5mM5fpuzHaHpCIUYTIE9r0U2FyxBhdk2w7wc9weov-mzBMQ7DeYawgqAxu-34qM-gI4GB8BaLO0cI8csoX8sD4cC9HoDVR3vsOWxmQBjU5azYudEp0nxQ9lgZXmFUagHkVszUoRh7gQ7oKkGAYO5W3keeKHyejDPud9SzPlFRv-uGTonpgC0_7yJ2oIThMBLQeBkswjUfEciSzTgOmnh9unpkFGCBviDWkt_f9mNUaBcJTXZPxdJH8LSQ8d2i9v2290YyhuNI9HVsPgZKyrezKXkh2OyHt9GFU5gnjXR9VphhKOBn2egvnO5QDU7j5TeQob3DPzrKn2EOofrzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138386" target="_blank">📅 08:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZGTp4SD3PvZEORRXAcYBJcVNrCGI8whjEVpzqba49MmPzzZSPiuJg-XAhP-sX6Sri6aLtIG2XEGu1wuGLsLwbpmLBCyo6Qla02ESLAXqxIJY_dymollUr3Asgmj_FOPLMdyH_zcaSasmvc3rkHTTPRrdIKHpe44v8fyzvOxO0UHsL2WrwoYmqja2223cNIUlsosvsJ2dE6GE8LO8GGm_IpWvq-TLgB7yIBVMh3XS0iQUa_yuZRJWp1i-Zih4lDt6bh-5GAd6BW7GEPkGSeYDYeLxDF1EkxHg5i-Bd8l6IZxjow2A4lQrKCM-KvslCEbcKaRRXkeEO3YKveUgjmAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎰
هیجان واقعی همراه با ماشین
اسلات
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
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138385" target="_blank">📅 01:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138384">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💢
💢
💢
🚨
مدیرای باشگاه میگن که نقل و انتقالات با جذب محمد قربانی تموم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/138384" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
باشگاه تصمیم گرفت از رفتار اورونوف چشم‌پوشی کنه و حاشیه رو ادامه نده/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/138383" target="_blank">📅 00:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/138382" target="_blank">📅 00:51 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
