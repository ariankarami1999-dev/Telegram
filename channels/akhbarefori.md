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
<img src="https://cdn4.telesco.pe/file/JdMi9JV36DLpvEf5klHmupy0B3KUsp23BwKuBSo41U1KuiIAeOhyqPkeuzOydAcadUH9EbnNWkatbZbTHcSWhsD6OiKckGFcgdD2tTB4oOQCdxC5vL_8xBvkcsatyjQb54IV5E1sUUFvNlYqjl6X5T2jJ63jTG9PlC_tmLOvFM7nbPqEGtUApSw8v_fLZ02MQJUp_dqBkW79UI22_HcM4vR-6inq-0JDjDWDuFvtnbH5J5x-IuXYZrv7FK5Uc1ITRinyVRdJ8mmCgzc3aH9Ilqs2lZpv_MEg36nOiVwBLDX3xA7ObZ8KgNF0INAkKeRHxWtJrprEbyILGmcalMuOWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-656044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
مبلغ جدید وام فرزندآوری از فرزند اول تا پنجم چقدر است؟
🔹
مبلغ تسهیلات برای فرزند اول ۴۴ میلیون تومان با دوره بازپرداخت ۳۶ ماهه تعیین شده است، این رقم برای فرزند دوم ۸۸ میلیون تومان با بازپرداخت ۴۸ ماهه، برای فرزند سوم ۱۳۲ میلیون تومان با بازپرداخت ۶۰ ماهه، برای فرزند چهارم ۱۶۵ میلیون تومان با بازپرداخت ۷۲ ماهه و برای فرزند پنجم و بیشتر ۲۲۰ میلیون تومان با دوره بازپرداخت ۸۴ ماهه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/akhbarefori/656044" target="_blank">📅 13:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZeZJK8FeRCZURIVNBTs7um9970CKMrnWFJE50bzfLmE2hG6opwh8SY0aAnZtXpTZkYoesJpEfhdBiinhLFcDe38vrRHS5oae2nBJk57F7nhrRG13hH6Cj-j74BTL8XfFXnQOOMMEyddJ3hNIh6e7pahMO8GLaNst_J-x04hQjZBd4ARM5LB34F8wguOucFjYWOjKGEZobZ6uVRPtLG96OQsRmtmgOA7LQovSTSxRK5M5n-aUvD8BisRYNF3NUVNipcekpF7dELLdD_VSj20OWecJA_Ywrs2_OZfq172D_jtOyFNgQRgPxdXOv8Zrk9Vl8A2eZfGx9T60NeEfGqWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز اعلام ولایت
🔹
هر کس من مولای اویم، علی مولای اوست، این جمله در میان جمعیتی عظیم طنین‌انداز شد و یکی از ماندگارترین رویدادهای تاریخ اسلام را رقم زد. #روایت_غدیر #فقط_به_عشق_علی #LiveLikeAli #VoiceOfAli
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/656043" target="_blank">📅 13:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN0X85uKoGOJqzYzcpmbyz3Ydxr9CVF7GTAW2DRQoKBDVC3SLFk3-_bUvixGAJhvXgIt0Fu8QVryxP5TMhuYBCroVZEirOenmyoTcmmPeQ3fmWP10QBV-ddkOpIZpt2KaJGCbkrDeVIIQqhYCyVa0Pl86nZY9PSAuI3U8sd5cWy2GT6lIUQUR6E-PQUv8pdEx_ws28w8LT9HDv0FYYuJpnL5-w8H7RUi-8Zk5pizyEzH6SUkNPpXOh0qz6ONyVFGjHo-08D-UFNgqolYzmWjdIMBgnI9IF8jEF3DWrr0-06xLX_QlInKVZkjP0PT-Rbp4_lRAWUjYOvxCDZbrYVflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
📲
‌
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/656042" target="_blank">📅 13:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mohsen Chavoshi</div>
  <div class="tg-doc-extra">Ali</div>
