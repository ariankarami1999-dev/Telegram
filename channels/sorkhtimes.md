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
<img src="https://cdn4.telesco.pe/file/vNCYc-W48NkS_oqt_oN0-7rYV_yLHGSmwP7sYn0D5pdTUQQXmBffbnwMoHGtUxOKoeY-8nI9BwS5IXbgoEWsy6bSSEJXBgEw5hMfTCnetWbqzR5AA4I-P-W0kz5UHGDC348ykSvZTpbab45gXrDUZzP9_oNA8coLH-GogfRyW3fmcrV46ZqpxlBfm6OiyH9cfsCwXxVdEfugFDK5er207wFhMt1lNHR4VuAolSuKn243zJvcfkJdCVu10DjuhPUaORnplIWanpEKilMcUA31rrwlXUlRtDY0aP8pPHqqxtAgJmdeDLcsXE2mWHrHC0hDCFGYSRda3MWPlw5uyzrrvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود، فقط با یه کلیک!
📌
هنوز برای ورود، دنبال لینک و مسیرهای مختلف می‌گردی؟
📌
وقتشه راه ساده‌تر رو انتخاب کنی!
🔗
با مینی‌اپ رسمی اسپورت‌نود، همه‌چیز یکجا و آماده‌ست؛ ربات رو باز کن، وارد شو و مستقیم به امکانات اسپورت‌نود دسترسی داشته باش.
1⃣
-  بدون لینک‌های سرگردان
2⃣
-  بدون مراحل اضافه
3⃣
-  سریع، ساده و یکپارچه
🔗
مسیر ورودت رو کوتاه کن؛ اسپورت‌نود همینجاست:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
کانال رسمی اسپورت‌نود:
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SorkhTimes/139068" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
تارتار با حضور بازیکنا در تیم ملی امید خارج از فیفادی مخالفت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/139067" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚠️
یایا امپرور بعداز نتایج درخشانش تو عراق میخاد برگرده ایران…سپاهان هم یه نیم نگاهی بهش داره؛فورا باید اسپند دود کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/139066" target="_blank">📅 00:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/139065" target="_blank">📅 00:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✖️
✖️
بهمنی رییس سازمان لیگ: فکر نمی‌کنم بتوانیم به خاطر فشردگی بازی ها امسال جام حذفی برگزار کنیم
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/139064" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًیــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًد۪ؔاٍؓ℘ًً</strong></div>
<div class="tg-text">تا میتونی اورنوف تشویق کنید و سرگیف اینا ستاره تیمند ارزو هرتیمی ک این بازیکن داشته باشند و ایری هم تشویق کنید روحیه اش برگرد</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/139063" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🅼🅴🅷🅳🅸</strong></div>
<div class="tg-text">پاس هایی ک باکیچ میندازه رو هیچ بازیکنی نمیتونه تو پرسپولیس بندازه بعد کلا یارو رو نیمکته</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/139062" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9qZyj6XPiT93WTdfeqVm2UsPzFaXwndj_rFqzP_GEfO08zQlmwqfWwUUNblokNlxozwK308UtSMIK4WDgpYqZQzAB6RoglnlOEOiT8q7vOKyXJnAZYft_youPIZzyrAy-WZLhFloKBfWx45EjaAyNsLr72xKPQ2cYqtafEKnNBrm513Ch4GBL2PzQb1JJezhGfufdbPWwSm42TY9fMDxpKpenGq51foR9UnNreG1HxVSvfLkDnZ_5n_d2KUVoqZzC_aQhkRa_JGCkgNpsQosKh6hN78Pv-5ASCCRXeIaTT6nBdKUFNQdkqdgfb7wYQaGy3QQ0jiQfqT5wsNEJPK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس:
⌛
مدیریت پرسپولیس تصمیمی برای تغییر در کادر فنی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/139061" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=iReW0Pf-hE5SM5-Oa4F2h8JnGyRtr4-Q3Nt8eMrHijnrx84pUljAfxeKpJgTI7K-p3Ep98a8eV2AkVy7Xvu4uCPCOwyI_HLeLRaBQoU_VqrnatRkCBXVxkIXhq-IKPmQfufeQhW-X8ls2CZW5KXO8MpAqJu2LbH5T4C4fqOmfyZqPUI2NlOn-x4R8Y2chEyFY6fx2j2Wg3yocOXOU51i8VJI-WDDkdGMdilhWc2kXSGkpiCG57kSaTkdX9Vf1Bs5gsA2qMZHDYkYvLhlTuOrec_1jGx6ZOq_sEKvKCRAxFi0ng3GWlb-th1xsJ_6N8HooWyVuI72wQWAOiuDM8jYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=iReW0Pf-hE5SM5-Oa4F2h8JnGyRtr4-Q3Nt8eMrHijnrx84pUljAfxeKpJgTI7K-p3Ep98a8eV2AkVy7Xvu4uCPCOwyI_HLeLRaBQoU_VqrnatRkCBXVxkIXhq-IKPmQfufeQhW-X8ls2CZW5KXO8MpAqJu2LbH5T4C4fqOmfyZqPUI2NlOn-x4R8Y2chEyFY6fx2j2Wg3yocOXOU51i8VJI-WDDkdGMdilhWc2kXSGkpiCG57kSaTkdX9Vf1Bs5gsA2qMZHDYkYvLhlTuOrec_1jGx6ZOq_sEKvKCRAxFi0ng3GWlb-th1xsJ_6N8HooWyVuI72wQWAOiuDM8jYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/139060" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/139059" target="_blank">📅 00:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/139058" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/139057" target="_blank">📅 23:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
قدوسی: اورونوف تو بازی با ملوان هم روی نیمکته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139056" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139055" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔄
❌
اسماعیل کارتال با فنرباغچه در مجموع 3-2 تیم لیون رو تو فرانسه شکست داد و به لیگ قهرمانان اروپا صعود کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139054" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtPlype0bo5yblGprj4uCOKQzzQwvfTS1zzOZh_KTaHU6NHEXXaSHwWWC9fS3cKLrf41HxyhD1pwn1H4kSm4tJSmwzRHwXfmHqFc-9bYtJQ_S4LatQ3mkBBRkoqInINj2lkm0OMgMh7s8n0bDzJ77ww9PeF_mBMl6NuZtpKpQDXrjaxyU6UBfq0xL_5NRV00JTW7m0KYUBbMHl-x0nCBPVLY3xaxVbCsSkt6ZE2ciTxvIR59LmbNW-EZeoD316_UyyRsLdBp8ggqCWxoISvmleYxc74k46av7mcxGKYtfFm31VV7vQ8U8BU7PH7dhawK6apKg4i8WTkqFGEQJpaE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
آبی‌ها آماده‌ی شکار؛ لوتون سد راه چلسی!
نبردی که می‌تونه از همون سوت اول بازی غافلگیرکننده باشه.
[
چلسی
🔹
🆚
🔹
لوتون
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/139053" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/139052" target="_blank">📅 22:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139051" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSU-oOS4w0dP7YeHTi5AxcfDsRAvX-SN05To0tioXesWmFo_FpXpXa4EufGuZowE2GL5VdNd-fOY3lvNZggqTO8xnGA-YiHWSNI-HhANPtBPqDcigYLfR94bx54XsQs1w5Xi8hGWAme0FOqDHz_SWnvc27kqWL3hFoyuexHd-DbPWvds9qTIpSo5gLOOOr13buIWau_TrV-ppVH3mIbrFM0kPIYw_nRNxyoKxvjlTnXoymRKVv-rmuiMzPqfx48WW-hfSIGS-fi4FKKebtEerwTIuO2aAKfGTEF-kgkFH6EoJcR9osUuIHkvd_sWbg6YMeLkSwlr7Ucltiw23lkgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/139050" target="_blank">📅 22:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: فراز امامعلی مدنظر ما نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139049" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
فراز امامعلی: پرسپولیس یکی از تیم‌هایی است که با من مذاکره کرد. اتفاقا به توافق نهایی هم رسیدیم و منتظرم ببینم جلسه عقد قرارداد برگزار خواهد شد یا نه
❌
❌
راجب پست‌هایی که توانایی بازی داره گفته: هم دفاع چپ بازی میکنم، هم وینگر چپ و هم مهاجم نوک
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/139048" target="_blank">📅 21:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9rsBCL2_rZXdRhSTBm6Z48os9d3fiKSOu3V-7p0CdNH2qnYlKyswrhPiTwDYbr8IRSfnIeQkDTipQ1vDJhUhosZB8ZJTyVL8a2uLtr5TIZTQ6en2jDqS-ieZSUl_1mPXfdv5QZjXD0DVE-lhL5-2yilN4_C1v6vxBP_7SC1wgHNUopFEx_19s08OBlq1OHdyZM7HwOIc4MXA8yctvllC006dk5nUEqwdZdwoiznGdFvpC1CuL9RURG--8CXYqn-7UuV8XgI5XaQLC_9evcy5gmIrBdwaIJ97SZyxMsTw0UjO2t4CzEqoKvgTinW5KzPLV607y0g_KwnfWxT51-I-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسکواد پرسپولیس با ۲۶ بازیکن برای فصل پیش رو بسته شد
🟪
۳ گلر
🟪
۵ مدافع وسط
🟪
۲ دفاع راست
🟪
۲ دفاع چپ
🟪
۵ هافبک وسط
🟪
۳ وینگر چپ
🟪
۳ وینگر راست
🟪
۳ مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139047" target="_blank">📅 20:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139046" target="_blank">📅 18:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139045" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139044" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
عادل فردوسی‌پور: فدراسیون لحظات آخر تصمیم گرفت سردار آزمون رو برگردونه و به جام‌جهانی ببرنش ولی یادشون افتاد اسمش تو لیست اولیه و ۵۵ نفره نبوده برا همین نمیتونن ببرنش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139043" target="_blank">📅 17:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139042" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139041" target="_blank">📅 15:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
آقا کریم باقری به عنوان بزرگتر تیم این روزها خیلی حواسش به دانیال ایری هست و کلی با این بازیکن صحبت کرده تا روحیه اش رو برگردونه و داره کمکش میکنه تا اون اشتباه مقابل تراکتور رو فراموش کنه و بجنگه برای جبران اون اتفاق
🎙
امثال آقا کریم برای پرسپولیس نعمت…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139040" target="_blank">📅 15:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
مصدومیت اوستن اورونوف جدی نیست و جای نگرانی وجود نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139039" target="_blank">📅 15:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iESG_YkVSTgKLi3N6YXaq7_GeWAzseAGLBsmG6_jEgdtjs77G822TwKpqeD_6pKw3RcxHbNliW8pQExBzR1hGLWnW_bYXQGpCH8hsTb0TmskLffUBzoObQxrzD7qSEcJqkdGhUN4pfNUaUPhRB0WY-MWSzXKoyYHX5ig-ypeS7FGzG1siNjfAX7nU1Ykq7kqQ5p7MkW_MIYC81YihkUU5_tLU4o4OB7YPzkj1uRDb_kYhmffU0lZvhidBVu9BkfH8Oiht5lQhbqwhN3jCI6Hi6lc-CiFIvgL5tI5VhjGR9tMrlsJ6bD1ts_HLJijvBU6mqjdJg7pc-MfLAy_mVr_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139038" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8eClcGfYAYgKW9Fn0ZGoIyOzoD7maHzIX_4rXgx1lxvM5D5iLdYY0nhKlCrxaGD43yhTyD8NlbP9RrSXeR7S73tDRbpgQpzAYKzsjJhrUHm8SPCU9MuZqO0PLhlaQwUOBqprjjVhBXLNEx4TjDjGZ3qvHSF_ZRPUYjiB4bHkp-El7M6BkzF8BxWNaU4YeBNrgss0zkJPb0Q2-hunHIU3rOHmrd3IXnqdXIfcKp1VPqqFUFhH7anv_DVEObuXtC6tAcWKBzu92PSxhb4nfSn_QjXqQl_L1BP2Odi-jJwJFv3lV-JpZJEvTUYG0zTlCk24h7xbnonn75VEATsoRzuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139037" target="_blank">📅 15:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139036" target="_blank">📅 14:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139035" target="_blank">📅 14:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVGEMJF7cLNv42oPMBVboGL-2JX77aNb3eOJUfcubciVhQuNSiexwXiGS48yqwrtpvJoqxxRv2aG7MdmvUZvKcm39ved27KM5iPzmyfSUp1p2KSyT4K-Cdt-0GGBD9Wgh8rLSJYywAW6zS7Lkt0uU7qpRxhYAPKwIIaWzhyJU1kHLcMFPVAU7-DiupSlI0viXW2hd0SWw_r1945gX0Yo4DRHJzzTCDGqd9vCiGGQsgoI6UsQ0L1tZ3soES-XDDO2tdOW-Ge5ys6YY6w9SItHRs0XIfMVlAmhYHGwZL1z96_X9bXgiuPcsc7o2ieUgehWvFpjTb0QyLYv--QzyPNVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب در نیو‌کمپ؛ زورآزمایی آبی‌واناری‌ها با شیرهای باسک، بارسا به‌دنبال ادامه شروع قدرتمند، بیلبائو به‌دنبال شگفتی بزرگ مقابل کاتالان‌‌ها
[
بارسلونا
🔵
🆚
🔴
اتلتیک‌بیلبائو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139034" target="_blank">📅 14:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPzWjSMpltjlnKd0xbOkcjBQ9e5uGnTPTLAH-dJJmhvD-Zgkn6lHFxPB7wabBiFY0bXRtzNpLwI-RkSSTO2SCbQ0WmufLYZm2e0LSLNJgCW_-Mtg_sRH79GyAuKLpsMVYfTCFVRAzpdVYALgfxKrPZPnZEklwVsNiQ3FAvnO12jmkt-PM3NkVUGGfkNCYPQmv6gs1YFXexty4t_jFIxr5gErNLrReZZnY9OTd7D-Hly3SlFFt_Gj7cE2Qa6bT3Y_jguc8c8Hj2v52Tpha0d-bTDZdU6Ho0NEUVsx0r3NjfRfj0QGfH9U2f-EHUypKaybzfIXHqEANu5L4QWAm6fcnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه پرسپولیس درآمد خود در مردادماه را ۴۶ میلیارد و ۴۰۰ میلیون تومان اعلام کرد که با احتساب این رقم، مجموع درآمدهای این باشگاه تا پایان مردادماه به ۸۴۱ میلیارد تومان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139033" target="_blank">📅 13:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
بلیت فروشی بازی پرسپولیس و ملوان شروع شد
http://footballeticket.ir
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139032" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139031">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
❗️
با اعلام ترانسفر مارکت؛ سروش رفیعی ، سرژ اوریه و ابوالفضل بابایی از پرسپولیس جدا شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139031" target="_blank">📅 11:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139030">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
فوری؛ فوتبالی: علیرضا بیرانوند هیچ راهی برای دور زدن سربازیش نداره و اگه تا آخر امشب با تراکتور فسخ نکنه نمیتونه در یک تیم لیگ برتری « ملوان، فجر» بازی کنه و باید بره لیگ یک و در نیروی زمینی بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139030" target="_blank">📅 11:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139029">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
یعقوب براجعه به صورت قرضی و با بند خرید ۵۰۰ هزار دلاری به نساجی پیوست
❌
امیرحسین طاهری به صورت قرضی به شمس اذر قزوین پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139029" target="_blank">📅 09:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139028">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
❌
❌
متاسفانه ترکیب اولیه تیم مشکل داشت چون عمری مصدومیت داشت و نتونستیم از اول بزاریم تو زمین و تیکدری تاحالا دفاع چپ بازی نکرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139028" target="_blank">📅 09:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
صبحی که هفته دیگه این موقع داریم درباره برد و باخت دربی حرف می‌زنیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139027" target="_blank">📅 09:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139026" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8dpIphmrl4lvNpx0HmDLo-gvABA9Gh7WD88z-5MF3Z7Ymy92CS8Yxg9Kb9_jm7S_hTwrkeEbJhHxp89q_w77_EqE9FkSskkDbWzfTtUDnaDXKqpv_np0c986Em3Mp3QDN7VvT5Jqs8uKUwi5vY1juwDKHcxtkBkMz5aO9BicVZ4hGqnAARPSO8ks8gvIQZLa2TU0_YX3rNJUqtfQqcfLZH0LxAF9tQvy8YJZxGAO_59V3IQ-IdtFo8czB4nS60gH4wosejtK3v5s9L_ZC_5Quc-CeVNmUCkzu2DdA1-djInTboYL5RhMgSrb8WGGj8lQgUiz-XwLig1aeUx425PUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
عدنان کوستوویچ
فصل گذشته دستیار تارتار بود و این رزومه ایشونه، آقا مهدی چون توهم توطئه داشتن ایشونو گذاشته بودن کنز بچینه سر تمرین و اجازه نمیدادن تو مسائل فنی ورود بکنه
و به همین خاطر عدنان نیم فصل رفت ذوب آهن؛فقط خاستم بگم انشالله که خیره
👀
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/139025" target="_blank">📅 00:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuR3Ioqo-zkyH65Sx5epBfBmtJbFS1nfZh2K_b6Qiov4nrXPVM7WuvUT6DQFAV-SsWwjPY4VVmkvNhh3CoBmhWu8MLPjsHvMuV2v-vq5mNknBzlMFJRPDbnfkjoRGMAoRcDsaTDZLGkQ309mCZIVyhW8En6_DEoH_wM6-5wUTa6_QkIjPJzmyyj4Yry_xOORWQCEuhRP7YOgY6onABRyfFrHYCr49kBNcbGuJT5GI6OVms92FizDejt9X-nJa7VELRAUE1aE6WCXHL6kyKFL7RmJbjiiHOMTRmiPi5AcYZGgZGrUq5lC_69ZJtR52i6bF3Iu3Kpk9OQMkGFONwTOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139023" target="_blank">📅 00:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🇹🇷
در هفته اول لیگ ترکیه، فنرباغچه با هدایت اسماعیل کارتال در برابر گنچلربیرلیغی با نتیجه 2 بر 1 شکست خورد !
❌
فقط باید اسی کارتال باشی با اون همه ستاره هفته اول ببازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139022" target="_blank">📅 00:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
پرسپولیس امکان جذب بازیکن خارجی ندارد چون ۵ خارجی دارد و  طبق قوانین جدید به شرطی می توانست خارجی جذب کند که با دو خارجی فسخ کتد.گرا و بیفوما هم مازاد بودند که با هیچ کدام شان توافق نشد و هر دو ماندنی شدند
❌
❌
در پست دفاع چپ که دغدغه اصلی تارتار است و هافبک…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139021" target="_blank">📅 00:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
پنجره نقل‌وانتقالات فوتبال ایران بسته شد
❌
پنجره نقل‌وانتقالات فوتبال ایران در ساعت 23:59 چهارشنبه 4 شهریور بسته شد و باشگاه‌ها دیگر امکان ثبت قرارداد با بازیکنان تحت قرارداد را در این پنجره نخواهند داشت.از این پس، تنها بازیکنان آزاد در صورت داشتن شرایط…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139020" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBsQI9qtgxnNfM5Uj5XnahumDszOp0cFfnbqnLjT_sQV_wEl8bEct7vgeT_whvqAgj0epDTbpfvkVYcX7Muf0r4Q4E7X0E5hLs4rtwSX6PC8uYDkyMAGcXI0f2IY-pTz-5MAbYhGzG6vQXhEsp7pQbvAxa_R66sKcfKuYjB4ydXfMYO4J0P2wZCvYk0FKJCve9ev-JOi3QlpA35fiFQVFgu-X3g8nfcLP5ieUOrFujbznJYVqmnLnBabLSqDOAQyWH9fgvFtKZll3bscV7C7MHqg7mVKxgVGtnt5xrloCviwZWHpVV2mVg5ipLF_o2xtv4jL1XxF14ySs-vpr_ujmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🤩
استوری حدادی، مدیرعامل پرسپولیس برای حمایت از ایری و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139019" target="_blank">📅 00:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2Zljz5AZmjSGWxBpuwIh-SzxcoQ-3yg4IoHXpwM8uLBL-nvqX2-XzPxOPrJPCVT5QdiGGR9c95cY0SCRuKTByX2kQV1Db0ipelZvN_vod6TmnCEb-PYuXk1_akk-kfV5qE_PoVb7t2aRDyayAtwfTOg3t3otvREEnS1eCawVEhT7tVkVEfFet2QFn8oO1uFRzEZFdgnQnXGulf79sej2ozQxzrVAk74NvYpHsMHGTus9iOqNvO2-hc-C6Pjm7Dqo1kc7ih7u5N8SRs_31YT_dhdstEV0iUW7eUEk1GzoXjeF4a73XqIUZkGKPIWfKs6k6gMSItsTrdOU_2k2TSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پنجره نقل‌وانتقالات فوتبال ایران بسته شد
❌
پنجره نقل‌وانتقالات فوتبال ایران در ساعت 23:59 چهارشنبه 4 شهریور بسته شد و باشگاه‌ها دیگر امکان ثبت قرارداد با بازیکنان تحت قرارداد را در این پنجره نخواهند داشت.از این پس، تنها بازیکنان آزاد در صورت داشتن شرایط قانونی می‌توانند با تیم‌ها قرارداد امضا کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139018" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
پرسپولیس از جذب ابوذر صفرزاده انصراف داد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139017" target="_blank">📅 23:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
محمد نوری چه فازی گرفته و صحبت های جالبی می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139016" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139013">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/139013" target="_blank">📅 23:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139012">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
🔴
تصاویری از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
❌
ویدیو عمق فاجعه رو به خوبی نشون میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/139012" target="_blank">📅 21:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139011">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
گرشاسبی، مدیرعامل فولاد: رامین رضاییان به فولاد علاقمند بود و در اتفاقی جالب به فولاد برگشت. قرارداد او هم زیر ۱۰۰ میلیارد تومان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/139011" target="_blank">📅 21:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139010">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139010" target="_blank">📅 21:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139009">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/bd751b7046.mp4?token=fguUyZ8HnQLZT8p7yyKRTBylodJIJf0YRzkVfdAXNIb8NLVl1TKjc2Ldn8o-x8WEPMzbznuOokX9SqtbnB-EJFEF_D1-yXd_PzDCDhCDUqujRfCfGvXeQRXqI8EN_XlP97614oD1Ih7nOyB1q1saltH370OnuzfMXpRKN7cUQEi4TJUw7mtFH8HHFjKlO66_ZkNuTHng-ofOahC2OGy1FwIdpAqCTLgUTUn8B07RlK7QqJNa05O-KijEW4l93XEYpNA2a1_cErA1fZEqaNeK3KaU9poB-waIqamV02dvBCSmIEoWYzCmqz9N4eggxTwa05dt4UIFd6FQGRboTCsf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/bd751b7046.mp4?token=fguUyZ8HnQLZT8p7yyKRTBylodJIJf0YRzkVfdAXNIb8NLVl1TKjc2Ldn8o-x8WEPMzbznuOokX9SqtbnB-EJFEF_D1-yXd_PzDCDhCDUqujRfCfGvXeQRXqI8EN_XlP97614oD1Ih7nOyB1q1saltH370OnuzfMXpRKN7cUQEi4TJUw7mtFH8HHFjKlO66_ZkNuTHng-ofOahC2OGy1FwIdpAqCTLgUTUn8B07RlK7QqJNa05O-KijEW4l93XEYpNA2a1_cErA1fZEqaNeK3KaU9poB-waIqamV02dvBCSmIEoWYzCmqz9N4eggxTwa05dt4UIFd6FQGRboTCsf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇾
شهاب زاهدی تو بازی امشب جوهور دارالتعظیم تو لیگ مالزی برای تیم‌ش ۴ گل زد و در آخر ۹-۰ برنده شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/139009" target="_blank">📅 21:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=Cx4XisYf-Ny504lNBifR0_jdkwcvgR0AMxnEUItCJjZkCdVF_-jiAN7meaBNs511YAq_L2ps3R5DTeUxpj1rXV-sTWSd4J_a-oTOi68YScC1P6eB0cK1LS3-ybRGY9AxMea-n_wXqWzfOIQr_LdgGcMP-TH9lc7Fxzn6HZRK2kn5uaBBQvRSW5BS2r51KQvIh5QlY3LCwouLpbYTyDFufzh4d542Nr51eG4PBOntg7YklZs5Ov8zghYi87u6457oTMUkTRQIM3N9HGmiMFac5WOIOXM5TA0lL_ZOfluoj0O80TEf8gvplDQ7HPLcsUCxSgfanY5iKGNxQy5S951btQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=Cx4XisYf-Ny504lNBifR0_jdkwcvgR0AMxnEUItCJjZkCdVF_-jiAN7meaBNs511YAq_L2ps3R5DTeUxpj1rXV-sTWSd4J_a-oTOi68YScC1P6eB0cK1LS3-ybRGY9AxMea-n_wXqWzfOIQr_LdgGcMP-TH9lc7Fxzn6HZRK2kn5uaBBQvRSW5BS2r51KQvIh5QlY3LCwouLpbYTyDFufzh4d542Nr51eG4PBOntg7YklZs5Ov8zghYi87u6457oTMUkTRQIM3N9HGmiMFac5WOIOXM5TA0lL_ZOfluoj0O80TEf8gvplDQ7HPLcsUCxSgfanY5iKGNxQy5S951btQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139008" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
اسپورت عراق: یحیی گل محمدی به شدت به جذب محمدرضا سلیمانی که 18 ماه بود بازی نکرده بود علاقه‌مند و تاکید داشت بود و الان این بازیکن به علت عملکرد به شدت ضعیف‌ای چه از خودش نشون داده سران دهوک عراق میخوان در لیست خروج بزارنش ولی باید تمام قراردادش رو پرداخت…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139007" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=j_0AeSmeP-mU6_6s20QyAvNJ_bH_taqBAcG0WA-eNfr2H9aEL8i1FJ_u25mszWKGY52qTpyBNpfB6wFVqM1wARHqm9_Il88D6xMvLcOZ49smgr7VzRc_RVwswbDPhFlBL950DAjUbHPL3-N6DO0XBYKJzNk_d5qNgLhMnT9Qh9oDhu8QoK4gdYavmvM0qMYIqoJ8BB64vS3mqabQmEs3zA-XVKlQmFnl1Q1lGWCykvL7S3OPDvw-sBxr2fTYJyVBZgcNgdkdnnvaZYIFjrINnRRc9qJXuYgx6WCM-KtJC-iVw1cQ2cO2N_0lS1NGMYxTFF-r0pIsgC_dfKO5866Q1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=j_0AeSmeP-mU6_6s20QyAvNJ_bH_taqBAcG0WA-eNfr2H9aEL8i1FJ_u25mszWKGY52qTpyBNpfB6wFVqM1wARHqm9_Il88D6xMvLcOZ49smgr7VzRc_RVwswbDPhFlBL950DAjUbHPL3-N6DO0XBYKJzNk_d5qNgLhMnT9Qh9oDhu8QoK4gdYavmvM0qMYIqoJ8BB64vS3mqabQmEs3zA-XVKlQmFnl1Q1lGWCykvL7S3OPDvw-sBxr2fTYJyVBZgcNgdkdnnvaZYIFjrINnRRc9qJXuYgx6WCM-KtJC-iVw1cQ2cO2N_0lS1NGMYxTFF-r0pIsgC_dfKO5866Q1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
شهردار تهران: قصد داریم 3 ورزشگاه 40 تا 100 هزار نفری در تهران احداث کنیم که شامل همۀ ورزش‌ها باشد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139006" target="_blank">📅 21:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139005">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139005" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139004">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139004" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139003">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود  ببین جیشده صدا چراغی هم در اومده چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139003" target="_blank">📅 20:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaeid</strong></div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود
ببین جیشده صدا چراغی هم در اومده
چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139000" target="_blank">📅 20:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/138999" target="_blank">📅 20:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب بروز مسائل حاشیه ای میشه، ایشون کلا توهم توطئه داره تو هر تیمی که بوده…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138998" target="_blank">📅 20:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
فووووووووووووری از آنا
🚨
مدیران باشگاه پرسپولیس از جذب ابوذر صفرزاده انصراف دادند و خبر مذاکرات مجدد با این بازیکن رو رد کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138997" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138996" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
فوری و مهم
🗣
🗣
سازمان نظام وظیفه اعلام کرد قانون معافیت بازیکنان تا نیم‌فصل لغو شده است. بر اساس این تصمیم، علیرضا بیرانوند تنها تا ساعت ۲۴ امشب فرصت دارد قرارداد خود را فسخ کند؛ در غیر این صورت، او باید برای گذراندن دوران خدمت سربازی به تیم نیروی زمینی…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138995" target="_blank">📅 20:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
تلاش بیرانوند برای تعویق سربازی تا بهمن
🔹
علیرضا بیرانوند در تلاش است با استناد به مهلت قانونی یک‌ساله پس از فارغ‌التحصیلی مقطع کارشناسی ارشد، خدمت سربازی خود را تا بهمن‌ماه ۱۴۰۵ به تعویق بیندازد تا بتواند تا زمان برگزاری جام ملت‌های آسیا ۲۰۲۷ در تیم تراکتور…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/138994" target="_blank">📅 20:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138993" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138992" target="_blank">📅 20:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCgEuuB8X-vuWOfSMxAHYulUcG3rH0S1xlZIeMsL1N6y6tdmnmEk85porBrlj5bkB5K3kxi8KoXTDGTPrWOTAWLKp0tCVZ1ORryWlPt2QruwXyqx16G7r54AqeKtsdgXAinqN6FmWXgA9O7SV0Cf4Vw0t0Dnj5whMDZmKoMZjfuBeocWe1Zzp-XLwSwxws0li3dEHPfUDcvbHH1nRUOfKPyVTaXjx8pgwrQ3_ZBVADa5MoIzdsH4bw_hf2gLGEZXr36i35tcWQDOi1-W5m3Bb5jh4df8xBmbEYRlei_GZXDDKEhJbhijptX4MOkFGivIEvVC0nsQX_WjjFWa9pU7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون و فنرباغچه؛ جدال برای یک‌قدم بزرگ
دوتیم، یک شب حساس و پر از هیجان
کدوم تیم امشب صعود خواهد کرد؟
[
لیون
⚽️
🆚
⚽️
فنرباغچه
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138991" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138990" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138989" target="_blank">📅 16:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
جلسه مدیرعامل و سرمربی پرسپولیس برگزار شد
✔️
✔️
جلسه پیمان حدادی، مدیرعامل باشگاه پرسپولیس، با مهدی تارتار، سرمربی تیم، برگزار شد و در جریان آن آخرین شرایط تیم و همچنین برنامه‌های پیش‌رو مورد بحث و بررسی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/138988" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
💢
💢
طبق پیگیری ها، جلسه مدیران باشگاه پرسپولیس و مدیران باشگاه خیبر از دقایقی پیش آغاز شده است و تا ساعات دیگر احتمالا قرارداد صفرزاده با پرسپولیس امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138987" target="_blank">📅 16:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138986" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138985" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138984" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138983" target="_blank">📅 16:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
کوپال ناظمی و موعود بنیادی فر دو گزینه اصلی برای قضاوت دربی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138982" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه امروز از بین این ۳ گزینه، یکی سرخ‌پوش میشه!
🔴
ابوذر صفرزاده
🔴
ابوالفضل رزاق‌پور
🔴
امیر جعفری
⏳
باید دید کدوم اسم در نهایت پرسپولیسی میشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138981" target="_blank">📅 15:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
پرسپولیس نا امید از جذب قربانی در تلاش است از بین رزاق‌پور، جعفری و صفرزاده یکی را جذب کند. فولاد پیشنهاد معاوضه رزاق‌پور با همایی‌فرد را مثل پیشنهاد معاوضه با بیفوما و ۸۰ میلیارد پول رد کرده. رحمتی مخالف جدایی جعفری است و خیبر خواهان معاوضه ابرقویی و…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138979" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F7Cy7WvVgwqzRBfeQ6p9dgtGutcuCLijA88-AF0eptekqEfX3Mj0mi1Ic0SaTOgZ0ahEaUW9SVUcPev6fBRd7CriHiz5TGou7GMvuiKw-mV9T1MUf6R8gmqKw2oyZCfnh2M_bS8YRHEQDhd77D6E3C7zm9isUdr7w-0jup6VJlPjaz1MkMx0x10w90UP5JnLDMFzNbpj1WceZs5vE-2ieGTIvhdNPI1520b6knQPcUuJ9wLVv3L_lQa6OuyUDsDP39L2c64dcEHlhbz3ZwZ3UDtJNAMjVeXYDlhcGY70miUrNCDIDX-ynurYxPM9ZvUFmZBY69TqRbn_DIeFiOGOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا برای امروز دیروز نیست برمیگرده به محرومیت عیسی ال کثیر در آسیا
✔️
✔️
پشت جوانان تیم باشید نذارید رسانه های وابسته به کیسه نابودشون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138978" target="_blank">📅 13:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚪️
هادی چوپان: مجتبی خامنه‌ای پرچمدار دفاع از ایرانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138977" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiDs_Iwb1P69djBwsPyT2Typwgd3yxUvVWwGefQ5FUQAxB-U3uMvoZTYv_jYMeVSBBlU6Xk2mB09LliX4J6h0WPSaiHVFZAJ8xdFrKb6ad3nq02-jXaBueqsSK_IRIGiVr2YaWJkkBSqttORvB2LM5rgvRtHCpPv21yBXhXHeMKj2elVZ80DvApj-9-avlwrpGqQAiyD-S3uGwKxEnxgHr3Z68ZWgBApLVhNDeBXE3TPnPH8VH1ZBABkmxcIyiqKzjVDxYJNj463Bx1hA-WoQBtcS9HCYIhvs-KfT8SUh1uPJB-7DBAJpNk1S4lZQchGtHsRnYzo5LmzyClzvguj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال در خانه؛ سه امتیاز برای کهکشانی‌ها یا یک غافلگیری بزرگ؟
امشب؛ بازی‌ای برای شکار بهترین انتخاب‌های پیش‌‌بینی!
[
رئال‌مادرید
⚽️
🆚
⚽️
رئال‌سوسیداد
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138976" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138975" target="_blank">📅 10:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/138974" target="_blank">📅 10:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138973" target="_blank">📅 09:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138972" target="_blank">📅 09:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
منابع مطلع میگن پرسپولیس علاوه بر رزاق‌پور، جعفری و صفرزاده، با چند گزینه دیگه هم وارد مذاکره شده.
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138971" target="_blank">📅 09:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🗣
🗣
🗣
باشگاه پرسپولیس در آستانه توافق نهایی و جذب امیر جعفری است اما بخاطر باخت روز گذشته و ترس از واکنش هواداران، برای رونمایی تردید دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138970" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
دلیل نیمکت‌نشینی اورونوف مقابل تراکتور؛ پرس نکردن!
✔️
تارتار از مشارکت کم اورونوف در پرس و کارهای دفاعی ناراضیه و معتقده مهاجما باید بعد از لو دادن توپ، برای پس گرفتنش بیشتر تلاش کنن.
⌛️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138969" target="_blank">📅 09:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR86IGGRQiAbfJivS39AvBbRGG4Rlf7jKGKRYRfJkY-KrbFcHlWVHrLcJ8Ex4H6QFOfIGVwVuw68-bjVdR0sHwSBV-KlQz300Z9HCYCrVTEX6wGSBhZnqH7q03ULM9SLmza77x63tU8v7ZSJ_bIggKAPwHqJ-Rdx3x6iBjU7_J_dOR-CKfVvtelsGFXEFOBGIBROgk5JC5h943MhhcrJ5P9kf3-jasfCvh7SkH0GOxqKp2uvElUu7_z9QihJp2RNXT5Eii_9m7e4MY0ySMcGy4KL9f0X9HMqUI47lUvEO6ftRk_ep6LsAmvrKPKX5O8p7Vr35awbMq9QkRIo6PmnYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138968" target="_blank">📅 09:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138967" target="_blank">📅 01:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
دلیل غیبت محمودی در لیست تیم ملی امید این بود که او در اردوی قبلی تیم در کایسری ترکیه شرکت نکرد و حالا عبدی برای حفظ نظم تیم این تصمیم رو گرفت/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138966" target="_blank">📅 00:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138965" target="_blank">📅 00:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی تیم پرسپولیس: اگر از بازی مقابل تراکتور درس نگیریم به معنی ضعف کادرفنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138964" target="_blank">📅 00:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138963" target="_blank">📅 00:14 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
