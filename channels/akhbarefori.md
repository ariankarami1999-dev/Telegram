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
<img src="https://cdn4.telesco.pe/file/symKfrijcFxG8zN2dWOabAN-U7IFwZ-4dEsPi2Dr3P3ujuMrLTILq7Ol3Tf1TnGCOfs1izT-iU258h9vkp_UWGWbDiZCsuWHoeo2FlmaYRy5Y5toL8V-68tFLKLrblbrqqfy6wghxAMcs1UcFWGdIOVI1IscUBMtg1vv4S9iTwzKcRUONiLYIOhKlOqz07kNSJd9SPBWhjSib7Ipuxa1AuzD9FZIRhij_ccUwkuow2h-jSU8YVFsudC38guFkyd0ASE2suunN8oKoDQaQRl6YmLHsFc6BrePwhfwvaplZHNAVxcKIJxkNiwOMjwTPD54kmdDym-CKCl8WU43pfZ6Jg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-698417">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0gZlHA_vnaYx_6HvQiSpRTTN_65x1xcYfWHdw9FkZLTh5YYr9yPhuVOyicVM93Ny1HFRdrpBY7aI6Gx_Z5nYcrsR7eC5NDAfyF6WCW4eKJ1rgi9GQoBRIqjwm6kCoqJ6Kgpba8TzHeY5S0IQpPzYjPxS4is32v-DX431sZcjs-tSMKYHdSicl7-Wqd7bxfH8qcPAWHf-iMzmOqXMxI_kk5xplJPuyGOyMC3W0ahCubLC-BNQdOmmnk3xdEuIOgbQBy6wKZRiquSP2GnGodDDAcQ_q_Uuo1NbC9xw5qs5OGN3NXqNuQ2zaQWFp79egTXFaoz4tRFf6kjJsD49QkXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها حاکی از آن است که آمریکا به کشتی‌های تجاری توصیه کرده است سامانه موقعیت‌یاب خودکار (AIS) و رادارهای ناوبری را خاموش نگه دارند
🔹
ادعا شده که سامانه‌های نظارتی ساحلی ایران قادر به شناسایی و رهگیری امواج راداری این کشتی‌ها هستند.
🔹
این ادعا در حالی مطرح می‌شود که مقام‌های آمریکایی بارها مدعی نابودی تجهیزات راداری ایران شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/698417" target="_blank">📅 16:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6a2b8eaa.mp4?token=M5QpdgFR4cRd9HYpJWd4E4OMKIImL4RiwdoJI0cd8_XOclp3wd05G-3Iyi1NH8mazRI9ybwA8tXyvRefCgOR832Sp0PYXyhye3nVcVHBgG73HlDSJjLq5y1uJnrVafrV0wrksHoByzI0qyifi_6RX4yCK765AbVl35hH18DQFZ6D8vrHuRR5Gy9MthXcxucp5GQnJ4-a-eWAdTTwTUhOzfgCSA1FdTbTWPyxcpZzM_fd3Rvj_sQMO2QfeXQF8hSVwoF2f3Go8NM7asI0yeTQjw9CpufrSmabRu-pw5eV14IEfFXcJ9C0a8UD12LEuSP5RIHtNhUag3nGml9ZDy1sig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6a2b8eaa.mp4?token=M5QpdgFR4cRd9HYpJWd4E4OMKIImL4RiwdoJI0cd8_XOclp3wd05G-3Iyi1NH8mazRI9ybwA8tXyvRefCgOR832Sp0PYXyhye3nVcVHBgG73HlDSJjLq5y1uJnrVafrV0wrksHoByzI0qyifi_6RX4yCK765AbVl35hH18DQFZ6D8vrHuRR5Gy9MthXcxucp5GQnJ4-a-eWAdTTwTUhOzfgCSA1FdTbTWPyxcpZzM_fd3Rvj_sQMO2QfeXQF8hSVwoF2f3Go8NM7asI0yeTQjw9CpufrSmabRu-pw5eV14IEfFXcJ9C0a8UD12LEuSP5RIHtNhUag3nGml9ZDy1sig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر که در جنوب تنگهٔ هرمز غرق شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/698416" target="_blank">📅 16:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24adb03833.mp4?token=rywuaUYfXQnsxVD7Jr5x-S8J35quFbRPHz_idKC6y_VTlw50_9m2vqZtTm-5jfBWpjSlepEThyJS2hjKYtTUlfhWKlNlhX-_2kINupuGuq6bHW6o3hGBTyGfTvsxnoCXlUhXV6z7s_0xarSUPeYyX7tthfXyg6BbGDF4ouT8d5gJjHL_LeXUh4phRArBn_-COBbFez2PH0eVPbLMOTlJxd1mahJNlVxg8FZyRvsD6d2nD_O2OnOgfBHjCtR0sy4EDd8c1qP23nvUkuoHAM0_LzGOthbqWt350lQ-EXy5QAGv1zG3iddzuTDSkpNbwus2en4ETeGES1z8JIQcrBIYLryfQrBe3bOsZl5-760VNvyTjVbGKvo1aUAwp14TioT5UJQg5WL2qlZzxUgQAlzd90Q3HxPzWvqJ7ZU-rYHcnU8yQluc4TGdqrt4je8-c1xyw5EDs_SHNIan9MkrMg3jap9ktc9amkBnLtfqfTSlPpf6hf_suh3-gZyZ_beJQGGyZTE86b1RF2Cb7GY9R0KFtIrn5n30aYhO6f92aTZNJtSPtNLowgyn8WANTDyrimoJeqUsr4yVT0xkPbSIK18cppg1aNshuUM76ewdXBLl7deB8H_5Li9uGjMSS63ors6_cYHI8nFe8FEfJis4f7neLLncA-hvf7z-H0PXGKHdSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24adb03833.mp4?token=rywuaUYfXQnsxVD7Jr5x-S8J35quFbRPHz_idKC6y_VTlw50_9m2vqZtTm-5jfBWpjSlepEThyJS2hjKYtTUlfhWKlNlhX-_2kINupuGuq6bHW6o3hGBTyGfTvsxnoCXlUhXV6z7s_0xarSUPeYyX7tthfXyg6BbGDF4ouT8d5gJjHL_LeXUh4phRArBn_-COBbFez2PH0eVPbLMOTlJxd1mahJNlVxg8FZyRvsD6d2nD_O2OnOgfBHjCtR0sy4EDd8c1qP23nvUkuoHAM0_LzGOthbqWt350lQ-EXy5QAGv1zG3iddzuTDSkpNbwus2en4ETeGES1z8JIQcrBIYLryfQrBe3bOsZl5-760VNvyTjVbGKvo1aUAwp14TioT5UJQg5WL2qlZzxUgQAlzd90Q3HxPzWvqJ7ZU-rYHcnU8yQluc4TGdqrt4je8-c1xyw5EDs_SHNIan9MkrMg3jap9ktc9amkBnLtfqfTSlPpf6hf_suh3-gZyZ_beJQGGyZTE86b1RF2Cb7GY9R0KFtIrn5n30aYhO6f92aTZNJtSPtNLowgyn8WANTDyrimoJeqUsr4yVT0xkPbSIK18cppg1aNshuUM76ewdXBLl7deB8H_5Li9uGjMSS63ors6_cYHI8nFe8FEfJis4f7neLLncA-hvf7z-H0PXGKHdSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی یمن به تأسیسات نفتی آرامکو
🔹
گزارش‌ها از حملات موشکی و پهپادهای انتحاری یمن به پالایشگاه نفت آرامکو در شهر جده عربستان سعودی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/698415" target="_blank">📅 16:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698414">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
لحظاتی پیش وزیر دفاع اسرائیل با حضور در جنوب لبنان تهدید کرد: اگر حزب‌الله به ایران در حمله احتمالی به اسرائیل بپیوندد، مناطق بیشتری را در جنوب لبنان، در مناطق نبطیه و رودخانه لیتانی، از دست خواهد داد
🔹
کل جمعیت شیعه جنوب تخلیه خواهند شد و دیگر اجازه بازگشت نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/698414" target="_blank">📅 16:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698413">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
احتمال گران شدن ۴۰ درصدی اینترنت از امشب
🔹
بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/698413" target="_blank">📅 16:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698412">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmCN-q1ubV2Vy5t91i5yPgn5hH98fLYtDVdFxdf83z2KkonsjcuniUpoBt2LLSRDF7irZnB6RBbULquQaFsIXxreRKaDxFIgsNRkRslUz1SYrYU9tEf2VdCWlzocuo_-iNyGkNznTEsX8gDWqcgkT9FSV8Ti778j15tn_pPrlRwdaa2e25L3AWRK-nFG6st-Pb8ezoYXm463n6KG7tVRpTNjrUd8cunCcM9XCJhxvzS0tWmEx6Sq_bQuastWNhkNYRPJqNqWUAHgvK6SUN5dx2oiOOTmiN47S0s8Qq6l1AfXwNHVj6XBb-Wtasa5PGegeFOtiGkKKXXkOUPjyIDyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه باقرآباد بافق، یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/698412" target="_blank">📅 16:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698411">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/698411" target="_blank">📅 16:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698410">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
به زودی پروازهای عمان به ایران از سر گرفته می‌شود/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/698410" target="_blank">📅 16:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698409">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91920d43b0.mp4?token=NTS-vtCBiN5gnTV8zKBhP4Z97t8Kn1K8ku0K5JAib-xUUdqH5fue3IwNiMVzC2hjZxV4Ea7cFvKokdIvKRhl1YsN2VsVTS3nmukcXIGoIxRisbbJC1ahBXrkPq-_JoWve19pB1fq6hATYuEwmvqckSNmrJlu5HU6El3bUU2IClR9JpiWDkQOWb3fOg4wdo7Rqtbp_plnHhgpza9w2mZGNaCMG0AT_wtXXCf3Y4fEh7LjD7CU92hhBI4GjQUrVLTjvFyy9YMzeITlDzzT_W9uHVAkfl4143b4Xms0VnO5AlRnBXAUbPoK2XRwIIwhgFfd2L52MLABTeybqM6qx41kYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91920d43b0.mp4?token=NTS-vtCBiN5gnTV8zKBhP4Z97t8Kn1K8ku0K5JAib-xUUdqH5fue3IwNiMVzC2hjZxV4Ea7cFvKokdIvKRhl1YsN2VsVTS3nmukcXIGoIxRisbbJC1ahBXrkPq-_JoWve19pB1fq6hATYuEwmvqckSNmrJlu5HU6El3bUU2IClR9JpiWDkQOWb3fOg4wdo7Rqtbp_plnHhgpza9w2mZGNaCMG0AT_wtXXCf3Y4fEh7LjD7CU92hhBI4GjQUrVLTjvFyy9YMzeITlDzzT_W9uHVAkfl4143b4Xms0VnO5AlRnBXAUbPoK2XRwIIwhgFfd2L52MLABTeybqM6qx41kYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: آیا میدانید در بریتانیا، کشوری که اسلام گرایی در آن گسترش یافته چه اتفاقاتی افتاده؟
🔹
سه هزار نفر در بریتانیا به دلیل انتشار مطالب در شبکه‌های اجتماعی دستگیر و محاکمه شده‌اند.
🔹
البته، فقط از یک جناح. فقط از جناح راست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/698409" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698408">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش نماینده مجلس به استفاده از عبارت دریای کاسپین در صداوسیما
غلامرضا شریعتی اندراتی، نماینده مازندران در مجلس در
#گفتگو
با خبرفوری:
🔹
موضوع درج عبارت دریای کاسپین به‌جای دریای خزر در بخش هواشناسی صداوسیما حتماً قابل پیگیری است و نباید در رسانه ملی چنین اشتباهی اتفاق بیفتد که فردا دستاویز دیگران شود.
🔹
ما ساکن مازندران هستیم و دریای خزر را می‌شناسیم، عبارت دریای خزر در زبان همه ما رایج است و دریای کاسپین در این زمینه غلط است و این موضوع  از طریق معاون حقوقی صداوسیما پیگیری می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/698408" target="_blank">📅 15:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698407">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای عجیب سارق خانم برای دفاع: یک سال است ماشین ندزدیده‌ام!
🔹
حضور یک زن با سابقه کیفری مشخص در زمینه سرقت خودرو، در پرونده باند ۴ نفره سارقان مسلح که با استفاده از ترفند طرح دوستی و اعتمادسازی بوده است؛ شگردی خطرناک که در آن با طعمه قرار دادن عواطف و اعتماد طعمه‌ها، زمینه سرقت خودروها فراهم می‌شده است.
🔹
او با وجود سابقه در کمال خونسردی مدعی شد:«من خیلی وقته دیگه سرقت نکردم؛ حتی یک سال است که هیچ ماشینی ندزدیده‌ام!»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/698407" target="_blank">📅 15:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698406">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e13e23f8.mp4?token=DXiQMTiqmukJ9ccvELOp4dGK6KKb3__5402XVxrBS_6XS4gsnTloIqlIOJ3iNd767Lli6chgYCRxqm0PrZYwPcjIevGpzExFHW9ppCdpZcgRsY7i-P6IoDk5xTu9Zx5MmZ5sDAsjzccfUJ6NPMKvNkD1R2u3O0DZBxoDVbEuJLKNLEDWwsrPqFVOiXw1aNoVc-uY5aKAp6xGuHa6px9gLb1MXfvzLExdkt6uPt2RYo_-tHaEqyuknXbp0PV8SqDQwKeHPYC16IcWC_0U-D5gdImuaY4jNZ4hrvfApKXE76Wh6ml7dG2iwaRO1gXlgu2DT6bbFtPr50qsi-vefb-psA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e13e23f8.mp4?token=DXiQMTiqmukJ9ccvELOp4dGK6KKb3__5402XVxrBS_6XS4gsnTloIqlIOJ3iNd767Lli6chgYCRxqm0PrZYwPcjIevGpzExFHW9ppCdpZcgRsY7i-P6IoDk5xTu9Zx5MmZ5sDAsjzccfUJ6NPMKvNkD1R2u3O0DZBxoDVbEuJLKNLEDWwsrPqFVOiXw1aNoVc-uY5aKAp6xGuHa6px9gLb1MXfvzLExdkt6uPt2RYo_-tHaEqyuknXbp0PV8SqDQwKeHPYC16IcWC_0U-D5gdImuaY4jNZ4hrvfApKXE76Wh6ml7dG2iwaRO1gXlgu2DT6bbFtPr50qsi-vefb-psA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض دانش‌آموزان یک مدرسه به قانون ممنوعیت ورود دختران محجبه به مراکز تحصیلی آذربایجان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/698406" target="_blank">📅 15:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698405">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: نیروهای نیابتی ایران قصد دارند در روزهای آینده به اسرائیل حمله کنند
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/698405" target="_blank">📅 15:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698404">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ثبت‌نام آزمون کارشناسی ارشد از ۱۶ تا ۲۲ آذر انجام می شود
🔹
آزمون کارشناسی ارشد پنجشنبه و جمعه ۱۶ و ۱۷ اردیبهشت‌ ۱۴۰۶ برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/698404" target="_blank">📅 15:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698403">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=lyfbhnNxakoBv6UXaiiAvQwZbjZeid-xek05HCA4OhGdhh_7MmN8qTRkpK88piqCP1GL2hhzo4yz4k7oih-iBN1AaNpPP5bmGU5GOjMsfFgpGT_VoVCazh4cB4H010PW_TURC9Oj6ICMLhQG50A6iaaXnlUS1QKpAKfqBxD1uznrH6l3EV-ErzPx5WTYYjoYhE9mEZxTwTtAG9lxRcxGhTwrn6kQXTrqcdv57iUheAp3md0uIV0rvYX4QyC3fXt8QawI0jZPVRO1psTc71sSXKRSkpEKpFNUG0m2vGIkNQx21S3-IRuourNykyS9f7ivOiXm-eUX_-b0t99kKSikd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=lyfbhnNxakoBv6UXaiiAvQwZbjZeid-xek05HCA4OhGdhh_7MmN8qTRkpK88piqCP1GL2hhzo4yz4k7oih-iBN1AaNpPP5bmGU5GOjMsfFgpGT_VoVCazh4cB4H010PW_TURC9Oj6ICMLhQG50A6iaaXnlUS1QKpAKfqBxD1uznrH6l3EV-ErzPx5WTYYjoYhE9mEZxTwTtAG9lxRcxGhTwrn6kQXTrqcdv57iUheAp3md0uIV0rvYX4QyC3fXt8QawI0jZPVRO1psTc71sSXKRSkpEKpFNUG0m2vGIkNQx21S3-IRuourNykyS9f7ivOiXm-eUX_-b0t99kKSikd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/698403" target="_blank">📅 15:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698402">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9885e4f95.mp4?token=s5FYSfGJwDVC-AfHlHnFJS5ILoT0ke7VkT9eTuOvpHCrVxXFON8UtXfAHzQWUpgiadCmjaFx2dfM7zypNNCUGqybMI3DC8HBJA1BtplsEr8e6hant3u4R0OWkPGQWOKVtCTNMFYK1sWBdMqUOQzcNCxcNll7eowjh8A1e4lLGCbucpyDyTP7EPy1bJTsuFAGB4wysc6Y9Kqt-KhxxaXmFGDFOnk4-e9F3_xB-dnCKP-E_f8eszUH34ZD9dQiDMl5uQgEs-O-Wn1kLq2EuMpIwfKs2ifRBVqgjRyY5f-zgM0dGYLYLnrmGbSmzFXsF2NUuXXrrJC55jlaSJ4LKCn3uDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9885e4f95.mp4?token=s5FYSfGJwDVC-AfHlHnFJS5ILoT0ke7VkT9eTuOvpHCrVxXFON8UtXfAHzQWUpgiadCmjaFx2dfM7zypNNCUGqybMI3DC8HBJA1BtplsEr8e6hant3u4R0OWkPGQWOKVtCTNMFYK1sWBdMqUOQzcNCxcNll7eowjh8A1e4lLGCbucpyDyTP7EPy1bJTsuFAGB4wysc6Y9Kqt-KhxxaXmFGDFOnk4-e9F3_xB-dnCKP-E_f8eszUH34ZD9dQiDMl5uQgEs-O-Wn1kLq2EuMpIwfKs2ifRBVqgjRyY5f-zgM0dGYLYLnrmGbSmzFXsF2NUuXXrrJC55jlaSJ4LKCn3uDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی دقیق رهبر انقلاب از آینده فرانسه؛ آشوب، بی‌عدالتی، فقر و تورم و نقض آزادی‌بیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/698402" target="_blank">📅 15:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698401">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
برخی منابع عربی از حمله موشکی جدید یمنی ها به عربستان سعودی گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/698401" target="_blank">📅 15:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تکذیب شایعه مشاهده پهپاد در آسمان نظرآباد/ پرنده مشاهده‌شده هواپیمای آموزشی بود
🔹
در پی انتشار شایعاتی درباره مشاهده یک پهپاد در آسمان شهرستان نظرآباد، مشخص شد پرنده مشاهده‌ شده یک هواپیمای آموزشی فوق‌سبک متعلق به فرودگاه پیام کرج بوده است.
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/698400" target="_blank">📅 15:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN-S60WVQeHDuDc42L2GDOLEOcPUQ2gTxGOPEQ5VFaswVGNmBAXiRSUMp-2u_SQF0XDyrflaRAcKFiQm3AHPdfjfc6tUpVfWhC57MnQ-G9ODbIxZjpvt5O6sb5rCBbizga0OmGyRLltLpRxuqHdMH-QiHP-MgCRjFsqOyCGTccvA3BWm_nuP69WLsbLVAQDTIlGzlhnS5YJ7qDnxDygzx5_iMul4gQSd1CDHMdXNTiI43Hfr8El_1zMCk1PyDcXvuLojHHfU9S8-TIwzO-0JU3X7VoZoIH3Mc9kvNo19UfWXEhaWtdDUBmOvUvYbUWLaWUVv6ezKuXwjIlyVn0PuzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالی است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/698399" target="_blank">📅 15:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
جزئیات مجروحیت رهبر انقلاب از زبان رئیس اورژانس تهران
محمداسماعیل توکلی رئیس اورژانس استان تهران:
🔹
ایشان جراحت‌های سطحی در پیشانی و لب و پا داشتند؛ من هم بعدا از دوستانی که در صحنه حضور داشتند این را شنیدم.
🔹
پنجره اتاقم مشرف به پردیس حکومتی بود.با آقای کولیوند به محل دفتر آقا رفتیم اما فضای داخل بیت، فضای حضور رهبر شهید نبود.
🔹
از طریق وزارت اطلاعات متوجه شهادت رهبر فقید انقلاب شدیم.
🔹
بهم گفتند اینجا جلسه شورای‌عالی دفاع بوده، «پیکرهای اربن اربا» فراوان بود.
🔹
آقای لاریجانی را با موتور از در خیابان فلسطین خارج کردند.
🔹
آقا میثم[خامنه‌ای] آمد و برخی پیکرها را دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/698398" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزیر ارتباطات: در شورای‌عالی فضای مجازی مصوبه‌ای ۳۲ بندی را برای رفع فیلتر سکوها تصویب کرده‌ایم که باید اجرای آن پیگیری شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/698397" target="_blank">📅 15:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sta0RHChl0ModM41QuOJRd-_ICqglQAXMN5yIbgiOj0Sn7ZTt3ulGzbSwl5STDENVDyweJLWsy6mR8YlkUbBVUItDdM5VeAn6qDYGfRE3SOmFPVro8lbuR3DgSOkHb3YNTPH5NmOsk_J6h3QM7ilHBQGxVxB5VWS2qbFMLPyYLQgmbnygGKX5HBigWsjx4_crU8KsevsmGiowneYnKqltlCEne1_LFLjP8BJspExf2JZrhcHCbE8MXy13BrzGYMvgC1qt5zuQXh-9mTaRQVWEkw5t7qrkdThzk6OtfkKFCPEz0t6t2CJ2rhEqGmeewONZSQUfWBCis2rO5uMsjB5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس برای پایان اسرائیل؟
🔹
پیش‌بینی جنجالی مورخ یهودی از فروپاشی اسرائیل؛ تنها دو سال تا موعدی که برای پایان عمر این رژیم تعیین کرده، باقی مانده است!
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2110329773155025085?s=46</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/698396" target="_blank">📅 15:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سایت عربستانی: احتمال تعویق یک‌ساله جام ملت‌ها
🔹
سایت عربستانی سعودی اسپورت در تازه‌ترین ادعای خود، از احتمال تعویق یک‌ساله جام ملت‌های آسیا ۲۰۲۷ به دلیل تداوم ناامنی‌ها در عربستان خبر داد. در صورت ادامه درگیری‌ها و برطرف نشدن نگرانی‌های امنیتی، برگزاری این رقابت‌ها ممکن است از سال ۲۰۲۷ به سال ۲۰۲۸ موکول شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/698395" target="_blank">📅 15:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d42391a9.mp4?token=R_iAdmjk5BOpVObBu-hjvsUXIMvV0t9FIFf7OYwf9M85QrAttM2NQzq6_rxiGVg8Mm2AnGOgeOujLP0sDRkIZb592Slp3iXN84R0suA0g9RB3R9gh18YWuz6n7FE5vpD9F5HKBDr9NEvkAy7wJQNTfE211HjLFPn1ktfM3KS8mew2wjbMb36NS7yL6OEVpn-klj8fulLhO01kS0YRsNo9MKBam3dRSVUiEBbEUxpYgAM3xtu7mZpwrfR6oIoAWqmXtewfs9H2kViIeVl5o6pxdOH_mKD7YddSQHPmkdM3K2vPKLOVI4eDJUvPUYmZdFL7XnUZMvfup_gfBCVU17dfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d42391a9.mp4?token=R_iAdmjk5BOpVObBu-hjvsUXIMvV0t9FIFf7OYwf9M85QrAttM2NQzq6_rxiGVg8Mm2AnGOgeOujLP0sDRkIZb592Slp3iXN84R0suA0g9RB3R9gh18YWuz6n7FE5vpD9F5HKBDr9NEvkAy7wJQNTfE211HjLFPn1ktfM3KS8mew2wjbMb36NS7yL6OEVpn-klj8fulLhO01kS0YRsNo9MKBam3dRSVUiEBbEUxpYgAM3xtu7mZpwrfR6oIoAWqmXtewfs9H2kViIeVl5o6pxdOH_mKD7YddSQHPmkdM3K2vPKLOVI4eDJUvPUYmZdFL7XnUZMvfup_gfBCVU17dfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس اورژانس استان تهران: شهید لاریجانی قبل از آغاز حملات برای آماده باش به من اطلاع داده بود که جنگ قطعی است
🔹
وقتی داشتم می‌رفتم، دستم را گرفت گفت دستت نلرزدها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/698394" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef27580e36.mp4?token=hBL6u_bnxSV4SovOYPtV6FDpQJhtnnl94UR8BsYobeP31EWgvWjMfYobvjCh3kdMdNps1cOIw0bzzlEe-yu2FhY7_bHL7K9zS1M7W4btppp5A4uX_qqud1BbfgF916oJlPqKtxkQC6ZS3InfxH3oKUti7qJT1HrI7BBGyE03PasF7YFNIYv_lkDr5i6BonlGtLwKJFsouKY1oK644cZozT4msmv4WUZWBT94T6qlkpYh4OaaSgq9CPT1a3nKs71myZtveufNomiTGOkh4Bz4rRgqAEeFGi07S5sp5Hs37OkJSVyiUMh4rHl0NNrb-SxPg5DG6v1wMfy5FZpoo9AYtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef27580e36.mp4?token=hBL6u_bnxSV4SovOYPtV6FDpQJhtnnl94UR8BsYobeP31EWgvWjMfYobvjCh3kdMdNps1cOIw0bzzlEe-yu2FhY7_bHL7K9zS1M7W4btppp5A4uX_qqud1BbfgF916oJlPqKtxkQC6ZS3InfxH3oKUti7qJT1HrI7BBGyE03PasF7YFNIYv_lkDr5i6BonlGtLwKJFsouKY1oK644cZozT4msmv4WUZWBT94T6qlkpYh4OaaSgq9CPT1a3nKs71myZtveufNomiTGOkh4Bz4rRgqAEeFGi07S5sp5Hs37OkJSVyiUMh4rHl0NNrb-SxPg5DG6v1wMfy5FZpoo9AYtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: این حکومت (ایران) تلاش خواهد کرد تا برنامه هسته‌ای‌اش را از سر بگیرد
🔹
تلاش خواهد کرد تا دوباره ما را نابود کند، حزب‌الله را بازسازی نماید و حماس را از نو بسازد
🔹
برای نابودی تمام این تشکیلات، ما نیازمند سرنگونی این حکومت هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/698393" target="_blank">📅 15:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvPH0yCkMjZPkOBwRCohxHgC35IzHh2qtd4RAq13ImZkBAzMb2n1auFTTwWHh-WxgE0yBy3DDAyE6P7_VZasXg9C7KR0yG2FQ_mtAkEsyJrJbOSClY-1ODQuOMrEJJ50qyj4zaFf2xOMG3rdW2v8stSuMNponqx-1Rl-HutbQvkjxxGaLiMElmKNrFD6rAzQ2Ibq1VrjIuyTbYfCP0KsPafMyeqUBO6lYknZVM5AOeRPjVsyKZkOCU8Fr2GwL3VWww2K01jqIB9UzBJa2YwFkqaZehSnC-EgpxNJADqQrkR8AEBN6HHp3nUrStCLxuN3dClYDybdBXl04kQI0CwkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت عجیب کارخانه برای ارزان‌ترین خودرو؛ پراید وانت یک میلیارد و دویست میلیون تومان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698392" target="_blank">📅 15:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی آموزش مفید</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzAMuxBlXZ2z0Gz7P_dvQMoQ9tn-SKYFpqhXVcsgT-N7D2wox7z5SIAIxLTNPkPYdPxKDKg5oK0LeX070q3KJxU_p2Wq-S6RjazjoltvfO9eFx0iXorKtOEZdSvRggwP4D2xFE9pnTDK6agb4tLwb4n80IbmtsOhiZF_4bcJtAgrRTRVEgTd8Edh3R3NsR4E95WEmNwid-UgymLYWmckzRSCXBtvLwoNgjFMa3N57_O3OVrRgtDbmLqVNpsCiq6PAEj--FDycdr5qo4Su66r7HUtMXYLkT9VSUIs2S_lOkSS-mrc4srID3AURVc3Q4uFAoQhK_Z3LPTs7A8qMTeIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای هفتمین سال متوالی
نشان طلای بورس‌های اروپایی-آسیایی به کارگزاری مفید تعلق گرفت
کارگزاری مفید در تازه‌ترین ارزیابی نهادهای مالی عضو فدراسیون بورس‌های اروپایی و آسیایی (FEAS) در سال ۲۰۲۶، توانست با پشت سر گذاشتن رقبایی از ۳۲ کشور جهان برای هفتمین سال متوالی نشان طلای بخش بازارهای سهام را کسب کند.
مفید طی مراسمی که در جریان مجمع عمومی FEAS در شهر مسقط عمان و با حضور نمایندگان بورس‌ها، تشکل‌های معاملاتی و نهادهای مالی عضو برگزار شد، بار دیگر در رتبه نخست این بخش ایستاد تا جایگاه خود را به‌عنوان برترین کارگزاری لیگ قهرمانان فیاس حفظ کند.
پیش از این در سال‌های ۲۰۲۰ تا ۲۰۲۵، کارگزاری مفید مدال طلای بخش بازارهای سهام را به خود اختصاص داده بود.
دهه چهارم مفید؛
تداوم اعتماد، پیشرفت و هوشمندی</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/698391" target="_blank">📅 15:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698390">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVPhb4X7m64psbMQrpYx2dzKBfGWLKuYKezQodjjjX_fP0DwYtTu7vW6J_r_4Bcrm5B_3iz7u-9-84hhUfvArLD_eDnGvz6j3SIgXemYC1QSIHh_sMwhMpM9FMmnoC92sQoTw0oTW04Q5LFzcDXIWKpE6zP6H1meEz1JTHaCll4iHb4hWbmiG4fIAky5Mtxa08OmEMpIDuWAmNC-UXIbXa3yFbp3HCLOf5XkkrSWO_kZ-qDD4snMm6FVaVVne2eDsDYGT3DZ5N8wxkrtSkhJson8wUKGmgze-lQvLocBhBxgCTsSiofOX0hEFibnFQlmh6-HXGWJ6NIxH9i2XWL8Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↗️
🙏
جهش معنادار بانک تجارت با رشد ۵۹ درصدی درآمدهای عملیاتی و تغییر مسیر ترکیب درآمدی
✔️
گزارش عملکرد ۶ ماهه بانک تجارت حاکی از جهش چشمگیر در شاخص‌های کلیدی، تنوع‌بخشی به درآمدهای پایدار و توسعه بانکداری کارمزدمحور در مقایسه با دوره مشابه سال گذشته است.
✔️
مجموع درآمدهای عملیاتی بانک با رشد ۵۹ درصدی از حدود ۷۵.۶ همت به بیش از ۱۲۰.۶ همت رسید. همچنین درآمد کارمزد با جهش ۶۹ درصدی از ۱۷ همت به بیش از ۲۸.۶ هزار میلیارد تومان افزایش یافت تا سهم درآمدهای کارمزدی به حدود ۲۴ درصد از کل درآمدهای عملیاتی ارتقا یابد.
✔️
مانده سپرده‌های بانک تجارت با افزایش ۶۹ درصدی به مرز ۱۸۳۲ همت رسید که در این میان، سپرده‌های ارزی با جهش خیره‌کننده ۲۱۱ درصدی به بیش از ۳۱۸.۱ همت دست یافت. همچنین مانده تسهیلات اعطایی با ۶۷ درصد رشد به بیش از ۱۵۳۸ همت رسیده است.
🌐
مشروح خبر
👉
📱
tejaratbankofficial</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698390" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698389">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf297e606.mp4?token=k5OKC43vR7e-esim98jSOtAIcTfS05Y8auIjo0yQ7QuTWLafS2-8xW6TLqamBoa7upviAnZtQd5yJBcsFYKFMNWQxeBKJMN7ss23UzjRw-mOT4212VrgNgeTU_L3i1xKEio9snfugrjEz2lho26i3Xx1hWeIfvmuGcG3xRM2j4ZAoJzoW6hXtxTh0JZutGFecfEbbdIPT5BehuuQV9O5s_Ky1HsiWjk06Htj3zRBNC0tvT8i3PUEztJI2N2vrzO10RtyDtn1kHVIE7pqzmSDqgf3vfncHfcoIkYiqv658ML5BfhCJbgC29SnFYqcXbxJmMhQFQsbi5r84TFbrR4DDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf297e606.mp4?token=k5OKC43vR7e-esim98jSOtAIcTfS05Y8auIjo0yQ7QuTWLafS2-8xW6TLqamBoa7upviAnZtQd5yJBcsFYKFMNWQxeBKJMN7ss23UzjRw-mOT4212VrgNgeTU_L3i1xKEio9snfugrjEz2lho26i3Xx1hWeIfvmuGcG3xRM2j4ZAoJzoW6hXtxTh0JZutGFecfEbbdIPT5BehuuQV9O5s_Ky1HsiWjk06Htj3zRBNC0tvT8i3PUEztJI2N2vrzO10RtyDtn1kHVIE7pqzmSDqgf3vfncHfcoIkYiqv658ML5BfhCJbgC29SnFYqcXbxJmMhQFQsbi5r84TFbrR4DDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان بهزیستی کشور: ۴۰ هزار نیازمند هنوز پشت نوبت مستمری مانده‌اند/ یک میلیون و ۷۰۰ هزار نفر از بهزیستی مستمری دریافت می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/698389" target="_blank">📅 14:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698388">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNt-tAmuqYEc_goykdIrOFzzOM6G9aMh402b5WPO9qvJZx2YKL3eniKyYb-h_Pr07Ny4dPiAdvikPVS1VtjOlz_uAqpMEhQB93PMDz-jxybsibLzP_9i9s7TPuTXPsoc9CzRBQ8SbsiEFV8bCjOVcodGTQwush8yqP9q-N9dukNEErHoUE2d_alt2XGYZy99nKCJAwvdFF2-nkmpW4PIjBZ4R-xSAy13gTea9PFPnbgZjK7ENBFCHF4RjGG2-NToFhTsl1w6ToMdMmq1e6Ex7NVv5gP75IO4yUiWD12k5AXg5xYuCNQD9NS7XqWPjnLH5adWsH-VAptgsp6Gls_Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای روزنامه جمهوری اسلامی: منابع غیر رسمی از قطعی شدن تغییر رئیس سازمان صداوسیما خبر می‌دهند
🔹
دوره مسئولیت پیمان جبلی پایان یافته.
🔹
اسامی افرادی برای عهده‌دار شدن این مسئولیت، مطرح است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698388" target="_blank">📅 14:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAK1ZTW1JPuG0VbRqHTp7h_nA8RhJ-a7kDZJiR79a0OLuEmZNHU7OmyWyuBo3u3-xOyt2EQRBWAW_MCtqJeZbdBE1bnfhKRE6R7dzuFe3c6l3SLBcOrE3Fv8mTpt7chp1NmYWF14wjqeT4bIu5y2qVqqmBz3m2NvLlZ1SrqZDR92Fvrra0HiLqLM3tv2QzB-lRpKIFcpNL-V2SibfC_as8CSnxswuhho-VyiVNxRV6FFKn4qQ6vt_ZM0LvrXXcBAYaCUvgv8Mvw2Kw-b7PGZNk2WKI4N5kQv4cGLtESHJZ25rp-cbD9m2gz4GShgC-RtRU5Dzhtk-xAMKgtO3jaJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی بریتانیا: یک کشتی باری دیگر را در تنگه هرمز مورد هدف قرار داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/698386" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698383">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyCiO3-NuqheLCT8l0gnoHk3CF_NwRQPVdHNvvNq5JO2ByplpszPGLavlGkJql3ystGlQagmN-jzWEAAzOrl8XKc2hqs5UhJ2_AGdQCBUFB1JUAjYakeEacxzUVn2LfnSbWx7aobV79w1Dkx5sJiTwQ5qjPaV_OMSHVDXCgNDJVW2NPIxlLiIH0Sh8cxkRAE2a1c9rLa1rRg3RfNQ3cGbJUgYFWPioC6Xg2fF3sSEsXa97RDnvBwuOE8f8E6XB1ip-SL97HmJhJJ5SItE_2UEwMcbgx5Sp1VyZ_odOqJoywBKrHtFTHZCYOzgzIQEappEU4e8WKbENzcXxZl7uhWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvA7S-I5lWASQvXv1xEIp33TNgtLEEPyykZdXIjNiDnAKRt4JA-l6TXG5Y1jURMQy0qD6Ji_ZTqsJrBRmkGKXxyY5EYF0MnNV3f-3l6jpjNMFDOH35DtJeRfi0W6xq9amO8ZuT-xibEK-OQfMk9kN6ZOWxPAK-ocVP1QmuMAHwcRk7K-zDnkipC4n-ZfCGtYtpz18US-ng0pW2fnvYHZVmZXNApz0xveL54QpBbFPQi-d4KKD6YAvPlX8fUmU6v4nUXMjpzELX_-pLQ0O3_bfpjUDfV32-S0JgNcRl_sBIwpmFmcYxZoKVKTQvsnEtmnYIDscP4w9kRJeN_PncCL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQB0KCMLfNLiCtthOcUCcWG5nK-_FyyonWaXeUgZJyJMcWjzbzKitRI5miCXcakScp5Dzvv4921Nxn3aMGy4myshDxW2QY_BHgqRA0LKMDNb-gY_dA4B_hBUBzUeauxKU985ZHy3SkEK4aJpYnamtDSx1BnRV7ZAeyg-tkM4hKI8iDkD7KkB-DL4Zfv4gIBEq5l2P5hGFhUtbV-D3T-k_eHHgH0CAwCJFJjYvbpxpLT02cmLmMgC-5P804812opBZkelTjFnA3s_dJWR_1jVOJvdD4nJv4pjIxXkZEfDP5XDCB0huw-f70MR5veynRuLJVGx2rJyI2uz_kfaEXdlow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سه تصویر از خطر، هشدار و فرصت اقتصاد ایران
🔹
تداوم تورم بالای خوراکی‌ها زنگ خطر کاهش قدرت خرید خانوارها را به صدا درآورده است. از طرفی، ناترازی گاز فعالیت صنایع را با هشدار محدودیت تولید روبه‌رو می‌کند.
🔹
در مقابل، هدف‌گذاری تأمین مالی غیرتورمی ۷۰۰ همتی تا پایان سال، فرصتی برای تقویت سرمایه در گردش بنگاه‌ها می‌باشد .
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/698383" target="_blank">📅 14:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bd5cc5d8.mp4?token=RSU5Ffwb54WXYFPbqYwQCCY0vkRaQSrmh-KyBtNhPEINwp-gI7GOWB4eMb5ejS4Ll5IIpi1GHEojoji3fY5MmEoC61X-3BtNTviyhtuSspTXKbdoS3gxzhoE32zZbMh7zpGAfwhyydm6BEH6P9LS4IdSe-gXADiUjRwA1n63fSBULqrZYZ51m83iEIpHN3gT9pbA5LAEV5-gWrZtQBlZCIPVCIBWa0OBsXPCImKvLMUPcKkhiHUMSyosHzAyR6qVzwtI3dKBGDfxH8bPthX1pGQqEc4aGhHsVvPBd9UCBTKPQx1njCxurs66KnK2FlEfXORPnLcIkZ7Ex1XwwivVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bd5cc5d8.mp4?token=RSU5Ffwb54WXYFPbqYwQCCY0vkRaQSrmh-KyBtNhPEINwp-gI7GOWB4eMb5ejS4Ll5IIpi1GHEojoji3fY5MmEoC61X-3BtNTviyhtuSspTXKbdoS3gxzhoE32zZbMh7zpGAfwhyydm6BEH6P9LS4IdSe-gXADiUjRwA1n63fSBULqrZYZ51m83iEIpHN3gT9pbA5LAEV5-gWrZtQBlZCIPVCIBWa0OBsXPCImKvLMUPcKkhiHUMSyosHzAyR6qVzwtI3dKBGDfxH8bPthX1pGQqEc4aGhHsVvPBd9UCBTKPQx1njCxurs66KnK2FlEfXORPnLcIkZ7Ex1XwwivVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قطر: باید برای بدترین سناریوهای ممکن آماده باشیم و همه، اعم از نهادها و شهروندان، مسئولیت‌های خود را بر عهده بگیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698382" target="_blank">📅 14:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3CtaNc0kRGpURd680PE5xGEirr3TdismkYnZe2sBwfuxfUMSANpan427LnvJSOu4vqtvEo94-vtmJ0ZpMwJfE9qVO1bazqcojQDbhZRYJJBtiu-DosokySasAe8S8xTO_H7lmf5SWE3WWSZ90lz1axwS5jWdSNu6wiMC38DHqTOE5TK0DniNEZaUTVT2fiJTVESmDpYUwOHIgR_wWhbeedsp7VsFIdJfWaI5ajwStHpJ3JZ97yWEumBzLkKgyeHQH9oko6XTtDJBZRaHA-1xas7ZFOvw1e47I4T_KikhX7seHQH5w_AezJMt0_4_DY5IGqlORK8p7msPaoiOdDudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه‌کسانی از جنگ ایران سود می‌برند؟
🔹
مهم‌ترین پرسشی که جنگ ایران مطرح می‌کند، این نیست که این جنگ چه زمانی پایان خواهد یافت، بلکه این است که چه کسی از شرایطی سود می‌برد که در آن درگیری‌ها هرگز پایان نمی‌یابند.
اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252158</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/698381" target="_blank">📅 14:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای نتانیاهو: با حمله پیش‌دستانه علیه ایران در آستانه برگزاری انتخابات در اسرائیل مخالف هستم؛ اکنون زمان مناسبی نیست
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/698380" target="_blank">📅 14:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nygb5bC4GbLXrB3LqUQNysW0FHoJqX6qBhnvU6jSnbLL3rsD5g6-rVTR-Wj_cOdH5aqfOekS10kcXeyETUbb1VEqXkZa7EK5cLPcq4mzEnKuNkQirNvrlr5NpBzFH1CtAo9NElQSWWNe2kR7nE1dhWg6-cvM_CQRwH0Iaumx-C0MTv_aFMrskhlKkCqlWO1_CK0PHpAKo7M3W8EGP309vK6Smfxv1u4FA7fApfXltTbhzu8B68PRtKhu7kmvx1lIjxD5paSU9RVTI9TtGncgGFeFJVGbemSWiWIt55Q-Pf2rBWJWGyaAirbdlQsnbjqKfkXdBHeB17iMC9_gLaDQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این کدها رو اول پرامپتت بنویس تا سبک پاسخ‌گویی ChatGPT رو مشخص کنی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/698379" target="_blank">📅 14:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyKyTOwcm2VF9NGGecu_66GGWtUhf5WKBX4IDG-aKK5VcDRI0DOtHOQSc-Ptz6ibheJaCrOt_IIXi9VxVpzMsWzFsfLeQPxhpX4-Bv_JeYRroBYekrxw3AktJpxg4AHweohHL-Nb2Ti6Z_Q24SpVOlK2tLhLIgx6DXDskEtEnimkU_Bf5AYF8C9bdsKJEh4epZLF2ydiBmeIgmEAXA3J2uGhuZLwRCpkHHY2yWPk2DQwRjKhpVZixiXDQOwBVVyOVxhJyaVXDeEB9g-iP-hbR5WkZCDSECuGSIHw3Ut1hx6NliBzsfkOUvnyOZvnjqDIt5DDe3Uc64YqO3WTe8qHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول به دنبال درآمدهای جدید/عبور از سیم‌کارت به اقتصاد دیجیتال
🔹
همراه اول در حال تغییر مدل کسب‌وکار خود است؛ بزرگ‌ترین اپراتور تلفن همراه ایران که حالا علاوه بر خدمات ارتباطی، روی سرمایه‌گذاری در کسب‌وکارهای نوآور، پلتفرم‌های دیجیتال و خدمات فناوری‌محور تمرکز کرده است. بر اساس اطلاعات منتشرشده در کدال، این شرکت با حدود ۹۴.۸ میلیون مشترک فعال و سهم ۵۴ درصدی از بازار موبایل، توسعه خدمات دیجیتال و متنوع‌سازی منابع درآمدی را در دستور کار قرار داده است.
🔹
از سرمایه‌گذاری جسورانه «حرکت اول» در کسب‌وکارهای نوآور تا توسعه خدمات ابری، کیف پول دیجیتال و راهکارهای سازمانی، همراه اول به دنبال گسترش حضور خود در اقتصاد دیجیتال است. با این حال، موفقیت این تغییر مسیر به یک عامل کلیدی بستگی دارد: اینکه این فعالیت‌ها تا چه اندازه بتوانند درآمد پایدار و سودآوری واقعی برای شرکت ایجاد کنند./ اقتصاد۲۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/698377" target="_blank">📅 14:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698373">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P45UDLVfr-p4dTuEuDcGJnIgThTzjmd9PMG1dbWf4oVuf8w6Jg5gT8qwnRWjstabESiMduDfo3_GFSqcTgJPW_4oZ4EeMNKZxdBk2FUUEIYtOCzy0wFtCjNb0o3WUovyFaQKylTqzzUDCQyw5HNdwrjVWsWFQ2635kItyEBD6A0v7SNGHfoT9IiGqhtmYjLok8DkaWNjq60g5y5i3M2ygWMPQUsSHf78A6rCfcLi3R5huZzWJmtNf6D28BVFDGEOWbK2pLxzZ_5Qp3Izm7CcxE_5jO4FzRM9zdc_iwNgvMyuMY_URslAyUupiujAdT7hcAQJkl1TybeMCnDs9JN0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibD9NJifqhaA7YNrKXbeZoxYRXbdqCN5GMbeew5waNta8MfcD1elnhAkwzJVHISx7VqZ0SSS0uig5Y9TdIg0YmsxxKJOk4ZQw3p9csfTFfdusrnr3puQwEDRhL6jPmIProXHSv3gJV27ychsYApXK47niCQPGmJlg_wwpe50DZ9hraML38tOXRJ4vmCqbgX0sAOr5uFxY4PoSWsQwo63pxDkp4FfbXCJZFGE4qcJe7cAk8S-rugIK5v8jmvk15IC-Okyje_Y4MFCECowo7ogIKzULvQHTMik_BLK8UF6vqQIedZU9jTr3xDf1KOIdGM05XzxacE04WFEJ85d5U140Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48ce43ce0.mp4?token=TLHnmHoe5WAYlUEYfv-j1ZQkLOryhoVGox2OzwFl1l-9L98x1pNIF1WPY41dDNNvm6lkKrEwWF3vj_ptBnJMEHvMuYhmXwMir26g1byUdbZ3QCHvlsYjl0z-l9zNjg1kzppewP5zos0SZ6NumkCw3HVVJXnuRW_K-N08dvNkgqHIE2PlEmpScRcUELpqoSMREsM8OKe8me0-ikkmkybSia_Sy4ZEUHGIwOuG54wb0B2EpPKU6yR1z4N1TPbSxcgg64CxIIhfVEFyZjihTyQtYIbtF6fccwDewQgZ40pGUW_kumOVOg-i62TcYxQXJXjYnjV4PBMYdPlXwnCqmL_7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48ce43ce0.mp4?token=TLHnmHoe5WAYlUEYfv-j1ZQkLOryhoVGox2OzwFl1l-9L98x1pNIF1WPY41dDNNvm6lkKrEwWF3vj_ptBnJMEHvMuYhmXwMir26g1byUdbZ3QCHvlsYjl0z-l9zNjg1kzppewP5zos0SZ6NumkCw3HVVJXnuRW_K-N08dvNkgqHIE2PlEmpScRcUELpqoSMREsM8OKe8me0-ikkmkybSia_Sy4ZEUHGIwOuG54wb0B2EpPKU6yR1z4N1TPbSxcgg64CxIIhfVEFyZjihTyQtYIbtF6fccwDewQgZ40pGUW_kumOVOg-i62TcYxQXJXjYnjV4PBMYdPlXwnCqmL_7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر که در جنوب تنگهٔ هرمز غرق شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/698373" target="_blank">📅 13:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698372">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رییس پلیس راهور: پلاک اختصاصی منطقه آزاد بوشهر به زودی رونمایی می‌شود
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/698372" target="_blank">📅 13:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698371">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کی باور میکنه که یه دختر دانش‌آموز، بتونه ۱۵ تا مدرسه بسازه!؟
@TV_Fori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/698371" target="_blank">📅 13:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698370">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7XwHJN9oLaLhR1gA6kp4DrBoW6rH9M8cy-fLRRGbZfdMvQfXvvU4ZzawbJRpA32ZVTcx9_qaYnyTrNqwEsqB8Te5RIYKx-5zyvR3OtUxwjCvnAYdNalvSNcS6cdFrme_zSuuorB_NJ4aCGgxkzE89-8JIbWR-n7gFqR6shEBxWjyUJa2cT2Bs2W8VcDMoVwrnHmgTYUBZSDoIEX-s4Zsxvf_y4SjXXVpky5P7d4v9L8NQdHXHNXICorn5KWFpmc7CdCHBJGMbhQnuah1ehMYgEUVwOyn_7YFuSjEXWZ6F5WT4amfhH16pLdYJ5OZ5LFEZnVobysEV1NQcU-3RhMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عجیب درباره کره شمالی؛ اعدام برای افرادی که از اقدام به خودکشی جان سالم به در ببرند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/698370" target="_blank">📅 13:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698369">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
برخی رسانه‌های عربی منطقه از شنیده شدن صدای انفجار در استان سلیمانیه در شمال عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/698369" target="_blank">📅 13:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698368">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt5q2opSZUjqJKKh42PQnEoXqMjIjdBWUNXh7DARGpZdcmqC2gAsKbq-iJ_0cGzCOcV85E_yMES8Rm5JlusHLlRFrko9JGz9ZJN1YMAs5npTzlYcGtS2BIV6mal4_N5pxkIU-9CTiVmev4oD7m9j1Qk2HaPEoArwn-L0kLzQ_8KwkZwL7U6RuBKxn6pcnhMxWraVbSZDfqrXUVe4h-0TjPq3XvufayHZq9eOX3WY7UEQGXHZ0Odsj-JtlYCz-6xqGGFLPDmntV4Uow0DszJn3G75OIFlLBn4nLLbmukaiKW3GHkeEoH2gH8Gj8vRErvuQTyQIGm9mB_b3Em2tuG7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زعفرون با چی بخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/698368" target="_blank">📅 13:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdJ-pfNQ7ycVbxDb6IlJr86MeRZn0thWjZRSK_5FHF754cIxdEsGDjAknjkpYAoL7MilRts-CWQ4jkrAxIBMKxs0_DRh4J_4YmDD8cFE6ELvgW3GAOMkyTY6VNOw1lxTUSZDVewyKasDOYJayBVgB_ErnK6CinM-pwtrlTsXmH3Z2mQfWV0SIDQfQRu6avz4FhTYrOMLZLeddK2oQlXgQFb91JqjvDZDfkVeQSLMAbOTRo-2XCv-dfsYeYsU3kgOXX6i4A4kek8z8xxxudALMple7Qm4QXTDqPHl7R2_k1ORc0Qmii55uEP2zPnVxLAOxZ_tb6yqdVd5uHxM0EUG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده یکی از حوزه‌های بسیج خواهران شهرستان مهرستان در جنوب استان سیستان و بلوچستان در پی تیراندازی تروریست‌های وابسته به آمریکا و رژیم صهیونسیتی درب منزل ترور شد و به شهادت رسید  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/698367" target="_blank">📅 13:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9O34WNgvahxFDmXp9xXgsawPYKJAhJPHvPoUmIpYiDI76hPF-XYUSEH2vfCbScHD9VGHpqUL6zMUPT1i5dRqmNH4pxGDrx_oACNDN7F6QlNc4OgDWW-sW97OJGlkanz8OkNINkWZgv0JliQZo6hVxlCp7rTxqrjo1doU4h_M0ja8zYlKwIUYlk9rUC880NZW4rCQKuZOM0i-EY7Dfv4h6xqc757NmiZQBur-C4gibh6Jf0sfQGTKyR0YBUFfvL90UwG-KyzPucfpYrL7ZwL_daMOqrLYwqKFKtraMKkK5i_r_FCExjT12hgp5TW6vGT8mKULv8jaNIp7H1LOGlBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلترشکن‌ها در صدر دانلودهای گوگل‌پلی ایرانی‌ها
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/698366" target="_blank">📅 13:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سخنگوی سپاه: ایران در جریان جنگ ۴۰ روزه، عمدتاً بر تسلیحات نسل قدیم خود تکیه داشت؛ اما از آن زمان تاکنون، به سلاح‌های بسیار پیشرفته‌تری دست یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/698365" target="_blank">📅 13:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698364">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMaR784myU8lz_Ng3iRHYb3urXOfaq7pRztFNsZskQMJT8Hjh6tq8y30V8--aNerbdH1x9myRNmfOf68LHZtc5gWQ0dAoRyZYa4fBAAs65RD2R7QefArmK8lZBP1F-D_aDWiIEniIzo5Gnjl2pj0fH4f1dN8pv9stOZ2Wbzl_9O3uiOoTIyfvGlerlo9_b-mgvBLGTfWtRMYtAfVdYYQLozUXySFZsbwn3Mz32_Ykt4OpmwgDpvgAju4JNg42Qu5-ZzWvzCm50jwMoSF8w2Hk4ciSXWSCvyq7ZQwJQJdnBiKG_Jh5hDZRMdYCHBQNeyggaiQONwJ6ufGjW99m7qW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۶ شریان ارتباطی خلیج‌فارس در فهرست اهداف احتمالی ایران
🔹
رسانه امنیتی «جریان» مدعی شد بر اساس اطلاعات دریافتی از منابع آگاه، ۶ سامانه راهبردی کابل زیردریایی خلیج فارس در فهرست اهداف احتمالی پاسخ متقابل ایران قرار دارند.
🔹
این فهرست شامل فالکون (FALCON)، ای‌ای‌ای…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/698364" target="_blank">📅 13:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP5OfHYSwIYho9pMLBdKrR9zO6mKuNhfTildIPNHSiQ8fRinZ_6Iy2iRGyodkcb6S45FdT6IRVL1fVpdUGGP8JH7ra5rUKJJzWBKIvA2jLRr4lJYGvjhfVv6bQb8GDN6BUC0Bu6q-HkMg_8C1HoOkI2PnFxser4CSP7K1EwXu08NDlqQJ_6aYew4AvSHpPoCD5np2uiWPdtwkr4keUIzHUYnKzImrTQtLBJVAw5t7I7VMCuF-VZz0H95uwY-yHQ53vcs_exYdGec0KDDLJ_1x82If0gURGOhMTTNWBpAVie_ckFjRTqKBtp1SJTCoj1PWli7TGRXt9VOiJdwfSbUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسایش در سفرهای جاده‌ای با آروباس
💛
با اتوبوس‌های جدید وارداتی، تهویه مطبوع و شارژر اختصاصی، سفر جاده‌ای راحت‌تری را تجربه کنید.
🚌
🎁
کد تخفیف ویژه مهرماه: MHR405
💳
امکان پرداخت اقساطی با اسنپ‌پی
برای دیدن مسیرها، تخفیف‌ها و خبرهای جدید، به کانال آروباس بپیوندید
👇🏾
@Arobus_ir
رزرو بلیط :
https://jryn.me/YJ4ngP</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/698363" target="_blank">📅 13:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698360">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPhwNqkxYxe9PVmHDaFfBFFnk7dbE6bbdIsPERoewJqqL5X-fCIJPJ4Hjtn2AEUeWWWoDC1TdSa08odOr3XB5U7dlguux3PgpoGXslf0hyE3RWoPn38GHTTlp_f4oQif9sUByGn0hMeUghc_rVVxwjz9kcFY89knFDooQI1_Q1npWu-kXT9Vc6DtUXyBp3DCc7D8eRkpfgSVNxLOIBXY_CxZCsg4rSIS3w35b5hrB3IP7zGDl0UJOi1AOJUOWIq1yLx9phQ9DfFv6YFbnF4JfPuffn_L-Qo3DCpwbFAZd7FUWnmodFladnNd94A5DdGVGpVG1JGJQAWC5GtIR8Abmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی حمله مسلحانه به خودروی پلیس در شهرستان مهرستان استان سیستان و بلوچستان، یکی از ماموران نیروی انتظامی به شهادت رسید  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698360" target="_blank">📅 12:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698359">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f1e63c63.mp4?token=vrxaBCKXhCw92vM4BSt5l9r_lHJWTLXDPcjWIfDu6kWequ-m6m42Y2oiIEfJtaa5DlMNCrjoNhzsTGfYWs_w4KeUxdv3cDmbthyOFVswMl4c4GYPXbhz-QBVDzs7P3vGc-e5JT7J92ujBNTaSnAguZaAFvCJRX8sNejaP9svsa6imoYBO9ci-BzvP41ELW_qd6RgfJ0pW_CL6btjpK-Tfabd04L3OVWjOdhgI2kc_FsZV288cugAP8Shj604G7VunscqOBqeciwU0-l9gkdMSzxxQMeiE9QrgrOyXX6aNvwQ8TsNkahcGh2OKbkV0Lh3_JAG6aJaP3cgMNL-gshEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f1e63c63.mp4?token=vrxaBCKXhCw92vM4BSt5l9r_lHJWTLXDPcjWIfDu6kWequ-m6m42Y2oiIEfJtaa5DlMNCrjoNhzsTGfYWs_w4KeUxdv3cDmbthyOFVswMl4c4GYPXbhz-QBVDzs7P3vGc-e5JT7J92ujBNTaSnAguZaAFvCJRX8sNejaP9svsa6imoYBO9ci-BzvP41ELW_qd6RgfJ0pW_CL6btjpK-Tfabd04L3OVWjOdhgI2kc_FsZV288cugAP8Shj604G7VunscqOBqeciwU0-l9gkdMSzxxQMeiE9QrgrOyXX6aNvwQ8TsNkahcGh2OKbkV0Lh3_JAG6aJaP3cgMNL-gshEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روابط عمومی نیروی دریایی سپاه: یک فروند کشتی کانتینر بر متخلف که قصد عبور از مسیر غیر مجاز و پر خطر تنگه هرمز را داشت با اصابت به یک فروند مین دریایی منفجر و دچار آتش‌سوزی سوزی شدید شد
🔹
این کشتی با بار بیش از ۲۵۰۰ کانتینر صبح امروز در آب‌های جنوبی تنگه…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698359" target="_blank">📅 12:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698358">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
وزارت خارجه: ایران و عمان درباره تعیین مسیر موقت کشتیرانی به تفاهم رسیده‌اند و جزئیات اجرایی آن در دست پیگیری است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/698358" target="_blank">📅 12:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698356">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6638d07252.mp4?token=RLjR8UjGiF17iS_6Hnrl4VZpUQ605Db50a5mAXeD2p4rL8XgGx--tepMOiAY_Fr_4dp8ih8lmo4FT9resIbVM8JEaMqsQsOupYINQwPmUT69N3q-ErSvTClxFCh-U-6fkj0JjLmOmeCGL-AouLEnz5AGcYXcYaLocpWMX3mZbDfKv7wH01HpKRqhjPnpojtNHn0RscnzrWcaxixgoguXOabBgNRHdWz9LHd1VhyOK8YC1k1bf8HPC0X7KC1UFpM8XUszQTV9YQnjN1wtdfHOPCG_gaU5IZBf1XETwaUJCqdQhCd8FsQwiphGNPAL3LfqTeHhaCI6Xqn_5SaIa4YHsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6638d07252.mp4?token=RLjR8UjGiF17iS_6Hnrl4VZpUQ605Db50a5mAXeD2p4rL8XgGx--tepMOiAY_Fr_4dp8ih8lmo4FT9resIbVM8JEaMqsQsOupYINQwPmUT69N3q-ErSvTClxFCh-U-6fkj0JjLmOmeCGL-AouLEnz5AGcYXcYaLocpWMX3mZbDfKv7wH01HpKRqhjPnpojtNHn0RscnzrWcaxixgoguXOabBgNRHdWz9LHd1VhyOK8YC1k1bf8HPC0X7KC1UFpM8XUszQTV9YQnjN1wtdfHOPCG_gaU5IZBf1XETwaUJCqdQhCd8FsQwiphGNPAL3LfqTeHhaCI6Xqn_5SaIa4YHsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیشب در یکی از تجمعات میادین سه نفر از حاضرین نقش قاضی دادستان و حسن روحانی را بازی کردند و حسن روحانی محاکمه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/698356" target="_blank">📅 12:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698355">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
تصاویر منتشرشده از هدف قرار گرفتن یک کشتی کانتینری در تنگه هرمز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/698355" target="_blank">📅 12:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9jeRBi2WBWvyRP-TBVxbrLPcf0alt9Ur2nF1lGmOPCsCUNlNAurcMd32VyvNcM-CYGjLnK24D21MbeINkPuXzxYeUSz8TLejV7oevb7QP60KzGQXQ580waEv3G1ehK7a_UbNcYlMUK_6eFyWAiLuFxTnJRkCGsKzOEBg1wD8E8lY1Or1mBpmZBUpJw7CdkDOfYnqJt2N_rNu1uBjNbQ4sYF2yufrgRC5fzk0FE4-RD9UTVjVEeao8dLkScfHferNcjlz_DQPOnSHnrtqogiMdlQmFRjf7q4QXub-cUVGJydCjJDLHz56HKQgbp_c49RdyUhX_NRyHtHsJWcabSrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران؛ سی‌ودومین شهر جهان از نظر تاب‌آوری اقلیمی
🔸
در رتبه‌بندی ۷۲ شهر بزرگ جهان از نظر تاب‌آوری در برابر خطرات اقلیمی، تهران در جایگاه ۳۲ قرار گرفته و در نیمه بالای فهرست شهرهای با خطر نسبتاً کم است.
🔸
این رتبه‌بندی بر اساس میزان مواجهه شهرها با سیلاب، گرما، خشکسالی، آتش‌سوزی و توفان و همچنین توانایی آن‌ها برای سازگاری با این خطرات انجام شده است.
@amarfact</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/698354" target="_blank">📅 12:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwLztwd8ofiyBXRgENVk-FEORAqPms3bbDOdwYGZF1otxImQKlkWbjZKojEzLXO0O5qmXojJSfXg_i4sRHkz_Ke40Z92enBnt6EgU85eB3XNLgTyeMQber0iPhGUjsKnHLgQfgQ79tju5mzMDS6Znwy-9GFcEatbzqPQzVUFJl7Yg-9ciqqaNNZ6fgydagwKRNhmYFUsa8KxBGD9NiYri63OMYxvaSsL16QlACidlPITKl8eUIGSSioC11Fk4UtX_Kjqz-DuFU3dLAE1Q8r3ZVVGx-jRgtyd31NVwWFt833OVTyGT3_OGLDZNIrW8UZYHyGIsH-X7lSBRE_gol6W-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی حمله مسلحانه به خودروی پلیس در شهرستان مهرستان استان سیستان و بلوچستان، یکی از ماموران نیروی انتظامی به شهادت رسید  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/698353" target="_blank">📅 12:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYqlxLT2pBClnbuCwbDO3ZANX-e5tDNlqvMJV1q9N06J0gjHvGWwZbM8vwqHLvqhJuANSBCKMLQIx2kuOrR32E9lEFR04MXSM25b9wQOvH3mJHxtaBbl6h-t1szLe61pjb5dHxUrxR463kqv6iPNcOgZYN2Esq8XtYm62LlR2kX4cx-Mfl3QKBGwbqrgPB0qjbVPei8txDimdcFtRLBuIVglsgCOGu-79u_4iZOVTnAFEYyMH8cAoV-v57-gmr3vHkc2UhsqLryyL2fkBQQVaw_EBViIsib50eUK7tSU0yn3NZBLb2A6mN4d0W3-apUAG1JNvEoNGo4VWZpQC85fkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست بهترین ربات‌های تلگرام که خیلی کاربردی هستن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/698352" target="_blank">📅 12:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd2691490.mp4?token=WNteOtFCOfi3seFmNMVdzgpzdGFWjOfL8lKIeiXVO0_iDlP_GAq_oYr0dXptUuIy2XzBm92ViJ27zPgqYdZfEHNmlpj_DsOVnq5BcuNQFNQlOjb_icX8WwAGK9QeRXRi341PkxHTJYTmAQ0yklVqWvvttbY4yIaiawPhlQ-t69Q3qTOag51qb0GCAea15cRJtf4bafcqg2wjZXLvKO74mGows35XlB5Z3TVvu1Jjj5vYPN_8-oPAbyEA-Z1FL5NEQBhM9SbDwp2QDri2n0tkUg4Hq7U4VJg4YLjmg_hyl649wooSJ4Gq-umdv8xbx2aIfIC5dZO6LnZdHVhq6l7uuVk8DjG4wiVA-DeZu12-W7GYPP6bjn5m4iLfQMeD__2RB7OYAiEbC6jCU7K3pF8_OicC_xAXsKmpwqPIT0VRKMPNmNEpj2NfPzqkRXDf5xZTokTLrycMZpddVIXiRd78J0y8IlpRcfcNuaLfAtChAzoTga5KiJUX1EfIjNXkHCypO7R9UcROHuQhxtF-wWvC42lY_mBelxs-FMxopBH0Iw0Y6ps_SnOR2CIM1T48qvxpkxn2O83tdUvmErjl5ds5aUgxzocTXOPyuGK1tQ8VksC_nQvzGPjY1oLwjKW1v897_GxSmhq722ISQRvl-j1ss4M_Yu_GW0aAY8ZI1c6SKQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd2691490.mp4?token=WNteOtFCOfi3seFmNMVdzgpzdGFWjOfL8lKIeiXVO0_iDlP_GAq_oYr0dXptUuIy2XzBm92ViJ27zPgqYdZfEHNmlpj_DsOVnq5BcuNQFNQlOjb_icX8WwAGK9QeRXRi341PkxHTJYTmAQ0yklVqWvvttbY4yIaiawPhlQ-t69Q3qTOag51qb0GCAea15cRJtf4bafcqg2wjZXLvKO74mGows35XlB5Z3TVvu1Jjj5vYPN_8-oPAbyEA-Z1FL5NEQBhM9SbDwp2QDri2n0tkUg4Hq7U4VJg4YLjmg_hyl649wooSJ4Gq-umdv8xbx2aIfIC5dZO6LnZdHVhq6l7uuVk8DjG4wiVA-DeZu12-W7GYPP6bjn5m4iLfQMeD__2RB7OYAiEbC6jCU7K3pF8_OicC_xAXsKmpwqPIT0VRKMPNmNEpj2NfPzqkRXDf5xZTokTLrycMZpddVIXiRd78J0y8IlpRcfcNuaLfAtChAzoTga5KiJUX1EfIjNXkHCypO7R9UcROHuQhxtF-wWvC42lY_mBelxs-FMxopBH0Iw0Y6ps_SnOR2CIM1T48qvxpkxn2O83tdUvmErjl5ds5aUgxzocTXOPyuGK1tQ8VksC_nQvzGPjY1oLwjKW1v897_GxSmhq722ISQRvl-j1ss4M_Yu_GW0aAY8ZI1c6SKQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: گاهی برای دو برابر کردن درآمدت، به کار بیشتر نیاز نداری؛ فقط کافیه ماهی یک شب، از هیاهوی دنیا فاصله بگیری و روی مسیرت تمرکز کنی
🎯
🔹
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/698351" target="_blank">📅 12:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552b4880f4.mp4?token=uSp7g9d0X0m3NhMvyEWbfM-EY1EOUJ32e-V3YcYFkGw3z6MCNrYeIPrXT_rgof4zmSeq7lzEv5G4jpzzBTPFPTX47so7YUpu24PyHCRp1zKfGfdpuuJmafRiBn2ei14jytP1HBgAMkPz9X5jByaNFNFlm-nADFQME5VmbUneswCQJ1db-8-G6H7JtFuV5knMVynqDGf27osv9T193MaA1T6LQ6AqyLqUmDoRwl6AFr-zG7-ordP2Hu3-sgf_SY724hUp75VrDJeFvSfMeLo8gDdIvoVDEQ4IfHu2xB0suBtLjFFzIxsQqSpfCXN6F5geEvltbMteXgcMFKemraUR_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552b4880f4.mp4?token=uSp7g9d0X0m3NhMvyEWbfM-EY1EOUJ32e-V3YcYFkGw3z6MCNrYeIPrXT_rgof4zmSeq7lzEv5G4jpzzBTPFPTX47so7YUpu24PyHCRp1zKfGfdpuuJmafRiBn2ei14jytP1HBgAMkPz9X5jByaNFNFlm-nADFQME5VmbUneswCQJ1db-8-G6H7JtFuV5knMVynqDGf27osv9T193MaA1T6LQ6AqyLqUmDoRwl6AFr-zG7-ordP2Hu3-sgf_SY724hUp75VrDJeFvSfMeLo8gDdIvoVDEQ4IfHu2xB0suBtLjFFzIxsQqSpfCXN6F5geEvltbMteXgcMFKemraUR_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب‌های بطری رو دور نریز! اون‌ها رو به آثار هنری تبدیل کن
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/698350" target="_blank">📅 12:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: توافق روسیه با آمریکا، ربطی به دور زدن ایران ندارد
محمدرضا محسنی‌ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
این توافق تأثیر قابل‌ملاحظه‌ای بر وضعیت انرژی و بازار آمریکا ندارد و بیشتر اقدامی تبلیغاتی ارزیابی می‌شود.
🔹
میزان نفت مورد اشاره در این توافق در مقایسه با مصرف روزانه بازار آمریکا ناچیز است و این توافق  در راستای تلاش‌های تبلیغاتی ترامپ تا زمان انتخابات برای تغییر وضعیت خود است.
🔹
این توافق ربطی به دور زدن ایران توسط روسیه و این چنین مسائلی ندارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698349" target="_blank">📅 12:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
حمله مهاجمان مسلح به خودروی پلیس در شهرستان مهرستان با مقابله نیروهای انتظامی و فرار مهاجمان از صحنه درگیری پایان یافت  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/698348" target="_blank">📅 12:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698347">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رویترز: قیمت قراردادهای آتی نفت برنت بیش از یک دلار افزایش یافت و به ۱۰۶.۷ دلار برای هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/698347" target="_blank">📅 12:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30edb7701c.mp4?token=BrxRPomUXnUSl-ZqOzDRyOpnnlx3SIDB9FxZHKuoAA4jA0ZLSkQl-i1Q4OwF4oTvtx2xVi09ifr6UDZFOFtu2Lb7ATIsFWgoXpx3Jm1HANHIAPdYYZ7NtfMy16R8VJtFIhDVVBsTeKBzbBrsEZCQT_lJh5cA74XNL9uC0MfUnCfMe0pN1s6XzwGzWdiHOvo6rKXNL9PPxFjdQuV8nOxED2bqKgOPaDSbueS-LrSubf-1nXFJIc_edoSo4YDLUI1us4VrgIZwy6uU3DM1dLO8o-_6xnWs5E1mOTXS5jCf6poPBRww26_Smaxe2lC2fPrHWxZbhr7Ia5db1thz5leu9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30edb7701c.mp4?token=BrxRPomUXnUSl-ZqOzDRyOpnnlx3SIDB9FxZHKuoAA4jA0ZLSkQl-i1Q4OwF4oTvtx2xVi09ifr6UDZFOFtu2Lb7ATIsFWgoXpx3Jm1HANHIAPdYYZ7NtfMy16R8VJtFIhDVVBsTeKBzbBrsEZCQT_lJh5cA74XNL9uC0MfUnCfMe0pN1s6XzwGzWdiHOvo6rKXNL9PPxFjdQuV8nOxED2bqKgOPaDSbueS-LrSubf-1nXFJIc_edoSo4YDLUI1us4VrgIZwy6uU3DM1dLO8o-_6xnWs5E1mOTXS5jCf6poPBRww26_Smaxe2lC2fPrHWxZbhr7Ia5db1thz5leu9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدعلی ابطحی فعال سیاسی اصلاح طلب، تصاویری از سید محمد خاتمی منتشر کرده که مصدوم شده و با عصا راه می‌رود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/698346" target="_blank">📅 12:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94bd701792.mp4?token=Tn-ocgHaUD-PNVwqOVXHttX8aMB6jIiq0jJJp-ia-pUA3Qlzyd4iYyIfnr8rRiZDq3NxwHR_MJqC9e_yXGmPE250VZsCp2SaFVTdMvkjue4Nb84TiFLTJQ7ECKxy5YM35n5EFdKfht2DxqkK-SKORgHCZ9Ll3-UKXAvO8cH6mX6Ga9tlwHJNSmbxNcEeBK7yXlwNpJIHwsH5hOUeNNrwkiK2sNlU2tkq-WlNaJC6YeNfX8NIFg0jdftlLrka5ZKhNRrdd4NU6hgOQW7dJzu2YwL6p3878cL9v2DQ20SU9P5ATvsm9MIgWkNYYJbiNRXbJsg3UUOBsv-KpSIvISuICo1AoQssqiDucvysynCVVfJcwbk-r_YRU2sMjIZ-K2R2monM5GYxUnKEwJP4DrVDd0B3M0-0hxE18rEywFRlRWC0YvvprXY_eotM8CrgBotCZQwHzTbJCpvyqHWZPW283z7pak_811pgrUO-8tQvlfx0LXzWLpnRUDQjul0_qeBF9pwL04cIyXX1vPn9PvxUKm696m2AlZS0srlOXe2JyY2wLM7tA4YVD7m49t74ne-vTM5POu-s-KHKCK8O95mSipSUgsdVVKlgaSPEEEWsSd1Rj9jMP5UzbExzuXf6qYxjSbm6CQ0lcIgLHqB9MvtA6BWiIJKRbUPyDUIsT4BiQmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94bd701792.mp4?token=Tn-ocgHaUD-PNVwqOVXHttX8aMB6jIiq0jJJp-ia-pUA3Qlzyd4iYyIfnr8rRiZDq3NxwHR_MJqC9e_yXGmPE250VZsCp2SaFVTdMvkjue4Nb84TiFLTJQ7ECKxy5YM35n5EFdKfht2DxqkK-SKORgHCZ9Ll3-UKXAvO8cH6mX6Ga9tlwHJNSmbxNcEeBK7yXlwNpJIHwsH5hOUeNNrwkiK2sNlU2tkq-WlNaJC6YeNfX8NIFg0jdftlLrka5ZKhNRrdd4NU6hgOQW7dJzu2YwL6p3878cL9v2DQ20SU9P5ATvsm9MIgWkNYYJbiNRXbJsg3UUOBsv-KpSIvISuICo1AoQssqiDucvysynCVVfJcwbk-r_YRU2sMjIZ-K2R2monM5GYxUnKEwJP4DrVDd0B3M0-0hxE18rEywFRlRWC0YvvprXY_eotM8CrgBotCZQwHzTbJCpvyqHWZPW283z7pak_811pgrUO-8tQvlfx0LXzWLpnRUDQjul0_qeBF9pwL04cIyXX1vPn9PvxUKm696m2AlZS0srlOXe2JyY2wLM7tA4YVD7m49t74ne-vTM5POu-s-KHKCK8O95mSipSUgsdVVKlgaSPEEEWsSd1Rj9jMP5UzbExzuXf6qYxjSbm6CQ0lcIgLHqB9MvtA6BWiIJKRbUPyDUIsT4BiQmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش یک ایرانی ساکن خارج از کشور به کلیپ وایرال شده دختر ایرانی در باز و بسته کردن حرفه ای سلاح: این گارد جاویدان نشستن خارج و هیچی بلد نیستن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/698345" target="_blank">📅 12:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا حسین زاده؛ یادداشت ها، صحبت ها و سخنرانی ها</strong></div>
<div class="tg-text">#گزارش
آنچه اتفاق افتاد…
بانک اقتصادنوین با افزایش قابل توجه منابع و رشد مناسب ترازنامه مواجه است، اما در ارزیابی عملکرد یک بانک،
افزایش حجم منابع یا بزرگ‌تر شدن ترازنامه به‌ تنهایی معیار موفقیت نیست
. آنچه برای ما در بانک اقتصادنوین اهمیت دارد،
کیفیت رشد
است؛
رشدی که در کنار توسعه منابع و مصارف، با بهبود سودآوری، کنترل ریسک و تقویت توان بانک در تأمین مالی اقتصاد
همراه باشد.
🔹
در یک سال منتهی به شهریور ۱۴۰۵، مانده منابع این بانک از ۳۵۱ همت به ۶۸۹ همت رسیده و ۹۶ درصد رشد کرده است.
🔹
در همین دوره، مانده تسهیلات نیز از ۳۱۰ همت به ۶۱۸ همت افزایش یافته و رشد ۹۹ درصدی را ثبت کرده است. این در حالی است که در بانک های بورسی کشور، رشد سپرده‌ها و تسهیلات به ترتیب ۷۲ و ۸۲ درصد بوده است.
🔹
این ارقام نشان می‌دهد افزایش منابع اقتصادنوین با توسعه متناسب ظرفیت اعتباری و تأمین مالی همراه بوده است. بیشترین منابع بانک برای تأمین نقدینگی و سرمایه در گردش واحدهای تولیدی و نیز کارخانه های داروسازی کشور مصرف شده است.
🔹
خالص درآمد واسطه گری بانک در شش‌ماهه نخست سال ۱۴۰۵ به حدود ۲۲ همت رسیده که در مقایسه با حدود ۱۱ همت در دوره مشابه سال قبل، کمی بیش از ۱۰۰ درصد رشد نشان می‌دهد.
🔹
در کنار توسعه فعالیت‌ها، حفظ سلامت مالی و کنترل ریسک از اولویت‌های این بانک بوده است. بر اساس آخرین اطلاعات، نسبت مطالبات غیرجاری (NPL) به کمتر از ۵ درصد رسیده است.
🔹
حاشیه سود بانک ۸.۴۸ درصد است.
🔹
ارزش بازار بانک اقتصادنوین به حدود ۱۲۳ همت رسیده و بازدهی سهام بانک نیز در یک سال گذشته بیش از ۲۱۰ درصد بوده است.
🔹
از دیگر دستاوردهای ارزشمند بانک می توان به عدم اضافه برداشت بانک (حتی یک روز) و کسب رتبه الف در گزارشگری بانک مرکزی اشاره کرد.
🔹
همچنین بانک اقتصادنوین بر اساس ارزیابی سازمان بورس و اوراق بهادار از منظر شفافیت در میان بانک های برتر بورسی قرار گرفته است. نماد بانک نیز در این مدت به تابلوی فرعی بازار اول بورس ارتقا یافت.
🔹
در ارزیابی شاخص سلامت بانکی CAMELZ نیز بانک اقتصادنوین یکی از سه بانک برتر کشور شناخته و معرفی شد.
🔹
تحول بانک اقتصادنوین را نمی‌توان صرفاً در شاخص‌های مالی مشاهده کرد. نوآوری در همه زمینه‌های بانک، از شیوه‌های مدرن مدیریتی در لایه های مختلف گرفته تا توسعه کسب‌وکارهای نوین و تحول در حوزه فناوری اطلاعات، به‌طور محسوسی در جریان است.
هدف ما در بانک اقتصاد نوین، صرفاً بزرگ تر شدن نیست، بلکه معتقدیم «بانک اقتصادنوین» باید هم زمان بانکی بزرگ تر، سالم تر، شفاف تر، کارآمدتر و سودآورتر باشد و رشد آن به خلق ارزش پایدار برای مشتریان، سهامداران و اقتصاد کشور منجر شود.
@Mohammadrezahoseinzadehh</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/698344" target="_blank">📅 11:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698342">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1EiMBKKFSqN_ky1a_i79VG9QoB4HHeqvE2Jaq3h6jLaos9D9VLA7wlpE681YjfpsxqoXpsXqfr2lGhYJRMhamWPx2aMrOt8SsDWtUF9yGykqHtlN0zHlZk17ujQnpScjs6i0DmdY3aviFmsUXP-dL_4Z6IEgSfLZuJBeLFd9WQjpkMCDjEGfN2pPXUn9XKv9K3bl_YAagDqstxY37uXBFld3bmUtuKFypNH1sjzpDR61GSZJNQoOa6-FLafFEv-79eV4UzhKXTrii20sY39LuzCyR09woHj5Y4mduMRmanBuTIPmxm14Q6OTmX4-qa8WkeNvz3MShpl2YsUzgNsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SmGwARf4miywxa6jRmXMThN74DRI4MgjvSUBivvtRTKp3m2tqrUhCP3Azipuxz54nS8zxYT9K4SvbCqmgtVUO6ePuOHXS0kOVpodtkO2pXAt8dmUBN-Dp1D0s8ZBdjBxflx_UfAQ3zTjpgAllart1Qse54YeEIVNFU9GkKzsHozxE7wxnYfDdGBB8vsG5xUGLvhCMD5BB6qhFfwSIjhXv_xJQxXWmE_QF18jQf2-5YMDcPmKdGHD1LIPkdbQiRbx6vUs0V2sAm_5aMOnxBW9GICvcfUdSDy5_Q9X9jWEU2wAl3nlcfydxxUUYiaEo2PIfF9CgxAXbbV080n4X7MUjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر منتشرشده از هدف قرار گرفتن یک کشتی کانتینری در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/698342" target="_blank">📅 11:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698341">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پول مردم بعد از جنگ کجا رفت؟
🔹
از ابتدای جنگ، هر سه بازار سهام، طلا و درآمد ثابت شاهد ورود پول حقیقی بوده‌اند.
🔹
بورس با جذب بیش از ۱۰۰ هزار میلیارد تومان در صدر ایستادهو طلا هم  با جذب حدود ۷۴ هزار میلیارد تومان از درآمد ثابت پیشی گرفته است.
🔹
صندوق‌های درآمد ثابت نیز با جذب نزدیک به ۶۰ هزار میلیارد تومان، همچنان مقصد سرمایه‌های محتاطی هستند که در فضای رکودی، نقدینگی را در حالت آماده‌باش نگه می‌دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/698341" target="_blank">📅 11:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698340">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e79a2652.mp4?token=mSdBFuAaDMLRFqFgDHnji0g-kBlh13pmbqofDsj4vWM59Eko7IrakhVBGT_OROioarEmZ3RKvrdDazf9CMggmUQ6ccx8xEcLwoC8hhUrBR05N9-Ba83iZ0iOUAeoPNoKoiXNWSn39iIfa4B7h941IQstUwOqX-6Xg1M9HjUDXpr9oHhIR8SAXt3L0_GyPBg9ki5PUNgU9EHMhEYThA0MEuVjf5_2TKi6vCT3ZdidkDBcgdytv2mLTCR44QncmP2GWoiqKlAPjPPkTmqmtt5-H0OdqISGCnFsdlKp8shLICNBdeZkvSkz9246tC2dox8zuy9cWn54pbFQyDsNWuuARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e79a2652.mp4?token=mSdBFuAaDMLRFqFgDHnji0g-kBlh13pmbqofDsj4vWM59Eko7IrakhVBGT_OROioarEmZ3RKvrdDazf9CMggmUQ6ccx8xEcLwoC8hhUrBR05N9-Ba83iZ0iOUAeoPNoKoiXNWSn39iIfa4B7h941IQstUwOqX-6Xg1M9HjUDXpr9oHhIR8SAXt3L0_GyPBg9ki5PUNgU9EHMhEYThA0MEuVjf5_2TKi6vCT3ZdidkDBcgdytv2mLTCR44QncmP2GWoiqKlAPjPPkTmqmtt5-H0OdqISGCnFsdlKp8shLICNBdeZkvSkz9246tC2dox8zuy9cWn54pbFQyDsNWuuARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر قالی قصه‌ای دارد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/698340" target="_blank">📅 11:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698339">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1443a897c3.mp4?token=sJtum1DlVjHNpo6Z08BJppBIN-i2_38j4DvcSCI6fcqfOPJPXNlZMBNsbkSEw_zgXm6FYCqd7NruFX6nhcv9yAgIpQt7ouInTfoBkKujWNhxMmuW9iSyp0uxMD1up1DjmWaR-C1QfX8IdFCuRNPhVMczXhSwWKCOYALqs6N9ZUcRUbvkjFWGhwy3DnxjMkUJ_q6mup-2bBl0H6_zWTeH0Rz-Cv75gL2edaDWVCUgBFBGYTqdLBOKKnm0eormzN73oD-96DNFTlHJ8Z3UdQQ7ayXNvaZi9_Xki-3GURbpLitmiCc5-Cx5ClFhIQmYICxYWqralTS84bmCh_szWmRgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1443a897c3.mp4?token=sJtum1DlVjHNpo6Z08BJppBIN-i2_38j4DvcSCI6fcqfOPJPXNlZMBNsbkSEw_zgXm6FYCqd7NruFX6nhcv9yAgIpQt7ouInTfoBkKujWNhxMmuW9iSyp0uxMD1up1DjmWaR-C1QfX8IdFCuRNPhVMczXhSwWKCOYALqs6N9ZUcRUbvkjFWGhwy3DnxjMkUJ_q6mup-2bBl0H6_zWTeH0Rz-Cv75gL2edaDWVCUgBFBGYTqdLBOKKnm0eormzN73oD-96DNFTlHJ8Z3UdQQ7ayXNvaZi9_Xki-3GURbpLitmiCc5-Cx5ClFhIQmYICxYWqralTS84bmCh_szWmRgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض دانش‌آموزان یک مدرسه به قانون ممنوعیت ورود دختران محجبه به مراکز تحصیلی آذربایجان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/698339" target="_blank">📅 11:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
بریتانیا، اسرائیل را کنار گذاشت / بیت‌المقدس شرقی، لقمه‌ای که در گلوی صهیونیست‌ها گیر خواهد کرد
🔹
اسرائیل روز پنج‌شنبه اعلام کرد کنسولگری بریتانیا در بیت‌المقدس شرقی «دیگر به عنوان کنسولگری فعالیت نمی‌کند» و سرکنسول به همراه ۱۹ دیپلمات، این کشور را ترک خواهند کرد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3251076</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/698338" target="_blank">📅 11:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حمله مهاجمان مسلح به خودروی پلیس در شهرستان مهرستان با مقابله نیروهای انتظامی و فرار مهاجمان از صحنه درگیری پایان یافت
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/698337" target="_blank">📅 11:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698336">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
گاف پنگوئنی ترامپ!
🔹
ترامپ تصویری از خود با پنگوئن‌ها در جزیره گرینلند منتشر کرد،‌ این در حالی است که گرینلند اصلا پنگوئن ندارد. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/698336" target="_blank">📅 11:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXN3H8et-nXHjykXYn2y9P-F2DjZjLJP2tMncG-RZKxVvNrCsXdOXWsiXM-glwkQoZ2zAMGGN3bpS38Jn_-At69knCM21EjYhd6qPmvaVkYAxi4x5dfA1qcJZfORmoJz0imxD2lFW8Z2LkhKUUu3kCOoz9YMU53d_nc9h_4mSGQFiXhbnybEKVZXTbomuQ1d-CdlARxieTQ-IYuCdncxgJkh2WvSNMg6hrjO_BIhZRqGezZx0ku7-YxhbkmXiWKJTwmSjCpMxNXHUUBTWyjzs6gWa6vIAAakm6FZGp8ScMjyE2OIcV24IhhgBOmeTSfQfRAPpTR-8HnomJlN_x6Oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیک تولد عجیب محمد خاتمی که در فضای مجازی پربازدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698335" target="_blank">📅 11:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وقتی ترامپ و پوتین برای زلنسکی تصمیم می‌گیرند!
🔹
ویدیوهای کنایه‌آمیز هوش مصنوعی از بازی قدرت‌ها با سرنوشت اوکراین در فضای مجازی وایرال شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/698334" target="_blank">📅 11:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFQmtXiTb5sRcSLB-1aTUymDl2UuZK1fxKoVGRoSbezfHX0l97RY3-cgV0T3KIh4Oo7_VWWQeWhE52xnsmdsRnDjwPm_-B_XFXhxI_8r2W9EOsvygO_o7xo0e8Mx-9Zv2eh5P5fKmHNoSE_FeRaGQTP3ZXFq9yRKfV-3XOSNXpFLvHajavdrxWXcosckOCtUOARBvy74it6Uk2de8EKCq5mBfc-veizGR3XALSm7lJz_ftPrXsi3OYUP29_Sh7qNBg94p57XcOJSNiaYE6Xd1rEBU_lWAUbfEZFhKBkiXU_TQWVlPQ1E_7sfvqGSDgB6vlZ7FZv2TxUsJiJuYsVGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام فرودگاه‌های عربستان تعطیل شده‌اند و چند روز متوالی بسته بوده‌اند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/698333" target="_blank">📅 11:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMj-kgLR1BqsIpbIlAt5Ir7po0p7jpTlBKLd4pIjL3M3OKsqK0bbQdzNM5Fp-6CErZS2gu_9n-RXEZi55FYIPus7C1Odify14MlSUNUQloeMY9R1gTvqrTwE0LYw_TQhN0xy42zWl-_wavxlxofi4uz5LTg7zrvWyIMz5WW9EYKglGYY9z8baziKaYsUE1sWCzBeqq7nNygv8PuJWAR5lRb3lKONRe7KDlVIh4k6uCzIbexXQAlOIGAsdOdeSQDwmkwD945cMQxWcrGvfeYBWCs3kvqEb7S3xyeTRKuWKqFNsEy88hfdEgG3tcWzcoK6PAjut6-RHld0Y6Labi8bbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ تب عفونی مهم که باید بشناسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/698332" target="_blank">📅 11:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قانون انتقال سهمیه از کارت سوخت به کارت بانکی در پنج استان اجرا می‌شود
رضا نواز، سخنگوی جایگاه‌داران سوخت در
#گفتگو
با خبرفوری:
🔹
از زمان اجرای نرخ ۱۰ هزار تومانی بنزین مصرف بنزین در برخی روزها حتی بیش از ۷ درصد کاهش داشته است.
🔹
مشکلات مردم و جایگاه‌داران از جمله اختلال در پرداخت با برخی کارت‌های بانکی و مسائل مربوط به سوخت‌گیری موتورسیکلت‌ها در طرح شناسه‌دار کردن کارت‌های جایگاه‌ها درحال پیگیری است.
🔹
طرح انتقال سهمیه سوخت به کارت بانکی پس از حدود ۶ تا ۷ ماه تأخیر در تصویب آیین‌نامه، ابتدا در دو جایگاه تهران به‌صورت آزمایشی اجرا شد و اکنون اجرای آزمایشی گسترده‌تر آن در پنج استان البرز، سمنان، قم، قزوین و همدان دنبال می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/698331" target="_blank">📅 11:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به صیادان سیریک ۳ مصدوم برجا گذاشت  استانداری هرمزگان:
🔹
یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد؛ براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شدند؛ مصدومان درحال انتقال به ساحل هستند.  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/698330" target="_blank">📅 11:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698329">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnKN9SrKD7AM16iajmKFnuFBcBakwvKKEX_GPYhRQREV1bcvV81DyN41uVOJ_2b0BTGL8XyBJ1AIslJPYyE7DQxkZ3HZFLbIawoq25EBm4Dx7QJC35IRsqmfBkbTVs5zBkGSHS_ojPwOEXAS5kLPrTH79RDqlJs5maquneLQEKyoskLDK7Mxj4HdNI9wbo9HHZrk0RUIlE7QLRSCCurZ4jmq195YOaOyhgLyXYw_vblVAcr4iKZV6S5ImCiiAD75G_jXyawwX1P1gMqB1WmAKwSOm_j2eMPL1pHssgZ2YLz4gXVn0pcZ1mu_ITZTNZgpN0bx5XSquroYALn27bqBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دمنوش میخک؛ نوشیدنی خوش‌عطر پاییزی برای روزهای سرد سال!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/698329" target="_blank">📅 11:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698328">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ترامپ ازدواج پسرش با سفیر آمریکا در یونان را تکذیب کرد
🔹
کیمبرلی گیلفویل عضو خانواده من نبود. گمان می‌کنم مدت‌ها پیش با پسرم رابطه داشت، اما [عضو خانواده] نبود. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/698328" target="_blank">📅 10:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698327">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSeQl6zGUTBw0_a8Mo2ljCVgFNhK19E7-OuN20jn_VaVBOmNYW-9_Fu_v8QtXqx8HWxztlyAjwv__LbHb3wyQpFe5uR7-dMfHopvlimOrz5h6ZCsqUFKLeXyazmlUM8W3cF9hDUCCAfk_8TwCYlu33TbbIDV1HQ6rnNZfrhb2N2SJtiv37A_QbxqhaA9EMvyy89JogZ6rHbxKPvD2CwqKIdqwctUNEMvPpN9YkcIX-h_KsTqD38luGd7X0y4bFnN0txAWeP8SYfQ3P3O3E9IolnPYVN2sy7dYBXBf_ojeFbmy3Zl2iLqhRxGBGpX2v1onwgNuHrx17jtGML6eWfbIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه دو فاکتور خرید با فاصله ۲۴ سال؛ شهروند آمریکایی: قیمت اجناس ۳ برابر شده، داریم بدبخت می‌شیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/698327" target="_blank">📅 10:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698326">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4429aa44cc.mp4?token=nXPdpwSpsnfEIPr99FJPq9r8Q1tjKt-pufQ2a1UWXLCTPi7dNsCKEQwdA-40sSrNfIZS0wVGZkPz1U5rTuYQZUjNvqu0w4apyqZrCqVLHkCuaAwbkJIAUHVFtRfkEEP-rt1KHLY8m_9vZsEO5eYvqAz-ayl2ZKOFODAA0HibfJ2W8uHdHMQswpFU9YN92EJ4FMPBHSQTcwqw4jc44j-ZMqFHAP0UOIFmE7ZJfFJSBH9GSBrNE1HAJj-Q1DobqCk7hKIe6cBNNltDdm9AaTOgH2Foba0QbGAtzAdgS1kbfFFpbSmyPhLA0F3XJK2tSYwfkAY2VVujrU9cWPAdv6mJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4429aa44cc.mp4?token=nXPdpwSpsnfEIPr99FJPq9r8Q1tjKt-pufQ2a1UWXLCTPi7dNsCKEQwdA-40sSrNfIZS0wVGZkPz1U5rTuYQZUjNvqu0w4apyqZrCqVLHkCuaAwbkJIAUHVFtRfkEEP-rt1KHLY8m_9vZsEO5eYvqAz-ayl2ZKOFODAA0HibfJ2W8uHdHMQswpFU9YN92EJ4FMPBHSQTcwqw4jc44j-ZMqFHAP0UOIFmE7ZJfFJSBH9GSBrNE1HAJj-Q1DobqCk7hKIe6cBNNltDdm9AaTOgH2Foba0QbGAtzAdgS1kbfFFpbSmyPhLA0F3XJK2tSYwfkAY2VVujrU9cWPAdv6mJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به صیادان سیریک ۳ مصدوم برجا گذاشت
استانداری هرمزگان:
🔹
یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد؛ براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شدند؛ مصدومان درحال انتقال به ساحل هستند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/698326" target="_blank">📅 10:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ملاک‌های جدید تعیین وسع اقتصادی برای دریافت کالابرگ چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/698325" target="_blank">📅 10:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سازمان تأمین اجتماعی و صندوق بازنشستگی کشوری خبر منتشرشده در فضای مجازی مبنی بر «آغاز پرداخت وام فوری ۱۲۰ میلیون تومانی به بازنشستگان و مستمری‌بگیران» را تکذیب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/698324" target="_blank">📅 10:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrrGyh1doJ2Gv2PJJdvvsRBJ3H9BAne3D_KiW63Y7n8s0YjPEqTFAOqJHSK-yEpxTlLQodYnAJ6DzgWSKCe-nIYdcB9AYPbco0hQh3OeHML3vPaBuX7zzgZAEuFs1Pk-GLTEgqiYnNpvkrB4QVMi4xJwnYZ7WvRRuNn1tQfXpIgxoqwUhGFu2MmU22l7k_gC8oqfi84mhJcHhN9w0J-pIO2YOlz7pjYjYE2iYCf6R24FIvBPi5IuqimLJ-LP55ZnQVqsEqhXRQ1-JHVHGQKq7emAJ-i7xGqvnkKK6zwbcOc1mI_qeTN5ROHuNgKO6_bTL8qxDZBQiWclE_F09k_H1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناریوهای مواجهه ایران و آمریکا در آستانه انتخابات کنگره/ چرا کوه‌های اصفهان هدف جذاب‌تری از عملیات زمینی است؟
جنگ در منطقه به کجا می‌رسد؟ تحلیلی درباره محاسبات واشنگتن، تل‌آویو و پایتخت‌های عربی را در ادامه بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3252254</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/698323" target="_blank">📅 10:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81452d05f8.mp4?token=f5RhYo0BSkpuFvbmotsZU29ZvkkDEnp4G4KFwu8GnIWU46mStgSk2flsJJ-cSpKke26Q8U7YIv0j62-wwUKdU7lprasoFXx0VYISI43WzLa432cW-CnwHOERUIetCMaUO-1lpS_FMiwSSlUPBxgZqLsjMSNi0xTxpefaKJ3ls8AehtL3ITQlDlKowMS-9GyWWw3Fz_MQbzd1vLnR-MYrzxZQwnriZirku08JFhlc75USj5C411iuvV1CzZqsLne2cZxNYUs5Z3tUIXiqMKWzqYh332I-qSc08a036bLvdT5boLG40eRCcTsZyiM_XSY4CZ_rQM0VMvrn0w85Bmd_jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81452d05f8.mp4?token=f5RhYo0BSkpuFvbmotsZU29ZvkkDEnp4G4KFwu8GnIWU46mStgSk2flsJJ-cSpKke26Q8U7YIv0j62-wwUKdU7lprasoFXx0VYISI43WzLa432cW-CnwHOERUIetCMaUO-1lpS_FMiwSSlUPBxgZqLsjMSNi0xTxpefaKJ3ls8AehtL3ITQlDlKowMS-9GyWWw3Fz_MQbzd1vLnR-MYrzxZQwnriZirku08JFhlc75USj5C411iuvV1CzZqsLne2cZxNYUs5Z3tUIXiqMKWzqYh332I-qSc08a036bLvdT5boLG40eRCcTsZyiM_XSY4CZ_rQM0VMvrn0w85Bmd_jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سحرگاه پلور و منظره زیبای دماوند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/698322" target="_blank">📅 10:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای نتانیاهو کودک‌کش: اگر مخالفان [من] در انتخابات پیروز شوند، هیچ اقدامی علیه ایران انجام نخواهند داد
🔹
آن‌ها از لبنان و غزه هم عقب‌نشینی خواهند کرد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/698321" target="_blank">📅 10:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سخنگوی وزارت صمت: میانگین مصرف سوخت خودروها در هر ۱۰۰ کیلومتر، ۷.۲ لیتر است/ نسبت به آمار جهانی بالاست اما نسبت به آمار گذشته خودمان کاهش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/698320" target="_blank">📅 10:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCFb1VNsIPnCyBVzGpI-UU7GKH8A1yde1xky_ag_5VTFRIwLAz3v3EHI3i__0_vja_CiYqXhuMPNIEIxyZGuA3hBW34OoiMjD1eB7h4Mp3P7e_k5ZvAiHs-J2GHf1IMn4uJ3DOf72-qbJwC0YIE8SgR7xCu7VZ2X21YJjsi9_wDPLKmCyhg-OzvP-Gomdv-wpUVzD_FhJ41viSpH-OXkMDhx9UEDJYIUHhf5jKwA5GNIz4zfnnpXhFwsti9x0ZJSPPUnS2fT3y9NehItvgSundh07ExgipuhoNWXuu4c8oQbVIGtsfXsH0qe-LT3SG_RJTADQfZDs1OA7MCnv2PMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس دادگستری کرمان: تروریست اعدام‌ شده در کرمان قصد تسخیر فرودگاه برای ورود رضا پهلوی را داشت
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/698319" target="_blank">📅 10:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c88c1e6.mp4?token=FKpJY38WGBUN_pbyrRHez_vSQ2-Vv0ArWPtibTUQZi9DbentrQWh9NlGKImEtZBZYzbDBrPWrBzanGy_eaLHCSP-HSo9UnPu9f0DhI266F__L8689efpcGC-iCXUOkb-3LqXNPExlThI8hJRauOLHKxzvAYCLtnMb2lQbV7gLTUja8VfwEpFc41zZ8Rp0lK_W7JERNGbfsyhXC2BVGIETkaUcH8H_AqTFnHL-bTpW3APekxiLZ71X6Vx0UnX_1yb5v5KhtFVuhbxpEmApWJHgHFwxlqJmq2uwCcJh9WnRZIDukF2JIhUBYemMFx4H-vtEhTuPFVSWMEJ8gM4xszclw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c88c1e6.mp4?token=FKpJY38WGBUN_pbyrRHez_vSQ2-Vv0ArWPtibTUQZi9DbentrQWh9NlGKImEtZBZYzbDBrPWrBzanGy_eaLHCSP-HSo9UnPu9f0DhI266F__L8689efpcGC-iCXUOkb-3LqXNPExlThI8hJRauOLHKxzvAYCLtnMb2lQbV7gLTUja8VfwEpFc41zZ8Rp0lK_W7JERNGbfsyhXC2BVGIETkaUcH8H_AqTFnHL-bTpW3APekxiLZ71X6Vx0UnX_1yb5v5KhtFVuhbxpEmApWJHgHFwxlqJmq2uwCcJh9WnRZIDukF2JIhUBYemMFx4H-vtEhTuPFVSWMEJ8gM4xszclw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیز کیک تام و جری/ بیاین پنیرهای خوشمزه‌ی تام و جری رو با هم درست کنیم!
🧀
🐭
مواد لازم:
🔹
۱ پاکت خامه
🔹
۳۰۰ گرم پنیر خامه‌ای
🔹
نصف قوطی شیر عسلی
🔹
زعفران یا رنگ خوراکی زرد‌ به مقدار لازم
🔹
۲ قاشق غذاخوری پودر ژلاتین ﻿#آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/698318" target="_blank">📅 10:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698315">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5dut7LA08kLgMTPeG9SdKUb_IgTAVaucMtBvzH8QEOc9AqiHNvO5tTAeiEs0LEdZK0sObhlF75b9vU6NY55GMIm0-rnGyMxgyi5QHrLftHmjB5LeJq7Q-QZWFz-Tm1Xn8S0yNGWFsyJEVbH2zdBknhQ0jelMtAp-d3zpgTMxp_eJBd0u13bAn67fHZbW22dqtjSZQehJDB6kAZJ66UILQtWJ8WGWWDXBYn4PC0Z1Tq32dgral9ZZBXu68vdDBDlh8S7l5XF3hnRjrR3XBLe8NmaZNoc_S6G0yq8SkBAurEYBz66EAXZUSfKDMpbNQ8TSSZ8p3rC_Wbknd1eGTfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDdBFtlO2AdCEIzTY41pfM008kI6esLxkv9hsX_xvPRxTDppnDe4vQosIUnc_gtxqYKoYkdG7I5QH5WZNAiVIdgt-okyqSCFBC5prkQVnj1hdJINe80EcAzbXQ2fZ3HZpQPSEZk2npE3UjVr_l8vQjF3v-WaaZKkCFEAIqQbdtqIY8sTmfw_FEIGkiHHaAmrWG0CHjGtFJicwEuPAqc_aEfFGMNboclHhE18KJKdXdH8qeB6SE1cJEJkKgqE3LoFhEZ9YMh1hQ77UlmvPNJKKB697HHlSmXx6Rq_aUbmASlFkJo9oyWBfBgCFnaMXHbUkOH6DUyt_NTi4c7EYs24eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6IYmMNhIFRbEVvOgcet2v6KGwYDP3oP9iKFGms-bf6BcNlidbW5hCZi25XvUO7FbRZ0PEklxBzP9qa_1LbncJhKTe-Fe4UioEjua2ILPG4Bp2awU76M3hrH17j43JlpqHb7fiuB8BL_nRrz8UD8Pb6CYKdTNhvnpOQP4mIpEgiAhlQuOt6X8iVf1Q5XQ8JN2fBKiF9eGkhQMHkhTLhp8-3WaLEIJFJWpDJp91c3hflMm9Y9zDfFClYjqYnzo3zhHvOJiZrckmKB6FkO5KmGLSJ1J4Wl3mqLP23bo1KrjsSo4GxusX7zkD2WSvInpJAc9HP5EzCEUlQtxDbkWOEVuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اعدام تروریست مسلح در کرمان
🔹
حکم اعدام علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی‌ـ‌صهیونیستی در جنگ تحمیلی اخیر که در چند عملیات تروریستی مسلحانه موجب مجروحیت شماری از شهروندان کرمانی شده بود، اجرا شد.  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/698315" target="_blank">📅 10:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698314">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی یمن به تأسیسات نفتی آرامکو
🔹
گزارش‌ها از حملات موشکی و پهپادهای انتحاری یمن به پالایشگاه نفت آرامکو در شهر جده عربستان سعودی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/698314" target="_blank">📅 09:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مبالغ جدید وام‌های دانشجویی اعلام شد
🔹
وام تحصیلی: کارشناسی ۷، ارشد و دکتری حرفه‌ای ۱۰ و دکتری تخصصی ۱۵ میلیون تومان؛ برای متأهلان این مبالغ به‌ترتیب ۱۴، ۲۰ و ۳۰ میلیون تومان است.
🔹
وام شهریه: از ۵ تا ۱۰ میلیون تومان، بسته به مقطع تحصیلی.
🔹
وام ضروری: ازدواج و تولد فرزند ۲۰ میلیون و حوادث، بیماری خاص، لوازم کمک‌آموزشی و بلایای طبیعی ۱۵ میلیون تومان.
🔹
وام عتبات عالیات: ۵ میلیون تومان؛ با تشخیص رئیس صندوق تا ۲۰ میلیون تومان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/698313" target="_blank">📅 09:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f845fba2a2.mp4?token=sKRL5QwLKCoKlHTQFBs7Xlfj8Y7uajVsmQR53hLgMASih0g_gWj6atO68HD2z54bGmmb0OkWjq57AQtRz1zQxY30BNfTpp6gWM261fjBQekPQrH6r5ZDkqxLrhMKiNKFgneWDlJlC1o_TSGRmFSbrTxWtw11c14i2t0lZTd15J5C2xdGziSCaRldVUOm3rF8djurpRX1dfdFImycsGX8i-fjKEAWY5EGqrBzXmbvnlcEWb1D0vXsyCUrQ733yS55V5XyPtkgLueLb5MrgJXTmPF6_HyYYw0k63vhd1xBaI9DX8krNQGKRUoVjh8_Jb5ecC1kD5k-lIqbo1dFUBSgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f845fba2a2.mp4?token=sKRL5QwLKCoKlHTQFBs7Xlfj8Y7uajVsmQR53hLgMASih0g_gWj6atO68HD2z54bGmmb0OkWjq57AQtRz1zQxY30BNfTpp6gWM261fjBQekPQrH6r5ZDkqxLrhMKiNKFgneWDlJlC1o_TSGRmFSbrTxWtw11c14i2t0lZTd15J5C2xdGziSCaRldVUOm3rF8djurpRX1dfdFImycsGX8i-fjKEAWY5EGqrBzXmbvnlcEWb1D0vXsyCUrQ733yS55V5XyPtkgLueLb5MrgJXTmPF6_HyYYw0k63vhd1xBaI9DX8krNQGKRUoVjh8_Jb5ecC1kD5k-lIqbo1dFUBSgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عجیب ترامپ به ماجرای کشته شدن یک فرد در باغ‌وحش یورک‌شر انگلیس توسط ببر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/698312" target="_blank">📅 09:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
حنظله کابوس شبانۀ مقامات صهیونیستی
🔹
گروه هکری حنظله در پیامی با اشاره به باقی‌ماندن ۱۳ روز تا انتخابات رژیم صهیونیستی، از آغاز مرحلۀ جدید فعالیت‌های خود با محوریت انتشار اطلاعات و افشاگری دربارۀ مقامات و شبکه‌های صهیونیستی خبر داد.
🔹
حنظله در این پیام، انتخابات اسرائیل را «روز بزرگ دروغ دموکراسی» خواند و اعلام کرد که از این پس، فعالیت‌های این گروه با تمرکز بر انتخابات و انتشار اطلاعات مربوط به مقامات و ساختارهای رژیم صهیونیستی ادامه خواهد یافت.
🔹
این گروه همچنین اعلام کرد که به‌دلیل محدودیت‌های موجود، اطلاعات و مطالب موردنظر خود را از طریق دو وب‌سایت Distributed Denial of Secrets و Drop Site News منتشر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/698311" target="_blank">📅 09:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی یمن به تأسیسات نفتی آرامکو
🔹
گزارش‌ها از حملات موشکی و پهپادهای انتحاری یمن به پالایشگاه نفت آرامکو در شهر جده عربستان سعودی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/698309" target="_blank">📅 09:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رویترز به نقل از مقامات ارشد ایرانی: ایران در حال به‌کارگیری تاکتیک‌های جدید برای حمله به کشتی‌های عبوری متخلف از تنگه هرمز است تا قیمت نفت پیش از انتخابات میان دوره‌ای آمریکا، کاهش پیدا نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698308" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: حوثی‌ها با استفاده از قطعات وارداتی از چین، در حال ساخت موشک‌های بالستیک میان‌برد پیشرفته است
🔹
این گروه قطعات تخصصی جهت ساخت نسخه‌ای از موشک ایرانی «خیبرشکن» را وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/698307" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVRl8OKHoG9ie2-YGCwXoECkhcUH7Bu2DUdkgOcYj9SbSsaf30l1AtelaUUOCOX0eo-wAWWWQny-S31zwat7yizBUJOp15pMro8knSrV3cXZAtYfZrRY7pJWDyW5uKIeKv_x1PKKmWR-DFi2rGSQVNzT0cxLMWVWOFHj4EHirsVO6P-9NnCJr_FaSG4eR6Ki8YHtlyNLCaDgalmCUsNIEsZ7uRMQOyrTywS_a-eDrzHX6EbjlUbw52p4woiUDagSLH34CxsHaTMChovgaBk5AdDFG_M1jXloV7DrR5aFWmo6IWmHnW41YCz-WYrSJ8pQNhnoodjcXlmo0ulTlutcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از کاخ فتح‌آباد، کرمان
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/698306" target="_blank">📅 09:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a696a0da2.mp4?token=Oh5vS2xFKUB-VgROPypDV6nYybYZ5vlx-lcl33kebevgHKKR6Z2ZFxyMKKd3fYb6SCqjuiEf5ErISS3z6noIUlYNnE3_TPOWGxL1EbMA4kKE5KFdpURVFaeBIjdhea_E3_9k3TbQa7kYtufrf3l6I5Qq0LikpmnGtW7kvwaYFA8i-teanGvZY5Ot-1JxYxa9vp_AyBZDjT3IL6JDzP5hKQEYDl1XGMc_lpqlhnKxm5zeDyzrfaWAXRMUd8KEutgZCEmL0UC6x9LZ1tQn0bP3HVQZMZt7yIBDQ53yR7aZmFmQmqK3DVO55n2twCIl9ZNtEojnbR-hs5emPdI0SZtJQERbUXPBNN5vsUaI4co1hDiJ00Xopf6osZDgtcFpZVdQGWlAjEhGA2TSGU_DM31LrWqYiUMWiRIPfdyd6hHeypHXmwxTuc2dVzaREhAowJy9YGeAAZFfyIjrmYfcWrifudWRyxGcNk0x-iRMgXQsYxJx0vDJEvsuslpfkJhkTYrU8tCVPEqul9yj1muYtyvbLjQc9qPgRSlkqqHCzMooQkhF99JaUstB2kGGv0VQrloBRfVqLkK4crgPFh9GDef-O3KPby5zB5cFvw0zQukSnaKCM34bjtOH1Zh9otyzCXawkkUOcrUA6vb3R1CFrWmvSZkGli_Ga9n4Q0vEkcm13rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a696a0da2.mp4?token=Oh5vS2xFKUB-VgROPypDV6nYybYZ5vlx-lcl33kebevgHKKR6Z2ZFxyMKKd3fYb6SCqjuiEf5ErISS3z6noIUlYNnE3_TPOWGxL1EbMA4kKE5KFdpURVFaeBIjdhea_E3_9k3TbQa7kYtufrf3l6I5Qq0LikpmnGtW7kvwaYFA8i-teanGvZY5Ot-1JxYxa9vp_AyBZDjT3IL6JDzP5hKQEYDl1XGMc_lpqlhnKxm5zeDyzrfaWAXRMUd8KEutgZCEmL0UC6x9LZ1tQn0bP3HVQZMZt7yIBDQ53yR7aZmFmQmqK3DVO55n2twCIl9ZNtEojnbR-hs5emPdI0SZtJQERbUXPBNN5vsUaI4co1hDiJ00Xopf6osZDgtcFpZVdQGWlAjEhGA2TSGU_DM31LrWqYiUMWiRIPfdyd6hHeypHXmwxTuc2dVzaREhAowJy9YGeAAZFfyIjrmYfcWrifudWRyxGcNk0x-iRMgXQsYxJx0vDJEvsuslpfkJhkTYrU8tCVPEqul9yj1muYtyvbLjQc9qPgRSlkqqHCzMooQkhF99JaUstB2kGGv0VQrloBRfVqLkK4crgPFh9GDef-O3KPby5zB5cFvw0zQukSnaKCM34bjtOH1Zh9otyzCXawkkUOcrUA6vb3R1CFrWmvSZkGli_Ga9n4Q0vEkcm13rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت آبی مسجد همت تجریش؛ سازه خلاقانه و جذاب که بدون نیاز به برق یا باتری کار میکنه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698305" target="_blank">📅 09:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d54b2c37.mp4?token=mPdZ4Ii1KTAP4fPblQupyhrGUWJVC1uFgWQQ9-2cEPtCFN6dEaMlYmFQ6yEC_0Dr23QL3IcSOnZdnNNV7lNCn4c8f3whvfRX3YoD2HON75IxsgHo7sd8bF7Mnde4q4zbjnVilj4EIxkCSZyUwRllDdLznUXEJErcz09s1lGOBRXoTSyUL5WOqmDAuEDCjWO_JGLxGY9PhNd_jFbp9LQrcHjet8RijZ8ikAD4832jA1BsBGoCYFpJDtu9ePB78SXC6wqR113HKzQEW_Ca4T3sptq1qrO2wxMq0Urv__UDi04GOAlm_IppQQk2vdzRWG593sPQsDfdmbQYq0dw0vNA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d54b2c37.mp4?token=mPdZ4Ii1KTAP4fPblQupyhrGUWJVC1uFgWQQ9-2cEPtCFN6dEaMlYmFQ6yEC_0Dr23QL3IcSOnZdnNNV7lNCn4c8f3whvfRX3YoD2HON75IxsgHo7sd8bF7Mnde4q4zbjnVilj4EIxkCSZyUwRllDdLznUXEJErcz09s1lGOBRXoTSyUL5WOqmDAuEDCjWO_JGLxGY9PhNd_jFbp9LQrcHjet8RijZ8ikAD4832jA1BsBGoCYFpJDtu9ePB78SXC6wqR113HKzQEW_Ca4T3sptq1qrO2wxMq0Urv__UDi04GOAlm_IppQQk2vdzRWG593sPQsDfdmbQYq0dw0vNA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی جدید انویدیا؛ گفتگو با ربات، درست مثل حرف زدن با یک انسان
!
🔹
با PersonaPlex-7B، یه مدل رایگان و متن‌باز که هم‌زمان گوش می‌ده و جواب می‌ده، مکالمه با هوش مصنوعی دیگه شبیه چت کردن نیست؛ انگار واقعاً داری با یکی حرف می‌زنی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/698302" target="_blank">📅 09:13 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
