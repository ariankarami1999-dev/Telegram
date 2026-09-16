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
<img src="https://cdn4.telesco.pe/file/FIXAL94d67otrcg8al9JeVjYlStH4suVu0r5XETLbJi8FwmuwZqNN3_IpLUuGWr2IbZxXmy-EI9H5YVvn3XSI86dvx9Mr5XHRirG9Zr2D-GUbOmRBjhFVkahDMsIp8xzh5VMdM9MrhtxnBL9IPBFnt3lp4IJzxY9zd8JDfhi7MhdUuizq4SQxFY40YTaQNRcYNGmXVOg3KSJDEPqq2QYf3W_vZNp_INN2c66pn8vI5Zt6dTWBsnZUFhFfYAd9ErQ8iUyjLuAcoJ9sXr4uHIB9R4RTErnF3gAr0fM7piI3sU7c05OHww-jPnUvSuCEjYt-86IjHR_CVgN7xQAZozeaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.11M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-690407">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نتایج امتحانات نهایی اعلام شد؛ آغاز مهلت ۷۲ ساعته اعتراض
🔹
رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش از اعلام نتایج اولیه آزمون‌های نهایی و آغاز مهلت ۷۲ ساعته اعتراض خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/690407" target="_blank">📅 18:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690406">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/690406" target="_blank">📅 18:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690405">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/690405" target="_blank">📅 18:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690404">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نماینده پارلمان کره جنوبی: ترامپ می‌خواهد ما را هم تبدیل به بازنده کند ، در نهایت این ما هستیم که در تقابل مستقیم با ایران تنها می‌مانیم و تاوانش را می‌دهیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/690404" target="_blank">📅 18:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690403">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLssUNmIHf02-rptoV_D6rdGPw1fF1lAAefMsc9erL1pRQDI-6Jbb0SqzWktwrA4uWLw1nr2bSpiGsvkZoMaSvM-Pp4Mmxz5fGR4RDcQQnJtn0QXrZwKKwVPle5fhO8zUZ8dnSB7Lr5ERzWJZ9XCB_gDBCJYZjlsW5ubTFjFwfdevfZ4DpluUP88rbpg5cZfR-venYMTpsAQ4bARnw4y3jR5vJ_EvQP6orLOI8XX1-AyfENgwSxXGZ76D0ojX5JDFXmYLO51Xu33wlEB6AU93qc8FqEaWT0LWzbjPOOCcwDurqNSZwx0y97fVwiPRHf1W3DlhAtUsmEvZUroaq3kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا سپاه شرکت آمازون را در بحرین هدف قرار داد؟
🔹
سپاه پاسداران انقلاب اسلامی شرکت آمازون را در بحرین مورد هدف قرار داد. این شرکت چه اهمیت نظامی دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/690403" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690402">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/690402" target="_blank">📅 18:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690401">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
یارانه شهریورماه دهک‌های اول تا سوم واریز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/690401" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690400">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18cfd2ee59.mp4?token=rHZ43Vzpnd4yTS1mE46tPrnVbmJmt5-G1ssYfU8frnKNMqXvXzFSuebmpX7XofpbB9UgsyhOsMJVLkI2K6LZo3sSoAkjbIPvlVm4WGftilLyDEZi_inir0iTDvdbyy3wf0MJAwc15F5rc_H9YqjVD0SHjvV2oecOw8V8eph8QfGk-YKIgojnO7v5hS6b0B0vi8RH97HirlQEV2nHVEONQijAluhzi8w3hnoaWIlFzqmrQzScIH56YURiOq9pPXvgfZx1LDYEriQejS1utt0s7H_mUit7L0VneKUhdL-8jwSKlC7VHxWrvhQjR-uqr4XNJf3h2Nhss4ceMiCO6KKbb7Mgi40sjGzkBqtXer2OVEFXKbvXAPqoMCua_6qmNG6ZWX2HGOTAaJO3aPHroAn1CUxXuZgiCFi3l0qSSSWsNA8BPWeJLbYKq31krIjnt4gukW6wNZ6QIfUS-N46byOqjQFWxVhE3djej0erzsvRdAaOlRTKdIQKBwpHaEtBMGytyhCtirMNxh0CSF9sqtnU_Bs2UlZnxxgUJY6-LTS4FyYAeGFlPrdcunbmViO66nS3I83lGPrHWPsfSX06PS2AkqVFqwX-hcIFvbcXlchZB5R4OrEnKZj3osR_5bTBzanDPrQkUGx4LJABF52UC4IJs0lOhTUIG9jRGqJQAf27XWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18cfd2ee59.mp4?token=rHZ43Vzpnd4yTS1mE46tPrnVbmJmt5-G1ssYfU8frnKNMqXvXzFSuebmpX7XofpbB9UgsyhOsMJVLkI2K6LZo3sSoAkjbIPvlVm4WGftilLyDEZi_inir0iTDvdbyy3wf0MJAwc15F5rc_H9YqjVD0SHjvV2oecOw8V8eph8QfGk-YKIgojnO7v5hS6b0B0vi8RH97HirlQEV2nHVEONQijAluhzi8w3hnoaWIlFzqmrQzScIH56YURiOq9pPXvgfZx1LDYEriQejS1utt0s7H_mUit7L0VneKUhdL-8jwSKlC7VHxWrvhQjR-uqr4XNJf3h2Nhss4ceMiCO6KKbb7Mgi40sjGzkBqtXer2OVEFXKbvXAPqoMCua_6qmNG6ZWX2HGOTAaJO3aPHroAn1CUxXuZgiCFi3l0qSSSWsNA8BPWeJLbYKq31krIjnt4gukW6wNZ6QIfUS-N46byOqjQFWxVhE3djej0erzsvRdAaOlRTKdIQKBwpHaEtBMGytyhCtirMNxh0CSF9sqtnU_Bs2UlZnxxgUJY6-LTS4FyYAeGFlPrdcunbmViO66nS3I83lGPrHWPsfSX06PS2AkqVFqwX-hcIFvbcXlchZB5R4OrEnKZj3osR_5bTBzanDPrQkUGx4LJABF52UC4IJs0lOhTUIG9jRGqJQAf27XWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهت آشنایی و کسب اطلاعات کامل از حساب معاملاتی شیلد zorafx وارد کانال زیر شوید.
https://t.me/zorafx_broker</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/690400" target="_blank">📅 18:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690399">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/690399" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690397">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/690397" target="_blank">📅 18:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690393">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/690393" target="_blank">📅 17:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690392">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تصاویری از لحظه سرنگونی یک جنگنده F-۱۵ سعودی توسط انصارالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/690392" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690390">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/690390" target="_blank">📅 17:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی تعلیق کرد
🔹
بر اساس بخشنامه‌های ابلاغ‌شده، مسیر تهران-مسقط از ۲۶ شهریور و مسیرهای تهران-استانبول و تهران-آنکارا از ۳۰ شهریور لغو می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/690389" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690388">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/690388" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690387">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/690387" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سوئد کارمند سفارت ایران را اخراج کرد
🔹
سوئد یکی از کارکنان سفارت ایران در استکهلم را اخراج و سفیر ایران را احضار کرد.
🔹
به‌تازگی وزیر دادگستری سوئد، بدون ارائه شواهدی، ایران را به انجام «رفتارهای خصمانه» و تهدید منافع اسرائیل در خاک این کشور متهم کرده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/690386" target="_blank">📅 17:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690385">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/690385" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690384">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/690384" target="_blank">📅 17:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690383">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/690383" target="_blank">📅 17:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690381">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690381" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690380">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بلومبرگ:  عربستان پس از تعطیلی خط لوله نفت خود، فروش فوری و نقدی نفت خام خارج از تنگه هرمز را افزایش داده
🔹
شرکت آرامکو این هفته حدود ۲۰ میلیون بشکه نفت خام به پالایشگاه‌های آسیایی فروخته؛ خریداران می‌توانند این محموله‌ها را در خارج از تنگه هرمز تحویل بگیرند.…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/690380" target="_blank">📅 16:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690379">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/690379" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690378">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a34ddfbf.mp4?token=dJWqjbHGu_WYx1TD3b0mPaIj7Av6YPUbkxsiRPi5NkbfOFdypBcmiNftGssrFftur27Iba-o4pOPYfVXbEd_v72BXmavr2yQS0ZEyZIBhM90FZWLQa8T-3_eEEf-xPK6LoqqPFkHHSeCAmnKzsCGRvoHTG7gBGSA3Lo-eENXtFpzjw2N6T3fT_QYWRfPy0Ri90rEYAiCayUnIudkpzM9HcmMISXMyToz8jOGPRqrypa2VgWez-Wc09h3PgsX6TGKvR5XrkRSLY8GU2X-zBE5rFUIQdbm_SpS8dkgyfB3tGtPueTW8o3PtRBl6-gmfNiSx_5wVvbO9gwRrsDvO_9Wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a34ddfbf.mp4?token=dJWqjbHGu_WYx1TD3b0mPaIj7Av6YPUbkxsiRPi5NkbfOFdypBcmiNftGssrFftur27Iba-o4pOPYfVXbEd_v72BXmavr2yQS0ZEyZIBhM90FZWLQa8T-3_eEEf-xPK6LoqqPFkHHSeCAmnKzsCGRvoHTG7gBGSA3Lo-eENXtFpzjw2N6T3fT_QYWRfPy0Ri90rEYAiCayUnIudkpzM9HcmMISXMyToz8jOGPRqrypa2VgWez-Wc09h3PgsX6TGKvR5XrkRSLY8GU2X-zBE5rFUIQdbm_SpS8dkgyfB3tGtPueTW8o3PtRBl6-gmfNiSx_5wVvbO9gwRrsDvO_9Wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فورد پهن؛ ابتکار جالب یک صنعتگر
🔹
یک صنعتگر با جوش دادن دو خودروی «فستیوا» به یکدیگر، عریض‌ترین فورد جهان را ساخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/690378" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690377">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyklLUuc2iVkn4rs5hlfRDAcmZ4rsXYLTpcqXTcQCqyHcx_xNQjojgql_4s-DK1kDtUI89anp8E841-uof_D2cEBlRw8jsM47ilgaYU68NSSV407E1ONkbWrmoOtG1T3PcVARE7f25rJMTe60eW10ds-_tua7b1x3e2U_cgICrAQlIRKLp5FfAdf6wgUW3oF8lL7N96dZEOkHVXl4OxQPxdJTnkTuEm1QOsoZMeMY1TBOXEMQaKeaIplnmI1L3VkO6QRT8DLahQUt08JLDFK264Ue5iyJAnNdYKWvCEdEdzapSK8rB7dciV9kvJtZjoeL3esS-jVrzWRel6zOlsufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارشناس آمریکایی: تحریم‌های جدید علیه ایران بی‌اثر و بی‌اهمیت‌اند
برت اریکسون، کارشناس آمریکایی حوزه ژئوپلیتیک:
🔹
تحریم‌های جدید آمریکا علیه ایران بی‌اهمیت و بی‌اثر هستند و طرح پرسر‌وصدای این اقدامات از سوی دولت ترامپ برای من به‌عنوان یک آمریکایی شرم‌آور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/690377" target="_blank">📅 16:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690376">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjAh1rBsV7qxcQkvbfWz2uXCrGDKicq1BCgWpq7hKX3Xwdx0gGO6Q2-YAamJEJVcSRRnIukewwstiyTaR5WC6z_HmrsWN5VV2YbS1pbYusU7z_xbWxp9qNAdosyJL7y2F9vf3tKJ3WOz20Yl-G2AfRqK-5DvjQsF48oEem5B1YangUsrN0Sa0sW6q28D46gZVfenX1xVHk5j1tClmb-MTggd2RoXNMqYLBGtvIDEaoCGzyxi7JfesGqocyRRftkxZFNZXPH28BYlfd084r3NcmrfpYltldrBAuYQ_BMeV8pTz9BEPxm8v8IoE-YNW3kw7ljeQ5guavJQQTOADkRbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا طرح کالابرگ توانسته نیازهای واقعی خانوارها را تامین کند؟
🔹
نتایج جدیدترین نظرسنجی متا درباره تجربه استفاده از کالابرگ، نشان می‌دهد که
بیش از نیمی
از ایرانیان، معتقدند اعتبار یک میلیونی، کمتر از مصرف معمول هر فرد است.
🔹
همچنین،
۴۱٪
از مردم اعلام کرده‌اند که فهرست کالاهای مشمول،
با نیازهای اصلی خانوار هم‌خوانی کمی دارد و نیاز به بازنگری جدی دارد
@metaacenter
#کالابرگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690376" target="_blank">📅 16:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdzg8CUoPrUr77RT9FSawbF16_B9QZfW0SVLnrAbHAsaxQ4SGxQ2gmWW2-4UF618FYzzYyEi5ljiGH3tg8Xyp9N1d8_UXj2Z3eGB9YrfxAvyidtsE4FnRc6UGd9u1XZa1ftkON4WWkonS6A9b8uWw-eWeGNMDiP1DyeXqICvsm9VM7osj-EUpgFSjvL4HUDEw16xIU9X8xlDtSViEVcCE4AK24KTeROCxcn18ugIPOZ6xLXMMUlEvyvyiFxZlnm4KxrOamBnTFH9WmbVruaSxzX771-G_Ldb6LpaiWOuQAfLsIJFvoXWdWd7g990udLuaruI9uh48LaO3snUNvvObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرونا از آستانه هشدار بالا گذشت
🔹
مرکز مدیریت بیماری‌های واگیر وزارت بهداشت از افزایش درصد مثبت کووید-۱۹ نسبت به هفته قبل خبر داد.
🔹
درصد مثبت‌شدن آزمایش‌های کرونا به ۱۱.۷ درصد رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/690375" target="_blank">📅 16:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
در تازه
‌
ترین جنایت رژیم غاصب صهیونیستی به مناطقی از غزه، تعداد زیادی از افراد عادی در زیرآوار به جا مانده از حملات هوایی گرفتار شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690374" target="_blank">📅 16:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: مهم‌ترین سرمایه امنیت ملی ایران مردم ایران هستند که در لحظه خطر، به چیزی جز میهن نمی‌اندیشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690373" target="_blank">📅 16:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb5f8539c.mp4?token=cuSCrYbGGJg6fGuLUoI6v1Q_3V5KLexBHfNoMYlJeUJFE1DoYTIjF-eA_ESKZgAnDGI_m6V3mBHWB_U4SqtQqdvSrKnqQl4Ii6LrXcNg4sXHFhsUhcwQmjhxQgRR5yOHAEY6oLiayCoqekiiXUfXS5e5Xmuyvj_iUjZpPEq6l-Qy6Jp_f16VqNoBX_CNTQ4yvHSwzm5-7Hrn1-wNu5elXVGJMQb85W0Ch9hmgDZ_s6Ybo-6GXFRydxJ6NL53QOaonSM6XNN-8U-Calwv4hRJ5Cg-AeL-aITbCJx2Li8jpT5Z3HcG8jcQ4aToq4d6DOUsPcLduwNaU5Ws2RurFeU9zpRFrQiYrEb9R1Uva7PsqM8cyHmqOgxYn0vhq0HoOgzpG9NN4aGVEAScLKdDAXHU5KsEp7V1QD79X95ktEB-gKRS2AUyX9WYlLOZW20C4PoVfDF1gE0jYb_vHKAweAjG0pZpi61Ug_z0DUrg0G_iCEenRYGy0dnr7Cup5XfvpbDSNDLAmJpIfE4nhuFj4CkfcKQmXXppIM4d-w_buvBLd7_z_RLkSir637rqCaPgUwMnyudnJ87l-YZ7iT66bKZ1-ZKvWHP1Jtd_32JUGFs3suQoeCEkeRjiyS2K-vcS9cTuDk38DQcSCXYLbq0n8clg3ZNWfc3TmRniXkV87eA8Tpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb5f8539c.mp4?token=cuSCrYbGGJg6fGuLUoI6v1Q_3V5KLexBHfNoMYlJeUJFE1DoYTIjF-eA_ESKZgAnDGI_m6V3mBHWB_U4SqtQqdvSrKnqQl4Ii6LrXcNg4sXHFhsUhcwQmjhxQgRR5yOHAEY6oLiayCoqekiiXUfXS5e5Xmuyvj_iUjZpPEq6l-Qy6Jp_f16VqNoBX_CNTQ4yvHSwzm5-7Hrn1-wNu5elXVGJMQb85W0Ch9hmgDZ_s6Ybo-6GXFRydxJ6NL53QOaonSM6XNN-8U-Calwv4hRJ5Cg-AeL-aITbCJx2Li8jpT5Z3HcG8jcQ4aToq4d6DOUsPcLduwNaU5Ws2RurFeU9zpRFrQiYrEb9R1Uva7PsqM8cyHmqOgxYn0vhq0HoOgzpG9NN4aGVEAScLKdDAXHU5KsEp7V1QD79X95ktEB-gKRS2AUyX9WYlLOZW20C4PoVfDF1gE0jYb_vHKAweAjG0pZpi61Ug_z0DUrg0G_iCEenRYGy0dnr7Cup5XfvpbDSNDLAmJpIfE4nhuFj4CkfcKQmXXppIM4d-w_buvBLd7_z_RLkSir637rqCaPgUwMnyudnJ87l-YZ7iT66bKZ1-ZKvWHP1Jtd_32JUGFs3suQoeCEkeRjiyS2K-vcS9cTuDk38DQcSCXYLbq0n8clg3ZNWfc3TmRniXkV87eA8Tpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران به ۹ جنگنده آمریکایی در اردن آسیب وارد کرد/«سی‌بی‌اس» گزارش داد در پی حمله به پایگاه موفق‌السلطی، ۹ هواپیمای نظامی آمریکا هدف قرار گرفته و آسیب دیده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/690372" target="_blank">📅 16:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آسوشیتدپرس: تعمیر خط لوله عربستان سه تا پنج هفته طول می‌کشد
🔹
خط لوله نفتی حیاتی عربستان سعودی که مورد حمله پهپادی قرار گرفته تا زمان تعمیر خسارت، عمدتا برای هفته‌ها از سرویس خارج خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/690371" target="_blank">📅 16:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTsMvuHHcNPxeN-nsgU5BEAramY1Th0NM8Yxy6A3z7psg7crJGzJ5SItrN72i3AMKBd4DCoNydA94YSPTkbm2IDcxdEYAZcpAU4DBrRklvNQ19Y168LEIzXUPmnw9ZNqdZaEMZcUO-HXMdV8DP73rNLJbXv_C7t36v51dKOQBs8EvWcD4EXg5h0NMqPzTs2NAXmx053GrBB-3II8JRSigiblo5ijLX6ynBRgwyasM8_s3tfPw4F_KFeHlQM7-MFsnIxIvZhhJwNvn0MLNXSFRyk-N70H-OPcMTmQWbyOxsLn93cfsH0lc7mEgCI95ZPXc09vuo346AD1yX_IMzF_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقوق در ترازوی طلا | پس‌انداز «گرمی»، سقوط «کیلویی» | با یک ماه حقوق ۲۰ سال پیش چند گرم طلا می‌شد خرید؟
🔹
حدود ربع قرن پیش، کارگری که دستمزد حداقلی می‌گرفت، می‌توانست با حقوق ماهانه‌اش ده گرم طلا بخرد؛ دارایی‌ای که سپرِ آینده خانواده‌اش بود. امروز، در سال ۱۴۰۴، همان حقوق به‌سختی یک گرم طلا می‌شود. این عدد ساده، شاید گویاترین تصویر از فرسایش قدرت خرید میلیون‌ها ایرانی در دو دهه گذشته باشد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245634</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/690370" target="_blank">📅 16:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf6vilVo9dykOc4LOB7NaxgnECtnWyBrw28CAFM6gjNi33v0kQXqp6-Hnp1cItGADfSnk4l-f_ZR_PMIAnaNhuvdKSNHNI4_G7ymk0RV13kEEuH_E8keTqeoQ9bdk_y2px-CJh2Q3HKo2L5dvvZ7yuOkoMf9La1neDRZ_aVbZKQ_PMMeu32yuWJj_MJHpk_JTp8d-8SGFK_FQqxWjsNSfrk11iErBlMzbU8DwLN6Pv7lVIPKNvcll0qWO_Z_Dt_sytCcAHdZwUIai1NxWluxYKQrPV29NQeXkdAP9MW65tHB4LUJSZ6Ns8P-k9iGWJ-UDmlmvLo2295Ix4kCbdp_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: چهارشنبه ۲۵ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
💳
امکان دریافت نقدی و اقساطی
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/690369" target="_blank">📅 16:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اکثریت آمریکایی‌ها ترامپ را فردی فاسد خطرناک می‌دانند
🔹
طبق نظرسنجی سپتامبر اکونومیست و YouGov، تنها ۱۸٪ از آمریکایی‌ها ترامپ را «با ثبات» و ۱۴٪ او را «تفرقه‌افکن نیست» توصیف کرده‌اند.
🔹
این نظرسنجی همچنین نشان می‌دهد صفاتی مانند «فاسد»، «بی‌رحم» و «نژادپرست» از جمله توصیف‌های مطرح‌شده درباره ترامپ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690365" target="_blank">📅 15:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690364">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f05bf09f.mp4?token=LIRop9X3xZ50rcthPIo2ucCSh1OYcGczl1ulcnTHcu8di9MQCuj9ei4lw647dMi5dfCvEH7_QEDq18kugCv9x1-mxUSYWoxX2szLLorvgbak3VDLwF9v8LM_vug7WmES846YawQODljHNKEv_vm7RgORUX8F5jEGekERhO5tBxtOzlrsXNpzlKzgxW0viVQpyP09_JBNf0mP_V_AOsZ1MbvYf0qLmOcKA0tvGBMdj1L29ArPH829qRK63c_n39BhJDziYYfKkYUaGUOWOXfOB5zU9KJQlnQOchu44sQzIpWUsqf-DeacaG-wpj-w-RsW3wJh9pHr9UOQw6fMGFqebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f05bf09f.mp4?token=LIRop9X3xZ50rcthPIo2ucCSh1OYcGczl1ulcnTHcu8di9MQCuj9ei4lw647dMi5dfCvEH7_QEDq18kugCv9x1-mxUSYWoxX2szLLorvgbak3VDLwF9v8LM_vug7WmES846YawQODljHNKEv_vm7RgORUX8F5jEGekERhO5tBxtOzlrsXNpzlKzgxW0viVQpyP09_JBNf0mP_V_AOsZ1MbvYf0qLmOcKA0tvGBMdj1L29ArPH829qRK63c_n39BhJDziYYfKkYUaGUOWOXfOB5zU9KJQlnQOchu44sQzIpWUsqf-DeacaG-wpj-w-RsW3wJh9pHr9UOQw6fMGFqebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت CR7؛ کشتی کریستیانو رونالدو با مدافع العین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/690364" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690363">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت آموزش و‌ پرورش از افزایش بیش از ۵۰ تخصص جدید در رشته‌های کار و دانش و فنی‌حرفه‌ای خبر داد
مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در
#گفتگو
با خبرفوری:
🔹
پارسال در شاخه فنی‌وحرفه‌ای بیش از ۲۴ رشته به‌روزآوری شد و در شاخه کاردانش نیز بیش از ۳۰ رشته جدید یا به‌روزآوری‌شده به تصویب رسید.
🔹
در سال پیش‌رو نیز ایجاد رشته‌های جدید در دستور کار قرار دارد و این رشته‌ها با توجه به نیاز بازار کار و با تعامل دستگاه متولی مهارت، بخش خصوصی و مؤسسات تولیدی و خدماتی طراحی می‌شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690363" target="_blank">📅 15:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690362">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgvAiK_x-U0ZoZ_cXTUeYAsx4z3M5MeTNdSAN_9b9JGf_Hvg3HluCJhteBUsS3XGwVoZXSdv5gu5fJtMw99VRu77KYq2gEl4zZtYaAkJtEmehjU06jkojuUKr1Qi7mzGTcic6a8pkf8mDhI1VJ0c2V6UHE1NK2MtADi2a006BurBM1oMn0MeKFNy8zCqFqHFOg71qTqtzsAHb6KY1W95mpDeZUuFISI-JbnpnZiPTL6bTD9ldSghGICozjVIAxosmLaYOtUOf5ln-Paz8hpdIv3Rl6sv8KluS38bjBKC7wTNCIm1IgK5GQXgkGZK4X2y6bKnRtUPuYhj-aAnlhjKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس برای بازگشت پل شور به مدار تردد؛ پیشرفت ۹۲ درصدی با تلاش ۶ اکیپ اجرایی
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان از پیشرفت ۹۲ درصدی عملیات بازسازی پل شور در کیلومتر ۳۶ محور بندرعباس - حاجی‌آباد خبر داد و گفت: با فعالیت ۶ اکیپ اجرایی و انجام بتن‌ریزی، بازسازی این پل در مراحل پایانی قرار دارد.
🔹
عباس شرفی با اشاره به تخریب کامل دهانه‌های سوم و چهارم پل دوم شور در این محور، افزود: با اجرای روند بی‌وقفه بازسازی این پل، هم‌اکنون پایه‌های آن آماده شده و پس از تکمیل تیرها در کارگاه، نصب آن‌ها در محل پروژه انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/690362" target="_blank">📅 15:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690361">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
کانال ۱۵ عبری: بن سلمان خود را در برابر حملات انصارالله تنها می‌بیند؛ در حالی که تأسیسات انرژی عربستان هر روز منفجر می‌شوند، آمریکا و اروپا هیچ کمکی نمی‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/690361" target="_blank">📅 15:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: تأسیسات آرامکو در ینبع و پایگاه خمیس‌مشیط را هدف حمله قرار دادیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690359" target="_blank">📅 15:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22bf042b3.mp4?token=WHQjtTquJ7dSI0CiglVvcmCHgMlk_d1I9NsEmi3wYw75CKckJQpOchxpJzkFYmsijKjvdF_jen6PwniLtkqO5ZY1iczK2f8cokC6uP6sij1PXAetv2bCM08fhrxPQLU5TkP7oDYesGVC70baLLrhnytwsbQ6zxt4odQuSwJJZSIVmco_SV6pT5ju5FxMc_AX9SqhVMt9tgIf5t4qUrBbfP4y9CP7PP_dghIIyMZdIuLnY-VxEtkOqzl72uJDseAwSt4ltnSRBM8g0uHds5ZQ4uFap135a5kTZMYVgRm4MDQBMPjoTS97AGk7VgXhLdMpkJ8sBulzLwiYLGnwKDEjIj9QP4f2HUAZN768eRa-ranw-yncO6bllIb9FPTRRuncB5LmHqAQ9aHJydVjWodJiRQYLK-AItuzYsXXI85z690oltmGZKfXMwSN5ST14OuaSgtvjF0UPWBQxm27ZcoYsor-ojhQqkAOIeUqvBAwTDECXoS_HSuFUSIzCMjEOf0ur2Mg8CvTAMWlyJqAPtC-uapZVNZ8RJHxjxPYiwkxngwVOdfEDD6yy9xAFFNu9XbxlZlZi4M-tCtNXLiFheiS2r6__Vch3sj-Da6bwdQaqPIph78iCtb4OmW3E7SeM84AZXRbHfER_ncmvTKDL3jiPTVN-F2adcxYZtEJRgLW52o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22bf042b3.mp4?token=WHQjtTquJ7dSI0CiglVvcmCHgMlk_d1I9NsEmi3wYw75CKckJQpOchxpJzkFYmsijKjvdF_jen6PwniLtkqO5ZY1iczK2f8cokC6uP6sij1PXAetv2bCM08fhrxPQLU5TkP7oDYesGVC70baLLrhnytwsbQ6zxt4odQuSwJJZSIVmco_SV6pT5ju5FxMc_AX9SqhVMt9tgIf5t4qUrBbfP4y9CP7PP_dghIIyMZdIuLnY-VxEtkOqzl72uJDseAwSt4ltnSRBM8g0uHds5ZQ4uFap135a5kTZMYVgRm4MDQBMPjoTS97AGk7VgXhLdMpkJ8sBulzLwiYLGnwKDEjIj9QP4f2HUAZN768eRa-ranw-yncO6bllIb9FPTRRuncB5LmHqAQ9aHJydVjWodJiRQYLK-AItuzYsXXI85z690oltmGZKfXMwSN5ST14OuaSgtvjF0UPWBQxm27ZcoYsor-ojhQqkAOIeUqvBAwTDECXoS_HSuFUSIzCMjEOf0ur2Mg8CvTAMWlyJqAPtC-uapZVNZ8RJHxjxPYiwkxngwVOdfEDD6yy9xAFFNu9XbxlZlZi4M-tCtNXLiFheiS2r6__Vch3sj-Da6bwdQaqPIph78iCtb4OmW3E7SeM84AZXRbHfER_ncmvTKDL3jiPTVN-F2adcxYZtEJRgLW52o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک تکه شیشه زیر پوست گیر می‌کند چه اتفاقی می‌افتد؟
🤯
#حواست_هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690358" target="_blank">📅 15:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ریابکوف، معاون وزیر خارجه روسیه: ایران و امارات به لطف قدرت بریکس موفق به حل اختلافاتشان شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690357" target="_blank">📅 15:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690356">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ارز برای دارو نیست، اما بعضی چهره‌ها می‌خواهند واردات لوازم خانگی را آزاد کنند! / به نام برندهای کره‌ای، به کام اجناس بی‌کیفیت ته‌لنجی!
🔹
وزارت بهداشت می‌گوید کرونا از مرحله هشدار بالا عبور کرده، ولی اگر سری به داروخانه‌ها بزنید، نه خبری از واکسن کرونا هست، نه حتی واکسن آنفلوآنزا! اما انگار ارز کافی برای لوازم خانگی پیدا می شود!
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245540</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690356" target="_blank">📅 14:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690355">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای رویترز : مقامات آمریکایی اوایل این هفته در عمان با حوثی‌ها دیدار کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690355" target="_blank">📅 14:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690354">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e768c522.mp4?token=E7cL7Jv7vkazeh0z5G8VEqRcaqMoI2Sufpvo695PqB2GCAQDYfYZ5T-W2klvgX-PsKFjJjI_EUufHyp0AKiu60VX1YtvdpEMC6wPEROQtjb9NhjmuDTR_5H2rn1r5YwQO1i6mXwUaZNtEv6l6HV_XbfogK8LHxWqm9E_nY7qk-0u783VMeurP4apKjae2Swl7vdAzMN0QMyjg5hZT1bQ4ACj9FY8Do1mxnxqFrto2tk6RXEyoJDyeBlUXKmF24Z9ttQO5F8rnro-vPwLGCBaFbPL8PiKjRQdsTQn9O3gBeZcK0R8yW2fze0IwjT9UIOdB2veaA7t3H4LOIworoltbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e768c522.mp4?token=E7cL7Jv7vkazeh0z5G8VEqRcaqMoI2Sufpvo695PqB2GCAQDYfYZ5T-W2klvgX-PsKFjJjI_EUufHyp0AKiu60VX1YtvdpEMC6wPEROQtjb9NhjmuDTR_5H2rn1r5YwQO1i6mXwUaZNtEv6l6HV_XbfogK8LHxWqm9E_nY7qk-0u783VMeurP4apKjae2Swl7vdAzMN0QMyjg5hZT1bQ4ACj9FY8Do1mxnxqFrto2tk6RXEyoJDyeBlUXKmF24Z9ttQO5F8rnro-vPwLGCBaFbPL8PiKjRQdsTQn9O3gBeZcK0R8yW2fze0IwjT9UIOdB2veaA7t3H4LOIworoltbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی ۱۰ سال قبل مرحوم علامه علی کورانی رحمت الله علیه
قبل از ظهور
۱.سقوط سوریه
۲. اختلافات داخل ایران
۳.پیروزی یمن</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/690354" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690353">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3905d8108d.mp4?token=PHPLoaaWjK2MBiDbeGu6vRHACgYTSJ54wGydPbQ_PxAFvlhKC9UE5snkbD1DuixySClcq-aXQcWGXnGTH8AbriweHPjGs_7AnwBe_Coy3kDAZUUN6eQZaB5nu01o2dCk_My5G96HZ5lTUrU_CQUPxyMgVsxuVDjGJfcII2cRNT5Fn0umRprjFVLgJNGXfj0QIMPMJDX33Ht6tdIQKs-G5pvNi0nR0aEeOcvbvJvdRSGpCdcaK5iHgHwOoLKKkOhXuUIlMHtE54lpt_uPCjWRcyilhaPdIfL3FA6nXfpSxYkX_ZxJo6C65Gkofrp1t8ug8EC3mJvrPaSFNnmdJZPiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3905d8108d.mp4?token=PHPLoaaWjK2MBiDbeGu6vRHACgYTSJ54wGydPbQ_PxAFvlhKC9UE5snkbD1DuixySClcq-aXQcWGXnGTH8AbriweHPjGs_7AnwBe_Coy3kDAZUUN6eQZaB5nu01o2dCk_My5G96HZ5lTUrU_CQUPxyMgVsxuVDjGJfcII2cRNT5Fn0umRprjFVLgJNGXfj0QIMPMJDX33Ht6tdIQKs-G5pvNi0nR0aEeOcvbvJvdRSGpCdcaK5iHgHwOoLKKkOhXuUIlMHtE54lpt_uPCjWRcyilhaPdIfL3FA6nXfpSxYkX_ZxJo6C65Gkofrp1t8ug8EC3mJvrPaSFNnmdJZPiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صورت‌های مالی فارس تایید شد/ تقسیم سود سهام ۶۰ تومانی به ازای هر سهم
🔹
صورت‌های مالی سالانه شرکت صنایع پتروشیمی خلیج‌فارس برای سال مالی منتهی به ۳۱ خرداد ۱۴۰۵ با نظر اکثریت به  تصویب مجمع رسید.
🔹
مجمع فارس همچنین به ازای هر سهم پرداخت ۶۰ تومان سود تصویب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/690353" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690352">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رئیس‌جمهور: برای صیانت از معیشت اقشار کم‌برخوردار در مورد کالابرگ تصمیم قطعی گرفته شده و اعلام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690352" target="_blank">📅 14:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690351">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b7f01aee.mp4?token=koKBz5mHHwUavMu0C-q5uonoFEHktzp31trxr7S6jgBtksem7rXN9xHec7rcHxlAcwquH2XRt2tKWOhGfuHAzsT8_CyUBF2u7YEcQ67J-h1eNTKt4wF0CN2ZNJ-SRctVanI9SWZFSdU31l1eNW8d-63tU_WPLy48Fix5wG1wmEwY4v1tDu_qktXPk9r3up-fwvu16f4doZHsnwO5g4CBbnTVaQzOgIIYqnW-AA4Y2o_4pyLsIiXhBdnrV_IqjDP1Zs78qHk3xuOyARG5rggeKX22yupVbredV3ByeNwwU7U1yldaBT029ujkEAjFyAg-R7twfr3guOxEMuZoeBfYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b7f01aee.mp4?token=koKBz5mHHwUavMu0C-q5uonoFEHktzp31trxr7S6jgBtksem7rXN9xHec7rcHxlAcwquH2XRt2tKWOhGfuHAzsT8_CyUBF2u7YEcQ67J-h1eNTKt4wF0CN2ZNJ-SRctVanI9SWZFSdU31l1eNW8d-63tU_WPLy48Fix5wG1wmEwY4v1tDu_qktXPk9r3up-fwvu16f4doZHsnwO5g4CBbnTVaQzOgIIYqnW-AA4Y2o_4pyLsIiXhBdnrV_IqjDP1Zs78qHk3xuOyARG5rggeKX22yupVbredV3ByeNwwU7U1yldaBT029ujkEAjFyAg-R7twfr3guOxEMuZoeBfYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌ صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌ از دیگری به‌ سراغ او می‌آیند
🔹
رسانه‌های خبری از سرنگونی جنگنده F۱۵ عربستان توسط نیروهای ارتش یمن (انصارالله) خبر دادند
🇮🇷
…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690351" target="_blank">📅 14:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690350">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای رویترز : مقامات آمریکایی اوایل این هفته در عمان با حوثی‌ها دیدار کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/690350" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690349">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUfcRg7gHpJBwrwJdfV8CHt6zmxBgufPyBC9RK20uq87TX3zsmx3KoVkM97z0luiVObmyZU_U0R99b59D45-rkYJgyqmSBaw9ZHCl6OPZ7DDpHPM_28qLYlCtvaMtM1NqqXrX0mKWlBta750VynwmEb31S6JApgzAYqL_2EzM6N9xC8IahH83Knn9V0qdM_o-oX56KseSBiUasvK0MWjmN7ZlHOvZTPhYz7PegOCWZDI-xbTt9o_HS1Zh8Zta1JBt5klek7IlSwBGJeq3Xb5j_wRIKdNYgHlG7SXHX0pihj76ioryx-h8mtvxZXx3w4K9zVOCd4qILD4ZS1SOeSZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند ۱۰ ساله بارش در ایران
🔹
آمار مرکز ملی خشکسالی نشان می‌دهد  بارش‌های کشور پس از اوج‌گیری در سال‌های ۹۷ و ۹۸، وارد دوره‌ای خشک و کم‌بارش شده است.
🔹
میانگین بارش سالانه کشور از اوج ۲۹۱.۶ میلی‌متر در سال ۱۳۹۷ به ۱۹۴.۵ میلی‌متر در سال ۱۴۰۴ رسیده است.
🔹
در این بازه ۱۰ ساله، بیشترین افت بارش با ۳۶.۶- درصد در سال ۱۳۹۶ و بیشترین رشد با ۲۴.۱+ درصد در سال ۱۳۹۷ ثبت شده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/690349" target="_blank">📅 14:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690348">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191ba4e16b.mp4?token=UBVdpfpjBiixybgUfYXn6kXR51kttL1UH17oM37HmeMMidvUmZe9Zj5vqvBTHz5VAVvGvR5VCbwirUFqJLICpH-UiSDz88Nd1heFV0_sesKC6XLCHnWd2BfeltCw8yYEg7Cr93FflPapPXwN8fTLVkHUJUcdkgEhEA8k_HleGbNTwqM0QSkfGXhSl07Kw3fxDwrEQXWzWk2mWgKN-FT_4sfgew-dTvIfCli2hrjVw5153u3ig85afOXiDIZ9A-jGWi3wZ7u_zx7goOadRpy01z4ehZ69-u9NfSyJshViNTECYx9cwv1zwIkdzj6MKdoms3xRIaAmxv9c5ExCpO8u1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191ba4e16b.mp4?token=UBVdpfpjBiixybgUfYXn6kXR51kttL1UH17oM37HmeMMidvUmZe9Zj5vqvBTHz5VAVvGvR5VCbwirUFqJLICpH-UiSDz88Nd1heFV0_sesKC6XLCHnWd2BfeltCw8yYEg7Cr93FflPapPXwN8fTLVkHUJUcdkgEhEA8k_HleGbNTwqM0QSkfGXhSl07Kw3fxDwrEQXWzWk2mWgKN-FT_4sfgew-dTvIfCli2hrjVw5153u3ig85afOXiDIZ9A-jGWi3wZ7u_zx7goOadRpy01z4ehZ69-u9NfSyJshViNTECYx9cwv1zwIkdzj6MKdoms3xRIaAmxv9c5ExCpO8u1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با همین گل‌های‌ ریز می‌تونی جیب‌هات رو خوشگل کنی
🌼
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690348" target="_blank">📅 14:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690347">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9b3c3589.mp4?token=AGSwEXMDyDZdiZngtCp57rPDf-CQBBJQ-yNuXrd9U9gL6M9IWEOoQYsq1tq_OyBcPaTKQDv-UTlSPDeLWrHRq_hVHXnDGxlNWzLD7nrvatXuGAiCAFj-0V05ZipVe-Y4XBjH5ywQEQOjsdjbrJo-DGTIdw0D39P3yQwdUmVXZH9yVnkP5YDqh9pYrRtv62HoMOoymKZCW3fqCFtUh5oKA1bvd3lrFM1JtwACuSNO4So-1TIzzOpARh-n68GoYzmVWFaTqN4OUB5mG9OvtpU_aEsFGItF4p3M-fdSX7_CG21OSdaCZK7QMdLo3Nfu6mQl7TSE9KLeH_jO20vcMwUv4lMx2uDDbtNYElNxM-3WGbXyUzxRw6dHFs14gYsjbHUK_fq1RO5f9tyOJWLOvz4E9mSP9uavPz1RjvM_Vl2vi_zlrGxkijOqkpXiYBWjHOTgTDR9eR8EcRfb0hQudoZrJNYzn-VPaqIglE8DaofXXCc1gVw9ZtM8aSJfqNgnwj1AuxzhhyDAGWTuubW0YNzzuYPeeKJ1FCNtOQJsdKHu0vVHKQr55RJ_gDKmbpYDTXPwO5CoJGJI2Z43Dzo6XDtZQaGr9Kc14ahypkqnHfSPryoLWSulNY6NZRya0L9hGVFdh-hoK6weytHFdE7B-ps0OD1DtfEx7Nisjb2qr5OEsXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9b3c3589.mp4?token=AGSwEXMDyDZdiZngtCp57rPDf-CQBBJQ-yNuXrd9U9gL6M9IWEOoQYsq1tq_OyBcPaTKQDv-UTlSPDeLWrHRq_hVHXnDGxlNWzLD7nrvatXuGAiCAFj-0V05ZipVe-Y4XBjH5ywQEQOjsdjbrJo-DGTIdw0D39P3yQwdUmVXZH9yVnkP5YDqh9pYrRtv62HoMOoymKZCW3fqCFtUh5oKA1bvd3lrFM1JtwACuSNO4So-1TIzzOpARh-n68GoYzmVWFaTqN4OUB5mG9OvtpU_aEsFGItF4p3M-fdSX7_CG21OSdaCZK7QMdLo3Nfu6mQl7TSE9KLeH_jO20vcMwUv4lMx2uDDbtNYElNxM-3WGbXyUzxRw6dHFs14gYsjbHUK_fq1RO5f9tyOJWLOvz4E9mSP9uavPz1RjvM_Vl2vi_zlrGxkijOqkpXiYBWjHOTgTDR9eR8EcRfb0hQudoZrJNYzn-VPaqIglE8DaofXXCc1gVw9ZtM8aSJfqNgnwj1AuxzhhyDAGWTuubW0YNzzuYPeeKJ1FCNtOQJsdKHu0vVHKQr55RJ_gDKmbpYDTXPwO5CoJGJI2Z43Dzo6XDtZQaGr9Kc14ahypkqnHfSPryoLWSulNY6NZRya0L9hGVFdh-hoK6weytHFdE7B-ps0OD1DtfEx7Nisjb2qr5OEsXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییرات بزرگ سیستم عامل جدید آیفون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/690347" target="_blank">📅 14:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690346">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تاکنون طرحی در خصوص خروج از NPT در مجلس تنظیم نشده است
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به اقداماتی که علیه ایران در موضوع هسته‌ای انجام شده، از جمله فعال‌شدن مکانیسم ماشه و ممانعت از حضور هیئت ایرانی در وین، عملاً اعتبار NPT از بین رفته و دیگر چیزی به نام NPT برای ایران مطرح نیست.
🔹
ایران همکاری‌های خود با آژانس بین‌المللی انرژی اتمی را نیز بر اساس مصوبه مجلس متوقف کرده است.
🔹
در کمیسیون امنیت ملی به‌صورت غیررسمی درباره خروج ایران از NPT بحث‌هایی انجام شده اما تاکنون طرح یا لایحه‌ای در این زمینه تنظیم نشده و در صورت تصمیم برای خروج، تصمیم نهایی با مجلس خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/690346" target="_blank">📅 14:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690345">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2046d9aba.mp4?token=fKMTKM0RzIy4JE9Ppww2bY0vXnicTu9VoGrV666LcDMZYhEFm8rIugAHFyQMKh_agQaCZ1OJWjnJ6yStDTU7TvjLirb1ReIM13sE-R6YLCC2ogxhFeaFJwHG6ZsE-D53GMzQFDrqh5qEWwRMSqMk6i7oy-QFIPY1021VGdB3SVcRMZqHvZtYC-q1fsyaHKDoqnLqWdCUAawLE5dkKVHpk_otap7P0o6E2FGjwZ5-oekK4Q2LIjC2GsyJzX_G5hW0BtFClGfEkWOzLSWvpJl4Cu9qzyohPjfbQcU_jRJ9OFQLPpiavToFxgUBHCj0nDhpDum2hUrTDHPZwX4mtpBtxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2046d9aba.mp4?token=fKMTKM0RzIy4JE9Ppww2bY0vXnicTu9VoGrV666LcDMZYhEFm8rIugAHFyQMKh_agQaCZ1OJWjnJ6yStDTU7TvjLirb1ReIM13sE-R6YLCC2ogxhFeaFJwHG6ZsE-D53GMzQFDrqh5qEWwRMSqMk6i7oy-QFIPY1021VGdB3SVcRMZqHvZtYC-q1fsyaHKDoqnLqWdCUAawLE5dkKVHpk_otap7P0o6E2FGjwZ5-oekK4Q2LIjC2GsyJzX_G5hW0BtFClGfEkWOzLSWvpJl4Cu9qzyohPjfbQcU_jRJ9OFQLPpiavToFxgUBHCj0nDhpDum2hUrTDHPZwX4mtpBtxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجموعه نقره برادران هاشمیان، شما را به بازدید از آخرین دستاوردها و محصولات اختصاصی سرمایه‌گذاری دعوت می‌نماید.
فرصتی برای گفتگو درباره استراتژی‌های سرمایه‌گذاری در بازار نقره و رونمایی از کالکشن آناهیتا.
زمان:
26 الی 29 شهریور| ساعت 15 الی 21
مکان:
محل دائمی نمایشگاه بین المللی اصفهان - غرفه B208
کانال اطلاع رسانی مظنه نقره خام برادران هاشمیان:
https://t.me/hashemiansilverbar</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690345" target="_blank">📅 14:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690344">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ایرنا: ۶ همت از مطالبات مراکز درمانی دانشگاهی پرداخت شد
🔹
سازمان تأمین اجتماعی امروز سه‌شنبه، ۲۴ شهریور، ۶ هزار میلیارد تومان از مطالبات مربوط به اسناد رسیدگی‌شده مراکز درمانی دانشگاهی و علوم پزشکی طرف قرارداد در سراسر کشور را پرداخت کرد.
🔹
این پرداخت، بخشی از روند تسویه مطالبات مراکز درمانی است و با هدف حمایت از مراکز ارائه‌دهنده خدمات و جلوگیری از ایجاد اختلال در درمان بیمه‌شدگان و بازنشستگان انجام شده است. روند پرداخت سایر مطالبات نیز از سوی سازمان تأمین اجتماعی ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/690344" target="_blank">📅 14:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690343">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
وزیر اقتصاد: ۳۰۰ هزارتومان کف افزایش کالابرگ است   وزیر اقتصاد:
🔹
درباره میزان رقم افزایش کالابرگ هنوز جزییات مشخص نیست و در حال بحث است.
🔹
کف افزایش ۳۰۰ هزار تومان است ولی هنوز دهک ها مشخص نیست./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690343" target="_blank">📅 13:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690342">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وزیر اقتصاد: ۳۰۰ هزارتومان کف افزایش کالابرگ است   وزیر اقتصاد:
🔹
درباره میزان رقم افزایش کالابرگ هنوز جزییات مشخص نیست و در حال بحث است.
🔹
کف افزایش ۳۰۰ هزار تومان است ولی هنوز دهک ها مشخص نیست./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690342" target="_blank">📅 13:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690340">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYiNYWoaGryiUFbwGrR-D6eSWQXn6qharw6U7E6er1Tj_JJlNuocYQByEDdHXs5UMvcQZu80bQjyVLNMIiijDcIHfMGr5z43W6s4PILxczLBmX8UbH2jkviL-tJOIUog8mALsrnymPH9Aj_Y05K_hwhSQQNxPZDtiBuHZZECtpIJAVz4c_BZd94Da7Xoga55Zy7f8PahhyGX-p3L__bAltb-nWFN70LNUXy5uiD6Jlj9qOsCuHTk5eRO2obOVhCsNb3uWWK7KWuIf4XqtHILsyaum05wMq_jocm8ayJlRWVLiDiWJf7GgswKWBIHuzPxH9P0mVf_C1FIQM5CZ5EXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامانه ناظر طلا؛ نظارت بدون متولی؟
🔹
الزام سکوهای فروش آنلاین طلا به اتصال به «سامانه ناظر» در حالی وارد مرحله اجرا شده که همچنان درباره متولی سامانه، مبنای حقوقی، دستورالعمل نظارتی و حدود مسئولیت دستگاه‌ها پرسش‌هایی وجود دارد. این سامانه قرار است موجودی طلای سکوها را با تعهدات آنها تطبیق دهد و از خالی‌فروشی جلوگیری کند.
🔹
در کنار ضرورت نظارت بر پشتوانه معاملات، نحوه حفاظت از اطلاعات مالی کاربران نیز به یکی از چالش‌های اصلی تبدیل شده است؛ اینکه داده‌ها کجا نگهداری می‌شوند، چه نهادهایی به آنها دسترسی دارند و در صورت خطا یا نشت اطلاعات، چه دستگاهی پاسخگو خواهد بود.
🔹
حاکم ممکان، عضو کمیسیون اقتصادی مجلس، با تاکید بر ضرورت نظارت بر سکوهای فروش آنلاین طلا گفت: «اصل نظارت بر فعالیت سکوهای طلا و اطمینان از وجود پشتوانه کافی برای معاملات ضروری است»، اما متولی سامانه و حدود مسئولیت دستگاه‌ها باید به‌طور شفاف مشخص شود.
🔹
فرشاد ابراهیم‌پور، عضو هیات‌رئیسه مجلس نیز تاکید کرده است: «اصل نظارت بر فعالیت سکوهای فروش طلا موضوعی قابل دفاع است»، اما پیش از الزام سکوها به اتصال، دستورالعمل نظارتی و مسئولیت دستگاه‌ها باید مشخص و ابلاغ شود.
🔹
در نهایت، پرسش اصلی این است: سامانه‌ای که قرار است ابزار نظارت بر بازار طلا باشد، خود تحت نظارت کدام نهاد و بر اساس چه چارچوبی فعالیت می‌کند؟/ دنیای اقتصاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690340" target="_blank">📅 13:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690339">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">معرفی و میزان تخریب پایگاه شاهزاده سلطان (الخرج)
🔹
در طول جنگ رمضان، ایران در جواب حملات دشمنان، ضربات متعددی به پایگاه‌های آمریکایی در ۷ کشور منطقه وارد کرد.
🔹
آمریکا دارای ۱ پایگاه اصلی در کشور عربستان است و بقیه تجهیزات نظامی آن در کل کشور عربستان به صورت…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690339" target="_blank">📅 13:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690338">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وزیر اقتصاد: ۳۰۰ هزارتومان کف افزایش کالابرگ است
وزیر اقتصاد:
🔹
درباره میزان رقم افزایش کالابرگ هنوز جزییات مشخص نیست و در حال بحث است.
🔹
کف افزایش ۳۰۰ هزار تومان است ولی هنوز دهک ها مشخص نیست./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/690338" target="_blank">📅 13:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690337">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
خبرفوری| هم‌اکنون نرخ سوم سوخت از ۵ هزار تومان به ۱۰ هزار تومان تغییر کرد @AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/690337" target="_blank">📅 13:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690335">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGXoRBPVXHWdIHNkvPQDNiyPJB_8Bjw4wZM_1K3SsdeMeqUr2LGJ60AvfAU7HhtXl2TShaz0_WnfSCkh6bcWZlrp9SIRQu3dqZhWacEoQC6Osflcrkdr0TB3UOABPLqxlZKne7_0mKMCuJ9EGIPDqx5_wYin0r2gzLQlU3k86meO8PG19giSgwAOi90Uf_9UWk3zWtjf0pJExbms6n6VXzIXdMiMYvD2pRYPSvCAWV193RTcgOCvjtocQ7bfUWXuXejIjldisUw62B7VImWTsvk1iiU69Yjw-pgsclj9bnnefr6j1ikZ_07wBF9zvH-JBkwxD4gWZGrMUEmSbKe4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش میلی‌ به ادعای طلای تقلبی: تصویر منتشرشده ارتباطی با شمش‌های میلی ندارد
🔹
پس از انتشار ادعاهایی درباره تحویل طلای تقلبی در میلی‌، مدیر ارتباطات این پلتفرم در گفت‌وگو با رویداد۲۴ این ادعاها را رد کرد و گفت بسته‌بندی منتشرشده در فضای مجازی اساساً متعلق به میلی نیست.
🔹
امیرحسین صدقی تأکید کرد تاکنون بیش از ۵۵۰ کیلوگرم طلای فیزیکی به کاربران تحویل شده و هیچ گزارشی درباره تقلبی بودن شمش‌های تحویلی ثبت نشده است.
🔹
او ادامه داد:  آنچه در روز‌های اخیر در فضای مجازی منتشر شده، اساساً ارتباطی با شمش‌های تحویلی میلی ندارد. شمش‌های طلای میلی با بسته‌بندی اختصاصی، قفل‌های امنیتی مشخص، هولوگرام و چندین لایه اصالت‌سنجی به کاربران تحویل داده می‌شوند. سکه یا بسته‌بندی که تصاویر آن در شبکه‌های اجتماعی منتشر شده، از اساس متعلق به میلی نیست و نسبت دادن آن به این مجموعه نادرست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/690335" target="_blank">📅 13:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690334">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
الجزیره: چین از ایران و آمریکا خواست به تفاهم‌نامه بازگردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690334" target="_blank">📅 13:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690333">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال قطع گاز خانگی در پاییز و زمستان
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
با توجه به احتمال سردتر بودن پاییز و زمستان امسال، افزایش مصرف خانگی و کاهش بخشی از تولید به‌دلیل حملات آمریکا به تاسیسات گاز، کشور در حوزه تأمین گاز با چالش جدی مواجه خواهد بود.
🔹
بخش عمده کسری گاز از طریق محدودیت مصرف صنایع، جبران می‌شود اما ممکن است امسال برخی استان‌های دورتر از منابع گازی به‌دلیل کاهش فشار، حتی گاز خانگی خود را نیز از دست بدهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690333" target="_blank">📅 13:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690332">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
پایین کشیدن پرچم حکومت جولانی در منطقه الحسکه در شمال شرق سوریه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/690332" target="_blank">📅 13:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690331">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daTchCF_wtTl-GJphlA69ne4EyTfovtUphhNRoWeeKiUH4UgyEhIVtv-mn5YI3E-6-hgL1JVlUH7SOCDxVaqK0O-E7jVJETCsyO3_occmdfufQ3Q1F8d0PJF-m7YTVW2xxfJFEYnSM_ZLOLhSiNScytCLIZFsWgGHIZjEzbK8g-9W1Tvp-2SMBy00SldO7A7iyh4b_iCTc0bmQxCa8wCtszsk9d7d64iI8MnH7BqtZkcQ_JQgQmr-66WyIAFwWZk8dRU11cH_AGv9ufVpo3sjOD5PVwHWd6a9C_TClclSajUpoGw-QjgHxJjtLNPQV0mDt87ZUMt_VUfsiUdFyor2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۵ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
بازار امروز شاهد رفتارهای واگرا میان بازارهای دارایی بود؛ در حالی که دلار آزاد با عقب‌نشینی از سطح ۲۳۰ هزار تومانی به مسیر کاهشی بازگشت، بازارهای طلا و سکه تحت تأثیر رشد انس جهانی طلا، روند صعودی را در پیش گرفتند.
🔹
طلا ۱۸ عیار با جهش ۳۵۰ هزار تومانی از مرز ۲۳ میلیون و ۵۰۰ هزار تومان عبور کرد و سکه بهار آزادی نیز با قیمت ۲۲۹ میلیون و ۵۴۰ هزار تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690331" target="_blank">📅 12:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690330">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/busjA1nMn9P8T83msPQVDWsolcTI9LYSCl9sz5p80CwsZCJZ__ghAmme6p7rMmxITCi0OYbABb7Lar5CZpSzvU-yqWhTrOj6Z_cDboS8Kjmenyztza7uW8U0kSxCxCju_IcXNRqeFCVKq6PEiwioI33ohb-l_HDjb1GgpXXChbXzotKHnQnkA-p1U7rm_7jZaMzzaxAAdorLVN1r47ghn3OAlNKsWVOOo2YnTpdgIRxqAltjKjZbrmUiAHnOlCLtgD5H-KSAzyAs5UEcvUGBkO47bGLhPNUgDq__tyKkh4rVl9Y2MIYC8ObLdRjUWyTf-mQ12a8BBOUMkUc1PZbs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین دیوارنگاره میدان ونک با اشاره به غنیمت گرفتن زیردریایی آمریکایی
صید هرمز؛ بازار باشه!
🔹
همزمان با هدف قرار گرفتن ناوهای متخاصم و زیردریایی پیشرفته آمریکایی در آب‌های خلیج فارس، از جدیدترین طرح دیوارنگاره میدان انقلاب تهران با شعار "لشکر شیطان در خلیج فارس غرق خواهد شد" رونمایی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/690330" target="_blank">📅 12:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690329">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
الجزیره: چین از ایران و آمریکا خواست به تفاهم‌نامه بازگردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690329" target="_blank">📅 12:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17905a14b6.mp4?token=lxmZDrQMERRwtbX6soAWWKcZqX8LU7cyvB9HRbqB_NlIoukKqAgR7LbUDt-VEpHm33lgr83tzc8uOkLYl1cX0XB9mf0ycmPbbZiIO9Lq9jM5sL--4HEYEBVglPT-YUcjlGXiQN3nD9gNlZzkVkidMA_6hUVoRcWxrQQkXK6WjfEfiTgIBqt21avAYg8auF84OoXSvgckNVRwjAIJfUIDrvhUisNdU1tUpPgAqWWx9CbevMXsACxlm6-x0BnbiAzEEDD9MjbyayuwX9XEunSkXDUl_e7cpNHZLy6b62gX-K6eHOHZE3x8tka48g7-kxgxAio78FyiM7xCozapG25kxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17905a14b6.mp4?token=lxmZDrQMERRwtbX6soAWWKcZqX8LU7cyvB9HRbqB_NlIoukKqAgR7LbUDt-VEpHm33lgr83tzc8uOkLYl1cX0XB9mf0ycmPbbZiIO9Lq9jM5sL--4HEYEBVglPT-YUcjlGXiQN3nD9gNlZzkVkidMA_6hUVoRcWxrQQkXK6WjfEfiTgIBqt21avAYg8auF84OoXSvgckNVRwjAIJfUIDrvhUisNdU1tUpPgAqWWx9CbevMXsACxlm6-x0BnbiAzEEDD9MjbyayuwX9XEunSkXDUl_e7cpNHZLy6b62gX-K6eHOHZE3x8tka48g7-kxgxAio78FyiM7xCozapG25kxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز خنک‌کننده یخچال‌های باستانی ایران؛ شاهکار مهندسی و معماری
🔹
در دل کویرهای ایران، یخچال‌های باستانی راهکاری شگفت‌انگیز برای تولید و نگهداری یخ بودند؛ بدون برق و با استفاده از معماری هوشمندانه، سایه، جریان هوا و سرمای شب.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690328" target="_blank">📅 12:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690327">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
حمله سایبری به دو نفتکش در تنگه جبل‌الطارق
وال‌استریت‌ژورنال:
🔹
دو نفتکش با پرچم کشورهای خارجی که عازم آمریکا بودند، هنگام عبور از تنگه جبل‌الطارق هدف حملات سایبری قرار گرفتند. واشنگتن تاکنون عامل این حملات را شناسایی نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690327" target="_blank">📅 12:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690326">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
گلایه رانندگان از وضعیت نابسامان مرز دوغارون/ متولی این مرز کدام دستگاه است؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690326" target="_blank">📅 12:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d353ee59.mp4?token=PFA1RyxBgzJik96Mz5pWmmFvqheI_I5mRY9WJByW5VxE54a_ceT0v8fkgQzUd0CF3KDQgRe2TAmlkjNU7xA00O1QhiquW4T9fFzX6bODNpm3j1fFms3ZdyhUJbnrlvgPJpkjx3l-vKtED3WjnbZkiaPyUrisZ7P0cjTNah4UF6lEQ_avIj4Bx9REpHSI-gV3_cVxeiN_70z9xBYkICghjL_hsY5yX0SS94m-GX2nQLZjPw59584KIksNTZ8Sgv4ZQbmNE_3NTy58vEZYjvTtZrsgF-Cks2NgAFY5wUotOIA03V0Mwg7QN0UmYLbWG-kPj_JoL87rIoX3_ObvD-eWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d353ee59.mp4?token=PFA1RyxBgzJik96Mz5pWmmFvqheI_I5mRY9WJByW5VxE54a_ceT0v8fkgQzUd0CF3KDQgRe2TAmlkjNU7xA00O1QhiquW4T9fFzX6bODNpm3j1fFms3ZdyhUJbnrlvgPJpkjx3l-vKtED3WjnbZkiaPyUrisZ7P0cjTNah4UF6lEQ_avIj4Bx9REpHSI-gV3_cVxeiN_70z9xBYkICghjL_hsY5yX0SS94m-GX2nQLZjPw59584KIksNTZ8Sgv4ZQbmNE_3NTy58vEZYjvTtZrsgF-Cks2NgAFY5wUotOIA03V0Mwg7QN0UmYLbWG-kPj_JoL87rIoX3_ObvD-eWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جانشین ستاد کل نیروهای مسلح: موشک‌های ما آسیب‌های جدی به ناوهای آمریکایی و ناوچه‌های همراهشان وارد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690325" target="_blank">📅 12:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه آرمان آتی | ArmanAti</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3HH1_O2XcdYj1uJK9EDON_zb2IumG9vG0VIwb7ZdGQfybrAh3fs-x81OvpnglgfIgXGVrZKiqKY0WWLInqL1lke7GpWhHl5G1HGxJX9yJkccvrlHepRQzCi_ZOKmmySJL8tiMDrkvjHq3rxJaeOA3hd_af0JUgDg-VThJ4E1YXMF1LUhhBeC0bgpuupgTWkmWG_ZLNFua_VD-EbcQBSUu76yXJ3txClQ3V0aOszkjWE_uYSkHF1eI2a0775KtKWB-oQfLQ-Q9iI1gByuD5gNgWtvX-3sgCIX9zJeTq05In1F_00v_bDOgetVCmu6e8gGlxBw653cvrBhSudkon5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏦
بالاترین نرخ سود موثر سالیانه
صندوق‌های تقسیم سودی با "گلبرگ" هم‌اکنون ۳۹
٪
است!
💳
هر ۱۰۰ میلیون تومان سرمایه‌گذاری = ۳۹ میلیون تومان سود
✅
سابقه درخشان – پایبندی به تعهدات سوددهی حتی در تعطیلات
✅
مدیریت حرفه‌ای دارایی – رشد سرمایه در امنیت کامل
✅
واریز سود ماهانه و کاملا منظم
💰
سرمایه گذاری از طریق سایت صندوق با نماد:
◀️
گلبرگ
➡️
🖥
لینک سرمایه‌گذاری و کسب اطلاعات بیشتر
⬇️
🗣
سایت صندوق گلبرگ
⚡️
همچنین جهت دریافت مشاوره رایگان و کسب اطلاعات بیشتر می‌توانید با شماره زیر تماس حاصل فرمایید:
🗣
02157206000
❤️
یک آتیه آرمانی…
📱
@ArmanAti</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/690324" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690323">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc63f399e.mp4?token=Qx1WhnjCg7iTNeBsO25TsLSQ8TZ0WCZnQTvc-edihQnb0L5pH2I9Eivm010m0ZPS9f6mLcwR7ecsde-9eDmEzwgJOSMT5Fe9xCUwEG7xtY4loG6bYkxV9UbLtEx-hl4JKggR6o1nIuujsKFdhoCrWTnfgjv3HQd3blEumVfrBTXZRtBq5sJNkUEkOIvp3-L5ihzd2QMie5qWZ1c9Dt99FGQdBgI4rvwZy978xE8W2DogiTzhwyfeunaY_CERPSWQxXTb8ZEDLXjXU1rIOJGnq5om25If2YdoaVBmKLH9tjwqW654WgPNVhqiIekuxtlWakXXCu6g2s21zm3SfMClbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc63f399e.mp4?token=Qx1WhnjCg7iTNeBsO25TsLSQ8TZ0WCZnQTvc-edihQnb0L5pH2I9Eivm010m0ZPS9f6mLcwR7ecsde-9eDmEzwgJOSMT5Fe9xCUwEG7xtY4loG6bYkxV9UbLtEx-hl4JKggR6o1nIuujsKFdhoCrWTnfgjv3HQd3blEumVfrBTXZRtBq5sJNkUEkOIvp3-L5ihzd2QMie5qWZ1c9Dt99FGQdBgI4rvwZy978xE8W2DogiTzhwyfeunaY_CERPSWQxXTb8ZEDLXjXU1rIOJGnq5om25If2YdoaVBmKLH9tjwqW654WgPNVhqiIekuxtlWakXXCu6g2s21zm3SfMClbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♥️
یک تغییر کوچک، یک همراهی بزرگ
پویش ملی «۲۵ درجه؛ قرار همدلی» با همراهی شما به ثمر نشست؛ با هم نشان دادیم که مسئولیت‌پذیری هرکدام از ما، پایداری برق برای همه است. از همراهی شما صمیمانه سپاسگزاریم.
💚
قرار همدلی ما برقرار می‌ماند...
#پویش_ملی_۲۵_درجه
|
#قرار_همدلی
|
#صنعت_برق_عرصه_تلاش_و_خدمت
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/690323" target="_blank">📅 12:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690321">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سفارت آمریکا در ریاض: به شهروندان خود توصیه می‌کنیم با توجه به احتمال هدف قرار گرفتن منافع ما توسط ایران، در مورد سفر به این کشور تجدید نظر کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690321" target="_blank">📅 12:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690320">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8008a3b3f9.mp4?token=Lu7dWTWGelrLGZM3Xgr5GT7bst3pRn59LohrioUEfvHXE_Ml2-lPwfTIqYweRFB81AkpDoz10dqvnpOHQvB7dqjJGEN5vjHO067CYzuF_jc9oQMc_O45UwJW2Bnd8Vw7wiWcpdy9MhGhXbpekEIXTOeJYbvYSp6qyag45XtIBhUhNTnoy4r3GCydoaz5QgBgMphxRiWFV9CtlrGurLyCjH7gAYwuCDk50xzTIfChLxfAIkjkLzgVEBKnW0FSga69kmCN4SHT_6c578T3v4zfzURsLul2sXxYpnOfnYjnW2-L94fs7_04YQpLmKEl8DCWy84UMVuovuRMcz3DGbsang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8008a3b3f9.mp4?token=Lu7dWTWGelrLGZM3Xgr5GT7bst3pRn59LohrioUEfvHXE_Ml2-lPwfTIqYweRFB81AkpDoz10dqvnpOHQvB7dqjJGEN5vjHO067CYzuF_jc9oQMc_O45UwJW2Bnd8Vw7wiWcpdy9MhGhXbpekEIXTOeJYbvYSp6qyag45XtIBhUhNTnoy4r3GCydoaz5QgBgMphxRiWFV9CtlrGurLyCjH7gAYwuCDk50xzTIfChLxfAIkjkLzgVEBKnW0FSga69kmCN4SHT_6c578T3v4zfzURsLul2sXxYpnOfnYjnW2-L94fs7_04YQpLmKEl8DCWy84UMVuovuRMcz3DGbsang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده‌ای ساده برای جابه‌جایی وسایل سنگین در ساختمان‌های بدون آسانسور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/690320" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690318">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bd069184.mp4?token=VGB7GAh0cY1Kyr6GNM-UZP2NIOy-dYb_l28KrXC3wL_x3xrCPQw1e8Yk-3tYwE-sfrHXCk8KRLWBiWgfGNhulhMf9KE3gFjnNOY3_NdOOg1lZo0zd8ZY8rLDHSyr2SFB1qL4cTgMFyWZs_KPBz-0m2QhfrIROriMO1FYNWLAvCm9NsovqLQRr6YA_bkfEpNEWqE1WblxOq1v3-320ViSvm9RanG1di3chMeBbgOk0T0ng9DLsLYEXQFg8bsOv-qTayNeR6hMyEkPvZPstRTmkGvuJz0vVOSprXqZX0yzc1aaEHi0FpQKJdZwpQZYGfDubzVjUIP0MWZw2eiC2WsDRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bd069184.mp4?token=VGB7GAh0cY1Kyr6GNM-UZP2NIOy-dYb_l28KrXC3wL_x3xrCPQw1e8Yk-3tYwE-sfrHXCk8KRLWBiWgfGNhulhMf9KE3gFjnNOY3_NdOOg1lZo0zd8ZY8rLDHSyr2SFB1qL4cTgMFyWZs_KPBz-0m2QhfrIROriMO1FYNWLAvCm9NsovqLQRr6YA_bkfEpNEWqE1WblxOq1v3-320ViSvm9RanG1di3chMeBbgOk0T0ng9DLsLYEXQFg8bsOv-qTayNeR6hMyEkPvZPstRTmkGvuJz0vVOSprXqZX0yzc1aaEHi0FpQKJdZwpQZYGfDubzVjUIP0MWZw2eiC2WsDRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای یک آهنگ بلوچی برای یک رهگذر بلوچ در شیراز؛ واکنش جالب این رهگذر به اجرای خواننده
🎶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/690318" target="_blank">📅 11:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690317">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W02O_9H2M36hWlNA-j9TD7gHougV2NVwKnhWjwesMuYKYENnT1k2eJnMEq2q1_vJOseQCHLJmckIlRL1TSYuSOTF1pHHuzveO6Lj6Q124yowu_DSWQVi7U8L-Rec7DnjjnUoDdeiLexYxfdyHaXIza3qTcgnpvhTiQL5jktMLBq5kGXapTyJxbU14YCYaXc1BlfYa8ySvihfcBMnrhT2OKnfSp6APqERb8UWTXRN2UlxaTP0b5M8msjCSuo_Bj24bGA7sq5tdAKK8kpr9juGNpOA4aqBpGxXzXULbSqxA8bp06jWUCpBmWRdl8_ukh9m_SNVWZyKyOt2NL0RwzTS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/690317" target="_blank">📅 11:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690316">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9VBZj6aSy9VrEDtkJhsx52A3iCZoMaza8NrhU8hgAJNpYWDcroXlGG0Rqp_hCCaOwSoa2yFEtzuCG_ByrFakWms2ohqIMz0S1EP0pfIbdHzJ5WvVABKYDHHbMl3vQqzjRjbpobURcNtAXUrGEbVOX_RpOjPuG07pyUhSLGuEth1e7P-88JqNFE2KmwiB6ymj7uYrz7-iJjn3hBYbxV9TIGjUlW7fUMo1xfE-GivNIUOpKs4ATkH3NW8_H58O-7vrlLUpTrN-No3VBNZcFcDMoQDAJEkhBx3RgKtOfZOfvZ5W6KymqJha8zZcU8Inazh9jeXp3hb-LNnYw-8VoOrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه‌های رنگی زیبای آلاداغلار، زنجان
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/690316" target="_blank">📅 11:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690314">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال به نقل از مقامات: آمریکا در جریان حمله هفته گذشته ایران به اردن، بین ۶۰ تا ۷۰ موشک پاتریوت، بیش از ۱۲ موشک رهگیر تاد و ۲۰ موشک بالستیک شلیک کرد؛ این تقریباً معادل میزان استفاده واشنگتن طی یک هفته کامل در دوره‌های دیگر جنگ بوده
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/690314" target="_blank">📅 11:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690313">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/690313" target="_blank">📅 11:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690312">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bacb2b39.mp4?token=YvLCb1Y3d3ffIwAjDJNBD2hOjeLcw3Kydhrh2NB0AtIm4tUP6GUJEQbqPSkBhjg-Ba_mvGSalKe847fDOf-jNOZOmt3qvREosk6YHg4kTfT_-BuO2kCw3RLww2htHhbCAXFTtOvt2Fgj6fk2QBsKYVVsgjLXNVADzHbF1tHbNYIqY-6SGEnF6wyCygAcgAendQqnk4osl25Yfh0Y5ILrGhahVwQIXqcYnLyz481YHGG9dQKF_qktwx9M3iA17cfw2kJp2lVbBpkQi2Na8dQHMWq86PxQPSDElV-prg0L9NzIhqIVamXCJMO7xnoBKKvvcWZyIkK4-SM469a93N-Big" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bacb2b39.mp4?token=YvLCb1Y3d3ffIwAjDJNBD2hOjeLcw3Kydhrh2NB0AtIm4tUP6GUJEQbqPSkBhjg-Ba_mvGSalKe847fDOf-jNOZOmt3qvREosk6YHg4kTfT_-BuO2kCw3RLww2htHhbCAXFTtOvt2Fgj6fk2QBsKYVVsgjLXNVADzHbF1tHbNYIqY-6SGEnF6wyCygAcgAendQqnk4osl25Yfh0Y5ILrGhahVwQIXqcYnLyz481YHGG9dQKF_qktwx9M3iA17cfw2kJp2lVbBpkQi2Na8dQHMWq86PxQPSDElV-prg0L9NzIhqIVamXCJMO7xnoBKKvvcWZyIkK4-SM469a93N-Big" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد پلیس بلژیک با زن دست‌بسته
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که در آن یک مأمور پلیس بلژیک هنگام سوار کردن زنی دست‌بسته به ون پلیس، با او برخورد فیزیکی خشن داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/690312" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تحقق آرزوی دیرینه کرجی‌ها/ دیوار زندان رجایی‌شهر تخریب شد
🔹
مهرداد کیانی، شهردار کرج از تخریب دیوار زندان رجایی‌شهر کرج خبر داد و از ادامه مراحل تخریب می‌گوید.
🔹
شهردار کرج می‌افزاید: این زمین وسیع به‌ پارک، فضای سبز، اماکن فرهنگی و... تبدیل می‌شود. این اقدام می‌تواند فضای رفاهی بسیاری ارزشمندی را به شهروندان کرج هدیه بدهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/690310" target="_blank">📅 11:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
طالبان: تحصیل دختران از پایه هفتم به بعد تعلیق شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/690309" target="_blank">📅 10:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جنوب اصفهان/ عملیات انفجار مهمات عمل‌نکرده امروز در محدوده جنوب شهر اصفهان اجرا می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/690305" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a43b876c.mp4?token=km1JMRaYIrfYVMn0oxqkEj4Oebk7oaGsM55KOlbRF9PXiRHLhDBm55adLOiD4Zs-4G6ZNQbH88aZdLZ-VqTPUcx7YCCR3gUukDtXdyH46-T_lyUopfxU9VZG2NYHy5vkMor5Cmd7W5kWtszrLCxFuDn6qBz8N27QYRIkDuy8xFuoeN-pvB1sh2HBHCBxbETGYPEgHYdeAFJyo-0rPNXImV1nI-8m5D94tJXXQo99_GwfnMuZ0ZNYw5ue3fI8JSqPZvSt0UjU23f0JzNUXWhXaFrljwTkwcCWfFh4opyejIsyPtGHuOZA0lJnw9t9j8YdtOlXo2P9fPo-8xm2dJiPL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a43b876c.mp4?token=km1JMRaYIrfYVMn0oxqkEj4Oebk7oaGsM55KOlbRF9PXiRHLhDBm55adLOiD4Zs-4G6ZNQbH88aZdLZ-VqTPUcx7YCCR3gUukDtXdyH46-T_lyUopfxU9VZG2NYHy5vkMor5Cmd7W5kWtszrLCxFuDn6qBz8N27QYRIkDuy8xFuoeN-pvB1sh2HBHCBxbETGYPEgHYdeAFJyo-0rPNXImV1nI-8m5D94tJXXQo99_GwfnMuZ0ZNYw5ue3fI8JSqPZvSt0UjU23f0JzNUXWhXaFrljwTkwcCWfFh4opyejIsyPtGHuOZA0lJnw9t9j8YdtOlXo2P9fPo-8xm2dJiPL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای ساده برای رب خانگی خوش‌رنگ، خوش‌طعم و ماندگار
🥫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/690304" target="_blank">📅 10:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">🌐
سامانه رفاتم بانک رفاه کارگران
🔗
زنجیره تامین مالی تولید
🔹
تقویت روابط پایدار میان تولیدکنندگان و تأمین‌کنندگان با بهره‌گیری از ابزارهای تعهدی در سامانه رفاتم بانک رفاه کارگران
🌍
آدرس سایت:
scf.rb24.ir
✅
مزایا:
🔹
تسهیل و تسریع فرایند مالی سرمایه در گردش بنگاه‌های تولیدی
🔹
تقویت روابط پایدار بین تولیدکننده و تأمین‌کننده
🔹
افزایش شفافیت و نظارت‌پذیری جریان‌های مالی اقتصاد
@refahkhabar
| بانک رفاه‌کارگران</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/690303" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای ونس: خروج آمریکا از معادلات خاورمیانه می‌تواند به بحران جهانی انرژی منجر شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/690302" target="_blank">📅 10:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
گزارش تصویری شبکه CBS از آسیب موشک‌های ایران به پایگاه‌های آمریکا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/690301" target="_blank">📅 10:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465ed155a1.mp4?token=ntVQ376hzOSeUEME6kvGIm4rIoqU2IETKxD97gOe2AiQ-u4Vy01fZsaMU_dkqKg1T_tSnZ6ZvWjjqTrCvTDpMf50RyfixGfogAix9-j_fW9xyNy2ZUs-OlYKkjOOwELhFsjB4PuL9HZld_6Pc7ll-Wt-f4uWfXG_6dy8rqCf15jTPv8S_5p35CN3W8MLL7wbo1PCrNFEQFxPudtQD0kmF5s1Jdcj02A3ujppZ94-YNHWejCAj8MNwIt9NDk6MeSJLlaZRTktsa8Cd45jlZ_n8syU4Sp5l8zhfidH_IrGq6EMzLzNBFt1qmjMUQcOALUei9zum7tHiRPLzcKqe6QUSxUhSsvcdCo8Bd2rMqjSoy_PIAqddhj39bNvFRSDZeRFdiphApAGW-KBivOq83OcO-uNZFBZJdDAhVT7YMFpZ94OrWYUQmGWBat4cfiU0vBcreqRlK2pSOWAObHQDJ-29dpN8oAnTfdHaJHXzNdroegRWQIRHopliUmduY6cpuuGFP3HEmzqlT9wDW4XVVFBIyYzeIC2pt8QTP7KQFI6LCsBzgkjbEfTVw4PBsKSFOhxYHSQ2jbRucruQ2sLwzsLU2askD3pdF4XqRweCCkDXWyEoN_L9uJs9jSFPQvGIg-PmPl3s7E9nDeEOT4RD8Tegg6p8QYHaq78rE1Icf5qfII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465ed155a1.mp4?token=ntVQ376hzOSeUEME6kvGIm4rIoqU2IETKxD97gOe2AiQ-u4Vy01fZsaMU_dkqKg1T_tSnZ6ZvWjjqTrCvTDpMf50RyfixGfogAix9-j_fW9xyNy2ZUs-OlYKkjOOwELhFsjB4PuL9HZld_6Pc7ll-Wt-f4uWfXG_6dy8rqCf15jTPv8S_5p35CN3W8MLL7wbo1PCrNFEQFxPudtQD0kmF5s1Jdcj02A3ujppZ94-YNHWejCAj8MNwIt9NDk6MeSJLlaZRTktsa8Cd45jlZ_n8syU4Sp5l8zhfidH_IrGq6EMzLzNBFt1qmjMUQcOALUei9zum7tHiRPLzcKqe6QUSxUhSsvcdCo8Bd2rMqjSoy_PIAqddhj39bNvFRSDZeRFdiphApAGW-KBivOq83OcO-uNZFBZJdDAhVT7YMFpZ94OrWYUQmGWBat4cfiU0vBcreqRlK2pSOWAObHQDJ-29dpN8oAnTfdHaJHXzNdroegRWQIRHopliUmduY6cpuuGFP3HEmzqlT9wDW4XVVFBIyYzeIC2pt8QTP7KQFI6LCsBzgkjbEfTVw4PBsKSFOhxYHSQ2jbRucruQ2sLwzsLU2askD3pdF4XqRweCCkDXWyEoN_L9uJs9jSFPQvGIg-PmPl3s7E9nDeEOT4RD8Tegg6p8QYHaq78rE1Icf5qfII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ونس: خروج آمریکا از معادلات خاورمیانه می‌تواند به بحران جهانی انرژی منجر شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/690300" target="_blank">📅 10:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نتانیاهو از ترس بازداشت، محل فرود هواپیمایش در نیویورک را تغییر داد
🔹
زهران ممدانی، شهردار نیویورک پیش از این اعلام کرده بود که نتانیاهو را بازداشت خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/690298" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690297">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c7b56713.mp4?token=dkbmz41CbP_59IBqzodokqa5TtQy5x72SgtcKgBx4_O3FL2HKb99oNFIcGV-QoG8PWKKHSewF248ptqS4WwexcMH0hy0MR1I1fl9yTEP6xBRsgYSi38W3mSsiUhTabejumo_DvpCqlvj7CMDThUw_QB89DAUMEgeZt7t0HSy4R5PQT9chIniMUcC4CSYAJsA4taFMEU08aRff_H9b-ZyjuL77dikNHuK5WQF6YbM0koJuVph8sq2gpiSyrd2eKbImkepMk0f3iVhlp9vZEHAqWuLx7EmzKHLL83CEcD_G92YS6BUhm4sj6NmJB2sXS7fQlyImdvVDtd2dTU0EDRToKr2tdUtZroUnQZQdHRmlJBO4kka9TaTbQhLT89HGZaTet-Jzhs0cbR3uiUO-CCApziv2MP3AQddUQZydE39CCHkCeSPmA5IY9jN6TM7Clqidn_8nrTG8GzFJOOzuTQXHjY2oXU47ro2jC_641rTdwqj3I2l5rTevXBwWMRYN3oLiVsNTfzN_e6gOJY90Mmm0fkzQo4GIMRuHBUogVHRpZ8WCC_FmXLRmMuZFzof7g4JW71qrE9T1wszVykAp5skmfpNTRkadSa945a3xdGLOeGm0niWXUVvaAt3JyYU7Up8aLv8yxm9ifV5GkILr3RaZpWYWjAV6VnmfeMSNbnEijc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c7b56713.mp4?token=dkbmz41CbP_59IBqzodokqa5TtQy5x72SgtcKgBx4_O3FL2HKb99oNFIcGV-QoG8PWKKHSewF248ptqS4WwexcMH0hy0MR1I1fl9yTEP6xBRsgYSi38W3mSsiUhTabejumo_DvpCqlvj7CMDThUw_QB89DAUMEgeZt7t0HSy4R5PQT9chIniMUcC4CSYAJsA4taFMEU08aRff_H9b-ZyjuL77dikNHuK5WQF6YbM0koJuVph8sq2gpiSyrd2eKbImkepMk0f3iVhlp9vZEHAqWuLx7EmzKHLL83CEcD_G92YS6BUhm4sj6NmJB2sXS7fQlyImdvVDtd2dTU0EDRToKr2tdUtZroUnQZQdHRmlJBO4kka9TaTbQhLT89HGZaTet-Jzhs0cbR3uiUO-CCApziv2MP3AQddUQZydE39CCHkCeSPmA5IY9jN6TM7Clqidn_8nrTG8GzFJOOzuTQXHjY2oXU47ro2jC_641rTdwqj3I2l5rTevXBwWMRYN3oLiVsNTfzN_e6gOJY90Mmm0fkzQo4GIMRuHBUogVHRpZ8WCC_FmXLRmMuZFzof7g4JW71qrE9T1wszVykAp5skmfpNTRkadSa945a3xdGLOeGm0niWXUVvaAt3JyYU7Up8aLv8yxm9ifV5GkILr3RaZpWYWjAV6VnmfeMSNbnEijc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حالا که داره فصل پرتقال میاد، بیا یک پاستیل خوشمزه و ضدسرماخوردگی درست کنیم
🍊
😋
مواد لازم:
🔹
پرتقال: ۲ عدد
🔹
نارنگی: ۲ عدد
🔹
لیموترش: ۱ عدد
🔹
پودر ژلاتین: ۴ قاشق غذاخوری
🔹
پودر زنجبیل: ۱ قاشق چای‌خوری
🔹
عسل: ۱ قاشق چای‌خوری
🔹
آب: یک‌سوم لیوان #آشپزی
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/690297" target="_blank">📅 10:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690296">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
بازنشر خاطره قاضی‌پور از سالم ماندن بعد از پریدنش از هلیکوپتر به مناسبت سالم ماندن خلبان آمریکایی پس از برخورد با سرعت ۱۶۰ کیلومتر بر ساعت به زمین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/690296" target="_blank">📅 09:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErZX39sBwncgjLxlVqHWp0-Vw4ijqeWuqwpRX_ZFcLca1zsYhj5n4AG3xiV_3C1pQvteKsbSGe78NQxJSqFUnFFGnzigmuTP5XTEI_3SZINKnkwdSwcuQ4dXZ5p2RtKYyS0J-CciufKMMjG-EbxGVrFXvq2xaTuXidY211IVvpQ7__n9S5hnk_WFSFKhR32AWOZXXxk1J1Ze-P36s5rSebxy5PSMn04X-hi-YiVwBGAteDf2Pt7Q50Ai6pCYrXCW0FGt6rvQX2SAl8TgmVse5zreDOZWRaqRmawj1nIeNMM5Xc3Wa84mgR1T5jl4Ddip5_Gi9RB6H_yodVV8WpY_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامانه بارشی جدید از شنبه وارد کشور می‌شود؛ تشدید بارش‌ها در شمال‌غرب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/690293" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e328e93b.mp4?token=Sd3HQAKF65k34ctHNXsORDrDojzvFPGDzOfMnnozoQoIuyjrdrsHZiCfXKE_xB2mREqR1b_QRjX3CZukFbvY0w7BdBIfp7qmBvVwy-95srDaN03eOAhiY4ASrFdH3UfcBs_XQEjIXkLpI0qKDkUx--hsXIDQngdD7UCon8YqUWGxkoSM8xqbSp2vE4_oXZBHJEiTEL8fq0iZtzR2qLvy7qtg6LesM0wN1XABO4w6yIMP_O5RTvHjIj7bqtSejKUGHu8chlTypaUPCL0d-CT0qIX2Vo3LXX8dk0iEYk_hL5xKo6YSYeOZ7x_fra1lcwh1x-mbip8JPCVVqgrgsgf6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e328e93b.mp4?token=Sd3HQAKF65k34ctHNXsORDrDojzvFPGDzOfMnnozoQoIuyjrdrsHZiCfXKE_xB2mREqR1b_QRjX3CZukFbvY0w7BdBIfp7qmBvVwy-95srDaN03eOAhiY4ASrFdH3UfcBs_XQEjIXkLpI0qKDkUx--hsXIDQngdD7UCon8YqUWGxkoSM8xqbSp2vE4_oXZBHJEiTEL8fq0iZtzR2qLvy7qtg6LesM0wN1XABO4w6yIMP_O5RTvHjIj7bqtSejKUGHu8chlTypaUPCL0d-CT0qIX2Vo3LXX8dk0iEYk_hL5xKo6YSYeOZ7x_fra1lcwh1x-mbip8JPCVVqgrgsgf6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازنشر خاطره قاضی‌پور از سالم ماندن بعد از پریدنش از هلیکوپتر به مناسبت سالم ماندن خلبان آمریکایی پس از برخورد با سرعت ۱۶۰ کیلومتر بر ساعت به زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/690291" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqm9bDZsZB95EOjiP9tj0Ykp0wnRmqPsdIyOfsZmy_zY40NeOSI-7y8IIO0PEDoaMOBuPQlffQsz7j8P8_vicQMBcDxMGjeY_KYgYnj73UdU4WkcIswrT2AFvGBvA7tjdPY1CiYEXEeIU114F_e5fYZAYPjs8YR19MIdP2ybS1b1BG3vYjbxa-BlpCl77igA_WAS23jGLmwqGEP7UIdwQs1Ps93JTxJlmTGnnrwBZFawpyPyb5A3Fj5co7_JpW18eNUZzStm9n514FtO_8g50Nx0EJo1Rsp4dcrBsdUmdDmUo5Yw93_VxAchP6aOhxOdWEuxGsFf8SaFAjLdbQtwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای کاربردی اکسل که هم سرعت رو بالا می‌بره و هم کار رو راحت‌تر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/690289" target="_blank">📅 09:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خانواده شهید رئیسی: اخبار مربوط به فوت مادر شهید که در فضای مجازی منتشر شده صحت ندارد
🔹
در این زمینه اقدام قضایی خواهیم کرد تا این خبرسازی‌ها صورت نگیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/690288" target="_blank">📅 09:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تیم ملی بسکتبال با پیروزی مقابل بحرین به جمع چهار تیم برتر بیستمین دوره بازی‌های آسیایی، راه یافت
۷۴
🇮🇷
۲۱ | ۲۲ | ۱۷ | ۱۴
۶۹
🇧🇭
۱۷ | ۱۷ | ۲۲ | ۱۳
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/690287" target="_blank">📅 09:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
دادستان جاسک: از یازدهم هر ماه به مدت ۲۰ روز، سهمیه ۴۰ لیتر از کارت آزاد جایگاه‌ها برای وسایل نقلیه اختصاص می‌یابد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/690286" target="_blank">📅 09:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌ صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌ از دیگری به‌ سراغ او می‌آیند
🔹
رسانه‌های خبری از سرنگونی جنگنده F۱۵ عربستان توسط نیروهای ارتش یمن (انصارالله) خبر دادند
🇮🇷
…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/690285" target="_blank">📅 09:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رشد بی‌سابقه ثروت ترامپ در دوران ریاست جمهوری/ فوربس: بعد از بازگشت او به کاخ سفید ثروتش دو میلیارد و ۷۰۰ میلیون دلار افزایش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/690284" target="_blank">📅 09:05 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
