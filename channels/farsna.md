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
<img src="https://cdn4.telesco.pe/file/sl5UpMLm81y6kv7AHq9QHlox1CpkEfJF524PG54iSc0KvhQ5gDcRx6I7fGHureZQxprnrsRXv3I_mhIfwwdP5HlxS1dWaWeALB8DQ6i4FPvwKpN0hX0w8IkuLhIvm4uK-oqZYsDow_8uuInZmsjb_0lK6Tf8Ka34BVeK9XtH74hS2SC5f2IGbEJ8DWEF5alqKw7F_1WzOKEStowPm26w1uZ-FkflL9NNVBzBaKFBT04j5FNkmFHL0PZnbiNwqio3ZDDLvlTOFuqhVvxvGYiBORDJku4yWwyuMmFFX2aheM4c2OVvfBMJZm-t3O_gNxrx_j7sKOQ8RN46FE11q0Wq0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-439451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYvucUi44fRoh0R0Q4uMZrbdf34HSkwR_7jw_3YICJxuGCv0Ig86Pokz-MAHoM9XftyqDAzWvwoGaYC30WyBpyzg9XnqifCRzHLwhXWcWpl5jS_rPsFiHoVNnQte1Ci9hIH3Tiur2s46tXiybNouiD2SXKvAGJVt2rrNC8avDuj7kWvuc_6q6YEpwvYM533pxPi73pVhFYlmQ-s50S2wqNKFLoOV2v78Mor3YuNxWlYu-yclMRnU-HlobtpMT_lwaQFn0YTPwsPPVu3zhh8DRq1NjynuU_579_yzPX7KIGC52g3aznSxhRGrXhXpLXpLwsRlRm3ZfwGiF1437mylEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ بمباران جنوب لبنان، صدور هشدار تخلیه برای شهر النبطیه
🔹
ارتش اسرائیل با صدور هشدار جدید، از ساکنان شهر النبطیه در جنوب لبنان خواست این شهر را تخلیه کنند و به مناطق شمال رود الزهرانی در ۴۰ کیلومتری مرز فلسطین اشغالی بروند.
🔹
النبطیه که حدود ۱۵ هزار نفر جمعیت دارد، در ماه‌های اخیر چندین‌بار هدف هشدارهای تخلیه و حملات ارتش اسرائیل قرار گرفته و بخش زیادی از ساکنان آن پیش‌تر از منطقه خارج شده‌اند.
🔹
پس از صدور این هشدار، مناطق اطراف النبطیه از جمله کفرصیر، یحمر الشقیف، زوطر الشرقیه و همچنین بخش‌هایی از مرکز شهر هدف حملات هوایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/farsna/439451" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGGYukZ6Bik-3Dq1EgDbMWKtCu0ESjSF1aGzjPRg1z6IndL7oUOpA6_OzhpdoF1O1J6mW7KQQ24M9-4_EGDXHv8VgYNB3RDAirwaqXd4vSpVC0KgiyuJJRSqZBVHPjDZ2tGTBk4sKNt3W0083cR-0rqg-IJoQl8B9pNpqb6_Hao-hLOzjxDiUB3tiMpmFfQaD4IZoHSdk_fFdEw8FyCMOwS5Slp7ULT2vpWiyyrxm0kCii6jygknhsfYJ1agYmGb3ygYx7oqXTZrxTS-QZXcm_9OYzO6z8jP-TtIYWIblqF8l0zmKrH2rzcuDnzUhs6fq2urWhtKheKDwOk5VrRrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم اشغالگر: ما به لبنان حمله می‌کنیم ولی حزب‌الله نباید پاسخ بدهد
🔹
درحالی‌که صهیونیست‌ها درحال حمله به لبنان هستند، وزیر جنگ رژیم اشغالگر امروز گفته در ازای این حملات، حزب‌الله حق ندارد شهرک‌های شمال فلسطین اشغالی را موشک‌باران کند.
🔹
او همچنین تهدید کرد که در صورت ادامه حملات موشکی و پهپادی حزب‌الله ضاحیۀ جنوبی بیروت هدف قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/439450" target="_blank">📅 16:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439449">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a261d285.mp4?token=b74NvDJgLA-_dII8xvzUiIOeo_YZ6qtdFZ2OCKf50DInTEWSvFc3ORmIzRcc264iRAfnba4CPry0oDydwi1ltlktRmidu3PcCUE1hMsTpi8qQXjEllDjcbGusaBwmuBOp2Mbt1XLkLw83OU6unhQ4rpVeLEOpHyA4y69_4HtQWY88kppGOC38tEoR5nMexeLG0G1IdvpaNITUYEF80ChjqNYwSeaLICuTOhRqPT0P7R866678nlAuZ3vuWwd_mc9nDASRyZGWd7_TKQFXIWntnBGewMbYTUQqa1oebYNFS_HItb9-oGboIiGUyfupPmKcf-rP7BjFADrjXhYEe1YZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a261d285.mp4?token=b74NvDJgLA-_dII8xvzUiIOeo_YZ6qtdFZ2OCKf50DInTEWSvFc3ORmIzRcc264iRAfnba4CPry0oDydwi1ltlktRmidu3PcCUE1hMsTpi8qQXjEllDjcbGusaBwmuBOp2Mbt1XLkLw83OU6unhQ4rpVeLEOpHyA4y69_4HtQWY88kppGOC38tEoR5nMexeLG0G1IdvpaNITUYEF80ChjqNYwSeaLICuTOhRqPT0P7R866678nlAuZ3vuWwd_mc9nDASRyZGWd7_TKQFXIWntnBGewMbYTUQqa1oebYNFS_HItb9-oGboIiGUyfupPmKcf-rP7BjFADrjXhYEe1YZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس شبکه افق: حزب‌الله سایه‌ای از ایران است
🔹
اگر کارشان با حزب‌الله تمام شود دوباره سراغ ایران می‌آیند.
@Farsna</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/439449" target="_blank">📅 16:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جزئیات جدید از مراسم تشییع رهبر شهید انقلاب
🔹
معاون فرهنگی شهردار تهران اعلام کرد برای بدرقۀ پیکر «امام شهید» ۳ روز برنامه‌ریزی شده تا مردم بتوانند در مراسم حضور پیدا کنند و پیش‌بینی شده مراسم تشییع در تهران دست‌کم ۲۴ ساعت به طول بینجامد.
🔹
به‌گفتۀ او تهران، قم و مشهد میزبانان قطعی مراسم تشییع خواهند بود و محل برگزاری مراسم تهران به‌زودی نهایی و اعلام می‌شود؛ مصلی تهران و حرم امام خمینی(ره) از گزینه‌های مطرح هستند.
🔹
به‎‌گفتۀ معاون شهردار تهران، احتمال برگزاری مراسم در روزهای پایانی ذی‌الحجه و آغاز ماه محرم وجود دارد.
🔹
همچنین برای میزبانی جمعیت گسترده، هماهنگی‌هایی میان کلان‌شهرها و شهرهای اطراف تهران انجام شده و برنامه‌ریزی‌ها برای حضور بیش از ۱۵ تا ۲۰ میلیون نفر در پایتخت درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/439448" target="_blank">📅 16:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaGMK5GHv8XwsKrwV_6xp0OKQKrsx7YmZGvTW3XOEvU_zaJJwmD_GWyFA465uTO6UUZsK4v8fSfenSjFm7LucJjb7eSdiYSuO-X4k9PycMDk6WHfoUmBXWJsIbjKYycHgUCQ05SQiwWLiw36VzCztSk_mujsj8ViQTorApPUQysjRv9gSFG4YJOJqxfLTeWJ5o_I5raAt3TSlwYYnIidaIBLV93ZIZkXjkMrgE3Fvqxx9BdYKGZJ1eBvQU2AAXn5TfFqz1l1YLFwgjhINUzsfPyDP8eutkH9IorbsKkvxXWKnuSX8yIpg0ERUADIa-aF5B07Ewd392MX90veHGuOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: حداقل ۱۰ دانشمند آمریکایی کشته یا ناپدید شده‌اند  سلسله این حوادث از سال ۲۰۲۳ آغاز شد:
🔸
مایکل دیوید هیکس: دانشمند ۵۹ ساله آزمایشگاه پیش‌رانش جت ناسا (JPL) که در جولای ۲۰۲۳ درگذشت.
🔸
رانک مایوالد و مونیکا رضا: دو متخصص دیگر از JPL؛ مایوالد در سال…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/439447" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439444">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ بعد از عقب‌نشینی از حمایتش از حملات اسرائیل به لبنان مدعی شد که مذاکرات با ایران با سرعت بالایی ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/439444" target="_blank">📅 16:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439443">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
حزب‌الله: شهرک‌های نهاریا، کرمئیل، صفد و کریات شمونه در شمال فلسطین را هدف قرار دادیم  @Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/439443" target="_blank">📅 16:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffifl3m-hiAQMxePwErVTSpRaok6TKcGNOPHlQUfnbjgxVIDtphhlgri_Je4Sj281YP9DsbPo1eAKDo94SIAb66WLuJ0EyUUnyNuVQWoQDMHjkVWQy8ssHegRj312Br7TKHs_RAkL5nkmZFwBlg8vpP02EW-G0baJpyHmAt5w4YDg0OIUmvxf6Uws1Bx-jtuuchSPu05xxpGg4yodDSZp0VGYqArIrLCc0utIpDplFVP0sQFsOQe39_zICj2t0REMoi_Ku0fZbrLnHjFjBfqMOTFLiDXvpMELsDUtq6kc_n2Mk8RanqunxuSE-IVdVpyE2a7RkMqNvy5pFlU38TLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی ۲۰۲۶ با قوانین تازه از راه می‌رسد
فیفا چند تغییر مهم را برای مسابقات جام جهانی ۲۰۲۶ در نظر گرفته است:
🔸
پوشاندن دهان با دست، بازو یا پیراهن هنگام بحث و درگیری با سایر بازیکنان یا داور، می‌تواند با کارت قرمز همراه شود.
🔸
اوت باید ظرف ۵ ثانیه پرتاب شود؛ درغیراین‌صورت توپ به تیم حریف واگذار خواهد شد.
🔸
بازیکن تعویض‌شده فقط ۱۰ ثانیه فرصت دارد زمین را ترک کند؛ در صورت تأخیر، بازیکن جانشین با یک دقیقه تأخیر اجازۀ ورود پیدا می‌کند.
🔸
در هر نیمه یک وقفه ۳ دقیقه‌ای برای نوشیدن آب (حدود دقیقه ۲۲) در نظر گرفته شده است.
🔸
هنگام مداوای دروازه‌بان در زمین، بازیکنان اجازه ندارند کنار زمین بروند و از مربیان دستور تاکتیکی دریافت کنند.
🔸
سرمربیان می‌توانند در زمان توقف بازی از لپ‌تاپ و تجهیزات الکترونیکی برای انتقال نکات تاکتیکی استفاده کنند، اما بازیکنان باید داخل زمین بمانند.
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/439441" target="_blank">📅 16:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed35b17646.mp4?token=WhHgRgS2nMqBZa57O2yUUaFIt9Qj--KHXXRwAUqvWF49rnWh7ZY8Raz-LJ15BPIwAgmHBF-ta35nQVMZ6mSwWdJDm6je3mn2rXuXC2HcBPFfC6t-ozvlx1nGiSFWvJJxiOWS3LmTgAW10-P8dAwZhaMBg19QvWta9IIFC3AEeESQ3hgKtQlJqkYPjPgdoEYmTwvbn8NrzTdUVpHaPdECxRiHB6woLKqtqHx5n-pn0KOe-fp_8dGjs0mR3BlSNLbOH34KfPfYpMRGZn-dxAkh_rYgHForI_vPTgSeE2K8GRu9xfvFi7m0UA7rGCnMMHOXHHVkM2LCfju3pgOjYdn8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed35b17646.mp4?token=WhHgRgS2nMqBZa57O2yUUaFIt9Qj--KHXXRwAUqvWF49rnWh7ZY8Raz-LJ15BPIwAgmHBF-ta35nQVMZ6mSwWdJDm6je3mn2rXuXC2HcBPFfC6t-ozvlx1nGiSFWvJJxiOWS3LmTgAW10-P8dAwZhaMBg19QvWta9IIFC3AEeESQ3hgKtQlJqkYPjPgdoEYmTwvbn8NrzTdUVpHaPdECxRiHB6woLKqtqHx5n-pn0KOe-fp_8dGjs0mR3BlSNLbOH34KfPfYpMRGZn-dxAkh_rYgHForI_vPTgSeE2K8GRu9xfvFi7m0UA7rGCnMMHOXHHVkM2LCfju3pgOjYdn8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: اسرائیل در لبنان حزب‌الله را تک گیر آورده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/439440" target="_blank">📅 16:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3bbfbd0de.mp4?token=VDUylnWocudR4oOYjSVXeGhvsohZ4FSO6G7tgLHhhVmF7jY3C-qvy8n0s57Um1jdu9Dn3bs60mRFYTJ_JdF-6VOQEpvZVDMS1VryDw5fNU_iDDGQI9ds89mJ3K-t6POzHzlPQh1WqCIUkeAnnp2jFdLlioATE50gjcxEhqTXfOLCa6amTjscE4LNsrB6aaZpkfS6H3QNGDx7h6Mm3lPQsuPGxn5H2zy4FXnibnpJdTCEakfavQb8Y8JdqPots-Lj7QpfapAWzBJa-r-EbRbelQ4Xjoudoo6eIfKNqwZ566nHX5gPykhZMVBK81ZdlsZO3bp50A-T10vL--_yYbgoQq9dgDKom5bb39cXp8OAHH8-PfMM0y2OA5GHJ0z2Jg41cAbgO2B4dTQjL1ye4ZKKaUmrh9t5DT2i4iOOlwSaDfCKAXX-hgIHjm6Pf3aOoDfa4ulFDOj3zuklAq6un2B2XP7826KuHKf8j7h8iUM7eLJvTbf87hBnYr5Or6iJl6bMHuCSdEuaBkKuNeTdgtguwK1_vhDHyIGI9zx4UoqBnOn5yjIyMVA85E_YbAwqxjAdQtRT0YsnpX6T7AFCTl0GJcB8fK10scleKPO4hSWYIRFDddByijzUv7TTkg-4Zt78Fk-gpJ3in_qsySfDfQhRiTCtly6JRav-tbtj1VYsy2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3bbfbd0de.mp4?token=VDUylnWocudR4oOYjSVXeGhvsohZ4FSO6G7tgLHhhVmF7jY3C-qvy8n0s57Um1jdu9Dn3bs60mRFYTJ_JdF-6VOQEpvZVDMS1VryDw5fNU_iDDGQI9ds89mJ3K-t6POzHzlPQh1WqCIUkeAnnp2jFdLlioATE50gjcxEhqTXfOLCa6amTjscE4LNsrB6aaZpkfS6H3QNGDx7h6Mm3lPQsuPGxn5H2zy4FXnibnpJdTCEakfavQb8Y8JdqPots-Lj7QpfapAWzBJa-r-EbRbelQ4Xjoudoo6eIfKNqwZ566nHX5gPykhZMVBK81ZdlsZO3bp50A-T10vL--_yYbgoQq9dgDKom5bb39cXp8OAHH8-PfMM0y2OA5GHJ0z2Jg41cAbgO2B4dTQjL1ye4ZKKaUmrh9t5DT2i4iOOlwSaDfCKAXX-hgIHjm6Pf3aOoDfa4ulFDOj3zuklAq6un2B2XP7826KuHKf8j7h8iUM7eLJvTbf87hBnYr5Or6iJl6bMHuCSdEuaBkKuNeTdgtguwK1_vhDHyIGI9zx4UoqBnOn5yjIyMVA85E_YbAwqxjAdQtRT0YsnpX6T7AFCTl0GJcB8fK10scleKPO4hSWYIRFDddByijzUv7TTkg-4Zt78Fk-gpJ3in_qsySfDfQhRiTCtly6JRav-tbtj1VYsy2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله: شهرک‌های نهاریا، کرمئیل، صفد و کریات شمونه در شمال فلسطین را هدف قرار دادیم
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/439439" target="_blank">📅 16:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439438">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b21e6e7cf.mp4?token=W5YFPaTyOeCog3LMcrempoBqN4jw5LX6RQKxzUM3B25Kc_E1iQCx-Iy3VFGPOG36JXcd03t3x4mdSJ7lXYIPv8ImzZFFpXT8mMYD8cAYkGRDxdu1srunzt03YpzKZEwW-nG-_1-_-DVaqV8X7drtDlp3_YDPUUmw5_IOGOScJ7ohT4lx_wRb2LD5DaUS9Syf6svjWosBBlvdxerlMlep8MybjhByfv2PzdjVEDh0czXfF-d3eqNoDAIZiIrMJTW08t2XZi-XK5pTXydzxq673dFQIeAKG1WL27-97KvbJlDumYfN8w0iTRLIxiIG-yKAwD5mpXzXGomm42HX5OYcV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b21e6e7cf.mp4?token=W5YFPaTyOeCog3LMcrempoBqN4jw5LX6RQKxzUM3B25Kc_E1iQCx-Iy3VFGPOG36JXcd03t3x4mdSJ7lXYIPv8ImzZFFpXT8mMYD8cAYkGRDxdu1srunzt03YpzKZEwW-nG-_1-_-DVaqV8X7drtDlp3_YDPUUmw5_IOGOScJ7ohT4lx_wRb2LD5DaUS9Syf6svjWosBBlvdxerlMlep8MybjhByfv2PzdjVEDh0czXfF-d3eqNoDAIZiIrMJTW08t2XZi-XK5pTXydzxq673dFQIeAKG1WL27-97KvbJlDumYfN8w0iTRLIxiIG-yKAwD5mpXzXGomm42HX5OYcV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شست‌وشوی ضریح علوی در آستانۀ عید غدیر
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/439438" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=uQ7xBCuIiTE2rFwZtVu76U27pmQIHIplDj9GB1DYwPxBCbRRLzLpo2QL_UOArN1XKXi4c9pLIWSLAWbRCt9QADIe3wR5vqKd_XpTf72Q1TVF_ytmhQ0CxofhR-cyQ9RFQL1CVhtlaspzEZeYshqe1rTXAJCYjruqDGA3VKexB04OVFnnNjdsUJdfMgwB_wRnXdnb10JFlAm5_7FnNPX0JMkck5to9zI-pCN4XObDOYwtxwkiSw40O5eIQs7EIlRxJnqJnLnCXhLSUamVy4_j3owv7pqhwP9pzQmocVx9TMb-7YoANwF2YhpfPbhXA_c9gaNM7Z2gz87HsHPBldAQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=uQ7xBCuIiTE2rFwZtVu76U27pmQIHIplDj9GB1DYwPxBCbRRLzLpo2QL_UOArN1XKXi4c9pLIWSLAWbRCt9QADIe3wR5vqKd_XpTf72Q1TVF_ytmhQ0CxofhR-cyQ9RFQL1CVhtlaspzEZeYshqe1rTXAJCYjruqDGA3VKexB04OVFnnNjdsUJdfMgwB_wRnXdnb10JFlAm5_7FnNPX0JMkck5to9zI-pCN4XObDOYwtxwkiSw40O5eIQs7EIlRxJnqJnLnCXhLSUamVy4_j3owv7pqhwP9pzQmocVx9TMb-7YoANwF2YhpfPbhXA_c9gaNM7Z2gz87HsHPBldAQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدور مجوز عبور از تنگۀ هرمز در هر ساعت از شبانه‌روز
🔹
مالکان و ناخدایان کشتی‌ها از سراسر جهان می‌توانند در هر زمان شبانه‌روز با مراجعه به سامانۀ نهاد مدیریت آبراهۀ خلیج فارس، درخواست عبور از تنگۀ هرمز دهند.
🔹
سامانه درخواست‌ها را بررسی کرده و در صورت تأیید،…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/439437" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656021c50d.mp4?token=lotbBDr1OyR0PjVp9GUAOYxxV-kTY_JhEawe_blTNCdanXi_bLkjxWgxyYdtx5qXL4AOavvJxqE_tCkI5jgE5dG46d5FwZApgOL2GbiUmU637s0o8-EOlKZlf3-hIdkJwxYUlsaQbuyLUUKbByTH_ZZ9-FjqPO7tKRTg1An-3-QORh2ubMC_szoSfmxG_N2vxOV4RKqqEAV9C_wo5oR3NBiUNFYLkH6Hgq283EYAjeu1VVN64o0CJ3F3XzcWuZ5g0IvK1vnzIxVGwfp1FqHr0rhjHCLJcv_2VAqVDmr1LEYCD3Y4NwqCqGPVVUbhztY29iJnBc-RaV-lhPNF6UQRSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656021c50d.mp4?token=lotbBDr1OyR0PjVp9GUAOYxxV-kTY_JhEawe_blTNCdanXi_bLkjxWgxyYdtx5qXL4AOavvJxqE_tCkI5jgE5dG46d5FwZApgOL2GbiUmU637s0o8-EOlKZlf3-hIdkJwxYUlsaQbuyLUUKbByTH_ZZ9-FjqPO7tKRTg1An-3-QORh2ubMC_szoSfmxG_N2vxOV4RKqqEAV9C_wo5oR3NBiUNFYLkH6Hgq283EYAjeu1VVN64o0CJ3F3XzcWuZ5g0IvK1vnzIxVGwfp1FqHr0rhjHCLJcv_2VAqVDmr1LEYCD3Y4NwqCqGPVVUbhztY29iJnBc-RaV-lhPNF6UQRSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو شورای‌عالی انقلاب‌ فرهنگی: امسال تغییری در تأثیر معدل بر کنکور ایجاد نمی‌شود
🔹
سعیدرضا عاملی: طبق ضوابطی که از قبل اعلام کردیم، هر تغییری در قاعده سازمان سنجش باید از یک‌سال قبل اعلام شود، بنابراین امسال تغییری در مصوبه نداریم و همان اثر قطعی معدل یازدهم…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/439436" target="_blank">📅 15:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313373d690.mp4?token=iCxqHSVvyvMT4FVXUTRsERHaTUqX5GDXwm-JJvKeBVl_eWfPcee3Gt0N5WR_vcduauyCt_JSu9EmKiomzLuO6XPaUgrfrooiOQ_NAz3iSvBZ6b8Hnr3340CD8Bjhk38N5plqfA7MzV-FhV_Cr3bGfFcBIsyJKt59589T8OP5LnHe9hSI8fGG6mn0HdYsjkzOsdERusxUyOINyWkXm-11cU3u5BKHLxhWazHYsalWeZCnlQFCSjJjGisF7vfWYRBMgeCZohrhUSTdniRttP9OKHbtVkgdvxxhDgwWlX7C9ecZWAl3u9WTNSinne-szJrnLTzXPaY7NedIoLiuP1vSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313373d690.mp4?token=iCxqHSVvyvMT4FVXUTRsERHaTUqX5GDXwm-JJvKeBVl_eWfPcee3Gt0N5WR_vcduauyCt_JSu9EmKiomzLuO6XPaUgrfrooiOQ_NAz3iSvBZ6b8Hnr3340CD8Bjhk38N5plqfA7MzV-FhV_Cr3bGfFcBIsyJKt59589T8OP5LnHe9hSI8fGG6mn0HdYsjkzOsdERusxUyOINyWkXm-11cU3u5BKHLxhWazHYsalWeZCnlQFCSjJjGisF7vfWYRBMgeCZohrhUSTdniRttP9OKHbtVkgdvxxhDgwWlX7C9ecZWAl3u9WTNSinne-szJrnLTzXPaY7NedIoLiuP1vSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی شهرداری تهران: مترو و بی‌آرتی تا زمان تعیین‌تکلیف توسط شورای شهر، رایگان می‌ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/439435" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f707799294.mp4?token=o3bme2jBzDjZeA7BY0E6JCjTvh1kVXoySXJ4woXTTWuUseYSMSz7C4vY-zkdPVOeYuGEEMPN7rXDmKEVj1EqxaJd5zsc2hKxDgoxf_bgoNegE7XJ_TePO-jrO6N4-dUC_-w6HuQJ0KimgdY4fRoUbbwsfykRmJ7hGhbNqobax-TvJ2NefsutGGXg118Ea0qaWsJJOUBlU1iivDWSzC-xfbh0-4Ma2XabiKj2UB8a076iCbODi54lxzsp2InijaGKAknh8qrMTgWNyUs91aiPRyG2HTPVOfSlp2qhDO_ed8X9IEENvyM_binRI8j5Q6TvYqaDZ2cu407aisawAVSFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f707799294.mp4?token=o3bme2jBzDjZeA7BY0E6JCjTvh1kVXoySXJ4woXTTWuUseYSMSz7C4vY-zkdPVOeYuGEEMPN7rXDmKEVj1EqxaJd5zsc2hKxDgoxf_bgoNegE7XJ_TePO-jrO6N4-dUC_-w6HuQJ0KimgdY4fRoUbbwsfykRmJ7hGhbNqobax-TvJ2NefsutGGXg118Ea0qaWsJJOUBlU1iivDWSzC-xfbh0-4Ma2XabiKj2UB8a076iCbODi54lxzsp2InijaGKAknh8qrMTgWNyUs91aiPRyG2HTPVOfSlp2qhDO_ed8X9IEENvyM_binRI8j5Q6TvYqaDZ2cu407aisawAVSFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: باورش برایم سخت است که اسرائیل از مناطق اشغال‌شدۀ لبنان با تفاهم خارج شود.  @Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/439434" target="_blank">📅 15:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPHxhcZwPT1WnbNydwxNPzHY-2ou1MFBGoBpd9ZVcqKepjQpgmBDGEuzhhcEqAVeCA5RFdBiGTafGXlvSfGsx-dHpE6kpdYLQ2vq4eVlE9YkVfbU8Ly3-ECxvPw6C_9y7y0Yw_fAZL-Bw-KhoO8d-hjQ8nbxYOl2pU47iqzKsCO7NDF0iEGNTOlfbxKKsBRSr_6pkb5R7E8AGIzSZ-pMTJ3hLHTW4xkRhtJwl3IshhHLk74_it3F3TnaTwpkbVa5F6SfnFDbipq-hx9sNYRxSwlVDAs2WGeBx1U6rO9b-zF67vEbEYqBETg7d7mORupdu5jUjIka2KqyIjWBwtuPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۴۰۰ میلیون تومانی برای نصب نیروگاه خورشیدی خانگی
🔹
رئیس ساتبا از پرداخت ۴۰۰ میلیون تومان تسهیلات به شهروندان برای احداث نیروگاه‌های خورشیدی ۵ کیلوواتی در پشت‌بام منازل خبر داد.
🔹
این طرح با هدف توسعه انرژی‌های تجدیدپذیر و کاهش ناترازی برق اجرا می‌شود و منابع آن از محل صندوق توسعه ملی تأمین خواهد شد.
🔹
همچنین قرار است نیروگاه‌های خورشیدی ۵ کیلوواتی در ۱۲ هزار مدرسۀ کشور نصب شود تا علاوه بر تولید برق، منبع درآمدی پایدار برای مدارس ایجاد کند.
عکس: مهدی قربانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/439433" target="_blank">📅 15:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXI0jGOJd6VWH2yvAdWOsXrYTezdsDFFZTR6kx1UinD6zPuTUUldxP94CQxxzTJHZ_NP6DJn2DLcodu-Hsvvwujv_HKHIILIrH6PVIBW9TNC2c27cfbHhThe5oGsgFoybUx9Xkxr-iTF0pk87lRYuAU0p3UoGiZRUE2v_0GipnBjxdGhrcgGL7SgWj9DtHEv8ANCxQujGYKbnsuLaon4sNzyCRoPC1l9qZ8lfTcqoZSdFjgfNKpm4hk6v8deJCAYOO7OYR2OBv40ck24HgDm4IySeFXtviLzzh-yvO7-MwprT9-blvUL0472sfO1TIPxfBeEnVYiAFr527fzNGP3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس آمریکایی‌ها از شروع دوباره درگیری‌ها
🔹
روزنامه واشنگتن پست به نقل از منابع آگاه نوشته که مقامات نظامی آمریکا در چندین منطقه جهان، «سطح حفاظت» از نیروها را از بیم از سرگیری درگیری‌ها افزایش داده‌اند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/439432" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjfMVEJ7gO58QE69-FhNmrXz1XiYbbrPBm53THgkpQqLrEN346LohOt5A0qO_7IXUCiZOqs3LE5xBMgzqA3K5VAczsUp-o7qwdruQ_n8enACrLB66rG7ogdSHyxTGmweF9Oil_ACAo_jPNRYSDY9KZR-Za1AQYpZPqPEDOw0uxkr1khZWaYZaoB9NqQ-jvQ98PBxAFmEpV6q_EWSLtSIiYeNo-vaTrWBWGN3MOO5Hv-Keshxq_Xvx0vl8A-lQnwTUaalCKg85Q0AkR1itbJ9Sa-SsG5ji-xqB5wHNK4I6o7c2JD_95qzXRVtZfuhHgZVeSel7fl_eQChLORebGjLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود خودروهای آفرود به جنگل‌‌های هیرکانی آمل ممنوع شد
🔹
دادستان آمل: هرگونه تردد وسایل نقلیهٔ آفرود در جاده‌های خاکی، مسیر‌های فرعی و حریم رودخانه‌های منتهی به جنگل‌های هیرکانی مطلقاً ممنوع است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/439431" target="_blank">📅 15:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46b032224.mp4?token=fwYcKgCPX3GfP23fJwLm2F4MeQ2p1ULn8AZDQBueKBw2NHAIAe7KUoSQFhlN2DKTzy6eSVJ_IWVLCgb0-fVf7NLVQy30QHHZgTFllw5KDeOyx8wq08NfsMNruTuVrThZ-R059N06t_3VXJeC7EFsWYC52tLphtJUTTj519G5iunV153pT6Yt5ed6UgY3ONw6JfDUQd3wIh442QPwie1PsuuBeRun7DXJmwlgCTHKXER4HYr2igl2KVJNZOrYZDb2l6zVXmRD74cDRQfrheUSPUepS-133DUAUsIpJr_OEBHezEwYd8_lchBe5q10l4wdfI2tAQbSx56w2MH7mdf0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46b032224.mp4?token=fwYcKgCPX3GfP23fJwLm2F4MeQ2p1ULn8AZDQBueKBw2NHAIAe7KUoSQFhlN2DKTzy6eSVJ_IWVLCgb0-fVf7NLVQy30QHHZgTFllw5KDeOyx8wq08NfsMNruTuVrThZ-R059N06t_3VXJeC7EFsWYC52tLphtJUTTj519G5iunV153pT6Yt5ed6UgY3ONw6JfDUQd3wIh442QPwie1PsuuBeRun7DXJmwlgCTHKXER4HYr2igl2KVJNZOrYZDb2l6zVXmRD74cDRQfrheUSPUepS-133DUAUsIpJr_OEBHezEwYd8_lchBe5q10l4wdfI2tAQbSx56w2MH7mdf0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: باورش برایم سخت است که اسرائیل از مناطق اشغال‌شدۀ لبنان با تفاهم خارج شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/439430" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5d386dc0.mp4?token=tMxFBD7A58KXFvYPxk8jyA-kBBpNcdzwbZRBzXchK2vSUESE3gXV_HONlDsWWBaeFqWOP6jdTXxRZUGIhH6ixnlLUr8oxfUWSBQsFnc8qb9s1-4CIYywieduxSI8pVCrCPsE5pLMWPHw66mFaqAdM1K63Jt6B4PbcLemRbf5gEPOXDt3D_PTdJPNrCSPgP5TiLwXTfy_UsJo6I7v5-TjBMR_hoMxCm2Q8LMIy569-g1YsaRy5_qbuD7tKMPEPAKeMkQ9iZWZ6k_tW4reTgwSb9-EpMuWZH7FdbsrGcVM0CD7uFRRMj2-A2aORgYt-R88XIlcpxv1lyXXJ26EVaWkJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5d386dc0.mp4?token=tMxFBD7A58KXFvYPxk8jyA-kBBpNcdzwbZRBzXchK2vSUESE3gXV_HONlDsWWBaeFqWOP6jdTXxRZUGIhH6ixnlLUr8oxfUWSBQsFnc8qb9s1-4CIYywieduxSI8pVCrCPsE5pLMWPHw66mFaqAdM1K63Jt6B4PbcLemRbf5gEPOXDt3D_PTdJPNrCSPgP5TiLwXTfy_UsJo6I7v5-TjBMR_hoMxCm2Q8LMIy569-g1YsaRy5_qbuD7tKMPEPAKeMkQ9iZWZ6k_tW4reTgwSb9-EpMuWZH7FdbsrGcVM0CD7uFRRMj2-A2aORgYt-R88XIlcpxv1lyXXJ26EVaWkJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب اقتدار دفاعی ایران در سرزمین وحی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/439429" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439427">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_IMump6K6363OYXoY3ZWB2SHkmx1fYcdh5OecKo_NNHIKg09GiC0KdLm3nvKz-tpqpCaLHYCer4irjuLDe0rE1W6mx9aRLJ6LZ5GUEon_OANVj0-JHGnGfjhSR97ATBAbVaFoO8noJbYXTHNF0cf14mHhIM5Sn1ttRgYaVhXlThT9QhTLjdl_XRwG4bkPHw3XODbsoCFuIFIUpNAT07g83iB93r3Xgs8l-DLVG04NwXBP-AbsxgfnPjII3wfUfSLcyMcqkfZBzyKCa5ZsEJmD1yENBNWODKg_nXpiPdm2r1PDaw753pvn89nedlyYcW7FEqst6MrqZdUus7Xc9DYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس بنیاد ملی گندم‌کاران: ۵۰ درصد پول گندم‌کاران این هفته پرداخت می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/439427" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTDvYoBFIM0cZsOeQ4HkFVVldHwaH83mwxvJlkfkYFqkJoKmdCEYycU47gWxvFCu1Ej21dArIQE1DXq6Eur93kdxay_6WU9bMUT9VeZKBVEEha5qmm9EA_g3BC4EwhRi7sxLK_4cTDdJdNFP100AGsfPts1i0HMws3UXt6nt5hwEzV3qojOs-2IlbZUk1Tqa_TKLSx3Bqwpx6U0LfBqMCBCHCDOyt9C44JatMJZZ_3mD8N3FCJ0mHLGH8kxorXRdVEW8_WvySxN0bCtQGXClQcH2lWhvhWtVgDcZMgBJ6jGLopmx4oKSf8aquwHT46c3pD9zfFZrMQF_Q13rvkKWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارهٔ پیراهن بازیکنان ایران در جام جهانی
مشخص شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/439426" target="_blank">📅 15:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3647677f2f.mp4?token=TsCK5l1iKjLaptsO2Gmaandae9_K0KSpbxD9SgHN4yYCRxPTNK0WtJjWMd5eAJtdyXxcvUjKegD-P35N1ytE-mltF-evDrXCcEGs1lBIpkDyHM6pSybvIPm8ZqXB44GL8LY50SDPNIbYlgX7YQ8RAsIkS9wTcyqktrMPzTc50JXcuxXACrcm3yK9pnDWF9X-58BuJ9GMbbAPwaZLdJ310x61y3nb7CMVx42KGyeEuUDooLWLnKwUkWNRLtyzcxe-Pqn0trL53L14X0uIlYBL4PmhtprsE6PxaQqTliPedNEtF02kSlR7rkcQKfuIrUaLrz9rkp898a1vPP4754JyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3647677f2f.mp4?token=TsCK5l1iKjLaptsO2Gmaandae9_K0KSpbxD9SgHN4yYCRxPTNK0WtJjWMd5eAJtdyXxcvUjKegD-P35N1ytE-mltF-evDrXCcEGs1lBIpkDyHM6pSybvIPm8ZqXB44GL8LY50SDPNIbYlgX7YQ8RAsIkS9wTcyqktrMPzTc50JXcuxXACrcm3yK9pnDWF9X-58BuJ9GMbbAPwaZLdJ310x61y3nb7CMVx42KGyeEuUDooLWLnKwUkWNRLtyzcxe-Pqn0trL53L14X0uIlYBL4PmhtprsE6PxaQqTliPedNEtF02kSlR7rkcQKfuIrUaLrz9rkp898a1vPP4754JyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در حین پخش برنامه آشپزی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/439425" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaehc8cm20RZa5i7jU9n0pCrlwEaGppOdFmtugZXJzN0NwqR6YOz-M-PBXP6Fy_J2OuFKytyfJp5bgoM6CS02dgbrsQRi0rgvLFPS2XP38Fe4q6D3P_QdjKOwFv1QRvnJUcD8Gwdk04uV1QdD27HxHBWV2V12uIk935IzMh3lpX5XAWzL2ME0Y6Cj7NwxNey8QA8frxR3o7lPgeUQaLwUg3Y-LnNwsaqv3viqGk9SMMcvrEoUWLcSIWOm00Zd2yRJxj1D4D2_uTwsGiSkxQgD7nBKOHouxGP0-kKbBG4OzuDcvVPe4LZ8YIqIXXaVZYx0LTtPbuxil4lBwrqaC79LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس آمریکایی‌ها از شروع دوباره درگیری‌ها
🔹
روزنامه واشنگتن پست به نقل از منابع آگاه نوشته که مقامات نظامی آمریکا در چندین منطقه جهان، «سطح حفاظت» از نیروها را از بیم از سرگیری درگیری‌ها افزایش داده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/439424" target="_blank">📅 15:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439423">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef0Dz2hM5iiPbEQWWc8uYqSdxXGn74m18ADM1qKP32ju3srw7pJghwTdVC0i3VIri3hIbr9FQVCLyiX2HTkk7Rks1F8ZY-wPzJoEHZpZ81-ald7i0w1MN4FpPQXapYV1gp5-o3q9vme1wLigfBs-FmKW8g9y9HFW1Ri2nuYkEbfYitpi4PAweYCoLDrwLil9EIDQHvX9AUKjX6Iu54GxY9d0oyoc_YwJFW4FluHZ3o9XOAfPA0q6gDtPr2nlTML_5TbDYBi-Ie8LkxZylor6ON1rIdG13WEwAzfEJzRIOJFNWrQAJiIpTzOGfc6MQsSdQW4ehkCTg9Hhw8Xuv_KeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر المپیکی تکواندو زیر تیغ جراحی
رفت
🔹
مبینا نعمت‌زاده، عضو تیم ملی تکواندوی بانوان کشورمان و دارندهٔ مدال برنز المپیک و طلای امیدهای جهان، به‌دلیل آسیب‌دیدگی از ناحیهٔ رباط صلیبی زانو، امروز تحت عمل جراحی قرار گرفت.
🔹
نعمت‌زاده پس از طی مراحل اولیهٔ درمان و دوران نقاهت، برنامه‌های توانبخشی و بازگشت به میادین را زیر نظر کادر پزشکی و فنی تیم ملی آغاز خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/439423" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439422">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67532ff2c.mp4?token=raqQRNLT3oiAL6TN4kFGM8FCHrhytKx3NCSyTkbik1oaide_m-Vjx5Kh5v4r1qQJ488BKENZVsbWlB5TYZlkTrNhylXs25lwCEvDUfb2-HIHz0m5D5JZRh88tkeb-lC-ofX50hKTN37ITRo6HgRvpYykCFuS71zQfBWcA9iZN4L-DR6St7IjyOSP9fAed0SH9LtV6sa-HOfFHr2vwPDo7eGWID5hvvRj7dvDsBbSUtZQsYYh-7EXYE4pEtZNJp7eFDrFVv88HS7F70iIH8m2X1A3JWCzeDzp8glwMreoYPQQRmlOCLvucrU5-xEsHotCvFJ-BRVx91MU9RFZjPecJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67532ff2c.mp4?token=raqQRNLT3oiAL6TN4kFGM8FCHrhytKx3NCSyTkbik1oaide_m-Vjx5Kh5v4r1qQJ488BKENZVsbWlB5TYZlkTrNhylXs25lwCEvDUfb2-HIHz0m5D5JZRh88tkeb-lC-ofX50hKTN37ITRo6HgRvpYykCFuS71zQfBWcA9iZN4L-DR6St7IjyOSP9fAed0SH9LtV6sa-HOfFHr2vwPDo7eGWID5hvvRj7dvDsBbSUtZQsYYh-7EXYE4pEtZNJp7eFDrFVv88HS7F70iIH8m2X1A3JWCzeDzp8glwMreoYPQQRmlOCLvucrU5-xEsHotCvFJ-BRVx91MU9RFZjPecJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاینده‌رود به اصفهان نزدیک شد
🔹
مدیریت بحران استانداری اصفهان: با افزایش خروجی سد زاینده‌رود در روز گذشته آب در مسیر رودخانه جریان یافته است.
🔹
باتوجه‌به خشکی بستر رودخانه در ۱۱ ماه گذشته انتظار می‌رود در ۲۴ ساعت آینده آب به اصفهان برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/439422" target="_blank">📅 14:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439421">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlVvBtTqsEdKYChDOLuc20LR_ByxHajiS1yjhThrTtMBPQodrYAh-VFyTLQTAk2RMrfP0WXgBdbOtoNhKqUMWjbMP0XafsXCe3fsg5Q7BhXDCdvjHmfJc_HyMXI0ZfuZlYDQWtkYBhDBG-XbuZQ2B2iPo2hBcUnS-FjGTThQpBT4W--x5cJAb5LvVpmCGh_Td6o-xisyy130nH1r1RM5j-KPZD83SqGHVWDNoyHwpTexSLhmu5eiE7T7xXIzg3QT_uPIUEgP6v1BUok80J-CaNaDXX12B5TkcD4wxYeYlp2xrX6HvpJ1mXnJd3ve2ltTk07YHC0bAX7sy5bXZIGpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نبض زندگی در دریاچهٔ ارومیه به قبادلو رسید
🔸
بندر قبادلو در شهرستان عجب‌شیر، یکی از جنوبی‌ترین نقاط دریاچهٔ ارومیه در استان آذربایجان‌شرقی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/439421" target="_blank">📅 14:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439420">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3644805d8e.mp4?token=F3DJM1pgz0vysu0LdtttGN3M-mZRJR0VSUiJFJIROTTLTcTVON6ErqwOiHXTEIZiAi2n4ZOQOn95HQwNRFsy5LWDyk15DrimgItMoKJRR2mGVlnN5MbrCdvOjs_XDE5oV_94VuHWjX3NabIdhv8jdgB8iP9hQIw5IaNCkR5L8mXmrumbnJmmMtdhKYsvoc0itgTBiQ7ELBnEhMdXbOpxiE-40UfWN7m0L-nadh3NqaKqEZMwo0h1PfeSiOVPn2EyphvXyoDmwfEcb9zCFrOMkFUcFK7MbpQCMmc6JeZndslssjhYLSfu_SlnUcoDPXg186MDKqnVb0Z6lsrIR3l6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3644805d8e.mp4?token=F3DJM1pgz0vysu0LdtttGN3M-mZRJR0VSUiJFJIROTTLTcTVON6ErqwOiHXTEIZiAi2n4ZOQOn95HQwNRFsy5LWDyk15DrimgItMoKJRR2mGVlnN5MbrCdvOjs_XDE5oV_94VuHWjX3NabIdhv8jdgB8iP9hQIw5IaNCkR5L8mXmrumbnJmmMtdhKYsvoc0itgTBiQ7ELBnEhMdXbOpxiE-40UfWN7m0L-nadh3NqaKqEZMwo0h1PfeSiOVPn2EyphvXyoDmwfEcb9zCFrOMkFUcFK7MbpQCMmc6JeZndslssjhYLSfu_SlnUcoDPXg186MDKqnVb0Z6lsrIR3l6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: از دولت درخواست کرده‌ایم کارکنان آموزش‌وپرورش شرکتی شوند و حقوق خود را مستقیم دریافت کنند
.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/439420" target="_blank">📅 14:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439419">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e6e55bfc.mp4?token=T9CzvJNf1HKTQCG7M_sVeh0JPre605gt-RlHeYArxgKEQuA-csNIpjzqQFy0Kg4MZSeHi1DhjJA5RWDHBvT_iTNRXnMnDutDrhQcCY9Uh5pAK7SUqqeVsxBuXZdFW6WLMLFBvgsrBZutCQSAPa_DKqVfzBc0YOpQGFVrmBS6OrZwJUBaxC4qCTgqyW2JfQx-MZH9sZ-G1KjTvCFh4n9X5qHXeFzCW1p6IqLzYC10kx2Y-Hl_qFUeOnoUEoVgQ3BLDN-XYobzrVmzizxiulihgGzmLi3r9SQLxWapqM7nkkGsCtbxmgciRxN1_7Ase9IY5iBQGwCgsAEmvcF3pWI6eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e6e55bfc.mp4?token=T9CzvJNf1HKTQCG7M_sVeh0JPre605gt-RlHeYArxgKEQuA-csNIpjzqQFy0Kg4MZSeHi1DhjJA5RWDHBvT_iTNRXnMnDutDrhQcCY9Uh5pAK7SUqqeVsxBuXZdFW6WLMLFBvgsrBZutCQSAPa_DKqVfzBc0YOpQGFVrmBS6OrZwJUBaxC4qCTgqyW2JfQx-MZH9sZ-G1KjTvCFh4n9X5qHXeFzCW1p6IqLzYC10kx2Y-Hl_qFUeOnoUEoVgQ3BLDN-XYobzrVmzizxiulihgGzmLi3r9SQLxWapqM7nkkGsCtbxmgciRxN1_7Ase9IY5iBQGwCgsAEmvcF3pWI6eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔹
وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/439419" target="_blank">📅 14:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439418">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1-Orjb4gRfOm4iEj1T_eeHVCMLTPcK2rs-gGBzK2yvtvD19wlIT2jFplPQ6opL5ZASeDxVR0a1Go85g4h3Vq6DZOJC-a3HUFiUNpdk6gz6oYnGeHjxQ2wXhwRIN8rlcph3IIZqqijgUZDbXsMiPGeQvq0s3aB29_EC1-FuTrVyeBg4zuhHPPqo5kHL-mZqVb-OWcodzzjTyX2lecpPUgix-8_XifwdGtyK5zy0TeaFsh3vjMHxSR0ueLvaslXGGxh-_g6ud_lVAC9xHrQ4uSXwwPTw1IqPmWIBSMxSQvnAT7qTUypCqh41-e1021nBCv1YzNORc6L66UCJ9eVFjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقف کارت‌به‌کارت روزانه ۱۵ میلیون تومان شد
🔹
طبق اعلام بانک مرکزی سقف کارت‌به‌کارت بین‌بانکی در شبکه شتاب از ۱۰ به ۱۵ میلیون تومان در روز افزایش یافت و سقف خرید با کارت بانکی به ۴۰۰ میلیون تومان رسیده است.
🔹
همچنین سقف انتقال وجه غیرحضوری حساب‌های غیرتجاری به ۳۰۰ میلیون تومان و حساب‌های تجاری به یک میلیارد تومان افزایش یافت.
🔹
سقف انتقال آنی(پل) هم ۱۰۰ میلیون تومان تعیین شد و انتقال غیرحضوری برای افراد ۱۲ تا ۱۸ سال به ۳۰ میلیون تومان رسیده است.
🔹
خرید با کارت برای افراد ۱۲ تا ۱۸ سال و افراد محجور تا سقف ۱۰۰ میلیون تومان امکان‌پذیر خواهد بود.
🔸
سقف انتقال‌وجه پایا و ساتنا همچنان ۲۰۰ میلیون تومان است.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/439418" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439417">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90929c1a8.mp4?token=sZGrWDpKcKKNc_TL2YDlzB5L1rQhih6uZCTZMCuNOwvVNgHcF5OPBgs2KI7RblnJd7y1kbU_qHQOnvNoG-UmZSQTsZ-Nhns8GyOS0fObl0bThwOcjkiR0COaa74n5lYEq6X3zmvYFDrbomYTrNWflD8Cah02GRavIDsG0hOAR5n1DwczDU4Wbs7mFvLGWQo9Cv56CadiQ5fQHsHQAP84mAMMOxIH89XOE6u22YsY6sKr1jMpi49FXJlXoU1keArW05sdiCqAWWEZXMhuPKsDK4vhdc8AW5sXddTswN0weZl7GlGeQw5hLkkyw4sdde13djRTNHP1iikx_VWN62K4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90929c1a8.mp4?token=sZGrWDpKcKKNc_TL2YDlzB5L1rQhih6uZCTZMCuNOwvVNgHcF5OPBgs2KI7RblnJd7y1kbU_qHQOnvNoG-UmZSQTsZ-Nhns8GyOS0fObl0bThwOcjkiR0COaa74n5lYEq6X3zmvYFDrbomYTrNWflD8Cah02GRavIDsG0hOAR5n1DwczDU4Wbs7mFvLGWQo9Cv56CadiQ5fQHsHQAP84mAMMOxIH89XOE6u22YsY6sKr1jMpi49FXJlXoU1keArW05sdiCqAWWEZXMhuPKsDK4vhdc8AW5sXddTswN0weZl7GlGeQw5hLkkyw4sdde13djRTNHP1iikx_VWN62K4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
عبور ۲۴ کشتی با اجازهٔ سپاه از تنگهٔ هرمز
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۴ کشتی پس‌از دریافت مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/439417" target="_blank">📅 14:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439416">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9O6OVxSbwRO7dc1I3lC_btu5pXapQvQK44jPVcMtRivOr7SuqSkyrD12A-h6RXUzEtJa6eAl9SGcOeMtqxTkAhoek1yPsSk7YU-YkLlMCQxch4dN5NqFPPcedry_cb-XLCVNNyi0vOPyY6N2RAQ8UC0yHRVhceXwcf9KGk-YJ6uFupFbTX5doe_78LWCNAgqSftisQvu-zcPx9aX8kgHBIPVxzpU1Dup7QipM0hSn_u5aPEx9k3AoZvtSnK0wsYQ78JgxrTw6sGMQxN69N26uOx-P8ZhU_hk8twNLdWr3qdM01l-CCJH7YXnEANdgnEIjtgj_NxB6ZDCmLm1eFgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/439416" target="_blank">📅 14:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439415">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این خانواده‌ها به‌زودی ۳ برابر یارانه می‌گیرند
🔹
براساس اطلاع خبرنگار فارس به‌زودی یارانۀ خانواده‌های دهک اول تا چهارم که حداقل ۳ فرزند دارند، ۳ برابر مقدار فعلی پرداخت می‌شود.
🔹
طبق مادۀ ۱۳ جوانی جمعیت که در سال ۱۴۰۰ تصویب شده، سازمان هدفمندسازی یارانه‌ها باید با حذف یارانه ۳ دهک درآمدی بالای جامعه، یارانۀ خانواده‌های دهک ۱ تا ۴ که حداقل ۳ فرزند دارند را ۳ برابر کند.
🔹
قرار است سازمان هدفمندی ابتدا اجرای قانون را از خانواده‌های بیشتر از ۳ فرزند در دهک اول شروع کند و به ترتیب به صورت پلکانی تا دهک ۴ ادامه دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/439415" target="_blank">📅 14:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439414">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlDNNQTV3aV-VYWtTkgZA68optelPo978mJM9ACPp_EFk3NrCEVFHYw66g5woTqrKhuVD1pigChtwYTXEHcnCKPY6xf7uO4fM61rLku9Bn8rcwdkFq1tSrulxiFjL1t2xgYLxAWcMNWQC8AHeiD-96sYKXJq-opLPrTLFRkIvIAXhDxs84KJ3CqEX1ZX5-ndLVpiBplecF6Kmjw0KFNkZWFydry8Rppl9vW2dabAdKOSXz3LN6cSMleDMJ42SiQVVx-vmi8IH7lOcLSO4zUPje1EuRKZZM1p5BaSE13Whx8s5ZWtbQ_LWhRQI6Cs8ohqs31BV0mzMKSCH7ck6AFtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس یک درصد دیگر هم رشد کرد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۴۴ هزار واحدی به ۴ میلیون و ۳۴۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/439414" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439413">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402d86f16.mp4?token=XDzwu9Fv3KNjj-9BatvLLZSsBki1l_-L8YhMf879zmZudsRx59w2TZWPXkkTF1eM25GCveyHwKzSxm9I5UT98lU22VHFulpXE5tG0WEupNsmwrOOH5RGYC2O1gluskKvNsumCbLOMT-hh4FsyxYC633Uw7vn-cpcgns5iZVIjwgh0c147D3_eqx0r6ke4Zbot39ji-bUY4AvZzIi9Y9kTFSy-bdsPj97q3P3cbX69P0zkQftkNT6BhwjTvrbqoeo0m3zifB7Aw5lAlAYh3aP8yxLJLJ5dgHi2_9imUl7mU9pneTxvDzJvyy3wTl81k_N-0ReK_JrF1q8FGBY3yNFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402d86f16.mp4?token=XDzwu9Fv3KNjj-9BatvLLZSsBki1l_-L8YhMf879zmZudsRx59w2TZWPXkkTF1eM25GCveyHwKzSxm9I5UT98lU22VHFulpXE5tG0WEupNsmwrOOH5RGYC2O1gluskKvNsumCbLOMT-hh4FsyxYC633Uw7vn-cpcgns5iZVIjwgh0c147D3_eqx0r6ke4Zbot39ji-bUY4AvZzIi9Y9kTFSy-bdsPj97q3P3cbX69P0zkQftkNT6BhwjTvrbqoeo0m3zifB7Aw5lAlAYh3aP8yxLJLJ5dgHi2_9imUl7mU9pneTxvDzJvyy3wTl81k_N-0ReK_JrF1q8FGBY3yNFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات سفر قالیباف به قطر دربارۀ دارایی‌های بلوکه‌شدۀ ایران
🔹
آجرلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده: قطری‌ها در مورد عدد و رقم آزادسازی دارایی‌های بلوکه‌شدۀ ایران حرف داشتند، هیئت مذاکره‌کنندۀ ایران تاکید داشت که به محض امضای توافق، باید ۱۲ میلیارد دلار…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/439413" target="_blank">📅 13:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439412">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2IWnz84dq2yAMyQmAygsMDs4QkzocJOLgeGKuUuo_ZNDTAb6Rh5YcabaV6UN2W8plXnfKgH1k0Czcrd1wIfWDu73OKolOCN5AN6RjTdfImq9breq1B1b0SWkycZBRRGRd9eS5NuNmi_UYxbk_RQTPgPBe1O3nC23-gYjujR2irZ3xy4Mq9lLHlNU8148_k4UuWs9KvFT99z7W2zEFww4RL2XXu_nHocuPaXaaixVnMXlGxOugHAhmKHh6bEbm9zXUGsjlnQW9H-0bQq35phM1YcPAPq4u86VQ5pKxQ-mM_WXpz5aTxv_KAnt8BFkThjtnVkK_fxghu2LdB64ryReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادریس سالاری» عهده‌دار شش اولویت راهبردی ارتباطی در بانک ملی ایران شد
طی حکمی از سوی محسن سیفی مدیرعامل بانک ملی ایران، «ادریس سالاری» به عنوان مشاور مدیرعامل و سرپرست مرکز روابط‌عمومی و اطلاع‌رسانی این بانک منصوب شد و مسئولیت اجرای شش اولویت راهبردی در راستای ارتقای جایگاه و شفافیت ارتباطی بزرگترین بانک کشور را بر عهده گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/439412" target="_blank">📅 13:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439411">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرادارخبر</strong></div>
<div class="tg-text">▶️
دریا برای ما میدان اقتدار است
⏺
هر ناوی که امنیت این آب‌ها را تهدید کند، با پاسخ قاطع نیروی دریایی ایران روبه‌رو خواهد شد.
@radarkhabar_ir
🇮🇷</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/439411" target="_blank">📅 13:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439410">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/439410" target="_blank">📅 13:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439409">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5YK2gzv4YROgGhbQGqwCksV97a_b6FUWwoZEeqAK0KiidrXQ5Uqqt4ZK1VtVBmxpzfYmsrBQ-Lyo_PlAcXnSBKd-cXCnFwrEaB9qv78pjBWlHUjMaf0B9WC5J5BnNDi2ns_O0TSO6yVLMyMxPaLEdl8wd7VBWgjGwSCnOekv6gOl0ffGfKCzfGV7ncVbaEptrkIh0KtfU0gA0LO2W5h_5sys1XA0lI1l_dcVDWdrg80882NgKsS2M6q-vnkWWc8M5cuD5obtXyu3-cBdTAm37pgQFCNS-7ikp383iT05UF4PCNvUzZOrmk4RJ8S1Bwqy0YHNMkvfkMNfltfKgwz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سبحانی: پزشکیان در سخت‌ترین موقعیت‌ها، مسئولیت پذیرفت
🔹
آیت‌الله سبحانی در دیدار رئیس دفتر رئیس‌جمهور: سلام بنده را به آقای دکتر پزشکیان برسانید. ایشان در سخت‌ترین مواقف، عَلَم مسئولیت را پذیرفتند.
🔹
مرد آن است که در کشاکش دهر، سنگ زیرین آسیا باشد و در سختی‌ها و مشکلات مردانگی خود را نشان بدهد.
🔹
ایشان باید همچون کوه استوار بایستد، از خدا کمک بخواهد و خداوند ان‌شاءالله کمک خواهد کرد.
🔹
اگر بخواهیم وحدت کلمه را احساس کنیم، باید به طبقه پایین جامعه بیشتر توجه کنیم. رعایت قیمت‌های مصوب کالاها یکی از راهکارهای حفظ وحدت است.
🔹
مذاکره فی‌نفسه مسئله‌ای نیست؛ باید نتیجه مذاکرات را دید. اگر توانستیم مبانی، استقلال و خواسته‌های ملت را تأمین کنیم، چه بهتر و اگر نشد، آن وقت باید تصمیم دیگری گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/439409" target="_blank">📅 13:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3185ac3ee.mp4?token=tyuKWc1vEuMq8qyH5zuIM4LJQy0JyVyTmOvT54-sZ8AgyFm6Cv8xJbOnJg0y4lNzhbA3UsLDD_opsIGbil8mwaoGO01-br6jtWgGxbKy1I56D0YF7R1KgDxHVlL4hfxFvSO4Gx_Cn3Ok3YvAyTRFSrBaQn1rxBJorKZcsy-u0Kb-AkcfSfqC1br6rz5cHqZOEbiVawPCiKtCClNZYN_LdMIdovBuInrsUf2CgD8d5M0B35eLRK2oFn5NFqG4TPeJNi4ch0puNePJa1E0Mn-meUg55yGTiXGL11GY8t2OkMaqria1qp_b9x8CaK9axrE-bKXnHFG4ZkBdnispKGDotw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3185ac3ee.mp4?token=tyuKWc1vEuMq8qyH5zuIM4LJQy0JyVyTmOvT54-sZ8AgyFm6Cv8xJbOnJg0y4lNzhbA3UsLDD_opsIGbil8mwaoGO01-br6jtWgGxbKy1I56D0YF7R1KgDxHVlL4hfxFvSO4Gx_Cn3Ok3YvAyTRFSrBaQn1rxBJorKZcsy-u0Kb-AkcfSfqC1br6rz5cHqZOEbiVawPCiKtCClNZYN_LdMIdovBuInrsUf2CgD8d5M0B35eLRK2oFn5NFqG4TPeJNi4ch0puNePJa1E0Mn-meUg55yGTiXGL11GY8t2OkMaqria1qp_b9x8CaK9axrE-bKXnHFG4ZkBdnispKGDotw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پروژۀ تجزیه ایران چگونه با مشت آهنین نیروهای مسلح درهم شکست
🔹
همزمان با حملۀ نظامی آمریکا و رژیم صهیونیستی به ایران، پروژه‌ای چندلایه برای ناامن‌سازی مناطق مرزی و فعال‌سازی گروهک‌های تجزیه‌طلب نیز کلید خورد.
🔹
این طرح با بمباران برخی مقرهای دفاعی، انتقال سلاح به داخل کشور و تلاش برای سازماندهی عناصر وابسته دنبال می‌شد، اما با اشراف اطلاعاتی و اقدامات عملیاتی نیروهای امنیتی و نظامی ناکام ماند و به شکست سناریوی تجزیۀ ایران انجامید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/439408" target="_blank">📅 13:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNCqiJhwjNu_Bh4b0qqm6VtJod1aKv3e7ZNd9IN1y8oVCVP2Ojb7HAc3jmFCGohEeDzULwBniKcve8zZVuFzvj2bZ0FEuTWWr4ABj3GmDp9QZ0kqTcIWH4Ei1B1Jxns1C3STxUSC8kEXa_-cFRyjqVRGbvTJ5RKg8ZT38GGOYeMF8hyJZxj8-vpRtpyGL9_8U1S0p6TTayzqb_dXUzYiELJm4EbQn9S9EI_1ppHqCTlywhFpn8S85g10kkR-WDUQv55l4mrZLgw6UcbTiUs8sMw2B9V_Z5gl3GEkyCwzyCAMWLg9H12gBzGPwIgrqbTQlZaDvj0BrYkBY1N8Qv8tMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم انفصال از خدمت شهردار تبریز باطل شد
🔹
شعبه ۲۹ تجدیدنظر دیوان عدالت اداری حکم انفصال از خدمت شهردار تبریز را باطل کرد. این رأی پس‌از آن صادر شد که معاونت حقوقی شهرداری تبریز با ارائه مدارک جدید، اعادهٔ دادرسی کرده بود و بر این اساس رأی برائت شهردار تبریز صادر شد.
🔹
حکم جدید درحالی صادر شد که هیئت‌رئیسهٔ شورای شهر تبریز تصمیم به تشکیل جلسهٔ فوق‌العاده برای تعیین سرپرست شهرداری گرفته بود.
🔹
هوشیار، شهردار تبریز، دیروز دربارهٔ دلیل صدور حکم انفصال از خدمتش گفته بود: در پی شکایت یکی از شرکت‌کنندگان آزمون استخدامی شهرداری تبریز، ابلاغیه‌ای از مرجع قضایی صادر شده بود که همزمان با اختلالات گستردهٔ اینترنتی در ناآرامی‌های دی‌ماه در سامانه قضایی بارگذاری شده بود و به‌دلیل نبود دسترسی، به‌دست من نرسیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439407" target="_blank">📅 13:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
عبور ۱۵ کشتی با مجوز س‍‍پاه از تنگۀ هرمز
🔹
روابط‌عمومی نیروی دریایی سپاه: طی شبانه‌روز گذشته ۱۵ فروند کشتی که ۴ فروند از آن نفتکش بود پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگۀ هرمز عبور کردند.
🔹
به شناورهای تجاری و نفتکش در خلیج فارس…</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/439406" target="_blank">📅 12:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjlR5aQEiqXgaxNbT9qsU6aIMrGMPH89AdsC5p1zgWBVjaDzU7q5t6_QjvYpbrlO9szOKITimjw9H9ndSyRrsv85s8byThbRiVSsRmGAYBp7jqooEtRGX0RF_ZhN51bUOxWaXdUnOz58-8vPLIXsYORCw1ajUvhSEewTr4o3B5L54ZL9JSwDoIP7R2MQGEdTS3BWZjHCtJIKLS0Gv10mKtScL2bCjdRo8dFI_eh8pjinQbXDX0qKA21isGCdbxVVDhbdcMkR2xthQl_2usUzzafRj8Fj3AHcEnwjZuPIdCUPhqOFcDUIPaa96Q6vzlpuNWQ4_J2a3rZe-I2C6xYMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول روابط خارجی موساد استعفا داد
🔹
کانال ۱۲ رژیم اشغالگر از استعفای یکی از برجسته‌ترین مقامات موساد، به‌دنبال انتصاب «رومان گوفمن» به ریاست این سازمان خبر داد؛ اقدامی که نشان‌دهنده وجود تنش در داخل این نهاد رژیم صهیونیستی است.
🔹
بر اساس گزارش این شبکه، شخصیتی که با حرف «د» از او یاد شده، رئیس بخش «تیفیل» (مسئول روابط اطلاعاتی خارجی در موساد)، ساعات پس از حکم دیوان عالی مبنی بر تثبیت انتصاب گوفمن به ریاست موساد، استعفای خود را اعلام کرد. این مقام مستعفی که پیش از آن، عالی‌ترین جایگاه در میان رؤسای بخش‌های موساد را داشت، یکی از کاندیداهای اصلی برای ریاست این سازمان محسوب می‌شد.
🔹
بخش «تیفیل» (به معنای جهان) مسئولیت مدیریت روابط اطلاعاتی خارجی موساد، هماهنگی با سرویس‌های اطلاعاتی جهان و همچنین توسعه و مدیریت کانال‌های ارتباطی و روابط دیپلماتیک با کشورهایی را بر عهده دارد که فاقد روابط رسمی با رژیم صهیونیستی هستند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/439405" target="_blank">📅 12:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YON2Gm1tkl4Oenn3qQ3QGbeJC02Cgrfq1JK7anMGYSzcJiRLX7_L-pWBLZh28jLu1_5phJrdCcs3ZKJ1nOY09RDT0dsjpsxSJ7UQsudXzZbn1ay67N7jDpi5frq5LSHO458wHJgsW4H0US_R5TfKDdcqTNwdKs8HZUW8zGn2phM2htXSDTH_j6VPPVKV8kvcGBM-rl35T3ZgGtu8ls5LLLCH4eu_0KIYHiCkvxdl65ChUPv6ObKbXCQG_zRFY3JelBmsF50wfB8iWV3mPGXBGXH6YOLu0Gb-xebi4DkN2MmdD13VWJ4hmImDClLJLxW_knNZyKN94377Q57X21K72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مذاکره‌ای که ۲ ساعته جواب داد
🔹
تنها ۲ ساعت پس از اخطار نیروهای مسلح ایران به اسرائیل در خصوص حمله به جنوب لبنان، این رژیم اعلام کرد از تصمیم خود منصرف شده است.
🔹
سازمان رادیو و تلویزیون اسرائیل اعلام کرد حملۀ برنامه‌ریزی شده این رژیم به ضاحیه جنوبی بیروت…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439404" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38dddfd872.mp4?token=vqrIVtwGOl7QJxQKl8S9e5CJqH1skoNh5HApFVGjwvEh8QYLmo2rAhEfrN7DL-8hAx01QmiC1LkbAHwGAIR5r4h8upciCQXynAZmpsqJgBgK6ENjDOiGKdVGnFKu4i6LWfzY3p4MNI21QXIHnQ0U4GxV3n4RqI5rOWZnLr1ZS4PaspyKh7Rqt_HvjsmYPtDV0Tnup7epuPWhquz7kanm4E9XJsvaheLbU3JUqAOppZRlwKmxuW_YmGUzZPp_3ipUht7L4G5YESDA7zTc6bpheMxuMNNka_yhJVNohg2oAl3LAwYHdkUBrgM7rj4UFLnCNMMailby7twTEu9_s3XbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38dddfd872.mp4?token=vqrIVtwGOl7QJxQKl8S9e5CJqH1skoNh5HApFVGjwvEh8QYLmo2rAhEfrN7DL-8hAx01QmiC1LkbAHwGAIR5r4h8upciCQXynAZmpsqJgBgK6ENjDOiGKdVGnFKu4i6LWfzY3p4MNI21QXIHnQ0U4GxV3n4RqI5rOWZnLr1ZS4PaspyKh7Rqt_HvjsmYPtDV0Tnup7epuPWhquz7kanm4E9XJsvaheLbU3JUqAOppZRlwKmxuW_YmGUzZPp_3ipUht7L4G5YESDA7zTc6bpheMxuMNNka_yhJVNohg2oAl3LAwYHdkUBrgM7rj4UFLnCNMMailby7twTEu9_s3XbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساخت و آب‌اندازی یک شناور با حمل بار ۷۰۰ تنی در هرمزگان
🔹
یک فروند شناور فلزی ۲ موتوره به‌طول ۴۹ متر و ظرفیت حمل ۷۰۰ تن، با‌تکیه‌بر دانش و توان متخصصان داخلی در یکی از کشتی‌سازی‌های استان هرمزگان طراحی، ساخته و با موفقیت به آب انداخته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/439403" target="_blank">📅 11:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VimYDgBmgpSOQKXrh9iSaUDH5CE8XweOyxXSI0yzNNpm3yKBP157Yc9-7_2-s9MUBoBc_naZddNzt0sWIHyJwyXJg1QO9ghdPx6gMsNYkBBigCZnzQFsy5JJRFc6RpWZKA2uCt4y1rkWU9AUZh7QmEpoUCPtB74hkrpeYJGGnAvWwzSOzPGG8DhoQnTXmnZOdWVeBYxl1Jtk-QnsexrvOVbL2ERMw7-8RFojMHaXZQoPasLRMJeQgZkTro-i6plFsNqsVVlFiacO53zIC-YQpuLEybMyD7DKD4RlSLVowRfwBqMz2L1aej2ndf3LVppjTXOzoaeTDM-xtQ6EPgat4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: توان نظامی و عملیاتی ما در دورۀ آتش‌بس افزایش داشته
🔹
واقعیت‌ آن است که در مقطع زمانی آتش‌بس، توان نظامی و عملیاتی ما افزایش داشته و فرصت ایجادشده صرف ارتقای توان رزمی، تقویت آمادگی‌ها و جبران آسیب‌ها شده و امروز نیروهای مسلح ما در شرایط بهتری…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/439402" target="_blank">📅 11:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0_Ecoz2gWml6RhF-CK_uiPtcgORq1uYEbNlyGuviMP5W0L4ChDvK_m2MgZpSc0sHFJQMclYVm8hWF83JQ_1LuqqrrDAAnyMrZKn_mHWNJddGwT93lFGY8Pct2XjTCm_n4n7Zh-Cyn4N1Xsm-NalaJ9WswKDf_y_I5LDY5itX_fBJM7t7ktYgiVZGHT1OpWZa_N32EYDMWMCWjbZIybgulOYkEUdFU74OMLH3PovAdqO-oKSRxhFtEM5n4FFAFE-66Y_UOxBHDQ_J3Jzj0DTFz0mVvvrOfEj4kDSFGZLzq6R7YuH_FqaUs3CRHHuVMiy7HeOPno36nj-jQByMSvM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا با بدعهدی مالی در سازمان‌ملل تنبیه شد
🔹
سازمان بین‌المللی کار (ILO) که یکی از نهادهای تخصصی سازمان‌ملل است، تعیین شینگ لی، مقام ارشد وزارت کار دولت آمریکا را به‌عنوان نایب‌رئیس خود لغو کرد.
🔹
دلیل این اقدام، تعلل واشنگتن در پرداخت بدهی‌های معوقهٔ این سازمان اعلام شده است.
🔹
بر‌اساس داده‌های منتشرشده در وبگاه سازمان بین‌المللی کار، تا اول ژوئن (۱۱ خرداد)، معوقات حق عضویت آمریکا به بیش از ۱۷۳ میلیون فرانک سوئیس (معادل ۲۲۰ میلیون دلار) برای ۲ سال گذشته رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/439401" target="_blank">📅 11:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9gdKCQ4EDY3jtHEF-0Jd-rRgJzdrl-L_J78GlSXwoxx5q_zDT_9rtIko_xlL8JIzKGozGfhFoEoHEhFHpdJPn5IeRFaKU5BPmeZbiRGnWhk2NbjfsvLCL6j2jaqH5SfypuGrx_MnV5sUZDiAVDhJY5xMW2fSN65iOzr9nZQtRicCXCH4vn0NCmb6jCkIRTWYYAe0_OkfqBnlZKhReWOmGKpWoOa2lwLq16sz8ora_-_NCTj8al8KBdGUtjCnybUnkhKAOndMLpc71eZYRLG0Uye0i_iX83ZgL_SBfo6x0H9JXXyjqMsu0iitaRh9cfojWhsCdDZbPW3_sGco9zjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ادعاهای آمریکا دربارۀ تضعیف توان نظامی ایران کذب است
🔹
در طول این مدت هیچ‌گاه توان رزمی کشور کاهش نیافته. برخلاف ادعاهای مطرح‌شده، نه نیروی دریایی ایران نابود شده و نه توان عملیاتی کشور آن کاهش یافته است.
🔹
بهترین دلیل برای این موضوع آن است که…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/439400" target="_blank">📅 11:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc-zFtut_m4u2VDEptzPt088FB_koWbYAH4X4EsJMMKj602YLu50I7w3qOM-MsasGrFzFQYYAh4E7cr_CjhCkxXiQgAEeNMGaIKHbAT3oGPjTQr8nDCdnwoIuDf0k5qZ5jeRfVXF_WWHNCXhDZi5cPeq1kn_aGYYtyBzwYR56KlCuL4YzhUUVbmwML-J_ApN5hFavxif8RWteLHVwPihE6RZCP5nBog8aTPTKksP1097AdKRkNlegP7XiRLoPV9H1ubZiFQmnLtdmDo8zRfEGlXlwZCY17t9uB9TnrwC_tEX-9Apgo1bgx8Zf03VjvwhyATII2uWSNs3woFFwHYvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار محبی: آمادگی امروز نیروهای مسلح بیشتر از گذشته است
🔹
سخنگوی سپاه: آمادگی امروز نیروهای مسلح بیشتر از گذشته است و این آمادگی علاوه‌بر توان گذشته، نتیجۀ تجربه‌ای است که در میدان نبرد و مواجهۀ مستقیم با دشمن به‌دست آمده است.
🔹
امروز شناخت ما از دشمن،…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/439399" target="_blank">📅 11:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdve4uKvIGF5bXV1OmWycZDl7jV6Kt5ERpRQoriSlXczvL5dfhH3sUU9e6Vku9zBppFQRmM22mGFoShcQcG0-2GlL8POAcdQSzX-MfwYQQbciPckevnKwIfE2ADeoddT4GDHS4Apu0WfobgfpqlR_VxLCQdrl_KIQlWfhnN8YOKYJwflbztBCkdNHqIVKz5CtTJd4_jsoyXliCX_KVWB1GkSX6dTcbx4T-Zl-M8LoWwSDY-R7mQ3v1hM_8BYe1eQ9ACESk_-3kh4w6jJ9z8OBgvOpRhrGXbPlUNpQs2GpoBW-lVNhlvwm7QQjKfDyDMrQc7dA4tsRnYg0K_5zlvU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی سپاه: برای تمامی سناریوهای احتمالی آمادگی داریم
🔹
با وجود آمادگی در تمامی عرصه‌ها، سنگر نظامی همچنان با بالاترین سطح آمادگی حفظ خواهد شد، زیرا معتقدیم مهم‌ترین عرصه‌ای که دشمن برای تحقق اهداف خود بر آن تکیه می‌کند، عرصه نظامی است.
🔹
در صورت بازگشت…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/439398" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZCuIerLfQCqVOuMi6tA-L1e7yJc_8XRKOYQKXxtNGlfQz6W45iyGcb6xYi5L2ZgPQZdPMR8mGodCjaWpnO4mp_GpDRGhoMp0I44tL5lscNRRLC9ByEg5kua2vTWdkYot9hhmsg_0Bf8PUiL33OEcBHHK6JXziPim31Ov2V3Mm-UWvlQHAwoSbZC4dU7HLGczlQm7DJ8U3AL8zRGCXLXwMmktJA8vfV_VofrfVvFM6DIp0tLZPbs93h3Wsa2sObe5m77e8tWO0tdrVmO5eFkYT7qXj1YfbtCIta02SDwepAAb1pyGraH6JOrgTDz_lhKRFfdEx1Ak5ekVUHbRzWOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی سپاه: برای تمامی سناریوهای احتمالی آمادگی داریم
🔹
با وجود آمادگی در تمامی عرصه‌ها، سنگر نظامی همچنان با بالاترین سطح آمادگی حفظ خواهد شد، زیرا معتقدیم مهم‌ترین عرصه‌ای که دشمن برای تحقق اهداف خود بر آن تکیه می‌کند، عرصه نظامی است.
🔹
در صورت بازگشت دشمن به عرصۀ نظامی، نوع عملیات، جغرافیای نبرد و حتی نوع جنگ‌افزارهای مورد استفاده متفاوت خواهد بود و سپاه پاسداران برای تمامی سناریوهای احتمالی آمادگی کامل دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/439397" target="_blank">📅 11:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXA9zYflgYYR1scj-Jmc1vAh67xRH51HnU-0qUso9CKfkZIO-PA0VDdpGnadK9SZb_osmcVE0Cxjsao5iDxlsZYuX5d_KSIm8v_Gd9WLKumpTAiWwI1_nBDZsQ8Zcw_6HURurntKCPAt1SbAigxOsf43apLzwPKjQFOo8zKNPN40LaIsoZqkpLFRMQC-sjQ0t_K2DfL50_bv_SKipb6oeXlwa-vEMZS8UC8o1NnzOvBlb1CgdkYrzRaOblbLg1Q-W0ohf_M7HlY0DtdF0S7jyAVQYMqh7SJHiweONqlK3eQ9aLa8qgb0onDq012w9ybQdgi49toZwD-7q0alNXatlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت هیئت‌رئیسۀ مجلس با برگزاری رسمی جلسات صحن
🔹
گودرزی: هیئت‌رئیسۀ مجلس، تصمیم مثبت و موافق خود را برای برگزاری جلسات به‌صورت رسمی و فعال‌سازی چرخۀ قانون‌گذاری اتخاذ کرده است.
🔹
مسیر هماهنگی‌ها و مقدمات لازم در حال انجام است و به‌زودی جلسات رسمی صحن همچون…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/439396" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">همزمان با سالروز رحلت امام خمینی (ره)، نماز جمعۀ این هفته در مرقد امام اقامه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/439395" target="_blank">📅 10:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e07c4b0e4.mp4?token=sE-_WqHI6Pi-flp1RbGmAAzhHOISByRiv68DCtJBnVyafw7eUdeGRNGuevlsDv2JRP0DVjvn8Vy3vI8iAddfHQMNNHJ2qe67BFjUl5GYK7kQwurCKgBt3Q1RJPaYXY9D4LQvcx7OIKPkRnxcUoOJGqiT6ZOdDBqfaIjXvwXAKb3-EZZE-sAM1S6ABwNVDchrrQl3D2OnpZ6ExM7VqdsH-zJyOOESWOjKdURFadU8UD1WY1WVw5opprh0vHRfbC3Ac1OeeBtLrYKYkU9PlnA-quGf4HN8NciqdPefBRzje6Rb-_fLe5erQVjbb1i2Va2JRZpY1DFvX2R8raIdNdiX-0L_g400B5UzXMNhpN7PFiZp2jPifyQ4l2ap9xTdP-STuKH9ZQNNsi8FK0TbUo_PfcI4L4SGkCNW_h15tNj_SRrRHKn56d6rYaATkGW4CVDyNdtNYmP1s-K96QUa0qsjnImuz9_os64NMjX2C2-ikW4c3LnzVPkDhRrM1Xi-CdAUNSWtv7aWOta_XmEVIEDLlcy6xmFI7-D2SUYunI5AwADFyxyIKP-tXMApvynrQU74l-TZ45zo6nhuoABQpnekEhMEPpLTuZoNFq-E8HKYfmhIgYFijpU4z46Ge0TJcG0PsUoX88rMq4INWjefgEnwoum7gxfZhxDKL8oOQ7bFqYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e07c4b0e4.mp4?token=sE-_WqHI6Pi-flp1RbGmAAzhHOISByRiv68DCtJBnVyafw7eUdeGRNGuevlsDv2JRP0DVjvn8Vy3vI8iAddfHQMNNHJ2qe67BFjUl5GYK7kQwurCKgBt3Q1RJPaYXY9D4LQvcx7OIKPkRnxcUoOJGqiT6ZOdDBqfaIjXvwXAKb3-EZZE-sAM1S6ABwNVDchrrQl3D2OnpZ6ExM7VqdsH-zJyOOESWOjKdURFadU8UD1WY1WVw5opprh0vHRfbC3Ac1OeeBtLrYKYkU9PlnA-quGf4HN8NciqdPefBRzje6Rb-_fLe5erQVjbb1i2Va2JRZpY1DFvX2R8raIdNdiX-0L_g400B5UzXMNhpN7PFiZp2jPifyQ4l2ap9xTdP-STuKH9ZQNNsi8FK0TbUo_PfcI4L4SGkCNW_h15tNj_SRrRHKn56d6rYaATkGW4CVDyNdtNYmP1s-K96QUa0qsjnImuz9_os64NMjX2C2-ikW4c3LnzVPkDhRrM1Xi-CdAUNSWtv7aWOta_XmEVIEDLlcy6xmFI7-D2SUYunI5AwADFyxyIKP-tXMApvynrQU74l-TZ45zo6nhuoABQpnekEhMEPpLTuZoNFq-E8HKYfmhIgYFijpU4z46Ge0TJcG0PsUoX88rMq4INWjefgEnwoum7gxfZhxDKL8oOQ7bFqYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی رهبر شهید اسکورت را متوقف کرد تا قانون رعایت شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/439394" target="_blank">📅 10:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمعاونت علمی، فناوری و اقتصاد دانش‌بنیان ریاست جمهوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPMtIfz5UpgbZc7jyr7oB_Rgor2PPw6jnWSxNa-JQi6-ELe5dDckBpK1fHgJAprWtpTgDsNgialK9_3qBeAfZbbaJ2zJ4M2JVsAqmvxGc8KhaeFhqmuwOQO6HknkLGHIpwDo4ct1impFFoF0P1yXm7Q6tgmAcyV7ATj0mFGhWplb16eTI5KB6t7u8l4FoZ0__t4jW_vg9ooUI2EuG7QxKsy0TFlvAcODbnEO6CTvBVmWUAWBoA2WfSTUTjn7m7QIzvKGHoA7JJNwbS3QeRc6qPoA8hr65hUVHvw9qDHmwSJdwVY34f9Kb2TRwNFpefZJ4wHTkqAHcQ0s_V76S-Gktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رییس جمهور با اشاره به پیچیده و درهم‌تنیده‌تر شدن مسائل اجتماعی، شهری و اقتصادی کشور، بر نقش «مراکز نوآوری اجتماعی محله‌محور» به عنوان الگوی نوین حکمرانی مردمی، مشارکتی و فناورانه تاکید کرد.
حسین افشین مطرح کرد:
🔸
تحولات گسترده در حوزه فناوری‌های دیجیتال، هوش مصنوعی، تحلیل داده و الگوهای نوین مشارکت مردمی، زمینه شکل‌گیری نسل جدیدی از حکمرانی را فراهم کرده است.
🔹
در این نوع از حکمرانی‌، حل مسئله از ساختارهای صرفاً اداری و متمرکز به شبکه‌های مشارکتی، محلی و یادگیرنده منتقل می‌شود.
🔸
فناوری در این الگو جایگاهی ابزاری و توانمندساز دارد و هدف استفاده از فناوری کاربردی برای مسائل روزمره و ورود فناوری به متن زندگی مردم است.
🔹
در این چارچوب، معاونت علمی نقش سیاست‌گذار، تنظیم‌گر و تسهیل‌گر را ایفا می‌کند، شهرداری‌ها و بنیادها بستر و زیرساخت محلی را فراهم می‌سازند و دانشگاه‌ها بازوی علمی و ارزیاب اثرگذاری خواهند بود.
🔸
بخش خصوصی در این الگو، به‌عنوان شریک توسعه و سرمایه‌گذار حضور خواهد داشت و جامعه محلی نیز ذی‌نفع اصلی و بازیگر محوری فرآیند خواهد بود.
🌐
مشاهده جزئیات خبر
#دولت_پای_کار_مردم
🆔
@pr_isti</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/439393" target="_blank">📅 10:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdMKYgOlLZKFIY_G_WKw0HceRK_2wQVz1i-MO5tkJPm9ISvsI8Ui7aC0MOvdHF0JxRvHzObryeTsI9EqHUg92q5hoIEEiGZMd7ABkIqWhWPuOm5Sm4X602AuFoPAfeGfT9DxcUHx6_YmSm_AXoN_pyN9sF3cHF2kvSTP6bO9qXpPM01TPo6p17MR3ulhYpw6FOW2BCqMdCwoDZSzxvOhq5RzU4lEzWyhl3_fxYH_FcYV5wBIua16D3Ms_BoLSITJCp4hmkyuCmBKd1kX-rhbn0GRUXCk-1DWxY6CAt-SJ2PPbI_OnnKMEuG_zBZxIH2DEj74bYD6rpWLev7QySuK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/439392" target="_blank">📅 10:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/439391" target="_blank">📅 10:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5ae60d74.mp4?token=e68y658fgsCKtiNX8mDAa00bb9VVYgyy8SkylzMRpRNv-QcHqdrfyABBvxeDSY2s3EbWs6ZkruPxr5TLVFjz8yfGZMJpAW07gpDIjJUf-KMnx_D2wGkuhBUadpv2Wx9ARFKbX1Q8RfojtRFknoh0NdA--mo1C2ZZX9qMLoI5HTjMwxXQNWxMHybBxFHfhCZ3bqChYZmMQsW9kTVvbp3ifmdZu1fWbtxo5-2k0T5nnZXZ1g-F3w9TBRhywcfpos_tT9zlYvpqhwBIl7FUzHk8sxSmzMCT7gnlUOJh6Hisa3eQ4IfDW37giq_0YXf-ny36IfK47-53mWaNZAB8ZqQp_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5ae60d74.mp4?token=e68y658fgsCKtiNX8mDAa00bb9VVYgyy8SkylzMRpRNv-QcHqdrfyABBvxeDSY2s3EbWs6ZkruPxr5TLVFjz8yfGZMJpAW07gpDIjJUf-KMnx_D2wGkuhBUadpv2Wx9ARFKbX1Q8RfojtRFknoh0NdA--mo1C2ZZX9qMLoI5HTjMwxXQNWxMHybBxFHfhCZ3bqChYZmMQsW9kTVvbp3ifmdZu1fWbtxo5-2k0T5nnZXZ1g-F3w9TBRhywcfpos_tT9zlYvpqhwBIl7FUzHk8sxSmzMCT7gnlUOJh6Hisa3eQ4IfDW37giq_0YXf-ny36IfK47-53mWaNZAB8ZqQp_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گنجی: نگاه چین و روسیه به قدرت بازدارندگی و  تاب‌آوری ایران ارتقا یافته است
🔹
تحلیلگر مسائل سیاسی: این دو کشور راغب شده‌اند روی ایران به‌عنوان متحد واقعی حساب باز کنند و می‌خواهند با ما کار کنند و حداقل کشور ما را تحریم نمی‌کنند.
🔹
در آینده رابطۀ ایران با…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/439390" target="_blank">📅 10:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96d4703e7.mp4?token=JdxRUlenSieH-LIwRNNUc57lymtJnDUmpRnPtXWyAJpImbZ_fmw0QKt4v-_ebWqXsxqoK4FblE7JK28tVX7-qP0mHxSlW3ZRsblii8CYnjpZJT8kQlnLBsWGOeDxOORWJ81P_o3tkU_tahtmoIga5pplk6N0218Q6KKbFIMBbz7AYaSnN_8yXx-s1aevQuT0BhqhgCqlbnKd9-oq-q0SkhCb9Fqeas1XqqGu56hH8kZICK3IbNhK-XapX2j6B4pV8hxQRaJ5JnUYq3s73K5YMKXn2UNo_ncM6jQq6xYPmi7Q4ZySzI_XpZSihDYNoenc-UEOk8cfIWmam9NRWtQ9sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96d4703e7.mp4?token=JdxRUlenSieH-LIwRNNUc57lymtJnDUmpRnPtXWyAJpImbZ_fmw0QKt4v-_ebWqXsxqoK4FblE7JK28tVX7-qP0mHxSlW3ZRsblii8CYnjpZJT8kQlnLBsWGOeDxOORWJ81P_o3tkU_tahtmoIga5pplk6N0218Q6KKbFIMBbz7AYaSnN_8yXx-s1aevQuT0BhqhgCqlbnKd9-oq-q0SkhCb9Fqeas1XqqGu56hH8kZICK3IbNhK-XapX2j6B4pV8hxQRaJ5JnUYq3s73K5YMKXn2UNo_ncM6jQq6xYPmi7Q4ZySzI_XpZSihDYNoenc-UEOk8cfIWmam9NRWtQ9sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
التماس علی‌نژاد برای حمله به ایران
🔹
شما یهودیان صهیونیست هستید که می‌توانید هم دموکرات و هم جمهوری‌خواه را در آمریکا متحد کنید پس چرا در مورد ایران مردد هستید و حمله نمی‌کنید؟!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/439389" target="_blank">📅 09:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0073527f.mp4?token=BCRGzncqiTAVVTzir7xQF_djQzKFKcewKqio5VWZLANvcPcYTeQXDeJd89Dunii6Hge8kn6Yq4Nx3IQHbJXpsr71rvWuvzTqiGiOKTJCQiTp70N1a9fagSanwSeoUcQymIOx0hqPaLRc9bRNj_aAPDQUHLhtdSi2aSdVq9zUrJJx34VM5R02gH8zG9lj0vl4Qz-YkkFZxoY1gWxEsA7Kz8CMd7dTgTq4y3tyGz4r2pkgF0KETrahzQa1XRxBb8TuDwLG4wLih08_JZP4axHWuImIyPcZjwoMj4ihUruzFF4eZ8CfBx94U3Evxn3hg4pCd80EqV7lzPiykM2Ki8ji8nKWwngj8Zv0HG-y2IoorBBmWxhrbjO0unpFW9XWu_o5krIBCwzt3gPGx6omnASBPhUw_2nlq8zwfnt4BQGD4ny2DOZ9KRBWrcDTzd70aW4qPOlKWqarkn9QtonfMvphA1f49Xa3o912sWL5r2EkL6MK0vJYV70lO5dk2Yc0qNYswdpss_pIfdcE3EC1ou-V0NNjvZx8k3Si3Q8_Uv_l230ONjtLWGjG2Z4UsnrkPkjuWhQX9Dbn7SLgLkvIqDMgaOlMdr1Ly9bpvilOseEEWIyJAF2Ylr3c_iU-uBcEjCxDUigZS8d3BMJh7ZoIsXEgnvJLWaIHoGiKYkx4QNAgWAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0073527f.mp4?token=BCRGzncqiTAVVTzir7xQF_djQzKFKcewKqio5VWZLANvcPcYTeQXDeJd89Dunii6Hge8kn6Yq4Nx3IQHbJXpsr71rvWuvzTqiGiOKTJCQiTp70N1a9fagSanwSeoUcQymIOx0hqPaLRc9bRNj_aAPDQUHLhtdSi2aSdVq9zUrJJx34VM5R02gH8zG9lj0vl4Qz-YkkFZxoY1gWxEsA7Kz8CMd7dTgTq4y3tyGz4r2pkgF0KETrahzQa1XRxBb8TuDwLG4wLih08_JZP4axHWuImIyPcZjwoMj4ihUruzFF4eZ8CfBx94U3Evxn3hg4pCd80EqV7lzPiykM2Ki8ji8nKWwngj8Zv0HG-y2IoorBBmWxhrbjO0unpFW9XWu_o5krIBCwzt3gPGx6omnASBPhUw_2nlq8zwfnt4BQGD4ny2DOZ9KRBWrcDTzd70aW4qPOlKWqarkn9QtonfMvphA1f49Xa3o912sWL5r2EkL6MK0vJYV70lO5dk2Yc0qNYswdpss_pIfdcE3EC1ou-V0NNjvZx8k3Si3Q8_Uv_l230ONjtLWGjG2Z4UsnrkPkjuWhQX9Dbn7SLgLkvIqDMgaOlMdr1Ly9bpvilOseEEWIyJAF2Ylr3c_iU-uBcEjCxDUigZS8d3BMJh7ZoIsXEgnvJLWaIHoGiKYkx4QNAgWAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حزنی: شهید پاکپور یک چریک مردمی بود
🔹
دبیر قرارگاه مرکزی محرومیت‌زدایی سپاه: شهید پا‌کپور شخصیتی مردم‌دار، مردم‌یار، مردم‌دوست و محرومیت‌زدا بود؛ او فرمانده‌ای بن‌بست‌شکن، چریک و یکی از یاوران اصلی قرارگاه مرکزی محرومیت‌زدایی سپاه بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/439388" target="_blank">📅 09:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8d85acf5.mp4?token=mzQPvA-MOOYH64cdaPgzzRqeQZqXiUWNcJntl5_vDPTIkUtiTpVpfAL7eK_dz34_RotnTkZfqrCxaJFqMrNWejTK3uLDOqC7jyy0BY3VSc1yI58zI-MFmC-1bVFXKpC0qtSebggyN85LpbRJEyPkNwpl9dIWE47qnaYY6RwEh5rWP7nwbdQDgMRUmX7qt4iVC2bZipPAA3U4GuJGhaR3oD1r_vmwzm165Hyw3tihcVLWBt4AzmlHB3AwOedGjlg3Y85wEoP-XdwBabwRE_ezd1cpS7LN4bG_qAm31Va8bxL5kdAquMitishK5EoG3AwqRR4zvLP4wGokM142CBmwxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8d85acf5.mp4?token=mzQPvA-MOOYH64cdaPgzzRqeQZqXiUWNcJntl5_vDPTIkUtiTpVpfAL7eK_dz34_RotnTkZfqrCxaJFqMrNWejTK3uLDOqC7jyy0BY3VSc1yI58zI-MFmC-1bVFXKpC0qtSebggyN85LpbRJEyPkNwpl9dIWE47qnaYY6RwEh5rWP7nwbdQDgMRUmX7qt4iVC2bZipPAA3U4GuJGhaR3oD1r_vmwzm165Hyw3tihcVLWBt4AzmlHB3AwOedGjlg3Y85wEoP-XdwBabwRE_ezd1cpS7LN4bG_qAm31Va8bxL5kdAquMitishK5EoG3AwqRR4zvLP4wGokM142CBmwxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو: ایران هنوز پاسخی به پیشنهاد جدید آمریکا نداده است
🔹
عضو تیم رسانه‌ای هیئت مذاکره‌کننده: پیشنهاد ارسالی جدید آمریکا در کمیتهٔ ۶ نفره و شورای‌عالی امنیت ملی درحال بررسی است.
🔹
از طریق میانجی‌ها متنی به ایران ارسال شده، ولی هنوز پاسخی به پیشنهاد جدید…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/439387" target="_blank">📅 09:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدور حکم انحلال یک صرافی بین‌المللی به جرم اخلال در نظام اقتصادی
🔹
رئیس دادگستری اصفهان: حکم انحلال شرکت تضامنی «جهانمرد و شرکا» (صرافی بین‌الملل) به جرم اخلال در نظام اقتصادی و خیانت در امانت صادر شد.
🔹
این پرونده که با شکایت ۲۵۰ نفر تشکیل شده بود، در شعبه ویژه رسیدگی به جرایم اقتصادی اصفهان مورد بررسی قرار گرفت.
🔸
شرکت تضامنی جهانمرد از سال ۱۳۸۴ با مجوز بانک‌مرکزی در زمینۀ خریدوفروش ارز و مسکوکات طلا و نقره فعالیت داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/439386" target="_blank">📅 08:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439385">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e6b889b9.mp4?token=HEEYxzfa4qPSM0vnrdCSllf1PAgcK97s3ywvrb8dime-0fGkr2tR5eKru97oWiOKuItB3I01y3lMK5yFzT7mWMtpESNvA91paHBcEYqgPrPrrtIvKUmQy5SVolFbcAtAWxpd-G587nMysJPa_V-SKKuTTjKePWFh_0LcIi4qYlqvzv2S0wOvDjHvHQrzz9-aA9F1LwFKGB6rJRJH3V56Wz_fofyGjmE319AqOtwfwii5ITTzWDdz4oiF5MjtjfAsr3ayFQJ9ug9_cg7N-2SrmfHJWGBz4CopCzTO1vyHoTWOvZDFuCeXWK1tuWnvErPIHIl2hMum9gbO6KlxGfXw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e6b889b9.mp4?token=HEEYxzfa4qPSM0vnrdCSllf1PAgcK97s3ywvrb8dime-0fGkr2tR5eKru97oWiOKuItB3I01y3lMK5yFzT7mWMtpESNvA91paHBcEYqgPrPrrtIvKUmQy5SVolFbcAtAWxpd-G587nMysJPa_V-SKKuTTjKePWFh_0LcIi4qYlqvzv2S0wOvDjHvHQrzz9-aA9F1LwFKGB6rJRJH3V56Wz_fofyGjmE319AqOtwfwii5ITTzWDdz4oiF5MjtjfAsr3ayFQJ9ug9_cg7N-2SrmfHJWGBz4CopCzTO1vyHoTWOvZDFuCeXWK1tuWnvErPIHIl2hMum9gbO6KlxGfXw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در پایتخت اندونزی بیش از ۲۰۰ خانه را در خود فرو برد
🔹
رسانه‌های اندونزی از یک آتش‌سوزی گسترده در جاکارتا خبر دادند که بخش بزرگی از یک بازار و مناطق مسکونی اطراف آن را در بر گرفت و خسارت‌های سنگینی به‌جا گذاشت.
🔹
براساس گزارش‌های منتشرشده، شعله‌های آتش با سرعت زیاد گسترش یافت و بیش از ۲۰۰ واحد مسکونی را به‌طور کامل نابود کرد. تصاویر منتشرشده از حادثه، ستون‌های بزرگ دود و بازار مرکزی جاکارتا را نشان می‌دهد که در محاصرهٔ کامل شعله‌های آتش قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439385" target="_blank">📅 08:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر آموزش‌وپرورش: امتحانات نهایی احتمالاً یکی از روزهای بین ۱۳ تا ۲۱ تیر آغاز می‌شود</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/439384" target="_blank">📅 08:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqUzuImlwNgl4ssfYz9r0xcnb65UQBzh1HNOm2Um_oZKCvGDvACCRShlnbVo6hp3yf2iM6CRudN-sgIzPU896YOhFDNolOZMJQQRLimNCvWHtbK6nZ99YGxOK8iu0FNPTqG0oAaRogg17DVlc3-NKOKVJBsCR0ynYdNKTdyIJ9JYc2hqai2-nXm05Ou1-wGV0_euoKJL0pPpoD1IUUBQ0ZakG8KGuxc3sLzMswt7mrq4jDYW5C2DYklklMwmHcD5f_J9VNr7MK81RY5oYeLY8YThu3yb_4U-rv7D8mtY-WvaECcwwwjPJ5lnIqbZeVsS35mnCXtl2JH3gASkEmNi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJYLOBeymnaiSe3kWY-VNha6Mo9aIa1Nqi-STZTwTUEVoNk9yHDsVm8M5DxERhIiJAbpDBUgeFzDYVUPThN2Z_M800Dl-TKFyAmD2xfJFbjORmLK4VyPC61hovpkvar6NbjnjZj0SAE_0VDnn8ACxrpklApMWn61bp-kiuIMAf5PeSJAt5lUoXt1Xsi_3uTjGHcE6OozWPGvYN83hWwn1RMFpAWzi0PR0C8KJrHTCtz6wFJdz1YoTjKMcS1aiMGtvH4uXHKCMeAukIcAd1gPbXKJ8ykmmT3cu-G9TTJ45ZhotYKawuuZOyjuwbqAlZ5vaSawbGX0a7NI5EXut4ulQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9BtekYpqCRv6gZIESradnUlL2bgTx9ci9EJIYVTI_f0Khp7EkR0LFJVXjM9ogEo5svsOqnxo7Ryausn3KTTeglPvWJB29xqc4GOCzUKbHbK86A6u_fQ09_gJlTd0LGNGkMtmrESZwD-lS2X9GabuniVvpct-K75McFq_oUsDYs4ZWlfC7-KB3UOF4LZMsxcjOhBcZHby50hMmRhyD19JLUFPPH9_K1YzscIurnaBRjTYybArSh6Yi7imADb1bsnxCoShvt_FIwVAm_BH86Ya4PhpIVeUveEyK6AsoJOyhmsHhg2VU6xPEOKdqcACgsc_8nFhSIGMCj_An2yBBuB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAdfBXeDlhHYa6CgTo-z-a9qLapxgZCPyAUA9WvsG0NZhYx2R8AuGs8dx1NlHWRQv0RhFcvRmbJAXi1Not4VMRgMlDLhXa49P3NzHMV0w2n1k1F0IXb4Xt7-YfSC2Qwokln-c8Pvsy4BxlCng9UOpNY_lFb_tRRkhQkFRpqiCZhhHsMgl-48jEjiYGerzwqyXOcNyb3j4AXSMfxmc7rabN4bIT6COmoHaf4Gaz-ee8kM9xbqy00uPfFT1l-lH5t9AJClGZ1wQdBc78VUF8MqkDMUAW81UVbRoJLA8rMKgvnQ4yrfSvrA9L0K9benAaKn25mxTP82bYZaSOuleJj-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsUxvcUvv78XujrDO1m6U2RWd7yZNgkM_hFYhaxQS97lI6bgmsYCZpcLN-_2cvrXmFzqfhGaKJJOteHILj5EOWf82JrhUyUcuz9yH-avCPxputRGvf0hDC9xepS-8gkSJTP61zoPQ65KpKRYxrN-2uOamLsF7jzNIKg4zwgalrS4WIdczJPuS9n1uWKQWWH5i0OHQyu9wiwmwA4MkY4PpbW6Y7fk6fkL2QjbrBn9ArMdzg54KYUi1hFt0d3BuDi4X1ON58PK1fr5dbQh-RFH5ogvU_vNTf9bpE1XvhxAFtkv30HGhEOff20N2rDRp1hA2Uy-k283jKu2pymq7wxUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-6Nx0j0kD4wkM3_zA7qPu5lmkuNS4sbwzIuRohCoUWQcTYXJNjOn6WY2PvV_wlVFf_jS8j4e5pifEucRmwhbf1X4nwz0rsKlkRWM4W-ZecKnE23RWi0li-D5V7KizgLJWMQ5sRoXu_AuHBdYRU2Cf4e1Wv0hIHHhf5NVwtfo_OGjKXokufOgFvkYlabkiQ0un1fH5eSl6L5M6uCetLn95wzM8DcgDZEp93rzvjcekR0kU0S7ERe0vJkfRQl9skfOZ9iGaiJTrKc_7-2ssD1wasCmZcHv7HuP9WaRZjJTUndSowJXNbRZzxRzZFag-gQmV86JkGbfPAhERvlmmJkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urE33-sG-iI_6KDqavBol-V_Rl_wVzsYYxJABevJLRcomkQhCREKOHWW4Vyp0BGH8MyLaW6Yxm3hkUU-BUY2yeM67_gEI5p02ReZpk16ogsjkluFIzZfSE3L1cnAezsDZOf5csqDafmkDF0wuR_PWmqnpkgscs5Qfy0gjFxQjm9OL5tv7zbZgAc_SdhBTmY6A-c2PS4aXJbd02S4n3m3VISexbdOipO1YhI3MypSCG-hHZmxR7pyW5n0iGRSspZZW0so7AM5y_vciP2NqgUM9utcUnvm1p_fjIWw4VUeK6tr6dGq_TeER-zEq24zzfeLD2Rpgdy4LDNsvSS-GQzHMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازگشت نخستین گروه زائران حج جنوب کشور به شیراز
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/439377" target="_blank">📅 08:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439376">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند و من سریع مشکل را حل کردم
🔹
«امروز یک مشکل کوچک پیش آمد، اما من خیلی سریع آن را برطرف کردم. این مشکل کوچک ناراحتی ایرانی‌ها از حملات اسرائیل به لبنان بود.
🔹
بنابراین، من با حزب‌الله صحبت کردم و گفتم شلیک…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/439376" target="_blank">📅 08:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWd4Vnr35r-7LFU3KgE3OX7PLH702f4y4X-ec4W7CI9ufKAyuLXrBp-crzuxtWR-A_phSOXG27P2-1L2SPID6zi6Yg4Gy3DmANGv0VTxu2_U2E31HqWf548y3MZgFgp3xGxA6w64sK_tM5CuE1CiE0C7rFqgHB7NtOiKllZniTDZQB6ZgY-E9C0baKGOosUUF9h3tS8htz8P6MxGR7F-klimYAey3Hn1hiM-1hH_Efj88c91vvL0iqGiFGfdLH2Kg9dauiq4Re3PpQKOOYBC_ucXvDWQEcmV7LjIZdAqVbAxqbb7OiI3Ob68wKZKODPw1YU7PfilQ9xxCI6p1R94Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده حزب‌الله: آتش‌بس یکجانبه در لبنان پایدار نخواهد ماند
🔹
عضو فراکسیون وفاداری به مقاومت وابسته به حزب‌الله در پارلمان لبنان تأکید کرد که هیچ آتش‌بس «یکجانبه‌ای» در لبنان دوام نخواهد آورد.
🔹
حسن فضل‌الله در گفت‌وگو با شبکه المنار تصریح کرد که موضع لبنان اکنون بر یک آتش‌بس جامع «زمینی، هوایی و دریایی» به‌عنوان گامی ضروری به سوی خروج اسرائیل و بازگشت ساکنان آواره به روستاهایشان متمرکز است.
🔹
وی افزود که این موضع به تمامی طرف‌ها ابلاغ شده و باید شامل تعهدی «روشن و صریح» از سوی رژیم صهیونیستی و همچنین توقف تخریب خانه‌ها در جنوب لبنان باشد.
🔹
فضل‌الله تصریح کرد که حزب‌الله به محض اینکه رژیم اسرائیل به توافق متعهد شود، به آن پایبند خواهد بود و تأکید کرد که گروه مقاومت حزب‌الله، پایبندی یکجانبه به آتش‌بس را نخواهد پذیرفت.
🔹
به گفته فضل‌الله، فشار ایران و تهدید به تعلیق مذاکرات در تغییر مسیر تحولات نقش داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/439375" target="_blank">📅 07:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۲ متجاوز به‌عنف اعدام شدند
🔹
حسن طهماسبی فرزند علی و کوهیار عباسی فرزند علی‌اکبر که به جرم تجاوز به عنف نسبت به فرید صادقی، نوجوان ۱۴ سالۀ شهرستان قروه به اعدام محکوم شده بودند، پس از تأیید حکم در دیوان عالی کشور به دار مجازات آویخته شدند.
🔸
۲۳ مرداد سال ۱۴۰۳، فرید صادقی پس از آدم‌ربایی توسط ۲ نفر به نام‌های حسن طهماسبی  و کوهیار عباسی، مورد تعرض و تجاوز قرار گرفت.
🔹
با شکایت اولیای‌دم متهمان شناسایی و دستگیر شدند. در جریان رسیدگی قضایی، متهمان به صراحت به ارتکاب جرم تجاوز به عنف اقرار کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/439374" target="_blank">📅 07:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA7VA-0KTJYQnxRFjS3FAsBhSgC86He-fUW-qe-w6XtYT1wLrAVF-eldTyqCeLPCATuvDdFNrsho2FPimmL7V6_W3Uv0CoMkv95uBc7q0YGLFNEniWUOhfaLa_r2RJIReYn8fyTlqtTix5M9F2xU3qsoWBNnznUx6DZPfNfWqYLM932nptWYC8v_NpimdHfiAQybC7vxBIRe9GYTdN9gKf2mFa-q392Rv2bO8tC9EyffRZcV1nBt8EH-ySELNp-6rw0WVP6qKrBEEG0i_D7qHte4OrdpUYnFPMXCyEtiykoZtY-SwsWErgbk2XcgibwuAnUZYxITvB3s_6eeCdp8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف انبار احتکار داروهای حیاتی در قائم‌شهر
🔹
فرماندۀ سپاه قائم‌شهر: ۱۵۰۰ قلم داروی حیاتی و ۳۵۰۰ قوطی شیرخشک احتکار شده در یک واحد مسکونی کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/439372" target="_blank">📅 07:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSb7m9T9sQCIhH0FZY5TnJbWHJYAM7RjpFz1k0pCI9elwjJ1TnoyDprvweL69mT93TtFDr2ag1vIQwelKsiEP7IuRVq29bhV3HeCFjqBrf9sHfxLdESjewjgemqulyxKf0ammXEepFHaPxYqAPOKN0aH1sBwm5vjuD2Wc3CycrCF0an34OYgLbEn09MtykxIL3t86YIuVy-Z7kWDEe5Foe-flHNJddaiwpPlVrzh7UB8O-MrVLfgLKgAQVQm-ypNjWD78UvQa5Dj6RMiIBQaMFGVXjQMk229IMhMnI64cs-J_C5VT1hDphm4h4y8EGa6YvTKaWoq6gxsZGFPCl157A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناهید کیانی مسافر قطعی بازی‌‌های آسیایی ناگویا شد
🔹
مبینا نعمت‌‌زاده، دارندۀ مدال برنز المپیک پاریس، با اعلام خبر پارگی رباط‌صلیبی خود از دوری طولانی‌‌مدت از میادین خبر داد.
🔹
این اظهارات عملاً حضور ناهید کیانی در بیستمین دورۀ بازی‌‌های آسیایی ناگویا را قطعی کرد.
🔸
پیش‌از این قرار بود کیانی و نعمت‌زاده به‌مصاف یکدیگر بروند تا نمایندۀ وزن ۵۷ کیلوگرم ایران برای اعزام به ناگویا مشخص شود، اما مصدومیت شدید نعمت‌زاده باعث شد کیانی بدون نیاز به برگزاری انتخابی، صاحب سهمیۀ این وزن شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/439371" target="_blank">📅 07:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439368">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsamgNqdzyNVCn4zzACMLtv3bXp6EGdXWB_VXR37iwekGripjID9u30lW7s7vsjxt6zXjiB41vkyObfAU0VMzrwi73alyW7Eh-68aMWIwyiW1tUrLY251ruB1S1Fwp8O9I3eBrwrO8uYO70mLAd6B5S_JgSs48HVCWpxQ8JOlnTkym1R5I4YsJNQzdn6Jxudc57OkQw6D_yf5QHUj41KKa-srKeixSn-sm2fRnUT57O4RC27VYnwm_yyF8_sAMlY89uXJYAJ3VymSPnzrJ0wSBe5VUIF7_2aTVgM-Tp_kyCC-DuzSJ8Ft7k51c9_4_pS4xAtMkXMHxx-RUBOhOdTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc7rWnWxWXb7wP3aivoS4_2hyjLLfQlfUooMHbpUGFJKPIgDZvDgH5JUu4KN-kkFar2Icie2T9ewjbRCPqHxIhPOQsLoXnPygQgDW0jbxIzYr1XDgALb9XVTVmT1XbJNstgaAXkr9Ht9bfbxq_LVBu3D8v2KK3dLF64Fo0VdjqgOepXRXw5UWnAJiHV1OgeDjiNIDxr49sT3pcz1c-wBxBO-d2x02Ienl6_liqao7TpvxyfSDwsfWQvvuqrUzeFezLCjmaT9pU6I5Tk0xlyMXVhB_9hQEwcOAe3IrkLxxwSOZ9OeFNopifNwQj4Enjx7slxKeeJsQ8vHLCOfatdpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpSUcFTV0d4x4xE2XtC6v4J9ywxb7zeoPFMur1TUJpvHMNwt5TQULQA9DOTgMiXHYWmYLdgisSpjFIPilVz4q6MWrkgz1OMiKaRCmQICvGcIZAj5xZ2X9IZW_WwMnvN0AS4-jU3TAE977RtELhL5gSLzDPaluy0q-EWflJkdhaca-jyrr9Xyge24leglHvC08MA_pQ_nQPF6UAfLUbhKwGVThjJBNxPJpCX9BqBgwRuy4sdy7oWbVIQU2b2xZsbT9kD1tLGC3iMRr7e2Z-5HSwCwk0bxeU8KdQU8SW4wrXUx_3TTaUhjtCO3IYLVbYX4jgwSOJWoeeraqe91tvrqpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آشوب در قلب مکزیک قبل از جام‌جهانی
🔹
در فاصلۀ چندروز باقی‌مانده تا جام‌جهانی، مکزیک به عنوان یکی از میزبانان همچنان با حاشیه‌های بزرگی روبه‌روست؛ به‌طوری‌که پلیس مکزیکوسیتی با معلمان معترض درگیر شد تا مانع رسیدن آن‌ها به میدان محل ساخت «جشن هواداران» جام جهانی ۲۰۲۶ شود.
🔹
تجمع‌کنندگان تهدید کردند که اگر دولت به خواسته‌های آن‌ها برای افزایش حقوق و لغو قوانین بازنشستگی عمل نکند، میلیون‌ها معلم در طول جام‌جهانی به پایتخت احضار خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/439368" target="_blank">📅 06:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439367">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125831ec91.mp4?token=G13Dxg6tQ115Z0uVuysTxh3cF_Ev8aSaOrGzTGXUvZUV-Ue9F1VQBpNxYYYaCd8PZeFZDVii56MFSy9A0SV-mn41haQncguhOWwnDQkBgdlgilbZR6gffQfJTXIPHBnTUBDPy9I6zHAM8jGwJjpjllO2NApbS1PjNcIbI2gabMKtB0cAiAgq5ILe3qWbpgCV72OL9YV25MDbm22JE_FkZSsvAAlfOMPa8OJ-84h9t4lMhZ4GjUXbapjgekij0qRfNrWoTSQPAZAwUY2PPyJQrZrCgxyh8I-LQz2q-ulhDJwKLrQdz7BrntasypeFOrgADZWEQmRg_CNrzGkWAl-3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125831ec91.mp4?token=G13Dxg6tQ115Z0uVuysTxh3cF_Ev8aSaOrGzTGXUvZUV-Ue9F1VQBpNxYYYaCd8PZeFZDVii56MFSy9A0SV-mn41haQncguhOWwnDQkBgdlgilbZR6gffQfJTXIPHBnTUBDPy9I6zHAM8jGwJjpjllO2NApbS1PjNcIbI2gabMKtB0cAiAgq5ILe3qWbpgCV72OL9YV25MDbm22JE_FkZSsvAAlfOMPa8OJ-84h9t4lMhZ4GjUXbapjgekij0qRfNrWoTSQPAZAwUY2PPyJQrZrCgxyh8I-LQz2q-ulhDJwKLrQdz7BrntasypeFOrgADZWEQmRg_CNrzGkWAl-3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یک کشتی با مالکیت آمریکایی-صهیونی هدف قرار گرفت
🔹
نیروی دریایی سپاه: درپی حملهٔ متجاوزانه ارتش تروریستی آمریکا به کشتی ایرانی «لیان استار» در محدودهٔ دریای عمان، در یک عملیات مقابله‌به‌مثل، کشتی MSC Sariska متعلق به دشمن آمریکایی-صهیونیستی هدف موشک کروز…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439367" target="_blank">📅 06:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439366">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سازمان ملل: وضعیت لبنان عمیقاً نگران‌کننده است
🔹
معاون دبیرکل سازمان ملل: وضعیت لبنان با پیشروی اسرائیل به‌سمت شمال و ورود به خاک لبنان، عمیقاً نگران‌کننده است.
🔹
حضور نیروهای اسرائیلی در شمال خط آبی، حاکمیت لبنان و قطعنامۀ ۱۷۰۱ شورای امنیت سازمان ملل را نقض می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/439366" target="_blank">📅 06:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439365">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یمن: اجازه نمی‌دهیم حزب‌الله به‌تنهایی بجنگد
🔹
روزنامۀ الاخبار لبنان نوشت: انصارالله که از نظر نظامی برای دورهای بعدی رویارویی با دشمن آماده شده، تحولات نبرد جاری میان حزب‌الله و اشغالگران را از نزدیک دنبال می‌کند و منتظر درخواست حزب‌الله است.
🔹
یک منبع نزدیک به انصارالله تاکید کرده صنعا اجازه نخواهد داد لبنان مورد تعرض قرار گرفته و حزب‌الله به‌تنهایی بجنگد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/439365" target="_blank">📅 05:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439364">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9ifw4sqkZMaTM9DvZTKNtHoECwLVOenxO4CzZeQnw1xB2I9EVgtNNoR8Wjo4Wl3B7uB5Ac0itznGZmnYaKdqqxpzvOdQBUvsBeomQhWY4kFKUfK__N69_An6BhcHMyRyKi-DYJ-l0i1_czifilyF8ZO-4VWSiI8YKUzuGujdq936st8wEjA7l7SnoZ0XLjTggwZp39Y2WLO8Skt_4GtnBuWgikNw_RvsblxskXVF1aAqIaPMbc7CkTHiDYPFdHGQ6YPxIGsqMDe9dvKlmIK4p8jiO9SBqdJKVkqb97Q_iJ7Coh-gGqUUl7WvNrIi-H7hm4Ad5ALXGiT_NjmmPRRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام در مدارس دولتی هزینه ندارد
🔹
براساس مادۀ ۱۳۳ آیین‌نامه اجرایی مدارس، گرفتن هرگونه وجه در مدارس دولتی به‌استثنای هزینه‌های مربوط با بیمۀ دانش‌آموزی، هزینۀ کتب‌درسی و لباس‌کار در هنرستان‌ها ممنوع است.
🔸
کمک‌های داوطلبانۀ مردمی به مدارس نیز صرفاً خارج از فصل ثبت‌نام امکان‌پذیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/439364" target="_blank">📅 05:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439363">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOPPYFhRBDsbb_75Wq_YJQxukrlEXx0xNKEGqpdrjBLbXjc7badfaVmveekOt3CX7exKQFoz4qcNVZlmy3DqJCl2Qkcn4NM4Vg4cUJjbRC7i1y5eLwzEwKYSRy3l6XRyFX-QyPRAwZfEM8-plJFNZK2Pt5nG9-pYPELjyUNAG9cLgK94wC4ZfVykAFhYOmKX8ufidycrPjBjvbKmhkAq-eT7cIzgy5Q3QVQmJU5I2jJrZeDPSrznmL2OqPxiZDkiL28YZ4eydFrHeN9XPYb6uUChfPHu_C4XDC1vsz0TMpVkm6AaT6shxPEUOIUzFZWdXJCaEGLx5SrxwEULgd4AKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکلیف مالکیت زمین‌های بیرون‌زده از دریای‌خزر معلوم شد
🔹
طبق مصوبۀ جدید شورای‌عالی‌حفاظت محیط‌زیست، همۀ زمین‌هایی که در نتیجۀ پایین‌رفتن سطح آب دریای‌خزر در نوار ساحلی ایجاد شده‌اند، متعلق به دولت هستند.
🔹
طبق قانون، هرگونه ساخت‌وساز در زمین‌های بیرون‌زده از آب دریای‌خزر ممنوع است و استانداران وظیفۀ اجرای این مصوبه را برعهده دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/439363" target="_blank">📅 04:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOZ9QBY86O4FGXToIdkOoE9s9T0TmvvWjT8HfHPxhH3tmZoKdEVa3vhOqmAtgJo6Nys0D3lx0dVRNGxA67-JrH2MfszcYw8QTX8li6b8ybvKG1cn3P30XAy8I-_e0p80TnkUfq52EBGxpoERDvuacoQ085oH8w0w--M7TU-xENLjq41_Q0VeuyHv0IVSsSvSA1bXlXbLTJp2Atq4SdzkpDif--rbL_k3ftQSjpux9SmR-u_-_tuuatau5F-K68I1wCl3cLhQ4UCzegZ2gDc2K-0qwLQRyXnSb4LUYVboNE6wEmZ-znAJM3b8IQfpfqSvYme8KB4qArTCSTvanzfSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته‌شدن نظامیان آمریکایی و انگلیسی در شمال عراق
🔹
ارتش آمریکا در بیانیه‌ای اعلام کرد که یک نظامی این کشور در جریان «حادثۀ آموزشی» در پایگاه هوایی أربیل کشته شده است.
🔹
در این بیانیه آمده است: این تمرین آموزشی به‌همراه شرکای ما از ارتش انگلیس انجام شد که آن‌ها نیز یک نظامی خود را از دست دادند. حادثه تحت بررسی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/439362" target="_blank">📅 04:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYwQjeUdnX_CpRa1nrShZtJlGQoBdmMx6irdlp4e4J73jATHfovRgMzbnpy-7twcWxpDjrKmwPyB77yaLI9KA38Q--QC1c8wtrQ-A5-h4cQtsEnHfslg3YNGF4tjD6T2GF9Hd0goKfPvHgB1-ssVPTIdpAJObOUSJtqiyJJWKJEubIEvFnmLKyiAXAFvozwu6BjE6SA_6-KI0BHcedzbeiOvdwXW23Fn15Wi2t6KQeanCORN2EXrXULxrfZxLJTCkHu8Aa36ERck283hzmQ3dos9mQRB70YwFtP6mEFZCrXUu1ktfs28IkRGDrJC2R-xBOFjJPeEt2Aigd0evJoVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس از بیم حملۀ ایران، موشک ذخیره می‌کند
🔹
نشریۀ تایمز نوشت: انگلیس در بحبوحۀ خطر فزایندۀ حملۀ ایران یا نیروهای نیابتی‌اش به پایگاه‌های متحدانش در خاورمیانه، درحال ذخیره‌سازی موشک‌های چندمنظوره برای مقابلۀ احتمالی با پهپادهای ایرانی است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/439361" target="_blank">📅 03:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439360">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx9_IOFf1URuxRQEGZvackqba8bUSnNDuk1k4tleDJGIA89nMO6TLEDna481wlODBdyjLctRhd7MCeFt6HJifo-CDX2K2PziIb1XFNy2vk97Pr-5aHPLI_seNyYNui1mmZ7IVdttjZqI_3NwvivmHa8rxLoawojahkSPh1jqMn8ka5b4GW15L3SoX04unGo12BKGUJw_1YlbbhiVD2T9cbrWKVyNHSqAl3pmZse7MsIlmaQaVfer3Tz18bqTyy_zHt8xPjmu27XjQ7Rtb8i_DItiCk5GkfsPqWSwn1UAXlIDyzF5-ph9Lt_kDDRM6aAK79eTD9uRUMjobycI3tLeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: اسرائیل باید فوراً از خاک لبنان خارج شود
🔹
نمایندۀ چین در جلسۀ شورای امنیت: حاکمیت، امنیت و تمامیت‌ارضی لبنان باید محترم شمرده شود و رژیم‌صهیونیستی فوراً عملیات نظامی را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/439360" target="_blank">📅 03:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJvxHm9iYJAnmYbCC0P31JetfaljH8vrbW08wcb3eWrFd_elbkRZ4f3Omw9vgADyfqJ--G20kxgsZvLGo4Mf4P_7D3OVODhVmWbr16OC9Tgh8nRq0SGIP0IXYP01fSOryuvndrLYLF2xkaGZrpW4hx1yhQT6Hkj1hTD6SasHskmJM962I7s3cwLWzcj4Gw3iSImkn0Vlii2s-fZX7Ue5Evg5lU6rgDCZe5IoYBz8BgANblJGxj4ffDNO3yl50CT_STYJx_1YdTJ19A9kJsInLjMqU03Grp344xwkmmRybJFCA2Dfw8UBkUdiWwqt8gi1ScZCIoiOWoPwoTDkjQm-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشارکت استارلینک در کشتار مردم ایران
🔹
رویترز به‌تازگی افشا کرد که ارتش آمریکا برای هدایت پهپادهای انتحاری لوکاس به شبکۀ استارلینک متکی بوده است. این درحالیست که آمریکا و رسانه‌های مختلف، مدت‌هاست بر روی ارائۀ استارلینک به مردم به‌عنوان ابزاری برای ارائه دسترسی به اینترنت آزاد تبلیغات کرده‌اند.
🔹
وابستگی عملیات‌های ارتش آمریکا به این شبکه به‌اندازه‌ای بوده که وزارت جنگ ایالات متحده حتی افزایش چشمگیر هزینه‌های این سرویس نظامی را هم پذیرفته است.
🔹
در میانۀ همین تحولات، وزارت جنگ آمریکا نیز قراردادهای چند میلیارد دلاری جدیدی با اسپیس‌ایکس امضا کرد تا این شرکت در توسعۀ شبکه ارتباطی ماهواره‌ای جنگی نسل بعدی آمریکا مشارکت کند؛ شبکه‌ای که قرار است سامانه‌های تسلیحاتی، سنسورها و زیرساخت‌های جنگی را به‌صورت لحظه‌ای به هم متصل کند.
🔸
در جنگ ۱۲ روزه بین ۱۰,۰۰۰ تا ۲۰,۰۰۰ ترمینال استارلینک به‌صورت مخفیانه در داخل ایران فعال بودند. این ترمینال‌ها از طریق قاچاق وارد شده بودند.
🔸
این پرتوها توسط عوامل اسرائیلی برای هماهنگی عملیات پهپادی و حملات هوایی استفاده شدند.
🔗
جزئیات بیشتر این همکاری را از
اینجا
ببینید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/439359" target="_blank">📅 02:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1dmzCAG66pirtjg6yhYITWPHcAf6sTJLKTX6IYt0odPcUP1D7o5HqzJzoEUWCZKoePTKd099tr2qBooF6efQaJuepBG5U3TfHS5dXv7srQd_BOU9VgDZCW-uet9dS2JdqSL08sMWPn3l09WBvw1wDCTtYVgTy70eNTcmfoAWYXVjx3-qHJneESxhl-dfrG0olll7l-33oQZyGXIShmlEAHdZ17AoYwTF3WQPPB50yqUPs3Hp7STDrH2niNkjHkyW4tAoCsBm1RY7mxc4NS6RhkUIeBpzhoW-K6fvCofFWxLT4vOhKazz3xoeAA4CbbJX7lebgYDd3rncvpooOPY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه: وقایع لبنان شبیه سناریوی غزه است
🔹
نمایندۀ روسیه در شورای امنیت: توافق آتش‌بس حاصل‌شده بین اسرائیل و لبنان که با میانجی‌گری آمریکا حاصل شد، متأسفانه به پوششی برای گسترش تجاوز علیه لبنان تبدیل شده است.
🔹
آنچه در لبنان اتفاق می‌افتد، بسیار شبیه به سناریوی غزه است که مبتنی بر اشغال گسترده و آوارگی اجباری جمعیت است.
🔹
وضعیت وخیم لبنان نتیجۀ مستقیم تجاوز ناموجه آمریکا و رژیم‌صهیونیستی علیه ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/439358" target="_blank">📅 02:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5aab5a2c3.mp4?token=alX86yWfa0Eh_iymUnRsb_1TyunqDAa6rab6GZtFH_fEb7IicZ8uhCjPN7ZUrNeFzm9vvSjJm7WhZxs1wCVq9QzynRhYsQ6y-SwClC4-BT2oNwSyagtOvrHmnHG_mASoH6OVb7ktpX4IzqdzAbuKA1cs3wWsQiB_dOThvDxedHkUVbDayL1IvoW_njVBBIgfuYT_ZE9r-15NeGOWmICgPGGd_KuSD66WEHszDFwYAFEyARIlJr6czk3ulQk_ZvcJZBd7j8Vo9kPAudDt91e7EnpaXziV8PA1X3k4B0GAH6liFwDgjpO-BpjojSwsDT7dry2-f5u8C9LBkYDnXqCDhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5aab5a2c3.mp4?token=alX86yWfa0Eh_iymUnRsb_1TyunqDAa6rab6GZtFH_fEb7IicZ8uhCjPN7ZUrNeFzm9vvSjJm7WhZxs1wCVq9QzynRhYsQ6y-SwClC4-BT2oNwSyagtOvrHmnHG_mASoH6OVb7ktpX4IzqdzAbuKA1cs3wWsQiB_dOThvDxedHkUVbDayL1IvoW_njVBBIgfuYT_ZE9r-15NeGOWmICgPGGd_KuSD66WEHszDFwYAFEyARIlJr6czk3ulQk_ZvcJZBd7j8Vo9kPAudDt91e7EnpaXziV8PA1X3k4B0GAH6liFwDgjpO-BpjojSwsDT7dry2-f5u8C9LBkYDnXqCDhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ‌جهانی دوم همچنان قربانی می‌گیرد؛ این‌بار در اندونزی
🔹
با گذشت حدود ۸۰ سال از پایان جنگ‌جهانی دوم، در پی انفجار بمب برجای مانده از این جنگ در شرق اندونزی، پنج نفر کشته و سه اندونزیایی مفقود شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/439357" target="_blank">📅 02:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPutlb8iNd_FCrzwNoMvRyCakk-ME9qxEHd7--oqyrr96VA4XEsQZE8DweL7EbeUIb19-y6xmeHCb4RSgwZjY89dvNVhQirD_f9Nofll4pAo4O3zfa0j1kI4e19HMjT1FqzK_WBvXB_xs8EUEdohN1ntGqM0UBLy1bAvfZ4wDkdEiGJeEJO9TOqvQMVUBnrvM54AKvcASdpyjLDnakkPf2mLti2CLrRQUGnMFK6lK7UaE3wtj8Jb1uvRr56YJ0is0e0sIg1qA3cY1G8n3UUu2bH3yBqip7QVTAQrOplFJR9tiufEelZv3UN6YQGETs8hZOH8KNIneNBtTngTytyjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه: ادامۀ حملات اسرائیل به لبنان توجیهی ندارد
🔹
نمایندۀ فرانسه در شورای امنیت: هیچ‌چیز نمی‌تواند ادامۀ عملیات نظامی اسرائیل در لبنان را توجیه کند. تهاجم فزایندۀ اسرائیل به خاک لبنان یک اشتباه راهبردی بزرگ است.
🔹
فرانسه کاملاً از مذاکرات مستقیم بین لبنان و اسرائیل، تحت نظارت آمریکا حمایت می‌کند؛ امیدواریم که مذاکرات منجر به خروج اسرائیل از خاک لبنان و تضمین احترام به تمامیت ارضی لبنان شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/439349" target="_blank">📅 01:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiKJJaP_5IJfYHhiFqMKkbcmsTrznj4SkF-Nm-QGbI4aU4mMDnbzTOsFlGCGygD1neTvsOLKQKG4Ls1LD7dwrTNoTGzLr2pfBlu9wsQlRgtpd79eOCwAtYvK51TGeeHnEeZ_a7nev4fCHi8kyzYCZ6_2x8g6LD8sWY8frOOzevrwQ8lOHG2pTb3YB-cabsxzhnejJnlRpDauqyuV5tm5XJfG77Yzrzz9Qp1UdRuRkVlUmH650MCmFBa1FO5QK8L7wg3CS9B6i3xyq1rdov0WcNQPEJCI7Xf-e904TjsEtd4-BlwzmcSlYWKy3ZY1cJ8Z__6WuH8ihr1liffx2PR-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد از عقب‌نشینی از حمایتش از حملات اسرائیل به لبنان مدعی شد که مذاکرات با ایران با سرعت بالایی ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/439348" target="_blank">📅 01:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCdvia-t6ytyIfnCyuf7lJOuF1S-qPNatUYduKvvULJ9VysXAFQ2AgauoRCjAveSgSf0mSZcqCyIm3d8psEqVgLMKJgjf9aKDFSTkoPwscdPAY26uJ9eHt56hKuMP8HfDaTvCy1sxuWjMZN3eqwXP1Pi-1WgRvRb5BE53nC150tch-xc4xtGM5ow9ppl5HQiqRBUfOhcA5-IT96uyEFUvCpQo1-wH7dlSc9eOPUwhCDBkH-r8fha820tin9dj85yuXr2Q4D8AlKo8y69J1EN06e-pldt-nKvH9ILBBST-MHZVfsmOv4FzArsf95DFxoxyycLz-HH70mWsHj5UZ85jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfwNDHdoY3OY-HgYE1sK5sLm9liq2K7wEOVrOn3XSkIrnjW68ansGI-6dJtp40R_YxqjvAwFYaluUd04GjzUVg2yeQdDKCf8fdxywVhDAdln0GeG35s3hk3YVvHanWID9FMvLGFSKGcvL4IzYbHdab2k8qk3DOZsgJk9W572xHEaQ3LHdHjTelet5MCk35btEJGgV1-zxDLqZkb2xh6uZVzEndGQPHX8AsFFzzZP5SnBDGn-KDVG_BwDK2qjkDqNyAY3h-RtERGIVHpfYftuWmwCvgb9xPppUBhhVx0oLUrxPmxThxnOKQRNtkUjvQ137fpXIm3gCV7g54U9LuFwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXseDT6GyIkD3JNs6AT3ayuZS0ifE7C6kPT4AetILZN2C-Gqat7sAmkYRPNjRYt76JPK2CSNbDok5c3ZROhv32LpA0QOrQfUVJx9Hfaaybm25i1JgTnYVBTtBf6whfPqN0JIjBNzi9jIM5obidzubVfyxe-8qyhRHyOM4gHJfpQy-EYqg8K5PNd8dlvnCAgrwrVoK9HWTpz08FUeWFDkblxph4M8CvZ3dio1wTSjJEbMztNnsRUjyjoV36aIP54RqrRKvHQyLqWWZHrtNTPl3vwHk1TYUcG2xcAfPv618l_3isoJnAoe30DdHZlfnauYjI56JzYPGZAMBRNRRXZlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pO-c7CMpcnTVjbPWtaEqXTLCCGw8Ex_yZOVOEBH5qlcRTxlIv8amF3_onvlAFc_Qku9uZLr2zeDFOP_0F7yqaiJcKDSRpBNNZPhoSRrQrgcUE5_3XYMhI_ksHEwQ3wz5oJDa-At3mfG02CyRgOcv6wtNgh682B0ATcPBYPM7Kbbj2czp1jeg84NYO5DkgXOc7Qshhhg2eZdMXpen5y32csS5IAvXFXf9HDuGmV6B72p8nBCMtMTswnZYEFXB1cefUsQ-_Mt1euU79BX0nE7Pg22FJiXuBWGMKrkGjADUIP8Ee66ud0WRnXPy3leBsw-cuKdGkW95FrYxlnqx4VCvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7SbN29wu99RtfdStXVwcvhD2MhpR7CFMhKgen9VamtsXwYUd91pueQpbNxRy9ch_Vk9Eqbj0uryZp0cdv9xKanRAALlPaMkyMDCbbekXlbW60oxPaWkvvuAN8rLmWGVnpV7WDZPjIuIQecNLb0V3sRndQs7z32y22k3VjHmOpupw72BMFFpY7cxfOUvr4KYEYf0BwW53E_YM5V42zwFSowebnLrdOV5iQjDCTtDASFCA4bT200dPaGrUiLJ2cK3JwVXm8pNNhjK_mvtYTHcB7D-u0O0-S6zz9jtaDJBPPPmjRkrev0Mkr4hO4i7JND0m1ozyhp7miB-2xC4J52MxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdXi-s24y0ll3RdNvzOjX2HzQ-RJORH_r7G9mHJBQIJOYyJzQxX02UNiA9a3tyFDkZXYIDDxirXMRmTsdERIEmZY7Ypl69pXikhygimfWO32LsxaOo8JoL8xJjJaa8sLAcKwrafYoy9jclK8Fcnk4MqmoZd2BxIqdGY2sq7MZyEmpFhVnytOl-B27MAPtN0IBZcpZOFG-MFNu--mfPPCtV9I8xguB-7bxwO6OfAnKhxX-a93GhELLZUSYE1vyW-th_7YPTF8Qe33NrqgDRfJF8Z0dE0mvFoBUD6zm0wIyUSWqgd-l-HfW8rG-PrDmy-TK8pV8duA8fGLj-QMMAV5oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۲ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439342" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcPxzCDASEgdng_5qIz1kHIp1WqDPSk3_Z4hrLvsZZXIRN0HCEc8P0G5BzZZqO_ypUM07va9AsIbkfGU8BnprXkXCvW4nuBvioHXcaFKY05Ao11XiGqwsRZWXKHrHMtLufArMQgE3fc9kdbE2ETAwL1knuIp1C9HwF6Xarrzfzd-lQrtfiYgNMHqZdHlAkzR7MawXBMojZ-v2edfcDvDuYrik4gF4XOot4FF7UE9jQIMiQmlU50LCNTUg8LfPnVhS6TfzQACmEEBSgEKrvuEj1YSe2o0XmkDXFzDrWlCmixVqo_dY5vTOKGJTBdkWf5hGfGC26PNyJ-B3WrD4KdcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U65K-28rVUtu4nZtPVruyoy_YuRNYlBkKxJSbxReSXPDD97DHTrDy3wCeyifD9TgeEiIxRxs1YbF4vs-VTFSe86jxUF1JCcugxGpNLauTPKvchbBV-Zwtd5RbpAun9w4kIqfRKc_K4_qHuyw5euJQs1O_QDUMyER3uHXZJ-81KsVUTj0igMSbC0ruXYYWXVxE0iGcR4a4sagWKZsGrV0ZeJ7znlKs9qLkSxRCshggCr4REpVPbguWU-RQEvwQK60DY-Ys6ksoNT7pwGqRD-MRG3yFsRIBiaUNqmcKVN1NRui-SAw_p0-rSUUsUUDHnmH56ehbod6kSXSRxQGmx0KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbaAvbvfwrovzcDK1nmfjPhwMVNvbLGt3ATPlO_YkAcEXx09ValqAx-5NTMKyzqtkmLZcv-wzlROrzTSTzdqa0xW3x8Mprm9yhCgtapTE3LPrT8wIxX5RedPALdr_s6s9lU5-4wnqUwx885kUXVm-0Ye9RIfJWDWnTdo94JpVyfrPSb70XQEfSCsOlj2A4DMMirZgFdZM_4iuZmIFYCGGedbC8jihuvU7Hw5bfGN4Widn_iLpW3ZiRKy5gkWeGH7oYigUAQH3_AnePCsEOp6nthQAGDL74T4UopTuneYzX_0JassQnEDDfXL24GQzM5aM7YUbfd8evdAh-2dB3LFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsN8FvucAyY1GYU90fbYCzrUEtG9btRKRoeEFSznyM5l4mgDavGAKCXw8zQM6FHpB-x_0RgavePaLe8LPwxmM2SjwiZmARVl-tvwGKTTodSr9zsQeyaa5XrGMx75GQvyYCiDpPnFX8mhIsOmS3AZgPb_kCM9_magC1dXHQ4PpBQL6YvDl2rzVVevEvBgRzB67hBosTf4P0nGKaeWp_9aSh4Qp6QXAEOG5_ixNOxfwW7y-rudY4EiDQY9DiKdZBzFM-XUQYyRSbXKAM2Gh92MVbpe0Izr57C4Gu3Eeh0ZdOyowzsPCkOk7J1BgR6DgFIqiUJZAdxdvtDDR9Sj-wIK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4gqJr9YwYEAtYerDETu9aqgC1fnJWA65GFY4GCIYxEvbXE299rQWvbNw31zVqcWQ8mrru5iRWvaGDBZteVgZnv42FtlhDw--24muQ5IVSuycFcwLqOtNkyO_3Ul6z0GIMAtN8B7BC8YH-kcY16zpJrU6vObCCkayZS3-6fjI2hSjUHldewY6ynMh2XgYx2m2EIJUSLvXbxOmBE1VJ7G-WH3p3FwkGjoGJ4ZAoglQ5rTIRwv1L0Ywdl6_tpPqk7Khs02CXSWUqxwjfgx9jhcOvaEg-ZemlJMmaEYy5QGJveUP5ZIzQBKUNPfcm-5mIxJTOxbKZaQC4hGk5ql7AhMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rC_cFlFCZoWVOh65bKv3jnOgJtxHLKsxR3aLgQPk5JD-dKlnjwBWwWRWMxffUDmSUpkHvhNi4ydZV_wl6unefDtt-xG9-uFXYX9azd1wrX3Ne05ogkA6aPZarg4Hb1m3NOcmiylJ2JHjapJovY0Wt8DrxmYIdu9_O2EAWGOYriTS4kCJWuLr2eMz6pVK2x_UKsNkzV2NVwDcVwt_AZ3yTCqprgu0_F3wkh4YVtyn9Mj2dZFYTxany3fqP0CgmYM1S4o3yzL11D5jN0w6ddJr3LsZZlLJRtFK5KehXXuTyOnfoQoddP6aCLPK6vfV39dShTp3_wahiXeGnX_L-gIw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyyqL581Aty_JgRsbp8kkyM-sU6PY3WaobhkpUdE0N-tcynpXev09uDHTRCFz0tQmANWymqGCrU36Zc93BgiXuAJaMI3HjoFk4e0u5DvNNAVBsCX_xV5CCe_Ci3EbsyX4jrLuW6UOQ_ylvY0GESKDQclztag8hVEj9fW-i0hGkGLUGoWe4mrU-Cft01HwFgBjr4j8Rx5Q3S6k3Wh9S1DCE_pAlLVA4jXLHOu3aPcdZ8Skxl1tPUZR50QGdEAICAfwb0ifTZhNGaD9V9gtrc_8bX9iWMR9XLdnU_5nfsvnwRImDmNDtgD0DIT2fRFeFxLeu7PJ1VF4kQV4VQaxgzg_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdOVUma9tDukgV-F_ImBR8EtyBob5IhNCSZSNM2sWJPtbGE-47BaWNzKsxD9SHaxejVoJzFCHARKlgmNh9fc4THRwp0GIuXvwKvNci4qkApXU7QFkwaA1m_yqSNLHV33RQtMg4diJiKMAuGsOOb3ZgJMLJDIRHUvWmHv4jCuwG2yZQ_V2Dqu79xR8xBTNVVqglvR_4qm8f7FgjxZp5fTY52gJXELBq_wDW52viXJuTAuSH-x6moJFpxLDvutQDKg4_KY5Xx3Fi8ynAuqAi7RtnqPXINzH0GMOtsTuUOjwa35johOIphRGvCuNxD4bzwEKvh7eFu7kkynvtVUwHv-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWKSYy178qQevGYpN-nJ4Gakrjv6DJIxVNrfoQnEpxDXXiUTgHMJCLt9ttjxLRIhfsIST-9HzKubugoEnemspmOwJcuaC4i-7c-XiYbYAnvPkH6Loi27S1ucPmX9oO6yV_HUsT-etoTP9SKnT52Bp-obWbkKPBTInruy5aq7-2AgedVAuTcrc1n7l6oeb8OdDBHrHp82zleRda7FwDX0bRhMwAHjyn5iH7INfjq2cLH26zXEU4iKsgeV-BaD9Nh7Ci62Vpw0lObqii-K2znqbxq1r9vx1UZeFztt4o1FrQ5M33-gyNCymWC_IvIs6KZU6EoqZYvoiZc3zxtaDmIz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQh5-H4CcumHOSvHG-3PGvLRJkgZA3lB4De0tJCKkfjr3CBmDnrDjA8f6jeSNdlHNqlROOOGnygWl4eviuukwWc13sbKXq7CjIicgO8oXgC9fktIJa0Z5hV465Dohciu3PkVykCAcpDGmTqfsAbu9fqQJ9X7Ya1j0fUbyG95xmn4S5_LXXjhngVdHeVOBNJ5EjPlnPFlMkJtOy5jCWi_4Nqpo7RMaYysXorwv2YV96kY708bZCOyovx4ZLS9j8YFT68xTj5_HiJ-N5Uyo56JIDHeet1Tcz7wXyBOwv0XixwDx6KMyXdRopgShYOpBmuCQfvIfwlPMRVOP4oMVcuaIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439332" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqySJgzKs5voSITEacTGTc15JjijWggnAf88oUgw_z4rolYHut9V19KAo7lJEOtSyHHWYGONLdEtYgeNXiVFCBTCUjfuuOh37LE6RHlq_sStngYPsYYpr7rAGjNNxHB4eeKS6RJyk4zrQXA4u3wwCvtuwkeXXkbekWTzkqvRIl47k0stGBR_UG8eqX5zU-a-HXzDuV406GMQwQ3IEASrvLZScJ4tJ0HXCb0bgOTmCReLJPGsy5_7PwQ7E7b_otImicdNoC0XkHt94IqAyOaTVA2nbiGSmD5ryxp6ucFd5am0_ei0n8LcL_cyObAc5FJXNZcT8CwMXGy2T3DNC_aeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در گفت‌وگو با رئیس مجلس لبنان: با ادامۀ جنایت، ضمن توقف گفتگو، جلوی صهیونیست‌ها می‌ایستیم
🔹
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔹
در ۲ روز…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/439331" target="_blank">📅 00:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SK5G2JIpMCGkwHT5Rgnm_KKm_JLR5LykwrsbmhrVc_HM6-u-yzCND77xh1Mxi2UQ8bVqu7nLur9iltdC99tvAPT4Ph2LLrFYACgYWwbqkuRPaoo6OAsvlqCzoM_8uZHy2EizL4Gr7W8hoA9VZbXrCuh6mems49rAVcMHy0hFJnF8idhgIJkygzn_cOXuHLCbplxctFmHTRI3zxV-fIuEhnoLbfUdBbbw_T1tjKOdI-ZSwfrBT7WbOwBYnc_fRsvtmwBtkB7QXDg0_WIkCaZ9YYJwfa8qILDyDI-DQg6yubDspST0R6WDwlahJYLhMsoaMxcyAlTzCetR4W0sj0a4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5hz6ussUAzMptZRBa57RbJAed-MvRG6lwADdcW_6b1RXgT7V22RlgmljlgBYhYgW_-_Xwtrq8t3xHE8Nw71D-kGS1Do4CKlYr_wLEN1kQCKyNSAtpUK30KfIVsCetq3DECLZkcjApCXoNuT3XSq0Nc7zy0kK5yXSYRaR5gmJ6U3QgnSBDf86HtqL_UTP6qpZVJf5g5FQMXyqGr-XQTvcTk5nbrl6mrETQs3nFLfEQNmQY1S7HgVhsIjFfigWCYogvIyWR5aBtGdrIGMXdokkSqMuM835JFv_n3crwSMOKFEEZWivB9cWOAxtktF8sRbWMOz1n44xXIm23XRU2Sz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAEQ7w37krS0HZ22OHc3GTx29n85j-GJv8bqEToxHZ6V0YPMzoJ_xEDWXbHyRn6Il0wVKVUwj2i0VvZgVioFLbvzLN7XJA5KYaT5xpLnFjqpzuz0koa8TZUV45GANG8RPDDrrYvk6s2kWbXpG74pKLGY2sx5SzND_gBrNWk1ZEpMSVd8QkdAT5jdt1hvhOUQu5G-dmCUx4etjCKB1JkL8tuNCj--FvvYK2oTWZvwtBcN7iAyAtbNcE0g469Oi4u_-d1HM1o9NaAjyhXa37lzWpF4OXZbWlueuBiNzkrf18PGj2m4S-nlMGwhdadjvzujvLHxCoXcN1rsOd30xEEw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZ8QoKc067Nn3QWV5RlXOYDch1zZR8SFupgqwK6YeSh5DjXdv_UaPSpyRBCZiJ8-ytzj_pqpPmPybK3rlT4GgzMGw8Fo7T-wrNUKmt7iwsb84xe7yMKjzu6zV4eKZJIBV3wrnCbn0rlTWalG8F92688FljWP0m1Z2Y9IWkwNXi7SMV08eHhxTY2trWqPUVUvFlSnZ97IQ6fTcE7gBBJ_BLiPpEu4MgaRKNlUU-DNjYUAKhSjGJJPItzygsOI3hgV_kbbUHb2jCZPxoIz41aNTIg1yhLS5K1B20ZKhm02huHcXnOuqwXbTuq5mCXfZ53FHb8gHgwYh-qsA1YfCBPP7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
گزارشی از نخستین‌ماه فعالیت نهاد مدیریت آب‌راه خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439327" target="_blank">📅 00:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be983ed74b.mp4?token=sQ1fa1ScV77Ps8YdLNaq4yKXF2RQK1np4gUCApuP1UgXSaheKNkUxHoRzqx4AjpI1Tz3YoxqSDOYgFhW_Nc7FNzE-gR6n3gqEfVOgHzr_Bs1MMDeuJegbWd1gOLr0QkAVtPmGmJHnDWP80oHQf1t0QgB9x7XM7Fe7NhZTw1MEVY4H6QaodrXd3Sk_6xdhlnHn6Jn3OwzuB8v_O__mnE0TUwmFswz5RclQN59qn06zTWFQH_KPM2Uh3YTjF6efYC12Xy2d8kA39z9TUPi5LPIT8dSSHQW4gszK3ewSkz9fAIeS6EapzGGPDZlP05xaJ_AIs0nJVg0ZrRv0zRzG_4uLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be983ed74b.mp4?token=sQ1fa1ScV77Ps8YdLNaq4yKXF2RQK1np4gUCApuP1UgXSaheKNkUxHoRzqx4AjpI1Tz3YoxqSDOYgFhW_Nc7FNzE-gR6n3gqEfVOgHzr_Bs1MMDeuJegbWd1gOLr0QkAVtPmGmJHnDWP80oHQf1t0QgB9x7XM7Fe7NhZTw1MEVY4H6QaodrXd3Sk_6xdhlnHn6Jn3OwzuB8v_O__mnE0TUwmFswz5RclQN59qn06zTWFQH_KPM2Uh3YTjF6efYC12Xy2d8kA39z9TUPi5LPIT8dSSHQW4gszK3ewSkz9fAIeS6EapzGGPDZlP05xaJ_AIs0nJVg0ZrRv0zRzG_4uLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقدام ویژۀ فیفا برای کاروان ایران در مکزیک
🔹
درحالی‌که کاروان ایران برای انتقال به شهر تیخوانا برای برگزاری کمپ خود در جام جهانی آماده می‌شود، نشریۀ اکیپ فرانسه از امنیتی‌شدن فضای شهر مرزی مکزیک به‌خاطر میزبانی از این تیم خبر داد.
🔹
طبق گزارش اکیپ، ٣٠٠ نیروی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/439323" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قالیباف در گفت‌وگو با رئیس مجلس لبنان: با ادامۀ جنایت، ضمن توقف گفتگو، جلوی صهیونیست‌ها می‌ایستیم
🔹
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔹
در ۲ روز گذشته با جدیت توقف حملات اسرائیل را دنبال کرده‌ایم و اگر جنایت‌ها ادامه پیدا کند نه‌تنها روند گفت‌وگوها را متوقف می‌کنیم بلکه جلوی رژیم‌صهیونیستی خواهیم ایستاد.
🔹
ما مصمم هستیم که آتش‌بس در همه‌جای لبنان و به‌ویژه در جنوب این کشور برقرار شود.
🔹
چنانچه توافقی برای پایان جنگ بین ایران و آمریکا شکل بگیرد شامل توقف حملات در همه جبهه‌ها به‌ویژه لبنان خواهد بود.
🔸
رئیس مجلس لبنان ضمن تقدیر از تلاش‌های جمهوری اسلامی ایران برای توقف جنایت‌های رژیم صهیونیستی گفت:
لبنان هرگز مواضع مثبت ایران در این مرحلۀ حساس را فراموش نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/439322" target="_blank">📅 00:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVKPJ8I_X0xGuL61p5KZJ8YuOC5RZW40Py_nAFqKgLEbUivd-3Y0bEMxA6hzPxM5XK8yv12Z2APAVl4D4XXrvAnMYT40hdTyKK-ZSt7ipjH4u_qniPeVs0bERj_v68LZKk5n6T2Ai3ThnxUXyzzeylpgso8ROUwofNlb1UHaMwqPNetsxs-wYD1XJhiNpylB8C3nfexiS8voXUveenNuhnPBSs6QYbxZCATO-_wUcfNzMSfV-y5hVUuaWDOMbQUQHkGxxrI-HdMgeac9z2xtT3gmCNecxDkk0vq7gX0b-KG6bwkWJhtLOTbz7AdCF86KUv4E08rSVi0YV0A6NBbInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی را رد کرد
🔹
نمایندۀ حزب‌الله در پارلمان لبنان: آمریکایی‌ها پیشنهاد دادند که حزب‌الله تمامی عملیات خود را متوقف کند تا اسرائیل هم به ضاحیۀ‌جنوبی و بیروت حمله نکند، این پذیرفتنی نبود.
🔹
مقاومت پیشنهاد آتش‌بس جزئی یعنی خودداری اسرائیل از حمله به بیروت در مقابل توقف حملات به شمال اراضی‌اشغالی را رد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/439321" target="_blank">📅 00:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4E1gwSkCntUWBHq32gnOIsaP48mKwg0qcdTrMc1JZdL-OdxBSFT2_T0wE32fNknBOVDE8XHIoYjWZ32uxPXfs6BHwnebCtgDQznaVh6-q-cIAbkXVNWHA4a3NlWXWAJDlhbmipVn8Lh2_FRQ9hscTtmoL3uOOrXjdHRTX4_OATomoXyF6mlnfng9eaV1cxL853yXLjHN_ZVwan0064cp_2xp-T0XKlZC_w-C0IVr0Yvo1CWmPlhFMm81iqOSjdL5bHZ4WrEESmxVREMsW-hA3MErsjjyshJw5AvhZKXbHjCDTu4uG4c6sKU-YjjEhma2JTLlOkVqJiQOdiQeURMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادتِ درخت
🔹
مردی پیش قاضی رفت و ادعا کرد: «من صد دینار طلا به یک شخص قرض داده‌ام و اکنون او منکر می‌شود و پولم را پس نمی‌دهد.»
🔹
قاضی از متهم پرسید: «آیا این سخن راست است؟»
🔹
متهم با خونسردی گفت: «خیر ای قاضی! من اصلاً این مرد را نمی‌شناسم و هیچ پولی هم از او نگرفته‌ام. اگر ادعایی دارد، باید شاهد بیاورد.»
🔹
قاضی رو به شاکی کرد و گفت: «شاهدی داری؟»
شاکی پاسخ داد: «خیر، ما تنها بودیم. اما در آن لحظه که پول را به او دادم، زیر درختِ بزرگی در بیابان بودیم. آن درخت شاهد ماست!»
🔹
قاضی لبخندی زد و گفت: «بسیار خب! برو پیش آن درخت و بگو قاضی تو را می‌خواند تا بیایی و شهادت بدهی.»
🔹
متهم که در دل به سادگیِ قاضی می‌خندید، آنجا نشست تا شاکی برود و برگردد.
🔹
مدتی گذشت. قاضی درحالی‌که مشغول رسیدگی به پرونده‌های دیگر بود، ناگهان رو به متهم کرد و پرسید: «فلانی، به نظرت آن مرد اکنون به آن درخت رسیده است یا هنوز در راه است؟»
🔹
متهم بی‌درنگ پاسخ داد: «خیر ای قاضی! هنوز نرسیده؛ درخت خیلی دور است!»
🔹
قاضی با خشم بر میز کوفت و گفت: «ای مرد! تو که گفتی اصلاً او را نمی‌شناسی و پولی نگرفته‌ای، از کجا می‌دانی که آن درخت کجاست و چقدر راه است؟ معلوم شد که تو در آن مکان بوده‌ای و آن درخت را دیده‌ای!»
🔹
متهم که غافلگیر شده بود و زبانش بند آمده بود، چاره‌ای جز اعتراف ندید. او اقرار کرد که پول را گرفته و بدین ترتیب، دانشِ متهم از موقعیتِ درخت، بر علیه او شهادت داد.
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/439319" target="_blank">📅 00:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
برخورد مسلمانان با حجاج ایرانی چگونه بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/439318" target="_blank">📅 23:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9ac54a9a.mp4?token=m4ZVL0Juvprxm2CktyGvZbniIuyMxx39rznJB6Uq6jOxN9vNgYoFgHt8Ey31OMlEKHTFniZg3u_T1adXXUHIuV3QSaWXaKL3E1qh7CQgQGmFAEvyopVfsLbNNq0ZqLupX7CnOIzWUNPwIyIApHEIV-k6L0uvofFV_rL2lxd5UAMh2LM4DLsqXHxqMxkbLN51Az3u2cZ6jNYt8UXRJocAmF4cGdzE9n3rWRZu2BtXlgSprbqsEerBYZDoXq3ehBHtW6IzQVzlIHvuHA-GD7ZyTHlrgF_jL_V34EzKeH2p-YOt_ALqpKwC_qOtLHCemclGguo_9X0OFBfZAL8hEY6SkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9ac54a9a.mp4?token=m4ZVL0Juvprxm2CktyGvZbniIuyMxx39rznJB6Uq6jOxN9vNgYoFgHt8Ey31OMlEKHTFniZg3u_T1adXXUHIuV3QSaWXaKL3E1qh7CQgQGmFAEvyopVfsLbNNq0ZqLupX7CnOIzWUNPwIyIApHEIV-k6L0uvofFV_rL2lxd5UAMh2LM4DLsqXHxqMxkbLN51Az3u2cZ6jNYt8UXRJocAmF4cGdzE9n3rWRZu2BtXlgSprbqsEerBYZDoXq3ehBHtW6IzQVzlIHvuHA-GD7ZyTHlrgF_jL_V34EzKeH2p-YOt_ALqpKwC_qOtLHCemclGguo_9X0OFBfZAL8hEY6SkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یک
کشتی با مالکیت آمریکایی-صهیونی هدف قرار گرفت
🔹
نیروی دریایی سپاه: درپی حملهٔ متجاوزانه ارتش تروریستی آمریکا به کشتی ایرانی «لیان استار» در محدودهٔ دریای عمان، در یک عملیات مقابله‌به‌مثل، کشتی MSC Sariska متعلق به دشمن آمریکایی-صهیونیستی هدف موشک کروز قرار گرفت.
🔹
​هرگونه تجاوز ارتش آمریکا در منطقه با پاسخ قاطع روبه‌رو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/439317" target="_blank">📅 23:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439316">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a212e1b27.mp4?token=VibRy12maL4AapjNSSBMwJivzlFe-UQqzKs4HTh3EL44D2_qV8LrXDPvYEnLKvUf4-jVjiw_IrRRm9JFrFqhNYE05nK62io8Wo9I0BgvxukoGEBEky_4f06N7ifKzi9sqJzSSOmSFaELXCMkwI3_-1LeEB7w6OMOgSTfAonU_7NA7wGQnapCZBEgAdS0Km7AXzCsb1Ubo6pvzDe-VCFGlDTg_s5mes7rUTlAGwpliFKEs48OfliiwAqCnwVzbcdJgCpxvGWko_TBDAYCRfUU6tzWAjvdQ9y0PO-lCBqOj2Nnn-q18DUu_zUOlbKKcHNH-9km29U-yRmNAYq0AhU3upj6G7K18MjKJSFCavEqAiLpMEU4sHqIvHkxrPPND-iNDjbx5t9H12nvxaRBSQsaqj32zK0icYiHgnI_jnbMQYQrwzuY2q8QpXd5WiC5OunHcM9P5qMqgFlvhN1HdIl8xAV4lnwdskH_LxfVvtkoJvVj_KKRDOcK4HhDrJvhcAXhtf5NBvkIj11vSC4TdhjA_khAndYN1cf2n3KCmE7yNka5uXmAkjbfPF_JU-9W4Q9HSRJx0n2srj6B9EtxuzJxQB2L0eCkwP8t6PLWOzHcqS5qf6lrsano1lo952tW7A86qhtH0z8uV29q4oQMOIOXBg8AQJRgwMDMlys29Rk9Fmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a212e1b27.mp4?token=VibRy12maL4AapjNSSBMwJivzlFe-UQqzKs4HTh3EL44D2_qV8LrXDPvYEnLKvUf4-jVjiw_IrRRm9JFrFqhNYE05nK62io8Wo9I0BgvxukoGEBEky_4f06N7ifKzi9sqJzSSOmSFaELXCMkwI3_-1LeEB7w6OMOgSTfAonU_7NA7wGQnapCZBEgAdS0Km7AXzCsb1Ubo6pvzDe-VCFGlDTg_s5mes7rUTlAGwpliFKEs48OfliiwAqCnwVzbcdJgCpxvGWko_TBDAYCRfUU6tzWAjvdQ9y0PO-lCBqOj2Nnn-q18DUu_zUOlbKKcHNH-9km29U-yRmNAYq0AhU3upj6G7K18MjKJSFCavEqAiLpMEU4sHqIvHkxrPPND-iNDjbx5t9H12nvxaRBSQsaqj32zK0icYiHgnI_jnbMQYQrwzuY2q8QpXd5WiC5OunHcM9P5qMqgFlvhN1HdIl8xAV4lnwdskH_LxfVvtkoJvVj_KKRDOcK4HhDrJvhcAXhtf5NBvkIj11vSC4TdhjA_khAndYN1cf2n3KCmE7yNka5uXmAkjbfPF_JU-9W4Q9HSRJx0n2srj6B9EtxuzJxQB2L0eCkwP8t6PLWOzHcqS5qf6lrsano1lo952tW7A86qhtH0z8uV29q4oQMOIOXBg8AQJRgwMDMlys29Rk9Fmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ر
وایتی از وقایع ۱۳ و ۱۴ خرداد ۱۳۶۸ و اعلام خبر رحلت امام خمینی(ره) در رادیو
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/439316" target="_blank">📅 23:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439315">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMMDvX9gTXHQz9fMNL_cXKLDKjFr9Q-bHtJ3ubNKYepX2rL1sLIDpDkak-LBc2QQCWMyTA47B_XxoJp1fgVALMuDWLotn2clA4hSRErsY4Y_fsUM_gHYVOeWiwMoztH4cnUHdrTAnj27j1NyjGE7mGjaAR_MvEwgTejz5_kfX20A0Zyp1uGPnwgAY6jMDLjerc9yfVtgIqmKVjlFp1Ens7cSqQyWtHBkgKq5C5HONfYm8dwMyp2p3DsBgTT-ddkRWDiseEWvz_na7OLq3VABkVrit4zys7sApK3Jdbaj3eO3BVESnOUCzylqZGTHQBBgtzVgNMHfGgxnhSs6HF6F1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مردم ایران در مورد جنگ و توافق چه نظراتی دارند؟
🔗
جزئیات نظرسنجی دانشگاه جامع انقلاب اسلامی را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/439315" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439314">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99966d935e.mp4?token=fNGMhA1awVgM53nR_lbed77cSQ9lMOebvgUwglXg3aGnMyKU3LEqAi287O1IUgKEtX_7m1XSRRzeyzbBplqkN0iWWIa5KnstH46djlHsmK5uhKujeJInVmWFHYXkk9IjHn7gclsnpW5hjZw83uvnA9N1TLdYKEeIKZOeK2Yd36UQEoc_62FgvrNf5yTZB9XX77GOTyXrxNZ0MgHSdmy90gRWKg3BMq_Nq_JMQ_Dihcjupt961QbHXyvJC2-Rg2r5_uzZXO8bUIDh8c5HH5QtSFfas2zLpRpBRX0qHwR8ovp03qz47fzvubnxeKWmVJueZpA5DesBpGDvgLhhgc-8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99966d935e.mp4?token=fNGMhA1awVgM53nR_lbed77cSQ9lMOebvgUwglXg3aGnMyKU3LEqAi287O1IUgKEtX_7m1XSRRzeyzbBplqkN0iWWIa5KnstH46djlHsmK5uhKujeJInVmWFHYXkk9IjHn7gclsnpW5hjZw83uvnA9N1TLdYKEeIKZOeK2Yd36UQEoc_62FgvrNf5yTZB9XX77GOTyXrxNZ0MgHSdmy90gRWKg3BMq_Nq_JMQ_Dihcjupt961QbHXyvJC2-Rg2r5_uzZXO8bUIDh8c5HH5QtSFfas2zLpRpBRX0qHwR8ovp03qz47fzvubnxeKWmVJueZpA5DesBpGDvgLhhgc-8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیخ حسین انصاریان مهمونی کیلومتری غدیر امسال را متفاوت خواند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439314" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luM9NhFzHbUonnpYMOpo2i4hU9uFusz7DRJhkM85eDfbONV_j-quR5lYd4-L-IJNJtebLjhqS5uzq3ANNVrt5EtuuH6FDAf6_8Kbk3tgMdVUyS28x6UT0txW-2GzGosUgA-lpfDP00fMQE_0upAxamDbIKq5RMY2yDf5gEr5oYMwsvGfJvKuda0YlPub0u0xUDWZg1t7WFmpAKAgtJeZFC47tYIJQB2yjigf5LrNm-TlKrib-3hpF-aFZlK0bsTl8lkGmUcUroMgqLL3BCk85plY5PjvEu7RZ06t4DgDeKIE0yC3sqGfeKh-vEFQiKE4J613EFlE8GNqHMlmpGSXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swwt_xSnj_ezidXn5T-GAeR9pAYqxM_RaRZuZF2N3Nc4v64syyChE2eqjq02rXrBpdz5DWxlf3L94gsxz2tj0NUObdUiNXnQysH2dzXSuNXczEDVrCZ0ZqrACeCWcTzIymUdh357Nn_8D3rbIJxhwkPDpCq_dxHy-JjDccLMup1Rt-LgOw0qMfgHqvL5vEbvC2r6oaCSwKypFCELsrn3AkTE8K73PglLsGVdstZI881hnz1rrknM8QzD3HrdhT-YPS1D9pQUqYj3798GLvHr_Fv9WFofjMisyib33VLzf52kNlrloxfWn-ik5mGRNSKF5Isspp2kPVdpS_WWlOP4sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHyKGT18JuknWhwjPB978_QAQJmkmlbDxTz_6nTncS23JDj_SygFopiJfVDc_30IDvl_8lTQsUYlg9XWPtONmH30-92vArqkNQncaQmgIf8z8LXTXCwTxF41On8OBShVcx_pgsOEXNNRJCUecVirqkiIccKZ-CGoGHjwl1bRHydlk-q3p3WFUo3rr6MXelQd5vpFs_Wgdn2XSz7JjTXFqp8xkvb0s7GzO9oRm17_ttuQEp-_dQccCxgWzjS00xSQDUL-BIEDNutuWt7jdwWTOtQ8FKxOpn931sMI70Pp0lftLFzZC0aXCX_mKvsVoXItLwgL7pzDhuCn-rlULZMBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ner1PV2X1XME2_TsdU_CYwWqaLCkX-nQGzqGZ_eIO345Hc4mCWk5mI3Tm_QrdnrMEMJSMmS69tYgFyaCh1alUVPfCT0c6JUcZiys47VQfYZN2ZsThjN7qF8Lfk0Qd3EbT90P8bL00hMbWdI0uvTFXLn3_KfZuFbbUOJMM-nqhHKzvOO1Onpto9WakW1zZvkDu5V6qaI_KWIrbJghtYDhDa45Q923Px_-lREDsMQC0w7aYIs67Fxw2CYfywrjY44UOxxAV3he8dNh2qIdW4YGPz5AzwAhweRz7nbC3_ySOR5e7YdKW3kr_m0451W6P8Aho3fGN7faQCvIoi3mvvlEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTmKpoX5IhP7zU2ueEzqHhAyBg-2Owm9ap0CT93LPCaSRKE0GYnEavTnxSXn6Q6FgV4ajRj-iSJ4mHOpsuihNb9yl3vhxkP-jftsg48isyI7Q4-Xgf2qNhCHLAFL4abJVgvtGmKaTAMO5x-ako7uqKGeXunWWRWog4rtlltzYGZYfZ28g0L3uW7-ovMlzqXyKIoNplhjT_2p7vI2DwW_171FQE5ODfGSX9sCjTFdZdTdNso7zugiUQhpU2Sxa_ooVLJm_EKujUvgNLSygolOqOrL0Z-NysLAgOBOXHHEes6cLbvOk1OuZAcQtIzBxBLyOVEBp_tWSzPt0ptw1Zhxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4aPeUQBQmJ8hjVZ_gQQpL70d5f-L-gPt_IasDyvxqmQXaXPM1Z5bC1S0t-w55c1-4nmq3VJU_qITJSu8gHhtVFQ_w3qfPQ-T6u6DrPPrVYImBY3c44TAuIb6RY-reJ-c2R-ibac-qA57KNHR_J2D145WkjQ77Mj4KW1d5strtltqRrqpXRwfP_aoV8PxoXr1hUsnaJebXfK9le5uk7_w5TlV6gtm_17GVyuB3puCeKJl3wYPPinv7vcRIfTgR8ZMwOGl4jJD3MQcwMWejWlXoFLpYKDzwmdagxqwIDZuGtydQTBb11l5rpNNyBzVxMM6NMDYo4enmj5dsgSTMmyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJWHAy7PiEcpWHeuudV6CbmA_RPsMqY9tFIxyHq8KabxsQy1lhWhEnJ1IwDjnp168xZhNyVH9nkCHclP37Utw46Q5a4Rao4TumElu3r8UuKLluX1il1rKjdEeitvf7a4YCVKKSJZ2iThc61nK1H7ceSD_jqirukVUMES8uYuDki-fQny80uKA7vD4xn4_EIdOA0ShrwbdwJh5Fw9RvTorZj-ZDZhHA6Yq0tw6MgyfiqJY4cpvWMSw1jqIHSjzK7eqlvTd3qBFZATkG0bBNQDse95_r_x4LQpzKNoQ-K39WoTivYVPh4AhpjAsgzcsqJg4EmI21Meg3WTYg9TXq9wFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین پرواز بازگشت حجاج به کشور
عکس:
هادی هیربدوش
@farsimages</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439306" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095eba5046.mp4?token=um1VYB28rntby1kA3MA1rj8oOS7OwHdOJ8ih0L21YO_E13Cf9-yUVDb-phjekzuWMjX9Y1bO3S5mGsH-TLOqgy9wwg7osMHVeDF0TZPlZHY2X98PFxoB4eP59We7hLGCbu6UBsegUcn4H7QadAVWe8EdNn3f9WxdM66n2AEgRT5AoSksmdvrgzVrrMSPBocjahps05ho23aSelWCGoBR9XZmqH9hHa2es--e2DCdui01R9lrX7cazFQIzsh7CpN-Tplmw_360IKLOrLeD1pqpQFK9fT0eiz65MThTgrGgFMl7jn8nD7MG-CFlTzTfSArGKQPz83ey13p8Mojil_2nG2faY5ZF7mtxPlgn1WZBiTn9zBZwVquOCpDvPQWQ92HGRi9Cznh9LDHVvhOyI840WAsAFZ7igs2XKTcMcofvC65A1GHMCYKZVNswUEjmFaYF24OfUCtH4WxJmsdkUVXaXSRDYliX17-uPfhaWOPXsAtdR6JODC3tLFChzznOkMWFBRXhJqqqb1FQe-Ds-orOuckFAu9c1gncO8q0Yt4Ve0Ige7Fk-t7lzs36gRcbry-5mGZqORwY0IeYQb5bET8thXHXMEblKcU5B4pYKD-o1R4y_A-C4AH3tQFij87M7t_o2dU0xqEI0Fxktqdricn7R4sRA5LKkW7FUVfsXmmeic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095eba5046.mp4?token=um1VYB28rntby1kA3MA1rj8oOS7OwHdOJ8ih0L21YO_E13Cf9-yUVDb-phjekzuWMjX9Y1bO3S5mGsH-TLOqgy9wwg7osMHVeDF0TZPlZHY2X98PFxoB4eP59We7hLGCbu6UBsegUcn4H7QadAVWe8EdNn3f9WxdM66n2AEgRT5AoSksmdvrgzVrrMSPBocjahps05ho23aSelWCGoBR9XZmqH9hHa2es--e2DCdui01R9lrX7cazFQIzsh7CpN-Tplmw_360IKLOrLeD1pqpQFK9fT0eiz65MThTgrGgFMl7jn8nD7MG-CFlTzTfSArGKQPz83ey13p8Mojil_2nG2faY5ZF7mtxPlgn1WZBiTn9zBZwVquOCpDvPQWQ92HGRi9Cznh9LDHVvhOyI840WAsAFZ7igs2XKTcMcofvC65A1GHMCYKZVNswUEjmFaYF24OfUCtH4WxJmsdkUVXaXSRDYliX17-uPfhaWOPXsAtdR6JODC3tLFChzznOkMWFBRXhJqqqb1FQe-Ds-orOuckFAu9c1gncO8q0Yt4Ve0Ige7Fk-t7lzs36gRcbry-5mGZqORwY0IeYQb5bET8thXHXMEblKcU5B4pYKD-o1R4y_A-C4AH3tQFij87M7t_o2dU0xqEI0Fxktqdricn7R4sRA5LKkW7FUVfsXmmeic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم قم به بیروت: مقاومت تنها نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439305" target="_blank">📅 23:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2391a616.mp4?token=hQCg7JPJ4_ynDTFoUwrtxjBWFnRQE8TdGdoa3SmJquyRfPmaV7qnD0po_jpEkML4VNIUUcOK4-mERCGm-IW72Ti7SQFA99ImZ86qluBgKVEoZibp7j_kUCkT_-nA197S2OCvCrSEFXy-qOmKGpG6edNCU1vqmJjz5dT2QyjQYbnUt9pF-dhLdjkJKIRqEY_ErrMmYBGzNI2YSqNZj8EXwgt2OCdMyFQsUecndNMfavrbss_1TdKO1v03aUvS8jRDab3ZNh92s-gtuXHoSoO244XDXzNHUB1LTAWdhLY4tp9C3l5oG044NLCkgXT5VWP4BUFauR_BGLMCVmUyae5Ojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2391a616.mp4?token=hQCg7JPJ4_ynDTFoUwrtxjBWFnRQE8TdGdoa3SmJquyRfPmaV7qnD0po_jpEkML4VNIUUcOK4-mERCGm-IW72Ti7SQFA99ImZ86qluBgKVEoZibp7j_kUCkT_-nA197S2OCvCrSEFXy-qOmKGpG6edNCU1vqmJjz5dT2QyjQYbnUt9pF-dhLdjkJKIRqEY_ErrMmYBGzNI2YSqNZj8EXwgt2OCdMyFQsUecndNMfavrbss_1TdKO1v03aUvS8jRDab3ZNh92s-gtuXHoSoO244XDXzNHUB1LTAWdhLY4tp9C3l5oG044NLCkgXT5VWP4BUFauR_BGLMCVmUyae5Ojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی کودکان پاوه از تماشای دستاوردهای پهپادی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439304" target="_blank">📅 22:59 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
