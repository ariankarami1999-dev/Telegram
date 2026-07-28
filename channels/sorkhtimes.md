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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-136921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚡️
⚡️
⚡️
شروع قرعه کشی لیگ برتر تا لحظاتی دیگر
⚡️
قرعه کشی لیگ برتر تا دقایقی دیگر آغاز خواهد شد و مشخص خواهد شد چه تیم هایی با هم رودرو هم قرار میگیرند رقابت های حساس و نفس گیر میان تیم ها امسال بیشتر از سال های پیش هست چون لیگ هجده تیمی شده هم بالا جدول هم…</div>
<div class="tg-footer">👁️ 369 · <a href="https://t.me/SorkhTimes/136921" target="_blank">📅 16:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⁉️
⁉️
از دیروز بین پرسپولیس و نساجی تنش بالا گرفته. نساجی گفته تا آخر امشب صبر می‌کنه و بعد تصمیم نهایی رو می‌گیره.
🔴
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/136920" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚡️
قرعه کشی لیگ برتر امروز ساعت 16 برگزار خواهد شد  ببینیم دربی و بازی با تراکتور و سپاهان هفته چندم هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/136919" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136918">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SorkhTimes/136918" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
در مجموع با توجه به جذب نشدن اخباری،رزاق پور،اریا یوسفی،نوراللهی،قربانی و...از دست دادن میلاد محمدی،ماندنی شدن برخی مازادها و متوسط ها و جدایی بحث برانگیز پیروانی و برخی بزرگترها، اگر ایری،طاهری و محبی هم جذب نشوند نه تنها نمی توان به باشگاه نمره قبولی داد…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/136917" target="_blank">📅 15:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/136916" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136915">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/136915" target="_blank">📅 14:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EikYOt0c3vauYWK8VyOwhybcEMlzC49_qnGac-qUHYXH8Dcji20oAiS5lyFFhS1M7_sUNp0N9Eo8x97A-Uc7uc4Cr1UVGSluZBCl60TS7xIEV4VZwuEZFPR56RA-O9YwxHVKOyK6sLVm7kTbiQzq2ekjlsvKQrethG-4WQ9WxqzAXnOEyUwDf20ryWpAvG1MEBNqVWhMHo3hxz-DD4ekNzEkkD6gq33N68bnZd5-id7H67gylVRWJenqwPLUnO2KdrAQhZ8KZWCIi5P2m__qtVLd0MXXFvgRHZJVvcnBG7zzztu1xumTOhGLcgym_imK9UzVIbO3WvRBfrwwWjujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
از توپ جدید لیگ برتر خلیج فارس رونمایی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/136914" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136913">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
فوری؛ قرارداد رضا غندی پور با شباب الاهلی با توافق دو طرفه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/136913" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136912">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/136912" target="_blank">📅 14:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136911">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p82Z5RtVOiEhuk3uDIz6Hq300-Z0pkQ9cP_H3RrRpILLNLzS1GzWKXkazItxHv6OWRpB2eXjHOTzrj46WnsRcVxwmO52wRtESwPMnL-WS_sR17zbol_5W3K5WPGz41izwtmONrGcU8ODI-gPWUvFR2c3HUAdsA4Q8TR-nlMVEGylWS-zzdEI1hgx623DjIoSoQ1buQRLgwFAU5cjQpPg5THPKi90iLt0GbdGM43eEC1s0ilWpwf03oeuxSW5cnwUqEgdltMn9q11PsX08Xd_NiJBUhEC1Iwpmlm8WpDBgmF8FvQG3ToPzr_MJtD0Begt54Xva3GcziETheKMvmcKyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/136911" target="_blank">📅 14:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136910">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/136910" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136909">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMhK-wxfSTD_336g1Nrxa9kXLGD8ekQGJvbrxvNDD26XinIM84RiJs4ZFuf5WWgXgX99nMzGux5urynALgV2UJmHDFB5pdgHvVyYUVb0Xl5D_ol1HUy8xLgKly8v6BZSp8fXbsEFQyNmQ5xdghG_xWMu664VZLPBWgoQ9ldYqMfEwcWDiC_e-JNRMqsbDPlacditqV86uR2sXJrMamPX5DWjtnMmk9Q-NbEm7ruF2BJx0n6QtbC0LE7gID2JTNUDk0CLfh2pR7fahAEg8Ve0MJQn5KBw0FDqpHi2dywMqnQW1rUZzcvEBcBw2_jq6fiWbs5k2hrAtjyWDWHr-tOG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
💛
◀️
محمدمهدی محبی 26 ساله ستاره سابق سپاهان که تا 2028 با کلبا قرارداد داشت، با پرداخت رقمی کمتر از 400 هزار دلار به پرسپولیس منتقل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/136909" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136908">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
✔️
گاف نقل‌وانتقالاتی چپ پرسپولیس را خالی کرد
😀
فرزین معامله‌گری، بازیکنی که در نیم‌فصل فصل گذشته از شمس‌آذر به جمع سرخ‌پوشان اضافه شد، در اردوی ترکیه حضور ندارد.
😀
این بازیکن به دلیل مشمول شدن برای خدمت سربازی باید دوران خدمت خود را در یکی از تیم‌های نظامی…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/136908" target="_blank">📅 14:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBTs29QpglaegitKvLCo2pDoz_t9Om_7HpL2fLCfntpfdSy97-MQvdZ41hXnds8UC2PW1G7KyLXtOCVTWfovOrfIYXHncEIcClk6lLklduBHgu8fl4EmaSLf61dAFY5z2htq1A5zp0o4T4wIorpEEyXC5UicbKUTmkty-m_WrNwpcW6tBtqUFqd53JaIeT-gV0BNtUTx4dj9L3XDD20W0mf572gioRNLpjOiGBDZHdkh5zPmcsiYPTBN_paqGYdzZCYIFndWOoN0HLnMyARpJo6dFzy9ewlVWIRZnFwTgpBevHgJRnf4KZk3ev002UxEG7okNtUXZFl4ep-jTs1V7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/136907" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ9LAgBydbrAtcTSsvNVLPbRx27qeeU98143jFfomfLSgC0mfJdPR6CTCHUxv63XuIUPzXDO8lykUY3FM58wuw0lZtAh5axeppTbVbEAiRnJvlkLBgyYjHjyxf7-nkKf8l48P_s8NdzEUlRcAi_Rh6hv7b0Z_-SHHzNPEenGMPXVReDabmj0ld9vWBsVf766Fsuyt6re9q_jT3tC6T8GfjvqRVDf_yGeHrZE3SGfG0PYp5w683zs29Yben0YrFwODWCmgMxcQlkU-hpaINgBrQ4lQEyBnxLf_cEO_D0ZpgnoNBM_mi9_1BI6jPAKP4fN38kEwpzeLCDHXOpJm1yhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
زین الدین زیدان  رسما سرمربی تیم ملی فرانسه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/136906" target="_blank">📅 13:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVeZsfL0d8KW0D-t6i_GnFoJbfsqzEkrTk0x_bMpK8I0mBrfQtj00s-KmIY8U2iz2187-1QT9vVvIwTDqF-Mnb88vVYglaFDhDwCaDBmxKMuh_odxWgIC8uc4Zix420Ytm2GOJFy3SBir34ReXauKKSp9XDmA4VXbDWKZW3WofTfAfjEh-7YKhdUzUU1wbndWLT_n_bK7I-3csPwN7TVRJXFTTfVhJEG3TtGP_C4OAnx-nIyDlUX0BF1QXB-iVIF0-LaIbuDDNxDLTZOp7aW3CVzjBA-DI9x589yBNGHvXbNyMUFq6GG6UOEeHMpcoF9XRbTOab-Hk0WKDwRucu8qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/136905" target="_blank">📅 13:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/136904" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136902" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136901" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136900" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136899" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136898" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136897" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG0zo9U-6fOALuMCibCLUN_ePRG2qXZrBXz9YBiQMWCfSmG4_Xla0sSAU-DcD05l3SctIRYukZeUL4XXRgaHSyToyG4lw28dGmQPx9DwX4NrpXUXP11oRhNGVX5N5xtHmV-KCnbFcyCLfTu3S9g_NAocsos4apQrYgQivbBSiydq-hQmyecrJt4oPr16gepeRU7_F3t492E0ULgPS8qysMaz1w4o0zdjE_QNzu_uOvIOGTbmIEPCnlrSf99fpe-a0L0r6Et-EqV2VrLniZNuG-qyDZ4pynkToDA8HzcTbpKTGeXecFmGQ1KOyZ-O_ILYyIQIjeyOHeHv3X6qFCqV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی
؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136896" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o41Dehhp9b_NEHM03-1J-DOsPj-SWRs9WzE92Y7WvMIL48iD1AR23TWXq62zieQefQ9lYXwN2Fnr-3ptOkAVrrnLx4oPStqYS1KeiojcVlE61boMxRoXZILfO7fJdKOKePT2aIj0B6SIi2z5Dtj7C4hvaRDqoSDyMTxMW0dLRvYLO0bqaVQyzdZAeOpapXEl_A41KD8cEAHz81rMVsQ8u67fAKFS2JPDE7LTImso3U2etnyTccato0xMg_pGPk7BJ7iETPatF7fC1V50fDVVUepJLwyzXi0a0JXx1lFTURsRnUzJjP0k34ihLl4C52gxQ0B0OhLp5tHqNAxC3hCOFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136895" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bTpEkEMnHuHCD7hSd2stOXKn8iVB_rxOpL20FCXSE3N6Ooq49omuIkdyXBVmIWuum_pF2sMQlekijzJO0i0ofwHXl9AMxGEylqoN_ykRVtfslMJ90SoxbnkiMX5jToMz1OYZebo9UGQXsHgl1SSrsnROW9o5yKL1sLsyKVN1w7ImtF8_p6u0EWC1jZX3b-P90JVvUfgOMpkxjnPA8RnsDVhkGDn8QE9Cb-gCCpNJVVQid_hnVvpFVCsmxTWAH7kynaqgtYPANQ8AAwzD6CaaxGy-_XpL9It-moPyihBamEjnteyAkXE7MGS1iPafI0fqmC_SExW8GT3gqPaLBWkPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/136894" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBtIL3pQoRFjVObmc2UgDfbmzexF_GMt3gus4yExOhG848x8Xs4KsJuyuRJL87Ltar-oBMevniNnq-8USDQV3nZjjVFAeCl2HHNkVi9CiUtSBfL5RNUzv4ayzqgihlIPjmda_2roaySsF_FdWWZneLuwrryHAFXE8II2ISc5QcVyO89pQw-9y-o0_WFZO-NzAqjU4mYVY63MF64kLEhioBwpfHGpLZ6CjoytzhhevHlyuYxGOSACkOKP-ncBIhixNCb5ifSOA5q3rJ1VSjDd918SI9-9h7JK0sX9BHpEmN4HxNRIE_hnz8LhziFJwynOHDxX3faj46urKSI6YY-EYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری؛ طبق شنیده ها استعلام باشگاه از وکیل خارجی برای جذب کسری طاهری و دانیال ایری امروز میرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/136893" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136892" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/136891" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/136890" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136889" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⁉️
⁉️
فردا شش‌ مرداد حوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136888" target="_blank">📅 09:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136887" target="_blank">📅 09:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV8JwF4kMP71JXJIazVgFE59402RsEn-5ZY4A_HeoqlfRCwBv8dKv057_U6mvHP071Y09eBs6ykfu39wqp8tIK_0DN-FJCExyIwlHZspHRveH1fP8-R1TiIlKPIVyfy7xVl5BdKvB5BHl9iPaI-6giWbMi29lRXgwTk1URdbHxGzyYFWVyAYyY05MdqXWHCRBX-WdLlwHCGmJiNYAS5IrI6jSSd1CDK1zuzU9yGNQ32xOiADl9k2BGmw-ptyC2u3cPzqnzlqk9Aiwmv8XdQ4K3gpEdGqXQ5xbyBzNKitZZBThPK5z9vu0K0MgQ_yF0B7THqheHl4KbfJc9GbkOhC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136886" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUviixKu5aKkptpc0UYVXURrZsurrZOQ6BhErucIXNcDPZ-EbqzZ0UUn9DyaSAoknVYjt7VuYXsDwzYS0JTkFUrWZy_I1EaoK3NgkMYHUXsH6JFlDMuwTTSO-hynoYf4TtL17ZlNpH698cLGJBAF088rhgnwy9g2K7yY5JfcqotCxWB9TmM7Y1QGSz8RHAhae6LwT2A8rovSZji5K_sJawoEsAYv534JjrFPgVbb3tZGXkVI61Xb1P2RKIqnoVOziNQXEMKBhItdgxQQurNhxjGEzYfiS1A6XFmllhdzFFsdTkgMhX_wfOjr4UD7k1qIInCQLs9TBEyOQBcwHpLP0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136885" target="_blank">📅 01:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136884" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136883" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔄
لطیفی‌فر فردا به ترکیه میره تا به اردوی پرسپولیس اضافه بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136882" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136881" target="_blank">📅 00:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔄
🔄
تیوی بیفوما در پرسپولیس ماندنی شد؟!
🔴
🔴
مهدی تارتار اخیرا در تمرینات پرسپولیس از عملکرد بیفوما رضایت داشت و به مدیران این تیم نیز عملکرد بیفوما را گزارش داده بود.  با توجه به عملکرد بیفوما در دیدار روز گذشته سرخپوشان برابر پیرامیدز مصر بعید نیست که این بازیکن…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136880" target="_blank">📅 00:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJNMNZHK9a6C6nvDoN0wYQqqZ4VStHCqoGLtL2TRY7AQeXZUl7rNx2O05ooUeHDUMNnBwnj4C5ghYkLOHj4hmflfmegYzqxl0ZCM_a-CGc-r9iG5U3OW4VSPDVLO5ngocxZMypS_0Gd5roiz-GzCKaJw9ld8Uaadukw2YC2YjpWwAWZu9MVfyOTN6_4EZWUl1BDWnxvWhcuO4b6uUycQetycu2eCIoJubm7etPju6K3toTRENqk3qZccRYl3DshxDzou7MwSbWHf-8ziwmcov-WTG4lywd1MvltU7lXQOGgXnkfuEKGu6iN9HnGKGhIlYmBkV0GmsLa_JOni_MP35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گویا رامین رضاییان به خواسته 200 میلیارد برای
هر فصل خودش رسید و در استقلال موندنی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136879" target="_blank">📅 00:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
⚠️
قدوسی و حقیری: مدیران باشگاه دارن فشار میارن که گرا بمونه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136878" target="_blank">📅 00:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
قرعه‌کشی لیگ برتر ایران فردا انجام خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136877" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b310-6xofmdJRIdOsW_D6Y1fNq6aZg_JauoBE7XwTivV7oTnmyVzkJCSJPF_orENwxMCLvazAZdSMGDu-uiQ-ngCd3BZo7m1ZuyXD0D3Yjt5n6hZNo5Umou0LYs7DFOYF60vKI7lrppfUbKaJa0zR08fh8Xw5EjRoVfygl0rADuSe0QFQr-_GBiYN_UUp7kQqsq38z9gEHdd5vb7R3rP18G7dawc96gN6Zf2c9rbnhvTJFQbWp9KggjKODKhSGIoh3BxcjPHh8LbnAkgUEntjPipAsghs8u76122tZeJ-ihLY87_qgrmyVzkCZzEgGG53WuEtjWrISMdQUDTqOu_7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136876" target="_blank">📅 23:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند  #ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136875" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136874" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izjas0azn2jcwyPpJ45wVGQSJA_ASN6vhQHYOPPS8QCJMlmwS_wf5YJnibvFwdMsR4tjImSt7B3OSDp8stsuYX09C5nliaffsaHZAitoSszAgReKo07UZZ_E3HprWK-hQ423Ylq9NQzQfVPK3SGMJeUHhmNqjYJaa5GfiPgfFxuNBveQoHOT9CQ6T8JTA9ER4kv8zMkTpm6Y5joTSabI7Ncrkaq6wDS47EgKicWLtwVeFHGTQsQm2t7Or1JNuIgkE0TA_HfewvaaRvRoCiGnma6PC2QrST2sbd4jdgRtWClL9wAo3igEt88k2IpcEctPcaMuS_TlAaP5jvw6_sxRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استوری حسین قهار خبرنگار حوزه پرسپولیس در مورد ایری و طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136873" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
گرا در بازی دوستانه غایب بوده و احتمالاً با نظر تارتار جدا میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136872" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdbcRqnjRcQzZOt9msEmpS6QE8vzwilgI0K0YyWpFEMBLBsSa6rd_4VMJVl9Xhdw4a8dU-JaS9AiYYJs79TVqodcLFa80kR3dE1xGiVVZIsBQh6UKbiJ0y2raP9tSzsXHMclDDKeFghDMQtbhZeh4Q7VwOWz28xSpr1MBI-NL4izetF5l5NbnE4Vrx2vkrmlca7pegZSdMw0nszZfnGEDsh8Qcok9YNHh07ezYFOhFDctd6ghx4nopQ-AWYS9GONh3EN_m4ZQsuUMlHMr-nKuxINvb4t-1Qwyn_KcrIZnJF0zuDNQArGEgEqfb_RanAm0sUVMvW80c-SHKIW5Ci1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
باگناما از گل گهر جدا شد، نیاد پرسپولیس صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136871" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=PME0yQ1kGnMHfrY10PYmk9a7pQzHw6vT76PHkAQ_L8_eXhPg4N8i85LcsoeoHA-2PRW_lG4_L2l_iVO89HzcVCNhqC_0vJ6fc5eyb90j7FVF22b63ZgspNOMz2-sZ9NE5adffMHllWGlx123xMR9Gq_hy-JLy20i1aCYW4yjYvJCRFOmPR_mUVs4wxSkOhK5VG43DYkIqqAoolj0d2nV7bHJr643THS9rRoKDIkU8o78OiM1yan-_fkGWCIOm05eFlCLEs2vY8p9_r6HMPyqfwDQ_NTmAWedTfSpbcN3P98wRcq4B3qdVlkudnSnf07AkIh0Tuk4IoIQYM7gzDO4jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=PME0yQ1kGnMHfrY10PYmk9a7pQzHw6vT76PHkAQ_L8_eXhPg4N8i85LcsoeoHA-2PRW_lG4_L2l_iVO89HzcVCNhqC_0vJ6fc5eyb90j7FVF22b63ZgspNOMz2-sZ9NE5adffMHllWGlx123xMR9Gq_hy-JLy20i1aCYW4yjYvJCRFOmPR_mUVs4wxSkOhK5VG43DYkIqqAoolj0d2nV7bHJr643THS9rRoKDIkU8o78OiM1yan-_fkGWCIOm05eFlCLEs2vY8p9_r6HMPyqfwDQ_NTmAWedTfSpbcN3P98wRcq4B3qdVlkudnSnf07AkIh0Tuk4IoIQYM7gzDO4jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136870" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136869" target="_blank">📅 23:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136868" target="_blank">📅 23:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahrooooookh Abbasi</strong></div>
<div class="tg-text">منطقیه این عدله و تفصیرتون کاملا
👍
ک پرسپولیس تو پست محمدقربانی الان بازیکن نیاز نداره،چون باکیچ،مملی و دوتا پوریا هامون ک تازه از گل گهر گرفتیم کافی هستن و بلاخره یجاهایی هم مربی این حقو داره ک با اون بازیکن هایی ک خودش میشناسه و خریده بازی کنه چون اینجور بازیکن هایی ک مورد علاقه سرمربي هستن و با نظر وتاکید خودش جذب میشن بخاطر اون رابطه ایی ک بینشونه یجورایی برای اون سرمربی جون میدن و تو زمین براش کم نمیزارن...ولی الان ک قربانی با این تفاصیل جذب نشد اینو هم باید بگیم ک تو پست ۱۰و پشت سر مهاجم حتما یکی مثل محبی،ترابی،هاشم نژادو...باید از نون شب واجب تر و جذب شه</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136867" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🔴
روزنامه گل چاپ فردا:
😀
مهدی طارمی بین لیگ برزیل یا پرسپولیس به زودی تصمیم گیری میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136866" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
‼️
شماره 8 مرتضی پورعلی گنجی رسماً به مهدی تیکدری رسید تا جدایی مدافع میانی قرمزها قطعی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136865" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
فارس: تارتار از عملکرد گرا و بیفوما تو تمرینات تیم راضیه و احتمالا این دو بازیکن فصل آینده تو پرسپولیس بمونن. ( شما بخون نتونستن یا اجازه ندادن این دوتا برن..)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136864" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
🏅
آقای هوادار ۸۰ درصد نفراتی که تو لیست اول تارتار بودن جذب شدن و تمام نفراتی که از گل گهر میخاست، لطفا از الان بهونه دست کادرفنی ندید، آقای تارتار طاهری رو نمیخاست و گفته بود حد المکان ایری رو جذب کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136863" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136862">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136862" target="_blank">📅 22:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
اعلام ساعت قرعه‌کشی لیگ برتر
🔴
🔴
مراسم قرعه کشی لیگ برتر جام خلیج فارس فصل ۱۴۰۵-۱۴۰۶ ساعت ۱۶ روز سه شنبه ۶ مرداد در سالن همایش های بین المللی هتل المپیک تهران و با حضور مدیران فدراسیون فوتبال، سازمان لیگ و نمایندگان ۱۸ باشگاه حاضر در این رقابت ها و اهالی…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136861" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein</strong></div>
<div class="tg-text">این نکته رو بگیم ک درویش با همین مدیر فاسد سر فخریان عجب دزدی کردن غیر عادل هیچ کسی حرف نزد</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136860" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
📌
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام عضو هئیت مدیره باشگاه پرسپولیس
⭕
باشگاه پرسپولیس برای جذب دانیال ایری و کسری طاهری به صورت رسمی از سازمان لیگ و فیفا استعلام گرفته تا در صورت نبود هرگونه مانع قانونی، قرارداد این دو بازیکن را نهایی…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136859" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136858" target="_blank">📅 22:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
فدراسیون فوتبال و شخص مهدی تاج به دنبال تمدید قرارداد بلندمدت با امیر قلعه‌نویی هستند! هیات رییسه با این تصمیم مخالف است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136856" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136853" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">➕
بعد پنج سال به این نتیجه رسیدم حداقل نصف هوادار هامون متعصب،ناآگاه،هیجانی،و تو دنیای موازی هستن و اغلب دنبال کری خوندن و دلقک بازی
➕
هیچ فهم و درکی از فوتبال حرفه ای ندارن و چشم گوششون به دهن چهارتا از خدا بی خبر بچه ساله که گوشی گرفتن دستشون میگن لنگش کنید، هوادار واقعی پرسپولیس رو سکوعه که لب دهن نیستن اونی که تو گرما و سرما از تیمش حمایت میکنه و بالا پایین این تیمو دیده و به مسائل اشراف کامل داره، یه عده فقط لب دهن مجازی هستن و ساخته شدن تو زمین رقبا بازی کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136851" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🫦
کونده رفته به ایجنت ایری و طاهری گفته به بازیکن هاتون بگید استوری بزارن… شما که پول نداشتید گوه خوردید این دوتا رو خریدید به امید اینکه این وسط یه پولی گیرتون بیاد ولی فعلا کیر خر دستتون داده بانک شهر… به قران خود بازیکن ها هم ذی نفع بودن وگرنه هیچ کصخولی…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136850" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136848" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136847" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136846" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akqy5OjnlTbegx7TIHIsNQ4OtYO2fuv34yPUyHHmrw0KF6BhHbn27XRDkLYhRlHoJB8-eKEF3joeDjzmOPZ4QKYSpNp3D5lb5ru3vPwQPnVm4grAinhwwFz-Rqw1nrI2fMhn1OcAYhtIstwoDVWBS8y97k0RZ0ejUSNYkGhG1icODmKXzn7SEbqXO83eOR_BtTm0pV-U9YoVDUnCpc2OsGnn_rTod9rbstRDjG3S70m4hKbAFbRnRQ8qhbhuAoGWQ38kJMuZ_rg6ackkajZ5-tdSUWqD2pPH5JzXkgGvN2uvOfU2KjT9AuCPZ16SoGkLaaYel-U-_Nme0m9fRdRcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری رومیخواهند یاکه خیر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136845" target="_blank">📅 21:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136844" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_rADIiAZ_BeE1CSo7Yp-F4Jk-Emym1c490X4BBnyDByjTbSgbfm9AJXNIDYL5nO13rEm5ePbHSP0AkslzkveWVWn5pqinknFjJE72GccEDg8qHCXPL-KhsmEXIsfZH-NG_WC0q2SGdeAS8c99mefISqXvddr6F7JJy5X8Jzx5sezki4Pg0UKUEm8nGkPPfJno6psUmvBW9eKhQ-XdAUT4RaRtl93Y6mrSMbneh7_dhHFht9ZlZdgQ4D8RgXPasVzLA1enWbNUXbg9FI9KmN_74QOdf09COSFidKwQDwIIeffy6K98bcDZz4Mgfb6Gf3tUIvapHN8dz4lsmWVuYK-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136843" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136842" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136841" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136840" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136839">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136839" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136837" target="_blank">📅 19:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎶
🎶
🎶
صادق محرمی طی روز های آینده از تراکتور تبریز به صورت رسمی جدا خواهد شد و احتمالا به پرسپولیس بازخواهد گشت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136835" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">همه چی رو کنار هم میزاری میبینی کسری طاهری و دانیال ایری و مدیرعامل نساجی و دلال این بازیکنا در کنار بنگاه دلالی ورزش سه دستشون تو یه کاسه هس و دارن آخرین زورشون رو میزنن برای تیغ زدن باشگاه صب ورزش سه خبر میده کنسل شدن الان بازیکنا خیلی یهویی با دستور دلال هایشان استوری مشترک میزارن هوادار هم که خدارو شکر سوار موج میشه</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136834" target="_blank">📅 18:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136833" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕
هرکسی از ننش قهر کرده گوشی دست گرفته کانال هواداری زده هر کصشری میخان میزنن، اون حروم زاده ها اگر میخاستم بیان پرسپولیس چرا رفتن نساجی؟! صدرصد هم خود بازیکن هم ایجنتشون با زندی بستن
‼️
یکم عقل تون به کار بندازید خداوکلی چرا هرکس هر کصشری میگه طوطی وار تکرار…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136832" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136831" target="_blank">📅 18:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136830" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyulbooOeQmQfzh1Jj8hR6KxondH7YRyXAkKQ4nhgXQ1dDsHUlkYytZxKWSov9RjkEDqKs1-J_AweHVb9bCWyxkg8hx9B4PhiCxaQJfp8Qwtwy0lSvRi4-blqg7p_O1a6a19cazoGzaEqHQW93JBAIZq2MEPS_1WHq-SF1Nn2X1gwNCkzwXKXjYPWOfJQmNh8-pU3Xe44ipt8cGu0b1ajRh_hkwIjKP96oqPiJFATyxN434hmpTUujtoiDKpdtIg0yOPaGZdje4r8XfCuVbHkNBhCpHyF0q6CaV4ymBMK9KAv_VVOHKCVj60RxYr69uTC_iUjdXmlsFbp2qZPkvH1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136829" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
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

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZih8NwZQ3Up0kSgyg2eCMeUPs7BfmMFuiYAIsIMz7NSEI_07eXHHGElWt9R99cCWvCt6tQ6rSuYQxWhvsNdRHLT3NES3OyZrQdqKJtlF-DC8j82jN9dawplk5rSTwLEyFK2D6zEr0HpbFUrv53U9eXkYSZhP9mfh8sgfqvmGB8_bx2IQp6QdEjFHqSXkApyAdjYaYGI4HLYWHTCcbFRnDC4LhZD07ja7hLdeLMJWluerdz7DqNZg24xDVulOch2BJTdRtywTn2zVwXj4fQT5XBJGMVS1En1bmdhERq-m0uvwR4DEfNRpdQ-E1DuR932398NFGIN14M3KR0CjhBqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
آغاز یک روز پرفشار و همراه با انگیزه سرخپوشان در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136826" target="_blank">📅 18:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔄
🔄
استوری مشترک کسری طاهری و دانیال ایری برای هواداران؛ ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136825" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136824" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136823" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136822" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚪️
⚪️
⚪️
انتقال کسری طاهری به پرسپولیس فعلاً نه قطعیه، نه منتفی. سرخ‌ها علاوه بر دردسرهای قانونی مربوط به قانون «پل»، بابت مصدومیت رباط صلیبی قبلی این بازیکن هم نگرانن. پرسپولیس تأکید کرده بیشتر از ۷۵۰ هزار دلار برای طاهری هزینه نمی‌کنه و تا وقتی از نظر حقوقی…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136821" target="_blank">📅 17:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136820" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
پرسپولیس و تراکتورسازی پشت پرده توافق کردن که پرسپولیس بیخیال قربانی بشه و تراکتور هم بیخیال محبی تا باشگاه های اماراتی بازار گرمی نکنن و مبلغ رضایت نامه رو نبرن بالا
😐
/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136819" target="_blank">📅 17:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136818" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
محمد قربانی: پرسپولیس و تراکتور مرا میخواهند/ مبلغ رضایتنامه‌ ام ۲۰۰ تا ۳۰۰ میلیارد است
🔴
🔴
بهتر بود نام تیم نیاورم، اما حالا که سئوال میکنید، میگویم. هم پرسپولیس و هم تراکتور با من و باشگاه الوحده مذاکره کرده‌ اند و در نهایت باید ببینیم ظرف روزهای آینده…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136817" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136816" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
