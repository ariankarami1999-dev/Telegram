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
<img src="https://cdn5.telesco.pe/file/PpQsdMp-cW7KjfsaJ0lPWHcJhECRgDQ9-uk8ulpl2eNhgByEqOVTHiFRDSxstdUiNSw-6AXQZ6CALjNlDYjVQLHbP07LlEoBnSkweytOOhCZu5r9DoW0VCtzIrgJHfKen-C28xTxbBMZFDDEtFaxfuTb0wkGfq-i0oEbf6hnEtbRA62RN732XhhT3ybdIrFXfvPzthclRxLA1dGEEZeSE-CvxmUmdp_Kw-6Xzgeh_UFz1N7s9p4sSsY-ZUXXct7bfcK1aU3JySFKdtK4JI7IIULPVJkoiNtC1Ct0WrTMLaC_QJ86uyNEdEaVp1d9iUSPp7OUblsyP4SDIycUnlcvHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 697K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 03:29:05</div>
<hr>

<div class="tg-post" id="msg-96500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه ازبکستان با اختلاف 7 گل ببره اونا جای ایران میرن مرحله بعدی</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/96500" target="_blank">📅 03:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f7de6f56.mp4?token=MEUkNWs5NOKw2cBS0SK_ugkPnb36EBdxl7HzhNZZtxK41JUqJnSC8tNQLd46my0WDbEBGRBsUsYx50ylIAvKXFWPndCoDr0hNyB0TIZORLgZsbjOUCZcMgkiaHN9Q-64QL-MuyrLhQG_0_D7E17VJpcfDa--AhcGPYYUsVDS1tSD4YmE09wvJPJGKt9FSN0OUBy1CXvV-GgteTrWpr5MYZAoa6mcliMe36awiG_hOpuKSzU2En5mWNwOIsXUOt5UvwZw3ynR1PS2lDcrDHfCUKRipv7GXAjlBLbm3kwMPRYlO8ns-BnTFuplOinSIaAdsQYovgYfxA6DZGFLDnSGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f7de6f56.mp4?token=MEUkNWs5NOKw2cBS0SK_ugkPnb36EBdxl7HzhNZZtxK41JUqJnSC8tNQLd46my0WDbEBGRBsUsYx50ylIAvKXFWPndCoDr0hNyB0TIZORLgZsbjOUCZcMgkiaHN9Q-64QL-MuyrLhQG_0_D7E17VJpcfDa--AhcGPYYUsVDS1tSD4YmE09wvJPJGKt9FSN0OUBy1CXvV-GgteTrWpr5MYZAoa6mcliMe36awiG_hOpuKSzU2En5mWNwOIsXUOt5UvwZw3ynR1PS2lDcrDHfCUKRipv7GXAjlBLbm3kwMPRYlO8ns-BnTFuplOinSIaAdsQYovgYfxA6DZGFLDnSGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سخنگوی قرارگاه تیم ملی در جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/Futball180TV/96499" target="_blank">📅 03:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📌
امشب، با سوت پایان آخرین دیدار مرحله گروهی، پرونده این بخش از جام جهانی بسته می‌شود.
در تمام این روزها تلاش کردیم لحظه‌به‌لحظه کنار شما باشیم و هر آنچه در این رقابت‌ها گذشت را با عشق و تعهد پوشش دهیم. همراهی، حمایت و اعتماد شما بزرگ‌ترین سرمایه ماست و صمیمانه از تک‌تک شما سپاسگزاریم.
اکنون با شور و انگیزه‌ای دوچندان، به استقبال حساس‌ترین و هیجان‌انگیزترین بخش مسابقات؛ یعنی مرحله حذفی، می‌رویم. امیدواریم همچنان افتخار همراهی‌تان را داشته باشیم و اگر از عملکرد ما رضایت دارید، با معرفی مجموعه
فوتبال ۱۸۰
به دوستانتان، در این مسیر کنارمان بمانید.
این هم خانواده بزرگ
فوتبال ۱۸۰
؛ با این امید که در ادامه رقابت‌ها نیز بتوانیم بهترینو کامل‌ترین پوشش را به شما عزیزان تقدیم کنیم.
همراهی شما، انگیزه ادامه راه ماست.
ما یک خانواده بزرگ فوتبالییم و میتونید در هر بخشی که بخواهید خانواده ما را دنبال کنید
⚽️
کانال های استقلالی فوتبال ۱۸۰
@EsteghlalPage
@esteghlalfan
@EsteghlalFans
@Tajieha
❤️
کانال های پرسپولیسی فوتبال ۱۸۰
@RedStarFc
@Perspolis6
@RedStarFc2
@RedStarrFc
❤️
🟣
🔴
🔹
🔴
🌟
کانال های عمومی و خبر فوتبالی فوتبال ۱۸۰
@Futball180Tv
@footballbartatv3ir
@FootballUltraBoys
@ExtraTime_Fut
♨️
کانال های اخبار جنگ و خبری سیاسی ۱۸۰
@News_hut
@KhabarraK
@HutNewsPlus
با فوتبال ۱۸۰ ( مجموعه تیوا ) جام جهانی را با هیجان دنبال کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/Futball180TV/96497" target="_blank">📅 03:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6362053e4b.mp4?token=VEy-LhOtsTb9IGt1fgkYBMJhBCx56s5lM2c9qMfuVOdhF7rCTh8hNbAaLNSzIIDniqGK3cIYAi8VXEPBMLAU581PJTwO96i00vhoX2zf2y0LSutL1XYxQ2duvF1v5w17t6zc-Zx1jPVucE5EAS7FyivRn_nosgceKiZhn-jrALZv1aYDnwqon-AML8bFz_Eda7zTitc1n_Dm3BgZeCT0cWoND_vjMml1IiwOsA0CIY-fN9uOq45Nv8JSpOOPnWV2Pp3y8ZlEg13wKwIZQBMnUjiNoTtESZoXqoK_0cDLJrag5U97MUQHfUCFK-_GNEMq1OIL7QKbmUWhb5LUuJ1TlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6362053e4b.mp4?token=VEy-LhOtsTb9IGt1fgkYBMJhBCx56s5lM2c9qMfuVOdhF7rCTh8hNbAaLNSzIIDniqGK3cIYAi8VXEPBMLAU581PJTwO96i00vhoX2zf2y0LSutL1XYxQ2duvF1v5w17t6zc-Zx1jPVucE5EAS7FyivRn_nosgceKiZhn-jrALZv1aYDnwqon-AML8bFz_Eda7zTitc1n_Dm3BgZeCT0cWoND_vjMml1IiwOsA0CIY-fN9uOq45Nv8JSpOOPnWV2Pp3y8ZlEg13wKwIZQBMnUjiNoTtESZoXqoK_0cDLJrag5U97MUQHfUCFK-_GNEMq1OIL7QKbmUWhb5LUuJ1TlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل ازبکستان به کنگو توسط شومورودوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/Futball180TV/96496" target="_blank">📅 03:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پشمامممم رد شد</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/96495" target="_blank">📅 03:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96494">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رفته وار</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/96494" target="_blank">📅 03:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96493">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کنگو گل مساوی زد
نیوکاسل بختتو
😂</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/96493" target="_blank">📅 03:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96492">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ازبکستان زد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/96492" target="_blank">📅 03:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96491">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/96491" target="_blank">📅 03:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsBdIMAeBk8cLAA3lwnzrW2bg_FL_hKKSX_6KtKAy19SltqH68mPwvkLPcC-9cLsUb9xv8AmixgkV1XaHXWPvzgLamuq7MKbQwFZqBU7e-0bf5EIY8qHAgZJRtkWaVDe1YMrSzXwDbqNpMOG-z8-DY-bArWSs6BdFIRaDEGnkK1n5QiMyU4bbzLCxAz-Uk06d6xujikDlQ7zrTXRMmktSTwvIn1tQnXmGpDE_610Kxhmbv2SrV0m0J9p3Gz__9DpR3CgPT5dG78f6YpDcBXxRHbf0FdEMhURrzqu5XhxYQy9z-5dlXBYeq_taJNsXMvozw-9EC_ZRfFZR-TxbFAx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
ترکیب آرژانتین مقابل اردن؛ 05:30
‼️
مسی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/96490" target="_blank">📅 03:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APaIlLE7vhXGJ7FWe2oJfHQVMT7epN1Upx0nQ_AC3v3ROcuaWLYoqa1dlMA7JpORbYz45UDpRWrHRWSbocDfBUBFU9ucVnEVs9B6zPBRLPUwi7FaqBacjCsLOCMMVH36Ax6d8parIz8XpxiWQHgcoaWIgfWfQe8gaIJYTbksxjav7Iq6a4E5uXifwjtOR4BbNpsvAxVr38ioyxGzoVKeGMZJv7jy-gKuagNYHnOU-72o0XUKsDpdW36f0LefB0XbkKVE84MZlaIrq9kdqfOZ6NmJLPLMPBwQavqggapc3f-KytrlFcevHhmLrwaHie2UOS8nvGDOLnseTbFPbhH6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVdvuoex5cXNiU80rNteCa108gXOucuAxbLHjt237aDxdgns5Nyjdqmcdvma10k9Op9bTdtW9pHLXzZmC8BK08L4Fpy4EISH2_XUTXsz6a4DKOe90LhrTO1Y3FsbRxM0C2S3noTJRLfTijqW-NaBUzEZpD9pLkpTKjUjZo4LS5WP9gbm0wmgs1krxNGZHrv1H5HqME701tm-1YWisjmpWPAuRhFZEJkA5bkp2Bb3AzIUKpkzrbecBK_ajYgjQCnW8UWBOJ8h0EVq5o4b7sh0nHm4Ap-M1mdLezy7DGX0JfIo2580tvFiZuWIPZ3wZ9yBOvKR6G5xypkpiQXdftRBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhwY4_h4qNDRWzmXfeW-tAVz88rxb6Gtqk6kfJTkuZ7US9F5nZtCSsh_rdtqIwcz8ZJJULHz_xSgka8Yxk_zRQa5mlSnFKnyjNFdBzCZLAKHsYlKKBBVL9yolJD4e2SVvyvKfjr5dJrSOPyYMs8vj2plwOEzq_Be-ajQZteP0uTiKqxOiKmQ-hP8PSGGtZNZomPOut2yA8ki9qwhb8HT3yGwoXbAAlvZ-StW_yntBulE6dWtT2qnB1gL3g99sw5iQRPdTrRxiD1fnOcgw5Dv-V6A_zi5p2oc1SRB4THAWZGnKDEpZvCaVPt9RNJuC_jxn1e2x-U-pxUpyJVMYm7a0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLSgVJcCBjDmnHFijlwk93uJddKVsznwuAuV7GISDMOXGvLv178a8hDmWeDye9OUjqqaf8NrfKZpd9Sd_NjyHBBbd0BKfrLvO-w4BTljhTq54GhiaCDuDMxZpPXNBS_rQRiFvAqaeRpDwnLTafnTiBEKKAo1HJIQ1yJUWOnILrGbLjBIxZUHM9PtC7BJ6htBi7vt6hdTX-nI4B30lZQCo4AXxLAGK0StvK03r0TWunF0ybaDnX8jUUROMrY_0jQXr0-g4zYZKGN-vr3-z-8RPvz77kId_H6qf98VKEwqNySUU_LSQEOn-Cl00M-4Su_cJviXxurN2CbzmrLKCLLFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THh_uo6JuOp7CLbMOnSnQLBItifgIlpR2D9H1AuOzB-kojbmBIMumsXPUGJdzCt6Gdkbctv3jXG9LPYi3hgR-I7H65sD2adVlj1jjdSDHEvpVCXm4-zE1jSB4g96rWJpNSge6eus7K0aZtCLUz5Q6pY63_ELmzZ1xf3yy5W42LEtdDlInK4_XlYmrMJwesmfAVs7zu_Af86ifMZ-mO-h4K7gvArnEGp4dyrH1ae-QwnPggFA8Pq6IDnBiFnpmspDF2qDKwnjnzDalXNlXqnmlQiPn8-9hpXNAYzw3loc-uDr_fQJ_1Cl4ylUp9hUYEHT0IgUu2V0uDvKVamVOkQ15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZ_PZTQNFFH5KQSIYScWOt6Ao2RZhU5Wnkm6vU5zIYiAz11EUJ8MYVkq7hXtfwqde4KAPwem7gTZSCVY95oBbl_veeo6dCcnQHMRDO1o3trWB1tOQyuDjsW_mBl__6g3N0Dr9PBCOITMIb5lpe01XokwehVRM8FvuEnrTW5xH3QKqdWDeNJSyzjMGTqUfvZY4FBEC78M5z-iV51nm1prbY1E1lAvlXRxTu8zWWQXtxEchrMW_y_3reE0dVJvPciNjR4OxJmMkGjsmguIxObKJgTNWQwJjGWcmS2VhhsdfXA27f-BFHjfqCtHd6XIK7dKJsl_59uBiUy_NqHH4WYJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imNWfm6qTxVELHUIor9O9uxCLQVmGfsL-ANXKkBzWMa7B_mrcKW64opm_Ab30cXuTOzEdjVppjQLPGjf4u40SMLA9SHYSOEEYbbY34aWsl655ti2r3FzlnFAKpf1cTQyLCy_CPDhSXlln1b0YpZ9P_lzmXtgzkUCuFGLCBQ93YlJJYRMN_N-Ce8gIkzrAN2hMUoyLx3afHRRO_L-7pGqbo7c3pUnWUJPeTHt1rFj4fHHDGbboYQj_ebXbMB390hyHksRU5yPrCklt7UVKin35REZQRiX-Ot8R9ArlzIrhR1OjsAP57b5qSF4CvbkiRTsMoM2BVxoAkBoe4VFvpR7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUS6-i8h7DLPZB6UoAYEQKgIudsOkvxnmh5dWRReze3CKqZYXRLQhCla_cnaXNv6XYOM_zrOpCwvhE50wdQBXM4W5MxQRBkPLVgVO3SQshcnrrefxR_SwhivgrqEtiho66QhDkpGa6oV08DHbUao2XLydk5z6yRGMvAOPI6qGysPLdPw70jZ2wjCCi66AAScMQnup43ECLba_C-ixvuj06jhnqGhcYMECA3ysEktkQhf_J1SXpmS6Z5mgoF36RbcnKjt9oCVAP3o3ArVbmUYAt7o8pLyf7N-FS-wahCfluk_w7SjMZD4l4FSwq8NcwPPlZKKa15MUAEDmoiFm6vlTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1iKR-Jv-by7zzXdBw0Bh5EYYdwBguZo97J4fOB498wuYkkmYAnJgYU7YNm7VVzQhX8cH7prWt50sVcb1QkjCj_2V_XwfFEkd0mIqdXwMOk_WxHXMRr75LF4aTn7h8p019Tsmda04dIlMViSykowcvW4oxb43eMoamuSI8juVZYk-s_Ij9dL_l3sr3BajN_Mu7mUmmTY4to4gXTDIVl5quB90AJLXiQSU1PoFsXXGcjxGG4CBJ2t-cmC4EJ-YNV1_GsMTMwJvOLZUdMTN4K6ClWSQvpT74X_0inqeXVuqyRMv7UnkS0bj2KYJxX9piRXZx1oWUn7nCrBETY1pY8x8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYwNrhiSwLVXr4vShHsuAlnTV2s9vrGPGMjsdEpTPK7gobLwo_JOUQT7KRcNLp9hpMRmuLoA57Bpx81Oh0JW90S0kwo2KwrYSI-FdOsRDWMtUvQ2yOkkTSDQPJa477uAAOmOJECFAwtxUvqfHK4zJQBvff-W56f5tkWqG4leYHpkMJVku552_mbDjZjSZCXtWRTfiBc_qa8Z97G0XeFfWF9zH8Aubj_gcoMXoFK24XmaWn5vaBf1InvRB7_Q-Mk9_jucIgx_Z_NXFQB3Ii4Wrj9cFCOPY6X-90WTBJt2UKWGX3gsBtMuErTet0eRqnCCQ62f2ZEgnBkqT38cdT-WWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای پرتغال - کلمبیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/96480" target="_blank">📅 03:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ازبکستان زد ولی افساید شد
ریدم به بختت امیر</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/96479" target="_blank">📅 03:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PODzRNQXNQJ487vd4l-8SAGTZh4ukmURgzYbqBNTUZpWIPJFwhhpmJLlPbVUTwWG0ri7J2GdV_yPvE3ANYq1nxIUO39qihfWg2uVfPPa5Cxw073XBtCU3lUS6SeSFXJZdDfSybYrCbdLq9351spngWPOhoOYsaOb_j7u2YoDxORh4W-MswrBk9XwLgdgZN6Q1xE65LY2NP8KsPYctZ8uehNJ69UzKyyuhIQul7-DFv8pN-ocSCZr3e1g5kURRS1YOGEqndnHIIRS8Cu0cb4JoBMNF202aSue6tmBzx1d-8REwcrEEQ1WttRWZoS5WSJbuPHfVrjqfSqieDkyuoPViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ با 40 سال و 292 روز مسن ترین بازیکن تاریخ جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/96478" target="_blank">📅 02:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIkSDEHzzoWliC9GNkQtmnHoOZpg-o83XQ9jGTzglhPVYHP5tuTM5jIEdgvBQqhEZbWnXRSsiApPjbzT76bRf6p-BoluoycsWO2g9kfAhe9f1a9V4Xm5FSPlpBq2YGokjinZWd6e51PCJvM8oPVaBssjyR1wJWco4Tp-DqFS2bGuquBdbiiMMKADlbfu2LYu-OndqnBW2n6dmQ0RfmeGFf_gNVcr4HI8C-xTDFlBhZlGOJsrGXeTo_D0jUyy8muFuWhdP5G1ToIn5DNBV1ihnnH5maN9sDk_txJczvMnzGvs8MJ7CrgfBjtfvgjeJGjmZyfjEkyAUxs6TC8oBIGrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول بهترین تیم‌های سوم در پایان بازی‌های گروه L
شرایط صعود تیم منتخب ایران:
ازبکستان موفق شود از کنگو امتیاز بگیرد
دیدار الجزایر - اتریش مساوی نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/96477" target="_blank">📅 02:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1-Iz4dONKtW9kJvXyu3xTYYpHyxUxDIJ38CL8e_7uS1YV5KdMfeIY14J-5L63_I66evjgu7-sWhPZsIEs0d9niq_6QSHd-ZCqrx7f5psM5tWUIR0X6LjN2oAA2hgFq5608CAoAJyHikFOmKLZ9prcCoUMkofSmrbZ6ZFJnoOqTFA-VQEYISUnbxTzbrOImQyQnahxjzDSeAds8i77gS_QGG3rtz50nuKZUjMV5UGN8XjleVla_uRK0XW-QigwlsroOwhtN9SGKE2UxrfVhhCQJ7HVdgwB9PNx3OMw77NfySBHHqw---KCPb_z3WeTh0nxo4P4XgRftxnFrKiIS7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لوکا مودریچ با 40 سال سن مسن ترین بازیکن تاریخ جام جهانی است که پاس گل داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/96476" target="_blank">📅 02:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNKE9M0qDDcmhdtqZuk9YDsgF1MYVHXWZNpeGRCh6cXR8zVtEE9QGVhf2j3wuIXvLO-6-3OvcHn4aRGWPHMpLrxhF2sSbG9Tv8UTk6OyLuSvL-Q-cAo-zFpYIP-ZWNt2cc66j1LdRM62-EpIEnX2T35atVV25xCm4VtC1o2SRzvuZCIfJAH9NfOM-cMNn-kF61RyMJDw8cWSWAHObeer5MIW8GJzYwH27Vu9X_6R45ja2T32fLiJX3f7aSuo14DkZfL0R08ApgljCkfrZtw-aFpky1ZJJTFSoI99TnjJTSdkMC4mNasIVTa18iZqiTT6GXjOGbY38zdHxRMvGXUtcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو برای گرم کردن وارد زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/Futball180TV/96475" target="_blank">📅 02:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzjPr-hgFF7EceGwXtKop2vwkyg_6TYbpS12d71p1agNofNXG2Avf70CdepUjbUBJixUwFHT8Xr3foNAtZm8YiiyXYI_9CYUsUvIgL8kjks3C5syi1P-Z0JgGQDMdtG5PmWsICEc93ZUmKkehBnQbgSStscEszUSctD1gS4q4GemagVByXCm87IWMI5f2XacJVasOapQC6ADWxId6jPxJgIZUgSlvFogZCLSSskUlGcvmWqZXlSJIKCz7fwOaGev_aXS92TYAMN41Od3BEuU-lsHW6r0QSvfiYDOiXFybyutK0GC0knLGRpvCCSIbPM-UB2i5_cVii17sNkvdNji9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های صعود کرده به مرحله حذفی جام‌جهانی ۲۰۲۶ تا این لحظه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/96474" target="_blank">📅 02:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🏆
جدول‌فعلی بهترین تیم‌های سوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/96473" target="_blank">📅 02:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz4n59qvFgIXNnAQpoDBD7Qa1kxGDjcYvROP2CPnZB7Wh_Q9Gr1c5luIaTrbAPov_yOaGpf1wwtWAXL1Cym-XLKiZ9SO1viyZrxSmIZVjbYqii31pDnEhKeukwR30eC7OBx9Ihat4yF3kvJeAk81Vkkx49VyGhIk5-Q5tsD0qKSU8RrHL5CyC9wnF0eMpUiDbKxRnqzbABwvGo8oEkzYx9EylZVVb2ZjCWYBv_D_o5creeQuBIIZfBkDPqR0Ejyz8i7r7Ei6kSL86PPS0oudV2B4-xahvsltPqFDjN6T8BQ7IY-uin_WP_O2z_jmMGYhJ__PpxKHPUFFpcBdIB7L0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان کی‌روش نتوانستند به نفع ایران کار کنند
🇭🇷
کرواسی 2 -
🇬🇭
غنا 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/96472" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxH4iFc5Bt2w2BsHkKQHy0IZHCBXdHYY5RePMXTK4TEsQiKymj2pRJdy8YPsrKirp26GP0m_Oa29hm0hgtFHb4z3-YzOpwygL9R0XwP0aDV3sPs7YYXJTIrbUezWrA5LA0xM-KrMOr4Xl9faVs3ecaK4a2BWXJHuRdnDbGkyCI5TFI-M5zlp-YcF7n8eEyD5lU-imH4kgvGxZ_tX7Z9_mqsUTaAqpG21dCMnLDxh8vBIGmm1Iv2_OHHQaQTl4--wxvAsY5l759gJu4GUlpYjLmbV_hDPKDxdfjyTnxALdq_LvS9HcGEPCcXDv8FFBOninXVrzlTSTyy9qS9qnsDLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سه شیرها به عنوان صدرنشین به دور حذفی صعود کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 2 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/96471" target="_blank">📅 02:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پاناما به انگلیس گل زد ولی مردود شد</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/96470" target="_blank">📅 02:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/207e6a01f0.mp4?token=f4AIiVGEnvy0aVo93CDYnn9ZL-3HStN42BS7v-fs44_g-IgKt-T3UqsvXvy_pbMR7SvIpWncDXWCjuFxnV8NKsmCO6LH0eSUSZJevvzZb9sNz5K7jUHmH3OEdvgFnhjqHedjove5Ig9yqk7cwu0BFpLX0cyCDemS9WYfNpfcLUhoyUFrcKv3dDt5JnHhuNyC1dOdBUBhaDE70vRmAUVZZzAv6mSoV0YTgD49CuPU80K80ozHq3aL_wncdU0f5wHdTzWNkDf7UtXsxmM9HtweJ1lN6AgQg_1YWxP2W-3iq6B8uBbX304Ch9oAtpwJF6rrqRiQHgCTfVFpG9q7VTm4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/207e6a01f0.mp4?token=f4AIiVGEnvy0aVo93CDYnn9ZL-3HStN42BS7v-fs44_g-IgKt-T3UqsvXvy_pbMR7SvIpWncDXWCjuFxnV8NKsmCO6LH0eSUSZJevvzZb9sNz5K7jUHmH3OEdvgFnhjqHedjove5Ig9yqk7cwu0BFpLX0cyCDemS9WYfNpfcLUhoyUFrcKv3dDt5JnHhuNyC1dOdBUBhaDE70vRmAUVZZzAv6mSoV0YTgD49CuPU80K80ozHq3aL_wncdU0f5wHdTzWNkDf7UtXsxmM9HtweJ1lN6AgQg_1YWxP2W-3iq6B8uBbX304Ch9oAtpwJF6rrqRiQHgCTfVFpG9q7VTm4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم کرواسی به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/96469" target="_blank">📅 02:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کرواسی زد دومیو</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96468" target="_blank">📅 02:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96466" target="_blank">📅 02:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پشمام چی گرفت گلر غنا</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96465" target="_blank">📅 02:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2539585ec9.mp4?token=IRno9mmSlMNsBQ852-EO4vbd8GY2OQLXMX4V3ew-NCk0PV6uXwt8qszvYZ0MzQCNDwCGT4NJG4vDkaQ5ku2PE7NZhVLCM3lR4XYJ_qRESFImvIoN5TMUBk8Nk3ugzWaXFpbxwhMQSnCkKg0k_wqKUDPt9t8Pfdw2SB7deD1eXmWKzu2u96lsJtYU4O9oNH53N0C6w8Ns9FTrRrNfG2QYKY8J9-_hrS32eKZWSnNyRzVy9zqNdF452450gGRUEsEVH4QtetMfrEXQn5Cq1XNbEtiQTzYBU8WsTLzLAlnHhF36odXcnetsyyA-a0hsTWyDLJs9HfLnWUg3hF2bWQ14oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2539585ec9.mp4?token=IRno9mmSlMNsBQ852-EO4vbd8GY2OQLXMX4V3ew-NCk0PV6uXwt8qszvYZ0MzQCNDwCGT4NJG4vDkaQ5ku2PE7NZhVLCM3lR4XYJ_qRESFImvIoN5TMUBk8Nk3ugzWaXFpbxwhMQSnCkKg0k_wqKUDPt9t8Pfdw2SB7deD1eXmWKzu2u96lsJtYU4O9oNH53N0C6w8Ns9FTrRrNfG2QYKY8J9-_hrS32eKZWSnNyRzVy9zqNdF452450gGRUEsEVH4QtetMfrEXQn5Cq1XNbEtiQTzYBU8WsTLzLAlnHhF36odXcnetsyyA-a0hsTWyDLJs9HfLnWUg3hF2bWQ14oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرامبال غنای کیروش مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96464" target="_blank">📅 02:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6XUP5RRdalVvnHxBYP9RsR4YIsFTEvKXca3NB-FuwROLFWLycU8t-rz2DMxZ5ePt3zteZOaWc5vriYXb3bFsasw1LKhlnIuuVrJ2_sLBlToBQ44TacYEBfGivD0cUELXNT6aZvnJ4y_GEpseabW9AxdwDM-VR6I8-XhMav0PoD8C76q7eZ2453iojFsVa8S2a6C0xJyidcVYij-Oot1VnW-zG2QyCmG6hEPTFrg4XeN1ahyCFhK99R0JJi5lu8TA4ujyb3iQnpfQt383oqH-D6vX8KuE4UUDS54AQqJmWW6uQQIwBsrhXbBUdl6bwNzSfjh6MXPJNyHREKBC4oN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جادوگر معروف هم تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/96463" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گل قبول شد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96462" target="_blank">📅 02:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">داور رفت خودش چک کنه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96461" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رد شد به خاطر آفساید</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/96459" target="_blank">📅 02:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">غنا گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/96458" target="_blank">📅 02:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96457" target="_blank">📅 02:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/445d339502.mp4?token=OPUHEbZQjMLni3s4wT7xwVv0NFhXsuWm9mGNx1ekVsFVl2ZAZJ9oOnV3Gq2Zj4qkda1fMmupsERsN6eXPnDpBzqxEXSXnr2etn4tMPVf7wFqdBdA2kjDKd7IztxLB2mvWotAirj_iz1swD14gVPgf3WPH4rKzvWwNpy5sCc4j2QdlDeKFn7urPGP03GpjAOKTcw7lCgDxyCWKBWcB1TmHPlZ2xTjZaxFYeO5Tz6ZACsrNioL1MDAwI1KsNgJZJ6py0vMuGq8UqVj-Cbr_qU0COxy2oV6sH3vFe2Ezbg20TGGIq7smQb6VS1O7YDFhO9OVpWe3nxje6OuYfSpufE8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/445d339502.mp4?token=OPUHEbZQjMLni3s4wT7xwVv0NFhXsuWm9mGNx1ekVsFVl2ZAZJ9oOnV3Gq2Zj4qkda1fMmupsERsN6eXPnDpBzqxEXSXnr2etn4tMPVf7wFqdBdA2kjDKd7IztxLB2mvWotAirj_iz1swD14gVPgf3WPH4rKzvWwNpy5sCc4j2QdlDeKFn7urPGP03GpjAOKTcw7lCgDxyCWKBWcB1TmHPlZ2xTjZaxFYeO5Tz6ZACsrNioL1MDAwI1KsNgJZJ6py0vMuGq8UqVj-Cbr_qU0COxy2oV6sH3vFe2Ezbg20TGGIq7smQb6VS1O7YDFhO9OVpWe3nxje6OuYfSpufE8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم انگلیس به پاناما توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/96456" target="_blank">📅 01:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96455">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کین دومی رو واسه انگلیس زد</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/96455" target="_blank">📅 01:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96454">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/96454" target="_blank">📅 01:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96453">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5f36943a5d.mp4?token=I2NM9qtTFtUDob_rL2Hq7t4XoAYwjNxyx6XXAKeukGkrCe82Q6ZKDa6_8yr3aNokYNPO5I0Piu16HtOA98NsI-1VnORjzZkIhX4vaQI96Bph37B4slRAPM80Z2b0OuCSNlvL1_RNQDNh95dvAR_Ah-0ZlNqNjlWmhrLIidD0H4dtP2gMf5McsQoj9b95C5S-e5vSr0C3c9suMaMCxqTknhV6J7bV6vTkAVwURBDxQEDVswskT-irxkgZS6sGqRq4o10NugLYmMgJATr7Foosfha-AbF_hhCD0k1oB-cI8-piBNSXO9OM0aN7IplbKAlMuoPNK3KutCgouDOlmRfnMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5f36943a5d.mp4?token=I2NM9qtTFtUDob_rL2Hq7t4XoAYwjNxyx6XXAKeukGkrCe82Q6ZKDa6_8yr3aNokYNPO5I0Piu16HtOA98NsI-1VnORjzZkIhX4vaQI96Bph37B4slRAPM80Z2b0OuCSNlvL1_RNQDNh95dvAR_Ah-0ZlNqNjlWmhrLIidD0H4dtP2gMf5McsQoj9b95C5S-e5vSr0C3c9suMaMCxqTknhV6J7bV6vTkAVwURBDxQEDVswskT-irxkgZS6sGqRq4o10NugLYmMgJATr7Foosfha-AbF_hhCD0k1oB-cI8-piBNSXO9OM0aN7IplbKAlMuoPNK3KutCgouDOlmRfnMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول انگلیس به پاناما توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/96453" target="_blank">📅 01:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96452">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انگلیس اولی رو زد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96452" target="_blank">📅 01:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96451" target="_blank">📅 01:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBtGeyeaA_k51UR5n7D8Oxw_xBvzIa42C9jEJu9SVnA_uHj20mdRbt7gbAlcEqoJkSACavuMYslxmm8JcX91e__7F-WoGnnE5-pD9TqvSF_Zw5Rsz9whfZnenyGNWCVQh8GfG8GAROzzY5V9yAq7JoRkpltk6PkooYqKOhkYAbtC5ih3Tympx6gXkjXM-gESFbrApIkSsGhXFaZobLU0LwHoe-8rqBQQrlm3SX0AIYzjHKp5q81197yzEE7c0Z3Q42SWrPhhUOwNo6s0eln80I0qGQi_TQ-_OzRf04sMfOgFbCd15aNlxJJHGmZXnPzMEi0dEHgZl-DtJXfsVTMvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxpizPtrZKQcphM7Lu9A1mCxVOwag_Ak-wrTU-exo6G5yx27kjE_xNE2KSWzEIym8Aw5hr1kEwhnQwspzjdMT_rsCE9HW1pZj8X2X_A3cFYM_0-61K7pjxnRJJkIGn7uTsBpjrQwEXYSJirVDVQjEffLDr6V8hDZ31cAapSUa9L0BoBVF4LBOCcn3J01BJB3UL7wFwSVUBJt47Tq7_usQZN2RKZqsQMSuyqhqRWl28XO3mifySCWdBmPCGlmf7HrwWdF2LUZ9BVhWWZ04jqB994oThW2ZvzaDzJ_7KoROTbEBIpYgh7_Ey9j5VmbKxWPAz4LavBZp7vvTfRSWZTm8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ترکیب رسمی پرتغال و کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96449" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بریم واسه نیمه دوم بازیها</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/96448" target="_blank">📅 01:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0G0jGfY9u14FpO7ILRTvCpfppZVriGlmZYF8UC5LRUui5jWswckpHJAw8NM18ae992U0x9DPSp4M9GRasvS8bbAuGpXHNYe1Kui89RnlvD2e_EwLkN2Xo5yzDf9Jc8w13RAeLhPoXK1oiO-SSb9P8XmJ6ZVk9XDTD3HPx1IOtR0GkLUnAHDomRfqHq0Lu56gYEeezLWUWUjCOMj8MzAo5tJPu31ogJwfH1tokEBm1QttUk5b1CFwhIlHIHzMUECsZJmrzJBqxE3LJiWwzo3tNI3z_QUuQR0WGkXshzItLImGNTZT3I2vNwyIMPia22Q9n6O7zNgBmt4pqeP_UF2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن کرواسی اینجوری گل خودشو به همسر باردارش تقدیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96447" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96446">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDp7AEW8loqIuQV85BGe3jL0g_ADOcLG8dYenT2-vssk06RwdPyK15ZAiSbQPiV7kvLlvc6TYnmE-bfpcq4EcIWTFIDepI5U1sP0mQFI9HhgRd0VTOYVqIk7ioZGNoVTIKWXYdveIraPcUn9pWpEhxblcQog9vBd1ftf6-b0-SHHsSRtl8nYohSh7m67NUWpEXtQT-nretT1OOF8WUig5v47yfVVBGW7WKh2WXf6nlOGNRSfgNveyVnVuk3scqFxxS5n4RBTvVZigAJYTc9LbkEliQvXiHVw6NA8x-fRXoODAGgzERpFGFOTLaZXf7h95BkGQQoxnrqboN-hU6WNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو وارد ورزشگاه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/96446" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47998bb9e.mp4?token=bnzbPYWHswoIyEk04V7pYQfGOpXr7e8VCEShU83sKDXYBnVKnF1NME9paLnKrVYpd_XOtFBwJ2WTQpGENeq3BZc9-tU5rNxzgBEGNPM4GJFpJK3Rrvf7vRfFXGjn6vyzClhPu1hzpsC-QZr1lXIlBJreX5QVvQ-iVId95MSNSxiDjOqS-4r0KsPGV-DY2z6kjXV2bGyPPoE29jsWKeesAOIZlGSLzQ8QiJaCkOkUGGGTaB32SRG-DUGowjBxsVnuT64MyWRRqCVnfZz2Y1qjgePwVmmgEpj14Cdo9DZmMYieLMjlktdF2JP4ZI8CDdsAL7Hl_wcvIG0wPGkT1Gc9KBIRLd5J3SSYn44RvqTU592cfphv8mJvnJLpsK9mzHYy2HzVQ2HVgaz6uWQo7bH1gzB6LXK00pKDf7-EgJFISRHzCthwM118NXoov8-xxrgwZzr8erXusue8wIcooBcrDtCpCW8o1rX4yloyFrccnUkRK3qvsmWIPY0nRocJ7RBV6u-bhaMD2fq7VBazhKbVRJgODknfuLL4rlN3hy5NJ25rUoR5ErrbHfnGxscaoNj7ZkYqk6CEpI3_c2nJB6CRDrKBZIACESbVwdMZ7GczKamCM_s3tHRsJ1LK4qk2QSDBi8HPHvqfxo1G4ynYdjesIVN1CsJMi5iEXNiRocga12s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47998bb9e.mp4?token=bnzbPYWHswoIyEk04V7pYQfGOpXr7e8VCEShU83sKDXYBnVKnF1NME9paLnKrVYpd_XOtFBwJ2WTQpGENeq3BZc9-tU5rNxzgBEGNPM4GJFpJK3Rrvf7vRfFXGjn6vyzClhPu1hzpsC-QZr1lXIlBJreX5QVvQ-iVId95MSNSxiDjOqS-4r0KsPGV-DY2z6kjXV2bGyPPoE29jsWKeesAOIZlGSLzQ8QiJaCkOkUGGGTaB32SRG-DUGowjBxsVnuT64MyWRRqCVnfZz2Y1qjgePwVmmgEpj14Cdo9DZmMYieLMjlktdF2JP4ZI8CDdsAL7Hl_wcvIG0wPGkT1Gc9KBIRLd5J3SSYn44RvqTU592cfphv8mJvnJLpsK9mzHYy2HzVQ2HVgaz6uWQo7bH1gzB6LXK00pKDf7-EgJFISRHzCthwM118NXoov8-xxrgwZzr8erXusue8wIcooBcrDtCpCW8o1rX4yloyFrccnUkRK3qvsmWIPY0nRocJ7RBV6u-bhaMD2fq7VBazhKbVRJgODknfuLL4rlN3hy5NJ25rUoR5ErrbHfnGxscaoNj7ZkYqk6CEpI3_c2nJB6CRDrKBZIACESbVwdMZ7GczKamCM_s3tHRsJ1LK4qk2QSDBi8HPHvqfxo1G4ynYdjesIVN1CsJMi5iEXNiRocga12s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام عربی جواد خیابانی به تیم ملی الجزایر برای برد اتریش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/96445" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96444" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tAl8CvACtbSoyE83bMp8PiwJOmyYxxiDzJ9k2lV88jZQMwHZhTQuJ12OBxhnH1qcxawEB_1U5Np0WEBGgQUS-ie2yyngKSeosHC7ZtMQGV1KRNGc1Ag0pmPkMmY-TfNuKkOXx8Rl5ymWRnZFrYwN-fs7foXS3Y7rn3gg5reGNnSxZRb9piE--lQo1fEFMlErjdq2BSg8xlryufsicqKbiCKBSxABINX789WKhb_fQS334SRef2ZBpgQicylwYCiisTZZvQGTg_slf4a0cbmunoTM5LPBma2dqwfl-kv7di_2b1CtE4WUJ9J0Cdf9RZOft-JFALtMBPIPlH_SU3xZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96443" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
انگلیس 0 - پاناما 0
کرواسی 1 - غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/96442" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96441">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صداوسیما در سیریک: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96441" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96440">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da8567b761.mp4?token=pbIlQb0GwspBj_iLubub3HSEnyIBraadPxVuOa9ZRpEZWA4e2GU-PU45bvtgqheLizQV7R5s2Mx4YL6arcHdP684FkygvczNCkhJDEpRx48-DqoJtVE3L3ukW4Mo1eKmX5JOtQ-AH0ZUHSTI4-JrjJDWVxT9343OJAswbVxOnTtFTOvHam3aHdC0rPj_w0Q4XxWALuJRHN08ZcCmq29-4toCDHRFeAJ2rV71Q4GkUVa2ABcylo-G8IW6LcBbKz8h8edbXqGnEkppwILWYPaCcvRFs_RtFePRmp5ZPLGikMtNxNAC9F5xWu2HxT_1br-wuHvyyMT3AX-wSCQHzpoJdBpIc6htiXor_iPJmcKDP5orBEalBWPhzgRl4u9G6NjJZjBbU7xjnm1wS1i6yv66XMulEQNKCgmBXS-6HToL_2FhQm36P4iB005798sRPSmVDSfzOoZ6PoHU_iiqpaRV5H0u6HQLTlLJyqC69fLMUCyBJLiW1l4O2v6BGQLdBD5u6VNqKn_OmcR2THrtqLymC5G4mA1k323eW1q57jitcWq3l7npFfMTrLoc4pdB1MxDi_wDKrxOGD5ppVoOkr87AXAh8ifAFpJL6MdTf-tyTxpAgZ8HHGW2q11IfD61vBqYqw68LEheh0Togkb2cFDidC1B76S2yoseoJVgFKaRQMU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da8567b761.mp4?token=pbIlQb0GwspBj_iLubub3HSEnyIBraadPxVuOa9ZRpEZWA4e2GU-PU45bvtgqheLizQV7R5s2Mx4YL6arcHdP684FkygvczNCkhJDEpRx48-DqoJtVE3L3ukW4Mo1eKmX5JOtQ-AH0ZUHSTI4-JrjJDWVxT9343OJAswbVxOnTtFTOvHam3aHdC0rPj_w0Q4XxWALuJRHN08ZcCmq29-4toCDHRFeAJ2rV71Q4GkUVa2ABcylo-G8IW6LcBbKz8h8edbXqGnEkppwILWYPaCcvRFs_RtFePRmp5ZPLGikMtNxNAC9F5xWu2HxT_1br-wuHvyyMT3AX-wSCQHzpoJdBpIc6htiXor_iPJmcKDP5orBEalBWPhzgRl4u9G6NjJZjBbU7xjnm1wS1i6yv66XMulEQNKCgmBXS-6HToL_2FhQm36P4iB005798sRPSmVDSfzOoZ6PoHU_iiqpaRV5H0u6HQLTlLJyqC69fLMUCyBJLiW1l4O2v6BGQLdBD5u6VNqKn_OmcR2THrtqLymC5G4mA1k323eW1q57jitcWq3l7npFfMTrLoc4pdB1MxDi_wDKrxOGD5ppVoOkr87AXAh8ifAFpJL6MdTf-tyTxpAgZ8HHGW2q11IfD61vBqYqw68LEheh0Togkb2cFDidC1B76S2yoseoJVgFKaRQMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کرواسی به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96440" target="_blank">📅 01:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلللللللللللل اول کرواسی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96439" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96438">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صداوسیما در سیریک: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96438" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4faa23c943.mp4?token=DfcILCvipA9BuVrypThvnKXHIWbXkCymxvd995ccxXDkUR5fc0aOX0fMzTkGL06j2MJw_SdSt5u9wphYJX_vkWe-wis7CWnBAiH93SPvvkQ5uWYS6L_qnyrqN9-zsMriOLnRvEfKAC8oW2SxLdXl0kcv3hxEo462hN6mz7KVgero23mlH2FFF8G_9lleicrLVyx2MHAwXYL7kzUpQMtMddB_ukxiW1JiGg0-yi7M4R7rBzIwE-V_7JLhB1BcL4wCwxc37sHvj4_ukX-DK7Hy6pJQToeIqoVoCwsX-04ZLnkr7mOIUPul4FgLGG568e7d7EC1-CBz3gb8Vpc5Q1C7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4faa23c943.mp4?token=DfcILCvipA9BuVrypThvnKXHIWbXkCymxvd995ccxXDkUR5fc0aOX0fMzTkGL06j2MJw_SdSt5u9wphYJX_vkWe-wis7CWnBAiH93SPvvkQ5uWYS6L_qnyrqN9-zsMriOLnRvEfKAC8oW2SxLdXl0kcv3hxEo462hN6mz7KVgero23mlH2FFF8G_9lleicrLVyx2MHAwXYL7kzUpQMtMddB_ukxiW1JiGg0-yi7M4R7rBzIwE-V_7JLhB1BcL4wCwxc37sHvj4_ukX-DK7Hy6pJQToeIqoVoCwsX-04ZLnkr7mOIUPul4FgLGG568e7d7EC1-CBz3gb8Vpc5Q1C7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کسخلم هرچی پیش‌بینی کرد برعکس شد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96437" target="_blank">📅 00:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شروع بازی های گروه L
کرواسی - غنا
انگلیس - پاناما</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96436" target="_blank">📅 00:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Y9XFfpWrVHdxVNj3hh2enP6BRe-aEozDlIXogBDU8Pg20Z_VU_zxma9RWprGUbp5rHqGjVfU_7YlKBL8DhzyvA_KxGjT-KmA0qt078XFlsc1huaGBzi7ERHiM8lZqW-A6GanQhfHRoAjzPGpef3eP9KM7tT6KjvXTQvsu6740xDMByRDJ8zVNYeYfo3dzhdoZPU1U_LAzuxQ7lSfphSa-0-FVVCxsT70VCAupggvFC3gPqUVFl6BvyKOeL1J5O7sK7kWhKYnUdpl_dVSb-HsbyBfxfSSkxnnPFjcZKvAuDPM3mgL1Ced_jwNAk7aoCGprSxW65PyNZGuEPRn91Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🇵🇹
الریاضیه: با تصمیم فدراسیون فوتبال عربستان، مذاکرات با ژرژ ژسوس پرتغالی برای هدایت این‌کشور آغاز شده و در مراحل خوبی به سر می‌برد. گفتنی‌است که عربستان سعودی میزبان جام‌ملت‌های‌آسیا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96435" target="_blank">📅 00:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e99f75d2f.mp4?token=ewyIa5NsTASwUK09IkA3ksbhaZODGGpcXgokgA3mo8kcJ3jbqFfE4QVNG6Y0ICv0nynoZkEM81l6ZXZkiSOVa6zPhF_g3GvM4Cogmes-uA7cW0V6TeGbdj7KXbQEAMlb7qi5mX5JELZTM0yyVu7jUNmyBNuTN025NKBLWD8XHvni0PwjpMrPFGEZ7HIyJ7mJPAZQt-MB6WX8mCB4IdZsLrmm0oB0KAKIHxylJzW-gRd-mx2DPOtnaEw17veE0MIP7tMcRJrQn1SZP6DqPFeJXNFebt1dGC4WHqVGmSB2wlDWy6aJ9eHW6pQGBjiNqTu09W8gnM4ryS253jLbAkUX1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e99f75d2f.mp4?token=ewyIa5NsTASwUK09IkA3ksbhaZODGGpcXgokgA3mo8kcJ3jbqFfE4QVNG6Y0ICv0nynoZkEM81l6ZXZkiSOVa6zPhF_g3GvM4Cogmes-uA7cW0V6TeGbdj7KXbQEAMlb7qi5mX5JELZTM0yyVu7jUNmyBNuTN025NKBLWD8XHvni0PwjpMrPFGEZ7HIyJ7mJPAZQt-MB6WX8mCB4IdZsLrmm0oB0KAKIHxylJzW-gRd-mx2DPOtnaEw17veE0MIP7tMcRJrQn1SZP6DqPFeJXNFebt1dGC4WHqVGmSB2wlDWy6aJ9eHW6pQGBjiNqTu09W8gnM4ryS253jLbAkUX1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🐐
صرفا در ستایش بهترین گلزن‌تاریخ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96434" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI_RiX-CTR5EwcirVfeucoz-T-KAnMsm2b5YEztqjUzSppblNgrKeVmR0I6etsmHi6PMb1zfIXwOvYcLl7lNEz6KyQRkuEPBRT4Hag1NNEgw2Rnmh3b7hUtpaJlQBW18aH_EEICsD4qUiA3dpy5XsR0oO54Nvw2QNmc-_Eqcazj2qJbxzOwAfFHSxU-hxT1dCNLMNWBxzvlNz1eYjj8LtrCXvtGmex4PlHvVHXL1IUOE7KlHUlMyBSownv3KDB2S6TjYIS4BdG6LhwlG8YiFeO-H8TEYOK1Lgp9vBSHHmCn0MAlgWBPybxoHtR92L2CLIZBN6lqa5258VlTERHCggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش لكيب
⚽️
🇨🇩
هوادار مشهور «لومومبا فيا» به دلیل عدم دریافت ویزای ورود به ایالات متحده آمریکا، قادر به حضور در بازی تیم ملی کشورش، جمهوری دموکراتیک کنگو، مقابل ازبکستان نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96433" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf1WFzqskYmlbHEdqv2HLta-aU-c1OeMi_UivfzVylQ2bUV35EyH9VLy3gMEMWYmm1xHSfw9HIbMCXlBgav_X5aHk2C_HQkAQK4LZd7cz7YJUYwU-ieEV2PSr9WkeHEf11rGkWKB-PdUNfiOq3Kmsyw8GHJdeok0S_5fNhBE78ehHVmAZJQHi42Q8F5new3vsQEfPYEiyGlsMEvv0BDiywD3FkVPeZIj5zNQ_QSuHGXBQJflX0I7Vf1JJMCTPt9Zz5KxJRHvl10Em0j4p8Ee8h-8ueeB8gFrOAViI35ZGc6RHqYLzJOLRZjSgAoqmSm81cR0J9U23q_piE7G4KPYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبن نوس: یه گروه واتساپ با ژوتا داشتم که هنوزم سرجاشه، هروقت دلم براش تنگ میشه روش ریپلای میزنم و باهاش صحبت میکنم یا هروقت اتفاق مهمی توی زندگیم بیفته میرم پی‌ویش و براش توضیح میدم، خیلی دلم براش تنگ شده، همیشه اون گروه رو نگه میدارم
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96432" target="_blank">📅 23:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3cdee6b.mp4?token=bY1H6bF3M4-FSbbD18RN9pACcZv_NaK8nY4I3uucTYkL7VGQcucG60SvJkQ9n-13xsHsOM5XrjWWJ0hYNPzzXBRd4X4GTQNDy02ZojC8sz8W8sIw5hkOmLAc3_M1W_ghIF7nv0X5OLER3m2QgkYD-7jMVuJ91o9Th22vg3mJx9UBFKAy6lWmnTD-hTj9prWWRYjOYD9zprDia3jVRZvNBXcKrwurabB91MTSCbfdpmaDEmK_kP4D62pBkfyByJwxHb2JdfCRqimO7C4geTnYSckTkT8dwpAT4fMRCp0wdFnF1Hye76dOzVydWDOKIvhrZWER0bYo-BrgpIA3FojDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3cdee6b.mp4?token=bY1H6bF3M4-FSbbD18RN9pACcZv_NaK8nY4I3uucTYkL7VGQcucG60SvJkQ9n-13xsHsOM5XrjWWJ0hYNPzzXBRd4X4GTQNDy02ZojC8sz8W8sIw5hkOmLAc3_M1W_ghIF7nv0X5OLER3m2QgkYD-7jMVuJ91o9Th22vg3mJx9UBFKAy6lWmnTD-hTj9prWWRYjOYD9zprDia3jVRZvNBXcKrwurabB91MTSCbfdpmaDEmK_kP4D62pBkfyByJwxHb2JdfCRqimO7C4geTnYSckTkT8dwpAT4fMRCp0wdFnF1Hye76dOzVydWDOKIvhrZWER0bYo-BrgpIA3FojDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شادی مردم از گل مردود شجاع خلیل‌زاده در یکی از کافه‌های تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96431" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96429">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWmMcUkIMDsfCAGs011Xq1PX0JRUQJ61XIEx665tZgnUAXak69zpQw1kx8QHZETmPldYgWVhUiqdi0IM7QvrUGcGTFhRD2egftYUdhmFzPYMfOHyO5zt7PkWD35ANGXIUdhssvBbcf9xBR0DMa7HFf_4GIJ1Osngb_36ewTLBFrao9T7fod-3Cv18d7V379YGgctmslsaR0m689xgE226yykVGyEj_-FbyqfL2RSZT3RMmon_dS4I2du7BWDqi1UhWwy-IL067WzEqaHugJG4oParmdG7NSRsdoMP7o6fzHk9BUI-sBADCqmg5TS0xxb0zV9P8sYhaxXPzLekym1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0nu1cVF7Kqd2veXnKUK938JhLb89N_yuK__onUBprFMHa-Kct1ilNqab_6GDtw1PRhoD72tX7Ue4kHZ4gZvvgMIqnBtabH1uRFRH7kuX5sdDbhABc2LELR20o2pSnkPj3KYcnznVkONZJOWWVTlI9aKuM6Rf656QnPrmm75Q6kt_t7LbNJu1xpQUfU3g0pc9XrFxxvYq-ioZR_oUB8OupzG1SWQWZCXuhHJDNLdrLF3ZWYIfl02B-qvtiY7BUYmoNjc0LHNNv4HGHMCwtil6RVeKv_cTo0Db4KHwBgEBT4YsWxanIbrAzPLJdgBsEwFq5Gfpc8Jkf0viUs3PBW6gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇭🇷
🇬🇭
ترکیب کرواسی و غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/96429" target="_blank">📅 23:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knpJ7i9Cw4vzqW7bF70nQzm7SsTrcSFQLxaa_E3JJod4xWd0_w_vh65xIu6LKmLRKYvoc8chiIrrl6SGhUKpldU32mIhQAmJQSd9iv_tWb7dMGq50KIifxurJm9tPwMZHVi5078z3gCjXoLtVwkozJPRvtcM9oyqmagGKziRSlMeK-UmJknAKPn4GoRVawv1jI2oaDUIrDlTPMpLl8m7Yhd5tnNZG8xCHWzIufgbgV9y9nQxSVZZeR-tr5p7CBshElsU8e_QmKh7c402XuxDGloeXCHZOqHgCvUDdWyhs3rKNvfvdDfzkr5GOxdFHGixCkqamjKnrqUhljU7pUBMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس مقابل پاناما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96428" target="_blank">📅 23:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0191009ab.mp4?token=llF8udgq78BWIQkTxmgXioxj2icXtLWw8IPSfPKKMAtN9jFY0q5OSOD1fUl9pJvdvi1MU_OIEJ7kLWFX7rOKJuMq7fEHKWEmiGRCCvHJN71tgsXCF1qmOmQOMxo6-ILl1tRszQAbVZOVMw4n2B9-5dUONoL2RKKKaJkMEEYhtyOYpFRD6yI99ODwFOxDu3C_faxVgQgjBoRHapvGRp52jkF1RbX1AR-dzn9G_CVUqgaBbT7yauAHgp2k5vF1X3d24OeftxOoDiMgVvSQ_BhIuYmp21hh9MiBGC9bj-IWSJuJlmgI5m4TBsNh8i60WcXeU_mpoVH5uoEy-ArLsLQn4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0191009ab.mp4?token=llF8udgq78BWIQkTxmgXioxj2icXtLWw8IPSfPKKMAtN9jFY0q5OSOD1fUl9pJvdvi1MU_OIEJ7kLWFX7rOKJuMq7fEHKWEmiGRCCvHJN71tgsXCF1qmOmQOMxo6-ILl1tRszQAbVZOVMw4n2B9-5dUONoL2RKKKaJkMEEYhtyOYpFRD6yI99ODwFOxDu3C_faxVgQgjBoRHapvGRp52jkF1RbX1AR-dzn9G_CVUqgaBbT7yauAHgp2k5vF1X3d24OeftxOoDiMgVvSQ_BhIuYmp21hh9MiBGC9bj-IWSJuJlmgI5m4TBsNh8i60WcXeU_mpoVH5uoEy-ArLsLQn4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
وضعیت صبح‌امروز مردم در مترو تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96427" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8xcwry5TqHwkqxBqAo77ZK8EA_0KeKK_ynME5iXCmbGQZaqDB6I30z-jfMeHy08Y_2dMQFq4nI1UanFy6qp0ZtGSLVb1u885AdU2XHaaoPoMfexGCxAO23eBoeRjxwiAak1qRn6f4dIpJYVt6-7QtprnnkYlBdusyKQ91NeQTGLCY_IYpf-nq_pX6xpiK9E8OeqNzqUn9ja1J-UtdTVTmUQTwXhsgY1dEYKdUd3G3jVFtxLgAMDHph5LPqAqMqNywmmihQHJxS-ETyx048dtYY1Mo5eEQHHwGBGDwbRd_2A_0fKogRnXQqSsh9Dp5Kx5yfH2IU1pYbUrO5EzfMUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فدراسیون فوتبال اروگوئه به خاطر نتایج ضعیف تیمشون پرواز اختصاصی این تیم رو کنسل کرد و بازیکنا با پرواز عادی بر میگردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96426" target="_blank">📅 23:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6750ccd1e2.mp4?token=cbKoP3oCu7RPmAhBJhagVJS7X3WvF8qAq8IgsS9H2TTSsU_s2F6WXfotUJE0ktrndqzwzi15S5PRzCk4JBoy0HQ1m0hRCGbYmNWFjXumJPf5hwfqzFPTiZrfTOKUPkmrpZy0JOirs2MaNsci-LrzsY1UlfTclQGT3bCzL2y-Rw63ZLCv_qLHzBZgsclZICCjZUTQh9hLJBGYXnCW4ljRoULAMupbhQEsW3Mq3eDUlgYWNfbaoWLdGpUnnmPnxn3TCCwL2_WERGwNCiQQoljykeImSt8yQVCUCz1E9FYQotfnhDyHDRORPME65rFLGhIzb4FETfPR_QKpxAFe_BnGNlleqC5Hav3T-ThOG9odoB_Aul_Hr_TB4jFDVs4zSL5buPNeEHInc8KMTIKymPAWBVAUlDNinIYBkFiNbYx_H7tZiktQBYpYSI9uUOJIfSMxdKQz5LoPrXOhsXcueedI90Jj2Pi-S-D8v9I-cXXBs_b93usSQSswjUwNrI7IpzRqHdjDC5i7c-qnz3XlssJ2Hs4slN6IiuLUyhDsMuY8QmZCCVmJgPCE_-foyMSrTEi6PM2_LLv5UQNuk5_up3NfQYqccK2furBhYFmrWb6tS4-M5dr_MOUDoFbNbjIkeZ7s_Xg7addZ9pNuzj8HFN-FFnCuQemlDMRlX1cEbpBBs6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6750ccd1e2.mp4?token=cbKoP3oCu7RPmAhBJhagVJS7X3WvF8qAq8IgsS9H2TTSsU_s2F6WXfotUJE0ktrndqzwzi15S5PRzCk4JBoy0HQ1m0hRCGbYmNWFjXumJPf5hwfqzFPTiZrfTOKUPkmrpZy0JOirs2MaNsci-LrzsY1UlfTclQGT3bCzL2y-Rw63ZLCv_qLHzBZgsclZICCjZUTQh9hLJBGYXnCW4ljRoULAMupbhQEsW3Mq3eDUlgYWNfbaoWLdGpUnnmPnxn3TCCwL2_WERGwNCiQQoljykeImSt8yQVCUCz1E9FYQotfnhDyHDRORPME65rFLGhIzb4FETfPR_QKpxAFe_BnGNlleqC5Hav3T-ThOG9odoB_Aul_Hr_TB4jFDVs4zSL5buPNeEHInc8KMTIKymPAWBVAUlDNinIYBkFiNbYx_H7tZiktQBYpYSI9uUOJIfSMxdKQz5LoPrXOhsXcueedI90Jj2Pi-S-D8v9I-cXXBs_b93usSQSswjUwNrI7IpzRqHdjDC5i7c-qnz3XlssJ2Hs4slN6IiuLUyhDsMuY8QmZCCVmJgPCE_-foyMSrTEi6PM2_LLv5UQNuk5_up3NfQYqccK2furBhYFmrWb6tS4-M5dr_MOUDoFbNbjIkeZ7s_Xg7addZ9pNuzj8HFN-FFnCuQemlDMRlX1cEbpBBs6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
سوال انریکه ماکایا مارکز، خبرنگار ۹۱ ساله آرژانتینی از اسکالونی: مسی بازی میکنه؟⁣
🇦🇷
اسکالونی: چون تو پرسیدی جواب میدم. فردا مقابل اردن روی نیمکته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96425" target="_blank">📅 22:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6c6b7b11.mp4?token=c1rTEZPu5Ww2l5tJlPGCnOwePVs6MtkUbxNHnXZZ1iIGO8z21kYQVHTK0qY-mCk-GqtYFGPmaDwougeu1LnZW2r9KYVMLzZ6r53wb4vFIQQH9kIMcjSiKC4tRdFSf5BSqqliuKSCQrH_yFfAbxiJtMNbrpbKxr1SA1tZl5OJGwBXlX9mP_SRxugVDu9FhBOQblKgsJf_U-OZxVv7vJMiaRXmV8f5hOqxkKQcQOZuzK-HG7oZb8hYj2HedbvA-iLxG2cRSVO6GBced0A1USKS05Xpa5wtaGQbZUmWI2WdC9euXeF3m5suJRZ94EquGJ1I1A5uRnfc6zcDW16AAt8rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6c6b7b11.mp4?token=c1rTEZPu5Ww2l5tJlPGCnOwePVs6MtkUbxNHnXZZ1iIGO8z21kYQVHTK0qY-mCk-GqtYFGPmaDwougeu1LnZW2r9KYVMLzZ6r53wb4vFIQQH9kIMcjSiKC4tRdFSf5BSqqliuKSCQrH_yFfAbxiJtMNbrpbKxr1SA1tZl5OJGwBXlX9mP_SRxugVDu9FhBOQblKgsJf_U-OZxVv7vJMiaRXmV8f5hOqxkKQcQOZuzK-HG7oZb8hYj2HedbvA-iLxG2cRSVO6GBced0A1USKS05Xpa5wtaGQbZUmWI2WdC9euXeF3m5suJRZ94EquGJ1I1A5uRnfc6zcDW16AAt8rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
واکنش قلعه‌نویی به شجاع خلیل‌زاده بعد آفساید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96424" target="_blank">📅 22:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cS4v1PSio0HUJOM71D0G3Cj5bTo2UjdZr3tSUw5Ai_B-Jx5ZJye-PT-gJYY1EOQImooB182HgMnM5Jrb605EqxgTwHOlmfB2unIE9reF3M6AFB07PraVd1WdxNVUU8Yv9dCXGK5Y-gE-NHwpsTe6fFPY1DRZxy4zU4KjIOzUnBqZXDzZn_PgkONUnCyqsUtvO3wBd1ipBhoLH6cEmK6P30cNZdTfIs7ffWyI4lp_qWNbIHDUbCu_Y_Q0WxmO7OiVc3TZ3LZ_LnVR81oGxOsnRcSj8d3gv-l88QHpo7OEXO1hDer2eE2XDqUm_ZJc66oGjestJQccxFHOPD6mpfR3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی ژاپن مقابل برزیل این کیت جذاب رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96423" target="_blank">📅 22:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔥
🔥
🔥
شادی وایکینگ‌ها کف قاره سیاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96422" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96421">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CboPl6xnPe2mGuBLzUD6jkorC_ZF7P9PHQjr8uUR99m9ZvWxKjFLLWoMQN4tRVHrF_FQbd1KugR2iqD5cclPTjZV-AoeRxgikPH0qFgJNCf6KIh8Dhk6NrpSAEHNNXgw4VrA1Qt8I9Iumi86veuhrSSVin4w9AXA8pX2IqXJqFWmoW0WrGTXTp8k8bNQy_vlCp9mwjTaAmVKtjdbT98Ml4mY73q6Qh1Razdv6XI-JqipcwpywHPRi8EIGjhzxPFiPlLj8yC39fRsFsIYD217uCDbACumiajYKXFU4vjdJWidyJZWMuhfWZJ_TLncPmR3a-L95xTHjtedL3-BzTyCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
شیوگای، بازیکن ذخیره ژاپن: «برزیل یک زمانی قدرت بزرگی بود، اما حالا چی؟ من فکر می‌کنم فقط فرانسه و آرژانتین قوی هستند. این روزها زیاد درباره برزیل نشنیده‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96421" target="_blank">📅 22:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96420">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAffURI_WOnmqag4dME2crBX9Sf7g2Kb791qWo_cqBB86M1BZChjBWLLquou9LSYt_U81TZ-Fc28FXoh2yGyjJOZtpKSsjcGNlyDDojd3tsN9xd2YL6_hamPfPTE-izYms9EXnsf79Exrf3OqwtQ3oVFm2Cnt7UVwbzxwOafSkZfkX608umG5Pli0s7RVGvAaDDXYv6qM7KWbYp_2t0UOsATRCQZdsFlsNxmzN1-V1-6VJf9ECczvpyBnOaRHUM_ZpVAqWXgh7MhNZktKofp4QoJgN9wmLzMSnS8-oxyZgqAHxYjS5aGN4tGruQRIOMmof4undS_MGnVLO307rjqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
کریستیانو رونالدو امشب این شانس را دارد که مقابل پنجاهمین تیم ملی متفاوت دوران حرفه‌ای‌اش گلزنی کند. رونالدو تا امروز هرگز مقابل کلمبیا به میدان نرفته و اگر امشب گل بزند، این تیم پنجاهمین قربانی ملی او خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96420" target="_blank">📅 21:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96419">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9ajYDFwt1JGAUKFYXcy9I41zJVCQsgnuT9gOYyawcqIFAPH1ffAafgMKSax92dxsK4SjFsoIrIuie-2sGsx77VJqMi-iCg3Q15sPqKZeePgAkLP3gTqQN8pgS50zgzv9kzc2D1p2cSrL6Ktp25I9nB0ut2fJtfGhXQVWcrukIpOFZ--fcxP2Ec9Qo3P1z1ig-h5hIsohqK4JffbOkrI3Z0gD3tHX1Eq-7-GvApr19B9VqWbElnvijQJW_y1Pm-QwZmMPHdMlntn7EvfOiYYZdrijxS-SoyF6Us275AN3hPB6q32i-TinfhGiIHY2KQQb4-R7FgbNPRYbZkZIiQ8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
جالبه بدونید ایران با 3 تا مساوی در صورت صعود به سوئیس میخوره درحالیکه اونور ژاپن با یه برد 4-0 مقابل تونس و دوتا تساوی جلو هلند و سوئد خورد به برزیل :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96419" target="_blank">📅 21:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96418">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7792e80fbd.mp4?token=fpAXRsoT1FeepkF3aP81gR8q54kf9k0wEsfuOPD6iKgIsUW6Ucl0iO5_VPXmEl54LG5q5cytJnQ4M9NzGoM71MMZYejPOEoLMM1moc0ofNg39F0rpsf-HjHx1UayWhXduT1ym4mGtuJSgnnTJH-bMPvwj0HeLFGTcM2d9mgTO8Ro4zEMlQn663e_y8Jx-HedNjoyiCwVdpmQdbGhNsEcbcVsaepVua8UFAJ5t5Xj44be984qnLMnHGu9iBeAfdpY6vVT0WA2mNLlp2zu9Tmk5Ip1xRhcwCR48lf3nPBM4WMzKy5HnknSuOw5uz4vPJe53Vy5KTcwfPAxvxdCjYa91rChC322TNTmsmHTPePBJ-7hyw2LUlMeTK3qjwNpcZkCCb-0Q6iN9pZXr38QMUbQInetYoU7DZSufZvnv_RDrrmZck7mQuieJf7Z_OVEFHIEanQ61NkOt3uqArGH9ztVW04js8sn0UuADR99fQc5TVp3R3Ln-Z_4IQQ0sJvGmtYxEPzLqzeqk8L4yjToJAGILiso4Kr6XuWTZp7yutS-VTTMK01tggA1i0EdR_rvzmnBPuq7iVPKDzJc92LQS-RwvruZWwni0SIGT94NJ8Q5FYIW7Gc0Sk6OrUm8CQ2uxheV6d9PjSH3iBfeyDtrzQTj_7jRS5qMHhKTLV_5QePR-Wc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7792e80fbd.mp4?token=fpAXRsoT1FeepkF3aP81gR8q54kf9k0wEsfuOPD6iKgIsUW6Ucl0iO5_VPXmEl54LG5q5cytJnQ4M9NzGoM71MMZYejPOEoLMM1moc0ofNg39F0rpsf-HjHx1UayWhXduT1ym4mGtuJSgnnTJH-bMPvwj0HeLFGTcM2d9mgTO8Ro4zEMlQn663e_y8Jx-HedNjoyiCwVdpmQdbGhNsEcbcVsaepVua8UFAJ5t5Xj44be984qnLMnHGu9iBeAfdpY6vVT0WA2mNLlp2zu9Tmk5Ip1xRhcwCR48lf3nPBM4WMzKy5HnknSuOw5uz4vPJe53Vy5KTcwfPAxvxdCjYa91rChC322TNTmsmHTPePBJ-7hyw2LUlMeTK3qjwNpcZkCCb-0Q6iN9pZXr38QMUbQInetYoU7DZSufZvnv_RDrrmZck7mQuieJf7Z_OVEFHIEanQ61NkOt3uqArGH9ztVW04js8sn0UuADR99fQc5TVp3R3Ln-Z_4IQQ0sJvGmtYxEPzLqzeqk8L4yjToJAGILiso4Kr6XuWTZp7yutS-VTTMK01tggA1i0EdR_rvzmnBPuq7iVPKDzJc92LQS-RwvruZWwni0SIGT94NJ8Q5FYIW7Gc0Sk6OrUm8CQ2uxheV6d9PjSH3iBfeyDtrzQTj_7jRS5qMHhKTLV_5QePR-Wc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
💥
روایت بامزه زوج ایرانی-روسی از بازی صبح امروز منتخب ایران و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/96418" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96417">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnaz5fC0BSo_bEZve7cFrDrTgqZqQf4eoyhhXWGUC8Wb9Z_KgU6mFlRZuPSiWRtlX2jcF0subMENAaiaFdH8rl9WzokRKbOsG--585LpQ2XIuOHOMwxyd-FopmVZ-tdUZ8r58kjjvCmrH-p3TqC4HpQayiLflGX70pfTr-56cJX4_-deMd9fqB17HECN132YnTJsfunGBObb1UdciBjKeylEQvlEx_is025Ag-kFebkpiRxLYXModPUWKWFs8mJkVxuYhquCyGyyJEtwXGO0_afrlPvmHwq9QASHnpN5q7D26WgwhGppFd6ZrcFCjPROXgcCEI6o3i1q6OdLFSD37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه لگانس قراره برای یک مناسبت تاریخی یه بازی دوستانه برگزار کنه
و اینم جایزه برای بهترین بازیکن زمینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96417" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96416">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c950377a2.mp4?token=c-singA9S9rDREjiBsQHqsRzLTqDA_mCFb9yR-QDLi7OhT40n9bJpqVFD0OLMa_rb-0ylNiH-7-sRzqo7mbAhPckZi5jW_RMesh4FvjpAvPgqJ1tVs6JjmyiZA9-fr9928WArFpX1SzVgkzkXmWLDdojzYVazrTmUdFXvXInZjn0ucDURS1c5uQd8XvuMcBJoWiBTo-7oqbLOR6geNHK8uKoCFFh_qPLZS6rwp5U7ofkKeWNHkeHxFfgIjg9dkLJwhXoKYojDMFR86lflB8pz9Hg70E6Q4B6vrnU9myD11f5CZOrWkHtTwZ10BcEErqYO9ocInKBcvWE_BTjNG1ZnXxL5sE3XxwVe2HuVNiwKX-ujAI3G7-p-79Vao67DukUgBzgsG3IfGHy94mN_u0lz3dGFmVFCdnS4EHJ4VbQ6bozlApBdj2YeuT7epEZalF5I4o3Lcskc7B423eeXdFTyCMu3bthjod43yX_VxcJlWi1l0eHYZSC9HX2dWcpb_eQ1zSZ2onVJWb55SA4vKa6NbGzi4A5dDM8fLM1L--DZL6NARCc57SjCpfJIDSJIULgSponvWdemTgp4SquScFU7Ub_cHYkbAY5UVZI9obsHYY6L_JEO70DhgtzewT8LsYUNxdLTCYQeNsimve3AWNuLR0QHLcyIkH8H-8eJr1SOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c950377a2.mp4?token=c-singA9S9rDREjiBsQHqsRzLTqDA_mCFb9yR-QDLi7OhT40n9bJpqVFD0OLMa_rb-0ylNiH-7-sRzqo7mbAhPckZi5jW_RMesh4FvjpAvPgqJ1tVs6JjmyiZA9-fr9928WArFpX1SzVgkzkXmWLDdojzYVazrTmUdFXvXInZjn0ucDURS1c5uQd8XvuMcBJoWiBTo-7oqbLOR6geNHK8uKoCFFh_qPLZS6rwp5U7ofkKeWNHkeHxFfgIjg9dkLJwhXoKYojDMFR86lflB8pz9Hg70E6Q4B6vrnU9myD11f5CZOrWkHtTwZ10BcEErqYO9ocInKBcvWE_BTjNG1ZnXxL5sE3XxwVe2HuVNiwKX-ujAI3G7-p-79Vao67DukUgBzgsG3IfGHy94mN_u0lz3dGFmVFCdnS4EHJ4VbQ6bozlApBdj2YeuT7epEZalF5I4o3Lcskc7B423eeXdFTyCMu3bthjod43yX_VxcJlWi1l0eHYZSC9HX2dWcpb_eQ1zSZ2onVJWb55SA4vKa6NbGzi4A5dDM8fLM1L--DZL6NARCc57SjCpfJIDSJIULgSponvWdemTgp4SquScFU7Ub_cHYkbAY5UVZI9obsHYY6L_JEO70DhgtzewT8LsYUNxdLTCYQeNsimve3AWNuLR0QHLcyIkH8H-8eJr1SOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
شادی اعضای تیم‌منتخب ایران بعد از گل مردود شجاع خلیل‌زاده از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96416" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96415">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyE4Gm4X_WC5nkfZv6P_4Gjd-cgQGDBkkupnIJVNhDwrOIVOSCJzGlNptUOS4hgOi7YjWabNteHnRwDuS3NY9577P3UK0XiqhYu1xEI4qVyGFaisDkxQKJrgtEXnyKeC3Q3SKmCxrkF82p-E_D4-fG5nkVmMIee_fj6j9wo8nAdcHDTa-UYrumnK5o5C15MwmKwBgaG8vm5JS5JBdDq75JEx2OxasAm8sEA7yiVWs13_-3gvCkUl9L-D5pZOO9KKov3uDgssG1zb8KZVCpHnNA6qSCppojS07McOwqAZBzJmxE8JisgrfxGv6EY71jfxcHcDJPpDtvMp_eFGdAQnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
این می‌تواند یک مسیر ممکن برای تیم ملی آرژانتین در جام جهانی ۲۰۲۶ باشد:
مرحله یک‌شانزدهم: کیپ ورد
🇨🇻
مرحله یک‌هشتم: استرالیا
🇦🇺
مرحله یک‌چهارم: کلمبیا
🇨🇴
نیمه نهایی: برزیل/انگلستان
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فینال: اسپانیا/فرانسه
🇫🇷
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96415" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96414">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh0H2Z6V_Uyj7DjFzYe6cXgPtVeYCK3x-uu13RqgXeD2PV4qxx05izi7XfH8SaulS6OnZMWKyNL_gNS9AZLIMjSFXiFYyKnWQr54E8CbIG_3QGvl8-puAwMF81bIW5nBUr2cglpc4L9L57UFeB7ZfSLj8UNq3jFXTOOV1c9FusGiCHwnvn8gmZnQtPB8aSuX17W8j8bXCxUtA4Ye9-eC6G76WY-ki5gEUmrTMSdZ3ij3Jb3oY34Zq9VEIa5uDC52xMpz1hB0S-gxK_Bf8lTAw4gocgfp4pZkKofhgYw3ffJx_VjgYJndpNKjBMjA5mNnjoKu2PMFDlp2chZY_sEQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇵🇦
🗓️
۷ تیر
⏰
۰۰:۳۰
انگلستان
🆚
پاناما
📌
صدرنشین در مسیر صعود یا تلاش تیم حذف‌شده برای پایان آبرومند؟
؛
جایی که یک مدعی جدی گروه برای تثبیت جایگاه خود وارد میدان می‌شود و تیمی دیگر آخرین بازی‌های خود را بدون فشار صعود برگزار می‌کند.
⚽
🔥
انگلستان، با ۴ امتیاز و قرار گرفتن در صدر جدول، حالا تنها یک پیروزی تا قطعی کردن صعود و تثبیت صدرنشینی فاصله دارد و به نظر می‌رسد با توجه به شرایط، کار دشواری در پیش نداشته باشد
در مقابل پاناما، که در قعر جدول قرار دارد و عملاً از رقابت برای صعود کنار رفته، برای حفظ اعتبار و ارائه یک نمایش متفاوت در آخرین دیدارهای خود به میدان می‌آید.
🚀
⚡️
آیا انگلستان به راحتی صدرنشین می‌شود؟
یا پاناما می‌تواند در آخرین فرصت خود غافلگیری ایجاد کند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96414" target="_blank">📅 21:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2riMlaYoLDCEVpg1ufoNPZmeAnic_7UK34HNrOIDJ4_Pk4Qzuw0Zn19bajWD_ate6c8nNEOYc-rwLyZDq5XM34Qrqc4wVxUMIbw4iltsjFxZDdKYdHkZCq1PlYTpKWjzi9zXnqrfZ6ajo9jtTygRyIy3gONmkdmEn4W0lvSj6g6QzYwEwafbnbCm_oTMjcGgCbk6KS9Od_62ZJBzptN_a0xMUi_kF2GHJrDd1_aTP_SVjMQrvbbd65y95ZvBHmmZBO_ux23iT-tuoDH_uDpLrlR6NvAPVhLF5rjfBKzlVfjHtC8P50D_pOwJWZ0B0b2KKux7r1pcAYsqTQ_GORE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inJfT33graFvOTkqouuSJi6-Gtp8T-cAhxsapFmk05WpiAnuHEmzOV7U9cWm_1_KNHiTBAPqoTBfbOYUpMp9iI2LoQQ80Qdk1lmEedktpyTIardp0GfpHq_1elgTM4LkvMqDaE3-VkMDqzyeXFkOz98XOKcfIceHHramamD-UIlNpRPD9gI7AFkHcc8g03QxYwCaB6iKUrAuh07DbYy8TNRntWXfAcZNjpmjQkgixkDNUmiZvn9i6YIA-uuBBu97dDc787vdK7NTBTSX8cbBvB87lwXnh6d8V99qby1Pbw8855uyvRahNhVQBlOXxSi-TAwp5lV0EqA6CvtAioetXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YU-QpIZQBIBJtO3iXFZ4HhSpXWvX_2SIqTdvg-mnxQjyVslHXLUBnZaecZGDQ-EbW3WITdg_3-gLX7Ko5RHf9xGHfEszKCSomzoHehWRfb-cHThmspV0CKSvXin8NqHNTStjEP9l3HyHTC-Sr9Yt0ljiPaNRtHiWG8byrbVlx39P8v3t8B2Wt1F_nhu0mM4aoOZpTI9sgPdL5q7DmEjFORRLOSRbgBT_mz0r6qYPXx4gvzc6HqGeXJW4mBx9Mfh9S4mzCCVr0yN3tq4_zOImSXnMPkkPwlXYJDOzbKjXINIKsMA0L3KAGXNAUtwkQ_6vXUYSvYLg9024NhDL-R1r9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIg_ZGBCO7Qt5keaQp72HQ0z8m7nUrkB1wKXTu2IpM6Q9xeww43199WE4WSMffIAr2YS7WzznrDj7LwRbx2tVgh80wid1PMXPNjP-sttJo3erk-XHQGN58Pyp0BJhiVuFbUuSE39nQVrnYgfSZA-CQ70J3owpEewqCeFf-Xiu4J7UMKMGsPFDOUCvm72n0jUoax3QDHYE3vQfufdv-iwlWHRkahQrSqausnsu5LhPsaAAL1svcf7QDobPRdnXjUk5w0ciZ0_Zxu_T5sUMCDcPN8oBYZmX4ELOdYzn7tmpp6fcKzMRjcUOLmgdsD6zlvgSt8nmnqwy0pxMuav0GcQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJWnmLH3wymLjIlbBlpfNy9woN4GSDE3ZiWAg4t-kf4a1g6edDahjKMPdE0K75V0Epc7tQ2tpQ_pcJhPQZ7bBkjtubqwfNK-PWG26rAORF3El4UHU2Rh5ePzAvjDd5w2sFvXO5CThcFnSglWcSjdYZBmN5MFjlO8VQN3hNpV-JI7Gmhdc4g6AenPf5c4cY5dTQFbfC-1CMPYMJLugpv2X2z6_nZVnj6NAj3T_-F_uvLPzCpflLDjlHesltKBHJcA_YZN2Q5A6UXtceyOOnP3yI400omv-Tc2AI9pYMPzxwfs4wHT-BlNakMu4Nwx4osH7P_1fkbovWqSqTBPsh3Cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2CqwSiLbTG62rj9OCieahTpuQgpHSsj9tjMJcbvpeUxAh_sS5a_btcSLEycqAjdviQ4UAmFNzwUtAQ-8YfTybUXSoRbLlq7R2IQEwtIMPKpBYpyMXaIvfw1Vke1mVxGW4hANObAc9o5fpDoH3ZpM-QtsLbyJNRnl8H4WekN-DfwnuZB86dKMjECDu-TkRmkwkRmi2KeI_N4GPpxfrWoCsPDU6N6IEYMe7uPGgAAgM3rdivtup7Q0D2oR3GE7ev0OqxTi8TyNBSpdCUSSlt9T0ou1HzTgKZydz_1iasSs0AfFhNK7jGqxv2g9iCdFtjXJGayt_1gWg7v_SMqdi_sxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLmmUQaCL6o7IJdZ7r4IX3m7SanWS5s1mBgPJcds-fIxilrPqSbGkDkmjFolsPSDhguS-MpL9pki9gotGAHti4VOiVE3dHteNYn2yP9xY7a7xGxYb0CZj6atUZCh0VCTSc2api0YaNQ8UUzR-FXcMtixMnk7nMyogruE1Xp0P47ZURmLyzSohEQGBbPNy9YhedckAAO1dgQg-0UZgDEWD5lAVtY-Is1cR-txUnhyvaAzApcN-6cmJ8yTl9qviZMLoi8u_bqZmeWI6svUDvoObzKwxhIWxst9nQjz_zDR8oeTo_rBCHe3XyvPUyZo1pRY7Ton5AOlESbt8FDBTsQcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTaughOxWbYybskY2U5qJlviyX6lVgz-Gyf-H9N2w6GtX8fJ4V_48SPqrLf1mo5RJZr9XdV_-iuZWZ0uLFnRVeq6bYaYwxc1E04-iZpeEZuK0bCkVYYbrdCTgq2cVd1l00McZ6_D7DafAqbulMS4a8tmun6O5bap6rvm2RV5pAMQs8YwNMfk0iwA_ysvFJtsGKGqE-ZiQsgiH4UXV842MOQkPrfGvLBhZlbFYccrbYMbufjq7PvzZ8AO6Qou11qcARPAzb0qjkqcRqRVEbh7B8VLd2UWee7ZbvIc48nmpxwxdjc5inwUVPgKvW6awo4LXTk3eZu6WSqcsV9k6ssacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiMZuvMiZ2sTSz6GIq5wa_IinrfPfXOHBv1-4Y4sZyT2JRbCBhKuCvXVoDIqkROJ1BHH8n6PvgEn1w4PDhuTjg_ZA9_PvU8kJq7V13dDI_NSuBBpkb1E68wWx_uAiptIcc3ggdCQlppjAz7o0y7K-gni950N_JE9NtrQ_woJ4scFpcoeVX5368Xl_SNHl6-4TwAWUtYb8ZPrdXj5WrH41eOdknwDkdAXro2AvZ5mpIo6becv6HIX4cJvRhe0quaSwwBHTzr8mXY-XAs0_q6pibgzpaq3QvpXr-oCI9xF0mdL0cGdHzy5190DaphQQQ0q5L7GQHu_qwN3SdnIv1GpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
🏆
فیفا با انتشار تصاویری نوشت: زنان ایرانی واقعا زیبا و جذاب هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96405" target="_blank">📅 21:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcg2OVd-7X46pfj4lKoKqUm-MTLtnJLgb9JRu4heVrt3DP5zmsJZFLiuNbt72de6s1kOe57EL4znLc-Td1XV2gbmy259yNAZ53YizmQT4aSb783NREHhJV2qeJ9KQBx0ts7WN8BSU_hwzHsVvBQWAFZ_usSOYhfyXrUqq4sKyNFJEI_i2c-yqA6si28tuGmpOTcNGcf3ewOHtWtxyMHWP4qZSTZ1kvZ1vSICPPOHNsvIkhDbw8s0OPbtNJ7I9_O4eNXLNn9-GgvQq9mIOrFLh_wz8fl9zsVUM1WCrxd0PeLwc3dSYf1kFbNRG4T7OxwDADwRbY5LrulqdKdipo0VAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
بازی اتریش و الجزایر هم جالبه...
الجزایر میاد نبازه چون حذفه از اون طرف الجزایر میاد که نبره چون میخوره به اسپانیا
اتریش میاد که نبازه چون حذف میشه
مساوی و برد اتریش هم مساویه با برخورد به اسپانیا...
خیلی شرایط دارکیه خلاصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/96404" target="_blank">📅 21:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c1abba44.mp4?token=sW2r_RJDMqAtNBbXicSgGm2Jjwken5Zk5Ez17mYr2p38MsksUsV1MzlxCIRXtWps69yIbYwWBmuN-XLrLAOJdTZR3U5F12qQuxLfxrf4S_sk_kXaLQu-VMHjPXNoWiceR4knWCipavp7j7IeRi5np7HIUDlEc28iza_4IZOKZcCNq9HlGqJ9GfRUXfKj6PJKrV6atcIXb8jNeRD2RAWccQnzD8m9RIKhqoy02_V6aatzfBtFz2I0k2Grf0M8SUrSP4q_jJ2S4ExsiOi2OYjycqZZzjUG-qT7FZovVBB7hqkz3qiza78WiOVUy6xGkMA1d5Awt5xzhBELpL2Ik-mWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c1abba44.mp4?token=sW2r_RJDMqAtNBbXicSgGm2Jjwken5Zk5Ez17mYr2p38MsksUsV1MzlxCIRXtWps69yIbYwWBmuN-XLrLAOJdTZR3U5F12qQuxLfxrf4S_sk_kXaLQu-VMHjPXNoWiceR4knWCipavp7j7IeRi5np7HIUDlEc28iza_4IZOKZcCNq9HlGqJ9GfRUXfKj6PJKrV6atcIXb8jNeRD2RAWccQnzD8m9RIKhqoy02_V6aatzfBtFz2I0k2Grf0M8SUrSP4q_jJ2S4ExsiOi2OYjycqZZzjUG-qT7FZovVBB7hqkz3qiza78WiOVUy6xGkMA1d5Awt5xzhBELpL2Ik-mWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
مردم مظلوم و ستم‌دیده غزه با پرچم مصر به تماشای بازی با منتخب ایران نشستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96403" target="_blank">📅 20:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX6F_2gTPOAdz-Bz13Xt_CKzWuefyzODDuClGSfF8_0iZNwr-bUzxp-3ScFsOb8JvcY1ZErv6XusbD_usFnG2eyX5a4DNmmCgxmik2zLrSq2_y5t-ev1TCuA1-62Bg9N5XDhyzFIRreh42jgX84OINbjaiParno2vTfzq4l5JWzaHTWI2u8KKFfu1KtYJqxxLp43VpmhNIx3wmrzMuH6Gj6VmljEMVgCq92wVYoF4o1-sxNHveXCy6EX8QL5pM3mD58ZCi5stTghpAf0BaE3NkizfvsWPP_Z_15bdHUdVslbPno0FPl0jAi8rTj-ZnWBvhWn94MlI7peGOzg5RhOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
🇯🇵
ماریانی‌ایتالیایی داور بازی برزیل و ژاپن در مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96402" target="_blank">📅 20:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCz22QS5NR-eoBGxCNxdf8qAhGzIsVDFjqvKYUHckDi5cy70kdfhFOdvItVsjXXggxe2jItBvmVplGR5ccZY52qA50ihJfqeQsGIDftaG7bAL7WBg3AMUDbTSHOmiLt_FpWxcWsdsHZLcFZ8em6UwmF65qreN0CHhTt50ru5Qan_7I9RiAxOf1YZuzxLWNrZuWPiGnsUbXBK-pl4GGk3hJKWqQ1A5RVE-i1ztPgjd7h6HjJy9RychkbaRQ1bS9cMiEbN4fNFE6jdRpuAJ8mRJGXwCdX-yFm9m7UMezZRCL64nA0y6W8te8LjqAuTGXsAXQFYsUc9mlWwKAalw7mROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پشمامممممم
یه زن و شوهر تو قرچک که شش ماه پیش ازدواج کردن سر طرفداری از تیم فوتبال ایران از هم جدا شدن
‼️
🔺
زن طرفدار تیم فوتبال ایران بوده و به دلیل اینکه شوهرش همیشه موقع پخش بازیا آرزوی باخت تیم ملی رو داشته با هم درگیر میشن و آخرشم از هم دیگه طلاق میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96401" target="_blank">📅 20:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0tlvPVA861jOYsB_swqXZIrmnT5k0Z210QYHi7b4zi85ANWjHMjG4SjBlZ1guSQRi9u9cewQDwxyMpCZ8d-h_UP34HjVyo3frqfroa5w_gMFkv4qUlG_wyyMPz7DABROUX1o1YQhwIQEKd3m3PKmcKc-q-yOoJ515IYoeIqMePJS-ayWQmeF_x2NS_xNYE8EF7xzIoLulkenjXJ7x5gCA-QP10M-Kbmb0EF3x7EVdkZ9D4Rq2se2jDr-0oka_01FrfV48JVkvJzH3-tAtT2W8u7wQKyvCd5fjMnilIJYNcJ9yVHlx6lfv43u-yaPegDDwlTh1at6JsCczZrbl3ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇯🇵
شیوکای‌بازیکن تیم‌ملی ژاپن
: درباره تقابل با برزیل باید بگویم که در دهه اخیر تیم مطرحی نبودند و دلیلی برای ترس از آنها وجود دارد. بنظرم فرانسه و آرژانتین بهترین هستند و ما از سایر تیم‌های دنیا چیزی کم نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/96400" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op5HmfZ8f83g5jyqfT_5xcXE9KjlM_3lVs6TI2iayFRD8VjtncaHCdsvfurW6e3hNZbOlikO1-_tfC7XOmTI0ayBE3vAtutNGrJqBHSx4ZS2NT3AUKJvr0rIAAo1YFjEDhRlU9OB4LUVF3PnNQ6ffReTuXsN_T0QeFM6Sb1yx7O7ftNRhqsHa_fVefEnzsVWThweiy5A40bGsWwQg-4GnmhPrKgq0KyAaY6LrcoENRqwFNVDi3zc2XZ6nKZtFa-RqpMM8NtNqmEs_b6J0hKBrr89jLzt8NyTiRv8WysgnedwbkeWYMPk3WRvAPS2lnJOOxdaWALlVep58Lc2KecuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده مورینیو
حقیقت رو بگو سیمئونه
اعتراف کن آرتتا
آیا او بهترین حرامبال نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96399" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzOWATdG8r7ADjA-uEYzeQnwbOLxTdGk-ApMi2G-doaG9KN3VpqPl4AvmP5Du_eOGAv9XEkolvvFUPjAzGnhxUjPP113pbUfkBm5tHU6bvWrvbq470NBbUiLRrYrcxVes1t4UiliQhYEKUMf29bra5tx3-clO9EZ6fShV0EFG2FuB8GuUPokYxfeBQabjEKoyoGlGFPGHn5uXVNIkovMeNv7ysdeZcpTJ2hum-QafICpUS0qz0zDj4ZMuaJX3i6VAPV9GEOQpObiIGGA7bfpfnJ08LVI4iSkMm5Nsd1al10SmyL8Di2ChgAXai_qlvvCKO3zzORrSjY6FX0iCVh_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xbsu-5QiXdcySaGn1CZa86YODlhAkCWgBgJmWsflBNxl9SkULo_VG-IBTkQ1IoswEr0lxwzBaTpgIcQpACt9sU-Fsr87wF1je3F8k-iLBn8hBOx3qjrbrto_p-M1E7A6TsoBlLYt6NBA-f5cE2QT16lw7nA0XnG70_cPePzFds2j7rxrmHEGhRRnEZVqoD6vdPyuOjGb1RMpZilOV9mJ3yHFvJqxFT-6T-RenhKrxmfsgIZfUtsulwtNPH1hO7urys8M1E6QiizRDuUMWlFB0KcYoCszpcmCjRPhTIccLD0Z1h6E2DyUOsYaf18p0cfX9Ql0ZEOy4lHiAhNLLt9mKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hW5GejL_B2AKF2e5y91z6z3BsyYx6Wu0YXDqcU2HusTMbmb4ulJ1ibYho2q8glKZN-mPH8awqryK_ruX0-7rdETfMP5T76HpWjE4pxDGMZ9X-SxSCdS9_YvlMxov7hd9nl8eUUk6O5gLmht0KMGcn8S0vy4UKtu6sxKyrl86Nw2ytwXrsCDR4Xl2ZrmcE2D3Q0v3oBgiRPnwVpkW7xAsG_vPpIfm6CVqiCuPrL6NNQ1gyoKEVjsv8nZNSmylniYgOLQJvaqw5Fv34oOyl1FodozHI-2edKcKKtAPOJvoso5PYrRe7rewKZfhNrUFd28Dx4U91NAy_oEjkNAGPlDRjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🇨🇴
کلمبیا سابقه بدی در بازی جوانمردانه مقابل برخی از بزرگ‌ترین ستاره‌های این نسل دارد:
🚑
🇧🇷
نیمار در مقابل کلمبیا در جام جهانی ۲۰۱۴ دچار مصدومیت شد.
🚑
🤩
لیونل مسی در مقابل کلمبیا در کوپا آمریکا ۲۰۲۴ مصدوم شد.
🇵🇹
- امشب... قرار ملاقات با کریستیانو رونالدو
⌛️
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96396" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNKpXoLrYd9Zd6QIISaIy64cVtopTM5ekH2VWXuVM7zpTFh558jjZUrfff7OztemXzCQAtjuYbUXdPkzph0nbX7HwcBKsclh56-uzKNav5aGEFv1cUnnv5BIVyfNlxj8DOj20QACXftjw7DHF-2a-yUKgOArN60ulnBcNTLo3qVAAFIy29-9k65vU6WJj4hNpQXPG9Xbu5rq2TVhheu1kDn1P88LWwCD3PkfvKAtDXArzEiOq8a-lLI4JKltocUKC1SFNfflMmo0Pkcea_Pa2s1xjhq46wO2DcdW_byx2VpAB3gkC6NwPNGfQnPaCVzW2cHQ1WXLpNorgKdhW6Y_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووری
؛ فلوریان پلتنبرگ: چلسی با ساندرلند برای جذب گرانیت‌ژاکا‌به توافق رسید. ارزش این انتقال حدود ۳۰ میلیون یورو خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96395" target="_blank">📅 20:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=avsIkaIV2dOZ1RKRtlRPcaV8xbe5-dWwkDivox9tskRdIs667lrx4e6ouKyNB40EXRgrYCVPjjxH8kSAu3EApMnIGBBCEz7uGlu3UwyUjXDjJ1C8R3EytXa_hi64dbDVnq4zgEr-IUwVAT0H-thPOeCIOFxrjmaD46MZg-l3Cdjdl6migtjP7PMNoU8QxcKSXKstgOEpf2qihq_EBAz_pnk3rK-44tMFzOzwJkE_rl9hbJmJGb9tNnvqc38B9s0XvefoajqhO-I_NOL6cOhulEUAzP3YU3tN0rwqZwRKIwrRR8J0d_uEQNS7avbuIFrFE2vVY-Zc68AOhJk321dCOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=avsIkaIV2dOZ1RKRtlRPcaV8xbe5-dWwkDivox9tskRdIs667lrx4e6ouKyNB40EXRgrYCVPjjxH8kSAu3EApMnIGBBCEz7uGlu3UwyUjXDjJ1C8R3EytXa_hi64dbDVnq4zgEr-IUwVAT0H-thPOeCIOFxrjmaD46MZg-l3Cdjdl6migtjP7PMNoU8QxcKSXKstgOEpf2qihq_EBAz_pnk3rK-44tMFzOzwJkE_rl9hbJmJGb9tNnvqc38B9s0XvefoajqhO-I_NOL6cOhulEUAzP3YU3tN0rwqZwRKIwrRR8J0d_uEQNS7avbuIFrFE2vVY-Zc68AOhJk321dCOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فحاشی‌ هواداران داخل ورزشگاه به کنعانی‌زادگان موقع گرم‌کردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96394" target="_blank">📅 20:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhrOi4LqYkiK_oZrhs1_i9hmIGjB_y71umKq3JBmaIjiV_B_z7AJWcYgRDphIKD81se9Lngo8BJjD-YpMyfvYRQmByMZmKNxy1F4ZGrxst6TEBeW2gxcGZ8bMRn6X8v39-O1flbAua3hdahQ1oAJZAzXVxkqo2G39xc9FPecKsg-cgzjbB9RNaFZOfugiQoCQy7A6TC31AVfV-A-DYebX0-HJc8bFQVTmLFWuP35CvV7VQb0qHyJTMCTkDZLzyTJ-d_7rQDTONPMfwmxMqCq5pfZKtoRECkehLx5fjS0XelftZz_vwM5kOV-Biyk1NjYchUi2DLAUJP4jGXvhdqO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
نوزاد کودی گاکپو ستاره تیم‌ملی هلند و لیورپول امروز بدلیل بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/96393" target="_blank">📅 19:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=NeFINQhPvLHCvMRp4CUgVP3K5edcgkP6hI-_zcxzs_PQnplXJOYvO9xerArR7VSMfCa9vg2Iqrqnh-szRwg4ixJFl6mzFlvoA45K1gg0pM9APt2X-doEHENKJdZd-fQ3I7wFOtT-yWU1zgY_wS4JqUbTLYbOdiyf8FnqM8mTT8LYcFZNXFL1SZqKQnGX6U5N9Upf9IxTyUtJik9LUVSKjS4jy-4ZXccgm-fb2gI9TNPPKrakJLh8oL6LZ2CSKNia3y0lEh59qkajKvL7t7tVXiSYrXJRPDpgSWd2vjpRyIajAlj21q968TABFtnJQuOKktz-eHI802KM89qm1Fn8_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=NeFINQhPvLHCvMRp4CUgVP3K5edcgkP6hI-_zcxzs_PQnplXJOYvO9xerArR7VSMfCa9vg2Iqrqnh-szRwg4ixJFl6mzFlvoA45K1gg0pM9APt2X-doEHENKJdZd-fQ3I7wFOtT-yWU1zgY_wS4JqUbTLYbOdiyf8FnqM8mTT8LYcFZNXFL1SZqKQnGX6U5N9Upf9IxTyUtJik9LUVSKjS4jy-4ZXccgm-fb2gI9TNPPKrakJLh8oL6LZ2CSKNia3y0lEh59qkajKvL7t7tVXiSYrXJRPDpgSWd2vjpRyIajAlj21q968TABFtnJQuOKktz-eHI802KM89qm1Fn8_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
انتقاد تند شریفی‌مقدم مجری صداوسیما از امیر قلعه‌نویی سرمربی تیم‌منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96392" target="_blank">📅 19:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Clvc2jety22C5s9FtA6oyKlnB8oNXTbzlMTeOYIZv_QtcH1mIiNtCUG2lEiRiWyKZTIUahbWKew4aQr2UWszf2tC9osCZgYn7z_ufqmc-rSVFnnqmJM8WYOenrDGwdC54-Cnx0N6bpP-mHoP4JIBluNH5mq0Nok2ooIkohFIJUnYxh5lSjWZDKizGC5DOd3l_X3zXazQW2dHhhr1gUSpoXrzizstocPGbCRhhZBbL6CA_OpopOlhBHSNbnaG8TQDrujkblQDwQ301nsGRS-MDF3xQCqcILesIYicDWJG8TiYMTBVodH3L-feq8FtxwMCquyX1RAeULzCV7NEy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عثمان دمبله در ۱۹ بازی اولش برای فرانسه در تورنمنت‌های بین‌المللی نتونست گلزنی کنه.
🔺
این درحالیه که دمبله در جام جهانی ۲۰۲۶ در تنها ۳ بازی، ۴ گل به ثمر رسونده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96391" target="_blank">📅 19:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=AuF5LLJqna06AkxvOK6143F86y5ccSUb5gk2Ar5V9TLvmZ4G-NOrg62rkSQpfd1EMLVw7YudeDUa78c_oPxHamE_26S9-YQiBGRCfoqQ_Df7mAtEFApFCQyjoxugT0FZ1fZeZQv1_QCQO7kwya5sMph_uC0encoqs1p711ZiRDYju8YjFCVH76luHURKVaNb8iqBWu0jYwKLGf_d8sHVj8n7FhopsAn20GQTEZmQv9dMcj2Bu4XCRMzQ9jhxGMdSh5ROgH4M_v6pocUJqd6ybKbhPf89-dXNhemxqsC9AQhTl9YigPBG6fr8F9F-PCt47OHa2CjtFK7JpDaQ1YWJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=AuF5LLJqna06AkxvOK6143F86y5ccSUb5gk2Ar5V9TLvmZ4G-NOrg62rkSQpfd1EMLVw7YudeDUa78c_oPxHamE_26S9-YQiBGRCfoqQ_Df7mAtEFApFCQyjoxugT0FZ1fZeZQv1_QCQO7kwya5sMph_uC0encoqs1p711ZiRDYju8YjFCVH76luHURKVaNb8iqBWu0jYwKLGf_d8sHVj8n7FhopsAn20GQTEZmQv9dMcj2Bu4XCRMzQ9jhxGMdSh5ROgH4M_v6pocUJqd6ybKbhPf89-dXNhemxqsC9AQhTl9YigPBG6fr8F9F-PCt47OHa2CjtFK7JpDaQ1YWJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی مصر از لحظه گل شجاع خلیل زاده تا آفساید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96390" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96389" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYEUolvJdejmDUIMpx3FK0vt13rTAFdz2qElY3LtPVtfDpTfAyi7W7vzcZA55rYHlShGUOJXvhpHADI2r2OcH2Gmqt4QuKynooSNV_JHBwdMHarqz7AF5gzN9Z6hz5uHLwuBryN9NCSq1grKDSvlr8IKfW0mGQNVPsWguZNa3LTBuvd_oZnPMDXVok1DcqWsnip2lpVT6kURBAU7msc82XApnBzt-PtXR4Dhf9Kv-1aPVMcpPZNLFDucMBy1mRkCjUrcKZkW3eXQ-U7Jg4DpBJaaHJLxdgWxA5k8RlKPSSBfPaFaSL1FFOEg05K1qEYv4auLgjkZK5kG9G7iUGYCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96388" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=RXp5p6xibJ8isXd_4JXNJV5pZOtJI8iV5KoZxzkOs5BYLOY9dNpWsePt2TIe0S-J8dfkVwcSwmK2j2G0wU7cjU2PSXqSW3Ms97D3AdHHwn-MKYn15P0gJR8EpRceJdz6uL2KU-mBxV5ATlY1fixqBLTXzn-xGUVLwJ2vVlYBXNneZ_wdMxZbmFWnRTm7l2mj7kpU_FoQ7OgkGF3yJb0LUusDlmxcd7p92eavG8RI3x4GakbF1d82DCEQGPxCA0cE-HEZ9ybTODODdinvk2Tt71cT5Mf_9_m1rtzO0BqIDsGk1F_7zOyQmAU1TT4aq_zsUKiG3r--DpHJn5h-kR8mxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=RXp5p6xibJ8isXd_4JXNJV5pZOtJI8iV5KoZxzkOs5BYLOY9dNpWsePt2TIe0S-J8dfkVwcSwmK2j2G0wU7cjU2PSXqSW3Ms97D3AdHHwn-MKYn15P0gJR8EpRceJdz6uL2KU-mBxV5ATlY1fixqBLTXzn-xGUVLwJ2vVlYBXNneZ_wdMxZbmFWnRTm7l2mj7kpU_FoQ7OgkGF3yJb0LUusDlmxcd7p92eavG8RI3x4GakbF1d82DCEQGPxCA0cE-HEZ9ybTODODdinvk2Tt71cT5Mf_9_m1rtzO0BqIDsGk1F_7zOyQmAU1TT4aq_zsUKiG3r--DpHJn5h-kR8mxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی میگذره کلیپای بیشتری رو میشه؛ وسط خوشحالی بعد گل شجاع خلیل‌زاده اون وسط یه دماغم باخت دادن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96387" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96386">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=oUmes6i5dVw34WeA5wc6TyC_BLObBVhq_rDyUv7LnDLizRFt2paaRjtt6SDme0Gp6tVvf0mj00dsZCEcQ3BhK-vuvmshAqVw_25NbQzH-4gDlSUEIPA-MHM2hEbFwGSXMm70Mpeh1xMxb7fENhq6EKDrqkqRDxqdKoLsAY0g83uPrBhcVBHitSqM8XNQj8eWwECzhM7pWdTIZ52GSIW1dkMy4ISG-BLH5UPgIJ9436-5ol7AmJdo9KEj1UndQB4tucpzwGvsW8_4IIj1Mo_5tVc2F3Dml-ggfIYIT629hWqlKbkmeQvOOuVYfcBqRLVck0LBkibkD2Lzdm9Ytm1-Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=oUmes6i5dVw34WeA5wc6TyC_BLObBVhq_rDyUv7LnDLizRFt2paaRjtt6SDme0Gp6tVvf0mj00dsZCEcQ3BhK-vuvmshAqVw_25NbQzH-4gDlSUEIPA-MHM2hEbFwGSXMm70Mpeh1xMxb7fENhq6EKDrqkqRDxqdKoLsAY0g83uPrBhcVBHitSqM8XNQj8eWwECzhM7pWdTIZ52GSIW1dkMy4ISG-BLH5UPgIJ9436-5ol7AmJdo9KEj1UndQB4tucpzwGvsW8_4IIj1Mo_5tVc2F3Dml-ggfIYIT629hWqlKbkmeQvOOuVYfcBqRLVck0LBkibkD2Lzdm9Ytm1-Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
جلالی: سر حرفم هستم و قلعه‌نویی از مورینیو بهتره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96386" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYvzuqq8bM8GU_XYmD42IMkdRhbA7-zyzRMlwMQba3N00nLxEP5NgRisQ5VBQMYNBh_kmKSEJ_zp9xveZN6nKDiFwRxroKAbDnKAOL8iCsC2uPU3u--g6yBwMlO_8W1OPuum_YJ_JSe9NEIF-ToIXnixMgjruqZZHCEtfG-S9gJ6ULxwlwGbZsCZdv4pSrSTlVhKM6GU7WY2CX2xRbmaRr0k06N90px1-9_X_g6YJ4fIbtwnOziemA3MYwuxedT8iZDm44cUR3Q4CCJTXtZAUxPD_hm0TYD-Chl5c5cpVT9XOdHViu8GMaESEnhou3y1cCAWCLgGLS7UxPtzvWGyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مربی های با بیشترین برد در تاریخ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96385" target="_blank">📅 18:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjG1OnmJRdA6bqsD8XPY6MbdZGse4hHEywOrKEJ1PAPQ6icCOnTX2vgKl3Bq-ab1KvzYVkWruIIqjQXzTHqVnazNEszK80HpKLZP0WO2Qkh6p37AkcSx-Pm_qUbA9qdAWNftuPISYepxWkqe1q4ByZNhY1HbyYh10cJT3-Kq97BplRsXcWPjDxImySos4_SeD2j4UYRBc5iL1yok6bjUzTBkEi4IcNVb0675hiLy4dwjHtzQ4A4lGEaq9Z2Wz6iGNmvjQTShR3xM7fXObQz5V7FQa3KTpwLu_DXL4E0No-Ew4kBZcc62pjmvOVTq4vBQ4vKllnGnJLIE1MtnR_tTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کفش‌طلایی کریس‌رونالدو در تمرینات پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96384" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-tGpB5fW6wJToUwQMBWMl9qXrLGmXht9HdGW1GDBjd0JJsKvjW1iRAuKavwv5LapLaXgNKai3uoGUwv69FC9X5u-6Vvnt24QYNPXQDzEDHRbo0vNUzySVaU6kL9KV7yuXIqTLOUGFaDOopbaY-aejI8laRD4cr2GvanYddTTKVmkftjc4UCHAbuHauo-PebSxf_UlDpNZU_cIDJwopAfx0XGunAzl-bbKVokGZEeFPXJ4NwAdek5QvBo5WOll7o8C5f8-zPIvgM6f8M_JhEB1cQCSLVR4_GXa8B3gsRwtLWLgVzi1LEGkMUToRrcCt3KST3vfFmTfhiNi3DO8Hqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده مسی از سال 2022 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/96383" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q02Fbs9gEfWjMDr2gko_P3bfgj8sgRwrZU_xe14XoCEL6eGYwF-KClSka-qFguKh3s8kgvPFFJmYY7AOBFZk3tkqExtVbaimtLfrXzKvCEghhg-H8ru331QJvSo1m0Y4PRcMN_70bGl31off7RqoOGasw5-ToyYpRRZ-mVBhKiYD_4K9pHcpOEkwRi-NVuVAFIH1CUekxOd8ihWpX13z7sSZ4zY6CVSsg22LJrxBw73R-wujYpe4N5Pw7-CncZgKyvQsp2FJ5xvj7anAmjEgHRymfqC3uRZ0gkIaQtdrc_0Lh1ubPe4NKipDQwj_OTiH0XPAvTgWA5MXECgMdVhW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودری تاکنون 328 پاس دقیق در جام جهانی ثبت کرده است که 109 پاس بیشتر از هر هافبک دیگر در مسابقات است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96382" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trgekH3K1ir_kZH9PcrNXebbX5SI_59xvbWVYdCrwURCszgSywn1CgRXtEC3bGKq-FZa_1Fpydxunt6XcU8K6P7-TYMQ_X0SsUuy7dd4jeMaImvWZjfF2P1ZAw7rxw9keRRgsSsi2gWbyXp-csdU5KDshP7qGWcQDV78TB8cMIo42cxuOK4TAQNh4cCF9kXCnjLiRhngm7WZHOgZqOOBkBEKqVcgZoCwVkhOTqfITHt578JL-j2_HYWUzS8Qu744pV1amjKGoSHCl9r_PfDLFYLY9rDxDtURtsSoGf2QG0YrNnoLMwLGYrfiBGkOS1y1KAnjj7C8z_gN1SXKdxq_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسامی برندگان جشنواره ۹۳×۹۳ بانک کشاورزی تا این لحظه
⬇️
⬇️
⬇️
https://www.bki.ir/fifa2026lottery
‌
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
‌
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/96381" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96380">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1zdoFnKVn6sC4Jyt0u0ytUcf5znRyVaT26wpv8SNlEvxauFmvML_i3xAoO6LRT5kzOuV39Hml2SxOUGl5Cx3KK7u1pDxjlYRxgDisjISA1uhSyHQnQHbNnFTZFiOQ6CnmAwJ-wHyn6a1RUAhruqCSi03NY7hvyQ7rFAVc342oMWg71Y1_HWpW03zCMVSK_Zv0iKTFFOPhxUZsNdqkuagnJPpl_8fP5x9ZSfHWf1FUTVznzs9X_WbeBm27ImGq4w3NSXe6Gzvy8VPkl0bcj5PqKRqX8Z7nW6uWn9kR_eysdMpTi6p2NkYczWZU9qqvJ6vCxqzvU-U9_rxw6jJFU2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پرز بگید حرکت نکنه که اوضاع خیطه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96380" target="_blank">📅 17:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96379">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1hNvRCW5KXxSqYAamzkSK9F6CPFFrnu_S0urGL9xISXmlSXMcoYP6uiVtEt-onqdKM6apJHCv_XiA8G7ZyMmZD3IY5KhlGZcSjUiKh7TAMIGmXETWs4t9pbG6qEHPabQrZqygxMSV-y9mDnZ_X0Oloo-VvhKyWrwK7KzgPl8wszLag55wPALjMA8-DFs-ixZ2MxSGVoQECulj-u6mpx-ZFadmr4S0niAGj7ruDHdW5_8BJcGCi71Bk3t6fpdmc_LIPS32nrPRXcDPWUMJrLFdoLp6RqSMMmpvFwlpG4zq1gLjjYOzm0iJ3hKxEf0yRueK_qP0pnsDDQCSx3GAgaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبرومون رفت و شجاع خلیل‌زاده تبدیل به ترندترین میم حال حاضر جام جهانی شد.🫪
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/96379" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tINOzXAoAZV_IsI9qQoemWvl2ltwUsLg9W8SAZYbP1xA1wvWEC9lL0WE-H20zOoGqZ8VVzqm1pt90uw_Yf-5sAqHGeVoJ7qawYvQoyTLjJsMeiadAoHdpigM4gOC-J6miUoiZA1q29VNEMNXfqkZfB00Aw9QoX3Qn8BKcsBh7hiJYWBcGvNAD41i26dUi9dhHNuZR4Ex4m-lt-Jn6xA4ru5ZKOv0FBEiKW0pG0OV-K-3DVZrBNQ0WvO_01c4PGKdWFZaiBDJnm2IovbUBwycN99KfDVNVIXT00Wf8SWc6mZMhl8uV6R-1gIbPGEOQQfsO35MFpNmVQyPkKgLAycM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2JAmDCdWT-imG6qw8jYjPguqxS8VzMj0Tby2IsfZgpLbA4VjTx5zlW4JlTweyQAMrE_rEbCo7eK-wWcExSjOxPfW3XgI6T3DlINu57wuiKBnguiPcjlePfeK6divOuFZ5hSyuD_VnX8jKVfnZfCwEnXyg0CCTPs8s_VG2v3_wE1hTypLWAguLUEBUvIkv5CPiwTB_6pK-dl-ogKG6Z7lbA8aRwEtXDgK7otS10hWDQX1OQNaGxdj9KYXwkMUEwi58QFYwiyT4mdiRSwbJQeyqV7Iqa3F_eiKw-jb6GJftAr2HexlsnP4W6JgdVbt1CbEkE_46t4LNJnl1s61iTKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ubbt_aY1UD-oN3f-_ZzGYQ2HtUflSBilO7rpKjb9GASkFj1Ki5PvZUpIyCePyFdMHuG7mqbecRmZBUxCbar_tGYkC4zE3ZXwGWd0CSdnqJYmoj0zzdgpUTTweQLwWQfVEC-p4gY9Ma_lXFGJGuG8cPUAiooW7TOx7c33435jxcK44Z4LWs1Eol4cpcauhKBWG_g7E2x5Xe0qXG9KZGgtbQZsWTAypltM_Nn0wctqmR3St74J2lP8x63RPEUB0BkpU25wxjUmyF7a-flysbsoxVelM-o1fiES2y4FLlj-bO4YiOQB5e8qT8rTieDs8-QQULF1Lzy0l47nZ4ehJcmP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUocoP_emqD6gZrSVDppBAjZQieJvGtyUmGZw7E3OGVx50bc-MRpCECrqlkLe3bsdFiF6bHi3doDxIs2TPGvXG_XD-eL9SdjpNFlK-GNd_nu-g0HrubJybcuFdX3tx0_MOizt7GTUPLNsOjW7fnKli1kTH2AgGlMvr78HC565HYkY-CAVRVHeydXbgK6155ZE5gjAWgbwlhUFmvDS9xLPen6JJ46p1QGrnFIGCQy8K0MOCYw0MQEC0q1iMak1bfEZDNhlcr99hPI7CIH3a1cExKw_vY7UcytIDOdIMDuNu2O0vGmIkjbG7B6Yavtc-nlXqOmeo5DkqWvVrF6Lvj3gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حیف شد عربستان دیشب حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/96375" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96374">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96374" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
