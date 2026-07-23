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
<img src="https://cdn4.telesco.pe/file/arvuIXHOnT2XDcLwFDYTz8STN5xnBOM_mccJS2aPwMGONRwUZJitEb63BGHXJ3ULkSNx9vSxSWiP8TQ8X-xDaquvu3rtZ1Dykk70lpvBDJ_XWzLa6M2u_XHmQ4V3zH8yX5RFgsjkM6VMatIx9E2gE-n2FQAf0vtLA8pr8EOKAfyIBMUONcIYgkZU87QJ7Pg711PA9gA40pslsQ8f6joaxR2nSQnxXhjyKXScJv2G5u1F1hmz00NJ1sx7qhRHQKD8DZ-nPHjuAswXZY_619IcUd__BqxsFa22iV2lFxphFN93FFWRlkLn6amU4AWTsPTM0GJO5yhd7aQGhOH8mc48_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-452103">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Qho1XyXef9NEzM_QJhO2Bv-tX0K8xa7kZuGu5ia5MqyTQVAVYj8S3V6zWHfD_sKeVrOv4kaJiXVleaq0kNCiXBypYCPoDY92-qlUYsDgOVVPFxQ7Yy_GN0A_wBDzPuAFnlcxsTZksjRfplw9onAU-0ZPOpQCgtGJdWBPdJ_x0ldaI9qYQDvudFgcUGe7TDayhpgWdIxApaaYpCF6B6Wgcn5Fom-ZAchbCaf7-lb9cOrtgQ9GGZWrrLObdddGm_8_y0KFdtlYsbjnYx_YNTEFlScZZQs3oAGR5wGC-KMA9YcZ5ItjNND9sAn6sDGYAeJfW79Cddk90lMCzGZ8uopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم بزرگداشت شهید زهرا حدادعادل از طرف خانوادهٔ ایشان
◾️
پنجشنبه ۱ مرداد، ساعت ۱۷ الی ۱۹
◾️
میدان فلسطین، مسجد امام صادق علیه‌السلام  @Farsna</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/452103" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452102">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50e3811ea.mp4?token=LhXTZLrK1yPB6SGy4Zb6E-wyhEf0QMZ5H-Tmd5siSaRmwRZUSXXCwo4E9eLn3ziUopg3T85nCDaefwuIgjC1D7Rnju08CGhLpQrIE329FwoRyDxuH-j52V2UhbX5tRcncp0_A2HAWFWjp-5jJSTD-M1eKJDsf15m3tpUVzk278P9PAmAsuR_nhgLUFY_SfEoKb-haviqk9izPeAXcWiFzEjqHbnt6QRYqWTeo_33jrj83lr-YznIJL3COySsHSrpW3k-FpfMJFZYau0SXlSzGeWnBtoVNyHb3YZ9K0UEhvpaW4v8sn_QjxKT_6jYSZGsuKdV5TPaShV1lZdIGGcq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50e3811ea.mp4?token=LhXTZLrK1yPB6SGy4Zb6E-wyhEf0QMZ5H-Tmd5siSaRmwRZUSXXCwo4E9eLn3ziUopg3T85nCDaefwuIgjC1D7Rnju08CGhLpQrIE329FwoRyDxuH-j52V2UhbX5tRcncp0_A2HAWFWjp-5jJSTD-M1eKJDsf15m3tpUVzk278P9PAmAsuR_nhgLUFY_SfEoKb-haviqk9izPeAXcWiFzEjqHbnt6QRYqWTeo_33jrj83lr-YznIJL3COySsHSrpW3k-FpfMJFZYau0SXlSzGeWnBtoVNyHb3YZ9K0UEhvpaW4v8sn_QjxKT_6jYSZGsuKdV5TPaShV1lZdIGGcq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر ماهواره‌ای از حملات امروز ایران به پایگاه ملک فیصل در اردن  @Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/452102" target="_blank">📅 13:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452101">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b94d872.mp4?token=c7p15_HLeCMW7tRPqHluZhOThQhHIGTGmghs4NAVH_JDY7ajVTdqz_aO-7pM9i0-WvaRg2vs-qHr4_Q3fPV9CwbVm4sb5cfIg83iOXrUUNZAwT1s2Ve2jAZTtsPM5dFboWY4Bq9wso6AfT5f4rZ6qEdmvy3zUx6tZb1732yXwP9TQWIWAeWLaMWoJigNUMavMLw6QFP5fuS8vFvzKafGOZMjtwJD3of4bhEHrXguPJNI9TWGbYMimmX-zicAlYnf1J4sMZlwxgvaeC8l5SGZbXkit4-Ofm0GcJ_ejVFrxt2WANjnyPYXSEkGkYCHSGssInPIXWZnXGIG66L4xu0SLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b94d872.mp4?token=c7p15_HLeCMW7tRPqHluZhOThQhHIGTGmghs4NAVH_JDY7ajVTdqz_aO-7pM9i0-WvaRg2vs-qHr4_Q3fPV9CwbVm4sb5cfIg83iOXrUUNZAwT1s2Ve2jAZTtsPM5dFboWY4Bq9wso6AfT5f4rZ6qEdmvy3zUx6tZb1732yXwP9TQWIWAeWLaMWoJigNUMavMLw6QFP5fuS8vFvzKafGOZMjtwJD3of4bhEHrXguPJNI9TWGbYMimmX-zicAlYnf1J4sMZlwxgvaeC8l5SGZbXkit4-Ofm0GcJ_ejVFrxt2WANjnyPYXSEkGkYCHSGssInPIXWZnXGIG66L4xu0SLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روبوسیِ پزشکیان با نخست‌وزیر عراق  @Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/452101" target="_blank">📅 13:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452100">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=hswwmAl7QMfqE2yDgNsBHq7D6HJb8uNIqpNG1fWFynfK3lt9v_mIUzOdrBaT6jDPgZ3B8R2Kcfq02h1GcfkY-GCqQ0sLorsrqfWiN_1bCY5oTsvgao6VELRHizUpB9tYUu-uJG5fLeHia9zI5NqAUpsgWGq7-gsrw5nYqqYIsjSCoG2AWDM7Ntfew33l72BTKYxayb1UoGM65zqAr8kMqhm70a7IECFrnelMkFjNLog3WSJWKU9iE5AEQpG6VNmZNmeMZuR8yBf6CK4QKGkBdgegpAd5JRpXpYW8qim-CUF0oZE5elbMqgTalc2xxUWUXjbBan2fEAz9zbHGqt4JXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=hswwmAl7QMfqE2yDgNsBHq7D6HJb8uNIqpNG1fWFynfK3lt9v_mIUzOdrBaT6jDPgZ3B8R2Kcfq02h1GcfkY-GCqQ0sLorsrqfWiN_1bCY5oTsvgao6VELRHizUpB9tYUu-uJG5fLeHia9zI5NqAUpsgWGq7-gsrw5nYqqYIsjSCoG2AWDM7Ntfew33l72BTKYxayb1UoGM65zqAr8kMqhm70a7IECFrnelMkFjNLog3WSJWKU9iE5AEQpG6VNmZNmeMZuR8yBf6CK4QKGkBdgegpAd5JRpXpYW8qim-CUF0oZE5elbMqgTalc2xxUWUXjbBan2fEAz9zbHGqt4JXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر عراق به تهران رسید  @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/452100" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19150166b.mp4?token=LfqsDYS4UkrPe6cMZhz48jUupOWh4mAsiDpm9YjpXvZyw6eOu1Kkf5nC3nsuhs3BIUM2F2GVu2Dv8DIxtlBIVo7HGw6IzGZA1e-pg4iaVUVr3aQhgF8ZdvW7_z8VXKCGx8mn9zdjwsIAjDpS8jKe0Hae2phpgl3ViZtB8SCQ-qYsYHXght7TTxXmm9-khADwxDzoxVAnYgQSHTXlaA3pUkE_udLspWyAbKLsbc6Zt04WirMAzIrqObs7U_RH4JAOoP8rm3mii9g9C7HSI76qEjgfXdPa6h2vBZXyoi-XaJGBBoLqXg2f-06lqw_YPpE2cSAql1i9lzdn-HpKd2n9PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19150166b.mp4?token=LfqsDYS4UkrPe6cMZhz48jUupOWh4mAsiDpm9YjpXvZyw6eOu1Kkf5nC3nsuhs3BIUM2F2GVu2Dv8DIxtlBIVo7HGw6IzGZA1e-pg4iaVUVr3aQhgF8ZdvW7_z8VXKCGx8mn9zdjwsIAjDpS8jKe0Hae2phpgl3ViZtB8SCQ-qYsYHXght7TTxXmm9-khADwxDzoxVAnYgQSHTXlaA3pUkE_udLspWyAbKLsbc6Zt04WirMAzIrqObs7U_RH4JAOoP8rm3mii9g9C7HSI76qEjgfXdPa6h2vBZXyoi-XaJGBBoLqXg2f-06lqw_YPpE2cSAql1i9lzdn-HpKd2n9PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لفاظی‌ روبیو: پاسخ ترامپ به ایران «سر در برابر چشم» خواهد بود
🔹
وزیر خارجه آمریکا بر تهدید دیروز دونالد ترامپ به هدف قرار دادن زیرساخت‌های ایران که مصداق جنایت جنگی است، تأکید کرد و مدعی شد ایران در صورت ادامه روند کنونی «بهای سنگین‌تری» خواهد پرداخت.
🔹
مارکو روبیو در گفت‌وگو با خبرنگاران در حاشیه نشست آسه‌آن در مانیل توهمات دونالد ترامپ درباره درخواست ایران برای مذاکره را تکرار کرد و گفت «ایران مستقیم و غیرمستقیم، التماس می‌کند «بیایید توافق کنیم. بیایید گفت‌وگو کنیم».
🔹
وزیر خارجه آمریکا همچنین در اشاره به پیام اخیر وزیر خارجه ایران عباس عراقچی که دکترین دفاعی جمهوری اسلامی ایران را «چشم در برابر چشم» توصیف کرد و گفت «هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قاطع و قدرتمند مواجه خواهد شد»، با افتخار به ارتکاب جنایت جنگی گفت که «سیاست رئیس‌جمهور (ترامپ) یک سر در برابر یک چشم است، قرار است همین‌طور باشد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/452099" target="_blank">📅 12:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هلاکت ۲ تروریست در درگیری با مرزبانان
🔹
فرمانده مرزبانی فراجا: در درگیری مسلحانۀ مرزبانان هنگ مرزی جکیگور با گروهک تروریستی، ۲ نفر از آنان به هلاکت رسیده و مقادیری سلاح و مهمات، فتیله و چاشنی انفجاری کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/452098" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هشدار حنظله درباره تداوم حملات سایبری به سامانه‌های کنترل صنعتی آمریکا
🔹
در پی حملۀ سایبری پیچیدۀ گروه هکری «حنظله» به زیرساخت‌های فناوری عملیاتی (OT) ایالت مریلند، این گروه با صدور یک بیانیه هشداردهنده، اعلام کرد که زیرساخت‌های حیاتی آمریکا در خط مقدم حملات آینده آنها قرار دارند.
🔹
حنظله تأکید کرده که دستکاری در کنترل‌کننده‌های منطقی برنامه‌پذیر (PLC) و سامانه‌های SCADA، تنها بخشی از توانمندی‌های تهاجمی این گروه است و تهدیدات گسترده‌تری متوجه شبکه‌های آب، برق و ترابری خواهد بود.
🔹
این هشدار در حالی منتشر می‌شود که اداره تحقیقات فدرال (FBI)، اخیرا با انتشار بیانیه‌ای امنیتی اذعان کرد که بازیگران سایبری، تجهیزات صنعتی شرکت‌های Rockwell Automation، Schneider Electric و Siemens را هدف قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/452097" target="_blank">📅 12:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیک‌ترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/452096" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4e206616.mp4?token=lIqBwe7B_yunAnpfmT-QpSTzTwdUoozD2hqrVVY1-fFq2GCaHTwX78QTzmLKMxa89fVz6px4Rj8hYmEg1nd_2YiAsOe-0SBLQlif-MkdImA_LJtKYVTnc_YCIo7xa-r9-VyGfd955dPaNQa5bX_0F6MpcRbx7LPG58EgDP1SRKuMtZDlrCDbnOIfe96dkhRoDyGpiPtxwn_TW8nbq0fXygjR3OgynatGsfLn_vHP7dakQjerDLVsjzOfM0t9IAtMreriYK1tz_jOx-eD8zE6PdqPZ8DruR_cblY5tLol0Qlr1buo8S0ltI6X250GCxh5z6q7eAdrWSd34pPxDIxaHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4e206616.mp4?token=lIqBwe7B_yunAnpfmT-QpSTzTwdUoozD2hqrVVY1-fFq2GCaHTwX78QTzmLKMxa89fVz6px4Rj8hYmEg1nd_2YiAsOe-0SBLQlif-MkdImA_LJtKYVTnc_YCIo7xa-r9-VyGfd955dPaNQa5bX_0F6MpcRbx7LPG58EgDP1SRKuMtZDlrCDbnOIfe96dkhRoDyGpiPtxwn_TW8nbq0fXygjR3OgynatGsfLn_vHP7dakQjerDLVsjzOfM0t9IAtMreriYK1tz_jOx-eD8zE6PdqPZ8DruR_cblY5tLol0Qlr1buo8S0ltI6X250GCxh5z6q7eAdrWSd34pPxDIxaHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هتک حرمت مسجدالاقصی با یورش بیش از ۲۳۰۰ صهیونیست
🔹
هزاران صهیونیست از صبح امروز در دسته‌های ۱۵۰ نفری تحت حفاظت شدید نیروهای اشغالگر اسرائیل و با همراهی ایتمار بن گویر به مسجد الاقصی یورش بردند.
🔹
وزارت اوقاف اسلامی قدس اعلام کرد تا این لحظه بیش از ۲۳۰۰ شهرک‌نشین افراطی، همزمان با مناسبت ادعایی «سالروز ویرانی معبد»، به مسجد الاقصی تعرض کرده‌اند.
🔹
گروه‌های افراطی معبد هر ساله این مناسبت را به عنوان سنگ‌بنا و ایستگاهی اصلی در مسیر تشدید اقدامات علیه مسجدالاقصی قرار می‌دهند. این روزی است که این گروه‌ها تلاش می‌کنند به هر طریق ممکن حضور و قدرت خود را در میدان ثابت کنند و خواهان تغییرات گسترده در وضعیت موجود مسجد و شهر (قدس) شوند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/452092" target="_blank">📅 12:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مرز استان‌های فارس و کهگیلویه لرزید
🔹
دقایقی پیش زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۱۰ کیلومتری، حوالی بابامنیر شهری از توابع بخش ماهورمیلاتی شهرستان ممسنی در استان فارس را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/452091" target="_blank">📅 12:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8922578c34.mp4?token=Jgho7lMZBPEiyzg_MIG5pwmEs0_64XajWxqvzBQ67OHg2Hyz0FFiX5X8uLwtt7VxbSkCjw3pMYKkKxYxJKhVNjz1EMC9EuUj8ECh3hMYLW25wtFAauvan-jSLZfk7F1Dd3RbS0Cwbk7QV7xTGUx2ASjYFoLtL3BYv6gT_fc5Gs4pQ2ATF_vrbQ7dpar_ARwWa3CdL3uDn8i2FcE7gUTfjewybuZ29bQakodG107eLbahV17IQHOsVePo2gxRSUxzxTbuQ65MfmMmCh11wYWZ1MtvxU_MI2Ftg7-Y99fXyPYmcUOWfrGCj28vVvPXyYsdN5Kg1HIqW4zzzan9664PrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8922578c34.mp4?token=Jgho7lMZBPEiyzg_MIG5pwmEs0_64XajWxqvzBQ67OHg2Hyz0FFiX5X8uLwtt7VxbSkCjw3pMYKkKxYxJKhVNjz1EMC9EuUj8ECh3hMYLW25wtFAauvan-jSLZfk7F1Dd3RbS0Cwbk7QV7xTGUx2ASjYFoLtL3BYv6gT_fc5Gs4pQ2ATF_vrbQ7dpar_ARwWa3CdL3uDn8i2FcE7gUTfjewybuZ29bQakodG107eLbahV17IQHOsVePo2gxRSUxzxTbuQ65MfmMmCh11wYWZ1MtvxU_MI2Ftg7-Y99fXyPYmcUOWfrGCj28vVvPXyYsdN5Kg1HIqW4zzzan9664PrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر عراق به تهران رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/452090" target="_blank">📅 11:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452089">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1328df24d9.mp4?token=U06jcYwCA8Exv5R_-E4prB0hlFzLLTWTAtiVNs0gIB-mY-kCjmeJMBiRf97ZiD2xT_43TwEtAdyo2qxtduJxry5a9DLabCVHk27kqvBJaOA0fo8GI-FHnythloLYabPulgjhMdTJE_SvO1Ay4qnlBlYc5-0QxjhaYJSL0a09wm6acuHh92DOnMu-yYyHSu6ntuYFXLoRTILQBa29UTi3apQNRxPSEfxU5qTdDNPrnTQAgYa6CJZ9cZUkxlLwIXmB2rd1apvrqJGUcgHIEDi7A0BskrgqfcQAmDVNhNWxdUFJQC6Mztcy1g9K3pj--dkVIa5VMINIw4wKlOrZB8S8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1328df24d9.mp4?token=U06jcYwCA8Exv5R_-E4prB0hlFzLLTWTAtiVNs0gIB-mY-kCjmeJMBiRf97ZiD2xT_43TwEtAdyo2qxtduJxry5a9DLabCVHk27kqvBJaOA0fo8GI-FHnythloLYabPulgjhMdTJE_SvO1Ay4qnlBlYc5-0QxjhaYJSL0a09wm6acuHh92DOnMu-yYyHSu6ntuYFXLoRTILQBa29UTi3apQNRxPSEfxU5qTdDNPrnTQAgYa6CJZ9cZUkxlLwIXmB2rd1apvrqJGUcgHIEDi7A0BskrgqfcQAmDVNhNWxdUFJQC6Mztcy1g9K3pj--dkVIa5VMINIw4wKlOrZB8S8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقایقی پیش صدای چند انفجار در کنارک شنیده شد
.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452089" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA40rg22dc-yB9qQ1esuXy2w8l_eqWhljx8ar0d9LgM1t3__ODHuTHsxqW9mZoPPrgnf-yTMI9KrP46Xhgynkw0nuTFSBkoZYT6-fFg060AwmlaafZdAQbOsTALb6DbQgpW9zyAPLZa2aVDei0iRu0iraG2dxMZM_Od0VrV3c0Fcjt-GkivxZPUzKANZW_rXMuytPFvdkCU2iYWpXxqiWzC8qr9a_koiTmLxpP-cK5OKtFJdDfkRCCwLv8aVPUD87MGIqiTCTgp0d1q1FFrZKzNKiKnzMJtOuRryotFGA6cInGCkEzWKZa4KZSL2jI4_2oA-qQuvQxvKrCC6FIh9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت از ۹۷ دلار عبور کرد
.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452088" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452087">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4r3GF-MpY6hmtra6m3sRHJ5EiUTFgqQfCCBJV5dgykh9DCWeEJhRId56Pv9MLBrK15niqNSoGiQEvHdLj_flX6ccTPvzvG5rR9Wy-bL0sGRljgMFRKkXpAsqVeA9Nq_vHuYJtHeCm7tCC7_xlXEEKu4P4y7ZjPQ_xkSWS1KbW3Fi_sJs5GnrLIEu9LXOoPcgQGH-ASTVb1iAr30rIfvxoI3V0P-R2R3JU8ERzv5pE-gyZwyDiE_td3BFxA74jyif2fRtdu6h7uj3MW-JeGCXi28cixUzT1OLH1_6QLmprZa1T59ckuXu3ZtuukRcdi9t1vX4XBR5-7UNRmiWcQsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌گروهی امید‌های ایران با چین، امارات و کره‌شمالی
🔹
قرعه‌کشی مسابقات فوتبال مردان بازی‌های آسیایی ناگویا ۲۰۲۶ برگزار شد و تیم ملی امید ایران در گروه B با تیم‌های چین، امارات و کره‌شمالی هم‌گروه شد.
🔹
هدایت تیم ملی امید ایران برعهدۀ حسین عبدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452087" target="_blank">📅 10:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452086">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxwAhAjvd6QzYCvTNGq8Dw7NOlHfe4CY8_6u3fKeRuH92BJNl-pgEiIGHtfraUdknFX4B9mB8ayl_SrPTGw7sWScHfSpTWILxi-vA5REHhC2tkMthzT58_JSEAYxgXfNb4bIpCzyn0UTxJRleG1NHwB7981MeAyg4kMuA3R3I_-hWsYgK8wxnNFLnTGZHYVW8060R0wiqbWZJW2QoNRp7YemPop6SFrRsYqhJpzsTSBZebHuJqtRqSRpHS0uVve8CQ1D-MIastn1Ap7HGemBTTDC_y1PxZawhh6pZ2IopNu2egKX1zzKleS6LA12j2rWt4lriyn1qf9nz8kvAz2i8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فردوسی‌پور را باز کنید
🔹
«من را در صداوسیما ناجوانمردانه کنار گذاشتند. از چه می‌ترسید که اجازه نمی‌دهید کار کنم؟ من بله‌قربان‌گو نمی‌شوم، حتی اگر بخواهید مرا بازداشت کنید.» این جملات را عادل فردوسی‌پور پس از بسته‌شدن وبگاه «فوتبال ۳۶۰» در برنامهٔ ویژهٔ…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452086" target="_blank">📅 10:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcJNYHOhLRw8Mb-IcBfSvzccdDyNOz6_PMJSnCHM9ZxDK5th42lywGs1msIMFjNS_RxxOzCotzVO1XzmCYDpp3bsEZrbBGjrnLxxQ2YXywV9dXWvpRoWnujFyuk3siAsKve3EF05kVSTs1zI7bXvRtQYe7X3KUlnhv9Ohqrug74KHuei3_YtbllCyRGd9kc5o0-EiWRbbD3yDG5xRLSO_f1yuOJRIp4OVs13FSY6Y1jsIK0HCt0gJXTWscn5t47kNWDGrEWofEdB1rtDsegtWjCrRHzUn9IiMZeV7ByR5KAPZqphNaogC1qTbXSPr3WRB2CKiOGt8i0_4i8bi0u42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMO4ChfE97vHh2WcZwx9ZW-GyEYSsVDeEV5vyUT68ON9sjJ1HscsCKG2B1VbY_LPiNMUd0f4DOzE1ECcMqGoHh2WaFe-ljy3ZTfW9C9a2mFaiV3RhlfqJYT8UXjM5h_egzsMaovY5RB7IskmA9amQsFlJCclGOKaIhalVDozLEu-mpnpemUEXn-HnKdlUl4Jrgz4CusfQ08UKxyb3xMtVEg4LWxfnmV85WZ5xY1uLqgt600qxA_w9jKKRcICtqXXx6EWxxF4bnXtQJK69K5aXOt6Fajd8VrKNTBNFgsxLYi3dK9BFIYgMNava1jD3RjIxcAUFbppavo-Br4ycqnzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBtyBBqB87JQ5r5IjFmL2_MUxBOeME3vIn1KPDCfFVu4nabCGp8iGtSg823WyGgyFPwDATC4M7FMN6v-oEENQ1mo2mcJjj4qAHKT18k-QwuIhM6CEEzdua1VGWPB8XLpJEvbRBO3JSUo3ZPQSNndB_l_rrgKDa1VVDVDUASBj7UGANmYvYtJh5hCTDib7UNtfymQWAhbwLXEFaaX0fU4ckW29rrwN6F8WFD_NVykR3G1uCnqmZjUINHIA5xDndJD3p-g64EZjR-5ib3_N2plRl4WpZixRnsMSa1pROZjaJfXnnbTRPzKFcXs2n1clCrzCSLzjrJwbN_FlU41Owk3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyFL1f6Ka3EYfF4dt53Wj_cqYAfc-UGaOt9dv8c6UgADqQk8R5n5qDdsPQOk7TJvYg8zj5MOGjU1trHxVOKucHjPi1uCjfwL3iz0MMz83ykkriJNYIY7B-2sJwTaFnMWqbDKF3fVUIf662dkYrRbHZTfVpTQYmGqEMPj8--DBWenstsRyM6ho6B4ozT4rmE_5b99vkGMUGqpOQn-Pr4YChbmc7P65hnMtZKWc47RIEtPCdzf_1QYfxnR-OCz5xzWwQ0UBeSvbe-1vmcQHdAeSvj0YyxNFVxjpDg3LKKMDTlcc9pYiYy3xGvElvtjdQwzjhsev1iGZ-k6tzhuleueow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmntHuANTfE7YEl9zfGCOIhIA6Tq56sPVV9c5KOJ8eNmSccQpNFSDedbbcdVFb-zQEafBTyZInpeBdytqzpewajWjFXk_QwZpYvoDU0P-Sn6iJd-F6SF9OvzmOvmNhZvSLZbwpHCfR1_qbyAWTzdHIKUIhBF1sF5_Agp3Tnh0ZE2qt_xUA1F1WA-teFTXYRrv9mrvl-PmvYkffJQq4y9ey6JgFaqErVBkNSvFnYr_uU-1rVjpd4yBttPD-V06wcATLBMFx46ZAyaSudxKo68JHNXlQWyNKHXfO3SclTt2vqcFCG10aY29tFW4Y8CmYEuYcc82vle7K_0Q5Z0Kus0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG7rgPk2pjTQhYP4sFKDPk_0gvsVJ1O0uTl07cQqxRKN3GTWzS73MmVPo_-2vDSJXjWaDSjwwz7gXwpA2OLQl7acIOv7boMy4g81ARQCOqh79OMlEhRAzjvUuIPlYc2Tvpz8zQb2wVBxp3DPWWJRnhnd46gf_AE5vU1VLG0_xHc2s8p9jwkTx_wQ-Foe5QBey1gpgIWnRCdUy0fwIG9NCYE3fPiq8lHiUd5TIAjVztKS01ya2hDaT_34zN4xLSRYJrguBhPgoM-seEVnI-gBG_f4ltV4JcQD6MiiDmEnBv_fL0TpzZDreJFsN6QjSNF21mVV-glyBjkOniTHRL_M_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMK6JmvAOu5qk1VsjtwUIaE2prokalBGkhnci91iXDLEcajVWQSotAtE4Gq1i35KXjwOKO3bk5I05IjnkNi80GJWobIiZxJXG38ysraScm7ua_5wMMWeXLC7O3Pd4Hw5M_a9Y6t3U39A3uZvCfymg1_agtIgbo9t33nIzeGRhtH5kXxZwiYTvisOTlDh3YDr2PuC0SzsnE32Y_ytaOTrAgaulan37yHgVLyHbJ1P_X6zoqRcWDaQTFtKPw2op1hzULJp473tpLB2YzlvxzuHRytcA3va8vcUXZ9aGC_h8iVMc8FDxVR8XI6qWFOdpltOAkdkxaGnyEOsWuO9kSFW0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
با حضور اکثریت سهامداران رقم خورد
✅
تصویب صورت‌های مالی سال ۱۴۰۴ بانک صادرات ایران در مجمع عمومی
🔹
مجمع عمومی عادی سالانه بانک صادرات ایران با حضور اکثریت سهامداران برگزار شد و صورت‌های مالی منتهی به پایان اسفندماه ۱۴۰۴ به اتفاق آرا به تصویب رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452079" target="_blank">📅 10:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw5KQtrEuGL1afjPGrEu5-tXF_9mJK-KsKpJe2rRWfyPQLu63qSbODGjA4s_glPzKAfnIVaHmzgbjdz7bqvgU5t2ZCGMy0DV-C9azsS1g5YCifdFtHxIkNCfPYkpHKbAlsyRtXQQyQr0UwUYw6XgF8qeIWQvScqioBIlUAnKHqcDWzlDPuQtBGop26piIEJ4Bl-EpTSrTAJXTUdeS0W604_VcECD7V1Kt-BBA6YgR66hCs5a6De-aVcs16UeymZbpo7nGXLtAMm8--ARHFq5sdso6bNGK7Sn2Cv4tJAFzJo7uihZNvWPWsKSQ4yhFi0K4ATqoerEMFMSBFzt95WtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
به مناسبت اربعین حسینی و ایام شهادت امام رضا (ع)، سدن پوش برگزار می‌کند:
طرح فردوس – نذر حجاب
✨
چادر حریر اسود با قیمت نذر (بهای تمام شده، بدون سود)
چاپ رایگان طرح‌های مفهومی روی تیشرت
✨
هر تیشرت با هر طرحی که دوست دارید، در محل چاپ می‌شود
محصولات ارائه‌شده در این رویداد:
▪️
چادر حریر اسود نذرحجاب
👕
تیشرت‌های مفهومی
🧕
انواع عبا (بزرگسال و نوجوان)
▪️
انواع شومیز مناسب اربعین
🧴
انواع محصولات ارگانیک و بهداشتی
📍
آدرس
: تهران، نازی‌آباد، خیابان بابایی، بعد از کوچه ترابی، پاساژ زمرد، طبقه همکف، پلاک ۱۴ و ۱۵
📅
تاریخ
: ۳۱ تیر تا ۲۲ مرداد
🕙
ساعت
: ۱۰ تا ۲۱
✅
ایران‌تن | واحد رویداد‌های سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452078" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/452077" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3u2t6jFgfj8PJgbwZaffkrwZNtQKvUwYtLsHmOX7EjTXJCWbD89WPFyk9fC_yibjqpNPvyYLgVn-O32mTPf1ywr1g7E1t9YZUv8NvizRDQD35Zi6uEy2XBF2jV_XbtVd1w0uQrOtcoOXcm8S5IpswWnA7VUu-JdS9BjoLyVJogK4N8pd_YkzFfIAAM5-XFNw_qwftL3vtOYSdhEvjtBJJMGWsboeu1cN1eCDrUuWo_FQ2GGd33I9PaqFIapsx1AETcs7eYrFcXECF4CoAvUXqpk5g4xf0b-TbFtU9eWmdMeUFtqWK_fvQZaBJOetHQzE5xrAi8lMbmb1Z8RfdCOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد توکلی، عضو مجمع تشخیص مصلحت نظام درگذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452076" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVj-tFTLrwxo3j4lOj5dXGcwK8mcV-VpQlq7zaa75GsmDRHZtjRtOoWREt1K1fW4Auh1tIFGnIvugnwqm04UzdKtRuVcD4o6aOno4r_UyUacoSJ_nWt0-IYqbOfbhzCPAotcW92K3TAXU8fKR1RjZF0peppcAJicIWy7HD5dwNdhpANcbxs9RqFnzx4JEWHjr36n9FIcBWsHzk0pcVFeNqk3AJxC0pxgFNV9QkuhfPHEYkXLHJu6xlSpYiwPEKYd0g5Q5Ur17XTTu3Ft4RCwp-L9I4CUsTOfjIGOrGpRmrnx-mshGAD7BKCRJJxdWZx_7U518ZEjU29qgOoler_vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سردار قاآنی: رژیم صهیونیستی باید بپذیرد که با وجود همۀ جنایت‌‌ها نتوانسته مقاومت را متوقف کند
🔹
پیام سردار قاآنی درپی انتخاب خلیل الحیه به‌عنوان رئیس دفتر سیاسی حماس: عرض تبریک انتخاب دکتر خلیل الحیه به عنوان رئیس دفتر سیاسی حماس، باید این انتخاب را به شخصیت‌های…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452075" target="_blank">📅 09:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEnneJjOL2SMIOdhEzmS4pm9IdvlQefFLuiHpfrMdkHAZX2bzgSZzngDIr9DQnTuU5XTRD7ni6NClJ9OcMJ0yWfiVcaToJkZP7Fx78L3tGamaBKvP-TEJFSl6kr1PQUH2em8yPOgS-psf2ITrwGBwiRhoBDy7K1LITPopzVX9VCTYwLPonGtdeelyPZ5uvY59zws4bOQrYHFkuh36lJFPF9qyqHqrMbHB_ZBXuVsuAzC4SY2gr31FHLClEh1G4y3Opf0lCb908EqLE8X5KJCbgWoiIdByAavrYxD6bcoeneuUVViC41WzZyCrBtG5Pf8tdziYvcqUXpQ-6X810FSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرۀ کد اضطراری توسط آواکس در آسمان عربستان
🔹
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) نیروی هوایی آمریکا پس از ساعت‌ها فعالیت بر فراز شرق عربستان و در نزدیکی قطر و بحرین، بامداد امروز کد اضطراری ۷۷۰۰ را مخابره کرد و مسیر خود را به‌سمت پایگاه شاهزاده سلطان در عربستان سعودی تغییر داد.
🔹
مخابرۀ کد اضطراری ۷۷۰۰ به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452074" target="_blank">📅 09:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452073">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTTd4_R9t12ZqGT4FMUV1ebVDBeY2M86koIvCcFD8te0Sy6dMLaUJ_S9hiXCzUBFauBT3WKon9bjqkY8QsfpSivoCbXluV6RZCOtqt6ZiqdyMv46xlYiIqP1QVptwBc2n5_t-Q6G4uQ-APh5_7yJ2Q5zbdp-ddDtZjHlo9eeHAwdVMC5_5gYCU8ytfMCsMdBZXtvToa-402y9qSK_zq_s20LYVpt-IAqLdXYQZAfs5Lh4TA3CtaRXZSBbgF7iKvKaOr8_TXCW64iei0O-Vg_6rBjZ_vQoggmKYzNJGk-VwCPf4Ui0IcXQrsqHbzHrExcBXeuaAeszefomVkGwMG3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید معاون اجرایی رئیس‌جمهور از پل B1
🔹
این پل که می‌توانست ۳۰ درصد از ترافیک تهران و کرج را کاهش دهد در جنگ رمضان مورد حملۀ دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452073" target="_blank">📅 09:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452072">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452072" target="_blank">📅 09:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خطر سیلاب و طغیان رودخانه‌ها در ۴ استان
🔹
سازمان مدیریت بحران کشور: با توجه فعالیت سامانۀ بارشی از امروز تا شنبه هشدار سطح نارنجی در سیستان‌وبلوچستان، هرمزگان، کرمان و فارس صادر شده.
🔹
احتمال وقوع سیلاب، طغیان رودخانه‌های فصلی، سقوط سنگ از ارتفاعات، شکستن درختان کهنسال و آسیب به محصولات کشاورزی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452071" target="_blank">📅 08:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452070">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حملۀ هوایی دشمن آمریکایی به شهرستان کیار
🔹
معاون امنیتی استاندار چهارمحال‌وبختیاری: بامداد امروز در پی حملۀ تجاوزکارانۀ دشمن آمریکایی، نقطه‌ای در شهرستان کیار هدف حملۀ هوایی قرار گرفت. حادثه خسارت جانی نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452070" target="_blank">📅 08:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452069">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">احتمال صدای انفجارهای کنترل‌شده در دزفول
🔹
روابط‌عمومی فرمانداری شهرستان دزفول: از ساعت ۹ صبح تا ۱۱ امروز، انفجارات کنترل‌شدۀ ناشی از امحای مهمات توسط نیروهای مسلح در برخی از نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452069" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452068">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bffd69d7.mp4?token=gkUfFUqEe6kaBMmePgi703y4e5FJR2EnhneRgKboQ7fipz1BYzpYTI5fdmt9Mgy1Y6nggvTxkGSRb75tTdjQ3mAljobH894v-W3O7y-PnRYW7pPC3XtlqV0fCe9fYgLvvYv3-Yg1_yzzAKJt_Mvzie8so3Plh9zACPwCMYDbOejZq7zK6dkKMbejC_I4yT8E99YQbGxEAHdr-OMjtLTXEl71UaMoCr85PbsVcHjtS7ho-TB5p3onsrgUJGDN4nBXzCJdqtJDAc3wzvYrLp19VDbQABO1YCIDI8eNyhwYU60mrxl1H3oa3bc3evZ90UgfGAHrw-hBhypkZO0_0jGkZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bffd69d7.mp4?token=gkUfFUqEe6kaBMmePgi703y4e5FJR2EnhneRgKboQ7fipz1BYzpYTI5fdmt9Mgy1Y6nggvTxkGSRb75tTdjQ3mAljobH894v-W3O7y-PnRYW7pPC3XtlqV0fCe9fYgLvvYv3-Yg1_yzzAKJt_Mvzie8so3Plh9zACPwCMYDbOejZq7zK6dkKMbejC_I4yT8E99YQbGxEAHdr-OMjtLTXEl71UaMoCr85PbsVcHjtS7ho-TB5p3onsrgUJGDN4nBXzCJdqtJDAc3wzvYrLp19VDbQABO1YCIDI8eNyhwYU60mrxl1H3oa3bc3evZ90UgfGAHrw-hBhypkZO0_0jGkZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش ۱۲۰ متری آبشار «کردیت» در دل زاگرس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452068" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452067">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a0fec006.mp4?token=Ab8Vyxf4YUWDTlBFPbiq52Iw800YFQPXsCDsw2mIHGn_xFWT_YjXbjPmOoD0HNfD5ks6P7U-37BlKFwRv9PyZMW0bu4ShEvL8dmQWyMJySK1_78eqb6VaQRfggJJ3Vx-vha6wCIXIep8SgX2SvrG4D6sj1zpYn9zxp3su8S0ITUI2sP5I8ufoN5xljyJE7oDiGuBQWZk229rNYxi3TfKPxZ-pJs1WpFyG2FMbSQTL4nO2GwsxjLA6EKluuv09jj3QTHzFqKVR_zrPsXy3oinPhAO0Fh-kE56PucqxxNB59syk8eMr7mRDl3Hkjrq6syTFvH-ZPzXpQzYR7Ci2bCeBjEfU3tj3_s_XzHUzhHnGd5qLQdE-XFeo-KGIXXOcZ5Tk3-NJyMnD9QXJpVlqNIdshzoDUDjJzNOxWNYaFvkdzJR2r0tccX-EeYXxYknSDbre7izjILS1mu8a6UJlTExk74J4XQNvdP5YJKFIv0CstHZrTR3P88M0r97nY18N6sY1omCsYkJMb0XNNyiZIKhH_nA0Ao2iX98t0JmfKS2PEzvO1abZgxot7P-LKZplaoVEgZisJX6lIu8DxP5cqBvTP_PlZXhlF8UjkJym93lDYBlJ557PEheMozDV_5MnyWv3fGjtWWrH7_o6H3pnXfSjgJvyaOWK0eH1sRf6FgXgb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a0fec006.mp4?token=Ab8Vyxf4YUWDTlBFPbiq52Iw800YFQPXsCDsw2mIHGn_xFWT_YjXbjPmOoD0HNfD5ks6P7U-37BlKFwRv9PyZMW0bu4ShEvL8dmQWyMJySK1_78eqb6VaQRfggJJ3Vx-vha6wCIXIep8SgX2SvrG4D6sj1zpYn9zxp3su8S0ITUI2sP5I8ufoN5xljyJE7oDiGuBQWZk229rNYxi3TfKPxZ-pJs1WpFyG2FMbSQTL4nO2GwsxjLA6EKluuv09jj3QTHzFqKVR_zrPsXy3oinPhAO0Fh-kE56PucqxxNB59syk8eMr7mRDl3Hkjrq6syTFvH-ZPzXpQzYR7Ci2bCeBjEfU3tj3_s_XzHUzhHnGd5qLQdE-XFeo-KGIXXOcZ5Tk3-NJyMnD9QXJpVlqNIdshzoDUDjJzNOxWNYaFvkdzJR2r0tccX-EeYXxYknSDbre7izjILS1mu8a6UJlTExk74J4XQNvdP5YJKFIv0CstHZrTR3P88M0r97nY18N6sY1omCsYkJMb0XNNyiZIKhH_nA0Ao2iX98t0JmfKS2PEzvO1abZgxot7P-LKZplaoVEgZisJX6lIu8DxP5cqBvTP_PlZXhlF8UjkJym93lDYBlJ557PEheMozDV_5MnyWv3fGjtWWrH7_o6H3pnXfSjgJvyaOWK0eH1sRf6FgXgb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت زائران اربعین از جنوب عراق استان ذی‌قار شهر ناصریه به‌سمت کربلا
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452067" target="_blank">📅 08:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5783ddb53.mp4?token=nudY5Z_02z_EZMcuDIzWrpH7FkIbpktT0lw6UGHjBjKOlZbaSGHlCPBjmaPNo4M2SQz-yfMyLUGYNiHMzrRapJEcKGTEPXOibtxuZy1w_7dSVgC5qtpSdnUxeirgRQRGzDthECSV81AOzsAzHfX2hYEERl_k9ByjmWQigHbCyMNMY1CMfh9KL0pSgoPOl0YG07P-q8Ds7mC_NT2aUKoskYORcfaXbdworUIiApMhV5FPvw311DQUxYD1Klpcj6WiBWAJ7JucQ8BuvPgh_Ft_gPqK_cm84-lP6k6MB_GVCRyxV8xwcFoTKmGet8AsuKe95Hv1xh0jrkzA4_LqYCl22A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5783ddb53.mp4?token=nudY5Z_02z_EZMcuDIzWrpH7FkIbpktT0lw6UGHjBjKOlZbaSGHlCPBjmaPNo4M2SQz-yfMyLUGYNiHMzrRapJEcKGTEPXOibtxuZy1w_7dSVgC5qtpSdnUxeirgRQRGzDthECSV81AOzsAzHfX2hYEERl_k9ByjmWQigHbCyMNMY1CMfh9KL0pSgoPOl0YG07P-q8Ds7mC_NT2aUKoskYORcfaXbdworUIiApMhV5FPvw311DQUxYD1Klpcj6WiBWAJ7JucQ8BuvPgh_Ft_gPqK_cm84-lP6k6MB_GVCRyxV8xwcFoTKmGet8AsuKe95Hv1xh0jrkzA4_LqYCl22A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
🔹
روابط‌عمومی ارتش: در پاسخ به ادامۀ گستاخی‌ها و تجاوزات دشمن خبیث به کشورمان، ارتش ایران  در مرحلۀ بیست‌وسوم عملیات صاعقه، ساعاتی قبل محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک‌کش آمریکا در پایگاه الدوحه، مخازن سوخت در پایگاه علی‌السالم و انبار مهمات در اردوگاه عریفجان کویت را هدف حملات پرحجم پهپادهای انهدامی خود قرار داد.
🔹
ارتش ایران با تاکید بر عظمت و استواری ایران در مصاف با شقی‌ترین دشمن بشریت، تاکید کرد : لازمۀ حفظ این اقتدار، تقویت اتحاد و هم‌افزایی و پایبندی به شعار همۀ ایران برای ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452066" target="_blank">📅 08:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452064">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ9 آمریکا در پایگاه هوایی علی السالم را مورد حمله پهپادی قرار داده و منهدم کردند.
🔹
برادران شما همچنین محل اسکان نیروهای آمریکایی، دو آشیانه بالگردها در پادگان العدیری را مورد تهاجم قرار داده و ضمن کشته و مجروح کردن تعدادی از نیروهای متجاوز، به چندین فروند بالگرد و پهپاد، خسارت سنگینی وارد آوردند.
🔹
رزمندگان همچنین در پاسخ به حملات آمریکا به دکل‌های مخابراتی در ایران، یک دکل مخابراتی را هدف قرار دادند.
🔹
گاهی گفته می‌شود ایران با حملات خود استقلال، تمامیت ارضی و سیادت کشورها را هتک کرده، درحالی که چنین قضاوتی کاملاً نادرست است. از نظر ما استقلال، تمامیت ارضی و سیادت دولت شما کاملاً محترم است.
🔹
پایگاه آمریکایی در کشورها چگونه جایی است؟، جایی که بدون کنترل مرزبانی شما آمریکایی‌ها و هر کسی که آنها بخواهند، گاهی زندانیانی از کشورهای دیگر به آنجا وارد میشوند و خارج میشوند، دژبان ارتش آمریکا انضباط آنجا را برقرار می کند نه دژبان ارتش شما، قاضی آمریکایی در مورد جنایاتی که آنجا رخ میدهد حکم می کند نه قاضی شما، قانون آمریکایی در آنجا حاکم است نه قانون شما، نه فقط نظامیان شما حتی وزیر دفاع شما بدون اجازه دژبان آمریکا حق ورود به آنجا را ندارد.
🔹
پس این آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است و نه ما. ما داریم به زمین هایی که توسط ارتش آمریکا اشغال شده حمله می کنیم. ارتشی که جز جنایت هیچ کاری بلد نیست.
🔹
در روز گذشته، مردم داغدار میناب باقی مانده قطعات اجساد فرزندان دانش آموز خودشان را که در جستجوی زیر آوارها کشف شده بود را، تشییع و به اجساد آنها در قبور ملحق کردند. آنها ۱۶۸ دانش آموز بودند که روز اول این جنگ در حمله ارتش کودک‌کش آمریکا به شهادت رسیدند و این جنایت ها ادامه دارد و بخشی از آن با استفاده از پایگاه های آمریکا در خاک کویت صورت می گیرد و این حق قانونی و شرعی و منطقی ماست که متجاوز به کشورمان و قاتل فرزندانمان را از هر جایی که حمله می‌کند هدف قرار دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452064" target="_blank">📅 08:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452063">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UthR7Xrp6hPKM2HdWS-hmG-mOCPPsiD8jtLmnwBEhmhpkBy5Gg5H5dCnQW9-3N14SZ1xZUJhnI414bKqOe644DGoYNxEZhbilyZsi2XtqPTgEIC5fojavIsIF_4vQ3g9oM5XGXpGjgUQvQ5H4KqglX_sLQboVihr40msTnBQ41x6Jp4EIlkuNUvkFqkSHsQtHgJaiMw7vyzrVUdAs58HEVEEVPw9Qa9YsoUap5V7ts0bHvM3-IpKvD1jrm1VRAXWkk5kqO3d19wy4e_1MHzeO4TxnAGZCphPyNz11KZpLLCeH8S5Ev2UZwegY6S1sSZuWU_xe8miqP7BHp8oTEBz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت در چندقدمی ۳ رقمی شدن
🔹
به‌دنبال تنش‌ها در تنگۀ هرمز و باب‌المندب، نفت خام برنت به بالاترین سطح شش هفتۀ اخیر خود یعنی بالای ۹۶ دلار در هر بشکه رسید.
🔹
همزمان ذخایر نفت آمریکا طبق آمار هفتۀ قبل به کمتر از ۳۱۱ میلیون بشکه رسید که کمترین میزان در نیم قرن گذشته است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452063" target="_blank">📅 07:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2NT5JyoLQY-DP1doWrAo1WC9hEI6MbGUiR5_s1xbAP55Qrb1wiOGmnDqUdGz1hXf_kexJsu_2tjcjOgfVptkcONVJYBOKnoZd8eS4xm7lzks9ITcqQ0MZVgPpBgU349F9TLINyH-hpKZ9x8Vvz_gGUtVZor3n1Yh9luxc7DxVJXZ2ZgHul_OAahXIYCeSBYwOx8zLYLLf3lYoKv6PV848OC9HC5q3D2v3EXNY-GavbAqbMhOhcR7V0hFTDw-V9cGxNinX2ckCYrDlrQfz3htbmoMNaUSjrAbIsyOaWQSUIhfZ4koIVL-R00S7BWQH_gSBS2-EGFNmUAeFTDUa8wTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنایع تا دوماه قطعی برق ندارند
🔹
با دستور رئیس‌جمهور و با هدف جلوگیری از توقف تولید و حفظ اشتغال، برق صنایع در مرداد و شهریور قطع نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452062" target="_blank">📅 07:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452061">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
حملۀ دشمن به شناورهای نجات دریایی در آبهای هرمزگان
🔹
اداره‌کل بنادر و دریانوردی هرمزگان: بامداد امروز دو فروند شناور جست‌وجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در اقدامی خصمانه از سوی دشمن آمریکایی-صهیونیستی مورد اصابت قرار گرفته و آسیب‌های جدی دیدند.
🔹
مأموریت این شناورها صرفاً امدادی و انسان‌دوستانه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452061" target="_blank">📅 06:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452060">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
یمن: ۲ نفت‌کش عربستان را هدف قرار دادیم
🔹
سخنگوی نیروهای مسلح یمن: با اجرای یک عملیات نظامی ویژه، ۲ نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را به‌دلیل نقض دستور ممنوعیت تردد کشتی‌های عربستان، هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452060" target="_blank">📅 06:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB9kPlHxNOBfUC0k1NTrzJRgtmiv-bvUxMVSiiXGLmc8SCvvdMxxBhcR2PrTCtuLThUfKVpHnNs78WGyVTLuNaxOetp3Ub1SjjdExzjW8M5yYCmL5qnV0i1GdVU4Nb2iuJLlTS1sJoaAUQGmCuLAIHHMwyl4UyhaxAC--yMSLbCEzrH7D_C5ImHtsCVKZwrmvQ_lDBeagcYBLPrdRCh8NGOAqZZqMQ6cSCXSYkqQmM58HwruxNsiWrJjWuFMlfmxvcUv2kUOsjzoVusLmcmawaP2nnmiW0yE30OjzRqcrEm4XpEEHj6roVMpCCcSddaj5lazk3PRpeOBR8dOI5NG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت ۹ کشتی از باب‌المندب پس از محاصرۀ یمن
🔹
خبرگزاری فرانسه: بعد از اعلام محاصرۀ عربستان سعودی توسط یمن، ۹ کشتی مسیر عبوری خود از تنگۀ باب‌المندب را تغییر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/452059" target="_blank">📅 06:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
حملۀ دشمن به حوالی اسلام‌آباد غرب
🔴
فرماندار شهرستان اسلام آباد: حوالی ساعت ۳:۴۰ بامداد امروز، در اثر حمله نیروهای تروریست آمریکا دو انفجار در اطراف شهرستان اسلام‌آباد غرب رخ داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452058" target="_blank">📅 06:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452057">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
شهادت ۲ نفر در حمله به مرز شلمچه
🔹
معاون استانداری خوزستان: تاکنون ۲ نفر در حملۀ دشمن تروریستی آمریکا به مرز شلمچه به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/452057" target="_blank">📅 04:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452056">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۲ انفجار در بوشهر
🔹
دقایقی قبل مردم بوشهر صدای ۲ انفجار از حوالی بوشهر شنیدند.  @Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/452056" target="_blank">📅 04:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
شهادت ۲ نفر در حمله به مرز شلمچه
🔹
معاون استانداری خوزستان: تاکنون ۲ نفر در حملۀ دشمن تروریستی آمریکا به مرز شلمچه به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452055" target="_blank">📅 04:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452054">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
حملۀ موشکی به اطراف شهر اندیمشک
🔹
معاون استاندار خوزستان: یک نقطه در اطراف شهر اندیمشک مورد حملۀ موشکی دشمن تروریستی آمریکا قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452054" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452053">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌ معاون استاندار خوزستان: دقایقی پیش اطراف پایانۀ مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/452053" target="_blank">📅 03:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452052">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
تکمیلی؛ رسانه‌های عراقی: آمریکا به محل استراحت پلیس ایران در گذرگاه مرزی شلمچه حمله کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452052" target="_blank">📅 03:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452051">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a87e9abd4.mp4?token=nSrNlaDuFBRxNO5VAM-vQHxU2_kjH1b2Rszw-ighzG3jyN8XM_3LnNwpj6imGTdJUzM8ELSmVKg07LNfZaeTFR5Le8ziKxToyq6_buDB_VTnjK0C5Jnnb-NtmY0W7xknbo2YVPEYnT660qYWEmK40nuJ3rsNTngz5th7ohQb0_hEfI70qG370l1c2JC9cyb0cKqHlgHsePMIgs87pzc3NTDNVc7S0Zjv4nbtA9GbcNUVD4LxdlHAebdDWC1NZXXnrF1PD_2NWEe9l1x8y8aaFjF8NAc10UtDXwPtYgg0PsmBV_YNTTCA-GWC3lxx1Nnbb9h3qyNkTOPGM6HU7liuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a87e9abd4.mp4?token=nSrNlaDuFBRxNO5VAM-vQHxU2_kjH1b2Rszw-ighzG3jyN8XM_3LnNwpj6imGTdJUzM8ELSmVKg07LNfZaeTFR5Le8ziKxToyq6_buDB_VTnjK0C5Jnnb-NtmY0W7xknbo2YVPEYnT660qYWEmK40nuJ3rsNTngz5th7ohQb0_hEfI70qG370l1c2JC9cyb0cKqHlgHsePMIgs87pzc3NTDNVc7S0Zjv4nbtA9GbcNUVD4LxdlHAebdDWC1NZXXnrF1PD_2NWEe9l1x8y8aaFjF8NAc10UtDXwPtYgg0PsmBV_YNTTCA-GWC3lxx1Nnbb9h3qyNkTOPGM6HU7liuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
«صابرین‌نیوز» با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/452051" target="_blank">📅 03:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452050">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=T6YIvYkK_4J5261A_8GRRIP_Lud9Ne96BRv3Em15qScb2BC_uGC0z5iT1IsnSfo5nSA7aGaO81pM-PuwctJIPtg8anpP9IqjRPUT2jR7AP9BpBKPQZeOAe7WUsk_7Dj239rYVVLzLHxSmhU3cc_xAJOom-oeWV1w2JYSBQl59TK-0mvpOP6UJeyTwnO8b90zCP_pSaAcqojqnexk3fMggJ6SveoZYdMMJawLjQs86ofzGQaXy0ue8HTq2BCeNIVsNA7MzdXjNjRS943DZCqKvl05gB2jpajL4hOWLAYdg4me1NgWN_hy9yJtx7Ak_fmrV2gwKn5Vbw7euHar7Us2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=T6YIvYkK_4J5261A_8GRRIP_Lud9Ne96BRv3Em15qScb2BC_uGC0z5iT1IsnSfo5nSA7aGaO81pM-PuwctJIPtg8anpP9IqjRPUT2jR7AP9BpBKPQZeOAe7WUsk_7Dj239rYVVLzLHxSmhU3cc_xAJOom-oeWV1w2JYSBQl59TK-0mvpOP6UJeyTwnO8b90zCP_pSaAcqojqnexk3fMggJ6SveoZYdMMJawLjQs86ofzGQaXy0ue8HTq2BCeNIVsNA7MzdXjNjRS943DZCqKvl05gB2jpajL4hOWLAYdg4me1NgWN_hy9yJtx7Ak_fmrV2gwKn5Vbw7euHar7Us2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
«صابرین‌نیوز» با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452050" target="_blank">📅 03:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452049">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
سپاه: یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگۀ هرمز را داشت دچار آتش‌سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
🔹
سه فروند کشتی نفتکش با تحریک و وسوسۀ ارتش کودک‌کش آمریکا قصد عبور از مسیر مین‌گذاری شدۀ جنوب تنگۀ هرمز را داشتند که…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452049" target="_blank">📅 03:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452048">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
سپاه: یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگۀ هرمز را داشت دچار آتش‌سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
🔹
سه فروند کشتی نفتکش با تحریک و وسوسۀ ارتش کودک‌کش آمریکا قصد عبور از مسیر مین‌گذاری شدۀ جنوب تنگۀ هرمز را داشتند که پس از انفجار و آتش‌سوزی شدید در یکی از آنها، دو فروند دیگر با سرعت دور زده و به عقب برگشتند.
🔹
نیروی دریایی مقتدر سپاه تاکید می‌کند که تنگۀ هرمز در کنترل ماست و تا زمان ادامۀ شرارت‌های آمریکا در منطقه، کاملا مسدود است و هیچ نفتکشی وارد و خارج نخواهد شد و هر کشتی که فریب آمریکا را بخورد و قصد عبور بدون هماهنگی با جمهوری اسلامی ایران را داشته باشد به همین سرنوشت دچار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452048" target="_blank">📅 03:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452047">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
اخبار اولیه حاکی از وقوع چندین انفجار در بندر عقبه اردن است.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/452047" target="_blank">📅 03:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452046">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منابع عربی: صدای چند انفجار در کویت شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452046" target="_blank">📅 03:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452045">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqFyyAFX9sdlltz5ixVsPAWzr9rLKNwDFH3QV5dwmJa2absYZDQuhQ36ZEPrLRvXZ7aLRAO-oiEjOn2JPhpNZhDO9H73pMQE2OCi-2R0hkOV44BO1OFr9KjpclKsRdTZFPGj5U5QzAvpvBIrruzGrH5vzuHfxa8N2NxdyvQt4MpkKt4gcq6XJGpt3GncXwcd-l6uOA3eppIoIH7nf6sTaHQsSRxUBRJxkY-KgT3tPNx7d8CGAZC9XHM3rXhqsWUy8MtoohIFaliWyAIZhDrCU9MkgnFpf-ardQvPPAIi3oaqyOu3-hSKjFiUS1Ite1zZYZEe7b8b7sJSIkJ6zGPZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ آمریکا: تفاهم‌نامه با ایران دیگر اجرا نمی‌شود
🔹
مارکو روبیو: تفاهم‌نامه با ایران، باز شدن تنگه هرمز و کشتیرانی آزاد را تصریح کرده بود و قرار بود ایران بیانیه‌ای صادر کند. اما آن‌روز آن‌ها یک کشتی را هدف قرار داده و به آن حمله کردند.
🔹
آنچه اکنون اتفاق می‌افتد واضح است؛ کشتی‌ها سعی می‌کنند از تنگۀ هرمز عبور کنند اما توسط ایرانی‌ها مورد حمله قرار می‌گیرند.
🔹
توافق‌ها بر اساس رعایت قوانین هستند و ما با ایران تفاهمی داشتیم که سپس آنها آن را نقض کردند و دیگر لازم‌الاجرا نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452045" target="_blank">📅 02:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452044">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/britaZeWyb782rGh0-GDotTgF2-Ni4zSkpkI7u5_iaSRw_Mz81l5dVoTwa4cGFMf4EHcX_B5NdVpzlmb5-klMIHtABlOtFKrEZiwBxRIczaIFUGrlaTBi4X4DbRdQpxSPfB4LvyOqBFthg_evZveWnSTuR9cH1OfateKTSTLeInjzHNsec5ve0OU672lisy3Y_E055gH5oMotHEhUalmtmxeMlgoOxiu48Qoer7C4pLvBXyHAJ07bkuKKe1HzLRhgZiPRGaw4kTNr1_ubMNef4Wsur9LZvzd3fhbDdML397v4NlGK1DHXJXlruXkMBRcoMOOTdC9nIPZG4BJGmZzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌
🔴
منابع عربی: مواضع نظامیان آمریکایی در کویت هدف حملۀ پهپادی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452044" target="_blank">📅 02:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452043">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تصویب بودجۀ میلیاردی برای تداوم جنگ آمریکا علیه ایران
🔹
مجلس نمایندگان آمریکا لایحۀ بودجه ۱۱۵۰ میلیارد دلاری پنتاگون که شامل بودجۀ اضافی برای تداوم جنگ تحمیلی علیه ایران است را تصویب کرد.
🔹
این لایحه شامل ۶۰ میلیارد دلار بودجۀ نظامی اضافی است که انتظار می‌رود بخش عمده‌ای از آن هزینه‌های مربوط به جنگ تحمیلی علیه ایران را پوشش دهد.
🔹
بر اساس گزارش‌ها، این لایحه اکنون باید به مجلس سنای آمریکا برود و در صورت تصویب، برای ابلاغ به رئیس‌جمهور تروریست این کشور ارسال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/452043" target="_blank">📅 02:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452039">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5iydWX1PrbWzhsJzQDgAu1HhAWzuoYFd7164VmutFRa80giQSW3TZppD7VQYspEY86XHSjE13LAB0Bjh8oXzmKs2VZYlulDX8xtotIuYmI4OeuA6JrjfDNR7v5qfPzD-q8DGMM-7ikFgkDB1s0hcZ2PG0mbVmhzWXWaOoHl4G8woIC35GWMRQ9sM4P_pa0GOOqdP5SIgQdIF4B5LVyHUiqf-e5ecNM31VeZfOY59Uv5KNqJnAXfxyCUCItYf0g0qtqn6OA_C_CJFgT4V5-kKveSYDsRj4-MWQLNActMnvwNbQEAoOpO5GEu165o2JrZcg9jCix9zFwJA5M6KkUmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5j1qU-7bqDb9JPqWyWLgnW9NhF7DfBqgwpVEZ50Jb01L3xp-hsp378JPgPdId-2g7bZfeD-98xXSlalnfcjhkbbDAtSGc45QVKInsd7X3ql5Zz1ReW9T6jUrICR09oNbe_MVelpQECx1jAU3zIWFaC-vCM-pIYkbAiDace8Gn2HFthJIzXp_s4dKzjOdMxjXZp7F_btkYDUfnHcWkjKLcrdwVxDDriMsOfuvu7cBVxAO4giad0rKI1tCVT-9hdJ6ZCjDDd5Ozry3KXaxxkEo6QhLzICpK-si43WyNxAz2VOyrIJW7-uXJpqWKpaGipg2g0KykMvkNwoufIeM9n37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgQfdiUmh2YhznvSqGrSaRwk5K7DCPyiiL3bQ7_9uRMt1iy_a5GwezF69zh4B_4VHEQ_TL9kK8SBdXoTFelBmF65VgJvHWgfOR0DgDpmeqSDGSuorLPDoU6OcaiJ8_6-VrnvpumwaZVGBLc4P5UfhrqIc4otd4a3k7xT8AgalbEK8rCS-5Q4opT0DwoeVtLp-qt0xEoqntNcKaFkcsbJJhx3jGrHlw7u5oF4UI3TGtNrgaUOj14gUUvMZOs_hGqquXWPWvQpx3qxAR8H4EacjGOYqIZKzqVI2pCGtowPFDv4rpyULjdYPGsTTOecz6DCbqbXLBj4GyV14gMfZXkVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLRBnDJmZPAwlhJ0teBT9fd1wfSneCQsC1txrFxfJZWG_r_RrG5sdqqZx61UGDdjUzsepOPS81QY3G93wn4k2t5iwJki0NW0ERqV5Yd8lGkaP_9xxlB0mVESBsSCAkM089s1rbnzEV4RnQF0SArUF2b4gBBM1Gb2L2dI6HwH_Hby2qrTStc3IMePAd6paM6lWoaiAjL8sumwaKTiksfP913ejNyA78wSJXTOAedQGc5mqu119qNrGFqVfPBts7TkDPef-LGs65_DAgt5oSK-ACVDgQOPAs4eKPtwhSpLAwgIqHJFqXxv8vd3k-6W0wy3KccLDEdXEdQB0JR74lz-cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452039" target="_blank">📅 01:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwDplfWRy4kQs2JzS9MLulpgqyz7A4CTn7JVYqjOA4_DVYrpj9tDNUZQqal5Y_j_L5KeoASJTRUlyoqV6ho5pgbo85FXktaDqIRzJUtZLgSwp3jQbK_NxC0EGPFN4XwtFJ2BhFK9NJzaWAnzdMB6VodNcqsQ4poRX746A9T282r4_m6Wxk1dliLu0gbrBgLbwd0rKRX4fgDWtjOGm29HM9x1LDIhq4tCSctEgr7zSJAGninTIUDrp7uZUeFcuui6I2eP9M4BQ8ych_yLHjeRrNKqKblSGXtlN9WOlxqgJqU9DAF4z-RhjScrx5YPf6IaUnpR2xYtluIvAS4M-7kOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oh_A7zg7g9gUmGxppKw6Bz1GcEQauHGVl_qN72fWQDKcguboAV0q3lE7ywze6G2Gy8NZfw6_ZbOSEnxxfTXkc4ZFw-vD3bElAi6r0FMGK-yxDsWpMbc7hbuohw3WoTMpPiNBxi06tI_696LjoGj1e2RPNEvkN0ZzjKBfJR3fy8qAim6wqnXzYBFcRzkRJAeA_Dw2p1c9NxOLa_CYOdhS9LW-rNwjqbNyPx2SV4di5oPl4y1GGgwMQ8ID_jU_GPOZK-xUv5GlqBRTaEagUTol82-ih4uF09PmYaA7ZJFM99Nj-BdzG8HJgsYG0MH3X90dq6hQoKcOedS9jhB3OQ8bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YArPzdRIp5aEtR0jaqZVTTohsJWeN8JB0x2zChlrJjHq6nEaAdShyuPQWdFbaQgJx_MjqdQA8OWzXOth5_uVqgpszSOeCeIsqUMJaj6KUEyUIgaJySuBdEBnkh1_lD3bROKYSqLFUandnvihmctzx1h0R4l47VJEKI_aXdL4UA_pW45naOpXOoCdqVvcFG_ivvivzDwakMikunGpG43l2zMwE25YA6oNFwnnO5Zbu_kVa41Zkjxu4tk3Il2NEWZ1rZhSS-fcyZqqMg9yPqr77yCofPPYhxL8XW1MzvlhdFgQfffYPYJ-8SYLJaK8Jdx-2b25axqK7_4qMT30vXXmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vc-WQ0yRzQ65x3UN2qoCrcD2UhQu6tIynBQWW9RvxmG6o1xtGWAAIUTRjCRoErbJ4kd5Lg7p8eTiXpr8RKJIzoAzUF0mW1kEbhy7Q9O8JAup-T_qydpEnutx0dbyqT4RYQ93lWVrRaLCELmTm4aguZ24KRQFiGPHGJrlRKpjampySU4JGd-hmqp32REBJxDB-qAe1iXU2yeYHqij_iSas6hgElS-fwPXJBeG4YNgny-1XsGOHdZBqAZgRjfikDLNhqDjaKO5TvB_oNIiJaXt3loOAjpDHWQrJCU3VV262-LGJbV4Ddp6nem6PQgwU8cNK9IX4uk8Y2lgUeDbTwDDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkJu2eOk8pdvaN_EyVPLSO-4wDznFSQ49F4SzgwTVfAW3uJBL5FThRwH12H-kdV1JUhV6R_pZU3eGKDHfHK-MjgKt7yV1pzPslmlzY1NsUG7mD670XUvbgwJd3KVR1xMn1my-wWAPidvTjZgx4Hq9zXXY_qbVn6bKFvIVX_kC-6jz-ul_2IAMhVGYNZAOrlJPwzg5X6JgFcmBjBF70t48OjLb7PsFsXNrgyVR7f8-xmZfC1xMnzuGx7qb_BExJdoFZOALFY16_cu-HbxPbRFb5WweAXJMIObFQI4wDc7vznb_yBjVCesWNBOXyzJwTXErKr1uEvYHzMRLCCTBDR2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kA1sEZBNuHEEDgM_NvKiPQPiX_pkWUDM-4gkHTDT4rHIEIYwsng7ukUi9tNLV7JoAFIa6lCVNgDcOAlyWfo33dzWJ9Bj2WInkClFWVzEZZMDmIXlAaa10gqMpGCw1dxCAMBFU0u8fwge_XKh1xy6yIgCRquBSK_OAsrVACCwO9JuS8Da0z-QEAxFhdkMPkx0KYYkm0aiDW9300CO23Bm5IopQbQrWpMJnkDKN5Ox9_EbelfLybv5k_LjthdlGbBqM0rTjvkGkAe-Nqho8z7VK9HRP9TpmsTY2emgNsOFuFhtIrs7zsKnyKhWMf4lwynbJ6XMUvxGOV-XBbkGLqps6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tv7UI2m6eIhMunB3jjPLnumLZemAb1To6ezNPyIpD9thCDn990fqH1E7pb1eQ4Szxw2Zap4E15ffGNFn-KRSi_FepRc3PMFZWLBlO4v1pjmIVJlNpw0LaoOteXJrIxnbLWqiwTBFAYZ_Q3UfoQNHmDuOyzV75AWk3KlpREEhyJ6G3y-Ynd27o2_JfsbNs7JysB9edmnQmy9bht-5ZvKwxjtj24rMN1eyOT34o-PzRRL1iZLQSrQIOY1VBPeAF3apKdYhYUoeEWIUmvpB3RD11bey5dUWzP3HV8zofpjDhZq0-uRWkd_yKb7D7Cq8f5fAHMJplFxExpWQu-9vKxHHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTElTFZKqtgTcEzC2GMNx0n311awIhYlh7x6LT-n7PlVHf6owB_amsKDf7EHeIh8DHh0-Gc72t5efEgTepQB786AiHvh-2qBvgBbIE6yIKWoquR6Cpd9NHkh5qOwR8SdlqLQ26i_V2QfAaTLwZpyeO0WOXNtTjC4C42V8RtMvjRdEc51ClrUuWiDxGuTN_O5ROfTajkoatXRipu5OZajWZ2RCR-cwFo-iYhv-IdJICHOn6z2F9GF-DWv3Fe48MUgkdc8s-tzyLHqhPVs0RQeRBRHNbimq7N11qBNEcPhwiw36NNCHaSF2r9v6dqmfKsW5D6_ozkO8iaCR11YWucI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyEd57zed-Prm-nU-i301pfQ9wIirnYOjjd_KJFq7QYjYqMYPBt1k2BerxX7qN355hSn35uGwVUjblhL48SA4H8gevpp7RvDVND4deY6cdjjSHjyBuqOJmxr8mhdSxsx3e4bN6vOm5_3tdeDhH9nFENDVTH5DVE1ARL7fHi7rggvzs28JFqDy9NHS6z854oCWAfjlZzsSy9i3DQZP5Lx4rVDdv16ZFj0upEVcW2HuKUoGNE-geP9QnsSWYHS-Clvm0LyqaS24uNHUhZS0fWX5gFCg5k2nf-eu8uvnP3_lCDeGYzyOyIBVCTLDJR-0IgArmqgF1QZcD4g5rqEi8Iy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xmc702q3iRpH8r-l-6NwaGlMUhseU18eL1SED8KIFUQVT-JLNDJfPPyiCcAivpfS-nS8mzMvPJj0CLTi0sIuD8pUtnpJW2iEtzBEHPqZaEUJDQUrn0SRg8kXWFnKOjL8wBU2FoTtMyifC-odeIBSAIQV4b05NZWABK246Lp6Wj3fyUTSyMYpW-Vf5RhZJbjjjxU8sgpKMFD0wIFTte7-etQkQGqG1nRCBaMz6GRjGc20jflSrV7yLkTdoGEUPMwivj05ONFuYYz-y04gnSF032r8IwQxrJfo1hdCRlXru1j50U88swMRkEk3e-KceSMyxfKIiFhqf4RdeetcXjs3bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452029" target="_blank">📅 01:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQDkve-oB7X9_Esn2SRwJ99m3FoGhcjzvY_sN-IV3DP_k4R6hDGW5IIZEKw2jdK_UjMffDkrCD0oSbdMWKC6vqLlEdiBeYb3m0q6FpZD9pKYcQzGB-sm3cbmixRiR90jow8IG4KPY7syKMQSP-lRBZBnKpm6qmtGrzWXxu1NdLMbasiXrHApWAOqim1VmTJqsVACPX5YHJE8R3XzQ1cqxSiut4pBoRt3wUdDy9-Z48uo5Lbmx3XDtpzbV5V3zEZjrLxAHeUwMA6HTY_z4LafUMppo1qPNDO9s_6DoGGmTrO9sIfeiPw7QEPTQLSYi_mxIYmvQLRq-lg-1YNWWh7hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با دستور ترامپ، و با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452028" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=uiSx3kk5pc08rW-HhmN599PuRkXsY9DKBAZZymZd2Ap9o-3Z3ymhIL8vcflmxgA5IT-fO7b9E9ShWsmZL3oha66x5hhguI6jKm8l09RqgfBRGv945TZozWE5RjoZ-vGdvBeoR552YZv6hv6d1nSjVlj6tGGdWruT_p7w5apd8Y4mZGzSkQ_BfF_47Zcp1VbNx3RyOCL-Y9UrGPhgUopWmCabBhtwbX2qN2QCilYRntLZ70hOS7IrtbcHHD7wMu_N1lqe3wrhRL4ch1QKEJ7nq28wgdioFug7f90laF8Z0idVfAVUPymv9rOdigimm5qbp6wosH3Q-NMuk4Tw9b7bNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=uiSx3kk5pc08rW-HhmN599PuRkXsY9DKBAZZymZd2Ap9o-3Z3ymhIL8vcflmxgA5IT-fO7b9E9ShWsmZL3oha66x5hhguI6jKm8l09RqgfBRGv945TZozWE5RjoZ-vGdvBeoR552YZv6hv6d1nSjVlj6tGGdWruT_p7w5apd8Y4mZGzSkQ_BfF_47Zcp1VbNx3RyOCL-Y9UrGPhgUopWmCabBhtwbX2qN2QCilYRntLZ70hOS7IrtbcHHD7wMu_N1lqe3wrhRL4ch1QKEJ7nq28wgdioFug7f90laF8Z0idVfAVUPymv9rOdigimm5qbp6wosH3Q-NMuk4Tw9b7bNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادی که به‌یاد دانش‌آموزان شهید مینابی پرتاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/452027" target="_blank">📅 01:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452026" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452025" target="_blank">📅 01:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpOBhQLKrZLpAhKAg4RqcsbwpBC1b94gKy-xyHrUUg4i8KItmzfUFBVYuANoajhA1rWFJkX3wcs6ouGhmd3uMcDtScZJyXRBp6GGuzcnX8OnmJtsjmtxCMz0ir_UkeQ3eRqAJ16iYqRa-tuM-Kq1nrj5enQ-PG6xVANxtP6b2gKeAB-NKpqwaetq71iiSEVc5dYMcHht_xIj9PjTlgp8x2A-KPw5nBys6HB81TZoGQdUJRg2BJNOwBiSgdm96ZZTIU8aOyKNqqJiEG2C28VHQsNpShKGAv5MUDLPZliXgkbvXTWabV4fugnoVCnJxX372-GBSAqcBKD68YM4SmvIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع نظامی: تنگه هرمز همچنان مسدود بوده و ادعای سنتکام بی‌اساس است
🔹
یک منبع آگاه نظامی بامداد امروز در گفت‌وگو با خبرگزاری فارس، ادعای اخیر سنتکام درباره وضعیت تنگه هرمز را به‌کلی بی‌اساس خواند و تأکید کرد که این آبراه استراتژیک همچنان مسدود است.
🔹
این منبع نظامی در واکنش به اظهارات «سازمان تروریستی سنتکام» که مدعی شده بود کنترل تنگه هرمز در اختیار ایران نیست، گفت: «تنگه هرمز تا زمانی که اقدامات خصمانه و تجاوزکارانه آمریکا ادامه دارد، مسدود خواهد ماند و باز نخواهد شد.»
🔹
این منبع نظامی همچنین خاطرنشان کرد که مرجعیت مدیریت تردد در این آبراه منحصراً در اختیار ایران است.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452024" target="_blank">📅 01:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
یمن: ۲ نفت‌کش عربستان را هدف قرار دادیم
🔹
سخنگوی نیروهای مسلح یمن: با اجرای یک عملیات نظامی ویژه، ۲ نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را به‌دلیل نقض دستور ممنوعیت تردد کشتی‌های عربستان، هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452023" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452022" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۲ انفجار در بوشهر
🔹
دقایقی قبل مردم بوشهر صدای ۲ انفجار از حوالی بوشهر شنیدند.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452021" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=iF_qP1-8mH1iGQ2tSnsdcyWbQJSC4v7Ti38rkrDeO5XipQbPC72qZ5-m0x6WfgIi1f4dLtS8EX9FL4oBY6AvemxZrcUyQEpTSyji_sp88yq4I18IDwIadlzKUTtjLHYVS-dRZRKcwxaV1OBz9HGxRYhO9HPSJpXc_ULysjICARkx7jqogzcQecNGu0HcHLl6lRqHOld5Se7v-pKUCZr9v4eojfzrLskjjDRRtjes_pJeFOBpD1Gks5JLDSFHX43uzKZwjwYTdYWGXV_Lsbq-QGdqmFOYehVQk1ct5eoVNFZzG9jHqZvOc0bZQu978gmgBPPagCpqp-59e6LypWXsXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=iF_qP1-8mH1iGQ2tSnsdcyWbQJSC4v7Ti38rkrDeO5XipQbPC72qZ5-m0x6WfgIi1f4dLtS8EX9FL4oBY6AvemxZrcUyQEpTSyji_sp88yq4I18IDwIadlzKUTtjLHYVS-dRZRKcwxaV1OBz9HGxRYhO9HPSJpXc_ULysjICARkx7jqogzcQecNGu0HcHLl6lRqHOld5Se7v-pKUCZr9v4eojfzrLskjjDRRtjes_pJeFOBpD1Gks5JLDSFHX43uzKZwjwYTdYWGXV_Lsbq-QGdqmFOYehVQk1ct5eoVNFZzG9jHqZvOc0bZQu978gmgBPPagCpqp-59e6LypWXsXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/452020" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به اطراف شهر اهواز
🔹
معاون استاندار خوزستان: یک نقطه در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452019" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک
🔹
حوالی ساعت ۲۴ صدای چند انفجار در حوالی سیریک در شرق هرمزگان شنیده شده است‌.
🔹
منابع محلی عنوان می‌کنند که صداها از محدوده بخش بمانی سیریک به گوش رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452018" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به اطراف شهر اهواز
🔹
معاون استاندار خوزستان: یک نقطه در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/452017" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-my6ZqzdzcShCex48I_eZaF7cLWdYp1yf9xmRtdJJObOVQ6ZKGCN52KjpJivUNUUR9yefXLbJqmz78V3ae9lSremV2telmbrEI2hVLut4DRweUEQdxzw-XtTfxObLqFB6mgSWExrw0D59gtwai-Kxd-7LGZyFLj8sw41T0Bl1GACREWfJMaLHW2goos_pTgaQDfrw8iFhmChgCyP789cJAh9x5WKh0pCIpvNc3YfvDCQ2zUyP4gWMx0-WnreGByVRGX9vdHxyh1YSz5ucRe8pm_AZ3Ftwa1-PgDeeAlzp63k-O4pwmzF7TezQsjIKSpl-a3LihgIMrsAHuzOZCITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: ایران در طول جنگ چند مقر سازمان سیا را هدف قرار داده است
🔹
رویترز گزارش داد بااینکه منابع از افشای تعداد دقیق یا مکان تأسیسات سیا که مورد اصابت پهپادهای ایران قرار گرفته، خودداری کرده‌اند، اما یک منبع تعداد آن‌ها را «بیش از یک و کمتر از دوازده» عنوان کرده است.
🔹
به گفتۀ دو مقام غربی در منطقۀ خلیج فارس، تحلیلگران معتقدند حمله به ریاض توسط دو فروند پهپاد از نوع «شاهد» ایران بوده است. یکی از پهپادها بخش آسیب‌پذیری از نمای بیرونی سفارت را تخریب کرده و پهپاد دوم از همان روزنه وارد و منفجر شده است.
🔸
تأسیسات سیا در خارج از آمریکا که به‌طور سنتی در سفارتخانه‌ها قرار دارند، «ایستگاه» نامیده می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452016" target="_blank">📅 00:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keJdYnoHjAEw-gibZ5w1y6lmwnTM9eR8INN0L5Iq99kHk1NUOM_dvNqyeTlTZGN7HhYamJvDBEKnEKqXEdb2xAF-LUtqAa4_9ixgj09isiMQOiUua1Kvq3Clc35cxVrwFn0p1crbnfH1hlT1W9E3JMqdIImmtIECkj-2L-o0H5qtsKtYZud0ChVnymwD2A9wM5ieC_SIlfwnO29cQoiFujdx_1RiMh5EQJyruFTblWpg-O1LL3w8AJL9QRzBsZzH5jExz0WsFrvd_H_JGTcqBm3OdMfvzCdLBqEUTeInAU1u1gD9xDUKT8Tid__XykAikTqrrwwnlrZgjzPBi4fwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه‌هایی که چراغ پایگاه‌های آمریکا در منطقه را روشن نگه‌داشته‌اند
🔹
به گزارش فارس، تهدیدات اخیر علیه زیرساخت‌های انرژی ایران، با نگاه به معماری امنیتی آمریکا در منطقه، پیچیدگی خاصی پیدا می‌کند. وابستگی عمیق پایگاه‌های نظامی کلیدی ایالات متحده به شبکه‌های…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452015" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5NJ3GyT6FgANhIXCyqk4VCr8etSrlS1fHp657mW37bTES6vfQuAwq5dJ5YF2PN0uwfRsOLBxWLnVlYYHMXvZqERdiRVakdkllexu2TxIa5-3rHJ2GZsteVyI56ftmc5IaQogRNUxMRU3ZqdpxkNyO4icSiiN80CVyycCaw8MC4KyfBe-k80zorQ1cPST4oauuOt7XKZmlwop95Ms0TxQqTrnJpktDgsxi4dE2qMcM_Pp5H8_K7OfgxcMYmU055XgSN8ax9cx5GFTrnh-i06Ml3GpTF80xfydkGMcJN5Mi3LcFn_eBc7Is8wq1CKQg_p-WREZxkKiN7ZtW6WByqKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: در صورت آغاز جنگ علیه غزه، فوراً وارد عمل می‌شویم
🔹
رئیس ستاد کل نیروهای مسلح یمن در پیامی ضمن تبریک انتخاب خلیل الحیه به ریاست حماس، گفت که اگر دشمن اسرائیلی بار دیگر برای آغاز جنگ علیه نوار غزه اقدام کند، یمن آمادگی کامل دارد که فوراً به تشدید عملیات نظامی بازگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452014" target="_blank">📅 00:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سهمیه ۶۰ لیتری بنزین مرداد شارژ شد
🔹
۶۰ لیتر سهمیه بنزین مرداد ۱۴۰۵ خودروهای شخصی بدون هیچ‌گونه تغییری در کارت‌های هوشمند سوخت شخصی شارژ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452013" target="_blank">📅 00:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb67e609d.mp4?token=giSd54pzcgvU5bHX1QuuURnoMq3KImjM9lBl_1ByCGbEmmOg9AVKcxCz7CMwwKgung4DajNDl3F12m6OWd1Y87Qy0WlWokcMgDjgJ5zuR9dTWBPciRRtt3YfvYhgbjJM5rgcJlZB207ALcWGF1TZZbJg0bJVhhO90WXqBAxfUCkkORKCNnOfLxMCwmMlgKVs_-kPhm63Qii9IRqf_SCrMP7TzzDj1NiamRSHbOpBBNeWW8NWGR_8Ikx6FGngg94qPsA-XczYeNdHwW0lQiUoHjkVyCet6FnTaY6Hz5fe6Yh4RD-V-S8qPwfBC35AXDCWvUhIB4UBVQSRvnfDqGjAOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb67e609d.mp4?token=giSd54pzcgvU5bHX1QuuURnoMq3KImjM9lBl_1ByCGbEmmOg9AVKcxCz7CMwwKgung4DajNDl3F12m6OWd1Y87Qy0WlWokcMgDjgJ5zuR9dTWBPciRRtt3YfvYhgbjJM5rgcJlZB207ALcWGF1TZZbJg0bJVhhO90WXqBAxfUCkkORKCNnOfLxMCwmMlgKVs_-kPhm63Qii9IRqf_SCrMP7TzzDj1NiamRSHbOpBBNeWW8NWGR_8Ikx6FGngg94qPsA-XczYeNdHwW0lQiUoHjkVyCet6FnTaY6Hz5fe6Yh4RD-V-S8qPwfBC35AXDCWvUhIB4UBVQSRvnfDqGjAOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردهٔ قتل زن جوان در شیراز چه بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/452012" target="_blank">📅 23:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452010">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITPd-fThIHe4UwkRErOo6W0SA-zcTtIjLg_NT-XmsOcX9lHLwd-pDeG1_Nd-Klka0hzOs5U9Z1kZUb6vcK5Iu3_AWrN-kYojpqImyrvB4eDDJm7OLxF1OlOUzfc3bLc4aSLhym65RIoX77hm8-WTF4Kn8qwQM-wrkZQfUsVcW5uBY70mFGIBKcZWOj-9eOipmxG6bKnazKtsrSxWsLobKHEtBhnqrBCR3FH60UyYN8iFqkrM9kFX7TChorKjdGGxMWLP72T5KVYtcnCMaYqGkHAYwHCtiOKx4YlwD3dlhHBP7YD8_dWfvyXOKA1xFLBHrUHdPy3GxFemj4KO3e6R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: جنون آمریکا را با غافلگیری در فناوری‌های تهاجمی پاسخ می‌دهیم
🔹
هرگونه تعدی به زیرساخت‌های ایران، در قیمت انرژی ایالت‌های آمریکا تاثیر تصاعدی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452010" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82765fb34b.mp4?token=XypT5Rt0YdqDbEy10KeSlUTgs9CvlGJl9z0g8QvqGHDsNAeaJwFx8GV_k0_FF0k9kSiP6y7QDN23JOP9AUt7Sh8FoknVoyq8Nwg2mZDLK4y97NrTz66xhZbb2qkIYNdLnzHzIyq48eq8TDp2DN1PVQpLit6gW_teM2T0gKsm0ndKigWtZrRt6ZWpbGeiGi-oddi5d9MfbuJSOXIDCTs_EcmpJ3coBFUtU4RktUkcH--2ehtc4K8i_ABOaamay86a8AyS_ord3FK4kTa8xLPgpFeE38lUl6ZfUWAvGOrqiX_310Qq2yGbWJfI6ulgZ1XyZCR6KLs9NiFiY5N6Vti9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82765fb34b.mp4?token=XypT5Rt0YdqDbEy10KeSlUTgs9CvlGJl9z0g8QvqGHDsNAeaJwFx8GV_k0_FF0k9kSiP6y7QDN23JOP9AUt7Sh8FoknVoyq8Nwg2mZDLK4y97NrTz66xhZbb2qkIYNdLnzHzIyq48eq8TDp2DN1PVQpLit6gW_teM2T0gKsm0ndKigWtZrRt6ZWpbGeiGi-oddi5d9MfbuJSOXIDCTs_EcmpJ3coBFUtU4RktUkcH--2ehtc4K8i_ABOaamay86a8AyS_ord3FK4kTa8xLPgpFeE38lUl6ZfUWAvGOrqiX_310Qq2yGbWJfI6ulgZ1XyZCR6KLs9NiFiY5N6Vti9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی مقدس مردم ایران به ۱۴۴ شب رسید
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/452009" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452008">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a84232a.mp4?token=ZltCQkPvAc5kHZRi5Zha1UoQpnFQe38MgLbT_37247-j9JyxhBClHIuacHPoi6AekfBx1IIdDMzbmJrCLFthpWHiNt8Lu5azA1_5X0_xZu-LdaQJd35tmOWQ2M1k5f04k_wkbHrdZBhh_KNMpE9tar4uWRHmmaFYagQRMAb4eT8YoPp5OhgS0siMemHYMv-Aes2hLFiU7uxsm2zyq9rS25oAcxKneM5YEP2-ady09jIj1-5tlNquVVQfrPaYtgKWb95cK1QVQEC7428HXO2jl8pcYHSjaK_cDbDXYIdsvNbTShLO9q0tG0Xoud7J0QjST5oL2k5wB6aTqWiZQJJpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a84232a.mp4?token=ZltCQkPvAc5kHZRi5Zha1UoQpnFQe38MgLbT_37247-j9JyxhBClHIuacHPoi6AekfBx1IIdDMzbmJrCLFthpWHiNt8Lu5azA1_5X0_xZu-LdaQJd35tmOWQ2M1k5f04k_wkbHrdZBhh_KNMpE9tar4uWRHmmaFYagQRMAb4eT8YoPp5OhgS0siMemHYMv-Aes2hLFiU7uxsm2zyq9rS25oAcxKneM5YEP2-ady09jIj1-5tlNquVVQfrPaYtgKWb95cK1QVQEC7428HXO2jl8pcYHSjaK_cDbDXYIdsvNbTShLO9q0tG0Xoud7J0QjST5oL2k5wB6aTqWiZQJJpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری نیشابوری‌ها در ایستگاه ۱۴۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452008" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452007">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88cbc0418a.mp4?token=XCRuiyUGJnJMU-QySBGw_SCdbUIQlaYiq-1ccizCGN3CWjb7lvgC-Nzo6OjxlDeykFjPkv_Sy90vPRhPnSUvko-Cdid1mlL08_8EEO9FyTwyD5EDieuKWwjt9KGlXXHa6XncT1sPcr2AyNNurZoZGKgc5WNAEEJJRJz7HE_SkstE9G3Ccpx6DzZ9UtlMkHUYToOHHybZJhlOEpb_OSq7kRYaRup0EmcI6bzTTh7Ei_NUVvrDcGuxwHhAEe89TW38owSAC2caJHXVdg5BDAUihX5mlCtZ7a7THBeB9gP085Sf5VQuSdgkQCJkBsTik6y2TVJyxwpFUhG8mbg3Xll-nh6pdvZoz5qUH9PTYf4YaAixyOLLaHx7rtXXVppqnRZS5uis_XMBlTSUlvegGc7c2loYMDIKnIufnke8XidG0al_Js8uyHIseDs1TKoNBVS87q5BVxryMe6xst9G32zIAtvQyo_D3gDSvlfp4VyeZKIGPpgc8731L6xPsoYrMhEHpSvG_EYOOE-Xu3HO4FT65HSCpPFB93FPxJS8xWZqUxUdrAgKvbWYzw0mvkpLIlzlCAsXw-z1ITX_J9U4Xe-Ul_MJSa9zmaHo8rZBDk2hLJBzCwxh7TuJOh5FszM7C75PQfmxPXPaSr6E76rR3uRGHSxN4ARgMg-oMLNGQRLknPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88cbc0418a.mp4?token=XCRuiyUGJnJMU-QySBGw_SCdbUIQlaYiq-1ccizCGN3CWjb7lvgC-Nzo6OjxlDeykFjPkv_Sy90vPRhPnSUvko-Cdid1mlL08_8EEO9FyTwyD5EDieuKWwjt9KGlXXHa6XncT1sPcr2AyNNurZoZGKgc5WNAEEJJRJz7HE_SkstE9G3Ccpx6DzZ9UtlMkHUYToOHHybZJhlOEpb_OSq7kRYaRup0EmcI6bzTTh7Ei_NUVvrDcGuxwHhAEe89TW38owSAC2caJHXVdg5BDAUihX5mlCtZ7a7THBeB9gP085Sf5VQuSdgkQCJkBsTik6y2TVJyxwpFUhG8mbg3Xll-nh6pdvZoz5qUH9PTYf4YaAixyOLLaHx7rtXXVppqnRZS5uis_XMBlTSUlvegGc7c2loYMDIKnIufnke8XidG0al_Js8uyHIseDs1TKoNBVS87q5BVxryMe6xst9G32zIAtvQyo_D3gDSvlfp4VyeZKIGPpgc8731L6xPsoYrMhEHpSvG_EYOOE-Xu3HO4FT65HSCpPFB93FPxJS8xWZqUxUdrAgKvbWYzw0mvkpLIlzlCAsXw-z1ITX_J9U4Xe-Ul_MJSa9zmaHo8rZBDk2hLJBzCwxh7TuJOh5FszM7C75PQfmxPXPaSr6E76rR3uRGHSxN4ARgMg-oMLNGQRLknPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کاشمر در شب ۱۴۴ قیام مردمی این‌گونه در میدان حاضر هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452007" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452006">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
برخی منابع خبر دادند که در اردن هم صدای چند انفجار شنیده می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452006" target="_blank">📅 23:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452005">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
برخی منابع خبر دادند که در اردن هم صدای چند انفجار شنیده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452005" target="_blank">📅 23:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452004">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/452004" target="_blank">📅 22:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452003">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89683dc21.mp4?token=CMsJulP9Fz8WaiO0GBVeXtrtMBiKh09fHEyUomF7A4fArQDIUG8UrgnJDsIYrI5_0YNIm3rDBvA81QiQ3xMbBby47Ym4PcOIS5NYl8J6iZmG_cbJGnsmYMHENfxpBoP3IiaAKdCKKl_Tnf2PjCzaR1U5adX8S9nQmSNrtb-4N2ddCCH0_iWmfsljrQnSoOOWjiE_8TMVKBMwjpeNsJhlEdOzhY0Qfy7cWFoMIDsqxrOlUS71VjhTpeNm3MUxH6YIf4YgbZrMO7AVcv3ds0DPFpR40Ba-mq3Iptxi8U9WxIPdHKHlalwqwxHQKVNqH5emIjbqmhXwYqc4jy-ih_0OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89683dc21.mp4?token=CMsJulP9Fz8WaiO0GBVeXtrtMBiKh09fHEyUomF7A4fArQDIUG8UrgnJDsIYrI5_0YNIm3rDBvA81QiQ3xMbBby47Ym4PcOIS5NYl8J6iZmG_cbJGnsmYMHENfxpBoP3IiaAKdCKKl_Tnf2PjCzaR1U5adX8S9nQmSNrtb-4N2ddCCH0_iWmfsljrQnSoOOWjiE_8TMVKBMwjpeNsJhlEdOzhY0Qfy7cWFoMIDsqxrOlUS71VjhTpeNm3MUxH6YIf4YgbZrMO7AVcv3ds0DPFpR40Ba-mq3Iptxi8U9WxIPdHKHlalwqwxHQKVNqH5emIjbqmhXwYqc4jy-ih_0OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعا می‌کنم از پیکر پسرم چیزی نمانده باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/452003" target="_blank">📅 22:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFejudodXr4tuMDoJ3V0rcuCS_5ZUoPApdyZcpLcdyy-frpAdHr6LRiOwx5tNp3xG7A93W6IexfuhpciPwn__5VKzBP94YI3spRVpe7VLN2hEvtOKCjsDzjBxxgvcpuYSYewI8AkAoGrCLFk1sCPPhwu8ApQ5ppPCu81LvlG07jno8Nr1Ce8sDfRPSV4tM0uhG9jC6iAYLmAPe8jLS8OaDDbAddkHrFYL1PsOOuZSonJiWkGuTzYhOz3EIFSutG3O-YP6dU6hiCasS367QdBeMTovd5k0z5GHQ-YIWmTuqUWhKZHFuaZoLyT3mH_PburUizMxQitJ3RkfQkmtxqYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه‌هایی که چراغ پایگاه‌های آمریکا در منطقه را روشن نگه‌داشته‌اند
🔹
به گزارش فارس، تهدیدات اخیر علیه زیرساخت‌های انرژی ایران، با نگاه به معماری امنیتی آمریکا در منطقه، پیچیدگی خاصی پیدا می‌کند. وابستگی عمیق پایگاه‌های نظامی کلیدی ایالات متحده به شبکه‌های برق کشورهای میزبان، یک شبکه وابستگی متقابل استراتژیک را شکل داده که هرگونه اقدام علیه آن، می‌تواند پیامدهای امنیتی گسترده‌ای برای منافع آمریکا در پی داشته باشد. در این گزارش، چهار نمونه بارز از این وابستگی حیاتی بررسی می‌شود.
🔸
۱. نیروگاه الطويله (امارات متحده عربی)؛ تأمین‌کننده برق پایگاه الظفره آمریکا
🔹
نیروگاه الطويله در ابوظبی، با تولید ۶,۰۰۰ مگاوات برق، سهمی معادل ۱۲ درصد از کل برق مصرفی امارات متحده عربی را تأمین می‌کند. این نیروگاه، نقش کلیدی در تأمین انرژی پایگاه هوایی الظفره دارد؛ پایگاهی که میزبان جنگنده‌ها و پهپادهای استراتژیک آمریکا مانند RQ-4 Global Hawk بوده و پیش‌تر سابقه هدف‌گیری توسط ایران را نیز دارد. هرگونه اختلال در برق این نیروگاه، به معنای اختلال مستقیم در توان عملیاتی الظفره خواهد بود.
🔸
۲. نیروگاه دیوا (دبی)؛ تأمین‌کننده برق پایگاه المنهاد
🔹
نیروگاه دیوا در دبی، با ظرفیت تولید ۹,۶۵۰ مگاوات برق، تأمین‌کننده ۸۵ درصد از برق مصرفی کلان‌شهر دبی است. این نیروگاه، شریان اصلی تأمین انرژی برای پایگاه نظامی المنهاد محسوب می‌شود. المنهاد به عنوان یکی از مراکز حیاتی حضور نظامی آمریکا در جنوب خلیج فارس، با هدف‌گیری این منبع تغذیه، عملاً از چرخه عملیاتی خارج خواهد شد.
🔸
۳. نیروگاه راس‌لفان (قطر)؛ تأمین‌کننده برق پایگاه العدید
🔹
نیروگاه راس‌لفان در قطر، با تولید ۴,۵۱۱ مگاوات برق، وظیفه تأمین انرژی پایگاه هوایی العدید را بر عهده دارد. العدید به عنوان بزرگترین پایگاه آمریکا در منطقه و مرکز فرماندهی هوایی سنتکام، نقشی بی‌بدیل در راهبرد نظامی واشنگتن ایفا می‌کند. اختلال در برق این نیروگاه، به معنای فلج شدن مرکز فرماندهی و کنترل عملیات هوایی آمریکا در غرب آسیاست.
🔸
۴. نیروگاه ریاض (عربستان سعودی)؛ تأمین‌کننده برق پایگاه الخرج
🔹
نیروگاه ریاض، با ظرفیت تولید ۹,۶۳۶ مگاوات برق، مسئول تأمین انرژی پایگاه هوایی شاهزاده سلطان در الخرج است. این پایگاه به عنوان یکی از مهم‌ترین مراکز پذیرنده دارایی‌های نظامی آمریکا در خاک عربستان، وابستگی کامل به شبکه برق پایتخت دارد و هرگونه بی‌ثباتی در این منبع تغذیه، امنیت عملیاتی آن را با خطر جدی مواجه می‌کند.
🔹
بررسی این چهار نیروگاه نشان می‌دهد که تأسیسات حیاتی انرژی در امارات، دبی، قطر و عربستان، نه تنها زیرساخت‌های غیرنظامی، بلکه حلقه‌های اتصال زنجیره تأمین قدرت نظامی آمریکا در منطقه هستند. بدین ترتیب، هر گونه تهدید یا اقدام علیه شبکه‌های برق ایران، با یک بازدارندگی متقابل آشکار مواجه است؛ چرا که این نیروگاه‌ها به عنوان شریان‌های حیاتی تأمین انرژی پایگاه‌های نظامی کلیدی آمریکا شناخته می‌شوند و هر گونه بی‌ثباتی در این منطقه، مستقیماً بر معادلات امنیتی و عملیاتی نیروهای آمریکایی تأثیر خواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452001" target="_blank">📅 22:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452000">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b22afbf78.mp4?token=VvaLvzG7KKcMQH6bl_OARp7_gi7nj0vJeIBHxpif_0MtnqLs0epZeQUR98lPTfxVJXe1eLuudcPadDEPN_9xDAG-iQN83F3lumNkYROLzOHmlggtCZuMWg2GEnEU5NS8_dbo81hfP2lQb_Vvmf-whipdq4gLTYrY6srDWc8xbwAOTRkvjxirLgdr0xB5G76IUhZGI12BTyRFt_hZreI0RuJfm7qu5J_eqiQuAjLLvpIQbyhQ1rrAkXh1q0uFWS7cqkRZUaxLD-DvhEvfr-pA52hI6HVfNj0k8CIQ027XoXSaNWeG_3Hbut4VqLAncielinXpq_yAN6K14f6d747Q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b22afbf78.mp4?token=VvaLvzG7KKcMQH6bl_OARp7_gi7nj0vJeIBHxpif_0MtnqLs0epZeQUR98lPTfxVJXe1eLuudcPadDEPN_9xDAG-iQN83F3lumNkYROLzOHmlggtCZuMWg2GEnEU5NS8_dbo81hfP2lQb_Vvmf-whipdq4gLTYrY6srDWc8xbwAOTRkvjxirLgdr0xB5G76IUhZGI12BTyRFt_hZreI0RuJfm7qu5J_eqiQuAjLLvpIQbyhQ1rrAkXh1q0uFWS7cqkRZUaxLD-DvhEvfr-pA52hI6HVfNj0k8CIQ027XoXSaNWeG_3Hbut4VqLAncielinXpq_yAN6K14f6d747Q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌ها می‌خواهند شما برای اسرائیل بمیرید
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452000" target="_blank">📅 22:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e1afe4b2.mp4?token=W_oiMdtVRcIibnb8LNH6q4wxEJDBKb8nqnaw1HF3xSEUPR0_FaV0WJcBTeaAhR1DLAToZsZPy1deiF3jncU_vLOn1cdRc-cIQBhVQlx7jzxA-IyLa1H1VKXQ6tKL93KqazSKM6UhkTyYL-KiWWx0Iu6l0hcBDWYvUJ_joMVUA9K-1U-dW2Psu6L2Kw4mvTGbux7ZxXwr7qF276TNIzHKvwFhDvrCnEFbY9KJqeujlzn-fJvH5-g-mwfQpkS1c1PbMrEg5G5Nj4Nz4TgOlvtFtb811rf_Vuj7Lwp0nbJDRu-UB3x76v-6yA7coKOy0KDThxhLk211IPfTOOYZJ24kmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e1afe4b2.mp4?token=W_oiMdtVRcIibnb8LNH6q4wxEJDBKb8nqnaw1HF3xSEUPR0_FaV0WJcBTeaAhR1DLAToZsZPy1deiF3jncU_vLOn1cdRc-cIQBhVQlx7jzxA-IyLa1H1VKXQ6tKL93KqazSKM6UhkTyYL-KiWWx0Iu6l0hcBDWYvUJ_joMVUA9K-1U-dW2Psu6L2Kw4mvTGbux7ZxXwr7qF276TNIzHKvwFhDvrCnEFbY9KJqeujlzn-fJvH5-g-mwfQpkS1c1PbMrEg5G5Nj4Nz4TgOlvtFtb811rf_Vuj7Lwp0nbJDRu-UB3x76v-6yA7coKOy0KDThxhLk211IPfTOOYZJ24kmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌سازمان بازرسی: اشخاصی از یک نهاد عمومی غیردولتی یک میلیارد دلار به جیب زده بودند که با پیگیری ما این اموال به بیت‌المال بازگشت.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451999" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFTOZyY_ziSVRYnW8fK04saY5rT2523weoTKe6SnjDIKN8bs9Zc_h9sbh-Yh3UVEeCAWZrCHihxdNJkgDeuJ5tkf7G_S20BNyQAPMOkheVOclsMAdcfM5XaGF_c-3i7VxjpXUF4lI9QR0YaQJCpQUoPEjP6OGdGsRpPhhaAm3-lHQoNEdi3NF0nuEXD3Up85JsLhKk0CCXJzBcsFVF7svs8IhgAwtToqMf89BW-D1m917HotP1P07DtA1RRZTIYqOC7j9JWD5wi4-U40ilzIzpr_g4pUPmmvwlGAjDMLInEV3IJ5hHQe2KEtgg-oKBb4fKyvfq38SaIUnopOnCX4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
الهی هیچکی داغ شاخ شمشادش نبینه
🔹
صحنه‌هایی از وداع جانسوز مادران شهدای میناب با پاره‌های پیکر فرزندان شهید خود. @Farsna - Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451998" target="_blank">📅 22:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf95ece1c.mp4?token=SnA8_OrS8K1DTDyUiZoGPbfSZcfazOkjaB-BOlr3X4KyfZciNvhrqQSs894F7S3tlrXFW-ug42Yqd8-Fut1ibKHDtg5gTw3hO75gIBNuRkBXNgzHcOME1Yv6duneJCj846fs-368myoxHInCntsWm2CWsMnFBUdvs7EHqrkHcpVTLANP_nAxV9s_lvcR7E5Q340DU3G2sIX4QunGEtUWhMSHf4FqtRTNqtdggb0jSKOQC4HYhM7RJS6w7U6_XEI3p1pHbNSzXcTzeTV71Nt6JWv0qz6v_UqQu7a_9AAF5WB4XGKceRw8kJZVlZu34jLmLhjqJ18ZkAlxFJMeZXAFCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf95ece1c.mp4?token=SnA8_OrS8K1DTDyUiZoGPbfSZcfazOkjaB-BOlr3X4KyfZciNvhrqQSs894F7S3tlrXFW-ug42Yqd8-Fut1ibKHDtg5gTw3hO75gIBNuRkBXNgzHcOME1Yv6duneJCj846fs-368myoxHInCntsWm2CWsMnFBUdvs7EHqrkHcpVTLANP_nAxV9s_lvcR7E5Q340DU3G2sIX4QunGEtUWhMSHf4FqtRTNqtdggb0jSKOQC4HYhM7RJS6w7U6_XEI3p1pHbNSzXcTzeTV71Nt6JWv0qz6v_UqQu7a_9AAF5WB4XGKceRw8kJZVlZu34jLmLhjqJ18ZkAlxFJMeZXAFCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلبِ یک ایران برای جنوب می‌تپد
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451996" target="_blank">📅 22:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfClFMlBM6PZhwUP4_S-ZjH_iv2hspEtTwbgqeURpPJVvfCR9EkKPtyDHqb1CqQvYy2alXxDTuuXrXj8VI8JnLmIY_qVxNhOADPQ1R7UbqlXWxW3LAf-PGkeBgO6rFTzUgmyOKQ6DxsQInk8F39hOy7O8xOMogne3r4Y0MX88FAxzzgQw2gHNdyugW5X12nzScPPs-zKYKir-wPVfZnjAmT7f5NIsI7Z9n7vfXGZNzlGOaW92SmEZBH02Lp9l_CXAf22OXOY3DWsC0sZ5DREq1h4KeSu4tc1bOVzqT5Opgf_hD3lcxdIpMHXvgEOomg3E778AD995ubsP3IcwGAZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارگاه خاتم‌الانبیا: در صورت حملۀ آمریکا به زیرساخت‌ها، صادرات نفت منطقه متوقف و زیرساخت‌های حیاتی هدف قرار می‌گیرد
🔹
رئیس‌جمهور آمریکا بار دیگر ایران را به هدف قراردادن زیرساخت‌های کشور تهدید کرده است. پیرو هشدار شب گذشته، تنگه هرمز همچنان بسته است و در صورت عبور هر شناوری، تردد فقط از مسیرهای تعیین‌شده و مطابق ترتیبات اعلام‌شده قبلی مجاز خواهد بود.
🔹
در صورت عملی‌شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات حتی یک قطره نفت را نخواهند داد و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه را هدف قرار خواهند داد.
🔹
تداوم تهدیدهای آمریکا و ارتش این کشور، نتیجه‌ای جز گسترش جنگ در منطقه و حتی فراتر از آن نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451994" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToeD6qsnOd4dZFi9KKslNQZBhkv0ClVMtza_DzMrptV6z4EB-IDi2ehqEX3_dq-n-5iwUZNVVYp6qLOAdwzi-3FgkfAQSxBsJn6-pu0rDa_pVC3megkm2eg_6bzksgINbCphAv8VVO76_63ZFWuzSA3tCAv5NUfk-qKWE7e0GgqegAK3TBxDt_n0I4tK0B98jyberBzzkazChzqvjj1-P_1EdWKFWMmU8tXY3KCnUfMIjWVPSfbuv3u869aOA6775GY7fZPJnH-wkABGG3UzjLLA5JAitj8zWk9uKLyF8xp_cQmaqlonCihAEzI2LR7MW1z2p1UdFBkUwYMUifwKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
برگزاری مجمع عمومی عادی سالیانه بانک شهر با حضور بیش از ۷۴ درصدی سهامداران
⭐️
«بانک شهر» با تأیید قاطع سهامداران، کارنامه موفق خود را به ثبت رساند
⬅️
مجمع عمومی عادی سالیانه بانک شهر برای سال مالی منتهی به 29 اسفندماه 1404 با حضور بیش از 74 درصدی سهامداران حقیقی و حقوقی برگزار شد و عملکرد این بانک با استقبال و حمایت گسترده سهامداران مورد تأیید قرار گرفت.
⬅️
به گزارش روابط عمومی بانک شهر، این مجمع با حضور نمایندگان بانک مرکزی، ناظر فرابورس و جمع گسترده‌ای از سهامداران برگزار شد. همچنین امکان مشاهده آنلاین این رویداد از طریق پایگاه اینترنتی بانک شهر برای سایر سهامداران فراهم بود تا روند برگزاری مجمع را به صورت زنده دنبال کنند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/451993" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKkpPr6gA56TWWQxX4feZmApLxzk31SUwDrhbcBKr-QrOrbMbbhr9ydmZFIkJxXVH3VKgUeYVFBMg-KJipJoJ82EqL4_jHYL7sUu94oQW3S0q7vJ2JpdJqvKmk6LDaELNDsArrKzee0mXFq399svMyef27FEOdf3dpyZUxEz6_EfViXHdKzTgkP9YtKeRFI0etbONxZIgu8WqaUnReGWKJiIIVxPETZkHMEpH3n8usF6_V21aI8858dtuVy2IPMtFupdxlSn3Y6IIetQWZQk1aETX8jInelMm3nNMnjZCFIyADDl6-RLrGFo2UF5Kz_-YK8QjiXaUBjyaIuHJGKi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اسنپ‌بیمه قسطی هم بخری، تخفیف داری!
💰
برای خرید بیمۀ بدنه یا شخص ثالث تا ۲ میلیون تومان تخفیف بگیر و هزینه‌اش رو قسطی و بدون سود پرداخت کن.
✅
کد تخفیف: GT3F
برای استعلام و خرید به‌صرفه بیمه، اسنپ‌بیمه ۲۴ساعته کنارته
💙
برای خرید بیمه وارد لینک زیر شو:
👇
👇
https://l.snpy.ir/z0kq4
https://l.snpy.ir/z0kq4</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451992" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451991" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451989">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATs01k_OiKN9iIgjLsUs1QLL5RHFn_hOOh5zauif2A_5gba5ZuL1LE89qFBG4YWtxVLfVTF_uER7FJ_zu6ChjEAyjYNYLUfsQOvIQy0aTBx0rdFWRZajPzq6XPT3YmoEKPuBmQjoEUAH3jvE_4te4H86zUxzW1G2-oQlXIA8E9Jkr1yo3YV2S8Jjpyf1mgzIpGVuU3xsf4GVRs7-Sw58kapW1oI93ynkqjHl8YDk4mVoTqY36XEu5CDM2TBOYYCC4aK9Mi2mydxlzLRuZ7JSlIGxOn-JV_1IpBuutdLjJr9JedpmazTRO1WVLIo_OTZuNH6ISnVweA4gCwktK1dm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: هرگونه تجاوز به ایران، از جمله به زیرساخت‌های ما، پاسخی قوی و قاطع را به همراه خواهد داشت
🔹
کسانی که به چنین تجاوزی کمک کنند، با هر نوع پشتیبانی که باشد، نیز اهداف مشروع تلقی خواهند شد.
🔹
دکترین دفاعی ما روشن است: چشم در برابر چشم.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451989" target="_blank">📅 22:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451988">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3d1564cc.mp4?token=PANSf8bF8Rz1RD5cHR9Hq5-fnTV-oPGyC1H2lkKhX5PJZkNQl6t76CWzPWtQmtcSuEuE9jRos7C4n3HZaa0oqSCA74jcHCQEz7zGl5Z-PGOZiFokUGUe1QnS4FCziEWcvUJ1O7y6cFjpuspPwdwxPEM0NppUNzVLMUUO1V9pC5i5WB4wwVhNjCoHo05IKEqo_SQOSFz7G363-C7x9ysiy0bc9BiSULHqgFfp50qEYg2V-I1r2Hrgud-7WOozrYEY1ej37xlp13m1V-dwN27HmjZx0rxI050VKwSs6iFSBSSUCNh3lfnozUHusIbKUKP8vjetyVuPflVFxU0WdEWaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3d1564cc.mp4?token=PANSf8bF8Rz1RD5cHR9Hq5-fnTV-oPGyC1H2lkKhX5PJZkNQl6t76CWzPWtQmtcSuEuE9jRos7C4n3HZaa0oqSCA74jcHCQEz7zGl5Z-PGOZiFokUGUe1QnS4FCziEWcvUJ1O7y6cFjpuspPwdwxPEM0NppUNzVLMUUO1V9pC5i5WB4wwVhNjCoHo05IKEqo_SQOSFz7G363-C7x9ysiy0bc9BiSULHqgFfp50qEYg2V-I1r2Hrgud-7WOozrYEY1ej37xlp13m1V-dwN27HmjZx0rxI050VKwSs6iFSBSSUCNh3lfnozUHusIbKUKP8vjetyVuPflVFxU0WdEWaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی باخت نمیده یعنی این!
🔸
مسیر جایگزین کنار گذر پل هدف قرار داده شده توسط آمریکا در استان هرمزگان به منظور تردد روان خودروهای عبوری آسفالت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451988" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451987">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT7h2NJQGPPxtSXiw-YZ8PZVDmE4Mzr1m4sIZr9AxqzNBOu6yh2W50oMCD2Rd5yKOadBJep1R5sh8Lor3q4TEPli9nbNU3u-65RVehxrTLBzG9Gauh_J_pu4k-r5cfHYBIG8K_3N2BjQGr-Il94s_vv4KwwGOQZUELOkkch6bfQSdTtbjnW5ea7TdZhyXm_C4CyeMhknMo55tu3uFRTiGBTuCNasb-ax2xpx09EDJl67Jqak9x7aBqw_JlbPnWhzOY3t5F0iC5rpAcAxzTwgHOPfEvyORaTDoEACkWfzmfsdB23U_aNWuw7bA8FkZAWchQsAU8pFRyX0lYIaHhBuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر جدیدی از مزار نورانی رهبر شهید انقلاب در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451987" target="_blank">📅 21:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451985">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9ab32bf5.mp4?token=BmvFL0FyJZnosHl1QoseOVF8qDsOSnWhHEfYmFJbT4M2XupdUvOyCLB-qywZVI4s3Hb9-U45tlMCqBjYlchiHM4mykDOzyRv-D5_TVj6g0NUVyc_C5jjUk9X7wpZJmdNHBy7Nw3EFiZ5fux9GF1pApEd5Ld3tTpHLSmnK-fuu0TozmteqWqS1mbU_C3sHHFfFjxdeSDa7XwDvltrDpkOHx5Bklte1d08GKn_9Vga3tb5cW6vXxhBWUclMRcWtax2_KPHu4MeY0G5bHK5_O-27GlkSUFNuFp_ONO1wOFfHfApWsddRKkEGWBmqfQGqIsDwk8FzhsobrY5KX5xGu0YPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9ab32bf5.mp4?token=BmvFL0FyJZnosHl1QoseOVF8qDsOSnWhHEfYmFJbT4M2XupdUvOyCLB-qywZVI4s3Hb9-U45tlMCqBjYlchiHM4mykDOzyRv-D5_TVj6g0NUVyc_C5jjUk9X7wpZJmdNHBy7Nw3EFiZ5fux9GF1pApEd5Ld3tTpHLSmnK-fuu0TozmteqWqS1mbU_C3sHHFfFjxdeSDa7XwDvltrDpkOHx5Bklte1d08GKn_9Vga3tb5cW6vXxhBWUclMRcWtax2_KPHu4MeY0G5bHK5_O-27GlkSUFNuFp_ONO1wOFfHfApWsddRKkEGWBmqfQGqIsDwk8FzhsobrY5KX5xGu0YPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهردار نیویورک: نتانیاهو باید دستگیر شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451985" target="_blank">📅 21:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-4vjsCRBU17yWWeBDuC_TW0Z8S0t_ZUAuqzC6ZkbCvFkTMbArELmTfkpeGGgS9SV4JMBJ4nCSDJYmibKLPipwqvE0KxLfsMIT12bxaI_UtZkivgh3hl6OHN-qtEDO2zK7hDXZajRo5U831KLLJOQMuUkQRVCqpjKiL80ImVdda0e7sxfu6rgqRYRQTIsQKWBYcolY9IlVn6f9QNHzdLJKl4dleUpO1-84gEAvj8MEN8MiO3wiHFVVHMFWQNZVg6kJXgrwXcjc6DfZ2jqoKSezIymMKLWu0MBP6Fn6r4ury4pp03LOAwYI4ImmdEazoxegnPRs9upRfifWY-dh1X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه به شرکت‌های کشتیرانی: مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز مسیر نابودی سرمایه ی شماست؛ فریب آمریکای کودک‎کش را نخورید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451984" target="_blank">📅 21:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpYCrpke3lptUo83Eqh6rhWOkNEqXGMmKwBQIsFNm9eJa6bO4rQQM2hHAz-Z93QDL0R-NI01CJGPorNPpmvQQCwWWrYbGpS43cSwOTrRWXbKKTHYdOR4kIaB0fiR2oPWfabzPbuoeEXDNdyS-DyZ3IIor9VCx---tcwdO03fk144mEyP3grNoU7A9U588_3q49ja4xDosHtuJAEnthwfr8vhv69pIJZDGZlU3kAZEBxMdCPC9HATAkuCazwYhmFeV8vydc30aT3hCAMUWAJ63cK5kE11vLtQpqUSEGVJG8IUDB_GGhkzIr6ucwsw8q4ThdD_Zf80E-jA8SoR_opuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده هوافضای سپاه: اگر به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451981" target="_blank">📅 21:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=VcCu_dkyPJO7Hn_64vcDn9PWZSgKXLT50wNCJGOUOU6hO8-W-38CN4HR9XwEB7BKBLzva-ckdjKj2kznsAKjac8pGSOAy-14NHggKoN3mleL-0BKMGQ17m53zd1KV96xVgjXQdIMBHPfk_LRhXBwNZCGleGLkw72eI-qtpzlZMTKkINxSAC1-u7wnJj-lj7AFL1ZWsPOE6Nzp7h-yu-2nOh62G2_lJXaI7xYkSXYUdhE0w45UtUqZFtOY10FuoIG5OcpX_1S4ppzZM5qMoGMmZz4gKTqoIj46WiMnsEJEoQos6iOvg3LMoc0GT6ibX7C3cuBhEw61jnaJuW3ZnEjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=VcCu_dkyPJO7Hn_64vcDn9PWZSgKXLT50wNCJGOUOU6hO8-W-38CN4HR9XwEB7BKBLzva-ckdjKj2kznsAKjac8pGSOAy-14NHggKoN3mleL-0BKMGQ17m53zd1KV96xVgjXQdIMBHPfk_LRhXBwNZCGleGLkw72eI-qtpzlZMTKkINxSAC1-u7wnJj-lj7AFL1ZWsPOE6Nzp7h-yu-2nOh62G2_lJXaI7xYkSXYUdhE0w45UtUqZFtOY10FuoIG5OcpX_1S4ppzZM5qMoGMmZz4gKTqoIj46WiMnsEJEoQos6iOvg3LMoc0GT6ibX7C3cuBhEw61jnaJuW3ZnEjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: حکام کشورهای عربی در جریان باشند ایران از عملیات زمینی نسبت به آن‌ها ترسی ندارد
🔹
ممکن است صبح بیدار شوند و با اتفاقی مواجه شوند که انتظارش را ندارند. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451980" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451973">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTKxWEhzwWO6PfWg6vLYHjPz76DhQNd7rzcXTWruROKpt_v6QpNdhimzFSIwGuyurwEaumzTXl4iqsrN8Brnsf0iCxyGFb27pP2_UXaqw4fiiT_MZU1C4WZT5Ne5vg1RIO1iiq5z2sOc-rjBYwaGuRutnmlNNGWtuNdzr5ZGkigVD4g4jcRFFCGdeAZm5WaziB6Ixb7oDbbD-PHg8a3mpatURhRLUH67gE2nikw0RkjbIs8ol2nkBTIloJ7gbDVgRcL0zkf-owv-IJtN9KRy8Yq8kjWwbESGVK--Ypz01qQS4H0k-0VweS4_kEHTraWE6ZumOsAz3YCpJK_w8_dlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnfRjEVhpGnWPuvKK_YNMWnH0cMmjw77Y8qV_JJzYEPo0Jy-wZuq15B8z3ZAk6C996H4FrN2b7K__oiqA-ZGm_B7tsDdREBqrUmMI_3o3GAvFiJP8w1k0IL9JJ8unCZQKHTuGW964XXBymg5txr0IB51SdQsVMrh1_tD1acdBHv49t_Q7BFHqWioGxxtHRDa0MeD0ly9S9Mu2Bzlui4U8anaZZHOo9jFg3AogrtfvTI1ih002l03xU6yYPXN9sqGS3AI59zgxMnk55EwJoTyKFDQAyHg7pks2RrEo_4s-Pz12Ti5pfTc51mjwBkyv68GcJdS-gIR6xEuhufbmOm-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RORQBQeZsjenSe10NeaArjipPhTkj-AOEuR90Qsrvpom0whrqd95iUKQspvBsEXCbSpb29G0TGPVvjhYjg_fpVA_lWbLMOCqq_rAu9C2ofSIqCHLyvKqX_HD6pW98YdLhGeMeWK4oc0ymlH1Vm0TFLc3UNUmNWQV7LvrqMPOo-8wy9x2zQXXJk0TPwFqRpKKOCQjesDXZAL3o_ED-biKRJVomS56O_8ngUWZUjgR66kYtFGxva8i3LdVJ5prmYivFzwUqhQ-q32-oWyPEDHPmc1v8YYFiDv7_WlFOYJtALpQz3Mlw5L4mlA33UD2Th-URKZyJmZnR7PelmwYl_PN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo2mD9GytheZczJp2SN3vHhm9IWSlahuha2-ETkV1AF7-mCchWKC8K09AUtxB7RSjVTyhAOev4RE20KPRxbVKQBJHZUg2eFIni6-rG6U2QKWgR8_XuU5rQpcHYX5DbcwWFnkuemBEx5zQLk-fBO-9o9hWSBCgmdylQ5pjsN8OkP0JbwzdoTMaD9sLWIYUrapsuGRA0IVUNPaMykLzKkKT931XMcv0VXS4PxqXdsj3rjZrR8JFLmtDszcun7kBvnWv_KQe9VcPM5yRJrPwa-HY2STthXAK9i8yuJ5eWccbIqKr01Fn8smFqvc8-JLhPjbPEj7bPx1FWKRMa3rQLn7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-bzXJESRKkV4AtI6PHpWbqnMZCfm1BNXkwpgThQHmoRudvi9BpyAP9uFlqWkUJHodATAQz4cn_mW1mShPOLjv7IiISDTNbVdZTSLEdKJHw6Rtc83LtGKYVtzFFPFvweX2451BUQopmUTpZpWjCroH8koDXdvGAVqgI2Rt1pV2Kx1aL5CPaf0--ipn6U4bHdpzmTMnJpeCvb5u9Yotjp8rrAXmeoBzXVwcL06kQagYPF-irkOgQqn7O43l9wq8H7DOkf2hpBLgK-meu7n1_oDi9DmD18xc4koLfcCNGNl-y4dUAyVT7Q6rqvJFdaqrhzzHPPc8yvtZ8IKcfGDurqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHDAZOA0GMx8yEqvPlIGamSFtGJXhA0SAtAifEXLQ8DhDsFQPioY1ATRZC4RRo4036sZm2CLJ_MD6Rj35V5waOkzXD1j5bZqBfxtDVvWEA1Ndxm3ywSN1cNLur-VqF7jdl2KLaTPtUBIMq7oA_JgKZzqi1qHPOcaFaxL2ZQ9zOjy_lC-gBVoDaJU0eN-VKm4NPfaXpOhAZY4ukf4AhIsmPzYdReCaFKFNk96GI3ETNGThMMJOCc8E73t5YHoe6-cSzWmJ5zx8to1xiisoOXEoPT-wGhrfiH9f8kFsMImervP0n2ux62n-7J1j_Wd61krIJSlLqvp9z0Jz8kEQZ_mzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVMmd757nwvgPtbHDFXMDQmiyxeVok56vjdZi6An1iKUV5aunREz1oOOF0jD-wfDudC6Mc7Us2ziNbNK_bHWULpsj3NK6rPfJLCftCwcgVgklpbINRr4rAV1KHtrzIuETr3UII39FFcv6vzLb2NgAO8oKVLvOzpgvdmUsq40rZ9Jqqr-cwSaoKE1BorXPJoWWXLsS0ZiL7NKmAXHKbH52HdYPKxdTA2ZjJR7vUY_f6kfS6PdA7qgG6uFGo5royIEiPXS4THKrHOhwmvXVgaq2DkqgRcUXB8O0d7t5_o3YmLX8xvDezefoJyttHQKYTT5vjw7NfmbStMzpO-gmi3srg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسم بزرگداشت شهید مصباح‌الهدی باقری‌کنی به میزبانی خانواده شهید
◾️
فردا؛ از ساعت ۱۷؛ مجتمع امام صادق(ع)؛ شهرک غرب، بلوار دریا  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451973" target="_blank">📅 21:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451971">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYGfCnOrMO16LrqPpFYLZkKI9YAO7UCRiQOBb8oxwlGY15SiwhrHi414Ns43onYmhGyTgMnkbsYwGWr4QezapUhwBTwndlvH9m_F_EJ4MhvugUea4wlmL71P-r_Z3aNfJPwsNClxLH9Zy_6b_ylJLCJRcVubPLZbGX1t9kOZA-1vDO-YPAqzlv-aojdWmdm1MqTz7niGpmgfwlYmmv-h3Abh0Bk5zra9nSrUuk_ThpH07iY-DCosclP8YZwj9zkmhlhpuM4dIWHYEO-ZJL3oWC3O3Y4oGAUYnliVldmK57kINNTLZqYJ4trOl39JWsg4rcQNeyA_hlFNGBdBQwc4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نیروی دریایی سپاه: اخطار می‌دهیم که از مسیرهای جایگزین تنگۀ هرمز استفاده نکنید
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451971" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
منابع عربی: صدای چند انفجار در کویت شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451970" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451969">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c645e09a1.mp4?token=LFYClR7v35O-AbaTwArSPSGJj-fJND2sp0kjtusiyR8AnpXeIIchzCqAwyx99Pjtgrip5-5bkwTBVmCezbrE2-28KMtGkdL-c7nCihY5L0sm6qWgsZ1nWK4PIN8q4svOqwiwDJPFiKrFAQnSMi2fyI8wj7HncA_k3KExNzjnHGXVbSv7p0D1-KwDfBT_saGZ9QNZAdvTZ6W9921s0igbj-cp-VXvXWiTC56-4l--Lq0V-4SQgA6bTFQEh4NZnehkTE75-0ofMrrHqKXnlrfBrP0QuqsG_sYb8K6HAVItOLqbGnB2xu6lIhuBb2mk_RJQ1Efed7ATHFZqq7f9AsDWxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c645e09a1.mp4?token=LFYClR7v35O-AbaTwArSPSGJj-fJND2sp0kjtusiyR8AnpXeIIchzCqAwyx99Pjtgrip5-5bkwTBVmCezbrE2-28KMtGkdL-c7nCihY5L0sm6qWgsZ1nWK4PIN8q4svOqwiwDJPFiKrFAQnSMi2fyI8wj7HncA_k3KExNzjnHGXVbSv7p0D1-KwDfBT_saGZ9QNZAdvTZ6W9921s0igbj-cp-VXvXWiTC56-4l--Lq0V-4SQgA6bTFQEh4NZnehkTE75-0ofMrrHqKXnlrfBrP0QuqsG_sYb8K6HAVItOLqbGnB2xu6lIhuBb2mk_RJQ1Efed7ATHFZqq7f9AsDWxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: پنتاگون هیچ سخنی درباره تلفاتی که در حملات ایران به ما وارد می‌شود نمی‌گوید و پنهانکاری می‌کند؛ اداره این کشور به دست یک دیکتاتور افتاده و این یک وضعیت رعب‌آور و نگران‌کننده است
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451969" target="_blank">📅 21:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0079f094f.mp4?token=flImfblpKtTksGw4eD06qEVMF3G0laW4u-METgqbMCBEtisyfLcEEKrFzHrDCDctsZjH2bIZkCbJQ07GU_BlGLe0NEOnCewOTAEm5YNZJlcdghqJ4xfYpaAoG1JXgV8aCFfiWySuvFJ3e-sbQ4V6dBD5QlU8VW2G-PG4-rHKeD_T6XnVKKcGNgve6v_Igj9gTt4J9L3cHYKpb1WX6gaBYTRZRHtP5mJcal4EYeIfQ5euZEFVjzhlnROYz2tEzj74G85oulvMa8kkXJoaGjT1gdD7EptDWvPzkytObDyYLlU4xvP6m3CjAzxuvXx_kkbBA6nvrApWnS8JwmGOTqsG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0079f094f.mp4?token=flImfblpKtTksGw4eD06qEVMF3G0laW4u-METgqbMCBEtisyfLcEEKrFzHrDCDctsZjH2bIZkCbJQ07GU_BlGLe0NEOnCewOTAEm5YNZJlcdghqJ4xfYpaAoG1JXgV8aCFfiWySuvFJ3e-sbQ4V6dBD5QlU8VW2G-PG4-rHKeD_T6XnVKKcGNgve6v_Igj9gTt4J9L3cHYKpb1WX6gaBYTRZRHtP5mJcal4EYeIfQ5euZEFVjzhlnROYz2tEzj74G85oulvMa8kkXJoaGjT1gdD7EptDWvPzkytObDyYLlU4xvP6m3CjAzxuvXx_kkbBA6nvrApWnS8JwmGOTqsG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ‌۱۴۴ وفاداری در خیابان‌های لامرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451968" target="_blank">📅 21:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451967">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495f9c4e42.mp4?token=p937q1drLua1wUZJd-Ak8d2qu3YV8iTTjnyPxWkWU5uqF8g2IApqyUpy9DgNMUl9lOMFk61rptQepNGs32hKZ9yGOxuAywup7_axkXCQ30yAFjU2WTFHa05Q1pQ3Imiu9S3xts_3N8DvnZjUo7RaVOK3IWOG33mrl2FDEA796JoIug1hURn7rSD99PWmGnWoEDXx91xElbT-5scvK0uXUxgkGg5qIcareF2GqiaRwgcTQC-ykJgUC51N8YMahhZNZqojcTR64w1JjbfE1H_Qmppu9RMeLiZoBqHkGZoOwDVEcZyBltSfDW6Q8NHvJXbfmhDfGwq3oe2iqzCpdRl4CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495f9c4e42.mp4?token=p937q1drLua1wUZJd-Ak8d2qu3YV8iTTjnyPxWkWU5uqF8g2IApqyUpy9DgNMUl9lOMFk61rptQepNGs32hKZ9yGOxuAywup7_axkXCQ30yAFjU2WTFHa05Q1pQ3Imiu9S3xts_3N8DvnZjUo7RaVOK3IWOG33mrl2FDEA796JoIug1hURn7rSD99PWmGnWoEDXx91xElbT-5scvK0uXUxgkGg5qIcareF2GqiaRwgcTQC-ykJgUC51N8YMahhZNZqojcTR64w1JjbfE1H_Qmppu9RMeLiZoBqHkGZoOwDVEcZyBltSfDW6Q8NHvJXbfmhDfGwq3oe2iqzCpdRl4CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صنعت: پروانهٔ واحدهای مستقر در شهرک‌های صنعتی که از ماینر برای سودجویی استفاده کنند، باطل می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451967" target="_blank">📅 21:21 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
