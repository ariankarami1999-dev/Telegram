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
<img src="https://cdn5.telesco.pe/file/ivbu0n7Mv2Z2_IZAh8tCO5vklJlEE4Qea1X0sbNWNonKbrj9isiFTxI0r9wWiERXpllwaKh2VQEWLorklr4ueynXoJTRFpNTLSE200IjryBWCz6I2F6MBuQtj_8_ITaG8t0RPPWAg8gPr-1aWJkKwv4lxIPyI592-WC4Jm5dkWwtNNMW3ec_eE0NGZFw4ZcozN2NnSFu7QUHEXCDX1KE88EvdhU48K4RyUMv46QUjOQ1MOGl-5bJJKnegqEI8qTnhvzdoIrPYUcTxcsfg990i0Fqcb3V5CzFzMr4QSDaJTtIdBlCBbrHibV9AjbIWpbUOp7fjjilvmgMRS6haJG7NQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 388K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-108128">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic85fY3yffouKx68HrDHmgayBCI8o3LRZSUamOzxkaHyZAqz78Bi9nfoUcnV-Nuj_HYuoerKdjU3blUZ5JP9qB15j-K9_esKZfV7TyC00ovOm9JBEegsEo4GXlN2-VyRak4ZwFd35GrqBmcPR0g3CbaxRC6JzsQ8xrKL0rywVlNTi2_tqkzkY30JaeQicRTfmw35WBe0dcVCLEed7m8eh4J6Yao8FSJirIGOH2okcGeN-H9hqLawpbnGFk98bVmeIc_daX2GYoBipcQ4vgdf0lHUlrqADsfcVI2-JOVbeDfSK3beZlkVAYvjPXSac9TgDRPh7zZvLXRGpcDibDdzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/108128" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36afca847.mp4?token=lpOIEGwPE4EJFp5U5eWozXTRN67bta_U14z7juJh0W-TdVhk48Ez1zl7UqePCMhsZeQimrNxm9iHVViKndKLQOTsaqY2Qi9rviRoFJtXWX_2gu0OAABto4LT9SA4eSCbBhhHvmrDKyUjnhU_zwBDCzbX5R8NBY_WAlFdNPfbQmPWaC94wPtI5OCkrSkmZfJiBYxlDkP_NVx70HykgMHmbPD1P15JPOYDdI-Ff4QqF2lTUYgebgk0EEqZsv1BnGJFxfc04K9Dwy6trtK6-TwQA8oAh_aisIX9eJLG4mc-tyhvp_WlwIySld4oM_fhUO8W5nLQWpsuhJknOnQGbMg9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36afca847.mp4?token=lpOIEGwPE4EJFp5U5eWozXTRN67bta_U14z7juJh0W-TdVhk48Ez1zl7UqePCMhsZeQimrNxm9iHVViKndKLQOTsaqY2Qi9rviRoFJtXWX_2gu0OAABto4LT9SA4eSCbBhhHvmrDKyUjnhU_zwBDCzbX5R8NBY_WAlFdNPfbQmPWaC94wPtI5OCkrSkmZfJiBYxlDkP_NVx70HykgMHmbPD1P15JPOYDdI-Ff4QqF2lTUYgebgk0EEqZsv1BnGJFxfc04K9Dwy6trtK6-TwQA8oAh_aisIX9eJLG4mc-tyhvp_WlwIySld4oM_fhUO8W5nLQWpsuhJknOnQGbMg9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل چهارم سپاهان به فجرسپاسی
آریا یوسفی در دقیقه 54 دبل کرد و گل چهارم سپاهان را به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/108127" target="_blank">📅 20:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108126">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=P2ALipjIwGSSRNEJpDedwnMGGftER1JqXcs0swhkSKzWBIhVIS9RnXUP9wqrIZz6CWW8qg4OLKYrojSEFpSUKz_y-GOXQyyVViRQrUzt6qYN9tOH7KTDfn_qo_IPB7iTZ9qykFrVBxGwxrv9ZYvoXa9YZdC-k74MTPseSGayCrOvCnBWHh5ezj3gzTx9D8vuapIU-X3z9tjiDSu9PEe-ZDk9u8pGaO4zIg4ibgmILtsidGQVMQ2j3kAbCNAAgPOATx2igjwOZ8IS9wC7dw_SBCbF2RroJ0Lp6QhpRQyxQ0B-q4yJ_xEl1AW9sR9xiEbAnyIwMCGum9I379G3lk04hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=P2ALipjIwGSSRNEJpDedwnMGGftER1JqXcs0swhkSKzWBIhVIS9RnXUP9wqrIZz6CWW8qg4OLKYrojSEFpSUKz_y-GOXQyyVViRQrUzt6qYN9tOH7KTDfn_qo_IPB7iTZ9qykFrVBxGwxrv9ZYvoXa9YZdC-k74MTPseSGayCrOvCnBWHh5ezj3gzTx9D8vuapIU-X3z9tjiDSu9PEe-ZDk9u8pGaO4zIg4ibgmILtsidGQVMQ2j3kAbCNAAgPOATx2igjwOZ8IS9wC7dw_SBCbF2RroJ0Lp6QhpRQyxQ0B-q4yJ_xEl1AW9sR9xiEbAnyIwMCGum9I379G3lk04hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل سوم سپاهان | احسان حاج‌صفی '47
سپاهان 3 - فجر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/Futball180TV/108126" target="_blank">📅 19:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108125">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=XeYco3vDgOGvqABL8XmoNgCAnh1BQpvunWwXtm0dn8ehpyP2KPrqBBC3aNd79mSYsIOxIsHPNklEKee7UbcCveYl2P1FCLH9LoBzGvwdr9PnkdeuMzURXgtyZaP15jNms9TUjlCB_WUgsHj0aKzMF0X6SCXmmejsrvITIOdeG8N8wnseIa9knV-aYp_feZ9MO1gOGEZuWYyIAvaWjG5FY2SKE_yFK80Ws5U4yx7d-kBp5hbtWcsRUEtHQpLoVDb4agO4pOOUgH8elOxQo9hSRIgKs6uneQCcglqxGluO7FtKIF7Tty6hI3XEprkcQRbRrRD4OuzgbA1YE0Xb2oohxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=XeYco3vDgOGvqABL8XmoNgCAnh1BQpvunWwXtm0dn8ehpyP2KPrqBBC3aNd79mSYsIOxIsHPNklEKee7UbcCveYl2P1FCLH9LoBzGvwdr9PnkdeuMzURXgtyZaP15jNms9TUjlCB_WUgsHj0aKzMF0X6SCXmmejsrvITIOdeG8N8wnseIa9knV-aYp_feZ9MO1gOGEZuWYyIAvaWjG5FY2SKE_yFK80Ws5U4yx7d-kBp5hbtWcsRUEtHQpLoVDb4agO4pOOUgH8elOxQo9hSRIgKs6uneQCcglqxGluO7FtKIF7Tty6hI3XEprkcQRbRrRD4OuzgbA1YE0Xb2oohxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری‌زاده : یاسر آسانی بازیکن تاثیرگذاری است/ بازیکنان تعویضی تلاش خود را کردند.
🔵
کادر پزشکی تلاش می‌کنند تا او را به الغرافه برسانند.
🔵
امیدوارم مصدومیت او جدی نباشد ولی احساس می‌کنم کارمان یک مقدار سخت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/Futball180TV/108125" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108124">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=lhArvIoUtzGpr3B2uQaegpTzqveJ5mJNub3BD-iP89tMi_G2Gnob23VvpSt4tLw7cIqKiHpKnMUZTd-9i0__KjXbNlaIhXdnLVRG7FjPgUTOL-3nyCQX33c-pt8BkyIBHIV1Jrwl3jPdxheIKIQQjYPVWKD-vE1_JCnPx1irXPVSffznM16AkNDbvPK6Wus5H9PKBNAKPnGhKhiysJz4MouT38ELKyRZlrEDJINmdAlUKkbfHuUIXWVlQWQIjhgZMF44XXGpR_V4i2syqHUkmulKdyGMaHCcETW5ETL19jiPlqvRegIlkrEoYXQCnp7qFrG8eW2Lbv-YVN4aODqMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=lhArvIoUtzGpr3B2uQaegpTzqveJ5mJNub3BD-iP89tMi_G2Gnob23VvpSt4tLw7cIqKiHpKnMUZTd-9i0__KjXbNlaIhXdnLVRG7FjPgUTOL-3nyCQX33c-pt8BkyIBHIV1Jrwl3jPdxheIKIQQjYPVWKD-vE1_JCnPx1irXPVSffznM16AkNDbvPK6Wus5H9PKBNAKPnGhKhiysJz4MouT38ELKyRZlrEDJINmdAlUKkbfHuUIXWVlQWQIjhgZMF44XXGpR_V4i2syqHUkmulKdyGMaHCcETW5ETL19jiPlqvRegIlkrEoYXQCnp7qFrG8eW2Lbv-YVN4aODqMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | احسان حاج‌صفی '38
سپاهان 2 - فجر 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/108124" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108123">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=QCyBQzB2pRNfu4zk3Xut_chJtdUoqqYLmhWQruFECv8T--ZE_z1duspfbEDVgn0GSk_BsXSNt8PX2liy-Gzdj21sjylMp7v3mqQb8VrpMcsfPxLYI35XWtWuxaZmpNveGhY3CUwYPCkH-3Ao6CuXtOL3f-gHGnrqoo5CrGYy_supESP5YMWszZPJ6qmyEMgwmfqmKTi880LBwW0cFM4HH4XTs0ckAv_au-HxO_BbyVvKxr-gxRtTuCErQt6o5m4YQnm9be-JK0KATafqaivAWwoKYWMqt3YfeuuDfRcCliPKucRLOOlJoMaLX_JB1cTy-Dd-8YbGSA87MvBRyi2fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=QCyBQzB2pRNfu4zk3Xut_chJtdUoqqYLmhWQruFECv8T--ZE_z1duspfbEDVgn0GSk_BsXSNt8PX2liy-Gzdj21sjylMp7v3mqQb8VrpMcsfPxLYI35XWtWuxaZmpNveGhY3CUwYPCkH-3Ao6CuXtOL3f-gHGnrqoo5CrGYy_supESP5YMWszZPJ6qmyEMgwmfqmKTi880LBwW0cFM4HH4XTs0ckAv_au-HxO_BbyVvKxr-gxRtTuCErQt6o5m4YQnm9be-JK0KATafqaivAWwoKYWMqt3YfeuuDfRcCliPKucRLOOlJoMaLX_JB1cTy-Dd-8YbGSA87MvBRyi2fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/108123" target="_blank">📅 19:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108122">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=nG0n2imOKNkg0oTH4SB_sVNJT6sBXsKeEZYjxtQ0QwMEVG3a4zk-HwjdPu8nFQaSR0aS2D1XXyKW67eEpSN45IbSVPWuGQ86A7xr5Vqih-dNUhmdpArbGIdfaIM-7akLgioPgauuNxHReSSJr1hUeaYAD9Tahsus2w7xmtUm4AMyaHNiUSspWwKOTm5FZqFizWhNBU3g-FH_rstjwh0scKCCoPHqw-sdzPhLavALFF94L6mh5hZYp53zaMcXhXc62VfQpHI8_0fnXRAQ8K-Kmn0mHA1jYlJ8N60LqFWzlFGCAD67NVupcq7qq2MuFx3JZyI483htI-fWitqjM0GCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=nG0n2imOKNkg0oTH4SB_sVNJT6sBXsKeEZYjxtQ0QwMEVG3a4zk-HwjdPu8nFQaSR0aS2D1XXyKW67eEpSN45IbSVPWuGQ86A7xr5Vqih-dNUhmdpArbGIdfaIM-7akLgioPgauuNxHReSSJr1hUeaYAD9Tahsus2w7xmtUm4AMyaHNiUSspWwKOTm5FZqFizWhNBU3g-FH_rstjwh0scKCCoPHqw-sdzPhLavALFF94L6mh5hZYp53zaMcXhXc62VfQpHI8_0fnXRAQ8K-Kmn0mHA1jYlJ8N60LqFWzlFGCAD67NVupcq7qq2MuFx3JZyI483htI-fWitqjM0GCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
شجاع خلیل زاده بعد از پایان بازی با عصبانیت بخاطر تصمیمات داور، راهی رختکن شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/108122" target="_blank">📅 19:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108121">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=E57nuKn0n5RUSatihExTWOTeIjGSy1WxbW15UEf9RDMeCmOqrWMUVTL-IQyye8MJHCz3Drhp4qvqWW3742MXVdJJqePu7vLDx1UGM2a_1lZSsyfgXgs9kuwD26DtNUr5JO5uRzgLgBv6hYa4uWfAMQxEbgf1WCZUnAJHb3HKStzV0No5-qNA1vgRB9uJ1l74JV11qEWFjzEht77GAZz5nTf0Dz3RD1i_X7FpIK-0iHD9k51bYiMl1a_tV9OeMrD-Z8J71PJgbBUqH8HIghSIsU4K0l81SSTDIvVGCA6_JU2BOyvT8a5cW2YkzK9FeOK1AbaMVFynKSXxcupsrhutdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=E57nuKn0n5RUSatihExTWOTeIjGSy1WxbW15UEf9RDMeCmOqrWMUVTL-IQyye8MJHCz3Drhp4qvqWW3742MXVdJJqePu7vLDx1UGM2a_1lZSsyfgXgs9kuwD26DtNUr5JO5uRzgLgBv6hYa4uWfAMQxEbgf1WCZUnAJHb3HKStzV0No5-qNA1vgRB9uJ1l74JV11qEWFjzEht77GAZz5nTf0Dz3RD1i_X7FpIK-0iHD9k51bYiMl1a_tV9OeMrD-Z8J71PJgbBUqH8HIghSIsU4K0l81SSTDIvVGCA6_JU2BOyvT8a5cW2YkzK9FeOK1AbaMVFynKSXxcupsrhutdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
گل‌اول سپاهان به فجرسپاسی توسط آریا یوسفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/108121" target="_blank">📅 19:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108120">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoLuhFZM1xg9wjPxoYEk0seQ8BGtKvJTbS-3MrmQ3HBLCw688qgsV6e6nqkVdaRZTm9zrvp7gTAye448GJ79-UR4MSCVH_7khvfBOwFEmh8HafD5colfNtHndIOkJeLJEtjOu01Lma2zD5v4khkkxbRR2VsDVNt57n5-zktx0TuWtrcLcDD8G3n6Gic5NokTEOb8Q0wkluZokjATLCvHgdik8JC-7yKYJXIhr8FSJ9UItRPqaJfhVNUptrLY_xWAlQjVaRvYtExJfOVcHaUyUj-BGay-Zo3eD-N43UP0c1U3JUpoZCkoKsxEEhfaYT-F_AMmSEP_FQ7ffiTQPf8Aow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/Futball180TV/108120" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTJ0Xp-HevS_NeJyh0scpWAFUkCp2EySRB9U3HBBUTsZYjkJHZUs7ue5RKAEwWeTvc49RNkArnU1Xn5NgdPbMeu_1d4RZGG0L12A0xRIerdKc5XOwezeQeXF7C4kNYP_S46HusKOUCpzoXEhGIxIdTjg_K6z4tGnlPSfWMJuZnjUsrL-dv79B3mO6tIlNAXBJfN3hJKy5iEXHLqxMZvGiWk6crugJ8WqLnMBvSX9uewGiW6zXXH2Y5BCYTNeORP8Zvd_8DWZueJpmKOQJpdcw4igpf3JvsSz1wxu51p4-ZzanIm46hMooWNpFk_RgQYX1LiaKDcKIaRJOZgVR9BLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/108119" target="_blank">📅 19:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxiepUfJgcyiC0k5K8Gbidcry3RBeqZzmfrhyVzzebVHQFODFISFgHQS-YoKZi_vswEJL3k33GkY4kHYyZzSiZNwgKb3G19CeYwRCOLQGmhuVaHZdzn9zilGIP2QnX_TIoXrJbmMCse5IdtA6StHZbwzsGm12V90vhWPofeDXinYiwonnLV4_z3vADacKbyswgkPO9ZTUwkl2sqZe3t0KHpZO8ddQ8qo9Jb6iRzT52qdN2eXv1JfuKxP9b83x6mfiV8yjAmS6XFa1WNmciwGQAVjkwTOeqrDPVdwYB8mVXhYPlITObR_2dmovao3KBkdPh5KxZSmkXskIjNpeVJzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/108118" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=aCF03mBwG8zDMgOUtB26I1zmADSbuIWU3mt2d7ntB2A9Nw9LRfnkVlxNwF_BSPxl_iAyM2DyhWHnBnxcG5ZKIuDNdE20geQ6Q76qVjkVMTp1HeN3NfQpmv-s7lR5HdH-viv6w_2aOXUxAxUO3MrNTQzazJxzow7PsCZf-ickPKZQIzui6l02ElofIKVmeNVcVv3xrJuP3X6cEhZ-Z-r8r2aEdln8IHctRKM4Bd9m1W12zV-nJ6ZxbYtVLPSnGE8s6ekXUXyTUYtDXUdl_J-wBeonAOpVyj5AT12_tinzezqdtCiUCMBaPQo95jQT6HTMJqbQsxtl1u5RgETLuCLO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=aCF03mBwG8zDMgOUtB26I1zmADSbuIWU3mt2d7ntB2A9Nw9LRfnkVlxNwF_BSPxl_iAyM2DyhWHnBnxcG5ZKIuDNdE20geQ6Q76qVjkVMTp1HeN3NfQpmv-s7lR5HdH-viv6w_2aOXUxAxUO3MrNTQzazJxzow7PsCZf-ickPKZQIzui6l02ElofIKVmeNVcVv3xrJuP3X6cEhZ-Z-r8r2aEdln8IHctRKM4Bd9m1W12zV-nJ6ZxbYtVLPSnGE8s6ekXUXyTUYtDXUdl_J-wBeonAOpVyj5AT12_tinzezqdtCiUCMBaPQo95jQT6HTMJqbQsxtl1u5RgETLuCLO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال توسط حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108117" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سید مهدی حسینی</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/108116" target="_blank">📅 18:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تراکتوروور زددددد</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/108115" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/108114" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=UpfpocweJejpdB-TdSvepfuSzG1fiOl7NdSWTFDUlbMiZU8h4Oq3bYN-DjEusonToZB72OzLYip9xRRRnTl40suWuhDlwCJCbvYjoJh1DL6lgF37KB2kFGXi2uTPLgFJxhdoghAFan3oqeeG9MlCPCxBaI_aXgVASjXR6flIISr4KKZQG21dmO84Lb0Oz-77CxJaj5WW9qXvJ-ZWSVa03-ekzKlK9n61fsq5UGyUq59etfrgt5z2jynJkM7SZAENSWdLSe1xSL2WmMw6F9jwAYSqQMy9A6V6OSXQg-4Vyuil3usY0w6agGIjSvWOlM4wvCAnVSkqezAUEq9ZgQOwGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=UpfpocweJejpdB-TdSvepfuSzG1fiOl7NdSWTFDUlbMiZU8h4Oq3bYN-DjEusonToZB72OzLYip9xRRRnTl40suWuhDlwCJCbvYjoJh1DL6lgF37KB2kFGXi2uTPLgFJxhdoghAFan3oqeeG9MlCPCxBaI_aXgVASjXR6flIISr4KKZQG21dmO84Lb0Oz-77CxJaj5WW9qXvJ-ZWSVa03-ekzKlK9n61fsq5UGyUq59etfrgt5z2jynJkM7SZAENSWdLSe1xSL2WmMw6F9jwAYSqQMy9A6V6OSXQg-4Vyuil3usY0w6agGIjSvWOlM4wvCAnVSkqezAUEq9ZgQOwGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
داور بعد از بازبینی VAR گل تراکتور را به دلیل خطای هند  بازیکن تراکتور رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/108113" target="_blank">📅 18:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/108112" target="_blank">📅 18:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
احتمالا خطای هند بازیکن تراکتور</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/108111" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صحنه داره وار بررسی میشه</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/108110" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726254fc85.mp4?token=K6l_mHlhtPHEaTzYrMA-ubD7bO69NUqgLRbCCStziOT3hq1J9F0-FlE6jI6ID8ajjlN-47Px2EfgWaRuevnD4JZTtssaTxgSEUm6KqbZqo38h-4P6W0meKJHAB9XNjvehWCluOJYyvYHsEZ4LZJrOyMGn7Xmv9t2-3dwjhIUCCe5Scd5cRKIaXYelMeIAXh3brvKYB-fubDp4rCpTJ72dRIofnmrOK1JskSH7ToTXlZd-H_uUYFsbXSHqo4kRIsA6FhVRgw6dzrccmHtq6Bz12EcCCk3Z3VpQ3pFaIRISPFAkoUIQWJQKt_gadmZBH8VWvLyyT7SMbJtxeZ2q_JgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726254fc85.mp4?token=K6l_mHlhtPHEaTzYrMA-ubD7bO69NUqgLRbCCStziOT3hq1J9F0-FlE6jI6ID8ajjlN-47Px2EfgWaRuevnD4JZTtssaTxgSEUm6KqbZqo38h-4P6W0meKJHAB9XNjvehWCluOJYyvYHsEZ4LZJrOyMGn7Xmv9t2-3dwjhIUCCe5Scd5cRKIaXYelMeIAXh3brvKYB-fubDp4rCpTJ72dRIofnmrOK1JskSH7ToTXlZd-H_uUYFsbXSHqo4kRIsA6FhVRgw6dzrccmHtq6Bz12EcCCk3Z3VpQ3pFaIRISPFAkoUIQWJQKt_gadmZBH8VWvLyyT7SMbJtxeZ2q_JgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/108109" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108108">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تیبوووووور هالیلووویچ</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/108108" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108107">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تراکتورووووو زددددد</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/108107" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108106">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/108106" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108105">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همچنان استقلال از کووووون میاره</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/108105" target="_blank">📅 18:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108104">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استقلال از کوووون آورددددد</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/Futball180TV/108104" target="_blank">📅 18:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108103">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppyk0v_gHL4fc8HcSebOR6D5tOhqmfQdUE5eKyZ9LeI8O8AYGfTwRlImiz2DzqTn1e0Lgt80LfL-JhIeiCRPvE4a2sf_4zWQlThlziiDFIaNeN3dkp42X3Vkjt19NfmcNmOILrXW7dqMONyHXP4nBNEqC-nc3EtNwj4JQS1109iudtD3H375fs0DilNTonDCgSmAcgUfR-Gb6arqWLetiKWL20Yj5QGPKZXRN5vGIs-GF6X1Msz7kRoiuYAaVxht83TBNIUpm6cWCbV0xiRnLi0hoJ1sdmhvecoxI1oThHmK2fJmPuFNJjLVJqoPxE5dcRUrEhtua-oQ2ZJv-Q3Wrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم فوتبال فولاد مبارکه سپاهان برای تقابل با فجر شهید سپاسی⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/108103" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108102">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRloVY5XxMlTMY_dfOd2KPtJFY_MB_QFYMQbTsgjfPpCpBrQ_lhOWEP6Ny7_xLMgimnOdRgJKhun4qeMm2VQls7QebGn-8SUm5ykZGMj-fFobm6f3M7mgqWGFhkmIjA3B55rQNP0mRuXCdV55KGvhyXPZwCbHj7ZuiiQJYK9T7z4rHopX31vlA--k2ueYaIY1Uf9C7JITM-jIjGg6Uwvta9aiz-2CjbPOXSeuPUWPcpeir0yGWDz4D3fDj_BVV78uiFkFBRqzRN_DZ6vUo1DxKt54qqHvsvGWgvGWl7KxmFuuFXXsO-M9jNqKJV8J9605sZf5Efnz5TtQg8T2JP-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📲
استوری منیر الحدادی درحال تماشای بازی استقلال و تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/108102" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108101">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=WuOmeoGFstcK4jzgh-Qym39qEPzpcBjqtjY0NcoTZrrZo9179mqqujHxXrMNvkrPl6CWGnYl5Jqc2VV82XUNbIiLxV2C0WC-bB1ZlKCJCIrPXapg306vr8KMWuoTlDJp0E3NxslWmk9ROl4E3leshlR6Ki4FTl7GeI1rfVBxLdsS-ocWNYdeH1HYKfG5c3kVpKgXMlyL1aWww3PVEvOq7xKoHTPrXh_qOFVs9sWaRu-I3rifhYjHP2B95lMfvFuichpPxnEleTfcLYdFtPZtS2QkRRkjWQ_cpyKJdXMpJPMHhgkkZvqarcLspIBSYCHD9LEJe39vBgLNtzVfaxRGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=WuOmeoGFstcK4jzgh-Qym39qEPzpcBjqtjY0NcoTZrrZo9179mqqujHxXrMNvkrPl6CWGnYl5Jqc2VV82XUNbIiLxV2C0WC-bB1ZlKCJCIrPXapg306vr8KMWuoTlDJp0E3NxslWmk9ROl4E3leshlR6Ki4FTl7GeI1rfVBxLdsS-ocWNYdeH1HYKfG5c3kVpKgXMlyL1aWww3PVEvOq7xKoHTPrXh_qOFVs9sWaRu-I3rifhYjHP2B95lMfvFuichpPxnEleTfcLYdFtPZtS2QkRRkjWQ_cpyKJdXMpJPMHhgkkZvqarcLspIBSYCHD9LEJe39vBgLNtzVfaxRGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشک‌های یاسر‌آسانی هنگام تعویض از زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/108101" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108100">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⭕️
یاسر‌آسانی در پایان نیمه‌اول و پس از سوت پایان بازی بدلیل مصدومیت روی زمین افتاد. باید دید در نیمه‌دوم تعویض می‌شود یا خیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108100" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108099">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
⭕️
یاسر‌آسانی در پایان نیمه‌اول و پس از سوت پایان بازی بدلیل مصدومیت روی زمین افتاد. باید دید در نیمه‌دوم تعویض می‌شود یا خیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108099" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108098">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab3fc2522.mp4?token=c90q1NRLOpALEBuItp5hbhjiMgsfRWCLCTsm-6OBaixmFPLYOKRkwLfahLofdTye4TgjUmU8sdrh-iMlWhtLtqR4PhumYDKa3VTS9n2UKsAJjLcxkjaovgXdyYwxB1_7jQlf2Rx4wan3LxB9YDTuR_zkydtMP08W4T1b_FcWyLs397VSpqFJkzmvUrMX2nxABm9Z04RDRs_0Nbe8PGbspOQvtuicelrPd7UaBHwTARwg38811JZvFRAlZLYBQAzMug4GqvNYg3q13EClq0kyv7Q11OI_MeC-duvdX6a0QLAi_V3WVqVwa-wOG98V6gp0LzcbxbAJ_x4CjyEa6MK9vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab3fc2522.mp4?token=c90q1NRLOpALEBuItp5hbhjiMgsfRWCLCTsm-6OBaixmFPLYOKRkwLfahLofdTye4TgjUmU8sdrh-iMlWhtLtqR4PhumYDKa3VTS9n2UKsAJjLcxkjaovgXdyYwxB1_7jQlf2Rx4wan3LxB9YDTuR_zkydtMP08W4T1b_FcWyLs397VSpqFJkzmvUrMX2nxABm9Z04RDRs_0Nbe8PGbspOQvtuicelrPd7UaBHwTARwg38811JZvFRAlZLYBQAzMug4GqvNYg3q13EClq0kyv7Q11OI_MeC-duvdX6a0QLAi_V3WVqVwa-wOG98V6gp0LzcbxbAJ_x4CjyEa6MK9vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
نوید مظفری، کارشناس داوری: در دقیقه ۴۱ بازیکن تراکتور هیچ خطایی روی بازیکن استقلال انجام نداد، جاگیری، زاویه دید و تشخصی داور عالی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108098" target="_blank">📅 17:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108097">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827ca52e8f.mp4?token=OQYV-p3zgQJ3Tw-RqAAIj_g-ZLFxiEI4FFmu-drohDTc9QGvYULIRhXe0BEz25qOGqP_29pGwFIFx5JWjTGEK5An2qF6ofJUmJMGvl_XvtKQYT64dZ_DeMQYrl2sQkfT3L74N4PKntYo549P2MUb2OKs0AzeNOlfD7fENBpmoz7N4Vboz9UyTPhZgjyQTeCypk8KqYwh1QycDwiypWy4medDmWRqQgbne0k9JdWqJZYCRgsLL1c-j0bI6PrenPAww_wX-nKWDYUFlJQzingDK6oSEwS2i8VKszPwzBgjw5uz1MtSmjcAGAZ_CMuOSsGgqWX2Lu0BFTrvUFCBYiL2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827ca52e8f.mp4?token=OQYV-p3zgQJ3Tw-RqAAIj_g-ZLFxiEI4FFmu-drohDTc9QGvYULIRhXe0BEz25qOGqP_29pGwFIFx5JWjTGEK5An2qF6ofJUmJMGvl_XvtKQYT64dZ_DeMQYrl2sQkfT3L74N4PKntYo549P2MUb2OKs0AzeNOlfD7fENBpmoz7N4Vboz9UyTPhZgjyQTeCypk8KqYwh1QycDwiypWy4medDmWRqQgbne0k9JdWqJZYCRgsLL1c-j0bI6PrenPAww_wX-nKWDYUFlJQzingDK6oSEwS2i8VKszPwzBgjw5uz1MtSmjcAGAZ_CMuOSsGgqWX2Lu0BFTrvUFCBYiL2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
موقعیتی که یاسر آسانی به این شکل از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108097" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108096">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
صحنه مشکوک به پنالتی برای استقلال</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108096" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108095">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108095" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108095" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108094">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYURxcUFkMhA89NErbkClaCpO1fV9j4LXfc6Z2WogcF7-jtxihbm5b5Sy98dIfM7D-Yp0tjH2BqOrOjJDVHoqUf_6K4HSuBbMcexYHVv4G93MTuu0G8IiavoBgLBjTIKmh7BYGmapiVZZvxWAN7KW80CO1z1VAR6vzDKW_ShWkPKlAkvyMrIvO-JHAFoZWyDdMEpNxZ7PMdvHpB2-VTg6glEA3WevEgdPojoF0AnLG0dcf1GmEkK16heIeLJaJz5rkNQf1dRAQDhkxFOdp6BI3MfpV6nFCbgyj-Iegyi71_Fn3F54oFZOyNVmNrKtjitqOtAzADurGMBGTGHpaJfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108094" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108093">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9b37ccf7.mp4?token=exeVjZpmw5cYbzOMjYiUL6F-Mt1MjdrVuRWC6dLxApCW5HCT0gQYCp55R8rVzT1sxwJ-8f_NwK-Q9PI_AS1Gu2gMNiSCwG8ZAImUMdZ3gcTYWnEDx5y-zl9r-qwrwwmrh46h4hY0eer-t3f1MU9RmKEPGYkmWpndBELmuk9EHUDntzeOC4yjNroMHS1SEz0GageHpPQbJGSqzsX58RVq3Hpn8Gh8uAjT_LbrhkFPLP5ahYOLPpWbharA1xgD0H2n47RLP_hje13KCpESMI2rDyi2UwgW1vUliqXlEvxt9zkUc4-q1NhB8_vGmKaX28S49C5Dr9dQw1pzUALiyJaRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9b37ccf7.mp4?token=exeVjZpmw5cYbzOMjYiUL6F-Mt1MjdrVuRWC6dLxApCW5HCT0gQYCp55R8rVzT1sxwJ-8f_NwK-Q9PI_AS1Gu2gMNiSCwG8ZAImUMdZ3gcTYWnEDx5y-zl9r-qwrwwmrh46h4hY0eer-t3f1MU9RmKEPGYkmWpndBELmuk9EHUDntzeOC4yjNroMHS1SEz0GageHpPQbJGSqzsX58RVq3Hpn8Gh8uAjT_LbrhkFPLP5ahYOLPpWbharA1xgD0H2n47RLP_hje13KCpESMI2rDyi2UwgW1vUliqXlEvxt9zkUc4-q1NhB8_vGmKaX28S49C5Dr9dQw1pzUALiyJaRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رقص آذری سعید سحرخیزان که باعث فحاشی شدید هواداران تراکتور تبریز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108093" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108092">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2859c6f67.mp4?token=gA1QAUvfC9o4Ni3iEW_BwUjCjSgQVn-dOD1gcLpalZCkdLtZYaEb9CXaOZv3eeBCoXupBfTn7ebHE_mOcpTNEERlzeFXlHIwDUQ11Jbs4Vzt1POH16tb__GTXOAeAoS8XMyGlQjdUxWUOhJPl8bxO3iHT69yvs0FR2iBe2aK3MEdDwM_gNs3Vpqhr5H9jsNRW7fzlQ0ZOvyWAqKkSiOJctkELkMU-7VO0O7xsbk5qdnttv-emSIcVeEHTWASbqEg3fAG6c7XhWmDddAHdegRB2fSQovsMeR4mK7CJplV6zFNb1bOGxArhJMg47zWpFZwh5yr9J0xwpcFotkuznkKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2859c6f67.mp4?token=gA1QAUvfC9o4Ni3iEW_BwUjCjSgQVn-dOD1gcLpalZCkdLtZYaEb9CXaOZv3eeBCoXupBfTn7ebHE_mOcpTNEERlzeFXlHIwDUQ11Jbs4Vzt1POH16tb__GTXOAeAoS8XMyGlQjdUxWUOhJPl8bxO3iHT69yvs0FR2iBe2aK3MEdDwM_gNs3Vpqhr5H9jsNRW7fzlQ0ZOvyWAqKkSiOJctkELkMU-7VO0O7xsbk5qdnttv-emSIcVeEHTWASbqEg3fAG6c7XhWmDddAHdegRB2fSQovsMeR4mK7CJplV6zFNb1bOGxArhJMg47zWpFZwh5yr9J0xwpcFotkuznkKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پرتاب بطری به سمت بازیکنان استقلال بعد از گل اول این تیم به تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108092" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108091">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c35a7666d.mp4?token=Zzvfo3g5nlkS56Yt4loKsfL8NEOapyCy2WhDRXkVNs-l_7w2qi2XEsbdwCXdbtYz3lzFJ35Xz-r2VCKOU8gy9PLonr6ahufyGG8872C-jGTGXZMXa2mSkxD7YHB_WPCuj9pv59P144viA3STBiB5GRhRr7Fj-JLEzI1Dx1bpLvs5qF8gKMy5eRqINBov2r1hvhZ9N6tSWxSG-pT8nAWNi9glFpSv13mk9bjZTkbLQZh4TuoY4gsozuu6XSjB2IKF9oUEWzKVS_XKyLtWpWc7Geh-UoS3_wHuV5g5RR_SI0MpRrWt3ijIQsnfeASpqNJiBQEWZQEJ6yYOFcNtUoZMvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c35a7666d.mp4?token=Zzvfo3g5nlkS56Yt4loKsfL8NEOapyCy2WhDRXkVNs-l_7w2qi2XEsbdwCXdbtYz3lzFJ35Xz-r2VCKOU8gy9PLonr6ahufyGG8872C-jGTGXZMXa2mSkxD7YHB_WPCuj9pv59P144viA3STBiB5GRhRr7Fj-JLEzI1Dx1bpLvs5qF8gKMy5eRqINBov2r1hvhZ9N6tSWxSG-pT8nAWNi9glFpSv13mk9bjZTkbLQZh4TuoY4gsozuu6XSjB2IKF9oUEWzKVS_XKyLtWpWc7Geh-UoS3_wHuV5g5RR_SI0MpRrWt3ijIQsnfeASpqNJiBQEWZQEJ6yYOFcNtUoZMvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل اول استقلال به تراکتور توسط سعید سحرخیزان
28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108091" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108090">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اوه اوه هواداران تراکتور رو تحریک کرد
😐
😂</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108090" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سعید سحرخیزان</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108089" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استقلال زددددد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108088" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگگلگللگل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108087" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108086">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
✅
تایید خبر اختصاصی فوتبال‌180؛
🔴
شکایت بابت مجوز کار بازیکنان! نامه باشگاه تراکتور به پلیس مهاجرت و گذرنامه آذربایجان شرقی درباره بازیکنان خارجی استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108086" target="_blank">📅 17:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2316aee10.mp4?token=qpL5KFzAMuUgKEyG9ovlkyH1LbohWQskPBR1oWZpfL0aKjTzZ8FSKHrzomVcFb1iHtTszRd3-hjn_k0kFGTJNadyDx5qXPFpsb6LNktqfkg9FTMAEdnGK_nzDyK_rSSgCN-KtPXO30ATTkUeL9pZkuVDFJttqxfWkpZa8t7pb5bP9Fluxeqrzh5_EplCVQdgESM_Jkr9PrU-wyiTlmstnwtVLLWksSxttjIeIqQmZ8p2NpjzOA0DMPzy41YigE11y-hxBOT9YFHd3KZ7IEhGmMStojCKPi0WazdoN4SkTEazzMDK5LPSDBPinucXDd3CUER2LjHUhpHsxS5yhvoC4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2316aee10.mp4?token=qpL5KFzAMuUgKEyG9ovlkyH1LbohWQskPBR1oWZpfL0aKjTzZ8FSKHrzomVcFb1iHtTszRd3-hjn_k0kFGTJNadyDx5qXPFpsb6LNktqfkg9FTMAEdnGK_nzDyK_rSSgCN-KtPXO30ATTkUeL9pZkuVDFJttqxfWkpZa8t7pb5bP9Fluxeqrzh5_EplCVQdgESM_Jkr9PrU-wyiTlmstnwtVLLWksSxttjIeIqQmZ8p2NpjzOA0DMPzy41YigE11y-hxBOT9YFHd3KZ7IEhGmMStojCKPi0WazdoN4SkTEazzMDK5LPSDBPinucXDd3CUER2LjHUhpHsxS5yhvoC4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇷
🇮🇷
کری‌خوانی تراکتوری‌ها برای استقلالی‌ها با پرچم‌های قهرمانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108085" target="_blank">📅 16:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108084">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1e614300.mp4?token=GUTjQ05U3RFM7g47MBpC1X1ViIDWNjP2-_sS6oKjI2SIxB4GtoWHa0E3tcHA0hPvDe_8NN3CueN0CLn8nyg4wGXt1-U_1CNWrTpj3RSMVwee1g89YoPdRnXNep69G_j1daAKr6cEI10rbEnDw8q6HqsWn8sU7tHsoqGJUsewHm_XAjl3o5fmzUv0jnuTPq2OmaseTBVD-OVFMAaw1xyuCpaFeIwk2V_U9paXHhL4oDclrES6jBlY7zLD_Ps70gglXWoj6wt3yYJE45WYUVCPpEhQP_MwTK_2yxOsrepFiV5XCsC9zhcTnYfAKvGgUQakshml3fJbR4-PUOj4mBnsM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1e614300.mp4?token=GUTjQ05U3RFM7g47MBpC1X1ViIDWNjP2-_sS6oKjI2SIxB4GtoWHa0E3tcHA0hPvDe_8NN3CueN0CLn8nyg4wGXt1-U_1CNWrTpj3RSMVwee1g89YoPdRnXNep69G_j1daAKr6cEI10rbEnDw8q6HqsWn8sU7tHsoqGJUsewHm_XAjl3o5fmzUv0jnuTPq2OmaseTBVD-OVFMAaw1xyuCpaFeIwk2V_U9paXHhL4oDclrES6jBlY7zLD_Ps70gglXWoj6wt3yYJE45WYUVCPpEhQP_MwTK_2yxOsrepFiV5XCsC9zhcTnYfAKvGgUQakshml3fJbR4-PUOj4mBnsM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
رقص و همخوانی هوادار استقلالی با آهنگ معروف تراکتوری ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108084" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108083">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ca421470.mp4?token=ryaM3ZRljslYX1hu21jwWvE62Dxj17cGLNLQTn2GXgDQ59YjPsFSCA3_KEFXCBfzcgoS5DXq7qKwgtuKiyTnWSWFCE7Jy3lf4tp18M0Sn5THreIH_4VbmTMUABgHPxsXSTsU_qlwH-u64M-MLem8NSxyVrXP5sWLb6kQ-lj6nAyrdQcOvBmVbniOdDjp3al4hdHk3LbEE8TPid0HsYvRq15ODgwmsL_8DH4c4ncbyZDMarwSBHSN7sxdWZ3kPzpi_xsrkVMmdJ8cJAo-2u4Lh1pbaP3JDdRzTucAapYewcIHT1WsTrZMTw1gTBSf1ospFCBZIohBqF9otpA8jUkAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ca421470.mp4?token=ryaM3ZRljslYX1hu21jwWvE62Dxj17cGLNLQTn2GXgDQ59YjPsFSCA3_KEFXCBfzcgoS5DXq7qKwgtuKiyTnWSWFCE7Jy3lf4tp18M0Sn5THreIH_4VbmTMUABgHPxsXSTsU_qlwH-u64M-MLem8NSxyVrXP5sWLb6kQ-lj6nAyrdQcOvBmVbniOdDjp3al4hdHk3LbEE8TPid0HsYvRq15ODgwmsL_8DH4c4ncbyZDMarwSBHSN7sxdWZ3kPzpi_xsrkVMmdJ8cJAo-2u4Lh1pbaP3JDdRzTucAapYewcIHT1WsTrZMTw1gTBSf1ospFCBZIohBqF9otpA8jUkAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
اتفاق عجیب برای فرعباسی؛
خون‌دماغ شدن دروازه‌بان استقلال در حین گرم‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108083" target="_blank">📅 16:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108082">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
هوادار تراکتور: استقلالی‌ها و پرسپولیسی‌ها می‌ترسند به تبریز بیایند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108082" target="_blank">📅 16:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108081">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI5TjW9Xs5B0rifLeuIL2Juf-RwUhW-sNMvmWiEQnR-fZDBzUro1HMNqU5dSWj4P8fhpDLbNedtfGCFPEwX-zE9FHgP6f59H4qWRZoxAbilDZz0IWdtwj1tlSSOz-QwLGxyefSwp1pSI9SmZcqB_d8QNTMvfH2f9DCR3ZmKWalzcdFzjNDUKb8qMAVxsnc2Ngx_g2yI4AA63irLqrAv0injL9LQM9FUGD7vPyKnu21qVFIPs8xzVgXq_6rGc37g0iBRIqjkMae2Dq-srtETNSCztSTC9jC808oVWDuiighWpHLT__aV-bVtYu9NLoWQMe4vJGz3yNJH3rzZF7Vzu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108081" target="_blank">📅 16:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108080">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a925bd26b4.mp4?token=o_qC0zH7o6E2wyEQ_qaA7dZp1_4TiHbDnTtHuxu4xkErQSa2JKL_P56kd3let2C6_oU97zuSzfbxanFq6hpvfaBMJNPq4KWSh1YM1gKW3VeHdVkebXdMkSly0PbZN3C7k4JRtFMqc2KdA3FwScTNa_Hkg6zQ9VQr_PqFcWoq9iOAarGjz3AC7D1xDXeMCxy7l-LZexirE5KbHepClsG3o6C4G3VLRXQNoUnsgK0ZUE026DeC2Ihvh_cPcawYG87SujeUHJHrWhQc_Ta6qyjUh_vkE-LnCOWRp74nphRfDs3rljeLlqlfa5BqJZzg9DXr3Ssm-u5BZ6dm9KLJ3UZb5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a925bd26b4.mp4?token=o_qC0zH7o6E2wyEQ_qaA7dZp1_4TiHbDnTtHuxu4xkErQSa2JKL_P56kd3let2C6_oU97zuSzfbxanFq6hpvfaBMJNPq4KWSh1YM1gKW3VeHdVkebXdMkSly0PbZN3C7k4JRtFMqc2KdA3FwScTNa_Hkg6zQ9VQr_PqFcWoq9iOAarGjz3AC7D1xDXeMCxy7l-LZexirE5KbHepClsG3o6C4G3VLRXQNoUnsgK0ZUE026DeC2Ihvh_cPcawYG87SujeUHJHrWhQc_Ta6qyjUh_vkE-LnCOWRp74nphRfDs3rljeLlqlfa5BqJZzg9DXr3Ssm-u5BZ6dm9KLJ3UZb5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
مشکل جدی قیاسی در تلفظ رولز رویس
گلزار: چقد فخر فروشی به مردم ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108080" target="_blank">📅 16:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108079">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzGuiAFejVLG8WrZcS7-ZJKBRb6W7RmxhkRK_PkB1cBCVHOeMtLyht2Oqe9_apIyRNcfNbvMNyUvO-dYnj4ucFWd3LJrV6kme4eopAc25iHuCPuMouc1rXp0oMH9cX8g4TvTHeDMjlpw39EQgLHWQLDTOJPVbRUHtB6Nk4eQUkbvxzGAgCNdnNjfESmaqBoBjui4Zw3y3WBWAOxanodGJJ6_exTw7nR0bxtVaRHMQAtJWyYouNtxb3GWYPtkGqpzTPx7tHzI7LKFRHhPOv6n4aRIU9XqvjgkcWZJteILImEwp6ZosUZhhBfro8YfG_3GYcYQdW3zFkAICv1-q-zCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب استقلال در مصاف مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108079" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108078">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-L9hZuVDqpNdVly__jUJGtrx3AMuzYf-4uHa-tSrMtNHEvqZYCAXzVIj3DvCrZdw06C75Pps8QH9roNs9f8g0W7HJkEF3bhXREVV4XLuvOX6jk6W-xcYx2q7GSrWRlDq5naN9nbcY-r_Ncehcdo9pR2EeFYiG8FEMuaj2YYdHNzVFvOrn9zJMCa1ASoY33dul_viWwD7LBgiqI_DcrFYPHDtjx_hbXVkwiIJZplIy1Evy_tVH7z_AFY1BkqjVpW9RbtAxy6-ioJpr1BFQ_EiHBYCZiLGA_gfLSLDYB7lBKGvxFDwjlw9dVDPUXu8ffwXKI6TEamYl3C1V1Zqri_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب استقلال در مصاف مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108078" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108077">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ea53f.mp4?token=dNXiixX6hd9RnHqTXjq25MEMQ7c1ovKZ5z-HwBBQEYfsliUVrk8BOMLjWAaDkW35MnSeLqccQ9tLqKxJViqkppWaJyMWNhi8hJ7fFVe8sRPu1wA8KYphZEgbomfhLkckxJdiKdIM_pCXtijc3te0vI6iq1iq1ePGSfaZPEQuSsztKtpahyCPpe7sW_q0FhEZbO-IUT0KHlhqIhNQhjjVJ2zxK9_e2IbWxYG9nie81L-CddxYOlw4THQCBRejhGSkMDI-FXm0V0iojRRsN3nxHYJKogiMZBmTattLgLZbG-l8NsEUN2yD4LxjHSC1dpUslDLB_OeqjkbulOrzK6n6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ea53f.mp4?token=dNXiixX6hd9RnHqTXjq25MEMQ7c1ovKZ5z-HwBBQEYfsliUVrk8BOMLjWAaDkW35MnSeLqccQ9tLqKxJViqkppWaJyMWNhi8hJ7fFVe8sRPu1wA8KYphZEgbomfhLkckxJdiKdIM_pCXtijc3te0vI6iq1iq1ePGSfaZPEQuSsztKtpahyCPpe7sW_q0FhEZbO-IUT0KHlhqIhNQhjjVJ2zxK9_e2IbWxYG9nie81L-CddxYOlw4THQCBRejhGSkMDI-FXm0V0iojRRsN3nxHYJKogiMZBmTattLgLZbG-l8NsEUN2yD4LxjHSC1dpUslDLB_OeqjkbulOrzK6n6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
هوادار تراکتور: بعضی تیم هایی که در لیگ نخبگان نیستند، از تلویزیون بازی تراکتور را در آسیا تماشا می‌ کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108077" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108076">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVaPcVg_bLloAt3vJX7VfIbn1tmMTp7tQuZSBQ1YnUtztCr83ScT-9eFeQRL5rMpN1jhUkQRNUe3GIcuiFkVnC6kjnN7NUxdo4S3K-TMSrVFohO6sgT5oX_42q8zP4xcQY76hWNiVx1U0tuBm9t45sbCPipjxxY0_vBjOe8oLx_-olpQZ95jaE7pyobsC2Czr_MgvfvByeYucLGj_K-EE7MiczlLdTMqD4FivinUXDR3M8JlxVh7Gkv_sRNTBoV1b1uuNYG0v2EMcQcAYzNCh4sewNii2OU-NMgq3nL3L62KnGmvfxqafpjHmBB3d8Lpd0l30SUiCSAX__MJn92NGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب تراکتور مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108076" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108075">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec3521bc4.mp4?token=qrQ_bMSmmSF0FUQOi7yZXDLwr98aFL7n865ODeWIPaXwIUocPBHBzXVABhBMjff5npkFGTAgG6-FhjQKG6zniurcQFgF7CzCD4GCCYuH_QF9CLcXD7dM-8alYiMKSZV9x4kWaM3Ub8-qWtxsDqkUC5adkkB8FUNT9cefDTSctBPR1lvizlJv3GTMioXWa_B9WixSH7tYtqJwv3oGAgERmCan7d0OyVWz7XbNs8Hkct8KCx1vqcZIcSfZHmBVIcA-zsopoKvivmhfY9sSQC_bYsbaRvY-VYGB0zJUQBHzGJigV2RwbeYVVqY_4Une8fbQ5mdhgcIkyyYY7HRxQJK0eAsFzudzziU3RaouaJialcCEhSifQo1I99YBb_wFMGr6scRPqkZ4wj2ugjc5chD6mD4pSbum1_yJ_-qzLeaSN3TZ-CBtPLPMDYstDdxM3EyzhcmboV0c7BH1bsBzFlLdyyhoStCgzGrDGOe92I6fgQWDfjr6sDfZ_KaOYnnn1GnoFn_9ND4P11Xp8K1YlvK4icW8Wywy0wwNktP11o6is3A3UeeidT22jYksWITs_be7PlwxEonp51cLp1qJTJ2SHjdCjYSLhNaVNYLfkmx5WLbFsFB-eE607B1HJXsiC6Y1yp6CT-WWBh184Gz7ToDgx9uTcdRWtef0jU-f7rv6QIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec3521bc4.mp4?token=qrQ_bMSmmSF0FUQOi7yZXDLwr98aFL7n865ODeWIPaXwIUocPBHBzXVABhBMjff5npkFGTAgG6-FhjQKG6zniurcQFgF7CzCD4GCCYuH_QF9CLcXD7dM-8alYiMKSZV9x4kWaM3Ub8-qWtxsDqkUC5adkkB8FUNT9cefDTSctBPR1lvizlJv3GTMioXWa_B9WixSH7tYtqJwv3oGAgERmCan7d0OyVWz7XbNs8Hkct8KCx1vqcZIcSfZHmBVIcA-zsopoKvivmhfY9sSQC_bYsbaRvY-VYGB0zJUQBHzGJigV2RwbeYVVqY_4Une8fbQ5mdhgcIkyyYY7HRxQJK0eAsFzudzziU3RaouaJialcCEhSifQo1I99YBb_wFMGr6scRPqkZ4wj2ugjc5chD6mD4pSbum1_yJ_-qzLeaSN3TZ-CBtPLPMDYstDdxM3EyzhcmboV0c7BH1bsBzFlLdyyhoStCgzGrDGOe92I6fgQWDfjr6sDfZ_KaOYnnn1GnoFn_9ND4P11Xp8K1YlvK4icW8Wywy0wwNktP11o6is3A3UeeidT22jYksWITs_be7PlwxEonp51cLp1qJTJ2SHjdCjYSLhNaVNYLfkmx5WLbFsFB-eE607B1HJXsiC6Y1yp6CT-WWBh184Gz7ToDgx9uTcdRWtef0jU-f7rv6QIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
کنایه‌های ژوله به سرماخوردگی عجیب رحمان‌رضایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108075" target="_blank">📅 15:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108074">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322ce18fa5.mp4?token=rUqDCnb7M4vXIg_aJDAEDFdbVfD3pRjXjcuai4CNg9bCmEdB9-MQEyeztdfiw18RFyBBFP2E-iUxMZXkknnzSrh7w5hoLcRgL_G3wbNRfkIXG3Ri1Zug9Y67UI5uYrGUnHm2oYeUyMmeW2Gwpo4z0MAewu4mZl9yNuVTk7NBToX-yHHMRtFC80L8u1zuSMRwUdZuhJZUeKoxI3K3pxas9pgBj_EAluPCWKuYG5SPbaLHY7p8g70Hg4TWXkGnIAswDS2q_enJNU-0t7lveKsO7Ai8t1qTPvvFiGCIa-HU3BS2vnGDBrxjcjFMmDxW1LVXkw1CmQCI6c6mmjpAUImjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322ce18fa5.mp4?token=rUqDCnb7M4vXIg_aJDAEDFdbVfD3pRjXjcuai4CNg9bCmEdB9-MQEyeztdfiw18RFyBBFP2E-iUxMZXkknnzSrh7w5hoLcRgL_G3wbNRfkIXG3Ri1Zug9Y67UI5uYrGUnHm2oYeUyMmeW2Gwpo4z0MAewu4mZl9yNuVTk7NBToX-yHHMRtFC80L8u1zuSMRwUdZuhJZUeKoxI3K3pxas9pgBj_EAluPCWKuYG5SPbaLHY7p8g70Hg4TWXkGnIAswDS2q_enJNU-0t7lveKsO7Ai8t1qTPvvFiGCIa-HU3BS2vnGDBrxjcjFMmDxW1LVXkw1CmQCI6c6mmjpAUImjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
هوادار تراکتور: عادل فردوسی پور دشمن خونی ماست و همیشه تیم‌مان را تحقیر می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108074" target="_blank">📅 15:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108073">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28665d2567.mp4?token=XikSFo-OPWEwWphoVQx9XXqGZ1K8bfNwFJcfWRQlqqNdnu_umMSPPytxs8IxmedmA8UjjggkSJSD40LexBJlhNJF3Netd41ej9p8IByMwE-RPT2CoNYoEEWCmARafyKd5-igz7dMqQjdN0sAV7k6KSCC6szCC6uTgiF1MeDLggzmZN3lo5A9LinESO6uNYe8WezYWMZlQNI7Vuze2s3S91JIVHsKN4WcTa9kSq-O6HMczoKnXzEhOgmOpf2Hq2i-c8AlKoIvuopNFJrHv5nJyNA0Rvm8IRerV-qrBs_LuJf1zoXEpISK_aeTgjBP8b0kB1ps8xIi3piMeA63W4SuQg02VV2EZIGZOGCqAb8cn6oOykuu3XId6TIw6zzBOtIVzR_xF5ffu0k_HRDIhECMGGu7QdjfcZQ3-KQAVaEVEijgKmyRSMPZBnOWO9UFK5tiCDidtBRVo6GcGxQKZ_LdCjPznRTSA8P18dr-0KYN_WSBfaVlHCXWFfwnAIPD1yPQ7SrKL9fGFYhhfjOwdM-qXLKpb2zsKJj0yXdP3Ddl-ejbLdZOLIOrwvVdnHpznWb7gghHIzS0-WGyAvrTUS2PyW670KHBbJj-hn0nW1dZffWYz-SiR5PJmkgAS0__xVQZe5nKln343k1S5shHAsz5zyd5VTV8p8wO2J2rePwpRaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28665d2567.mp4?token=XikSFo-OPWEwWphoVQx9XXqGZ1K8bfNwFJcfWRQlqqNdnu_umMSPPytxs8IxmedmA8UjjggkSJSD40LexBJlhNJF3Netd41ej9p8IByMwE-RPT2CoNYoEEWCmARafyKd5-igz7dMqQjdN0sAV7k6KSCC6szCC6uTgiF1MeDLggzmZN3lo5A9LinESO6uNYe8WezYWMZlQNI7Vuze2s3S91JIVHsKN4WcTa9kSq-O6HMczoKnXzEhOgmOpf2Hq2i-c8AlKoIvuopNFJrHv5nJyNA0Rvm8IRerV-qrBs_LuJf1zoXEpISK_aeTgjBP8b0kB1ps8xIi3piMeA63W4SuQg02VV2EZIGZOGCqAb8cn6oOykuu3XId6TIw6zzBOtIVzR_xF5ffu0k_HRDIhECMGGu7QdjfcZQ3-KQAVaEVEijgKmyRSMPZBnOWO9UFK5tiCDidtBRVo6GcGxQKZ_LdCjPznRTSA8P18dr-0KYN_WSBfaVlHCXWFfwnAIPD1yPQ7SrKL9fGFYhhfjOwdM-qXLKpb2zsKJj0yXdP3Ddl-ejbLdZOLIOrwvVdnHpznWb7gghHIzS0-WGyAvrTUS2PyW670KHBbJj-hn0nW1dZffWYz-SiR5PJmkgAS0__xVQZe5nKln343k1S5shHAsz5zyd5VTV8p8wO2J2rePwpRaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
مهدی تارتار، سرمربی پرسپولیس:
جام حذفی را می توانیم بدون ملی پوشان برگزار کنیم به جایش از جوان ها استفاده کنیم. مگر یک بار قشقایی پرسپولیس را حذف نکرد؟ چه اشکالی دارد که جام‌حذفی برگزار شود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108073" target="_blank">📅 15:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108072">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108072" target="_blank">📅 14:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108071">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b4e1c6b0.mp4?token=k-vy8Mt76KL8OmcXjzy3lUb3Ig44f1lF3r3M2UWodGsLyjjVbryu-QkZN1KJUwwHAhQkA0qwyRJfPpnbIP-bcicO3taUZZFSUrbQ2rwTvwoF8CqVGuapm8F_nTvsroPuBErgLDmqUfUE-o0SunsVwkTRewCiTiSAhzbSOyuW3z_85S8gDNP4tjjaVa6PMTt84B39EiN-OP9wR0hXW8fXXpvGre3wfrc8DIzkX9LG_mfWeQLExSzSHOvorArBubo083Y4Uw-Ojg48YwmW2UzA2A79jXmY4HiBcai4lqJgXDXcTCIFyxvdrZbWkrk9VJREN2FHQKQnVYJGFg8b4D9n7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b4e1c6b0.mp4?token=k-vy8Mt76KL8OmcXjzy3lUb3Ig44f1lF3r3M2UWodGsLyjjVbryu-QkZN1KJUwwHAhQkA0qwyRJfPpnbIP-bcicO3taUZZFSUrbQ2rwTvwoF8CqVGuapm8F_nTvsroPuBErgLDmqUfUE-o0SunsVwkTRewCiTiSAhzbSOyuW3z_85S8gDNP4tjjaVa6PMTt84B39EiN-OP9wR0hXW8fXXpvGre3wfrc8DIzkX9LG_mfWeQLExSzSHOvorArBubo083Y4Uw-Ojg48YwmW2UzA2A79jXmY4HiBcai4lqJgXDXcTCIFyxvdrZbWkrk9VJREN2FHQKQnVYJGFg8b4D9n7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
هوادار تراکتور: استقلال و پرسپولیس در تبریز کلا ۱۰ نفر هوادار دارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108071" target="_blank">📅 14:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd3638bac.mp4?token=sGUiuskBdDVfZxVPSL8mUVF2chE265-YM81Q5uWUhjiaevY8FvJFxxLhubUCbnDDn3Q_SMFu45sjhynNmZEHlP9OuXmkwDKn0upXEno7Nji4JjCB2b6xH9BiVUtXZwe_t7rSQS2UKB5w1GpS_3AYf_P9V-nxgWyH20JNpKpyVVOtgP3IKu0bdToyvqpSfVYv0x-jKct6hXx6u6ts7lqq87B_9t9TuZGI2PV9gZHm57kQ7RxIROxG4rLcPFJ0AIRTvWDOc8eJZ8Ipz4sQXE15aD_uhPjZW8xpBTBSYAIYPKrEaMuK0fErGCN9gEVRAMi0PheSqnb0YqwTkWMa6bUQlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd3638bac.mp4?token=sGUiuskBdDVfZxVPSL8mUVF2chE265-YM81Q5uWUhjiaevY8FvJFxxLhubUCbnDDn3Q_SMFu45sjhynNmZEHlP9OuXmkwDKn0upXEno7Nji4JjCB2b6xH9BiVUtXZwe_t7rSQS2UKB5w1GpS_3AYf_P9V-nxgWyH20JNpKpyVVOtgP3IKu0bdToyvqpSfVYv0x-jKct6hXx6u6ts7lqq87B_9t9TuZGI2PV9gZHm57kQ7RxIROxG4rLcPFJ0AIRTvWDOc8eJZ8Ipz4sQXE15aD_uhPjZW8xpBTBSYAIYPKrEaMuK0fErGCN9gEVRAMi0PheSqnb0YqwTkWMa6bUQlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
❌
🇮🇷
🇮🇷
هوادار تراکتور تبریز: ما مثل استقلال تهران گدایی جام نمی‌کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108070" target="_blank">📅 14:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ایجنت یاسر‌آسانی: اسناد منتشر شده در دقایق‌اخیر که با ادعای مدارک فسخ آسانی با استقلال است، کاملا فیک و ساخته هوش‌مصنوعی است و اعتباری برای هیچ نهاد حقوقی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108069" target="_blank">📅 14:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu388EVPg9OewlS1u_MPyypgEKYqquWrCBiDgh9KqevYR-3FlTarBqh54EQ7HpL-a6AfxZbNXiXUADYAgfLA_QNcfKJby53hdUEILF06fpb-F19pNXRsjuiguqMDOlRYQrJog5nVK6yIplR4paKVKKPrAop5eJYaQVnSvMvLz95zPdMRVjhO1EEfcMGKid9XuHyB3jQOL4HVTs45cA2mSEaGaz59y3E2wKOjg54d36HiiKKt170r6QcctpTVSIGYorWXBsBhuh8Hf_6cT6FpegQr1OC2Vg95_MYRw9q4sQ-SH05uJ7xRHwm9dtiSxMm4SNOEdDa_QOuSDSgy_yWsyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ایجنت یاسر‌آسانی: اسناد منتشر شده در دقایق‌اخیر که با ادعای مدارک فسخ آسانی با استقلال است، کاملا فیک و ساخته هوش‌مصنوعی است و اعتباری برای هیچ نهاد حقوقی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108068" target="_blank">📅 14:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syvdPhcYQSdrSShdbRhknl_qw5qs8OFrCm4KSu_3-d_2vinbYCgoiPGUm_zDcRWuXbFKlF0sHwKI6EIUfGnk3HGNwTXkaOzTv9Z3AsR4TX3pK6eiR_8Xh15K58sXe1mDp7n3Mr4BxxlGYV87_yUMjyorGDEFzjYly3oBu2EtOxJKbuX5ECktLZk9-8cbCfF8w5SBUpUpleWj0dGe8z8oan-4C4Gi6J0OzRhTm-n5Rkiz8kBWPaUm8JKfj37w8VmJFEqLz3NFiBg6hRSXwuQeJhEUAsmd6M0qkyygD8m937UCf0iC8GVbgRO7s6i8RIsmnrPIKc5TKEujbZbOe-9zGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
‼️
روزنامه‌SER: در روزهای اخیر درگیری میان چند بازیکن در رختکن رئال‌مادرید شکل گرفته و مورینیو کنترل رختکن را مشابه فصل قبل و دوران آربلوآ از دست داده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108067" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💥
🔥
خانم دوناجان وایلد، در سن 61 سالگی، رکورد جهانی طولانی‌ترین مدت نگه‌داشتن حالت پلانک (تمرین شکم) را برای زنان با ثبت زمانی 5 ساعت، به نام خود ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108066" target="_blank">📅 14:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a13616851.mp4?token=DJiR1LLPANmRWzRUxH_taCkCeTfc4Y_1c6W43M_h45KSGTL_qSi060IqCmf7AxdNJq5v_Bh4aWBiWsP8Zg28tp6hXWN_HrGLJXe1qJ7I5z2vLnX5YUWu2TAZV4Ej--FbT-DclVnbSpXj-Yb9kfjVDth2n7rvoDFsic-hb98MBksA_eLKuKfWOgEabIyY1E956xCP-neTxEp4oVPiS782UQk3Wa3h7_IUisIpSjW_jm8_2jq4P3GpptIfg4O2Pm5Go1RaPEprQcYy6yEi5yugU2XiyqaQUor-4-fkhA1NhJt6ivjYmmqw36oVJfCocB11utgpZ4gaJJw1zQLljkEODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a13616851.mp4?token=DJiR1LLPANmRWzRUxH_taCkCeTfc4Y_1c6W43M_h45KSGTL_qSi060IqCmf7AxdNJq5v_Bh4aWBiWsP8Zg28tp6hXWN_HrGLJXe1qJ7I5z2vLnX5YUWu2TAZV4Ej--FbT-DclVnbSpXj-Yb9kfjVDth2n7rvoDFsic-hb98MBksA_eLKuKfWOgEabIyY1E956xCP-neTxEp4oVPiS782UQk3Wa3h7_IUisIpSjW_jm8_2jq4P3GpptIfg4O2Pm5Go1RaPEprQcYy6yEi5yugU2XiyqaQUor-4-fkhA1NhJt6ivjYmmqw36oVJfCocB11utgpZ4gaJJw1zQLljkEODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
خلاصه حواستون باشه موقع خرید آیفون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108065" target="_blank">📅 14:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdjHUHQCI7rupdBGWcwwjodIfYLtm9MvxLNO_Vo1_xEd3I7tIDffCiLBf_-TMeBaNaYzWK2zKhqprNDJTf_gMbnOmVmeHNVbK51RRz2KwKBopRWdI35ud-l0cuDaTCP6zqwu0Bo3cbLIH-1Q1I1iBkgES-cIjf_i6SbjXBSMSHFE7-m83qQK_VUm-v_bYONLPCg1u7VgERFLspvF2jE8046qySCCoJVzjphp81vIDjfwOF68zNVBccrOj8wWsza0p1lmHouk-L_vv8fafZC2EhYwGO1QF56ftCGFG2AH8Ub18199gTWpvTZU1S3Eduou9dec_U7cvTECQpAl0Ti5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا در فاصله دو روز تا بازی ختافه در تمرینات امروز تیم بارسلونا غایب بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108064" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9ae65408.mp4?token=YcHmTjgjF9AB46NvpVnfIAIEB5M-Y5_H5D7OklZ7EbWl13Bv97tDRrD81dAiMU-hYRd6IQtUv_4MAwkBV-OVDH1P8fr3L4XUNyWkLbcHr4danpBpUvlSA7FX5ORj4pqwal_PekMxWFLbYmsYqM8J5sUwcDC1W_j2CwmT7xYyfunmPnY5QgXQmD1f7yxGdm5oljomjcwX0DL_2RDyhu_TZ6oBwPyRUwabFEJlcSUnJCJGUa28MzEV9mMWEv_RAOTPgxhSzairToVN7YNC7e7cWDuInEoLoVNhF9fw_tM3Drs72QQ5eKcqAAr0cw9V0bPRZTd4zBCnFMmJLjwv-93IHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9ae65408.mp4?token=YcHmTjgjF9AB46NvpVnfIAIEB5M-Y5_H5D7OklZ7EbWl13Bv97tDRrD81dAiMU-hYRd6IQtUv_4MAwkBV-OVDH1P8fr3L4XUNyWkLbcHr4danpBpUvlSA7FX5ORj4pqwal_PekMxWFLbYmsYqM8J5sUwcDC1W_j2CwmT7xYyfunmPnY5QgXQmD1f7yxGdm5oljomjcwX0DL_2RDyhu_TZ6oBwPyRUwabFEJlcSUnJCJGUa28MzEV9mMWEv_RAOTPgxhSzairToVN7YNC7e7cWDuInEoLoVNhF9fw_tM3Drs72QQ5eKcqAAr0cw9V0bPRZTd4zBCnFMmJLjwv-93IHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
تئوری کشته شدن وینیسیوس صحت داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108063" target="_blank">📅 13:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoBpRI7IN3m3LJ_ew1EJjvwknNyDIuuDppifeC9SM0jwj0Yp6YqnwOHuAEte-HDlQHuo30vZoUx7j8iJRfrFqjqG2d7sdwJ6wPrnfyvnd-0q7VPowujZWAiSR_nNKVNWzzx-PZnQM7NVhNo7Z9c-VF0k-OPw0QyBrcz4h-bKkh5jRBUx6_MvwUbk7Lsp1-ynk-XXf8ITPF8GrS4eEOlSXuirG9GMgCmMzexrlKzJjJKQ8MxmYwGxnGpimkWH51nZXpQYU37aAT3AVhrWKIxS4A8-xVLma9y_18v_Klec15mNIUqp1mc_5zoaKtF2m9fbRyOd0QMStKZ1rPUh2WLHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه بازی بعدی رو می‌دونی؟
👀
تو
آی‌اسپورت
بازی رو ببین، پیش‌بینی کن، امتیاز بگیر و برای جایزه رقابت کن!
🎁
🔥
👇
همین حالا پیش‌بینی کن
همین حالا پیش بینی کن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108062" target="_blank">📅 13:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKDpU7330GN5TQ2tnHZ5YlgP-wk1PvuEKxHCDdt9x05Pz0jrTQd-ERnMzmtqk-3OWtpttNHg6qWBmkuoHcq6I3t6Swdd2e6F9KpUpYr6UqD5AJzbuMUORrcjXNpguPnyVYnfrT4rFSZ-BdcvQJ9mjlucB3ETN5KgsAp1LAq8lIDOjRKWYwxUCZX7rVHRbqJoKjUmcDcRUKrgz5uqat9thnxTkzomyh_K8L6-LySjK3cNwRSjaKCsDT0k9Pwhp8EMjGz9q11lisLIQYH9bQQKNTbY1furin07W7Ax1FV3gg-JcFPwt--sY3esjGSrTJOChFnQkUhYceiJPteiJioqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا در مسیر جاودانگی، از برزیل تا کرواسی
؛ لاروخا رکورد باورنکردنی ۴۲ بازی متوالی بدون شکست را به ثبت رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108060" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108059">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1507fa12f.mp4?token=ogiYx2vIMp4gJRhHnR41Jhz5_3dNlFlWFMQY3LzFzRan_rviAAktUiTycRSJxm7KOGfiP38UonEr6kEzJUiIVNj-vWNuP3HwBN6F9Dl5IkZO0RGE_yS2CID_sFiBh4Kx-eVdEd6_0hzucPyXlVKLdE9bl5kqaPSKtgYaidUXAOk3O16T_QwuzAcq2JRT62pxpjKdQpe6AoK8-4Vr4S2OZAb1FnjdoPb9TeqV7jhO2lKuzgxK-Ho3tcka1H5d7BLtLgP2Vk_bn6qUphKfPG2C8rvJIkRQjh4SBOY2ihh5ud0X_Xj9PqyRRrlcab8YqSKKeBdaH-J4VR5uhU3BTgxAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1507fa12f.mp4?token=ogiYx2vIMp4gJRhHnR41Jhz5_3dNlFlWFMQY3LzFzRan_rviAAktUiTycRSJxm7KOGfiP38UonEr6kEzJUiIVNj-vWNuP3HwBN6F9Dl5IkZO0RGE_yS2CID_sFiBh4Kx-eVdEd6_0hzucPyXlVKLdE9bl5kqaPSKtgYaidUXAOk3O16T_QwuzAcq2JRT62pxpjKdQpe6AoK8-4Vr4S2OZAb1FnjdoPb9TeqV7jhO2lKuzgxK-Ho3tcka1H5d7BLtLgP2Vk_bn6qUphKfPG2C8rvJIkRQjh4SBOY2ihh5ud0X_Xj9PqyRRrlcab8YqSKKeBdaH-J4VR5uhU3BTgxAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
محرم نویدکیا سرمربی سپاهان: هواداران و شرایط اقتصادی را درک می‌کنم و این که من به عنوان سرمربی از آن‌ها بخواهم با این قیمت دلار و گرانی به ورزشگاه‌ها بیایند خیلی جالب نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108059" target="_blank">📅 12:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e684a43eea.mp4?token=k-yyJAg2SexTA1k2XU8J0UIBxYU1mJCGx7qt49mc4QDpVXw5p5otWFpX37_WxmPJFkNoIiu9fvY5pUG76Zt-5CwA8AvXpxP-NcGBJYgEfmfiTg7bYdU5kviX0KiXJBJToPNhHtZeQZA08EZVsv4GbngDIlX-IBZBYUW31Ob-DZ3GPuG27M7QRtbfe5UEJ0P142n3D9QpafX4crpArHYyCv5IR-6k9Awz4v2C4gdOGLGvDCtw7GLKmQBRaEjoKtEO_Bb6umYh1xuEw8hFi6OdtemieqHW5MBdueq88-ABVFlZdkIOef5Ghr1bb0kF5TrigOqTej0FZisFRFX6f5qR43ZzoUXg_ncO7LbYZ_-ZWv_wwWPU7rRlLMA7Gd4ew0ux-at5b20P6THIiJWjMQnm_tFI1k7Ztu5kqBPaxOwgAXve7MnRxCpcRtqsCaLf7ApTN2DmbN8KMg-SsyuLvkNJ-rZK6b5ECiWfafa69egQphJIGo3qOAqn9SuNM0GiSoyEzbfrPQZ50AaIpsH1XOMCXibjezhlcuFba324QQ3RhKTtRjkN4wFap1QhTNKY5QjfjIZ5coeYvqUMyx7q0BQtb93SrWff4Lftp-gmqvROP6Rwf2nH264-ft2m38PkFFPwLvr5Ru6OSIHsq4sonb0oxJqKuFHynrks0bFi7oV7rtY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e684a43eea.mp4?token=k-yyJAg2SexTA1k2XU8J0UIBxYU1mJCGx7qt49mc4QDpVXw5p5otWFpX37_WxmPJFkNoIiu9fvY5pUG76Zt-5CwA8AvXpxP-NcGBJYgEfmfiTg7bYdU5kviX0KiXJBJToPNhHtZeQZA08EZVsv4GbngDIlX-IBZBYUW31Ob-DZ3GPuG27M7QRtbfe5UEJ0P142n3D9QpafX4crpArHYyCv5IR-6k9Awz4v2C4gdOGLGvDCtw7GLKmQBRaEjoKtEO_Bb6umYh1xuEw8hFi6OdtemieqHW5MBdueq88-ABVFlZdkIOef5Ghr1bb0kF5TrigOqTej0FZisFRFX6f5qR43ZzoUXg_ncO7LbYZ_-ZWv_wwWPU7rRlLMA7Gd4ew0ux-at5b20P6THIiJWjMQnm_tFI1k7Ztu5kqBPaxOwgAXve7MnRxCpcRtqsCaLf7ApTN2DmbN8KMg-SsyuLvkNJ-rZK6b5ECiWfafa69egQphJIGo3qOAqn9SuNM0GiSoyEzbfrPQZ50AaIpsH1XOMCXibjezhlcuFba324QQ3RhKTtRjkN4wFap1QhTNKY5QjfjIZ5coeYvqUMyx7q0BQtb93SrWff4Lftp-gmqvROP6Rwf2nH264-ft2m38PkFFPwLvr5Ru6OSIHsq4sonb0oxJqKuFHynrks0bFi7oV7rtY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
نورافشانی فوق‌العاده ورزشگاه مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108058" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c30835c72.mp4?token=M1BAo-oMi0F5NGTgawEXqoGAAkqBeEECHYX15qksbSvASaIHj32dSKBx-jpEgP_4XH31YMgDs3z6bptJ5DwNSTa0qStjJdiKaPUM6YLwngdIeNHDrs2OOxAnx1I99Zz_HfQjFRiSc2uslNTJNq34kUcxvMF8GzqLb9ho4AD0ENG3vwRD5p1W7XJo9AQ0HHbjr9Tl9BjzaPEiL7hAzOMKAt5RrZFiZ2sHzH4D9CsrEmu5NYU6tyQGvjgCznIhW22G2KOyP4QOOCiE9MyqVK-TWBqV5vwqlNsVQnzorCCbJNJdow-wtbLvp2So6n4v2SEH_fIEdg_aYdPKosB38KOMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c30835c72.mp4?token=M1BAo-oMi0F5NGTgawEXqoGAAkqBeEECHYX15qksbSvASaIHj32dSKBx-jpEgP_4XH31YMgDs3z6bptJ5DwNSTa0qStjJdiKaPUM6YLwngdIeNHDrs2OOxAnx1I99Zz_HfQjFRiSc2uslNTJNq34kUcxvMF8GzqLb9ho4AD0ENG3vwRD5p1W7XJo9AQ0HHbjr9Tl9BjzaPEiL7hAzOMKAt5RrZFiZ2sHzH4D9CsrEmu5NYU6tyQGvjgCznIhW22G2KOyP4QOOCiE9MyqVK-TWBqV5vwqlNsVQnzorCCbJNJdow-wtbLvp2So6n4v2SEH_fIEdg_aYdPKosB38KOMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🔥
🔥
پایان یک افسانه ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108057" target="_blank">📅 11:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108056">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6399207329.mp4?token=cGt81soMtqOMmA6_l8ToL6FbfvFRsU77KkXygLrYVgVgGu24RVoiUomrztZdthrXN3y_ehasXs0X2RDNiOsiVylZ_XXcHDRQdzfLdgwTw9zugrtTB_leOJgS0oS4lZ3eDEzd_FdbO5Mqv_99BNWAN_v5x7NcgY3166ZuISPXU1TfYmnufky8EysE6hu_7nGaBFgPYU82k9e4Lwq-BuiyWeppAz2hWzHy1vij-8ZgcohtcU9CtdBNiR-4H7LiCjCIY8BOWMSAUOf5Dm5nXJRUgL8jg3lv5YeMM23togY0ceSXMVvu3sLlJBYG_nV831Fe04LAILB2jxFzbEf-MkOtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6399207329.mp4?token=cGt81soMtqOMmA6_l8ToL6FbfvFRsU77KkXygLrYVgVgGu24RVoiUomrztZdthrXN3y_ehasXs0X2RDNiOsiVylZ_XXcHDRQdzfLdgwTw9zugrtTB_leOJgS0oS4lZ3eDEzd_FdbO5Mqv_99BNWAN_v5x7NcgY3166ZuISPXU1TfYmnufky8EysE6hu_7nGaBFgPYU82k9e4Lwq-BuiyWeppAz2hWzHy1vij-8ZgcohtcU9CtdBNiR-4H7LiCjCIY8BOWMSAUOf5Dm5nXJRUgL8jg3lv5YeMM23togY0ceSXMVvu3sLlJBYG_nV831Fe04LAILB2jxFzbEf-MkOtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
زیدان محبوب‌ترین فرد در فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108056" target="_blank">📅 11:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37d8d2b4.mp4?token=WNdcej6VGGnaDDR4beQrIwEWx3nF4AN01FK0oDh8CX7db190LphR_1FTXAwkUNdfy2DzIGqF_T9yU_UqVaIFqiES9PPcdZ5BdSTEUzZWHQLFYIT9-FYxxKPhurMd6OvjlZSJ56Gt1i9SGs71Lq2UDLBqHIeQnkG0hHuxO9uys7S0wGUMlO5ZrlwbW7FmLPFlWazB75I9jeWx5GP7cVhM3cah6zJZ1K2XHWv2GnQAc8uVWIr7aZd5hdJHxRfik7GWgl7xbXf-WByT1m-kZg2bAfcLG2hxdPTc_rQZnLBQ7lZBx82tA2h2hfmIxH9YUUIn1EqoMjurutF2m6VaTMgUTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37d8d2b4.mp4?token=WNdcej6VGGnaDDR4beQrIwEWx3nF4AN01FK0oDh8CX7db190LphR_1FTXAwkUNdfy2DzIGqF_T9yU_UqVaIFqiES9PPcdZ5BdSTEUzZWHQLFYIT9-FYxxKPhurMd6OvjlZSJ56Gt1i9SGs71Lq2UDLBqHIeQnkG0hHuxO9uys7S0wGUMlO5ZrlwbW7FmLPFlWazB75I9jeWx5GP7cVhM3cah6zJZ1K2XHWv2GnQAc8uVWIr7aZd5hdJHxRfik7GWgl7xbXf-WByT1m-kZg2bAfcLG2hxdPTc_rQZnLBQ7lZBx82tA2h2hfmIxH9YUUIn1EqoMjurutF2m6VaTMgUTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آقا جمشید حسابی سوژه هوش‌مصنوعی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108055" target="_blank">📅 11:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
🙂
ماجرای لقب حمید بلان از زبان حمید مطهری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108054" target="_blank">📅 11:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880aca12e8.mp4?token=vaSCPqdKqqgEhCtBY5k6sz-FYRSsgyrqmXji8e0qRZAHUyk7jXdkS3ICZ_QIPij5zkrFzU68hy9De-CWQ1wEQT3fsXQundBTC7re3_WigIYN6G18Nkr0HBBqouSt6L6f3ae8aYxT1tciUKm0iw8Rmj1ExKmHyOlbx0mSbffvLelzDOeqrFrpBejS4KQPuvb6CGg3x_WjvFTLH1cL7FmJGZFmRh4xh0pSMSkVOms_AFlV5DcEbnyiJs97Vz8oZYQprBKvwatRyO9wrYmpKp-ige7YZSYokH28XuIvrn6kCwXIIEvpmsoIJW4Gr6NEKI1qKLAphhDp4CoAyMVbAwhurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880aca12e8.mp4?token=vaSCPqdKqqgEhCtBY5k6sz-FYRSsgyrqmXji8e0qRZAHUyk7jXdkS3ICZ_QIPij5zkrFzU68hy9De-CWQ1wEQT3fsXQundBTC7re3_WigIYN6G18Nkr0HBBqouSt6L6f3ae8aYxT1tciUKm0iw8Rmj1ExKmHyOlbx0mSbffvLelzDOeqrFrpBejS4KQPuvb6CGg3x_WjvFTLH1cL7FmJGZFmRh4xh0pSMSkVOms_AFlV5DcEbnyiJs97Vz8oZYQprBKvwatRyO9wrYmpKp-ige7YZSYokH28XuIvrn6kCwXIIEvpmsoIJW4Gr6NEKI1qKLAphhDp4CoAyMVbAwhurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دلیل نتیجه نگرفتن تیم امیرخان مشخص شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108053" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108052" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108052" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6lEMElmMbg93uyTvwvMauwa_7f5R5NKlJn5alkaUwnShwNsT7fLTx0ZY3XoWeeBx7uUJMgHAmf8NkKTihOZvqRvZiwq8oogzuPOSLUXARJrOfqb-uBi_LJCX4Y_faQ_lw5lszhvuhtsXVvjTSOiwa_DUqAxxv31gwVVkD1Y_0VJP-kdLpOBX-tMwSkjIIqNu3V7VyYJZgQnQ_4eqk63R36s5aksuVskbKypdqtMHwWkEwnyccaUHK1VyHROXsN6Xen2BsKSawmG9GUp-SaFvbuAH0PHv1NOafPBI63YctLzQoT7exWlcbavpgaChMaM9zmZ8YpKWIZKd_x1s92WPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108051" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6152c3dc5.mp4?token=S4CCplfwL5qRCfhTdSXlIsJMmQLnBsLlGDVb9lIQARA0FOWGCOLuEBhJw5-oUU18Dgrdhv5n9rjQCFH82ws7tAP-FOLr8Tf6e4bVfp4w7S_Ku25uU6w2Z4OZZBHo55dR6FGSukymwHkAYalhmVrpTl1LWtCJ1XdoLES_wVf4vYslcZqbK9zLxvLOoDq2TwqLo1T22IzlcTtTtwtd87vuHtE9vyLFSZ1HkcSJ94xwYr0QpqzGArrFvL_C4d0BmFjjXRJUPAuC8WvncgQ2NeZK22uSjBgcE_9El3GpyRW3N7S_Gl152z7vKJ9KozLr4vH4k8VW1PPyWAGN1NOxb_lqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6152c3dc5.mp4?token=S4CCplfwL5qRCfhTdSXlIsJMmQLnBsLlGDVb9lIQARA0FOWGCOLuEBhJw5-oUU18Dgrdhv5n9rjQCFH82ws7tAP-FOLr8Tf6e4bVfp4w7S_Ku25uU6w2Z4OZZBHo55dR6FGSukymwHkAYalhmVrpTl1LWtCJ1XdoLES_wVf4vYslcZqbK9zLxvLOoDq2TwqLo1T22IzlcTtTtwtd87vuHtE9vyLFSZ1HkcSJ94xwYr0QpqzGArrFvL_C4d0BmFjjXRJUPAuC8WvncgQ2NeZK22uSjBgcE_9El3GpyRW3N7S_Gl152z7vKJ9KozLr4vH4k8VW1PPyWAGN1NOxb_lqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
استارت بهانه‌های نکونام: بازیکن نداریم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108050" target="_blank">📅 10:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22eef45598.mp4?token=ULFbPhfMGbiuOLLdUhw9K5okidCxwbx53jOPcgk32NrrgoHTbUjxaAGtk7QT49XkMOD-SSsoOIlzATWsyjBIfdo7u94uUy90lAoGgQi4z5BwNfXJbJ_qh8YzrA-cUmEPTYS8RbwYSYINNcQoTrTQHZGRTxggPX6D-wKyi1k56FRtsUQASZT-f7hA-gJwcb_3q304VtKqmA8NYSM8oV5l8nqcpGgArJI4onxfzE1rGZGj1I9Z7Xy-U4IGqJcpyVOkea2V6s29XGW_PF8WrpqYOUcVL3oPRSADD_2qg364Ssp-l-5MMcYo_n4WWN3ObdviIpkPnhvqpL_C3CVHaIF5KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22eef45598.mp4?token=ULFbPhfMGbiuOLLdUhw9K5okidCxwbx53jOPcgk32NrrgoHTbUjxaAGtk7QT49XkMOD-SSsoOIlzATWsyjBIfdo7u94uUy90lAoGgQi4z5BwNfXJbJ_qh8YzrA-cUmEPTYS8RbwYSYINNcQoTrTQHZGRTxggPX6D-wKyi1k56FRtsUQASZT-f7hA-gJwcb_3q304VtKqmA8NYSM8oV5l8nqcpGgArJI4onxfzE1rGZGj1I9Z7Xy-U4IGqJcpyVOkea2V6s29XGW_PF8WrpqYOUcVL3oPRSADD_2qg364Ssp-l-5MMcYo_n4WWN3ObdviIpkPnhvqpL_C3CVHaIF5KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
❌
پیروز قربانی: آقای دبیر احترامت واجبه اما فوتبال ما دست فوتبالی‌ها نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108049" target="_blank">📅 10:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd5wA5nlhiVD3d_5_7Rhdq3WoB9mtB8F4OAif6qVBiUXJDhm3b3AnQU0fzuOCK14CQZKitA_NLpa1wpjRbJ-wlHulUP1bh5Z93af4f_OBXN9dIW1A88SCGUbpwNy6rciL9CkrtojVVdIyuN4hCqw88dfMAgTWOT9uuE-p_sXtW5la4BinKCvuKDpM65iM23HwPhdPZ9U9Uz8cVeagYbl67lid68jWxggLQwFupTl3987yFMj0leJgcBwjQ87S25KuUZqflT8BNICYp696_2faIlzWx5l-wr4aLsFepJfRyoIk4t0QG9ITAyoXJRXoYIcfulN_cWnAEl4ppz4UOu3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🚨
‼️
بیلد المان :
⚽️
بایرن مونیخ آماده است برای جذب دنی اولمو اقدام کند. بارسلونا ارزش این هافبک را حدود ۸۰ تا ۹۰ میلیون یورو تعیین کرده است. با این حال، هنوز هیچ پیشنهاد رسمی‌ای ارائه نشده و اولمو هیچ قصدی برای ترک بارسلونا ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108048" target="_blank">📅 10:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
🎙
افشاگری عجیب عادل فردوسی‌پور: همه از بازیکن کمیسیون می‌خواهند، حتی فدراسیون! سهم ۵۰۰ میلیاردی فدراسیون از قراردادها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108047" target="_blank">📅 09:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddf4bbda24.mp4?token=fmC9TcPF4KAffnCK5IJTn2DEL8Xb_O3REg2k5B4e_YXR0Sy0xmpf6yetj8TbQhumJpO3gQHrnofcyqxhRJdB3V1dRZiwLhkNHmqYjoBXeGWeVb5BIgODxZQt0YFZ-fWr_PzmrbzsMbcTDcnqDvoxhjnkuIg0ubw0zGmFvIWvcT-gy4K3eFlpN1Fb8k7i4SX8E6kj4ob-PhGv9ONkuKOA-9Vns0V7hrOOd1zM7SW6BTnmxQNFzLRfBmBJX8xW6CtFqCTg9gS1TpZZOtvVvaji2JLC0tKq7YR7kp3XDT4X5ZKGMkZTeoxut0h6TdKqOWWBscLip-eUxVZjxZYpYLr_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddf4bbda24.mp4?token=fmC9TcPF4KAffnCK5IJTn2DEL8Xb_O3REg2k5B4e_YXR0Sy0xmpf6yetj8TbQhumJpO3gQHrnofcyqxhRJdB3V1dRZiwLhkNHmqYjoBXeGWeVb5BIgODxZQt0YFZ-fWr_PzmrbzsMbcTDcnqDvoxhjnkuIg0ubw0zGmFvIWvcT-gy4K3eFlpN1Fb8k7i4SX8E6kj4ob-PhGv9ONkuKOA-9Vns0V7hrOOd1zM7SW6BTnmxQNFzLRfBmBJX8xW6CtFqCTg9gS1TpZZOtvVvaji2JLC0tKq7YR7kp3XDT4X5ZKGMkZTeoxut0h6TdKqOWWBscLip-eUxVZjxZYpYLr_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‼️
🇮🇷
صحبت‌های قابل تامل پیروز قربانی درباره وضعیت کشور و‌ فیلترینگ؛ از من سرمربی چه توقعی دارید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108046" target="_blank">📅 09:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d9f01002.mp4?token=luaOttXWocTc7rRLJ8oY5ELmGdynzryeVVjpQtni6iGpx3zA64WxJSacvR8zNvg7PTp3k1ufp299jwQm80sKAE_blyN0UQeoRmMyGHF119ZHfZ5GYpw0e3Io3nDGhqAobxbqVw1o1e3WOI21Z3OrrS4NfewDYxbDNn-q77ccS1HVKLZFqVHpv9Asv54yJSfT-FLeikbTmnikr9I2yu9yEoWFTHwoB_4HJSIVBtJbSdUt1Od9EpmfA0Kf3vhkVCEdnYrlDm2KFB1RSpWFk0we8wFtty0CYflUjQM3-rBJJZbZFfuvLtPA-XDdaugw7jacW-JfjMCCOdWflA16xbuiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d9f01002.mp4?token=luaOttXWocTc7rRLJ8oY5ELmGdynzryeVVjpQtni6iGpx3zA64WxJSacvR8zNvg7PTp3k1ufp299jwQm80sKAE_blyN0UQeoRmMyGHF119ZHfZ5GYpw0e3Io3nDGhqAobxbqVw1o1e3WOI21Z3OrrS4NfewDYxbDNn-q77ccS1HVKLZFqVHpv9Asv54yJSfT-FLeikbTmnikr9I2yu9yEoWFTHwoB_4HJSIVBtJbSdUt1Od9EpmfA0Kf3vhkVCEdnYrlDm2KFB1RSpWFk0we8wFtty0CYflUjQM3-rBJJZbZFfuvLtPA-XDdaugw7jacW-JfjMCCOdWflA16xbuiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
⚽️
کنایه تند روزگذشته نکونام به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108045" target="_blank">📅 09:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108044">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dbe528e3d.mp4?token=ZTf0KXSGFNPlE08pXBavStpAjSkwgNvL3d0rUQ9KUI0VZkyiL-kyzEgeHrg41iuo5Y0rQlfoq8msj-buoSEZ8dgeTR05K4Lve27lAv08CUwwlzTJBBCEgSpKBDpqMcDIYpgm6etsqnsAAWrngTb0K4V-ERp6nIpwPM3V9jBDT90RG0rTpW5Y4t39RJ8LNFBQ6Bze_459LQvpgMR7kzkyK4CzCZqqOn-DESNzOPza4PhxcuX85xtYAShsVxl4uoBVm6utt9-Fa6HK8eLQhHQhzU856rNyvtZ8s_HwvETjVwgpSLDFH7n93PnONfSz_cN9X90y0bTIGNKFUT6EPUFl5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dbe528e3d.mp4?token=ZTf0KXSGFNPlE08pXBavStpAjSkwgNvL3d0rUQ9KUI0VZkyiL-kyzEgeHrg41iuo5Y0rQlfoq8msj-buoSEZ8dgeTR05K4Lve27lAv08CUwwlzTJBBCEgSpKBDpqMcDIYpgm6etsqnsAAWrngTb0K4V-ERp6nIpwPM3V9jBDT90RG0rTpW5Y4t39RJ8LNFBQ6Bze_459LQvpgMR7kzkyK4CzCZqqOn-DESNzOPza4PhxcuX85xtYAShsVxl4uoBVm6utt9-Fa6HK8eLQhHQhzU856rNyvtZ8s_HwvETjVwgpSLDFH7n93PnONfSz_cN9X90y0bTIGNKFUT6EPUFl5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
واکنش تند نادر قاضی‌پور به سوال مجری درباره محمدرضا زنوزی؛ مالک تراکتور: «این همه پول از کجا آورده؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108044" target="_blank">📅 08:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108043">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108043" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108042" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108041" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ceb61fe00.mp4?token=mMLUNK1m7A0EDwoeCgYkNUqlOUOVjRv1XzI2XnHoTN1VcHBjrYmIiqIyibYP-0vWooyoY-GfxBaiNXYQVVqhUdh9JVvKZgXQ3O7RL1To9hYSKhbmWaCXPBSOwq5EcHIUCPP_erGz_4gQhfIweNX3kX7bv6qCz8QWIUgSN0qql82xB2u5-g4c7hTz_Fa-cVu_E4HHcUkNy4UzpHYyjd8aiBpcAgQIv4sTLOKqHZ2c3z87mv_WnxH2Z2IHv6aEPRZ9Fn-MIw1iLObLnM1mA0r1MAQ62Bp2c98x8ggB8EV-bDN71Pe9KAuOHLatEIMAvYqvdScteUscoGoAUO1XdLI7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ceb61fe00.mp4?token=mMLUNK1m7A0EDwoeCgYkNUqlOUOVjRv1XzI2XnHoTN1VcHBjrYmIiqIyibYP-0vWooyoY-GfxBaiNXYQVVqhUdh9JVvKZgXQ3O7RL1To9hYSKhbmWaCXPBSOwq5EcHIUCPP_erGz_4gQhfIweNX3kX7bv6qCz8QWIUgSN0qql82xB2u5-g4c7hTz_Fa-cVu_E4HHcUkNy4UzpHYyjd8aiBpcAgQIv4sTLOKqHZ2c3z87mv_WnxH2Z2IHv6aEPRZ9Fn-MIw1iLObLnM1mA0r1MAQ62Bp2c98x8ggB8EV-bDN71Pe9KAuOHLatEIMAvYqvdScteUscoGoAUO1XdLI7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های تلخ امی‌مارتینز حین تماشای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108040" target="_blank">📅 00:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">احساسی‌شدن دیشب آنتونلا‌ و فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108039" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11ce2c532.mp4?token=SY7ZxPnzFr-M3O9BVE_MiPQa4R2mC61FEKbfJxq0LcegyxwvcWTEQXrNUlr917S-Hf_hQx0mf31iVCXK4UMqPi964jxWP_Je44orgWwomM3ZcDXgEgGpiVnaabRQrVSYCanA0-COC285uYL8aCE6eK07Y8MKZB2yycy1nhmQqL37j5JNCLzSv-vUMn4gL1ElV33vpqjF8Zm7Do-_Nwo0ws6wcc7xeuJmuPQaya2L6PGSAzHUSd4sVagwn3J88bbmY4wxnzvxEca8lS4t2KDkbpvWZ4raJvS8Y6QUvSlzjxK6iic6IRWbtjaTSDaIfA0BxNJk3V3WzZXKZm8Q4K_ucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11ce2c532.mp4?token=SY7ZxPnzFr-M3O9BVE_MiPQa4R2mC61FEKbfJxq0LcegyxwvcWTEQXrNUlr917S-Hf_hQx0mf31iVCXK4UMqPi964jxWP_Je44orgWwomM3ZcDXgEgGpiVnaabRQrVSYCanA0-COC285uYL8aCE6eK07Y8MKZB2yycy1nhmQqL37j5JNCLzSv-vUMn4gL1ElV33vpqjF8Zm7Do-_Nwo0ws6wcc7xeuJmuPQaya2L6PGSAzHUSd4sVagwn3J88bbmY4wxnzvxEca8lS4t2KDkbpvWZ4raJvS8Y6QUvSlzjxK6iic6IRWbtjaTSDaIfA0BxNJk3V3WzZXKZm8Q4K_ucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
میانگین نمرات لیونل‌مسی در ۲۱ سال حضور ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108038" target="_blank">📅 22:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f285b4a4ed.mp4?token=jmRZNKXr7chjGPJO23Hsl0xiTbuB1U7qmOpqxox58dVwBdDwuVmAeJerKB0DZL0uBsRdR2ireFY--CdGQ04QdNVTVhyFV5vmewQumOpNPvbxeX849BzBgm7zm9eNWQ1sF1eAbcG2penO3JMJCpmutOJL1B21gqa3bK6_g427rrqA-uIJ5I5_3xG4x2-NvNS4yXPpTYkADJAObUyngE0aGUpJR1Fj29ZRnC5WvsFOVnf3qyOFOgjLJ5Gmlhn8PZJRWhBiknOVPjYpCEI7mrxONr6bBiFSn5dTgkHwesOGLcua5TS7IlRLM_XtjEa1yT_BTOTHQJF75wwPjCjiwGXnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f285b4a4ed.mp4?token=jmRZNKXr7chjGPJO23Hsl0xiTbuB1U7qmOpqxox58dVwBdDwuVmAeJerKB0DZL0uBsRdR2ireFY--CdGQ04QdNVTVhyFV5vmewQumOpNPvbxeX849BzBgm7zm9eNWQ1sF1eAbcG2penO3JMJCpmutOJL1B21gqa3bK6_g427rrqA-uIJ5I5_3xG4x2-NvNS4yXPpTYkADJAObUyngE0aGUpJR1Fj29ZRnC5WvsFOVnf3qyOFOgjLJ5Gmlhn8PZJRWhBiknOVPjYpCEI7mrxONr6bBiFSn5dTgkHwesOGLcua5TS7IlRLM_XtjEa1yT_BTOTHQJF75wwPjCjiwGXnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
فریاد بازیکنان آرژانتین در اتوبوس برای اسطوره مسی فریاد می‌زنند:
🔺
‏لیونل مسی، ما می‌خواهیم برایت بخوانیم،
‏تو جاودانه هستی، درست مثل شب قطر.
🔺
‏رفتن را متوقف کن، یک بار دیگر به این موضوع فکر کن، ‏این چیزی است که همه در استادیوم مونومنتال از تو می‌خواهند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108037" target="_blank">📅 22:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa857c27d9.mp4?token=Spr1BO4ELk8kMBb8m3C7Xv2VBvQehhdFxyZtOof8WM78fLYZHfCwSBKKUFY_yfRJhvNz_9tSWWvWqgWC-RKmV3Ltln0Gb6wSPX2d8XxyqSuSG4OSCeirHcQjj7MMAg14GvXVZI3uu9zfjtWIERTfog90aLcw47ApVacCFyXzL1zwOW6VBpxlQLZcTVw0yaU9dOYDQ7ag5TDFLW4ppmN7YZDjEZoU9K4kIfkhF0rxws2tzL-QEwt5IfWmnbKWT7QH3mOzTmlaxi-WmTa0GQleqOhRbfDpWmgHktSjY7OkEj6XkYvymq69MvDViee6d3daSrMz6oI2PbrJ4CuIkeF-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa857c27d9.mp4?token=Spr1BO4ELk8kMBb8m3C7Xv2VBvQehhdFxyZtOof8WM78fLYZHfCwSBKKUFY_yfRJhvNz_9tSWWvWqgWC-RKmV3Ltln0Gb6wSPX2d8XxyqSuSG4OSCeirHcQjj7MMAg14GvXVZI3uu9zfjtWIERTfog90aLcw47ApVacCFyXzL1zwOW6VBpxlQLZcTVw0yaU9dOYDQ7ag5TDFLW4ppmN7YZDjEZoU9K4kIfkhF0rxws2tzL-QEwt5IfWmnbKWT7QH3mOzTmlaxi-WmTa0GQleqOhRbfDpWmgHktSjY7OkEj6XkYvymq69MvDViee6d3daSrMz6oI2PbrJ4CuIkeF-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوبان‌عالم وقتی راجب تیم‌ملی حرف میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108036" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el3yqOMeeUJGBem2z3B56rpHqikO8Zl93c0pHL5Eq3FCuop8nSXiLzKGLBWCjvAVRhLFjhukaCn2xzUl7K4SIBI2c6DczyqFeOWOP3-rjaUtYsCelJvQXtd5sK2bP_bHxhSEiICss3XUd7OfgP3Wyt1RC8WaeBoA2clRkGIM8cxqQtOUf9O35YCgVgGOmZONwIFE6H-fvpdafWGWylK_VKKzx6B1nZxnZ_lC5cROvHGcBj-rPwK-RGEaJcyjSSdluLi95frih8ZD1bGGxaiP2cSdd7sBy7Btglz2Hdl4I2GMjEqJ016Dm2_bjH-5eyu1KDMOtqfeLaPcj8QPETOlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇪🇸
کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108035" target="_blank">📅 21:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb4f97376.mp4?token=TWY_LcZcQyjlWWeiW31AhIFVrR_GJ_AMiIcnk_jGN1zAnER6auFk-C95B0KQgiHxI8ykhDZzH3iqNbXgEz5eXUc0bURaOpDZrinrqGDHLyye2GWgR9GnDZPZTCR92DDVfNjKGvqchEoSPxWZVhxwDGpFHxr0ops7yMbBnSMgX_d5OuX3lBT8E7XCpmBXhsWJIPvoVmTUIg6IHtAMNyCIc_PYCjhSR9Fm9R7imA-7NwAOmOrChZ73zzLe0hAINAbxQbItudQjgMgdbOhUlph34S6eVCzPTUqud8hJrlStYhl2PUJdgLh2-sMIZ_5UanbUyMl5gPgmpUJx-pQ3VCSYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb4f97376.mp4?token=TWY_LcZcQyjlWWeiW31AhIFVrR_GJ_AMiIcnk_jGN1zAnER6auFk-C95B0KQgiHxI8ykhDZzH3iqNbXgEz5eXUc0bURaOpDZrinrqGDHLyye2GWgR9GnDZPZTCR92DDVfNjKGvqchEoSPxWZVhxwDGpFHxr0ops7yMbBnSMgX_d5OuX3lBT8E7XCpmBXhsWJIPvoVmTUIg6IHtAMNyCIc_PYCjhSR9Fm9R7imA-7NwAOmOrChZ73zzLe0hAINAbxQbItudQjgMgdbOhUlph34S6eVCzPTUqud8hJrlStYhl2PUJdgLh2-sMIZ_5UanbUyMl5gPgmpUJx-pQ3VCSYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره ابدی تاریخ فوتبال
❤️
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108034" target="_blank">📅 21:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c820a58fa5.mp4?token=Hjiv1md8I6ru8kJ6lQqYmg7m2UscCQfEFZXFiSb01BEHLqcSAFhQTUy5daAl5WID7V_2aCY8rQSdxgM_Zk0-3dlii6bCCoR3MO69z9gEnV-3DFjRMAffKbnxaPMy21t9esumtTyrErZ9LynkepmOy35z7_DRYbncEmP5_6uDtrgD0g0D4g1U7T45Ca2KrR-8m32ZNUE6KLKVLB-1muD_IGftTkT-6Qf8SxoWmec66gl4UD2U_hsa6CbKWUchDjiUgj-9MTu3trxJvaY5snaAns06PMFznhZ2VJjv1vXOzpHz0-_GIVSCkfdGFMie5Gv3I1CcGz3211Zn-1qQCeYywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c820a58fa5.mp4?token=Hjiv1md8I6ru8kJ6lQqYmg7m2UscCQfEFZXFiSb01BEHLqcSAFhQTUy5daAl5WID7V_2aCY8rQSdxgM_Zk0-3dlii6bCCoR3MO69z9gEnV-3DFjRMAffKbnxaPMy21t9esumtTyrErZ9LynkepmOy35z7_DRYbncEmP5_6uDtrgD0g0D4g1U7T45Ca2KrR-8m32ZNUE6KLKVLB-1muD_IGftTkT-6Qf8SxoWmec66gl4UD2U_hsa6CbKWUchDjiUgj-9MTu3trxJvaY5snaAns06PMFznhZ2VJjv1vXOzpHz0-_GIVSCkfdGFMie5Gv3I1CcGz3211Zn-1qQCeYywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان آرژانتینی‌ها بعد از آخرین جمله لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108033" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=aKGSPg238qGueLqVCJgqAd_YcUzz7xNQSeFBA966FtHcHwJnuLjS8-pqGkP0C8nQGLmLByLCvQ52q3no8dgru2s4cB7kwtz5t-IQNgoanrPSojRsEsZfQBadCRAJk7OfitZ1eHhc6swKEDLnKT7pFsdLo7X0y1unHSrQZwwndfCKcoBlyekj4MOJXFpv6lUOMqQ_ogdepiop0d9NNOUYl2ZvsvwO9kKAyEoaOwi_109bsr_BU3dEGTaNjf7HXyMQRKYUo9NdJUkf6r6U9aVznG8XkEKrerEOXLenjm0oiRTXxMQLS-zQdarNBNuVZ5JwLof0908bScX-gXwlDdHs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=aKGSPg238qGueLqVCJgqAd_YcUzz7xNQSeFBA966FtHcHwJnuLjS8-pqGkP0C8nQGLmLByLCvQ52q3no8dgru2s4cB7kwtz5t-IQNgoanrPSojRsEsZfQBadCRAJk7OfitZ1eHhc6swKEDLnKT7pFsdLo7X0y1unHSrQZwwndfCKcoBlyekj4MOJXFpv6lUOMqQ_ogdepiop0d9NNOUYl2ZvsvwO9kKAyEoaOwi_109bsr_BU3dEGTaNjf7HXyMQRKYUo9NdJUkf6r6U9aVznG8XkEKrerEOXLenjm0oiRTXxMQLS-zQdarNBNuVZ5JwLof0908bScX-gXwlDdHs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🥹
لیونل اسکالونی: "اون «جذبه» یا هاله‌ای که داره. من تو تمام عمرم چنین چیزی رو تو هیچ‌کس ندیدم. اون شور و حسی که مسی ایجاد می‌کنه رو تو هیچ‌کس دیگه‌ای ندیدم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108032" target="_blank">📅 20:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=LL5BLHnm1hqFm92b6C5qmh_K0q3U42sy8BLCBijSZeCoZ2KUKq43i45j_xwAv4fX94EMXLOZaVysFn7SeEe9dIksOMaXCPopntljTXid9SCtSPVSChCwSHijPw4qB5q-5cU7cKuE36L1D_wHD1vtnuRxUgu9StyHnluLvUIck3ByZX8YP_HoCy0WuC28tPVk26UOYu0-1yHLE6Vf5ydRs5IdYApAldcbUbFKlk2SoZbLFSGnNt_bcI4yLL-YVxqIGRZxfrJgDSPLnArKRVE4yWJVMxmJbShnflOiTnSf-enF9ftkE7-Xk4GSVAJrJjzFR962Gqffj7Es2iquS2Zk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=LL5BLHnm1hqFm92b6C5qmh_K0q3U42sy8BLCBijSZeCoZ2KUKq43i45j_xwAv4fX94EMXLOZaVysFn7SeEe9dIksOMaXCPopntljTXid9SCtSPVSChCwSHijPw4qB5q-5cU7cKuE36L1D_wHD1vtnuRxUgu9StyHnluLvUIck3ByZX8YP_HoCy0WuC28tPVk26UOYu0-1yHLE6Vf5ydRs5IdYApAldcbUbFKlk2SoZbLFSGnNt_bcI4yLL-YVxqIGRZxfrJgDSPLnArKRVE4yWJVMxmJbShnflOiTnSf-enF9ftkE7-Xk4GSVAJrJjzFR962Gqffj7Es2iquS2Zk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌ویژه ابوطالب به قشر دانشجویان عزیز
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108031" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98248b467.mp4?token=B7bTA0h8xU-C3R3U77hPDCh-ueLXcOxfYyhPOdtgJ_rhEbgBfDPmyoJUxky2Q9XPNR484UUjwO_I96dgme9_51twVUdCkeJmkQ7oDxKK967Zozok2BLYwCyFZeITw0WcIBrRF4H2MHtJfRcwF2-36AciTCRcjk32VMM6k74-7RUVuw08GG3u29mop_hzdYiOagyv1BryVm7741RE9nW6xkkZwv_HKcsvu8o7F5zTL3Z9KkspG0_a4-d8znmMmmM1Xf8n1Bnv_ZolzUwcXWb6VuHNv_vG0nE7Wfa40Nk6HadUDCkZlnq5rYZcr1v-p-0k8k5lDXZ3CYbm1dCPvUh0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98248b467.mp4?token=B7bTA0h8xU-C3R3U77hPDCh-ueLXcOxfYyhPOdtgJ_rhEbgBfDPmyoJUxky2Q9XPNR484UUjwO_I96dgme9_51twVUdCkeJmkQ7oDxKK967Zozok2BLYwCyFZeITw0WcIBrRF4H2MHtJfRcwF2-36AciTCRcjk32VMM6k74-7RUVuw08GG3u29mop_hzdYiOagyv1BryVm7741RE9nW6xkkZwv_HKcsvu8o7F5zTL3Z9KkspG0_a4-d8znmMmmM1Xf8n1Bnv_ZolzUwcXWb6VuHNv_vG0nE7Wfa40Nk6HadUDCkZlnq5rYZcr1v-p-0k8k5lDXZ3CYbm1dCPvUh0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«یه روزنامه از ۵۴ سال پیش…
تیترهاش حسابی آدمو به فکر می‌بره!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108030" target="_blank">📅 19:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjFcfpAKtILOAhjiiJlurwqWLEpEIc104SxTNzeiMRxeYhXMzayPOMEpl2XGvuVeLOScQ15l9m75ue4V8xwW5NPlv5tZLbyVS9EGNLTV5t-_nAR7YzPzqRBfWfKjS1ivM7vcbVajnGodZWZhNke-TmXiaQWgJT49TumpNfQDwqe-gWfhDk4zA9RuOfD-ouSQSf0lF_iIjS8VHfwMOTO1y6SUi4NCS6KwFb4zbuXoSaKKu4yCcpp0vl08gNyYJZuuxklC3sCSrHk2mRQBTAeoXctYH1Ezgw5IidQuzU2OhO0v1HJv5UhBRTugi_Qd0L-adlO8Vl2fdMw9EJFP_F5M-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
تمام 126 گل ملی لیونل مسی به تفکیک هر کشور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108029" target="_blank">📅 19:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=XP2Fz-yNC69kRCSxYzfSIPl3uR52-S8LL_nttD9oHHhS-ig24nf0ZbUz_ovRGIAEdbGT87bNli6sLIBrCr60Hs1-cnOrkl8BCod7UyUEeJeDt4kRoz8qJ-CXDDF_chuMm82bqe0x0Ct07qvYGoKdLG4qRL97CjSUZW0so3jBo4oYvPaiTVuwIiN6AwV07IjyM681H1G0_TDxjgvLN7DoptjDvbIjNFvKYE71_-l5LH5c9BgvywV4H-pKtaUkLqF4n4yS-r7lEPKtodbSv-8gH2jLtopdThf7UjpJYpApQR_vp9A9tNB5iLb2UA_8b0yzuLAXjLIpb4RjEtyeUpWjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=XP2Fz-yNC69kRCSxYzfSIPl3uR52-S8LL_nttD9oHHhS-ig24nf0ZbUz_ovRGIAEdbGT87bNli6sLIBrCr60Hs1-cnOrkl8BCod7UyUEeJeDt4kRoz8qJ-CXDDF_chuMm82bqe0x0Ct07qvYGoKdLG4qRL97CjSUZW0so3jBo4oYvPaiTVuwIiN6AwV07IjyM681H1G0_TDxjgvLN7DoptjDvbIjNFvKYE71_-l5LH5c9BgvywV4H-pKtaUkLqF4n4yS-r7lEPKtodbSv-8gH2jLtopdThf7UjpJYpApQR_vp9A9tNB5iLb2UA_8b0yzuLAXjLIpb4RjEtyeUpWjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اهدای تابلو فرش به صالح‌حردانی توسط تبریزی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108028" target="_blank">📅 18:54 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