</div>
<a href="https://t.me/akhbarefori/656041" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">علی آن دلیل رحمت، علی آن چراغ ایمان
علی آن که می‌درخشد به دل همه دوران
به ولای او قسم خورده خدا به روز محشر
که بود علی حقیقت، به یقین ره‌گشای جان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/656041" target="_blank">📅 13:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خسارات جنگ بر نظام سلامت؛ ۳۸۵ مرکز خدمات سلامت دچار حادثه شدند
حسین کرمانپور، مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
۶۳ مرکز بیمارستانی، ۵۶ پایگاه اورژانس پیش بیمارستانی و ۶۴ آمبولانس در طول جنگ آسیب دیدند.
🔹
از بین آمبولانس‌های آسیب دیده، بیش از ۱۰ تا ۱۵ آمبولانس نتوانستند به چرخه بازگردند. همچنین دو آمبولانس هوایی منهدم شد و دو آمبولانس دریایی نیز دچار حادثه شد.
🔹
هر آمبولانس ما که از رده خارج می شود بالغ بر ۱۷ تا ۱۸ میلیارد تومان هزینه دارد. ۳۸۵ مرکز خدمات سلامت معروف به مراکز جامع بهداشتی دچار حادثه شدند.
🔹
۷۱۸ نفر از همکاران ما دچار حوادث مجروحیت شدند و تقریبا ۵۲ نفر از همکاران ما در طی دو جنگ شهید شدند که ۲۷ نفر از آنها در جنگ اخیر به شهادت رسیدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/656040" target="_blank">📅 13:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
آکسیوس مدعی شد: دو مقام ارشد آمریکایی گفتند که در حالی که ترامپ می‌خواهد به جنگ پایان دهد، به نظر می‌رسد نتانیاهو می‌خواهد آن را از سر بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/656039" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656038">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53de2848c.mp4?token=UsqLKYsbl9FR_Fe0TdnEG6Cw1pCAbeZ-aNNDGBCw6t08Pf7GD4CEGeikm65UVyzre_PTXJ_wDH6DWnP8YAd9GaIjDfBqlJbKJBbwnBeAH2e1G5r5SCHK__tOu83T1KInc6ghGjLRhCgRJgwXJRKxxJCvcdV9lo7XnqQ-KvnJdFGRQIBXVYhj5KkgGB3BA_77zPXxCBfiZOC1JnBP4FfVzCwmq7cDFJngCnGZNlqtwsChOzsJBMHchkZa03oyFweuv958VNTVkETWnSAH65d1NyDto6Dqya6wqEoASjJWi9eaSg1mNnVDaCTBJlUmX5BU_ZNccs48f6pt65UZIsQ1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53de2848c.mp4?token=UsqLKYsbl9FR_Fe0TdnEG6Cw1pCAbeZ-aNNDGBCw6t08Pf7GD4CEGeikm65UVyzre_PTXJ_wDH6DWnP8YAd9GaIjDfBqlJbKJBbwnBeAH2e1G5r5SCHK__tOu83T1KInc6ghGjLRhCgRJgwXJRKxxJCvcdV9lo7XnqQ-KvnJdFGRQIBXVYhj5KkgGB3BA_77zPXxCBfiZOC1JnBP4FfVzCwmq7cDFJngCnGZNlqtwsChOzsJBMHchkZa03oyFweuv958VNTVkETWnSAH65d1NyDto6Dqya6wqEoASjJWi9eaSg1mNnVDaCTBJlUmX5BU_ZNccs48f6pt65UZIsQ1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی جدید از حمله هوایی به پل B1 کرج در جنگ رمضان
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/656038" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656037">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bea3aba.mp4?token=Zysbts1kQ1Jp1WaAd3nlKScTKmKI4wOfrW9-8Ds8b6vKzsvHQ-co4XUveStl662g8abPjS0aaugwHFHDkVGQPMY-9m8AHPG8w_493jnSE8LGEvnF3h3Jm1yfV9L74nbVtHg0kxa3aU7I6mYfdzcfJn095Tav08QD5J2RbS7bD-8siSzQnwwOqX6v-WiCLjTaR3KEbhOAcjlAArv6GuzK7z4TtHzfPSTtcDG-uIdCL1hZ429JF0mbMtprTqQd-CBozkWggtuaDZktvsmJsiYwNxXQqQBlHbu7KAWYqEM0SHeFJNx0WkfCwboqLI9BaCsD0M9ExBrKR-fCVpT8tZIhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bea3aba.mp4?token=Zysbts1kQ1Jp1WaAd3nlKScTKmKI4wOfrW9-8Ds8b6vKzsvHQ-co4XUveStl662g8abPjS0aaugwHFHDkVGQPMY-9m8AHPG8w_493jnSE8LGEvnF3h3Jm1yfV9L74nbVtHg0kxa3aU7I6mYfdzcfJn095Tav08QD5J2RbS7bD-8siSzQnwwOqX6v-WiCLjTaR3KEbhOAcjlAArv6GuzK7z4TtHzfPSTtcDG-uIdCL1hZ429JF0mbMtprTqQd-CBozkWggtuaDZktvsmJsiYwNxXQqQBlHbu7KAWYqEM0SHeFJNx0WkfCwboqLI9BaCsD0M9ExBrKR-fCVpT8tZIhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی‌که ۲ تا دست میره بالا، ولی نه به نشانه‌ تسلیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/656037" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656036">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پیام تبریک سخنگوی وزارت خارجه به مناسبت عید غدیر
اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی به مناسبت عید سعید غدیر خم این عید را تبریک گفت و حدیثی از حضرت امیرالمؤمنین علی(ع) را به اشتراک گذاشت:
🔹
«اَلْعامِلُ بِالظُّلْمِ وَ المُعینُ عَلَیْهِ وَ الرّاضِیُ بِهِ شُرَکاءُ ثَلاثَهٌ»؛ یعنی ستمکار، یاری‌دهنده ظلم و کسی که به ظلم رضایت می‌دهد، هر سه در آن شریک‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/656036" target="_blank">📅 13:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای العربیه: مذاکرات آزادسازی بخشی از دارایی‌های ایران به مراحل پایانی نزدیک شده است
🔹
مذاکرات برای دستیابی به توافق درباره آزادسازی بخشی از دارایی‌های مسدودشده ایران به مراحل پایانی نزدیک شده است.
🔹
رایزنی‌ها درباره سازوکار آزادسازی این دارایی‌ها همچنان ادامه دارد و مهم‌ترین مانع فعلی، نحوه مدیریت و استفاده از این اموال عنوان شده است.
🔹
همچنین پیشنهاد تشکیل یک «صندوق ویژه» برای واریز و نگهداری دارایی‌های آزادشده ایران تحت نظارت مشخص، در حال بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/656035" target="_blank">📅 13:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تکذیب اعلام برنامه امتحانات نهایی
روابط عمومی وزارت آموزش و پرورش:
🔹
جدولی که تحت عنوان برنامه امتحانات نهایی تیر و مردادماه با امضای رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش در فضای مجازی منتشر شده است، صحت ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656034" target="_blank">📅 13:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFmj6uIwVw5ZU3NNStGa97MmiCnNNldl85Vvxs7xVyfLrukLCClgJ3y8WLRQ6NAyL6p5xynBkTVeKdbG0aA8_LrUOfbExjZehbm4li2-gabePzWR7eiDTDq35SbrRHFD1noVzao9omWRys-dA6BdWk9h1jHvb7z_d4nKO6yCvPcA82RgOHUWOh3DZu2djKuNhfHuO_3-oIE9VW0XGbwt6igSX5whHzz4dTbkFvEd4miik-hT5bIs5NY5F9RaEpyLHQBgPs9jaNuFZDaE8JSX_GyTIGZzBwrD8IoVa2U_ZgTWZHAbQIPRY5faT45UlW4mXU82GMcZWKLo5mc6lL3jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ترامپ ادعا کرده جنگ تمام‌عیار با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند
وال‌استریت‌ژورنال:
🔹
مقامات آمریکایی گفتند، ترامپ به طور خصوصی به دستیارانش گفته است که اگر تهران نیروهای آمریکایی را بکشد، پایان دادن به آتش‌بس با ایران را بررسی خواهد کرد.
🔹
اکراه ترامپ برای شعله‌ور کردن مجدد جنگ نشان می‌دهد که او ممکن است مایل باشد برای جلوگیری از درگیری گسترده‌تر در خاورمیانه، شعله‌های آتش کوچکتر را برای هفته‌ها یا حتی ماه‌ها تحمل کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656033" target="_blank">📅 12:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uknVBtg-luZYFJNSda2ak8gDtJRO9_Y1JIx6ZS9akGkfWapQu7TZRoOeLFJ8xrtxRVOkuXvZ48wSOF60W8WDcQZKgx8p6yRBNlIrbFP7nbh10zYbwZlEjU-dRrkmtLpF-bmSGBUAq0mF6YHEmLmOGsGx0yOoq5ywNefgSm6QoewM7oZFmhJGuz3QloYOacPVUXL8g93tCzP1FhOz2SfWl89-NY92fhiWh4g8k6ODqb0RmwduYR114o_ruElqabs9hQwcZWN0SWZJY9pqUMEA0AeDeOLX5jN6Bnso_NcJLsNfnGuyRxI3Xe1nvgHGjTb7amO3FJJbEMHTgqu8Rot3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ
🔹
سرپرست و دوست شما فقط خدا و رسول اوست و مؤمنانی که همواره نماز را برپا می دارند و در حالی که در رکوعند زکات می دهند
(آیه ۵۵ سوره مائده)
.
🔹
روزی فقیری وارد مسجد پیامبر شد و تقاضای کمک کرد؛ اما کسی چیزی به او نداد. او دست خود را به‌سوی آسمان بلند کرد و گفت: خدایا! شاهد باش که من در مسجد رسول تو تقاضای کمک کردم؛ اما کسی به من چیزی نداد.
🔹
در همین حال، امام علی(ع) که در حال رکوع بود، به انگشت کوچک دست راست خود، اشاره کرد، فقیر نزدیک آمد و انگشتر را از دست او بیرون آورد.
#اخلاق_علوی
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/656032" target="_blank">📅 12:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آستان قدس رضوی: چند مکان برای تدفین رهبر شهید بررسی شده است
🔹
در زمان مقتضی به فرزندان رهبر شهید و رهبر معظم کنونی انقلاب پیشنهاد خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/656031" target="_blank">📅 12:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0A6zsPHo6-O2d4fwd1GB8g_63bxLduIbTQ4vWqMURm91kQuUOIxl-7H1tLp8JsmZ2DimebeM3A38C8ExK-p7uzVhhOwAIYrtPBgRyC1QRM7n0xzqGbJGi-WM2QskvVYESSknL4Q28q4lue7BXGNLD_NED3LHRTYqqgdVcEOjx043mLwnMpEAAjsTq9hXyP46yu1gGsa4z_pWYEhsmDIl918P6O_mW2nGpKpvJ55jSGnkYOAnVIeu3XUVohhEYuQwIUnIBHpU7i1xKdXb88D0lCrfRaO2GzdAgaBnQEBgzcWLIAYf9PtJU1RGuKlsqMh7m_Oli2Lwpbh3yEmYs0PqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: تنگه هرمز مهم‌ترین اهرم ایران در معادلات جهانی
سی‌ان‌ان:
🔹
ایران با کنترل تنگه هرمز یکی از مهم‌ترین اهرم‌های خود را در معادلات اقتصادی و سیاسی جهان در اختیار دارد؛ حتی در صورت دستیابی به توافق دیپلماتیک نیز این ابزار از دست تهران خارج نخواهد شد.
🔹
نگرانی اصلی بازار انرژی نه هزینه احتمالی برای عبور نفتکش‌ها، بلکه احتمال اختلال یا توقف کامل جریان نفت از این گذرگاه راهبردی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/656030" target="_blank">📅 12:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f642f8f3.mp4?token=JeCidDAScuvrpdEkYNl1XWoW6dx67JeFDHKBeqfsz4R5MwNIXsMiXwKM_Z1WqUAefXlttBSc12i2mGKMUy9HRJrK3CcOhAMcV-FEnxhJxxt9vjfHi5br00VH6vjcVayrsxY8N0FKVrO4PZ3S5Z3dCj7_6Smmfey08RG11HgfJecy5Fz_JHXQZqOhu8dj7RVAVlj7_jy-cRAa_QlspMlosL9XTYd3iQ-_8WQldMWqo57Wiskiqe7y8Odak-wgpuQxNyNWqwZDwE0X0xR_N4-y9CRiM6jk6KRCJDKywr1yVX6rXgfhTE9saZeC-AjlNSzwzaIsQjYCqXj81s34zP_D6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f642f8f3.mp4?token=JeCidDAScuvrpdEkYNl1XWoW6dx67JeFDHKBeqfsz4R5MwNIXsMiXwKM_Z1WqUAefXlttBSc12i2mGKMUy9HRJrK3CcOhAMcV-FEnxhJxxt9vjfHi5br00VH6vjcVayrsxY8N0FKVrO4PZ3S5Z3dCj7_6Smmfey08RG11HgfJecy5Fz_JHXQZqOhu8dj7RVAVlj7_jy-cRAa_QlspMlosL9XTYd3iQ-_8WQldMWqo57Wiskiqe7y8Odak-wgpuQxNyNWqwZDwE0X0xR_N4-y9CRiM6jk6KRCJDKywr1yVX6rXgfhTE9saZeC-AjlNSzwzaIsQjYCqXj81s34zP_D6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان شیولوچ در منطقه کامچاتکا روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/656029" target="_blank">📅 12:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش مبلغ کالابرگ در چه صورتی خطر ندارد؟
کامران ندری، کارشناس مسائل اقتصادی در
#گفتگو
با خبرفوری:
🔹
باید دید مبلغی را که بخواهند به کالابرگ اضافه کنند، از کجا تامین می‌کنند. اگر از بانک مرکزی یا شبکه بانکی بگیرند خیلی فرقی نمی‌کند.
🔹
اگر از طریق خلق یا چاپ پول این مبالغ مربوط به کالابرگ را دولت تامین کند، آثار و تبعات تورمی دارد که فوری نیست و در اقصاد ما نزدیک به یک‌سال طول می‌کشد تا تورم ناشی از خلق پول اتفاق بیوفتد. اگر از محل درآمد مالیاتی، ارزی یا فروش اوراق این وجوه تامین شود، آثار تورمی ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/656028" target="_blank">📅 12:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656027">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp0jTrdZRr1Bk6t5br8dn55CH1vCMntYnorz1wN7u8se7QpbzHie87jfJH8XXrJEZ3zWYyKMTge5UG58n8PHzYaeWXZBdVt5xBrrWyiso0ORhx5aGnvLyP439arReRv7Q7fve57S5k0SDGMYbH1_gtovkWaTTp_ghPQvcyPYQLqytlXdLyNBzpeuQZqimf40G96eVQ2XyKzTjZGHTr3IRHRNlfSCiLnS46ofiTipt0xH3PwLG1nz0h5CamMyl30wxOKmCPPQBK9L96-1hpv7oqtR1AVgqjqMhX_tdhA4dFlWQe_Kw0jqqZPoOyzzRhpiCLuAVW6Zqqzdc0fpYD4b2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکات کلیدی پیام رهبر انقلاب اسلامی به مناسبت سی‌و‌هفتمین سالگرد ارتحال حضرت امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/656027" target="_blank">📅 12:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656026">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تکمیل ویزای اعضای تیم ملی ایران برای سفر به مکزیک
🔹
با انجام فرآیند اداری معمول و صدور ویزای دو نفر از اعضای باقی مانده تیم ملی، روادید تمامی اعضای تیم ملی صادر و این فرایند تکمیل شد.
🔹
تیم ملی فوتبال ایران روز شنبه ۱۶ خرداد در ساعت ۱۵:۲۰ به وقت ترکیه عازم تیخوانای مکزیک می‌شود.
🔹
طبق برنامه‌ریزی انجام گرفته، کاروان تیم ایران در ساعت ۱:۳۰ بامداد روز یکشنبه ۱۷ خرداد وارد شهر تیخوانا مکزیک خواهد شد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/656026" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
جزئیات رای‌گیری کنگره برای متوقف کردن جنگ ایران؛ ۴ هم حزبی ترامپ علیه او رای دادند  نیویورک‌تایمز:
🔹
مجلس نمایندگان آمریکا روز چهارشنبه طرحی را تصویب کرد که به موجب آن، ترامپ باید نیروهای آمریکایی را از خلیج فارس خارج کند یا برای ادامه عملیات نظامی در آنجا،…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/656024" target="_blank">📅 12:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39d0b8201.mp4?token=flEa1bappwPqgpBCHgexoDr408PfaO2CvNN6SvwnN7S4TPOXoiDUOk8GeWqQVF7gXAbtI_cnJNrGORl2EIQxiOo4XO34IpKSTtYf-XCMlWqgyhrZaFWXuS0G-h2gafJvCza31eOfz6CW48nBd4w2WNRPii51TzuynXFL_WypmEtFOkpGqJ6WPV5zo0HWW5ffmbIcG52WpXTqMYtEwRJ8GKR4NH66400Ak_G4gv1Dcr6ni11PkfFBPpRHtuiJnHFUF76CtixHir-sbuVChGc81ReM022KDOLaNHbKQi1YyyC1M0OTWa_vq4_9bW9B2eulwhuzDpcNcT8JTr-pHFs6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39d0b8201.mp4?token=flEa1bappwPqgpBCHgexoDr408PfaO2CvNN6SvwnN7S4TPOXoiDUOk8GeWqQVF7gXAbtI_cnJNrGORl2EIQxiOo4XO34IpKSTtYf-XCMlWqgyhrZaFWXuS0G-h2gafJvCza31eOfz6CW48nBd4w2WNRPii51TzuynXFL_WypmEtFOkpGqJ6WPV5zo0HWW5ffmbIcG52WpXTqMYtEwRJ8GKR4NH66400Ak_G4gv1Dcr6ni11PkfFBPpRHtuiJnHFUF76CtixHir-sbuVChGc81ReM022KDOLaNHbKQi1YyyC1M0OTWa_vq4_9bW9B2eulwhuzDpcNcT8JTr-pHFs6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی درباره‌ی تغییر جنسیتش: تا ۴۷ سالگی خودمو تو آینه نگاه نمی‌کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/656023" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
دسترسی به اسپاتیفای بدون vpn ممکن شد
🔹
بررسی‌ها نشان می‌دهد دسترسی به سرویس پخش موسیقی اسپاتیفای (Spotify) بدون نیاز به استفاده از VPN امکان‌پذیر شده است؛ البته نه روی تمامی اپراتورها.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656022" target="_blank">📅 12:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/casd51aG3RGW3q6UNwOc4YKawSncveQEQ6GzgD4fb1Rm5ikoy5E5nKrDiW0_rJ2pvu-J-bpmERwm_xQQChB3ruDEEjkl46iJEjhFSorv1ixLHAAVJXgQIy9T4rG3hAutfrRMcBp_D1B9XYaCEpfMj75s985qwMOFtzoigfrWONikCWrr9CcEUXrkqVCZRKWj62Lpuc5LD-5tyWdF4HuC7g8kvmx1vZGR61pQqdSNM4FJZ0AuEPWo3ic83XIKNsLVUKkI6rt6fUGcjPIXkWzzWpSRr5U4kue2YvWHHJ99Inuhj5pL1zvqJ305W7nIf5VBGWdEuVpHTkAJtt4Y-Put7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام دستیار رهبر انقلاب به مناسبت ۱۴ خرداد و تحولات آینده کشور و منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656021" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
دستگیری عاملان شهادت مأمور کلانتری باغ‌فیض
فرماندهی انتظامی تهران:
🔹
در پی شهادت یکی از مأموران گشت کلانتری ۱۴۰ باغ‌فیض در شب گذشته عملیاتی برای دستگیری عاملان این جنایت آغاز شد.
🔹
مخفیگاه متهمان متواری شناسایی و  هر ۳ متهم حاضر در صحنه جنایت در محل اختفای خود دستگیر شدند؛ متهمان در تحقیقات اولیه به ارتکاب قتل با سلاح گرم اعتراف کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/656020" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7690bfcd4a.mp4?token=TjxVQDf0AU3_qmfDJKzsoO2GoJt_XTfuLC2ZEvVvmDymtuJkjRRxBbQf6VM9fZfIUN60kYg2ovAjooxVRqPJBZkZYTaZ_KdDHVVarA3vv7-BDczYRP9KdWBQpRAvwTegiACanpmBQTl5S5w4LermcfqXP9NkvLWiVY-OPeLRmRyyJ8dpU2KKMaGue5YGrLMEENSe6ECXFyMpU6cunPaXF4WmM-QSPmeWqQFrOrFLcK6rX-noVxGjWye2VARx5JSfy_CmJS6vs8KYg-9tbrRqATNwQjwzC_ZbzZF7uoDmKsglTPCGxeGlL3NC3mUv6iYcquf6TCcYKvf_60wGnfGNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7690bfcd4a.mp4?token=TjxVQDf0AU3_qmfDJKzsoO2GoJt_XTfuLC2ZEvVvmDymtuJkjRRxBbQf6VM9fZfIUN60kYg2ovAjooxVRqPJBZkZYTaZ_KdDHVVarA3vv7-BDczYRP9KdWBQpRAvwTegiACanpmBQTl5S5w4LermcfqXP9NkvLWiVY-OPeLRmRyyJ8dpU2KKMaGue5YGrLMEENSe6ECXFyMpU6cunPaXF4WmM-QSPmeWqQFrOrFLcK6rX-noVxGjWye2VARx5JSfy_CmJS6vs8KYg-9tbrRqATNwQjwzC_ZbzZF7uoDmKsglTPCGxeGlL3NC3mUv6iYcquf6TCcYKvf_60wGnfGNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غدیر خم؛ رویدادی که تاریخ را ساخت
🔹
برخی لحظه‌ها در تاریخ تمام نمی‌شوند؛ از دل یک بیابان آغاز می‌شوند و قرن‌ها بعد، همچنان در حافظه ملت‌ها زنده می‌مانند.
#روایت_غدیر
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/656019" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lw_CWSBHFN1Eay8kpAlENDhWMiK3qTKmNpcnAM4PvNgnI7POXzaz00VOBztEFQYUbVW9dgTTOQX9aRv-7X15RQ75hVKE0W8JseBoOt_m7vZ4BYQ0-axJSwL-MydKMjNxMPnNdLjBysppDDPQNRllwulNXVVGqKv2HpRxNXMDQChoW81eOwKVCdAlmHZai4M9_EGziYlShTDmPhKJ2Jw_JHe5dBlsVHXzUDFR6mo8yCH_INnQieV_kSrPQvs6qiSoyl2CFFNImqCz82OOszqBmygMEo-xQmvaK29IWooC1W8ctlZLeldYx0NJFsmfbtHYU0NEsOBy4CFCQvVC7IDwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqkpQ9pZObupMVxWo-w4Cb2-elpZNf6qnmqpe_BmAUC__CuLFngw6rC6rEvTjl1xzygSKCNNBsOMnDUH8bhtaCuVdYSGjvJK6yHoD20uPSxZQgVTdNPDiRi5K1b8R8-26YX7Sm8c2waRyCuCqVsOFMbikU4JxQmz9Y0m_M-e-Rkn-O7TutahCXSiRa4epvPK-jhNCHsDDW-0wZK5Pe_wTIvK1OmEzWcUDTl0BrHvWT_Js5f6GDE--bXdHlZl3kvMrsQBeWgNwUADuey-F9An5jhYtzuI6I6pKSV907dZ6qKr4tnnQefYBWGvm8mL_KCzqq9_ilGDcTY0kqbixPdRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0-RI0tAaPuXmsX0Cx2uOFLHgXUnP7uMVyRDsvkIkqLSYC4qD-IQHuOYwpUNCkywY7ei1cs7Uz6JAM1WcxjTK1Jg-mhAou-il9ix-z6rqVW0Z8T4Pio6DKFjSpXYkXAbhLxdggTaR3RR_ee41tHRW81a1naiXX8rqrFZzsoSmxfrV5sJH_jG3ckmCAYr4Szw5CiDkJwFpcPZIWwgC8rl4bwRLL6Em4okLP8tw3Ka7Hu6dDxMTcAp5uwGYcvW6IjnKEBJAA-4rnfX14SqitPh143ZhcThbuO_eOYAR_ZwaVKHVyf_8K5Z_SECA778-hrjLlhs1PRGcqA3Pdpq751wMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXDSS8XCMIFpebZs-r88zkDCxpJfdICAb3r_u9Bcuav9w0aXdTkdCAu7v6YK6LvLH-TNUbN2uT_Q-xKYpg8868ji0pxIAnP8kFl0XxIFSjcD5qHgqdMX3CWvWSLZVh0wlki0LznhZljkYnUna-gKBUUzkhqFAwWHmhPM82w9k8C9rE_LaMTWPkeElPdglhddTdnV7iLrA1yT5WvEkJmpce19szCmqqtjl0yuuRwhf5yw97OapwhjfJuIhb92oGKrceAD9RTopwdQv7cKZllRnwwllRQN1g1_q97734CtBmSudh8aO6zO7X-KGAhQH9zjCPO2BFrwUV1tEHXRw5NExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLBu-MC28Cfue8bJzZZjr9rcAOc0BvchnRlIeyNnw-uxGaO2x9EmqMCBt4J6SqG-xiaYCHv69rxQCLHSSXd6-4CcjaFIJEU75TIu-7CUMH0Hb1yqMxHJyTS_ekhI_CrZfPKLEZblXTBzBN7q54XovjaOhXlbGYNr2IjlKqAdoxhs8xwXJjt5iI3UxeFJ_i6Q1XzPLqcV6jU36Bq4gZF1N1nWqo97q-wsN1xYpWTxCuEkMGzdyn3Q4hAtMOvLxFfVZdjmZBI6sA8w7-a_FfyZY8QgUBNZnOEJPRBFMqgpNjzx08XMlQMb1-V8-z9sW1aMDFSiAkLJvqMGHC72oh_vHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6yJWiClwV78iubQbmQGAjuxGmwi-cubV8eevc6rVFVuZOO-suLXglm1yFXcR5kuLYVB2EWPIg59tGNQ0ICaiTR3MYTsiYpdBVfd6abjzIIeDrQeLv8_Ikdh9-ycvTK339BOI4kN4UdwitM3tgfhcxeOZ3bqHRdfuvKzqG9qL0yhNRHAVgUPmu9HUnWUnQOvfrGqCHb9OwE22fo-M67foZS8pcAr8FYhEducGegmZxMXhMkWk0P5cbDFDgxvCnxvPdlfKbOeyeW9PR0i00N6cg_A_wU1j_n6nrNhOFHMHLBcIDI8oVW6x8qJgJAF2O7KCK3ekxPJEylcQBuumYOtjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حرم مطهر امیرالمومنین(ع) در شب عید ولایت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/656013" target="_blank">📅 11:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af4175881.mp4?token=cFJFgrcg2fseyoOx48peEpV5s1nM9IpQil9dTldpbXI-CIhyyj-94AtGnUSnCVRXKdpbKUucvxlpQ1LyCFqYYvsantASnZ-V7d3oQehtEXoOcgd2jNfNzIszoXNaW2CJ-bvW0ZopXRdluWPozq2aKktQv6DGjJn0p6n9imsxhQlD6hyTWnEOK4mIKTQ0fhFvk793ZD5DCYMaUyuNMyhdn0Tt4lXqVypM3zpp6ONl2Wsl-Fi3wGfWlI15_sY3gIeT-1_nQVJ2YEpa0KY8CFRY_vHy4eUq-HEXj3z6IGmJe7cDE9l3Z66vQAZtK6POVCS8TqwgNXPHdWM8HMoOaewe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af4175881.mp4?token=cFJFgrcg2fseyoOx48peEpV5s1nM9IpQil9dTldpbXI-CIhyyj-94AtGnUSnCVRXKdpbKUucvxlpQ1LyCFqYYvsantASnZ-V7d3oQehtEXoOcgd2jNfNzIszoXNaW2CJ-bvW0ZopXRdluWPozq2aKktQv6DGjJn0p6n9imsxhQlD6hyTWnEOK4mIKTQ0fhFvk793ZD5DCYMaUyuNMyhdn0Tt4lXqVypM3zpp6ONl2Wsl-Fi3wGfWlI15_sY3gIeT-1_nQVJ2YEpa0KY8CFRY_vHy4eUq-HEXj3z6IGmJe7cDE9l3Z66vQAZtK6POVCS8TqwgNXPHdWM8HMoOaewe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جملات معروف رهبر شهید انقلاب در مورد امام خمینی(ره)
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/656012" target="_blank">📅 11:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656010">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhgf9jobYjCe9EqGSuYfd5AnaOWK_OWSAjaJHvAhanPokJL7binXpEp8Q_tp8nUNknsM-j8bPdtS4Y9P4-UJva5jLDIRTauX074HVZA0zOHc-rH9juqdYj6vmVWayhgGc8J3hX1XUoje0UL9PoDeuRbgh27KWRqkUCiB6fpoUWwpIJijoOfdgro5pYJYE7UFAmR5heqtLR3mpglT_XhOZFTBRevP-UuTevwRzFE6lET02A_rFsP8HvvVL6mBzCJJeAS1yAqYaOBfYqdfbe2wZ_t_GvSjOPy8t7uNNHYO5thdqBjwyTBpLRiGAjJip9rLhmVMO_FWP9Gc2DkoktZEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23a3791278.mp4?token=ivu6G7Gh2GyhC99DeYbA6RAuEiuRrjj3PLxwKT785Ix9CJjmOjS9aSFLnikLG6Pzp1z3Fk6Saad3-Ilc9s7SHAh4gYVeRjrb35p9cNGhZQJH0inLG-yjaaP6bbCZjA_avk9gu6lvxUOXOss0YvvogEIg2qOi2-w7WBfGAr4HiYpGzGK9eNyURrPDjM-Hztrxcaaw5FfKT2kdWylxU-uv0BKjcyMTwYx5Hl_AEqTHgYT5Wa7sagwtKNQFHqzq7IdYQLl3fFVlIfHONoXoT2Nh1HTAzwD9tSW9RTrRI4lBwDZLMfVnd_KkwbIbH7rZzjoLC3G33wOE4qLppwiMmif_xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23a3791278.mp4?token=ivu6G7Gh2GyhC99DeYbA6RAuEiuRrjj3PLxwKT785Ix9CJjmOjS9aSFLnikLG6Pzp1z3Fk6Saad3-Ilc9s7SHAh4gYVeRjrb35p9cNGhZQJH0inLG-yjaaP6bbCZjA_avk9gu6lvxUOXOss0YvvogEIg2qOi2-w7WBfGAr4HiYpGzGK9eNyURrPDjM-Hztrxcaaw5FfKT2kdWylxU-uv0BKjcyMTwYx5Hl_AEqTHgYT5Wa7sagwtKNQFHqzq7IdYQLl3fFVlIfHONoXoT2Nh1HTAzwD9tSW9RTrRI4lBwDZLMfVnd_KkwbIbH7rZzjoLC3G33wOE4qLppwiMmif_xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل ۶۸ متری آردا گولر به الچه به عنوان بهترین گل فصل ۲۶-۲۰۲۵ لالیگا انتخاب شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/656010" target="_blank">📅 11:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPhzB1LvKwfa1Q9FMyWWe-pRveUG2dZhdVxEY605z4bC57tbG5VEAemyKjGOsgGQ3XN70UyzRRRmHwNSBV0R39R1AG0zk6cRwKVvUwJxpEk62wN29kZU63PB2iD9QDtVgnDCyLwgc8W08wB5hRPTmBPlEYagtCdBFoGME7hOlICKiKdK6_LxU6fmt9QYop1mpmBiZJZwzVfy2W1XirIazUrB8-QqDVX37tmbLNU8okMSh2s4AWl1O2OCIGhG_1w1FqCWsKqBPo0asHm7h2a4yMnGkj0e66D_22lNkT837yVCUleY106MGkIm1LQsfUdS1eVvLeJg87N5n65GHU7IWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات رای‌گیری کنگره برای متوقف کردن جنگ ایران؛ ۴ هم حزبی ترامپ علیه او رای دادند
نیویورک‌تایمز:
🔹
مجلس نمایندگان آمریکا روز چهارشنبه طرحی را تصویب کرد که به موجب آن، ترامپ باید نیروهای آمریکایی را از خلیج فارس خارج کند یا برای ادامه عملیات نظامی در آنجا، تأیید کنگره را کسب کند.
🔹
این طرح با ۲۱۵ رای موافق در مقابل ۲۰۸ رای مخالف، ترامپ را برای ادامه جنگ در ایران محدود کرد. آرا عمدتاً در راستای خطوط حزبی بود، به استثنای چهار جمهوری‌خواه که به همراه دموکرات‌ها به تصویب این طرح رأی دادند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656009" target="_blank">📅 11:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzFq8lN-u-m7FoB_OSVa7nfvCpzXjBUs3Mq1hRHOOfXlwF5YfRwNlSewUEtoIFdFYYEJL3HY9sN6gE2aF_z0x0MXPcnqkI26U2LcYdWBPoSFTAOxZHZXQSc0QtHKGAdv3dlBMEUHB6hAdTc8PNI_6lsR2T6BFnS0WE5On-9JdbngqerLw2Uu8Ykgh01moQd94T_22yHa69ExBU1SuKGlZuH3e31OH7AiT21wwrJGSC5UjYS4dtUlUwo4tx6mgSEbTlBhFWDKw0UsAGr6hjj9KU9FceeK59df_b9CZMEieba_ik2anTdZFSw3REbFuE386HyTXPji8MFVtLvJTteRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهدی‌های عزیز امشب مهمونی غدیر رو یادتون نره...
🔸
از ساعت ۱۹الی ۲۳ در حدفاصل چهارراه نخریسی تا چهارراه چمن
🔸
با حضور هنرمندان و چهره‌های فرهنگی و هنری کشور
🔸
۱۱۰موکب پذیرایی و فرهنگی و تفریحی هم تدارک دیده شده...
منتظرتون هستیم...
❤️
@Heyate_gharar</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656008" target="_blank">📅 11:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-qtc5M0f0qVWFlAz2KsU_jWZsSUZrexHkAgOnA_w2svPa9EvCsq71f22bsn3nHhbWwvrJAN8920U4aKYCQ_3ZKuu0vtZVSjzPuzKTufyHCaDIDnB_tI_Ul5zKdxX9icvpIbJJMVCXFNo5XjAQn4-iN2wG19Mo392z5CvzcVBNx5GdImISS0R8xXj3lWixwA5PWT7e6zrZ4D5rkgHTWTc9AeK2_0Xx6s6tZgaRtQlMNbMQ8r4Hsy7LnIfe0pZeH4weIIDCP1eU_HOOyVYdnVLg89P-C6jdAVjNJyuPIIxpoTGqbwXogAIDVEQHt_P5D7cnUeah0ym-pDClz4yumRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نقشه‌ای از جهانِ غدیر؛ از نجف تا پنج قاره، یک پیام و میلیون‌ها دل
#جهان_بر_مدار_غدیر
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/656007" target="_blank">📅 11:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/656006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت عید غدیر،   سی و هفتمین سالگرد ارتحال حضرت امام خمینی (ره) و آغاز رهبری حضرت آیت‌الله شهید سیدعلی خامنه‌ای | ۱۴/خرداد/۱۴۰۵
🔗
farsi.khamenei.ir/news-content?id=62998
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/656006" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رهبر انقلاب: از خداوند متعال پیروزی نهایی ملت بعثت یافته را مسئلت می‌کنم
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره).
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/656005" target="_blank">📅 11:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
رهبرانقلاب: دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است   پیام رهبر انقلاب اسلامی به‌مناسبت سی و هفتمین سالگرد ارتحال امام (ره):
🔹
دشمن تحقیری پر معنا و عمیق را در میدان و خیابان تجربه می‌کند اما کید خود را در جنگ ترکیبی در…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/656004" target="_blank">📅 11:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رهبرانقلاب: دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است
پیام رهبر انقلاب اسلامی به‌مناسبت سی و هفتمین سالگرد ارتحال امام (ره):
🔹
دشمن تحقیری پر معنا و عمیق را در میدان و خیابان تجربه می‌کند اما کید خود را در جنگ ترکیبی در دو نقطه تاب آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولین کشور قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/656003" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
رهبر انقلاب: همگان با ایستادگی، روشن بینی و حفظ وحدت و اعتماد متقابل و هم‌صدایی نکردن با دشمن نقشه او را خنثی نمایند
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/656002" target="_blank">📅 11:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رهبر انقلاب: رهبر شهید چهارده خرداد را به فرصت میثاق سالیانه ملت با امام خمینی (ره) تبدیل کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/656001" target="_blank">📅 11:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رهبر انقلاب: ملت ایران با بعثت تازه خود در کنار جبهه مقاومت مایه مباهات ملت‌های آزاده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/656000" target="_blank">📅 11:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رهبر انقلاب: خمینی کبیر و خامنه‌ای شهید آمادگی ملت را کشف و احیا نمودند
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/655999" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe4240b41.mp4?token=Y6BY86LjdpBvvcxQjqdRUxduvYD8Wxvtzd3BkUWQVrB9welPyOOuzMD7GIhTrgmlRO9udlmGVpsA3Kb5lOQIUKr1F-6YzmZf7s8bJOw0jjBAAHTw_xpmI_MTD6iTY4ZoDi92C7aYmvRazhE5jB86Y2x8oCwIFx6iXQ04cw7gtkyG-yuEbo8eEmSIH85UrGa1JDHL4K0CdPuNxoYXzxeWWP1sTW6sPX4JYPIvUP2gEOYvfhkAPXuHPt8AvtIDYrxfUmPK5Eq_8Zp29mQctWiGMUaeydDAX5WUoB5Jkisbqe4ZI3ii1CkjWK0f5qbqNGrHQWJarX08CPRjBu6NUv2MAaF94DFZ7wL1rXQjckV8RIpi5WBxJGRVshNhv2Jw0kputWom4LoYKPlDplVfgqh8oFwkja2QFVqZkyUxi5gq90HsvTcWtYBX5X8eUuLQDkKHf8jytn8KSu6uW6edZX_zg0gMpLR8g_1O_EcpauJsP2mhzmRV3PeM5EeowYbyLbuEOHUqiUb7hHZNBLaZSbP35mY4h6yXhI28Yja4dih5CGnI19-MzyCZcu9NLo_9a1XNiYqBqL5nesHQSGmOOo72-UepcH5ZC_vb606z-dcJg_9Je9uLmUHjoJUhYopIDm1WEs4W08sqKSFQIsqIdDLuxGvKFHID8nf2ERc8XJmvOZk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe4240b41.mp4?token=Y6BY86LjdpBvvcxQjqdRUxduvYD8Wxvtzd3BkUWQVrB9welPyOOuzMD7GIhTrgmlRO9udlmGVpsA3Kb5lOQIUKr1F-6YzmZf7s8bJOw0jjBAAHTw_xpmI_MTD6iTY4ZoDi92C7aYmvRazhE5jB86Y2x8oCwIFx6iXQ04cw7gtkyG-yuEbo8eEmSIH85UrGa1JDHL4K0CdPuNxoYXzxeWWP1sTW6sPX4JYPIvUP2gEOYvfhkAPXuHPt8AvtIDYrxfUmPK5Eq_8Zp29mQctWiGMUaeydDAX5WUoB5Jkisbqe4ZI3ii1CkjWK0f5qbqNGrHQWJarX08CPRjBu6NUv2MAaF94DFZ7wL1rXQjckV8RIpi5WBxJGRVshNhv2Jw0kputWom4LoYKPlDplVfgqh8oFwkja2QFVqZkyUxi5gq90HsvTcWtYBX5X8eUuLQDkKHf8jytn8KSu6uW6edZX_zg0gMpLR8g_1O_EcpauJsP2mhzmRV3PeM5EeowYbyLbuEOHUqiUb7hHZNBLaZSbP35mY4h6yXhI28Yja4dih5CGnI19-MzyCZcu9NLo_9a1XNiYqBqL5nesHQSGmOOo72-UepcH5ZC_vb606z-dcJg_9Je9uLmUHjoJUhYopIDm1WEs4W08sqKSFQIsqIdDLuxGvKFHID8nf2ERc8XJmvOZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انقلاب: قیام لله زیربنای مکتب امام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655998" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf43b60997.mp4?token=NfBlnoF0MMkW4oSRIywPPI0JqQkovIP8ax2uFYREYp7TKOZPF65xME9ofG5foo1RlClpk5FEOgGKOEghGZ5s8ZRyD_RmD-bkjJ23xioJRFK5l5ldrQHJvq32juPIVHiH6k0r9xqn7pb0mJiUSLp5rQzfraHjEn0o5u3DMxHbiFEs8MDpl8vXkqWuQM4mUtAalXtUItZvkPT98ZlxNuU8Pz9DKrz6A-OQlBqdCgObXjSa9v30T1vjXZv3Dhyxh2Xq-ZCoLptRdaIbRclNhNzFIuRLGusZw7cEFXKTZC5z7pibU9dyYaAj_mhWWbllxtG78W8HPpjRGf8vQ2NnGf-f-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf43b60997.mp4?token=NfBlnoF0MMkW4oSRIywPPI0JqQkovIP8ax2uFYREYp7TKOZPF65xME9ofG5foo1RlClpk5FEOgGKOEghGZ5s8ZRyD_RmD-bkjJ23xioJRFK5l5ldrQHJvq32juPIVHiH6k0r9xqn7pb0mJiUSLp5rQzfraHjEn0o5u3DMxHbiFEs8MDpl8vXkqWuQM4mUtAalXtUItZvkPT98ZlxNuU8Pz9DKrz6A-OQlBqdCgObXjSa9v30T1vjXZv3Dhyxh2Xq-ZCoLptRdaIbRclNhNzFIuRLGusZw7cEFXKTZC5z7pibU9dyYaAj_mhWWbllxtG78W8HPpjRGf8vQ2NnGf-f-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انقلاب: درک و شناخت امام چراغ راه آینده ایران اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/655997" target="_blank">📅 10:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b13b3815e2.mp4?token=u7unjYUXTs6H67xii7PuDVoyYHbqer48aAvepE5Ga1x5eCBIyLePA71BCwzTJxGHS1p82MykyypXRXtsTRU9nh_68ZchY7rv_mgKDbqMp9ScC7XbEl7cfoqhunNOuNL9cqHaS0dFSD6LgDQ7ZA9WTjSKd2s7I9mV3SimROh2d1CWFtPQ6Y3uTVQgJuTD5t8u7v9kpicTb6TLo8L2K6nzNZaBi16jVZKE7RVbK94jij3H46u43u1avxQoLNUyf8uVjjlPsI5j7lxGv70F3c8Osh9zZ2VjbsQQhQBviJw2KaD6bTeJtxSVEIHwgvlm1jNjdG_5uUrkFzoZJN2kPQbyoaNafaIfcGmynwN8BKELSEkPBiUOjAAE0KkRw_ORYr1JkV0H97gVWFe0pv3eLyZtQd0-iwAOykXx8gxWtW6Hjnp4crgjNf-iFnTGVFfxNKSoiExleiacSUfhgxJHW5EW4iGe0voH-OGJMw1DlcIP3MEH4RqOrQrOteM8kAFhiTIPzr7fG0aH5u4H7ELVgJYrjtDB-h3lN4QWUyJipEXOv4wECyktozqtKEdg7OIHnmx0n_fUEptGa6ckjGahlsMdTFelbnhT0NLFV8L6jM8MN7bHb9yCX1KgTJg2Fw3sCz2zlyGWSaE25tDu3Y0JdQX6WAlhzaedb_zaagwmXEfgV2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b13b3815e2.mp4?token=u7unjYUXTs6H67xii7PuDVoyYHbqer48aAvepE5Ga1x5eCBIyLePA71BCwzTJxGHS1p82MykyypXRXtsTRU9nh_68ZchY7rv_mgKDbqMp9ScC7XbEl7cfoqhunNOuNL9cqHaS0dFSD6LgDQ7ZA9WTjSKd2s7I9mV3SimROh2d1CWFtPQ6Y3uTVQgJuTD5t8u7v9kpicTb6TLo8L2K6nzNZaBi16jVZKE7RVbK94jij3H46u43u1avxQoLNUyf8uVjjlPsI5j7lxGv70F3c8Osh9zZ2VjbsQQhQBviJw2KaD6bTeJtxSVEIHwgvlm1jNjdG_5uUrkFzoZJN2kPQbyoaNafaIfcGmynwN8BKELSEkPBiUOjAAE0KkRw_ORYr1JkV0H97gVWFe0pv3eLyZtQd0-iwAOykXx8gxWtW6Hjnp4crgjNf-iFnTGVFfxNKSoiExleiacSUfhgxJHW5EW4iGe0voH-OGJMw1DlcIP3MEH4RqOrQrOteM8kAFhiTIPzr7fG0aH5u4H7ELVgJYrjtDB-h3lN4QWUyJipEXOv4wECyktozqtKEdg7OIHnmx0n_fUEptGa6ckjGahlsMdTFelbnhT0NLFV8L6jM8MN7bHb9yCX1KgTJg2Fw3sCz2zlyGWSaE25tDu3Y0JdQX6WAlhzaedb_zaagwmXEfgV2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انقلاب: سند افتخار زندگی امامین انقلاب تأسی به حضرت علی (ع) بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655996" target="_blank">📅 10:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/212666adfb.mp4?token=TUR0idK2_8mozTvNnYQq0cxAkoxVkMkpqgvWcoIRfh99mRHXHj_g5_WX0SRIeyy6PkUSwb3J-ajF1p1G2qcyCAzHLR109CWTxtD4cMDEG_yzfnEx3cHbAoL8WVxyqT6U8CCqCxr1lq0PLDTz0E8ieA7mpCpy7j81kCoOW0AWwXH_fR_Z-KJMN8Vm_mrbrUFf9Z3gncwSLy-9uwZvlyUGOeQlH_oYHK7ejaGIwn8vGPk5Fss2JSOrYS73UxMXC8R1FZJcNK19X28zqvDl2GKETgdNsRRDdVBgL-fcxIO6LOVhpwOL84c6biMuTYrftDn0virYvtXlHZ0Ze8hE4jBvSSmjVLO0kUbDwCvFvRbr09atHfCAZPfORofefbJ8rZvhNrsKv8NZ1BHKWzJpI9kKSvo8nqTRqXDRd5t_ieNd7udvnkFI3fp_7p1dF2XKHuRfBqtlJwx5y3dJRMca5jjuvwZrtfvtgvnPuS6juIwgVkG2KYCa44lw1sS1DiCG8qMkcGGy655La7PWxOjMR7tCGEDgzWRhlHt-5cPjYqUD6nq13tNfW60t6kZDbgGV1fP6-FHdF-MGeuJSi_YTFET0kb7og0rImXuZU47CKjUuDBHj163KNihctzO0899xAWVUJ0qnSWvEcN-Og-IcGb0YEWDwRYSbvhq1EvsBEWF_zx8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/212666adfb.mp4?token=TUR0idK2_8mozTvNnYQq0cxAkoxVkMkpqgvWcoIRfh99mRHXHj_g5_WX0SRIeyy6PkUSwb3J-ajF1p1G2qcyCAzHLR109CWTxtD4cMDEG_yzfnEx3cHbAoL8WVxyqT6U8CCqCxr1lq0PLDTz0E8ieA7mpCpy7j81kCoOW0AWwXH_fR_Z-KJMN8Vm_mrbrUFf9Z3gncwSLy-9uwZvlyUGOeQlH_oYHK7ejaGIwn8vGPk5Fss2JSOrYS73UxMXC8R1FZJcNK19X28zqvDl2GKETgdNsRRDdVBgL-fcxIO6LOVhpwOL84c6biMuTYrftDn0virYvtXlHZ0Ze8hE4jBvSSmjVLO0kUbDwCvFvRbr09atHfCAZPfORofefbJ8rZvhNrsKv8NZ1BHKWzJpI9kKSvo8nqTRqXDRd5t_ieNd7udvnkFI3fp_7p1dF2XKHuRfBqtlJwx5y3dJRMca5jjuvwZrtfvtgvnPuS6juIwgVkG2KYCa44lw1sS1DiCG8qMkcGGy655La7PWxOjMR7tCGEDgzWRhlHt-5cPjYqUD6nq13tNfW60t6kZDbgGV1fP6-FHdF-MGeuJSi_YTFET0kb7og0rImXuZU47CKjUuDBHj163KNihctzO0899xAWVUJ0qnSWvEcN-Og-IcGb0YEWDwRYSbvhq1EvsBEWF_zx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغازقرائت پیام رهبر انقلاب: اولین چهارده خردادی است که پدر مهربان امت، مهمان ضیافت الهی شده
🔹
قرائت پیام رهبر انقلاب اسلامی به‌مناسبت سی و هفتمین سالگرد ارتحال حضرت امام خمینی (ره) توسط حجت‌الاسلام و المسلمین حاج علی اکبری.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655995" target="_blank">📅 10:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پیام مقام معظم رهبری به مناسبت سی و هفتمین سالگرد بزرگداشت امام خمینی(ر‌ه) تا دقایقی دیگر در حرم مطهر امام قرائت می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655994" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655992">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe969a8ca5.mp4?token=d7AZ6fH7BsWozHKqxJQsDAUEcJEWgr8opDznWIx-DLwezloKupP5oEEBdGgRUv8Bx9zFhtaBGzUD1tXFcI4TAgjgcxW9s1Cbs0hX9TDU68iz3c7lIvDRhvxOEVIZ9YaqpUiyU6KrEa323eXGtMkP7RKv_BxCMz_8qhE9XukrmdQB_cxxzbbX0ulv9-KBZU6drtuHOcgSeDXhRyxnbXerr46vPjfLixdVbiDGVY13Fmv2XuQiPOYnGTL91Ver8RSuV4FObVbkd8wm2C92XSZHupuuVhCcqzQlPlbN34KoQAPxpOD4N-9xzljxRjuCK0yFGqevykqnKN3BWHtSmZ24xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe969a8ca5.mp4?token=d7AZ6fH7BsWozHKqxJQsDAUEcJEWgr8opDznWIx-DLwezloKupP5oEEBdGgRUv8Bx9zFhtaBGzUD1tXFcI4TAgjgcxW9s1Cbs0hX9TDU68iz3c7lIvDRhvxOEVIZ9YaqpUiyU6KrEa323eXGtMkP7RKv_BxCMz_8qhE9XukrmdQB_cxxzbbX0ulv9-KBZU6drtuHOcgSeDXhRyxnbXerr46vPjfLixdVbiDGVY13Fmv2XuQiPOYnGTL91Ver8RSuV4FObVbkd8wm2C92XSZHupuuVhCcqzQlPlbN34KoQAPxpOD4N-9xzljxRjuCK0yFGqevykqnKN3BWHtSmZ24xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشته شدن یک صهیونیست براثر انفجار خودرو در تل آویو
🔹
یک شهرک‌نشین صهیونیست براثر انفجار خودرو در جاده «آیالون» در جنوب «تل‌آویو» کشته شد؛ رسانه های صهیونیستی هنوز از علت وقوع این حادثه اخباری منتشر نکردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655992" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655991">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHUux9g5pU_tzqvovqN3M6U2q3SXYEKwFfaU8YDa1KelS-FxNSenGKkBacMX7kAPfeW1u-Bg9tzp-swhmJk1o9k7EK_84yvOKKx6BSw0zL68Wz5MdjghYFfomAce9K4tUwW_-G5v279Ud7Xp-rhsxImomtgwsWhtxye8oXfCCtH1seGb5W16LIW2O4s-Wrb06B0epOSbMIbFSwSrA80i8YhfHwg6xCRqgcPDIOrFFLLKa5oekr9LIyVMQXsbdw0qWriOJtcs486CX1cerNi_fA1znkjRiLTwD3FRaOqa4BORPItO4HSApKkyLuU2XxI-2N_SPs7a6edIAzgpdT7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عزم بانک صنعت و معدن برای احیای واحدهای صنعتی آسیب‌دیده قم
دکتر شایان، مدیرعامل بانک صنعت و معدن در بازدید از واحدهای صنعتی آسیب‌دیده استان قم:
🔹
اولویت اصلی بانک در شرایط فعلی، احیای سریع واحدهای آسیب‌دیده و تأمین منابع لازم برای بازسازی و نوسازی آنهاست.
🔹
فرآیند ارائه تسهیلات حمایتی و استمهال بدهی‌های قبلی با هدف تسریع در بازگشت واحدها به چرخه تولید دنبال می‌شود.
🔹
هدف بانک تنها بازسازی فیزیکی نیست، بلکه بازگشت این مجموعه‌ها با توان بیشتر به عرصه تولید و حفظ اشتغال است.
🔹
بانک صنعت و معدن تا زمان بهره‌برداری مجدد و بازگشت کامل این واحدها به ظرفیت تولید، در کنار صنعتگران خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655991" target="_blank">📅 10:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655990">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e8261837.mp4?token=RVKViS-asKvwwfU1rPg3TdabofY39BHLKUzfSeUg3RcGgk32bTU2huzczCnCM62tLhsIrB_DymRcsGVLMNynPAw0hM9chHt6GXFnxD5fS8cNwmLa5TAZY5gZYV6k_zWtVC6b_5I_dBNzKNtEOAcwqSP1zkma-IgWqBVA0lU4wPoR6BOzZQMtpCyUK2akxf4t2y12OFdXMkydXMF9mPL2w9wu0GZqcvR8uMAud7nG91y3oWu8_JGR0E5em_oHpRv8cCE2xlYaEUMalsT230vd_slN21UxEOTaiQ4Q7w5EVZctNYpAXDbqpXvv9SKu3vobbKa0PsPWXkCXm7_gbkX3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e8261837.mp4?token=RVKViS-asKvwwfU1rPg3TdabofY39BHLKUzfSeUg3RcGgk32bTU2huzczCnCM62tLhsIrB_DymRcsGVLMNynPAw0hM9chHt6GXFnxD5fS8cNwmLa5TAZY5gZYV6k_zWtVC6b_5I_dBNzKNtEOAcwqSP1zkma-IgWqBVA0lU4wPoR6BOzZQMtpCyUK2akxf4t2y12OFdXMkydXMF9mPL2w9wu0GZqcvR8uMAud7nG91y3oWu8_JGR0E5em_oHpRv8cCE2xlYaEUMalsT230vd_slN21UxEOTaiQ4Q7w5EVZctNYpAXDbqpXvv9SKu3vobbKa0PsPWXkCXm7_gbkX3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیانات زیبای امام خمینی درباره امام علی (ع)؛ علی (ع) همه چیز ماست
🔹
این علی- علیه‌السلام- که در هر جا می‌رویم اسم او هست- پیش فقها وقتی می‌رویم فقه علی؛ پیش زاهدها وقتی که می‌رویم زهد علی؛ پیش صوفیها وقتی که می‌رویم آنها هم می‌گویند تصوف علی؛ پیش ورزشکاران هم که می‌رویم آنها هم می‌گویند که علی و با اسم علی شروع می‌کنند. این علی همه چیز است. و همه چیز ماست. و ما همه باید تابع او باشیم. در عبادت، فوق همه‌ عبادت کنندگان هست؛ در زهد، فوق همه زاهدها هست، در جنگ، فوق همه جنگجویان هست؛ در قدرت، فوق همه قدرتمندان هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/655990" target="_blank">📅 10:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655989">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIdZYRALGxA-pNXSy64bfp1aJUFju95GVZoPLg9vR0gsDCRPwil_VDWW8pLEvnQgvISrlNHiyo2_qluEyDsFL2HMX5zvsYAZjFWr94xhQt41BfBiaF8LI4VnTGeEodVC-OU6ofguw40wAvJwOP6NuFsVZJF6InCHDR6UkZDFs0DWryQAIjJCkYu9L2X0BGTuf2h7rsKiN3NdxQzdxzD3LZIfmJGgdwC6GBeb-JswclExxaFi8OhYu868gGLvtq9hxo4Biked2XqJnWDve_PnqUwFWSHalZqXE5oSes_18daXxhRaG_PK2DbfA4UFcUfogYEwrsr6PJerTm7zuaTd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/655989" target="_blank">📅 10:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655988">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_E0oCfXNkflIiMLaAV_DBcbf18vzMj5t2Sgx_GuK9GOaINXKlsnr75tuHbpzws3QiKNi4l9DdCMSiEJc1z9GRBE_3HrSZ0iafWNBmkmMWq0eAObaQiR9jIbO75WeYvwxfDyC6bKwSSmK8hI_nm1DMPPpwkc9SiHrJl8GK4pTFZ2ZA93DNalO4HqTSU20YV5y6i_1cx1lMRDkt8dHtdJnX3F9WQ5PqB7dty6Ye0JtGFhrkYvGheM6x-QsVqu7xBB49p7Ylax_vvsIHFmfo2L7LtvCTepNilmgWKhXjvySSbiCsxUgF41jFUqCQNLbXVrpZew_8mDfActLOKwAxIhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت الله فیاض درگذشت
🔹
آیت الله شیخ محمد اسحاق فیاض، از مراجع عالیقدر شیعیان در نجف اشرف امروز در سن ۹۶ سالگی در یکی از بیمارستان های بغداد درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655988" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655987">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8wJ_iVHVBZEWK_Qr9dsHuVZA3sDxGeTT3N33w44VnYS8YjCqehBYX0imzgY7_yPINupzs2eN3t--sHXyK2OEBq97dkEuCWpZVEGoi51kaOpSplRUmmCReYMYPQP0cTFrrmn3J-0O14QrDSyDirGP0kxHFTAkHgZm0c1fksz1mxWNeNLZfWuiBIvXGiXmGwVg2zcy8tYTelrjYwKi_tPYGBKjcnd4K90U5JaN0BP46heueQwxL5I7-Rosld-tLp35QGIlbM82k-D5E11iWh9aFiry4gQAeXb3i1PDwgVO5GCiNTYBchyLQkwxHR8T5R7B0H_TqVICZgOXXSDCduSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رتبه‌بندی تیم‌های جام‌جهانی در رنکینگ فیفا
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/655987" target="_blank">📅 10:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655986">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e87b41f.mp4?token=mcVXVHUw4_3KEvBOO8x3Nj5nAYQ2alReI0pNlIz0w9COvWWE0eIDoAx6wBLyrm4TKuT28N9E69RGlIvzryMduX3lD8QeyrAydlGEf2GQ9jfelG_qneBCW3MerMYdhVAbN8P0cEBaiDsKAV8dlWTDJ2cxs2Q68vg3MDdw84DWDVnGhYbKFvLoPMLk6PI3VvnKrX3FrOfkwr17urQsshhnW9bwvLsXmixQpIzGRkJgkdLmv1PAPHMlSMwGRWzrQIlA5-ZtKLJfUAetsZZjLjzEs3XOruUeD5x03CieIZkfNQlRyUtQBLE33vAYonLVaF5DSxj1QOHwDbDUemoSUy8rIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e87b41f.mp4?token=mcVXVHUw4_3KEvBOO8x3Nj5nAYQ2alReI0pNlIz0w9COvWWE0eIDoAx6wBLyrm4TKuT28N9E69RGlIvzryMduX3lD8QeyrAydlGEf2GQ9jfelG_qneBCW3MerMYdhVAbN8P0cEBaiDsKAV8dlWTDJ2cxs2Q68vg3MDdw84DWDVnGhYbKFvLoPMLk6PI3VvnKrX3FrOfkwr17urQsshhnW9bwvLsXmixQpIzGRkJgkdLmv1PAPHMlSMwGRWzrQIlA5-ZtKLJfUAetsZZjLjzEs3XOruUeD5x03CieIZkfNQlRyUtQBLE33vAYonLVaF5DSxj1QOHwDbDUemoSUy8rIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جالب از هشدار امام خمینی(ره) در سال ۱۳۶۱ درباره اسرائیل
🔹
اسرائیل قناعت به جایی که هست نمی‌کند، قدم به قدم پیش می‌رود، امروز لبنان است، فردا سوریه، پس فردا عراق.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655986" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655984">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ الصبوح الصبوح</div>
  <div class="tg-doc-extra">حسن عطایی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
