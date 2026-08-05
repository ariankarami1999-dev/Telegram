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
<img src="https://cdn4.telesco.pe/file/Ld5yOJa3tejneW6IZaC3-_A9lmwM09Udc1Fk3IzUxZOMXg_c0gBR4qf2DC2-1wo1kajZhDpTboOnJla1NW5K82A6KW9B15gQ2BszbeQYB2QTCNogwr1kVGjhDFASYEf_uYVoQg9zOERambTSIHoGmd1ihTD5C-WcbXljyWhxrgJE0La7WDSO-VthSekJKNM9I4-A1Kcbi-U_pGfVE5yw0oY9Ff5PdWlgyXLOGShUgW5Q5hWzFb14vYWRXfYJrCFDU12HHFDQrD9a0McG-0d16TvQKFlwWLYHcQ6Flx8zDzdzVqNJgtEfoz751FafbyY087ypwFhwdR8uiRlIrb-8tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 02:19:37</div>
<hr>

<div class="tg-post" id="msg-137423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=Hp9c8F-7krLWwwh7RFLwK6U815cYwjmk4H-3gVvIYWSwtTv-lzJ4jlOsHHDiI_TGxhqnYKyzESXlzWCSJrliMwL1yqL-sm8otxvQF8SSgyTem_9j0QQQdiU3Qie_i1RudE35yjY76HsPi9zn5EVznOHIr2k_3ThfLwswCNPV4g2GgAisxvfCNqm0QRNvTIX3K2rfbL39q966N2FX1-TF_i8dnWT-6RoyCWXyP5Bg1-KPuU3qSSR37AQYnkYXjA_z9eSRsbJk5R9XojaOhRU1fovejh2nEd3zdgRCfXBUuKPJjBmFb7kLH_xIw2kG3Sppk9a8fn36tmMadhx4vvYN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=Hp9c8F-7krLWwwh7RFLwK6U815cYwjmk4H-3gVvIYWSwtTv-lzJ4jlOsHHDiI_TGxhqnYKyzESXlzWCSJrliMwL1yqL-sm8otxvQF8SSgyTem_9j0QQQdiU3Qie_i1RudE35yjY76HsPi9zn5EVznOHIr2k_3ThfLwswCNPV4g2GgAisxvfCNqm0QRNvTIX3K2rfbL39q966N2FX1-TF_i8dnWT-6RoyCWXyP5Bg1-KPuU3qSSR37AQYnkYXjA_z9eSRsbJk5R9XojaOhRU1fovejh2nEd3zdgRCfXBUuKPJjBmFb7kLH_xIw2kG3Sppk9a8fn36tmMadhx4vvYN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
بونوس ویژه ۱۵ چرخش رایگان بازی Egypt Power x1000 با شانس جوایز میلیونی فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان ۱۰۰ هزار تومانی دریافت کنید.
📌
نکات مهم این بونوس:
👇
▪
︎ ۱۵ اسپین رایگان ۱۰۰ هزار تومانی
▪
︎ ارزش اسمی بونوس: ۱,۵۰۰,۰۰۰ تومان
▪
︎ مبلغ فوق تضمین‌شده نیست و میزان برد به نتیجه چرخش اسپین‌ها بستگی دارد.
▪
︎ پس از پایان اسپین‌ها، برد نهایی بی‌قید و شرط به موجودی حساب شما اضافه می‌شود.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔵
sportn5b2.com
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/137423" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/137422" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKPkt4mYCaGoHGWqtBawLxWjhBqhPr_RnLwbAUm77xTgo2h5EwcOGF9x28A9xizzgqHZuZBrdJuISFtz8jBV2CpIpFYvg7v8HDBLkWbKFP1_D2yPPBapzaZIwBVfO0t-aSxzWnIxAxzsSw65DBgIvSNrbnXKwH6PWXUKQRQTHIyo4whLdvvl7WY7qH4UQAWaC79WChbFZT5_VExHYUCYjcJ4dWBPu9-W2s2aVu2joEWVp4xxgjigSuSlE6lWUXu97js6IxtbsIQult3wq-vkFFAWKFCXiT8kJZs0p_rhs2VAKnKdX2bKlOysleKbX0enTux9ArDigfZrK5YdtNSWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیتر سوپر حق فرهیختگان چاپ فردا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/137421" target="_blank">📅 00:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/137420" target="_blank">📅 00:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5Tx3xujQpL1V4RJPNqc7ZbsydSYiH_g_O2HYYn44oryF44dzDFplnDooLT6_P0ppqbk69NnDT2IEP1SSTYfqGQNpuz76hi0_KzxOGzy-WZQyPlSWu54YWBtFwMYCCDVZA9ds0PIITZQ2Iv44sItxZ6PgWz8v1P5tnPryCQDP3Gbr8YjqSlENBYEjD4_e-JVhDNMf1GYuN-Gy1baXttEQWBqqfeKqHse9uUbNoFaku9O4heReWPtaogvPVg5bHVbqq3TNiAAhCzOQiKkqpBk31bjzAutPR9OcaND1jThZ9oOt92lxfmT8C7Ee6f2Iu_xvftbdaC_7sayPXghOPpHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/137419" target="_blank">📅 00:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
❌
پرسپولیسی‌ها ریختن زیر کانال تلگرامی باشگاه ماخاچ قلعه روسیه و ۱۳ هزارتا کامنت گذاشتن که آقا این محمدجواد حسین نژاد رو بدید ما ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/137418" target="_blank">📅 00:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/137417" target="_blank">📅 23:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/137416" target="_blank">📅 23:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/137415" target="_blank">📅 23:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
رقابت پرسپولیس و تراکتور بر سر جذب هافبک الوحده ادامه دارد.
❌
❌
به گزارش قرمزآنلاین، در خبرها آمده، باشگاه الوحده رضایت‌نامه محمد قربانی را ۸۰۰ دلار تعیین کرده اما تراکتورسازی حاضر است  ۶۰۰ هزار دلار بپردازد و اگر پرسپولیس با این رقم موافقت کند الوحده مجوز…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/137414" target="_blank">📅 23:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
🔹
🔹
با اعلام رسمی باشگاه استقلال، پنجره این تیم بسته باقی ماند
😀
‼️
پ.ن این همه هزینه کردن وکیل گرفتن
🙃
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/137413" target="_blank">📅 23:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🗣
🗣
🗣
‏  پنجره استقلال همچنان بسته است/ خریدهای جدید در خطر از دست دادن فصل  ‏
✅
در حالی که طی روزهای اخیر در فضای مجازی عنوان شده بود پنجره نقل‌وانتقالاتی باشگاه استقلال روز سه‌شنبه ۱۳ مرداد باز خواهد شد، این اتفاق رخ نداد و آبی‌پوشان پایتخت همچنان با مشکل بسته…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/137412" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
فوری؛ معاونت ورزشی منحل شد!
🔴
باشگاه پرسپولیس در بیانیه‌ای رسمی اعلام کرد معاونت ورزشی منحل شد و ۳ مدیریت جدید جایگزین آن شد:
مدیریت آکادمی
مدیریت تیم بزرگسالان
مدیریت تیم‌های بانوان
🔴
پ. ن؛ البته در بیانیه باشگاه قید شده این تصمیم هیئت مدیره با قید «تا اطلاع ثانوی» هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/137411" target="_blank">📅 23:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK4EmgkBE8VbvrbQxhZy6DA2wpA_8RSGxc_T3cf4fCXHSjq0EFDTnR-9Dcy49hwN1T5UuUUhjich9dTY-Jc3UzY8JzB3kSBosjGILJhkk_08cibfu7nqovM7v_aWhWwHbSwlb_2NciubYQqSnHAur4otSjvX3i2J3mwTNAeDbF6pCwDK-A_P81sYOoFqZ2L1gz8GzGAxwTDzcWFbpvgNJJ6uS0KWgWVnUU5cI5d-HUkjXv6eAbzJ0jB-AV-ZV1Crcnbuk4RRbZgHqrAH1A6dtfVgiEaBmWBBw6zeb3Qzce5py_m-1CxzqZLjGCmpSthMnhnOtwvnOW2ps1GgbUVaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
خط حمله فصل بعد گلگهر
.
👀
👀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/137410" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjbrO8AQXJECVFZG6oybTDDLwYjr-EP7pEih16Fel0ytKhRZSzHz-E_AmUN9skMDPc9soMuMp8dq2_v49W0TGXIraCfPjVE3rciX2K0X5p97jA34FeoqQyW7Ls45SnowYYDSRaOsxvBgNmvLa7wGIiU6GdrZRRO94Pi1QqfNIPUUaS_6z5ux6G4cjxz5V8UN2LWOVbxyJQQ3e4dLNNq5gAFboYKvsmPxpGw-ZyREkRZUl70meJrXwc3yt7rdgTnLEgS0LAuNnyHRPNKSC7wa7XtCk7TZ-DFBq9dviUIgY6U79WsxPEl08NSzI8tN3vbWSZTICrB_kQ2RDzwROj8aQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عضو هیئت‌رئیسه فدراسیون در پرسپولیس پست گرفت
🗣
با اعلام باشگاه پرسپولیس، محمدرحمان سالاری، عضو هیئت‌رئیسه فدراسیون به‌عنوان مشاور حدادی، مدیرعامل سرخپوشان منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/137409" target="_blank">📅 23:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
قدوسی: رامین تمایل داره به پرسپولیس برگرده و از قطر هم پیشنهاد داره و تکلیفش تا روز های آینده مشخص میشه.
❌
❌
اول نیاز به تأیید تارتار هستش ؛ بعد از اون بحث مبلغ قرارداد و پرسپولیس بیشتر از سقف خودش به هیچ کسی پول نمیده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/137408" target="_blank">📅 22:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری از ورزش سه
🚨
جدایی دنیل گرا از پرسپولیس قطعی شد و مدافع مجارستانی از پرسپولیس جدا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137407" target="_blank">📅 22:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
تعداد کامنت های پست آخر پیج پرسپولیس به بیش از 130 هزار رسیده است
✈️
✈️
هشتگ های هواداران به جذب بازیکنانی مانند قربانی، ایری و حسین نژاد اختصاص یافته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/137406" target="_blank">📅 21:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
❗️
❗️
سه پیراهن ماندگار همچنان بدون صاحب
🔴
🔴
در فهرست جدید پرسپولیس، سه پیراهن مهم هنوز به هیچ بازیکنی اختصاص پیدا نکرده است
🔴
🔴
شماره ۲ که سال‌ها بر تن امید عالیشاه بود، فعلاً خالی مانده و باشگاه هنوز جانشینی برای آن معرفی نکرده است. شماره ۱۰ نیز همچنان بدون…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/137405" target="_blank">📅 21:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی، قرمزآنلاین:
🚨
پرسپولیس و تراکتورسازی حاضر به پرداخت ۶۰۰ هزار دلار به الوحده امارات برای محمد قربانی هستند
❌
و این به تصمیم خود بازیکن مربوط که به کدوم تیم جواب مثبت بده ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/137404" target="_blank">📅 21:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💢
💢
💢
💢
💢
#غیرـرسمی
🔴
🔴
توافقات انجام شد؛ ایری یک قدم تا پرسپولیسی شدن.
❗
❗
❗
توافقات با باشگاه نساجی انجام شد. باشگاه تا نیم فصل تمامی رفت امد هاش با شرکت هواپیمایی وارش انجام می ده. و نیم فصل قرار شده بند خرید دائمی ایری فعال بشه.
💢
💢
تنها یک گام مونده نهایی بشه،…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137403" target="_blank">📅 21:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
قدوسی
🚨
از داخل باشگاه خبر رسیده که به جذب محمد قربانی بسیار امیدوار هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/137402" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137401">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=IgDimF36rVw8fkqC3FrpNnqB_KHTfXInX8Nnscj8YAqKygCIxQLvCo2jW7USAv3q74s72hCxs_qsLmtHaemBqTOGGx2VpAuShMemuPGvngEo3aKbIlAxOSkOpa6oOhjJ28M9eCRIdz9xNzoXmhiI8hS_3r-RRMTZIaUyG1u7hEihAAzMDxR1z-poCQGENjVTNLdIIdQeP1KjpTSE6MVSuuzDfFf6mN22RyK8hXuAlZudlRvn7vMC99GN6Uk_D6aFXygJygvSENqAqjrqCX1zcngqpcEDKHxXPs0JLv33txpCILAAavgYlOHuHrNxuEJpk5OtM51_jXxh4t_XKQ3CKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=IgDimF36rVw8fkqC3FrpNnqB_KHTfXInX8Nnscj8YAqKygCIxQLvCo2jW7USAv3q74s72hCxs_qsLmtHaemBqTOGGx2VpAuShMemuPGvngEo3aKbIlAxOSkOpa6oOhjJ28M9eCRIdz9xNzoXmhiI8hS_3r-RRMTZIaUyG1u7hEihAAzMDxR1z-poCQGENjVTNLdIIdQeP1KjpTSE6MVSuuzDfFf6mN22RyK8hXuAlZudlRvn7vMC99GN6Uk_D6aFXygJygvSENqAqjrqCX1zcngqpcEDKHxXPs0JLv33txpCILAAavgYlOHuHrNxuEJpk5OtM51_jXxh4t_XKQ3CKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137401" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137400">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
در صورتی که فولاد برای جدایی ابوالفضل رزاق پور کوتاه نیاد ممکنه باشگاه تا نیم فصل قید جذب مدافع چپ رو بزنه و با همایی فر و جلالی ادامه بده و بره جلو
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137400" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137399" target="_blank">📅 19:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
العربی کویت قید بازی دوستانه با پرسپولیس را زد و از این دیدار انصراف داد. این تیم گفته به خاطر شرایط منطقه و دردسرهایی که ممکن است در کشورشان برایشان پیش بیاید، نمی‌تواند مقابل پرسپولیس بازی کند و بابت لغو مسابقه هم از باشگاه پرسپولیس عذرخواهی کرده…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137398" target="_blank">📅 18:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137397">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⏳
⏳
⏳
⏳
روزنامه‌ همشهری هم نوشته پرسپولیس شانس خوبی برای جذب محمد قربانی داره و مذاکرات برای مبلغ رضایت‌ نامه ادامه داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137397" target="_blank">📅 18:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
قدوسی: رامین تمایل داره به پرسپولیس برگرده و از قطر هم پیشنهاد داره و تکلیفش تا روز های آینده مشخص میشه.
❌
❌
اول نیاز به تأیید تارتار هستش ؛ بعد از اون بحث مبلغ قرارداد و پرسپولیس بیشتر از سقف خودش به هیچ کسی پول نمیده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137396" target="_blank">📅 18:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1xIpEpdZU7uDlKhgyzWDVjQgHV1MFDiIaifVKovkRhufiYXeZyLYo4rtKGfpCUhtWdmre4WDgqY_ao_XW3b7q0Q8lkArIH079Pez0rBrafz1f6ea0uI6KTbo3Nn3Tx5urO5V8t6vyH-pD61BWdJcu5CvhVCbiABAQSjBWxGRPvgvpfXgL8A_0ryLwPf79oqW-PJ7oqmoc4l4SU3TN7H6cBXHont0VBN5r1C3hN2J37tLBSKmwPPmLFO4EzpOX4hMRAJHgotCzhe-C_mcFwe3pKgl3fp-Jcqukwt_HfUw5sw2NBFNz_NSn_5ZuEcbyaVGvlZVmpzZReNeJtJlUUgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حاشیه جدید برای سرمربی زنان پرسپولیس
❌
باشگاه ایستا البرز مدعی شده نیلوفر اردلان با این تیم قرارداد سه‌ساله داشته و فسخ یک‌طرفه قراردادش قانونی نبوده است.
این موضوع در حالی مطرح شده که اردلان چند روز پیش به‌عنوان سرمربی تیم فوتبال بانوان پرسپولیس معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137395" target="_blank">📅 18:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
ورزش 3: تارتار گفته پول رامین 36 ساله و بدید ایری و قربانی جوان و جذب کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137393" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4uBOu5xgRyTT7NekMW5PhBbj9S07O_2FCo_FSo2N5FVKY_oN2fmrFr1FgXJF4v-V4NEdD0wM0jvdn2_jDC5h5nhT3DbT-d8gCwvK30TURcMtouoRkeaGxXOPKJ-1TToeF0i97VmWrSDdan5WlVayPVnpTFxRkrZzl_xXzaQIzp8NehR4CO8BC8AccIq6N1pKhkCdAYw9LYaSwmlkmmwVYft74ukcI4SLKfcH0HH2KLitj1-5c_rth_zgtjfFgnrvQ_sYnN1y7nE4TbXjYJZ0yOhH7RWF9zGzxwgeXFVw7uxATbE78LvIp-u9Jm1RzcY41zcMl-KO14YV4KNE36d5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137392" target="_blank">📅 18:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
قرمزآنلاین: دانیال ایری، رزاق‌پور و محمد قربانی سه خرید پایانی پرسپولیس
🚨
🚨
باشگاه همچنان برای جذب ایری و رزاق‌پور تلاش می‌کند، هرچند فولاد فعلاً با جدایی رزاق‌پور مخالفت کرده است. همچنین با درخواست دوباره تارتار، مذاکرات برای جذب محمد قربانی پس از کاهش…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137391" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
فوووری؛ باشگاه فجر سپاسی شیراز بازی مقابل پرسپولیس در ۱۶ مرداد انصراف داد.
❌
❌
احتمالا نساجی جایگزین این تیم برای بازی دوستانه ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137390" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137389">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137389" target="_blank">📅 16:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137388">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddNaTLfplu-1LssXOlTHTZfdIZrgMHXWkmiXh9xh1L6oQ19VS79zDquP2-YGd1AEA1Rk88gsin_M3Yv-8jPw-oPduonS88ddRk_Jh7uDswDrac9mNpYMXn_SBtip66gmIrsEB_kWnxAyYbICG4HeOrMyaY8xdU1nQhCAJKrbTci54LF3CMBgneucHIFnwRKbwWIykJieUTJUaFHLs_IZcDgNOdhmsldCNK9iRLZd4CP0ibl0L8-wTOBB3Xpn66UujxyLE1sHV2VtKvJXDmik1sHW-bRyGXuRSdceo9jbZAHo3pREg8TekvKdA-MC12RPCEkz-zy3QI9AWWa1mbUr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137388" target="_blank">📅 15:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137387">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137387" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137386">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏳
⏳
با پایان اردوی ۱۲ روزه تیم فوتبال پرسپولیس در ترکیه، بازیکنان این تیم امروز طبق برنامه در مرکز پزشکی ایفمارک حاضر می‌شوند تا تست‌های پزشکی پیش از آغاز رقابت‌های فصل جدید لیگ برتر را پشت سر بگذارند.
⏳
⏳
بازیکنان خارجی پرسپولیس هم که مرخصی 2 روزه داشتن امروز…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137386" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137385">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚡️
⚡️
مهدی تاج، رئیس فدراسیون فوتبال: تلاش‌ می‌کنیم تا فصل آینده بازی‌ها با تماشاگر برگزار شود/ تمام بازی‌های لیگ با VAR برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137385" target="_blank">📅 14:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137384">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137384" target="_blank">📅 14:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⬇
⬇
⬇
با‌ارزش ترین تیم‌های ایرانی:  • پرسپولیس: ۱۶.۵۰ میلیون یورو • تراکتور: ۱۴.۳۰ میلیون یورو • استقلال: ۱۴ میلیون یورو • سپاهان: ۱۲.۸۵ میلیون یورو  • نساجی: ۷.۶۳ میلیون یورو •  خیبر: ۶.۳۰ میلیون یورو • گل‌گهر: ۵.۹۳ میلیون یورو • فولاد: ۵.۸۸ میلیون یورو • …</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137383" target="_blank">📅 14:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137382">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137382" target="_blank">📅 14:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
شاهرخ بیانی: رضاییان با پنجره بسته کلاس گذاشت.
🔹
قرارداد رضاییان با استقلال 100 میلیارد تومان بسته شده بود و بعد درخواست 200 میلیارد کرد. مگر فوتبال ایران چقدر می‌ارزد که به بازیکن 200 میلیارد تومان بدهند؟ اگر به بازیکنی چنین پولی بدهند، تیم بهم می‌ریزد.…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137381" target="_blank">📅 14:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137380">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b74c6288d.mp4?token=JSqO0oROLRYLRCmCYiz-SVLYQ9gDIy3YsTatPyTyzlyQPxCw5Zdp1cYn3PlLm9uQ81oBcaSWGsNvmYK7vnqhPaAbGmykQbfLwKs7V4mkXlDTQp5a0Os_PmZWrd38B4AfMTj8_HqRa6-YjSk-EeoRYZTfHNJevAWWoAOUNiqbLxGQvY3Gvv_VU-P5kpXfCvhwVL7rFw1zNUEeDa8fKuPesi0kEVTnaoQcVQ2F6NETMkAUgO98IzvLxdZdcEMd29tn__WPVaS8PN0AcYWCvh3zevPYuDqr5V9ltfBCs_hj8XB-su0TktzhvPIoiJRU7k8Lp5iB5G62zLeulAxxdej3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b74c6288d.mp4?token=JSqO0oROLRYLRCmCYiz-SVLYQ9gDIy3YsTatPyTyzlyQPxCw5Zdp1cYn3PlLm9uQ81oBcaSWGsNvmYK7vnqhPaAbGmykQbfLwKs7V4mkXlDTQp5a0Os_PmZWrd38B4AfMTj8_HqRa6-YjSk-EeoRYZTfHNJevAWWoAOUNiqbLxGQvY3Gvv_VU-P5kpXfCvhwVL7rFw1zNUEeDa8fKuPesi0kEVTnaoQcVQ2F6NETMkAUgO98IzvLxdZdcEMd29tn__WPVaS8PN0AcYWCvh3zevPYuDqr5V9ltfBCs_hj8XB-su0TktzhvPIoiJRU7k8Lp5iB5G62zLeulAxxdej3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗞
🇮🇷
🤍
فوتبالی: قرارداد امیر قلعه‌نویی با تیم ملی به زودی و بعد جلسه هفته آینده تمدید میشه تنها شرطی که داره اینه باید ژنرال تو جلسه قول بده که در جام ملتهای آسیا ایران رو فینالیست کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137380" target="_blank">📅 13:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT_ZBdn0K3Qc9YeCk7_Dp8G9luBjJ3_GqUJjEo8pynjzc091nvIhvF3Zabi_YBAEJZzu9AR2MxFHi06Gjy4lJMKrlddfC0zVyDRNbQrgMNeuORq7n8GbbsqbMkHpvwn0AhBAnuyIaNPE3YPawRqdyVsyikS_y3qslmHzqq5wZdez8fbjyVQWVBGpi_4l7nfpNsCushd34eimeVwqcl6NYKeRjo_f6nKjfXpFmVVAGjYZZwei2a24SWQXt8ox2hZj79rchwuF4-sUncrrHMQzxqWZworck96BiqFVnVqmg6fhwOdeBUp7QEw175-BFRpFGgZGUt0Mw43rd8mAA6CIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
🏅
مقایسه ارزش مهاجمان تیمهای پرسپولیس، استقلال و تراکتور؛
💵
پرسپولیس: علیپور 1.7 - سرگیف 1.2
💵
استقلال: سحرخیزان 900 - آزادی 300
💵
تراکتور: حسین‌زاده 2.2 - مغانلو 800
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/137379" target="_blank">📅 13:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
یحیی گلمحمدی با حضور در تمرینات دهوک عراق به شایعات حضورش در پرسپولیس پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137378" target="_blank">📅 13:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHoN9HXV6sctdN8lvk_dk0Iwktbn1XRSaz5P83Vx5ixfxqlW5NMmJi-40pNp-QBPs8k0PWYZoaJK0tiaACYOQzQiTWxxKEmX-NztVSjtcCbAKEg4lW6LjinJUStpbzxm7Q5O9EJTl9BfjJqjP1EP5zwIcR1MqUSo8xQnOaj3U0DZhLVYRJdOIjYDEWcW0IqaZf3ccQhOidy3nsQj_2ZFKZqtAt-7gKM_Dye0cqB9GKpIn6V8BjYVsR4a2BCSWXgfgS3MJyAxCxufYOWCZ5oYF9j_DM6GH74g862TlA2VLQ01bUpjvEUMsyopkIEDZmUGagRl2RGgtIkmg1Np1WSN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اعضای تیم پرسپولیس با حضور در ایفمارک تست های پزشکی را انجام دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137377" target="_blank">📅 13:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
شاهرخ بیانی: رضاییان با پنجره بسته کلاس گذاشت.
🔹
قرارداد رضاییان با استقلال 100 میلیارد تومان بسته شده بود و بعد درخواست 200 میلیارد کرد. مگر فوتبال ایران چقدر می‌ارزد که به بازیکن 200 میلیارد تومان بدهند؟ اگر به بازیکنی چنین پولی بدهند، تیم بهم می‌ریزد. بازیکنی در سطح رضاییان 20 میلیارد بگیرد، کل تیم بهم می‌ریزد. قرارداد رضاییان به اندازه کافی بالاست، حالا برای استقلال ناز می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/137376" target="_blank">📅 13:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
منهای ورزش
❌
بعد از هشت ماه نرفتن بچه ها به مدرسه
❌
فوری : مدارس امسال از مهر باز نمیشن!
❌
+ عمران عباسی، عضو کمیسیون آموزش مجلس:
❌
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
❌
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/137375" target="_blank">📅 13:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4HIfn763k8Q85W5ZtVXOKa8C25S2L8gDj3FyXAQysDhXL5gNDuqpBgO79IiMvVsIabuoRMbumy_yZxj_SwIEvPAOvfZy7lb_405dUHZ50m2SpyMGR9A0qE2QZYNhKBtc-XiXfSGCUl40nPOkkvSA_HvViK7Oa4AeSBbn2If7gf8Nb7pr_U4GtLbdG00h4u9TxckgKaw5_iKXtus3qpfmsmvw1svE7ShmG0gUHxvcno2H18A_kHnE-_-hPcVfBGf4ymGnnNaat2bTSUDd1p1lN3g2UUUffrSM_MC5r1--uuMQuavCnqZgNotr0Fmp0NEY1QbHUx2Ztd3SdQ-QxvDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
با اعلام باشگاه استقلال؛ رامین رضاییان رسما جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137374" target="_blank">📅 12:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
❌
رامین رضاییان به باشگاه پیغام داده دوس دارم برگردم./سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137372" target="_blank">📅 12:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه خانه‌ای که در اختیار بیفوما و گرا قرار داده بود را از آن‌ها پس گرفت و این دو بازیکن را به هتل فرستاد؛
🔻
اقدامی که گفته می‌شود با این هدف انجام شده تا شاید آن‌ها ناراضی شوند، قراردادشان را فسخ کنند و از تیم جدا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137371" target="_blank">📅 11:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137370" target="_blank">📅 11:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137369" target="_blank">📅 11:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه خانه‌ای که در اختیار بیفوما و گرا قرار داده بود را از آن‌ها پس گرفت و این دو بازیکن را به هتل فرستاد؛
🔻
اقدامی که گفته می‌شود با این هدف انجام شده تا شاید آن‌ها ناراضی شوند، قراردادشان را فسخ کنند و از تیم جدا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137368" target="_blank">📅 10:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
رامین رضاییان با انتشار یک استوری تلویحا جدایی شو از استقلال اعلام کرد
🔹
نکته جالب اینه که خیلی کلی و راجب همه تیمایی که توش بوده حرف زده و اشاره به هوادارای یه تیم نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137367" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137366" target="_blank">📅 10:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✨
✨
✨
پیمان حدادی:
🔴
🔴
همه امید داریم که امسال بتونیم جبران مافات کنیم. در حال حاضر تنها تیمی هستیم خارج از ایران اردو برگزار کردیم. سعی داشتیم بهترین امکانات و بهترین بازیکنان را به تیم اضافه کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137365" target="_blank">📅 10:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⏳
⏳
مهلت ۴۸ ساعته ادعایی ترامپ که برای تعویق حمله به ایران گذاشته شده بود ساعت ۳ بامداد امشب به وقت تهران به پایان می‌رسه و فعلا نه خبری از توافق قطعی منتشر شده و نه خبری از تمدید مهلت تعیین شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137364" target="_blank">📅 09:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
رامین با آسانی هم به مشکل خورد
⚡️
رامین رضاییان و یاسر آسانی یکدیگر را در اینستاگرام آنفالو کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137363" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0xmjuG7MstFl4njl8J22yHdhZwPebTSXJPwykNbiOM9VdVmneZeoaSusS0C0CSZI2n3kBUVwACrDPL6DwjOoJrC_sab2v3GpGIyrX14P5XAUdfizojE_z5lxuNuIenyzBk8_uryOvLYo9XhZLnhsDV8qGx6MG_cCj4z6LRkZUoCpL_sg8MF-FD8fP_itfJJaedmcXO3a0YSkOZAqnbsJHf-oi7iJUnudgVWiPzbCnxOboIc9nLpXZoGno8dUculBRAFJC99eft-BZi7ONy93Zz5dlPtn714ubacsZ_QKkF-95-5mKhGp0zeLcRM_iOWMLBdanZo5R4KVkDbCpeuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین با آسانی هم به مشکل خورد
⚡️
رامین رضاییان و یاسر آسانی یکدیگر را در اینستاگرام آنفالو کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137362" target="_blank">📅 09:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137361" target="_blank">📅 09:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhiA-n_IhQI3rTwxzVidsFzv5he2dB8JbT6_E_5wITuFZj5zCS4kU_QOisMo2VoTxqfWQ2gp2vMuoNO2tAAKzgY9HkUs_MiKAomEXrFyuaplR7DUORP_pDl9TUWcj8Brg701NKMW2-YWo_eqI3WsSWO8HhfYrhkJTOGcs_dcTAz-J6O6XI-cANM8nyPa8clHFMcMekAFbAJ25zknKGv8YVxNCx3bbIhWa1iF6qowVXPNSwTb8dJCIAxocK1-vkTgSNJvXCtuzmSWUjEFgH_neUTE_iCgv2c2sZKnRd1QAg6Q4R5A6vBno3CAWSH6AKjtwdcOgjvWod8yKbI6usyvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137360" target="_blank">📅 09:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=KXRtQB30MO_JoN-QFXiQxuG4LA92dQ8crpl2NLqISQeeTVH2XrdNG57ISHHzIA9RONYAJNL6hlwiwZS7Y6Gf9QjeAbDYAFka7aL-9jlJrl2Cjbfna_5GwojUqZmmViqs3sQqs3p8stRDVUSFgysy_QaZQ1ZWn-fjN0Wlxt2shzxvvLwDPEg7iWgrKzbP6lrlu-dUpUI0i4E7dXdb9bT14WSia-h09YyTxAKJkXL6EH6KuapNHvabuUqTgurWOMNakhZ1BlsNNjCyheyQTUrfJf9TfuIOIi3LlkhfnQWFC6LejvZrQeYyLw4vapHDNkJZLrPghozD4VNIeVcfUbI5Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=KXRtQB30MO_JoN-QFXiQxuG4LA92dQ8crpl2NLqISQeeTVH2XrdNG57ISHHzIA9RONYAJNL6hlwiwZS7Y6Gf9QjeAbDYAFka7aL-9jlJrl2Cjbfna_5GwojUqZmmViqs3sQqs3p8stRDVUSFgysy_QaZQ1ZWn-fjN0Wlxt2shzxvvLwDPEg7iWgrKzbP6lrlu-dUpUI0i4E7dXdb9bT14WSia-h09YyTxAKJkXL6EH6KuapNHvabuUqTgurWOMNakhZ1BlsNNjCyheyQTUrfJf9TfuIOIi3LlkhfnQWFC6LejvZrQeYyLw4vapHDNkJZLrPghozD4VNIeVcfUbI5Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137359" target="_blank">📅 01:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnqReW5xB26zlIUuVV_1gsnjho72G7Ge1WjLdikNR2lZ7ObJJ8o2lJ76TDoOKb3DpjFC5POLyXqKJ96aOb_fTfgK5SZeBN9S7AEj0WftCcewHtEhu7auImSirMOonzG2eBtwPdmbTpeyAgVTV1fJIkdAlIBkCcss12zmS8xTOixuMarb8Gb7OWvOiLN1zWF1r48N0Rz4loFOXWvwS9jyEO3d8ss5cTIUqyaX94pFgcOqq8SgE1WtngUQ0YyGfyMra1DQEXfR0iLtUxcYOBXu2Vc21sOLlUh3ky7kMMKeRIq36xdn2zXdODLkDmrZVW4hrJea2l4PJg3hIBfMmdZpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
هفته‌اول لیگ‌برتر خلیج فارس
✅
🔴
پرسپولیس
🆚
شمس‌آذر
🔴
🗓
تاریخ شنبه 24 مرداد
⏰
ساعت 19:30
🏟
میزبان ورزشگاه سردار آزادگان قروین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137358" target="_blank">📅 01:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW6cfzSSar82zTxkP3md58QcyfID9zn8at2fFd_ioqA4WzpdGBVUi9MzjmKt2_w_oai92Q9m0YZ0gbXwpon3MK5SLw1L97r3zjWkX4uZBOyEo2dqGAFsxJrmXbE7fbBdEAqRdSoCJXH5wjRFjtOvPFXjBXmtUVwPomqRo8pYJdA6Scu0udkcbSkI3PctanZabOhX7Te8kvNCXr8e7MLRoRgkboXCGDankVXjgKqhF2og6FBJ1Vbvt51OAWZrGBx_cdog-EbezvrdTnX6YkkxAALv6mpa8fwi8fkc7w8Eu1LZ8M1e4oSywvLfFIG9oTq1ZQLg2q6pyB-U83GwvBoIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت انگشتهای عجیب دیدا در مراسم تشییع بارزی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137357" target="_blank">📅 01:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔸
رویترز : فقط چند ساعت از فرصت ترامپ به ایران برای باز‌ کردن تنگه هرمز باقی مونده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137356" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137355" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏳
⏳
⏳
⏳
روزنامه‌ همشهری هم نوشته پرسپولیس شانس خوبی برای جذب محمد قربانی داره و مذاکرات برای مبلغ رضایت‌ نامه ادامه داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137354" target="_blank">📅 00:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
رقم شوکه‌کننده و عجیبی که فولادی‌ها روی هدف پرسپولیس گذاشتند!
❌
بازار نقل و انتقالات تابستانی برای ارتش سرخ با ارقام فضایی به بن‌بست رسیده است. بر اساس آخرین شنیده‌ها، قیمت درخواستی برای رضایت‌نامه ابوالفضل رزاق‌پور از مرز ۲۰۰ میلیارد تومان عبور کرده که…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137353" target="_blank">📅 00:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
❌
ترامپ: در حال حاضر درباره بازگشایی کامل تنگه هرمز تا فردا با ایران صحبت می‌کنیم. این آخرین فرصت ایران برای دستیابی به توافقی خوب است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137352" target="_blank">📅 00:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
در حال حاضر مذاکرات برای جذب قربانی جدی‌تر است و با کاهش مبلغ رضایت‌نامه‌اش، شانس انتقالش بیشتر شده. درباره حسین‌نژاد هم فعلاً مذاکره رسمی تأیید نشده و پرسپولیس فقط شرایط او را بررسی کرده است.
🚨
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137351" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
محمد قربانی به مدیران الوحده اعلام کرده است بین تیم های خواهانش اولویتش پرسپولیس است و میخواهد راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137350" target="_blank">📅 00:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
فووووووووووری
🚨
مهدی تارتار ظهر امروز جلسه ای با پیمان حدادی برگزار کرد و نام دنیل گرا و تیوی بیفوما را در لیست مازاد پرسپولیس قرار داد
🚨
قرار است مدیران باشگاه برای فسخ توافقی این دو بازیکن اقدام کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137349" target="_blank">📅 00:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJiC9ejdgqXontVCl1na2OLmJO21YOcs7T7rNHOtq06Eu0wwqZVc8wNsO55pN2aQq702Sx91tEZn-NA9Y4w85Q30pil6ju3520BGp4RQ_sdZ1gxJQ150zzC0EB2H-grx0xQ22izl1sXcPq3iRHT9CsyptNQKmxWj5mMYXhZug2Oh4YMx86ScEj2dWnO_7Wiz-5BqBWe5vl59c_gfTp3BuvMJDwo4nPMnFy-CvFV4Hp5iGsHeEhYSeaguQbUlE2QSJfXvlgCmHndCb-9O9JfkxwmEZi8s5nOWT5BCh-lS8DbItbKMLQRDk8YyDNziqsCvMnQkk8THcsO-40anOe20oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
💣
🇹🇷
یاغیز سابونچوغلو: ترابزون اسپور ترکیه با صلاح با قرادادی 2 ساله به توافق رسید
😕
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137348" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
دو آفر باشگاه الوحده برای دریافت رضایت نامه محمد قربانی
🚨
پرداخت 700 هزار دلار  دو قسط 350 هزار دلاری طی دو ماه
🚨
تخفیف برای پرداخت نقد  600 هزار دلار
🔹
مبلغ رضایت نامه اولیه 2 میلیون دلار اعلام شده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137347" target="_blank">📅 00:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
همشهری آنلاین:
🚨
مذاکرات پرسپولیس با الوحده برای جذب محمد قربانی و پرداخت مبلغ رضایت‌نامه این بازیکن ادامه داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137346" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137345" target="_blank">📅 23:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3bf0fnQh5BRnYbCRGMzLG9R3wyV8UholiCSTt1m4BrmGa2ONg0lnfvfSqexIlYFXs_o12vHqF0B0VOxlNArddwEpfVvLPwSVhbXD77UF3OReomLHHmGIaJglyIghjtCzK0uH5Ribrzgp_phdoJ1LLX01SkByOQwSaXX_02xBZkJTkfcXnbcyCfz2rM95zImYqS5cJQO8peBWgtEROhAf2YdLLdns4C8RqfU-wusaaXzXzWejzfRMXlro-WQtlomMqvhwGjb-aQf065LnJC4zlef4EBx977b7qWfLxc7A9Dkr7Sxs7QRx5Wngep93-kHoG500BQHRKTDCB7395WH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137344" target="_blank">📅 22:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137343" target="_blank">📅 22:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137342" target="_blank">📅 22:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌ فصل‌ جدید تکمیل شود. در پست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/137341" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
✔️
محمد جواد حسین نژاد امروز هم تو بازی تیمش بازی نکرد و نیمکت نشین بود
🔴
گفته میشه حسین نژاد دیگه تو دینامو نمیمونه و قطعا در این پنجره از این تیم جدا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137340" target="_blank">📅 22:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
رضایتنامه حسین نژاد از 6 میلیون یورو به 1 میلیون و 500 هزار یورو کاهش پیدا کرده، حسین‌نژاد جز استقلال و پرسپولیس از ریو آوه پرتغال هم پیشنهاد جدی دارد‌ ولی اطرافیان حسین‌نژاد می‌گویند اولویت  وی همچنان ادامه مسیر در فوتبال اروپا میباشد
✍
ورزش سه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137339" target="_blank">📅 21:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137338" target="_blank">📅 20:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚫️
⚫️
⚫️
سرمربی باشگاه پرسپولیس به الن هالیلوویچ هافبک کروات پاسخ منفی داد و حضور وی منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137337" target="_blank">📅 20:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
فوری از ورزش‌سه:
⬆
مذاکرات مخفیانه استقلال با رامین به نتیجه رسید و در صورت حل آخرین جزئیات مورد اختلاف رامین به استقلال برمیگرده و در ایران میمونه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137336" target="_blank">📅 20:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyQZSjM3NPJDYPVbo8kARTTW5cUYu4zWHV6IvK78PJbZyVVQTp_Vkb3slTzKG5eC9Q5ukG3oIAthOReSnRr6bzlEZIGArJuQhrY5bPfanBnLrpmTzuc9lNvaj-8cOY2ziH9PFnwP5aTnp_pjbj7YdgOxMT9za7bimaTavGWG-FGOxIGse-wgsDrODxofIZbPaMNeRsfoBG_3U0NSaKjIFGBx67jwFhy_ZHt2SMLQCrn2XqBocFnQlWFA0vOe7o3Xebu0FFqRdmUhCE2HVj5VVYzl6BZhp38aW0Ul25QNxUVme4c1pK8dqTFgQxStOsCKoBIYurRcNGjJl9udM3KAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137335" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137334">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
فوووری؛ باشگاه فجر سپاسی شیراز بازی مقابل پرسپولیس در ۱۶ مرداد انصراف داد.
❌
❌
احتمالا نساجی جایگزین این تیم برای بازی دوستانه ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137334" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137333">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXzChnLJUPpQS2V_OXtXpoavGvWhVKDIMFEGAgyizPyWsifUbXJudqeWFgwDNsBWP8Hnd7w0Qe1RWA8hfcjKxdg4_EiOJWDEUByG5c5UeDf-hf-n4HCocjGolGCG40YyLU4FEsT4FJ561k8w1xfwetBPIvSIN96ToGv0UAMNpYJxHwFLlT9su_Zo-zV8P-EfGugnV3VsOn9_aZzCpkxGk4VySObxCmYIr4Y1UBDb_ktbpAepJKokuUdcOqG-I9xJm9QNfeS9_NVMh_J6eL6iFm9BoYKQfUIs6Qu5a-oqWBHgfofML2WEgOAgXgtJFRlBAbkkuUJislENumpMzMP02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
#
رسمی
؛ علی نعمتی مدافع‌ سابق پرسپولیس و فولاد با عقد قراردادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137333" target="_blank">📅 19:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137332">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
فولاد قیمت رضایت‌نامه رزاق‌پور را برای پرسپولیس ۲۰۰ میلیارد تومان اعلام کرد!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137332" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzFOdkOeogE2JGuU4XV7C5B3VLbDOaVfvfL3IEJt7njeZ3s44KgPEO5TVgOXijCCWrbi-4whmaR1UHz3QaFOCmznXIGqc9FnvOU-AuT0eZtmlw8fWV91Led3_s6-v9yU9Xc1cd3_jps-H_vYJXzRr_23mZsXd4WB-GccpTbihT6aKbC-DHhPFzJzrA_qhzxU1TsmSWATNE8a0GwZw3duS4RzVQCCUSFHegDQFeuUYOXpdXqmLi6FxnSXUeW2eZeVizVwrcoz8p1meBCaRlfyhRKAASHaR5B3QflunT15UTTk334smYRhccVSuSvkOjywNSIbY__zGqBU7qkvgjp4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تارتار نه از جلالی و نه از عیدی راضی نیست و دفاع چپ و راست میخواد
☹️
☹️
☹️
///فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137331" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
15 روز تا اولین بازی پرسپولیس ورژن تارتار در لیگ برتر مونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137330" target="_blank">📅 18:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🔴
🔴
🔴
مهدی تارتار تأکید ویژه‌ای روی جذب محمد قربانی دارد و نام این بازیکن را در صدر فهرست نفرات مدنظر خود قرار داده
🔄
🔄
باشگاه پرسپولیس همچنان در حال چانه زنی برای کم کردن مبلغ رضایتنامه است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137329" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137328" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🗣
باشگاه عصر دیروز به جمع بندی رسید که باید برای جذب قربانی اقدام کنه
👀
مذاکره با قربانی و ایجنتش که رابطه خوبی با مدیران الوحده دارد شروع شده و امروز با جدیت بیشتر پیگیری شده است.
🎤
حسین قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137327" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137326" target="_blank">📅 17:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس به فولاد پیشنهاد بیفوما + ۸۰ میلیارد برای رزاق‌پور رو داده که مطهری گفته اگه یکی از بین علیپور، سرگیف یا شهرابادی رو بدید میزارم جدا بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137325" target="_blank">📅 17:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVjCUoCzb61KcMw0X84A5Hzl-FzPhfqg8ylb8xxtiW0HpGxVfzDuUbs1ySrDP2WU8G1ysZsVpsrhvbax3AKDPTNDlpb7j8l-10MUJgvXSh-A_7exiqzgSKVIsFtHf0Q59R_xAzKW_TzIB-sAP4XSMTYw-K7HgyQ87GifZ9rwd8PbQTnahKmhSXU56Q1PGIuZCeXmXrsvfkbP-3Bt8X2NbTXrdysPZ-Dkrytvqw8af6I0OPaCJ7y_gpZdbzRbFVGqGM6psAP_Qukug3Br18h6705taDF3PVgpzzI8KT8B5Q0znl3K30nyQIjOlb6zLnaNPSryu8YIEbQd_PnwyL8YQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
پرسپولیس تنها تیم در جمع تمام تیم‌های لیگ برتر بود که اردوی خارج کشور داشت و بیش از ۸ خرید جدید هم به صورت رسمی ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137324" target="_blank">📅 16:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
❌
کسری طاهری: وظیفه‌ی من بازی کردن برای نساجیه و درباره بقیه مسائل باید مدیریت پاسخگو باشه/الان زمان صحبت کردن درباره‌ی اون داستانا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137323" target="_blank">📅 16:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
فووووری 360: رضاییان از کیسه جدا شد
🚨
🚨
با توجه به حضور صالح حردانی و سامان تورانیان، سهراب بختیاری زاده با برگشت رضاییان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137322" target="_blank">📅 15:38 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
