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
<img src="https://cdn4.telesco.pe/file/IywVzZmRifxaktD1_TnuGi0ZQaRajNUgPaDOiLAtpMXvZmdJlw0xEurOFDerKRSdlq1rLmM6dlmJz9NpSY3Mq9r4JZ2txvQVfVT48jdVcV2QLfxm_C_zUAOFUfOX72rMXcNBfWOhhYcx-OkrkO4sfjiMIA4BdVrOK2JT5CdwrMfO5aa9QpIyn7d5MN9FO3rJd0wG6VwFKVaPP0Xuxxo7uwUrYuY_NnL_rw-_R5D9klMzCJYibIYztAdd2mSRO7TRFyYwi4uCOsr9WoW5soKwGjrr8iyzhEuCunk-yU-cbw_BXp5NV6ypAW8whXmKBdP_UGDlGF3AnkwQrxC_nM_J-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-678948">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: تجمع مزدوران سعودی را هدف قرار دادیم
🔹
در پی ادامه محاصره و تجاوز علیه ملت عزیز یمن از سوی دشمن جنایتکار سعودی که نزدیک به ۱۲ سال ادامه داشته است، نیروهای مسلح ما تحرکات و تجمعات گسترده نظامی عربستان را رصد کردند که در مراحل پایانی آماده‌سازی…</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/678948" target="_blank">📅 18:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678947">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350cc28638.mp4?token=hGVLPv5lda7AuplR4UEk5XsjY_PszAdNADPHeF65-4UDw7q_RqPSkCljHTXJcBMmlDB5uuEwLbd7fZcv53fhGOxGpuerjsEKzBXMo75zfo50eJMY-MiUpMXK7-8ceDU961xGo-G90MznVZ0QNXFipP2wvayUYZn1XqtyVyGgcdIPp1UvFmh84Cv-smtwNwli6Rgxh4-iaaUU3fZb0_zpznrPTFup7GYLAEFQ2Al9KaLn5pTDXLxb8AOpyEydify4r2j2-x3SGsOf9OVkr5yhCsre14nHNGjPU1LZHgzmkbisaez2Mb532YKPI5njyoSxhGF6AAafUbmhm9j68dKxsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350cc28638.mp4?token=hGVLPv5lda7AuplR4UEk5XsjY_PszAdNADPHeF65-4UDw7q_RqPSkCljHTXJcBMmlDB5uuEwLbd7fZcv53fhGOxGpuerjsEKzBXMo75zfo50eJMY-MiUpMXK7-8ceDU961xGo-G90MznVZ0QNXFipP2wvayUYZn1XqtyVyGgcdIPp1UvFmh84Cv-smtwNwli6Rgxh4-iaaUU3fZb0_zpznrPTFup7GYLAEFQ2Al9KaLn5pTDXLxb8AOpyEydify4r2j2-x3SGsOf9OVkr5yhCsre14nHNGjPU1LZHgzmkbisaez2Mb532YKPI5njyoSxhGF6AAafUbmhm9j68dKxsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در میان رنگ‌های یک پرچم و زمزمه‌های یک شعر،صدای یک عشق شنیده می‌شود؛ عشق به خاکی که نامش وطن است…ایرانِ همیشه جاودان
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/678947" target="_blank">📅 18:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678946">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پایان مذاکرات لبنان و اسرائیل در رم
🔹
به گزارش الجزیره، آخرین دور مذاکرات بین لبنان و اسرائیل در ایتالیا به پایان رسید.
🔹
این مذاکرات که با میانجی‌گری آمریکا انجام شد، به مدت سه روز ادامه داشت، در حالی که رژیم صهیونیستی همچنان به تجاوز نظامی علیه لبنان ادامه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/678946" target="_blank">📅 18:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678945">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
یمن: نقشه عربستان برای حمله به صنعا را در نطفه خفه کردیم
🔹
محمد شوکه، عضو دفتر سیاسی جنبش انصارالله یمن، در اظهاراتی تأکید کرد که عملیات اخیر در جبهه‌های مأرب و الجوف، یک پاسخ تاکتیکی و پیش‌دستانه علیه نقشه‌های تهاجمی عربستان بوده است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/678945" target="_blank">📅 18:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678944">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQmViG73y1lrj8iCsHfQBZdVTOZPkaQe-Zhux2B49Vsk5R_4q6RAMVeo8mUHpUzOu1ApOKKNA5fmGe38YH43-thet4LtVE4mO_Sth6tRgK79ZTgVQVQrAsyjMjtayVYHT9xfu4kh7Os6Hon06L0u5nCT2kzZpN7btCqwPEkeExTkljyAFSOruR-fBFS5rGTJuLNq9aTxDPhTMjbLfC9DJRwUTZIzB4XBiuSxdUwUTFqIErIdHFw2-WJtcSQdMVTZplm4R5EpeNoD9lgVgw_RlAY-Q9ZHmeajIUucECTYUc3aLRS0x8evLIAgqOdVaTSmBcBWHKNXc6Z8lbVOQIy5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدودف: سکوت ژاپن درباره عامل بمباران هیروشیما و ناکازاکی مایه ننگ است
دیمیتری مدودف، معاون رئیس شورای امنیت روسیه:
🔹
چه ننگ‌آور است که ژاپن در مراسم یادبود بمباران اتمی هیروشیما و ناکازاکی، حتی یک‌بار هم از عامل این حملات نام نبرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/678944" target="_blank">📅 18:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678943">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c122c5a82a.mp4?token=bnKx9ek2aqXksZhcdZgMtHEkQ3dZeVjL07fCGfGGnNrFHpPSHBBlRWD6p0dwlQbD505HNNrbYesN-kz_CpYTqrDmF8LWihSg97hBgbAZmGT97G9eCilBCKF9JG7HI-w6ITCBJDZa9Xpd9b6OZX6PBLTlDcDpViCjYaQ9-d2dbTUWeFQhrVaRwQ3Trnmi11Bjp2A0W3tfXu-M5VVlfSgmAm1KEv7-e-NyX0tQyQYLNy1XhCf-s-H4_qbzL-lWujkDAx229wjIsZbV5AQWADnidKjRbo34PF6YGsfQVi75ZVs1sea1scBI8LyHKOTjBrJObeObRnmYHbNVJMMrgxTCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c122c5a82a.mp4?token=bnKx9ek2aqXksZhcdZgMtHEkQ3dZeVjL07fCGfGGnNrFHpPSHBBlRWD6p0dwlQbD505HNNrbYesN-kz_CpYTqrDmF8LWihSg97hBgbAZmGT97G9eCilBCKF9JG7HI-w6ITCBJDZa9Xpd9b6OZX6PBLTlDcDpViCjYaQ9-d2dbTUWeFQhrVaRwQ3Trnmi11Bjp2A0W3tfXu-M5VVlfSgmAm1KEv7-e-NyX0tQyQYLNy1XhCf-s-H4_qbzL-lWujkDAx229wjIsZbV5AQWADnidKjRbo34PF6YGsfQVi75ZVs1sea1scBI8LyHKOTjBrJObeObRnmYHbNVJMMrgxTCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشنواره ۱۰ سالگی "چرم مَنطِـ" ادامه دارد...
همراه با شارژ «کالکشن جدید»
✨
تا %𝟴𝟬 تخفیف پلکانی
✨
➕
2,000,000 تومان تخفیف اسنپ‌پی
حضوری و اینترنتی
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/678943" target="_blank">📅 18:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678942">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نشریه اکونومیست: باید قبول کنیم که پرداخت عوارض به ایران بهتر از ادامه تنش است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/678942" target="_blank">📅 17:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678941">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تکمیلی| حمله کوبنده نیروهای مسلح یمن به مواضع مزدوران سعودی
🔹
در حملات موشکی کوبنده نیروهای مسلح یمن به مواضع مزدوران سعودی در دو استان مأرب و حضرموت دست‌کم ۴۵ نفر کشته و ده‌ها تن زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/678941" target="_blank">📅 17:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678940">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رویترز: در حمله نیروهای مسلح یمن به مواضع نیروهای وابسته به عربستان در حضرموت و مأرب، دست‌کم ۳۰ نفر کشته شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/678940" target="_blank">📅 17:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678939">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE1gRHhZlGnlzS2ZBZvNG1v2KgzYXo8U86tJEUrnwK3GWV4VR2xc2jshFTZVCyy804TWQnbqvB5NdLfMUe8uPjiSzOK3T8DeYaSNo2Tj6h9A2i5vFdA3XTU7fCHnkU_jVLfcXUjzmI4s9w9r9ksWHfvHOjyStuNVaOmHvgZMxNoBZSBz4N_7fXXnl5aD17wmBIjjPkDGPuyEuucZ2OFtA8gE__w0i0Q4ac2xKIo95hxKVofy7qNnjbcuuoSWIJLqCJOiie61W1GH7j1Ft5LebHzYhTxr8VLChmflT-LwvdqHdtfCwcXM6R05aaxFtv0mi1_xoMCr2Nn8EdzER5Vaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدهای دریافت رمز پویا بانک‌های ایران
/ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/678939" target="_blank">📅 17:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
چراغ سبز شورای صلح ترامپ به ساخت اولین پایگاه نظامی در غزه
🔹
نشریه گاردین امروز (پنجشنبه) به نقل از یک منبع آگاه گزارش داد شورای صلح تحت رهبری ایالات متحده، اولین مناقصه برای ساخت یک پایگاه نظامی ۱۵۰ نفره برای نیروهای مراکشی در نوار غزه را اعطا کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678937" target="_blank">📅 17:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678936">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81283038c3.mp4?token=l7LthRPlNgJkkmBkAycGUwHHJ9GGKGY_luF6k3705GJ9SQoDT1MvE_zjqFDZChCDoiXeH8FvLD5jYC8tvGoCttyAzni6YDlc6moG2rEL5z8E2SSAQqFeOijGud5NQKCjtizBUyQNBFXAwMDYTL0sANTUzJfEkqAmEi692VbWDNlr8wOtIy7eEP2MnV7XTCKNYfGNNesfqEcwLb_zOXOJqtdA_K8iMCXcmf3rG5hT35S_wiwjiifnnyhGX_Ksy79m78VMfeJCpn7C28iKw_N-NnA4lDcyIAmzurtWJjFX_XKBjadtscnaaUOFnfdwepLww4GBjW4DK_4w-FAN8gd5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81283038c3.mp4?token=l7LthRPlNgJkkmBkAycGUwHHJ9GGKGY_luF6k3705GJ9SQoDT1MvE_zjqFDZChCDoiXeH8FvLD5jYC8tvGoCttyAzni6YDlc6moG2rEL5z8E2SSAQqFeOijGud5NQKCjtizBUyQNBFXAwMDYTL0sANTUzJfEkqAmEi692VbWDNlr8wOtIy7eEP2MnV7XTCKNYfGNNesfqEcwLb_zOXOJqtdA_K8iMCXcmf3rG5hT35S_wiwjiifnnyhGX_Ksy79m78VMfeJCpn7C28iKw_N-NnA4lDcyIAmzurtWJjFX_XKBjadtscnaaUOFnfdwepLww4GBjW4DK_4w-FAN8gd5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خود فروخته‌ها چطور با موساد همکاری می‌کردند؟
🔹
این عناصر مزدور در عملیات سربازان گمنام امام زمان در وزارت اطلاعات شناسایی و بازداشت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/678936" target="_blank">📅 17:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9758b875b.mp4?token=iWpNsB8hI0aDckeklLYlbh8QOCqEN8pMT8lwEgscdbLhbHwelnEsWYiA64zmooAEAjDItOSHZHVauBXybooZihioqc024ydZc8HWDQvk_OjW2458E_elvyx2jG5-VTNTOMU3k173zq070d8Rs7VOsQhcXx3gqVsksUxUKI74cXriv0q7kmBzoymQ_jh9xPsCm35tc5SwVwBYk0geapcm88YeUQIX52tnbkuSuDH5pWPKvgKSK1JBl4AywFIR206c6cybGPGmXy57o7EqwbTCne_AioMsmHjbo9-qJc8mtO63SSzfIDkmItGzdjjlHiS0LOEG2SaCKUv53E4V7oAeiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9758b875b.mp4?token=iWpNsB8hI0aDckeklLYlbh8QOCqEN8pMT8lwEgscdbLhbHwelnEsWYiA64zmooAEAjDItOSHZHVauBXybooZihioqc024ydZc8HWDQvk_OjW2458E_elvyx2jG5-VTNTOMU3k173zq070d8Rs7VOsQhcXx3gqVsksUxUKI74cXriv0q7kmBzoymQ_jh9xPsCm35tc5SwVwBYk0geapcm88YeUQIX52tnbkuSuDH5pWPKvgKSK1JBl4AywFIR206c6cybGPGmXy57o7EqwbTCne_AioMsmHjbo9-qJc8mtO63SSzfIDkmItGzdjjlHiS0LOEG2SaCKUv53E4V7oAeiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس کارشناس کویتی از تسلط ایران بر تنگۀ هرمز
فیصل ابو صلیب:
🔹
شاه که رابطۀ خوبی با آمریکا داشت و ژاندارم منطقه نامیده می‌شد چنین اختیاراتی در هرمز نداشت اما ایران اکنون می‌تواند کلیددار امنیتی تنگه نام بگیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678935" target="_blank">📅 17:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ونس: ایرانی‌ها در مذاکرات بسیار سرسخت هستند
معاون ترامپ با اشاره به روند مذاکرات با ایران:
🔹
مذاکره با ایران مانند قدم به جلو و عقب است؛ ایرانی‌ها بسیار سرسخت هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678934" target="_blank">📅 17:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
افزایش قیمت طلا با امید به بازگشایی تنگه هرمز
🔹
قیمت طلا برای چهارمین روز متوالی افزایش یافت و به بالاترین سطح ۷ هفته اخیر رسید؛ کاهش ارزش دلار و امید به بازگشایی تنگه هرمز از عوامل این رشد عنوان شده‌اند. هر اونس طلای نقدی با ۰.۲ درصد افزایش، ۴۲۵۴.۹۸ دلار معامله شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/678933" target="_blank">📅 17:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea84347b7.mp4?token=DXMFalJNPoSmeWrv_SHQMYWlhJGQXI-eIJwWoAkvmcmjCvhh-wEdLEe9jJBgbm_bcKYvOQd-cyi2nFHPW-rOstYBDn3VXEkokAQCt0dH_7fi43mLkh0MoAlKfgzV9NfSJ-fMdqnkfvphdgZieQ2vKjUBIAqVkOOgL7XqKnTv1yTSPVrmfY9fRsmpAG45js667oof6ZFrxaFhKtrMyImMc9ark-j81CgZKzDkW39JDZUNl2sQPrsgz1NW64mTRsSpQgHrTpnOD5xbJ7cB-4tBzMGr-imwITJE9e7HuI46GCZ12ev_I5ZOGWbiugg4OxaHaByTFKBl_iZF1L5vOw0YfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea84347b7.mp4?token=DXMFalJNPoSmeWrv_SHQMYWlhJGQXI-eIJwWoAkvmcmjCvhh-wEdLEe9jJBgbm_bcKYvOQd-cyi2nFHPW-rOstYBDn3VXEkokAQCt0dH_7fi43mLkh0MoAlKfgzV9NfSJ-fMdqnkfvphdgZieQ2vKjUBIAqVkOOgL7XqKnTv1yTSPVrmfY9fRsmpAG45js667oof6ZFrxaFhKtrMyImMc9ark-j81CgZKzDkW39JDZUNl2sQPrsgz1NW64mTRsSpQgHrTpnOD5xbJ7cB-4tBzMGr-imwITJE9e7HuI46GCZ12ev_I5ZOGWbiugg4OxaHaByTFKBl_iZF1L5vOw0YfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم میلیونی ملخ‌ها آسمان یک از شهرهای روسیه را تیره کرد
🦗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/678932" target="_blank">📅 16:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678931">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRLr7gF49Of1D1G4-Ibkhx3dr7JfApHHDgqwWarG-20REU8S0_EEEg-cMfG4-pspGTo-jLEoP8bly0tubnZdGp4NbPHcR2LiRodlN7_poyGVTbzykWtnJ6bElu19gEdy53xOsVTcr5SJk7jjlFJPdIZSqferpmJWPUdthUt0s8jK2z8sFpFzrf4kLuKXOvCHVGQtpZ3y11c6a2MV8ndDfzPH3c5z0K3Neb36veXVeje7UnjYfVaOuPJYknC3jxaIFJpFJndFdJ9_5tgw9IyhPh_M1pZDnoE6vBtarS62yCCqYbY77KoS7-XPBqOnYrnsq3umI1FzJGfQcDgCZXkD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم برق هسته‌ای در کدام کشورها بیشتر است؟
🔸
بررسی آمارهای جهانی نشان می‌دهد فرانسه با اختصاص حدود ۶۷ درصد از سبد تولید برق خود به انرژی هسته‌ای، بیشترین سهم و بهره‌برداری را از این انرژی در جهان دارد.
🔸
پس از فرانسه، فنلاند با ۳۹ درصد و کره جنوبی با ۳۱ درصد در رتبه‌های بعدی قرار دارند.
🔸
از نظر حجم کل تولید نیز آمریکا با ۷۸۲ و چین با ۴۱۸ میلیارد کیلووات‌ساعت، بزرگ‌ترین تولیدکنندگان برق هسته‌ای در دنیا هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/678931" target="_blank">📅 16:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678930">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt6U0j_PColsrjlwiqbvR6-jLsMxk7m5GzIVBCX8r4kNLERIaKiraRK1JWEhogT2HPgOrT41fqi3b_mZwnRCd3bW_ZYz8sXE2rrygZ77IHXOjD9PLHsk1HJQr2CxMC9LDGIYnny4YuXnbg3resgY6nRVvOjpq45JYaFUxG_pRWgT429VlERd4OL-6VrkakIdSX3VFQ73HURVJCX2fVBhjjZxdAi8T6QGAAOsBLp6FoLxHMnxZt1TudhWT3VGWEH9SD3uK8cUdoU4KUnK--dD6nZ3CU5r2uaqYhOqwSQVdx6noiQLZ6jcLg3inwa4DFZ8QNp_v0HdiprvgpsgjkM7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی دختر ایرانی در دوومیدانی بلاروس
🔹
زهرا زارعی با درخشش در مسابقات بین‌المللی بلاروس، ضمن کسب عنوان قهرمانی رکورد ملی ایران را نیز ارتقا داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678930" target="_blank">📅 16:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678929">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e068c7790.mp4?token=OJHAe5DMQ5xki77U1fyZtk_-aNkCLQDNtL3KOZ_SBKg9GjzosM0axWy3tUE8tk5P_B7H4IVtChGQhqBsk4oLNjcZKF-wvGs3gdGOKnU9MaBxS0qBwbqgdrr2xAnsD3M9OBTnEuh35-nXM99uZANaYP9wHrYxXiFkj6lBYaudCd4GT5yK7Pbm9ahwK0JUMAPcGkIq-xtC4MM7j78QD2WZ8xfQ-hGE7_hruiXjIadiW9nri6YqQohVVh5Eud3TwekgSQ652BSWxUbD-N--X2yP8rftPPk14ImmTdJY7FtXtF4cNuGBATBsG-aguFoBtmn4bNTd13M8TN1LGVbMpiYSTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e068c7790.mp4?token=OJHAe5DMQ5xki77U1fyZtk_-aNkCLQDNtL3KOZ_SBKg9GjzosM0axWy3tUE8tk5P_B7H4IVtChGQhqBsk4oLNjcZKF-wvGs3gdGOKnU9MaBxS0qBwbqgdrr2xAnsD3M9OBTnEuh35-nXM99uZANaYP9wHrYxXiFkj6lBYaudCd4GT5yK7Pbm9ahwK0JUMAPcGkIq-xtC4MM7j78QD2WZ8xfQ-hGE7_hruiXjIadiW9nri6YqQohVVh5Eud3TwekgSQ652BSWxUbD-N--X2yP8rftPPk14ImmTdJY7FtXtF4cNuGBATBsG-aguFoBtmn4bNTd13M8TN1LGVbMpiYSTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز: در حمله نیروهای مسلح یمن به مواضع نیروهای وابسته به عربستان در حضرموت و مأرب، دست‌کم ۳۰ نفر کشته شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/678929" target="_blank">📅 16:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678928">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c555dffe.mp4?token=DLVg6rdCYtr34lyI2GOMvqRyJE3ACnxHdcbsGa3Fyua6KGR9und2jFG5WS4kn-KW_0katLmAae3P8u2Se8oIA_NnKutj38QihXtXu2-GYcSLm5y_Bu7KeKbESEeMIsvP0RLTXy6qa7BCu_rhA2YFUfH7dKRlbUEAXCU8RQCM8ku2OwXlfOV8izbfHzvdxmdvZXxvax1NUirqnsv4b4KWRQOY2hYLsCaYL36vh4lTUbRXP3UXKjq9X-xzpsBFwHCCDUjRHnvs05a4IxODKq3kewjRFWp7r2AnBoYzfTJtRaOcRKPY65HvOFeEGU5GNBATiHDo8BcczgphIFFqalbyEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c555dffe.mp4?token=DLVg6rdCYtr34lyI2GOMvqRyJE3ACnxHdcbsGa3Fyua6KGR9und2jFG5WS4kn-KW_0katLmAae3P8u2Se8oIA_NnKutj38QihXtXu2-GYcSLm5y_Bu7KeKbESEeMIsvP0RLTXy6qa7BCu_rhA2YFUfH7dKRlbUEAXCU8RQCM8ku2OwXlfOV8izbfHzvdxmdvZXxvax1NUirqnsv4b4KWRQOY2hYLsCaYL36vh4lTUbRXP3UXKjq9X-xzpsBFwHCCDUjRHnvs05a4IxODKq3kewjRFWp7r2AnBoYzfTJtRaOcRKPY65HvOFeEGU5GNBATiHDo8BcczgphIFFqalbyEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی حاج قاسم سلیمانی به بهانه مأموریت، حاج رمضان را به پیاده‌روی اربعین فرستاد
🔹
خاطره شنیدنی سردار شهید سعید ایزدی(حاج رمضان) از شهید حاج قاسم سلیمانی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/678928" target="_blank">📅 16:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMZLkVRe021v9tBzPJkIqLx1XO9vHQDZKcBwmOOnD7eGaqssUUpYLnRUFkBLG2qXD-PnZDcyi4sW3oY4DE3i09FoLiQIdXSZJNH4BGk6mjJ_lnf-EtSQ_Wl0A0eNwCgx1adiocMl9S6iTm0LRTrIqIkEkqVSZTYeBmxE3edcgau-HlLdhfK2gzK_nx_WCm6PM7-gx5QANx52V67PCDsd9a3JHc_T1alXS80VpAoPvToxERiWusl3Ne8fifTmsrxoo5b9Q91FIUJ0PSGlLruxKf0tws0IPODZG9aEvBPWoWeQ9KykRmZjVh5H3QQ0HVK_kicFx_ZAkc31Q9tUdRKTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سحر دولتشاهی عذرخواهی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/678926" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
منابع یمنی: تا دقایقی دیگر، نیروهای مسلح یمن با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/678925" target="_blank">📅 16:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678924">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای الحدث به نقل از منابع آگاه: بیانیه‌ای مشترک از سوی عمان و ایران به‌زودی منتشر خواهد شد که از ایجاد یک گذرگاه موقت در تنگه هرمز خبر می‌دهد
🔹
این گذرگاه تا زمان نهایی شدن ترتیبات مربوط به عبور دائمی مورد استفاده قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/678924" target="_blank">📅 16:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsygbxwuXyY1pM1XYU0a73uAndY6ssbSWi_n4gqovhH7yKFrsKESttKnqvTPhNRk9mkXeVZNALolPT2DuMiEj0F0Ta-gkhW3pxhV_fkhsnEY4cWqxsgy72dczYd3nSuLY8oZaWgiHJ4SHdsiiFDXTG3CHt5Q2HsvAXWm3GntxxfP2C8sctXSsS0YBOR277vJRogPrDgQOKBrKZjABBsT9GXIetTZ8csTaA6tSGmKFpGybqYXKHTjGNcLh215-9TF6v9cUZMCvz8l0zWDYk0AXj5XGVCtwGG-cXLSo8-CWc1_2V6p-TOYtOBUJsFkVIbeG2h_7xDNOBbuX52ia0MYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3f6z7vVNOzjVwZCFkAiCk_Y97sdS63Kc96YTQlbfaDr3jHr_EKr1LPYaaaojalPYC0Le08h-nX7TpxxsGzDJpDuq_lQJKRLbh74b8BJt4c-v5Nv4c3CJxz0VwZKQfJ-faVn_WGjFr9GPHjzprrX2iVUE2C9UzoeTK-IGiJz1F9YR_M4IQmp8Rvv9lIODNW8h3SqBUNWVNRhEB48CW4sGtT36TkZpKgzgKp_oTBJhgd9hj4Wa-s23LkclkGU-hP5bwnFwHqOGSDW_GJ9QIAOzeh44p_cur127cYPEVorsN_wR4rIrexRekGMdIX-gk933pAKFgNvuDG27l4aIWSISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xo8UNhXLIdJgzxtSYa-2fMj31LP5MH15xVYGT9M5cp0wl_JWZhZPnlrxxeCpJxEqBCjs4cR28onqkSRft977teIaSVNhq9lEkN-dzWSvoZJ-d1_q9ArKO27o7mw-qwIw-i6KnPMO9k64Jd9slCeMMTV1kHYbxfjD8VomI2DfylJlMsDY2N4U5bdnjTI8gkD6K5PllzugRRUw2LlkJXg7Ks_cwXynmhxcyxUQDWDFo6Ky__K6g0A2AH9ioZhvEOR60EVTXY29BtM-oYD_d4nydueB6j9C5v2AaGygQFy8gE5bo8JCt2Ee3DyNK5oi6QVDG7DSjnQaHi0xsXp9APY_bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیاین به زبان‌ساده بشنویم که چرا چاپ‌پول بیشتر به تورم ختم میشه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/678921" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVJ0etJT5ch5meMl7BEtXBp0x7mXUSL3cvemk4_BLmiCZoU4C_hQlWFkc74TYIEjGndlHiHD2GgoBxFMWbWnzaEFWzFRZhWpgEIRY0G0g4cB3pudagKLOiNTBEgKtCRM2yHPqWrFqCcxpkTCrAdOra-5BOQ2rwPrgUaM53b-Zsj7fZCCnrPCHGAfWY_xmhReqLFmr4e-OsIElfd0x9q373ZjTSRzLqLcKohrZSNSnOwowDKSMNegx449_vi1WaHjqUSJ6kEtoZjcVlOYSpFfeZZwibhIOlhyl9bQcG-w4gXs3WIp2zA3V2MtR8nNkSEEhXluLRWZHeuKLqPRKb0zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
بررسی صورت‌های مالی ۳ ماهه نخست ۱۴۰۵ نشان داد
✅
تغییر مثبت در عملکرد مالی بانک صادرات ایران/ درآمد عملیاتی ۸۰ درصد رشد کرد
🔹
بانک صادرات ایران با هدف بهبود عملکرد خود در خدمت‌رسانی به مشتریان، فرآیند اصلاح ساختار درآمدی را سرعت بخشید و طی ۳ ماهه نخست سال جاری موفق به افزایش ۸۰ درصدی درآمد عملیاتی و ۲۶ درصدی سود خالص شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678920" target="_blank">📅 16:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فراجا: ویدئوهای بازنشر شده از سخنگوی پلیس درباره حجاب و برخورد با هنجارشکنان، جعلی است.
🔹
کویت دستور تعطیلی تنها مدرسه ایرانی را صادر کرد.
🔹
محمد حقیقی، صداگذار و صدابردار پیشکسوت سینما درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678918" target="_blank">📅 15:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رویترز: در حمله نیروهای مسلح یمن به مواضع نیروهای وابسته به عربستان در حضرموت و مأرب، دست‌کم ۳۰ نفر کشته شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/678917" target="_blank">📅 15:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678915">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
واشنگتن‌پست: کمبود بحرانی مهمات ارتش آمریکا از ترامپ پنهان شده بود
🔹
ترامپ در جلسه کابینه از پیتر هگست، وزیر جنگ آمریکا، درباره کمبود شدید مهمات انتقاد کرد؛ هگست نیز معاون خود را مسئول اطلاع‌رسانی ناقص به رئیس‌جمهور دانست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/678915" target="_blank">📅 15:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678914">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای الحدث به نقل از منابع آگاه: بیانیه‌ای مشترک از سوی عمان و ایران به‌زودی منتشر خواهد شد که از ایجاد یک گذرگاه موقت در تنگه هرمز خبر می‌دهد
🔹
این گذرگاه تا زمان نهایی شدن ترتیبات مربوط به عبور دائمی مورد استفاده قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/678914" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
♦️
همکاری با امارات، فلای‌دبی و قطر ایرویز؛ آیا جنگ و تحریم‌ها اجازه خواهند داد؟
🔹
یک مقام مطلع فاش کرد یک شرکت هواپیمایی تازه‌ تأسیس ایرانی مذاکرات خود را برای همکاری با شرکت‌های هواپیمایی امارات، فلای‌دبی و قطر ایرویز آغاز کرده و همزمان جذب مهمانداران چندزبانه را نیز در دستور کار قرار داده است.
🔹
با این حال، در سایه تنش‌های منطقه‌ای، پیامدهای جنگ و محدودیت‌های ناشی از تحریم‌های بین‌المللی، این پرسش مطرح است که آیا این مذاکرات به قراردادهای عملیاتی منجر خواهد شد یا موانع سیاسی و اقتصادی، مسیر این همکاری‌ها را تغییر خواهد داد؟ صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678913" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
جلسه وبیناری مجلس در روزهای یکشنبه و دوشنبه
سخنگوی هیئت‌رئیسه مجلس:
🔹
جلسات صحن علنی مجلس در روزهای یکشنبه و دوشنبه هفته آینده به‌صورت وبیناری و با محوریت ادامه بررسی لایحه جنایات بین‌المللی برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678912" target="_blank">📅 15:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb4e8ab6b.mp4?token=OFL39BMmBhWk6-Kl-SaNBjF7wiNGFzbjjKeyEBdvTW-oN8BZb3gz8jQ4E7zKMUvooKmpBKCIH5t7LP8AbLGjSMcHhNobnCgHITuhYne7eE0eRnMxHwVYdVrohpGnosTgYregM8txfYT7K9llMNvXVsTcAelXZrV6LjC7OZptDrK4d7Tun2-F3BX1bo4xGM6KbuINge3qQTZwHi9vG_pXaRmb7vJD6lH6qm9qP372rOU7Z2Dguu0crqJ7Qi7fnB_2IOduN0r0e-PEcuGHoCX1OqIWlklYqX4IaISfj7YY1_V0OK1J1y-IERLmXSTPvtupzRgnWEm1vIhqdoUgVOiuRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb4e8ab6b.mp4?token=OFL39BMmBhWk6-Kl-SaNBjF7wiNGFzbjjKeyEBdvTW-oN8BZb3gz8jQ4E7zKMUvooKmpBKCIH5t7LP8AbLGjSMcHhNobnCgHITuhYne7eE0eRnMxHwVYdVrohpGnosTgYregM8txfYT7K9llMNvXVsTcAelXZrV6LjC7OZptDrK4d7Tun2-F3BX1bo4xGM6KbuINge3qQTZwHi9vG_pXaRmb7vJD6lH6qm9qP372rOU7Z2Dguu0crqJ7Qi7fnB_2IOduN0r0e-PEcuGHoCX1OqIWlklYqX4IaISfj7YY1_V0OK1J1y-IERLmXSTPvtupzRgnWEm1vIhqdoUgVOiuRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی به یکی از بزرگ‌ترین پالایشگاه‌های روسیه
🔹
پالایشگاه نفت یاروسلاول روسیه در پی حمله چندین پهپاد اوکراینی دچار انفجار و آتش‌سوزی شد؛ این پالایشگاه یکی از ۵ پالایشگاه بزرگ روسیه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678911" target="_blank">📅 15:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff31cbc30.mp4?token=NOd4clWQr_VyBGnYx0aKf5bhTgoCMyVgLULNKl5CTtvuNo-ImY4Uzm4C_QQV8h7UyLZORXjAw0pclxms1Lv9RQbyhrLlxb45JG9evqghSMTUnZ4t7blVbde6ajGy368TgOUB7K5gLqCI5C-YRg5jLbyF8HXmzGuw3qgB6S-fyt5Gf7HD4oW4ohhbIEC0gbfQEE1j5Jv8bEfCGE6HeEC-8Nvjh3wuqXheYZBMrHGHjELP043ebPQ7HjmVBy3VvRZ5BvZCQ2fM_Vid3ZXDYHMxeBCdaY0Qod5UmP56gkeSpJR4EFkkiWbjAkvqQB23XvEkpUOYDhVjzIkO8l6UfBguuD5y-svYQIOE_nZYsL_hixyrMILha9QUSmxFxiQTr3EQ_h3qqzq_ICS_XIt338qcmeQjeQEdVzxZWF52augefl6XVlqRfj-IE8dlsgNrnEHJKsdrcMdOkcDtaVZob845JSEGCx4mKQmx39nueHwLSCrnLvhCUZ_cGUd5m4xF19lPJ8X9LDsqIsi7KKLmrkiQVdmXiv_kGt45QwEFIYZLfd39cov03Xq2G-zKy57kd73NTGTcVSp7gVIGbPk_2bPFXcYa5dGSqZjJSfj4wH8PLbAgC3KZ5qHznoYIGz6LbMksj_gUQl35iEmww09ypdITSb0qOAjaloK5hc3sA5_kVL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff31cbc30.mp4?token=NOd4clWQr_VyBGnYx0aKf5bhTgoCMyVgLULNKl5CTtvuNo-ImY4Uzm4C_QQV8h7UyLZORXjAw0pclxms1Lv9RQbyhrLlxb45JG9evqghSMTUnZ4t7blVbde6ajGy368TgOUB7K5gLqCI5C-YRg5jLbyF8HXmzGuw3qgB6S-fyt5Gf7HD4oW4ohhbIEC0gbfQEE1j5Jv8bEfCGE6HeEC-8Nvjh3wuqXheYZBMrHGHjELP043ebPQ7HjmVBy3VvRZ5BvZCQ2fM_Vid3ZXDYHMxeBCdaY0Qod5UmP56gkeSpJR4EFkkiWbjAkvqQB23XvEkpUOYDhVjzIkO8l6UfBguuD5y-svYQIOE_nZYsL_hixyrMILha9QUSmxFxiQTr3EQ_h3qqzq_ICS_XIt338qcmeQjeQEdVzxZWF52augefl6XVlqRfj-IE8dlsgNrnEHJKsdrcMdOkcDtaVZob845JSEGCx4mKQmx39nueHwLSCrnLvhCUZ_cGUd5m4xF19lPJ8X9LDsqIsi7KKLmrkiQVdmXiv_kGt45QwEFIYZLfd39cov03Xq2G-zKy57kd73NTGTcVSp7gVIGbPk_2bPFXcYa5dGSqZjJSfj4wH8PLbAgC3KZ5qHznoYIGz6LbMksj_gUQl35iEmww09ypdITSb0qOAjaloK5hc3sA5_kVL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این سرزمین با عشق مردمش پابرجا مانده و پابرجا خواهد ماند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/678910" target="_blank">📅 15:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7638006ac7.mp4?token=CcAfb0KDDbK2dnne8hc8vmB8Vz2sXTn95WMyF_PgymcJJxi9uoSvqX1ZCz_kkKQs8T-FoKPwltzxHrUdS6z9qXXZIsaZ2iQzCrKhpX0PRcZfe-qFTd_UZx6xCVPMrdgUsrYCLW4ffrLe69KOh5B6MKmU3eCztsO4SXLIRro96Lh2Wpy8xl0k9cjc_ShOuAt-3Xh7atseDWhqPk-n1hf9qaxySLMZmzPAJjGosm8ztRDLDwHipif3ypY1i03MnsdIrQLoz-Ji7khNt2ybGmrYXMaD66bvlCIXvNFAxvp88G_NxdVuCl-PiZ24jYXkVZ1vbD15BmPO9lEeVtf4e0KON5M8TMgKIHgzlTRwkAAtw2dEIZjiF0HsZywCiinKyfH4yONqfeuGypPO7nUD5fQA8W__P3moAtiPN3GomUMdhOLEoZhn2jNvoMS3JFdQlKpHV8OMPcvlFgxLlQq2JJMVmp9JGfvjk5QfeTODgc7IOoyudoJcJNGRLLuFeO1gbrhKwATdIIOz2ozcFzatPbOJhpWJQPBC-8MSS1lrrutEeB1PjHmN0vK9of9CblKvROzn3t6Lkv6yfh-RUSv9B8BaZ5_plqo4RarTeu5k4ESjAnRJF3dQUKYyPdYA4QRuoBtqn4dMGGKKw0zspY0BwAGn7x9MTByeeI_gYVfaKyZF2b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7638006ac7.mp4?token=CcAfb0KDDbK2dnne8hc8vmB8Vz2sXTn95WMyF_PgymcJJxi9uoSvqX1ZCz_kkKQs8T-FoKPwltzxHrUdS6z9qXXZIsaZ2iQzCrKhpX0PRcZfe-qFTd_UZx6xCVPMrdgUsrYCLW4ffrLe69KOh5B6MKmU3eCztsO4SXLIRro96Lh2Wpy8xl0k9cjc_ShOuAt-3Xh7atseDWhqPk-n1hf9qaxySLMZmzPAJjGosm8ztRDLDwHipif3ypY1i03MnsdIrQLoz-Ji7khNt2ybGmrYXMaD66bvlCIXvNFAxvp88G_NxdVuCl-PiZ24jYXkVZ1vbD15BmPO9lEeVtf4e0KON5M8TMgKIHgzlTRwkAAtw2dEIZjiF0HsZywCiinKyfH4yONqfeuGypPO7nUD5fQA8W__P3moAtiPN3GomUMdhOLEoZhn2jNvoMS3JFdQlKpHV8OMPcvlFgxLlQq2JJMVmp9JGfvjk5QfeTODgc7IOoyudoJcJNGRLLuFeO1gbrhKwATdIIOz2ozcFzatPbOJhpWJQPBC-8MSS1lrrutEeB1PjHmN0vK9of9CblKvROzn3t6Lkv6yfh-RUSv9B8BaZ5_plqo4RarTeu5k4ESjAnRJF3dQUKYyPdYA4QRuoBtqn4dMGGKKw0zspY0BwAGn7x9MTByeeI_gYVfaKyZF2b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گاهی مهربانی یک مادر، مرز نمی‌شناسد…
جیلان، علاوه بر دو فرزند خودش، از دو کودک دیگر نیز مثل فرزندانش مراقبت می‌کند. امروز، این خانواده ۵ نفره با فقر غذایی دست‌وپنجه نرم می‌کنند و سفره‌شان چشم‌انتظار مهربانی شماست.
🌿
پنجشنبه مهرورزی این هفته را به تأمین مواد غذایی خانواده‌های نیازمند اختصاص داده‌ایم.
🏦
شماره کارت:
💳
6037991199529904
💳
5894637000012820
💳
6037991199500038
🔖
شماره شبا:
IR710170000000216780692009
📞
*780*35260#
📌
اگر مایلید کمک شما فقط برای جیلان و فرزندانش هزینه شود، از طریق واتساپ یا تلگرام به ما پیام دهید تا راهنمایی‌تان کنیم.
📲
+989101785282
🤍
گرسنگی سهم هیچ‌کس نیست.
🌿
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/678909" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای وزیر امور خارجه ترکیه: در مورد مسائل فراتر از تنگه هرمز، به‌ویژه در مسئله هسته‌ای، توافقات اصولی مشخصی میان ایران و آمریکا حاصل شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/678908" target="_blank">📅 15:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ، ونس را وارث جمهوری‌خواهان می‌خواهد؟
واشنگتن‌پست به نقل از منابع آگاه:
🔹
ترامپ به‌صورت خصوصی از حامیان مالی خواسته در انتخابات ۲۰۲۸ از جی‌دی ونس در برابر مارکو روبیو حمایت کنند؛ هرچند مشاوران می‌گویند تصمیم نهایی هنوز گرفته نشده است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/678907" target="_blank">📅 15:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485ed10759.mp4?token=cjSiN-9igbp14CCpSZAImQrmR9Ih8sR7Xn9tU59AfWpz35vKyhFqr-b_2hXSb7T_UM6DYkLfo65_R3hkjKkxurEtuWcnE8_0Ov_FYivrrAh2KIGw1f14G6dI2pMfP-hB9TvjzbnQ7uJdrQw-GOHv-2DA-K0DcQI0nK1Rg6jibC6keiQwsS879UWYwTD1Bu364ONqz9LJslc_dEkRNrkVBFqjFPEY-dUk5gaJaRhp1Hg-gzaE5hwJODhaAI1c_Dz-Fx3LaIYJ6X-ACZno_rFzIDUOvi1za7kQz30-k3jveNdWyfetzO8krH6d_rXjvyKyvyDsr7aLjtEtz1oivwQfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485ed10759.mp4?token=cjSiN-9igbp14CCpSZAImQrmR9Ih8sR7Xn9tU59AfWpz35vKyhFqr-b_2hXSb7T_UM6DYkLfo65_R3hkjKkxurEtuWcnE8_0Ov_FYivrrAh2KIGw1f14G6dI2pMfP-hB9TvjzbnQ7uJdrQw-GOHv-2DA-K0DcQI0nK1Rg6jibC6keiQwsS879UWYwTD1Bu364ONqz9LJslc_dEkRNrkVBFqjFPEY-dUk5gaJaRhp1Hg-gzaE5hwJODhaAI1c_Dz-Fx3LaIYJ6X-ACZno_rFzIDUOvi1za7kQz30-k3jveNdWyfetzO8krH6d_rXjvyKyvyDsr7aLjtEtz1oivwQfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاشه‌های ناوگان دریایی آلمان نازی نمایان شد
🔹
کاهش سطح آب دانوب بر اثر خشکسالی، لاشه ده‌ها ناو جنگی آلمانی از جنگ جهانی دوم را نمایان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/678906" target="_blank">📅 15:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIw_8bv5jIDy02JXvZFQh4rmkZPF37_QkcXt3h2Kfse1Lv-4igF6yyZ-jRn0fYA-rJU4bLJ8Tg4a23ppt8Vs69BWGPJO0DchfFtsiz_xJDhFm-geL4kcnSMfGhESdLCM5Fiz08woaeWXOwKbFKLZQbX49MZ1w_00to9xeCBzx-Zaq_MCdnV_9Qvma8z3tW-QNzoekOGkE816h4dd6hqbozQ7mnP2ZVAP-_QznQE1AI9nIGjStcu6euLm1DI-TeNhc-Fg8RPpLl_KD5WCpoOmPl2V601m1L25LJkdJzV0SA2CXcO5c3pzmjKvPOXHU2AI-BFV5amjzTm_pih6fVk84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۵ مرداد ۱۴۰۵؛ ساعت ۱۴:۵۵
🔹
بازار سکه امروز برخلاف دلار صعودی بود؛ سکه بهار آزادی به ۱۸۱ میلیون و ۹۰۵ هزار تومان رسید.
🔹
ربع‌سکه ۵۳ میلیون تومان قیمت خورد؛ دلار اما به ۱۸۷ هزار و ۶۰۰ تومان عقب نشست./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/678905" target="_blank">📅 15:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای هرمز لتر: ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است
🔹
که این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/678904" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
روایت مستندساز آمریکایی از فرهنگ، تنوع و پرچم‌های قرمز خونخواهی در اربعین امسال عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/678903" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678901">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای نماینده مجلس درباره «نحوه ردزنی محل استقرار شهید لاریجانی» صحت ندارد
🔹
در پی طرح ادعایی از سوی یکی از نمایندگان مجلس مبنی بر این که محل استقرار شهید علی لاریجانی در جریان جنگ رمضان که منجر به شهادت وی و تعدادی از همراهانش شد، از طریق تماس تلفنی فرزند…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/678901" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678900">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01786ee176.mp4?token=qTANXdvIvMjNXMGBDhkALx_2M4UDrMZkpe99QanTTZTm25YTugYP_9aOXeQUyFLmHOI0U5tamJ3BghwrBK3UJOnUDs97C-y0WI71yL9TmujAOWFJoC_V8zeqOkSm5IvDpZ1K7-uJeH4cXb41PwRaLXOMd5-l0W7r5oYDX0MSww4mAoZLzEoUiuJmQRAObjuF-KLtg3894OMEyQCYE4_-csFS-3BRu2oLJ68YV3naarplSXI_lk4nf7sIasdZjAuBmodweJjtOAGSPKkaNTc9NpoGbhsF2MMts7dpK-HhcWgzEJBXchmTpxoIW_bPxWK9yWLKRj66LWJACqMtiiJaGklZ-Pvpjiy51vhXTm_3CUXL5ef5f-1OG3ZOgWmr_IFyMpUYswn34Dq4xlyRZnfk5cB4KuK9xVtQsIrls4yx9ZT36JzfBY90pGwK-1Zhi2RF7ZPrIWq6zHvZFj0M04DTNOVfJDgg_OEV6y-BWOqM2oZaFjJI7Si51TjrqSBhZlC4Rn_0VnvVFskDuPgIWsyENwXewRhuQcz3EF3OglcmY1x6O1ZY-6uAvMSUPlYAMJPagmZmdUIuaWg_4t5u4WeFUA_AUniHnWWuVV4bPLXoUzPtX3Oke4V_kk258RYl4DHUVmyNWiivjB4m0On7SJ4M1SD2Sl-DAJXMFqbnXWVCKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01786ee176.mp4?token=qTANXdvIvMjNXMGBDhkALx_2M4UDrMZkpe99QanTTZTm25YTugYP_9aOXeQUyFLmHOI0U5tamJ3BghwrBK3UJOnUDs97C-y0WI71yL9TmujAOWFJoC_V8zeqOkSm5IvDpZ1K7-uJeH4cXb41PwRaLXOMd5-l0W7r5oYDX0MSww4mAoZLzEoUiuJmQRAObjuF-KLtg3894OMEyQCYE4_-csFS-3BRu2oLJ68YV3naarplSXI_lk4nf7sIasdZjAuBmodweJjtOAGSPKkaNTc9NpoGbhsF2MMts7dpK-HhcWgzEJBXchmTpxoIW_bPxWK9yWLKRj66LWJACqMtiiJaGklZ-Pvpjiy51vhXTm_3CUXL5ef5f-1OG3ZOgWmr_IFyMpUYswn34Dq4xlyRZnfk5cB4KuK9xVtQsIrls4yx9ZT36JzfBY90pGwK-1Zhi2RF7ZPrIWq6zHvZFj0M04DTNOVfJDgg_OEV6y-BWOqM2oZaFjJI7Si51TjrqSBhZlC4Rn_0VnvVFskDuPgIWsyENwXewRhuQcz3EF3OglcmY1x6O1ZY-6uAvMSUPlYAMJPagmZmdUIuaWg_4t5u4WeFUA_AUniHnWWuVV4bPLXoUzPtX3Oke4V_kk258RYl4DHUVmyNWiivjB4m0On7SJ4M1SD2Sl-DAJXMFqbnXWVCKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: آمریکا درباره تاب‌آوری مردم ایران دچار اشتباه محاسباتی شد؛ با حمله به مدرسه میناب خواستند بی‌رحمی خود را نشان دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/678900" target="_blank">📅 14:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678899">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ و هگست در کمپ دیوید بر سر نگرانی از کاهش ذخایر موشکی مرتبط با ایران با یکدیگر درگیر شدند
🔹
در نشست آخر هفته در کمپ دیوید، ترامپ از وزیر جنگ، خواست درباره کمبود شدید مهمات و تسلیحات توضیح دهد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/678899" target="_blank">📅 14:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
شرط جدید بازنشستگی؛ افزایش سنوات الزامی برای برخی کارکنان
مدیرکل امور فنی صندوق بازنشستگی کشوری:
🔹
سنوات لازم برای بازنشستگی برخی کارکنان بر اساس سابقه خدمت در ۳ مرداد ۱۴۰۳ افزایش یافته است؛ برای سابقه‌های ۲۵ تا ۲۸ سال، سالانه ۲ ماه، ۲۰ تا ۲۵ سال، ۳ ماه و ۱۵ تا ۲۰ سال، ۴ ماه به سنوات لازم اضافه می‌شود.
🔹
این افزایش تا ۶۲ سالگی مردان و ۵۵ سالگی زنان ادامه دارد؛ افرادی با بیش از ۲۸ سال سابقه و همچنین ایثارگران، معلولان، مشاغل سخت و زیان‌آور و برخی بانوان واجد شرایط، مشمول این تغییر نیستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/678897" target="_blank">📅 14:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678896">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b4c718a1.mp4?token=WsQnnK7Ruv9NV6_CSV3sH6ZDSM64J-5ShXp3gPKbl-DtSDH3EYbvqI4meDoZij0yQEDnOkuYYWHZslKsYaY3ZSoLVVgtBio2WQAC5GbGPCwWvZpsWGNV1LxYYXIGlpUcyv_w3i5uV0wiCQ8nZwznlbZQTjHeXdFF_YvPMSCtGYoX4Ch7N8jWne1ttq4d7budigCl7sNjHIBBkUy5fZ5lWTSfMLzKgo3guIg4CNQwm_zCBlxtRl_hAlmZHfJeC6K4l0ovqwMQgXQvHe3SQmWAd-kS_xuZ-NggSV6VB8KtDo4xpZ24GrCc_x5HUzLPw2P8mn3dACpgNw6VENlhA_KJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b4c718a1.mp4?token=WsQnnK7Ruv9NV6_CSV3sH6ZDSM64J-5ShXp3gPKbl-DtSDH3EYbvqI4meDoZij0yQEDnOkuYYWHZslKsYaY3ZSoLVVgtBio2WQAC5GbGPCwWvZpsWGNV1LxYYXIGlpUcyv_w3i5uV0wiCQ8nZwznlbZQTjHeXdFF_YvPMSCtGYoX4Ch7N8jWne1ttq4d7budigCl7sNjHIBBkUy5fZ5lWTSfMLzKgo3guIg4CNQwm_zCBlxtRl_hAlmZHfJeC6K4l0ovqwMQgXQvHe3SQmWAd-kS_xuZ-NggSV6VB8KtDo4xpZ24GrCc_x5HUzLPw2P8mn3dACpgNw6VENlhA_KJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روستای خواچكين، خمام، استان گیلان
🇮🇷
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678896" target="_blank">📅 14:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678895">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af17a92c36.mp4?token=JiPS4YzcUuXLBU1fTkzZBnEOQnsDUUktsGpaie17cNCZJsFxiHCEJ2I2DODz9we6YLjmQ1DNX2wR51g2-yy1M2NoQzqJvCpzNwIGWYhbb3LP299HacAVqAJXW8JPmYCFatKDJoAKGkpXY7aVrnqib5xym0ZJO0LCrVqzrp1rSncoYdU1bcxTWJpF9AnYYkCqYT7hhO8IOrVZ-B1tgRYg9WW7AleFcc7_G6KsiNykodq4KDCFCe1jdiOc_-GPS3lhAUaEEhV5QPq2Fl7Cs2l7JtnjbciSvcjrhqKN1CD48IkOLqWOLU1lSyXD2dqzn6EMtxANWCauLYmCQlRtGP9esA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af17a92c36.mp4?token=JiPS4YzcUuXLBU1fTkzZBnEOQnsDUUktsGpaie17cNCZJsFxiHCEJ2I2DODz9we6YLjmQ1DNX2wR51g2-yy1M2NoQzqJvCpzNwIGWYhbb3LP299HacAVqAJXW8JPmYCFatKDJoAKGkpXY7aVrnqib5xym0ZJO0LCrVqzrp1rSncoYdU1bcxTWJpF9AnYYkCqYT7hhO8IOrVZ-B1tgRYg9WW7AleFcc7_G6KsiNykodq4KDCFCe1jdiOc_-GPS3lhAUaEEhV5QPq2Fl7Cs2l7JtnjbciSvcjrhqKN1CD48IkOLqWOLU1lSyXD2dqzn6EMtxANWCauLYmCQlRtGP9esA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا صندوق سیمان انتخابی هوشمندانه برای سرمایه‌گذاری است؟
مهدی محمدی، مدیر سرمایه‌گذاری صندوق سیمان در
#گفتگو
با خبرفوری:
🔹
صنعت سیمان در ۱۰ سال گذشته یکی از پربازده‌ترین صنایع کشور بوده و به‌طور متوسط سالانه حدود ۲۰ درصد رشد سودآوری دلاری را ثبت کرده است.
🔹
سیمان یکی از صنایع پایه اقتصاد و از ارکان اصلی پروژه‌های عمرانی و ساختمانی کشور است.
🔹
اگرچه محدودیت‌های انرژی بر تولید سیمان اثرگذار است، اما کاهش عرضه معمولا به افزایش قیمت محصول منجر می‌شود و بخشی از این فشار را جبران می‌کند.
🔹
سودآوری پایدار، تقسیم سود مناسب، جریان نقدی قوی و ارزش‌گذاری مطلوب، از مهم‌ترین دلایل استقبال سرمایه‌گذاران از صنعت سیمان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/678895" target="_blank">📅 14:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای نماینده مجلس درباره «نحوه ردزنی محل استقرار شهید لاریجانی» صحت ندارد
🔹
در پی طرح ادعایی از سوی یکی از نمایندگان مجلس مبنی بر این که محل استقرار شهید علی لاریجانی در جریان جنگ رمضان که منجر به شهادت وی و تعدادی از همراهانش شد، از طریق تماس تلفنی فرزند شهید با خانواده شناسایی شده، پیگیری‌ها از پرونده تشکیل‌شده در مورد شهادت ایشان نشان می‌دهد این ادعا صحت ندارد./ میزان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678894" target="_blank">📅 14:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678893">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d769281469.mp4?token=D7eTKvKWWtQKeY8Y0Xeuu8VExwdDFG1PXXZx6_Lwga3ko-nHXmG09b4CEPEg6Zr355QsWLJ02fB-LScvk68bXYb_jNza_69W4V3V69t3-CV7j-pvrbEe8Yjybbot7RcHY2iCpHEUkoJYNtf7NQBrSl0LEJLmGauAOtjq4hFX70hAqQAWykmV5zJCdIeWN31-UGqCwj12tl3kGfPTlhEDXAa2YZJqkNZDPdy0pFsJsrClE1acbzZLG780qknzWBCJGBs9ZUjRSutqA4PYSz-LZmLXRWoDunqM-LJeHY1quNEbw9KZ-BvPhqaX2LGFTGuBcZ4lqwG4nAxIj92KnZ0PyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d769281469.mp4?token=D7eTKvKWWtQKeY8Y0Xeuu8VExwdDFG1PXXZx6_Lwga3ko-nHXmG09b4CEPEg6Zr355QsWLJ02fB-LScvk68bXYb_jNza_69W4V3V69t3-CV7j-pvrbEe8Yjybbot7RcHY2iCpHEUkoJYNtf7NQBrSl0LEJLmGauAOtjq4hFX70hAqQAWykmV5zJCdIeWN31-UGqCwj12tl3kGfPTlhEDXAa2YZJqkNZDPdy0pFsJsrClE1acbzZLG780qknzWBCJGBs9ZUjRSutqA4PYSz-LZmLXRWoDunqM-LJeHY1quNEbw9KZ-BvPhqaX2LGFTGuBcZ4lqwG4nAxIj92KnZ0PyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یوتیوبر آمریکایی از ۲۲میلیون زائر امسال اربعین و تعجب او از موج خونخواهی رهبر شهید ایران در بین زائرین اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/678893" target="_blank">📅 14:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlFuN35x6UN7d3njd5N3IjgB3NQ7Hpi_Pw_RhQuMmxGZUKH4KpZBpc_lMYsCEVj80vsHhohdTOEVjxTBKmfPP9Pc_bu_LwQXCMl6Pmlo2teVELnwZN3CO3kwgMajwPpRzjlyrOc8kz28BourtK-XN1D5xu2vpOROzgRLWFSitsq1e_Ue-VJaLiXxeN3DXlnTE_PtNR2xnMimpuccJ9xN16_2U6OnObLQnTKSRrtG_P1j0wRl-zOnaaf7ty0dKkWDhR7CY58HAtoq0rfkHyHksh6XgyUalngpv40MMqzpFDu580xTZOIwGpn1e15M-4hlkkKBTyNNS_zVvpGkZ3PJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1ayq-XdYPbprwTiUkWQ8-wkoZAMBxaAbzIu-DoqZJvri2bXJmJmssgcJ8tb2eP_xTkOZiFlpWrpZWN-GTB75ELvodf1QKBkrbiheESyQCyOUWn5R8W9LpXuYeVbTxulbOSLxwWI6V7w-GkRpEsNfftyhLJwzXAuQvFwb6V-1Cbz9Ha0y4BJoF5JwXd1LuGspn5H6mfgKBkmlChE8X9ZuQwL0TYo2ejWbgkg8TgEz6bEr1zlTI2olIh2C4ssFJvFkWqZGBo7YpmMX99iggG3DUF6XTZFB_LZ1O7hBqSLwD8nGTEdkLA82vqF_D7WavOqyxn1UDexG5Bqhg6-ob2rGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
به همین راحتی شالت رو خیلی شیک و ساده اما باحجاب سرت کن
✨
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678891" target="_blank">📅 14:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2b4c27b6.mp4?token=NzUuSs_kTqdIsZXKTZUJmM7P1LnaMOAlcjBDXZ0bChUtyTsn_HS6-XrutpVj6XLtPlv-7Iqg4GqbmiN5iHECmC2vWPl8ja165kSzmHWKyvaN2LebFjP8FAWl-uNGsVgrmxOMuhx5qqJzXKO0wPqZNPyoK5MAn_hWUFqmW0BRoSOJW12v7OkRbUAvY_1RPZqRZw_ow14dgMIbtj488KMzxnYL0Gv8P6KssoP_0zAcanNWLBApCxhf-FvrDt2n6vDhe3tQi0NkaVQ9J3rXB-tNeOn00qaPo0omcuOxMp0QMQE9Sv5PfOdjs56SpYM5-HLAWSHDbuv7DsrekgTId56pxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2b4c27b6.mp4?token=NzUuSs_kTqdIsZXKTZUJmM7P1LnaMOAlcjBDXZ0bChUtyTsn_HS6-XrutpVj6XLtPlv-7Iqg4GqbmiN5iHECmC2vWPl8ja165kSzmHWKyvaN2LebFjP8FAWl-uNGsVgrmxOMuhx5qqJzXKO0wPqZNPyoK5MAn_hWUFqmW0BRoSOJW12v7OkRbUAvY_1RPZqRZw_ow14dgMIbtj488KMzxnYL0Gv8P6KssoP_0zAcanNWLBApCxhf-FvrDt2n6vDhe3tQi0NkaVQ9J3rXB-tNeOn00qaPo0omcuOxMp0QMQE9Sv5PfOdjs56SpYM5-HLAWSHDbuv7DsrekgTId56pxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفت‌انگیزترین فلزات دنیا را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678890" target="_blank">📅 13:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kysB2JV2Jx2N8Y5xI-mb1N2z4jGk_66JYzLXRtDJwCmRSlHERykCO_WkxyD3TE3ux1BFZcYprFaXMnOgSyO--iUdrGcWy7oQwj0bt8R2RAtCT63dbV5BA7LOD_lp4MiR2J8bKu02OivTpVNE8rqDIisNKkvDnq1suxYWtfA9CgHlVWXm24_E-10GtHX8VGslLB0xPhtsbRTv6y8NzOGiaw-j8FHc5HL2uwO6t1vLEv7QHsQxrxfeGlscC-0jJ2Fho38HziSCHld20lXJnA5TjJJlsMXPVbVQAVczqsJTHQ2xFdfk72IvrW7uhcduzLXk9wfWeyt0rAROc5l82U0pnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای هرمز لتر: ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است
🔹
که این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/678889" target="_blank">📅 13:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
توقیف اموال شرکت‌های تراستی
دادستان تهران:
🔹
۱۶۷۳ میلیارد تومان از اموال شرکت‌های تراستی تهاتر و ۵۰ میلیون دلار، ۵۵ میلیون یورو و ۵۳ میلیون درهم وصول شده است؛ همچنین اموال منقول و غیرمنقول این شرکت‌ها توقیف شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/678888" target="_blank">📅 13:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: امارات ترامپ را به حمله زمینی علیه ایران ترغیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/678887" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCsrE8HkTy2XaQcLlvBL7P5vmDpgg0MDPM6yPqqMW49OOUFu52eEhl-ARa-Ac1mZNybCq-PGDsW2sBQtkti4SLH07MrowQMPtcYXy6WOrD0ewRwrMCgxo7fYVpoWeZMs-ZK_cPSN3XLyLKt69Ev3VcEUDYIxhRUSC8QAL4VYMuROKOSHlsft2KqqWWreHcxNzorkVd43Re181E6uow-KIX1_A_EHL0I-_bCanZFM8X6PsOHd0SSqvl0YR8WGFkOSrGwp8rKueJhKHNUxQEApWNIbzqsWUewjE6Bam612P22_E4IJNDBVySTZ1EdNNAMH2IucffG_MyCFpvXlXweVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ و هگست در کمپ دیوید بر سر نگرانی از کاهش ذخایر موشکی مرتبط با ایران با یکدیگر درگیر شدند
🔹
در نشست آخر هفته در کمپ دیوید، ترامپ از وزیر جنگ، خواست درباره کمبود شدید مهمات و تسلیحات توضیح دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/678885" target="_blank">📅 13:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e70ce5b7e.mp4?token=arPfSZn-VURV08u0Ii8PsXZoWHz0eKovEj_oadAGz14NQ1DYqfdLzFDhOpLb-3kDvdYyO71dGBgZF6UVA18hUwZ5lkTsw1maAjrRsdGoe2HEaMQbijjaJqBFafhdUeuX-tn5UfHlVpyvKBOL4EbKif4_AFLjok-JFcwN9WfodrT-X1oI0uTOfd7C8jwjPC5BPJQrdzifwPCgpw8RCHTbg0-Ya3_82DG7Nm1IjT1LKnVYVbYG2u7o-DRLVIi7yuRkldR39hplwSsWSOhZbSbPiLgYYrKOT3SuYB72l72rN0yCZlhZpaeM7sMt-IupXaR3PUPjIIgVLUf3joZh9QT_jxgse5kQm6SdF5OJ5nJfBNQJ-y0uMZDF4Q3fPaY18TflG_OFW9W1alp27cgqSIPtY-1ODM8_FfN2pe47sjKZnaw5sRbzdlKINWF0ch0PmQzOxDjkVI6mnhCYoFXVjqxuAddanXvQ7kZD-WhVAg59S3Qkw5rh_QzUevCc_Jn1LnxuMz2_Yo3n3mwasKx9fXw8FaEfOfLgrt4lvJ4pxui4Eoni4w8NtBnt53mPnYHKf6cJrH4fo93T0QH1hWRJzrWJAW_jjPolI34uB7VZvDC1vtqE8q1LhrHuzSeMWJ_2aX5B-ZmCtL9SRLGkm8sIEPoD2igjsd_VNo0zulJ-OX5lyX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e70ce5b7e.mp4?token=arPfSZn-VURV08u0Ii8PsXZoWHz0eKovEj_oadAGz14NQ1DYqfdLzFDhOpLb-3kDvdYyO71dGBgZF6UVA18hUwZ5lkTsw1maAjrRsdGoe2HEaMQbijjaJqBFafhdUeuX-tn5UfHlVpyvKBOL4EbKif4_AFLjok-JFcwN9WfodrT-X1oI0uTOfd7C8jwjPC5BPJQrdzifwPCgpw8RCHTbg0-Ya3_82DG7Nm1IjT1LKnVYVbYG2u7o-DRLVIi7yuRkldR39hplwSsWSOhZbSbPiLgYYrKOT3SuYB72l72rN0yCZlhZpaeM7sMt-IupXaR3PUPjIIgVLUf3joZh9QT_jxgse5kQm6SdF5OJ5nJfBNQJ-y0uMZDF4Q3fPaY18TflG_OFW9W1alp27cgqSIPtY-1ODM8_FfN2pe47sjKZnaw5sRbzdlKINWF0ch0PmQzOxDjkVI6mnhCYoFXVjqxuAddanXvQ7kZD-WhVAg59S3Qkw5rh_QzUevCc_Jn1LnxuMz2_Yo3n3mwasKx9fXw8FaEfOfLgrt4lvJ4pxui4Eoni4w8NtBnt53mPnYHKf6cJrH4fo93T0QH1hWRJzrWJAW_jjPolI34uB7VZvDC1vtqE8q1LhrHuzSeMWJ_2aX5B-ZmCtL9SRLGkm8sIEPoD2igjsd_VNo0zulJ-OX5lyX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر ژاپن در ایران آهنگ سریال اوشین را نواخت و خاطرات یک نسل را زنده کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678883" target="_blank">📅 13:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0G37HLl-cBub-Rv9o5WX_6ztwym8Dy6OiD2eH1idE43ZZgXl-zx_Dx_Cp52yDY14rS3fIVGpcji955XHoIJXs2zHPUj-noudbHufrShnz9KY3osvovxSU_UVIFN212ugrdtbJZumjGsDz-lYXNpYXTGbMOUUeabzAqw9zcJNS9zJHK0770v0Xv8zvrCeOMqVNT--xRDUDPtivWdFmjrJRTD3Kh7kmaStoPdcWnO-Mt2_N10r6baWyilUyDjWiBTP3x29OJxv_Izp5vy6oMfTOgtshbPgFIGA-04NtuGy4ix6sgsNvmHYnnHtT2KWjR9RxjIoq5U2lbyT49WTMM_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امور خارجه پیشین هند: توانمندی‌های نظامی ایران واقعاً شگفت‌انگیز است
🔹
توان نظامی چشمگیر و تاب‌آوری ایران که در طول دهه‌ها تحریم و هزاران حمله آمریکا و اسرائیل شکل گرفته، قابل تمجید است.
🔹
ایران از آن دسته توانمندی‌های نظامی برخوردار است که بیشتر کشورهای جنوب جهانی اساساً در اختیار ندارند. آن‌ها چگونه توانسته‌اند به چنین سطحی از توانایی دست پیدا کنند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/678882" target="_blank">📅 13:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678881">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
خبرهای متفاوت را هر روز در وبسایت خبرفوری کلیک کنید
🔹
🔹
ترامپ ۳۰ سال با این زن دوست بود، حالا به او فحش می‌دهد | جنین پیرو کیست؟
👇
khabarfoori.com/fa/tiny/news-3235763
🔹
جنجال ویدئوی سرباز با لباس زنانه در خط مقدم + ویدئو
👇
khabarfoori.com/fa/tiny/news-3235908
🔹
بازیگر زن مشهور از سینما خداحافظی کرد
👇
khabarfoori.com/fa/tiny/news-3235922
🔹
شهردار در دفتر منشی‌اش دوربین مخفی نصب کرد و گیر افتاد!
👇
khabarfoori.com/fa/tiny/news-3235694
🔹
اینفلوئنسر محبوب در پخش زنده کشته شد! + ویدئو
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
برای مرور لحظه‌ای خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/678881" target="_blank">📅 13:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678880">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27160806c.mp4?token=EvZLxHzLukxg4_CHgN5AU0I70FaA3qI3_JA1nURUYoxJmVLUQRN1etosVvh4hxhIzW6mWqohatNjXKOjK5jSQlGXk_unNse99hy3GAENseUoiZXm7UmBRAGUbPFqQ2p2KbE5w5DIqROI3oML_Rs3fwFJMWCcDR-SSQw5siB_W_upm9yW-avU0-jdnoeHdtCpSu7sEKKCveDwoETmjalGU63EK-gF-BIfKc_yLYYynu5x1r1iFlIBjeSNfWDgx69ufYYt2O1HMGU8ttDS7DtstperBCpVZGQMkYn8ex17IVlp1hEVfWP-628wA_R6NFgnpM_ZKulId1x5P5CQhxLMhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27160806c.mp4?token=EvZLxHzLukxg4_CHgN5AU0I70FaA3qI3_JA1nURUYoxJmVLUQRN1etosVvh4hxhIzW6mWqohatNjXKOjK5jSQlGXk_unNse99hy3GAENseUoiZXm7UmBRAGUbPFqQ2p2KbE5w5DIqROI3oML_Rs3fwFJMWCcDR-SSQw5siB_W_upm9yW-avU0-jdnoeHdtCpSu7sEKKCveDwoETmjalGU63EK-gF-BIfKc_yLYYynu5x1r1iFlIBjeSNfWDgx69ufYYt2O1HMGU8ttDS7DtstperBCpVZGQMkYn8ex17IVlp1hEVfWP-628wA_R6NFgnpM_ZKulId1x5P5CQhxLMhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز شگفت‌انگیز یک سوراخ کلید در رم؛ منظره‌ای که سه کشور را هم‌زمان به نمایش می‌گذارد
🔹
نکته جالب اینکه در این نقطه، به‌طور هم‌زمان سه قلمرو در یک قاب دیده می‌شوند؛ شما در ایتالیا ایستاده‌اید، از قلمرو شوالیه‌های مالت نگاه می‌کنید و در دوردست، شهر واتیکان را تماشا می‌کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/678880" target="_blank">📅 12:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_i1YtVJfROQEWEE7v8123_MYIrTQuWLYaR02lAWG3BxL14bpY_3a5amDFed44zKOOtwT6Ze4iAcTiFj9FrTp5sGcx5GvnrACxxoFlHYAYVPVlfocQtsz-zAn8OO8_1U2AdtOPIAznlxB4_FWT-RlcF5-7PT73PL_e2RmmMzDOYNH6Y_PmLMkUicDU4NnME3G8sYtKQ0G4dRUImOBMbBfOB8oKWBPVZ0PhXLho2myyeWcjiy-RHjyWGFfMqaQBbpbFZvX_SlpTL2zM4_AEY6CDDGhlA0pFOtSbwjq2xJKLDBnSMxjBIUADi2T6UuHMEIfl5wnCdv46M2z_1indu0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBXd9x9l6eLFg-c52j-FEHn11smtgNO9dn491CmKzsChskNH-1fBINdgd15Eu2H9QBbTOCqtQuetSrtspzRP9Lj6cbXCeYqulk0r0Aq51h-L9VSBAP6RdBDjd7yQjMxcQfWw0qT2svoFatiAnJbSlBkAYjGueX0TV6jagLoL7bnoIGf2Y2rvwPUA44RXorOlrR16uy-rFSwcJSzt2rwtnjlRvi1DtZ_dOww1oZhOTb8ZQGLatr5x0-E0mJeqaUoBnhp60QA-W8YzC-rkB4oywtLc3bM3HFJVBDOPqtF0gcFeDBkhLQ6APZqyxZkOAtN0UToQUh--mOJfW3wknbeDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALYZmyIgoF1Em8iFCkF1W8zTPxSrmNKSBlNYm5LFDprG91LKJ4zrEUdELKiOs0FrxDBBJNYlnOKDLOlGVycsQrft8OBHh8aieSV72ymCGU2H_ZHq_7KddUq7kM3t3cPWRRVEu-xdzqXcSpFdKjEkCEw5zPhJdo7bTeg9_4MLS9M0nEbW3oBkxhPwV8883vbT7U0amS6buJLfp_puq_BJlDPnvBMaqyEKpDvEUdQMpbnMYg_o81iDpG-HEpLe5Oi1b80pLhR7y63N06E8M79NQseT18nChcMzfWPWvhlGP-1QC6rAdr3UIqu2eFpapa7MjAL5UuVy1S0UOh_vRfQ6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBso9swR75DNJV9OXVE5z8GV7AvxMHP53xdiMColVBAVACI7UZFaZfRNUeY53HQ-f7cR2pJ7xClVgfNOTprdy9vimplyR4xiCivTQ7_yS8YBWT1GEmEHwywfWkVj_QwI1xd0n_P4NqIclyFZzeZxg8DRe_ylBhw2_x_vJ2ICnzw8X8Megf2BEd2yC3VTPM8T0JrGcmMN8yxNvfg9nV328TVLbNK0onLpKq6p17kuNx5EzTHi7t6TbeN7tQK7fy9XdiemwtqbF5w9yEVSDG5g0ivJ9raGioeO0Vyw-DCCuH8oFaDpwqj0oPqR98K93wLHLGzHugm11in9r8v-NKh0-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
هر یک از ما می‌توانیم با اقداماتی کوچک در زندگی روزمره، سهمی بزرگ در نجات منابع آبی داشته باشیم.
🔸
ماشین ظرف‌شویی را فقط هنگام پر بودن روشن می‌کنم.
🔸
از شستن خودرو با شلنگ خودداری می‌کنم.
🔸
در صورت مشاهده هدررفت آب، محترمانه تذکر می‌دهم.
🔸
استفاده درست از آب را به کودکان خانواده آموزش می‌دهم.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/678874" target="_blank">📅 12:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf38085f0.mp4?token=KZMV_h5gFNRHQTSyeRZksTgjxobLr6IJadU6mNfWBrfr3vczzs8ZqUynSsFp0tb0i7qdpHmEaEvIEmjjohjZDPjLjWvD2mYtpIyc0NyYAwHp9aaJa0Y26IUXOjoxudDbRswo3Uny_0jj1arAqeE3MRBkhTrDa4oyQPEBh1Lv1IQQi3sQX7gDfDbSP7My1iinoXZ66Bf8E1QZHq-2IOjJRM3DUnt0Nkox2jp3O3SPy4e9C71V82zAU6HFmrp9ACjzFCOmFv1JD9Dou69zU42_j5aamau1q5OMps-ojuF51jYogUfn2-Rar-jHdPDNQ27yPJyJWsT7jR4D4RZXD-kjehOPbhMDGB6Ln143TZr0E9lki0GjJUpWb-pAGLJk6MNhsc_coNvJkwBJXSfIVho-8NYog-2i7dTD3uK9Z83Ykv5XfChecs4QiW3lHU9SikMVELsWMQBH8LtWcqqwXrndsgK92Qf3FCtV5iTNq7Uzht3ExpaCMKjvUdD1_GtjirmOnRvJYpAmKj9z_VHWTEAbGYXlIdMHRFf5ynuhBBSF7VIsbBIxLw3cqIMszyeBJnOKtjMs2zvdrzyO4lsgrWSjB0Fw03ryqYeXQKAS7EhHdTMO1Kyz-DR7YRos3LlApG_uYI5nvRKcLV-8D5xpK5MNAPfj5HgIUKxfKLEXCg4rkuE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf38085f0.mp4?token=KZMV_h5gFNRHQTSyeRZksTgjxobLr6IJadU6mNfWBrfr3vczzs8ZqUynSsFp0tb0i7qdpHmEaEvIEmjjohjZDPjLjWvD2mYtpIyc0NyYAwHp9aaJa0Y26IUXOjoxudDbRswo3Uny_0jj1arAqeE3MRBkhTrDa4oyQPEBh1Lv1IQQi3sQX7gDfDbSP7My1iinoXZ66Bf8E1QZHq-2IOjJRM3DUnt0Nkox2jp3O3SPy4e9C71V82zAU6HFmrp9ACjzFCOmFv1JD9Dou69zU42_j5aamau1q5OMps-ojuF51jYogUfn2-Rar-jHdPDNQ27yPJyJWsT7jR4D4RZXD-kjehOPbhMDGB6Ln143TZr0E9lki0GjJUpWb-pAGLJk6MNhsc_coNvJkwBJXSfIVho-8NYog-2i7dTD3uK9Z83Ykv5XfChecs4QiW3lHU9SikMVELsWMQBH8LtWcqqwXrndsgK92Qf3FCtV5iTNq7Uzht3ExpaCMKjvUdD1_GtjirmOnRvJYpAmKj9z_VHWTEAbGYXlIdMHRFf5ynuhBBSF7VIsbBIxLw3cqIMszyeBJnOKtjMs2zvdrzyO4lsgrWSjB0Fw03ryqYeXQKAS7EhHdTMO1Kyz-DR7YRos3LlApG_uYI5nvRKcLV-8D5xpK5MNAPfj5HgIUKxfKLEXCg4rkuE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرورت آشنایی با مانور هایملیخ برای مواجهه با موارد خفگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/678873" target="_blank">📅 12:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9MtpsQbelCYGig-eMISv5ZQYKJnohyibt-6VCdA5OBmUk70GfU8XH9ZJYT_bUhhjqUtJmDeG-6iTSMR92qS6tkwC5rtqXBmIW-b3BCSAcMtWDm-hWiclj6Nip14rEmBwEdbMIUVi3zoMk4Qr9YHTORapxHc4VxsUiXU8yNUsBMCDWtXR6Ux_3SmsJxaELJzLxw5K9MXe2d3FqdLLh694LsTpgebjPqxRo3ENqKSLG82zF_-ZrgvfQgFKX533fzVwYUdt2PsqvEUiPOrg_sOHa4cjZv8jRcyWYJs3iFOtXGBeYLppK7zTShFlOD4P7aK3PBU-_mwtGm08dn4Dyb-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالسید کیست و چرا ناگهان به یکی از چهره‌های مهم سیاست آمریکا تبدیل شد؟
🔹
یک پزشک ۴۱ ساله، فرزند یک مهاجر مصری و از چهره‌های جناح چپ حزب دموکرات، حالا در آستانه ثبت یک اتفاق تاریخی در سیاست آمریکاست. اگر عبدال السید بتواند در انتخابات نوامبر میشیگان رقیب جمهوری‌خواهش را شکست دهد، اولین مسلمان تاریخ آمریکا خواهد بود که به مجلس سنا راه پیدا می‌کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235921</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678872" target="_blank">📅 12:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
یک منبع بلندپایه به العربیه: اعلام توافق برای بازگشایی دوباره تنگه هرمز ممکن است طی چند روز آینده انجام شود
🔹
کشتی‌های ورودی به تنگه هرمز از مسیر کشتیرانی نزدیک‌تر به سواحل ایران عبور خواهند کرد.
🔹
کشتی‌های خروجی از تنگه هرمز از مسیر کشتیرانی نزدیک‌تر به سواحل عمان استفاده خواهند کرد.
🔹
برخی طرف‌های منطقه‌ای ممکن است در عملیات مین‌روبی و اجرای اقدامات فنی لازم مشارکت کنند.
🔹
توافق ۶۰ روزه درباره تنگه هرمز با هدف شکستن بن‌بست و آغاز مذاکرات فنی طراحی شده است.
🔹
تماس‌های غیرمستقیم میان واشنگتن و تهران از طریق میانجی‌ها در جریان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/678870" target="_blank">📅 12:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766c526cd8.mp4?token=YrdgtjHAEtLZhVTV1U4EB2q6NUaAHxqTGCsJu-ghfBM7IUo7EEQVZm96GyT_bZrsmrHPwSGxHHBwh79tJ-slV4Ci3_x4bFzOIuWxSeUQ86ASbF2h7fhe3g0J2fUxihd8JQKYe6YDPCV7cIfPQCzqSAZnPynkrOLTvHp0478JaBCO6-E58dlW3LR6eZ_rl3UKgekmDYXiYIRdu9Tkpmn0ejrvt8MJVUeFcdt8T9edlKMb_V4iDaei_iCTMFXGbUYvua9dvgUULa2Yp_tFRo0wTK4n4bz-VGB577XJZzrP9rCdnMLQ6efYmSv20CInh2by1zEMhQBrgJYhF2l0zvAeiiHfZNPZxe3RSGsJoUmajKn_s2E78dbAvnv7zFn5okQw0SaboWw8mAMYeHiVfIxfnPMkvzLv_8tFbua2-9oKnuI_Og3AkpSeZFZ4p4_XwVeaPY-JFouohIoOfSD4_UF56j2xtOb3AQtSAGxXZeW0jiBMSUt2KRHe6ZYvvHo8OvBXboguut-ImfKh6ZuSmU1nHuEjBnkSdNKIIZKhqLyUeRdgupCHuCuhmwT4oIBe1rhbZf49olKLZ0vJyGvkscMplj1pZaYIiw_YNvEzYnMBc2c31RzQLeHp6CYm84xd0FFyY9rOMaPUI9nbGC0uKcwIJODM_Zr4xPHMm56-3WRJvug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766c526cd8.mp4?token=YrdgtjHAEtLZhVTV1U4EB2q6NUaAHxqTGCsJu-ghfBM7IUo7EEQVZm96GyT_bZrsmrHPwSGxHHBwh79tJ-slV4Ci3_x4bFzOIuWxSeUQ86ASbF2h7fhe3g0J2fUxihd8JQKYe6YDPCV7cIfPQCzqSAZnPynkrOLTvHp0478JaBCO6-E58dlW3LR6eZ_rl3UKgekmDYXiYIRdu9Tkpmn0ejrvt8MJVUeFcdt8T9edlKMb_V4iDaei_iCTMFXGbUYvua9dvgUULa2Yp_tFRo0wTK4n4bz-VGB577XJZzrP9rCdnMLQ6efYmSv20CInh2by1zEMhQBrgJYhF2l0zvAeiiHfZNPZxe3RSGsJoUmajKn_s2E78dbAvnv7zFn5okQw0SaboWw8mAMYeHiVfIxfnPMkvzLv_8tFbua2-9oKnuI_Og3AkpSeZFZ4p4_XwVeaPY-JFouohIoOfSD4_UF56j2xtOb3AQtSAGxXZeW0jiBMSUt2KRHe6ZYvvHo8OvBXboguut-ImfKh6ZuSmU1nHuEjBnkSdNKIIZKhqLyUeRdgupCHuCuhmwT4oIBe1rhbZf49olKLZ0vJyGvkscMplj1pZaYIiw_YNvEzYnMBc2c31RzQLeHp6CYm84xd0FFyY9rOMaPUI9nbGC0uKcwIJODM_Zr4xPHMm56-3WRJvug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری خودمون، حال احساسات‌مون‌ رو بهتر کنیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/678868" target="_blank">📅 12:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhUgBnbfqVnep8jRIKxLk6DbDsM5wHfA4OYklwxNPeir4HIBpe9Rfc3-RkKDo5qgtiIABsKN_E7GJo8NTS7YDuhI1b-gGfJnFc7To-Bqgj4zUMvqfEE32fWG_l5wQrw7nkvXo6PXW_pjwWI9IXBmTXs_QwOR0zRxsWOr6gDLKwtCaZOjBBBqfia6IH62dvGKburpXKkYVNsJLlKaO1dOC6RmX4xuDdYq6-AKZY-HgAHPLG5u2v5PqYttHUTTrblj2ANBvMK9suVG-WwFfSOoTSINSYW15HkF-xu9rzlkrZja4qvEXiaf12giUx46dqcSWP1CYkYhkcdHen0yGIMUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استایل اسپرت و شیک با یک پکیج کامل!
🔥
پکیج ست تیشرت کلاهدار و شلوار مردانه مدل Juventus همراه با کفش ورزشی مردانه مدل Alshen
👕
👟
✅
طراحی جذاب و اسپرت
✅
مناسب استفاده روزمره، پیاده‌روی و استایل خیابانی
✅
ترکیب راحتی و شیک‌پوشی در یک ست کامل
✨
یه انتخاب خاص برای آقایونی که به استایلشون اهمیت میدن!
جنس تیشرت و شلوار: پلی‌استر
سایز: فری‌سایز مناسب L و XL
یقه: گرد
جنس رویه کفش: ترکیبی
جنس زیره: PU
سایز: 41 تا 44
🔴
قیمت 1,698,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/59407/180124/</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/678866" target="_blank">📅 12:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03a869cf7.mp4?token=tTGtHp9oGraDw4WMw61s1F3AohuKV49gIqOsAdsGdrrTKr3Ygh0pKxq-1E9CjZ7lRIJL6eZnX4pv7nc-szeIQ_eSAuj-bvQ9w6zZahVB4r2e8ZSaD_0J3rVuJIkca0bR8TTtD-tcZiCgFGxV5CreHzteWkhw-7PYpcu9Y6NTXNBRq1rfmShDetozSXpXZAH6d1a75LzGvzDwb125svsuSQEbU9PVYV3C7ZC5Mzc-MGPf_uOT7kcW2aAi2tjIHLeWBx-fXJPlN45uhCCUOfSOPtNaiYhXnCXYb5P4fKXmQTmA30aEzLNaZ5iYJj_81dP8LwBIPwZn1Wy5NrtSQ0p8Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03a869cf7.mp4?token=tTGtHp9oGraDw4WMw61s1F3AohuKV49gIqOsAdsGdrrTKr3Ygh0pKxq-1E9CjZ7lRIJL6eZnX4pv7nc-szeIQ_eSAuj-bvQ9w6zZahVB4r2e8ZSaD_0J3rVuJIkca0bR8TTtD-tcZiCgFGxV5CreHzteWkhw-7PYpcu9Y6NTXNBRq1rfmShDetozSXpXZAH6d1a75LzGvzDwb125svsuSQEbU9PVYV3C7ZC5Mzc-MGPf_uOT7kcW2aAi2tjIHLeWBx-fXJPlN45uhCCUOfSOPtNaiYhXnCXYb5P4fKXmQTmA30aEzLNaZ5iYJj_81dP8LwBIPwZn1Wy5NrtSQ0p8Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوشش جدید رونالدو مورد توجه شبکه‌های اجتماعی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678865" target="_blank">📅 11:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPjJZtQC-uxKqSVV8wCwQ4i3qPZLz-fxVvhcSGFfgYziXamzlPIHOHZBXfzyRfnq6KqQD8tnGq7khidXhGw3e98_VJ488MH3_UAZ7Iv9JHQKS2ZVJeyFyDC8WrNYgzaqXyLzJrKhkPLGNTlYc1pmIHr3Smmw99hfJc0xPNucJcqK4CEEzX_5UaGV5bLGQTvrOU0eYZNi10Zr5QBD39VhkawdE7NACoVozXVHAa-MkraywNViG6T6Nd2sn4LibLIwF9Ky0O7_Pn0rnkVNg0rKoqvgNrUaXrga9UUlEdCP7ZCvv_XgY3ebaZ0Q1RebGORlREED5XkJ9E5SicwAc3p3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGWpxVIwUw55IyWeJzIVuwuVZP26-WFBVl4AlhvVjJyaADtWgES-p3fq-VExFUnKBA4GZuVytDZgpafk9d_BST_RLri6hZNQXCpFavUXT32QwQ4HtPzyszItTqGzqe08nJ82GdP6HPLknUV81JXjgU-4hS9Oil7gkp2igLmvECyLMOgxagaUiiugECcJbon9JV9i1MDyTPMZ_kLl47tj7_nnjpOv_PVNpdKqGW3SqEJ-nR6J7fxWFFan4QacfOVIisz9R0vIAM-iy4b5XTCj6VHmGPpA7Vo5SJj-bEJkbHQbe8ZcCTjaYJ4-87N7ABwPMlaHhav6_BzaJJZA5veryg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زنان آسیایی، پیشتاز تحصیل در رشته‌های علوم و مهندسی
🔸
براساس آمار یونسکو در چین ۴۱ درصد از فارغ‌التحصیلان دانشگاهی در رشته‌های علوم و مهندسی تحصیل کرده‌اند. این سهم در روسیه ۳۷، آلمان ۳۶ و ایران ۳۳ درصد است.
🔸
در سهم زنان از فارغ‌التحصیلان علوم و مهندسی نیز کشورهای خاورمیانه تصویری متفاوت از تصور رایج ارائه می‌کنند.
🔸
در عمان ۵۵ و قطر ۵۱ درصد از فارغ‌التحصیلان علوم و مهندسی را زنان تشکیل می‌دهند. ایران نیز با ۳۳.۳ درصد بالاتر از کشورهایی مانند فرانسه، آلمان و سوئیس قرار دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/678863" target="_blank">📅 11:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678862">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CghvOKMteuI8IhNe-yatrXd_iMVwy02140hEaK2L66KapyC9hTPQQdAExiq8M3JpiBaOc9FBrZPQCL4JTeYI0jOSQyvKsz4fEGKgQ37VAaQ-JZSl4HLNLjUnERoHTHV1ar51h7f25sXsg9WcbYcbqAPa3VMOT5GezYWh5kn8LTU6YPIRp3RZtBQYNNF3sXMH5DPneHvQVaeNKl3PLX7O79AghhrVisLNjQUiH4rZ478urk11Chf1WyHEQ2XXvEslEU0IUI-P2g-7Y-kEa49E2CXkVbHYWcpICAppmfjzr-TsbHIL1AtP_qdBDAJT5MOXPxCbxcvx5KvTtRgTnnjLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استایل جدید صابر ابر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/678862" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JseSPCktA-V-ORAU4xgYTW224jlJbQQ7o2_p7bkRlvw7HVVNTKPHz-R9FFj7hJtbC4KBL8lHCeX6K-UAkdkYFEKqYOKnMst1czj5FoTcVL3XImco_iJojMI9Dw1Z_jmmVzvzpWMTce01jvWrn_kCkklMD_X6_WFLGhF2Ami_FKcivGyPCJzEmp7B14hI5LImlpt6big2DEgoyKVjbNirCvxck_H9l9_Leh2KUOZefaa5FkZrwEBxxsuipxGXsJ95VaRmPxQTnuUuRLjSU0rD7FtflNRWKCq3vBUlhpVa7rENAJWJHdyVF6RABeKxRG7GX61CLcaPP4FZcUaX9Azj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاییز پرباران در راه ایران
🔹
سازمان جهانی هواشناسی به‌ تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔹
النینو که با گرم شدن غیرعادی آب اقیانوس آرام شناخته می‌شود، معمولاً بارش پاییز و زمستان ایران را افزایش می‌دهد. تمام ماه‌های پاییز از بارش بالاتر از نرمال برخوردار خواهند بود، اما اوج این بارش‌ها در ماه اکتبر (۱۰ مهر تا ۱۰ آبان) متمرکز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/678859" target="_blank">📅 11:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92a1603b01.mp4?token=eXA28I9T0aP3QvZ4uAnl6II7oISvqSAAPOzWHvjsyzh15Gby1WQunojgACNzozrCtxX6hG5vi3TNoihvdj3mDivFSxvoVzQcqFM8WP1bj0-6x0vX5-4RpJ2JZ98_NG0t3nrqTNPN_PvSL8W9GjAfOQTXQK6KELfRitOSioyIoUb_qFDVD1mn9ltQ0SPZY5AsyVmPlrOx5c7YQO63yOc8hMVGrtmLEE_ZGL5Tp59SjS4k094zrcQqZ_vuK37oZjRw4Uo5Q0id19SCxtjWYmjow4VXF_RhaojV_kyCBiUPG59RZw3yMpL-8REYRQWiS3sR7AzMoQCzjvejWLV0xMtoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92a1603b01.mp4?token=eXA28I9T0aP3QvZ4uAnl6II7oISvqSAAPOzWHvjsyzh15Gby1WQunojgACNzozrCtxX6hG5vi3TNoihvdj3mDivFSxvoVzQcqFM8WP1bj0-6x0vX5-4RpJ2JZ98_NG0t3nrqTNPN_PvSL8W9GjAfOQTXQK6KELfRitOSioyIoUb_qFDVD1mn9ltQ0SPZY5AsyVmPlrOx5c7YQO63yOc8hMVGrtmLEE_ZGL5Tp59SjS4k094zrcQqZ_vuK37oZjRw4Uo5Q0id19SCxtjWYmjow4VXF_RhaojV_kyCBiUPG59RZw3yMpL-8REYRQWiS3sR7AzMoQCzjvejWLV0xMtoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از مهمان‌نوازی در مسیر اربعین
🔹
در یکی از موکب‌های عراقی، پسربچه‌ای تلفن همراه خود را گم می‌کند. خادمان موکب پس از اطلاع از ماجرا، با جمع‌آوری کمک از میان خود، برای او یک گوشی جدید تهیه می‌کنند تا ناراحتی‌اش را جبران کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/678858" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo_nU_ArG6CZyQyk12mX580Nga5wV8FgRT6-fRT9_R8esJ1EBlccdX411ZlowtSF_iFXE2LxlgXcEeik1Poz4umVFo0N5Yo15CukOAYX8z4CaZwRuFdSF0TrtFCOb5bKCJS6PNXcUsyW73QneGAZWqmLyIlWYv3iHMIg5LAEFnEVeoMIUsMVRLhPAm_aw1jf-G8y0ZJ_gDd91ngNjI61T1vRry1U_83F89vZNhM5QmARt6YTV1K18F4AJFVEfnFqX6SJzeYrfGu0R9pZaLX496RD6bTxnrxoihWNgVk9ti0-in9MFsPlmQGd5g7lkcKnuEOhTKkCaDQnxFd_gPQ3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مدیریت موج بازگشت سفرهای زائران اربعینی؛ هر ۴۰ ثانیه خروج یک اتوبوس از پایانه شهید رئیسی (برکت)
🔹
سخنگوی قرارگاه حمل‌ونقل اربعین حسینی سازمان راهداری و حمل‌ونقل جاده‌ای با اشاره به موج بازگشت زائران اربعین، گفت: هر ۴۰ ثانیه یک اتوبوس از پایانه شهید رئیسی (برکت) در مرز شهید سلیمانی (مهران) خارج می‌شود.
🔹
مهدی قلی‌زاد با اشاره به این‌که هر ساله در سفرهای اربعین یک موج رفت و یک موج بازگشت وجود دارد، بیان کرد: در سال جاری شرایط منطقه‌ای موجب تغییر الگوی سفرهای زائران شده و در مواقعی شاهد تداخل سفرهای رفت و برگشت زائران بودیم و این موضوع، مدیریت سفرها را دشوار می‌کرد.
🔹
وی از جابه‌جایی بیش از ۷۰ هزار زائر با استفاده از ناوگان حمل‌ونقل عمومی در مسیرهای بازگشت طی روز گذشته خبر داد و افزود: از این تعداد، ۵۱ هزار نفر از مرز شهید سلیمانی (مهران) به مبادی اولیه سفرها بازگشتند.
‌
🔗
لینک خبر:
https://rmto.ir/s/mfan7Jx
⬆️
با پیشنهاد به مجله از کانال راهبران ایران حمایت کنید
#اربعین_حسینی
#چشم_به_راهیم
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🌐
@cheshm_be_rahim</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/678857" target="_blank">📅 11:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بر بال وطن
🔹
پانزدهم مرداد، سی‌ونهمین سالروز پرواز آسمانی قهرمان ایران، عباس بابایی است. بابایی، نامی فراتر از یک قهرمان جنگی و اسطوره‌ای ماندگار در تاریخ ایران است.
🔹
او با نبوغ تاکتیکی خود سرنوشت نبردها را تغییر می‌داد و بزرگ‌ترین دارایی‌اش را ایمان خود می‌دانست. پرواز برای او نه یک شغل، که یک سیر و سلوک معنوی برای رسیدن به معبود بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/678855" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
حذف نام همسر سابق از شناسنامه ممکن است؟/ امکان حذف «زاده» و «پور» از نام‌خانوادگی
🔹
حذف نام همسر سابق موضوعی نیست که به‌صورت عمومی و برای همه افراد انجام شود، بلکه تابع شرایط و ضوابط تعیین‌شده در قوانین ثبت احوال است.
🔹
تغییر نام خانوادگی از جمله خدماتی است که در چارچوب مقررات ثبت احوال امکان‌پذیر است. افراد می‌توانند در شرایط مشخص، درخواست حذف پیشوند یا پسوند نام‌خانوادگی خود را ثبت کنند؛ برای مثال حذف برخی پسوندهای رایج مانند «زاده» یا «پور».
🔹
همچنین برخی پسوندها و پیشوندهای نام خانوادگی که نشان‌دهنده محل، شهر یا منطقه خاصی هستند، در صورت دارا بودن شرایط قانونی، امکان حذف دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/678854" target="_blank">📅 11:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEdqRQ4V_6938m_KBTVcqw9-O26AKra8ix1r-3CFnBBh8GNgoM-LDKwjPR1OZRpOaStYXQ6kqM2H3FWafOizc9oM1L3Ki2eiRFKDj5kNN52GAoY_NINBFBce_a8bHXCLI8Fj_gjcRihhtxXWkV55JtMmuHByHAeZtXQ9gfLSGJM2X08LMXNpBU6sdeob-923XV21QGyBrz71E5rQ7EOWdNfGIqkPRDIHoyztvPhat_pp02Qj2rGHq8Ro5Xzr8WZpzPE0dx_7VMeN-nKMLoPUHTWqDdpMpPNeF6tUZorqes_MjKXgkBZ6fvVMUxFLMxjAHTZVfcyx8FtoxHZkucuRvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موهای گاوی صورتی شد
🔹
گاوی قبل از جام جهانی قول داده بود که اگر اسپانیا قهرمان جام جهانی شود، موهایش را صورتی کند.
🔹
او در واکنش به این تغییر ظاهر گفت: من مردِ قولم هستم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/678853" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbwC0fb6HmEIxfmWsmmtua9demlBKCmcI-1tp1Y3bSW5HUcudSkit3_VeucrUZLlcl3yTjSEpsSUDxKbUpwu_3_sctKCMB5nyd6YSVGjXVwaDghN9Od6BNc2LwFOals8oARzCvxyVXA_wLCOw-R1Q-UHCJk1e1liUqh2M5me1-EJodqN2K6W27TS6tO_glZzKLslSBlnBYM3Q3lJYwcvfZn7LuXtZmSLreDAqa4vsZqMDwP4EqZUnRM2T4Hm6tykr6OzpgclGK-KfXna7CLo0n3j62CKYOaBX9SCLaJxMrAxXJt9Bo3vaw8548r-3pmEkkRSDsk3V8p6trRvgHEmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/678852" target="_blank">📅 11:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e666aa6e1.mp4?token=j5AU9zdQ-dtVZGByY1mpRNyUNSvi1_McwwIisMWCAPBBCtSd72r2IZRiPYV65UwlHo1biVUOwCofLI9VltCzVGQmgkLVLhoQIWk5Xxo7CWZzdipGzg1wDN4aY4N33KiSweNdoKnZO-nuhwP8gQk46Yk8tiRbhTw8a7TERNnz4zRQASH6g-Z2LpEA0fG7801LLqXac6JznIRWpcy-tv0jP8SfKNv6Qr-IlyKq5rOoCJk2GQt4Ga9YRkUChk_HdS35iCbsO_4w_1ejhCy8XAJohL_PuTw8EAgRFLxsQqbTl-XQa7vOW4SaJBQBUzgC98FnTJCFkm0cTIPeWLGonyptkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e666aa6e1.mp4?token=j5AU9zdQ-dtVZGByY1mpRNyUNSvi1_McwwIisMWCAPBBCtSd72r2IZRiPYV65UwlHo1biVUOwCofLI9VltCzVGQmgkLVLhoQIWk5Xxo7CWZzdipGzg1wDN4aY4N33KiSweNdoKnZO-nuhwP8gQk46Yk8tiRbhTw8a7TERNnz4zRQASH6g-Z2LpEA0fG7801LLqXac6JznIRWpcy-tv0jP8SfKNv6Qr-IlyKq5rOoCJk2GQt4Ga9YRkUChk_HdS35iCbsO_4w_1ejhCy8XAJohL_PuTw8EAgRFLxsQqbTl-XQa7vOW4SaJBQBUzgC98FnTJCFkm0cTIPeWLGonyptkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنباکسینگ نخستین گوشی رباتی دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/678851" target="_blank">📅 11:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز ایمپلنت دکتر دهقان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX9wAlBzbXuSRpMVUJfAtz032XXU60dR8z13P16biDWdDDfFqRmi_IM3ncl9YM5Y7P_GK20tYNODfW3ViFd6F_zaIx5NRJWFba8_TXBVbiXOUZDJH_xyUBsv3kfQwFRszWlfoQ0CaY53EeUZ9G3_NZml2YLFHGXtpB7zqKznztZnN2J_X4nPEUllsBexi7hZdWe6k-0fXq41FvX8VCBDEdxA6CxiejeUzR3KSNOL5eklObMl5rf4bZErfe-Lh1UUrrgPodQwOI3jvcKnukAl5GjJelTTQoLsLn-VYmB22IvLLh2io7Ce7Occ9PdArsDkYO4rGstHolyRLH1jSb0jEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
✨
وقتی قرار است ایمپلنت انجام دهید، فقط قیمت مهم نیست؛ اعتماد مهم‌تر است.
سال‌هاست بیماران، درمان خود را به مرکز تخصصی ایمپلنت ما می‌سپارند؛ جایی که تمام مراحل درمان، از بررسی اولیه تا پایان کار، در یک مجموعه تخصصی و مجهز انجام می‌شود.
⭐
درمان توسط تیم تخصصی جراحی فک و صورت
⭐
تمامی خدمات مورد نیاز در یک مرکز (رادیولوژی، جراحی و درمان)
⭐
امکان پرداخت اقساطی تا ۵ سال
اگر تا امروز هزینه درمان باعث شده ایمپلنت را به تعویق بیندازید، اکنون می‌توانید با شرایط پرداخت مناسب، درمان خود را آغاز کنید.
📞
مشاوره و تعیین وقت 02191003999
💬
ارتباط با ادمین
@aesthetic_center
📸
نمونه درمان‌ها
@drdehghan_implant</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/678850" target="_blank">📅 11:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIRlGRAwsY18H3K4mUgGLUOYDAbyIfGZtpqldrIQhOLuhs5gPpGnl76ulC2s0ITTd7QDU6RlFwOEOrCRBhvBX4_QMPQLxJ9gQsJNO36uYPnavJrFSIej87thiSp-aTk1BFvdVFXsFxKrD2E5mDpJ2ir88KCWhHfXBudPkaF7w4DMHiboEPBtZUMyk4kknbFDkEpagINvGbuHm8Odhw6TKVaiQOIlWleelfAAVB06-w8V84XO9YgBsO4F9WNzgmungaZSfzBlv7af-ZL7GKQGjC9XYI2ZKVctGR-7OORYnKrwHucdE7LpdkykP7Gscmnz2h8s0Am89A0DMEQT_7P8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه کریان جزیره قشم
🔹
صبا موسوی
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678848" target="_blank">📅 10:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
زمان‌بندی واریز کالابرگ
🔹
خانواده‌های تحت پوشش نهادی حمایتی و کد ملی با رقم پایانی: ۰ - ۱ - ۲ از ۱۵ مرداد(واریز شد)
🔹
کد ملی با رقم پایانی: ۳ - ۴ - ۵ - ۶ از ۲۵ مرداد
🔹
کد ملی با رقم پایانی: ۷ - ۸ - ۹ از ۵ شهریور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/678844" target="_blank">📅 10:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85eaa40b88.mp4?token=vT0zjkcFL0jfoM0Ugj63-TygdV-MMqIMUnEJz_dxLq_5NplgFxdTrPUSrIHWYLctQ1RSGnTCoHHXCpJv_7jFcQtemnM9UkFrZmgJeTVbpnqLkxboLPVoxm7EmFSFiLEsjjwfToFmhnA0LeI9xvyJTG-07hwPllTjK8TFFb2f7o28UJRZjsMb3ryH6ZPmyQVlZrunTrpggSXo0QECWmQCODvHQyfqbVuK1XtMhGtvEKfMytBMwX8SU0XS5LzYwH3ruG-OYhWGfJ4uF2F6p1s2uyUWxw6HghxCLFNyLK5bJi7MdqcIBrixh7jrltNJFyZN8uj_hnffRw6h9mBtcVyMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85eaa40b88.mp4?token=vT0zjkcFL0jfoM0Ugj63-TygdV-MMqIMUnEJz_dxLq_5NplgFxdTrPUSrIHWYLctQ1RSGnTCoHHXCpJv_7jFcQtemnM9UkFrZmgJeTVbpnqLkxboLPVoxm7EmFSFiLEsjjwfToFmhnA0LeI9xvyJTG-07hwPllTjK8TFFb2f7o28UJRZjsMb3ryH6ZPmyQVlZrunTrpggSXo0QECWmQCODvHQyfqbVuK1XtMhGtvEKfMytBMwX8SU0XS5LzYwH3ruG-OYhWGfJ4uF2F6p1s2uyUWxw6HghxCLFNyLK5bJi7MdqcIBrixh7jrltNJFyZN8uj_hnffRw6h9mBtcVyMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین عمامه‌پیچی سیدمحمد خاتمی
🔹
ویدئو: محمدعلی ابطحی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/678843" target="_blank">📅 10:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/678840" target="_blank">📅 10:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1c4c9803.mp4?token=vrkCl2hW3h9iOpTYzOLmvb018Q3jGaRjn_E3qjy0QxKN9L0KtmPocKklYPiOu_pDFVuZAe0bibuUvCdov3TjBVgV5ru57REaWzj1jzl2hTbCW1d3xd-fJCrrPvmvX9jkNMJDPdcBBX0d5gJbYPXOKQZ7rK_jl5CH0GxKRV22ZS6i22uBdq79nla5pqKce0_8DBNqaNzX_JPTgZ0ykFctxZMAVXT0WEZvdPp8MP_8ZtTuV4R0--7WPUCcx0c9jl6Mwfv_j_9XngcNlzW2m-ZbHagZau8qjGr5vuPJSvHnTSbGsC-zrSFQyUbJQHHkotSHl5HUcrrR4cCWdEMqYa0qYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1c4c9803.mp4?token=vrkCl2hW3h9iOpTYzOLmvb018Q3jGaRjn_E3qjy0QxKN9L0KtmPocKklYPiOu_pDFVuZAe0bibuUvCdov3TjBVgV5ru57REaWzj1jzl2hTbCW1d3xd-fJCrrPvmvX9jkNMJDPdcBBX0d5gJbYPXOKQZ7rK_jl5CH0GxKRV22ZS6i22uBdq79nla5pqKce0_8DBNqaNzX_JPTgZ0ykFctxZMAVXT0WEZvdPp8MP_8ZtTuV4R0--7WPUCcx0c9jl6Mwfv_j_9XngcNlzW2m-ZbHagZau8qjGr5vuPJSvHnTSbGsC-zrSFQyUbJQHHkotSHl5HUcrrR4cCWdEMqYa0qYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی با ۹۷ سال سن؛ یک سال بعد از سکته!
🔹
زن ۹۷ ساله‌ای با شکستن رکورد پیشین خود در کتاب رکوردهای گینس، بار دیگر عنوان مسن‌ترین زن «بال‌نورد» (Wing Walker) جهان را به دست آورد. او تنها یک سال پس از سکته مغزی، دوباره بر فراز هواپیما به اجرای این حرکت پرداخت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/678839" target="_blank">📅 10:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2a41fafb.mp4?token=pBA6BgoV5icps3l8HFSTxv98Bcccg1I12c8O2fvP0GihQhe-LcEjmKCyrjkmDBSfiHdvoRWL-uDm7kJZZ26tjcD5GzAR9vXnElO8dRn63GdHAwdSCQTfuNaxIPpBD2WI4_Efyu5EBXoi9ItVVZp0hyYY_YTfGRpELeHOfwvk7BcFdXs1MmTQ_6zNc4DQ92ywm0I2Un25It1LEwexiMFqLnoMXnkoFHEap79jEMHPyYqR3x0LhbwicwJfsF7LrigZPNSjbhQk2um9Ol_Dm4FI0QLkhrFGNMZ4oNU-ll0KERSFGsYVEKPtd1wKTL48JeOgWdgR3DiPOjwBAh4sPDKZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2a41fafb.mp4?token=pBA6BgoV5icps3l8HFSTxv98Bcccg1I12c8O2fvP0GihQhe-LcEjmKCyrjkmDBSfiHdvoRWL-uDm7kJZZ26tjcD5GzAR9vXnElO8dRn63GdHAwdSCQTfuNaxIPpBD2WI4_Efyu5EBXoi9ItVVZp0hyYY_YTfGRpELeHOfwvk7BcFdXs1MmTQ_6zNc4DQ92ywm0I2Un25It1LEwexiMFqLnoMXnkoFHEap79jEMHPyYqR3x0LhbwicwJfsF7LrigZPNSjbhQk2um9Ol_Dm4FI0QLkhrFGNMZ4oNU-ll0KERSFGsYVEKPtd1wKTL48JeOgWdgR3DiPOjwBAh4sPDKZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان یک یهودی برابر ۱۰ میلیون انسان؟!
🔹
از انکار «قوم برگزیده» تا اعتراف به قیمت‌گذاری جان انسان‌ها؛ تحلیلگر اسرائیلی فارسی‌زبان انکار می‌کند، وکیل اسرائیلی تأیید می‌کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/678838" target="_blank">📅 10:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1179852768.mp4?token=v1frfKjQo_6j0IfpY4r7kfVP0NK2sagDw_pNII3uPa-_ru7qnY8g_wC1Swo3efKOUpcWr9fgJeZeHCF4JhIqUhn_a-1kaOSrBXCy-rO_ItkV_CVz6zediRk1kFA0m-_QpXluQ6VQF_qwghtFHG2Wb12pbOEowIT61ZX5WWYA_MZ0NU6XIO9UqWZ7Ddk7u2UGkUY8yhevYX1T65gIgUoY5it9XtW8XQ0QY1zWSHcHUHVEPPCLJJ6IlBilGbN95fN0NA-tgnEbsGHkuV4G6d1nns9gawfIxoWnIryn7e50ojUYHJYhD_Kh24IMNjmpqXfD-O5T7uvz6mrmkG2cXskaH1tZfKE257ZbthXkBG2ewPstjWOk3UM1lSjTItiMJ-SCAV8XQqi27O_Wc3Wl4WUQ-JrmDj12mIew0sJvG9VjmiGAB6JpQO_2go-57coMuJrVWhzGmwXcZ5pJ5GRNbaB87VvVoiPvd4v0wbDwJRY-raHUsSHfTbjeYdscQxLrZUYZ-eTsgUuy3ycyglDHvzdZYE2qglwYLNJfyVafjjHFd_tg1poG4U45ruLFIV7W34-Bx3-4ke2Rtijb4bqzKPnN5L6gHgH4Pi5C1WyoeMMo4u3DAnHUhO4CeRqyR6vWmeOx2rM2Oi3Q6GLYQ_PX5TUH0-5p_COIsumd_8s6MIr_GcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1179852768.mp4?token=v1frfKjQo_6j0IfpY4r7kfVP0NK2sagDw_pNII3uPa-_ru7qnY8g_wC1Swo3efKOUpcWr9fgJeZeHCF4JhIqUhn_a-1kaOSrBXCy-rO_ItkV_CVz6zediRk1kFA0m-_QpXluQ6VQF_qwghtFHG2Wb12pbOEowIT61ZX5WWYA_MZ0NU6XIO9UqWZ7Ddk7u2UGkUY8yhevYX1T65gIgUoY5it9XtW8XQ0QY1zWSHcHUHVEPPCLJJ6IlBilGbN95fN0NA-tgnEbsGHkuV4G6d1nns9gawfIxoWnIryn7e50ojUYHJYhD_Kh24IMNjmpqXfD-O5T7uvz6mrmkG2cXskaH1tZfKE257ZbthXkBG2ewPstjWOk3UM1lSjTItiMJ-SCAV8XQqi27O_Wc3Wl4WUQ-JrmDj12mIew0sJvG9VjmiGAB6JpQO_2go-57coMuJrVWhzGmwXcZ5pJ5GRNbaB87VvVoiPvd4v0wbDwJRY-raHUsSHfTbjeYdscQxLrZUYZ-eTsgUuy3ycyglDHvzdZYE2qglwYLNJfyVafjjHFd_tg1poG4U45ruLFIV7W34-Bx3-4ke2Rtijb4bqzKPnN5L6gHgH4Pi5C1WyoeMMo4u3DAnHUhO4CeRqyR6vWmeOx2rM2Oi3Q6GLYQ_PX5TUH0-5p_COIsumd_8s6MIr_GcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیراشکی گوشتی رو به سبک انیمیشن سندباد درست کن
🌮
مواد لازم:
🔹
۴۰۰گرم گوشت چرخ‌کرده
🔹
۲عدد پیاز بزرگ
🔹
۲حبه سیر
🔹
نمک، فلفل، زردچوبه و دارچین
🔹
جعفری خردشده ۲قاشق غذاخوری
🔹
خمیرپیراشکی
🔹
زرده‌تخم‌مرغ #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/678836" target="_blank">📅 10:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475549b9ee.mp4?token=BLeQEs5ILUxwShmgR5JRwUMiGH_nSxwZLcOF2UTeuH0Ywc4OXIfsuaHyD6YpvoankgWyx2EZKL_AF2EGj_ZUvh12IAmsVgAnZ_cItwaVD5t1kUwrH1b8exS0npkb1bSCOoxA8vgMt-ZcL8hmORIZWLU8QBCZa-ub1QWbF3wr_fyq2stNluVWrVtHYj3cIKNCU_7dBv4tOprjJQDXVzijOgB0Cb7ohJ8-UYtYXFJiytSKndV5h_hTlIn65hIm-4Z4k-NL2V6Q4J2zaEAL90uQM7hFxsksHm6rhZuMsp_SNikY-M_xB7X-BiQOmSz8X-6TEJeWjvM-XNVDnkfcIrkHzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475549b9ee.mp4?token=BLeQEs5ILUxwShmgR5JRwUMiGH_nSxwZLcOF2UTeuH0Ywc4OXIfsuaHyD6YpvoankgWyx2EZKL_AF2EGj_ZUvh12IAmsVgAnZ_cItwaVD5t1kUwrH1b8exS0npkb1bSCOoxA8vgMt-ZcL8hmORIZWLU8QBCZa-ub1QWbF3wr_fyq2stNluVWrVtHYj3cIKNCU_7dBv4tOprjJQDXVzijOgB0Cb7ohJ8-UYtYXFJiytSKndV5h_hTlIn65hIm-4Z4k-NL2V6Q4J2zaEAL90uQM7hFxsksHm6rhZuMsp_SNikY-M_xB7X-BiQOmSz8X-6TEJeWjvM-XNVDnkfcIrkHzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاشی که فراتر از وظیفه بود؛ پرستاری که باور داشت هنوز امیدی هست... و تا آخرین لحظه جنگید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/678832" target="_blank">📅 09:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/678830" target="_blank">📅 09:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d149c218.mp4?token=o1cQEp3v0NH3qpaP6-NMe88uaWVN2R-6sirB9lMcF9jfA39iSOufdM-74Ct19OdmagioGuVRZhWGFzYT9JMoTuYsDhaJy_70vriMUSEtx0d2LaKMsfeeI7rY36yd0KMGHAATV5nLy3UrJHtzD42mYegJDX-z-EdJukJuZ2on2ySfcbitim4xabaaXgeD_gR6-S6qmll45rKbQoUdVsKfnHlWx-akRlZ8rDAYrcaqAzvZGEDFkCv7Ub5FRGClU_hdmL5wXdHArDlzH8sUrmRnFiG_OT_GmvM_Y0QT3pH00Pr5BEcXGThAoNfWk3eTCrpdHsin_5LoxGXMiq31xesUtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d149c218.mp4?token=o1cQEp3v0NH3qpaP6-NMe88uaWVN2R-6sirB9lMcF9jfA39iSOufdM-74Ct19OdmagioGuVRZhWGFzYT9JMoTuYsDhaJy_70vriMUSEtx0d2LaKMsfeeI7rY36yd0KMGHAATV5nLy3UrJHtzD42mYegJDX-z-EdJukJuZ2on2ySfcbitim4xabaaXgeD_gR6-S6qmll45rKbQoUdVsKfnHlWx-akRlZ8rDAYrcaqAzvZGEDFkCv7Ub5FRGClU_hdmL5wXdHArDlzH8sUrmRnFiG_OT_GmvM_Y0QT3pH00Pr5BEcXGThAoNfWk3eTCrpdHsin_5LoxGXMiq31xesUtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمدی ترامپ شیاد در لاس‌وگاس: کودکی که طعمه سیاسی شد!
🔹
دونالد ترامپ در تجمع انتخاباتی لاس‌وگاس، با تمسخر جو بایدن، مانع خروج یک کودک از صحنه شد و گفت «نمی‌خواهم مثل بایدن از روی سن بیفتد» که با خنده حامیان همراه شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/678829" target="_blank">📅 09:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGZ3lPdj2m8OTu9m9OGZL6fg7UKrBFfAGwi4ZfKxQX3t5XzSFQ2BNnUw7xY1rK1CAAj1r4CQqZJwlVenS5q6qPS1rGC7XNwjb0LAVxZgtULAvNiu46N2xHb8v4KBSiafQzlKd801k3pU-uWGKikFcwMbslTu2AJ4JFr-vk3LD2rS1TRY-0umC_Msc-iINLZHm3rCINPU9tioYCrxZjP1ntuU7Jn9tQTiNtgR095D0Zg9mE-5T3vTMkIQdgbWAP3_Mj1YWga2K84dzCB83dTwhELsd6bUfFzQDBRx9uo-1IyCU6XFkyNgKKBLpYFXyKeDKSfmBkVpAcvcRX0lW1Oc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس کنایه‌آمیزی که حساب کاربری وزارت خارجه ایران در بوسنی پست کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/678828" target="_blank">📅 09:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gedyLcKWJslgh7_GyeLdFAt06NjQD8urepy_Wjxs2ZMmtF5dF2C-XOQwFbPI6ZkOObD1WubBO-DUlO8Cts1lcQcPvVdd5y4kZOpDp8cBdMz6Z0KBdLapVVKS39p9BRGWV-g8Xpv-9t6cHovFMmNlbHx_iD7eER32iAjGWP4y5XYaDwQIjNFaxGWI0Ph_2Wgp3xzSwRlgNJUgoeTgtr1gqYHWKBhQfOxv9Dfz41MqMVqpoS9Z12Z18vY08-npYxx5uSEV46iPQYod2vgBJXpfp3Gtc3mQ8gducQweA7Gsi7SHq4kU16gLasw19oCkG0RDqOoMBwyo8qMYCEMjDyX_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تویوتا برترین خودروساز جهان از نگاه کانسومر ریپورتس شد
🔹
سوبارو و لکسوس (Lexus) نیز رده‌های بعدی این فهرست را به تصاحب رسیدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/678827" target="_blank">📅 09:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1c1e934f.mp4?token=L-TeP0U6VeY9WYbOsmv9FCVM_AfMzO2z84vcG69eYgmOXSRW36fkOC63jU51IC1iziud8EziPD9FKHLpKUpLSoD1YtAI-0Pc9t2Nt1p9TR5j9PdelxVz9FjKuDHmzs-0thvbRxJG-57vsVJhpCc8kAD9awyevJCWu28QGV4YldAyJh6UHETKE4xhGepWe3ZAagXKBZOI9d4-BQvQPXGODTEmLEaU2eQMBGhCYsNf0Ou37qu0AP_K5eesK_hg7DUyHB9bnzZoWL45XB_YKIXgbzjT0OyS164frSpGstwnZdZucP4hGtAfObkqoqxDdjBp3E39C28VoXF_Wi3flMlr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1c1e934f.mp4?token=L-TeP0U6VeY9WYbOsmv9FCVM_AfMzO2z84vcG69eYgmOXSRW36fkOC63jU51IC1iziud8EziPD9FKHLpKUpLSoD1YtAI-0Pc9t2Nt1p9TR5j9PdelxVz9FjKuDHmzs-0thvbRxJG-57vsVJhpCc8kAD9awyevJCWu28QGV4YldAyJh6UHETKE4xhGepWe3ZAagXKBZOI9d4-BQvQPXGODTEmLEaU2eQMBGhCYsNf0Ou37qu0AP_K5eesK_hg7DUyHB9bnzZoWL45XB_YKIXgbzjT0OyS164frSpGstwnZdZucP4hGtAfObkqoqxDdjBp3E39C28VoXF_Wi3flMlr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این حرکات بازوهای سفت و خوش فرم، سرشانه‌های صاف و ایده‌ال، پشت بدون چربی و زیبا در خونه بساز! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/678823" target="_blank">📅 08:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df107556f6.mp4?token=AfPTI2IMHFpjQz-beEbycR_W4SAipgmSQTt8jXbBxqVyLug7mWokHpxuPzHNJsuYbzb3-mazAjY93DgzusQqCXn8LL-sNtPvOxQCErsX6_5rA4Ru0b0rYPYX5o5jo0d1tQaCUuwRGoOmN7M42ZIITgKodgs2Ce90Ah92UKT35ofSM7CNOfhI87k2wVTWnAy-ZLzL_gtLFoNOvAVLrRq3B3K38kbw2lzA567TVFvZ6ugMR09r4PvRghDLIk69aMrsQaK3iOfeiMJq-YKvbFMeWa3eafQLm_7LchJhYibTbE7G9U03Cc92L8N3QVqKfCqQK9NlmvwxNe-uf8SX-Ltb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df107556f6.mp4?token=AfPTI2IMHFpjQz-beEbycR_W4SAipgmSQTt8jXbBxqVyLug7mWokHpxuPzHNJsuYbzb3-mazAjY93DgzusQqCXn8LL-sNtPvOxQCErsX6_5rA4Ru0b0rYPYX5o5jo0d1tQaCUuwRGoOmN7M42ZIITgKodgs2Ce90Ah92UKT35ofSM7CNOfhI87k2wVTWnAy-ZLzL_gtLFoNOvAVLrRq3B3K38kbw2lzA567TVFvZ6ugMR09r4PvRghDLIk69aMrsQaK3iOfeiMJq-YKvbFMeWa3eafQLm_7LchJhYibTbE7G9U03Cc92L8N3QVqKfCqQK9NlmvwxNe-uf8SX-Ltb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی که یک انفجار مشکوک رخ داد
🔹
۶ سال پیش، "انفجار بیروت" که یکی از قدرتمندترین انفجارهای غیرهسته‌ای مصنوعی در تاریخ محسوب می‌شود، اتفاق افتاد. این انفجار معادل حدود ۱.۱ کیلوتن تی‌ان‌تی بود و زلزله‌ای با قدرت ۳.۳ ریشتر ایجاد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/678822" target="_blank">📅 08:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
صبح ها خرما بخورید!
🔹
کسی که با معده خالی خرما می خورد، کمتر دچار کم‌خونی می شود و بدنی مقاوم در برابر بیماری‌ها خواهد داشت، خرما با افزایش سوخت و ساز بدن باعث لاغری نیز می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/678819" target="_blank">📅 07:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad59116b2d.mp4?token=rNIXrdrJWf5FIs4aTfk5CgB5R4Civ6Wo8T-Hob24-ZHFVvoakYVcF9UFY7wO5LTDbYdv857WUtQ9ebWYbt-mbwOYgC8eL9osY-S5AQ-UzIbAzSve5GKDbof4Il_hAf1M76DDE6sSKSD2_Whze_GW4pYbHr-fP4U4OaBxJsUqfeu-0fK_84B9J6r0nypIisLC5XnBwouvm8x_vfS3s1F-67uLEmlPjUh9xcgJJfxXrS8q00Nd4TCGx0HhtAuGUXPEh28K4hZQ1k5-mn-nBX7H7NKrOwKDcbKCoKnewl5FblSO0arL_n9RjjKqbSmNre8xGNiCHXGzaxqlyb3ETHAiVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad59116b2d.mp4?token=rNIXrdrJWf5FIs4aTfk5CgB5R4Civ6Wo8T-Hob24-ZHFVvoakYVcF9UFY7wO5LTDbYdv857WUtQ9ebWYbt-mbwOYgC8eL9osY-S5AQ-UzIbAzSve5GKDbof4Il_hAf1M76DDE6sSKSD2_Whze_GW4pYbHr-fP4U4OaBxJsUqfeu-0fK_84B9J6r0nypIisLC5XnBwouvm8x_vfS3s1F-67uLEmlPjUh9xcgJJfxXrS8q00Nd4TCGx0HhtAuGUXPEh28K4hZQ1k5-mn-nBX7H7NKrOwKDcbKCoKnewl5FblSO0arL_n9RjjKqbSmNre8xGNiCHXGzaxqlyb3ETHAiVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: تنگه هرمز قبل از جنگ باز بود؛ ترامپ حالا ادعای قهرمانی برای بازگشایی آن را دارد!
🔹
ترامپ می‌خواهد خرابی‌هایی را بر‌طرف کند که خودش به بار آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/678818" target="_blank">📅 07:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuoGwDIzuLJjwy432l0GxNIt0r06MUzZSZygsCVJtiq4DWV3MZZtECtR7UMj3x2dzVWyEpBOtg1HnGNMj_en69BJMM8CcdEiP5kqpngfv0--FrwKAcyv9aKd4fq5TSmpPwbcbsujRq41XaQmvM1VxCpEzfQFk4rzguI5OmFinUKdc8P0J9EBg-S6rTPnSORHkwkrfbFhcDqQUyhTjQCw1_59wIk7YTmFzw39qJceBBdRauWa9Ha5GIeJ2H1kO_Gqq05PZCcK_w5-pfPc4f8Fwo7XaHUdoxMPgkjf3XBGMQgjdL580VXAwkqkp5DzuAIwwatbufwbS-bis1QlYfbbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۵ مرداد ماه
۲۲ صفر ۱۴۴۸
۶ آگوست ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/678817" target="_blank">📅 07:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کالابرگ سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲ شارژ شد
🔹
دریای مازندران فعلا تا ۱۶ مرداد مواج و تعطیل است.
🔹
ارتش اسرائیل: دو نظامی دیگر در درگیری‌های جنوب لبنان کشته شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/678816" target="_blank">📅 06:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A71rfUUVB4_xqcxQw5LSu3bfZBfcze9SoJxsdxvjeKa_4VTovDt0wzjDQ0bQXyhVcPfT3IKvBafX5fA4YSsGmolqGaN8bp2QzVe1fXrpW8k9Cm6kGiX6hWR2d8TC5LQGLx0a4ceqkgla1OdWvBqIkkfCs59VpleaE9ffSQ8yGsRuXCZEus9nl5i_S7bc6wMSnZyU2KUVf48QvbODJTHXsUGCFnKFfm_PPFiB78qWs1Y-8FyftS4r_FlzFC6n_EmRJSV6t6fq-Y8l7xEYsxJLrG55tsXOYLCAiP840I7oPXYXUvnYp9uzdQxTIANRsDGPT-Pq8XuMFePVuQLyCJpVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رفقا، برای اعتباربخشی به یک کار پژوهشی نیاز به تعدادی پاسخنامه داریم
🙏
🗳
تو این نظرسنجی میخوایم درباره تجربه شما از برنامه‌ها، تبلیغات و فعالیت‌های
مرتبط با جام جهانی
بدونیم و بیشتر از چند دقیقه وقتتون رو نمی‌گیریم.
پاسخ
صحیح یا غلطی
وجود نداره و منظور ما فقط
نظر و تجربه شخصی
شماست و
هیچ اطلاعات شخصی از شما گرفته نمی‌شه.
لینک پرسشنامه
لینک پرسشنامه
ممنون از کمک بزرگی که به ما می‌کنید
🌸</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/678814" target="_blank">📅 04:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678812">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
واشینگتن پست به نقل از مقام‌های آگاه: نارضایتی ترامپ از وزیر جنگ خود شدت یافته /چرا که هگست از حامیان اصلی اقدام نظامی علیه ایران به شمار می‌رفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/678812" target="_blank">📅 03:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ونس: ایرانی‌ها سرسخت هستند و نظام این کشور دچار شکاف شده/ وظیفه ما دستیابی به بهترین نتایج برای مردم آمریکاست
🔹
قیمت‌های انرژی کاهش خواهد یافت و ایران به سلاح هسته‌ای دست نخواهد یافت/ ایالات متحده در موضع قدرتمندتری قرار خواهد گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/678807" target="_blank">📅 03:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678800">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bddc34601.mp4?token=Txx7OK8gGdyN84tQmOcQdJdoJa6i0lteB9WYx6UiFFTmI0ZOqiFtH-i4r3dVbp171Fyk6gJw3wbLr5-MOzgrjW-NUtt6PBXqXnUOHzM7figYrsIqs-sZ23jqH9hOeqxRVJncReehD4gDPimj5nnfa57wQU6lDk6IcNaPnFNtykElywcVzMpwEScjjhe13e_K9fMNHGfcdbhjYpwixnZ66MF0mFZcGUU8uWnlf7bWkovhMwv0ZoFWYz4P4AK-yf8su1ieIduxj6FSlc7IHnmC78lGaMkuIbXiPypDkgiNPgugAd9kiufgh3jwrvFvYvp0X_nLQKkRiN4RSuxIVg3kzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bddc34601.mp4?token=Txx7OK8gGdyN84tQmOcQdJdoJa6i0lteB9WYx6UiFFTmI0ZOqiFtH-i4r3dVbp171Fyk6gJw3wbLr5-MOzgrjW-NUtt6PBXqXnUOHzM7figYrsIqs-sZ23jqH9hOeqxRVJncReehD4gDPimj5nnfa57wQU6lDk6IcNaPnFNtykElywcVzMpwEScjjhe13e_K9fMNHGfcdbhjYpwixnZ66MF0mFZcGUU8uWnlf7bWkovhMwv0ZoFWYz4P4AK-yf8su1ieIduxj6FSlc7IHnmC78lGaMkuIbXiPypDkgiNPgugAd9kiufgh3jwrvFvYvp0X_nLQKkRiN4RSuxIVg3kzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار درباره ایران: وقتی این موضوع را تمام کنیم، قیمت نفت و بنزین به شدت کاهش می یابد و در مدت کوتاهی به چیزی شبیه به معجزه دست خواهیم یافت
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/akhbarefori/678800" target="_blank">📅 02:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678797">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da3608a66.mp4?token=cYxB2CLrhNq93fEGQw36Lu3hLUhifE9bFpp7avDrKmW_pStrRAcoYdJqhR8ggzZBm5e971Vqg56uYZkEnCtPM0oe7b5g65pD96kr4MS1EjCTX47QcVPp3AAaxMKxOuhVvk_t6Nzvz-uBGtPoy7FyvL789xLUaQg8k5rgE8gizgxg7YG6kUoqqSDk106uq5rWMdxnNaOBsBUBSYTBFtFPyyuRPG_rAMo2PC0x9GG9i0M2A7WXMaFC5qP-ncOTgnGyLsjuSMIXmOKXdC5CGXvFZe1ZLW_EfvBS4A05ouUd6CBvlK-vKNU935uV80nuVybLEDvWBIakCRZjA4g_crwsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da3608a66.mp4?token=cYxB2CLrhNq93fEGQw36Lu3hLUhifE9bFpp7avDrKmW_pStrRAcoYdJqhR8ggzZBm5e971Vqg56uYZkEnCtPM0oe7b5g65pD96kr4MS1EjCTX47QcVPp3AAaxMKxOuhVvk_t6Nzvz-uBGtPoy7FyvL789xLUaQg8k5rgE8gizgxg7YG6kUoqqSDk106uq5rWMdxnNaOBsBUBSYTBFtFPyyuRPG_rAMo2PC0x9GG9i0M2A7WXMaFC5qP-ncOTgnGyLsjuSMIXmOKXdC5CGXvFZe1ZLW_EfvBS4A05ouUd6CBvlK-vKNU935uV80nuVybLEDvWBIakCRZjA4g_crwsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: ما در حال آماده شدن برای بزرگترین حمله از زمان جنگ جهانی دوم بودیم، اما ایرانی‌ها از من خواستند که مذاکره کند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/678797" target="_blank">📅 01:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKvBkjWpl9knKloyQjQkd_XuG9PRb5403snUTHfjgvBb_AWsDaif4haf6J3zuPfH8XbhvJzQ6deYJJgEkSh-i2mL5v24T0NfYa189ufT3ozt6D8BhCn9Nh0igk0-HOEfRntTAGZ1eWwb_p384JiFNcQPwyrV4MFFJDX863_Y5RWBye89QQoxTYGiOlO8uTy8nO6DQ7dSDZV24evJixC-qEJPtMUAaNv37X1x_HM5cVKv8iaeZ9rRJo5o6DA6G0EnT8cnPdjhzjjYa8U4-Lsz_kIeSBn3ZWkbR_HvIqvUEczIMBe25o2OfRlBkxTFtijDMCiBImGMaXNrg1YDKvN5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرار غول‌های فناوری از خاورمیانه
سی‌ان‌ان:
🔹
جنگ علیه ایران برخلاف انتظار، فقط بازار انرژی را تحت تأثیر قرار نداده، بلکه امنیت سرمایه‌گذاری در مهم‌ترین صنعت آینده جهان یعنی هوش مصنوعی را نیز متزلزل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/678793" target="_blank">📅 01:26 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
