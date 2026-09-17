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
<img src="https://cdn4.telesco.pe/file/GCnh-bCLnt0Wqg2N7c1X17BohsVdYaVSj7or_mjxLFuS6ZBRCd9pEM-yeb5lwZupsLKjS2Fm_IbVhY8xylyHe5TZVFgPsr7ijObyMjsMHtUFRTZa2QD20b4IqWC4ACrBj0X5AO15Ag38Nt1M9VALkCIJTUulDTN4OiTQAtfCEJ3NjyNxka_Nx8YXTYAFsTxolJzpgtWXdmxqzHAsk8e7pnsBtg53kQKTv1T36oSzirGAo40cUBOh1FV6o58Lc3Ck_Fgd-rrRnkF4liJv1Ig767xZ1IafbLqOzJDi1C9HSTJdXn9hdN87cOdMca9X_ozUl4yX01RknuhowxrEoyIB5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-690515">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پادگان گروهک‌های تروریستی در «سلیمانیه»
🔹
رسانه «صابرین نیوز» بامداد پنجشنبه گزارش داد که صدای انفجار در منطقه کردستان عراق ناشی از هدف قرار گرفتن مخفیگاه تروریست‌های جدایی‌طلب در منطقه «هه‌لشو» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/690515" target="_blank">📅 01:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGFFOa8bvzWp1MyoGKRqQ3yQv-KchPoV9iuov8TmDN3sSp7OqGpgfZNoICe3Fu7YjJ6woe21ZjHV1hM3Y36gN92eEHOY7GXxkPbDZYgNGJQ5swtUPdeGOBEdt2kmAgkOJhYLHKCsd07XPMI40YBvu8ChtjYyRdbaOVBUbr1wa-nvIn3rYUe7yIyvxN3pDqJmDI39SuHxNtpCidgd58nJxlGUOCCrffJy00YEP5UNXAQlIOZlr-LpGBJc7RQPn1fD6ujFK9Cp2cUmhWfYDMvGkggMlnU-Xonn-Uyybyz54yOwlXhff2DzEeslhh-QwCBzmtT658zJzqSIhV_qrscdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
📚
سال تحصیلی جدید رو با حامین شروع کن!
✨
از
لوازم‌التحریر
،
دفتر
و کتاب تا کوله‌پشتی‌های
جذاب
؛ هرچی برای یک شروع دوست‌داشتنی لازمه، اینجاست!
😍
🛍️
🎁
تخفیف ویژه سازمانی برای خریدهای سازمانی و تعداد بالا
🛍️
حامین، نزدیک شماست!
۶
شعبه در تهران برای یک خرید راحت و لذت‌بخش
👇
📍
شعب حامین در سراسر تهران
🌐
خرید اینترنتی:
Haminstore.com
🎧
پشتیبانی و مشاوره خرید:
📞
۰۹۲۰۶۹۶۸۰۰۱
🔵
کانال بله حامین
برای دیدن محصولات و اطلاع از تخفیف‌ها
:
👇
🔗
http://ble.ir/join/DYPXxvTLNv
صفحه اینستاگرام حامین
https://instagram.com/hamin.store</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/690514" target="_blank">📅 00:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690513">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu5Qe4ZD1CxE0g42cKD6G7qqPwbcNPV5Bzsw_3EMvL9Ty2gSr03kr3bsDRtEeFzj8_BVvoGyl60O752inWuGJhf4xMqfHWVSSA7LUBScdRuUHlR_rWN9JUBEOCgFlbH1kMc4y7odRnbQPZ64Umk7tmK0xfJio_32BV6aBU0BlpFyNjtiQAaSYhZBGR-JhpvVCqIR6jC87ytk8AJwz7zsTqtpQDb5cWYa6yleV0vufmIEMAlkxY-JBS-XquQhrUUpSfCMTwyhllOCBRbhai8fpUwcYwf74E71cL9i6vhXOMrDklPllLbBXYxhHissvfXAJgKsoQ_t-cW2UX9NtXGDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال یه گوشی دوم، سبک و جمع‌وجوری، نوکیا 105 انتخاب خوبیه
👌
🔹
دو سیم‌کارت/ منوی فارسی
🔹
باتری ۸۰۰ میلی‌آمپری قابل تعویض
🔹
چراغ‌قوه و رادیو FM/ صفحه‌نمایش رنگی ۱.۷۷ اینچی/
ریجستر شده
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔴
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
🚚
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63518/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/690513" target="_blank">📅 00:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690512">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orGRKXWYD7MFBAjDuakhm8Pv0ZnfcxT-lOPI35JZ7d0ebc332hhBPjH-TBMhyOfFvVp0rqHv5oj4RYXBsPeQl-kF3_j-D0dPt_YMoJTb42Z7li3BBqZoVEvkVGmJjWku3u0OQcxgRPjc2zz5Mg8pRqu9JZDFesXbNx5dCQSPp5FGDFsNizdH-iVW_aczWBmTioK5rllGgXTjpJ3vtLKIxOK0HUELClDVGu_fgxWtUeaAbbGkjz2RkMuLlAeYKzn_9hH-l6trEGPY9SX4-DgXpKfrNeB4Qq2dZYFeb3MedAnRlE93j8n8NAJfbj-Wc-ZlUzE1P5OU7OLvuFFNzU8hmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواص زنجبیل برای روماتیسم مفصلی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/690512" target="_blank">📅 00:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690511">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای شبکه اسرائیلی: عوامل ایران به موسسه وایزمن هم نفوذ کردند
🔹
شبکه ۱۴ اسرائیل مدعی شد دادگاهی در قدس، چهار ساکن محله بیت‌صفافا را به اتهام همکاری با سرویس اطلاعاتی ایران و انجام اقدامات امنیتی علیه اسرائیل محکوم کرده است.
🔹
طبق این گزارش، متهمان در چارچوب توافق اقرار به جرم، به انجام مأموریت‌هایی از جمله جمع‌آوری اطلاعات برای آسیب‌زدن به یک دانشمند هسته‌ای اسرائیلی، تلاش برای تهیه سلاح و نارنجک و طراحی اقداماتی برای ایجاد خسارت اعتراف کرده‌اند.
🔹
این رسانه همچنین مدعی شده یک مقام ایرانی از طریق ارتباط با یکی از متهمان، او را برای تشکیل یک هسته عملیاتی و انجام این مأموریت‌ها به خدمت گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690511" target="_blank">📅 00:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
فایننشال تایمز: قوانین حمل‌ونقل جهانی و دریایی در حال فروپاشی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/690510" target="_blank">📅 00:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRekNYUBesP40CJOO6DKbyDLt9h4ZUIj5DNPV2pJVn4_FEz6QFputRvnngcG8SI32ktYXIwrfAeQGBHUXN5CBLT8Cu3TzFdcJAYsiubcZZYQ6RtP-g452ZusTY9iNtOL-wlx47VanG34tX4Wg2f7mvBqjWbOkwA9EUHVrUYnsesq6N9cMxgPzDDAbw9sF1p2G1andvgaLW-31jKSbCKNAn25vvspLoB9iFgLrgAXH4qukwksncnSeTl4JGqpC3Qi1AsTqyDL53PQIcIUvLc5rSluAlbQ2c9Ekxnw63aYJMnhRU6poFqWpFijd8bgATG5p4rwTCj8ZjvK5ETbT-cnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/690509" target="_blank">📅 00:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
گزارش لحظه به لحظه از رویارویی امروز نظامی ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3245535
🔹
موج جدید تلاش مافیای لوازم خانگی برای آزادسازی واردات
👇
khabarfoori.com/fa/tiny/news-3245759
🔹
حقوق در ترازوی طلا | پس‌انداز «گرمی»، سقوط «کیلویی» | با یک ماه حقوق ۲۰ سال پیش چند گرم طلا می‌شد خرید؟
👇
khabarfoori.com/fa/tiny/news-3245634
🔹
جی‌دی‌ونس: جنگ ایران طی چند ماه وارد «مرحله‌ای بسیار متفاوت» می‌شود! | فاز جدید جنگ چیست؟
👇
khabarfoori.com/fa/tiny/news-3245604
🔹
جنجال در پرواز؛ مسافر زن برهنه شد، هواپیما فرود اضطراری کرد!
👇
khabarfoori.com/fa/tiny/news-3245446
🔹
خبرهای منتخب هر روز را اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/690508" target="_blank">📅 23:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbqnnV-LDifMsi3NZAshPaT6KSNiiMnNA5RxY8vLieAnM2q2XWWG4fdt4ugi5CIpgDWmJGnmVXfQAyw0GHFmEjALQrU6oiTJru-G-vJvuz5y4mWucKY3ujpBqmq0nk7omrmW7WeULFo_p43iIiUf0oWQQHQhaA7tWijTXytdc8ZRMpbUe4WFzDncSDA5O36nw9hBsYGTxbwFxWHiY7A9imQSjnn4t5kxDwgCPVeixKhRAwvFXW6QIGGaBLpfi087xLjWXbAZVzQDsRcRTY4VcmS36shvvaaad_KxfkvPMaNnG2lMk_-ulkpbp3qOwWt9j8CfYB4Gx8SOemDhzcvYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی امریکایی: جی‌دی ونس می‌گوید که در حال التماس کردن به رأی‌دهندگان است تا در انتخابات میان‌دوره‌ای به جمهوری‌خواهان رأی دهند: «به ما یک شانس دیگر بدهید. به ما چند سال دیگر فرصت بدهید.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/690507" target="_blank">📅 23:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=OhBqnMajqDAQo0YI-2gbViy5wBZnYLqrT3upDGbIsHZ1Tlvp-qpZMjD9BJYDJQjYCm0xkJhBYjjJMd885WOO_RM1T6PVUjpLGiNL-90AlR_T_ChtFdTeMxUaKX-54HTEgZY9_8FmMksmfS1WvUlRnviQgUuyvrZ-8Hs_U7ifIEed5-Zs9x0NVUXr8VkoXX3mGGHuDxDPtSZQiDWs9_2T37J_mMJ8Y6AgblSsfaXVvex00MVennALvZmk3IaKJmgAp4YH31utw3FFbA9cyNnGvpQr61wY2WoZgEAYfIlp2EvnVd8JR_FaOWsPFdCEiJKVhEg84JAdzyF12h0fIFkp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=OhBqnMajqDAQo0YI-2gbViy5wBZnYLqrT3upDGbIsHZ1Tlvp-qpZMjD9BJYDJQjYCm0xkJhBYjjJMd885WOO_RM1T6PVUjpLGiNL-90AlR_T_ChtFdTeMxUaKX-54HTEgZY9_8FmMksmfS1WvUlRnviQgUuyvrZ-8Hs_U7ifIEed5-Zs9x0NVUXr8VkoXX3mGGHuDxDPtSZQiDWs9_2T37J_mMJ8Y6AgblSsfaXVvex00MVennALvZmk3IaKJmgAp4YH31utw3FFbA9cyNnGvpQr61wY2WoZgEAYfIlp2EvnVd8JR_FaOWsPFdCEiJKVhEg84JAdzyF12h0fIFkp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آژانس بین‌المللی انرژی اتمی چه گذشت؟
🔹
روایت رضا نجفی، نماینده دائم ایران، از رقابت ایران و آمریکا در آژانس و اتفاقی که معادلات رأی‌گیری را تغییر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690506" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690505">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: یک پهپاد RQ-۲۰ سعودی را در منطقه حَرَض در استان حَجّه، نزدیک مرز عربستان، سرنگون کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690505" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690504">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3kNlMLnIpKijpSj5kPcHj1I-Oybd9soahkIUxIyuTndRbBd0yDC5WQfoUnOzEcnsNS9jX9HLf7B-sY9uYIXk30EPFBIyp6TtXuiB52f4qpD5Z5bYBuSf8WqTJuvsLuQWjUo_j6RjJnZU1W3AuOJ1FmT47IEd-4YjCac5rGMxR_C_OhReGPlbY-RO-N4WzPoBydRvSAXckOlcV_df-doEmOybEy8LurrvUmgbEV2m3k89LBE1aWIJbd4lKrgnbVuEAV2kZNLvtYur9vM5-w2jnHpsJXPNXCzT6Hz7fzXPWDvd8cj8W20sX5bIZzXAtNbcsXw0LMaEwW7gemis781Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکارگاه
🔹
سپاه اعلام کرد بامداد امروز، پنجاه‌ودومین فروند پهپاد MQ-9 آمریکا در آسمان جزیره قشم رهگیری و منهدم شده است؛ اتفاقی که تنها یک روز پس از اعلام انهدام سه فروند پهپاد MQ-1 آمریکا در یک روز رخ داده است. توالی این موارد در روزهای اخیر، توجه‌ها را بار دیگر به توان پدافندی ایران در شناسایی و رهگیری پهپادهای آمریکایی جلب کرده است؛ به‌ویژه آنکه MQ-9 یکی از پهپادهای پیشرفته و دوربرد ارتش آمریکاست. تکرار چنین رهگیری‌هایی می‌تواند بیانگر افزایش کارایی شبکه پدافندی ایران در مقابله با پرنده‌های بدون سرنشین آمریکا باشد.
🔹
هشتصدوشصت‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/690504" target="_blank">📅 23:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690503">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaclsMG72nOc_c_XsjSQsDIV0-p5EH3l9od5DiDFuI-xbvJQgwywF5TDOk3d5GOTGTu6eldPeBa3zyNR0Tly2JXpvAlD0tB1p6sygbPcxkCEiqVyZdrTXQUFGULJLy5V1ZBK-JVVocgeQA9CEZMaqbLfJYeRP3Ldhrgu2aR8-3iUE0FoD9G4rJllCKvxMU1XXLeBgHqCX9gshVoyXs_SVmpayxJkXsWcDSRXVcR5kaPJAHKqOC1SU3ZkHSg6WkvSfmAMbA1gXSv1o1rqHcPpBRxSZHngdUM4aaLXJNFe_vdHIXtbBgBw3wVgSAPWSoHeIveI21TmEwy-rwzC0IdVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری هادی چوپان: پاینده باد وطن
زنده باد جمهوری اسلامی
🇮🇷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/690503" target="_blank">📅 23:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690502">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6527a4f926.mp4?token=twn_piyDLK-YT8778u-T0eWUkNHtn1PXM0qK-Cthx2A9IneAiN0NQdX2bsweHGRKDQBS1PbnDh7LC4oCSi0Uc-PKXQGuOYrzf7QZhkt4IgfHtS8yTHL0LMISf7HnK-X5_NmyralTHWNEK-uhz1ZCq7JVQKkJub7pQwQIBa8sT1a-L3msoNJKfR_Kes0CvZgPEc97p-Z3J-Ni6OOw7-qqN9kxjgXeJDeT2_w0f-P-sOQQGUCFMfvIfmMtdHJVy0hc636XFwGlBsMXMYxAiHHlTuHAcKZzx-7tih4S5s-WlQZyLHGzIkd-VuP8oRFZFLRpN2Yuj4Np7Hylv305p7s0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6527a4f926.mp4?token=twn_piyDLK-YT8778u-T0eWUkNHtn1PXM0qK-Cthx2A9IneAiN0NQdX2bsweHGRKDQBS1PbnDh7LC4oCSi0Uc-PKXQGuOYrzf7QZhkt4IgfHtS8yTHL0LMISf7HnK-X5_NmyralTHWNEK-uhz1ZCq7JVQKkJub7pQwQIBa8sT1a-L3msoNJKfR_Kes0CvZgPEc97p-Z3J-Ni6OOw7-qqN9kxjgXeJDeT2_w0f-P-sOQQGUCFMfvIfmMtdHJVy0hc636XFwGlBsMXMYxAiHHlTuHAcKZzx-7tih4S5s-WlQZyLHGzIkd-VuP8oRFZFLRpN2Yuj4Np7Hylv305p7s0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توییت کاربر یمنی: جنیفر لوپز در حال رقص در استان مکه در ۱۹ آوریل ۲۰۲۵. ظاهراً تقدس مکه در آن زمان نقض نشده بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690502" target="_blank">📅 23:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690501">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a954fa76a.mp4?token=U4avpNARZFivAzj3NO5RpKva0OgnrQUWBoW5VWUv2J0yKxrz1sJgA9gIubcazarLr89MNPdvRgYP5WSeYINDiMmFirQ9FFWS7axp5kBrRcvomv6E43mneZHMjzvZVjyaB0sx1AjL4lHs1v06AsBjYZyPpTJjeuTiwO-9z4vTzFG25MEWAm7zNqwNtzzTcuo6o9lg2xOotrsbB9AgVd9Audx4fRYVQ5odviV1RFdEd5Scwe47vfXRupLlGH9E1R8fwM-bfgjVt039zL2Cpf2kXib71TwmbGoaO5pc_RJkVe6tP1v2ddHontRYzZzB5CVdziDVr5TKaIy5NUb53SkBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a954fa76a.mp4?token=U4avpNARZFivAzj3NO5RpKva0OgnrQUWBoW5VWUv2J0yKxrz1sJgA9gIubcazarLr89MNPdvRgYP5WSeYINDiMmFirQ9FFWS7axp5kBrRcvomv6E43mneZHMjzvZVjyaB0sx1AjL4lHs1v06AsBjYZyPpTJjeuTiwO-9z4vTzFG25MEWAm7zNqwNtzzTcuo6o9lg2xOotrsbB9AgVd9Audx4fRYVQ5odviV1RFdEd5Scwe47vfXRupLlGH9E1R8fwM-bfgjVt039zL2Cpf2kXib71TwmbGoaO5pc_RJkVe6tP1v2ddHontRYzZzB5CVdziDVr5TKaIy5NUb53SkBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجید شاکری: استفاده آمریکا از بمب اتمی تاکتیکی علیه ایران، قفل استفاده از این سلاح را برای روس‌ها و چینی‌ها باز می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/690501" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=I5wa30zWy4f7xFmhYLYXkxqjNjErTMwwwBk225Za2ddnU1naaXBkYyfnVtLvLv_YYCm7q1Sp_EvaB99M2qwnPxfg2vIK5DbBHN0mZngp4H3Nn66NnTfoSdoP_sV2Oy-wJkp8ka5kpQPbONfTo1WqeuVM_LKbNjJVBY6-isDlNo8QiFgSfy8WH0Ecg-HzyvKUl2VOkDziCU6ApPjdV1cSp3n1jlfonZ4pHCg9RYSZzDZiPqCGavjG2GVzEiwopaPqmf5pj440KpdGfYlCm7QXzfrmkVLDOIi9joM_Hxg_KUnUBQtuZg7rWRKCGMRsKroLfNPJBT3hDpZXQIrKe0rLvGKQ6YRmA7UTeGHXx5XTVkwBW8noNkUzbJSGDqxVUucVMIXMnkcjRG4bcryDBQa7Qrj7XERUkDrRPAzyoNs5D9J47vB7sJzl6PJB61t7NWkGHBWHzYsU-tZmrVjFR9hcKCWrgfwVZre4PgqiP_nJ-xrMwmnD0c3iKQuGIHFjjX2aRVKjmB9RO1Vp1MLrAB1u4a5bJ4OBWuUgz6eaQvDsCIpf_AZyOILU3Wkw3Lz6hip8uxHyMiyPMwc577Zo1DXIzcm9GcfTuZe0xDP-1yTuvE7P7d83Y1v7RE7fkcBTRUIXOd9KvHAKDiQXcOLIlGeDLUI73HXTiDRAGBnrEIOC9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=I5wa30zWy4f7xFmhYLYXkxqjNjErTMwwwBk225Za2ddnU1naaXBkYyfnVtLvLv_YYCm7q1Sp_EvaB99M2qwnPxfg2vIK5DbBHN0mZngp4H3Nn66NnTfoSdoP_sV2Oy-wJkp8ka5kpQPbONfTo1WqeuVM_LKbNjJVBY6-isDlNo8QiFgSfy8WH0Ecg-HzyvKUl2VOkDziCU6ApPjdV1cSp3n1jlfonZ4pHCg9RYSZzDZiPqCGavjG2GVzEiwopaPqmf5pj440KpdGfYlCm7QXzfrmkVLDOIi9joM_Hxg_KUnUBQtuZg7rWRKCGMRsKroLfNPJBT3hDpZXQIrKe0rLvGKQ6YRmA7UTeGHXx5XTVkwBW8noNkUzbJSGDqxVUucVMIXMnkcjRG4bcryDBQa7Qrj7XERUkDrRPAzyoNs5D9J47vB7sJzl6PJB61t7NWkGHBWHzYsU-tZmrVjFR9hcKCWrgfwVZre4PgqiP_nJ-xrMwmnD0c3iKQuGIHFjjX2aRVKjmB9RO1Vp1MLrAB1u4a5bJ4OBWuUgz6eaQvDsCIpf_AZyOILU3Wkw3Lz6hip8uxHyMiyPMwc577Zo1DXIzcm9GcfTuZe0xDP-1yTuvE7P7d83Y1v7RE7fkcBTRUIXOd9KvHAKDiQXcOLIlGeDLUI73HXTiDRAGBnrEIOC9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
این
طاق،
جاودان
است
مرمت
میراث
فرهنگی
، ادامه‌دادن مسیری است برای حفظ بنایی که سال‌ها بخشی از هویت این سرزمین بوده است.
پروژه
مسئولیت
اجتماعی
بیمه‌بازار برای مرمت
مسجد جامع عباسی اصفهان
، حالا وارد مراحل بعدی شده و عملیات بازسازی در بخش‌های مختلف بنا ادامه دارد. کاشی‌های آسیب‌دیده، سنگ‌ها و بخش‌هایی که بیشتر در معرض آسیب بوده‌اند، به‌تدریج در حال مرمت و استحکام‌بخشی هستند.
بیمه‌بازار
؛ در ادامه پروژه مسئولیت اجتماعی
«
طاق
جاودان
»
، همچنان همراه این مسیر است تا سهمی در حفظ و ماندگاری یکی از ارزشمندترین آثار تاریخی ایران داشته باشد
#مسئولیت_اجتماعی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/690499" target="_blank">📅 23:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b90e4877.mp4?token=RaL8GtqYC49wGDNcGQleG7bUm4nhdByoLDqVTFAulHf_bhpUm2PRbSjBHp7Sgw0U8juD_awqy_qcngkX31UKTD3cQ4u1WflY9hmHclwaGIhIjLLYVHVF0K3q7PKNNk4ZDQxjEU7TRXg5I2jN281A9GJnokUaO0Qw6bhY4uRfH0uj4PUd9DjOogw3TjYdnq_h6drNm-3qz732h_RnQiN-55gs55XDLpefbcoOth1tX4VUfjxz00gGotFgoV8IKOvK0s0gI8uxAgoGGJttgzkdmn084sC66twPR7CDM7h9481EuuiYNEInKL57Hl3V_UF3liKviIJTkUND9JL-ePIBoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b90e4877.mp4?token=RaL8GtqYC49wGDNcGQleG7bUm4nhdByoLDqVTFAulHf_bhpUm2PRbSjBHp7Sgw0U8juD_awqy_qcngkX31UKTD3cQ4u1WflY9hmHclwaGIhIjLLYVHVF0K3q7PKNNk4ZDQxjEU7TRXg5I2jN281A9GJnokUaO0Qw6bhY4uRfH0uj4PUd9DjOogw3TjYdnq_h6drNm-3qz732h_RnQiN-55gs55XDLpefbcoOth1tX4VUfjxz00gGotFgoV8IKOvK0s0gI8uxAgoGGJttgzkdmn084sC66twPR7CDM7h9481EuuiYNEInKL57Hl3V_UF3liKviIJTkUND9JL-ePIBoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی پویش ملی جانفدا: در پویش ملی جانفدا تقریبا همه مسئولان تراز اول کشور با هر گرایش سیاسی ثبت نام کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/690498" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd3db3e8f.mp4?token=czgPKmvK4JQz4JdapGeIPE8TRaPN5-EOsCW3TTwBjo2Lzge5muYcrrnKIg0qOqc0wMuzzNoKuklEGM9VdrhHOFB4FzOj789EHyacmhd_Em4basdO6GW71_1ddnSgZWfBKR2kYOY3xIs9vCZHeIDRrE5FwnpXRt7xY_HiuYrl5Sc7IUKaQS6DVdH6YXUSf29__eEcrhbKkfenBCRYRJSMOQI4OLgkK7_TJchaUPJXJdfLJwHNWWJRaGgEJqzG8yJaY0LTtK3QZXC7FZKcQJCED7VCcRrWP2NVyG7GBWl5ThsfR3K8-8CG8zg8VoJrkHvErM1Zw62jlLzIO_ol6YOlykA1sZJMt_8W7xR3sqw7cOaWrJJ6BSqBf4yvQawmj0pLP19RWH279jp8vbdO8GDsA7DyAU3TG3nawBss0SCU9Y_KZUdy5kwQgiTHcA-P77uglVyyq2jh4gkqsA0HiO6vRcsPRES66s_4zHzqxHMkN9Q1iYXAo_FX0WCSYIx2mv_Rmk7-PyYXpe9duadI-nfZtl2tPr_KzGR-Z35QwqGvjbHA6EJvi8XujVkrzZfk_GZWHadfObDTHV-LBjprXoWe4aoNayFmJ-s-oXOUES9sRX0bcleWBzpM-sfYGr-DkabcCYtnq4klZguOD6-HORlo0Wfu1fMYe6Un5c9qJwFnvDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd3db3e8f.mp4?token=czgPKmvK4JQz4JdapGeIPE8TRaPN5-EOsCW3TTwBjo2Lzge5muYcrrnKIg0qOqc0wMuzzNoKuklEGM9VdrhHOFB4FzOj789EHyacmhd_Em4basdO6GW71_1ddnSgZWfBKR2kYOY3xIs9vCZHeIDRrE5FwnpXRt7xY_HiuYrl5Sc7IUKaQS6DVdH6YXUSf29__eEcrhbKkfenBCRYRJSMOQI4OLgkK7_TJchaUPJXJdfLJwHNWWJRaGgEJqzG8yJaY0LTtK3QZXC7FZKcQJCED7VCcRrWP2NVyG7GBWl5ThsfR3K8-8CG8zg8VoJrkHvErM1Zw62jlLzIO_ol6YOlykA1sZJMt_8W7xR3sqw7cOaWrJJ6BSqBf4yvQawmj0pLP19RWH279jp8vbdO8GDsA7DyAU3TG3nawBss0SCU9Y_KZUdy5kwQgiTHcA-P77uglVyyq2jh4gkqsA0HiO6vRcsPRES66s_4zHzqxHMkN9Q1iYXAo_FX0WCSYIx2mv_Rmk7-PyYXpe9duadI-nfZtl2tPr_KzGR-Z35QwqGvjbHA6EJvi8XujVkrzZfk_GZWHadfObDTHV-LBjprXoWe4aoNayFmJ-s-oXOUES9sRX0bcleWBzpM-sfYGr-DkabcCYtnq4klZguOD6-HORlo0Wfu1fMYe6Un5c9qJwFnvDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از اصرار مادرزن تا دلهره‌های پیش از ازدواج؛ گزارش خبرفوری از جشن ازدواج ۱۱۰ زوج جوان
🔹
۱۱۰ زوج جوان تهرانی در جشن ازدواج جمعی گردهم آمدند؛ هرکدام با یک قصه متفاوت، از روزهای آشنایی و تردیدهای قبل از ازدواج تا تصمیمی که در نهایت آنها را پای سفره عقد نشاند.
🔹
از ماجرای دامادی که با اصرار مادرزن‌ در جشن حاضر شد، تا  دلهره‌های شروع زندگی مشترک و زوجی دیگر که با وجود همه سختی‌ها، تصمیم گرفتند برای ساختن آینده دل به دریا بزنند تا دامادی که تعداد سکه های مهریه را فراموش کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/690497" target="_blank">📅 23:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
معاون پزشکیان: حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷ میلیون یارانه به هر نفر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/690496" target="_blank">📅 23:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14519dfcfa.mp4?token=PE8_BntYbeXp7d6-mkonJLTo-8_NWgCl4Sc94GZaoPWWYevsxf6YEzOkcP6YjhqdUzOBmkBUlAx5-nYaE4H1nRyuH6SUr4zD7yPH8ftjsaRC5K5fr_Vq2hWjKKGiklgDej_lXLLj9roytxZ8_pDMTO9YgDlKzt8RbJ1TfZFpeyNLlQ_ZWt7v28P2TmlXW-Am-0axOT4BmwNH2htRDimMCviUunilMjLs88mZYR6odJFAZ-LMH0GhTokyAA664ye-KFOQxcvVfCjleV3gcbs2S8fzGp0DlKSORKXYfPJCIlAde3IXpYs2WAaDjAdv2AlRD5Z-ZYAn85p_creAvJQo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14519dfcfa.mp4?token=PE8_BntYbeXp7d6-mkonJLTo-8_NWgCl4Sc94GZaoPWWYevsxf6YEzOkcP6YjhqdUzOBmkBUlAx5-nYaE4H1nRyuH6SUr4zD7yPH8ftjsaRC5K5fr_Vq2hWjKKGiklgDej_lXLLj9roytxZ8_pDMTO9YgDlKzt8RbJ1TfZFpeyNLlQ_ZWt7v28P2TmlXW-Am-0axOT4BmwNH2htRDimMCviUunilMjLs88mZYR6odJFAZ-LMH0GhTokyAA664ye-KFOQxcvVfCjleV3gcbs2S8fzGp0DlKSORKXYfPJCIlAde3IXpYs2WAaDjAdv2AlRD5Z-ZYAn85p_creAvJQo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشته‌شدنِ دو نفر به‌خاطر یک آینه بغل
🔹
در پی درگیری یک راننده خودرو با موتورسوار بر سر شکستن آینه بغل، موتورسوار پس از تعقیب و ضرب‌وشتم جان باخت. راننده خودرو نیز پس از صدور حکم قصاص، امروز اعدام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/690495" target="_blank">📅 23:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx5WzG0CPGSwRU3rxdh2E1tiWlw0tZJFMWGZPNB0GiDtt4Hkrgo6VNsbC74MkYSY6MyE6v-O4Kh1aAC9_b0MAbkL6ZyS57NInDsqUJd9vY-dF8X0AUuuY7hHV0EEmxhO30ZTAcZ8oWTCh3wQEGf22AUi_i42TTSTdXp7Fn5ngvgT92pFNQwQ2fnYnedPVDuO70sSd-ggUo_qVMmpYb0vfTjF8w5UIOCROM1xfSPUiJtqA50D5D80eSwgmNChkKrkDSMyKqk8fuMrrHQqvswv5eJOQBjV18S3jsgBz63r9Wi6aSOO-a0SEANv8L2ynuMpHPAqyT04Rb2Qjb9uTwzvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار لوازم خانگی و جولان برندهای کره ای؛ جنگ ایران و کره در قلب "امین حضور"/ سلاح خطرناکی که علیه ایران به کارگرفته شد
🔹
ممکن است بازار لوازم خانگی ایران نیز تبدیل به همان سلاحی شود که «چی» خواست از طریق آن، چو را شکست دهد. در واقع، وابستگی بازار لوازم خانگی به برندهای کره ای می تواند همان «گوزن خطرناک» باشد یا مانند اسب تروا عمل کند و مخفیانه اقتصاد ما را فلج کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245776</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690494" target="_blank">📅 23:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf0d19b22.mp4?token=LfMC8igxToL_itlaS-AzEED_uFgukgJ1_o5A8SpLeiaastS6uvu4Rgg4Ceo7EU8VP0vAgPBaZlosmZu10odHXdVgHn_BBdnXoGVayybPasp3pmEmJi6oYn9T1IiKkTiezDmL0xT8Y09Pw2mtKMH5CnJSIKqphIHlNoYSXgUnInUIUIA2ETaMscVgLbUiT7BF3-A6lC8d1t6tiHHh_he9d3tzNWHPfKBIxU2XTjz7We47QgjYiyIXbfMMPEzCpOFrN3FcEROs7jZ1jgxD1NhmtPMGRoNE_Nso2WSaVpbZtr71iOn1zlac-C6z1_JE8iHyoVaKctkEfG_SIx-ks7eNVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf0d19b22.mp4?token=LfMC8igxToL_itlaS-AzEED_uFgukgJ1_o5A8SpLeiaastS6uvu4Rgg4Ceo7EU8VP0vAgPBaZlosmZu10odHXdVgHn_BBdnXoGVayybPasp3pmEmJi6oYn9T1IiKkTiezDmL0xT8Y09Pw2mtKMH5CnJSIKqphIHlNoYSXgUnInUIUIA2ETaMscVgLbUiT7BF3-A6lC8d1t6tiHHh_he9d3tzNWHPfKBIxU2XTjz7We47QgjYiyIXbfMMPEzCpOFrN3FcEROs7jZ1jgxD1NhmtPMGRoNE_Nso2WSaVpbZtr71iOn1zlac-C6z1_JE8iHyoVaKctkEfG_SIx-ks7eNVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با کمی خلاقیت، توی خونه هم می‌تونی خیلی راحت این‌جوری فیلم‌برداری کنی!
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/690493" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMy5p_3t0e7JevOVn5FU4taFJum3-xY1hGOJBPE7OsUhJ8tMu9AQQGDXYB7PhriASt500XRYHx2e13KYS1pSpJmoYqBEtUgzHl2ve9GOiJixLDztDg-dKUE3rSxTZ3wNe7kkm17xuk7WpWRsTlesnYPI8h8hIEl6eHNywyEiL0vJjURDoNxEz8SYtQ3NPOnnkz8VzEpY45RnqBaSP3oVx4p_GMYRP7RR9Wvf9ktMKCE-XFWkr8N3LxymS8bWJn6eAX4VskjlPSJVHEpQS8d_r-whKydAg9fkjX8C2RupUZrQChi69jwi_YBKuREjKyq9tYqq-HAxeBxjibVQylsbgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار اینستاگرامی ایران ۱۰۰ برابر شد!
🔹
بازار فروشگاه‌های اینستاگرامی ایران طی سال‌های ۱۳۹۷ تا ۱۴۰۳ جهشی خیره‌کننده را تجربه کرده است؛ به‌طوری‌که ارزش اسمی این بازار از حدود ۰.۹ همت به ۸۸.۷ همت رسیده است.
🔹
بنا بر گزارش مرکز تجارت الکترونیک، بررسی ارزش حقیقی بازار با حذف اثر افزایش قیمت‌ها نشان می‌دهد که حتی پس از تعدیل تورمی، بازار اینستاگرامی در سناریوی کمینه بیش از ۹ برابر بزرگ‌تر شده است.
🔹
در این میان، چهار حوزه مد و پوشاک، خانه و آشپزخانه، هنری و فانتزی و آرایشی و بهداشتی با حدود ۵۸.۸ همت فروش، ۶۵.۴ درصد کل بازار را در اختیار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690492" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi6JgxIW0D0V-mbdo0zcU4H7W1_QRMmb6L3gRmg5Yyw6DyK0Qy3VUvPQWBQz5cSqARdM-G93CjHmkga8vozt15g11LZWE3buZP3bmuTEujMjL5Ezf1F5wPpC41ZNQPfpjeAX7x501KYlZT411h5F783yMh7f4E5JV-GKcaS252aewYc6yHUW9FNuQSXpWS2lrrmdU0a-L_XpXTPlSGre8nb6c8lX97cbhwPYyeKdQyjJawrBkRqnQf6S-8uqddy0MqUIe1sjSCmaodgXZ9a1XHmD3aV1WMIgDSgFqd0AjM2eSHf8A29_JG35-8448LAvgMDuSTRjbrDzKfP5mno0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۵۰٪ تخفیف برای تبلیغات حرفه‌ای!
یک پکیج، حضور در ۵ پیام‌رسان و دسترسی به بیش از ۲.۴ میلیون مخاطب
🚀
@Titretejarat
📱
روبیکا | ایتا | بله | سروش | تلگرام
اگر می‌خوای کسب‌وکارت بیشتر دیده بشه، این فرصت رو از دست نده
👀
🎁
۵۰٪ تخفیف ویژه برای حمایت از کسب‌وکارها
برای اطلاع از جزئیات و قیمت کلمه‌ی تیتر تجارت رو بفرستید.
@ads_ghimat</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690491" target="_blank">📅 23:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VefXz03x0Ha7gy4DqMRLZ94t2x4OjFghHjZuT1lTgNjDMA0T1RqhDFG-pL4Z9FwXkDvSSfRZ24dBO2xgLUcTq2TQBEINfWmV1-iLuLwmfJblLasNqKls1gLPeGl6hRRSY00VZ12GslEJDXRyit_wI0FgF1tuAS8a2DFErQ4AVkoHV47IP4-MsFdkpAXDxSPqW5SWL4alF4IFR0BI6tl6WZd2t2trfIDXNGBttEGgtahqY0Z8Qhp5O_4o3QvER7wKFfi-TMFOUQZV0P5mRLSEH4SdaNC0dBLEqFC407UlZlqEm2EnYFCqoPD8IuaTRlLum5K77zAxgpG39FDFd8jbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/690490" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFTgRxbYu0BAkuOkHFJHGu5RXr31bGET2W1O1BcYFovD3eizHxDnxxCDuCXt7Q-LAXpZEAzoDewelHZy-6a1MXAuGy7vXrltMl9IF2nH50eElrxETyHLZKVCyUfI3fDZL-378FtmkyCDg_5PV2emGlDNATPJ3RtLPEp5CA9wXHETKd1b5cztgSfZ40KdD6LNSX-0KAv-1RoCYNmJaOiH8-4jyYKVo2YGQ1cIZUA577EF8iKsRfUty4uGhP2GGWeScZobYSB5DWqOFIrANBUVkLUwAMhXw2ekwL9H5FM3pMyXU0k4z4chekAVvRaHv-Pd_a_3Y1u9I9edI-k_SkzuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی آکسیوس، رسانه همسو با صهیونیست‌ها: اکثریت افراد ترامپ را فردی خطرناک و فاسد می‌دانند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/690489" target="_blank">📅 22:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5L75oKA4x1wg6z4ptUwN4xZ6d41twlfmWJoEz1oFPMZmUaNqZzNJTmWyj-KKsWMQCI0XokiZ_8JWlUJp6LSfCTZiAY-KceQIBvy8-vQmDl9zOqDMXBAX_FpD8HeLZ1Ai2nGN4IvQ9gtm81XuGrcoxPnIn0eUVlQqtqf_EIRuwL-WvIMklnqkySQvleddTANRZhiosIYieBueholEdDNSDyrrFas0odxHe2O_jLjFksVull7anLiEXd9WT3uXmee2e9BiJ3IX0ONQaUFqqw1kde-uPr3lneB0HRazfiYwHsSc2kq3fJOUt2z6ImabYXsYfKaOEuMRfsVHBT5Pl3xwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوانه های پر خاصیت برای بدن
🌱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690488" target="_blank">📅 22:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvrfCp8LwGLA827rTZgG2awYlKAqbhL8z2LLxqX-4zTF7HH03D9wgYXZvVNByzua7jPSHqrhtyMk--cVTC4f7uSRocYxIl4G3E64eH7uY3etqTChUZ2x1PsbnZg-CFZqQSt2nvb9kBmJkXnz8iuO8JPHhgaN5QkNQLKxVQw8bEFvEecjM16a16nIYc17ymvBSZ8wRIAq56oD0PuVaOzp82gD_yx0pdPaCe1l6vNCdGoTopP9Wgdz-lYVoNyFortx0w9TECKhMqQD8z824sJsCYN69ul9JNSi2QbZ5T20CXbQQtwveQn1XwZB94yB3LH8sx4Dq2sEZvISLGXFiYP3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vN-vnHph6FoSdVzGGq5by6XQ_6gVFu1Dg_Iiw66iGqhZm6AMNZ_LnKiMRemk9LpeX80kxkb57tnDCcfm7DeBwgvdsSN4iaFQeVObicJkA_MkOwpB6aLchy3XCE8KRsrCB6V4ZcxRDkZqkevWk1KShumB07QB-IEJZ8bT_YyNS2t4qBQE4SvOc72m9w865oYjQQFRD3i-ywH8kS3A60px5OLxEiN5YrztQBowwCLGf0e159NN_2D2HAXWGjz0wvMDBUTL-z0UhoQ6YeWt-Zn9jUPEhjfLB1KDv2fgsYKtb5noq3DfwQCSeiZGQ8Y3q1nBd4Lxj2jXTh9wQ9Peq5VRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ji0Gz0_V34cxIniyWEPZATVhZWKfeRjJChBp1iNp3bITeUfuLjWgM1B1hW8eKLUqAwNMq1GT-5kPPusnSrwMoiuSD4eUrJ4Y959eiZsrO2_Ays0AEb82VLkg1rCC-QQEI_8lzWpi7JkkjJX6734_neqC8PaIMRrj6jenINapjfuS7p4mGVufgvNBqtgxCRaK66FWDJpzPxWGXyxoeTKT-7MlbXKNSNlmO3shMohfebODluHwU8SHZcrLb8dA7RXae4JjVLEbzpkMcu2NgfmGAI03W3mTtLFXM4Yn87lUxok6KaWN8zOPyUQphozfiiZr2-PDwB6W5QBxE5Wn1s3W8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qunl32VWU9hb5pfE75Q3bdoWIvwlTrMpWoMX6vSH3Pq4ib3YQZpWOIjeeYwKI6dTm3zCci_jDtLzCX7slZMoRHE4pgb_soq93uYhszXKg9LPc3Y5gvxTl8ZoiMETybBQ2yhVhPy7tNmUwZhC2qvRrZySdfCeNR9xWAkcmrdq8opsWIQ9mDihL-7OGuU55rt07lCe_apZ5h6_E01qlYjeoc2GuuHnNrjVdmxpKtZgPY771oFk6wyuBy5QjidpP8Q5tryrzUgNyaAJWF3zPRDIIOgOvEigAHu00GXprBqhP8At1OCGGWexw_b90rYA34y3qESU4IVpvgzosC7wDHvnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e72jRaLq8b7SsO-YJLwkq9ImDpZBx-QGh1mHg95b2b8EFpf6Ih32ODO5hhKMUM9p09_d8Eh__oI0HzMf1M1l-pwCjaJO8eOEA_VCvVNPtigtInE8yF2V1zjLOcjge2J53Z8T95uCaRXuT80hlTFFKXlAlq40p1JWFC3Pc7hkIrVHacnfDdfV-MVSE9a1qI_TjMHgXlcRPY_JaokmPi0R1SaDaHEPh91eYcE6EcwicA9_IP5lflB3Cl780gZnCOp1LS0YqjljjBa9W6RP84yxWJA54D0wubc7x5R4g85hy2QpM6A9Oi2krCkJef0KCLzmBGkpMe2jNHqzjDY21V393Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7fbqXUo5UXsh9HVy14XG9e3rosst76l3NqKROl90ADz5w3wMBR-nszVOcbbD-Yu913HlF8iEVhSn4e5Cf-fRI9oVwRbqEcJ_tNZqlqino2d34FpcydCfylPdmG7vx2QrIkMn0qllcmJSRmo7hp1zsvgmNi9Kep5i-rG6JPOlG1gTzKYewxHpj1r8AN_ACgKaLr6zzb4cv721hZEgJvoch2NPulS92T5UQMaBCtrLWpP7glw5B_upiMneZxi8UatHScbYHicFmQ2YOZSaUuTnko8Qz6NlK-f6OukCjkHwMs1pQhJgkdrfcweD6Ju21RDrn9ee9MwjVf6DNcIUmwQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvupzSUYvD5NMcTc1coa-WFc8gLZU9ydgys2Nmqel8nx7MoGyYsGI8HECRBFioI6gn7sxmhf0SbwhvlgVTkYpGLmihXNSWPd6oUzEzcjFUW8dw0VvXDRPgF9X7upboGwNZaM1p202ahfa3iX6jupIxMLQq4t5NVj-EzARfSU9Yc_D25pdgActrsQcd2DDgqLUZ6q7knmbYkMWRYL1uGgtRhUVBddYlzFk8Eib0EaIKMu8QhXyUtslekEm4mXKaYk6v1ILSUtwu1GjYyEaX1_aWe54yC32IcOysBzAo-4sDoWhwj7oEZT3l8wEDqs0Zn428pd6jTkLhyp1bJnZJiWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnj0N2yzE204C7iBvdFa91LhVuZUEKZrVsef1uFFfjwiH4IZdrIKTCvt1dm7vL-H2FAZUKGMGJ95iMHi7fl41E8WdGVsFO6hP-i6_2hZz5G1UtWowXn9glL6Ff1hBsEasdhcQ7xaKTcnU6tHV48Z7WUrzeE3a8uVBat-FE11W101ltqoNmoGz-xcdMhjdFKFTU_nWO87uIcLGbGfHgRu9pZg9YdIP60kzO4-XlOeKeUFI4BQrUL0z4uNglh3QILACSxb8l7z12-svJlzRjkpsjvwf_UpEi9y5AStJs_r7k6kAfWfOA6DexumcH6a8RNyA6dbPs-4i47vqTWrYjwztA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاس پیام‌ها و مشکلات مخاطبین الوفوری در آستانه بازگشایی مدارس.
🔸
روایت خود را در قالب متن کوتاه ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/690480" target="_blank">📅 22:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آمریکا رسما بالا بودن تورم را تایید کرد
رئیس فدرال رزرو (بانک مرکزی ایالات متحده):
🔹
واقعیت این است که تورم بیش از حد بالا است و مدت زیادی است که این وضعیت ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690479" target="_blank">📅 22:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkz7wpQ-Ltd19HpDRPrVSN1WivisIhw4gp9bzc6Jj0ClwsK0XjgP2jx8xkwoDZdmCMYa6Ge0TEdGPBWUFXuuMVNOJSOitEHZTNhZJnsMf0HQ8f_U4jgZMnILlB5YvKCwDbYj8Ltcq4zfYgG-yhPdU0OUMXKFB4gsRNkJitPp2ad8xYE4ZNAQYg_xPXIQQWfm3zqqYij6YLplWiXWRdJo39AZWmTGSFoV50Ec037ZqTpZ4KOjRbsj0zUko4cZX7Fac8Qo__vrC3nbPhMbFZKbDtQAaN_NWQYRxXUzAv2fV6ZVopxTK9IZ_cseLQ5m1A1DKqusKYQT5v0VG2FbmoJicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/690477" target="_blank">📅 22:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/690476" target="_blank">📅 22:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690474">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش ۷.۹ درصدی حیوان‌گزیدگی در کشور
قباد مرادی، رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
در پنج‌ماهه نخست سال ۱۴۰۵، تعداد موارد حیوان‌گزیدگی در کشور ۱۸۰ هزار و ۹۲۲ مورد بوده که نسبت به مدت مشابه در سال گذشته ۷.۹ درصد کاهش داشته است.
🔹
در این مدت استان‌های تهران با ۲۷ هزار و ۲۳۰ مورد، فارس با ۱۴ هزار و ۸۷۱ مورد و اصفهان با ۱۳ هزار و ۷۷۸ مورد، بیشترین موارد حیوان‌گزیدگی را به خود اختصاص داده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/690474" target="_blank">📅 22:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690473">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
واشنگتن پست: آمریکا به اسرائیل چهل هزار بمب ۲۰۰۰ پوندی می‌دهد!
🔹
این اقدام بزرگ‌ترین فروش از  این نوع مهمات در سال‌های اخیر خواهد بود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/690473" target="_blank">📅 22:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690472">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فعالیت تجاری در مرز چذابه روز پنجشنبه از سر گرفته می‌شود/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/690472" target="_blank">📅 22:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690471">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای مضحک ونس: تا زمانی که ایران به هدف قرار دادن کشتی‌ها ادامه می‌دهد، خروج آمریکا از منطقه ناگزیر به معنای بحران انرژی جهانی خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/690471" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690470">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUs8N_CtCXKEOm1t56bkZ9qxIAbJ1_6Yj__tM_8kqF1gFgIh86UlOaBftnlDeVS0Bi-HxptMxF3WCuk8ihAY48UiJ7mtAAaucRjjP3JZ0ztR70JbQN5cnhn_pr2Nf6lGSA861ZGLWWNxr1Lqpy0m2FRgPgQyElixJ03OIwiAMRkX_kbDTdN4Rg7zGAZf5_g0OSrlKLSDF6zJV3omjdX5ktmH6i5Tx9lGUwnv5fvwX_-NTqW6YTrUZdDv8KnfP8vHdISA1lbnEY9msnAWZHg8PYdOPf5Sgqw1GhdcF-jyLDJf0K5Z48jWHqrnsQ2zrrPoJobhbHcuMy2g9czPzPoEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استرس چطور در بدن ما ظاهر میشه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/690470" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690469">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نخستین صندوق سرمایه‌گذاری ارزی کشور با نام «مانا ملت» آغاز به کار کرد
یکی از چالش‌های اقتصاد ایران، نبود ابزارهای شفاف برای سرمایه‌گذاری و به‌کارگیری منابع ارزی است.
در همین راستا، آیین آغاز پذیره‌نویسی نخستین صندوق سرمایه‌گذاری ارزی کشور با نام «مانا ملت» در ساختمان مرکزی سازمان بورس برگزار شد. صندوقی با ضمانت نقدشوندگی بانک ملت که تحت نظارت بانک مرکزی و سازمان بورس فعالیت می‌کند.
در این مراسم، وزیر اقتصاد، رئیس سازمان بورس، مدیرعامل بانک ملت و جمعی از مدیران و مسئولان اقتصادی حضور داشتند و درباره اهداف و سازوکار این صندوق توضیح دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/690469" target="_blank">📅 22:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690468">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA8LqHUHgcXSipCmxs798Y21hQ0xvuMPbMVVPXCJUFD0G6fCBcponCPz43wHu6SOqJHTjfIMfhjW-hE-KvraWDoEJCfYT6rxcYKjba96vEtOSjHyzFeGEUKwzV4GdXgwJ94lsBw4Dr0NjGatQybAld1SlDmZV3Mc9bfATWFgByPDwm5AS21kFfAZcnQgGg5IbzP0jsEBdvyFvyzoxDEUIQ0ZQKpNhP-Qv-D8JTf-W5nYvA5xarA86qB_cjCf_OCsVObJWjWUp73W2CU_9uE-YoAHdJB-DxiLDo0-l7gS4Hp9YEgJlKzMYgjj9NbMd4B2w6QOYyvMWQVroFJE5zH8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧥
کاپشن مردانه مدل Ferrari
🏎
🔥
مشکی طوسی | مشکی زرد
✔️
رویه سه‌لایه مموری
✔️
داخل پشم‌شیشه
✔️
فری‌سایز، مناسب
L و XL
✔️
قد کاپشن ۷۸ سانتی‌متر
✔️
ضمانت تعویض و بازگشت تا ۷۲ ساعت
🔴
قیمت: 2,380,000 تومان
رنگ مشکی زرد
https://memarket24.ir/product/brief/63704/180124/
رنگ مشکی طوسی
https://memarket24.ir/product/brief/63705/180124/</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/690468" target="_blank">📅 22:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690467">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA5RJU96dHIZK6GduFfLmFB17yzR2hIBrZ1NTwdfcbm7oV_6t3yUX12REn1c3wSP5zl1T8AfsZiQO0ULQu_Crws6vlA5O6u72qlFqGtvQDa3G_Z5wQ393TA633K-p6Ffl5lDz255wIbqKpv0GTcV0MCi-0TLkNKTV1x9UL-qiqUJkleO3BkLvXy38SmNcEgumWEhSSfNuNIrl8WcYBPrILj_rU09y0xJ7vuG96cC1uwOjBjyoMHaySnADRwxdcZHoWeTbot2D1lAy-uxt8QsQIgzTMtFXACi_xRLdN43LAl2z0bcjN_ZpyqKCVyZWJRtIw8tk_WlQ0cxF3KvWon8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب: دفاع مقدّس، ملّت ایران را عزیز کرد، روح معنوی را در کشور ترویج کرد. ۱۴۰۳/۰۷/۰۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690467" target="_blank">📅 21:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690466">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ادعای سخنگوی‌سنتکام: ما بیش از ۱۰۰ کشتی را که سعی در شکستن محاصره تنگه هرمز داشتند، تغییر مسیر دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/690466" target="_blank">📅 21:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انجمن صنایع آرایشی و بهداشتی: میزان تقاضای محصولات آرایشی و بهداشتی، نسبت به سال‌های گذشته اندکی کاهش یافته است
علیرضا کیانی، رئیس انجمن صنایع شوینده، بهداشتی و آرایشی در
#گفتگو
با خبرفوری:
🔹
امسال صادرات محصولات شوینده با محدودیت‌های زیادی مواجه شده و سیاست‌های تصفیه ارزی، رفع تعهد ارزی و سایر قوانین صادراتی کشور از جمله موانع موجود در این مسیر هستند.
🔹
با وجود این محدودیت‌ها، احتمال جبران کاهش صادرات محصولات شوینده تا پایان سال وجود دارد.
🔹
تقاضا نسبت به سال گذشته تغییر چندانی نداشته، اما میزان تقاضا در محصولات آرایشی و بهداشتی، نسبت به سال‌های گذشته اندکی کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/690465" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690464">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b0e77466.mp4?token=upFyIVbKIKVBris5R4C1ylEF5A7IWT23wHIVM_8wzuTJHWpL9jM3Fwk8DUKidr6gozbeFgCEcuItSl3APVbzLvri8A5oawtzfamDEX67f2knKdKaysrYFI-KQmRHeqZcr0KlKS7ncwSPDL2bcH3jXCx7aBZ7BbEyh21oWLW1v3BJb103cYLCJ1Y9dZhxFoN6zGwVr9nlJmnXoS6uz7tn1fCmTSTp8xVZKoWvJ-XTHnPqdCuH0esB0UYuaW1g2qhrClcbJKnfBp69rIDiyXLnKZ2V9V2c0Li8Yd-ym9zuEvcyRPMte9Rg0ZYMUnBidERzZe7vUQsFLtO_1jhTZo3H2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b0e77466.mp4?token=upFyIVbKIKVBris5R4C1ylEF5A7IWT23wHIVM_8wzuTJHWpL9jM3Fwk8DUKidr6gozbeFgCEcuItSl3APVbzLvri8A5oawtzfamDEX67f2knKdKaysrYFI-KQmRHeqZcr0KlKS7ncwSPDL2bcH3jXCx7aBZ7BbEyh21oWLW1v3BJb103cYLCJ1Y9dZhxFoN6zGwVr9nlJmnXoS6uz7tn1fCmTSTp8xVZKoWvJ-XTHnPqdCuH0esB0UYuaW1g2qhrClcbJKnfBp69rIDiyXLnKZ2V9V2c0Li8Yd-ym9zuEvcyRPMte9Rg0ZYMUnBidERzZe7vUQsFLtO_1jhTZo3H2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: ورود جان‌فداها به پرونده ناترازی انرژی؛ عملیات ملی در راه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/690464" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNVG2BCagJdEb7A6gZKKKwrMAn00J7qgkEttj2CHDwG6EY-0mKwuns5oZKsOTaNbqYxalNb_byi7uv7KcQ5uuJa0y4BauQjcZqL9qTYsNntFw7hHIs7h69ij7PTkjk13YCxtP_beBTnrG2syaZWY5Z1Fj5glCx8s97RHY1HWmW7QwDk61MEIat_XGAubcU2x-cvmRKuUj75_UzdQcTbuOKIdBKqylk2jVi_s3Q2ZONJkJiw43Ksaq6auvRLP0s7oAmAAKuv3DVkT2TKi3vdqoHlHdIhQOsVBm8sy_qtKj5YnByE9WSW25QTEQPaTcAGDF6NLhoD-iJZvLNAJo_MF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت کاربر یمنی: جنیفر لوپز در حال رقص در استان مکه در ۱۹ آوریل ۲۰۲۵. ظاهراً تقدس مکه در آن زمان نقض نشده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/690463" target="_blank">📅 21:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qm57s9pIRHicC5_-nyb4rqwEDAklOqC6QVJQjnw8Lariu6GtsIGURzfYDTSDCPzU-8_us0PW-zz64z79TucHszEjmyEIUeLecI1MKE2lp5DeTJgFVwjjJYWQjp1PK77W9I_Kh65GdeHK5SKAa2eB0nURXlHPvwcsTxFn-_0QP1dBTRd-pvbobUQqcX8GV8OpE1jQsThZenHNY2ehVHTyqMsYYon0_GIKd9gJXQ4iu4fr57K4cPJWJPC6T26FqSQjNcYzZIfvzJyQWU_aB8d9QUtyHUsA4JnnHXZDK6yiS7TgvBJRmXwe5tj78E5GlndZen3Qeud9GzmBbBbclunwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQRN1lWFH7wrOLMVopWpHSEDv90Ksm2QuuHUHBBPV5Tm9pyJGpfgXMqaeOUeoz6TBPPT7akOrbbr8TZeziYlo1kJIAV25yG2DbcG6dV9cf5B8uEXmwTo0xczfx_lK-aJFlR_vq6F6MLF0TWz7-UXydy8y3xk5277cX-g1ukfkDBNQKQJQ9MUMrQyd10SfFl7k4Ue6q2Cpv9zGTfMFHDfanmgL1KDNnStz0lwBsfg5xVJwbuZwiT7Sn8uJGJJXB0rfVDt_GFfnHCXEH9XWiBsEeBExBcGmP8j_p_Hi-Ck-UxOoaWA5gUiq2e9CmyPTAiUQkkfrE0HF-BIV6F3vgo3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXhYWPXGMZzy7f6xuJqQSI87R73Ikg5wf6eWm4HWe_UPfnNpIQOPbaoIOPvIg-VBHS3nBNJvkfW5ld54vzeCopJyclSY13imAND5hRwZ2rDlbXSF9R1eFkb0GvncYDlLxa8p6GH5-QCAw1XacJD2p_3K-zS91ROCsALODysBy1zTTgZm-XB-trt7sCEL2v7_duhK_dSGQmigMUGWphAcDsnvQKzWBCG-gAzAvQ1MUykMyIxgIYCjti_aXdJ5Fn0pd2EVW3tofDkiobb2h8gIObYUWyUJ052WDoaJStVP4zaNIns9T4FJO8waeFJEk1jqL3kG1NMzI1QxKUuiNcLi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOHfF9r4clL4HvVG8P718vte4TC7rGWlZ4l0cYkJ2xcilKW6Dn1EPTHeZxly0AX5rshmV06VDIVBDkbrTywtk9NvvCgMCdpNJDpGAu5Ok0fNkmUHG5G0fasIufR1fFEIOBzoqT9fpZNAwxD7O1lCDEPVcncD7qM5oansq-bXp87sWgkNFBFn6a9zay7EIh0Rqrr6X3Shnlj5pyeM7Xrz9aPYIW-p4MwJUe-OV40dP-6iZKiaSZpeTD42r7EMPu7c1baDKng5BnSJXB-gPNy-A8M7uGXJm_Clg66jlR6m5qw76lA34dG8YKvknHZNsQpw8j2z2hPZ1fzhgKA5TjChng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRmwwe38auteoLHyN370qzvBhRMp24d46ySYJZBsHsxcydgEvc_PNvVN--YodM3woP2PNn-qPl5cyhNaPBg1Dll1JAoaHxmDWVab0h8wyyfSZ1uAO3aet7nTS1ZwbgFHVtIFuEo_TxcOS89SmkHP7eEaPsG_R55zOYsWtVLNbMWXHNmss6GCEzKmlFVwKvpz-fjoDTpAW2DwUyKDjwffn6lWK55nr_yrMoIP0GydKVAmXgOJHS9K962UB6L8s8eV9IDJf-vF0JdiLlUA9NSNsJsqQpmE7AjsCBa3V_yNBX3QE7iCpZ2DLJKvTmnYYHx2VyTUa4XE7t-PRXx9S90pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijy7VNwgVnBZk3O4sE4zU2zg84WVYHQk0-JARtUSsHph0azRjHhP_d4E78HEpuBI9m-9U2xMyWF_xqwEAFF9oT3MW4zpwRitXqhbHewdemu6yePrjIh3qIqNmvK7f816wjmibAhQLUdqh1FAJKL6Ir37w0R5TSVTTrwp8s9QBnILpLB-32FF1ISqS0n3LVN_qPpa3IuO_srMo-CUQIFHk19SvD2WFDf570B55EK3gcm-V1ly4F8kmpJ0KzoViOdSdIPVF3pZNFevMP6u0a-W1frnhHzV__9x97iOF1V2wfARqkrMWeKILo1DIiTraKPY83YyaGTCF4V-DxmpHqtjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrxyDjGUlZZtNjJw2Qkz3wE-H2lKP_ziFGtFCS64Dr67Q9S-3W3GnC8QKZK7isRJWt4kX1TdvYLLpJPqO-kbeAzIVZXTZVw7EW5f0MEXMurLvmLLq0KMpc6e-eOQ1FOkm85UEiRMQnkajcvVr8waGNC2uBweXsjHbYMFigo7wtiVCBFCtSwvIRSjCpHAGUhROe_TD1u8QXqpad4USqHe9I1APymnEqD82hKzfblbLGPxuZRHg_qvffYZ5mOBeb_YKvX_deYUhDxWy-v1CQZJ436IWcyMRhN5aFZZGSvkV0XtE35VWoNMwT4BhfU8_GfGMeLeHuLuZs4fxCOrctla2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REn7AKq3BM0W1XBvJBtxdLbUlDE3QYTDlhPLxPY632hPnDI8slNppSHIVpT6qyTQDIdOhH6bDAJg6NbcM6bdlHhDYoHPLjSZtfBiOyoacDvx6_kVGAPSKEErgqmxQWhApjA7wgcIy7yX5ub4lcdA5p6QImk54P-L0peGuzBiWCM_-Tj1w3Jsowd1tuHnqygrRDixuFQxdukpSERuw4nwmGV1hRDuzDJfwwL9qx4MeSSv9kE-Xi5UrKCdghAOH-Nm9Dgsg0x-pLc0zwBHBM5BHt64z4dILfn15WQhO8KOad7ma1Vgzwi1-N8HmG7vTPS6rfHtjIbvjanDD99QabMkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzOGZ6Tt0QNeP8OLIsgfs3Fp5zn7hfH_W5q19WZr79I8Qi3RRl4aQiFMeqyDZyWwLgqQrTW-ce6S7CXHxn5163ZM1ypl9Y0NSHTgN8-x-2MnDRvnGBMe0jngq3EUcvGjTeNuKMWSYYMgDKeFURiqsrWAMQWkrsigumVAvshM8djG0JgDgEajnXgCSXa45uGJ0cI16oEE9fIKYEfDEM4ejEQML4248e5WPIv4oujQokkVTHzic4u-NF1K3_Pf_G4qmG8K9CgAd-FP-gNsilP5iwgkiTmqGj0XWW9fY0dra0PV5ubCVUC50IX7Zv00K09vDquIdU5ZUSZ-FHhwptO8bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
سال‌ها همراهی، سال‌ها صبر، و سرانجام شهادت
💫
⚡️
در پنجاهمین  قرار با خانواده‌های آسمانی، میهمان جانباز شهید مهدی سورچی بودیم.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/690453" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
هیئت اعزامی دفتر حضرت آیت‌الله سیستانی در سفر به ایران، از اختصاص و توزیع ۱۱ میلیون دلار کمک مالی میان ۳۶۰۰ خانواده آسیب‌دیده از «جنگ رمضان» خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/690452" target="_blank">📅 21:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: لایحه حجاب، همه نظامات کشور را بهم می‌ریخت/ باید کاری کنیم که باحجاب و بی‌حجاب، برادر و خواهر هم بمانند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/690451" target="_blank">📅 21:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJxX2IBowRKw11pXnyaP1jgm2w2mt1Ic92FicLUTdHiFUkHP22IPq20f6Lx9KCm9wzPp1aCQ-XDRlP-hGa-uXFTZ6eWnXPR6ExKd37-ScP0KpXWc4wf6AC_cB1vTjlQfLbRF9YkfM-FLC6zSg2W2XoVrbi6IVGUcvFMPSNkgcWfxMwS4qxyJrEkiotLU0fRm8ChdXoYFz0fserh5gIFG3V6fHqd3DQKZKgKI_S_jZ6rTshtiJVjvos_Fg_EpUCyD3X_sOga5YrbM-1vBTdnBTp-3kd1yg2cjyG5CGqg1lkLJ93viaR6ReiZAYiiE59RomSvmMQQ5K-rWX10fXBWn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار فعال سیاسی ژئوپلیتیکی: جهان فکر می‌کرد ایران در عرض چند روز سقوط خواهد کرد، حالا ۲۰۰ روز است که استوار ایستاده است. دعا می‌کنم برای پایان این جنگ علیه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/690450" target="_blank">📅 21:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
گچ شرق؛ ایستادگی پای تولید برای مردم و ایران
امید یعقوبی؛ مدیرعامل کارخانه گچ ماشینی شرق و دبیر انجمن گچ استان خراسان:
🔹
با وجود شرایط دشوار روزهای جنگ، کارخانه گچ شرق با تلاش و حضور مضاعف کارکنان، بدون توقف به تولید ادامه داد که این تداوم تولید و حفظ نیروی انسانی در چنین شرایطی، گچ ماشینی شرق را به یکی از نمونه‌های قابل‌توجه در مسیر پایداری تولید و مایه افتخار صنعت کشور تبدیل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/690449" target="_blank">📅 21:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-bHxN1jPEUe-zoSY96lxLLHYRAlRcPc98Qe_LdJSIl1oU5w-GiJKYe1UXA9qzoP5R8O_nhpszbdaXqcrWf3rne1msXAub1m0c0qWJw-dwXzQgTJpHj4kIeA6CO1VZUZzl0GkWw78OGcg_8klBSRoNkr0iMz7eb5T9G9W1Mrp1egimG7sQsd-h15Ehumn6d3OciiUdwdjZ5K44i2y9YxUVLg9J0ivaXfSCQyJrczYuIMgJUvy-e6gwsDwxZ4nHVZudcqdz1dDzHOreZC_-fDI_ZloNh4k_zBTDq4Pud6xZVLBYhzj_-xbW2FNw0t9xmMpH4yt9Xt_wYqh4XiYO3XZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vu-KDTwibkhJqkWc3aK8WdartsAhoym_w_yEWte00ozOsscXs-oDYWxK9_AKnlHoaLCOccUxYU1V_XPyUQMxQuK426f2ESLrq_6Om0qcPviiw1cCuQu_EHHjZ62Sh0LmOYOcOOuOrsfeS7mXkcwWPtX2v3ExSEu0dwXKiVKJELKRqffp-f9NWoNlBUPzp-K-kyalYwVOvyHv2GHd3Dk9UJs_sRGi9WqZCMXGTq2IAmVckI6hr9GLMXyxwiczuuODFdJeu_Q6T0nN0xv9G59QjEe60ALtXxoxRR_8RG-oAlVq3eodiJVErpShDQknfYTsrgCi4QArRRw221_iAuUMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-6CPZRLdohlIK4x7IzGIhsbsFRny1imMcZuMt-b7YBe0DWkC9pb3ZlGBhk2Ey5_LEZ2lFZlEB0Gy1YRLciL18nBbukFM5-WADFGgNPGtPv2cTnRgsXrsBWEbOFMiItvXv6deRr9uu12i4rZOVyjsM_IsLJMVUudlJCHUaHKWX_BkfpJM2kJzRSZrEI5A4a0vouTNWda8eCuZEh6r4QV--wrBCl3_LNHtH6o7KOKIjvfvh7b2sX1uRNA4VzVmrrVPskE7W0EuuSJAC0du2UyJ8RnnW_I1ltdUAmAyQCBwCLcm0SCysbw-BKdm5Z0i-e_4q3CM0XxGLFC7NsOsJ5_9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه باید تا آخر ماه پروپوزالت رو تحویل بدی، این ابزارهای هوش مصنوعی رو از دست نده/ مخصوص دانشجوهایی که هنوز با پایان‌نامه درگیرن
📖
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/690446" target="_blank">📅 21:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690445">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تصاویری کامل از لحظه رهگیری و سقوط جنگنده عربستانی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/690445" target="_blank">📅 20:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDqO83M383qCHkTVP14m2fdJ-No4CuhjcFyD700B7_X5OKw6f5Mo1RPQVOtCB9ufZz3hSc7W3ikvxWx0Vj6zaj0ZHcoRzufdgblY4hiFp-me2E3hWAXMLVzdgkDOiOCrMOGgM56dRNLbxioUJtmsBOhauCqCs25YrQ9OCi6NrMy5G05sfVlHLDFz16nOSvBk5o56ZKIqpS67km-KQyUhZbuatKkzkho9gZoACunfqiCF6YQLyOralTeuSdLOs04zp-nE_Xo4cjjFmP2LGqm-SXMAQj18p9CaYsCyn_UPhm4sBAXWSA-tonYepFuifX_pKO1YKXszxQs6ZljleQedeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgnDV0o8VvZ0lxjX8RDYzjgqWPP1BLai6-LAxmNDYgWLwaMpSfMD_S1M0zYRJMp4yyS7kPe0Xu0RqnuT3oqWGb7OOyz7FFf5Y791zfjY_FXqRqQSaoqZvDNY1DlyAzSwN__u2EbZho37bEUy2ce79qfkPZHvAx2IHYKtHdcmOdVA6Db89ad5wdbvdY3bqZR5mEb8LC9DlTtRqLAV3YD8CMcNArSwePf3Vzp3Kruhs1XKqSUa0H0M48moun-4QMzf0RLxkQrmk0Phzf-UrI4moUep7xL195VM13p53-QYQjHsLkkfcmHP5h473s3q0zLz7dsIm9mEutCviZnqvKBvfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نام چهار تراستی بزرگ ایران منتشر شد
🔹
حسین شمخانی
🔹
روح‌الله رضوی
🔹
علی بایندریان
🔹
محمدهادی مؤمنین/همشهری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/690443" target="_blank">📅 20:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/528eb714d0.mp4?token=N7hBOgVcX73sdlu-PgMWONspmj8sTTr9VS-Kzm3S5UP4L2Nek-VKBIAlaV7sFwX8mdtNMSFwk4BiGfPBZ_kvPsSHWe9ok42YXlWkPjzsmSKLzRUccm0NuoRf9uv17OWceCQO3Jr0I-E9XcgHBak_J4i1iaRLyycqTHz93WvYDyIVwr00Nhe-uO_GyUdCuiytTKDhwp5jzoc_FS9fO5WpjydsaB9fBPlo0tw_3EaCWzAhwL8a0yc-qutKonQvHawZn7BIbRGD41KtGyBn3o_kP_j-wyRQSPAufQnkAd8Q9XsqQzcCOh5BwRUh4at20vRsQedzPm_Wl5GQqQhxGstvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/528eb714d0.mp4?token=N7hBOgVcX73sdlu-PgMWONspmj8sTTr9VS-Kzm3S5UP4L2Nek-VKBIAlaV7sFwX8mdtNMSFwk4BiGfPBZ_kvPsSHWe9ok42YXlWkPjzsmSKLzRUccm0NuoRf9uv17OWceCQO3Jr0I-E9XcgHBak_J4i1iaRLyycqTHz93WvYDyIVwr00Nhe-uO_GyUdCuiytTKDhwp5jzoc_FS9fO5WpjydsaB9fBPlo0tw_3EaCWzAhwL8a0yc-qutKonQvHawZn7BIbRGD41KtGyBn3o_kP_j-wyRQSPAufQnkAd8Q9XsqQzcCOh5BwRUh4at20vRsQedzPm_Wl5GQqQhxGstvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: بعید می‌دانم حتی سازمان‌های امنیتی در جنگ‌ها این‌قدر مورد حمله سایبری قرار بگیرند که به حمدالله هیچ‌کدام از این حملات هم به نتیجه نرسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/690442" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4246385ee0.mp4?token=R-KysYCgMEgiVMNx6oKy1Sin4vtqOUpStdQX7L0BoQpBp8hCaaWfMfhD4ayyzbWiLuc9QMROIIA0gz-UcEW28RIaIshxJkG3EeJBmSLxlzxKpNL1IzuClTQnZQowDf3MNNxJAgODzusmoNYcJrJB4iTBeR7GTGeRJhFPrM1ED4ZeC4g5oUsKxJKrBz1FRb6Xfy2ImhFq8r_mrBGKqdTb8nWNO_taxawWr7wqWnHtiUPHTPABN2M6YxgUR-F2zrdNHp1xSI6IIrhySd5pkuE-fQYakAWTMBw8q78fmP9L9DrHr_eAMzDpqX1MzKl_C6AWXFTHJ3eCHYeTEJmkXhUvaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4246385ee0.mp4?token=R-KysYCgMEgiVMNx6oKy1Sin4vtqOUpStdQX7L0BoQpBp8hCaaWfMfhD4ayyzbWiLuc9QMROIIA0gz-UcEW28RIaIshxJkG3EeJBmSLxlzxKpNL1IzuClTQnZQowDf3MNNxJAgODzusmoNYcJrJB4iTBeR7GTGeRJhFPrM1ED4ZeC4g5oUsKxJKrBz1FRb6Xfy2ImhFq8r_mrBGKqdTb8nWNO_taxawWr7wqWnHtiUPHTPABN2M6YxgUR-F2zrdNHp1xSI6IIrhySd5pkuE-fQYakAWTMBw8q78fmP9L9DrHr_eAMzDpqX1MzKl_C6AWXFTHJ3eCHYeTEJmkXhUvaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: لایحه حجاب، همه نظامات کشور را بهم می‌ریخت/ باید کاری کنیم که باحجاب و بی‌حجاب، برادر و خواهر هم بمانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/690441" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPS3HyAUdUzDfgMqHFr0rRkPa4HweA2HdMEJmHvwqNH4VWW6UzHoiziIfraJQLYAayZqAbkN15bDhvZeQ-VbwE7FlnHsoLyHb4CQIF0rAhAjkwLOeHgsbdnIC-bFNo3KQtERv9IK-73O--xQHHkX9VbqWGbbJiTlTsfoaMeydYuDAQ7unTd_V45jB_DzGSwGqo7ps2krKi7oX2-ue74V7s4thX5YzpYI5XxCnXJIbewxBXUcNMmkhXdqe6ZEX4EuvOsi0mztWNmhR57YJDp4rwv_-kec4CpiBKQoIeRxJTMFaJe1GwaiOn5ZziwqM8s4PtRI7Ff1YgfxvqH12wwW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJP7xE-NMDt850Pft7qByqv1xK0xy_vPatCXp3IU1Uer4TFyJYB8KKmXsv8K7xCVCVssSgaKM1apdcGwWoxrP-IQEfitGfzbYes1V-OpLbGpKymXzPcCxVPx9s9UrTRosd9JupKj5SDhhH7V21qVmSTZNBZmrHw2B0hc4snNefSezQbtAQghq5VNii8kHdCkbmx2bhJ5KZMPUYgUXpcKvdNWVXia1P6eEyWIMWkweUtCPFDh-_kNYWZD-N6E4CzuYh515pt51vdSgvzWJbiCPyyv2Au8kNluVOuvtrGefurpHsp45toTvLoJ_Q4xdItDNczjEG7xnH883a30aW-qwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHxpwJ7QRFyejWLaldwPJ4z2ZOVaHNBCA92s7Q7We12pnBo84pJuoXwmIxOf3kG4C9rSfd7SxwiP0wpEAsCrPMehzCeMdahBgPNe53ystDY9RKRC1twAmkzb6h-QJnNHGw_8JYFXixT-Gle3Q9EtdeOBXMuMCflCafoQKXhcp56sM4W4JLtCgZ4G24X-G57FgShrFfP6vbpIe_lsmOGLub6wKwtkGmQv7XEUKQWFVtFW6Ax-9w0pRdyYZnUPD3Lo5QcWrEbN74tsYZ-BzwQTSIF2e_qBJLIOGcDCucDgEBwVWQzflikHEAv-QU4ubfYZa3qEm5p_sAunWePS9wQ0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HD1zHZZok1LnPbAl5FGwJXNrWzbfPz0KxuSg0_RunfRMIp7Bc9-N29NJ4josBoyJGlomICmxXwVBOH3Z4KrNkOTjLOVtLRyGGmYZIT4-YzAZTd6uKRca-UkkP1eytZVlYzrsV_-H3IW0DQxyeb4WF8hK4AtLETeEtL1jPgVYSojzfrCWPELm8jYuW7Ig7CV8VMM4pw1Nu8XWbV5rsrtTih_uK6Lsm0kf2bb8ZPk6jt4rkJiEQIN7fXtmQ6ilmPYpvnIwFFxd3lrHjw-zol4Gr_J1a7oxyXX4LjyN9i9XWdPHd6AWUY1ENiWLW1RyBnVS4spBzaP-CuDcbyBP4kAVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnLVqka1E09-nVZIcGEnhna8C2zXV0V8Q34SEZMNWlEqs2aZCBLpwNoRMg73Xc7uWIgEZO-94_Dr1H_PqIb9AraV3tuIxVpyhM2u3Czq8POK8FEwcXftQYDCHjjVUzme8Qitm53FpYjjPE7mgBnyLtrffLlbWIFYYKOCjSxgPJOm6tDOekCQAv-NwhU0xulT4WjYVhCs_PQe9C8w0C4lsjU_q8pgNh-OHpWHdC4nqEzVEiW-JHU-PDX8fnjxfT-SkUgXKDI8P1NPI40anG7f7ZwtFcEkIHHdRy4XxMvTVoXb4cdfcoLqS_POn6cITsUhFCOaz5Lbe4VHBapKKYMBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwZUONOWulAnhj4cT-O5fG7czdHCnWTyQ-brTL1CDLsZqBA9pKmeHlv442ojiRhHGrUZbW5JWv1erHRIU3r2MVK8JiLE1nq8YCC_UO74UpQ6xN9_5wCixbN3uhJvEKtSt7ORdPuBGeZj18Xq91YgoeN2kwnc-X24ZuhdXmqD1Kn8z2ugaywwaNDI8VKBAGeSl2A0gA8cX_TjbM4YWP49Sp4dhXsWLOs2BmnNwZY6SLfKv2EBNef6BbAxeVu7ceoG9zS1iF3viN2xp0s3pEksl0-wFS6f2o0eIP0CgyURaZYuCN3I5_LDwiNjA93q2weO8VgmUn0924739IwPf808Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتی رسانه‌های انگلیسی از حمله‌ها می‌نویسند؛ روایت جنگ از نگاه دیگران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/690435" target="_blank">📅 20:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da786da29.mp4?token=YV02ZE4-pbLkA7wE2mEgMh5mY96V_WtSzMkgcjjKN9WLkwAHKtdQwKEFNZgkE87nDsQKTeMrq8g3x00hgLMauIF9fIvLVId1V9NFLh9pj3sjcyzhUPH4q-N7FgbaVWji2OoPTvsSqK2u8zK7-pcqUroaAsBI_N_l7Ow_GVoXESekZPIN5dWd4Cl39nu111V7umKEWQ1VZMbiCQfwaw4yLLNs8atVNNWqJKTxA-cMfX8mFgV4EkYBPOZct6N5dmCvy9Z8jNRhMiPdukosanB0v1EbzmLB1Uv8iU4ZZb9XIZKtczFqrcWao0pgieWeuVU0ZGv04Nve2h5NHhPgE0h4fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da786da29.mp4?token=YV02ZE4-pbLkA7wE2mEgMh5mY96V_WtSzMkgcjjKN9WLkwAHKtdQwKEFNZgkE87nDsQKTeMrq8g3x00hgLMauIF9fIvLVId1V9NFLh9pj3sjcyzhUPH4q-N7FgbaVWji2OoPTvsSqK2u8zK7-pcqUroaAsBI_N_l7Ow_GVoXESekZPIN5dWd4Cl39nu111V7umKEWQ1VZMbiCQfwaw4yLLNs8atVNNWqJKTxA-cMfX8mFgV4EkYBPOZct6N5dmCvy9Z8jNRhMiPdukosanB0v1EbzmLB1Uv8iU4ZZb9XIZKtczFqrcWao0pgieWeuVU0ZGv04Nve2h5NHhPgE0h4fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درآمد گران‌کردن بنزین، معادل فقط ۱ ساعت یارانه پرداختی دولت!/ تلویزیون اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/690434" target="_blank">📅 20:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
قالیباف: ببینم فدرال رزرو با بالا بردن نرخ بهره می‌تواند تنگه هرمز را باز کند یا یک بشکه نفت بیشتر تولید کند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/690433" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
جانشین رئیس سازمان نظام وظیفه: بیرانوند از یکم مهر باید در اختیار یکی از تیم‌های نظامی قرار بگیرد؛ البته پرونده ایشان در حال رسیدگی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/690432" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpoeDsVs18MYto4jVKJ8D18pmJ2CvEpUyCzXuGq4DptA2SDBufC_0k6KEBamsYkCAsSAfwp-KPvc9xyZUHiA-M57R1bOYNFQiTb1nfJsrNGD6XZoTLq3ho0Z8Qk0ktZU_giKdXvBX_OBLdliLrq1mFLhn3BoBA38uzHiq2w1dRxvI1CNkxjG2oqjuuQtnlVBXyAfN5Euo3oe7DFSwZ6Jp5KC_omiqNPH81gVRuw9G1Dt7N2MRxY3zOFf8cPa4-xmcu6HPlnuiYTsqImF8CeUI7UjRRDLnDBp1kPjkIM1J0zh-VpteVwKmnv0wIOszBcJPV2EIwEM0Jo4LipKGMC3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت گازوئیل در آلمان به ۲.۸۰ یورو در هر لیتر رسید
🔹
با احتساب هر لیتر ۶۴۴ هزار تومان، پر کردن یک باک ۶۰ لیتری حدود
۳۸ میلیون‌ تومان
در آلمان هزینه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/690431" target="_blank">📅 20:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9DwgU042tw1bQ_lIStAn15OLGLG7HCNUo5I9wBn_EKlXDSCoUAP9Wa3LEe5K1eykbYXAst0sNXPC9iGLGiOrKMVcOQncByZ7Utq40PuT_KBSm6yDwA8kcjWK21N4SQqlr4Je_flwnNBhXWVksOzj4ccZkItZAPojingnjZcdEPfs6RUKkmuh8NHNdfphyrCrKWpsMyY0oPjxgvPUAZbZkX8J1F3fsPdEBBxyQAEkZAvL4YrvFP1yCt5CEBy5PltYMdRpjRUrjujSup0WWZHKwpvpHElbRTQ2BKyn5cpPUE4aACT6AaR5ocLE3aQhtMYnqnqkF4FTmtkFP6prh2Idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: تأسیسات آرامکو در ینبع و پایگاه خمیس‌مشیط را هدف حمله قرار دادیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/690430" target="_blank">📅 20:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610438ef31.mp4?token=sod0Yix7DyiQlDJcrLGHsXaxv5LaPhzADNq6W9kMT1Gjfimy-16blmUYyZZP43UX_5-zpc93DTL2XbULPH9u9R_QbIBT9V6jTNo2DJFn2DcJa8kfOBRA53zJwcgYmZ9oqFylidqjOGY52AzmPqJRyLTEnaJAjjOl2iHBXraEb5kdG4V8L9iLncdHzNhyfws7PAO94HWuUFVetJ9TCfM6JxvrxXVyHg1vR9LYQygt3CjDh7X-AOnqhvTGkzDS178dqxSbnWj5gQLe0dj9E2REYtZJaZ3ijO5SOsseRG98OVnpMy9pDZ4GogJLdnD9yzHhpIZmHRJzYHyZ5Uq22sMEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610438ef31.mp4?token=sod0Yix7DyiQlDJcrLGHsXaxv5LaPhzADNq6W9kMT1Gjfimy-16blmUYyZZP43UX_5-zpc93DTL2XbULPH9u9R_QbIBT9V6jTNo2DJFn2DcJa8kfOBRA53zJwcgYmZ9oqFylidqjOGY52AzmPqJRyLTEnaJAjjOl2iHBXraEb5kdG4V8L9iLncdHzNhyfws7PAO94HWuUFVetJ9TCfM6JxvrxXVyHg1vR9LYQygt3CjDh7X-AOnqhvTGkzDS178dqxSbnWj5gQLe0dj9E2REYtZJaZ3ijO5SOsseRG98OVnpMy9pDZ4GogJLdnD9yzHhpIZmHRJzYHyZ5Uq22sMEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف
سفیر اسرائیل: به دنبال فراهم کردن آشوب مسلحانه در ایرانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/690429" target="_blank">📅 20:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUQJas1rq_87vBsvLguLoOP4fu8uzDQpXaoLVoMJgI33fi_uAO6-qT5KHRzllIf_eM2DL3VGX0V65JrXIUOpeTzU2A2TELGVu7O4s4qKL241enT0dY3-aMO47GPKNA_GFtWRu1bGTgT9xzB43f1Kc_TZ3XrwhIp7oiuLWJDJjM7IcS7_DbzK1F3w5W7rLqJ3Fi9KtJ9XGzCyt6j4bens60dHMEkT_MNw2-pcNS4zjuR8t7hGS_APzbSqZims-6vRGI4VpiJfvu9w91GEPzYcs_Ee_Y33CygkDvGZmvdVpwQO29arPF5xEn3D6P4o87KUFMqJxfYq_tGdVCk5oLnRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پذیره نویسی نخستین صندوق ارزی كشور از سوی بانك ملت و با حضور وزیر اقتصاد
🔹
آیین آغاز پذیره نویسی نخستین صندوق سرمایه گذاری ارزی کشور با حضور سیدعلی مدنی زاده وزیر امور اقتصادی و دارایی، فرشید فرخ نژاد مدیرعامل بانک ملت و حجت الله صیدی رییس سازمان بورس و اوراق بهادار برگزار شد و بدین ترتیب صندوق ارزی "مانا ملت" با هدف فراهم کردن بستری شفاف، امن و قابل اعتماد برای سرمایه گذاری دارندگان ارز و تبدیل منابع ارزی راکد به منابع مولد و درآمدزا، وارد چرخه اقتصادی کشور شد.</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/690428" target="_blank">📅 20:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رویترز: هزینه جنگ ایران برای آمریکا به ۳۸ میلیارد دلار رسید؛ پیش‌بینی افزایش ۳ میلیارد دلاری در هر ماه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/690427" target="_blank">📅 20:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtg1rfgRJXAhz86ToRX-kgVc38XCat2grAjWtSSBcASc2v7Qk5revl8wxT1s0AB5NJCFP_TsYzwKz2R80CdZZEuekagPTJ0zQRYB6EzdGSKm1RlwQEdEQbHdw3ko4unNYVGx0jXHDEo0r79FGLy_VEVeLrHuOfXQ1i-gIli3wbfJ0RuZuIUr0AdS0J4_eqtJpKF7pIUpC7viwi59GBu5ShJlSX02Ht-uW38vnONe4skzkRTnwldL0oHQ7m5XEYRlXRBk6HrljxESgPKp-Tq3YgY4FPuYg5EeAIe7UvrBc9D8s11RxfhaiPZzrpmsmiKJRkJQP2P--0z4Of9q4cXOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفندهایی که ممکنه به درد خیلی‌ها بخوره #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/690426" target="_blank">📅 20:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
کاتز، وزیر جنگ اسرائیل مدعی شد: ارتش اسرائیل آماده است تا به محض صدور دستور، حماس را نابود کرده و کار را یکسره کند، تا بتوانیم طرح کوچ [ساکنان] را نیز اجرا کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/690425" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBhnEruzPkSwA_24RSBchM8cfo4w_T5S52nyHh90bVyF_qh3U2acftfBpNN1HazrWm-2rrqdL9VwT0DKPdVzPE4Rd3ObwgFZ6hyDO2P_8V5lUt-oujTZzIYGFb5rJXUSU3NuuNHvwIsG05CT-Ma9uZuU-yKysEHCuKtqGKtqSMl1EoUI6N4Goss_Cdu6ASmONJs30ndMuINSF5Og6jf9sZ2w4DWim0oZnmGmw2iCnBpKkrC6k1Y7ylDvKVvEKLMUOnsjrcyuh6HMHc0-aurQTWWvqn8O2huqevmbL_PLw0jO3jl-UWOnVkK-Nn3Tt621kZ94-Q922_AzOSa60A_oRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاشه جنگنده شکار شده توسط یمن، از نوع F-۱۵SA است که جزو پیشرفته‌ترین و مدرن‌ترین جنگنده‌های عملیاتی نیروی هوایی عربستان محسوب می‌شود. ارزش تقریبی این جنگنده مدرن بیش از ۱۱۰ میلیون دلار برآورد می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/690423" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/131e70f8fc.mp4?token=SY1vNU3pT5-bjwK_YdK9ZNnyGvQUpv5ObeOLWlQk_CHTsSg3AwTopyQiU-ZV-GxR0JExlZOHnRwdUVXbhNRFOKJc4wbsqj1N6Vvl1LoPOYVkzxhL09O1ONcdzFjRHDX8x5OH3wdwxfqc28lqj8oTxdUwZ4EHYjAqkMLc7eQib9T8dN3YeDWeaVGxvLYcvHok28UlAjTaZ-QHtfd9e3hXxddLvjrLJ4cGWWhmjIVj8w9DHl62g58xQZ10hXVukj6CLUt6L8GIlCi8vKa7pW8xd9FueUz18pk_NKVpI-5ldFntPlan3QB0oKKHab5cdiYelSg0WofoiO-zIwH8yyElPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/131e70f8fc.mp4?token=SY1vNU3pT5-bjwK_YdK9ZNnyGvQUpv5ObeOLWlQk_CHTsSg3AwTopyQiU-ZV-GxR0JExlZOHnRwdUVXbhNRFOKJc4wbsqj1N6Vvl1LoPOYVkzxhL09O1ONcdzFjRHDX8x5OH3wdwxfqc28lqj8oTxdUwZ4EHYjAqkMLc7eQib9T8dN3YeDWeaVGxvLYcvHok28UlAjTaZ-QHtfd9e3hXxddLvjrLJ4cGWWhmjIVj8w9DHl62g58xQZ10hXVukj6CLUt6L8GIlCi8vKa7pW8xd9FueUz18pk_NKVpI-5ldFntPlan3QB0oKKHab5cdiYelSg0WofoiO-zIwH8yyElPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: آموزش نظامی برای آقایان و بانوان پیش‌بینی شده و ظرفیت اولیه ۱۰۰۰ گردان، در کمتر از ۱۰۰ دقیقه پس از آغاز ثبت‌نام تکمیل شد. ثبت‌نام‌های بعدی در فهرست انتظار قرار گرفتند تا در صورت ایجاد ظرفیت جدید، اطلاع‌رسانی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/690422" target="_blank">📅 19:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea211cc01.mp4?token=jhAo2JZc-ETVNrLI2XTKfNH-crPvTnB8GK2XRfjpzJAIXjW_44SiwewV93uDJ53zndjt5p6uminz6A1UIv9s905Yeu1cRQ9E4xy9Db6E7Ux2dvRv5QlR3RlqrV6PXtQ1DgBplpLrPOzFlEwsQ-3gT4t6y8f_W_3nPDuFcQy8lBEKlrC4HX2CTd0Z9nBC-XBLxFpk9rV2zydKqemMuq_Rwo47DaaMumQdPEkJX1b2M5W5AI-kiiKYPCwaFoKbhVncwZUamobmfBL4OwMmCcSZqdZ3Ig3rM2JUuBqrQziNaL43-UJ35pfHBMcJ_9JDoRbl-_-HXHkxLmIe0iqgtPk7mCI7Aro9VlT6Si8CVfBfa4sOklKmOysHja0zofaZbDaDX7ph9LuxPyaoZQzzzJ0HmerpPAvY_OE06ZKmsLYy_boaH54DoGTC3-PKPevKxf5ZHS1O24s3mm0uk1vF-JLy6AIND1Bx0JrRzhEwy5kJKqTeyIU_j_jBZ_yS3lQziRuQ2tEearVupXjmW8R88seH2rggkuhVYFzzHExYJtNAHVhtAN7TXVdthJwOB_YIuwlhN39sxES7HraDi6tRMdV7yujX4VyAkX1MqZ0O5CKgn2owa5Y4OGWFp_onFNySqOmqu5sImhN1M0TftktLonVUOewjKdK6jpUVSR5ZQ7rRxJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea211cc01.mp4?token=jhAo2JZc-ETVNrLI2XTKfNH-crPvTnB8GK2XRfjpzJAIXjW_44SiwewV93uDJ53zndjt5p6uminz6A1UIv9s905Yeu1cRQ9E4xy9Db6E7Ux2dvRv5QlR3RlqrV6PXtQ1DgBplpLrPOzFlEwsQ-3gT4t6y8f_W_3nPDuFcQy8lBEKlrC4HX2CTd0Z9nBC-XBLxFpk9rV2zydKqemMuq_Rwo47DaaMumQdPEkJX1b2M5W5AI-kiiKYPCwaFoKbhVncwZUamobmfBL4OwMmCcSZqdZ3Ig3rM2JUuBqrQziNaL43-UJ35pfHBMcJ_9JDoRbl-_-HXHkxLmIe0iqgtPk7mCI7Aro9VlT6Si8CVfBfa4sOklKmOysHja0zofaZbDaDX7ph9LuxPyaoZQzzzJ0HmerpPAvY_OE06ZKmsLYy_boaH54DoGTC3-PKPevKxf5ZHS1O24s3mm0uk1vF-JLy6AIND1Bx0JrRzhEwy5kJKqTeyIU_j_jBZ_yS3lQziRuQ2tEearVupXjmW8R88seH2rggkuhVYFzzHExYJtNAHVhtAN7TXVdthJwOB_YIuwlhN39sxES7HraDi6tRMdV7yujX4VyAkX1MqZ0O5CKgn2owa5Y4OGWFp_onFNySqOmqu5sImhN1M0TftktLonVUOewjKdK6jpUVSR5ZQ7rRxJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمارهای توهمی دولت ترامپ درباره تنگه هرمز ادامه دارد
🔹
وزیر انرژی آمریکا امروز چهارشنبه مدعی شد که روز گذشته ۱۸ میلیون بشکه نفت از تنگه هرمز عبور کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/690421" target="_blank">📅 19:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690419">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
اظهارات جانب‌دارانه گوترش، دبیرکل سازمان ملل: ما حملات انصارالله به عربستان و بستن تنگه باب‌المندب را مغایر قوانین بین‌المللی می‌دانیم و محکوم می‌کنیم!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/690419" target="_blank">📅 19:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ-iocmpcgLqHSpU3X2PFUVRp1fDWaVpFQn9WVH5LvJXBhegjZ8OE9NCVxW6ST4SEjSc2mFIrE3FhCcmJV6tbMP3Ieczw1r0xemP4L9zljtoDh-x3bEZanS82Imx1n2WnSWuOTyWDTRW91daQbN-NJhqyNAuI2_aTTW7ejZC1gsVFfaG7EAxSCui0vaE0qcR8WLg8ewY_S_UDVaJFZ_aBKpJmdYOv3-aq76Jd9mAjhP9iJBb5A3Bvr728w_XHmHiqtc7gbAwHe_k56zcrGyQos0g1VWMofkPsjU_oLysbWKzrjZMpoELHSVSISdIZP0ssN8Dag2YqTMd2e9uRIbRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: آمریکا به ویرایش تصاویر و ساختن روایت‌هایی به سبک هالیوود عادت دارد
سردار محبی:
🔹
بد نیست نگاهی هم به لاشۀ آن جنگندۀ اف ۱۵ که در ایران هدف قرار گرفته بود بیندازیم که قطعات آن با فرغون جمع‌آوری شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/690417" target="_blank">📅 19:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afd9da57c.mp4?token=E7R5IwzUK-l_ngMgY1zplCd8yFCPBTavRQWdpfGeM0St-1k0guDVbaccx3J2KuE2n8JtkpSZt24rggNGtuROaobHZkAbMroH_6_ise4tfbWZwneR7Utw0LGJtzJFFIZaYRkk42g5N3HZUTlA0z7K3G_AWd1Xu0-NLOCyC95zaTzAugD_R5laTwnSrsLxgcoQl06ACtLraatc7HWoC86DJ0-qeNFGYZaIqexzkvh-eur-THE70qOMcdQSn35gFD9lofx-fz7spsaEc7EXLJy3kUJgIMLh6sGC5JZqzUhyMdw5S4xhg0wT4igaHyTQvHegtppKWupU8uN-SJEQK2VoSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afd9da57c.mp4?token=E7R5IwzUK-l_ngMgY1zplCd8yFCPBTavRQWdpfGeM0St-1k0guDVbaccx3J2KuE2n8JtkpSZt24rggNGtuROaobHZkAbMroH_6_ise4tfbWZwneR7Utw0LGJtzJFFIZaYRkk42g5N3HZUTlA0z7K3G_AWd1Xu0-NLOCyC95zaTzAugD_R5laTwnSrsLxgcoQl06ACtLraatc7HWoC86DJ0-qeNFGYZaIqexzkvh-eur-THE70qOMcdQSn35gFD9lofx-fz7spsaEc7EXLJy3kUJgIMLh6sGC5JZqzUhyMdw5S4xhg0wT4igaHyTQvHegtppKWupU8uN-SJEQK2VoSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوشش زنده حادثه، خودش به حادثه تبدیل شد!/ بالگرد شبکه NBC هنگام پوشش حادثه اتوبوس در لس‌آنجلس سقوط کرد و ۳ نفر را کشت؛ در حادثه اصلی اتوبوس هم ۲ نفر جان باخته بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/690416" target="_blank">📅 19:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه صنایع پتروشیمی خلیج فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr42Jn5NQGEbvQ5GPOPj9bKNpCsL6OSU1ySQTzc-OOdekXcNgo5YiiMZzuGjfXs9OP6yvxSJ2I8pLYkD2B3a5ChrL9RCo9JDx36EvUWS2giJ8p-YTdmD3feyjT7Hr0gBbc4cg43kc8Y811ASbARzavLhOLpOhCJ9eM2pS02KAL82S9TO_hVQTJX4flxnEBsK372ULJFIRIeAmjfSPsm9s44SRphwQz-R9Vx9xtLn2BKSJLsU36Cn0kFiCXNhvHN7ETueJK7paeVIa8ZtolXhhs9AvbF7S-p7kJX-E0M7A6tz02WjFZpE7szTutBdCb2o0o-Ui4RoE1_yYWiBqcqTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش مجمع سالیانه شرکت صنایع پتروشیمی خلیج‌فارس؛
راهبرد جدید هلدینگ خلیج‌فارس پس از جنگ/ رکورد تولید باوجود جنگ/رشد سود خالص شرکت صنایع ونروشیمی‌خلیج‌فارس به ۱۸۷ همت/ فارس ۶۰ تومان سود تقسیم کرد
🔸
شریعتمداری، مدیرعامل گروه صنایع پتروشیمی خلیج فارس:
🔹
۱۹ پروژه با ظرفیت اسمی مجموع ۹.۲ میلیون تن در سبد سرمایه‌گذاری هلدینگ قرار دارد که مجموع سرمایه‌گذاری موردنیاز آن‌ها ۸.۸ میلیارد یورو و ۴۴۰ همت برآورد شده است.
🔹
طرح‌های فاقد اولویت متوقف یا از برنامه اجرایی خارج می‌شوند تا بودجه و منابع در اختیار پروژه‌هایی قرار گیرد که اولویت بالاتری دارند.
🔹
افزایش بهره‌وری و استفاده کامل‌تر از ظرفیت کارخانه‌های موجود یکی از محورهای توسعه هلدینگ است.
🔹
افزایش سرمایه ۷۵ همتی هلدینگ در آینده نزدیک انجام می‌شود.
🔹
طرح‌های توسعه هلدینگ تاکنون عمدتاً از محل منابع داخلی و سود انباشته تأمین مالی شده و افزایش سرمایه از محل آورده نقدی سهامداران، به‌ویژه سهامداران عدالت، مطالبه نشده است.
🔹
سود خالص تلفیقی هلدینگ با رشد ۱۱ درصدی از ۱۵۷ همت به ۱۷۵ همت رسیده است.
🔹
سود خالص شرکت اصلی نیز از ۱۲۷ همت به ۱۸۷ همت افزایش یافت.
🔹
باوجود جنگ و از دست رفتن۸۵۰ هزار تن محصول، موفق به تولید ۲۷.۳میلیون تن محصول شدیم که نسبت به سال قبل افزایش داشت و رکورد جدید تولید است.
🔹
هلدینگ امکان تولید یک میلیون و ۵۰۰ هزار تن بیشتر را نیز داشت، اما تولید این میزان محصول از نظر اقتصادی حدود ۹۰ همت زیان به مجموعه تحمیل می‌کرد.
🔹
فارس در مجموع ۷۹ درصد ظرفیت اسمی و ۹۱ درصد برنامه تولید خود را محقق کرده است.
🔹
جنگ ۱۲روزه و ۴۰ روزه نشانه‌ای از ضرورت افزایش تاب‌آوری هلدینگ بود و گروه صنایع پتروشیمی خلیج فارس در حال کاهش وابستگی به واحدهای تک‌محصولی و متنوع‌کردن منابع تولید و درآمد است.
🔹
مسیرهای صادرات زمینی برای فروش محصولات به پنج کشور همسایه و انتقال کالا از خاک کشورهای مجاور نیز گسترش خواهد یافت.
🔹
ارزش ساخت داخل در سال ۱۴۰۴ حدود ۹ همت بوده و پیش‌بینی شده این رقم به ۱۱ همت افزایش یابد.
🔗
متن کامل را
اینجا
بخوانید
🌐
@PGPIC1</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/690415" target="_blank">📅 19:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
توافق ایران و ترکیه برای فعال‌سازی مرز جدید در منطقه سلماس
وزیر کشور:
🔹
در حال حاضر سه مرز فعال داریم و مقرر شد یک مرز دیگر نیز در منطقه سلماس فعال شود.
🔹
دو طرف باید مقدمات و زیرساخت‌های لازم را فراهم کنند که این کار آغاز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/690414" target="_blank">📅 19:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690413">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سپاه تهران: ستون دود در اطراف دماوند ناشی از امحای کنترل‌شده مهمات عمل‌نکرده در حومه شهر است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/690413" target="_blank">📅 19:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9d9fde84.mp4?token=uFukK-f2pCw5U6I_xTA7KITY8jZl2T6lRvmjemO2ANgj2cz14Jwfwn4SdaTFB0rD04ebY12HP4f0FJgGHXx3SGspyCFUO3np_aSCvFQQ41aRQD3vWZT9Juil7MC7v9YtVReVk2XhT6e9ew97___bXm6hmE3uhX9r7Qj9aUBRo9SRWEsyU8rQjdj5NAfhEHzDMjsDBE7iT1bSvnczxS8m1RikHclyxmnFRD6RDZdc37csIPsOLYUSyOSasFFyYAXkcnTIhzFe3lAbWJyy-DMEeXCZzShJ4D4-6p_HHohEEKvVhRxvUn3Fq9LsNpQ0E3M2mnXUgEEH3iEedwQydLioszYDOhBCAjgUbn4bdbgG6XltykIQv-DzSM74R_Htz4XbLAonjZY8in_j3Ov98EsgEOCe_ZKiMdRpAtt6sb-UFzCW3EA8Q8jWN4FQKH4Kx1t7Wif0eGQ2RpNqjvfA_88JRK4LRfMjLLB67asNJUGS54V-lpG4_T_tR1kUP2DzeZjcEPHUh1hYsGkOru930f5x5RF6n0Zk3gJDJPJIIcEdd3oyiE0iYLYCvaTfLzg83xlKocsq-CYwbc_39T9sYmJoGQAUWCwicBeo0fXO9iViSjwHlZNYVUHm8_5QhQ9PZIkCrd2JbWulUZ0Fz7Ep7gat_A8qTlczD8FtS08lGCsr624" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9d9fde84.mp4?token=uFukK-f2pCw5U6I_xTA7KITY8jZl2T6lRvmjemO2ANgj2cz14Jwfwn4SdaTFB0rD04ebY12HP4f0FJgGHXx3SGspyCFUO3np_aSCvFQQ41aRQD3vWZT9Juil7MC7v9YtVReVk2XhT6e9ew97___bXm6hmE3uhX9r7Qj9aUBRo9SRWEsyU8rQjdj5NAfhEHzDMjsDBE7iT1bSvnczxS8m1RikHclyxmnFRD6RDZdc37csIPsOLYUSyOSasFFyYAXkcnTIhzFe3lAbWJyy-DMEeXCZzShJ4D4-6p_HHohEEKvVhRxvUn3Fq9LsNpQ0E3M2mnXUgEEH3iEedwQydLioszYDOhBCAjgUbn4bdbgG6XltykIQv-DzSM74R_Htz4XbLAonjZY8in_j3Ov98EsgEOCe_ZKiMdRpAtt6sb-UFzCW3EA8Q8jWN4FQKH4Kx1t7Wif0eGQ2RpNqjvfA_88JRK4LRfMjLLB67asNJUGS54V-lpG4_T_tR1kUP2DzeZjcEPHUh1hYsGkOru930f5x5RF6n0Zk3gJDJPJIIcEdd3oyiE0iYLYCvaTfLzg83xlKocsq-CYwbc_39T9sYmJoGQAUWCwicBeo0fXO9iViSjwHlZNYVUHm8_5QhQ9PZIkCrd2JbWulUZ0Fz7Ep7gat_A8qTlczD8FtS08lGCsr624" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهم‌ترین گلوگاه‌های کشور پس از جنگ تحمیلی سوم و راهکار مدیریت آن/ تلویزیون‌اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/690412" target="_blank">📅 19:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رویترز: بارگیری نفت در بندر اصلی ینبع که در دریای سرخ واقع در عربستان سعودی قرار دارد، متوقف شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/690411" target="_blank">📅 19:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13720a4145.mp4?token=DK9Qgv8h2zq8ytc3iFj8Mmh7emlDxr48jUgyeF923ORq8dPo5oZFCHpEKI-Hs8WTAOuSJoZ2TIhSCkM0FK-AZNnYxLHnNHn0Sym5cdmMwkHbDUYRj4hgoUlMcJZNtB1YUTCW03Qo-C-nOO598ZXhkrN3XLKfoDHTYPYE1ndsQ9Cyc53bZ6dOdj21p_qspUqSuB4N4Y1JJeGndrs0xdUhjDRxot5terc3FzjtoUHRt1fz4nzPTEMjHFmQN-JvJ9w1EFADFSKLRljg7J7-QM1NoQxcA9e8nq5alnaJXuubT4TJSl-lHWgFNQFYYxvezRXv-esoCbTiMD2jC0z6IjCidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13720a4145.mp4?token=DK9Qgv8h2zq8ytc3iFj8Mmh7emlDxr48jUgyeF923ORq8dPo5oZFCHpEKI-Hs8WTAOuSJoZ2TIhSCkM0FK-AZNnYxLHnNHn0Sym5cdmMwkHbDUYRj4hgoUlMcJZNtB1YUTCW03Qo-C-nOO598ZXhkrN3XLKfoDHTYPYE1ndsQ9Cyc53bZ6dOdj21p_qspUqSuB4N4Y1JJeGndrs0xdUhjDRxot5terc3FzjtoUHRt1fz4nzPTEMjHFmQN-JvJ9w1EFADFSKLRljg7J7-QM1NoQxcA9e8nq5alnaJXuubT4TJSl-lHWgFNQFYYxvezRXv-esoCbTiMD2jC0z6IjCidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۱ میلیون ایرانی در «جان‌فدای ایران»؛ مشارکت جوانان و تنوع حوزه‌های داوطلبی
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»:
🔹
از میان ۳۱ میلیون شرکت‌کننده، ۳۲ درصد بانوان و ۶۸ درصد آقایان بودند و بیش از ۶۰ درصد زیر ۴۶ سال سن داشتند. داوطلبان نیز آمادگی خود را در حوزه‌های نظامی و امنیتی، امداد و نجات، خدمات اجتماعی، فرهنگی و رسانه‌ای و پشتیبانی مالی اعلام کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/690410" target="_blank">📅 19:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690409">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d6fe4ecb.mp4?token=e0wW5ssFK2yUDEWHf0Zlaf-2vRc5UjJezXkglIZ8-tBvxL4dFItuPuOeJ4K6RA83eL4IOqgkbwSgWZ82VdWDhiZUHZgqyiGls31reYVwAkxdJKij1lvg__uvZWDmgYdkCfXOKhQ1CrGqrvZzh6mBw9--JFDiXN_9UgcKZpWSF2ln3DyVuG6a0nulUuWmfqBLW-3qzWiNiq7zNREZUSdZVl4sB46gZTPIrmxMqoxRmssAqRZaDZsDdXAL8lIaESu_2FHHnWZK3aYYEjHyQO35xuEJMy1Tf-4j5LWjzAzPXVIAJlqSWNW5ztaTT4fWzvUDQr3DkP_i7tTOdPNsjHPVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d6fe4ecb.mp4?token=e0wW5ssFK2yUDEWHf0Zlaf-2vRc5UjJezXkglIZ8-tBvxL4dFItuPuOeJ4K6RA83eL4IOqgkbwSgWZ82VdWDhiZUHZgqyiGls31reYVwAkxdJKij1lvg__uvZWDmgYdkCfXOKhQ1CrGqrvZzh6mBw9--JFDiXN_9UgcKZpWSF2ln3DyVuG6a0nulUuWmfqBLW-3qzWiNiq7zNREZUSdZVl4sB46gZTPIrmxMqoxRmssAqRZaDZsDdXAL8lIaESu_2FHHnWZK3aYYEjHyQO35xuEJMy1Tf-4j5LWjzAzPXVIAJlqSWNW5ztaTT4fWzvUDQr3DkP_i7tTOdPNsjHPVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنترل ارتفاعات راهبردی باب المندب به دست انصارالله یمن افتاد ⁣
🔹
در ادامه پیشروی‌های منحصربه فرد نیروهای مسلح یمن، کنترل ارتفاعات مهم و راهبردی مشرف بر تنگه باب‌المندب به دست این نیروها افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/690409" target="_blank">📅 18:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690408">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl-wjeg98FeCW5maTDCjMo8MWx73vGmzfNJSP2-g8DPZkyVsMDfqrX0gM4JkKOY0eKxP_GEIgojQTq6XUKizQa_buGJghb1MLdUOx8YISh3y3VPzjKsKn7G3o1BWxZmq6OnvifGJHvpmHYOq3gkHaNvooJHLjAa3qzBjiG0ZmufGC-3L4pu5a5ctjqReQnKysU5zdhy1mOPJsNwh2cLkGCpJynNAA4MhMpV8KpDHoGHzSgjBHv91bNRnKjQcNe5L5RJhErSTqgHcW_HYEMD_2LlEjdIIU_GV4zaUG6-ezMZWkjPnqBzSg6g6vY3f064lvJt9xRtRGOL2RTXY93UQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ریسک تنگه هرمز بر نرخ تورم آمریکا اثرگذار است
قالیباف با اشاره به تصمیم فدرال رزرو:
🔹
افزایش یا کاهش نرخ بهره به‌تنهایی نمی‌تواند تورم آمریکا را مهار کند؛ زیرا انتظارات تورمی تحت تأثیر بسته بودن گلوگاه‌های انرژی، به‌ویژه تنگه هرمز و باب‌المندب، قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/690408" target="_blank">📅 18:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e330b6f59.mp4?token=Jr-6yolciv37cAMBX9G-eyQzHIV_teqwPHpyy93yKAO2EWa0JmUebiK8xOyqlZ2XVtpKO04OiewLbmsCD7dEJ3xl17zL1ihb72tGaP_ytTamMU561TzUmkK5IYPn8tYN5qLx9rKO1Tm0bfvOT1F2oV4rIjDQkDGz_nvJ4X30bUPJJ7rcvFcwAoxuT7v8DlyuxMWPxpSxIiGYoONoFEi0AJ7C4ONXwYL0kz6cnCaFjx0eKOl8npoBBNqe_hswiY1GWFOKOMSwyrcklMWfAQaGqJ7dz56EzKo35rdeM6iLvOZmPFIn1EdVMu-deooTUgFgJqEAdr0HGBYzyORKskDcfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e330b6f59.mp4?token=Jr-6yolciv37cAMBX9G-eyQzHIV_teqwPHpyy93yKAO2EWa0JmUebiK8xOyqlZ2XVtpKO04OiewLbmsCD7dEJ3xl17zL1ihb72tGaP_ytTamMU561TzUmkK5IYPn8tYN5qLx9rKO1Tm0bfvOT1F2oV4rIjDQkDGz_nvJ4X30bUPJJ7rcvFcwAoxuT7v8DlyuxMWPxpSxIiGYoONoFEi0AJ7C4ONXwYL0kz6cnCaFjx0eKOl8npoBBNqe_hswiY1GWFOKOMSwyrcklMWfAQaGqJ7dz56EzKo35rdeM6iLvOZmPFIn1EdVMu-deooTUgFgJqEAdr0HGBYzyORKskDcfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: ۲۷ درصد از جان فدایان اعلام کرده‌اند که حاضرند روزانه چند ساعت را به این پویش اختصاص دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/690406" target="_blank">📅 18:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت نیرو از پایان قطعی‌های برق خبر داد
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو در
#گفتگو
با خبرفوری:
🔹
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد.
🔹
پس از پنج ماه کار مداوم نیروگاه‌های حرارتی، بیش از هزار مگاوات از نیروگاه‌ها برای انجام تعمیرات اساسی از مدار خارج شده‌اند تا با آمادگی حداکثری به مدار تولید بازگردند.
🔹
ظرفیت نیروگاه‌های تجدیدپذیر خورشیدی اکنون حدود ۶ هزار مگاوات است و امیدواریم تا پایان سال به ۱۲ هزار مگاوات برسد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/690405" target="_blank">📅 18:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
نماینده پارلمان کره جنوبی: ترامپ می‌خواهد ما را هم تبدیل به بازنده کند ، در نهایت این ما هستیم که در تقابل مستقیم با ایران تنها می‌مانیم و تاوانش را می‌دهیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/690404" target="_blank">📅 18:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLssUNmIHf02-rptoV_D6rdGPw1fF1lAAefMsc9erL1pRQDI-6Jbb0SqzWktwrA4uWLw1nr2bSpiGsvkZoMaSvM-Pp4Mmxz5fGR4RDcQQnJtn0QXrZwKKwVPle5fhO8zUZ8dnSB7Lr5ERzWJZ9XCB_gDBCJYZjlsW5ubTFjFwfdevfZ4DpluUP88rbpg5cZfR-venYMTpsAQ4bARnw4y3jR5vJ_EvQP6orLOI8XX1-AyfENgwSxXGZ76D0ojX5JDFXmYLO51Xu33wlEB6AU93qc8FqEaWT0LWzbjPOOCcwDurqNSZwx0y97fVwiPRHf1W3DlhAtUsmEvZUroaq3kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا سپاه شرکت آمازون را در بحرین هدف قرار داد؟
🔹
سپاه پاسداران انقلاب اسلامی شرکت آمازون را در بحرین مورد هدف قرار داد. این شرکت چه اهمیت نظامی دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/690403" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a063d53ac0.mp4?token=cPWVX2SZKGOdRM8O9EPFNsdG1VmerqR7SFzKEbVFF2iD8ur46y9J_XUMI3ucFEbZGWET4eAZcKcpCMh3AOsFESWbB8c9ZTgvmuskN2yo8rvYi7G0-zHk3Vx22a4aGDof25dplBUhlqemqGryJ8nhFe5OFhooWYNNJfgpGPbqC85Px1-WAMBRq89VT6S2SAllNiGWDZgzg2CrxJYGxA2sfAUBxJ23kHtyogLTXeI7_SIa8UGWwowFum4QHPMpiiF_iRfb6c8_AGkSam05v1wRtggPIepVjRkE5a6XLPHTSwWU4tCZW8BeisJM7zpkJ2w60dfpIeEmTRQDbrMiMKEFkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a063d53ac0.mp4?token=cPWVX2SZKGOdRM8O9EPFNsdG1VmerqR7SFzKEbVFF2iD8ur46y9J_XUMI3ucFEbZGWET4eAZcKcpCMh3AOsFESWbB8c9ZTgvmuskN2yo8rvYi7G0-zHk3Vx22a4aGDof25dplBUhlqemqGryJ8nhFe5OFhooWYNNJfgpGPbqC85Px1-WAMBRq89VT6S2SAllNiGWDZgzg2CrxJYGxA2sfAUBxJ23kHtyogLTXeI7_SIa8UGWwowFum4QHPMpiiF_iRfb6c8_AGkSam05v1wRtggPIepVjRkE5a6XLPHTSwWU4tCZW8BeisJM7zpkJ2w60dfpIeEmTRQDbrMiMKEFkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در زبان انگلیسی کجا باید از the استفاده کنیم؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/690402" target="_blank">📅 18:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
یارانه شهریورماه دهک‌های اول تا سوم واریز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/690401" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18cfd2ee59.mp4?token=rHZ43Vzpnd4yTS1mE46tPrnVbmJmt5-G1ssYfU8frnKNMqXvXzFSuebmpX7XofpbB9UgsyhOsMJVLkI2K6LZo3sSoAkjbIPvlVm4WGftilLyDEZi_inir0iTDvdbyy3wf0MJAwc15F5rc_H9YqjVD0SHjvV2oecOw8V8eph8QfGk-YKIgojnO7v5hS6b0B0vi8RH97HirlQEV2nHVEONQijAluhzi8w3hnoaWIlFzqmrQzScIH56YURiOq9pPXvgfZx1LDYEriQejS1utt0s7H_mUit7L0VneKUhdL-8jwSKlC7VHxWrvhQjR-uqr4XNJf3h2Nhss4ceMiCO6KKbb7Mgi40sjGzkBqtXer2OVEFXKbvXAPqoMCua_6qmNG6ZWX2HGOTAaJO3aPHroAn1CUxXuZgiCFi3l0qSSSWsNA8BPWeJLbYKq31krIjnt4gukW6wNZ6QIfUS-N46byOqjQFWxVhE3djej0erzsvRdAaOlRTKdIQKBwpHaEtBMGytyhCtirMNxh0CSF9sqtnU_Bs2UlZnxxgUJY6-LTS4FyYAeGFlPrdcunbmViO66nS3I83lGPrHWPsfSX06PS2AkqVFqwX-hcIFvbcXlchZB5R4OrEnKZj3osR_5bTBzanDPrQkUGx4LJABF52UC4IJs0lOhTUIG9jRGqJQAf27XWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18cfd2ee59.mp4?token=rHZ43Vzpnd4yTS1mE46tPrnVbmJmt5-G1ssYfU8frnKNMqXvXzFSuebmpX7XofpbB9UgsyhOsMJVLkI2K6LZo3sSoAkjbIPvlVm4WGftilLyDEZi_inir0iTDvdbyy3wf0MJAwc15F5rc_H9YqjVD0SHjvV2oecOw8V8eph8QfGk-YKIgojnO7v5hS6b0B0vi8RH97HirlQEV2nHVEONQijAluhzi8w3hnoaWIlFzqmrQzScIH56YURiOq9pPXvgfZx1LDYEriQejS1utt0s7H_mUit7L0VneKUhdL-8jwSKlC7VHxWrvhQjR-uqr4XNJf3h2Nhss4ceMiCO6KKbb7Mgi40sjGzkBqtXer2OVEFXKbvXAPqoMCua_6qmNG6ZWX2HGOTAaJO3aPHroAn1CUxXuZgiCFi3l0qSSSWsNA8BPWeJLbYKq31krIjnt4gukW6wNZ6QIfUS-N46byOqjQFWxVhE3djej0erzsvRdAaOlRTKdIQKBwpHaEtBMGytyhCtirMNxh0CSF9sqtnU_Bs2UlZnxxgUJY6-LTS4FyYAeGFlPrdcunbmViO66nS3I83lGPrHWPsfSX06PS2AkqVFqwX-hcIFvbcXlchZB5R4OrEnKZj3osR_5bTBzanDPrQkUGx4LJABF52UC4IJs0lOhTUIG9jRGqJQAf27XWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهت آشنایی و کسب اطلاعات کامل از حساب معاملاتی شیلد zorafx وارد کانال زیر شوید.
https://t.me/zorafx_broker</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/690400" target="_blank">📅 18:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc89fd892.mp4?token=IqnMHqrUCQGYZFgzYT1QVlDE0jqK92dHWvdCJFkJglyROW7jJvj0nHJCuU6MSvDalCZ-XJL0qg1N4EhFzzrTNT6affo6Xlg2nPl_QCewiU1ktJGWxU0mqWrkUJdgDfmeBHzmWCklWI1usm1RLyKpahKRBW89R1exiQVbgPvCPQ-gaGPVvQYZc3_eEZC2lBVvujrIHHTLMdzwPiWndylSwcEq4c3z4CuPrgbYn1vSxmsV3d2CIV2P-Kmlu_EbH7VdmPMbR5ciwcYXMHsCzOdOOW05PRIKXtS7zejp_s9MUnM5nLgzTfs0w4CTTCKm9Bg5HE6Mm9xVMIHBeuprEqedUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc89fd892.mp4?token=IqnMHqrUCQGYZFgzYT1QVlDE0jqK92dHWvdCJFkJglyROW7jJvj0nHJCuU6MSvDalCZ-XJL0qg1N4EhFzzrTNT6affo6Xlg2nPl_QCewiU1ktJGWxU0mqWrkUJdgDfmeBHzmWCklWI1usm1RLyKpahKRBW89R1exiQVbgPvCPQ-gaGPVvQYZc3_eEZC2lBVvujrIHHTLMdzwPiWndylSwcEq4c3z4CuPrgbYn1vSxmsV3d2CIV2P-Kmlu_EbH7VdmPMbR5ciwcYXMHsCzOdOOW05PRIKXtS7zejp_s9MUnM5nLgzTfs0w4CTTCKm9Bg5HE6Mm9xVMIHBeuprEqedUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: آیا شما به اندازه‌ای شجاع هستید که یک جدول زمانی برای کاهش قیمت انرژی ارائه دهید؟
🔹
وزیر انرژی آمریکا: من قطعاً نمی‌توانم رفتار ایران را پیش‌بینی کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/690399" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار درباره کمبود تجهیزات پزشکی در هفته‌های آینده؛ ۳۰۰ همت اعتبار ریالی برای جبران این کمبود نیاز است
علیرضا چیذری، رئیس انجمن صنفی تولید، تأمین، توزیع و صادرکنندگان تجهیزات پزشکی و دارویی در
#گفتگو
با خبرفوری:
🔹
بیشترین کمبود تجهیزات پزشکی مربوط به اقلام مصرفی و قطعات یدکی از جمله برخی شنت‌های مغزی، سمعک، کتترهای خاص و محصولات وارداتی دیالیزی است.
🔹
اگر کمبودی در برخی اقلام احساس نمی‌شود به‌دلیل وجود ذخایر در ته انبارهاست اما با ادامه این روند، در ماه‌ها و حتی هفته‌های آینده احتمال بروز کمبودهای جدی وجود دارد.
🔹
برای جبران این وضعیت با ملاک قرار دادن قیمت‌های سال گذشته، حدود ۲۵۰ تا ۳۰۰ همت اعتبار ریالی نیاز است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/690397" target="_blank">📅 18:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690393">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8nZGcynN513N9AkZub3xO_s0dlKQxmjpsU4dtLd-JPlRcgJc8rUpNFxqmPlqxTwuqiwbFe0kzT_tRQvwa1cu_InJCTgqlNnetETO2EHN-HbvBMEEdWHjq9M64tffhQG7sVl7oHJPi0b1fasHn4aF3BGzu6T22kTGdqdJUXmnXR0EoXl8cjTwteoMjwEdTPnE3Y333C_2dudLMnXUYGsF9iiJRAThIzr21ZF37iKLK_fXRma_p3OONyCA-ZR6qTuVCuV1QXjxNgXE4q_T3qGDumYsqYuUfD6UJj4ZcFPpiubJMqXTXmkDY5J_b6x-P7QoI-mL7zxaLDXcO0v5f3kpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFiH5NY5l9Z9ZuVl7iEUp8Rh7tlImyd5VXPNgmzGLyW0FNC5BnSm7uqGppp5lazDS9nLdZTUH_GJEDTFTaLVx2xGT_18zcNacbYQ4dbQJyCL0hIPkNZHafSpU4nlKns9T96wXa7HPYGkOc6rnjmq95Mm9Gcwltk5unpjTV0Z1pcYDGhh-RBkzrJkhoeMwRU_bKQpTHLhS6talo5AtD0VLC07IPdhyRXeM8oQehhbPY1jFquoUkvZcoySOSm3bILXEgIVrxyQ1ZvRXZMPCJPYVFRFYKUylzftdyNxgYuyK7p2YQqURwSIV3AtCeXkQwKMayhzIj0JPW00WRJzh62Wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul4Jd6e1Pj5zXfGM3oeI87Fh09YyQAwO7mgOQcHdlZ2ta6Rbsht0gVVDMbrGQLXtUCb5Vk7ufm97znexnA5ri_DKD_EqI6NKMVBXLVU_mSl4IyNSo5-1OpRhamFIJf8A75Ky32iGiqV-mk5GPf4n1X-ECpKbTU4Cmrausq75b_MIjK_za-7tjE4Q8wGf4zrEncMDk58TbdxQ8gNtwKOtYRhUefNWLKhXwqrYI4jLlBBTHynOMefdwDGfmzVigzMpidFf0onkSCJx8hSzQyj2B0cL9yRcMqkBPItKKlD6VFUzu62gpYdi192oVtlReWlUWEcSFRzHEkKMJmJEFU3JcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Es6KxV_JlMMvE_TrdjMz_qz4DJkYz8S0-vpvxW6QxO9Qo0YwF7ODVyHvJANBIgi48Axdz1nCRHmme2hbIoczNwhArP_UHjP9wF4u27M9Axgx3W96B8y1uOXEvj2FlG9yTKl80K7GWZcZz7RPXbRXRbUpK3-CGiJve8jOwTJeNWQWYD0J47-a9_8lq3iPcXV_LMQhFxFAA_XIwKiEU4hrMw3CXfNpxpoHHi3b6F2bj9DCnN7xxwVh9m-jJcewZ8VvTpq37DFRH0XRMkA_lCfKMlPDONBmOIKoDU2cTSx3i0z4ARisBBQOcpHG3f7vHKq7KJrUnKgKuT03qKSNc39PXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری کامل از لحظه رهگیری و سقوط جنگنده عربستانی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/690393" target="_blank">📅 17:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690392">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تصاویری از لحظه سرنگونی یک جنگنده F-۱۵ سعودی توسط انصارالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/690392" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVh1MOCr2DZsH0tD4VWvToLDHVjjOQI2BmroTytAO_IYYkCRKsgYIuihJr6wP7hS5vt60_WeNnoCs9c7FNb2-AnJANFUrVW55OcEQyKON9qJnQjTomUPDkj9uWH3Xp9vRKKbjzopQ8L4mkMgKN2O9wVy9XKqfcBjDXj7z39Jz4bMGUva-Dob_mHEEYQLXXKUQtNQnU44aFe4ronbBduEjNPYixJI-REEX2fdwL_AG5cjpNamWPLUgcJgjAEMCF-jMnWhb0VgHO7BjW_TEic6TXOtyNPE6UQYYNUJqN9ROj2xJFhXEJohGMans3MOHc0sm4Lfi951VLME6ufdpM5Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین بازدهی یک‌ساله صندوق‌های سهامی
🔹
بررسی بازدهی یک‌ساله صندوق‌های سهامی نشان می‌دهد صندوق سهامدار با ثبت بازدهی ۲۳۱.۵۴ درصدی در صدر این فهرست قرار گرفته است.
🔹
پس از آن، صندوق رشدی کیان با ۲۰۹.۷۱ درصد، صندوق مانا با ۱۹۹.۴۷ درصد، صندوق ثنا با ۱۹۶.۲۰ درصد و صندوق زرین با ۱۹۱.۴۴ درصد قرار دارند./ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/690390" target="_blank">📅 17:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690389">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی تعلیق کرد
🔹
بر اساس بخشنامه‌های ابلاغ‌شده، مسیر تهران-مسقط از ۲۶ شهریور و مسیرهای تهران-استانبول و تهران-آنکارا از ۳۰ شهریور لغو می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/690389" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690388">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRf9i_-bGMJ7o72Wd92jDTsjmENKoNmmuZ5fJsWd0WEbU5PiNis3ldXCWDu96G97DOfYDwpvoM2DUuNeIgXB9xifL8-oyE50IADA6rT6u0dZJQO7WMTHZ8stuv4wgcJIDVdGbm-gk82LFJcUw62a2U3Iu5dpDVCMXMTkeX7RedJtbARC234vo7TiFKW4kDufQWyf4R1XiVyJ9CeTPnQ_-thjZiaFfrGu-T11w7mQCZcZcDr3BHGX0VQZctJGCaHRyZ_kFNLp4FBKTQj0LHmD3O82wHVFByGL2z8sQwRUzSnWro9jTN6e-6iFNXwiNDSVYUp7POJ2bUxTgHZ87m5HSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انواع کشتی‌ها و محموله‌های آن‌ها
🔹
در صنعت کشتیرانی، کشتی‌ها متناسب با نوع بار طراحی می‌شوند؛ بر همین اساس، کشتی‌های تانکر برای جابه‌جایی نفت، فرآورده‌های نفتی، گاز مایع و مواد شیمیایی به کار می‌روند.
🔹
کشتی‌های کانتینری و عمومی کالاهای مصرفی، صنعتی و دسته‌بندی‌شده را حمل می‌کنند، در حالی که کشتی‌های فله‌بر ویژه جابه‌جایی غلات و زغال‌سنگ هستند.
🔹
کشتی‌های رو-رو نیز برای حمل وسایل نقلیه و تجهیزات سنگین مانند خودرو، اتوبوس و تریلی استفاده می‌شوند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/690388" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690387">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhlRWpqLRZeiut9alSZs62Nwnwe3zmV-Jp8fnre2CZaKb1txkYnJIAt0v1ldP9BWDxm94FCHDbXE-y93AHn7aLNr6OEE3hRQiB3Xiu6mRWIIK6Mvvqvi4iVZASe8uE_oKHwNwy8lmNIr-DJMKqd9VvWDj4rBOkMRbRiWpBJWPe1ZaF30Ca8ja5jc5HINXzqN0Uhh_CzB9MbhGIBtqABeEN9LrPdHwafJnAz3KpC1ukeYbatwPkNXlin-rkFtiBy6pBXZgsv4a-hk19lStlEAV4-lmLXUrZCKJ1zbDY4udPCHnZvl961eOPZECKFlfAZmWVk-gZASoIx7rKo5v7WOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدر اعظم آلمان نمی‌تواند از جنگ و جنایت حمایت کند و همزمان خود را قهرمان صلح و معلم اخلاق معرفی کند
اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
«صدراعظم آلمان از «جنگ» ایران، «برنامه هسته‌ای نظامی» آن و «نیابتی‌های» ایران سخن می‌گوید.
🔹
این، یک روایت کاملا تحریف‌شده است. این آمریکا و رژیم صهیونیستی بود، نه ایران، که جنگ تجاوزکارانه را آغاز کرد. آلمان حتی از حداقل شجاعت اخلاقی لازم برای محکوم کردن این عمل تجاوز هم برخوردار نبود.
🔹
آلمان نمی‌تواند آشکارا از کار کثیف» پشتیبانی کند و سپس خود را قهرمان صلح و معلم اخلاق جا بزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/690387" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690386">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
وزارت خارجه سوئد در راستای اعلام حمایت خود از اسرائیل، یکی از کارمندان سفارت ایران در استکهلم را اخراج کرده و سفیر ایران را نیز به وزارت خارجه احضار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/690386" target="_blank">📅 17:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690385">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سیستان‌وبلوچستان در صدر هزینه بنزین؛ قزوین در انتهای جدول
🔹
بررسی میانگین مخارج سالانه بنزین در استان‌های کشور، اختلاف قابل‌توجهی میان الگوی مصرف و هزینه‌کرد خانوارها نشان می‌دهد.
🔹
بر اساس گزارش سازمان برنامه و بودجه، سیستان‌وبلوچستان، بوشهر و هرمزگان بالاترین میانگین مخارج سالانه بنزین را به خود اختصاص داده‌اند؛ در مقابل، قزوین، قم و کرمانشاه در پایین‌ترین سطوح این رتبه‌بندی قرار گرفته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/690385" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690384">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f889f99f36.mp4?token=QyPxn-ki6jcBbchySIXBc5wcCVTXcU-NDMvxA6XRTMeRUB4zIQLqyCQDGpH_1EHrwDHOQlGg9Sg0RGxEG5niW06XT_4TdENn-FFmIQJha-ZyvsyRwlSh-a3J9OCnMBzefS9FS7Lo3KUK7bXSk4Ra7YOxf4WErSc48XlV6268Gs31rzm1o9oN2nNWwz0rbiCWfod8bdzmTysjFSdDQw3u8ap2kLjUA4tJmwQxJjiSOGyZ61g2I-lsoNxnnniPihJsK7iyI2iwtCecuiBZh5sPKKdNFdTLuNlHAS4ZeO7lrpQGvox1Kb6Vyl3Zf8Vou-hNvH_gsVip_Tsph7NGJJVdVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f889f99f36.mp4?token=QyPxn-ki6jcBbchySIXBc5wcCVTXcU-NDMvxA6XRTMeRUB4zIQLqyCQDGpH_1EHrwDHOQlGg9Sg0RGxEG5niW06XT_4TdENn-FFmIQJha-ZyvsyRwlSh-a3J9OCnMBzefS9FS7Lo3KUK7bXSk4Ra7YOxf4WErSc48XlV6268Gs31rzm1o9oN2nNWwz0rbiCWfod8bdzmTysjFSdDQw3u8ap2kLjUA4tJmwQxJjiSOGyZ61g2I-lsoNxnnniPihJsK7iyI2iwtCecuiBZh5sPKKdNFdTLuNlHAS4ZeO7lrpQGvox1Kb6Vyl3Zf8Vou-hNvH_gsVip_Tsph7NGJJVdVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر درد کمر، علت یکسانی نداره؛ محل درد می‌تونه سرنخ مهمی درباره عامل ایجادکننده اون باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/690384" target="_blank">📅 17:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690383">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfd7aae45f.mp4?token=vTV6gJgsNfCZE3gSyJCh1U4fJoPeqU15ZC6GiTVdIV-gXEJSLGpNkrAuIg_RYzCuvPqOXvaqG4kt3UilHN4IBcjVkiXOr8Yv_ERPxew7-jIas-GQWdP2dckoljRgYHuvtrBWHWjOPly30P4cQRL5J4dM9HMTPeKK_opm0kg8oZs40yQkbKhbpCjVx1fGDCltAGYMvHlEJ-3Nsow1jjb8uuiYiQGjhbk_Sb3BOG3_75dXyrWxguQFBWlSrHFq6C00EbxRTg4s1LuEEW85lkvR4v7HZnRzcUvVe_I1o_AmPl0okhD708EFe5Xb9fzkAMk7GsGaICOwP6W-kVWdZ0c4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfd7aae45f.mp4?token=vTV6gJgsNfCZE3gSyJCh1U4fJoPeqU15ZC6GiTVdIV-gXEJSLGpNkrAuIg_RYzCuvPqOXvaqG4kt3UilHN4IBcjVkiXOr8Yv_ERPxew7-jIas-GQWdP2dckoljRgYHuvtrBWHWjOPly30P4cQRL5J4dM9HMTPeKK_opm0kg8oZs40yQkbKhbpCjVx1fGDCltAGYMvHlEJ-3Nsow1jjb8uuiYiQGjhbk_Sb3BOG3_75dXyrWxguQFBWlSrHFq6C00EbxRTg4s1LuEEW85lkvR4v7HZnRzcUvVe_I1o_AmPl0okhD708EFe5Xb9fzkAMk7GsGaICOwP6W-kVWdZ0c4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه انصارالله یمن: اخبار منتشر شده در خصوص حمله به جده و مکه را قویا تکذیب می‌کنیم/ هیچ ارتباطی بین انصارالله و انفجارهایی ادعایی در جده و مکه وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/690383" target="_blank">📅 17:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNobitex | نوبیتکس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vitrq0d7joF0IIaFah6du_LASE0aOsAWTiQ9MZ7s38aYUUHc9mvr17dhcHoGFKFcJi43U64FZtDMt_bFFFdTE8dgYVQ8eqwmtuFHYNC_yFFBo2UtNVaT00iCeCuySHgUd0sBig_vLMAAxBdYUmlmfk_i6wh14D7sl0no00Qe4QGzbvDSolaT95rGLIXwRwaGfPIYMiXfqxw2uhvUsxPWLqm5cLr6AJXNeH-j3quokiGg3_ZdKW1jva5kkCyyQbcvmDfDAHogX2mahRUrhUquH2oTCiiyDOy3qb6EXSokYa1X0g2k-dXVX_W3yp9wUqT8A1yoQqzfYt-XoO3JSYqTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
مهم‌ترین سیگنال بازارهای مالی؛ چهارشنبه‌شب
این روزها تاثیر اخبار اقتصادی کاملا مشخص است. مثلا خبر افزایش بازخرید اوراق کافی بود تا طلا در یک روز بیشتر از ۳٪ رشد کند و بیت ‌کوین هم تا ۸۰٬۰۰۰ دلار افزایش یابد.
داده‌های بازار کار امیدها به کاهش نرخ بهره را تقویت کرد، اما عواملی مثل رشد دوباره تورم و سخنرانی کوین وارش در جکسون هول،
احتمال افزایش نرخ بهره را در پایان تابستان ۲۰۲۶ به ۹۰٪ رساند!
حالا سؤال این است؛ بازارهایی که اول ۲۰۲۶ منتظر کاهش نرخ بهره بودند، با افزایش آن چه می‌کنند؟
نوبیتکس یک سال است که رویدادهای فدرال رزرو را همراه با کارشناسان و فعالان بازارهای مالی در قالب برنامه «Federal Effect» پوشش می‌دهد.
موضوعات مورد بررسی در «فدرال افکت» نوبیتکس:
🔴
پوشش زنده اعلام نرخ بهره و سخنرانی رئیس فد
📄
بررسی تغییرات بیانیه و مسیر آینده نرخ بهره
📊
تحلیل اثر تصمیم فد بر دلار، طلا، بیت‌کوین، سهام و بازار ایران
🗓️
چهارشنبه ۲۵ شهریور، ساعت ۲۱
:۰۰
🔗
این ایونت را می‌توانید به‌صورت زنده از
مجله نوبیتکس
و شبکه‌های اجتماعی نوبیتکس تماشا کنید:
📹
یوتیوب فدرال افکت
💖
آپارات نوبیتکس
⭐
تلگرام نوبیتکس
🌐
اینستاگرام نوبیتکس
💜
@NobitexMarket</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/690381" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
بلومبرگ:  عربستان پس از تعطیلی خط لوله نفت خود، فروش فوری و نقدی نفت خام خارج از تنگه هرمز را افزایش داده
🔹
شرکت آرامکو این هفته حدود ۲۰ میلیون بشکه نفت خام به پالایشگاه‌های آسیایی فروخته؛ خریداران می‌توانند این محموله‌ها را در خارج از تنگه هرمز تحویل بگیرند.…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/690380" target="_blank">📅 16:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
حمله ایران به کشتی آمریکایی در اوایل هفته جاری
ادعای فاکس‌نیوز:
🔹
اوایل هفته جاری، یک کشتی آمریکایی با ۴ پهپاد و دست‌کم یک موشک ایرانی هدف قرار گرفت و تعدادی از سرنشینان آن مجروح شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/690379" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
