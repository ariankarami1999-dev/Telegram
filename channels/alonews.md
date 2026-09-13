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
<img src="https://cdn4.telesco.pe/file/arViCvswGiuJrbxt5iQoBfah-JJsuKylYbupPHyKDhjc2m2-jRGgl-T-27JmeP0R0CXMfi1tfMGHQJzMJfX0sRHLnyvIw4yJwett0aYqSA_4nr0Jir6NfyWXzXl1yTba65iSHubQ7uFEFcsdY97sYjYkKPXR4IPnQuSkkEv1Fl3t4cBgbZT3z3desD_6vEP0WnfuhzRcFznbyy_9XVI4cIQeCeD2n8yytOhVGMonyiH4a9vgqlWK0pqFvuFFuVTkVreLf6FbVSROsw9shOSYwsZ3GexcThtCAFQaYpD0W3nvDEH8NnI9nnXzc0qBbjPnfiLIE5tsnagw3ibCg7BTzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 915K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 01:01:02</div>
<hr>

<div class="tg-post" id="msg-147304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ به نزدیکانش گفته باید یبارم به ایران حمله کنم احتمالا برنامش برای تاسیسات هسته ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/147304" target="_blank">📅 00:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شوک و بهت در خاورمیانه
‼️
اسرائیل هیوم:
🔴
رهبر عربستان از موساد و ارتش اسرائیل برای مقابله و کمک اطلاعاتی برای حمله به حوثی ها درخواست کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147303" target="_blank">📅 00:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bljNJwCmz8ApDJSmrUj9CbPDJNdakQOKckDnAAFTPJERsS6BjM9MnoHmsU9qBNfPXJgbyUosO4_TkGsaBG0Gr7CUWzJcH65EZnPSrV_liINauGu5cnH9FC4xA-kcmsgNLFMMsAc_nzr-zqGHkFCkC5qBsxU7JcHK1DKyP5NFlR8ODT430oHEII-FaFZCONiyRuDXaH62jgFKNnqalDQUQhZUbnO9ZiQ0STaxAIHDY_jqKNV2TAzx88vMYpLC0quTM5eBeVmRfUFv7ENUQCkE_G18NZPIEz_ZbsqH_9x4i1Thn1_iaNjMpQwk88ykNTcKpxzeXf5mYr0KJTU9iY2cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادان: شرایط جنگیه، هرکی دست به اعتراض بزنه ما دست به ماشه هستیم، چون تو این وضعیت هر شلوغی یعنی کودتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/147302" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWcsnU17J0FsCUG89FOFjS8C4vwdY9QsbWvYDDPfQFCDx72x7AbeZGhomem1ogHl56OfT-oieJkavxNEBdwcriROxjmUPmKJ-EDy-HYCrgdrZDW6WRpI0vSh6_W89PEzGSoUvFt7Q5prvALpPH4Uz-NB3mTZb7wE1eEsxhqpAhlRT9qgIBjvTs-7sGRdL5-FaSPw69SszdXeLvv5nzfx41DTCgKEmGlGurV4XJBe3ZwgCHHF2VUYfzlLibFrM1YGlRU_5sAdkrX5jgq8T3BneCw_ZsRNYYixFuK9SMTWfyvCKHIJHS8g4VWMW7kxsd5tlDqORnB78EBbxGTsHJF6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر هم اکنون 232000
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147301" target="_blank">📅 00:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کاتز: تا خلع سلاح حزب‌الله از جنوب لبنان عقب‌نشینی نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/147299" target="_blank">📅 23:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی ان‌ان به نقل از منابع آگاه: آمادگی برای بررسی پرداخت‌های داوطلبانه در ازای هدایت عبور کشتی‌ها از تنگه هرمز وجود دارد
🔴
بر اساس چارچوب حقوقی عمان، پرداخت داوطلبانه در ازای تأمین ایمنی ناوبری و حفاظت از محیط زیست پیش‌بینی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147298" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیران خارجه قطر و عربستان درباره تلاش‌ها و هماهنگی‌های مشترک برای کاهش تنش و تشدیدزدایی گفت‌وگو کردند
🔴
وزرای خارجه قطر و عمان درباره تلاش‌ها برای کاهش تنش و تقویت امنیت گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147297" target="_blank">📅 23:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوووووری / گزارش ها حاکی از شلیک دو موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/147296" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / گزارش‌ها از وقوع یک انفجار شدید در نزدیکی ساحل سیریک در استان هرمزگان حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/147295" target="_blank">📅 23:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خبرگزاری واس گزارش داد وزیر خارجه عربستان در تماس با همتای اماراتی خود درباره تلاش‌ها برای مهار تنش‌ها و جلوگیری از تشدید اوضاع در منطقه گفت‌وگو کرده است.
🔴
دو طرف همچنین بر ضرورت یکپارچه‌سازی مواضع در برابر تحولات اخیر و تقویت چارچوب همکاری میان کشورهای شورای همکاری خلیج فارس تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/147294" target="_blank">📅 23:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
محمد علی بک» مدیرکل خلیج فارس وزارت خارجه: بنا به درخواست برخی کشورهای منطقه و تصمیم مشترک عمان و ایران، نشست وزرای امور خارجه کشورهای ساحلی خلیج فارس که برای روز دوشنبه برنامه‌ریزی شده بود، به تاریخی دیگر موکول گردید.
🔴
ایران در رایزنی نزدیک با عمان، درباره زمان مناسب برای برگزاری این نشست هماهنگی‌های لازم را انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/147293" target="_blank">📅 23:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عمان نشست منطقه‌ای برای دستیابی به توافق درباره تنگه هرمز را به تعویق انداخت!
🔴
بدر البوسعیدی، وزیر امور خارجه عمان در بیانیه‌ای رسمی، از تغییر در برنامه‌ریزی نشست منطقه‌ای که قرار بود فردا در خصوص تنگه هرمز برگزار شود، خبر داد.
🔴
وزیر خارجه عمان اعلام کرد…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/147292" target="_blank">📅 23:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWI1uCH-csefv73GuORUigRRHeRIWO22WlSI-A-tECVb99MSh7v8SECfYvKk6u2ZEqJ1PvYijeyoy2S7uGgaKy7HLi4zGKKYrhRDgCJEVAmuHvzEiJoFPxOO2MolEHoHCKei3oq5H1GFxF9RQf1viyW7-fkWX32kY-CxIDkpmPzyexvmAETavlEEkYcl6gaQzxiGI2tuilpCPCnxyQE4Z9RnWW6hBG4OXI8ILdfkzPieRfYufk1sIkGlQjsqL5h_PIfGdH8AwGSXFTpYo6O-qkt3FVGXCOUxM6Qj-bk2lrT1lweyC7S9YPDV_B8z08E_f1OsmJQbYgbqhGKQcGpNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عمان نشست منطقه‌ای برای دستیابی به توافق درباره تنگه هرمز را به تعویق انداخت!
🔴
بدر البوسعیدی، وزیر امور خارجه عمان در بیانیه‌ای رسمی، از تغییر در برنامه‌ریزی نشست منطقه‌ای که قرار بود فردا در خصوص تنگه هرمز برگزار شود، خبر داد.
🔴
وزیر خارجه عمان اعلام کرد نشست منطقه‌ای قرار بود فردا در صلاله برگزار شود، اما برای تضمین دستیابی به توافق، موعد آن به تعویق افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147291" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6de5b369.mp4?token=DEVw3gH8Xs-ghvK7aBFJL0mxh7z8CD6wNkO_LY2c6MZUY03wO579jB9y8zeFiDci49ZosCRul8HNwFtKQbw37RFP4W8_s07gA9QhWnijDEYgbqU3UEjVKPuJ0MSnG0vvunjn11zSoyghI-6Ra2hLsklnMRdy9CewIRh9hftTDbKGcr8EDr9mPNBZuRFrQ7sG5ELjE2FkYKMFp3tjXX7tCdLXutcziuWNPTBmIaQZLm_niPShuiSB5mphK4hlrwLSdmrJebR7RI5DCanz5SlbzixDgOiYfqC3SzSxvDoIdgbSakTCnXyZZFOAqgUYmQQUH76Igtn2gTF_aOMQrL8vYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6de5b369.mp4?token=DEVw3gH8Xs-ghvK7aBFJL0mxh7z8CD6wNkO_LY2c6MZUY03wO579jB9y8zeFiDci49ZosCRul8HNwFtKQbw37RFP4W8_s07gA9QhWnijDEYgbqU3UEjVKPuJ0MSnG0vvunjn11zSoyghI-6Ra2hLsklnMRdy9CewIRh9hftTDbKGcr8EDr9mPNBZuRFrQ7sG5ELjE2FkYKMFp3tjXX7tCdLXutcziuWNPTBmIaQZLm_niPShuiSB5mphK4hlrwLSdmrJebR7RI5DCanz5SlbzixDgOiYfqC3SzSxvDoIdgbSakTCnXyZZFOAqgUYmQQUH76Igtn2gTF_aOMQrL8vYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران اعلام کرده که یکی از کشتی‌هایش شب گذشته مورد اصابت قرار گرفته است. آیا این کار توسط آمریکا انجام شده است؟
🔴
ترامپ: نمی‌خواهم چیزی بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/147290" target="_blank">📅 22:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b85cbdf7.mp4?token=N7tH6A0Ooktn1C0qAaJf9W1h3Njvu46_EMro_WaX7au5cGlNj7W9ukzaDv0Az52ssdEOMtb8KauFFk1dPLbBNyiKdH-EzbpyrzKW0jbqwuzpBDH-FvNUucAm1AWa_BoDxBLCWXb16wBQPu8VSPyS1CNAaRTjQfLxhY2u337ombzo8BWAO5Ud8XIUYg-CO-wfgljvinautqfyhlmQgYWHlYiqee5GOWLJerzdFfL9Mn2P-mEY5AxRrOA4p4morruPsJPm_3_J-nS-MFIJXH2Gzbeyi3Twde3O8GG0hFwiWLNwMO0NwjmTgvoXDA7jsvVsGl-IEfLqbD30rhdSiZdHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b85cbdf7.mp4?token=N7tH6A0Ooktn1C0qAaJf9W1h3Njvu46_EMro_WaX7au5cGlNj7W9ukzaDv0Az52ssdEOMtb8KauFFk1dPLbBNyiKdH-EzbpyrzKW0jbqwuzpBDH-FvNUucAm1AWa_BoDxBLCWXb16wBQPu8VSPyS1CNAaRTjQfLxhY2u337ombzo8BWAO5Ud8XIUYg-CO-wfgljvinautqfyhlmQgYWHlYiqee5GOWLJerzdFfL9Mn2P-mEY5AxRrOA4p4morruPsJPm_3_J-nS-MFIJXH2Gzbeyi3Twde3O8GG0hFwiWLNwMO0NwjmTgvoXDA7jsvVsGl-IEfLqbD30rhdSiZdHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا شما آماده‌اید که در سال 2028 از جِی. دی. ونس حمایت کنید؟
🔴
ترامپ: الان خیلی زود است. من فکر می‌کنم او فوق‌العاده است. ما افراد فوق‌العاده زیادی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/147289" target="_blank">📅 22:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147288">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7989307a6.mp4?token=NlECgj8yV5VidgjsY7b9d6kI0T_JGZf3Dwyx6OU7_ZLvU3BS-23MythQjMXgQ5lmWXbpeBBIU-bIGsygnZiOeCJpauUNK9VDLtSfLH63FkygAx4p0sevE6niKihLAJZPkKG8Wjyhs47oMUnRnjwlF_S2tYi7ASr9KS0NxsVk7ukeOVjaIfhW89EiD92JAgKxNUToopBaVJecl36hBONxb4t4bT_kgHTBr70LFDqhX7cIpQguz3eWz848fPKozq2fj2S26JcwalzDH6o3JZRNGtdgZiKC0CmMtI-8NQTK0gHdnBJKonuSl47mdUoHKRBOAGwqxiFLmmtSFmc2KRepiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7989307a6.mp4?token=NlECgj8yV5VidgjsY7b9d6kI0T_JGZf3Dwyx6OU7_ZLvU3BS-23MythQjMXgQ5lmWXbpeBBIU-bIGsygnZiOeCJpauUNK9VDLtSfLH63FkygAx4p0sevE6niKihLAJZPkKG8Wjyhs47oMUnRnjwlF_S2tYi7ASr9KS0NxsVk7ukeOVjaIfhW89EiD92JAgKxNUToopBaVJecl36hBONxb4t4bT_kgHTBr70LFDqhX7cIpQguz3eWz848fPKozq2fj2S26JcwalzDH6o3JZRNGtdgZiKC0CmMtI-8NQTK0gHdnBJKonuSl47mdUoHKRBOAGwqxiFLmmtSFmc2KRepiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: خانواده‌های قربانیان حادثه 11 سپتامبر از شما خواسته‌اند که به آن‌ها کمک کنید تا دولت عربستان سعودی را در قبال این حادثه مسئول بدانند، و از شما می‌خواهند اسناد بیشتری را منتشر کنید که ارتباط برخی از تروریست‌ها را با افراد در عربستان سعودی نشان دهد. آیا شما آمادگی انجام این کار را دارید؟
🔴
ترامپ: من این موضوع را بررسی خواهم کرد، زمانی که به [کشور] بازگردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/147288" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147287">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72265eb413.mp4?token=Yd4WIfyMNtg2cQB3yeAVsTmqMksIYHFPSod8MnBirOeUD7yKifT3_SynRnymZ88BxTJYnHXSqLhBcK0RhtcKZOF9z0J6eLEp6MdzDzTyzTWP12opCXkgQSaOpi3DsjNZq3ZozUXaE6Hl8Pt5J1c9JnpM4R3Vj1WVwmJ_Ns-2qxPAPbPMe1OLEhLg1dXKqLq2Gnayycl0cE8aIwDOwHGAk_NSw_vLLjNcP03LnWWwv9vSzM4z5zZ5nzksGr1X70DczIeQsAbuUF8Iw8RvW3qhKif6qw0UaWjPteSjxye6K5BQkG7L5kFVzOsOGV-Uq5yx7pHGZDIh8LeBFGMssBUPDKlKDLHmwd6Rt_-vxWIYm1pdPiRF4XAc_KyHyRVDnO6dVWNAYQkAmOadCc7cWAGIc4pemv2bjnqkECw6h241BbhR3KQsA9waFePJc-EMeEhX5o4NCVKjCDoKlvlLAuDFynOzkxB94_ilUAlY1WbYTdbTNhJNrbS6zltXPrpDprT6jxMGGl58qp2JdE3fadfEx-dBElQf6f9kUBRcWHPJV-yWTpBHJfEme9IavdaszcSnCGMLoeBjo2lqDlAxH2GTjNI8iDNDk8HitAOVQI-q8_YUWqziEp235oHg5isAoioctGOkdiDm2Eb-SRIJ08puqw3FX2TnjS4MrGj1ol5RBMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72265eb413.mp4?token=Yd4WIfyMNtg2cQB3yeAVsTmqMksIYHFPSod8MnBirOeUD7yKifT3_SynRnymZ88BxTJYnHXSqLhBcK0RhtcKZOF9z0J6eLEp6MdzDzTyzTWP12opCXkgQSaOpi3DsjNZq3ZozUXaE6Hl8Pt5J1c9JnpM4R3Vj1WVwmJ_Ns-2qxPAPbPMe1OLEhLg1dXKqLq2Gnayycl0cE8aIwDOwHGAk_NSw_vLLjNcP03LnWWwv9vSzM4z5zZ5nzksGr1X70DczIeQsAbuUF8Iw8RvW3qhKif6qw0UaWjPteSjxye6K5BQkG7L5kFVzOsOGV-Uq5yx7pHGZDIh8LeBFGMssBUPDKlKDLHmwd6Rt_-vxWIYm1pdPiRF4XAc_KyHyRVDnO6dVWNAYQkAmOadCc7cWAGIc4pemv2bjnqkECw6h241BbhR3KQsA9waFePJc-EMeEhX5o4NCVKjCDoKlvlLAuDFynOzkxB94_ilUAlY1WbYTdbTNhJNrbS6zltXPrpDprT6jxMGGl58qp2JdE3fadfEx-dBElQf6f9kUBRcWHPJV-yWTpBHJfEme9IavdaszcSnCGMLoeBjo2lqDlAxH2GTjNI8iDNDk8HitAOVQI-q8_YUWqziEp235oHg5isAoioctGOkdiDm2Eb-SRIJ08puqw3FX2TnjS4MrGj1ol5RBMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کاهش روابط تجاری با کشورها: من این کار را با برخی از کشورها انجام خواهم داد. من هیچ انتخابی نخواهم داشت.
🔴
ما نمی‌خواهیم با هیچ کشوری کسری بودجه داشته باشیم. ما می‌خواهیم مازاد داشته باشیم، یا حداقل به تعادل برسیم.
🔴
این کار در یک بازه زمانی انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/147287" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38762dc8a9.mp4?token=duWAiRGoLhLB45OiZXy8XnAAOK0jzTw2oC6Cl8rH2BBkvE1KXjyk0DyfI3qr_Io4PRutTB32bno9J3z1UTGgInHS32oQKZPzjSjEIwf-7DvD5NbqVaZ5u3799LFwUcZEFpijvbeOF3sYDC9uhlvIu0n1odYd2iLpOxsGQ-eDFuHVfWsgCiBPkRHY1I5ROP_eqE7RBdfTZKLw48BkGxGT-G_jUf2JO8gk81IFr3wbrpy1DQ-FWiTMFVJWr7AhUnHwREoNMLzKci2DKkHJPcn4fICWlwKMrA5cMTfBZJYMZXog1tee1XB_CKJrexuvzBKeczfZamvyrB4ZgpeFXQMGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38762dc8a9.mp4?token=duWAiRGoLhLB45OiZXy8XnAAOK0jzTw2oC6Cl8rH2BBkvE1KXjyk0DyfI3qr_Io4PRutTB32bno9J3z1UTGgInHS32oQKZPzjSjEIwf-7DvD5NbqVaZ5u3799LFwUcZEFpijvbeOF3sYDC9uhlvIu0n1odYd2iLpOxsGQ-eDFuHVfWsgCiBPkRHY1I5ROP_eqE7RBdfTZKLw48BkGxGT-G_jUf2JO8gk81IFr3wbrpy1DQ-FWiTMFVJWr7AhUnHwREoNMLzKci2DKkHJPcn4fICWlwKMrA5cMTfBZJYMZXog1tee1XB_CKJrexuvzBKeczfZamvyrB4ZgpeFXQMGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، نظرسنجی‌ها جعلی هستند. میزان محبوبیت من در ایرلند خوب است. میزان محبوبیت من در ایالات متحده عالی است.
🔴
مشکل این است که فقط نظرسنجی‌های معتبر منتشر می‌شوند، همانطور که شما می‌دانید. ما عملکرد خوبی داریم. کشور ما عملکرد بسیار خوبی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/147286" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28945f0ed.mp4?token=I8GU62T6LkrxsTx9n-qo7nLZLbKT5btqtsEm4D2JkYrkbbriv4Pchq8fSoVTy4ESl2ogLbsKMrQwi_sjNMv078eUQqwLjG3viSehLA4JJ8TZ69g0_S9UdN2ZJ6FBsC2GX9dqcPGG8EKv4jaQtJRZToqqQhf6a8aovfG_1qbyO51WWhdJ-jff5xyjfsZGJEyVINcVJSdqMBGIRDXlyv87yUutsd9qYxVp9ChBrpY5sIh8esgyguXx4gFCai5VNlPVifueLGIHru0KuRlM0sq1v6uHVY8Z1tus-pcVGcdHdIrq2C0ug69-MNbx-AuBTqAN0AM3Cx9PiI3j4AkWoE_gqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28945f0ed.mp4?token=I8GU62T6LkrxsTx9n-qo7nLZLbKT5btqtsEm4D2JkYrkbbriv4Pchq8fSoVTy4ESl2ogLbsKMrQwi_sjNMv078eUQqwLjG3viSehLA4JJ8TZ69g0_S9UdN2ZJ6FBsC2GX9dqcPGG8EKv4jaQtJRZToqqQhf6a8aovfG_1qbyO51WWhdJ-jff5xyjfsZGJEyVINcVJSdqMBGIRDXlyv87yUutsd9qYxVp9ChBrpY5sIh8esgyguXx4gFCai5VNlPVifueLGIHru0KuRlM0sq1v6uHVY8Z1tus-pcVGcdHdIrq2C0ug69-MNbx-AuBTqAN0AM3Cx9PiI3j4AkWoE_gqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا، درباره ترامپ: ترامپ ایده‌پرداز فوق‌العاده‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/147285" target="_blank">📅 22:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536ffda598.mp4?token=hmGCDiWd6XNnCOKKT8W81C7Lbva5xWI7LiBL3pQIg84sn3nv_Bo9dXN72jIYSVfukgkHy31BG6einDnHDvwsBXehTnXqCeMVQCVAucl5gb-tlk5aOcxvrge7rRRL9tYnev6mMRJdUztd1HxYC-4kuZnT5NHqV9ZvP5821yjeFXoOn3ZFRCckgzuyQW3tp_RgBLedZ0x4d6iG1otfaM1828Kop5CPpFHEYUnpxuZSGoMeU9WsYullUP8jbvylv0SZyhos8cOKwbiRBECdjd4h-hU0Vi3ASR1j2FkVRgq6Pcad8-26h4QYujhz6qgVxkCbiTtxNsW5xwPQQuXnRGgJ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536ffda598.mp4?token=hmGCDiWd6XNnCOKKT8W81C7Lbva5xWI7LiBL3pQIg84sn3nv_Bo9dXN72jIYSVfukgkHy31BG6einDnHDvwsBXehTnXqCeMVQCVAucl5gb-tlk5aOcxvrge7rRRL9tYnev6mMRJdUztd1HxYC-4kuZnT5NHqV9ZvP5821yjeFXoOn3ZFRCckgzuyQW3tp_RgBLedZ0x4d6iG1otfaM1828Kop5CPpFHEYUnpxuZSGoMeU9WsYullUP8jbvylv0SZyhos8cOKwbiRBECdjd4h-hU0Vi3ASR1j2FkVRgq6Pcad8-26h4QYujhz6qgVxkCbiTtxNsW5xwPQQuXnRGgJ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان ایالات متحده: به نظر من، این ترکیبی از کشورهای متحد ما، دوستان ما در ناتو و سایر کشورهای عربی خواهد بود ... که با هم متحد می‌شوند تا اطمینان حاصل کنند که تنگه هرمز باز بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/147284" target="_blank">📅 22:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تسنیم: حذف سهمیه بنزین ۱۵۰۰ و ۳۰۰۰ تومانی خودروهای بالای یک میلیارد تومان تکذیب شد؛ سهمیه‌بندی مثل گذشته ادامه داره وق فقط نرخ سوم بنزین از ۵ به ۱۰ هزار تومان افزایش پیدا کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/147283" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ed9b90c6.mp4?token=NA-wvq2MMzl3qs3kvuaALR70vtvhOfo9NWR8DxLr3ae6eF5Pw1JFwg_0nTfz-3Ty4YDzSuCCUm42rpY1BltnxTceV8jN1C-qDI9U2YKzOpMv9d7LAm_fpFhlqFbQnTSUkXRy8KKAxy_FGBExjGuqacZ14-5ZyPzRK6YMMaC-pYL6801jhRpBudb5FbIwISPzJCJtxb7HxFLvuk9-Rvo2c9_B298om-MAglmrOASR125jXLxIpDairHPOdtBpsl7KCm6t7lEJWlVGgNAiV3mW2oatydhT3E73PzkhUlEUsWFUbrPn-K_zfHb80IlNbonErfmNK-6Y-yZEF7tmnNqsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ed9b90c6.mp4?token=NA-wvq2MMzl3qs3kvuaALR70vtvhOfo9NWR8DxLr3ae6eF5Pw1JFwg_0nTfz-3Ty4YDzSuCCUm42rpY1BltnxTceV8jN1C-qDI9U2YKzOpMv9d7LAm_fpFhlqFbQnTSUkXRy8KKAxy_FGBExjGuqacZ14-5ZyPzRK6YMMaC-pYL6801jhRpBudb5FbIwISPzJCJtxb7HxFLvuk9-Rvo2c9_B298om-MAglmrOASR125jXLxIpDairHPOdtBpsl7KCm6t7lEJWlVGgNAiV3mW2oatydhT3E73PzkhUlEUsWFUbrPn-K_zfHb80IlNbonErfmNK-6Y-yZEF7tmnNqsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا:ایران‌ها شرکای قابل اعتمادی در مذاکرات نیستند. البته، آن‌ها هر روز دروغ می‌گویند. آن‌ها سر میز مذاکره می‌آیند، یک چیز به شما می‌گویند و عمل متفاوتی انجام می‌دهند
🔴
برای برخی از آن‌ها، این بخشی از دینشان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147282" target="_blank">📅 22:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147281" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyQIGCwAHe-4u298UE8Wk6GZ_wFevSwRb_JU56rQYW0etRYFTZ2X6XZHpFSiRNoPzMF4Lb_YX1hiPDc3kO4Of4hrhDrTrZpYX5IbSI9-24f_C9qQJciuwmkYBUTPDgqdRCiAOc_A9YbF6DCNxSta_7Si4UUstBFxWD9DZMhYB9JlO7K_I8lZ4Ydqd3SA_gq908XWBMeXCfaMfh960Xw_r2uHynizPQFUuAd0JWkaFRX03GVar4Z4r1om3zk4iUCPAwAY-Qgw-EHBj1H_6np7EEK1hj0d0aaga9TgCMzBRfIqZchzjtgUqIJ7Yg65wH8dHB6fbmpbSrQpU9-FoodM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فانا: مدیرکل دارو: واکسن آنفلوآنزا در اواخر شهریور و اوایل مهر ماه می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147280" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شی جین‌پینگ رئیس‌جمهور چین ممکن است از دیدار در اواخر این ماه با «دونالد ترامپ» رئیس جمهور آمریکا، خودداری کند.
🔴
دلیل این تصمیم احتمالی از سوی پکن، اعلام تایید فروش تسلیحات جدید از سوی آمریکا به تایوان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147279" target="_blank">📅 22:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=a2cXxNX6aRTjEu1GGDWHI8kv1s2-BFvZDbk9wGcvODTr4ZkBjQAANMH33iWpuX6kCi1bv8AM-aZx0k7RYuwN1s3eN_gxwwGtz8YGhVIGbdDs2pEWn_YhchtCBmqcyNqYXSyd_b0EwfQvqT25IYwNw3-551tF3P3So_OlqU0ffI8p7ezyIuK5rLk7tdk86O_hQCWms0gwVjsK1KS_e2xLAhcNuXTP5tiHK1Dd8GyM3fOh8NVQxDjrxUX2RR2Mp9JXMld2o1Fj96HgmGa36TpBgvwQt2IbRHJgrWypnXkr8kUE9H0G5kUSBqPWfRF378KP15e0YNEsgvqnHK4PFWr3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=a2cXxNX6aRTjEu1GGDWHI8kv1s2-BFvZDbk9wGcvODTr4ZkBjQAANMH33iWpuX6kCi1bv8AM-aZx0k7RYuwN1s3eN_gxwwGtz8YGhVIGbdDs2pEWn_YhchtCBmqcyNqYXSyd_b0EwfQvqT25IYwNw3-551tF3P3So_OlqU0ffI8p7ezyIuK5rLk7tdk86O_hQCWms0gwVjsK1KS_e2xLAhcNuXTP5tiHK1Dd8GyM3fOh8NVQxDjrxUX2RR2Mp9JXMld2o1Fj96HgmGa36TpBgvwQt2IbRHJgrWypnXkr8kUE9H0G5kUSBqPWfRF378KP15e0YNEsgvqnHK4PFWr3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند : شطرنج، پاسور و سودوکو باعث احضار اجنه میشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147278" target="_blank">📅 22:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147277" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سازمان رسانه‌ای اسرائیل مدعی شد ارتش اسرائیل به صورت محدود از ارتفاعات «علی الطاهر» به سمت قلعه «شقيف» در جنوب لبنان عقب‌نشینی کرده‌ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147276" target="_blank">📅 21:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خبرگزاری تسنیم: از روز سه‌شنبه ۲۴ شهریور گردهمایی جانفداها برای آموزش کار با اسلحه شروع میشه و بعد از آموزش به گردان های نیروهای مسلح اضافه میشن تا برای جنگ با دشمن آماده بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147275" target="_blank">📅 21:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b41b26dc.mp4?token=kxzGuE4cxtetqVpJA04Jce9IPb-k3nQTDHhQT3vgVxjK0tp0WtwG9RXHLLc_oEVJ5QvdvkhSpdrcemDDzLPkALQ1ERiqRQB_WUxAAtOEcbAE13Mo-vlyedoWuMQ-NO4EFWDi2SNy4GGn5mn9PXMH8gVl0Uo4UzU8GaCMi5sQD8FWeoVt6R_TWUlyr2VC-BvOa0DUE0LiwJqZs_6lP1nZVVAuwMPBfzZ0yj-MzwfRFM2FzKtVMq2uP2S3Wj4hp2yEns4bgZVixYRunT8hv81kgTyVDPuJ9ogPOjq84-9580io5mPMfy-jLPxv0FvYowCKmVqb27nw5RNf9bJPBaAKsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b41b26dc.mp4?token=kxzGuE4cxtetqVpJA04Jce9IPb-k3nQTDHhQT3vgVxjK0tp0WtwG9RXHLLc_oEVJ5QvdvkhSpdrcemDDzLPkALQ1ERiqRQB_WUxAAtOEcbAE13Mo-vlyedoWuMQ-NO4EFWDi2SNy4GGn5mn9PXMH8gVl0Uo4UzU8GaCMi5sQD8FWeoVt6R_TWUlyr2VC-BvOa0DUE0LiwJqZs_6lP1nZVVAuwMPBfzZ0yj-MzwfRFM2FzKtVMq2uP2S3Wj4hp2yEns4bgZVixYRunT8hv81kgTyVDPuJ9ogPOjq84-9580io5mPMfy-jLPxv0FvYowCKmVqb27nw5RNf9bJPBaAKsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف در واکنش به قیمت ۹.۹۹ دلاری سوخت در آمریکا، ویدیویی از سیمپسون‌ها منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147274" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJs77_WJ4QfqnqkN986s7pAfl66gMTjh8Hrb0YPkoRcAVAwkAe-0iZ3-zwuMao1GzRhVXsnvi8gMyg6FjDOVxmghSdb4jl8WXlSu2S3fq98ytZ3GDOPjXw_uCSB2GXxJmZFHEDqB2leEzS7j5-88q4mIs-fkoJRcdvgGKpb8V3A7v9t-ze9KM4q1Qi7w5SHdtcraSBtU7V0-hUWKEGXe1E1ALvtkzTDe5a2nA3BusmUhA-Gd7d2cUsXLEZpIf4AOEdSUJrd_RhGW6RMjuhoyLvkO6nkHzahwVdocNO2Z_-h-4K9EzhJ2sjv016m_JTr8h0u2sU18J2c4EgDhSXd28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار بمب مقابل یک کلیسا در شهر حماه سوریه
🔴
یک بمب دست‌ساز مقابل یکی از کلیساهای شهر حماه سوریه منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147273" target="_blank">📅 21:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الجزیره: پیشروی سریع انصارالله در یمن «قطعاً یک نقطه عطف» در جنگ منطقه‌ای است
🔴
حملات هوایی به رهبری عربستان به‌تنهایی احتمالاً برای بیرون راندن انصارالله کافی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147272" target="_blank">📅 21:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147271">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که ائتلاف تحت رهبری عربستان سعودی در ۲۴ ساعت گذشته، ۵۸ حمله هوایی در مناطق مختلف یمن انجام داده است که این حملات مناطق تعز، لحج، الجوف، حجه، البیضا و صعدا را هدف قرار داده‌اند.
🔴
این حملات توسط جنگنده‌های اف-۱۵ که از پایگاه هوایی خمیس مشیت عملیات انجام می‌دهند، صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147271" target="_blank">📅 21:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سی‌ان‌ان: عمان پیشنهاد ایران برای دریافت اجباری عوارض را رد کرد و پرداخت‌های داوطلبانه برای ایمنی ناوبری و زیست‌محیطی را پیشنهاد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147270" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سازمان بین‌المللی مهاجرت: حدود ۸۵ هزار نفر به دلیل جنگ در یمن مجبور به ترک خانه‌های خود شده‌اند و حدود ۲۰۰۰ نفر به جیبوتی رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147269" target="_blank">📅 21:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
لهستان: اگر روسیه حمله می‌کرد، فورا شکستش می‌دادیم!
🔴
وزیر خارجه لهستان : ما در قدرت هوایی برتری قاطعی نسبت به روسیه داریم.
🔴
اگر اوکراینی‌ها نیمی از ظرفیت پالایشگاهی روسیه را در شش ماه از کار انداخته‌اند، ما می‌توانیم این کار را در شش هفته انجام دهیم و نیم دیگر را از بین ببریم.
🔴
اگر روسیه به ما حمله می‌کرد، ورشو فورا مسکو را شکست می‌داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147267" target="_blank">📅 21:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سه منبع ناشناس به خبرگزاری رویترز گفته‌اند عربستان سعودی در بندر دریای سرخ خود در ینبع تنها به اندازه پنج تا هفت روز ذخیره نفت دارد و مقدار کمتری نیز در مصر ذخیره کرده است
🔴
توانایی عربستان برای دور زدن تنگه هرمز و ادامه صادرات نفت پس از حمله به خط لوله شرق به غرب این کشور به‌شدت محدود شده است.
🔴
این خط لوله روز بعد از حمله، به‌عنوان «اقدامی احتیاطی» متوقف شد. این مسیر، تنها گزینه اصلی عربستان برای صادرات نفت بدون اتکا به تنگه هرمز محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147266" target="_blank">📅 20:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=jyxb7gP241sSpYOGe1OjU0mQhEoaLPNMjB_Ja1qr3u8XTCSZ5rvf1khsJ9vri1oHT_2PSXYOIZZFxfkrjQBarXxS0z5vIW9wf4eY7ousfzTHVtucSZY5X8Q4b00FI4UveqvozvXUeVgs4ZMe0hPO6sfuV3jaK91T720S_v_zVS832cGbHt9goXMxZ_xnITCkTowGxOjL8sKO_nBxdk1_-bnpG0v83DwC3OA9Yg63vjvwY2idBWjiSIQMloeLwGqkmRFzsYhtv4K7y84x5gEAxwJfFkjPg0hKbEUcQHTVsi59YCk1ZIbIKfsI7GzZy8FWWCwcqkAuo9hxBms_NnuBOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=jyxb7gP241sSpYOGe1OjU0mQhEoaLPNMjB_Ja1qr3u8XTCSZ5rvf1khsJ9vri1oHT_2PSXYOIZZFxfkrjQBarXxS0z5vIW9wf4eY7ousfzTHVtucSZY5X8Q4b00FI4UveqvozvXUeVgs4ZMe0hPO6sfuV3jaK91T720S_v_zVS832cGbHt9goXMxZ_xnITCkTowGxOjL8sKO_nBxdk1_-bnpG0v83DwC3OA9Yg63vjvwY2idBWjiSIQMloeLwGqkmRFzsYhtv4K7y84x5gEAxwJfFkjPg0hKbEUcQHTVsi59YCk1ZIbIKfsI7GzZy8FWWCwcqkAuo9hxBms_NnuBOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147265" target="_blank">📅 20:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fa531cab.mp4?token=H0uDwrGh8JZhm6t7b3F2jN6bFSpDH-0iCTGAfA-brodx20CNuj7W4SqI1qQ9Rr1r3qgQpKubt6w5RZW4IXr0LycoxQ6A5_PVQq7VnIHMUsmP-JBgsrBHn9t00Z1baoELuS9jea1CPMerA9i63qtSosLKPEywRNeLJ2NyAQvqn8mwPIcTc7TozDhEZM7SqeIHNyrGXVzzQxaTP2dYxqXkFXJQK_LDXqDNJrFF77JhQ-oQb758eGYjyAp3FKGPF4WFa778tayGvspw1sM1Ae0IJFCMGG7ZsF59k5yhG5n824ZxqdxHpAaKdxIn9Lc-BtJk51q-nLI0Z-hPbtJi5OZZPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fa531cab.mp4?token=H0uDwrGh8JZhm6t7b3F2jN6bFSpDH-0iCTGAfA-brodx20CNuj7W4SqI1qQ9Rr1r3qgQpKubt6w5RZW4IXr0LycoxQ6A5_PVQq7VnIHMUsmP-JBgsrBHn9t00Z1baoELuS9jea1CPMerA9i63qtSosLKPEywRNeLJ2NyAQvqn8mwPIcTc7TozDhEZM7SqeIHNyrGXVzzQxaTP2dYxqXkFXJQK_LDXqDNJrFF77JhQ-oQb758eGYjyAp3FKGPF4WFa778tayGvspw1sM1Ae0IJFCMGG7ZsF59k5yhG5n824ZxqdxHpAaKdxIn9Lc-BtJk51q-nLI0Z-hPbtJi5OZZPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده مرکز فرماندهی نیروهای مسلح ایالات متحده (CENTCOM)، ادمیرال برد کوپر، می‌گوید که نگرانی‌ای درباره کمبود مهمات نظامی ایالات متحده ندارد.
🔴
«ما به خوبی تسلیح شده‌ایم و برای هر سناریوی احتمالی آماده هستیم.»
🔴
در پاسخ به پرسشی مبنی بر اینکه آیا نگران تهدیدات آینده است یا خیر، کوپر پاسخ داد:  «من نگران نیستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147264" target="_blank">📅 20:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
با وجود عدم پیشرفت در مذاکرات مستقیم دولت لبنان با اسرائیل، سفارت آمریکا در بیروت، از دور جدید مذاکرات دو طرف در ماه اکتبر در رم خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147263" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: تنگه هرمز اقتصاد جهان را «بحرانی» کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147261" target="_blank">📅 20:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پرسیدن دلار 235 تومنی خریدم ریخته؛ چیکار کنم؟</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147260" target="_blank">📅 20:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
قبیله بنی حشیش علیه حوثیا اعلام جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147259" target="_blank">📅 20:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مدیر سامانه هوشمند سوخت گفته خودروهای بالای یک میلیارد تومن دیگه سهمیه نرخ یک و دو نمی‌گیرن
🔴
پ.ن: خب قرمساق مگه الان ماشین زیر ۱ت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147258" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا؛ جنگ علیه ایران ادامه ندارد و اقدامی که اکنون سعی در انجام آن داریم، حل‌وفصل جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147257" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147256" target="_blank">📅 20:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inp0rY-BpKXTC1XSfZsRn_Gw55C9MdJ0qOqiC3Wkq96jiGeMp6E2MsGQiGeq_weT34jZZlFEm-J2xCLOIcYcC5Zjj-GMSmpsGPjyJavbhZUZVrFDIKH5QnFhOUtOcrO5-aivGiusjdE4f3WLKuZyMpn_ITmvqOVFluPb72D4cu6OPt7JIOFhEEfaAZRctTNkMSIFU-MXtcegCsqVa3yFh9O_j4mpxuvVptUHZanmVdGvxsWZfH4o2MZn-SJNSMXo1uIuKJ0eY7XgWiztYSBFSumANCa2L_U8VKH2zvllb_iwz7GE02YTIRPZqE0QdCP7MazAIJszPOUwiVBHU2mD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی به منطقه‌ای بین شهرهای زوطر شرقیه و مایفادون در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147255" target="_blank">📅 20:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhPNZiyiIliMEn8t-nn0kDGOhqHHQmpX1qZfWP94saZbBIH0ddpdhjxjcW7cPuWMFjyPWedgt01Dmk_UftSkkjDs5nSR2_Ova16q-3neYP1owRyJxNcQ5U92boVO8cwakLZdKaCLaPjT6KavBHAE7uSZRt8pcPULeFfxmd_ThBNqW_3sMOQnIjHp7jm0bRxKMwhBMV3Tt8W2ZNZU2vNhqFgfYyJNUOsMwbGTpR_aw95jwt-lDTjrgT70nVMVlA3TqdNa7tk-PadDulmZA-HIUPPscohIaTpLfz1erchI9ns3phA3qcvADZoNrqrL1cpn4Z7uiItymxHtc2KasGDuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست قیمت انواع موبایل ریجستری در بازار
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147254" target="_blank">📅 20:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
روزنامه رای‌الیوم: اولتیماتوم سخت عربستان و اردن به عراق؛ گروه‌های مسلح را منحل کنید یا منتظر پاسخ باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147253" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=bJak475-ygva5pmvleqbWgidor8GOukNvViLIdy5NtTXZEx47Z85Hu0TbNc1n0dipe2mJkz3rSr6lztGkrkh6s3NegaECtFnGdQqWlWolylEJD5qGKh3yHJSy9b3k5XPC__vnCoRa6O3LBXNVHDqs_Z34OxPZm7egYtb3tgqC3NoERD9RvgWTizuOqAXIuuC5wJxRFu1tiYS0qVE-UhZ42t2_6_kn77bUxSkm51xw4GchUqW1y_JEkcWL4CNAk-GVxCcFMELIvAsmvEwF0kkkRsq1R9CnEooMlFCcmpgcP9dYwTf1Yh_R2Lx3mikTkKsfoCovh8MeR9iqPbiDisJeCbJWHpE92kKt2RdmKhTrROc0YHX5pk2nK_5I09v4_RudE4OgNUJ3YELXqOAlPxZM-18-pCvXYN62uschz7uF0rK27R7wVJhSIV76z-plplJnxk4iD4-PdS2MtmdqNXjgpnXiDfkN2TcqHofY5O_4HbrMa8ziCan4bJzyBc9euB7W2UBZYOF0WNcla56-28dHAxJwlKhXHszKWd8-WzQ0vSoAzZZVY3yLErY-90ONr2-mbmka4FLETgWcJ6B4kj2Vf97xzhQs6W8sr8PzSjMAR2tEJI6T0I0uIKLlp5_rG440_uExXSNfgZ6Q-mbTDZeiIlOT7AfZcskI0yRXxkkWhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=bJak475-ygva5pmvleqbWgidor8GOukNvViLIdy5NtTXZEx47Z85Hu0TbNc1n0dipe2mJkz3rSr6lztGkrkh6s3NegaECtFnGdQqWlWolylEJD5qGKh3yHJSy9b3k5XPC__vnCoRa6O3LBXNVHDqs_Z34OxPZm7egYtb3tgqC3NoERD9RvgWTizuOqAXIuuC5wJxRFu1tiYS0qVE-UhZ42t2_6_kn77bUxSkm51xw4GchUqW1y_JEkcWL4CNAk-GVxCcFMELIvAsmvEwF0kkkRsq1R9CnEooMlFCcmpgcP9dYwTf1Yh_R2Lx3mikTkKsfoCovh8MeR9iqPbiDisJeCbJWHpE92kKt2RdmKhTrROc0YHX5pk2nK_5I09v4_RudE4OgNUJ3YELXqOAlPxZM-18-pCvXYN62uschz7uF0rK27R7wVJhSIV76z-plplJnxk4iD4-PdS2MtmdqNXjgpnXiDfkN2TcqHofY5O_4HbrMa8ziCan4bJzyBc9euB7W2UBZYOF0WNcla56-28dHAxJwlKhXHszKWd8-WzQ0vSoAzZZVY3yLErY-90ONr2-mbmka4FLETgWcJ6B4kj2Vf97xzhQs6W8sr8PzSjMAR2tEJI6T0I0uIKLlp5_rG440_uExXSNfgZ6Q-mbTDZeiIlOT7AfZcskI0yRXxkkWhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نظر علی دایی درباره مافیای خودرو در ایران:  کجای جامعه مافیا ندارد که صنعت خودرو نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147252" target="_blank">📅 19:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم به نقل از منابع دیپلماتیک منطقه‌ای نوشت محمد بن‌سلمان از طریق آمریکا با اسرائیل تماس گرفته و خواستار دریافت اطلاعات و کمک‌های دیگر شده است
🔴
به نوشته این روزنامه، هدف این درخواست جلوگیری از بسته‌شدن تنگه باب‌ المندب توسط انصارالله بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147251" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJU3I8mmz14R82U5Ax2X8zMaEVIBddiG7s4AnEDC--q26GogLEHCaJ3kxNbKaadCJqv8it_7IeIZpYpUMLZX9gGtMbStDRhBAMxG73l6BTm1RSH3oxT5nr9LjcQf8f1OLamBZSISLrcsCdrl4Sl2xz_gQuJz3HP-ERBI9kdhrOYno2v6sFDatLLJd3WYv00JWdAIHN-5Yd3fT2uki-aIxLa06qsBw62EXVsVeRctur76CICOxjX8-AGAt4jPGG7LzLRvOnihRSQuX0VsrwWbxUNaDEqhQYKvsTb7e-VOLAWMOx42UdEI7QHM-5f6foBWul1SAOouO5QUHdJ6v0cSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: جنگنده‌های سعودی جزیره حنیش در یمن را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147250" target="_blank">📅 19:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع ارشد ایرانی:
نشست روز دوشنبه در عمان بخشی از برنامه ایران برای تقویت اعتماد میان کشورهای منطقه است
🔴
با این حال، توافق به معنای بازگشایی خودکار تنگه هرمز نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147249" target="_blank">📅 19:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOGT_h67-g5SDFmEwjZoQFwGTTLsb0FRUmGymemwjdqQqpwtEMOSkdJeSFTAzvM4KevbcMwdDH1QTdctmN3ho63hweWiF_Srd2HCsuAiyPzH31z-68d-6ZGT48fM14JeGYst6WKimsrhavXZ7d8FzdKYqhCTweptMJZwQb2Fx9guogRBQdJhtyEG-zg6TVCAVU08qRaA1-VxxZaLQgYlef46YEgZLlAdyCm06sAsKuvahOjozvlTGqEDy9FPYHRZr6d0ipeNeELXeukxG9c95c53Zl78Ys4jgcLpL-DvU1hdT2Q4OB7g2gtnl5h2mi54rmjCvhBZA0-Ef916you7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نقدعلی:
رژیم آمریکا رفتنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147248" target="_blank">📅 19:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6466153e9f.mp4?token=L1rcrrgHuIFsddLmGsZRgAzwK-agpEU5zhkdz0rBL_yxAPTl-i17TvqpGaaHbkDAr3c5Aj96uV2n8ZnmnC8ITRCP4vuV9LfnloV-dBTkmnwUPXgM9-KjPVz3Hy8b_5kraGiK-G2093-KvndHAiTc70JDZWjmeRE8IPEr53ofJ1LkMbfn0aL1UlVV4vGYcWR6xO35ubnVRsvHZFNpJ33Ez8VMoqvMncVkMO-M40AwO-8JFWNbTA392YXlcXkQ1Qi2CqJkkiAkF_kpzRFT5UxSnBbuHHuWJurFqQri7OGXGSv51u-e343hewYh_HCmXMzyKQeqir5isTwAzxrgnpib9jFNAbitYH8FUoEvqgGWgHgngf1kx8Nqc4Kx_9h2aVqHyYSucttM3ccxJaLNXxfTXuBqD2VrgfqN5hsFGFvP4_-GS1aq9iKOisUClOMqbldz8EM51hMxcnlKxOh_9KY-3e3DnRQfafF4zyTTjAqZBEvh29foRygzA5G0bJ5JHWaWXfLKoTqbljCee-DM7vEXwjxnTsh1OCjTzhGpca6Yxf3z0bLk9Ax9iyp-lZMzibn0WMUr0jgFvqB5FG4wj_7M0BCi5AwkUgBn6dEGwGFxF0eePgZsObo36GxRqLYYk_ajv2KdXR7TcLQa8p6KL6G1XWd2BbIjuMRZ3Bevg8R-u4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6466153e9f.mp4?token=L1rcrrgHuIFsddLmGsZRgAzwK-agpEU5zhkdz0rBL_yxAPTl-i17TvqpGaaHbkDAr3c5Aj96uV2n8ZnmnC8ITRCP4vuV9LfnloV-dBTkmnwUPXgM9-KjPVz3Hy8b_5kraGiK-G2093-KvndHAiTc70JDZWjmeRE8IPEr53ofJ1LkMbfn0aL1UlVV4vGYcWR6xO35ubnVRsvHZFNpJ33Ez8VMoqvMncVkMO-M40AwO-8JFWNbTA392YXlcXkQ1Qi2CqJkkiAkF_kpzRFT5UxSnBbuHHuWJurFqQri7OGXGSv51u-e343hewYh_HCmXMzyKQeqir5isTwAzxrgnpib9jFNAbitYH8FUoEvqgGWgHgngf1kx8Nqc4Kx_9h2aVqHyYSucttM3ccxJaLNXxfTXuBqD2VrgfqN5hsFGFvP4_-GS1aq9iKOisUClOMqbldz8EM51hMxcnlKxOh_9KY-3e3DnRQfafF4zyTTjAqZBEvh29foRygzA5G0bJ5JHWaWXfLKoTqbljCee-DM7vEXwjxnTsh1OCjTzhGpca6Yxf3z0bLk9Ax9iyp-lZMzibn0WMUr0jgFvqB5FG4wj_7M0BCi5AwkUgBn6dEGwGFxF0eePgZsObo36GxRqLYYk_ajv2KdXR7TcLQa8p6KL6G1XWd2BbIjuMRZ3Bevg8R-u4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:‌ با ولیعهد ابوظبی توافق کردیم به آینده نگاه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147247" target="_blank">📅 19:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کانال ۱۴ اسرائیل گفته ایران داره آماده آزمایش بمب اتم میشه  قبلش هم میخواد از npt خارج بشه!   البته ممکنه این بهونه حمله به تاسیسات کوه کلنگ باشه.  @AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147246" target="_blank">📅 19:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECbXGovs4yRKQOEJw4lhLiyE-mU310ZHHcQamwyKHbJ4SebDzy3sWYyzuHHi0gaA74_r8mQ9cb8nwuqU_adDS5NuSVq-M3wPcNx0ZkeibBtazYOJc2QKPK2mTWzUdyV59cWx2p_UM3Uvzcj1kXvKRU3MxD29b1fwEjWRVdv_q9A3AyMw-v9Y2JM_rDMqqVbqUgdtJiFQiEZF-bqK1YA3yDIQsaYy2JefJon2kF0xodNmHiRraSYAukxTvU9Pd32koadbk369QeJTlY8deu9L57IyPOrtRHMBXOnJoCzGgkk1KMpBnIjDKnHW9NzYzGwCBzudSX30xQx-Rqo5KTQCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر خوب/استاد خوش چشم که بخاطر تحلیل‌های کصشر و اشتباهش ممنوع التصویر شده بود از امشب مجدد به صداوسیما میره تا مجدد تفت بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147245" target="_blank">📅 19:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فارس: اگه جنگ بشه، جانفداها میفرستیم‌ جلو
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147244" target="_blank">📅 19:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94a010ef6.mp4?token=K6ziD4ru9E8kKCO5wchF13uf7HtD_VMug__q_TEbHRCv7P7FpYwrD0SLfl8XnBd6dxX6NpZDfO6QhUjg7tzEQyDGP0a91oSEiPsnzEnqMIRg2fBF0GxOqf1imjrX2nL5kNBSK2bqrM_SQe41uDoBqjz3Yx8KaYTuyd3NO-zudeSDeWmE9NkbkZyKxU_SsDqUdFAfhVYfjlHiNhAI3k0hrf9zxdYyQNYK4GIBfKbVVyxs2nQEK3IBOY_g0idoGFy-QB2_Zuh8tWrOhNVVCLwLPIVRZeiGUe90_kdVJNSzcsD_KYMgKDwyEjTqTruEfIFDACCZI1OaBU6kyOGBRlugVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94a010ef6.mp4?token=K6ziD4ru9E8kKCO5wchF13uf7HtD_VMug__q_TEbHRCv7P7FpYwrD0SLfl8XnBd6dxX6NpZDfO6QhUjg7tzEQyDGP0a91oSEiPsnzEnqMIRg2fBF0GxOqf1imjrX2nL5kNBSK2bqrM_SQe41uDoBqjz3Yx8KaYTuyd3NO-zudeSDeWmE9NkbkZyKxU_SsDqUdFAfhVYfjlHiNhAI3k0hrf9zxdYyQNYK4GIBfKbVVyxs2nQEK3IBOY_g0idoGFy-QB2_Zuh8tWrOhNVVCLwLPIVRZeiGUe90_kdVJNSzcsD_KYMgKDwyEjTqTruEfIFDACCZI1OaBU6kyOGBRlugVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رؤیت شده در شب نشینی‌ها؛ عرزشی‌ها شعارهایی علیه حسن روحانی دادن و گفتن «از آمریکا تو دل بکن، خیلی خطر داره حسن».
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/147243" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147241" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
محسن زنگنه، نماینده مجلس: من نماینده مجلس بی‌تعارف میگم ما رانت داریم؛ این مسائل قابل حل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147240" target="_blank">📅 18:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
👈
تسنیم: جانفداها اماده شن که قراره ببریمشون کنار نیروهای مسلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147239" target="_blank">📅 18:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مقامات جمهوری اسلامی به نیویورک تایمز:
🔴
ژنرال‌های تندرو، از جمله سرتیپ
سید مجید موسوی
، فرمانده نیروی هوافضای سپاه پاسداران، یک طرح جنگی مفصل را به شورای عالی امنیت ملی ارائه کردند.
🔴
این طرح خواستار گسترش حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه از سوی سپاه و گروه‌های متحد آن، به ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق بود.
🔴
رئیس‌جمهور مسعود پزشکیان و رئیس مجلس، قالیباف با این طرح مخالفت کردند و هشدار دادند که این طرح می‌تواند کشور را به یک جنگ بسیار بزرگ‌تر بکشاند، باعث افزایش حملات هوایی آمریکا شود و بحران اقتصادی این کشور را عمیق‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147238" target="_blank">📅 18:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1d14cafc.mp4?token=OcoPfBB6l9Tn_CE-la0-H4LBB7ZfdpwmyexhKrRjAxziZdSCrJi4dmgta0GyQGXi8DRyxGxkMDF5MQliNlc9Cpm_Q-NZWmpR3GuLbYHr5hmzBio5uGlwMP2ElOAU7UbJScx-rjKiS7YtIvmnzIVHaALx4yCFutMJOOXzBRCMhTbDJ-1DjoaxdS91fSqAwb28YQNm9G_YPiUjmfDDJdvFDHHHL4-KtvPidaf8J-xMaVD-Ev2ckC0O776w8GYkSD6gXpzHhU54JBZtrb17AIHl_V6JR1UHuCyWKYr4113MEnehFTd0ykkB-fKn-U7yip5SBDtHmOeeJreRBAOY1IXlaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1d14cafc.mp4?token=OcoPfBB6l9Tn_CE-la0-H4LBB7ZfdpwmyexhKrRjAxziZdSCrJi4dmgta0GyQGXi8DRyxGxkMDF5MQliNlc9Cpm_Q-NZWmpR3GuLbYHr5hmzBio5uGlwMP2ElOAU7UbJScx-rjKiS7YtIvmnzIVHaALx4yCFutMJOOXzBRCMhTbDJ-1DjoaxdS91fSqAwb28YQNm9G_YPiUjmfDDJdvFDHHHL4-KtvPidaf8J-xMaVD-Ev2ckC0O776w8GYkSD6gXpzHhU54JBZtrb17AIHl_V6JR1UHuCyWKYr4113MEnehFTd0ykkB-fKn-U7yip5SBDtHmOeeJreRBAOY1IXlaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: آمریکایی‌ها بارها گفتن با زدن تأسیسات ایران تونستن ظهور امام زمان رو عقب بندازن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147237" target="_blank">📅 18:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOXvCp8fVs7CW2EcJtbO0oOxvhPit26hWyxq1Uchm0dGtyitYQYrkNG0td6avMbOGF87_I33_Tt3zNP1e3l4knD6f2r0yLQpGmv5EaCMpFVIvA9r_P5JM8DhL0jvdX2M5WnLQF_k_FvwGr18ZbcMABF7rn6t7rzu5429g0ov-SOicUFqqvZOFMsd4ALnHN__8yzgmB77O0LoRB6WM490pkPlDAtL5w8mQk7vcwbE0NP1GJk75Rnj58kEZNZ_pAEWLZD4qUYcOsUySccpjk2bCT2Wnhs5HymM0Z4wj4qJGF7MSGaiSJcxCLJTQTK5S0edYu18UcCfcqdsz2Vd5nciuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIbpzWVwNytp-EBLWhsJjEB873jPvEZdFG2iQhonNVDio7WMzpyYwesGkDl6c_sHAUlfo9mBaCu-gSk0xt6eTMgT5ONqBhFUdqj5T-WYnxt5WFqkxhvkDmCZFPwdUjAsgWGEmTYw5xhzNaFdKNg2RnPtuWrpumSaW6fjuCBMXv0iAiyR25kHAfqdPPTEw4Jyb6Ema95sKrMGULtU7j8RicZOwqKqJiIbKFZfqMTRy6EWKYEIN47Wl8DJcgCvhnFrncwVJcStVW_pl6qtu0jFlRcJrXg2Wy9mJ0TRKB_7YEpXEbMG4Pru5Dt6BYFJN6uaiMq1jVVFrt0TYpkQBD3joA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahmc1SP6-cQ4tPaRAotgdwmQ4Ch-qLElM26tOsPxIRJgg7rdM6RJMRGLhCRD7_bPOjxx_L75hxP3qPO-plyLM7zBrlGvgzD1DHdaj7XFqB_grQMBB-A5SKIdgFLgiZlK6dJrQK8Il_VZlzpKqajxSqjHy4M4kNdEJT8UKXzvqZV2QUDjJK24lOofJNXkaatqKAW1HXRZAsgyOZQ2lYmTFB034o1chFUTXdUNqIb9rrQ0sMx52BB2i-_rIco8qNtxAT_RU8SeqrFCqjxF0gD5UM-SGEjjsu6XvlRcqWbT6TYjgyzleyUiPf4XBvmfeB6vtDZ43XHfnaf7keKsPfhULg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از حملات تازه‌ی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147234" target="_blank">📅 18:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10fc0802be.mp4?token=YZ0DPsxRIStCkAtut9knEr9rX9N3HjPChuMtigDPDVb8lVtUiXHwjfHWTgBd1MSIJ2XCY9ob7cmIHDqOEO91a-V7s-Is11_4wMqNu6iYr0-J32mvpCZympsXfR7GX1boa_Ue-4Xo1XvutvqvADsJo81mQQWt4hwkZWSDxR7FvU7UqH6Ej2m3MwxJNsMO2QsV57SEKaMe4EckmA5Fz5Y2z2txVPym7qzHRBVYw_j5JH488YppOBF_KCxgRFQweFtsKP3Y1uifJuX-opiUPuJKuNJVZLMnNLtDHhY0BYYeGp93pY-YqyaNNuFPw6NEF75tVkyQZkjKGtJs9hjC96J3xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10fc0802be.mp4?token=YZ0DPsxRIStCkAtut9knEr9rX9N3HjPChuMtigDPDVb8lVtUiXHwjfHWTgBd1MSIJ2XCY9ob7cmIHDqOEO91a-V7s-Is11_4wMqNu6iYr0-J32mvpCZympsXfR7GX1boa_Ue-4Xo1XvutvqvADsJo81mQQWt4hwkZWSDxR7FvU7UqH6Ej2m3MwxJNsMO2QsV57SEKaMe4EckmA5Fz5Y2z2txVPym7qzHRBVYw_j5JH488YppOBF_KCxgRFQweFtsKP3Y1uifJuX-opiUPuJKuNJVZLMnNLtDHhY0BYYeGp93pY-YqyaNNuFPw6NEF75tVkyQZkjKGtJs9hjC96J3xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمب‌افکن B-1B از پایگاه فرفورد بلند شد
🔴
یک بمب‌افکن B-1B لنسر از پایگاه هوایی فرفورد به پرواز دراومد. صدای غرش موتورش تو منطقه شنیده شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147233" target="_blank">📅 17:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
👈
تسنیم: جانفداها اماده شن که قراره ببریمشون کنار نیروهای مسلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147232" target="_blank">📅 17:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
پارسال میگفتن ماشین‌های نوشماره زیر یه میلیارد سهمیه ۱۵۰۰ و ۳۰۰۰ تومنی دارن  اگه ماشینی هست که زیر یک میلیارده سایپا و ایران خودرو یه افزایش قیمت بدن درست میشه
‼️
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147231" target="_blank">📅 17:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رسانه‌های غربی:
امروز قطار حامل مقام‌‌های اروپایی از جمله نخست‌وزیر آلمان با یک فروند پهپاد مورد حمله قرار گرفته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147230" target="_blank">📅 17:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee9bf5d0bf.mp4?token=Ttvh6cPPh55VoVMbwcUHpAPH8geK3kb2JMBA8f8sIxrVAzcjDJSvV2JcGpchtQJkaQ3_Zszsi35spU94ZT5aAaSXzQxGZdsZNmJo73mrlQ2k4FRInHJO1jA0t2LaXICXiQwcvtO5cr8SN8EO5oS2MNYc30pqfy6X7g36b8DdmpHuH0wr8RoMdtlqXNjbFG_gkEujM85IHMlAmZvJT5jTFizAVJ5VQbBzTusHrvuvJ8xlZOX-lC2-_8OZBbeVaHE5_uyUEeYzm3-q8gLKPPigZFRTqkcHoaT_UznvZItl8iKNmx2X2UO2pNzTRJ4tOP8yH5b-T8htUfTj9e142CjAeGtrLKbxtTHKq7xCYUk-r8Dde2U9PVhmcSUv3Wh9hUtyuM8vVFkez0arGA5FgaDW172NuzcQ5__WZTOWVvAd_oKfBIsmxI3rRPRFfUuUEF7pWk5KEm8wm_LPzssuYECFcH_SpcvdYTrS_zqhTGWqESO_7jnpVzD13J-12RomR2GVcbPHYDl0uA6-8tNZ_dzM_CD8KCI8AIFEe3--JzAn7cUXoiRQwI-vNFbPpqH2kz0eBlR6itO459LL6_R1E6XmG4Z73RrohCnjfnDjCvjarybeUityvbKyn19G4vVBy10fjbOCG4t8bi6ZC5F4OcZMkPD8FW-bloyFPJyv8x-ymng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee9bf5d0bf.mp4?token=Ttvh6cPPh55VoVMbwcUHpAPH8geK3kb2JMBA8f8sIxrVAzcjDJSvV2JcGpchtQJkaQ3_Zszsi35spU94ZT5aAaSXzQxGZdsZNmJo73mrlQ2k4FRInHJO1jA0t2LaXICXiQwcvtO5cr8SN8EO5oS2MNYc30pqfy6X7g36b8DdmpHuH0wr8RoMdtlqXNjbFG_gkEujM85IHMlAmZvJT5jTFizAVJ5VQbBzTusHrvuvJ8xlZOX-lC2-_8OZBbeVaHE5_uyUEeYzm3-q8gLKPPigZFRTqkcHoaT_UznvZItl8iKNmx2X2UO2pNzTRJ4tOP8yH5b-T8htUfTj9e142CjAeGtrLKbxtTHKq7xCYUk-r8Dde2U9PVhmcSUv3Wh9hUtyuM8vVFkez0arGA5FgaDW172NuzcQ5__WZTOWVvAd_oKfBIsmxI3rRPRFfUuUEF7pWk5KEm8wm_LPzssuYECFcH_SpcvdYTrS_zqhTGWqESO_7jnpVzD13J-12RomR2GVcbPHYDl0uA6-8tNZ_dzM_CD8KCI8AIFEe3--JzAn7cUXoiRQwI-vNFbPpqH2kz0eBlR6itO459LL6_R1E6XmG4Z73RrohCnjfnDjCvjarybeUityvbKyn19G4vVBy10fjbOCG4t8bi6ZC5F4OcZMkPD8FW-bloyFPJyv8x-ymng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
به نظرتون چه زمانی انتخابات دموکراتیک در ونزوئلا برگزار می‌شه؟
🔴
ترامپ
:
وقتی که آماده باشن. مردم ونزوئلا الان خیلی خوشحالن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147229" target="_blank">📅 17:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
واکنش ترامپ به نشست دوشنبه ایران و کشورهای عربی: برایم اهمیتی ندارد
خبرنگار:
🔴
نظر شما درباره دیدار کشورهای حوزه خلیج [فارس] با ایران چیست؟
ترامپ:
🔴
برایم اهمیتی ندارد. این به خودشان مربوط است. ما در نهایت از آنجا خارج خواهیم شد. مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147228" target="_blank">📅 17:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: رابطه فوق‌العاده‌ای با چین داریم
دونالد ترامپ، رئیس جمهور آمریکا:
🔴
به نظرم در سال‌های اخیر پکن با ما بسیار منصفانه رفتار کرده است.
🔴
ما رابطه فوق‌العاده‌ای داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147227" target="_blank">📅 17:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAsBTtfA63PYXDmESH44CrbDDNCdtn6q7Ky_7iFethRbwmt1FXfFOCroUJlF6p4VN8SLTeGoYerTG_qSMrZvPa0cNgI5-ArEjq6j1QMOkVxw9JIhWPIkax7IN0AGQ2oKObnjtHWLSJFDLd8MNsBgWmTenb-72-veOCZxuWrcG33zGMH426e1wUrLTLOwoP7tebQe_hsyzl6L1JL10qDcybV0kMi3iGy3E1eEMbugOSu7OUnAloJwY5hTwkgd_kFKIlqWgIcS232KpBtNUnxLLNZuX2i8WkmFV5qICjvcURk7gyZhCnRGgJ0Olq1Bnnl6xGcBP-QbhD_ij453ad1QRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی
‼️
👈
این پسره ماهان پارسال همین موقع گفته بود که شهریور ۱۴۰۵ دلار به ۲۳۰هزار و طلا به گرمی ۲۴میلیون میرسه و اون زمان همه مسخرش کردن اما دقیق گفت
😐
الانم یه تحلیل خیلی عجیب گفته
😐
👇
https://t.me/mahaneconomy
https://t.me/mahaneconomy</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/147226" target="_blank">📅 17:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: به نظر من، شما ایرلند شمالی و ایرلند را دارید.
🔴
به نظر من، یکی از بدیهیات این است: آن‌ها را با هم متحد کنید.
🔴
این فقط نظر من است، و البته، بسیاری از افراد با این نظر موافق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147225" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ:زلنسکی باید حمله به تأسیسات تولید و پالایش سوخت دیزل در روسیه را متوقف کند.
🔴
او باعث ایجاد کمبود سوخت دیزل شده است.
🔴
این وضعیت ناشی از خاورمیانه نیست؛ بلکه نتیجه آن چیزی است که میان روسیه و اوکراین در حال رخ دادن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147224" target="_blank">📅 16:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ
:
جنگ با ایران قبل یا بلافاصله پس از انتخابات میان‌دوره‌ای پایان خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147223" target="_blank">📅 16:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81d794a7c.mp4?token=SSSbWI7hcIRqAx0z8Qx7dwwRGDJQK_ZkKDl1wpq4FpIXSIAEhfoN1Y1PaNu3BrNQx8W6yh5hVNFTDCd8J-9kDiv7JSo9IGWntFBedfCvXTQ52-CXIGXDqUxVwdJq6VBka6wxeVlTIbNDR_eujlI4Cvq0cntN8vxpYvaHNmhVkkxkc46vQIDQ3oezV2gf_vaLxOf4diU3LXrE4m0iQQiH_4nYx_WW_BcxJGIyxQgDpKB8rcq1poKQ58ZhjmLpxb3JA8CY3NUTEnLMNNs2hmUcoy6YA0aD1UKBirlsSUKT9Noh8tz9wX6AkHBig7e4cBNKkIBktmMz4jiK2vWbID87AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81d794a7c.mp4?token=SSSbWI7hcIRqAx0z8Qx7dwwRGDJQK_ZkKDl1wpq4FpIXSIAEhfoN1Y1PaNu3BrNQx8W6yh5hVNFTDCd8J-9kDiv7JSo9IGWntFBedfCvXTQ52-CXIGXDqUxVwdJq6VBka6wxeVlTIbNDR_eujlI4Cvq0cntN8vxpYvaHNmhVkkxkc46vQIDQ3oezV2gf_vaLxOf4diU3LXrE4m0iQQiH_4nYx_WW_BcxJGIyxQgDpKB8rcq1poKQ58ZhjmLpxb3JA8CY3NUTEnLMNNs2hmUcoy6YA0aD1UKBirlsSUKT9Noh8tz9wX6AkHBig7e4cBNKkIBktmMz4jiK2vWbID87AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جرد کوشنر درباره غزه: اسرائیل این عملیات را در دوحه انجام داد، که یک کار فاجعه‌بار بود. این عملیات از نظر نظامی ناموفق بود و در نتیجه، اسرائیل به صورت جهانی منزوی شد.
🔴
ما از این وضعیت برای تحت فشار قرار دادن آن‌ها به منظور دستیابی به توافقی استفاده کردیم که اکنون، امروز، آن‌ها از آن بسیار راضی هستند.
🔴
در آن زمان، آن‌ها کمی نسبت به آنچه ما آن‌ها را به انجام آن تشویق می‌کردیم، احساس ناراحتی می‌کردند.
🔴
اما در نهایت، این موضوع برای آن‌ها و همچنین برای مردم غزه، بسیار سودمند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147222" target="_blank">📅 16:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد به هر قیمتی توافق کند، اما من توافقی را که بی‌نقص نباشد امضا نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147220" target="_blank">📅 16:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
🔴
وزیر خارجه ترکیه گفت سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147219" target="_blank">📅 16:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
واس: ولیعهد عربستان سعودی و نخست‌وزیر پاکستان در تماسی تلفنی درباره آخرین تحولات و تلاش‌ها برای کاهش تنش در منطقه گفت‌وگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147218" target="_blank">📅 16:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147217">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پزشکیان: با ولیعهد امارات گفتگوی خوبی داشتیم و قرار شد گذشته را کنار بگذاریم و آینده خوبی بسازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147217" target="_blank">📅 16:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da2aacdd5d.mp4?token=gxhiVIWXh-ZHqGJvAuGBWcCtyYMmj9KE0xXQoETHXL0Jgic86Wk9kxfbDhEosQcGM-b_HolKYo64Ybi3uZwSiRvm58d07kyZzu_8oE8aSwJ4xoO28mQRU0_2Qe5ya_wZ1oFSnjIQOiUrygegLtsxNy3SfwP_-CXS70hVpBl9XmrTUX_QVhhDm7pjVFblIM2QYRZPPyDCaR7Ca1iCyhm9xu2GJCj9n2q1zxR_13FmQg7qa-CNUvFdlMR6LIcMTHp4sYVKQwtmocHXQIvV4M0PQGsBCzU5g4e8NxePSHlTKuogQ1fIVECaf-6xL1dsH1XsdXSqi567LjsgNZ4yyEImPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da2aacdd5d.mp4?token=gxhiVIWXh-ZHqGJvAuGBWcCtyYMmj9KE0xXQoETHXL0Jgic86Wk9kxfbDhEosQcGM-b_HolKYo64Ybi3uZwSiRvm58d07kyZzu_8oE8aSwJ4xoO28mQRU0_2Qe5ya_wZ1oFSnjIQOiUrygegLtsxNy3SfwP_-CXS70hVpBl9XmrTUX_QVhhDm7pjVFblIM2QYRZPPyDCaR7Ca1iCyhm9xu2GJCj9n2q1zxR_13FmQg7qa-CNUvFdlMR6LIcMTHp4sYVKQwtmocHXQIvV4M0PQGsBCzU5g4e8NxePSHlTKuogQ1fIVECaf-6xL1dsH1XsdXSqi567LjsgNZ4yyEImPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: راه جدیدی در ارتباط ایران و هند خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147216" target="_blank">📅 16:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پزشکیان: وزیر اقتصاد با سران و وزرای اقتصادی اعضای بریکس جلسه داشت
🔴
گفتگوهای سازنده با بانک توسعه بریکس داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147215" target="_blank">📅 16:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رویترز به نقل از منابع: اگر عربستان ظرف چند روز خط لوله اصلی انتقال نفت خود به دریای سرخ را دوباره راه‌اندازی نکند، ذخایر نفتش برای صادرات به پایان خواهد رسید؛ در نتیجه ممکن است تا ۴ درصد از عرضه جهانی از بازار حذف شود
🔴
شاید تعمیر این خط لوله پنج تا شش هفته طول بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147214" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147211">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تنش‌های اخیر و اهرم باب‌المندب کار خودشونو کردن، تردد تو تنگه‌ی هرمز به شدت پایین اومده  دیروز فقط یه نفتکش از تنگه رد شده!
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/147211" target="_blank">📅 15:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147210">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مدیر سامانه هوشمند سوخت: خودروهای بالای یک میلیارد تومان مشمول بنزین ۳ و ۵ هزار تومانی نمی‌شوند و تنها ۱۱۰ لیتر بنزین با نرخ ۱۰ هزارتومان در کارت سوختشان شارژ می‌شود
🔴
پ.ن : مگه خودرو زیر یک میلیارد هم داریم الان ؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/147210" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147209">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuDjoEq5Psu-TfpBec2LpXz8t8D8slbZnviWUfoAeeZXm71qqca5XHAjDMj0i7X5UCrosEjmS_aC1athwpiVtM0X6-Ip6hHD0cmjEQqc4Dh4TqH0gk3Xamc12Q7hnMhdhAHyrskWe7msKy6QeB6Q9_bFhkPvxgt03BPH_qQ3pyDbQdJSbO3wNZZx3FzXBZhEnM43AorDr932ulyHK7IlhyjwfLFM_uC4tSeV0Cz6OEAeNmyW2y0U0XucIDn1ioVbZE7HZztEgQVBGEtLZsZB3CqZ7Wn6y39BW2ba9Hr1Pi1DAYlYns7T8FWRJ48tkIyXMoOOKbubWob36mONaK0Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهار سال پیش در چنین روزی، جاویدنام مهسا امینی، دختر پاک ایران زمین توسط مامورین گشت منحوس ارشاد به قتل رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147209" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147208">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
توی مشهد این همه معتاد یهو باهم از کمپ فرار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147208" target="_blank">📅 15:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cfbe5e94.mp4?token=FmeqiQ4zBKCnPDr6nnRyIb-3PwOa40Sa0jSax5nCNbZGdwfwoDeqXmpVke2SMvfIw6xWaKP_-fdAH6WA3_u6K1redWv1K6zCVEGTsoyhBv2HVyKERQkaV6wSvjQ5WgS1jPr1shxG3_jvEU8AOjndA7BzY2xcINOgzmsN7r7aksqJB2a2j5SEjLElbQscC550koZGUgQJiCUBLN3LFKgoXhgpVKYTnb_OvmmQT1RhEoGWKwz4t931o1t0eqPGkAvSS7GfDhwnCak-PMduQS9gpTYtij-CZ5uBvTbz-ssmo8l6DtcPifxJjXBofYpcT-8LR-_3Ts-hW7PDcz2V8ONPEw5HW0Kfx1AL2EJ8ihkLpteMYjn8r9fGm8u-mY1lXtljkmz03WlvLxkRCi-vZfKkwesa56dHBlKp4bAov0SkHKs6qf9cqGA_COKWt8ENWac20D-qvcpkg6O9G7FR46mL9qvwkyRplIU8Qs4-75AhJhLUV5b7AWCuRUkyfnme91RBZ2jXctRLAAJrQ2FEO6WA1inB1P96ovjLmRoia9i0DOFJSQxAyGfgWTmNBOkyAlZv1lmVJXjyLiSiKJMc7PmqdCTkukHN2xmMoCf7GTciFBGZC1tmM1-pUrRW-8IbPRvs-w9MFzLSoz1MLSBmgxBVSZZ0mixwYP1CnYiXWGFDQ-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cfbe5e94.mp4?token=FmeqiQ4zBKCnPDr6nnRyIb-3PwOa40Sa0jSax5nCNbZGdwfwoDeqXmpVke2SMvfIw6xWaKP_-fdAH6WA3_u6K1redWv1K6zCVEGTsoyhBv2HVyKERQkaV6wSvjQ5WgS1jPr1shxG3_jvEU8AOjndA7BzY2xcINOgzmsN7r7aksqJB2a2j5SEjLElbQscC550koZGUgQJiCUBLN3LFKgoXhgpVKYTnb_OvmmQT1RhEoGWKwz4t931o1t0eqPGkAvSS7GfDhwnCak-PMduQS9gpTYtij-CZ5uBvTbz-ssmo8l6DtcPifxJjXBofYpcT-8LR-_3Ts-hW7PDcz2V8ONPEw5HW0Kfx1AL2EJ8ihkLpteMYjn8r9fGm8u-mY1lXtljkmz03WlvLxkRCi-vZfKkwesa56dHBlKp4bAov0SkHKs6qf9cqGA_COKWt8ENWac20D-qvcpkg6O9G7FR46mL9qvwkyRplIU8Qs4-75AhJhLUV5b7AWCuRUkyfnme91RBZ2jXctRLAAJrQ2FEO6WA1inB1P96ovjLmRoia9i0DOFJSQxAyGfgWTmNBOkyAlZv1lmVJXjyLiSiKJMc7PmqdCTkukHN2xmMoCf7GTciFBGZC1tmM1-pUrRW-8IbPRvs-w9MFzLSoz1MLSBmgxBVSZZ0mixwYP1CnYiXWGFDQ-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ایرانی که امروز در نزدیکی جزیرۀ هنگام مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147207" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e83f6c2.mp4?token=DaHPvefh30WagVREzMVdzmliIzdfcKzhG8H9Pp5I2O2uCpeE_1EXs8565Wo9laB1hRjlN2H9y08IQyE3ujQdAI_VzQgs4TzAZOWlWsIJUAzhwyI4dnrLy3qdPSLKF_bhdmMFnPAw7GNoy_dzQU8qlPHtF6ul2HIcxQ2EuPU1Yril42rOuga_ZRMFrxBnqf5drIUG0NpfSvzUYFx4orDf1T9RKNEGwtQW8Q57b0FQRMuzhEXmC6t4AdaMaI1xTu1TbXuvqCJKz_hVrz5qcwRuSTpKGbXYeB0bR69dcAIFcrdj5yW0fbNZo78Af88n1vmJdMQgrJ-E12tem452gNicHgFDoG_rGDiEHuQsT-3WczZIcxBSFZc17icBlL_ipgjndpw_ph5LDiLFRWOwDeBC21GwRgswLuI30YYxGnpf8zgft3m8yHdAaudWvW67XlT5mO0LiJy93EmW1UIWiHHC5iWEv_BCgOsOAHwQSVLMQGorVkCbTCL0ZL-JLT6o0DzXE94uvZPt429S-6PT6P5HXf7CWbne-X_garkKpQE9d8n02LKWm7ZzzOjCu6VOtu2qd7OlLwqV7Myvov145tNs2dTYRX95K9Thwnc1s1H_6VSxl9TR_CquW5jVmZITYYZCDkELriRpRTpqpMiiCtspblL8Ifgh706UG_jxjcVR3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e83f6c2.mp4?token=DaHPvefh30WagVREzMVdzmliIzdfcKzhG8H9Pp5I2O2uCpeE_1EXs8565Wo9laB1hRjlN2H9y08IQyE3ujQdAI_VzQgs4TzAZOWlWsIJUAzhwyI4dnrLy3qdPSLKF_bhdmMFnPAw7GNoy_dzQU8qlPHtF6ul2HIcxQ2EuPU1Yril42rOuga_ZRMFrxBnqf5drIUG0NpfSvzUYFx4orDf1T9RKNEGwtQW8Q57b0FQRMuzhEXmC6t4AdaMaI1xTu1TbXuvqCJKz_hVrz5qcwRuSTpKGbXYeB0bR69dcAIFcrdj5yW0fbNZo78Af88n1vmJdMQgrJ-E12tem452gNicHgFDoG_rGDiEHuQsT-3WczZIcxBSFZc17icBlL_ipgjndpw_ph5LDiLFRWOwDeBC21GwRgswLuI30YYxGnpf8zgft3m8yHdAaudWvW67XlT5mO0LiJy93EmW1UIWiHHC5iWEv_BCgOsOAHwQSVLMQGorVkCbTCL0ZL-JLT6o0DzXE94uvZPt429S-6PT6P5HXf7CWbne-X_garkKpQE9d8n02LKWm7ZzzOjCu6VOtu2qd7OlLwqV7Myvov145tNs2dTYRX95K9Thwnc1s1H_6VSxl9TR_CquW5jVmZITYYZCDkELriRpRTpqpMiiCtspblL8Ifgh706UG_jxjcVR3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان : «آنها به مردمی حمله می‌کنند که هیچ ارتباطی با جنگ ندارند و حالا همان مردم را نیز تحریم می‌کنند.
🔴
اصلاً اینها انسان هستند؟ چرا با ما می‌جنگند؟
ما
چه کرده‌ایم
؟
🔴
این یک فاجعه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147206" target="_blank">📅 15:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147205">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWVyUbumdg0EKpClCRUVeKg6gvNa1yIv3O0cq6riJrZXqoBkGGN6y8oqy8s7gKIasDPUzYyoHTPf9_kRFjImEyXHsLAx14Jc_IQ6Ed-Ch7v4C_NGp5nOq7IybHf6KqtjKRC3q_sfbfGIFu1rmZVA75hC5xdMnwjym_VZaYghx_8UAWakb9wYXYlZfluDBBNCnKv5k51tFXNWjDGC47NS69Ai5ASMwDMFb2twc9Ijq6nra3o8GleOgiVWGC71nVEfjABAMGBZtMhsi6f9B_hEy6OQOyd9S6QIyWHdvEIIOgQywIKr0Y19cqaPEspk0ncV-jipIZA_SjNwTGxjoKsWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش ۹۷ درصدی تردد نفتکش‌ها در تنگه هرمز؛ تنها یک نفتکش روز جمعه از این آبراه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147205" target="_blank">📅 15:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره:
تهران نشست مسقط را اقدامی مثبت برای بازسازی اعتماد با کشورهای همسایه می‌داند.
🔴
حضور عراق نیز مهم است، هرچند یکی از کشورها دیدگاهی مبنی بر عدم مشارکت عراق در این نشست داشته است.
🔴
این نشست می‌تواند زمینه‌ای برای بازسازی ترتیبات امنیتی در منطقه باشد؛ اما اکنون نگاه‌ها به واشنگتن، واکنش آن و مسائل دیگر دوخته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147204" target="_blank">📅 15:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دلار (تتر) از دیروز ۸ هزار تومن ریزش داشته
‼️
امیدوارم همینجوری که هر روز بالا میره، هر روز بیاد پایین
🔴
با این حال الان روی ۲۳۰ معامله میشه
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147203" target="_blank">📅 15:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ordgySIsvXK1iPnkKw7pFaUq80sl8Bow7-mCglFziR1krTHJJdTmF4-PCOhoseOkhxhizi7FB0sosFfYGuyE0FDw-nk4QM9be0gzA6Sl2gg1eUb_Pn73hdIQlJ_cycdcDT1-uYgGomaggNgF3f8DoAMjZIpOFL3_QYxua4sZd5YAqzf8TPI_9ZMxTXzB4as1tEceYBiCdKWPq46sDHOWR9a6BIyWDP-LVb16sv-3dtPfQbp8ME9GbfE7DYd85q4BxeaFW0NpgzXjDvgvMp-I77T-oTrJm8OyJq7dvdHqByLbhPN83exLxuTUdY-SzkY1wQ8LHbu9a8KGvNdehYvqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / به گزارش روزنامه تلگراف، نخست‌وزیران ایرلند شمالی، اسکاتلند و ولز قصد دارند در نشست مشترک خود در کاردیف، یک یادداشت تفاهم امضا کنند تا بتوانند درخواست برگزاری همه‌پرسی برای استقلال را مطرح کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147202" target="_blank">📅 14:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147201">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تلویزیون سوریه: نیروهای اسرائیلی در حال پیشروی به سمت منطقه جورا اللوز در نزدیکی تل بت‌الورده در محدوده بیت جِن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147201" target="_blank">📅 14:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b0f7822b.mov?token=AuGQ-VyIC5SPy0ghFrqrvLOqT0eqE8aNvfRrMqPTy0ITZXHKjNqQnsiLta7Tfr_HJ9tgngPVZj9PgbKuWK9cAbr4DnQnuyM7ltdzlVbvwenEC59hsFNu-UemyL2jIysQRCsWkHU4L3hwtE39wVJyxXGWlGdE9ChFirdjqkx9va6De0AQK1JJ1OHV9lC9DFC2yeXYFwQ6iJFo_nfvHkTWUmCZLs7zeKcswOrNpVoEQOQBNLJA-SiBvBsbschNaXIhQf1n1NYYz1ThWo1VyCiZyDOZQkQjfeQlFCkdY5V7nahZjETBPgfZaUSWxA726DkIsXkltGDN5qTAIImLYUpOsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b0f7822b.mov?token=AuGQ-VyIC5SPy0ghFrqrvLOqT0eqE8aNvfRrMqPTy0ITZXHKjNqQnsiLta7Tfr_HJ9tgngPVZj9PgbKuWK9cAbr4DnQnuyM7ltdzlVbvwenEC59hsFNu-UemyL2jIysQRCsWkHU4L3hwtE39wVJyxXGWlGdE9ChFirdjqkx9va6De0AQK1JJ1OHV9lC9DFC2yeXYFwQ6iJFo_nfvHkTWUmCZLs7zeKcswOrNpVoEQOQBNLJA-SiBvBsbschNaXIhQf1n1NYYz1ThWo1VyCiZyDOZQkQjfeQlFCkdY5V7nahZjETBPgfZaUSWxA726DkIsXkltGDN5qTAIImLYUpOsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه: در حال کار کردن برای رفع موانع موجود برای پیوستن به بانک توسعه نوین هستیم
🔴
برخی کشورها مانع هستند که در حال رایزنی‌های لازم  هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147200" target="_blank">📅 14:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q43jMidw7Do0xF5DLVgcn3CpUmXh2goXg98gvmbfCkK9DfyiNcL8gfXuTSd3N2F_Qa4BwUKv0Aml8pUrIHdAxTaCrNgxRCPltNMQ5pLll62HNBxzaI-TeSxR_NgEZDb5PsSBh-h3cnnZ56pVKcB2non27wML4tl_WC485FYvtt4Tfy6JXAkbj3Kqy0GayK9kVNvg4YihJEbHx5BwKcUCjA7RBOPSHxAGpxq3klB6Gp8M9WKxt2HXyrXmtk1bcuQ2xM-Zx806jdf_G8JdnNsLLd27d5vkUERMsyv_Mrdcg9zrfdtYQLVHIkq_GCfuEZg4EevKfP3ye-zLIduOn1rZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید دیگری از
گلوله‌باران اسرائیل علیه بیت جِن
در حومه غربی دمشق منتشر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147199" target="_blank">📅 14:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
به گزارش فایننشال تایمز، ایران امسال از روسیه خواسته پهپادهای پیشرفته «گران» را برای استفاده در درگیری با اسرائیل و آمریکا در اختیارش قرار دهد.
🔴
این ادعا به نقل از مقام‌های امنیتی غربی و یک فرد نزدیک به کرملین مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147198" target="_blank">📅 14:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3yjwOH4RLo382R43xvd9dAKcE8MBO111wvf8389afUnK6MmP45opV0IQqDUrb3VdsS2rXvD7TBhGE-u0YSWthnWQc3Ppd8i9_2OnP1h7MbU8Bs0T4JdtB021zT-hwMwMT1qcmfKFNblOvZC5xha_S0nv23i4hHvEXLCzFCBECQSf0y9RVgB8_d9xO0CNowUJVq9yaf9C_BMdWrNCFWqh4L-x_Im09keoFLFvF3YZcxq1YIuLZIr4ZQMM0GQ52-by0Kj6frzShKkzxv24E6whHU1Xw-4V1oWazdqju249FJQBUAIIvCBSk8991Wgo3DHLomOXJvEVVkK-lq8d_G6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DE_GSM4hO1jpuUlHzgK_VwFRK-5Al3nZZVxi6vRqebTdsz4UYuPobzEhwCem8p1Gc7hA5OG4dM8H8cMZeqFJiawqwi9GTc8jP7acVmDGhKI2aeZTpk0EHaHdOQRk-2WqYtoSwecdBjKiKrefUncfnxc2mTx2IX1lyBrmN60F_BOMgs4AxrosGwUJhvh8ja3fewGqBoEAuCVJBTnnc51iXDukkLyDUo9aF1V92qTZXhTillg8Vp-MhPMXEjwmBLFFhNvmF2WNmxQv4MQIBYxPptOKwZ6sPGCT9yFUJMeihQP8SjJKQ7CvB2LAof9bP4tJMpVWxruwqOvEImLvtfgiPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دود غلیظی از پالایشگاه یِنبوی عربستان سعودی به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147196" target="_blank">📅 14:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نیروهای وفادار به عربستان سعودی اعلام کردند که در درگیری‌های اخیر در سواحل غربی با ارتش یمن، بیش از 500 نفر از نیروهایشان کشته و حدود 1500 نفر دیگر مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147195" target="_blank">📅 14:04 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