الصبوح الصبوح یا اصحاب
المدام المدام یا احباب
در میخانه بسته اند دگر
افتتح یا مفتح الابواب
🎙
#حسن_عطایی
#عید_غدیر
💚
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/655984" target="_blank">📅 10:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655983">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQr4ekCczPr2r-Cb_P0JAkMhWxl2Ay_X9_3mB1R7BsJ21yMvmNfyJ9skjqpZx8uXRbuVpS_E6fh5EpK4TVCTEJtHaOmek7VJ38H8Q9JoVfFCXSozzRPpUOUCyKF6JQqEW24uTMA8UaDQt72UqDyGqg4WcrtNb3VUnMvSBk6UaOMk2_UgLQDRw6yI4ESDoZWx0FLJc39BH9AtL4Bm-bffOrzqeKsjby0lHbmwVoNDmZGMeOoMShj40EfP4ch3sswXO7rltCaXOoXzIMVznKyfRV49-IVgMW7ORIuhqVz2q-zBpML1WcPLThL3AjcemrP0OpSGCCHt6UmxzDyUFeMTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ کشور دارای بیشترین ذخایر نفتی در سال ۲۰۲۶؛ ایران در رتبه سوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655983" target="_blank">📅 10:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655982">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a7f9c8af.mp4?token=BgiQFWIYwGuciCmwDMfnrCIDCKTB71mGyMag3KxR4rTfmTABW_z4pnBXxSv_yRAUwtFV09Yi5FvX6McTjCYFEUJ0Ir2VnfWo8DhFFhAIwM8scBM5Op7AayItbIi-QbJXl7V6o8BOC3C6haxqDe6Mgs53Gn0tM2yr_OJ90KuxpYQresdotP8ffwjvjUpPBV0ft9UnZIVf95EVBfAmZs1R0_AdA5l6otQmu4ml91Q6fiNnWoA-XHiQzmlQu65oy5Icnwf6wjWhfRIrKh2spaAnsKhZRYyCDLfsdotbDDFlVoZrHT_dgv5wF9CbQEo9exOedG2ibszzBavOS9fgbxCTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a7f9c8af.mp4?token=BgiQFWIYwGuciCmwDMfnrCIDCKTB71mGyMag3KxR4rTfmTABW_z4pnBXxSv_yRAUwtFV09Yi5FvX6McTjCYFEUJ0Ir2VnfWo8DhFFhAIwM8scBM5Op7AayItbIi-QbJXl7V6o8BOC3C6haxqDe6Mgs53Gn0tM2yr_OJ90KuxpYQresdotP8ffwjvjUpPBV0ft9UnZIVf95EVBfAmZs1R0_AdA5l6otQmu4ml91Q6fiNnWoA-XHiQzmlQu65oy5Icnwf6wjWhfRIrKh2spaAnsKhZRYyCDLfsdotbDDFlVoZrHT_dgv5wF9CbQEo9exOedG2ibszzBavOS9fgbxCTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بچه ها! قرارمون از ساعت ۱۵:۳۰ تا پاسی از شب شهربازی و ویژه برنامه مهمونی کیلومتری غدیر تهران در میدان آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655982" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655981">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424979765e.mp4?token=XvIryGUXtLOGdE7JmxDLwhBhjTlNHI9QeVPnKG78lzWrc4acWywXMW6-K5ZFni1JDyBjh7A3fEts-8KcODxNC2LVRHNJ24ths00LyzhSKMiLjaNyZ1X3hA6sR9F8AZXUGzu2vqlZBZCDKTjzvEXTwkjD6UtocaMzjtR0Eu77k7OCIKTaiYopRE9X9bvZkHiTG_weuEs3YQ90K4w_8wuNs3Fr0hxcERjKGJ0XmSAyZ4TlXbsqutudPpCnxZml5ucphllQPGAzQcK5lwbASYaXtdh3bmZfhsUV-etPEsiunM281XWefvoQywJe41YvKwbLW8ZtMwC0cn_hEMojCFdKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424979765e.mp4?token=XvIryGUXtLOGdE7JmxDLwhBhjTlNHI9QeVPnKG78lzWrc4acWywXMW6-K5ZFni1JDyBjh7A3fEts-8KcODxNC2LVRHNJ24ths00LyzhSKMiLjaNyZ1X3hA6sR9F8AZXUGzu2vqlZBZCDKTjzvEXTwkjD6UtocaMzjtR0Eu77k7OCIKTaiYopRE9X9bvZkHiTG_weuEs3YQ90K4w_8wuNs3Fr0hxcERjKGJ0XmSAyZ4TlXbsqutudPpCnxZml5ucphllQPGAzQcK5lwbASYaXtdh3bmZfhsUV-etPEsiunM281XWefvoQywJe41YvKwbLW8ZtMwC0cn_hEMojCFdKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تولید یخ با دستگاه‌های جدید در مسیر مهمونی ده کیلومتری
برای اولین بار در مسیر مهمونی ده کیلومتری دستگاه‌های جدید ساخت یخ قالبی عملیاتی شده است و با استفاده از این دستگاه‌ها چند صدهزار لیتر آب و شربت مصرفی مواکب تگری و خنک می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/655981" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un5KrGe8TsDx3ux9zZos_aMWnZxDk4YzwIFeWOkAIanBaP-rBLrAndT3CoVwrYNvvC3DEisxvotyGrNFpOhqcHnROgdsLo5nz_K_R9AILESrAsMVQxKmL1FfdDzRQuwI0aulISJE9BrpX8aBIVUz8_WAQgZkGvaT4sWFPtLXH9xTSX9oyl5hlrGC92YxHGQLFnxpQ5RUUujRga8UqscrNwYg1D5i4SFQXGpALQW_N_mGqeD-tnjrN6EkQB-VhVB10xYkECHrNkaRJ28Ym_MUab1vsftJZkK6V78B-Fz_3z-XnhsggLuXLHbOumVMIS2mlWEzshghWzaVFhCPjaeV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور کشورهای مختلف جهان در موکب بین المللی مهمونی کیلومتری غدیر تهران
با حضور چهره های فرهنگی و رسانه ای بین المللی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/655980" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_cZs7Lhh-quSl77TjPbRaPpKCRl8oPNWSx-UGzUEePE4akbWDyAGY3yOvuVUL9ecITvdanqCWQzrGuR5X2fH3WJockwpG8NwHYth64guCdbZGZ3yrDqResbCNTpw-5JFIsYJpUVvNgkAXh1paEBGoycfna4cuFfzr_PtXj7paCmPr_gvyvKSMDiv8qn5IdQxvT-nGcyst1Xp8SEW2Bpki5Mt60RQRQ8GmEK3uJvdS4Fj8rfDMln0_AbquPuyYBHyURUDuE7On5W1rinbMdAbigRe4bXmesArp1t7BUuEBxtwhFlMb4fpcO-cn06EqqfOKCvbF22z_vi7rbfGXPRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوشش برفی دریاچه مام‌شیخ در دالانپر ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655979" target="_blank">📅 09:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRfhGTX0c7KsK8W5kGNC-ej9rQ7fvuHDFPh2MRUzQi2MlKbI--syfM42fzRvMvRzqZTRSjWMBVmpOr56edIA3q_WDz10d7rffu65VxjvrnsL0iJlqvJi2dzqi9jxpnz4hJvM_R-yfmcuNmHoOv3eSokOUF0FFB2H3BODUjvSpOs3g1vFXeBIEgBIt1Njvazjvyqp4TAiQ1HcpKmf8tij6_cihW6jSnILdTVZsF3zZI3wt0Nin1rdH6K8jpACkA1JtLmz9swHN5n56dubuQcSJKg1LAeXQVQQwceWHjgE1yMSgj4C50KFdXT8mrfdLFk_-sbJRjPrNOL2iKiqwDAZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانی از آسمان
🔹
در مسیر بازگشت از حج، پیام مهمی از سوی خداوند بر پیامبر(ص) نازل شد. پیامی که خداوند درباره آن فرمود اگر ابلاغ نشود، رسالت الهی کامل نخواهد شد، قرار بود همه شاهد واقعه‌ای باشند که سرنوشت امت اسلامی را رقم می‌زد. #روایت_غدیر #فقط_به_عشق_علی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655978" target="_blank">📅 09:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
زمان‌ شارژ کالابرگ خرداد اعلام شد/ مهلت استفاده تا پایان تیرماه
🔹
رقم پایانی کد ملی ۰، ۱ و ۲: از ۱۵ خرداد.
🔹
رقم پایانی کد ملی ۳، ۴، ۵ و ۶: از ۲۰ خرداد.
🔹
رقم پایانی کد ملی ۷، ۸ و ۹: از ۲۵ خرداد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655977" target="_blank">📅 09:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887fa91a3.mp4?token=Pimhilx3sj8U1SgtUPpd04al9dREAEbIT9hm5i0cXk6T47fsqdQMMIxvbrRbBd96dHBOn-yzGsTzv04TM6ducE6vVDpd5m10_q5Q9ZuEto4R-XUbxQJ3WzjWAq16YE_-u4slrHmy2Ww_WfcMSZ8kOqGCIRpa9hURmX7MtP2SDGb8BAI1k3QQIwLD5RgrT1DL01M5lCFU1-vI3Q0drnwD2b_M1edwvCjUyQwx8H041eL_IBi5rszw7BXWOEJzDpceHwrHd17cI5mP3-h7QmOKQWvOgRFBMfyxEPDuWeSECYsiKUqMYy9vhrb6QR44wILvFzx6LkZvSgd52XxNw0SI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887fa91a3.mp4?token=Pimhilx3sj8U1SgtUPpd04al9dREAEbIT9hm5i0cXk6T47fsqdQMMIxvbrRbBd96dHBOn-yzGsTzv04TM6ducE6vVDpd5m10_q5Q9ZuEto4R-XUbxQJ3WzjWAq16YE_-u4slrHmy2Ww_WfcMSZ8kOqGCIRpa9hURmX7MtP2SDGb8BAI1k3QQIwLD5RgrT1DL01M5lCFU1-vI3Q0drnwD2b_M1edwvCjUyQwx8H041eL_IBi5rszw7BXWOEJzDpceHwrHd17cI5mP3-h7QmOKQWvOgRFBMfyxEPDuWeSECYsiKUqMYy9vhrb6QR44wILvFzx6LkZvSgd52XxNw0SI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان ملخ در دهستان درونه، بردسکن
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/655975" target="_blank">📅 09:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8YWHvvNUQ25dpnAQQHgD47N7fmb1u8IqJbHk7GbFaH5UkhiMO_ZqNKGuKhe5rk229ljdCuMlQXOpcN_uAVl3EQsMpoRAodfOvVrC3A-RIFIF5e59h0bZ7cF8cET12hukqLB-Tnpqq9EX23tXyqeiRYmpONo2-mqZ9zN_4ey9zEOu7I8U5aC1rsCJp9iSBFV9Ct_9h-gg3MGQVkh8jr9RlnPuyhg_s-4SVF3KCf8ZsmYr9t2Cc06g6Wq5ZjPW3qlyoSQz0W_gGvlDUIVjSnY4zeAhD5WfuU0YPV99aya0RSxCOf7kcpEg5i0lAnMp5LUtk2coepTuR5Y-uAgJLZZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۲۰۰ملیارد دلاری ارزش بازار رمزارزها در ۲۴ ساعت گذشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655974" target="_blank">📅 09:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kul_M8a7Xf7VzDUrMEAYzaC4K-IEors6Zh-DfraN1XDqZgzCByuKy1qArocmxJctqX626N2HNOp9c7hyefN3irHUtt3Esc3dbHB0r0_IIIp8sf5hHYvUNflZjbK13X-7myBuqF0T1Hc2BaRuYGWnSviO29WI-FqUeEupyTHDKLCVAMMccp-2NlK3AcsSTgLZBKz-a93kHqsQjTu2I5CzlRD6bYDpi2HG8WTftcfNWQoJ4c8_5Cr__f0wI0daP1akUujM0_enDTwLcBMHzJeRp2BeEQTfjNL9-UH8-gpDhUSCylME5YIpIWx8a7BbSMEKIP4I_5T6xS4oO_NmXQFOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیلمان، گیلان زیبا
🇮🇷
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655973" target="_blank">📅 08:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b574136a08.mp4?token=XIQAH0W8-2QM3EsU-NmrDAMEoZytncbkRWjwcI_EhBvRBOo7aTHp9QQSGaBjdSOPGcnumgwn6bA_IlMghLfpIGrTETBUBIQRo6iRSxxLwxtrA8vXzfVoIt7Sy-DysjKQveEXblcu1XrD1478Mq_g_gpe5KNQzHYnZT3gVctIRAfeyVd2xiO6pRmEyZ2ZB2eCz4YlFHCXuGLuwGTOPsHksP4bGP0os3CBoRKdRDNZPzXOEXkpHflSQafnlBH30N7v81OmTAg6uk3dkmLkp2XjO7UjQnwDVo-U0E81ywAIKiPUznAlAD5vs2AbRjpWbygz7p6zGtvNaGSJLJo4yNuCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b574136a08.mp4?token=XIQAH0W8-2QM3EsU-NmrDAMEoZytncbkRWjwcI_EhBvRBOo7aTHp9QQSGaBjdSOPGcnumgwn6bA_IlMghLfpIGrTETBUBIQRo6iRSxxLwxtrA8vXzfVoIt7Sy-DysjKQveEXblcu1XrD1478Mq_g_gpe5KNQzHYnZT3gVctIRAfeyVd2xiO6pRmEyZ2ZB2eCz4YlFHCXuGLuwGTOPsHksP4bGP0os3CBoRKdRDNZPzXOEXkpHflSQafnlBH30N7v81OmTAg6uk3dkmLkp2XjO7UjQnwDVo-U0E81ywAIKiPUznAlAD5vs2AbRjpWbygz7p6zGtvNaGSJLJo4yNuCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اولیه از فرودگاه کویت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655972" target="_blank">📅 08:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cea969d.mp4?token=oPJKYn6-goBedFvuPwsM962YDZ8JsBwFPUt1wCOeTmDqmH3xqFepbXlUhQmbvPyle2qxjFhPjz8HHOLJq2Na3jLQAdQlKqxaRzzkh_0yP0CUhCw1Wc_QqpbKfUAZ65CO_NuTt18EP4NEZFPrIQlUD72hLfTlPiwtVvuSnty6VPUuM5QRLSlG-GjQqWGQiqqdZaa5XjBpA84O2jNizBPe_1vsRX4liNvV4JsrnQC5SkLYg-ZNSpGO7uC2bHaX5aRjGBKGe2nnEey6TNHBvsd6eZiuyLj57ks1qOEMvF7nhz8fCsBXn8iCmQxrmgjej5mIWFadAoz95N5HpIeF1DhmAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cea969d.mp4?token=oPJKYn6-goBedFvuPwsM962YDZ8JsBwFPUt1wCOeTmDqmH3xqFepbXlUhQmbvPyle2qxjFhPjz8HHOLJq2Na3jLQAdQlKqxaRzzkh_0yP0CUhCw1Wc_QqpbKfUAZ65CO_NuTt18EP4NEZFPrIQlUD72hLfTlPiwtVvuSnty6VPUuM5QRLSlG-GjQqWGQiqqdZaa5XjBpA84O2jNizBPe_1vsRX4liNvV4JsrnQC5SkLYg-ZNSpGO7uC2bHaX5aRjGBKGe2nnEey6TNHBvsd6eZiuyLj57ks1qOEMvF7nhz8fCsBXn8iCmQxrmgjej5mIWFadAoz95N5HpIeF1DhmAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایگاه خالی امام شهید در سی‌وهفتمین سالگرد ارتحال امام خمینی (ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/655971" target="_blank">📅 08:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78d99f5f8.mp4?token=MHYghyfkyjGeMHikpz07sHcV_-cgZdjp2SUbfUnU-qhfbWyeZSzx8RclBRjle68icqOd-7Cm6ULpRS2sm5_5cHHPIJ5oNOjqBlttvyunJAoKj-_ArF2K8B5tC91BhqRP4C_k5uLukHcrV52AVDF4oIhHO-c0lq7fugKFWBG0Nvxa-tDULw52xhEVtoL18k8cg3GvDoFlBwhMJ9wPsaUULsyGhfExtBujyiH6UQwOftFXrq1S95s4zdZHR7A2E0kUutN9VcuMBVshIZDgei5tEmIn5usTAq19k4y4WZ4IDRYzE-uuFF-PKXV4DKqEZZ5uQxivq_V055Ti6HMqQiWxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78d99f5f8.mp4?token=MHYghyfkyjGeMHikpz07sHcV_-cgZdjp2SUbfUnU-qhfbWyeZSzx8RclBRjle68icqOd-7Cm6ULpRS2sm5_5cHHPIJ5oNOjqBlttvyunJAoKj-_ArF2K8B5tC91BhqRP4C_k5uLukHcrV52AVDF4oIhHO-c0lq7fugKFWBG0Nvxa-tDULw52xhEVtoL18k8cg3GvDoFlBwhMJ9wPsaUULsyGhfExtBujyiH6UQwOftFXrq1S95s4zdZHR7A2E0kUutN9VcuMBVshIZDgei5tEmIn5usTAq19k4y4WZ4IDRYzE-uuFF-PKXV4DKqEZZ5uQxivq_V055Ti6HMqQiWxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: حمله ایران پایگاه آمریکایی «علی السالم» در کویت را هدف قرار داد   رسانه‌های اسرائیلی:
🔹
در این حمله یک ساختمان محل نگهداری هواپیما و تعدادی از پهپادهای مستقر در این پایگاه هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655970" target="_blank">📅 08:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: ترامپ از امضای توافقی که در آن مستقیماً به ایران پول داده شود، خودداری می‌کند
سی‌ان‌ان به نقل از منابع:
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، به مشاوران خود گفته است که هیچ توافقی را امضا نخواهد کرد که در آن ایالات متحده مستقیماً به ایران پول بدهد.
🔹
بحث‌هایی درباره ایجاد صندوقی وجود دارد که به محض دستیابی به توافق نهایی، میلیاردها دلار در اختیار ایران قرار دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655969" target="_blank">📅 08:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnRP8CJvdAB8-1RSQhrW_R8rtzbLWc_qOt3tt_dIwEQZuQQVTozgXviYBgitN9Wlr15feS7wtXkx6Ymqm7s403iRVSvAnjUWi9vdsck4UEONNztGbBC_TL9Auvtjik-2PvuTO2xunZJetGw-ZGe5iLW0tWwqErvcVkfTnBRHUHmViFXChxoen7JQ1sd_6azQrBEzrrJ4SfNyIadP7H9fK8bz3UbWHqPHjYCDkOGUhR3RAZOTYCJQVCKS9WfQvec7KO6aJGv9B5ULDZix87C1-kH9_MWM4Pe-O7TG6X7GtAuCGE84ZJqYtuhVt8HIQWNNuNfvh5zYNccFR1UwkihhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲ کشته بر اثر حمله ارتش آمریکا به یک قایق در شرق اقیانوس آرام
🔹
در ادامه عملیات های ادعایی دولت آمریکا علیه قاچاق مواد مخدر، ارتش این کشور اعلام کرد که یک قایق متهم به قاچاق مواد مخدر را در شرق اقیانوس آرام هدف قرار داده و ۲ نفر را در جریان این حمله کشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655968" target="_blank">📅 08:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEh-YP_uL3yyrMJ_87ZrIOeCm7UZoCnzMJWVVAjeTZPiDrbH72cml9wkiR2Mt7PgCEWkHm5Xwz5fjwI4Er495FFeYINrduSUa9-apebCPuJnFCvewUvFBNTZGxecqkmHTvFMXS5wRMH9HRwe3m7iKCkibi4n2aD1dvRnyaG4wdxxLLeuy2WtXYLz2dEaRyAbeEIBtyhq-btosNE4JDjL3PjA0gAY6FzXwkb7KNlS4-XVezf9aEfdBuGY5yXxShwJhzL1ajR5LRZT6sBcq-nX67R6B6dIzcQHvpEhwjDeLJS9mOyeiBlKCt3LuZn6YGj93sMSYa23E0-eDhrusjyGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۴ خرداد ماه
۱۸ ذی‌الحجة ۱۴۴۷
۴ ژوئن ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655967" target="_blank">📅 08:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4-3VRzvxnOWSjbgZXuhnkKk5lCms7HLZ8DFBsKlmjJeboIfeth5V8Et5XZHbvnw06j0EGdH6c1G8afs9e2iDswxNwLacqFFjuGObpNbyQmVQOEmaudwTLv5x5gIOGBwI65-DVIVIsXjASQhJ1B1Jwy1PWkwDE-obYcCOMhkAmF1LAf70rboW1h2atzaUwzGC7NKjbro-YnLEf1XyDuCMPgGvJylNJ8aiD3P19DYVMpM8yiykY86GUwXrrHFi9s7upS8jWoWl3_HGRBt9L7QW7GVzBBMatOe4Gm7nYQ-FdfdLp-tdFQFsZzE7JL58gbq5QCfk3M156f-esCoPFUkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرف دلت را با امیر غدیر بگو
+ هدیه متبرک
در روزهایی که دل‌ها در انتظار ظهور منجی به سر می‌برند، در پویش «
نجوای غدیر
» شما مخاطبان عزیز می‌توانید هر آنچه در دل دارید را با مولای متقیان، در میان بگذارید.
کافی است با مراجعه به صفحهٔ غدیر به نشانی زیر، دلنوشته‌ خود را خطاب به حضرت امیرالمؤمنین علی (علیه‌السلام) بنویسید و ارسال کنید:
🔸
ghdir.ir/k
🎁
علاوه بر قرار گرفتن دلنوشته‌های شما در ضریح مطهر، به ۱۱۰ نفر از آثار منتخب، به قید قرعه هدیه‌ای متبرک از حرم مطهر علوی اهدا می‌شود.
@ImamAliNetFA
🔸
🔸
🔸
🔸</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/655965" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX6zF8xwGgG7tabzNRsD0w_yiFlzS2loP43dfhv74RH839FwZOkselXSxTbaYCUCxrtd7RyjlEBPRscieP_n21YC0f9AMxdp-8T4TkW8-XWEG1xyQ4HdD_lU0D0nGJmOey0YqyujUUluVGCMf_wFQX5xQAq5DqVQzOyA8R3iwn7u8q4UKH7nXm5EIO4DkFKqkOaLNBech8GlAU_Pz6YtR7dhFsC3QeIGepLMcZGzVt0vnpZGW2Ayacj1Y58FXrm10fCYQ_2gbuXUwm9tsU-yYwIBfGKXt_zJAj7K-26FWJ4xPTw4hLIkkr1Zu5C3Nq6GIgBwLXi0abImP3kVVDbYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swtLr394GlLVY9pYkXys4O3MCJh7eNl4NHpzYf4_NXDWmQCV2ag95UfN04YfVsQ6toHlzV_bR7zSRm6uN6OzeJI-GtFlf-MuBRrL68-4ncYO2YNTihIGfilIPbShYMntLJwCtFywmnRozOjbzHK1Nyg9C0JOuZf59CdCuM4ahHM_AmOvLmVIttGW0UngjBb1KSFEFdsC9Rw7oDGl0POTMyvzLjhzHmCS3cvnxKm5F_5tDC0R9FEh1HyOyWCFncUPvokrEW1zphkvWgMax4gUfKQWKx77jCrTu0Gbd0I3e7cZizd6C6cp6R7ZFKqt7kUHtWR8zlb8Yr3eOZ8ME2-TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwX4za3oOeXOnn65a3IBs1de-mRCOekNajK_ppU-J0BsAMyIfLGa1oXvyhhvgaxxpVUY7Y9r1bRxm1Aapc0olQcWJo4Bt6xJtxRxGSfdFbMTzHQq_qu3-N3LwzT9-U_E6vP8-BdaMerIZYlv-FRCqNwYyI0UPDliWFdVKPAG9lG4VEdwEZGgmbKZPXkHxXF3iH6tYSjLdrZmT4CVaCHCgpu7PhCvacX73SkjCm0RDtUSY65DCsiJXgbzRmC-ptkrieGE_F-GT0KbTbFh8hZ3Ziir8xOcG2IswgDCRNQh7TMEFvSpGiqXkisvC2Yk-5_TNTaafv_XZSWEN1a6K4LHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMkGduz4Z3CMBDHp-vpQYxrLcu_CsE09vGULHZvyguIo4th27W40TvjPC1TkcWu7ZAvGBZY7owP5elahMP0DgXd4A9gDpOkck_IJ_cZ8fnpdPpbhqG49yf8Y-2Q02G-Q1XDX3GLSqBnIehw_-M0p759OUYJw4K7a8YkM-jy_PboEkdF0OG9_PEJQHQUP7onQNmhH1T_1cOQt6Ou2NXEqMljyxDnKquZktaapWLUCMmGmpfdvyGV5p9ybdD5nL81CAxlwfZpev-RS_ZTQtvdpUm_uZPKwv0Lxz0D9aIecE-zWaEgmpOZvZVSeiG-FIbNnUB4UTGeXEjxRJsU2oc5EHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTvARff7C1v-Hng0C_LIp0rno4dZbQf7_klEY9Mq1_I5XorA-m4OdJVQZYPw-zla1nAFtqc4MNHVxdjQZ6X_HTJJA763Cymnb_fL-AnUoKjI7I_TQDhrjByxAaDwD9X7vlUp2VBRGoF-MnfxfLqD_PWjY0uotyuUFUCHbYqpzFelr1FW_6zT2_X0RT45oZKNOvAhzxDRR5LsgbC9OKEnFK9Qa-qFdJisnmwiba4_ZA9DU7Aiew2P_ZbmAp2CPZw1DSaP6w_mgwnLUYKvuokN4iHCdbnOgRyydCmJKvp3mJ_zEVIxy4T-x94siOHX1iuJEM7_d6io7lAUGITXILEB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seVJkI-H-DmscgmjB-n4msZje69fyp1lpfH628k-VSm6Ky5zsrIZVIX7oo842dtogDaog797BTk0gn1h0fj2eaXjyS4EWLEStm9oEAxcefTGDX_vNdA7IXA9vafBfYPSMkInlfKwyjf6S3E4DHToEY-Etz62VRJCooLw9HYo9V9pjdyypDSOdMnm3Zrst8RuSrrJ9b0rNnhJhcnp0xrxC-iKkurrc421KmAu8o45Qwyu2FxbtdB0Eyjb5LwWKyc9_LuIENghDW5uIUaYvjbsKMaJBvSh8qYVg0P-bXrO0Rw7gEYQ1o9AKx5oLG5kzvLt7k80kgCGsN9WHIeuPZPLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXxsd-PvF2hLmOa49tI0Fon0JORYw-oDb_dipMdnjiPeUXlOhM-2OxylMm68o7vbW6MZby_CApw-_Vi9tWV1XP2lDi9M3Q4kmmqC2B09p_OPqT_NmQackKP_2tvROisGf-DU_LsJeg5Z0kQT-2rLOd9wgKl4cVEv8x2jnBFaj4kB7exj4n2PZ7t9-vIM2y5Bf3E1ZrlfmaFLvakCO7fxI-R7iMXTMnGDzNrckpYY6CFkk0H-1ayBRnbaxXX4TkLW9BltasrT-963YEFwRtP5KcAg5Xee6J6HRLpKGzfmNMjZj8d9fS6JyihhXpmrEfj61t9LJg_0PrAOr5W75TePUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CytGKtMjem6W2PaoC6NmVUIcgHgD0kTp6V46EJ6uH2JHWXMy0yYt4tgfe_8ASBXrxvUUhFWG17ik05CNY4opyr4fManfiEwW6zgjA-3IXpYpqvpTiG-PL3DO6ueNgejRTpNHxWDTwDmOxW71GA2YT7dJL2rUBK0rpf4bIv2eS9cmb-GjrmulgFsSj9jIXntm2dYTuVMCNqIytdr3ZHW9znFHw32ZbVK-e4PKXSAzdf-kt3zUzbjZuOXa_enIkWz2O4OuaUrDrzNMUnH_UwjPrKQ6xPei6o_eoQWC8hqIYQ7aZcwBtB6Pau3KCqomr5LLCJfFBILA-KjL2YGZY1CxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewxo5-2OneBzunYt4plWpu0u_EskX5Yy6IogedGGlDpKkkC4hiphHK42hKddoyuSEloFA0AwyB2YcalgS2uRhjJaGwWhw6eJ7SiUJAWy3xljSm4AX0SADF2azW4PFIHY5dEd8NeQBNNU2WdhS6SYzPv0JsjPX6GfBHJuhRJvV96_2hLc09HvhoTMMkwwsJ3znSZEfWiVs7Q2L_vwadGLRvX30rWiCEpztKuzxJKkJJUpLrlcJ2RIZ_LDBifHHqhDDO_DEXmegxLubnkLiQx_WN1tHGlB5F3LtMlSu8Pue2IUZ3DWSxvprgYUMLBK_ywRpqvsF-K0Rp9KGUMTVCpwaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
فردا که هرکسی به شفیعی زنند دست
ماییم و دست و دامن معصوم مرتضی (ع)
سعدی
#امام_علی
(ع )
#عید_غدیر
💚
گرافیک های خاص مذهبی را اینجا ببینید
👇🏻
👇🏻
@gerafic_gharar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/655956" target="_blank">📅 01:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ترامپ: اسرائیل بدون آمریکا نمی‌توانست کاری کند
🔹
ترامپ با ادعای اینکه آمریکا تأسیسات هسته‌ای ایران را شبانه‌روزی رصد می‌کند، مدعی شد: «اگر ایران این توافق را امضا کند، به این معنی است که موافقت کرده سلاح هسته‌ای نداشته باشد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/655955" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c05eb7d7e3.mp4?token=ePTx6ltzlaFF_PARfrXBFASy2iST0Ww4-y9G9pbXwOHoTkD8NPy2FnCjkGxfz4HE7fmfd3G7nEtWs_n1z_HhTKacit9iZwQKa0nSbw9Z1pHz-3KNh6_cd49j6N_H2bm1ZJFpbvinq1YqhusniKKJajIYV2O_LViAYnXmgLh1JYgidQ6GU1aoBeqZGQ4qvEN1Lo3Y0I-l3FiiWrbyToIjcgMGeTY2uZxZ9omHKm4L_tIhCRBmXeY1jWuVSVAWs53yRWVGtzPeLCFnzYsqmhE-KKjuJIavjgIcV0qgTzJAlBs009td74HIkHRWZCWiAfTvEy0_WAtncQGuNGSReI-J-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c05eb7d7e3.mp4?token=ePTx6ltzlaFF_PARfrXBFASy2iST0Ww4-y9G9pbXwOHoTkD8NPy2FnCjkGxfz4HE7fmfd3G7nEtWs_n1z_HhTKacit9iZwQKa0nSbw9Z1pHz-3KNh6_cd49j6N_H2bm1ZJFpbvinq1YqhusniKKJajIYV2O_LViAYnXmgLh1JYgidQ6GU1aoBeqZGQ4qvEN1Lo3Y0I-l3FiiWrbyToIjcgMGeTY2uZxZ9omHKm4L_tIhCRBmXeY1jWuVSVAWs53yRWVGtzPeLCFnzYsqmhE-KKjuJIavjgIcV0qgTzJAlBs009td74HIkHRWZCWiAfTvEy0_WAtncQGuNGSReI-J-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: ترجیح می‌دهم جنگ نکنم  ترامپ:
🔹
ما می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را از بین ببریم، اما ترجیح می‌دهم این کار را نکنم.
🔹
توافق فعلی، در صورت حصول با ایران، نقطه مقابل توافق قبلی امضا شده توسط اوباما خواهد بود.
🔹
محاصره ایران…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/655954" target="_blank">📅 00:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هم‌زمان با فرارسیدن عید سعید غدیرخم و برگزاری مهمونی کیلومتری، قطعه «شاه عشق» با صدای رضا صادقی منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/655953" target="_blank">📅 00:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655947">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74e967f12.mp4?token=EHJAYmzk5JgJu3OinYbFjdFuqTDEpZzWYtRe-UAgtuAm-Pcg1Zqj4FIfOAtmEPGsZB_AbktxpBb_ozdHn2gKV1qAJN8Ej7UeSlaFwRLV2FWNTVz2s9HmfYZ_XyqOoa2K8GpyLj3z-9tB8sabV9pY1PM7jHHfD6lwLIy2t57lY3L8XHrYnZD0KPIwS-hd4CDaR1oLhvGjPW3zhu9z7_E1zMNydAZc2BGPyiHuPh0oPXjRsFXfybe7HVkgJYGC1kHbNcZC4Nxv8ZtRAlFPaVdxEapGCaLxywytTmoDbXO9xTmijkkJDsG9p1qGQRajXYjqyDF9g4XEd3Z_tjwFa4CSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74e967f12.mp4?token=EHJAYmzk5JgJu3OinYbFjdFuqTDEpZzWYtRe-UAgtuAm-Pcg1Zqj4FIfOAtmEPGsZB_AbktxpBb_ozdHn2gKV1qAJN8Ej7UeSlaFwRLV2FWNTVz2s9HmfYZ_XyqOoa2K8GpyLj3z-9tB8sabV9pY1PM7jHHfD6lwLIy2t57lY3L8XHrYnZD0KPIwS-hd4CDaR1oLhvGjPW3zhu9z7_E1zMNydAZc2BGPyiHuPh0oPXjRsFXfybe7HVkgJYGC1kHbNcZC4Nxv8ZtRAlFPaVdxEapGCaLxywytTmoDbXO9xTmijkkJDsG9p1qGQRajXYjqyDF9g4XEd3Z_tjwFa4CSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
پک استوری ویژه عید غدیر
✨
گفتی ثنای شاه ولایت نکرده ام؟
بیرون ز هر ستایش و حد ثنا ، علی ست ..
🌿
#عید_غدیر
💚
#امام_علی
(ع)
#استوری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/655947" target="_blank">📅 00:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655946">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔹
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/655946" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655945">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f398eb77fe.mp4?token=C9Zv0rSfR3Lk81V57wclIj0v79108o3J4RWmK6pGyZYWkUeI5lWrgsHhEdl5ectaFRTB8B1fOnvckcS2lAFPUco56T5JjT7PPpqztLO3DASP0dfmXEP7Ux4RXfr55rwadqfslhc0QmGm54R9k0ZqiDbSpK62qM4f5qzfGqCQHeADWcTG7VSs5ff4n39Lnqv5ojarJeAEyc5-qlnMylb2tpuMTZeycbr1hRUwlRcmRo7lk2kgiC4d9z70NKXixOnA-kdNcbA_tcTRgqXJlylWm6VGMtTIw8qUcIomlGIc2xHJ_l9nSRSHaNuqQPLikzUm_BWuTLZ3sNe3AlrfnY9C4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f398eb77fe.mp4?token=C9Zv0rSfR3Lk81V57wclIj0v79108o3J4RWmK6pGyZYWkUeI5lWrgsHhEdl5ectaFRTB8B1fOnvckcS2lAFPUco56T5JjT7PPpqztLO3DASP0dfmXEP7Ux4RXfr55rwadqfslhc0QmGm54R9k0ZqiDbSpK62qM4f5qzfGqCQHeADWcTG7VSs5ff4n39Lnqv5ojarJeAEyc5-qlnMylb2tpuMTZeycbr1hRUwlRcmRo7lk2kgiC4d9z70NKXixOnA-kdNcbA_tcTRgqXJlylWm6VGMtTIw8qUcIomlGIc2xHJ_l9nSRSHaNuqQPLikzUm_BWuTLZ3sNe3AlrfnY9C4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔹
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/655945" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3RXjD40cEk-hA8proKLXj0oakqMDuYGzvlyRKO129O7ocxMN3jeQZcY6I_yMj39TI9q9UmxLa80DZLICrNZI9UOWnzRO8jVxqbXVCvgEKRgWtxSr6W-dKxB_RV8HmdJ1dZyQRm-Pv6-yfH5-TnooX8K2SUBPssu288Ho9UusTEgjikYgjLPcswdQ0MTEb8IQVZ1ud0p4O9Q07006jd0eNSa4sPFVrrMQa5Sz5RUJCzgBIhk0fTGslFeO1o305W5pkWuiWPIEnHWp3ynRtqAllD7GEpcLYgl5KsPNwUG6L0a-GVaAvBgfQ5mRI3NSFt-vbcBr9_GjNGP1Fyk2lICDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
*فراخوان، رها ۱۵ ساله را به زندگی برگردانیم*
رها، دختر ۱۵ ساله‌ای‌ست که با سرطان خون می‌جنگد و برای ادامه شیمی‌درمانی به داروهای حیاتی نیاز دارد
💔
پدرش را از دست داده و مادرِ دلسوزش با درآمدی اندک و زندگی در خانه‌ای اجاره‌ای، به‌تنهایی از او مراقبت می‌کند؛ اما هزینه‌های سنگین درمان از توانشان خارج است
😭
🥺
با هر مبلغ کم زندگی را به این دختر معصوم برگردانیم.
😭
🙏
🌹
💳
برای کارت/شبا کپی کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/655944" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAvhWSyNbw44_6Os1jii9vB_saAjZLFX9SmemAbdwL43a4mvtwiuE9SWyZ2g9lhM9OyHlOl15HPhUA86OeAORWSZKwKogDC2BKa4n0H2yodcscqVJK1zBxdlzWbuF60q4rfejQQ8s0rolILU34qo4elH92mjf8FalPw05N-Jt4G07N_-yomwwwU2eUU_PhpiwcyPVxr109OLYUmGIJKjcFqD_WPPmil_ZYwri4sj4jCRPmESGgUZM1fiuT1d8TIv6gbqZqYzJe1BPlIbF0fgpskSreSRA4aq7JYqFzeLJ8jNfcU6pRmBr68e83G8rpUD1-63WhN48tuz3TXfNzzF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/655942" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ اسدالله</div>
  <div class="tg-doc-extra">حسین طاهری قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
می جویمت می جویمت باید که پیدایت کنم
می خواهمت می خواهمت باید تماشایت کنم
ای دل اگر یاری کنی یاری جانان میکنم
مست علی تا میشوم رو سوی ایوان میکنم
🎙
#حسین_طاهری
#عید_غدیر
💚
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/655941" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d945556a.mp4?token=uZRMyiW-cEuxG0F845dFL7JrP93Nh2qvvICrN9PMtUi2fTL5InqS4mmU7ieDyPzxUQhmR2yQ-iU6vOidp2X7rCzc-OipvWyT28YZ3uagwm2Ba3k5Z7c-QorcVmoanWpSeAn9oRNMK1zopomcRECy1-8zDKRarGvTjG269CSycOt1WiGXuzu-aHLiJCNL50SpPrUeZXHYloVlIlzKDuOKKJa6R42t2qS6kYdPdKuFHrc8T6y__ebSugxQlRLy3tiqdPrXr0r1cmb98U75ZT3wAZC-8mtskDZ09OXzadkyIFkdyrEgxfUKGtU-53ROnw-IOg0O1uehrZKGfW7vzdBmyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d945556a.mp4?token=uZRMyiW-cEuxG0F845dFL7JrP93Nh2qvvICrN9PMtUi2fTL5InqS4mmU7ieDyPzxUQhmR2yQ-iU6vOidp2X7rCzc-OipvWyT28YZ3uagwm2Ba3k5Z7c-QorcVmoanWpSeAn9oRNMK1zopomcRECy1-8zDKRarGvTjG269CSycOt1WiGXuzu-aHLiJCNL50SpPrUeZXHYloVlIlzKDuOKKJa6R42t2qS6kYdPdKuFHrc8T6y__ebSugxQlRLy3tiqdPrXr0r1cmb98U75ZT3wAZC-8mtskDZ09OXzadkyIFkdyrEgxfUKGtU-53ROnw-IOg0O1uehrZKGfW7vzdBmyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت بغض
‌
آلود دیدار بانوی لبنانی با رهبر شهید پس از شهادت
سید حسن نصرالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/655940" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: دست تولیدکنندگان خودرو و دلال‌ها در یک کاسه است!
فرهاد طهماسبی، نایب رئیس کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
تولیدکننده‌ها و دلالان دست به دست هم داده‌اند تا قیمت‌ها افزایش پیدا کند. خودروسازان خودسرانه قیمت‌ها را افزایش می‌دهند و اعتنایی به جایی ندارند.
🔹
مبنای خودروسازان برای افزایش قیمت، مواد اولیه است ولی مواد اولیه‌ای که نیاز داشتند با قیمت جدید نخریده‌اند و دو سه ماه قبل، خرید مواد اولیه را انجام داده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/655939" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: مذاکرات خیلی خوب پیش می‌رود
🔹
دونالد ترامپ، رئیس جمهور دولت تروریستی آمریکا در نشستی در کاخ سفید مدعی شد که مذاکرات با تهران خوب پیش می‌رود.
🔹
خود مذاکرات خیلی خوب پیش می‌رود... ممکن است انجام نشود، اما اگر انجام شود، احتمالاً در آخر هفته خواهد بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/655938" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/655935" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/655935" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">| هیئت قرار ‏@Heyate_ghatar</div>
</div>
<a href="https://t.me/akhbarefori/655934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/655934" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0YMlm3Ng6ab3ekTq58jvn9WXFwuNsWSBTc_O0btjKZxkRktvY11200QVcjj3CqRm_06qm0hcWLmuHcf80IU6s7PqN1wDCr6T9lN2gJE9vzDZYQp3lqIfZyFZZpIkknQKQi4oBZ-YvebZPUvufIVmx2o0sufGrvi6fbswyE8CoR0hibwZR8xFNb3bWwUL5IfOSQTsfZkcYBpaXEUmOP4FBx2oAuZ5wgG5wvkbRrmGbtEJkUEtdt0rNkI1T3STekYdaKJaYcD4EJI87cuQmMWSAqGlUtiEMmwcLrJ11C0VYwBJGtYUK_bN7xM4qBa5a_9nuchSQZzOrtC5_sbEFp2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5YaBqMz8yynsdpktvLth1UARvFs2aAxLtTWKEoYigRlr-V3r1Nx1KCqSS7K1MikS7VKGJOC5vEiF-kZH-u72brjuL_Z5TWPwsJM84W3EfYvZBsJJ8doEPTPy6EQVcKP4ZJVFbnEIZ8wQHxaN3yu3BahXUI2xoxZMbE8g8tJ2SgV07szkdOErQt-Uwb41_h_ISdDuumZPMYW_bTe4rEYYdvAe2Qs4XUgwNBzPyZD_lyqhVufRnBIk0caNLoKilG4dEv2OEERA1XV2pMDLRXrJ8jGhGL1lRD4gM-vCkG-2-1jO6e6dobpEJv_1Z5CSZpBla-DcOiwgiTVa90zMuT25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuvX7z1TxfP7S0Ck-ECkTXJGP4I1hrdddTTtA1R2njRNt3iJMo-O-VW2Pna5eRlpUErzPnMZvYU8tUAsmiobHsXNQ3A1TmtReg8zSvWvv_KlQmgEmh3EiDHSdGMShPCPpsUlrgUqeemc8SH6eevGckq9wnaGBIY5IqpMU-eVRIxwCOyNz0XG-2OlSTsCYOe_NbtgIXZtyv2a_B7Yb6_zry5VsZMUJSnbR3XYzaW6ygTvF_nK5gpYBTVyHF9gshN1KGSXELVAOynS3ax3X_U9ptpVrdBuHuzZHUdwTbFPUloooY37ctP3IZYlP7f-ERygJDQQ7xRYpVFsfRAkNc7vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gq7B1QVKYGqH2daYhYc1SuKk8Mb6yXFmsknNTSoJ0ocqc2Ze7KIAvQ_qZOGexH3gNgFVz3cDoc-2kG2sNdtoC29teVNfSgWfllXQ2J8A7-MW2Wcga39MrYsJ86itZwxmpBySZyc_nULN7ZHWi33bLadY93unNNEi2z6GAfBz_H_g-XOzj8he1Yn020YAs6w-kM_yXFaqC7Oue0XkC8rztXh1DPz0xmRThTfiKAzsXsbLqXHM-g-CdndOBx8MhZOR8HJv-ZE3MJHEsw7NWTHwDwHLcs-y96yAFtsMjmYMJmYrAXPZBHP2MMpMmj_TUg-Lz7JaalTswVR2zMN_aO8nCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fegg1pUIXiODtMPnZyuZOiilkZINWpdHwoD8qKwdQiOseCDRAceH9wO2BzU2HoWfRyxWQ_5xuHo_1uvAfb3r9BuZqNbd67-IyrVKsWf5S-xnN1WmEyHzU6dM9XYQder9y6_TppL4lNPyJs2RH1WWsyfOeYqHLLTV7tWc2bsjZxnvkJjygYdzM5OdBXVMN_ptUxi3oDyqj2jNps2NLLMJVSyyx4rEt_WN_QX0vrqZqJ9YZjeMQWB_iNYWOl5oQ-DCCZswzhSJ21qgkMNFqVT2Gie6DzfrAjZRxTcPJlK1TKD81Hr5RTIFTSg-ZgFLltmHAh4IVrP4CJgmfWgpmxfHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uurIAvfKzToJHSIwYqmL8tI2c210LU7JKt454JRzsma1CFVRVz8uC0m-fypdSodxkKkkJB4p94AjkbxhVx6pkvA4qPy-mf0eLikdjHwvqZt0ww6P5XQI2hciIeit2B0bjjM-xVjs71wV63cAMN7rqOZhiMmXx6DmJMssG9wRr3jQySyQonPzZkiqfahtkgEgfNWKdCkqqXDBQvp5DCfPrZbkRzho3d1BTPAQ9_uy7AXosnOA76X-pcUHnvhtfGVzRfgexGKhhRjlYH7CzxioioT5hopaqVSzW48HE3mcHbwPj5Qw2eyiHT_QCx7jW2L7jo050u6di9BwAhqHGUobaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBTI8F-KU1_c3vL59NZjR2K8Z8_qyZaB8iT0oEsCYgLPVJwjHX-yYFvpP0CBVaNJKcKcwwtUx3DzhyBIyqOO_DEP9IC-AsQ18wChrqEbTmwGOZ1MOxymjpBldHr0gWidXBwB5UmqMaXq0uQt9kw65BDyC_y_WNf8zb5XPamfaUlgGFejsunWKHSBKEsbkOwrm8cXtqutjhpDzAHSIIxGbqI6Bh_zDq7KYA6MdISzFkq_4txwWKpjtt32HLqJfxhtmxXDrPgvVsNjORVH6cOa3cH2ieEHIQFIEkh7CVVGRpAlNaQsl_WtDP3pqd5lsKG2tA5zOnW1e-BrsCJCfOVSXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از مرقد امام علی علیه السلام در آستانه عید سعید غدیر خم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/655927" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soLA5cxexLzWfO2uokFY-1BVnFHafNw4JQIpTlF7Cfc38sQmvVR9-HOMqag3bE-27Hk35nprPv_IF7WRMypNPhoIx-6tDu_KTAdGtP4IDW9cXpjGZG0L29UfiT1NkdC9KFkLH7K4UjH-o-pdgzZoZWEC7BDkxtqsRLd5QNC1aHGyYPXYBkBOGmsPpkq9vvjJm-JGEFzUH0TPo7he1Kj2P2Owg5Q_Re0-qi_Ux-6Jqnkqy32Maeck8pRVsF70BeB0FjdyFl8J79gRoDP3S5eCuITIfeH_9EtZPHYwdrFX9VQntrY3mILmbonNolX088ZprDsOJyje4DPntEWPGpZcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نتانیاهو مانع توافق ایران و آمریکاست؟
گاردین:
🔹
نتانیاهو، به دلایل حیاتی شخصی و سیاسی مانع اصلی توافق میان تهران و واشنگتن است. او با انتخابات زودهنگام پیش‌رو مواجه است. کنست اولین قرائت لایحه انحلال پارلمان را با ۱۰۶ رأی موافق تصویب کرده و انتظار می‌رود انتخابات پاییز برگزار شود.
🔹
محبوبیت نتانیاهو پس از افزایش اولیه، با طولانی شدن جنگ‌ها کاهش یافته است. او به روایتی از «پیروزی کامل» نیاز دارد تا در انتخابات دوام آورد؛ توافق با ایران این روایت را نابود می‌کند.
🔹
جلسات محاکمه نتانیاهو به اتهام کلاهبرداری و رشوه از سر گرفته شده. او از جایگاه نخست‌وزیری برای به تأخیر انداختن دادگاه استفاده می‌کند؛ توافق، موقعیت او را تضعیف و آزادیش را در معرض خطر قرار می‌دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/655926" target="_blank">📅 23:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
روسیه: ایران بارها اعلام کرده در پی سلاح اتمی نیست
‌
نماینده روسیه در سازمان‌های بین‌المللی:
🔹
ایران بارها اعلام کرده است که در پی سلاح اتمی نیست. ایران بیش از ۴۰ سال پیش، زمانی که به پیمان منع گسترش تسلیحات هسته‌ای پیوست، موافقت کرد که هرگز تسلیحات اتمی در اختیار نگیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/655925" target="_blank">📅 23:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzp_2ofL2ibjEiXg2jp-h5MRkWNaZ_3ZBZpbpDfrZerFQBnDY14kXMr0Kr3BMtnRU52v9mLlEs1Qsltc3OUtv9k6HcD6ufDsvNr58LDiok4hsQFIV5x34rQCG8F9Qo2FMJCLijM8_N6d3D5LnlHVTj4udcXuK8SxSjNLJfgnoPMYt9q1kHZCwNiZ2t6IWVBinCn2j0q_VRSgODpE8Wi32QXnCtnyhd5O-oNf-oGOVxP4wU9VRgVcc2iOAOL-a5uoTJzzzkQqhvu0yKw1rUN2xm9m6TSqI_ufGcFMBYuXzVgtK2GKRLjG09Ou76yR4cCxdIpwQ1WYM3ljTY74T5zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر را روایت کنیم
🔹
امسال شما راوی عید غدیر باشید؛ عکس، ویدئو یا حتی یه متن کوتاه ارسال کنید
💚
🔹
همین کارای ساده، حال‌وهوای عید رو قشنگ‌تر می‌کنه.
#فقط_به_عشق_علی
#LiveLikeAli
شما هم به این پویش بپیوندید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/655924" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
ترامپ: دوست دارم با رهبری جدید ایران دیدار کنم
👇
khabarfoori.com/fa/tiny/news-3220188
🔹
یک چهارم کودکان ایرانی از تحصیل بازمانده اند یعنی بیش از یک میلیون کودک
👇
khabarfoori.com/fa/tiny/news-3219779
🔹
واکنش دوست محمدرضا شهبازی به شایعه تجاوز به او
👇
khabarfoori.com/fa/tiny/news-3220245
🔹
این دختر نوجوان فروشی است!/ عکس مادر در حال فروش علنی دخترش کنار خیابان!
👇
khabarfoori.com/fa/tiny/news-3220211
🔹
سردرگمی عجیب در اعلام روز کنکور و امتحان نهایی/ کنکور رسما بحران شد
👇
khabarfoori.com/fa/tiny/news-3219943
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655923" target="_blank">📅 23:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28189c9644.mp4?token=tUh2bK7yMyrm8lwAyhQlZDafxxiEfLa6_wkO84fhtiJfTfePOsSY76fzizushhjTaKZIEiQiw1S4M55Nz2rUJIMi8Qy3NTtpxPl3OWM1aYHsDVy5u9EiCh3HqPa1awuJXgX0Q5b8GP8YYxPmPNMk3aZ_3txLYZbJ-As7myYbkVgqgiychUp4eu0bA6NkByWL9-FOnsyFewgkRUBAc__YJkPL0gNVs_kLwrMOjCTB50tEWIZsULIk28RS5I4mryxqeBAHZnJLb4MM7RB1_W6pxxvb-kiZoO-XgKHCMhXuFcb55SEQGcGg4g2aUvElkkB-LL-4nkWh7BSwJRyClxM7Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28189c9644.mp4?token=tUh2bK7yMyrm8lwAyhQlZDafxxiEfLa6_wkO84fhtiJfTfePOsSY76fzizushhjTaKZIEiQiw1S4M55Nz2rUJIMi8Qy3NTtpxPl3OWM1aYHsDVy5u9EiCh3HqPa1awuJXgX0Q5b8GP8YYxPmPNMk3aZ_3txLYZbJ-As7myYbkVgqgiychUp4eu0bA6NkByWL9-FOnsyFewgkRUBAc__YJkPL0gNVs_kLwrMOjCTB50tEWIZsULIk28RS5I4mryxqeBAHZnJLb4MM7RB1_W6pxxvb-kiZoO-XgKHCMhXuFcb55SEQGcGg4g2aUvElkkB-LL-4nkWh7BSwJRyClxM7Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی ارتش، مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
ساعاتی قبل و در پی اقدامات تجاوزکارانه، نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/655922" target="_blank">📅 23:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA2WtZYbPemmL5eFrMViTy5sjXLv60tk2wdnxTaAvBtr2pok_cdPwvkqVEk_lY_aCOioHd_TIXtl0blTgN8gjnSXPrMRItj37xjvCUMnnQvMBwb5ZbGH7WlRou1-seoiMYDQIdw1oq1O3jL7p4nK-IQcaXU6oEtQsERBm1kKAN0U12w9jNqaDMpwBT8TaqiZcKNx8yCzxSwVqm7Ay6dlzZ9K3hfMhMDOWp7voACsdPPiIuo6heUu97J-r7NqUrenGVi_ajsFmiPJymPM2cCn-STI2mCXmu367n_eFuqmchiFnKtoa63vdb8qg3fsH47ifh2npEwgSWRsvpIE-FRz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز بمب ساعتی شد!
🔹
دفتر توسعه و تجارت سازمان ملل هشدار داد که در پی بسته شدن تنگه هرمز، رشد تجارت جهانی از ۴.۷ درصد به کمتر از ۲.۵ درصد سقوط می‌کند.
🔹
اختلال در تنگه هرمز، هزینه حمل‌ونقل و بیمه را به شدت افزایش داده و فشار مضاعفی بر تجارت وارد کرده است. همچنین رشد اقتصادی جهان از ۲.۹ درصد در ۲۰۲۵ به ۲.۶ درصد در ۲۰۲۶ تنزل خواهد یافت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/655921" target="_blank">📅 23:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به ازای هر کودک تحت حمایت بهزیستی، ۲۰ خانواده متقاضی داریم / در بهزیستی هم مثل هر جای دیگری ممکن است کارمندی کوتاهی کند
رئیس سازمان بهزیستی کشور در
#گفتگو
با خبرفوری:
🔹
تعداد متقاضیان فرزندخواندگی در ایران نسبت به کودکان ما ۲۰ به یک است. یعنی به ازای هر کودک، ۲۰ خانواده متقاضی داریم. در شهرهایی مثل تهران و مشهد این نسبت ۲۵ به یک است و لذا ما همیشه با خانواده های پشت نوبتی مواجهیم که فرزند می خواهند که ما به دلیل وسواس و حساسیتی که داریم یا به آنها فرزند نمی دهیم یا کند می دهیم.
🔹
نگاه ما در سازمان بهزیستی این است که سلب حضانت مسیرش را کامل طی کند و پرونده دقیقی تشکیل شود اما مثل همه دستگاه ها که گاهی آرمانشان با خدمات‌رسانی‌شان متفاوت است و ممکن است کارمندی کوتاهی کند، در بهزیستی هم ممکن است پیش بیاید.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/655920" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-L-QWhQU3sxRKFB4aV40sguDJb_P9QX5h0enbbjAmuP-yGa1hSwOn8bJFKfUFuVIsOhuBpGAHcm0M0eMM8MZh204wsEC-LpZks55DhhucHbp8J8bt2xyQkv_3YvbWtyZ9X0W0U5CPupAq1NeuTFBVkWjJXQDPi_BkKTPrOokUuzxQZWgYMruN_-F9nHbJGLnLL-ODZZkylq8ekhyKj7KuaGI1NSuZkmlL5WhDdyDyL_9tX3ZFQ3a5r18-Y9uboa0KOHN4seZqCpDCIl1CT6ENiFxhWu65GPhgUszDbKHjgM3ICOfwJnHjqFQoXv9Bq8z2dUV_UTuH20-r3T1N5B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه اصلی مهمانی ده کیلومتری غدیر در میدان انقلاب اعلام شد
پنجشنبه از ساعت ۱۵:۳۰ تا ۲۳
میدان انقلاب اسلامی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/655919" target="_blank">📅 23:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ بیعت با تو</div>
  <div class="tg-doc-extra">حاج محمود کریمی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655918" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
ای دین و زندگی من مولا
بخن بخن ابالحسن مولا
جون هر کی که دوست داری امشب
به ما هم یه سری بزن مولا
🎙
#حاج_محمود_کریمی
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/655918" target="_blank">📅 23:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0FrfCa3jFFQNkQC0146ag-y2lO71DSlN_uX6yRwvy67DNOUEvsCmyv3X0x-oWFoPxVOEH6UNZjzvwKh-IKYrq4OP535ecRq-XYexlEt2aJQShE_0r90hLHg3seRHQVXJmrvEen5s_DZwo5VvovF0Z7FBRjWcuUGQRrgiIPb-Pt-ICMJm4hZyE9pJj8c31DUXmBo8mKjs9axqG9Ym7TfTfRArtxOESM7SkAPs31GOPChgtZnOKHm9L6uI2t2VjhD-waHIJBl8JwKI6-vIO7Xb2VC-CK9R3pGz_rHlyhzZis9cvqejcrQ5F8CAGd4GxV6rm5aDES-NiRiBxwJayHsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت دفاع آمریکا از کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/655917" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed9351f0b.mp4?token=D4S0d0CBbrbMn0pzn5ZWtol21CoOuhgEiA6BshcPYpytq1j79nwcg4tmgRXfXeskSIGlhRi4lWC8JvfRjLDeBZ-EdWuFMSUgt4oQ19WcjBzjof62ojPQqPhB3i4baPnllSPn52Nd0endrNGL21Cxl2REGrhkhNEGKsuJdYmcNLoDAiakrsWWOtqV1JDz6dNNWLDyQRg69w7Mzn5ppaIzh9anJ5pBmZrFJ2b0YhL7by3SE_pmyc4cU4C9pWQn2827k6-kr6zFTIDcA5acNMV9IeXB13QEOVBo-BuGJZPVgT_3KyFlwfm2qNu0sF6VGOEOSPm3-c3qFeISTUCUgzAtwnSJlT941dMvH3McIMytUQ8ornZzTy4HzpETMp229KUprcRCBwfBGl1q6WykncER1rAu-Ne99eP7Q841PCEYcCbSYLcrepmqwzCYqpzO36UqMjm5-k1MxhFCSAEwsczV3MEKMstyCPB-nJZ6Kj7p3ZfTzhTkwXVPFs5mXyam86TPnJdxyDSHibDrvqJiLL-GTQKW43LklpBeN3jAlPUjqjmI9aCtBTVIBQr380aDooiFXs6RYSo2mfZfEHcOHF5Ifh5SRJsA_9vEMMAunT_rUHEELqBfEFjTmhMeEld0r3zn-MLB4DSKu_XBAarrHceap94X12X44DUB61hAOgkKr_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed9351f0b.mp4?token=D4S0d0CBbrbMn0pzn5ZWtol21CoOuhgEiA6BshcPYpytq1j79nwcg4tmgRXfXeskSIGlhRi4lWC8JvfRjLDeBZ-EdWuFMSUgt4oQ19WcjBzjof62ojPQqPhB3i4baPnllSPn52Nd0endrNGL21Cxl2REGrhkhNEGKsuJdYmcNLoDAiakrsWWOtqV1JDz6dNNWLDyQRg69w7Mzn5ppaIzh9anJ5pBmZrFJ2b0YhL7by3SE_pmyc4cU4C9pWQn2827k6-kr6zFTIDcA5acNMV9IeXB13QEOVBo-BuGJZPVgT_3KyFlwfm2qNu0sF6VGOEOSPm3-c3qFeISTUCUgzAtwnSJlT941dMvH3McIMytUQ8ornZzTy4HzpETMp229KUprcRCBwfBGl1q6WykncER1rAu-Ne99eP7Q841PCEYcCbSYLcrepmqwzCYqpzO36UqMjm5-k1MxhFCSAEwsczV3MEKMstyCPB-nJZ6Kj7p3ZfTzhTkwXVPFs5mXyam86TPnJdxyDSHibDrvqJiLL-GTQKW43LklpBeN3jAlPUjqjmI9aCtBTVIBQr380aDooiFXs6RYSo2mfZfEHcOHF5Ifh5SRJsA_9vEMMAunT_rUHEELqBfEFjTmhMeEld0r3zn-MLB4DSKu_XBAarrHceap94X12X44DUB61hAOgkKr_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به طرف آمریکایی اعلام کردیم اگر به بیروت حمله شود اصلاً تحمل نخواهیم کرد
‌
🔹
آنچه در این دو روز گذشته این وضعیت جنگ را متوقف کرد قدرت مقاومت بود؛ قدرت نیروهای مسلح در ایران و مقاومت لبنان.
‌
🔹
وقتی دستور حمله به ضاحیه بیروت صادر شد، ما موضع بسیار قاطعی گرفتیم. نیروهای مسلح ما آماده واکنش شدند. الان چندین روز است که اسرائیل آتش‌بس بین ایران و آمریکا و همچنین در لبنان را نقض می‌کند، اما حمله به بیروت یک نقض بسیار بزرگ بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/655916" target="_blank">📅 23:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ تمام خسارت‌های ایام جنگ به مردم پرداخت شده است!
علیرضا نوین، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
هزینه آسیب‌های جزئی جنگ در کلان شهرها پرداخت شده و بنیاد مسکن در شهرهای کوچک زیر ۲۰۰ هزار نفر، خسارات مربوطه را پرداخت کرده است.
🔹
تمام خسارت‌ها پرداخت شده و در بعضی موارد با وام‌های ودیعه مسکن و در موارد دیگر نقدی و غیرنقدی پرداخت شده است.
🔹
پرداخت غیرنقدی برای ساختمان‌های صددرصد تخریب به صورت تراکم دادن انجام شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/655914" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b43bd65e5.mp4?token=J_K1KDp7RkIlxy7ffeEiWpWRF2BmCdD9No0cGK30FvyUBrfAsHV7w4xCjW_KS7cEQOP3UlBW7gMiA2gueglMlRmUZX4I4cQYwyuAqmQ7nkgfHA-FUMNrjXLjnWTXsHXxIqAQf2ucsVhqC5ecU0Fs4-fl9y8omWrjiVR4l4bYOzyQjUaGklW8OY9a5rekwmK2VdvkAVtx7rMlw8IARHVZRp0r8O7QSHNIrLbHUYv-VSQKWFBtLidTf-ILzQu_6Ga8gT1dLrzuCuYDOZxu_xEGpSIZzq334vf9nmJimBuPW-irn-AnHGicqG3e3b7EXtMIXz0tBjlQ8uN2IuJJDFFm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b43bd65e5.mp4?token=J_K1KDp7RkIlxy7ffeEiWpWRF2BmCdD9No0cGK30FvyUBrfAsHV7w4xCjW_KS7cEQOP3UlBW7gMiA2gueglMlRmUZX4I4cQYwyuAqmQ7nkgfHA-FUMNrjXLjnWTXsHXxIqAQf2ucsVhqC5ecU0Fs4-fl9y8omWrjiVR4l4bYOzyQjUaGklW8OY9a5rekwmK2VdvkAVtx7rMlw8IARHVZRp0r8O7QSHNIrLbHUYv-VSQKWFBtLidTf-ILzQu_6Ga8gT1dLrzuCuYDOZxu_xEGpSIZzq334vf9nmJimBuPW-irn-AnHGicqG3e3b7EXtMIXz0tBjlQ8uN2IuJJDFFm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر اسرائیل پهپاد منتسب به حزب‌ الله را به شورای امنیت سازمان ملل برد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/655913" target="_blank">📅 22:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
صدای انفجار در بحرین و اربیل واقع در اقلیم کردستان عراق شنیده شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/655912" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
در طول جنگها کمک های مردمی کم می شود اما در جنگ ۴۰ روزه فقط کمک به بهزیستی ۴۰۰ درصد افزایش یافت
رئیس سازمان بهزیستی کشور در
#گفتگو
با خبرفوری:
🔹
کمک های نقدی و غیرنقدی عموما در طول جنگ ها کاهش پیدا می کند در جنگ ۱۲ روزه ما هم این اتفاق افتاد چراکه مردم احساس ناامنی می کنند و نگران منابع زیستی مثل غذا و دارو هستند. اما در جنگ چهل روزه این روند معکوس شد. کمک های مردم افزایش پیدا کرد و فقط به سازمان بهزیستی هزار و ۷۰۰ میلیارد تومان کمک کردند که نسبت به مدت مشابه ۴۰۰درصد افزایش داشت. این یک قاعده گریزی بود.
🔹
همچنین ۳۰هزار نفر در قالب پزشک، روانپزشک و مددکار به ما کمک کردند. ما به این جمع بندی رسیدیم که از این فرصت در پساجنگ نیز استفاده کنیم و آن را استمرار دهیم.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/655911" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
