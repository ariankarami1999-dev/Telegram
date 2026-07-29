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
<img src="https://cdn4.telesco.pe/file/OB3V9RBtyPHvAqPbX6k92l7-IkSaFIn9ijdQ9NP9Fotewy81E7i4WmSj6J1HPqD91hWC2zXaYCKrFKgvgzxLfgyHry38f1oqbYLVEPaqpnkJDq24jyUej9vRSWXPQgjGAW1xLBuxfQBlFo8RIDfg6LAhwym9Lzq-sC2H7lEpcytNrbLx7g7u65CRhBgC6anfgiV2SqPGsx0t5mq0vDCgIXNfc3Twk78_Zpa1DPISIQtoY-GnMRPdD_M1WWspK21kIrwL8se_yC9d_nNdKMglmSYx4npicesNOateq9k-y8NubTsTHqDdpoF1ZVn6gSYrIHscWMJty6fxU8nXhrkuIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 20:16:35</div>
<hr>

<div class="tg-post" id="msg-137000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=AdOMMIRd0I8YRoABDThdnwl4MeZfqCGqF33O4rLwqcBD6FzPNP6k5dA-1OV0uLFm1kRD2hl1-h_0kF4JMQuYQsvCBKHT_379lfTVavxB4dRRdWVJLL99w8qqYiKjCENuLUbq_5K_NDxQi4WygHVVSL6ZjNjoGqX0H-qIqt1scKU1cUKmknzWPMYuL8cwG6v_3g85pkjGx-73RwCOKWIUNUoQL25T6pEi7dS0pgt52vlYPvM0k53ftBa98E0TqlK3gIHojy9downy7BSpL4-lGuvPzhtqf-eU9MNMdDd-Cjm5QvU2y7lRXz0ZH6W-eZvH8Mx0-gJ7-xEEBkQ_7whBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=AdOMMIRd0I8YRoABDThdnwl4MeZfqCGqF33O4rLwqcBD6FzPNP6k5dA-1OV0uLFm1kRD2hl1-h_0kF4JMQuYQsvCBKHT_379lfTVavxB4dRRdWVJLL99w8qqYiKjCENuLUbq_5K_NDxQi4WygHVVSL6ZjNjoGqX0H-qIqt1scKU1cUKmknzWPMYuL8cwG6v_3g85pkjGx-73RwCOKWIUNUoQL25T6pEi7dS0pgt52vlYPvM0k53ftBa98E0TqlK3gIHojy9downy7BSpL4-lGuvPzhtqf-eU9MNMdDd-Cjm5QvU2y7lRXz0ZH6W-eZvH8Mx0-gJ7-xEEBkQ_7whBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/SorkhTimes/137000" target="_blank">📅 20:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⬇
⬇
بازگشت جنگ اعصاب به فوتبال
🔴
فوری - جواد نکونام به لیگ برتر برگشت
🤝
جواد نکونام پس از ساعت‌های طولانی مذاکره با باشگاه پیکان، به توافق نهایی با خودروسازان رسید تا پس از یک وقفه، دوباره به لیگ برتر برگردد و هدایت این تیم را برعهده بگیرد.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/136999" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbOufIO2BmBu0qhVVk1ljmerM-gi-dP46FfOrwZbeF5ng-x_-TBf5UaUEIhiCu7UWZZGahbIxH22RqYi__b1YcHAJDi7MV9SqzrsIRQB4KkvlAPpnHCARfahV-gFcwBjnxKIZjEtS8weFAU5ELQ_LPUMhSadgPkLmo394IsYHgypwRHOqYx-AC3c-TvXN4tUgMmRWAUOInOV9sxc3pd5G1QtkucTLzfPiZwMKM-0B902pUY2Gz7pn1BtGgyJjY2H-sAHsLSA4fNMZfP9frjdn8Wa55oC-BifsVv1oLnVDV04xlVGZ6L_xnljKnJ-7sLWanFohyXOr6gyksiciiklwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
در عربستان پول پارو کرد!
🇸🇦
کریستیانو رونالدو از زمان پیوستن به تیم النصر، مبلغ شگفت‌انگیز 625 میلیون یورو به عنوان حقوق و پاداش کسب کرده است.
😇
فوق ستاره پرتغالی در کمتر از چهار سال، ثروتی بی‌سابقه به دست آورده و او را به فوتبالیستی تبدیل کرد که بیشترین میزان درآمد را از قراردادهای خود در تاریخ این ورزش داشته است.
🟡
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
🟡
پاداش برای ۱۲۹ گل: ۱۱ میلیون یورو
🟡
پاداش برای ۲۳ پاس گل: ۱ میلیون یورو
🟡
دو جایزه بهترین گلزن لیگ: ۸.۵ میلیون یورو
🟡
پاداش قهرمانی در لیگ: ۸.۵ میلیون یورو
⚡️
مجموع درآمد: تقریباً ۶۲۵ میلیون یورو
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/136998" target="_blank">📅 19:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY7UggLxaUoznlwiF9LAUXZZRmEz0sVquo__1B7kOhOQbMTcKsXiwtnBhfA60TDR7CqHuS9aU2kOKm4SACXYRp1o9hyX3VhamXKj3DD_BB-L60YPzgn8ap_NdUngh--guul1EnreqNAHHOW9uVLirIUeEPfKaJz87v-795tyaaNbcW1jny4kaJWjPkuyzPQHgysNbZ85gZxDv0EJEXwqF0-G0fd2Jgdcj84KbK6ei9dVKeBW1l3Xm3x3jhcQu4L0JWLPzgCAFAGpHWF7fEimGv6tGLksIInSabeNoMP2MuBJLwlhs1hPyhU1vs1pzPLsjYrpFLEBZlzMymhFjZ-Y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👤
ممد مهتی امشب به اردوی پرسپولیس اضافه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/136997" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌀
🌀
تارتار تو پست های دروازبان، دفاع راست ، دفاع چپ و دفاع وسط بازیکن میخواد/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/136996" target="_blank">📅 18:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
تارتار: حداقل به 4 خرید دیگر لازم داریم (دفاع چپ،دفاع میانی،گلر و مهاجم ) بازیکن می‌خوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/136995" target="_blank">📅 18:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات،…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/136994" target="_blank">📅 18:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/136993" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136992">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚡️
⚡️
فوری/ دونالد ترامپ: در پاسخ به حملاتی که سپاه پاسداران به اردن کرده، ما ایران را به شدت مورد حمله قرار خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136992" target="_blank">📅 16:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136991">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚡️
ترامپ: اگر توافق نشود، پل‌ها را ظرف دو ساعت و نیروگاه‌ها را در یک روز از بین می‌برم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136991" target="_blank">📅 15:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
گل های محمدمهدی محبی خرید و ستاره جدید پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136990" target="_blank">📅 15:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136988">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
🔴
🔴
باشگاه پرسپولیس با مبلغ ۵۰ میلیارد با وحید امیری تمدید کرده و حالا با توجه به جدایی و بدون اینکه بازی کنه، ۲۸ میلیارد میگیره و توافق می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/136988" target="_blank">📅 15:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136987" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/136986" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🔴
🔴
🔴
توجه به پیوستن محمدرضا اخباری، احتمال بازگشت امیر رفیعی قوت گرفته است. برخلاف اخبار منتشره، باشگاه پرسپولیس، با احمد گوهری و سایر دروازه بان هایی که نام آن ها مطرح است مذاکره ای نداشته
🔴
رفیعی به مدیران پرسپولیس اعلام کرد توافقی جدا شود و باشگاه به او…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136985" target="_blank">📅 15:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136984" target="_blank">📅 15:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136983">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136983" target="_blank">📅 14:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136982">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
امیر روستایی مهاجم سابق پرسپولیس به سترة بحرین پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136982" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136981">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136981" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136980">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFsUwDyLa28WZVXBV8B1PphIT-QyToBFtay6k5OWaBXGouvqOTM6U0hof9McLvZaSoubsj9x0pYf-Gx6PMemBEOcU2-7QbpMAbs1zmJJpFgtZUHMlxMU78KfqorJhiP77lCG3pMWCsL64OAytxsaXjZkeXR69l71kISyxj__Lxt9y31MLaVM5H7h86nHA9das9W9AQz0I887BdBkNlhpxs5_zyAovMTz8MVPMmxqkX_z0m8NEq22en-hoZvuVgrYV3pNEMBoKSRuBS7gz-cugmLqWxnRmWfaBUqy4S04yfoX4IFjCFmdrr2_vBI37WvoqlQytvDSnoIhQFcgcd08YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136980" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136979">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
علی بازگشا، سخنگوی باشگاه پرسپولیس: «اینکه پیشنهادی آمده بی‌اطلاعم، اما ما می‌خواهیم اورونوف و سرگیف را حفظ کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136979" target="_blank">📅 11:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136978">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔄
🔄
باشگاه نساجی: دانیال ایری و کسری طاهری رو دیگر به پرسپولیس نمیدیم. بانک شهر ما رو سرکار گذاشت. اگه با استقلال توافق کنیم اونارو به استقلال میفروشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136978" target="_blank">📅 11:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136977">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
✅
کسری طاهری رسما توسط نساجی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136977" target="_blank">📅 11:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136976">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💢
💢
قرعه نه سخت نه آسون گیرمون اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136976" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136975">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💠
💠
💠
تارتار دوست دارد در ابتدای شخصیت گل نخوردن را به تیمش منتقل کند که حریفان به راحتی دروازه تیمش را باز نکنند.
⚠️
⚠️
تارتار در مسابقات مختلف خطاب به شاگردانش تاکید کرده نباید به هیچ وجه گل بخورند چون وقتی تیمی گل نخورد شخصیت پیدا می کند همانطور که تیمی که…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136975" target="_blank">📅 10:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136974">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🗣
🚨
شیوخ ابوظبی اعلام کردن دیگه ایرانی‌ها جایی توی این شهر ندارن و محمد قربانی هم به این دلیل از الوحده کنار گذاشته شده / هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136974" target="_blank">📅 10:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136973">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
خالد در آستانه بازگشت به پرسپولیس
🔴
❌
مدیران باشگاه پرسپولیس بعد از منتفی شدن حضور محمدرضا اخباری در این تیم برای تقویت دروازه خود به دنبال جذب محمدرضا خالدآبادی گلر سابق استقلال و فعلی شمس آذر قزوین رفته اند
🔴
خالدآبادی سابقه عضویت در آکادمی پرسپولیس را…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136973" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136972">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136972" target="_blank">📅 09:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136971">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVTZsne6M02nDDS0F71rfSjsbTBV9tKr6ODUOED_YpEyq9rNwIZBIjdcSzTOX6YTg3AMM8p59wYjvhGWNeSI-d_OgCbNuL-NxMlIn663zId9BZV49VZurtAnBE_Zect-5FbgZVGbU0stlfFkHzz_fU1uplbACstHO_lW4Q-eI4JoaAFVoztAf6Bu9dwRYj1E3bng4WMwwc0tRmA4RfZgqtMAazBc8GV5uGm1OI5B4ixxTFjfKwIpQgbzP3E40fZkdRSXCMPYjwLUd_1AdsRfC5-x849QQCmITiGxPw72N30Y5DFEfIZzSGWOfFYMFpQQ-Ie6Dmv3fnlDRa-HVuiN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خبرنگار ورزش سه حاضر در تمرینات تیم در ترکیه: اسکواد سرخپوشان همچنان ناقص است و احساس نیاز در پستهای دفاع مرکزی، دفاع راست، دفاع چپ، هافبک بازیساز، مهاجم و البته دروازه‌بان ذخیره احساس می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136971" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136970">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✖️
✅
سه گزینه نهایی مهدی تارتار برای جذب هافبک بازیساز مشخص شدند:
🔄
⏺
1_ فرهان جعفری از ملوان
🔻
2_ مهدی گودرزی از خیبر
🔻
3_ مهدی نجفی از پیکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136970" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136969">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✖️
✅
سه گزینه نهایی مهدی تارتار برای جذب هافبک بازیساز مشخص شدند:
🔄
⏺
1_ فرهان جعفری از ملوان
🔻
2_ مهدی گودرزی از خیبر
🔻
3_ مهدی نجفی از پیکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136969" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🗣
🚨
شیوخ ابوظبی اعلام کردن دیگه ایرانی‌ها جایی توی این شهر ندارن و محمد قربانی هم به این دلیل از الوحده کنار گذاشته شده / هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136968" target="_blank">📅 08:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2J0Y18noglIjlv5dC0SUx4dEylTC3j70QDwrP2DHNw_fPtXM_hJQWZxJPih0zqRX_f7SpskbSc0lDYv60ff8lvblIvsTm2yKK6jqYzUyE-pTCRvXnVo-eOultdzeCvcQgW4c5fvyAd97UMoUB5SwqggGWGRasdYsBYoXgZE3ZaoymkcCQZZzwf5o70_ehCRGTsVe1UsaLPhirAg8Cj-8xRKu0pD0Wq2wSCEZd5k4LX-zZuTtOGcIEIwmzaPsldchA-3NEYzDYJM7bbyiDwBMxKR4KVrxFS2-Ndu3UfG-M8ibsk4MEii_WI2Zt0Erbdhn0q_9b1WGK05KkjgBDPrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136967" target="_blank">📅 08:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/How2Y_aywMHhyJrCnUK_N89OMXVn3CTCqUEnTZqnVdBRaxk54_b1KZ88Q8St7Ob2G4LEoIutXKduF_JMuZNroVJGfh7zCsQuI7pPYQEZdXCFer1HoDBt2bvWk5Q-1UnHUk9fcKO4CBJhp9Zebiyp4ZD6Sm1nouutXKQDjCx8y8ON9Y0UV_u24Pc0_vs0QAW5HcBlx4hOBf5v_or1Wm-bGl9oQ3KiphT6SJhWVpdsuK34rz7tgSIFdbW22655Hv-ycop0LwAa4GJ-xvVjBZj7ByOdzxB66S0xWfbkD18_R3cpa4orWYdak7T3XfbeGEKs6oPXwlTRR4_X7mmFcrXEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136966" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚡️
⚡️
قرارداد دنیل گرا با پرسپولیس ۶۵۰ هزار دلار است و این بازیکن اعلام کرده تنها در شرایطی حاضر به فسخ قرارداد خواهد شد که کل مبلغ قرارداد فصل آینده‌اش را بگیرد. گرا در مدت زمان حضور کوتاهش در پرسپولیس به اندازه‌ای ضعیف ظاهر شده که نه تنها باشگاه‌های لیگ برتری،…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136965" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136964" target="_blank">📅 00:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚡️
⚡️
شنیده ها: با درخواست مهدی تارتار؛ باشگاه پرسپولیس فردا برای جذب مهدی گودرزی اقدام خواهد کرد
🔹
پ.ن: گویا خیبر هم مشکلی با جدایی گودرزی نداره و به دنبال درامدزایی ازشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136963" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚡️
فوری از مهر
🔻
برخی از دلال سعی در فرو کردن قربانی به پرسپولیس دارن ولی تارتار گفته من چهار تا هافبک دفاعی دارم و نیاز به این بازیکن ندارم
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136962" target="_blank">📅 00:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
شنیده ها :معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن باقی مونده.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136961" target="_blank">📅 00:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136960" target="_blank">📅 00:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svc8ZydE7O6lw5fATHojFTrWEvq7o4ZXcy_dcqI4p5YEXiyL0KsGO83FY6FMVFjqKh3Smzxeek742hvfJcwMUlEHaAscIxgF7zXHjOKJd5HRqy_v-JiaWX0rHKHiu1AVDMRbjTKtrEbq0Ve_lKhaV6LtcGafejwvySkKjNCMKZT8ny8NvLdvDTSYL5O9UYrqeHUgR9x9J64JA5ArPYRhjJ2xX_4Q5cSXyAESRWzqhuJ1M7rU3Z1lRb99aJeNP3qRz0ngQd-4jc4tTYDkRmYdjO_3pmfZkv4uWTBG2VYik37D_S8lpR28yUiyS4g_jGciw60Z5ZbnTZ08vKWc5efxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
سرخ‌ها در مسیر آمادگی؛ تصاویری از تمرین امروز تیم با حضور لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136959" target="_blank">📅 22:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🔴
🔴
دو خبر از قدوسی
🔴
امیررضا رفیعی به احتمال زیاد در جمع سرخپوشان ماندگار خواهد شد
🔴
🔴
تراکتور مشتری دانیال ایری و کسری طاهری شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136958" target="_blank">📅 22:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS2KPc61AX5JrVl_Hl3tZXzCftO1iUEqFZSzHvyoRPpXbL9KCYyj9ELsHIQ6uJQY0ydJ5Y41NgMFAt8WAsVyjK2nR9D-NGUpC-fSvsxswNY22mARCtl_2WLGeW9SqXGBvcqB6Rt_JFDSWzxt_jLVmADNFGVRchZTo3RANhU9xd8GG2cs19yB6kWhW1wAuXp46I2CvXZclnr-6VpvqLgq50Yc_iOQROJAjXcgPMBPUHySqCddiulSaM7NjjVHPAqHuDsKjiKG0K78-oKfWGUxuJNrBWDevOLzEkdVAyaBxwxqD8ozfd2i2UGi_wFtxw0X39a9C8h3HnFhjqiU2rKuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه می‌کنند. این چهارمین بازی دوستانه پرسپولیس در فصل جدید تمرینات خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136957" target="_blank">📅 22:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚡️
⚡️
خوش‌آمدگویی پرسپولیسی‌ها به محبی
🟪
🟪
کنعانی‌: بازیکنان جدید باید بدانند به چه تیمی آمده‌اند. خوشحالم محبی به این تیم بزرگ آمده و امیدوارم لژیونر شود.
🟪
🟪
علیپور: در جریان بودم که محبی چقدر دوست داشت به پرسپولیس بیاید؛ به او تبریک می‌گویم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136956" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136955" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
❗️
محسن خلیلی معاون تیم پرسپولیس: دیشب با یک مدافع جوان قرارداد بستیم. با یک مدافع چپ نیز درحال مذاکره هستیم. با یک دروازه بان نیز به توافق کامل رسیدیم و به زودی ایشان به ساختمان باشگاه مراجعه خواهد کرد و قراردادش رو امضا میکند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136954" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
🔴
🔴
تارتار: حداقل ۴ بازیکن دیگه نیاز داریم تا کامل بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136953" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
🔴
🔴
تارتار: حداقل ۴ بازیکن دیگه نیاز داریم تا کامل بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136952" target="_blank">📅 22:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚽️
بیژن طاهری: مهم ترین دغدغه ما امروز جام قهرمانی لیگ برتر در فصل گذشتش، از سازمان لیگ خواهش میکنم جام قهرمانی رو به استقلال بده چون ما صدرنشین بودیم و حق ماست
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136951" target="_blank">📅 22:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚡️
۸ خرید پرسپولیس در این فصل راضی هستید   پ.ن البته هنوز ی دفاع چپ و هافبک بازیساز و گلر دوم به شدت نیازه و جاش خالیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136950" target="_blank">📅 22:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff7jaDRdIyY9aipgGmbi1AS8fA6YdW6jpT8TCY7aRCIsPkt8M30wBMlhghlpTqGJ8EXFHIOxR1TINnEuiQ13dShtxCyqJ3d_4BCwM_b5ajTtT7otiRFyu-XvE_sCQAXcgTWJUTRt9RttI2tIgQnbB9m2MrSiqTQ4n7_bdOKAqz-LOsJ3BScDcUlFCkdK52W2TFW1WrcsemBjIyCcp9kx6AGYsB9_eHkJQhDQrpkaDXlogx9H2y623IWciOWCNjZ7-YLi5raYtwoRiKaR-3rJIkrSogloJ01h-R3gWBlw6mkO2ryhLN0_EPS0CpLsKuVfSx4r-y808syhKb1-YFc_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✅
کسری طاهری رسما توسط نساجی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136949" target="_blank">📅 21:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
🌹
رسمی؛ دانیال ایری به نساجی مازندران پیوست  پ.ن.... و همه سرکار بودیم و از کسی بخاری بلند نشد برای جذبش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136948" target="_blank">📅 21:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات، نشانه ایستادگی در برابر تجاوز است. ورزشگاه تختی تهران بعید است به لیگ برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136947" target="_blank">📅 20:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhF8tTltkw5Dlo-irWsqzMicUDXDkAGktPBurdjOYKt9-J6qcLDo3JAaNEe-u4wk4sOmnlbYOh_IgzxlWfgRBvf_YBpAY9vs4mBUndgs9sU435b1TMn8sMEOAztbf2BdxxAwF1TT0Vod3lAy4GDI5HdTnMLoblmd9TZAWQ8g6BHiTTPVicrvs7R14-yQRc7y023AVTCKxFSQpHyL-NnF87-bXvtUbMyscV5S7JX33zWqYPeCDM9iQytUQ3I1igO0c8aerONsD4Pcex961uR5UDzFGhWvlDsIv3DW_48fYDMK3_FFpXt7cNpXBHAeYqfRqvLB_nyf38N6RInbP4AKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
⚠️
امید عالیشاه به ذوب‌آهن پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136946" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWHX2C9zt9Gwtp9lD97ma9lju_k8h6jIqB7M-1VKVhp_QeSLHHBux0ZitiJw3-4xFQ7hMORfzLYLlbJReJyB09AYIbw42VVaouMwq36LsJXBImBJH7DZIW9sXS5ml2l0LKYf3Fdp7WIK9nOipbg3kRfqEu1Vaaiv3KC5kVclT1T6DPeU5_dEmr_ZMUacvayzevBOq85s4Yxo0PybJaCIfauE9sqlzSeb_q_nKfur-Fdt5hTZ8Oc4-lYfaC5qgL3RoG-05s8aFSkqxWJKT6VwjBLfoNjxm11NMD3AAReIUybh3zrVSCgnKeEFtf2dKv7J3ofGxdmO08xAiaUv31ClDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🌹
رسمی؛ دانیال ایری به نساجی مازندران پیوست
پ.ن.... و همه سرکار بودیم و از کسی بخاری بلند نشد برای جذبش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136945" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHXpUbRP7w3r7Tp2re79ySi9elRXrVn2yc1hfc29LJcsVyHdt_JaT7nw0zAs68Z0Q0nNjLqXJ_mJrYaDDE752OjcBDxP0OqiI1ok9BQ-ATatg68_Y-TN5agG_kUqxOGN4eYRmmnObg46mmgilIwv2MObb5LdoGxbHZaTzG0QCnMzWGQxcjEukXrvIVKIL06St3XYsfCghz9IWhvlTbp_1w541Zf_qZ5rXBsJ_VUOiM07MGwJibo1aE9LPMgakmMXb9171JvFWvwEhjASI9a0K0-z-U9f0BxEUqGB4De1qioPhyfpaye2Rfj79gXhZQs9Pu3p4b8OumY7WSxC_DFfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
امشب خبری از شانس نیست؛ اینجا فقط جسارت، تمرکز و یک تصمیم به‌موقع برنده را مشخص می‌کند…
🎾
امشب یا فیلس دوباره قدرتش را به رخ می‌کشد یا جودار انتقام باخت در تور بارسلونا را خواهد گرفت.
🎾
Fils -
🎾
Jodar
1⃣
هر گیم می‌تواند جریان بازی را زیر و رو کند.
2⃣
هر بریک‌پوینت می‌تواند معادلات را به هم بزند.
3⃣
و فقط کسانی که زودتر تصمیم می‌گیرند، از بهترین ضرایب استفاده می‌کنند.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136944" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔵
🇮🇷
باشگاه نساجی مازندران انتشار این ویدیو از دانیال ایری مدافع جدید این تیم رسما رونمایی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136943" target="_blank">📅 20:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=oh0BDKA8n_S3AkscahsLy5StJq7MIEiEncj4TTuUEuJuVaZRY-BYvqMj0lgx-eY-A1DWzgV88FS3YQvfdnanVxWcwF040Aj7JpNXJz97OHln2EiTFheYfRyFJjxaLEyigg4aligguFzfI1NJWCbWvYS26MIEkUkHcURA6rqw6-gPUolelceqYUKkGBwQuT-SRPmXCHkoWgYPgNauPR551lwF3Oh-WndsXX0qYROeDOoyBUwKjmqNDSHTQYLlZ5veErp395am1iK3lR0Hliv8t3gFMzKASySRPwx3G3fNXFlv486wC-CMRKQ3-reQrTenEG5LQwQ0qxXPcSyZ59TFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=oh0BDKA8n_S3AkscahsLy5StJq7MIEiEncj4TTuUEuJuVaZRY-BYvqMj0lgx-eY-A1DWzgV88FS3YQvfdnanVxWcwF040Aj7JpNXJz97OHln2EiTFheYfRyFJjxaLEyigg4aligguFzfI1NJWCbWvYS26MIEkUkHcURA6rqw6-gPUolelceqYUKkGBwQuT-SRPmXCHkoWgYPgNauPR551lwF3Oh-WndsXX0qYROeDOoyBUwKjmqNDSHTQYLlZ5veErp395am1iK3lR0Hliv8t3gFMzKASySRPwx3G3fNXFlv486wC-CMRKQ3-reQrTenEG5LQwQ0qxXPcSyZ59TFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇷
باشگاه نساجی مازندران انتشار این ویدیو از دانیال ایری مدافع جدید این تیم رسما رونمایی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136942" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#شفاف_سازی
⛔️
در خصوص محمد قربانی خیلی هوادارا میگن بخاطر اینکه تراکتور تقویت نشه ما باید جذبش میکردیم، اما بودن خدابنده لو،باکیچ،پورعلی و لطیفی فر به هیچ وجه قابل توجیه نیست جذب قربانی
🔴
البته باشگاه قبل از جذب پورعلی و لطیفی فر برای محمد قربانی نامه زده…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136941" target="_blank">📅 19:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCfe7l-YsIZhLKruyQPBQd80lQ8Yg5OG1wU0BrtCq5OvNz3_xWJwRzEmF9P9e5hLzRiahIAgt3E14OxVglNNTTaEe2TN3yomXm5CM3EAxTp9CfyJqswaixqmH6-dDTZQ4JdbpFuioMEwDBZSQVbXzQOwP089VdojbJyn5OLtwY6-qzeYeyKsdT96scvbM3YxPpnX8eORPiNY7KI1hnMnqb6bQyqTip1y1kVDfEDegVTMfkT5wnIR9lEFtXWRul050Pz8Yi2lzJOO_A5nmMUi7Y5RrBmF9IfkkltmyVezNO8K0vCLmJ6obyvtf1DInkzytRviIqxEDNASTXdO5ahauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت عدم جذب دفاع چپ، از همایی فرد برای دفاع چپ استفاده میشه
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136940" target="_blank">📅 19:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚡️
⚡️
#مهم | ادعای جدید ترامپ:
🔻
ایران در حال حاضر با ما در ارتباط است تا به توافقی برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136939" target="_blank">📅 19:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnNAhqPAoJhEq-rvjkkWeCueAm5Ave96Y_2FguvINd5Y_gCN2HPpy34ghaWKuAlNrt6FvPqEVdbTTBAWXXWEJMYy1vloAvNo04MuZ9zybe8SgLbQS9Zc87Ye0XHewPwXtV4088qRMd2gU48tMzLByfpfhL_eOM-upMt1kCkjYUWa3aid4UznbpC3_eGoDlAlD3QGtlau9w9eoUcl_YhMoByCW6n0tDuGjKgX_6sb7aBCGQ0WoZ2UjpgYdLJyZlBmZJeGM_iQMJUOoulr5EtNIqvhamW-Bs217QXCl4jFOcNQjq20h-ie8Z65RcsJmIS-gnW9BFHUnq5yZ5jsc1-Kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۸ خرید پرسپولیس در این فصل راضی هستید
پ.ن البته هنوز ی دفاع چپ و هافبک بازیساز و گلر دوم به شدت نیازه و جاش خالیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136938" target="_blank">📅 19:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136937" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c4177448.mp4?token=un_8ksBW_23NrexWl0W1uaQwyTno4f-XuWwjxS2OUrWYPyksE4UuiPv4-mLrDwVhvTFSzM6DVCVTIctR6NTHFyo95wSdNkm9MT7_8IR_ZJrHN3P6_a1U4mxKeVNJ5_ikKMsNz1GAlotAHT3_YnZNqnhZ5a3UZxmmu3ZRqhix4xv1YWFMHsMOEwm1ZXn1y6CeBrV9mbhoXBxD47NuvXcOAemyka7hCvuZlRv6avyzl3LHRKBGpTKGEZWNliqEo8yY2sfMCMehvTJsOK_Gj9v_1fkv5-DzOnbQwx3LMXGbpV4CMjV2dvvR1sE3AYABsLTeTkENeLSEiQE8jHrKI8-BOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c4177448.mp4?token=un_8ksBW_23NrexWl0W1uaQwyTno4f-XuWwjxS2OUrWYPyksE4UuiPv4-mLrDwVhvTFSzM6DVCVTIctR6NTHFyo95wSdNkm9MT7_8IR_ZJrHN3P6_a1U4mxKeVNJ5_ikKMsNz1GAlotAHT3_YnZNqnhZ5a3UZxmmu3ZRqhix4xv1YWFMHsMOEwm1ZXn1y6CeBrV9mbhoXBxD47NuvXcOAemyka7hCvuZlRv6avyzl3LHRKBGpTKGEZWNliqEo8yY2sfMCMehvTJsOK_Gj9v_1fkv5-DzOnbQwx3LMXGbpV4CMjV2dvvR1sE3AYABsLTeTkENeLSEiQE8jHrKI8-BOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
بیژن طاهری: مهم ترین دغدغه ما امروز جام قهرمانی لیگ برتر در فصل گذشتش، از سازمان لیگ خواهش میکنم جام قهرمانی رو به استقلال بده چون ما صدرنشین بودیم و حق ماست
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136936" target="_blank">📅 18:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZufqot9bKAlvptzBECkGlDQTyMsaesRyhd3XlWLcBHAhdhDjHUXmujFnXZE8gz6bqm-HslWWrbTnBFbOSmHdCcOKFSA7IbIUzkJ6VhmmthoEyIEyLi9Xx5TOYBDJHaN-9KxVEL4q8knSpyX_sb4a01wdE1Hzx1p9kiLV3jxYxo9dsfKBZl2VuwlZ8k-DqhGfiCJBuLMnf7puVnTs_UVEZbbkmr9mAV6n_r-wksmjc8Q2V0o5QOxD1UuHW8vRreUS99AYzxkp_MCxkJRsVg8fVxYfD_RCCm46L-6Ouf-AITbp2vTONKUpStpTocSt4lm8fiHBH8110y57fd1lolOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136935" target="_blank">📅 18:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136934">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136934" target="_blank">📅 18:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136933" target="_blank">📅 17:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKl6y7mOqldujl8dbkmJShtZVheoUO3W6ek3pYCIjIzzlNPeIWMi8sZgi1BdIPqYvGhTiiFDe-Z5pM_7PwWz2kw-oNPvazLed6m8ay1hK_SCy6FofQL-8TtxjR4LwTG9_ie6k2L9OrppIpYfI8ZpMH8SZrM-W02tZCiMhvhIKHRPmks7S8RoXTpGH7dAWNMzIXnHRNGa1PTfvhEyzxwycMyOpGaams029JY64GOIMQh-T-VtcbLLyk0lCCsvcsDLeRVHZNYPON-ZMWkggQsqU8_DwWnHW9LuEyq-y83TLsioS-gAvivzDbVYNWgoTHcgm-zvsIRfD4TXyYRkJ77xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136932" target="_blank">📅 17:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136929">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136929" target="_blank">📅 17:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136928" target="_blank">📅 17:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136927" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136926" target="_blank">📅 16:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⏳
⚽️
پوستر باشگاه پرسپولیس که خبر از یک خرید جدید می‌دهد
🔄
به نظر میاد محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136925" target="_blank">📅 16:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136924" target="_blank">📅 16:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1hbo1gNCWAlKBvDTrbtLqcIHjW3WWWa8dr3XAPBUqYxjulAKmCqvjSj9mDvMUxJyicBj5nk9KuEpSCKOmv_U68AddLZue8qRhz43rVaDZPINUWxsi4-lupqAA7NAhAC3YHKsvsprle1wSAwTr5NI5_LiXTEMXdCkNzORSslr_8Ki3okE-2vglvcoVZtak8LawrNzsT03LacJ1-exZ21y5jV4t_Udr0Ew-Z_-L8wsmO6Kp6FpMrS0F1gJSvFOZIbIaShAoW2nhOW_yAMs0QwR55X7-Iw0kK2ggwpm2nKmvPG8QCKaCp_Q7qHLPbxx5DEGd8VAsrT49IbP6wmFeeYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
⚽️
پوستر باشگاه پرسپولیس که خبر از یک خرید جدید می‌دهد
🔄
به نظر میاد محبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136923" target="_blank">📅 16:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136922" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚡️
⚡️
⚡️
شروع قرعه کشی لیگ برتر تا لحظاتی دیگر
⚡️
قرعه کشی لیگ برتر تا دقایقی دیگر آغاز خواهد شد و مشخص خواهد شد چه تیم هایی با هم رودرو هم قرار میگیرند رقابت های حساس و نفس گیر میان تیم ها امسال بیشتر از سال های پیش هست چون لیگ هجده تیمی شده هم بالا جدول هم…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136921" target="_blank">📅 16:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136920" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚡️
قرعه کشی لیگ برتر امروز ساعت 16 برگزار خواهد شد  ببینیم دربی و بازی با تراکتور و سپاهان هفته چندم هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136919" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136918">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136918" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
در مجموع با توجه به جذب نشدن اخباری،رزاق پور،اریا یوسفی،نوراللهی،قربانی و...از دست دادن میلاد محمدی،ماندنی شدن برخی مازادها و متوسط ها و جدایی بحث برانگیز پیروانی و برخی بزرگترها، اگر ایری،طاهری و محبی هم جذب نشوند نه تنها نمی توان به باشگاه نمره قبولی داد…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136917" target="_blank">📅 15:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136916" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYq5tT72Tr_FnN-eMKtJp1Ot8J1FeVHBi3qQti4OaSvBiqBKbeF5rE49gYT8R3XWyUXY8fkZNd7bHVoJuL6fu4CH6mc53q8Jxf13zw4HoSZpJnEC0q4Ythw2MhtgJNfCN6muFRqUAElq16MvswsL2dv8Va-srdy1HOiDRw6VTmzQ9qpCjt0QbByeUPg4I-t7kuL7edz4ptwexr1_v846_BtcTCNdELDArGL5x5YDN-NQf18-nlaudxtO8X4Wh1EAD_BYgqBiBHcaDVrOPYu94UDqbyuQXyRiDMBojdBxFXiTRcpeJF39iBhU4uIyaIA5kWrLNI5yqdLBXC_XupkJAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
منهای ورزش
⚡️
⚡️
طبق گزارش‌های منتشرشده، اپراتورهای تلفن همراه برای اینترنت بین‌الملل ضریب 2.7 در نظر گرفتن؛ یعنی اگه کاربر 1 گیگ اینترنت بین‌الملل مصرف کنه، 2.7 گیگ از حجم بسته‌ش کم میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136915" target="_blank">📅 14:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136914">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMqwcWMZjViK2gCeFv2j0FoaDmEL5QxWSad8PBK3PuL6QAWxZrGcD0m3CaZ-u5KdRnYNv8Cg9COAU-QYH59zDNQBwdHBujy7_UKRJhIMtXhiK3f8zBY5gnh8-RT4S7RG84nfFqZDuRTyprDXm8pu7sXXdkuGFfAkKoDownZuFIjZQtN8rf9ZJeVNbhxetJPUyiOozq7WN1dy4CXx4RNPiD0kyT_W5VgW9qzJ69GNqu_Qn0ja45aPwbimw2BfUl4Id0XrTR1r8XhHXz-gIDMzJKbtQD5ZXcgp0xtpyVd491uetfaQ3cIpWem-aB-kY-chP_yqAuRScUawvwxDX62l8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
از توپ جدید لیگ برتر خلیج فارس رونمایی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136914" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136913">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
فوری؛ قرارداد رضا غندی پور با شباب الاهلی با توافق دو طرفه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136913" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136912">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136912" target="_blank">📅 14:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaISFCB-0vD3WraIbIfP26OyZ0S3pfNslz7JIFbPcumsSLTSr01erZlF_D_fcf4D3oRJ0eIK7KavIRpU1DwuOEbratUV9Rq6Evuwzkmn74lSpj5K74FaJ7h1IRAC8BWs_fc1SyO9wLg1CQFHredmKgXTHxcwNF9yWfLIHC4ETLosmxfobe9xop1n6gxW1X93CY6QwoXK9905t23uc2c91k3r4WwQ4bmYzz-zPEAZKe5a0uMofAzKkT1UTXZLiBd5U9tTlqivZ7Hbc7OeV87onrs3SK1Bn0sNXiHPaFL1ktBT6xC_5TLS9FKekjXsiU65VzkIg6vknPi-1psJ-Y74yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136911" target="_blank">📅 14:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136910" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136909">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRkhbzKzG4HAG2Ukwkh2IT-vnWT2oELP9xjs__2rpeIhYBtkzSOchOvZrJC24GXkI8m9hXvHLKhyoS6VdjdReRNtYr3ejx6REGtxEfFb7b7p8HhAMucCr2XW3KE3oCj8fAiqYF0JGc-Ba1ypcIUPbVWqblMsfTZxxvL6bRF8PRcB-FI_Ckz4ShDf1x_q3lvDDVMLmzo8zSh0SpkB6m_cc05MpcAYFJd_jh1PX5_4TzXSVNySLxGqVZ6J6oJTCtId4ofkNp_jx70QAuCWzUOsJ2rA2Tx4I8qFGSPL9ZYCwMU4gJO7Zr5gWXamLaovRG8PzIWcY-MIZiLCs8frH2HIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136909" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
گاف نقل‌وانتقالاتی چپ پرسپولیس را خالی کرد
😀
فرزین معامله‌گری، بازیکنی که در نیم‌فصل فصل گذشته از شمس‌آذر به جمع سرخ‌پوشان اضافه شد، در اردوی ترکیه حضور ندارد.
😀
این بازیکن به دلیل مشمول شدن برای خدمت سربازی باید دوران خدمت خود را در یکی از تیم‌های نظامی…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136908" target="_blank">📅 14:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbZwRsAvTinyLRO9fLPmy8Xv6vM6aTM-5LZeIkrGZESpO-Cvyh6yCRhfNZNUlmIPzqW5YdZ7wcUWd0zqjOCoXgmU9AEjh-uUQ7XRfBYJcYFs4N2yZCCEr3XBt3bRBRjzFriALmfjvz93gk6A6B0cX2yJf_9x4okUeIZmQ9fpzX7NN8lTGM2iJ7L6ueaNg6U-7PzEvdWg4rglRo-g2T3v-ERH72bhnN7uOrv5eRaysHhi5UGRs29AtWQtE6_R_S_OZgm3_YM32pwd3rg6c2Z4Cd7puVGzRKn5b6ceamwVApTwj07UAmxQjVgnUeYSLSEXrvqA0fMiK8df0mxvZXvwUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136907" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPn1WyriE1XXlYE3sH5KPZENLnSa-ls-F9RNMFOOkt1Nt6bMwrBJhGINclcG8RtKfpVlvNo0dA6NHjZBHkendCpZlYc3rEAERrDuGPfOzV6GlXw5ZR-ZeZWFH_2PWxBvK1EzW0fHZaypyVyn8uTGYiAGdcO9czozqtUDwtu0eZ4n6tWuIdoQfpSRTp9b0Cia3_dey2ZSD60FDcBROFrDku85W3MpvqYkxxkw0IxR_DDrNaMjZhCkkhvJH9c0SBtMnAkbPhNcadwFPVLlGZn_W0mgGFBVkN_-XCIH9Vwyvqa56GvM8KBJSeWRE0iNccJKKEFbT9OM4o-EalCFBZNKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
زین الدین زیدان  رسما سرمربی تیم ملی فرانسه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136906" target="_blank">📅 13:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4p0lJPwPEf5PkRpiJpI2KaXYeC8vgogF9K0Q5ngteJoNGlmky8xlky1-sMp1_iVWBhNUkr3FAoXv12TkbSWBU_XGLwx1ThfIPjilM-6Q-Wnoq7JlS-pX71VUCrCRgogs3M3WORwcFqrT9Igvq37h2zeoBNTtAC3ljdaMyCkKmWIjv32W9hbPxtQ84NB4_7HhHyvLKuUF7tuybcDC5zcgPDGJ1rr5yWf8YhUXU97gOPhSvQSUaT3gciMSbEwpARhYmWKEqZWBv0K8DYWqc-jcsQfbqf2SVXT1YAvXARMm4OEYnm7PBm7oijAdLcQaipZ-BlVT05zrV22bxaG383H0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136905" target="_blank">📅 13:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136904" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136902" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136901" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136900" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136899" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136898" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136897" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
