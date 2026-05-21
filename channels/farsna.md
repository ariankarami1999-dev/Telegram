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
<img src="https://cdn4.telesco.pe/file/jdzCdD02teaWhRXvzO-fYHEIUryDHlMNHyGLTXPzQzLrRHZUHl_h3Sg4DcrvBspnFYid0eZdaO1Xya59d7liD2krMN9SIkSWVli7GcJIXGL-LCLGZXIpvcjwgDJjz3TvnuQEJsFtmq72Kd46nM35NnlKlm3UPpxK3h8HM1HTvuMBFHThm-TIMIzEnedWLguZw2gNFeWcDi8c_FoOa4S53KmcBkBHtLSaBR74_4NhIAeSPzgL316oF5NB1esjpz1NY9QKxurZZxq_0X1dlzESUWsfMaHwoEJlMZAXS_txbkBdXTeF-b3HS_ImtTlyvjJL15kmZWCqgBfrVwL-7165OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 03:03:07</div>
<hr>

<div class="tg-post" id="msg-437151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
حماسۀ ۸۲ دامغانی‌ها در میدان دفاع ملی
@Farsna</div>
<div class="tg-footer">👁️ 172 · <a href="https://t.me/farsna/437151" target="_blank">📅 03:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تعویق رأی‌گیری دربارۀ اختیارات جنگی ترامپ در مجلس نمایندگان
🔹
مجلس نمایندگان آمریکا رأی‌گیری دربارۀ قطعنامۀ موسوم به «اختیارات جنگی» را به تعویق انداخت.
🔹
این قطعنامه را اعضای دموکرات این مجلس با هدف محدود کردن اختیارات دونالد ترامپ در جنگ علیه ایران پیشنهاد داده‌اند.
🔹
نشریۀ هیل نوشته به نظر می‌رسد رهبران جمهوری‌خواه در این مجلس این رأی‌گیری را به‌دلیل به‌حد نصاب نرسیدن شمار نمایندگان حاضر خود عقب انداخته‌اند.
🔹
اگرچه اعضای جمهوری‌خواه در مجلس نمایندگان هفتۀ گذشته توانسته بودند قطعنامۀ مشابهی را با اختلافی بسیار اندک رد کنند، اما روند تحولات در کنگره نشان از شکاف در بدنۀ حزب حاکم دارد.
@Farsna</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/farsna/437150" target="_blank">📅 02:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هشدار بلومبرگ؛ احتمال رکود بزرگ در نتیجۀ بسته‌ماندن تنگۀ هرمز
🔹
بلومبرگ به نقل از مؤسسۀ انرژی راپیدان هشدار داد تداوم وضعیت تنگۀ هرمز تا ماه اوت (مردادماه)، خطر وقوع یک رکود اقتصادی ویرانگر در سطح جهان را به‌شدت افزایش می‌دهد.
🔹
رکودی که ابعاد و قدرت تخریب آن می‌تواند با بحران مالی بزرگ سال ۲۰۰۸ میلادی برابری کند.
@Farsna</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/437149" target="_blank">📅 02:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437148">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpgjdt_F90jTlirAp9g9M2yGkEye6NwGcFoHwhoiMDqReMo64tMyLOP70OTAI1jywMgLkzK1uE2tzQ_AXPIC4oRggVjLOmj-9OAcRukSt8lz-lmmDNbhEW3HwYtz_bx526cNiA8pg0Gc30G1g-HSfISdTKDDyt7NVEiXmpI7JX-ZU0_F2FSqzOCBcn4tAuQeTpH08pMxNUOdaMlkYYcjiVbKOHBaQ09Pty8ITW11elGaSmJc6Gjqr8mbP1xYO51przYlgoqFrm1Ntn9jc2noST45n7p-jAWOfzxGoNS5hK2Rp3ag0uiudQ2C46K9Dpoii5g-KCXu-7EVxrBRrDcWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان موقت استفاده از کارت‌سوخت اضطراری در جایگاه‌های هرمزگان
🔹
فرماندار بندرعباس: از بامداد یکم خرداد به مدت ۱۰ روز کارت‌های سوخت اضطراری جایگاه‌ها جمع آوری می‌شود.
🔹
در این مدت شرکت پخش فرآورد‌های نفتی نسبت به فعال‌سازی سیستم پایش تصویری و پلاک‌خوان در جایگاه‌ها اقدام خواهد کرد.
🔹
دوجایگاه برای خودروهای اداری یا فاقد کارت‌سوخت در نظر گرفته شده است. اما وسایل نقلیۀ فاقد کارت‌سوخت باید برای صدور کارت اقدام کنند، که ۴۸ ساعته صادر خواهد شد.
🔗
جزئیات کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/farsna/437148" target="_blank">📅 02:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437147">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
بندرعباسی‌ها در ساحل خلیج‌فارس هشتادودومین شب اقتدار ملی را حماسه‌ساز کردند
@Farsna</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/437147" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437146">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
مداحی جدید مهدی رسولی برای میدان
🔸
میدان خداقوت، خیابان خداقوت
🔸
جمهوری‌اسلامی‌ایران خداقوت
🔹
خودش را دیده سلطان زمانه؟
🔹
تو برگردی ازاینجا فاتحانه؟
🔹
شتر در خواب بیند پنبه‌دانه!
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/437146" target="_blank">📅 01:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437145">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
۱:۲۰ | حاج قاسم سلیمانی: در حرکت امام حسین(ع) از صحرای عرفات تا گودی قتلگاه، اصول و هدف سیدالشهداء هیچ تغییری نکرد
@Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/437145" target="_blank">📅 01:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437144">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملات هوایی رژیم‌صهیونیستی به جنوب لبنان
🔹
خبرنگار المیادین در جنوب لبنان گزارش داد جنگنده‌های اسرائیلی مناطق «زوطر»، «کفرا» و «حناویه» را بمباران کرده‌اند.
🔹
هنوز جزئیاتی دربارۀ تلفات و خسارت‌های احتمالی این حملات منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/437144" target="_blank">📅 01:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437143">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGFv3lG38-6rg0x1UHuI4uYerOiLJtkFgx9zovkDQaWuQwFnqV7NTtJqZMeWCUDtuFSCWDLPbLvG0fqo8lMWqXkzrDZuAfPQXTU8exNOFtl-ZlO0GBhtTydgJq0SOeO_yg9wp6qu3DXNCGi9YCIqWgLql9jzNVAw2zPMQPXRJaVeSRDoVihwR5F7EcF3ZkoAruHbAhb3omGivWi-UHqxoDiNFirVY44J1FRlyw_DJwas5ghZjEAYA1nQY4xchiBKOqCRyH9MTzszUPJfmTivuQpW7X7Wxk9sKMMr6XaBnE3vxfBgj98Mz5Hninux2KNSbHRgxyujNxbvqoDR7mehnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصد آمریکا برای اعزام نظامی به لهستان؛ پاداش به ورشو پس از تنبیه برلین
🔹
دونالد ترامپ، رئیس‌جمهور ایالات متحده با انتشار پیامی در «تروث سوشال» اعلام کرد که مایل است ۵,۰۰۰ سرباز آمریکایی دیگر به کشور لهستان اعزام کند.
🔹
او به جزئیات بیشتری از جمله زمان دقیق اعزام نیروها و اینکه آنها از کدام پایگاه‌ها منتقل خواهند شد، اشاره‌ای نکرد.
🔹
ترامپ دلیل این تصمیم را روابط بسیار خوب و نزدیک خود با «کارول ناوروکی»، رئیس‌جمهور راست‌گرای محافظه‌کار لهستان، عنوان کرد.
🔹
ناوروکی که در اواسط سال ۲۰۲۵ در دور دوم انتخابات ریاست‌جمهوری لهستان پیروز شد، پاییز گذشته در دفتر بیضی کاخ سفید با ترامپ دیدار کرد.
🔹
حدود سه هفته پیش وزیر دفاع آمریکا دستور خروج حدود ۵,۰۰۰ سرباز آمریکایی از خاک آلمان را صادر کرد؛ تصمیمی که پس از انتقادات تند «فریدریش مرتس»، صدراعظم آلمان، از اقدامات نظامی و سیاست‌های ترامپ در قبال جنگ ایران اتخاذ شد.
🔹
بلافاصله پس از تنبیه انضباطی برلین توسط کاخ سفید، دولت لهستان آمادگی خود را برای پذیرش این سربازان رانده‌شده از آلمان اعلام کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/437143" target="_blank">📅 01:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437141">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f0cd0b59.mp4?token=b_TuLZcNMxeRHaDYFTOtjxxJ7Yz6ZryqWMtCVTK8DEozVIxwFfWuaJISDA4uO4IwAjLsbi9jzOzj_fLwMEfcjgN0_keMuibTE9opeVBY8N5Woxu96WbO72piSMNzsOJskDlzVDJTnz1ODyp_NCcbHic80svbQCyUuaJ0d-J4bYR5-NLP-0tfPgKIZSO2AjfVhjE2eoaA2CFOB2tnOxY5fezIR_M_dm74gud_T9zyKQNnUD3ae-HzLledL4Gn3Bf7QE0Puwnkjj8qGnCWVO5QxikBvLxR-y6B46T_yw-8N-G54vbe187Vt92pbqb1uag7DQWxxcu-it8U5kYkma20noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f0cd0b59.mp4?token=b_TuLZcNMxeRHaDYFTOtjxxJ7Yz6ZryqWMtCVTK8DEozVIxwFfWuaJISDA4uO4IwAjLsbi9jzOzj_fLwMEfcjgN0_keMuibTE9opeVBY8N5Woxu96WbO72piSMNzsOJskDlzVDJTnz1ODyp_NCcbHic80svbQCyUuaJ0d-J4bYR5-NLP-0tfPgKIZSO2AjfVhjE2eoaA2CFOB2tnOxY5fezIR_M_dm74gud_T9zyKQNnUD3ae-HzLledL4Gn3Bf7QE0Puwnkjj8qGnCWVO5QxikBvLxR-y6B46T_yw-8N-G54vbe187Vt92pbqb1uag7DQWxxcu-it8U5kYkma20noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری کرمانی‌ها به شب ۸۲ رسید
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/437141" target="_blank">📅 00:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437140">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiiDun9y4EL9oXvT8cNffH_OVzf5sMjbZbEJ3wnjs8E2dCV0Bqvcol81w49s5SDZXR7wUuLB1OWhULBS10vEdQgISP2Wdx1ab1-f9i0xPwukl11RRoci9dLSJEFKANYlZ6K358Q-aDOzOpfVj47aWjW9KEGkZaJ-hSlm5LM7Ja299rUdrS1jQHhbp0g-NHLtdBke1RlLPb3reENXnWOO5ESRFwyo3rPOLassRXM0DbNTMQIJLbDtKCZaLCrYfqyiCShJE3rObgyincV7adGWnUqUsCtySvANcxPTbWb2gcEpKd388MlhaiQPXqIFIooZyoyjy8ec0yCxsrTLdZbocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان‌: ترامپ شکست مقابل ایران را در کوبا تلافی می‌کند
🔹
سی‌ان‌ان، صدور کیفرخواست علیه رائول کاسترو، رئیس‌جمهور پیشین کوبا را تلاشی از سوی ترامپ برای جبران شکست در پیگیری براندازی در ایران توصیف کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437140" target="_blank">📅 00:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKZwVSUwQ5Ci2vlrPqLrJCjem9c3NXkNKTX_RB_n6WqSVOLsD2PKqk2TfrMR-Y0vlyGTFW_Ocmj0tJgrhloiKoJseoSznp6O139aNbZzHRNVuZJYd2tHIn1qPNPRQLlQpcgR8OQIBcPOFq4TAnfD51ZXYVK9gNzQ2zzCfFVl3FbU8GbhaGEaREH9EZLfHd7KfxiwqxsggQkH7rZvNQGSJpcFWthQdAqDO1nhrl0dQYMmop-tZpEegUo71bY7zHPLkwFLHfyY1oU0TKSVLyuby4wIjzeMbnqlK4MmqFwzoc9LKZbTR3355J0cxut6zLR7diwTmkelllJ1mxc8kIQzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریز به سایهٔ تقدیر
🔹
روزی شخصی پریشان و رنگ‌پریده به درگاه حضرت سلیمان(ع) پناه برد. سلیمان از او پرسید: «ای مرد، چرا چنین هراسانی؟ چه بر سرت آمده است؟»
🔹
آن مرد با لرز گفت: «در راه، ملک‌الموت را دیدم که با خشمی عجیب و نگاهی تند به من می‌نگریست؛ گویی قصدِ جانم را داشت. ای پیامبر خدا، تو بر باد فرمان‌روایی؛ از تو خواهش می‌کنم به باد دستور دهی مرا به دورترین نقطه در هند ببرد تا شاید از چنگال مرگ رهایی یابم.»
🔹
سلیمان دلش بر او سوخت و به باد فرمان داد تا مرد را بی‌درنگ به اعماق سرزمین هند ببرد.
🔹
مدتی بعد، سلیمان(ع) فرشتهٔ مرگ را دید و از او پرسید: «چرا آن روز به آن بندهٔ خدا با خشم و غضب نگریستی که چنان هراسان شد؟»
🔹
عزرائیل پاسخ داد: «ای سلیمان، نگاه من از سرِ خشم نبود، بلکه از روی تعجب و شگفتی بود! خداوند به من فرمان داده بود که جانِ آن مرد را در همین ساعت در خاک هند قبض کنم. وقتی او را اینجا دیدم، با خود گفتم اگر او ۱۰۰ سال هم بدود، به هند نمی‌رسد؛ پس چگونه مأموریتم را انجام دهم؟ اما وقتی به هند رفتم، او را همان‌جا یافتم که به پای خود آمده بود و در زمانِ مقرر، جانش را گرفتم!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/437138" target="_blank">📅 00:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVUJdXaq6tmAw0TDL9XqWtm_r2A5fGNCVaAg3g1RfSLhL1NEgMwkG-f_xlz36AU0oomJlUp27jiJMUupLvjhIkA9uxIm0FXq4HfVbV7S-mblnzTFf94vuI6L3jKRLBqJIS3goem74__ih-1M8e0XbDIuurDXSTGblwsmUWG407CPOpD7z5BECtoVd5xLLxYsA1wGxMXxl-tXGI5rmesa6bRbeoqn3k25Qua1hjji8xktPQAX98YEaA8b-NTINSeWIl9veUVytpCu3PicCb6ehkEXWYjbBGn4ApeL4GTluH_Q6SLhJWpoYejNC7il9DotRQO0iqafKT1OSM9KD9Smiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان انتظار CR7
النصر قهرمان لیگ عربستان شد
🔸
با برد ۴ بر یک النصر مقابل ضمک در هفتۀ آخر لیگ عربستان این تیم به مقام قهرمانی رسید. رونالدو در این بازی دو گل به ثمر رساند.
🔸
این اولین جام رونالدو پس از سه سال حضور در النصر است
@Sportfars</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/437137" target="_blank">📅 23:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e61794309.mp4?token=jBtzOwLUBfIOwfP5BIJDyfO0GW4d0sDc1xmlfh1Spxr1DYlf05Kzw6JC5vBROocSYhm_Jr9_-IqXh0XYc5hQRTtn6aeavvWJXyMyqqa5rA03N2oTY6jNMGBlJNdn3QdLxN4HiA37cYkgLTNM5EElG_JhBlvApr9W16RidixWJ9UkXRp-dGzjELaGPYTTRFX79GBq2ndPRBRTxKzgAvQhCLtqQaBKX4xOHiJbuLlik3NA_hukTUDABRS72wL9BV0H7ZcZxaQwqt2OI3920xVcvigapZXr7mxHNzaqxMN_PRa60xE5V_y92GbEqcM55iAymQ7cubm_wopa7bxUqCSBozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e61794309.mp4?token=jBtzOwLUBfIOwfP5BIJDyfO0GW4d0sDc1xmlfh1Spxr1DYlf05Kzw6JC5vBROocSYhm_Jr9_-IqXh0XYc5hQRTtn6aeavvWJXyMyqqa5rA03N2oTY6jNMGBlJNdn3QdLxN4HiA37cYkgLTNM5EElG_JhBlvApr9W16RidixWJ9UkXRp-dGzjELaGPYTTRFX79GBq2ndPRBRTxKzgAvQhCLtqQaBKX4xOHiJbuLlik3NA_hukTUDABRS72wL9BV0H7ZcZxaQwqt2OI3920xVcvigapZXr7mxHNzaqxMN_PRa60xE5V_y92GbEqcM55iAymQ7cubm_wopa7bxUqCSBozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاسوج همچنان عزادار رهبر شهید امت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/437136" target="_blank">📅 23:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d57dbedb.mp4?token=QpOj3EpFJbYNa5-gS7QhFDG2dHjs9mlPS-h2bDkHhiQB3rDQtqUFUVeBkN-DBZ2sQ52QycVBZs-n9VxKszk-MHjoFEC5OGROtFAcnjA3tF0VeGpXAyL7EZ5ygplZLOb86Z3AdGQ0m2_TfMHwBTelKI8Yc6cG1O7ZLUIAmCxYnh7q2DOvK2Vp-_w7EJjZosAxUo5mRslDDiR4tvA1zXFb8uOc_czqAMNoOAQUNuv0Sc1OglaXMxZrQkrk8iHmzD-aphC4C6BrtoXkx1-OPnyCGT1v1p_Y0OEDtwbfBuCfhsAdsCf_vM5IZRa8HVFePVhYKoXq7BUfIJIyUiSi9n-jKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d57dbedb.mp4?token=QpOj3EpFJbYNa5-gS7QhFDG2dHjs9mlPS-h2bDkHhiQB3rDQtqUFUVeBkN-DBZ2sQ52QycVBZs-n9VxKszk-MHjoFEC5OGROtFAcnjA3tF0VeGpXAyL7EZ5ygplZLOb86Z3AdGQ0m2_TfMHwBTelKI8Yc6cG1O7ZLUIAmCxYnh7q2DOvK2Vp-_w7EJjZosAxUo5mRslDDiR4tvA1zXFb8uOc_czqAMNoOAQUNuv0Sc1OglaXMxZrQkrk8iHmzD-aphC4C6BrtoXkx1-OPnyCGT1v1p_Y0OEDtwbfBuCfhsAdsCf_vM5IZRa8HVFePVhYKoXq7BUfIJIyUiSi9n-jKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: نظر رهبر انقلاب و دولت، داشتن ارتباطات خوب با منطقه است اما مشکل این است که این کشورها دارند به‌عنوان پایگاه آمریکا عمل می‌کنند
🔹
وقتی از خاک این کشورها به ایران حمله می‌شود ما چاره‌ای جز مقابله و پاسخ نداریم. @Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/437135" target="_blank">📅 23:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcf537d83.mp4?token=c4--UqHTXGysr1QU3USsx5T-rbrchINkVsRlr1MuSMTAaR09ygdCYQdvrWGkcHY6wuA7ag_E8WA-F6hMZnWyJZJGUaQz9PQNkaqwvPPOdgFZ54IEkdHf6TlKrIkKC5bOetxKKAs_56QFzqZPm8Uw7LQIMzvTJXvaxvwU-Z13nzjVyYppcUh0G60EYl30_zztSgbETAAQ1XBDLo8cOJYbhjt8vQWRU6ayp5b757-0XwORR8WNeX_kT0vdr3Mwz4xbUSnPmY9rKUs5PySz_shgx3JJ8SHr3Jw1fjdp2nV1zz6D4x3HtPyzhTxju68PjOao-HoR-d_OwU-2Qv1d9U7IZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcf537d83.mp4?token=c4--UqHTXGysr1QU3USsx5T-rbrchINkVsRlr1MuSMTAaR09ygdCYQdvrWGkcHY6wuA7ag_E8WA-F6hMZnWyJZJGUaQz9PQNkaqwvPPOdgFZ54IEkdHf6TlKrIkKC5bOetxKKAs_56QFzqZPm8Uw7LQIMzvTJXvaxvwU-Z13nzjVyYppcUh0G60EYl30_zztSgbETAAQ1XBDLo8cOJYbhjt8vQWRU6ayp5b757-0XwORR8WNeX_kT0vdr3Mwz4xbUSnPmY9rKUs5PySz_shgx3JJ8SHr3Jw1fjdp2nV1zz6D4x3HtPyzhTxju68PjOao-HoR-d_OwU-2Qv1d9U7IZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: مسائل ما با آمریکا وقتی حل می‌شود که آن‌ها مطمئن شوند که ما به‌حدی از قدرت رسیده‌ایم که نمی‌توانند در مقابل ما کاری انجام دهند.  @Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/437134" target="_blank">📅 23:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4bb83829.mp4?token=ceo2dG2DdR1CcJXlAORpsRb45SNG09A7wfWD84Mgmfta5W6OsKUYu6wrH9TFCxngQ1KqbPKNAGchtVQJ7EofkmXVbYO_GwpkscGgVukyj2IkT6Sre6eGLKK5XC_6w7D7l4CyFjrfyRMd-_qv05qQsCm4Sbs2i6SOFjJ886EnchTxDCeQcUr7K-GycECy8kq5AUnVSmK1Zgmv-sRyaUMxJamGCLnBAQOt7kC6zpkB-tPk6i_M-xnzHtLRBDbyb5gTAQ9NMmt0btHvsv9CqRViTZ7ZAyCq4BKiPsXYaNJp_KAHk5HolS59eUiOuzG3nlXGJ_r40Ikdt6I-3x8arD5eIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4bb83829.mp4?token=ceo2dG2DdR1CcJXlAORpsRb45SNG09A7wfWD84Mgmfta5W6OsKUYu6wrH9TFCxngQ1KqbPKNAGchtVQJ7EofkmXVbYO_GwpkscGgVukyj2IkT6Sre6eGLKK5XC_6w7D7l4CyFjrfyRMd-_qv05qQsCm4Sbs2i6SOFjJ886EnchTxDCeQcUr7K-GycECy8kq5AUnVSmK1Zgmv-sRyaUMxJamGCLnBAQOt7kC6zpkB-tPk6i_M-xnzHtLRBDbyb5gTAQ9NMmt0btHvsv9CqRViTZ7ZAyCq4BKiPsXYaNJp_KAHk5HolS59eUiOuzG3nlXGJ_r40Ikdt6I-3x8arD5eIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در دهلران هم‌چنان صدای حضور می‌آید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/437133" target="_blank">📅 23:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS3bbXYw4-vx9C2Obt5OCiaX4IGNIHGtTfAo-Sg6OsfjD2SlvKd1lIlurdO_vc_nGbTDXv5apRR7vHO1keCoKx5Bd0UScNtcO-SaYJGJo0twVj1YFc0ViS3JoOjZA8I7VvS23x1bpVp8Ekvg6P7TXe5Q9BnxVjK-8rK5ibs0C3AYm8Zi4-CGOrG5z9kU6--StX3mSmbi6SgCp2wnpsluAOX3eJbsX_sFjRE98TrpwvEb9r6iiPktac0Zq-_UdsZrVNetohzvzDXgP4OhSia1c8DW2xMXC4IjX0fmfKEjHrW7-9ynjbWtIWxZW_Quoi5l_voIALu5lQfgLGPR1Wlsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالیوود برای قهرمان‌سازی از شکست آمریکا در ایران دست‌به‌کار شد
🔹
درحالی‌که روایت رسمی آمریکا از عملیات نجات خلبانان سرنگون‌شده بر فراز ایران همچنان با ابهامات گسترده روبه‌روست، هالیوود خیلی زود وارد میدان شده تا نسخه سینمایی این ماجرا را بسازد.
🔹
این پروژهٔ تازه از مایکل بی، کارگردان شناخته‌شده فیلم‌های جنگی و اکشن، بار دیگر نشان می‌دهد که صنعت سرگرمی آمریکا چگونه سال‌هاست روایت‌های یک‌طرفهٔ جنگی واشنگتن را به قهرمان‌سازی‌های پرزرق‌وبرق سینمایی تبدیل می‌کند.
🔹
سخنگوی قرارگاه مرکزی خاتم‌الانبیا (ص) تأکید کرده است که تلاش آمریکا برای نجات خلبانان با عملیات مشترک نیروهای ایرانی ناکام مانده است.
🔹
لاشه این تجهیزات در جنوب اصفهان همچنان وجود دارد و قابل رویت است، اما ظاهراً هالیوود پیشاپیش تصمیم خود را گرفته و روایت آمریکایی را به یک پروژه سینمایی بزرگ تبدیل کرده است.
🔹
این شتاب برای تبدیل یک روایت جنگی به محصول سرگرمی، برای منتقدان نشانه‌ای آشناست: هالیوود بار دیگر در حال ایفای نقش مکمل سیاست خارجی آمریکاست؛ جایی که دوربین‌ها، انفجارها و موسیقی حماسی، جایگزین پرسش درباره حقیقت جنگ می‌شوند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/437132" target="_blank">📅 23:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c599021b11.mp4?token=nL1sGgCr6s-f-ePoq4uDP6zcd1teIw5DgsBVE8J902S28UP1a70ykxiF_VSATuGCDBW9P0TjtqbaUGJfRWBtyqoTl2i3JtI3xUUGAV9-aXjKgMG0ABEBQCR-FRvh2vQVxH9KoeEGN3xcTHqJ2EfHiJ-baShTRPdGjTQzm9ty60dZ7mR6nZ2Gu7K8hLP6Nbh7pOApkCVGv2J6dEoRfk87DQpDFT_T39GbSzw4QdYSeY-78aYmSqgwaUxrlEgbLCMECITZbtXV2OuWz2tz2lgAlZB2Os6ByOc0y1niUKI-Xhp97wP-OEb3I4lWLXvrVXBVtrBWhm9AiUAUSe2o4HgIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c599021b11.mp4?token=nL1sGgCr6s-f-ePoq4uDP6zcd1teIw5DgsBVE8J902S28UP1a70ykxiF_VSATuGCDBW9P0TjtqbaUGJfRWBtyqoTl2i3JtI3xUUGAV9-aXjKgMG0ABEBQCR-FRvh2vQVxH9KoeEGN3xcTHqJ2EfHiJ-baShTRPdGjTQzm9ty60dZ7mR6nZ2Gu7K8hLP6Nbh7pOApkCVGv2J6dEoRfk87DQpDFT_T39GbSzw4QdYSeY-78aYmSqgwaUxrlEgbLCMECITZbtXV2OuWz2tz2lgAlZB2Os6ByOc0y1niUKI-Xhp97wP-OEb3I4lWLXvrVXBVtrBWhm9AiUAUSe2o4HgIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: بحث پایان منطقه‌ای جنگ، دریافت غرامت، مدیریت تنگهٔ هرمز و رفع تحریم‌ها چیزهایی نیست که مردم و مسئولان از آن بگذرند.  @Farsna</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/437131" target="_blank">📅 23:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5922b81255.mp4?token=X8UHCL77ikEQ7VPK_F2jybPjp-H6AfHrV8JmDIEpqniDTTMpkhfe6DSkT_xDHMPUw4b6An1Q5Is6b41FchnREAZ5Wi-Nb_Iq5nFkHfnvOmE6SfISR0KsjrkCPsBObBB1TxHe6bQOk7AvIcUkRxul9sKMJGVzqvmdIRDJS3OYQ8iCFuK45965e4zakteW350EBL0vsAqnjZAjAc_jdjUkathhbJunpLgykZYMKpeXy-_QnbynuNmU1K2niO2F2lS9TMK-zYc32sChnsLDKKhxhg6j2lIQPiE0weuJoT928xe5x4YQ33w895IrOc1O5GfMqVuX5zcQBMJfjmKsH0JmGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5922b81255.mp4?token=X8UHCL77ikEQ7VPK_F2jybPjp-H6AfHrV8JmDIEpqniDTTMpkhfe6DSkT_xDHMPUw4b6An1Q5Is6b41FchnREAZ5Wi-Nb_Iq5nFkHfnvOmE6SfISR0KsjrkCPsBObBB1TxHe6bQOk7AvIcUkRxul9sKMJGVzqvmdIRDJS3OYQ8iCFuK45965e4zakteW350EBL0vsAqnjZAjAc_jdjUkathhbJunpLgykZYMKpeXy-_QnbynuNmU1K2niO2F2lS9TMK-zYc32sChnsLDKKhxhg6j2lIQPiE0weuJoT928xe5x4YQ33w895IrOc1O5GfMqVuX5zcQBMJfjmKsH0JmGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی مردم پارس‌آباد اردبیل در هشتادودومین شب اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/437130" target="_blank">📅 23:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e3e44a7a.mp4?token=kE5YFPIp2H5ibx99f8ZZP-speg1PCI5O18zh1bFetYCghq-e8yvkDbjTV2WCjc2IQXTivjvxVBuNyItEuMtT56hcWxjtqK3jQ6QuRumSwkJ35G6_-xHTYQDM0fw8_DeaQFRWeniP0NRgsOzZNVFk0FwCQTYtw1wKtei5yckY3JTL-mORxcvOW6c2si1XisIM_CQ-7naN76Flr55y96d6yYVIrlGlYtIoyp2OpqAY5ly7yDCstU8YPVnVhoA-gHICov0q-i3h5ac1Ig-vEgXmhhxUP26N1dOqaRDxtB5JkF9VSdi504CdYgrx0MLlpdDuMhV3ezT_bZ15AYPmqO9hwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e3e44a7a.mp4?token=kE5YFPIp2H5ibx99f8ZZP-speg1PCI5O18zh1bFetYCghq-e8yvkDbjTV2WCjc2IQXTivjvxVBuNyItEuMtT56hcWxjtqK3jQ6QuRumSwkJ35G6_-xHTYQDM0fw8_DeaQFRWeniP0NRgsOzZNVFk0FwCQTYtw1wKtei5yckY3JTL-mORxcvOW6c2si1XisIM_CQ-7naN76Flr55y96d6yYVIrlGlYtIoyp2OpqAY5ly7yDCstU8YPVnVhoA-gHICov0q-i3h5ac1Ig-vEgXmhhxUP26N1dOqaRDxtB5JkF9VSdi504CdYgrx0MLlpdDuMhV3ezT_bZ15AYPmqO9hwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: هیچ‌وقت باور نکردم که حادثهٔ سقوط بالگرد شهید رئیسی یک اتفاق عادی باشد.  @Farsna</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/437129" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e9239273.mp4?token=p5O2rYHyYlKUB7G_ZSRUQHIQjSUdu4OyTya55EI489fLudjlLCJfhcbbyxFDrsfrlw34o6ernl7NMudFH8Mm4codSROHGjUFnPvKIcN4szkJBplEe-RhAxXkxHWeTuz1z7b_NTCgiLUOlM-QmqQSqiJTtaiAT_54Yjv8W5-J5-hlimfPSSu6lSIAOeNKSi4wPO58uTWVGtLvTXIP2p-P6b6unUR-KZkI4IbI9a3nagD6BXjpFqjQh0CM-AHG7rnOt2_odF2MHmtxDtTcNxFipe5jOqZegh_iMG7UOzB-_tUVxRmFYeWkY2rnyZDm1mTT3Bf_L2F3LpnkKkYp0HFv3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e9239273.mp4?token=p5O2rYHyYlKUB7G_ZSRUQHIQjSUdu4OyTya55EI489fLudjlLCJfhcbbyxFDrsfrlw34o6ernl7NMudFH8Mm4codSROHGjUFnPvKIcN4szkJBplEe-RhAxXkxHWeTuz1z7b_NTCgiLUOlM-QmqQSqiJTtaiAT_54Yjv8W5-J5-hlimfPSSu6lSIAOeNKSi4wPO58uTWVGtLvTXIP2p-P6b6unUR-KZkI4IbI9a3nagD6BXjpFqjQh0CM-AHG7rnOt2_odF2MHmtxDtTcNxFipe5jOqZegh_iMG7UOzB-_tUVxRmFYeWkY2rnyZDm1mTT3Bf_L2F3LpnkKkYp0HFv3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: هیچ‌وقت باور نکردم که حادثهٔ سقوط بالگرد شهید رئیسی یک اتفاق عادی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/farsna/437128" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dce039f1b.mp4?token=KdhU_c0ZyHlNEqtSYL9GWn__HX6L0bua9wvkLs6Dh_3e9QIEjvH_EGlYdWRlIbXbNOSyA4372AYDulirk_bY6YBQ3eLYJRtxSQxFkSHGcg9D0lUX3cV6oZLhYgGFJhgJSNAv76_xZvWwmKLHlJLhPGPcPh6JlqhRFftrDSN1drqpfNEMx9RC_GE9gqYRHhKQWGPq8fgJX_VWLrLPTyDRg-jyag9Wt-wf6bkfkXJmh7rURWX1k5k2qhz1aQ_nuIJw07lSyox7RCblua1rYSdAVFVztG7dGy_tiaOoVQf0cErRIOX65ZJvZyRR40aFcmon5gTFe0dNKecckP8-LQif44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dce039f1b.mp4?token=KdhU_c0ZyHlNEqtSYL9GWn__HX6L0bua9wvkLs6Dh_3e9QIEjvH_EGlYdWRlIbXbNOSyA4372AYDulirk_bY6YBQ3eLYJRtxSQxFkSHGcg9D0lUX3cV6oZLhYgGFJhgJSNAv76_xZvWwmKLHlJLhPGPcPh6JlqhRFftrDSN1drqpfNEMx9RC_GE9gqYRHhKQWGPq8fgJX_VWLrLPTyDRg-jyag9Wt-wf6bkfkXJmh7rURWX1k5k2qhz1aQ_nuIJw07lSyox7RCblua1rYSdAVFVztG7dGy_tiaOoVQf0cErRIOX65ZJvZyRR40aFcmon5gTFe0dNKecckP8-LQif44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مازندرانی‌ها امشب هم سنگر خیابان را حفظ کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/437127" target="_blank">📅 23:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az4R9jtY4PHeB6J6fjY8AftWKGr9d8z-sNYuvtN09JkdaKY07Bx0BIHyqvl8sP5iDhGEwYButuzSNsdBPYNvfbDq1GmfiWGTaFrjs4fH2yNYOgxYYBycXwfQq23kMVGliNykSz49uCRTIUG4KxOqmAdcDbGBfETxWaUVgKzk4pC7gEIbD4774a0Rjgaig-7ORukt_ix9SnhhIds4Bt28RbKsdv5Ynkn6ENkX3GSOcEdr5tEMCCPcY-2kS0tPE5i94F_sYxH2ytvj0nOLNwvuZnwPiL8hrfJESqmbpy-4KYVAUwcpmymyoZFDSJ_qqGeudz6PDIzVDA8amAyG16kCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکش‌های جنگ علیه ایران به اقتصاد عربستان
🔹
عربستان در پی کسری بودجهٔ ۳۳.۵ میلیارد دلاری و جهش ۲۶ درصدی هزینه‌های نظامی، تمامی قراردادهای جدید با شرکت‌های مشاوره‌ای غربی را متوقف و پرداخت‌ها را به تعویق انداخت.
🔹
روزنامه فایننشال‌تایمز می‌گوید: ریاض پرداخت صورت‌حساب‌های این شرکت‌ها را به تعویق انداخته و این اقدام بی‌سابقه نشان می‌دهد ریاض در حال بازنگری اساسی در بودجه کلان‌پروژه‌های بلندپروازانه خود است.
🔹
این تصمیم، زنگ خطر را برای غول‌های مشاوره‌ای جهان نظیر «مک‌کینزی»، «بوستون کانسالتینگ گروپ» و چهار شرکت بزرگ حسابرسی جهان (Big Four) که در یک دهه گذشته بازار عربستان را به «معدن طلای» خود تبدیل کرده بودند، به صدا درآورده است.
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/437126" target="_blank">📅 23:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
بروجردی‌ها ۸۲ شب در خیابان
ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/437125" target="_blank">📅 23:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb6680f1d.mp4?token=PFbKCiAtfC1S0-7b-eU_Vl8ckT84j98EZYg7abUI0hJx3wcqmhjzjlLN50lGxNGJ7SezzT7sRdfQTZdXbBIBZJWvhi_3kV2Rq8520SBMh58hCBrK3aKVR5A9Ig_TJZI8BD-eBiXDhy8dMmIEZ7T-XzsnO_pvqbUIRuC_2EG7HMjWeeN9JDzzTpxqpVzwjGwzUkFOIeIR9xOLumaeSmzy_w6d2U3xzD-UOhZNaa_IqYTlaaq6TYHzpYaTkNL5apXECYxqJGYqJvkllPhJmHrLlCqYenLhX3L62uZMUcCaPFrMhLvWW1aCHVi0T4Rclt9nb-571J3Pat7uhJhtQTJKJj2RPxZiJCbgmLe75x9GqbkbI28-wMgdZsgD0DF1jx47b4wYAoNFn59yVi3fcxbIH97nk8FRwkixkCyyhPHSsbzh7GacGHwcK2yBl8SYZyxn0_JcLSTZcBXHZTjF_zbgE4eGDczJNy-MjM57AALC2tgMLCLwI954x6r9ib8JZVfTbHVHPjMtBpeokV2mU_4OLU1Nhpoqg_3HhrzSAVH8pSTao6qErcWy5JXEgru1DxKNbActHkRhFmUGFeO4hEjvnCaGZLFiqPYKm3CpST76dJvjhTjTXi-GfFKcAmQTYAqLNHxMv3WAKwQ-MyXdbLnoUHq-XVsBWk3wypsFJ1c_i5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb6680f1d.mp4?token=PFbKCiAtfC1S0-7b-eU_Vl8ckT84j98EZYg7abUI0hJx3wcqmhjzjlLN50lGxNGJ7SezzT7sRdfQTZdXbBIBZJWvhi_3kV2Rq8520SBMh58hCBrK3aKVR5A9Ig_TJZI8BD-eBiXDhy8dMmIEZ7T-XzsnO_pvqbUIRuC_2EG7HMjWeeN9JDzzTpxqpVzwjGwzUkFOIeIR9xOLumaeSmzy_w6d2U3xzD-UOhZNaa_IqYTlaaq6TYHzpYaTkNL5apXECYxqJGYqJvkllPhJmHrLlCqYenLhX3L62uZMUcCaPFrMhLvWW1aCHVi0T4Rclt9nb-571J3Pat7uhJhtQTJKJj2RPxZiJCbgmLe75x9GqbkbI28-wMgdZsgD0DF1jx47b4wYAoNFn59yVi3fcxbIH97nk8FRwkixkCyyhPHSsbzh7GacGHwcK2yBl8SYZyxn0_JcLSTZcBXHZTjF_zbgE4eGDczJNy-MjM57AALC2tgMLCLwI954x6r9ib8JZVfTbHVHPjMtBpeokV2mU_4OLU1Nhpoqg_3HhrzSAVH8pSTao6qErcWy5JXEgru1DxKNbActHkRhFmUGFeO4hEjvnCaGZLFiqPYKm3CpST76dJvjhTjTXi-GfFKcAmQTYAqLNHxMv3WAKwQ-MyXdbLnoUHq-XVsBWk3wypsFJ1c_i5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا خیابان؟ اهوازی‌ها پاسخ می‌دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/437124" target="_blank">📅 23:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIjK7pewPHbN6WfjjcnWbyb15o3z2ZTG7267DNngq6_OhhK4sYgWYlCOPr87GlrI4TpkUZ6iPLDoO8D-oORLO4f4hfKr33v4dI8CZsRU_sU-kF4d_gBQMveUH5OK1qDq-cX_lwF8Ob4V68_Mr14lhgymRU3xmNPKNUzUW84VhgcXCNCVEYYfmYNb_WEmQ1Bn6drYOxV7uN_ZwU2jVSP6RBC0XhOa9vmq_KLwUq2K8hWoPi1JBfluKl49C3x1weJIQiEvFX1wGRvHV438MVvQRQF5yRmC_U0CwLebshi4wQ1xjFy4gs3F_cl6Z0lGyH7bC1_8AChxvsD_CAS75wlUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/437123" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎥
پرچم‌داری مراغه‌ای ها در میدان حضور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/437122" target="_blank">📅 22:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15e6185467.mp4?token=ZYRKMk6OG_LNWzXZbrnksuydhvL4l3y9dO0nrNqaObqS8kNYO3Yg-kugtFWgnb80kNXYql63cQtcmoumX2GW_AARyl--lmqoUtbfS6SA29-G_B7f2-QjmnVCRkLtSQXlYL4gxL-qaEK9UsRnqEgWyrfJ6-higMyKx30Gm4ARnN1ZBVWi4unBIp21crzHDT-IXo4FmkPQPB0wjAj2vZwP-wYv6uc9LxRwiZej2wKSAMUA8fvRhM2n-4mxKC3kt760DaPkPL2vDNiS6vU4jfetrnw73rcY5qhRk_shn7tc2LE_mrbXjw-pUO6uDwpDjaHqv7eAPCdNF84B8mbp1TeCKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15e6185467.mp4?token=ZYRKMk6OG_LNWzXZbrnksuydhvL4l3y9dO0nrNqaObqS8kNYO3Yg-kugtFWgnb80kNXYql63cQtcmoumX2GW_AARyl--lmqoUtbfS6SA29-G_B7f2-QjmnVCRkLtSQXlYL4gxL-qaEK9UsRnqEgWyrfJ6-higMyKx30Gm4ARnN1ZBVWi4unBIp21crzHDT-IXo4FmkPQPB0wjAj2vZwP-wYv6uc9LxRwiZej2wKSAMUA8fvRhM2n-4mxKC3kt760DaPkPL2vDNiS6vU4jfetrnw73rcY5qhRk_shn7tc2LE_mrbXjw-pUO6uDwpDjaHqv7eAPCdNF84B8mbp1TeCKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنینِ «نام جاوید وطن» در میدان انقلاب تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/437121" target="_blank">📅 22:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781f24a277.mp4?token=TMklJbEOXaW8i9jDxInJ5VJPnit0xNet2gPnYTF3QA0M0_MgI1XlSgUD5vP1a9KZ7XrhyYeL12iKu5NYvvmCiTkDoit_Q5wv260JdJHPO7K7CWRXXRT7E26PLihDFZFy6LfQX_Pp40SwKXLHw2GtPTTqyeAkZEYas0rz7NZ0tHhtqlI-pRpZ-zt11ueRSMjiAgcD2S_Mn8AO8wlQ2e5Dsar9qC_616aCBdXsyR9DVCYMo3IKA8YiI2MOIJQWhRSUN4_jr-CBJg9DZd1kaDXmVRUQruPZNpRVafOV9cNgGj-PUWUBhb6ymXoyjMgJ5T7ss2GPDixNO34lDQW7YliGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781f24a277.mp4?token=TMklJbEOXaW8i9jDxInJ5VJPnit0xNet2gPnYTF3QA0M0_MgI1XlSgUD5vP1a9KZ7XrhyYeL12iKu5NYvvmCiTkDoit_Q5wv260JdJHPO7K7CWRXXRT7E26PLihDFZFy6LfQX_Pp40SwKXLHw2GtPTTqyeAkZEYas0rz7NZ0tHhtqlI-pRpZ-zt11ueRSMjiAgcD2S_Mn8AO8wlQ2e5Dsar9qC_616aCBdXsyR9DVCYMo3IKA8YiI2MOIJQWhRSUN4_jr-CBJg9DZd1kaDXmVRUQruPZNpRVafOV9cNgGj-PUWUBhb6ymXoyjMgJ5T7ss2GPDixNO34lDQW7YliGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر امروز، روز آخر زندگی‌تان باشد چه‌کار می‌کنید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/437120" target="_blank">📅 22:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-text">بالا و پایینِ «تهران کنارت»
🔹
بعد از انتقادهای مکرر از اکران فیلم سینمایی «تهران کنارت» و ثبت پویشی با بیش از ۴ هزار امضا در سامانهٔ «فارس من» خبرگزاری فارس، رسانه قوه قضائیه از احضار رئیس سازمان سینمایی در پی انتشار یک فیلم سینمایی با محتوای مغایر با عفت عمومی خبر داد.
🔹
انتشار تیزر این فیلم سینمایی با پوشش خلاف عرف و صحنه‌های منافی با عفت عمومی انتقادهایی را از طرف مردم متوجه این فیلم کرده بود؛ هرچند بعدا پخش‌کننده این فیلم در مصاحبه‌ای بیان کرده بود که «‌انتشار تیزر بدون مجوز و با استفاده از سکانس‌های حذف شده فیلم ساخته شده است.» اما پخش صدای خواننده زن،‌ صحنه‌های رقص و تصاویر منافی عفت در اصل فیلم سینمایی هم وجود داشت.
🔹
رسانه قوه قضائیه خبر از تشکیل پرونده برای دست‌اندرکاران این فیلم سینمایی داد؛ همچنین قرار بر اصلاح نسخه اکران شده و بازگشت فیلم به پرده سینما بوده است.
🔹
با این وجود هم‌اکنون امکان خرید بلیت فیلم سینمایی «تهران کنارت» برای روز جاری و روز آینده وجود دارد.
🔹
با وجود دغدغه مردمی و رسیدگی قوه‌قضائیه به این مطالبه حسین فرح بخش کارگردان آثاری چون «شهر هرت» و «خالتور» با مصادره تجمعات شبانه مردم به نام خود به امضا کنندگان پویش فارس من حمله کرده و گفته بود «آن ۹ نفری که به فیلم پروانه نمایش دادند معتمدین به نظام هستند و از شما به نظام‌ نزدیک‌تر هستند.»
🔹
فرحبخش در این ویدئو ابتدا گفت «مردم ۸۰ روز در خیابان هستند و شما به جای همدلی با مردم و دولت، کمپین تشکیل می‌دهید؟» و بعد به مردم گفت «به جهنم که فیلم را نمی‌پسندید‌. شما در این مملکت چه‌کاره هستید که هرازچندگاه سبز می‌شوید و آبروی همه چیز را می‌برید.»
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/437119" target="_blank">📅 22:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9ecda6c9.mp4?token=BjWTCvX2MVi1T4GnrCrLsHixaMapM4uZsr3vY0iycnKJ4ROSGzrAS3pOBpb2K7Mt6y24NH9-t7hMz003B85Gs5UWjRPc1d8p2PwK7xHP0vYKn_e9tdUQs3k6dLsLBdCPfQmryppi7vmbfCT3JyYPyQYOEtLGBBqBRXLdGxW_nA07N3hJ2Poocg-gv1HU2sT0Bn4GaWl2ooHQyZLoh9N-8TlrWwssKpYzC-B2-YK6UyVZSwIrWM1PZxOYzF2Z6HQAewzeHqfUgW9hX8e692ee1jgZcUURGhSLzO3HHuJ1STx2_NlJbpeWR8DrzPkXMaY9r0TAUPFNuGtewNh_6qF-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9ecda6c9.mp4?token=BjWTCvX2MVi1T4GnrCrLsHixaMapM4uZsr3vY0iycnKJ4ROSGzrAS3pOBpb2K7Mt6y24NH9-t7hMz003B85Gs5UWjRPc1d8p2PwK7xHP0vYKn_e9tdUQs3k6dLsLBdCPfQmryppi7vmbfCT3JyYPyQYOEtLGBBqBRXLdGxW_nA07N3hJ2Poocg-gv1HU2sT0Bn4GaWl2ooHQyZLoh9N-8TlrWwssKpYzC-B2-YK6UyVZSwIrWM1PZxOYzF2Z6HQAewzeHqfUgW9hX8e692ee1jgZcUURGhSLzO3HHuJ1STx2_NlJbpeWR8DrzPkXMaY9r0TAUPFNuGtewNh_6qF-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ شهرکردی‌ها در شب ۸۲ ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/437118" target="_blank">📅 22:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آمریکا سفیر ایران در لبنان را تحریم کرد
🔹
خزانه‌داری آمریکا اعلام کرد که ۹ نفر از جمله محمدرضا رئوف شیبانی، سفیر ایران در لبنان، را به‌دلیل ممانعت از خلع سلاح حزب‌الله تحریم کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437117" target="_blank">📅 22:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab79e5d64.mp4?token=UBS1toxIQ7QeeZKwd0zT-zxX_7iWmRR-KdjzdGg7om9lnIGJwGxj6FqepgWo_7SnPNvLUy6E1J2bluN6dsHtjOhm5EqRu0MR7uX_wckPnCiXUjUO8TyLRjW8M8IuQ8AFYTN-_nHowx6dtQHM6N3za1YT4euOxCf5ZimaJX9wIFxeCp6snILBPxQdkSUHPru2DwW8W3RjTJInSKcGea4T81WiwsxtpPMkElh3E_v3ZaiEf1h9XBnKqLt8Zt45tKfa3no7rAScMaHmGgS_8RvkGG6fhQpB_b7atDTDRKk-xGrJKZOzonQouWyxymFdrBKAuNENADzv_bkOGEyHJ0UTXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab79e5d64.mp4?token=UBS1toxIQ7QeeZKwd0zT-zxX_7iWmRR-KdjzdGg7om9lnIGJwGxj6FqepgWo_7SnPNvLUy6E1J2bluN6dsHtjOhm5EqRu0MR7uX_wckPnCiXUjUO8TyLRjW8M8IuQ8AFYTN-_nHowx6dtQHM6N3za1YT4euOxCf5ZimaJX9wIFxeCp6snILBPxQdkSUHPru2DwW8W3RjTJInSKcGea4T81WiwsxtpPMkElh3E_v3ZaiEf1h9XBnKqLt8Zt45tKfa3no7rAScMaHmGgS_8RvkGG6fhQpB_b7atDTDRKk-xGrJKZOzonQouWyxymFdrBKAuNENADzv_bkOGEyHJ0UTXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواد اولیهٔ پلاستیک به اندازهٔ کافی در بازار هست اما قیمت‌ها چند برابر شده
!
🔸
کارشناسان می‌گویند مواد اولیه را برخی با قیمت مناسب از بورس کالا می‌خرند اما به‌جای تولید آن را با قیمت بالا می‌فروشند.
@Farsna</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/437116" target="_blank">📅 21:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3f5d2009.mp4?token=Yr2Az1gxWa_AqlfZGOOea52pv4h7ejWy90y0mJ1OOLwYIrpNDafqQX8KBZptCpedD2sKazLv6Kf9wmGdQpZeDQVs04WQk40poSMVEBvWx5V9BiWZ56cUDvbeAztsduM_06S7N2UnUWh5xaGImVeMx1OZFgtFOM5Eaer5JHo3ETH8Hd3epzbmvxA9FnRjtp7XVsuQcRL4Wm5wKlrjI7EDz7g5-7Q6FkS3K1THtZi_VwnDjC3qkxzdYQ7Zw0hcICyDIuX4DdGJSLBptuJD_7JPSCLCnXUGQ73eVnHEJ3gIJMMhzU1Ap9d90NJV7yNcQluiOMso7kgbgZAzDmFMU5DYKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3f5d2009.mp4?token=Yr2Az1gxWa_AqlfZGOOea52pv4h7ejWy90y0mJ1OOLwYIrpNDafqQX8KBZptCpedD2sKazLv6Kf9wmGdQpZeDQVs04WQk40poSMVEBvWx5V9BiWZ56cUDvbeAztsduM_06S7N2UnUWh5xaGImVeMx1OZFgtFOM5Eaer5JHo3ETH8Hd3epzbmvxA9FnRjtp7XVsuQcRL4Wm5wKlrjI7EDz7g5-7Q6FkS3K1THtZi_VwnDjC3qkxzdYQ7Zw0hcICyDIuX4DdGJSLBptuJD_7JPSCLCnXUGQ73eVnHEJ3gIJMMhzU1Ap9d90NJV7yNcQluiOMso7kgbgZAzDmFMU5DYKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی و شهیدان شمخانی و لاریجانی در سفر حج
🔹
این تصاویر مربوط به سفر هیئت عالی رتبه سپاه پاسداران انقلاب اسلامی به سفر حج در سال ۱۳۷۱ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/437115" target="_blank">📅 21:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwNbuwZAHAhKhgVQoKzo7SaLcJksMbeeLnn9gKCk0v94MFzCRbQslMqlMhcgfFhzxNm6LPB9-3AVtkTsZg-1IT4uYAc7S537pG1it7Gslv_a2wEhLqaxaWnBf7tuOuxQ0koZR21sRcQdu9n30lsilAPxkjMPDGC2Uwaype7bwmgpAX3IJbqZjOUXD8a_9wPZk7Cx5yAu-gd_qKuKEbjYx_4vOnmxzZmP4rbgn98koiR-unu4aOz3nApAl6eGJP-TuD7LDnBTZAZyBqDEM_jLtVIBJi4smx6VaXIPjEoOdrqU-5JKr3khRICvRp7o55LmjBM8ZjfDCLWYFev9RuNLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3yqef7AgmGdHnA9HktrIRBICA9UqlXCK7MlBlSUYMp65IGbdpmDmr5IC2LwGg0rFH2YD7gm7TCOt9Ak9BZtduhfGqEr1Q_xamO1JlVAN1qLGJPajHO0qaOciqGtWp6CNuF9kB204bbotW5Nx88RtUeZ3AlHwr5RFi1jNwjG0euR4daOCXlnNoVGFrYagVD_QRR7HM5k3TZInkkXMbVKVM_e5NkzDKu_S1X-e34GtO_DA99Ca83xuObjbdbd85wbgLLyq2PBx3l5pEXbQ2pSRr9-v9rsrcsl-EJx0Chgv-Y84hEUHPqYEnHs12lUCysNwUZOr8QrZc-DPv4Tt0nhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmWCSdxO54JvRLXVU53YcuAgGJy3ZiN71HSO8-2yd37pQSBUJWQDFW2OcxY0ZsPB3cA2r9-bBh6Bb3iqq9V7WsKaeU58uXjCDMDT2JKjcQLnbLDNpbewImznGfmuSSVytIxcJ07WprNt_o3_hHEjdUjDKp4ZjwseolTUg1gEBvaY5hwjqzvsvCo5NbG3bxInPvUMSnmYzLJlUXU3pjqQzl6eXtlRFZu1AjXf0vdzSSB1CKthTwgIrCkEOebAOmUnvKecFPJ72QYPm5NMBhtTzYF_vm6Gzv10StqtyICewqTqdZnoaA0goTPcliD-FHnxxgCy2EPEAFbjhzv_Tg3Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3R3Up0TbNXkWKe67M9uWhSrwS7DJBy1gQ2D5XMk57siG-F_Y3x2AkUrv2WdeylnkcOT0k27mOEYtkI4KJYwNhZWG--HzvWPC0ZE_Ys7pX46ZQg8lIATlRBTL_tXqOIBoIOeyHSFGb6HkV9PN_lH0JBR3LURZajPkFkCX9sblw_mLErAuUgAM3J-X6_3HzzGPm7xfZIuokX1C259EmhB4zZp6befPzK2UD8gPYEym3h2EZStHCG1ZidaeyemH4pcYQiGE2EWmMYl1WEMQ-t0mo646QqKi1SDK6pXZRNcKNNapGhOM7i1UoC5ZOmW15k3daIQSr4Py4xBZEXPDv3l0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qs-2JF6i5PGK2o7NYOHejVphT6yigUQi1LqPLhYl6slEN4XL0EA1uARtDtRTnlLWrYPM8E_eIrWp-cBIYI8se1k1QG29k0C8v-VZa_24FAKBcD30cnhOMcVQyH2AX_bY8p57hDv5jIXV4Ey11cgN6gD_H9qiksWHoDAkXcLf4Cc7nMJjnJZoZFXkcxE-u7xUU3aqEQ_-QnqNCzIIteS3Oo3k80y2gdhqQ4GiUseMxs-gAIexQdiB-_kcRMc5NJbaiue7fag7ox7dWdIvTzF1x26tMHDYm8mXArZNa_qDOJgKuvyynUyhMSl77neAjltFSlsCyZPr98rL42SEmb6RTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجمع دوچرخه‌سواران دهه‌نودی در شهرک اکباتان تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/437110" target="_blank">📅 21:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0591f2f022.mp4?token=rp6YiJ-VSgxIkXa9Y6eB0UpXIAmagqFVNIp3feqIrHkCu73tc0Hrq9X4Gi8SQKr1QPgSbysOWmK4TODk4U15JMHYTmo39Xc6OkwkWEgDIY0J-G8Fz2CcXs8l9fm08LtDemq7XDnKj7lbCVDlLOYzJ8Kycp7Dj2cgBQJcsnDIwqHvz4Ijk66nBAw4MJ3tlLTzyALQi1eute3VytWQfaJP0ltGAQmF6LrSJRC7Nl5MZGwruzr2QYb9oI3d0SCTdl7Non3i-NWnMMbCEkL5i8MjrdRujszb901A_ABHHIExbEpm-iaUBwGrZU0nQU2Msd7Ayq4fgwYK4nDKLjPzsK_LXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0591f2f022.mp4?token=rp6YiJ-VSgxIkXa9Y6eB0UpXIAmagqFVNIp3feqIrHkCu73tc0Hrq9X4Gi8SQKr1QPgSbysOWmK4TODk4U15JMHYTmo39Xc6OkwkWEgDIY0J-G8Fz2CcXs8l9fm08LtDemq7XDnKj7lbCVDlLOYzJ8Kycp7Dj2cgBQJcsnDIwqHvz4Ijk66nBAw4MJ3tlLTzyALQi1eute3VytWQfaJP0ltGAQmF6LrSJRC7Nl5MZGwruzr2QYb9oI3d0SCTdl7Non3i-NWnMMbCEkL5i8MjrdRujszb901A_ABHHIExbEpm-iaUBwGrZU0nQU2Msd7Ayq4fgwYK4nDKLjPzsK_LXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گردوخاک و باد شدید در شهر یزد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/437109" target="_blank">📅 21:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">۳ عملیات امروز حزب‌الله علیه رژیم صهیونیستی
🔹
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در شهر دبل، و دو تجمع خودروها و نیروهای دشمن صهیونی در نزدیکی بندر شهر «الناقوره» و شهر «طیر حرفا» مورد اصابت قطعی پهپادها قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/437108" target="_blank">📅 21:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QonhceNsMoHEMhBO_uIFy7-wzaAqc8QmGJSxmwwSCuJPDT1TBnFeNoExI5CIPCpTS8HzTHLyhGA3Ber3_4Nz3AVTpQEl0873bhFkRry2mFBEKEJ36lXvdwNIi9ADMxW-MZFySkFRYUSOwj4nimnTY4yeCdM8lKTZeZIehuSecKq7izfSE8egEz9FS3snOu1qT9SkP5a3lFYFmZl3ULL-xXHFJy73VQ33ocoXMyxbJbK_L2LCYooe-uw9BpcNe9-7GTmpZsQtUAJjOW6DExIIo1GFJu9JnwZl-NF42WlJcW5FshPYjDOhvc0vKvHKaqPrgdGQ_cWi3mgmmVesjTwcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد گمانه‌زنی‌های رسانه‌ای درباره جزئیات مذاکرات مرتبط با خاتمه جنگ
🔹
سخنگوی وزارت امور خارجه در پاسخ به ایرنا ضمن رد گمانه‌زنی‌های رسانه‌ای درباره جزئیات مذاکرات مرتبط با خاتمه جنگ گفت: در این مرحله تمرکز مذاکرات بر خاتمه جنگ در همه جبهه‌ها به شمول لبنان است و ادعاهای مطرح شده در رسانه‌ها درباره مباحث هسته‌ای از جمله مواد غنی شده یا بحث غنی‌سازی، گمانه‌زنی رسانه‌ای بوده و فاقد اعتبار است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/437107" target="_blank">📅 21:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437106">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEXcgWQY_kDZMq04L6g6Na-4I6YtWfWyCmYEIZAp3B5j1zWqaXxiy5b3QwAno8Uclwb0fFaPJLlvJa9-HLGS-E5LrrVc0QQDWVHbj7bACFClysBXpjILUBD-lmpM4f8oOasXdWJbwskB13oRCFiFERTzweB0X0UVroi2QdlalToacuYdVXxy_kQayW6iH1znxTzY8BZZ5rAd5HQGXkj00Bri_S9te79mSZaOpLZzDKhWWEBYvw_Nw5XeCmHF3iz3cnLaWwFAeusLIBzh5ENMfvNP-v4oUVUM5ogqcwnW-1KtU-5hmu1vPsUc_8kCjMGYmsegOdHjRI0RdbpYvcynXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سازمان اطلاعات سپاه: جمع‌بندی نهادهای اطلاعاتی آمریکا این است: «گذشت زمان به نفع ما نیست و برای رهایی از مخمصه چندلایه، ابتکار و تهدید ایران را جدی بگیرید.»
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/437106" target="_blank">📅 21:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437105">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4a110d2e.mp4?token=DGKpMmqvGuWgwhSsBA0BttUg5FCAQD7wAeJ70_k4_h7hVVwiMZDQ7Diw-v8a7qwfKvF7x6E--mihfgyiN2l2fAAgNLzEERp-sgE_6ujIS5AU-9r-PBU688HyCBcmhRBzf3cHnsFd5XPmCOw9Gf1sCxT4vK7WLfLNGJXlAg2JacNHTsHy7LIvOWZb9PZwXHDt8ZYNzLLcBK_yZ_OyZTdvHB49QGTTI98e2O_6awZjuYBSkzlX62ZRj4YYzYmdh9NA81M4WHdGGH_wqtaTjlsOFBV_JjMcjdRxODrhXjm5GFU-cYBnEU6r6v2Mym7MtKZ0ttB1NL3HrxSyLuy8fu8NBqwDW-01XZS0VuxHWGiHsce_0CKufSpsTGaX-FNXnW_OdpstoKSddn3NOZ8qVIJWD1gGsO4ek5nUrGZH7MScPQkTUQZXfSOvhwtoBGTZXG-uASdTaar_RK9978JWml3ooP7V7FxUJYsSr5lEio5JTdDxVljAqHtxx-zOcEzFLH9ZFo0oeyDv5K1t_je8DWo1G3CX_KGcnaTAnEygqagCX1C50BBUYJsIpD9W6y7TJBiqkih3B5wUc5Bi5-xxyq37MZP4B1IY5KGFz2KE7AUh52zgI8t2XBXTbnEjZ6LAumRFoWtxbsh2R4ko6K0KZDk4XG0T6bY-p24HsplhRC9_YcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4a110d2e.mp4?token=DGKpMmqvGuWgwhSsBA0BttUg5FCAQD7wAeJ70_k4_h7hVVwiMZDQ7Diw-v8a7qwfKvF7x6E--mihfgyiN2l2fAAgNLzEERp-sgE_6ujIS5AU-9r-PBU688HyCBcmhRBzf3cHnsFd5XPmCOw9Gf1sCxT4vK7WLfLNGJXlAg2JacNHTsHy7LIvOWZb9PZwXHDt8ZYNzLLcBK_yZ_OyZTdvHB49QGTTI98e2O_6awZjuYBSkzlX62ZRj4YYzYmdh9NA81M4WHdGGH_wqtaTjlsOFBV_JjMcjdRxODrhXjm5GFU-cYBnEU6r6v2Mym7MtKZ0ttB1NL3HrxSyLuy8fu8NBqwDW-01XZS0VuxHWGiHsce_0CKufSpsTGaX-FNXnW_OdpstoKSddn3NOZ8qVIJWD1gGsO4ek5nUrGZH7MScPQkTUQZXfSOvhwtoBGTZXG-uASdTaar_RK9978JWml3ooP7V7FxUJYsSr5lEio5JTdDxVljAqHtxx-zOcEzFLH9ZFo0oeyDv5K1t_je8DWo1G3CX_KGcnaTAnEygqagCX1C50BBUYJsIpD9W6y7TJBiqkih3B5wUc5Bi5-xxyq37MZP4B1IY5KGFz2KE7AUh52zgI8t2XBXTbnEjZ6LAumRFoWtxbsh2R4ko6K0KZDk4XG0T6bY-p24HsplhRC9_YcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور ۵۷ خبرنگار بین‌المللی در مدرسهٔ شجرهٔ طبیهٔ میناب
🔹
۵۷ خبرنگار از کشورهایی مانند ترکیه، آمریکا، چین، روسیه، یمن و... از آثار حملهٔ دشمن آمریکایی صهیوینی به دبستان میناب بازدید کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/437105" target="_blank">📅 21:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f197d827b8.mp4?token=dDMBkZ50yoSpTljJJcTIkYz5xgvPvot6c9bW_0ZHjG5rwNTAPSOlvI1-dnxvtRtUb8REmxP-XtOcnJ58E8e8GNHa0Fr-34UzCB5ZkizyQuCmv2-Q94vfc4PPgI9ODK_-cab-GzI7AwoaX4HnsFMLK_-l2zddG9kBnH75lKMcDO5Va7qiCudmZLJ1wI68ASFf3VFIHpSKzjA64_babvLIE1G0s7-6lZn4pIABGHomV249UXAlOLZgQ4W38rWEEYhkmcq4LRXQRZJNKcVtz_ePBxDbkToUsRko1O-vENYiTD4G4pSgsqC0YbSnQAMnWDLLdGLmvOnawWKOY73AyJhV0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f197d827b8.mp4?token=dDMBkZ50yoSpTljJJcTIkYz5xgvPvot6c9bW_0ZHjG5rwNTAPSOlvI1-dnxvtRtUb8REmxP-XtOcnJ58E8e8GNHa0Fr-34UzCB5ZkizyQuCmv2-Q94vfc4PPgI9ODK_-cab-GzI7AwoaX4HnsFMLK_-l2zddG9kBnH75lKMcDO5Va7qiCudmZLJ1wI68ASFf3VFIHpSKzjA64_babvLIE1G0s7-6lZn4pIABGHomV249UXAlOLZgQ4W38rWEEYhkmcq4LRXQRZJNKcVtz_ePBxDbkToUsRko1O-vENYiTD4G4pSgsqC0YbSnQAMnWDLLdGLmvOnawWKOY73AyJhV0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دوست دارم به عروسی پسرم بروم ولی درگیر ایران هستم؛ پوستم را می‌کَنند!
🔸
خبرنگار: آخر هفته به عروسی پسرتان می‌روید؟
🔹
ترامپ: او دوست دارد که بروم اما الان اصلاً زمان مناسبی برای من نیست. من درگیر مسئله‌ای به‌نام ایران و موضوعات دیگر هستم.
🔹
این از آن موقعیت‌هایی است که در هر صورت بازنده‌ام؛ اگر شرکت کنم، پوستم را می‌کَنند (شدیداً تخریبم می‌کنند)، اگر شرکت هم نکنم، بازهم پوستم را می‌کَنند. البته مشخص است که منظورم رسانه‌های جعلی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/437104" target="_blank">📅 20:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvWcDflhYTedeTqfFB4uM2bFhJU1fOyIcf534b2oDq1gjV7GTBfsMSO6Fcsya-sJdiQwoAvmkO8mm30VPtEICK79LyD4pztMQQY0XzsiLo-THyutvnlvMXt9ecVKFcyQeIavWG2Oy2WTMwoFkaMoqb9AhaTcEL7wHlVumDn2wlHEc9QSfjZPlPxD4FU2THVBLx8BoUIUxVKTIPzyzKwZPo0r7nsM6ZcpywO0EJtjWt4nadFQMZ-6vdIydkunrr3-Gyoyle5Y678FqHY_dEPJHVYBhzpimwDJOFYXyOdqroeubKTRxOK5nAK6guTAFTXoWUjsVmTSxuKmF90PEc3sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۴۶ درصدی پیش‌بینی اروپا برای بهای نفت در سال ۲۰۲۶
🔹
کمیسیون اروپا پیش‌بینی قیمت نفت در سال ۲۰۲۶ را نسبت به تخمین‌های پیشین، ۴۶ درصد افزایش داد.
🔹
کمیسیون اروپا در گزارش «چشم‌انداز اقتصادی بهار ۲۰۲۶» خود تأکید کرده است که شوک انرژی ناشی از جنگ در خاورمیانه و بسته شدن عملی تنگهٔ هرمز، مهم‌ترین عامل این بازنگری صعودی در قیمت‌های نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/437103" target="_blank">📅 20:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0048bc4ba9.mp4?token=hIyStSrPFcqEItdPW0l7CECZ5S4k6WQfCGLNbl-8au-buhfpCIIDblYwAp8UCrWEvU84nPyvPiFTQ_4H62fxv4vaOrV-kdGKAd5kdkoQNMHUNwiAwbFKhpkKSJMMlimtETidktfcesRJl26FM1lsIEnImJN96IOzojF6s0G7PAxiL3FUGxx8IEc4Tg_eH4V1gR73b_C4k9dRRb_YNAkF1xckCgGhlrIjwQwWSb7esEs3yXqEgvBpdxUQr3etaYvqr6AbIMbhXCNY49ICoB376dRYgi1TvCuBexDLe_rlZc1Q1N8Js0MNEsYiwuvxnYB9zxaXDPtH43c3PkVLO-UC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0048bc4ba9.mp4?token=hIyStSrPFcqEItdPW0l7CECZ5S4k6WQfCGLNbl-8au-buhfpCIIDblYwAp8UCrWEvU84nPyvPiFTQ_4H62fxv4vaOrV-kdGKAd5kdkoQNMHUNwiAwbFKhpkKSJMMlimtETidktfcesRJl26FM1lsIEnImJN96IOzojF6s0G7PAxiL3FUGxx8IEc4Tg_eH4V1gR73b_C4k9dRRb_YNAkF1xckCgGhlrIjwQwWSb7esEs3yXqEgvBpdxUQr3etaYvqr6AbIMbhXCNY49ICoB376dRYgi1TvCuBexDLe_rlZc1Q1N8Js0MNEsYiwuvxnYB9zxaXDPtH43c3PkVLO-UC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس گذرنامه: طی ۸۲ روز گذشته ۱.۵ میلیون نفر به کشور بازگشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437102" target="_blank">📅 20:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khvQFDtCps6tCGHS1lGCEnBhn9GYpi_y540JRfrBb1gjcuY9yr6yZvPOVDp6IXQhL-wm2TZTXap2YdCWxAeaniz7V-tnv8DzvUbSHX8RvXHvhKHKN26-8XJuCoGjgnDuK67CGd8auIQWvNZ6q_170cuLl1VybzfJiblJZzq74RvAtvqovHSQ5esJAure6BAGx-S45ZOPU7rBPebPm9Leq8Zg8kZdrKODnZd2qqPuJEPr_OLyWvHHo6FONULHpeJImG2qcM_pfu5_0N4fD6hv343WRndo6FkAzcxaW22avlmqAWpyUSbOpWGV_szfC_dKVKnVmvYEL_rVfW7O0_4wRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/437101" target="_blank">📅 20:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437096">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awvZFuxso8szOSNmqkuDo_jjAh9T5Ay0E3b6ZE7qdfoz2WOCTcZMny6tM3QYj-KUqCRmogEeKZd4q5Zvl5hlIU-rM2CU22HtZcuyge57FoPF2yPwkb6K0LKHxAYdjwUyhZH0hk0VOrsoOaoPz8DZJa8EuMtVkU7psscN9rhCRlGUGgrfQkIB7q-JUvtquAzaMVyd3klL7EgTXd4aZt3STkk-VFsmg0ExudYbg5JzaM0SE7Wm7APwMM_tu1votnj3PE1uCi199HTbV85jDKsiOl9xwGhEEvUxTyBO6ZiTP0tz0dDMvz2Kv1WT1rXr1kqH29ulfqlAwamdxxfVVZyZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_Gj3IXJiGqtO7ZV6zRE8FP0w-UIG6vvOyiKj-czFE6a335dZqXDyEk21-abe8tUM4ngj3V0yGqLJIxbCeZyPfJnh_61exCA8W_l_0kW2V7V7_5PSRzB4Qqzk5mrF1d6v1IayO5WvJR2xzmBvQgEawhX9ydv0q2YaFv9XcI-AqHM7CWynponTXrosseKGzlSovvAYTXo6jA-teLAO-g79E4z2PUkdwP8jwCheqHnmuT5wmlO30uYTf-oUtFw82ivWu9woKiqdHiuuSlb8NyhXY1nu3o311rAt5aZFTi0iNdS_CATOUhZ5Ha8MHWZLXOi_XiF2VN6gyMSsVt0Dia9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgKw2bYHPycBW9ddgLMon6MoIUn-H6mep8VX4T5fbU--C9hNPesebKqsKDzHIJctgRjylKfVaMx1Y7JryBzqPQVE7zOHpNngqD2bQE7qmodIUBy1EpSYafoXtJ70YxGQc26akeREWNtX19XG8oMgmLlmplPnUQwQCJmqCJg0JcRQisJnyeUFT5cfHL-XTCHql9ZXEEToKx5v-TSzxxNWoPtMU_74TKNNFOOlXA0nMbRsBpiwNahLxZUhIT5nbj60xf3V9FD-m1KhHoZx-IfkW0t1DpLhjVXvKCK6bfk-Y6w2YnbtYvADjhcdzbRg62R0mZM8FDmgX8NRq82Kh2cLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtYQMLj4bVFTRRutFIvBqlePFhQGodMUEt9uYYA4uqR49MgWcqUK-WI4ZKqISEvRMEyIxaciNr1Y1x-G6OYNyQ4s5N24bGl4s3LN_u0NMDs184cG8Mxlwlv3gh33_uLhGPH0inBeVVyoIigjBliJq3pv3hDNGwyhqlQPPjqR4Obd5B5Nz9ZbJwbg6TlEFQX5XrhPw2FMlP_Mta4Q1prg0tda_gcvM1IAtRxtBfUWdE70W44IGRB6BRG3FfMBvnh4dbbbrMVbO4AK0ABn07maB4PntSHJKe-Eopu_2aun3nL3pDiIwGoNzDBunS9C3yEpL7nNNMzWNxc1ivHwk5ahnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMrauBDcPXkTDO70zL6F6WI7hzmfLLS2vQQVAtkjaW3bLj6HKlMAS0fz_11v8gk14CmP3fwKUYJKaz7_7L9guXSTg8-COjvjBXt7i1us5V74fchlml7XoMC8Go7rDY8N5Elxu2AsgFu2BOK3zPVtci9_9SmvJJawx5jTMNlDA2Zd0HJHNKjUedpRv8GN6655gFbWNshxDz3aoQxN-O45501cELDMOzuliwd3khYUhiKEezHp7Dchy3Bzu7KVy9wfC_E-yDGswEMC_8c2ftgW0ed_QbkVozoR3pjptdfDocxM_uIDGYqb3s4UhEWM39INyOkyzcvrSXngZWhTN3SQcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دومین سالگرد شهید جمهور و شهدای خدمت در حرم رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/437096" target="_blank">📅 20:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437095">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_BB9vPa8OMqv1KMSYFZK45dboQbpPLQBrsGKGsWiKt9z5uTFm_6KMBTId-zEDOnz2ZfylvCGQhVMVk_NjcOYbWSiWceeJvoLXe6FluoPufTl5gqFoZhl3M8rMojxB24jsq6STthreP-GMwE_ha1NJXf9wZ3mH0k3GjDCleSLXhF9IsNsW84ZDeZnPwsmNQaVFXwZ0cRt7kywYJPd7Ae0M8lPXx6LAVspByeDUChjjqxJoYBDKWb0CABRgXkmvhhFB9Vmi7dXgLyr6lTZrIaViUTe6LXPU1JckKF27VK6HKXsJSO0xyerRGvNlz0OLax4gzlG4W-8Mk7i2isXq37kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت الله نوری همدانی: نباید در تجمعات ذره‌ای بوی اختلاف باشد
🔹
مرجع تقلید شیعیان: باید در اجتماعات مردمی جوری عمل شود که ذره‌ای بوی اختلاف وجود نداشته باشد و فقط صدای وحدت آن هم حول نظر رهبر معظم انقلاب به گوش برسد.
🔹
ما قدردان حضور مردم هستیم و هرچه این حضور پررنگ‌تر باشد، پشتیبانی مستحکم‌تری از نظام، انقلاب و رهبری معظم شکل خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/437095" target="_blank">📅 19:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437094">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ed333922.mp4?token=jToWtXC_8VkZ64hrTRxlmCkXeWFl3m7A3Re_TzpFpZiB_tnE-F_OhiqJjle7TOFgQRe7-JzYSMxgpYpPorL5VoqbKx6BD9XwjP7VmM8buc9iBk1R-CP2qr9lvl00jvv_53yIttEhs3Q4dwVtbR10Ox2f_l4r1QZYINgUwdnyricO0_mSEWxevyNrxMX3De0DX-QTMurF5uVooaQzyz2tjrSxCXtB6Y4bAMUEyspvkHghM-XbgoX0aYaGfudr98KdXqjt_-Rka6zzmxdxtMKkjqJKSYYFc-GId5pjwk1pD5WGV9qj-MO-rO8opz8bKuK_8uNJGdirDmWdwOWl9Gh-ukydqY2170TB6kLCb6TBV4pcn-t9_g2rWfbY-fV8QMTp9wKcXo_7Deje9-B7CB4M32sk0xH1U1OhHg5Sdu6neQ479qCU_pYAfbIGHCcdePRPI8MjO0q85PM-NrMNoqmBMZKW2hosRsYc6czLHobToTs6w4gYLdFtzRjdc9IXmbqZhXR0ph6DRCHUD8EM7VgXH1a9ROmvbnbr5TigSIJWY58uGXWIqhGoSxH0I6O2qB4NM6lTKzMYwt6aIY5c9AR_IVQ8jSdFr5ji7qdvN3xTN9YEWyH5-Z6NNux2wecSRPVrjlnTc8ZDFcrOlxBygF6y7uD6HaPPPW0CMe3eP5KYOiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ed333922.mp4?token=jToWtXC_8VkZ64hrTRxlmCkXeWFl3m7A3Re_TzpFpZiB_tnE-F_OhiqJjle7TOFgQRe7-JzYSMxgpYpPorL5VoqbKx6BD9XwjP7VmM8buc9iBk1R-CP2qr9lvl00jvv_53yIttEhs3Q4dwVtbR10Ox2f_l4r1QZYINgUwdnyricO0_mSEWxevyNrxMX3De0DX-QTMurF5uVooaQzyz2tjrSxCXtB6Y4bAMUEyspvkHghM-XbgoX0aYaGfudr98KdXqjt_-Rka6zzmxdxtMKkjqJKSYYFc-GId5pjwk1pD5WGV9qj-MO-rO8opz8bKuK_8uNJGdirDmWdwOWl9Gh-ukydqY2170TB6kLCb6TBV4pcn-t9_g2rWfbY-fV8QMTp9wKcXo_7Deje9-B7CB4M32sk0xH1U1OhHg5Sdu6neQ479qCU_pYAfbIGHCcdePRPI8MjO0q85PM-NrMNoqmBMZKW2hosRsYc6czLHobToTs6w4gYLdFtzRjdc9IXmbqZhXR0ph6DRCHUD8EM7VgXH1a9ROmvbnbr5TigSIJWY58uGXWIqhGoSxH0I6O2qB4NM6lTKzMYwt6aIY5c9AR_IVQ8jSdFr5ji7qdvN3xTN9YEWyH5-Z6NNux2wecSRPVrjlnTc8ZDFcrOlxBygF6y7uD6HaPPPW0CMe3eP5KYOiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع شهیدِ خنثی‌سازی بمب‌های صهیونیستی در بروجن
🔹
شهید حمید خانی از نیروهای داوطلبی بود که هنگام عملیات خنثی‌سازی بمب‌های عمل‌نکرده دشمن به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/437094" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437092">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ پس از استقلال و پرسپولیس، مجوز حرفه‌ای تراکتور نیز صادر شد
🔹
باشگاه تراکتور با دریافت نامه‌ای از سوی فدراسیون فوتبال، مجوز حرفه‌ای برای فصل پیش رو را گرفت و می‌تواند فصل بعد در آسیا شرکت کند. @Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/437092" target="_blank">📅 19:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437091">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d05200a7.mp4?token=EXWFNBZMGORg5xAXheVb0thXq2-AQq6evEJxMg-pWaJS5bKvo30XlmuwMHhV8ROtr0-6UagcTGVwirfsjhUiSy6lshXk4swHVRjjzkiV2wfZY3aBMzbrD4VzXyJjpOPSZwM7yc7jAnXJrHf_7WgpiCc9koMjfLwDo7y2lB_uPc-VMcJCdp1xX3uPKqA8rVK3vAkyT-1DDUk8CpPEMilC-3ScqhREouqrl5QDF8Jc-DJQX0cDd7WMo_Fq_PELLoJMoqXt5MJnEi3JGMy8_YajkiHjLI7ie2Cc99tswxQPKk3gVXuGowDCriCSjMXgfWU_85Sm4RMGOw2stTOPhhQ7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d05200a7.mp4?token=EXWFNBZMGORg5xAXheVb0thXq2-AQq6evEJxMg-pWaJS5bKvo30XlmuwMHhV8ROtr0-6UagcTGVwirfsjhUiSy6lshXk4swHVRjjzkiV2wfZY3aBMzbrD4VzXyJjpOPSZwM7yc7jAnXJrHf_7WgpiCc9koMjfLwDo7y2lB_uPc-VMcJCdp1xX3uPKqA8rVK3vAkyT-1DDUk8CpPEMilC-3ScqhREouqrl5QDF8Jc-DJQX0cDd7WMo_Fq_PELLoJMoqXt5MJnEi3JGMy8_YajkiHjLI7ie2Cc99tswxQPKk3gVXuGowDCriCSjMXgfWU_85Sm4RMGOw2stTOPhhQ7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری من‌و‌تو: دنیا توجهی به ما نمی‌کند
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/437091" target="_blank">📅 19:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437090">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqMF4CMyMKGCL5XjqRBtQaxN6R652dpG1IMwy_GLmn_A4AplROi28DXl4twn4EMOd0fPCta4ya_q7DBJ-PnP8hW2O3fW6LzqBUN3i3PkTUslbtEsSX65wgjaVglvWq_gX3GR96z0QXbX5hN2ZViIxZKL1cLAM6cDAnKzneNvoVXX_0n2z61AUhcy7a6C49k7TW-O8Q34gjQ_c9g1vK4m3s2Prk3upwhoIIvrif7St7NbAU8yOWK5uyb8bYSEtnSRSee7zJ4LyP9gl9KW6PMi3wYgD7v6mUK8vzh5ZqpDOE0KuzJ8OykCZUmYwJJOL69xi0O0TOKnbuzYSUawP0JHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش حیاتی انستیتو پاستور برای منطقه در نگاه نشریهٔ پزشکی جهانی
🔹
نشریهٔ پزشکی بین‌المللی «لنست» با انتشار مقاله‌ای با عنوان «آسیب به انستیتو پاستور ایران، امنیت سلامت منطقه را تهدید می‌کند» تضعیف این نهاد را نه تنها یک مسئله ملی بلکه تهدیدی جدی برای امنیت بهداشتی کل منطقه دانسته‌است.
🔹
این مقاله با هشدار نسبت به ناتوانی در واکنش به شیوع‌های فصلی و منطقه‌ای بیماری‌ها به دلیل از دست رفتن برخی زیرساخت‌ها، از جامعهٔ جهانی سلامت درخواست کرده تا با تمام توان برای حفاظت و بازسازی کامل انستیتو پاستور ایران وارد عمل شوند.
🔹
نویسندگان این مقاله تأکید دارند که احیای ظرفیت‌های تشخیص، پایش و تولید واکسن در این مؤسسه، یک ضرورت اضطراری برای حفظ امنیت سلامت عمومی در منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/437090" target="_blank">📅 19:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437089">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3xTfC5gEMJXgHJ0PIzIuJYtPSXEiiHHaQpDzSWm3j08VPNVf45QGykzB5VfanvwkAssiAhWFYDleU1UNVb29H-QR-AyU4noOmzIwQMqhFMY2-eHN5kjW9cvJZeQpTBuOtOTspkw79hF2JWBFCLyEEnihB0KPXnYUFryC2er_IQPIDJjyYa46AlkgzGDuldrinK2aeuvZ1Ky2yGqFZP6PfIFiSi6AGyBCzaneGNILiYbUrQGagIMYdTv4-bhbWowH81ksjTqNqjnsGqvx4bb3d3iP6M2WkC62b8APTTkdDOcBpwPPWjY8IhAuHBCXm6H8sZ3iyqR-qmNbLpakUe-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردپای نمایندگی‌ها در تعیین برندگان طرح‌های فروش خودرو
🔹
در عرضهٔ اخیر ایران‌خودرو، میلیون‌ها متقاضی موفق به ثبت‌نام نشدند، زیرا کمتر از ۱۰ دقیقه پس از آغاز ثبت‌نام، خودروساز تکمیل ظرفیت را اعلام کرد.
🔹
نایب رئیس کمیسیون صنایع مجلس می‌گوید: مبالغی غیرقانونی برای ثبت‌نام افراد دریافت می‌شود و از طریق کدهای ویژه نمایندگی‌ها، «برندگان از پیش تعیین می‌شوند»؛ با این شرایط، مردم عادی در اغلب طرح‌های فروش بدون قرعه‌کشی نمی‌توانند ثبت‌نام کنند.
🔹
طهماسبی در این‌باره می‌گوید: سیستم فروش خودروسازان به‌جای تأمین نیاز بازار به ابزاری برای ایجاد انحصار و کسب منافع خاص تبدیل شده است؛ هیچ سازمان و نهاد مسئولی هم از جمله وزارت صمت، اقدامی برای جلوگیری از این‌گونه ثبت‌نام‌های غیرشفاف نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/437089" target="_blank">📅 18:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437088">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97abf2dd3c.mp4?token=QhpkyYQjSdCKAD2BjH7jTAjL3knSdGRdgN6A2Rut8SfFuKgXeINyiKaKtd1wl-b1o_QraLY9R46LMhxyh1AOas2NResAO0a_052qc03DyUeFcEXzlumkflI14JPOi6qIHkBmXAZUjbyIPP3xOJy42l48o-H1MRmH9iV5bwKM0QKobzevb3U8XUQBfEmMvi75QBlcjU5D2zTq0ABAzfoFYlA-HB9XAXneHbghHlNGhaubLDF_c3vUaf-Zg1z5IObXOus04DZOs5FTSvshNP4j6uRuFTxQoPi8OcMZHox9-ASVFIulKcxjD0oe2-AD2MgK8WDACl8w6M10G6_Rd9wceg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97abf2dd3c.mp4?token=QhpkyYQjSdCKAD2BjH7jTAjL3knSdGRdgN6A2Rut8SfFuKgXeINyiKaKtd1wl-b1o_QraLY9R46LMhxyh1AOas2NResAO0a_052qc03DyUeFcEXzlumkflI14JPOi6qIHkBmXAZUjbyIPP3xOJy42l48o-H1MRmH9iV5bwKM0QKobzevb3U8XUQBfEmMvi75QBlcjU5D2zTq0ABAzfoFYlA-HB9XAXneHbghHlNGhaubLDF_c3vUaf-Zg1z5IObXOus04DZOs5FTSvshNP4j6uRuFTxQoPi8OcMZHox9-ASVFIulKcxjD0oe2-AD2MgK8WDACl8w6M10G6_Rd9wceg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخ نمایی رنگین‌کمان در جادهٔ الموت استان قزوین
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/437088" target="_blank">📅 18:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437087">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرسپولیس هم مجوز حرفه‌ای گرفت
🔹
پرسپولیس با دریافت نامه‌ای از سوی فدراسیون فوتبال، مجوز حرفه‌ای برای فصل پیش رو گرفت.  @Sportfars</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/437087" target="_blank">📅 18:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437086">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc77674f.mp4?token=nOTW04n4SdKMyiMvy4guPnKbEgpJhz3OK5giMNmwEDSp3ZEE4899vY6YoCf32RDcSXUk27yvqj5muUSEUg5v6XQTYhb5aZvRVB5zR-hCjiNQzOFuZ22SkqZTUBPkI3pBkordnpkEv0OaB1FmdfRxYifUDI8FdoLt09nXNbr8nIbk6pBwRDRgoRDHNRdUyGwD8yjDHANjE4jhN_dwX8h1awWZ0siyW9rSHZJ14QWxCMyouH9zpgbrf0-Tw3J7611r2IaJNF3HczXoBXf15jRz67TPxjDyeL9lORr6tRhJPn7qJaMcdtzCbov357asg8O-legaCGwrxQSN3_-8OA1ZFiqoUlpMsVz38V3KS8yCR_EvCxNHz8YFUkR0EMVFzwmI3EQiD9D9u3ol0DoDcXXrjfnoJjhSbHLZDr2MRaOCcU0DtsYG9yiJtyhoYDwu9ocYCL9ejTBDEeLfMaxR_SpoKCYPaG1kQ9uhkue0yk3XEeTpHOvdlf9fGZZ8JCL6XFx3fWllK68_1WlT3vntQ2JPi7pntGjj73QdLEwJ-pDacQZIoeaLHyY5_P7n-eqc1GxDb2K9JnjUZ8kswrmNr2XYqkC52Dy4-6khELkWr_sCVxCUKVCApkyQXhf-TJ3sq4qumjryLft4PjB8k0n2jOXJLU-q--TQ6jvpo3UHH4sFKSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc77674f.mp4?token=nOTW04n4SdKMyiMvy4guPnKbEgpJhz3OK5giMNmwEDSp3ZEE4899vY6YoCf32RDcSXUk27yvqj5muUSEUg5v6XQTYhb5aZvRVB5zR-hCjiNQzOFuZ22SkqZTUBPkI3pBkordnpkEv0OaB1FmdfRxYifUDI8FdoLt09nXNbr8nIbk6pBwRDRgoRDHNRdUyGwD8yjDHANjE4jhN_dwX8h1awWZ0siyW9rSHZJ14QWxCMyouH9zpgbrf0-Tw3J7611r2IaJNF3HczXoBXf15jRz67TPxjDyeL9lORr6tRhJPn7qJaMcdtzCbov357asg8O-legaCGwrxQSN3_-8OA1ZFiqoUlpMsVz38V3KS8yCR_EvCxNHz8YFUkR0EMVFzwmI3EQiD9D9u3ol0DoDcXXrjfnoJjhSbHLZDr2MRaOCcU0DtsYG9yiJtyhoYDwu9ocYCL9ejTBDEeLfMaxR_SpoKCYPaG1kQ9uhkue0yk3XEeTpHOvdlf9fGZZ8JCL6XFx3fWllK68_1WlT3vntQ2JPi7pntGjj73QdLEwJ-pDacQZIoeaLHyY5_P7n-eqc1GxDb2K9JnjUZ8kswrmNr2XYqkC52Dy4-6khELkWr_sCVxCUKVCApkyQXhf-TJ3sq4qumjryLft4PjB8k0n2jOXJLU-q--TQ6jvpo3UHH4sFKSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آئین یادبود رهبر شهید و بیعت با رهبر انقلاب در کنیسهٔ «کترداود» اصفهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/437086" target="_blank">📅 18:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437085">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیروی دریایی سپاه: ۳۱ فروند کشتی با هماهنگی سپاه از تنگهٔ هرمز عبور کردند
🔹
روابط عمومی نیروی دریایی سپاه: طی شبانه روز گذشته ۳۱ فروند کشتی اعم از نفتکش، کانتینر بر و سایر کشتی های تجاری با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند.
🔹
علی‌رغم تجاوز ارتش تروریستی امریکا و ایجاد ناامنی بی سابقه در کل خلیج فارس و  بطور خاص تنگهٔ هرمز، نیروی دریایی سپاه تلاش نمود مسیر مشخص و ایمنی برای عبور و استمرار تجارت جهانی ایجاد نماید.
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/437085" target="_blank">📅 18:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437084">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-42.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/437084" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-41.pdf</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/437084" target="_blank">📅 18:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437083">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">پرسپولیس هم مجوز حرفه‌ای گرفت
🔹
پرسپولیس با دریافت نامه‌ای از سوی فدراسیون فوتبال، مجوز حرفه‌ای برای فصل پیش رو گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/437083" target="_blank">📅 17:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437082">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واریز سهمیهٔ اول و دوم بنزین بدون تغییر در خرداد
🔹
هر دو سهمیه ۶۰ لیتر ۱۵۰۰ تومانی و ۷۰ لیتر ۳۰۰۰ تومانی کارت‌های سوخت شخصی بدون تغییر راس ساعت ۱۲ امشب شارژ خواهد شد.
🔹
بر این اساس، در خردادماه مردم می‌توانند از سهیمهٔ کارت‌های شخصی و همچنین کارت جایگاه با نرخ ۵۰۰۰ تومان در صورت اضطرار استفاده کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/437082" target="_blank">📅 17:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437081">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
سرهنگ بازنشسته آمریکایی: ایرانی‌ها هرگز برای خواسته‌ی ترامپ، از حاکمیت و استقلال خود عقب‌نشینی نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/437081" target="_blank">📅 17:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437080">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZojmf5my-rHfOf0fuLxRSos_z4BSByWEWJLlqLTKoBa-yVUgnMdF9UpYl-syDgh9dqEX2_QDAmRAnNZ104Tnt2qKQR2BWVEx9QhscR4-w_GSdV5AWPua7bUu7anE0s1zSp5BzJlilkQhQExUQvJFlaF4uGlEkSb8ZG6A1eO1yLmd9xYJcWd_pW5GiZywtuy6nW4HEF4iytjSy3wf3D_ZIl4DWLfX-S460J_DOgZ0t5xOHnWEYb1d5IghQFmGHvt2QdljfPcLRbjxYPuG3-S7w0Qi4MPIwsG69oSnu0cA6SSTJcn3kI6tsSgclPTZf_G0M7P9PUTJxZ1_RY0H65qGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«زمانه»؛ برنامه‌ای که از دل تحولات، زبان تازه‌ای پیدا کرد
🔹
امین سلیمی، مجری برنامه «زمانه» در گفت‌وگو بافارس: زمانه قبل از جنگ ۱۲ روزه روی آنتن نبود و ما در یک استراحتی بودیم. سه و نیم صبح به من زنگ زدند و گفتند تهران مورد اصابت قرار گرفته است و بیا. من روی پله‌ها آقای آزادی را دیدم و از ۶ صبح آن روز شروع کردیم.
🔹
این یک آنتن دیگر در جنگ بود و فضای ما نیز از حالت آسایشگاهی فاصله گرفت. همچنین آنتن بیشتری داشتیم و ماه رمضان بود. در مجموع زمانه جدیدی به وجود آمد.
🔹
یک نکته‌ای که در زمانه خوب است، این است که آن چیزی که مجری می‌گوید را از پشت دوربین به او نگفته‌اند؛ زیست مجری است. یعنی من آن کتاب و شعری که می‌گویم را خوانده‌ام.
🔹
برخی اوقات به من کتاب یا محتوایی داده‌اند و من روی آنتن نگفته‌ام. حتما هماهنگی وجود دارد و سردبیر محتوا را می‌رساند، اما عمدتا بداهه گویی است.
🔗
ادامه میزگرد برنامه «زمانه» با حضور عوامل را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/437080" target="_blank">📅 17:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0d578360.mp4?token=lHhfzvNCJ3rZeIpFArrMPIOqtC1WbCds_ynDB0LAixXeaIc2PrS4nm0yRGkzuFXbiDW6YpFxoVrBizBtjZrlDKHrbb2-jXpeUG9yYXLHQPgobLjMfz0povk4vftM65TdkvsUznorYAo2I-nQ3bq0Zzk-51jFG-2bose61i7N2qsO9cz4M3Sq4cIe2bVNsA3fmCgATsYCCpuCfTLCvKRAGGWq5ALboIf2M70QalsKCik2EE_UohEXP8sdvQxvFPBQ-TUoK4pYYt3rIZlEWUePoUMmF7ngLuHATciT9wszCQ3_cYeBLsVs22I5-RDKe0TB7dp2-SjkzTChih_othnJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0d578360.mp4?token=lHhfzvNCJ3rZeIpFArrMPIOqtC1WbCds_ynDB0LAixXeaIc2PrS4nm0yRGkzuFXbiDW6YpFxoVrBizBtjZrlDKHrbb2-jXpeUG9yYXLHQPgobLjMfz0povk4vftM65TdkvsUznorYAo2I-nQ3bq0Zzk-51jFG-2bose61i7N2qsO9cz4M3Sq4cIe2bVNsA3fmCgATsYCCpuCfTLCvKRAGGWq5ALboIf2M70QalsKCik2EE_UohEXP8sdvQxvFPBQ-TUoK4pYYt3rIZlEWUePoUMmF7ngLuHATciT9wszCQ3_cYeBLsVs22I5-RDKe0TB7dp2-SjkzTChih_othnJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از پرنده کمیاب «هما» در منطقه حفاظت‌شده سبزکوه چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/437079" target="_blank">📅 17:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437078">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
حزب‌الله: تجمع خودروها و سربازان رژیم صهیونیستی در شهر رشاف با چند پهپاد هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437078" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437077">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7GfgMoNYU84NPSn1vWfmPCjaruLVdAp7STMIj0T_BjgnB7y0yUBwJTAuR6_2LDlJ61hUlanPcGYThaSXBMazzfr6SZ2n0jL2gdV_EDsseH6QmLv8S0gi9LG5rOWk-rb7b0p5sykg-aio_YAU7IGbYA6bElt2Sk_yQapqiGufj7KEw5_hP5zEWPQbjD_iS56AMpPKF1tzULpXWCQKmtHVIAiZ2iEo2ZUQkP_6Wp_wRQ6X8I4XTL_rav2JCAXgUDzwe-XMLlFEGk9g27kXPTCATwXPLElXZUdYVW6PjBZ0NjRqjEAgoeg8C8kySUOur_kWNKma-tDaY0el615vo7hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان هنوز به ۱۱۵ زائر ایرانی روادید نداده است
🔹
یک هفته دیگر مناسک حج آغاز می‌شود اما رئیس سازمان حج می‌گوید: هنوز ۱۱۵ نفر از زائران حج کشورمان اعزام نشده‌اند.
🔹
باوجود گذشت ۲ روز از پایان عملیات انتقال زائران، سازمان حج می‌گوید «طرف سعودی قول مساعد داده…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/437077" target="_blank">📅 17:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437076">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قوه‌قضائیه: مدیرمسئول خبرگزاری دولت به دادسرا احضار شد
🔹
قوه‌قضائیه اعلام کرد: درپی انتشار تصاویری از یک خانم بدون رعایت قوانین و مقررات اسلامی کشور  از سوی خبرگزاری ایرنا، مدیر مسئول این رسانه برای ارائه توضیحات به دادسرای فرهنگ و رسانه احضار شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/437076" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437075">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تشکیل پروندۀ قضایی برای یک فیلم سینمایی با محتوای غیراخلاقی
🔹
درپی انتشار فیلم سینمایی «تهران کنارت» با محتوای مغایر با عفت عمومی، پروندۀ قضایی برای دست‌اندرکاران ان تشکیل شد.
🔹
همچنین رئیس سازمان سینمایی دربارۀ صدور پروانهٔ نمایش برای این فیلم با وجود محتوای غیراخلاقی و مغایر با عفت عمومی احضار و بازخواست شد.
🔹
با دستور مرجع قضایی و نظارت وزارت ارشاد، مقرر شد محتوای غیراخلاقی از فیلم حذف و نسخۀ اصلاحی در سینماهای سراسر کشور اکران شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/437075" target="_blank">📅 16:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437074">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌ کانادا و فنلاند سفیر اسرائیل را احضار کردند
🔹
کانادا سفیر رژیم صهیونیستی را در ارتباط با ربودن و بازداشت فعالان ناوگان جهانی صمود احضار کرد.
🔹
نخست‌وزیر کانادا گفته «کانادا از قبل تحریم‌های شدیدی را علیه بن‌گویر شامل مسدود کردن دارایی‌ها و ممنوعیت سفر، در…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/437074" target="_blank">📅 16:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437073">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
موج محکومیت اهانت وزیر امنیت داخلی رژیم صهیونیستی به بازداشت‌شدگان ناوگان کمک‌رسانی به غزه  @Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/437073" target="_blank">📅 16:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjYMdG6LJxTpO-gQ81X9JtjDsBEqRzX1_tGD61l9zhN-HDGzhjiOQQWHYUEczw89f8CgVoWoa-pE4OInSPTFgCCaVVDPPD7QU43vSCz1fBQLVAcnnfbTIwQ0zESbLAtM5SYNugH0woJ4hw3fb-3KaE-NYIoFapSG2oEGIezjjrGBzNvgzpeODXiAkVhjhPuFKvxI2H0OhWAO-9J7-4sCz2SbL13yY9QhwkPOXJhmlYOKYQd_FJSuEtTG3DanfkaAUgLxLmqzX4QA3k0ujf_GzNSKsSIg8xHxSge_TQ3WzscqxjCjXdokPY6uDgwyGAP7vltMvSp9s7oVrDgfIzWvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtYsOeLmwk39lj7sNUOxFjQ9ASebFsgFuOSJuO3VA8Nn-dU3IWXql82WODk-9vbTcyy3r1wq9LHDkPzpCzqWNijRGEogUI1nTWHPKQDrUHRcFr7f71d-jZUycmD6M8q34Ny4Gnp_QWldZIW5c7JeO5MVBnPSmAFi3PQ2F0RtFHpWiptGQ2GyJ0r6D2HiXxYcX9jwnf8fobMLXPXZy0Ucu-a-blloS-iBJRgYOwQak38tRtzwZDHe1pL0QPVlkh8ELtxZ-6NJU6mHveP5F0wyBFKXJEvhzHyBF6qPV8cpKIdmZaA8VnQyrhhB071Otgza8h5M3NvfsDahj1kEzZe0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUcxlNoH2kWJCg1OwqDwwd6Maan6_EpQrTVDavFRRYuIM5zjG69hu5BmCSPVkLqPQHo41hjxbFNe_ioeGN2YjdrOn6POqNW-q2vlu8b3UwOvAhJ3TIQzrEgThshMzXPbLKEu0657rm4BOpV2PHpzlpudWcNBfJ0o_Rm1BHM3ZrcSjVs4-pZisnTtRw1aZAqVAFn7lwEISc8-ViLMc4Y2hStzGNoPco6QyzIc0m5AgfvCOhO5zCSzHKo0b2C6PpalJGGZv_U40ncm0hUFiN2PpukQZgZ9N2y21zXyrNF0p_-JxJ7moSoWJVJAPX811Gr3u5JYHk2upWuQb2diEb0Ulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMT96ZTCJTUMTIq6r2o3VdKl0bI1A1Qj9sh9XzNwy8TVukDpBpSBwUjc_5dUliuV7Y-9C6X9119SgQhxyqlNg6G8nbT8nWApS13dBot04ZFRQDg9yn7yLDvAgTMjPyQ27-vmm9rVBjHiG2WELt9CCqY5DavWcQWld5U67FL8s3rYSCONDPtyJ13gqh8fTZlxxcpXddkt74VxZxl76yxEkBbTPtpfDaTGoJpUtbYLAzR5tbfb1Ns4UbvU5J4RCqLxezV1Ao0Ag_tsiMLdgVtYJK2crE7MM_F3H9Fvt8hQjPh_UAeJ0UseeFuqrtbbJDWp6HSLdHtIqhEYP2NWa67aMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiZpmq5rSmgQVuc5ZlrURxUwqfREYyz0dhwuwzXPwpjFhb6UpydHgXYNxCgL3V6WaXrhv51p4u5OfEIV1EfxalIqAAeOrEJl2YZ6apXt5PrQaq5ryhO99Qki-L_C85DMkfvvhu67c1-PrvYUt0__azbzQQZ6WfTc4PVmR-_AKsiQmi11qR-oaBF2xonyzIFZVR3oj9tQ4CNme8vXT_nMzpikT7qc44-FRyX2F97QhUV8DDNbz9eNIUMxQof8UKJnDfq8d6fB4wUXtsJWgiG7K_Xb7ukP6nlq0S2lBDlKd0eBqjiLQUQaiHkOurq9sFeIywXa0zvWMdebc592sxJi2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند
🔹
رئیس‌جمهور در دیدار با فرمانده کل ارتش: انسجام ملی و اقتدار نیروهای مسلح مهم‌ترین پشتوانۀ امنیت کشور است. دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند.
🔹
امروز انسجام ملی، آمادگی دفاعی…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/437068" target="_blank">📅 16:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b5170e37.mp4?token=HqcAnQCdZcKYh8DwcJ-lTBhObijc24Io1sg_E-6v-qkj1lHg6l1crNNX32Ocdg_hLwmJkyRjMKLVMq2W35Utw1ITCAI5KehWXPFhvnerMDAwboJTdoi-qLIM8FvIC-zvJBLv6yVFSwYp5ffmfQfamSOesC_7V2xVMd5W6et14fKoQHdh5_3lYbEFK7IDzZTwOemoWQpLZdpA-SsSNL7Ike9s3Tvv3OLmWGCoggbhsCCTIQYFpB8qa_6u9e0jxC_SynpGaeC-Lt7kONKimzFL_QGkp69BIz7hyicxlmzaWrDcgD1s-dp0oI7aHuMM5JBQIZ1rDC_QoiDJfU0vZ0xoxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b5170e37.mp4?token=HqcAnQCdZcKYh8DwcJ-lTBhObijc24Io1sg_E-6v-qkj1lHg6l1crNNX32Ocdg_hLwmJkyRjMKLVMq2W35Utw1ITCAI5KehWXPFhvnerMDAwboJTdoi-qLIM8FvIC-zvJBLv6yVFSwYp5ffmfQfamSOesC_7V2xVMd5W6et14fKoQHdh5_3lYbEFK7IDzZTwOemoWQpLZdpA-SsSNL7Ike9s3Tvv3OLmWGCoggbhsCCTIQYFpB8qa_6u9e0jxC_SynpGaeC-Lt7kONKimzFL_QGkp69BIz7hyicxlmzaWrDcgD1s-dp0oI7aHuMM5JBQIZ1rDC_QoiDJfU0vZ0xoxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی انرژی اتمی: دانش بومی تولید رادیوداروها با هیچ تهدیدی از بین نمی‌رود و روند تولید آنها همچنان ادامه دارد
🔹
تاکنون بیش از ۱۳ هزار دُز از رادیوداروی حیاتی تشخصی و درمان سرطان پروستات به‌همت متخصصان صنعت هسته‌ای کشورمان تولید شده.
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/437067" target="_blank">📅 15:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHtWblZojHr5z4tg85LiSz7hVixAQennp5BpqjtaPyyxKsVJUrZ795fHzckAJ-rOcgJd_86mR0iGo3azgfAzrODd1AY0VPrdzHcyWDKX-HzJVVqdI8ATOJpjFyXhPiO8qxRQ1uKeyKa7AbhagOsuM-I-gUb8t32G2OEH06HuSZDN7-40D3wGhUxUEvvYCdskUOREaeTfdgZJhPsjmSogwcMwqL-YxpNlV55I0qi0tRwCbDVxLTw_1aP3_zZUtdXyyjC9hSu2Lifmux_DrUOX1Q_Grh0k5CwFowGyiQfm9R23uXvsNu6IlQRIAU_E3Ekd-VZTiG-tfklRvrbMG6iKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرمانده کل ارتش با رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/437066" target="_blank">📅 15:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3e15c830.mp4?token=ODWjPUdZqbxsmAh3qHU7sLhuKMoApl3Y5HArW1jsPXZrtVwgBqlFN9OfuY9woaYlVivQ9TUQPhbE-IBR4zb_V03mllEaIJv6lm9E6qRluyrUqGVjzgNSpF3ioeRpBNYggRUm_Say_39OyZa0HuJ9qQquZXpepK2ibdcXdFG20s0ouEaHo4bmpxvEnjVBzpxTC-v6fZDoq3L5N1_IWYc5VlZiAp7VlPjeX-_mRSQwBnzvPAtZfR-UHDoKGHVg_ipp4KoXuaL_89Iwynr9j22oZ2Rf0of96TQUagUwWPP1Vz68xSEXPWoKjF0yDZ9dvqHL4KaoKnyOuOerFcWCvPHdzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3e15c830.mp4?token=ODWjPUdZqbxsmAh3qHU7sLhuKMoApl3Y5HArW1jsPXZrtVwgBqlFN9OfuY9woaYlVivQ9TUQPhbE-IBR4zb_V03mllEaIJv6lm9E6qRluyrUqGVjzgNSpF3ioeRpBNYggRUm_Say_39OyZa0HuJ9qQquZXpepK2ibdcXdFG20s0ouEaHo4bmpxvEnjVBzpxTC-v6fZDoq3L5N1_IWYc5VlZiAp7VlPjeX-_mRSQwBnzvPAtZfR-UHDoKGHVg_ipp4KoXuaL_89Iwynr9j22oZ2Rf0of96TQUagUwWPP1Vz68xSEXPWoKjF0yDZ9dvqHL4KaoKnyOuOerFcWCvPHdzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: رئیس‌جمهور و وزرای دولت برای حل مشکلات معیشتی مردم بی‌وقفه تلاش می‌کنند
🔹
مشاور رهبر انقلاب در دیدار تولیدکنندگان و فعالان دام و طیور: همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد.
🔹
دشمن آمریکایی‌صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می‌دانیم این بخش جنگ برعهدۀ تولیدکنندگان در سنگر امنیت غذایی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/437065" target="_blank">📅 15:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcuU_-gufzF-W8BFRQZlQujG1P_Kj-HhANnnTQs8JRb7mCXnlHu4QUvLmei8RyM_dsmsxjCy7VkGEGh6p-3ESckPHfdcZj5qAAbe6bN6o8fkCMpfXQDWhLnaRf_suy43y0n6I2bpb9TXd-o9QF635l3DsaljqOFhEgzfqwcQNXnSW32FkNj5V6kOcdAi5qWSNap53Nw7nAp0rkxecDcOmoNrTOJYg0QzpRo9KQ5KbwsANa5gtB8oHqm-Q9heBsbhYr6ajkaWS1u8gq9dxttgdS6tNW6q8r5UyNzUM_m-_uZfKXUfRNUEbc6uJEL01cbhrKrCRckPiCcU7iRJ01AM4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تأکید ایرانسل و سازمان اداری و استخدامی بر توسعه سراسری فواد۱۲۸
🔸
در نشست مشترک سازمان اداری و استخدامی کشور و ایرانسل، با حضور معاون رئیس‌‌جمهوری و رئیس سازمان اداری و استخدامی کشور، مدیرعامل و جمعی از معاونان و مدیران ایرانسل، ضمن ارزیابی آخرین گزارش‌ها از عملکرد سامانه فواد۱۲۸، بر لزوم توسعه این طرح و تسریع اجرای سراسری آن تأکید شد.
🔸
مدیرعامل ایرانسل، سامانه فواد۱۲۸ را یکی از پروژه‌های مؤثر در مسیر تحول دیجیتال و اصلاح نظام اداری کشور دانست و گفت: ایرانسل این پروژه را به‌صورت کامل پشتیبانی می‌کند و آمادگی دارد با توسعه زیرساخت‌ها و خدمات مرتبط، اجرای سراسری آن را در کشور تسریع کند.
🔸
رئیس سازمان اداری و استخدامی کشور، با تأکید بر نقش مردم در اصلاح فرایندهای اداری، سامانه «فواد۱۲۸» را بستری برای شنیدن صدای شهروندان، ارتقای کیفیت خدمات و افزایش پاسخگویی در نظام اداری کشور دانست.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/437064" target="_blank">📅 15:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWoFHNPx3NHT41xFJy8Sx3m7Y71gbu8in8UBC6ngsGhsOnbwDfi-FtX0xKhGg9-rA3SS0Ax8g6yIyORYPIHW1Nzk7ntTk7t5D7xs24KuJO_PTZ4DFyy1dMTv75hbKvIJuKCIqx9doI3JaVfApZDhrs-1jb-W71dkUswikAbK5lACB72E-gThns6QmKAxTQ3o-sLlphIvXGfAltr9EGwbifVm3cCJlVe2uXSiZ5O9cvhsZfjqmphGQr0MmFaLhFYdBXUTeisr6YQ9ahJd-PbcIp5Qy7qArNkBBDsoMzjLo08NAGXWHxIpSU1YcnKlTQrTKUtrMpYrCLESTlbQ2zHNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsMOciRI_Xjjfuh6yvLSYcT_9PKBVKpFHKs1kXkEdrfELKX86PlvV9DResRnrk5TKHHyni5I221X-YoEmgBdg4M9zvmm_quB3_P30LrC3xrIPQa06nA6yggxTiKUrLVEBjRVardXKuXeMrmbT5HyTsttSQe4Czk5p99OOLwZHEymdJbn0EAFL3GK2dvK04R9jhabJjs6qSpsChFGCXhAlsX8GNVoaose_uMg3a28qCioytQdaNx4amxyF8QxQDIOHlYG1oHDoJRMeRZ171_BOPAWIHFzfz2WDzru1t1gc2TduQ3ybEkETfr78W8FBoGuK32gphacNBBtTuUW4UKtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2ezK6pD224aeVEe9u48jqURE7jxHpaiK0w6R8sc5NN9yk3ytjPVCh8D69sRoax9Q-dYsr4tFsS_QPxbcMlVGUCMCZzrf2q1HFVzjwa5qkHt3PeqD8CzE95XzSi8FndwPJlThtLQSU_RrfR7fkuZlchVi9Vao1JDE7PIOh6Hdi8ShX8yEapQCtRptqk2ZvQubNt54F4Z-7DbsGT0RHQyhr4p3na5Dpyo4vNDu-pDE7rfJTleNoLARtfaOOqD0aI-LH0tztmuVPJpdhYoGWRDpmgh-yiW_UCwVdpSUI9S5MwbbYkqUdPEzs0mZPId78bQ82FTaqaGmrfBEaiUs41BsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
رونماییِ یک سامانه بومی در شرکت ملی مس؛
🔰
مس ایران در مسیر هوشمندسازی
🔻
آیین رونماییِ «سامانه جامع تحقیق، توسعه و نوآوری» در شرکت ملی صنایع مس ایران برگزار شد؛ سامانه‌ای بومی که با هدف هوشمندسازی فرآیندهای پژوهشی، کاهش خطای انسانی و تسریع مسیر تحول دیجیتال در صنعت مس کشور طراحی و پیاده‌سازی شده‌ است.
🔸
دکتر غلامرضا ملاطاهری، معاون طرح و برنامه‌ریزی راهبردی شرکت ملی صنایع مس ایران، چهارشنبه ۳۰اردیبهشت‌ماه در آیین رونمایی این سامانه و همچنین «ماژول تجهیزات حفاظت فردی- سامانه HSE» در مجتمع مس سرچشمه، با تأکید بر جایگاه ممتاز شرکت ملی مس در صنعت کشور گفت: برای حفظ اقتدار صنعتی، باید با شتاب بیشتری به سمت هوشمندسازی حرکت کنیم و روش‌های سنتی را پشت‌سر بگذاریم.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6QN
@mespress_ir</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/437061" target="_blank">📅 15:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/437060" target="_blank">📅 15:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437059">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e85iIZgwP3-UD5gQTWrD4vkEkSdeoOsyqtzIDMiB4SYFM0a1UJxKyihNpzrWWP7JJUatvHxczSdW_zOwrX-0Gf7kErU4mKUjnhgx7nGWoS43WKA1vPwTUXB632XrY2q4CalEQDRPOnvUnafDWLIE1zoBkuGp5VG_gmmEUvcrvM2_z4Zn91XCEfl0Zqb3o9b-2SDV58rhzKo6Lf_SJNUIxK9kpNCan3Zv-usTuIk2Hm8MRE-5iyGrKmCgW0NKrqavyWi81RJgQ3dGk_CEo6R7oYCp8Z9uttansGUBFYlB_EssCvhX86S1uivfnn5n4hk6PfpxYaDcLNCa9d_G9jHm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرمانده کل ارتش با رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/437059" target="_blank">📅 15:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4def724.mp4?token=g1rF4NmPhf6PMVNkHTQuVmQHURlOG3Oz5G0NaUuSqUbGaSGXmjgFRcBAe8rQSdwD0qscOTASpOjazqEYzIhpLh6JcXHVX7wRMApV11Zxu2useV1GNoBvCbMIvo5CB6iSXCTfhuw770BDpmMAJCX1RThrszRQqZTZ6By3mPpIgMCcSSS0zzzq_xd8x2no5rIUliRiLNzZ4r6h8N7oMtRNIx5w-TSQrP00IyNmoPKZs7V10_8mhylGFmsys6L1C2VeUB1wXfswtA0NFoa4a1YSontJrheB7PXCS1X11WGHLYv9sPlq_aBJiQNqpePHUayh2OfxxfFU78VcgaCcI6-Dhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4def724.mp4?token=g1rF4NmPhf6PMVNkHTQuVmQHURlOG3Oz5G0NaUuSqUbGaSGXmjgFRcBAe8rQSdwD0qscOTASpOjazqEYzIhpLh6JcXHVX7wRMApV11Zxu2useV1GNoBvCbMIvo5CB6iSXCTfhuw770BDpmMAJCX1RThrszRQqZTZ6By3mPpIgMCcSSS0zzzq_xd8x2no5rIUliRiLNzZ4r6h8N7oMtRNIx5w-TSQrP00IyNmoPKZs7V10_8mhylGFmsys6L1C2VeUB1wXfswtA0NFoa4a1YSontJrheB7PXCS1X11WGHLYv9sPlq_aBJiQNqpePHUayh2OfxxfFU78VcgaCcI6-Dhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با ۱۲۲ تماس بگیرید و تجهیزات کاهندۀ مصرف آب دریافت کنید
🔹
با نصب تجهیزات کاهنده، میزان آب‌بها به‌طور قابل توجهی کاهش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/437058" target="_blank">📅 15:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f3aaf7f9.mp4?token=K5wUpBdOrzRnhBUXDfrOo7dQuPw2h-_L-HFF8BjU0Qhk5yAZqYfnd-O7yqLWgd_dZJLjsSl5wzAa031D3W-xKh3G0ne-zdFMr48zmd76KhF4wpBv8H3w0v1ulieitwLgg8wBWIWrst0K8lyAw-hxiYyNQn_-AC-3uiC048aUBwIs4qs05nOL02l-A9NcnkVEhjJvxmYYKqjdEN3DI935evg1bjYQ5cvYo6KxyUKAjIbRf4A9Y1DfXngZYpwbJSRY1IxW65bIl9jPVYe30uldfke0eGtFK1yx3WzLO4hwpxhQNUPBobINE87jVwvckugmLUfUvDH_3fNOD_GTJwC4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f3aaf7f9.mp4?token=K5wUpBdOrzRnhBUXDfrOo7dQuPw2h-_L-HFF8BjU0Qhk5yAZqYfnd-O7yqLWgd_dZJLjsSl5wzAa031D3W-xKh3G0ne-zdFMr48zmd76KhF4wpBv8H3w0v1ulieitwLgg8wBWIWrst0K8lyAw-hxiYyNQn_-AC-3uiC048aUBwIs4qs05nOL02l-A9NcnkVEhjJvxmYYKqjdEN3DI935evg1bjYQ5cvYo6KxyUKAjIbRf4A9Y1DfXngZYpwbJSRY1IxW65bIl9jPVYe30uldfke0eGtFK1yx3WzLO4hwpxhQNUPBobINE87jVwvckugmLUfUvDH_3fNOD_GTJwC4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ انگلیس کاردار اسرائیل را احضار کرد
🔹
انگلیس اعلام کرد که کاردار اسرائیل را به‌دلیل تصاویری که وزیر اسرائیلی از فعالان ناوگان صمود منتشر کرده و آن‌ها را درحالی که پس از توقیف کشتی‌هایشان زانو زده و دست‌وپا بسته دیده می‌شوند، مورد تمسخر قرار داده، احضار کرده…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/437057" target="_blank">📅 15:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd9663f89.mp4?token=POXz59fteX9CEBrN4HQpJ6_gwB9ll_Qmi6xHpNTk03JtVFKmEWEp8fASR5AWfasyIHihHbQz74GIhuOo49xlxAPNDoIPaaEFLziB6Dru5SO5RR8tdo3QjcbGS2wKsDpqyKDRP59HGOR5qWEtzXvwWLsmtNmPJN_XZvm2l6rdHQHZXXj55mTL3exH5I4hgHKjmptLhrEwnGqyD4SOeND4GjnddPRbNkwwFPH79uuwJ5GgD6pNdDwwSPMWEEXqwWBFbiiQwGudELplGvoPO11oI49quGXXR-jPSOp2iMOGMVO0Q2LjVS38B9MzFRUTRB8yeqgCTjpzE7ICFBRWKwqgtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd9663f89.mp4?token=POXz59fteX9CEBrN4HQpJ6_gwB9ll_Qmi6xHpNTk03JtVFKmEWEp8fASR5AWfasyIHihHbQz74GIhuOo49xlxAPNDoIPaaEFLziB6Dru5SO5RR8tdo3QjcbGS2wKsDpqyKDRP59HGOR5qWEtzXvwWLsmtNmPJN_XZvm2l6rdHQHZXXj55mTL3exH5I4hgHKjmptLhrEwnGqyD4SOeND4GjnddPRbNkwwFPH79uuwJ5GgD6pNdDwwSPMWEEXqwWBFbiiQwGudELplGvoPO11oI49quGXXR-jPSOp2iMOGMVO0Q2LjVS38B9MzFRUTRB8yeqgCTjpzE7ICFBRWKwqgtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقاضای حدود ۳۰ شناور برای عبور از تنگۀ هرمز
🔹
خبرنگار صداوسیما در تنگه هرمز: از دیشب تا الان ۳۰ مالک و کاپیتان کشتی با نیروی دریایی سپاه درحال هماهنگی برای گذشتن از تنگه هرمز هستند.
🔹
به احتمال بسیار زیاد این ۳۰ فروند امشب با هماهنگی نیروی دریای سپاه از مسیر تعیین‌شده از تنگه می‌گذرند.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/437056" target="_blank">📅 14:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4410c0cfdb.mp4?token=MWJFf6gGOXvi_q3fJ47V6XwL99E2Vi5UZPfRyRANHv9YICZsZflS0XWZa_pbLk7k1SHcODfoivPevx16gXz6hp7CJOLM_ivVYnT0LxZRi4BvyXaIKsAd9_4tiVSyj67HUuqsR7KFxcU1PYX6YE9kFuGwFCqx8jW50oxxQ18nK4JXiyvne8d7BpjagcS3_IRr6Gb-iQuZG4E2ox7Hnr40KI5Adzz0Py0T95xvZtvEqXjq8c9AeZEwmSFPBCHfT3xM_4T7TBPrqsl-l5Ph9oXyOW7IPi90645G2ozWEam6DS1lbSeICXZpvuKLd95ce6PpcqAO9KpbI21OiE5_Jje32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4410c0cfdb.mp4?token=MWJFf6gGOXvi_q3fJ47V6XwL99E2Vi5UZPfRyRANHv9YICZsZflS0XWZa_pbLk7k1SHcODfoivPevx16gXz6hp7CJOLM_ivVYnT0LxZRi4BvyXaIKsAd9_4tiVSyj67HUuqsR7KFxcU1PYX6YE9kFuGwFCqx8jW50oxxQ18nK4JXiyvne8d7BpjagcS3_IRr6Gb-iQuZG4E2ox7Hnr40KI5Adzz0Py0T95xvZtvEqXjq8c9AeZEwmSFPBCHfT3xM_4T7TBPrqsl-l5Ph9oXyOW7IPi90645G2ozWEam6DS1lbSeICXZpvuKLd95ce6PpcqAO9KpbI21OiE5_Jje32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار فرماندهان اسرائیلی یکی پس از دیگری در لبنان
🔹
یگان اطلاعاتی حزب‌الله با رصد دقیق تحرکات ارتش اشغالگر، راه را برای پهپادهای مرگبار مقاومت باز کرده تا فرماندهان میدانی دشمن را یکی پس از دیگری هدف قرار دهد. از فرمانده تیپ ۳۰۰ در شومیرا گرفته تا فرمانده…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/437055" target="_blank">📅 14:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1afce8680.mp4?token=lSM295U4-439fBDCTG3MBI_zceSgmQuKss8BUC_yis6Gd72Nj_i4X9XZYRWQgg2T167ZhSDKQNfECLKrYSb0Hj_qFcZyhBxvMEznXEW_bwfSsqTtx69UGDhezDfmn9AiKrHqRFPnjFmrjZbV1mdlztlo7vd132kE0Xzb_XdKLdf6HW7_73A0rm6UAGiLAn8I5MC-KtpvCn_OtXnrInbvJ6YKEUOt0QPA9iecWvUb43DxolMVzMrGn-sCiyS8D2SSzlXZ8CS5Lbd1ZunXvJcsP_w0I7vNcUXdWF03_zXWOQYNgmh_Z6aM194bDPQ9QUaE3nIPLQPTnq1qVomhJhwVu6eD77c7qSK_BRwqaMJz1nOja9Cl8AjkEyn7I9Lgf-3iQJlICpoJeVe1mRWnSGfpaDQe-hcXwrKko7vtzzcXGsIv8pWSaRzWsPWJAAOtCFihkDJWppad13L__X4rFM154NWsxx3mtDkcPng08XcYGwN1Ht9ZqJ8rUcrzmYzSGw9duO6hWV4NCHU_3XFYHfglufV1cWm4XXLRiCl0G6W4KuT1mnpjNV_02esV4l3FXWfNxotXysGjndw-gMEZDSZvqELqSk8Rp9Jl3QPiviZu29uBSvsq6uJTxYX04plYQjvtTrYjsSIt_HC9MWak94ZzX2Dj1-Ny33MnZWUHLktYULI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1afce8680.mp4?token=lSM295U4-439fBDCTG3MBI_zceSgmQuKss8BUC_yis6Gd72Nj_i4X9XZYRWQgg2T167ZhSDKQNfECLKrYSb0Hj_qFcZyhBxvMEznXEW_bwfSsqTtx69UGDhezDfmn9AiKrHqRFPnjFmrjZbV1mdlztlo7vd132kE0Xzb_XdKLdf6HW7_73A0rm6UAGiLAn8I5MC-KtpvCn_OtXnrInbvJ6YKEUOt0QPA9iecWvUb43DxolMVzMrGn-sCiyS8D2SSzlXZ8CS5Lbd1ZunXvJcsP_w0I7vNcUXdWF03_zXWOQYNgmh_Z6aM194bDPQ9QUaE3nIPLQPTnq1qVomhJhwVu6eD77c7qSK_BRwqaMJz1nOja9Cl8AjkEyn7I9Lgf-3iQJlICpoJeVe1mRWnSGfpaDQe-hcXwrKko7vtzzcXGsIv8pWSaRzWsPWJAAOtCFihkDJWppad13L__X4rFM154NWsxx3mtDkcPng08XcYGwN1Ht9ZqJ8rUcrzmYzSGw9duO6hWV4NCHU_3XFYHfglufV1cWm4XXLRiCl0G6W4KuT1mnpjNV_02esV4l3FXWfNxotXysGjndw-gMEZDSZvqELqSk8Rp9Jl3QPiviZu29uBSvsq6uJTxYX04plYQjvtTrYjsSIt_HC9MWak94ZzX2Dj1-Ny33MnZWUHLktYULI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار فرماندهان اسرائیلی یکی پس از دیگری در لبنان
🔹
یگان اطلاعاتی حزب‌الله با رصد دقیق تحرکات ارتش اشغالگر، راه را برای پهپادهای مرگبار مقاومت باز کرده تا فرماندهان میدانی دشمن را یکی پس از دیگری هدف قرار دهد. از فرمانده تیپ ۳۰۰ در شومیرا گرفته تا فرمانده تیپ ۴۰۱ که هنوز در کماست.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/437054" target="_blank">📅 14:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181370e43b.mp4?token=k1bZD2_7bNgxs237SUxciAiFF_yVeApk4IKBGPIqzVK5c9Ot9yy5V3DR29ndIi7FpRTh0sTK69R2_MHRYygk3AYhmfi6aR3FYoIe-CLh4qYpLpzdEh8-FrIwX8AlIj87G1kXiJX6LJ2eKPnB9ToDGRnHeFneRpgYFmxAMfv8fUXaxkLxaTPFRvNYWuOy8zgfitKNzQ8LLijp_8REulj3KP2NuReYhuZn-YBVh7fZ8CSw7ixaUKhsIGE87sGcS8tq0rYHPRUmMtVWGJ_2Ls1C681-Z1LTXLcUtqUUCaSTSl8ERcFrZG7rTa91v9JIuThxU0UArawHwJNqBEyReNfoAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181370e43b.mp4?token=k1bZD2_7bNgxs237SUxciAiFF_yVeApk4IKBGPIqzVK5c9Ot9yy5V3DR29ndIi7FpRTh0sTK69R2_MHRYygk3AYhmfi6aR3FYoIe-CLh4qYpLpzdEh8-FrIwX8AlIj87G1kXiJX6LJ2eKPnB9ToDGRnHeFneRpgYFmxAMfv8fUXaxkLxaTPFRvNYWuOy8zgfitKNzQ8LLijp_8REulj3KP2NuReYhuZn-YBVh7fZ8CSw7ixaUKhsIGE87sGcS8tq0rYHPRUmMtVWGJ_2Ls1C681-Z1LTXLcUtqUUCaSTSl8ERcFrZG7rTa91v9JIuThxU0UArawHwJNqBEyReNfoAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: اسامی اداره‌های پرمصرف برق اعلام عمومی می‌شود
🔹
در مناطق غیرگرمسیری یک ساعت قبل از تمام شدن کار باید دستگاه‌های سرمایشی خاموش شوند.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/437053" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437052">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نخست‌وزیر اسپانیا: فشار می‌آورم تا کل اروپا وزیر امنیت اسرائیل را تحریم کند
🔹
تصاویر بن‌گویر، وزیر اسرائیلی، که اعضای ناوگان بین‌المللی حمایت از غزه را تحقیر می‌کند، غیرقابل قبول است. اجازه نمی‌دهیم کسی با شهروندان ما بدرفتاری کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/437052" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0cca0ba9.mp4?token=b1vbir4xKuzN0wwXZuSXcSXyS_HX8TA6YxMsTMqs3smZ9dNNL6VTYoPm4VvD8CNorVLOvCuNOr4tv5-NWL4Y7oM0Pn5fNK7mjTNWWRm6LTW5jNS3jZU7pE3pTlTKWy2XQZNRjNaZMe0EtyYG3ZAdACKMYR7fzB_hQDyepH3kssMS1cFwbpjleiQrZpJDXHMgYhSyqZl1poqps7ff9dpIYy6uJc4EXlltJNu1C9ugyYdVQn6W00dU1H0KN2_y4amEJrYZBLEW1f0dJqI_CB6hayFTytxsFGGDnxpDOCsMTd3FFOSZ_SKBdXJcDTpLqnhKSG0b1-03jNxVwl9wEQ72tpGYwMwKEp-WeZt2YXVQO_WumFjb4QvsWYEs0BsKUo1ERLncp96ZLMnVi1Wqyg39IkojoSXYbJIVSirnz1n_6D9As3tNEZcqfDBOdmPV-0fuZaAxL7KrObQHBk0PacWYu6VsxckJU_bFkkSIp9vjzVIIRKV7sYAyFFEKcw0uXs3Vl5tl0L6rrefpNTMAmymsIfwgxyxZmRjxk4KKEfoapP3gRFNT5mLO22oz-uQAQkSPdDDr92IfxkRCc7mhGIUxPZjO-vJFIsGvweidXlNFLtc7wxZxkJo4rsnK2B3QIqcaFfNymRtGYiCraHhcUiVIg4iJ4jNatg6ordGJw1xJoks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0cca0ba9.mp4?token=b1vbir4xKuzN0wwXZuSXcSXyS_HX8TA6YxMsTMqs3smZ9dNNL6VTYoPm4VvD8CNorVLOvCuNOr4tv5-NWL4Y7oM0Pn5fNK7mjTNWWRm6LTW5jNS3jZU7pE3pTlTKWy2XQZNRjNaZMe0EtyYG3ZAdACKMYR7fzB_hQDyepH3kssMS1cFwbpjleiQrZpJDXHMgYhSyqZl1poqps7ff9dpIYy6uJc4EXlltJNu1C9ugyYdVQn6W00dU1H0KN2_y4amEJrYZBLEW1f0dJqI_CB6hayFTytxsFGGDnxpDOCsMTd3FFOSZ_SKBdXJcDTpLqnhKSG0b1-03jNxVwl9wEQ72tpGYwMwKEp-WeZt2YXVQO_WumFjb4QvsWYEs0BsKUo1ERLncp96ZLMnVi1Wqyg39IkojoSXYbJIVSirnz1n_6D9As3tNEZcqfDBOdmPV-0fuZaAxL7KrObQHBk0PacWYu6VsxckJU_bFkkSIp9vjzVIIRKV7sYAyFFEKcw0uXs3Vl5tl0L6rrefpNTMAmymsIfwgxyxZmRjxk4KKEfoapP3gRFNT5mLO22oz-uQAQkSPdDDr92IfxkRCc7mhGIUxPZjO-vJFIsGvweidXlNFLtc7wxZxkJo4rsnK2B3QIqcaFfNymRtGYiCraHhcUiVIg4iJ4jNatg6ordGJw1xJoks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلم برای رئیسی سوخت
🔹
روایتی از روزهای تلخ و پرالتهابِ عروج «شهید جمهور»؛ مروری بر روزهایی که رهبر شهید انقلاب، در قامت تکیه‌گاه یک ملت، ضمن آرامش‌بخشی به جامعه و تأکید بر اینکه «خللی در کار کشور ایجاد نمی‌شود»، با کلامی که در دل‌ها ماندگار شد از عمق یک اندوه بزرگ پرده برداشتند: «دلم برای رئیسی سوخت...»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/437051" target="_blank">📅 14:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlaiRoIfkXk2PtItiuCaIE318ZWuYbNQ4nHJr4J978NkSp3f8rFC56oPhpT3qPI_m9kJQIR4_0lPCTUI5Y_5d_3TIRHv-k05jXTrjH_wiOe25bcTMZS-rB8vrvhE43rC_kqbPzI_xasDLDaFCL2dvQ2ZN17QwPUDKH2GfHXhdkhT9IqLOA3FTBMO70KUACNDgqsdaIwwaLGQROXlgZivPZVHIDuJtOg4dTKHbCgBIuMLMvIAVxVEopzzbYjlE64Y4-XNYfrhS5nFKxtcQwCByQiCP-rIQ4O9ZJyN--eKwSiESRB3fJpQv7o1c04zmMNA8aJL81wZibXAfxrZFopqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی
وزارت خارجۀ روسیه: فقط خود ایران باید دربارۀ ذخایر اورانیومش تصمیم‌ بگیرد
🔹
مسئلۀ ایران تنها از طریق کانال‌های دیپلماتیک و با در نظر گرفتن منافع ایران قابل حل‌وفصل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/437050" target="_blank">📅 14:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437049">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjbgCtfbIC5WmcIEBsNygkFKvgN3qzCyHwVQjxhKA1FvVFwaHGnjMTh0NNyxhCdp98DIijbtTnAmLcvcH9rKbZPbTU5OuhQSZxjZDJ9mbNUcbmJu44F1q_ZxKb9B7IyeZ8lKTgk7KfAc-jfj12gUdAZVgk3sf83SHmCWgg2UcVmRldpbMSwzwNfWpbs5vOx70tXMjKy-hVjRffO03yVqdYyM07zMKe50DMFKReJyD25ToldmJDP09ylzmfCvASOoiM2Mjh-I7hxI3Jiqjk8CeQS1zOBhXmWyFTTn7ic6SrzRfKxuH8AbaX_A6_64dyYcSl4MZwCRTyU_vy-Avgn3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دومین سالگرد امیر دیپلماسی، شهید امیرعبداللهیان فردا در حرم حضرت عبدالعظیم برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/437049" target="_blank">📅 14:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437048">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b753e2edf.mp4?token=SNTbow4_KSznYmW-ESVWSLVyzHBHlUMFT-0ypt6C0VvnDXVP8UGKHlDE47LeoG1AwL6C58pVAtfmiu6b28I_BQr1CvBLN_GJmfpF3APd29hWSZ4HnkNSeVBE2eX-5jgqrInbPr_T28PLmdD1A3o5K81BSZQmAaHCLqHTsbSiyLx75sj4yLneIfR0A8fSoEOJBW8i4MgNh-TYY_0e5Y2oXQsA1MFoIOREMUr-jkMhI9rN_mZdqwMT41c4qfTKYr2T0IjPzr6h87VeTWfiAz4pWu887aPF5HKIY6jVkAe29nKpZK59hoFShzf7OwAVLtLQav_XjAtt9dhp5W3MCLKR-laLo7ArO2dSQiZGmo3sp6oWWKCzL-IkU2wQxqmvBfv2MavOhF9eexSBV7PPJS1wMywoULXh4iAE47gJ4vLKz0Nj9dtHSFfl6WQJGdzKM8Y5Ip3aRBOUZ60c8oTHGBkCZs6x_GOK068_wPbEIg3Mbzs5nDzC5V3sEQuVWWk7lAa6PllielyujfoFoQEVF4nhdiloU-jUdmuXCTD7sKUtTRQcpk1ZXOvC5qQa1qDQc1twZLzXczAqgzoKV7qlcsDQjjMhQ-GDtvRS8TLgMAvKdCVgXblSYoXiq4wdL2MmbYGJnYRN8VunKJMnilGK8l4FuLYkuJiOGlJM2lmy2cVoYVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b753e2edf.mp4?token=SNTbow4_KSznYmW-ESVWSLVyzHBHlUMFT-0ypt6C0VvnDXVP8UGKHlDE47LeoG1AwL6C58pVAtfmiu6b28I_BQr1CvBLN_GJmfpF3APd29hWSZ4HnkNSeVBE2eX-5jgqrInbPr_T28PLmdD1A3o5K81BSZQmAaHCLqHTsbSiyLx75sj4yLneIfR0A8fSoEOJBW8i4MgNh-TYY_0e5Y2oXQsA1MFoIOREMUr-jkMhI9rN_mZdqwMT41c4qfTKYr2T0IjPzr6h87VeTWfiAz4pWu887aPF5HKIY6jVkAe29nKpZK59hoFShzf7OwAVLtLQav_XjAtt9dhp5W3MCLKR-laLo7ArO2dSQiZGmo3sp6oWWKCzL-IkU2wQxqmvBfv2MavOhF9eexSBV7PPJS1wMywoULXh4iAE47gJ4vLKz0Nj9dtHSFfl6WQJGdzKM8Y5Ip3aRBOUZ60c8oTHGBkCZs6x_GOK068_wPbEIg3Mbzs5nDzC5V3sEQuVWWk7lAa6PllielyujfoFoQEVF4nhdiloU-jUdmuXCTD7sKUtTRQcpk1ZXOvC5qQa1qDQc1twZLzXczAqgzoKV7qlcsDQjjMhQ-GDtvRS8TLgMAvKdCVgXblSYoXiq4wdL2MmbYGJnYRN8VunKJMnilGK8l4FuLYkuJiOGlJM2lmy2cVoYVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلیمی در ثانیه پایانی طلایی شد
🥇
آرین سلیمی در فینال وزن  ۸۴+ کیلوگرم تکواندوی قهرمانی آسیا مقابل رقیب ازبکستانی برنده شد و طلا گرفت.
📊
نتیجه:
راند اول: ۷-۷ برنده ازبکستان
راند دوم: ۶-۳ برنده سلیمی
راند سوم: ۱۲-۱۰ برنده سلیمی
@Sportfars</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/437048" target="_blank">📅 14:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0XUxC2zFZ2pN_Y6ERClZvGr9y2K1sYo8AN9rOmL0vkksnH03uFuaL_wGhCNkB7QD5E6ekHC3SMigZmuF92dGDzXTy217LqIryNPV8lfDuqhjCoj5N578J-v60_1A3t8KwZSG1Qn-jqg_vq4kFCVBV1WwarE07tbOs1is5-DPxggQBDk5Co-T1rBMLbznxJFRwDilxRyEOU0e1DgEl5g8hGrGpT_gvhsn-tM0QbibXIAoi8YB6fR3KnA4K-fKFCBjzpyknI_QAidoW27OFw0-_0JVoyv5FABbL3WLNG58gSHafdLltfzAIHLk503DJnGvbX7orrqRIykybvhlWnlcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: نقشۀ کریدورهای منطقه را با واقعیت‌های میدانی تهران می‌نویسند
🔹
مشاور رهبر انقلاب در امور بین‌الملل: ترامپ در پارادوکس «تهدیدهای روزانۀ ایران» و «مشتریان عصبانی پمپ‌بنزین‌های آمریکا» گرفتار شده؛ او برای مهار تورم داخلی خود محتاج ثبات بازار و کاهش قیمت انرژی است.
🔹
از سوی دیگر، تغییر محاسبات در قفقاز و کمرنگ شدن واژه تحمیلی «کریدور ترامپ»(زنگزور)، نشان داد که اکنون نقشۀ کریدورهای (راهگذرهای ) منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/437046" target="_blank">📅 13:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA2ln2zGaDEURqlox4jhYRiB-NPl-8lBEZvTRpkLK804cugsBsxtfUUguzUuBYNhY2CIbT8Kp4QpqlYMMLTy7CqLOMgx96oM8q-nuRexEUCP_WnkirNdPH6ubPD4FCSqrI3ZIyg8xPNkC_t9V-IAPgI_IbvlMln9AXGFybNGyTTO9xkB2nCuUvZvWMnWEsrf0ceFAIYLpKpDwqZysCpz0ifgIp82O-6yatFIPqkXFtF53fhOyUJwZ9elSao_sgkzb2tvWPsiMklZgro41tFPbhPw8A0VjgK5zE-gWa-EuH1QKS-pOAGoJY0JoODxsYdeP3XhRznkBfdeiI9OnJv_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437045" target="_blank">📅 13:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9ab1c59.mp4?token=qiycEJ9bZjEizalzD_rpEsdamRZTAzlPnmcfSMNQCrjOQWvewC40slralMBr35HWrASOuwdXq9hMIL38sCcfyhjqvx9jYkC24qQ0h__dEr1QFKcRHT0rpVOlgffYNDnLOrWausMz82KynsmIN2u_P3pukxg_I9ThjAeOpX3niez-c-gDEz5XvG3DC7FY-bUTKzUj3h4jKrr5c5sadY4cmmm_WwbGMEIyvP2fcBCwK9ZJqucraRFYgrFb7oEcHpugk4s2FJJs_qi4EL97H0InV1ATjg-YBPKwwCvEntogOHyJ6xvSmL3yUuf5SLzIs6wCqrlb67i8UisqNrZsTqWpIqVVIVsXM9RrpeDJsDYJGWgLHtSVJCE0byL6zLm6bQl5-iHSqR3BURIlDc4O0AGy_CFHz2_81kwLLEgizmaBr_TFXNFvebWzRpGe23XzFSKwLkKg3VU6t2Och8ToJCqfiBid1Z5Lf-CTHLC8LrN73_SaEpptz7Xa4fZWwW-zksVEbLJWhVIcd6gmuV9YETRyD03WWZXX6JYLQsPHu4fRKBLWGd60MHYNaMFpBe-WC_4-_fa913Cq6eQDV9IDJbROqBnFbZjHysI3tSFvSAu6hZw57xTnZCgiaZrBW3bI_ZCUSn-H5Hlj1JqKf9h1uf4tqa7bwrMq5G-o6jRQGS5K-Pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9ab1c59.mp4?token=qiycEJ9bZjEizalzD_rpEsdamRZTAzlPnmcfSMNQCrjOQWvewC40slralMBr35HWrASOuwdXq9hMIL38sCcfyhjqvx9jYkC24qQ0h__dEr1QFKcRHT0rpVOlgffYNDnLOrWausMz82KynsmIN2u_P3pukxg_I9ThjAeOpX3niez-c-gDEz5XvG3DC7FY-bUTKzUj3h4jKrr5c5sadY4cmmm_WwbGMEIyvP2fcBCwK9ZJqucraRFYgrFb7oEcHpugk4s2FJJs_qi4EL97H0InV1ATjg-YBPKwwCvEntogOHyJ6xvSmL3yUuf5SLzIs6wCqrlb67i8UisqNrZsTqWpIqVVIVsXM9RrpeDJsDYJGWgLHtSVJCE0byL6zLm6bQl5-iHSqR3BURIlDc4O0AGy_CFHz2_81kwLLEgizmaBr_TFXNFvebWzRpGe23XzFSKwLkKg3VU6t2Och8ToJCqfiBid1Z5Lf-CTHLC8LrN73_SaEpptz7Xa4fZWwW-zksVEbLJWhVIcd6gmuV9YETRyD03WWZXX6JYLQsPHu4fRKBLWGd60MHYNaMFpBe-WC_4-_fa913Cq6eQDV9IDJbROqBnFbZjHysI3tSFvSAu6hZw57xTnZCgiaZrBW3bI_ZCUSn-H5Hlj1JqKf9h1uf4tqa7bwrMq5G-o6jRQGS5K-Pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درس غیرت کارگر ایرانی به رضا پهلوی و وطن‌فروشان
اعتراف مهم رضا پهلوی و مشاورش: ما بودیم که تحریم‌های شدید اقتصادی ایران را درخواست کردیم. این تحریم‌ها دامن مردم را نیز خواهد گرفت.
@Fars_plus</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437044" target="_blank">📅 13:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqarlO48sO1T-QbNqdWMt6jU046sORTICrH0-2U7FdLb3NdukCjzC33hlk4PIcIjljCkhDEcAXx1Wt5Uu2ktpDqA6QhSWtxeyHDt47m1ON0VUJc9v5JM6W7Qcr6Q52BRr39DJHVCdlhOng7PZAKrwKxGmSMJlCwzDH0o3lA8VycAYIVht2s4QfsuRTQdy4nDeQep5WqY1oJI75Nx8Z3XrThwRfsYGgooPj8-DJZf6YCAPNo56jUnMperJKo11BquYBxAD70KtW2oePtAh0FQLODH6LQu_LGEn7Mri-V0SpbpRW6XjAQ_3lyUdt_Tt7NL-PZMWu7gj0g2hh5bUAd0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
بانک رفاه کارگران و صندوق بازنشستگی کشوری تفاهم‌نامه همکاری امضا کردند*
🔹️
با هدف تامین مالی طرح‌های توسعه‌ای و سرمایه در گردش شرکت‌های زیرمجموعه صندوق بازنشستگی کشوری، تفاهم‌نامه همکاری بانک رفاه کارگران و این صندوق امضاء شد.
🔹️
این تفاهم‌نامه طی مراسمی که به همین منظور در محل بانک برگزار شد، به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران و دکتر ازوجی مدیرعامل صندوق رسید.
🔹️
دکتر اسماعیل للـه‌گانی، مدیرعامل بانک رفاه کارگران طی سخنانی در این مراسم که با حضور جمعی از مدیران دو مجموعه برگزار شد، بر ضرورت استفاده از ابزارهای نوین بانکی برای تامین مالی طرح‌های اجرایی و پروژه‌های توسعه‌ای صندوق تاکید کرد.
🔹️
دکتر ازوجی نیز طی سخنانی در این نشست با قدردانی از حمایت‌های بانک رفاه کارگران تاکید کرد: ضرورت دارد همکاری‌های متقابل صندوق بازنشستگی کشوری و بانک افزایش یابد و این مهم با جدیت بسیار در دستور کار صندوق است.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/437043" target="_blank">📅 13:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue2KYqs2Uf2ZBDeCR1D4LLmlse6v07HjlJjgJ2UkQsBKkzbu7NntvSAw5eW9UOOsTMJYyYCpXlJbIenXCzOF1Awp9w7IXzQ4DHpoewDaZkoa8DXCXdiJLcgFmn13lr4FcuAmtvNry07idDhi_87u4srVmGZnSGzxpTPPdlnCcfkHNoZiBfAa0TuDTFGDrb4IoYJnvMMxdl8cAiyTpt37q-vfcq9Jcm5yyGxTpX1AE4pFGrYW6XAcGdAsYMLGksEy_SHMr09mNDaLoaGyIM4BMCEjReezY0SQez94Mhll5IvZuvc135DN78dX8a79DltzwW__ASN4f7Fqx3_b23RhGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/437042" target="_blank">📅 13:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/437041" target="_blank">📅 13:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4492e1f20e.mp4?token=dQvtbbkpBX0ilEyJiJiGvRaPiUKJQEJFKG8s5_bx2SoTVfOST56--xXYBIZ4Aw42ncyPuoYgio0joowHWNVW6fVM6Dnj6Sfz0gFHni7RJaH2fTxb25rXi21ZKDdu4oIX4fV4eOd-kDThCpvPmS-6RDVd9lgGUhdly5rQLfEg_iVkosOk2CwX1-N5zuu4IdBNxJhqgFYZWpKzWjiGcwfb6oVYCe-_5eczCdGSDU1Zq11z3MOoxOHi18Ly3Kp9ipS1Re8Qjb1qTFXyOQAJQ6HJigg32ZEYL8AHG_zh0NlOdV2tk8vSQYr6cTbJ6dW1w2absOqyfdW1XWQZXMwlTr7CWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4492e1f20e.mp4?token=dQvtbbkpBX0ilEyJiJiGvRaPiUKJQEJFKG8s5_bx2SoTVfOST56--xXYBIZ4Aw42ncyPuoYgio0joowHWNVW6fVM6Dnj6Sfz0gFHni7RJaH2fTxb25rXi21ZKDdu4oIX4fV4eOd-kDThCpvPmS-6RDVd9lgGUhdly5rQLfEg_iVkosOk2CwX1-N5zuu4IdBNxJhqgFYZWpKzWjiGcwfb6oVYCe-_5eczCdGSDU1Zq11z3MOoxOHi18Ly3Kp9ipS1Re8Qjb1qTFXyOQAJQ6HJigg32ZEYL8AHG_zh0NlOdV2tk8vSQYr6cTbJ6dW1w2absOqyfdW1XWQZXMwlTr7CWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی وزنه‌بردار ایران
🔹
علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی، ضمن شکستن رکورد دوضرب جهان، مدال طلای دوضرب، برنز یک‌ضرب و نقرۀ مجموع مسابقات قهرمانی آسیا را کسب کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/437040" target="_blank">📅 12:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9edae61e8.mp4?token=Bv8G_jayRlaWuhfPYjbqPDcxKGfibnQNztua4Y-EHDGKZpo6r0GIpfXR7ijAey-dIiCvfa2_vosLgXQXQ48vHnwPKQBtMK0YO16YD9jiN2H4aHRsWdlxYrJhBEgovv3JIW3U-4ZrtsdGDsF9RbtYVNhTb0GXgZRBRBB6Nn1znFT1Yju2e772VMpkbj41bIvWPvHhaP5hZBb_-4na4Kz6aC_ZN6dNGlv6_DESzIK_PUDD53-t06Z8dZqbPlr3TK0VkplSXR0HDw04lpfZDI9TKV466IcRi8bBqpH2fofyYAUhgdq_ma8k6zU_y6j2t86KVyuheLpO6fDDfq59wwHJ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9edae61e8.mp4?token=Bv8G_jayRlaWuhfPYjbqPDcxKGfibnQNztua4Y-EHDGKZpo6r0GIpfXR7ijAey-dIiCvfa2_vosLgXQXQ48vHnwPKQBtMK0YO16YD9jiN2H4aHRsWdlxYrJhBEgovv3JIW3U-4ZrtsdGDsF9RbtYVNhTb0GXgZRBRBB6Nn1znFT1Yju2e772VMpkbj41bIvWPvHhaP5hZBb_-4na4Kz6aC_ZN6dNGlv6_DESzIK_PUDD53-t06Z8dZqbPlr3TK0VkplSXR0HDw04lpfZDI9TKV466IcRi8bBqpH2fofyYAUhgdq_ma8k6zU_y6j2t86KVyuheLpO6fDDfq59wwHJ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت محسن منصوری از نصیحت شهید رئیسی به الهام علی‌اف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/437039" target="_blank">📅 12:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پاکستان: آماده‌ایم تا ایمنی بازگشت ملوانان ایرانی از طریق پاکستان را فراهم کنیم
🔹
وزیر خارجه پاکستان: از سنگاپور درخواست حمایت در تسهیل رفاه و بازگشت ۱۱ ملوان پاکستانی و ۲۰ ملوان ایرانی، که سوار بر کشتی‌های توقیف شده توسط مقامات آمریکایی، در نزدیکی آب‌های…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/437038" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDAex0t4_h5U-X7NqNwoNMYQ12MsBH2-PEYtaMF2IMJlKxr0mXS1GnjlYBqrIbZBeC2jxQwpaC9EjkWIt9l5Z62-ptIdXcZZOV-K_zD630FJmPqH8vE9ojXc3pNECJlDqT3LY6fyzJkBQpQcWyMINqxSeald1QSc3Mk8QWlCFP77yX5t-U0WmrL304BkvlFdiIB3F9yuCayAODuFN2CHg8nA6Dh2pNgUkIEkysVVRI3lEpiceOhMXXse8gIwjfnjxSaWWCTOl4NX7oXbl0vOS0dogTSspph7INM9-LiwdvxTzNzkg8vhumOfgTLgLzpRiFXzEUwE1dDhlLG6IscwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/437037" target="_blank">📅 12:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj4w-2gcI03Pp0GvRVKQr3xRjvRLEE8gXGpHrnzQkSKUDSophvMAiKkSus3cy1LMrJ372aXZU1HKCuSYJxtmUSPu0FS_IGv9CS9Bu602_Plos0de56vy2U8xPDMXwHkIQGH1MZF1cFQ_3BMKoDWKUcjOldYiL5kIkyVOZZgDSUJIiWpTRNMqA8o5weRdLceKjIn-Vx_D0OTn4PEpSMlXsdxpvFW-9sqovO7FZEpqCgBlZ6Hr05K12mrOwurKt74HhWk1tStMoHpKVpVE54wh2M5lG8tQPRzXJa4sOGAz9jI8RiE-zFfGoFQpNmCI2KjYXT7-vmjSvs_7UVUPnDJ0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بچه‌ها استودیوی شبکه سه را به آتش کشیدند
🔹
روایت شیرینِ مادری که ۶ فرزند دارد از اتفاقاتی که در بستر این خانوادۀ زیبا رخ می‌دهد.
🔹
نام فرزند آیندۀ خودتان را به ۳۰۰۰۱۲۱۳ بفرستید و در قرعه‌کشی سفر به کربلا و مشهد شرکت کنید.  @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/437036" target="_blank">📅 12:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1z6XGJ6HSx9bsahWxY_rw5yL8rnleaBQ86YDa0T06RqjzZygRiDE1TDGnR0daOJY5pwoBVMxl0H36OCbjaBvs5y00IAQyd-DggNtVaGjuJqF9hVxYvT5NPfvcBhjHn0Ox_TVbxrfjFvJU_dOkXydldc7csVXGzF_tC8xenLtkb3OcyxrCIQmZBz0A4xZ_9QbBdlT9w1bYrYgEKvlmwsYMp80SBu4QQEhIylCmy3VauZe9lpKzaoZAWX2AtZPQHtcoCC_BDTAOG2EC3gLQrvczFVkW8g-1vAnie8Q0q-ZJbMYwClrGav4VnqiYX2TrWmJ_PQvKUpLeByrJk7kf5XFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آخرین وضعیت پروندۀ شهادت آرمان علی‌وردی
🔹
سخنگوی قوه‌قضائیه: پروندۀ شهادت علی‌وردی پس از نقض رای دیوان عالی کشور به دادگاه کیفری بازگشته و هم‌اکنون در حال رسیدگی برای رفع نقص است.
🔹
مطابق مادۀ ۲۴۲ قانون آیین دادرسی کیفری، در صورتی که بازداشت متهم ادامه یابد،…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/437034" target="_blank">📅 12:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437033">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-N1Vn2nNm0KzH-7n_il1zMlGAY8zgUmkgi3epn1U4tJiMhtbDhIc1m5rTeOAzIvzfkW6czLErwO4R6Mr-LjLFTaY0rCNx2U2FIIEz3CvSo4Yt2rCFa7q9hQlhvtI1UiGSVhhv3DOzP0Mqqlj6Mc51_hrCWXjRhgZKzjDNjIkp6TNGWxnmCnkxMsrxvpHNiZhtzJqShDOufUNEgzTp3BpKjFl6g5BB6rttSgTMa2r9EDwz2vheJSoywlTxmD9LIcMy8Nt0fUhZ7K4CeAjWO9rsUbymPI7r6YU75lPYArcv_FKt0vMIkNdT6CXFQi475pbwCeiEgdLST_V6A22_vkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی توان نظامی‌‌اش است
🔹
به گزارش سی‌ان‌ان،‌ ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس شش هفته‌ای که از اوایل آوریل آغاز شد، بخشی از تولید پهپادی خود را از سر گرفته که نشان می‌دهد به سرعت در حال بازسازی برخی از قابلیت‌های نظامی تضعیف‌شده‌اش در اثر حملات ایالات متحده و اسرائیل است» این بخشی از گزارش امروز سی‌ان‌ان به استناد اظهارات «دو منبع مطلع از ارزیابی‌های اطلاعاتی ایالات متحده» است.
🔹
طبق این گزارش به نقل از چهار منبع آگاه، «بازسازی توانایی‌های نظامی، از جمله جایگزینی سایت‌های موشکی، سامانه‌های پرتاب و ظرفیت تولید سیستم‌های تسلیحاتی کلیدی که در جریان جنگ نابود شدند، به این معنی است که اگر آمریکا بمباران را از سر بگیرد، ایران همچنان تهدیدی قابل توجه برای متحدان منطقه‌ای واشنگتن است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/437033" target="_blank">📅 11:28 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
