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
<img src="https://cdn4.telesco.pe/file/eoeNUCF0Uvh3RCp8aQpxbBrAIPMFCLpXN8oZ1WYxw916wnxdxdNUc573-oOesFzKZ4hoQiYb34mm7mYypWOL8e4kap6xSkkqYSIz-GPk3mZ6BlEEd5gd0uERoycWGVe1K5Pai4YkTT38LWR490jXOuorxj0UxVC5-iB6hfFjnYJLPcmwzngT-AMCObtmDYY4gtggwIOWZNwlWHlG8rwH_csz8ZzLAWCVctzkBbEYnf5f2yB-XTyBFQVilG7QilJ15GkqaaZk8Q4b2PxxvEsqHJyQGxWxJLNP72dEOfyhjWtohOD-HAEJqFj-YVMVrVSBgJnCz9iZmyIqi50u90dR5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-693231">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
مهران مدیری دوباره راهی اتاق عمل شد
🔹
مهران مدیری برای دومین بار طی دو ماه گذشته تحت عمل جراحی دیسک کمر قرار گرفت و ادامه تولید آثارش فعلاً متوقف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/693231" target="_blank">📅 20:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3053de3fdc.mp4?token=MQu6EzxyBPvgC-0zZYPx_t1rf4T1rEMlOvsDT2PO98SwAhuW6NUHcpi_PFnJpsh8-noMvIHTOpRsQYW1psU3SMqXgYxpfDaQYKRlgF-iMbSw9MO1ZXpcpgHaiWoJYOnOAcwFPfdd5HDLvp1KN8OoFJnzCTdzTkJbntTkJgN6U94g3qJczgiZJl8a_XjUqhM6ZYAVWh1AwYwm42LjgykAgEy6iDpU8UcPcetdnQBXc0JTLvb2xW5FXA7y12BiU6PI7dOnVAHeFEkbCxPoebtvDE9xZUOc11njQQ4eCDxN54khdE-XQR5sFX9rvmWwRHkt6pBRkafr7MLzE9NbFV0jGBlgpKbOGaI4OIY16jRTlrP6fmQByaPN_x0GFE77_jlilvP_cERdXd4QoitfEJlSwSQCyPV443vdNcvayi39Bv7Sr6S3GOd5x8uR6IhYS8AbuE8E4L6JW0oqa1AyzFNZe4Rz_T-1pceTE1N5yXfkUanftKZWnXHktHG0mWOtocThgliC830oJz0LUc5171FH2DqwrpCrv7HibY9V9URX9mxhZ2x-W6SaRuDTQ6kC1WhOhw_OUCtxXMX_U3c0UVkLJm6yDIWOoVzaJwUz4cAyd-RMoVc-RYJyu1oSizYhJer1AQYKDSGYxR9sNxmDB3ddBu6XQdSQI3y8IBD6dla4B6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3053de3fdc.mp4?token=MQu6EzxyBPvgC-0zZYPx_t1rf4T1rEMlOvsDT2PO98SwAhuW6NUHcpi_PFnJpsh8-noMvIHTOpRsQYW1psU3SMqXgYxpfDaQYKRlgF-iMbSw9MO1ZXpcpgHaiWoJYOnOAcwFPfdd5HDLvp1KN8OoFJnzCTdzTkJbntTkJgN6U94g3qJczgiZJl8a_XjUqhM6ZYAVWh1AwYwm42LjgykAgEy6iDpU8UcPcetdnQBXc0JTLvb2xW5FXA7y12BiU6PI7dOnVAHeFEkbCxPoebtvDE9xZUOc11njQQ4eCDxN54khdE-XQR5sFX9rvmWwRHkt6pBRkafr7MLzE9NbFV0jGBlgpKbOGaI4OIY16jRTlrP6fmQByaPN_x0GFE77_jlilvP_cERdXd4QoitfEJlSwSQCyPV443vdNcvayi39Bv7Sr6S3GOd5x8uR6IhYS8AbuE8E4L6JW0oqa1AyzFNZe4Rz_T-1pceTE1N5yXfkUanftKZWnXHktHG0mWOtocThgliC830oJz0LUc5171FH2DqwrpCrv7HibY9V9URX9mxhZ2x-W6SaRuDTQ6kC1WhOhw_OUCtxXMX_U3c0UVkLJm6yDIWOoVzaJwUz4cAyd-RMoVc-RYJyu1oSizYhJer1AQYKDSGYxR9sNxmDB3ddBu6XQdSQI3y8IBD6dla4B6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن کیایی و پوریا رحیمی سام در سانس‌های ویژه «قبض روح» روی صحنه می‌روند
🔹
بلیت سانس‌های ویژه از طریق فیدیبوآرت در دسترس است.
لینک تهیه بلیت
👇
https://fidb.ir/t8x
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/693229" target="_blank">📅 20:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
معاون وزیر اقتصاد: دلیل جهش آمار واردات خودروهای لوکس، تخلیۀ اضطراری انبارها در شرایط جنگی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/693228" target="_blank">📅 20:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادامه پیشروی یمن به سمت باب المندب
سخنگوی نیروهای مسلح یمن:
🔹
نیروهای یمنی در کمتر از دو هفته با پیشروی در جنوب و مناطق ساحلی، به مناطق مشرف به تنگه باب‌المندب رسیده‌اند و در واکنش به افزایش حملات هوایی عربستان، با حملات موشکی و پهپادی به عمق خاک این کشور پاسخ داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/693227" target="_blank">📅 20:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6693eaba7.mp4?token=EUMTPevU_VG0fPCl1r63F0Btb57Ke2T5kZKyJnigKWEsqCHXyxhJcYLR6Pl7K7dAm8icyQ1Mk5j7k8qAdPFGwCVyJn18QRbwwC-lLUCkKIXctSDHaMM8EWmE6PdgBLIIXMvvdQPyVCEFDNl_etsmlI6-z1IzJBDUY7GWsE8-aaPqYCNQh6rPGU7WWc3E_bMVgct5j4hXpS2IcLldGxs9Wh3-MjdfNf2SPMrvYRhidNv3zCR2T496Wgmxcrrn2q1KlyAuyFZLGw1R44aQSEDT0uHRVf95dPfupF2l4oOIiRV4kUa47drG3hXSpnjp8nSl_i8h5UEi9PHOWqYHnNTqnU3jyfC2tsy7JuNOTWTPjdBXoeEMmdk5AqpMY0ehJckQZnKxoM3X08AKGGFCMyqaASFsM4UH7FZHkV-rhDosAK6FfNX9Oz5ra4YC29_WgiUklX8yyBpnOC__k4sVlfrXy714FQZHx6mTO6U1wfvLcNPcjDTE4wg8qxqtknNA6bWPC8LHXUJBbG4nGjXrEtnH3xsHmG8NjwljgwemTTMpKM601U2fkLYvnFEx6KkHVzoq3yCfmLKT9kFseyW22Rbr05EsQ6TR5XaO8wjePaBKayjpnu8mnzE948K0Q7SSPiJoVErvoW8fneQr4LP26r7Q4g7v3FIGPotVJUT_DhR1dxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6693eaba7.mp4?token=EUMTPevU_VG0fPCl1r63F0Btb57Ke2T5kZKyJnigKWEsqCHXyxhJcYLR6Pl7K7dAm8icyQ1Mk5j7k8qAdPFGwCVyJn18QRbwwC-lLUCkKIXctSDHaMM8EWmE6PdgBLIIXMvvdQPyVCEFDNl_etsmlI6-z1IzJBDUY7GWsE8-aaPqYCNQh6rPGU7WWc3E_bMVgct5j4hXpS2IcLldGxs9Wh3-MjdfNf2SPMrvYRhidNv3zCR2T496Wgmxcrrn2q1KlyAuyFZLGw1R44aQSEDT0uHRVf95dPfupF2l4oOIiRV4kUa47drG3hXSpnjp8nSl_i8h5UEi9PHOWqYHnNTqnU3jyfC2tsy7JuNOTWTPjdBXoeEMmdk5AqpMY0ehJckQZnKxoM3X08AKGGFCMyqaASFsM4UH7FZHkV-rhDosAK6FfNX9Oz5ra4YC29_WgiUklX8yyBpnOC__k4sVlfrXy714FQZHx6mTO6U1wfvLcNPcjDTE4wg8qxqtknNA6bWPC8LHXUJBbG4nGjXrEtnH3xsHmG8NjwljgwemTTMpKM601U2fkLYvnFEx6KkHVzoq3yCfmLKT9kFseyW22Rbr05EsQ6TR5XaO8wjePaBKayjpnu8mnzE948K0Q7SSPiJoVErvoW8fneQr4LP26r7Q4g7v3FIGPotVJUT_DhR1dxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی ربیعی، دستیار رئیس جمهور در امور اجتماعی: بخش بزرگی از مردم می‌گویند هیچ راهی برای اعتراض ندارند / باید سازوکاری ایجاد کنیم که مردم بتوانند اعتراض کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/693226" target="_blank">📅 20:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
صالحی: چین میزبان نشست سه‌جانبه ایران و آمریکا شود
🔹
علی‌اکبر صالحی، وزیر خارجه پیشین ایران، پیشنهاد کرد چین با میانجی‌گری و تضمین اجرای توافق احتمالی، میزبان نشست سه‌جانبه ایران، آمریکا و چین باشد.
🔹
او تأکید کرد با وجود از دست رفتن برخی فرصت‌های دیپلماتیک، کانال‌های ارتباطی همچنان از طریق قطر و پاکستان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/693225" target="_blank">📅 20:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhsLHparwxx_cIt4XCh8X5Jx6G2zCIUi4-DvpUB9pUdOGXnyPMl6HSsg_u6YPKlC0YQ-QH4nwbrWCoAxf63ImaZglWp5beiYjVNEY1GKrQkj9eLmpmdCKkNRF7rINCRVUa_gUNcFW28dePturWrL0xH74hWwqcKVNPNsXqz0jWOV-TfPUs8ymrFM4P7vxSbd5lzM4Djlgd1LoNsxYYenlc-rKMey5SZ513EulpGNz0FC7OyuqJ4mE72ukSJ9neoJRV8BNdY-qP9t8O0ttEQQDl12MSRanjd_fskvTAuRs4WCUfXw9QDKbRR4hXASZuf0u0jteelKR7FJtY614vpuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلی: ۹۶۵ کیلوگرم طلای کاربران موجود است؛ تسویه و تحویل ادامه دارد
🔹
میلی در بیانیه‌ای درباره تأخیر در بخشی از تسویه‌ها، ضمن عذرخواهی از کاربران اعلام کرد معادل ۹۶۵ کیلوگرم طلای مربوط به تعهدات آنان به‌صورت فیزیکی در خزانه‌های امن و بانکی نگهداری می‌شود.
🔹
به گفته میلی، محدودیت دسترسی به بخشی از این طلا، از جمله در بانک کارگشایی، روند برخی تسویه‌ها را کند کرده است.
🔹
این شرکت همچنین از انجام بیش از ۷ هزار میلیارد تومان تسویه ریالی و تحویل فیزیکی بیش از ۳۶ کیلوگرم طلا در ۳۰ روز گذشته خبر داد و اعلام کرد پیگیری‌ها برای رفع محدودیت و انجام کامل تعهدات ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/693223" target="_blank">📅 20:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">19-1 Ane Manaee (1404-02-06)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/693222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه نوزدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
توصیف منافقان و بیماردلان با ظاهر مؤمنانه و ایمان مستودع، در سوره مبارکه محمد [01:46]
🔹
چهره غلط‌‌انداز حق و باطل در فتنه‌های آخرالزمان؛ خطر سقوط برخی مؤمنان و فرصت عروج برخی کافران! [07:50]
🔹
وقوف به عجز و کاستی خویش، اولین و بزرگ‌ترین گام است در مسیر خود سازی و اصلاح نفس [17:45]
🔹
موضع‌گیری جریان‌های مختلف با فرمایشات رهبری در لباس تبعیّت از حق؛ مصداق "زُیِّنَ له سوءُ عمله" [22:08]
🔹
مَثَل فتنه‌های بزرگ و ایمان‌های ظاهری، مَثَل چوب است و لجن های ته حوض! و تکانه‌هایی‌ که باطن ما را بیرون می‌ریزند [26:50]
🔹
امتحان ولایت پذیری، سیلی خوردن از ولیّ خدا و ماندن پای اوست! نه صرفا ناسزا شنیدن از دشمن [31:13]
🔹
دایره امتحانات اهل حق؛ از شیرین بودن طعن و آزار فسّاق! تا شنیدنی بودن اذّیت مؤمنان! [34:43]
🔹
آیت‌الله مصباح و مخالفت با هر نوع مصلحت‌سنجی، بی هیچ رودربایستی! مردی که «از خدا کوتاه نمی‌آمد.» [37:56]
🔹
دین؛ ابزاریست برای توجیه نفس، یا تدیّنی برای تبعیت از حق؟! [42:30]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/693222" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
محکومیت ترور رهبر شهید انقلاب از سوی لاوروف
🔹
وزیرخارجه روسیه در سخنرانی در مجمع عمومی سازمان ملل در نیویورک ترور رهبر عالی‌قدر و نمایندگان دولت ایران را نمایش غیرقابل‌قبول از دیکتاتوری و زور خواند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/693221" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bdbcc32d.mp4?token=TMGmIEzl4krRWzjr6cjQhbZ8InSyApQisLye792RkE8RDdcDUUCGPvC_2F_lWzO-JzSIOsivAVMsczW2blaXvBVdUgp0mMTclOsxcepL31gIxwmd74vKsQL32EVowf6gr0CwhRrfaVMgrqxtEdAiZ_Td1rQUP6m-I6Z9HVuIqsDFCL5Hb3roVzUgFqRocOT1R1grgz18Lo1hC8jv19_vffUiPt1rQFi7mOX2zu4PlSPc9YQmdMt4kLiW-tcUpXdqiMuyQVMRKfDxli_MV_O2iQ1SOh1YbJUNwxuKOS4PcgCvC8in9ceNvln9ZrplJhYcA8CXCJY_NlJ7SBA1vVHztA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bdbcc32d.mp4?token=TMGmIEzl4krRWzjr6cjQhbZ8InSyApQisLye792RkE8RDdcDUUCGPvC_2F_lWzO-JzSIOsivAVMsczW2blaXvBVdUgp0mMTclOsxcepL31gIxwmd74vKsQL32EVowf6gr0CwhRrfaVMgrqxtEdAiZ_Td1rQUP6m-I6Z9HVuIqsDFCL5Hb3roVzUgFqRocOT1R1grgz18Lo1hC8jv19_vffUiPt1rQFi7mOX2zu4PlSPc9YQmdMt4kLiW-tcUpXdqiMuyQVMRKfDxli_MV_O2iQ1SOh1YbJUNwxuKOS4PcgCvC8in9ceNvln9ZrplJhYcA8CXCJY_NlJ7SBA1vVHztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از دانشگاه آزاد تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/693220" target="_blank">📅 19:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e51551b9b.mp4?token=m7BPyGm-EHLCWUecdmg6_7sDBkV6zi5Vc5HwpmQNESuTeCoVblLb6SG4-bjZArTU3dSV215Nw3vU9w-7OzYqGYFwtf40g_W8vHwZl6cFhEDRmrWnY5laWA5h-cjD8MnQAwSkvBB7jm_rF8bI0z3vKn6Q7-yxg64vVUyqdZcS1VvtX-Eq1gRq0utv4QDIkJ8hSzBuYT5Pw_P0M5J0OIrg-8K8laA8V2BulXxb1bw1wixRl2lwMN6idfvAH1O-A9LwcBWY8Ho7kKIp03syYqVsIFdLwh7vnybjUklAuHndo9AuFCgH5tiXfqQPYXQ7fxeaKqoG_da-jdFWSVL7WmUqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e51551b9b.mp4?token=m7BPyGm-EHLCWUecdmg6_7sDBkV6zi5Vc5HwpmQNESuTeCoVblLb6SG4-bjZArTU3dSV215Nw3vU9w-7OzYqGYFwtf40g_W8vHwZl6cFhEDRmrWnY5laWA5h-cjD8MnQAwSkvBB7jm_rF8bI0z3vKn6Q7-yxg64vVUyqdZcS1VvtX-Eq1gRq0utv4QDIkJ8hSzBuYT5Pw_P0M5J0OIrg-8K8laA8V2BulXxb1bw1wixRl2lwMN6idfvAH1O-A9LwcBWY8Ho7kKIp03syYqVsIFdLwh7vnybjUklAuHndo9AuFCgH5tiXfqQPYXQ7fxeaKqoG_da-jdFWSVL7WmUqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محکومیت ترور رهبر شهید انقلاب از سوی لاوروف
🔹
وزیرخارجه روسیه در سخنرانی در مجمع عمومی سازمان ملل در نیویورک ترور رهبر عالی‌قدر و نمایندگان دولت ایران را نمایش غیرقابل‌قبول از دیکتاتوری و زور خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/693219" target="_blank">📅 19:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: مقامات وزارت خزانه‌داری آمریکا با نمایندگانی از بیش از ۵۰ کشور دیدار کرده‌اند تا تحریم‌ها علیه ایران به‌خصوص در حوزه هوانوردی را افزایش دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/693218" target="_blank">📅 19:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3137cf5f.mp4?token=XhLWEpw0t2tUk-66YtOMej-rE5XlePMIO1OXYeJzUs3X64JA4zBFhklYcS2xgR0Y3otBkbg3pLzywgI5dVntrALVhzyPwtnomT947eNHzDe5lzoyKH8R9B8m5uiNZNdBWAwTNR96XG6hB1-9bPV5k5k4YPMUXV5GNrw2x7mQBAbtkR8AaYKKrSg22hTPqRQFAwdL6HT4AKAZa4bH5Y_CYlAjvn2q97ALOSX61sFiijn3S3SCwmBJjm6ILOkdEFTDr6-tMen9-ypLYyeDY00ojr5gLsuoov5vl-Cte4IoXii0QSged8YVqB-GfjH-Bz-hCo3qB2zuD_nNS333b76K8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3137cf5f.mp4?token=XhLWEpw0t2tUk-66YtOMej-rE5XlePMIO1OXYeJzUs3X64JA4zBFhklYcS2xgR0Y3otBkbg3pLzywgI5dVntrALVhzyPwtnomT947eNHzDe5lzoyKH8R9B8m5uiNZNdBWAwTNR96XG6hB1-9bPV5k5k4YPMUXV5GNrw2x7mQBAbtkR8AaYKKrSg22hTPqRQFAwdL6HT4AKAZa4bH5Y_CYlAjvn2q97ALOSX61sFiijn3S3SCwmBJjm6ILOkdEFTDr6-tMen9-ypLYyeDY00ojr5gLsuoov5vl-Cte4IoXii0QSged8YVqB-GfjH-Bz-hCo3qB2zuD_nNS333b76K8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده تعلیق پروازهای ایران به نجف   یک منبع عراقی:
🔹
نخست‌وزیر عراق دستور تعلیق پروازهای ایرانی را به وزارت حمل‌ونقل این کشور داده تا این تصمیم به فرودگاه نجف ابلاغ شود؛ با این حال، تصمیم‌گیری درباره پروازهای فرودگاهی در اختیار سازمان هواپیمایی و وزارت…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/693217" target="_blank">📅 19:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سی‌بی‌اس به نقل از یک منبع آگاه مدعی شد: مذاکرات آمریکا و ایران با وجود رد پیشنهاد توسط ترامپ، هفته آینده برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/693216" target="_blank">📅 19:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21de8c005.mp4?token=jKJmlUkVjS4GBzWr902Kbf7W_wR_IdYzCMn-J7-0k5uLHL-ms8jmVlDJQ2sX27_GeNuimYIXYOxj8K_-3DWt05ie1NANbzDRqfNtn9_jZlJdPk1Dm9uEeb3umAAVFwFP7Uy7euXb7B8HPfzwaVMzCQWktGiPA4OIk-oLnSi_FSYJkAEU-GBwmDPbfLTw67KORO94k0rjs4aA_NF_xgag6B1ed_d1Kn12bLppZB099sqSmXc6bjQJQ_1eM8UWMadoud8eY49p_XQB61eHCBauVVTZ-_subKslqK1W6kYBv0UtWG2EY5y0sxoKymL7VQnAHsg10Hq237lS12-KSVwqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21de8c005.mp4?token=jKJmlUkVjS4GBzWr902Kbf7W_wR_IdYzCMn-J7-0k5uLHL-ms8jmVlDJQ2sX27_GeNuimYIXYOxj8K_-3DWt05ie1NANbzDRqfNtn9_jZlJdPk1Dm9uEeb3umAAVFwFP7Uy7euXb7B8HPfzwaVMzCQWktGiPA4OIk-oLnSi_FSYJkAEU-GBwmDPbfLTw67KORO94k0rjs4aA_NF_xgag6B1ed_d1Kn12bLppZB099sqSmXc6bjQJQ_1eM8UWMadoud8eY49p_XQB61eHCBauVVTZ-_subKslqK1W6kYBv0UtWG2EY5y0sxoKymL7VQnAHsg10Hq237lS12-KSVwqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پلیس انسان‌نما به خیابان‌های چین آمد؛ گشت‌زنی T800 در کنار افسران مسلح
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/693215" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsEYoA24CFCscHkUA56ry1kDF-Bqb0nOgknm3hEA4foxKCgxekeBp7AumdWcy4OfmFgI2zji_TfingeFQREHmNPrQl_zXZGZQ8DOopwKXqF-Ear0bkRDIcNvDBNXitXKmoABlqs_8BgRzdF9SD1O0LdwDxB_2-67wb15TNP0o1cOROonUjC7ChEZe_p0OtHRp03DOuAVEvHpyyMWJrULdkezEgvIoCz0SR0NvQvpJ6I14ztCoZW7MvbNQ_e8IwI-mJDunAqjo0tYFSQdSmSUfv08dStg3HbecQ3V5Fqw4iq5tV-ZTCOdr3-xCV0M815IWV-TYwK-IEYkxL5lcdvMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممکن است اسرائیل جنگ جدیدی به راه بیندازد
سیدمحمد مرندی، کارشناس مسائل بین‌الملل:
🔹
به نظر می‌رسد ترامپ تحت فشارنتانیاهو و متحدانش برای تشدید تنش، پیشنهاد ایران را که مبتنی بر تفاهم‌نامه اسلام‌آبادبود، رد کرده است.
🔹
اگر نتانیاهو تصور کند که درانتخابات شکست خواهد خورد، ممکن است برای به تعویق انداختن رأی‌گیری یا ایجاد فضای«همبستگی ملی در شرایط بحرانی» (پدیده «حمایت از پرچم»)، به دنبال جنگ باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693214" target="_blank">📅 19:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
غذاهای فوق‌فرآوری‌شده و افزایش خطر بیماری‌ها
🔹
تحلیل داده‌های نزدیک به ۹ میلیون نفر نشان می‌دهد مصرف مداوم غذاهای فوق‌فرآوری‌شده با افزایش خطر بیماری‌هایی مانند دیابت، بیماری قلبی، چاقی و افسردگی و همچنین مرگ زودهنگام مرتبط است.
🔹
به زبان ساده، هرچه سهم این خوراکی‌ها در رژیم غذایی بیشتر باشد، خطر برخی پیامدهای نامطلوب سلامتی نیز می‌تواند افزایش یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/693213" target="_blank">📅 19:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu48Yk_O1A_Izr2doWg9DDLFuS8Xp00ABKmPcEIl5kPOUzYkCrjD_RA5X98IqxRJ9dTq7dxL0S4kR4TSQ03EnkRXXkOYcjrWsd5T1P3VYM0goOmhMix7E-Q_7wuOLfOwW0GbmVvDFlHIWB6o7K97zwhQL0atdnpzX7WsCbAMBrSs9zfOds2CLmJzG4eEP18YAYu1iibvMjvd98I20ZAh16TiZMxPFZPlthl2gCHTT0LRz0MKlgqjeJ13Ngwvk9QQeVOcXS5SkDYku0n13-T2zbDd_yXHsb3Dkf7I-cJyvWJEx88aFyEOkNIZ37NQN5yxk42ZyQ7prvvNaKO1OORs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نجفی، مشاور محسن رضایی: هرچه جلوتر می‌رویم هزینه توافق برای دو طرف افزایش پیدا می‌کند همانطور که هزینه منازعه وسیع‌تر و شدیدتر می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693212" target="_blank">📅 19:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
چین: از بازگشت آمریکا و ایران به توافق اسلام آباد استقبال می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/693211" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/693210" target="_blank">📅 18:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693209">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmitlysWqDgI4VvZ8pMOuWrhhr68OfyNr9x9hlN_vDavrqUp5OmYeiP-dx11W7HkglmhocpfHfxYLeYIdJTU8-0e3BjnV5gIZ_REj61ZfHG8T6XHYWr_WF-4ufXVbIvx1Q2iaTPshHvPD-PelPIOMABeid6DFk2k55KTJ2tfBY1PozO7WX9WTwdj4-O67lX68vMIsAfqzuVy_jbwKEpUzdbrCaXvik_lvhmukqdv4vyaq8ZEEoHWIGeuzcN4Nh2Mm7H2HFjGAp7zsh77rbwGNASDGo_eLMZwfyqK151KspANF67D4ljOFU80na2JHOui5QYqM5xHrWcGwvmPYTNeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واردات سامسونگ و ال‌جی آزاد شد
سازمان توسعه تجارت ایران در نامه‌ای به گمرک:
🔹
با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/693209" target="_blank">📅 18:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای سفیر عراق در تهران: بغداد برای بازگرداندن پروازهای میان دو کشور به وضعیت عادی، رایزنی‌ها و تماس‌های فشرده‌ای را ادامه می‌دهد و توقف پروازها را موقت و گذرا دانست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/693208" target="_blank">📅 18:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تقاضای مرغ ۵۰ درصد و گوشت قرمز ۶۰ درصد کاهش یافته است
مسعود رسولی، دبیر انجمن صنعت گوشت و مواد پروتئینی کشور در
#گفتگو
با خبرفوری:
🔹
واردات گوشت و مرغ بسیار کم شده و کشتار نیز کاهش قابل توجهی داشته و جوجه‌ریزی نیز نسبت به دوره ارز ترجیحی بسیار کمتر شده است.
🔹
تقاضای بازار برای گوشت مرغ حدود ۵۰ درصد و برای گوشت قرمز حدود ۶۰ درصد نسبت به سال گذشته کاهش پیدا کرده است و مردم دیگر از پروتئین دست شسته‌اند و به سمت کربوهیدرات رفته‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693207" target="_blank">📅 18:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693203">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDvEyDTUu9NCqYmJsuk1P7r9UzaqX25z6jton1EbeMy3H1Z6TvUlFYKabJBfuZtG0UMI61KvpvnK9xDAdXf5SWAbTGp1I-72l2ymd8BmnFwOv2WKq_GAtqXly2xI6ldnPUf0PJA98jTOgbFTqPJQZPUGJTL3L6oWyTJabLFUlrft_J0PYmJyX5wIaGhllMF_vxF8uaxS-y9pxkg6AlwCNY1WBTsf8Jb9MhGN4jKFZgJdJn0sxCKn55Ejz8S8K103UDI4mVjrJcFfXfXKlGOLL2QOb7VuDHB3BnJBGMO4uFKphwlSEGO25KtsfT2Au10-6yMQ92FNIG6xZ1Y92ey8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAwCz0YwNbwXBDdoesz1vGO4d8DS8NYcmWQ2NTN4F4kNzWvXS-d4KyYnsA2DEBZwnBhG1Wgr7PCodff0VKwif8nIZImtxf0O2RHLPXH8zmX38tYFTDKZ1VoisRBogCox7OPiLeEotc_JziQqvBHI8k26YCvtMNCkz1IsBkDqpqUf_a929fRms-cRzY5eTMMKcnT1tua5gdwvtc1PB11zRDnGJPLLl7K8p-721OpT2eyjDc-FHLudXBqJGWIbmGM4xoMUaxOWKQC1rR4Rpa7CkZabMSwQDU6-VlB7_AjsTS90Y3_LTl_TWdymKC3eQLw99nx3X50A9GwvhoajIarmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueglZIg8-GEqajnbleGd-ecKfk4XAAVBfKIouhn_v8KMjf_B6OIkTBaLkcvlLkz0bRU_DniVvAUmKjChWFXhtJogx9gPmqA5C9HgKkp695cFhJMWoxYW_eLucBThI2tg6h6l6XvIpuryViIiZGSSZ88FE9MTTW9XgglLbs_wHfLQmnGrNGQYQcvhm3taYAvd-x_7d2rsRLlJu_TjTe3118Fjz7Mc10L9J5UrkhInTgDvv1OSrk8u_OrZER5Tsgt5_uHaMqH7xaRXCvWUVZHQDAz9VUA_HVneIYdHffkCSrdqjze8LBJdOYVvXBNqh1dNP9S0nYay5IyM-wcSglAcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhcFRV6Ro0uBVJzy6rfVIEC5L0btiwBLAI2alrwJAivWQF-qTGWgpfMgqcvHLTquqwonjBkyo0db6IU0kMgZipZFHhb6GYTJmdMMC9M_7wSr0hmMS8shgBTUgJ5jEyQn0377j0BlORb5vp_UzSedy8hN0zBWtEpehBnLZRHhcTZDyBaaMrsP3ffynhvBKR3yv44kbR6Lc60aoRIxDRO80qA_RKdVUjGTVMmB2ev1yO836OfjXmxzjaCXwvVGP-LMyzIQcQZNKrXnvkfuACrM_Vr3B3liFfebMerMr9TfW2E_KgrV6oks4lX2cSLiVEuhJUgtrOAWlAgfDkur0oAsmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پاییز با این دسرهای خوشمزه یک حال‌ و هوای دیگه داره
😋
🍁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/693203" target="_blank">📅 18:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693201">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای اکسیوس: در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693201" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693200">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اکونومیست: آمریکا پس از ۳۵ سال ناکامی در بازسازی منطقه، در حال عقب‌نشینی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/693200" target="_blank">📅 18:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yv9l-oJANVNY7SGKW1-aAm2jdJzi6zKaPZ6Zb1dK9oHf_NbQjlUMmAioZG4qXNLXMgEkWvD5hk7LEj1u4RqCW6pB-JaokOI2Ry2hXwehTn308tDPhTgxnjC4L0iuZf-xa-uLnbuBes8YfzF7TvKczYS2lL5ZP4TJUm8VLGjb_n0T7L-gGG1dVIiX26Dg3k2-lQu63Yvl1MMTcsOuCFJ-U45xcSF5RfKCLKhrPdtKTrKwoK6RwNqVvXNSo3j_D_txmV2cTy6gvUMtbq_5krD9zlVO1DpU4ptY4kltc0v44L8GNeDhp9s0tOqK9L6joUxTvoRvKfUnEOPOxMn6oaJglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwdDbZ8F4HZctj-Azc8NrTwMNjOcryarDAJ4KczfF5w3SpTJurJ9fy8xYVY1_WarVYVWNyjdxiKDxfgmR0ZJ5h-cZXu-goxOSziRgTwML6O9aYy-BzAX4QZRd-DnnBs0vlrfaqMpn2Q9zyerfZY8lktrUuBAG5RcA-HIhoxF-3eNM-5qM5VTTBmcpXQWd7-fBaRmP0FdSnRFBnEaDXsZ5EBPl0AMWev2BMhxHBvCRbP5uWG2mZyPzhe1tsSmmSxCH8r_QrldHGANZWL8x9yNI5gWH0C5rEq9NHDKmSmG_ihFxNagMtZZOCtRg8h9D0ewP8ASDlIuegose1ZHDTFkbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c7e8903e.mp4?token=chz7IoIBeHO4wvdk6WoI_5QVzinHs8CBLq85uN8gl0a74IujAy6JZ9WSn52m_KQYYwpXuuN7ypnFzrd5S-M1AP45Rzr0d7jXzG41v1fgwYJQCo3E1KpUiDg9JOaWdSAEiccxRgYZWudEI-d2rnx0QwgCt-Cz-9WHaceZzQMMeimvLbkMIad4UHsL1IMrxK5tJry4_gCmc_4BEiz2kdegLluXAGjiYEAblMz7Rw4GhBmZYZK5Nr57jhzxa1z-0jTog2Sq-wb8-ccLM8YTrcC9AUShYb4KlUQVbid5P5r8xv5SR1yn1v6rIzLdAssC8nZiLOJ48qcTnxmw6N1QdtuU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c7e8903e.mp4?token=chz7IoIBeHO4wvdk6WoI_5QVzinHs8CBLq85uN8gl0a74IujAy6JZ9WSn52m_KQYYwpXuuN7ypnFzrd5S-M1AP45Rzr0d7jXzG41v1fgwYJQCo3E1KpUiDg9JOaWdSAEiccxRgYZWudEI-d2rnx0QwgCt-Cz-9WHaceZzQMMeimvLbkMIad4UHsL1IMrxK5tJry4_gCmc_4BEiz2kdegLluXAGjiYEAblMz7Rw4GhBmZYZK5Nr57jhzxa1z-0jTog2Sq-wb8-ccLM8YTrcC9AUShYb4KlUQVbid5P5r8xv5SR1yn1v6rIzLdAssC8nZiLOJ48qcTnxmw6N1QdtuU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبایی‌های جاده چالوس زیر چتر پاییز هزار رنگ
😍
🍁
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/693197" target="_blank">📅 18:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693191">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIUCa_7o4uO9vEiq0GObn0dIzKiWA-wISl-Hh7ywi9tPJaetMgfWL27KS2R3d1fehM1GFdshQqxm-6N-pYMRvbqfKJzn3I43t_pzw_iG5VGOUI5YEBCf-UoyBnz2_uZzPTJo8yScwcEIgJ4PFHvN0n-mml1HnYKyPOqXyz-W-A0ztkccER5M3s5R5DV7Y_k14IsRno5zKalApQFGfxgYn3IKsLPB6bHnskxtwqTGte4Db5nA5GmzygI--8QV_ilmkg_bnuCS3DEAAVlKeTbYbqmNclTvnyNJGhm4J6yQBtpLHzuQSMwTowVU4yrcQV7qd8E1L8_83bb0Lc7dFfz_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilkzDvqBJlzKBcB7atYdhfam7IXb108NbfQDhAlr1pDmqFMpgQexiO8MKNSxm_hYbfEdhQoYupurZHyt3gy7gZ9GC1lZ0f0ejQB0F1HkbS4osJPorxt2C59lVfqyihwx4hD20qQR8-SYTWMOoSc9C8Rx4Vn0LDwVuQ7mHJKFGNVmd6LJCtFlghR3bqKN9FLH-FBGhCOSUWtkxEohImmP9fWokRi8Kbp8oM6_v-qnXJgd5msh1nHX6t9lB0Me1hHZS16tpuWvcrKnVpq3_-xw8EKyVzLN3bzQRNPh9188ByZ9CMLddibyJQfGN3NTk_6WJGxbkaftbjrJf2PyukSArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZBBXpdFTcpLUftAvGtrKW1qjxGRzWQggo7Dax3pAPcp4TsRs65iOFn8FjsBRm5cSzIry-4VhDcr6im7YdiNqvVvc1jqJyudf3Dw_KSFuEPCAgHb3GRGaVBovJDX37Utpy1cWhKD1GnCS8n9SdnIulc0lIVJPlndMKdUFhsG3_Aio3HDriVkcik7X2ETOLDfZhe8QfZbxBvssQJHqeocGGy6WwNEuioQY3bS_7755qPIyA7hbOmF5O_DeI7FiWpgML6z6cV-8-vcDN_821jDCpgs6KUjtfCjWZhpD2vYKqlnezHnJjTdM7dRg5-seNkER9eKzC1Cv6Wjv7Qmf9o19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JItzOKqOtHb4xgb6q7g2QchyQrf156HUNeAZeWduFfLC8_qv0zzp-InSQY4lAajJJN7FWqhnU38ZR0ddmCz-bamd3aTn-cCcw-pWEP6wP1aQIof7psBRUl6P6QZtP0VY8UVDpJKxLkLS6I5xCSuNEV8Fe9OwspfGWIbWX0SwTGX6kXAV-SlXIg33YFpqc3oV0KZ62lQUxLVuQah4bcHWdIbx8wsKWxHG6lTZfSHvbuYM-wd1cOYd47gbqNBBXKgEMiLTEmUCEyXpBFRxQiO5dr-pszxN21f_GweWuJasETQls_Xyw7AP2i6S6wK6GzeYw44qmZ3zybJCPCPMuBUgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYnH4Jcr3B-qguWtzRRSPT6PeCcSdP35BPdElOnGcs1e71Y4hsQpMLsWHiTs4e5YUGPr1yW4AbqZGZ09FkySgxQUSfrXkP8OKC_uAHGuzW5m-7m41aH1Pk_zvvwINvFCAhwonQV2GTufbsJyJt5rfScGT3v8vWNb-uwgOT2Ag1BA1t2J29Eeljbm72ZAtz2brrJn5afzsPUmpsi5A9egQStAmq2ABZQmY-J-Khk-j2JOTXqwcPeb0gHoLjMJqeXhV3il6rZ7QXyH4N6hHCVSeZSq-ELiv26jyxEN4nHkyYAZTJXbuQbo788EPTisiRHA48AMJMg6TdjHxhlDuOemsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6q8p77AEHIjV9EBtqvOzLkFINXSHWjhLp_4kiUGGG_CKz8q10VV8HEAmZaRi3EuE53BwzaITnoWzWtbQHXe5MO3UID3ftZhfCXUDcMEHpE58--6qLSpYBWEKvJKehszYIDIc8BHRxxMCtg1MobUvv6c5Z--clGtUAcX45AKyJ96dZCTUJFYiS9GTclpHoQpz7vlJxAPU_8iqRj53wpLSU9T1VLXErzhY0CNgGze3C3YyzT6Lqh1hgwDg2bRIRf0I_4BSwpFRkuzRSBaRRGs4jY1Kxv2j_sA0Wg8clZGxuAYbzIG0mIqS3Fit3b7MvhrX2Q-PrxXcsDAKnAyDAN63w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی هفته
🔹
این هفته بازارها چه مسیری را در پیش دارند؟
🔹
از بورس و سهام تا طلا، دلار و دیگر بازارهای سرمایه‌ای؛ کارشناسان، روند بازارها را بررسی کرده‌ و از چشم‌انداز روزهای پیش‌رو می‌گویند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/693191" target="_blank">📅 17:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693190">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42553cf21.mp4?token=UkQBtsarBEctHtCgihBA41mU5w2Oi3eUWrMNn308ziGZ4kp8DuKq9KUPDpSBy7UxNAPnYTr9mpJthRmy9xObYHw-OBOLno7q4BHzxHey_EAfc_wDT5nvh7tcRRFPEIJ_pwL3_XxK-cYhlqUGIT3hfjgPdDimweJHkOqYfuLv7Xy8Jy_iR0sl6NdbWZ6H7654J6imSWSNyI3FDHHDYSkwNRpnYNXChXiVAzCK5mLtN8pVT0YRnvVXRvRcxJR9knwCeNwyseb3OFcztZfLym_qVcsdC4tfImcvCIuFYukJY1OjjH9qGVTtGBbo4ZHh9Za8HKHVdv-PAFozZo2iHwiO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42553cf21.mp4?token=UkQBtsarBEctHtCgihBA41mU5w2Oi3eUWrMNn308ziGZ4kp8DuKq9KUPDpSBy7UxNAPnYTr9mpJthRmy9xObYHw-OBOLno7q4BHzxHey_EAfc_wDT5nvh7tcRRFPEIJ_pwL3_XxK-cYhlqUGIT3hfjgPdDimweJHkOqYfuLv7Xy8Jy_iR0sl6NdbWZ6H7654J6imSWSNyI3FDHHDYSkwNRpnYNXChXiVAzCK5mLtN8pVT0YRnvVXRvRcxJR9knwCeNwyseb3OFcztZfLym_qVcsdC4tfImcvCIuFYukJY1OjjH9qGVTtGBbo4ZHh9Za8HKHVdv-PAFozZo2iHwiO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هاوئین؛ بلور آبیِ فوق‌العاده کمیابی که درخشش آن خیره‌کننده است
🤩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/693190" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693189">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ: ایران با بستن تنگه هرمز به دردسر بزرگی افتاده است/ ما بزرگترین محاصره تاریخ را بر آنها تحمیل کردیم
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693189" target="_blank">📅 17:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693188">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای
مضحک
ترامپ: مقادیر عظیمی نفت از تنگه هرمز عبور می‌کند و دیشب ۲۹ کشتی از آن عبور کردند/ ایران می‌خواهد تنگه فورا باز شود چرا که خسارات زیادی متحمل شده
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693188" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693187">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ترامپ: ایران می‌خواهد توافق کند، من هم دوست دارم توافق کنم اما این پیشنهاد غیرقابل قبول است
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693187" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/693185" target="_blank">📅 17:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع آمریکایی: ترامپ به تیم مذاکره‌کننده ابلاغ کرده است که بدون اقدام اولیه از سوی ایران، هیچ توافقی در کار نخواهد بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/693183" target="_blank">📅 17:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693181">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d54893051.mp4?token=HggAjoNmGRR8LoHf9YxlrnhxlaHVYnsEN2wxcGwbYs2hW30f4n1S3zbj8M0dwS0Rx-8khSlsvKZegeR9XrZEidoy6kTvWqoPSLQf0Cr_gnxKzHOnb6YqQKizX7JoxNqnMoIpLvtn0AkAi7JwCRmRAZocGy6hFXfd3MIobaD0BzOUaXZzECZy9AF3WXJa1ctgzFw5wKDs5XisDn2obhHgTVBsJrSsthWpFLyH3McpflNP011kTZOemoILnLrE9QApRALjDdM8a7CP-3rqJBO3jNnbHjA-6UiW8Rt9_3Cs7KlCjcxH-d51zxm4agigCSUUtWdGdA9I6frdxQp0kAGYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d54893051.mp4?token=HggAjoNmGRR8LoHf9YxlrnhxlaHVYnsEN2wxcGwbYs2hW30f4n1S3zbj8M0dwS0Rx-8khSlsvKZegeR9XrZEidoy6kTvWqoPSLQf0Cr_gnxKzHOnb6YqQKizX7JoxNqnMoIpLvtn0AkAi7JwCRmRAZocGy6hFXfd3MIobaD0BzOUaXZzECZy9AF3WXJa1ctgzFw5wKDs5XisDn2obhHgTVBsJrSsthWpFLyH3McpflNP011kTZOemoILnLrE9QApRALjDdM8a7CP-3rqJBO3jNnbHjA-6UiW8Rt9_3Cs7KlCjcxH-d51zxm4agigCSUUtWdGdA9I6frdxQp0kAGYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض عراقی‌ها به توقف پروازهای ایران بالا گرفت
🔹
«پروازهای ایران را برگردانید.» این مطالبه حالا از بصره تا سلیمانیه شنیده می‌شود. توقف پروازهای ایران به عراق با اعتراض‌هایی در میان مردم، علما، نمایندگان مجلس و چهره‌های سیاسی عراقی همراه شده است؛ تا جایی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/693181" target="_blank">📅 17:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693180">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سردار شکارچی، سخنگوی ارشد نیروهای مسلح: اگر آمریکا و رژیم صهیونیستی مجددا دچار خطای محاسباتی شوند، ضربات ما این‌بار سنگین‌تر، وسیع‌تر و دقیق‌تر از قبل خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/693180" target="_blank">📅 17:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693179">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: کشورهای محدودکننده پروازهای ایران متقابلاً متضرر می‌شوند
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا تاکنون از روش‌های مختلف برای اعمال فشار بر ایران استفاده کرده و محدودیت پروازهای ایرانی نیز در ادامه همین اقدامات است و با این حال این فشارها نتیجه مدنظر آن‌ها را نخواهد داشت.
🔹
اگر امکان برقراری پل هوایی با ایران از بین برود، کشورهایی که در این محدودیت‌ها همراهی می‌کنند نیز از کاهش رفت‌وآمد و تبعات اقتصادی و گردشگری آن متضرر خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693179" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693178">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رئیس جمهور: ساختار رهبری در حقیقت سیاست‌گذاری است؛ اجرا بر عهده ماست و قانون‌گذاری هم بر عهده قوه قانون‌گذار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/693178" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693177">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfb3b9c81.mp4?token=B8XSGuBDsj8cCNczT0MO-prCARN7txQHDVRi7szSt8FTnu9P3mWX5sGq8chyaAIEaMc2Y8q08bimH7yvC3PngJ-4JaaXwKNFDxGOzPpjvnHeCtWO9EIIIoAWdzVl4Kqy1EPdchMZtaXS2zlrgho5nzgrAtE_lyjHdT8K6-0bQCl5dCwJ7mkkrkhGjbnhBmJ6Qb9va4dD3_J1x5uLwc7YeVXByBuOxGRsRwnFPgXsICCbkAntb9my-3IlmaEe8wSemlFKRJLfNsEVF96cgEuvgMHt26zEYTrwmaWEkU1XgSQ3T-IMqDBwjIPuK7WCL8Ji8jgA4wzg-IYk0Z_gwOIuRCnbYEkS-5sUoFt4LZl8bSVKJC8BS-_9iL9CqD1oquUHSt-VAm8XX8v5k9lvrzdwCcGLiIbYJBD8n5t0Y3xkaMiPN2yGllfk_rXgYk--J3M7LsTD1QG8dvqQPkny57jCs-3lzHLoU7fiuTMBf4PuoY2oRAMWBjfhrbG3xKf5BSbpAbbMN59PsGKDG05aPq4tqrz21gaazsoHHvXlssiGHjxyn9anreiV0DFmc4NsQzQhSjgTRM5_g5RoKosOnuSa1lHz52i2XjAhvFKQ6ASlg72uSb1aREbBcgwnu6Z6k6-PTNEsaf97fxJoTaNP6mVEZDJxhpH1fYexF5PeisJrFDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfb3b9c81.mp4?token=B8XSGuBDsj8cCNczT0MO-prCARN7txQHDVRi7szSt8FTnu9P3mWX5sGq8chyaAIEaMc2Y8q08bimH7yvC3PngJ-4JaaXwKNFDxGOzPpjvnHeCtWO9EIIIoAWdzVl4Kqy1EPdchMZtaXS2zlrgho5nzgrAtE_lyjHdT8K6-0bQCl5dCwJ7mkkrkhGjbnhBmJ6Qb9va4dD3_J1x5uLwc7YeVXByBuOxGRsRwnFPgXsICCbkAntb9my-3IlmaEe8wSemlFKRJLfNsEVF96cgEuvgMHt26zEYTrwmaWEkU1XgSQ3T-IMqDBwjIPuK7WCL8Ji8jgA4wzg-IYk0Z_gwOIuRCnbYEkS-5sUoFt4LZl8bSVKJC8BS-_9iL9CqD1oquUHSt-VAm8XX8v5k9lvrzdwCcGLiIbYJBD8n5t0Y3xkaMiPN2yGllfk_rXgYk--J3M7LsTD1QG8dvqQPkny57jCs-3lzHLoU7fiuTMBf4PuoY2oRAMWBjfhrbG3xKf5BSbpAbbMN59PsGKDG05aPq4tqrz21gaazsoHHvXlssiGHjxyn9anreiV0DFmc4NsQzQhSjgTRM5_g5RoKosOnuSa1lHz52i2XjAhvFKQ6ASlg72uSb1aREbBcgwnu6Z6k6-PTNEsaf97fxJoTaNP6mVEZDJxhpH1fYexF5PeisJrFDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت سیده سارا دستوم:
ضدانقلاب القا کرد که زنان بی‌حجاب، لزوما ضدانقلاب هستند؛ اما شکست خوردند؛ من اگر برگردم باز هم از انقلاب اسلامی حمایت می‌کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693177" target="_blank">📅 16:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693176">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38f22edfd.mp4?token=PKY6t8HMPrg_Fy00igwMj_RojSRmN34FMQShZL2GEoizdkDp6UMatWHJE31JilWc_G7Md8S_BuuRshAUV7_YRLOnVBwq0kCdvsufF0ssmZMzgE7NpdFO6GLXmZrLc35By0YzfxZrk2Q0z4r7F9cJnli4PTa48kaU2Vkjmy_J0wA1kYOLMW7zkvZ5VJGjGqgJP73UlWAZW5Y_w_8d6fsOXxOCdLt0zObI_HeI7CxyzDMnmCzfAOuy4U7AyxangBzssw2y740BAEg_YuEwVBZsmBh8vdW5jqb4ij3D83CBuwsxAiiLVyo06Fq-dYHODNjf5bhawLZeEjkNAnRUNVXWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38f22edfd.mp4?token=PKY6t8HMPrg_Fy00igwMj_RojSRmN34FMQShZL2GEoizdkDp6UMatWHJE31JilWc_G7Md8S_BuuRshAUV7_YRLOnVBwq0kCdvsufF0ssmZMzgE7NpdFO6GLXmZrLc35By0YzfxZrk2Q0z4r7F9cJnli4PTa48kaU2Vkjmy_J0wA1kYOLMW7zkvZ5VJGjGqgJP73UlWAZW5Y_w_8d6fsOXxOCdLt0zObI_HeI7CxyzDMnmCzfAOuy4U7AyxangBzssw2y740BAEg_YuEwVBZsmBh8vdW5jqb4ij3D83CBuwsxAiiLVyo06Fq-dYHODNjf5bhawLZeEjkNAnRUNVXWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض دانشجویان دانشگاه رازی کرمانشاه به غذای سلف این دانشگاه و تاخیر چند ساعته در تحویل آن
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/693176" target="_blank">📅 16:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693175">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONw6WFJiaqvs4-so_fNkP1Jn_nhuGdQHT2MCDvopLwQwRwZRyxkSa-O276YRmDaZ8B6YDN67TbTpc2dH-9fqyMSbEjp2HJZalx2sQsTJXXbTKG-ExmWWzZL-FoIf_6GdOf1h1mmOiC0seH-DviLnVI66rdlgwToiIbWQwt06xgRawtHHMhQcHetXWsFFtMWd-Hd0y6e70-DBMi_zYmCpo254ns3yKaifRH1xq9peB_YsWBgoDDYbz165-XqHbhQJdAtbRuNHziRjcyb9rD3TamwgY4PlDKcqH2_HecnmavHK8GD4KfLhpYILn80mqeWlg4S52g56JOFjfsE0mL3J3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا با بیش از ۵۰ کشور تماس گرفته تا تحریم‌ها علیه ایران را تشدید کنند
🔹
آمریکا به انها گفته یا با ما هستید یا علیه ما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693175" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693174">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تصاویر جدید از حملات با پهپادهای انتحاری به تجمع‌ها و تجهیزات متعلق به دشمن سعودی در چندین جبهه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693174" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693173">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
انیمیشن لگویی هیولایی که بر پایه دهه‌ها غارت جهان ساخته شده؛ اکنون به وحشیانه‌ترین حالت خود رسیده و به پایانش نزدیک می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693173" target="_blank">📅 16:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
یک منبع آگاه: عباس عراقچی وزیر خارجه ایران و هیات مذاکره‌کننده همراه او احتمالا تا روز چهارشنبه در نیویورک می‌مانند
🔹
پیش از این برخی منابع خبر داده بودند که پس از نخستین دیدار میان عراقچی و استیو ویتکاف نمایندگان آمریکا، کارشناسان فنی از ایران به مذاکرات…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693171" target="_blank">📅 16:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اعتراض عراقی‌ها به توقف پروازهای ایران بالا گرفت
🔹
«پروازهای ایران را برگردانید.» این مطالبه حالا از بصره تا سلیمانیه شنیده می‌شود. توقف پروازهای ایران به عراق با اعتراض‌هایی در میان مردم، علما، نمایندگان مجلس و چهره‌های سیاسی عراقی همراه شده است؛ تا جایی که برخی هم برای برگزاری تجمع در بصره و نجف فراخوان داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693170" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoVqP0TgqQ2MYe-WnzINzlizoLVVJi0veZZ-fqfUNQzY9h6w6a2D6MW-uJFE5Fa0ymPoEvxhHz15ixoaDCAZoGoxK8hG-wJBuQoqI-Xry9NgrQ-9M_Rp6ZaL74455aM7UvD-B5AJQkX4n68h52avRZzZUvV7Hjc50-6Bbd-fuPfs1Zl8Y0VypXXWsZTeQHgl1xKS8araIaw3yEEc25ujN_vjCJAmmx8Oy9AIj-RrWjIf7QXW6p2l2_UAACr8jBUYZv4ajn6oRWeYIR3Pb6fUNi83ciYc_HAYJ79Sll08zt-t4WZlzohCf0-cxdIgUW_N2dfebRtX6_clo4gPzmAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت تیتر اکونومیست
🔹
قبل جنگ با اشاره به ایران:
ایران چگونه پایان میپذیرد؟
🔹
اکنون بعد از جنگ:
آمریکا کی از منطقه میره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693169" target="_blank">📅 16:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سعید آجرلو، عضو کمیته رسانه‌ای تیم مذاکره‌کننده: آمریکایی‌ها در ابتدا پیشنهادی برای توافق ۳ روزه روی میز گذاشتند که محتوای آن عمدتا از جنس اسلام‌آباد بود
🔹
اکنون ما آن پیشنهاد را اصلاح کردیم و شروط خود را به آن اضافه کردیم این جمع‌بندی در کمیته مذاکرات در شعام انجام شده؛
در پیشنهاد ایران، از موضوع لبنان تا پایان جنگ، معافیت نفتی و لغو تحریم‌های جدید و محاصره وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693168" target="_blank">📅 16:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJTo68GzHPsuXLmmU0CAr1TzWWkq2rmRRddnojfr7G0ga48IjhSOOY1Go30LR9COHv3owqwPz5zbGnfEekejnUY1cAvle45n0DqOEQg_Ot-6o-9NuJL0YvFYBpJI2yNMF4ozVKa7Rz3clw6AdQrj0w2-uKJYic26Jr5wn_UjMRTlWfz7ek90qBh5bkec8anDLP-dedQvQfrLR6SZ2iEVfZptWF3C0N9PPrsNiTzG7UBIDd080v4AJT-ZSJvm3Dw_ASj4bglOkyL3gvCQibcvZdOU839PTt8kAePtKrWUTn9d9X0qgGqUA-3NoX6uIi7aEL7v75B6KhOvzVpPOjBs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه دبیرخانه شورای عالی امنیت ملی درباره برخی اخبار خلاف واقع در‌ موضوع حمل و نقل هوایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/693167" target="_blank">📅 16:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
باج دادن به آمریکا هم جواب نداد؛ دلارهای عراق نرسید
منبع آگاه در بغداد:
🔹
آمریکا با وجود همراهی دولت عراق با تحریم هوایی ایران، از ارسال ماهانه دلارهای نقدی عراق خودداری کرده است؛ این اقدام به افزایش قیمت ارز در عراق منجر شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693166" target="_blank">📅 16:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160941dea.mp4?token=kHZvI6yxDrdPMc-BcQZe4Hbmd-F-UYN6zAj0LiI6j_Iq-uOC-uX4I6fJ-huveQSEgzpLIabeD6zMWG-2VmBmNAfs3wCFuvLU7K2Y114TM95TnH3RXOhIuVDa9rHHAmGSbcL2wNcW948GE-y6oP7XITeXjzI_epyD9FjKSNXfUHKbBDB_rDgOay3t6D9z7kow3OEUkPu9NP8U0-UzthlUc3RtppX4RA51ua4RIOGprj0cWdgAehjMw6PFcryux0Q22eg2BD6CVJCNAH8F3zqZQwUJgAWAWtWoZkytNr4YQ2_nWNzQQARfvrQRvwgCYpfAPllTuGLQqRZYJ-Up_HZAyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160941dea.mp4?token=kHZvI6yxDrdPMc-BcQZe4Hbmd-F-UYN6zAj0LiI6j_Iq-uOC-uX4I6fJ-huveQSEgzpLIabeD6zMWG-2VmBmNAfs3wCFuvLU7K2Y114TM95TnH3RXOhIuVDa9rHHAmGSbcL2wNcW948GE-y6oP7XITeXjzI_epyD9FjKSNXfUHKbBDB_rDgOay3t6D9z7kow3OEUkPu9NP8U0-UzthlUc3RtppX4RA51ua4RIOGprj0cWdgAehjMw6PFcryux0Q22eg2BD6CVJCNAH8F3zqZQwUJgAWAWtWoZkytNr4YQ2_nWNzQQARfvrQRvwgCYpfAPllTuGLQqRZYJ-Up_HZAyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به روياهات فكر كن!
اولين قرعه كشى روزانه جوايز ديما؛ فردا يكشنبه
🎁
جشنواره جوايز ديما(شعبه ديجيتال بانك ملت) از ٥ مهرماه شروع مى شود.
💎
۲ جايزه ٥ ميليارد تومانى در قرعه كشى نهايى
🛵
١٢ دستگاه موتورسيكلت در قرعه كشى هفتگى
📣
و هزاران جايزه نقدى روزانه به مدت ٤٥ روز
mellat.ir/dimadream</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693165" target="_blank">📅 16:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxZEI17BnpkWPHItxoc-sqXEHlglJ1n0HuWAA-VJRDm23cgQdOhjXS_oCQjxfZUNXVeJTFxAflYc914CEGTQg6i-Z_3r1QJAVIKLRLrPSk5wvr6GuI7GNnqx--tsXVkQo3unM5UG7pXVR1bucrZYM6tA0GLngFy35LpLpeEQBKuJwQ-xQ9RcswEVmxaIxlY5pyBx8yqUabrhBKegxK2hI7IHCGPXtDo0rC6aOg7KBMEca1-i90-zdRhexFfZT4XecYxo4LPkgh7orsEaaAZqtEQms-oYnYOGfc2-v4-ViIqlOyc6PVBRK86pOq0ln2kRnG0S3oKqCL61-4u8ENPm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گذار ناگزیر از بانکداری محافظه‌کار به بنگاه‌سازی توسعه‌ای
🔹
امیر نیک‌رویان در تحلیلی برای روزنامه شرق نوشت:سیاست‌گذاری در اقتصاد امروز ایران، دیگر انتخاب میان گزینه «خوب» و «ایدئال» نیست، بلکه انتخابی ناگزیر میان «بد» و «بدتر» است. تداوم روند منفی تشکیل سرمایه ثابت، به‌ معنای واقعی کلمه در حال بلعیدن امکانات تولید و فرسایش زیرساخت‌های حیاتی مملکت است. هم‌زمان، با تشدید محدودیت‌های فروش نفت و تنگنای تحریم‌ها، شریان درآمدهای دولت به‌شدت در حال انقباض است و نمی‌توان به نجات اقتصاد از مسیر بودجه‌های عمرانی و دولتی امید بست. از سوی دیگر، در محیطی با نرخ واقعی سود پایین و انتظارات تورمی شدید و نبود امنیت سرمایه‌گذاری، افزایش اعتبار الزاما به سرمایه‌گذاری مولد ختم نمی‌شود و می‌تواند تقاضا برای دارایی‌های تورم‌پناه مانند ارز، طلا و ملک را تقویت کند؛ مسیری که از طریق فشار بر بازار دارایی و نرخ ارز می‌تواند بی‌ثباتی قیمت‌ها و انتظارات تورمی را تشدید کند.
ادامه
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693164" target="_blank">📅 16:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4tu-b-UAH_DtuCCNKef6glIkPmaZvtzvnbh04IJGOI0GKYcP0dMgKhlfLqcaHYGxC82HLcgvqfc3aOVaPWAclZOCCAiD2X6kebXJotfsqT0i1dzUeRRmeaSGUXOCmTKuuy8IzO0zCV5RwleD615bh49XXrydpl1-rkvfvAQlvCdJ7EkL0-yo7LgM7wyFPnUYu0_b57gW-hhapP1A_iGnSw17zHfAUFxx0qjwN4UGS507yYPb5QqI1uVRLIjesmMWtMYI2RTgo2_Fmu3H7tU4WvUzDneOiApC7vYvEX53ERIa1G1_Oe3jCecC7BPZJaBkjrRov04foYpiOiEtvzc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صحبت تکراری ترامپ: ایران نمی‌تواند به سلاح هسته‌ای دست پیدا کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/693163" target="_blank">📅 16:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0SKd5gIVqeG1ZXReTNbrw70Yh_XFqU3ArsiQA3bmAZgbzoyTtnfyOPUrFSOh_aD5Q7HXMdboy13uThuU0nO__C-NKfIMOuWez5uQhF6Rp29dIAYTXN8fUKzWZHFJBquNWxMz-02GhrzE6rrHKo2S15CIt8EXghJtcDTvqFkMj_zOVTlV25VIGpA-laSjK3Wl3A9vi404AIVmabTKLGRjbdNcorXc3bbdIo2r870x5YUe2tBJ0qa7DF2heC8yDgB-pUycj29XspuJ8a72JMBFoEZKpdOS02HCH1r3f9bNMeKWRYvyuqukc9V8EctxEyEHEfJK4dcV95yvFTW2yFsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y23KZlUAEvh_1iTe-4lyT-J00_M6ZPqMFMrxZ-nWZWbSPPBzAG1hOgJtYmfs16i8PXWcgPyczdCFirmKEDn4FH01UegOQsBE-uRCrA9kyXfg15dnFS4WOEX-KUqMXcH8PKTsvkhlrWMXo1xOMTqFA7-fHAZFDdnDSYmeEXaqO3l6YB6EVb1-h6VxYeHvi97gsOSJNP0gauREEwVVSZFbxy_AC4ofol_Q7M2w78f9f39uAYbZkAN7AaDbWU_Y3gZSkTtJLPB0U7SoPUeLvrlQIi-dAWwm34mOj0oJrv6HxjTcfpRb2JQUuKOZwIR4XXFETiAe4wQv0B5WXY13Q-kXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1L1YJ4WPiBaHJu-nj8oJhO5EKbylYLuL1ro6wjwiNDOZWQhcMPWYDkY0nSKlnUjxseTQG8Ld2_HgIT0XEvk_0wLp9otYTWI0e6KxX_nODQDjNn2xaV7Rkt_twojVkwwe0XeNBPD2lOhT1ZOPEaj_CQ6-yJIULCXLgfo77AthF1qAckKQrTldff6E6kDipHs3TDiGd8ycFFxrlfwLg5_j57O4XNeqxa414v5M_R4KMwcgrVxXjOlpHMRjbOPmmQq-BiJAAWoc15uQtOTSknydqoftyeMwap0cYSifcEd2BxPElR2lmRpAOJjlAyswW7_cJTTE3g8z4kYdKOYUQ7WgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYT76h3jzNy9g96KDYRh7Yyy9nx567qNYQjocs5ZQDB_EWHMEZ4aOVnCeJ6KwSoH8_C43ZsHaz1qSP8q7H20581Artgep-4HkL1d3HqDZljq44GLbQJ1lqh7ERnwUca6epPbhYhvd95bZECe3IexBfqzs6HuD7-MBuGblgdKg-tbnrd3ALkLEJm2yYVNc7rCGTpr0zmYXIbvIuhZgspUQugZFYZUyqt8xmAQXfGpu3-oRX_G-Sp9hfr4ropTOSMVUT-GaFy5zatoiEe5WbRIn9IJ08Q7lLD2LzaCxjCs10F0YON6ztwmmKMsax8W_Fn7hhDtTVRErdNEi0fOLTKmcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴ مدل ماست خوشمزه و متفاوت؛ از ماست لبو تا اسفناج برای سفره‌های رنگی
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/693159" target="_blank">📅 16:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
صداهای انفجار شنیده‌ شده در جزیرۀ خارگ مربوط به انهدام کنترل‌شده مهمات جنگی دشمن است که از قبل نیز دربارۀ آن اطلاع‌رسانی شده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/693158" target="_blank">📅 16:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ایزدخواه، نماینده مجلس: تحقیق و تفحص و سوال از وزیر اقتصاد در مورد سهام عدالت استانی کلید خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/693157" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
رایزنی‌های محرمانه درباره پیش‌نویس قطعنامه فرانسه درباره تنگه هرمز
🔹
به گفته یک دیپلمات سازمان ملل، پیش‌نویس قطعنامه فرانسه بر آزادی کشتیرانی در تنگه هرمز، رعایت قوانین بین‌المللی دریاها و عبور ایمن کشتی‌ها تأکید خواهد داشت.
🔹
این دیپلمات همچنین از رایزنی ترامپ و مکرون درباره این موضوع و گفتگو با کشورهای عربی و ایران خبر داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693156" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: آمریکا از بریتانیا خواست مجوز فعالیت بانک «ملی» در لندن را تمدید نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/693155" target="_blank">📅 15:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693153">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
از وعده به رئیس‌جمهور تا عمل؛ پل‌های استان هرمزگان به مدار خدمت بازگشتند
‌
🔹
از گفت‌وگوی تلفنی رئیس‌جمهور با مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان و تاکید بر بازسازی و آماده‌سازی مسیرها پیش از آغاز بارندگی‌ها، تا تلاش شبانه‌روزی مهندسان و راهداران...
‌
🔹
۵۵ روز، شبانه‌روز تلاش کردیم تا شریان‌های حیاتی استان، پیش از موعدِ مقرر به بهره‌برداری برسد، امروز این عهد با حضور وزیر راه و شهرسازی، رئیس سازمان راهداری، استاندار و مسئولان استان به ثمر نشست.
‌
🔹
روایتِ این تلاشِ جهادی و حماسه‌ احیایِ دوباره‌ پل‌ها و تونل‌های هرمزگان را در این ۶ دقیقه به تماشا بنشینید..
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
#هم_راه_مردم
#دولت_پای_کار_مردم
‌
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/693153" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl8s4PYDaLIeH2e-BPUxeWZ7OJC3ilyuj5byIq7Rez_EnslMGlo4fqf3xVNHBrNuI4R7prxIrUAO__gTcl4BYaZLw68Nauy4hBwAVZxCL7Hi6cuXklcmbMFBYDCUbRvb3VS3S6joZHSb8uetmQgDvssaPSJ-sgWTWGY6mRXXeH24iLV31b1-6NjGFxbflelK4qdkLhvxmkz_TStiJEky31BDjZC1eMmCVuniRxpHflP6oBO9eYW8Lia09YtayxL77uBhuKFdHZJGnBc7j-_S32szThit4cLkf6LlpnKHCIXnhowoEE0CdaN3cyjedbAh2DO0yS2nZWV4_h2hf1-sQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40347efb99.mp4?token=cwkDMDAlNlUAe4aTfRcspssHQyuiwREpGrMBj8G2Oq6D0YqRcDqpx_DGfwxxl6Otg735VjokrXiLuWjqw2WuGQ2sfDqM9nuE9VTj_oVQfOX9YlMoclPmQtTq7kaF7R4Wcv9juDvG0SC3abLFELr01n6VEBawPQKbezdD9lxfN8Ix0I6i3_2uvoAZ1yv-n0TCTiNQ-Ncx9wkAW4TP1P0k0EKIIOpfcJjaea3-3-7csbxgbhic2tnEEbqKDRRb9J0S6FnOLceA1_XljEHs9YpeErKH6XgiVozHg3SLs-J-nCNO51EAnWBSshe0PXChpNTeGElwo1YtmiImWXeK05UOZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40347efb99.mp4?token=cwkDMDAlNlUAe4aTfRcspssHQyuiwREpGrMBj8G2Oq6D0YqRcDqpx_DGfwxxl6Otg735VjokrXiLuWjqw2WuGQ2sfDqM9nuE9VTj_oVQfOX9YlMoclPmQtTq7kaF7R4Wcv9juDvG0SC3abLFELr01n6VEBawPQKbezdD9lxfN8Ix0I6i3_2uvoAZ1yv-n0TCTiNQ-Ncx9wkAW4TP1P0k0EKIIOpfcJjaea3-3-7csbxgbhic2tnEEbqKDRRb9J0S6FnOLceA1_XljEHs9YpeErKH6XgiVozHg3SLs-J-nCNO51EAnWBSshe0PXChpNTeGElwo1YtmiImWXeK05UOZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/693151" target="_blank">📅 15:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEIl3zlPB63rxZTeKPwm40mGw_1YO9UetIu2fC4pJeyvSZ3YydRbqyFbF-QlY0JC3_dXenIVxw8Wqou6LTK5dD1aZCd21N4x8m_7CPW5c0eIBOOGyv5oG4zpe5RhW5kWq_eRGK-TkWwtrlcM0QUrQAlI82jXz5t78ccU-KPweg13Gk7KZK5P2zalmdJ91dl2LIXNPc1dTzY79fCA7Gt3aw4uS-0u8TE_ppURjH79F2CTBFeX75Hhg17UiFJMJqNr-rja8u15RzfAsbUWvQnKCSCyXvmBZcCdmreStK5E_c-r023Xkr1YOyrwwhiih4V3yim3Bu6xxKR3rYiv-U2GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد روزهای پاک کلان‌شهرها در سال جاری
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/693150" target="_blank">📅 15:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0zjtbeWsSkd3XsKfQn9m47beMlunqz5gVVC_LLur0wBF8EY9qRwufFxNmVAaDrxPUUZIrf-VFfCrtItvJlAkruyKjtDBDv1uw4X50TgQqUlHAmTI8z-Qn9SUKvMmqDkFLG-nMeGhF8Ijw4LRMzvdVhrlxMaJuI_zYJh3LR4o_4aTNlVUIuG3ntS29HKMt0fvYj2ufMzWuuF99qdcw0yNzsbgAbn-G0WFw2yOrkWJevQa4cXVdP2XypFEHZQMmTCPAOVvleAdvZ60Yc9BgZpmNXLhlRxnQ0szS0poFd9iSnnf8rYLwyMHMrHowTuhz6dXBmUJepRAJi34ZcNKDkMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر مشکل پوستی چه درمانی مناسب است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/693149" target="_blank">📅 15:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbPHb-JD-tduAlgl5MBR9pVQ4bj6AFlAKqb_Zpht1JXwraANT8t2kZBIoLyB1xB1CNiBUTOYdUrKUCpVwxWYq4244q_ruvCCSsbnkpebNy_BUXZ5gClEa3npaNK_0TPMfOA8I5zR63UWiW_GHoH2szwSO0uHlR6olQF0AOzwcZ8zT-M1cC-Na-DEAYmEeQbZ0Nh_tRPDPQpc7DkuUnxd1A-NGW4bCxckTcODae4hFNORaOt4FKwALCKr19r7ojflXMBCWu8Mv7KelvdiZQzJNMYFnHFjzW-5eST8xi_SYGJC1ot8f7VY5xWXD88LiqG-w6EoajTiXbs7LhCNIY0hpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/693147" target="_blank">📅 15:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QelY0bxNODLkvc8GQpDXgT2ujMZVA-jPDDPlOZnaFAeXJlpEqBIgUHev33dVyCakX-6JjTvKQ9nTrYPz9mnqRNI4x0WeLOB8BqG3I_gP6d37VRnT2GD444rboit087D5BYhEZkkObqb2XAbgVETQq2GBhuwONRyms3UIN4zc3PNeCXSsB5E5TrRe9j2NeMcSGrxUFDWYXugto-FGMMsS9q0u-yebe3eO3V4-BLw8X_FiJuqusGPB5wloKOneBD8gXUlu7UrHq94ADpwQ08EQjRZOnvH90CPaGIzD9u2rcVeQC3m5c1M_JIGoYdUpL86YlPS8dd4JQjZyAvWhvCEh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه میلی به شعام: مشکل نبود طلا نیست/ موانع تحویل طلا را برطرف کنید
🔹
شرکت سرمایه زرین ماندگار (میلی) اعلام کرد معادل ۹۶۵ کیلوگرم طلا مربوط به تعهدات این شرکت به کاربران، به‌صورت فیزیکی در خزانه‌های امن و بانکی موجود است؛ اما به گفته میلی، محدودیت‌های ایجادشده در فرآیندهای نظارتی، دسترسی به این ذخایر و تسویه بخشی از کاربران را با تأخیر مواجه کرده است.
🔹
میلی در نامه‌ای به دبیر شورای عالی امنیت ملی، با اشاره به مستندات نگهداری طلا در خزانه‌های امن و بانکی، خواستار رفع موانع و تعیین تکلیف فوری این ذخایر شده است.
🔹
این شرکت همچنین اعلام کرده طی ۳۰ روز گذشته بیش از ۷ هزار میلیارد تومان تسویه ریالی انجام داده و بیش از ۳۶ کیلوگرم طلا نیز به‌صورت فیزیکی به کاربران تحویل داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/693146" target="_blank">📅 15:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
یک منبع آگاه: عباس عراقچی وزیر خارجه ایران و هیات مذاکره‌کننده همراه او احتمالا تا روز چهارشنبه در نیویورک می‌مانند
🔹
پیش از این برخی منابع خبر داده بودند که پس از نخستین دیدار میان عراقچی و استیو ویتکاف نمایندگان آمریکا، کارشناسان فنی از ایران به مذاکرات پیوستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/693144" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
عراقچی: مهلت هفت روزه به محض پذیرش پیشنهاد ما توسط آمریکا آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/693143" target="_blank">📅 14:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555a41deb9.mp4?token=KBunO1HpsY7gkdkHYqyeMfDOoKNiIz_FlshVfPwGICN9kHkQmyN5Mu3Elw8GYhtznhkY87IQ01NkNz-XT4q0efQG71JLsMw1WIu7IQHBQQv7tDgcDjwLjds1RusUBPf7vc7nuZB6Svn8ATyC3tlpFbxD0aPlgCByveVSwPE1qmlvjuSy2JwK6-vsrNk304P2xzLkPgH-PoeD76AqR0EAWM2Dz48MThUtgk4nIyhTcq70yif-y6ps44a-IqLjUH8jQ0jMkyhHDyTgpJ961RH9gYXGQ4sLkGIsQABh06lwePKqyIhKCDqxgtKjkcveQzndneP6byBjHhYznEPzrEaCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555a41deb9.mp4?token=KBunO1HpsY7gkdkHYqyeMfDOoKNiIz_FlshVfPwGICN9kHkQmyN5Mu3Elw8GYhtznhkY87IQ01NkNz-XT4q0efQG71JLsMw1WIu7IQHBQQv7tDgcDjwLjds1RusUBPf7vc7nuZB6Svn8ATyC3tlpFbxD0aPlgCByveVSwPE1qmlvjuSy2JwK6-vsrNk304P2xzLkPgH-PoeD76AqR0EAWM2Dz48MThUtgk4nIyhTcq70yif-y6ps44a-IqLjUH8jQ0jMkyhHDyTgpJ961RH9gYXGQ4sLkGIsQABh06lwePKqyIhKCDqxgtKjkcveQzndneP6byBjHhYznEPzrEaCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه کار پله برقی از نمای داخلی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/693142" target="_blank">📅 14:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
درخواست عجیب «بیرانوند» برای بررسی پرونده پزشکی‌اش در کمیسیون اعصاب و روان
🔹
دروازه‌بان شماره یک تیم ملی و تراکتور، با هدف تعویق خدمت سربازی خود، درخواست تشکیل کمیسیون پزشکی به سازمان نظام وظیفه داده است.
🔹
طبق پیگیری‌ها اولین درخواست بیرانوند، ارجاع پرونده…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693141" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhThGCdNmLgqbOyubvZHMPKrO5Ic5KgTfFx3d85A4s0qnZOob1YUBVl6wn-xGEFbrf5yIFRVrCzAXzpwqAwKt2USVBK98CZ97F1a59h9mWw5ikQOQI9VjcYbcRLXvaHHqvDVT3TWw62Zjz80Jab9RLCq91zYeary4VL0_tWmDgBie793iSwAK-KAq7Clr7oxYSFfLE_ox-4l-WA7byHxiRAyI2OuZc0XhkKhOekSffbu622HmqnuRT4857m-41djIgZ-LCny-65ybMq-KubJRb9ggUIY2uvpFJfcnb3EYdRWlwwIecdKPDfMxZxh9NFugQI0aba0tVI8bXk9vgdz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZuskrdIxwBlElyrN7YRSpNOQ2hkI7Ozd1bKDNMMK8NL1CVyBedpWD9NWChFToMArRbrOxe8jsfs889JuUddNnbomohRF9Auk_Nfy3UALexW5X-znFx8BYtc8CHROOyJ_A7ZDTHtZ2C1tPovb09MoO7eyF2sT3Msm_lXWPZlC3veH4_ixF1Z0p6DgZjZxg3V8jnsvspeBnOKvRIGk-P9Xd10Pv80YTjLckdoL7CqiY4f2j5mcY9q5Hz2E9Vwfl7QG5HKxqT4sJU7wwrOTBDwntkznwEyWehqLTzbuWnSjtuOS8a9VKRElXzMWUCQxz-qFJdWbvlAMtcXKI8F-D0eqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شاید باورتان نشود، اما در این دو عکس هیچ اثری از فتوشاپ نیست
🤩
🔹
ابرهای نادر استراتوسفر قطبی - ایسلند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693139" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مکرون از ریاست جمهوری کناره‌گیری خواهد کرد
🔹
امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/693138" target="_blank">📅 14:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پزشکیان در گفتگو با شبکه الجزیره قطر: ما هر وقت با آمریکا سر میز مذاکره نشستیم شروع کردند به جنگیدن و حمله به ایران؛ سه بار این اتفاق افتاد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693137" target="_blank">📅 14:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ef3041c.mp4?token=hLtteVciyRSHE7Odqga6lKDs9Fsl15v15ofHu0yfm3yfixR8Xk9Zl_O_80N20WiKnsJTs0__chLVei51zp9GyXjmCDPoAFEeCtAUh__zFNwcS6XHZ_N03qt3qGHyZiF5SIZao-mX3Z9pw2yfm6IXDJd75s1Z6blgxbSc-925WIMVbLoIkQ4MJi5uup9kq2PYdjYeAxJ1OWscX6Cyey2gFzxBDq_Ibv8sIbfkVyERLrFbrtLKarEEHt8ESwF18gGj2SRc2y-TrqIHOgkQo5I8EbHbn2gzFk3ILpslMv4daHWI_tMLUTei0l0qiVlqpyBElpYLEgGXJtrDLpGGqF6ztA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ef3041c.mp4?token=hLtteVciyRSHE7Odqga6lKDs9Fsl15v15ofHu0yfm3yfixR8Xk9Zl_O_80N20WiKnsJTs0__chLVei51zp9GyXjmCDPoAFEeCtAUh__zFNwcS6XHZ_N03qt3qGHyZiF5SIZao-mX3Z9pw2yfm6IXDJd75s1Z6blgxbSc-925WIMVbLoIkQ4MJi5uup9kq2PYdjYeAxJ1OWscX6Cyey2gFzxBDq_Ibv8sIbfkVyERLrFbrtLKarEEHt8ESwF18gGj2SRc2y-TrqIHOgkQo5I8EbHbn2gzFk3ILpslMv4daHWI_tMLUTei0l0qiVlqpyBElpYLEgGXJtrDLpGGqF6ztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: چرا و به چه منظور باید با رئیس جمهور آمریکا دیدار کنم؟ وقتی ما توافق را امضا کردیم، آنها آن را اجرا نکردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/693136" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl4CB8Ikf_I7W0Ed0grssp-UMPNAnmayL2GLpF5garF72pUR_weP7h_5bN_ywCrZIVBeUFOh8IlAwureVfeqc6A2zAg28EidH-_ktfYtNpl67dg32gaickxk5k-DDo75PIbxwpzHUN6vdJ_Mf3URz323qY2caksv5ANwTKWQ7pFd5N3FLFoTVIIQDre7ZT-7vxF5Kk_RyJS0dgYhuGbbU3JnziZ_B4g9T5hoSJgI4-DXrqNFGWuzRwm9gchPSERkm_Jbj6XSRjwaUbCLT-zwB6zgs5vPJ0csrpE_XvlJz5PIrB7AxcTmE3U02weF5DIPWxrSYbi2N9Ztf-8ZaubiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: با گران شدن گاز در اروپا، تولیدکنندگان برق دوباره به زغال‌سنگ روی آورده‌اند. پیش‌بینی می‌شود تولید برق با زغال‌سنگ در شش ماه آینده حدود یک‌چهارم افزایش یابد تا کاهش تولید با گاز را جبران کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693135" target="_blank">📅 14:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693129">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr5UJjqjNiA8OZhf8fgNXaKyHJV5nE9uQEde8Q0OVCLTadAgHQ69Z-0KCQeI03DYbEY1lsvJ85kmtbYe5cDT1BwknhJVsvLBE3vpNVczj55aJKBL5U7Wl_XZ_dSnMrJllfxndWlOObWMCpElIpSFFaDPBjx-18frmjJ8bQUBuAP-uiS1-dU8J9cpBkesZfLTpz1RgJp4sLG2rrk2rvpNZWBADv1jiMuDHFvO9BbrNH_Ae3wiQsqIZBMVjWIi_WGTjkAPrq41Vy-WfYjvVO6fPz9ylwocOtcr3B9J-vDfh9ql9gpyuuZv6egWvjhOczLyz8Tymtm3e6Cpu-6OUOQhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVU8nk7TmL_ETYS4M7adEG-hi0ObHuizSetK-1AlULdTcMlVuQVWrLSQbh2PmTvgO1PXEJvjieDdOl8iDx72LEBDXj9EJhDzCaOodfdWiFW7vDVfRJXYUwITr5BBf965hSkEmuE_vqLX8-XVBgmbywFSBT1yIqeu3cvl-vwS7n9BkC-pCFKVgm74TyNYVc95OZGxKFI0V_i7X97Y8Tu2qOv4_Yu3mPjrQeRfNsy6q7PGZsPg77Yk4dA7ZD7dsQVr8izA3qXfTVIoZFLBPiNqyUPdTSnMP8FHaq4f01uJuMraNrA7ELibL1F729znBO5xWb9efdHIt4ankjBi-0kKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bX3EBaN_6GUSPGxSz6qMMDc_FPrQBcwHJxvBK4hKVcLRYcpPfHutDeeRXiXkSJB8G8Dr8cJZUnC7d9XsfYml6tREehwjJFX4_wqS8JBx1aedMir4V-Z3rwfCW-TOCWA0OBaMaBegSM1laBB89tq81zfrGJiOYrFhf0qSB58QJY4E7phRzgGCbJTIRdbl8KtRkojdY9_WQhPuiQVHfwd0mochUw00w0b4zMFl1yFm5sn5A4Tsw7ZMJP5-YDGrZkyt_-oA5qqQBdct0zGsD-L0XoUsJ8PQEWDNF3IP_BoxtCjAqiTBgjVM6lM82flm8B2aiGXmDVhhUAy0cevQ2Q7QRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGmLoCUCjOueumPYp4jHslwBZ8MJTNq_AnZftAFO4dpyraL6VNwIxvCLI0l7r6dlV2AKwSyv9aMe0p6b4VEj1dbbzOFhlTPWVGRoqn02S8j8Gbur9m5s_xTrcs6f6VQRRPDsU1EfJlvOwh8fM-faZR_lmKr4iyaAPoEsHGXSAlgGRXDQQm2ou82vV2AKUrrAYsXXW7DEMjVQydLT_bYh4O57sIjZEd8zlK_9-3UjnycQDEK1j9bcf7ByQJOG55nurCLXpX4TgqbgDHfatr_5ZTQrWkRSw4jjzeciMfX9_L0b2aLQYVH6HsyvCZ1SzqFIWSNpjePoSgehgOnYWa5CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmC7Fok6uwC1cw7Ds5J72-QWwOQ-dVZm8wzfYgOQuEwWE1vcj_TIKU2TqywKjMyq6wBmAVC23SIG1kxc6pusSIt2ZdDRmdvSTodLPLByyse1naOsX2TJu6PxY_mJ5aSHJK7Jp1jizmRdspSvpvaZ0fqWM0aPGVX-hBxNgAAng_va_h7Na6vUy0_QuUGyQ5I5J3Lk7XXYR9HWoAf1LbSDb0PfkTGNOmk9SywgzsqJc4nxTigUcXhH0kMsxWLuV5OnlmDKaeKv8u5dMeIR2WMz43WNMSPI4OmytuBNBS-9PV5Ky65kaDECtpuWNM3dAhjcd66TkcoVLvpLK-4L2wU9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkX1j_h-rB6w7IewhFacbVjgbX1Bzm1uTi12xtZV5PV9eQlFAHwqRRfoVr6X4Aq-PrAuOwe3mAcTdGGbCab5yz2fWzlaKhRfdObcBOP06oBhx-YW8aBK7EvbROVzMkwSCCDr31ucxirN2pbl8TMj_-YWh1yy31fHU7XVWTA9ZZeoqVUaqowk3y8eKvkSZBIASKNuOk_R4M661S10FTvFTHZSjdlmTm7di-_Oy_k2AAdTrsV8F9zC6gFOPiIVUk5NRZHnOyF6ZDtZnOSFQsBkJhIOMw_UTonx_hni6DvQ1GZihE5J56msigQHf-nTrAg_q7OuRXjCkigoUFBVSl6jVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
به هر صورتی چه مدل مویی میاد؟ یک راهنمای کامل برای آقایان #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/693129" target="_blank">📅 14:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693128">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBli2Vb_q0Bmm5Xk5hdEb-7Du3tUGn2KNpt5LiUP3ugJnfnA8ihVhymD1wPUKSskisIHevO_Y3AoQh9DtjF9vjrsYYaeG90jK6UsR3bMK3fcqNb2r0WYLCsRSOm58cUrzKaL7EeWeUeYPKvtaOHuCvxKRVSi3qR06bppd2lFl4fRzx8FeqoAkHr8avYcuYjBQKjk-TV7kK2jXF0xMWQKRYlViYQD97JBSI4YE7oiAehitGp1oSWR0EPX16JV_vJwrklR5IPL8rwA-qKwavGZWZp87YKQD16W4Ju7rB6Y4CKJ4LkQY71zR6lUb9_hVo0JYpTsnQyaDLbLGMxiPJW0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ مهر ۱۴۰۵؛ ساعت ۱۳:۴۵
🔹
معاملات امروز بازار ارز تحت تأثیر انتشار اخبار ضدونقیض از مذاکرات ایران و آمریکا، تغییر فاز داد و دلار با عقب‌نشینی همراه شد.
🔹
این سیگنال‌های متناقض، فضای مه‌آلود و سردرگمی شدیدی را در بازار ایجاد کرده است؛ وضعیتی که موجب شده معامله‌گران با احتیاط بیشتری رفتار کنند و خریداران از ورود به بازار منصرف شوند تا مسیر آتی نرخ‌ها پس از شفاف‌سازی اخبار مشخص شود./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693128" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693127">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldkRmphFbaWBBkVXFiW0l1lXjV34mKqS0TEmi6Ic74Sd0RPkeE_sD9a5q0m49tg9elwmfVGsAS1jTcu_vLXXCdpxlH2FZjUTLCbJU0bUJHCjE98iDk2FvY04-qPyZmGSWaQhr2aIAGD992S3-N5EDugtSp4qt7hr-fF-MmDUxLEGxUL70g1ZNYLUSwMkHZWQGb1b4CyqHHLNmyvOc_iKf_jv19Lz5CIjHpyvsWSnNGKkhru5KTZoBz7xt62rICrmJ9sOOTZ7Uo8AFv3jk5Pafeq90fAX8v9D5JOipQzfhxcED8sgkCvcVqFuA2TZ71iLCoJ9rClz7Agb2F25agO3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان رضایت از عملکرد رئیس‌جمهور پیش از انتخابات میان‌دوره‌ای
🔹
جورج اچ. دابلیو. بوش، ۱۹۹۰: ۷۵٪
🔹
کلینتون، ۱۹۹۸: ۶۶٪
🔹
جورج دابلیو. بوش، ۲۰۰۲: ۶۴٪
🔹
کلینتون، ۱۹۹۴: ۴۸٪
🔹
اوباما، ۲۰۱۰: ۴۶٪
🔹
ترامپ، ۲۰۱۸: ۴۴٪
🔹
بایدن، ۲۰۲۲: ۴۳٪
🔹
اوباما، ۲۰۱۴: ۴۰٪
🔹
جورج دابلیو. بوش، ۲۰۰۶: ۳۹٪
🔹
ترامپ، ۲۰۲۶: ۳۷٪
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693127" target="_blank">📅 14:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پزشکیان: من دو بار با مقام معظم رهبری ملاقات کردم، بار اول حدود سه ساعت و بار دوم هفت ساعت و نیم  رئیس‌جمهور:
🔹
ساختار رهبری مسئول سیاست‌گذاری است، در حالی که اجرا بر عهده ماست. آنچه ما اجرا می‌کنیم در چارچوب قوانین موجود است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693125" target="_blank">📅 13:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ6P2csVSb6xDGxbC5we2Zo166O3CjH7QPJnrElqc7RsOscXHGv0X7ZtW8T0tMaHPKDLUb9TUvlthzKFatkMRV1WLGfbAU5oICsIjllFXibnwpc4cth9ZJ5r_rGHDhDX7r7fMZQzRZ306YssQKQ-6MsrjjyoTCXuBzIMwuD4u9WMepd1Uqf91gki2J7uTGPgmZSOBzRw_SZc9RDhVJo_zeXUy8cqCt3yUHb1qSiNP8R1hknMzVcd-feQWvJUoTfxGvx0I_rl3nh0gr12KotL-WGFIwdkxrcPwTpPJ6GJiASJmtUABJgdOFLRcN4Cf9YxyeSQ0_nKcoHQUZq2vkQXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrwHZq5zrwh8-6EEnWno6fbz0NtrMSPWc10LggZEaf_Si1GOCFwV7z77b96Zae3opWwzfvEonUA9L5E4lZ-xEfCGnNTwUzZQ2f4CNR6euIXDdSEUotrzDsOQSbONKjjhJBBPxGeiuk7g6FX_nOTCd4g3pNFLHwNDiFCRK58GQKl2ce86DKkfmIzFsOoxxo6i3Fv_YIHCVdD7JU-9BKGtyD_PxmiIBOeWLWlQzyNHex455RoQtrgty1Fvbxo63BvWwYf5NVhz-4GWZwNMGDLdRCDuOLh5zxuAGAbI7RTrzLzu47jomDT6OuZKBeo6_D5JS7iMtffWoVNhnEaG9TOmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogWfSUnK5mxpDsWdjAYRWHvMI7E3tCsdf_vNq9Ppaty1qOn325U5Qpy0Ef-PoF8vv-yxQZImLXKgqIxJ3LNt6nPUg6oodBPYqU2acq7FbWlvGEKdGWyPXRqBWlcCPCuZgayDTdsRZOHX-cq6C9smiy4dZ5ES7jstZ51sphAErt3ydGueVbtPpZtvquDBs7Ym1s-OBBcLb-EYgUtv3ea9n595U_oQh9xcDNdsyMHxN7VGig6i_-nL1WJEWpYyuoj-X5BkOzRkHAnoFIjbsWAkhlhM2s7t7twNiyh7NkrE3JJsRLJVsQ2B5crxLuguvc1dg0FNMc-DtoL9wbfaoK_2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/be9g8zlBmsm-hVigyDIWtOvcjp8YBGuLIFtfmfx0dqxqqtON-Z2cuzV0j3gceWStzCxWSmFI64bKcXhvm1W92pTGXFNghkRdFDD9DKiAMKqLRPIRrLCvG79dl9Yb3TiN7Z_GvPbuoFXfKU2Pi5xCuMarPrThEKOC079eibywvxTeJtQqvhPaEBdJSO9icA6ioP2ndNUeJrLrWSpPn4oPL-ebNJ52kxPvarTRysuWGZwAvb79bCkbM29yU2-UaqofbMBXsiUM_EMyX2YpxM_DNmHLRouqRdHGGf0LxF6Y8uPIo4Bl7w_3124Ximh3SPjhfRrv2Am8s_APAeB5-dPtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjSLBUDa3tAT-8qppkmXu7r-VmMsj-5Tf45meLA_NchV2J9BuXSvdOq-yog5fSSWD9pVExVJRVDsWI9rhhfddD_ux_pPPFy0GBn9OIdXHEEay8RGvoVlspneKw0ATC5JH-6JC_UUauNHuvSgVSm2lXqavgxWnMLAZ-H5xw2ErRhDxAEwRPRGc_IFzR8-MfGHEaxANYYwe8z0BgzsBKJhdYgHnY-A84QiqdjrYdAYYF9YU1PoXgHaY6boueEPJsuZGMVT2Ysce5BHMZwjWYg7C6vKFb69UjHSSDQRq1QBYzPHIEGCeJ6Y22pn9BGyAi6bjVP7tR4IUGKMPtuaKKGNGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیائومی ۱۸ پرو با این وسیله جانبی جذاب به گیتار جیبی تبدیل می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/693120" target="_blank">📅 13:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693118">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d806c987.mp4?token=Z_9U7XVO1awG72ptkmVxMMYoabC0RxMzWz6iHIqYqDT7tJuwNnzijCRS7FN0FoS-ae49MSBmB3oINzUplNs0vNDVYbxwB7ynvpeh8doz7IhhdWkcnMjJV9Ean0DUl9VN281xylbwhTXWDt1hvb7LKEfVel5WcsM_SarTSpkAUITJVj8t_D9myWZswituJRI80_3uJzIgF73Oa-XHnCroJbIrIvMGfYjonbEv-XlP0EyEALtcfxx1oaqA86JyCaOW3BurtkzRiQn6P-eVfAg-D8mfE6mk_j5OWg9NSCfVRlLrLee4_y_cRvP_bmgtpkW8fzX_zkQNl7sBtImWRhq2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d806c987.mp4?token=Z_9U7XVO1awG72ptkmVxMMYoabC0RxMzWz6iHIqYqDT7tJuwNnzijCRS7FN0FoS-ae49MSBmB3oINzUplNs0vNDVYbxwB7ynvpeh8doz7IhhdWkcnMjJV9Ean0DUl9VN281xylbwhTXWDt1hvb7LKEfVel5WcsM_SarTSpkAUITJVj8t_D9myWZswituJRI80_3uJzIgF73Oa-XHnCroJbIrIvMGfYjonbEv-XlP0EyEALtcfxx1oaqA86JyCaOW3BurtkzRiQn6P-eVfAg-D8mfE6mk_j5OWg9NSCfVRlLrLee4_y_cRvP_bmgtpkW8fzX_zkQNl7sBtImWRhq2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از دلایلی که نباید در طبیعت زباله ریخت؛ روباه فقط یک قدم با مرگ فاصله داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/693118" target="_blank">📅 13:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaSyYya7oWHyRBHSrJ6q4caRMa2AjWM1DduNYmu5wGN1eTeY1hRFneibilYUR_9rVhMjRa7hcaryoIDju4hi7q4w39gTn9hHWHw6sSJjL9_jcN9tFWnmWAFSyXm40Kh3osrGYv0WzGI4dW_LiEKBLako60j3PAWzrTatwTRph3-22EIMSKoJ2aBXwV1e-b5ge0eoVfIFwGI_jJSiVpvR7RQkO_02js34g4qrYS8PTtHkjg6BVRV0fnRzb-VVJB0G_9IWILaa-gbh56S1bCQM27ODuYZFuEgke1lFuuCa0hrZQp6yOIbeTurQ2TB7MYc5Rjq40nt4l6i_yXDYJt6VaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیرسایه پرچم ایران/ قطعه شهدا بهشت زهرا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/693116" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
پزشکیان: دیگر به مذاکرات با واشنگتن اعتماد نداریم  رئیس جمهور در گفتگو با الجزیره:
🔹
قطر و پاکستان در حال حاضر بین ایران و آمریکا میانجیگری می‌کنند و پیام‌های ما را به واشنگتن منتقل می‌کنند.
🔹
مذاکرات ما با واشنگتن بر اساس یادداشت تفاهم قبلی است و آمریکایی…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/693115" target="_blank">📅 13:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
دفتر نخست‌وزیر عراق: در حال مذاکره با واشنگتن برای مستثنا کردن فرودگاه‌های عراق از تحریم‌های شرکت‌های هواپیمایی ایران هستیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693114" target="_blank">📅 13:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693113">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">💡
برق، سرمایه ملی است؛ نه ابزار سودجویی!
🔸
استخراج غیرمجاز رمزارز با مصرف بی‌ضابطه برق، تضییع حقوق مشترکان و تحمیل هزینه به شبکه، تنها یک تخلف ساده نیست؛ مسئله‌ای مرتبط با امنیت انرژی و عدالت در دسترسی به برق است.
🔺
مقابله با این پدیده، نیازمند برخورد مؤثر و بازدارنده قانونی است.
#استخراج_غیرمجاز_رمزارز
#صنعت_برق_عرصه_تلاش_و_خدمت
💫
با ما همراه بمانید.
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693113" target="_blank">📅 13:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWc4EqA4OZMBDKWZcAW9d8SyNsWzEdI-TINs8hYxgiIp9k0qh3aQnHOEenJRnndolSs63btZOcYKRWhzbCwMa_Na5jzqXy0-HFrX1cktr3llmmg2e7jsWyA3I5ibQG8PgPpl7FiLx5CMjVmMvM9b4BTyu1QCFg9yRKasOmpzxyLe8tRTWN8G2sAGJNMlMhteLd4uA3OwsmeLIO4jCt2ofvSLQ_52tF16TxCEAD-e4sfOgJUc4itV2UKowMxuojzJk172RB_BvLT3ISg4Cwm9GrWXrCFXVTepn1sSEO_zPAo7t1K_aR7iPc5B5AEdKP6GT_j2Ch83kXP1-s3P8P6_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش عجیب از لو رفتن یک باند سرقت با حرف‌های یک بچه ۶ ساله!
🔹
چند روز پیش، همزمان با شروع سال تحصیلی، مربی یکی از مهدکودک‌های تهران از بچه‌ها پرسیده‌است شغل پدران چیست. یک پسر ۶ ساله با هیجان گفته‌است: «بابام دزده، تو خونه‌مونم اسلحه داریم!»
🔹
مربی اول فکر میکند بچه شوخی میکند، اما وقتی پسر میگوید پدرش هر شب با کلی پول به خانه می‌آید، موضوع را به پلیس اطلاع میدهد.
🔹
پلیس هم با بررسی موضوع به خونه این خانواده میرسد و سرنخ‌ها در نهایت به دستگیری سردسته یک باند سرقت منجر میشود؛ باندی که گفته میشود پلیس حدود دو سال دنبال دستگیریشان بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/693112" target="_blank">📅 13:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693111">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پزشکیان: دیگر به مذاکرات با واشنگتن اعتماد نداریم
رئیس جمهور در گفتگو با الجزیره:
🔹
قطر و پاکستان در حال حاضر بین ایران و آمریکا میانجیگری می‌کنند و پیام‌های ما را به واشنگتن منتقل می‌کنند.
🔹
مذاکرات ما با واشنگتن بر اساس یادداشت تفاهم قبلی است و آمریکایی ها باید موضع خود را در مورد آن مشخص کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/693111" target="_blank">📅 13:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693110">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7017f8cf.mp4?token=mN8uKQ05PaPXiCkQ4GFJEC-zQnVVEGXLTffaQHG-L4s7qU7IVdJ8tA3zroPzp9ewk_WUyY7xj2VxCknzMaHD6Wcq7XK-2GW7cTVdchQSaJW9MSom7mBcOEgSKtO4U9OXnoDY4stwV5XmoXdeawlF3lLPqISYozsIX5LXqv9tbFLWFQE08LD4_umyWJSEKj_AE3gDcgKq7yOAZI8_j4-UHuu_bazmXQEc3wUayLo0qxuvgdRbqypoAJyO3065Kd8M7kOyVNTp73Y3JTccs5ycLURQ-elbBXdeYkjPZIuxZxXTTW6kJPCdml9geiasOk1qfljA2CrybVYURashXeP8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7017f8cf.mp4?token=mN8uKQ05PaPXiCkQ4GFJEC-zQnVVEGXLTffaQHG-L4s7qU7IVdJ8tA3zroPzp9ewk_WUyY7xj2VxCknzMaHD6Wcq7XK-2GW7cTVdchQSaJW9MSom7mBcOEgSKtO4U9OXnoDY4stwV5XmoXdeawlF3lLPqISYozsIX5LXqv9tbFLWFQE08LD4_umyWJSEKj_AE3gDcgKq7yOAZI8_j4-UHuu_bazmXQEc3wUayLo0qxuvgdRbqypoAJyO3065Kd8M7kOyVNTp73Y3JTccs5ycLURQ-elbBXdeYkjPZIuxZxXTTW6kJPCdml9geiasOk1qfljA2CrybVYURashXeP8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا حمل جیوه در هواپیما ممنوع است!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/693110" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693109">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8lGTNz3_U33I1QGL6B8TR4LiYcfG7GFail7VmoF0OkcwuyOWl7rh9fnCNuyAFGBpimjY9jXYzbcf9v9tRD4lxenwRnr-IpRqHI9thY9INJVpn_8uaxy3hhFFAySCHLBsBb81CjtxtxARDnYGbnVRenLYoY_EKm1OZRv-5fOC4D_hho8p_n4fEzFsJAALBXvgs_zdJ4Hql6Y2ccrZre7byAalCn27etsgOVLn2oiT3Ugf8MgtTDuN1S2nrcfkMfDW5QU4H_pDTe1Al9v43twqrnfs1YmKt07lOUcD5CCeBvMtDBbCFIcWaHvsi710onKMwcE0DnWrNQZeXidKvn8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهایی که زنان بیشتر از مردان به دانشگاه می‌روند!
🔹
بر اساس آمار بانک جهانی و یونسکو، در بسیاری از کشورهای جهان نرخ ثبت‌نام زنان در آموزش عالی بیشتر از مردان است و کشور گامبیا با اختلاف ۸۳ درصدی زنان در صدر این فهرست قرار دارد.
🔹
در این میان، قطر ۶۴، گویان ۵۷ و ایسلند ۵۲ درصد نیز شاهد غلبه چشمگیر حضور زنان در دانشگاه‌ها هستند؛ این شاخص برای ایران با ۱ درصد برتری حضور زنان، در حد فاصل برابری تقریبی ثبت شده است.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/693109" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693108">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f677f368f.mp4?token=kg2cYuTWX6BcS0oIIuPLdF0f6T40jTc_1Ogh9wob5jk6iNZskPU1PYrwqx7lWhCcLypkqvJDN8FmoscbIkPxzXVBOWQib3gKLxdtjcl45_GNxFoJ9u2V0cv7vJCe1SSE7W9gIDS8VdrHqF6VZQwaysyZeKkJRj2YYreX1XHdrHWE-2nsNSXbXPWFH9OkWbisJUUU0dlYNEV4KDWDGkD39rawIvO1Pzss2Y6LAoHhbe0EhwXEQks9e1UVNnwJcgy-AevFTBH51HmbpVtkW-UyRcYo0-bXINhl5Zk1KAmMHy9iaj5Y_hcVaFiccwI6d8jrvdno50kUhuj63AxpVu3OXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f677f368f.mp4?token=kg2cYuTWX6BcS0oIIuPLdF0f6T40jTc_1Ogh9wob5jk6iNZskPU1PYrwqx7lWhCcLypkqvJDN8FmoscbIkPxzXVBOWQib3gKLxdtjcl45_GNxFoJ9u2V0cv7vJCe1SSE7W9gIDS8VdrHqF6VZQwaysyZeKkJRj2YYreX1XHdrHWE-2nsNSXbXPWFH9OkWbisJUUU0dlYNEV4KDWDGkD39rawIvO1Pzss2Y6LAoHhbe0EhwXEQks9e1UVNnwJcgy-AevFTBH51HmbpVtkW-UyRcYo0-bXINhl5Zk1KAmMHy9iaj5Y_hcVaFiccwI6d8jrvdno50kUhuj63AxpVu3OXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیابی رمز اینستاگرام و جیمیل در ۳۰ ثانیه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/693108" target="_blank">📅 13:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693107">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce462ceb59.mp4?token=YIUqnuTJOP74Vn-oLpzOih35jGamAIv88i5CNGFCrEj2TXH-IOtKUg8zXN_AJJK0OGrwQjuyGOsJH0K0dNBGWdmdw3EmkWDU9OrQMJPKmlEpkeu1aXQY-4k4kFoRM1YL11rRdfG3G6njfxTtdAzUeZqFlE2WDSsbREYQef19ySr5i1lAMOg458q4w8GpVVlIap8IjP3E4PWETEM5IZgFzei414WGyldyN-5JSxsQgTfZYqEDhnddCsuQP_fjM6jP3gbi-vbEVBsaeEqKIGG0Ws6FF-NMiaxjFLdqZM-yPYFKVi3K5pBVkmF1-l4QXQh_Irpd0gHY5v7tPLDw9OakTBYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce462ceb59.mp4?token=YIUqnuTJOP74Vn-oLpzOih35jGamAIv88i5CNGFCrEj2TXH-IOtKUg8zXN_AJJK0OGrwQjuyGOsJH0K0dNBGWdmdw3EmkWDU9OrQMJPKmlEpkeu1aXQY-4k4kFoRM1YL11rRdfG3G6njfxTtdAzUeZqFlE2WDSsbREYQef19ySr5i1lAMOg458q4w8GpVVlIap8IjP3E4PWETEM5IZgFzei414WGyldyN-5JSxsQgTfZYqEDhnddCsuQP_fjM6jP3gbi-vbEVBsaeEqKIGG0Ws6FF-NMiaxjFLdqZM-yPYFKVi3K5pBVkmF1-l4QXQh_Irpd0gHY5v7tPLDw9OakTBYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی رسمی از فعالیت آکادمی آموزشی «آوید»/گام تازه خبرفوری در مسیر توسعه آموزش
🔹
در یازدهمین سال فعالیت هلدینگ تبلیغاتی و رسانه‌ای خبرفوری آکادمی آموزشی «آوید» به‌عنوان یکی از تازه‌ترین دستاوردهای این مجموعه فعالیت رسمی خود را آغاز کرد، اقدامی که نشان…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/693107" target="_blank">📅 13:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693106">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ4LKWT9b1L4xWE1DFaZYItBDBDqzB0QTQ-MmzIcoz-cfiVD0tRTzBYcSG-FLt2aM0obXd7jq3Cwj6QW_MpJsXSKpCloH-9JgjlPRfXQQXmrH73jhLWDyzJot5PSZkK8m-AYjPERkm_fd-YH97Kfvm3a53RtWBvrYyqIqnS7flK68s1MeLx56LlHML9HeURZ4SXF4vlYpdj_7uy9N3dzJ-oP6I-VdHE7BLI2AXkepLNg9JiWmAMIwzG9hWLTKFDCneUTzCK0SLqKGi96aQE38ZHjfFnWsqCn2P6Ahr8CJajF8Ji9JWko8pijrn6W2uBJ9PHdUW37-zc6A_GskPRz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
و حالا در «مدار» باشید...
🔹
امروز «مدار» به‌عنوان تلویزیون اینترنتی خبرفوری رسماً رونمایی شد.
🔹
پس از ماه‌ها فعالیت آزمایشی، حالا «مدار» آمده است تا فصل تازه‌ای از حضور خبرفوری در رسانه تصویر را رقم بزند، با تولید، روایت و نگاه‌هایی تازه...
🔹
«مدار» با تکیه…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/693106" target="_blank">📅 12:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693105">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه CBS آمریکا: ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد/ ما نمی‌خواهیم بجنگیم اما اگر بزنند، دفاع می‌کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/693105" target="_blank">📅 12:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52665c934.mp4?token=bxK7w_KZ0UgOuBlXTn--xpZLuaV5CLFpdh2M7IBJTIQykON6x-HZUZrOZCSlFRZJSDCkgQjR8U73BDIwzVJG3_T4XofbvmS_YswGy0WHvuA-xD2-INdPWTnWd3sTzhfgkbMlt7xyuXzdnWuIlibIXBuEQlnNMpMHVxM7byvrJrSR_yLZnWoeOA_vrMk_L9TGU7SdVammys4qHx9C0YvC7BSTPSwug5irnuBvAG7DLLuuPD3vxu9L5PRl7xRTbPKTaWEJXe-CNoltn3q2UmeipqthVTM1ienV90-S4ng6q66Nf7JyXqMSimkg2142pF_AUK_S-khRacI1Ph00uUdtow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52665c934.mp4?token=bxK7w_KZ0UgOuBlXTn--xpZLuaV5CLFpdh2M7IBJTIQykON6x-HZUZrOZCSlFRZJSDCkgQjR8U73BDIwzVJG3_T4XofbvmS_YswGy0WHvuA-xD2-INdPWTnWd3sTzhfgkbMlt7xyuXzdnWuIlibIXBuEQlnNMpMHVxM7byvrJrSR_yLZnWoeOA_vrMk_L9TGU7SdVammys4qHx9C0YvC7BSTPSwug5irnuBvAG7DLLuuPD3vxu9L5PRl7xRTbPKTaWEJXe-CNoltn3q2UmeipqthVTM1ienV90-S4ng6q66Nf7JyXqMSimkg2142pF_AUK_S-khRacI1Ph00uUdtow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل گیتس هشدار داد هوش مصنوعی می‌تواند آن‌قدر قدرتمند شود که خطرات فاجعه‌باری ایجاد کرده و حتی به مرگ یک میلیارد نفر منجر شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/693102" target="_blank">📅 12:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDh-55N8PnwLkUKWvDs9B87sRLVcVaMGEGfCTyCedKJqrJtjTFt9PkdJQt6TOzzsQS7BAqCleM5g1vKUVheiShNS2bymSkgyhY2K5HzWeY4MIJwZ0sHCdvxt7VCb8T7pvEixZIJ8kVJCKbuDb01tEkZZKZJpfWt-0YXsRuCRNEtLX19Eu2YqVefOeaUQCb69_glC7Ek_81nH5IjsP3ItFFlWC1FAqxucMdKl2F4yVIO_R0rZqsimDchaH94u7-I067cEpyZ1UY1yds5vShtlyeSDPOdFln2RN9VynBNBNrE-qTbpQgIyMpEhuquLGtx5kdMNEjGvd5hvO-3hrMBfAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/693101" target="_blank">📅 12:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ویدیویی از تجمع عده‌ای مقابل منزل حسن روحانی و درخواست محاکمه او!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/693100" target="_blank">📅 12:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پزشکیان: آمریکا در دی‌ماه به دنبال کودتا در ایران بود و وقتی کودتا شکست خورد، به فکر حمله نظامی افتادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/693099" target="_blank">📅 12:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aab458b1.mp4?token=Jg4P9UJuZkIhWYBBQqBB2_cx5vJFfo1KdmWw-eeqb93Db8c7p0nSbZrUJh8R0cU0k7LDvAVATk1Vd1qUcDBTRO-g52Z1s4UGR98Qlw3TSQuT5rv7MrDx5phcDUjjuLxBHxBbB6zany73W-q7D8vf2dpG0syJCfF8-4MurpGlMNuW1jyPbE_FQqk_JzZRTg3kHqkLVLOA8vDnyUqqh0ZlbDDxFP1oGbE7SChqvTwSuBXndFm-MahFJa9y04UdBIIhqpg0KiA9NegqWG7oA49EMThce99QOSGwqZKUTYBDcvZzn5d1ybhpjs1eRFXXIIwVIiNcUf-_HzTcJYeJu6qhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aab458b1.mp4?token=Jg4P9UJuZkIhWYBBQqBB2_cx5vJFfo1KdmWw-eeqb93Db8c7p0nSbZrUJh8R0cU0k7LDvAVATk1Vd1qUcDBTRO-g52Z1s4UGR98Qlw3TSQuT5rv7MrDx5phcDUjjuLxBHxBbB6zany73W-q7D8vf2dpG0syJCfF8-4MurpGlMNuW1jyPbE_FQqk_JzZRTg3kHqkLVLOA8vDnyUqqh0ZlbDDxFP1oGbE7SChqvTwSuBXndFm-MahFJa9y04UdBIIhqpg0KiA9NegqWG7oA49EMThce99QOSGwqZKUTYBDcvZzn5d1ybhpjs1eRFXXIIwVIiNcUf-_HzTcJYeJu6qhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ژاپن، بسته‌بندی محصولات باید تا حد امکان با محصول واقعی داخل بسته مطابقت داشته باشد و تصاویر روی بسته نباید مصرف‌کننده را درباره شکل و اندازه محصول گمراه کند
🇯🇵
📦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/693098" target="_blank">📅 12:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsxZ7PES2fzVFmT1EUGQhui9GdlhhS4TT1cEZHlTXEw6JyEvfocGB-tNrINvcLFlLSc8bnEUfKOY2HHaWBwqlo3uymaYCRbrQn6gknUdHefuIhMPG-yluRPxvtblzVofwMVla216M7psor4O5TPmTWaNmPBYm6WYy9JuJIjI0MoPmABC4Qmv9nXEv5i5h_PTpDySYtvJA1qj_HVvWWNajbmbbVeLkwQawsvmk-aXidLl8WXWnVu9ogEgmQq9Pr8a1FpOgX_3xKEjLypwjIuw8UWh4JVZZbM6050vNnNyQpLmGo_zf3bhWfOmcxP2QEdNiQoRIr5GS5WhJ60UeNUIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متا از دو ابزار جدید رونمایی کرد که باهاشون می‌شه با کمک ⁦AI⁩ بازی ساخت:
Horizon Create⁩ و ⁦Horizon Studio⁩
🎮
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/693097" target="_blank">📅 12:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پزشکیان: آمریکا در دی‌ماه به دنبال کودتا در ایران بود و وقتی کودتا شکست خورد، به فکر حمله نظامی افتادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/693095" target="_blank">📅 12:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: قصد آمریکا حل موضع هسته‌ای نیست، بلکه براندازی جمهوری اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/693094" target="_blank">📅 12:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693092">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7efc4fe9a.mp4?token=Nu7CFDlyYOo9sAj8NE5eRhXFElbndzNq9ViovzlTkhEhNeRL3LJubX9Gm8KPtooWmj3kkuuD64nGWZgHLfnYqyR9imOq7cXBYhIEw_OAyFTvWoeJG2qE-DkdXO9Uk0rOA9wNI8ORjV8jia-_Ex2HHRV8h-yNL5DHOn15M9cXfYzmI6JwaHFM5d2sfchCKlcudj4zlLGhWAenlqxxTbvCEm9D1vJMPgGADLjX8VKR1q3oxwEafb3Qe_RYerCXg8OWgBBWGUIn405IReyZecYYwUx6b4Qm-lWQP8u-XegdXTyLHW9-9emXFubfxWM08Y66BohMNexSlP8RCotcS8hKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7efc4fe9a.mp4?token=Nu7CFDlyYOo9sAj8NE5eRhXFElbndzNq9ViovzlTkhEhNeRL3LJubX9Gm8KPtooWmj3kkuuD64nGWZgHLfnYqyR9imOq7cXBYhIEw_OAyFTvWoeJG2qE-DkdXO9Uk0rOA9wNI8ORjV8jia-_Ex2HHRV8h-yNL5DHOn15M9cXfYzmI6JwaHFM5d2sfchCKlcudj4zlLGhWAenlqxxTbvCEm9D1vJMPgGADLjX8VKR1q3oxwEafb3Qe_RYerCXg8OWgBBWGUIn405IReyZecYYwUx6b4Qm-lWQP8u-XegdXTyLHW9-9emXFubfxWM08Y66BohMNexSlP8RCotcS8hKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تهران، پس از تماس خانواده یک بیمار با اورژانس و حضور آمبولانس برای انتقال او، خودرو روشن نشد و در نهایت خانواده بیمار و همسایه‌ها برای هل دادن آمبولانس وارد عمل شدند
🚑
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/693092" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1gJUOj5HRJFyj7JAS3JEzGnAN7cI8Em1cMGtAb6QjqtNoHiYuK1D02RPuUETM1ciRXooAWA8jXxk8Ah1ON5-053NEpueRnmd60a6JoikDvZ4Peo27bK0IedJ7_lKTohQMokme4ZXSJUuNiXbGdlHjZCvDEkUQou47PD64_TSWg2kgjvopQNLm1atZGq9l0jTgC5vkbfdLjMZVl90gsiCybxLSv9oI9oOBFBaTAcUbz7vdCItqADvOVe-NHVJoz6av9xQ6pmP6UO5T_GdO4HHuZuRlgt6bGcIL85L2LMWQL3y4SugeZGWnUeG2G9de7EewVAx6vtyP-BXRmWFjsRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بابک تقوایی، خبرنگار ساکن اسرائیل، مدعی شده است که منابع اسرائیلی به او گفته‌اند؛ بیست و نه ملوان و تفنگدار دریایی آمریکا که به عنوان زخمی‌های جدید جنگ ایران معرفی شدند، در حمله ایران به یک ناو آمریکایی زخمی شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/693091" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
